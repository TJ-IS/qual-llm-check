---
otero_id: 7746
otero_key: "VESNGQRY"
title: "Network effects in online two-sided market platforms: A research note"
authors: "Shengli Li; Yipeng Liu; Subhajyoti Bandyopadhyay"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.02.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Network effects in online two-sided market platforms: A research note

Shengli Li, Yipeng Liu, Subhajyoti Bandyopadhyay ⁎

Warrington College of Business Administration, University of Florida, USA Kania School of Management, University of Scranton, USA

## a r t i c l e i n f o

Article history: Received 22 July 2009 Received in revised form 10 February 2010 Accepted 13 February 2010 Available online 19 February 2010

Keywords: Two-sided market competition Network externality Platform differentiation

## a b s t r a c t

Many online platforms show characteristics whereby two groups of agents – the buyers and the sellers – come together and interact with one another via the enabling platform. The bene<sup>fi</sup>t that accrues to a member of either group depends on both the number of agents within each group and the extent of competition between the sellers for the buyers. We present a model to analyze such interactions. The results imply that if two platforms are relatively undifferentiated, trying to increase the cross-group network bene<sup>fi</sup>ts for the buyers can be counterproductive. Instead, the platforms should <sup>fi</sup>rst try to increase their relative differentiation, which then allows them to charge higher prices relative to the other platform. The results have particular signi<sup>fi</sup>cance in the online world, where the erstwhile strategy of many platforms that seem relatively undifferentiated from the consumers perspective has been to increase the cross-group network bene<sup>fi</sup>ts.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

There are many examples of markets where the buyers and sellers interact with each other through the means of a platform, the most common example being perhaps the ubiquitous shopping mall. Many examples are increasingly being found in the online marketplaces, with the online auction platform EBay being one of the <sup>fi</sup>rst names that come to mind. Other examples include online social networks and online business-to-business (B2B) marketplaces. Other similar examples are summarized in Evans [10]. The platforms get compensated for their services by a possible market entry fee from each seller and buyer (though in almost all cases we see that the platforms usually choose not to charge the latter group), and optionally from some part of the proceeds of the transactions that it helps enable. This kind of pricing structure has been discussed in the literature such as Rochet and Tirole [15] and [16]. In each of such markets, the success of the platform depends on both the number of buyers and sellers it can attract, as well as the interaction effects between the members of each group. For example, too many sellers exacerbate the competition for buyers, which deter future sellers from joining the platform. Similarly, buyers might also be deterred from visiting the platform if there are already many buyers on the platform (e.g. some people might avoid shopping malls during crowded weekends). The opposite effect is also possible – the popularity of the online social platforms such as Facebook or MySpace is driven by the presence of one's friends and acquaintances who also are members of the platform [9]. Due to the diverse nature and magnitude of the possible interactions, such two-sided markets, as they have been called in the extant literature, present some unique challenges in their modeling and analysis.

Unlike traditional markets, two-sided market platforms (a market is considered two-sided “if the platforms serve two types of agents, such that the participation of at least one group raises the value of participating for the other group”<sup>1</sup> [17, p. 142]) are affected by two distinct types of competition (for a very nice introduction to the economics of two-sided markets, see Rysman [18]). The <sup>fi</sup>rst, which we call ‘inside competition’, occurs between subjects within the same platform, for example, between the different sellers competing for a consumer on an auction site such as EBay. The second type of competition, which we call ‘outside competition’, occurs between the platforms themselves as they compete in terms of getting the buyers and sellers to use their platform. Whereas in a conventional market customers may be attracted through lower prices and higher utility for a product, in a two-sided market the competition takes place in multiple contexts: between platforms who need to attract both buyers and sellers to transact on them, between sellers who need to strategically decide as to which platform to join and then compete with other sellers on that platform for the buyers' attention, and the buyers who need to decide on the platform they want to visit. As a result, the platform may strategically choose to reduce the commission/access fees charged to the sellers or to the buyers, a phenomenon that is almost always observed in online two-sided market platforms whereby the consumers are granted free entry and the sellers on the other side of the platform get charged for the privilege.

