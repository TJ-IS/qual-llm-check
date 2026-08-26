---
otero_id: 8624
otero_key: "B847HUSP"
title: "Price discount and capacity planning under demand postponement with opaque selling"
authors: "Zhengping Wu; Jianghua Wu"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.02.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Price discount and capacity planning under demand postponement with opaque selling Zhengping Wu <sup>a</sup>, Jianghua Wu <sup>b,</sup>⁎

<sup>a</sup> Whitman School of Management, Syracuse University, Syracuse, NY 13244-2450, United States

<sup>b</sup> School of Business, Renmin University of China, Beijing 100872, China

## a r t i c l e i n f o

Available online xxxx

Keywords: Demand management Early order discounts Newsvendor model Opaque selling

## a b s t r a c t

In this paper, we consider the opaque selling strategy of a <sup>fi</sup>rm that uses a price discount to induce demand postponement. Under demand postponement, the <sup>fi</sup>rm offers a price discount to advance customers in exchange for the option to ful<sup>fi</sup>ll their orders after the spot demand has been satis<sup>fi</sup>ed. Advance customers who take the discount commit their orders early, but the actual delivery time is chosen by the <sup>fi</sup>rm. In effect, the price discount enables the <sup>fi</sup>rm to create a capacity buffer for the spot demand. We formulate a two-stage stochastic program, and characterize the <sup>fi</sup>rm's optimal capacity and price discount decisions to maximize its expected pro<sup>fi</sup>t. We <sup>fi</sup>nd that the driver of demand postponement is that the option to postpone allows the <sup>fi</sup>rm to not only use less safety stock to hedge against the risk in the spot demand, but also reduce capacity waste. In addition, the <sup>fi</sup>rm might gain from the potentially lower capacity cost for postponed demand. In the event that the advance demand information can be utilized to update the regular demand distribution, the <sup>fi</sup>rm can garner additional bene<sup>fi</sup>ts from information updating through the early orders. Through numerical experiments, we demonstrate the signi<sup>fi</sup>cance of the value of demand postponement and information updating, and assess the impact of market conditions on the <sup>fi</sup>rm's optimal capacity and price discount decisions.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

The rapid advancement of information technology has changed the way the business world operates. For instance, many major Chinese travel agencies have moved their business online in recent years (e.g., Aoyou.com). While the addition of the online channel allows these <sup>fi</sup>rms to reach out to a larger customer base, it also ampli<sup>fi</sup>es the demand variance and operational risk, especially during holiday seasons with rush demand. As a result, matching supply and demand, a constant challenge faced by business executives, becomes even more demanding.

Commonly used matching strategies to deal with operational risk, as extensively reviewed by Tang [1], include supply management, demand management, product management, information management, etc. Under circumstances where demand is highly volatile, <sup>fi</sup>rms often use various demand management strategies to manipulate the uncertain demand dynamically so that the modi<sup>fi</sup>ed demand is better matched by supply.

Along the demand management line of research, innovative approaches like shifting demand across time, across markets, and across products have been studied. Of particular interest is the strategy of shifting demand across time. While it is common in many industries to use an advance booking discount program to enable a <sup>fi</sup>rm to shift customer demand earlier (e.g., Tang et al. [2]), we consider in this paper a different approach—demand postponement through price discount—for the <sup>fi</sup>rm to shift customer demand later. Under demand postponement, the <sup>fi</sup>rm offers a price discount to customers in exchange for the option to ful<sup>fi</sup>ll their orders at a later time. Customers who take the discount commit their orders early, but the actual delivery time of their orders is chosen by the <sup>fi</sup>rm. In effect, the price discount enables the <sup>fi</sup>rm to postpone these early orders to a later period, if necessary. From the perspective of the customers who order early, the product is opaque as the order ful<sup>fi</sup>llment time is uncertain at the time of ordering.

The demand postponement strategy is made possible by exploiting customer heterogeneity regarding time and price, and thus generates a price discrimination effect. This is in the same spirit as the emerging opaque selling in the travel industry, such as last-minute sales and selling <sup>fl</sup>exible products (see Jerath et al. [3] and Jiang [4] for speci<sup>fi</sup>c examples). In opaque selling, service providers (e.g., airlines, hotels) aim to use opaque products to better utilize their limited capacity and maximize the revenue. In this paper, however, we take the perspective of an intermediary (e.g., a travel agency) that reserves and takes ownership of capacity (e.g., <sup>fl</sup>ight seats and hotel rooms) from service providers and sells them to two classes of uncertain demand in a holiday season. We investigate the price discount and capacity decision of the travel agency.

To motivate our model, consider the so-called Golden Week (GW) economy, an emerging phenomenon in the Chinese tourism industry. Recently, to stimulate the domestic tourism economy, the central government has set up two week-long national holidays: the National Day Golden Week in October and the Spring Festival Golden Week in

January or February. These GWs see the largest <sup>fl</sup>ows of tourists, many of whom typically join group tours organized by travel agencies (Weisenthal [5]). Travel agencies reserve capacity from service providers in advance and then sell them in the form of bundled packages to tourists for pro<sup>fi</sup>t (note that the capacity reservation here is similar to inventory acquisition, which is completely different from commission-based consignment sales). The capacity decision of travel agencies is a challenging one: if they do not reserve enough, they may lose the opportunity to capitalize on the high traf<sup>fi</sup>c and high markups during GWs (WantChinaTimes.com [6]). If they reserve too much, however, they may get hit by the large swings commonly observed in tourist demand. A local travel agency in Sanya city of southern China, for instance, is reported to have lost nearly ¥2 million due to average daily leftovers of 100 to 200 reserved hotel rooms during the 2010 Spring Festival GW (Lei [7]).

An effective strategy to help travel agencies hedge against the demand risk would be to exploit the customer heterogeneity. Since some tourists are <sup>fl</sup>exible in terms of when to have their vacations, such losses can be largely reduced by selling opaque tour packages with <sup>fl</sup>exible consumption time to better match the demand with capacity: suppose there are two demand classes $X _ { 1 }$ and $X _ { 2 } ,$ differing in the timing of reservation. The advance demand class $X _ { 1 }$ makes reservations for the GW in the advance period (before the GW), which is before the travel agency commits capacity for the GW, while the spot demand class $X _ { 2 }$ arrives in the regular period (the GW) before which the capacity decision has been made. The $X _ { 1 }$ group consists of heterogeneous customers with different price sensitivities and time requirements. At the beginning of the advance period, the agency offers a price discount to the advance demand class $X _ { 1 } .$ . Customers in this class who are more price sensitive but less time sensitive (e.g., college students with onemonth winter vacation) take the discount and are willing to be postponed. Others in this class, $\mathrm { i . e . }$ , advance customers with stricter time requirement, will pay the regular price and have their reservations guaranteed during the GW. Effectively, the agency uses a price discount to induce a fraction of the advance customers to agree to demand postponement. The orders from the spot demand class $X _ { 2 }$ are generated from spontaneous purchases during the regular period. Therefore, this demand class exhibits little <sup>fl</sup>exibility in terms of consumption date—once capacity shortage occurs, the excess demand in the $X _ { 2 }$ class is lost.

The bene<sup>fi</sup>t of the postponable demand then becomes evident: the agency can take advantage of the postponable demand to reserve less capacity for the GW. In the event that the spot demand turns out to be large, the postponable demand can be indeed postponed to reduce stockouts of the spot demand. On the other hand, in case the spot demand realization turns out to be low, the postponable demand can be satis<sup>fi</sup>ed in the GW without postponement to reduce capacity waste. It is worth noting that our model framework is also applicable to a wide array of manufacturing settings when advance booking discounts are available. Readers are referred to Tang et al. [2] for more examples.

Essentially, the value of demand postponement accrues from the fact that the postponable demand can be used as a capacity buffer during the regular period. The tradeoffs, of course, are to balance the revenue forgone due to the price discount with the value of the option to postpone. In this paper, we use a stylized model to capture the above tradeoffs and evaluate the bene<sup>fi</sup>t of demand postponement through opaque selling. In the model, we formulate and solve a two-stage stochastic program to determine the <sup>fi</sup>rm's optimal price discount and capacity choice. We <sup>fi</sup>nd that the driver of the demand postponement strategy is that the <sup>fi</sup>rm's <sup>fl</sup>exibility to deliver the early orders at a later time enables it to not only use less safety stock to hedge against uncertainties in the spot demand, but also reduce capacity waste in the regular period. In addition, opaque selling offers the <sup>fi</sup>rm the opportunity to speculate the timing of satisfying the postponable demand: if the capacity cost is higher in the postponement period than in the regular period, the <sup>fi</sup>rm will build a capacity no less than the postponable demand in the regular period, and use the postponable demand as a capacity buffer for the spot demand; otherwise, the <sup>fi</sup>rm could bene<sup>fi</sup>t from building less regular period capacity than the postponable demand and intentionally satisfying part of the <sup>fl</sup>exible orders in the postponement period at a lower cost. We make two major contributions to the literature: <sup>fi</sup>rst, we integrate the demand postponement and opaque selling strategies based on observations from tourism practices. Second, we also incorporate the capacity decision into opaque selling. To the best of our knowledge, this is the <sup>fi</sup>rst paper to endogenize the capacity decision in opaque selling in a newsvendor setting.

The remainder of this paper is organized as follows: Section 2 outlines related literature. We formulate the problem in Section 3 and then solve for the <sup>fi</sup>rm's optimal capacity choice and price discount in Sections 4 and $5 ,$ respectively. An extension to study the value of information updating is presented in Section 6. Section 7 presents numerical studies and additional managerial insights. The paper concludes in Section 8 with a brief discussion of future research directions. All proofs are provided in Appendix A.

## 2. Literature review

Our paper studies the opaque selling strategy in which a price discount is introduced to induce customers to make postponable orders. It is related to three streams of research, namely, research on demand management, inter-temporal pricing, and opaque selling.

## 2.1. Demand management

Our work is most closely related to the research stream broadly categorized as demand management (Tang [1]). Of particular relevance are papers considering shifting demand across time, either backwards or forwards. Iyer et al. [8] is the <sup>fi</sup>rst to examine the bene<sup>fi</sup>t of shifting demand to a later time. They study a model to reduce overall inventory costs by preempting stockouts through demand postponement. Customers whose demands are postponed are paid a reimbursement per unit. However, in their model, customers behave in a passive manner and are forced to accept demand postponement made by the <sup>fi</sup>rms. In our paper, we consider the more realistic case where customers play an active role, i.e., they can self-select whether or not to participate in demand management through their choice of whether to take the price discount. In addition, unlike in their work, customers in our model are heterogenous in terms of their price and order ful<sup>fi</sup>llment time sensitivity.

Using early order (or advance-purchase) discounts to shift demand earlier has also been widely studied in the literature. Weng and Parlar [9] are among the <sup>fi</sup>rst to analyze a model in which the retailer offers a price discount in order to induce customers to pre-commit their orders. The discount helps lock in some customers, thus decreasing the variance of the total demand, as the market size is assumed to be <sup>fi</sup>xed in their base model. They determine the optimal discount rate and the retailer's order quantity. Tang et al. [2] address a similar problem with different features. They consider two market segments, and emphasize the fact the early orders (advance bookings) provide information for the retailer to make a more accurate demand forecast. McCardle et al. [10] extend this work to include retail competition. The value of advance-purchase discounts is also studied by Xie and Shugan [11], who argue that advance-purchase discounts can be a win-win strategy for both some service providers and their customers, if there exists customer uncertainty about future valuations. In terms of the value of advance-purchase discounts, our model differs in two aspects: <sup>fi</sup>rst, we focus on the role of early orders as a capacity buffer, rather than the use of them as advance information to reduce demand uncertainty. Second, while early orders in all the above papers require immediate ful<sup>fi</sup>llment once the product becomes available, our model, in sharp contrast, considers the case where early orders induced by price discounts can be delivered at a later time.

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002

<table><tr><td>Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002</td></tr></table>

## 2.2. Inter-temporal pricing

