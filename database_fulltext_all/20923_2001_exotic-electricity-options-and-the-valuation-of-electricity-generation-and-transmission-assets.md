---
otero_id: 20923
otero_key: "DKDA3A7D"
title: "Exotic electricity options and the valuation of electricity generation and transmission assets"
authors: "Shi-Jie Deng; Blake Johnson; Aram Sogomonian"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00112-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exotic electricity options and the valuation of electricity generation and transmission assets

Shi-Jie Deng <sup>a,)</sup>, Blake Johnson <sup>b</sup>, Aram Sogomonian <sup>c</sup>

<sup>a</sup> IE and OR Department, UniÕersity of California at Berkeley, CA 94720, USA EES and OR Department, Stanford UniÕersity, CA 94305, USA <sup>c</sup> Risk Management, Pacificorp, Portland, OR 97232, USA

## Abstract

We present and apply a methodology for valuing electricity derivatives by constructing replicating portfolios from electricity futures and the risk-free asset. Futures-based replication is made necessary by the non-storable nature of electricity, which rules out the traditional spot market, storage-based method of valuing commodity derivatives. Using the futures-based approach, valuation formulae are derived for both spark and locational spread options for both geometric Brownian motion and mean reverting price processes. These valuation results are in turn used to construct real options-based valuation formulae for generation and transmission assets. Finally, the valuation formula derived for generation assets is used to value a sample of assets that have been recently sold, and the theoretical values calculated are compared to the observed sales prices of the assets. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Electricity derivatives; Spark spread; Mean reversion; Exchange option; Electricity futures contract; Real options; Capacity valuation

## 1. Introduction

With deregulation sweeping through the US electric power industry and a fully competitive marketplace for electricity taking shape, electric utilities and their customers accustomed to a cost-recovery pricing structure for electricity must adapt to market-based pricing. Risk management needs this transition has generated have made electricity derivatives one of the fastest growing derivatives markets, as financial institutions, utilities and other energy market participants work to provide the tools necessary to manage the price and investment risks associated with competitive markets. While many of the risk-management tools and methods now well established in other markets 1,2,5,8 can be readily trans-<sup>w</sup> <sup>x</sup> ferred to the electricity markets, the unique characteristics of electricity and electricity markets also present new challenges to the risk-management discipline. The most important of these are the challenges that the non-storable nature of electricity presents to the traditional methods of modeling price processes and valuing derivatives 11 . Specifically, <sup>w</sup> <sup>x</sup> due to the non-storable nature of electricity, the traditional storage-based, no-arbitrage methods of valuing commodity derivatives are unavailable. In addition, electricity prices can and do demonstrateŽ .

properties such as strong mean reversion over short time horizons that would be inconsistent with an efficient market for a storable good. A second risk management challenge that electricity markets present is the need to value a range of cross-commodity transactions, such as spark and locational spreads 3 .

In this paper, we present tools to address these unique properties of electricity and electricity derivatives. First, we develop a method to value electricity derivatives by replicating them with futures contracts rather than by attempting to store or borrow electricity in the spot market. This allows us to apply traditional no-arbitrage-based methods of derivatives valuation and to proceed without requiring the assumption that electricity is storable. We then present closed-form expressions for the value of a range of cross-commodity derivatives, including spark and locational spread options, both for the case in which the underlying price processes follow geometric Brownian motion, and for the more plausible case in which prices are mean reverting. These results are closely related to those of Shimko’s 9 analysis of<sup>w</sup> <sup>x</sup> futures spread options and Margrabe’s 7 analysis of<sup>w</sup> <sup>x</sup> exchange options. Margrabe’s work is relevant since Ž an exchange option can be thought of a spread option with a zero strike price. Shimko’s results, . however, are for a futures price process derived from a model of the spot price and convenience yield of a storable good, while Margrabe’s are exclusively for geometric Brownian motion processes. After deriving the valuation formulae, we demonstrate how these results can be used to value both generation and transmission assets see 4,10 for a review ofŽ <sup>w</sup> <sup>x</sup> real options and decision analytic approaches to capacity valuation , and present a preliminary compari- . son between the values these models generate and the actual prices at which these types of assets have recently been sold.

The remainder of the paper is organized as follows. In Section 2, we introduce the set of crosscommodity derivatives we will consider in the paper, and identify some of their basic characteristics. In Section 3, we describe how these derivatives can be replicated and thus valued by arbitrage using fu-Ž . tures contracts, and present the principal valuation results of the paper. In Section 4, we use these results to develop a real-options-based methodology for valuing generation and transmission assets, and present the results of our preliminary empirical evaluation of the effectiveness of the methodology.

## 2. Cross-commodity electricity derivatives

There are two principal categories of cross-commodity electricity derivatives; spark spread, or heatrate-linked derivatives, and locational spread derivatives. We consider each below.

## 2.1. Spark spread, or heat rate-linked deriÕatiÕes

The primary cross-commodity transaction in electricity markets is the spark spread 6 , which is based<sup>w</sup> <sup>x</sup> on the difference between the price of electricity and the price of a particular fuel used to generate it. The spread between the price of electricity and a fuel that can be used to generate it is of interest since it is this spread that determines the economic value of generation assets that can be used to transform the fuel into electricity This idea is analogous to the concept ofŽ the Acrack spreadB used in the oil<sup>r</sup>refining industry. In that case the relevant spread between crude oil and refined products like diesel or gasoline seeŽ Shimko 9 . The amount of fuel that a particular<sup>w</sup> <sup>x</sup>. . generation asset requires to generate a given amount of electricity will of course depend on the asset’s efficiency. This efficiency is summarized by the asset’s heat rate, which is defined as the number of British thermal units Btu of the input fuel mea-Ž . Ž sured in millions required to generate 1 megawatt. hour MWh of electricity. Thus, the lower the heatŽ . rate, the more efficient the facility. The spark spread associated with a particular heat rate is defined as the current price of electricity less the product of the heat rate and the current fuel price. Thus, the lower the heat rate, the lower the fuel price, and the higher the electricity price, the larger the spark spread.

