---
otero_id: 10032
otero_key: "ET5K4AS7"
title: "A randomized pricing decision support system in electronic commerce"
authors: "Jianghua Wu; Ling Li; Li Da Xu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.015"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A randomized pricing decision support system in electronic commerce

Jianghua Wu <sup>a,</sup>⁎, Ling Li <sup>b</sup>, Li Da Xu <sup>b,c</sup>

<sup>a</sup> School of Business, Renmin University of China, Beijing 100872, China

<sup>b</sup> Department of Information Technology and Decision Sciences, Old Dominion University, Norfolk, VA 23529, USA

<sup>c</sup> Antai College of Economics & Management, Shanghai Jiaotong University, Shanghai 200052, China

## a r t i c l e i n f o

Article history: Received 1 August 2011 Accepted 31 December 2012 Available online xxxx

Keywords: Electronic commerce Randomized pricing Promotion Price discrimination

## a b s t r a c t

The Internet has provided great convenience for online shoppers and has presented unprecedented opportunities for online retailers to understand their customers. Getting the pricing right has emerged as one of the ultimate keys to the success of electronic commerce. Although some online retailers have tried some personalized pricing strategies for perishable capacity or inventory in some industries, consumers' resistance to price discrimination is still a great concern. Can we develop other price discrimination strategies for online sellers to sell standard durable products without giving the impression that they are treating their customers unfairly? Randomized pricing, which is proposed in this paper, belongs to this kind of strategy. In this paper, we present a framework that can be used to study the randomized pricing strategy by incorporating some new features into electronic commerce. For example, information asymmetry about the prices of products does not exist across internet users because of easy access to price information and very low searching cost. Consumers' reneging behavior is also considered. Online consumers usually wait up to a certain period of time for deals. Speci<sup>fi</sup>cally, we model online retailers' price variation as a Markov process in which the price randomly switches between high level and low level. Strategic consumers make a tradeoff between buying immediately at a high price with instant utility or buying later at a low price with a probability and discounted utility. We show in this paper that randomized pricing strategy can always generate more pro<sup>fi</sup>t than <sup>fl</sup>at pricing strategy. The effects of consumers' patience and discount factor on optimal prices and promotion probability are studied. Finally, we show that the optimal bene<sup>fi</sup>t that the retailer can obtain from hiding promotion probability depends on the value of the discount factor.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

With the development of electronic commerce and the fast growing number of Internet users, Internet has become a vital distribution channel in many industries. In recent years, emerging online stores have become another great source of retailing. Although consumers still purchase nondurable goods in traditional retail stores, e.g., Walmart, many intense Internet users have become accustomed to buying durable products online, such as computers, camcorders, and MP3 players, among others. However, most online retailers still struggle to make money out of the Web after making a huge investment in online business. Therefore, searching for ways to run an online business successfully is a great challenge. According to Baker et al. [2], getting the pricing right has emerged as one of the ultimate keys to success in managing online businesses. They observe two widely disparate approaches to pricing that dominate the online business. Many start-ups offer untenably low prices to capture <sup>fi</sup>rst-mover advantage. By contrast, many incumbents largely neglect online pricing and simply apply their of<sup>fl</sup>ine prices to the Internet.

The purpose of this research is to explore some online pricing strategies in electronic commerce. By breaking the barriers of geography and time, Internet has provided great convenience for online shoppers and unprecedented opportunities for online retailers to understand their customers. Through the Internet, consumers can instantaneously obtain all the information they need about the products they intend to buy without incurring a searching cost. Recently, with the development of 3G and 4G telecommunication technology, online retailers have provided more applications based on new operating systems (e.g., Apple OS and Android systems) for cell phones and other mobile devices (e.g., iPad). Users with wireless-connected mobile devices can access real-time commercial environments wherever they are. However, the Internet gives online companies opportunities to test customers' price sensitivity, change prices instantly, and segment customers. In the last decade, electronic commerce provided online sellers a <sup>fi</sup>eld for experimenting with different alternatives for pricing. For example, Amazon.com experimented with a pricing strategy in which different customers were charged different prices for the same DVD movies. By using the information gathered from the customers' pro<sup>fi</sup>le, Amazon.com adjusted the price of identical goods to make them correspond to the customers' willingness to pay. Although Amazon.com claimed that the price variations were part of a random

J. Wu et al. / Decision Support Systems xxx (2013) xxx–xxx

“price test,” many customers responded negatively to the strategy; hence, Amazon.com stopped the pricing tests (Streitfeld [22]). Hotware.com and Priceline.com are two Internet success stories, each of which used a business model based on variations of opaque pricing. Through Hotware.com, customers can buy last-minute unsold seats and hotel rooms at listed prices but with opaque quality. By contrast, Princeline.com offers customers a self-pricing alternative called Name-Your-Own-Price (NYOP) (see Hinz et al. [11]). In this setting, a buyer <sup>fi</sup>rst places an initial offer. If it is rejected, the buyer updates the offer until it is accepted. Thus, the <sup>fi</sup>nal price depends on the individual buyer's willingness to pay, which is opaque to the public. The opaque pricing strategy helps hotels and airlines cut losses by offering unsold products at discounted prices without revealing the published fares they promoted. In fact, some empirical research reported that sellers bene<sup>fi</sup>t from obfuscated pricing strategies in the electronic marketplace (see Ellison and Ellison [8]). However, designing opaque pricing is tricky, considering the strong buyer's resistance to one-to-one price discrimination. Currently, opaque pricing strategies are usually applied to sell products with perishable capacity and that entail the personal perception of quality, such as hotel rooms and <sup>fl</sup>ight seats. Can we develop other price discrimination strategies for online sellers to sell durable products with standard quality without giving the impression that they are unfairly treating their customers? The randomized pricing strategy that we propose in this paper belongs to this kind of strategy.

In this paper, we construct a randomized pricing strategy for online retailers by borrowing long-standing promotion methods from traditional retailing and incorporating some new characteristics into electronic commerce. Under this promotional pricing strategy, the online retailer can randomly provide promotions by reducing the price temporally over an in<sup>fi</sup>nite horizon. The temporary price reduction or promotion is a common strategy in brick-and-mortar stores. Sellers can provide price discount on selected packages of goods or seasonal products for a short period of time. Promotion generates a price discrimination effect because of the information asymmetry on promotions and the differentiation in searching and transportation costs across consumers. However, the Internet has brought doubleedged effects on traditional promotion strategies. On the one hand, without advertising on traditional media, online retailers can instantly change posted prices on websites. This type of advertisement gives online retailers more <sup>fl</sup>exibility to launch promotions (e.g., promotion frequency and duration) at low cost. On the other hand, because of low transportation cost in electronic commerce (e.g., free-shipping policy offered by online sellers), potential consumers are more likely to wait before they make <sup>fi</sup>nal purchases. Moreover, they are unlikely to miss deal chances during their waiting period because of the low cost that searching incurs. Some online retailers even email promotional newsletters or send SMS to registered users regularly. In other words, online product and price information visibility are equal to all potential consumers; therefore, information asymmetry across consumers does not exist. Given the fact that online sellers encounter more sophisticated consumers who are more patient and are well-informed, designing new promotion strategies oriented toward electronic commerce elicits some interesting research questions.

We now summarize our research model and questions. Using a randomized pricing strategy, we focus our study on the online retail selling of durable products over an in<sup>fi</sup>nite horizon. In view of this pricing strategy, the retailer randomly switches the price between regular level and low level; thus, we assume that customers are heterogeneous in terms of reservation price and patience. When the current price is high, consumers evaluate the tradeoff between buying at high price with an instant utility and buying later at low price with a probability and a discounted utility. The questions we raise and answer in this study are as follows. First, what are the optimal promotion probabilities and high/low prices in this pricing strategy? Second, how is optimal pricing strategy affected by consumers' discount factor and patience? Finally, how can the retailer bene<sup>fi</sup>t from hiding the pricing pattern?

The remainder of the paper is organized as follows. In Section 2, we brie<sup>fl</sup>y review the related literature and identify the contributions of our work. Then, we present the pricing model and derive optimal solutions in Section 3. In Section 4, we analyze the effects of information asymmetry on the retailers' pricing strategy. Section 5 concludes the paper with a brief summary and suggestions for further research.

## 2. Literature review

Although no explicit evidence shows that price promotion im proves the retailers' long-term pro<sup>fi</sup>t, compared with <sup>fl</sup>at price strategy, it is still a widely used strategy by practitioners (see Blattberg et al. [4] and Blattberg and Neslin [3]). Earlier studies in economics and marketing determined different kinds of price reduction strategies. For example, Varian [25] identi<sup>fi</sup>es price variation as a way to price discriminate between informed consumers and uninformed consumers. His study reveals that price variation is viewed as the eco nomic outcome of mixed strategies given that a pure equilibrium strat egy does not exist. In contrast to Varian's monopoly setting, Rao [20] models promotion competition as a multistage game in an asymmetric duopoly consisting of a national brand and a private label. In this game, regular prices are chosen <sup>fi</sup>rst, followed by the choice of promotion depths and then frequencies. Similarly, Kinberg et al. [16] explore the optimal promotion strategy to use when one premium brand face competition from one private label given the assumption that price is the only indicator of quality. Lazear's [18] study reveals that price variation over time can be used to identify reservation prices in the presence of ex ante uncertainty regarding consumer reservation prices. Lazear's model demonstrates that consumers are segmented by differ ent reservation prices. Courty and Li [6] extend Lazear's model by explicitly considering the timing of promotion, product variety, and store competition. The main result is that promotion starts earlier in the presence of competition. Generally, from the perspective of these sales models, price is non-increasing toward the end of a selling season. Some promotion models include more dimensions of consumers' varia tion. Jeuland and Narasimhan [14] assert that consumers are separated by different consumption rates and that promotion is viewed as a buyer discrimination mechanism. Kinberg and Rao [15] derive the optima promotion duration from a model in which discount price is provided only once and in which stochastic consumptions are affected by price. Iyer and Ye [12] derive the optimal promotion price for a retailer who encounters segmented consumers with heterogeneous reservation prices and inventory holding cost, given that promotion prices are of fered at intervals of time following a negative-binomial distribution. This model considers consumers' stockpiling behavior during promotion periods, Almost all existing promotion models are oriented toward traditional brick-and-mortar retailing stores. Through temporal price reduction, sellers bene<sup>fi</sup>t from price discrimination mainly because of consumers' difference in the reservation price and searching or trans portation cost.

