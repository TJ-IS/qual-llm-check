---
otero_id: 5902
otero_key: "AK9RQXSS"
title: "Incentive control of spinning reserve in electricity multi-markets"
authors: "Ashkan R. Kian; Ali Keyhani"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Incentive control of spinning reserve in electricity multi-markets

Ashkan R. Kian<sup>a,\*</sup>, Ali Keyhani<sup>b</sup>

<sup>a</sup>School of ECE, Cornell University, 428 Phillips Hall, Ithaca, NY 14850, USA

<sup>b</sup>205 Dreese Laboratory, Electrical Engineering Department, Ohio State University, Columbus, OH 43210, USA

Available online 17 July 2004

## Abstract

Reliable and efficient operation of deregulated electricity markets requires supply and demand elasticity. This paper presents incentive control of spinning reserves in electricity multi-markets using game theory. Interruptible load contracts (ILC) could reduce the amount of spinning reserve requirements during system contingencies such as transmission congestion. It is shown that the power utilities (PU) with ILC could increase their benefits in timeseparated energy and spinning reserves markets (e.g., inter-temporal market gaming among day-ahead, hour-ahead and real-time markets).

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Incentive control; Spinning reserve; Energy markets; Game theory; Demand management; Load shedding; Customer willingness to participate (customer type); Incentive payment

## 1. Introduction

Researchers [1,4,6,11,17–20] have shown that strategic behaviors of the market participants and demand-elasticity have major effects on price volatility in electricity multi-markets. Designing optimal load management programs by power utilities could improve the reliability and efficiency of energy and ancillary services markets and reduce the price volatility. If the power utilities estimate their customers’ costs of load shedding and their willingness to sign load management contracts (e.g. customer types), they will be able to control the amount of spinning reserve requirements. Power utilities need to collect information about transmission and generation maintenance schedules, and historical data about highly congested transmission paths. They also need to have a dynamic model of the system zonal prices. In this paper, a stochastic model for the system zonal prices is considered. Based on the assumed dynamic price model, optimization problems for the load management contracts are formulated and solved for a three-zone deregulated power system (Fig. 1). The rest of the paper is organized as follows: Section 2 covers the literature review. In Section 3, we formulate the problem mathematically. In Section 4, a numerical example of the proposed method is presented. Section 5 concludes the paper.

![](/api/attachments/AK9RQXSS/fulltext/images/b4a05a7a9aa500197ca084e44dd4be34414349a1345c4fe2c605d377a415a3b7.jpg)  
Fig. 1. A three-zone deregulated power system.

## 2. Literature review

Studies of supply and demand strategic bidding and energy market design have been attempted by many researchers [1–20]. Visudhiphan and Ilic [20] have introduced dynamic bidding models for representing possible behavior of rational profitmaximizing generators responding to the electricity price variation in a simplified poolco-type electricity market. The emphasis of their work is to address mechanisms and critical factors that enable generators (Gencos) to exert market power during the bidding process. They have shown that in electricity markets with price-inelastic loads, generators will attempt to game the market extensively. With the aid of a dynamic bidding model, they have analyzed the effect of generators bidding strategies on the market-clearing price. Two types of generator supply functions are considered in this research work: (1) single-step supply function (SSF) and (2) linear supply function (LSF). The authors have studied two possible strategies for power generators:

1. Estimated profit maximization (EPM): In this strategy, the generator will increase its offer price in his next bid if the expected (estimated) profit of the next period is larger than the profit of the current period.

2. Competition to be a base-load generator (CBG): In this strategy, the base-load generator offering the lowest bid is scheduled at each hour for power generation by the independent system operator (ISO).

Based on their simulation results, the marketclearing price will be lower when the generators adopt the CBG strategy rather than EPM strategy.

Skantze and Chapman [18] have shown some of the complexity related to the bidding of electric power in a deregulated market. They use California system to examine the price dynamics of electric power. They define a new index to measure the existence of market power. This index is derived specifically for electric power markets, taking into account the nature of generators operating costs. The first challenge of understanding price dynamics in electric power markets is to identify the forces driving up the cumulative supply curves. The second is to quantify and estimate them. The authors consider three possible causes for shifts in supply curve:

1. Generator outages: if a generator is off line due to faults or service requirements, its bid curve is withheld from the market, shifting the cumulative supply curve to the left.

2. Market entry or exit: a new generator entering the market, either from a competing power exchange or a terminated bilateral contract will shift the supply curve to the right. Similarly generators exiting the power exchange markets will shift the supply curve to the left.

3. Gaming and strategic bidding: generators with significant market share may attempt to increase profits by shifting their bid curves to the left, thus driving up the market clearing price.

