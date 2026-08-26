---
otero_id: 6092
otero_key: "SBEXFDXV"
title: "Online reputation systems: Design and strategic practices"
authors: "Ming Zhou; Martin Dresner; Robert J. Windle"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Online reputation systems: Design and strategic practices

Ming Zhou <sup>a,⁎</sup>, Martin Dresner <sup>b</sup>, Robert J. Windle <sup>c</sup>

<sup>a</sup> Supply Chain and Operations Management, Department of Organization and Management, Lucas Graduate School of Business, San Jose State University, BT 659, One Washington Square, San Jose, CA, 95192 - 0070, United States

<sup>b</sup> Robert H. Smith School of Business Logistics, Business and Public Policy, 3433 Van Munching Hall, College Park, MD 20742-1815, 301.405.2204, United States

<sup>c</sup> Robert H. Smith School of Business Logistics, Business and Public Policy, 3409 Van Munching Hall, College Park, MD 20742-1815, 301.405.2187, United States

Received 14 December 2005; received in revised form 25 September 2007; accepted 3 October 2007 Available online 25 October 2007

## Abstract

This paper provides a comprehensive framework for evaluating the effects of feedback systems, and the potential problems with feedback systems, on seller incentives to provide high quality products under the case of asymmetric information. In particular, a baseline auction system without a feedback-based reputation system is first modeled and it is shown that the market for the sale of high quality products may not be sustainable. We then show how the institution of a feedback system can lead to sustainable market outcomes. Next, we demonstrate how three practices – the changing of identifications by dishonest sellers, shilling, and failure to leave feedback – can negate the usefulness of the feedback system in maintaining the market. Finally, we describe some actions that may be taken to overcome these problems. These results highlight the important role market managers play in ameliorating these market failure problems and ensuring the effective functioning of a market. © 2007 Elsevier B.V. All rights reserved.

Keywords: e-Commerce; Trust; Incentive Structure; B2B; B2C

## 1. Introduction

The internet auction business, led by its dominant firm, eBay.com, has been one of the most successful dotcom sectors. eBay's sales in 2004 were \$3.27 billion, a 51% increase over the previous year. The company had 135 million registered users and did business in countries around the world (www.hoovers.com 2005).

Yet despite the evident success of eBay.com, or more likely due to the firm's success, the company has been a prime target for online fraud. The Internet Crime and Convention Center, a partnership between the National White Collar Crime Center and the FBI, found that in 2004, 71.2% of all Internet-related complaints – 207,000 in total – pertained to online auctions [33]. According to the Federal Trade Commission [15], most Internet auction fraud reports concern the following practices:

• Failure to send merchandise

• Sending something of lesser value than advertised

• Failure to deliver in a timely manner • Failure to deliver all relevant information about a product or terms of sale.

In addition, the FTC states that buyers may experience problems with respect to fraudulent bidding practices. “Shill bidding”, for example, results when either fraudulent sellers or their associates bid up the price of products in order to obtain a higher price from an honest bidder.

In order to combat problems with dishonest or fraudulent market participants, eBay.com (as well as other auction sites) has established a reputation system based on feedback from market participants. Both buyers and sellers are able to leave positive, negative, or neutral feedback following a transaction. The accumulated feedback then forms the basis of a seller's or a buyer's online reputation. There has been a considerable amount of research conducted on reputation systems and the effects of these systems on the operations of online markets. Topics covered include the effects of feedback on bidding behaviors [17,29,34], improvements in the design of feedback systems [8,11,14], system effectiveness and robustness [27,10,12 etc.], and buyer perceptions of feedback systems [9,28]. Research has also contrasted feedback systems with other mechanisms for inducing honest behavior [4,2]. In this paper, we address four concerns: how the institution of a feedback system can reduce fraud by altering seller incentives and how each of three practices – the failure to leave feedback, collusive feedback (shilling), and ID changing – reduce the effectiveness of a feedback system.

The major objective of this paper is to provide a comprehensive framework for evaluating the effects of feedback systems, and the potential problems with feedback systems, on seller incentives to provide high quality products under the case of asymmetric information (i.e., buyers are not able to discern product quality prior to making their purchase decisions while sellers are aware of the quality of their product offerings). In particular, we first model a baseline auction system without a feedback-based reputation system and show that the market for the sale of high quality products may not be sustainable. Following the well-known findings from [1], dishonest or low-quality sellers will drive honest or high-quality sellers out of the market due to asymmetric information between buyers and sellers, leading to the eventual collapse of the market for high-quality products. We then show how the institution of a feedback system can lead to sustainable market outcomes. Positive feedback allows honest sellers to earn economic rents after first establishing their reputations. Negative feedback helps to distinguish between honest and dishonest sellers. Next, we demonstrate how three practices – the changing of identifications by dishonest sellers, shilling, and failure to leave feedback – can negate the usefulness of the feedback system in maintaining the market. Finally, we describe some actions that may be taken to overcome these problems.

The main contributions of our paper are as follows: First, we explicitly and analytically examine how buyer feedback influences a seller's decision with respect to product quality. We show that a feedback system allows a market for high quality products to be sustained and therefore allows a seller to choose to sell high quality products and still earn non-negative economic profits. Next, we demonstrate how both positive and negative feedback can influence the costs faced by an honest seller — both the setup costs (i.e., initial losses an honest seller will incur until its reputation is established) and opportunity costs (i.e., profits forgone by not choosing the dishonest option). Simplifying the current system with only the positive or negative feedback can reduce the effectiveness. Third, we show analytically how three problems with feedback systems changes seller incentives, potentially negating the positive impacts of a feedback system on establishing a market for high quality products. These results highlight the important role market managers play in ameliorating these market failure problems and ensuring the effective functioning of a market.

The rest of the paper is organized as follows. In the next section, we provide a brief review of the literature on feedback systems. In Section 3, we formulate our model, show how a feedback system can help maintain a market for high quality sellers, and discuss how the three practices described above can reduce the effectiveness of the feedback system. Section 4 provides a brief discussion of some of the potential ways to overcome the problems with feedback systems. Finally, in Section 5, we draw conclusions and implications from our research, and discuss the potential for future research.

## 2. Literature review

An effective signaling system should lead to the ability of users to distinguish quality attributes among potential transaction partners. If there are sellers of both high quality and low quality products (as was the case with [1] in the used car market), then with an effective signaling mechanism, price differentials should exist between the high and low quality products. A feedback system is effective if it is capable of helping buyers to differentiate between products of different quality, thus producing price differentials [10].

Most of the research on online feedback systems has focused on the functioning of major online business-toconsumer (B2C) auction sites, especially eBay.com. As the pioneer in online B2C auctions, eBay has established a set of policies that have been followed by other online auction sites. Therefore, results found for eBay should be largely generalizable to other auction sites.

