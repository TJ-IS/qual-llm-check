---
otero_id: 20911
otero_key: "MT8A9N2K"
title: "Analysis of power pools in the deregulated energy market through simulation"
authors: "Simo Makkonen; Risto Lahdelma"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00106-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysis of power pools in the deregulated energy market through simulation

Simo Makkonen <sup>a,)</sup>, Risto Lahdelma

<sup>a</sup> Process Vision Ltd., Melkonkatu 18, 00210 Helsinki, Finland b Technical Research Centre of Finland, P.O. Box 1606, FIN-02044 VTT, Finland

## Abstract

The electricity market has changed rapidly in the Northern European countries. Harmonisation of the legislation and trading methods widens the market area outside national limits. Vertical integration among electricity companies is changing the traditional structure of the inner market. Successful business in this new, more volatile market requires sophisticated techniques for identifying new market opportunities and managing the increased risks.

We study the new market from the perspectives of regional distributors and power pools. We analyse the trading possibilities and profitability of different kinds of power pools, when a spot market and several new contract structures are available along with existing capacity-based long-term contracts. Different policies for allocating the common benefits of a power pool among its members are compared and a new booking algorithm for balance settlement is introduced.

To analyse the operation of different kinds of pools, we use simulation and optimisation techniques. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Deregulated energy market; Energy management; Optimisation; Simulation

## 1. Introduction

The electricity market in the Northern European countries, Finland, Sweden and Norway, has encountered a fundamental change since the beginning of the 1990s. The previously regulated and monopolistic electricity industry has been deregulated and a free electricity market has been created through legislative actions. The Finnish electricity market was deregulated by the Electricity Market Act, which has been in effect as of 1st June 1995 4 . The Act<sup>w</sup> <sup>x</sup> includes prerequisites for competition in power generation, foreign trade, and power sales, so that the electricity market can function efficiently. It also establishes clear rules for the grid business, which operates in a position of a natural monopoly. The business areas open to competition now have a separate accounting from those in a monopoly position. In August 1996, EL-EX, the Finnish electricity spot market, was invoked to serve large electricity producers, distributors, and industrial consumers. Competition has already resulted in dramatically lower energy prices on the spot market.

The electricity grid forms a marketplace where buyers and sellers meet. The grid companies or business units do not participate in power trading; power transmission and sales have been completely separated. Transfer services in the national main grid owned and operated by Fingrid, the national grid company, are based on the principle of point pricing. Regional distribution network operators must provide fairly and within the local network equallyŽ . priced services to all customers. A customer connected anywhere to the grid has thus the right to use the entire Finnish grid from the main grid to the distribution network. A single contract gives access to all grid services.

Similar changes have been introduced in Sweden and Norway with the objective to later create a common Nordic electricity market, which makes it possible to buy and sell electricity in any Nordic country. There are also plans to combine the Swedish–Norwegian spot market Nord Pool 13<sup>w</sup> <sup>x</sup> with EL-EX. Several actors operate already in both EL-EX and Nord Pool causing Finnish and Swedish–Norwegian spot price curves to almost coincide.

Deregulation along with more sophisticated metering and accounting technologies makes way for various new types of electricity contracts and derivatives. New contract types and the lowered price level have serious effects on old capacity-based long-term contracts that are thus currently highly over-priced. While most of the old long-term contracts expire by year 2000, they are gradually being replaced with new energy-based contracts, short-term contracts, and spot market trade. During the transition phase, the actors have the challenging problem of managing very complex portfolios of new and old contracts.

Deregulation opens new possibilities for co-operation between electricity market actors. Different kinds of coalitions or pools can more efficiently utilise the various types of trading possibilities than individual companies. During the last few years, several pools have indeed been formed in Finland. The market structure transition is depicted in Fig. 1.

![](/api/attachments/MT8A9N2K/fulltext/images/fdaa5f9ce7636e2ea6e66c8b56d51dee7fd995b786aa7d4fe90f5dba7a73269b.jpg)  
Fig. 1. The traditional and new market structure.

In this paper, we discuss why and how power pools are formed, and analyse the management of different types of pools with and without access to spot market instruments. We apply a simulation model for long-term market analysis. The model is based on the commercial EHTO energy optimisation software that is reported in Ref. 9 . We use the<sup>w</sup> <sup>x</sup> simulation model to compute the benefits of different types of pools and to compare different policies for sharing the benefits among pool members. We also introduce a balance booking algorithm to allocate the pool benefits on an hourly basis, overcoming thus the traditional problems of allocation. Simulation data is based on a real-life example.

## 2. Old and new contracts and financial instruments

## 2.1. Old contracts in a new world

Up to deregulation of the electricity market, the basic type of contracts in Finland has been the open long-term multi-tariff contract with capacity limits and separate capacity and energy fees. The duration of long-term contracts is typically from one to several years. The cost function $C ( p )$ of open multitariff contracts is modelled as

$$
C (p) = c _ {0} + \sum_ {k = 1} ^ {K} \left(c _ {k} ^ {\max} p _ {k} ^ {\max} + \sum_ {t \in T} c _ {k} ^ {\mathrm{t}} p _ {k} ^ {t}\right),\tag{1}
$$

$$
\begin{array}{l l} 0 \leq p ^ {t} \leq \sum_ {k = 1} ^ {K} p _ {k} ^ {t} & \forall t \in T, \\ 0 \leq p _ {k} ^ {t} \leq p _ {k} ^ {\max} & k = 1, \ldots , K, \quad \forall t \in T, \end{array}
$$

where $p = \left[ p ^ { t } \right]$ is the vector of hourly power traded through the contract, T is the set of hours for the duration of the contract, $p _ { k } ^ { t }$ is the partition of $p ^ { t }$ into tariff components, $c _ { 0 }$ is the fixed contract fee, $c _ { k } ^ { \operatorname* { m a x } }$ is the capacity fee of tariff component $k$ and $\boldsymbol { c } _ { k } ^ { t }$ is the hourly energy fee. The energy fee typically varies according to a few time zones such as day<sup>r</sup>night and winter<sup>r</sup>summer. The seller sets the fees, which may depend on official indices fuel Ž prices, currency rates, etc . The buyer may then . choose the power limits $p _ { k } ^ { \mathrm { m a x } }$ optimally based on estimated load, own production capacity, and other contracts. After the contract is made, the fees and power limits cannot under normal circumstances be modified. Multi-tariff contracts may also contain energy constraints so-called energy packages for tar- Ž . iff components