Fahrioglu and Alvarado [6] consider and describe a variety of voluntary demand management programs, including full interruption, equipment specific partial interruptions and programs that guarantee a certain <sup>b</sup>relief performance<sup>Q</sup>. The authors define, consider and compare three types of demand management programs:

<sup>!</sup> Firm Power Level Program, which defines a maximum power level (FPL) for each customer. During an interruption request, the customers in this program are required to reduce their demand to their pre-agreed FPL or below.

<sup>!</sup> Agreed Relief Program, which has some similarities with the FPL program. When customers receive a relief request, they shed a predetermined amount of load from their demand level at the time of the curtailment request and have a sloping upper limit to their demand pickup during the requested curtailment period. After the curtailment ends, they may resume their typical demand.

<sup>!</sup> Equipment Specific Interruption Program is different in a sense that there are no parameters to decide upon. However, the customer can decide what equipment to shut off upon request. Air conditioners and heaters would be among the best candidates since they put a big burden on the utility.

The authors use a concept from game theory called <sup>b</sup>mechanism design<sup>Q</sup> to develop demand management contracts for the power utilities based on their customer willingness to shed load. Their demand management contracts are largely governed by customer type (willingness to shed load) and customer location. Locational value of each customer is calculated using sensitivity method (sensitivity of line flows to individual loads). Some customers are at more critical locations than the others that make them more important for the power utilities to sign interruptible load contracts with them.

## 3. Problem formulation

It is assumed that power utilities may use any of the following four strategies to optimize their energy and spinning reserve scheduling in electricity multimarkets:

1. Intra-market strategy: gaming within a single isolated power market. The opportunity cost of gaming this market is given by the difference between the market clearing price and the marginal cost of generation (shadow price).

2. Inter-market strategy: gaming between separate power exchanges or scheduling coordinators. This may allow a generator to reduce the opportunity cost of withholding generation from the market by shifting that portion of the bid to a different power exchange or into bilateral contracts.

3. Inter-commodity strategy: similar to inter-market strategy except that excess generation capacity is shifted into ancillary services markets.

4. Inter-temporal strategy: load and generation are shifted between day-ahead, hour-ahead and realtime markets.

Prices in energy markets vary both as a function of time (day-ahead, hour-ahead and real-time markets) and location (different zonal prices due to line outages, congestion and other power system contingencies). In this paper a stochastic model is used to show the zonal price dynamics in different markets. It is assumed that zonal energy prices have three components: (1) zonal marginal cost, (2) zonal mark-up price, which is a function of power system reliability index and load elasticity and (3) independent random price jumps (jump-up and jumpdown). The dynamic energy price model is as follows:

$$
\lambda_ {k} = \mathrm{mce} _ {k} + \mathrm{mupe} _ {k} + K _ {\mathrm{P}} \cdot \text { rand } (- 1, 1)\tag{1}
$$

$$
\mathrm{mupe} _ {k + 1} = \frac {K _ {\lambda} \cdot \mathrm{mupe} _ {k}}{\mathrm{RI} _ {k} \cdot \varepsilon_ {\lambda_ {k}} ^ {D _ {k}}}\tag{2}
$$

$$
\varepsilon_ {\lambda_ {k}} ^ {D _ {k}} = \frac {\partial D _ {k}}{\partial \lambda_ {k}} \cdot \frac {\lambda_ {k}}{D _ {k}}\tag{3}
$$

Where $\lambda _ { k } \mathrm { : }$ zonal price of energy at time step $k ;$ mce<sub>k</sub>: zonal marginal cost of energy at time step $k ;$ mupe<sub>k</sub>: zonal mark-up price of energy at time step k; $K _ { \mathrm { P } } \mathrm { : }$ amplitude of the independent random price jumps; rand(1,1): a random variable between 1 and 1; $K _ { \lambda } \colon$ amplitude of the zonal mark-up price; $\mathrm { R I } _ { k } { = }$ $\mathrm { T R I } _ { k } \cdot \mathrm { G R I } _ { k }$ : zonal reliability index at time step k; $\varepsilon _ { \lambda _ { k } } ^ { D _ { k } } \mathrm { = } ( \mathrm { { } } \partial D _ { k } / \partial \lambda _ { k } ) \cdot ( \lambda _ { k } / D _ { k } )$ : zonal demand elasticity at time step k.

In this paper, we assume that the zonal spinning reserve prices have two components, (1) capacity reserve price $( r _ { k } )$ and (2) execution price $( g _ { k } )$ . The dynamic model of the spinning reserve price is explained as follows:

$$
r _ {k} = \operatorname{mcr} _ {k} + \operatorname{mupr} _ {k}\tag{4}
$$

$$
\operatorname{mupr} _ {k + 1} = \frac {K _ {r} \cdot \operatorname{mupr} _ {k}}{\mathrm{RI} _ {k} \cdot \varepsilon_ {r _ {k}} ^ {R _ {k}}}\tag{5}
$$

