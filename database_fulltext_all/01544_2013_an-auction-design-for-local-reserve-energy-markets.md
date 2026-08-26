---
otero_id: 1544
otero_key: "WTNCSD5A"
title: "An auction design for local reserve energy markets"
authors: "C. Rosen; R. Madlener"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.022"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An auction design for local reserve energy markets

C. Rosen <sup>a,</sup>⁎, R. Madlener <sup>a</sup>

<sup>a</sup> Institute for Future Energy Consumer Needs and Behavior (FCN), School of Business and Economics/E.ON Energy Research Center, RWTH Aachen University, Mathieustrasse 10, 52074 Aachen, Germany

## a r t i c l e i n f o

Article history: Received 1 September 2012 Received in revised form 27 May 2013 Accepted 28 May 2013 Available online xxxx

Keywords: Auction Ancillary services Local market Agent-based simulation Distributed generation

## a b s t r a c t

In this paper we develop an auction mechanism that is designed for a local energy market. It aims to enable regionally or virtually restricted trading of ancillary services, which enhances the position of the balance group responsible party beyond that of simple accounting. Furthermore, it makes local market participants somewhat more independent from the transmission grid operator, but at the same time provides incentives for investments in distributed generation technologies. A wider spread of these technologies can help to save CO emissions, while at the same time a part of them can also be used to counter the <sup>fl</sup>uctuations of energy from volatile renewable sources, such as wind and solar power. Because of their relatively high margins and small share in total production, ancillary services are well-suited for a remuneration scheme. Participants in the auction are, thus, private households, which impose speci<sup>fi</sup>c design characteristics on the auction. Most importantly, it needs to be transparent and easy to understand, as homeowners will typically not have the insights of a professional trader as well as lack a similar position and motivation. Also, the con<sup>fi</sup>nement to a single balance group, i.e. a local market, means that especially in the beginning of the trading only a small number of bidders can be expected Therefore competition will initially be limited, so that the auction design needs to be adapted accordingly. In order to test the performance of the proposed auction market design under varying information policies, a simple agent-based simulation program has been developed. We <sup>fi</sup>nd that the theoretical predictions hold and that competition quickly leads to price convergence.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years ancillary services in electricity markets and especially such providing reserve energy have received increasing attention. This is due to several facts. First of all, the increase of the share of unpredictably <sup>fl</sup>uctuating renewable energy in total energy production has led to a higher demand for reserve capacities to buffer those <sup>fl</sup>uctuations. Secondly, new technological and societal developments have started to offer new ways of meeting this demand. Smaller and larger consumers can offer some of their loads and capacities to external control or even offer load adjustments at certain times of the day themselves. They can further participate in virtual power plants (VPPs) to sell power produced in large numbers of smallscale, distributed home devices, such as micro combined-heatand-power (CHP) plants or photovoltaics. So far, this has been limited to the trade of real power. Balancing energy market mechanisms have only been examined in pilot projects with microgrids, i.e. only under these special circumstances has household energy been used as reserve energy.

The purpose of this paper is to show how in current circumstances decentralized generation can be used bene<sup>fi</sup>cially for a regional energy system with an appropriate auction design. In particular, this paper aims at determining a valid auction mechanism that suits a local reserve energy market with all its special needs and characteristics, as discussed below. Once this mechanism is de<sup>fi</sup>ned, it needs to be evaluated as to how bidders in such a market behave over time. The details with respect to how this mechanism can eventually be implemented optimally are side issues and will, therefore, only be treated brie<sup>fl</sup>y.

Keeping in mind the characteristics of bidders in a local energy auction, the problem that needs to be solved is, thus, to <sup>fi</sup>nd an adequate and reliable remuneration for each provider of reserve capacity and energy. At the same time, the auction mechanism needs to be as simple and easily understandable as possible in order not to turn down potential participants, while reducing opportunities for strategic behavior to a minimum. Moreover, transaction costs in a market with such small quantities need to be low in order to leave room for at least a minimal pro<sup>fi</sup>t. The analysis of an auction for such a matter entails many parts. Electricity auctions are a speci<sup>fi</sup>c type of auction because the good is perfectly divisible and non-storable, which means transactions need to happen in real time or at least at a prede<sup>fi</sup>ned point of time in the future. This type of auction can be compared to the treasury auction, which has received considerable scienti<sup>fi</sup>c attention in the past. So far, game-theoretic analyses of reserve auctions with the properties needed in a local market are very limited.

C. Rosen, R. Madlener / Decision Support Systems xxx (2013) xxx–xxx

The remainder of the paper is structured as follows: In Section 2, the literature on theoretical analysis, electricity auctions, and reserve energy auctions is reviewed. In Section 3, the market is brie<sup>fl</sup>y described as a preparation of the auction model, which is explained in the same section. It is presented for both the asymmetric and the symmetric case and solved accordingly. Section 4 introduces the simulation and theoretical considerations of the strategies implemented, and the results of the simulation. Section 5 explains the technical backgrounds of the simulation as well as the results obtained. Section 6 provides a conclusion and some suggestions for future research.

## 2. Literature review

The liberalization of the electricity sector has fueled the desire to analyze markets and the behavior of market participants. Due to the complex nature of the good itself, each individual market and the interaction of several markets for different energy products have set strong limitations on analytical methods. Therefore, simulations have very quickly gained acceptance in this <sup>fi</sup>eld.

Many different kinds of electricity market models are possible. Ventosa et al. [33] classify them as optimization models, equilibrium models, and simulation models, whereby simulation models can either be derived from equilibrium models or formulated as agent-based models. The main difference between these two is the static nature of the approach in the <sup>fi</sup>rst case and the dynamic approach in the second. Sensfuß et al. [29] categorize these agent-based models as tools to analyze market power and market design, agent decisions and learning, and the interdependence of short-term and long-term decisions. At least for wholesale electricity markets, Weidlich and Veit [35] offer a very different way of distinguishing agent-based models, namely with regard to their algorithms. According to the authors, these may be model-based adaptation algorithms, genetic algorithms, and algorithms applying the reinforcement learning approach by Erev and Roth [14].

From an economic point of view, the major problem with most of the recent electricity market modeling is the overemphasis on detailed modeling of generation equipment [11,21] or individual agents representing several interest groups [23,32], whereas a sound market model has rarely been analyzed. Two exceptions are the analysis of Wilson's design [37] by Otero-Novas et al. [22] and the comparison of uniform-price to discriminatory-price auctions by Bower and Bunn [8].

The remaining part of this section is used to review the literature on auction design in general and for our local market in particular. Especially research on treasury auctions and its accommodation of a small number of bidders or diverse technologies, as well as the literature on electricity and ancillary services auctions is of interest.

From a theoretical point of view, a reserve energy auction is a multi-unit (or share auction, i.e. an auction of a divisible good, with equivalent characteristics; [36]) as well as a multi-part auction. In the multi-unit part it resembles a treasury auction, which is an auction of a divisible good. A very important topic in this <sup>fi</sup>eld is whether uniform pricing or discriminatory pricing, whereof the Ausubel auction [3] is treated as a special case, yields more favorable outcomes. A downside of uniform pricing is that bidders have an incentive to understate their demand for the second and following units in order to win those at lower prices in case of a demand auction. Transferred to a procurement auction like the one at hand, this means that bidders understate their supply, thereby creating an arti<sup>fi</sup>cial scarcity, and are able to extract price premiums [4,13]. Back and Zender [5] describe this mechanism as “collusive”, meaning that each bidder colludes with himself while trying to maximize his pro<sup>fi</sup>t. Even more important is that this does not change with the number of bidders, i.e. no real competition may emerge. Discriminatory pricing does not exhibit these downsides, but helps to limit market power [20], which is especially prevalent in local markets. A disadvantage, however, is that revenues for the auctioneer are generally lower in discriminatory auctions [34]. Put differently, one could say that “competition needs to be bought with higher prices” (i.e. bids). Furthermore, Rassenti et al. [24] <sup>fi</sup>nd that price volatility is reduced in discriminatory price auctions, which is an important feature for markets with household participation, as <sup>fl</sup>uctuating prices can easily alienate this kind of participant and thereby reduce participation rates. Haghighat et al. [17], however, <sup>fi</sup>nd no differences between the two auction formats under imperfect competition, i.e., for example, when bidders can exercise market power or are able to collude.

The model primarily meant for treasury auctions in [34] represents, in principle, a situation very similar to the one at hand. Besides simply equating demand and supply, the authors also allow for non-competitive bids, which reduce the quantity available. The size of this reduction, however, is not endogenous but random. Furthermore, their model uses common values with private signals, which is very straightforward for <sup>fi</sup>nancial goods that are acquired in the hope that they will increase in value, determined by subsequent trading, which affects all holders of such items equally in a common market. This is very different for an energy auction, which comprises several differentiated units and technologies and, therefore, exhibits private values, or rather cost.

