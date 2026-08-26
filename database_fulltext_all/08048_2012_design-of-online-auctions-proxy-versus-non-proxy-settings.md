---
otero_id: 8048
otero_key: "RTK8XPS3"
title: "Design of online auctions: Proxy versus non-proxy settings"
authors: "Gangshu (George) Cai; Ying-Ju Chen; Xiting Gong"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.09.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design of online auctions: Proxy versus non-proxy settings

Gangshu (George) Cai <sup>a</sup>, Ying-Ju Chen <sup>b,</sup>⁎, Xiting Gong <sup>c</sup>

<sup>a</sup> Department of Management, Kansas State University, Manhattan, KS 66506, United States

<sup>b</sup> IEOR Department, University of California at Berkeley, 4121 Etcheverry Hall, Berkeley, CA 94720, United States

<sup>c</sup> Department of Industrial and Operations Engineering, University of Michigan, Ann Arbor, MI 48109, United States

## a r t i c l e i n f o

Article history: Received 4 December 2010 Received in revised form 11 September 2011 Accepted 18 September 2011 Available online 24 September 2011

Keywords: e-Commerce Sequential auctions Proxy bidding Traf<sup>fi</sup>c congestion

## a b s t r a c t

Recent years have witnessed the rapid development of online auctions. Currently, some online auctions, such as eBay, introduce a proxy bidding policy, under which bidders submit their maximum bids and delegate to a proxy agent to automatically outbid other competitors for the top bidder, whereas other online auctions do not. This paper compares these two widely used auction mechanisms (proxy setting and non-proxy setting) and characterizes the equilibrium bidding behavior and the seller's expected revenue. We <sup>fi</sup>nd the proxy auction outperforms the non-proxy auction in terms of the seller's expected revenue. This dominance result is not prone to the speci<sup>fi</sup>c bid announcement policy, the bidder's knowledge regarding the number of bidders, the impact of traf<sup>fi</sup>c congestion along the bidding process, the number of items sold through the auction, and the existence of a reserve price.

We further <sup>fi</sup>nd that the proxy setting usually fails to sustain the truthful bidding as a dominant strategy equilibrium even if no minimum bid increments are adopted, and the possibility of a low-valuation-bidder dilemma where the low-valuation bidders could be better off if all bidders collude to bid at the last minute. We also discuss the dramatically different equilibrium bidding behaviors under the two auction mechanisms

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Ascending-bid auctions are by far the most prevalent online auction format [20]. Rather than using the “going…going…gone!” procedure of traditional English auctions, eBay, bidz, and many other auction sites introduce a fixed-deadline mechanism, in which bidders submit bids until the end of a <sup>fi</sup>xed time period. In each period, the submitted bids are disclosed/posted on the auction website, and the bidder with the highest bid at the deadline wins the item. In these auction websites, a commonly documented phenomenon is that bidders tend to bid at the last minute. According to [2], “more than 50% of <sup>fi</sup>nal bids are submitted after 90% of the auction duration has passed.” Among them, “25% of the winning bids arrived after 99.8% of the auction time elapsed (the last 8 minutes of a 3-day auction).” This last-minute bidding, also referred to as the sniping behavior, invites the Internet traffic congestion as a majority of bids are submitted simultaneously. Due to the limited bandwidth, some bids may inevitably fail to be successfully transmitted.<sup>1</sup> Such a herding behavior among the bidders and the traf<sup>fi</sup>c congestion that results from the <sup>fi</sup>xed deadline make the Internet auctions deviate from the traditional English auctions.

In order to mitigate the impact of these new features of the modern Internet auctions, some auction websites, such as eBay, introduce the a proxy bidding policy to auctions. According to the auction rule with proxy bidding (hereafter the proxy setting), bidders are allowed to submit their maximum bids, based on which a proxy agent will automatically outbid other competitors until the maximum bid is reached. Thus, equivalently, the winner pays an amount of the second highest bid (plus the minimum bid increment in eBay's practice). This novel setting is intended to restore the desirable feature of the Vickrey auction, see [20]. In an auction mechanism without proxy bidding, a bidder submits a bid in each period and the winner pays her own bid (the highest bid). These two mechanisms are well perceived as the Internet counterparts of the classical single-shot second-price and first-price auctions.

At <sup>fi</sup>rst glance, one may conjecture that the choice of either the proxy or non-proxy setting does not matter from the seller's perspective given the celebrated revenue equivalence theorem ([26]). The central premise of this theorem is that as long as two auction mechanisms employ the same allocation rule and the buyers are risk neutral and possess identically and independently distributed valuations, these two mechanisms should generate exactly the same expected revenue for the seller. Any two auctions that award the object to the bidder with the highest valuation should be revenue equivalent. The two textbook examples of the standard auctions, the <sup>fi</sup>rst-price and second-price auctions, therefore generate the same expected revenue.

However, recent years have witnessed a prevalent trend towards the adoption of the proxy setting. As of 1998, 65 out of 142 online auction sites surveyed by [20] adopted the proxy setting, while more than half of them did not. Nevertheless, as of June, 2009, among more than 30 popular online auction websites we have compared, almost all these auction websites, such as eBay, onSale, uBid, Bidz, Overstock, and others, are currently using the proxy setting. In contrast, some auction websites using the non-proxy setting such as zbestoffer.com and OTWA.com have become inactive. If we were to blindly apply the conventional wisdom to the modern online auction business, we would be unable to explain such a prevalent phenomenon.

This paper intends to provide a rationale of the aforementioned trend towards the proxy setting. Speci<sup>fi</sup>cally, we argue that such revenue equivalence fails to apply to the Internet auctions precisely due to the aforementioned novel features, namely the <sup>fi</sup>xed deadline, bid announcement, and traf<sup>fi</sup>c congestion. These combined novel features essentially induce a discrepancy between the proxy and nonproxy settings in terms of the allocation, even though they both award the object to the highest bidder. We, therefore, are able to establish the advantageous position of the proxy setting over the nonproxy setting from the revenue maximization perspective.

To illustrate our idea, we develop a stylized model in which a riskneutral seller intends to sell a product to a set of risk-neutral buyers. Each buyer desires one unit of product and the corresponding valuation is privately known to the buyer but unknown to the seller and other buyers. Initially, we assume that the seller has only one item (object) for sale, and he has to rely on the existing online auctions. The online auction has pre-determined a (hard) <sup>fi</sup>xed deadline. Each buyer (bidder hereafter) can submit a bid at any given period prior to the deadline, and is allowed to revise her bid in each period. In the end of the auction, the seller awards the object to the bidder with the highest bid, and the bidding history is disclosed/posted at the end of each period. The bids submitted in the last period may get lost in the way due to the Internet traf<sup>fi</sup>c congestion. We exclude the minimum bid increments to make the minimum departure from the classical auction settings in the existing dynamic auction literature.

We show that from the revenue maximization perspective, the proxy setting strictly outperforms the non-proxy setting. The intuition is that the introduction of proxy bidding ensures that bidding the true valuation (immediately) is an equilibrium, and therefore facilitates the desirable allocative ef<sup>fi</sup>ciency. Since the social preference coincides with the auctioneer's incentive in that the ef<sup>fi</sup>cient mechanism also achieves the revenue maximization, the proxy setting is a simple way to ensure such incentive alignment. Furthermore, we <sup>fi</sup>nd that in some cases, the proxy setting fails to sustain the truthful bidding as a dominant strategy equilibrium. Thus, the signature property of the classical single-shot second-price auction disappears in the presence of the <sup>fi</sup>xed deadline, bid announcement, and traf<sup>fi</sup>c congestion. To this end, we construct speci<sup>fi</sup>c instances and “trigger strategies” that allow a bidder's strategy depends on the available information up to date. This in turn creates the contingence on the bidding strategies among different bidders (please see the appendix for details).

Our results suggest that the dynamic bidding environment provides too much leeway for the bidders to mimic, learn, and interact among each other, and capitalize on the publicly available information by cleverly adjusting their own subsequent bids accordingly. Therefore, it is no longer guaranteed to sustain a dominant strategy equilibrium in the most ef<sup>fi</sup>cient $\mathrm { w a y . } ^ { 2 }$ It is also worth noting that we also demonstrate a low-valuation-bidder dilemma where the low-valuation bidders could be better off if all bidders collude to bid at the last minute. Although this dilemma does not alter the above equilibrium feature, it may lead to last-minute bidding if all bidders conceive themselves as having low valuations.

While the bidders are willing to bid their true valuations in the proxy setting, the non-proxy setting fails to sustain a fully revealing equilibrium among the bidders. Due to the traf<sup>fi</sup>c congestion, buyers may attempt to bid earlier to ensure that the bids are transmitted successfully; nevertheless, this also implies that their bids, and henceforth their private valuations, will be disclosed in public prior to the deadline. Such information disclosure along the bidding process triggers bid revisions in the later periods and potentially more intense competition among the bidders. Therefore, the bidders intend to conceal their true valuations, thereby leading to a breakdown of the ef<sup>fi</sup>- cient allocation and a lower expected revenue for the seller. This dominance result may provide a rationale why the majority of existing auction websites are currently employing the proxy setting in contrast to the fact that more than half of them used the traditional non-proxy setting years ago.

We further investigate various alternative setups to evaluate the robustness of this dominance result. We <sup>fi</sup>nd that, the proxy setting continues to dominate the non-proxy setting even when 1) only a partial list of bids are announced, 2) when the total number of bidders is uncertain from each bidder's viewpoint, 3) when the traf<sup>fi</sup>c congestion may arise along the bidding process, 4) when the seller intends to sell multiple items, and 5) when the seller is allowed to set a reserve price. Overall, our results speak to the prevalent adoption of the proxy setting and the competitive advantages of these two auction settings in response to the modern features of Internet auctions. We also discuss some possible scenarios when the non-proxy setting may outperform the proxy setting, including risk attitude, bidders' reluctance to reveal information, and the potential cheating.

The remainder of this paper is organized as follows. Section 2 reviews some relevant literature. Section 3 describes our model setting, including the players' preferences, objectives, and the auction mechanisms. In Section 4, we characterize the equilibrium behavior of the bidders and the seller's expected revenue and compare the auction mechanisms. Section 5 provides some variants of the base model and evaluates the robustness of our results. Section 6 concludes and provides some future directions. All the proofs are relegated to the appendix.

