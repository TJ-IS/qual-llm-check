---
otero_id: 7122
otero_key: "GJND58SU"
title: "Robust double auction protocol against false-name bids"
authors: "Makoto Yokoo; Yuko Sakurai; Shigeo Matsubara"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.10.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Robust double auction protocol against false-name bids<sup>\$</sup>

Makoto Yokoo\*, Yuko Sakurai, Shigeo Matsubara

NTT Communication Science Laboratories, 2-4 Hikaridai, Seika-cho, Soraku-gun, Kyoto 619-0237, Japan

Available online 3 December 2003

## Abstract

In this paper, we develop a new double auction protocol called the Threshold Price Double auction (TPD) protocol, which is dominant-strategy incentive compatible even if participants can submit several bids under fictitious names (false-name bids). In Internet auctions, false-name bids are very difficult to detect since identifying each participant on the Internet is virtually impossible. The characteristics of the TPD protocol are that the number of trades and prices of exchange are controlled by the threshold price. Simulation results show that this protocol can achieve a social surplus that is very close to being Pareto efficient.

<sup>D</sup> 2003 Elsevier B.V. All rights reserved.

JEL classification: D44 - auctions Keywords: Double auction; Mechanism design

## 1. Introduction

Electronic Commerce (EC) has made rapid progress in recent years. Internet auctions have become especially popular in EC. Commercial auction sites have been very successful and continue to expand. Auction protocols can be divided into two types: onesided auctions in which a single seller (or buyer) accepts bids from multiple buyers (or sellers), and two-sided or double auctions that permit multiple buyers and sellers to bid to exchange a designated good. For one-sided auctions, many theoretical and practical studies have been conducted [5], including those on Internet auctions and on applications of software agents [4,13,18].

The Internet provides an excellent infrastructure for executing much cheaper auctions with many more sellers and buyers from all over the world. However, we must consider the possibility of new types of cheating. For example, a participant may try to profit from submitting multiple bids made under fictitious names, such as using multiple e-mail addresses. Such a dishonest action is very difficult to detect since identifying each participant on the Internet is virtually impossible. We call a bid made under a fictitious name a false-name bid. The problems resulting from collusion have been discussed by many researchers [8,11,14]. Compared with collusion, a false-name bid is easier to execute since it can be done by someone acting alone, while a bidder has to seek out and persuade other bidders to join in collusion. We can consider false-name bid manipulations as a very restricted special case of general collusion. The authors have analyzed the effect of false-name bids in one-sided auctions [12,19,22] and have developed a one-sided auction protocol that is robust against falsename bids [20].

In this paper, we analyze the effect of false-name bids<sup>1</sup> in double auctions. Double auctions can handle situations where multiple buyers and sellers bid to exchange a designated good, and have been widely used in stock, bond, and foreign exchange markets [2,17]. Double auctions can be either continuous-time or discrete-time. A continuous-time double auction permits exchanges at any moment during a trading period, and the overall trades of the auction are composed of multiple bilateral transactions. On the other hand, in a discrete-time auction (also called clearing-house or call-market), all traders move in a single step from the initial allocation to the final allocation. In addition, the demand/supply of a buyer/seller can be either a single unit of the designated good or multiple units.

As pointed out in Ref. [7], compared with the vast amount of studies on one-sided auctions, there exists a relatively small number of theoretical research efforts on double auctions. This is because since there exist multiple buyers and sellers, theoretical analyses become immensely complicated. For a very simple problem setting where a single unit is traded between a single buyer and a single seller (this setting is called bilateral trade), it has been proven that there exists no trading protocol that is dominantstrategy incentive compatible<sup>2</sup> and also satisfies Pareto efficiency and individual rationality for all cases<sup>3</sup> [10].

In Ref. [7], a dominant-strategy incentive compatible double auction protocol that gives up Pareto efficiency was developed. This protocol deals with the discrete-time case where each participant’s demand/supply is a single unit, and it satisfies individual rationality. We call this protocol McAfee’s Double auction (MCD) protocol.

If we consider the possibility of false-name bids, such as a seller submitting a false-name bid by pretending to be a potential buyer, the MCD protocol is no longer dominant-strategy incentive compatible. In Ref. [20] the authors developed a one-sided, combinatorial auction protocol that is robust against false-name bids. The main idea of this protocol is to utilize the reservation prices of auctioned goods. In this paper, we present a robust double auction protocol that utilizes a concept similar to that presented in [20]. We call this protocol the Threshold Price Double auction (TPD) protocol.

In the following, we first define the basic terms used in this paper (Section 2). Next, we describe the MCD protocol and show examples where the MCD protocol is vulnerable against false-name bids (Section 3). Then, we describe the TPD protocol and show the proof that it is dominant-strategy incentive compatible (Section 4). Furthermore, we show simulation results to evaluate the social surplus obtained by using the TPD protocol (Section 5). Then, we discuss the characteristics of the TPD protocol (Section 6). Finally, we discuss a method to extend the TPD protocol to cases where the demand/supply of each buyer/seller can be multiple units (Section 7).

## 2. Preliminaries

In this section, we define the problem and basic terms used in this paper.

## 2.1. Participants

We assume that there exist m buyers and n sellers. We also assume that these numbers (m and n) are not common knowledge, i.e., each buyer/seller does not know the number of buyers/sellers; thus, participants can submit false-name bids. We assume a buyer x desires to have exactly one unit of the good traded in the $\mathrm { \ a u c t i o n ^ { 4 } }$ and $\mathrm { { h i s } } ^ { 5 }$ valuation for one unit of the good is represented as $b _ { x } { ^ * }$ . This value is private information, so the buyers/sellers other than x do not know this value. In addition, a seller y has exactly one unit of the good and his valuation for one unit of the good is represented as ${ s _ { y } } ^ { * }$ . This value is also private information.