However, we consider a promotion strategy in an electronic commerce setting where very low searching and transportation cost exist. Consumers need not buy instantly at <sup>fi</sup>rst visit of an online store; thus, we add a new dimension, that is, patience, to segment consumers. From the perspective of this model, we assume that consumers are heterogeneous in both reservation price and patience. Thus, this model can be applied to online retailers who sell durable products without immediate consumption after the purchase, such as electronic products.

The existing literature so far has ignored the initial incentive for retailers to create a given pattern of price variation. Whether a temporary promotion truly increases long-term pro<sup>fi</sup>ts for companies is not certain. After studying the promotion patterns of Coca-cola and Pepsi, Krishna [17] <sup>fi</sup>nds that, although both were promoted in alternative weeks in New York supermarkets, smart and well-informed consumers easily guessed their promotion patterns. The effect of this kind of promotion patterns on little uncertainty can be overestimated, especially in an electronic commerce environment where sellers encounter more well-informed and more sophisticated consumers. Maneuvering online consumers' purchase behavior through a simple promotion strategy (e.g., weekend sales) is actually more dif<sup>fi</sup>cult. These observations inspired research on the interaction between promotion strategies and purchase behavior. Research in this area can be classi<sup>fi</sup>ed into two categories, namely, effects of promotion patterns on purchase behavior and optimal promotion strategies that respond to strategic consumers.

The <sup>fi</sup>rst category focuses on consumers' optimal purchase decision given some known promotion patterns. For example, Golabi [9] af<sup>fi</sup>rms that the price in each period is a random variable with some known distribution. Consumption rate is also known to the retailer in each period. The consumers' objective is to <sup>fi</sup>nd an optimal inventory policy to minimize its total cost; this is very similar to the traditional dynamic lot-sizing problem. Similarly, Assuncao and Meyer [1] present a model that classi<sup>fi</sup>es price as a <sup>fi</sup>rst-order stochastic process but extends the consumption rate as a function of the current inventory level and market price information. Using this model, they explore how changes in long-term frequency and temporary correlations of price promotion should normatively affect the purchase and consumption of goods. Krishna's [17] model shows that price, as a higher-order price, and consumption rate are known in each period. She argues that the optimal policy is to purchase up to K periods on a deal. Then, she uses the Weibull distribution to simulate the effect of a dealing pattern on purchase behavior. One implication of this model is that the average quantity purchased in a deal is greater when greater certainty is determined regarding the timing of the deal.