A number of empirical studies of online feedback systems (most using eBay data) have been designed to determine if better (i.e., more positive and/or less negative) feedback leads to higher prices [17,3,22,23,27,20,7,12]. Although much of this research has found feedback systems to be effective, the importance of feedback and the significance of the feedback systems in influencing prices have varied widely across studies. An important reason why feedback systems may not be effective is that they may not be perceived as credible. A number analytical studies have been conducted to determine how the design of the feedback systems might be improved and their credibility enhanced [8,9,6,14]. For instance, [14] shows that a feedback system where reputation is calculated using an exponential smoothing method (rather than, for example, by simply adding up positive feedback counts) can help to enhance seller incentives to be honest or to provide high quality products. Based on [30]'s study of reputation, [18] considers the strategic decision-making of sellers and the impact of feedback systems on seller choices. [18] states that there should be a stream of returns to honest sellers that arise as a result of feedback systems. Using a dynamic programming approach, [14] suggests that the returns to an honest seller need to outweigh the potential lost profits a seller may garner by being dishonest.

Building on the analytical results obtained in prior research, this paper explicitly examines how three behaviors – shilling, the changing of IDs, and the failure to leave feedback – affect the credibility of feedback systems, thus reducing the ability of sellers to charge higher prices for better quality products. Our model explicitly accounts for the opportunity costs sellers of high quality products face; i.e., the lost profits that they may obtain by providing low quality, low cost products. Finally, we provide recommendations as to how feedback systems may be improved.

## 3. Modeling the online auction market

## 3.1. Base model

This section presents a model to describe the impact of information asymmetry on market performance. The model demonstrates that high quality products may be driven out of the market in the presence of information asymmetry.

The base model consists of a simple competitive market where there are a large number of sellers and buyers, all of which are price takers. Sellers offer one unit of product each period and buyers each consume one or zero units of the product. Sellers transact with buyers in the market to maximize their profits while buyers consume goods to maximize their utilities. We assume that the conditions for a competitive market are met. These conditions include free entry and exit from the market, a homogeneous product, and perfect information. A hypothetical good, A, is bought and sold. The assumption is that good A is a small fraction of a buyer's wealth or expenditures and that the prices of other goods are unaffected by price changes in A.

At equilibrium, a price level, $P ^ { E }$ , is defined as the price for product A at quality level Qu. The presence of perfect information means that an identical cost structure can be assumed for each firm: c(Qu,V) for each unit of A, where Qu measures the quality level of the product and V represents product-related characteristics. In the case of homogeneous products, V is identical across products, so, for parsimony, the cost function is denoted as $c ( \mathrm { Q u } )$ in this base case. The cost function is monotonically increasing in quality, Qu, where $\scriptstyle { \frac { d c } { d \mathrm { Q u } } } > 0$ . Fixed costs are assumed to be zero. As a result, every firm will earn a profit of $\mathsf { \Pi } ^ { \cdot } P ^ { E } - c ( \mathrm { Q u } )$ for each unit sold. Economic profits will be zero under a competitive equilibrium, where $\scriptstyle { \dot { P } } ^ { E } = c ( \mathrm { Q u } )$ . At this price, firms are indifferent between staying in the market and ceasing operations. Since firms are making a fair rate of return on assets employed in the business, the model assumes that firms choose to stay in a market when earning zero economic profits.

Assume now that firms can produce product A at two different quality levels, $\mathrm { Q u } ^ { \mathrm { L o w } }$ and Qu, where $\mathrm { Q u } ^ { \mathrm { L o w } } \ll \mathrm { Q u }$ This now generates two levels of cost: $c ( \mathrm { Q u } ^ { \mathrm { L o w } } )$ and $c ( \mathrm { Q u } )$ . Cost functions are defined as monotonically increasing in quality, so $c ( \mathrm { Q u } ^ { \mathrm { L o w } } ) { < } c ( \mathrm { Q u } )$ . At equilibrium, product A at quality level $\mathrm { Q u } ^ { \mathrm { L o w } }$ should be sold at $P ^ { \prime } { = } c ( \mathrm { Q u } ^ { \mathrm { L o w } } )$ and product A at quality level Qu should settle at price level $P ^ { E } { = } c ( \mathrm { Q u } )$ , both of which are equilibrium prices if buyers have full information on product quality prior to making their purchases.

The next step is to introduce asymmetric information into the model. Suppose sellers of both high and low quality products claim to offer products at the high quality level, $\mathrm { Q u } ,$ such as in the used car market studied by [1]. The only information buyers have on product quality is provided by the sellers. As a result, buyers are unable to determine prior to a purchase the true quality of the product. Online markets are more vulnerable to the problem since buyers often do not have a chance to physically inspect products before final payment is made [27]. Quality differences may result from insufficient inventory of high quality products on hand, poor quality control, improper storage methods, poor shipping practices, etc. For illustrative purposes, sellers that offer A at quality level, Qu, are labeled as “honest” sellers while sellers that offer A at quality level, $\mathrm { Q u } ^ { \mathrm { L o w } }$ , are labeled as “dishonest”, even though the reasons for delivering poor quality products may not be related to seller dishonesty. Following the framework used by [25], the following model is developed for information asymmetry.

Assume both quality levels are offered in one marketplace and that sellers do not disclose the true quality level to buyers before payment. In this circumstance, buyers will know that there is some chance that they will receive a product of high quality and some chance that they will receive a product of low quality. Assume that a buyer's initial belief is that the probability of receiving a high quality version of product A is α, and the probability of receiving a low quality product is $( 1 - \alpha )$ . These probabilities may be based on previous experience, on market information, on media reports, etc. For simplicity, assume that the vector Vof product characteristics is fixed and does not vary between the two types of sellers. In this situation, buyers are willing to pay an expected price for product A as follows:

$$
\alpha P ^ {E} + (1 - \alpha) P ^ {\prime}
$$

For low quality sellers, profits would be the following:

$$
\alpha P ^ {E} + (1 - \alpha) P ^ {\prime} - c (\mathrm{Qu} ^ {\text { Low }}) > 0\tag{1}
$$

In the short run, sellers of low quality product A do not have an incentive to accept prices lower than $\alpha { \cal P } ^ { E } + ( 1 - \alpha ) { \cal P } ^ { \prime }$ Offering the product at a lower price would signal to buyers that product being sold is of poor quality, thereby lowering profits. Sellers of high quality products may have to exit the market since economic losses would be the following:

$$
\alpha P ^ {E} + (1 - \alpha) P ^ {\prime} - c (\mathrm{Qu}) <   0\tag{2}
$$

The condition for honest sellers to remain in the market is for $\mathsf { \alpha } \mathsf { \alpha } \partial _ { \mathsf { \alpha } } = 1$ ; i.e., a market where buyers perceive the existence of only high quality sellers, an unlikely occurrence. Hence, sellers offering high quality products are driven from the market, leaving only a market for low quality products.

## 3.2. A perfect feedback system in an ideal market

