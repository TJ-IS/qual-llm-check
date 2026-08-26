---
otero_id: 28320
otero_key: "TFXNMKJS"
title: "When Sharing Economy Meets Traditional Business: Coopetition Between Ride-Sharing Platforms and Car-Rental Firms"
authors: "Chenglong Zhang; Jianqing Chen; Srinivasan Raghunathan"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# When Sharing Economy Meets Traditional Business: Coopetition Between Ride-Sharing Platforms and Car-Rental Firms

Chenglong Zhang,<sup>a</sup> Jianqing Chen,<sup>b,</sup>\* Srinivasan Raghunathan<sup>b</sup>

<sup>a</sup> School of Management and Economics, Chinese University of Hong Kong, Shenzhen 518172, China; <sup>b</sup> Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75080

Contact: zhangchenglong@cuhk.edu.cn, https://orcid.org/0000-0001-7547-4751 (CZ); chenjq@utdallas.edu, https://orcid.org/0000-0001-5907-2680 (JC); sraghu@utdallas.edu, https://orcid.org/0000-0002-2782-3520 (SR)

Received: January 6, 2022 Revised: October 10, 2022; April 16, 2023 Accepted: July 27, 2023 Published Online in Articles in Advance: October 3, 2023

https://doi.org/10.1287/isre.2022.0011

Copyright: © 2023 INFORMS

Abstract. We examine the coopetition relationship between a ride-sharing platform and a car-rental firm. A distinctive aspect of this coopetition relationship is that they operate under two different business models. The platform, exploiting information technology (IT) capabilities, controls its demand and supply sides by setting rider price and driver wage in real time based on demand and supply conditions. In contrast, the car-rental firm operates under the traditional model with a fixed supply and cost structure. Both the IT-driven platform and the car-rental firm compete for riders seeking for transportation. If the two engage in coopetition, they cooperate to allow a (secondary) driver to rent from the rental firm and drive for the platform. In the absence of coopetition, only those with their own vehicles (i.e., primary drivers) are allowed to drive for the platform. We show that such supply-side (i.e., driver-side) cooperation intensifies the demand-side (i.e., rider-side) price competition and decreases total revenue. Therefore, coopetition is mutually beneficial only when it leads to a significant decrease in the supply, or driver, cost. Moreover, when coope tition is mutually beneficial, the benefit arises solely because of the improved profit margin from riders who switch from the rental firm to the platform and from those who are switched from primary to secondary drivers. We find that the platform and the rental firm are likely to form a coopetition relationship when the total rider market size is not high, the degree of rider substitutability between the platform and the rental firm is low, or the platform has a significant market-size advantage over the rental firm. Coopetition between the platform and the rental firm benefits riders and hurts drivers, but benefits society overall. The incentive to form the coopetition relationship is enhanced if cross-side network effects are present on the platform or if each player serves a loyal rider segment in addition to the competitive rider segment that considers the two as substitutes.

History: Ram Gopal, Senior Editor; Hong Guo, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0011.

Keywords: sharing economy • coopetition • competition • frenemies • analytical modeling

## 1. Introduction

Information technology (IT)-driven two-sided platforms that operate under a sharing-economy model have proliferated across several industries in recent years. IT enables platforms to match demand and supply in real time. This matching is facilitated by accurate real-time market information, enabling platforms to control both demand and supply sides of the market through prices. The convenience and consumer-friendly features offered by these platforms have attracted a large consumer base. On the supply side, the ability to offer service-at-will has encouraged many providers to join platforms as well. Platforms are able to handle large consumer and provider bases and large transaction volumes at negligible additional cost because they rely on highly automated algorithm-based matching.

The rapid growth of two-sided sharing platforms has received significant attention from information-systems researchers and others interested in understanding the disruptions caused by novel phenomena and new busi ness models created and driven by IT developments. Studies in such industries as transportation, lodging, and labor markets (Cramer and Krueger 2016, Zervas et al. 2017) generally show that a sharing platform’s entry in an industry adversely affects existing firms operating under the traditional business model, suggesting that the platforms may have a competitive advantage over tradi tional firms. A key difference between sharing-economy and traditional business models is the self-scheduled nature of supply in the sharing model (drivers in the ride-sharing context) that allows platforms to dynamically control the supply quantity and cost using price (wage in the ride-sharing context). In contrast, a firm operating under the traditional business model typically has a long-term contractual relationship or commitment that prevents dynamic control of supply quantity and cost. Despite the differences in business models and potential competitive advantages of a sharing model over the traditional business model, we recently witnessed cooperation in the form of driver-side partnerships between ride-sharing platforms and car-rental firms that operate under a traditional business model. For instance, Uber formed partnership agreements with such car-rental firms as Hertz that allow drivers to rent vehicles from rental firms on special terms and drive for Uber (Eldredge 2017, Walmsley 2018, Uber 2019). Lyft has also entered into similar cooperation agreements with several car-rental firms under a program called ExpressDrive. Despite such agreements, Uber and Lyft still compete with car-rental firms for riders.<sup>1</sup> Thus, these agreements between ride-sharing platforms and carrental firms create simultaneous cooperation and competition between them, commonly referred to as coopetition.

A general sentiment among industry experts is that coopetition benefits both platforms and car-rental firms. From a platform’s perspective, it helps manage the supply-side challenges arising from the self-scheduling nature of drivers and enhances the driver supply (Walmsley 2018). For the rental firm, it is an opportunity to expand the rental market and demand for vehicles (Bomey 2017). Despite these obvious benefits to both sides, the value of the coopetition relationship between Uber/Lyft and car-rental firms remains unclear, and experts have offered diverse speculations on its impact.

The coopetition relationship between firms is not new. Coopetition is prevalent in many industries including electronics, automobiles, airlines, and pharmaceuticals (Dagnino 2009). The parties in a coopetition relationship are sometimes called frenemies (Adner et al. 2020). However, the feature that sets the coopetition between ridesharing platforms and car-rental firms apart is that they operate under two different business models—the platforms operate under the sharing-economy model, and the car-rental firms operate under the traditional model. Prior literature has examined coopetition between firms that operate under one (e.g., traditional) business model. However, coopetition between firms that operate under different business models is new and may have novel implications. In this paper, we seek to provide insights into whether and under what conditions coopetition benefits the platform and the car-rental firm and its driving forces. We also examine the impacts of such coopetition on other stakeholders such as drivers, riders, and society.

To focus on the strategic aspects of coopetition, we develop a parsimonious aggregate model of the ridesharing context that abstracts away the operational details. A platform and a rental firm compete for riders looking for transportation. Whereas the rental firm offers only the vehicle, the platform offers a vehicle and a driver. Renting a vehicle from the rental firm and driving it for the platform is prohibited when the platform and the rental firm are not in a coopetition relationship (Uber 2019), but is allowed under coopetition. The financial terms (i.e., rental price and wage) for drivers who rent from the rental firm and drive for the platform are set jointly (i.e. cooperatively) by the platform and the rental firm, consistent with prevailing practices in agreements between ride-sharing platforms and car-rental firms. In contrast, the platform and the rental firm set their prices for riders independently, and the platform alone sets the wage for drivers that drive for the platform without renting the vehicle from the rental firm.

We show that coopetition benefits the two firms only under some conditions. In fact, it intensifies the price competition and decreases the total joint revenue of the platform and the rental firm. Consequently, coopetition benefits only when it induces the platform to reduce the driver wage significantly, relative to what the platform would offer without the coopetition relationship. When coopetition is beneficial, despite the wage decrease, the platform realizes a smaller profit margin from the riders served by the primary drivers—those who own their own vehicles. Similarly, the rental firm realizes a smalle profit margin from the riders it serves. Altogether, we find that when coopetition is mutually beneficial, the benefit comes solely from the improved profit margin realized through redistribution of riders. Under coopetition, some riders switch from the rental firm to the plat form and some riders served by primary drivers are switched to being served by secondary drivers—those who rent a car from the rental firm and drive it for the platform. The former shift occurs because the platform decreases the price more than the rental firm does under coopetition; the latter shift occurs because the platform uses fewer primary drivers under coopetition.

We find that a coopetition relationship is more likely to form when the platform has a significant market-size advantage over the rental firm, the total rider market size is not high, or the degree of rider substitutability between the platform and the rental firm is low. In other words, the value of coopetition (defined as the joint profit when the platform and the rental firm use the coopetition strategy minus the joint profit when they do not) is high in these cases. The primary reason for this set of findings relates to how the market conditions affect the firms’ incentives to shift riders from the rental firm to the platform under coopetition. For instance, intuitively, an increase in the platform’s market-size advantage is associated with an increase in the relative value of the platform’s ride sharing service or a decrease in the relative value of the rental firm’s service. In the absence of coopetition, an increase in the market-size advantage increases the platform’s price and decreases the rental firm’s price, thus increasing the price differential between them, which makes shifting the riders from the rental firm to the platform more valuable for the two firms.

Coopetition between the platform and the rental firm benefits the riders and hurts the drivers. The benefit to riders stems from the more intense price competition between the platform and the rental firm and hence a lower price. The drivers are hurt overall because of the smaller wage offered to primary drivers. We note that the overall driver surplus is lower despite the surplus gain enjoyed by secondary drivers under coopetition. Social welfare improves under coopetition because more consumers use the platform, which provides a higher value than the rental firm (i.e., the platform provides a vehicle and a driver whereas the rental firm provides only a vehicle).

Finally, we find that cross-side network effects on the platform (i.e., an increase in the supply increases the demand and vice versa) have a positive influence on coopetition: A stronger cross-network effect, on either the demand side or the supply side, increases the likelihood of a coopetition relationship between the platform and the rental firm. Analogously, the presence of loyal rider segments that would choose either the platform or the rental firm only also enhances the likelihood of coopetition between the platform and the rental firm.

The rest of the paper is organized as follows. Section 2 reviews the relevant literature. Section 3 introduces our baseline model. We analyze the competition between a platform and a rental firm in Section 4 and then derive the conditions under which the two firms have incentive to form a coopetition relationship in Section 5. Section 6 presents several model extensions. Section 7 discusses managerial implications and concludes.

## 2. Literature Review