Recently, inter-temporal pricing has received signi<sup>fi</sup>cant attention in the revenue management community (Shen and Su [12]). Papers on this topic typically study the optimal pricing and capacity (inventory) allocation rules to maximize the revenue/pro<sup>fi</sup>t of a seller. Su and Zhang [13] consider a newsvendor who sells products to strategic consumers in two periods. The seller can initially charge a regular price but will most likely salvage the leftover inventory at a lower salvage price after a random demand is realized. Su [14] incorporates heterogeneous consumers with different valuations and degrees of patience into the same framework. The seller uses a class of pricing policies in which he commits to a price path along with a rationing function that speci<sup>fi</sup>es the fraction of demand that is ful<sup>fi</sup>lled at any given time. Cachon and Swinney [15] consider a similar two-period newsvendor model in which the seller charges a full price during the <sup>fi</sup>rst period and a sale price during the second period if the product is still available. Thus, the sale price depends on the demand realization in the <sup>fi</sup>rst period and remaining inventory. Mersereau and Zhang [16] consider a two-period setting with <sup>fi</sup>xed capacity and an unknown fraction of strategic consumers. The objective of the seller is to <sup>fi</sup>nd the optimal regular price and the clearance price. In a similar setting with full information regarding strategic consumers, Aviv and Pazgal [17] compare two classes of pricing strategies: contingent and announced <sup>fi</sup>xed-discount. In this line of research, the discount price is set to clear the inventory/capacity in the clearance period. However, in our model, the price discount is introduced to attract precommitted orders that can be postponed and serve as the capacity buffer in the regular period.

## 2.3. Opaque selling

A third area related to our paper is the emerging research in opaque selling, which is also termed “probabilistic selling”. Opaque selling is commonly used in online travel market, where some information (e.g., airline, destination) is hidden when customers buy products such as <sup>fl</sup>ight seats and hotel rooms. Based on the Hotelling model, both Jiang [4] and Fay and Xie [18] model a monopolist selling horizontally differentiated products. Jiang [4] considers a <sup>fi</sup>rm selling a morning <sup>fl</sup>ight and an afternoon or night <sup>fl</sup>ight. She shows that when buyer heterogeneity is high enough, the dual-market strategy under which both transparent and opaque tickets are sold can improve the pro<sup>fi</sup>ts of the <sup>fi</sup>rm and consumers. Fay and Xie [18] compare two selling strategies: traditional selling and probabilistic selling, and <sup>fi</sup>nd that pro<sup>fi</sup>t advantage from probabilistic selling is the highest when the horizontal differentiation of the product is at the intermediate level. They also show that offering probabilistic goods can reduce the seller's information disadvantage and improve its pro<sup>fi</sup>t by reducing the mismatch between capacity and demand. Indeed, the demand postponement through opaque selling considered in our model shares the same spirit. Granados et al. [19] analyze the optimal price levels set by airlines across transparent and opaque online travel agencies. They suggest that airlines can increase pro<sup>fi</sup>t by increasing price differentials or in<sup>fl</sup>uencing agencies' transparency differences. Wu et al. [20] propose the opaque pricing strategy, named randomized pricing, for online sellers selling durable products. They show that randomized pricing can improve sellers' pro<sup>fi</sup>t. Some papers also study the opaque selling under competition. Shapiro and Shi [21] model a Salop's market with N competing <sup>fi</sup>rms. They study the effect of the number of competitors on the opaque selling strategy. Fay [22] considers the competition between two <sup>fi</sup>rms and an opaque intermediary, and investigates a variety of contracts between service <sup>fi</sup>rms and the intermediary. Jerath et al. [3] consider both last-minute selling through a direct channel and opaque selling through an opaque intermediary in a duopoly setting. They show that direct last-minute sales are preferred over opaque selling when consumer valuations for travel are high or there is little service differentiation between competing service providers, or both. More recently, some papers study the opaque selling regarding quality-differentiated products. For example, Marom and Seidmann [23] model a random last-minute selling strategy in which the seller may randomly provide high-quality products or low-quality products. They derive the optimal probabilities to offer both products in the last-minute sales. Zhang et al. [24] model a probabilistic selling strategy in which probabilistic products with uncertain quality are sold along with two quality-differentiated products such as the <sup>fi</sup>rst class seats and the economy seats in a <sup>fl</sup>ight. The probabilistic products are targeted at low-type consumers, and play a role to pro<sup>fi</sup>tably dispose excess capacity. In general, the objective of this line of research is to derive the optimal price for a service provider with limited (and given) capacity. However, our model takes the perspective of an intermediary facing uncertain demand and endogenizes the capacity decision. To the best of our knowledge, our paper is among the <sup>fi</sup>rst to incorporate both capacity planing and pricing decision into opaque selling through demand postponement.

## 3. The model

## 3.1. Notation

For convenience, a list of notation used in this paper is summarized below.

$X _ { 1 }$ advance demand in the advance period, unfolds after the price discount decision but before the capacity decision;

$X _ { 2 }$ random spot demand in regular period, unfolds after capacity is built;

$f _ { i } ( x _ { i } )$ probability density function of demand $X _ { i } , i = 1 , 2 ;$

$F _ { i } ( x _ { i } )$ cumulative density function of demand $X _ { i } , i = 1 , 2 ;$

$c _ { r }$ unit capacity cost in the regular period, $c _ { r } < r ;$

$c _ { p }$ unit capacity cost in the postponement period, $c _ { p } < r ;$

$r$ regular price (unit revenue);

$q$ price discount (percent off the regular price r), $0 \leq q \leq 1 ;$

$\gamma ( q )$ fraction of advance customers who take the price discount; $0 \leq \gamma ( q ) \leq 1 ; \gamma ( q )$ is strictly increasing in q;

$k$ additional capacity (in addition to $( 1 - \gamma ( q ) ) x _ { 1 } )$ built in the regular period;

