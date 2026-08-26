---
otero_id: 7286
otero_key: "VHDGKPB8"
title: "Hedging risks with interruptible load programs for a load serving entity"
authors: "A.R. Hatami; H. Seifi; M.K. Sheikh-El-Eslami"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hedging risks with interruptible load programs for a load serving entity

A.R. Hatami <sup>a,1</sup>, H. Seifi <sup>b,</sup>⁎, M.K. Sheikh-El-Eslami <sup>b</sup>

<sup>a</sup> Bu-Ali Sina University, Hamedan, Iran

<sup>b</sup> Tarbiat Modares University, Tehran, Iran

## a r t i c l e i n f o

Article history: Received 5 March 2008 Received in revised form 17 June 2009 Accepted 22 July 2009 Available online 29 July 2009

Keywords: Load serving entity Interruptible load program Hedging Conditional value at risk Stochastic programming

## a b s t r a c t

In deregulated power systems, a load serving entity purchases electric energy from the wholesale market and sells it to its customers at regulated <sup>fi</sup>xed prices. The load serving entity faces several uncertainties in its trading. This paper addresses the hedging problem of a load serving entity with the aid of interruptible load programs. A method, based on stochastic programming, is proposed to determine the optimal procurement of interruptible loads for a speci<sup>fi</sup>ed period of time. The objective is to minimize the market risks presented by a multi-period risk measure. Meanwhile, the conditional value at risk approach is used to measure the risks. In addition, different types of interruptible contracts are considered and their effects on the optimal procurement policy are analyzed. A case study is illustrated to demonstrate the proposed method.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

During the past two decades, the electric industry throughout the world has been subject to major changes. The power industry has moved from a vertically integrated structure to a more competitive one. The restructuring of electric industry has changed the role of traditional entities and created new entities such as generation companies (GENCOs), regulated transmission companies (TRANSCOs), and load serving entities (LSEs) [31].

An LSE buys electricity from the wholesale market for resale to its customers. The price of electricity in the wholesale market is set by the supply and demand equilibrium. Consequently, the spot market price is uncertain and volatile, so the LSE is exposed to price risk. In addition, the LSE is obliged to meet the varying demand of its customers at regulated prices. Therefore, the LSE is faced with the uncertainties of customers' demand. Nevertheless, the most challenging problem faced by the LSE is the market price risk such that uncontrolled exposure to this risk could lead to devastating consequences. For example, in February 2004, the marginal clearing prices in ERCOT (Electric Reliability Council of Texas), during a 3-day ice storm reached the maximum allowable of \$999 per megawatt hour, causing one LSE, Texas Commercial Energy, to lose substantial amounts of money that led to bankruptcy [9,12].

Using risk management techniques for managing and controlling of such uncertainties is necessary. There are several instruments such as forward contracts, future contracts, call/put options, which can be used by the LSE for hedging against risks [9,25,36]. Interruptible service contract is another type to be used by the LSE for managing and controlling the risks [15].

Interruptible load programs are voluntary options, in which customers receive credits for permitting the utility to interrupt temporarily part or all of their loads during the period of the contract [5]. Generally, in an interruptible contract, the supply of customers is not interrupted. Instead, the customers who fail to comply are subject to severe penalties, thereby providing an incentive for customers to interrupt their loads. In an interruptible contract, the number of interruptions over the period of the contract, the maximum duration of each interruption, and the noti<sup>fi</sup>cation time required prior to an interruption, which is typically between 5 min and 24 h, are speci<sup>fi</sup>ed [5].

Many papers have addressed the issue of interruptible load programs. The proposed approaches can be classi<sup>fi</sup>ed as: improving power system reliability [8,23,34,37,38], designing appropriate incentive rates for interruptible load programs [10,19,24,32], and hedging against risks [1,15,20,30].

In the regulated environments, interruptible load program has been used as a load management technique for reducing utilities operating costs or mitigating capacity shortages [8,23]. In contrary, in deregulated power systems, interruptible load program has been used as an ancillary service [34], or as an equivalent price-based generating resource for improving power system reliability [37,38].

In Ref. [32], a methodology for designing priority pricing of interruptible load programs with an early noti<sup>fi</sup>cation option has been proposed. In Ref. [24], a double-call option has beenproposed that allows taking into account the effects of early noti<sup>fi</sup>cation of interruptions. In Ref. [10], using mechanism-design theory, an interruptible load program with optimal incentive rate structure has been designed. In Ref. [19], pricing of <sup>fi</sup>nancial contracts, using forward contracts and option derivatives, for the supply and procurement of interruptible load programs has been presented.

In Ref. [15], it has been shown that some voluntary options such as interruptible load services are Pareto-superior ex-ante, in that they bene<sup>fi</sup>t both the participants and the companies offering them, while notaffecting the non-participants. In Ref. [30], a methodology for assessing and valuing of demand-response options such as load curtailment has been proposed. In Ref. [20], a multi-period energy acquisition model for a distribution company, using options such as wholesale market purchase, distributed generations and interruptible load services has been proposed. In Ref. [1], a framework has been proposed to hedge a large retailer against risks by interruptible contracts, while it is assumed that the retailer can reduce the demand of the whole system by these contracts, and so the market price is reduced. Generally, the demand of a typical LSE is small as compared with the total demand of a power system. Therefore, it is reasonable to assume that the LSE is price-taker, i.e., its bidding actions do not in<sup>fl</sup>uence the spot market price [7,12,36].

In this paper, a price-taker LSE is considered. It is assumed that the LSE buys energy from bilateral contracts and the pool to meet the demand of its customers at <sup>fi</sup>xed prices. The pool market consists of two markets, day-ahead and real-time market. The LSE use bilateral contracts to reduce its risks. Nevertheless, the LSE may not be completely hedged against risks especially for all of its peak demand and/or peak market prices. In situations where a supply or demand shock occurs and consequently the spot market price is sharply increased, the LSE can use interruptible load programs to interrupt customers' service at a lower cost than serving them by purchasing power at high spot market prices [15].

This paper proposes a mathematical method, based on stochastic programming, to determine the optimal procurement of interruptible loads for the LSE within a medium-term period with the lead time of one to a few months. The objective is to minimize the risks in terms of a multi-period risk measure. Meanwhile, the conditional value at risk (CVaR) is used as a risk measurement index [27,28]. In addition, different types of interruptible contracts are considered and their effects on the optimal procurement policy are analyzed. Moreover, to model a realistic case, the available amounts of interruptible loads are considered as a function of the LSE's proposed pecuniary compensation. To apply this concept in the mathematical model, an acceptance function is presented. This function speci<sup>fi</sup>es the probability that the customers accept the interruptible contracts, given the LSE's proposed pecuniary compensation.

The rest of this paper is organized as follows. Basic methodologies are covered in Section 2. These include the problem assumptions, uncertainties characterization and risk modeling. In Section 3, the proposed mathematical formulation is described. Case study and results analysis are illustrated in Section 4 and <sup>fi</sup>nally conclusions are presented in Section 5.

## 2. Basic methodologies

## 2.1. Problem assumptions

In this paper, it is assumed that the sale price of electricity to the customers is given. In addition, the LSE, based on its strategies, has signed bilateral contracts with power producing companies.

Let T [h] denote the planning horizon. Generally, the planning horizon is divided into several periods, $t = 1 , . . . , T ,$ corresponding to the times at which decisions are made. In this paper, the planning horizon is discretized in hourly time steps.

## 2.2. Uncertainties characterization