## 2.2. Private value auction

We assume that each buyer/seller knows his valuation of a good with certainty, which is independent of other participants’ valuations. Such a model is called a private value auction.

## 2.3. Quasi-linear utility

If a buyer x with the valuation $b _ { x } ^ { * }$ buys one unit of the good by paying the price $p ,$ we assume his utility is defined as $b _ { x } { } ^ { * } - p .$ Such a utility is called a quasilinear utility. Similarly, if a seller $y$ with the valuation ${ s _ { y } } ^ { * }$ sells one unit of the good at the price $p ,$ we assume his utility is defined as ${ p - { s _ { y } } ^ { * } }$ . If a buyer cannot obtain a unit, or a seller cannot sell a unit, we assume his utility is 0.

## 2.4. Direct revelation mechanism

There exist many variations of possible auction protocols/mechanisms. In particular, we call the following very simple type of mechanism a direct revelation mechanism. In a direct revelation mechanism, each buyer/seller is directly asked his valuation, and the trades and prices are determined according to the declared valuations.

## 2.5. Incentive compatibility

In a traditional definition [6], a direct revelation mechanism is called dominant-strategy incentive compatible if for each participant, declaring his true valuation is a dominant strategy, i.e., the optimal strategy for maximizing his utility regardless of other participants’ actions.

In this paper, we extend this traditional definition so that it can address false-name bid manipulations, i.e., a direct revelation mechanism is dominant-strategy incentive compatible if for each participant, declaring his true valuation by using a single identifier, i.e., without using false-name bids, is a dominant strategy [19,22].

If the revelation principle holds [9], we can restrict our attention to direct revelation mechanisms that are dominant-strategy incentive compatible without loss of generality. In other words, if a certain property (e.g., Pareto efficiency) can be achieved using some auction protocol in a dominant strategy equilibrium, i.e., a combination of dominant strategies of all participants, the property can also be achieved using a direct revelation mechanism that is dominant-strategy incentive compatible. The authors proved that the revelation principle still holds even if the participants can submit false-name bids [19,22]. Therefore, in the rest of this paper, we restrict our attention to direct revelation mechanisms.

We say that an auction protocol is robust against false-name bids if no participant can obtain additional profit by submitting false-name bids. If such robustness is not satisfied, the auction protocol lacks dominant-strategy incentive compatibility.

## 2.6. Individual rationality

If a mechanism has a dominant strategy equilibrium, and the utility of each participant is always nonnegative at the equilibrium, we say that the mechanism is individually rational. In other words, if the mechanism is individually rational, each participant never suffers any loss by participating in the mechanism. In a private value auction, individual rationality is indispensable: nobody wants to participate in an auction where he might be charged more money than he is willing to pay or his property might be taken away without sufficient compensation.

## 2.7. Pareto efficiency

We say that the mechanism is Pareto efficient if a mechanism has a dominant strategy equilibrium and the social surplus, i.e., the sum of the utilities of all participants, is maximized at the equilibrium. In a more general setting, Pareto efficiency does not necessarily mean maximizing the social surplus. In an auction setting, however, participants can transfer money among themselves, and the utility of each participant is quasi-linear. Therefore, the sum of the utilities is always maximized in a Pareto efficient allocation.

Although Pareto efficiency is desirable, it has been proven that there exists no double auction protocol that satisfies Pareto efficiency and individual rationality at the same time [10]. Since individual rationality is indispensable, and we can assume a protocol is dominant-strategy incentive compatible without loss of generality, we need to develop a double auction protocol that is dominant-strategy incentive compatible and individually rational and that can achieve a social surplus that is close to being Pareto efficient.

## 3. MCD protocol

## 3.1. Protocol description

In this section, we first describe the double auction protocol proposed by Ref. [7]. We call this protocol the MCD protocol.

Let us represent declared (not necessarily true) buyers’ valuations as $b _ { 1 } , \ldots , b _ { m }$ and declared (not necessarily true) sellers’ valuations as $s _ { 1 } , . . . . s _ { n }$ . Furthermore, we define the order statistics to be

$$
b _ {(1)} \geq b _ {(2)} \geq \dots \geq b _ {(m)}
$$

and

$$
s _ {(1)} \leq s _ {(2)} \leq \dots \leq s _ {(n)}.
$$

Please note the reverse ordering for buyers and sellers. We use the notation (i) for the i-th highest valuation of buyers<sup>6</sup> and the i-th lowest valuation of sellers.

In addition, to simplify the protocol description, we assume $b _ { ( m + 1 ) }$ denotes the lowest possible valuation of buyers $( \mathrm { e . g . , \ 0 ) }$ , and $s _ { ( n + 1 ) }$ denotes the highest possible valuation of sellers (e.g., one billion dollars). Furthermore, we assume $b _ { ( m + 1 ) } < s _ { ( n + 1 ) }$ holds.

Let us choose k so that

$$
b _ {(k)} \geq s _ {(k)}
$$

and

$$
b _ {(k + 1)} <   s _ {(k + 1)}
$$

hold.

Since for (1) to (k), the valuation of the buyer is larger than that of the seller, at most k trades are possible.

Additionally, we define the candidate of a trading price $p _ { 0 }$ as follows:

$$
p _ {0} = \frac {1}{2} (b _ {(k + 1)} + s _ {(k + 1)}).
$$

The protocol is defined as follows.

(1) If $s _ { ( k ) } { \le } p _ { 0 } { \le } b _ { ( k ) }$ holds: the buyers/sellers from (1) to (k) trade at price $p _ { 0 }$

(2) ${ \mathrm { I f } } p _ { 0 } { > } b _ { ( k ) } { \mathrm { o r } } p _ { 0 } { < } s _ { ( k ) }$ holds: the buyers/sellers from (1) to $( k - 1 )$ trade. Each buyer pays $b _ { ( k ) } ,$ , and each seller gets $s _ { ( k ) }$

If the second condition holds, we cannot use $p _ { 0 }$ as the trading price for k trades, since it is either larger than buyer’s bid $b _ { ( k ) }$ or smaller than seller’s bid $s _ { ( k ) } .$ . In this case, to set an appropriate trading price, we sacrifice k-th trade and use $b _ { ( k ) }$ as buyer’s price and $s _ { ( k ) }$ as seller’s price. Since $b _ { ( k ) }$ is larger than $s _ { ( k ) } ,$ , the amount $\left( k - 1 \right) \left( b _ { \left( k \right) } - s _ { \left( k \right) } \right)$ is left over. We assume that the auctioneer, or the budget balancer, receives this amount. We assume that the auctioneer is a nontrading agent who does not desire to buy or sell the good.

If there exists no false-name bid, this protocol is proven to be dominant-strategy incentive compatible [7]. In this protocol, if the first condition holds, the obtained result is Pareto efficient. On the other hand, if the second condition holds, the result is not Pareto efficient since the k-th buyer/seller cannot trade.

An intuitive explanation why the MCD protocol is dominant-strategy incentive compatible is as follows. Let us consider the protocol from a buyer’s viewpoint. Assume a buyer reports a valuation $b '$ while his true valuation is b and this buyer can trade.

If the first condition holds, this buyer can win a unit and pay $p _ { 0 }$ as long as his declared valuation $b ^ { \prime }$ is larger than (or equal to) $p _ { 0 }$ . With a similar argument to the Vickrey auction protocol [16], truth-telling is a dominant strategy. More specifically, under-reporting is useless since the payment never changes. Overreporting is also useless since it only increases the chance for winning by paying more than his valuation.

If the second condition holds, this buyer can win a unit and pay $b _ { ( k ) }$ as long as his declared valuation $b ^ { \prime }$ is larger than (or equal to) $b _ { ( k ) }$ . With a similar argument, truth-telling is a dominant strategy.

## 3.2. Effect of false-name bids on MCD protocol

Next, we show examples where the MCD protocol is not robust against false-name bids.

Example 1. Let us assume the true valuations of buyers/sellers are as follows.

 buyers’ valuations: 9>8>7>4

 sellers’ valuations: 2 < 3 < 4 < 5.

If each participant truthfully declares his valuation, the first condition of the protocol holds, and buyers/ sellers from (1) to (3) trade at the price $p _ { 0 } { = } ( 4 + 5 ) /$ 2 = 4.5. On the other hand, if one of the sellers from (1) to (3) submits a false-name bid 4.8 pretending to be a potential buyer, the declared valuations become as follows.

 buyers’ valuations: 9>8>7>4.8>4

 sellers’ valuations: $2 < 3 < 4 < 5 .$

In this case, the number of trades does not change, but the price is increased to (4.8 + 5)/2 = 4.9. We can see that a seller can increase his utility by submitting a false-name bid while pretending to be a potential buyer; thus, the MCD protocol is not robust against false-name bids.

Example 2. Let us assume the true valuations of buyers/sellers are as follows.

If each participant truthfully declares his valuation, the second condition of the protocol holds, and buyers/sellers from (1) to (2) trade, each buyer pays 7, and each seller gets 4.

On the other hand, let us assume seller (3) submits a false-name bid 6 pretending to be another potential seller. In this case, the declared valuations are as follows.

 buyers’ valuations: 9>8>7>4

 sellers’ valuations: $2 < 3 < 4 < 6 < 1 2 .$

Now, the first condition of the protocol holds. Thus, the buyers/sellers from (1) to (3) trade at the price $p _ { 0 } \mathrm { = } ( 4 + 6 ) / 2 = 5$ . If seller (3) truthfully declares his valuation, he cannot trade and his utility is 0. On the other hand, if he submits a false-name bid, his utility becomes 5  4 = 1.

These examples show that the MCD protocol is not dominant-strategy incentive compatible when participants can submit false-name bids.

## 4. Robust double auction protocol against falsename bids

## 4.1. TPD protocol

In this section, we present a double auction protocol that utilizes a concept similar to that presented in Ref. [20]. We call it the Threshold Price Double auction (TPD) protocol.

First, the auctioneer determines a threshold price r. As in the MCD protocol, we assume that the auctioneer is a non-trading agent who does not desire to buy or sell the good. We assume that the auctioneer determines this threshold price without consulting the declared valuations of buyers/sellers. Then, each buyer/seller declares his valuation.<sup>7</sup> Let us assume the declared (not necessarily true) valuations are as follows.

 buyers’ valuations:

$$
b _ {(1)} \geq b _ {(2)} \geq \dots \geq b _ {(i)} \geq r > b _ {(i + 1)} \geq \dots
$$

 sellers’ valuations:

$$
s _ {(1)} \leq s _ {(2)} \leq \dots \leq s _ {(j)} \leq r > b <   s _ {(j + 1)} \leq \dots
$$