This paper is closely related to and contributes to two streams of literature: sharing economy and coopetition. Research on sharing economy is recent and this stream has focused on the operational and informational aspects of two-sided platforms and the economic impacts of the sharing economy on various stakeholders. This research has generally found that the introduction of sharingeconomy platforms negatively affects firms operating under traditional business models (Martin et al. 2010, Zervas et al. 2017). For instance, Zervas et al. (2017) examine the economic impact of Airbnb on the traditional lodging industry and find that hotels’ average revenue decreases between 8% and 10% because of Airbnb’s entry, with the lower priced hotels being more severely affected. Fraiberger and Sundararajan (2015) show that peer-to-peer Internet-enabled rental markets enhance consumer welfare. Cohen and Sundararajan (2015) and Friedman (2014) study the regulatory aspects of the sharing economy. Burtch et al. (2018) find that the entry of gig-economy platforms has different impacts on low- and high-quality entrepreneurial activities. Several papers have examined the optimal price and wage schemes for a monopoly sharing platform under different market conditions (Taylor 2018), and some have studied price competition between ride-sharing platforms (Zhang et al. 2022). Weber (2014) studies moral hazard in the sharing economy.

Although we also study the sharing economy’s strategic and economic aspects, we focus on the coopetition phenomenon whereas the extant literature has studied either a monopoly platform or two competing platforms. Our work’s key contribution to the sharing-economy literature is that the findings extend our understanding of the role of the self-scheduled nature of supply and its novel implications in sharing-economy contexts. More generally, this research highlights the need to examine existing strategies and theories in the sharing-economy context because of its distinctive characteristics absent from traditional business models. Furthermore, our results highlight how coopetition can be a tool for traditional firms to mitigate the disruptions caused by the entry of firms that operate under the sharing-economy model. As a sharp contrast, although a few papers also noted the potential benefit of the sharing economy to traditional industries (Jiang and Tian 2018, Abhishek et al. 2021), the benefit does not stem from the traditiona industry’s use of cooperation as a strategic tool.

The second related stream is the extensive research on coopetition. In their seminal book on this topic, Brandenburger and Nalebuff (1996) describe coopetition using a pie metaphor. Specifically, they view coopetition as a strategy in which firms first cooperate to bake the largest possible pie and later compete with each other to take the largest slice of the pie. Following the publication of this book, several articles examined the coopetition phenomenon. Much of the coopetition literature has used a qualitative case-study approach and a resourcebased framework. In this framework, coopetition is used as a strategy for firms to pool their resources to create new innovations from which the firms can later appropriate value. A few papers have studied coopetition using analytical models. Banker et al. (1998) examine how cooperation in investments to improve product quality could affect the subsequent price competition. Granot and Sosˇic ´ (2005) study the formation of Internetbased supply exchanges where competing companies form online alliances and share supply. Nagarajan and Sosˇic ´ (2007) study the stability of such cooperation and examine the impact of market size, degree of competi tion, cost parameters, and demand-process visibility on prices, inventory levels, and market structure. Granot and Yin (2008) investigate competition and cooperation among component suppliers in an assembly system.

Recent work has also examined coopetition involving platforms. Chen and Guo (2022) examine why a large online retailer (e.g., Amazon) would open its retailing platform to small third-party sellers, providing the insight that recently available low-cost advertising could be a driving force because third-party sellers could advertise elsewhere and compete with the retailer anyway. Song et al. (2021) examine, in the presence of a spillover effect of consumer awareness, third-party sellers product offering on a large retailer’s platform and the effect of the spillover on equilibrium partnership. Mantena and Saha (2012) study coopetition between twosided platforms by focusing on the effect of technology asymmetry between platforms on the incentives to collaborate. Adner et al. (2020) show that a partnership is likely to be formed between two competing platforms when they have different profit foci. Cohen and Zhang (2022) examine coopetition between two ride-sharing platforms and show that a well-designed contract ensures benefit from coopetition.

Our work departs from the existing coopetition literature in an important aspect. Much of the prior work assumes that cooperation leads to a new or higher quality product or service enhancing consumer utility, allowing firms to compete for consumers in a larger market (i.e., a larger pie in the pie metaphor). In our context, consumer utility and market size are unaffected by cooperation. Essentially, the product offered to (and seen by) consumers is unchanged by cooperation. Furthermore, we examine coopetition between firms that operate under different business models—one operates under the sharing-economy model, and the other operates under a more traditional model. Thus, one important contribution of this paper to the coopetition literature lies in the identification of a novel impact of coopetition that departs from the standard pie metaphor and arises from the distinctive characteristics of the sharing-economy model.

In particular, we articulate two underlying mechanisms of the novel impact of coopetition and how the sharing-economy model generates these novel impacts. First, the platform’s ability to adjust wage based on demand and supply under the sharing-economy model is vital to coopetition’s success. If the platform operates under a fixed wage as in the traditional business model, coopetition would never emerge in the equilibrium. Second, without any market expansion, the redistribution of riders and drivers, which is also enabled by the dynamic matching of the IT-driven sharing-economy model, serves as a primary driving force for coopetition success. Specifically, we find that some riders switch from the rental firm to the platform under coopetition and they are served by secondary drivers. Also, because the platform lowers the wage offered to the primary drivers under coopetition, some primary drivers quit and their would-be-matched riders are served by secondary drivers under coopetition. These two types of redistributed rider–driver pairs contribute high profit margins, whereas the profit margins from the previous matching pairs decrease under coopetition.

## 3. Model

Consistent with our goal of examining the strategic impacts of coopetition between firms that operate under two different business models, we adopt a parsimonious aggregate model of the transport service context for our analysis. We consider a platform, $S ,$ that operates under the sharing-economy model and connects riders with drivers, such as Uber, and a rental firm, $R ,$ that operates under the traditional business model, such as Hertz.

## 3.1. Demand/Riders

A rider’s transportation need could be satisfied by either the platform or the rental firm. When a rider uses the rental firm, she would drive the vehicle herself; when she uses the platform, the platform provides a vehicle and a driver. Given prices $p _ { S }$ and $p _ { R }$ charged to riders by the platform and the rental firm, respectively, the platform and rental-firm demands are given by

$$
\begin{array}{l} {d _ {S} = a + \delta - b (p _ {S} - p _ {R})} \\ {d _ {R} = a - \delta - b (p _ {R} - p _ {S}).} \end{array}\tag{1}
$$

In this model, the total rider market size (equal to 2a) is captured by parameter $a > 0 .$ . We refer to $\delta \in ( - a , a )$ as the market-size differential between the platform and the rental firm. The parameter $\delta ,$ although we make no assumption about its sign, is likely to be nonnegative, because the platform provides convenient services with a vehicle and driver at a rider’s location whereas the rental firm provides only a vehicle at specific locations. The parameter b captures the degree of substitutability between the platform and the rental firm from a rider’s perspective.

Following the procedure used in the existing literature (Kwark et al. 2014), the demand function in Equation (1) can be derived using microeconomic utility-based assumptions about rider behavior. Briefly, we consider 2a riders in the market with heterogeneous preferences regarding their ideal transportation mode.<sup>2</sup> We model their preferences using a Hotelling model with the platform located at zero and the rental firm at one. A rider has a valuation $v _ { S }$ for the platform and $v _ { R }$ for the rental firm. We denote a rider’s misfit cost per unit distance as t. Following the standard procedure for computing the demands of the competing firms in a Hotelling model of consumer preferences—by assuming full market coverage, identifying the indifference point, and computing the platform’s (rental firm’s) demand as the riders to the left (right) of the indifference point—we obtain Equation (1) where $b = a / t$ and $\delta = ( v _ { S } - v _ { R } ) a / t$

The demand functions represented by Equation (1) model the scenario in which all riders view the platform and the rental firm as imperfect substitutes and the market is fully covered. We use this scenario for the main analysis for expositional clarity and to highlight the competition element of the coopetition relationship. In Section 6.2, we consider a more general scenario in which the platform and the rental firm have their own loyal rider segments, in addition to the competitive rider segment choosing between the two, and in which the market is not fully covered. We show that the results of the main analysis continue to hold qualitatively in the more general scenario.

## 3.2. Supply/Drivers for the Platform

The driver supply for the platform may consist of two driver segments: (i) the drivers who have their own vehicles, which we refer to as the primary driver supply, and (ii) those who do not have a vehicle, which we refer to as the secondary driver supply. The secondary driver supply exists only when the rental firm cooperates with the platform by allowing individuals to rent from the rental firm and drive for the platform. In this case, we say that the rental firm and the platform are in a coopetition relationship because they still compete for riders.

We assume that the driver segments are static in the sense that each driver belongs to one of the two segments and cannot switch from one to the other. Several factors contribute to this setup. First, financial conditions, the primary reason a driver belongs to a specific segment, do not change in the short term.<sup>3</sup> Moreover, rental contracts for secondary drivers are typically long term. Second, for a driver that already owns an eligible vehicle that is available for ride sharing, renting an additional vehicle and using it for ride-sharing service is unlikely to offer a superior payoff, considering the additional costs on top of the costs associated with owning a vehicle (e.g., insurance and maintenance); it is uncommon in practice for drivers with available vehicles to use a rental vehicle to offer ride-sharing service.

A driver is more willing to drive for the platform if the wage is higher. We denote the wage offered by the platform to primary drivers using their own vehicles as $w _ { S } .$ The primary driver supply available to the platform is given by

$$
q _ {S} = \alpha (- k + l w _ {S}),\tag{2}
$$

where $k > 0 .$ . The supply function implies that the wage must be strictly positive and greater than $k / l$ to ensure a positive supply. Analogously, we denote the wage offered by the platform to the secondary drivers as $w _ { S R }$ and assume that the secondary driver supply available to the platform is

$$
q _ {S R} = \beta (- k + l (w _ {S R} - p _ {S R})),\tag{3}
$$

where $p _ { S R }$ is the price charged by the rental firm to secondary drivers. The net wage of a secondary driver is $( w _ { S R } - p _ { S R } )$ , whereas it is $w _ { S }$ for a primary driver. Our supply models capture the relative populations of drivers owning and not owning vehicles by α and $\beta ,$ respectively. The total driver supply for the platform is $q _ { S } + q _ { S R }$ in the presence of the coopetition and is $q _ { S }$ in its absence.

## 3.3. Game Timing

In the game’s first stage, the platform and the rental firm decide whether to form a coopetition relationship. If they decide to form such a relationship, they collectively decide the wage and price, $w _ { S R }$ and $p _ { S R } ,$ for the secondary drivers, determining the net wage, ${ w _ { S R } } - p _ { S R }$ . In the second stage, the platform decides the rider price, ${ p } _ { S } ,$ and the wage, $w _ { S } ,$ for the primary drivers, whereas the rental firm decides price, $p _ { R } ,$ for its riders.