In this research note, we present a stylized model to analyze such online market platforms. While there exists a wealth of literature that models competition between online platforms, for the sake of analytical tractability, the focus of such analysis has always been the competition between the platforms themselves (i.e. the ‘outside competition’), and in the process abstracting away the actual competition between the sellers for the buyers (the ‘inside competition’). While such a process is undoubtedly useful, it simpli<sup>fi</sup>es some of the intricacies that arise due to the two-sidedness of the interactions. In contrast to that extant literature, in this article we explicitly model the competition between the sellers for the buyers, as well as the competition between the platforms themselves (we detail our contribution to the literature further in the next paragraph). This helps us model the intricacies of the competition that exists in online platforms that has so far not been captured in the literature. In the process, we discover some seemingly counter-intuitive results that have practical strategic implications for such platforms.

There has been a recent surge of interest in two-sided market platforms, and the two papers by Roson [17] and Rochet and Tirole[16] do an admirable job in surveying much of the extant literature. For the purposes of our model, some of the most relevant literatures include the seminal work by Armstrong [1] and Armstrong and Wright [2], who have considered different scenarios of competition in two-sided markets. In particular, Gupta et al. [12] discusses the difference between electronic retailers and in-store retailers, which are examples of two-sided markets. Muylle and Basu [14] de<sup>fi</sup>ne and discuss electronic intermediary in general. The pricing strategies of electronic retailers are studied by Granados et al. [11], Chircu and Mahajan [7] and Chun and Kim [8]. Other literature featuring competition models in two-sided markets include Caillaud and Jullien [5,6] and Rochet and Tirole [15]. A framework of online platform support for electronic commerce processes has been given in Shaw et al. [19] and Basu and Muylle [3], where the authors investigate the impact of web retailers' extent of technology adoption and electronic commerce practices. As compared to these models, our work explicitly models the possibility of both positive and negative cross-group and within-group network effects that might be present in such platforms (in fact, in much of the extant literature, only cross-group network effects are modeled, and that too only as a positive effect). Further, the role of the competing platforms is often that of a matchmaker (for example, [5,6]), so that it is not possible to understand the strategic interaction between sellers who are competing for buyers on a two-sided platform. Even when the models have differentiated between the two types of agents as buyers and sellers (as in [15]), simplifying assumptions have made the price charged by the sellers equal to the buyer's gross surplus for the products sold. In our model, we explicitly consider the effect of competition between the sellers on the price they charge the buyers, which introduces an additional layer of complexity.

In the following two sections, we present our stylized model followed by the analysis and results. The latter section also discusses the practical implications of these results. The <sup>fi</sup>nal section concludes.

## 2. The model