The pro<sup>fi</sup>t of the LSE is in<sup>fl</sup>uenced by some uncertain factors such as market price, its demand and its competitors' strategies. Among them, the spot market price is more volatile and has much effect on the pro<sup>fi</sup>tability of the LSE. In this paper, only the uncertainties of the spot market price and the LSE's demand are considered.

There are several methods to account for the uncertainties of the spot market price such as time series approach, input/output hidden Markov model, and generalized autoregressive conditional heteroscedastic model (GARCH) [3,6,14]. Meanwhile, in some researches, it has been shown that the lognormal distribution functions can properly model the stochastic behavior of the spot market price [12,13,36]. In this paper, the uncertainties of the spot market price, at each period of the planning horizon (i.e., each hour) are modeled by a lognormal distribution function. The probability density function of the spot market price in period t, γ(s<sub>P,t</sub>), is given by:

$$
\gamma (s _ {P, t}): \ln (s _ {P, t}) \approx N (\mu_ {P, t}, \sigma_ {P, t} ^ {2})\tag{1}
$$

where $\mu _ { P , t }$ and $\sigma _ { P , t }$ are, respectively, the mean and the standard deviation of the normally distributed ln $\left( { { s _ { P , t } } } \right)$ in period t and ${ S } _ { P , t } { \in } { S } _ { P , t }$ is the index for a particular realization of the set of possible spot market prices in period $t , S _ { P , t }$

The uncertainties of the LSE's demand, at each period of the planning horizon can be described by a normal distribution function or a triangular distribution function [7,13]. In this paper, a normal distribution function is used to account for these uncertainties. Therefore, the probability density function of the LSE's demand in period $t , \gamma ( s _ { D , t } )$ , is given by:

$$
\gamma (s _ {D, t}): s _ {D, t} \approx N (\mu_ {D, t}, \sigma_ {D, t} ^ {2})\tag{2}
$$

where $\mu _ { D , t }$ and $\sigma _ { D , t }$ are, respectively, the mean and the standard deviation of the normally distributed $S _ { D , t }$ in period t and ${ S } _ { D , t } \in { S } _ { D , t }$ is the index for a particular realization of the set of possible LSE's demand in period $t , S _ { D , t }$

In most markets, there is a strong correlation between the market price and the load. However, for a typical LSE, the correlation of the market price and the demand depends on the size of the LSE. For some LSEs, this correlation is strong, while for the others, it may be weak. As suggested in Ref. [13], the correlation of the market price and the demand for small LSEs is weak, as the demand of such LSEs is not large enough to sway market prices. However, for large LSEs that can affect the market price by their actions, this correlation may be strong.

One approach to consider the correlation of the spot market price and the LSE's demand is to use a joint probability density function. This probability density function can be formed based on historical data. Since the marginal distributions of the market price and the LSE's demand are lognormally and normally distributed, respectively; it is reasonable to assume that the associated joint probability density function can be described by a bivariate normal distribution function [25,33]. This probability density function in period t is given by:

$$
\begin{array}{l} \gamma (s _ {P, t}, s _ {D, t}): (\ln s _ {P, t}, s _ {D, t}) \approx N (\mu_ {P, t}, \mu_ {D, t}, \sigma_ {P, t} ^ {2}, \sigma_ {D, t} ^ {2}, \rho) \\ \rho = C o r r (\ln s _ {P, t}, s _ {D, t}) \end{array}\tag{3}
$$

where $\rho$ is the correlation coef<sup>fi</sup>cient of $\ln ( s _ { P , t } )$ and $s _ { D , t } .$

Based on this probability density function, a set of joint realizations of the spot market price and the LSE's demand can be generated for each period (hour) of the planning horizon. Plausible evolutions of the random variables, the market price and the LSE's demand, during the planning horizon can be speci<sup>fi</sup>ed by a scenario tree. A scenario tree consists of a set of nodes and branches. Each node re<sup>fl</sup>ects a point at which decisions are made and captures a joint realization of random variables at that time. Therefore, a scenario tree consists of a sequence of joint realizations of the random variables during the planning horizon, where in each scenario the prices (demands) across hours exhibit some autocorrelations (see Appendix $\mathsf { A } ) .$ . The number of scenario trees is considered to be equal to the number of joint realizations of random variables generated at each period.

## 2.3. Risk modeling

Risk results from uncertainty about the future and is the possibility of suffering harm or loss. Risk management is the process of identifying, controlling and minimizing risks and evaluating the results. Several techniques can be found in the literature to introduce risk management into decision-making. Some of them are mean-variance technique, value at risk (VaR) approach and CVaR methodology.

The mean-variance technique is a cornerstone of modern portfolio theory [26]. This model has been extensively utilized to manage portfolio risk. However, mean-variance approach is not appropriate for the LSE, as the LSE is exposed to the risks only when it purchases/ sells electric energy at prices higher/lower than the expected [12].

VaR is a downside and quantile risk measure. In practice, it is a widely accepted risk measure. For a speci<sup>fi</sup>ed con<sup>fi</sup>dence level $\beta ,$ the $\mathrm { V a R } _ { \beta }$ of a portfolio is the lowest amount ζ such that with a probability of $\beta ,$ the loss will not exceed ζ [27]. This risk measure can be easily calculated when the loss function is normally (lognormally) distributed. However, for non-normal distributions which in fact are often the case, VaR may have undesirable properties, such as lack of subadditivity and convexity, so it fails to be a coherent risk measure [28]. The other drawback of this approach is that portfolio optimization problems with VaR objectives or constraints are generally hard to solve numerically and may have multiple local extrema [27]. A serious limitation of VaR, in addition, is that it takes no account of the size of the losses, which may occur beyond the threshold amount indicated by this measure [28].

CVaR as another percentile risk measure is a modi<sup>fi</sup>cation of VaR that has not the drawbacks of VaR [28]. Consequently, it is a coherent risk measure [27]. It is also known as the mean excess loss or mean shortfall and is de<sup>fi</sup>ned as the conditional expectation of losses given that the loss exceeds a threshold value. Mathematically, for a speci<sup>fi</sup>ed con<sup>fi</sup>dence level $\beta , \mathrm { C V a R } _ { \beta }$ of a portfolio is de<sup>fi</sup>ned as the expected value of the loss function in the $( 1 - \beta ) \times 1 0 0 \%$ worst cases (Fig. 1). For example, a 95% con<sup>fi</sup>dence CVaR value, $\mathrm { C V a R } _ { 0 . 9 5 } ,$ , provides the mean of the expected losses for the potential loss values that exceed the $\mathsf { V a R } _ { 0 . 9 5 }$ value.

In recent years, risk assessment techniques, based on CVaR, have been used in the electricity market. For example, CVaR has been applied to address: (a) the integrated risk management problem of a hydrothermal generation company [4], (b) the electricity procurement problem of a large consumer [6], (c) the self-scheduling problem of a power producing company in an uncertain environment [18], and (d) the determination of selling price for an electric retailer [7].

CVaR can be expressed by a minimization formula. Let $x \in R ^ { n }$ denote the decision vector, $\xi \in R ^ { m }$ denote the random vector, f(x,ξ): $R ^ { n } { \times } R ^ { m } { \to } R$ denote the loss function, $\begin{array} { r } { . p ( \xi ) { : } R ^ { m } \to } \end{array}$ R denote the probability distribution function of random vector, and N denote the number of scenarios. The minimum of $C V a R _ { \beta } ( f ( x , \xi ) )$ can be calculated as [28]:

![](/api/attachments/VHDGKPB8/fulltext/images/87f7adf0019724a5a56dd6ffe6bf02c60f9077bdd3577312d28e14a94ee73460.jpg)  
Fig. 1. VaR and CVaR with a con<sup>fi</sup>dence level of β.

$$
\underset {x} {\text { Min }} C V a R _ {\beta} (f (x, \xi)) = \underset {x, \zeta} {\text { Min }} \zeta + (1 - \beta) ^ {- 1} \sum_ {k = 1} ^ {N} p (\xi^ {k}) \cdot (\max ([ f (x, \xi^ {k}) - \zeta ], 0)).\tag{4}
$$

## 3. Proposed mathematical formulation

## 3.1. Calculating the expected profit of interruptible load programs

In deregulated power markets, there are several options for interruptible contracts. Refs. [5,11,16,22] provide some real-world examples for implementing of these contracts. However, in this paper, two particular types of interruptible contracts, which appear to be more common than the others, are considered [5]. In the <sup>fi</sup>rst form, the participating customers receive compensation for per unit of interrupted load, which is typically higher than the sale price of the electricity (type 1). In the second form, the participating customers receive a discount on their electricity rates for the amounts that are subject to curtailment (type 2) [1,5]. It is assumed that each customer can only participate in one type of interruptible load programs.

Let k denote the types of interruptible contracts $( k = 1$ for type 1 and $k = 2$ for type 2), $N P _ { k } ^ { \mathrm { i n t } }$ denote the number of permitted interruptions type $k ,$ over the period of contract, $M D _ { k } ^ { \mathrm { i n t } }$ [h] denote the maximum duration of interruption type k, and $M L _ { k } ^ { \mathrm { i n t } }$ [MW] denote the selected amounts of interruptible program type k. To model a realistic case, $M L _ { k } ^ { \mathrm { i n t } }$ is considered as a function of compensation/ discount rate, as if the compensation rate or the discount rate is high/ low, many/few customers are willing to sign interruptible contracts with the LSE. To apply this concept, an acceptance function, $a c f ( . )$ , is proposed. This function speci<sup>fi</sup>es the probability that the customers accept the interruptible contracts (type1/type2), given the LSE's suggested compensation/discount rate.

$$
\begin{array}{l} M L _ {1} ^ {\text { int }} = M L _ {1} ^ {\text { int,max }} \cdot a c f (\lambda^ {\text { comp }}) \\ M L _ {2} ^ {\text { int }} = M L _ {2} ^ {\text { int,max }} \cdot a c f (D R) \end{array}\tag{5}
$$

where ML<sup>int,max</sup> [MW] is the maximum interruptible load type 1, acf $\left( \lambda ^ { \mathrm { { c o m p } } } \right)$ is the acceptance function of interruptible load type 1 (as a function of compensation rate), $M L _ { 2 } ^ { \mathrm { i n t , m a x } }$ [MW] is the maximum interruptible load type 2, and $a c f ( D R )$ is the acceptance function of interruptible load type 2 (as a function of the discount rate). The maximum interruptible loads (type 1 and type 2) are determined based on some factors such as the volume of customers' demands, the customers' demands characteristics, and the value of electricity for different customers.

As stated before, in each interruptible contract, the number of interruptions over the period of the contract, and the maximum duration of each interruption are known. Therefore, the planning horizon, T, is divided into H sub-periods. Let $T _ { h }$ denote the duration of sub-period $\ i , \ h { = } 1 , \ 2 , . . . , H , \ T { = } H { \times } T _ { h } .$ . The participating customers can be interrupted only once in each sub-period such as one day, two days, and one week. Moreover, $M L _ { k } ^ { \mathrm { i n t } }$ can be represented as multiples of a block size $( \Delta P _ { k } ^ { \mathrm { i n t } } \left( \mathrm { M W } \right) )$ ). Therefore, the interrupted load of type k, at hour t and scenario $s , s = 1 , 2 , . . . , S , P _ { k , s , i } ^ { \mathrm { i n t } }$ (MW), can vary from 0 to $M L _ { k } ^ { \mathrm { i n t } }$ in steps of $\Delta P _ { k } ^ { \mathrm { i n t } }$ and is given by:

$$
P _ {k, s, t} ^ {\text { int }} = \left\{0, \Delta P _ {k} ^ {\text { int }}, 2 \cdot \Delta P _ {k} ^ {\text { int }},..., M L _ {k} ^ {\text { int }} \right\}; k = 1, 2; s = 1, 2,..., S; t = 1, 2,... T.\tag{6}
$$

The expected pro<sup>fi</sup>t of the LSE due to interruptible contracts, PROFIT<sup>int</sup> (\$), can be given by:

$$
P R O F I T ^ {\text { int }} = \sum_ {s = 1} ^ {S} \pi_ {s} \cdot \left(\sum_ {k = 1} ^ {2} \sum_ {t = 1} ^ {T} p r o f i t _ {k, s, t} ^ {\text { int }}\right)\tag{7}
$$

$$
\operatorname{profit} _ {1, s, t} ^ {\text { int }} = \left[ \left(\lambda_ {s, t} ^ {\text { mcp }} - S P - \lambda^ {\text { comp }}\right) \cdot P _ {1, s, t} ^ {\text { int }} \right]\tag{8}
$$

$$
p r o f i t _ {2, s, t} ^ {\mathrm{int}} = (\lambda_ {s, t} ^ {\mathrm{mcp}} - S P) \cdot P _ {2, s, t} ^ {\mathrm{int}} - (1 - D R) \cdot S P \cdot (M L _ {2} ^ {\mathrm{int}} - P _ {2, s, t} ^ {\mathrm{int}})\tag{9}
$$

$$
\sum_ {t = t _ {1}} ^ {h \cdot T _ {h}} \left| P _ {k, s, t + 1} ^ {\text { int }} - P _ {k, s, t} ^ {\text { int }} \right| / \max (\Delta P _ {k} ^ {\text { int }}, \left| P _ {k, s, t + 1} ^ {\text { int }} - P _ {k, s, t} ^ {\text { int }} \right|) \leq 2;\tag{10}
$$

$$
t _ {1} = 1 + (h - 1) \cdot T _ {h}; h = 1, 2, \dots , H; s = 1, 2, \dots , S
$$

$$
\sum_ {t = t _ {1}} ^ {h \cdot T _ {h}} P _ {k, s, t} ^ {\text { int }} \leq M D _ {k} ^ {\text { int }} \cdot M L _ {k} ^ {\text { int }}; t _ {1} = 1 + (h - 1) \cdot T _ {h}; k = 1, 2; h = 1, 2,..., H; s = 1, 2,..., S\tag{11}
$$

$$
\sum_ {t = 1} ^ {T} P _ {k, s, t} ^ {\mathrm{int}} \leq N P _ {k} ^ {\mathrm{int}} \cdot M D _ {k} ^ {\mathrm{int}} \cdot M L _ {k} ^ {\mathrm{int}}; k = 1, 2; s = 1, 2,..., S\tag{12}
$$

where profit<sup>int</sup> [\$] is the pro<sup>fi</sup>t of the LSE due to the interruptible contract type $k ,$ at hour t and scenario $s , \ \pi _ { s }$ is the probability of scenario s, λ<sup>mcp</sup> [\$/MWh] is the spot market price, at hour t and scenario s, SP [\$/MWh] is the sale price of electricity to the customers, λ<sup>comp</sup> [\$/MWh] is the compensation for per unit of interrupted load that the customers receive in interruptible program type 1, and DR is the discount rate that the customers receive on their electricity rates (for example 10%) in interruptible program type 2.