## 2. Literature review

Our paper belongs to a long-standing literature on auction theory, including the seminal paper by [35], the paper on interdependent values by [25], the mechanism design approaches of [22] and [26], the survey by [16], and the recent book by [17]. Auction theory has been applied in the context of internet auctions, including the regular auctions for physical goods [5–7, 14, 27, 30, 33], keywords/search auctions [8, 10, 18, 19, 34], and display advertising auctions [1, 9, 12, 21, 24]. A comprehensive survey on online auctions is referred to [28]. Although this stream of literature is large, auction designs that take into account modern features of online auctions, including the <sup>fi</sup>xed deadline, traf<sup>fi</sup>c congestion, and proxy/non-proxy bidding, are relatively limited.

There have been a lot of papers studying internet auctions with proxy bidding. However, to the best of our knowledge, no prior work has ever compared the performance of the proxy and nonproxy settings. [33] documents the effect of traf<sup>fi</sup>c congestion and relates this effect to the last-minute bidding behavior via experimental data. [37] studies the computational issues faced by the auctioneer in combinatorial auctions with proxy bidding; and presents an alternative algorithm to compute the <sup>fi</sup>nal prices and allocation of items after all proxy bids are collected. [27] presents a continuous-time auction model with proxy bidding and shows that late bidding in a <sup>fi</sup>xed deadline auction can occur at equilibrium in auctions. [38] empirically tests the bidding behaviors on eBay and <sup>fi</sup>nds that the data are better described by ascending auctions rather than real-bid auctions. [32] presents a model to study the effects that the eBay proxy bidding system and the minimum bid increment have on the auction properties. A recent literature review on eBay auctions can be found in [13]. The most related paper to ours is [27]. Our model with proxy setting shares some similarities with theirs in that both models incorporate <sup>fi</sup>xed deadlines and traf<sup>fi</sup>c congestion. From the modeling standpoint, our model differs from theirs as we consider a discrete-time model and assume no minimum bid increment. More importantly, the research questions are radically different. While our paper establishes a uni<sup>fi</sup>ed framework to study and compare the performances between the proxy and non-proxy settings, the non-proxy setting is not studied in [27] and therefore the central topic in our paper has no counterpart in [27].

There are a few papers that consider multiple-period bidding processes for allocating a single object. [3] considers a reverse auction setting in which the bidders bid for multiple periods and the contract is awarded only in the end. Its focus is on how the auctioneer should dynamically adjust the scoring rules, which determine the current winners, to learn the suppliers' cost functions. In contrast, our winner determination rule is constant over time. [4] constructs a dynamically ef<sup>fi</sup>cient allocation rule for a single object among the buyers whose valuations vary over time. Since each buyer exogenously obtains new information in each period, the dynamic allocation rule aims at eliciting the buyers' information and facilitating ef<sup>fi</sup>ciency given the updated information. In contrast, the buyers in our model possess constant valuations and the only source of new information follows from the bid announcements along the bidding process.

## 3. The model

We consider a stylized model in which a seller intends to sell a product to a set of buyers indexed by i, where i=1,…,N. Each buyer desires one unit of product, and, upon receiving it, obtains valuation X . The valuation X is identically and independently drawn from a common distribution function F with the corresponding density function f on 0; v . <sup>½ -</sup>We assume that the valuation X is privately observed by buyer i but unknown to either the seller or any other buyer. Since the valuations {X }'s are identically and independently drawn from a common distribution, the buyers are ex ante symmetric (identical). The assumptions on symmetry and independence are in line with the literature on auctions, see, e.g., [14, 23, 27, 30]. Furthermore, as a buyer's valuation does not depend on the private information of the other buyers, the buyers are said to possess independent private values (IPV) ([17]).

As the seller has no access to the buyers' private valuations, he therefore resorts to conducting an auction in order to sell the product to the buyers. Initially, we assume that the seller has only one item (object) for sale. The cost of producing the product is sunk at the time the seller intends to sell the product to the buyers; thus, it is ignored without loss of generality. Following the convention of the literature on mechanism design and auctions, we assume that the seller and the buyers are risk neutral; thus, the seller's goal is to <sup>fi</sup>nd an appropriate auction mechanism that maximizes his expected revenue. If the seller is able to choose the auction arbitrarily, the auction literature suggests that the optimal mechanism is composed of any standard auction, in which the seller simply requests each buyer to submit a bid, awards the object to the buyer with the highest bid, and sets an optimal reserve price that allows the seller to withhold the object when none of the submitted bids exceed this price ([17]). Nevertheless, in compliance with the common practice, we assume that the seller has to rely on the existing online auctions due to the lack of the ability of conducting such an auction himself.

We assume that the online auction is of the form of English auction with a (hard) <sup>fi</sup>xed deadline. To incorporate the deadline effect, we adopt the discrete time setting; in other words, there are T bid ding periods (rounds). In each period, each buyer can submit a bid and is allowed to revise her previous bid; equivalently, a bidder can submit multiple bids in different periods. For simplicity, we assume the cost for bidders to submit a bid is zero. It can be seen later that the introduction of the bidding cost will not impact our main qualitative result. By adopting the discrete-time setting, we are able to demonstrate in detail how each bidder will adjust her bid subsequently in all the instances. Under this setting, a period is de<sup>fi</sup>ned as a time interval within which each bidder can submit a bid and observe the entire bidding history in previous periods. By increasing the number of total periods T, the time interval in each period can be made suf<sup>fi</sup>- ciently short (e.g., one second) to re<sup>fl</sup>ect the reality. In the end of the auction, the seller (auctioneer) awards the object to the bidder with the highest bid. Ties are broken arbitrarily, and, without loss of generality, we assume that each bidder with the same highest bid wins the object with an equal probability.

We let the reserve price equal zero for simplicity; under this assumption, the seller is committed to sell the object as long as at least one bidder submits a positive bid. Our qualitative results are not prone to this assumption. The scenario with a positive reserve price can be conveniently incorporated by slightly modifying our analysis. (See Section 5 for details.) The entire bidding history is disclosed/posted at the end of each period. In the proxy bidding, each bidder submits her maximum bid to her proxy agent and delegate the agent to automatically outbid other competitors until the maximum bid is reached. Thus, the bidding history in the proxy bidding consists of all the previous bids submitted by the proxy agents rather than the bidders. This assumption is intended to capture the common practice in the online auctions such as eBay auctions. In Section 5, we investigate other alternative scenarios in which the seller only discloses some of the submitted bids.

To incorporate the effect of traf<sup>fi</sup>c congestion in accepting the bids from the Internet, we assume that the bids submitted in the last period (i.e., period T) may get lost in the way with probability ρ, where 0bρb1. This probability corresponds to the common, exogenous transmission failure rate for every bidder (see, e.g., [27] and [29]). This is similar to the “last-minute bid” widely observed and discussed in the recent literature.<sup>3</sup> For simplicity, bids submitted before the last period (the last minute) are successfully transmitted with certainty. In reality, bids might be lost before the last minute; however, these bids can usually be recovered with suf<sup>fi</sup>cient time. The scenario in which bids prior to the last period may fail in transmission is discussed in Section 5.

Our primary goal is to compare two commonly adopted auction mechanisms: proxy and non-proxy settings. In an auction mechanism without proxy bidding, a bidder can submit a bid in each period and the winner pays her own bid (the highest bid). If proxy bidding is allowed, a bidder can simply submit her maximum bid and a proxy agent will automatically outbid other competitors for the top bidder. Thus, with proxy bidding, the winner pays an amount of the second highest bid. In compliance with the current online auction practice, we assume that in the proxy setting, only the current winning payment (i.e., the current second highest bid) is announced, whereas the winning bid remains private. In the non-proxy setting, however, the current winning payment coincides with the current winning bid.

To illustrate the major difference between these two auction mechanisms, suppose that \$100 and \$80 are the top two bids and the auction ends in this period. In either mechanism, \$100 is the winning bid. The winner pays \$80 in the auction with proxy bidding, but pays \$100 in the auction without proxy bidding. Furthermore, in the proxy setting, the payment by the winner, \$80, is announced, whereas in the non-proxy setting \$100 is disclosed to the public. Thus, if we augment an additional bidding period after this period, in the proxy setting, the bidders other than the current winner only know that currently the second-highest bid is \$80 but are unsure of the current winning bid. In contrast, all bidders observe the current winning bid \$100 and the amount they have to increase their bids to outbid the current winning bid in the non-proxy setting.

In both proxy and non-proxy settings, each bidder is allowed to submit a bid in each period, and the entire bidding history in the previous periods are disclosed publicly according to the auction rule. Thus, a bidding strategy should specify a complete bidding pro<sup>fi</sup>le that depends on the past history. Due to this dynamic structure, an appropriate solution concept is the perfect Bayesian equilibrium that consists of the bidders strategies and beliefs along the bidding process. A perfect Bayesian equilibrium requires that bidder i updates her belief correctly based on the history, and the equilibrium bidding strategy in each period is the best response given the history and her updated belief.

## 4. Equilibrium analysis

In this section, we investigate the bidders' equilibrium bidding strategies and the seller's expected revenues under different auction mechanisms.

## 4.1. Proxy setting

We <sup>fi</sup>rst consider the proxy setting in which each bidder is allowed to submit a proxy bid in any period. Let $\{ ( b _ { i j } ) , j = 1 , . . . , T \}$ denote the (proxy) bid pro<sup>fi</sup>le submitted by bidder i in T periods. According to the auction mechanism, the seller awards the object to the bidder who successfully submits $b _ { m a x } = b _ { i j } \equiv m a x _ { i , j } \{ b _ { i j } \}$ , and the payment is determined by the second highest bid $m a x _ { \{ ( i , j ) \neq ( i ^ { * } j ^ { * } ) \} } \{ b _ { i j } \}$

Our <sup>fi</sup>rst result proves that each bidder can simply claim her true valuation as the proxy bid in this sequential auction.

Proposition 1. In the proxy setting, bidding the true valuation at the beginning is a symmetric equilibrium. The corresponding seller's expected revenue is