We model two platforms competing for sellers and buyers. The two platforms, while providing similar functionality, appeal to different types of buyers, who are spatially distributed in a Hotelling sense [13], with the two platforms situated at the two ends of the linear model (see Fig. 1). For example, the two online bookstores Alibris and Half.com provide similar functionalities, but have known to attract different types of consumers, due to the very different demographics between the customers of the two sites. Alibris is predominantly preferred by users searching for old, rare and collectable books while Half.com is frequented by college students seeking for discounted textbooks. Thus, even though both sites will end up serving very similar ends (i.e. selling books), different users will rate the experience on the two sites very differently due to their private preferences. The cost of “transportation” (also called the $" \mathrm { f i t " }$ cost in the literature) in this spatial differentiation model is an abstraction that models consumer preferences — it is a measure of the disutility faced by a consumer in order to “orient” her to the offerings of a particular site (in other words, the difference is more in terms of the users' perception about the two platforms rather than in terms of their actual functionality). As compared to the standard Hotelling setup between the two platforms, our model introduces another dimension of competition between the sellers who are on one side of the two platforms, and who are competing for buyers who are on the other side of the platforms.

![](/api/attachments/VESNGQRY/fulltext/images/2666677f7696f1fe00dca8ea1dfce32cdb75804a651b153f79223557b5244797.jpg)  
Fig. 1. Potential user distribution for the competing platforms.

The number of sellers and the number of buyers both are normalized to 1. All the sellers sell the same product, and sellers on a particular platform sell the product at the same price as every other seller on that platform. We assume that the number of buyers who will actually buy the product will depend on the price the sellers charge, and this number will decrease linearly as the price increases. A fraction of buyers n<sup>1</sup> will prefer platform 1, while the rest of the buyers 1−n<sup>1</sup> will go to platform 2. Buyers face a transportation/<sup>fi</sup>t cost (unit cost t) in order to access either platform. A number of sellers n<sup>1</sup> will join platform 1, while the rest will join platform 2. For simplicity, as in Armstrong [1], we assume that both the buyers and sellers are single-homing. Table 1 in the Appendix provides a summary of the notation used throughout the text.

The utility the buyers can derive depend on the number of sellers on the same platform. For example, in an online shopping site like Amazon. com or Buy.com, this utility is positively correlated with the number of sellers on the platform. We model this cross-group network utility of the platform i(i=1,2) with the parameter $\alpha _ { i } .$ Buyers also experience a within-group network effect — for example, in a online auction site, buyers face an increasing disutility with every additional user visiting the platform, as the presence of other buyers makes it hard for the buyer to purchase the goods at a bargain. A similar experience is observed in the conventional market (i.e. shopping mall), where the buyer's utility is positively related to the number of stores the shopping mall has but face an increasing disutility with every additional buyer visiting the mall as the increasing crowds make the shopping experience less pleasurable. On the other hand, users of social networking platforms (i.e. MySpace.com vs. Facebook.com) or online dating platforms (i.e. Match.com vs. eHarmony. com) derive positive utilities with every additional user registered with the platform as the increased users adding up the chances for meeting new friends or <sup>fi</sup>nding the perfect date. We therefore model this withingroup network utility/disutility of the platform i(i=1,2) with the parameter $\beta _ { i } - \mathsf { a }$ modeling artifact that has so far been overlooked in the literature on two-sided markets. (e.g. [5,6,15]). Note that $\beta _ { i }$ can be either positive or negative depending on the nature of the platform.

Platform 1 charges a <sup>fi</sup>xed fee $F _ { 1 }$ to sellers on platform 1, while platform 2 charges a <sup>fi</sup>xed fee $F _ { 2 }$ to sellers on platform 2.

The utility of the marginal buyer on either platform is given by the following expressions:

$$
u _ {B} ^ {1} = \alpha_ {1} n _ {S} ^ {1} + \beta_ {1} n _ {B} ^ {1} + v - (\widehat {p} - a n _ {S} ^ {1}) - n _ {B} ^ {1} t\tag{1}
$$

$$
u _ {B} ^ {2} = \alpha_ {2} \left(1 - n _ {S} ^ {1}\right) + \beta_ {2} \left(1 - n _ {B} ^ {1}\right) + v - \left(\widehat {p} - a \left(1 - n _ {S} ^ {1}\right)\right) - \left(1 - n _ {B} ^ {1}\right) t\tag{2}
$$

v is the gross utility the buyers can derive from the product. $\widehat { P }$ is the monopoly price, while ${ \widehat { p } } - a n _ { S } ^ { 1 }$ is the price of the product induced by competition on platform 1 when the number of sellers on that platform is n<sub>S</sub><sup>1</sup>.

The sellers' utility function on each platform is given by:

$$
u _ {S} ^ {1} = \left(n _ {B} ^ {1} - \gamma (\widehat {p} - a n _ {S} ^ {1})\right) (\widehat {p} - a n _ {S} ^ {1}) - F _ {1}\tag{3}
$$

$$
u _ {S} ^ {2} = \left(\left(1 - n _ {B} ^ {1}\right) - \gamma \left(\widehat {p} - a \left(1 - n _ {S} ^ {1}\right)\right)\right) \left(\widehat {p} - a \left(1 - n _ {S} ^ {1}\right)\right) - F _ {2}\tag{4}
$$

We note that the number of buyers depends on the price charged by the sellers. Thus, $n _ { B } ^ { 1 } - \gamma ( \widehat { p } - a n _ { S } ^ { 1 } ) \mathrm { i } s$ the number of consumers on platform 1 that actually buy the product.

The pro<sup>fi</sup>t expressions for the two platforms are simply the number of sellers multiplied by the <sup>fi</sup>xed access fee that a platform charges the sellers on that platform:

$$
\Pi_ {1} = n _ {S} ^ {1} F _ {1}\tag{5}
$$

$$
\Pi_ {2} = \left(1 - n _ {S} ^ {1}\right) F _ {2}\tag{6}
$$

## 3. Analysis and results

In equilibrium, the utility derived by buyers on platform 1 will equal to the utility derived by buyers on platform 2, since otherwise sellers will migrate away from the platform that provides lower utility. Similarly, the utility derived by sellers on platform 1 will equal to the utility derived by sellers on platform 2, i.e.

$$
u _ {B} ^ {1} = u _ {B} ^ {2} \text { and } u _ {S} ^ {1} = u _ {S} ^ {2}\tag{7}
$$

We now solve for the optimum prices charged by the two platforms to each of the sellers subject to the participation constraints of the buyers and the sellers, i.e.

$$
u _ {B} ^ {1}, u _ {B} ^ {2}, u _ {S} ^ {1}, u _ {S} ^ {2} \geq 0\tag{8}
$$

In the equilibrium, the number of sellers on each platform is such that the utility derived by each of them on either platform is the same (these utilities are given by Eqs. (3) and (4)). Similarly, in the equilibrium, the number of buyers on each platform is such that the utility derived by each of them on either platform is the same (Eqs. (1) and (2)). We already know the revenues for either platform — they come from the sellers, which are expressed by Eqs. (5) and (6). Maximizing these revenue terms with respect to the <sup>fi</sup>xed prices $F _ { 1 }$ and $F _ { 2 } ,$ and using the fact that the utilities of the buyers and sellers are respectively the same on each platform (Eq (7)) and that these utilities are non-negative (Eq. (8)) gives us the expressions for the optimum $F _ { i }$ to charge for either platform. Solving, we get the following expressions for the optimum prices charged by the two platforms to each of the sellers:

$$
F _ {1} = \frac {1}{6 t - 3 (\beta_ {1} + \beta_ {2})} \left[ \begin{array}{c} - \hat {p} (2 \alpha_ {1} + 4 \alpha_ {2} - \beta_ {1} + \beta_ {2}) + a ^ {2} (3 + 6 t \gamma - 3 \beta_ {1} \gamma - 3 \beta_ {2} \gamma) \\ + a (3 t + \alpha_ {1} + 2 \alpha_ {2} - 2 \beta_ {1} - \beta_ {2} + 6 \hat {p} (- 1 - 2 t \gamma + (\beta_ {1} + \beta_ {2}) \gamma)) \end{array} \right]\tag{9}
$$

$$
F _ {2} = \frac {1}{6 t - 3 (\beta_ {1} + \beta_ {2})} \left[ \begin{array}{c} - \hat {p} (4 \alpha_ {1} + 2 \alpha_ {2} + \beta_ {1} - \beta_ {2}) - 3 a ^ {2} (- 1 + (- 2 t + \beta_ {1} + \beta_ {2}) \gamma) \\ - a (- 3 t - 2 \alpha_ {1} - \alpha_ {2} + \beta_ {1} + 2 \beta_ {2} + 6 \hat {p} (1 + 2 t \gamma - (\beta_ {1} + \beta_ {2}) \gamma)) \end{array} \right]\tag{10}
$$

Given the surfeit of parameters, it is challenging to explicitly compare expressions (11) and (12). To get some meaningful insights, we therefore compare the values of the two expressions by <sup>fi</sup>rst equating the within-group network effects across the two platforms (while keeping the cross-group network effect parameters different), and subsequently equating the cross-group network effects (while keeping the within-group effects different). The results are detailed in Cases 1 and 2 below:

$$
\text { Case } 1: \alpha_ {1} \neq \alpha_ {2}, \beta_ {1} = \beta_ {2} = \beta
$$

These assumptions help considerably in simplifying the above expressions. A meaningful comparison between the values of the two expressions is found by subtracting one from the other:

$$
F _ {1} - F _ {2} = \frac {(a - 2 \hat {p}) (\alpha_ {1} - \alpha_ {2})}{6 (\beta - t)}\tag{11}
$$

$$
\Pi_ {1} - \Pi_ {2} = \frac {(a - 2 \hat {p}) (\alpha_ {1} - \alpha_ {2})}{6 (\beta - t)}\tag{12}
$$

A similar analysis is carried out under Case 2.

$$
\text { Case   2 }: \alpha_ {1} = \alpha_ {2}, \beta_ {1} \neq \beta_ {2}
$$

$$
F _ {1} - F _ {2} = - \frac {(a - 2 \hat {p}) (\beta_ {1} - \beta_ {2})}{6 t - 3 (\beta_ {1} + \beta_ {2})}\tag{13}
$$

$$
\Pi_ {1} - \Pi_ {2} = - \frac {(a - 2 \hat {p}) (\beta_ {1} - \beta_ {2})}{6 t - 3 (\beta_ {1} + \beta_ {2})}\tag{14}
$$

From the above equations, we can see $F _ { 1 } - F _ { 2 } { = } \Pi _ { 1 } - \Pi _ { 2 } ,$ implying that $\begin{array} { r } { \frac { F _ { 1 } } { F _ { 2 } } = \frac { n _ { s } ^ { 1 } } { 1 - n _ { \mathrm { c } } ^ { 1 } } = \frac { n _ { s } ^ { 1 } } { n _ { \mathrm { c } } ^ { 2 } } . } \end{array}$ We now analyze the results of Eqs. (11)–(14) in <sup>S S</sup>greater depth. Note that ${ \widehat { p } } { - } a n _ { S } ^ { 1 }$ is the price charged by the sellers on platform 1, which is always positive for a pro<sup>fi</sup>t maximizing seller. Since n<sup>1</sup> could range from 0 to $\lvert , \widehat { p } - a n _ { \mathrm { S } } ^ { 1 } > 0$ for all n<sup>1</sup>, 0bn<sup>1</sup>b1. When $\begin{array} { r } { n _ { S } ^ { 1 } = \frac { 1 } { 2 } , } \end{array}$ , we have $\hat { p } - \frac { a } { 2 } > 0$ , and thus $a - 2 \bar { \hat { p } } { < } 0$

Consider now Case 1, where $\alpha _ { 1 } \neq \alpha _ { 2 } , \beta _ { 1 } = \beta _ { 2 } = \beta _ { \cdot }$ . If we assume the <sup>fi</sup>t cost to be low, and speci<sup>fi</sup>cally $t { < } \beta$ (as is arguably the case with some online two-sided platforms which offer similar services, and are viewed by the consumers to be close substitutes), then if $\alpha _ { 1 } { > } \alpha _ { 2 }$ Eqs. (11) and (12) show that $F _ { 1 } { < } F _ { 2 }$ and $\Pi _ { 1 } { < } \Pi _ { 2 } .$ Thus, higher cross-group positive network externalities for the buyers actually lead to lower pro<sup>fi</sup>ts for the platform in such cases. However, if the platforms are suf<sup>fi</sup>ciently differentiated in the minds of the consumers (and speci<sup>fi</sup>cally if $\cdot _ { t > \beta } ) ^ { 2 }$ , the platforms should strive to increase the cross-group network effects for the buyers. The results imply that if two rival platforms are perceived by their potential consumers to be very similar in their offerings, trying to increase the perceived bene<sup>fi</sup>t for the consumers from the sellers might be counterproductive. Rather, it would make more sense for the platforms to <sup>fi</sup>rst increase the perceived differentiation between them, and then cater to their distinct clientele. This result helps explain how the online bookstore Alibris and Half.com have evolved over the years. These two platforms have developed very distinct personalities that have made them attractive to very different types of users — Alibris has positioned itself as the leading vender for older in-print and out-of print books that is appealed to the majority of book collectors. Half.com, on the other hand, provide users a <sup>fi</sup>xed-price, online marketplace to buy and sell new, overstocked or used books at discounted prices and therefore is attractive to most price sensitive consumers (especially college students). Not surprisingly we <sup>fi</sup>nd that both platforms strive to <sup>fi</sup>rst increase the perceived differentiation between them rather than increase the perceived bene<sup>fi</sup>t for consumers by solely increasing the number of sellers on their platforms.

Another good example that echoes our <sup>fi</sup>ndings can be found in the competing social networking platforms. For instance, Facebook has arguably a more “simple” interface with a very limited amount of customization. It has therefore appealed to more “mainstream” users who want to use a social networking site casually without getting bothered by the “nitty-gritty's” of de<sup>fi</sup>ning their social space. MySpace conversely has a more complex interface that can be customized extensively by a user, and therefore has appealed more to those users who enjoy that customization [4].

Consider now Case 2, when we keep the cross-group network effects to be the same, and instead vary the within-group network effects, i.e. $\alpha _ { 1 } = \alpha _ { 2 } , \beta _ { 1 } \neq \beta _ { 2 }$ . If the <sup>fi</sup>t cost t is low enough (speci<sup>fi</sup>cally $t < \frac { \beta _ { 1 } + \beta _ { 2 } } { 2 } )$ ), and $\beta _ { 1 } { > } \beta _ { 2 } , \mathtt { E q s . } \left( 1 3 \right)$ and (14) show that F bF and Π bΠ . A reverse effect is observed when the <sup>fi</sup>t cost is high. The takeaway from the results is similar to Case 1: two similarly perceived two-sided market platforms end up harming their prospects by trying to increase the within-group network effects for their consumers.