In expression $( 7 ) ,$ the expected pro<sup>fi</sup>t is determined. It is calculated as the sum over all scenarios of the pro<sup>fi</sup>t multiplied by their respective probabilities. In expressions (8) and $( 9 ) ,$ the pro<sup>fi</sup>ts of the interruptible contract types 1 and 2, at hour t and scenario s, are calculated, respectively. Expression (10) limits the number of interruptions in each sub-period so that the participants can be interrupted only once in each sub-period. Expression (11) limits the interruption duration in each sub-period, and <sup>fi</sup>nally expression (12) limits the number of interruptions over the period of the contract.

## 3.2. Objective function

The expected pro<sup>fi</sup>t of the LSE due to interruptible contracts can be negligible, but the LSE can be hedged against risks using these contracts. Therefore, the objective function of the LSE can be formulated as minimizing the risk measure. The risk measure is de<sup>fi</sup>ned as the weighted average of the CVaR of the loss function at each hour, at con<sup>fi</sup>dence level of $\beta .$ The loss function is considered to be the negative of the pro<sup>fi</sup>ts due to interruptible contracts. Therefore, the objective function can be expressed as:

$$
\text { Minimize } \sum_ {t = 1} ^ {T} \delta_ {t} \cdot C V a R _ {\beta} \left(- \sum_ {s = 1} ^ {S} \sum_ {k = 1} ^ {2} (\pi (s) \cdot p r o f i t _ {k, s, t} ^ {\text { int }})\right)\tag{13}
$$

subject to

$$
P R O F I T ^ {\text { int }} \geq C
$$

where in Eq. (13), β represents the probability level at which CVaR is evaluated and is typically set to 95%. In addition, $\delta _ { t }$ is the weighting factor of the CVaR at hour t. The weighting factors of different hours are considered to be equal, $\delta _ { t } = 1 , \forall t \in T .$ The parameter C in expression (13) models the preferences of the LSE. CN0 means that the LSE wishes to achieve pro<sup>fi</sup>t in addition to hedging against risks. $C = 0$ means that interruptible contracts are used only to hedge against risks. $C { < } 0$ means that the LSE is willing to lose some money to be better hedged against risks. It is obvious that the degree of hedging against risks is increased as C decreases. The complete formulation can be given by:

$$
\underset {\zeta_ {t}, P _ {k, s, t} ^ {\text { int }}} {\text { Minimize }} \sum_ {t = 1} ^ {T} \left(\zeta_ {t} + \frac {1}{(1 - \beta)} \cdot \sum_ {s = 1} ^ {S} \pi_ {s} \cdot \mu_ {s, t}\right)\tag{14}
$$

subject to:

$$
\left[ (\lambda_ {s, t} ^ {\mathrm{mcp}} - S P - \lambda^ {\mathrm{comp}}) \cdot P _ {1, s, t} ^ {\mathrm{int}} \right] + [ (\lambda_ {s, t} ^ {\mathrm{mcp}} - S P) \cdot P _ {2, s, t} ^ {\mathrm{int}} - (1 - D R) \cdot S P \cdot (M L _ {2} ^ {\mathrm{int}} - P _ {2, s, t} ^ {\mathrm{int}}) ]
$$

$$
+ \mu_ {s, t} + \zeta_ {t} \geq 0; s = 1, 2, \dots , S; t = 1, 2, \dots , T\tag{15}
$$

$$
\mu_ {s, t} \geq 0; s = 1, 2, \dots , S; t = 1, 2, \dots , T\tag{16}
$$

$$
\sum_ {s = 1} ^ {S} \pi (s) \cdot \left(\sum_ {t = 1} ^ {T} \left[ (\lambda_ {s, t} ^ {\mathrm{mcp}} - S P - \lambda^ {\mathrm{comp}}) \cdot P _ {1, s, t} ^ {\mathrm{int}} \right]\right) + \sum_ {s = 1} ^ {S} \pi (s)
$$

$$
\times \left(\sum_ {t = 1} ^ {T} (\lambda_ {s, t} ^ {\mathrm{mcp}} - S P) \cdot P _ {2, s, t} ^ {\mathrm{int}} - (1 - D R) \cdot S P \cdot (M L _ {2} ^ {\mathrm{int}} - P _ {2, s, t} ^ {\mathrm{int}})\right) \geq C\tag{17}
$$

and expressions (5), (6), (10), (11), and (12).

The overall model is a mixed-integer stochastic programming problem that can be solved by decomposition methods such as branch-and-bound method [2,29]. The decision variables of the problem are the amounts of interrupted loads of each type and in each hour. In addition to these variables, the VaR at each hour, $\zeta _ { t } ,$ is also determined by solving the problem. The problem could have large dimensions due to the need for a suf<sup>fi</sup>ciently large number of scenarios for an accurate representation of the uncertainty. Without loss of generality, it can be assumed that the interrupted loads of each type at off-peak hours are zero. By this assumption, the dimension of the problem can be reduced to about 50%.

## 4. Case study and results analysis

## 4.1. Data

The performance of the proposed method is illustrated through a case study. A contractual period of three months is considered. The daily peak period is considered as 06:00–22:00 (5×16) and the remaining hours are considered as the daily off-peak period $( 5 \times 8 + 2 \times 2 4 )$ . The day-ahead locational marginal prices (LMPs) of New England Connecticut zone [17] during three months, ended August 30, 2007, are used as the predicted mean spot market price (Fig. 2). The analysis of historical market data of this zone shows a standard deviation of 6.5% for logarithm of the spot market price. Therefore, the mean and the standard deviation of the market price in hour t, i.e., $\mu _ { P , t }$ and $\sigma _ { P , t }$ in expression (3), are set to the logarithm and 6.5% of the logarithm of the predicted market price in hour t, respectively.

![](/api/attachments/VHDGKPB8/fulltext/images/1d3bacf4b9c5c87d41b9b80e353833cb04e354bb0f9ba32e1dd080b7483e3337.jpg)  
Fig. 2. The predicted hourly market price.

![](/api/attachments/VHDGKPB8/fulltext/images/3443eaa375bf3affe1484323a6065ebfc1c79e7298bfaf53f03b02aa0823e5fb.jpg)  
Fig. 3. The predicted hourly demand of the LSE.

In addition, a percentage of Connecticut zone demand during three months, ended August 30, 2007, shown in Fig. 3 at hourly level, is considered as the LSE's demand [17]. The analysis of historical data of this zone shows a standard deviation of 8% for the considered demand. Therefore, the mean and the standard deviation of the demand in hour t, $\mathrm { i } . \mathrm { e } . , \mu _ { D , t }$ and $\sigma _ { D , t }$ in expression (3), are set to the predicted demand and 8% of the predicted demand in hour t, respectively.

Generally the correlation between the market price and the demand for a price-taker LSE is weak. Therefore the correlation coef<sup>fi</sup>cient between the demand and the logarithm of the price, ρ in expression (3), is set to 0.1. By replacing the parameters related to each hour, i.e., ${ \mathrm { \Delta } } , { \mu } _ { P , t } , { \sigma } _ { P , t } , { \mu } _ { D , t } , { \sigma } _ { D , t }$ and ρ in expression (3), a set of joint realizations of the stochastic variables are generated for each hour. Using these joint realizations of random variables, a set of scenarios is generated so that their number will be equal to the number of joint realizations of random variables at each hour.