The timeline is consistent with empirical observations. For example, according to Uber (2019), Uber offers differential net wages for primary and secondary drivers by offering different promotions applicable to different driver types.<sup>4</sup> Moreover, the promotions applicable to drivers that rent from a rental firm and drive for Uber are in accordance with Uber’s specific agreements with rental firms. Analogously, Zipcar charges differential rental rates for normal renters and those who drive for Uber (Zipcar 2020). Moreover, the promotions and rental rates applicable to secondary drivers are preannounced (Zipcar 2020).<sup>5</sup> These observations suggest that the secondary drivers’ net wage is determined jointly by the platform and the rental firm.<sup>6</sup> The first stage is the cooperation stage because the platform and the rental firm together decide the net wage for secondary drivers if they decide to form a coopetition relationship. Whether or not they decide to cooperate in the first stage, the two firms engage in price competition for riders in the subsequent stage. Our game sequence implies that the platform uses the dynamic-commission-rate (DCR) scheme (Zhang et al. 2022). The bulk of the extant literature on ride sharing examines this scheme as it offers the most flexibility to the platform to match demand and sup ply. In Section $^ { 6 , }$ we also examine a model variation in which the platform decides $w _ { S R }$ and the rental firm decides $p _ { S R }$ separately to optimize their own profits in the first stage and a model variation in which the platform adopts a fixed-commission-rate scheme. We find that the qualitative insights of this paper continue to hold.

We assume a fixed, exogenous marginal cost, $c ,$ for the rental firm because the rental firm operates under the traditional business model. Conversely, the wage the platform pays the drivers, which is its cost, is endogenous and determined by the platform because it operates under the sharing-economy model. We normalize drivers’ cost (other than the price paid by secondary drivers to the rental firm) to zero. In Section $6 ,$ we examine a model extension by considering that primary drivers incur a positive cost and show that the main results carry over. We assume that the values of model parameters are in reasonable ranges such that both firms have positive profits in both the no-cooperation and cooperation cases.

## 4. Analysis of the Competition Stage

We use subgame-perfect equilibrium as the solution concept and use backward induction to derive the equilibrium. Depending on whether the platform and the rental firm cooperate in the first stage, the equilibria differ in the two subgames in the competition stage. We use superscripts N and $C ,$ respectively, to indicate the no-cooperation and cooperation scenarios.

For the platform, a transaction happens only when a rider is matched with a driver. Therefore, the transaction volume on the platform is the minimum of its demand and supply. If the platform and the rental firm do not cooperate, then the platform has only the primary driver supply. Thus, the platform’s and rental firm’s profits in the second stage in the no-cooperation scenario are given by

$$
\begin{array}{r l} & {\pi_ {S} ^ {N} = (p _ {S} ^ {N} - w _ {S} ^ {N}) \mathrm{min} \{d _ {S} ^ {N}, q _ {S} ^ {N} \}} \\ & {\pi_ {R} ^ {N} = (p _ {R} ^ {N} - c) d _ {R} ^ {N}.} \end{array}\tag{4}
$$

If the platform and the rental firm cooperate, then the platform has both the primary and secondary driver supplies. If it chooses $w _ { S } \leq w _ { S R } ,$ the platform would use all available primary drivers and use secondary drivers to meet excess demand; the reverse happens otherwise. Thus, the platform’s profits in the cooperation scenario are