In a deregulated market, presumably only assets that have a positive spark spreads under prevailing market conditions will be operated. This leads naturally to the definition of the prevailing market implied heat rate H as:

H<sup>s</sup>number of MM Btu needed for a marginal genera-

$$
= \frac {S _ {\mathrm{E}}}{S _ {\mathrm{G}}} \mathrm{MMBtu/MWh}
$$

ting plant to generate 1 MW h of electricity

1Ž .

where $S _ { \mathrm { E } }$ is the spot price of electricity per MWh and $S _ { \mathrm { G } }$ is the spot price of the generating fuel per MM Btu. With the notion of a heat rate established, we define European spark spread put and call options.

Definition 1. A European spark spread call option written on fuel G at a fixed orŽ . AstrikeB heat rate $K _ { \mathrm { H } }$ gives the option holder the right but not the obligation to pay $K _ { \mathrm { H } }$ times the unit price of fuel G at the option’s maturity T and receive the price of 1 unit of electricity. Let $S _ { \mathrm { E } } ^ { T }$ and $S _ { \mathrm { G } } ^ { T }$ be the unit spot prices of electricity and fuel at time T, respectively. Denote the value of the option at time t by $\mathrm { C } _ { 1 } ( S _ { \mathrm { E } } ^ { t }$ $S _ { \mathrm { G } } ^ { t } , t )$ . Then the payoff of the option at maturity time T is:

$$
C _ {1} \left(S _ {\mathrm{E}} ^ {T}, S _ {\mathrm{G}} ^ {T}, K _ {\mathrm{H}}, T\right) = \max \left(S _ {\mathrm{E}} ^ {T} - K _ {\mathrm{H}} S _ {\mathrm{G}} ^ {T}, 0\right)\tag{2}
$$

Definition 2. A European spark spread put option written on fuel G at a fixed heat rate $K _ { \mathrm { H } }$ gives the option holder the right but not the obligation to pay the price of 1 unit of electricity and receive $K _ { \mathrm { H } }$ times the unit price of fuel G at maturity time $T .$ Denote the value of the option at time t by $P _ { 1 } ( S _ { \mathrm { E } } ^ { t }$ $S _ { \mathrm { G } } ^ { t }$ , t.. Then the payoff of the option at time T is:

$$
P _ {1} \left(S _ {\mathrm{E}} ^ {T}, S _ {\mathrm{G}} ^ {T}, K _ {\mathrm{H}}, T\right) = \max \left(K _ {\mathrm{H}} S _ {\mathrm{G}} ^ {T} - S _ {\mathrm{E}} ^ {T}, 0\right)\tag{3}
$$

The following example provides a simple illustration of how spark spread options can be used to manage electricity price risk.

v A power marketer in a region where the marginal generating fuel is natural gas would like to buy power at time T at a market implied heat rate not to exceed $K _ { \mathrm { H } }$ . An agreement providing such a heat rate cap would ensure the marketer power at time T at a price given by $S _ { \mathrm { G } } \times \mathrm { m i n } ( H , \ K _ { \mathrm { H } } )$ . Assuming the marketer sells the power into the spot market at time T, his payoff will be $( S _ { \mathrm { E } } ^ { T } - S _ { \mathrm { G } } ^ { T } \overset { \cdot } { \times } \operatorname* { m i n } ( H ^ { T } , \ K _ { \mathrm { H } } ) )$ which is equal to $S _ { \mathrm { G } } ^ { T } \times \mathrm { m a x } \bar { ( } H ^ { T } - K _ { \mathrm { H } } , 0 )$ . Bringing $S _ { \mathrm { G } } ^ { T }$ inside the brackets, the payoff is max $\big ( S _ { \mathrm { E } } ^ { T } - K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { T }$ 0 , which is exactly the same as that of a European . spark spread call option with strike heat rate $K _ { \mathrm { H } }$ The power marketer can therefore achieve his goal by purchasing this spark spread call.

Throughout the remainder of the article, we make the following assumptions.

Assumption 1. A complete set of futures contracts for electricity and for the relevant generating fuels are traded.

Assumption 2. The risk-free interest rate r is constant.

Following Shimko 9 , we next provide a put-call<sup>w</sup> <sup>x</sup> parity relationship between the spark spread put and call options, as well as upper and lower bounds on their values. We delay making specific assumptions about the price processes that electricity and the generating fuels follow until Section 3.

( ) Proposition 1. Put-Call Parity Let $F _ { E } ^ { t }$ and $F _ { G } ^ { t }$ denote the futures prices of electricity and the generating fuel, respectiÕely. The following parity relationship holds for European spark spread put and call options with the same fixed heat rate $K _ { H }$ and expiration date t.

$$
C _ {1} = P _ {1} + \mathrm{e} ^ {- r t} \left(F _ {\mathrm{E}} ^ {t} - K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t}\right)\tag{4}
$$

Proof. At time t, the payoff of a long position in 1 unit of spark spread call option $C _ { 1 }$ is max $( S _ { \mathrm { E } } ^ { t } -$ $K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } , 0 ) ;$ ; the payoff of 1 unit of spark spread put option $P _ { 1 }$ is max $( K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } - S _ { \mathrm { E } } ^ { t } , \ 0 )$ . Consequently, the payoff of $( C _ { 1 } - P _ { 1 } )$ at maturity time t is $( S _ { \mathrm { E } } ^ { t } -$ $K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } )$ . The present value of $( S _ { \mathrm { E } } ^ { t } - K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } )$ is $\mathrm { e } ^ { - r t }$ $( F _ { \mathrm { E } } ^ { t } - K _ { \mathrm { H } } F _ { \mathrm { G } } ^ { t } )$ . Therefore,