The TPD protocol is defined as follows.

(1) When $i = j \colon$ the buyers/sellers from (1) to (i) trade at the price r.

(2) When $i { > } j \colon$ the buyers/sellers from (1) to ( j) trade. Each buyer pays $b _ { ( j + 1 ) } ,$ each seller gets r. The auctioneer gets the amount of $j ( b _ { ( j + 1 ) } - r )$

(3) When $i < j \colon$ the buyers/sellers from (1) to (i) trade. Each buyer pays r, each seller gets $s _ { ( i + 1 ) }$ . The auctioneer gets the amount of $i ( r - s _ { ( i + 1 ) } )$

## 4.2. Example

Example 3. Let us assume the valuations are identical to Example 1.

 buyers’ valuations: $9 { > } 8 { > } 7 { > } 4$

 sellers’ valuations: $2 < 3 < 4 < 5 .$

In addition, let us assume the threshold price $r = 4 . 5$ . In this case, if each buyer/seller declares his true valuation, the first condition of the protocol holds. Thus, the buyers/sellers from (1) to (3) trade at the price $r { = } 4 . 5$

If one of the sellers from (1) to (3) submits a falsename bid 4.8 by pretending to be a potential buyer, although the price for buyers increases, the price for sellers does not change from the threshold price 4.5; thus, submitting a false-name bid is useless.

Example 4. Let us assume the valuations are identical to Example 2.

 buyers’ valuations: $9 { > } 8 { > } 7 { > } 4$

 sellers’ valuations: $2 < 3 < 4 < 1 2 .$

If the threshold price $r = 6$ and each buyer/seller declares his true valuation, the first condition of the protocol holds; the buyers/sellers from (1) to (3) trade at the price $r = 6$

On the other hand, if the threshold price $r = 7 . 5 ,$ , the third condition of the protocol holds. Thus, the buyers/ sellers from (1) to (2) trade, each buyer pays the threshold price $r = 7 . 5 ,$ , and each seller gets 4. The seller (3) cannot trade even if he submits a false-name bid pretending to be another potential seller.

## 4.3. Proof of incentive compatibility

We show the proof of the following theorem.

Theorem 1. The TPD protocol is dominant-strategy incentive compatible even if participants can submit false-name bids.

Since buyers and sellers are basically symmetrical, we only show the proof for the following lemma.

Lemma 1. In the TPD protocol, for a buyer, declaring his true valuation using a single identifier as a buyer is a dominant strategy.

We can show the fact that for a seller, declaring his true valuation is a dominant strategy in a similar way.

To prove Lemma 1, we first prove the following lemma.

Lemma 2. In the TPD protocol, if a non-trading bid is removed (in other words, if the bidder did not participate in the auction), then for each of the other bidders, his utility increases or remains the same.

The proof is as follows. First, let us consider the case that a non-trading buyer’s bid b is removed. If $b < r ,$ clearly, removing this bid has no effect; for each buyer and seller, his utility remains the same. If $b \geq r ,$ since b is a non-trading bid, the second condition of the TPD protocol must hold, i.e., i >j. For each buyer, clearly, the effect of removing this bid is non-negative, since the payment might decrease (or at least remains the same).

Then, let us consider the effect for sellers in the following two cases.

i  1>j: By removing b, the second condition still holds and all j sellers can trade at price $r ,$ thus the utility of a seller remains the same.

$i - 1 = j \colon$ By removing b, the first condition holds and all j sellers can trade at price $r ,$ thus the utility of a seller remains the same.

Therefore, the effect of removing b on the utility of each buyer and seller is either to increase the utility or leave it unchanged. In a similar way, we can show that the effect of removing a non-trading seller’s bid s on the utility of each buyer and seller is either to increase the utility or leave it unchanged. 5

Next, we prove the following lemma.

Lemma 3. In the TPD protocol, if a pair of a trading seller’s bid and a trading buyer’s bid is removed, then for each of the other bidders, his utility remains the same.

The proof is almost straightforward. By removing a pair of a trading seller’s bid s and a trading buyer’s bid b, in the TPD protocol, the applied conditions does not change and the payment remains the same for all other bidders. 5

Next, we prove the following lemma.

Lemma 4. In the TPD protocol, if a trading buyer’s bid is removed, then for each of other buyers, his utility increases or remains the same.

The proof is also straightforward. By removing a trading buyer’s bid b, clearly, the payment of other buyers decreases or at least remains the same. 5

By using these lemmas, we prove the following lemma holds.

Lemma 5. In the TPD protocol, if a buyer submits multiple bids (both as buyers and sellers), his utility increases or remains the same if he uses a single identifier as a buyer.

The proof is as follows. From Lemma 2, submitting a non-trading bid is totally useless, i.e., he cannot obtain any gain from a non-trading bid itself, and his utility increases or remains the same by removing the non-trading bid. Therefore, we can assume all bids are included in the actual trades. Let us assume the buyer obtains k units as buyers and sells l units as sellers. From the assumption that he is a buyer, k>l must hold, i.e., he does not own any units initially.<sup>8</sup>

From Lemma 3, the buyer would be better off if he removes l trading pairs. This is because he cannot obtain any gain from each trading pair since the seller’s price is always smaller than or equal to the buyer’s price, and by removing a trading pair, the utility of other bidders remains the same.

