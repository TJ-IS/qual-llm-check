---
otero_id: 12032
otero_key: "63CXHJ5S"
title: "Targeted Couponing in Online Auctions"
authors: "Vidyanand Choudhary; Shivendu Shivendu"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0688"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Information Systems Research

![](/api/attachments/63CXHJ5S/fulltext/images/de690247f7596cc8e3c973c55a7dca703f8bfce3215f659f76de701be48e2c18.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Targeted Couponing in Online Auctions

Vidyanand Choudhary, Shivendu Shivendu

To cite this article:

Vidyanand Choudhary, Shivendu Shivendu (2017) Targeted Couponing in Online Auctions. Information Systems Research

Published online in Articles in Advance 03 Jul 2017

https://doi.org/10.1287/isre.2017.0688

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/63CXHJ5S/fulltext/images/ea1879103e20651af6fb2a52e5c7479f9b01af08540d4bf956aac0d643e3a3f5.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Targeted Couponing in Online Auctions

Vidyanand Choudhary,<sup>a</sup> Shivendu Shivendu<sup>b</sup>

<sup>a</sup> Paul Merage School of Business, University of California, Irvine, Irvine, California 92697; <sup>b</sup> Muma College of Business, University of South Florida, Tampa, Florida 33620

Contact: veecee@uci.edu (VC); shivendu@usf.edu (SS)

Received: November 9, 2012 Revised: August 31, 2013; November 22, 2014, September 18, 2015; May 16, 2016 Accepted: June 19, 2016 Published Online in Articles in Advance: July 3, 2017

https://doi.org/10.1287/isre.2017.068

Copyright: © 2017 INFORMS

Abstract. To study the role of targeted couponing in auctions, we develop a stylized model in which bidders have heterogeneous valuations and participation costs wherein their entry probabilities are endogenous. Couponing impacts the seller’s profit in two ways: (i) impact on bidders’ entry probability including negative externalities for the bidder who does not receive a coupon and (ii) value extraction. We find that targeting a coupon to the low-valuation bidder can be optimal for the firm even if it leads to a reduction in the joint entry probability of the two bidders because of the benefit from value extraction. A novel result is that in the context of auctions it can be optimal for the seller to issue targeted coupons to the high-valuation bidder. We also find that an increase in the bidders’ valuation or reduction in the participation cost can lead to lower profit for the seller. This result is driven by the nonmonotonicity of the joint entry probability of the two bidders and the seller profits being nonmonotone functions of bidders’ valuations and participation costs.

History: Chris Forman, Senior Editor; De Liu, Associate Editor.

Keywords: online auction • couponing • second-price auction • targeted couponing • participation cost • entry probability

## 1. Introduction

Academic researchers have studied the impact of couponing and targeted couponing on consumers, sellers, and social welfare in the retail context. The analytics and big data technology that has enabled targeted couponing in the retail context also makes it feasible for online auctions. There is some evidence to suggest that online auction platforms are starting to ofer coupons. For example, eBay provides a third-party hosted couponing solution through MyStoreRewards “to reward buyers by ofering a small cash-back.”<sup>1</sup> Aucser.com allows online auction sellers to create a working coupon on the fly. The coupon can either be a dollar value or a percentage of the winning bid, and it can be set to expire on a certain date or after a certain number of uses. Aucser.com also allows sellers to target the coupons and track redemptions. Similarly, SkyAuction.com gives coupons to bidders, and the winning bidder receives a \$50 discount for auctions in certain time periods. However, there is scant research on the implications of targeted couponing in the context of online auctions. By contrast, there is a rich literature on the role of targeted couponing in the retail context. In this paper, we seek to bridge this gap between literature on targeted couponing in the retail context and online auctions.

What is the rationale for couponing in the retail setting? Is that rationale applicable in an auction context? While the literature on couponing in the retail context has focused largely on the role of couponing as a second degree price discrimination mechanism (Narasimhan 1984, Levedahl 1984, Sweeney 1984, Varian 1989), some researchers have also examined the role of targeted couponing in the retail context (Shafer and Zhang 1995).<sup>2</sup> In the retail context, couponing is used to expand the market by either allowing lowervaluation consumers or consumers who purchase from other sellers to purchase the product. Also, couponing in the retail context does not create any externalities on consumers who do not receive the coupon.

The auction context is diferent in three important ways: (i) couponing does not lead to market expansion, (ii) couponing creates negative externalities on consumers who do not receive the coupon as they have to compete with coupon-bearing consumers to win the auction, and (iii) bidders incur a cost to participate in the auction (participation cost) because they have to learn the rules of the auction, wait for the auction to be over before realizing whether they win the item, etc. This cost of participation is diferent from that in the retail context where the literature has focused on the cost of clipping coupons, which is tied to the use of coupons. In the auction context, the participation costs are not linked to the use of coupons, but are related to participation in the auction. These diferences between the retail and auction contexts may lead to diferent couponing strategies. For example, since couponing leads to negative externalities in auctions, couponing low-valuation consumers may not be profit enhancing because it hurts high-valuation consumers. This may change the conditions under which targeted couponing is optimal and may create new opportunities for couponing that leverage the externalities.

In this paper, we study the role of coupons in auctions and focus on the following research questions. What are the conditions that support targeted couponing in online auctions? To whom should the seller target the coupons? What factors determine the face value of the coupon? How does couponing impact the strategies of the bidders? What are the diferences in targeted couponing in auctions from prior literature on couponing in retail contexts?

To study these questions, we develop an analytical model with two types of bidders who are heterogeneous in their valuations and participation costs. The seller has information about bidder types but is uncertain about their participation costs and can leverage information about bidder types to issue targeted coupons. As discussed previously, bidders incur a participation cost because they have to learn the rules of the auction, wait for the auction to be over before realizing whether they win the item, etc. Since highervaluation bidders, on average, place a higher value on their time, in our model, high-valuation bidders, on average, face higher participation costs. Furthermore, in our conceptualization, each bidder takes into account his<sup>3</sup> participation cost, the probability of winning the auction, and the expected surplus if he wins. The bidders enter the auction when their expected surplus is nonnegative. The seller can influence bidders’ decision to enter the auction by issuing coupons, and her couponing strategy depends on the relative values of three parameters: the valuations of the low- and high-valuation bidders and the relative participation cost of the low-valuation bidder.

One novel result in the context of couponing in the auction setting that is diferent from prior literature on couponing in the retail setting is that it can be optimal to target the low-valuation bidder even when he always enters the auction. This is diferent from the literature where coupons are typically used to entice consumers who may not otherwise purchase (Narasimhan 1984). To understand this result, note that in online auctions, coupons impact seller’s profit in two distinct ways: (i) value extraction from the bidder who wins the auction and (ii) impact on bidders’ entry probabilities. Since a bidder who has a coupon will be willing to bid higher than his valuation, one role of coupons in auctions is to enhance value extraction from the winner of the auction. The value extraction role of coupons does not exist in the couponing literature in the retail context. The second role of couponing is to influence bidders’ entry probabilities, which are endogenous. The entry probability of each bidder depends on their expected surplus from participating in the auction, and the seller can impact the expected surplus of the bidders through her couponing strategy—the bidders who receive a coupon are more likely to enter, whereas those who do not are less likely to enter. The couponing literature in the retail context has modeled the positive impact of coupons on purchase probability, whereas in the auction context, coupons also have a negative externality on the entry probability of bidders who do not receive coupons. The optimal couponing strategy depends on the balance of the benefits and the costs of value extraction and bidders’ entry probabilities.

Another interesting finding is that, in the context of online auctions it can be optimal for the seller to issue targeted coupons to the high-valuation bidder. By contrast, prior literature recommends issuing coupons to low-valuation consumers for price discrimination or to marginal consumers to poach them from competitors (Narasimhan 1984, Levedahl 1984, Sweeney 1984, Varian 1989, Shafer and Zhang 1995, Fudenberg and Tirole 2000). The strategy of targeting the highvaluation bidder is driven by the impact of coupons on the joint entry probability of both bidders. This occurs because in a two-bidder model, the seller obtains strictly positive profit only when both bidders enter the auction. Since couponing exhibits negative externalities, therefore, to maximize profit, the firm seeks to optimize the bidders’ joint entry probability by targeting either the high-valuation or the low-valuation bidder depending on their entry probabilities. If the entry probability of the low-valuation bidder is low, then the seller seeks to optimize the joint entry probability by targeting the low-valuation bidder. On the other hand, when the entry probability of the high-valuation bidder is low, the firm targets that bidder to increase the joint entry probability.

Whereas one may expect seller’s profit to increase with bidders’ valuations and decrease with their participation costs, we find that the seller’s profit is nonmonotone in valuations and participation costs of the bidders. This nonmonotonicity of the profit is driven by nonmonotonicity in the joint entry probability of the two bidders. In other words, high valuation or low participation costs of one bidder boost his entry probability but will lower the joint entry probability when this bidder’s entry probability is high enough.

Finally, we find that it is never optimal for the firm to target both bidders with coupons. As discussed previously, coupons have two roles: value extraction and impact on bidder entry probability. The value extraction role does not generate any extra benefit by couponing both bidders compared to issuing coupons to only one bidder. Moreover, issuing coupons to both bidders provides lower marginal benefit from changes in joint entry probability because the coupons work at crosspurposes. However, the cost of couponing increases significantly because the winning bidder always cashes his coupon even when he alone enters the auction. Thus, the net profit impact of issuing coupons to both bidders is negative, and hence it is not optimal to issue coupons to both bidders.

## 1.1. Literature Review

With the advent of personalization technologies, it has become rather commonplace for sellers to identify individual consumers and “tailor their promotional prices to consumers on a one-to-one basis” (Shafer and Zhang 2002, p. 1143). For example, online contentenabled workflow solutions provider LexisNexis sells to diferent users at diferent prices (Shapiro and Varian 1999). Online commercial transactions enable sellers to collect and analyze data at the individual buyer level to decipher each buyer’s willingness to pay (WTP) for a certain good and adopt personalized pricing strategies (Choudhary et al. 2005, Chen and Iyer 2002). Researchers have also studied targeted couponing as a competitive strategy to poach rival firms’ loyal customers (Shafer and Zhang 1995, Bester and Petrakis 1996, Fudenberg and Tirole 2000), and couponing to convert buyers into repeat loyal consumers (Fong and Liu 2008).

Bapna et al. (2008) use data from Yankee and uniform-price multiunit auctions to predict bidders’ WTP and report that their estimates are within 2% of bidders’ revealed WTP. There is extensive empirical literature in the information systems (IS) area on auctions. This research has studied diferences between online and ofline auctions (Overby and Jap 2009), the role of bidders and bidder characteristics (Ariely and Simonson 2003, Bapna et al. 2004), interdependence between diferent auctions (Bapna et al. 2009), and the impact of auction design on outcome and bidding behavior (Bapna et al. 2003, Gallien and Gupta 2007, Goes et al. 2010). The role of seller search for a highvaluation buyer and buyer search for an appropriate product and low price are key to the growth of online auctions, and the search behavior impacts market outcome and eficiency (Kuruzovich et al. 2010).

There have been some notable exceptions where IS researchers have undertaken analytical investigations of online auctions, especially design of keyword auctions (Liu et al. 2010), design of online auctions (Liu and Chen 2006; Kannan 2010, 2012), and analysis of simultaneous use of online auctions and posted prices (Etzion et al. 2006). These studies informed our research, although we restrict our attention to the role of targeted coupons in online auctions.

The remainder of this paper is organized as follows: In Section 2, we present the model, and in Section 3, we examine the benchmark case in which the seller does not issue any coupons. In Section 4, we examine the seller’s optimal targeted couponing strategy. We discuss our results and identify suitable theoretical and managerial implications in Section 5 and conclude in Section 6.

## 2. Model

We model the online auction as a second-price auction consistent with real-world online auctions on eBay (Roth and Ockenfels 2002, Zeithammer 2006). Our auction setting is similar to the web-based auctions of Van Heck and Vervest (1998) in which one seller auctions a single item to many prospective buyers; much of the research in auctions has focused on this setting (for an extensive literature survey of auction theory, see Klemperer 1999). Following the extant literature, in our model the seller has information about prospective buyers such that she has the ability to target coupons to diferent types of buyers.

We consider a private-value auction where each bidder knows his valuation for the item, which is independent of others’ valuations. The private-value setting has been supported by extensive literature that has empirically studied online auction platforms like eBay (Hou and Rego 2007, Ockenfels and Roth 2006, Roth and Ockenfels 2002, Zeithammer 2006). The seller has no intrinsic value for the good, and therefore, her reservation price is zero. Following the literature, we assume that the cost of the good to the seller is sunk, and therefore, the seller’s objective is to maximize revenue from the auction (Myerson 1981).

There is empirical evidence to show that most of the online auctions have few bidders. Geldman (2007) examines a sample of 3,500 items across eBay categories and finds that 82% of the auctions have two or fewer bids, although there may have been more than two potential bidders in the market. Since our context is online auctions, we develop a stylized model with two bidders: a high-valuation bidder with valuation $v _ { H } \leq 1$ and a low-valuation bidder with valuation $v _ { L } ,$ where $v _ { L } < v _ { H }$ . Our approach is similar to that in prior literature that has developed models with two bidders to study auctions (Budish and Takeyama 2001, Gale and Hausch 1994, Maskin and Riley 1985, Milgrom and Weber 1982). Bidders’ valuations for the product are unafected by the valuations of other bidders and are common knowledge.

The bidders incur participation costs to participate in the auction. Prior literature has described several sources of participation costs. Etzion et al. (2006) describe two sources: the cost of monitoring the auction and making bids and the waiting cost for the end of the auction. Cao and Tian (2010) state that bidders incur costs to learn the rules of the auction and to make bids, and opportunity costs to attend the auction. Bajari and Hortacsu (2003) studied eBay auctions and found evidence that bidders face participation costs in online auctions. One of the key determinants of the participation cost for a bidder is his opportunity cost of time. Therefore, in our conceptualization, highvaluation bidders, on average, face higher participation costs. This is consistent with the literature, including Narasimhan (1982, 1984) models of consumers with higher wage rates as facing higher opportunity cost of time. Etzion et al. (2006) also assume that participation cost is higher for high-type consumers.

Bidders’ participation cost is their private information though the distribution is common knowledge. The high-valuation bidder incurs a participation cost of $t _ { H } ,$ which is drawn from U<sup>[</sup>0, 1<sup>]</sup>. Similarly, the lowvaluation bidder’s participation cost is $t _ { L }$ drawn from $\mathrm { U } [ 0 , \kappa ]$ , where $\kappa \leq 1$ . We refer to the parameter κ as the relative participation cost of the low-valuation bidder. Each bidder learns his true participation cost before entering the auction. The seller only knows the probability distributions from which the participation costs of the bidders are drawn. Each bidder computes his expected payof from participating in the auction and enters the auction only if his expected payof is nonnegative.

The seller can auction the good with or without issuing coupons. When she adopts a couponing strategy, she can target the coupon to specific bidder(s), and the value of the coupon can be diferent for diferent types of bidders. A targeted couponing strategy involves the seller targeting a coupon of value $c _ { L }$ to the low-valuation bidder and/or $c _ { H }$ to the high-valuation bidder. The coupon has no value if the bidder does not win the auction. If the bidder with a coupon wins the auction, then she pays the second highest bid amount less the value of the coupon. Note that coupon amount $c _ { L }$ and/or $c _ { H }$ may be greater than the second highest bid amount, resulting in net negative profit to the seller. The bidders are rational and can compute the seller’s couponing strategy.

The summary of notations is in Appendix A. We make the following additional assumptions.

1. The seller and all bidders are risk neutral and there is no collusive bidding by the bidders. Note that since our setting is one of private value, the seller does not benefit from shill bidding, and therefore there is no shill bidding. Shill bidding may play a role in a commonvalue auction (Chakraborty and Kosmopoulou 2004).

2. Coupons cannot be traded, and the bidder who wins the auction always claims the product.

3. The seller’s cost of organizing the auction and cost of targeting coupons and the bidder’s cost of using a coupon are negligible.

## 2.1. Participation Decision of Bidders

In our model, the entry decision of the bidders’ is endogenous, and we now describe bidders’ participation decisions. The low-valuation bidder’s entry probability is denoted by $p _ { L } ,$ and the high-valuation bidder’s entry probability is denoted by $p _ { H }$ . The low-valuation bidder enters the auction only if he expects nonnegative surplus net of participation cost. He knows that if the high-valuation bidder enters the auction, he will not win. Therefore the low-valuation bidder’s entry probability depends on his expectation of the high-valuation bidder’s entry probability. On the other hand, the high-valuation bidder knows that if he enters the auction, he will win but his surplus depends on whether the low-valuation bidder enters the auction or not. Hence, the high-valuation bidder’s probability of entry also depends on his expectation of the lowvaluation bidder’s entry probability. Note that our formulation of endogenous entry by bidders is consistent with Levin and Smith (1994) and Etzion et al. (2006).

The seller may or may not target the bidders with coupons. We begin with a description of a general model where the seller targets each bidder with a coupon. Later in Section 3 we will examine the cases where some or none of the bidders are targeted by setting the corresponding coupon values to zero. Let the draws of the participation cost of high-valuation and low-valuation bidders be denoted as $\tilde { t } _ { H }$ and $\tilde { t } _ { L } ,$ respectively.

The expected surplus of the low-valuation bidder is $s _ { L } = ( 1 - \bar { p _ { H } } ) ( v _ { L } + c _ { L } ) \bar { - t _ { L } }$ . To understand this expression, note that the low-valuation bidder wins the auction only when the high-valuation bidder does not enter the auction, and in that case his payof is $( v _ { L } + c _ { L } ) . ^ { 4 }$ The low-valuation bidder will enter the auction when his expected surplus is nonnegative, that is, when $s _ { L } \geq 0$ ⇔ $\hat { t } _ { L } \overset { \cdot } { \leq } ( 1 - p _ { H } ) ( \overset { \cdot } { \boldsymbol { v } } _ { L } + \boldsymbol { c } _ { L } )$ . There exists a $\tilde { t } _ { L }$ at which the lowvaluation bidder is indiferent between entering and not entering the auction. We refer to this critical value of low-valuation bidder’s participation cost as $\hat { t } _ { L }$ . The low-valuation bidder participates in the auction only when $\tilde { t } _ { L } \leq \hat { t } _ { L }$ . Hence, the probability of entry of the low-valuation bidder is

$$
p _ {L} = \frac {\hat {t} _ {L}}{\kappa} = \frac {(1 - p _ {H}) (v _ {L} + c _ {L})}{\kappa}.\tag{1}
$$

The expected surplus of the high-valuation bidder is: $s _ { H } = ( 1 - p _ { L } ) ( { v } _ { H } + { c } _ { H } ) + p _ { L } ( { v } _ { H } + { c } _ { H } - ( v _ { L } + c _ { L } ) )$ $- \tilde { t } _ { H }$ . To understand this expression, note that the highvaluation bidder wins the auction whenever he enters the auction. When the low-valuation bidder does not enter the auction, the high-valuation bidder’s payof is $v _ { H } + c _ { H } ,$ and the probability of this event is $1 - p _ { L }$ . When the low-valuation bidder enters the auction then the high-valuation bidder’s payof is $v _ { H } + c _ { H } -$ $\left( v _ { L } + c _ { L } \right)$ with probability $p _ { L }$ . The high-valuation bidder will enter the auction when his expected surplus is nonnegative, or, in other words, when $s _ { H } \geq 0 .$ . There exists a $\tilde { t _ { H } }$ at which the high-valuation bidder is indifferent between entering and not entering the auction. We refer to this critical value of high-valuation bidder’s participation cost as $\hat { t } _ { { \scriptscriptstyle H } }$ . The high-valuation bidder participates in the auction only when $\tilde { t } _ { { \scriptscriptstyle H } } \le \hat { t } _ { { \scriptscriptstyle H } }$ . Hence, the probability of entry of the high-valuation bidder is

$$
p _ {H} = (1 - p _ {L}) (v _ {H} + c _ {H}) + p _ {L} (v _ {H} + c _ {H} - (v _ {L} + c _ {L})).\tag{2}
$$

Under rational fulfilled expectations equilibrium, the equilibrium entry probabilities can be obtained by simultaneously solving the system of two Equations (1) and (2)

$$
p _ {L} = \frac {(1 - c _ {H} - v _ {H}) (c _ {L} + v _ {L})}{\kappa - (c _ {L} + v _ {L}) ^ {2}},\tag{3}
$$

$$
p _ {H} = 1 - \frac {\kappa (1 - c _ {H} - v _ {H})}{\kappa - (c _ {L} + v _ {L}) ^ {2}}.\tag{4}
$$

Since our setting is of a second-price auction, the optimal bidding strategy for a bidder of type $i ~ ( i \in$ $\{ \bar { L } , H \} )$ is to bid his true WTP with the coupon, that is, $v _ { i } + c _ { i }$ (Vickrey 1961, McAfee and McMillan 1987). The online auction ends with the highest bidder winning the auction and paying the second highest bid amount. We do not model the dynamics of the auction such as the sequence of bids and assume that the valuations are exogenous.

To find the expected profit of the seller, we need to consider four scenarios: (i) no bidder enters the auction, (ii) only the low-valuation bidder enters the auction, (iii) only the high-valuation bidder enters the auction, and (iv) both types of bidders enter the auction. The resulting expected profit can be written as

$$
\begin{array}{r l} & {\pi (c _ {H}, c _ {L}) = (1 - p _ {L}) (1 - p _ {H}) \cdot 0 + p _ {L} (1 - p _ {H}) \cdot (- c _ {L})} \\ & {\qquad + (1 - p _ {L}) (p _ {H}) \cdot (- c _ {H})} \\ & {\qquad + p _ {L} \cdot p _ {H} (v _ {L} + c _ {L} - c _ {H}).} \end{array}\tag{5}
$$

We now provide an overview of the trade-ofs associated with the couponing strategy. As discussed previously, in our conceptualization, targeted couponing implies that the seller has the ability to provide a coupon of a particular value to any one type or more types of bidders. Couponing can be beneficial to the seller because targeted couponing may make a couponbearing bidder raise the bid amount, which may generate a higher profit from the winning bidder in a second-price auction. If the auction winner is a bidder without a coupon, then the seller’s profit increases due to couponing. On the other hand, couponing may hurt the seller if only one bidder enters the auction because the winning bidder redeems the coupon without any increase in the amount paid by the winner. Furthermore, coupons may impact the entry probabilities of bidders because each bidder’s decision to enter the auction is endogenous in our setting and coupons impact the expected gain of the bidder(s) who has (have) the coupon(s) from entering the auction. Therefore, it is clear that the optimality of a couponing strategy is critically dependent on the balance of trade-ofs between the potential gain and potential loss to the seller from targeted couponing. The seller has several strategies for targeted couponing: (i) she may target both bidder types simultaneously, or (ii) she may target only one bidder type. First, in Section 3, we consider the benchmark case in which the seller does not issue any coupons.

## 3. Benchmark Case: Seller Does Not Issue Any Coupons

We start with a benchmark case to compute the seller’s profit when no coupons are issued. We will compare the profit from various couponing strategies to this benchmark to determine whether the couponing strategies are profit increasing. When no coupons are issued, the profit of the seller can be obtained from Equation (3) by setting $c _ { H } = 0$ and $c _ { L } = 0$ . The interior equilibrium entry probabilities of both types of bidders and expected profit of the seller from the auction are reported in Lemma 1.

Lemma 1 (Interior Region). The equilibrium entry probabilities of the bidders in the interior region are ${ p } _ { L } = { v } _ { L }$ $( 1 - v _ { H } ) / ( \kappa - v _ { L } ^ { 2 } )$ and $p _ { H } = 1 - \kappa ( 1 - v _ { H } ) / ( \kappa - v _ { L } ^ { 2 } )$ when $\kappa > v _ { L } ( 1 + v _ { L } - v _ { H } )$ and $v _ { H } < 1$ . The expected profit of the seller is $\pi _ { N } = ( v _ { L } ^ { 2 } ( 1 - v _ { H } ) ( \kappa v _ { H } - v _ { L } ^ { 2 } ) ) / ( \dot { \kappa } - v _ { L } ^ { 2 } ) ^ { 2 }$

All proofs of the lemmas and propositions are provided in Appendix B.

Lemma 1 explores the expected profit of the seller in the interior region, where there is some uncertainty about the entry of the bidders, and therefore the entry probabilities of both types of bidders are strictly in $\bar { ( 0 , 1 ) }$ . The conditions for the interior region require that the relative participation cost of the low-valuation bidder (κ<sup>)</sup> is not too small relative to $v _ { L }$ because otherwise the low-valuation bidder always enters the auction when he draws his participation cost. This condition can also be rewritten as $\begin{array} { r } { { v } _ { H } ^ { - } > 1 + { v } _ { L } - ( \kappa / v _ { L } ) ; } \end{array}$ ; this implies that the valuation of the high-valuation bidder $( v _ { H } )$ should be high relative to the valuation of the low-valuation bidder. The equilibrium entry probabilities of both types of bidders and expected profit of the seller in the boundary region are reported in Lemma 2.

Lemma 2 (Boundary Region). The equilibrium entry probabilities of the bidders on the boundaries are as follows:

(i) ${ \cal I } f v _ { \cal H } = 1$ , then $p _ { L } = 0$ and $p _ { H } = 1$ . The expected profit of the seller is $\pi _ { N } = 0 .$

(ii) $I f \kappa \leq v _ { L } ( 1 + v _ { L } - v _ { H } )$ and $v _ { H } < 1$ , then $p _ { L } = 1$ and $p _ { H } = v _ { H } - v _ { L }$ . The expected profit of the seller is $\pi _ { N } =$ $v _ { L } ( v _ { H } - v _ { L } )$

Part (i) of Lemma 2 states the boundary condition when the high-valuation bidder enters with certainty.

Note that the high-valuation bidder always wins the auctions when he enters. Thus, the low-valuation bidder does not enter when the high-valuation bidder’s entry is certain. This situation is realized when $v _ { H } = 1 ,$ since the maximum participation cost that the highvaluation bidder can draw is 1. In this case the highvaluation bidder always has a nonnegative surplus from entering the auction when the low-valuation bidder does not enter. Therefore, the low-valuation bidder has no incentive to enter, and this boundary condition is realized.

On the other hand, when the relative participation cost of the low-valuation bidder is small relative to $v _ { L } ,$ then the low-valuation bidder is more likely to enter the auction. When the high-valuation bidder’s valuation is small enough (the condition in part (ii) of Lemma 2 can be rewritten as $v _ { H } \le 1 + v _ { L } - ( \kappa / v _ { L } ) )$ , the low-valuation bidder expects the high-valuation bidder to enter less often and that increases his entry probability. Hence, when the stated conditions in part (ii) of Lemma 2 are satisfied, the low-valuation bidder always enters the auction, that is, $p _ { L } = 1$

Proposition 1. Comparative Statics of Entry Probabilities in the Interior Region: When the seller does not issue any coupons, (i) the entry probability of the lowvaluation bidder $( p _ { L } )$ increases with $v _ { L } .$ , decreases with $\kappa ,$ and decreases with $v _ { H } .$ . (ii) The entry probability of the highvaluation bidder $\left( \boldsymbol { p } _ { H } \right)$ decreases with $v _ { L } ,$ increases with $\kappa ,$ and increases with $v _ { H }$

Figure 1(a) shows the entry probabilities of both types of bidders as a function of the relative participation cost of the low-valuation bidder <sup>(</sup>κ<sup>)</sup>. The curved portion lies in the interior region as specified in Lemma 1, and the flat portion indicates the probabilities on the boundary as stated in Lemma 2. Similarly, Figure 1(b) shows the entry probabilities as a function of the valuation of the low-valuation bidder $\left( v _ { L } \right)$

Note that the equilibrium entry probabilities in the interior region are determined by the interplay of all three parameters in our setting, namely, $v _ { H } , \ v _ { L } ,$ and $\kappa ,$ and in turn the entry probabilities determine the seller’s expected profit. The following proposition describes the impact of diferent parameters on the expected profit.

Proposition 2. Comparative Statics of Profit in the Interior Region: (i) When $v _ { H } < ( \kappa + v _ { L } ^ { 2 } ) / ( 2 \kappa )$ , the seller’s profit increases with $v _ { H }$ and decreases otherwise. (ii) When $\kappa < v _ { L } ^ { 2 } ( 2 - v _ { H } ) / v _ { H } .$ , the seller’s profit increases with κ and decreases otherwise. (iii) When $v _ { L } > v _ { H } / 2$ and $v _ { L } >$ $\sqrt { \kappa v _ { H } / ( 2 - v _ { H } ) }$ , the seller’s profit decreases with $v _ { L }$ and increases otherwise.

One would expect that an increase in the valuations of the bidders would lead to increased profit to the seller. Surprisingly, the seller’s expected profit may not be monotonically increasing in the valuation of the high-valuation bidder (Proposition 2(i) and Figure $2 ( \mathsf { a } ) ) ,$ , the valuation of the low-valuation bidder, and the relative participation cost of the low-valuation bidder. To understand the intuition for this result, one has to understand the underlying dynamics in the model.

The seller’s expected profit is mediated by the entry probabilities as stated in Lemma 1. As $v _ { H }$ increases, the entry probability of the high-valuation bidder increases, but the entry probability of the low-valuation bidder decreases because his expected surplus decreases when the high-valuation bidder enters more often. Replacing $c _ { L } = c _ { H } = 0$ in Equations (1)–(3), we obtain the entry probabilities and the expected profit of the seller when no coupon is issued. Let the joint entry probability be $J ( p _ { L } , p _ { H } ) = p _ { L } \cdot p _ { H } .$ We have $\delta J / \delta p _ { H } = p _ { L } + p _ { H } ( \delta p _ { L } / \delta p _ { H } ) .$ , which can be written as $\delta J / \delta p _ { H } = v _ { L } ( 1 - p _ { H } ) / \kappa + p _ { H } ( - v _ { L } / \kappa )$ . Evaluating $\delta J / \delta p _ { H }$ at the two limits, $p _ { H } = 0$ and $p _ { H } = 1$ we have $\delta J / \delta p _ { H } | _ { p _ { H } = 0 } > 0 , \delta J / \delta p _ { H } | _ { p _ { H } = 1 } < 0$ . Hence, ${ \cal J } ( p _ { L } , p _ { H } )$ can be a nonmonotone function of $p _ { H }$ when $p _ { H }$ is in the interior. Using Lemma 1, we have $\delta p _ { H } /$ $\delta v _ { H } = \kappa / ( \kappa - v _ { L } ^ { 2 } )$ , which can be positive or negative but does not change signs as $v _ { H }$ changes. Therefore, $p _ { H }$ is a monotone function of $v _ { H }$

Figure 1. (a) Impact of Low-Valuation Bidder’s Relative Participation Cost on the Entry Probabilities of Both Bidder $( v _ { H } = 0 . 9 , v _ { L } = 0 . 5 )$ and (b) Impact of Valuation of Low-Valuation Bidder on the Entry Probabilities of Both Bidders $( v _ { H } = 0 . 9 , \kappa = 0 . 4 )$  
(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/8601da7568ba9da146cf4185295405190e07cb1e3a9d2c4e7636f9a6787d5f29.jpg)

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/c80f4bf6f664d3a5eca1279a4a18d3ca44c8336d8805a5ffc078b8145b2d006a.jpg)

