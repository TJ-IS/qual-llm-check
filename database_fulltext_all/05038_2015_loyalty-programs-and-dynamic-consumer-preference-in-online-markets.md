---
otero_id: 5038
otero_key: "B4FXBQZV"
title: "Loyalty programs and dynamic consumer preference in online markets"
authors: "Sanghee Lim; Byungtae Lee"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.05.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Loyalty programs and dynamic consumer preference in online markets

Sanghee Lim <sup>a</sup>, Byungtae Lee <sup>b</sup>

<sup>a</sup> The Johns Hopkins Carey Business School, 100 International Drive, Baltimore, MD, USA

<sup>b</sup> College of Business, KAIST, 85 Hoegiro, Dongdaemun-gu, Seoul, South Korea

## a r t i c l e i n f o

Available online xxxx

Keywords: Loyalty programs Reward programs Online markets Electronic commerce

## a b s t r a c t

With the rise of online retail markets, many online retailers are replicating the promotion strategies that offline retailers have used without a clear understanding of whether these strategies will deliver similar results in online markets. In particular, a loyalty program, which provides rewards that can be used for future purchase, is a widely adopted promotion strategy by both offline and online retailers with the intention of increasing customer retention and resultant profits. However, the profit contribution of loyalty programs in offline markets is highly controversial. Our question is whether the result will be similar in online markets. Our game-theoretic model shows that the likelihood of success for loyalty programs is higher in online than in offline markets. We note that consumers' preference for retail stores is more dynamic, and the cost of revisiting a store to redeem loyalty rewards is relatively lower in online markets, because consumers in online markets do not incur physical transportation costs. These characteristics provide the condition where loyalty programs effectively facilitate customer retention, while having fewer risks of rewarding the customers who would have made a purchase regardless of any offered rewards. Our model also suggests that, due to the more dynamic consumer preference in online markets, transaction data collected through loyalty programs provides stronger profit incentives for retailers. Our study helps retailers understand the differences between offline and online markets as well as the impact of the differences on the effectiveness of their loyalty programs.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

With the rise of online retail markets, many online retailers are replicating promotion strategies traditionally used by offline retailers. A loyalty program is one such promotion strategy, used by many retailers, both off- and online. A loyalty program is a marketing promotion vehicle that provides customers with incentives to make repeat purchases. For example, consider the well-known frequent flier programs offered by many airlines, in which airlines offer a free trip or a free upgrade according to a customer's accumulated flight mileage. Similarly, a number of retailers have programs (e.g., Bloomingdale's Loyallist Program, Nordstrom's Fashion Rewards, Starbucks' My Starbucks Rewards) that offer rewards to frequent buyers such as points redeemable as discounts for future purchases.<sup>1</sup> The purported objective of a loyalty program is to retain existing customers and, ideally, increase profits [12]. Such a program tries to change the customer's choice process from operating in a spot market to operating in a multi-period, contractual relationship market. In addition to the potential increase in customer retention, many retailers are trying to capitalize on the transaction data of individual customers collected through a loyalty program [24]. With the high rise of interest in data analytics and advances in data-mining technologies, retailers expect increasing potential value in loyalty programs for their customer relationship management (CRM). Target is one retailer that has successfully combined the data from its loyalty program with its data-mining capabilities [22]. The data collected through its loyalty program, REDCard, enable Target to provide customized offers to its highest-value consumers by analyzing their transaction histories at an individual customer level.

The profit contribution of loyalty programs in offline retail markets, however, is still controversial [12,19,22,23,24]. There have been questions regarding the actual value of loyalty programs, and skeptics raise concerns about the possibility of detrimental effects of loyalty programs on the profitability of retailers [22]. A recent McKinsey research report found that profit margins of companies with high spending on loyalty programs are about 10% lower than those of their competitors [22]. Moreover, several empirical studies [11,18,20] suggest that the overall effectiveness of loyalty programs diminishes as markets become saturated. These findings further heighten skepticism regarding the future of loyalty programs.

Despite questionable returns from loyalty programs in offline markets, several online retailers have adopted and replicated these strategies of offline retailers. For example, Overstock.com offers Club O, which provides rewards on the basis of previous purchases that can be used for future purchases. Drugstore.com also offers Drugstore.com Dollars™, which allow customers to earn 5% credit toward future purchases.

Although there is high interest in the impact of loyalty programs on retailers' profits, our understanding of what conditions are necessary for a loyalty program to contribute to increasing retailers' profits is still unclear. In particular, Fox et al. [13] call for more research that compares the effectiveness of marketing promotions across channels, including online and offline channels. However, very little research has actually addressed these issues. A study by Zhang and Wedel [30] is one exception in that it provides empirical evidence of higher effectiveness of loyalty programs in online than in offline markets. This study does demand a more thorough theoretical investigation for the underlying mechanism that explains the differences between loyalty programs in online and offline markets.

Our paper aims to explain under what conditions a loyalty program can be successful, and whether such conditions are relevant to explain the difference between offline and online markets. Based on the literature of dynamic consumer preference and horizontal differentiation, we propose a game-theoretic model that examines the impact of three factors on the profit implications of loyalty programs: (1) the dynamics of consumer preference, (2) the sensitivity of consumers to the differentiation between stores, and (3) the value of transaction data collected through loyalty programs. For online markets, a consumer's preference for a particular retail store is more dynamic and changes relatively easily over time compared with offline markets; in offline markets, consumers are bound to a geographical location, which serves as an exogenous switching cost. Also, the sensitivity of consumers to the differentiation between stores is relatively lower in online markets, because the cost of visiting the less preferred store is relatively lower due to the absence of physical transportation costs. These characteristics provide a condition where loyalty programs effectively persuade consumers to revisit the stores to redeem their loyalty rewards, while having fewer risks of rewarding customers who would have purchased regardless of the offered rewards. Our model also suggests that, when consumer preference is stable (i.e., consumers rarely change their preference over time), the benefits from analyzing transaction data gathered through loyalty programs are distributed to the consumers and have no impact on the retailers' profits. On the other hand, with dynamic consumer preference, the benefit of transaction data provides stronger profit incentives for retailers to adopt loyalty programs. Furthermore, we suggest that the existence of online loyalty programs may explain a low level of shopbot usage [28]. Knowing that the potential rewards are not displayed on shopbot results, informed consumers may select a retailer that charges a higher regular price or may not use shopbots at all.

Our results provide many important theoretical and practical implications. Theoretically, this is the first study that explicitly examines the differences of the efficacy of loyalty programs between online and offline markets, suggesting a high potential of loyalty programs in online markets. Our study contributes to the literature by identifying three key factors (the dynamics and sensitivity of consumer preference and the value of the transaction data) that determine the profitability of loyalty programs. The first two factors characterize the differences between online and offline markets, and these factors explain the different impact of loyalty programs between online and offline markets. In addition, our study is the first attempt to consider the value of transaction data gathered through loyalty programs in the analysis of profit implications related to loyalty programs. This study also provides several practical implications, suggesting that retailers should rationalize implementing loyalty programs on the basis of the dynamics of their target consumers' preference, their sensitivity to the differentiation of stores, and the potential value of transaction data gathered from loyalty programs. Our results also suggest that even if retailers have not gained substantial financial benefits from implementing loyalty programs in the offline channel, they should still consider implementing them in the online channel because the result can be signi cantly different in a positive way. In addition, our study emphasizes the importance of complementary data-mining capabilities and technologies in order to take full advantage of the benefits from loyalty programs.