$k _ { t }$ total capacity the <sup>fi</sup>rm builds in the regular period, $k _ { t } = ( 1 -$ $\gamma ( q ) x _ { 1 } + k .$

## 3.2. The sequence of events

The <sup>fi</sup>rm faces two demand classes: the advance demand $X _ { 1 }$ that occurs in the advance period, and the spot demand $X _ { 2 }$ that occurs in the spot period (also called the regular period), as shown in Fig. 1 below.

Since capacity is built after the realization of the advance demand but before the spot demand, the main challenge is how to better plan capacity for the spot demand $X _ { 2 } .$ One idea is to leverage the already realized advance demand $x _ { 1 }$ to better serve the spot demand $X _ { 2 } .$ . Indeed, a price discount provided by the <sup>fi</sup>rm to induce part of $x _ { 1 }$ to agree to possible ful<sup>fi</sup>llment in the postponement period, rather than the regular period, makes such leverage possible.

![](/api/attachments/B847HUSP/fulltext/images/cf3ad47d58ff8058120642ee05919c3884ac0092c486c7617cd5cc0125806ba5.jpg)  
Fig. 1. The sequence of events.

A detailed description of the sequence of events is as follows:

1. At the beginning of the advance period, the <sup>fi</sup>rm announces a price discount q.

2. The advance demand $x _ { 1 }$ unfolds in the advance period. In response to the price discount $q ,$ a fraction $\gamma ( q )$ of $x _ { 1 }$ order at the discount price $( 1 - q ) t$ r and agree to possible postponement of their orders, while the remaining $( 1 - \gamma ( q ) ) x _ { 1 }$ commit their orders at the regular price r and prefer to have the ful<sup>fi</sup>llment guaranteed in the regular period.

3. At the beginning of the regular period, the <sup>fi</sup>rm builds (subcontracts) total capacity $k _ { t } = ( 1 - \gamma ( q ) ) x _ { 1 } +$ k at the unit capacity cost $c _ { r } .$ The <sup>fi</sup>rst component of the total capacity $( 1 - \gamma ( q ) ) x _ { 1 } ,$ is reserved for the time sensitive advance customers who place advance orders to have their ful<sup>fi</sup>llment guaranteed in the regular period. The second component k is used to meet the remaining aggregate demand $\gamma ( q ) x _ { 1 } + X _ { 2 } .$

4. The random demand $X _ { 2 }$ reveals in the regular period. If the capacity k is suf<sup>fi</sup>cient, then all demand $\gamma ( q ) x _ { 1 } + x _ { 2 }$ is satis<sup>fi</sup>ed in the regular period. Otherwise, if the <sup>fi</sup>rm falls short of capacity, $\mathrm { i } . \mathrm { e } . , \gamma ( q ) x _ { 1 } + x _ { 2 } > k ,$ then the spot demand $x _ { 2 }$ takes priority and the <sup>fi</sup>rm defers up to $\gamma ( q ) x _ { 1 }$ demand to the postponement period. In the event that $x _ { 2 } > k ,$ all of $\gamma ( q ) x _ { 1 }$ is postponed, and the excess demand $x _ { 2 } - k$ is lost.

5. In the postponement period, the <sup>fi</sup>rm purchases just enough capacity at unit cost $c _ { p }$ to satisfy the postponed demand, if any.

A few remarks are in order. First, throughout the paper, the capacity discussed refers to short term capacity, which can be outsourced through subcontracting. Therefore, the only relevant capacity cost is the variable cost, and no <sup>fi</sup>xed capacity cost is considered. In this sense, the terms capacity and inventory can be used interchangeably in our context.

Second, besides the regularity conditions that $\gamma ( 0 ) = 0$ and $\gamma ( 1 ) =$ 1, it is appealing to assume that the response function $\gamma ( q )$ is strictly increasing in $q , \mathrm { i . e . , } \partial \gamma ( q ) / \partial q > 0 .$ . This assumption is congruent with the intuition that a deeper discount (a larger q) induces more customers (a larger $\gamma ( q ) )$ from the advance demand class $X _ { 1 }$ to agree to postponement. Further, it implies a one-to-one mapping between q and $\gamma ( q )$

Third, in practice, the unit capacity cost $c _ { r }$ in the regular period can be either greater or less than the unit cost $c _ { p }$ in the postponement period, depending on the context. For instance, if the regular period is generally a peak period and consequently capacity is more dif<sup>fi</sup>cult to acquire, then $c _ { r } > c _ { p } .$ In other contexts, if the product does not exhibit strong seasonality, then it might be the case that $C _ { r } \leq C _ { p } ,$ , because the capacity in the regular period can be built well in advance of the spot demand whereas the capacity for the postponement period has to be rushed after the spot demand realization in the regular period. In such contexts, the postponement period capacity acquisition is similar to an emergency shipment, which incurs a higher cost because of the expedited production and shipment (Cachon and Swinney [15]). For the above-mentioned reasons, no speci<sup>fi</sup>c relationship between $c _ { r }$ and $c _ { p }$ is assumed in our model. Instead, we focus on how their relationship drives our modeling results.

In what follows, we formulate a two-stage stochastic program, and take the standard backward induction approach to solve the <sup>fi</sup>rm's problem. Two steps are involved in the solution procedure:

Step 1: choose capacity $k _ { t \cdot }$ . At the beginning of the regular period, given the discount q and the subsequently realized advance demand $x _ { 1 } ,$ the <sup>fi</sup>rm chooses the total capacity $k _ { t } = ( 1 - \gamma ( q ) ) x _ { 1 } + k$ to satisfy the aggregate demand $x _ { 1 } + X _ { 2 } .$ . As explained earlier in the sequence of events, the capacity k is meant to meet the demand $\gamma ( q ) x _ { 1 } + X _ { 2 }$ . Since $( 1 - \gamma ( q ) ) x _ { 1 }$ can be treated as a given constant, the capacity decision reduces to determining the additional capacity k.

Step 2: choose the price discount q. At the beginning of the advance period, the <sup>fi</sup>rm seeks the optimal price discount $q$ to maximize its expected (over possible realizations of $X _ { 1 } )$ pro<sup>fi</sup>t. Since each value of q can be uniquely mapped to a corresponding $\gamma ( q )$ , we choose to work on $\gamma ( q )$ rather than q for analytical convenience.

## 4. The optimal capacity choice

For notational brevity, in the following text, we omit the argument of $\gamma ( q )$ and simply write it as $\gamma$ whenever doing so does not cause confusion. In the same spirit, we express the capacity k without its argument γ.

When it comes to the capacity decision for the regular period, the advance demand $x _ { 1 }$ has already been realized. Recall that $( 1 - \gamma ) x _ { 1 }$ has to be satis<sup>fi</sup>ed in the regular period, whereas all or part of $\gamma x _ { 1 }$ can be deferred to the postponement period. This explains why we write the <sup>fi</sup>rm's total capacity as $k _ { t } = ( 1 - \gamma ) x _ { 1 } + k$ : the second part k is used to meet the spot demand $X _ { 2 }$ as much as possible, and any surplus is used to <sup>fi</sup>ll part or all of $\gamma x _ { 1 }$

As discussed earlier, the postponable demand $\gamma x _ { 1 }$ creates a capacity buffer in the regular period. Nevertheless, although the postponable amount of demand is always $\gamma x _ { 1 }$ , it is instrumental to note that the amount of capacity buffer created may be further capped by the capacity k. Indeed, the capacity buffer is only up to $\operatorname* { m i n } ( \gamma x _ { 1 } , k )$ . Therefore, the relationship between k and $\gamma x _ { 1 }$ is critical as it determines the amount of capacity buffer and affects how we write the objective function. Various forces drive how k compares with $\gamma x _ { 1 }$ . On the one hand, $\gamma x _ { 1 }$ has been revealed and has to be satis<sup>fi</sup>ed sooner or later. Therefore, it makes sense to build more capacity in the regular period such that $k > \gamma x _ { 1 }$ . Because in the event that the spot demand realization $x _ { 2 }$ is large, the amount of capacity that can be used to absorb the demand surge is at least $\gamma x _ { 1 }$ and lost sales can be mitigated. On the other hand, $\operatorname { i f } x _ { 2 }$ turns out to be small, capacity waste can be reduced if $k < \gamma x _ { 1 }$ . In addition, if $c _ { p } < c _ { r }$ i.e., it is less costly to build capacity in the postponement period, the <sup>fi</sup>rm may take advantage of the <sup>fl</sup>exibility of $\gamma x _ { 1 }$ and build a small capacity k (less than $\gamma x _ { 1 } )$ in the regular period. We next take a close look at how the relationship between k and $\gamma x _ { 1 }$ determines the objective function.

$\mathrm { I f } \ k < \gamma x _ { 1 }$ , then there are 3 cases to consider: (i) $x _ { 2 } \leq k - \gamma x _ { 1 } ;$ : the capacity k is suf<sup>fi</sup>cient to satisfy both x and the postponable demand $\gamma x _ { 1 } .$ . As a result, all demands are satis<sup>fi</sup>ed in the regular period and nothing is postponed; $( \mathrm { i i } ) k - \gamma x _ { 1 } < x _ { 2 } \leq$ k: the capacity k is suf<sup>fi</sup>cient for $x _ { 2 }$ , but the surplus can only cover the postponable demand $\gamma x _ { 1 }$ partially. As a result, $\gamma x _ { 1 } - ( k - x _ { 2 } ) = \gamma x _ { 1 } - k + x _ { 2 }$ is postponed; (iii) $x _ { 2 } > k$ : the capacity k is not even enough for $x _ { 2 } .$ As a result, the amount of $x _ { 2 }$ in excess of k is lost, and all of $\gamma x _ { 1 }$ is postponed.

$\operatorname { I f } k \leq \gamma x _ { 1 }$ , then at least part of $\gamma x _ { 1 }$ will be postponed. We consider the following 2 cases: $( \mathrm { i } ) x _ { 2 } \leq$ k: the capacity k is suf<sup>fi</sup>cient for $x _ { 2 }$ and the surplus is used for the postponable demand $\gamma x _ { 1 }$ . The unmet portion of the postponable demand $\gamma x _ { 1 } - ( k - x _ { 2 } ) = \gamma x _ { 1 } - k + x _ { 2 }$ is postponed; (ii) $x _ { 2 } > k \colon$ the capacity k is not even enough for x . As a result, the amount of $x _ { 2 }$ in excess of k is lost, and all of $\gamma x _ { 1 }$ is postponed.

Summing up the above scenarios, we can now write the regular period objective function $J _ { 2 } ( k )$ as a step function as follows:

$$
J _ {2} (k) = \left\{ \begin{array}{l l} J _ {2} ^ {a} (k), & \text { if } k \geq \gamma x _ {1}; \\ J _ {2} ^ {b} (k), & \text { if } k \leq \gamma x _ {1}, \end{array} \right.
$$

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002

where

$$
\begin{array}{l} J _ {2} ^ {a} (k) = r (1 - \gamma) x _ {1} + (1 - q) r \gamma x _ {1} - c _ {r} [ (1 - \gamma) x _ {1} + k ] \\ \qquad + \int_ {0} ^ {k - \gamma x _ {1}} r x _ {2} f _ {2} (x _ {2}) d x _ {2} + \int_ {k - \gamma x _ {1}} ^ {k} \Big [ r x _ {2} - c _ {p} (\gamma x _ {1} - k + x _ {2}) \Big ] f _ {2} (x _ {2}) d x _ {2} \\ \qquad + \int_ {k} ^ {\infty} \Big (r k - c _ {p} \gamma x _ {1} \Big) f _ {2} (x _ {2}) d x _ {2}, \\ J _ {2} ^ {b} (k) = r (1 - \gamma) x _ {1} + (1 - q) r \gamma x _ {1} - c _ {r} [ (1 - \gamma) x _ {1} + k ] \\ \qquad + \int_ {0} ^ {k} \Big [ r x _ {2} - c _ {p} (\gamma x _ {1} - k + x _ {2}) \Big ] f _ {2} (x _ {2}) d x _ {2} + \int_ {k} ^ {\infty} \Big (r k - c _ {p} \gamma x _ {1} \Big) f _ {2} (x _ {2}) d x _ {2}. \end{array}
$$

In the above formulation, $r ( 1 - \gamma ) x _ { 1 }$ is the revenue from timesensitive and thus non-postponable demand, $( 1 - q ) \operatorname { r } \gamma x _ { 1 }$ is the revenue from the postponable demand, and $c _ { r } [ ( 1 - \gamma ) x _ { 1 } + k ]$ is the cost of acquiring capacity $k _ { t } = ( 1 - \gamma ) x _ { 1 } + k$ in the regular period. If any portion of the postponable demand is indeed postponed, then the corresponding unit capacity cost is $c _ { p } .$ . For instance, in the second integral of $J _ { 2 } ^ { a } ( k ) ,$ , the term $c _ { p } ( \gamma x _ { 1 } - k + x _ { 2 } )$ ) re<sup>fl</sup>ects the capacity cost in the postponement period, as $\gamma x _ { 1 } ~ - ~ k ~ + ~ x _ { 2 }$ units of demand is postponed.

To facilitate the solution to the optimal capacity decision, we <sup>fi</sup>rst provide some structural properties of the objective function $J _ { 2 } ( k )$

Lemma 1. The objective function $J _ { 2 } ( k )$ is piecewise concave. Moreover, it is continuous and differentiable at $k = \gamma x _ { 1 }$

Further, one can easily verify that $\partial J _ { 2 } ^ { b } ( k ) / \partial k | _ { k = 0 } = r - c _ { r } > 0$ and $\partial J _ { 2 } ^ { a } ( k ) / \partial k | _ { k } = \infty = - \ c _ { r } < 0$ . These results suggest that $J _ { 2 } ( k )$ <sup>fi</sup>rst increases for small k and then decreases when k is big enough. Together with Lemma 1, these results rule out the possibility of $J _ { 2 } ( k )$ being concave monotone increasing or decreasing. Therefore, an interior optimal solution is guaranteed and is characterized in the following theorem.

Let $F _ { 2 } ^ { - 1 } ( \cdot )$ be the inverse function of $F _ { 2 } ( \cdot )$ and de<sup>fi</sup>ne

$$
\hat {x} _ {1} = F _ {2} ^ {- 1} \left(\frac {r - c _ {r}}{r - c _ {p}}\right).\tag{1}
$$

Theorem 1. The optimal capacity $k ^ { * }$ depends on the postponable demand $\gamma x _ { 1 }$ . Specifically,

(a) $i f \gamma x _ { 1 } \leq \hat { x } _ { 1 }$ , then the optimal capacity $\boldsymbol { k } ^ { * } = k ^ { A } \geq \gamma \boldsymbol { x } _ { 1 }$ and $k ^ { A }$ solves the following equation:

$$
- c _ {r} + c _ {p} \int_ {k ^ {A} - \gamma x _ {1}} ^ {k ^ {A}} f _ {2} (x _ {2}) d x _ {2} + r \int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} = 0.\tag{2}
$$

(b) $i f \gamma x _ { 1 } \geq \hat { x } _ { 1 }$ , then the optimal capacity is $\boldsymbol { k } ^ { * } = \boldsymbol { k } ^ { B } = \hat { \boldsymbol { x } } _ { 1 }$ Moreover, $k ^ { A }$ never exceeds $\hat { x } _ { 1 } , \mathrm { i } . e . , k ^ { A } \leq \hat { x } _ { 1 }$ , and the equality holds $i f$ and only $i f \gamma x _ { 1 } = \hat { x } _ { 1 }$

The technical aspects of Theorem 1 can be explained by the sketch of the objective function $J _ { 2 } ( k )$ in Fig. 2. In $\mathrm { F i g . } 2 ( \mathsf { a } )$ , note that the condition $\gamma x _ { 1 } { < } \hat { x } _ { 1 }$ implies tha ${ \cdot } J _ { 2 } ( k )$ is increasing at the break point $\gamma x _ { 1 }$ , as shown in the proof of Theorem 1. This further implies that $J _ { 2 } ^ { b } ( k )$ is monotone increasing and $J _ { 2 } ^ { a } ( k )$ <sup>fi</sup>rst increases then decreases. Therefore, the optimal solution is the stationary point of $J _ { 2 } ^ { a } ( k )$ , as characterized in $\operatorname { E q } . \left( 2 \right)$ . Likewise, in Fig. 2(b), the condition $\gamma x _ { 1 } { > } \hat { x } _ { 1 }$ implies that $J _ { 2 } ( k )$ is decreasing at the break point $\gamma x _ { 1 }$ . This further implies that $J _ { 2 } ^ { b } ( k )$ <sup>fi</sup>rst increases and then decreases, and $J _ { 2 } ^ { a } ( k )$ is monotone decreasing. Therefore, the optimal solution is the stationary point of $J _ { 2 } ^ { b } ( k )$ , as characterized in Eq. (1). It is worth noting that if $\gamma x _ { 1 } = \hat { x } _ { 1 }$ , then the stationary points of J<sup>a</sup>(k) and $J _ { 2 } ^ { b } ( k )$ coincide at the break point γx . That is, in such a case $\boldsymbol k ^ { A } = \hat { \boldsymbol x } _ { 1 }$ which can be easily veri<sup>fi</sup>ed from Eqs. (2) and (1).

Fig. $2 ( \mathsf { a } )$ shows that $\mathrm { i f } \gamma x _ { 1 } \leq \hat { x } _ { 1 }$ , then $k ^ { * } = k ^ { A } \geq \gamma x _ { 1 }$ . One may wonder $\operatorname { i f } k ^ { A }$ can ever be greater than $\hat { x } _ { 1 }$ . The last part of Theorem 1 gives a negative answer, which is not surprising because $k ^ { A }$ corresponds to the lower postponable demand case. As a result, the corresponding regular period capacity should be lower.