Recently, studies have been conducted on revenue management, speci<sup>fi</sup>cally optimal pricing strategies, in relation to strategic consumer behavior (Shen and Su [21]). Our work falls into this category. Su and Zhang [24] cite a newsvendor who has strategic consumers as an example. According to them, the seller can initially charge a regular price but will most likely salvage the leftover inventory at a lower salvage price after a random demand is realized. Strategic consumers make a tradeoff between purchasing for sure at full price now and then purchasing later at a markdown price without guarantee of product availability, Afterward. Su [23l incorporates heterogeneous consumers with different valuations and degrees of patience into the framework. The problem with these models is that the price path is <sup>fi</sup>xed; thus, consumers do not face price risk. Cachon and Swinney [5] consider a similar two-period newsvendor model in which the seller charges at full price during the <sup>fi</sup>rst period and a sale price during the second period when the product is still available. Thus, the sale price depends on the demand realization in the <sup>fi</sup>rst period and remaining inventory. Based on the observation of the travel industry (e.g., airlines, hotels, and car rentals), Jerath et al. [13] consider both discounted last-minute selling and opaque selling strategies in a duopoly setting. Using mixed-strategy equilibria, they derive the optimal probability to use opaque selling for <sup>fi</sup>rms. In a similar business context, Marom and Seidmann [19] use a random last-minute selling strategy in which the seller may randomly provide high-quality products or low-quality products. They derive the optimal probabilities to offer both products in the last-minute sale. Their key <sup>fi</sup>nding is that, by randomizing the offering of last-minute deals, the sellers can increase their total pro<sup>fi</sup>t. Generally, the focus of this line of research is to schedule periodic sales to get rid of excess inventory or capacity with maximal revenue. The dynamic pricing strategy is used to in<sup>fl</sup>uence consumers' beliefs in the risk of stock-outs. Thus, these pricing strategies are more suitable for selling perishable capacity or inventory.

However, in the promotion model that we propose, no risk of product availability exists. Instead, consumers face the risk of price uncertainty and discounted utility when they delay their purchase.

Our model is more suitable for retailers who sell general durable products without a speci<sup>fi</sup>c consumption date.

To sum up, our model differs from previous promotion models and contributes threefold. First, we consider the sale of durable products (e.g., camcorders) online over an in<sup>fi</sup>nite horizon to discourage the display of stockpiling behaviors, such as purchasing package consumer goods or depleting the remaining inventory through last-minute sales. Second, we model the consumers' reneging behavior, which has not been included in previous studies. The reneging behavior means that potential consumers who visit online stores hold their intention to purchase until they see a good deal. If the price is still higher than their reservation price after the waiting period, potential customers leave the online store without buying. To the best of our knowledge, our research pioneers the study on the relationship between consumers' patience and optimal promotion frequency and depth. Third, we explore the effect of information asymmetry on the sellers' pricing strategy for the <sup>fi</sup>rst time. We show that the retailer can bene<sup>fi</sup>t from hiding the promotion probability depending on the value of the discount factor.

## 3. Promotional model with price uncertainty

We now consider a pricing problem faced by an online retailer who sells a durable product (e.g., camcorder) over an in<sup>fi</sup>nite horizon. We assume that (1) consumers are equal in information visibility on the product's price; (2) potential consumers can obtain posted promotion information on time and therefore they will not miss any opportunities to make a good deal; (3) consumers wait up to a <sup>fi</sup>xed period of time if there is no good deal (i.e., reneging behavior). We also assume that consumers who intend to purchase will visit the website at a constant rate, which is normalized to 1. Consumers are heterogeneous individuals with type θ, which is uniformly distributed within [0,1]. Their valuation (reservation price) for this product is v=θ. Consumers only consider purchasing a product when their utility v−p is positive. We <sup>fi</sup>rst consider a <sup>fl</sup>at price strategy as a benchmark and then a randomized pricing strategy, that is, the promotion strategy, and show how randomized pricing improves the retailer's pro<sup>fi</sup>t.

## 3.1. Flat price model

Under a <sup>fl</sup>at price strategy, the retailer charges a <sup>fl</sup>at price over the entire horizon. Without loss of generality, we assume that the unit cost for the retailer is 0. Suppose the price is $p _ { 0 } .$ Then, $1 - p _ { 0 }$ of the total consumers will buy this product. Therefore, the average pro<sup>fi</sup>t per period is $( 1 - p _ { 0 } ) p _ { 0 } .$ . The optimal solution is $p _ { 0 } ^ { * } = 1 / 2$ , and the retailer obtains a pro<sup>fi</sup>t of $I I _ { 0 } { = } 1 / 4$ per period.

## 3.2. Randomized pricing model

## 3.2.1. Price structure

Under the randomized pricing strategy, the retailer can randomize the price over the entire horizon. For simplicity, we model the price as a <sup>fi</sup>rst-order Markov process with two states, namely, a high price $p _ { h } ,$ which represents a regular price, and a low price $p _ { l } ,$ which represents a promotion price, where $0 { < } p _ { l } { < } p _ { 0 } { < } p _ { h } { < } 1$ (see Heyman and Sobel [10]). When the price is in a high (low) state, it remains in that state for $\mu _ { h }$ (μ ) periods. After $\mu _ { h } \ \left( \mu _ { l } \right)$ periods, the retailer decides whether to change the price or not. Hereafter, one period represents one unit of time, such as one hour, one day or one week. The transition probability matrix is described $\mathtt { a s }$ follows:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Next state</td></tr><tr><td> $p_h$ </td><td> $p_l$ </td></tr><tr><td rowspan="2">Current state</td><td> $p_h$ </td><td>α</td><td>1-α</td></tr><tr><td> $p_l$ </td><td>β</td><td>1-β</td></tr></table>

J. Wu et al. / Decision Support Systems xxx (2013) xxx–xxx

In this form of pricing, $( 1 - \alpha )$ represents the promotion probability. A larger α corresponds to a lower promotion probability or frequency. Clearly, when α=1 or $\beta = 0 ,$ it corresponds to the <sup>fl</sup>at price strategy.

Let π<sub>i</sub> $( i = h , l )$ denote the proportion of transitions that are into state i. Then, $\pi _ { i }$ satis<sup>fi</sup>es the following conditions:

$$
\pi_ {h} + \pi_ {l} = 1,\tag{1}
$$

$$
\pi_ {h} = \alpha \pi_ {h} + \beta \pi_ {l}\tag{2}
$$

$$
\pi_ {l} = (1 - \alpha) \pi_ {h} + (1 - \beta) \pi_ {l}\tag{3}
$$

The solution is

$$
\pi_ {h} = \frac {\beta}{1 - \alpha + \beta}, \pi_ {l} = \frac {1 - \alpha}{1 - \alpha + \beta}\tag{4}
$$

Thus, the proportion of time when price is in state i is given by

$$
M _ {h} = \frac {\pi_ {h} \mu_ {h}}{\pi_ {h} \mu_ {h} + \pi_ {l} \mu_ {l}} = \frac {\beta \mu_ {h}}{\beta \mu_ {h} + (1 - \alpha) \mu_ {l}}\tag{5}
$$

$$
M _ {l} = \frac {\pi_ {l} \mu_ {l}}{\pi_ {h} \mu_ {h} + \pi_ {l} \mu_ {l}} = \frac {(1 - \alpha) \mu_ {l}}{\beta \mu_ {h} + (1 - \alpha) \mu_ {l}}\tag{6}
$$

Given the memory-less property of Markov chain, whenever consumers enter the retailer' store for the <sup>fi</sup>rst time, they will see the high (low) price with probability of $M _ { h } \left( M _ { l } \right)$ . In the following analysis, we assume that the retailer randomly transits the price at the end of each period, that is, $\mu _ { h } { = } \mu _ { l } { = } 1 , M _ { h } { = } \beta / ( 1 { - } \alpha + \beta )$ , and $M _ { l } = ( 1 - \alpha ) /$ $( 1 - \alpha + \beta )$ . The retailer can commit a long-term pricing strategy with the form $S = \{ p _ { h } , p _ { l } , \alpha , \beta \}$ , which is public information. Our goal is to design the optimal pricing strategy for the retailer.

## 3.2.2. Consumer behavior

The low price is $p _ { l } .$ Thus, only consumers with $\theta \ge p _ { l }$ prefer to purchase the product, whereas consumers with θbp do not purchase the product. Consumers with $\theta \geq p _ { h } ,$ , who are called high-type consumers, may buy the product at the price $p _ { h }$ or $p _ { l } .$ Consumers with $\theta { \in } [ p _ { l } , p _ { h } ]$ who are called low-type consumers, can buy the product only at price $p _ { l } .$ When a consumer <sup>fi</sup>rst visit the webpage that sells his/her desired product, if the posted price is $p _ { l } ,$ the consumer purchases the product immediately. Otherwise, high-type and low-type consumers prefer to wait for up to $T _ { h }$ and $T _ { l }$ periods, respectively. We assume that high-type consumers are not more patient than are low-type consumers, that is, $T _ { h } \leq T _ { l } .$ . This assumption is commonly applied in revenue management models in the airline and hotel industries, where customers are categorized according to their sensitivity to price and service time (Duadel and Vialle [7]). Generally, business customers are highly sensitive to the timing of trips but not that sensitive to the price. By contrast, leisure consumers are highly sensitive to the price and begin to wait for deals long before the departure time. We also assume that consumers face costs for prolonging the purchase process. The utility for subsequent purchase is discounted by the factor δ for $0 \leq \delta < 1$ . Assume that a consumer begins to visit the website at period 0. If the consumer with type v buys the product at price $p _ { i }$ in period j, his/her utility is $\delta ^ { j } ( \nu - p _ { i } )$ . The objective of each consumer is to maximize his/her expected utility across the waiting periods. Hinz et al. [11] used the similar discount utility function to study the NYOP strategy. For low-type consumers, the decision is simple: they only wait up to T periods for the low price $p _ { l } .$ If they do not see p during T periods, they sacri<sup>fi</sup>ce purchase intentions or switch to other brands. For high-type consumers, the decision process is more complex. They need to evaluate the tradeoff between buying at high price $p _ { h }$ with instant utility and buying later at low price $p _ { l }$ with a probability and discounted utility.

We now analyze the decision process for high-type consumers. In the current period, the price is assumed to be high, and n remaining waiting periods are present. The utility for high-type consumers with type v to buy the product immediately ${ \mathrm { i } } s \nu - p _ { h } .$ . If n=0,the high-type consumer buys the product at the current price. If $n { = } 1$ , the expected utility to delay the purchase to the next period will be

$$
F (1) = \delta (\alpha (v - p _ {h}) + (1 - \alpha) (v - p _ {l})).\tag{7}
$$

If n=2, the expected utility to delay the purchase will be

$$
F (2) = \delta (\alpha (\delta (F (1) + (1 - \alpha) (v - p _ {l}))) + (1 - \alpha) (v - p _ {l})).\tag{8}
$$

Thus, for the general n-period problem, the expected utility to delay the purchase can be written as follows:

$$
\begin{array}{l} F (n) = \delta (\alpha (\delta (F (n - 1) + (1 - \alpha) (v - p _ {l}))) + (1 - \alpha) (v - p _ {l})) \\ \qquad = \sum_ {i = 1} ^ {n} \alpha^ {i} \delta^ {i} (v - p _ {h}) + \alpha^ {(i - 1)} (1 - \alpha) \delta^ {i} (v - p _ {l}) \\ \qquad = \frac {\delta (1 - \alpha^ {n} \delta^ {n}) (v - \alpha p _ {h} - (1 - \alpha) p _ {l})}{1 - \alpha \delta}. \end{array}\tag{9}
$$

Proposition 1. For high-type consumers, if the current price is high and n waiting periods remain, the following threshold value exists:

$$
\theta_ {t} (n) = \min \left\{\frac {(1 - 2 \alpha \delta + \alpha^ {n + 1} \delta^ {n + 1}) p _ {h} - (1 - \alpha) \delta \big (1 - \alpha^ {n} \delta^ {n} \big) p _ {l}}{1 - (1 + \alpha) \delta + \alpha^ {n} \delta^ {n + 1}}, 1 \right\}.\tag{10}
$$

Consumers with $\theta \in [ \theta _ { t } ( n )$ , 1] buy the product immediately at price $p _ { h } ,$ whereas consumers with $\theta \in [ p _ { h } , \theta _ { t } ( n ) ]$ delay the purchase decision to the next period.

Proof. By comparing $\boldsymbol { v } - \boldsymbol { p } _ { h }$ and $F ( n ) ,$ , we can easily obtain the above threshold value. The following can be veri<sup>fi</sup>ed:

$$
\begin{array}{l} \frac {(1 - 2 \alpha \delta + \alpha^ {n + 1} \delta^ {n + 1}) _ {p _ {h} - (1 - \alpha) \delta (1 - \alpha^ {n} \delta^ {n}) p _ {l}}}{1 - (1 + \alpha) \delta + \alpha^ {n} \delta^ {n + 1}} - p _ {h} \\ = \frac {(1 - \alpha) \delta (1 - \alpha^ {n} \delta^ {n}) (p _ {h} - p _ {l})}{1 - (1 + \alpha) \delta + \alpha^ {n} \delta^ {n + 1}} > 0. \end{array}\tag{11}
$$

This expression completes the proof Q.E.D.

This result suggests that when the reservation price of a high-type consumer is close to $p _ { h } ,$ the marginal pro<sup>fi</sup>t from the instant purchase is too small. Thus, the high-type consumer is more willing to wait for a deal in the future. The optimal decision of high-type consumers is essentially a dynamic programming problem. The threshold value is updated along with the change in n. We assume that $T _ { h } = 1$ and $T _ { l } = N \ge 1$ in the following analysis to maintain tractability. Thus, high-type consumers are less patient and prefer to wait for one more period for the deal. If high-type consumers meet the high price when they enter the market, the threshold value for buying or waiting will be:

$$
\theta_ {t} = \min \left\{\frac {(1 - \alpha \delta) p _ {h} - (1 - \alpha) \delta p _ {l}}{1 - \delta}, 1 \right\}.\tag{12}
$$

## 3.2.3. Optimal decision of the retailer

We now study the randomized pricing strategy of the retailer in which the retailer randomizes the price over the in<sup>fi</sup>nite horizon. The price of the retailer follows a Markov process, and consumers arrive at a constant rate. Thus, we calculate the expected pro<sup>fi</sup>t of the retailer obtained from consumers arriving in one period.

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015

J. Wu et al. / Decision Support Systems xxx (2013) xxx–xxx

In each period, the expected pro<sup>fi</sup>t obtained from high-type consumers is

$$
\Pi_ {h} = M _ {l} (1 - p _ {h}) p _ {l} + M _ {h} ((1 - \theta_ {t}) p _ {h} + (\theta_ {t} - p _ {h}) (\alpha p _ {h} + (1 - \alpha) p _ {l})).\tag{13}
$$

In the above function, the <sup>fi</sup>rst item represents the expected pro<sup>fi</sup>t obtained when the current price is low. The second item represents the expected pro<sup>fi</sup>t obtained when the current price is high. In this case, consumers with $\theta \in [ \theta _ { t } , 1 ]$ buy the product immediately at $p _ { h } ,$ whereas consumers with $\theta \in [ p _ { h } , \theta _ { t } ]$ delay the purchase decision to the next period. In the next period, the price may be high or low with the probability of α or $( 1 - \alpha ) ,$ , respectively.

Similarly, the expected pro<sup>fi</sup>t obtained from the low-type consumer per period is

$$
\varPi_ {l} = M _ {l} (p _ {h} - p _ {l}) p _ {l} + M _ {h} (p _ {h} - p _ {l}) (1 - \alpha^ {N}) p _ {l}.\tag{14}
$$

In the above function, $( 1 - \alpha ^ { N } )$ represents the probability that a low-type consumer may see a low price during the N waiting periods when the current price is high.

The pro<sup>fi</sup>t-maximization problem of the retailer is written as follows:

max $\begin{array} { r } { I I _ { 1 } = I I _ { h } + I I _ { l } , } \end{array}$ S

15

where $S = \{ p _ { h } , p _ { l } , \alpha , \beta \}$ . In function $\Pi _ { 1 } ,$ , the value of θ depends on $p _ { h }$ and $p _ { l } .$ Thus, the retailer optimization consists of two problems as follows:

$$
\begin{array}{l} \text {P1:} \max _ {S} \Pi_ {1 1} = \Pi_ {1} \left(\theta_ {t} = \frac {(1 - \alpha \delta) p _ {h} - (1 - \alpha) \delta p _ {l}}{1 - \delta}\right) \\ \frac {\text {s.t. :}}{(1 - \alpha \delta) p _ {h} - (1 - \alpha) \delta p _ {l}} <   1, \end{array}\tag{16}
$$

and

$$
\begin{array}{l} \text {P2:} \max _ {S} \Pi_ {1 2} = \Pi_ {1} (\theta_ {t} = 1) \\ \frac {\text {s.t. :}}{(1 - \alpha \delta) p _ {h} - (1 - \alpha) \delta p _ {l}} \geq 1. \end{array}\tag{17}
$$

Problem P1 corresponds to the case in which partial high-type consumers buy the product immediately at the current high price, whereas problem P2 corresponds to the case in which all high-type consumers delay the purchase to the next period when the current price is high.

Case I. Problem P1

$S _ { 1 } = \{ p _ { 1 h } , p _ { 1 l } , \alpha , \beta \}$ denotes the pricing strategy that guarantees the instant purchase at the high price. We have the following optimal solution.

Lemma 1. For $T _ { h } = 1$ and $T _ { l } = N \ge 1$ , when transition probabilities are fixed at α and $\beta , i f$ partial high-type consumers buy the product at the current high price, the optimal prices can be determined as follows:

$$
\left\{ \begin{array}{l} p _ {1 h} ^ {*} = \frac {2 M _ {h} \left(1 - (1 - \delta) \alpha^ {N} - (2 - \alpha) \alpha \delta\right) + M _ {l} \left(3 - \alpha^ {N} - \left(1 - \alpha^ {N} + (2 - \alpha) \alpha\right) \delta\right)}{4 M _ {l} (1 - (2 - \alpha) \alpha \delta) + M _ {h} \left(3 - \alpha^ {N} (2 + \alpha^ {N}) (1 - \delta) + (1 - 4 (2 - \alpha) \alpha) \delta\right)} \\ p _ {1 l} ^ {*} = \frac {M _ {h} \left(1 - (1 - \delta) \alpha^ {N} + \delta - 2 (2 - \alpha) \alpha \delta\right) + 2 M _ {l} (1 - (2 - \alpha) \alpha \delta)}{4 M _ {l} (1 - (2 - \alpha) \alpha \delta) + M _ {h} \left(3 - \alpha^ {N} (2 + \alpha^ {N}) (1 - \delta) + (1 - 4 (2 - \alpha) \alpha) \delta\right)} \end{array} \right.\tag{18}
$$

Proof. We calculate the <sup>fi</sup>rst- and second-order conditions with respect to $p _ { h }$ and $p _ { l }$ as follows:

$$
\frac {\partial \Pi_ {1 1}}{\partial p _ {h}} = \frac {M _ {h} \left(1 - \delta - 2 (1 - \alpha \delta + \alpha^ {2} \delta) p _ {h} + (1 - \alpha^ {N} (1 - \delta) + (1 - 4 \alpha + 2 \alpha^ {2}) \delta) p _ {l}\right)}{1 - \delta}\tag{19}
$$

$$
\begin{array}{c} \frac {\partial \Pi_ {1 1}}{\partial p _ {l}} = \frac {1}{1 - \delta} \Big ((1 - \delta) M _ {l} + M _ {h} \Big (1 - \alpha^ {N} (1 - \delta) + \Big (1 - 4 \alpha + 2 \alpha^ {2} \Big) \delta \Big) p _ {h} \\ - 2 \Big ((1 - \delta) M _ {l} + M _ {h} \Big (1 - \alpha^ {N} (1 - \delta) - \Big (2 \alpha - \alpha^ {2} \Big) \delta \Big) \Big) p _ {l} \Big), \end{array}\tag{20}
$$

$$
\frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {h} ^ {2}} = \frac {- 2 M _ {h} (1 - 2 \alpha \delta + \alpha^ {2} \delta)}{1 - \delta} <   0,\tag{21}
$$

$$
\frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {l} ^ {2}} = \frac {- 2 (1 - \delta) M _ {l} - 2 M _ {h} \left(1 - \alpha^ {N} (1 - \delta) - \left(2 \alpha - \alpha^ {2}\right) \delta\right)}{1 - \delta} <   0,\tag{22}
$$