Figure 2. No-Coupon Case: (a) Impact of Valuation of the High-Valuation Bidder on Profit $( v _ { L } = 0 . 5 )$ and (b) Interior and Boundary Regions with Valuation of the Low-Valuation Bidder and the Low-Valuation Bidder’s Relative Participation Cost $( v _ { H } = 0 . 6 )$  
(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/4505c537a0235b062bded55d3dc63801b719b62a53d58ec0e99b3f8ce8664c47.jpg)

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/ea704208576b8b1f199eaab744bc2faf0e52fcc04d960485d2a9416315213199.jpg)  
joint entry probability than the maximum level. Therefore, as κ increases, up to a critical value of $\kappa =$ $( 2 - v _ { H } ) v _ { L } ^ { 2 } / v _ { H } ,$ the joint entry probability approaches the maximum level, and the seller’s expected profit increases. After this critical value, a further increase in κ leads to a reduction in the seller’s profit.

From the chain rule, we can write $\delta J ( p _ { L } , p _ { H } ) / \delta v _ { H } =$ $( \delta J ( p _ { L } , p _ { H } ) / \delta p _ { H } ) ( \delta p _ { H } / \delta v _ { H } )$ . Since $\delta J / \delta p _ { H } | _ { p _ { H } = 0 } > 0$ and $\delta J / \delta p _ { H } | _ { p _ { H } = 1 } < 0 ,$ , and since $\delta p _ { H } / \delta v _ { H }$ does not change sign, the joint entry probability ${ \cal J } ( p _ { L } , p _ { H } )$ can be a nonmonotone function of $v _ { H }$ . Note that the expected profit of the seller is $p _ { L } p _ { H } v _ { L } .$ , and it can be written as $J ( p _ { L } , p _ { H } ) v _ { L }$ . Since $J ( p _ { L } , p _ { H } )$ can be a nonmonotone function of $v _ { H } ,$ the seller’s profit can be a nonmonotone function of $v _ { H }$ for some parameter values.