The managerial aspects of Theorem 1 begin with an interpretation of the threshold value $\hat { x } _ { 1 }$ de<sup>fi</sup>ned in Eq. (1). It is interesting to note that $\hat { x } _ { 1 }$ corresponds to the critical fractile solution to a constrained newsvendor problem where a relatively small capacity (less than the postponable demand $\gamma x _ { 1 } )$ is determined to meet the spot demand $X _ { 2 }$ in the regular period. Clearly, the underage cost is $r - c _ { r }$ . The overage cost is $c _ { r } - c _ { p }$ because there is always suf<sup>fi</sup>cient postponable demand to absorb any slack capacity after satisfying the spot demand, which reduces the amount of demand actually postponed and eliminates the need to purchase capacity at $c _ { p }$ in the postponement period. Effectively, ${ \mathrm { , } } C _ { p }$ here can be viewed as the salvage value of slack capacity in the regular period.

Note that part (b) of Theorem 1 pertains to the case $\gamma x _ { 1 } > k$ (see Fig. $2 ( \mathsf { b } ) ,$ whereby the postponable demand $\gamma x _ { 1 }$ is large enough to absorb any leftover capacity in the regular period. As a result, the corresponding optimal capacity is precisely $\hat { x } _ { 1 }$

On the other hand, part (a) of Theorem 1 pertains to the case $\gamma x _ { 1 } \leq k$ (see Fig. 2(a)) whereby the postponable demand $\gamma x _ { 1 }$ is no more than k and thus may be insuf<sup>fi</sup>cient to absorb leftover capacity in the regular period. In particular, if $\dot { \gamma } x _ { 1 } + x _ { 2 } < k ,$ then there will be no postponable demand to absorb the slack capacity, i.e., the slack capacity has no salvage value under such circumstances. Indeed, this observation leads

to the sole discrepancy $c _ { p } \int _ { 0 } ^ { k - \gamma x _ { 1 } } f _ { 2 } ( x _ { 2 } ) d x _ { 2 }$ between the <sup>fi</sup>rst order derivatives of $J _ { 2 } ^ { a } ( k )$ and $J _ { 2 } ^ { b } ( k )$ , as can be seen from Eqs. $( \mathsf { A } \mathrm { - i } )$ and (A-ii) in the proof of Lemma 1. This is because when $x _ { 2 }$ is small enough $( 0 \leq x _ { 2 } \leq k - \gamma x _ { 1 } )$ , any slack capacity is totally wasted.

In essence,^x de<sup>fi</sup>nes the ideal level of capacity buffer. If the postponable demand γx is too high, i.e., $\gamma x _ { 1 } \geq \hat { x } _ { 1 }$ , then part (b) of the theorem tells us to build a capacity of just ^x to curtail the postponable demand at the ideal level of capacity buffer and avoid excessive use of demand postponement (recall that the capacity buffer is given by $\operatorname* { m i n } ( \gamma x _ { 1 } , k ) )$ On the other hand, if the postponable demand $\gamma x _ { 1 }$ is not suf<sup>fi</sup>cient to create the ideal level of capacity buffer, i.e., $\gamma x _ { 1 } \leq \hat { x } _ { 1 }$ , then a capacity level above $\gamma x _ { 1 }$ (but less than or equal to $\hat { x } _ { 1 } )$ is preferred in order not to further limit the amount of capacity buffer available, as illustrated in Fig. 2(a). Part (a) of the theorem characterizes the optimal capacity level in such a case.

A question of interest is the impact of demand postponement on the <sup>fi</sup>rm's regular period capacity decision. What if $\gamma x _ { 1 }$ is otherwise not postponable? We explore this issue by comparing the cases where $\gamma x _ { 1 }$ is postponable and not postponable. Let $k ^ { 0 }$ be the optimal additional capacity for the aggregate demand $\gamma x _ { 1 } + X _ { 2 }$ when $\gamma x _ { 1 }$ also must be satisfied in the regular period.

Lemma 2. The following holds:

$$
F _ {2} ^ {- 1} \left(\frac {r - c _ {r}}{r}\right) \leq k ^ {*} \leq k ^ {0} = \gamma x _ {1} + F _ {2} ^ {- 1} \left(\frac {r - c _ {r}}{r}\right).
$$

Note that when $x _ { 1 } = 0 , k ^ { 0 }$ reduces to $F _ { 2 } ^ { - 1 } ( ( r \mathrm { ~ - ~ } c _ { r } ) / r )$ , the newsvendor optimal capacity to meet the spot demand $X _ { 2 }$ only. This quantity should be no more than $k ^ { * }$ as there is less demand to meet, which explains the <sup>fi</sup>rst inequality in the above lemma.

The second inequality in Lemma 2 claims that it is optimal for the <sup>fi</sup>rm to build less regular period capacity under demand postponement than the capacity when $\gamma x _ { 1 }$ is not postponable. This implies that the safety stock, referred to as the amount of stock in excess of the mean demand, is reduced as a result of demand postponement. This observation uncovers the driver of demand postponement from a different angle: demand postponement enables the <sup>fi</sup>rm to use less safety stock to hedge against the same risk in the spot demand $X _ { 2 } ,$ thus reducing

Z. Wu, J. Wu / Decision Support Systems xxx (2015) xxx–xxx

![](/api/attachments/B847HUSP/fulltext/images/09519f286d1ce1714bbb37ac4a3bce1ae7278f506ece49ca045db8f81dd0cffb.jpg)  
(a) J2(k) when γx1 < x1

![](/api/attachments/B847HUSP/fulltext/images/8679cf61e078cb2d0671c3f4585fb1d2d04ee7e26e193fe1d8103d47a6182f58.jpg)  
(b) J2(k) when γx1 > x1  
Fig. 2. Sketch of the objective function J (k).

the overall cost. The underlying reason is that the postponable demand γx , playing the role of capacity buffer, is effectively a substitute for safety stock.

The relationship between $c _ { r }$ and $c _ { p }$ merits some discussion. Recall that for customers who take the discount in the advance period, their demand may or may not be deferred to the postponement period, depending on the realization of the spot demand. It is interesting to note that the potential ful<sup>fi</sup>llment time of the postponable demand can be affected by the relationship between $c _ { r }$ and $c _ { p } .$ When $c _ { r } \leq c _ { p } ,$ $\mathrm { i } . \mathsf { e } . _ { \mathsf { v } }$ , when it is more costly to build capacity in the postponement period than in the regular period, $( r - c _ { r } ) / ( r - c _ { p } ) \geq 1$ , and the corresponding ideal level of capacity buffer $\hat { x } _ { 1 }$ becomes in<sup>fi</sup>nity, as can be seen from Eq. (1). In other words, the postponable demand γx would never be suf<sup>fi</sup>cient to create the ideal level of capacity buffer, and the optimal regular period capacity $k ^ { A }$ is no less than the postponable demand γx . As a result, it is possible that all customers who take the discount will have their demand satis<sup>fi</sup>ed in the regular period rather than in the postponement period.

On the other hand, when $c _ { r } > c _ { p } ,$ , we have $0 < ( r - c _ { r } ) / ( r - c _ { p } ) < 1$ Therefore, both $k ^ { A }$ and $\hat { x } _ { 1 }$ are possible to be the optimal capacity decision, depending on the value of the postponable demand $\gamma x _ { 1 }$ . If $\gamma x _ { 1 }$ exceeds the threshold $\hat { x } _ { 1 }$ , then the optimal capacity is just $\hat { x } _ { 1 }$ implying that a portion of the postponable demand will indeed be postponed for certain. The fact that some advance customers will pay (being postponed) for sure for the bene<sup>fi</sup>t (price discount) they enjoy is in sharp contrast with the $c _ { r } \leq c _ { p }$ case whereby it is possible that all advance customers who take the price discount may enjoy the discount for free (without being postponed). From the advance customers' standpoint, they de<sup>fi</sup>nitely prefer the latter case, especially when the size of the advance demand class is large (i.e., when $x _ { 1 }$ tends to be large).

Before concluding this section, we examine the impact of model parameters on the optimal regular period capacity decision. The comparative statics are summarized in the following lemma. Interpretation is omitted as it is straightforward.

Lemma 3. The optimal capacity k\* has the following properties:

$$
\frac {d k ^ {*}}{d c _ {r}} \leq 0; \quad \frac {d k ^ {*}}{d c _ {p}} \geq 0; \quad \frac {d k ^ {*}}{d r} \geq 0; \quad \frac {d k ^ {*}}{d \gamma} \geq 0.
$$

## 5. The optimal price discount

As mentioned earlier, we choose to work on the customer response function γ rather than the price discount q for analytical convenience. At the beginning of the advance period, in anticipation of the optimal capacity decision in the regular period, the <sup>fi</sup>rm optimizes its expected pro<sup>fi</sup>t over γ as follows:

$$
J _ {1} ^ {*} = \max _ {0 \leq \gamma \leq 1} J _ {1} (\gamma , k ^ {*}),
$$

where

$$
\begin{array}{l} J _ {1} (\gamma , k ^ {*}) = E _ {X _ {1}} \left[ J _ {2} (k ^ {*}) \right] \\ = \int_ {0} ^ {\hat {x} _ {1} / \gamma} J _ {2} ^ {a} (k ^ {A}) f _ {1} (x _ {1}) d x _ {1} + \int_ {\hat {x} _ {1} / \gamma} ^ {\infty} J _ {2} ^ {b} (k ^ {B}) f _ {1} (x _ {1}) d x _ {1}. \end{array}\tag{3}
$$

Recall from earlier discussion that if $c _ { r } \leq c _ { p } ,$ scenario (b) of Theorem 1 disappears and $J _ { 2 } ( k ) = J _ { 2 } ^ { a } ( k )$ on the entire support of $x _ { 1 }$ . Therefore, for notational consistency, we de<sup>fi</sup>ne $F _ { 2 } ^ { - 1 } ( t ) \stackrel { - } { = } \infty$ for $t \geq 1$ to accommodate the above situation. Given this de<sup>fi</sup>nition, ${ \mathrm { i f } } c _ { r } \leq c _ { p } ,$ then the second term in Eq. (3) vanishes because $\hat { x } _ { 1 } =$ $F _ { 2 } ^ { - 1 } \left[ ( r { - } c _ { r } ) / ( r { - } c _ { p } ) \right] = \infty$ . The optimal price discount $q ^ { * }$ is given in the following theorem.

Theorem 2. The optimal price discount $q ^ { * }$ is the inverse of $\gamma ^ { * } ,$ , where $\gamma ^ { * } \in ( 0 , 1 )$ is characterized by the following equation:

$$
\begin{array}{l} \left((1 - q) r - r \gamma \frac {\partial q}{\partial \gamma} - r + c _ {r}\right) E (X _ {1}) \\ - c _ {p} \left[ \int_ {0} ^ {\dot {x} _ {1} / \gamma} \left(\int_ {k ^ {A} - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}) x _ {1} f _ {1} (x _ {1}) d x _ {1} + \int_ {\dot {x} _ {1} / \gamma} ^ {\infty} x _ {1} f _ {1} (x _ {1}) d x _ {1} \right] = 0. \right. \end{array}\tag{4}
$$

Basically, Eq. (4) captures the tradeoffs between revenue forgone by the price discount and the bene<sup>fi</sup>t of having the postponable demand as capacity buffer. To see why, let us rewrite the equation as follows:

$$
\begin{array}{l} \left[ (r - c _ {r}) - \left((1 - q) r - r \gamma \frac {\partial q}{\partial \gamma} - c _ {r}\right) \right] E (X _ {1}) \\ = \int_ {0} ^ {\hat {x} _ {1} / \gamma} \left(c _ {r} - c _ {p} \int_ {k ^ {A} - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) x _ {1} f _ {1} (x _ {1}) d x _ {1} + \left(c _ {r} - c _ {p}\right) \int_ {\hat {x} _ {1} / \gamma} ^ {\infty} x _ {1} f _ {1} (x _ {1}) d x _ {1} \\ = \int_ {0} ^ {\hat {x} _ {1} / \gamma} \left[ \left(r - c _ {p}\right) \int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} \right] x _ {1} f _ {1} (x _ {1}) d x _ {1} + \left(c _ {r} - c _ {p}\right) \int_ {\hat {x} _ {1} / \gamma} ^ {\infty} x _ {1} f _ {1} (x _ {1}) d x _ {1}, \end{array}\tag{5}
$$

where the last step follows from Eq. (2).

On the left-hand side of the above equation, $r - c _ { r }$ is the pro<sup>fi</sup>t margin for demand $( 1 - \gamma ) x _ { 1 }$ , whereas $\left( ( 1 - q ) r - r \gamma \frac { \partial q } { \partial \gamma } - c _ { r } \right)$ relates to the

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002

pro<sup>fi</sup>t margin for the postponable demand $\gamma x _ { 1 } .$ . Together, they re<sup>fl</sup>ect the revenue forgone for the advance demand class $X _ { 1 }$ due to price discount. The right-hand side mirrors the pro<sup>fi</sup>t improvement in the spot demand $X _ { 2 }$ rendered by demand postponement, which is more readily understandable by examining the following two cases.

We <sup>fi</sup>rst look at the case where $c _ { r } \leq c _ { p } .$ . As discussed earlier in this section, $\hat { x } _ { 1 } = \infty$ in this case and the right-hand side of Eq. (5) reduces to

$$
\int_ {0} ^ {\infty} \left[ (r - c _ {p}) \int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} \right] x _ {1} f _ {1} (x _ {1}) d x _ {1},
$$