In this section, a feedback system is added to the model. The feedback system serves as a signal with regard to seller credibility, thus facilitating trust between the buyer and seller. We define the effectiveness of a feedback system as its ability to induce adequate returns to maintain a market for sellers of high quality products. We further state that the effectiveness of a reputation system increases as accurate feedback is reported to potential buyers. This is consistent with the previous literature such as [10]. Although other factors may also influence the information that buyers have regarding sellers (e.g., provision of warranties, inclusion of product photographs, etc.), these factors are considered fixed in this model. The model shows that the addition of a feedback system can help to maintain or re-establish the market for high quality products.

Assume, initially, that a buyer leaves feedback after each transaction (either positive or negative) and that feedback accurately reflects the buyer's experience with the seller. Subsequent buyers are able to learn about seller honesty by reading feedback profiles. With the introduction of feedback, the price that a buyer is willing to pay is influenced by two beliefs: an overall belief in the marketplace and a belief in a particular seller. We can rewrite $\alpha { \cal P } ^ { \bar { E } } { + } ( 1 - \alpha ) { \cal P } ^ { \prime } \mathrm { a s } ( 1 - \not d ) { \cal P } ^ { { \cal E } }$ where d is between 0 and 1. Since $\alpha P ^ { E } + ( 1 - \alpha ) P ^ { \prime }$ is less than $P ^ { E } { = } c ( \mathrm { Q u } )$ , d is the discount from the equilibrium high quality price. If a seller attempts to enter the high quality market, d represents its potential loss on a transaction.

We denote the amount of feedback received by a particular firm by n. Other factors that may influence seller credibility are denoted by X. The impact of all trust-enhancing factors on a seller is denoted by $f ( n _ { p } , X _ { p } )$ , where $n _ { p }$ stands for the positive feedback count and $X _ { p }$ is a vector of factors, other than positive feedback, that may help enforce the trust of a seller. The influence from any negative factors on seller credibility is denoted by $g ( n _ { n } , X _ { n } )$ , where $n _ { n }$ stands for the seller's negative feedback count and $X _ { n }$ is the vector of factors that reduce seller credibility. The positive feedback function $f ( . )$ is assumed to be concave, where $\partial f ( . ) / \partial n _ { p } { > } 0$ and $\hat { o } ^ { 2 } f ( . ) / \hat { o } n _ { p } \hat { o } n _ { p } { < } 0$ . No assumption is imposed on the negative feedback function. Both functions converge asymptotically as follows: $f ( . ) { \longrightarrow } \theta _ { f }$ when $n _ { p } \longrightarrow \infty ,$ $g ( . ) \longrightarrow \theta _ { g }$ when $n _ { n } \longrightarrow \infty . f ( . ) = 0$ if and only if $n _ { p } = 0$ and X is empty. $g ( . ) { = } 0$ if and only if $n _ { n } { = } 0$ and X is empty. In this model the impact from positive feedback offsets the impact from negative feedback (i.e., both types of feedback are weighed equally). The overall reputation effect for a seller is the net impact of the positive and negative feedback.

We first restrict buyer and seller activity to two time periods. (In Appendix A, the model is expanded to infinite periods.) The discount factor, $r ,$ is used to compute the present value of monetary flows. The payoffs for an honest seller in a two period model are listed below. For simplicity the model assumes that X is constant and that all revenues and costs are realized at the beginning of a period.

<table><tr><td colspan="3">An honest seller:</td></tr><tr><td></td><td>Revenue</td><td>Cost</td></tr><tr><td>Period 1:</td><td> $P=(1-d)P^{E}$ </td><td>c(Qu)</td></tr><tr><td>Period 2:</td><td> $(1-d)P^{E}+f(1)$ </td><td>c(Qu)</td></tr></table>

The honest seller's payoff in period 1 is $( 1 - d ) P ^ { E } - c ( \mathrm { Q u } )$ . The payoff in period 2 is $[ ( 1 - d ) P ^ { E } + f ( 1 ) - c ( \mathrm { Q u } ) ] / ( 1 + r )$ The model assumes that the characteristics that make a seller honest are fixed and as a result the honest seller does not change its behavior in period 2 (i.e., it would not lower product quality for the second transaction). The sum of the payoffs from being honest is:

$$
\begin{array}{l} (1 - d) P ^ {E} - c (\mathrm{Qu}) + [ (1 - d) P ^ {E} + f (1) - c (\mathrm{Qu}) ] / (1 + r) \\ \Rightarrow (2 + r) (1 - d) P ^ {E} / (1 + r) + f (1) / (1 + r) - (2 + r) c (\mathrm{Qu}) / (1 + r) \\ \Rightarrow (2 + r) [ (1 - d) P ^ {E} - c (\mathrm{Qu}) ] / (1 + r) + f (1) / (1 + r) \end{array}
$$

The positive feedback earned from the first transaction can help buyers in the second period update their beliefs regarding this particular seller. Each positive feedback count enhances buyer trust. This mechanism also makes it possible for individual sellers to use feedback as a device to distinguish themselves from other sellers. f (1) represents a price premium that is earned by the honest seller. For an honest seller to break even or achieve economic profits, the present value of the above payoff must be greater than or equal to zero:

$$
(2 + r) [ (1 - d) P ^ {E} - c (\mathrm{Qu}) ] / (1 + r) + f (1) / (1 + r) \geq 0
$$

which gives:

$$
f (1) \geq (2 + r) [ c (\mathrm{Qu}) - (1 - d) P ^ {E} ]\tag{3}
$$

The condition in Eq. (3) indicates that the premium earned by the honest seller as a result of positive feedback must cover the cost of producing a high quality product. As a result, the honest seller is at least as well off offering a high quality product as exiting the market. However, there is no guarantee that a premium high enough can be earned to meet the condition in Eq. (3).

Seller honesty may not be exogenous as assumed by asymmetric information models [16] and reputation studies [19,30]. Being honest or dishonest is dependent on the present value of future rents. A seller chooses to be honest in order to maintain a continual stream of income that can be diminished if it produces low quality products and thus has to accept lower prices [32]. The continued existence of a high quality market is predicated on a price premium that results in positive profits for the honest seller.

[30] examined the issue of quality-assuring prices and called the positive profit earned by the honest seller a premium to reputation. He further described the process through which the positive profit is earned. Firms enter the high quality market by initially selling high-quality goods at a minimum quality price $( ( 1 - d ) P ^ { E }$ in the model above), which leads to a loss. Future price premiums are required to offset the initial losses incurred by a firm as a result of such pricing behavior. In the two period example, if the premium only covers production cost (that is, π = 0), a seller faces zero economic profits if it chooses to be honest.

The revenues and costs for a dishonest seller would be the following:

<table><tr><td colspan="3">A dishonest seller:</td></tr><tr><td></td><td>Revenue</td><td>Cost</td></tr><tr><td>Period 1:</td><td> $P=(1-d)P^{E}$ </td><td> $c(\text{Qu}^{\text{Low}})$ </td></tr><tr><td>Period 2:</td><td> $(1-d)P^{E}-g(1)$ </td><td> $c(\text{Qu}^{\text{Low}})$ </td></tr></table>

The payoff for the dishonest seller is:

$$
(2 + r) [ (1 - d) P ^ {E} - c (\mathrm{Qu} ^ {\text { Low }}) ] / (1 + r) - g (1) (1 + r)\tag{4}
$$

If the payoff for the dishonest seller is greater than the payoff for the honest seller, then the market for quality products disappears; that is, the opportunity cost to being an honest seller would be greater than the payoffs for being honest. A positive opportunity cost serves as a legitimate incentive for sellers to employ a dishonest strategy if being honest only earns a seller zero economic profits. The function, g(1), is the price penalty associated with negative feedback. The larger the price penalty associated with negative feedback, the smaller the opportunity cost incurred by an honest seller.

The total revenue in present value terms for an honest seller in the two period model is as follows:

$$
(2 + r) (1 - d) P ^ {E} / (1 + r) + f (1) / (1 + r)\tag{a}
$$

The total production cost in present value terms is:

$$
(2 + r) c (\mathrm{Qu}) / (1 + r)\tag{b}
$$

The total opportunity cost in present value terms is:

$$
(2 + r) [ (1 - d) P ^ {E} - c (\mathrm{Qu} ^ {\text { Low }}) ] / (1 + r) - g (1) / (1 + r)\tag{c}
$$

An honest strategy will be chosen by a seller if and only if $( \mathrm { a } ) - ( \mathrm { b } ) { \neq } ( \mathrm { c } )$ (assuming that in the case of equality, the honest seller will choose to remain honest). A seller will choose to be honest if:

$$
\begin{array}{l} (a) - (b) - (c) \\ \neq 0 (2 + r) (1 - d) P ^ {E} / (1 + r) + f (1) / (1 + r) - (2 + r) c (\mathrm{Qu}) / (1 + r) \\ - (2 + r) [ (1 - d) P ^ {E} - c (\mathrm{Qu} ^ {\mathrm{Low}}) ] / (1 + r) + g (1) / (1 + r) \geq 0 \Rightarrow (2 + r) [ c (\mathrm{Qu} ^ {\mathrm{Low}}) \\ - c (\mathrm{Qu}) ] / (1 + r) + f (1) / (1 + r) + g (1) / (1 + r) \geq 0 \Rightarrow f (1) \geq (2 + r) [ c (\mathrm{Qu}) - c (\mathrm{Qu} ^ {\mathrm{Low}}) ] - g (1) \end{array}\tag{5}
$$

It can be seen from the condition in Eq. (5) that the larger the impact of the feedback system (both positive and negative) the more likely it becomes that sellers will choose the honest strategy. This is consistent with [18] who argued that cheating is influenced by the probability of being caught. The decision of a seller to pursue an honest strategy is dependent on the premium earned by positive feedback, the penalty incurred from negative feedback, and on the difference in production costs between high and low quality products. The condition shown in Eq. (5) can be easily expanded to the infinite period case (see Appendix A).

## 3.3. Feedback problems

So far, we have assumed away some common problems associated with online feedback systems. The most often discussed problems are the lack of incentives to leave feedback, shilling, and ID changing. The feedback incentive problem refers to the potential for system users to act as free riders. If there is information to be gained from leaving feedback, the gain accrues to all buyers as a group, rather than to a particular individual. An individual buyer may not have an incentive to leave feedback, since free riding may be a short run optimal strategy for the buyer. We define shilling as unwarranted positive feedback left by a seller's collusive partners or by the seller, itself. A shilling variant may be unwarranted negative feedback left by malicious attackers. With shilling, a dishonest seller will have a positive probability of receiving positive feedback and an honest seller will have a positive probability of receiving negative feedback. Shilling reduces the credibility of the feedback system which decreases the price premium buyers are willing to give to honest sellers and the penalty to dishonest sellers from receiving negative feedback. ID changing refers to the potential for dishonest sellers to restart their business as a new entity whenever negative feedback reveals them to be dishonest. ID changing allows dishonest sellers to escape the negative consequences of being dishonest.

Despite collective incentives that may induce participants to leave feedback [21,3,24,14 etc.], there is no documented research to support the notion that an individual buyer has strong economic incentives to leave feedback.

[22] claimed: “there is little economic motivation for providing feedback subsequent to a transaction”. [27] found that only 50% of all participants chose to leave feedback. The question is how this lack of incentive to leave feedback impacts the effectiveness of the feedback system. The lack of incentives will result in less feedback and thus increase the time (or number of transactions) necessary for an honest seller to earn sufficient premiums on its sales to justify its honest strategy. This increase in time raises both the setup costs and the opportunity costs faced by an honest seller. For the purposes of this paper, setup costs refer to the losses incurred by a seller before it can establish a good enough reputation to break even in its operations. Opportunity costs are the profits an honest seller forgoes by adopting an honest strategy rather than a dishonest strategy. (See the appendix for details.) The setup costs rise in the case of incomplete feedback since it takes longer for honest sellers to gain a price sufficient to cover the marginal cost of selling a high quality product. As shown in Fig. 1, instead of break-even at $t , t ^ { \prime } > t$ is the new break-even point due to the longer time needed to earn sufficient positive feedback.

As defined in the Appendix, setup cost can be calculated as follows:

$$
\operatorname{SetupCost} (\mathrm{Qu}) = \sum_ {i = 1} ^ {t} \left[ \frac {1}{(1 + r) ^ {i - 1}} (f (i - 1) + (1 - d) P ^ {E} - c (\mathrm{Qu})) \right]\tag{6}
$$

when the break even point is t. Delaying the break-even point to $t ^ { \prime } > t$ increases the setup cost an honest seller faces. If negative feedback is missing, the opportunity cost increases further. As defined in the appendix, opportunity cost can be calculated as follows:

$$
\text { OpportunityCost } = \sum_ {i = 1} ^ {m} \frac {1}{(1 + r) ^ {i - 1}} g (i - 1) + \frac {(1 + r) (1 - (1 + r) ^ {- m})}{r} [ (1 - d) P ^ {E} - c (\mathrm{Qu} ^ {\mathrm{Low}}) ]\tag{7}
$$

[30] argued that for a signal to be effective, people have to trust the signal. The presence of shilling by sellers influences the credibility of the feedback. $f ( )$ and $g ( \ u )$ are adjustments buyers make after observing feedback. If the feedback cannot be trusted as a result of sellers leaving either false positive or false negative feedback, then the adjustments buyers make as a result of feedback will be inhibited. If the actual quality of a seller's product is $\mathrm { Q u } _ { \mathrm { A } } ,$ , the probability of receiving correct/incorrect feedback based on actual quality can be described as follows:

$$
\begin{array}{l} p (n _ {p} ^ {t} - n _ {p} ^ {t - 1} = 1 | \mathrm{Qu} _ {\mathrm{A}} = \mathrm{Qu}) = \psi , \text {while} p (n _ {n} ^ {t} - n _ {n} ^ {t - 1} = 1 | \mathrm{Qu} _ {\mathrm{A}} = \mathrm{Qu}) = 1 - \psi \\ p (n _ {p} ^ {t} - n _ {p} ^ {t - 1} = 1 | \mathrm{Qu} _ {\mathrm{A}} = \mathrm{Qu} ^ {\text {Low}}) = \tau , \text {while} p (n _ {n} ^ {t} - n _ {n} ^ {t - 1} = 1 | \mathrm{Qu} _ {\mathrm{A}} = \mathrm{Qu} ^ {\text {Low}}) = 1 - \tau \end{array}
$$

where $p ( n _ { p } ^ { t } - n _ { p } ^ { t - 1 } = I | \ u { Q u } _ { A } = \ u { Q u } ) = \psi$ implies receiving positive feedback is based on sending out high quality products, while $p ( n _ { n } ^ { \dot { t } } - n _ { n } ^ { \dot { t } - I } = I | \uplus u _ { A } = \uplus u ) = I - \psi$ means the seller, unfortunately, received negative feedback after sending out a high quality product. $p ( n _ { p } ^ { t } - \bar { n } _ { p } ^ { t - 1 } = I | \mathcal { Q } u _ { A } = \mathcal { Q } u ^ { L o w } ) = \tau$ implies the seller received positive feedback after he/she sent out a low quality product, while $p ( n _ { n } ^ { t } - n _ { n } ^ { t - 1 } = I | \ u { Q u } _ { A } = \ u { Q u } ^ { L o w } \ u ) = I - \tau$ means that receiving negative feedback is based on sending out low quality products. A bidder who is aware that there may be shilling updates his/her belief on the latest positive feedback by the following:

![](/api/attachments/SBEXFDXV/fulltext/images/33c29af8155a5e4deb92f1f78a538dbc9bdeae0f6cdc9a555b46deac9df84547.jpg)  
Fig. 1. Partial vs. full feedback.

$$
\begin{array}{l} p (\mathrm {Qu_ {A}} = \mathrm{Qu} | n _ {p} ^ {t} - n _ {p} ^ {t - 1} = 1) \\ = \frac {p (\mathrm {Qu_ {A}} = \mathrm{Qu}) p (n _ {p} ^ {t} - n _ {p} ^ {t - 1} = 1 | \mathrm {Qu_ {A}} = \mathrm{Qu})}{P (\mathrm {Qu_ {A}} = \mathrm{Qu}) p (n _ {p} ^ {t} - n _ {p} ^ {t - 1} = 1 | \mathrm {Qu_ {A}} = \mathrm{Qu}) + p (\mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}}) p (n _ {p} ^ {t} - n _ {p} ^ {t - 1} = 1 | \mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}})} = \frac {\alpha \psi}{\alpha \psi + (1 - \alpha) \tau} \end{array}
$$

Note that unless τ is zero, there will always be a discount on bids due to the feedback credibility issue under asymmetric information on product quality; i.e., the value of positive feedback is discounted by bidders, thus increasing setup cost. Similarly, the value of negative feedback is also discounted as follows:

$$
\begin{array}{l} p (\mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}} | n _ {n} ^ {t} - n _ {n} ^ {t - 1} = 1) \\ = \frac {p (\mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}}) p (n _ {n} ^ {t} - n _ {n} ^ {t - 1} = 1 | \mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}})}{P (\mathrm {Qu_ {A}} = \mathrm{Qu}) p (n _ {n} ^ {t} - n _ {n} ^ {t - 1} = 1 | \mathrm {Qu_ {A}} = \mathrm{Qu}) + p (\mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}} = 1) p (n _ {n} ^ {t} - n _ {n} ^ {t - 1} | \mathrm {Qu_ {A}} = \mathrm {Qu^ {Low}})} \\ = \frac {(1 - \alpha) (1 - \tau)}{\alpha (1 - \psi) + (1 - \alpha) (1 - \tau)} \end{array}
$$

A discount on the value of negative feedback to bidders weakens the effect of negative feedback in differentiating between the prices of high and low quality goods. If feedback is completely not thought to be credible, then buyers may simply choose to ignore it. The feedback system is then not able to assure the presence of a market for high quality products. We are essentially back to the initial problem: dishonest sellers will drive honest sellers out of the market. If shilling only delays the time required to separate the high and low quality sellers, then its impact is similar to the incomplete feedback problem. The setup and opportunity costs of the honest seller are increased and the final price of high quality products will be higher than would be the price if no shilling were to occur.

The third feedback problem we consider is ID changing. Each online auction participant needs to register an ID, equivalent to brand name for a brick-and-mortar firm. Buyers leave feedback on a specific ID. If the feedback system works well, dishonest sellers receive negative feedback and the price they receive for their low quality products will be driven down to marginal cost. If dishonest sellers can change IDs once this occurs, it raises the possibility that a dishonest seller can continually earn profits by switching IDs. Thus, ID switching raises the opportunity costs associated with being an honest seller. The market for high quality products may not emerge, or higher price differentials for high quality products may be required to overcome the greater opportunity costs. Similar to [14], our analysis shows that seller incentives to behave honestly can be greatly weakened.

To examine the problem of ID changing, the results derived from the case of incomplete feedback can be borrowed. Any seller using a new ID can be subject to the setup cost as follows:

$$
\operatorname{SetupCost} (\mathrm{Qu}) = \sum_ {i = 1} ^ {t} \left[ \frac {1}{(1 + r) ^ {i - 1}} (f (i - 1) + (1 - d) P ^ {E} - c (\mathrm{Qu})) \right]\tag{8}
$$

The honest seller's opportunity cost is equal to the profits earned by the dishonest seller:

$$
\text { OpportunityCost } = \sum_ {i = 1} ^ {m} \frac {1}{(1 + r) ^ {i - 1}} g (i - 1) + \frac {(1 + r) (1 - (1 + r) ^ {- m})}{r} [ (1 - d) P ^ {E} - c (\mathrm{Qu} ^ {\mathrm{Low}}) ]\tag{9}
$$

The net gain (NG) to a dishonest seller is the difference between its profits from product sales (i.e., the opportunity cost to the honest seller) and the setup cost which will only be incurred if he/she delivers high quality products in the initial period:

$$
\mathrm{NG} _ {1} = \sum_ {n = 1} ^ {\infty} (\text { OpportunityCost } - \text { SetupCost })\tag{10}
$$