$$
g _ {k} = x _ {k} \cdot \lambda_ {k}\tag{6}
$$

$$
x _ {k} = 1 - \mathrm{RI} _ {k}\tag{7}
$$

$$
\mu_ {k} = r _ {k} + g _ {k} = r _ {k} + x _ {k} \cdot \lambda_ {k}\tag{8}
$$

Where mcr<sub>k</sub>: zonal marginal cost of spinning reserve at time step $k ;$ mupr<sub>k</sub>: zonal mark-up price of spinning reserve at time step $k ; K _ { r } .$ : amplitude of the zonal mark-up price; $\varepsilon _ { r _ { k } } ^ { R _ { k } } \mathrm { = } ( \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm $ : zonal spinning reserve elasticity at time step $k ; x _ { k } .$ zonal loss of load probability (LOLP) at time step k; $\mathrm { R I } _ { k } { = } \mathrm { T R I } _ { k } \cdot \mathrm { G R I } _ { k } \colon$ zonal reliability index at time step $k ; \lambda _ { k } \colon$ zonal price of energy at time step $k ; \mu _ { k } \colon$ zonal spinning reserve price at time step k.

In this section, different scenarios of market gaming that could be played by a power utility to maximize its expected payoffs in the market are explained and mathematically formulated. Consider a three-zone deregulated power system, where a utility could have one customer at each zone as shown in Fig. 1.

Suppose that each zone has a day-ahead, hourahead and real-time energy price such as, $\lambda _ { \mathrm { D A } } , \lambda _ { \mathrm { H A } } ,$ $\lambda _ { \mathrm { R T } } ,$ respectively. In a same manner, assume that each zone has a day-ahead and hour-ahead spinning reserve price such as, $\mu _ { \mathrm { D A } } , ~ \mu _ { \mathrm { H A } } ,$ , respectively. It is also assumed that each transmission line that connects two zones of the power system (e.g., zone<sup>\_</sup>i to zone<sup>\_</sup>j) has a usage charge such as: $h _ { i j } , h _ { j i } , h _ { i i } { = } h _ { j j } { = } 0$ , which will be collected by the transmission owner. The total system demand is: $D _ { 1 } { + } D _ { 2 } { + } D _ { 3 }$ and changes over a 24- h period of load cycle. The peak hours of system demand are considered from 7 a.m. to 22 p.m. Therefore, for the 16 h of peak demand, each utility will try to sign optimal load management contracts with its customers to maximize its expected payoff function. Different scenarios of market gaming by a power utility could be formulated as follows.

## 3.1. Scenario 1

Inter-market gaming of real-time markets (spot markets). In this scenario, the power utility will try to buy the required spinning reserve from the cheapest zonal market. By offering minimum incentive payments to its customers, the utility will encourage them to sign interruptible load contracts during the peak hours of demand. If the utility succeeds in its strategy, it will be able to sell the excessive power (from the interruptible load contracts) to the most expensive zonal spot market (real-time market). The objective function of such a scenario could be formulated as follows:

Let us assume a quadratic concave benefit function for a power utility:

$$
U B (P) = A \cdot P - \frac {1}{2} B \cdot P ^ {2}\tag{9}
$$

and assume quadratic convex cost functions for the customers of that utility:

$$
C _ {j} \left(\theta_ {j}, q _ {j}\right) = \alpha \cdot \left(1 - \theta_ {j}\right) \cdot q _ {j} + \frac {1}{2} \beta \cdot q _ {j} ^ {2}\tag{10}
$$

where $\theta _ { j }$ is customer-j willingness to shed load with probability $p _ { j }$ . In order to succeed in its load management program, a power utility needs to recognize (estimate) each customer’s type and its opportunity cost of participating in this program. The marginal cost of load curtailment for customer-j is defined as follows:

$$
m c _ {j} \left(\theta_ {j}, q _ {j}\right) = \frac {\partial C _ {j}}{\partial q _ {j}} = \alpha \cdot \left(1 - \theta_ {j}\right) + \beta \cdot q _ {j}\tag{11}
$$

The above formula shows that as $\theta _ { j }$ increases the marginal cost of load shedding for customer-j decreases. The customer with highest $\theta _ { j }$ (willingness to shed load) will have the lowest marginal cost. Please note that $\theta _ { j }$ could take values in the interval [0, 1]. The objective of a power utility would be to determine an optimal incentive payment (/ \$/MW h) to each customer who agrees to curtail 1 MW of its demand. The optimization problem for scenario 1 could be formulated as follows:

$$
\Pi_ {1} = \max _ {q, \phi} \left\{ \begin{array}{l} U B (x \cdot P) - \sum_ {j = 1} ^ {\mathrm{nc}} \bigl (\mu_ {j} ^ {\min} \cdot x _ {j} \cdot D _ {j} \bigr) + \\ \sum_ {j = 1} ^ {\mathrm{nc}} \bigl (\bigl (\lambda_ {j} ^ {\max} - \phi_ {j} \bigr) \cdot q _ {j} \cdot p _ {j} \bigr) \end{array} \right\}\tag{12}
$$

Subject to:

$$
x \cdot P = \sum_ {j = 1} ^ {\mathrm{nc}} q _ {j}
$$

$$
\phi_ {j} = m c _ {j} = \alpha \cdot (1 - \theta_ {j}) + \beta \cdot q _ {j}, \text {   for   } j = 1, \dots , \mathrm{nc}
$$

where $\mu _ { j } ^ { \mathrm { { m i n } } } ;$ =min $\{ \mu _ { i } { + } h _ { i j } \} _ { i = 1 } ^ { 3 } , \mathrm { f o r } j { = } 1 , . . . ,$ nc: expectedminimum-price of spinning reserve for customer-j; $\lambda _ { j } ^ { \mathrm { m a x } } { = } \mathrm { m a x } \bar { \{ }  \lambda _ { i } { - } h _ { j i } \} _ { i = 1 } ^ { 3 } ,$ , for $j = 1 , . . . , \mathrm { n c } \colon$ expectedmaximum-spot price of energy for customer-j load management contract; x: zonal loss of load probability vector (LOLP), which shows the percentage of spinning reserve requirement at each zone of the power system; $x \cdot P ;$ : total amount of spinning reserve requirement purchased by the power utility; $q _ { j } \colon$ optimal amount of the load shedding contract for customer-j; $\phi _ { j } \colon$ optimal incentive payment to customer-j for participating in the load management program; $p _ { j } \colon$ probability of participation of customer-j in the load management program; $\theta _ { j } \colon$ type of customer-j that shows its willingness to participate in the load management program; $D _ { j } { \mathrm { : } }$ demand of customer-j; nc: number of customers who participate in the load management program.

The power utility should solve the above Kuhn-Tucker optimization problem over the peak hours of demand (7 a.m. to 10 p.m.) to maximize its expected payoff in the market. As it can be seen from the expected payoff function (Eq. (12)), the market power index in this scenario is: $I _ { \mathrm { M P } } { = } \lambda _ { j } ^ { \mathrm { m a x } } { - } \phi _ { j } ^ { \ast }$ . It means that, if the expected-maximum-spot price of energy in the system is higher than the optimal incentive payment to customer-j for participating in the load management program, the power utility has market power.

## 3.2. Scenario 2

Inter-commodity gaming of spinning reserve markets. In this scenario, the power utility could maximize its expected payoff in the market by purchasing the required spinning reserve from the cheapest zone and selling its excessive power from the load management contracts to the most expensive spinning reserve market. The mathematical formulation of Scenario 2 is as follows:

$$
\Pi_ {2} = \max _ {q, \phi} \left\{ \begin{array}{l} U B (x \cdot P) - \sum_ {j = 1} ^ {\mathrm{nc}} \left(\mu_ {j} ^ {\min} \cdot x _ {j} \cdot D _ {j}\right) + \\ \sum_ {j = 1} ^ {\mathrm{nc}} \left(\left(\mu_ {j} ^ {\max} - \phi_ {j}\right) \cdot q _ {j} \cdot p _ {j}\right) \end{array} \right\}\tag{13}
$$

Subject to:

$$
\begin{array}{l} x \cdot P = \sum_ {j = 1} ^ {\mathrm{nc}} q _ {j} \\ \phi_ {j} = m c _ {j} = \alpha \cdot (1 - \theta_ {j}) + \beta \cdot q _ {j}, \text {   for   } j = 1,.., \mathrm{nc} \end{array}
$$

where $\mu _ { j } ^ { \mathrm { m i n } } { = } \mathrm { m i n } \{ \mu _ { i } { + } h _ { i j } \} _ { i = 1 } ^ { 3 }$ , for $j { = } 1 , \ldots$ nc: expected-minimum-price of spinning reserve for customer-j; $\mu _ { j } ^ { \mathrm { m a x } } { = } \mathrm { m a x } \{ \mu _ { i } { - } h _ { j i } \} _ { i = 1 } ^ { 3 }$ , for $j { = } 1 , \ \ldots$ nc: expected-maximum-price of spinning reserve for customer-j load management contract.

All other parameters are as defined in scenario 1. The power utility should solve the above Kuhn-Tucker optimization problem over the peak hours of demand (7 a.m. to 10 p.m.) to maximize its expected payoff in the market. $\mathrm { A s }$ it can be seen from the expected payoff function (Eq. (13)), the market power index in this scenario is: $I _ { \mathrm { M P } } { = } \mu _ { j } ^ { \mathrm { m a x } } { - } \phi _ { j } ^ { * } .$ . It shows that, if the expected-maximum-price of the spinning reserve in the system is higher than the optimal incentive payment to customer-j for participating in the load management program, the power utility has market power. The power utility could assign two probability distribution functions $( \mathrm { p d f } _ { \mu } , \mathrm { p d f } _ { \lambda } )$ to $\stackrel { \mathrm { - } } { \mu _ { j } ^ { \mathrm { m a x } } } = \mathrm { m a x } \stackrel { \mathrm { - } } { \mu _ { i } } - h _ { j i } \stackrel { \textstyle \large 3 } { \mu _ { i } } = 1$ and $\lambda _ { j } ^ { \mathrm { m a x } } { = } \mathrm { m a x } \dot { \{ } \lambda _ { i } { - } h _ { j i } \} _ { i = 1 } ^ { 3 } ,$ respectively and then construct a payoff function for gaming both the energy and spinning reserve markets. The market power index for the new proposed payoff function could be defined as:

$I _ { \mathrm { M P } } = \pi _ { \mu } \cdot \mu _ { j } ^ { \mathrm { m a x } } + \pi _ { \lambda } \cdot \lambda _ { j } ^ { \mathrm { m a x } } - \phi _ { j } ^ { * }$ where, $\pi _ { \mu } + \pi _ { \lambda } = 1$ . If the LOLP increases, then scenario 2 becomes more profitable for the power utility.

## 3.3. Scenario 3

Inter-temporal gaming of time-separated energy markets (day-ahead, hour-ahead and real-time markets). In this scenario the power utility attempts to buy the required spinning reserve from the cheapest temporal-market. Then it will sell its excessive power from the load management contracts to the most expensive energy temporal-market. It is important to note that in this scenario, all the customers of a power utility are at one zone. Therefore, the power utility will attempt to game the time-separated energy markets of that zone. The mathematical formulation of scenario 3 is as follows:

$$
\Pi_ {3} = \max _ {q, \phi} \left\{ \begin{array}{l} U B (x \cdot P) - \mu^ {\min} (x \cdot P) + \\ \sum_ {j = 1} ^ {\mathrm{nc}} \big (\big (\lambda^ {\max} - \phi_ {j} \big) \cdot q _ {j} \cdot p _ {j} \big) \end{array} \right\}\tag{14}
$$

Subject to:

$$
\begin{array}{l} x \cdot P = \sum_ {j = 1} ^ {\mathrm{nc}} q _ {j} \\ \phi_ {j} = m c _ {j} = \alpha \cdot (1 - \theta_ {j}) + \beta \cdot q _ {j}, \text {   for   } j = 1, \dots , \mathrm{nc} \end{array}
$$

where $\lambda ^ { \mathrm { m a x } } = \mathrm { m a x } ( \lambda _ { \mathrm { D A } } , \lambda _ { \mathrm { H A } } , \lambda _ { \mathrm { R T } } )$ of the desired zone. $\mu ^ { \mathrm { m i n } } { = } \mathrm { m i n } ( \mu _ { \mathrm { D A } } , \mu _ { \mathrm { H A } } )$ of the desired zone.

All other parameters are as defined in scenario 1. The power utility should solve the above Kuhn-Tucker optimization problem over the peak hours of demand (7 a.m. to 10 p.m.) to maximize its expected payoff in the temporal-markets. As it can be seen from the expected payoff function (Eq. (14)), the market power index in this scenario is: $I _ { \mathrm { M P } } { = } \lambda ^ { \mathrm { m a x } } { - } \phi _ { j } ^ { \ast }$ . It means that if the expected-maximum-price of energy in the desired zone is higher than the optimal incentive payments to the customers for participating in the load management program, the power utility has market power. The power utility could assign two probability distribution functions $( \mathrm { p d f } _ { \mu } , \mathrm { p d f } _ { \lambda } )$ to $\mu ^ { \mathrm { m a x } } { = } \mathrm { m a x } \{ \mu _ { \mathrm { D A } } , $ $\mu _ { \mathrm { H A } } \}$ and $\lambda ^ { \operatorname* { m a x } } = \operatorname* { m a x } \{ \lambda _ { \mathrm { D A } } , ~ \lambda _ { \mathrm { H A } } , ~ \lambda _ { \mathrm { R T } } \}$ , respectively, and then construct a payoff function for gaming both the energy and spinning reserve markets. The market power index for the proposed payoff function could be defined as: $I _ { \mathrm { M P } } { = } { \pi } _ { \mu } \cdot { \mu } ^ { \mathrm { m a x } } { + } { \pi } _ { \lambda } \cdot { \lambda } ^ { \mathrm { m a x } } { - } { \phi } _ { j } ^ { \ast }$ where $\pi _ { \mu } + \mu _ { \lambda } = 1$

## 4. Numerical example

In this section of the paper, a numerical example is presented to show the applicability of the proposed scenarios in Section 3. One could compare these scenarios in terms of their maximum-expected-payoffs and effectiveness in reducing the spinning reserve prices (as a result of increasing the demand elasticity). Here, we apply the proposed method to a three-zone deregulated power system as shown in Fig. 1. We assume a total load of 2000 MW for the system and assume that 470 MW of this load belongs to the three customers of our interested power utility. Assume that the utility benefit function is given as:

$$
U B (P) = 3 5 P - \frac {1}{2} 0. 0 3 5 P ^ {2}\tag{15}
$$

The general cost function of the customers is given as:

$$
C (\theta , q) = 7 (1 - \theta) \cdot q + \frac {1}{2} 0. 0 3 q ^ {2}\tag{16}
$$

The customers’ types are given in a vector form as:

$$
\theta = \left[ \begin{array}{c c c} 0. 5 5 & 0. 5 0 & 0. 5 6 \end{array} \right]
$$

and the probability of their willingness to participate in the load management program is given in a vector form as:

$$
p = \left[ \begin{array}{c c c} 0. 7 5 & 0. 8 0 & 0. 7 8 \end{array} \right]
$$

The initial demand (in MW) of the customers is given in a vector form as:

$$
D = \left[ \begin{array}{c c c} 1 5 0 & 2 0 0 & 1 2 0 \end{array} \right]
$$

There are assumed some reasonable values for the transmission reliability index (TRI), generation reliability index (GRI), zonal marginal cost of energy (mce) and spinning reserve (mcr), zonal mark-up price for energy (mupe) and spinning reserve (mupr), and transmission usage charges $( h _ { i j } , ~ h _ { j i } )$ from the literature, historical data and the OASIS databases available at the Cal-ISO web site (www.caiso.com).

![](/api/attachments/AK9RQXSS/fulltext/images/11cba85aa3338eb8cdd0f94b6f34d56a9d558ff8bf0092807a5025d37df8f394.jpg)

The market simulation results for 1 scenarios 2 scenarios 3 are shown in Figs. 2–4, respectively. The simulation of zonal spinning reserve prices $( \mu _ { \mathrm { D A } } ,$ $\mu _ { \mathrm { H A } }$ \$/MW h), optimal incentive payments (/ \$/MW h) to the participants of the load management contracts, and the optimal quantities of load shedding ( q MW h) for the customers are shown in Figs. 2–4 for 16 h of peak demand. The maximum-expectedbenefit (MEB) of the power utility for 1 scenarios 2 scenarios 3 are as follows:

$$
\mathrm{MEB} _ {s c 1} = 2 7, 7 2 0. 0 0 ()
$$

$$
\mathrm{MEB} _ {s c 2} = 2 1, 5 0 9. 0 0 ()
$$

$$
\mathrm{MEB} _ {s c 3} = 2 3, 1 9 5. 0 0 ()
$$

$$
\text { MEB } _ {s c 1 \& s c 2} = 2 5, 3 1 6. 0 0 () \text { with } \pi_ {\mu} = \pi_ {\lambda} = 0. 5
$$

It can be seen that inter-market gaming of spot markets (scenario 1) and inter-temporal gaming of time-separated markets (scenario 2) are more profitable than inter-commodity gaming of spinning reserve markets (scenario 2) for this power utility with the given system conditions. If the loss of load probability (LOLP) increases then, scenario 2 can be more profitable than scenarios 1 and 3. The key observation from Figs. 2–4 is that as h (willingness to shed load) increases the zonal spinning reserve elasticity $( \varepsilon _ { r _ { \mathrm { k } } } ^ { R _ { k } } )$ increases and therefore, it forces the mark-up price of spinning reserve (mupr) to go to zero. The increment of the zonal spinning reserve elasticity could be formulated as follows:

![](/api/attachments/AK9RQXSS/fulltext/images/86c95c0fed35af0ace24b312a435787efe70a0b8fd8a71aa576b43b0289c1a08.jpg)  
Fig. 2. Simulation results of scenario 1: (1-a) $\mu _ { \mathrm { D A } } \left( - \right) , \mu _ { \mathrm { H A } } \left( - \right)$ (\$/MW h) for zone-1; (1-b) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/MW h) for zone-2; (1-c) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/MW h) for zone-3; (1-d) optimal incentive payments to customers 1 (–), 2 (- -) and 3 (-.) (\$/MW h); (1-e) optimal load shedding quantities for customers ${ 1 \left( - \right) , 2 \left( - - \right) }$ and 3 (-.) (MW h).