The sale price of the electricity and the selected forward contracts are shown in Table 1. The cost of the forward contracts is determined based on the expected predicted price over the relevant period. The sale price is determined based on the rate of return. At the sale price of 84 \$/MWh, the rate of return of the LSE is approximately 10%.

The parameters of the interruptible load programs are shown in Table 2 [5]. In addition, the acceptance functions of interruptible programs, type 1 and type 2, are shown in Figs. 4 and 5, respectively.

## 4.2. Results analysis

The number of considered scenarios affects the results of the problem. A low number of scenarios may result in inaccuracy, while a large number of scenarios requires high computational burden. To determine the number of scenarios required for an accurate representation of the uncertainties, the expected pro<sup>fi</sup>t versus the number of

## Table 1

The selected forward contracts and the sale price.

<table><tr><td colspan="2"></td><td>Price ($/MWh)</td><td>Purchased power (MW)</td></tr><tr><td rowspan="2">Forward contracts</td><td>On-peak</td><td>84.5</td><td>500</td></tr><tr><td>Round-the-clock</td><td>72</td><td>3000</td></tr><tr><td colspan="4">Sale price: 84 $/MWh</td></tr><tr><td colspan="4">Expected market price: 68.5 $/MWh</td></tr><tr><td colspan="4">Expected market price of on-peak hours: 80.4 $/MWh</td></tr></table>

Table 2  
The parameters of interruptible load programs (types 1 and 2)

<table><tr><td></td><td>T (month)</td><td> $NP^{int}$ </td><td> $MD^{int}$  (h)</td><td> $T_h$  (day)</td><td> $ML^{int,max}$  (MW)</td><td> $\Delta P^{int}$  (MW)</td></tr><tr><td>Interruptible program type 1</td><td>3</td><td>9</td><td>4</td><td>1</td><td>1000</td><td>50</td></tr><tr><td>Interruptible program type 2</td><td>3</td><td>9</td><td>4</td><td>1</td><td>500</td><td>10</td></tr></table>

![](/api/attachments/VHDGKPB8/fulltext/images/68f1f30df552a9bb5bc52361ad997c10ef130ee6789675686a681ecf25840129.jpg)

Fig. 4. The acceptance function of interruptible program type 1.  
![](/api/attachments/VHDGKPB8/fulltext/images/df9f00661b649600e43ce21322b23a8969dfd95a00ba4469bb88bc60cd87b812.jpg)  
Fig. 5. The acceptance function of interruptible program type 2.

![](/api/attachments/VHDGKPB8/fulltext/images/8d6b5eb863fb3e2acae258a7c21b9039f9964c021d00faa50be989d2de51b733.jpg)  
Fig. 6. The expected pro<sup>fi</sup>t versus the number of considered scenarios

scenarios is plotted in Fig. 6. As shown, the expected pro<sup>fi</sup>t is stabilized after 100 scenarios. Therefore, 100 scenarios are considered.

To analyze the effects of interruptible programs, seven cases are considered as follows:

• Usual cases:

a) Case 1: base case;

b) Case 2: use of interruptible load program type 1;

c) Case 3: use of interruptible load program type 2;

d) Case 4: use of both interruptible load programs.

• Unusual cases (supply shock occurring):

e) Case 5: base case;

f) Case 6: use of both interruptible load programs;

g) Case 7: use of both interruptible load programs with steeper acceptance function.

The expected pro<sup>fi</sup>t and $\mathrm { C V a R } _ { 0 . 9 5 }$ of the base case (case 1), where the LSE procures its demand from the pool and forward contracts, are shown in Table 3. To explain the results better, $\mathrm { C V a R } _ { 0 . 9 5 }$ of the pro<sup>fi</sup>t is calculated instead of $\mathrm { C V a R } _ { 0 . 9 5 }$ of the negative of the pro<sup>fi</sup>t.

## Table 3

The results of the base case (case 1).

<table><tr><td>Expected profit ($)</td><td> $CVaR_{0.95}$  ($)</td></tr><tr><td> $62.677 \times 10^{6}$ </td><td> $-15.105 \times 10^{6}$ </td></tr></table>

Table 4  
The results of case 2.

<table><tr><td>C ($)</td><td>200,000</td><td>&lt;200,000</td></tr><tr><td> $\Delta Profit^{int}$ ($)</td><td>204,852</td><td>204,852</td></tr><tr><td> $\Delta CVaR_{0.95}$ ($)</td><td>201,500</td><td>201,500</td></tr><tr><td>Compensation rate ($/MWh)</td><td>90</td><td>90</td></tr><tr><td> $ML_{1}^{int}$ (MW)</td><td>400</td><td>400</td></tr></table>

In case 2, the effects of interruptible program type 1 are analyzed. Therefore, it is assumed that only the interruptible load program type 1 is available. Table 4 shows the results of this case. The $\Delta P r o f i t / \Delta C \mathrm { V a R } _ { 0 . 9 5 }$ is de<sup>fi</sup>ned as: $\Delta P r o f i t / \Delta \mathrm { C V a R } _ { 0 . 9 5 } = ( P r o f i t / \mathrm { C V a R } _ { 0 . 9 5 } ) _ { ( \mathrm { a ) } } - ( P r o f i t /$ $\mathrm { C V a R } _ { 0 . 9 5 } ) _ { ( \mathrm { b } ) } ,$ , where (a) is the case when interruptible contracts are used and (b) is the base case (i.e., when interruptible contracts are not used). It is observed that using interruptible contracts type 1, the expected pro<sup>fi</sup>t is increased and the risks are decreased. As shown in Table 4, the optimal solution is obtained when the LSE procures 400 MW at the compensation rate of 90 \$/MWh. It can be seen that as C decreases, $\Delta \mathrm { C V a R } _ { 0 . 9 5 }$ does not increase, i.e., the LSE cannot reduce its risks by losing some pro<sup>fi</sup>ts. The reason is the facts that for this type of interruptible program, generally maximizing the expected pro<sup>fi</sup>t and minimizing the risks occur simultaneously, as the interruptible programs mainly affect the periods that have the highest prices.

In case 3, the effects of interruptible program type 2 are analyzed. The results are shown in Table 5. As shown, $\mathrm { f o r } C \ge 0 ,$ , there is no solution, i.e., the LSE cannot reduce its risks without losing some money. However, by losing some money, the LSE can reduce its risks. It can be seen as C decreases, $\Delta \mathrm { C V a R } _ { 0 . 9 5 }$ increases, so the risks decrease. Therefore, the LSE loses some money in exchange for reducing its risks.

Table 6 shows the results of case 4. In this case, the LSE uses both types of interruptible load programs. As shown in Table 6, for some values of C, for which ΔProfit and $\Delta C V a R _ { 0 . 9 5 }$ are greater than zero, the LSE can achieve pro<sup>fi</sup>t in addition to reducing its risks. As $\Delta C V a R _ { 0 . 9 5 }$ increases, ΔProfit decreases and for some values of $C , \Delta P r o f i t { < } 0 .$ . This means that the LSE may even lose some money to be better hedged against risks. It is observed that as C varies, the optimal procurement policy is changed, but this change is limited to interruptible load program type 2. For example, for $C = 0 ,$ , the optimal procurement policy consists of procuring 400 MW of interruptible program type 1 at the compensation rate of 90 \$/MWh and 30 MW of interruptible program type 2 at the discount rate of 4%.

In cases 5–7, it is assumed that due to a supply shock, the market prices at on-peak hours in some days (four days of a week) are sharply increased. Meanwhile, it is assumed that the LSE's demand remains unchanged. The market prices of such shock are depicted in Fig. 7. In order to properly generate a set of joint realizations of the stochastic variables during the supply shock, σ and ρ in expression (3) are set to 0.1% of the logarithm of the predicted market price and 0, respectively.