$\mathrm { N G } _ { 1 }$ seems to suggest that the setup cost can be a viable method to reduce the incentive for ID changing. The setup cost, if increased, should reduce the net gain from ID changing. However, increasing setup cost is a double-blade sword. On one side, the incentive to change ID may be weakened; on the other side, higher setup cost also applies to all honest sellers. Hence, the net effect of increasing setup cost should be better explored before any conclusion can be drawn.

![](/api/attachments/SBEXFDXV/fulltext/images/87596f6875fa3a5a9920604435c5f347fcbeecd9d20687b6e7ea7791355fa3e6.jpg)  
Fig. 2. ID changing strategy by a dishonest seller.

The calculation of $\mathrm { N G } _ { 1 }$ assumes that a dishonest seller would deliver high quality products in the initial period. Alternatively, the dishonest seller can simply choose to deliver low quality products in every period until no more profits can be earned and change to a new ID. In this case, the setup cost may be as low as zero and the dishonest seller's net gain will equal the honest seller's opportunity costs:

$$
\mathrm{NG} _ {2} = \sum_ {n = 1} ^ {\infty} (\text { OpportunityCost })\tag{11}
$$

As a result, a high setup cost makes it more likely for a dishonest seller to follow this simple path.

An ID changing example is illustrated in Fig. 2. As shown in the figure, a dishonest seller will begin selling at a starting price, $P ^ { E } . \mathrm { A } 1$ some point, at or before the dishonest seller reaches the price at which positive economic profits are no longer earned, $c ( \mathrm { Q u } ^ { \mathrm { L o w } } )$ , the seller will switch IDs and begin, again, at the starting point. The result of an ID changing behavior is that a dishonest seller can always negate the penalty incurred from negative feedback by restarting its operations. It is easy to see that if this practice was followed by a significant proportion of sellers, the online auction market for high quality products would be greatly endangered. The initial price for a product would be greatly discounted as the market for honest sellers disappeared and as buyers re-evaluated their chances of obtaining a quality product.

## 4. Discussion

In the modeling section, above, we show first, following [1], how the market for quality products cannot be sustained under conditions of asymmetric information. We next demonstrate how a reputation-based feedback system can resurrect the market for high quality products in that it increases the information available to buyers, thereby helping to level the playing field between buyers and sellers. Finally, we show how three problems with feedback systems may undermine the effectiveness of the systems by increasing the setup and/or opportunity costs to sellers of high quality products.

An important consideration for auction sites, such as eBay.com, is how they can maintain the integrity of their feedback systems. It is clear that there are a number of actions that the auction sites can undertake. First, with respect to the problem of incomplete feedback, the auction sites could offer incentives to buyers to leave feedback. For example, buyers that leave feedback could be eligible for prize draws or could accumulate “frequent purchase points” that may be used for the purchase of select products. Feedback leaving is often considered a reciprocal process [10]. Hence, the auction site or the seller could make it easy for buyers to leave feedback by sending out a URL that would allow a buyer to access a feedback site with a single mouse click. The seller may also want to leave feedback for the buyer first in return for a higher probability of receiving feedback from the buyer.

The problem of shilling may be tackled in a number of ways. For example, an auction house could limit the feedback from any one buyer to a single response as a first step. In addition, the auction house could use data mining techniques to identify buyer–seller combinations to determine if self-dealing is a consideration resulting in inflated positive feedback counts. Finally, if shilling is more serious a concern for positive feedback, the auction house can give more weight to negative feedback in computing the reputation score of a seller.

The problem of ID changing may be the trickiest to tackle. The auction house could make IDs more difficult to obtain, for example, by requiring the disclosure of personal information, such as social security numbers, that would make ID changing difficult. However, given the sensitive nature of private information, market participants may be reluctant to cooperate. Less sensitive information that is harder to forge and is capable of identifying an individual can be used as a second-best solution. For instance, Yahoo Auctions requires every seller to provide a valid credit card. It is certainly harder to forge a credit card than to obtain two email addresses, which should alleviate the ID changing problem to a certain extent. ID changing also has its bearing on the other two problems. When auction houses use data mining methods to identify buyer–seller combinations to deal with shilling problems, the assumption is that each ID represents a unique individual. An ID that can be easily obtained and frequently changed flatly complicates the combination identification process since one can use a large set of IDs to collude that may never alarm the data mining system. As a buyer looses his/her confidence in seller identity, leaving feedback is discouraged as well.

## 5. Conclusions, implications, and future research

In his landmark paper, [1] demonstrated how, given asymmetric information between buyers and sellers, honest sellers of high quality products can be driven out of the market by dishonest sellers of low quality products. The online market is especially susceptible to low quality sellers driving out high quality sellers, given the anonymous nature of the market; i.e., in most cases buyers do not personally know sellers, nor can they physically inspect products prior to purchase. As a result, a feedback system that establishes the reputation of online sellers can be especially important in maintaining the market.

This study contributes to extant literature in the following ways: In our analytical model, we show how a feedback system can offer returns to honest sellers of high quality products after an initial period of reputation building in which setup costs have been incurred. Second, we show that the provision of both positive and negative feedback is critical for the functioning of an effective feedback system. Both positive and negative feedback is important in ensuring the value of a high quality product, or the honesty of a seller. Third, three potential drawbacks of a feedback system are integrated into the model for determining seller incentives to provide high quality products. The three practices, notably incomplete feedback, shilling, and ID changing, can reduce the effectiveness of the feedback system by increasing the time required by honest sellers to reach a breakeven price, thereby increasing the setup costs necessary to build a reputation. Among the three, ID changing can make the feedback system completely ineffective for maintaining a market for high quality products.

Clearly, it is the best interest of the market maker (e.g., eBay.com) to enhance the effectiveness of feedback.

Possibilities would include rewarding sellers and buyers for providing feedback, toughening the criteria for acquiring IDs, and closely monitoring transactions to guard against self-buys and shilling behavior.

There exists opportunities for future researchers to both enhance the analytical model to account for other behaviors (e.g., by using non-linear functions for positive and negative feedback) and to undertake empirical work in this area. On the empirical side, although there has been research conducted on the effectiveness of feedback systems, much of the work has covered standard products (e.g., coins). Since feedback systems are most helpful when products can be differentiated by quality, further studies that use differentiable products may be helpful in determining the value of feedback systems and the effects of the various strategies (shilling, ID changing, etc.) on the operations of the online markets.

Recent studies of online auctions have focused on firm practices in using online auctions, such as [26,13,5] etc. The effects of strategic options, such as secret reserve prices, bid increment, minimum bid/starting bid, and the use of buy-it-now prices should also be thoroughly studied. From the supply chain point of view, the question of how feedback systems or online auctions can help to achieve more efficient supply chains should be explored; for example, how a feedback system can help in selecting suppliers and in segmenting consumer demand.

The online auction markets offer participants not only expanded market reach, but also strategic flexibility in market research and operation optimization. For example, a recent paper by [31] developed methods to use online auctions to achieve optimal product configuration. These opportunities may be negated by an inefficient market, such as a market that lacks credence. Establishing online auction credence is, therefore, critical to the continued development of online auction markets.