$$
\frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {h} \partial p _ {l}} = \frac {2 M _ {h} \left(1 - \alpha^ {N} (1 - \delta) + \left(1 - 4 \alpha + 2 \alpha^ {2}\right) \delta\right)}{1 - \delta}.\tag{23}
$$

Let

$$
M = \left( \begin{array}{c c} \frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {h} ^ {2}} & \frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {h} \partial p _ {l}} \\ \frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {h} \partial p _ {l}} & \frac {\partial^ {2} \prod_ {1 1}}{\partial p _ {l} ^ {2}} \end{array} \right).
$$

The following can be veri<sup>fi</sup>ed:

$$
| M | = \frac {M _ {h} \left(4 - M _ {h} (1 - \alpha^ {N}) ^ {2} (1 - \delta) - 4 (2 - \alpha) \alpha \delta\right)}{1 - \delta} > 0.\tag{24}
$$

This is because for $0 < M _ { h } , \ \delta , \ \alpha < 1 , M _ { h } ( 1 - \alpha ^ { N } ) ^ { 2 } ( 1 - \delta ) < 1 - \delta$ and $4 ( 2 - \alpha ) \alpha \delta < 4 \delta .$ . Thus, M is negative semi-de<sup>fi</sup>nite, that is, $\boldsymbol { { \Pi } } _ { 1 1 }$ is jointly concave in $p _ { h }$ and $p _ { l } .$ Based on the <sup>fi</sup>rst-order conditions, we can obtain the optimal solution shown in Eq. (18) Q.E.D.

Given the above price decision, the retailer pro<sup>fi</sup>t is as follows:

$$
\Pi_ {1 1} = \frac {1 - \alpha + (1 - \alpha^ {N}) \beta - (\alpha (2 - \alpha) (1 - \alpha + \beta) - \alpha^ {N} \beta) \delta}{4 - 4 \alpha + (1 - \alpha^ {N}) (3 + \alpha^ {N}) \beta - (4 \alpha (2 - \alpha) (1 - \alpha + \beta) - (1 + \alpha^ {N}) ^ {2} \beta) \delta}.\tag{25}
$$

Now, the optimization problem of the retailer is equivalent to

$$
\begin{array}{l} \max _ {\{\alpha , \beta \}} H _ {1 1} = \frac {1 - \alpha + (1 - \alpha^ {N}) \beta - (\alpha (2 - \alpha) (1 - \alpha + \beta) - \alpha^ {N} \beta) \delta}{4 - 4 \alpha + (1 - \alpha^ {N}) (3 + \alpha^ {N}) \beta - (4 \alpha (2 - \alpha) (1 - \alpha + \beta) - (1 + \alpha^ {N}) ^ {2} \beta) \delta} \\ s. t.: \\ \frac {(1 - \alpha \delta) p _ {1 h} ^ {*} - (1 - \alpha) \delta p _ {1 l} ^ {*}}{1 - \delta} <   1. \end{array}\tag{26}
$$

The following proposition describes the properties of the optimal strategy.

Lemma 2. For $T _ { h } = 1$ and $T _ { l } = N \geq 1 ,$ , if partial high-type consumers buy the product at the current high price, the optimal transition probabilities will have the following properties:

$$
\begin{array}{l} \text {(1).} \beta^ {*} = 1; \\ \text {(2).} \text { For } N = 1, \end{array}
$$