which captures how the spot demand $X _ { 2 }$ can bene<sup>fi</sup>t from demand postponement: as γ increases, the capacity buffer in the regular period also increases. As discussed earlier in Section $^ { 4 , }$ the capacity buffer, if indeed utilized, can reduce the underage cost from $r \mathrm { ~ - ~ } c _ { r }$ to $c _ { p } - c _ { r } , \mathrm { i . e . }$ , the net underage cost reduction is $r - c _ { p } .$ Note that the underage cost reduction by the additional capacity buffer comes into effect only if stockouts do occur. In other words, the additional capacity buffer adds values only if it is indeed utilized, i.e., only if the spot demand realization $x _ { 2 }$ exceeds the capacity k. Therefore, for a given $x _ { 1 } ,$ , the marginal bene<sup>fi</sup>t of the additional capacity buffer is $\left( r - c _ { p } \right) \int _ { k ^ { A } } ^ { \infty } f _ { 2 } ( x _ { 2 } ) d x _ { 2 }$

On a side note, the above discussion suggests that demand postponement is always bene<sup>fi</sup>cial as long as $c _ { p } < r .$ In fact, it is shown in the proof of Theorem 2 that it is always optimal to provide a price discount $( \mathrm { i } . \mathrm { e } . , q ^ { * } > 0 )$ , given our assumptions that capacity costs $c _ { r }$ and $c _ { p }$ are less than r. Once $c _ { p }$ reaches $r ,$ demand postponement will have no value because the <sup>fi</sup>rm cannot make a pro<sup>fi</sup>t in the postponement period and thus would rather not provide any price discount.

We now turn our attention to the case where $c _ { r } > c _ { p } .$ . In this case, if $x _ { 1 } \leq \hat { x } _ { 1 } / \gamma ,$ then the postponable demand $\gamma x _ { 1 }$ is no more than the ideal level of capacity buffe $\hat { x } _ { 1 }$ . Therefore, as γ increases, the increment in the postponable demand will turn into an effective capacity buffer and can be potentially utilized to mitigate stockouts of the spot demand $X _ { 2 } .$ . This explains the <sup>fi</sup>rst integral in Eq. (5). On the other hand, $\mathrm { i f } x _ { 1 } \ge \hat { x } _ { 1 } / \gamma ,$ then $\gamma x _ { 1 }$ already exceed ${ \hat { x } } _ { 1 } ,$ , and the optimal capacity is set at $\hat { x } _ { 1 }$ to curtail any additional capacity buffer. As γ increases, the incremental amount in the postponable demand is useless in mitigating stockouts of the spot demand $X _ { 2 } .$ Instead, it can be used to absorb slack capacity in the event that the spot demand realization $x _ { 2 }$ is low. In other words, the capacity waste reduction brought by the additional postponable demand is more salient in this case. Recall that according to discussions in Section 4, the overage cost is $c _ { r } -$ $c _ { p } ,$ as $c _ { p }$ can be thought of as the salvage value of slack capacity in the regular period. The second term in Eq. (5) re<sup>fl</sup>ects the additional capacity buffer's expected bene<sup>fi</sup>t of capacity waste reduction.

## 6. Additional value of information updating

So far, our model has not assumed any speci<sup>fi</sup>c probability distributions of the two demand classes or any relationship between them, which allows us to focus on demand postponement's role of spot demand stockout mitigation and capacity waste reduction. The <sup>fi</sup>rm may also derive the bene<sup>fi</sup>t of spot demand information updating since the regular period capacity decision is made after the realization of the advance demand. This is possible if the two demand classes are correlated, and thus the realization of the advance demand can be used to update the distribution of the spot demand.

In this section, we assume that the joint distribution of $X _ { 1 }$ and $X _ { 2 }$ is bivariate normal with means μ and $\mu _ { 2 } ,$ standard variations $\sigma _ { 1 }$ and $\sigma _ { 2 }$ and a correlation coef<sup>fi</sup>cient $\rho \in ( - 1 , 1 )$ ). To simplify the analysis, we assume that $X _ { 1 }$ and $X _ { 2 }$ have the same coef<sup>fi</sup>cient of variation $\theta ,$ i.e., $\theta \ : = \ : \sigma _ { 1 } / \mu _ { 1 } \ : = \ : \sigma _ { 2 } / \mu _ { 2 }$ . For a given realization $x _ { 1 }$ of $X _ { 1 } ,$ , the updated spot demand follows a normal distribution with mean $\widetilde { \mu } _ { 2 } ( x _ { 1 } ) =$ $\mu _ { 2 } + \rho ( x _ { 1 } - \mu _ { 1 } ) \sigma _ { 2 } / \sigma _ { 1 }$ and standard deviation $\widetilde { \sigma } _ { 2 } = \sigma _ { 2 } \sqrt { 1 - \rho ^ { 2 } }$ . Let $f _ { 2 } ( x _ { 2 } | x _ { 1 } )$ and $F _ { 2 } ( x _ { 2 } | x _ { 1 } )$ ) denote the PDF and CDF of the updated $X _ { 2 } ,$ , respectively, and let $z = \Phi ^ { - 1 } \left( \frac { r - c _ { r } } { r - c _ { p } } \right)$ , where Φ(⋅) denotes the CDF of the unit normal distribution.

It is useful to note that the solution procedure for the information updating case largely mimics that for the no updating case. The main difference is that now the above conditional density function $f _ { 2 } ( x _ { 2 } | x _ { 1 } )$ is in place of $f _ { 2 } ( x _ { 2 } ) .$ , and everything else carries through.

According to Eq. (1), $\begin{array} { r } { \hat { x } _ { 1 } = F _ { 2 } ^ { - 1 } \Big ( \frac { r - c _ { r } } { r - c _ { p } } | x _ { 1 } \Big ) = \widetilde { \mu } _ { 2 } ( x _ { 1 } ) + z \widetilde { \sigma } _ { 2 } } \end{array}$ . It is straightforward to verify that the condition $\gamma x _ { 1 } \leq \hat { x } _ { 1 }$ in part (a) of Theorem 1 becomes $( \gamma \mu _ { 1 } - \rho \mu _ { 2 } ) x _ { 1 } \le \mu _ { 1 } \mu _ { 2 } - \rho \mu _ { 1 } \mu _ { 2 } + z \theta \mu _ { 1 } \mu _ { 2 } \sqrt { 1 - \rho ^ { 2 } }$ Since $x _ { 1 } \geq 0$ , this condition clearly holds for all values of $x _ { 1 }$ if $\gamma \mu _ { 1 } -$ $\rho \mu _ { 2 } \leq 0 .$

De<sup>fi</sup>ne

$$
\widetilde {\widetilde {x}} _ {1} = \frac {\mu_ {1} \mu_ {2} - \rho \mu_ {1} \mu_ {2} + z \theta \mu_ {1} \mu_ {2} \sqrt {1 - \rho^ {2}}}{(\gamma \mu_ {1} - \rho \mu_ {2}) ^ {+}},
$$

where the + operator means $y ^ { + } = y , \mathrm { i f } y \geq 0 ;$ and 0 otherwise. It is worth noting that the threshold $\widetilde { \widetilde { x } } _ { 1 }$ becomes in<sup>fi</sup>nity if $\gamma \mu _ { 1 } ~ -$ $\rho \mu _ { 2 } \leq 0 ,$ , implying that the condition $\gamma x _ { 1 } \leq \hat { x } _ { 1 }$ can be written as $x _ { 1 } \leq \widetilde { \widetilde { x } } _ { 1 }$ Then the optimal capacity and price discount decisions mimic those in Theorems 1 and 2, respectively, and are presented below without proof.

Theorem 3. The optimal capacity $k ^ { * } i f o f c$ a threshold type. Specifically

(a) $i f x _ { 1 } \le \widetilde { \widetilde { x } } _ { 1 } ,$ , then the optimal capacity $k ^ { * } = \widetilde { k } ^ { A }$ solves the following equation:

$$
- c _ {r} + c _ {p} \int_ {\widetilde {k} ^ {A}} ^ {\widetilde {k} ^ {A}} f _ {2} (x _ {2} | x _ {1}) d x _ {2} + r \int_ {\widetilde {k} ^ {A}} ^ {\infty} f _ {2} (x _ {2} | x _ {1}) d x _ {2} = 0;
$$

(b) $x _ { 1 } \geq \widetilde { \widetilde { x } } _ { 1 }$ , then the optimal capacity is $k ^ { * } = \widetilde { k } ^ { B } = \widetilde { \mu } _ { 2 } ( x _ { 1 } ) + z \widetilde { \sigma } _ { 2 } .$

Theorem 4. The optimal price discount $q ^ { * }$ is the inverse of $\gamma ^ { * }$ , where $\gamma ^ { * } \in ( 0 , 1 )$ is characterized by the following equation:

$$
\begin{array}{l} \left((1 - q) q r - r \gamma \frac {\partial q}{\partial \gamma} - r + c _ {r}\right) E (X _ {1}) \\ - c _ {p} \left[ \int_ {0} ^ {\widetilde {\widetilde {x}} _ {1}} \left(\int_ {\widetilde {k} - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2} | x _ {1}) d x _ {2}\right) x _ {1} f _ {1} (x _ {1}) d x _ {1} + \int_ {\widetilde {x} _ {1}} ^ {\infty} x _ {1} f _ {1} (x _ {1}) d x _ {1} \right] = 0. \end{array}
$$

## 7. Numerical studies

In this section, we conduct numerical studies to illustrate the magnitude of the bene<sup>fi</sup>t of demand postponement and the optimal price discount. In our numerical examples, we adopt the response function $\gamma ( q ) = 1 - ( 1 - q ) ^ { \omega }$ , where $\omega > 0$ . This form of the response function belongs to the class of deterministic exponential sales response function and is commonly used in the marketing literature (Tang et al. [2]). Note that the assumption $\omega > 0$ is made to ensure that $\gamma ( q )$ is increasing, thus guaranteeing a solution of $q \in ( 0 , 1 )$ . Also note that when the price discount $q = 0$ or when there is no discount, the response function $\gamma ( q ) = 0 ,$ , which means that there is no postponable demand, i.e., no opaque products are provided. The two demand classes $X _ { 1 }$ and $X _ { 2 }$ are assumed to follow a bivariate normal distribution with correlation coef<sup>fi</sup>cient ρ.

The same pattern is found across our numerical examples with various combinations of parameters. In the illustrative examples reported below, we set $r = 3 0 , c _ { r } = 1 0 , \omega = 3 , \mu _ { 1 } = \mu _ { 2 } = \mu = 1 0 0 , \sigma _ { 1 } = \sigma _ { 2 } =$ $\sigma = 3 0$ , and $\rho = 0 . \mathsf { A s }$ the unit capacity cost $c _ { p }$ in the postponement

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002