In summary, the seller earns a profit only when both bidders enter the auction, and hence the seller’s profit is determined by the joint entry probability of both bidders. Increased entry by one bidder causes the other bidder to enter less often. Thus, it is possible that higher valuations that incentivize one bidder to enter more often may lead to a reduction in the joint entry probability and thus hurt the seller’s profit. Hence, the impact of $v _ { H }$ on the seller’s profit can be nonmonotone.

One would expect that an increase in the participation cost of any bidder would lead to a decrease in profit. Counterintuitively, we find that an increase in the relative participation cost of the low-valuation bidder (κ<sup>)</sup> can increase the seller’s profit. Using Lemma 1, we have $\delta p _ { H } / \delta \kappa = ( 1 - v _ { H } ) v _ { L } ^ { 2 } / ( \bar { k } - v _ { L } ^ { 2 } ) ^ { 2 } > 0 .$ . Thus, it can be shown that ${ \cal J } ( p _ { L } , p _ { H } )$ can be a nonmonotone function of the relative participation cost of the low-valuation bidder κ. Therefore, the seller’s profit can be a nonmonotone function of κ. To understand this result, note that the seller’s expected profit is maximized only when both types of bidders enter the auction. As κ increases, the entry probability of the low-valuation bidder decreases and that of the high-valuation bidder increases. When κ is very small, the low-valuation bidder’s entry probability is high, causing the highvaluation bidder to enter less often, leading to a lower

The behavior of ${ \cal J } ( p _ { L } , p _ { H } )$ with respect to the valuation of the low-valuation bidder is similar and can be a nonmonotone function of $v _ { I }$ because $\delta p _ { H } / \delta v _ { L } =$ $- ( 2 \kappa ( 1 - v _ { H } ) v _ { L } ) / ( \kappa - v _ { I } ^ { 2 } ) ^ { 2 } < 0$ . However, the seller’s profit is $J ( p _ { L } , p _ { H } ) \cdot v _ { L } ,$ which can be monotone increasing in $v _ { L }$ even when ${ \cal J } ( p _ { L } , p _ { H } )$ is a nonmonotone function of $v _ { L }$ . This can occur because the derivative of the seller’s profit with $v _ { L }$ is $\delta ( v _ { L } \cdot J ( p _ { L } , p _ { H } ) ) / \delta v _ { L } =$ $J ( p _ { L } , p _ { H } ) + \bar { v _ { L } } ( \delta J ( p _ { L } , p _ { H } ) / \delta v _ { L } )$ , which is monotone in the interior region when $v _ { L } \leq v _ { H } / 2$ and nonmonotone otherwise. Thus, we find that the seller’s profit can decrease even when the valuation of the low-valuation bidder increases.

Figure 2(b) shows the interior and the boundary region with the valuation and the relative participation cost of the low-valuation bidder. Please note that we have labeled the interior region as “Uncertain entry of L and $H ^ { \prime \prime }$ in Figure 2(b), and this region represents the space where the entry probability of each bidder is strictly between 0 and 1. The boundary region is labeled as $^ { \dot { \prime } \prime } L$ always enters, H uncertain entry,” and this region represents the space where the entry probability of the low-valuation bidder is 1 while the entry probability of the high-valuation bidder is strictly between 0 and 1. We can see that when κ is large, the interior region is realized, whereas small κ leads to the boundary where $p _ { L } = 1$ . The boundary region is larger when $v _ { L }$ increases, for a given κ.

In Section $^ { 4 , }$ we consider the cases in which the seller issues a coupon to both bidders, only to the high-valuation bidder, and only to the low-valuation bidder. In Section $4 . 4 ,$ we evaluate the overall optimal couponing strategy.

## 4. Targeted Couponing

In this section, we examine three cases: (i) the seller targets high- and low-valuation bidders, (ii) the seller targets only the high-valuation bidder, and (iii) the seller targets only the low-valuation bidder. When the seller issues coupons, then the sequence of moves is as follows: First, the seller determines her couponing strategy, which consists of determining the value and target of each coupon. Next, bidders enter the auction (with or without a coupon) with their respective entry probabilities. Finally, bidders place their bids and the winning bid is finalized.

## 4.1. Targeted Couponing at Both Bidders

First, we analyze the case in which the seller targets a coupon of value $c _ { L }$ to the low-valuation bidder and $c _ { H }$ to the high-valuation bidder. The profit of the seller depends on the entry of diferent types of bidders, and these entry probabilities are the same as those reported in Equations (1) to (4).

One might expect that since targeted couponing increases the entry probability of the targeted bidder, it may be optimal to issue coupons to both bidders under certain conditions. Interestingly, this couponing strategy is never optimal, as stated in Proposition 3.

Proposition 3. Simultaneously giving coupons to both low-valuation and high-valuation bidders is never optimal for the seller.

To understand why it is not optimal to issue coupons to both bidders simultaneously in the interior region, note that a coupon issued to any bidder has two opposing efects on the benefits and costs of the coupon: (i) an efect on entry probability (it increases the entry probability of the recipient of the coupon but it reduces the entry probability of the other bidder) and (ii) an efect on value extraction (if the winner has a coupon, then it has a weakly negative impact on profit; otherwise, it has a weakly positive impact). Issuing coupons to both bidders provides a lower marginal benefit from changes in entry probability because the coupons work at cross-purposes. In addition, there is no improvement in value extraction from issuing coupons to both bidders. However, the cost of couponing increases sharply, as the winning bidder always cashes his coupon. Thus, the net profit impact is negative, and it is not optimal to issue coupons to both bidders.

Now we describe why it is not optimal to issue coupons to both bidders in the boundary region. If the boundary involves $p _ { L } = 0 , p _ { H } = 1$ , then the seller should not give a coupon to the high-valuation bidder as her entry probability is already maximized. Similarly, the seller should not give a coupon to the low-valuation bidder as well as to the high-valuation bidder when $p _ { L } = 1$

## 4.2. Targeted Couponing to the High-Valuation Bidder

Now we examine the seller’s profit from targeting only the high-valuation bidder. We will compare this profit to the profit in the absence of couponing to determine the parameter space in which targeted couponing to the high-valuation bidder may be profit-enhancing. Recall from Section 2.1 that couponing impacts a seller’s profit through two avenues: (i) it serves to influence the entry probabilities of the two bidders such that joint entry probability can be increased, and (ii) it allows the seller to extract more revenue from the highvaluation bidder by incentivizing the low-valuation bidder to bid a higher amount. When the seller targets only the high-valuation bidder, she can use couponing to increase the entry probability of the high-valuation bidder but cannot increase value extraction. This is because the high-valuation bidder wins the auction whenever he enters. The coupon amount is deducted from the winning bid, so the revenue to the seller is $p _ { L } \cdot p _ { H } ( v _ { L } - c _ { H } ) + ( 1 - p _ { L } ) ( p _ { H } ) ( - c _ { H } )$ . Therefore, the coupon does not improve value extraction but carries a cost. Proposition 4 states the solution in the interior region when the seller considers targeting only the high-valuation bidder.

Proposition 4 (Interior Region). When the seller targets an optimal coupon only to the high-valuation bidder, the equilibrium entry probabilities of the bidders in the interior region are $p _ { L } = v _ { L } ( 2 - v _ { H } ) / ( 2 \kappa )$ and $p _ { H } = v _ { H } / 2$ when $2 - 2 \kappa / v _ { I . } <$ $v _ { H } < 2 v _ { L } ^ { 2 } / ( \kappa + v _ { L } ^ { 2 } )$ . The optimal coupon value is $c _ { H } ^ { * } = ( 2 v _ { L } ^ { 2 } -$ $v _ { H } ( \kappa + \bar { v } _ { I } ^ { 2 } ) ) / ( 2 \bar { \kappa } )$ , and the expected profit of the seller is $\pi _ { H } ^ { * } = v _ { H } ^ { 2 } / \bar { 4 } .$

Proposition 4 shows that if the seller wants to follow a strategy of targeting only the high-valuation bidder, then it issues a coupon of strictly positive value when the valuation of the high-valuation bidder is moderate. When the seller targets a coupon to the highvaluation bidder, the entry probabilities of both bidders are afected. Note that the entry probability for the high-valuation bidder is no longer dependent on any characteristic of the low-valuation bidder, such as the valuation $\left( v _ { L } \right)$ or the relative participation cost (κ<sup>)</sup>. From observation it is easy to see that $p _ { H }$ increases with $v _ { H }$ and is independent of $v _ { L } ; p _ { L }$ increases with $v _ { L }$ and decreases with $v _ { H }$ and κ. It is interesting to note that in Proposition 4 the seller’s profit depends only on the valuation of the high-valuation bidder.

Proposition 5 (Boundary Region). (a) When the seller targets an optimal coupon only to the high-valuation bidder, the equilibrium entry probabilities of the bidders on the boundary are $p _ { L } = 1$ and $p _ { H } = v _ { H } / 2$ when $v _ { H } \leq 2 - ( 2 \kappa / v _ { L } )$ and $v _ { H } < 2 v _ { L }$ . The optimal coupon value is $c _ { H } ^ { * } = v _ { L } - ( v _ { H } / 2 )$

and the expected profit of the seller is $\pi _ { H } ^ { * } = v _ { H } ^ { 2 } / 4 .$ . (b) The seller does not target the high-valuation bidder when (i) $v _ { H } \leq$ $2 - 2 \kappa / v _ { L }$ and $v _ { H } \geq 2 v _ { L }$ or (ii) $v _ { H } > 2 - 2 \kappa / v _ { L }$ and $v _ { H } \geq$ $2 v _ { L } ^ { 2 } / ( \kappa + v _ { L } ^ { 2 } )$

When the valuation of the high-valuation bidder is relatively small, the low-valuation bidder always enters the auction. The seller issues a coupon to the high-valuation bidder to increase his entry probability; however, in this region, the low-valuation bidder always enters the auction $( p _ { L } = 1 )$ . It is interesting that when the seller issues an optimal coupon, the highvaluation bidder’s entry probability is the same in the interior region as well as in the boundary region.

One interesting observation from Propositions 4 and 5 is that when the high-valuation bidder is targeted, the optimal profit in the interior region and the boundary region depends only on the valuation of the high-type bidder. The economic intuition for this result is as follows. The objective of targeting the highvaluation bidder is to optimize joint entry probability of both bidders, specifically by increasing the entry probability of the high-valuation bidder. When the valuation of the low-valuation bidder increases, it causes two separate impacts on the firm’s profit, and these two impacts perfectly ofset each other. First, increasing valuation of the low-type bidder increases profit because the winning bid is higher. Second, an increase in the valuation of the low-type bidder reduces the entry probability of the high-valuation bidder, thus requiring a larger coupon, which increases the cost of couponing. Thus, these two efects ofset each other, and there is no net change in the seller’s profit due to changes in the valuation of the low-valuation bidder. Similarly, any increase in the relative participation cost of the low-valuation bidder leads to a reduction in the joint entry probability because the entry probability of the low-valuation bidder is smaller. This increases the high-valuation bidder’s entry probability. Thus, the coupon amount to the high-valuation bidder decreases. The reduction in joint entry probability leads to lower revenue, whereas the reduction in the cost of couponing leads to higher profit. These two efects cancel each other, and there is no net impact of κ on the seller’s profit.

The regions for interior and boundary solutions stated in Propositions 4 and 5 are shown in Figure 3. Please note that we refer to the interior region as “Uncertain entry of L and $H , \prime \prime$ and the boundary region as $^ { \prime \prime } L$ always enters, H uncertain entry” in Figure 3. It is optimal to target a coupon at the high-valuation bidder when the valuation of the low-valuation bidder is relatively large or the valuation of the high-valuation bidder is relatively small or when the relative participation cost of the low-valuation bidder is relatively small.

Now, we examine the impact of changes in bidder characteristics on the optimal coupon amount and the seller’s profit in Proposition 6.

Proposition 6. Comparative Statics of Profit and Coupon Amount When the High-Valuation Bidder Is Targeted: When the seller considers targeting the highvaluation bidder such that conditions in Proposition 3 are satisfied, (i) the optimal coupon amount increases with $v _ { L }$ and decreases with $v _ { H }$ and $\kappa ,$ and (ii) the seller’s profit is increasing with valuation of the high-valuation bidder $v _ { H }$ and is independent of $v _ { L }$ and κ.

To understand part (i) of Proposition $^ { 6 , }$ note that a coupon targeted at the high-valuation bidder serves to

Figure 3. Interior and Boundary Regions Under Target High-Valuation Bidder Case: (a) Valuation of the High-Valuation Bidder and the Low-Valuation Bidder’s Relative Participation Cost $( v _ { L } = 0 . 4 5 )$ and (b) Valuation of the Low-Valuation Bidder and the Low-Valuation Bidder’s Relative Participation Cost $( v _ { H } = 0 . 8 )$ 1  
![](/api/attachments/63CXHJ5S/fulltext/images/7f67929336b2f6dc7aca5e885017dacc00e8e1911224e59cb4cf87814f9c76ee.jpg)

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/5b13c5bbf00cee8cf16ce8568d6d065c33ef59ecff058363c7f0321c5a0deacf.jpg)

Figure 4. Target High-Valuation Bidder Case: (a) Impact of the High-Valuation Bidder’s Valuation on Profit $( \kappa = 0 . 2 , v _ { L } = 0 . 5 )$ and (b) Impact of the Low-Valuation Bidder’s Relative Participation Cost on the Optimal Coupon $( v _ { L } = 0 . 6 )$  
(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/830fe092eac618d7a84b33b768c9614355845ae7fd20babde11c15f1b095a1f2.jpg)  
increase his entry probability and has no role in value extraction. When $v _ { H }$ is low or $v _ { L }$ is high or κ is low, the low-valuation bidder enters more often and that discourages the high-valuation bidder from entering the auction such that joint entry probability is lower than the optimal level. By issuing a coupon to the highvaluation bidder, the seller provides an incentive to the high-valuation bidder to enter more often, thus increasing his entry probability. As $v _ { H }$ decreases or $v _ { L }$ increases or κ decreases, the seller needs to provide stronger incentives, and hence the optimal coupon amount increases (Figure 4(b)). Similarly, increasing $v _ { H }$ increases the entry probability of the high-valuation bidder, reducing the need for a coupon, thus leading to a lower optimal coupon amount (Figure 4(b)). The expected profit of the seller increases as the valuation of the high-valuation bidder increases (Figure 4(a)).  
(b)

Recall from Proposition 1(ii) that the seller’s profit is a nonmonotone function of $v _ { H } ,$ increasing with $v _ { H }$ when $v _ { H }$ is small and then decreasing with $v _ { H }$ . It is interesting to contrast this result with Proposition $4 ( \mathrm { i i } )$ where profit is a monotonically increasing function of $v _ { H }$ . However, this result can be understood by examining the regions under which this result holds. When the seller’s profit is decreasing with $v _ { H } ,$ , it is not optimal for the seller to target the high-valuation bidder. The region in which the seller targets the high-valuation bidder is a subset of the region where the seller’s profit is increasing with $v _ { H }$ . The reason why the seller stops targeting the high-valuation bidder even when the profit is increasing with $v _ { H }$ is that couponing carries a cost in terms of potential loss when only the high-valuation bidder enters the auction.

## 4.3. Targeted Couponing to the Low-Valuation Bidder

In this section we examine the seller’s strategy where she targets a coupon at the low-valuation bidder only. Recall that when the seller targets only the high-valuation bidder, then she can use couponing to

![](/api/attachments/63CXHJ5S/fulltext/images/5ae6d8d64a75406bbe151c9188510d92ab0269932b93971206a23eca9d80b28b.jpg)  
increase the entry probability of the high-valuation bidder but cannot increase value extraction. By contrast, when the seller targets the low-valuation bidder, she can use couponing to increase the entry probability of the low-valuation bidder and also enhance value extraction from the high-valuation bidder. In this case, the revenue to the seller is $( p _ { L } \cdot p _ { H } ) ( v _ { L } + c _ { L } ) + ( p _ { L } )$ $( 1 - p _ { H } ) ( - c _ { L } )$ . The first term highlights the value extraction role of $c _ { L }$ when both bidders enter the auction. The first term also indicates the influence of joint entry probability $p _ { L } \cdot p _ { H }$ , which also serves to increase revenue. Targeting the low-valuation bidder can help the seller adjust the entry probabilities so as to increase the joint entry probability. Finally, the second term $\left( { { p } _ { L } } \right)$ $( 1 - p _ { H } ) ( - c _ { L } )$ shows the cost of couponing when only the low-valuation bidder enters the auction. Proposition 7 states the solution in the interior region when the seller considers targeting only the low-valuation bidder.

