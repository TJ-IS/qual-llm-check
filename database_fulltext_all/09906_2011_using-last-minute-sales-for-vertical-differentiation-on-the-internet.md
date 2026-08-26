---
otero_id: 9906
otero_key: "X9E5UYG2"
title: "Using “last-minute” sales for vertical differentiation on the Internet"
authors: "Ori Marom; Abraham Seidmann"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using “last-minute” sales for vertical differentiation on the Internet

Ori Marom <sup>a</sup>, Abraham Seidmann <sup>b,</sup>⁎

<sup>a</sup> RSM Erasmus University, Burgemeester Oudlaan 50, 3062 PA Rotterdam, The Netherlands

<sup>b</sup> William E. Simon Graduate School of Business Administration, University of Rochester, Rochester, NY 14627, United States

## a r t i c l e i n f o

Available online 5 February 2011

JEL classification: D42 L1

Keywords: Price discrimination Risk aversion Monopolistic quality provision

## a b s t r a c t

In Internet-based commerce, sellers often use multiple distribution channels for the sale of standard consumer goods. We study a model of second-degree price discrimination in which a monopolist sells to riskaverse buyers. The seller uses two channels that differ in their risk attributes. In one channel prices and qualities are <sup>fi</sup>xed and availability is assured. In the second channel, the seller offers a joint distribution of prices and qualities and may not guarantee availability. We characterize optimal two-channel selling policies. We show that it can be optimal to offer multiple identical items in a random sale event. However, the seller cannot bene<sup>fi</sup>t by offering two distinct quality levels in a sale event that is held with probability smaller than one. We use the model to offer explanations for the observed behavior of online sellers and discuss implementation issues in recent e-commerce environments

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

In Internet-based commerce, sellers often use multiple distribution channels for the sale of standard consumer goods. For example, within a two-week period, Carnival Cruise Lines offered units of the same cabin class on one of its ships in three distinct ways: standard posted prices, ascending bid (“English”) auctions, and “last-minute” clearance sales. A possible explanation for such behavior is that sellers like Carnival are deliberately embedding price uncertainties into their sales channels in order to employ second-degree price discrimination among buyers who are risk-averse. Buyers who assign higher values to the offered product are typically more reluctant to risk compromising their surplus and are therefore prone to purchase at a higher posted price earlier, while buyers with lower values may wait and attempt to acquire the product at a bargain price.

The Internet has given buyers unprecedented ability to learn about sellers' behavior and use the information in order to search for the best deals. As a result, it is often imperative for online sellers to give careful consideration to strategic consumer behavior when these sellers determine their pricing policies. As an illustration of this, Fig. 1 depicts pricing data sampled from US Airways' website for economy-class travel from three cities in western New York (Buffalo, Rochester, and Syracuse) to Philadelphia. US Airways is the only airline offering nonstop services on these three routes. As the <sup>fi</sup>gure shows, the airline offered dramatically reduced e-Saver™ airfares on <sup>fl</sup>ights from Syracuse about 72 h before their departure but did not offer similar discounts on <sup>fl</sup>ights from either Rochester or Buffalo. Similar to the pattern shown by Fig. 1, the airline offered e-Saver™ discounts from Rochester, Buffalo, or

Syracuse to Philadelphia on 17 out of 35 consecutive weekends (or about 50% of the time) during our observation period.<sup>1</sup> It was not immediately clear to us whether in the presence of well-informed and sophisticated consumers US Airways could sustain a pricing policy that entailed charging advance-purchase prices of up to \$800 for a <sup>fl</sup>ight while offering “last-minute” fares of less than \$200 for a similar <sup>fl</sup>ight with high frequency.

According to our observations, US-based carriers such as American Airlines and US Airways offer special “last-minute” Internet fares only for travel in economy-class. However, some retail travel specialists such as lastminute.com and site59.com offer also high-end hotel accommodations and luxury cruise vacations in “last-minute” promotions. Can airlines bene<sup>fi</sup>t by offering special last-minute promotions for business-class tickets, and if so, how?

This paper provides a simple framework that permits the investigation of these issues. The analysis provides insights into the determination of pro<sup>fi</sup>t-maximizing selling policies that involve the offering of products of distinct qualities through a mechanism that involves both advanced-purchase posted price transactions and a random “last-minute” sale. We use our model to argue that it can be pro<sup>fi</sup>table for a monopolist who offers two products of distinct qualities to commit that with some probability it will not satisfy late demand for one of the products (or both) at low prices. The seller's aim in making such a commitment is to induce consumers with relatively high values to purchase early.

Although several recent papers (Su [16], Aviv and Pazgal [2], Koenigsberg et al. [9], Liu and van Ryzin [10], and Cachon and Swinney [4]) have shown that a monopolist can enhance its pro<sup>fi</sup>ts by deliberately introducing rationing risk (i.e., increasing the likelihood of “stock outs”) all of these models are based on the premise that the sole source of rationing risk in markets is the complete depletion of the seller's inventory. Jerath et al. [7] analyzed a duopoly setting in which strategic consumers who choose to wait may face not only rationing risk but also uncertainty regarding the identity of the purchased product (as when products are transacted by “opaque” online intermediaries such as Hotwire.com). In their model, as well, the rationing risk that consumers face in equilibrium occurs naturally as a consequence of uncertain demand and in<sup>fl</sup>exible supply—it does not result from an up-front commitment made by the seller prior to the realization of the demand.

Table 1  
![](/api/attachments/X9E5UYG2/fulltext/images/390640295b4a701adf953b746e5b16c132071c9b69a76a23305796737850173e.jpg)  
Fig. 1. Pricing data for US Airways <sup>fl</sup>ights between western New York and Philadelphia. Roundtrip fares for departure on 6/6/2009 and return on 6/9/2009. Source: usairways.com.

We, however, will argue that selling strategies that involve an up-front commitment by the seller not to satisfy late demand at low prices can be both profitable and practical. As an illustration of the practicality of making such a commitment, Table 1 documents occurrences of e-Saver™ sales for travel from western New York to Philadelphia. As the table shows, US Airways appears to have followed a policy that precluded offering last-minute discounts on any given route on two consecutive weeks. Indeed, during our 35-week observation period we collected e-Saver™ sales data for 571 different routes on US Airways' domestic network (2666 data points in total) but recorded only 8 instances (or 0.3% of the overall number of recorded sale events) that were not in line with this rule. The fact that sellers contend with strategic consumer behavior on the Internet by using clearance sale policies that are not contingent only on supply and demand but rely also on up-front commitments and other rules gives rise to new and interesting research questions and serves as the main motivation for our work.

We summarize our main research questions as follows. We assume that a monopolist can commit to a selling strategy that involves both advance-purchase posted price selling and a random “last-minute” sale event. Then, what are the determinants of the two-period pro<sup>fi</sup>tmaximizing strategy? What products should optimally be offered in the last-minute sale? How do changes in buyers' risk aversion and willingness to pay for higher quality affect the optimal selling strategy?

## 1.1. Related literature

A number of papers in the price-discrimination literature assume, as we do in this paper, that consumers rationally anticipate price reductions. Coase [5] has famously conjectured that when consumers have perfect foresight and are suf<sup>fi</sup>ciently patient a monopolist will set its price arbitrarily close to marginal cost. The reason is that at any given time period buyers understand the ex post pro<sup>fi</sup>tability of reducing the price in subsequent periods and optimally wait for such reductions to materialize. Stokey [15] formalizes this result and shows that when consumers differ in their degrees of impatience a monopolist will commit to a decreasing pricing path that induces the most impatient consumers to purchase <sup>fi</sup>rst. Besanko and Winston [3] argue that a decreasing price path will result also in an alternative setting with subgame perfect equilibrium (SPE) that does not involve an explicit commitment to prices. Su [16] analyzed an SPE where consumers arrive at a constant rate over time to the point of sale and individually decide whether to purchase immediately, or wait. He shows that the monopolist will dynamically adjust its prices downward over time whenever buyers' waiting costs are positively correlated with their values for the good.

Our model, however, does not consider buyers' disutility from waiting. Rather, we describe a setting in which the consumption occurs at some point in time that is common to all buyers and does not depend on the time of purchase; airline tickets and cruise vacations, for example, <sup>fi</sup>t into this category. Accordingly, our results may apply to a lesser extent to goods that are not consumed immediately after purchase.

The potential segmentation bene<sup>fi</sup>ts that may arise from incentive schemes yielding random outcomes have long been recognized. In two independent seminal studies, Matthews [13] and Maskin and Riley [12] characterize optimal auctions with risk-averse buyers under different sets of assumptions. While assuming that buyers have uniform utility functions and differ only in their valuation of a single item, both studies establish that the seller can devise a truth-revelation mechanism that strictly dominates any one-price scheme while inducing an equilibrium in which almost all buyers are faced with risk. With such an “optimal auction,” every buyer is induced to reveal his value of the good; he is then assigned a schedule that includes a “bid submission” fee, a probability of winning the item, and an “acquisition price” to be paid only if the item is won. In a related study, Marom and Seidmann [11] characterize an optimal scheme for the sale of multiple identical items by a monopolist in a market comprising risk-averse buyers. They assume that the monopolist is restricted to the offering of a two-item menu: (i) a unit of the good that is supplied with certainty at price p ; and (ii) a unit of the good that is supplied at a price y that is a random variable drawn from a probability distribution F. The authors show that it is optimal for the monopolist to use a distribution $F _ { 0 } \mathbf { f } \mathbf { a }$ “two-point” form; this discrete distribution assigns a probability α to a realization in which a “sale” price $p _ { 2 } { < } p _ { 1 }$ is offered, and a complementary probability $1 - \alpha \mathrm { t o } i$ a realization in which the price y is high enough so that no buyer is willing to purchase.

Weekly e-Saver™ sale events.  
(Source: usairways.com; observation period: August 19th, 2009 till November 18th, 2009).