Table 5  
The results of case 3.

<table><tr><td>C ($)</td><td> $\geq 0$ </td><td>-100,000</td><td>-200,000</td><td>-300,000</td><td>-400,000</td></tr><tr><td> $\Delta Profit^{int}$ ($)</td><td>No solution</td><td>-62,702</td><td>-188,106</td><td>-250,808</td><td>-376,212</td></tr><tr><td> $\Delta CVaR_{0.95}$ ($)</td><td></td><td>60,538</td><td>181,614</td><td>242,152</td><td>363,228</td></tr><tr><td>Discount rate (%)</td><td></td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td> $ML_{2}^{int}$ (MW)</td><td></td><td>10</td><td>30</td><td>40</td><td>60</td></tr></table>

Table 6  
The results of case 4.

<table><tr><td>C ($)</td><td>300,000</td><td>200,000</td><td>100,000</td><td>0</td><td>-100,000</td><td>-200,000</td></tr><tr><td> $\Delta Profit^{int}$ ($)</td><td>No</td><td>204,852</td><td>142,150</td><td>16,746</td><td>-45,956</td><td>-171,360</td></tr><tr><td> $\Delta CVaR_{0.95}$ ($)</td><td>solution</td><td>201,500</td><td>260,465</td><td>381,198</td><td>440,102</td><td>560,774</td></tr><tr><td>Compensation rate ($/MWh)</td><td></td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td></tr><tr><td> $ML_{1}^{int}$ (MW)</td><td></td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td></tr><tr><td>Discount rate (%)</td><td></td><td>-</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td> $ML_{2}^{int}$ (MW)</td><td></td><td>0</td><td>10</td><td>30</td><td>40</td><td>60</td></tr></table>

![](/api/attachments/VHDGKPB8/fulltext/images/74f09001502f871127666b5d360483ce56f8a02377b284cedfcfaef78934437c.jpg)  
Fig. 7. The market price during a supply shock.

The expected pro<sup>fi</sup>t and $\mathrm { C V a R } _ { 0 . 9 5 }$ of the LSE in case 5, i.e., the base case when a supply shock occurs, are shown in Table 7. It is observed that the expected pro<sup>fi</sup>t and the $\mathrm { C V a R } _ { 0 . 9 5 }$ of case 5 are reduced 16.3% and 204.5%, respectively, as compared with case 1.

The effects of interruptible load programs (when a supply shock occurs) are analyzed in case 6. In this case no value is assigned to parameter C in Eq. (17). The results are shown in Table 8. It is observed that using interruptible contracts, the expected pro<sup>fi</sup>t is considerably increased and the risks are signi<sup>fi</sup>cantly decreased. For example, by selecting 400 MW and 30 MW of interruptible programs type 1 and type 2, respectively, the expected pro<sup>fi</sup>t and $\mathrm { C V a R } _ { 0 . 9 5 }$ are increased by 8.6% and 9.1%, respectively.

In case 7, the effects of increasing compensation/discount rates on the results of case 6 are studied. In fact, this case is a re-run of case 6 with steeper acceptance functions. The reason for this is that if the LSE is experiencing a supply shock and the associated increase in spot market prices, the customers may require more compensation to accept an interruptible load contract, as they expect their loads to be interrupted more frequently. The results as well as the new compensation/discount rates are shown in Table 9. It can be observed that by increasing compensation and/or discount rates, the expected pro<sup>fi</sup>t is decreased and the risks are increased as compared with case 6, but in comparison with case 5, the results show signi<sup>fi</sup>cant effects on the expected pro<sup>fi</sup>t increasing and/or risks decreasing.

By comparing the results of cases 1–7, it is observed that in normal state, interruptible contracts have insigni<sup>fi</sup>cant effects on the expected pro<sup>fi</sup>t increasing and/or risks decreasing. However, when the market prices are sharply increased due to a shock in supply and/or demand, which can be found in many electricity markets (for example: Nord Pool, at the end year 2002 [21], ERCOT in years 2001, 2002, 2003, and 2004 [39], and California electricity market in years 1999 and 2001 [9]), this option can be used as a main tool for hedging against risks.

Table 7 The results of case 5.

<table><tr><td>Expected profit ($)</td><td>CVaR0.95 ($)</td></tr><tr><td> $52.460 \times 10^{6}$ </td><td> $-46.0 \times 10^{6}$ </td></tr></table>

Table 8  
The results of case 6.

<table><tr><td> $\Delta Profit^{int} (\$)$ </td><td> $4.131 \times 10^{6}$ </td><td> $4.263 \times 10^{6}$ </td><td> $4.525 \times 10^{6}$ </td><td> $4.657 \times 10^{6}$ </td><td> $4.920 \times 10^{6}$ </td></tr><tr><td> $\Delta CVaR_{0.95} (\$)$ </td><td> $3.925 \times 10^{6}$ </td><td> $4.092 \times 10^{6}$ </td><td> $4.2083 \times 10^{6}$ </td><td> $4.378 \times 10^{6}$ </td><td> $4.625 \times 10^{6}$ </td></tr><tr><td>Compensation rate ($/MWh)</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td></tr><tr><td> $ML_{1}^{int} (MW)$ </td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td></tr><tr><td>Discount rate (%)</td><td>-</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td> $ML_{2}^{int} (MW)$ </td><td>0</td><td>10</td><td>30</td><td>40</td><td>60</td></tr></table>

Table 9  
The results of case 7.

<table><tr><td> $\Delta Profit^{int} (\$)$ </td><td> $3.267 \times 10^{6}$ </td><td> $3.305 \times 10^{6}$ </td><td> $3.379 \times 10^{6}$ </td><td> $3.415 \times 10^{6}$ </td><td> $3.489 \times 10^{6}$ </td></tr><tr><td> $\Delta CVaR_{0.95} (\$)$ </td><td> $3.104 \times 10^{6}$ </td><td> $3.143 \times 10^{6}$ </td><td> $3.243 \times 10^{6}$ </td><td> $3.261 \times 10^{6}$ </td><td> $3.318 \times 10^{6}$ </td></tr><tr><td>Compensation rate ($/MWh)</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td></tr><tr><td> $ML_{1}^{int} (MW)$ </td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td></tr><tr><td>Discount rate (%)</td><td>-</td><td>10</td><td>10</td><td>10</td><td>10</td></tr><tr><td> $ML_{2}^{int} (MW)$ </td><td>0</td><td>10</td><td>30</td><td>40</td><td>60</td></tr></table>

Table 10  
The results for different values of forward contracts.

<table><tr><td colspan="2"></td><td>Expected profit ($)</td><td> $CVaR_{0.95}$  ($)</td></tr><tr><td rowspan="2">Case 1</td><td>FW1</td><td> $66.010 \times 10^6$ </td><td> $-87.500 \times 10^6$ </td></tr><tr><td>FW2</td><td> $60.239 \times 10^6$ </td><td> $-8.332 \times 10^6$ </td></tr><tr><td rowspan="2">Case 5</td><td>FW1</td><td> $-44.067 \times 10^6$ </td><td> $-585.0 \times 10^6$ </td></tr><tr><td>FW2</td><td> $68.800 \times 10^7$ </td><td> $-36.280 \times 10^6$ </td></tr></table>

Table 11  
The effects of interruptible programs (during the supply shock).