A limitation of our paper is that we assume that positive and negative feedback responses are weighed equally by buyers. This may not be the case. Buyers may place more emphasis on negative feedback responses than on positive responses. More complex methods of determining a reputational score may provide information to buyers that more adequately differentiate between honest and dishonest buyers and sellers. See, for example, [14]'s use of exponential smoothing to calculate reputational scores.

## Appendix A

In this section, the condition shown in Eq. (2) is expanded to an infinite number of periods. To simplify the model we assume that sellers choose to be honest or dishonest in time period one and that this decision is not changed in subsequent time periods.

Revenues and costs associated with being dishonest in an infinite period model are:

<table><tr><td></td><td>Gain</td><td>Cost</td></tr><tr><td>Period 1:</td><td> $P=(1-d)P^{E}$ </td><td> $c(\text{Qu}')$ </td></tr><tr><td>Period 2:</td><td> $(1-d)P^{E}+g(1)$ </td><td> $c(\text{Qu}')$ </td></tr><tr><td>Period 3:</td><td> $(1-d)P^{E}+g(2)$ </td><td> $c(\text{Qu}')$ </td></tr><tr><td>Period m:</td><td> $(1-d)P^{E}+g(m-1)$ </td><td> $c(\text{Qu}')$ </td></tr></table>

For an honest seller, the infinite period model results in the following revenues and costs:

<table><tr><td></td><td>Gain</td><td>Cost</td></tr><tr><td>Period 1:</td><td> $P=(1-d)P^{E}$ </td><td>c(Qu)</td></tr><tr><td>Period 2:</td><td> $(1-d)P^{E}+f(1)$ </td><td>c(Qu)</td></tr><tr><td>Period 3:</td><td> $(1-d)P^{E}+f(2)$ </td><td>c(Qu)</td></tr><tr><td>Period n:</td><td> $(1-d)P^{E}+f(n_{p}-1)$ </td><td>c(Qu)</td></tr></table>

The result of the feedback system is to generate an increase in price as positive feedback is received and a reduction in price as negative feedback is received. As a result the present value of the price received for the product can be expressed as a function of the starting point $( 1 - d ) P ^ { E }$ and the cumulative effect of the feedback at any given point in time:

$$
P = \frac {1}{(1 + r) ^ {n _ {p} - 1}} f (n _ {p} - 1) + (1 - d) P ^ {E}
$$

This equation can be approximated by a continuous function which allows the use of integration to compute the sum of the returns over time. The effects of the feedback, both positive and negative, have been defined previously as concave functions. Fig. 3 gives a possible shape of the curve as an example.

An honest seller realizes revenues of $( 1 - d ) P ^ { E }$ in the first time period as a result of beliefs about the industry. An honest seller consistently sends out high quality products and earns only positive feedback. t denotes the time period when the price level equals $P ^ { E }$ , where $P ^ { E } { = } c ( \mathrm { Q u } )$ . Area A defined by the vertical axis, the price curve, and the horizontal line at $P ^ { E }$ in Fig. 1 can be labeled as the setup cost (beginning loss) incurred by the honest seller. Up to time period t, the honest seller loses money on each unit of the product sold. Assuming a seller conducts one transaction in each period, and that each transaction earns the seller one feedback response, then the number of periods and the number of transactions is equivalent. This allows the price function to be integrated with respect to the number of feedback responses. The losses accumulated in the first t periods can be perceived as the setup cost.

$$
\begin{array}{l} \text { SetupCost(Qu) } \\ = \sum_ {i = 1} ^ {t} \left[ \frac {1}{(1 + r) ^ {i - 1}} (f (i - 1) + (1 - d) P ^ {E} - c (\mathrm{Qu})) \right] \end{array}
$$

An honest seller begins to earn positive returns after period $t ,$ denoted by area B in Fig. 3. The present value of the sum of all positive profits from time period t onward is:

$$
\begin{array}{l}\text { Profits } (\mathrm{Qu})\\= \lim _ {n _ {p} \rightarrow \infty} \int_ {t} ^ {n _ {p}} \left[ \frac {1}{(1 + r) ^ {n _ {p} - 1 + t}} (f (n _ {p} - 1) + (1 - d) P ^ {E} - c (\mathrm{Qu})) \right] d n _ {p}\end{array}
$$

Profits earned as a result of being honest are therefore:

$$
\text { Profits } (\mathrm{Qu}) - \text { SetupCost } (\mathrm{Qu}) \geq 0\tag{A - 1}
$$

This result only offers incentives for an honest seller to remain in a market. In order to ensure that the honest seller does not initially choose the dishonest strategy, the seller also has to cover the opportunity costs of choosing the honest strategy. The present value of the opportunity cost associated with being honest is given by:

![](/api/attachments/SBEXFDXV/fulltext/images/16568299783d43e0f469b1a5357d63699c5bdf52556b8abcbf73f87f15d7ccb2.jpg)  
Fig. 3. Price curve: infinite necessary condition.

$$
\begin{array}{l} \text { OpportunityCost } = \sum_ {i = 1} ^ {m} \frac {1}{(1 + r) ^ {i - 1}} g (i - 1) \\ \quad + \frac {(1 + r) (1 - (1 + r) ^ {- m})}{r} \\ \quad \times [ (1 - d) P ^ {E} - c (\mathrm{Qu} ^ {\prime}) ] \end{array}
$$

resulting in the following inequality:

$$
\text { Profits } (\mathrm{Qu}) - \text { SetupCost } (\mathrm{Qu}) - \text { OpportunityCost } \geq 0 \tag {A-2}
$$

This is a necessary but not sufficient condition to ensure that firms do not switch to a dishonest strategy at some point in time. It may still be possible that the rewards for complex and dishonest strategies may result in higher payoffs.

## References

[1] G. Akerlof, The market for “Lemons”: quality uncertainty and the market mechanism, The Quarterly Journal of Economics 84 (3) (1970) 488–500.

[2] N. Award, C. Dellarocas, X.Q. Zhang, Is online word of mouth a complement or substitute to traditional means of consumer conversion, Proceedings of Workshop on Information Systems and Economics. Washington, DC., 2004.

[3] S. Ba, P. Pavlou, Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior, MIS Quarterly 26 (2002) 243–268.

[4] Y. Bakos, C. Dellarocas, Cooperation without enforcement? A comparative analysis of litigation and online reputation as quality assurance mechanisms, MIT Sloan Working Paper, No. 4295-03, 2002.

[5] R. Bapna, P. Goes, A. Gupta, Analysis and design of business-toconsumer online auctions, Management Science 49 (1) (2003) 85–101.

[6] G. Bolton, E. Katok, A. Ockenfels, How effective are online reputation mechanisms? An experimental investigation, Management Science 50 (11) (2004) 1587–1602.