Scenario-2 simulation results  
![](/api/attachments/AK9RQXSS/fulltext/images/e18715b1d5113316f25407c4815f62ad364a957377c0034cda522609073a8e61.jpg)  
Fig. 3. Simulation results of scenario 2: (2-a) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/MW h) for zone-1; (2-b) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/MW h) for zone-2; (2-c) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/MW h) for zone-3; (2-d) optimal incentive payments to customers 1 $( - ) , 2 \ ( - - )$ and 3 (-.) (\$/MW h); (2-e) optimal load shedding quantities for customers 1 (–), 2 (- -) and 3 (-.) (MW h).  
Fig. 4. Simulation results of scenario 3: (3-a) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/ MW h) for zone-1; (3-b) optimal incentive payments to customers 1 $( - ) , ~ 2 ~ ( - - )$ and 3 (-.) (\$/MW h); (3-c) Optimal load shedding quantities for customers 1 $( - ) , 2 \ ( - - )$ and 3 (-.) (MW h).

![](/api/attachments/AK9RQXSS/fulltext/images/2272afb55aa10c4c709b511913e75b2aef850d43f3f5d2d878a4c1775368479d.jpg)  
Fig. 5. Simulation results for the case that $\theta _ { 1 }$ decreases: (a) $\mu _ { \mathrm { D A } }$ (–), $\mu _ { \mathrm { H A } }$ (- -) (\$/MW h) for zone-1; (b) l<sub>DA</sub> (–), l<sub>HA</sub> (- -) (\$/MW h) for zone-2; (c) $\mu _ { \mathrm { D A } }$ (–), $\mu _ { \mathrm { H A } }$ (- -) (\$/MW h) for zone-3.