$$
\sum_ {t \in T} p _ {k} ^ {t} \geq E _ {k},\tag{2}
$$

whereby a small discount is granted for the energy $E _ { k }$

Another common and simple contract type is a fixed or adjustable bilateral contract with a fixed contract fee $c _ { 0 }$ and an hourly energy fee $\boldsymbol { c } _ { k } ^ { t }$ that typically varies according to day<sup>r</sup>night time zones. In the fixed contract, the maximum amount $p ^ { \mathrm { m a x } }$ is traded each hour, whereas in the adjustable contract the buyer must specify the amount to buy between zero and the maximum at least 1 h before delivery. Bilateral contracts are often short- or medium-term contracts, where the duration is typically from 1 week to 1 year. These contracts may also cover non-consecutive hours, for example, only day or night hours. The bilateral contracts are modelled as

$$
\begin{array}{l} C (p) = c _ {0} + \sum_ {t \in T} c ^ {t} p ^ {t}, \\ \text { s.t. } \\ p ^ {t} = p ^ {\max} \quad \forall t \in T (\text { fixed }) \\ \text { or } \\ 0 \leq p ^ {t} \leq p ^ {\max} \quad \forall t \in T (\text { adjustable }). \end{array}\tag{3}
$$

The energy traded through open contracts is resolved afterwards in monthly balance settlements according to predetermined rules using the merit ordering principle 1 . Fixed and adjustable compo-<sup>w</sup> <sup>x</sup> nents, spot market trade, and the measured own production are first subtracted from the hourly demand. The residual demand is then satisfied using open tariff components in order of increasing energy price. Whatever the residual is, it will be supplied through the open contract, but significant penalties follow, if the capacity limits are exceeded.

Management of the traditional electricity purchase and sales contract portfolio has been fairly straightforward, because the number of different contracts and contract types has been small. Optimisation of the capacity limits of traditional contracts based on an overall energy planning model and demand forecasts is a computationally expensive, but in principle well understood problem. Traditional contracts have earlier also been fairly risk-free both to the seller and buyer e.g. distributor . The capacity fees have pro- Ž . vided secure earnings covering the fixed costs of the seller, regardless the amount of actually delivered energy. The energy fees have covered the variable costs. The buyer, on the other hand, knows a priori how much the energy costs, and may plan for each hour how much energy to buy, within the agreed capacity limits. Even if the contract is overpriced, a distributor can in a monopolistic market forward the acquisition costs to the end-users with a similar contract structure of fixed and variable costs.

The opening of the deregulated market has changed the situation dramatically. The Nordic spot market price, which acts as a reference price for new contracts, has on average dropped below the energy fees of the old long-term contracts and even below the variable production costs of most plant types save for hydro and nuclear power. A variety of new short-and medium-term contract types are suddenly available at very competitive prices. While the distributors are stuck with their old, over-priced longterm contracts, they are, under the threat of losing their customers to competing distributors, forced to lower their sales prices to a competitive level. While paying capacity fees of old long-term contracts until they gradually expire around the end of year 2000, the distributors must now actively participate to short-term and spot trade in order to reduce their acquisition costs.

Contract management during the transition phase is particularly difficult, because the contract portfolio contains both old and new contracts along with other types of market instruments. Furthermore, the different contract types do not necessarily fit well together. In particular, due to the greater volatility of the free market, optimisation of the contract portfolio requires now more advanced risk analytical techniques and understanding of various financial instruments.

## 2.2. New short- to medium-term contracts

In a competitive market, contract structures must reflect the hourly variation in the electricity price and demand more accurately than in a monopolistic and regulated market. There is typically no capacity fee in these contracts. The energy fee $c ^ { t }$ varies typically from hour to hour, according to, e.g. the actual spot market price, the marginal production cost, or a forecast of either. Furthermore, the power limit $p ^ { \operatorname* { m a x } } ( t )$ may also be subject to hourly variation according to, e.g., the operation of combined heat and power generation CHP plants. Such dynami- Ž . cally priced and constrained contracts may be either fixed or adjustable, and they are modelled as

$$
\begin{array}{l} C (p) = c _ {0} + \sum_ {t \in T} c ^ {t} p ^ {t}, \\ \text {s.t.} \\ p ^ {t} = p ^ {\max} (t) \qquad \forall t \in T (\text {fixed}) \\ \text {or} \\ 0 \leq p ^ {t} \leq p ^ {\max} (t) \qquad \forall t \in T (\text {adjustable}). \end{array}\tag{4}
$$

These kinds of dynamic contracts are sensitive to the volatile market, and they may include considerable risks to the buyer.

## 2.3. The spot and futures markets

Deregulation of the electricity market and opening of a common Northern European energy market has generated a new set of instruments that can replace existing contract structures or can be used in combination with old contract types for minimising the energy procurement costs and hedging risks. In particular, the Finnish EL-EX and the Swedish– Norwegian Nord Pool spot markets have made it possible for actors to react rapidly to changes in the marginal electricity price.

EL-EX, the Finnish electricity spot market, is a fully automated, transaction-based forward market similar to a stock exchange. The basic commodity is a fixed forward contract for 1 MW h of electricity for a particular hour. Members of EL-EX enter their bids and asks anonymously for stipulated amount and price. It is thus possible to enter bids and asks to specify an arbitrary load-cost-curve. Alternatively, it is possible to accept any amount of existing offers at the offered price. It is also possible to withdraw unaccepted offers from EL-EX, or to modify them. Currently, the spot market is open during weekdays, and the trade for hourly forwards is open for 1 week Ž . 168 h ahead. Trade for a particular hour is closed 2 h prior to delivery.

