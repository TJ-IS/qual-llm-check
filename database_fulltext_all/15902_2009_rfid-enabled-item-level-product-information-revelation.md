---
otero_id: 15902
otero_key: "5R6D5AW4"
title: "RFID-enabled item-level product information revelation"
authors: "Wei Zhou; Gaurav Kapoor; Selwyn Piramuthu"
year: "2009"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2009.45"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# RFID-enabled item-level product information revelation

Wei Zhou<sup>1,3</sup>, Gaurav Kapoor<sup>2</sup> and Selwyn Piramuthu<sup>2,3</sup>

<sup>1</sup>Information Systems and Technologies, ESCP Europe, France; <sup>2</sup>Information Systems and Operations Management, University of Florida, U.S.A.; <sup>3</sup>RFID European Lab @ ESCP-Europe.

Correspondence: Selwyn Piramuthu, Wei Zhou, Information Systems and Technologies, ESCP Europe, 75543 Paris cedex 11. France. Tel: þ 1-352-392-8882; E-mail: wzhou@escpeurope.eu

## Abstract

We consider a homogeneous product market and the incentive for oligopolists to share item-level product information with their customers. Enabled by Radio Frequency Identification technology, each firm has the option to record and reveal item-level information of a proportion of its products. We consider a two-stage game where each firm first decides its production plan and then determines its level of information revelation. With a constant clearance discount rate, we derive pure strategy equilibria that are subgame perfect and demonstrate that complete information sharing is the unique Nash equilibrium for the game when the common demand is volatile and that no information revelation is the unique Nash equilibrium when demand is not volatile. Furthermore, we show that the Nash equilibrium is the same with a decreasing clearance discount rate and that neither complete information revelation nor zero information revelation is consistent with an equilibrium with an increasing discount rate. Results are similar in a duopoly non-homogeneous product market scenario.

doi:10.1057/ejis.2009.45; published online 10 November 2009

Keywords: RFID; item-level information; information revelation; information sharing

## Introduction

Thanks to modern identification (ID) track and trace storage and retrieval technology such as Radio Frequency Identification (RFID), business practitioners are able to obtain and record item-level product information on any product. By acknowledging the individual quality disparity even within a bin of homogeneous products, firms are faced with the decision on whether to share this item-level product information with their buyers. In a monopolist’s market scenario, the clear choice for the firm is not to reveal this information. However, because revealing product information generates competitive advantage and possibly could increase sales, it may not necessarily be true in an oligopolists’ market.

We investigate the incentives for item-level information sharing from firms to consumers in a market with duopolists selling homogeneous products. In contrast to earlier work (e.g., Novshek & Sonnenschein, 1982; Vives, 1984; Gal-or, 1985) where information sharing is about unknown common demand, or (e.g., Gal-or, 1986) where information is about unknown private costs, we consider the information transmission of itemlevel product information that is enabled by modern information tracing technologies such as RFID.

RFID-embedded tracking systems use tags (silicon chips implanted in a product or its packaging) to communicate and share information about the tagged object with a reader. RFID tags can be used to store and retrieve product information at an item level in a way that is fully automatic, instantaneous, and touchless and could be used to track and trace any object. Despite its limited processing power and storage capacity, the item-level information it can store is dramatically higher than those using competing technologies such as bar code (Piramuthu, 2007). Unlike bar code that provides categorical-level information, RFID technology facilitates distinguishing individual instances of products by assigning a unique electronic product code to each of them. While there are certainly limitations associated with RFID implementations such as security and privacy issues, issues related to infrastructure, and read rate accuracy, several studies have attempted to address these issues (e.g., Kapoor et al., 2008; Piramuthu, 2008; Sundaram et al., 2008; Tu et al., 2009).

Although technology such as the RFID item-level price tag with electronic display that was introduced in 2008 (e.g., Zhou et al., 2008a), has enabled item-level product information revelation, it is only a matter of time before it gains widespread attention from both researchers and business practitioners. Given a choice, it is obvious that customers often pick and choose only those items that they perceive to have ‘better’ quality. For example, in grocery stores where fruits such as bananas are sold in an open basket, customers always pick the ‘good’ bananas and leave those they perceive to be of (relatively) inferior quality in the basket. We consider the consumer market for large screen flat TV and find that there exists a large quality variance even among the same brand/model TV such as the number of dead pixels (dps) (e.g., 0 dp – 25 dps) and the locations of dps (e.g., center and edge). Clearly, if retailers of consumer electronics reveal detailed item-level information on large screen TV, we most likely would observe similar results as bananas in grocery store baskets.

As a matter of fact, retailers (Zhou et al., 2008a) and manufacturers (Zhou et al., 2008b) are able to provide item-level information for most of their products in a way that is automatic and instantaneous. Consumers are also able to read such information through new technology, such as RFID-embedded item-level price tags or RFIDready cell phones. Although bar codes can be used to provide item-level product information, it needs direct line-of-sight to be read and cannot be understood without a reader. Moreover, although feasible, it is extremely cumbersome to enable bar codes to provide item-level information, Reusable RFID price tag with electronic display, on the other hand, is able to display selected product and pricing information. With so many options to deal with additional information, we are faced with very realistic questions such as (a) whether retailers/ manufacturers will benefit from revealing such information, (b) if so, to what extent, and (c) what strategy should be followed to share item-level information when the market is crowded. To answer these questions, we need to first re-examine the traditional definition of homogeneous product to account for the presence of additional item-level information. A homogeneous product is defined traditionally as a product from an industry in which outputs from different firms are indistinguishable. Even when two products are labeled to be homogeneous, they are most likely not perfect clones of each other. More precisely, the term ‘homogeneous’ should be used to describe a group of products that follow a certain statistical criteria, which is pre-defined by an industry to conform to certain standardizations. Quality variance of different homogeneous products differs by a wide margin depending on the industry. If item-level product information is available, it brings additional value to the buyer by providing the opportunity to choose better products and making better control decisions (Zhou, 2009). Other benefits include location tracking, inventory monitoring, etc. (Gaukler et al., 2007).