<table><tr><td rowspan="2">FW1</td><td> $\Delta Profit^{int} (\$)$ </td><td> $4.868 \times 10^{6}$ </td><td> $4.992 \times 10^{6}$ </td><td> $5.241 \times 10^{6}$ </td><td> $5.366 \times 10^{6}$ </td><td> $5.6146 \times 10^{6}$ </td></tr><tr><td> $\Delta CVaR_{0.95} (\$)$ </td><td> $4.624 \times 10^{6}$ </td><td> $4.717 \times 10^{6}$ </td><td> $4.932 \times 10^{6}$ </td><td> $5.044 \times 10^{6}$ </td><td> $5.266 \times 10^{6}$ </td></tr><tr><td rowspan="2">FW2</td><td> $\Delta Profit^{int} (\$)$ </td><td> $3.681 \times 10^{6}$ </td><td> $3.787 \times 10^{6}$ </td><td> $3.999 \times 10^{6}$ </td><td> $4.105 \times 10^{6}$ </td><td> $4.317 \times 10^{6}$ </td></tr><tr><td> $\Delta CVaR_{0.95} (\$)$ </td><td> $3.479 \times 10^{6}$ </td><td> $3.635 \times 10^{6}$ </td><td> $3.787 \times 10^{6}$ </td><td> $3.859 \times 10^{6}$ </td><td> $4.058 \times 10^{6}$ </td></tr><tr><td colspan="2">Compensation rate ($/MWh)</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td></tr><tr><td colspan="2"> $ML_{1}^{int} (MW)$ </td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td></tr><tr><td colspan="2">Discount rate (%)</td><td>-</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td colspan="2"> $ML_{2}^{int} (MW)$ </td><td>0</td><td>10</td><td>30</td><td>40</td><td>60</td></tr></table>

## 4.3. Sensitivity analysis

As mentioned before, forward contracts are the ef<sup>fi</sup>cient means for hedging against risks. To determine how assumed contracts (forward contracts) affect the results, two scenarios with different volumes of forward contracts are considered (as compared with Table 1).

• Scenario FW1: In this scenario, it is assumed that the LSE procures its demand only from the pool. In other words, the LSE does not sign any forward contract.

(a)  
![](/api/attachments/VHDGKPB8/fulltext/images/acd275f97735e0cf3f4909d828616ace18812596ca6e01a509631f2f97fa5dc0.jpg)  
(b)

![](/api/attachments/VHDGKPB8/fulltext/images/8e7265d6226a71a5bd1d89035057e820f9f28793f5121a8ffd783ac807c73203.jpg)

• Scenario FW2: In this scenario, it is assumed that the LSE uses more forward contracts. It is assumed that the LSE procures the average of its demand through forward contracts. In other words, the purchased power from the on-peak and round-the-clock forward contracts are assumed to be 700 MW and 3500 MW, respectively, while the prices of forward contracts are remained unchanged.

The expected pro<sup>fi</sup>t and $\mathrm { C V a R } _ { 0 . 9 5 }$ of FW1 and FW2, for two base cases, i.e., normal state (case 1) and when a supply/demand shock occurs (case 5), are shown in Table 10. It is observed that in normal state, the expected pro<sup>fi</sup>t of FW1 is greater than that of FW2. In contrast, when the supply shock occurs, the expected pro<sup>fi</sup>t of FW2 is greater than that of FW1. In addition, in both scenarios, the risks of FW2 are smaller than that of FW1.

Table 11 shows the effects of interruptible load programs for scenarios FW1 and FW2, when the supply shock occurs. It is observed that in both scenarios, the expected pro<sup>fi</sup>t is considerably increased and the risks are signi<sup>fi</sup>cantly decreased. Meanwhile, as the volume of forward contracts increases, the effects of interruptible contracts on improving the expected pro<sup>fi</sup>t or reducing the risks decrease.

## 5. Conclusions

This paper addressed the hedging problem of the LSE using interruptible load programs. A stochastic programming framework was proposed to determine the optimal procurement of interruptible loads, for a speci<sup>fi</sup>ed period of time. The objective was to minimize the risks in terms of a multi-period risk measure. As some risk measures such as variance and VaR fail to be coherent risk measures and are not appropriate for discrete functions, CVaR was used as a risk measurement index. The available amounts of interruptible loads were considered as a function of pecuniary compensation that the LSE offers to the participants. Different types of interruptible contracts were considered and their effects in the optimal procurement policy were analyzed.

The analysis showed that in usual cases, the effects of interruptible contracts on the expected pro<sup>fi</sup>t increasing and/or risks decreasing are insigni<sup>fi</sup>cant, but in situations where a supply or demand shock occurs and consequently the spot market prices are sharply increased, interruptible contracts can help the LSE to prevent decreasing/increasing its expected pro<sup>fi</sup>t/risks. Therefore, this option can act as an ef<sup>fi</sup>cient means for hedging risks in these situations.

![](/api/attachments/VHDGKPB8/fulltext/images/16c2148b7e6583a288439771de6917c869b6f7e51595b9dfb94ef4fb4ee3533b.jpg)

![](/api/attachments/VHDGKPB8/fulltext/images/791b32e1a7f84d7eb2b231967860f1aa4e69c0dba07733494bbff8383b2cb05f.jpg)  
Fig. 8. The sample autocorrelation function.

## Appendix A. Autocorrelation of prices (demands)

The predicted parameters of distribution functions for the demand and the spot market price are estimated using historical data. On the other hand, the spot market price and the LSE's demand exhibit seasonal <sup>fl</sup>uctuations at the daily, weekly, and annual time scale [35]. Therefore, the predicted mean values for price (demand) exhibit seasonal <sup>fl</sup>uctuations at daily, weekly, and annual time scale, i.e., the prices (demands) of different hours exhibit some autocorrelations. Consequently, the prices (demands) of different hours in each scenario tree exhibit some autocorrelations. To verify this point, the ACF (sample autocorrelation function) for the actual price and demand and also for a typical scenario tree are shown in Fig. 8(a) and (b), respectively. As shown in Fig. 8(b), the spot market prices (demands) of a scenario tree exhibit some autocorrelations.

## References

[1] R. Baldick, S. Kolos, S. Tompaidis, Interruptible electricity contracts from an electricity retailer's point of view: valuation and optimal interruption, Operations Research 54 (4) (July–Aug. 2006) 627–642.

[2] J.R. Birge, F. Louveaux, Introduction to Stochastic Programming, Springer-Verlag New York, 1997.

[3] T. Bollerslev, Generalized autoregressive conditional heteroskedasticity, Journal of Econometric 31 (3) (Apr. 1986) 307–327.

[4] J. Cabero, A. Baillo, S. Cerisola, M. Ventosa, A. Garcıa-Alcalde, F. Peran, G. Relano, A medium-term integrated risk management model for a hydrothermal generation company, IEEE Transactions on Power System 20 (3) (Aug. 2005) 1379–1388.

[5] California Public Utilities Commission, Energy Division's Report on Interruptible Programs and Rotating Outages, 2001 (Retrieved June, 2006), [available] online: http://www.cpuc.ca.gov/PUBLISHED/REPORT/5119.htm.

[6] M. Carrión, A.B. Philpott, A.J. Conejo, J.M. Arroyo, A stochastic programming approach to electric energy procurement for large consumers, IEEE Transactions on Power System 22 (2) (May 2007) 744–754.

[7] M. Carrión, A.J. Conejo, J.M. Arroyo, Forward contracting and selling price determination for a retailer, IEEE Transactions on Power System 22 (4) (Nov. 2007) 2105–2114.