Therefore, we can assume the buyer submits only $k - l$ buyer’s bids (without submitting any sellers bids). If $k - l = 1$ , the proof is completed. If $k - l { > } 1$ since we assume the demand/supply of each bidder is a single-unit, having multiple units is useless. From Lemma 4, the buyer can increase his utility by removing $k - l - 1$ buyer’s bids, i.e., by submitting only one bid. 5

Next, we show the following lemma holds.

Lemma 6. In the TPD protocol, if a buyer submits one bid as a buyer, declaring his true valuation is a dominant strategy.

The proof is as follows. Let us assume the true valuation of a buyer x is $b _ { x } { } ^ { * }$ . If ${ b _ { x } } ^ { * } { < r } ,$ the price for buyers will never be less than r; thus, trying to obtain a unit by over-reporting is useless. In addition, if ${ b _ { x } } ^ { * } { \geq } r$ and x can obtain a unit when he truthfully declares his valuation, the price for buyers does not change by over/under-reporting as long as he obtains one unit; thus, over/under-reporting is useless. Additionally, if ${ b _ { x } } ^ { * } { \geq } r$ and x cannot obtain a unit when he truthfully declares his valuation, then the second condition of the protocol holds, and the price for buyers is $b _ { ( j + 1 ) }$ . In this case, $b _ { ( j + 1 ) } \geq b _ { x } ^ { * }$ holds, and by over-reporting, the price for buyers will never be less than $b _ { ( j + 1 ) } ;$ thus, x cannot obtain a positive utility. From these facts, we conclude that truth-telling is a dominant strategy for a buyer x. 5

From these lemmas, we can conclude Lemma 1, i.e., submitting his true valuation without using falsename bids is a dominant strategy for a buyer.

## 5. Evaluation

In this section, we use simulation results to compare the social surplus obtained by the TPD protocol and that obtained by the MCD protocol under the assumption that participants do not submit false-name bids.

We generated a problem instance by the following method.

(1) Determine the number of buyers m and the number of sellers n.

Table 1  
Comparison of social surplus between TPD and MCD

<table><tr><td>n=m</td><td>TPD</td><td>TPDexceptauctioneer</td><td>MCD</td><td>MCDexceptauctioneer</td></tr><tr><td>5</td><td>103.4(92.4%)</td><td>84.4(75.4%)</td><td>105.9(94.6%)</td><td>96.7(86.5%)</td></tr><tr><td>10</td><td>228.9(95.9%)</td><td>187.5(78.6%)</td><td>235.1(98.5%)</td><td>220.5(92.4%)</td></tr><tr><td>25</td><td>609.6(98.4%)</td><td>519.9(83.9%)</td><td>617.9(99.7%)</td><td>599.0(96.7%)</td></tr><tr><td>50</td><td>1255.9(99.2%)</td><td>1111.4(87.8%)</td><td>1265.7(99.9%)</td><td>1246.5(98.4%)</td></tr><tr><td>100</td><td>2533.8(99.6%)</td><td>2314.3(91.0%)</td><td>2543.3(100.0%)</td><td>2527.8(99.6%)</td></tr><tr><td>500</td><td>12738.3(99.9%)</td><td>12254.1(96.1%)</td><td>12745.5(100.0%)</td><td>12744.9(100.0%)</td></tr></table>

(2) Choose the valuation of each buyer/seller randomly from a uniform distribution [0,100].

In Table 1, we show the results when we set $n = m$ and vary n( = m) from 5 to 500. For the TPD protocol, we set the threshold price to 50. In Table 1, we show the social surplus and the social surplus except the auctioneer. Each data point is the average of 1000 problem instances. We show the ratio to the Pareto efficient social surplus<sup>9</sup> within the parentheses.

As shown in Table 1, when $n ( = m )$ becomes large, the difference between the TPD protocol and the MCD protocol becomes relatively small, and both results become close to the Pareto efficient social surplus. The trend is similar for the social surplus except the auctioneer. When $n = m = 5 0 0$ , the revenue of the auctioneer is less than 4% of the Pareto efficient social surplus.

In Fig. 1, we show the results where we set $n = m = 5 0 0$ and vary the threshold price. We show the social surplus of the TPD protocol and the social surplus except the auctioneer. As shown in Fig. 1, the best result is obtained when the threshold price is 50. This is true for all problem sizes in Table 1, since the valuation of each buyer/seller is chosen randomly from a uniform distribution [0,100].

The social surplus is relatively stable when the threshold price slightly moves away from the optimal value 50. On the other hand, the social surplus except the auctioneer is less stable compared with the social surplus including the auctioneer. When the threshold price slightly moves away from the optimal value, less valuable trades will be lost; thus, the social surplus does not change very rapidly. On the other hand, the difference between the price for sellers and the price for buyers increases almost linearly when the threshold price moves away from the optimal value; thus, the revenue of the auctioneer increases (and the social surplus except the auctioneer decreases) rather rapidly.

![](/api/attachments/GJND58SU/fulltext/images/d0f843b6a2ba1f6d858e4a00b0e0409fbebeb56b5b3d03c70c1d02587e43fda6.jpg)  
Fig. 1. Social surplus of TPD protocol (n = 500, varying threshold price).

Comparison of social surplus between TPD and MCD (binomial distribution)