$$
\Pi = N \int_ {0} ^ {\bar {v}} (N - 1) x (1 - F (x)) F ^ {N - 2} (x) f (x) d x.
$$

Proposition 1 shows that it is optimal for bidders to bid truthfully right at the beginning of the auction. Equivalently, each bidder can choose to bid her true valuation in any period prior to the last period (last minute). This is because as long as her proxy bid is successfully submitted to the auction, a bidder does not care about when the bid is submitted. A rather subtle point here is that in the proxy setting, the information disclosed along the bidding process does not affect the bidders' best responses. This result is reminiscent of the classical result in the (single-shot) second-price auction ([35]). Moreover, this result also echoes [27], where they show that no bidder can be better off by bidding only at the last period if all other bidders bid their true valuations in the earlier periods.

Note that the equilibrium described in Proposition 1 is generally not the unique perfect Bayesian equilibrium. In fact, the multiplicity of equilibria is widely observed in various auction settings. Nevertheless, following the mechanism design literature, our primary research question is whether information asymmetry is a barrier against ef<sup>fi</sup>cient allocation, and how information asymmetry may result in some materialistic social inef<sup>fi</sup>ciencies. Thus, it seems a nomenclature rather than an exception to focus on the most appealing equilibrium. This viewpoint is also applicable to all kinds of principal-agent problems. While some incentive compatibility and individual rationality constraints are binding at optimality, the agents certainly can deviate to choose the wrong contracts/actions without being worse off. Nevertheless, obeying the principal's expectation of choosing the right contract remains an equilibrium.

It is worth mentioning that, in contrast to the single-shot secondprice auction, the equilibrium characterized in Proposition 1 is not always a dominant strategy equilibrium. Furthermore, we <sup>fi</sup>nd that as long as there are more than three bidding periods, no dominant strategy exists in the proxy setting. We summarize the results in the following proposition.

Proposition 2. In the proxy setting,

• When T=2 and $\rho { < } \frac { E ( X ) } { \overline { { \nu } } + E ( X ) } ,$ where E(X) and v are the common <sup>þ ð Þ</sup>expected and maximal valuation for each bidder respectively, then bidding the true valuation at the beginning is not a dominant strategy equilibrium.<sup>4</sup>

• When $T \geq 3 ,$ , there does not exist any dominant strategy equilibrium.

Proposition 2 implies that the signature property of the classical single-shot second-price auction disappears in the presence of the <sup>fi</sup>xed deadline, bid announcement, and traf<sup>fi</sup>c congestion. Consequently, the optimality of bidding the true valuation under proxy setting can only be justi<sup>fi</sup>ed when all other bidders also bid their true valuations; otherwise, it may be suboptimal for a bidder to bid her true valuation. To break down the dominance of bidding the true valuation, and more generally any potential dominant strategy equilibrium when there are more than three periods, we construct speci<sup>fi</sup>c instances and “trigger strategies” that allow a bidder's strategy depends on the available information up to date. This in turn creates the contingence on the bidding strategies among different bidders. Our results suggest that the dynamic bidding environment provides too much leeway for the bidders to mimic, learn, and interact between each other, and capitalize on the publicly available information by cleverly adjusting their own subsequent bids accordingly. Therefore, it is no longer guaranteed to sustain a dominant strategy equilibrium in the most ef<sup>fi</sup>cient way. This is in strict contrast with the common belief (e.g., [20]) and the claims by some leading online auction websites (e.g., eBay).

However, the proxy setting may sometimes make the truthful bidding a dominant strategy, as demonstrated in the following proposition.

Proposition 3. In the proxy setting, when $T { = } 2 a n d \rho ^ { N - 1 } { + } \rho { \geq } 1$ , bidding the true valuation at the beginning, i.e., the first period, is a (weakly) dominant strategy for each bidder.

Next, we use a simple example to illustrate Proposition 1 and demonstrate an interesting phenomenon that some bidders could be better off if all bidders could “collude” to bid only at the last minute.

## 4.1.1. An example

Consider the proxy setting with two periods and two bidders. In such a scenario, a bidder has two options: 1) participating in the second period and bidding her true valuation (Strategy I), and 2) bidding her true valuation in the <sup>fi</sup>rst period (Strategy II). Without loss of generality, we take bidder 1's perspective. We assume that her valuation is x and let y denote bidder 2's valuation.<sup>5</sup> Table 1 describes bidder 1's expected payoff under different strategy pro<sup>fi</sup>les.

Table 1  
Bidder 1's expected payoffs.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Bidder 2</td></tr><tr><td>I</td><td>II</td></tr><tr><td rowspan="2">Bidder 1</td><td>I</td><td> $(1-\rho)((1-\rho)Pr(y\( <x$ ) $[x-E[y|y\( <x$ ]+ $\rho x$ )</td><td> $(1-\rho)Pr(y\( <x$ [ $x-E[y|y\( <x$ ]</td></tr><tr><td>II</td><td> $(1-\rho)Pr(y\( <x$ )[ $x-E[y|y\( <x$ ]+ $\rho x$ )</td><td> $Pr(y\( <x$ [ $x-E[y|y\( <x$ ]</td></tr></table>

Table 2  
Bidder 1's payoff given x= 0.6.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Bidder 2</td></tr><tr><td>I</td><td>II</td></tr><tr><td rowspan="2">Bidder 1</td><td>I</td><td>0.21</td><td>0.11</td></tr><tr><td>II</td><td>0.35</td><td>0.18</td></tr></table>

From Proposition 1, Strategy II is the equilibrium strategy for both bidders. Nevertheless, it is possible that a bidder with low valuation is better off if both bidders submit the bids only in the last period $( \mathrm { i } . \mathrm { e } . , \{ I , I \} )$ , which is referred to as “low-valuation bidder dilemma.” This occurs when

$$
(1 - \rho) \{(1 - \rho) P r (y <   x) [ x - E [ y | y <   x ] ] + \rho x \} > P r (y <   x) [ x - E [ y | y <   x ] ],
$$

which holds when $P r ( y < x ) < \frac { 1 - \rho } { 2 - \rho } .$ . On the other hand, this dilemma does <sup>ð Þ</sup>not arise for a bidder with high valuation; more precisely, a bidder prefers {II, II} to {I, I} as long as $P r ( y < x ) \left( { \frac { 1 - { \dot { E } } [ y | y < x ] } { x } } \right) > { \frac { 1 - \rho } { 2 - \rho } } .$

<sup>ð Þ</sup>Let us now provide some more numerical examples to demonstrate this result. Suppose the valuation follows from a uniform distribution U[0, 1] and the failure rate is ρ=0.4. We consider two possible instances for bidder 1's valuations: x=0.6, and x=0.8. The bidder 1's expected payoffs are given in Tables 2 and 3. In Table 2, bidder 1 faces the “low-valuation-bidder dilemma” since $0 . 2 1 { > } 0 . 1 8 ,$ , whereas such a dilemma disappears when x=0.8 (as demonstrated in Table 3). Note also that from both tables, strategy II is the optimal strategy for bidder 1 (and for bidder 2 by symmetry).

To understand why such a dilemma may arise, note that if all bidders bid only in the last period, the competition among the bidders can be mitigated due to the traf<sup>fi</sup>c congestion. Since some bids may not be transmitted successfully, if a bidder's bid gets into the auction, she wins with a higher probability (which happens when all those bids higher than hers lose in the way); moreover, the winner is likely to pay less (because the supposed second highest bid may not be submitted successfully). On the other hand, a bidder may incur a potential utility loss if she could have won the auction were her bid submitted successfully. The <sup>fi</sup>rst two driving forces work in favor of a bidder's bene<sup>fi</sup>t, whereas the last force indicates the downside of bidding in the last period. Notably, a high-valuation bidder is more concerned about the traf<sup>fi</sup>c congestion because she is more likely to win; thus, she is less inclined to collude for the last period submission. On the contrary, a lowvaluation bidder bene<sup>fi</sup>ts more from the (potential) collusion since her chance is slim under the severe competition.

The low-valuation-bidder dilemma partially shares a similar feature of the famous Prisoner's Dilemma: The low-valuation bidders intend to bid before the last minute in equilibrium, but they can be worse off by doing so. The intuition behind this low-valuationbidder dilemma is that the low-valuation bidders have a lower chance of winning the auction if all bidders bid at the beginning; while they will have a higher chance if all bidders bid only at the last minute due to the traf<sup>fi</sup>c congestion.

Table 3  
Bidder 1's payoff given x=0.8

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Bidder 2</td></tr><tr><td>I</td><td>II</td></tr><tr><td rowspan="2">Bidder 1</td><td>I</td><td>0.31</td><td>0.19</td></tr><tr><td>II</td><td>0.51</td><td>0.32</td></tr></table>

Having obtained the equilibrium bidding strategies and the seller's expected revenue in the proxy setting, we next turn to the non-proxy setting.

## 4.2. Non-proxy setting

When the proxy bidding is unavailable, each bidder is requested to submit a bid in each period, and the payment coincides with the winning bid. Thus, the non-proxy bidding is similar to a dynamic first-price auction in which the single object is awarded only in the end with the possible last-period traf<sup>fi</sup>c congestion (this analogy is also mentioned in [20]). Note that the game involves multiple periods of strategic interactions among the bidders and each bidder possesses private information regarding her own valuation, the appropriate solution concept is perfect Bayesian equilibrium ([11]).

In the following we shall only consider symmetric equilibria: an equilibrium in the non-proxy setting is said to be symmetric if every bidder adopts the same bidding function, i.e., $\beta _ { i t } ( x _ { i } , h _ { t } ) \equiv \beta _ { t } ( x _ { i } , h _ { t } )$ $\forall i { \in } \{ 1 , . . . , N \}$ . Furthermore, we are particularly interested in the pure-strategy equilibrium that facilitates ef<sup>fi</sup>cient allocation (i.e., the object is awarded to the bidder with the highest valuation). Ef<sup>fi</sup>ciency is de<sup>fi</sup>nitely a desirable property from the social surplus standpoint, and this is guaranteed in the proxy setting as we have demonstrated in Proposition 1.<sup>6</sup> However, our next proposition ends the hope if the bidding process is under the in<sup>fl</sup>uence of traf<sup>fi</sup>c congestion.