$$
\pi_ {S} ^ {C} = \left\{ \begin{array}{c c} p _ {S} ^ {C} \min \{d _ {S} ^ {C}, q _ {S} ^ {C} + q _ {S R} ^ {C} \} - w _ {S} ^ {C} \min \{q _ {S} ^ {C}, d _ {S} ^ {C} - q _ {S R} ^ {C} \} \\ - w _ {S R} ^ {C} q _ {S R} ^ {C} & \text {if} w _ {S R} ^ {C} \leq w _ {S} ^ {C} \\ p _ {S} ^ {C} \min \{d _ {S} ^ {C}, q _ {S} ^ {C} + q _ {S R} ^ {C} \} - w _ {S R} ^ {C} \min \{q _ {S R} ^ {C}, d _ {S} ^ {C} - q _ {S} ^ {C} \} \\ - w _ {S} ^ {C} q _ {S} ^ {C} & \text {otherwise.} \end{array} \right.\tag{5}
$$

The rental firm’s profits in the cooperation scenario are

$$
\begin{array}{l} \pi_ {R} ^ {C} = \\ \left\{ \begin{array}{l l} (p _ {R} ^ {C} - c) d _ {R} ^ {C} + (p _ {S R} ^ {C} - c) q _ {S R} ^ {C} & \text { if } w _ {S R} ^ {C} \leq w _ {S} ^ {C} \\ (p _ {R} ^ {C} - c) d _ {R} ^ {C} + (p _ {S R} ^ {C} - c) \min \{q _ {S R} ^ {C}, d _ {S} ^ {C} - q _ {S} ^ {C} \} & \text { otherwise }. \end{array} \right. \end{array}\tag{6}
$$

When $w _ { S } ^ { C } < w _ { S R } ^ { C } ,$ the demand from secondary drivers for the rental firm is either the total available secondary driver supply or the number of unmatched riders remaining after the match with primary drivers, whichever is smaller (i.e., min $\{ q _ { S R } ^ { C } , d _ { S } ^ { C } - q _ { S } ^ { \dot { C } } \} )$ ), because the platform would use all available primary drivers first to serve riders.

Whether or not the platform and the rental firm cooperate in the first stage, the platform chooses the price charged to riders, ${ p } _ { S } ,$ and wage offered to primary drivers, w<sub>S</sub>, and the rental firm chooses the price charged to riders, $p _ { R } ,$ simultaneously in the second stage. In the case of cooperation, $p _ { S R } ^ { C }$ and ${ w _ { S R } ^ { C } }$ would have already been decided prior to this stage. Depending on the values of $p _ { S R } ^ { C }$ and ${ w _ { S R } ^ { C } } ,$ , any of the following three cases is possible in the competition stage: (i) the platform uses only primary drivers to match with riders, (ii) the platform uses only secondary drivers to match with riders, or (iii) the platform uses both primary and secondary drivers to match with riders. The first case is equivalent to the no-cooperation scenario. Furthermore, we show in the proof of Lemma 1 that the second scenario is dominated by the third scenario when the platform and the rental firm choose to cooperate. Consequently, for the cooperation scenario, we focus on the case when the platform matches both primary and secondary drivers with riders.

In equilibrium, regardless of whether the platform and the rental firm cooperate, the platform matches its demand with supply. We note that the transaction volume for the platform is equal to the minimum of demand and supply. Intuitively, if the demand exceeds the supply for the platform, the transaction volume is equal to the number of drivers. In this case, if the platform offers the same wage and increases the rider price a little bit, it could have the same transaction volume and a higher profit margin and profit. Thus, demand cannot exceed supply for the platform in equilibrium. Similarly, supply cannot exceed demand in equilibrium because the platform could increase the profit by decreasing the wage by a small amount. Lemma 1 shows the prices and primary-driver wage in the competition stage for the case when supply matches demand for the platform.

Lemma 1. In the competition stage, the equilibrium price and wages under the no-cooperation and cooperation scenarios are given by the following.

(i) In the no-cooperation scenario,

$$
\begin{array}{l} p _ {S} ^ {N *} = \frac {6 a b + 3 a \alpha l + 2 b ^ {2} c + \alpha b c l + 2 b \delta + 2 \alpha b k + \alpha \delta l}{b (2 b + 3 \alpha l)} \\ w _ {S} ^ {N *} = \frac {3 a l + b c l + b k + 3 \alpha k l + \delta l}{l (2 b + 3 \alpha l)} \\ p _ {R} ^ {N *} = \frac {4 a b + 3 a \alpha l + 2 b ^ {2} c + 2 \alpha b c l + \alpha b k - \alpha \delta l}{b (2 b + 3 \alpha l)}. \end{array}\tag{7}
$$

(ii) In the cooperation scenario,

$$
\begin{array}{l} p _ {S} ^ {C *} = p _ {S} ^ {N *} - \frac {4 \beta (- k + l (w _ {S R} - p _ {S R}))}{2 b + 3 \alpha l} \\ w _ {S} ^ {C *} = w _ {S} ^ {N *} - \frac {3 \beta (- k + l (w _ {S R} - p _ {S R}))}{2 b + 3 \alpha l} \\ p _ {R} ^ {C *} = p _ {R} ^ {N *} - \frac {2 \beta (- k + l (w _ {S R} - p _ {S R}))}{2 b + 3 \alpha l}. \end{array}\tag{8}
$$

We can verify that an increase in the total market size, $a ,$ increases the rider prices charged by the platform and the rental firm (i.e., softens the rider-side competition, whether or not the platform and the rental firm cooperate). The impact of the total market size on price competition is intuitive because an increase in the total market size increases the demand for both the platform and the rental firm, ceteris paribus. On the supply side, an increase in the total market size increases the wage offered by the platform to its drivers. The platform would need more drivers to satisfy the demand increase resulting from an increase in the total market size. Conversely, an increase in the market-size differential δ increases the platform’s price but decreases the rental firm’s price, whether or not they cooperate, because it enhances the platform’s market size but diminishes the rental firm’s size.

Under cooperation, an increase in $( w _ { S R } ^ { C } - p _ { S R } ^ { C } )$ decreases the rider prices charged by the two firms and the wage offered by the platform to its primary drivers. This is because an increase in $( w _ { S R } ^ { C } - p _ { S R } ^ { \bar { C } } )$ increases the secondary driver supply, which decreases the platform’s need for drivers from the primary driver supply; therefore, the platform decreases their wage. Moreover, the increase in the total driver supply pushes the platform to compete more intensely for riders on price which causes both the platform and the rental firm to reduce rider prices. Whereas the qualitative impacts of $a , \delta ,$ and $\dot { ( } w _ { S R } ^ { C } - p _ { S R } ^ { C } )$ on the platform and the rental firm are monotonic, the degree of substitutability between the platform and the rental firm $( \mathrm { i . e . , } b )$ could have nonmonotonic effects on them as shown by the following proposition.

Proposition 1. With or without cooperation, a higher degree of substitutability between the platform and the renta firm always decreases the price charged by the rental firm, decreases the price charged by the platform if and only if

$$
4 b ^ {2} \left(p _ {R} ^ {X *} - p _ {S} ^ {X *}\right) <   \alpha l (3 a + \delta) + 2 b (a - \delta),\tag{9}
$$

and increases the wage offered by the platform to primary drivers if and only if

$$
w _ {S} ^ {X *} <   \frac {c}{2} + \frac {k}{2 l},\tag{10}
$$

where X � N for the no-cooperation case and $X { = } C f o r$ the cooperation case.

A well-established result in the literature is that an increase in substitutability between horizontally differentiated firms intensifies the price competition between them in a traditional marketplace. The negative effect of b on the price charged by the rental firm is consistent with this result. However, Proposition 1 shows that this well-established result does not always hold in our setting when one firm operating under the sharingeconomy model competes with another operating under the traditional business model. Condition (9) implies that when the platform charges a lower price than that of the rental firm in a scenario—cooperation or no cooperation— $\cdot ( \mathrm { i . e . , } p _ { S } ^ { X * } < p _ { R } ^ { X * } )$ , the platform’s price might increase in substitutability. Only when Condition (9) is satisfied does the price decrease. The platform can exploit an increase in demand from a price decrease only if it increases the supply by increasing the wage it offers to drivers. That is, an increase in b affects not only the demand, but also the supply side for the platform. From Condition (10), the platform would increase the wage when b increases if the primary drivers’ wage, and therefore the primary driver supply, is small enough such that increasing it is not too costly. When $( p _ { R } ^ { X * } - p _ { S } ^ { X * } )$ is positive and large such that Condition (9) does not hold, the platform enjoys a high demand and offers a high wage. If b increases under this condition, the platform has no incentive to reduce its price and increase the already high demand because it has to increase its marginal cost (i.e., wage) to attract a large driver base, which is costly. However, the unit cost of supply is fixed and unaffected by b for the rental firm. Thus, an increase in b causes it to decrease its price.

We present Conditions (9) and (10) in Proposition 1 in an implicit form for compactness and readability. Substitution of equilibrium wage and price expressions stated in Lemma 1 into those conditions reveals that the plat form’s equilibrium wage, $w _ { S } ^ { X * }$ , either increases or decreases in the substitutability, depending on whether Condition (10) is satisfied. Conversely, the platform’s equilibrium price $p _ { S } ^ { X * }$ can either always decrease in the substitutability or follow a U-shape (i.e., decrease when the substitutability is less than a threshold and increase when the substitutability is greater than the threshold). Moreover, we find that the latter behavior occurs when the substitutability on the supply side, l, is sufficiently large.

Next, we examine how cooperation in the first stage affects the subsequent price competition between the platform and the rental firm and the wage offered by the platform.

## Proposition 2.

(i) Cooperation between the platform and the rental firm in the first stage intensifies the price competition between them in the second stage (i.e., $p _ { S } ^ { N * } > p _ { S } ^ { C * }$ and $\dot { p } _ { R } ^ { N * } > p _ { R } ^ { C * } )$

(ii) The price decrease due to cooperation is greater for the platform than for the rental firm (i.e., $p _ { S } ^ { N * } - p _ { S } ^ { C * } >$ $p _ { R } ^ { N * } - p _ { R } ^ { C * } )$

(iii) The wage offered by the platform to primary drivers is smaller under cooperation than under no cooperation $( i . e . ,$ $w _ { S } ^ { N * } > w _ { S } ^ { C * } )$

Proposition 2(i) shows that the price competition is more intense under cooperation than under no cooperation, consistent with some reports that claim Zipcar has been engaged in a more intense fight for riders after establishing the coopetition relationship with Uber (Higgins and Roberts 2017). We might expect that a purpose of cooperation in the first stage would be to soften the price competition in the second stage. However, Proposition 2(i) shows the opposite—cooperation in the first stage intensifies price competition between the two firms. The reason for this result is as follows. Cooperation in the first stage offers additional drivers (i.e., a secondary driver supply) to the platform. Thus, for the same platform and rental firm prices and hence the same demand, the platform needs fewer drivers from its primary supply when the firms cooperate than when they do not. Therefore, the platform can afford to pay a smaller wage and enjoy a higher profit margin under cooperation than under no cooperation for the same level of demand. Thus, the platform has more incentive to increase its demand by decreasing price under cooperation than under no cooperation. When the platform charges a lower price under cooperation, the rental firm also charges a lower price under cooperation to mitigate the decrease in its own demand.

Although both firms reduce their prices under cooperation, the platform decreases its price more than the rental firm, as shown in Proposition 2(ii), because the platform has the flexibility to reduce the wage (i.e., cost) as well, which the rental firm does not have. Consequently, the platform enjoys a higher rider demand under cooperation than under no cooperation, whereas the rental firm suffers a decline in its rider demand under cooperation. Essentially, cooperation induces some riders to switch from the rental firm to the platform. In addition, the platform enjoys the higher demand while paying a smaller wage to its primary drivers when the firms cooperate $( \mathrm { i . e . , } w _ { S } ^ { N * } > w _ { S } ^ { C * } )$ . Intuitively, cooperation guarantees a secondary supply of drivers, which the platform exploits to drive down the primary drivers’ wage.

Altogether, Proposition 2 shows that, under cooperation, whereas the rental firm gets additional demand from those drivers who rent from it and drive for the platform, it suffers from a lower price and lower demand from riders. Similarly, although the platform benefits by paying a smaller wage to its primary drivers and serving more riders, the more intense price competition hurts its revenue. Therefore, cooperation has ambiguous effects on the platform and the rental firm; it remains unclear whether and under what conditions the two firms would cooperate. We examine this question next.

## 5. When Would the Platform and the Rental Firm Form the Coopetition Relationship?

The platform and the rental firm would cooperate in the first stage only if they create a positive surplus for themselves (i.e., a higher total profit) when they cooperate. Moreover, if they choose to cooperate, they would choose the net wage for secondary drivers that maximizes the surplus; that is, the platform and the rental firm would solve the optimization problem in Equation

(11) jointly.

$$
\max _ {w _ {S R}, p _ {S R}} \left(\pi_ {S} ^ {*} (w _ {S R}, p _ {S R}) + \pi_ {R} ^ {*} (w _ {S R}, p _ {S R})\right)\tag{11}
$$

Proposition 3 summarizes the conditions under which both the platform and the rental firm have incentive to cooperate.

## Proposition 3.

(i) The platform and the rental firm might cooperate if and only if

$$
\Delta \equiv \alpha l ^ {2} (8 \delta - 9 \alpha c l) - 4 b ^ {2} k - 4 b l (\alpha c l + a - \delta + 2 \alpha k) > 0.\tag{12}
$$

(ii) Under Condition (12), the platform would cooperate if and only if $w _ { S R } \leq \overline { { w } } _ { S R } ,$ and the rental firm would cooperate if and only if w<sub>SR</sub> ≥ w<sub>SR</sub>. In the equilibrium of cooperation, $w _ { S R } ^ { * } \in [ \underline { { w } } _ { S R } , \overline { { w } } _ { S R } ] .$ , and they would set the net wage such that

$$
w _ {S R} ^ {*} - p _ {S R} ^ {*} = \frac {k}{l} + \frac {\Delta}{2 l (4 b ^ {2} + 4 b l (3 \alpha + \beta) + 9 \alpha l ^ {2} (\alpha + \beta))},\tag{13}
$$

where $\overline { { w } } _ { S R }$ and ${ \underline { { w } } } _ { S R }$ are defined in the appendix and $\overline { { w } } _ { S R } >$ w<sub>SR</sub>.

Proposition 3 presents the condition for a greater joint profit under cooperation and the conditions for both firms to benefit from the cooperation. According to Proposition 3(i), cooperation generates a positive surplus if and only if Condition (12) holds. The intuition for this finding is as follows. Under no cooperation, the platform and rental firm segment the rider market: Some riders are served by the platform at a cost $w _ { S } ^ { N * }$ , and the others are served by the rental firm at a cost c. When the two firms cooperate, by Proposition 2(ii), the platform reduces the price more than the rental firm, and thus the platform gains additional rider demand; Meanwhile, by Proposition 2(iii), the platform reduces the wage offered to primary drivers, reducing its primary driver supply. In both the no-cooperation and cooperation cases, demand matches supply. Therefore, at the aggregate level, we can interpret the change from no-cooperation to cooperation as follows. Some of the platform’s riders who used to be served by primary drivers under no cooperation are currently served by secondary drivers under cooperation, and the platform’s additional riders who used to be served by the rental firm under no coop eration are served by the platform’s secondary drivers. The former is a rider segment that switches drivers, and the latter is a rider segment that switches firms.

The total demand remains the same $( \mathrm { i . e . , ~ } 2 a )$ in the no-cooperation and cooperation scenarios. However, the prices charged by the platform and the rental firm decrease under cooperation as shown by Proposition 2(i). Although the riders who switch from the rental firm to the platform can be charged a higher price after switching, the revenue increase from them cannot compensate the revenue loss from riders who stay with the platform and the rental firm. Therefore, the total (joint) revenue from riders decreases when the two firms cooperate. This observation implies that any benefit from cooperation stems only from a reduction in the cost of serving the demand. However, using Lemma 1, we can verify that the profit margin from the riders served by the platform’s primary drivers decreases under cooperation compared with noncooperation. Meanwhile, the profit margin from the riders served by the rental firm decreases under cooperation compared with noncooperation because, by Proposition 2(i), the price decreases, whereas the cost remains the same. Therefore, any benefit from cooperation arises only from those switching riders who used to be served by the rental firm and are now served by the platform and those riders on the platform whose driver type is switched from primary to secondary. We further note that the net wage offered to secondary drivers is always less than the wage offered to the primary drivers when cooperation occurs, which also explains the increased profit margins from such switching. Proposition 3(i) states the condition under which the profit gain from switchers offsets the profit loss from all other riders.

Furthermore, Proposition 3(ii) shows that if the coopetition relationship increases the joint profit, the two firms choose an optimal net wage for secondary drivers that maximizes the joint profit and can always find a sharing rule (e.g., via ${ w } _ { S R } )$ that makes both firms better off with coopetition than without. Given the net wage, intuitively, a high wage for secondary drivers benefits the rental firm but hurts the platform because the high wage allows the rental firm to charge a high price to these drivers but raises the driver supply cost for the platform. As a result, $w _ { S R }$ cannot be too large or too small to give both the platform and the rental firm an incentive to establish the partnership. The equilibrium wage can be settled based on negotiation, and the relative bargaining power of the two determines the equilibrium sharing rule. If the platform has complete bargaining power over the rental firm, the platform might set the lowest possible $w _ { S R }$ for cooperation and extract the entire surplus generated by cooperation and leave the rental firm with the same profit as with no cooperation. Conversely, if the rental firm has complete bargaining power over the platform, the reverse would happen. When neither party has complete bargaining power over the other, in equilibrium the wage is chosen between the highest and lowest possible value for cooperation and both strictly benefit from the partnership.

Figure 1. The Impact of Net Wage  
(a) The Impact of Net Wage on Total Revenue  
![](/api/attachments/TFXNMKJS/fulltext/images/767976bc8bd064720379ba2f3b2b12c6ca8bf938f79b2bfd56fae806065f7466.jpg)

Proposition 3 and the related discussions highlight the important role of the sharing-economy model—the platform’s ability to adjust wage to control the self-scheduled driver supply—in inducing cooperation between the competing firms. The following result provides further support for the notion that the sharing-economy model is necessary to benefit from cooperation in our context.

Proposition 4. If the platform is prohibited from changing the primary drivers’ wage because of cooperation (i.e., the platform sets wage $w _ { S } ^ { N * }$ under cooperation), then coopera tion can never increase the joint profit.

When cooperation is profitable, the optimal net secondary-driver wage is given by Equation (13). The impacts of net wage on the total revenue and total cost are depicted in Figure 1. An increase in the net wage decreases the total revenue because it increases the supply of drivers to the platform, which in turn intensifies the price competition between the two firms. Conversely, an increase in the net wage initially decreases the total cost more quickly than it decreases the revenue because the platform reduces the wage for the primary drivers.

(b) The Impact of Net Wage on Total Cost  
![](/api/attachments/TFXNMKJS/fulltext/images/7221ae519bb086c628611900f45d9ae37e31fa1b534d40df2c7e99c97c54e758.jpg)  
Note. The figure is generated based on the following parameter value: $a = 2 0 , b = 0 . 5 , c = 0 . 5 , \delta = 5 , k = 0 . 1 , l = 1 , \alpha = 0 . 5 , \mathrm { a n d } \beta = 0 . 5 .$

However, after a threshold, the increased cost stemming from a high net wage for the secondary drivers offsets the savings in the primary drivers’ wage. The optimal net wage balances the tradeoff between these two effects.

The incentive for the platform and the rental firm to cooperate is determined by the condition on ∆, which depends on factors that characterize the market in our model—the total market size $( \mathrm { i . e . , ~ } a ) ,$ , the platform’s market-size differential $( \mathrm { i } . \mathrm { e } . , \delta )$ , and the degree of substitutability between the platform and the rental firm (i.e., b). Condition (12) further shows that the platform and the rental firm are more likely to cooperate with a lower $a ,$ a lower $b ,$ or a higher δ. In particular, Condition (12) could be satisfied only if $\delta > 0 ;$ that is, the two might have incentive to cooperate only if the platform’s service is more valuable than the rental firm’s service. Intuitively, cooperation creates value for the firms by improving profits from serving riders who switch from the rental firm to the platform. If the rental firm’s service is more valuable than the platform’s, the firms have no incentive to induce switching.

We next examine the market conditions that favor coopetition between the platform and the rental firm by analyzing the value of coopetition to the platform and the rental firm. We define the value of coopetition as the maximum joint profit when the two cooperate (i.e., when they set the optimal net wage under cooperation) minus the joint profit when they do not cooperate.

Proposition 5. The value of coopetition to the platform and the rental firm increases in the market-size differential $( i . e . , \delta )$ , and decreases in the total market size $( i . e . , a )$ and in the degree of substitutability between firms $( i . e . , b )$

Proposition 5 reveals that an increase in market-size differential $( \mathrm { i . e . , } \delta )$ makes coopetition more valuable and makes the two firms more likely to cooperate. Intuitively, an increase in δ increases the value of the platform’s riding service and decreases that of the rental firm’s service. Under no cooperation, by Lemma 1, an increase in δ increases the platform’s price and decreases the rental firm’s price, thus increasing the price differential between them. Moreover, the difference in the profit margins also increases in δ in the direction of favoring the platform. Therefore, as δ increases, cooperation creates more value for the two firms from shifting the riders from the rental firm to the platform. Meanwhile, the two firms are induced to increase the optimal net wage under cooperation (i.e., the net wage given by Equation (13) increases in δ), which, in turn, increases the secondary driver supply and benefits the platform by increasing its overall driver supply. Consequently, the value of coopetition increases in δ.

In contrast to the effect of $\delta ,$ an increase in market size $( \mathrm { i . e . , } a )$ makes coopetition less valuable and makes the two firms less likely to cooperate. An increase in a increases the joint profit under both the cooperation and no-cooperation scenarios. However, the marginal impact of the market potential on the joint profit is higher under no cooperation than under cooperation, decreasing the value of coopetition as a increases. An increase in market size increases the number of riders who stay with the platform or with the rental firm after cooperation, which is a loss for the two firms from cooperation because both firms lower their prices after cooperation. Meanwhile, we can show that an increase in a reduces the number of riders who switch from the rental firm to the platform and thus reduces cooperation’s benefit. Intuitively, an increase in market size makes the market-size differential smaller relative to the market size, making its effect less salient. Consequently, the number of riders who switch from the rental firm to the platform decreases, and the firms are induced to offer a lower net wage, resulting in fewer riders whose driver type switches from the primary to secondary. The reduction in both types of switchers reduces the benefit from coopetition.

An increase in the degree of substitutability has the same qualitative impact as an increase in a. If the degree of substitutability is high, the platform’s and rental firm’s price decreases due to cooperation are small, because, even in the no-cooperation case, the competition is already high, and thus the increase in competition because of cooperation is limited. Technically, by Lemma 1, when b becomes larger, the platform’s and rental firm’s price decreases due to cooperation become smaller; that is, $\begin{array} { r } { \frac { 4 \beta ( - k + l ( w _ { S R } - p _ { S R } ) ) } { 2 b + 3 \alpha l } \mathrm { ~ a n d ~ } \frac { 2 \beta ( \bar { - } k + l ( w _ { S R } - p _ { S R } ) ) } { 2 b + 3 \alpha l } } \end{array}$ decrease in b. Furthermore, the difference in their price decreases due to cooperation also shrinks. Consequently, fewer consumers would shift from the rental firm to the platform under cooperation, ceteris paribus, reducing the firms’ incentive to cooperate.

Next, we examine the effects of cooperation on rider surplus, driver surplus, and social welfare.

Proposition 6. If the platform and the rental firm cooperate, relative to no cooperation, the rider surplus and socia welfare increase, but the driver surplus decreases.

Intuitively, cooperation leads to more intense price competition between the platform and the rental firm and makes them lower their prices, which benefits the riders. Moreover, as shown in Proposition $^ { 6 , }$ social welfare, which captures the riders’ valuation and misfit costs, also improves under cooperation, and this also contributes to the higher rider surplus. The social welfare improves under cooperation because more riders use the platform, which provides greater value to riders than the rental firm provides. The drivers are hurt overall by cooperation because of the decrease in wage offered to primary drivers, although cooperation increases the driver supply.

In sum, the analysis reveals that coopetition between a ride-sharing platform and a rental firm may not always benefit both of them simultaneously. Such coopetition is more likely, and the benefit from coopetition would be significant when the total rider market size is not large, the platform has a significant market-size differential advantage over the rental firm, or the platform and the rental firm are only weakly substitutable. Moreover, any possible benefit from coopetition for the platform, rental firm, and consumers comes at the expense of primary drivers.

## 6. Model Extensions

6.1. Cross-Side Network Effects for the Platform In many two-sided markets, including in ride sharing, cross-side network effects are likely to exist. For instance, in the ride-sharing context, a rider might have a higher valuation for a platform if it has more drivers because the rider might have to wait less to find a driver. In the same vein, a driver is likely to have a higher valuation for a platform if it has more riders. On the other hand, such network effects are less salient in traditional rental firms. In this section, we extend the baseline model by incorporating such cross-side network effects for the platform.

We introduce the cross-side network effects in the baseline model by letting the demand for the platform relative to the rental firm to be affected not only by prices, but also by its driver supply. Analogously, the primary supply for a platform is affected not only by wage, but also by its rider demand. Specifically, in accordance with the existing literature (Parker and Van Alstyne 2005), we model the platform’s primary supply as

$$
q _ {S} = \alpha (- k + l w _ {S} + \mu d _ {S}),\tag{14}
$$

where $\mu$ is nonnegative and captures the supplyboosting effect of the platform’s demand. We assume that the cross-network effects do not change the secondary driver supply.<sup>8</sup> Similarly, we use λ to capture the cross-network effect of the platform’s supply on its demand relative to that of the rental firm. Thus, the platform’s and the rental firm’s demands under cooperation are given as

$$
\begin{array}{r} d _ {S} = a + \delta - b (p _ {S} - p _ {R}) + \lambda (q _ {S} + q _ {S R}) \\ d _ {R} = a - \delta - b (p _ {R} - p _ {S}) - \lambda (q _ {S} + q _ {S R}). \end{array}\tag{15}
$$

Combining Equations (14) and (15), we derive the platform’s demand and supply, and the rental firm’s demand, under cooperation as functions of exogenous parameters:

$$
\begin{array}{l} d _ {S} = \frac {a + \delta - b (p _ {S} - p _ {R}) + \lambda \alpha (- k + l w _ {S}) + \lambda q _ {S R}}{1 - \alpha \lambda \mu} \\ q _ {S} = \frac {\alpha (- k + l w _ {S} + \mu (a + \delta - b (p _ {S} - p _ {R})) + \lambda \mu q _ {S R})}{1 - \alpha \lambda \mu} \\ d _ {R} = \frac {a (1 - 2 \alpha \lambda \mu) - \delta - b (p _ {R} - p _ {S}) + \lambda \alpha (- k + l w _ {S}) + \lambda q _ {S R}}{1 - \alpha \lambda \mu}. \end{array}\tag{16}
$$

The demands and supply for the case without cooperation in the presence of network effects are obtained by setting the secondary supply, $q _ { S R } ,$ to zero in the above demand and supply functions given by Equations (16). To ensure that the platform’s demand decreases in its price and its supply increases in its wage with or without coop eration, we assume that $\lambda < 1$ and $\mu < 1 / \alpha$ . Furthermore, we must ensure that the platform’s price has a greater marginal impact on its demand than the primary wage, $w _ { S } ,$ and secondary net wage, ${ w _ { S R } } - p _ { S R }$ , and, analogously, the primary wage has a greater impact on the primary supply than the price and secondary net wage. Altogether, we impose the following constraints on λ and $\mu \mathrm { : }$

$$
\begin{array}{l} \lambda <   \min \left\{\frac {b}{\beta l}, \frac {b}{\alpha l}, 1 \right\} \\ \mu <   \min \left\{\frac {1}{\alpha}, \frac {l}{b}, \frac {1}{\beta \lambda} \right\}. \end{array}\tag{17}
$$

When $\lambda = 0$ and $\mu = 0 ,$ , the extended model reduces to the baseline model. Proposition 7 summarizes the condition under which both the platform and the rental firm would cooperate.

## Proposition 7.

(i) The platform and the rental firm would cooperate if and only if

$$
\begin{array}{l} \Delta^ {\prime} \equiv 2 b l (a (2 - \alpha \mu) (1 - \alpha \mu) (2 \alpha \lambda \mu - 1) \\ \quad - \alpha \mu (\alpha (c l (\alpha \lambda \mu + 3 \lambda - 4) - \delta \mu \\ \quad + k (\alpha \lambda \mu - \lambda - 2)) + 3 \delta) + 2 (\alpha c (\lambda - 1) l + \delta + \alpha k (\lambda - 2))) \\ \quad + \alpha l ^ {2} (2 (2 - \alpha \mu) (\alpha \lambda \mu (a - \delta - 2 a \lambda) + a \lambda + \delta (2 - \lambda)) \\ \quad - \alpha c l (\alpha \lambda \mu + 2 \lambda - 3) ^ {2}) \\ \quad - 2 b ^ {2} (1 - \alpha \mu) (2 k - \alpha \mu (c l + k)) > 0. \end{array} \tag {18}
$$

(ii) When they cooperate, they set the net wage to $\begin{array} { r } { \frac { k } { l } + \frac { \Delta ^ { \prime } } { 2 l X ^ { \prime } } , } \end{array}$ where

$$
\begin{array}{r l} & X = b l (\alpha^ {3} \lambda \mu^ {2} (\beta \mu + 4) + \alpha^ {2} \mu (\beta (\lambda - 2) \mu + 4 (\lambda - 3)) \\ & \qquad + 4 \alpha (\beta (\lambda - 1) \mu - 2 \lambda + 3) - 4 \beta (\lambda - 1)) \\ & \qquad + b ^ {2} (\alpha \mu - 1) (\alpha \mu (\beta \mu + 4) - 4) \\ & \qquad + \alpha l ^ {2} (\alpha + \beta) (\lambda (\alpha \mu + 2) - 3) ^ {2}. \end{array}\tag{19}
$$

Proposition 7 is qualitatively similar to Proposition 3. We find that the primary driving forces when the platform and the rental firm cooperate in the presence of crossnetwork effects are similar to those discussed for the baseline model without network effects. Specifically, any potential benefit comes from the improved profit margins from riders that switch from the rental firm to the platform and riders whose driver type is changed from primary to secondary under cooperation. In addition, we show the following result about how the cross-networkeffect parameter, λ, affects the condition under which the platform and the rental firm cooperate.

Proposition 8. If the platform and the rental firm have incentive to cooperate when $\lambda = 0 ,$ , they would cooperate for all feasible values of λ.

Proposition 8 shows that if the platform and the rental firm find coopetition to be beneficial when demand-side network effects are absent, they would find coopetition to be beneficial in the presence of demand-side network effects as well. Figure 2 further illustrates that even though the platform and the rental firm do not find coopetition to be beneficial when the demand-side network effect is absent, they do find it to be beneficial if the demand-side network effect is sufficiently strong. Although analytically showing a similar result for the supply-side network effect parameter, $\mu ,$ is difficult, Figure 2 numerically illustrates that a similar finding applies for the supply-side network effect as well—the supply-side network effect makes the two firms more likely to cooperate. Moreover, Figure 3 shows that the value of coopetition increases in λ and $\mu .$ Proposition 8 and Figure 3 demonstrate that the crossnetwork effects on either side strengthen the firms’ incentives to cooperate.

The primary reasons for the findings related to the cross-network effects are the following. By Equation (16), an increase in λ is akin to an increase in the platform’s market-size differential $( \mathrm { i } . \mathrm { e } . , \delta )$ , and Proposition 5 establishes that the two firms are more likely to cooperate as the market differential increases. Thus, the intuition for the impact of δ on the firms’ incentives to cooperate applies to the intuition for the impact of λ as well. Conversely, an increase in $\mu$ increases the primary driver supply for the platform. Thus, the platform is able to get the same amount of driver supply with a smaller wage in the presence of a cross-network effect of demand on supply compared with without such cross-network effect, ceteris paribus. The increase in the rider demand under coopetition induces the platform to reduce driver wage even more with cross-network effects than without. Therefore, the increase in cost savings increases the value of coopetition when µ increases.

Figure 2. (Color online) The Impact of Network Effects on Cooperation  
![](/api/attachments/TFXNMKJS/fulltext/images/5596b39d84f131d6e80db95d0409fc7a56098d8ed4c07e1907d4a0e2e1378c3f.jpg)  
Note. The figure is generated based on the following parameter value $a = 2 0 , \overset { \cdot } { \delta } = 5 , b = 0 . 5 , c = 0 . 5 , k = 0 . 1 , l = 1 , \alpha = 0 . 5 ,$ and β � 0:5.

## 6.2. Loyal Rider Segments for the Platform and the Rental Firm

In this extension, we consider the case where some riders would only consider using the platform or the rental firm. In other words, both the platform and rental firm have their own loyal rider segments. Additionally, as in the base model, some riders choose between the platform and the rental firm, whichever offers them a higher surplus. Specifically, we revise the demand functions to the following to model this case.

$$
\begin{array}{l} d _ {S} = a + \delta - b (p _ {S} - p _ {R}) + m (1 - \epsilon p _ {S}) \\ d _ {R} = a - \delta - b (p _ {R} - p _ {S}) + n (1 - \tau p _ {R}) \end{array}\tag{20}
$$

The terms $m ( 1 - \epsilon p _ { S } )$ and $n ( 1 - \tau p _ { R } )$ in Equation (20) correspond to the two loyal rider segments. To interpret, m and n denote the sizes of the platform’s and rentalfirm’s loyal segments, respectively; ɛ and $\tau$ denote, respectively, the price sensitivity of each rider in the plat form’s and the rental firm’s loyal segment. If $m = n = 0 ,$ this model reduces to that in the base case. The rest of the model is identical to that of the base case.

We follow the same solution procedure as in the base model. We provide the detailed analysis in the online appendix, but state the main result here regarding the conditions under which the platform and the rental firm would engage in coopetition.

Proposition 9. The platform and the rental firm would cooperate if and only if

$$
\begin{array}{r l} & {\Delta^ {\prime \prime} \equiv [ l (a + b c + \delta + \alpha k + m) - (c l + k) (b + \alpha l + m \epsilon) ] Y ^ {2}} \\ & {\qquad + b ^ {2} l (- \alpha l (a + \delta + m) + b ^ {2} c + b (c m \epsilon + \alpha k) + \alpha k m \epsilon) Y} \\ & {\qquad - b ^ {3} l (b + \alpha l + m \epsilon) [ b (a (8 b + 6 \alpha l) + 2 b ^ {2} c} \\ & {\qquad + b (\alpha c l + 2 \alpha k + 4 m + 4 n) + 2 \alpha l (- \delta + m + 2 n))} \\ & {\qquad + 2 m \epsilon (6 a b + 2 a \alpha l + b ^ {2} c + \alpha b k - 2 \delta (b + \alpha l)} \\ & {\qquad + 2 b m + 4 b n + 2 \alpha l n) + 4 m ^ {2} \epsilon^ {2} (a - \delta + n) ] > 0,} \end{array}\tag{21}
$$

where

$$
\begin{array}{c} Y = b (2 b ^ {2} + 3 b (\alpha l + 2 m \epsilon) + 4 m \epsilon (\alpha l + m \epsilon)) \\ + 4 n \tau (b + m \epsilon) (b + \alpha l + m \epsilon). \end{array}\tag{22}
$$

Comparing Proposition 9 with Proposition 3, we verify that $\bar { \Delta } ^ { \prime \prime } > \breve { \Delta }$ when $m , n > 0$ , implying that the platform and the rental firm are more likely to engage in coopetition when they have loyal rider segments than when they do not. Intuitively, loyal rider segments diminish the negative effects of the rider-side competition on driver-side cooperation. Proposition 9 is also consistent with the insight derived in the base model that the platform and the rental firm do not necessarily want to cooperate on the driver side. Further examination of the model with loyal rider segments reveals that cooperation still intensifies the competition. In addition, our insights on market characteristics continue to hold: The two firms’ incentives to engage in the coopetition increase in the platform’s market-size advantage over the rental firm and decrease in the substitutability between the platform and the rental firm.

(b) Network Effect of Supply on Demanc  
Figure 3. Cross-Side Network Effects and the Value of Cooperation  
(a) Network Effect of Demand on Supply  
![](/api/attachments/TFXNMKJS/fulltext/images/9770e1d8406453b7df661413ff2c582782e42a481fc4ab014162923de628e457.jpg)

![](/api/attachments/TFXNMKJS/fulltext/images/806a9e445fd40533cf72823bad2326ce03df422e5f76b521a7cafe98d760b89c.jpg)  
Notes. The figure is generated based on the following parameter value: $a = 2 0 , \delta = 5 , b = 0 . 5 , c = 0 . 5 , k = 0 . 1 , l = 1 , \alpha = 0 . 5 ,$ , and $\beta = 0 . 5 .$ . In addition, $\mu = 0 . 9 \left( \mathrm { a } \right)$ and $\lambda = 0 . { \overset { \sim } { 9 } } ( { \mathfrak { b } } )$ ).