The comparative statics results (see the Appendix) lend additional credence to this intuition. In the most generalized form, the surfeit of parameters do not allow us to derive very meaningful insights (since the parameters $\alpha _ { i }$ and $\beta _ { i }$ can be either positive or negative), and so we investigate the special Cases 1 and 2 elaborated earlier. In Case 1, when $\alpha _ { 1 } \neq \alpha _ { 2 } , \beta _ { 1 } = \beta _ { 2 } = \beta ,$ if we assume the cross-group network effects to be positive, we will always have $\begin{array} { r } { \frac { \partial F _ { i } } { \partial t } > 0 ; } \end{array}$ in other words, as the platforms differentiate themselves more prominently, they can charge higher prices from the sellers. In Case 2 (where $\alpha _ { 1 } = \alpha _ { 2 } = \alpha , \beta _ { 1 } \neq \beta _ { 2 } )$ , the sign $\mathrm { o f } \frac { \partial F _ { i } } { \partial t }$ depends on the sign of $6 a + 6 \alpha - \beta _ { 1 } + \beta _ { 2 } .$ If we assume the cross-group network effects to be positive, and if one assumes that the within-group network effects have the same sign regardless of the platform, unless the absolute value of one of the $\beta _ { i }$ is signi<sup>fi</sup>cantly higher than the other, we will always have $\frac { \partial F _ { i } } { \partial t } > 0 . \mathrm { T }$ he results are summarized in the following proposition.

