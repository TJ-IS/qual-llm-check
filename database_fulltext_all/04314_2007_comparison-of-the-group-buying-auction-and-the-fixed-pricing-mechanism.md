---
otero_id: 4314
otero_key: "2P475FYW"
title: "Comparison of the group-buying auction and the fixed pricing mechanism"
authors: "Jian Chen; Xilong Chen; Xiping Song"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.11.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comparison of the group-buying auction and the fixed pricing mechanism

Jian Chen <sup>a,⁎</sup>, Xilong Chen <sup>a</sup>, Xiping Song

<sup>a</sup> Department of Management Science, School of Economics and Management, Tsinghua University, Beijing, 100084, China <sup>b</sup> Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, NT, Hong Kong, China

Received 21 December 2004; received in revised form 10 August 2006; accepted 5 November 2006 Available online 29 December 2006

## Abstract

With the development of electronic commerce, online auction plays an important role in the electronic market. This paper analyzes the seller's pricing strategy with the group-buying auction (GBA), a popular form of online auction, which is designed to aggregate the power of buyers to gain volume discounts. Based on the bidders' stochastic arrival process and optimal strategy with independent private value model, this paper analyzes the sellers' optimal price curve of the GBA in the uniform unit cost case and in some supply chain coordination contracts. We find that the best discount rate is zero, which implies the optimal GBA is equivalent to the optimal fixed pricing mechanism (FPM). Then we compare the GBA with the FPM—in two special cases, the economies of scale and risk-seeking seller, and find that (1) when economies of scale are considered, the GBA outperforms the FPM; (2) when the seller is risk-seeking, the GBA also outperforms the FPM. © 2006 Elsevier B.V. All rights reserved

Keywords: Group-buying auction; On-line auction; Fixed pricing mechanism

## 1. Introduction

With the development of E-business, online auction plays an important role. Johnson et. al. [13] point out that the online consumer auction sales in the US will reach \$65 billion by 2010, accounting for nearly onefifth of all online retail sales. The popularity of the online auctions creates many new kinds of price mechanisms, where the consumers participate more and more in the price-setting process. The group-buying auction (GBA) is one of them. As a homogeneous multi-unit auction, the GBA has many users on the sites such as

LetsBuyIt.com and Ewinwin.com. In contrast to the traditional auction, where bidders compete against one another to be the “winner” with the highest price, the GBA enables bidders to aggregate to offer a lower price at which they all “win” [11].

The GBA was once regarded as a promising novel auction mechanism, e.g., the GBA websites Mercata.com and Mobshop.com were once widely recognized as international market leaders. Partly because they misused the mechanism in the B2C market, Mercata closed down in January 2001 [6], and Mobshop changed its strategic direction to the B2B market [5]. Since then, many groupbuying websites have failed or reoriented themselves and have given up the mechanism. However, some (e.g., LetsBuyIt.com and Ewinwin.com) still use the GBA as their pricing mechanism and have passed the winter of the

E-commerce. The GBA is based on the idea that “globally locate, encourage and enable all buyers wishing to purchase a particular product or service within a given time frame to join forces in a buying group formed specifically to accomplish the desired purchase” [11]. If this idea does work, why do so many websites fail? Comparing to the traditional FPM, in which scenario can the GBA bring us more profit? These questions motivate us to study the GBA with a theoretical analysis.

The study on the GBA is rare. Most existing papers on the GBA is experimental. They use the data from the GBA websites to study the customer behaviors. Kauffman and Wang [14,15] analyze the changes in the number of orders for Mobshop-listed products over various periods, and find the “positive participation externality effect,” the “price drop effect,” and the “ending effect”. These experimental studies on consumer behavior are very useful for building the analytical models to study the GBA. Anand and Aron [1] devise an analytical model to study the GBA. Based on the assumptions that the revenue function is derived from a deterministic demand curve, they compare the fixed pricing mechanism (i.e., FPM) with the GBA in different scenarios, e.g., uncertain demand regime and economies of scale. Using the simple analytic model, they finds that the GBA outperforms the FPM when 1) the seller faces uncertain market with two possible intersecting demand regimes and 2) the seller sets the price vector before production in combination with scale economies. With Anand and Aron's results, we know that the value of the GBA depends on the nature of the uncertainty about the demand regimes. If the sellers do know about in which demand regime they are operating, they are almost always better off by running a postedprice market. So, it is critical for the seller to know about the advantage of the GBA over the FPM before using it.

Although similar to Anand and Aron's paper we also focus on the conditions that favor the GBA, we deal different scenarios.

First, the demand assumption is different in the following ways.

i) Different from the deterministic demand curve in Anand and Aron's paper, the demand in our model is based on the rational strategy of the bidders in the GBA. According to Gupta and Bapna [9], the customers in the online auctions become involved in the price-setting process and their bidding strategy becomes very important to determine the trading price. Hence, studying the GBA based on the customers' behavior becomes more practical. Our paper based on Chen et. al.'s paper [4], which builds a dynamic game model for the GBA and studies the bidders' optimal strategy. It proves that the mechanism is incentive compatible for bidders under the IPV (independent private values) assumption.

ii) We consider a different demand uncertainty case. In Anand and Aron's paper, they consider the seller operates in two different demand regimes. In each demand regime, the demand is deterministic. In reality, even if we are clear of the customer segmentation (demand regime), the visibility in volatile B2C markets is sharply limited because so many different variables are in play. According to Sull [21], in volatile markets, many variables are individually uncertain and they interact with one another to create unexpected outcomes, the randomness in the demand is inevitable. Hence, we consider the randomness in the regime. Pinker et al. [19] point out that for the online auction, the bidding process is an important issue. Our model introduces the bidding process, which simulates the randomness in the demand regime and the bidders' strategy in the GBA.

Second, we study the GBA in the case when the risk seeking seller is considered. Astebro [2] points out that risk-seeking is one of several plausible reasons why so many inventors proceed to develop their inventions while only a small fraction can reasonably expect to earn positive returns on their efforts. Risk seeking also applies to the E-business world. Many websites care more about the possible explosive expanding market as Ebay encounters than the expected profit. Hence the resulting insights on the risk seeking sellers can be of value to the sellers whose objective is not only on the expected revenue.

This paper considers a situation that one auctioneer uses the GBA to sell products to the individual online consumers. As what happens in the online auction, in our paper, the consumers with different values to the objects may arrive to the auction with a stochastic process. They make their decision according to their rational strategy. The auctioneers may face uncertain demand, supply chain contracts, economies of scale and risk seeking scenario. The objective of our paper is to answer the following questions: Can the GBA bring more profit than the fixed pricing mechanism (FPM)? In what scenarios does the GBA perform better?

The rest of this paper is organized as follows. In Section 2, we explain the GBA and the FPM. Section 3 describes the problem that we study. In Section 4, the equivalence of the optimal GBA and FPM is proved. Section 5 studies the GBA in various scenarios. In

Section 6, we summarize the paper and highlight directions for future study.

## 2. The group-buying auction and the fixed pricing mechanism

Although there exist plenty of studies on traditional auctions (see Klemperer (1999) [16] for surveys of the auction literature), these results cannot be used in the GBA directly because the GBA has the following properties. 1) It is more often used in the B2C and B2B markets. Hence, we should pay more attention to its multi-unit property. 2) Unlike traditional auctions, in which the number of bidders is fixed, in the GBA the number is random and the seller does not know how many bidders will take part. 3) It is widely used by different companies whose risk attitudes are quite different. Hence, we should not only consider the riskneutral profit-maximizing seller, as do most studies of the traditional auction. Paying more attention to the different objectives will be more practical.

We list the main notation in Appendix F for reference. A typical GBA includes two rounds, the offer round and the bidding round. The auction period T and the number of objects N are exogenously given. The seller acts first in the offer round, and determines the price curve $P { = } ( p _ { 1 } , p _ { 2 } { , } { \ldots } { , } p _ { N } ) , p _ { 1 } { \geq } p _ { 2 } { \geq } \cdots { \geq } p _ { N } ,$ , where $p _ { i }$ denotes the price if the sold quantity is i. Then the bidding round begins at time 0. In this round, the buyers arrive with a stochastic process. The arriving buyer determines whether and how much to bid. Once the buyer bids, he is not permitted to change the bid. The auction will end when either of the following two cases occurs: 1) there are N bids; or 2) the time reaches T. To distinguish the buyers who bid and the buyers who do not bid, we call all of the buyers who come to the GBA before T as the potential buyers and the buyers who bid in the auction as the bidders. It should be noted that only the potential buyers who come before the auction ends have the opportunity to bid because the auction may end before T. Although the number of potential buyers is independent of the price curve $P ,$ because the buyers bidding strategy is related to the price setting, the number of the bidders is related to the price level. N and $P$ are common knowledge. Only discrete bids are allowed, i.e., bidders can only bid $p _ { i } , i { \in } [ 1 , N ]$

According to the mechanism of the GBA, the number of the winners and the trading price in the GBA can be determine by Rule I, which is equivalent to Chen et. al. (2002)'s paper [4]:

Rule I: If the bidding vector is $B { = } ( b _ { 1 } , b _ { 2 } { , } { \ldots } , b _ { n } ) , n { \leq } N ,$ then the trading price is $p ( B ) = p _ { q } ,$ where $q =$ max $\begin{array} { r } { ( i | \sum _ { j = 1 } ^ { n } H ( b _ { j } – p _ { i } ) { \ge } i ) } \end{array}$ , and where H is the heavyside function, i.e.,