Burke and Auslander [9] speci<sup>fi</sup>cally consider a residential electricity auction. While the design is directed at acquiring electricity by residential bidders and should, therefore, entail consumer behavior, it needs only one bid, composed of the maximum quantity desired and the maximum price to be paid. The mechanism then determines how much each bidder can obtain and what price he will need to pay. This is done by using uniform pricing and soft budget constraints, meaning that allocated quantities are reduced for increased prices, but the overall amount being paid remains the same.

Chao and Wilson [10] suggest an auction design with a robust incentive mechanism. Similar to the design currently in use, they require two bids, one for capacity and the other for energy. The capacity bids are used to construct a merit order in which the units are called. Upon being called, they are remunerated with the real-time spot price, which is thus outside their range of in<sup>fl</sup>uence. As this seems to be a promising approach to limiting gaming in the auction process, the basic idea of independence between energy price and bid will be followed in the model presented in Section 3.

Swider and Weber [31] analyze the bidding behavior in the German minute reserve auction market, using a decision-theoretical framework. They are among the <sup>fi</sup>rst to analyze the bidding behavior in the actual market as it occurs in reality. In particular, they address the dif<sup>fi</sup>culty of de<sup>fi</sup>ning a probability density function for the price and thereby the expected price itself, by deriving it from historic time series. However, their investigation can only be applied to a limited extent to a local market, as they look at the behavior of one individual bidder and describe the rest of the market by a probability function. In a small market, this generalization cannot be justi<sup>fi</sup>ed due to the lack of statistical validity.

Another approach with a similar goal is presented in the work by Block et al. [7]. They describe a scenario of a microgrid where households can act as energy consumers and producers in an alternating fashion. For this purpose, they introduce a combinatorial double auction. While it is ef<sup>fi</sup>cient and welfare-maximizing in theory, they do not examine possible gaming strategies or cooperation inherent in the auction design that the bidders might pursue. Also, it is not sensible to use this design in situations with only one buyer.

Hao [19] focuses on simple electricity auctions. While his design allows the usage of probabilities of other bidders bidding less or more, in our case it is too simple to be applied, as it uses <sup>fi</sup>xed MWh blocks combined with a single price bid. The auction is then cleared at the price of the last accepted bid. As concluded in the paper itself, this leads to untruthful bidding and overstatement of costs.

Bernard et al. [6] compare the outcomes of several uniform auction designs with varying numbers of bidders. Similar to the theoretical

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

result derived in our paper later on, they <sup>fi</sup>nd empirical evidence for growing supply reduction with growing group sizes. Unfortunately, their design does not allow the drawing of <sup>fi</sup>nal conclusions from this phenomenon, as it could also be a result of the information given to bidders, namely that not all of their capacity will be used under all circumstances. The auction form chosen was apparently less signi<sup>fi</sup>cant, which hints at the fact that it might be transferable to other forms than those examined by the authors, including pay-as-bid auctions.

However, none of the work presented deals with small, local markets. Therefore, this paper can be seen as an extension to Chao and Wilson's design [10], but with discriminatory pricing instead of uniform pricing and allowing for endogenous demand reduction of the central buyer. From a mechanism design point of view, our work most closely relates to [5,34], who were inspired by the treasury auctions. From the authors cited here, they are the only ones considering continuous bidding functions, while all others focus on discrete bids. In both papers, they chose a theoretical approach, such that their re-<sup>fl</sup>ections on bidding behavior in discriminatory price auctions give important insights into expected outcomes in our local market. The uniqueness of our auction design lies more within the application and the adjustment to the local energy market. Furthermore, the approach of using historic prices in the simulation is inspired by Swider and Weber [31], with bidders adjusting their strategies accordingly. The market and the auction design are presented in the following section. For a better overview of the auction designs examined in previous studies, a table has been produced with a selection of the cited literature. It can be found in the Appendix, Part A.

## 3. Auction design

## 3.1. Getting to know the market

In an electricity grid it is paramount to always have exactly as much power input as consumption. If this is not sustained, blackouts or other major distortions will occur. While commercial energy providers do their best to forecast the demand of the consumers they supply, it can never be perfectly predicted. At the same time, supply from most renewable energy sources (such as wind and solar power) as well as the possibility of power plant outages contributes to unforeseen <sup>fl</sup>uctuations in the power grid. This is the reason why reserve energy for balancing purposes is such a crucial element of the energy system. Most countries have a regime distinguishing between several qualities of reserve energy (cf. Singh [30] for an extensive discussion of the ancillary services market in California). They are activated in hierarchical order in different degrees of automation, after different time spans, and depending on whether there is an energy shortage or surplus. This poses corresponding requirements on the availability of reserve energy and technological infrastructure. In a local market, we assume that the different kinds of reserve energy can all be met by using different types of technologies. For the highest quality batteries seem appropriate as they can almost instantly provide the necessary energy.

Currently, the dimensioning of the capacity needed depends on the forecasts submitted as schedules to the transmission system operator (TSO). It is responsible for the large, transnationally interconnected grids on the highest voltage levels. These grids absorb energy produced by large power stations and transmit as well as distribute it over long distances. The schedules are produced on a lower level by the balance group responsible parties with the help of the commercial suppliers active in their balance group. The lower voltage levels encompass the medium and low voltage grids, where smaller power plants can feed in their energy, and larger and smaller customers extract their demand. Taking Germany as an example, there are four TSOs, but more than 600 balance group responsible parties, who all report to the TSO that supervises their geographical region. Within each balance group, supply needs to equal demand. The balance group responsible party needs to arrange for this by forecasting loads, adjusting supply, and submitting the schedules to its TSO. Using these, the exact amount of capacity needed and the implementation are determined using the regulations put forward by the European Network of Transmission System Operators for Electricity (ENTSO-E) [16]. This means that the demand for reserve capacity is known in advance and perfectly inelastic. On the contrary, the amount of reserve energy that actually needs to be supplied is uncertain and depends on stochastic events. This is why the central auction requires a three-part bid consisting of a capacity price, an energy price, and the amount of capacity offered. The reserve energy is then not used by the TSOs themselves, but again by the balance group responsible parties in their balance group. Due to the stochastic nature of electricity demand and partly also of the supply an exact match is never possible. The balance group responsible party is, therefore, billed by the TSO according to the share of reserve energy it uses in the area that it supervises. Typically, a balance group responsible party is either a local utility, a large industrial consumer with its own energy supply or a trader at the energy exchange, or a combination of the aforementioned. It should be noted that due to the unbundling process the balance group responsible party in the function described here does not possess any generation capacity itself, but is just an administrative entity.

In the current market regime, it is very dif<sup>fi</sup>cult for households to participate in the reserve energy market. The barriers to enter the central market are high and the threshold capacities for the lowest quality are still 5 MW, which most households cannot easily spare. The only way they are affected by the market is through the costs of the reserve energy that are transferred to them by their energy provider as part of their regular bill.

The local market that is proposed in this paper makes the balance group responsible party more independent. Via an online auction platform it can itself ask private households or small businesses that dispose of decentralized generation units (or <sup>fl</sup>exible loads, which is analogous and, therefore, not explicitly treated here) to submit bids to cover its reserve energy needs. Those that win the auction need to reserve the allocated capacity and are automatically called when needed. The auction takes place weekly for the following week for each hour of the day. For renewable sources, it is assumed that reliable forecasts are available. Note that for micro-CHP plants and batteries, this uncertainty is not relevant. As these have higher unit costs, the market price is likely to be driven by these technologies, providing for a risk premium for participants with solar panels. The advantages of a local market for reserve energy are reduced grid losses and reduced market power of the large providers in the central market. Due to the implemented reserve price from the control area level of the TSOs, prices are always lower or equal to the current level. Furthermore, local trading of reserve energy is a necessary complement to trading of real power by private households.

## 3.2. Pricing mechanism

The buyer of reserve energy is, thus, the local balance group responsible party with total demand Q. Q is measured in kW (kilowatt) as only the capacity to be reserved is known. Sellers are market participants that bid within an auction. In this case they are households that dispose of devices that are capable of energy production or provision. These would typically be single- or multi-family homes with solar panels, micro-CHP plants, or storage batteries. Furthermore, small businesses with similar equipment that does not exceed 50 kW of installed capacity might also be included. Note that this threshold is not arbitrary, but speci<sup>fi</sup>ed in the EU Directive 2004/8/EC [15] and is also the upper threshold for the highest remuneration (disregarding the option of heat-driven operation, which has been treated differently since the latest amendment, cf. [1]) for electricity from CHP plants according to the German CHP Act, where §7, Art. 4 [2] regulates that for an installed capacity of 50 $\mathrm { k W _ { e l } , }$ a subsidy of 5.11 Euro-ct per kWh is paid.

