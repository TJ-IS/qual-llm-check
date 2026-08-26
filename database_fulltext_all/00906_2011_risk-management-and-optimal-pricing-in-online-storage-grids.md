---
otero_id: 906
otero_key: "BKFJXE3G"
title: "Risk Management and Optimal Pricing in Online Storage Grids"
authors: "Sanjukta Das; Anna Ye Du; Ram Gopal; R. Ramesh"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0288"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/BKFJXE3G/fulltext/images/230e378db0a5362b3ee8496bbe1df1ef224b675c3b177b780febc1f091fbe8c0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Risk Management and Optimal Pricing in Online Storage Grids

Sanjukta Das, Anna Ye Du, Ram Gopal, R. Ramesh,

To cite this article:

Sanjukta Das, Anna Ye Du, Ram Gopal, R. Ramesh, (2011) Risk Management and Optimal Pricing in Online Storage Grids. Information Systems Research 22(4):756-773. http://dx.doi.org/10.1287/isre.1100.0288

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/BKFJXE3G/fulltext/images/4bad7cc6790ef9dc142afc2f78406787e67f4d07fb1fe534f63892940c11c035.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Risk Management and Optimal Pricing in Online Storage Grids

Sanjukta Das, Anna Ye Du

Department of Management Science and Systems, State University of New York at Buffalo, Buffalo, New York 14260 {sdsmith4@buffalo.edu, yedu@buffalo.edu}

Ram Gopal

Department of Operations and Information Management, University of Connecticut, Storrs, Connecticut 06269, ram@business.uconn.edu

R. Ramesh

Department of Management Science and Systems, State University of New York Buffalo, Buffalo, New York 14260, rramesh@buffalo.edu

nline storage service providers grant a way for companies to avoid spending resources on maintaining their own in-house storage infrastructure and thereby allowing them to focus on their core business activities. These providers, however, follow a fixed, posted pricing strategy that charges the same price in each time period and thus bear all the risk arising out of demand uncertainties faced by their client companies. We examine the effects of providing a spot market with dynamic prices and forward contracts to hedge against future revenue uncertainty. We derive revenue-maximizing spot and forward prices for a single seller facing a known set of buyers. We perform a simulation study using publicly available traffic data regarding Amazon S3 clients from Alexa.com to validate our analytical results. Our field study supports our analysis and indicates that spot markets alone can enhance revenues to Amazon, but this comes at the cost of increased risks due to the increased market share in the spot markets. Furthermore, adding a forward contract feature to the spot markets can reduce risks while still providing the benefits of enhanced revenues. Although the buyers incur an increase in costs in the spot market, adding a forward contract does not cause any additional cost increase while transferring the risk to the buyers. Thus, storage grid providers can greatly benefit by applying a forward contract alongside the spot market.

Key words: online storage; grid computing; forward contracts; market mechanism design History: Alok Gupta, Senior Editor; Yong Tan, Associate Editor. This paper was received on May 2, 2008, and was with the authors 7 <sup>3</sup><sub>4</sub> months for 3 revisions. Published online in Articles in Advance June 14, 2010.

## 1. Introduction

This research is motivated by recent advances in the market for Internet storage grids pioneered by emergent business models of firms such as Amazon S3 (Amazon.com 2008) and Nirvanix (Nirvanix 2008). The value proposition of these models is driven by the rapid growth in online businesses that create media-rich content or serve customers that use such content. These businesses continually face the problem of uncertain demands for storage infrastructures while having to maintain acceptable service quality levels such as timely delivery of data-intensive services. This entails following one of two strategies for storage provisioning: build enough capacity to service a maximum estimated demand at a chosen quality level or build an acceptable capacity with the option that additional capacity can be rented when needed if an online storage provider is available. The value proposition of Amazon S3 and Nirvanix enables the second strategy. Amazon S3 serves as an online provider with its own storage grid by utilizing the vast idle capacity in its thousands of servers around the globe. This allows Amazon’s clients (primarily start-up companies) to store their content on Amazon servers and in turn also serve the content to their customers from these servers. SmugMug.com, an online photo-sharing start-up company that uses S3 for content storage and delivery, claims to save between \$1 and \$2 million in a single year in direct and indirect costs as a result of not needing to invest in servers (SmugMug 2006a). According to Amazon, businesses spend 70% of their time building and maintaining their infrastructure, and this effort could be better spent focusing on their core business functions by utilizing the services of Amazon S3.

Central to the business models of online storage grids like Amazon S3 are resource pricing and hedging against the risks of unsold capacities over time. Almost every real-world example of grid computing (storage or otherwise), including Amazon, uses posted prices. Posted prices have the nice property of being simple and easily communicable. However, the market for computing resources is still in its infancy. There is not enough information available regarding the overall demand and supply in the market to determine reliable posted prices. Therefore, prices tend to be somewhat ad hoc, and hedging the risks of unsold capacities has not yet been addressed in these emerging markets. In our research, following along the lines of Amazon, we develop an optimal resource-pricing model that incorporates a risk-hedging mechanism using forward contracts for a single seller serving multiple clients with stochastic demands over time. The proposed model also uses posted spot prices, but such prices do not remain fixed across periods and are determined by the customers’ demand profiles and the relative prices of other substitutes.

We show that it is more efficient and practically feasible for a revenue-maximizing seller such as Amazon to derive commodity prices in predetermined time periods. Currently, Amazon uses a fixed posted price regardless of time, and the proposed model is a significant improvement of this practice. Further, now the seller bears all the risk associated with the fluctuating demands of its clients, who buy only what is needed at any given time. By introducing a forwards contract over time periods where buyers agree to satisfy their entire demand in the future period by buying from the online provider subject to a minimum purchase of a predetermined amount at a predetermined rate, the risk is transferred from the seller to the buyers. The model also ensures that such a pricing strategy is compatible with the clients’ incentives to buy. Moreover, this strategy enables clients to reserve capacity before demand is realized. Note that using a service such as Amazon S3 is a way to manage the risk due to demand fluctuations faced by a client over time periods, and capacity reservations based on forecasts are a logical choice for them. We draw upon the forwards and spot-pricing literature in finance to derive the pricing model.

We model the seller’s pricing problem as a mixedinteger program. We compare our transparent pricing policy with that of first-degree price discrimination and find that the latter does not always dominate. We devise an optimal algorithm that exploits the special structure of this problem to solve it in polynomial time. We conduct a risk-return analysis to evaluate the pricing strategies. We validate our results from real-world data on 37 current clients of Amazon. Our empirical analysis indicates that spot markets alone can on average enhance revenues to Amazon by 41% and increase risks by 108% due to increased market share. Furthermore, forward contracts alongside the spot markets can on average reduce risks to Amazon by 57% and enhance revenues by 51%. These results support our theoretical findings.

## 1.1. The Model Context

The pricing decisions are made for a predetermined time period, the length of which is at the discretion of the seller. The seller provides online storage service to its clients and is unconstrained in its capacity. This is a reasonable assumption for a large provider such as Amazon. We model the pricing and risk management problem over two time periods. The buyer’s exact demand in Period 1 is known, whereas in Period 2 only the demand distribution is known. Note that the buyers are heterogeneous in terms of their demand distributions. This demand information is known by both the buyer and the seller. For existing buyers, this information can be compiled by the seller directly from their past usage history. For new buyers, either they provide this information directly to the seller or the seller estimates their demand based on past behavior of similar buyers (e.g., similar start-ups, similarly sized companies). Section 6 provides a practical approach to perform such demand estimation. The assumption of known demand in Period 1 is valid because buyers normally commit to a certain quantity ahead of time, as opposed to ordering right at the point of consumption. This is true regardless of whether a buyer chooses to build his own capacity or buy in the spot market. Prior to the start of Period 1, the buyer derives some estimate, based on which a purchase commitment is made and a forward contract may be arrived at. This estimate could be based on some demand distribution. Consequently, the amount of capacity acquired at the beginning of Period 1 is treated as fixed, and this defines the initial conditions in the model. However, recognizing that it could still be estimated, in the remainder of the paper we use the term “estimated demand” with reference to Period 1.

The objective of the seller is to determine unit prices for the storage service such that he manages the risk and return and optimizes his expected revenues. We demonstrate, both analytically and computationally, that risk management tools such as forward contracts can mitigate risk and not reduce (and under certain conditions even increase) the revenue of the seller as opposed to simply charging the spot price alone. We also analyze the risk-return portfolio when the seller faces a particular set of buyers, which allows the seller to select a set of prices based on the attractiveness of the returns and its tolerance for the risk associated with that level of returns. We provide below the setup of the buyers’ and the seller’s decision problems.

## 1.2. Buyer’s and Seller’s Problem Description

In our problem, the seller observes the building cost and estimates the demand of buyers in Period 1. He uses these in conjunction with the demand distributions of buyers in Period 2 to determine a set of spot and forward prices such that they maximize his return, while using forward contracts as a risk mitigation strategy. The seller then announces these prices in the market. Based on these prices, the buyers decide on their resource acquisition strategy for each of the two periods: whether to build their own capacity or to buy from the seller either in the spot or forward market. The buyer’s objective is to minimize cost. Figure 1 shows this problem setup in a diagrammatic manner.

Figure 1 Sequence of Buyer and Seller Decisions  
![](/api/attachments/BKFJXE3G/fulltext/images/5160d7536f3852ca446b8baaffed0ae497588f5916cb52c931801329975a5355.jpg)

## 1.3. Roadmap of the Paper

Section 2 presents the related work, and §3 develops the pricing and the risk model under different strategies. Section 4 presents an optimal algorithm for deriving the spot and forward prices in polynomial time. We analyze the risk and return trade-offs of the seller under the different pricing strategies in §5. In §6, we validate our analytical results by conducting a simulation study using publicly available data from Alexa.com and Quantcast.com. We conclude with §7.

## 2. Related Work

The areas most related to our research are the domains of grid computing and other distributed computational economies (DCE). The literature on resource management and sharing in DCE is quite large (see Du et al. 2008 for a comprehensive survey). A DCE is modeled as a network of resources with both localized and distributed management with explicit ownerships. As a result, the idea of producers and consumers of resources is extensively utilized in the grid- and storage-centered DCE research community. Research on grid capacity trading and associated economic incentives is evolving (Bapna et al. 2008, 2011; Frey et al. 2001; Du et al. 2008; Sairamesh and Kephart 1998). Computational grids with sharable resources have been developed by businesses such as United Devices, Entropia, ProcessTree, Parabon, and Popular Power. These grids are rooted in economic inducement for individual resource owners to partake in trading in integrated network architectures (Buyya 2002). Hierarchical and network-based resource management and sharing strategies, together with the economics of DCE, are outlined in Buyya (2002). The fundamental motivation to trade happens as a result of the resource topography, demand and supply of resources, system integration, quality of service (QoS), and system availability and scalability (Cocchi et al. 1993, Lalis and Karipidis 2000).