Proposition 4. In the non-proxy setting, when $\rho { \in } ( 0 , 1 )$ , there does not exist an equilibrium that leads to efficient allocation.

In the proof of Proposition 4, we show that in order to facilitate ef-<sup>fi</sup>cient allocation, it is necessary that the bids prior to the last period fully reveal the bidders' true valuations. However, this cannot be sustained as an equilibrium, as some bidder has an incentive to outbid others in the last period. Proposition 4 also suggests that we should instead look for either a partially pooling equilibrium in which bidders with heterogeneous valuations submit identical bids or even a mixed-strategy equilibrium in which a bidder randomizes her bid to avoid direct information revelation. In both cases, the allocation cannot be ef<sup>fi</sup>cient. If bidders with heterogeneous valuations pool together, the seller may occasionally award the object to a bidder whose valuation is not the highest; on the other hand, in a mixed-strategy equilibrium, a bidder with the highest valuation may be outbid given the randomized bids.

It is worth mentioning that this result is in strict contrast with [36], where he considers a setting with repeated <sup>fi</sup>rst-price auctions in which the seller has multiple units to sell, each bidder desires at most one unit, and only the winning bids are disclosed after each period. This peculiar model setup ensures that a bidder's private information is disclosed only when she no longer participates in the subsequent auctions (because in that case she has won one object and has left the game); consequently, a symmetric, pure-strategy equilibrium that fully reveals the bidders' true valuations exists.

Note that this inef<sup>fi</sup>ciency vanishes if the traf<sup>fi</sup>c congestion is absent: when the bids in the last period are always transmitted successfully, each bidder can simply wait until the last period. In this way, the non-proxy setting behaves as a (one-shot) <sup>fi</sup>rst-price sealed-bid auction, which has been well known to guarantee the allocative ef<sup>fi</sup>ciency (e.g., [17]). Thus, we conclude that the traf<sup>fi</sup>c congestion is the focal reason that makes the Internet non-proxy setting depart from the classical auction theory. This result also implies that blind adoption of the conventional wisdom may jeopardize one's business in the Internet era. On a related note, such a last-period (last-minute) traf<sup>fi</sup>c congestion also degenerates were there no <sup>fi</sup>xed deadline (e.g., the “going… going…gone!” mechanism). Our results suggest that the proxy bidding is more likely to be bene<sup>fi</sup>cial (from the ef<sup>fi</sup>ciency perspective) when the auction intermediary adopts a hard deadline.

Having discussed the equilibrium bidding behaviors in the two mechanisms, we next compare their performance in terms of the seller's expected revenue.

## 4.3. Comparison

Now we are ready to present our comparison result. We <sup>fi</sup>nd that the revenue comparison between the proxy and non-proxy settings can be unambiguously determined.

Proposition 5. The seller obtains a higher expected revenue from the proxy setting than from the non-proxy setting.

Proposition 5 shows that from the revenue maximization perspective, the proxy setting outperforms the non-proxy setting. This dominance result provides the rationale why most of popular auction websites such as eBay and OnlineAuction.com are currently adopting the proxy setting. The intuition is that the introduction of proxy bidding guarantees the allocative ef<sup>fi</sup>ciency. Without the reserve price, the social preference coincides with the auctioneer's incentive in that the ef<sup>fi</sup>cient mechanism also achieves the revenue maximization. Thus, the proxy setting is a simple way to ensure such incentive alignment.

Note that according to the revenue equivalence theorem, if there were no <sup>fi</sup>xed deadline and traf<sup>fi</sup>c congestion, any standard auction could be adopted for revenue maximization. However, when the traf<sup>fi</sup>c congestion is in effect, the non-proxy setting fails to sustain a fully revealing equilibrium among the bidders, thereby leading to a breakdown of the ef<sup>fi</sup>cient allocation. This suggests that the proxy setting is more likely to be bene<sup>fi</sup>- cial (from both the perspectives of revenue maximization and the allocative ef<sup>fi</sup>ciency) when the auction intermediary adopts a hard deadline.

While this dominance result is remarkably strong, a natural question is whether this follows from the speci<sup>fi</sup>c choice of our model characteristics. In the next section, we investigate how alternative assumptions may (or may not) alter the ranking over different settings.

## 5. Discussions and extensions

In this section, we consider several variants of our basic model and demonstrate that our dominance result is robust against various modi<sup>fi</sup>cations of our model characteristics.

## 5.1. Alternative bid disclosure policies

In our model, we assume that all bids are announced after each period. This assumption is intended to capture the common practice such as eBay, OnlineAuction.com, and Overstock.com Auction. However, there are other situations in which only a partial list of bids are announced. In theory, there can be a huge number of possible bid announcement policies. Nevertheless, our dominance result is not prone to the speci<sup>fi</sup>c bid announcement policy. This is because in the proxy setting, bidding the true valuation (at the beginning) remains the equilibrium strategy irrespective of the information disclosure over time. Thus, the (constrained) ef<sup>fi</sup>ciency continues to hold, and the second-price feature is not altered by the bid announcement policy. In the non-proxy setting, however, the equilibrium behavior is sensitive to the dynamic information disclosure. Although we do not attempt to characterize the equilibrium behavior, it can be veri<sup>fi</sup>ed that with alternative bid announcement policies, a symmetric, fullyrevealing, pure-strategy equilibrium is hard to sustain because each bidder is concerned about the potential disclosure of her private information. Thus, either the pooling phenomenon arises or the bidders randomize their bids. In both cases, the allocative ef<sup>fi</sup>ciency is not guaranteed; consequently, the proxy setting continues to outperform the non-proxy setting.

## 5.2. Stochastic number of bidders

In reality, each bidder is unable to observe the total number of bidders in the system. Moreover, in reality, there may be new arrivals that participate in the auction after the auction has been started. These are the two possible sources of the “stochastic number of bidders” from a bidder's perspective. Let us <sup>fi</sup>rst start with the case in which all the bidders arrive at the beginning. In the proxy setting, the uncertainty does not affect the bidders' strategies: it is still an equilibrium strategy to bid the true valuation at the beginning. Thus, allocative ef<sup>fi</sup>ciency is guaranteed for every instance; consequently, the proxy setting outperforms all other mechanisms, including the non-proxy setting. When there are new arrivals along the bidding process, as long as these new bidders arrive before the last period, they are able to submit a successful bid to the system and therefore the object will be awarded to the bidder with the highest valuation. This assumption is plausible if one regards the last period as the last minute. In principle, the last minute should be suf<sup>fi</sup>ciently short for the traf<sup>fi</sup>c congestion to be effective. Our result thus implies that the proxy setting gives rise to a higher expected revenue for the seller than any other setting (including the non-proxy setting studied in our paper).

## 5.3. Traffic congestion along the bidding process

In our model, we assume that the traf<sup>fi</sup>c congestion occurs only in the last period (last minute) to capture the practical Internet collision. This phenomenon is also reported in [27]. Of course, the bids submitted in earlier periods may also get lost in other periods if the Internet traf<sup>fi</sup>c is overloaded occasionally. A natural question is, therefore, how does our result change if the traf<sup>fi</sup>c congestion also arises in periods prior to the last period? In such a scenario, the ef<sup>fi</sup>cient allocation is still guaranteed as long as each bidder is able to successfully submit her bid sometime along the process; moreover, following our argument, bidding the true valuation remains an equilibrium strategy because this result is insensitive to whether the bids can be transmitted successfully or not. On the other hand, since with certain probability the bids submitted in the early periods will be disclosed, in the non-proxy setting, the threat of information disclosure remains. Consequently, it is dif<sup>fi</sup>cult to sustain a pure-strategy fully revealing equilibrium in the non-proxy setting, thereby leading to a lower expected revenue for the seller (compared to that in the proxy setting).

Another possible extension is that the transmission rate may depend on the number of submitted bids. This assumption may be more realistic in the situations in which the traf<sup>fi</sup>c congestion mainly arises from the limited computing power of the auction sites' servers. On the contrary, our basic setting is more appropriate when traf<sup>fi</sup>c congestion, more broadly captures the Internet bandwidth from the bidders' side to the auction website. On the contrary, in the nonproxy setting, each bidder suffers from the potential lost bid if she waits until the last period, and is concerned about the information disclosure along the bidding process. Thus, following our argument, a fully revealing equilibrium cannot be sustained even when the transmission rate depends on the number of submitted bids, thereby giving rise to a more advantageous position for the proxy setting from the revenue maximization perspective.

## 5.4. Multiple items

In our model setting, the seller intends to sell only one unit as in the case of eBay.<sup>7</sup> However, in other auction websites such as uBid, the seller is allowed to list multiple identical items (e.g., one book, one cellphone, one microwave, etc.). Note that even if the seller intends to sell multiple identical items, each bidder desires at most one unit.<sup>8</sup> This corresponds to the “single-unit demand” assumption in the auction theory.

When a seller intends to sell multiple (m) items through an auction, the proxy bidding scheme shall work as follows. Suppose that the bidder submits a (maximum) bid, and the proxy agent submits the bid on behalf of the bidder to outbid other bidders to ensure that her bid is within the top m bids. Thus, the proxy agent is competing against the highest losing (m+1)st bid in each period. In this proxy setting with single-unit demand, it can be veri<sup>fi</sup>ed that bidding the true valuation remains an equilibrium strategy; consequently, the ef<sup>fi</sup>ciency is guaranteed. Moreover, a modi<sup>fi</sup>ed version of the revenue equivalence theorem applies to this multiple-item auction. Thus, the proxy setting yields the highest expected revenue for the seller among those mechanisms for which the seller must sell the object, with the non-proxy setting being one example. The proof essentially follows exactly the same argument in the proof of Proposition 5. Note that the close connection between the mechanism designs for the multi-unit auctions and the single-unit auctions has been established in [22], and thus we refer the interested readers to it for details.

## 5.5. Reserve price