<table><tr><td colspan="2">Survey week (#)</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><td colspan="2">Sale announcement date</td><td>19-Aug</td><td>26-Aug</td><td>2-Sep</td><td>9-Sep</td><td>16-Sep</td><td>23-Sep</td><td>30-Sep</td><td>7-Oct</td><td>14-Oct</td><td>21-Oct</td><td>28-Oct</td><td>4-Nov</td><td>11-Nov</td><td>18-Nov</td></tr><tr><td colspan="2">Departure date</td><td>22-Aug</td><td>29-Aug</td><td>5-Sep</td><td>12-Sep</td><td>19-Sep</td><td>26-Sep</td><td>3-Oct</td><td>10-Oct</td><td>17-Oct</td><td>24-Oct</td><td>31-Oct</td><td>7-Nov</td><td>14-Nov</td><td>21-Nov</td></tr><tr><td rowspan="2">Trip originating in Philadelphia</td><td>Destination city</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rochester</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td></tr><tr><td>Rochester</td><td>Philadelphia</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>N</td></tr><tr><td>Philadelphia</td><td>Syracuse</td><td>N</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td></tr><tr><td>Syracuse</td><td>Philadelphia</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td></tr><tr><td>Philadelphia</td><td>Buffalo</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td></tr><tr><td>Buffalo</td><td>Philadelphia</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>Y</td></tr></table>

In this paper, we extend the modeling framework used in Marom and Seidmann [11] by considering two products of distinct qualities that are offered by the monopolist. Buyers are risk-averse and differ in their appreciations of quality. We investigate how differences in buyers' willingness to pay and the monopolist's costs of production for each product may affect the equilibrium outcome in this case. In addition, we study the effects of different levels of buyers' risk aversion on the monopolist's optimal selling policy. Our theoretical results indicate that it can be optimal to offer the high-quality product alone in a random sale event. It can also be optimal to offer the low-quality product alone in a sale. However, the seller cannot bene<sup>fi</sup>t by offering both high and low-quality products (with positive probabilities α and β, respectively) in a sale that is held with probability smaller than one (i.e., when $\alpha + \beta < 1 )$

A substantial body of literature examines the provision of quality by a discriminating monopolist. Of particular relevance to our discussion are works by Mussa and Rosen [14], Deneckere and McAfee [6], Johnson and Myatt [8], and Anderson and Dana [1]. A basic result that follows from all of these models is that when products' quality is endogenous and buyers self-select among quality levels a discriminating monopolist will distort the provision of quality at the lower end of the quality spectrum. Interestingly, our theoretical results indicate that when buyers are risk averse the use of random “last-minute” sales can either alleviate or exacerbate such quality distortions, depending on the circumstances. Nonetheless, we show that when the degree of buyers' risk aversion exceeds a threshold a monopolist who uses “last-minute” sales can maximize its pro<sup>fi</sup>ts by offering only products of ef<sup>fi</sup>cient quality.

The remainder of the discussion is organized as follows. In Section 2 we introduce the model. In Section 2.1, we investigate optimal strategies whereby the seller offers only one product of standard quality. In Section 2.2, we study a case in which the seller offers two products but does not use randomization. In Section 2.3, we develop the optimal solution for the general case in which the seller offers two products and at the same time can use randomization. In Section 2.4 we analyze the effects of buyers' risk aversion on quality distortions in different states of the model. Section 3 includes a few concluding remarks.

## 2. Model

A monopolist sells two distinct products: a high-quality product A and a low-quality product B. The per-unit marginal production cost of product B is <sup>fi</sup>xed and normalized at zero; the per-unit marginal production cost of product A is a positive constant c.

Customers are divided into two types H and L. There are $q _ { \mathrm { H } } { > } 0$ customers of type H and $q _ { \mathrm { L } } { > } 0$ customers of type L. A type-i customer's demand (i H,L) is for one unit of product A, one unit of product B, or no product at all. The reservation values of type-H and type-L customers for a unit of product B are denoted by $V _ { \mathrm { H } }$ and $V _ { \mathrm { { L } } } ,$ respectively $( V _ { \mathrm { H } } ) 2 V _ { \mathrm { L } } )$ . The corresponding reservation values for product A are $V _ { \mathrm { H } } + \delta _ { \mathrm { H } }$ and $V _ { \mathrm { L } } + \delta _ { \mathrm { L } }$

We make the following model assumptions:

$$
\mathrm{A1)} \delta_ {\mathrm{H}} \geq \delta_ {\mathrm{L}}.
$$

$$
\text { A2) } \delta_ {\mathrm{L}} \geq c > 0.
$$

Assumption $( \mathsf { A } 1 )$ implies that buyers' willingness to pay for higher quality is positively correlated with their values for the low-quality product B. Assumption (A2) implies that it can be pro<sup>fi</sup>table to sell high-quality products to customers of type L. Thus, the high-quality product A is ef<sup>fi</sup>cient for both customer types.

Buyers care only about product and price and are completely indifferent as to the time of purchase. We let the utility function $U _ { i }$ represent the preferences of both buyer types $( i \in \mathrm { H } , \mathrm { L } ) . U _ { i }$ is de<sup>fi</sup>ned as follows:

If a type-i customer buys A: $U _ { i } = ( V _ { i } + \delta _ { i } - p _ { \mathsf { A } } ) ^ { 1 - \rho } , V _ { i } + \delta _ { i } - p _ { \mathsf { A } } \geq 0 ,$ If a type-i customer buys B: $U _ { i } = ( V _ { i } - p _ { \mathrm { { B } } } ) ^ { 1 - \rho } , V _ { i } - p _ { \mathrm { { B } } } \geq 0$ If a type-i customer buys no product at all: $U _ { i } = 0 .$

Customers of both types thus exhibit the same degree of constant relative risk aversion $\rho \left( 0 \leq \rho < 1 \right)$

Suppose that the seller initially offers the good ${ j } \left( { j } { \in } \mathsf { A } , \mathsf { B } \right)$ at price $p _ { 1 j } .$ If potential demand (and production capacity) is not totally exhausted, it pays for the seller to continue and then offer additional units at a lower price $p _ { 2 j } < p _ { 1 j } ,$ targeting potential buyers who have so far chosen not to buy at $p _ { 1 j } .$ Since buyers understand this, they anticipate the subsequent discount, and optimally wait for it. In the absence of a time limit, similar considerations apply inde<sup>fi</sup>nitely. The seller's power to attain strictly positive pro<sup>fi</sup>ts depends on the possibility of a commitment, whereby some potentially pro<sup>fi</sup>table future decisions (such as clearing all unsold inventories at a very low price at the “last-minute”) are inhibited.

With any non-degenerate pure strategy, all sales take place in the same period. Recognizing the possibility (indeed inevitability) of commitment, we consider an alternative “two-period” selling strategy that involves randomization. We assume that all buyers of both types are present in the market at the beginning of the <sup>fi</sup>rst period; there are no arrivals of new customers after this time. This assumption is reasonable, for example, in a situation in which “last-minute” deals are offered by an airline only a very short time prior to departure. In such cases, it can be argued that customers in period 1 include business-customers and tourist-customers, and that ticket prices either remain the same as before or drop.

We assume that the seller can commit to a strategy of the form

$$
S = (p _ {1 A}, p _ {1 B}, p _ {2 A}, p _ {2 B}; \alpha , \beta , \gamma),
$$

where:

$$
p _ {k j} > 0 \quad \text {   is   the   price   of   product   } j \text {   in   period   } k (k = 1, 2).
$$

$$
\left. p _ {2 \mathrm{A}}\right)
$$

0 ≤ β ≤ 1−α is the probability that product B alone is offered in period 2 (at price $p _ { 2 \mathrm { B } } )$

0 ≤ γ ≤ 1−α−β is the probability that both products are offered in period 2 (at prices $p _ { 2 \mathsf { A } }$ and $p _ { 2 \mathrm { B } } )$

In what follows, our main goal is to solve for the optimal selling strategy S.

## 2.1. Randomization with a single quality level

In this section we consider a case where only one product is offered; without loss of generality, let it be product B. In period 1, the posted price of product B (denoted by $p _ { 1 \mathrm { B } } )$ is announced. At the same time the monopolist commits that with probability β it will hold a sale in period 2 (at price $p _ { 2 \mathrm { B } } )$ . To save on notations we represent the seller's strategy S in this case by $S = ( p _ { 1 \mathrm { B } } , p _ { 2 \mathrm { B } } , \beta )$

Let S be a strategy with pro<sup>fi</sup>ts $\Pi { = } \Pi ( S )$ . If at the corresponding equilibrium both customer types purchase in the same period the seller can trivially attain or exceed Π with some strategy $S ^ { \prime }$ where $\beta = 0 .$ . It therefore suf<sup>fi</sup>ces to consider the case in which one type (i.e., H) buys in period 1 and the other buys in period 2. The seller's pro<sup>fi</sup>t-maximization problem is thus equivalent to:

$$
\underset {S} {\text { Max }} p _ {1 B} q _ {H} + \beta p _ {2 B} q _ {L}\tag{1}
$$

s.t.:

$$
V _ {H} - p _ {1 B} \geq 0.\tag{1.1}
$$

$$
V _ {H} - p _ {1 B} \geq \beta^ {\frac {1}{1 - \rho}} (V _ {H} - p _ {2 B}).\tag{1.2}
$$

$$
V _ {L} - p _ {2 B} \geq 0.\tag{1.3}
$$

$$
\beta^ {\frac {1}{1 - \rho}} (V _ {L} - p _ {2 B}) \geq V _ {L} - p _ {1 B}.
$$

$$
\beta \in [ 0, 1 ].\tag{1.4}
$$

<sub>ð</sub>1:5<sub>Þ</sub>

Conditions (1.1) and (1.3) are individual-rationality constraints for type H and type L customers, respectively. Condition (1.1), for example, means that a type-H customer prefers purchasing product B at price $p _ { 1 \mathtt { B } }$ to purchasing no product at all. Conditions (1.2) and (1.4) are incentive-compatibility constraints for the two customer types. Condition (1.2) implies that a type-H customer prefers purchasing product B in period 1 to waiting until period 2. Condition (1.4) implies that the opposite holds true for a type-L customer.

Since

$$
V _ {H} - p _ {1 B} \geq \beta^ {\frac {1}{1 - \rho}} (V _ {H} - p _ {2 B}) \geq \beta^ {\frac {1}{1 - \rho}} (V _ {L} - p _ {2 B}) \geq 0, \beta \in [ 0, 1 ].\tag{2}
$$

Condition (1.1) is automatically satis<sup>fi</sup>ed by Conditions (1.2) and (1.3) and can be omitted. Note that whenever Condition (1.2) is not binding the seller can raise $p _ { 1 B }$ without affecting the remaining two constraints (1.3) and (1.5) and thus improve the maximand. Condition (1.2) therefore must be binding in any equilibrium. As a result, it is always optimal to set

$$
p _ {1 B} ^ {*} = V _ {H} - \beta^ {\frac {1}{1 - \rho}} (V _ {H} - p _ {2 B}) \leq V _ {H}, \beta \in [ 0, 1 ].\tag{3}
$$