## 6.3. When the Primary Drivers Incur a Cost for Using Their Own Vehicles

In the base model, we assume that the primary drivers do not incur any marginal cost for using their own vehicles. In this extension, we relax this assumption and quantify how the primary drivers’ marginal cost of vehicle use, $c _ { m } ,$ would affect our main insights. This relaxation makes the primary driver supply function

$$
q _ {S} = \alpha (- k + l (w _ {S} - c _ {m})),\tag{23}
$$

where $w _ { S } - c _ { m }$ is the net wage for the primary drivers. This supply function is analogous to that of the secondary drivers. Everything else remains the same as in the base model. Similarly, we can derive the condition under which the platform and the rental firm have incentive to cooperate.

Proposition 10. The two firms cooperate if and only if

$$
\begin{array}{c} \alpha l ^ {2} [ 8 \delta - 9 \alpha (c - c _ {m}) l ] - 4 b ^ {2} k - 4 b l (\alpha (c - c _ {m}) l \\ + a - \delta + 2 \alpha k) > 0. \end{array}\tag{24}
$$

Comparing Conditions (12) and (24), we find that the cooperation condition in this extension is very similar to that in the base model. Essentially, Condition (24) is obtained by replacing c in Condition (12) by $c - c _ { m }$ When $c _ { m } = 0 ,$ , Condition (24) reduces to (12). We find that as long as the primary drivers’ vehicle cost $c _ { m }$ is less than the rental firm’s vehicle cost $( \mathrm { i } . \mathrm { e } . , c _ { m } < c )$ , which is likely to be the case in practice, all results of the base model hold qualitatively in this model extension. Moreover, our analysis shows that as long as $c _ { m }$ is less than $c , \mathrm { a }$ primary driver has no incentive to switch to being a secondary driver (i.e., $w _ { S } ^ { C * } - c _ { m } > w _ { S R } ^ { * } - p _ { S R } ^ { * } )$ , which also keeps the primary and secondary driver populations identical in the base model and in this extended model, demonstrating the robustness of our base-model results.