![](/api/attachments/B847HUSP/fulltext/images/ac1e0320ec8c59a1fc65a4c79b8bde08612e0fe0401ef4140afb38188153f08f.jpg)  
Fig. 3. The impact of c on the expected pro<sup>fi</sup>t $( r = 3 0 , c _ { r } = 1 0 , \omega = 3 , \rho = 0 , X _ { i } \sim N [ 1 0 0 , 3 0 ^ { 2 } ] )$

period plays an important role in our model, we vary its values in our examples between 1 and 30 to examine how it affects the optimal decisions and the associated expected pro<sup>fi</sup>t.

We also use numerical examples to explore the effect of demand correlation and uncertainty. To do so, we <sup>fi</sup>x $c _ { p }$ at 10 and vary $\boldsymbol { \rho }$ and σ, respectively.

## 7.1. The value of demand postponement with opaque selling

Compared to the case with no postponement (or no discount, i.e., $q =$ 0), the case with demand postponement yields higher expected pro<sup>fi</sup>t. We refer to the pro<sup>fi</sup>t difference between the two cases as the value of demand postponement. Fig. 3 plots the expected pro<sup>fi</sup>t and percent pro<sup>fi</sup>t increase (over the no discount case) as a function of $c _ { p } .$ As we can see, as $c _ { p }$ decreases, the percent pro<sup>fi</sup>t increases. This is because a lower unit capacity cost in the postponement period makes demand postponement more advantageous. It is worth noting that in the special case where $c _ { p } =$ $c _ { r } = 1 0 , \mathrm { i . e . }$ , when there is no capacity cost difference between the regular period and the postponement period, demand postponement still enables the <sup>fi</sup>rm to increase its pro<sup>fi</sup>t by 2 %, which represents the value of capacity buffer to reduce stockouts as well as capacity waste in the regular period. As $c _ { p }$ falls below $c _ { r }$ there is further incentive for the <sup>fi</sup>rm to use price discount to induce demand postponement, because additional savings in capacity acquisition accrue. Fig. 3 shows that when $c _ { p }$ is very small $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . , c _ { p } = 1 )$ , the percent pro<sup>fi</sup>t increase of the <sup>fi</sup>rm can be as high as 5 %. This is a considerable improvement in the bottom line, especially for industries where the usual pro<sup>fi</sup>t margin is thin. Note that when $c _ { p } = r = 3 0$ , there is no bene<sup>fi</sup>t from demand postponement. This corresponds to the case with $q ^ { * } = 0$

## 7.2. The optimal price discount $q ^ { * }$

With the response function γ(q) speci<sup>fi</sup>ed earlier in this section, we calculate the optimal price discount $q ^ { * }$ that the <sup>fi</sup>rm should offer, and examine how it is affected by the unit capacity cost in the postponement period. Fig. 4 shows that the optimal discount $q ^ { * }$ and customer response $\gamma ^ { * }$ both are decreasing in $c _ { p } .$ This is because for a given <sup>fi</sup>xed $c _ { r }$ as $c _ { p }$ increases, the relative “cost of demand postponement” $( \mathrm { i } . \mathrm { e } . , c _ { p } - c _ { r } )$ increases. As a result, the <sup>fi</sup>rm is less willing to postpone demand, and the price discount becomes smaller. When $c _ { p } = r = 3 0$ , the optimal price discount reaches 0. This is consistent with the discussion in Section 5.

![](/api/attachments/B847HUSP/fulltext/images/8a3d453b04c918884ef10337c704d50bd920338496c6698b76d2b579ddb8abe0.jpg)  
Fig. 4. The impact of $c _ { p }$ on the optimal discount $q ^ { * } ( r = 3 0 , c _ { r } = 1 0 , \omega = 3 , \rho = $ 0,X \~ N[100,30<sup>2</sup>]).

![](/api/attachments/B847HUSP/fulltext/images/ec6befd9e38a1710bf8e985bf38c57dde413b520cdac7721b8d54de4c8be04f6.jpg)  
Fig. 5. The impact of σ on the optimal discount $q ^ { * }$ and expected pro<sup>fi</sup>t $( r = 3 0 , c _ { r } = c _ { p } =$ $1 0 , \omega = 3 , \rho = 0 . 5 , X _ { i } \sim N [ 1 0 0 , \sigma _ { i } ^ { 2 } ] ;$ ).

## 7.3. The impact of demand uncertainty

We now use an example to illustrate the impact of the demand uncertainty. For simplicity, we assume the same mean and standard deviation for $X _ { 1 }$ and $X _ { 2 } ,$ thus their coef<sup>fi</sup>cients of variation are also the same. We vary the standard deviation σ to see its effect. Note that to ensure a negligible chance of negative demand, we only vary σ in the range such that the coef<sup>fi</sup>cient of variation is less than 1/3.

Fig. 5 shows that both the optimal price discount and the percent pro<sup>fi</sup>t increase (over the no postponement case) are increasing in σ, which is not surprising because, again, the main bene<sup>fi</sup>t of demand postponement is that the capacity buffer induced by the price discount can be used to hedge against spot demand uncertainty. The larger the value of σ, the more the <sup>fi</sup>rm can bene<sup>fi</sup>t from demand postponement.

## 7.4. The impact of demand correlation

In this part, we vary $\rho ,$ the correlation coef<sup>fi</sup>cient between the advance demand and spot demand, on the range [−0.9, 0.9] to study its impact on the optimal price discount and expected pro<sup>fi</sup>t. It is interesting to see from Fig. 6 that the expected pro<sup>fi</sup>t is convex in $\rho ,$ while the optimal price discount is concave in $\rho .$ Effectively, what plays a role is the magnitude o ${ \bf \dot { \rho } } _ { \rho } ,$ instead of its sign. A larger |ρ| means that the realization of the advance demand $x _ { 1 }$ becomes more informative. As a result, $X _ { 2 }$ becomes more certain, as the standard deviation of its updated distribution $\widetilde { \sigma } _ { 2 } = \sigma _ { 2 } \sqrt { 1 - \rho ^ { 2 } }$ is decreasing in $| \rho | .$ . Therefore, the <sup>fi</sup>rm can better match the regular period capacity with the spot demand, hence the increased pro<sup>fi</sup>t. Recall that the main idea of demand postponement is to use the capacity buffer induced by price discount to hedge against uncertainties in the spot demand $X _ { 2 } .$ Since uncertainties in X decrease in |ρ|, the bene<sup>fi</sup>ts of price discount also decrease. Therefore, the price discount decreases in |ρ|. Further, note that $\widetilde { \sigma } _ { 2 }$ is concave decreasing in |ρ|, which explains why the expected pro<sup>fi</sup>t increases in |ρ| at an accelerating rate, while the optimal price discount decreases at an accelerating rate.

## 8. Conclusion and future research

In today's business world, information technology advancements allow <sup>fi</sup>rms to take reservations in advance, which enables them to

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002

![](/api/attachments/B847HUSP/fulltext/images/c578d2459169858c58129e00f1b6da1206c93610c09a738744250422bc90ccbd.jpg)  
Fig. 6. The impact of ρ on the optimal discoun $\cdot q ^ { * }$ and expected pro<sup>fi</sup>t $( r = 3 0 , c _ { r } = c _ { p } =$ $1 \bar { 0 , } \omega = 3 , X _ { \mathrm { i } } \tilde { { } _ { \sim } } \tilde { N } [ 1 0 0 , \dot { 3 } 0 ^ { 2 } ] )$ ).

collect demand information and develop innovative and effective selling strategies such as advance selling and opaque selling (Xie and Shugan [11]). Motivated by observations from the travel industry, we develop a <sup>fi</sup>rm's opaque selling strategy in this paper. The <sup>fi</sup>rm faces two classes of random demand—the advance demand class and the spot demand class. Some advance customers are <sup>fl</sup>exible in terms of their order ful<sup>fi</sup>llment timing, and can be enticed to have their demand met in the postponement period. The <sup>fi</sup>rm uses a price discount to induce <sup>fl</sup>exible customers to agree to demand postponement, effectively creating an opaque product. We formulate a two-stage stochastic program and characterize the optimal capacity and price discount the <sup>fi</sup>rm should offer to maximize its expected pro<sup>fi</sup>t.

Our analysis shows that the driver of the demand postponement strategy is that the <sup>fi</sup>rm's option to satisfy early orders at a later time enables it to use less safety stock to hedge against uncertainties in the spot demand. The <sup>fi</sup>rm bene<sup>fi</sup>ts from both stockout cost reduction and capacity waste decrease. Additionally, the <sup>fi</sup>rm may also bene<sup>fi</sup>t from the lower capacity cost brought by the second ordering chance, if the unit capacity cost in the postponement period is lower. Furthermore, when advance demand and spot demand are correlated, the <sup>fi</sup>rm can derive additional bene<sup>fi</sup>t from information updating. Through illustrative numerical examples, we demonstrate that demand postponement may present a good opportunity to noticeably improve the <sup>fi</sup>rm's bottom line.

A limitation of our model is that the advance demand $X _ { 1 }$ is invariant with respect to the price discount, which omits to capture effect of the price discount on customer migration from competing <sup>fi</sup>rms. Therefore, our model works best in environments where the <sup>fi</sup>rm in question is a monopolist (or customers of competing <sup>fi</sup>rms are so loyal that little switchover takes place), and the market potential remains virtually constant. Potential ways to address this limitation, possibly at the expense of tractability, include assuming demand transfer from competitors, or allowing the advance demand class to be stochastically increasing in the price discount. We remark that if the customer switchover effect is included in the model, the bene<sup>fi</sup>t of demand postponement may be sizeably enhanced, as the <sup>fi</sup>rm can not only gain extra revenue from the enlarged customer base, but also enjoy a larger capacity buffer. As such, our model establishes a lower bound for the value of demand postponement. We leave further exploration to future research.

## Acknowledgments

This research was supported in part by the Fundamental Research Funds for the Central Universities and the Research Funds of Renmin University of China (grant No. 10XNJ042).

## Appendix A

Proof of Lemma 1. Taking the <sup>fi</sup>rst and second order derivative of J<sup>a</sup>(k) with respect to k yields

$$
\begin{array}{l} \frac {\partial J _ {2} ^ {a} (k)}{\partial k} = - c _ {r} + c _ {p} \int_ {k - \gamma x _ {1}} ^ {k} f _ {2} (x _ {2}) d x _ {2} + r \int_ {k} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}, \\ \frac {\partial^ {2} J _ {2} ^ {a} (k)}{\partial k ^ {2}} = - c _ {p} f _ {2} (k - \gamma x _ {1}) - \Big (r - c _ {p} \Big) f _ {2} (k) <   0. \end{array}\tag{A - i}
$$

It then follows that $J _ { 2 } ^ { a } ( k )$ is concave in k. Similarly, for $J _ { 2 } ^ { b } ( k )$ , we get

$$
\begin{array}{l} \frac {\partial J _ {2} ^ {b} (k)}{\partial k} = - c _ {r} + c _ {p} \int_ {0} ^ {k} f _ {2} (x _ {2}) d x _ {2} + r \int_ {k} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} \\ \qquad = (r - c _ {r}) - \Big (r - c _ {p} \Big) F _ {2} (k), \\ \frac {\partial^ {2} J _ {2} ^ {b} (k)}{\partial k ^ {2}} = - \Big (r - c _ {p} \Big) f _ {2} (k) <   0. \end{array}\tag{A - ii}
$$

Therefore, $J _ { 2 } ^ { b } ( k )$ is also concave.

It is straightforward to verify that $J _ { 2 } ^ { a } ( \gamma x _ { 1 } ) = J _ { 2 } ^ { b } ( \gamma x _ { 1 } ) , s 0 J _ { 2 } ( k )$ is continuous at $\gamma x _ { 1 } .$ . Further, it can be shown that the left and right derivatives of $J _ { 2 } ( k )$ at $\gamma x _ { 1 }$ are