Proposition 1. When two competing two-sided market platforms are perceived to be very similar among consumers (who are granted free access), increasing the network effects (either cross-group or withingroup) of one platform will lead to lower pro<sup>fi</sup>ts for the platform with respect to the other platform. Increasing the differentiation between the platforms, however, helps reverse these effects.

## 4. Conclusion

This research note extends the <sup>fi</sup>ndings on two-sided market platforms in the extant literature. These online platforms serve as intermediaries who bring together two classes of agents – the sellers and the consumers – with the former competing for the business of the latter. As is common in the online world, the platforms earn their revenue by charging a <sup>fi</sup>xed price to the sellers for allowing them to participate in the platform, while the consumers are granted free access. We construct a stylized model of competition between two online platforms that are competing for the sellers by attracting consumers at the other side of the platforms.

The extant literature has largely abstracted away the competition between the sellers in order to analyze the competition between twosided platforms. In contrast, the speci<sup>fi</sup>c nature of online platforms allow us to consider the effects of both the competition between platforms to accumulate buyers and sellers who transact through the platforms and that between the sellers (who compete for the buyers) simultaneously.

The results of the stylized modeling reveal some seemingly counterintuitive results that have interesting implications for the strategies that might be employed by competing two-sided market platforms, especially in the online world, where it is relatively easy for consumers to shift from one platform to another. Trying to increase the cross-network bene<sup>fi</sup>ts of the consumers (i.e. the marginal bene<sup>fi</sup>t that the consumers accrue from an additional seller on the other side of the platform) might actually lower the pro<sup>fi</sup>ts of the platforms. Instead, the platforms should spend their resources to increasingly differentiate themselves from the rival platforms, a move that will allow them to charge higher prices from the sellers and thus increase their pro<sup>fi</sup>ts. Our results explain why the online social networking sites such as Facebook and MySpace have developed very distinct “personalities” to attract very different types of users even though their core functionalities remain very similar.