$$
\Delta \varepsilon = K _ {\varepsilon}. \frac {\sum_ {j = 1} ^ {\mathrm{nc} _ {z}} \left(q _ {j} \cdot p _ {j}\right)}{\frac {1}{\mathrm{nc} _ {z}} \cdot \sum_ {j = 1} ^ {\mathrm{nc} _ {z}} \phi_ {j}}\tag{17}
$$

Where $\mathrm { n c } _ { z }$ is the number of customers in a zone who are willing to participate in the load management programs and $K _ { \varepsilon }$ is a scaling factor. All other variables are as defined in 1 scenarios 2 scenarios 3. Fig. 5 shows that as $\theta$ decreases in zone-1 the mark-up price of spinning reserve (mupr) in that zone goes up considerably. The market simulation results show that optimal load management contracts increase the zonal spinning reserve elasticity and, therefore, could force the markup price of spinning reserve (mupr) to go down dramatically (if the number of participating power consumers in these management programs is large enough). A power utility that encourages all of its customers (especially those located at highly congested areas also known as load pockets) to participate in the load management contracts (by offering optimal incentive payments) could become the market leader. Another observation from the simulation results is that the market forces (mainly the demand elasticity in our proposed scenarios) will drive the energy and spinning reserve prices to their marginal values. Therefore, the energy and reserve prices do not need to be settled by an authority such as ISO.