Under such a scenario, a firm might enjoy a better market position by virtue of possessing the ability to reveal item-level product information by selling more of its above-average products than his competitors. This dynamic is especially salient when supply exceeds anticipated common demand. In this paper, we assume that firms don’t manipulate or selectively reveal informa tion although it is doable and beneficial to the firms under certain circumstances (e.g., Crawford & Sobel, 1982; Greezy, 2005). A buyer always benefits from additional information afforded by the choice to pick the best above-average products (Blackwell, 1953).

The remainder of this paper is organized as follows. The next section presents a brief overview of relevant literature. The subsequent section includes information about the model description, assumptions and setup. Derivation of equilibria is presented in the next following section, along with related analysis. The penultimate section considers the scenario with non-homogeneous products. The final section concludes the paper with a brief discussion on the insights garnered and their implications.

## Literature review

The economic aspects of information sharing have long been studied and, moreover, it is generally believed that an increase in useful information results in generating positive value (Blackwell, 1953). Eckwert & Zilcha (2001), however, show that under certain circumstances Blackwell theorem fails completely in exchange economies. They show that the Blackwell theorem holds in competitive equilibrium with risk averse consumers and risk neutral producers given that risk-sharing markets are absent. When risk-sharing markets are present, all agents may become worse off with better information.

Crawford & Sobel (1982) develop a model of strategic information transmission in which an informed agent transmits information (possibly noisy) to the principal who takes an action that determines the welfare of both. They show that the principal’s equilibrium expected utility rises when the agent’s preferences are more similar, assuming that the principal bases his choice of action on rational expectations. Okuno-Fujiwara et al. (1990) analyze the problem of strategic information revelation, assuming agents may reveal some or all of their information to the principal prior to playing the game. They use the equilibria resulting from various revelation strategies to determine equilibrium revelation of information and to find sufficient conditions for complete revelation of all private information.

We consider strategic item-level product information transmission from the firm to the consumer, facilitated by modern tracing technology such as RFID. Most literature in oligopoly game theory with strategic information transmission deal with information associated with non-public information on common demand (e.g., Gal-or, 1985) or unknown private costs $( \mathrm { e . g . }$ , Gal-or, 1986). We assume that the information sender doesn’t manipulate the information nor does he selectively choose information within a certain range in his favor. Krishna & Morgan (2001) study the model of expertize in which perfectly informed experts, who are biased, transmit information to a decision maker whose action decides the welfare of all and show that the expert withholds sizable information from the decision maker in a one-expert scenario. Greezy (2005), in his discussion of deception in information transmission, shows that the average person prefers not to lie and by doing so increases his payoff only by a little but greatly reduces the other’s payoff. In this study, we don’t consider the moral games that have previously been studied.

The research question in this paper stems from the fact that RFID, as an emerging tracing and ID technology, has numerous advantages compared to traditional bar codes. However, the exact benefits of RFID in retailing and supply chain management haven’t been very clear since its introduction during WWII. Most existing literature in the area of RFID applications are case studies or simulations of domain-specific possible RFID implementations, mostly in the fields of inventory management and replenishment, supply chain operations, and retailing. Lee & Ozer (2005) investigate the value of RFID in a supply chain. Dutta, Lee, & Whang (2007) examine three dimensions of the value proposition of RFID. Gaukler et al. (2007) study item-Level RFID in the Retail Supply Chain. Alexander, Birkhofer, Gramling, Kleinberger, Leng, Moogimane, & Woods (2002), based on business case study of current leading practices for the adoption of Auto-ID system, illustrate the impact of Auto-ID system on specific pain points faced by companies in the consumer goods and retail value chain.

## The model

We consider a market consisting of two firms, each producing (or acquiring) a homogeneous product. The demand function facing this industry is stochastic and linear:

$$
P = A - Q - e\tag{1}
$$

The prior distribution of $e ,$ which is independent and with mean zero, is known to both firms. e may follow a different distribution according to the market characteristics of the modeled industry. $Q = Q _ { 1 } + Q _ { 2 } ,$ where $Q _ { i } ( i = 1 , 2 )$ denotes the quantity produced by firm i.

$$
E (P) = A - Q\tag{2}
$$

At the beginning of a time period, each firm decides the product acquisition/manufacturing plan for quantity (Q ) and the proportion of the products with item-level information $( \theta _ { i } )$ revealed. The number of RFID-tagged units is, therefore, $\theta _ { i } Q$ and the number of units without tags is $( 1 - \theta _ { i } ) Q$ . Tags with item-level information can no longer be placed once the product has passed the manufacturing (acquisition) stage. We assume the cost of tagging to be negligible. It is a reasonable assumption given the unit cost of RFID to be 10 cents compared to a \$10 bottle of shampoo or a \$500 computer. We also assume that all the buyers are rational and buy the best product that is available.

At the end of the time period, the actual demand is realized and both firms may over-sell or under-sell. If a firm has unsold product, $h _ { i } Q _ { i } ,$ , where $h _ { i }$ denotes the proportion of unsold product to the total amount produced, it clears out the unsold with a discount rate $\xi , \xi \in ( 0 , 1 )$ ). We may also consider the discount rate as the liquidation cost for unsold products. The discount rate differs under different business scenario where the rate could be constant, decreasing or increasing. For example, the liquidation cost of unsold perishable food for a grocery store is simply the lump sum cost of disposing unsold food no matter how much is disposed. The cost to dispose unsold electronic goods such as computers in an electronic store increases in regards to the volume, especially when the value of the goods depreciates quickly. Overall the discount rate varies in different industries, and this could be determined by the volume of unsold goods, the capacity of the firm, and the characteristics of industry, $\xi = k h _ { i } ,$ or $\zeta = 1 - k h _ { i }$

We model the system as a two-stage game. At the first stage each firm makes its manufacturing or acquisition plan. At the second stage each firm decides how much item-level information should be revealed. The level of information revelation is chosen dependent upon the output plan and the distribution of the common demand. We derive pure strategy Nash equilibria that are subgame perfect and investigate the incentives to share item-level product information in possible scenarios such as non-constant discounting rate and nonsymmetric product quality distribution.