<table><tr><td>N</td><td>TPD</td><td>TPDexceptauctioneer</td><td>MCD</td><td>MCDexceptauctioneer</td></tr><tr><td>10</td><td>101.3(91.7%)</td><td>81.0(73.3%)</td><td>103.8(94.0%)</td><td>93.7(84.8%)</td></tr><tr><td>20</td><td>223.4(94.8%)</td><td>175.7(74.6%)</td><td>231.2(98.1%)</td><td>213.4(90.7%)</td></tr><tr><td>50</td><td>607.0(97.8%)</td><td>504.4(81.3%)</td><td>618.7(99.7%)</td><td>598.5(96.5%)</td></tr><tr><td>100</td><td>1252.9(98.8%)</td><td>1076.7(84.9%)</td><td>1267.4(99.9%)</td><td>1247.8(98.4%)</td></tr><tr><td>200</td><td>2492.0(99.4%)</td><td>2223.6(88.7%)</td><td>2506.6(100.0%)</td><td>2491.6(99.4%)</td></tr><tr><td>1000</td><td>12724.0(99.9%)</td><td>12123.9(95.2%)</td><td>12734.9(100.0%)</td><td>12734.4(100.0%)</td></tr></table>

In Table 2, we show the result where n and m can be different, i.e., we randomly choose the number of buyers m and the number of sellers n from a binomial distribution $B ( N , p )$ , where we set $p { = } 0 . 5 .$ . In this case, the average number of m and n is N/2. Other parameter settings are identical to Table 1. We can see that the results in Table 2 are very similar to the results in Table 1.

## 6. Discussions

As far as the authors’ know, the TPD protocol is the first non-trivial double auction protocol that is dominant-strategy incentive compatible even if participants can submit false-name bids. When there exists no false-name bid, designing a dominant-strategy incentive compatible protocol is not very difficult. For example, the following simple protocol is dominant-strategy incentive compatible: we set the threshold price and determine the trades randomly from potential buyers/sellers whose valuations are larger/ smaller than the threshold price. On the other hand, when false-name bids are possible, this simple randomization protocol is no longer dominant-strategy incentive compatible. For example, let us assume the valuation of a buyer is very large (e.g., US\$10,000), and the threshold price is small (e.g., US\$10). In this case, the buyer will submit multiple bids as buyers so that the chance of getting one unit increases, even if he needs only one unit.

The reason that we cannot apply a similar proof method described in Section 4 for this protocol is as follows. In this simple randomized protocol, whether an agent can trade or not becomes probabilistic. In the proof of Lemma 5, we conclude that if a buyer obtains two units using false-name bids, his utility increases by dropping one bid, since he can win one unit for sure. This is no longer true for a probabilistic protocol.

One limitation of the TPD protocol is that the revenue of the auctioneer becomes large compared with the MCD protocol. This fact is not desirable, since if the revenue of the auctioneer is large, the buyers/sellers are discouraged from participating in trading. The auctioneer cannot simply return the revenue to the participants since it will affect incentives of participants. This problem has been pointed out for the Clarke tax [15].

As shown in the simulation result in Fig. 1, when the threshold price is set appropriately, the ratio of the auctioneer’s revenue in the social surplus is small, but it can be large when the threshold price moves away from the optimal value. We need to develop a method for finding the optimal threshold price for a given situation.

## 7. Extending protocol to multiple unit demand/ supply cases

In this section, we discuss a method for extending the TPD protocol to cases where the demand/supply of each buyer/seller can be multiple units. Such an extension is of practical importance since double auctions have been widely used in stock, bond, and foreign exchange markets, and the demand/supply of each participant is usually multiple units in these markets.

The authors have shown that in one-sided auctions, the robustness of a protocol against false-name bids is affected by the marginal values of each unit. The marginal value of a unit means the increase of the participant’s utility as a result of obtaining one additional unit. In Refs. [12,22], the authors have shown that the generalized Vickrey auction protocol [14], which is one instance of the Clarke (or the pivotal) mechanism [1], is robust against false-name bids when the marginal values of all participants decrease.

An intuitive explanation why decreasing marginal values in multi-unit auction are sufficient for the robustness of the GVA against false-name bids is as follows. In the GVA, the payment of each agent is equal to the decreased amount of the social surplus except the agent, caused by his participation. In addition, the net utility (after the payment) of an agent is equal to the increased amount of the social surplus (including the agent). If the problem domain satisfies the condition called concavity of agents [19,22], as the number of other agents becomes large, the increased amount of the social surplus by adding one agent becomes small, which means the net utility of the agent becomes small.<sup>10</sup> This condition holds when marginal values of all agents decrease. In this case, pretending to be multiple agents by using false-name bids is useless since it only decreases the net utility. On the other hand, when marginal values can increase, the concavity condition can be violated. In this case, using false-name bids can be profitable. Please consult Refs. [19,22] for more detailed discussions.

In the following, we show that a simple extension of the TPD protocol is dominant-strategy incentive compatible when the marginal values of all participants decrease or remain the same.

Let us represent the valuations of buyer x as $b _ { x , 1 }$ $b _ { x , 2 } , b _ { x , 3 } , . . . ,$ where $b _ { x , k }$ represents the marginal value of k-th unit for x. More specifically, $b _ { x , k }$ represents the increase of $x ^ { \prime } \mathrm { s }$ utility by obtaining one additional unit when x already has k  1 units. Under the assumption that the marginal values decrease (or remain the same), for all x and k, $b _ { x , k } \geq b _ { x , k + 1 }$ holds. The assumption that marginal values decrease seems to be reasonable when trading stocks, bonds, or foreign currencies. Similarly, we represent the valuations of seller y as $s _ { y , 1 } , s _ { y , 2 } , s _ { y , 3 } , . . .$ . We assume if y has three units to sell, the minimum price at which y is willing to sell the first unit (while keeping two units at hand) is represented as $s _ { y , 1 }$ . In addition, the minimum price at which y is willing to sell two units can be represented as $s _ { y , 1 } + s _ { y , 2 }$ . Under the assumption that the marginal values decrease (or remain the same), for all y and k, $s _ { y , k } { \le } s _ { y , k + 1 }$ holds.