In our research, we modeled the buyers and sellers to be singlehoming. Future research can look at the case in which sellers and buyers might be multi-homing, that is, they can participate in multiple platforms in order to reap maximal network bene<sup>fi</sup>ts and pro<sup>fi</sup>ts. While the assumption of single-homing is realistic enough in many environments (especially if the platforms are sharply differentiated with respect to each other, and therefore attract very different types of consumers) a multihoming model is more realistic and thus might give us more insight on the competitions among sellers and buyers. Considering multi-homing among agents also has potential to counteract the tendency towards tipping and the lock-in effects in platforms with strong cross-group network externalities. Another area of research would be to study the use of more <sup>fl</sup>exible pricing strategies (e.g. a two-tier pricing mechanism that combines a <sup>fi</sup>xed fee with transaction fees) and investigate their impact on the competition between platforms. While all such questions are available for future research, we feel that the present analysis contributes to the understanding of the fundamental interaction underlying the competition in two-sided markets.

## Appendix

Comparative statics results

$$
\alpha_ {1} \neq \alpha_ {2}, \beta_ {1} \neq \beta_ {2}
$$

$$
\frac {\partial F _ {1}}{\partial t} = - \frac {(a - 2 \hat {p}) (6 a + 2 \alpha_ {1} + 4 \alpha_ {2} - \beta_ {1} + \beta_ {2})}{3 (- 2 t + \beta_ {1} + \beta_ {2}) ^ {2}}
$$