Whenever Condition (1.2) is binding, Condition (1.4) is automatically satis<sup>fi</sup>ed and thus can be ignored. Because the seller can exclude type-L customers by setting $\beta = 0$ and $p _ { 1 B } { > } V _ { \mathrm { I } }$ we restrict our attention to strategies S with $p _ { 2 B } = V _ { L }$ without any loss of optimality. The seller's optimization problem is thus equivalent to

$$
\underset {\beta \in [ 0, 1 ]} {\text { Max }} \pi (\beta) = \Big (V _ {H} - \beta^ {\frac {1}{1 - \rho}} (V _ {H} - V _ {L}) \Big) q _ {H} + \beta V _ {L} q _ {L}.\tag{4}
$$

■ Under what circumstances should the monopolist use randomization (i.e. set $\beta$ in the interior), and how?

We <sup>fi</sup>rst observe that setting $\beta = 0$ is never optimal. This holds true because $\pi ( \beta )$ is a continuously differentiable function, whereas at the point $\beta = 0$ we have

$$
\pi^ {\prime} (0) = V _ {L} q _ {L} > 0.\tag{5}
$$

Hence, whenever using randomization is not pro<sup>fi</sup>table, the seller will set $\beta = 1$ . The following lemma shows that using a randomized selling strategy is optimal if and only if buyers' risk aversion (ρ) exceeds a threshold value.

Lemma 1. Setting $p _ { 1 B } { > } V _ { L } , p _ { 2 B } { = } V _ { L } ,$ , and $0 < \beta < 1$ is optimal if and only if:

$$
\rho > 1 - \frac {V _ {H} - V _ {L}}{V _ {L}} \cdot \frac {q _ {H}}{q _ {L}}.
$$

All proofs in this paper are contained in Appendix A.

It is indeed an intuitive result that an increased degree of differentiation between the two types (i.e., a higher ratio $\big ( V _ { \mathrm { H } } - V _ { \mathrm { L } } \big ) / V _ { \mathrm { L } } \big )$ facilitates pro<sup>fi</sup>table price-discrimination (in this model the monopolist can sell the same product at two different prices only if it uses randomization). In addition, Lemma 1 shows that a higher proportion of type-H customers $( \mathrm { i . e . , } \mathsf { a }$ higher ratio $q _ { \mathrm { H } } / q _ { \mathrm { L } } )$ necessarily results in the same effect. We explain the latter result as follows. By setting a probability β that is (strictly) smaller than 1, the seller can charge a higher price $\left( p _ { 1 A } > p _ { 2 B } \right)$ for each unit of the quantity sold in period 1 (i.e., q<sub>H</sub>). At the same time, however, the seller forgoes potential revenues of $( 1 - \beta ) p _ { 2 \mathrm { B } } q _ { \mathrm { L } }$ in period 2. A higher ratio $q _ { \mathrm { H } } / q _ { \mathrm { I } }$ results in a higher relative magnitude of the positive effect on pro<sup>fi</sup>ts (in period 1) as compared to the negative effect (in period 2); thus, the seller's motivation to segment the market is increased.

Whenever the condition of Lemma 1 is satis<sup>fi</sup>ed, the optimal point $S ^ { * }$ involves:

$$
p _ {1 \mathrm{B}} ^ {*} = V _ {\mathrm{H}} - \beta^ {\frac {1}{1 - \rho}} (V _ {\mathrm{H}} - V _ {\mathrm{L}}), p _ {2 \mathrm{B}} ^ {*} = V _ {\mathrm{L}}.\tag{6}
$$

$$
\beta^ {*} = \left(\frac {1}{1 - \rho} \cdot \frac {V _ {\mathrm{H}} - V _ {\mathrm{L}}}{V _ {\mathrm{L}}} \cdot \frac {q _ {\mathrm{H}}}{q _ {\mathrm{L}}}\right) ^ {\frac {\rho - 1}{\rho}} <   1, \quad V _ {\mathrm{H}} \geq V _ {\mathrm{L}} \geq 0, \quad 0 <   \rho \leq 1.\tag{7}
$$

The above expression for the optimal probability of sale $\beta ^ { * }$ is an increasing function of risk-aversion $^ 2 ( \rho )$ and a decreasing function of both ratios $q _ { \mathrm { H } } / q _ { \mathrm { I } }$ <sub>L</sub> and $( V _ { \mathrm { H } } - V _ { \mathrm { L } } ) / V _ { \mathrm { L } }$ . We explain these results as follows.

When the ratio $( V _ { \mathrm { H } } - V _ { \mathrm { L } } ) / V _ { \mathrm { L } }$ increases, a type-H customer observes a period 2 price $\left( p _ { 2 \mathrm { B } } ^ { \mathrm { ~ * ~ } } = V _ { \mathrm { L } } \right)$ that is lower as compared to his own value $( V _ { \mathrm { H } } )$ . As a result, he has a greater incentive to defer his purchase to period 2. The seller's best response in this case is to reduce the probability $\beta$ to a level such that type-H customers remain indifferent between making early and late purchases.

Let $\beta$ be <sup>fi</sup>xed at some value between 0 and 1. When the ratio $q _ { \mathrm { H } } / q _ { \mathrm { L } }$ increases, a greater advantage arises to the seller from incrementally increasing the price $p _ { 1 \mathsf { A } }$ while simultaneously reducing the probability β such that type-H customers remain indifferent. Accordingly, we <sup>fi</sup>nd that the optimal probability $\boldsymbol { \beta ^ { * } }$ is a decreasing function of the ratio $q _ { \mathrm { H } } / q _ { \mathrm { L } }$

Finally, we note that whenever the condition of Lemma 1 is not satis<sup>fi</sup>ed, any strategy that results in selling B at a price $V _ { \mathrm { { L } } }$ to both types with probability 1 (e.g., setting $p _ { 1 } = p _ { 2 } = V _ { \mathrm { { L } } }$ and $\beta = 1 )$ is optimal.

## 2.2. Two quality levels and no randomization

In this part of the analysis we consider the problem of a seller who offers two distinct products but does not use randomization. For convenience, let us assume that all sales take place in period 1. To save on notations we represent the seller's strategy S in this case by $S { = } \left( p _ { \mathrm { { A } } } , p _ { \mathrm { { B } } } \right)$

Obviously, it suf<sup>fi</sup>ces for the seller to consider only the following three strategies:

S —(“Sell product A to type H and product B to type L”): $p _ { \mathrm { { A } } } = V _ { \mathrm { { L } } } + \delta _ { \mathrm { { H } } }$ $p _ { \mathrm { B } } { = } V _ { \mathrm { L } }$