The incentives for revealing item-level information are investigated when the dynamic of common demand ranges from extreme volatility to freezingly stable. We demonstrate that complete information revelation $( { \theta _ { i } } ^ { \star } { = } 1 , i { = } 1 , 2 )$ is a dominant strategy when demand is volatile and no information sharing $( { \theta _ { i } } ^ { \star } { = } 0 , i { = } 1 , 2 )$ is a dominant strategy when demand is not volatile.

## Summary:

1. There are two players in the market – Duopoly.

2. Products are homogeneous and have the same statistical characteristics.

3. At the beginning of a time period, each player i(i ¼ 1, 2) decides the product acquisition/manufacturing plan for quantity (Q ) and the proportion of the products with item-level information $( \theta _ { i } )$ revealed, so the number of tagged units equals $\theta _ { i } Q$ and the number of units without tags equals $( 1 - \theta _ { i } ) Q .$ Tags with item-level information can no longer be placed once the product is acquired/manufactured. Product per unit cost is denoted as $C _ { i } .$ Cost of tagging is assumed to be negligible.

4. The price is set as a function of expected accumulated demand $\scriptstyle P = A - \sum _ { i } Q _ { i }$ considering unsold product discount. Accumulated demand in a time period is statistically known to both the players. The actual accumulated demand by the end of a time period may be different from the expectation and follows a certain distribution. In other words, we assume that with probability p the demand will be $( 1 - \beta ) ( Q _ { 1 } + Q _ { 2 } )$ and $1 { - } p$ the demand will be $( 1 + \beta ) ( Q _ { 1 } + Q _ { 2 } )$

5. At the end of a time period, if there are unsold products, unsold products $q _ { i } ( i = 1 , 2 )$ will be cleared out with a discount x.

6. Consumer behavior: Customers buy the best aboveaverage product with known-item-level information first. If all the above-average RFID-tagged products are sold out, customers buy the untagged products until they are sold out. If both the above-average tagged and the untagged products are sold out, the customers will buy the best of the below average tagged ones.

Assumptions:

\- The cost of search is negligible. For instance, assume that the two firms are online retailers so customers’ search cost is minimal.

\- Customers have no prior preference on retailers.

\- Tagging cost is negligible.

## Derivation of the equilibria

At the Nash equilibrium, the strategy of each firm consists of an output level and an amount of information to be revealed, namely the pair $\left\{ Q _ { i } , \theta _ { i } \right\}$

where $\theta _ { i } \in [ 0 , \ 1 ]$ and $Q _ { i } \geqslant 0$ . The payoff function for firm i is

$$
\begin{array}{c} \pi_ {i} (Q _ {i},   \theta_ {i}) = [ Q _ {i} - p (1 - \xi) h _ {i} (Q _ {i},   \theta_ {i}) Q _ {i} ] \\ [ A - (Q _ {i} + Q _ {j} ^ {*}) ] - C _ {i} Q _ {i} \end{array}\tag{3}
$$

where $h _ { i } ( Q _ { i } , \theta _ { i } )$ denotes the proportion of player i’s unsold product and $\xi$ denotes the clearance discount rate. The unsold proportion of firm $i \prime s$ output is

$$
h _ {i} = \left\{ \begin{array}{l l} \frac {\theta_ {i} \beta (Q _ {i} + Q _ {j})}{(Q _ {i} \theta_ {i} + Q _ {i} \theta_ {j})} & \text { I. } \beta (Q _ {1} + Q _ {2}) \leqslant \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \\ \frac {\theta_ {j} Q _ {j} - \theta_ {i} Q _ {j} + \theta_ {i} \beta (Q _ {i} + Q _ {j})}{\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}} & \text { III. } Q _ {1} + Q 2 - \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \leqslant \beta (Q _ {1} + Q _ {2}) \\ \frac {(1 - \theta_ {i}) \beta (Q _ {i} + Q _ {j}) + \frac {1}{2} Q _ {j} (\theta_ {i} - \theta_ {j})}{(1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j}) Q _ {j}} & \text { II.otherwise } \end{array} \right.\tag{4}
$$

The unsold portion of firm $j ^ { \prime } s$ output is

$$
(\beta - h _ {i}) \frac {Q _ {i}}{Q _ {j}} + \beta\tag{5}
$$

Firm i chooses its decision rule $\theta _ { i } ( \cdot )$ and subsequently $Q _ { i } ( \cdot )$ to maximize (3), given decision rules chosen by the other firms. The quantity/information pair $\{ ( Q _ { 1 } ^ { ~ \star } , ~ \theta _ { 1 } ^ { ~ \star } )$ $( Q _ { 2 } ^ { \star } , \theta _ { 2 } ^ { \star } ) \}$ } is a Nash equilibrium if for each firm $i , ( Q _ { i } ^ { \star } , \theta _ { i } ^ { \star } )$ solves

$$
\max _ {0 \leqslant Q _ {i} <   \infty ; 0 \leqslant \theta_ {i} \leqslant 1} \pi_ {i} [ (Q _ {i}, \theta_ {i}), (Q _ {j} ^ {*}, \theta_ {j} ^ {*}) ]\tag{6}
$$

$$
\max _ {0 \leqslant Q _ {i} <   \infty ; 0 \leqslant \theta_ {i} \leqslant 1} [ Q _ {i} - p (1 - \xi) h _ {i} (Q _ {i}, \theta_ {i}) Q _ {j} ] [ A - (Q _ {i} + Q _ {j} ^ {*}) ] - C _ {i} Q _ {i}\tag{7}
$$

Theorem 1 If the clearance discount rate is constant and $\scriptstyle { \beta < { \frac { 1 } { 2 } } , }$ the unique Nash equilibrium of the two stage game is $\theta _ { i } { } ^ { \star } = O$ and $Q _ { i } { } ^ { \star } = A / 3 + ( C _ { j } { - } 2 C _ { i } ) /$ $3 [ 1 - p ( 1 - \xi ) \beta ] .$

Proof The first order condition on $\theta _ { i }$ is