$$
H (x) = \left\{ \begin{array}{l l} 1 & \text { if } \quad x \geq 0 \\ 0 & \text { if } \quad x <   0 \end{array} \right.
$$

With the trading price $p _ { q } ,$ the bidders bidding higher than or equal to $p _ { q }$ will get the object and pay unit price $p _ { q } .$ Those who don't bid or bid lower than $p _ { q }$ will get nothing and pay nothing.

Rule I is illustrated in Fig. 1. Let the demand curve denote the number of bids bidding higher than or equal to the price. The demand curve and the price curve's right point of intersection, $K ( p , q )$ , denotes the trading price and the number of winners. In Fig. 1, $K \mathbf { \bar { s } }$ vertical coordinate, ${ , p , }$ is the trading price and horizontal coordinate, $^ { \textit { q } , }$ is the number of winners. The bidders bidding higher than or equal to $p$ will get one object with unit price $p$ each. The bidders bidding lower than $p$ will get nothing and pay nothing.

The FPM can be described as a special case of the GBA with the horizontal price curve, i.e., $P { = } ( p , . . . , p )$ . The bidders get the products when and only when they pay the unit price $p .$

## 3. Problem description

The GBA can be considered as a two-stage game model: the offer stage for the seller and the bidding stage for the bidders. The bidders' strategies in the bidding stage have been studied by Chen et al. [4], based on which our study emphasizes the seller's optimal strategy in the offer stage in various scenarios. The argument is based on the following assumptions.

Assumption 1. The independent private values model applies, i.e. each potential buyer gives the object a valuation, and the valuations are statistically independent.

![](/api/attachments/2P475FYW/fulltext/images/2a4fdb1525f413ef386b4800b05420612db7de9ba6dd771dfbb248a646d98ab7.jpg)  
Fig. 1. The trading price in the GBA.

Assumption 2. The potential buyers' valuations are in monetary units, and the potential buyers are risk neutral.

Assumption 3. The potential buyers are symmetric, i.e. all potential buyers draw their valuations from the same probability distribution. Let F(·) denote the cdf of the distribution and f (·) the pdf respectively.

Assumption 4. There is no collusion between potential buyers.

Assumption 5. The potential buyers' arrival times are statistically independent and have no correlation with their values to the object and bids.

Assumption 6. Each potential buyer's demand is 1. Segev et al. [20] point out that in online auction, approximately 76% of the purchases made were for one item.

Assumption 7. When a potential buyer decides not to bid, he silently “drops out” forever, i.e., he leaves the auction without record and never returns to it.

Assumption 8. The interval between the bidder's arrival and bidding is omitted, i.e., the arrival time equals the bidding time.

Assumption 9. The buyer chooses to buy the object when there is no difference between buying and not buying.

Assumption 10. The buyers are individual rational.

With these assumptions, Chen et al. [4] prove that strategy S is weakly dominant.

Strategy S: If a potential buyer's valuation of the object is, ν, then he bids $b { = } \theta ( \nu )$ , where

$$
\theta (v) \equiv \left\{ \begin{array}{l} p _ {1}, v \geq p _ {1} \\ p _ {j}, p _ {j - 1} > v \geq p _ {j}, j \in [ 2, N ] \\ 0, v <   p _ {N} \end{array} \right.\tag{1}
$$

Here bidding 0 means that the bidder doesn't bid and drops out forever. Strategy S implies that the bidder should drop out when his value is lower than the lowest price level $p _ { N } .$ . Otherwise, he should bid the price level which is just below his valuation to the object, ν.

Because strategy S is the buyers' weakly dominant strategy, it is rational for the bidders to take it. It is trivial that in the FPM, if a buyer's valuation of the object is no less than $p ,$ he will bid $p$ and get one object with payment $p .$ Otherwise he will not buy the object.

According to rule I and strategy S, the sold quantity $q ( V _ { n } , P )$ is

$$
q (V _ {n}, P) = \max (i | \sum_ {r = 1} ^ {n} H (\theta (v _ {r}) - p _ {i}) \geq i)\tag{2}
$$

where $V _ { n } { = } ( \nu _ { 1 } , \ \nu _ { 2 } { , } . . . , \ \nu _ { n } )$ denotes n potential buyers' valuations of the object, where $\nu _ { i }$ denotes potential buyer i's valuation, and the profit of the seller is $q ( V _ { n } , P )$ $( p _ { q ( V _ { n } , P ) } - c )$ , where $p _ { q ( V _ { n } , P ) }$ denotes the trading price.

In both the GBA and the FPM, the seller knows the buyers' arrival process distribution and their valuation distribution. The seller's objective is to set the optimal price curve P to maximize his utility. In different scenarios, the seller may have different utility functions, e.g., the expected profit, the expected profit with economies of scale, and the risk-seeking utility, which will be studied in the following sections.

## 4. The seller's expected profit

In this section, we suppose that the seller is riskneutral and his objective is to maximize the expected profit. If a seller sells k identical products at price $p ,$ and the unit cost is $c ,$ then his profit is $k ^ { * } ( p - c )$ . The seller faces a trade-off between losing a sale because of a high price and losing the customer's surplus because of a low price.

If there are n potential buyers, the seller's expected profit $\pi _ { n } ( P )$ is:

$$
\pi_ {n} (P) = \sum_ {r = 0} ^ {N} \operatorname * {P r} _ {q} (r, n, P) \cdot r \cdot (p _ {r} - c)\tag{3}
$$

where $\operatorname* { P r } _ { q } ( r , n , P )$ denotes the probability that there are r sold units with n potential buyers in the auction, $0 \leq r \leq N$

Lemma 1. Any given P, $n , ~ \exists p , ~ \pi _ { n } ~ ( L ( p , N ) ) \geq \pi _ { n } ( P )$ where $L ( p , k ) = ( p , p , \dotsc , p )$ denotes a k-dimensional {z<sub>k</sub> vector with k identical elements, p. vector with k identical elements, n

Lemma 1 shows that if the seller knows exactly how many potential buyers are in the auction, then the optimal price curve is horizontal. In traditional auctions, the number of bidders is open to the seller. Hence, this lemma implies that using the GBA in a traditional manner will not bring the seller more profit. However, in an online GBA, potential buyers come to the auction in a stochastic process. Hence, the seller does not know exactly how many buyers will come. In the GBA, according to the total probability formula, the sellers' expected profit is $\begin{array} { r } { \pi _ { T } ( P ) = \sum _ { n = 0 } ^ { \infty } \operatorname* { P r } _ { A } ( T , n ) \cdot \pi _ { n } ( P ) } \end{array}$ , where $\mathrm { P r } _ { A } ( { \cal T } ,$ <sup>p ð Þ ¼ ¼ ð Þ p ð Þ</sup>n)denotes the probability that there are n potential buyers in GBA with period T.

Table 1

Theorem 1. ∀ $P , ~ \pi _ { T } ( P ) \leq \pi _ { T } ( L ( p * , N ) )$ , where $p ^ { * } = \arg \operatorname* { m a x } _ { p } \pi _ { T } ( L ( p , N ) )$

Theorem 1 implies even when the potential buyers arrival process is stochastic and not known to the seller, the GBA cannot outperform the FPM either. Because the GBA can mimic an FPM by setting a horizontal price curve, the GBA is at least as good as the FPM. Hence, the optimal GBA and the optimal FPM are equivalent. Why can't the GBA utilize the discount to bring the seller more profit? According to Chen et al. [4], the GBA cannot motivate the bidders bidding higher. And also, according to Assumption 6, because the demand for each bidder is only one, the GBA cannot motivate the bidders bidding more. Can the GBA play as a price discrimination mechanism based on the number of bids? Because the GBA asks for a higher unit price when the market is worse (less sold quantity) and asks for a lower unit price when the market is better (more sold quantity), this mechanism cannot be an excellent price discrimination mechanism intuitively. It follows that if the website only considers maximizing its expected profit, it should not use a GBA, because it cannot bring more profit. It should be noted that if $c { = } 0$ , then this theorem implies that should the seller's objective be to maximize their revenue, the GBA is still not a good mechanism.

We now use a numerical example to illustrate the result that the discount of the GBA cannot bring the seller more profit than the FPM. Suppose that the bidders' arrival process is a Poisson one with arrival rate $\lambda = 1 / 3$ . The auction period is $T = 1 0 0$ . The quantity of available objects is $N { = } 4 0$ . The distribution of the bidders' valuations is a normal distribution with mean $\mu { = } 6$ and standard variance $\sigma = 2$ . The products' unit cost c is 0.

In the Poisson arrival process case, we have

$$
\begin{array}{l} \pi_ {T} (L (p, N)) \\ = p \left(N - e ^ {- \lambda T (1 - F (p))} \sum_ {k = 0} ^ {N - 1} \frac {(N - k) (\lambda T (1 - F (p))) ^ {k}}{k !}\right) \end{array}\tag{4}
$$

By solving

$$
\begin{array}{l} \frac {\partial \pi_ {T} (L (p , N))}{\partial p} \\ = N \cdot \biggl (1 - \frac {\Gamma (N + 1 , (1 - F (p)) \lambda T)}{\Gamma (N + 1)} \biggr) \\ \quad + \frac {\lambda T (\Gamma (N , (1 - F (p)) \lambda T)}{\Gamma (N)} (1 - F (p) - p \cdot f (p)) = 0, \end{array}\tag{5}
$$

Comparison of expected revenues under the different price curves

<table><tr><td> $k^{\text{th}}$  Element in price curve  $P (1 \leq k \leq N)$ </td><td>Expected revenue</td></tr><tr><td> $p_{k}=p^{*}=4.67$ </td><td>116.4</td></tr><tr><td> $p_{k}=4.67-0.05 \cdot (k-1)$ </td><td>95.8</td></tr><tr><td> $p_{k}=5.6-0.1 \cdot (k-1)$ </td><td>76.8</td></tr><tr><td> $p_{k}=5.6-0.02 \cdot (k-1)$ </td><td>113.7</td></tr><tr><td> $p_{k}=4.67-0.05 \cdot (k-1)^{1.1}$ </td><td>77.1</td></tr><tr><td> $p_{k}=5.8-0.1 \cdot (k-1)^{1.1}$ </td><td>42.28</td></tr><tr><td> $p_{k}=5.8-0.02 \cdot (k-1)^{1.1}$ </td><td>96.2</td></tr><tr><td> $p_{k}=4.94-0.05 \cdot (k-1)^{0.9}$ </td><td>92.4</td></tr><tr><td> $p_{k}=5.5-0.1 \cdot (k-1)^{0.9}$ </td><td>87.2</td></tr><tr><td> $p_{k}=5.5-0.02 \cdot (k-1)^{0.9}$ </td><td>96.3</td></tr></table>

where $\begin{array} { r } { T ( n , z ) = \int _ { z } ^ { + \infty } t ^ { n - 1 } e ^ { - t } \mathrm { d } t , T ( n ) = \int _ { 0 } ^ { + \infty } t ^ { n - 1 } e ^ { - t } \mathrm { d } t , } \end{array}$ we can get that $p ^ { * } { = } 4 . 6 7 4 3 7$

Table 1 shows that although different families of price curves lead to different revenues for the seller, none of them outmatch the optimal price level $q ^ { * } .$ . This result confirms Theorem 1, i.e. under the assumptions the optimal price curve is horizontal in the GBA.

This conclusion may partly explain why some websites with the GBA failed in the B2C e-market. Products commonly sold in this market are CDs, cameras, and other electronic products, the cost structures of which are similar to this model. Hence, those websites that use the GBA with a positive discount rate can hardly outperform their competitors.

Coordination plays an important role in the supply chain management, where the sellers, called the retailer in the Cachon et al.'s paper [3], may face different profit functions [3].

We suppose that if there are r sold units, where $0 \leq r \leq N$ the seller's profit is

$$
\pi_ {r} (r, p _ {r}) = r (\alpha p _ {r} - \beta c _ {v}) - \eta c _ {f}\tag{6}
$$

where $c _ { f }$ is the fixed cost, $c _ { \nu }$ is the variable cost and $\alpha , \beta ,$ and $\eta \in [ 0 , 1 ]$ are the divison ratio of the unit revenue, variable cost, and fixed cost respectively for the seller. For example, α implies the division ratio of the unit revenue between the seller and his upstream supplier is $\alpha { : } ( 1 - \alpha )$

The seller's expected profit with this kind of linear profit function is

$$
\pi_ {c} (P) = \sum_ {n = 0} ^ {\infty} \operatorname * {P r} _ {A} (T, n) \sum_ {r = 0} ^ {N} \operatorname * {P r} _ {q} (r, n, P) \cdot r \cdot (\alpha p _ {r} - \beta c) - \eta c _ {f}\tag{7}
$$

This profit function can describe the profit of the sellers in many typic supply chain contracts.

For example, in revenue-sharing contract, the seller's profit can be expressed as

$$
\begin{array}{l} \pi (P) = \phi (S (N, P) \cdot (p _ {S (N, P)})) - (c _ {R} + w) \cdot N \\ = \sum_ {n = 0} ^ {\infty} \operatorname * {P r} _ {A} (T, n) \sum_ {r = 0} ^ {N} \operatorname * {P r} _ {q} (r, n, P) \cdot r \cdot \phi p _ {r} \\ - (c _ {R} + w) \cdot N \end{array}\tag{8}
$$

where $0 \leq \varphi \leq 1$ is the seller's share of revenue, S(N, P) <sup>u</sup>is the sold quantity with price vector P and total order quantity $N , c _ { R }$ is the unit cost for the seller and w is the wholesale price. Suppose the order quantity N is determined before selling, the order cost is fixed when determine the optimal price vector.

If we set $\begin{array} { r } { \dot { { \alpha } } = \phi , \dot { \beta } = 0 , \eta = \frac { ( c _ { R } + w ) N } { c _ { c } } , } \end{array}$ which implies that the seller will get share of the revenue and pay the <sup>u</sup>fixed cost caused in the selling side, i.e., $( c _ { R } + w ) N ,$ Eq. (7) is the same as Eq. (8), which implies that the revenue-sharing contract is a special case of the contract considered in the form of Eq. (6).

Theorem 2. ∀P, $\pi _ { C } \left( P \right) \leq \pi _ { C } \left( L ( p ^ { * } , N ) \right)$ , where $p ^ { * }$ is the optimal fixed price when contract (in the form of Eq. (6)) is considered.

Theorem 2 extends the result of Theorem 1. With Theorem 2, it is sufficient to say that the GBA cannot outperform the FPM with linear profit function. Hence, with the supply chain coordination, if the sellers face this kind of linear profit function, (e.g., revenue sharing contracts, buy back contracts,) they should not use the GBA as a pricing mechanism.

## 5. The GBA in other scenarios

## 5.1. Scenario 1: economies of scale

Demand aggregation is at the core of the GBA. By bringing together as many bidders as possible, websites can negotiate lower prices with merchant partners or manufacturers (e.g., Letsbuyit.com, Ewinwin.com). For GBA websites, more sold units imply less unit cost, i.e., economies of scale are important. In this section we introduce the economies of scale into our model when we compare the GBA with the FPM. Here we use the all units quantity discounts schedule model. Suppose that a seller's utility function is $\pi ( r , p _ { r } ) =$ $r ( p _ { r } { - } c _ { r } )$ , where r is the number of the sold units, $p _ { r }$ is the final trading price, and $c _ { r }$ is the unit cost when the volume is $r .$

For simplification, we only consider the price curve with two price levels and assume that the supply can always fulfill the demand. Suppose that the bidders arrival process is a Poisson process with arrival rate λ. The price curve is $P = ( \underbrace { p _ { 1 } , \dots , p _ { 1 } } _ { l } , p _ { 2 } , p _ { 2 } , \dots . )$ . The cost function is $C = \left( c _ { 1 } , c _ { 2 } , l \right)$ , where $c _ { 1 } > c _ { 2 }$ are the cost levels and l is threshold to get the economies of scale. That is if the sold units are less than or equal to l, the unit cost is $c _ { 1 } ;$ if the sold units are more than l, the economies of scale are achieved and the unit cost for all products is c .

The seller's expected profit with economies of scale is

$$
\begin{array}{l} \pi_ {G, E} (P) = \sum_ {k = 0} ^ {l} \frac {(\lambda T) ^ {k} e ^ {- \lambda T}}{k !} \cdot (\sum_ {y = 0} ^ {k} \sum_ {x = 0} ^ {y} z p (k, x, y) \\ \times (x \cdot (p _ {1} - c _ {1}))) + \sum_ {k = l + 1} ^ {+ \infty} \frac {(\lambda T) ^ {k} e ^ {- \lambda T}}{k !} \\ \times (\sum_ {y = 0} ^ {l} \sum_ {x = 0} ^ {y} z p (k, x, y) (x \cdot (p _ {1} - c _ {1}))) \\ + \sum_ {k = l + 1} ^ {+ \infty} \frac {(\lambda T) ^ {k} e ^ {- \lambda T}}{k !} \\ \times (\sum_ {y = l + 1} ^ {k} \sum_ {x = 0} ^ {y} z p (k, x, y) (y \cdot (p _ {2} - c _ {2}))) \end{array}\tag{9}
$$

where

$$
z p (k, x, y) = \frac {k ! (1 - F (p _ {1})) ^ {x} (F (p _ {1}) - F (p _ {2})) ^ {y - x} F (p _ {2}) ^ {k - y}}{x ! (y - x) ! (k - y) !}
$$

With some algebraic transactions, the expected profit can be formulated as follows,

$$
\begin{array}{l} \pi_ {G, E} (P) = \lambda T (1 - F (p _ {1})) (p _ {1} - c _ {1}) \cdot w (p _ {2}) \\ \qquad + \lambda T (1 - F (p _ {2})) (p _ {2} - c _ {2}) (1 - w (p _ {2})) \end{array}\tag{10}
$$

where $w ( p ) { = } T ( l , \ \lambda T ( 1 - F ( p ) ) ) / \varGamma ( l ) { \in } ( 0 , 1 ) )$ and $\begin{array} { r } { \Gamma ( n , z ) = \int _ { z } ^ { + \infty } t ^ { n - 1 } e ^ { - t } \mathrm { d } t , { \Gamma ( n ) } = \int _ { 0 } ^ { + \infty } t ^ { n - 1 } e ^ { - t } \mathrm { d } t . } \end{array}$

<sup>Þ ¼ Cð Þ ¼</sup>If the seller posts a fixed price, p instead, it can be deduced from Eq. (4) that the seller's expected profit is

$$
\begin{array}{c} \pi_ {F, E} (p) = \lambda T (1 - F (p)) (p - c _ {1}) \cdot w (p) \\ + \lambda T (1 - F (p)) (p - c _ {2}) (1 - w (p)) \end{array}\tag{11}
$$

By optimizing Eqs. (5) and (6), we get the optimal GBA price curve and the optimal FPM, with which we can compare the expected profit of the GBA and that of the FPM.

Theorem 3. max $\pi _ { G , E } ( P ) { > } \operatorname* { m a x } _ { p } \pi _ { F , E } ( p )$ P

Theorem 3's implication is interesting. Different from the former scenario without economies of scale, the GBA now strictly outperforms the FPM. This means that economies of scale are important for GBA websites. Because the GBA automatically asks for a higher price when the unit cost is higher and a lower one when the unit cost is lower, it can outperform the fixed mechanism intuitively.

To illustrate this result, we provide a numerical example. Suppose that the potential buyers' arrival process is a Poisson process with λ = 10; their valuations are drawn from the same uniform distribution in interval [0,1], T=7, l=10, 20, 30, ${ c _ { 1 } } \mathrm { { = } } 0 . 8 _ { \mathrm { { i } } }$ , and $c _ { 2 } = 0 . 7 , \ 0 . 6 ,$ respectively. With Mathematica 4.0, by searching the maximal point in Eqs. (10) and (11) with the above parameters, we get the optimal price and maximal profit, which are shown in Table 2.

As these numbers suggest, the GBA outperforms the FPM when we consider economies of scale, which confirms Theorem 3. And also we can clearly observe that the improvement of the seller's profitability in the GBA depends on the expected demand (λT) and the threshold (l). Comparing to the expected demand, a too long or too short threshold provides a less improvement than do the medium one. Because the GBA outperforms the FPM through its adaptability, i.e., the GBA automatically asks for a higher price when the unit cost is higher and a lower one when the unit cost is lower. A too long or too short threshold implies the uncertainty of the unit cost is low, i.e., we are clear if we can use the economies of scale or not. A medium threshold implies the uncertainty of the unit cost is high, i.e., we don't know if we can use the economies of scale or not before the sales realized. Hence, in this scenario, the adaptability of the GBA values higher.

Comparison of GBA and FPM with economies of scale

<table><tr><td> $c_{2}$ </td><td> $p_{1}^{*}, p_{2}^{*}$ </td><td> $\pi_{G,E}$ </td><td> $p^{*}$ </td><td> $\pi_{F,E}$ </td></tr><tr><td> $l=10$ </td><td></td><td></td><td></td><td></td></tr><tr><td>0.7</td><td>0.900, 0.817</td><td>1.356</td><td>0.815</td><td>1.270</td></tr><tr><td>0.6</td><td>0.900, 0.775</td><td>2.656</td><td>0.771</td><td>2.604</td></tr><tr><td> $l=20$ </td><td></td><td></td><td></td><td></td></tr><tr><td>0.7</td><td>0.900, 0.770</td><td>0.783</td><td>0.900</td><td>0.700</td></tr><tr><td>0.6</td><td>0.900, 0.702</td><td>1.562</td><td>0.900</td><td>0.700</td></tr><tr><td> $l=30$ </td><td></td><td></td><td></td><td></td></tr><tr><td>0.7</td><td>0.900, 0.754</td><td>0.701</td><td>0.900</td><td>0.700</td></tr><tr><td>0.6</td><td>0.900, 0.662</td><td>0.790</td><td>0.900</td><td>0.700</td></tr></table>

If the seller can obtain volume discount from the supplier, then the seller should choose the GBA as the pricing mechanism because this choice will bring more profit. However, as Kauffman and Wang [15] shows, many GBA websites in B2C markets cannot achieve the critical mass, i.e. which implies that the threshold is too long for the demand, which ultimately induces their failure. To solve this problem, trying to attract more consumers in different regions through the Internet is an effective way for sellers to expand their consumer groups. And it is also a good idea to sign with the supplier some contract through which the GBA websites can get the discount with a small threshold.

## 5.2. Scenario 2: risk seeking seller

Another focus of the networked economy is riskseeking. The players' different risk attitudes play an important role on the application of the auction. In the expanding E-business environment, there exists a fairly large group of risk-seeking persons, who believe that no venture no gain. As Gourville [8] points out, especially for the sellers of the new products, gains have a greater impact on them than similarly sized losses. Hence, though they may not have sufficient sale scale in the past, they still take a risk and hope to get it at some point in the future. Quadratic utility function is popular used in the literatures to study different risk attitudes [12]. In this paper, we also use a simple quadratic utility function to model the riskseeking sellers, where we assume that the seller's utility function is $r ^ { 2 } p _ { r }$ instead of the revenue being $r p _ { r }$ where r is the number of sold units and $p _ { r }$ is the trading price. We only consider the two-level price curve and suppose that the supply always fulfills the demand. We also suppose that the bidders' arrival process is a Poisson process with arrival rate $\lambda .$ . Hence, the utility of the seller in GBA with price curve $P = ( \underbrace { p _ { 1 } , \ldots , p _ { 1 } } _ { l } , p _ { 2 } , p _ { 2 } , \ldots )$ is

$$
\begin{array}{l} \pi_ {G, R} (P) = \sum_ {k = 1} ^ {+ \infty} \sum_ {z = 1} ^ {k} \sum_ {y = 1} ^ {z} \frac {(\lambda T) ^ {k} e ^ {- \lambda T}}{k !} \\ \times \frac {k ! (1 - F (p _ {1})) ^ {y} (F (p _ {1}) - F (p _ {2})) ^ {z - y} F (p _ {2}) ^ {k - z}}{y ! (z - y) ! (k - z) !} y ^ {2} p _ {1} \\ - \sum_ {k = 1} ^ {+ \infty} \sum_ {z = l + 1} ^ {k} \sum_ {y = 1} ^ {z} \frac {(\lambda T) ^ {k} e ^ {- \lambda T}}{k !} \\ \times \frac {k ! (1 - F (p _ {1})) ^ {y} (F (p _ {1}) - F (p _ {2})) ^ {z - y} F (p _ {2}) ^ {k - z}}{\textit {y ! (z - y) ! (k - z) !}} y ^ {2} p _ {1} \\ + \sum_ {z = l + 1} ^ {+ \infty} \frac {(\lambda T) ^ {z} (1 - F (p _ {2})) ^ {z}}{z !} e ^ {- \lambda T (1 - F (p _ {2}))} z ^ {2} p _ {2} \end{array} \tag {12}\tag{12}
$$

With some algebraic transactions, the expected utility is formulated as,

$$
\begin{array}{l} \pi_ {G, R} (P) = (h _ {2} ^ {2} + h _ {2}) p _ {2} \\ \qquad + (h _ {1} ^ {2} p _ {1} - h _ {2} ^ {2} p _ {2}) \frac {\Gamma (l - 1 , h _ {2})}{\Gamma (l - 1)} \\ \qquad + (h _ {1} p _ {1} - h _ {2} p _ {2}) \frac {\Gamma (l , h _ {2})}{\Gamma (l)}, \end{array}\tag{13}
$$

where $h _ { i } \equiv \lambda t ( 1 - P ( q _ { i } ) ) , i = 1$ , 2

When the seller uses the FPM, the expected utility is

$$
\pi_ {F, R} (p) = \lambda t (1 - F (p)) \cdot (\lambda t (1 - F (p)) + 1) \cdot p\tag{14}
$$

where $p$ is the fixed price.

With these formulae, we can now compare the expected utility of the GBA and that of the FPM. Let $P { * } { \in } { \arg \operatorname* { m a x } } _ { P } \pi _ { G , R } ( P )$

Theorem 4. For the optimal price curve $P ^ { * } =$ $\big ( \underbrace { p _ { 1 } ^ { * } , \ldots , p _ { 1 } ^ { * } } _ { l } p _ { 2 } ^ { * } , p _ { 2 } ^ { * } , \ldots . \big )$ , where $l { > } 0 , p _ { I } ^ { * } { > } p _ { 2 } ^ { * }$

Theorem 4 implies that for the risk-seeking sellers, the optimal price curve in the GBA is no longer horizontal. Because the GBA can mimic the FPM by setting a horizontal price curve, this theorem also infers that the optimal GBA will outperform the FPM for the risk-seeking sellers. Because the optimal price mechanism is to find out the best tradeoff between the sold quantity and the unit price and comparing with the risk neutral sellers, in the marginal utility point of view, the risk-seeking one weighs more and more on selling one more product than on getting a higher unit price (the power 2 on r in the objective function $r ^ { 2 } { \bar { p } } _ { r }$ shows a heavier weight on r when r becomes larger.). The GBA automatically adjusts the tradeoff between the sold quantity and unit price that can definitely benefit the seller. Different from the economies of scale case where exists an exogenous threshold l to get the discount, here, l is endogenetic, yet how to set a suitable l in the optimal GBA is our future work.

## 6. Conclusions and future studies

In this paper, we study the GBA mechanism in three scenarios. First we consider the seller's expected profit when he is risk-neutral. By comparing the GBA with the FPM, we find that the optimal GBA is equivalent to the optimal FPM. This result also applies to the seller with linear profit division contracts with his suppliers. Second, we introduce economies of scale into our model, and find that the GBA will outperform the FPM in this scenario. This result implies that GBA is more suitable for selling the goods that produce a learning effect; it also infers that there is a critical mass for the GBA. If the GBA websites can never achieve a critical mass of units sold no matter the market is good or bad, then they can hardly outperform their competitors. Finally, we consider the GBA in the e-economy context, where do exist a large amount of risk seeking sellers. We find that the GBA outperforms the FPM in this scenario, which implies that the GBA is a suitable mechanism in the expanding E-business environment, where the seller is riskseeking.

There is still much work to do. It has been pointed out that the GBA, in contrast to the ordinary sale mechanism, can attract buyers with different objectives [7]. Because these buyers may take different actions, asymmetric buyers will have to be considered. This paper models the GBA in the B2C markets, where the individual consumers buy the products for their own use. When we want to extend the GBA to the B2B world, we should pay more attention to the common value model or an affiliate value model [18]. And also, as we point out, achieving more consumers is a key factor for the GBA websites to get the discount from the supplier. Collusion, cooperation of the buyers, may make the existing consumers to invite more friends to join the GBA. Hence considering the cooperation in the GBA is useful. Almost all auction forms are susceptible to collusion, but degrees of incentives vary [10] and collusion may heavily affect the efficiency of the auction [17]. Because the GBA may use collusion to attract more consumers and more participants benefit the seller and the buyers both, introducing collusion to the GBA may lead to some interesting results.

## Acknowledgments

This work was supported in part by the National Science Foundation of China under Grant No. 70321001, NSFC/RCG Joint Research Grant 79910161987.

## Appendix A. Proof of lemma 1

Before proving this lemma, we need first prove some lemmas and a corollary for technical reasons. Notation. $I I ( V _ { n } , P ) \equiv q ( V _ { n } , P ) \cdot ( p _ { q ( V _ { n } , P ) } - \mathbf { c } )$ , which denotes the seller's profit when the price curve P and n potential buyers' valuations $V _ { n }$ are given.

Lemma A1. For any given n and any price curve $P = ( \underbrace { p _ { k - 1 } , p _ { k - 1 } , \dots , p _ { k - 1 } } _ { k - 1 } , p _ { k } , \dots , p _ { N } ) , l e t P ^ { \prime } = ( \underbrace { p _ { k } , p _ { k } , \dots , p _ { k } } _ { k } , p _ { k + 1 } , \dots ,$ $p _ { N } ) \ , \ i f \pi _ { u } ( p _ { b } c ) { \geq } \pi _ { u } ( p _ { k - l } , c ) ,$ , where $\pi _ { u } ( p , c ) = ( I - F ( p ) ) ( p - c )$ denotes the >unit expected profit, then $\pi _ { n } ( P ^ { \prime } ) { \geq } \pi _ { n } ( P )$

Let us discuss the cases according to $r , r { = } q ( V _ { n } , P ^ { \prime } )$

C1) In the case that $r \in [ 0 , k )$ : because $p _ { k - 1 } \geq p _ { k } ,$ , it follows that $q ( V _ { n } , P ) { = } j { \leq } r .$

$$
\begin{array}{l} \operatorname * {P r} (q (V _ {n}, P) = j | q (V _ {n}, P ^ {\prime}) = r) = \frac {C _ {r} ^ {j} \cdot (1 - F (p _ {k - 1})) ^ {j} \cdot (F (p _ {k - 1}) - F (p _ {k})) ^ {r - j}}{(1 - F (p _ {k})) ^ {r}} \\ E (\Pi (V _ {n}, P) | q (V _ {n}, P ^ {\prime}) = r) = \sum_ {i = 1} ^ {r} i \cdot (p _ {k - 1} - c) \cdot \operatorname * {P r} (q (V _ {n}, P) = i | q (V _ {n}, P ^ {\prime}) = r) \\ = \frac {(p _ {k - 1} - c) \cdot (\sum_ {i = 0} ^ {r} i \cdot C _ {r} ^ {i} \cdot (1 - F (p _ {k - 1})) ^ {i} \cdot (F (p _ {k - 1}) - F (p _ {k}))) ^ {r - j}}{(1 - F (p _ {k})) ^ {r}} = \frac {(p _ {k - 1} - c) \cdot r \cdot (1 - F (p _ {k - 1}))}{1 - F (p _ {k})} \end{array}
$$

$$
\text { So } \frac {E (\Pi (V _ {n} , P) | q (V _ {n} , P ^ {\prime}) = r)}{E (\Pi (V _ {n} , P ^ {\prime}) | q (V _ {n} , P ^ {\prime}) = r)} = \frac {\pi_ {u} (p _ {k - 1} , c)}{\pi_ {u} (p _ {k} , c)} \leq 1
$$

Hence, $E ( \Pi ( V _ { n } , P ) | q ( V _ { n } , P ^ { \prime } ) = r ) \le E ( \Pi ( V _ { n } , P ^ { \prime } ) | q ( V _ { n } , P ^ { \prime } ) = r ) , r \in [ 0 , k )$

C2) In the case that $r \geq k :$ With the definition of $q ( { \bf \dot { \theta } } ) , q ( V _ { n } , P ) = r .$

$$
E (\Pi (V _ {n}, P) | q (V _ {n}, P ^ {\prime}) = r) \leq E (\Pi (V _ {n}, P ^ {\prime}) | q (V _ {n}, P ^ {\prime}) = r), r \geq k
$$

Integrating C1) and C2),