S —(“Sell product A to both types H and $\mathrm { L } ^ { \ " } ) \colon p _ { \mathsf { A } } = V _ { \mathrm { L } } + \delta _ { \mathrm { L } } , p _ { \mathsf { B } } > V _ { \mathsf { H } } .$ S —(“Sell product A to type H and no product to type $\mathrm { L } ^ { \prime } ) \colon p _ { \mathsf { A } } = V _ { \mathrm { H } } + \delta _ { \mathrm { H } }$ $p _ { \mathrm { B } } { > } V _ { \mathrm { H } } .$

Let π<sub>i</sub> represent the equilibrium pro<sup>fi</sup>t from strategy $S _ { i } , ( i \in \mathrm { I } , \mathrm { I I } , \mathrm { I I I } )$ . We have:

$\pi _ { \mathrm { I I I } } { \geq } \pi _ { \mathrm { I I } }$ if and only if $V _ { \mathrm { H } } + \ S _ { \mathrm { H } } { \geq } \frac { q _ { \mathrm { H } } + q _ { \mathrm { L } } } { q _ { \mathrm { H } } } ( V _ { \mathrm { L } } + \ S _ { \mathrm { L } } ) { - } \frac { q _ { \mathrm { L } } } { q _ { \mathrm { H } } } c .$ $\pi _ { \mathrm { I I I } } { \geq } \pi _ { \mathrm { I } }$ if and only if $V _ { \mathrm { H } } { \geq } \frac { q _ { \mathrm { H } } + q _ { \mathrm { L } } } { a _ { \mathrm { H } } } V _ { \mathrm { L } } .$ $\pi _ { \mathrm { I I } } { \geq } \pi _ { \mathrm { I } }$ if and only if $\mathrm { \bar { \Phi } } _ { \mathrm { \hat { H } } } \mathrm { \leq } \frac { q _ { \mathrm { H } } + q _ { \mathrm { L } } } { q _ { \mathrm { H } } } \delta _ { \mathrm { L } } - \frac { q _ { \mathrm { L } } } { q _ { \mathrm { H } } } c .$

## 2.3. Two quality levels and randomization

We study optimal selling strategies that involve both vertical differentiation and randomized selling. This part of the analysis addresses the main research questions of the paper. We discuss when it is optimal for the seller to offer the low-quality product B alone in a “last-minute” sale. We show the different conditions under which it is optimal to offer the high-quality product A alone and, <sup>fi</sup>nally, also show when it is optimal offer both products A and B with positive probabilities in a sale.

The seller's strategy space in this general case is spun by all well de<sup>fi</sup>ned<sup>3</sup> strategies of the form,

$$
S = (p _ {1 \mathrm{A}}, p _ {1 \mathrm{B}}, p _ {2 \mathrm{A}}, p _ {2 \mathrm{B}}; \alpha , \beta , \gamma).
$$

The model yields the following results:

Lemma 2. Without loss of optimality, the seller can restrict herself to strategies that induce customers of type H to buy product A in period 1, and customers of type L to buy either product A or product B in period 2.

Corollary. There is always an optimal strategy with $p _ { 1 \mathrm { B } } { > } V _ { \mathrm { H } } , p _ { 2 \mathrm { A } } { = } V _ { \mathrm { L } } + \delta _ { \mathrm { L } }$ and $p _ { 2 \mathrm { B } } = V _ { \mathrm { L } }$ .

Lemma 3. Without loss of optimality, the seller can restrict herself to strategies with $\gamma = 0 .$

Theorem 1. In equilibrium, customers of type H buy product A with certainty and customers of type L buy either product A or product B with non-zero probability.

Theorem 1's assertion does not generally hold true when the seller is restricted to pure strategies (see Section 2.2). Thus, this result indicates that a monopolist who uses randomization excludes fewer buyers entirely from consumption. The next theorem contains our main result.

Theorem 2. Without loss of optimality, the seller can restrict herself to strategies with either $\alpha = 0 , \beta = 0 , o r 1 - \alpha - \beta = 0$

Simply put, the monopolist cannot increase its pro<sup>fi</sup>ts by offering more than one product with positive probability in a random (i.e., $\alpha + \beta { < } 1 )$ sale event.

With these results in hand, we proceed to show a solution to the seller's pro<sup>fi</sup>t-maximization problem. Following Theorem $^ { 2 , }$ we restrict our attention to strategies $S = ( p _ { 1 \mathrm { A } } , p _ { 1 \mathrm { B } } , p _ { 2 \mathrm { A } } , p _ { 2 \mathrm { B } } ; \alpha , \beta , \gamma )$ (with $p _ { 1 \mathrm { B } } { > } V _ { \mathrm { H } } , \ p _ { 2 \mathrm { A } } { = } V _ { \mathrm { L } } + \delta _ { \mathrm { L } } , \ p _ { 2 \mathrm { B } } { = } V _ { \mathrm { L } } ,$ and $\gamma = 0 )$ that correspond to one (or more) of the following three cases.

Case I: At the optimum $\alpha = 0$

In this case the seller optimally commits in advance not to sell product A in period 2. For notational convenience, we let the abbreviated<sup>4</sup> form $s _ { 1 } = ( _ { 1 } p _ { 1 A } , _ { 1 } p _ { 2 B } , _ { 1 } \beta )$ describe an optimal strategy in this case. The corresponding equilibrium pro<sup>fi</sup>t is

$$
\pi_ {1} = (_ {1} p _ {1 \mathrm{A}} - c) q _ {\mathrm{H}} + _ {1} \beta V _ {\mathrm{L}} q _ {\mathrm{L}}.\tag{8}
$$

Whereas $\pi _ { 1 }$ exceeds π $( \mathrm { i } . { \mathsf { e } } . , 0 < _ { 1 } \beta { < } 1 )$ if and only if

$$
\rho > 1 - \frac {V _ {\mathrm{H}} - V _ {\mathrm{L}}}{V _ {\mathrm{L}}} \cdot \frac {q _ {\mathrm{H}}}{q _ {\mathrm{L}}}, 0 <   \rho <   1.\tag{9}
$$

Surprisingly, Condition (9) is identical to Lemma 1's condition. That ${ \mathrm { i } } s ,$ we <sup>fi</sup>nd that the optimality of the use of randomization in this case is completely independent of the attributes of product A (because Condition (9) does not depend on either $\delta _ { \mathrm { H } }$ or $\delta _ { \mathrm { L } } )$

Whenever Condition (9) is satis<sup>fi</sup>ed, we have

$$
{ } _ { 1 } \beta = \left( \frac { 1 } { 1 - \rho } \cdot \frac { V _ { \mathrm{H} } - V _ { \mathrm{L} } } { V _ { \mathrm{L} } } \cdot \frac { q _ { \mathrm{H} } } { q _ { \mathrm{L} } } \right) ^ { \frac { \rho - 1 } { \rho } } <   1 , 0 <   \rho <   1 .\tag{10}
$$

$$
{ } _ { 1 } p _ { 1 \mathrm{A} } = V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - _ { 1 } \beta ^ { \frac { 1 } { 1 - \rho } } ( V _ { \mathrm{H} } - _ { 1 } p _ { 2 \mathrm{B} } ) ; \quad { } _ { 1 } p _ { 2 \mathrm{B} } = V _ { \mathrm{L} } .\tag{11}
$$

The optimal probability $_ { 1 } \beta$ is identical to what is described by Eq. (7). In particular, it is an increasing function of risk-aversion (ρ) and a decreasing function of both ratios $q _ { \mathrm { H } } / q _ { \mathrm { I } }$ and $( V _ { \mathrm { H } } - V _ { \mathrm { L } } ) / V _ { \mathrm { L } }$

If Condition (9) is not satis<sup>fi</sup>ed, then strategy $S _ { \mathrm { I } }$ (see Section 2.2) is optimal.

Case II: At the optimum $\beta = 0$

In this case the seller optimally commits in advance not to sell product B in period 2. Let $s _ { 2 } = ( _ { 2 } p _ { 1 \mathrm { A } } , _ { 2 } p _ { 2 \mathrm { A } } , _ { 2 } \alpha )$ be an optimal strategy in this case. The corresponding equilibrium pro<sup>fi</sup>t is

$$
\pi_ {2} = _ {2} p _ {1 \mathrm{A}} q _ {\mathrm{H}} + _ {2} \alpha (V _ {\mathrm{L}} + \delta_ {\mathrm{L}}) q _ {\mathrm{L}} - (q _ {\mathrm{H}} + _ {2} \alpha q _ {\mathrm{L}}) c.\tag{12}
$$

We <sup>fi</sup>nd that $\pi _ { 2 } { > } \pi _ { \mathrm { I I } } ( \mathrm { i . e . , } 0 { < } _ { 2 } \alpha { < } 1 )$ if and only if buyers are suf<sup>fi</sup>ciently risk averse:

$$
\rho > 1 - \frac {V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}}{V _ {\mathrm{L}} + \delta_ {\mathrm{L}} - c} \cdot \frac {q _ {\mathrm{H}}}{q _ {\mathrm{L}}}, 0 <   \rho <   1.\tag{13}
$$

Whenever Condition (13) is satis<sup>fi</sup>ed we have

$$
{ } _ { 2 } \alpha = \left( \frac { 1 } { 1 - \rho } \cdot \frac { V _ { \mathrm{H} } - V _ { \mathrm{L} } + \delta _ { \mathrm{H} } - \delta _ { \mathrm{L} } } { V _ { \mathrm{L} } + \delta _ { \mathrm{L} } - c } \cdot \frac { q _ { \mathrm{H} } } { q _ { \mathrm{L} } } \right) ^ { \frac { \rho - 1 } { \rho } } <   1 , 0 <   \rho <   1 .\tag{14}
$$

$$
{ } _ { 2 } p _ { 1 \mathrm{A} } = V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - _ { 2 } \alpha ^ { \frac { 1 } { 1 - \rho } } ( V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - _ { 2 } p _ { 2 \mathrm{A} } ) ; \quad { } _ { 2 } p _ { 2 \mathrm{A} } = V _ { \mathrm{L} } + \delta _ { \mathrm{L} } .\tag{15}
$$

As in the previous case (see Eq. (10)), the optimal probability of sale $_ { 2 \alpha }$ is an increasing function of risk-aversion $( \rho )$ as well as a decreasing function of the ratios $q _ { \mathrm { H } } / q _ { \mathrm { L } }$ and $( V _ { \mathrm { H } } - V _ { \mathrm { L } } ) / V _ { \mathrm { L } }$

If Condition (13) is not satis<sup>fi</sup>ed, then strategy S is optimal.

■ Should the seller offer product A or product B in a random sale event (i.e., when at the optimum α+βb1)?

We <sup>fi</sup>nd that $\pi _ { 2 } { > } \pi _ { 1 }$ holds true if and only $\mathrm { i f } , ^ { 5 }$

$$
\left(\frac {V _ {\mathrm{H}} - V _ {\mathrm{L}}}{V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}}\right) ^ {1 - \rho} \geq \frac {V _ {\mathrm{L}}}{V _ {\mathrm{L}} + \delta_ {\mathrm{L}} - c}, 0 \leq \rho \leq 1.\tag{16}
$$

Thus we $\mathrm { { \ f i n d ^ { 6 } } }$ that an incremental increase in risk-aversion (ρ) in<sup>fl</sup>uences the seller to offer product A alone rather than product B alone in a period-2 random sale event. Surprisingly, Condition (16) does not depend on the quantities $q _ { \mathrm { H } }$ and $q _ { \mathrm { L } }$ . This result implies, for example, that an increase in the relative number of type-L buyers does not necessarily in<sup>fl</sup>uence the seller to offer the high-quality product A to them. Quite expectedly,<sup>7</sup> Condition (16) implies that a greater difference between the two types' valuations of product B $\left( V _ { \mathrm { H } } - V _ { \mathrm { L } } \right)$ increases the seller's motivation to offer product A in period 2, whereas a greater difference in their valuation of product $\textsf { A } ( V _ { \mathrm { H } } - V _ { \mathrm { L } } + \delta _ { \mathrm { H } } - \delta _ { \mathrm { L } } )$ in<sup>fl</sup>uences the <sup>fi</sup>rm to offer product B in period 2.

## Case III: At the optimum $1 - \alpha - \beta = 0$

In this case, the seller holds a sale in period 2 with certainty but may randomly offer different products in the sale. Let $\begin{array} { r } { s _ { 3 } = ( _ { 3 } p _ { 1 \mathrm { A } } , 3 p _ { 2 \mathrm { A } } , } \end{array}$ p ; α, β) be an optimal strategy in this case. The corresponding equilibrium pro<sup>fi</sup>t is

$$
\pi_ {3} = _ {3} p _ {1 A} q _ {H} + (_ {3} \alpha_ {3} p _ {2 A} + _ {3} \beta_ {3} p _ {2 B}) q _ {L} - (q _ {H} + _ {3} \alpha q _ {L}) c.\tag{17}
$$

For all $0 { < } \rho { < } 1$ , de<sup>fi</sup>ne

$$
\omega (\rho) = \left(\frac {q _ {\mathrm{H}}}{q _ {\mathrm{L}}} \cdot \frac {1}{1 - \rho} \cdot \frac {(V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} - (V _ {\mathrm{H}} - V _ {\mathrm{L}}) ^ {1 - \rho}}{\delta_ {\mathrm{L}} - c}\right) ^ {- \frac {1}{\rho}}.\tag{18}
$$

We <sup>fi</sup>nd that $\pi _ { 3 } \mathrm { > m a x } \{ \pi _ { \mathrm { I } } , \pi _ { \mathrm { I I } } \} ( \mathrm { i . e . , } 0 < _ { 3 } \alpha ^ { \cdot } { _ 3 } \beta < 1 )$ if and only if

$$
V _ {\mathrm{H}} - V _ {\mathrm{L}} <   \omega (\rho) <   V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}, 0 <   \rho <   1.\tag{19}
$$

Whenever Condition (19) is satis<sup>fi</sup>ed, the optimal strategy s<sub>3</sub> entails:

$$
{ } _ { 3 } \alpha = \left( \frac { ( \omega ( \rho ) ) ^ { 1 - \rho } - ( V _ { \mathrm{H} } - V _ { \mathrm{L} } ) ^ { 1 - \rho } } { ( V _ { \mathrm{H} } - V _ { \mathrm{L} } + \delta _ { \mathrm{H} } - \delta _ { \mathrm{L} } ) ^ { 1 - \rho } - ( V _ { \mathrm{H} } - V _ { \mathrm{L} } ) ^ { 1 - \rho } } \cdot \frac { q _ { \mathrm{H} } } { q _ { \mathrm{L} } } \right) ^ { \frac { \rho - 1 } { \rho } } <   1 , 0 <   \rho <   1 .\tag{20}
$$