$$
\begin{array}{l} \frac {\partial \pi_ {i} [ (Q _ {i} , \theta_ {i}) , (Q _ {j} ^ {*} , \theta_ {j} ^ {*}) ]}{\partial \theta_ {i}} = - p (1 - \xi) Q _ {i} \\ [ A - (Q _ {i} + Q _ {j} ^ {*}) ] \partial h _ {i} / \partial \theta_ {i} \end{array}\tag{8}
$$

Under condition I:

$$
\beta (Q _ {1} + Q _ {2}) \leqslant \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2})\tag{9}
$$

Player i’s unsold portion of his product is

$$
h _ {i} = \frac {\theta_ {i} \beta (Q _ {i} + Q _ {j})}{(Q _ {i} \theta_ {i} + Q _ {j} \theta_ {j})}\tag{10}
$$

$$
\frac {\partial h _ {i}}{\partial \theta_ {i}} = \frac {Q _ {j} ^ {*} \theta_ {j} ^ {*} \beta (Q _ {i} + Q _ {j} ^ {*})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {2}} > 0\tag{11}
$$

The payoff function is a strictly decreasing function of $\theta _ { i \cdot }$ Hence under condition $I , \theta _ { i } { } ^ { \star } = 0$ is a dominant strategy for each firm.

Under condition II:

$$
\begin{array}{l} Q _ {1} + Q _ {2} - \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \geqslant \beta (Q _ {1} + Q _ {2}) \\ \geqslant \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \end{array}\tag{12}
$$

player i’s unsold portion is

$$
h _ {i} = \frac {(1 - \theta_ {i}) \beta (Q _ {i} + Q _ {j}) + \frac {1}{2} Q _ {j} (\theta_ {i} - \theta_ {j})}{(1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j}) Q _ {j}}\tag{13}
$$

$$
\frac {\partial h _ {i}}{\partial \theta_ {i}} = \frac {(1 - \theta_ {j} ^ {*}) Q _ {j} [ - \beta (Q _ {i} + Q _ {j} ^ {*}) + \frac {1}{2} Q _ {j} ^ {*} + \frac {1}{2} Q _ {i} ]}{[ (1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} ] ^ {2}}\tag{14}
$$

The payoff function is a strictly decreasing function of $\theta _ { i } \operatorname { i f } \beta < { \frac { 1 } { 2 } }$ . Hence in condition $\operatorname { I I } , \theta _ { i } ^ { \star } = 0$ is also a dominant strategy for each firm.

The first order condition on $Q _ { i }$ is

$$
\frac {\partial \left[ \left[ Q _ {i} - p (1 - \xi) \beta Q _ {i} \right] \left(A - Q _ {i} - Q _ {j} ^ {*}\right) - C _ {i} Q _ {i} \right]}{\partial Q _ {i}} = 0
$$

$$
Q _ {i} = \frac {A - Q _ {j} ^ {*}}{2} - \frac {C _ {i}}{2 [ 1 - p (1 - \xi) \beta ]}\tag{15}
$$

Through a similarly procedure for firm j we have

$$
Q _ {j} = \frac {A - Q _ {i} ^ {*}}{2} - \frac {C _ {j}}{2 [ 1 - p (1 - \xi) \beta ]}\tag{16}
$$

Therefore,

$$
Q _ {i} ^ {*} = \frac {A}{3} + \frac {C _ {j} - 2 C _ {i}}{3 [ 1 - p (1 - \xi) \beta ]}\tag{17}
$$

$$
Q _ {j} ^ {*} = \frac {A}{3} + \frac {C _ {i} - 2 C _ {j}}{3 [ 1 - p (1 - \xi) \beta ]}\tag{18}
$$

&

According to the Theorem 1 no information revelation is a dominant strategy for each firm when the volatility of the common demand is low.

Theorem 2 If the clearance discount rate is constant and $\beta > \frac { 1 } { 2 } ,$ the unique Nash equilibrium of the two stage game is ${ \theta _ { i } } ^ { \star } = 1$ and Q \* ¼ A/3 þ (C 2C )/ 3[1p(1x)b].

Proof Under condition II:

When $\beta \geqslant { \frac { 1 } { 2 } } .$ , the first order condition on $\theta _ { i }$ is strictly decreasing, according to (12). Hence ${ \theta _ { i } } ^ { \star } = 1$ is a dominant strategy for each firm.

Under condition III:

$$
Q _ {1} + Q _ {2} - \frac {1}{2} \left(\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}\right) \leqslant \beta \left(Q _ {1} + Q _ {2}\right)\tag{19}
$$

Player i’s unsold portion is

$$
h _ {i} = \frac {\theta_ {j} Q _ {j} - \theta_ {i} Q _ {j} + \theta_ {i} \beta (Q _ {i} + Q _ {j})}{\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}}\tag{20}
$$