Other commodities in EL-EX are formed as aggregates of the hourly forward contracts. 24 h form a basic day, hours 7–22 a day, and hours 22–7 a night. These are aggregated into week forwards, and the week forwards further into 4-week blocks. Week blocks form winter and summer season forwards.

Nord Pool, the Nordic Power Exchange established in 1993, was the world’s first international commodity exchange for electrical power. ELSPOT is the spot market of Nord Pool for physical delivery of electrical power for an hour. ELSPOT is based on auction trading and simultaneous price fixing. Participants enter their sales and purchase offers by telephone or, since the autumn of 1996, electronically. Offers are entered on a daily basis for delivery the next day. Different market areas are formed to handle limited transmission capacity between geographical areas. The price calculation is based on the balance price between the supply and demand for all participants in the different areas, considering the transmission limits. An hourly single price is thus applied in all trades in a market area 13 .<sup>w</sup> <sup>x</sup>

ELTERMIN is the financial futures market of Nord Pool. The ELTERMIN offers participants an instrument for price hedging and risk management. There is no physical delivery when the contracts fall due for delivery. The power exchange settles the contracts day by day at the spot market’s system price. In a daily mark to market settlement, the portfolio value is calculated based on the contracts’ market value and changes in value settled between buyers and sellers 12 .<sup>w</sup> <sup>x</sup>

There are plans to combine EL-EX and Nord Pool in the near future. The new EL-EX<sup>r</sup>Nord Pool will offer a wide range of instruments for the future and spot market. One scenario is to adopt the EL-EX convention for spot market trade and ELTERMIN from Nord Pool as a short- to long-term futures market.

## 3. Power pools

## 3.1. Who needs pools and why?

Pools can be classified according to member type.

v Producers’ pools can optimise members’ production centrally and thus avoid, for example, unnecessary start-ups and shutdowns. This is particularly useful in the presence of a spot market, because price co-ordination does not result in optimal unit commitment.

v Consumers’ pools can benefit from the economy of scale, the diversity of load curves, increased market power, and centralised demand side management.

v Distributors’ pools can in fact combine benefits from producers’ and consumers’ pools.

As discussed previously, actors in the free electricity market face a number of problems, such as:

v maintaining competitiveness while stuck with old and over-expensive long-term contracts,

v understanding and utilising the new contract types and financial instruments,

v managing the exceedingly versatile and complex contract portfolios with old and new instruments, and

v handling the increased risks in a more volatile market.

Most of the above problems are particularly difficult for small distributors. Because small distributors also suffer from small resources for investments and lack economies of scale, there are strong reasons why they could benefit from forming various kinds of coalitions or pools. Several different strategies and operation modes are available. To analyse the distributors’ pools we classify them as follows.

v Long-term supply pool. Regional distributors sum their load curves together and combine their long-term power procurement to get a better negotiation position towards the power producers and traders. They also benefit from the diversity of their load curves, which may result in significantly lower tariff limits and thus lower priced long-term contracts.

v Short-term supply pool. The pool manages short-term supply for its members. A short-term supply pool may also include the functionality of a long-term supply pool, in particular, if a long-term supply pool has evolved to incorporate short term trading.

v Spot market pool. This pool type extends the functions of short-and long-term pools with spot market and futures transactions. Spot market pools are formed because small regional energy distributors do not possess enough resources to build an organisation for active power trading. The fixed costs for entering the spot market about 0.5 millionŽ FIM<sup>r</sup>year may also exceed the expected profits. from spot trade for individual small companies.

v Trade pool. This is a spot market pool with an active trading role. While the spot market pool operates mainly within the supply and demand of its members, trade pools may seek profits from active speculative operations in the short-term and spot markets. The volume of operations in a trade pool may thus exceed that of its members.

## 3.2. Maximising the profit of a pool

In the new market environment, decision making cannot anymore be entirely based on cost optimisation of acquisition through contracts and own production or, in the long term, on optimisation capacity limits of long-term contracts. The new problem is an intractable dynamic, combinatorial multi-criteria decision problem under uncertainties. In addition to maximising the overall profits, the pool should also try to minimise the risks. To avoid the combinatorial nature of the problem, operations must in practice be based on opportunistic greedy decision strategies.Ž . Risk analysis can be based on simulation techniques using different scenarios. Risk hedging using financial derivatives and other available instruments is becoming an essential part of the daily decision making. In this process, new tools and methods are needed to manage the financial market along with physical supply and demand control.

In medium- and short-term trade, given a certain scenario, greedy profit maximisation can be based on a dynamic planning model maximising the expected profits of the pool with respect to only one or a few new trade instruments at a time. When multiple scenarios are included to the planning model, the potential risks can be estimated. The trades can then be constrained so that a predetermined risk level is not exceeded. Alternatively, various derivatives can be used to hedge the risks.

In spot market trade, the risks are generally much smaller, and the optimisation problem is thus simpler. In particular, when the spot market is used for making fairly small adjustments to the hourly supply and demand, the pool can act as a completely risk neutral decision-maker.

The same planning and optimisation methods can be used for a pool as for independent market actors if the following conditions holds:

v Forecasts are available from all members.

v Pool members inform the pool of all contracts made.

v Pool members are not allowed to make their own trading simultaneously with the pool.

Some methods that can be utilised in short- and long-term planning are described in Refs. 2,6,7, <sup>w</sup> 11,14 .<sup>x</sup>

## 3.3. Allocation of the benefits of the pool

The primary purpose of a pool is to maximise the overall benefits of pool members. While this goal can be reached, under the assumptions listed in the previous section, by similar methods that an independent market actor would use, a more ambiguous problem is that of allocating the common benefits among pool members.

Several kinds of benefit allocation principles for pools have been reported. In Ref. 3 , the allocation <sup>w</sup> <sup>x</sup> of the cost-savings of a power pool is realised by utilising the following principles:

v Split-the-savings

v Pool averaging

v Proportional participation