## 5. Conclusion

In this paper, the design of optimal load management contracts by power utilities in the deregulated energy and spinning reserve markets was proposed and mathematically formulated using game theory. As it can be seen from the market simulation results (Figs. 2–5), the proposed method is an incentive control of spinning reserve markets. Three types of gaming strategies (scenarios) by power utilities in the deregulated energy markets were studied and formulated. The market simulation results also showed that as the demand elasticity (consumers’ willingness to participate in load shedding contracts) increases the mark-up price of spinning reserve would be forced to zero, and the spinning reserve prices settle to their marginal cost values. It is important to note that in the proposed method, market prices will be discovered rather than set by an authority such as ISO.

## References

[1] F. Alvarado, The stability of power system markets, IEEE Transactions on Power Systems 14 (2) (1999 May) 505– 511.

[2] R. Billinton, R. Kavki, Capacity reserve assessment using system well-being analysis, IEEE Transactions on Power Systems 14 (2) (1999 May) 433 – 438.

[3] R. Bjorgan, C.C. Liu, J. Lawarree, Financial risk management in a competitive electricity market, IEEE Transactions on Power Systems 14 (4) (1999 Nov.) 1285– 1291.

[4] A.S. Chuang, F. Wu, Capacity payments and the pricing of reliability in competitive generation markets, Proceedings of the 33rd HICSS, 2000.