$$
\frac {\partial h _ {i}}{\theta_ {i}} = \frac {\theta_ {j} Q _ {j} [ (- 1 + \beta) (Q _ {i} + Q _ {j}) ]}{(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ^ {2}}\tag{21}
$$

the first order condition on $Q _ { i }$ is

$$
\frac {\partial \left[ \left[ Q _ {j} - p (1 - \xi) \beta Q _ {i} \right] \left(A - Q _ {j} - Q _ {j} ^ {*}\right) - C _ {i} Q _ {i} \right]}{\partial Q _ {j}} = 0
$$

$$
Q _ {i} = \frac {A - Q _ {j} ^ {*}}{2} - \frac {C _ {i}}{2 [ 1 - p (1 - \xi) \beta ]}\tag{22}
$$

Similarly for firm j

$$
Q _ {j} = \frac {A - Q _ {i} ^ {*}}{2} - \frac {C _ {j}}{2 [ 1 - p (1 - \xi) \beta ]}\tag{23}
$$

Therefore,

$$
Q _ {i} ^ {*} = \frac {A}{3} + \frac {C _ {j} - 2 C _ {i}}{3 [ 1 - p (1 - \xi) \beta ]}\tag{24}
$$

$$
Q _ {j} ^ {*} = \frac {A}{3} + \frac {C _ {i} - 2 C _ {j}}{3 [ 1 - p (1 - \xi) \beta ]}\tag{25}
$$

&

Theorem 2 shows that complete information revelation is a dominant strategy for each firm when the volatility of the common demand is high.

Theorem 3 When $\beta < \frac { 1 } { 2 } , \ i f \ ( \ni \xi ) / ( \widehat { \Theta } h ) < 0 ,$ , the unique Nash equilibrium of the game is ${ \theta _ { 1 } } ^ { \star } = { \theta _ { 2 } } ^ { \star } = 0 ,$ , if (qx)/ $( \widehat { \mathrm { O } } h ) > 0 ,$ , there exists no equilibrium where ${ \theta _ { \cal I } } ^ { \star } { = } { \theta _ { \cal 2 } } ^ { \star } { = } { \theta } { \in } { \cal { I } } { { \cal 0 } } , 1 J .$

Proof When the clearance discount rate decreases with the quantity of unsold product, we model it as a linear function with $h _ { i }$ such as $\{ \xi = 1 - k h _ { i } \colon \xi \in ( O , 1 ) \}$ where k is a constant with $k h _ { i } \in ( O , 1 )$ . The first order condition on $\theta _ { i }$ becomes

$$
\begin{array}{c} \frac {\partial \pi_ {i} [ (Q _ {i} , \theta_ {i}) , (Q _ {j} ^ {*} , \theta_ {j} ^ {*}) ]}{\partial \theta_ {i}} = - p [ A - (Q _ {i} + Q _ {j} ^ {*}) ] \\ 2 k Q _ {i} h _ {i} h _ {i} ^ {\prime} \end{array}\tag{26}
$$

where $p { \geqslant } 0 , A { - } ( Q _ { i } { + } Q _ { j } { ^ { \star } } ) { \geqslant } 0$ and $h _ { i } { \geqslant } 0$ . When $\beta < \frac { 1 } { 2 } ,$ ,we have $h _ { i } ^ { \prime } > 0$ and $h _ { i } \geqslant 0$ . So the equilibria on information sharing is ${ \theta _ { i } } ^ { \star } \mathrm { = } { \theta _ { j } } ^ { \star } \mathrm { = } 0$

If the clearance discount rate increases with the quantity of unsold product, $\{ \xi = k h _ { i } \colon \xi \in ( 0 , 1 ) \}$ }. The first order condition on $\theta _ { i }$ is

$$
\begin{array}{c} \frac {\partial \pi_ {i} [ (Q _ {i} , \theta_ {i}) , (Q _ {j} ^ {*} , \theta_ {j} ^ {*}) ]}{\partial \theta_ {i}} = - p [ A - (Q _ {i} + Q _ {j} ^ {*}) ] \\ h _ {i} ^ {\prime} (1 - 2 k h _ {i}) \end{array}\tag{27}
$$

And the second order condition is

$$
\begin{array}{c} \frac {\partial^ {2} \pi_ {i} [ (Q _ {j} , \theta_ {i}) , (Q _ {j} ^ {*} , \theta_ {j} ^ {*}) ]}{\partial \theta_ {i} ^ {2}} = - p [ A - (Q _ {i} + Q _ {j} ^ {*}) ] \\ [ h _ {i} ^ {\prime \prime} - 2 k (h _ {i} ^ {\prime \prime} h _ {i} + h _ {i} ^ {\prime} 2) ] <   0 \end{array}\tag{28}
$$