v Proportional contribution

These methods are valid if the allocation is made between two members and if there are no auxiliary transactions in the pool, i.e. the pool operates only as a common brokerage system for the members. In addition, Ref. 3 utilises a marginal cost-curve as a <sup>w</sup> <sup>x</sup> market signal from a single member towards the pool, which is applicable for a pool of producers, but not in a more general case. Another method presented by Ref. 5 is based on game theory. This<sup>w</sup> <sup>x</sup> method should yield an optimal allocation of benefits if the market has perfect competition conditions.

Regardless of the pool type and profit allocation method, the weak Pareto condition should be valid:Ž . the total profit of a pool is greater than the sum of the profits of the separated pool members, and every pool member should receive a share of these common benefits. Denoting by J the total profit of the pool and by $J _ { j }$ the profit of member j when separated from the pool, the first part means that the pool benefit

$$
\Delta J = J - \sum_ {j} J _ {j}\tag{5}
$$

should be positive. Within the Pareto condition, any allocation of common profits as agreed by the members can be considered equally ‘fair’. The Pareto condition does guarantee the integrity of the pool, making it unprofitable for any member to disjoin, but it does not protect the pool from new members who might cause net losses to the pool as long as the overall common benefits are positive. The latter might happen, e.g. when a new member of a longterm supply pool has a highly coincident load curve with the pool’s existing load, but due to poor load estimates of the newcomer, the tariff limits are set too low. This will cause high additional costs to cover for lacking energy lowering the overall benefits of the pool. As a result, depending on the allocation scheme, the newcomer may obtain considerable benefits while old members’ benefits are lowered.

To create a more sophisticated and fair allocation rule, we compare the performance of the n-member pool with the different sub-pools of n<sup>y</sup>1 members. We denote by $J _ { \bar { j } }$ the expected profit of the pool without member j. The net profit effect of member j to the pool is then

$$
\Delta J _ {j} = J - J _ {\bar {j}},\tag{6}
$$

which should normally not be negative. Applying the n<sup>y</sup>1 principle, the common benefits are then allocated to the members in the proportion of their net profit effects, that is, member j is allocated the benefit

$$
A _ {j} = \frac {\Delta J _ {j}}{\sum_ {j} \Delta J _ {j}} \Delta J.\tag{7}
$$

## 4. A simulation model for power pool analysis

To analyse the performance of a pool, we use a simulation environment that consists of an optimisation model, a balance booking application and a spreadsheet application. The simulation model is based on an upper-level spreadsheet framework where the input values and the optimisation results are presented and the results are compared. In addition, different algorithms for allocating the pool benefits and comparing them are implemented in this framework. Optimisation of the contracts with chosen sets of parameters is done using a separate optimisation package. Similarly, balance booking is analysed with a separate application from which the results are transferred to the simulation framework. A similar kind of modelling approach to analyse the electricity market is presented in Ref. 15 . <sup>w</sup> <sup>x</sup>

## 4.1. Optimisation model

The optimisation model is developed particularly for optimisation of energy procurement in a combined heat and power CHP production system. Ž . Optimisation is based on the Power Simplex algorithm, which solves hourly cogeneration problems efficiently 8 . The dynamic planning model is for- <sup>w</sup> <sup>x</sup> mulated as

$$
\max J (x) = \max \sum_ {i} \pm C _ {i} (x _ {i})
$$

$$
\begin{array}{l} \text {s.t.} \\ \mathbf {G} x \leq \mathbf {g} _ {0} \\ \mathbf {H} x = \mathbf {h} _ {0} \\ x _ {i} \in X _ {i} \end{array}\tag{8}
$$

where $C _ { i } ( x _ { i } )$ Ž . Ž . is the net profit <sup>q</sup> or cost <sup>y</sup> function of subsystem i. The subsystems interact in the energy system through common hourly power and heat balances. The balance constraints are represented by the transmission matrix H and the vector $\pmb { h } _ { o }$ corresponding to demand forecasts. Power reserve constraints can be included into the model similarly by matrix G and vector ${ \pmb g } _ { 0 } .$ . The subsystem specific constraints are represented by the sets $X _ { i } ,$ The method for optimising the tariff limits of capacity based multi-tariff contracts and the long-term energy procurement is described in Ref. 9 .<sup>w</sup> <sup>x</sup>

The algorithm is embedded in the EHTO Optimiser application 10 , which is used by several<sup>w</sup> <sup>x</sup> energy companies and pools in Finland. In this paper, the optimisation model is applied both for optimisation of the pool and its separated members.

## 4.2. Balance booking model

We introduce a booking model for allocating the hourly benefits of a pool to its members. This model overcomes some problems of benefit allocation because the allocation is based on the available contract portfolios of the pool and its members. As hourly spot market prices are available, the allocation reflects the real market situation. In addition, the model satisfies the Pareto conditions and encourages pool members to optimise their purchase contract portfolios, because the hourly profit allocation is based on pool members’ existing contracts.

The model consists of a booking algorithm and a procedure for allocating the pool benefits. The model includes a pool with two contract portfolios as illustrated in Fig. 2. The pool’s purchase contract portfolio PPP includes one multi-tariff contract as de-Ž . fined in Eq. 1 , and bilateral contracts Eq. 3 . TheŽ . Ž Ž .. pool can also trade with the power exchange, which is represented by dynamic contracts of type 4 . OnŽ . the other side of the pool is the pool’s sales contract portfolio PSP , which includes one open purchase Ž . contract for each pool member, and possibly other bilateral contracts. In addition, pool members may have auxiliary purchase contracts with third parties, and the pool must have knowledge about these, because they affect the total load towards the pool.

![](/api/attachments/MT8A9N2K/fulltext/images/1e98eb8d9d46503a4d63133f201c8d518368b9fc750dee97b9985d262dc569ca.jpg)  
Fig. 2. Pool structure.

The pool uses the following procedure for balance settlement and benefit allocation.

## 4.2.1. Phase 1. Pool’s purchase balance settlement