A number of economic models of resource sharing that lie beneath the resource management processes have been put forward (Lazar and Semret 1997, Huhns and Stephens 2000, Miller and Drexler 1998, Buyya 2002, Smith and Davis 1980). These are comprised of familiar models such as commodity markets, posted prices, bargaining, contract-nets, auctions, and proportional resource sharing, among others. Additionally, quite a few research systems have put several of these models into practice. A few of the pertinent systems include Mungi (Heiser et al. 1998), CSAR (Brooke et al. 2000), Mojo Nation (http://www.mojonation.net/), Stanford Peers (Cooper and Garcia-Molina 2002), Mariposa (Stonebraker et al. 1994), Spawn (Waldspurger et al. 1992), and GridSim (Buyya 2002). To the best of our knowledge, none of these research works address the issue of risk management and the use of financial instruments such as forward contracts in the derivation of commodity prices for computing resources.

## 3. The Pricing and Risk Model

We introduce the notion of downside risk embedded in the buy-or-build decision in §3.1. In §3.2, we model the spot and forward prices for a single buyer to gain insights into the buyer behavior in response to prices under a controlled environment. This includes an analysis of pricing, return, properties of risk under various pricing scenarios, and risk management. In §3.3, we develop the full set of alternatives available to each buyer and model the general case of multiple buyers. Finally, in §3.4, we compare the effectiveness of providing transparent prices vis-à-vis following a strategy of first-degree price discrimination and derive the conditions under which each strategy is better.

## 3.1. The Concept of Downside Risk

The buyer’s build-or-buy decision is made in both Periods 1 and 2. However, the cost-benefit analysis of this decision is different in the two periods, because in Period 1, the demand can be estimated fairly accurately whereas that for Period 2 is unknown. The risk faced by a buyer in this context is modeled as follows. Let c denote the known amount of capacity that a buyer needs in Period 1. If the buyer chooses to build capacity $c ,$ then it can be used to meet both the estimated demand in Period 1 and some or all of the demand in Period 2.

Let X denote the demand random variable in Period 2 with a continuous probability density function $\begin{array} { r } { \pi ( x ) , \int _ { 0 } ^ { \infty } \pi ( x ) d x = 1 } \end{array}$ . If demand goes up in

Period 2, $\mathrm { i } . \mathrm { e } . , x > c ,$ the buyer will just need to obtain the additional capacity of $x - c$ in Period 2.<sup>1</sup> If demand goes down, $\mathrm { i . e . , } \ x < c ,$ the capacity $c \mathrm { ~ - ~ } x$ built in Period 1 will remain idle in Period 2. We call this the “risk of overbuilding.” However, note that due to the nature of fairly accurate estimate of demand in Period 1, a parallel notion of “risk of overbuying” either does not exist when the buyer chooses to buy and pay only for what he consumes or such risk can be considered to be negligible for the purpose of tractability of the model and insightfulness of the results.

The demand for Period 2 becomes known at its onset. Consequently, the principal risk embedded in the buy-or-build process is a downside risk associated with the amount of capacity built in Period 1. This risk is captured by the risk of overbuilding. Similarly, we define a reward concept where capacity built in Period 1 can be reused in Period 2. The choice of buying does not entail such reward or risk concepts. When the buyer buys capacity c in Period 1 and whatever is needed in Period 2, the seller assumes all the associated reward and risk.

Risk is traditionally associated with some underlying commodity. In our case, the capacity built is the commodity. The capacity, $^ { c , }$ that is built in Period 1 to meet the demand in both periods, is a risky commodity due to the risk of overbuilding. When $x > c$ in Period 2, the amount $x - c$ is a risk-free commodity because the demand for it involves no uncertainty at the time (Period 2) it is built. Let d denote the normalized average absolute downside deviation from c. We use $d _ { X / c }$ to denote the downside risk in demand as defined below.

<sup>Definition</sup> <sup>1.</sup> The downside risk in demand is measured as

$$
d _ {\frac {X}{c}} = \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x) d x.
$$

We show how the different pricing mechanisms affect the bearing and hedging of risk in the next section.

## 3.2. Modeling Buyer Strategies

We first model a single-buyer market and develop the expected costs to the buyer and the expected revenues of the seller under different pricing scenarios in the following discussion.

3.2.1. Spot Market. Let the seller’s price in Periods 1 and 2 be $p _ { 1 } ^ { S }$ and $p _ { 2 } ^ { S } ,$ , respectively. Let C and G be the buyer’s total cost and the seller’s total gain, respectively, over the two periods. Let r be the unit building cost faced by the buyer less the salvage value of that unit.<sup>2</sup> If $p _ { 1 } ^ { S } , p _ { 2 } ^ { S } \leq \dot { r } ,$ the buyer has two choices: (a) build in Period 1 and buy any shortage in Period 2, or (b) buy in both periods. If the buyer chooses (a), his expected cost and the seller’s expected gain are, respectively,

$$
\begin{array}{c} E ^ {a} [ C ] = r c + p _ {2} ^ {S} \int_ {c} ^ {\infty} (x - c) \pi (x)   d x \quad \text { and } \\ E ^ {a} [ G ] = p _ {2} ^ {S} \int_ {c} ^ {\infty} (x - c) \pi (x)   d x. \end{array}
$$

If the buyer chooses (b), his expected cost is $E ^ { b } [ C ] ,$ which is the same as the seller’s expected gain, $E ^ { b } [ G ]$

$$
E ^ {b} [ C ] = p _ {1} ^ {S} c + p _ {2} ^ {S} \int_ {0} ^ {\infty} x \pi (x) d x.
$$

The buyer will choose (b), if ${ \cal E } ^ { b } [ C ] \leq { \cal E } ^ { a } [ C ]$ , or

$$
p _ {1} ^ {S} c + p _ {2} ^ {S} \left(\int_ {0} ^ {c} x \pi (x) d x + c \int_ {c} ^ {\infty} \pi (x) d x\right) \leq r c.\tag{1}
$$

<sup>Lemma</sup> <sup>1.</sup> A buyer would choose to buy in the spot market in both periods rather than to build all by himself, if

$$
p _ {1} ^ {S} + p _ {2} ^ {S} \left(\int_ {c} ^ {\infty} \pi (x) d x + \int_ {0} ^ {c} \frac {x}{c} \pi (x) d x\right) \leq r.
$$

<sup>Proof.</sup> Simplify constraint (1).

Lemma 1 is trivial. However, it shows how the reward from building capacity c in Period 1 would affect the buyer’s buy-or-build decision making for c. If buyer builds $^ { c , }$ then in the parentheses in inequality (1), the first term is the amount of capacity c that could be used in Period 2 when there is a downside demand, and the second term is that when there is an upside demand. If the buyer buys c in Period 1 instead, the reward essentially goes to the seller. Equation (1) states that the buyer would choose the spot market over the build option when the purchase cost for c in Period 1 plus the reward to the seller in Period 2 is less than the buyer’s building cost for c. Lemma 1 expresses this notion using per-unit costs.

The seller, being the price-setter, faces two maximization problems.

For choice (a)

$$
\begin{array}{l} \max p _ {2} ^ {S} \int_ {c} ^ {\infty} (x - c) \pi (x) d x \\ \text {s.t.} p _ {1} ^ {S} c + p _ {2} ^ {S} \bigg (\int_ {0} ^ {c} x \pi (x) d x + c \int_ {c} ^ {\infty} \pi (x) d x \bigg) \geq r c, \\ p _ {1} ^ {S}, p _ {2} ^ {S} \leq r. \end{array}
$$

For choice (b)

$$
\begin{array}{l} \max p _ {1} ^ {S} c + p _ {2} ^ {S} \int_ {0} ^ {\infty} x \pi (x)   d x \\ \text {s.t.} p _ {1} ^ {S} c + p _ {2} ^ {S} \bigg (\int_ {0} ^ {c} x \pi (x)   d x + c \int_ {c} ^ {\infty} \pi (x)   d x \bigg) \leq r c, \\ p _ {1} ^ {S}, p _ {2} ^ {S} \leq r. \end{array}
$$

The maximum value of the objective function for choice (a) is $\textstyle r \int _ { c } ^ { \infty } ( x - c ) \pi ( x ) d x$ . Choice (b) is a linear knapsack problem. The maximum value of the objective function for it is $\begin{array} { r } { r ( c \int _ { 0 } ^ { c } \pi ( x ) d x + \int _ { c } ^ { \infty } x \pi ( x ) d x ) } \end{array}$ at the following spot prices:

$$
\begin{array}{l} p _ {1} ^ {S} = \frac {r c - r \left(\int_ {0} ^ {c} x \pi (x) d x + c \int_ {c} ^ {\infty} \pi (x) d x\right)}{c} \\ \qquad = r \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x) d x \quad \text { and } \\ p _ {2} ^ {S} = r. \end{array}
$$

It can be shown that the seller’s gain from (b) is greater than that from (a) if $c \geq 0 ,$ , which always holds. Therefore, to achieve the highest gain, the seller should set the price as follows:

$$
p _ {1} ^ {S *} = r \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x) d x \quad \text { and } \quad p _ {2} ^ {S *} = r.
$$

From the solutions, we can see that $p _ { 1 } ^ { S * } \leq r ,$ whereas $p _ { 2 } ^ { S * } = r .$ , which is the most that the seller can charge. This is similar to a marketing strategy where the seller attracts the buyer with lower prices in Period 1 to induce buying instead of building, and then increases the price to extract the buyer’s entire surplus in Period 2. When the seller wants to get higher revenue, (b) is better than (a). Nevertheless, (b) also involves risk. This pricing mechanism allows the buyer to buy only what he needs in each period, thus avoiding the risk of overbuilding due to the uncertainty. Thus, the buyer could pay less at the start-up of his business and decide how much to buy at a later time, based on the market conditions. As a result of buying, however, the seller shoulders the risk of overbuilding or the downside risk that the buyer originally faced. Note that from the perspective of the seller, the downside risk can be viewed as opportunity revenue lost. On the other hand, the pricing mechanism allows the seller to compensate himself with a higher price for taking on greater risk. The price $p _ { 1 } ^ { S * }$ increases monotonically with downside risk $d _ { X / c }$ . Therefore, the higher the downside risk, the higher is the overbuilding risk, and the higher is the price at which the buyer would still buy rather than build in Period 1. We show in the next subsection that there is a ground where the seller transfers the risk back to the buyer by employing a forward contract. We further show that it is possible for the seller to extract additional surplus if he uses the forward contract.

We now consider, for the purpose of illustrating some special properties of the prices, a case where the seller charges the same price $p$ in both Periods 1 and 2. Note that this is also currently the practice of Amazon S3. If the buyer chooses (a), his expected cost and the seller’s expected gain are, respectively,

$$
\begin{array}{c} E ^ {a} [ C ] = r c + p \int_ {c} ^ {\infty} (x - c) \pi (x) d x \quad \text { and } \\ E ^ {a} [ G ] = p \int_ {c} ^ {\infty} (x - c) \pi (x) d x. \end{array}
$$

If the buyer chooses (b), his expected cost (which is the same as the seller’s expected gain $E ^ { b } [ G ] )$ is

$$
E ^ {b} [ C ] = p c + p \int_ {0} ^ {\infty} x \pi (x) d x.
$$

The buyer will choose (b), i.e., to buy in Period 1, if $E ^ { b } [ C ] \leq ^ { \prime } E ^ { a } [ C ]$ , or when

$$
p \leq \frac {r c}{c + \int_ {0} ^ {c} x \pi (x) d x + c \int_ {c} ^ {\infty} \pi (x) d x} = \bar {p}.
$$

Let $\bar { p }$ be the highest price at which the buyer will buy. The seller’s expected gain over price is shown in Figure 2.

When the price is relatively low, the buyer chooses (b) and the seller’s revenue increases with price and reaches its highest point B in that segment at the price ${ \bar { p } } .$ However, when the price moves above ${ \bar { p } } ,$ the buyer chooses (a), and the seller’s revenue drops. As the price continues to increase, the seller’s revenue increases again and reaches the highest point A in that segment at price r . If $p > r ,$ the buyer will choose neither (a) nor (b) but will build in both periods. Let $E ^ { A } [ G ]$ and $E ^ { B } [ G ]$ denote the seller’s gains at points A and $B ,$ respectively,

$$
\begin{array}{l} E ^ {A} [ G ] = r \int_ {c} ^ {\infty} (x - c) \pi (x) d x \quad \text { and } \\ E ^ {B} [ G ] = \bar {p} c + \bar {p} \int_ {0} ^ {\infty} x \pi (x) d x. \end{array}
$$

The optimal price, $p ^ { * } ,$ , is determined as $p ^ { * } = \bar { p }$ if ${ \cal E } ^ { \scriptscriptstyle B } [ G ] \ \geq \ { \cal E } ^ { \scriptscriptstyle A } [ \dot { G } ]$ and $\boldsymbol { p ^ { * } } = \boldsymbol { r }$ otherwise. From ${ \cal E } ^ { \scriptscriptstyle B } [ G ] \stackrel { \scriptscriptstyle - } { \geq } \bar { \cal E } ^ { \scriptscriptstyle A } [ G ]$ , we get

$$
\bar {p} \geq \frac {r \int_ {c} ^ {\infty} (x - c) \pi (x) d x}{c + \int_ {0} ^ {\infty} x \pi (x) d x}.
$$

Figure 2 The Seller’s Expected Gain Over Price  
![](/api/attachments/BKFJXE3G/fulltext/images/6dc276aeb01d2d73da96b93a8fa796abdb845dbd68b1c65db93c437c6e4146bb.jpg)