$$
{ } _ { 3 } \beta = 1 - _ { 3 } \alpha <   1 .\tag{21}
$$

$$
{ } _ { 3 } p _ { 1 \mathrm{A} } = V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - \left( { } _ { 3 } \alpha ( V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - { } _ { 3 } p _ { 2 \mathrm{A} } ) ^ { 1 - \rho } + { } _ { 3 } \beta ( V _ { \mathrm{H} } - { } _ { 3 } p _ { 2 \mathrm{B} } ) ^ { 1 - \rho } \right) ^ { \frac { 1 } { 1 - \rho } } .\tag{22}
$$

$$
{ } _ { 3 } p _ { 2 \mathrm{A} } = V _ { \mathrm{L} } + \delta _ { \mathrm{L} } , \quad { } _ { 3 } P _ { 2 \mathrm{B} } = V _ { \mathrm{L} } .\tag{23}
$$

We note that in this case the optimal probabilities $_ { 3 } \alpha$ and $_ { 3 } \beta$ are (while everywhere continuous) not necessarily monotone functions of buyers' risk-aversion $( \rho )$

If Condition (19) is not satis<sup>fi</sup>ed, then either strategy S is optimal or strategy $S _ { \mathrm { I I } }$ is optimal (see Section 2.2).

It remains to show the alternative conditions under which the optimal selling strategy falls under Cases I, II, or III. We proceed to investigate these conditions now.

In order to determine the optimal selling strategy, we <sup>fi</sup>rst compare the equilibrium pro<sup>fi</sup>ts that correspond to the following 5 strategies (see Lemma 1).

Table 2  
Relevant selling-strategy alternatives.

<table><tr><td>Selling strategy</td><td>Description</td></tr><tr><td> $s_1$ </td><td>Offer product A in period 1 and randomly offer product B in period 2</td></tr><tr><td> $s_2$ </td><td>Offer product A in period 1 and randomly offer product A in period 2</td></tr><tr><td> $s_3$ </td><td>Offer product A in period 1 and randomly offer product A or product B in period 2</td></tr><tr><td> $s_I$ </td><td>Offer product A with certainty in period 1 and product B with certainty in period 2</td></tr><tr><td> $s_{II}$ </td><td>Offer product A with certainty in both periods 1 and 2</td></tr></table>

Table 3  
Comparisons of strategy alternatives' pro<sup>fi</sup>tability.

<table><tr><td></td><td>Relationship</td><td>Condition</td><td>References</td></tr><tr><td>1</td><td> $\pi_1 > \pi_2$ </td><td> $\left( \frac{V_H - V_L}{V_H - V_L + \delta_H - \delta_L} \right)^{1-\rho} < \frac{V_L}{V_L + \delta_L - c}$ </td><td>Eq. (16)</td></tr><tr><td>2</td><td> $\pi_1 > \pi_3$ </td><td>N/A*</td><td></td></tr><tr><td>3</td><td> $\pi_1 > \pi_{\text{II}}$ </td><td>N/A*</td><td></td></tr><tr><td>4</td><td> $\pi_1 > \pi_I$ </td><td> $\rho > 1 - \frac{V_H - V_L}{V_L} \cdot \frac{q_H}{q_L}$ </td><td>Eq. (9)</td></tr><tr><td>5</td><td> $\pi_2 > \pi_3$ </td><td>N/A*</td><td></td></tr><tr><td>6</td><td> $\pi_2 > \pi_{\text{II}}$ </td><td> $\rho > 1 - \frac{V_H - V_L + \delta_H - \delta_L}{V_L + \delta_L - c} \cdot \frac{q_H}{q_L}$ </td><td>Eq. (13)</td></tr><tr><td>7</td><td> $\pi_2 > \pi_I$ </td><td>N/A*</td><td></td></tr><tr><td>8</td><td> $\pi_3 > \pi_{\text{II}}$ </td><td> $\omega(\rho) < V_H - V_L + \delta_H - \delta_L$ </td><td>Eq. (19)</td></tr><tr><td>9</td><td> $\pi_3 > \pi_I$ </td><td> $\omega(\rho) > V_H - V_L$ </td><td>Eq. (19)</td></tr><tr><td>10</td><td> $\pi_{\text{II}} > \pi_I$ </td><td> $\delta_H \leq \frac{q_H + q_L}{q_H} \delta_L - \frac{q_L}{q_H} c.$ </td><td>Section 2.2</td></tr></table>

\* A simple condition was not found.

Table 3 summarizes the conditions used in order to compare different pairs of strategies in terms of the seller's equilibrium pro<sup>fi</sup>ts.

Finally, for any given set of model parameters the set of conditions above enables us to <sup>fi</sup>nd an optimal selling strategy. We use this framework in order to investigate how changes in buyers' values for products A and B affect the seller's optimal selection among the <sup>fi</sup>ve strategy alternatives listed in Table 2. Fig. 2 depicts optimal strategy categories for various pairs of the parameters $V _ { \mathrm { H } }$ and $\delta _ { \mathrm { H } }$ when the values of the remaining model parameters $( V _ { \mathrm { L } } , \delta _ { \mathrm { L } } , c _ { \mathrm { \ell } }$ , and ρ) are held <sup>fi</sup>xed. As the <sup>fi</sup>gure shows, when the differences $\Delta _ { \mathrm { V } } = V _ { \mathrm { H } } - V _ { \mathrm { L } }$ and $\Delta _ { \mathrm { D } } { = } \delta _ { \mathrm { H } } { - } \delta _ { \mathrm { L } }$ are both relatively small it is optimal for the seller to offer product A with certainty in both periods 1 and 2. When both differences are relatively large, we <sup>fi</sup>nd that it is optimal to offer product A in period 1 with certainty and then randomly offer product A with some probability in period 2. When the difference $\Delta _ { \mathrm { D } }$ is relatively large but the difference $\Delta _ { \mathsf { V } }$ is relatively small, it is optimal to offer product A (with certainty) in period 1 and product B (either with certainty, or randomly) in period 2. In similar circumstances, we <sup>fi</sup>nd that (as part of strategy s ) it can also be optimal to randomly offer either product A alone or product B alone in period 2. In line with prior price-discrimination studies, therefore, our model indicates that a discriminating monopolist will offer only products of ef<sup>fi</sup>cient quality (in this case, product A) whenever the premium that the high-type buyers are willing to pay for higher quality is not significantly higher than the corresponding premium for the lowtype buyers. The reason is that under this condition the threat of consumption of a lower quality product (e.g., traveling in economy-class rather than in business-class) serves as a weaker deterrent for purchase deferrals (for high-type customers) as compared to the threat of complete product unavailability $( \mathrm { e . g . }$ , not being able to travel at all). It is worth emphasizing that randomized selling strategies thus can allow the seller to offer high quality products to low-type consumers at moderate prices.

![](/api/attachments/X9E5UYG2/fulltext/images/7deade63e102f796a988168b4beb66c3a6992602961cd1a6da25f79bfea07d5f.jpg)  
Fig. 2. Optimal selling strategies as functions of type-H customers values $V _ { \mathrm { H } }$ and $\delta _ { \mathrm { H } }$ $( V _ { \mathrm { L } } { = } 1 , \delta _ { \mathrm { L } } { = } 1 , c { = } 0 . 5 , \rho { = } 0 . 5 )$

## 2.4. The effects of buyers' risk-aversion on product-line efficiency

We analyze two speci<sup>fi</sup>c scenarios in order to argue that an increase in buyers' risk-aversion $( \rho )$ can lead either to an increase or to a decrease in the extent of quality distortions by a discriminating monopolist.

## Case I: Greater risk-aversion has a moderating effect on quality distortions

Using the framework developed in Section 2.3, we consider a scenario with the following parameters: $V _ { \mathrm { H } } { = } 1 . 1 ; \delta _ { \mathrm { H } } { = } 3 ; V _ { \mathrm { L } } { = } 1 ; \delta _ { \mathrm { L } } { = } 1$ and $c = 0 . 5 .$ We also let $q _ { \mathrm { H } } { = } q _ { \mathrm { L } } { = } q \left( q { > } 0 \right)$ .

If buyers are uniformly risk neutral $( \rho { = } 0 )$ , then it is optimal to sell product A to type-H buyers in period 1 (at price $p _ { 1 \mathrm { A } } = 4 )$ and product B with certainty $( \beta = 1 )$ to type-L buyers in period $2 \left( \mathrm { a t p r i c e } p _ { 2 \mathrm { B } } { = } 1 \right)$ This strategy yields the seller pro<sup>fi</sup>ts of $\tau { = } 4 . 5 ,$

Suppose now that ceteris paribus $\rho { = } 0 . 8 5 \ ( \mathrm { i . e . }$ ., buyers are highly risk averse). In this case, it is optimal to sell product A to type-H buyers in period 1 at price $p _ { 1 A } = 3 . 9 6 4 .$ . In period 2, the monopolist randomizes its strategy as follows. With probability $\alpha { = } 0 . 0 8 1$ , it sells product A to type-L buyers at price $p _ { 2 \mathsf { A } } = 2$ . With the complementary probability $\beta = 1 - \alpha = 0 . 9 1 9 ,$ , it sells product B to type-L buyers at price $p _ { 2 \mathrm { B } } = 1$ . This strategy yields the seller pro<sup>fi</sup>ts of $\pi { = } 4 . 5 0 5$

We observe that in this case a higher level of risk-aversion on the part of buyers in<sup>fl</sup>uences the monopolist to reduce quality distortions by offering the ef<sup>fi</sup>cient product A with some likelihood in period 2. Interestingly, in this case a higher value of $\rho$ also results in a Pareto improvement due to the simultaneous decrease in the price $p _ { 1 \mathrm { A } } .$

## Case II: Greater risk-aversion exacerbates quality distortions

We consider the following model settings: $V _ { \mathrm { H } } = 1 . 0 3 ; \delta _ { \mathrm { H } } = 1 . 4 5$

$$
V _ {\mathrm{L}} = 1, \delta_ {\mathrm{L}} = 1, c = 0. 5, \text {   and   } q _ {\mathrm{H}} = q _ {\mathrm{L}} = q (q > 0).
$$

If buyers are uniformly risk neutral $( \rho { = } 0 )$ , then it is optimal to sell the high-quality product A to both types of buyers at price $p _ { 1 \mathrm { A } } = 2 $ . The seller's resulting pro<sup>fi</sup>t is then $\pi = 3$