There are n bidders. Each bidder $i \in I ,$ with I being the set of potential bidders, can submit a set of offers $q _ { i } ( p )$ , which consists of an arbitrary number of $( l _ { i } + 1 )$ bids.

A bid $x _ { i , k }$ is composed of a price $p _ { i , k } \left[ \in \mathbf { \Omega } / \mathrm { ~ k W } \right]$ and the amount of capacity to be reserved $q _ { i , k } [ \mathrm { k W } ]$ . Index k with $k \in { 0 , 1 , . . . , }$ l hereby denotes the rank of an individual bid among all bids submitted by bidder i. Each bidder may submit $l _ { i }$ of these bids altogether plus a mandatory nil-offer (0;0). This gives the above-mentioned total number of bids $q _ { i } ( p ) = ( x _ { i , 0 } , x _ { i , 1 } , . . . , x _ { i , l } )$

The bids are ranked with $x _ { i , 0 }$ being the lowest offer and $x _ { i , m a x } ( = x _ { i , l } )$ being the highest offer. A continuous set of offers thereby constitutes an offer function. Each bidder knows his cost as a function of quantity $c _ { i } ( q )$ Per bidder and auction only one contract is concluded and the successful bid is denoted by $x _ { i } ^ { * } .$ The balance group responsible party can further buy the amount $q _ { R }$ at price $p _ { R }$ from the transmission grid operator. Obviously, it does not make sense for the buyer to procure reserve energy in the local market if it costs signi<sup>fi</sup>cantly more than in the global market. Article 29 (3) of the European Council Directive 90/531/EEC [12] sets the price difference up to which offers can be regarded as equivalent to 3%, giving preference to local offers.

Let $p$ be the vector of prices that the balance group responsible party faces due to the submitted sets of offers and let q be the corresponding quantity vector, as emerging from the bids $x _ { i \cdot }$ The total costs for the grid operator are, thus,

$$
Y (p, q _ {R}): \mathbb {R} ^ {n + 1} \rightarrow \mathbb {R} \text { with } Y (p, q _ {R}) = p ^ {T} q + q _ {R} p _ {R}.\tag{1}
$$

Successful bids and the capacity to be reserved via the TSO can be determined by solving the minimization problem mi $1 _ { p , q _ { R } } \left[ Y ( p , q _ { R } ) \right]$ The sum of the power bought from bidders and the grid operator must be at least as much as total demand Q, where $Q$ is de<sup>fi</sup>ned as the capacity that needs to be reserved times the time slot considered, which is one hour: $\sum { _ { i } q _ { i } } \ge Q . Q$ can either be determined in a separate optimization problem or might be de<sup>fi</sup>ned in some future amendment to the current ENTSO-E procedures. Both possibilities will not be discussed further at this point and, therefore, Q will be viewed as externally given, i.e. <sup>fi</sup>xed and inelastic. Furthermore, the price constraint in acknowledgment of the EU Council Directive 90/531/EEC needs to be obeved: $p _ { i } \le 1 . 0 3 p _ { R } .$

The solution to this optimization problem describes the pricing mechanism. The complete optimization problem is, thus,

$$
\begin{array}{l l} & \min _ {p, q _ {R}} (Y (p, q _ {R})) \\ \text { s.t. } & \sum_ {i} q _ {i} - Q \geq 0 \\ & 1. 0 3 p _ {R} - p _ {i} \geq 0 i \in I. \end{array}\tag{2}
$$

From here, the solution $\left( p ^ { * } ; q _ { R } ^ { * } \right)$ follows with $\boldsymbol { p } ^ { * } = ( p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , . . . , p _ { n } ^ { * } )$ whereas the successful bid of bidder i is given as $x _ { i } ^ { * } = [ p _ { i } ^ { * } , q _ { i } ^ { * } ( p _ { i } ^ { * } ) ]$ The bidder's pro<sup>fi</sup>t, taking into account his cost function $c _ { i } ( q )$ , is $\pi _ { i } = q _ { i } ^ { * } p _ { i } ^ { * } - c _ { i } ( q _ { i } ^ { * } )$

In case of discrete bids $q _ { i } ( p )$ , a situation of ties may emerge. This situation arises with price equality of several quantities offered and when each quantity as such is suf<sup>fi</sup>cient to ful<sup>fi</sup>ll the constraint, i.e. each quantity is at least as large as the missing amount up to total demand. In this case, the bid with higher quantity is preferred. If prices as well as quantities among bidders are equal, the winner is determined randomly with equal probabilities.

The information <sup>fl</sup>ow starts with the determination of the required quantity according to UCTE requirements. The balance group responsible party can then publish the beginning and the end of the auction as well as invite participants to submit bids. After determining their free capacity and evaluating the competition to optimize their bids, these may then send their offers. From the prices and quantities the balance group responsible party can estimate whether it is able to procure enough reserve energy at a reasonable price. If there is not enough reserve energy offered, or if prices exceed those on the global market, i.e. the market at the transmission grid level, it should be able to register its residual needs with the TSO. Such a mechanism is currently not available in the market, but should require only a small change in the current regulation. At the same time, successful bidders are informed about the quantities they are obliged to reserve and prepare to be called.

## 3.3. Bidder's strategy

## 3.3.1. Asymmetric case

In principle, each bidder tries to maximize his expected pro<sup>fi</sup>t. The expected pro<sup>fi</sup>ts are the sum of all bids less the respective costs weighted by the respective probability of winning. Costs are hereby a very general term and do not only include technology-related costs like fuel expenses, but also opportunity costs that rise with quantity as some of the available capacity might be needed for consumption within the household. In this sense the cost variable is equivalent to an individual reservation price. In the discrete case the expected pro<sup>fi</sup>t can be expressed as

$$
\begin{array}{l} E _ {d} (\pi_ {i}) = \sum_ {k} \Big (P r \Big (q _ {i, k} \Big) \Big (p _ {i, k} - c _ {i} \Big (q _ {i, k} \Big) \Big) q _ {i, k} \Big) \\ \sum_ {k} P r \Big (q _ {i, k} \Big) = 1. \end{array}\tag{3}
$$

In the continuous case, the probabilities are expressed by a func tion $f ( q )$ , giving the following formula for expected pro<sup>fi</sup>t:

$$
E _ {c} (\pi_ {i}) = \int_ {0} ^ {q _ {i, l}} f (q) (p _ {i} (q) - c _ {i} (q)) q d q.\tag{4}
$$

Note that in both cases, $p _ { i } ( q ) = q _ { i } ^ { - 1 } ( p )$ . The problem is that unlike in [19] the probability is not dependent on a simple <sup>fi</sup>gure, but on a function or at least the association of price and quantity. Therefore, it cannot be assumed to exhibit continuity and is intractable analytically ex ante. In the current setting, there is thus no easy way to work with it.

To complete the analysis of the auction and the expected pro<sup>fi</sup>t to be gained from it, the energy that is actually being called and remunerated separately should also be considered. As the necessary reserve energy per time slot cannot be known a priori, it can only be embraced in stochastic terms. The reserve energy being called, w , is, thus, a function of the capacity reserved.

In order to prevent gaming and market power, it is advisable to ensure equal chances for each participant in the calling process, much unlike the current procedure of arranging a merit order. In other words, the process needs to ensure that the probability of being called exhibits a uniform distribution. Let the expected value thereof be $\gamma .$ The expected pro<sup>fi</sup>t of an individual bidder then becomes

$$
E (\pi_ {i}) = \int_ {0} ^ {q _ {i}, l} \left(q * p _ {i} + \int_ {t _ {s}} ^ {t _ {f}} \gamma q d t p _ {W} - c - c _ {W}\right) f (q) d q,\tag{5}
$$

where $c _ { W }$ is the additional cost that is incurred for generating the power called. Under the condition that $p _ { W }$ is greater than $c _ { W } ,$ riskaverse bidders should not add this additional stochastic pro<sup>fi</sup>t to their certain pro<sup>fi</sup>t during the strategy-planning phase at the auction stage. This means that they would never understate their costs for reserving capacity to increase their chances of winning the auction in the expectation of making up for it by being called and receiving additional payment for delivering energy.

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

Summing over all $q _ { i } ^ { * } ,$ total costs of the balance group responsible party become