[7] N. Bruce, E. Haruvy, R. Rao, Seller rating, price, and default in online auctions, Journal of Interactive Marketing 18 (4) (2004) 37–51.

[8] C. Dellarocas, Building trust on-line: the design of reliable reputation reporting, MIT Sloan Working Paper, 2001.

[9] C. Dellarocas, Analyzing the economic efficiency of eBay-like online reputation reporting mechanism, MIT Sloan Working Paper, 2001.

[10] C. Dellarocas, The digitization of word of mouth: promise and challenges of online feedback mechanisms, Management Science 49 (10) (2003) 1407–1424.

[11] C. Dellarocas, Efficiency and robustness of binary feedback mechanisms in trading environment with moral hazard, Proceed

ings of the 4th ACM Conference on Electronic Commerce, ACM Press, San Diego, CA, 2003, pp. 11–18.

[12] S. Dewan, V. Hsu, Adverse selection in electronic markets: evidence from online stamp auctions, Journal of Industrial Economics 52 (4) (2004) 497–516.

[13] H. Etzion, E. Pinker, A. Seidmann, Analyzing the simultaneous use of auctions and posted prices for online selling, Working Paper No. CIS 03–01, Computer Information Systems, University of Rochester, 2004.

[14] M. Fan, Y. Tan, A. Whinston, Evaluation and Design of online cooperative feedback mechanisms for reputation management, IEEE Transactions on Knowledge and Data Engineering 17 (2) (2005) 244–254.

[15] Federal Trade Commission. Internet auctions: a guide for buyers and sellers, 2005 available at www.FTC.gov.

[16] D. Fudenberg, J. Tirole, Game Theory, The MIT Press, London, 2000.

[17] D. Houser, J. Wooders, Reputation in auctions: theory and evidence from eBay, Working Paper, Department of Economics, University of Arizona, 2000.

[18] R. Kauffman, C. Wood, Running up the bid: detecting, predicting, and preventing reserve price shilling in online auctions, Proceedings of the 5th International Conference on Electronic Commerce, ACM Press, Pittsburgh, PA, 2003, pp. 259–265.

[19] B. Klein, K. Leffler, The role of market forces in assuring contractual performance, The Journal of Political Economy 89 (4) (1981).

[20] J. Livingston, How valuable is a good reputation? A sample selection model of Internet auctions, Working Paper, Department of Economics, University of Maryland, 2003.

[21] K. McCabe, S. Rassenti, V. Smith, Design auction institutions for exchange, IEEE Transactions 31 (9) (1999) 803–811.

[22] C. McDonald, V. Slawson, Reputation in an Internet auction market, Economic Inquiry 40 (4) (2000) 633–651.

[23] M. Melnik, J. Alm, Does a seller's ecommerce reputation matter? Evidence from eBay auctions, Journal of Industrial Economics L (3) (2002) 337–349.

[24] F. Nah, K. Siau, Y. Tian, M. Ling, Knowledge management mechanisms in e-commerce: a study of online retailing and auctions sites, The Journal of Computer Information Systems 42 (5) (2002) 119-129

[25] J.M. Perloff, Microeconomics, Addison-Wesley, Menlo Park, California, 1998.

[26] E. Pinker, A. Seidmann, Y. Vakrat, Managing online auctions: current business and research issues, Management Science 49 (11) (2003) 1457–1484.

[27] P. Resnick, R. Zeckhauser, The value of reputation on eBay: A controlled Experiment, School of Information, University of Michigan, 2002.

[28] S. Rice, Online reputations with noisy transactions: an experimental study, Proceedings of Workshop on Information Systems and Economics. Washington, DC, 2004.

[29] A. Roth, A. Ockenfels, Last minute bidding and the rules for ending second-price auctions: theory and evidence from a natural experiment on the Internet, NBER Working Paper 7729 (2000).

[30] C. Shapiro, Premiums for high quality products as returns to reputation, The Quarterly Journal of Economics 98 (4) (1983).

[31] E. Snir, M. Sobol, Using online auctions to choose optimal product configurations, Proceedings of the 25th International Conference on Information Systems. Washington, DC, 2004, pp. 615–627.

[32] J. Stiglitz, The causes and consequences of the dependence of quality on price, Journal of Economic Literature 25 (1) (1987) 1–48.

[33] S. Woodward, Online Auction Fraud. available at www. ezinearticles.com (2005).

[34] D.J. Wu, F. Zhong, S. Narasimhan, H. Zhang, Internet auction equilibrium selection: theory, evidence and impact of strategic bidding behavior, Proceedings of Workshop on Information Systems and Economics. Washington, DC, 2004.

![](/api/attachments/SBEXFDXV/fulltext/images/e5b633933a5cabc54c96e9d60923e86c3e99e294b5812e470766529bc500d126.jpg)  
Ming Zhou has served on the faculty of the Lucas Graduate School of Business at the San Jose State University since 2006. He is currently an assistant professor of operations and supply chain management. He received his Ph.D. in Supply Chain Management from the University of Maryland. Zhou's research focuses on online reputation systems and security, service industry management, online auctions, and operations strategies. He is a DSI, and CSCMP.

member of INFORMs,  
![](/api/attachments/SBEXFDXV/fulltext/images/ce17097089832e525f3874e9bb1e587ce4d015740aa3304a041611139520e290.jpg)

Martin Dresner has served on the faculty of the R.H. Smith School of Business at the University of Maryland since 1988 where he is currently Professor of Logistics and Transportation. He received his Ph.D. in Policy Analysis from the University of British Columbia. Dresner's research focuses on two broad areas, air transport policy and logistics management. He has published papers in leading transportation, logistics, and supply chain journals, as

well as in related fields. In addition, Dresner has co-authored a book on supply chain management. Professionally, he is Series Editor for Research in Transportation Economics, editor of Transportation Journal, and is active in several organizations, including the Transportation and Public Utilities Group and the Transportation Research Forum. He has testified before the House Aviation Subcommittee, and has worked on consulting projects for a number of organizations, including the Maryland Aviation Administration and the U.S. Department of Energy.

![](/api/attachments/SBEXFDXV/fulltext/images/343a8a41f3c69705d5dd5a824750e7e8cca33ac4bccf3dc9cfd7807b30abbc0b.jpg)

Professor Robert J. Windle joined the R.H. Smith School at the University of Maryland in 1988 after working for six years at a private economic consulting firm. His area of specialization is applied transportation and public utility economics with a particular emphasis on the airline industry. His research focuses on public policy issues such as the threat of predatory pricing practices in the airline industry, the impact of hub and spoke systems

on competition at hub airports, and the potential impact of opening the interstate highway system to economic development. Professor Windle has published over 25 articles in leading academic journals and is a member of the American Economic Association and the Transportation Research Forum. He has consulted for various private and public agencies including the Maryland Aviation Administration, the World Travel and Tourism Council, and the Greater Washington Board of Trade.