Proposition 7 (Interior Region). When the seller targets an optimal coupon only to the low-valuation bidder, the equilibrium entry probabilities of the bidders in the interior region are $p _ { L } = ( 1 - v _ { H } ) ( c _ { I . } ^ { * } + v _ { L } ) / ( \kappa - ( c _ { I . } ^ { * } + v _ { L } ) ^ { 2 } )$ and $p _ { H } = 1 -$ $\kappa ( 1 - v _ { H } ) / ( \kappa - ( c _ { L } ^ { * } \bar { + } v _ { L } ) ^ { 2 } )$ <sup>)</sup> when the high-valuation bidder’s valuation is relatively large such that

$$
v _ {H} > \max \left\{\frac {\kappa + 3 v _ {L} ^ {2}}{3 \kappa + v _ {L} ^ {2}}, 1 + v _ {L} + c _ {L} ^ {*} - \frac {\kappa}{v _ {L} + c _ {L} ^ {*}} \right\}.
$$

The optimal coupon value is $c _ { \scriptscriptstyle I } ^ { \scriptscriptstyle * } = 2 ^ { 1 / 3 } ( b ^ { 2 } - 3 a c ) / ( 3 a e ) +$ $e / ( 3 2 ^ { \dot { 1 } / 3 } a ) - b / ( 3 a )$ , where $a \overset { \sim } { = } - 2 ( 3 - 2 v _ { H } ) , \ b = - 3$ $( 5 - 3 v _ { H } ) v _ { L } , c = 2 ( 2 \kappa v _ { H } - \kappa ) - 6 ( 2 - v _ { H } ) v _ { L } ^ { 2 } , d = v _ { L } ( v _ { H } .$ $( 3 \kappa + v _ { L } ^ { 2 } ) - \kappa - 3 v _ { L } ^ { 2 } )$ , and

$$
\begin{array}{r l} & {e = (9 a b c - 2 b ^ {3} - 2 7 a ^ {2} d} \\ & {\qquad + \sqrt {4 (3 a c - b ^ {2}) ^ {3} + (9 a b c - 2 b ^ {3} - 2 7 a ^ {2} d) ^ {2}}) ^ {1 / 3}.} \end{array}
$$

The expected profit of the seller is $\pi _ { I _ { . } } ^ { * } = ( ( 1 - v _ { H } ) ( c _ { I _ { . } } ^ { * } + v _ { L } )$ $( k v _ { H } v _ { L } \ + \ { c _ { L } ^ { * } } ( 2 \dot { k } v _ { H } \ - \ k \ - \ 3 v _ { L } ^ { 2 } ) \ \stackrel { \sim } { - \ } { c _ { L } ^ { * 3 } } \ - \ 3 c _ { L } ^ { * 2 } v _ { L } \ \stackrel { \sim } { - \ } { v _ { L } ^ { 3 } } ) ) /$ $( ( c _ { L } ^ { * } + v _ { L } ) ^ { 2 } - \kappa ) ^ { 2 }$

The seller considers targeting the low-valuation bidder in the interior only when he does not enter often enough. The low-valuation bidder enters less often when his relative participation cost (κ<sup>)</sup> is high enough (the condition stated in Proposition 7 can be rewritten as $( \kappa > v _ { { I } } ^ { 2 } ( 3 - v _ { { H } } ) / ( 3 v _ { { H } } - \hat { 1 ) } ) \}$ ), and the highvaluation bidder enters more often when his valuation is high enough $( v _ { H } > ( 1 + 3 v _ { L } ^ { 2 } ) / ( 3 + v _ { L } ^ { 2 } ) )$ , as reported in Proposition $\check { 7 } .$

Proposition 7 shows that if the seller follows a strategy of targeting only the low-valuation bidder, then she issues a coupon of strictly positive value when the valuation of the high-valuation bidder is relatively high. When the seller targets a coupon to the lowvaluation bidder, the entry probabilities of both bidders are afected. From observation it is easy to see that $p _ { H }$ decreases with $c _ { L } ^ { * } .$ , whereas $p _ { L }$ increases with $c _ { L } ^ { * }$ .

Proposition 8 (Boundary Region). The strategy of targeting the low-valuation bidder in the boundary region is optimal when the high-valuation bidder’s valuation is relatively large such that (i) when $\begin{array} { r } { \frac { 1 } { 2 } ( 1 + 3 v _ { L } ) < v _ { H } \leq 1 } \end{array}$ + $v _ { L } + c _ { L B 1 } ^ { * } - \kappa / ( v _ { L } + c _ { L B 1 } ^ { * } ) ,$ , the equilibrium entry probabilities of the bidders in the boundary are $p _ { L } = 1$ and $p _ { H } = 1 - \kappa ( 1 - v _ { H } ) / ( \kappa - ( c _ { L B 1 } ^ { * } + v _ { L } ) ^ { 2 } )$ . The optimal coupon value in the boundary is $\overset { \vartriangle { } } { c _ { L B 1 } ^ { \ast } } = \frac { 1 } { 4 } \big ( - 1 + 2 \boldsymbol { v } _ { H } - 3 \boldsymbol { v } _ { L } \big )$ , and the expected profit of the seller is $\pi _ { L B 1 } ^ { \ast } = ( v _ { H } - v _ { L } ) v _ { L } +$ $\mathsf { \Omega } _ { 8 } ^ { 1 } ( 1 - \mathsf { \dot { 2 } } v _ { H } + \mathsf { \dot { 3 } } v _ { L } ) ^ { 2 }$ . (ii) When $v _ { H } \leq a n d ~ 1 + c _ { L B 1 } ^ { * } + v _ { L } -$ $\begin{array} { r } { \dot { \kappa } / ( c _ { L B 1 } ^ { * } + v _ { L } ) < v _ { H } \le 1 + c _ { L } ^ { * } + v _ { L } - \kappa / ( c _ { L } ^ { * } + v _ { L } ) } \end{array}$ , the equilibrium entry probabilities of the bidders in the boundary are $p _ { L } = 1$ and $p _ { H } = 1 - \kappa ( \bar { 1 } - v _ { H } ) / ( \kappa - ( c _ { L B 2 } ^ { * } + v _ { L } ) ^ { 2 } )$ . The optimal coupon value in the boundary is $c _ { L B 2 } ^ { \ast } = \scriptstyle { \frac { 1 } { 2 } } ( v _ { H } - 1 +$ $\sqrt { 1 + 4 \kappa + ( v _ { H } - 2 ) v _ { H } } - 2 v _ { L } )$ , and the expected profit of the seller is $\pi _ { L B 2 } ^ { * } = { \textstyle { \frac { 1 } { 2 } } } ( \sqrt { 1 + 4 \kappa + ( - 2 + v _ { { \scriptscriptstyle H } } ) v _ { { \scriptscriptstyle H } } } - 4 \kappa - ( 1 - v _ { { \scriptscriptstyle H } } )$ $( 1 - v _ { L } ) + \sqrt { 1 + 4 \kappa - ( 2 - v _ { H } ) v _ { H } } v _ { L } )$

The diference between the two boundary solutions (Boundary 1 and Boundary 2) stems from the formulation used to derive the optimal value of the coupon in these regions and is therefore technical. These technical diferences are discussed in the proof of Proposition 8 in Appendix B. It is interesting to note in Proposition 8 that the seller sometimes finds it optimal to issue a coupon to the low-valuation bidder even when he always enters the auction. This occurs because the seller is motivated to target the low-valuation bidder for two reasons: (i) to optimize the joint entry probability and (ii) to improve revenue by increasing value extraction from the high-valuation bidder. When both bidders enter the auction, the high-valuation bidder has to pay a larger amount when the low-valuation bidder has a coupon. We refer to this as the value extraction role of couponing. It can also be seen that the optimal coupon amount in the boundary region is decreasing with the valuation of the low-valuation bidder, and it is increasing with the valuation of the high-valuation bidder.

The regions for interior and boundary solutions stated in Propositions 7 and 8 are shown in Figure 5. Please note that we refer to the interior region as “Uncertain entry of L and $H ^ { \prime \prime }$ and the two boundary regions as $^ { \prime \prime } L$ always enters 1, H uncertain entry” and $^ { \prime \prime } L$ always enters ${ \dot { 2 } } ,$ H uncertain entry” in Figures 5 and 6. We can see that the region for targeting the lowvaluation bidder is larger when $v _ { H }$ is large and κ is relatively large or $v _ { L }$ is small and κ is relatively large. The boundary region where the low-valuation bidder always enters the auction $( p _ { L } = 1 )$ occurs when κ is small relative to $v _ { H } ,$ or $v _ { L }$ is small. Note that the coupon amount in the boundary region decreases with $v _ { L }$ , as stated in Proposition 8.

Figure 5. Target Low-Valuation Bidder Case: (a) Valuation of the High-Valuation Bidder and the Low-Valuation Bidder’s Relative Participation Cost $( v _ { L } = 0 . 2 )$ and (b) the Low-Valuation Bidder’s Valuation and Relative Participation Cost $( v _ { H } = 0 . 9 )$  
(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/6f9e0dacdada084463460845e669f0f9224e9dd822c5143287d103f888819bf3.jpg)

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/028b1d3831baf7d18ec382b6e5da6a15edda6eb1b19457d701414cfe9257827d.jpg)

Figure 6. Target Low-Valuation Bidder Case: (a) Impact of the Low-Valuation Bidder’s Valuation on Profit <sup>(</sup>κ <sup></sup> 0.09<sup>)</sup> and (b) Impact of the Low-Valuation Bidder’s Relative Participation Cost on the Optimal Coupon Amount $( v _ { H } = 0 . 9 )$

(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/e46e4c2c937a626afcda9abd0b7b455d00b131577e7fbd3717ca8a402e14020f.jpg)

Figure 6(a) shows the seller’s profit as a function of $v _ { L } .$ We can see the medium dashed curve in the interior region and the short dashed curve and the long dashed curve in the boundary regions are both increasing with $v _ { L }$ . In these regions, it is optimal to target the low-valuation bidder. The very long dashed curve shows where it is not optimal to issue any coupons. In this region, the optimal profit can be a nonmonotone function of the valuation of the low-valuation bidder as discussed in Section 3. Increasing $v _ { H }$ shifts the profit curves upward, as is shown in Figure 6(a).

From Figure 6(b), it is easy to see that the optimal coupon amount to the low-valuation bidder is increasing with κ. Note that in the case of issuing a coupon to the high-valuation bidder, the coupon amount decreases with κ (Figure 4(b)). This is so because as κ increases, the low-valuation bidder enters less often and therefore requires a larger coupon amount to induce more entry from the low-valuation bidder, which increases the joint entry probability.

In the next section, we examine the overall optimal couponing strategy of the seller.

## 4.4. Optimal Strategy for Targeted Couponing

Now we determine the seller’s overall coupon targeting strategy by comparing the profit and feasibility conditions derived in Sections 3, 4.2, and 4.3. The feasible region for targeting only the high-valuation bidder is given in Propositions 4 and 5, and the feasible region for targeting only the low-valuation bidder is given in Propositions 7 and 8.

Proposition 9. Optimal Strategy for Targeted Couponing:

(i) The seller targets the high-valuation bidder when the high-valuation bidder’s valuation is relatively small such that $( \mathrm { a } ) ~ 2 - 2 \kappa / v _ { L } < v _ { H } < 2 v _ { L } ^ { 2 } / ( \kappa + v _ { L } ^ { 2 } )$ or (b) $v _ { H } \leq 2 -$ $2 \kappa / v _ { L }$ and $v _ { H } < 2 v _ { L }$ . The optimal value of the coupon for the interior region is stated in Proposition 4, and that for the boundary region is stated in Proposition 5.

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/ebbc138c85ee4fac1cbbedab850ecdbab703cb5cbaf65948791a2c32925fdd61.jpg)

(ii) The seller targets the low-valuation bidder when the high-valuation bidder’s valuation is relatively large such that (a) $v _ { H } > \mathrm { m a x } \{ ( \kappa + 3 v _ { I } ^ { 2 } ) / ( 3 \kappa + v _ { I } ^ { 2 } ) , 1 + v _ { L } ^ { - } + c _ { I } ^ { * } -$ $\kappa / ( v _ { L } + c _ { L } ^ { * } ) \} _ { . }$ , or (b) $\begin{array} { r } { \frac { 1 } { 2 } \big ( 1 + \tilde { 3 v _ { L } } \big ) < v _ { H } \tilde { \le 1 } + v _ { L } + \bar { c _ { L B 1 } ^ { * } } - } \end{array}$ $( \kappa / ( v _ { L } + c _ { L B 1 } ^ { * } ) )$ , or $\begin{array} { r } { \dot { \mathbf { \sigma } } ( \mathbf { c } ) \mathbf { \bar { \boldsymbol { v } } } _ { H } > 1 - \left( \kappa / v _ { L } \right) + v _ { L } , v _ { H } \leq 1 + c _ { I } ^ { * } . } \end{array}$ + $v _ { L } - \kappa / ( c _ { I . } ^ { * } + v _ { L . } )$ <sup>)</sup> and $v _ { H } > 1 + c _ { L B 1 } ^ { * } + v _ { L } - \kappa / ( c _ { L B 1 } ^ { * } + v _ { L } ) ,$ . The optimal value of the coupon for the interior region is stated in Proposition ${ \bar { 7 } } ,$ and that for the boundary region is stated in Proposition 8.

(iii) The region in which the firm targets the low-valuation bidder does not overlap with the region in which the firm targets the high-valuation bidder.

Why is it optimal to target the high-valuation bidder when his valuation is low to moderate relative to the valuation of the low-valuation bidder and κ, whereas it is optimal to target the low-valuation bidder when the valuation of the high-valuation bidder is large relative to the valuation of the low-valuation bidder and κ. The intuition behind this result can be understood through the interplay of the two efects of couponing in our setup, namely, (i) targeted couponing impacts the entry probability of the targeted as well as nontargeted bidder to increase the joint entry probability, and (ii) targeted couponing can be used to extract value from the high-valuation bidder.

The impact of the optimal couponing strategy is shown in Figure $^ { 7 , }$ which illustrates the joint entry probability with κ. We refer to the interior regions where the seller targets the coupon to the highvaluation bidder and to the low-valuation bidder as “Target H: Uncertain entry of L and $H ^ { \prime \prime }$ and “Target L: Uncertain entry of L and $\cdot \mathcal { H } , ^ { \prime \prime }$ respectively. The boundary region where the low-valuation bidder always enters and the seller targets the high-valuation bidder is labeled as “Target H: L always enters, H uncertain entry” in Figure 7. The long dotted portion of the curve (on the left, Panel (a)) shows the joint entry probability when the seller targets the high-valuation bidder with an optimal coupon, and the long dotted portion of the curve (top right) shows the joint entry probability when the seller targets the low-valuation bidder. Finally, the solid curve shows the joint entry probability when the seller does not target either bidder.

Figure 7. Joint Entry Probability as a Function of (a) the Low-Valuation Bidder’s Relative Participation Cost $( v _ { H } = 0 . 7 , v _ { L } = 0 . 5 )$ and (b) the Low-Valuation Bidder’s Valuation $( \kappa = 0 . 3 , v _ { H } = 0 . 7 )$  
(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/2738cbb2c6837c2a02e84e9d72346ec21efac1b6b440edb66f036cccf674210b.jpg)

We now describe the impact of couponing on entry probabilities. The entry probability of each bidder depends on their own valuation and participation cost and also on the valuation and participation cost of the other bidder. The entry probability of the bidder who receives the coupon (targeted bidder) increases because his expected surplus from entering the auction increases. At the same time, the entry probability of the bidder without coupon (nontargeted bidder) decreases because his expected surplus is a decreasing function of the entry probability of the targeted bidder. This is because entry of the targeted bidder can reduce both the probability of winning and the surplus when the nontargeted bidder wins. Since the entry probabilities of the bidders in our setup are interdependent, targeted couponing impacts the targeted as well as the nontargeted bidder. The seller obtains a positive profit only when both bidders enter the auction. Therefore, the joint entry probability of the two bidders is key to maximizing the seller’s profit. Thus, profit can be improved by adjusting the entry probability of the two bidders through the use of targeted couponing. When the entry probabilities are such that one bidder enters much more often than the other, targeted couponing can be used to increase the entry probability of the bidder who enters less often.