$$
Y = p ^ {T} q + p _ {R} q _ {R} + \int_ {t _ {s}} ^ {t _ {f}} \gamma Q p _ {W} d t\tag{6}
$$

for each time slot, where $p _ { W } \left[ \in \mathrm { ~ / ~ k W h } \right]$ is the constant energy price for reserve energy called. As this energy price as well as Q, the total capacity to be reserved, and $\gamma ,$ the expected value of the portion of power actually called, are all independent from the bid sets $( p _ { i } , q ( p _ { i } ) )$ , the solution of the optimization problem remains identical to the solution from Eq. (2). It can clearly be seen that the price and the amount of energy being called do not in<sup>fl</sup>uence the pricing mechanism. Please also note that this structure makes the auction mechanism very robust, as truthful bidding is the dominant strategy.

## 3.3.2. Symmetric case

In the case of a symmetric market, the bid functions of all bidders are identical, i.e. $q _ { 1 } = q _ { 2 } = \ldots = q _ { n } .$ This could happen when all bidders have identical technologies, for example when solar panels are especially popular in a city quarter. Furthermore, the symmetric case gives a <sup>fi</sup>rst benchmark for the behavior in an asymmetric market.

The total costs of the buyer are, thus,

$$
\begin{array}{l l} & Y _ {\xi} = n p _ {\xi} q _ {\xi} + q _ {R} p _ {R} \\ \text { s.t. } & p _ {\xi} = p _ {1} = p _ {2} = \ldots = p _ {n} \\ & q _ {\xi} = q _ {1} = \ldots = q _ {n} = q _ {\xi} \big (p _ {\xi} \big), \end{array}\tag{7}
$$

i.e., the price received by each bidder is $p _ { \xi }$ and the corresponding power offered is $q _ { \xi } .$ From this, the optimization problem can be written as:

$$
\begin{array}{l l} & \min _ {p, q _ {R}} \left(n p _ {\xi} q _ {\xi} + q _ {R} p _ {R}\right) \\ \text { s.t. } & n q _ {\xi} - Q \geq 0 \\ & 1. 0 3 p _ {R} - p _ {i} \geq 0 \quad i \in I. \end{array}\tag{8}
$$

As competition rises, a transition phase begins. During this phase, bidding is according to the Cournot equilibrium, where quantities are endogenously determined while understating capacities. As soon as capacities signi<sup>fi</sup>cantly outrange total demand, a situation of perfect competition is reached. This motivates bidders eventually to bid their marginal (economic) costs $c _ { i } ( q )$

In order to <sup>fi</sup>nd out the point up to which it makes sense for the bidder not to deviate from the collusive bid, i.e. from which point onwards convergence to competitive bidding can be assumed one needs to compare bidder j's pro<sup>fi</sup>t under each bidding regime:

$$
\pi_ {i} = \frac {Q}{n} (p _ {R} - c).\tag{9}
$$

When deviating, the pro<sup>fi</sup>t becomes

$$
\pi_ {j} = q _ {j} (p _ {R} - c - \varepsilon).\tag{10}
$$

Letting $p _ { R } - c = m$ and rearranging terms, one obtains from $\pi _ { i } = \pi _ { j }$ that

$$
\varepsilon = \frac {q _ {j} n - Q}{q _ {j} n} m.\tag{11}
$$

Note that $q _ { j } , Q ,$ and m are all <sup>fi</sup>xed. The only changing parameter is, thus, n, i.e. the number of bidders participating in the auction. For a growing number of participants, ε grows as well. This is in line with theoretical considerations of market movements, as it says that the greater the competition, the faster prices drop to marginal costs. This is because once someone has deviated, the other bidders will follow in the coming round until equilibrium is reached and everyone bids marginal costs. This already implies that m or rather p needs to be updated for every round, meaning $p _ { j , t } = p _ { j , t - 1 } - \varepsilon \mathrm { o r } ,$ , reformulating

$$
\begin{array}{l} p _ {j, t} = \frac {q _ {j} n - Q}{q _ {j} n} c + \frac {Q}{q _ {j} n} p _ {j, t + 1} \\ p _ {j, t + z} = c. \end{array}
$$

until

<sub>ð</sub><sup>12</sup><sub>Þ</sub>

Note that ε is the upper limit of the amount by which the price should be reduced. If it were a little more, the bidder would be better off sticking to the old price and strategy. In order to get the strategy working, a much smaller amount of reduction might suf<sup>fi</sup>ce. However, this is only true for the symmetric case. For the asymmetric case, the undercutting will stop as soon as the most costly generators bid their marginal costs. Therefore, less cost-intensive generators can sustain a higher pro<sup>fi</sup>t forever, at least if total demand Q cannot be met by them alone. This higher pro<sup>fi</sup>t margin equals the marginal costs of expensive generators less the marginal costs of cheaper generators. If, however, demand can be met by the reduced number of less cost-intensive generators, more cost-intensive generators are driven out of the market, as competition continues until the price has reached marginal costs of less expensive generators, at least as long as there are no regulatory measures to prevent such an outcome. This also means that none of the bidders has an incentive to underbid costs, who might have a motivation in a commercial setting, for example to secure a higher market share. In the household setting at hand, and with such limited capacities, strategic actions in terms of marketing activities are not relevant.

The calculation of the expected pro<sup>fi</sup>t of the individual including energy called is analogous to the asymmetric case.

## 4. Simulation of an asymmetric market

In the previous section we have seen the derivation of the strategy for symmetric bidders, which can be used as a reference value now. For an asymmetric market, however, an analytical solution is very hard to <sup>fi</sup>nd, as we cannot construct the probability of winning in the auction. This leaves us with the option of simulation. In the case presented here, a learning strategy has been formulated and translated into an algorithm as presented in the coming paragraphs. The formulation of probability expectations is not necessary for the current investigation, but will be handled later on in the course of the still ongoing research project, which is running till the end of 2012 and investigates behavior of energy consumers using experimental methods.

The second part is the cognition and strategy formulation of the bidders. The basic bidding curves are characterized as partially differentiable functions of the form

$$
p (q) = k \left(a _ {0} + a _ {1} q + a _ {2} e ^ {b q}\right).\tag{13}
$$

This means that bidding curves of several shapes can be implemented, i.e. they may be linear, constant, or exponential. They might be limited by the real world boundaries, such as the corresponding cost functions, but are meant to be monotonically increasing in principle. The mathematically redundant coef<sup>fi</sup>cients k and k are used for reasons of practicality, i.e. to be able to easily shift the curves upwards or downwards if required by the implemented strategy. The cost functions are modeled accordingly and exhibit the same properties:

$$
c (q) = k _ {c} \left(a _ {c 0} + a _ {c 1} q + a _ {c 2} e ^ {b _ {c} q}\right).\tag{14}
$$

An example cost curve and bidding curves for the <sup>fi</sup>rst 30 rounds of the “no information” case (see explanations further below) are shown in Fig. 1. The cost curve is the lowest curve in the diagram, and the squares are the accepted bids.

After each auction round, the bidder is informed about his winning bid. The quantity is a point between zero and the maximum quantity bid, while the price is determined from the bid function. This means that in the following round, the bidder can react to the outcome and either increase his price (i.e. shift his bid function upwards) to increase his pro<sup>fi</sup>t margin or lower his price (i.e. shift his bid function downwards) to increase chances of selling a higher quantity. His action space is thereby limited by the given cost function, which represents a lower limit. This algorithm is modeled according to the learning direction theory of Selten and Stoecker [28]. Hailu and Schilizzi [18] also showed that there is no signi<sup>fi</sup>cant difference in outcome when applying a more complicated learning algorithm, like the reinforcement algorithm by Roth and Erev [27,14], which is why we can comfortably stick to the simpler algorithm.

Furthermore, bidders can differ in a number of ways: First of all, they own equipment of various sizes in the range from 3 kW to 50 kW, which is randomly distributed with a mean of 9 kW and a standard deviation of 6.3 kW. To illustrate this, bidding curves of all bidders in the market are shown in Fig. 2; squares are again accepted bids. Each bidding curve stops at the maximum capacity. Secondly, their bidding curves as well as cost curves may be steeper or <sup>fl</sup>atter, also randomly generated with the coef<sup>fi</sup>cients introduced in Eqs. (13) and (14) above. Moreover, <sup>fi</sup>xed and variable prices vary across bidders, re<sup>fl</sup>ecting ample technologies. The strategy used by all bidders is to increase or decrease their bids by some percentage points, depending on whether they are satis<sup>fi</sup>ed with the outcome or not. The boundary is hereby set to 25% of each bidder's individually available capacity.