$$
\begin{array}{l} \pi_ {n} (P ^ {\prime}) = \sum_ {r = 0} ^ {N} \operatorname * {P r} (q (V _ {n}, P ^ {\prime}) = r) \cdot E (\Pi (V _ {n}, P ^ {\prime}) | q (V _ {n}, P ^ {\prime}) = r) \geq \sum_ {r = 0} ^ {N} \operatorname * {P r} (q (V _ {n}, P ^ {\prime}) = r) \cdot E (\Pi (V _ {n}, P) | q (V _ {n}, P ^ {\prime}) \\ = r) = \pi_ {n} (P). \end{array}
$$

Lemma A2. For any given n and price curve $P = ( \underbrace { p _ { k - 1 } , p _ { k - 1 } , \dots , p _ { k - 1 } } _ { k - 1 } , p _ { k } , \dots , p _ { N } ) , k { < } N , l e t P ^ { \prime } = ( \underbrace { p _ { k - 1 } , p _ { k - 1 } , \dots , p _ { k - 1 } } _ { k } ,$

$$
\left. p _ {k + 1}, \dots , p _ {N}\right), i f \pi_ {u} \left(p _ {k}, c\right) <   \pi_ {u} \left(p _ {k - 1}, c\right), t h e n \pi_ {n} \left(P ^ {\prime}\right) > \pi_ {n} (P).
$$