The paper is organized as follows. Literature relevant to loyalty programs is reviewed in the next section. In Section 3, the basic settings of our model are explained. In Section 4, we examine the competition between two stores in the market with low dynamics, which reflects characteristics of offline markets. We propose our main model in Section 5, where the competition in the market with dynamic consumer preference is examined and discussed. We analyze the profit gains obtained by implementing loyalty programs as a function of the sensitivity of consumers to differentiation between stores and the value of transaction data from loyalty programs. In Section 6, we discuss the theoretical and practical implications and limitations of our model and suggest directions for future research.

## 2. Previous literature

Reflecting the popularity in practice, loyalty programs have been examined extensively under various concepts and terminologies in marketing and microeconomics research, such as endogenous<sup>2</sup> switching costs, frequent-shopper (flier) programs, reward programs, and rearloaded promotions. We recommend Dorotic et al. [11] for a thorough review of previous research on loyalty programs. In this section, we focus on the research that examines economic drivers and financial consequences of implementing loyalty programs. There are mainly two perspectives in this stream of research, which views a loyalty program as: (1) a means to reduce future uncertainty, and (2) a means to create switching costs under dynamic consumer preference.

Earlier studies [9,17] that examine the value of loyalty programs focus on the fact that loyalty programs reduce uncertainty for customers regarding future prices. When consumers purchase an initial unit, they are uncertain of the value of a repeat purchase from the same supplier at a later date. Klemperer [17] and Crémer [9] consider a loyalty program as the pre-commitment to a low future price by the seller and model that the customer resolves uncertainty by joining a loyalty program even before the decision to repurchase is made. Specifically, Crémer [9] shows using a two-period model that, when consumers are risk-neutral, the increase in the initial price by a seller in the first period does not diminish the expected utility of consumers, if the seller guarantees a lower future price in the second period. In this case, the seller's sales level in the first period is the same, but there is an increased proportion of repurchases due to the lower second-period price, demonstrating that the loyalty program would have positive impact on a seller's revenue. These earlier studies provide valuable insight on the approach to examining loyalty programs. However, they examine the case when a seller has a monopolistic power, so the implications from these studies provide little insight for retailers facing fierce competition.

To explain the viability of loyalty programs in competitive environments, Bulkley [6] considers the case where the price dispersion exists as equilibrium, and consumers compare a certain number of firms to find the most favorable price in the market. In his model, the uncertainty of future prices again serves as a key factor driving the value of loyalty programs. The model shows that if consumers are risk-neutral, there is an incentive for a firm to offer loyalty programs, because firms can set a higher first-period price.

Another approach to examining loyalty programs is to consider them as explicit switching costs when consumer preference changes dynamically over time. Caminal and Matutes [7] extend the notion that a loyalty program is an endogenous switching cost. They suggest a game-theoretic model, which shows that, if the preference of a

S. Lim, B. Lee / Decision Support Systems xxx (2015) xxx–xxx

![](/api/attachments/B4FXBQZV/fulltext/images/edaf943dcae9e8b737422dcb72df0ddd4a966c7dfdf8211587e2670c9d4507ed.jpg)  
Fig. 1. Basic setting of duopoly competition of horizontal differentiation.

consumer varies over time randomly and independently, and if sellers can pre-commit to a second-period price, the unique perfect equilibrium is the case where the sellers' pre-committed prices are strictly lower than those charged to newcomers. Zhang and et al. [29] also show, using long-run choice probabilities of the Markov model, that a loyalty program is a profitable strategy in a variety-seeking market, because loyalty programs keep customers from switching to other brands by offering rewards. Shin and Sudhir [24] show that firms should offer loyalty programs when consumer preference is stochastic and changes depending on the purchase occasion.

Although these prior studies provide several important insights for understanding why firms implement loyalty programs and how the programs are profitable to a firm, few studies recognize the difference between online and offline markets and investigate the potential differences in the effectiveness of loyalty programs between two channels. There have been calls for more research to better understand the difference between online and offline markets [13]. Zhang and Wedel [30] took the first step to investigate the potential difference between the two and compared the effects of loyalty promotions operated by brands between online and offline channels. Their empirical result shows that loyalty promotions are more profitable in online channels than in offline ones, implying the possibility of a similar difference for loyalty programs operated by retailers. To the best of our knowledge, no one has investigated the relative efficacy of online loyalty programs for retailers. Furthermore, no study has explicitly investigated the value of transaction data collected through loyalty programs. Our study provides unique insight regarding these points using a game-theoretic model, developed in the next section.

## 3. The model

## 3.1. Assumptions

The general setting we consider is a structure for a standard horizontal differentiation duopoly setting in which consumers demand at most one unit of goods from one of two stores in the market (Fig. 1) [7,14,19]. We want to examine profitability when these stores have the option to implement a loyalty program. Table 1 summarizes the assumptions and notations of the models.

## 3.1.1. Stores

Consider a market where two stores, store A and store B, carry the same assortment<sup>3</sup> of items over two specific periods of time. Each store is located at the end of a line of unit length [7,14]. Both stores are readily available to all consumers, so the consumer has the option of purchasing an item at any one of these stores. For the sake of expositional simplicity, we make the following assumptions: (1) the prices of the products sold in each store are the same, denoted as $p _ { A }$ and $p _ { B } ,$ respectively, and (2) the marginal cost of the goods to the stores, the fixed cost, and the discount rate are assumed to be zero. Also, (3) trust and brand power of each store are at similar levels, so they do not factor into the store selection by the consumer. In addition, it is assumed that (4) there is no entry or exit in the market for the two periods.

<table><tr><td>Variables</td><td>Description</td></tr><tr><td colspan="2">Stores:</td></tr><tr><td> $p_A, p_B$ </td><td>The unit prices of items from store A and store B.</td></tr><tr><td> $r_A, r_B$ </td><td>The amount of reward discount offered by store A and store B, when each implements a loyalty program.</td></tr><tr><td> $\alpha$ </td><td>The value of individual transaction data collected through a loyalty program.</td></tr><tr><td colspan="2">Consumers:</td></tr><tr><td>t</td><td>The unit misfit (e.g., transportation) cost, which represents the sensitivity of consumers to the differentiation of retailers. A higher sensitivity means that the consumer pays a higher misfit cost for the same degree of misfit.</td></tr><tr><td> $\tilde{U}$ </td><td>Reservation price of consumers. We assume that the reservation price is sufficiently high that all consumers in the market purchase an item.</td></tr><tr><td> $\beta$ </td><td> $=\frac{t}{\alpha}$ . Relative value of the unit misfit cost (i.e., consumer sensitivity) to the value of the individual transaction data.</td></tr></table>

Each store may implement a loyalty program, which provides reward discounts to repeat buyers in the second period. We assume that, when a loyalty program is in place, a store has a mechanism that makes all consumers who purchase from the store in the first period register for its loyalty program.<sup>4</sup> In addition, stores can record purchase histories of each consumer at zero marginal cost [1]. The reward, r, is available to repeat buyers within the stores that implement a loyalty program. This means that a consumer is offered the discounted price, $p _ { A } - r _ { A } ,$ if the consumer purchases from store A in the first period and makes another purchase from this store again in the second period. Stores operating a loyalty program can collect transaction data (i.e., purchase history), and let α represent the value of the data of each transaction.

## 3.1.2. Assumptions—consumers