Step 1.1. Make the balance settlement for the supply side based on the total load of the pool. The algorithm books first the fixed and predetermined adjustable contracts, and then the open contracts by the merit order principle.

Next, pool members’ balance booking and simultaneous allocation of pool benefits to members is done as follows.

## 4.2.2. Phase 2. Allocate the traditional contracts

Step 2.1. Book the available fixed contracts, the predetermined adjustable contracts and possible own production of pool members.

Step 2.2. Book the open contracts in merit order. If the load of a pool member exceeds the sum of the fixed and open contracts, book an exceeded power component $p ^ { \mathrm { { e } } }$ Ž . contract penalty .

## 4.2.3. Phase 3. Allocate spot market energy

Step 3.1. To allocate the available spot market energy of the pool, compute the sum $p ^ { \mathrm { f } }$ of all futures ordered by members.

Step 3.2. Substitute the most expensive components of already booked energy using the futures in merit order, if and only if the futures provide a cheaper supply than the primary booking.

Step 3.3. Substitute the most expensive components of already booked energy using available spot market electricity in merit order, if and only if the spot market provides a cheaper supply than the existing booking.

Step 3.4. The pool books any remaining market electricity and covers the losses.

4.2.4. Phase 4: Allocate the diÕersity benefit of the pool

Step 4.1. Find the most expensive unallocated component of the pool and denote that as the reference product $p ^ { \mathrm { r } }$ . Define the reference price $c ^ { \mathrm { r } }$ as the maximum of the spot market price and the price of $p ^ { \mathrm { r } }$

Step 4.2. Iterate through pool members and find the components with the highest price $c ^ { \mathrm { h } }$ . While $c ^ { \mathrm { h } }$ is higher than the price of $p ^ { \mathrm { r } }$ , substitute these components with $p ^ { \mathrm { r } }$ in proportion of energies for price $c ^ { \mathrm { r } } .$

## 4.2.5. Phase 5: Allocate the ‘ passiÕe’ sales reÕenues of the pool

Allocation of passive trading follows a similar procedure as that of allocation of the supply savings. Set the lowest sales component of the pool as the reference component. Sort the available non-booked open contract components of pool members according to price and find if the members have free capacity to a lower price than the reference component. Allocate the possible sales profits to these pool members in proportion of their free capacities. Repeat until the sales capacity of the pool is allocated or no lower priced components remain in pool members’ contract portfolios. The possible remaining profit stays in the pool.

## 4.2.6. Phase 6: Allocate ‘actiÕe’ trading reÕenues

If the pool participates in ‘active’ trading, the allocation of possible trade revenues and losses is not a straightforward task. We discuss the problem only briefly in Section 6.

## 5. Analysing the pool operation

In the following, we analyse through simulation the profitability of three different types of pools, and compare four different methods for allocating the benefits among members.

The first pool type is a long-term supply pool, formed to benefit only from the economies of scale and the diversity of the pool members load curves. The cost savings of the pool are compared with savings for separated members.

Table 1  
Company information

<table><tr><td></td><td>Company A</td><td>Company B</td><td>Company C</td><td>Total</td></tr><tr><td>Energy (GW h)</td><td>811.0</td><td>300.2</td><td>985.3</td><td>2096.4</td></tr><tr><td>Min. capacity (MW)</td><td>22.2</td><td>0.0</td><td>43.9</td><td>68.7</td></tr><tr><td>Max. capacity (MW)</td><td>183.4</td><td>84.5</td><td>219.5</td><td>479.5</td></tr></table>

The second pool type is a short-term supply pool. Fixed bilateral contracts with optimised capacity limits are first inserted into separated pool members supply portfolios. Then the pool optimises the use of similar contracts.

The third pool type is a spot market pool with an exchange market for purchasing electricity available for the pool and its members. In this case, the problem is to allocate the savings of the pool that arise from substitution of more expensive open long-term tariff components with cheaper spot market electricity and to allocate the revenues of this kind of ‘passive trade’.

The different benefit allocation methods we compare in our analysis are:

v split benefits equally among members,

v split benefits in proportion of members’ energy,

v split according to the members net profit effect Ž .based on n<sup>y</sup>1 sub-pool analysis , and

v split benefits using the hourly booking algorithm.

## 5.1. Example system

We consider three regional distribution companies A, B, and C, which are to form a common pool. The

Table 2  
Prices of open long-term multi-tariff contract

<table><tr><td rowspan="3">Tariff components</td><td rowspan="3">Capacity (FIM/MW, month)</td><td colspan="4">Energy fees (FIM/MW h, h)</td></tr><tr><td colspan="2">Winter</td><td colspan="2">Summer</td></tr><tr><td>Day</td><td>Night</td><td>Day</td><td>Night</td></tr><tr><td>Base load</td><td>40000</td><td>107</td><td>97</td><td>98</td><td>97</td></tr><tr><td>Middle load</td><td>21000</td><td>162</td><td>137</td><td>130</td><td>106</td></tr><tr><td>Peak load</td><td>17000</td><td>519</td><td>151</td><td>131</td><td>111</td></tr></table>

Table 3  
Results of the tariff optimisation