Proof. Let us discuss the cases according to $r , r { = } q ( V _ { n } , P )$

C1) In the case that $r \in [ 0 , k )$

Because the price elements in $P ^ { \prime }$ are not lower than those in $P , r { \geq } q ( V _ { n } , P ^ { \prime } )$

With Rule I, there are r bidders whose values are not lower than $q _ { k - 1 } ,$ , which implies that $q ( V _ { n } , P ^ { \prime } ) \geq r .$ Thus, $q ( V _ { n } , P ) { = } r { = } q ( V _ { n } , P ^ { \prime } )$

Hence, $E ( \varPi ( V _ { n } , P ) | q ( V _ { n } , P ) { = } r ) \leq E ( \varPi ( V _ { n } , P ^ { \prime } ) | q ( V _ { n } , P ) { = } r ) .$

C2) In the case that $r { = } k ;$

$$
\operatorname * {P r} (q (V _ {n}, P ^ {\prime}) = j | q (V _ {n}, P) = r) = \frac {C _ {r} ^ {j} \cdot (1 - F (p _ {k - 1})) ^ {j} \cdot (F (p _ {k - 1}) - F (p _ {k})) ^ {r - j}}{(1 - F (p _ {k})) ^ {r}}.
$$

$$
\begin{array}{l} E (\Pi (V _ {n}, P ^ {\prime}) | q (V _ {n}, P) = r) = \sum_ {j = 0} ^ {r} j \cdot p _ {k - 1} \cdot \operatorname * {P r} (q (V _ {n}, P ^ {\prime}) = j | q (V _ {n}, P) = r) \\ = \frac {(p _ {k - 1} - c) \cdot (\sum_ {j = 0} ^ {r} j \cdot C _ {r} ^ {j} \cdot (1 - F (p _ {k - 1})) ^ {j} \cdot (F (p _ {k - 1}) - F (p _ {k})) ^ {r - j}}{(1 - F (p _ {k})) ^ {r}} = \frac {(p _ {k - 1} - c) \cdot r \cdot (1 - F (p _ {k - 1}))}{(1 - F (p _ {k}))}. \end{array}
$$

It follows that $\frac { E ( \Pi ( V _ { n } , P ) | q ( V _ { n } , P ) = r ) } { E ( \Pi ( V _ { n } , P ^ { \prime } ) | q ( V _ { n } , P ) = r ) } = \frac { \pi _ { u } ( p _ { k } , c ) } { \pi _ { u } ( p _ { k - 1 } , c ) } < 1$

Hence, $E ( \varPi ( V _ { n } , P ^ { \prime } ) | q ( V _ { n } , P ) { = } r ) { > } E ( \varPi ( V _ { n } , P ) | q ( V _ { n } , P ) { = } r ) .$

C3) In the case that r <sup>N</sup> k: with the definition of q(<sup>·</sup>), q(V<sub>n</sub>, P′) = q(V<sub>n</sub>, P) = r.