During each period, a consumer demands a single unit of an item and makes a purchase from one of the stores. Consumers have a reservation price Ū for the item, and we assume that this reservation price is sufficiently high that no consumer chooses not to buy this item.

The decision of which store the consumer makes a purchase from is determined via two factors: (1) the prices of the items that are known to the consumers before they select a store and (2) the fit between the consumer and each of the stores. Regarding fit, we assume that consumers are distributed uniformly along the line connecting the two stores and incur a cost t per unit distance. This parameter, t, relates to the captured consumer sensitivity to the differentiation between stores [2,10] and is often interpreted as the unit misfit or transportation cost [14] in offline markets. Therefore, tx represents the cost of total misfit [10], such as transportation costs, when the consumer at a distance x from store A makes a purchase at store A. The net utility of the consumers is reduced by the amount of tx. A consumer will buy an item from the store that offers the higher net utility, considering the price of the item and the misfit costs.

## 3.1.3. Online vs. offline

The above assumptions are general ones that can be easily found in the horizontal differentiation literature in microeconomics and quantitative marketing research. To compare the differences between online and offline markets, we posit two additional key assumptions: (1) more dynamic consumer preference and (2) lower misfit costs in online than in offline markets.

First, following Caminal and Matutes [7] and Shin and Sudhir [24], we assume that consumers change their locations randomly and independently in each period. In addition, we assume that it is more prevalent in online markets than in offline markets for the following reasons. The relocation of consumers along the line can be interpreted as (1) the changes in consumer preference due to geographical locations, mainly in the offline markets [24], or (2) the changes in consumer psychological preference [7]. Regarding the first explanation, consider offline grocery shopping as an example, as suggested by Shin and Sudhir [24]. The store that is closest to a consumer depends on where she starts her grocery shopping trip—it can be her home, work, or any other place she may visit. For example, a consumer may prefer shopping at Giant on her way home from work, while she may prefer Shoppers during the weekends, because it is closer to her home. However, this logic cannot be applied to online markets, because consumers are not limited to their geographical locations [3].

Regarding the changes in consumers' psychological preference, consider the case where the consumers' needs or wants depend on the specific purchase situation, which changes over time [7,24]. As an example, Caminal and Matutes [7] discuss the airline industry, where consumers' needs and preferences change according to travel plan aspects, such as schedules, connecting flights, and so on. Likewise, in online markets, consumers may have changing preferences between two websites based on their distinct features, such as product descriptions and/or the richness of the customer reviews. These factors can change depending on the product of interest. For example, consider a consumer comparing Amazon (www.amazon.com) and Drugstore.com (www. drugstore.com) to purchase kids' vitamins<sup>5</sup> in the first period, who then compares the two retailers again when making a purchase of fitness equipment (e.g., Fitbit) during the second period. Both items are available at both stores. However, significant differences can be observed in the ways the items are described. For the vitamin product, Drugstore.com provides detailed descriptions of the vitamins, including usage, dosage, side effects, and supplementary fact tables that can be found on the back of the actual product box. These are not available on Amazon's website. On the other hand, for Fitbit, Amazon provides richer information, with thousands of consumer reviews. Therefore, consumers may have different store preferences for each period, depending on the product being purchased.

The changes of psychological preference can occur both online and offline. But in offline markets, physical restriction provides an additional burden for consumers to change their position from their first-period choice. This leads to our assumption that consumer preference is more dynamic online than offline.

The second key assumption that characterizes the difference between online and offline markets is that consumers' sensitivity to the differentiation of stores, t, is relatively smaller in online markets than in offline markets. As discussed above, t accounts mainly for misfit costs in online markets, while it incorporates transportation costs and misfit costs in offline markets. Therefore, we can make comparisons between online and offline markets by examining the varying degrees of the inconvenience cost, t, when consumers randomly relocate during each period.

## 4. Markets with stable consumer preference

In this section, for benchmark purposes, we consider an extreme case when consumers stay at the same location for both periods. This setting mainly demonstrates an offline market where consumers do not change their locations over time at all. Our main model in Section 5 relaxes this assumption and allows consumer preference to change over time for both online and offline markets.

Under this condition, we analyze three different scenarios: (1) when stores do not implement a loyalty program, (2) when only one store implements a loyalty program, and (3) when both stores implement a loyalty program.

## 4.1. No loyalty program

We begin with this simple case, which follows the basic setting of Hotelling's well-known spatial differentiation model [7,14]. Though consumers purchase products over two periods, all necessary information to make a decision about the store for the second period is known to consumers in the first period—the prices at each store, the respective distances to each store, and the unit misfit costs—because these factors do not change. Accordingly, there is no reason for consumers to change their decision from one time period to the next, if both stores do not provide a loyalty discount. As a result, all consumers repeat their store choice from the first period to the second. We can get the total demand and profits of each store by simply doubling the optimal profits in the first period.

When x represents the distance between a consumer and store A, the consumers who satisfy the following conditions purchase from store A: (1) the individual rationality (IR) constraint, $\bar { U } - ( p _ { A } - d ) -$ $t x > 0 ,$ , and (2) the incentive compatibility (IC) constraint, $\bar { U } - p _ { A } -$ $\displaystyle t x > \bar { U } - p _ { B } - t ( 1 - x )$ . The demand for store A and store B in each period is $\frac { p _ { B } - p _ { A } + t } { 2 t }$ and $\frac { p _ { A } - p _ { B } + t } { 2 t }$ . The profits of stores are given by:

$$
\pi_ {A} = \frac {p _ {A} (p _ {B} - p _ {A} + t)}{t}, \pi_ {B} = \frac {p _ {B} (p _ {A} - p _ {B} + t)}{t}.
$$

## 4.2. When only store A implements a loyalty program

Consider the case where only one store, store A, implements a loyalty program. Under the assumption that consumers know that their location in the second period will not change, they will put the future price into the consideration of their decision during the first period. When a consumer purchases from store A in the first period, the amount the consumer pays in the second period to store A is $p _ { A } -$ $r _ { A } ,$ , while the amount she pays to store B is $p _ { B } .$ Therefore, when the reservation price is sufficiently high, the marginal consumer, who is indifferent between store A and store B, is located at a distance x from store A where $( \bar { U } - p _ { A } - t x ) + ( \bar { U } - ( p _ { A } - r _ { A } ) - t x ) =$ $2 \times ( \bar { U } - p _ { B } - t ( 1 - x ) )$ ). With this demand function, store A's profits are given as $\begin{array} { r } { \pi _ { A } = ( 2 p _ { A } - r _ { A } + \alpha ) \times \frac { 2 ( p _ { B } - p _ { A } ) + 2 t + t } { 4 t } } \end{array}$ , and store B's profits are given as $\begin{array} { r } { \pi _ { B } = 2 p _ { B } \times \frac { 2 ( p _ { A } - p _ { B } ) + 2 t - r } { 4 t } . } \end{array}$

## 4.3. When both stores implement loyalty programs

Next, consider the case where both stores A and B implement loyalty programs. The consumers purchasing from store A in the first period will pay $p _ { A } - r _ { A }$ to store A in the second period, while they will pay p<sub>B</sub> to store B. Similarly, the consumers who purchased from store B in the first period will pay $p _ { B } - r _ { B }$ to store B in the second period, while they will pay $p _ { A }$ to store A. Because consumers know that they will be at the same location for the second-period purchase, they will consider what price they will pay in the second-purchase period for their purchase decision in the first period. As a result, no consumer will switch stores, because their store selection was made with the consideration that future reward discounts would be given during the second period. Therefore, when the reservation price is sufficiently high, the marginal consumer is located at a distance x from store A where:

$$
\begin{array}{c} \big (\bar {U} - p _ {A} - t x \big) + \big (\bar {U} - (p _ {A} - r _ {A}) - t x \big) = \big (\bar {U} - p _ {B} - t (1 - x) \big) \\ + \big (\bar {U} - (p _ {B} - r _ {B}) - t (1 - x) \big). \end{array}
$$

The profits are given a $\begin{array} { r } { { \mathfrak { m } } _ { A } = ( 2 p _ { A } - r _ { A } + \alpha ) \times \frac { 2 ( p _ { B } - p _ { A } ) + ( r _ { A } - r _ { B } ) + 2 t } { 4 t } , \pi _ { B } = } \end{array}$ $\begin{array} { r } { ( 2 p _ { B } - r _ { B } + \alpha ) \times \frac { 2 ( p _ { A } - p _ { B } ) + ( r _ { B } - r _ { A } ) + 2 t } { 4 t } . } \end{array}$

## 4.4. Discussion on the markets with stable consumer preference

Table 2 summarizes the optimal prices and the maximum profits of each store under the options of implementing a loyalty program.

Note that the optimal prices and rewards are not uniquely identified. Instead, the optimal prices are given as a function of the rewards and the value of the transaction data.

When a store implements a loyalty program when its competitor does not, it sets its regular price higher than that of its competitor, unless transaction data are so valuable that loyalty rewards are provided at the expense of getting the data. For example, when only store A implements a loyalty program, the price difference between the two stores is $\begin{array} { r } { p _ { A } ^ { * } - p _ { B } ^ { * } = \frac { 3 r _ { A } ^ { * } - \alpha } { 6 } . } \end{array}$ . If the value of the transaction data (α) is not sufficiently high (i.e., if it is not three times higher than the reward), store A should set its regular price higher than store B in order to compensate for the loss from the offered rewards. However, as α increases, store A can set its price similar to the price of store B, because the loss will be compensated by the benefit from gathered transaction data.

## Proposition 1. Pricing with a loyalty program in stable markets

In a market where consumer preference is stable, when only one store implements a loyalty program, the store sets its regular price higher than its competitor in order to compensate the loss from offered rewards. The price difference decreases as the value of the transaction data collected through loyalty programs increases.

When store A implements a loyalty program when its competitor does not, the profit gains from implementing a loyalty program is Δπ <sup>α</sup> <sup>αð</sup> <sup>Þ</sup> <sup>þ12t</sup> , which is non-negative if α N 0. Therefore, as long as the transaction data provide a non-negative value, implementing a loyalty program is always preferred, and the best response for each store is to implement a loyalty program. As a result, the case when both stores implement loyalty programs is a unique equilibrium in this game.

## Proposition 2. Equilibrium in stable markets

In a market where consumer preference is stable, which characterizes an offline market, implementing a loyalty program is strictly the dominant strategy for both stores. Therefore, the unique Nash equilibrium is the case when both stores implement loyalty programs.

When both stores implement loyalty programs, the optimal prices are the same between the stores, due to market symmetry. Although implementing loyalty programs results in equilibrium, the profits of both stores do not improve compared with the case when neither store implements a loyalty program.

## Proposition 3. Profit impact of a loyalty program in stable markets

When consumer preference is stable, a store cannot increase profits by implementing a loyalty program if its competitor also offers a loyalty program, regardless of the value of the customer transaction data.

This result explains the prevalent skepticism over the value of loyalty programs in many offline markets. Although rewards programs create switching costs for consumers to some extent, the increase in switching cost does not provide much additional value for the stores in retaining their customers. The reason for this is that consumer preference for a specific store due to geographical restrictions is so strong that consumers rarely change the stores from which they shop in each period. Therefore, a loyalty program works only as a defensive strategy to avoid losing customers to the competitor. At the same time, both stores do not lose money because they increase their regular prices to compensate the loss from providing loyalty rewards.

## 5. Market with dynamic consumer preference

We now consider the case where consumers change their locations randomly and independently for their second purchase period. Note that the random relocation assumption implies that consumers do not know their exact locations in the second period but only know them as a distribution. A consumer's best prediction for her future location in the second period is the mean of the distribution (E(x)), which is ${ \scriptstyle { \frac { 1 } { 2 } } } ,$ as the consumers are uniformly distributed from zero to one. Similar to the previous section, we analyze three different scenarios: (1) when stores do not implement a loyalty program, (2) when only one store implements a loyalty program, and (3) when both stores implement a loyalty program.

We will use the notation ${ D _ { i } } \left( i = A o r B \right)$ to represent the segment of consumers who make their first-period purchase from each store. Likewise, ${ D _ { i j } } \left( i , j = A o r B \right)$ represents the segment of consumers for the second-period purchase, where the first and second subscripts represent the store from which the consumers purchase items in the first and the second purchase periods, respectively. For example, the segment of consumers who purchase items from store A in both periods is denoted as $D _ { A A } ,$ while the segment of consumers who purchase item from store A in the first period and from store B in the second period is denoted as $D _ { A B } .$ We will use a similar notation for the expected utilities evaluated in the first period, such that $U _ { A A }$ represents the expected utility of the consumer in the first period when she purchases from store A in the first period and expects to purchase again from store A in the second period.

Summary of optimal prices and pro ts in the market with stable consumer preference.

<table><tr><td colspan="2"></td><td colspan="2">Store A</td></tr><tr><td rowspan="3">Store B</td><td>Strategies</td><td>No loyalty program</td><td>Loyalty program</td></tr><tr><td>No loyalty program</td><td> $p_A^* = p_B^* = t$  $\pi_A^* = \pi_B^* = t$ </td><td> $p_A^* = \frac{6t + 3r_A - 2\alpha}{6}$ ,  $p_B^* = \frac{6t - \alpha}{6}$  $\pi_A^* = \frac{(a + 6t)^2}{36t}$ ,  $\pi_B^* = \frac{(a - 6t)^2}{36t}$ </td></tr><tr><td>Loyalty program</td><td> $p_A^* = \frac{6t - \alpha}{6}$ ,  $p_B^* = \frac{6t + 3r_B - 2\alpha}{6}$  $\pi_A^* = \frac{(a + 6t)^2}{36t}$ ,  $\pi_B^* = \frac{(a + 6t)^2}{36t}$ </td><td> $p_A^* = \frac{r_A + 2t - \alpha}{2}$  $p_B^* = \frac{r_B + 2t - \alpha}{2}$  $\pi_A^* = \pi_B^* = t$ </td></tr></table>

Please cite this article as: S. Lim, B. Lee, Loyalty programs and dynamic consumer preference in online markets, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.008

## 5.1. No loyalty program