$$
C _ {1} - P _ {1} = \mathrm{e} ^ {- r t} \left(F _ {\mathrm{E}} ^ {t} - K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t}\right)\tag{5}
$$

Proposition 2. ( ) No-arbitrage lower<sup>r</sup>upper bounds Let $F _ { E } ^ { t }$ and $F _ { G } ^ { t }$ denote the futures prices of electricity and the generating fuel, respectiÕely. Then the Õalue of a spark spread call option $C _ { I }$ can be bounded aboÕe and below as follows:

$$
\mathrm{e} ^ {- r t} \max \left(F _ {\mathrm{E}} ^ {t} - K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t}, 0\right) \leq C _ {1} \leq \mathrm{e} ^ {- r t} F _ {\mathrm{E}} ^ {t}\tag{6}
$$

Proof. The first inequality is by put-call parity 4Ž . and the fact $P _ { 1 } \geq 0$ . The second inequality is due to the fact max $\mathrm { ' } \bar { S _ { \mathrm { E } } ^ { t } } - K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } , 0 ) \leq S _ { \mathrm { E } } ^ { t }$ at time t and the present values of max $( S _ { \mathrm { E } } ^ { t } - K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } , 0 )$ and $S _ { \mathrm { E } } ^ { t }$ are $C _ { 1 }$ and $\mathrm { e } ^ { - r t } F _ { \mathrm { E } } ^ { t }$ , respectively. B

## 2.2. Locational spread options

Due to transmission costs and constraints noteŽ that the impact of transmission constraints is compounded by the non-storability of electricity, which forces real time delivery. , substantial differences. frequently exist between the price of electricity at different locations. We refer to these differences as locational spreads, and define call options on them as follows.

Definition 3. Ž . Locational spread : a European call option on the locational spread between location one and location two with maturity T gives its holder the right but not the obligation to pay the price of 1 unit of electricity at location one at time T and receive the price of $K _ { \mathrm { L } }$ units of electricity at location two Žtransmission cost from location 1 to 2 can be incorporated by setting $K _ { \mathrm { L } }$ . being less than 1 . Let $S _ { i } ^ { T }$ be the unit price of electricity at location $i ( i = 1 , 2 )$ at time T. Denote the value of the option at time t by $C _ { 2 } ( S _ { 1 } ^ { t } , ~ S _ { 2 } ^ { t } , ~ K _ { \mathrm { L } } , ~ t )$ . Then the payoff of the option at time T is:

$$
C _ {2} \left(S _ {1} ^ {T}, S _ {2} ^ {T}, K _ {\mathrm{L}}, T\right) = \max \left(S _ {1} ^ {T} - K _ {\mathrm{L}} S _ {2} ^ {T}, 0\right)\tag{7}
$$

A European locational spread put option can be defined in a similar way.

## 3. Valuation of electricity derivatives

In this section, we present a futures-based method of replicating electricity derivatives, and illustrate the method by using it to derive explicit expressions for the value of the spark spread and locational spread options defined above. Valuation equations are provided for these instruments for both geometric Brownian motion price processes and mean-reverting price processes. In both cases we explicitly derive only the value of the call options. The value of put options can then be derived using the put-call parity relationship presented in Section 2.

## 3.1. Futures-based replication of electricity deriÕatiÕes

As noted above, because electricity is non-storable, the traditional storage-based methods of constructing replicating portfolios for commodity derivatives cannot be used to value electricity derivatives. In place of the storage-based methods, we present a method for replicating electricity derivatives by dynamically trading futures contracts of the appropriate maturity. Since, at maturity, the price of a futures contract must converge to the then current spot price, the methodology permits exact replication. Since the precise nature of the replicating strategy will naturally depend on the specific derivative being replicated, to illustrate the method we use it to derive the replicating strategy for spark and locational spread options. We do so first under the assumption that the relevant futures price processes follow geometric Brownian motion processes, and then under the more reasonable assumption that they follow mean reverting processes.

## 3.2. Geometric Brownian motion price process

We first consider the case in which the futures price processes of electricity and the appropriate generating fuel of the relevant maturity, $F _ { \mathrm { E } }$ and $F _ { \mathrm { G } }$ follow geometric Brownian motion processes

$$
\begin{array}{l} \mathrm {d F _ {E} / F _ {E}} = \mu_ {\mathrm{E}} \mathrm{d} t + \sigma_ {\mathrm{E}} \mathrm{d} B ^ {1} \\ \mathrm {d F _ {G} / F _ {G}} = \mu_ {\mathrm{G}} \mathrm{d} t + \sigma_ {\mathrm{G}} \mathrm{d} B ^ {2} \end{array}\tag{8}
$$

where $B ^ { 1 }$ and $B ^ { 2 }$ are two Wiener processes with instantaneous correlation $\rho . ~ \mu _ { \mathrm { E } } , ~ \mu _ { \mathrm { G } } , ~ \sigma _ { \mathrm { E } } ,$ , and $\sigma _ { \mathrm { G } }$ are assumed to be constants for the moment. The valuation results are therefore the same as those in Ref. 7 except that the underlying are futures con- <sup>w</sup> <sup>x</sup> tracts. The more general case where the volatility and correlation parameters can be functions of time is considered in the mean-reversion model.

## 3.2.1. Valuation of spark spread options

Denote the time-t value of a spark spread call option which matures at time T by $V \left( x , \ y , \ t \right) \equiv$ $\bar { C _ { 1 } } ( F _ { \mathrm { E } } ^ { t , T } , ~ F _ { \mathrm { G } } ^ { t , T } , ~ K _ { \mathrm { H } } , ~ T - t )$ and let $F _ { * } ^ { t , T }$ represent the price at time t of the commodity futures contract with maturity date T. By constructing an instantaneously risk-free portfolio using the electricity and generating fuel futures contracts and the riskless asset, it follows that $C _ { 1 }$ , normalized by the value of the risk-free asset, must satisfy the partial differential equation PDE :Ž .

$$
\begin{array}{r l} - V _ {t} + \frac {1}{2} \left[ x ^ {2} V _ {x x} \sigma_ {x} ^ {2} + 2 \rho \sigma_ {x} \sigma_ {y} x y V _ {x y} + y ^ {2} V _ {y y} \sigma_ {y} ^ {2} \right] \\ = 0 \end{array}\tag{9}
$$

with boundary conditions $V ( x , \ y , \ T ) = \operatorname* { m a x } ( x - y$ $0 ) , V ( x , 0 , t ) = x .$ , and $V ( 0 , \ y , \ t ) = 0$

Proposition 3. ( ) Value of a spark spread call option The closed-form solution for $C _ { I }$ is:

$$
\begin{array}{c} C _ {1} \big (F _ {\mathrm{E}} ^ {t, T}, F _ {\mathrm{G}} ^ {t, T}, K _ {\mathrm{H}}, T - t \big) \\ = \mathrm{e} ^ {- r (T - t)} \Big [ F _ {\mathrm{E}} ^ {t, T} N \big (d _ {1} \big) - K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t, T} N \big (d _ {2} \big) \Big ] \end{array}\tag{10}
$$