$$
\frac {\partial F _ {2}}{\partial t} = - \frac {(a - 2 \hat {p}) (6 a + 4 \alpha_ {1} + 2 \alpha_ {2} + \beta_ {1} - \beta_ {2})}{3 (- 2 t + \beta_ {1} + \beta_ {2}) ^ {2}}
$$

$$
\alpha_ {1} \neq \alpha_ {2}, \beta_ {1} = \beta_ {2}
$$

$$
\frac {\partial F _ {1}}{\partial t} = - \frac {(a - 2 \hat {p}) (3 a + \alpha_ {1} + 2 \alpha_ {2})}{6 (t - \beta) ^ {2}}
$$

$$
\frac {\partial F _ {2}}{\partial t} = - \frac {(a - 2 \hat {p}) (3 a + 2 \alpha_ {1} + \alpha_ {2})}{6 (t - \beta) ^ {2}}
$$

$$
\alpha_ {1} = \alpha_ {2}, \beta_ {1} \neq \beta_ {2}
$$

$$
\frac {\partial F _ {1}}{\partial t} = - \frac {(a - 2 \hat {p}) (6 a + 6 \alpha - \beta_ {1} + \beta_ {2})}{3 (- 2 t + \beta_ {1} + \beta_ {2}) ^ {2}}
$$

$$
\frac {\partial F _ {2}}{\partial t} = - \frac {(a - 2 \hat {p}) (6 a + 6 \alpha + \beta_ {1} - \beta_ {2})}{3 (- 2 t + \beta_ {1} + \beta_ {2}) ^ {2}}
$$