$$
\begin{array}{c} \partial h _ {i} / \theta_ {i} = \frac {Q _ {j} ^ {*} \theta_ {j} ^ {*} \beta (Q _ {i} + Q _ {j} ^ {*})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {2}} > 0 \\ \frac {\partial^ {2} h _ {i}}{\theta_ {i} ^ {2}} = \frac {- Q _ {i} Q _ {j} ^ {*} \theta_ {j} ^ {*} \beta (Q _ {i} + Q _ {j} ^ {*}) (Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {4}} <   0 \end{array}
$$

Thus, $h _ { i } = 1 / ( 2 k )$ maximizes firm’s payoff function. Now let’s assume there exists an equilibrium and $h _ { i } \neq \beta ,$ then $h _ { i } { = } 1 / ( 2 k )$ is the necessary condition for a unique equilibrium for firm i. Following the same procedure we can obtain the necessary condition for firm j. Then we have $h _ { i } Q _ { i } + h _ { j } Q _ { j } = 1 / ( 2 k ) \quad ( Q _ { i } + Q _ { j } ) = \beta ( Q _ { i } + Q _ { j } ) ,$ which signifies $1 / ( 2 k ) = \beta$ or $h _ { i } = \beta ,$ , which contradicts the assumption.

In contrast to the case when the clearance discount rate is decreasing, completely reveal product information or reveal nothing is not necessarily a dominant strategy when clearance discount rate is an increasing function of the proportion of unsold product.

Theorem 4 When $\beta > \frac { 1 } { 2 } , ~ i f ~ ( \ni \xi ) / ( \ni h ) \leqslant O ,$ , the unique Nash equilibrium of the game is $\theta _ { \boldsymbol { { \cal { I } } } } { } ^ { \star } = \theta _ { 2 } { } ^ { \star } = \theta _ { 2 } { } ^ { \star } = { \cal { I } } ,$ if $( \widehat { \sf { O } } \xi ) / ( \widehat { \sf { O } } h ) > 0 ,$ , there exists no equilibrium where ${ \theta _ { 1 } } ^ { \star } { = } { \theta _ { 2 } } ^ { \star } { = } { \theta } { \in } [ 0 , 1 J .$

Proof When $\beta > \frac { 1 } { \gamma } , h ^ { \prime } _ { i } < 0 ,$ , so the first order derivative on the payoff function is positive $i f \left( \widehat { 0 } \xi \right) / ( \widehat { 0 } h ) \leqslant O$ according to (24). Therefore, the unique Nash equilibria is ${ \theta _ { i } } ^ { \star } = { \theta _ { j } } ^ { \star } = 1 .$

When $\beta > \frac { 1 } { 2 } ,$ we find that qp $i [ ( { \mathrm { Q } } _ { i } , { \theta } _ { i } ) , ( { \mathrm { Q } } _ { j } ^ { \star } , { \theta } _ { j } ^ { \star } ) ] / { \alpha \theta } _ { i } = 0$ if

$$
\begin{array}{c} h _ {i} = \frac {1}{2 k} \\ \Rightarrow \frac {\theta_ {j} ^ {*} Q _ {j} ^ {*} - \theta_ {i} Q _ {j} ^ {*} + \theta_ {i} \beta (Q _ {i} + Q _ {j} ^ {*})}{\theta_ {i} Q _ {i} + \theta_ {j} ^ {*} Q _ {j} ^ {*}} = \frac {1}{2 k} \end{array}\tag{29}
$$

$$
\Rightarrow \theta_ {i} = \frac {(1 - 2 k) \theta_ {j} ^ {*} Q _ {j} ^ {*}}{2 k \beta (Q _ {i} + Q _ {j} ^ {*}) - 2 k Q _ {j} ^ {*} - Q _ {i}}
$$

Similarly,

$$
\theta_ {j} = \frac {(1 - 2 k) \theta_ {i} ^ {*} Q _ {i} ^ {*}}{2 k \beta (Q _ {j} + Q _ {i} ^ {*}) - 2 k Q _ {i} ^ {*} - Q _ {j}}
$$

Following a similar proof procedure as in Theorem $^ { 3 , }$ we can show that $h _ { i } = h _ { j } = 1 / ( 2 k )$ contradicts the existence of a unique Nash equilibrium. &

Proposition 1 When $( \widehat { \sf { O } } \xi ) / ( \widehat { \sf { O } } h ) > { \cal { O } } ,$ neither complete nor zero information revelation is consistent with an equilibrium.

This proposition naturally follows from the results in Theorems 3 and 4.

Theorem 5 Theorems 1–4 are true if quality information is not symmetrically distributed.

Proof If the quality of both firms’ product is asymmetric distributed, we denote the $\sigma _ { i }$ as the proportion of firm i’s below average product. The unsold proportion can be derived as

$$
\widetilde {h} _ {i} = \left\{ \begin{array}{l l} \frac {\sigma_ {i} \theta_ {i} \beta (Q _ {i} + Q _ {j})}{(Q _ {i} \theta_ {i} \sigma_ {i} + Q _ {j} \theta_ {j} \sigma_ {j})} & \text { I. } \beta (Q _ {1} + Q _ {2}) \leqslant \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \\ \frac {\sigma_ {j} \theta_ {j} Q _ {j} - \sigma_ {i} \theta_ {i} Q _ {j} + \sigma_ {i} \theta_ {i} \beta (Q _ {i} + Q _ {j})}{\theta_ {i} Q _ {j} \sigma_ {i} + \theta_ {j} Q _ {j} \sigma_ {j}} \text { III. } Q _ {1} + Q _ {2} - \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \leqslant \beta (Q _ {1} + Q _ {2}) \\ \frac {(1 - \theta_ {i} \sigma_ {i}) \beta (Q _ {i} + Q _ {j}) + \frac {1}{2} Q _ {j} (\theta_ {i} \sigma_ {i} - \theta_ {j} \sigma_ {j})}{(1 - \theta_ {i} \sigma_ {i}) Q _ {i} + (1 - \theta_ {j} \sigma_ {j}) Q _ {j}} & \text { II.otherwise } \end{array} \right.\tag{30}
$$

Replacing $\theta _ { i }$ by $\tilde { \theta } _ { i } = \theta _ { i } \sigma _ { i } ,$ we find that it’s indeed the same expression as in the symmetric case. &

## Non-homogeneous product

In this section, we examine the game between two competing firms selling non-homogeneous products that are substitutable. We model this as a Bertrand game using price instead of quantity as decision variable. The strategy of each firm consists of its price and the proportion of information to reveal, namely the pair $\{ P _ { i } , \theta _ { i } \}$ . The output plan is determined by the estimated common demand as

$$
Q _ {i} (P _ {i}, P _ {j}) = A - P _ {i} + b P _ {j}\tag{31}
$$

The payoff function of firm i is

$$
\pi_ {i} (P _ {i}, \theta_ {i}) = [ Q _ {i} - p (1 - \xi) h _ {i} (P _ {i}, \theta_ {i}) ] P _ {i} - C _ {i} Q _ {i}\tag{32}
$$

Firm i chooses its decision rule $P _ { i } ( \cdot )$ and subsequently $\theta _ { i } ( \cdot )$ to maximize (29), given decision rules chosen by the other firms. The price/information pair $\{ ( P _ { 1 } ^ { \star } , \theta _ { 1 } ^ { \star } )$ $( P _ { 2 } ^ { \star } , \theta _ { 2 } ^ { \star } ) \}$ is a Nash equilibrium if for each firm $i , ( P _ { i } { ^ { \star } } , \theta _ { i } { ^ { \star } } )$ solves

$$
\max _ {0 \leqslant p _ {i} <   \infty ; 0 \leqslant \theta_ {i} \leqslant 1} \pi_ {i} [ (P _ {i}, \theta_ {i}), (P _ {j} ^ {*}, \theta_ {j} ^ {*}) ]\tag{33}
$$

$$
\max _ {0 \leqslant Q _ {i} <   \infty ; 0 \leqslant \theta_ {i} \leqslant 1} [ Q _ {i} - p (1 - \xi) h _ {i} (P _ {i}, \theta_ {i}) ] P _ {i} - C _ {i} Q _ {i}\tag{34}
$$

Theorem 6 Theorems 1–5 are true for duopoly in a nonhomogeneous product market.

Proof

$$
\begin{array}{c} \pi_ {i} (P _ {i}, \theta_ {i}) = [ Q _ {i} - p (1 - \xi) h _ {i} (P _ {i}, \theta_ {i}) ] P _ {i} - C _ {i} Q _ {i} \\ = [ A - P _ {i} + b P _ {j} - p (1 - \xi) h _ {i} (P _ {i}, \theta_ {i}) ] \\ P _ {i} - C _ {i} (A - P _ {i} + b P _ {j}) \end{array}
$$

The first order derivative on $\theta _ { i }$ is

$$
\frac {\partial \pi_ {i}}{\partial \theta_ {i}} = - p (1 - \xi) P _ {i} \frac {\partial h _ {i}}{\theta_ {i}}\tag{35}
$$

Since $h _ { i } ( \theta _ { i } )$ follows the same expression that we derived in the previous section, we can prove the same theorems with non-homogeneous product in a similar manner as described before.

## Concluding remarks

Modern tracing technology such as RFID has made it possible to reveal item-level information of almost any product in any industry. We investigate the incentives to reveal such information in a competing market dealing with a homogeneous product. We find that it pays for firms to completely reveal information if the common demand is volatile. If the demand is stable, however, it’s worse off if competing firms reveal any of their product information. This result applies if the unsold product clearance discount rate is constant or decreasing. If the discount rate increases with the number of unsold products, neither complete nor zero information revelation is consistent with an equilibrium for both firms. We also find that the above findings apply even if the item-level information is not symmetrically distributed.

## About the authors

Wei Zhou received his Ph.D. in Information Systems from the University of Florida. He is Assistant Professor of Information Systems and Technologies and a member of the RFID European Lab at ESCP Europe. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. Gaurav Kapoor received his Ph.D. in Information Systems from the University of Florida. His research interests include RFID systems.

## References

ALEXANDER K, BIRKHOFER G, GRAMLING K, KLEINBERGER H, LENG S, MOOGIMANE D and WOODS M (2002) Focus on retail: applying auto-ID to improve product availability at the retail shelf. MIT Auto-ID Center, 1 June 2002.

BLACKWELL D (1953) Equivalent comparisons of experiments. The Annals of Mathematical Statistics 24(2), 265–272.

CRAWFORD VP and SOBEL J (1982) Strategic information transmission. Econometrica 50(6), 1431–1451.

DUTTA A, LEE H.L and WHANG S (2007) RFID and operations management: technology, value and incentives. Production and Operations Management 16(5), 646–655.

ECKWERT B and ZILCHA I (2001) The value of information in production economies. Journal of Economic Theory 100(1), 172–186.

GAL-OR E (1985) Information sharing in oligopoly. Econometrica 53(2), 329–343.

GAL-OR E (1986) Information transmission – Cournot and Bertrand equilibria. The Review of Economic Studies 53(1), 85–92.

GAUKLER GM, SEIFERT RW and HAUSMAN WH (2007) Item-level RFID in the retail supply chain. Production and Operations Management 16(1), 65–76.

G U (2005) Deception: The role of consequences. American Economic Review 95(1), 384–394.

K G, Z W and P S (2008) RFID and information security in supply chains. In Proceedings of the The 4th International Conference on Mobile Ad-hoc and Sensor Networks (MSN’08), 59–62. IEEE Press.

KRISHNA V and MORGAN J (2001) A model of expertise. The Quarterly Journal of Economics 116(2), 747–775.

The analysis presented here leaves unanswered many interesting questions in the field of item-level information revelation and sharing. One interesting problem in signaling is a firm’s best information transmission strategy if it can selectively reveal information to maximize its own utility.

As an immediate extension to this paper, we are working on the games of information revelation in a horizontally and vertically differentiated market. This research also has wide applications in supply chain management when unsold merchandize are usually stored in inventory for use in the next period rather than simply being cleared out at a discount.

## Acknowledgements

The authors thank the anonymous reviewers, Associate Editor, and Editor for their helpful suggestions.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida. He is a member of the RFID European Lab at ESCP Europe. His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and financial credit-risk analysis.

LEE H and OZER O (2007) Unlocking the true value of RFID. Production and Operations Management 16(1), 40–64.

NOVSHEK W and SONNENSCHEIN H (1982) Fulfilled expectations Cournot duopoly with information acquisition and release. Bell Journal of Fconomics 13. 214-218.

OKUNO-FUJIWARA M, POSTLEWAITE A and SUZUMURA K (1990) Strategic information revelation. Review of Economic Studies 57, 2547.

PIRAMUTHU S (2007) Protocols for RFID tag/reader authentication. Decision Support Systems 43(3), 897–914.

PIRAMUTHU S (2008) Adaptive framework for collisions in RFID tag identification. Journal of Information & Knowledge Management 7(1), 9–14.

SUNDARAM D, PIENAAR S and PIRAMUTHU S (2008) Web services based workflow architecture for RFID applications using service chains. In Proceedinas of the 5th International Conference on Service Systems and Service Management (ICSSSM’08), 1–6. IEEE Society.

TU Y-J, ZHOU W and PIRAMUTHU S (2009) Identifying RFID-embedded objects in pervasive healthcare applications. Decision Support Systems 46(2), 586–593.

VIVES X (1984) Duopoly information equilibrium: Cournot and Bertrand. Journal of Economic Theory 34, 71–94.

ZHOU W (2009) RFID and item-level information visibility. European Journal of Operational Research 198(1), 252–258.

Z W, K G and P S (2008a) RFID-enabled dynamic retail pricing. In Proceedings of the Seventh Workshop on e-Business (WeB2008),

ZHOU W, KAPOOR G and PIRAMUTHU S (2008b) RFID tags and eManufacturing. In Proceedings of the All India Manufacturing Technology, Design and Research Conference (AIMTDR2008), 1067–1073.

## Appendix

Unsold amount as a function of information and quantity

I. b(Q<sub>1</sub> þ Q<sub>2</sub>)p<sup>1</sup>(y<sub>1</sub>Q<sub>1</sub> þ y<sub>2</sub>Q<sub>2</sub>)

Player i’s unsold portion of the his product is

$$
h _ {i} = \frac {\theta_ {i} \beta (Q _ {i} + Q _ {j})}{(Q _ {i} \theta_ {i} + Q _ {j} \theta_ {j})}\tag{A1}
$$

$$
\begin{array}{l} \frac {\partial h _ {i}}{\theta_ {i}} = \frac {(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) \beta (Q _ {i} + Q _ {j} ^ {*}) - Q _ {i} \theta_ {i} \beta (Q _ {i} + Q _ {j} ^ {*})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {2}} \\ = \frac {Q _ {j} ^ {*} \theta_ {j} ^ {*} \beta (Q _ {i} + Q _ {j} ^ {*})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {2}} > 0 \\ \frac {\partial h _ {i}}{Q _ {i}} = \frac {(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) \theta_ {i} \beta - \theta_ {i} ^ {2} \beta (Q _ {i} + Q _ {j} ^ {*})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {2}} \\ = \frac {\theta_ {i} \beta Q _ {j} (\theta_ {j} - \theta_ {i})}{(Q _ {i} \theta_ {i} + Q _ {j} ^ {*} \theta_ {j} ^ {*}) ^ {2}} \end{array}
$$

$$
\text { II. } Q _ {1} + Q _ {2} - \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2}) \geqslant \beta (Q _ {1} + Q _ {2}) \geqslant \frac {1}{2} (\theta_ {1} Q _ {1} + \theta_ {2} Q _ {2})
$$

player i’s unsold portion can be described as

$$
\begin{array}{l} h _ {i} = \frac {\left[ \frac {(1 - \theta_ {i}) Q _ {i} [ \beta (Q _ {i} + Q _ {j}) + \frac {1}{2} (\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ]}{(1 - \theta_ {i}) Q _ {j} + (1 - \theta_ {j}) Q _ {j}} + \frac {1}{2} \theta_ {i} Q _ {i} \right]}{Q _ {i}} \\ = \frac {(1 - \theta_ {i}) \beta (Q _ {i} + Q _ {j}) - \frac {1}{2} (1 - \theta_ {i}) \theta_ {j} Q _ {j} + \frac {1}{2} \theta_ {i} (1 - \theta_ {j}) Q _ {j}}{(1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j}) Q _ {j}} \\ = \frac {(1 - \theta_ {i}) \beta (Q _ {i} + Q _ {j}) + \frac {1}{2} Q _ {j} (\theta_ {i} - \theta_ {j})}{(1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j}) Q _ {j}} \end{array}
$$