The second efect of couponing is value extraction. When both bidders enter the auction, the highvaluation bidder is forced to bid higher if the lowvaluation bidder has a coupon. Thus, the seller may obtain an additional benefit from targeting the lowvaluation bidder. The value extraction benefit is moderated by the impact of couponing on entry probabilities because targeting the low-valuation bidder will lead to reduced entry by the high-valuation bidder, which can lead to a reduction in profit. Note that there is no value extraction benefit when the coupon is targeted to the high-valuation bidder.

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/35c60f207a60e88f434b3c70f3947b48d731817c7a19bc35b786edb531408ee5.jpg)

The optimal couponing strategy is determined by balancing these two efects of couponing with the potential revenue loss from couponing. This revenue loss from couponing is incurred when a bidder who has a coupon is the only one who enters the auction or he wins the auction (if the high-valuation bidder is targeted). When this happens the bidder is able to cash his coupon without any gain to the seller. Figure 8 shows the regions in which it is optimal to target the coupon either to the low- or high-valuation bidder within the parameter space formed by $v _ { L } , v _ { H } ,$ , and κ. Please note that we refer to the interior region where the seller targets the coupon to the high-valuation bidder as “Target H: Uncertain entry of L and $H , \prime \prime$ and that where she targets the low-valuation bidder as “Target L: Uncertain entry of L and H.” The boundary regions where the low-valuation bidder always enters and the seller targets the high-valuation bidder are labeled as “Target H: L always enters, H uncertain entry” in Figures 8 and 9. Similarly, the two boundary regions where the seller targets the low-valuation bidder and the low-valuation bidder always enters are labeled as “Target L: L always enters 1, H uncertain entry” and “Target L: L always enters 2, H uncertain entry.”

These regions can be explained by noting that when κ is relatively small $\mathrm { ~ o r ~ } v _ { L }$ is relatively large, the entry probability of the low-valuation bidder is high, and this decreases the entry probability of the highvaluation bidder. To maximize profit, the seller seeks to optimize the joint entry probability by targeting the high-valuation bidder. When κ is relatively large or $v _ { L }$ is relatively small, the entry probability of the lowvaluation bidder is low. The seller seeks to optimize the joint entry probability by targeting the low-valuation bidder. When the relative participation cost for the lowvaluation bidder (κ<sup>)</sup> is relatively moderate, then the bidders’ entry probabilities are such that the gain to the seller from couponing is not suficient to overcome the potential revenue loss from the coupon. Hence, when κ is relatively moderate, the seller prefers not to issue any coupons. As noted in Proposition 9, part (iii), the regions where couponing is optimal (Figure 8) do not overlap. However, in a model with more than two bidders, it may be optimal to issue coupons to more than one bidder at a time.

Figure 8. Interior and Boundary Regions for Targeting Low- and High-Valuation Bidders with (a) Valuation of the High-Valuation Bidder and Low-Valuation Bidder’s Relative Participation Cost $( v _ { L } = 0 . 2 5 )$ and (b) Valuation of the Low-Valuation Bidder and Low-Valuation Bidder’s Relative Participation Cost $( v _ { H } = 0 . 7 )$  
![](/api/attachments/63CXHJ5S/fulltext/images/f1e9a6d4245ab490a135fdc4ffe76f6c57d70969687ba1ca2ff3f354716f6f60.jpg)

Figure 9(a) shows how the optimal coupon value changes with the relative participation cost of the lowvaluation bidder. When the relative participation cost of the low-valuation bidder is low, the firm targets the high-valuation bidder; when it is moderate, the firm does not issue coupons; and when it is high, the firm targets the low-valuation bidder. Figure 9(b) shows the expected profit of the firm with the valuation of the lowvaluation bidder under an optimal couponing strategy. When the valuation of the low-valuation bidder is low, the firm targets the low-valuation bidder; when it is moderate, the firm does not issue coupons; and when it is high, the firm targets the high-valuation bidder.

Figure 9. (a) Impact of the Low-Valuation Bidder’s Relative Participation Cost on the Optimal Coupon Amount to Low- and High-Valuation Bidders $( v _ { H } = 0 . 7 , v _ { L } = 0 . 5 )$ and (b) Impact of the Low-Valuation Bidder’s Valuation on the Profit from Optimal Targeting $( \kappa = 0 . 1 , v _ { H } = 0 . 7 )$  
(a)  
![](/api/attachments/63CXHJ5S/fulltext/images/f3ca1fa05da5766c3696f14b6d916ae93c5443e032ad169df65b2b5c7bfe4227.jpg)

(b)  
![](/api/attachments/63CXHJ5S/fulltext/images/943dfdb26a0e639ef4672c6d658a77111d3418a4c34beeba18fc0d38fca7c205.jpg)

Recall from Proposition 2 that when the seller does not use couponing, the joint entry probability of the two bidders as well as the seller’s profit is a nonmonotone function of the bidders’ valuations and the participation cost parameter of the low-valuation bidder. It is interesting to note in Figure 9(b) that when the seller issues coupons, the seller’s profit becomes a monotone function of the valuation of the low-valuation bidder. We have verified that this observation also holds true with respect to the valuation of the high-valuation bidder and the relative participation cost of the lowvaluation bidder (κ<sup>)</sup>. Thus, we find that when couponing is introduced, the nonmonotonicity result is no longer present. This occurs because couponing allows the seller to internalize the externality caused by the entry of one bidder on other bidders.

## 5. Discussion

In this paper, we analyze the impact of targeted coupons issued by a seller to bidders in an auction setting. We first provide an overview of our results and then discuss our contributions and highlight some managerial implications that follow from our analysis.

We find that under endogenous entry of bidders, the seller’s revenue can be a nonmonotone function of the valuations and participation costs of the bidders. The optimal couponing strategy of the seller depends on the relative values of the valuations of the bidders and the relative participation cost of the low-valuation bidder. We find that it is optimal for the firm to target the high-valuation bidder when his valuation is low, the relative participation cost of the low-valuation bidder is low, and the valuation of the low-valuation bidder is relatively high. On the other hand, the firm should target the low-valuation bidder when the highvaluation bidder’s valuation is moderate to high and the relative participation cost of the low-valuation bidder is moderate to high. The seller earns a profit only when both bidders enter the auction, yet couponing may be optimal for the seller even when it leads to a reduction in the joint entry probability of the two bidders. We find that it is never optimal for the firm to simultaneously target both bidders with coupons. Finally, we also determine the optimal coupon values under each targeting strategy and find that the value of the low-valuation bidder’s optimal coupon increases when the relative participation cost of the low-valuation bidder increases.

We find novel results that are diferent from prior literature on couponing. In the context of online auctions, it can be optimal for the seller to issue targeted coupons to the high-valuation bidder. By contrast, prior literature recommends issuing coupons to low-valuation consumers for price discrimination or to marginal consumers to poach them from competitors (Narasimhan 1984, Levedahl 1984, Sweeney 1984,

Varian 1989, Shafer and Zhang 1995, Fudenberg and Tirole 2000). Another counterintuitive result is that there exist conditions under which it can be optimal to target the low-valuation bidder even when he always enters the auction. This is also diferent from the literature, where coupons are typically used to entice consumers who may not otherwise purchase.

These novel findings can be understood in the context of the two key forces driving couponing in auctions which difer from the key forces in couponing in the retail context. The two forces are (i) the value extraction role of coupons and (ii) the influence of coupons on the entry probability of the bidders. The value extraction role of coupons allows the seller to extract value from the winning bidder by making him pay a higher amount when the coupon increases the second highest bid amount. This dynamic does not exist in the couponing literature in the retail context where there is no supply-side constraint and, hence, consumers do not compete for a unit of the product. The second force of couponing in auctions influences bidders’ entry probability in two ways—there is a positive impact on the entry probability of the bidder who receives the coupon and a negative impact on the entry probability of other bidders. By contrast, in couponing in the retail context, there is only a positive impact on purchase probability of the recipient of the coupon.

Our analysis generates insights that have implications for online auctioneers and platforms when there is endogenous entry based on valuations and asymmetric participation costs. Participation costs include the cost of inspecting auction goods, the time cost of monitoring and participating in an auction, the search cost, and the delay cost from waiting for the auction to close. The extent of impact of participation costs on diferent bidders is likely to be diferent. The high-valuation bidders are likely to incur greater participation costs due to their higher opportunity cost of time. These higher participation costs may result in lower entry probability for high-valuation bidders. Therefore, managers who sell items that appeal to high-valuation buyers, such as expensive artwork and real estate, may need to provide incentives to highvaluation buyers. For example, Sotheby’s is a leading auction house for high-value collectible items, and they ofer value-added services only to “Sotheby’s Preferred” members, where membership is by invitation. This lowers the participation cost for high-valuation bidders and its impact is similar to issuing coupons to high-valuation bidders in our model. Similarly, Auction.com, which auctions residential and commercial real estate has a VIP program for high-valuation buyers. Their VIP program provides several benefits including dedicated account associates, a dedicated closing team, waiver of deposit and earnest money, and a streamlined process for postauction activities.

Our findings related to the nonmonotonicity of the joint entry probability of bidders have important implications for managers. The presence of a very high valuation buyer can make it unattractive for others to participate in the auction. Such concerns may be addressed by limiting the number of items that a single bidder can win in an auction. For example, the auctioneer may limit any single bidder to winning at most 20% of the auction inventory. This would reassure bidders with moderate or low valuation that they have a reasonable probability of winning an auction.

Managers must be careful in using coupons in auctions because they lead to externalities on bidders who do not have coupons. Sometimes, this property of auction coupons can be leveraged to optimize the joint entry probability of multiple bidders. We also find that it can be optimal to issue coupons to low-valuation bidders even when they always enter the auction. Online automobile auction firms such as Copart.com and Car-Max.com should consider ofering coupons to lowvaluation bidders who regularly attend their auctions but rarely win. Such a strategy is beneficial because of the value extraction benefit to the seller—the low valuation bidder who receives a coupon can cause an increase in the amount realized from the bidder who wins the auction.

Targeted couponing strategy can inform managers at eBay, which is one of the largest online auction platforms. It runs a wide variety of auctions every day ranging from high-value industrial items to low-value consumer items. The auction platform used by eBay is the same across all items. However, bidder valuations and participation costs are likely to be very diferent in diferent categories of auctions. eBay can actively reduce the participation costs faced by high-value bidders by providing value-added services related to search and authentication to high-valuation bidders. They can also monitor the items listed in the highvalue categories such as “Business and Industrial” to prevent low-value items being listed there. eBay could also partner with targeted couponing firms such as Aucser.com, Criteo, and Highco to make it easier for sellers to issue targeted coupons. High-valuation bidders may face large participation costs either when they are new to the auction site and thus need to invest time and efort to learn the interface and the rules for auctions or when the auction duration is relatively long. We recommend that when high-valuation bidders face a relatively large participation cost, managers should provide coupons targeted at them.

## 6. Conclusion and Limitations

This paper analyzes the role of targeted couponing in online auctions. We find that the role of couponing in auctions is substantially diferent from that in other retail settings. Our stylized model assumes a privatevalue auction. How would the results change in the context of common-value auctions? If the bidder valuations were to be common value, then the impact of couponing would be diferent on the bidding behavior and the entry probability of bidders. In common-value auctions, the bidder without a coupon may bid more because the bidder with a coupon bids higher, and this may impact the entry probabilities of the bidders. One of the limitations of our model is that it features two bidders. Future research can study the conditions under which these forces generalize to multiple-bidder auctions. There is some empirical evidence that the key forces discussed in our model may remain relevant even when the number of bidders is large (Wang et al. 2008). Moreover, we have also assumed that bidder valuations are common knowledge, and this research can be extended by allowing bidder valuations to be private information.

We studied a model of a single seller; however, coupons could be used to attract bidders and obtain a competitive advantage over other sellers in a setting with competing sellers. Another extension could be the analysis of couponing by an auction platform owner. For example, eBay has an “eBay Bucks” program that awards $2 \%$ cash back to auction winners, which could be studied. Future research can also study the impact of relaxing our assumption of zero reserve price and the role of coupons in multiunit auctions.

Appendix A. Summary of Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\nu_{H}$ </td><td>Valuation of high-valuation bidder</td></tr><tr><td> $\nu_{L}$ </td><td>Valuation of low-valuation bidder</td></tr><tr><td> $p_{H}$ </td><td>Entry probability of high-valuation bidder</td></tr><tr><td> $p_{L}$ </td><td>Entry probability of low-valuation bidder</td></tr><tr><td> $\kappa$ </td><td>Relative participation cost of low-valuation bidder</td></tr><tr><td> $\tilde{t}_{H}$ </td><td>Draw of participation cost of high-valuation bidder</td></tr><tr><td> $\tilde{t}_{L}$ </td><td>Draw of participation cost of low-valuation bidder</td></tr><tr><td> $s_{H}$ </td><td>Expected surplus of high-valuation bidder</td></tr><tr><td> $s_{L}$ </td><td>Expected surplus of low-valuation bidder</td></tr><tr><td> $c_{LB1}^{*}$ </td><td>Optimal coupon targeted to low-valuation bidder in Boundary 1</td></tr><tr><td> $c_{H}$ </td><td>Coupon amount targeted to high-valuation bidder</td></tr><tr><td> $c_{H}^{*}$ </td><td>Optimal coupon amount targeted to high-valuation bidder</td></tr><tr><td> $c_{L}$ </td><td>Coupon amount targeted to low-valuation bidder</td></tr><tr><td> $c_{L}^{*}$ </td><td>Optimal coupon amount targeted to low-valuation bidder</td></tr><tr><td> $\pi_{N}^{*}$ </td><td>Expected profit of seller with no couponing</td></tr><tr><td> $\pi_{H}^{*}$ </td><td>Expected profit of seller with optimal targeted couponing to high-valuation bidder</td></tr><tr><td> $\pi_{L}^{*}$ </td><td>Expected profit of seller with optimal targeted couponing to low-valuation bidder</td></tr><tr><td> $J(p_{L},p_{H})$ </td><td>Joint entry probability of both types of bidders</td></tr><tr><td> $c_{LB2}^{*}$ </td><td>Optimal coupon targeted to low-valuation bidder in Boundary 2</td></tr></table>

Appendix B. Proofs of Lemmas and Propositions Lemma 1a. It is never optimal for the seller to issue a coupon to both bidders such that when both bidders enter, the low-type bidder wins the auction.

Proof. We now show that it is never optimal for the seller to issue coupons to both types of bidders such that when both bidders enter, the low-type bidder wins the auction. There are two benefits to targeting a coupon to the low-type bidder: (i) increase in the joint entry probability of the two bidders $( p _ { L } \cdot p _ { H } )$ and (ii) increase in value extraction from the hightype bidder when both enter. When $c _ { L } < v _ { H } + c _ { H } - v _ { L }$ and both bidders enter, seller’s revenue is $v _ { L } + c _ { L } - c _ { H }$ . When $c _ { L } >$ $v _ { H } + c _ { H } - v _ { L }$ and both enter, seller’s revenue is $v _ { H } + c _ { H } - c _ { L }$ When $c _ { L }$ is in the neighborhood of $v _ { H } + c _ { H } - v _ { L }$ from the left side, then revenue approaches $v _ { H }$ . When $c _ { L }$ is in the neighborhood of $v _ { H } + c _ { H } - v _ { L }$ from the right side, then revenue approaches $v _ { L }$ . Since $v _ { H } > v _ { L } ,$ there is a discrete reduction in revenue when $c _ { L }$ crosses from the left neighborhood to the right neighborhood. The impact of this increase in $c _ { L }$ on the joint entry probability is neutral or negative. This is so because when $\kappa < 1$ and $v _ { L } + c _ { L }$ is in the neighborhood of $v _ { H } + c _ { H } ,$ the low-type bidder enters more often than the hightype bidder. Increasing the coupon to the low-type bidder further increases the entry probability of the low-type bidder, thus causing a negative impact on the joint entry probability. It is easy to see that when $\kappa = 1$ , the impact on the joint entry probability is neutral. Hence, it is never optimal for the seller to give coupons to both types of bidders such that the lowtype bidder wins the auction when both bidders enter. <sup></sup>

Proof of Lemma 1. As reported in Section 2.1, the equilibrium entry probabilities are

$$
p _ {L} = \frac {(1 - c _ {H} - v _ {H}) (c _ {L} + v _ {L})}{\kappa - (c _ {L} + v _ {L}) ^ {2}},\tag{B1}
$$

$$
p _ {H} = 1 - \frac {\kappa (1 - c _ {H} - v _ {H})}{\kappa - (c _ {L} + v _ {L}) ^ {2}}.\tag{B2}
$$