where

$$
\begin{array}{l} d _ {1} = \frac {\ln \left(F _ {\mathrm{E}} ^ {t , T} / \left(K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t , T}\right)\right) + v ^ {2} (T - t) / 2 v}{\sqrt {T - t}} \\ d _ {2} = d _ {1} - v \sqrt {T - t} \\ v ^ {2} = \sigma_ {\mathrm{E}} ^ {2} - 2 \rho \sigma_ {\mathrm{E}} \sigma_ {\mathrm{G}} + \sigma_ {\mathrm{G}} ^ {2} \end{array}
$$

Proof. Verify $V = C _ { 1 } ( F _ { \mathrm { E } } ^ { t , T } , ~ F _ { \mathrm { G } } ^ { t , T } , ~ K _ { \mathrm { H } } , ~ T - t ) { \bf e } ^ { r ( T - t ) }$ solves PDE 9 with the corresponding boundaryŽ . conditions. B

## 3.2.2. Valuation of locational spread options

The value of the locational spread call option can be derived in exactly the same way the value of the spark spread call option was derived above. Specifically, defining $\mathrm { F } _ { \mathrm { E } , 1 }$ and $\mathrm { F } _ { \mathrm { E } , 2 }$ to be the geometric Brownian motion price processes that the futures prices of electricity at locations 1 and 2 follow, we have:

Proposition 4. (Value of a locational spread call option The ) Õalue of $C _ { 2 }$ is giÕen by

$$
\begin{array}{l} C _ {2} \big (F _ {\mathrm{E}, 1} ^ {t, T}, F _ {\mathrm{E}, 2} ^ {t, T}, K _ {\mathrm{L}}, T - t \big) \\ = \mathrm{e} ^ {- r (T - t)} \Big [ F _ {\mathrm{E}, 1} ^ {t, T} N (d _ {1}) - K _ {\mathrm{L}} F _ {\mathrm{E}, 2} ^ {t, T} N (d _ {2}) \Big ] \end{array}
$$

where

$$
\begin{array}{l} d _ {1} = \frac {\ln \big (F _ {\mathrm{E} , 1} ^ {t , T} / K _ {\mathrm{L}} F _ {\mathrm{E} , 2} ^ {t , T} \big) + v ^ {2} (T - t) / 2}{v \sqrt {T - t}} \\ d _ {2} = d _ {1} - v \sqrt {T - t} \\ v ^ {2} = \sigma_ {\mathrm{E}, 1} ^ {2} - 2   \rho \sigma_ {\mathrm{E}, 1} \sigma_ {\mathrm{E}, 2} + \sigma_ {\mathrm{E}, 2} ^ {2} \end{array}\tag{11}
$$

## 3.3. Mean-reÕerting price process

In this section, we assume that the futures price processes of electricity $F _ { \mathrm { E } }$ and of the relevant generating fuel $F _ { \mathrm { G } }$ follow the mean-reverting processes