$$
\begin{array}{l} \frac {\partial h _ {i}}{\theta_ {i}} = \frac {[ (1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} ] \cdot (- \beta (Q _ {i} + Q _ {j} ^ {*}) + \frac {1}{2} Q _ {j} ^ {*})}{(1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j}) Q _ {j}} \\ \qquad + \frac {(1 - \theta_ {i}) Q _ {i} \beta (Q _ {i} + Q _ {j} ^ {*}) + \frac {1}{2} Q _ {j} Q _ {j} (\theta_ {i} - \theta_ {j})}{[ (1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} ] ^ {2}} \\ = \frac {- (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} \beta (Q _ {i} + Q _ {j} ^ {*}) + (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} \frac {1}{2} Q _ {j} ^ {*} + \frac {1}{2} Q _ {i} Q _ {j} (1 - \theta_ {j})}{[ (1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} ] ^ {2}} \\ = \frac {(1 - \theta_ {j} ^ {*}) Q _ {j} [ - \beta (Q _ {i} + Q _ {j} ^ {*}) + \frac {1}{2} Q _ {j} ^ {*} + \frac {1}{2} Q _ {i} ]}{[ (1 - \theta_ {i}) Q _ {i} + (1 - \theta_ {j} ^ {*}) Q _ {j} ^ {*} ] ^ {2}} \\ > 0, \text {if} \beta <   \frac {1}{2} \\ <   0, \text {if} \beta > \frac {1}{2} \\ = 0, \text {if} \beta = \frac {1}{2} \end{array}
$$