We have so far ignored the possibility of using the reserve price. In many auctions, the seller is allowed to set a reserve price for the auction, in which case the seller can withhold the object if none of the submitted bids exceeds the reserve price. In some auctions, bidders are not allowed to initiate the bidding process by submitting a bid below a pre-speci<sup>fi</sup>ed reserve price. How does our dominance result fare with the introduction of the reserve price? If we ignore the additional charge the auction website requests from the seller for setting a reserve price, the revenue-maximizing mechanism characterized by [26] can be implemented by a second-price auction with an appropriately chosen reserve price. Thus, the proxy setting allows the seller to maximize his expected revenue when he is allowed to set the optimal reserve price. This implies that the dominance result is insensitive to the possibility of employing a reserve price. Moreover, this revenue maximization result continues to work when the seller is allowed to sell multiple items in one auction. Thus, we conclude that all our results are unaffected by the introduction of the reserve price. Of course, if the seller accidentally chooses a suboptimal reserve price, our results do not apply and no unambiguous revenue ranking can be obtained.

## 5.6. Single-period auctions

A special case of our model is that the buyers are allowed to bid only once, i.e., T=1. This alternative setting may be appropriate when the duration of the auction is suf<sup>fi</sup>ciently short or when the bidders are ignorant regarding the possibility of revising their bids. In such a scenario, the threat of information disclosure vanishes because the bidders have no chance to respond to other bidders' bids. Our goal here is to demonstrate the dramatically different bidding behavior in the non-proxy setting. We summarize our results in the following proposition.

Proposition 6. Suppose the buyers are allowed to submit the bids only once. Then

• In the proxy setting, bidding the true valuation remains the equilibrium strategy for each bidder; however, the allocation may be inefficient.

• In the non-proxy setting, there exists a symmetric, fully revealing equilibrium with a monotonic bidding function.

• These two settings are revenue equivalent.

In the presence of traf<sup>fi</sup>c congestion, it is still optimal for the bid ders to bid their true valuations in the proxy setting, since this incentive is not prone to the number of bidders or whether the bid will be transmitted successfully. However, the allocation may be inef<sup>fi</sup>cient, since the bid of the highest bidder may not enter the system successfully. In the non-proxy setting, because the bidders are not concerned about the bid disclosure, we are able to establish a fully-revealing equilibrium despite the traf<sup>fi</sup>c congestion. As the bidding function is monotonic, among the bidders who successfully submit their bids, the seller awards the object to the bidder with the highest valuation. Thus, the allocations in the proxy and non-proxy settings are equivalent in every instance (sample-path-wise equivalent). We can then invoke the revenue equivalence theorem to show that these two settings yield the same expected revenue for the seller.

## 5.7. When may the non-proxy setting be adopted?

Given the dominance result in our paper, an immediate question that arises is: is it possible that the non-proxy bidding outperforms the proxy bidding under some scenarios? In the following we discuss some possible scenarios when the non-proxy bidding may outperform the proxy bidding.

## 5.7.1. Risk attitude

In our model, we assume that all the players, including the seller and the bidders, are risk neutral following the convention of the auction literature. However, in reality, they might exhibit other risk attitudes. When the bidders are risk averse, the comparison between the proxy and non-proxy settings becomes more involved. On one hand, bidders may incur some disutility in the proxy setting because the payment is uncertain from a winner's perspective. Such a random payment may dissuade the bidders from submitting a high bid ex ante. In contrast, in the non-proxy setting, the winner has the discretion of determining her payment, namely, her own winning bid. This force works in favor of the non-proxy setting. On the other hand, the allocative ef<sup>fi</sup>ciency is preserved in the proxy setting even when the bidders are risk averse, thereby making the proxy setting advantageous compared to the non-proxy setting. It is conceivable that when the bidders are extremely averse to the uncertainty, the nonproxy setting may outperform the proxy setting.

The seller's risk attitude certainly affects how she ranks these two settings as well. As is documented in the existing literature, the payment in the (single-shot) second-price auction is a mean-preserving spread of that in the <sup>fi</sup>rst-price auction; therefore, a risk-averse seller prefers the <sup>fi</sup>rst-price auction to the second-price auction even though the payoffs are equivalent ([17]). Since these single shot auctions are analogous to the proxy and non-proxy settings, we expect that the non-proxy setting is more likely to be preferred when the seller is more risk averse.

## 5.7.2. Reluctance to reveal information

Some psychological effects may also affect the outcomes of the auctions. While it is well-known that bidding the true valuation is the dominant strategy in the second-price type of auctions, in reality bidders are generally reluctant to reveal their true valuations to the auctioneer. This phenomenon is typically perceived to be the consequence of the bidders' irrationality/bounded rationality, but such a concern appears to be very natural in practical situations. The non-proxy setting is not exposed to this threat of information revelation; consequently, a boundedly rational bidder may deviate further from the theoretically optimal strategy in the proxy setting compared to the non-proxy setting, thereby leading to the preference towards the non-proxy setting.

## 5.7.3. Cheating

Sometimes the internet auctions are not perfectly transparent and thus there might be room for manipulation. For example, since each bidder are represented by an internet ID rather than a person that other bidders are able to see physically, it may be relatively easy for the seller or the auction website to insert some fake/shadow bidders. In the proxy setting, such a threat is particularly in<sup>fl</sup>uential, because the payment is determined by the highest losing bid ([20]). Bid takers (either the seller or the auction website) may then submit some false bids to realize a higher revenue. Also, the second-price type auction is also vulnerable to the collusive behavior such as the conspiracies by the bidders ([31]). As the bidders collude and submit the bids jointly, the seller may be unable to extract revenue from the bidders. On the contrary, collusion is less likely to arise in the <sup>fi</sup>rst-price type auction. This may make the nonproxy setting more desirable than the proxy setting.

## 6. Concluding remarks

We consider a model in which a seller intends to sell a product through an online auction to a set of buyers with private valuations. The online auction has pre-determined a (hard) <sup>fi</sup>xed deadline and is subject to traf<sup>fi</sup>c congestion that may result in transmission failure. We show that from the revenue maximization perspective, the proxy setting outperforms the non-proxy setting, which may provide a rationale for the prevalent use of the proxy setting. We further show that our results are robust against the speci<sup>fi</sup>c bid announcement policy, the bidder's knowledge regarding the number of bidders, the impact of traf<sup>fi</sup>c congestion along the bidding process, and the number of items sold through the auction. Overall, our results speak to the prevalent adoption of the proxy setting and the competitive advantages of these two auction settings in response to the modern features of Internet auctions.

Our results can be extended in various ways. A challenging extension would be to consider the interdependence of valuations among bidders. In such a scenario, a bidder's true valuation depends not only on her own signal, but also on the private information of other bidders. This interdependence makes the information disclosure along the bidding process extremely intriguing, because each bidder is able to adjust/update her estimation of her own valuation as the bidding goes along. For example, if a bidder drops from the auction, each bidder may conjecture that bidder's private information and consequently update how she should regard this object. The strategic interaction with interdependent valuations is certainly a research priority.

Moreover, there are many alternative models for the bidders' behaviors in online auctions. While this paper aims at providing a fresh look into the auctions with traf<sup>fi</sup>c congestion and proxy/non-proxy setting, there are certain other issues that cannot be incorporated in this single model. In reality, bidders may be categorized into different groups, thereby breaking down the symmetry assumption used in this paper (and in the majority of the auction literature). For example, bidders may be risk-neutral/seeking/averse, may possess different precision of information regarding the quality of the object, may exhibit different time preferences,<sup>9</sup> and may be endowed with different degrees of (bounded) rationality. Therefore, psychology and behavioral economics could be a new venue to explain the online bidders' behaviors. These complicated bidders' behaviors certainly are crucial for the design of online auctions, but are left as an open venue for future research.

## Acknowledgments

We thank Andrew Whinston (the Editor-in-Chief) and the review team for their detailed comments and many valuable suggestions that have signi<sup>fi</sup>cantly improved the quality of the paper. We have also bene<sup>fi</sup>ted from the discussions with Tsung-Sheng Chang, Chia-Hui Chen, Xiuli Chao, Wen-Chyuan Chiang, De Liu, Joshua Schumm, Zhixi Wan, Peter R. Wurman, and the conference participants at INFORMS 2005. The <sup>fi</sup>rst author also acknowledges support from the National Science Foundation (NSF) through Grant CMMI-0927591 and NSF China (70972046, 71172039, 71171074). All the remaining errors are our own.

## Appendix

Proof of Proposition 1. Let us focus on a speci<sup>fi</sup>c bidder i and assume that every other bidder follows the equilibrium strategy, i.e., bidding the true valuation at the beginning. Assume the true valuation of bidder k is $x _ { k } , k = 1 , . . . , N .$ . To prove the proposition, it suf<sup>fi</sup>ces to consider the truthful bid pro<sup>fi</sup>le $( x _ { i } , 0 , . . . , 0 )$ and an arbitrary bid pro<sup>fi</sup>le $\{ ( b _ { i j } ) .$ $j { = } 1 , . . . , T \}$ . Following the truthful bidding, the bidder obtains $x _ { i } -$ $m a x _ { k \neq i } \{ x _ { k } \}$ } if $x _ { i } { \geq } m a x _ { k \neq i } \{ x _ { k } \}$ , and obtains 0 otherwise. By using the alternative bid pro<sup>fi</sup>le, the bidder's payoff is $x _ { i } - m a x _ { k \not = i } \{ x _ { k } \}$ if $m a x _ { j = 1 , . . . , T - 1 } \{ b _ { i j } \} { \geq } m a x _ { k \neq i } \{ x _ { k } \}$ or $b _ { i T } { \geq } m a x _ { j \neq i } \{ x _ { j } \}$ and $b _ { i T }$ is transmitted successfully, and is zero otherwise.

When $\iota _ { i } \geq m a x _ { k \neq i } \{ x _ { k } \}$ , the bidder is supposed to win under truthtelling and obtains a positive net payoff. However, if she adopts the alternative bid pro<sup>fi</sup>le, she may lose with some probability; more speci<sup>fi</sup>cally, this occurs when $m a x _ { j = 1 , . . . , T } \{ b _ { i j } \} { < } m a x _ { k \neq i } \{ x _ { k } \}$ or $b _ { i T } { \geq } m a x _ { k \neq i } \{ x _ { k } \}$ but $b _ { i T }$ fails to be transmitted. On the other hand, when $x _ { i } { < } m a x _ { k \neq i } \{ x _ { k } \} ,$ , the bidder is supposed to obtain a null payoff under truth-telling, but she may win and obtains a negative payoff occasionally upon adopting the alternative bid pro<sup>fi</sup>le. Neither case is in favor of the alternative bid pro<sup>fi</sup>le. Thus, we conclude that no bidder has an incentive to deviate from the equilibrium.