Note the lower and upper bounds on ${ \bar { p } } .$ Simplifying ${ \bar { p } } ,$ we get

$$
\bar {p} = \frac {r}{2 - \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x) d x}.
$$

Because $\begin{array} { r } { \int _ { 0 } ^ { c } \left( 1 - x / c \right) \pi ( x ) d x \geq 0 , } \end{array}$ , we therefore obtain the lower bound on ${ \bar { p } } .$ Because the upper bound is $r ,$ we have $r / 2 \le \bar { p } \le r$ . Note that the effects of the distribution on the value of $\bar { p }$ are such that a buyer facing greater downside risk would have lesser incentive to build in Period 1, and therefore the seller could charge a higher price and it would still be preferable for that buyer to buy rather than build.

<sup>Lemma</sup> <sup>2.</sup> In the single-buyer case, uniform price in both periods results in suboptimal revenues for the seller.

<sup>Proof.</sup> See the online supplement.<sup>3</sup>

3.2.2. Forward Contract. In this scenario, the seller offers the buyer a forward contract that specifies that he must commit to buy a minimum amount of c and any additional $x - c , { \mathrm { ~ i f ~ } } x > c ,$ in Period $2$ at the price of $p _ { 2 } ^ { F }$ . As a part of this contract, the buyer gets a special rate for the quantity bought in Period $^ { 1 , }$ i.e., $p _ { 1 } ^ { F }$ . Note that it is also possible for the buyer to not accept the forward contract and buy from the spot market on an as-needed basis in Period 1. Here we ignore this option to keep the analysis simple while still obtaining some critical insights. We include this option when we explore the multiple-buyer case in §3.3.

When $p _ { 1 } ^ { F } , p _ { 2 } ^ { F } , p _ { 2 } ^ { S } \leq r ,$ the buyer has two choices: (a) build in Period 1 and buy any shortage, if needed, in Period 2 at the spot price $p _ { 2 } ^ { \check { S } } ,$ , or (b) buy the forward contract in Period 1. If the buyer chooses (a), his expected cost and the seller’s expected gain are, respectively:

$$
\begin{array}{c} E ^ {a} [ C ] = r c + p _ {2} ^ {S} \int_ {c} ^ {\infty} (x - c) \pi (x)   d x \quad \text { and } \\ E ^ {a} [ G ] = p _ {2} ^ {S} \int_ {c} ^ {\infty} (x - c) \pi (x)   d x. \end{array}
$$

If the buyer chooses (b), his expected cost is $E ^ { b } [ C ] ,$ which is also equal to the seller $' \mathrm { s }$ expected gain ${ \cal E } ^ { b } [ G ]$

$$
E ^ {b} [ C ] = c p _ {1} ^ {F} + c p _ {2} ^ {F} + p _ {2} ^ {F} \int_ {c} ^ {\infty} (x - c) \pi (x) d x.
$$

The buyer will choose (b) if $E ^ { b } [ C ] \leq E ^ { a } [ C ]$ . Setting $p _ { 2 } ^ { S }$ to the highest possible value, $\begin{array} { r } { \mathrm { i . e . , } p _ { 2 } ^ { S } = r , } \end{array}$ and substituting into the above inequality (see page 2 of online supplement), we have

$$
c p _ {1} ^ {F} + p _ {2} ^ {F} \left(c + \int_ {c} ^ {\infty} (x - c) \pi (x) d x\right)
$$

$$
\leq r \left(c + \int_ {c} ^ {\infty} (x - c) \pi (x) d x\right).\tag{2}
$$

<sup>Lemma</sup> <sup>3.</sup> Assume that $p _ { 2 } ^ { S } = r$ is the real underlying price of the risk-free commodity $x - c .$ A buyer would choose to buy with the forward contract rather than build, $i f p _ { 1 } ^ { F } + p _ { 2 } ^ { F } \leq \check { r }$

<sup>Proof.</sup> Simplify constraint (2).

Under the assumption that $p _ { 2 } ^ { S } = r$ is the real underlying price of the risk-free commodity, the buyer’s unit cost for obtaining capacity c is what is expressed on the left-hand side of the inequality in Lemma 3. The reason is as follows. With the forward contract, the buyer commits to buying all of capacity c in both Periods 1 and 2 regardless of the demand distribution. A commitment of assuming all the risk and reward for capacity c is the same as that when the buyer builds c in Period 1. Thus, Lemma 3 states that if the cost of obtaining c via the forward contract is no greater than the building cost, the buyer would consider choosing the forward contract as opposed to building.

Thus, the seller has the following maximization problem:

$$
\begin{array}{l l} \text {max} & c p _ {1} ^ {F} + c p _ {2} ^ {F} + p _ {2} ^ {F} \int_ {c} ^ {\infty} (x - c) \pi (x)   d x \\ \text {s.t.} & c p _ {1} ^ {F} + p _ {2} ^ {F} \bigg (c + \int_ {c} ^ {\infty} (x - c) \pi (x)   d x \bigg) \\ & \leq r \bigg (c + \int_ {c} ^ {\infty} (x - c) \pi (x)   d x \bigg), \\ & p _ {1} ^ {F}, p _ {2} ^ {F} \leq r. \end{array}
$$

There are an infinite number of solutions for $p _ { 1 } ^ { F }$ and $p _ { 2 } ^ { F } .$ One possible solution is $p _ { 2 } ^ { F * } = r$ and $p _ { 1 } ^ { F * } = 0$ Table 1 compares the forward contract with the spot market in Period 1.

The maximum expected profit in Table 1 is the maximum amount that the seller can possibly obtain from that buyer, depending on how he sets the prices. The seller cannot do any better than earning that amount of profit because any expected profit better than that would imply that it then becomes more cost effective for the buyer to build as opposed to buying from the seller. Therefore, this is not an exact representation of the seller’s profit under that choice, but rather an upper bound on the possible profits to be had. Note that the seller’s maximum expected profits under the two scenarios are the same. This is because both profits are capped by the buyer’s expected cost of building. If the seller’s prices are any higher than that in Table 1, then the buyer will not buy. In that sense, the cost of building can be thought of as the buyer’s maximum willingness to pay. In the single-buyer case, the best the seller can do is to extract the largest surplus possible by pricing the resources to the highest amount the buyer would like to pay. However, in the multiple-buyer case, the buyers cannot be assumed to have identical demand distributions and building costs, and therefore the results can be quite different. Under uniform pricing, the seller cannot extract the entire surplus from every buyer. However, he can price his services such that the highest possible surplus is extracted from some, leaving the rest to choose the build option.

Table 1 Comparison of Spot Market with Forward Contract in Period 1

<table><tr><td></td><td>Spot market</td><td>Forward contract</td></tr><tr><td>Buyer&#x27;s expected cost if building by self</td><td> $rc + r \int_{c}^{\infty}(x - c)\pi(x)dx$ </td><td> $rc + r \int_{c}^{\infty}(x - c)\pi(x)dx$ </td></tr><tr><td>Pricing schemes</td><td> $p_{1}^{S*} = r \int_{0}^{c}\left(1 - \frac{x}{c}\right)\pi(x)dx,$  $p_{2}^{S*} = r$ </td><td> $p_{1}^{F*} = 0,\quad p_{2}^{F*} = r,\quad p_{2}^{S*} = r$ </td></tr><tr><td>Seller&#x27;s max expected profit</td><td> $rc + r \int_{c}^{\infty}(x - c)\pi(x)dx$ </td><td> $rc + r \int_{c}^{\infty}(x - c)\pi(x)dx$ </td></tr></table>

In Figure 3, the buyers are depicted by the circles and have different building costs. The higher up a buyer is in the figure, the greater is his building cost. The horizontal line showing the selected price separates the buyer population into two segments. For the ones above the line segment, buying is a better option. The ones that are slightly above the line segment are the ones from whom their entire surplus is extracted, whereas for those below the line segment, it is less expensive to build.

Instead of bearing all the risk as in the spot market, the seller uses the forward contract to hedge the risk due to market uncertainty by transferring the risk to the buyer. Under the forward contract, the buyer commits to buying the entire quantity demanded with a minimum purchase of c from the seller. Even if the demand in Period 2 is less than $c ,$ the buyer still has to buy the contracted amount. Whether the buyer chooses to buy commodity c at the real committed price $p _ { 1 } ^ { c } = { p _ { 1 } ^ { F * } } \dot { + } p _ { 2 } ^ { F * } = r$ under the forward contract or not therefore does not depend on his downside demand distribution. In the spot market, the seller charges a commitment price $p _ { 1 } ^ { c } \bar { = } p _ { 1 } ^ { S * } \leq r$ for commodity c in Period 1. The following formulation reflects the downside risk:

Figure 3 Surplus Extraction Under Buyers with Differing Building Costs  
```txt
Cost
Selected price
Potential buyers
Buyers not priced to their limits
Buyers from whom max surplus is extracted
Buyers choosing to build
```

$$
p _ {1} ^ {S *} = r \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x) d x.
$$

In the presence of a contract, however, the seller could charge a commitment price $p _ { 1 } ^ { c } = p _ { 1 } ^ { F * } + p _ { 2 } ^ { F * } = r$ in Period 1. $p _ { 1 } ^ { F * } + p _ { 2 } ^ { F * } = r$ is indifferent to the downside risk. The forward contract thus enables the seller to hedge the risk embedded in this commodity. The risk in commodity c is now borne by the buyer.

Note that in both the analysis for the spot market and the forward market, we do not consider the option of buying in Period 1 and building in Period $^ { 2 , }$ although for the sake of completeness we do include this option in the generalized model in §3.3. The spot and forward prices are less than the building cost in any period, and even though built capacity can be reused, we are only looking at two periods in our analysis, which results in closed-form solutions. Therefore, this option (Buy, Build) would be suboptimal to (Build, Buy) or (Buy, Buy). Although this option is technically feasible, however, because of its inferiority in terms of optimality, we do not consider that option in our model.

## 3.3. The Generalized Multiple-Buyer Model

Table 2 presents a list of the parameters in the model. The decision variables are the per-unit spot and forward prices.

The alternatives that are available to each buyer and the impact of each alternative on their costs are presented in Table 3. The impact on the seller’s revenue can be derived from the buyer’s cost function.

Table 2 List of Parameters and Variables

<table><tr><td colspan="2">Parameters</td></tr><tr><td> $I$ </td><td>Index set of buyers</td></tr><tr><td> $K$ </td><td>Index set of alternatives</td></tr><tr><td> $r_i$ </td><td>Per-unit building cost of Buyer  $i$ </td></tr><tr><td> $c_i$ </td><td>Capacity needed by Buyer  $i$  in Period 1 (known)</td></tr><tr><td> $X_i$ </td><td>Capacity needed by Buyer  $i$  in Period 2 (random variable)</td></tr><tr><td> $\pi_j(x_i)$ </td><td>Probability density function of Buyer  $i$  for capacity needed in Period 2</td></tr><tr><td> $U_i^k$ </td><td>Revenue generated from Buyer  $i$  under Alternative  $k$ </td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td> $p_{1i}^{Sk}$ </td><td>Spot price charged to Buyer  $i$  in Period 1 under Alternative  $k$ </td></tr><tr><td> $p_{2i}^{Sk}$ </td><td>Spot price charged to Buyer  $i$  in Period 2 under Alternative  $k$ </td></tr><tr><td> $p_{1i}^{Fk}$ </td><td>Forward price charged to Buyer  $i$  in Period 1 under Alternative  $k$ </td></tr><tr><td> $p_{2i}^{Fk}$ </td><td>Forward price charged to Buyer  $i$  in Period 2 under Alternative  $k$ </td></tr><tr><td> $v_i^k$ </td><td>Binary variable indicating whether Buyer  $i$  picked Alternative  $k$ </td></tr></table>

Table 3 Alternatives and Their Respective Costs on Each Buyer i