<table><tr><td rowspan="2">Tariff component</td><td rowspan="2">Capacity (MW)</td><td colspan="2">Winter (GW h)</td><td colspan="2">Summer (GW h)</td><td rowspan="2">Total (GW h)</td></tr><tr><td>Day</td><td>Night</td><td>Day</td><td>Night</td></tr><tr><td colspan="7">Company A</td></tr><tr><td>Base load</td><td>85.0</td><td>162.4</td><td>317.8</td><td>77.2</td><td>115.6</td><td>673.1</td></tr><tr><td>Middle load</td><td>56.6</td><td>58.1</td><td>72.8</td><td>3.1</td><td>0.7</td><td>134.8</td></tr><tr><td>Peak load</td><td>41.7</td><td>1.0</td><td>2.0</td><td>0.0</td><td>0.0</td><td>3.0</td></tr><tr><td>Total</td><td>183.4</td><td>221.6</td><td>392.6</td><td>80.3</td><td>116.4</td><td>810.9</td></tr><tr><td>Costs [MFIM]</td><td>63.6</td><td>41.1</td><td>27.3</td><td>11.3</td><td>8.0</td><td>151.3</td></tr><tr><td colspan="7">Company B</td></tr><tr><td>Base load</td><td>27.8</td><td>53.2</td><td>100.3</td><td>23.2</td><td>31.3</td><td>207.8</td></tr><tr><td>Middle load</td><td>36.4</td><td>39.4</td><td>47.0</td><td>3.1</td><td>1.6</td><td>91.1</td></tr><tr><td>Peak load</td><td>20.3</td><td>0.6</td><td>0.7</td><td>0.0</td><td>0.0</td><td>1.3</td></tr><tr><td>Total</td><td>84.5</td><td>93.2</td><td>148.0</td><td>26.2</td><td>32.8</td><td>300.2</td></tr><tr><td>Costs [MFIM]</td><td>26.7</td><td>16.3</td><td>12.4</td><td>3.2</td><td>2.7</td><td>61.2</td></tr><tr><td colspan="7">Company C</td></tr><tr><td>Base load</td><td>102.9</td><td>196.6</td><td>388.0</td><td>90.3</td><td>146.7</td><td>821.6</td></tr><tr><td>Middle load</td><td>68.3</td><td>69.7</td><td>89.4</td><td>1.5</td><td>0.4</td><td>160.9</td></tr><tr><td>Peak load</td><td>48.3</td><td>1.1</td><td>1.7</td><td>0.0</td><td>0.0</td><td>2.8</td></tr><tr><td>Total</td><td>219.5</td><td>267.4</td><td>479.0</td><td>91.8</td><td>147.0</td><td>985.3</td></tr><tr><td>Costs [MFIM]</td><td>76.5</td><td>50.1</td><td>32.9</td><td>14.3</td><td>9.0</td><td>182.8</td></tr><tr><td colspan="7">Pool (A+B+C)</td></tr><tr><td>Base load</td><td>218.0</td><td>416.9</td><td>814.3</td><td>193.2</td><td>295.1</td><td>1719.5</td></tr><tr><td>Middle load</td><td>156.3</td><td>182.8</td><td>201.3</td><td>5.1</td><td>1.2</td><td>370.4</td></tr><tr><td>Peak load</td><td>105.3</td><td>2.5</td><td>4.0</td><td>0.0</td><td>0.0</td><td>6.5</td></tr><tr><td>Total</td><td>479.5</td><td>582.1</td><td>1019.6</td><td>198.3</td><td>296.2</td><td>2096.4</td></tr><tr><td>Costs [MFIM]</td><td>165.5</td><td>107.2</td><td>72.3</td><td>28.7</td><td>19.6</td><td>393.3</td></tr><tr><td colspan="7">Pool (B+C)</td></tr><tr><td>Base load</td><td>130.8</td><td>250.0</td><td>489.3</td><td>114.4</td><td>178.9</td><td>1032.7</td></tr><tr><td>Middle load</td><td>103.6</td><td>109.1</td><td>135.5</td><td>3.6</td><td>1.0</td><td>249.2</td></tr><tr><td>Peak load</td><td>64.5</td><td>1.5</td><td>2.2</td><td>0.0</td><td>0.0</td><td>3.6</td></tr><tr><td>Total</td><td>298.9</td><td>360.6</td><td>627.0</td><td>118.0</td><td>179.9</td><td>1285.5</td></tr><tr><td>Costs [MFIM]</td><td>102.0</td><td>66.4</td><td>45.2</td><td>17.5</td><td>11.7</td><td>242.7</td></tr><tr><td colspan="7">Pool (A+C)</td></tr><tr><td>Base load</td><td>189.4</td><td>362.2</td><td>711.0</td><td>168.5</td><td>262.7</td><td>1504.4</td></tr><tr><td>Middle load</td><td>120.6</td><td>124.5</td><td>156.9</td><td>3.6</td><td>0.7</td><td>285.8</td></tr><tr><td>Peak load</td><td>92.8</td><td>2.2</td><td>3.7</td><td>0.0</td><td>0.0</td><td>6.0</td></tr><tr><td>Total</td><td>402.9</td><td>489.0</td><td>871.7</td><td>172.1</td><td>263.4</td><td>1796.2</td></tr><tr><td>Costs [MFIM]</td><td>140.2</td><td>88.2</td><td>56.5</td><td>25.6</td><td>16.9</td><td>327.3</td></tr><tr><td colspan="7">Pool (A+B)</td></tr><tr><td>Base load</td><td>114.0</td><td>218.1</td><td>422.4</td><td>102.2</td><td>148.0</td><td>890.7</td></tr><tr><td>Middle load</td><td>88.8</td><td>94.9</td><td>115.4</td><td>4.4</td><td>1.2</td><td>215.9</td></tr><tr><td>Peak load</td><td>59.1</td><td>1.7</td><td>2.7</td><td>0.0</td><td>0.0</td><td>4.5</td></tr><tr><td>Total</td><td>261.9</td><td>314.7</td><td>540.6</td><td>106.6</td><td>149.2</td><td>1111.1</td></tr><tr><td>Costs [MFIM]</td><td>89.2</td><td>57.2</td><td>39.6</td><td>14.5</td><td>10.6</td><td>211.0</td></tr></table>

annual demand and capacity information of the companies is shown in Table 1.

Table 4  
Overall supply costs for separated companies, pools and sub-pools

<table><tr><td>Pool type</td><td>A</td><td>B</td><td>C</td><td>Sum</td><td>(A + B + C)</td><td>(B + C) + A</td><td>(A + C) + B</td><td>(A + B) + C</td></tr><tr><td>Long-term supply</td><td>151.3</td><td>61.2</td><td>182.8</td><td>395.3</td><td>393.3</td><td>393.9</td><td>395.1</td><td>394.0</td></tr><tr><td>Short-term supply</td><td>150.0</td><td>61.0</td><td>180.9</td><td>391.9</td><td>384.3</td><td>384.9</td><td>386.8</td><td>385.6</td></tr><tr><td>Spot market</td><td>147.5</td><td>60.6</td><td>178.4</td><td>386.5</td><td>377.6</td><td>379.9</td><td>380.7</td><td>380.3</td></tr></table>