Setting, $c _ { L } = c _ { H } = 0$ in Equations (B1) and (B2), we obtain the equilibrium entry probabilities reported in Lemma 1 for the interior region.

The interior region is characterized by the following conditions: $0 < p _ { L } < 1 , 0 < p _ { H } < 1$ . The condition $p _ { L } < 1$ implies that $( 1 - v _ { H } ) v _ { L } / ( \kappa - v _ { I } ^ { 2 } ) < 1$ . Simplifying, we get the condition $\kappa > v _ { L } ( 1 + v _ { L } - v _ { H } )$ stated in Lemma 1. This condition also ensures that $p _ { H } < 1$ . To see this, note that $p _ { H } < 1 \Leftrightarrow \kappa > v _ { L } ^ { 2 } / v _ { H }$ Replacing $\kappa = v _ { L } ( 1 + v _ { L } - v _ { H } )$ in this condition and simplifying, we get $( v _ { H } - 1 ) ( v _ { H } - v _ { L } ) v _ { L } < 0 .$ . One can see that this condition is always true. Hence, whenever $\kappa > v _ { L } ( 1 + v _ { L } - v _ { H } ) .$ then $\kappa > v _ { { \scriptscriptstyle L } } ^ { 2 } / v _ { { \scriptscriptstyle H } } ,$ , and therefore $p _ { H } < 1$

The condition $p _ { H } > 0$ implies that $\kappa ( 1 - v _ { H } ) / ( \kappa - v _ { I } ^ { 2 } ) < 1$ ⇔ $\kappa v _ { H } > v _ { L } ^ { 2 }$ . As shown above, $\kappa > v _ { L } ( 1 + v _ { L } - v _ { H } )$ ensures that this condition is satisfied. The condition $p _ { L } > 0$ can be written as $( 1 - v _ { H } ) v _ { L } / ( \kappa - v _ { I } ^ { 2 } ) > 0$ . It follows from $\kappa > v _ { \cal L } ^ { 2 } / v _ { \cal H }$ that $\kappa >$ $v _ { L } ^ { 2 } .$ , so the denominator is positive. Condition $v _ { H } < 1$ ensures that the numerator is positive. Hence, $p _ { L } > 0$

Substituting the equilibrium entry probabilities reported in Lemma 1 into the profit function given in Equation (3), we obtain the seller’s expected profit reported in Lemma 1. <sup></sup> Proof of Lemma 2. Solving the two equations (Equations (1) and (2)) in Section 2.1 and setting $c _ { L } = c _ { H } = 0$ and $v _ { H } = 1$ , we get $p _ { L } = 0$ and $p _ { H } = 1$ . Since only the high-type bidder enters the auction, the seller obtains zero profit. Hence, we obtain part (i) of Lemma 2.

Solving the two equations (Equations (1) and (2)) in Section 2.1 and setting $c _ { L } = c _ { H } = 0$ and $\kappa = v _ { L } ( 1 + v _ { L } - v _ { H } ) .$ , we get $p _ { L } = 1$ and $p _ { H } = v _ { H } - v _ { L }$ . When $\kappa < v _ { L } ( 1 + v _ { L } - v _ { H } ) .$ , then also the low-type bidder always enters, and hence $p _ { L } = 1$ and $p _ { H } = v _ { H } - v _ { L }$ . Hence, we obtain part (ii) of Lemma 2. <sup></sup>

Proof of Proposition 1. We know from the proof of Lemma 1 that $\kappa > v _ { L } ^ { 2 } ;$ therefore,

$$
\begin{array}{l l} \frac {\partial p _ {L}}{\partial \kappa} = - \frac {(1 - v _ {H}) v _ {L}}{(\kappa - v _ {L} ^ {2}) ^ {2}} <   0, & \frac {\partial p _ {L}}{\partial v _ {L}} = \frac {(1 - v _ {H}) (\kappa + v _ {L} ^ {2})}{(\kappa - v _ {L} ^ {2}) ^ {2}} > 0, \\ \frac {\partial p _ {L}}{\partial v _ {H}} = - \frac {v _ {L}}{\kappa - v _ {L} ^ {2}} <   0, & \frac {\partial p _ {H}}{\partial \kappa} = \frac {(1 - v _ {H}) v _ {L} ^ {2}}{(\kappa - v _ {L} ^ {2}) ^ {2}} > 0, \\ \frac {\partial p _ {H}}{\partial v _ {L}} = - \frac {2 \kappa (1 - v _ {H}) v _ {L}}{(\kappa - v _ {L} ^ {2}) ^ {2}} <   0, & \frac {\partial p _ {H}}{\partial v _ {H}} = \frac {\kappa}{\kappa - v _ {L} ^ {2}} > 0. \end{array}
$$

Proof of Proposition ${ \bf 2 . } ~ \partial \pi _ { N } / \partial v _ { H } = v _ { L } ^ { 2 } ( \kappa + v _ { L } ^ { 2 } - 2 \kappa v _ { H } ) / ( \kappa -$ $v _ { L } ^ { 2 } ) ^ { 2 }$ . Solving $\partial \pi _ { N } / \partial v _ { H } = 0$ yields a unique root: $\tilde { v } _ { H } = ( \kappa +$ $v _ { L } ^ { 2 } ) / ( 2 \kappa )$ . Testing to the left and right of this root, it is easy to verify that $\partial \bar { \pi } _ { N } / \partial v _ { H } > 0$ when $v _ { H } < \tilde { v } _ { H }$ and $\partial \pi _ { N } / \partial v _ { H } < 0$ when $v _ { H } > \tilde { v } _ { H }$ . This yields part (i) of Proposition 2.

$$
\frac {\partial \pi_ {N}}{\partial \kappa} = \frac {(1 - v _ {H}) v _ {L} ^ {2} (2 v _ {L} ^ {2} - v _ {H} (\kappa + v _ {L} ^ {2}))}{(\kappa - v _ {L} ^ {2}) ^ {3}}.
$$

Solving $\partial \pi _ { N } / \partial \kappa = 0$ yields a unique root: $\tilde { \kappa } = v _ { L } ^ { 2 } ( 2 - v _ { H } ) / v _ { H }$ Testing to the left and right of this root, it is easy to verify that $\partial \pi _ { N } / \partial \kappa > 0$ when $\kappa < \tilde { \kappa }$ and $\partial \pi _ { N } / \partial \kappa < 0$ when $\kappa > \tilde { \kappa }$ This yields part (ii) of Proposition 2.

$\partial \pi _ { N } / \partial v _ { L } = ( 2 \kappa v _ { L } ( 1 - v _ { H } ) ( v _ { H } ( \kappa + v _ { L } ^ { 2 } ) - 2 v _ { L } ^ { 2 } ) ) / ( \kappa - v _ { L } ^ { 2 } ) ^ { 3 } . 5 \mathrm { o l v - \Omega }$ ing $\partial \pi _ { N } / \partial v _ { L } = 0$ yields three roots, $\{ - \sqrt { \kappa v _ { H } / ( 2 - v _ { H } ) } , 0 ,$ $\sqrt { \kappa v _ { H } / ( 2 - v _ { H } ) } \}$ , only one of which is positive and is $\tilde { v } _ { L } =$ $\sqrt { \kappa v _ { H } / ( 2 - v _ { H } ) }$ . We check to see whether this root is in the interior, that is, if $\kappa > v _ { L } ( 1 + v _ { L } - v _ { H } )$ . Rewriting the root and replacing $\kappa = v _ { { I } } ^ { 2 } ( 2 - v _ { { H } } ) / v _ { { H } }$ in $\kappa > v _ { L } ( 1 + v _ { L } - v _ { H } )$ , we get $( 1 - v _ { H } ) v _ { H } \cdot ( v _ { H } - 2 v _ { L } ) v _ { L } < 0$ . This condition is satisfied whenever $v _ { H } < 2 v _ { L }$ . Testing to the left and right of this root, it is easy to verify that $\partial \pi _ { N } / \partial v _ { L } > 0$ when $v _ { L } < \tilde { v } _ { L }$ and $\partial \pi _ { N } / \partial v _ { L }$ $< 0$ when $v _ { L } > \tilde { v } _ { L }$ . This yields part (iii) of Proposition 2. <sup></sup>

Proof of Proposition 3. The equilibrium entry probabilities of the bidders are provided in Equations (B1) and (B2). The expected revenue of the seller is

$$
\begin{array}{r l} \pi_ {L H} = & [ \kappa c _ {H} ((c _ {L} + v _ {L}) (c _ {L} (4 - 3 v _ {H}) + (2 - v _ {H}) v _ {L}) - \kappa v _ {H}) \\ & - \kappa c _ {H} ^ {2} (\kappa + c _ {L} (c _ {L} + v _ {L})) ] \cdot [ (\kappa - (v _ {L} + c _ {L}) ^ {2}) ^ {2} ] ^ {- 1} \\ & - [ (1 - v _ {H}) (c _ {L} ^ {4} + 4 c _ {L} ^ {3} v _ {L} - v _ {L} ^ {2} (\kappa v _ {H} - v _ {L} ^ {2}) \\ & + c _ {L} v _ {L} (\kappa - 3 \kappa v _ {H} + 4 v _ {L} ^ {2}) + c _ {L} ^ {2} (\kappa - 2 \kappa v _ {H} + 6 v _ {L} ^ {2})) ] \\ & \cdot [ (\kappa - (v _ {L} + c _ {L}) ^ {2}) ^ {2} ] ^ {- 1}. \end{array}\tag{B3}
$$

The first order conditions (FOCs) with respect to $c _ { H }$ and $c _ { L }$ are