Hence $E ( \varPi ( V _ { n } , P ^ { \prime } ) | q ( V _ { n } , P ) { = } r ) { = } E ( \varPi ( V _ { n } , P ) | q ( V _ { n } , P ) { = } r ) .$

Integrating C1), C2) and C3), with total probability formula,

$$
\begin{array}{l} \pi_ {n} (P ^ {\prime}) = \sum_ {r = 0} ^ {N} \operatorname * {P r} (q (V _ {n}, P) = r) \cdot E (\Pi (V _ {n}, P ^ {\prime}) | q (V _ {n}, P) = r) \\ \qquad \qquad \qquad \geq \sum_ {r = 0} ^ {N} \operatorname * {P r} (q (V _ {n}, P) = r) \cdot E (\Pi (V _ {n}, P) | q (V _ {n}, P) = r) = \pi_ {n} (P). \end{array}
$$

Corollary A1. For any given n and price curve P, let $B = ( \underbrace { p _ { x _ { N - 1 } } , \ldots , p _ { x _ { N - 1 } } } _ { N - 1 } , p _ { N } )$ , where $p _ { x _ { N - 1 } } { \in } \mathrm { a r g } \operatorname* { m a x } _ { p _ { j } }$ $( \pi _ { u } ( p _ { j } , c ) ) , 1 { \le } j { \le } N { - } 1 , \pi _ { n } ( P ) { \le } \pi _ { n } ( B )$