B and C have small power production plants, which have been eliminated from the analysis by subtracting their production from the corresponding load curves.

## 5.2. Analysis of the pool

In the analysis, the simulation interval is 1 year Ž . 8760 h . The open long-term multi-tariff contracts with capacity limits Eq. 1 are assumed to be Ž Ž .. similar for all actors with the same prices as presented in Table 2. Both the pool and the members have optimised their capacity limits.

Table 3 presents for each member separately, and for the pool, the optimised capacity limits and the corresponding annual capacity and energy costs. The table also includes data for sub-pools with n<sup>y</sup>1 members.

Table 4 summarises the overall acquisition costs for the separated members and the different types of pools. In addition, the costs for the n <sup>y</sup> 1-member sub-pools added with the costs of the company not included in the pool are shown. The pool benefits are presented in Table 5. Table 6 presents the allocation of the pool benefits according to the different allocation methods. The benefits allocated to A, B and C, respectively, are presented in parenthesis.

Table 5  
Pool benefits for different types of pools and sub-pools

<table><tr><td>Pool type</td><td>(A+B+C)</td><td>(B+C)+A</td><td>(A+C)+B</td><td>(A+B)+C</td></tr><tr><td>Long-term supply</td><td>2.06</td><td>1.28</td><td>0.24</td><td>1.40</td></tr><tr><td>Short-term supply</td><td>7.68</td><td>6.37</td><td>5.14</td><td>7.07</td></tr><tr><td>Spot market</td><td>8.91</td><td>6.16</td><td>5.77</td><td>6.58</td></tr></table>

We observe that allocation of the benefits is not a straightforward task. Company C, for example, receives the largest profit in the proportional allocation in all pool types, but when based on the net profit effect, company B obtains the largest benefit.

The split equally method does not in any way consider how much each member has contributed to the common benefit. Besides being unfair, the more serious problem with this method is that it provides very weak incentives for activating members to increase the common benefits.

Similar arguments hold for the proportion to energy method. Company C, for example, with the largest demand, receives always the largest share of pool’s benefits regardless of its contribution to benefit making. This method could be justified only if no method for assessing individual members’ benefits for the pool exists.

The n<sup>y</sup>1 analysis overcomes the energy domination of A and C, and it makes possible for a small actor such as B to receive a considerable benefit from the pool. Companies A and C have highly coincident load curves, and they do not alone benefit very much from forming a pool. But together with B with a very non-coincident load curve, either one of them or all three together reaches substantial benefits from forming a pool. Thus, we can argue that B should receive a greater share of the pool benefits than its size demand alone would justify. TheŽ . n<sup>y</sup>1 analysis does exactly this.

The hourly booking method yields a similar result in allocation of benefits as the n<sup>y</sup>1 analysis does. In fact, this result seems reasonable, because in the hourly booking method companies A and C with coincident load curves and optimised tariff limits of the long-term contracts cannot benefit from hourly allocation, because they ‘compete’ hourly from the same reference product $p ^ { \mathrm { r } }$ . If they can benefit from $p ^ { \mathrm { r } }$ , the benefit is allocated equally on average because of the similar contract portfolio. On the other hand, company B with a non-coincident load curve can benefit more.

Table 6  
Pool benefit allocations according to different methods

<table><tr><td>Pool type</td><td>Split equally</td><td>Prop. to energy</td><td>n-1 analysis</td><td>Hourly booking</td></tr><tr><td>Long-term supply</td><td>(0.69; 0.69; 0.69)</td><td>(0.80; 0.29; 0.97)</td><td>(0.41; 1.18; 0.49)</td><td>N/A</td></tr><tr><td>Short-term supply</td><td>(2.56; 2.56; 2.56)</td><td>(2.97; 1.10; 3.61)</td><td>(1.05; 4.37; 2.25)</td><td>(1.90; 3.12; 2.66)</td></tr><tr><td>Spot market</td><td>(2.97; 2.97; 2.97)</td><td>(3.40; 1.28; 4.19)</td><td>(2.52; 3.40; 2.98)</td><td>(2.47; 2.83; 2.71)</td></tr></table>

As seen, the n<sup>y</sup>1 analysis provides on average a result similar to that of hourly booking. We have to remind that in the analysis we have only used few contracts, which are similar both to the pool and its members. In addition, the spot market was simulated with a simple model, where we used the same dynamic cost and availability curves for all participants through the simulation period. In the real life, spot market actors affect each other and the price level and availability changes dynamically. Thus, the booking algorithm will be more sensitive to the pool members’ activity than in our analysis.

## 6. Discussion

The new market situation creates a potential need for combining energy procurement and trade operations of small and medium-size energy distributors. As the electricity transmission has remained monopolistic, and cross-subvention is prevented by the market authorities, the supply business has met a new competition. In addition, the new market area, new market instruments and larger contract portfolios require a wide-range knowledge and sophisticated information management that in many cases is difficult to organise in small business units. In this development, the sales companies are about to strengthen their competitiveness by forming pools.

Above we have analysed the operation of different pool types. The analysis is based on real data, but some simplifications and assumptions have been made. We have intentionally overlooked the uncertainties in our analysis, although in real operation the load and price forecasts are not accurate and many other uncertainties exist. Compared to a single actor, a pool is less risk-averse because of the scale, but otherwise the same principles can be applied to risk-management as for a single pool member. We have earlier described some methods for managing uncertainties and short-term risks of energy procurement in Ref. 11 .<sup>w</sup> <sup>x</sup>

One important question arises from the deregulation of the retail trade because the load structure may change crucially, and the accuracy of long-term load forecasts may decrease radically. Under these circumstances, pool operating and benefit allocation principles should be planned well to avoid unnecessary risks. In particular, it should be ensured that the allocation of potential profits and losses is focused to the right members if the load of one pool member collapses rapidly or a member is able to increase its market share substantially.