$$
\alpha^ {*} = \left\{ \begin{array}{l} 0, \text {   for   } \delta <   2 / 3 \\ 1 - \sqrt {2 (1 - \delta) / \delta}, \text {   for   } \delta \geq 2 / 3; \end{array} \right.
$$

(3). For $N { > } 1 , \alpha { \in } ( 0 , 1 )$ exists, which maximizes $\Pi _ { 1 1 }$

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015

J. Wu et al. / Decision Support Systems xxx (2013) xxx–xxx

Proof. Based on Eq. (25), the following can be easily veri<sup>fi</sup>ed:

$$
\frac {\partial \Pi_ {1 1}}{\partial \beta} = \frac {(1 - \alpha^ {N}) 2 (1 - \alpha) (1 - \delta) (1 - (2 - \alpha) \alpha \delta)}{(4 - 4 \alpha + (1 - \alpha^ {N}) (3 + \alpha^ {N}) \beta - (4 \alpha (2 - \alpha) (1 - \alpha + \beta) - (1 + \alpha^ {N}) ^ {2} \beta) \delta) ^ {2}} > 0.\tag{27}
$$

Thus, the optimum of β is $\beta ^ { * } = 1$ . Given $\beta = 1$ , the profit function is

$$
\Pi_ {1 1} = \frac {2 - \alpha - \alpha^ {N} (1 - \delta) - (2 - \alpha) ^ {2} \alpha \delta}{7 - 4 \alpha - (2 \alpha^ {N} + \alpha^ {2 N}) (1 - \delta) + (1 - 4 (2 - \alpha) ^ {2} \alpha) \delta}.\tag{28}
$$

For N=1, we have

$$
\frac {\partial \Pi_ {1 1}}{\partial \alpha} = \frac {(1 - \delta) (\delta (3 - 2 \alpha + \alpha^ {2}) - 2)}{(7 + \alpha + \delta + (- 1 3 + 4 \alpha) \alpha \delta) ^ {2}}.\tag{29}
$$

Note that $3 - 2 \alpha + \alpha ^ { 2 }$ is decreasing in $\alpha \in [ 0 , 1 ]$ , and its maximum is 3. Thus, when $\delta { < } 2 / 3 , \partial { \varPi } _ { 1 1 }$ /∂α is always negative, and the optimum is $\alpha ^ { * } = 0 .$ . However, when $\delta \geq 2 / 3 , \ \partial \varPi _ { 1 1 } / \partial \alpha > 0$ for $\alpha { < } 1 - \sqrt { 2 ( 1 { - } \delta ) / \delta } ,$ and $\partial { \cal I } { \cal I } _ { 1 1 } / \partial \alpha { < } 0$ for $\alpha > 1 - \sqrt { 2 ( 1 - \delta ) / \delta } .$ Thus, profit $\boldsymbol { { \Pi } } _ { 1 1 }$ <sup>ð Þ</sup>reaches its maximum at $\alpha ^ { * } = 1 - \sqrt { 2 ( 1 - \delta ) / \delta }$

For $N { > } 1$ <sup>¼</sup>, we have

$$
\frac {\partial \Pi_ {1} ^ {*}}{\partial \alpha} = \frac {f _ {1} (\alpha)}{f _ {2} (\alpha)},\tag{30}
$$

where

$$
\begin{array}{c} f _ {1} (\alpha) = - (1 - \alpha^ {N}) (1 - \delta) (N \alpha^ {2 N} (- 1 + \delta) - \alpha (1 + (2 - \alpha) (2 - 3 \alpha) \delta) \\ \qquad + \alpha^ {N} \Big (\alpha \Big (1 + (2 - \alpha) (2 - 3 \alpha) \delta + N \Big (3 - 2 \alpha + \delta - 2 (2 - \alpha) ^ {2} \alpha \delta \Big) \Big) \Big), \end{array}\tag{31}
$$

and

$$
f _ {2} (\alpha) = \alpha \left(7 - 4 \alpha - \left(2 \alpha^ {N} + \alpha^ {2 N}\right) (1 - \delta) + \delta - 4 (2 - \alpha) ^ {2} \alpha \delta\right) ^ {2}.\tag{32}
$$

$$
\begin{array}{l} \lim _ {\alpha \to 0 ^ {+}} f _ {i} (\alpha) = 0, \lim _ {\alpha \to 0 ^ {+}} f _ {1} ^ {'} (\alpha) = (1 - \delta) (1 + 4 \delta), a n d \lim _ {\alpha \to 0 ^ {+}} f _ {2} ^ {'} (\alpha) = (7 + \delta) ^ {2}, \\ f o r i = 1, 2. T h u s, \end{array}
$$

$$
\lim _ {\alpha \rightarrow 0 ^ {+}} \frac {\partial \Pi_ {1 1}}{\partial \alpha} = \lim _ {\alpha \rightarrow 0 ^ {+}} \frac {f _ {1} ^ {\prime} (\alpha)}{f _ {2} ^ {\prime} (\alpha)} = \lim _ {\alpha \rightarrow 0 ^ {+}} \frac {(1 - \delta) (1 + 4 \delta)}{(7 + \delta) ^ {2}} > 0.\tag{33}
$$

If

$$
\begin{array}{l} f _ {3} (\alpha) = - (N \alpha^ {2 N} (- 1 + \delta) - \alpha (1 + (2 - \alpha) (2 - 3 \alpha) \delta) + \alpha^ {N} (\alpha (1 + (2 - \alpha) (2 - 3 \alpha) \delta \\ \quad + N (3 - 2 \alpha + \delta - 2 (2 - \alpha) ^ {2} \alpha \delta))), \end{array} \tag {34}
$$

then $f _ { 1 } ( \alpha ) = ( 1 - \alpha ^ { N } ) ( 1 - \delta ) f _ { 3 } ( \alpha )$ . Note that $f _ { 3 } ( \alpha { = } 1 ) { = } 0$ and $f _ { 3 } ( \alpha = 1 ) = N ( 1 + N ) ( 1 - \delta ) > 0 .$ Thus, lim $f _ { 3 } ( \alpha ) { < } 0 ,$ , and α→1<sup>−</sup>

$$
\lim _ {\alpha \rightarrow 1 ^ {-}} \frac {\partial \Pi_ {1 1} ^ {*}}{\partial \alpha} = \lim _ {\alpha \rightarrow 1 ^ {-}} \frac {f _ {1} (\alpha)}{f _ {2} (\alpha)} = \lim _ {\alpha \rightarrow 1 ^ {-}} \frac {(1 - \alpha^ {N}) (1 - \delta) f _ {3} (\alpha)}{f _ {2} (\alpha)} <   0.\tag{35}
$$

Based on Eqs. (33) and (36), α exists between 0 and 1 that maximizes ∏<sub>1</sub>.

This finding completes the proof Q.E.D.

Given that the price constraint in problem P1 is satis<sup>fi</sup>ed, some high-type consumers delay the purchase decision to the next period.

The optimal dynamic pricing strategy is described in Lemmas 1 and 2. These results suggest that, if the retailer provides the low price in one period, then he/she will return to the regular price in the next period $( \beta ^ { * } = 1 )$ . This situation is consistent across observations in many retail stores where promotions are not offered for two consecutive weeks (e.g., Krishna [17] and Marom and Seidmann [19]). However, if the current price is high, the retailer will not necessarily offer sales in the next period $( \alpha ^ { * } { > } 0 )$ because the retailer can obtain more pro<sup>fi</sup>t from high-type consumers by maintaining the high price longer. However, in the case in which low-type consumers are willing to wait for only one period $( N { = } 1 )$ and the discount factor is low $_ { ( \delta < 2 / 3 ) }$ , the retailer should switch between high and low prices over every period $( \alpha ^ { * } = 0 )$ because if the retailer does not provide a promotional price after the regular price, all low-type consumers will leave this market. Moreover, the discount factor is low $_ { ( \delta < 2 / 3 ) }$ and thus even the retailer de<sup>fi</sup>nitely lowers the price in the next period, and enough high-type consumers buy immediately at the current high price. However, when the discount factor is higher $\left( \delta > 2 / 3 \right)$ fewer high-type consumers prefer to buy at the current high price. If the retailer still provides high/low prices alternately, the loss from high-type consumers may exceed the sales from low-type consumers. Furthermore, when low-type consumers are more patient $\left( \mathrm { i } . \mathrm { e } . , N > 1 \right)$ the promotional price does not need to be provided immediately after the regular price. The optimal transition probability $\alpha ^ { * }$ depends only on the patience of low-type consumers. The effects of patience and discount factor are studied further in the following analysis.

Case II. Problem P2

In this case, all high-type consumers wait for one more period if the current price is high. $S _ { 2 } = \{ p _ { 2 h } , p _ { 2 l } , \alpha , \beta \}$ denotes the correspondent strategy. We can obtain results similar to those in Case I.

Lemma 3. For $T _ { h } = 1$ and $T _ { l } = N \ge 1$ , when transition probabilities are fixed at α and $\beta , i f$ all high-type consumers delay the purchase decision to the next period when the current price is high, the optimal prices will be determined by

$$
\left\{ \begin{array}{l} p _ {2 h} ^ {*} = \frac {M _ {l} \left(3 \alpha - \alpha^ {N}\right) + M _ {h} \left(\alpha \left(3 - \alpha^ {N}\right) - \alpha^ {N} - \alpha^ {2}\right)}{4 M _ {l} \alpha + M _ {h} \left(4 \alpha - (\alpha + \alpha^ {N}) ^ {2}\right)} \\ p _ {2 l} ^ {*} = \frac {\alpha \left(2 M _ {l} + M _ {h} \left(2 - \alpha - \alpha^ {N}\right) \right.}{4 M _ {l} \alpha + M _ {h} \left(4 \alpha - (\alpha + \alpha^ {N}) ^ {2}\right)} \end{array} . \right.\tag{36}
$$

Lemma 4. For $T _ { h } = 1$ and $T _ { l } = N \ge 1$ , if all high-type consumers delay the purchase decision to the next period when the current price is high the optimal transition probabilities will have the following properties:

$$
\begin{array}{l} \text {(1)} \beta^ {*} = 1; \\ \text {(2)} \text { For } N = 1, \alpha^ {*} = 1; \\ \text {(3)} \text { For } N > 1, \alpha \in (0, 1) \text { exists, which maximizes } \prod_ {1 2}. \end{array}
$$

Given strategy $S _ { 2 } ,$ when low-type consumers have the same level of patience as high-type consumers $( N { = } 1 )$ , the optimal solution corresponds to a <sup>fl</sup>at price strategy with $p _ { i } ^ { * } { = } 0 . 5$ and $\prod _ { 1 2 } ^ { * } = 1 / 4$

Given these optimal solutions under two strategies, we can write the expected pro<sup>fi</sup>t of the retailer as functions of α as follows:

$$
\Pi_ {1 1} = \frac {2 - \alpha - \alpha^ {N} (1 - \delta) - (2 - \alpha) ^ {2} \alpha \delta}{7 - 4 \alpha - \left(2 \alpha^ {N} + \alpha^ {2 N}\right) (1 - \delta) + (1 - 4 (2 - \alpha) ^ {2} \alpha) \delta}\tag{37}
$$

$$
\Pi_ {1 2} = \frac {\alpha (2 - \alpha^ {N} - \alpha)}{\alpha (8 - 5 \alpha) - \alpha^ {2 N} - 2 \alpha^ {N + 1}}\tag{38}
$$

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015

J. Wu et al. / Decision Support Systems xxx (2013) xxx–xxx

Proposition 1. For $T _ { h } = 1$ and $T _ { l } = N \ge 1$ , the retailer can always design dynamic pricing $S _ { i }$ to obtain a higher profit, that is, $I I _ { 1 } \geq I I _ { 0 } .$

Proof. We <sup>fi</sup>rst verify that

$$
\Pi_ {1 1} - \Pi_ {0} = \frac {\left(1 - \alpha^ {N}\right) ^ {2} (1 - \delta)}{4 (7 - 4 \alpha - (2 \alpha^ {N} + \alpha^ {2 N}) (1 - \delta) + (1 - 4 (2 - \alpha) ^ {2} \alpha) \delta)} \geq 0,\tag{and}
$$

39

$$
\Pi_ {1 2} - \Pi_ {0} = \frac {\left(\alpha^ {N} - \alpha\right) ^ {2}}{4 \left(\alpha (8 - 5 \alpha) - \alpha^ {2 N} - 2 \alpha^ {N + 1}\right)} \geq 0.\tag{40}
$$

This is because for N 1, α and $\delta < 1$

$$
\begin{array}{l} 7 - 4 \alpha - \left(2 \alpha^ {N} + \alpha^ {2 N}\right) (1 - \delta) + \left(1 - 4 (2 - \alpha) ^ {2} \alpha\right) \delta > 7 - 4 \alpha - \left(2 \alpha + \alpha^ {2}\right) (1 - \delta) \\ + \left(1 - 4 (2 - \alpha) ^ {2} \alpha\right) \delta = 7 + \alpha + \delta - (1 3 - 4 \alpha) a \delta > 7 + \alpha + \delta - 9 a \delta > 0, \end{array}
$$

and $\alpha ( 8 - 5 \alpha ) - \alpha ^ { 2 N } - 2 \alpha ^ { N + 1 } > \alpha ( 8 - 5 \alpha ) - \alpha ^ { 2 } - 2 \alpha ^ { 2 } = 8 ( \alpha - \alpha ^ { 2 } ) > 0 .$

This veri<sup>fi</sup>cation completes the proof Q.E.D.

Proposition 1 suggests that the pro<sup>fi</sup>t of the retailer under the randomized pricing strategy is always greater than that under the <sup>fl</sup>at price strategy. In a special case with $\alpha = 1$ , the price is <sup>fi</sup>xed at $p _ { i } ^ { * } { = } 0 . 5$ and $I I _ { 1 } ^ { * } { = } I I _ { 0 } ^ { * }$ , which corresponds to the <sup>fl</sup>at price strategy.

## 4. Optimal pricing strategy

In the previous analysis, both candidate strategies $S _ { 1 }$ and $S _ { 2 }$ depend on only the patience of low-type consumers N and discount factor δ. For a pair of N and δ, we need to <sup>fi</sup>rst solve for $S _ { 1 }$ and $S _ { 2 }$ and check their feasibility. If they are both feasible, we can then compare the maximums of $\boldsymbol { { \Pi } } _ { 1 1 }$ and $\boldsymbol { \Pi } _ { 1 2 }$ and choose the strategy with the higher maximal pro<sup>fi</sup>t as the optimal strategy S.

In the case with $N { = } 1 , S _ { 2 }$ is essentially a <sup>fl</sup>at price strategy. Thus, the choice is simple: $S { = } S _ { 1 }$ for δ ∈ [0, 1). Is it optimal for the retailer to induce partial consumers to buy at the high price always? Structural results for general N and δ are dif<sup>fi</sup>cult to offer, and thus we analyze an example with $N = 2$ . Under strategy $S _ { 1 }$ and given δ, we <sup>fi</sup>rst search the optimal α and calculate the maximum of $H _ { 1 1 } \ ( \mathrm { F i g . \ 1 } )$ ). We then check the feasibility of the optimal solution. For 0bαb1,

$$
\begin{array}{l} \frac {(1 - \alpha \delta) p _ {1 h} ^ {*} - (1 - \alpha) \delta p _ {1 l} ^ {*}}{1 - \delta} \\ = \frac {\alpha^ {N} ((3 - \alpha) \alpha \delta - 2) + \alpha (6 - 4 \delta - \alpha (4 - \delta - \alpha \delta))}{(1 - \delta) (\alpha (8 - 5 \alpha) - \alpha^ {2 N} + 2 \alpha^ {N + 1})} <   1. \end{array}\tag{41}
$$

![](/api/attachments/ET5K4AS7/fulltext/images/095bff8cb13a7a1a2adfca372589e6bcd24c6b72581cb6d631bb403839916e03.jpg)  
Fig. 1. Effects of on maximal pro<sup>fi</sup>ts in the case with N=2

This expression suggests that the optimal pricing scheme p<sup>⁎</sup> for any $\delta \in [ 0 , 1 )$ is feasible. Given strategy $^ { \cdot } S _ { 2 } ,$ , we solve for the optimal solution as follows:

$$
S _ {2} ^ {*} = \left\{\alpha^ {*} = 0. 4 4 9, \beta^ {*} = 1, p _ {2 h} ^ {*} = 0. 6 2 8, p _ {2 l} ^ {*} = 0. 4 6 6 \right\}.\tag{42}
$$

The maximum of the expected pro<sup>fi</sup>t is $\begin{array} { r } { { \cal I } { \cal I } _ { 1 2 } ^ { * } = 0 . 2 5 6 . } \end{array}$ . This optimal solution is feasible only when $\delta { > } 0 . 8 0 6 .$ . Fig. 1 shows that $\pi _ { 1 1 } ^ { * }$ is decreasing in $\delta ,$ li $\mathfrak { n } _ { \delta  0 } I I _ { 1 1 } ^ { * } = 0 . 2 8 8$ , and $\begin{array} { r } { \operatorname* { l i m } _ { \delta \to 1 } \varPi _ { 1 1 } ^ { * } = 0 . 2 5 . \varPi _ { 1 1 } ^ { * } } \end{array}$ and $\boldsymbol { \Pi _ { 1 2 } } ^ { * }$ intersect at $\delta _ { 1 } = 0 . 9 4$ <sup>¼ ¼</sup>. Thus, the optimal strategy is

$$
S = \{S _ {1}, \text {   for   } \delta \in [ 0, 0. 9 4 ]; S _ {2}, \text {   for   } \delta \in (0. 9 4, 1) \}.\tag{43}
$$

This example suggests that, for $N { > } 1$ , the optimal strategy is a combination of $S _ { 1 }$ and $S _ { 2 } .$ This observation is shown in the following proposition.

Proposition 2. For $T _ { h } = 1$ and $T _ { l } = N > 1$ , the expected profit $\boldsymbol { \Pi } _ { 1 1 }$ is decreasing in δ. Moreover, profit functions $\boldsymbol { \Pi } _ { 1 1 }$ and $\Pi _ { 1 2 }$ must intersect at $\delta _ { 1 } \in ( 0 , 1 $ ).

Proof. We <sup>fi</sup>rst verify that

$$
\frac {\partial \Pi_ {1 1}}{\partial \delta} = \frac {- (1 - \alpha^ {N}) 2 (1 - \alpha) ^ {2} (2 - \alpha)}{(7 - 4 \alpha - (2 \alpha^ {N} + \alpha^ {2 N}) (1 - \delta) + (1 - 4 (2 - \alpha) ^ {2} \alpha) \delta) ^ {2}} <   0.\tag{44}
$$

Then, we can verify that

$$
\begin{array}{l}\lim _ {\delta \rightarrow 0} \Pi_ {1 1} - \Pi_ {1 2} = \frac {2 - \alpha - \alpha^ {N}}{7 - 4 \alpha - 2 \alpha^ {N} - \alpha^ {2 N}} - \frac {\alpha (2 - \alpha - \alpha^ {N})}{\alpha (8 - 5 \alpha) - 2 \alpha^ {N + 1} - \alpha^ {2 N}}\\= \frac {(2 - \alpha - \alpha^ {N}) (1 - \alpha) (\alpha - \alpha^ {2 N})}{(7 - 4 \alpha - 2 \alpha^ {N} - \alpha^ {2 N}) (\alpha (8 - 5 \alpha) - 2 \alpha^ {N + 1} - \alpha^ {2 N})} > 0,\end{array}\tag{45}
$$

and

$$
\begin{array}{c} \lim _ {\delta \to 1} \Pi_ {1 1} - \Pi_ {1 2} = \frac {1}{4} - \frac {\alpha (2 - \alpha - \alpha^ {N})}{\alpha (8 - 5 \alpha) - 2 \alpha^ {N + 1} - \alpha^ {2 N}} \\ = \frac {- (\alpha^ {N} - \alpha) ^ {2}}{4 (\alpha (8 - 5 \alpha) - \alpha^ {2 N} - 2 \alpha^ {N + 1})} <   0. \end{array}\tag{46}
$$

This veri<sup>fi</sup>cation completes the proof Q.E.D.

This proposition suggests that the maximum of the expected profit given strategy $S _ { 1 }$ is decreasing in the discount factor. Given a higher discount factor, high-type consumers are more likely to delay the purchase decision to the next period. Thus, the bene<sup>fi</sup>t from the price discrimination associated with the randomized pricing strategy is reduced. The upper bound of the expected pro<sup>fi</sup>t is reached at $\delta = 0 .$

$$
\Pi_ {1 1} (\delta = 0) = \frac {2 - \alpha - \alpha^ {N}}{7 - 4 \alpha - 2 \alpha^ {N} - \alpha^ {2 N}},\tag{47}
$$

which reaches the maximum $1 / 3$ when $\alpha \to 1$ . This <sup>fi</sup>nding suggests that the randomized pricing strategy can increase the pro<sup>fi</sup>t of the retailer by at most 33.3% (from 1/4 to 1/3). Moreover, because of the monotonicity of $\varPi _ { 1 1 } , \varPi _ { 1 1 } ^ { * } { > } \varPi _ { 1 2 } ^ { * }$ if and only if $\delta { < } \delta _ { 1 }$ . This <sup>fi</sup>nding suggests that the optimal strategy S takes the form of $S _ { 1 }$ or $S _ { 2 }$ depending on the value of the discount factor.

## 4.0.1. Effects of the discount factor on pricing strategy

Given strategy $S _ { 1 } ,$ the optimal solution depends on the value of δ. The structural solution for optimal α is dif<sup>fi</sup>cult to obtain. We analyze the case with $N = 2$ to show the effect of the discount factor on the optimal solution. Effects of δ on optimal α and the prices are shown in Figs. 2 and 3, respectively. When the discount factor is high, high-type consumers are more likely to wait. Thus, the retailer should

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015

decrease the promotion frequency $( \mathrm { i } . \mathrm { e } . , 1 - \alpha )$ to reduce the probability that high-type consumers buy the product at the low price. Conversely, in response to the increasing intention of the high-type consumers to wait for the promotion, the retailer should increase the low price and decrease the high price and promotion depth $( \mathrm { i . e . , } p _ { 1 h } ^ { * } - p _ { 1 l } ^ { * } )$ , which will make the delayed purchase less attractive to high-type consumers.

We <sup>fi</sup>rst prove that the expected pro<sup>fi</sup>ts increase because of the patience of low-type consumers. The case with $\delta { = } 0 . 8$ is an example that shows the effects of the patience on optimal α and prices given strategies $S _ { 1 }$ and $S _ { 2 } .$

Proposition 4. For $T _ { h } = 1$ and $T _ { l } = N > 1$ , the expected profits under strategies $S _ { 1 }$ and $S _ { 2 }$ are increasing in N.

Proof. We can verify that

$$
\frac {\partial \Pi_ {1 1}}{\partial N} = \frac {- \alpha^ {N} (1 - \alpha^ {N}) (3 - 2 \alpha - \alpha^ {N} (1 - \delta) + \delta - 2 (2 - \alpha) ^ {2} \alpha \delta) \ln \alpha}{(7 - 4 \alpha - (2 \alpha^ {N} + \alpha^ {2 N}) (1 - \delta) + (1 - 4 (2 - \alpha) ^ {2} \alpha) \delta) ^ {2}} > 0,\tag{48}
$$

and

$$
\frac {\partial \Pi_ {1 2}}{\partial N} = \frac {- \alpha^ {N + 1} (\alpha - \alpha^ {N}) (4 - 3 \alpha - \alpha^ {N}) \ln \alpha}{(\alpha (8 - 5 \alpha) - \alpha^ {2 N} - 2 \alpha^ {N + 1}) ^ {2}} > 0.\tag{49}
$$

This is because for $N { > } 1 .$ , α and $\delta < 1$

$$
\begin{array}{c} 3 - 2 \alpha - \alpha^ {N} (1 - \delta) + \delta - 2 (2 - \alpha) ^ {2} \alpha \delta > 3 - 2 \alpha - \alpha (1 - \delta) + \delta - 2 (2 - \alpha) ^ {2} \alpha \delta \\ = (1 - \alpha) \Big (3 + \Big (1 - 6 \alpha + 2 \alpha^ {2} \Big) \delta > (1 - \alpha) (3 - 3 \delta) > 0. \end{array}
$$

This veri<sup>fi</sup>cation completes the proof Q.E.D.

Fig. 4 shows that the optimal probability α is increasing in waiting time N among low-type consumers. Intuitively, when low-type consumers are more patient by reducing promotion frequency, the retailer can increase the probability that high-type consumers will buy the product at the high price, without loss of chances for low-type consumers to see the low price. In accordance with the reduction in promotion frequency, the retailer should increase the high price to obtain more revenue from high-type consumers and decrease the low price to maintain the number of low-type consumers (Fig. 5). Consequently, the promotion depths also increase in N. In sum, the increase in the patience of low-type consumers makes the randomized pricing strategy of the retailer gain more bene<sup>fi</sup>t from price discrimination.

![](/api/attachments/ET5K4AS7/fulltext/images/ceae133335bcfe4a96c492ecdad5aae4d16dcc79380e527aa73a64a2c6b69f9b.jpg)  
Fig. 2. Effects of on optimal probability in the case with N=2.

![](/api/attachments/ET5K4AS7/fulltext/images/fb6350b0e4618b06e043303c64c7ef0a94d7c4e1cb6adcd35c0bd8b11a764a23.jpg)  
Fig. 3. Effects of δ on optimal high/low prices in the case with N=2.

## 5. Effects of information asymmetry

In the previous analysis, we assume that the optimal decision of the seller regarding the randomized pricing strategy is public information. Thus, consumers make a tradeoff between buying immediately or waiting according to known high/low prices and transition probabilities. Consumers may easily observe two levels of the price, but the exact promotion probability (i.e., α) is dif<sup>fi</sup>cult to determine if it is not shared or maintained by the retailer. We now consider a case with information asymmetry. In this case, consumers know the values of $p _ { h }$ and $p _ { l }$ but not α. Speci<sup>fi</sup>cally, we assume that consumers have no information on promotion probability and that they believe that the price in the next period will be high or low with equal probability if the current price is high. Can the retailer manipulate and bene<sup>fi</sup>t from this information asymmetry?

The retailer still solves for optimal strategies de<sup>fi</sup>ned in Problems P1 and P2. Consumer's belief on α is 0.5, and thus the threshold value of δ is

$$
\delta_ {t} = \frac {2 (1 - \delta) p _ {h} ^ {*} - \delta p _ {l} ^ {*}}{2 (1 - \delta)}.\tag{50}
$$

$\prod { _ { 2 1 } }$ and $\prod _ { 2 2 }$ denote the expected pro<sup>fi</sup>ts given strategies $S _ { 1 }$ and $S _ { 2 } ,$ respectively. Information asymmetry changes the optimal solution given strategy $S _ { 1 }$ while having no effect on decisions under strategy $S _ { 2 } ,$ that is, $\prod _ { 2 2 } = \prod _ { 1 2 } .$ Given strategy $S _ { 1 } ,$ we solve for the optimal solution as follows:

$$
\left\{ \begin{array}{l} p _ {1 h} ^ {*} = \frac {5 - 3 \alpha - (3 - \alpha) (1 - \delta) \alpha^ {N} - \left(3 - \alpha^ {2}\right) \delta}{7 - (1 - \delta) \alpha^ {N} \left(2 + \alpha^ {N}\right) - 4 \alpha - \left(3 + 2 \alpha - 2 \alpha^ {2}\right) \delta} \\ p _ {1 l} ^ {*} = \frac {3 - 2 \alpha - (1 - \delta) \alpha^ {N} - \left(1 + \alpha - \alpha^ {2}\right) \delta}{7 - (1 - \delta) \alpha^ {N} \left(2 + \alpha^ {N}\right) - 4 \alpha - \left(3 + 2 \alpha - 2 \alpha^ {2}\right) \delta} \\ \beta^ {*} = 1, \prod_ {2 1} = \frac {- 2 (1 - \delta) \alpha^ {N} - (2 - \alpha) (2 - \delta - \alpha \delta)}{2 (7 - (1 - \delta) \alpha^ {N} (2 + \alpha^ {N}) - 4 \alpha - (3 + 2 \alpha - 2 \alpha^ {2}) \delta)} \end{array} \right.\tag{. (51}
$$

![](/api/attachments/ET5K4AS7/fulltext/images/9d967cfafd0acb42a60e4570ce4479f19717ce34156311b089734df29b7adfeb.jpg)  
Fig. 4. Effects of N on optimal promotion probabilities in the case with =0.8

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015

![](/api/attachments/ET5K4AS7/fulltext/images/4f824c4bae8e86121796816cc6f1d1f59c80ade820f2ea7504b70d2249180c7d.jpg)  
Fig. 5. Effects of N on optimal high/low prices in the case with $\delta { = } 0 . 8 .$

Now we still use the case of $N = 2$ as an example to search for the optimal α that maximizes $\Pi _ { 2 1 } . ~ \alpha _ { 1 } ^ { * }$ and $\alpha _ { 2 } ^ { * }$ represent the optimal values of α in cases with symmetric and asymmetric information, respectively. We then compare the optimal strategies and performances in these two cases. Fig. 6 shows that $\alpha _ { 2 } ^ { * }$ is always less than $\alpha _ { 1 } ^ { * } .$ . This <sup>fi</sup>nding suggests that the retailer should increase the promotion frequency when information asymmetry exists. However, the retailer cannot always bene<sup>fi</sup>t from this information asymmetry. The maximal values of $\prod { _ { 1 1 } }$ and $\prod { _ { 2 1 } }$ , denoted by $\Pi _ { 1 1 } ^ { * }$ and $\Pi _ { 2 1 } ^ { * }$ , respectively, intersect at $\delta _ { 1 2 } = 0 . 7 9$ . Moreover, $\prod _ { 2 1 } ^ { * } > \prod _ { 1 1 } { } ^ { * }$ when $\delta { < } \delta _ { 1 2 } ,$ and $\dot { \prod } _ { 2 1 } ^ { * } < \prod _ { 1 1 } ^ { * }$ when $\delta > \delta _ { 1 2 }$ (Fig. 7). This <sup>fi</sup>nding suggests that the retailer can bene<sup>fi</sup>t from information asymmetry only when the discount factor is small enough $( \mathrm { i } . \mathsf { e } . , \delta { < } \delta _ { 1 2 } )$ . If the discount factor is high, the retailer should maintain the pricing strategy for consumers.

## 6. Concluding remarks

Promotion, a commonly used strategy in the retail and service industries, is currently popular among both researchers and practitioners. In previous literature, information asymmetry is identi<sup>fi</sup>ed as a main driver of price reduction as a promotion strategy. However, research on promotion strategy in electronic commerce is absent. Different from traditional retailing, online retailing possesses some unique features. For example, information asymmetry on product prices does not exist among potential online consumers because of the low cost of online searching. No transportation cost is spent to visit online stores, and thus consumers may withhold their intention to purchase to wait for deals. Information technology has enhanced the capacity of online sellers to track and analyze the purchase behavior of consumers. Considering these factors in electronic commerce, we propose and develop a randomized pricing strategy for an online retailer who sells durable goods.

Speci<sup>fi</sup>cally, we model the price variation of the retailer as a Markov process and derive the optimal promotion frequency and depth for the retailer. The reneging behavior of strategic consumers is also included in the model. In this framework, consumers are categorized according to their reservation prices and levels of patience. They make a tradeoff between buying at the current high price with instant utility and buying later at a low price with probability and discounted utility. We study the effect of patience and discount factor on the optimal pricing strategy. Furthermore, we check the incentives for online retailers to hide their promotion probability.

![](/api/attachments/ET5K4AS7/fulltext/images/d4335261ea60e49dc982aeb70a365b7ef86182848aa213326b91d6b930f08c1b.jpg)  
Fig, 6. Effects of δ on optimal probabilities in the case with $N = 2 .$

![](/api/attachments/ET5K4AS7/fulltext/images/a2d1b50b10ba2be5c17e436921d5888463970a44ad789c70bfc94aa2cba01cf8.jpg)  
Fig. 7. Effects of δ on maximal pro<sup>fi</sup>ts in the case with $N = 2 .$

Our model offers several interesting managerial insights for online retailers applying the randomized pricing strategy. First, we show that, compared with the <sup>fl</sup>at price strategy, the randomized pricing strategy always increases the pro<sup>fi</sup>t of the retailer, which can be improved by up to 33.3%. This result encourages online retailers to use more intelligent randomized pricing strategies, which are not fully explored in the current electronic commerce context. Second, our research results provide some guidelines for implementing randomized pricing according to the characteristics of consumers. Our analysis suggests that the retailer should maintain the promotional price for only one period and then return to the regular price. When low-type consumers are more patient, the retailer should decrease promotion frequency and the low price and increase the high price simultaneously. By contrast, when the discount factor is higher, the retailer should decrease the promotion frequency and the high price and increase the low price to induce high-type consumers to purchase at the high price. Third, by checking the effect of information asymmetry on pricing strategy in the background, we show that hiding promotion probability only when the discount factor is low is bene<sup>fi</sup>cial. However, when the discount factor is larger than some threshold values, the retailer should maintain the pricing strategy for consumers. These results show the importance of information on the pro<sup>fi</sup>le of consumers to implement the appropriate randomized pricing strategy.

Our model has a few limitations that provide avenues for future research. One limitation is that we only model the randomized pricing strategy of a monopolist. If competitors are present in the market, consumers may be redirected to other retailers when the current price is high. Then some other factors, such as product substitutability, searching cost, and consumer loyalty, can be included in the model to study the equilibrium outcome under competition. This model can be extended to analyze the pricing strategy for a brick-and-mortar company that opens a new online channel. Another limitation of our model is that to maintain the tractability we only consider the case with $T _ { h } = 1$ . However, we infer that some results still hold in more generic situations. For example, one of key results is that the retailer should not provide the promotion in two consecutive periods $( \mathrm { i . e . , ~ } \beta ^ { \ast } = 1 )$ We predict that even if high-type consumers are more patient $( \mathrm { i } . { \mathsf { e } } . , T _ { h } > 1 )$ ), the retailer should still follow this strategy. The essence of this randomized pricing strategy is to make price discrimination through occasional promotions. If the retailer immediately returns the price to the regular level after the promotional period, some high-type consumers may buy the product at the high price without loss of any

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015

other consumers. This is better than the strategy with offering two consecutive promotions, under which all high-type consumers arriving in the second promotional period will pay the low price.

## Acknowledgments

The authors would like to thank the guest editors and the anonymous referees for their constructive suggestions and comments on the early version of the paper. The research of the <sup>fi</sup>rst author was supported in part by the National Natural Science Foundation of China (grant no. 71171192), the Fundamental Research Funds for the Central Universities and the Research Funds of Renmin University of China (grant no. 10XNJ042).

## References

[1] J.L. Assuncao, R.J. Meyer, The rational effect of price promotions on sales and consumption, Marketing Science 39 (5) (1993) 517–535.

[2] W.L. Baker, E. Lin, M.V. Marn, C.C. Zawada, Getting prices right on the Web, McKinsey Ouarterly. June 2001.

[3] R.C. Blattberg, S.A. Neslin, Sales Promotion: Concepts, Methods and Strategies, Prentice-Hall, Englewood Cliffs, NJ, 1990.

[4] R.C. Blattberg, R.B. Edward, J.F. Fox, How promotions work, Marketing Science 14 (3) (1995) 122–132.

[5] G.P. Cachon, R. Swinney, Purchasing, pricing, and quick response in the presence of strategic consumers, Management Science 55 (3) (2009) 497–511.

[6] P. Courty, H. Li, Timing of seasonal sales, Journal of Business 72 (4) (1999) 545–572.

[7] S. Duadel, G. Vialle, Yield Management: Applications to Transport and other Service Industries, ITA, Paris, 1994

[8] G. Ellison, S.F. Ellison, Search, obfuscation, and price elasticities on the Internet, Econometrica 77 (2) (2009) 427–452.

[9] K. Golabi, Optimal inventory policies when ordering prices are random, Operations Research 33 (3) (1985) 575–588.

[10] D.P. Heyman, M.J. Sobel, Stochastic Models in Operations Research Volume 1, McGraw-Hill Inc. New York. 1982

[11] O. Hinz, I.H. Horn, M. Spann, Price discrimination in e-commerce? An examination of dynamic pricing in name-your-own-price markets, MIS Quarterly 35 (1) (2011) 81–98.

[12] A.V. Iyer, J. Ye, Assessing the value of information sharing in a promotional retail environment, Manufacturing & Service Operations Management 2 (2) (2000) 128–143.

[13] K. Jerath, S. Netessine, S.K. Veeraraghavan, Revenue management with strategic customers: last-minute selling and opaque selling, Management Science 56 (3) (2010) 430–448.

[14] A.P. Jeuland, C. Narasimhan, Dealing–temporary price cuts–by seller as a buyer discrimination mechanism, Journal of Business 58 (3) (1985) 295–308.

[15] Y. Kinberg, A.G. Rao, Stochastic models of a price promotion, Management Science 21 (8) (1975) 897–907.

[16] Y. Kinberg, A.G. Rao, M.F. Shakun, A mathematical model for price promotions, Management Science 20 (6) (1974) 948–959.

[17] A. Krishna, The impact of dealing patterns on purchase behavior, Marketing Science 13 (4) (1994) 351–373.

[18] E.P. Lazear, Retail pricing and clearance sales, The American Economic Review 76 (1) (1986) 14–32.

[19] O. Marom, A. Seidmann, Using “last-minute” sales for vertical differentiation on the Internet, Decision Support Systems 51 (4) (2011) 894–903.

[20] R.C. Rao, Pricing and promotions in asymmetric duopolies, Marketing Science 10 (2) (1991) 131–144.

[21] Z.M. Shen, X. Su, Customer behavior modeling in revenue management and auctions: a review and new research opportunities, Production and Operations Management 16 (6) (2007) 713–728.

[22] D. Streitfeld, Amazon pays a price for marketing test, Washington Post, October 2000.

[23] X. Su, Inter-temporal pricing with strategic customer behavior, Management Science 53 (5) (2007) 726–741

[24] X. Su, F. Zhang, Strategic customer behavior, commitment, and supply chain performance, Management Science 54 (10) (2008) 1759–1773.

[25] H.R. Varian, A model of sales, The American Economic Review 70 (9) (1980) 651–659.

Jianghua Wu is an Associate Professor of Operations Management at the School of Business, Renmin University of China. He obtained his PhD in Operations Management from Purdue University. His main research interests include Supply Chain Management, Inventory Control, Revenue Management and Marketing/Operations Management Interfaces. His work has been published in Computers & Operations research, International Journal of Production Research, OMEGA, etc. His research has been supported by the National Natural Science Foundation of China and research grants from the Ministry of Education.

Ling Li is a Full Professor at the College of Business and Public Administration, Old Dominion University, USA, and an E.V. Williams Research Fellow. She is a Certi<sup>fi</sup>ed Fellow in Production and Inventory Management (CFPIM). Her work has been nation ally and internationally recognized. She has published over 160 research papers, encyclopedia articles, book chapters, and two books

Li Da Xu is a Changjiang Chair Professor, an Eminent Professor at the Old Dominion University, and a Professor at Shanghai Jiaotong University. He is the founding Editor-in-Chief of the journal entitled Enterprise Information Systems published by Taylor & Francis, founding Chair of IFIP TC8 WG8.9 and founding Chair of the IEEE SMC Society Technical Committee on Enterprise Information Systems.

Please cite this article as: J. Wu, et al., A randomized pricing decision support system in electronic commerce, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.015