## 6.4. Fixed Commission Rate for the Platform

The DCR scheme in our base model offers the platform flexibility in the sense that rider price and driver wage can be chosen independently. Another observed scheme in practice is the fixed-commission-rate (FCR) scheme, under which the driver wage is a fixed fraction of the rider price. We examine the coopetition relationship between the platform and the rental firm under the FCR scheme in this subsection.

Under the FCR scheme, we denote as γ the platform’s commission rate, and thus a driver receives $1 - \gamma$ of the rider price, where $0 < \gamma < 1$ . Compared with the base model, the FCR scheme implies two additional constraints: $w _ { S } = ( 1 - \gamma ) p _ { S }$ and $w _ { S R } = ( 1 - \gamma ) p _ { S }$ . The demand and supply functions remain the same as in the base model. The time sequence would be the same as in the base model except that wages are no longer independent decision variables. Rather, they depend on the price the platform charges its riders.

We solve the game following a similar procedure as in the base model. The supply might exceed demand in equilibrium for the platform when the commission rate, $\gamma ,$ is low enough, under both no-cooperation and cooperation scenarios, because, with a low commission rate, the wage offered to the drivers would be high, ceteris paribus. We present our analysis for the case when supply and demand are matched in equilibrium. The conditions for this case are provided in the online appendix.