Three main scenarios are scrutinized, varying in the information provided to the bidders. In each scenario, 24 bidders participate in the market during 365 rounds. The idea is to test several plausible scenarios that are based on different information policies, but also on how this information is processed, i.e. how the bidder lets himself be in<sup>fl</sup>uenced (in terms of bids for the coming round) by the information provided. Information policies are inspired by Ausubel [3], who suggests a no-bid information, an aggregate bid information, and a full bid information policy. As Ray and Cashman [25] report, different degrees of information provision make sense from a regulatory point of view, especially in markets where perfect competition cannot be guaranteed and market power might be an issue. In an early phase of the market introduction scarce information can, thus, spur competition and disencourage collusion, which is why regulators employed this strategy in New South Wales (Australia) when restructuring the electricity market [26]. This leads us to the following scenarios subject to our analysis:

![](/api/attachments/WTNCSD5A/fulltext/images/26a29e7bd2b34fe0ff310b3248839d2e5097bc767a977c0bc517628da0700013.jpg)  
Fig. 2. Bidding curves of all bidders in the 25th round of the “no information” case

as long as he can still generate a pro<sup>fi</sup>t, i.e. as long as he is not bidding his cost curve. In the case where it is accepted, the bidder might be content with the outcome and not change anything. However, he might also want to gain more pro<sup>fi</sup>t by increasing the capacity sold. In this case, strategy adaptation might happen under the condition that the previous pro<sup>fi</sup>t margin is maintained, but stretched to more units.

Together with the cost function, the information can be used to <sup>fi</sup>nd the most pro<sup>fi</sup>table response to the actions of the other bidders. This also means that the implemented strategies do not necessarily force the bidder to lower prices, but may also push him to increase prices when competition allows it.

The aggregated price curve is constructed by summing up the inverse of all submitted bid functions, whereas total supply is a vertical curve at the quantity desired. From the intersection the market price, i.e. the highest price paid per kW in this market, can be determined:

$$
\sum_ {i = 1} ^ {n} p _ {i} ^ {- 1} (q) - Q = 0.\tag{15}
$$

At the same time, $p ^ { * }$ solves the inverse of the above-mentioned equation and is the highest price any bidder can obtain and beyond which chances of winning dramatically decrease. It is, therefore, most sensible for a bidder to bid <sup>fl</sup>at at this price to achieve the highest pro<sup>fi</sup>t margins while assuring the maximal sales volume. In case his sales volume drops too low, he can choose to adapt his strategy by bidding just below the market price. At any point in time, he will not bid more than the reserve price because the balance group responsible party would never accept such a bid and he will bid his cost curve whenever

2. All accepted bids;

1. Total supply and aggregated price curve of accepted bids;

3. No information.

In each scenario, the bidder's bid may or may not be accepted. In the case where it is not accepted, the bidder will adapt his strategy

![](/api/attachments/WTNCSD5A/fulltext/images/13588bbb4ebb6f27c3503ee51e424f4ac41edfaf28a1c735602be20c91079dde.jpg)  
Fig. 1. Example cost curve and bidding curves with price convergence over 30 rounds.

Parameter values in the simulation

<table><tr><td>Variable</td><td>Mean  $\mu$ </td><td>Standard deviation  $\sigma$ </td><td>Min value</td><td>Max value</td></tr><tr><td> $k$ </td><td>8</td><td> $k\frac{1}{0}$ </td><td>0</td><td> $k*3$ </td></tr><tr><td> $a_0$ </td><td>0.3</td><td> $a_1\frac{1}{0}$ </td><td>-15</td><td>15</td></tr><tr><td> $a_1$ </td><td>-0.8</td><td> $a_2\frac{2}{0}$ </td><td>-15</td><td>15</td></tr><tr><td> $a_2$ </td><td>5</td><td> $a_3\frac{2}{0}$ </td><td>-15</td><td>15</td></tr><tr><td> $b$ </td><td>0.1</td><td> $b\frac{1}{0}$ </td><td>-15</td><td>15</td></tr><tr><td> $a_{c0}$ </td><td>-0.1</td><td> $a_{c1}\frac{1}{0}$ </td><td>-5</td><td>5</td></tr><tr><td> $a_{c1}*(qmax/lqmax)$ </td><td>1</td><td> $a_{c2}\frac{1}{0}$ </td><td>-5</td><td>5</td></tr><tr><td> $a_{c2}$ </td><td>2</td><td> $a_{c3}\frac{1}{0}$ </td><td>-5</td><td>5</td></tr><tr><td> $b_c*(qmax/lqmax)^{0.7}$ </td><td>0.2</td><td> $b_{c1}\frac{1}{0}$ </td><td>-5</td><td>5</td></tr><tr><td> $qmin$ </td><td>0</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $qmax$ </td><td>9</td><td> $qmax*\frac{7}{10}$ </td><td>3</td><td>50</td></tr></table>

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

![](/api/attachments/WTNCSD5A/fulltext/images/9c59d80e5a72be5184c833c12dd1e4d44a868dca2a5f2b5d0108535932cbe142.jpg)  
Fig. 3. Flowchart of bidding algorithm and price determination algorithm.

the <sup>fl</sup>at bid would not cover the expenses for a certain amount of energy reserved. His bid function, thus, looks like:

$$
p _ {i} (q) = \left\{ \begin{array}{c c} p _ {R} & \beta p ^ {*} \geq p _ {R} \geq c _ {i} (q) \\ \beta p ^ {*} & p _ {R} \geq \beta p ^ {*} \geq c _ {i} (q) \\ c _ {i} (q) & \beta p ^ {*} <   c _ {i} (q) \end{array} \right..\tag{16}
$$

Note that β is equal to one as long as the bidder is satis<sup>fi</sup>ed with the quantity sold. If it drops too low, β becomes a discount factor for the bid function, which is randomly chosen from a normal distribution with a mean of 0.98 and a standard deviation of 0.01. It has an upper limit, as risk-averse bidders will not become more expensive.

![](/api/attachments/WTNCSD5A/fulltext/images/615a636718316f19f5e3066ee0a0377eacfe54d6cf848f6e6c862d1033f267cb.jpg)  
Fig. 4. Overview of capacities of all bidders.

When the information provided is very detailed, the bidder can look at the individual price/quantity-pairs and might, for example, adjust his curve to intersect all the winning points or to lie just below them. Otherwise, he might simply identify the point that is most pro<sup>fi</sup>table to him and adjust his bid curve to have this pro<sup>fi</sup>t margin for all possible quantities. As this kind of extensive information supports a variety of strategies, we exemplarily implement two possible reactions. In the <sup>fi</sup>rst, as mentioned above, the most pro<sup>fi</sup>table winning point is identi<sup>fi</sup>ed and the bid is adjusted to ensure the same amount of pro<sup>fi</sup>t for all quantities larger than the one in this point. Below this limiting quantity, bids are <sup>fl</sup>at on the price in the optimal point. The most pro<sup>fi</sup>table bid

$$
\tilde {x} _ {s} = [ p _ {s}, q _ {s} ]\tag{17}
$$

is, thus, determined from:

$$
\max _ {\tilde {x} _ {k}} (p _ {s} - c _ {i} (q _ {s})) q _ {s}.\tag{18}
$$

His bidding curve is then:

$$
\tilde {p} _ {i} (q) = \left\{ \begin{array}{l l} \frac {(p _ {s} - c (q _ {s})) q _ {s}}{q} + c (q) & q > q _ {s} \\ p _ {s} & q \leq q _ {s}. \end{array} \right.\tag{19}
$$

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

C. Rosen, R. Madlener / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/WTNCSD5A/fulltext/images/711a5e962c73b2ea5ffbf67537201b3f84ba0b124b13fe605b67698350fe0cf8.jpg)

![](/api/attachments/WTNCSD5A/fulltext/images/d8b9799a50e4a0b1a0fcde354d84183880dbfdad4b016bb498a573e1019afb04.jpg)  
Fig. 5. Expenditures of the balance group responsible party (left plot) and highest, average, and lowest price received (right plot) in “all accepted bids” information setting with <sup>fl</sup>at bids.

In other words, he bids his costs plus the most suitable relative pro<sup>fi</sup>t margin for large quantities and the optimal price for low quantities. In case he does not sell enough with these bids, he can shift his bid functions downwards with the same randomly distributed discount factor β as in the previous section.

In the second reaction, bids are <sup>fl</sup>at at the most pro<sup>fi</sup>table point until they hit the cost curve

$$
\tilde {p} _ {i} (q) = p _ {s}.\tag{20}
$$

This can be regarded as an easier strategy from the point of view of the household bidder and has also been put forward by [34], among others, as an equilibrium strategy. Discounts are assumed to be given by β again. As bidding above the reserve price does not make any sense, we can summarize the bid curves for both alternatives as follows:

$$
p _ {i} (q) = \left\{ \begin{array}{l l} p _ {R} & \beta \tilde {p} _ {i} (q) \geq p _ {R} \geq c _ {i} (q) \\ \beta \tilde {p} _ {i} (q) & p _ {R} \geq \beta \tilde {p} _ {i} (q) \geq c _ {i} (q) \\ c _ {i} (q) & \beta \tilde {p} _ {i} (q) <   c _ {i} (q). \end{array} \right.\tag{21}
$$

In the “no information” case, the bidder does not receive any information on what happened during the auctioning process and what the outcomes of the other bidders were. He has only the feedback if at all and how much he was able to sell from his capacity offered. This input added he can decide whether he is happy with his personal result or whether he would like to sell more. If he concludes that the quantity sold should be increased, he needs to lower the price. He does so in a similar manner as in the <sup>fi</sup>rst and in the second case, i.e. by pushing down his bid curve with the discount factor $\beta .$

![](/api/attachments/WTNCSD5A/fulltext/images/3061a7f36232bec69ea1156462b5be88302244ab81c2c5fd3c686394467acf90.jpg)

However, he does not change the shape of his original bid curve determined in Eq. (13).

## 5. Simulation set-up and results

## 5.1. Set-up

The simulation program has been implemented on an objectoriented basis in MATLAB, version R2011b, using the MATLAB optimization toolbox. It has been run on a Windows 7 machine with a dualcore processor, taking a runtime of about 30 to 60 min. Each bidder behaves as an independent agent trying to maximize his own pro<sup>fi</sup>t. He is modeled using the bid function (Eq. (13)) and the cost function (Eq. (14)) developed in Section 4. The exact values of the parameters in the functions are determined by a random number generator that draws values from a given distribution. The mean values and the standard deviations of the distributions for each parameter can be seen in Table 1. The capacities, for example, are set between 3 kW to 50 kW, and are randomly drawn from a distribution with a mean of 9 kW and a standard deviation of 6.3 kW. The so-constructed normal distribution is now cut off at 3 kW at the lower end and 50 kW at the upper end. Capacities of each bidder are illustrated in Fig. 4, with the dark horizontal line describing the mean of the sample and the lighter horizontal lines describing the con<sup>fi</sup>dence interval of one standard deviation in the sample. Please note that the theoretical mean and standard deviation and the sample mean and standard deviation do not exactly coincide because of the small sample size and, more importantly, because of the imposed upper and lower bounds when drawing the sample. The slope is determined in a similar way with a mean of −0.8 and a standard deviation of 0.04. For computational reasons, the limits here are set at +15 and −15. Fixed costs are described by the product of k and $a _ { 0 } .$ The start price (y-intercept) of

![](/api/attachments/WTNCSD5A/fulltext/images/d31483bcbe603f6e12dd17d5c73545062f70f3125d7cc2025124bb679ee98d2b.jpg)  
Fig. 6. Expenditures of the balance group responsible party (left plot) and highest, average, and lowest price received (right plot) in “all accepted bids” setting with individual bid functions.

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

C. Rosen, R. Madlener / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/WTNCSD5A/fulltext/images/b3437ee61c9cfbf869a46eb93f9537db112c9a70914e21f9feda7c2efb154c09.jpg)

![](/api/attachments/WTNCSD5A/fulltext/images/435fd8ae20de60c7b417094ec10e4dd42117e0751ffa67027573423ebca6cc63.jpg)  
Fig. 7. Expenditures of the balance group responsible party (left plot) and highest, average, and lowest price received (right plot) in a no information setting

the bid function is constructed by analogy. The resulting con<sup>fi</sup>guration has been produced automatically at the beginning of the <sup>fi</sup>rst simulation. To allow comparisons across treatments it has then been saved and served as input for all other simulations as well.

Depending on the strategy used by a bidder he adjusts original bidding curves according to Eqs. (16), (19), and (21) after the <sup>fi</sup>rst auction round.

The simulated auction round proceeds as follows: After all bidding agents have “submitted”, i.e. formed their bidding curves, the resulting optimization problem is solved according to Eq. (2). This classical nonlinear programming (NLP) problem represents, thus, the role of the balance group responsible party. For determining the outcome of the pricing mechanism, an SQP Solver with an active-set method is applied.

The outcome of this optimization is then used as an input for the following auction round. This can be in the form of the aggregated price curve of accepted bids, individual price-quantity pairs, or only the information of how much of the own capacity has been sold. Bidding agents use this feedback to evaluate their bidding curve of the preceding round and adjust it, if necessary, in the current round according to the strategies described before.

This procedure is repeated 365 times to cover an entire year. Output at each stage is a table with the adjusted parameters of the bidding curve of each bidder, individual pro<sup>fi</sup>ts gained, and expenditures of the balance group responsible party. Fig. 3 shows the <sup>fl</sup>owchart of the algorithm for determining the bid in general (left-hand side) and the function for determining the price of a bid in case full information is provided (right-hand side). The code for this part of the simulation can be found in the Appendix, Part B.

## 5.2. Results

The results clearly show that the information policy in a local reserve energy market makes a difference. Generally speaking, the more information is provided, the <sup>fi</sup>ercer the competition becomes.

In the “all accepted bids” case, market equilibrium is reached after only about ten rounds. Even in case the convergence process were to take longer in a real-world setting, the swiftness is remarkable and promises a reliable market. When assuming <sup>fl</sup>at bid functions, convergence stretches over 100 auction rounds before equilibrium is reached. However, even this is rather quick and proves the robustness of the mechanism. The equilibrium price is only slightly higher in the second case (0.16 cents), which can be regarded as non-signi<sup>fi</sup>cant.

In the “no information” case, where bidders have only their individual feedback, competition is signi<sup>fi</sup>cantly reduced. Although bidding is according to individual bid curves that maintain their shape during the entire process, market equilibrium takes more than 180 rounds to be reached. Compared to the full information case above, the market is less ef<sup>fi</sup>cient, and thus suffers from the typical market failure. Also, the equilibrium price is twice as high forever, providing a substantially higher pro<sup>fi</sup>t for the households in the long run.

The case “total supply and aggregated price curve” gives a result that lies in between the informational extremes of the two other cases. When thinking about what information is given to the bidders and how they can react to it, this is not surprising. After 215 rounds, market equilibrium is reached with an equilibrium price of about the same amount as in the “all accepted bids” case with individual bid functions that are only <sup>fl</sup>at on the <sup>fi</sup>rst part. Interestingly, it is below the “all accepted bids” case with <sup>fl</sup>at bids, but not signi<sup>fi</sup>cantly. The slow speed of convergence can be explained by the single point that is provided to the bidders on the one hand, and the lowering of the price in response to dissatisfaction on the other hand. Even when lowering the price in one round, the market price is still likely to remain less signi<sup>fi</sup>cantly changed. With this higher reference point, bidders can go back to the higher price in the next round, thus hindering the market dynamics.

The information policy chosen for such a market thus depends on what authorities would like to achieve. For energy markets, this is of

![](/api/attachments/WTNCSD5A/fulltext/images/744c9ce3597f225aedfc08870e48ae7cc44ade11871e77e7365f2adec4c599de.jpg)

![](/api/attachments/WTNCSD5A/fulltext/images/ede2bb0bc9db47d0bf002c66237b621cbbb6743e9e5b94bf0a0033cbdbcc33dc.jpg)  
Fig. 8. Expenditures of the balance group responsible party (left plot) and highest, average, and lowest price received (right plot) in aggregated information setting

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

special interest, as regulators usually try to achieve explicit goals with their guidelines. Considerable pro<sup>fi</sup>ts can attract more participants in the market and thereby support liquidity and competition, calling for a policy with very limited information. If, however, the objective is to run the market as ef<sup>fi</sup>ciently as possible from the beginning, in order to bene<sup>fi</sup>t from low reserve energy prices immediately, a broader information policy should be put into place. These results are also illustrated in Figs. 5–8. More detailed output data is available from the authors upon request.

## 6. Conclusion

In this paper a new auction model for a local reserve energy market has been introduced and tested in a simulation. It has been designed to accommodate the special needs of non-expert bidders such as private households. This model can be used to revolutionize the reserve energy market, as a balance group responsible party is given the chance to self-supply reserve energy. Thereby it serves several purposes as it helps to further integrate decentralized and renewable energy penetration, but can also help to lower the costs for reserve energy by cutting back the market power of the currently dominating, large-scale utility companies. Final energy consumers can pro<sup>fi</sup>t from this twice because they are the ones providing the energy and getting paid for it as well as having to pay a lower energy bill, once the market provides cheaper reserve energy. At the same time the mechanism supports the remuneration and subsidy schemes for decentralized and renewable energy that are already in place. In the long run, when promotion schemes eventually expire, it can serve as a long-lasting incentive scheme for investments in the designated technologies. This is supported by both the results from the theoretical investigation of the symmetric case and the simulation of the asymmetric case. We found that the information policy in the market has a signi<sup>fi</sup>cant in<sup>fl</sup>uence on the speed of convergence and also a small effect on the equilibrium market price that is <sup>fi</sup>nally reached. In the extreme treatment with no information provided, the effect on the equilibrium price becomes substantial and, even more importantly, is sustained inde<sup>fi</sup>nitely, which emphasizes the importance of the design choice.

The advantage of such a market-based incentive scheme is that it eliminates itself when it is no longer needed. This can happen under two circumstances: Firstly, as soon as further investments in the supported technologies do not enhance total welfare anymore and secondly, as soon as the slope of the learning curves for the respective technologies has reached its minimum alongside with the unit costs of the technologies, such that the acquisition happens without the need of subsidies. Furthermore, the concept can be used in a microgrid to solve the issue of remuneration of ancillary services. If a barter economy is desired in such circumstances, bids can easily be translated into amounts of energy that may be consumed at a later point in time.

Beyond energy markets the design can also be applied in other small, possibly local markets, for example those known in the <sup>fi</sup>nancial sector, i.e. cloud <sup>fi</sup>nancing or crowd funding. These are characterized by a rather non-professional environment (usually no banks or other <sup>fi</sup>nancial institutions participate) and aim to gather a certain, predetermined amount of <sup>fi</sup>nancial resources. Whether an explicit reservation price makes sense in those circumstances remains to be determined. An implicit reservation price is, however, certainly given by the prevailing conditions of the of<sup>fi</sup>cial <sup>fi</sup>nancial sector. Moreover, competition is likely to be much more quantity-based, as market participants might like to invest a certain amount and only <sup>fi</sup>ne-tune according to the prices on the market.

Subsequent research will need to examine how actual human bidders react to the proposed design and whether theoretical predictions as well as simulation results hold. To this end, we plan to conduct a laboratory experiment as an empirical test of the validity of the design. This is also supposed to investigate the importance of the auction format on truth-revealing behavior in this context. Field tests can further validate these <sup>fi</sup>ndings and enable the investigation of practical issues. Finally, it would also be interesting to examine some other parameters than those chosen alongside the possibility of market entry and mechanisms to prevent collusion.

## Acknowledgments

The authors gratefully acknowledge funding received from the E.ON ERC Foundation (E.ON ERC gGmbH Project No. 04-023). Furthermore, they would like to thank the three anonymous referees, Anke Weidlich, and participants of the conference “Energieinformatik 2012” in Oldenburg for the helpful comments.

## Appendix A. Literature overview

Table 2  
Overview of literature with related auction mechanisms

<table><tr><td>Reference</td><td>Method</td><td>Type of auction</td><td>Major finding</td><td>Comments</td></tr><tr><td>Ausubel and Cramton [4]</td><td>Mathematical proofs</td><td>Multi-unit auction with discriminatory and uniform pricing</td><td>Bidders have an incentive to understate demand in uniform price auctions with private values.</td><td>-</td></tr><tr><td>Back and Zender [5]</td><td>Theoretical model/ mathematical proofs</td><td>Divisible good auction; sealed-bid uniform pricing vs. discriminatory pricing</td><td>Sellers&#x27; revenue is lower in uniform-price auctions because of self-enforcing collusive strategies (very steep demand curves).</td><td>-</td></tr><tr><td>Bernard et al. [6]</td><td>Laboratory experiments</td><td>Uniform-price auction with last-accepted offer and first-rejected offer pricing</td><td>Group size has a much greater impact on prices and efficiency than auction type.</td><td>Single buyer; two, four or six sellers; reservation price</td></tr><tr><td>Burke and Auslander [9]</td><td>Theoretical/ mathematical proofs</td><td>Divisible good auction with uniform pricing</td><td>Pricing mechanism for automatic real-time electricity pricing</td><td>Residential electricity auction</td></tr><tr><td>Chao and Wilson [10]</td><td>Mathematical proofs</td><td>Uniform price multi-unit auction</td><td>Incentive compatible mechanism by using capacity bids only for reserving capacity and using the marginal energy price for energy called (i.e. the last unit of energy actually needed determines the energy price for all energy called)</td><td>Procurement auction for reserve energy</td></tr><tr><td>Engelbrecht-Wiggans and Kahn [13]</td><td>Theoretical model/ mathematical proofs</td><td>Multi-unit auction with uniform pricing</td><td>Equilibria in uniform price auctions</td><td>-</td></tr></table>

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

C. Rosen, R. Madlener / Decision Support Systems xxx (2013) xxx–xxx

Table 2 (continued)

<table><tr><td>Reference</td><td>Method</td><td>Type of auction</td><td>Major finding</td><td>Comments</td></tr><tr><td>Haghighat et al. [17]</td><td>Mathematical model/proofs and simulations</td><td>Discriminatory and uniform pricing multi-unit auction</td><td>Theoretically, no difference between both designs concerning profits, market clearing price and bidding strategies; with transmission constraints, profits are influenced by the pricing mechanism.</td><td>-</td></tr><tr><td>Hao [19]</td><td>Mathematical model and numerical examples</td><td>Multi-unit auction with fixed MWh blocks and one-part price bids</td><td>No true cost bidding under uniform pricing.</td><td>Electricity auction</td></tr><tr><td>Hudson [20]</td><td>Comprehensive market simulation of energy and ancillary services markets</td><td>Multi-unit auction with uniform and discriminatory pricing</td><td>Discriminatory pricing limits market power in periods of high demand through higher price visibility</td><td>Energy and ancillary services markets</td></tr><tr><td>Rassenti et al. [24]</td><td>Laboratory experiment</td><td>Multi-unit procurement auction with uniform and discriminatory pricing</td><td>Discriminatory pricing raises prices and bidders submit higher offer curves; price variance is lower; discriminatory pricing leads to “tacit collusion”, bidders coordinate on the highest observed offers of the previous round.</td><td>Electricity trading with simulation of typical trading days</td></tr><tr><td>Swider and Weber [31]</td><td>Theoretical model and empirical application in MATLAB</td><td>Multi-unit auction with discriminatory pricing</td><td>Estimation of the profit-maximizing bid in a discriminatory auction by deriving the probability of acceptance</td><td>Procurement auction for power systems reserve</td></tr><tr><td>Wang and Zender [34]</td><td>Theoretical model/mathematical proofs</td><td>Divisible good auction (uniform and discriminatory pricing, symmetric and asymmetric information, risk-neutral and risk-averse bidders)</td><td>There is a continuum of equilibria, but with a reserve price of zero, it can be reduced to only one; for risk-averse symmetric bidders, the auctioneer&#x27;s revenue in a discriminatory auction is strictly greater than in a uniform-price auction; only risk-neutral bidders submit completely flat bid schedules; in divisible good auctions there is almost always some degree of demand reduction; auctioneer&#x27;s revenue is strictly increasing in the precision of public information.</td><td>-</td></tr></table>

## Appendix B. MATLAB code for the pricing function when detailed information is available

```matlab
function bid_price = flatAndConstProfit(BID, transferred_q)
    % Function bid_price
    % Determines the price of a bid in case full information is provided
    % Parameters: BID: Instance of Bidder Class
    % transferred_q: argument of pricing function
    % Author: Christiane Rosen
    % Date: 05.07.2012
    % Revision: 10.08.2012
    theoretical_Profit = BID.stored_Target_Bid(1,1) - BID.cost_Function(1,BID.costfactor_a0, BID.costfactor_a1,BID.costfactor_a2,BID.costfactor_b,BID.stored_Target_Bid(1,2));
    theoretical_Profit = BID.discount_Factor* theoretical_Profit* BID.stored_Target_Bid(1,2);
    if (transferred_q < BID.stored_Target_Bid(1,2))
    bid_price = BID.discount_Factor* BID.stored_Target_Bid(1,1);
    else
    bid_price = theoretical_Profit./(transferred_q) + BID.cost_Function(1,BID.costfactor_a0, BID.costfactor_a1,BID.costfactor_a2,BID.costfactor_b,transferred_q);
    end
    if (bid_price > BID.reserve_price)
    bid_price = BID.reserve_price;
    end
    if (bid_price < BID.cost_Function(1,BID.costfactor_a0,BID.costfactor_a1,BID.costfactor_a2, BID.costfactor_b,transferred_q))
    bid_price = BID.cost_Function(1,BID.costfactor_a0,BID.costfactor_a1,BID.costfactor_a2, BID.costfactor_b,transferred_q);
    end
end
```

Please cite this article as: C. Rosen, R. Madlener, An auction design for local reserve energy markets, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2013.05.022

## References

[1] Bundesgesetzblatt Jahrgang 2012 Teil INr. 33. Gesetz zur Änderung des Kraft-Wärme-Kopplungsgesetzes vom 12. Juli 2012, ausgegeben zu Bonn am 18. Juli 2012.

[2] Bundesgesetzblatt Jahrgang 2008 Teil I Nr. 49. Gesetz zur Förderung der Kraft-Wärme-Kopplung vom 25. Oktober 2008, ausgegeben zu Bonn am 31. Oktober 2008.

[3] L.M. Ausubel, An ef<sup>fi</sup>cient ascending-bid auction for multiple objects, The American Economic Review 94 (5) (2004) 1452–1475.

[4] L.M. Ausubel, P. Cramton, Demand reduction and inef<sup>fi</sup>ciency in multi-unit auctions, University of Maryland Working Paper, 96-07, 2002.

[5] K. Back, J.F. Zender, Auctions of divisible goods: on the rationale for the treasury experiment, The Review of Financial Studies 6 (4) (1993) 733–764.

[6] J.C. Bernard, T. Mount, W. Schulze, Alternative auction institutions for electric power markets, Agricultural and Resource Economics Review 27 (2) (1998) 125–131.

[7] C. Block, D. Neumann, C. Weinhardt, A market mechanism for energy allocation in micro-CHP grids, Proceedings of the 41th Hawaii Conference on System Sciences, 21, 2007.

[8] J. Bower, D. Bunn, Experimental analysis of the ef<sup>fi</sup>ciency of uniform-price versus discriminatory auctions in the England and Wales electricity market, Journal of Economic Dynamics and Control 25 (3–4) (2001) 561–592.

[9] W.J. Burke, D.M. Auslander, Residential electricity auction with uniform pricing and cost constraints, North American Power Symposium, 4–6 October 2009, 2009.

[10] H.-P. Chao, R. Wilson, Multi-dimensional procurement auctions for power reserves: robust incentive-compatible scoring and settlement rules, Journal of Regulatory Economics 22 (2) (2002) 161–183.

[11] J. Contreras, O. Candilles, J.I. de la Fuente, T. Gomez, Auction design in day-ahead electricity markets, IEEE Transactions on Power Systems 16 (3) (2001) 409–417.

[12] Council, Council Directive 90/531/EEC of 17 September 1990 on the procurement procedures of entities operating in the water, energy, transport and telecommunications sectors, Of<sup>fi</sup>cial Journal of the European Communities L 297 (10/29/1990) 1–48.

[13] R. Engelbrecht-Wiggans, C.M. Kahn, Multi-unit auctions with uniform prices, Economic Theory 12 (2) (1998) 227–258.

[14] I. Erev, A.E. Roth, Predicting how people play games: reinforcement learning in experimental games with unique, mixed strategy equilibria, The American Economic Review 88 (4) (1998) 848–881.

[15] Council European Parliament, Directive 2004/8/EC of the European Parliament and of the Council of 11 February 2004 on the promotion of cogeneration based on a useful heat demand in the internal energy market and amending Directive 92/42/EEC, Official Journal of the European Union L 52 (02/21/2004) 50–60.

[16] Union for the Co-ordination of Transmission of Electricity, Operation Handbook, 2004.

[17] H. Haghighat, H. Sei<sup>fi</sup>, A.R. Kian, The role of market pricing mechanism under imperfect competition, Decision Support Systems 45 (2) (2008) 267–277.

[18] A. Hailu, S. Schilizzi, Are auctions more ef<sup>fi</sup>cient than <sup>fi</sup>xed price schemes when bidders learn? Australian Journal of Management 29 (2) (2004) 147–168.

[19] S. Hao, A study of basic bidding strategy in clearing pricing auctions, IEEE Transactions on Power Systems 15 (3) (2000) 975–980.

[20] R. Hudson, Analysis of uniform and discriminatory price auctions in restructured electricity markets, Oak Ridge National Laboratory, Oak Ridge, TN, 2000.

[21] A. Martini, L. Pellegrini, M.V. Cazzol, A. Garzillo, M. Innorta, A simulation tool for short term electricity markets, 22nd IEEE Power Engineering Society International Conference on Power Industry Computer Applications, 2001.

[22] I. Otero-Novas, C. Meseguer, C. Batlle, J.J. Alba, A simulation model for a competitive generation market, IEEE Transactions on Power Systems 15 (1) (2000) 250-256

[23] I. Praca, C. Ramos, Z. Vale, M. Cordeiro, Mascem: a multiagent system that simulates competitive electricity markets, IEEE Intelligent Systems 18 (6) (2003) 54–60.

[24] S.J. Rassenti, V.L. Smith, B.J. Wilson, Discriminatory price auctions in electricity markets: low volatility at the expense of high price levels, Journal of Regulatory Economics 23 (2) (2003) 109–123.

[25] D. Ray, E. Cashman, Operational risks, bidding strategies and information policies in restructured power markets, Decision Support Systems 24 (3–4) (1999) 175–182.

[26] D.J. Ray, Electric power industry restructuring in Australia: lessons from down-under, The National Regulatory Research Institute, Occasional Paper, 20, Jan., 1997.

[27] A.E. Roth, I. Erev, Learning in extensive-form games: experimental data and simple dynamic models in the intermediate term, Games and Economic Behavior 8 (1) (1995) 164–212.

[28] R. Selten, R. Stoecker, End behavior in sequences of <sup>fi</sup>nite prisoner's dilemma supergames: a learning theory approach, Journal of Economic Behavior & Organisation 7 (1) (1986) 47–70.

[29] F. Sensfuß, M. Ragwitz, M. Genoese, D. Möst, Agent-based simulation of electricity markets: a literature review, Working paper sustainability and innovation, S5/2007, 2007.

[30] H. Singh, Auctions for ancillary services, Decision Support Systems 24 (3–4) (1999) 183–191.

[31] D.J. Swider, C. Weber, Bidding under price uncertainty in multi-unit pay-as-bid procurement auctions for power systems reserve, European Journal of Operational Research 181 (3) (2007) 1297–1308.

[32] Z. Vale, T. Pinto, I. Praca, H. Morais, MASCEM: electricity markets simulation with strategic agents, IEEE Intelligent Systems 26 (2) (2009) 9–17.

[33] M. Ventosa, A. Baillo, A. Ramos, M. Rivier, Electricity market modeling trends, Energy Policy 33 (7) (2005) 897–913

[34] J.J.D. Wang, J.F. Zender, Auctioning divisible goods, Economic Theory 19 (4) (2002) 673–705.

[35] A. Weidlich, D. Veit, A critical survey of agent-based wholesale electricity market models, Energy Economics 30 (4) (2008) 1728–1759.

[36] R. Wilson, Auctions of shares, Quarterly Journal of Economics 93 (4) (1979) 675–689.

[37] R. Wilson, Activity rules for a power exchange, Power Conference, Berkeley, 1997

C. Rosen is a Ph.D. candidate at the Institute for Future Energy Consumer Needs and Behavior at RWTH Aachen, Germany. She received the B.Sc. degree in Economics in 2008, and the M.Sc. degree in Infonomics in 2009 from Maastricht University, The Netherlands. Her research focuses on auction design and energy markets, thereof especially ancillary services markets, using theoretical approaches and experimental methodologies.

R. Madlener is one of <sup>fi</sup>ve full professors at the E.ON Energy Research Center, established at RWTH Aachen University, Germany, at the end of 2006, and is the director of the Institute for Future Energy Consumer Needs and Behavior. He studied commerce and <sup>fi</sup>nance as well as paedagogics at the Vienna University of Economics and Business Administration (WU Wien) and then also Economics at the Institute for Advanced Studies Vienna (IHS). He received his doctoral degree from WU Wien in the economics and social sciences (Dr, rer, soc, oec.), specializing in General Econom: ics. Environmental Economics, and Statistics. Before taking up his position at RWTH Aachen University in 2007, he was the managing director of the Institute for Advanced Studies Carinthia (1999–2000), assistant professor at the Centre for Energy Policy and Economics (CEPE), ETH Zurich (2001–2007), lecturer at the Faculty of Economics, University of Zurich (as of 2003), and senior researcher at the German Institute of Economic Research/DIW Berlin (2007).