It is straightforward to verify that bidder i receives exactly the same payoff while adopting arbitrary bid pro<sup>fi</sup>le for the remaining periods is optimal as long as $b _ { i 1 } = x _ { i }$ and $b _ { i j } \leq x _ { i } , \forall j = 2 , . . . , T .$ . Given this, the corresponding seller's expected revenue follows immediately from the existing auction literature (e.g., [17]). □

Proof of Proposition 2. We divide the analysis into two cases.

$$
\text { Case   1. } T = 2 \text { and } \rho <   \frac {E (X)}{\overline {{v}} + E (X)}:
$$

Since a dominant strategy equilibrium requires the equilibrium strategy be a dominant strategy for each bidder, thus to complete the proof, it suf<sup>fi</sup>ces to show that under the speci<sup>fi</sup>ed condition, bidding the true valuation at the beginning is not a dominant strategy for each bidder. To this end, we construct as follows a pro<sup>fi</sup>le of the other bidders' bidding strategies under which bidding the true valuation at the beginning is not dominant for a speci<sup>fi</sup>c bidder i.

Suppose bidder i's true valuation is x (0 x v) and all the other bidders adopt the following “trigger” strategy: “do not bid in period one; in period two, if bidder i submits a (positive) bid in period one, then bid the true valuation; otherwise, do not bid.” Note that this trigger strategy is implementable, since before submitting their second bids, all the other bidders have known whether bidder i submitted a bid in the <sup>fi</sup>rst period.

Under above trigger strategy for the other bidders, the expected payoff of bidding the true valuation at the beginning for bidder i is

$$
\sum_ {k = 0} ^ {N - 1} \binom {N - 1} {k} \rho^ {N - 1 - k} (1 - \rho) ^ {k} E (x _ {i} - Y _ {k}) ^ {+},
$$

where $Y _ { k }$ is the maximal valuation of the k bidders who successfully submit their bids in period two. Note that this payoff is decreasing in $N \ ( \geq 2 )$ and thus is less than $\rho x _ { i } + ( 1 - \rho ) E ( x _ { i } - X ) ^ { + }$ , where X is the common random valuation with distribution F. However, when bidder i does not bid in period one and bids true valuation in period two, her expected payoff becomes $( 1 - \rho ) x _ { i }$ . When $\rho { < } \frac { E ( X ) } { \overline { { \nu } } + E ( X ) } ,$ , it can be easily veri<sup>fi</sup>ed that $\rho x _ { i } + ( 1 - \rho ) E ( x _ { i } - X ) ^ { + } < ( 1 - \rho ) x _ { i }$ <sup>þ ð Þ</sup>. Thus, bidding the true valuation in period one yields a lower expected payoff than the latter strategy for bidder i, which breaks down the dominance of bidding the true valuation at the beginning.

## Case 2. T≥3:

Let us again focus on a speci<sup>fi</sup>c bidder i and suppose her <sup>fi</sup>rst bid is $b _ { i 1 } \left( \geq 0 \right)$ . In the following we show that there does not exist any dominant strategy regardless of whether $b _ { i 1 }$ is positive or not.

We <sup>fi</sup>rst consider the case when $b _ { i 1 } = 0 .$ . In this case, suppose all the other bidders adopt the following bidding strategy: “bid zero in period one; in the remaining $T - 1$ periods, if bidder i bids zero in the <sup>fi</sup>rst period, then always bid the true valuation; otherwise, always bid $z { \mathrm { e r o . } } ^ { \prime \prime }$ Given that all the other bidders follow this strategy and $T \geq 3 ,$ it is obviously not optimal for bidder i to bid zero in period one, since bidding nonzero instead eliminates the competition. Thus, $b _ { i 1 } = 0$ never constitutes a dominant strategy.

Now consider the case when $b _ { i 1 } > 0$ . In this case, suppose all the other bidders adopt the following bidding strategy: “do not bid in period one; in the remaining $T - 1$ periods, if bidder i submits a (positive) bid in the <sup>fi</sup>rst period, then always bid the true valuation; otherwise, always do not bid.” Given that all the other bidders follow this strategy and $T { \geq } 0 ,$ submitting a bid in period one is suboptimal for bidder i as well. Thus, $b _ { i 1 } > 0$ never constitutes a dominant strategy either. Collectively, we <sup>fi</sup>nd that it is impossible to <sup>fi</sup>nd a $b _ { i 1 }$ to constitute a dominant strategy, and therefore no dominant strategy equilibrium exists when $T 2 3 . \square$

Let us again focus on a speci<sup>fi</sup>c bidder i and suppose her <sup>fi</sup>rst bid is $b _ { i 1 } \left( \geq 0 \right)$ . In the following we show that there does not exist any dominant strategy regardless of whether $b _ { i 1 }$ is positive or not.

We <sup>fi</sup>rst consider the case when $b _ { i 1 } = 0 .$ . In this case, suppose all the other bidders adopt the following bidding strategy: “bid zero in period one; in the remaining $T - 1$ periods, if bidder i bids zero in the <sup>fi</sup>rst period, then always bid the true valuation; otherwise, always bid $z { \mathrm { e r o . } } ^ { \prime \prime }$ Given that all the other bidders follow this strategy and $T \geq 3 ,$ , it is obviously not optimal for bidder i to bid zero in period one, since bidding nonzero instead eliminates the competition. Thus, $b _ { i 1 } = 0$ never constitutes a dominant strategy.

Now consider the case when $b _ { i 1 } > 0$ . In this case, suppose all the other bidders adopt the following bidding strategy: “do not bid in period one; in the remaining $T - 1$ periods, if bidder i submits a (positive) bid in the <sup>fi</sup>rst period, then always bid the true valuation; otherwise, always do not $\mathrm { b i d . ^ { \prime } }$ Given that all the other bidders follow this strategy and $T { \geq } 0 ,$ submitting a bid in period one is suboptimal for bidder i as well. Thus, $b _ { i 1 } > 0$ never constitutes a dominant strategy either. Collectively, we <sup>fi</sup>nd that it is impossible to <sup>fi</sup>nd a $b _ { i 1 }$ to constitute a dominant strategy, and therefore no dominant strategy equilibrium exists when $T 2 3 . \square$

Proof of Proposition 3. Let us focus on a speci<sup>fi</sup>c bidder i and <sup>fi</sup>x an arbitrary bid pro<sup>fi</sup>le from the other $N - 1$ bidders in the <sup>fi</sup>rst period as $\{ b _ { k 1 } ,$ $k \neq i \}$ . Suppose bidder i's true valuation is x . When $x _ { i } { \leq } m a x _ { k \neq i } \{ b _ { k 1 } \}$ , it is obvious that bidder i obtains a null payoff under any bidding strategy. In this case, truthful bidding weakly dominates any other strategy.

Now assume $x _ { i } { > } m a x _ { k \neq i } \{ b _ { k 1 } \}$ and suppose bidder i submits $b _ { i 1 }$ in period one. Then, if $b _ { i 1 } { \leq } m a x _ { k \neq i } \{ b _ { k 1 } \}$ , bidder i's expected payoff is at most $( 1 - \rho ) ( x _ { i } - m a x _ { k \neq i } \{ b _ { k 1 } \} )$ , since the probability of her second bid being successfully transmitted is $1 - \rho .$ However, if $b _ { i 1 } > m a x _ { k \neq i }$ $\{ b _ { k 1 } \}$ , her expected payoff is at least $\rho ^ { N - 1 } ( x _ { i } - m a x _ { k \neq i } \{ b _ { k 1 } \} )$ , since there is a probability of $\rho ^ { N - 1 }$ when all the other $N - 1$ bidders fail to transmit their second bids. When $\rho ^ { N - 1 } + \rho \ge 1$ , submitting a bid above $m a x _ { k \neq i } \{ b _ { k 1 } \}$ in period one gives the bidder higher expected payoff, and dominates any of those below $m a x _ { k \neq i } \{ b _ { k 1 } \}$

Given the information disclosure rule in the proxy bidding, when $b _ { i 1 } { > } m a x _ { k \neq i } \{ b _ { k 1 } \}$ , the other $N - 1$ bidders have exactly the same information before submitting their second bids regardless of whether $b _ { i 1 }$ equals $x _ { i }$ or not. Note also that bidder i's second bid may get lost. Thus, bidding the true valuation in period one dominates the others when $\rho ^ { N - 1 } + \rho \ge 1$

Proof of Proposition 4. Since in the last period the bids may fail to be transmitted, if the equilibrium allocation is ef<sup>fi</sup>cient, it must be that 1) up to period $T - 1$ the effective bids, $m a x _ { t \in \{ 1 , . . . , T - 1 \} } \beta _ { t } ( x _ { i } , h _ { t } )$ are fully revealing and monotonic; and 2) the last-period bids do not overturn the results in the end of period $T - 1$ . The reason for 1) is because the ef<sup>fi</sup>cient allocation requires a deterministic winner determination that awards the object to the bidder with the highest valuation in every instance; thus, the outcome based on the effective bids in the periods without the traf<sup>fi</sup>c congestion (namely, periods 1 to $T - 1 )$ must ensure that the bidder with the highest valuation wins. The reason for 2) is to completely exclude the effect of the traf<sup>fi</sup>c congestion (otherwise the bidder with the highest valuation may fail to submit the bid successfully).