[8] D.W. Caves, J.A. Herriges, Optimal dispatch of interruptible and curtailable service options, Operations Research 40 (1) (1992) 104–112.

[9] S.J. Deng, S.S. Oren, Electricity derivatives and risk management, Energy Journal 31 (2006) 940–953.

[10] M. Fahrioglu, F.L. Alvarado, Designing incentive compatible contracts for effective demand management, IEEE Transactions on Power System 15 (4) (Nov. 2000) 1255-1260

[11] Federal Energy Regulatory Commission (FERC), Assessment of Demand Response and Advanced Metering, Document number: AD06-2-000, Aug. 2006, [available] online: http://www.ferc.gov/legal/staff-reports/demand-response.pdf.

[12] S.A. Gabriel, A.J. Conejo, M.A. Plazas, S. Balakrishnan, Optimal price and quantity determination for retail electric power contracts, IEEE Transactions on Power System 21 (1) (Feb. 2006) 180–187.

[13] S.A. Gabriel, M.F. Genc, S. Balakrishnan, A simulation approach to balancing annual risk and reward in retail electrical power markets, IEEE Transactions on Power System 17 (4) (Nov. 2002) 1050–1057

[14] A.M. González, A.M. San Roque, J. García-González, Modeling and forecasting electricity prices with input/output hidden Markov models, IEEE Transactions on Power System 20 (1) (Feb. 2005) 13–24.

[15] I. Horowitza, C.K. Woo, Designing pareto-superior demand-response rate options, Energy Journal 31 (2006) 1040–1051.

[16] Institute for Sustainable Energy, An Assessment and Report of Load Management Opportunities in Southwest Connecticut, Eastern Connecticut State University, June 2003, [available] online: http://www.easternct.edu/depts/sustainenergy.

[17] ISO New England Inc., http://www.iso-ne.com.

[18] R.A. Jabr, Robust self-scheduling under price uncertainty using conditional valueat-risk, IEEE Transactions on Power System 20 (4) (Nov. 2005) 1852–1858.

[19] R. Kamat, S.S. Oren, Exotic options for interruptible electricity supply contracts, Operations Research 50 (2002) 835–850.

[20] H. Li, Y. Li, Z. Li, A multiperiod energy acquisition model for a distribution company with distributed generation and interruptible load, IEEE Transactions on Power System 22 (2) (May 2007) 588–596.

[21] J. J. Lucia and H. Torro, A Short-Term Electricity Futures Prices: Evidence on the Time-Varving Risk Premium Working Paper Department of Financial Economics University of Valencia, Feb. 2008, available [online]: http://www.ivie.es/downloads/ docs/wpasec/wpasec-2008-08.pdf

[22] A. Ng'uni, L. A. Tuan, Interruptible Load and Demand Response: Worldwide Picture and the Situation in Sweden, Power Symposium, NAPS-2006, 2006.

[23] S.S. Oren, S.A. Smith, Design and management of curtailable electricity service to reduce annual peaks, Operations Research 40 (2) (Mar.–Apr. 1992) 213–228.

[24] S.S. Oren, Integrating real and <sup>fi</sup>nancial options in demand-side electricity contracts, Decision Support Systems 30 (3) (2001) 279–288.

[25] Y. Oum, S.S. Oren, S. Deng, Hedging quantity risks with standard power options in a competitive wholesale electricity market, Naval Research Logistics 53 (7) (2006) 697–712.

[26] M.E. Porter, Competitive Strategy: Techniques for Analyzing Industries and Competitors, The Free Press, New York, 1998.

[27] R.T. Rockafellar, S. Uryasev, Optimization of conditional value-at-risk, Journal of Risk 2 (3) (2000) 21–41.

[28] R.T. Rockafellar, S. Uryasev, Conditional value-at-risk for general loss distributions, Journal of Banking & Finance 26 (7) (Jul. 2002) 1443–1471.

[29] R. Schultz, Stochastic programming with integer variables, Math. Program. Ser. B 97 (2003) 285–309.

[30] O. Sezgena, C.A. Goldmana, P. Krishnarao, Option value of electricity demand response, Energy Journal 32 (2) (2007) 108–119.

[31] M. Shahidehpour, H. Yamin, Z. Li, Market Operations in Electric Power Systems, John Wiley and Sons, 2002.

[32] T.P. Strauss, S.S. Oren, Priority pricing of interruptible electric power with an early noti<sup>fi</sup>cation option, Energy Journal 14 (2) (1993) 175–195.

[33] Y.L. Tong, The Multivariate Normal Distribution, Springer-Verlag, New York, 1990.

[34] L.A. Tuan, K. Bhattacharya, Competitive framework for procurement of interruptible load services, IEEE Transactions on Power System 18 (2) (May 2003) 889–897.

[35] R. Weron, Modeling and Forecasting Electricity Loads and Prices: a Statistical Approach, John Wiley & Sons, 2006.

[36] J. Xu, P.B. Luh, F.B. White, E. Ni, K. Kasiviswanathan, Power portfolio optimization in deregulated electricity markets with risk management, IEEE Transactions on Power System 21 (4) (Nov. 2006) 1653–1662.

[37] C.W. Yu, S. Zhang, T.S. Chung, K.P. Wong, Modelling and evaluation of interruptibleload programmes in electricity markets, IEE Proceedings — Generation Transmission and Distribution 152 (5) (Sep. 2005) 581–588.

[38] C.W. Yu, S.H. Zhang, L. Wang, T.S. Chung, Analysis of interruptible electric power in deregulated power systems, Electric Power Systems Research 77 (2007) 637–645.

[39] J. Zarnikau, A review of efforts to restructure Texas' electricity market, Energy Policy 33 (2005) 15–25.

![](/api/attachments/VHDGKPB8/fulltext/images/eada62d0cad4b4209f4b1540fe538611819bfd42e54b55f40de320fc1011956b.jpg)  
Alireza Hatami received his B.Sc. degree in Electrical Engineering from Amirkabir University of technology, Tehran, Iran, in 1995, and M.Sc. and Ph.D. degrees from Tarbiat Modares University, Tehran, Iran, in 1998 and 2009. He is currently an Assistant Professor of Electrical Engineering at the University of Bu-Ali Sina. His research interests include power system economics, electricity market and risk modeling.

![](/api/attachments/VHDGKPB8/fulltext/images/e05c3cc3ce74f5be926886790ee3941842756dc7ace430d57dba8962b10c6450.jpg)  
Hossein Sei<sup>fi</sup> was born in Shiraz/Iran in 1957. He received B.Sc. from Shiraz University in 1980 and M.Sc. and Ph.D both from UMIST/UK in 1987 and 1989, respectively. He then joined Tarbiat Modares University where he is currently a full professor and at the same time as the Head of Iran Power System Engineering Research Center (IPSERC) He is a senior member ofIFFE and Iran Association of Electrical Engineers. His research interests include power system planning and operational issues in both conventional and restructured power systems

![](/api/attachments/VHDGKPB8/fulltext/images/cfea83ff22c0b0a92657034c7cef1beb634e26f2991724967bf0700dcac8d33f.jpg)

Mohammad Kazem Sheikh-El-Eslami received his B.Sc. degree in Electrical Engineering from Tehran University, Tehran, Iran, in 1992 and the M.Sc and Ph.D. degrees from Tarbiat Modares University, Tehran, Iran, 2001 and 2005. He is currently with the Electrical Engineering Department of Tarbiat Modares University His research interests include power market simulation and generation expansion planning.