When a consumer makes a purchase decision in the first period, she considers four possibilities and compares the resultant utilities: (1) purchase from store A in both periods where $U _ { A A } = \left( \overline { { { U } } } - p _ { A } - t x \right) +$ $( \overline { { U } } - p _ { A } - \frac { t } { 2 } ) , ( 2 )$ purchase from store B in both periods where $U _ { B B } =$ $\left( \overline { { U } } - p _ { B } - t ( 1 - x ) \right) + \left( \overline { { U } } - p _ { B } - \frac { t } { 2 } \right) , ( 3 )$ purchase from store A in the first period and switch to store B in the second period where $U _ { A B } =$ $( \overline { { U } } - p _ { A } - t x ) + ( \overline { { U } } - p _ { B } - \frac { t } { 2 } )$ , and (4) purchase from store B in the first period and switch to store A in the second period where $U _ { B A } =$ $\left( \overline { { U } } - p _ { B } - t ( 1 - x ) \right) + \left( \overline { { U } } - p _ { A } - \frac { t } { 2 } \right)$ . The first part of the equations is the utility from the purchase in the first period, and the second part is the expected utility of the second-period purchase. The expected utility from the second-period purchase depends only on the prices, $p _ { A }$ and $p _ { B } ,$ that are observable in the first period. Due to market symmetry, there is no feasible solution where ${ p } _ { A } \neq { p } _ { B } ,$ so we can solve the equation by stating that the expected utility from the second-period purchase is indifferent between store A and store B. In this case, consumers can make a decision about which store to go to in the first period without considering the second purchase period. Also, in this second period, with no loyalty program offered at either store, the store selection of the second-period purchase is not affected by the decision made in the first period. As a result, it is a case of the simple Hotelling competition repeating over the two periods. As a result, the analysis and results are the same as the case with no reward in Section 4.1.

## 5.2. When only store A implements a loyalty program

When only store A offers a loyalty program, it can be shown that the expected utilities of switching stores $\left( U _ { A B } , U _ { B A } \right)$ are lower than the ones of purchasing from the same stores in both periods $( U _ { A A } , U _ { B B } ) ^ { 6 }$ Therefore, the demand for the stores in the first period can be determined by comparing $U _ { A A }$ and $U _ { B B } .$ Consumers purchase from store A $\mathrm { i f } U _ { A A } > U _ { B B }$ , while purchasing from store B if $U _ { A A } < U _ { B B }$ . The indifferent consumer between store A and store B for the first-period purchase is located at a distance x from store A where $( { \overline { { U } } } - p _ { A } - t x )$ $\begin{array} { r } { \left( \overline { { U } } - ( p _ { A } - r _ { A } ) - \frac { t } { 2 } \right) = \left( \overline { { U } } - p _ { B } - t ( 1 - x ) \right) + \left( \overline { { U } } - p _ { B } - \frac { t } { 2 } \right) } \end{array}$ . Therefore, the demand of the stores in the first period are given as $D _ { A } =$ $\begin{array} { r } { \frac { 2 ( p _ { B } - p _ { A } ) + r _ { A } + t } { 2 t } \mathrm { a n d } \ D _ { B } = \frac { 2 ( p _ { A } - p _ { B } ) - r _ { A } + t } { 2 t } , } \end{array}$

In the second purchase period, we consider two segments of consumers separately (Fig. 2): (1) the consumers purchasing from store $\mathsf { A } ,$ and (2) the consumers purchasing from store B in the first purchase period. We assume that, in each segment, consumers are uniformly distributed along the line of the unit length. However, by reflecting the demand of each store in the first period, the total consumers that constitute each segment are $D _ { A }$ and $D _ { B } ,$ respectively.

The first segment, consumers purchasing an item from store A in the first period, will receive rewards from store A, and the price that these consumers should pay to store A in the second period is $p _ { A } \mathrm { ~ - ~ } r _ { A } .$ Given that the reservation price is sufficiently high, the marginal consumer, who is indifferent between store A and store B, is located at a distance x from store A where

$$
\overline {{{U}}} - (p _ {A} - r _ {A}) - t x = \overline {{{U}}} - p _ {B} - t (1 - x)
$$

If $x { \leq } \left( \frac { p _ { B } - p _ { A } + r _ { A } + t } { 2 t } \right)$ , the consumers purchase items a second time from store A, and $D _ { A A }$ is given by $\begin{array} { r } { D _ { A A } = \left( \frac { 2 ( p _ { B } - p _ { A } ) + r _ { A } + t } { 2 t } \right) \left( \frac { p _ { B } - p _ { A } + r _ { A } + t } { 2 t } \right) } \end{array}$ . On the other hand, the consumers who are at a distance x from store A where $x { > } \left( \frac { p _ { B } { - } p _ { A } { + } r _ { A } { + } t } { 2 t } \right)$ will switch to store B. This segment of consumers, $D _ { A B } ,$ , is given by $\begin{array} { r } { D _ { A B } = \left( \frac { 2 ( p _ { B } - p _ { A } ) + r _ { A } + t } { 2 t } \right) \left( \frac { p _ { A } - p _ { B } - r _ { A } + t } { 2 t } \right) } \end{array}$

Next, we consider the consumers making a purchase from store B in the first period, the segment of consumers given by $\frac { 2 ( p _ { A } - p _ { B } ) - r _ { A } + t } { 2 t }$ Because store B does not offer a loyalty program, the prices available to those consumers are $p _ { A }$ and $p _ { B } .$ . The marginal consumer, who is indifferent between store A and store B, is located at a distance x from store A, where $\bar { U } - p _ { A } - t x = \bar { U } - p _ { B } - t ( 1 - x )$ . Therefore, $D _ { B B }$ and $D _ { B A }$ are given by $\begin{array} { r } { D _ { B A } = \left( \frac { 2 ( p _ { A } - p _ { B } ) - r _ { A } + t } { 2 t } \right) \left( \frac { p _ { A } - p _ { B } + t } { 2 t } \right) } \end{array}$ and $\begin{array} { r } { D _ { B B } = \left( \frac { 2 ( p _ { A } - p _ { B } ) - r _ { A } + t } { 2 t } \right) \times } \end{array}$ $\left( { \frac { p _ { A } - p _ { B } + t } { 2 t } } \right)$

Store A earns $p _ { A }$ per customer from (1) all consumers purchasing from store A in the first period and (2) the consumers purchasing from store B in the first and switch to store A during the second purchase period. From the consumers purchasing from store A in both periods, store A earns $p _ { A } - r _ { A }$ in the second period and gets additional value α as the value of transaction data gathered through store A's loyalty program. On the other hand, the per-customer profit for store B is the same as $p _ { B }$ for all consumers. Therefore, the profits of stores are given by $\pi _ { A } = p _ { A } ( D _ { A } + D _ { B A } ) + ( p _ { A } - r _ { A } + \alpha ) \times D _ { A A }$ and $\pi _ { B } =$ $p _ { B } \times \left( D _ { B } + D _ { B B } + D _ { A B } \right)$

## 5.3. Both stores implement loyalty programs