We now prove that when 0bρb1, there does not exist an equilibrium that guarantees 1) and $2 ) .$ . For ease of notation, let us de<sup>fi</sup>ne $\beta ( x _ { i } ) \equiv m a x _ { t \in \{ 1 , . . . , T - 1 \} } \beta _ { t } ( x _ { i } , h _ { t } )$ as the effective bid of each bidder at the end of period $T - 1 .$ . When $x { > } 0 ,$ it is obvious that $\beta ( x ) < x ,$ since bidding x in the <sup>fi</sup>rst $T - 1$ periods will always leave a bidder with zero surplus; thus, we rule out this trivial case where $\beta ( x ) = x .$ In the following, we show that if $\beta ( x _ { i } )$ is symmetric, fully-revealing, and monotonic, the bidding game in period T does not have a pure Nash equilibrium. Since $\beta ( x _ { i } )$ is fully-revealing, at the beginning of period T, bidders' true valuations $x _ { 1 } , \cdots , x _ { N }$ become common knowledge, and without loss of generality we assume $x _ { 1 } \ge x _ { 2 } \ge \cdots \ge x _ { N } . \ >$ From the monotonicity assumption, we have $\beta ( x _ { 1 } ) { \ge } \cdots { \ge } \beta ( x _ { N } )$ . In what follows, we prove that when $x _ { 1 } \ge x _ { 2 } > \beta ( x _ { 1 } )$ , there exists no pure Nash equilibrium of the bidding game in period $T . ^ { 1 0 }$ This instance suf <sup>fi</sup>ces to establish that no equilibrium guarantees an ef<sup>fi</sup>cient allocation. Moreover, while evaluating whether there exists a pro<sup>fi</sup>table deviation for a speci<sup>fi</sup>c bidder, we can simply focus on the cases when her bid is successfully transmitted (since otherwise her bid is irrelevant).

The proof is by contradiction. Suppose, on the contrary, that a pure Nash equilibrium of the bidding game in period T exists and denote it as $\{ x _ { 1 } ^ { * } , \cdots , x _ { N } ^ { * } \}$ . Assume $x _ { 1 } \ge x _ { 2 } > \beta ( x _ { 1 } )$ and $x _ { n } ^ { * }$ is the highest equilibrium bid with the smallest index. Then, $\beta ( x _ { 1 } ) \leq x _ { 1 } ^ { * } \leq x _ { n } ^ { * } \leq x _ { n }$ and since $x _ { 1 } > \beta ( x _ { 1 } )$ we have $x _ { n } { > } \beta ( x _ { 1 } )$ . We <sup>fi</sup>rst claim that in equilibrium, $x _ { n } ^ { * } \neq x _ { n } .$ If this were not true, bidder n has zero surplus when her bid is successfully transmitted. However, if she bids $x _ { n } - \varepsilon$ where $0 < \varepsilon < x _ { n } - \beta ( x _ { 1 } )$ , she will have some chances to win and obtain surplus ε, at least in those cases when all other bids fail to be transmitted in period T. Therefore, she has an incentive to deviate from $x _ { n } ^ { * } ,$ which implies that ${ x _ { n } ^ { * } } \neq x _ { n }$

Next, we prove in equilibrium ${ x _ { n } ^ { * } } \not \in [ \beta ( x _ { 1 } ) , x _ { n } )$ . If this were not true, we would have two possible cases. In the <sup>fi</sup>rst case, at least two bidders submit $x _ { n } ^ { * } \left( \mathrm { i . e . } \right.$ , there may be a tie). When bidder n's bid is successfully transmitted, her surplus is $x _ { n } - x _ { n } ^ { * }$ if all other bids equal to $x _ { n } ^ { * }$ fail to be transmitted (with a probability less than $\rho )$ and at most <sup>1</sup> $\cdot \left( x _ { n } - x _ { n } ^ { * } \right)$ otherwise (with a probability more than $1 - \rho )$ . Therefore, her expected surplus is no more than $\textstyle { \frac { 1 } { 2 } } ( 1 + \rho ) \left( x _ { n } - x _ { n } ^ { * } \right)$ . However, if she bids $x _ { n } ^ { * } + \varepsilon$ where $0 < \varepsilon < \frac { 1 } { 2 } ( 1 - \rho ) \left( x _ { n } - \tilde { x } _ { n } ^ { \ast } \right)$ <sup>Þþ</sup>, she will obtain a higher surplus $x _ { n } - x _ { n } ^ { * } -$ $\varepsilon .$ <sup>ð Þ</sup>Therefore, she has an incentive to deviate from $x _ { n } ^ { * } .$ In the second case, only bidder n bids $x _ { n } ^ { * } .$ In such a scenario, when $x _ { n } ^ { * } { > } \beta ( x _ { 1 } )$ , bidder n has surplus ${ x } _ { n } - { x } _ { n } ^ { * }$ when her bid is successfully transmitted. However, if she bids $x _ { n } ^ { * } - \varepsilon$ ε where $0 { < } \varepsilon { < } x _ { n } ^ { * } { - } m a x _ { k \neq { n } } \{ x _ { k } ^ { * } \}$ , she will also always win and obtain a higher surplus $x - x _ { n } ^ { * } + \varepsilon$ . Therefore, she has an incentive to deviate from $x _ { n } ^ { * } .$ When ${ x } _ { n } ^ { * } { = } \beta ( { x } _ { 1 } )$ , it must be bidder 1 who submits the highest equilibrium bid, $\mathrm { i } . \mathrm { e } _ { \cdot } , n = 1$ , and then bidder 2 always has zero surplus. However, if bidder 2 bids $\beta ( x _ { 1 } ) + \varepsilon ,$ , where $0 < \varepsilon < x _ { 2 } - \beta ( x _ { 1 } )$ she will obtain a higher surplus $x _ { 2 } - \beta ( x _ { 1 } ) - \varepsilon$ when her bid is successfully transmitted. Therefore, she has an incentive to deviate from $x _ { 2 } ^ { * } .$ In summary, when ${ x _ { n } ^ { * } } \mathrm { { = } } [ \beta ( x _ { 1 } ) , x _ { n } )$ , there always exists a bidder who intends to deviate. Thus, in equilibrium, ${ x _ { n } ^ { * } } \not \in [ \beta ( x _ { 1 } ) , x _ { n } )$

Collectively, ${ x _ { n } ^ { * } } \not \in [ \beta ( x _ { 1 } ) , x _ { n } ]$ in equilibrium. However, this is inconsistent with our assumption; consequently, when $x _ { 1 } \ge x _ { 2 } > \beta ( x _ { 1 } )$ , no pure Nash equilibrium of the bidding game in period T exists. □

Proof of Proposition 5. When withholding the object is ruled out, as is assumed in our setting without the reserve price, it has been shown that no other mechanism yields a higher expected revenue for the seller than the single-shot second-price auction, see, e.g., Section 5.2 in [17] and [15]. Speci<sup>fi</sup>cally, the optimality is established through the mechanism design approach in [17]. Note that the mechanism design approach can be applied in our context as well, even though the bidders are allowed to bid for multiple periods. The crucial point is that the auctioneer can only elicit information through the bidders' bids. In the absence of the reserve price, the auctioneer is then committed to awarding the object to the bidders. This can be conveniently incorporated to the mechanism design problem speci<sup>fi</sup>ed in Section 5.2 in [17] by adding an additional constraint that $\begin{array} { r } { \bar { \sum _ { i = 1 } ^ { N } } Q _ { i } ( \mathbf { x } ) = 1 } \end{array}$ , where $Q _ { i } ( \mathbf { x } )$ is the probability that <sup>¼</sup>bidder i obtains the object based on x, the report pro<sup>fi</sup>le of the bidders' valuations. Given the monotone hazard rate property, in order to maximize his expected revenue, the auctioneer intends to award the object to the bidder with the highest valuation $( \mathrm { i . e . , ~ } Q _ { i } ( \mathbf { x } ) = 1 \mathrm { ~ i f ~ } i = a r g m a x _ { j }$ {x<sub>j</sub>}, and $Q _ { i } ( { \bf x } ) = 0$ otherwise when the reserve price is ruled out).

From Propositions 1 and $^ { 4 , }$ the allocation is ef<sup>fi</sup>cient in the proxy setting (i.e., the object is awarded to the bidder with the highest valuation), but inef<sup>fi</sup>ciency arises in the non-proxy setting. Since the proxy setting gives rise to the same expected revenue as the second-price auction, it outperforms the non-proxy setting. □

Proof of Proposition 6. Let us <sup>fi</sup>rst consider the proxy setting. In the presence of traf<sup>fi</sup>c congestion, it is still optimal for the bidders to bid their true valuations, because the truth-revealing incentive in the Vickrey auction is independent of the number of bidders. Taking into account the traf<sup>fi</sup>c congestion, a buyer with valuation x obtains the following expected payoff

$$
\Pi (x) = \sum_ {k = 0} ^ {N - 1} \Phi (N, k) G _ {k} (x) [ x - E [ Y _ {k} | Y _ {k} <   x ] ],
$$

where Φ(N, k) indicates the probability that the bidder's own bid and the other k bids are transmitted successfully, $G _ { k } ( \boldsymbol { x } )$ is the probability that the bidder outbids all other bidders whose bids are effective, and $E [ Y _ { k } | Y _ { k } { < } x ]$ is the expected payment (expected second highest bid) following the standard argument in the auction literature (see, e.g., [17]). Note that the allocation may be inef<sup>fi</sup>cient, since the bid from the bidder with the highest valuation may not be transmitted successfully.

Now we switch to the non-proxy setting. We claim that the following bidding function constitutes a symmetric, fully-revealing, monotonic equilibrium:

$$
\beta (x) = \frac {1}{\sum_ {k = 0} ^ {N - 1} \Phi (N , k) G _ {k} (x)} \int_ {0} ^ {x} y \sum_ {k = 0} ^ {N - 1} \Phi (N, k) g _ {k} (y) d y.
$$

To verify that this is indeed an equilibrium, it is helpful to consider the expected payoff of a bidder with valuation x but pretends to be type-z (by bidding $\beta ( z ) )$ . We can express this expected payoff, denoted by Π(z, x), as follows:

$$
\Pi (z, x) = \sum_ {k = 0} ^ {N - 1} \Phi (N, k) G _ {k} (z) [ x - \beta (z) ],
$$

where $\sum _ { \mathrm { k } = 0 } ^ { \mathrm { N } - 1 } \Phi ( N , k ) G _ { k } ( z )$ is the probability that the bidder's own bid is <sup>¼</sup>transmitted successfully and exceeds all other effective bids, and $x -$ $\beta ( z )$ is the net payoff upon winning the object.