In Section 5, we analysed the pool when acting as a ‘passive’ trader. But the pool could also operate actively to maximise the trading revenue while ensuring members’ cost-savings in the energy supply. In fact, a power pool operating on the behalf of its members is an ideal organisation for active trading for the following reasons:

v The pool can utilise the common contract portfolio as a basis for trading.

v The pool has a large enough volume to speculate in the market.

v If the pool uses the market price as a reference price in pool benefits allocation, pool members do not gain any additional benefits from independent trading transactions.

v The pool can hedge the risks internally.

But some critical questions can also be asked:

v Is there a risk of cross subvention between trading business and energy supply activity?

v How to cover the risks that arise purely from active trading?

v How to allocate the potential revenues of the trading business?

v Should the pool members participate to pay potential losses, or are the shareholders solely in charge of the losses?

Answering these questions requires detailed knowledge about pool background and deep understanding of the phenomena in exchange market.

## 7. Conclusions

We have analysed different types of power pools using simulation. The analysis shows that a pool can operate more efficiently than a single actor both in supply and the spot market. The allocation of the cost-savings and sales profits is not straightforward. While the allocation must follow predetermined rules that satisfy the Pareto conditions it should also incorporate some notion of ‘fairness’ , along with providing sufficient incentives for the individual members to promote the common benefit. Based on the simulation results, we recommend the net profit effects method Ž . n <sup>y</sup> 1 member sub-pools analysis , or, in case of short-term or spot market pool, the more sophisticated booking algorithm, which reflects pool members’ hourly contract portfolio.

## References

<sup>w</sup> <sup>x</sup> 1 J.B. Bushnell, S.S. Oren, Bidder cost revelation in electric power auctions, Journal of Regulatory Economics 6 1994Ž . 5–26.

<sup>w</sup> <sup>x</sup> 2 U.M. Divekar, E.S. Ribin, Optimal design of advanced power systems under uncertainty, Proc. of the International Symposium of ECOS’96, Efficiency, Cost, Optimization, Simulation and Environmental Aspects of Energy Systems, June 25–27, Stockholm, Sweden, 1996, pp. 389–396.

<sup>w</sup> <sup>x</sup> 3 K.W. Doty, An analysis of electric power brokerage systems, IEEE Transaction on Power Apparatus and Systems PAS-101 Ž . Ž . 2 1982 389–396, February.

4 Energy Market Act, 1995, Ministry of Trade and Industry, Helsinki, Finland.

<sup>w</sup> <sup>x</sup> 5 R.W. Ferrero, Transaction analysis in deregulated power systems using game theory, IEEE Transactions on Power Systems 12 3 1997 1340–1347.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 X. Guan, P. Luh, L. Zhang, Non-linear approximation method in Lagrangian relaxation-based algorithms for hydrothermal scheduling, IEEE Transaction on Power Systems 10 2Ž . Ž . 1995 772–778, May.

<sup>w</sup> <sup>x</sup> 7 M. Kliman, Competitive bidding for independent power, developments in the USA, Energy Policy 1994 41–56,Ž . January.

<sup>w</sup> <sup>x</sup> 8 R. Lahdelma, H. Hakonen, An efficient linear programming algorithm for combined heat and power production, 1998Ž . submitted.

<sup>w</sup> <sup>x</sup> 9 R. Lahdelma, S. Makkonen, Interactive graphical object-oriented energy modelling and optimization, Proc. of the International Symposium of ECOS’ 96, Efficiency, Cost, Optimization, Simulation and Environmental Aspects of Energy Systems, June 25–27, Stockholm, Sweden, 1996, pp. 425– 431.

<sup>w</sup> <sup>x</sup> 10 S. Makkonen, R. Lahdelma, A concept for simulation and optimization of the energy trade, The International Conference: Simulation, Gaming, Training and Business Process Re-engineering in Operations, Riga, Latvian, September 19– 21, 1996.

<sup>w</sup> <sup>x</sup> 11 S. Makkonen, R. Lahdelma, Stochastic simulation in risk analysis of energy trade, Trends in Multicriteria Decision Making: Proceedings of the 13th International Conference on Multiple Criteria Decision Making, Cape Town, 1998, pp. 147–156.

<sup>w</sup> <sup>x</sup> 12 Nord Pool — The Futures Market, Report, October 30th, 1997 available at www.nordpool.no .Ž .

<sup>w</sup> <sup>x</sup> 13 Nord Pool — The Spot Market, Report, October 15th, 1997 Ž . available at www.nordpool.no .

<sup>w</sup> <sup>x</sup> 14 P.J. Spinney, G.C. Watkins, Monte Carlo simulation technique and electric utility resource decisions, Energy Policy 24 2 1996 155–164, February.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 K. Vlahos, P. Ninios, D. Bunn, An interactive modelling approach for understanding competitive electricity markets, Journal of the Operational Research Society 49 3 1998Ž . Ž . 187–199, March.

![](/api/attachments/MT8A9N2K/fulltext/images/4d4e93035cae54d8a76505b93fdf65d94c17334e37cc7445c5fa31e51d39fb03.jpg)  
MSc Simo Makkonen born 1966 re-Ž . ceived his MSc in Systems and Operations Research in 1990 at Helsinki University of Technology. He is currently the Managing Director of Process Vision. His research interests include systems analysis, energy trade modelling and international financing.

![](/api/attachments/MT8A9N2K/fulltext/images/cf8e0b3f9df33dc95260e7e573ff6c8e717f2a2b631a0d51df9fbe1c03dce557.jpg)

Dr. Risto Lahdelma was born in Helsinki, Finland, in 1961. He is currently Research Professor of Energy Markets at the Technical Research Centre of Finland, Docent of Artificial Intelligence and Mathematical Modelling at Helsinki University of Technology, and Docent of Systems and Operations Research at University of Jyvaskyla.¨ ¨