Let us represent the valuations of each unit for buyers sorted in decreasing order as

$$
b _ {(1)} \geq b _ {(2)} \geq \dots \geq b _ {(i)} \geq r > b _ {(i + 1)} \geq \dots
$$

and the valuations of each unit for sellers sorted in increasing order as

$$
s _ {(1)} \leq s _ {(2)} \leq \dots \leq s _ {(j)} \leq r <   s _ {(j + 1)} \leq \dots ,
$$

where r is the threshold price.

The protocol is described as follows.

(1) When $i = j \colon$ the buyers/sellers from (1) to (i) trade at the price r for each unit.

(2) When $i > j \colon$ the buyers/sellers from (1) to ( j) trade. Each seller gets r for each unit. A buyer x who obtains k units pays the total of $\scriptstyle \sum _ { l = j - k + 1 } ^ { j }$ max $( b _ { ( l ) } ^ { \sim x } , r )$ , where $\bar { b _ { ( l ) } ^ { - x } }$ represents the l-th largest valuation except those of x. The auctioneer gets the difference.

(3) When $i < j \colon$ the buyers/sellers from (1) to (i) trade. Each buyer pays r for each unit. A seller y who sells k units gets the total of $\textstyle \sum _ { l = i - k + 1 } ^ { i }$ min $( s _ { ( l ) } ^ { \sim y } , r )$ 2 where $s _ { ( l ) } ^ { \sim y }$ is l-th smallest valuation except those of $y .$ The auctioneer gets the difference.

Example 5. We show an example of the protocol execution. Let us assume the valuations of buyers/ sellers are as follows.

 buyers’ valuations: $9 { > } 8 { > } 7 { > } 6 { > } 4$

 sellers’ valuations: $2 < 3 < 4 < 5 < 7$

In addition, let us assume that the threshold price is 4.5. Furthermore, buyer x declares both valuations 9 and 8, and other valuations belong to different sellers/ buyers.

The second condition of the protocol holds and three units are traded. Each seller gets the threshold price 4.5. The payment of buyer x is calculated as follows: $\sum _ { l = 3 - 2 + 1 } ^ { 3 }$ max $( b _ { ( l ) } ^ { \sim x } , r ) =$ max $( b _ { ( 2 ) } ^ { \sim x } , 4 . 5 )$ þ max $( b _ { ( 3 ) } ^ { \sim x } , 4 . 5 )$ . Since $( b _ { ( 2 ) } ^ { \sim } \overset { x ^ { \sim } } { = } 6 )$ and $( b _ { ( 3 ) } ^ { \sim } { } ^ { x } { = } 4 < 4 . 5 )$ the payment of x becomes $6 + 4 . 5 = 1 0 . 5$ . On the other hand, the payment of the buyer who declares 7 and obtains one unit is calculated as the third highest valuation except 7, i.e., 6.

With the assumption that marginal values decrease, if a buyer’s valuation for the k-th unit is included in the trade, his valuation for the k  1-th unit is also included in the trade. In addition, if a seller’s valuation for the k-th unit is included in the trade, his valuation for the k  1-th unit is also included in the trade.

On the other hand, if marginal values of participants can increase, these properties cannot hold, i.e., we cannot express valuations of agents by a value associated to each unit. For example, if an agent has an all-or-nothing valuation of 10 for two units, there is no way to correctly associate separate values for each unit. The proposed protocol does not work if we cannot associate a value for each unit since we cannot determine the trades by sorting the participants’ valuations of each unit.

The outline of the proof that this protocol is dominant-strategy incentive compatible is as follows. Since buyers and sellers are basically symmetrical, let us show that for a buyer, declaring his true valuations using a single identifier as a buyer is a dominant strategy. Let us assume a buyer submits multiple bids both as sellers and buyers. Basically, Lemmas 2 and 3 still hold. Therefore, we can safely assume a buyer submits bids only as buyers.

When the first or the third condition of the protocol holds, the buyer pays threshold price r for each unit. Clearly, using false-name bids in this situation is useless since his payment does not change as long as he obtains the same number of units. When the second condition of this protocol holds, the procedure for determining the payments of buyers is identical to the generalized Vickrey auction protocol [14]. By using the method presented in Refs. [12,22] for proving that the generalized Vickrey auction protocol is robust against false-name bids when marginal values decrease, we can prove that submitting multiple bids as buyers is useless. Similarly, we can show that for a seller, submitting falsename bids is useless.

## 8. Conclusions

This paper developed a new double auction protocol (TPD protocol) that is dominant-strategy incentive compatible even if participants can submit false-name bids. When the participants of an auction do not submit false-name bids, the MCD protocol is proven to be dominant-strategy incentive compatible. On the other hand, if the participants can submit false-name bids, we showed that the MCD protocol is no longer dominant-strategy incentive compatible. We described the TPD protocol that utilizes the threshold price to control the number of trades and the exchange prices, and proved that this protocol is dominant-strategy incentive compatible. By using simulation results, we showed that this protocol can achieve a social surplus that is very close to the Pareto efficient social surplus.

Our future work includes extending the TPD protocol to cases where marginal values of units can increase and to cases where multiple heterogeneous goods with correlated values are traded.

## References

[1] E.H. Clarke, Multipart pricing of public goods, Public Choice 2 (1971) 19 – 33.