We <sup>fi</sup>rst characterize a candidate bidding function. Later, we verify that this bidding function indeed constitutes an equilibrium. A necessary condition for $\beta ( x )$ to be an equilibrium bidding function is that each bidder must be better off under truth-telling. In other words, the following incentive compatibility constraint must be satis<sup>fi</sup>ed:

$$
\Pi (x, x) \geq \Pi (z, x), \forall x, z,
$$

i.e., $\Pi ( z , x )$ attains its maximum at $z = x .$ This implies the following <sup>fi</sup>rst-order condition:

$$
\left. \frac {\partial \Pi (z , x)}{\partial z} \right| _ {z = x} = \sum_ {k = 0} ^ {N - 1} \Phi (N, k) g _ {k} (x) x - \sum_ {k = 0} ^ {N - 1} \Phi (N, k) [ G _ {k} (x) \beta (x) ] ^ {\prime} = 0,
$$

Since a bidder with valuation 0 never bene<sup>fi</sup>ts from bidding a positive amount, $\beta ( 0 ) = 0$ . Thus,

$$
\frac {d \left[ \sum_ {k = 0} ^ {N - 1} \Phi (N , k) G _ {k} (x) \beta (x) \right]}{d x} = \sum_ {k = 0} ^ {N - 1} \Phi (N, k) g _ {k} (x) x,
$$

which yields

$$
\beta (x) = \frac {\int_ {0} ^ {x} y \sum_ {k = 0} ^ {N - 1} \Phi (N , k) g _ {k} (y) d y}{\sum_ {k = 0} ^ {N - 1} \Phi (N , k) G _ {k} (x)}.
$$

It can then be veri<sup>fi</sup>ed that this bidding function is monotonic in x and the incentive compatibility constraints are satis<sup>fi</sup>ed following the standard procedure. We omit the details here.

Now we can establish the revenue equivalence between the singleperiod proxy and non-proxy settings. In the non-proxy setting, the probability with which a bidder with valuation x wins is $\sum _ { \mathrm { k } = 0 } ^ {  { \hat { \mathrm { N } } } - 1 } \Phi ( N , k ) G _ { k } ( x )$ , and upon winning, her payoff is $x - \beta ( x )$ . Therefore, <sup>¼</sup>her expected payoff is $\sum _ { k = 0 } ^ { \mathrm { N } - 1 } \Phi ( N , k ) G _ { k } ( x ) \Bigl ( x - \textstyle { \frac { 1 } { G _ { k } ( x ) } } \int _ { 0 } ^ { x } y g _ { k } ( y ) d y \Bigr )$ , which is identical to $\varPi ( x )$ <sup>¼</sup>we established before in the proxy setting. This implies that the expected revenue the seller can extract from each bidder is the same in both the proxy and non-proxy settings, thereby leading to the revenue equivalence result. □

## References

[1] M. Babaioff, J. Hartline, R. Kleinberg, Selling banner ads: online algorithms with buyback, Fourth Workshop on Ad Auctions, 2008.

[2] P. Bajari, A. Hortacsu, Winner's curse, reserve prices and endogenous entry: empirical insights from eBay, The Rand Journal of Economics (2003) 329–355.

[3] D. Beil, L. Wein, An inverse-optimization-based auction mechanism to support a multi-attribute RFQ process, Management Science 49 (2003) 1529–1545.

[4] D. Bergemann, J. Valimaki, The Dynamic Pivot Mechanism, Cowles Foundation Discussion Papers Cowles Foundation, Yale University 2008

[5] G. Cai, P. Wurman, Monte Carlo approximation in incomplete-information, sequential-auction games, Decision Support Systems 39 (2) (2005) 153–168.

[6] G. Cai, P. Wurman, X. Chao, The non-existence of equilibrium in sequential auctions when bids are revealed, Journal of Electronic Commerce Research 8 (2) (2007).141-156

[7] R. Caldentey, G. Vulcano, Online auction and list price revenue management, Management Science 53 (5) (2007) 795–813

[8] J. Chen, J. Feng, A. Whinston, Keyword auctions, unit-price contracts, and the role of commitment, Production and Operations Management 19 (2010) 305–321.

[9] F. Constantin, J. Feldman, S. Muthukrishnan, M. Pal, Online ad slotting with cancellations, Fourth Workshop on Ad Auctions, 2008.

[10] B. Edelman, M. Ostrovsky, M. Schwarz, Internet advertising and the generalized second-price auction: selling billions of dollars worth of keywords, The American Economic Review 97 (2007) 242–259.

[11] D. Fudenberg, J. Tirole, Game Theory, The MIT Press, Cambridge, Massachusetts, 1994.

[12] A. Ghosh, P. McAfee, K. Papineni, Vassilvitskii, Bidding for representative allocations for display advertising, Proceedings of the 4th international Workshop on Internet and Network Economics (WINE), 2009.

[13] K. Hasker, R.C. Sickles, ebay in the economic literature: analysis of an auction marketplace, Review of Industrial Organization 37 (2010) 3–42.

[14] Z. Hidvegi, W. Wang, A.B. Whinston, Buy-price English auction, Journal of Economic Theory 129 (2006) 31–56.

[15] R. Kirkegaard, P. Overgaard, Pre-auction offers in asymmetric <sup>fi</sup>rst-price and second-price auctions, Games and Economic Behavior 63 (2008) 145–165.

[16] P. Klemperer, Auction theory: a guide to the literature, Journal of Economics Surveys 13 (1999) 227–286.

[17] V. Krishna, Auction Theory, Elsevier Science, Academic Press, 2002.

[18] D. Liu, J. Chen, Designing online auctions with past performance information, Decision Support Systems 42 (2006) 1307–1320.

[19] D. Liu, J. Chen, A. Whinston, Ex ante information and the design of keyword auctions, Information Systems Research 21 (2010) 133–153.

[20] D. Lucking-Reiley, Auctions on the internet: what's being auctioned, and how? The Journal of Industrial Economics 48 (3) (2000) 227–252.

[21] M. Mahdian, H. Nazerzadeh, A. Saberi, Allocating online advertisement space with unreliable estimates, Proceedings of the 8th ACM conference on Electronic commerce, 2007, pp. 294–301.

[22] E. Maskin, J. Riley, Optimal multi-unit auctions, in: Frank Hahn (Ed.), The Economics of Missing Markets, Information, and Games, Oxford University Press, Oxford, 1989, pp. 312–335.

[23] T. Mathews, The impact of discounting on an auction with a buyout option: a theoretical analysis motivated by eBay's buy-it-now feature, Journal of Economics 81 (2004) 25–52.

[24] P. McAfee, K. Papineni, S. Vassilvitskii, Maximally representative allocations for guaranteed delivery advertising campaigns, Working paper, Yahoo! Research, 2010.

[25] P.R. Milgrom, R.J. Weber, A theory of auctions and competitive bidding, Econometrica 50 (1982) 1089–1122.

[26] R. Myerson, Optimal auction design, Mathematics of Operations Research 6 (1981) 58–73.

[27] A. Ockenfels, A.E. Roth, Late bidding in second price internet auctions: theory and evidence concerning different rules for ending an auction, Games and Economic Behavior 55 (2006) 297–320.

[28] A. Ockenfels, D. Reiley, A. Sadrieh, Online auctions, in: T. Hendershott (Ed.), Economics and Information Systems, Volume 1 of Handbooks in Information Systems, Elsevier, Amsterdam, The Netherlands, 2006, pp. 571–628.

[29] I. Onur, K. Tomak, Impact of ending rules in online auctions: the case of yahoo. com, Decision Support Systems 42 (2006) 1835–1842.

[30] S.S. Reynolds, J.C. Wooders, Auctions with a buy price, Economic Theory 38 (1) (2006) 9–39.

[31] M. Robinson, Collusion and the choice of auction, The Rand Journal of Economics 16 (1985) 141–145.

[32] A. Rogers, E. David, N.R. Jennings, The effects of proxy bidding and minimum bid increments within ebay auctions, ACM Transactions on the Web 1, 2007, Article 9.

[33] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-pric auctions: evidence from eBay and Amazon auctions on the Internet, The Ameri can Economic Review 92 (2002) 1093–1103.

[34] H. Varian, Position auctions, International Journal of Industrial Organization 25 (2007) 1163–1178.

[35] W. Vickrey, Conterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1961) 8–37.

[36] R.J. Weber, Multiple-object auctions, in: R. Engelbrecht-Wiggans, M. Shubik, R.M. Stark (Eds.), Auctions, Bidding and Contracting: Uses and Theory, New York University Press, 1983, pp. 165–191.

[37] P.R. Wurman, J. Zhong, G. Cai, Computing price trajectories in combinatorial auctions with proxy bidding, Electronic Commerce Research and Applications 3 (2004) 329–340.

[38] R. Zeithammer, C. Adams, Modeling online auctions with proxy-bidding: ascending versus sealed model, Working paper, University of Chicago, 2006.

Gangshu (George) Cai is an associate professor in the Department of Management at Kansas State University. He received his PhD in Operations Research from North Carolina State University in 2005, and his MS in Business Statistics and Economics in 1999 and BS in Physics in 1996 from Peking University. His research is concentrated on multichannel supply chain management, with particular focus on the interface between operations management and marketing, <sup>fi</sup>nance, and e-commerce

Ying-Ju Chen joined the Department of Industrial Engineering and Operations Research at UC Berkeley in July 2007 after completing his PhD in Operations Management in the IOMS Department, Leonard N. Stern School of Business, New York University. He also holds master's and bachelor's degrees of Electrical Engineering from National Taiwan University. He is a recipient of a NYU teaching excellence award, the second place of an INFORMS Junior Faculty Interest Group (JFIG) paper competition, the Harold MacDowell Award from Stern School, Meritorious Service Awards from Management Science and Manufacturing & Service Operations Management, and other awards and fellowships during his academic journey. His current research interests lie in operations–marketing interface, auctions, supply chain management, and competitive strategies. His work has appeared in several leading conferences and journals in the <sup>fi</sup>elds of accounting, economics, information systems marketing and operations research

Xiting Gong is currently a research fellow in the department of Industrial and Operations Engineering at the University of Michigan, Ann Arbor. He received his PhD in management from the Guanghua School of Management, Peking University, China. His main research area is operations and supply chain management with particular interests in stochastic inventory control and game theoretic applications.