$$
\left. \frac {\partial J _ {2} ^ {b} (k)}{\partial k} \right| _ {k \rightarrow \gamma x _ {1} -} = \left. \frac {\partial J _ {2} ^ {a} (k)}{\partial k} \right| _ {k \rightarrow \gamma x _ {1} +} = (r - c _ {r}) - (r - c _ {p}) F _ {2} (\gamma x _ {1}),
$$

which implies that $J _ { 2 } ( k )$ is differentiable at $\gamma x _ { 1 } . \sqsupset$

Proof of Theorem 1. Recall that we have the following from Eqs. (A-i) and (A-ii) in the proof of Lemma 1:

$$
\left. \frac {\partial J _ {2} (k)}{\partial k} \right| _ {k = \gamma x _ {1}} = \left(r - c _ {r}\right) - \left(r - c _ {p}\right) F _ {2} (\gamma x _ {1}).
$$

Also recall that on the range [0, $\gamma x _ { 1 } ] , J _ { 2 } ( k ) = J _ { 2 } ^ { b } ( k )$ . If the above derivative is positive, namely, $\begin{array} { r } { \mathrm { i f } \gamma x _ { 1 } { < } F _ { 2 } ^ { - 1 } \left( \frac { r - c _ { r } } { r - c _ { v } } \right) = \hat { x } _ { 1 } , } \end{array}$ , then it means that $J _ { 2 } ^ { b } ( k )$ is concave increasing on $[ 0 , \gamma x _ { 1 } ] .$ . It also implies that $\partial J _ { 2 } ^ { a } ( k ) ,$ /∂k changes from positive to negative on the range $[ \gamma x _ { 1 } , \infty )$ . Therefore, the optimal capacity $k ^ { A }$ can be obtained from the <sup>fi</sup>rst order condition speci<sup>fi</sup>ed in $\operatorname { E q . } \left( 2 \right)$ , which follows directly from Eq. (A-i).

On the other hand, if the above derivative is negative, namely, $\mathrm { i f } \gamma x _ { 1 }$ ${ > } \hat { x } _ { 1 } ,$ , then it means $J _ { 2 } ^ { a } ( k )$ is concave decreasing on $[ \gamma x _ { 1 } , \infty )$ . It also implies that $\partial J _ { 2 } ^ { b } ( k ) / \partial k$ changes from positive to negative on the range [0, γx ]. As a result, the optimal capacity $k ^ { B }$ can be obtained from the <sup>fi</sup>rst order condition speci<sup>fi</sup>ed in Eq. (1), which follows directly from Eq. (A-ii).

To show that $\boldsymbol { k } ^ { A } \le \hat { \boldsymbol { x } } _ { 1 }$ , <sup>fi</sup>rst note that Eq. (1) can be rewritten as

$$
c _ {r} = r - \left(r - c _ {p}\right) \int_ {0} ^ {\hat {x} _ {1}} f _ {2} (x _ {2}) d x _ {2},
$$

which is then substituted into Eq. (A-i) to yield

$$
\begin{array}{l} \left. \frac {\partial f _ {2} ^ {a} (k)}{\partial k} \right| _ {k = \hat {x} _ {1}} = \left(- c _ {r} + c _ {p} \int_ {k - \gamma x _ {1}} ^ {k} f _ {2} (x _ {2}) d x _ {2} + r \int_ {k} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) \bigg | _ {k = \hat {x} _ {1}} \\ = -   r + \Big (r - c _ {p} \Big) \int_ {0} ^ {\hat {x} _ {1}} f _ {2} (x _ {2}) d x _ {2} + c _ {p} \int_ {\hat {x} _ {1} - \gamma x _ {1}} ^ {\hat {x} _ {1}} f _ {2} (x _ {2}) d x _ {2} \\ \quad + r \int_ {\hat {x} _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} = - c _ {p} \int_ {0} ^ {\hat {x} _ {1} - \gamma x _ {1}} f _ {2} (x _ {2}) d x _ {2} \leq 0. \end{array}
$$

It then follows from the concavity of J<sup>a</sup>(k) that $\hat { x } _ { 1 }$ lies on the right of the stationary point of J<sup>a</sup>(k), i.e., $\boldsymbol { k } ^ { A } \le \hat { \boldsymbol { x } } _ { 1 }$ . In addition, it is clear that the equality holds if and only $\mathrm { i f } \hat { x } _ { 1 } = \gamma x _ { 1 }$ .

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002

Proof of Lemma 2. Note that $k ^ { * }$ is either $k ^ { A }$ or $\hat { x } _ { 1 }$ . It is clear that $\begin{array} { r } { \boldsymbol { F } _ { 2 } ^ { - 1 } \left( \frac { r - c _ { r } } { r } \right) \le \hat { \boldsymbol { x } } _ { 1 } \le \gamma \boldsymbol { x } _ { 1 } } \end{array}$ and thus $\hat { x } _ { 1 }$ evidently satis<sup>fi</sup>es the inequalities in the lemma. Therefore, it suf<sup>fi</sup>ces to show that $k ^ { A }$ also satis<sup>fi</sup>es the same.

If $\gamma x _ { 1 }$ is not postponable, the problem boils down to the classic newsvendor problem: in the regular period, the capacity k is used to meet the aggregate demand $\gamma x _ { 1 } + X _ { 2 }$ with a underage cost $r -$ $c _ { r }$ and overage cost $c _ { r }$ . It then follows from the newsvendor critical ratio solution that

$$
k ^ {0} = \gamma x _ {1} + F _ {2} ^ {- 1} \left(\frac {r - c _ {r}}{r}\right),
$$

which can be rewritten as

$$
c _ {r} = r \int_ {k ^ {0} - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}.
$$

Substituting the above expression for $c _ { r }$ into the <sup>fi</sup>rst order derivative of J<sub>2</sub><sup>a</sup>(k) yields

$$
\begin{array}{l} \frac {\partial J _ {2} ^ {a} (k)}{\partial k} \bigg | _ {k = k ^ {0}} = \left(- c _ {r} + c _ {p} \int_ {k - \gamma x _ {1}} ^ {k} f _ {2} (x _ {2}) d x _ {2} + r \int_ {k} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) \bigg | _ {k = k ^ {0}} \\ = - r \int_ {k ^ {0} - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} + c _ {p} \int_ {k ^ {0} - \gamma x _ {1}} ^ {k ^ {0}} f _ {2} (x _ {2}) d x _ {2} \\ \qquad + r \int_ {k ^ {0}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} = - \Big (r - c _ {p} \Big) \int_ {k ^ {0} - \gamma x _ {1}} ^ {k ^ {0}} f _ {2} (x _ {2}) d x _ {2} \leq 0. \end{array}
$$

It then follows from the concavity of $J _ { 2 } ^ { a } ( k )$ that $k ^ { 0 }$ lies on the right of the stationary point of J<sup>a</sup>(k), i.e., $k ^ { A } \leq k ^ { 0 } .$

Similarly, note that $r \int _ { { F _ { 2 } ^ { - 1 } } \left( { \frac { r - c _ { r } } { r } } \right) } ^ { \infty } f _ { 2 } ( x _ { 2 } ) d x _ { 2 } = c _ { 1 }$ <sub>r</sub>. From Eq. (A-i), we get

$$
\begin{array}{c} \left. \frac {\partial J _ {2} ^ {a} (k)}{\partial k} \right| _ {k = F _ {2} ^ {- 1} \left(\frac {(r - c _ {r})}{r}\right)} = \left(- c _ {r} + c _ {p} \int_ {k - \gamma x _ {1}} ^ {k} f _ {2} (x _ {2}) d x _ {2} + r \int_ {k} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) \Bigg | _ {k = F _ {2} ^ {- 1} \left(\frac {(r - c _ {r})}{r}\right)} \\ = c _ {p} \int_ {F _ {2} ^ {- 1} \left(\frac {(r - c _ {r})}{r}\right) - \gamma x _ {1}} ^ {F _ {2} ^ {- 1} \left(\frac {(r - c _ {r})}{r}\right)} f _ {2} (x _ {2}) d x _ {2} \geq 0, \end{array}
$$

which implies that $F _ { 2 } ^ { - 1 } \left( \frac { r - c _ { r } } { r } \right) \leq k ^ { A }$ . □

Proof of Lemma 3. Recall that $k ^ { * }$ is either $k ^ { A }$ or $\hat { x } _ { 1 }$ . It is evident from $\operatorname { E q . } \left( 1 \right)$ tha $\cdot \hat { x } _ { 1 }$ is decreasing (or non-increasing, to be more precise) in $c _ { r } ,$ increasing in $c _ { p }$ and r, and independent of $\gamma .$ It then suf<sup>fi</sup>ces to show that $k ^ { A }$ also satis<sup>fi</sup>es the inequalities in the lemma.

Differentiation of Eq. (2) with respect to c yields

$$
\left[ \left(r - c _ {p}\right) f _ {2} \left(k ^ {A}\right) + c _ {p} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right) \right] \frac {\partial k ^ {A}}{\partial c _ {r}} = - 1,
$$

which implies that $k ^ { A }$ is decreasing in $c _ { r }$ . This completes the <sup>fi</sup>rst part of the lemma.

Following similar steps, we can obtain the following:

$$
\begin{array}{l} \left[ \left(r - c _ {p}\right) f _ {2} \left(k ^ {A}\right) + c _ {p} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right) \right] \frac {\partial k ^ {A}}{\partial c} = \int_ {k ^ {A} - \gamma x _ {1}} ^ {k ^ {A}} f _ {2} (x _ {2}) d x _ {2}, \\ \left[ \left(r - c _ {p}\right) f _ {2} \left(k ^ {A}\right) + c _ {p} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right) \right] \frac {\partial k ^ {A}}{\partial r} = \int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}, \\ \left[ \left(r - c _ {p}\right) f _ {2} \left(k ^ {A}\right) + c _ {p} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right) \right] \frac {\partial k ^ {A}}{\partial \gamma} = c _ {p} x _ {1} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right), \end{array}
$$

which completes the rest of the lemma. □

Proof of Theorem 2. According to the envelope theorem, we can obtain the <sup>fi</sup>rst order derivative of $J _ { 1 } ( \gamma , k ^ { * } )$ with respect to γ by taking the partial derivative as follows:

$$
\begin{array}{l} \frac {\partial J _ {1} (\gamma , k ^ {*})}{\partial \gamma} = \frac {\partial J _ {1} (\gamma , k)}{\partial \gamma} \Big | _ {k = k ^ {*}} \\ = \left(\int_ {0} ^ {\hat {x} _ {1} / \gamma} \frac {\partial J _ {2} ^ {a} (k)}{\partial \gamma} f _ {1} (x _ {1}) d x _ {1} + \int_ {\hat {x} _ {1} / \gamma} ^ {\infty} \frac {\partial J _ {2} ^ {b} (k)}{\partial \gamma} f _ {1} (x _ {1}) d x _ {1} \right. \\ \left. - \frac {\hat {x} _ {1} f _ {1} (x _ {1})}{\gamma^ {2}} \left(J _ {2} ^ {a} (k) - J _ {2} ^ {b} (k)\right) \Big | _ {x _ {1} = \hat {x} _ {1} / \gamma}\right) \Bigg | _ {k = k ^ {*}}. \end{array}
$$

However, recall that from Eqs. (A-i) and (A-ii) in the proof of Lemma 1, the <sup>fi</sup>rst order derivative of $J _ { 2 } ( k )$ evaluated at the break point $k = \gamma x _ { 1 }$ is as follows:

$$
\left. \frac {\partial J _ {2} (k)}{\partial k} \right| _ {k = \gamma x _ {1}} = \left(r - c _ {r}\right) - \left(r - c _ {p}\right) F _ {2} (\gamma x _ {1}).
$$