<table><tr><td> $n_{B}^{1}$ </td><td>The proportion of the buyers who prefer platform 1</td></tr><tr><td> $1-n_{B}^{1}$ </td><td>The proportion of the buyers who prefer platform 2</td></tr><tr><td>t</td><td>Unit transportation cost</td></tr><tr><td> $n_{S}^{1}$ </td><td>The proportion of the sellers who join platform 1</td></tr><tr><td> $1-n_{S}^{1}$ </td><td>The proportion of the sellers who join platform 2</td></tr><tr><td> $\alpha_{i}$ </td><td>Cross-group network externalities of platform i, (i=1,2)</td></tr><tr><td> $\beta_{i}$ </td><td>Within-group network utility of platform i, (i=1,2)</td></tr><tr><td> $F_{i}$ </td><td>Fixed fee charged to sellers on platform i, (i=1,2)</td></tr><tr><td> $u_{B}^{i}$ </td><td>Buyers&#x27; utilities on platform i, (i=1,2)</td></tr><tr><td>v</td><td>Gross utility derived from the purchased product</td></tr><tr><td> $\widehat{P}$ </td><td>Monopoly price a seller can charge for the product he sells.</td></tr><tr><td>a</td><td>Coefficient of competition among sellers</td></tr><tr><td>γ</td><td>Coefficient of price sensitivity among buyers</td></tr><tr><td> $\Pi_{i}$ </td><td>Net profit of platform i</td></tr></table>

## References

[1] M. Armstrong, Competition in two-sided markets, RAND Journal of Economics 37 (3) (2006) 668–691.

[2] M. Armstrong, J. Wright, Two-sided markets, Competitive Bottlenecks and Exclusive Contracts. Economic Theory 32 (2) (2007) 353–380.

[3] A. Basu, S. Muylle, Online support for commerce processes by web retailers Decision Support Systems 34 (2002) 379–395.

[4] d boyd,, Why youth (heart) social network sites, in: David Buckingham (Ed.), The Role of Networked Publics in Teenage Social Life, in Youth, Identity and Digital Media, The MIT Press, Cambridge, MA, 2008, pp. 119–142.

[5] B. Caillaud, B. Jullien, Competing cybermediaries, European Economic Review 45 (4–6) (2001) 797–808.

[6] B. Caillaud, B. Jullien, Chicken & egg: competition among intermediation service providers, RAND Journal of Economics (2003) 309–328.

[7] A.M. Chircu, V. Mahajan, Managing electronic commerce retail transaction costs for customer value, Decision Support Systems 42 (2006) 898–914.

[8] S. Chun, J. Kim, Pricing strategies in B2C electronic commerce: analytical and empirical approaches, Decision Support Systems 40 (2005) 375–388.

[9] Economist. Fun with network effects. October 13 2009 [cited 2009 December 6]; Available from: http://www.economist.com/blogs/freeexchange/2009/10/ fun\_with\_network\_effects

[10] D.S. Evans, Some empirical aspects of multi-sided platform industries, The Review of Network Economics 2 (3) (2003) 191–209.

[11] N. Granados, A. Gupta, R.J. Kauffman, Designing online selling mechanisms: transparency levels and prices, Decision Support Systems 45 (2008) 729–745.

[12] A. Gupta, S. Ba, Z. Walter, Risk pro<sup>fi</sup>le and consumer shopping behavior in electronic and traditional channels, Decision Support Systems 38 (2004) 347–367.

[13] H. Hotelling, Stability in competition, The Economic Journal 39 (153) (1929) 41–57.

[14] S. Muylle, A. Basu, Online support for business processes by electronic intermediaries, Decision Support Systems 45 (2008) 845–857.

[15] J.C. Rochet, J. Tirole, Platform competition in two-sided markets, Journal of the European Economic Association 1 (4) (2003) 990–1029.

[16] J.C. Rochet, J. Tirole, Two-sided markets: a progress report, RAND Journal of Economics (2006) 645–667.

[17] R. Roson, Two-sided markets: a tentative survey, Review of Network Economics 4 (2) (2005) 142–160.

[18] M. Rysman, The economics of two-sided markets, Journal of Economic Perspectives 23 (3) (2009) 125–143.

[19] M.J. Shaw, D.M. Gardner, H. Thomas, Research opportunities in electronic commerce, Decision Support Systems 21 (1997) 149–156.