[5] S. Dekrajangpetch, G.B. Sheble, A.J. Conejo, Auction implementation problems using Lagrangian relaxation, IEEE Transactions on Power Systems 14 (1) (1999 Feb.) 82 – 88.

[6] M. Fahrioglu, F. Alvarado, On the importance of customer location in demand management contracts, PSERC, 1999. www.PSERC.WISC.edu (papers/1999 publications).

[7] R.W. Ferrero, J.F. Rivera, S.M. Shahidehpour, Application of games with incomplete information for pricing electricity in deregulated power pools, IEEE Transactions on Power Systems 13 (1) (1998 Feb.) 184–189.

[8] F.D. Galiana, M. Ilic, A mathematical framework for the analysis and management of power transactions under open access, IEEE Transactions on Power Systems 13 (2) (1998 May) 681– 687.

[9] T.W. Gedra, On transmission congestion and pricing, IEEE Transactions on Power Systems 14 (1) (1999 Feb.) 241–248.

[10] G. Gross, D.J. Finlay, G. Deltas, Strategic bidding in electricity generation supply markets, IEEE-PES Annual Conference Proceedings, NY, NY, 1999 (Feb.).

[11] B.H. Kim, M.L. Baughman, The economic efficiency impacts of alternatives for revenue reconciliation, IEEE Transactions on Power Systems 12 (3) (1997 August) 1129–1135.