Proof.. Lemmas A1 and A2 imply $\forall k { < } N , \ \pi _ { n } ( P ) { \leq } E _ { n } ( P ^ { \prime } )$ , where $P = ( \underbrace { p _ { k - 1 } , p _ { k - 1 } , \ldots , p _ { k - 1 } } _ { k - 1 } , p _ { k } , \ldots , p _ { N } )$ and $P ^ { \prime } =$ $( \underbrace { p _ { x } , p _ { x } , \ldots , p _ { x } } _ { k } , \underbrace { p _ { k + 1 } , \ldots , p _ { N } } )$ with xaarg max $( \pi _ { u } ~ ( p _ { j } , c ) ) , j = k$ or $k - 1$ . It follows that

$$
\pi_ {n} (P) \leq \pi_ {n} ((\underbrace {p _ {x _ {2}} , p _ {x _ {2}}} _ {2}, \ldots , p _ {N})) \leq \pi_ {n} ((\underbrace {p _ {x _ {3}} , p _ {x _ {3}} , p _ {x _ {3}}} _ {3}, \ldots , p _ {N})) \leq \ldots \leq \pi_ {n} ((\underbrace {p _ {x _ {N - 1}} , \ldots , p _ {x _ {N - 1}}} _ {N - 1}, p _ {N})) = \pi_ {n} (B),
$$

Where $p _ { x _ { N - 1 } } \in \arg \operatorname* { m a x } _ { p _ { j } } ( \pi _ { u } ( p _ { j } , c ) ) , 1 { \leq } j { \leq } N \mathrm { - 1 }$

Lemma A3.<sup>.</sup> For any given n and price curve $B = ( \underbrace { p _ { N - 1 } , \ldots , p _ { N - 1 } } _ { N - 1 } , p _ { N } ) , i f \pi u ( p ^ { N } , c ) < \pi u ( p ^ { N - I } , c ) , l e t B ^ { \prime } = L ( p ^ { N - I } , N ) ,$ πn $( B ^ { \prime } ) { \geq } \pi ^ { n } \left( B \right)$

Proof. Let us discuss the cases according to $r , r { = } q ( V _ { n } , B )$

C1) In the case that $r \in [ 0 , N )$ , similar with Lemma A2 C1).

$$
E (\Pi (V _ {n}, B ^ {\prime}) | q (V _ {n}, B) = r) = E (\Pi (V _ {n}, B) | q (V _ {n}, B) = r)
$$

C2) In the case that $r { = } N ;$

This implies that there are at least N potential buyers who value the objects at no less than $q _ { N } .$ Because the price elements in $B ^ { \prime }$ are not lower than those in $B , q ( V _ { n } , B ^ { \prime } ) \leq q ( V _ { n } , B )$

Suppose that there are $i ( i \geq N )$ potential buyers who value the objects at no less than $q _ { N } ,$ , which is denoted by $\mathrm { A R } = i ,$ then