The following result presents the condition under which the platform and the rental firm would form the coopetition relationship.

Proposition 11. The platform and the rental firm would cooperate if and only if

$$
\frac {b ^ {2} + b l (4 \alpha (1 - \gamma) - \beta \gamma) + 4 \alpha^ {2} (1 - \gamma) ^ {2} l ^ {2}}{b + 2 \alpha (1 - \gamma) l} <   \sqrt {\frac {X}{2 Y}},\tag{25}
$$

where $X , Y > 0$ and are provided in the online appendix.

The two firms cooperate if and only if both firms benefit from cooperation. We find that the rental firm always benefits from cooperation. However, the platform does not necessarily enjoy a higher profit under cooperation. Condition (25) shows the condition under which the platform gains a higher profit under cooperation compared with no cooperation. The impact of the cooperation on the rental firm differs from that in the base model because of the embedded feature of the FCR scheme— the platform has no flexibility to independently decide its wage under the FCR scheme—which restricts the platform’s ability to compete with the rental firm. We also find, as in the base model, the two firms charge a lower price under cooperation than under no-cooperation. Moreover, the impacts of market characteristics on the value of coopetition remain the same. Specifically, theoretical analysis and numerical results demonstrate that the two firms are more likely to cooperate when the total market size, $a ,$ is lower, the platform’s market-size advantage δ is higher, or the degree of substitutability b is lower. In addition, we find that a higher commission rate makes the two firms less likely to cooperate.

## 6.5. When the Two Firms Do Not Maximize Joint Profit in Cooperation

In the base model, if the platform and the rental firm decide to cooperate, the two firms decide the secondary driver’s net wage jointly to maximize the joint profit. Meanwhile, it is conceivable that, although the platform and the rental firm decide to cooperate, the cooperation could be limited to the extent of only allowing drivers to rent from the rental firm and drive for the platform. In particular, in Stage 1, the two firms could decide the price and wage noncooperatively to maximize their own profits; that is, the platform decides the wage offered to the secondary driver, and the rental firm decides the price charged for using the rental vehicle. We analyze this scenario in this section. The rest of the model for this scenario is identical to that of the base model.

Stage 2 of the game is identical to that in the base model, given the net wage resulting from the platform’s and the rental firm’s decisions in Stage 1. Therefore, the solution of the subgame in Stage 2 remains the same, as summarized by Lemma 1. Anticipating the equilibrium in the second stage, the two firms respond to each other’s decisions in the first stage.

Proposition 12. Both firms benefit from the cooperation $i f$ and only if $\Delta > 0$ and

$$
(2 b + 3 \alpha l) ^ {2} - 4 b \beta l > 0,\tag{26}
$$

where ∆ is defined in Equation (12).

Proposition 12 is qualitatively similar to Proposition 3(i) for the base model. When the two firms set price and wage jointly in cooperation, only $\Delta > 0$ is required to ensure cooperation. When they set price and wage separately to maximize their own profits, the additional Condition (26) is required for cooperation to occur. Thus, the two firms would cooperate in a smaller region of the parameter space when the two firms make wage and price decisions separately than when they make those decisions jointly in the first stage. Intuitively, this is because the two firms negotiate cooperatively in the base model. We can verify that Condition (26) can be satisfied unless the population of secondary drivers is significantly greater than that of primary drivers.

Compared with the base model, we also find that the net wage offered to the secondary drivers under cooperation is lower. The rationale behind this result is that, when decreasing the wage w or increasing the price $p _ { S R } ,$ neither of the two firms considers the negative impacts on the other party’s benefit when they maximize their own profit, whereas the two parties in the base model do. Metaphorically, in the base model the two firms first bake the largest pie and then bargain to divide the pie, whereas the two firms are concerned only about their individual pie size in the model considered in this section. As in the base model, we can also verify that the two firms are more likely to cooperate when the total market size, $a ,$ is lower or the platform’s market-size advantage, $\delta ,$ is higher. In addition, the cooperation conditions would be satisfied when the degree of substitutability, $b ,$ is lower than a threshold. More importantly, the driving forces behind the coopetition incentives remain the same because the impacts of additional supply on their subsequent competition in the second stage remain qualitatively the same.

In sum, while there are a few differences, the key qual itative results of the base model carry over to the scenario where the platform and the rental firm engage in a limited cooperation, only allowing drivers to rent from the rental firm and drive for the platform and setting wage and price independently.

## 6.6. When Only the Rental Price for Secondary Drivers Is Decided Jointly

In the base mode, we assume that under cooperation, the platform and the rental firm collectively decide the wage, $w _ { S R } ,$ and $\mathrm { p r i c e } , p _ { S R } ,$ to maximize their joint profit, which is divided between them through negotiation. However, it might be possible that cooperation only affects the rental price, $p _ { S R } ,$ but not the wage that the secondary driver receives: The platform and the rental firm collectively decide only the price, $p _ { S R } ,$ to maximize their joint profit. We examine the robustness of our main insights under this model variation.

The no-cooperation scenario remains the same as in the base model. Under cooperation, the rental firm and the service platform collectively decide the rental price, $p _ { S R } ,$ for secondary drivers in the first stage. In Stage 2, the platform decides the price charged to riders, ${ p } _ { S } ,$ and the wage, $w _ { S } ,$ offered to drivers (including both primary and secondary drivers); the rental firm decides its price charged to riders $p _ { R }$

Proposition 13. The two firms cooperate $i f$ and only $i f$ $p _ { S R } ^ { \prime \prime } > p _ { S R } ^ { \prime } ,$ , where $p _ { S R } ^ { \prime }$ and $p _ { S R } ^ { \prime \prime }$ are provided in the online appendix.

Proposition 13 shows that, as in the base model, the two firms would cooperate only under some condition. In the condition, $p _ { S R } ^ { \prime \prime }$ is defined as the rental price under cooperation charged to the secondary drivers that would provide the platform the same profit as under the no-cooperation case. Analogously, $p _ { S R } ^ { \prime }$ is defined as the rental price under cooperation charged to the secondary drivers that would provide the rental firm the same profit as under the no-cooperation case. As in the baseline model, we find that, in the subgame equilibrium, the platform’s profit decreases and the rental firm’s profit increases in the rental price for secondary drivers $p _ { S R } .$ Therefore, if the rental price is located in the interva $[ p _ { S R } ^ { \prime } , p _ { S R } ^ { \prime \prime } ]$ , both firms obtain higher profits under cooperation and they consequently would cooperate. The existence of such an interval requires $p _ { S R } ^ { \prime \prime } > p _ { S R } ^ { \prime } ,$ , the condition in Proposition 13.

We also investigate the rationale behind the coopetition condition. As in the base model, we can verify that cooperation in the first stage intensifies the price competition in the subsequent stage. The benefit of coopetition comes solely from riders switched from the rental firm to the service platform. In addition, we examine the impacts of market characteristics on the coopetition condition. Numerically, we find the same set of results as in the base model: The coopetition is more likely to occur if the market size, $a ,$ is lower, the market differential, $\delta ,$ is lower, or the degree of substitutability on the demand side, $b ,$ is lower.

## 7. Conclusion

Coopetition by firms is a commonly observed business strategy in many traditional industries. We examine the coopetition strategy in the transportation context where one firm (the platform) operates under the sharingeconomy model and the other (the rental firm) operates under the traditional model. We show that coopetition does not always benefit both the platform and the rental firm. We find that coopetition is more likely when the rider market size is not high, the platform has a high market-size advantage over the rental firm, or the plat form and the rental firm are weakly substitutable from riders’ perspectives. More importantly, when coopetition is mutually beneficial, the benefit comes solely from the improved profit margin realized in serving riders that switch from the rental firm to the platform under coope tition and riders who are switched from primary drivers to secondary drivers by the platform. Coopetition between the platform and the rental firm always benefits the riders and hurts the drivers, while benefiting society overall. The presence of cross-network effects for the platform and of loyal rider segments for the platform and the rental firm enhance their incentives to form a coopetition relationship.