If buyers are risk averse, with $\rho { = } 0 . 8 5$ , then it is optimal to sell product A to type-H buyers in period 1 (at price $p _ { 1 A } { = } 2 . 2 8 7 )$ ). In period 2 the monopolist sells product A to type-L buyers (at price $p _ { 2 \mathrm { A } } = 2 \cdot$ )with probability $\alpha { = } 0 . 6 2 2$ , and product B (at price $p _ { 2 \mathrm { B } } = 1 )$ with a complementary probability $\beta = 1 - \alpha = 0 . 3 7 8$ . The seller's resulting pro<sup>fi</sup>t is then $\pi { = } 3 . 0 9 9$

In this case, therefore, the monopolist will distort the provision of quality by introducing the product B only if buyers are risk averse.

## 3. Concluding remarks

On the Internet, sellers face well-informed and sophisticated buyers who time their purchases strategically. As a result, online sellers such as US Airways have devised novel pricing policies in order to induce highvalued buyers to purchase early. One possible mean of discouraging strategic deferrals of purchases is the use of an up-front commitment to limit the frequency of clearance sales. As we have seen, a revenue manager for an airline can decide, for instance, to refrain from offering <sup>fl</sup>ights on the same route in subsequent weekly clearance sale events. Such a policy, however, can prove ineffective when customers become aware of it and update their expectations accordingly. Our paper therefore advocates the use of deliberately randomized selling strategies by a seller who aims to induce early purchases.

By randomizing the offering of $" \mathrm { l a s t - m i n u t e } "$ deals the monopolist can increase its total pro<sup>fi</sup>ts in both periods (1 and 2), even though it cannot get the highest possible pro<sup>fi</sup>t in period 2. Such a randomized strategy thus requires the <sup>fi</sup>rm's strong commitment to consumers. In practice, a seller can make such a commitment by consistently following the same (or similar) pricing patterns over time. As an illustration of this, our data shows that US Airways did not rely only on <sup>fl</sup>uctuating demand when it chose when to discount. Rather, the airline followed a predetermined (and highly non-orthodox) clearance-sales strategy that entailed holding sales in certain cyclical and highly predictable patterns. Following such cyclical patterns constitutes, in effect, a commitment from the viewpoint of well-informed buyers. Similarly, a seller can commit to hold a “sale” in a non-cyclical pattern but with a prede<sup>fi</sup>ned probability. In real market settings, such a policy can be closely mimicked by imposing a cap on the frequency of “last-minute” promotions (e.g., in lieu of a commitment not to hold sales on two consecutive weekends, a seller can commit not to offer discounts more than 50% of the time). The use of such a commitment can readily prove viable because sophisticated travelers can nowadays assess the likelihood of “last-minute” fare-sales quite accurately by using websites such as bing.com that offer predictions on when is the best time to purchase airline tickets

We extend the risk-based segmentation model of Marom and Seidmann [11] by considering two products instead of one. Although the two models take different approaches and largely deal with separate issues, the main conclusions that arise from them are similar. Marom and Seidmann [11] argue that when the monopolist's available capacity is suf<sup>fi</sup>ciently high it has a unique optimal strategy that involves <sup>fi</sup>xing both prices $p _ { 1 }$ and $p _ { 2 }$ and holding a “sale” with probability α smaller than one. In this paper, we show that it is always optimal for the seller to commit to selling but a single product (either A or B) in a random sale event (that is held with probability smaller than one). Put together, the two models indicate that the monopolist cannot bene<sup>fi</sup>t by offering a non-degenerate joint-distribution of qualities and prices in a random sale event.

The characterization of pro<sup>fi</sup>t-maximizing policies that involve randomization proved a fairly complicated matter even within the simpli<sup>fi</sup>ed framework used, and it undoubtedly constitutes a signi<sup>fi</sup>cant challenge in real market settings. The dynamic nature and rapid growth of new electronic markets underscore the importance of a better understanding of related issues and warrant the development of further theoretical foundations.

We have shown how different demand characteristics (such as buyers' risk-aversion and willingness to pay for higher quality) in<sup>fl</sup>uence the monopolist's pro<sup>fi</sup>t-maximizing selling policy. One of the main contributions of our work is in arguing the conditions under which the use of a randomized selling strategy can be pro<sup>fi</sup>table. We have shown, for example, that when buyers belong to two distinct types (“high” and $" \mathrm { l o w " } )$ and select between two products of differing quality, a higher difference in the two types' willingness to pay for either product in<sup>fl</sup>uences the monopolist to randomize its strategy. In addition, a nonintuitive managerial implication that arises from the analysis is that a monopoly seller optimally should offer random “last-minute” promotions when there are relatively few “low-budget” customers present in the markets.

In our opening remarks we asked whether airlines can bene<sup>fi</sup>t by offering special last-minute promotions for travel in business-class. The results of our theoretical investigation demonstrate that when buyers are highly risk averse it can indeed be optimal for a monopoly seller to offer high-quality products (such as business-class tickets) in “lastminute” sales. Interestingly, the sale of high-end products through a randomized mechanism can assume one of two optimal forms. The <sup>fi</sup>rst form is a random “sale” event in which the high-quality product alone is offered. The second form is essentially a sequential transaction in which the seller <sup>fi</sup>rst guarantees the supply of a basic-quality product and then randomly offers an upgrade opportunity (for a fee) at a later time. This result helps to explain, for instance, why airlines often offer upgrades to their loyal customers only a short time before departure.

One limitation of our model is that it assumes that demand is deterministic. In real market settings, however, clearance sales are often a consequence of unexpectedly weak demand. Yet our observations of e-Saver™ promotions indicate that on the Internet clearance sales policies are not driven by demand uncertainty alone. Rather, “lastminute” sales can also occur as a consequence of the seller's previous (pro<sup>fi</sup>table) commitment to follow certain price patterns. By assuming that demand and supply are deterministic, we were able to better focus on the study of such commitments and other novel aspects of onlineselling policies. It should be emphasized, however, that although we studied only deterministic demand our model can serve as a benchmark for comparison with real world practices. Indeed, it can be easily<sup>8</sup> demonstrated that the main results of our analysis still hold in an extended setting where demand is not deterministic. Still, the introduction of demand uncertainty into the model is certainly an interesting topic for future research.

A second limitation of our model is that it assumes that all buyers arrive in the market at a single point in time. In many markets, this assumption cannot be regarded as being very realistic. In the airline industry, for example, it is well known that business travelers arrive on average later than leisure travelers. For this reason, we often observe that prices of airline tickets are increasing over time. Nevertheless, airlines do offer “last-minute” price-promotions as a matter of course. As Fig. 1 demonstrates, deeply discounted tickets were sold by US Airways as late as 72 h prior to <sup>fl</sup>ights' departures. Around a time that is so close to departure, it is likely that both leisure and business travelers are readily present in the market (relatively few of them are likely to arrive later). In such situations, therefore, we <sup>fi</sup>nd it reasonable to assume that demand is stationary and that travelers of both types simultaneously consider whether to purchase immediately at a higher price or wait for clearance sales. Of course, the incorporation of differential arrival rates over time for different customer types is most relevant and can result in a richer set of managerial implications. We leave this interesting issue, as well, as a topic for future research.

Lastly, another limitation of our model is that we consider a monopoly setting and thus ignore the impact of strategic interactions in a competitive environment. It is quite possible that competition will dramatically reduce the bene<sup>fi</sup>ts of segmentation, as deliberately imposing transaction risk on buyers may lead to an unsustainable equilibrium outcome. In markets that possess a relatively low degree of horizontal differentiation, we expect that buyers will tend to purchase a close substitute when their most preferred product is unavailable or its price is deemed too high. Incorporation of different transaction costs for buyers or different venue costs for the seller, nonlinear production cost functions, and endogenous product qualities could also contribute signi<sup>fi</sup>cantly to this discussion.

## Acknowledgements

The authors thank the editors Yabing Jiang and Jie Zhang, two anonymous referees, Evan Dudley, Assaf Eisdorfer, Rob Kaufmann, John Long, Evgeny Lyandres, Ravi Mantena, Amit Mehra, Edi Pinker, Michael Raith, Gabor Virag, and participants of the Workshop on Information Systems Economics 2007, and of the Hawaii International Conference on Systems Sciences 2010 for their valuable comments. The opinions presented are the exclusive responsibility of the authors.

## Appendix A. Proofs

Lemma 1. π(β) is a continuously differentiable function. Setting $\beta = 0$ is never optimal since

$$
\pi^ {\prime} (0) = V _ {\mathrm{L}} q _ {\mathrm{L}} > 0.\tag{24}
$$

A necessary condition for the optimality of setting $\beta = 1$ is

$$
\pi^ {\prime} (1) = - \frac {V _ {\mathrm{H}} - V _ {\mathrm{L}}}{1 - \rho} q _ {\mathrm{H}} + V _ {\mathrm{L}} q _ {\mathrm{L}} \geq 0.\tag{25}
$$

It can be shown that the above condition is also suf<sup>fi</sup>cient. Rearranging Eq. (25), we get

$$
\rho \leq 1 - \frac {V _ {\mathrm{H}} - V _ {\mathrm{L}}}{V _ {\mathrm{L}}} \cdot \frac {q _ {\mathrm{H}}}{q _ {\mathrm{L}}}.\tag{26}
$$

Therefore, at the optimum, $0 < \beta < 1$ if and only if $\rho > 1 -$ $\frac { V _ { \mathrm { H } } { - } \bar { V _ { \mathrm { L } } } } { V _ { \mathrm { L } } } \cdot \frac { q _ { \mathrm { H } } } { q _ { \mathrm { L } } } .$

This concludes the lemma's proof.