[2] D. Friedman, J. Rust (Eds.), The Double Auction Market: Institutions, Theories, and Evidence, Addison-Wesley, Reading, Massachusetts, 1991.

[3] F. Gul, E. Stacchetti, Walrasian equilibrium with gross substitutes, Journal of Economic Theory 87 (1999) 95– 124.

[4] R.H. Guttman, A.G. Moukas, P. Maes, Agent-mediated electronic commerce: a survey, The Knowledge Engineering Review 13 (2) (1998) 147 – 159.

[5] P. Klemperer, Auction theory: a guide to the literature, Journal of Economics Surveys 13 (3) (1999) 227 – 286.

[6] A. Mas-Colell, M.D. Whinston, J.R. Green, Microeconomic Theory, Oxford University Press, New York, 1995.

[7] R.P. McAfee, A dominant strategy double auction, Journal of Economic Theory 56 (1992) 434–450.

[8] R.P. McAfee, J. McMillan, Bidding rings, American Economic Review 82 (3) (1992) 579– 599.

[9] R.B. Myerson, Optimal auction design, Mathematics of Operation Research 6 (1981) 58 – 73.

[10] R.B. Myerson, M.A. Satterthwaite, Efficient mechanisms for bilateral trading, Journal of Economic Theory 29 (1983) 265– 281.

[11] E. Rasmusen, Games and Information, Blackwell, Cambridge, Massachusetts, 1994.

[12] Y. Sakurai, M. Yokoo, S. Matsubara, A limitation of the generalized Vickrey auction in electronic commerce: robustness against false-name bids, Proceedings of the Sixteenth National Conference on Artificial Intelligence (AAAI-99), AAAI Press, Menlo Park, California, 1999, pp. 86– 92.

[13] T. Sandholm, Limitations of the Vickrey auction in computational multiagent systems, Proceedings of the Second International Conference on Multiagent Systems (ICMAS-96), AAAI Press, Menlo Park, California, 1996, pp. 299 – 306.

[14] H.R. Varian, Economic mechanism design for computerized agents, Proceedings of the First Usenix Workshop on Electronic Commerce, 1995.

[15] H.R. Varian, Intermediate Microeconomics: A Modern Approach, 5th ed., W.W. Norton, New York, 1999.

[16] W. Vickrey, Counter speculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1961) 8 – 37.

[17] P.R. Wurman, W.E. Walsh, M.P. Wellman, Flexible double auctions for electronic commerce: theory and implementation, Decision Support Systems 24 (1998) 17 – 27.

[18] P.R. Wurman, M.P. Wellman, W.E. Walsh, The Michigan Internet AuctionBot: a configurable auction server for human and software agents, Proceedings of the Second International Conference on Autonomous Agents (Agents-98), 1998, pp. 301 – 308.

[19] M. Yokoo, Y. Sakurai, S. Matsubara, The effect of false-name declarations in mechanism design: towards collective decision making on the internet, Proceedings of the Twentieth International Conference on Distributed Computing Systems (ICDCS-2000), IEEE Computer Society, Los Alamitos, California, 2000, pp. 146– 153.

[20] M. Yokoo, Y. Sakurai, S. Matsubara, Robust combinatorial auction protocol against false-name bids, Artificial Intelligence 130 (2) (2001) 167 – 181.

[21] M. Yokoo, Y. Sakurai, S. Matsubara, Robust double auction protocol against false-name bids, Proceedings of the 21st International Conference on Distributed Computing Systems (ICDCS-2001), IEEE Computer Society, Los Alamitos, Cal ifornia, 2001, pp. 137– 145.

[22] M. Yokoo, Y. Sakurai, S. Matsubara, The effect of false-name bids in combinatorial auctions: new fraud in Internet auctions, Games and Economic Behavior (forthcoming).

![](/api/attachments/GJND58SU/fulltext/images/1a3e2191a181956e643be000fbfdaf0ab713fd2f4534df83acd95b0b16406416.jpg)  
Yuko Sakurai is a research scientist of NTT Communication Science Laboratories, NTT. She received her MS degree in Mathematics from Nagoya University. Her research interests are in the area of multi-agent systems and game theory, especially mechanism design on the Internet auctions.

Makoto Yokoo received the BE, ME, and PhD degrees from the University of Tokyo, Japan, in 1984, 1986, and 1995, respectively. He is currently a distinguished technical member in NTT Communication Science Laboratories, Kyoto, Japan. His research interests include multi-agent systems, constraint satisfaction, and mechanism design among selfinterested agents. His research on constraint satisfaction

among multiple agents is presented in his book ‘‘Distributed Constraint Satisfaction: Foundation of Cooperation in Multi-agent Systems’’ (Springer, 2000). He is an associate editor of ‘‘Journal of Artificial Intelligence Research’’ and an editorial board member of ‘‘Constraints’’ and ‘‘Autonomous Agents and Multi-agent Systems’’.

![](/api/attachments/GJND58SU/fulltext/images/2588d4ae62b3415b847d9911e21257e786052915b1ee6076f59b5a4d5a979e14.jpg)

![](/api/attachments/GJND58SU/fulltext/images/3207037771c38dbdddb0b9d1e4c5d12f062babc68aff84ab97d0671c0874a6bf.jpg)

Shigeo Matsubara is a senior research scientist of NTT Communication Science Laboratories, NTT. He received his PhD degree in Informatics from Kyoto University. His research focuses on multiagent systems and information economics, especially the design of Internet trade. He has published in Artificial Intelligence Journal and other academic journals.