Similar to the case in Section 5.2, a consumer's ex ante expected utilities of switching stores $\left( U _ { A B } , U _ { B A } \right)$ ) are always inferior to the ones of purchasing from the same stores in both periods $\left( U _ { A A } , \ U _ { B B } \right)$ Therefore, the demand is determined by the indifferent consumer between store A and store B for the first-period purchase, who is located at a distance x from store A where $\begin{array} { r } { ( \overline { { U } } - p _ { A } - t x ) + ( \overline { { U } } - ( p _ { A } - r _ { A } ) - \frac { t } { 2 } ) = } \end{array}$ $\left( \overline { { U } } - p _ { B } - t ( 1 - x ) \right) + \left( \overline { { U } } - ( p _ { B } - r _ { B } ) - \frac { t } { 2 } \right)$ . The demands of the stores in the first period are given as $\begin{array} { r } { D _ { A } = \frac { 2 ( p _ { B } - p _ { A } ) - ( r _ { B } - r _ { A } ) + t } { 2 t } } \end{array}$ and $D _ { B } =$ $\frac { 2 ( p _ { A } - p _ { B } ) - ( r _ { A } - r _ { B } ) + t } { 2 t }$ . The demands of consumers who purchase from store A in both periods $\left( D _ { A A } \right)$ and the demand of consumers who switch from A to B $\left( D _ { A B } \right)$ are driven with similar logic as in Section 5.2, and given as $\begin{array} { r } { D _ { A A } = \left( \frac { 2 ( p _ { B } - p _ { A } ) - ( r _ { B } - r _ { A } ) + t } { 2 t } \right) \left( \frac { p _ { B } - p _ { A } + r _ { A } + t } { 2 t } \right) } \end{array}$ and $\begin{array} { r } { D _ { A B } = \left( \frac { 2 ( p _ { B } - p _ { A } ) - ( r _ { B } - r _ { A } ) + t } { 2 t } \right) \left( \frac { p _ { A } - p _ { B } - r _ { A } + t } { 2 t } \right) } \end{array}$

Among the consumers who purchased an item from store B in the first period, the indifferent consumer between store A and store B is located at a distance x from store A where:

$$
\overline {{U}} - p _ {A} - t x = \overline {{U}} - (p _ {B} - r _ {B}) - t (1 - x).
$$

Therefore, $\operatorname { i f } x { < } \left( { \frac { p _ { B } - r _ { B } - p _ { A } + t } { 2 t } } \right)$ , consumers switch from store B to store $\mathsf { A } \left( D _ { B A } \right)$ , which is given as $\begin{array} { r } { D _ { B A } = \left( \frac { 2 ( p _ { A } - p _ { B } ) - ( r _ { A } - r _ { B } ) + t } { 2 t } \right) \left( \frac { p _ { B } - p _ { A } - r _ { B } + t } { 2 t } \right) } \end{array}$ . Otherwise, consumers purchase items from store B again $\left( D _ { B B } \right)$ , and $D _ { B B }$ is given as $\begin{array} { r } { D _ { B B } = \left( \frac { 2 ( p _ { A } - p _ { B } ) - ( r _ { A } - r _ { B } ) + t } { 2 t } \right) \left( \frac { p _ { A } - p _ { B } + r _ { B } + t } { 2 t } \right) } \end{array}$

The profits for store A and store B are given as $\pi _ { A } = p _ { A } ( D _ { A } +$ $D _ { B A } ) + ( p _ { A } - r _ { A } + \alpha ) \times D _ { A A }$ and $\pi _ { B } = p _ { B } ( D _ { B } + D _ { B B } ) + ( p _ { B } -$ $r _ { B } + \alpha ) \times D _ { A B } .$

## 5.4. Discussion on markets with dynamic consumer preference

Table 3 summarizes the optimal prices and the maximum profits of stores that have the option to implement loyalty programs when consumer preference changes over time.

The optimal prices and profits when only one store implements a loyalty program is analytically tractable but too complex to display. Instead, as Caminal and Matues [7] show, we can qualitatively prove that implementing a loyalty program is a dominant strategy, provided that $t > 0$ and $\alpha > 0 .$ Consider store A when it takes as given that store B does not implement a loyalty program. Store A can always enhance its profit by charging the same regular price as store $\mathsf { B } , p _ { B } = t ,$ , while providing rewards to returning customers by ε.

S. Lim, B. Lee / Decision Support Systems xxx (2015) xxx–xxx  
![](/api/attachments/B4FXBQZV/fulltext/images/82ee5919a7051bb98ff006041802e65300aadf11df36ee87a19b0bfd9e5b5a41.jpg)  
Fig. 2. Market segmentation when only one store implements a loyalty program.

## Proposition 4. Equilibrium in Dynamic Markets

In a market with dynamic consumer preference, implementing a loyalty program is a dominant strategy for both stores. Therefore, the case when both stores implement loyalty programs constitutes equilibrium.

Next, for the analysis of the case when both stores implement a loyalty program, we introduce a new variable, $\beta .$ Let $\begin{array} { r } { \beta = \frac { t } { \alpha } , } \end{array}$ which represents the ratio of the unit misfit cost to the value of individual transaction data. The difference in maximum profits $( \Delta \pi ^ { * } )$ between the cases when both stores offer a loyalty program (<sub>πBoth Reward</sub><sup>⁎</sup> ) and when neither store offers a loyalty program ( <sup>⁎</sup> ) can be represented as a function of β: $\Delta \pi ^ { * } = \pi _ { B o t h R e w a r d } ^ { * } - \pi _ { N o R e w a r d } ^ { * } = f ( \beta )$

Fig. 3 shows $\Delta \pi ^ { * }$ as a function of $\beta .$ This function crosses the xaxis at approximately 0.216. The loyalty programs yield higher profits when $\beta$ is small, while any extra profits decrease as $\beta$ increases. $\mathsf { A }$ lower $\beta$ implies (1) lower sensitivity of consumer preference $( \mathrm { i . e . } ,$ , smaller t) or (2) higher value of transaction data (i.e., bigger α).

Summary of optimal prices and profits in the market with dynamic consumer preference.

<table><tr><td>Case</td><td>Optimal prices and maximum profits</td></tr><tr><td>No rewards</td><td> $p_{A}^{*}=p_{B}^{*}=t$  $\pi_{A}^{*}=\pi_{B}^{*}=t$ </td></tr><tr><td>Only one store (A) offers rewards</td><td> $p_{A}^{*}=g_{1}(t,\alpha),\ p_{B}^{*}=g_{2}(t,\alpha)$  $\pi_{A}^{*}=h_{1}(t,\alpha),\ \pi_{B}^{*}=h_{2}(t,\alpha)$ </td></tr><tr><td>Both stores offer rewards</td><td> $p_{A}^{*}=p_{B}^{*}=\frac{1}{3}\left(t-v+\frac{18t^{2}}{13t+2v}\right)$  $r_{A}^{*}=r_{B}^{*}=\frac{1}{3}(2t+v)$  $\pi_{A}^{*}=\pi_{B}^{*}=\frac{121t^{3}-24t^{2}v+9tv^{2}+2v^{3}}{234t^{2}+36tv}$ </td></tr></table>

## Proposition 5. Profit impact of loyalty program in dynamic markets

When consumer preference is dynamic, a loyalty program is more profitable in the market if (1) the sensitivity of consumers to the differentiation of stores is lower and (2) the potential value of transaction data is higher

When t is high, a loyalty program is not likely to contribute positively to profits and, instead, has a negative impact. A high t implies that consumers are sensitive to the differentiation of stores, so that it is costly for them to purchase from a less preferred store. A higher misfit cost can be due to transportation costs in the case of offline markets, or simply psychological preference. With the high misfit cost, the reward incentive does not induce additional demand, and the reward would benefit only consumers who would have purchased from the store even if the reward was not offered. In this case, the loss from offering rewards is rarely compensated by the increase in demand. When we consider an offline market as the one with relatively higher misfit costs due to transportation, the value of loyalty programs in offline markets is likely to be low. On the other hand, when the misfit cost, t, is small, the profit contribution of a loyalty program is high. This is due to consumers being