<table><tr><td>k</td><td>Period 1</td><td>Period 2</td><td>Cost to buyer</td></tr><tr><td>A</td><td>Build</td><td>Buy (spot)</td><td> $c_{i}r_{i} + p_{2}^{S}\int_{c_{i}}^{\infty}(x_{i} - c_{i})\pi_{i}(x_{i})dx_{i}$ </td></tr><tr><td>B</td><td>Buy (spot)</td><td>Buy (spot)</td><td> $c_{i}p_{1}^{S} + p_{2}^{S}\int_{0}^{\infty}x_{i}\pi_{i}(x_{i})dx_{i}$ </td></tr><tr><td>C</td><td>Buy (forward)</td><td>Buy (forward)</td><td> $c_{i}p_{1}^{F} + c_{i}p_{2}^{F} + p_{2}^{F}\int_{c_{i}}^{\infty}(x_{i} - c_{i})\pi_{i}(x_{i})dx_{i}$ </td></tr><tr><td>D</td><td>Build</td><td>Build</td><td> $c_{i}r_{i} + r_{i}\int_{c_{i}}^{\infty}(x_{i} - c_{i})\pi_{i}(x_{i})dx_{i}$ </td></tr><tr><td>E</td><td>Buy (spot)</td><td>Build</td><td> $c_{i}p_{1}^{S} + r_{i}\int_{0}^{\infty}x_{i}\pi_{i}(x_{i})dx_{i}$ </td></tr></table>

Additionally, all the integrals can be preprocessed, and therefore they serve as data in the seller’s expected revenue maximization problem (SERMax) below, which is a mixed-integer program:

$$
\max \sum_ {i \in I} \sum_ {k \in K} U _ {i} ^ {k}\tag{3}
$$

s.t.

$$
U _ {i} ^ {A} = p _ {2 i} ^ {S A} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{4}
$$

$$
c _ {i} p _ {1 i} ^ {F A} + c _ {i} p _ {2 i} ^ {F A} + p _ {2 i} ^ {F A} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
- p _ {2 i} ^ {S A} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \geq c _ {i} r _ {i} v _ {i} ^ {A} \quad \forall i \in I,\tag{5}
$$

$$
c _ {i} p _ {1 i} ^ {S A} + p _ {2 i} ^ {S A} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
- p _ {2 i} ^ {S A} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \geq c _ {i} r _ {i} v _ {i} ^ {A} \quad \forall i \in I,\tag{6}
$$

$$
r _ {i} v _ {i} ^ {A} \geq p _ {2 i} ^ {S A} \quad \forall i \in I,\tag{7}
$$

$$
c _ {i} p _ {1 i} ^ {S A} - p _ {2 i} ^ {S A} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} r _ {i} v _ {i} ^ {A} - r _ {i} v _ {i} ^ {A} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{8}
$$

$$
U _ {i} ^ {B} = c _ {i} p _ {1 i} ^ {S B} + p _ {2 i} ^ {S B} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{9}
$$

$$
c _ {i} r _ {i} v _ {i} ^ {B} \geq c _ {i} p _ {1 i} ^ {S B} + p _ {2 i} ^ {S B} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
- p _ {2 i} ^ {S B} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{10}
$$

$$
c _ {i} p _ {1 i} ^ {F B} + c _ {i} p _ {2 i} ^ {F B} + p _ {2 i} ^ {F B} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} p _ {1 i} ^ {S B} + p _ {2 i} ^ {S B} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{11}
$$

$$
c _ {i} r _ {i} v _ {i} ^ {B} + r _ {i} v _ {i} ^ {B} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} p _ {1 i} ^ {S B} + p _ {2 i} ^ {S B} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i} \quad \forall   i \in I,\tag{12}
$$

$$
r _ {i} v _ {i} ^ {B} \geq p _ {2 i} ^ {S B} \quad \forall i \in I,\tag{13}
$$

$$
U _ {i} ^ {C} = c _ {i} p _ {1 i} ^ {F C} + c _ {i} p _ {2 i} ^ {F C} + p _ {2 i} ^ {F C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\forall i \in I,\tag{14}
$$

$$
c _ {i} r _ {i} v _ {i} ^ {C} \geq c _ {i} p _ {1 i} ^ {F C} + c _ {i} p _ {2 i} ^ {F C} + p _ {2 i} ^ {F C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
- p _ {2 i} ^ {S C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{15}
$$

$$
c _ {i} p _ {1 i} ^ {S C} + p _ {2 i} ^ {S C} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} p _ {1 i} ^ {F C} + c _ {i} p _ {2 i} ^ {F C} + p _ {2 i} ^ {F C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{16}
$$

$$
c _ {i} r _ {i} v _ {i} ^ {C} + r _ {i} v _ {i} ^ {C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} p _ {1 i} ^ {F C} + c _ {i} p _ {2 i} ^ {F C} + p _ {2 i} ^ {F C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{17}
$$

$$
r _ {i} v _ {i} ^ {C} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} p _ {1 i} ^ {F C} + c _ {i} p _ {2 i} ^ {F C} + p _ {2 i} ^ {F C} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} - c _ {i} p _ {1 i} ^ {S C}
$$

$$
\forall i \in I,\tag{18}
$$

$$
U _ {i} ^ {D} = 0 \quad \forall i \in I,\tag{19}
$$

$$
p _ {2 i} ^ {S D} \geq r _ {i} v _ {i} ^ {D} \quad \forall i \in I,\tag{20}
$$

$$
c _ {i} p _ {1 i} ^ {F D} + c _ {i} p _ {2 i} ^ {F D} + p _ {2 i} ^ {F D} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} r _ {i} v _ {i} ^ {D} + r _ {i} v _ {i} ^ {D} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{21}
$$

$$
c _ {i} p _ {1 i} ^ {S D} + p _ {2 i} ^ {S D} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
\geq c _ {i} r _ {i} v _ {i} ^ {D} + r _ {i} v _ {i} ^ {D} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{22}
$$

$$
c _ {i} p _ {1 i} ^ {S D} \geq c _ {i} r _ {i} v _ {i} ^ {D} + r _ {i} v _ {i} ^ {D} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}
$$

$$
- r _ {i} v _ {i} ^ {D} \int_ {0} ^ {\infty} x _ {i} \pi_ {i} (x _ {i}) d x _ {i} \quad \forall i \in I,\tag{23}
$$

$$
U _ {i} ^ {E} = c _ {i} p _ {1 i} ^ {S E} \quad \forall i \in I,\tag{24}
$$

$$
p _ {1 i} ^ {S k}, p _ {2 i} ^ {S k}, p _ {1 i} ^ {F k}, p _ {2 i} ^ {F k} \leq M v _ {i} ^ {k} \quad \forall   i \in I,   k \in K,\tag{25}
$$

$$
\sum_ {k \in K} v _ {i} ^ {k} = 1 \quad \forall i \in I,\tag{26}
$$

$$
\sum_ {k \in K} p _ {1 i} ^ {S k} = \sum_ {k \in K} p _ {1 j} ^ {S k} \quad \forall   i \in I,   j \in I \backslash i,\tag{27}
$$

$$
\sum_ {k \in K} p _ {1 i} ^ {F k} = \sum_ {k \in K} p _ {1 j} ^ {F k} \quad \forall   i \in I,   j \in I \backslash i,\tag{28}
$$

$$
\sum_ {k \in K} p _ {2 i} ^ {S k} = \sum_ {k \in K} p _ {2 j} ^ {S k} \quad \forall   i \in I,   j \in I \backslash i,\tag{29}
$$

$$
\sum_ {k \in K} p _ {2 i} ^ {F k} = \sum_ {k \in K} p _ {2 j} ^ {F k} \quad \forall   i \in I,   j \in I \backslash i,\tag{30}
$$

$$
v _ {i} ^ {k} \in \{0, 1 \} \quad \forall i \in I, k \in K.\tag{31}
$$

The mixed-integer programming formulation (3)–(31) above maximizes the seller’s expected revenue, where each buyer has five alternatives with regard to obtaining their resources. $v _ { i } ^ { k }$ is a binary variable, which is one if Buyer i chooses alternative k and zero otherwise. Therefore, constraints (26) ensure that for each Buyer i exactly one alternative is selected. For a particular Buyer $i ,$ a specific $v _ { i } ^ { k }$ will be equal to one if and only if all the constraints pertaining to this binary variable are satisfied. For example, for a Buyer $i , \ \bar { v _ { i } ^ { A } }$ will be equal to one if and only if constraints (5)–(8) are satisfied. Basically, these constraints are comparing the costs (to the buyer) of every other alternative to alternative $\scriptstyle \mathbf { A } ,$ and thus $v _ { i } ^ { A }$ will be set to one if and only if the cost under A is the lowest. Alternative B will be chosen (and consequently, $v _ { i } ^ { B } = 1 )$ if constraints (10), (12), and (13) are satisfied. Alternative C will be chosen if constraints (15), (17), and (18) are satisfied. And lastly, alternative D will be chosen if constraints (20)–(23) are satisfied. Note that $v _ { i } ^ { E }$ will be one if and only if $v _ { i } ^ { k } = 0 , \forall k \in K \backslash \{ E \}$

$p _ { 1 i } ^ { S k }$ and $p _ { 2 i } ^ { S k }$ are the spot prices charged to Buyer i under alternative k. Likewise, $p _ { 1 i } ^ { F k }$ and $p _ { 2 i } ^ { F k }$ are the prices charged under the forward contract to i. Constraints (25) make sure that if an alternative k is not selected $\left( \mathrm { i . e . , ~ } v _ { i } ^ { k } = 0 \right)$ , then the corresponding prices $p _ { 1 i } ^ { S k } , p _ { 2 i } ^ { S k } , p _ { 1 i } ^ { F k }$ , and $p _ { 2 i } ^ { F k }$ are set to zero. M is a large number and can be set to max4r<sub>i</sub>5. Constraints (4), (9), (14), (19), and (24) are the revenue functions of the seller under the five alternatives. These constraints, along with constraints (25), will ensure that the appropriate revenue function is applied for Buyer i depending on the alternative. Note that if alternative B is not selected, constraint (11) is automatically satisfied because the corresponding prices are set to zero. Similarly, constraint (16) pertains to alternative C. Note that, due to constraint (25), the set $( p _ { 1 i } ^ { S k } , ~ p _ { 2 i } ^ { S k } , ~ p _ { 1 i } ^ { F k }$ and $p _ { 2 i } ^ { F k } )$ of prices can be greater than zero for exactly one k. Consequently, the seller’s revenue from all suboptimal alternatives for any given buyer becomes zero. Constraints (27)–(30) compare the spot and forward prices faced by each buyer with that of all other buyers, and thus ensure that the same spot and forward prices are charged to all buyers, regardless of the alternative most favorable for each buyer.

## 3.4. Analysis of Price Discrimination Strategies in Storage Grid Markets

We now discuss the efficacy of using first-degree price discrimination in the multiple-buyer storage grid market. The presumption of price discrimination is that the customer responds submissively to the price set by the seller and that the seller can identify the demand curve of the customer. In practice, however, especially when dealing with computing resources such as CPU time and storage, there is considerable and complex bargaining. Companies such as IBM and Akamai do practice price discrimination. However, there are noticeable administrative overheads associated with one-on-one iterative negotiations utilizing IT experts who analyze different aspects of the client’s business (Akamai 2009). In practical cases of price discrimination for computing resources, the clients are typically large in size, with multiyear contracts. Other buyers might prefer less negotiation effort, greater transparency in pricing, and a discomfort regarding the unknown in the negotiation process that has a perception of higher transaction cost (Kira 2009). In fact, all clients of Amazon S3 and Nirvanix are start-up firms whose small purchases pale in comparison to those of the clients of Akamai and IBM. Here we model the phenomenon of price discrimination, and we derive the conditions under which the different pricing strategies prevail.

For a single buyer, the seller charges the maximum amount, which can thus be seen as a trivial case of price discrimination. For multiple buyers, the seller solves the single-buyer problem for each and charges each buyer their maximum amount. In keeping with the current business practices in the computing resources domain, we introduce a parameter for transaction cost into the model. This transaction cost captures the overheads incurred by each party when negotiating a personalized price. Let $\theta$ and  be the transaction cost incurred by the seller and the buyer, respectively. We assume that this cost is only incurred once between the seller and each buyer. Then Buyer i’s cost and the seller’s revenue for the $\mathrm { f i v e ^ { 4 } }$ alternatives are given in Table 4. The buyer chooses the most cost-effective alternative. From Table $^ { 4 , }$ the maximum that the buyer would like to pay to the seller and the maximum revenue the seller could generate from each buyer are, respectively, reduced to