[12] J. Mitra, C. Singh, Capacity assistance distributions for arbitrarily configured multi-area networks, IEEE Transactions on Power Systems 12 (4) (1997 Nov.) 1530 – 1535.

[13] M.A. Mostafa, M.E. El-Hawary, G.A.N. Mbamalu, M.M. Mansour, K.M. El-Nagar, A.M. El-Arabaty, A computational comparison of steady state load shedding approaches in electric power systems, IEEE Transactions on Power Systems 12 (1) (1997 Feb.) 30 – 37.

[14] S. Oren Shmuel, Design of ancillary service markets, Proceeding of the 34th Hawaii International Conference on Systems Sciences HICSS 34, Maui, Hawaii, January 5–8, 2001.

[15] N.S. Rau, Optimal dispatch of a system based on offers and bids—A mixed integer LP formulation, IEEE Transactions on Power Systems 14 (1) (1999 Feb.) 274– 279.

[16] D. Shirmohammadi, B. Wollenberg, A. Vojdani, P. Sandrin, M. Pereira, F. Rahimi, T. Schneider, B. Scott, Transmission dispatch and congestion management in the emerging energy market structures, IEEE Transactions on Power Systems 13 (4) (1998 Nov.) 1466 – 1474.

[17] H. Singh, A. Papalexopoulos, Competitive procurement of ancillary services by an independent system operator, IEEE Transactions on Power Systems 14 (2) (1999 May) 498–504.

[18] P. Skantze, J. Chapman, Price dynamics in the deregulated California energy market, IEEE-PES Annual Conference Proceedings, NY, NY, 1999 (February).

[19] G. Strbac, D. Kirschen, Assessing the competitiveness of demand-side bidding, IEEE Transactions on Power Systems 14 (1) (1999 Feb.) 120– 125.

[20] P. Visudhiphan, M.D. Ilic, Dynamic games-based modeling of electricity markets, IEEE-PES Annual Conference Proceedings, NY, NY, 1999 (February).

![](/api/attachments/AK9RQXSS/fulltext/images/b47fa5f8c9812caff1550ba3a6a518d8678bfebb337232da8a22187e238d98bd.jpg)

Ashkan R. Kian was borne in May 1970 in Tehran, Iran. He received his BSc degree in Electrical Engineering from University of Tehran, Iran (with Honors) in 1992. From 1992 to 1995, he worked for the Electric Power Research Center, Tehran, Iran. He received his MS and PhD degrees in Electrical Engineering from the Ohio State University in 1998 and 2001, respectively. Dr. Kian was the Vice President of Engineering and Devel-

opment at Genscape, Louisville, KY from September 2001 to October 2002. He is currently a Research Associate at the school of ECE, Cornell University. His research interests are: bidding strategies in dynamic energy multi-markets, game theory, stochastic optimal control, market monitoring, power systems operation and control.

Ali Keyhani is a fellow of IEEE and a recipient of the Ohio State University College of Engineering Research Award for 1989 and 1999. He established the Ohio State University Mechatronic graduate program in 1995 and he is the director of the Department of Electrical Engineering Mechatronic Systems Laboratory. His research interests are in the areas of electromechanical systems, power systems control and operation, power electronics, design of electric machines and parameter estimation. Dr. Keyhani is the Chairman of the Electric Machinery Committee and the past Editor of IEEE Transactions on Energy Conversion. He has been a consultant to Accuray, Combustion Engineering, Asea Brown Boveri, TRW Controls, Harris Controls, Liebert, Delphi Automotive Systems, Mahab Engineering, IRD, and Foster Wheeler Engineering. He has authored many papers in the IEEE Transactions on control of power systems, machine modeling, parameter estimation, power electronic systems, design of virtual and test beds for variable speed drive systems.