![](/api/attachments/B4FXBQZV/fulltext/images/80221655de837843c0ead5e61b89324ed59ad3a8edc1857a82693daf291cc569.jpg)  
Fig. 3. Profit gains from loyalty program ( <sup>⁎</sup> − $\pi _ { N o \ R e w a r d } ^ { * } )$ in the market with dynamic consumer preference. Note: This graph shows the case when α is 1. The change in α does not change the shape of the graph and affects only the magnitude of the profit difference. is the ratio of the unit mis t cost to the value of individual transaction data $\left( { \frac { t } { \alpha } } \right)$

Please cite this article as: S. Lim, B. Lee, Loyalty programs and dynamic consumer preference in online markets, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.008

S. Lim, B. Lee / Decision Support Systems xxx (2015) xxx–xxx

willing to revisit the less preferred store if they can use the reward they received from their past purchase. In this regard, the loyalty program creates effective switching costs for the consumers.

The detrimental effect of high misfit cost on the profitability of loyalty programs can be mitigated by the value of transaction data (α) gathered through loyalty programs. Therefore, retailers who are equipped with a capability to mine data collected from a loyalty program and generate valuable insights from them may be able to overcome their situation and create positive gains from implementing a loyalty program.

5.5. Loyalty programs, price dispersion, and low usage of shopbots in online markets

A shopbot is a website that lists several retailers for a specific product and includes information pertaining to the price and other aspects of the product bundles [4,16,25]. Shopbots help consumers by acting as a clearinghouse with information on product offerings from various online sellers. From a rational, payoff-maximizing viewpoint, a consumer using a shopbot must always select the lowest price in the shopbot. However, empirical studies have shown that a consumer does not always choose the lowest price in a shopbot [27]. Moreover, consumer search behavior has not dramatically changed since the introduction of shopbots. Only 6% of Internet shoppers use shopbots [5,21], and consumers tend to search fewer sites as they become more experienced with online shopping [8].

Prior studies [15,26] have suggested brand loyalty and composition of other price attributes (tax, shipping cost) as plausible explanations for this observation. We propose another explanation where customers, being aware of the presence of loyalty programs in the online market, recognize that the results of a shopbot do not reveal the presence of loyalty programs at retailers and will decide to stay with a specific seller. Shopbots bear a weakness in that they display only the regular price and do not present information about the existence of a loyalty program for a seller. A cursory search at price comparison sites revealed that although many sellers that are listed in the search results had implemented loyalty programs, no price comparison site listed loyalty program information.

## 6. Discussion

Though it has been more than a decade since online markets have become major sales channels for retailers, the online marketplace is still a new environment that exhibits many unique features that warrant further academic research. There is no guarantee that marketing strategies that may have worked or not worked in offline markets will operate the same in online markets.

In this study, we develop a game-theoretic model that explains how loyalty programs work differently in online and offline markets. The analysis demonstrates that the profit gains from loyalty programs are determined by three factors: (1) the dynamics of consumer preference, (2) the sensitivity of consumer preference to store differentiation, and (3) the value of transaction data collected through loyalty programs. When consumer preference is relatively stable and sensitive to the differentiation of stores, a loyalty program has little financial value, as observed in many offline markets where consumers are geographically bound to certain locations.

On the other hand, when consumer preference is dynamic, loyalty programs could likely deliver substantial profit gains, given that it is not too costly for consumers to visit a certain store to redeem loyalty rewards. If it is costly for consumers to purchase from a relatively less-preferred store (i.e., sensitive to the difference between stores), a loyalty program is less likely to induce additional demand and, furthermore, may lose money due to the rewards given to existing customers. This case can be observed in many offline markets, where customers are subject to transportation cost to visit the stores. However, if the misfit cost is low, as in many online markets, the profit gains from loyalty programs can be substantial.

Our results also suggest that the benefits of analyzing transaction data gathered through loyalty programs have little impact on the profit of a retailer when consumer preference is stable. This is due to the fact that these benefits are distributed to consumers because of competition. On the other hand, with dynamic consumer preference, retailers' profit gains depend on the value they derive from transaction data. On one extreme, if retailers do nothing with the data collected through loyalty programs, these programs will have only a negative impact on the profit of the retailers. Therefore, our results strongly recommend that retailers should invest in data-mining capabilities and technologies, especially if they want profitable returns from implementing loyalty programs.

Our model is a highly simplified, abstract characterization of loyalty programs and does have several limitations, which provide further opportunities for future research. First, the locations in the second period may not be completely random [24]. A more realistic assumption may be to allow correlation in preferences across time, but the model is not analytically tractable with this new assumption. For future study, it would be worth examining correlated preference with a simulation approach. Empirical assessment on this assumption and the model would be worthwhile to undertake.

Second, our model is a two-period model, which is important given that loyalty programs operate on a longer term. A natural extension of our model is to consider multi-period analysis. Furthermore, a loyalty program is a dynamic promotion vehicle as rewards accumulate, meaning that the program is deemed more worthwhile as points accumulate. In addition, there are several different schemes for loyalty programs. Some retailers require consumers to use rewards during a specific period of time, after which the accumulated rewards will expire. Other retailers impose various restrictions on the use of rewards, such as a minimum purchase requirement. Loyalty programs with different schemes can have varying degrees of impact on the profit for the retailer and, in turn, will lead to different performances for online and offline markets.

Third, we consider pure offline or online stores. Many major retailers in the real world, however, have both online and offline channels. Therefore, the effect of loyalty programs can be quite different for dual-channel retailers. Consumers may earn rewards from offline stores and use them for online shopping, and vice versa. The competition between dual-channel retailers would provide deeper insights on the management of loyalty programs.

Fourth, we focused on assessing only the financial impact of loyalty programs, but loyalty programs may have other positive indirect effects. They may induce higher-volume purchase [19], or enhance psychological loyalty of consumers [11], all of which serve as points that offer further opportunities for future research.

Despite the limitations mentioned above, our study contributes to the academic research in several ways. First, our study contributes to the literature on loyalty programs by identifying key factors that determine the profitability of loyalty programs. In particular, our study is the first attempt to investigate the different impact of loyalty programs on the profit of retailers between offline and online markets. Our model explicitly examines the effects of two characteristics within online markets—relatively higher dynamics of consumer preference and lower sensitivity to the differentiation between retailers in online markets. These factors characterize the condition where loyalty programs provide significant profit gains for retailers.

Second, our study is the first attempt to consider the value of transactions gathered through loyalty programs in the analysis of profit implications related to loyalty programs. Our model shows that, although transaction data gathered through loyalty programs have the potential to deliver positive values to retailers, the benefits can be realized only when consumer preference is dynamic, and consumers are less sensitive to the difference between retailers.

Our study provides several practical implications as well. First, our model clearly demonstrates that there are certain conditions where

Please cite this article as: S. Lim, B. Lee, Loyalty programs and dynamic consumer preference in online markets, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.008

loyalty programs provide positive value. Managers should set their expectations of loyalty programs accordingly based on their customer base and market conditions. Our model suggests that retailers should not expect significant profit gains from loyalty programs when customer preference is relatively stable, because loyalty programs work only as a defensive strategy to retain existing customers. If consumer preference is dynamic but sensitive to the differentiation between stores, the profit can actually decrease; the costs of providing rewards can outweigh the potential of attracting repeat customers. Therefore, managers should understand that loyalty programs could be beneficial only when consumer preference is dynamic and consumers are relatively insensitive to the difference between retailers, the condition often observed in online markets.

Second, our study strongly suggests that even if retailers have not enjoyed substantial financial benefits from implementing loyalty programs in offline channels, they may still want to consider investing in and adopting loyalty programs for their online channels. Our model suggests that the underlying differences between online and offline markets can drive substantial differences between two channels in terms of profit gains from loyalty programs.