III. $\begin{array} { r } { Q _ { 1 } + Q _ { 2 } - \frac { 1 } { 2 } ( \theta _ { 1 } Q _ { 1 } + \theta _ { 2 } Q _ { 2 } ) \leqslant \beta ( Q _ { 1 } + Q _ { 2 } ) } \end{array}$ Player i’s unsold portion can be described as

$$
\begin{array}{r l} h _ {i} & = \frac {\left[ Q _ {i} - \frac {\theta_ {i} Q _ {i} (1 - \beta) (Q _ {i} + Q _ {j})}{\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}} \right]}{Q _ {i}} \\ & = \frac {\left(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}\right) - \theta_ {i} (Q _ {i} + Q _ {j}) + \theta_ {i} \beta (Q _ {i} + Q _ {j})}{\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}} \\ & = \frac {\theta_ {j} Q _ {j} - \theta_ {i} Q _ {j} + \theta_ {i} \beta (Q _ {i} + Q _ {j})}{\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}} \end{array}
$$

$$
\begin{array}{l} \frac {\partial h _ {i}}{\theta_ {i}} = \frac {(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) (- Q _ {j} + \beta (Q _ {i} + Q _ {j}))}{- \theta_ {j} Q _ {i} Q _ {j} + \theta_ {i} Q _ {i} Q _ {j} - \theta_ {i} Q _ {j} \beta (Q _ {i} + Q _ {j})} \\ = \frac {\theta_ {j} Q _ {j} [ - Q _ {j} + \beta (Q _ {i} + Q _ {j}) - Q _ {i} ]}{(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ^ {2}} \\ = \frac {\theta_ {j} Q _ {j} [ (- 1 + \beta) (Q _ {i} + Q _ {j}) ]}{(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ^ {2}} <   0 \end{array}
$$

$$
\begin{array}{l} \frac {\partial h _ {i}}{Q _ {i}} = \frac {(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) \theta_ {i} \beta - \theta_ {i} (\theta_ {j} Q _ {j} - \theta_ {i} Q _ {j} + \theta_ {i} \beta (Q _ {i} + Q _ {j}))}{(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ^ {2}} \\ = \frac {\theta_ {i} (\theta_ {j} Q _ {j} \beta - (\theta_ {j} Q _ {j} - \theta_ {i} Q _ {j} + \theta_ {i} \beta Q _ {j})}{(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ^ {2}} \\ = \frac {\theta_ {i} Q _ {j} (- 1 + \beta) (\theta_ {i} + \theta_ {j})}{(\theta_ {i} Q _ {i} + \theta_ {j} Q _ {j}) ^ {2}} \end{array}
$$