These findings have important implications for academics, practitioners, and policymakers. First, our findings highlight how well-established strategies that are common under traditional business models can have novel implications when applied to sharing-economy models. The extant coopetition literature has identified softening of price competition and enhancement of prod uct quality, consumer valuation, and market size as the primary contributing factors for the success of the coopetition strategy. Our results demonstrate that the purpose of coopetition need not be to soften price competition or enhance the product quality and demand; it can be to shift the demand from a lower-value firm to a highervalue firm and to redistribute the demand from a highercost supply to a lower-cost supply within a firm, even though doing so can intensify competition in a setting like ours. Essentially, it is the use of the sharing-economy model by one of the firms and the supply-side flexibility it enjoys that give rise to the novel findings. Thus, our study highlights the need to examine traditional strategies and theories in the context of the sharing-economy model to enrich our understanding of these theories.

Second, our study also points to a surprising implication for rental firms. The conventional expectation would be that partnering with a competitor that already has a significant competitive advantage over the rental firm and providing it additional resources (vehicles) would only make the competitor stronger and hurt the rental firm. However, our study shows that under some conditions, the rental firm can extract adequate profit from this supply to offset the loss on the rider side. Thus, although the rental firm lacks the flexibility to control its supply side dynamically, which the platform has, by partnering with the platform, the rental firm can benefit from the platform’s wage flexibility.

In contrast, it seems that a platform would always welcome partnership with the rental firm because the rental firm can provide a critical resource (i.e., vehicles) needed to operate under the sharing-economy model. In fact, when Uber and Zipcar announced their first partnership in Boston, the Zipcar and Uber spokespeople touted that the cooperation solved Uber’s supply issue and created a new revenue source for Zipcar. However, our analysis shows that the success of such partnerships can vary across markets, depending on market characteristics.

Our findings provide guidance to platforms and rental firms regarding the market conditions that favor coopetition. In a market where the platform has a high marketsize advantage (e.g., a big city where riders may not desire to drive on their own and attach a high value to having a driver), coopetition is more likely to be beneficial. Analogously, in a market where riders are not averse to driving on their own, if the riders have a strong preference for the platform or the rental firm, then coopetition is more likely to be beneficial. Smaller markets can also be attractive for firms to engage in coopetition.

Finally, our results provide implications for riders, drivers, social planners, and policymakers. Clearly, as consumers, riders would welcome the cooperation as it intensifies the price competition between the firms. However, the drivers would be split—the secondary drivers would welcome cooperation, but the primary drivers would not. In fact, it is this segmentation of drivers— those with vehicles and those without—that enables the platform to use cooperation to its advantage by offering different wage structures to the two segments. In addition to drivers, this finding should be of concern to social planners and policymakers because the cooperation benefits all other stakeholders at the expense of primary drivers.

A significant concern of social planners is that coopetition can lead to collusion and lessening of competition that could hurt consumers. If coopetition leads to new products or enhanced product quality and therefore new markets or market expansion, as is usually the case in industries such as automobiles and pharmaceuticals, then it could potentially mitigate the competition concern. In these cases, coopetition could be justified. In our context, solely from the market-competition perspective, it seems that social planners should encourage cooperation as it makes the two firms more competitive. However, the social planners would have to consider the welfare of drivers as well in the ride-sharing and carrental contexts. Because the benefits of cooperation to the other stakeholders come at the expense of primary drivers (possibly those who drive for the platform as fulltime work), it becomes imperative for social planners to address their needs and devise policies that would make all parties better off under cooperation. That is, our results highlight a potential new concern that social planners should consider when they examine coopetition between firms operating under different models (e.g., traditional and sharing).

This study can be extended in several directions. We consider a single platform and a single rental agency. However, in practice, a platform such as Uber partners with several rental firms and a rental firm such as National could partner with several platforms. Examination of such industry-wide partnership networks would provide additional insights into coopetition within this industry. Another potential direction is to identify and examine policies that would ensure that all players are better off under cooperation if it occurs. Finally, we examine a context in which the two-sided platform sets prices on both sides. Other sharing-economy models used in other industries may involve suppliers setting their own prices for their services, such as short-term housing rentals. Examination of potential coopetition between such platforms as Airbnb and traditional hotels can be a valuable extension of our research.

## Endnotes

<sup>1</sup> See, for example, https://www.wsj.com/articles/zipcar-betscommuters-will-pay-subscription-1509012000 and https://www. ridesharingforum.com/t/zipcar-vs-uber-is-zipcar-still-a-viable alternative-to-uber/220.

<sup>2</sup> See the discussions in the ride-sharing forum https://www. ridesharingforum.com/t/zipcar-vs-uber-is-zipcar-still-a-viablealternative-to-uber/220 about varying rider preferences for Uber and Zipcar.

<sup>3</sup> See, for example, https://therideshareguy.com/uber-car-rental/ for more details.

<sup>8</sup> It is reasonable to assume that the secondary drivers would be affected less by the cross-network effects than primary drivers because the secondary drivers’ wage (and price) are set jointly prior to the competition stage. We present the analysis for the boundary case where cross-network effects do not affect the secondary driver supply at all. A more general model, where the secondary supply is affected by cross-network effects, yields qualitatively similar results to those presented in this section, albeit with significantly more complex analysis.

## References

Abhishek V, Guajardo JA, Zhang Z (2021) Business models in the sharing economy: Manufacturing durable goods in the presence of peer-to-peer rental markets. Inform. Systems Res. 32(4):1450–1469.

Adner R, Chen J, Zhu F (2020) Frenemies in platform markets: Het erogeneous profit foci as drivers of compatibility decisions. Management Sci. 66(6):2432–2451.

Banker RD, Khosla I, Sinha KK (1998) Quality and competition. Management Sci. 44(9):1179–1192.

Bomey N (2017) Uber, Zipcar sign car-sharing deal. Accessed April 6, 2019, https://www.usatoday.com/story/money/cars/2017/ 02/08/uber-zipcar-sign-car-sharing-deal/97637790.

Brandenburger AM, Nalebuff BJ (1996) Coopetition. Currency (Crown Business, Danvers, MA).

Burtch G, Carnahan S, Greenwood BN (2018) Can you gig it? An empirical examination of the gig economy and entrepreneurial activity. Management Sci. 64(12):5497–5520.

Chen J, Guo Z (2022) New-media advertising and retail platform openness. Management Inform. Systems Quart. 46(1):431–456.

Cohen M, Sundararajan A (2015) Self-regulation and innovation in the peer-to-peer sharing economy. University Chicago Law Rev. Online 82(1):8.

Cohen MC, Zhang R (2022) Competition and coopetition for twosided platforms. Production Oper. Management 31(5):1997–2014.

Cramer J, Krueger AB (2016) Disruptive change in the taxi business: The case of Uber. Amer. Econom. Rev. 106(5):177–182.

Dagnino GB (2009) Coopetition strategy: A new kind of interfirm dynamics for value creation. Coopetition Strategy (Routledge, London), 45–63.

Eldredge B (2017) Uber and Zipcar join forces for car-sharing deal. Accessed December 20, 2017, https://www.curbed.com/2017/ 2/10/14569872/uber-and-zipcar-join-forces-for-car-sharing-deal.

Fraiberger SP, Sundararajan A (2015) Peer-to-peer rental markets in the sharing economy. Research Paper, NYU Stern School of Business, New York.

Friedman G (2014) Workers without employers: Shadow corpora tions and the rise of the gig economy. Rev. Keynesian Econom. 2(2):171–188.

Granot D, Sosˇic ´ G (2005) Formation of alliances in Internet-based supply exchanges. Management Sci. 51(1):92–105.

Granot D, Yin S (2008) Competition and cooperation in decentralized push and pull assembly systems. Management Sci. 54(4): 733–747.

Higgins T, Roberts A (2017) Zipcar steps up fight against Uber with push for commuter subscriptions. Accessed May 15, 2020, https://www.wsj.com/articles/zipcar-bets-commuters-will-paysubscription-1509012000.

Jiang B, Tian L (2018) Collaborative consumption: Strategic and economic implications of product sharing. Management Sci. 64(3): 1171–1188.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Mantena R, Saha RL (2012) Co-opetition between differentiated platforms in two-sided markets. J. Management Inform. Systems 29(2): 109–140.

Martin E, Shaheen SA, Lidicker J (2010) Impact of carsharing on household vehicle holdings. Transportation Res. Record 2143: 150–158.

Nagarajan M, Sosˇic ´ G (2007) Stable farsighted coalitions in competitive markets. Management Sci. 53(1):29–45.

Parker GG, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10): 1494-1504

Song W, Chen J, Li W (2021) Spillover effect of consumer awareness on third parties’ selling strategies and retailers’ platforms open ness. Inform. Systems Res. 32(1):172–193.

Taylor TA (2018) On-demand service platforms. Manufacturing Ser vice Oper. Management 20(4):704–720.

Uber (2019) Rent a car and start earning: Vehicle solutions. Accessed April 6, 2019, https://www.uber.com/drive/vehicle-solutions/.

Walmsley J (2018) Carless Uber drivers can now rent one for \$5 an hour in 3 U.S. cities. Accessed April 6, 2019, https://www.forbes. com/sites/juliewalmsley/2018/12/13/carless-uber-drivers-cannow-rent-one-for-5-an-hour-in-5-u-s-cities/#cf89f566dfd1.

Weber TA (2014) Intermediation in a sharing economy: Insurance, moral hazard, and rent extraction. J. Management Inform. Systems 31(3):35–71.

Zervas G, Proserpio D, Byers JW (2017) The rise of the sharing economy: Estimating the impact of airbnb on the hotel industry. J. Marketing Res. 54(5):687–705.

Zhang C, Chen J, Raghunathan S (2022) Two-sided platform compe tition in sharing economy. Management Sci. 68(12):8909–8932.

Zipcar (2020) Uber partnership program – Zipcar. Accessed April 15, 2020, https://support.zipcar.com/hc/en-us/articles/360038136153- Uber-Partnership-Program#how-it-works-0-0.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