Lemma 2. Consider a strategy $S _ { 0 } { = } \left( { _ 0 p _ { 1 \mathrm { A } } , _ { 0 } p _ { 1 \mathrm { B } } , _ { 0 } p _ { 2 \mathrm { A } } , _ { 0 } p _ { 2 \mathrm { B } } ; _ { 0 } \alpha , _ { 0 } \beta , _ { 0 } \gamma } \right)$ with pro<sup>fi</sup>ts $\Pi ( S _ { 0 } ) = \pi _ { 0 } .$ If at the corresponding equilibrium all customers who buy do it in the same period, the seller can trivially attain or exceed $\pi _ { 0 }$ with some strategy $S _ { 1 }$ where $_ { 1 } \alpha = _ { 1 } \beta = _ { 1 } \gamma = 0$ . Hence it suf<sup>fi</sup>ces to consider the case where one customer type (H or L) buys in period 1 and the other type buys in period 2. If in equilibrium type-L customers buy in period 1 and type-H customers buy in period 2 then there is a strategy $S _ { 2 }$ with $_ { 2 } p _ { 2 \mathrm { A } } = V _ { \mathrm { H } } + \delta _ { \mathrm { H } } , _ { 2 } p _ { 2 \mathrm { B } } = V _ { \mathrm { H } }$ , and $_ { 2 } \alpha = 1$ and pro<sup>fi</sup>ts of $\Pi ( S _ { 2 } ) = \pi _ { 2 }$ such that $\pi _ { 2 } \geq \pi _ { 0 } .$ Thus there exists a strategy $S _ { 3 }$ with ${ } _ { 3 } p _ { 1 \mathrm { A } } = V _ { \mathrm { H } } + \delta _ { \mathrm { H } } , { } _ { 3 } p _ { 1 \mathrm { B } } > V _ { \mathrm { H } } , { } _ { 3 } p _ { 2 \mathrm { A } } = V _ { \mathrm { L } } + \delta _ { \mathrm { L } } , { } _ { 3 } p _ { 2 \mathrm { B } } = V _ { \mathrm { L } }$ , and $_ { 3 } \alpha = 1$ and pro<sup>fi</sup>ts of $\Pi ( S _ { 3 } ) = \pi _ { 3 } \geq \pi _ { 2 } \geq \pi _ { 0 }$ such that at the corresponding equilibrium type-H customers buy product A in period 1 and type-L customers buy either product A or product B in period 2. This proves the lemma's assertion. □

Lemma 3. Let $S _ { 0 } { = } ( \phantom { } _ { 0 } p _ { 1 \mathrm { A } } , \phantom { } _ { 0 } p _ { 1 \mathrm { B } } , \phantom { } _ { 0 } p _ { 2 \mathrm { A } } , \phantom { } _ { 0 } p _ { 2 \mathrm { B } } ; \phantom { } _ { 0 } \alpha , \phantom { } _ { 0 } \beta , \phantom { } _ { 0 } \gamma )$ be a strategy with $_ 0 \gamma { > } 0$ and pro<sup>fi</sup>ts $\Pi ( S _ { 0 } ) = \pi _ { 0 } .$

Following Lemma 1, we let

$$
{ } _ { 0 } p _ { 1 \mathrm{A} } = V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - \left[ ( { } _ { 0 } \alpha + { } _ { 0 } \gamma ) ( V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - { } _ { 0 } p _ { 2 \mathrm{A} } ) ^ { 1 - \rho } + { } _ { 0 } \beta ( V _ { \mathrm{H} } - { } _ { 0 } p _ { 2 \mathrm{B} } ) ^ { 1 - \rho } \right] ^ { \frac { 1 } { 1 - \rho } } .\tag{27}
$$

$$
{ } _ { 0 } p _ { 2 \mathrm{A} } = V _ { \mathrm{L} } + \delta _ { \mathrm{L} } \text {~ and~ } { } _ { 0 } p _ { 2 \mathrm{B} } = V _ { \mathrm{L} } .\tag{28}
$$

Consider now a modi<sup>fi</sup>ed strategy $\hat { S } _ { 0 } = ( \boldsymbol { 0 } p _ { 1 \mathrm { A } } ,$ ; p ; p ; p ; $\hat { \mathbf { \alpha } } _ { \mathrm { { \sf { d } } } } , \mathrm { { \beta } } , \hat { \mathsf { { \gamma } } } )$ with $\hat { \mathbf { \alpha } } = _ { 0 } \mathbf { \alpha } \mathbf { \alpha } + _ { 0 } \mathbf { \gamma } \gamma$ and $\hat { \gamma } = 0 .$ . It can be easily veri<sup>fi</sup>ed that $\hat { S } _ { 0 }$ dominates $S _ { 0 } .$ Therefore, the seller can indeed restrict herself to $\gamma = 0$ with no loss of optimality.

Theorem 1. Let $S _ { 0 } { = } \left( { _ 0 p _ { 1 \mathrm { A } } , _ { 0 } p _ { 1 \mathrm { B } } , _ { 0 } p _ { 2 \mathrm { A } } , _ { 0 } p _ { 2 \mathrm { B } } ; _ { 0 } { \alpha } , _ { 0 } \beta , _ { 0 } \gamma } \right)$ be a strategy such that at the corresponding equilibrium only type-H customers are buying (product A in period 1). We denote $\Pi ( S _ { 0 } ) = \pi _ { 0 }$

For any $0 \le \beta < 1 - \phantom { } _ { 1 } \alpha ,$ , let the strategy $S _ { 1 } ( \beta )$ be de<sup>fi</sup>ned as follows.

$$
S _ {1} (\beta) = (_ {1} P _ {1 \mathrm{A}} (\beta), _ {1} p _ {1 \mathrm{B}, 1} p _ {2 \mathrm{A}, 1} p _ {2 \mathrm{B}}; _ {1} \alpha , \beta , _ {1} \gamma), \text { with },\tag{29}
$$

$$
{ } _ { 1 } P _ { 1 \mathrm{A} } ( \beta ) = V _ { \mathrm{H} } + \delta _ { \mathrm{H} } - \beta ^ { \frac { 1 } { 1 - \rho } } ( V _ { \mathrm{H} } - V _ { \mathrm{L} } ) = { } _ { 1 } p _ { 1 \mathrm{A} } , { } _ { 1 } p _ { 2 \mathrm{B} } = V _ { \mathrm{L} } ,\tag{30}
$$

$$
{ } _ { 1 } p _ { 1 \mathrm{B} } = V _ { \mathrm{H} } + \varepsilon ; ( \varepsilon > 0 ) , \text {   and   } { } _ { 1 } \alpha = { } _ { 1 } \gamma = 0 .\tag{31}
$$

The seller's equilibrium pro<sup>fi</sup>ts can be described as a function of β:

$$
\Pi (S _ {1} (\beta)) \equiv \Pi_ {1} (\beta) = \left(V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - \beta^ {\frac {1}{1 - \rho}} (V _ {\mathrm{H}} - V _ {\mathrm{L}}) - c\right) q _ {\mathrm{H}} + \beta V _ {\mathrm{L}} q _ {\mathrm{L}}, 0 \leq \rho <   1.\tag{32}
$$

Clearly, $\Pi _ { 1 } ( 0 ) { \geq } \pi _ { 0 } .$ . The function $\Pi _ { 1 } ( \beta )$ is continuously differentiable with respect to β and $d \Pi _ { 1 } ( 0 ) = V _ { \mathrm { L } } q _ { \mathrm { L } } { > } 0$ for all $V _ { \mathrm { L } } , q _ { \mathrm { L } } { > } 0 .$ Therefore, there exists $\beta { > } 0$ such that $\Pi _ { 1 } ( \beta ) { > } \pi _ { 0 } .$ It follows that any pro<sup>fi</sup>t-maximizing strategy indeed induces type-L customers to buy with positive probability. □

Theorem 2. We need to show that for any set of model parametervalues $\{ V _ { \mathrm { H } } , V _ { \mathrm { L } } , \delta _ { \mathrm { H } } , \delta _ { \mathrm { L } } , q _ { \mathrm { H } } , q _ { \mathrm { L } } , \rho , c \}$ there is an optimal strategy where $\alpha = 0 , \beta = 0 , o r 1 - \alpha - \beta = 0 ,$

Let $S { = } ( p _ { 1 \mathrm { A } } , p _ { 1 \mathrm { B } } , p _ { 2 \mathrm { A } } , p _ { 2 \mathrm { B } } ; { \alpha } , \beta , \gamma )$ . Following Lemma 1 and Lemma 2, the following optimization problem is equivalent to the seller's pro<sup>fi</sup>tmaximization problem:

$$
\underset {S} {\text { Max }} p _ {1 A} q _ {H} + (\alpha \cdot p _ {2 A} + \beta \cdot p _ {2 B}) q _ {L} - (q _ {H} + \alpha q _ {L}) c.\tag{33}
$$

s.t.:

$$
(V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - p _ {1 \mathrm{A}}) ^ {1 - \rho} \geq \alpha (V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - p _ {2 \mathrm{A}}) ^ {1 - \rho} + \beta (V _ {\mathrm{H}} - p _ {2 \mathrm{B}}) ^ {1 - \rho}.\tag{33.1}
$$

$$
V _ {\mathrm{L}} + \delta_ {\mathrm{L}} \geq p _ {2 \mathrm{A}}.\tag{33.2}
$$

$$
V _ {\mathrm{L}} \geq p _ {2 \mathrm{B}}.\tag{33.3}
$$

$$
\alpha + \beta \leq 1.\tag{33.4}
$$

$$
\alpha , \beta \geq 0.\tag{33.5}
$$

Condition (33.1) is an incentive-compatibility constraint for type-H buyers. Without loss of optimality, we can consider only strategies S such that at the corresponding equilibrium Condition (33.1) is binding. That is,

$$
p _ {1 \mathrm{A}} = V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - \Big (\alpha (V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - p _ {2 \mathrm{A}}) ^ {1 - \rho} + \beta (V _ {\mathrm{H}} - p _ {2 \mathrm{B}}) ^ {1 - \rho} \Big) ^ {\frac {1}{1 - \rho}}.\tag{34}
$$

Conditions (33.2) and (33.3) are individual-rationality constraints for L-type buyers. Because at least one of these two constraints must be binding at equilibrium, we can restrict our attention to strategies S with

$$
p _ {2 \mathrm{A}} = V _ {\mathrm{L}} + \delta_ {\mathrm{L}} \text { and } p _ {2 \mathrm{B}} = V _ {\mathrm{L}}.\tag{35}
$$

Let λ be the Lagrange multiplier that corresponds to the constraint $\alpha + \beta \leq 1$ and let $\lambda _ { 2 }$ and $\lambda _ { 3 } \ \left( \lambda _ { 2 } , \lambda _ { 3 } { \le } 0 \right)$ be the multipliers that correspond to $( \alpha { \ge } 0 )$ and $( \beta \ge 0 )$ , respectively.

Then,

$$
\begin{array}{l} L (\alpha , \beta ; \lambda , \lambda_ {2}, \lambda_ {3}) = \Big (V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - \Big (\alpha (V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} \\ \qquad + \beta (V _ {\mathrm{H}} - V _ {\mathrm{L}}) ^ {1 - \rho} \Big) ^ {\frac {1}{1 - \rho}} \Big) q _ {\mathrm{H}} + (\alpha \cdot p _ {2 \mathrm{A}} + \beta \cdot p _ {2 \mathrm{B}}) q _ {\mathrm{L}} \\ \qquad - (q _ {\mathrm{H}} + \alpha q _ {\mathrm{L}}) c - \lambda (1 - \alpha - \beta) - \lambda_ {2} \cdot \alpha - \lambda_ {3} \cdot \beta . \end{array}\tag{36}
$$