$$
\begin{array}{l} \mathrm{d} F _ {\mathrm{E}} = \kappa_ {\mathrm{E}} \big (\mu_ {\mathrm{E}} (t) - \ln F _ {\mathrm{E}} \big) F _ {\mathrm{E}} \mathrm{d} t + \sigma_ {\mathrm{E}} (t) F _ {\mathrm{E}} \mathrm{d} B ^ {1} \\ \mathrm{d} F _ {\mathrm{G}} = \kappa_ {\mathrm{G}} \big (\mu_ {\mathrm{G}} (t) - \ln F _ {\mathrm{G}} \big) F _ {\mathrm{G}} \mathrm{d} t + \sigma_ {\mathrm{G}} (t) F _ {\mathrm{G}} \mathrm{d} B ^ {2} \end{array}\tag{12}
$$

where $\sigma _ { \mathrm { E } } ( t )$ and $\sigma _ { \mathrm { G } } ( t )$ are functions of time $t ,$ $\mu _ { \mathrm { E } } ( t )$ and $\mu _ { \mathrm { G } } ( t )$ are the long-term means, $\kappa _ { \mathrm { E } }$ and $\kappa _ { \mathrm { G } }$ are the mean-reverting coefficients, and $B ^ { 1 }$ and $B ^ { 2 }$ are, as above, two Wiener processes with instantaneous correlation $\rho .$ The mean-reverting assumption on the futures price processes put restrictions on the choice of volatility functions $\sigma _ { \mathrm { E } } ( t )$ and $\sigma _ { \mathrm { G } } ( t )$ Among many other forms, the following is a feasible one.

$$
\sigma_ {\mathrm{E}} (t) = \sigma_ {\mathrm{E}} \mathrm{e} ^ {- \kappa_ {\mathrm{E}} ^ {*} t}, \quad \sigma_ {\mathrm{G}} (t) = \sigma_ {\mathrm{G}} \mathrm{e} ^ {- \kappa_ {\mathrm{G}} ^ {*} t}\tag{13}
$$

## 3.3.1. Valuation of spark spread options

Denote the time t value of a spark spread call option which matures at time T by $V \left( x , \ y , \ t \right) \equiv$ $C _ { 1 } ( F _ { \mathrm { E } } ^ { t , T } , ~ F _ { \mathrm { G } } ^ { t , T } , ~ K _ { \mathrm { H } } , ~ T - t )$ . Applying the same replication arguments applied above, it follows that $C _ { 1 } \mathrm { e }$ $r ( T - t )$ must satisfy the PDE:

$$
\begin{array}{l} - V _ {t} + \frac {1}{2} \left[ x ^ {2} V _ {x x} \sigma_ {x} ^ {2} (t) + 2 \rho \sigma_ {x} (t) \sigma_ {y} (t) x y V _ {x y} \right. \\ \left. + y ^ {2} V _ {y y} \sigma_ {y} ^ {2} (t) \right] = 0 \end{array}\tag{14}
$$

with boundary conditions $V ( x , \ y , \ T ) = \operatorname* { m a x } ( x - y$ 0 ,. $V ( x , 0 , t ) = x$ , and $V ( 0 , \ y , \ t ) = 0$

Proposition 5. ( ) Value of a spark spread call option The closed-form solution for $C _ { I }$ is:

$$
\begin{array}{c} C _ {1} \big (F _ {\mathrm{E}} ^ {t, T}, F _ {\mathrm{G}} ^ {t, T}, K _ {\mathrm{H}}, T - t \big) \\ = \mathrm{e} ^ {- r (T - t)} \Big [ F _ {\mathrm{E}} ^ {t, T} N \big (d _ {1} \big) - K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t, T} N \big (d _ {2} \big) \Big ] \end{array}\tag{15}
$$

where

$$
\begin{array}{l} d _ {1} = \frac {\ln \left(F _ {\mathrm{E}} ^ {t , T} / \left(K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t , T}\right)\right) + v ^ {2} (T - t) / 2}{v \sqrt {T - t}} \\ d _ {2} = d _ {1} - v \sqrt {T - t} \\ v ^ {2} = \frac {\int_ {t} ^ {T} \left[ \sigma_ {\mathrm{E}} ^ {2} (s) - 2 \rho \sigma_ {\mathrm{E}} (s) \sigma_ {\mathrm{G}} (s) + \sigma_ {\mathrm{G}} ^ {2} (s) \right] \mathrm{d} s}{T - t} \end{array}
$$

![](/api/attachments/DKDA3A7D/fulltext/images/b7f62dfeca488977dbddb3264e22d2bc8cb2a3a1e52baf95b59e96554bb3acc3.jpg)  
Fig. 1. Value of spark spread call under mean-reversion and GBM.

Proof. Verify $V = C _ { 1 } ( F _ { \mathrm { E } } ^ { t , T } , ~ F _ { \mathrm { G } } ^ { t , T } , ~ K _ { \mathrm { H } } , ~ T - t ) { \mathrm e } ^ { r ( T - t ) }$ solves PDE 14 with the corresponding boundaryŽ . conditions. B

Fig. 1 illustrates the value of spark spread options under both the geometric Brownian motion GBMŽ . price process assumption and the mean-reverting price process assumption. When the underlying price process is actually mean-reverting, the geometric Brownian motion assumption leads to the overvaluation of spark spread options, especially those with long maturities.

Several comparative static properties of the spark spread call option value can be derived by investigating the sign of the partial derivatives of $C _ { 1 }$ with respect to their parameters.

## Proposition 6.