$$
\begin{array}{l} c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} - \lambda \quad \text { and } \\ c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} - \lambda - \theta . \end{array}
$$

For each client, the seller computes this maximum obtainable revenue. If

$$
c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i} - \lambda - \theta \geq 0,\tag{32}
$$

the seller sells to Buyer i at a total charge equal to the maximum the buyer is willing to pay. Otherwise, the seller would not have the incentive to serve this small customer.

Table 4 Alternatives and Their Respective Costs on Each Buyer i

<table><tr><td colspan="3">Alternatives</td><td rowspan="2">Cost to buyer</td><td rowspan="2">Revenue to the seller</td></tr><tr><td>k</td><td>Period 1</td><td>Period 2</td></tr><tr><td>A</td><td>Build</td><td>Buy (spot)</td><td> $c_{i}r_{i} + p_{2}^{S}\int_{c_{i}}^{\infty}(x_{i}-c_{i})\pi_{i}(x_{i})dx_{i}+\lambda$ </td><td> $p_{2}^{S}\int_{c_{i}}^{\infty}(x_{i}-c_{i})\pi_{i}(x_{i})dx_{i}-\theta$ </td></tr><tr><td>B</td><td>Buy (spot)</td><td>Buy (spot)</td><td> $c_{i}p_{1}^{S}+p_{2}^{S}\int_{0}^{\infty}x_{i}\pi_{i}(x_{i})dx_{i}+\lambda$ </td><td> $c_{i}p_{1}^{S}+p_{2}^{S}\int_{0}^{\infty}x_{i}\pi_{i}(x_{i})dx_{i}-\theta$ </td></tr><tr><td>C</td><td>Buy (forward)</td><td>Buy (forward)</td><td> $c_{i}p_{1}^{F}+c_{i}p_{2}^{F}+p_{2}^{F}\int_{c_{i}}^{\infty}(x_{i}-c_{i})\pi_{i}(x_{i})dx_{i}+\lambda$ </td><td> $c_{i}p_{1}^{F}+c_{i}p_{2}^{F}+p_{2}^{F}\int_{c_{i}}^{\infty}(x_{i}-c_{i})\pi_{i}(x_{i})dx_{i}-\theta$ </td></tr><tr><td>D</td><td>Build</td><td>Build</td><td> $c_{i}r_{i}+r_{i}\int_{c_{i}}^{\infty}(x_{i}-c_{i})\pi_{i}(x_{i})dx_{i}$ </td><td>0</td></tr><tr><td>E</td><td>Buy (spot)</td><td>Build</td><td> $c_{i}p_{1}^{S}+r_{i}\int_{0}^{\infty}x_{i}\pi_{i}(x_{i})dx_{i}+\lambda$ </td><td> $c_{i}p_{1}^{S}-\theta$ </td></tr></table>

For simplicity,  and  are assumed constant. For a client, if specific information is known, it is possible to identify the particular functional forms of  and $\lambda ,$ which could then be easily substituted into the discussion below. In a multiple-buyer market of set I, the seller’s total revenue is

$$
\sum_ {i \in I} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}\right) - | I | (\lambda + \theta).
$$

Let z<sup>∗</sup> = max $\textstyle \sum _ { i \in I } \sum _ { k \in K } U _ { i } ^ { k }$ in the SERMax MIP problem. Only when

$$
\sum_ {i \in I} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}\right) - | I | (\lambda + \theta) \geq z _ {I} ^ {*},\tag{33}
$$

where constraint (32) is met for all $i ,$ the seller gets more revenue from price discrimination. Otherwise, the seller is better off adopting a transparent price uniform to all buyers.

The number of buyers in the market could also have impact on the efficacy of using price discrimination in our setting. Rewriting condition (33),

$$
| I | \leq \frac {\sum_ {i \in I} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}\right) - z _ {I} ^ {*}}{\lambda + \theta}.\tag{34}
$$

Expression (34) implies that when the size of the market, I , is relatively small, the seller could generate more revenue by using price discrimination, whereas as I becomes large, the seller earns more by using transparent prices. This is consistent with current computing resource markets where businesses that practice price discrimination tend to cater to a much smaller group of large clients compared to Amazon, which has a large customer base of smaller clients (typically start-ups) and uses posted prices.

When an additional buyer joins this market, it may change the dynamics of the market, and price discrimination might not necessarily be favored over the public pricing policy, except under the following case when new Buyer j joins the market I:

$$
\sum_ {i \in I} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}\right) - z _ {I} ^ {*}
$$

$$
\leq \sum_ {i \in I \cup \{j \}} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}\right) - z _ {I \cup \{j \}} ^ {*},
$$

or

$$
\begin{array}{c} z _ {I \cup \{j \}} ^ {*} - z _ {I} ^ {*} \leq \sum_ {i \in I \cup \{j \}} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i})   d x _ {i}\right) \\ - \sum_ {i \in I} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i})   d x _ {i}\right), \end{array}
$$

or

$$
z _ {I \cup \{j \}} ^ {*} - z _ {I} ^ {*} \leq c _ {j} r _ {j} + r _ {j} \int_ {c _ {j}} ^ {\infty} (x _ {j} - c _ {j}) \pi_ {j} (x _ {j}) d x _ {j}.
$$

Otherwise, $z _ { I } ^ { * }$ cannot be the maximum value to the SERMax problem, which is a contradiction. After the growth in the market, the seller gets more revenue by price discriminating only when the following condition is still true:

$$
| I | + 1 \leq \frac {\sum_ {i \in I \cup \{j \}} \left(c _ {i} r _ {i} + r _ {i} \int_ {c _ {i}} ^ {\infty} (x _ {i} - c _ {i}) \pi_ {i} (x _ {i}) d x _ {i}\right) - z _ {I \cup \{j \}} ^ {*}}{\lambda + \theta}.
$$

Otherwise, the seller would be better off following a transparent pricing policy.

## 4. The Optimal Pricing Algorithm

The special structure of problem SERMax leads to an algorithm to derive the optimal set of spot prices with or without the seller’s offer of the corresponding forward prices. We first introduce the concept of decision rules that are used in the algorithm. Following this, we present the algorithm and discuss the construction of the efficient frontier of the risk-return trade-offs faced by the seller.

## 4.1. Decision Rules

The decisions faced by each Buyer i in each period can be encoded into four separate decision rules, as described in Table 5. $\phi _ { i , l } ( \cdot )$ is the price function that is evaluated under Rule l for Buyer i. (See the online supplement.)

Table 5 The Decision Rules for Buyer i

<table><tr><td>Rules (I)</td><td>Period</td><td>Actions</td><td>Function</td><td>Constant</td><td>Space</td></tr><tr><td>1</td><td>1</td><td>Spot, Build</td><td> $\phi_{i1}(\cdot)$ </td><td> $\Phi_{i1}=r_i$ </td><td> $(p_1^S,p_2^S)$ </td></tr><tr><td>2</td><td>2</td><td>Spot, Build</td><td> $\phi_{i2}(\cdot)$ </td><td> $\Phi_{i2}=r_i$ </td><td> $(p_1^S,p_2^S)$ </td></tr><tr><td>3</td><td>1</td><td>Contract, Build</td><td> $\phi_{i3}(\cdot)$ </td><td> $\Phi_{i3}=r_i$ </td><td> $(p_2^S,p_1^F,p_2^F)$ </td></tr><tr><td>4</td><td>1</td><td>Contract, Spot</td><td> $\phi_{i4}(\cdot)$ </td><td> $\Phi_{i4}=0$ </td><td> $(p_1^S,p_2^S,p_1^F,p_2^F)$ </td></tr></table>

Specifically, in Table 5,

$$
\begin{array}{c} \phi_ {i 1} (\cdot) = p _ {1} ^ {S} + \min \{p _ {2} ^ {S}, r _ {i} \} \bigg (1 - \int_ {0} ^ {c _ {i}} \bigg (1 - \frac {x _ {i}}{c _ {i}} \bigg) \pi_ {i} (x _ {i})   d x _ {i} \bigg), \\ \phi_ {i 2} (\cdot) = p _ {2} ^ {S}, \end{array}
$$

$$
\begin{array}{r l} & {\phi_ {i 3} (\cdot) = p _ {1} ^ {F} + p _ {2} ^ {F} \bigg (1 + \int_ {c _ {i}} ^ {\infty} \bigg (\frac {x _ {i}}{c _ {i}} - 1 \bigg) \pi_ {i} (x _ {i}) d x _ {i} \bigg)} \\ & {- \min \{p _ {2} ^ {S}, r _ {i} \} \int_ {c _ {i}} ^ {\infty} \bigg (\frac {x _ {i}}{c _ {i}} - 1 \bigg) \pi_ {i} (x _ {i}) d x _ {i},} \\ & {\phi_ {i 4} (\cdot) = \phi_ {i 3} (\cdot) - \min \{\phi_ {i 1} (\cdot), r _ {i} \}.} \end{array}
$$

Each price function is evaluated against a constant $\Phi _ { i , l }$ in order to determine the optimal action for that buyer. If $\phi _ { i , l } ( { \cdot } ) < \Phi _ { i , l } ,$ the former of the two relevant actions in the decision rule l is taken, the latter action is taken if $\phi _ { i , l } ( \cdot ) > \Phi _ { i , l } ,$ and the buyer is indifferent between the two actions otherwise. We introduce the following definition for this purpose.

<sup>Definition</sup> <sup>2.</sup> A decision line (or hyperplane) is where a buyer is indifferent between two actions within a particular period.

$\phi _ { i l } ( \cdot ) = \Phi _ { i l } , l = 1 , 2 , 3$ 1 4 are all decision lines. Figure 4 shows the buyer’s choice under different prices in a spot market under Rules 1 and 2 with decision lines $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$ and $\begin{array} { r } { \phi _ { i 2 } ( \cdot ) = \Phi _ { i 2 } , } \end{array}$ respectively. The hyperplane $\phi _ { i 3 } ( \cdot ) = \Phi _ { i 3 }$ for Rule 3 is shown in Figure 5 and has been drawn in space $( p _ { 2 } ^ { S } , p _ { 1 } ^ { F } , p _ { 2 } ^ { F } )$ Under Rule 3, the buyer can only choose between alternatives ${ \mathrm { A } } , \ { \mathrm { C } } ,$ and D. Below the hyperplane, $\mathrm { i . e . , }$ closer to the origin, the buyer chooses C. The decision rule for choosing between a spot and forward contract in Period 1 is Rule 4. In the proof

Figure 4 Optimal Choices Under Rules 1 and 2  
![](/api/attachments/BKFJXE3G/fulltext/images/12dcdf8d38b2e5eac54496ad1cf7ee7219ac331c59941839b421aabcc7d1e3ba.jpg)

Figure 5 Optimal Choices Under Rule 3  
![](/api/attachments/BKFJXE3G/fulltext/images/750eca6a60f7faf525fad98c56682e65d83d535fe21e620ca4329ea4a127e4d6.jpg)  
for Theorem $^ { 1 , }$ we show that if it is possible for the seller to achieve higher revenue by adding a forward contract to the spot market, there must exist a maximal pricing both on line $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$ for some i and on line $\phi _ { k 3 } ( \cdot ) = \Phi _ { k 3 }$ for some $k .$ . Then the price $( p _ { 1 } ^ { S } , p _ { 2 } ^ { S } , p _ { 1 } ^ { F } , p _ { 2 } ^ { F } )$ and the decision hyperplane $\dot { \phi _ { j 4 } ( \cdot ) } = \Phi _ { j 4 }$ can be reduced to the two-dimensional space. $( p _ { 2 } ^ { S } , p _ { 2 } ^ { F } \mid \phi _ { i 1 } ( . ) = \Phi _ { i 1 } , \phi _ { k 3 } ( . ) = \Phi _ { k 3 } )$ . Figures 6(a) and 6(b) illustrate an example.