$$
\begin{array}{r l} & {\frac {\partial \pi_ {L H}}{\partial c _ {H}} = [ \kappa ((c _ {L} + v _ {L}) (c _ {L} (4 - 3 v _ {H}) + (2 - v _ {H}) v _ {L}) - \kappa v _ {H}} \\ & {- 2 c _ {H} (\kappa + c _ {L} (c _ {L} + v _ {L}))) ] \cdot [ (\kappa - (v _ {L} + c _ {L}) ^ {2}) ^ {2} ] ^ {- 1} = 0,} \\ & {\frac {\partial \pi_ {L H}}{\partial c _ {L}} = [ \kappa (- 1 + c _ {H} + v _ {H}) (2 c _ {L} ^ {3} (- 3 + c _ {H} + 2 v _ {H})} \end{array}\tag{B4}
$$

$$
\begin{array}{r l} & {- 2 c _ {L} (\kappa - 3 \kappa c _ {H} - 2 \kappa v _ {H})) ] \cdot [ (\kappa - (v _ {L} + c _ {L}) ^ {2}) ^ {2} ] ^ {- 1}} \\ & {+ [ \kappa (- 1 + c _ {H} + v _ {H}) (+ 3 c _ {L} ^ {2} (- 5 + c _ {H} + 3 v _ {H}) v _ {L}} \\ & {+ 6 c _ {L} (- 2 + v _ {H}) v _ {L} ^ {2} + v _ {L} (- \kappa - 3 v _ {L} ^ {2} - c _ {H} (- 5 \kappa + v _ {L} ^ {2})} \\ & {+ v _ {H} (3 \kappa + v _ {L} ^ {2})) ] \cdot [ (\kappa - (v _ {L} + c _ {L}) ^ {2}) ^ {2} ] ^ {- 1} = 0.} \end{array}\tag{B5}
$$

Solving the two $\mathrm { F O C } \mathbf { s } ,$ , we obtain a unique critical point: $\hat { c } _ { L } =$ $- v _ { L } / 2 < 0$ and $\hat { c } _ { H } = - ( v _ { H } / 2 - 2 ( 2 - v _ { H } ) \big / ( 4 \kappa - v _ { I } ^ { 2 } ) )$ . We have $\hat { c } _ { H } < 0$ when $\kappa > ( v _ { H } v _ { L } ^ { 2 } + 4 ( 2 - v _ { H } ) ) / ( 4 v _ { H } )$ or $\kappa < v _ { \scriptscriptstyle L } ^ { 2 } / 4$ . We now compute the Hessian matrix at the critical point to check whether this critical point is a maxima or minima. The relevant second derivatives are

$$
\begin{array}{r l} & {\left. \frac {\partial^ {2} \pi_ {L H}}{\partial c _ {H} ^ {2}} \right| _ {\hat {c} _ {L}, \hat {c} _ {H}} = - \frac {8 \kappa (4 \kappa - v _ {L} ^ {2})}{(4 \kappa - v _ {L} ^ {2}) ^ {2}} <   0,} \\ & {\left. \frac {\partial^ {2} \pi_ {L H}}{\partial c _ {L} ^ {2}} \right| _ {\hat {c} _ {L}, \hat {c} _ {H}} = \frac {8 \kappa (2 - v _ {H}) ^ {2} (3 v _ {L} ^ {4} - 1 6 \kappa^ {2} - 8 \kappa v _ {L} ^ {2})}{(4 \kappa - v _ {L} ^ {2}) ^ {2} (4 \kappa - v _ {L} ^ {2}) ^ {2}},} \\ & {\left. \frac {\partial^ {2} \pi_ {L H}}{\partial c _ {L} \partial c _ {H}} \right| _ {\hat {c} _ {L}, \hat {c} _ {H}} = \frac {1 6 \kappa (2 - v _ {H}) v _ {L}}{(4 \kappa - v _ {L} ^ {2}) ^ {2}},} \\ & {| H | = \frac {6 4 \kappa^ {2} (2 - v _ {H}) ^ {2}}{(4 \kappa - v _ {L} ^ {2}) (4 \kappa - v _ {L} ^ {2}) ^ {2}} > 0.} \end{array}
$$

Since, at the critical point, $| H | > 0$ and $( \partial ^ { 2 } \pi _ { L H } / \partial c _ { H } ^ { 2 } ) | _ { \hat { c } _ { L } , \hat { c } _ { H } } < 0 .$ the Hessian matrix is negative definite and the critical point is a local maxima. Since the critical point is outside the feasible region, the maxima lies along the boundary: $( \mathrm { i } ) \ c _ { H } ^ { * } = 0 ,$ (ii) $c _ { L } ^ { * } = 0 , \mathrm { o r } \mathrm { ( i i i ) } c _ { H } ^ { * } = 0 , c _ { L } ^ { * } = 0 .$ 

Proof of Proposition 4. The sellers profit when targeting only the high-type bidder can be obtained from Equation (B3) by setting $c _ { L } = 0$ . The FOC is $\partial \pi _ { H } / \partial c _ { H } = \kappa ( - \kappa \bar { v _ { H } } + v _ { L } ( ( 2 -$ $\dot { v _ { H } } ) v _ { L } ) + \bar { 2 } c _ { H } \kappa ) / ( \kappa - v _ { I } ^ { 2 } ) ^ { 2 } = 0$ . Solving, we get a unique root: $\hat { c } _ { H } = ( 2 v _ { L } ^ { 2 } - v _ { H } ( \kappa + v _ { L } ^ { 2 } ) \bar { ) } / ( 2 \kappa )$ . Checking second order conditions, we find $\partial ^ { 2 } \pi _ { H } / \partial c _ { H } ^ { 2 } | _ { \hat { c } _ { H } } = - 2 \kappa ^ { 2 } / ( \kappa - v _ { L } ^ { 2 } ) ^ { 2 } < 0 ;$ hence, the root $( \hat { c } _ { H } )$ is a maxima. Now we check for conditions under which $\hat { c } _ { H }$ is positive. We find that it is positive when $v _ { H } <$ $2 v _ { { \scriptscriptstyle L } } ^ { 2 } / ( \kappa + v _ { { \scriptscriptstyle L } } ^ { 2 } )$

Substituting $c _ { H } = ( 2 ( \varepsilon _ { L } ^ { 2 } + v _ { L } ^ { 2 } ) - v _ { H } ( \varepsilon _ { L } ^ { 2 } + \kappa + v _ { L } ^ { 2 } ) ) / ( 2 \kappa )$ and $c _ { L } = 0$ in Equations (B1) and (B2), we obtain the equilibrium entry probabilities of both types of bidders when the seller issues an optimal coupon to the high-type bidder. These entry probabilities are reported in Lemma 2.

The interior region is characterized by two conditions: $0 <$ $p _ { L } < 1 , 0 < p _ { H } < 1$ . The condition $p _ { L } < 1$ implies that $v _ { H } >$ $2 - 2 \kappa / v _ { L }$ . Since $v _ { H } \leq 1$ , this implies that $p _ { L } > 0$ . Since $p _ { H } =$ $v _ { H } / 2 , 0 < p _ { H } < 1$

Hence, when $2 - 2 \kappa / v _ { L } < v _ { H } < 2 v _ { L } ^ { 2 } / ( \kappa + v _ { L } ^ { 2 } ) , \hat { c } _ { H } = c _ { H } ^ { * }$ in the interior region. Plugging the value of optimal coupon $c _ { H } ^ { * } , c _ { L } = 0$ and equilibrium entry probabilities in the profit function in Equation (B3) yields the optimal profit reported in Proposition 4: $\pi _ { H } ^ { * } = v _ { H } ^ { 2 } / 4$ 

Proof of Proposition 5. From the proof of Proposition 4, we know that $p _ { L } < 1$ if and only if $v _ { H } > 2 - 2 \kappa / v _ { L }$ . Thus, when $v _ { H } \leq 2 - 2 \kappa / v _ { L } , p _ { L } = 1$ . Substituting $p _ { L } = 1$ and $c _ { L } = 0$ in Equation (2), we get $p _ { H } = v _ { H } + c _ { H } - v _ { L }$ . Replacing this value of $p _ { H } ,$ and setting $p _ { L } = 1$ and $c _ { L } = 0$ in Equation (3), we get $\pi _ { H } = p _ { H } ( v _ { L } - c _ { H } ) = ( v _ { H } + c _ { H } - v _ { L } ) ( v _ { L } - c _ { H } )$ . Next we compute the FOC, which is $\partial \pi _ { H } / \partial c _ { H } = ( v _ { L } - c _ { H } ) - ( v _ { H } + c _ { H } - v _ { L } ) =$ $2 v _ { L } - 2 c _ { H } - v _ { H } = 0$ . Thus, we get a candidate solution, $\tilde { c } _ { H } =$ $v _ { L } - v _ { H } / 2$ . Checking the second order condition, we get $\partial ^ { 2 } \pi _ { H } / \partial c _ { H } ^ { 2 } = - 2 < 0$ . Hence, the optimal coupon value is $c _ { H } ^ { * } =$ $v _ { L } - \left( v _ { H } / 2 \right)$ . It can be seen that this coupon value is positive only when $v _ { H } < 2 v _ { L }$ . Replacing $c _ { H } ^ { * } = v _ { L } - ( v _ { H } / 2 )$ in $\pi _ { H } =$ $( v _ { H } + c _ { H } - v _ { L } ) ( v _ { L } - c _ { H } ) ,$ , we get $\pi _ { H } ^ { * } = v _ { H } ^ { 2 } / 4$ . Hence, we have part (a) of Proposition 5. Part (b) of Proposition 5 follows directly from Propositions 4 and 5(a). <sup></sup>

Proof of Proposition 6. Part (i) of Proposition 6 is easy to see from the partial derivatives of $c _ { H } ^ { * }$ as reported here:

$$
\begin{array}{l} \frac {\partial c _ {H} ^ {*}}{\partial v _ {H}} = - \frac {\kappa + v _ {L} ^ {2}}{2 \kappa} <   0, \\ \frac {\partial c _ {H} ^ {*}}{\partial v _ {L}} = \frac {(2 - v _ {H}) v _ {L}}{\kappa} > 0, \\ \frac {\partial c _ {H} ^ {*}}{\partial \kappa} = - \frac {v _ {L} ^ {2} (2 - v _ {H})}{2 \kappa^ {2}} <   0. \end{array}
$$

Part (ii) follows from $\pi _ { H } ^ { * } = v _ { H } ^ { 2 } / 4 . \quad \sqcup$

Proof of Proposition 7. The seller’s profit when targeting only the low-type bidder can be obtained from Equation (B3) by setting $c _ { H } = 0$ . The FOC is

$$
\begin{array}{r l} \frac {\partial \pi_ {L}}{\partial c _ {L}} = 2 c _ {L} \Bigg (\kappa (2 v _ {H} - 1) - \frac {\kappa (- 1 + v _ {H}) (c _ {L} ^ {3} (- 6 + 4 v _ {H}))}{(\kappa - (c _ {L} + v _ {L}) ^ {2}) ^ {3}} \\ & + 3 c _ {L} ^ {2} (- 5 + 3 v _ {H}) v _ {L} + \kappa (- 1 + 3 v _ {H}) v _ {L} \\ & + (- 3 + v _ {H}) v _ {L} ^ {3} + 3 (- 2 + v _ {H}) v _ {L} ^ {2} \Bigg) = 0. \end{array}
$$

Solving this FOC, we get three critical points, one of which is real and positive when $v _ { H } > ( \kappa + 3 v _ { L } ^ { 2 } ) / ( 3 \kappa + v _ { L } ^ { 2 } )$ and this root is

$$
\begin{array}{l} \hat {c} _ {L} = \frac {1}{6} \Bigg (\frac {6 (5 - 3 v _ {H}) v _ {L}}{- 6 + 4 v _ {H}} + [ 3 ^ {2 / 3} (1 2 \kappa - 3 v _ {L} ^ {2} + v _ {H} ^ {2} (1 6 \kappa - 3 v _ {L} ^ {2}) \\ \quad + v _ {H} (- 3 2 \kappa + 6 v _ {L} ^ {2})) ] / [ (- 3 + 2 v _ {H}) (3 6 \kappa (3 - 5 v _ {H} + 2 v _ {H} ^ {2}) v _ {L} \\ \quad - 9 (- 1 + v _ {H}) ^ {3} v _ {L} ^ {3} + 2 \sqrt {3} [ \kappa (3 - 2 v _ {H}) ^ {2} (3 (4 \kappa + 3 v _ {L} ^ {2}) ^ {2} \\ \quad - 1 2 v _ {H} ^ {3} (6 4 \kappa^ {2} - 3 6 \kappa v _ {L} ^ {2} + 9 v _ {L} ^ {4}) - 4 v _ {H} (8 0 \kappa^ {2} + 2 7 v _ {L} ^ {4}) \\ \quad + v _ {H} ^ {4} (2 5 6 \kappa^ {2} - 1 4 4 \kappa v _ {L} ^ {2} + 2 7 v _ {L} ^ {4}) \\ \quad + 6 v _ {H} ^ {2} (1 2 8 \kappa^ {2} - 6 0 \kappa v _ {L} ^ {2} + 2 7 v _ {L} ^ {4})) ] ^ {1 / 2}) ^ {1 / 3} ] \\ \quad - \frac {1}{- 3 + 2 v _ {H}} 3 ^ {1 / 3} (3 6 \kappa (3 - 5 v _ {H} + 2 v _ {H} ^ {2}) v _ {L} \\ \quad - 9 (- 1 + v _ {H}) ^ {3} v _ {L} ^ {3} + 2 \sqrt {3} [ \kappa (3 - 2 v _ {H}) ^ {2} (3 (4 \kappa + 3 v_{L}^{2}) ^{2} \\ \quad - 1 2 v _ {H} ^ {3} (6 4 \kappa^ {2} - 3 6 \kappa v _ {L} ^ {2} + 9 v _ {L} ^ {4}) - 4 v _ {H} (8 0 \kappa^ {2} + 2 7 v _ {L} ^ {4}) \\ \quad + v _ { H } ^ {4} (2 5 6 \kappa^ {2} - 1 4 4 \kappa v _ { L } ^ {2} + 2 7 v _ { L } ^ {4}) \\ \quad + 6 v _ { H } ^ {2} (1 2 8 \kappa^ {2} - 6 0 \kappa v _ { L } ^ {2} + 2 7 v _ { L } ^ {4})) ] ^ {1 / 2}) ^ {1 / 3} \Bigg). \end{array}
$$

We have numerically verified the second order condition at the critical point and it is always negative.

The equilibrium entry probabilities reported in Proposition $7$ can be obtained by substituting $c _ { H } = 0$ and $c _ { L } = c _ { L } ^ { * }$ in Equations (B1) and (B2).

The interior region is characterized by the conditions $0 <$ $p _ { L } < 1$ and $0 < p _ { H } < 1$ . The condition $p _ { L } < 1$ implies that $v _ { H } >$ $1 + v _ { L } + c _ { L } ^ { * } - \kappa \dot { / } ( v _ { L } + c _ { L } ^ { * } )$ . For $p _ { L } > 0 .$ , we need $\bar { \kappa } - ( c _ { L } ^ { * } + v _ { L } ) ^ { 2 } >$ 0 and $v _ { H } > 1 + v _ { L } + c _ { I } ^ { * } - \kappa / ( v _ { L } + c _ { I } ^ { * } )$ . We can rewrite $v _ { H } >$ $1 + v _ { L } + c _ { I . } ^ { * } - \kappa / ( v _ { L } + c _ { I . } ^ { * } )$ as $\kappa - ( { v _ { L } } + { c _ { \scriptscriptstyle I } ^ { * } } ) ^ { 2 } > ( 1 - { v _ { H } } ) ( { v _ { L } } + { c _ { \scriptscriptstyle I } ^ { * } } )$ The right-hand side $( 1 - v _ { H } ) ( v _ { L } + c _ { L } ^ { * } )$ is clearly positive, and therefore $\kappa - ( c _ { _ L } ^ { \ast } + v _ { L } ) ^ { 2 } > 0$ . Hence, we have shown that $p _ { L } > 0$ when $v _ { H } > 1 + \bar { v } _ { L } + c _ { \sc } ^ { * } - \kappa / ( v _ { L } + c _ { \sc } ^ { * } )$

$v _ { H } > 1 + v _ { L } + c _ { L } ^ { * } - \kappa / ( v _ { L } + c _ { L } ^ { * } )$ also ensures that $0 < p _ { H } < 1$ Note that $p _ { H } = \tilde { 1 } - \kappa ( 1 - v _ { H } ) \tilde { / } ( \kappa - ( c _ { I } ^ { * } + v _ { L } ) ^ { 2 } ) .$ , which can be rewritten as $( \kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } ) / ( \kappa - ( \bar { c _ { L } } + v _ { L } ) ^ { 2 } )$ . First note that the denominator is always positive, as shown in the previous paragraph. We need to show that $0 < ( \kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } ) / ( \kappa -$ $( c _ { L } + v _ { L } ) ^ { 2 } ) < 1$ . We begin with $0 < ( \kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } ) / ( \kappa -$ $( c _ { L } + v _ { L } ) ^ { 2 } )$ , which can be written as $\kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } > 0 .$ Note that $v _ { H } > 1 + v _ { L } + c _ { { \scriptscriptstyle I } } ^ { * } - \kappa / ( v _ { L } + c _ { { \scriptscriptstyle I } } ^ { * } )$ can be written as $\kappa > ( c _ { L } + v _ { L } ) ( 1 + c _ { L } - v _ { H } + v _ { L } )$ . So if $\kappa \overset { \sim } { \boldsymbol { v } _ { H } } - ( c _ { L } + v _ { L } ) ^ { 2 } > 0$ for $\kappa = ( c _ { L } + v _ { L } ) ( 1 + c _ { L } - v _ { H } + v _ { L } )$ , then $\kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 }$ > 0 must be true for all feasible κ. We replace $\kappa = ( c _ { L } + v _ { L } ) ( 1 + c _ { L } - v _ { H } + v _ { L } )$ in $\kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } > 0$ and we get $v _ { H } ( c _ { L } + v _ { L } ) ( 1 + c _ { L } - v _ { H } + v _ { L } ) -$ $( c _ { L } + v _ { L } ) ^ { 2 } > 0$ . Simplifying, we get $( 1 - v _ { H } ) v _ { H } ( c _ { L } + v _ { L } ) ( v _ { H } -$ $\left( c _ { L } + v _ { L } \right) ) > 0$ . We can see that this is always true since each of the three terms is positive. (Recall that $v _ { H } > \left( c _ { L } + v _ { L } \right) .$ , which we show below.)

Now we show that $( \kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } ) / ( \kappa - ( c _ { L } + v _ { L } ) ^ { 2 } ) < 1$ Rewrite this as $\kappa v _ { H } - ( c _ { L } + v _ { L } ) ^ { 2 } < \kappa - ( c _ { L } + v _ { L } ) ^ { 2 } \Leftrightarrow \kappa v _ { H } < \kappa \Leftrightarrow$ $v _ { H } < 1$

In Lemma $^ { 1 \mathrm { a } , }$ we have shown that it is never optimal for the seller to give a coupon to the low-type bidder such that he wins the auction when both bidders enter. Combining with Proposition 3, we get $c _ { L } ^ { \ast } < v _ { H } - v _ { L } . \quad \sqcup$

Proof of Proposition 8. (i) This boundary solution is obtained by assuming that $p _ { L } = 1$ . We reformulate the firm’s objective function and solve the FOC.

Replacing $p _ { L } = 1$ in Equation (2), we get $p _ { H } = v _ { H } - v _ { L } - c _ { L }$ Substituting $p _ { L } = 1 , p _ { H } = v _ { H } - v _ { L } - c _ { L }$ in the firm’s objective function in Equation (5), we get $\pi _ { L B 1 } = c _ { L } ( 2 v _ { H } - 3 v _ { L } - 1 ) +$ $( v _ { H } - v _ { L } ) v _ { L } - \bar { 2 } c _ { L } ^ { 2 }$ . The FOC is $\partial \pi _ { L B 1 } / \partial c _ { L } = - 1 - 4 c _ { L } + 2 v _ { H } -$ $3 v _ { I } = 0$ . Solving for $c _ { L }$ we get $c _ { L B 1 } ^ { * } = { \textstyle { \frac { 1 } { 4 } } } ( 2 v _ { H } - 3 v _ { L } - 1 )$ <sup>)</sup>. It is easy to see that the second order condition is satisfied. Substituting $c _ { L } = c _ { L B 1 } ^ { * } \mathrm { i n } \pi _ { L B 1 } = c _ { L } ( 2 v _ { H } - 3 v _ { L } - 1 ) + ( v _ { H } - v _ { L } ) v _ { L } - 2 c _ { L } ^ { 2 }$ , we get the optimal profit. $\frac { 1 } { 2 } \big ( 1 + 3 v _ { L } \big ) < v _ { H }$ ensures that $c _ { I . B 1 } ^ { * } > 0$

Note that this solution was obtained assuming the lowtype bidder always enters $( p _ { L } = 1 )$ . In Proposition $^ { 7 , }$ we have shown that when $v _ { H } > 1 + v _ { L } + c _ { L } ^ { * } - \kappa / ( v _ { L } + c _ { L } ^ { * } ) , 0 < p _ { L } < 1$ In this boundary, the firm issues a coupon $c _ { L } = c _ { L B 1 } ^ { * } , \mathbf { s o } \ v _ { H } \leq$ $1 + v _ { L } + c _ { L B 1 } ^ { * } - \kappa / ( v _ { L } + c _ { L B 1 } ^ { * } )$ ensures that our assumption of the low-type bidder always entering is satisfied. It is interesting to note that this condition is not always satisfied. Sometimes the entry probability of the low-type bidder in the interior is $p _ { L } ^ { * } > 1$ and at the same time the entry probability in boundary (i) is $p _ { L B 1 } ^ { * } < 1$ . In this zone, we must identify a coupon value that makes $p _ { L } = 1$ . We do this in part (ii).

(ii) From Proposition $^ { 7 , }$ , we have $p _ { L } = ( 1 - v _ { H } ) ( c _ { I } ^ { \ast } + v _ { L } ) / ( \kappa -$ $( c _ { I . } ^ { * } + v _ { L } ) ^ { 2 } )$ in the interior. When the condition $p _ { L } < 1$ is violated, we solve for that coupon value $c _ { L }$ such that $p _ { L } =$ $( 1 - v _ { H } ) ( c _ { L } + v _ { L } ) / ( \kappa - ( c _ { L } + \overset { \textstyle - } { v _ { L } } ) ^ { 2 } ) = 1$ . This yields two roots, one of which is always negative. Thus, the positive root is $c _ { _ { I . B 2 } } ^ { \ast } = \scriptstyle { \frac { 1 } { 2 } } ( v _ { { H } } - 1 + \sqrt { 1 + 4 \kappa + ( v _ { { H } } - 2 ) v _ { { H } } } - 2 v _ { { L } } )$

$v _ { H } > 1 - \kappa / v _ { L } + v _ { L }$ ensures that $c _ { L B 2 } ^ { * } > 0 ; v _ { H } \leq 1 + c _ { L } ^ { * } + v _ { L } -$ $\kappa / ( c _ { L } ^ { * } + v _ { L } )$ ensures that we are not in the interior region; and $v _ { H } > 1 + c _ { L B 1 } ^ { * } + v _ { L } - \kappa / ( c _ { L B 1 } ^ { * } + v _ { L } )$ ensures that we are not in boundary part (i).