$$
\begin{array}{c} \text { As } F _ {\mathrm{E}} ^ {t, T} \nearrow (\text { increases }), \text { or } F _ {\mathrm{G}} ^ {t, T} \searrow (\text { decreases}) \Rightarrow C _ {1} \nearrow (\text { increases }) \\ F _ {\mathrm{G}} ^ {t, T} \nearrow \text { and } \frac {F _ {\mathrm{E}} ^ {t , T}}{F _ {\mathrm{G}} ^ {t , T}} \nearrow \Rightarrow C _ {1} \nearrow \\ \rho \searrow \text { or } r \searrow \Rightarrow C _ {1} \nearrow \end{array}\tag{16}
$$

## 3.3.2. Valuation of locational spread options

Defining $F _ { \mathrm { E } , 1 }$ and $F _ { \mathrm { E } , 2 }$ to be the mean-reverting price processes that govern the futures prices of electricity at locations 1 and 2 and following the derivation above, we have:

Proposition 7. ( ) Value of a locational spread option The Õalue of $C _ { 2 }$ is giÕen by

$$
\begin{array}{c} C _ {2} \big (F _ {\mathrm{E}, 1} ^ {t, T}, F _ {\mathrm{E}, 2} ^ {t, T}, K _ {\mathrm{L}}, T - t \big) \\ = \mathrm{e} ^ {- r (T - t)} \Big [ F _ {\mathrm{E}, 1} ^ {t, T} N \big (d _ {1} \big) - K _ {\mathrm{L}} F _ {\mathrm{E}, 2} ^ {t, T} N \big (d _ {2} \big) \Big ] \end{array}\tag{17}
$$

where

$$
\begin{array}{l} d _ {1} = \frac {\ln \left(F _ {\mathrm{E} , 1} ^ {t , T} / F _ {\mathrm{E} , 2} ^ {t , T}\right) + v ^ {2} (T - t) / 2}{v \sqrt {T - t}} \\ d _ {2} = d _ {1} - v \sqrt {T - t} \\ v ^ {2} = \frac {\int_ {t} ^ {T} \left[ \sigma_ {\mathrm{E} , 1} ^ {2} (s) - 2 \rho \sigma_ {\mathrm{E} , 1} (s) \sigma_ {\mathrm{E} , 2} (s) + \sigma_ {\mathrm{E} , 2} ^ {2} (s) \right] \mathrm{d} s}{T - t} \end{array}
$$

## 4. Real options valuation of generation and transmission assets

The right to operate a generation asset with heat rate H that uses generating fuel G is clearly given by the value of a spark spread option with AstrikeB heat rate H written on generating fuel G. Similarly, the value of a transmission asset that connects location 1 to location 2 is equal to the sum of the value of the locational spread option to buy electricity at location 1 and sell it at location 2 and the value of the option to buy electricity at location 2 and sell it a location 1 in both cases, less the appropriate trans-Ž mission cost . This equivalence between the value of. appropriately defined spark and locational spread options and the right to operate a generation or a transmission asset can be easily used to value such assets. In this section we illustrate this approach by developing a simple spark spread-based model of the value of a gas-fired generation asset. Once established, we fit the model and use it to generate estimates of the value of several gas-fired plants that have recently been sold. The accuracy of the model is then evaluated by comparing the estimates constructed to the prices at which the assets were actually sold.

In the analysis we make the following simplifying assumptions about the operating characteristics of the generation assets under consideration.

Assumption 3. Ramp-ups and ramp-downs of the facility can be done with very little advance notice.

Assumption 4. The facility’s operation e.g., start-Ž up<sup>r</sup>shutdown costs and maintenance costs are con-. stant.

These assumptions are reasonable, since for a typical gas turbine combined cycle cogeneration plant the response time ramp upŽ . <sup>r</sup>down is several hours and the variable costs e.g., operation and mainte- Ž nance are generally stable over time..

To construct a spark spread-based estimate of the value of a generation asset, we estimate the value of the right to operate the asset over its remaining useful life. This value can be found by integrating the value of the spark spread options over the remaining life of the asset. Specifically,

Definition 4. Let 1 unit of the time t capacity right of a natural gas-fired electric power plant represent the right to convert $K _ { \mathrm { H } }$ units of natural gas into 1 unit of electricity by using the plant at time t, where $K _ { \mathrm { H } }$ is the plant’s heat rate.

The payoff of 1 unit of time-t capacity right is max $\left( S _ { \mathrm { E } } ^ { t } - K _ { \mathrm { H } } S _ { \mathrm { G } } ^ { t } , 0 \right)$ , where $S _ { \mathrm { E } } ^ { t }$ and $S _ { \mathrm { G } } ^ { t }$ are the spot prices of electricity and natural gas at time t, respectively. Denote the value of 1 unit of the time t capacity right by u tŽ ..

Definition 5. Denote the virtual value of 1 unit of capacity of a gas-fired power plant by V. Then, V is equal to 1 unit of the plant’s time-t capacity right over the remaining life 0, <sup>w</sup> <sup>x</sup> T of the power plant, i.e. $\begin{array} { r } { V = \int _ { 0 } ^ { T } u ( t ) \mathrm { d } t } \end{array}$

Without making any distributional assumptions about the price processes that $S _ { \mathrm { E } } ^ { t }$ and $S _ { \mathrm { G } } ^ { t }$ follow, we have the following proposition.

Proposition 8. The Õalue of 1 unit of capacity V of a plant that has a useful life of T has both a lower bound and an upper bound:

$$
\int_ {0} ^ {T} \mathrm{e} ^ {- r t} \max \left(F _ {\mathrm{E}} ^ {T} - K _ {\mathrm{H}} F _ {\mathrm{G}} ^ {t}, 0\right) \mathrm{d} t \leq V \leq \int_ {0} ^ {T} \mathrm{e} ^ {- r t} F _ {\mathrm{E}} ^ {t} \mathrm{d} t\tag{18}
$$

Proof. By definition and Proposition 2.

If we further assume that the price processes of electricity and natural gas spot and futures prices follow the mean-reverting processes as given by Ž .12 , then we have $\begin{array} { r } { \mathbf { \boldsymbol { u } } ( t ) = \mathbf { \boldsymbol { \ C } } _ { 1 } ( t ) } \end{array}$ where $C _ { 1 } ( t )$ is given by Proposition 5. The value of a gas-fired power plant with lifetime T is therefore

$$
V _ {\text { gen }} = \int_ {0} ^ {T} C _ {1} (t) \mathrm{d} t\tag{19}
$$

Similarly, if we assume that the price processes of the electricity futures prices at two different locations follow mean-reverting processes, the value of a transmission line connecting the two locations a and b in a network is

$$
V _ {\text { tran }} = \int_ {0} ^ {T} \left[ C _ {2, 1} (t) + C _ {2, 2} (t) \right] \mathrm{d} t\tag{20}
$$

where $C _ { 2 , 1 } ( t )$ and $C _ { 2 , 2 } ( t )$ represent the locational spread option value at time t from a to b and from b to a, respectively. Eqs. 19 and 20 are the twoŽ . Ž .

Electricity and Natural Gas Forward Curves  
![](/api/attachments/DKDA3A7D/fulltext/images/a9372f142e0decddb7cf5ac020ae8dcbf3f34e75820dded21a9d5050d24c0de1.jpg)  
Fig. 2. Electricity and natural gas futures price curve.

fundamental valuation formulae we propose for the valuation of generation and transmission assets in a competitive electricity market.

## 4.1. Application of the model to recent generation asset sales

To evaluate the accuracy of 19 , we fit the modelŽ . and use it to construct estimates of the value of several generation assets that have been recently sold. For purposes of comparison, we also estimate the value of each asset using a standard discounted cash flow DCF calculation.Ž .

In order to fit the model, we first estimate the volatilities of the price processes of the relevant futures contracts. Let $f _ { n } ^ { t }$ be the price of the futures contract that matures in n months, and assume that $f _ { n } ^ { t }$ follows a mean-reverting process of the kind considered above. Let $R _ { n } ^ { t } \equiv \ \ln f _ { n } ^ { t }$ , then

$$
\mathrm{d} R _ {n} = \kappa_ {1} \left(\hat {\mu} _ {n} - R _ {n}\right) \mathrm{d} t + \sigma_ {n} \mathrm{d} B\tag{21}
$$

We estimate $\sigma _ { n }$ using the New York Mercantile Exchange NYMEX electricity futures historical Ž . price data. The natural gas volatility term structure and the gas-to-electricity price correlation are also estimated using historical data on the NYMEX natural gas Henry Hub futures contracts. Once esti-Ž . mated, these parameters along with implied volatility from the market traded call options are used to calibrate the parameters in the volatility functions Ž . Ž . 13 . We will use 13 in the valuation formulae derived in Section 3 to construct real-options-based estimates of the value of the assets in question. To calculate the discounted cash flow value of the assets we use the relevant electricity and natural gas futures curves.

The sample of generation assets considered consists of four gas-fired power plants which Southern California Edison recently sold to Houston Industries. At present, not all of the individual plant dollar investments have been made public. As a proxy, we use the total investment made by Houston Industries ŽUS\$237 million to purchase four plants — Coolwater, Ellwood, Etiwanda and Mandalay , divided by . the total number of megawatts MW of capacityŽ . Ž . 2172 MW to get approximately US\$110,000<sup>r</sup>MW Ž . or US\$110<sup>r</sup>kW of capacity for the entire package <sup>1</sup> of plants. However, the Coolwater Plant Daggett, Ž CA is the most efficient with an average heat rate . Ž of 9500 of the four plants in the package and thus .

![](/api/attachments/DKDA3A7D/fulltext/images/4a549c3f9c5f5ece8aa37a9dbcd4bce964414138251be494608a2ae541eeb9a5.jpg)  
Fig. 3. Capacity value of a gas-fired plant.

should have a higher value per MW. We therefore assume that the implied market value for Coolwater could range from US\$110,000 to US\$220,000 per MW, or equivalently, US\$110<sup>r</sup>kW to US\$220<sup>r</sup>kW.

Using the NYMEX electricity and natural gas futures price data on October 15, 1997, see Fig. 2 ,Ž . we compute both the option value and DCF value Ž . using a risk-adjusted discount rate of 10% of a gas-fired plant with various possible heat rates assuming a remaining operating life of 15 years for the plant. It is also assumed the plant is operated during peak hours only. Fig. 3 shows the plot of the option values and the DCF values of a plant of various possible heat rates using forward curves at different times and at different trading hubs.

We can see that the option values of capacity are significantly higher than the DCF values. For heat rate higher than 9500 Btu<sup>r</sup>kW h, the DCF values of capacity are close to zero. For example, at the heat rate level of 9500 and using the electricity forward curve at Palo Verde PV , the theoretical option-based Ž . capacity value of a plant comparable to the Coolwater Plant 5 is around US\$185<sup>r</sup>kW, while the DCF valuation is only US\$28<sup>r</sup>kW.