In both Figures 6(a) and 6(b), the lines $\phi _ { j 1 } ( p _ { 2 } ^ { S } \mid$ $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 } \bar { ) = \Phi _ { j 1 } } ( \mathrm { o r } p _ { 2 } ^ { S } = \bar { p } _ { 2 } ^ { S } )$ and $\phi _ { j 2 } ( \cdot ) \stackrel { \cdot } { = } \Phi _ { j 2 }$ (or $p _ { 2 } ^ { S } = r _ { j } )$ divide the corresponding space into three areas pertaining to Buyer $ { \mathbf { \hat { \rho } } } _ { j ^ { \prime } \mathbf { s } }$ choices. Figure 6(b) illustrates which alternative buyer j chooses in each segment of $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$ when only spot prices are considered. Note that j does not choose alternative (E) in this example because the points on $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$ never enter the alternative (E) area for $j .$ Figure 6(a) shows what $j$ would choose when forward pricing is also considered. The two additional lines related to forward contract, $\phi _ { j 3 } ( p _ { 2 } ^ { S } , p _ { 2 } ^ { F } \mid \phi _ { k 3 } ( . ) = \Phi _ { k 3 } ) = \Phi _ { j 3 }$ and $\phi _ { j 4 } ( p _ { 2 } ^ { S } , p _ { 2 } ^ { F } \mid \phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 } , \phi _ { k 3 } ( \cdot ) = \Phi _ { k 3 } ) = \Phi _ { j 4 } ,$ are drawn in the space $( p _ { 2 } ^ { S } , p _ { 2 } ^ { F } \mid \phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 } , \phi _ { k 3 } ( \cdot ) = \Phi _ { k 3 } )$ in Figure $6 ( \mathsf { a } )$ . When the price of the forward contract, $\overset { \vartriangle } { \boldsymbol { p } _ { 2 } ^ { F } }$ , is so large that the pricing point is above $\phi _ { j 3 } ( p _ { 2 } ^ { S } , \bar { p } _ { 2 } ^ { F } \mid \phi _ { k 3 } ( . ) = \Phi _ { k 3 } ) = \Phi _ { j 3 }$ and $\phi _ { j 4 } ^ { - } ( \dot { p } _ { 2 } ^ { s } , p _ { 2 } ^ { F } \mid \phi _ { i 1 } ( \cdot ) =$ $\Phi _ { i 1 } ^ { ' } , \phi _ { k 3 } ( . ) = \Phi _ { k 3 } ) = \Phi _ { j 4 } ,$ then based on Rules 3 and $^ { 4 , }$ j would not prefer the forward contract and thus abide by his choice in Figure 6(b). Otherwise $, j$ would choose the forward contract. Further details are provided in the proof of Theorem 1 in the online supplement.

## 4.2. SERMax Algorithm

Step 1. Identify All the Critical Points:<sup>5</sup> Find all the critical points for a global maximum

## Figure 6 Two-Dimensional Space Illustration of Decision Rule 4

(a) Optimal choices under Rule 4  
![](/api/attachments/BKFJXE3G/fulltext/images/1637db6645536d987bb013e8a300608a9bd0e02046980622c674a84304bdeffc.jpg)

(b) j ’s choice on spot price at $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$  
![](/api/attachments/BKFJXE3G/fulltext/images/3830e01eafeb33f44e03040c54b35e9b3b1ecd53f13cc747fa48861caddc78d2.jpg)

Step 1.1. For the Spot Market: Find all the critical points $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } )$ in space $( p _ { 1 } ^ { S } , p _ { 2 } ^ { S } ) \colon$ : For each pair of $i , j , i , j = 1 , \dots , n ,$ obtain the critical points $( p _ { 1 } ^ { \bar { S } * } , p _ { 2 } ^ { S * } )$ on the intersections of $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$ with $\phi _ { i 1 } ( \cdot ) = \Phi _ { i 1 }$ $( i \neq j )$ and $\begin{array} { r } { \phi _ { j 2 } ( \cdot ) = \Phi _ { j 2 } , } \end{array}$ and with lines $p _ { 2 } ^ { S } = 0 .$ . (Note that $i , j$ in this step could be different from those in other steps.)

Step 1.2. For the Forward Contract: Find all the critical points $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } , p _ { 1 } ^ { F * } , p _ { 2 } ^ { F * } )$ :

Step 1.2.1. Derive Points that Achieve Greater Revenue than Spot Prices: For each combination of Buyers $i , j , j ^ { \prime }$ and $k , \ i , j , j ^ { \prime } , k = 1 , \dots , n ,$ obtain the critical points $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } , \dot { p } _ { 1 } ^ { F * } , p _ { 2 } ^ { F * } )$ on the intersections of $\hat { \phi } _ { j ^ { \prime } 4 } ( p _ { 2 } ^ { S } , p _ { 2 } ^ { \dot { F } } \stackrel {  } { | } \dot { \phi _ { i 1 } } ( \cdot ) = \stackrel {  } { \Phi _ { i 1 } } , \phi _ { k 3 } ( \cdot ) = \Phi _ { k 3 } ) =$ $\Phi _ { j ^ { \prime } 4 }$ with $\phi _ { j 1 } ( p _ { 2 } ^ { S } \mid \phi _ { i 1 } ( . ) = \Phi _ { i 1 } ) = \Phi _ { j 1 } , \phi _ { j 2 } ( . ) = \Phi _ { j 2 } ,$ $\dot { \phi _ { j 3 } } ( p _ { 2 } ^ { S } , p _ { 2 } ^ { F } \mid \dot { \phi _ { k 3 } } ( . ) = \Phi _ { k 3 } ) = \Phi _ { j 3 } ,$ and $\phi _ { j 4 } ( p _ { 2 } ^ { S } , \dot { p } _ { 2 } ^ { F } \mid \phi _ { i 1 } ( \cdot ) \dot { = }$ $\Phi _ { i 1 } , \phi _ { k 3 } ( \cdot ) = \Phi _ { k 3 } ) = \Phi _ { j 4 } ( j \neq j ^ { \prime } )$ and with line $p _ { 2 } ^ { S } = 0$ (Note that $i , j$ in this step could be different from those in other steps.)

Step 1.2.2. Derive Points that Do Not Reduce Revenue from that of Spot Prices: For each critical point c obtained from Step 1.1, for each pair of $i , j$ obtain the critical points $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } , p _ { 1 } ^ { F * } , p _ { 2 } ^ { F * } )$ on the intersections of $\phi _ { i 4 } ( p _ { 1 } ^ { F } , \bar { p } _ { 2 } ^ { F } \mid p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } ) = \Phi _ { i 4 }$ with $\phi _ { j 4 } ( p _ { 1 } ^ { F } , p _ { 2 } ^ { F } \mid p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } ) =$ $\Phi _ { j 4 }$ and with line $p _ { 2 } ^ { F } = 0$ . (Note that $i , j$ in this step could be different from those in other steps.)

Step 2. Calculate the Revenue: At each critical point, check each buyer’s choice and the seller’s related revenue: for each critical point $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } )$ (for without contract) or $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } , p _ { 1 } ^ { F * } , \mathsf { \bar { p } } _ { 2 } ^ { F * } )$ (for with contract), if this is a feasible price, find each buyer’s cost for each alternative. Then each buyer’s choice is the alternative under which the cost is minimal. If the buyer is indifferent among a set of alternatives, record them all.

Step 3. Find the Global Maximal Point: Obtain the maximum expected return from all buyers, $\scriptstyle \sum _ { i = 1 } ^ { n } E [ U _ { i } ]$ and its corresponding price $( p _ { 1 } ^ { S * } , p _ { 2 } ^ { S * } )$ (without forward contract) or $( p _ { 1 } ^ { \check { S } * } , \bar { p } _ { 2 } ^ { S * } , p _ { 1 } ^ { F * } , \bar { p } _ { 2 } ^ { F * } )$ (with forward), which is then the price to achieve global maximum revenue.

Note that the above algorithm provides the seller with the option of either obtaining prices for just the spot or both the spot and forward market. The latter would entail running the entire algorithm, whereas if the former is of interest, the seller should omit Step 1.2. Step 1.2 contains two substeps. We show in $\bar { \mathsf { S } } 5$ that the seller’s revenue will not be reduced by offering an appropriate forward contract to the spot market. Step 1.2.1 deals with the case when the revenue is increased and Step 1.2.2 when the revenue is not decreased. The two substeps are dealing with two different cases that might overlap. Theorem 1 below essentially proves that there exists a revenuemaximizing price vector amongst the critical points enumerated in the algorithm. Lemma 4 shows that the algorithm is polynomial in nature.

<sup>Theorem</sup> <sup>1.</sup> The SERMax algorithm yields a globally revenue-maximizing price vector.

<sup>Proof.</sup> See the online supplement.

<sup>Lemma</sup> <sup>4.</sup> The computational complexity of the algorithm for spot markets alone is $O ( n ^ { 2 } )$ . The computational complexity for forward contracts alongside spot markets is $O ( n ^ { 4 } )$ 0

<sup>Proof.</sup> See the online supplement.

## 4.3. Construction of the Efficient Frontier

The efficient frontier of the risk-return trade-offs for the different alternatives is obtained as follows. In Step 2, we add the following computations: Let $p _ { 2 , i }$ be the price that the seller charges for the downside risk from Buyer i. $p _ { 2 , i } = p _ { 2 } ^ { S * }$ if i chooses to buy in Period 2 from the spot market; $p _ { 2 , i } = 0$ otherwise. Let vector $P _ { 2 } c = \{ p _ { 2 , 1 } c _ { 1 } , \dots , p _ { 2 , n } c _ { n } \}$ . Let $\mathbf { d } _ { X / c }$ be the downside risk vector for demand vector $X _ { 1 } , \dots , X _ { n } .$ ${ \bf d } _ { X / c } = \{ d _ { X _ { 1 } / c _ { 1 } } , \dots , d _ { X _ { N } / c _ { N } } \}$ . The downside risk in the seller’s revenue is $d _ { G } ^ { \mathrm { ~ ~ } } = \mathbf { d } _ { X / c } ( P _ { 2 } c ) ^ { T }$ . Correspondingly, we add the following computations in Step 3: Plot $\textstyle ( \sum _ { i = 1 } ^ { n } E [ U _ { i } ] , d _ { G } )$ . The elements of the opportunity set contain all these points. The efficient frontier is the upper left envelope of the opportunity set.

## 5. Analysis of the Efficient Frontier

In this section, we develop an analysis of the seller’s risk-return trade-offs for the different strategies that are available to the buyers. Lemma 5 shows that in the one-buyer case, the efficient frontier comprises a single point. Specifically, alternatives B and C yield the same return (and at least as much as A, D, and E). However, C is preferred because its downside risk is zero.

<sup>Lemma</sup> <sup>5.</sup> The efficient frontier collapses to a single point for a single buyer.

<sup>Proof.</sup> See the online supplement.

We now demonstrate that the seller earns at least as much revenue from selling using a forward contract as he does when selling without. For tractable and meaningful analysis, we derive this in a two-buyer setting where each buyer faces the same per-unit building cost. In the absence of a forward contract, the optimal price to charge a buyer with parameters $c , X ,$ is

$$
\begin{array}{c} p _ {1} ^ {S *} = r \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x)   d x \quad \text { and } \\ p _ {2} ^ {S *} = r. \end{array}
$$

The buyer will not buy in Period 1 if the price is higher than the $p _ { 1 } ^ { S * }$ corresponding to his demand distribution. Thus, without the contract, the seller has two choices in the two-buyer case. One is to charge the higher $p _ { 1 } ^ { S } , \mathrm { i . e . , }$ getting the highest possible surplus from one buyer, while the other is forced to build. The alternative is to charge a lower $p _ { 1 } ^ { S }$ whereby both buyers would choose to buy. Here, the seller may have to forfeit portions of the surplus from one of the buyers. However, the seller can do better while still charging the same per-unit price to both buyers.

Suppose Buyer 1 follows the demand distribution specified thus far and assume that Buyer 1 is the price-setting buyer, i.e., in the absence of a forward contract, the per-unit prices are set as above.<sup>6</sup> Buyer 2’s demand distribution follows a similar structure as Buyer 1 with $c ^ { \prime }$ estimated demand in Period 1. Let X<sup>0</sup> denote Buyer 2’s demand variable in Period 2 with a probability density function $\pi ^ { \prime } ( x ^ { \prime } ) .$ $\textstyle \int _ { 0 } ^ { \infty } \pi ^ { \prime } ( x ^ { \prime } ) d x ^ { \prime } = 1$ . The costs and prices faced by Buyer 2 and the seller’s revenue from this buyer are shown in Table 6.