First-order KKT conditions for optima include:

$$
\begin{array}{l} \frac {\partial L (\cdot)}{\partial \alpha} = (V _ {\mathrm{L}} + \delta_ {\mathrm{L}} - c) \cdot q _ {\mathrm{L}} \\ - \frac {(V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} \cdot \left(\alpha (V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} + \beta (V _ {\mathrm{H}} - V _ {\mathrm{L}}) ^ {1 - \rho}\right) ^ {\frac {\rho}{1 - \rho}}}{1 - \rho} \cdot q _ {\mathrm{H}} \\ + \lambda - \lambda_ {2}. \end{array} \tag {37}
$$

$$
\frac {\partial L (\cdot)}{\partial \beta} = V _ {L} \cdot q _ {L} - \frac {(V _ {H} - V _ {L}) ^ {1 - \rho} \cdot (\alpha (V _ {H} - V _ {L} + \delta_ {H} - \delta_ {L}) ^ {1 - \rho} + \beta (V _ {H} - V _ {L}) ^ {1 - \rho}) ^ {\frac {\rho}{1 - \rho}}}{1 - \rho} \cdot q _ {H} + \lambda - \lambda_ {3}.\tag{38}
$$

At any optimal point where $\alpha { > } 0 ,$

$$
\alpha = (V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {\rho - 1}. \bigg (\bigg [ \frac {(1 - \rho) ((V _ {\mathrm{L}} + \delta_ {\mathrm{L}} - c) q _ {\mathrm{L}} + \lambda)}{(V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} \cdot q _ {\mathrm{H}}} \bigg ] ^ {\frac {1 - \rho}{\rho}} - \beta \cdot (V _ {\mathrm{H}} - V _ {\mathrm{L}}) ^ {1 - \rho} \bigg).\tag{39}
$$

And at any optimum with $\beta { > } 0$

$$
\beta = (V _ {\mathrm{H}} - V _ {\mathrm{L}}) ^ {\rho - 1} \cdot \biggl (\Big [ \frac {(1 - \rho) (V _ {\mathrm{L}} q _ {\mathrm{L}} + \lambda)}{(V _ {\mathrm{H}} - V _ {\mathrm{L}}) ^ {1 - \rho} \cdot q _ {\mathrm{H}}} \Big ] ^ {\frac {1 - \rho}{\rho}} - \alpha \cdot (V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} \biggr).\tag{40}
$$

Whenever $\lambda { < } 0 ,$ , then $\alpha + \beta = 1$ and the theorem is trivially satis<sup>fi</sup>ed. Let us consider then the case when $\lambda = 0$ . We de<sup>fi</sup>ne

$$
M = \left(\frac {V _ {\mathrm{H}} - V _ {\mathrm{L}}}{V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}}\right) ^ {1 - \rho} \geq 0 \text { and } N = \frac {V _ {\mathrm{L}}}{V _ {\mathrm{L}} + \delta_ {\mathrm{L}} - c} \geq 0.\tag{41}
$$

Based on different values of M and N, we deal with three separate cases.

Case I: MNN

If at the optimum $\alpha { = } 0 ,$ , then the theorem is trivially satis<sup>fi</sup>ed. If $\alpha = 1$ , then $\beta = 0 ,$ , and the theorem is again trivially satis<sup>fi</sup>ed. When $0 { < } \alpha { < } 1$ , from Eqs. (38) and (39),

$$
\frac {\partial L (\cdot)}{\partial \beta} = (V _ {L} + \delta_ {L} - c) (N - M) q _ {L} - \lambda_ {3} = 0, 0 <   \alpha <   1, \beta \leq 1 - \alpha .\tag{42}
$$

Since $M { > } N$ (and $q _ { L } { > } 0 )$ , Condition (42) is satis<sup>fi</sup>ed only if $\lambda _ { 3 } { < } 0$ (i.e., only $\operatorname { i f } \beta = 0 )$ , in accord with the theorem.

Case II: MbN

If at the optimum $\beta = 0$ or $\beta = 1$ , then the theorem is trivially satis<sup>fi</sup>ed. Elsewhere $( 0 < \beta < 1 )$ , from Eqs. (37) and (40),

$$
\frac {\partial L (\cdot)}{\partial \alpha} = V _ {L} \left(\frac {1}{N} - \frac {1}{M}\right) q _ {L} - \lambda_ {2} = 0, \alpha \leq 1 - \beta , \quad 0 <   \beta <   1.\tag{43}
$$

Since $M { < } N ,$ Condition (43) is satis<sup>fi</sup>ed only if λ b0 (i.e., only if α=0). Therefore, there is an optimal strategy S with $\alpha { = } 0 ,$ , in accord with the theorem.

Case III: $M = N$

If at the optimum $\alpha { = } 0 \ \mathrm { o r } \ \alpha { = } 1$ , then the theorem is trivially satis<sup>fi</sup>ed. By Eqs. (33) and (34), for any α and β such that $0 < \alpha + \beta < 1$

$$
\begin{array}{c} \Pi (S) = \Big (V _ {\mathrm{H}} + \delta_ {\mathrm{H}} - (V _ {\mathrm{H}} - V _ {\mathrm{L}} + \delta_ {\mathrm{H}} - \delta_ {\mathrm{L}}) ^ {1 - \rho} (\alpha + \beta \cdot M) - c \Big) q _ {\mathrm{H}} \\ + (V _ {\mathrm{L}} + \delta_ {\mathrm{L}} - c) (\alpha + \beta \cdot N) q _ {\mathrm{L}} \end{array}\tag{44}
$$

Suppose that S is an optimal policy with $\alpha { > } 0$ and $\beta { > } 0$ . Let $K = \alpha + \beta N = \alpha + \beta M < 1$ . The seller's equilibrium pro<sup>fi</sup>t is the same for all strategies with probability α and $\beta$ that result in the same value of K. Hence there is another optimal strategy $S _ { 0 } { = } ( \phantom { } _ { 0 } p _ { 1 \mathrm { A } } , \phantom { } _ { 0 } p _ { 1 \mathrm { B } } , \phantom { } _ { 0 } p _ { 2 \mathrm { A } } , \phantom { } _ { 0 } p _ { 2 \mathrm { B } } ; \phantom { } _ { 0 }$ $_ 0 \alpha , _ { 0 } \beta , _ { 0 } \gamma )$ with $\phantom { } _ { 0 } \alpha = K$ and $_ 0 \beta = 0$ such that $\Pi ( S _ { 0 } ) = \Pi ( S )$ , in accord with the theorem.

This completes the proof.

□

## References

[1] E.T. Anderson, J. Dana, When is price discrimination pro<sup>fi</sup>table? Manage. Sci. 55 (6) (2009) 980–989.

[2] Y. Aviv, A. Pazgal, Optimal pricing of seasonal products in the presence of forwardlooking consumers, Manuf. Serv. Oper. Manage. 10 (3) (2008) 339–359.

[3] D. Besanko, W.L. Winston, Optimal price skimming by a monopolist facing rational consumers, Manage. Sci. 36 (5) (1990) 555–567.

[4] G.P. Cachon, R. Swinney, Purchasing, pricing, and quick response in the presence of strategic consumers, Manage. Sci. 55 (3) (2009) 497–511.

[5] R.H. Coase, Durability and monopoly, J. Law Econ. 15 (1) (1972) 143–149.

[6] R.J. Deneckere, R.P. McAfee, Damaged goods, J. Econ. Manage. Strategy 5 (2) (1996) 149–174.

[7] K. Jerath, S. Netessine, S.K. Veeraraghavan, Revenue management with strategic customers: last-minute selling and opaque selling, Manage. Sci. 56 (3) (2010) 430–448.

[8] J.P. Johnson, D.P. Myatt, Multiproduct quality competition: <sup>fi</sup>ghting brands and product line pruning, Am. Econ. Rev. 93 (3) (2003) 748–774.

[9] O. Koenigsberg, E. Muller, N.J. Vilcassim, easyJet® pricing strategy: should lowfare airlines offer last-minute deals? Quant. Mark. Econ. 6 (3) (2008) 279–297.

[10] Q. Liu, G.J. van Ryzin, Strategic capacity rationing to induce early purchases, Manage. Sci. 54 (6) (2008) 1115–1131.

[11] O. Marom, A. Seidmann, A Model of Market Segmentation with Risk, Working paper, University of Rochester, 2008.

[12] E. Maskin, J. Riley, Optimal auctions with risk averse buyers, Econometrica 52 (6) (1984) 1473–1518.

[13] S.A. Matthews, Selling to risk averse buyers with unobservable tastes, J. Econ. Theory 30 (1983) 370–400.

[14] M.S. Mussa, S. Rosen, Monopoly and product quality, J. Econ. Theory 18 (1978) 301–317.

[15] N. Stokey, Intertemporal price discrimination, Quart. J. Econ. 93 (3) (1979) 355–371.

[16] X. Su, Inter-temporal pricing with strategic customer behavior, Manage. Sci. 53 (5) (2007) 726–741.

![](/api/attachments/X9E5UYG2/fulltext/images/3784556d23c310c08ebad3414834e11c10aa8b15e1d6ac2664e764856454c813.jpg)  
Ori Marom is Assistant Professor of Decision and Information Sciences at the Rotterdam School of Management Erasmus University. His work is in the area of Economics and Value of Information Technologies, Pricing and Revenue Management, and Electronic Marketing. He holds a Ph.D. in Information Systems Economics (2008) from the University of Rochester, Rochester, New York

![](/api/attachments/X9E5UYG2/fulltext/images/13ebcf217dca4599d199fc713eda9ae993faf07fcef01b7063f6f148eacddde8.jpg)

Abraham Seidmann is Xerox Professor of Computers and Information Systems and Operations Management at the William E. Simon Graduate School of Business Administration, University of Rochester. He is the author of over 100 research articles, which appear in many of the leading scienti<sup>fi</sup>c journals, and has been the founding department editor on interdisciplinary management research and applications in Management Science for 10 years. He is also an associate or area editor for IIE Transactions, the International Journal of Flexible Manufacturing Systems, Production Planning and Controls, the Journal of Intelligent Manufacturing, the Journal of Management Information Systems, and Production and Operations Management.