Remark. The natural electricity trading hub for Coolwater to sell into is the Mead hub. However, due to the liquidity of the Palo Verde financial futures contracts we use the PV futures contracts as a proxy for the electricity price information for Coolwater. In addition, the basis differential associated with PV<sup>r</sup>Mead is typically not large.

## 5. Conclusions

This article has presented a methodology for valuing electricity derivatives by constructing replicating portfolios with futures contracts and the risk-free asset. Futures-based replication is made necessary by the non-storable nature of electricity, which rules out the traditional spot market, storage-based method of valuing commodity derivatives. Once developed, the methodology was used to derive valuation formulae for both spark and locational spread options when the prices of the underlying assets follow either geometric Brownian motion or mean reverting processes. These valuation results were in turn used to construct real-options-based valuation formulae for generation and transmission assets. Application of the generation asset valuation formula to a sample of recent asset sales suggests that the spark spread analysis generates reasonable estimates of the actual market value of the assets, and certainly more accurate estimates than those which traditional DCF methods provide. The estimates generated could be improved by incorporating a greater level of detail about the plants, particularly their hourly and daily operating optionality. Analysis of this kind presents a natural avenue for future research.

## References

<sup>w</sup> <sup>x</sup> 1 F. Black, The pricing of commodity contracts, Journal of Financial Economics 3 1976 167–179, Sept. Ž .

<sup>w</sup> <sup>x</sup> 2 F. Black, M. Scholes, The pricing of options and corporate liabilities, Journal of Political Economy 81 1973 637–659,Ž . May–June.

<sup>w</sup> <sup>x</sup> 3 S. Deng, Financial methods in competitive electricity markets, PhD Dissertation forthcoming , University of Califor-Ž . nia at Berkeley, CA, 1998.

<sup>w</sup> <sup>x</sup> 4 A.K. Dixit, R.S. Pindyck, Investment Under Uncertainty, Princeton Univ. Press, NJ, 1994.

<sup>w</sup> <sup>x</sup> 5 D. Duffie, Dynamic Asset Pricing Theory, 2nd edn., Princeton Univ. Press, NJ, 1996.

<sup>w</sup> <sup>x</sup> 6 M. Hsu, Spark spread options are hot! The Electricity Journal 11 2 1998 1–12, Elsevier Sciences, March.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 W. Margrabe, The value of an option to exchange one asset for another, Journal of Finance 33 1 1978 177–186.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 R.C. Merton, Theory of Rational Option Pricing, Bell Journal of Economics and Management Science 4 1973 141–183,Ž . Spring.

<sup>w</sup> <sup>x</sup> 9 D. Shimko, Options on futures spreads: hedging, speculation and valuation, Journal of Futures Markets 14 2 1994Ž . Ž . 183–213.

<sup>w</sup> <sup>x</sup> 10 J.E. Smith, R.F. Nau, Valuing risky projects: option pricing theory and decision analysis, Management Science 41 no.5 Ž . Ž . 1995 795–816.

<sup>w</sup> <sup>x</sup> 11 E.S. Schwartz, The stochastic behavior of commodity prices: implications for valuation and hedging, Journal of Finance 52 Ž . Ž . 3 1997 923–973.

![](/api/attachments/DKDA3A7D/fulltext/images/02bcc62dbbc043add89d29e6bd4faf96320946b727c9366851306fee4e860183.jpg)  
Dr. Shi-Jie Deng is an Assistant Professor of Industrial and Systems Engineering at Georgia Institute of Technology. His research interests include financial asset pricing and real options valuation, financial engineering applications in energy commodity markets, transmission pricing in electric power systems, stochastic modeling and simulation. Dr. Deng has served as a consultant to several private and public organizations on issues of risk management and asset val-

uation in the deregulated electricity industry.

Dr. Deng holds a BS degree in Applied Mathematics from Beijing University in China, an MS degree in Mathematics from the University of Minnesota at Twin Cities, as well as MS and PhD degrees in Industrial Engineering and Operations Research from the University of California at Berkeley.

![](/api/attachments/DKDA3A7D/fulltext/images/145dc031533d4f387ae14b8e2d0354b5b00006c090ab9e0e604c19b2941e6731.jpg)

Dr. Blake Johnson is an Assistant Professor of Engineering Economic Systems and Operations Research at Stanford University. His research interests include. The application of multiperiod asset pricing methods to the valuation of real assets e.g., businesses, technolo-Ž gies, large projects, real estate as op- . posed to financial assets e.g., stocks,Ž bonds, derivatives ..

versity.

Dr. Johnson has a PhD in Engineering Economic Systems from Stanford Uni-

![](/api/attachments/DKDA3A7D/fulltext/images/ffeeeaffee73481515d1af3b3057e09a5016bdefb347db61559393af065bf52a.jpg)

Dr. Aram Sogomonian was recently named Chief Risk Officer of PacifiCorp. He is currently implementing his organization which will have primary responsibility for understanding the firms risk exposures and how to manage them. Prior to his current position, Dr. Sogomonian was vice president at Pacifi-Corp Power Marketing with primary responsibility for heading up the middle once and analytical functions. Prior to PacifiCorp, Dr. Sogomonian was vice

president of Risk Management at Edison Source. Before coming to Edison Source, Dr. Sogomonian was director of the risk analytics and asset pricing group at Houston-based Enron Capital and Trade resources, which does project evaluation for Enron. Dr. Sogomonian holds a PhD in Management Science from the Anderson Graduate School of Management at UCLA, an MS degree in Operations Research and BA degrees in Applied Mathematics and Economics from the University of California at Berkeley.