It can be shown that the seller earns higher revenues by selling the forward contract to Buyer 2 if

$$
\int_ {0} ^ {c ^ {\prime}} \left(1 - \frac {x ^ {\prime}}{c ^ {\prime}}\right) \pi^ {\prime} (x ^ {\prime}) d x ^ {\prime} \geq \int_ {0} ^ {c} \left(1 - \frac {x}{c}\right) \pi (x) d x.
$$

Table 6 Costs and Prices Related to Buyer 2

<table><tr><td></td><td>Without contract</td><td>With contract</td></tr><tr><td>Buyer 2&#x27;s building cost</td><td> $rc' + r \int_{c'}^{\infty} (x' - c') \pi'(x') dx'$ </td><td> $rc' + r \int_{c'}^{\infty} (x' - c') \pi'(x') dx'$ </td></tr><tr><td>Per-unit prices</td><td> $p_1^S = r \int_0^c \left(1 - \frac{x}{c}\right) \pi(x) dx$ , $p_2^S = r$ </td><td> $p_1^F = 0, \quad p_2^F = r, \quad p_2^S = r$ </td></tr></table>

We can see that this condition will always hold as long as the buyer chooses not to build as the new buyer is willing to buy when

$$
p _ {1} ^ {S} \leq r \int_ {0} ^ {c ^ {\prime}} \left(1 - \frac {x ^ {\prime}}{c ^ {\prime}}\right) \pi^ {\prime} (x ^ {\prime}) d x ^ {\prime}.
$$

Table 7 shows the decisions made by Buyer 2 (and the corresponding impact on the seller’s revenue) under the different circumstances in Period 1. In either case, the seller’s revenue is higher when selling the forward contract. Lemma 6 provides a more general result for multiple buyers and demonstrates an attractive property of the forward contract: even though a forward contract reduces the risk borne by the seller, it does not simultaneously reduce the return. The forward contract then is guaranteed to provide at least as much revenue as the spot market with lesser risk.

<sup>Lemma</sup> <sup>6.</sup> The seller will not suffer a reduction in revenue by introducing such a forward contract to the spot market if at least one buyer chooses to buy the forward contract.

<sup>Proof.</sup> See the online supplement.

Lemma 7 below applies to multiple buyers and shows that when buyers face same building costs, the efficient frontier collapses to a single point, and alternative C is still the preferred one. Thus, under certain conditions, the seller can get higher revenue by offering a forward contract as opposed to simply operating a spot market.

<sup>Lemma</sup> <sup>7.</sup> Under the assumption of uniform building cost, the efficient frontier is a single point, with the following prices as shown:

$$
\begin{array}{c} p _ {1} ^ {F *} = 0, \\ p _ {2} ^ {F *} = r, \\ p _ {1} ^ {S *} = r \int_ {0} ^ {c _ {i}} \left(1 - \frac {x _ {i}}{c _ {i}}\right) \pi_ {i} (x _ {i}) d x _ {i}, \\ p _ {2} ^ {S *} = r, \quad w h e r e \end{array}
$$

$$
\begin{array}{l} \int_ {0} ^ {c} \left(1 - \frac {x _ {i}}{c _ {i}}\right) \pi_ {i} (x _ {i}) d x _ {i} \\ = \max \left\{\int_ {0} ^ {c _ {j}} \left(1 - \frac {x _ {j}}{c _ {j}}\right) \pi_ {j} (x _ {j}) d x _ {j}, j = 1, \dots , n \right\}. \end{array}
$$

<sup>Proof.</sup> See the online supplement.

Table 7 Buyer 2’s Decisions and Impact on Seller’s Revenue