Observe that $x _ { 1 } = \hat { x } _ { 1 } / \gamma$ is precisely the point that makes the above derivative equal to 0. In other words, $\begin{array} { r } { \mathrm { a t } x _ { 1 } = \hat { x } _ { 1 } / \gamma , } \end{array}$ , the stationary points of ${ \bf \bar { \it J } } _ { 2 } ^ { a } ( k )$ and ${ \bar { J } } _ { 2 } ^ { b } ( k )$ coincide at the break point $\gamma x _ { 1 } = \hat { x } _ { 1 }$ . Therefore, at this point, $\boldsymbol { k } ^ { A } = \boldsymbol { \bar { k } } ^ { B } = \boldsymbol { \hat { x } } _ { 1 }$ , and thus the last term of $\partial J _ { 1 } ( \gamma , k ^ { * } ) / \partial \gamma$ becomes 0. Further, after some algebraic simpli<sup>fi</sup>cation, we get

$$
\begin{array}{l} \frac {\partial J _ {2} ^ {a} (k)}{\partial \gamma} = \bigg ((1 - q) r - r \gamma \frac {\partial q}{\partial \gamma} - r + c _ {r} \bigg) x _ {1} - c _ {p} x _ {1} \int_ {k - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}, \\ \frac {\partial J _ {2} ^ {b} (k)}{\partial \gamma} = \bigg ((1 - q) r - r \gamma \frac {\partial q}{\partial \gamma} - r + c _ {r} \bigg) x _ {1} - c _ {p} x _ {1}, \end{array}
$$

which leads to the following:

$$
\begin{array}{l} \frac {\partial J _ {1} (\gamma , k ^ {*})}{\partial \gamma} = \bigg ((1 - q) r - r \gamma \frac {\partial q}{\partial \gamma} - r + c _ {r} \bigg) E (X _ {1}) \\ \qquad - c _ {p} \left[ \int_ {0} ^ {\hat {x} _ {1} / \gamma} \left(\int_ {k ^ {A} - \gamma x _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}) x _ {1} f _ {1} (x _ {1}) d x _ {1} \right. \right. \\ \qquad \left. + \int_ {\hat {x} _ {1} / \gamma} ^ {\infty} x _ {1} f _ {1} (x _ {1}) d x _ {1} \right]. \end{array}
$$

Next, note that $\gamma = 0$ corresponds to the case of no discount, i.e., $q =$ 0. Therefore, we get

$$
\begin{array}{c} \left. \frac {\partial J _ {1} (\gamma , k ^ {*})}{\partial \gamma} \right| _ {\gamma = 0} = c _ {r} E (X _ {1}) - c _ {p} \int_ {0} ^ {\infty} \left(\int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) x _ {1} f _ {1} (x _ {1}) d x _ {1} \\ = \int_ {0} ^ {\infty} \left(c _ {r} - c _ {p} \int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) x _ {1} f _ {1} (x _ {1}) d x _ {1} > 0, \end{array}
$$

where the inequality follows from Eq. (2), because this equation can be written as

$$
c _ {r} - r \int_ {k ^ {A}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2} = c _ {p} \int_ {k ^ {A} - \gamma x _ {1}} ^ {k ^ {A}} f _ {2} (x _ {2}) d x _ {2} > 0.
$$

Since $r > c _ { p } ,$ we have $c _ { r } - c _ { p } \int _ { k ^ { A } } ^ { \infty } f _ { 2 } ( x _ { 2 } ) d x _ { 2 } { > } c _ { r } - r \int _ { k ^ { A } } ^ { \infty } f _ { 2 } ( x _ { 2 } ) d x _ { 2 } { > } 0 .$

Moreover, $\gamma = 1$ corresponds to the case $q \stackrel { } { = } 1$ . Therefore when $\gamma = 1$ , the coef<sup>fi</sup>cient of $E ( X _ { 1 } )$ in the expression o $\mathrm { f } \partial J _ { 1 } ( \gamma , k ^ { * } ) / \partial \gamma$ becomes negative, which further means that $\partial J _ { 1 } ( \gamma , k ^ { * } ) / \partial \gamma | _ { \gamma = 1 } < 0 .$ . In sum, the above results show that the objective function is increasing at 0 but decreasing at 1. This implies that there exists at least one local maximum on the range (0, 1), and it is determined by the <sup>fi</sup>rst order condition as characterized in $\operatorname { E q . }$ (4). If multiple local maxima exist, then a line search on (0, 1) is suf<sup>fi</sup>cient to <sup>fi</sup>nd the global optimal solution.

After the optimal $\gamma ^ { * }$ is found from Eq. (4), the optimal price discount $q ^ { * }$ can be obtained from the inverse function of γ due to the one-to-one mapping between q and $\gamma .$

In the special case where γ is convex in q, i.e. $\partial ^ { 2 } \gamma / \partial q ^ { 2 } \ge 0$ , we can derive the second order derivative as follows:

$$
\begin{array}{l} \frac {\partial^ {2} J _ {1} (\gamma , k ^ {*})}{\partial \gamma^ {2}} = - r \left(2 \frac {\partial q}{\partial \gamma} + \gamma \frac {\partial^ {2} q}{\partial \gamma^ {2}}\right) E (X _ {1}) \\ \qquad - c _ {p} \left[ \int_ {0} ^ {\hat {x} _ {1} / \gamma} x _ {1} ^ {2} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right) f _ {1} (x _ {1}) d x _ {1} \right. \\ \qquad + \frac {\hat {x} _ {1}}{\gamma^ {2}} \left(1 - \int_ {k ^ {A} - \hat {x} _ {1}} ^ {\infty} f _ {2} (x _ {2}) d x _ {2}\right) \frac {\hat {x} _ {1}}{\gamma} f _ {1} \left(\frac {\hat {x} _ {1}}{\gamma}\right) ] \\ = - r \left(2 \frac {\partial q}{\partial \gamma} + \gamma \frac {\partial^ {2} q}{\partial \gamma^ {2}}\right) E (X _ {1}) - c _ {p} \int_ {0} ^ {\hat {x} _ {1} / \gamma} x _ {1} ^ {2} f _ {2} \left(k ^ {A} - \gamma x _ {1}\right) f _ {1} (x _ {1}) d x _ {1} <   0, \end{array}
$$

where the second equality above is due to the fact that $\boldsymbol { \cdot } \boldsymbol { k } ^ { A } = \hat { \boldsymbol { x } } _ { 1 }$ when the break point $\gamma x _ { 1 } = \hat { x } _ { 1 }$ , as argued before. The inequality follows from our assumption that γ is strictly increasing in $q .$ In such a case, the concavity 一 $\mathrm { o f } J _ { 1 } ( \gamma , k ^ { * } )$ in γ is established and the solution characterized in Eq. (4) is guaranteed to be unique. Note that the convexity of γ is just a suf<sup>fi</sup>cient condition for the convenience of exposition, but not necessary. In fact, even if γ is concave, the concavity of the objective function still holds as long as the curvature of γ is not too large, as can be seen from the above derivation.

It is worth noting that our model considers the more general case and does not make any assumption about the second order derivative of γ, because without any information about the second order derivative of γ, Eq. (4) is already enough to characterize the optimal γ. □

## References

[1] C.S. Tang, Perspectives in supply chain risk management, International Journal of Production Economics 103 (2006) 451–488.

[2] C.S. Tang, K. Rajaram, A. Alptekinoglu, J. Ou, The bene<sup>fi</sup>ts of advance booking discount programs: model and analysis, Management Science 50 (2004) 465–478.

[3] K. Jerath, S. Netessine, S.K. Veeraraghavan, Revenue management with strategic customers: last-minute selling and opaque selling, Management Science 56 (2010) 430–448.

[4] Y. Jiang, Price discrimination with opaque products, Journal of Revenue and Pricing Management 6 (2007) 118–134.

[5] J. Weisenthal, It's ‘golden week’ in China, and the traf<sup>fi</sup>c jams are like nothing you've ever seen, Business Insider (2012) (09–30), http://www.businessinsider.com/golden-week-huge-traf<sup>fi</sup>c-james-in-china-2012-9.

[6] WantChinaTimes.com, China's ‘golden week’ travelers face 100% mark-up on prices, http://www.wantchinatimes.com/news-subclass-cnt.aspx?id= 20120928000077&cid=1502 2012.

[7] H. Lei, Big loss from stock-piling of Sanya hotel rooms during the spring festival, http://<sup>fi</sup>nance.sina.com.cn/china/dfjj/20100220/11097426832.shtml 2010.

[8] A.V. Iyer, V. Deshpand, Z. Wu, A postponement model for demand management, Management Science 49 (2003) 983–1002.

[9] K.Z. Weng, M. Parlar, Integrating early sales with production decisions: analysis and insights, IIE Transactions 31 (1999) 1051–1060.

[10] K. McCardle, K. Rajaram, C.S. Tang, Advance booking discount program under retail competition, Management Science 50 (2004) 701–708.

[11] J. Xie, S. Shugan, Electronic tickets, smart cards, and online prepayments: when and how to advance sell, Marketing Science 20 (2001) 219–243.

[12] Z. Shen, X. Su, Customer behavior modeling in revenue management and auctions: a review and new research opportunities, Production and Operations Management 16 (2007) 713–728.

[13] X. Su, F. Zhang, Strategic customer behavior, commitment, and supply chain performance, Management Science 54 (2008) 1759–1773.

[14] X. Su, Inter-temporal pricing with strategic customer behavior, Management Science 53 (2007) 726–741.

[15] G. Cachon, R. Swinney, Purchasing, pricing, and quick response in the presence of strategic consumers, Management Science 55 (2009) 497–511.

[16] A.J. Mersereau, D. Zhang, Markdown pricing with unknown fraction of strategic customers, Manufacturing & Service Operations Management 14 (2012) 355–370.

[17] Y. Aviv, A. Pazgal, Optimal pricing of seasonal products in the presence of forwardlooking consumers, Manufacturing & Service Operations Management 10 (2008) 339–359.

[18] S. Fay, J. Xie, Probabilistic goods: a creative way of selling products and services, Marketing Science 27 (2008) 674–690.

[19] N. Granados, A. Gupta, R.J. Kauffman, Designing online selling mechanisms: transparency levels and prices, Decision Support Systems 45 (2008) 729–745.

[20] J. Wu, L. Li, L.D. Xu, A randomized pricing decision support system in electronic commerce, Decision Support Systems 58 (2014) 43–52.

[21] D. Shapiro, X. Shi, Market segmentation: the role of opaque travel agencies, Journal of Economics and Management Strategy 17 (2008) 803–837.

[22] S. Fay, Selling an opaque product through an intermediary: the case of disguising ones product, Journal of Retailing 84 (2008) 59–75.

[23] O. Marom, A. Seidmann, Using last-minute sales for vertical differentiation on the internet, Decision Support Systems 51 (2011) 894–903.

[24] Z. Zhang, K. Joseph, R. Subramaniam, Probabilistic selling in quality-differentiated markets, Management Science (2014), http://dx.doi.org/10.1287/mnsc2014.1974.

Zhengping Wu is an Associate Professor of Supply Chain Management at Whitman School of Management, Syracuse University. Prior to his current position, he was on the faculty of Lee Kong Chian School of Business of Singapore Management University (SMU). Dr. Wu received his PhD degree in operations management from Krannert School of Management, Purdue University. His research interests include supply chain coordination and contracting, operations and marketing interfaces, pricing and inventory management. His research work has been published in Management Science, Manufacturing & Service Operations Management, Production and Operations Management, Operations Research Letters, European Journal of Operational Research, etc. Dr. Wu has received Dean's Teaching Honor recognition in every semester he taught at SMU. He was also nominated for the 2013 SMU Excellent Teacher award.

Jianghua Wu is an Associate Professor of Operations Management at School of Business, Renmin University of China. He obtained his PhD in Operations Management from Purdue University. His main research interests include Supply Chain Management, Inventory Control, Revenue Management and Marketing/Operations Management Interfaces. His work has been published in Computers & Operations research, Decision Support Systems, International Journal of Production Research, OMEGA, etc. His research has been supported by the National Natural Science Foundation of China and research grants from the Ministry of Education.

Please cite this article as: Z. Wu, J. Wu, Price discount and capacity planning under demand postponement with opaque selling, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.02.002