Note that $1 + c _ { L B 1 } ^ { * } + v _ { L } - \kappa / ( c _ { L B 1 } ^ { * } + v _ { L } ) > 1 - \kappa / v _ { L } + v _ { l }$ because $c _ { L B 1 } ^ { * } \geq 0$ . Hence, $v _ { H } > 1 + c _ { L B 1 } ^ { * } + v _ { L } - \kappa / ( c _ { L B 1 } ^ { * } + v _ { L } )$ implies $v _ { H } >$ $1 - \kappa / v _ { L } + v _ { L }$

Substituting $c _ { L } = c _ { L B 2 } ^ { * } \sin \pi _ { L B 2 } = c _ { L } ( 2 v _ { H } - 3 v _ { L } - 1 ) + ( v _ { H } - v _ { L } )$ $v _ { L } - 2 c _ { I . } ^ { 2 }$ , we get the optimal profit.

Hence, we have Proposition 8. <sup></sup>

Proof of Proposition 9. The conditions reported in parts (i) and (ii) follow from Propositions 4 and 5 and Propositions 7 and 8, respectively. We now prove part (iii) of Proposition 9:

First we show that the interior region for targeting the high-type bidder given in (i)(a) does not overlap with the interior region for targeting the low-type bidder given in region (ii)(a). Note that $v _ { H } ^ { - } < 2 v _ { I } ^ { 2 } / ( \kappa + \stackrel { \textstyle \cdot } { v _ { I } ^ { 2 } } )$ can be rewritten as $\kappa < ( 2 - v _ { H } ) v _ { I . } ^ { 2 } / v _ { H }$ . The condition $v _ { H } > ( \kappa + 3 v _ { { t } } ^ { 2 } ) /$ $\left( 3 \kappa + v _ { I } ^ { 2 } \right)$ can be rewritten as $\kappa > ( 3 - v _ { H } ) v _ { I } ^ { 2 } / ( 3 v _ { H } - 1 )$ . Comparing the conditions on κ: $\kappa > ( 3 - v _ { H } ) v _ { I } ^ { 2 } / ( 3 v _ { H } - 1 )$ and $\kappa <$ $( 2 - v _ { H } ) v _ { I } ^ { 2 } / v _ { H } .$ , we have $( 3 - v _ { H } ) v _ { I . } ^ { 2 } / ( 3 v _ { H } - \tilde { 1 } ) - ( 2 - v _ { H } ) v _ { I . } ^ { 2 } / v _ { H } =$ $( 2 ( 1 - v _ { H } \bar { ) } ^ { 2 } v _ { L } ^ { 2 } ) / ( v _ { H } ( 3 v _ { H } - 1 ) )$ , which is positive for $v _ { H } > 1 / 3 .$ Note the condition $v _ { H } > ( \kappa + 3 v _ { I } ^ { 2 } ) / ( 3 \kappa + \overline { { v _ { I } ^ { 2 } } } )$ implies that $v _ { H } >$ $1 / 3$ . Therefore, $v _ { H } < 2 v _ { I } ^ { 2 } / ( \kappa + v _ { I } ^ { 2 } )$ and $v _ { H } > \bar { ( \kappa + 3 v _ { L } ^ { 2 } ) } / ( 3 \kappa + v _ { L } ^ { 2 } )$ and $v _ { H } > ( \kappa + 3 v _ { L } ^ { 2 } ) / ( 3 \bar { \kappa } + v _ { L } ^ { 2 } )$ cannot all be satisfied for any parameter values. This implies that the interior regions do not overlap.

Now we show that the boundary region for targeting the high type given in (i)(b) does not overlap with the interior region for targeting the low-type bidder given in (ii)(a). This is easy to see since we have already shown that that there is no overlap in the following two conditions: $v _ { H } < 2 v _ { L } ^ { 2 } / ( \kappa + v _ { L } ^ { 2 } )$ and $v _ { H } > ^ { ^ { . } } ( \kappa + 3 v _ { { I } } ^ { 2 } ) / ( 3 \kappa + v _ { { I } } ^ { 2 } )$ . Note that region (i)(b) is a subset of $v _ { H } < 2 v _ { L } ^ { 2 } / ( \kappa \stackrel { - } { + } v _ { L } ^ { 2 } )$ . Hence, region (i)(b) does not overlap with region (ii)(a).

Next we show that there is no overlap in the region for targeting the high-type bidder given in (i)(a) and (i)(b) with the boundary region for targeting the low-type bidder given in region (ii)(b). We will show that the highest value of $v _ { H }$ in regions (i)(a) and (i)(b) is smaller than the lowest value that $v _ { H }$ can take in region (ii)(b). Proposition 4 defines the interior region for targeting the high-type bidder. The condition stated in the proposition is $2 - 2 \kappa \bar { / } \bar { v _ { L } } < v _ { H } < 2 v _ { _ { I } } ^ { 2 } / ( \kappa + v _ { _ { I } } ^ { 2 } )$ Note that the lower bound $( 2 - 2 \kappa / v _ { L } )$ and the upper bound $( 2 v _ { L } ^ { 2 } / ( \kappa + v _ { L } ^ { 2 } ) )$ are increasing functions of $v _ { L }$ . It can be seen that when $\stackrel {  } { \kappa } = v _ { L } - v _ { I } ^ { 2 } , ( 2 - 2 \stackrel {  } { \kappa } / v _ { L } ) = ( 2 v _ { I } ^ { 2 } / ( \kappa + \stackrel {  } { v } _ { I } ^ { 2 } ) ) = 2 v _ { L }$ . Since these bounds specify the range of $v _ { H }$ and they reach their maximum value at $2 v _ { L }$ , the limiting value (maximum possible) for $v _ { H }$ is $2 v _ { L }$ . Hence, $2 - 2 \kappa \breve { / } v _ { L } < v _ { H } < 2 v _ { { \scriptscriptstyle I } } ^ { 2 } / ( \kappa \stackrel { \cdot } { + } v _ { { \scriptscriptstyle I } } ^ { 2 } )$ implies that $v _ { H } < 2 v _ { L }$ . To target the high-type bidder (interior or boundary), the following condition must hold: $v _ { H } < 2 v _ { L }$

To target the low-type bidder in region (ii)(b), the following condition must hold: $\overline { { \frac { 1 } { 2 } ( 1 + 3 v _ { L } ) } } < v _ { H }$ . This implies $2 v _ { L } < v _ { H }$ Hence, the region for targeting the low-type bidder given in (ii)(b) does not overlap with the region for targeting the high-type bidder given in (i)(a) and (i)(b).

Finally, we show that there is no overlap in the region for targeting the high-type bidder given in (i)(a) and (i)(b) with the boundary region for targeting the low-type bidder given in region (ii)(c). We will show that the highest value of $v _ { H }$ in regions (i)(a) and (i)(b) is smaller than the lowest value that $v _ { H }$ can take in region (ii)(c). As discussed previously, the highest value of $v _ { H }$ in regions (i)(a) and (i)(b) is $2 v _ { L }$

Please note that the boundary region B1 (shown in Figure 8) is defined in part by the following conditions stated in Proposition 9 (ii)(c):

$v _ { H } > 1 - \kappa / v _ { L } + v _ { L }$ and $v _ { H } \le 1 + c _ { L } ^ { * } + v _ { L } - \kappa / ( c _ { L } ^ { * } + v _ { L } )$ . It can be seen that these conditions will intersect when $c _ { { I } . } ^ { * } = 0$ . This intersection point yields the lowest value of $v _ { H }$ for which these two conditions are satisfied. Furthermore, the following condition from Proposition 9(ii)(a) also yields $c _ { I . } ^ { * } = 0 ; v _ { H } >$ $( \kappa + 3 v _ { L } ^ { 2 } ) / ( 3 \kappa + v _ { L } ^ { 2 } )$ . This is true because the condition was obtained to ensure $c _ { L } ^ { * } > 0$ . Hence, the following three curves must intersect at the same point: $v _ { H } > 1 - \kappa / v _ { L } + v _ { L } ,$ and $v _ { H } \leq$ $1 + c _ { L } ^ { * } + v _ { L } - \kappa / ( c _ { L } ^ { * } + v _ { L } )$ and $\overline { { v } } _ { H } > ( \kappa + 3 v _ { L } ^ { 2 } ) / ( 3 \kappa + v _ { L } ^ { 2 } ) .$ . To find the intersection point, we set $1 - \kappa / v _ { L } + \stackrel { \sim } { v _ { L } } = ( \kappa + \stackrel { \sim } { 3 } v _ { I } ^ { 2 } ) / ( 3 \kappa + v _ { I } ^ { 2 } )$ and solve for κ. This yields $\kappa = { \textstyle \frac { 1 } { 3 } } ( 2 v _ { L } - v _ { L } ^ { 2 } )$ . Replacing this value of κ in $v _ { H } > 1 - \kappa / v _ { L } + v _ { L } ,$ we obtain the lowest value of $\begin{array} { r } { v _ { H } = \frac { 1 } { 3 } ( 1 + 4 v _ { L } ) } \end{array}$ .

It can be seen that $\frac { 1 } { 3 } ( 1 + 4 v _ { L } ) > 2 v _ { L }$ for $0 \le v _ { L } < 0 . 5$ . When $v _ { L } > 0 . 5 ,$ then, both conditions yield $v _ { H } = 1$ , and the regions touch each other. The region given in (ii)(c) is also bounded by the condition $v _ { H } > 1 - \kappa / v _ { L } + v _ { L } ,$ , which has a negative slope with κ. Hence, we have shown that there is no overlap in the regions for targeting the high-type bidder given in (i)(a) and (i)(b) with the boundary region for targeting the low-type bidder given in region (ii)(c). <sup></sup>

## Endnotes

<sup>1</sup> https://apps.ebay.com/selling?appId=mystorerewards.newage.msr .com (accessed June 12, 2017).

<sup>2</sup> For the role of coupons as a price discrimination mechanism in a distribution channel, see Gerstner et al. (1994).

<sup>3</sup> We refer to the seller as “she” and the bidder as “he” throughout this paper.

<sup>4</sup> The case where the coupon to the low-valuation bidder is so large that he wins even when the high-valuation bidder enters the auction is examined in Lemma 1a in Appendix B. We show in Lemma 1a that it is never optimal for the seller to issue such a large coupon to the low-valuation bidder that he wins even when the high-valuation bidder enters the auction.

## References

Ariely D, Simonson I (2003) Buying, bidding, plying, or competing? Value assessment and decision dynamics in online auctions. J. Consumer Psych. 13(1–2):38–53.

Bajari P, Hortacsu A (2003) The winner’s curse, reserve prices, and endogenous entry: Empirical insights from eBay auctions. RAND J. Econom. 34:329–355.

Bapna R, Goes P, Gupta A (2003) Analysis and design of business-toconsumer online auctions. Management Sci. 49(1):85–101.

Bapna R, Goes P, Gupta A, Karuga G (2008) Predicting bidders’ willingness to pay in online multiunit ascending auctions: Analytical and empirical insights. INFORMS J. Comput. 20(3):345–355.

Bapna R, Goes P, Gupta A, Yiwei J (2004) User heterogeneity and its impact on electronic auction market design: An empirical exploration. MIS Quart. 28(1):21–43.

Bapna R, Seokjoo AC, Goes P, Gupta A (2009) Overlapping online auctions: Empirical characterization of bidder strategies and auction prices. MIS Quart. 10(4):763–783.

Bester H, Petrakis E (1996) Coupons and oligopolistic price discrimination. Internat. J. Indust. Organ. 14:227–242.

Budish EB, Takeyama LN (2001) Buy prices in online auctions: Irrationality on the Internet? Econom. Lett. 72(3):325–333.

Cao X, Tian G (2010) Equilibria in first price auctions with participation costs. Games Econom. Behav. 69(2):258–273.

Chakraborty I, Kosmopoulou G (2004) Auctions with shill bidding. Econom. Theory 24(2):271–287.

Chen Y, Iyer G (2002) Consumer addressability and customized pricing. Marketing Sci. 21(2):197–208.

Choudhary V, Ghose A, Mukhopadhyay T, Rajan U (2005) Personalized pricing and quality diferentiation. Management Sci. 51(7):1120–1130.

Etzion H, Pinker E, Seidmann A (2006) Analyzing the simultaneous use of auctions and posted prices for online selling. Manufacturing Service Oper. Management 8(1):68–91.

Fong Y, Liu Q (2008) Using coupons to intertemporally price discriminate and tacitly collude. Working paper, Northwestern University, Evanston, IL.

Fudenberg D, Tirole J (2000) Customer poaching and brand switching. RAND J. Econom. 31:634–657.

Gale IL, Hausch DB (1994) Bottom-fishing and declining prices in sequential auctions. Games Econom. Behav. 7(3):318–331.

Gallien J, Gupta S (2007) Temporary and permanent buyout prices in online auctions. Management Sci. 53(5):814–833.

Geldman A (2007) Statistics you won’t find on eBay. WebRetailer, http://www.webretailer.com/articles/ebay-statistics.asp#how manybids.

Gerstner E, Hess JD, Holthausen DM (1994) Price discrimination through a distribution channel: Theory and evidence. Amer. Econom. Rev. 84(5):1437–1445.

Goes PB, Karuga GG, Tripathi A (2010) Understanding willingnessto-pay formation of repeat bidders in sequential online auctions. Inform. Systems Res. 21(4):907–924.

Hou J, Rego C (2007) A classification of online bidders in a private value auction: Evidence from eBay. Internat. J. Electronic Marketing Retailing 1(4):322–338.

Kannan KN (2010) Declining prices in sequential auctions with complete revelation of bids. Econom. Lett. 108:49–51.

Kannan KN (2012) Efects of information revelation policies under cost uncertainty. Inform. Systems Res. 23(1):75–92.

Klemperer P (1999) Auction theory: A guide to the literature. J. Econom. Surveys 13(3):227–286.

Kuruzovich J, Viswanathan S, Agarwal R (2010) Seller search and market outcomes in online auctions. Inform. Systems Res. 56(10):1702–1717.

Levedahl W (1984) Marketing, price discrimination, and welfare: Comment. Southern Econom. J. 50:886–891.

Levin D, Smith JL (1994) Equilibrium in auctions with entry. Amer. Econom. Rev. 84(3):585–599.

Liu D, Chen J (2006) Designing online auctions with performance information. Decision Support Systems 42(3):1307–1320.

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1):133–153.

Maskin ES, Riley JG (1985) Auction theory with private values. Amer. Econom. Rev. 75(2):150–155.

McAfee RP, McMillan J (1987) Auctions and bidding. J. Econom. Literature 25(2):699–738.

Milgrom P, Weber RJ (1982) The value of information in a sealed-bid auction. J. Math. Econom. 10(1):105–114.

Myerson RB (1981) Optimal auction design. Math. Oper. Res. 6:58–73.

Narasimhan C (1982) Coupons as price discrimination devices— A theoretical perspective and empirical analysis. Unpublished doctoral dissertation, Graduate School of Management, University of Rochester, Rochester, NY.

Narasimhan C (1984) A price discrimination theory of coupons. Marketing Sci. 3(2):128–147.

Ockenfels A, Roth AE (2006) Late and multiple bidding in second price Internet auctions: Theory and evidence concerning different rules for ending an auction. Games Econom. Behav. 55(2): 297–320.

Overby E, Jap S (2009) Electronic and physical market channels: A multiyear investigation in a market for products of uncertain quality. Management Sci. 55(6):940–957.

Roth AE, Ockenfels A (2002) Last minute bidding and the rules for ending second-price auctions: Evidence from eBay and Amazon auctions on the Internet. Amer. Econom. Rev. 92(4):1093–1103.

Shafer G, Zhang ZJ (1995) Competitive coupon targeting. Marketing Sci. 14(4):395–415.

Shafer G, Zhang ZJ (2002) Competitive one-to-one promotions. Management Sci. 48(9):1143–1160.

Shapiro C, Varian H (1999) Information Rules (Harvard Business School Press, Boston).

Sweeney G (1984) Marketing, price discrimination, and welfare: Comment. Southern Econom. J. 50:892–899.

Van Heck E, Vervest P (1998) How should CIOs deal with web-based auctions? Comm. ACM 41(7):99–100.

Varian H (1989) Price discrimination. Schmalensee R, Willig RD, eds. Handbook of Industrial Organization (North-Holland, Amsterdam), 597–654.

Vickrey W (1961) Counter speculation, auctions, and competitive sealed tenders. J. Finance 16:8–37.

Wang X, Montgomery A, Srinivasan K (2008) When auction meets fixed price: A theoretical and empirical examination of buy-itnow auctions. Quant. Marketing Econom. 6(4):339–370.

Zeithammer R (2006) Forward-looking bidding in online auctions. J. Marketing Res. 43(3):462–476.