<table><tr><td rowspan="2"></td><td colspan="2">Without contract</td><td colspan="2">With contract</td></tr><tr><td>Buyer 2</td><td>Seller</td><td>Buyer 2</td><td>Seller</td></tr><tr><td> $\int_{0}^{c'} \left(1 - \frac{x'}{c'}\right) \pi'(x') dx' \geq \int_{0}^{c} \left(1 - \frac{x}{c}\right) \pi(x) dx$ </td><td>Buy</td><td>Unable to extract highest surplus, because the buyer is willing to pay more</td><td>Buy</td><td>Entire surplus obtained</td></tr><tr><td> $\int_{0}^{c'} \left(1 - \frac{x'}{c'}\right) \pi'(x') dx' < \int_{0}^{c} \left(1 - \frac{x}{c}\right) \pi(x) dx$ </td><td>Build</td><td>Unable to extract highest surplus. Earns revenue only if Period 2 demand is  $X' > c'$ .</td><td>Buy</td><td>Entire surplus obtained</td></tr></table>

## 6. Data Collection and Empirical Evaluation

We conducted an empirical study to compare the revenues generated under the different pricing strategies and evaluate the risk under each. Specifically, the objectives of our simulation study are as follows:

• To characterize the seller’s risk-return trade-off under the different alternatives by analyzing the efficient frontier;

• To determine which alternative yields the highest return for the seller and which one the lowest risk;

• To determine how the alternatives compare in terms of cost and risk borne by the buyers, especially vis-à-vis the baseline strategy of building own capacity. Is the buyer better off or worse off in terms of cost and risk when buying instead of building?

From publicly available information available on the Internet, we obtained the names of 37 Amazon S3 clients. We collected Internet traffic data for these clients and used it to estimate their storage demand. We also derived some estimates regarding the building costs faced by the clients. We then utilized the optimal algorithm presented in §4.2 to derive the optimal prices, and, correspondingly, the revenues generated under the different pricing strategies. The efficient frontier was also simultaneously constructed using the step in §4.3 to help us validate our theoretical results regarding the greater efficiency of the forward market in terms of reducing risk while not eroding revenues. In §6.1, we provide details of our Internet traffic data collection exercise from Alexa and Quantcast along with the assumptions made in the estimation process. Section 6.2 presents and interprets the simulation results.

## 6.1. Data Collection Methodology

The relevant data were collected for the May 5, 2007 to November 4, 2007 time frame. We randomly picked the end of the fourth day of each calendar month as the billing time. First, we estimated the total Internet traffic from Yahoo’s traffic information. We collected Yahoo’s monthly reach from Quantcast.com (Quantcast.com 2008) on November 6, 2007 and its number of page views per reach (averaged over three months) within November 4, 2007 from Alexa (Alexa.com 2008). Monthly reach implies the number of unique visitors to the site in a month. To derive the total Internet traffic, we assume that Yahoo’s daily reach and number of page views per reach remains constant over the period of our data collection exercise. We further assume that most of Yahoo’s users visit the website every day. Therefore, the monthly reach becomes equivalent to the daily reach. Note that these assumptions are reasonable because Yahoo is a popular portal, and as with most portals, its users tend to visit it everyday for the purpose of checking e-mails, news, weather, etc. We therefore estimated the total Internet traffic using Yahoo’s data using the formula in Table 8. Again, Yahoo’s data are important only for the purpose of deriving the total Internet traffic. To the best of our knowledge, Yahoo is not a client of Amazon S3, and therefore, we did not use Yahoo’s traffic data in our simulations. Second, we collected the data on percentage of page views and reach per day from Alexa for each of the 37 clients, as well as those of Yahoo. The traffic data for each of these clients are then estimated using the formula in Table 8.

Third, we estimated the daily storage demand for each client by studying the website of each to see how its storage demand is related to its business. We found that such demand is due either to users simply accessing the S3 clients’ Web pages or via a user’s subscription to the clients’ service (photo-sharing websites, blogs, etc.). Either some of the clients did not

## Table 8 Formula for Deriving Total Internet and S3 Clients Traffic Information

```txt
Yahoo's daily page views = Yahoo's daily reach
    × Yahoo's daily number of page views per reach
Total Internet daily reach = Yahoo's daily reach/Yahoo's daily reach
    (percentage).
Total Internet daily page views = Yahoo's daily page views/Yahoo's daily page views (percentage)
S3 Client's daily reach = Total Internet daily reach
    × Client's daily reach (percentage)
S3 Client's daily page views = Total Internet daily page views
    × Client's daily page views (percentage)
```

have a quota for each user or the quota was very large (and thus in essence nonbinding). For such clients, we related their storage demand to their page views. Such storage demand was estimated by assuming a fixed size for each page view for similar websites. Note that the size assumed for photo-sharing websites would be considerably larger than that assumed for websites hosting text blogs. Other clients sold fixed quota of workspaces for users to back-up files and share team objects. We related those clients’ storage demand to their specified quotas and their reaches. Then, for each website, we computed its monthly demand from its daily demand by means of weighted average, which is also adopted by Amazon S3.

Lastly, because building costs increase with increased usage, we assumed three different levels of per-unit building costs based on high-, medium-, and low-intensity usage levels and we applied the corresponding level to an S3 client based on its line of business. For instance, a team collaboration website would be a high-intensity firm, whereas a file backup site would be a low-intensity one. We obtained the building costs of three of Amazon S3 clients: the building costs of Mediasilo (Amazon.com 2008), SmugMug (SmugMug.com 2006a), and an unnamed S3 client (SmugMug.com 2006b) are, respectively, \$0.22/GB, \$0.284/GB, and \$0.51/GB. We used these as the means of low-, medium-, and high-intensity building costs, respectively, in our simulations. In the simulation, we generated the building cost of each client from a uniform distribution with the corresponding mean of its intensity level and range 6−50%1 50%7.

## 6.2. Empirical Study Results

We utilized the data collected in §6.1 to derive the simulation results for five two-month time windows in various scenarios. In each two-month window, the first month serves as Period 1 and the second month as Period 2. In each window, the demand in Period 2 is assumed to be unknown, and its distribution is estimated from that in Period 1. We studied the results from both the sellers’ and the buyers’ perspectives. Figures 7(a) and 7(b) compare the seller’s normalized expected revenues and risks across all five time windows. Using the benchmark case of Amazon S3’s current fixed-pricing policy for comparison, our analysis with 37 current clients indicates that spot markets alone can on average enhance revenues to Amazon by 41% while also increasing risks by 108%. On average, the first-period prices are 15% lower and the second-period prices are 124% higher than Amazon’s current price. This conforms to the theoretical analysis in §3, where in spot markets the seller sets lower prices in Period 1 to induce buying instead of building. This results in greater market share and, consequently, greater revenues for the seller. However, this increase comes at a cost such that the seller ends up assuming a greater portion of the market’s downside risk due to the increased volume sold in Period 1. Note that the downside risk is borne purely by the buyers when choosing to build. Next, we studied the effects of forward contracts. Our results show that on average forward contracts alongside the spot markets can reduce risks to Amazon by 57% and enhance revenues by 51%. These results support our theoretical analysis that the forward contracts hedge the risk for the seller while not reducing, and under certain circumstances even increasing, revenues. Note that when the seller moves from the fixed-pricing market to the spot market, the seller sees higher revenues, but at a higher risk. When we introduce the forward market into this spot market, it allows the seller to maintain, at the very least, these higher revenues, but now at a considerably lower risk.

Figures 7(c)–7(g) depict the efficient frontier for the five time windows obtained using the optimal algorithm in §§4.2 and 4.3 and show the normalized risk on the X-axis and the normalized return on the Y -axis. The efficient frontier in each of these cases shows that issuing the forward contract provides higher revenues with lower risk, as opposed to selling in a spot market only. Note that in the spot market, the revenues are appreciably poorer compared to the forward market for similar risk levels. Clearly, the seller can do better by providing the option of forward contracts to the buyers. Furthermore, note that in time windows 1, 4, and 5 the efficient frontier is a single point. This implies that given the demand distribution of the buyers in each of these time windows, it is optimal for the seller to set the spot prices comparatively higher than the forward prices, and therefore buyers are driven towards obtaining the forward contract. That is, it is optimal for the seller to use the forward contract as an instrument for not only reducing his risk but also maximizing his expected revenues.

Figures 7(h) and 7(i) present the buyers’ normalized average costs and downside risks under various scenarios to provide insights from the buyers’ perspective. Using nonexistence of storage grids as the base line for comparison, in terms of both costs and risks, the buyers are generally better off buying from the storage grids than building, regardless of the pricing strategy of the storage grid. The buyers’ average risks are decreased by 62%, 48%, and 24% by Amazon’s current fixed pricing, our proposed spot markets alone, and forward contracts alongside spot markets, respectively, and their costs are decreased by 26%, 15%, and 15% in those three scenarios, respectively. The latter two pricing strategies allow the seller to extract a greater amount of the buyers’ surplus.

Figure 7 Computational Results  
![](/api/attachments/BKFJXE3G/fulltext/images/cabac7bee8f2c6f3eaf5eb55574939f7bd26b2d96da5558cbf774a9afc6da7de.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/b4d01afcf81bb4c7f1dd0929b561afc45cd91d27c8f64c96f050f1166c6e0914.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/4d9684057ff02de4cde204f9989cae267d188f6765b297276923926525ceb253.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/4f4037d80864b5482dadf91644402d1e773a00837b20d8013c2cb16eb596d522.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/877b30c7cd5e4e30e119cbb36dff3d01de3b7a037f5d14e7871bc0ecb4bd48ec.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/e0879ad45854afb112a36a4c4a2e9c787bb385ce28740dedaf7ea3fd18d653ee.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/a23faa70891c22c5282f794a4b780b1d31a82ab9643d9e46643b2fb15d1e3b6c.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/4181c58abef085ec3cdaacaabc338e7c9e8be7fe2f33842c7edc866053986558.jpg)

![](/api/attachments/BKFJXE3G/fulltext/images/50934df79c303affe2abf0f2a062f372c257a9ade9b8b65757c0c060a8031583.jpg)

The implications of our simulation study are that a seller looking to increase revenues would do well by offering both a spot and a forward market, especially because the latter does not pay a price in terms of erosion of revenue as a result of risk reduction. Even by simply launching a spot market, the seller can realize higher revenues, but this alternative is attractive to the seller only if he does not mind the higher risk associated with this alternative. A buyer would be better off buying instead of building, irrespective of the storage grid’s pricing strategy. A cost-conscious buyer would be indifferent between the spot and forward markets, where both reduce the buyer’s risk when compared to building, although the reduction is slightly less under the forward market.

We also performed an empirical analysis using our data set over one period to evaluate the efficacy of using price discrimination. We found that when the transaction costs to derive a specific price for a specific client are above a certain level, the payoff of this effort may not contribute to increasing the seller’s total revenue. Only if the transaction cost of each buyer is less than a certain amount can the seller gain by price discriminating across all buyers. In all our experiments, transaction costs need to be extremely small so that the seller could gain more revenue by price discrimination instead of public pricing. Complete details of this analysis can be found in the online supplement, along with an expanded review of the price discrimination practices in computing and e-commerce.

Finally, in order to show how our analysis can be extended beyond two periods, we transformed the two-period optimal algorithm to fit three and four periods. Following the same demand assumption as in the two-period problem, we assume that the demand in Period 1 is known, whereas for Periods 2, 3, and 4 only the demand distributions are known. A for-

Figure 8 Efficient Frontier of the Three-Period Problem  
![](/api/attachments/BKFJXE3G/fulltext/images/06cdaefdb030cbf3162ad2cd64714be30d19275d13842e9c1ca07916a616c399.jpg)  
ward contract can be entered into only in Period 1 and includes purchases in Periods 2, 3, and 4. We ran a simulation with the three-period algorithm for two markets—one with a single buyer and another with five buyers. We used the three-period optimal algorithm and demonstrated how the efficient frontier can be derived. The results are shown in Figure 8. In the onebuyer case, the forward contract can hedge some but not all of the seller’s risk, because in the three-period problem, there is opportunity risk both for selling in Period 1 and in Period 2, and the forward contract designed in this case can hedge the former, but not the latter. In general, when more periods are considered, the original forward contract designed for the twoperiod problem could hedge the risk in the next period. A simple extension of the two-period optimal algorithm to the three-period case causes a drastic worsening of solution time. Therefore, for the simulation of the four-period case, we modeled the revenue maximization problem in a manner similar to the MILP in §3.3 with 307 sets of constraints and ran it on LINGO for five buyers instead of using the optimal algorithm devised and shown in the online supplement.<sup>7</sup> We thus obtained the revenue-maximizing price vector as follows: \$0.02, \$0.1, \$0.04, and \$0.32 were the spot prices in Periods 1, 2, 3, and 4, respectively, whereas \$0.04, \$0.2, \$0, and \$0 were the forward prices in Periods 1, 2, 3, and 4, respectively, with the optimal revenue being \$2,815.39. Complete details of this analysis can be found in the online supplement.

![](/api/attachments/BKFJXE3G/fulltext/images/f0f8c4ef2070bddd7f44bdc0e35c7ba8e624d8a65c4065f155305b081ca9ee3e.jpg)

## 7. Conclusions and Future Research

We highlighted the different strategies available to buyers of storage: building own infrastructure versus buying from an online storage provider. For the latter, we proposed a spot market and a forward market and we show, both analytically and computationally, that both of these provide higher revenues than the simple posted pricing policy of charging the same price in each time period. In fact, in the absence of a forward market, the seller bears the risk arising out of any demand uncertainty. Forward contracts allow the seller to hedge this risk with the buyers, from whom the risk actually emanates. We model the seller as a price setter and his expected revenue-maximizing problem is modeled as a mixed-integer program.

We exploit the special structure of the problem to devise an algorithm that generates a globally revenuemaximizing forward and spot price vector in polynomial time. We perform a simulation study using data from Alexa and Quantcast to derive revenues under different pricing strategies and to compare risk-return trade-offs. Our analytical results show that forward contracts do not reduce seller’s revenue, while lowering risk (i.e., hedging against uncertainty in future revenues) and increase seller’s revenue under certain conditions. Our computational study confirms these results and shows a stronger result—that a spot and forward market on average enhance revenues by 41% and 51%, respectively, and the latter reduces risks by 57% as opposed to the benchmark case of Amazon S3’s current pricing policy.

Future research may consider issues such as incorporating quality of service metrics, studying the topographical dispersion of user demand and the utilization of this information in deriving a prioritybased pricing scheme. Here, we derive spot and forward prices only for storage, but Amazon S3 also sells bandwidth with separate upload and download charges. An interesting research study could involve the joint derivation of spot and forward prices of both storage and bandwidth. Lastly, note that our research can be extended to the study of call center operations serving multiple companies. Such operations also face demand uncertainty, and forward contracts can be used to hedge against such uncertainty.

## 8. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Acknowledgments

The authors thank the senior editor, the associate editor, and all the anonymous reviewers for their valuable comments that have significantly enhanced the paper.

## References

Akamai. 2009. Akamai’s netstorage services: Outsourced service to ease cost of storing content. http://www.akamai.com/html/ technology/products/netstorage.html.

Alexa.com. Alexa the Web information company. Accessed 2008. http://www.alexa.com.

Amazon.com. 2008. Success stories. http://www.amazon.com/ Success-Stories-AWS-home-page/b/ref=sc\_fe\_l\_1\_3435361\_5/ 104-1585210-549543?ie=UTF8&node=182241011&no=3435361 &me=A36L942TSJ2AJA.

Bapna, R., S. Das, R. Garfinkel, J. Stallaert. 2008. A market design for grid computing. INFORMS J. Comput. 20(1) 100–111.

Bapna, R., S. Das, R. Day, R. Garfinkel, J. Stallaert. 2011. A clock-andoffer auction market for grid resources when bidders face stochastic computational needs. INFORMS J. Comput. 23(4) 630–647.

Brooke, J., M. Foster, S. Pickles, K. Taylor, T. Hewitt. 2000. Mini-grids: Effective test-beds for grid application. Proc. 1st IEEE/ACM Internat. Workshop Grid Comput. (GRID 2000), Bangalore, India.

Buyya, R. 2002. Economic-based distributed resource management and scheduling for Grid computing. Ph.D. thesis, Monash University, Melbourne, Australia.

Cocchi, R., S. Shanker, D. Estrin, L. Zhang. 1993. Pricing in computer networks: Motivation formulation, and example. IEEE/ACM Trans. Networking 1(6) 617–627.

Cooper, B., H. Garcia-Molina. 2002. Bidding for storage space in a peer-to-peer data preservation system. Proc. 22nd Internat. Conf. Distributed Comput. Sytems (ICDSC 2002), Vienna, 372–381.

Du, Y. A., X. Geng, R. D. Gopal, R. Ramesh, A. B. Whinston. 2008. Capacity provision networks: Foundations of markets for sharable resources in distributed computational economies. Inform. Systems Res. 19(2) 144–160.

Frey, J., T. Tannenbaum, M. Livny, I. Foster, S. Tuecke. 2002. Condor-G: A computation management agent for multiinstitutional grids. Cluster Comput. 5(3) 237–246.

Heiser, G., F. Lam, S. Russell. 1998. Resource management in the mungi single-address-space operating system. Proc. Australasian Comput. Sci. Conf., Perth, Australia.

Huhns, M., L. Stephens. 2000. Multiagent systems and societies of agents. G. Weiss, ed. Multiagent Systems. MIT Press, Cambridge, MA, 79–120.

Kira, A. 2009. Cloud computing, transaction costs, and avoiding the salesperson. Alex Kira’s Blog, http://alexkira.blogspot.com/ 2009/01/cloud-computing-transaction-costs-and.html.

Lalis, S., A. Karipidis. 2000. JAWS: An open market-based framework for distributed computing over the Internet. Proc. 1st IEEE/ACM Internat. Workshop Grid Comput. (GRID 2000), Springer-Verlag, London, 35–45.

Lazar, A., N. Semret. 1997. Auctions for network resource sharing. Technical Report CV/CTR/TR 468-97-02, Columbia University, New York.

Miller, M., K. Drexler. 1998. Markets and computation: Agoric open systems. B. Huberman, ed. The Ecology of Computation. Elsevier Science Publishers, Amsterdam, 133–176.

Nirvanix.com. Enterprise cloud storage: Nirvanix public hybrid private clouds. Accessed 2008, http://www.nirvanix.com/.

Quantcast.com. How do you collect your data? Accessed 2008, http://www.quantcast.com/faq.jsp#How\_do\_you\_collect\_your \_data.3F.

Sairamesh, J., J. Kephart. 1998. Price dynamics of vertically differentiated information markets. Proc. 1st Internat. Conf. Inform. Comput. Economies, Charleston, SC.

Smith, R., R. Davis. 1980. The contract net protocol: High level communication and control in a distributed problem solver. IEEE Trans. Comput. C-29(12) 1104–1113.

SmugMug.com. 2006a. Amazon S3: Show me the money. Smug-Mug’s Don MacAskill (blog), November 10, http://blogs .smugmug.com/don/2006/11/10/amazon-s3-show-me-the -money/.

SmugMug.com 2006b. Amazon S3: Show me the money: Comments by J. S. SmugMug’s Don MacAskill (blog), November 10, http://blogs.smugmug.com/don/2006/11/10/amazon-s3 -show-me-the-money/#comment-549.

Staimer, M. 2008. The compelling price/performance economics of the Nirvanix storage delivery network versus in-house storage. Report (June 11), http://www.nirvanix.com/pdfs/Nirvanix \_vs\_In-house\_Storage.pdf.

Stonebraker, M., R. Devine, M. Kornacker, W. Litwin, A. Pfeffer, A. Sah, C. Staelin. 1994. An economic paradigm for query processing and data migration in Mariposa. Proc. 3rd Internat. Conf. Parallel Distributed Inform. Systems, IEEE Computer Society, Los Alamitos, CA, 58–67.

Waldspurger, C., T. Hogg, B. Huberman, J. Kephart, W. Stornetta. 1992. Spawn: A distributed computational economy. IEEE Trans. Software Engrg. 18(2) 103–117.

## CORRECTION

In this article, “Risk Management and Optimal Pricing in Online Storage Grids” by Sanjukta Das, Anna Ye Du, Ram Gopal, and R. Ramesh (first published in Articles in Advance, June 14, 2010, Information Systems Research, DOI:10.1287/isre.1100.0288), in-text citations for Figures 5(a) and 5(b) have been corrected to refer to Figures 6(a) and 6(b).