Third, our results also suggest that the potential for profit gains due to loyalty programs improves with the increase in the value of transaction data gathered through loyalty programs. This result emphasizes the importance of complementary data-mining capabilities and technologies in order to take full advantage of the benefits from loyalty programs. Therefore, retailers wishing to make profitable gains from implementing loyalty programs should consider investing in datamining capability and technologies, which will in turn enhance the potential of gaining insights from these loyalty programs.

## References

[1] A. Acquisti, H.R. Varian, Conditioning prices on purchase history, Mark. Sci. 24 (3) (2005) 367–381.

[2] j.Y. Bakos, Reducing buver search costs: implications for electronic marketplaces. Manag. Sci. 43 (12) (1997) 1676–1692.

[3] S. Balasubramanian, Mail versus mall: a strategic analysis of competition between direct marketers and conventional retailers, Mark. Sci. 17 (3) (1998) 181–195.

[4] M.R. Baye, J. Morgan, P. Scholten, Price dispersion in the small and in the large: evidence from an Internet price comparison site, J. Ind. Econ. 52 (4) (2004) 463–496.

[5] E. Brynjolfsson, M.D. Smith, Frictionless commerce? A Comparison of Internet and conventional retailers, Manag. Sci. 46 (4) (2000) 563–585.

[6] G. Bulkley, The role of loyalty discounts when consumers are uncertain of the value of repeat purchases, Int. J. Ind. Organ. 10 (1) (1992) 91–101.

[7] R. Caminal, C. Matutes, Endogenous switching costs in a duopoly model, Int. J. Ind. Organ. 8 (3) (1990) 353–373.

[8] P.Y. Chen, L.M. Hitt, Measuring switching costs and the determinants of customer retention in Internet-enabled businesses: a study of the online brokerage industry, Inf Syst, Res. 13 (3) (2002) 255–274

[9] J. Crémer, On the economics of repeat buying, RAND J. Econ. 15 (3) (1984) 396–403.

[10] R. Dewan, B. Jing, A. Seidmann, Product customization and price competition on the internet, Manag. Sci. 49 (8) (2003) 1055–1070.

[11] M. Dorotic, T.H.A. Bijmolt, P.C. Verhoef, Loyalty programmes: current knowledge and research directions Int. I Manag, Rey, 14 (3) (2012) 217–237.

[12] G.R. Dowling, M. Uncles, Do customer loyalty programs really work? Sloan Manag. Rev, 38 (4)(1997) 71–82

[13] E.J. Fox, A.L. Montgomery, L.M. Lodish, Consumer shopping and spending across retail formats, J. Bus. 77 (2) (2004) S25–S60.

[14] H. Hotelling, Stability in competition, Econ. J. 39 (153) (1929) 41–57.

[15] E.J. Johnson, W.W. Moe, P.S. Fader, S. Bellman, G.L. Lohse, On the depth and dynamics of online search behavior, Manag. Sci. 50 (3) (2004) 299–308.

[16] J.O. Kephart, A.R. Greenwald, Shopbot economics, Auton. Agent. Multi-Agent Syst. 5 (3) (2002) 255–287.

[17] P. Klemperer, Markets with consumer switching costs, Q. J. Econ. 102 (2) (1987) 375–394.

[18] P.K. Kopalle, S.A. Neslin, The economic viability of frequency reward programs in a strategic competitive environment, Rev. Mark. Sci. 1 (2003) 1–39.

[19] R. Lal, D. Bell, The impact of frequent shopper programs in grocery retailing, Quant. Mark. Econ. 1 (2003) 179–202.

[20] Y. Liu, R. Yang, Competing loyalty programs: impact of market saturation, market share, and category expandability, J. Mark. 73 (1) (2009) 93–108.

[21] A.L. Montgomery, K. Hosanagar, R. Krishnan, K.B. Clay, Designing a better shopbot, Manag. Sci. 50 (2) (2004) 189–206

[22] M.C. Nideau, M. Singer, The secret to creating loyalty programs that actually work, business insider, 2014.

[23] B. Sharp, A. Sharp, Loyalty programs and their impact on repeat-purchase loyalty patterns, Int. J. Res. Mark. 14 (5) (1997) 473–486.

[24] J. Shin, K. Sudhir, A customer management dilemma: when is it profitable to reward one's own customers? Mark, Sci, 29 (4) (2010) 671–689

[25] M.D. Smith, The impact of shopbots on electronic markets, J. Acad. Mark. Sci. 30 (4) (2002) 446–454.

[26] M.D. Smith, E. Brynjolfsson, Consumer decision-making at an internet shopbot: brand still matters, J. Ind. Econ. 49 (4) (2001) 541–558.

[27] Z. Tang, M.D. Smith, A. Montgomery, The impact of shopbot use on prices and price dispersion: evidence from online book retailing, Int. J. Ind. Organ. 28 (6) (2010) 579–590.

[28] H.R. Varian, A model of sales, Am. Econ. Rev. 70 (4) (1980) 651–659.

[29] Z.J. Zhang, A. Krishna, S.K. Dhar, The optimal choice of promotional vehicles: frontloaded or rear-loaded incentives? Manag. Sci. 46 (3) (2000) 348–362.

[30] J. Zhang, M. Wedel, The effectiveness of customized promotions in online and offline stores, J. Mark. Res. 46 (2) (2009) 190–206.

Dr. Sanghee Lim is an Assistant Professor in the area of Information Systems at the Carey Business School, Johns Hopkins University. Her research examines the ways in which organizations employ IT to generate value. Her current research focuses on the strategic and performance implications of IT, with particular emphasis on organizational capabilities for managing strategic alliance portfolios and networks. Her work has been presented at the International Conference on Information Systems (ICIS) and the Americas Conference on Information Systems (AMCIS). She received a Ph.D. in Business Administration from the University of Michigan, and a Master of Science (M.S.) degree from Korea Advanced Institute of Science and Technology (KAIST).

Dr. Byungtae Lee is a faculty of College of Business, KAIST. And he has been served for various administrative positions at the College of Business at KAIST such as Dean of the College, Associate Dean of Academic Programs, Head of Graduate School of Management, and Ph.D. Director. He also taught at The University of Illinois at Chicago and The University of Arizona as a faculty member of their business schools. He received his Ph.D. in information systems from The University of Texas at Austin. He is currently the president of Korea Business School Association and the president of Business School Deans Association of Public Universities of Korea. He is also one of co-chairs of Asia-Pacific Affinity Group of AACSB.

His research area is Economics of Information Systems. His research topics include IT pro: ductivity measurement, strategic IT investments, electronic commerce, electronic auction markets, IT applications for health industry, and economic analysis of digital content business. Several of his research papers have appeared in several MIS and Economics journals such as MIS Quarterly, Information Systems Research, Journal of MIS etc. He was also the chair of Korean Chapter of AIS (Association of Information Systems).

He has served as an associate editor for some academic journals such as Information Systems Research, The e-Service Journal, and Electronic Commerce Research and Application. Prior to his academic profession, he had held top managerial positions in manufacturing sector as CIO and General Manager for New Business Development. He has extensively provided consulting services to Executives of global companies for IT investment and e-Business Strategies.

Please cite this article as: S. Lim, B. Lee, Loyalty programs and dynamic consumer preference in online markets, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.05.008