$$
\begin{array}{l} E (\Pi (V _ {n}, B ^ {\prime}) | \mathrm{AR} = i) = \sum_ {j = 0} ^ {N - 1} \operatorname * {P r} \{q (V _ {n}, B ^ {\prime})) = j | \mathrm{AR} = i \} \cdot j \cdot (p _ {N - 1} - c) + \operatorname * {P r} \{q (V _ {n}, B ^ {\prime}) = N | \mathrm{AR} = i \} \\ \times N \cdot (p _ {N - 1} - c) = \frac {\sum_ {j = 0} ^ {N - 1} j \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \\ + \frac {\sum_ {j = N} ^ {i} N \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \end{array}
$$

$$
\begin{array}{l} \sum_ {j = k} ^ {i} (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j} \\ \text { i) If } \exists k \in [ N, i ], \frac {(1 - F (p _ {N})) ^ {i}}{(1 - F (p _ {N})) ^ {i}} > (p _ {N} - c), \text { then } \\ \frac {\sum_ {j = k} ^ {i} N \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} > N \cdot (p _ {N} - c). \end{array}
$$

Hence, $E ( \varPi ( V _ { n } , B ^ { \prime } ) | \mathrm { A R } = i )$

$$
\begin{array}{l} = \frac {\sum_ {j = 0} ^ {N - 1} j \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} + \frac {\sum_ {j = N} ^ {k - 1} N \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \\ + \frac {\sum_ {j = k} ^ {i} N \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} > \frac {\sum_ {j = k} ^ {i} N \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \\ > N \cdot (p _ {N} - c) = E (\Pi (V _ {n}, B) | \mathrm{AR} = i). \\ \text {ii)} \text {If} \forall k \in [ N, i ], \frac {\sum_ {j = k} ^ {i} (p _ {N - 1} - c) \cdot C _ {i} ^ {j} (1 - F (p _ {N - 1})) ^ {j} (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \leq p _ {N} - c, \text {then} \\ \sum_ {k = N + 1} ^ {i} \sum_ {j = k} ^ {i} \frac {(p _ {N - 1} - c) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \leq (i - N) \cdot (p _ {N} - c). \end{array}
$$

Because

$$
\begin{array}{l} \sum_ {k = N + 1} ^ {i} \sum_ {j = k} ^ {i} \frac {(p _ {N - 1} - c) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \\ = \sum_ {j = N + 1} ^ {i} \frac {(p _ {N - 1} - c) \cdot (j - N) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}}, \end{array}
$$

Hence,

$$
\begin{array}{l} \sum_ {j = N + 1} ^ {i} \frac {(p _ {N - 1} - c) \cdot (j - N) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} \leq (i - N) \cdot (p _ {N} - c) \\ \text { As } \frac {\sum_ {j = 0} ^ {i} j \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} = \frac {i \cdot (p _ {N - 1} - c) \cdot (1 - F (p _ {N - 1}))}{(1 - F (p _ {N - 1}))} \text { and } \end{array}\tag{A1}
$$

$$
\pi_ {u} (p _ {N - 1}, c) = (p _ {N - 1} - c) (1 - F (p _ {N - 1})) \geq (p _ {N} - c) (1 - F (p _ {N})) = \pi_ {u} (p _ {N}, c),
$$

$$
\frac {\sum_ {j = 0} ^ {i} j \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}} > i \cdot (p _ {N} - c)\tag{A2}
$$

With in Eqs. (A1) and (A2), it can be deducted that

$$
\frac {\sum_ {j = 1} ^ {N} j \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j} + \sum_ {j = N + 1} ^ {i} N \cdot (p _ {N - 1} - c) \cdot C _ {i} ^ {j} \cdot (1 - F (p _ {N - 1})) ^ {j} \cdot (F (p _ {N - 1}) - F (p _ {N})) ^ {i - j}}{(1 - F (p _ {N})) ^ {i}}
$$

$$
> N \cdot (p _ {N} - c)
$$

i.e., $E ( \varPi ( V _ { n } , B ^ { \prime } ) \vert \mathrm { A R } = i ) > E ( \varPi ( V _ { n } , B ) \vert \mathrm { A R } = i ) .$

Thus, in both cases

$$
E (\Pi (V _ {n}, B ^ {\prime}) | \mathrm{AR} = i) > E (\Pi (V _ {n}, B) | \mathrm{AR} = i),
$$

Because $q ( V _ { n } , B ) { = } N$ if and only $\mathrm { i f } \exists i \geq N ,$ s.t. $\mathrm { A R } = i ,$

$$
\begin{array}{l} E (\Pi (V _ {n}, B ^ {\prime}) | q (V _ {n}, B) = N) = \sum_ {i = N} ^ {+ \infty} \operatorname * {P r} \frac {\{\mathrm{AR} = i \} E (q (V _ {n} , L (p _ {N - 1} , N)) | \mathrm{AR} = i)}{\operatorname * {P r} \{q (V _ {n} , B) = N \}} \\ \geq \frac {\sum_ {i = N} ^ {+ \infty} \operatorname * {P r} \{\mathrm{AR} = i \} E (q (V _ {n} , B) | \mathrm{AR} = i)}{\operatorname * {P r} \{q (V _ {n} , B) = N \}} = E (\Pi (V _ {n}, B) | q (V _ {n}, B) = N), \end{array}
$$

Hence,

$$
E (\Pi (V _ {n}, B ^ {\prime}) | q (V _ {n}, B) = N) \geq E (\Pi (V _ {n}, B) | q (V _ {n}, B) = N)
$$

Thus, with total probability formula

$$
\begin{array}{l} \pi_ {n} (B) = \sum_ {r = 0} ^ {N} \operatorname * {P r} \{q (V _ {n}, B) = r \} \cdot E (\Pi (V _ {n}, B) | q (V _ {n}, B) = r) \\ \leq \sum_ {r = 0} ^ {N} \operatorname * {P r} \{q (V _ {n}, B) = r \} \cdot E (\Pi (V _ {n}, B ^ {\prime}) | q (V _ {n}, B) = r) = \pi_ {n} (B ^ {\prime}). \end{array}
$$

$j { \le } N { - } 1 , { \pi } _ { n } ( P ) { \le } { \pi } _ { n } ( B )$ Proof of Lemma 1. According to Corollary A1, let . Hence, $B = ( \underbrace { p _ { x _ { N - 1 } } , \ldots , p _ { x _ { N - 1 } } , p _ { N } } _ { N - 1 } )$ , where $p _ { x _ { N - 1 } } { \in } \mathrm { a r g m a x } _ { p _ { j } } ( \pi _ { u } ( p _ { j } , c ) )$ ; 1V

1) if $\pi _ { u } ( p _ { N } , c ) \geq \pi _ { u } \left( p _ { N - 1 } , c \right)$ , then $\pi _ { n } ( L ( p _ { N } , N ) ) \ge \pi _ { n } ( B ) \ge \pi _ { n } ( P )$ with Lemma A1, 2) if $\pi _ { u } \left( p _ { N } , c \right) < \pi _ { u } \left( p _ { N - 1 } , c \right)$ , then $\pi _ { n } \left( L ( p _ { N - 1 } , N ) \right) \geq \pi _ { n } \left( B \right) \geq \pi _ { n } \left( P \right)$ with Lemma A3.

## Appendix B. Proof of Theorem 1

With Lemma 1, for any given P there exists $p ,$ which is irrelated to n, s.t., for any $n , \pi _ { n } ( L ( p , N ) ) { \geq } \pi _ { n } ( P )$

With total probability formula,

$$
\begin{array}{l} \pi_ {T} (P) = \sum_ {n = 0} ^ {\infty} \operatorname * {P r} _ {A} (T, n) \cdot \pi_ {n} (P) \\ \leq \sum_ {n = 0} ^ {\infty} \operatorname * {P r} _ {A} (T, n) \cdot \pi_ {n} (L (p, N)) = \pi_ {T} (L (p, N)). \end{array}
$$

Suppose that $p ^ { * } { \in } \mathrm { a r g m a x } _ { p } \pi _ { T } ( L ( p , N ) )$ i.e., for any $p , \ \pi _ { T } ( L ( p , N ) ) { \leq } \pi _ { T } ( L ( p { * } , N ) ) .$ It follows that $\pi _ { T } ( P ) \leq \pi _ { T } ( L ( p * , N ) )$ □

## Appendix C. Proof of Theorem 2

The proof is very similar to the proofs of Lemma 1 and Theorem 1. The only difference is to define $\pi _ { u } ( p , c ) { = } ( 1 { - } F ( p ) ) \left( { \alpha } p { - } \beta c \right)$ instead of $\pi _ { u } ( p , c ) =$ $\left( 1 - F ( p ) \right) \left( p - c \right)$ □

Appendix D. Proof of Theorem 3

Suppose that $p ^ { * } { \in } { \mathrm { a r g m a x } } _ { p } \pi _ { F , E } ( p )$ . It follows that

$$
\begin{array}{r l} d \pi_ {F, E} (p) / \mathrm{d} p _ {p = p *} & = 0 = \lambda T (- p f (p) + (c _ {1} w (p) \\ & \quad + c _ {2} (1 - w (p))) f (p) - (1 - F (p)) \\ & \quad \times (c _ {1} - c _ {2}) w ^ {\prime} (p) + 1 - F (p)) \end{array}
$$

$$
\begin{array}{c} \text { Because } w ^ {\prime} (p) = \lambda T e ^ {- \lambda T (1 - F (p))} (\lambda T (1 - F (p))) ^ {l - 1} \\ f (p) / \Gamma (l) \geq 0, \end{array}
$$

$$
\begin{array}{l} (1 - F (p ^ {*})) (c _ {1} - c _ {2}) w ^ {\prime} (p ^ {*}) = 1 - F (p ^ {*}) - p ^ {*} f (p ^ {*}) \\ \qquad + (c _ {1} w (p ^ {*}) \\ \qquad + c _ {2} (1 - w (p ^ {*})) f (p ^ {*}) \geq 0 \end{array}
$$

Suppose that $p _ { 1 } ^ { * } = \arg \operatorname* { m a x } _ { p } \pi _ { u } ( p , c _ { 1 } )$ . It follows that $\partial \pi _ { u } ( p , c _ { 1 } ) / \partial p | _ { p = p _ { 1 } ^ { * } } = 0$

Hence,

$$
\begin{array}{l} \partial \pi_ {u} (p, c _ {1}) / \partial p | _ {p = p ^ {*}} = 1 - F (p ^ {*}) - p ^ {*} f (p ^ {*}) + c _ {1} f (p ^ {*}) \\ \quad = 1 - F (p ^ {*}) - p ^ {*} f (p ^ {*}) + c _ {1} (w (p ^ {*}) \\ \qquad + 1 - w (p ^ {*})) f (p ^ {*}) > 1 - F (p ^ {*}) - p ^ {*} f (p ^ {*}) \\ \qquad + (c _ {1} w (p ^ {*}) + c _ {2} (1 - w (p ^ {*})) f (p ^ {*}) \\ \quad = (1 - F (p ^ {*})) (c _ {1} - c _ {2}) w ^ {\prime} (p ^ {*}) \geq 0 \\ \quad = \partial \pi_ {u} (p, c _ {1}) / \partial p | _ {p = p _ {1} ^ {*}} \end{array}
$$

$$
\begin{array}{l} \max _ {P} \pi_ {G, E} (P) \geq (\underbrace {p _ {1} ^ {*} , \ldots , p _ {1} ^ {*}} _ {l}, p ^ {*}, \ldots) \\ = \lambda T ((1 - F (p _ {1} ^ {*})) (p _ {1} ^ {*} - c _ {1}) w (p ^ {*}) \\ \quad + (1 - F (p ^ {*})) (p ^ {*} - c _ {2}) (1 - w (p ^ {*}))) \\ > \lambda T ((1 - F (p ^ {*})) (p ^ {*} - c _ {1}) w (p ^ {*}) \\ \quad + (1 - F (p ^ {*})) (p ^ {*} - c _ {2}) (1 - w (p ^ {*}))) \\ = \pi_ {F, E} (p ^ {*}) = \max _ {p} \pi_ {F, E} (p) \\ \text {It follows that} \max _ {P} \pi_ {G, E} (P) > \max _ {p} \pi_ {F, E} (p). \end{array}
$$

Appendix E. Proof of Theorem 4

Suppose that p<sup>⁎</sup> arg max p

Define $I ( p ) { = } { \pi } _ { F , R } ( p ) / ( \lambda T ( 1 { - } F ( p ) ) { + } 1 )$

With some algebraic transactions, the expected utility of the seller in the GBA can be formulated as follows,

$$
\begin{array}{l} \pi_ {G, R} (P) = \pi_ {F, R} (p _ {1}) \frac {\Gamma (l - 1 , \lambda T (1 - F (p _ {2})))}{\Gamma (l - 1)} + \pi_ {F, R} (p _ {2}) \\ \qquad \times \left(1 - \frac {\Gamma (l - 1 , \lambda T (1 - F (p _ {2})))}{\Gamma (l - 1)} \right. \\ \qquad + (I (p _ {1}) - I (p _ {2})) \frac {(\lambda T (1 - F (p _ {2})) ^ {l - 1}}{(l - 1) !} e ^ {- \lambda T (1 - F (p _ {2})}. \end{array}
$$

Because

$$
\begin{array}{l} \frac {\partial I (p)}{\partial p} \Bigg | _ {p = p ^ {*}} \\ = \frac {\pi_ {F , R} (p) \lambda T f (p) + \pi_ {G , R} ^ {\prime} (p) (\lambda T (1 - F (p) + 1)}{(\lambda T (1 - F (p) + 1) ^ {2}} \Bigg | _ {p ^ {*}} \\ = \frac {\pi_ {F , R} (p ^ {*}) \lambda T f (p ^ {*})}{(\lambda T (1 - F (p ^ {*}) + 1) ^ {2}} > 0 \end{array}
$$

It follows that

$$
\begin{array}{l} \frac {\partial \pi_ {G , R} (P)}{\partial p _ {1}} \Bigg | _ {(p _ {1} = p ^ {*}, p _ {2} = p ^ {*})} \\ = (\frac {\partial \pi_ {F , R} (p _ {1})}{\partial p _ {1}} \frac {\Gamma (l - 1 , \lambda T (1 - F (p _ {2}))}{\Gamma (l - 1)} \\ + \frac {\partial I (p _ {1})}{\partial p _ {1}} \frac {(\lambda T (1 - F (p _ {2})) ^ {l - 1}}{(l - 1) !} e ^ {- \lambda T (1 - F (p _ {2}))} \Bigg | _ {(p _ {1} = p ^ {*}, p _ {2} = p ^ {*})} \\ = 0 + \frac {(\lambda T (1 - F (p _ {2})) ^ {l - 1} e ^ {- \lambda T (1 - F (p _ {2})}}{(l - 1) !} \frac {\partial I (p _ {1})}{\partial p _ {1}} \Bigg | _ {(p _ {1} = p ^ {*}, p _ {2} = p ^ {*})} > 0 \end{array}
$$

$$
\begin{array}{l} \frac {\partial \pi_ {G , R} (P)}{\partial p _ {2}} \Big | _ {(p _ {1} = p ^ {*}, p _ {2} = p ^ {*})} \\ \quad = \left\{(\pi_ {F, R} (p _ {1}) - \pi_ {F, R} (p _ {2})) \partial \left(\Gamma \frac {(l - 1 , \lambda T (1 - F (p _ {2}))}{\Gamma (l - 1)}\right) / \partial p _ {2} \right. \\ \quad + \pi_ {F, R} ^ {\prime} (p _ {2}) \left(1 - \frac {\Gamma (l - 1 , \lambda T (1 - F (p _ {2}))}{\Gamma (l - 1)}\right) \\ \quad + (I (p _ {1}) - I (p _ {2})) \partial \left(\frac {(\lambda T (1 - F (p _ {2})) ^ {l - 1} e ^ {- \lambda T (1 - F (p _ {2})}}{(l - 1) !}\right) / \partial p _ {2} \\ \quad - \frac {(\lambda T (1 - F (p _ {2})) ^ {l - 1} e ^ {- \lambda T (1 - F (p _ {2})}}{(l - 1) !} I ^ {\prime} (p _ {2}) \bigg \} \Big | _ {(p _ {1} = p ^ {*}, p _ {2} = p ^ {*})} \\ \quad = - \frac {(\lambda T (1 - F (p _ {2})) ^ {l - 1} e ^ {- \lambda T (1 - F (p _ {2})}}{(l - 1) !} I ^ {\prime} (p _ {2}) \Big | _ {(p _ {1} = p ^ {*}, p _ {2} = p ^ {*})} \\ \quad = - \frac {(\lambda T (1 - F (p ^ {*})) ^ {l - 1} e ^ {- \lambda T (1 - F (p ^ {*}))}}{(l - 1) !} I ^ {\prime} (p ^ {*}) <   0 \end{array}
$$

Hence, there exists a feasible ascent direction at the point $( p ^ { * } , p ^ { * } , . . . )$ for $\pi _ { G , R } ( P )$

It follows that

$$
p _ {1} ^ {*} > p _ {2} ^ {*}
$$

## Appendix F. The notation

N The number of objects to be sold in the GBA $T$ The auction time

$P = ( p _ { 1 } , p _ { 2 } , . . . , p _ { N } ) , p _ { I } \geq p _ { 2 } \geq . . . \geq p _ { N }$ The price curve in the GBA

$L ( p , k ) = ( \underbrace { p , p , \ldots , p } _ { k } )$ Denotes a k-dimensional vector

with k Identical elements, $p .$

$V _ { n } { = } ( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { n } )$ Denotes n potential buyers' valuations iof the object, where $\nu _ { i }$ denotes potential buyer $i \mathrm { { ^ { \circ } s } }$ valuation.

$\mathrm { P r } _ { A } ~ ( T , ~ n )$ Denotes the probability that there are n ipotential buyers in GBA with period T

c Is the unit cost of the auctioned products in the scenario without economies of scale.

$C { = } ( c _ { 1 } , c _ { 2 } ; l )$ Where $c _ { 1 } > c _ { 2 }$ are the cost levels and l is ithreshold to get the economies of scale. That is if the sold units are less than or equal to $l ,$ the unit cost is $c _ { 1 } ;$ if the sold units are more than $l ,$ the economies of scale are achieved and the unit cost for all products is $c _ { 2 } .$

Given the price curve P and posted price p

$q ( V _ { n } , P )$ Denotes the sold quantity in the auction with n potential buyers, $V _ { n } ,$

$\mathrm { P r } _ { q } ~ ( r , ~ n , ~ P )$ Denotes the probability that there are r sold units with n potential buyers in the auction, $0 \leq r \leq N$

$\scriptstyle \pi _ { u } ~ ( p , c ) = ( 1 - F ( p ) ) ( p - c )$ Denotes the unit expected iprofit, where for any given $c , \ \pi _ { u } \ ( p , \ c )$ is unimodal in p.

$\pi _ { n } \ ( P )$ Denotes the seller's expected profit with n potential buyers in the auction.

$\pi _ { T } \left( P \right)$ Denotes the seller's expected profit in the GBA with auction time T

$\pi _ { C } \left( P \right)$ Denotes the seller's expected profit in the GBA with some coordination contracts.

$\pi _ { G , E } \left( P \right)$ Denotes the seller's expected profit in the GBA with economies of scale where the cost function is C.

$\pi _ { F , E } \left( P \right)$ Denotes the seller's expected profit in the FPM with price $p$ when the cost function is C

$\pi _ { G , R }$ (P) Denotes the seller's utility in the GBA when the seller is risk seeking.

$\pi _ { F , R } \left( P \right)$ Denotes the seller's utility in the FPM with the price p when the seller is risk seeking.

## References

[1] S.K. Anand, R. Aron, Group-buying on the Web: a comparison of price discovery mechanisms, Management Science 49 (2003) 1546–1562.

[2] T. Astebro, The return to independent invention: evidence of unrealistic optimism, risk seeking or skewness loving? Economic Journal 113 (2003) 226–239.

[3] G.P. Cachon, M.A. Lariviere, Supply chain coordination with revenue sharing contracts: strengths and limitations, Management Science 51 (2005) 30–44.

[4] J. Chen, X. Chen, X. Song, Bidder's strategy under groupbuying auction on the Internet, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 32 (2002) 680–690.

[5] D. Clark, Mobshop, a pioneer in group-buying on the web, discontinues consumer service, Wall Street Journal (2001) (Available on the Internet at www.mobshop.com/ar011501d).

[6] J. Cook, Venture capital: Where Mercata Led, Consumers Were Unwilling to Follow. Seattle Post-Intelligencer, Available on the Internet at http://seattlep-i.nwsource.com/business/vc122.shtm 2001.

[7] B. Gottlieb, Does Group-Shopping Work? The Economics of Mercata and Mobshop, http://www.slate.lycos.com/Features/ groupshop/groupshop.asp 2000.

[8] J.T. Gourville, Eager sellers and stony buers: understanding the psychology of new-product adoption, Harvard Business Review (June 2005) 98–106.

[9] A. Gupta, R. Bapna, Online auctions: a closer look. Handbook of electronic commerce in business and society, CRC Press, Boca Raton (FL), 2001.

[10] K. Hendricks, R.H. Porter, An empirical study of an auction with asymmetric information, American Economic Review 78 (1988) 865–883.

[11] T.V. Horn, N. Gustafsson, Demand Aggregation through Online Buying Groups, U.S. Patent 6047266, 2000.

[12] J.M. Jia, J.S. Dyer, A standard measure of risk and risk-value models, Management Science 42 (1996) 1691–1705.

[13] A.C. Johnson, B. Tesch, A Forecast and analysis of US auction sales to consumers, Forrester Research, 2005.

[14] R.J. Kauffman, B. Wang, New buyers' arrival under dynamic pricing market microstructure: the case of group-buying discounts on the Internet, Journal of Management Information Systems 18 (2002) 157–188.

[15] R.J. Kauffman, B. Wang, Bid Together, Buy together: On the Efficacy of Group-Buying Business Models in Internet-Based Selling, Handbook of Electronic Commerce in Business and Society, CRC Press, Boca Raton, FL, 2002.

[16] P. Klemperer, Auction theory: a guide to the literature, Journal of Economic Surveys 13 (1999) 227–286.

[17] P. Klemperer, Collusion and Predation in Auction Markets, Nuffield College, Oxford University, England, 2001 www.nuff. ox.ac.uk/economics/people/klemperer.htm.

[18] P.R. Milgrom, R.J. Weber, A theory of auctions and competitive bidding, Econometrica 50 (1982) 1089–1122.

[19] J.E. Pinker, A. Seidmann, Y. Vakrat, Managing online auctions: current business and research issues, Management Science 49 (2003) 1457–1484.

[20] A. Segev, C. Beam, J. Shanthikumar, Optimal design of Internetbased auctions, Information Technology and Management 2 (2001) 121–163.

[21] D.N. Sull, Strategy as active waiting, Harvard Business Review (September 2005) 120–131.

Jian Chen received the B.Sc. degree in Electrical Engineering from Tsinghua University, Beijing, China, in 1983, and the M.Sc. and the Ph.D. degree both in Systems Engineering from the same University in 1986 and 1989, respectively.

He is a Professor and Chairman of Management Science Department, Director of Research Center for Contemporary Management, Tsinghua University. Dr. Chen has over 100 journal papers and has been a principal investigator for over 30 grants or research contracts with National Science Foundation of China, governmental organizations and companies. His main research interests include modeling and control of complex systems, decision support systems and information systems, forecast and optimization techniques, supply chain management, E-commerce.

He is a senior member of IEEE and a member of INFORMS. He serves as Chairman of the Service Systems and Organizations Technical Committee of IEEE Systems, Man and Cybernetics Society, vice president of China Society for Optimization and Overall Planning, a member of the Standing Committee of Systems Engineering Society of China, China Information Industry Association and Decision Science Society of China. He is the recipient of Science and Technology Progress Awards of Beijing Municipal Government, 2000 and 2001; the Outstanding Contribution Award of IEEE Systems, Man and Cybernetics Society, 1996; Science and Technology Progress Award of the State Educational Commission, 1994.

He is the editor of “the Journal of Systems Science and Systems Engineering”, an associate editor of “IEEE Transactions on Systems, Man and Cybernetics: Part $\mathbf { A } ^ { \ast }$ and “IEEE Transactions on Systems, Man and Cybernetics: Part C”, and serves on the Editorial Board of “Systems Research and Behavioral Science”, “International Journal of Information Technology and Decision Making ” and “International Journal of Electronic Business”. He is the Secretary General of the 1996 IEEE International Conference on Systems, Man and Cybernetics in Beijing, co-chair of the IPC of the 3rd (1998) and 4th (2003) International Conferences on Systems Science and Systems Engineering, and Chair of the 1st Asian eBiz Workshop in 2001, co-chair of the International Conference on Service Systems and Service Management in 2004, Chair of the 4th International Conference on Electronic Business in 2004.

Xilong Chen received the PhD. Degree from Tsinghua University, Beijing, China, in 2004. He is currently a doctoral student at North Carolina State University, USA.

Xiping Song received the M.Sc. Degree from Tsinghua University, Beijing, China, in 2003. He is currently a doctoral student at the Chinese University of Hongkong, Hongkong, China.
