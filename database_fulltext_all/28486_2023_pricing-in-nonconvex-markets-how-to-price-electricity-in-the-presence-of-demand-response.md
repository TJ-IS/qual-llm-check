---
otero_id: 28486
otero_key: "993CDZD6"
title: "Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response"
authors: "Martin Bichler; Johannes Knörr; Felipe Maldonado"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1139"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response

Martin Bichler,<sup>a,</sup>\* Johannes Knorr,¨ <sup>a</sup> Felipe Maldonado<sup>b</sup>

<sup>a</sup> Department of Computer Science, Technical University of Munich, 85748 Munich, Germany; <sup>b</sup> Department of Mathematical Sciences, University of Essex, Colchester CO4 3SQ, United Kingdom \*Corresponding author

Contact: bichler@in.tum.de, https://orcid.org/0000-0001-5491-2935 (MB); knoerr@in.tum.de, https://orcid.org/0000-0003-0952-2633 (JK); felipe.maldonado@essex.ac.uk, https://orcid.org/0000-0001-8272-5192 (FM)

Received: May 20, 2021 Revised: November 23, 2021; April 5, 2022 Accepted: April 17, 2022 Published Online in Articles in Advance: July 8, 2022

https://doi.org/10.1287/isre.2022.1139

Copyright: © 2022 INFORMS

Abstract. A Walrasian competitive equilibrium de<sup>fi</sup>nes a set of linear and anonymous prices where no coalition of market participants wants to deviate. Walrasian prices do not exist in nonconvex markets in general, with electricity markets as an important real-world example. However, the availability of linear and anonymous prices is important for derivatives markets and as a signal for scarcity. Prior literature on electricity markets assumed price-inelastic demand and introduced numerous heuristics to compute linear and anonymous prices on electricity markets. At these prices, market participants often make a loss. As a result, market operators provide out-of-market side-payments (so-called make-whole payments) to cover these losses. Make-whole payments dilute public price signals and are a signi<sup>fi</sup>cant concern in electricity markets. Moreover, demand-side <sup>fl</sup>exibility becomes increasingly important with growing levels of renewable energy sources. Demand response implies that different <sup>fl</sup>exibility options come at different prices, and the proportion of price-sensitive demand that actively bids on power exchanges will further increase. We show that with price-inelastic demand there are simple pricing schemes that are individually rational (participants do not make a loss), clear the market, support an ef<sup>fi</sup>cient solution, and do not require make-whole payments. With the advent of demand-side bids, budget balanced prices (no subsidies are necessary) cannot exist anymore, and we propose a pricing rule that minimizes make-whole payments. We describe design desiderata that different pricing schemes satisfy and report results of experiments that evaluate the level of subsidies required for linear and anonymous prices on electricity spot markets with price-sensitive demand.

History: Xiaoquan (Michael) Zhang, Senior Editor; Pallab Sanyal, Associate Editor. Funding: This work was supported by the Deutsche Forschungsgemeinschaft [Grant BI 1057/1-9]. Supplemental Material: The online supplement is available at https://doi.org/10.1287/isre.2022.1139.

Keywords: electronic markets and auctions decision support systems electricity market design demand <sup>fl</sup>exibility nonconvexities pricing

## 1. Introduction

In many parts of the world, electricity markets have developed from monopolies to competitive wholesale markets. For example, European countries and large parts of the United States liberalized their electricity markets in the 1990s. Short-term electricity procurement is now carried out via power exchanges in these jurisdictions. These power exchanges determine central price signals for over-the-counter trades and futures markets (Shah and Chatterjee 2020). Typically, on day-ahead markets, hourly products for the next day are traded. After the day-ahead markets, the market operators use real-time markets in the United States (or intraday markets in Europe) to deal with changes in supply and demand that are closer to the actual dispatch. We will distinguish these types of electricity spot markets from futures markets where participants can hedge against longer-term price risks.

Spot markets are signi<sup>fi</sup>cant in size. In 2020, European coupled day-ahead markets alone cleared 1,530 TWh in 27 countries with average prices between EUR 30 and 40 per megawatt-hour (All NEMO Committee 2021). Similarly, the cost of serving load amounted to \$8.9 billion in the Californian market, covering 26,000 circuit miles, roughly 1,000 power plants, a population of 30 million, and about 9,700 pricing nodes (California ISO 2018; 2021).

With climate change and a transition to renewable energy sources (RES) such as wind and solar power, we are moving to an economy with many thousands of small generators and a more price-sensitive demand side that actively bids in electricity markets and offers <sup>fl</sup>exibility to cope with variability in the supply (IRENA 2019, Hytowitz et al. 2020). Changes in electricity markets are not only relevant for market operators but also impact generators, industrial consumers, and retail consumers alike. These changes in the market have led to renewed interest in the design of electricity markets. Although many aspects of electricity market design are similar to other markets, a few features stand out. First, demand and supply need to be balanced at all times to guarantee a stable electricity grid. Second, electricity markets are characterized by nonconvex preferences. For example, electricity suppliers often incur <sup>fi</sup>xed costs for starting up and running their generators. On the demand side, industrial customers typically need a certain volume of electricity over consecutive hours to <sup>fi</sup>nish production or maintain energy-intensive services. Such consumption pro<sup>fi</sup>les can sometimes be shifted over time, but the pro<sup>fi</sup>les themselves must not be altered. These nonconvexities in the preferences typically lead to nonconvex optimization problems that need to be solved in order to determine the ef<sup>fi</sup>cient or welfaremaximizing dispatch and prices. We will use the term nonconvex markets in what follows.

Deciding over a particular pricing rule in a nonconvex market is a complex problem. In this paper we will describe a series of desirable properties for such pricing rules, outlining when those properties are feasible in real-life settings. We will start describing the theoretical ideal called Walrasian equilibrium, where prices are linear (per megawatt-hour) and anonymous (independent of the participant), they are also envy-free such that nobody would want to deviate from the optimal allocation or dispatch at these prices, and they are budget balanced; that is, no subsidies are required. Unfortunately, it is a well-known fact that in nonconvex markets, Walrasian equilibrium prices do not exist in general. Therefore both academics and practitioners have proposed alternatives where necessarily some of the properties are violated. For instance, electricity markets in the United States compute linear and anonymous market prices but violate budget balance. Pricing rules as they are used by market operators stipulate out-of-market side payments, so-called makewhole payments, to market participants who would make a loss at the market prices. However, makewhole payments are currently under scrutiny by regulators, which demands new approaches, as we will discuss in what follows.

## 1.1. Contributions

First, we prove that make-whole payments cannot be avoided in markets with a price-sensitive buy side. Although the literature suggests that demand response and price-sensitive demand will play an increasing role in the future, standard models in electricity market design mostly assume price-inelastic demand.

We introduce a pricing rule that minimizes makewhole payments and compare it to existing payment rules used in practice and to other academic proposals. This is in contrast to other literature on electricity market pricing, which is largely based on heuristics to minimize lost opportunity costs (i.e., incentives to deviate from the optimal allocation). We argue that lost opportunity costs are less of a concern, because market operators on electricity markets typically enforce stability via penalties. Our experimental results show that high make-whole payments on electricity markets as they are challenged by regulators can either be avoided or be reduced substantially with the new pricing rule. This is not at the expense of higher market prices, and the changes in the overall payments of market participants are very small. The new pricing rule can be solved ef<sup>fi</sup>ciently with standard linear programming techniques, and it is easy to understand. The approach is generic and also of interest to nonconvex markets beyond those for electricity only.

## 1.2. Organization of the Paper

The rest of the paper is structured as follows: Section 2 discusses related literature, and Section 3 provides a short introduction to electricity market design. In Section 4, we discuss competitive equilibrium theory and show when anonymous and linear prices are possible on budget-balanced electricity markets. Section 5 introduces optimization models to compute prices in environments with price-inelastic and price-sensitive demand. We brie<sup>fl</sup>y characterize existing proposals for electricity prices before we provide results of experiments in Section 6. Section 7 provides a summary and conclusions.

## 2. Related Literature

The literature on competitive equilibrium has a long history. In this section, we summarize central theoretical <sup>fi</sup>ndings before we discuss the related literature on electricity market design. We brie<sup>fl</sup>y survey the literature on demand response that leads to price-sensitive demand and the challenges arising from this change for market design. Finally, we discuss the connections between the different literature streams.

## 2.1. Equilibrium Theory

Early in the research on markets, general equilibrium theory was developed to study demand, supply, and prices for multiple goods or objects on markets. The Arrow–Debreu model shows that under convex prefer ences, perfect competition, and demand independence, there must be a set of competitive equilibrium prices (Arrow and Debreu 1954, McKenzie 1959, Gale 1963,

Kaneko 1976). The results derived from the Arrow– Debreu model led to the well-known welfare theorems, representing important arguments for markets to be used as ef<sup>fi</sup>cient or welfare-maximizing means to allocate scarce resources such as electricity. The <sup>fi</sup>rst theorem states that any Walrasian equilibrium leads to a Pareto-ef<sup>fi</sup>cient allocation of resources. The second theorem states that any ef<sup>fi</sup>cient allocation can be attained by a Walrasian equilibrium under the Arrow–Debreu model assumptions (Mas-Colell et al. 1995). Walrasian equilibrium prices are such that there is a single price for each product (i.e., prices for a package are linear), and this is the same price for all participants (i.e., anonymous prices with no price differentiation).

However, standard general equilibrium theory assumes divisible goods and convex preferences. Most real-world markets such as those for electricity, transportation, radio frequency spectrum, and environmental access rights are traded as indivisible goods, and participants have nonconvex preferences and complex constraints. Such markets have led to substantial interest in the question of when Walrasian equilibria exist. Unfortunately, in markets with indivisible goods, it is well known that only very restricted types of valuations (e.g., substitute valuations) allow for convex allocation problems and Walrasian equilibria (Kim 1986, Bikhchandani and Mamer 1997, Leme 2017, Baldwin and Klemperer 2019).

This raises the question of how prices can be computed in the presence of nonconvex preferences for indivisible goods and which properties we can hope to achieve compared with Walrasian equilibria. Established market design desiderata are efficiency (i.e., maximization of welfare or gains from trade), individual rationality (i.e., participants should not make a loss), budget balance (i.e., the market operator should not make a loss or a gain), and envy-freeness (i.e., participants would not want a different allocation at the prices). These axioms are not only central to economic theory (Mas-Colell et al. 1995) but also widely adopted and natural design desiderata for practical market design. If the allocation problem is convex, duality theory and dual prices in convex optimization provide a principled way to determine competitive equilibrium prices that satisfy these desiderata (Bichler et al. 2021). In nonconvex markets, it is well known that competitive equilibrium prices might need to be nonlinear and personalized, and such prices might not even exist (Bichler and Waldherr 2017). Thus, in a combinatorial auction or a combinatorial exchange that allows for supply and demand bids on packages of items, each bidder might need to have a different price for the same package (personalized prices), and each package price could differ from the sum of the item prices in this package (nonlinear prices). As a simple example, consider a single supplier with an (indivisible) sell bid of 2 MWh for \$30, whereas there is one buyer asking for 1 MWh for at most \$10 and another buyer asking for 1 MWh for \$28. Linear and anonymous market pri ces could not be higher than \$10/MWh, and as such, there would be no trade and no gains from trade. With price differentiation, trade would be possible. However, nonlinear and personalized prices would convey little information other than that a bidder lost or won. Besides, if prices should serve as a baseline for derivatives, as is the case for options or futures, this is hardly possible with nonlinear prices that differ among participants. In other words, anonymity and linearity are important requirements for prices not only on electricity markets but also in other domains (Bichler et al. 2018).

## 2.2. Pricing on Electricity Spot Markets

Electricity spot markets are composed of varying levels of “demand” (load) and matching levels of “supply” (generation). Market participants submit supply and demand bids according to a certain bid language that determines the form of the allocation problem (which yields the ef<sup>fi</sup>cient dispatch) and the pricing rule. For example, in markets in the United States, generators can express start-up or no-load costs, economies of scale (by means of piecewise-linear cost functions), or minimum-generation requirements. These and other elements of the bid language then translate into nonconvex allocation problems (Herrero et al. 2020). In 2005, the Pennsylvania, Jersey, Maryland Power Pool (PJM) introduced mixed integer programming (MIP) in order to address these nonconvexities and to determine the ef<sup>fi</sup>cient allocation or dispatch (O’Neill et al. 2020). Since 2018, all independent system operators (ISOs) in the United States use MIPs to compute the ef<sup>fi</sup>cient dispatch instead of the Lagrangian relaxation that was used before. Dual prices, as they are accessible for convex optimization problems, are not available in such markets, which led to a fundamental question: How can market prices per hour be computed in such nonconvex markets?

One approach followed by European day-ahead markets is to sacri<sup>fi</sup>ce ef<sup>fi</sup>ciency. The EUPHEMIA algorithm that is used to clear European day-ahead markets <sup>fi</sup>rst solves a welfare maximization allocation problem as a mixed-integer program and then iteratively tries to <sup>fi</sup>nd linear and anonymous prices that clear the market. If such prices cannot be found, additional constraints are added to the welfare maximization problem (NEMO Committee 2020). However, it is unclear how much of the gains from trade are sacri-<sup>fi</sup>ced this way. Furthermore, this approach inevitably leads to paradoxically rejected bids (Meeus et al. 2009). In particular, there are generators with an ask price that is less than the market price, yet they will not be dispatched. Such prices are also not envy-free and hence not a Walrasian equilibrium. We will not further discuss this approach in our paper and focus on market designs that implement the ef<sup>fi</sup>cient outcome, as done in the United States.

Over the years, several pricing rules have been suggested that aim to mimic competitive equilibrium prices on such MIP-based electricity markets (Liberopoulos and Andrianesis 2016). Locational marginal pricing (LMP) rules of many ISOs are based on integer programming (IP) pricing, where the allocation problem is solved to optimality, the integer variables are <sup>fi</sup>xed, and the prices are then derived from the dual variables of the demand-supply constraint of the resulting (convex) linear program (O’Neill et al. 2005). IP pricing computes anonymous and linear prices, but these prices do not constitute competitive equilibrium prices. Some generators might not maximize their individual pro<sup>fi</sup>ts and want to deviate (i.e., switch to a different dispatch at those prices), and IP prices are thus not envy-free. The latter is central to the de<sup>fi</sup>nition of a competitive equilibrium and leads to stability of the outcome. It is important to note that, besides a lack of stability, the generators often make a loss at the IP prices (i.e., prices are not even individually rational). Pricing in U.S. ISO markets has changed in an attempt to reduce the weight of uplift and to internalize all operational costs into market prices as far as possible (Herrero et al. 2020). Some ISOs switched from IP pricing to Extended LMP (ELMP) in recent years, which is based on the dual variables from the demand-supply constraint in the linear programming (LP) relaxation of the underlying MIP. However, similar issues arise. As a consequence, U.S. ISOs continue to search for improvements via new formulations for ELMP.<sup>1</sup>

ISOs use personalized side payments to address the fact that the public market prices from IP pricing or ELMP are neither envy-free nor individually rational. This effectively differentiates the linear and anonymous market prices from the payments of the market participants, which are then nonlinear and personalized. Typically, two kinds of external side payments are considered in the literature: lost opportunity costs and make-whole payments (Schiro et al. 2016). Lost opportunity costs describe payments that are so high that no generator would want to change its dispatch, and envy-freeness is achieved. Such payments may be very large if the market contains nonconvexities, and these payments could even go to generators that were not scheduled (Eldridge et al. 2019). However, electricity markets are highly regulated markets, and as such, there are alternative means to enforce stability other than high lost opportunity cost payments. In actuality, most ISOs only pay make-whole payments to ensure individual rationality of all generators and stipulate penalties that a generator has to pay if it indeed deviates from the optimal dispatch. In other words, they relax envy-freeness to only individual rationality requirements. We refer to such outcomes as having penalty-based stability.

However, even the make-whole payments are a signi<sup>fi</sup>cant concern (Hytowitz et al. 2020). The U.S. Federal Energy Regulatory Commission (FERC) regulates the U.S. wholesale power markets to promote just competition. In 2018, the FERC found that the practices of several ISOs were unjust and ordered them to change their pricing because prices did not accurately re<sup>fl</sup>ect the cost of serving load (O’Neill et al. 2019). Make-whole payments are not re<sup>fl</sup>ected in the public price signals, and they lead to biased investment signals. This also constitutes a problem for futures markets, where spot market prices serve as the key reference. In addition, the FERC has released several orders and notices about pricing, which argue that the “use of uplift payments can undermine the market’s ability to send actionable price signals.”<sup>2</sup> Similarly, O’Neill et al. (2019, p. 14) state that “the makewhole payments are not transparent to other market participants and are allocated too broadly to provide correct price incentives for market participants to make ef<sup>fi</sup>cient entry and exit decisions as well as ef<sup>fi</sup>cient investments in facilities and equipment.” In summary, a challenge in U.S. ISO markets is to reduce side payments, which are a clear sign of inef<sup>fi</sup>cient pricing, while still ensuring individual rationality of all market participants.

In our <sup>fi</sup>rst contribution, we introduce an optimization model that always computes prices that are individually rational and budget balanced and clear the market at the ef<sup>fi</sup>cient dispatch without make-whole payments under the assumptions of price-inelastic demand and strict demand-supply equality. These assumptions are standard in the electricity market literature (Liberopoulos and Andrianesis 2016).

## 2.3. Price-Sensitive vs. Price-Inelastic Demand

Although the academic literature on electricity market pricing almost exclusively relies on the assumption of price-inelastic demand, this assumption is unlikely to hold in the future (Herrero et al. 2020). Power systems are changing profoundly as a result of the introduction of large volumes of RES. The largest proportion of RES capacity are variable energy resources (VERs) such as solar and wind power. The characteristic variability and uncertainty of these VERs require an integration of demand <sup>fl</sup>exibility (Reihani et al. 2016). Demand response is the most immediately available way of increasing demand <sup>fl</sup>exibility and the cheape option compared with storage technologies (European Commission Directorate-General for Energy 2016). For example, industrial processes for the production of pulp and paper are able to provide demand response with a duration of up to three hours without any notice time (European Commission Directorate-General for Energy 2016). Still, this <sup>fl</sup>exibility comes at a cost, and bidders want lower prices if they provide more <sup>fl</sup>exibility. As indicated, it is expected that in the future we will see a much increased price-responsive demand (Hytowitz et al. 2020). FERC Order 2222, issued in 2020, also aims at an active demand side to bid in wholesale markets. However, such pricesensitive bids for <sup>fl</sup>exible demand make market design more challenging. First, new bid formats lead to additional nonconvexities, which even increase the makewhole payments needed with currently used pricing rules. Second, prices that are individually rational and clear the market at the ef<sup>fi</sup>cient dispatch cannot always be budget balanced anymore, as we will show.

In our second contribution, we introduce alternative pricing rules that minimize make-whole payments while still clearing the market at the ef<sup>fi</sup>cient dispatch with price-sensitive demand. The pricing rules introduced in this paper are based on a mathematical program that differs signi<sup>fi</sup>cantly from IP pricing, ELMP, or other proposals in the literature. Similar to existing pricing rules on ISO markets, it treats ef<sup>fi</sup>ciency and individual rationality as <sup>fi</sup>rst-order goals (i.e., enforces these directly in the model), whereas budget balance and envy-freeness are treated as second-order goals. However, in contrast to the existing literature, we prioritize budget balance over envy-freeness in a lexicographical way. This lexicographical ordering is motivated by the fact that the violation of budget balance and the resulting side payments have led to concerns by regulators and market participants, as we discussed earlier. Envy-freeness should lead to stability of the outcome in markets, as participants do not have an incentive to deviate. In highly regulated and transparent electricity markets, stability can be achieved by imposing penalties, which is already common on ISO markets today. Participants cannot easily deviate from the ef<sup>fi</sup>cient dispatch determined by the market operator, and the level of penalties (that generators would only have to pay if they deviated from the ef<sup>fi</sup>cient dispatch) is much less of a concern than high personalized side payments by the market operator that are not re<sup>fl</sup>ected in the market prices.

The new pricing rule that we propose, PE-A, can be computed in polynomial time and scales to large problem sizes. It is worth noting that, we show that average locational hourly prices do not increase compared with other established pricing rules in our experiments, and the impact on the payments of individual market participants are small. However, PE-A avoids large make-whole payments as they occur with IP pricing, even with price-sensitive demand. In Section 6.2 we analyze our proposed pricing schemes based on a widely used benchmark data set: the IEEE Reliability Test System (RTS) consisting of 24 nodes, 24 hours, 32 generators (with nonconvex cost functions), and 17 consumers. The average make-whole payments for PE-A pricing only amount to 0%–0.15% of the total costs in all treatments. By contrast, for IP pricing or

ELMP, the make-whole payments were 4%–5% on average for all generators. Actually, for some generators, the make-whole payments could be more than 10% of their payment with IP pricing. Such high make-whole payments can be avoided with PE-A, and we achieve almost-budget-balanced outcomes in all experiments. We also compare PE-A with a simple implementation of average incremental cost (AIC) pricing, a pricing rule that was recently proposed to address high side payments on electricity spot markets. PE-A is not restricted to the speci<sup>fi</sup>cs of the allocation problem on electricity markets and can also be applied to other types of nonconvex and two-sided markets.

## 2.4. Positioning in the Literature

This paper draws on different streams in the literature. The fundamental problem of pricing in multiobject markets is central to microeconomic theory and the management sciences. The fact that nonconvex preferences lead to problems in equilibrium theory has been known for a long time (see, e.g., Farrell (1959)). Several contributions such as the well-known Shapley-Folkman-Starr lemma (Starr 1969) suggest that nearly competitive equilibria are possible if the market grows large. A number of more recent articles suggest that Walrasian prices can be approximated in (very) large markets and that such markets are approximately incentive compatible (Azevedo et al. 2013, Azevedo and Budish 2019).

Electricity markets are already very large, with hundreds of participants, but their nonconvex nature adds extra complexity to the pricing problem. The question of how actual pricing rules for such nonconvex electricity markets should be designed has led to a number of heuristics such as IP pricing and ELMP in the operations research and power engineering literature (O’Neill et al. 2005; 2016; 2019; Liberopoulos and Andrianesis 2016; Eldridge et al. 2019). We will revisit this literature in Section 5.4. These heuristics typically aim to approximate a competitive equilibrium and relax budget balance and envy-freeness.

The information systems literature has made numerous contributions to market design and pricing in nonconvex markets. Some of the work deals with pricing in combinatorial auctions (Xia et al. 2004; Adomavicius and Gupta 2005; Adomavicius et al. 2012; 2020; Guo et al. 2012; Bichler et al. 2013; Petrakis et al. 2013), whereas other articles deal with combinatorial exchanges (Guo et al. 2012, Bichler et al. 2018). The design of energy markets has also received attention in information systems more recently (Ketter et al. 2016, Valogianni and Ketter 2016, Koolen et al. 2018). This paper combines these two strands, suggesting a new approach to pricing in electricity markets that substantially reduces or even eliminates the need for side payments. Our approach can well be relevant to other nonconvex markets such as those used in transportation (Caplice and Shef<sup>fi</sup> 2003, Garrido 2007) or for trading <sup>fi</sup>shery access rights (Bichler et al. 2019).

## 3. Bid Languages and Demand-Side Flexibility

Let us provide a brief overview of electricity market design and the role of demand response for future market designs. The pricing rules that can be employed on a market depend on the underlying allocation problem, which again depends on the types of bids or the bid language available on a market. The bid languages on electricity markets today are speci<sup>fi</sup>c and aim at re<sup>fl</sup>ecting the underlying cost functions of generators and, in part, valuation functions of the demand side. They allow the participants to communicate their valuations or cost structures effectively. The market operator then solves the allocation problem and determines a schedule of generation and prices (Cramton 2017). Day-ahead markets are complemented by intraday (Europe) or real-time (U.S.) markets. These markets modify the day-ahead schedule to determine the actual physical dispatch. Especially in European countries, the day-ahead market is considered to be the main reference market, whereas in the United States, it mostly possesses the notion of a forward market for the real-time market that determines the dispatch (Antonopoulos et al. 2020).

Bid languages allow for the expression of the underlying costs in order to enable ef<sup>fi</sup>cient outcomes (Cramton 2003). For instance, generators typically incur certain <sup>fi</sup>xed costs for starting up and running a generator, as well as variable electricity production costs. Moreover, the operation is often subject to technical conditions (e.g., referring to minimum runtimes or ramping constraints). On the demand side, market participants might want to express certain <sup>fl</sup>exibility options, and this will become much more of an issue in the future with increasing levels of RES. Let us brie<sup>fl</sup>y summarize the state of the practice.

In European markets, aside from regular bids for individual hours of the day, the bid language allows for block bids. The latter represent a set of individual bids that can be executed only in total or not at all (NEMO Committee 2020). Cost structures are communicated as single-part offers, requiring market participants to aggregate various cost components into a single parameter. The communication of multiple cost components is explicitly avoided in order to promote decentralized decision making on the part of the market participants (Herrero et al. 2020). Most European markets allow for price-sensitive bids on the demand side, although between 2010 and 2015, an estimated 82%–89% of the bids were not price sensitive (European Commission Directorate-General for Energy 2016). In Europe, the market is cleared with (zonal) linear and anonymous prices without any side payments, which leads to ef<sup>fi</sup>- ciency losses in the dispatch (Meeus et al. 2009). Overall, the bid language permits a less detailed expression of cost functions than, for instance, bid languages used in the United States.

Market participants in the United States are generally permitted to indicate their costs in a more granular way than in European markets (Madani et al. 2018). Cost structures can be communicated with multipart bids, usually consisting of start-up costs, no-load costs, and an offer curve. Furthermore, generators can express technical constraints such as minimum up- and downtimes, minimum and maximum output levels, ramp rates, or start-up times. This allows generators to express their cost characteristics very effectively (Cramton 2017). So-called self-schedules are pure quantity bids specifying an amount of energy that needs to be dispatched regardless of price levels or cost structures. Demandside bids comprise price-inelastic self-scheduling as well as price-sensitive bid curves (Cramton 2017).

As an example of an ISO bid language, PJM allows for <sup>fi</sup>xed-demand bids and price-sensitive bids on the demand side. A <sup>fi</sup>xed-demand bid or self-schedule is price inelastic and de<sup>fi</sup>nes a level of energy to be purchased at any price over a particular hour at a location or node. By contrast, price-sensitive bids specify a de<sup>fi</sup>ned level of energy, a location and a price, above which the demand bid is 0. More than 90% of the bids in the PJM market were <sup>fi</sup>xed-demand bids in 2019, and only a very small proportion is price sensitive at this point (Monitoring Analytics 2019). This explains why most proposals for pricing rules in the literature assume only price-inelastic demand. However, this is expected to change with increasing levels of demand response, which speci<sup>fi</sup>es <sup>fl</sup>exible bids to be executed but only up to a certain price.

U.S. ISO markets aim to <sup>fi</sup>nd a welfare-maximizing dispatch based on bids, yet in contrast to European markets, they <sup>fi</sup>rst determine the ef<sup>fi</sup>cient dispatch before they compute prices. Whereas European markets compute prices for large price zones, the prices on U.S. electricity markets are computed per node in the electricity grid. The nodal system aims to consider physical grid constraints in the optimization. In U.S. nodal markets, bids and offers, resource constraints, network constraints, transmission losses, and certain ancillary service requirements are all optimized simultaneously<sup>3</sup> (Cramton 2017). As a result, the electricity price re<sup>fl</sup>ects the marginal cost of supplying electricity at a speci<sup>fi</sup>c node in the network (assuming the underlying problem was convex). Locational marginal pri ces have also been suggested for European markets (Purchala 2018, Ashour Novirdoust et al. 2021). Fo the remainder of this paper, we discuss markets as they are operated by ISOs in the United States, in Australia, in South American markets, and in many other parts of the world.

As indicated, demand-side bidding is central to accommodate the volatile nature of VERs in the future. ISOs in the United States have already taken steps to accommodate demand-side <sup>fl</sup>exibility and pricesensitive bids. For example, the Midcontinent ISO (MISO) is undergoing reforms<sup>4</sup> to better incorporate demand-responsive resources into the price formation (in both day-ahead and real-time markets). The abovementioned FERC Order 2222 promotes participation of the demand side—in particular, distributed energy resources and storage in wholesale electricity markets. There is signi<sup>fi</sup>cant potential for industrial demand <sup>fl</sup>exibility, but industry will invest in <sup>fl</sup>exibility options only if it comes with lower electricity prices (European Commission Directorate-General for Energy 2016). Therefore, the increase of price-sensitive bids in wholesale electricity markets is to be expected in the future.

A number of proposals have been made for the demand side to express <sup>fl</sup>exibility (Liu et al. 2015, Ottesen and Tomasgard 2015, Ottesen et al. 2016). Flexibility extensions of a bid language on the demand side can include shiftable volumes (asking to meet a certain volume within a certain time frame), shiftable pro<sup>fi</sup>les (allowing to shift a predetermined demand pro<sup>fi</sup>le over time), or adjustable demand (involving extensible or curtailable demand). Such <sup>fl</sup>exibility options in the bid language would be a powerful way to address the intermittent nature of VERs, but they lead to substantial nonconvexities because of additional integer variables in the allocation problem. For example, thermal power plants have ramping constraints that make the production available in one period dependent on the production in the preceding and following periods. The introduction of renewable energy sources leads to an increased use of the dispatchability of thermal units, and ramping constraints are expected to be binding more frequently (Herrero et al. 2020). Ignoring such constraints in the day-ahead schedule can signi<sup>fi</sup>cantly degrade the ef<sup>fi</sup>- ciency of the dispatch. Thus, one cannot expect the nonconvexities on electricity markets to vanish, especially in a future with large proportions of renewable energy sources. Such demand <sup>fl</sup>exibility and price-sensitive demand have ample consequences on the properties of prices that we can compute, as we will show.

## 4. Competitive Equilibrium

In this section, we introduce necessary notation, summarize existing theory on pricing in nonconvex markets, and discuss design desiderata for electricity markets.

4.1. Notation and Economic Environment In the auction market, there are K types of items (goods; hours and locations in a day-ahead market), denoted by $k \in { \mathcal { K } } = \left\{ 1 , \ldots , K \right\} _ { } .$ , buyers $i \in \mathcal { T } = \left\{ 1 , \ldots , I \right\}$ and sellers $j \in \mathcal { I } = \{ 1 , \ldots , J \}$ . In the multiunit case, we have multiple homogeneous units (e.g., the minimum bid increment) for each of the heterogeneous K items $k \in \mathcal { K } .$ . A bundle of interest to buyer i (seller j) is described by a vector $x _ { i } \in \mathcal { X } \ ( y _ { j } \in \mathcal { Y } )$ , where $\mathcal { X } \left( \mathcal { V } \right)$ is a compact subset of $\mathbb { Z } _ { \geq 0 } ^ { K }$ . Each buyer i (seller j) has a monotonously increasing (decreasing) value function v<sub>i</sub>: $\mathcal { X } \xrightarrow { } \mathbb { R } _ { \ge 0 } \mathrm { ~ } ( v _ { j } \colon \mathcal { Y } \xrightarrow { } \mathbb { R } _ { \ge 0 } )$ over bundles of items or objects $x _ { i } \left( y _ { j } \right)$

An auctioneer wants to <sup>fi</sup>nd an allocation of items to bidders. The auctioneer aims for allocative efficiency. This means the auctioneer wants to maximize social welfare, which is the gains from trade for all participants (the buyers and sellers). The goal of the auctioneer is to <sup>fi</sup>nd an ef<sup>fi</sup>cient allocation $( \mathbf { x } , \mathbf { y } ) = ( x _ { 1 } ,$ $\dots , x _ { I } , y _ { 1 } , \dots , y _ { J } )$ and linear and anonymous marketclearing prices $\lambda = \{ \lambda ( k ) \} _ { k \in \mathcal { K } } \in \mathbb { R } _ { \geq 0 } ^ { K }$ . The linearity of prices refers to the property that individual prices are set for each item $k \in \mathcal { K } ;$ the price for a bundle $x _ { i }$ is then simply the sum of the prices of its components (i.e., it is given by the dot product $\lambda ^ { \prime } x _ { i } )$ . Anonymity means that the resulting prices λ are the same for all bidders, and there is no price differentiation. Competitive equilibrium prices might also be nonlinear and personalized, but linearity and anonymity are crucial on electricity and other real-world markets, as we discussed earlier. We assume buyer i’s (direct) utility from bundle $x _ { i }$ is given by $\pi _ { i } ( x _ { i } , \lambda ) = v _ { i } ( x _ { i } ) -$ $\lambda ^ { \prime } x _ { i } ,$ and seller $j ^ { \prime } \mathrm { s }$ utility from bundle $y _ { j }$ is given by $\pi _ { j } ( y _ { j } , \lambda ) = \lambda ^ { \prime } y _ { j } - v _ { j } ( y _ { j } )$ . Such utility functions are linear in price and referred to as quasilinear utility functions. All market participants are assumed to be price takers, meaning that they cannot in<sup>fl</sup>uence the market prices on their own. Social welfare can now be de<sup>fi</sup>ned as $\begin{array} { r } { \sum _ { i \in \mathcal { T } } v _ { i } ( x _ { i } ) - \sum _ { j \in \mathcal { T } } v _ { j } ( y _ { j } ) } \end{array}$ , as prices cancel when the utilities of market participants are added.

With linear and anonymous prices $\lambda = ( \lambda ( 1 ) , \ldots ,$ $\lambda ( k ) , \ldots , \lambda ( K ) )$ , the indirect utility function is de<sup>fi</sup>ned as

$$
\begin{array}{l} u _ {i} (\lambda) = \max _ {x \in \mathcal {X}} \{v _ {i} (x) - \lambda^ {\prime} x \} \quad \text { and } \\ u _ {j} (\lambda) = \max _ {y \in \mathcal {Y}} \{\lambda^ {\prime} y - v _ {j} (y) \}. \end{array}
$$

The indirect utility function is widely used in economics and returns the maximal utility that bidder i can obtain at prices λ. The demand correspondence terms $D _ { i } ( \boldsymbol { \lambda } )$ and $\overset { \ – } { D } _ { j } ( \lambda )$ respectively describe the sets of bun dles that maximize the indirect utility function at

prices λ:

$$
\begin{array}{l} D _ {i} (\lambda) = \underset {x \in \mathcal {X}} {\arg \max} \{v _ {i} (x) - \lambda^ {\prime} x \} \quad \text { and } \\ D _ {j} (\lambda) = \underset {y \in \mathcal {Y}} {\arg \max} \{\lambda^ {\prime} y - v _ {j} (y) \}. \end{array}
$$

## 4.2. Competitive Equilibrium

If in an outcome (consisting of an allocation and prices) all bidders are allocated a bundle from their demand correspondence, then the outcome is envy-free (EV). No bidder would want to get another bundle, as a bidder cannot increase her utility at these prices. If we have EV and the market is budget balanced (BB), we have a competitive equilibrium (CE). If competitive equilibrium prices are linear and anonymous (LA), we also refer to this as a Walrasian equilibrium.

Definition 1 (Walrasian (Competitive) Equilibrium (WE)). A price vector $\lambda ^ { * }$ and a feasible allocation $( \mathbf { x } , \mathbf { y } )$ form a Walrasian equilibrium if $\textstyle \sum _ { i \in { \mathcal { T } } } x _ { i } = \sum _ { j \in { \mathcal { T } } } y _ { j } , x _ { i } \in D _ { i } ( \lambda ^ { * } )$ for every buyer i $\mathcal { T } , y _ { j } \in D _ { j } ( \lambda ^ { * } )$ for every seller $j \in \mathcal { I } ,$ , and budget is balanced with $\begin{array} { r } { \sum _ { i \in \mathcal { T } } \lambda ^ { * ^ { \prime } } x _ { i } = \sum _ { j \in \mathcal { T } } \lambda ^ { * ^ { \prime } } y _ { j } } \end{array}$

The BB condition implies that an unallocated item has a price of 0. Note that getting a bundle from the demand correspondence implies individual rationality (IR), because if bidders would make a loss with a bundle, it would never be in their demand correspondence. However, EV is a much stronger condition than IR. In summary, a WE has the properties BB  EV  LA. Later we will distinguish between LA prices and linear and anonymous payments (LAPs). For now, we assume that prices coincide with the payments.

The question is now under which conditions Walrasian equilibria exist and whether they support ef<sup>fi</sup>cient (welfare-maximizing) outcomes (EF). To study these questions in a market with quasilinear utilities and independent private values, we use the following mathematical optimization problem describing a (combinatorial) exchange, which allows for arbitrary package bids. This bid language does not impose any restrictions on the types of valuations or cost functions and can be seen as the most general form of nonconvex markets. As a matter of fact, the most prominent element of bid languages used in European day-ahead markets are block bids $( \mathrm { i . e . , }$ package bids on adjacent time slots), and they can be easily captured in the following optimization problem. Electricity markets in the United States stipulate different bid languages to reduce the number of bids that participants need to submit, but they can be seen as a speci<sup>fi</sup>c type of combinatorial exchange.

Let $\dot { \mathcal { X } _ { i } } \subseteq \mathbb { Z } _ { \geq 0 } ^ { K }$ denote all bundles for which buyer i submitted a bid, and let $\mathcal { V } _ { j } \subseteq \mathbb { Z } _ { \geq 0 } ^ { K }$ denote all bundles for which seller j submitted an ask. For simplicity, we make the natural assumption that every bidder submits a bid with value 0 for the empty bundle. Let $z _ { i } ( x ) \in \{ 0 , 1 \}$ be a binary decision variable denoting whether buyer i wins bundle $x \in \mathcal { X } _ { i } ,$ and let $z _ { j } ( y ) \in$ $\{ 0 , 1 \}$ be a binary decision variable denoting whether seller $j$ wins bundle $\boldsymbol { y } \in \mathcal { D } _ { j }$ . The parameters $x ( k )$ and y(k) describe how many units a buyer wants or a seller provides of item k in a bundle. The allocation or winner determination problem (WDP) can then be written as an integer program as follows:

$$
\begin{array}{l l} \max \sum_ {i \in \mathcal {I}} \sum_ {x \in \mathcal {X} _ {i}} v _ {i} (x) z _ {i} (x) - \sum_ {j \in \mathcal {J}} \sum_ {y \in \mathcal {Y} _ {j}} v _ {j} (y) z _ {j} (y) \\ \text {s.t.} \\ \sum_ {x \in \mathcal {X} _ {i}} z _ {i} (x) \leq 1 & \forall i \in \mathcal {I} \quad (\pi_ {i}), \\ \sum_ {y \in \mathcal {Y} _ {j}} z _ {j} (y) \leq 1 & \forall j \in \mathcal {J} \quad (\pi_ {j}), \\ \sum_ {i \in \mathcal {I}} \sum_ {x \in \mathcal {X} _ {i}} x (k) z _ {i} (x) \leq \sum_ {j \in \mathcal {J}} \sum_ {y \in \mathcal {Y} _ {j}} y (k) z _ {j} (y) \\ & \forall k \in \mathcal {K} \quad (\lambda (k)), \\ z _ {i} (x) \in \{0, 1 \} & \forall i \in \mathcal {I},   \forall x \in \mathcal {X} _ {i}, \\ z _ {j} (y) \in \{0, 1 \} & \forall j \in \mathcal {J},   \forall y \in \mathcal {Y} _ {j}. \\ & (\text {WDP}) \end{array}\tag{WDP}
$$

The WDP determines an allocation of bundles maximizing gains from trade (i.e., an ef<sup>fi</sup>cient outcome). It assumes that participants specify a package bid for each possible package of interest, but they can win at most one. This is also referred to as an XOR bid language. Although such a bid language is fully expressive, it requires exponentially many bids and is impractical for most applications. This is why electricity markets specify compact bid languages assuming some knowledge of the cost functions of generators. Bikhchandani and Mamer (1997) describe a multi-item, single-unit market. Their central theorem shows that there exist clearing prices for the indivisible single-unit problem if and only if the LP relaxation of WDP has an integer solution. In this case, the dual variables $\lambda ( k )$ constitute WE prices, and the dual variables $\pi _ { i }$ and $\pi _ { j }$ determine the surplus of buyer i and seller $j ,$ respectively. The result can be proven via the strong duality theorem and the complementary slackness conditions in linear programming. As was already noted by Bikhchandani and Mamer (1997), the result for multi-item, multi-unit markets also directly follows from their result, by considering each of the mul tiple units as separate items. As a result, the welfare theorems hold in the quasilinear model.

Theorem 1 (First and Second Welfare Theorems). Let x, y be an equilibrium allocation induced by a Walrasian equilibrium price vector $\lambda ;$ then $( \mathbf { x } , \mathbf { y } )$ yields the optimal social welfare. Conversely, $i f \left( \mathbf { x } , \mathbf { y } \right)$ is a Pareto-efficient allocation, then it can be supported by a Walrasian price vector λ so that $\left( \lambda , \mathbf { x } , \mathbf { y } \right)$ forms a Walrasian equilibrium.

Unfortunately, the LP relaxation of WDP does not yield integer solutions in general, and thus we cannot expect a WE to exist in general. In fact, it is well known that a WE only exists for restricted types of valuations for which the LP relaxation actually yields a feasible integer solution. For example, if all bidders valuations are strong substitutes, this is a suf<sup>fi</sup>cient condition for a WE to exist (Bikhchandani and Mamer 1997, Leme 2017, Baldwin and Klemperer 2019, Bichler et al. 2021). In practice, these conditions are rarely satis<sup>fi</sup>ed. In particular, nonconvex cost functions on electricity markets lead to nonconvex allocation problems that do not satisfy conditions for a WE.

Competitive equilibrium prices do not need to be linear and anonymous. Bikhchandani and Ostroy (2002) show that for combinatorial auctions with arbitrary valuations, competitive equilibrium prices need to be personalized and nonlinear. Such prices convey little information other than that a particular package was winning or losing. In fact, for combinatorial exchanges with multiple buyers and sellers, there can even be situations where no competitive equilibrium exists (Bichler and Waldherr 2017). As discussed earlier, linear and anonymous prices on day-ahead electricity markets are an important baseline for forward markets and serve as investment signals. Therefore, we need to relax some of the design desiderata of Walrasian equilibria.

## 4.3. Penalty-Based Stability

We discussed that prices should be linear and anonymous (LA), they should support ef<sup>fi</sup>cient allocation (EF), and neither the participants (IR) nor the auctioneer (BB) should make a loss. If envy-freeness (EV) was additionally satis<sup>fi</sup>ed, prices would support a Walrasian equilibrium. The welfare theorems (Theorem 1) suggest that all of these axioms are satis<sup>fi</sup>ed in convex markets. With general preferences in nonconvex markets, however, this is impossible to achieve (Bikhchandani and Ostroy 2002, Bichler and Waldherr 2017). Market operators might not want to relax EF and IR, as welfare should be maximized, and no participants should incur losses from submitting bids. Current pricing schemes such as IP pricing and ELMP sacri<sup>fi</sup>ce BB and EV, but the side payments that arise from the violation of BB have led to controversy, as outlined in the introduction.

EV describes stability at prices from which no participant would want to deviate. In highly regulated and transparent markets such as electricity markets, stability can also be enforced without prices. As a matter of fact, U.S. ISOs such as MISO, the Electric Reliability Council of Texas, New York Independent System Operator, and California Independent System Operator enforce the stability of the outcome via penalties in cases where the generator deviates from the ef<sup>fi</sup>cient dispatch (O’Neill et al. 2020). Compared with a WE, they relax the EV condition and only ask for IR. In what follows, we will show that with price-inelastic demand and a strict demand-supply equivalence, we can always <sup>fi</sup>nd prices that satisfy $\mathrm { I R } \wedge \mathrm { B B } \wedge \mathrm { L A } \wedge \mathrm { E F } .$ Although we focus on an electricity market example, the insights are relevant to all types of nonconvex markets. Let us introduce a simpli<sup>fi</sup>ed example of a single hour traded on an electricity market to illustrate which properties we can hope to achieve with linear and anonymous prices. From now on, we require strict demand-supply equivalence.

Example 1. Suppose we have three generators, G1, G2, and G3 (the sellers on electricity markets). G1 produces 10 MWh and asks for \$500 (\$50/MWh). G2 produces 20 MWh and asks for \$300 (\$15/MWh). Finally, G3 produces 30 MWh and asks for \$700 (\$23.3/ MWh). A buyer needs exactly 30 MWh in this hour and can purchase either from G1 and G2 or from G3, where buying from G3 is the ef<sup>fi</sup>cient dispatch. Bids are indivisible. There are several options for the ISO:

1. The ISO could select the ef<sup>fi</sup>cient dispatch but set the price just below \$15/MWh, the ask of G2. The ef<sup>fi</sup>- cient dispatch with G3 is selected, but G3 makes a loss. In order to achieve IR, the market maker can pay G3 \$700 30 MWh \$15= MWh \$250 as a make whole payment. These side payments are commonly used in U.S. electricity markets, but they violate BB.<sup>5</sup>

2. The ISO could select the ef<sup>fi</sup>cient dispatch and set the price at the ask of G3 (i.e., \$23.3/MWh). At this price it would be attractive for G2 to produce, and her ask is “paradoxically rejected.” It is common on U.S. electricity markets to de<sup>fi</sup>ne a penalty for G2 in case she does. This penalty would be at the difference of her ask and the market price. In our example, this penalty for G2 would be 20 MWh \$23:3= MWh \$300 \$166:67. The market satis<sup>fi</sup>es EF, IR, and BB but not EV, as G2 does not maximize her payoff at the prices. As such, it is ef<sup>fi</sup>cient but not a WE.

3. The ISO could pick the inef<sup>fi</sup>cient dispatch with generators G1 and G2 and set the price at \$50/MWh. No side payments by an ISO are needed, but there is a welfare loss of \$100. This alternative is implemented on European day-ahead markets. G3 is paradoxically rejected.

If we use penalties to enforce stability of the outcome, we can de<sup>fi</sup>ne new design desiderata for pricing on nonconvex markets. Recall that $\pi _ { k }$ is the direct utility for market participant k.

Definition 2 (Penalty-Based Stable, Budget-Balanced, and Efficient Outcome (PBE)). A linear and anonymous price vector λ<sup>∗</sup> and an ef<sup>fi</sup>cient allocation $( { \bf x } , { \bf y } )$ form a penalty-based stable and ef<sup>fi</sup>cient outcome if $\pi _ { i } ( x _ { i } , \lambda ^ { * } )$ $\ge \bar { 0 } , \pi _ { j } ( \dot { y _ { j } } , \lambda ^ { * } ) \ge 0$ for every buyer $i \in \mathcal { T }$ and every seller $j \in \mathcal { I }$ if the market is budget balanced with $\Sigma _ { i \in \mathcal { T } } \lambda ^ { * ^ { \prime } } x _ { i }$ $\mathbf { \chi } = \sum \limits _ { j \in \mathcal { I } } \lambda ^ { * ^ { \prime } } y _ { j }$

Note that budget balance and linear and anonymous prices in nonconvex markets imply a strict demandsupply equivalence. If buyers and sellers have the very same anonymous and linear price vector (λ) and buyers buy less than what the sellers sell, then makewhole payments are required, and BB is violated. To see this, assume that a seller sells a package of 2 MWh, and a buyer is interested in only 1 MWh. We have a nonconvexity arising from the indivisible package bid of the seller, which does not allow us to price one of the two megawatt-hours in the seller’s package at 0. Even if the buyer has a higher value for 1 MWh than what the seller asks for the package, we cannot achieve budget balance with a single price λ. Thus, the auctioneer needs to compensate the seller for the second megawatt-hour. But even if we have strict demandsupply equivalence, a PBE might not be possible, as the following example shows.

Example 2. Suppose there are generators G1 and G2 both asking for \$30 for 3 MWh. Buyer B1 wants to buy 4 MWh for \$20 in total, and buyer B2 is price inelastic with a demand of 2 MWh. With an ask price of \$10/MWh, the two generators ask for \$60 in total. However, as the market price cannot be higher than \$5/MWh, which is what B1 is willing to pay, the buyers will pay only \$30 for the 6 MWh in total. The ISO would need to pay a total of \$30 of make-whole payments to the two generators to facilitate the ef<sup>fi</sup>- cient trade at a price of \$5/MWh. The ISO could also set a different market price, but at any price, it is inevitable to compensate the losses of some of the market participants.

The ef<sup>fi</sup>cient trade would be possible only if the bids of the demand side are all higher than the average ask price or all buyers are price inelastic. As indicated, the latter is the standard assumption in the literature on electricity market design.

Definition 3. Buyer $i \in \mathcal { T }$ is price inelastic if for any bundle $x \in \mathcal { X } , v _ { i } ( x ) - \lambda ^ { \prime } x \geq 0$ for all $\lambda \in \mathbb { R } _ { \geq 0 } ^ { K }$ . Such a condition implies that, for any price vector $\lambda , \pi _ { i } ( x _ { i } , \lambda ) \geq 0$

Proposition 1. A combinatorial exchange can implement a PBE if the demand is price inelastic and demand equals supply.

Proof. We assume that we can solve the WDP to optimality, providing an ef<sup>fi</sup>cient allocation (EF), $( \mathbf { x } , \mathbf { y } ) =$ $( ( x _ { i } ) _ { i \in \mathcal { T } } , ( y _ { j } ) _ { j \in \mathcal { T } } )$ , such that $\begin{array} { r } { \sum _ { i \in \mathcal { T } } x _ { i } = \sum _ { j \in \mathcal { T } } y _ { j } } \end{array}$ . Furthermore, if we assume that all the buyers are price inelastic, we can choose a linear and anonymous price vector $\lambda ^ { * } =$ $( \lambda ^ { * } ( 1 ) , \ldots , \lambda ^ { * } ( K ) )$ large enough such that $\pi _ { i } ( x _ { i } , \lambda ^ { * } ) \geq 0$ for all $j \in \mathcal { I }$ . For example, one can set $\lambda ^ { * } ( k )$ as the highest average cost for item $k ,$ such that IR is satis<sup>fi</sup>ed for all generators. Finally, the condition $\begin{array} { r } { \sum _ { i \in \mathcal { T } } \lambda ^ { * ^ { \prime } } x _ { i } = \sum _ { j \in \mathcal { T } } \lambda ^ { * ^ { \prime } } y _ { j } } \end{array}$ gives us budget balance (BB). As a result, this combinatorial exchange can implement a PBE. Q.E.D.

With price-inelastic demand and strict demandsupply equivalence, we can increase the linear and anonymous price until we obtain IR for the generators. The same would hold true if some buyers are price sensitive but all their bids are higher than the average cost of the sellers. Because these conditions are rarely met on electricity markets, it is common to deviate from budget balance (BB) by providing makewhole payments that ensure individual rationality of the generators. We want these make-whole payments to be minimal, because such personalized payments are not re<sup>fl</sup>ected in the public market prices. Let us now de<sup>fi</sup>ne a penalty-based stable and ef<sup>fi</sup>cient outcome (PE).

Definition 4 (Penalty-Based Stable and Efficient Out come (PE)). A linear and anonymous market price vector $\lambda ^ { * } ,$ personalized make-whole payments ${ \bar { \delta } } _ { i } , \delta _ { j } ,$ and an ef<sup>fi</sup>cient allocation x, y form a penalty-based stable and ef<sup>fi</sup>cient outcome if $\pi _ { i } ( x _ { i } , \lambda ^ { * } ) + \delta _ { i } \geq 0 , \pi _ { j } ( y _ { j } ,$ $\lambda ^ { * } ) + \delta _ { j } \geq 0$ for every buyer $i \in \mathcal { T }$ and every seller $j \in { \mathcal { I } } .$ For PE prices, we demand the total of the personalized make-whole payments to be minimal.

Here, the make-whole payments compensate (aggregate) losses that result from the allocated bundle. As we will see, there can be different notions of make-whole payments on electricity markets, such as compensating item-level losses. Next, we will introduce optimization problems to compute PBE whenever it exists or PE otherwise.

## 5. Pricing Rules

For price computation, we want prices to be linear and anonymous, and we enforce ef<sup>fi</sup>ciency, whereas other design goals can be relaxed. We treat BB as <sup>fi</sup>rst-order design goal and price-based stability as second-order goal. This means that we <sup>fi</sup>rst aim for linear and anonymous prices, eliminating or minimizing the make-whole payments that the ISO needs to pay. Such prices better re<sup>fl</sup>ect the value of electricity compared with pricing schemes where the price signal is signi<sup>fi</sup>cantly distorted because of large private and personalized make-whole payments.

PBE (and also PE) prices are not unique. Therefore, we select those prices that minimize incentives to deviate. Unfortunately, these are computationally intractable problems if we want to compute them exactly, as we will show. In lieu thereof, we choose the price vector that is closest to the dual variables of the LP relaxation of the allocation problem. If the allocation problem were a convex optimization problem, such dual prices would constitute a competitive equilibrium (i.e., a stable solution that satis<sup>fi</sup>es EV).

Before we get to price computation, let us introduce an abstract version of the central allocation problem on electricity markets. Then, we introduce optimization models to compute prices on markets with priceinelastic demand and with price-sensitive demand to compute PBE and PE prices, respectively. Finally, we compare these pricing rules with other approaches in the literature.

## 5.1. Allocation Problem

In the last section, we have discussed combinatorial exchanges with package bidding, as they do not restrict the types of preferences that a participant might have. Combinatorial exchanges with package bids are impractical for electricity markets because they would require bidders to submit an exponential set of bids. Rather, electricity markets use compact bid languages (Goetzendorff et al. 2015) that only require generators to specify a small number of parameters describing their underlying cost functions and technical constraints as well as buyers to specify their bid curves.

Unit commitment (UC) problems represent our starting point. Operational constraints on thermal generation units such as ramping limits and minimum up-/downtimes require those units to be committed in advance of when they are needed, typically via day-ahead unit commitment. Unit commitment models determine the optimal scheduling of a given set of power suppliers in order to meet electricity demand. Such models minimize total system costs subject to market-clearing conditions (supply meets demand) and technical power plant constraints (Stott et al. 2009). Unit commitment models are generation scheduling models, determining the output of each generator. We use the term “securityconstrained unit commitment” model (SCUC) if it additionally includes network characteristics and constraints (Van den Bergh et al. 2014).

The SCUC problem can be formulated as a mixedinteger nonlinear problem. The nonlinearity comes from the fact that transmission lines are typically highvoltage alternating current (AC). An AC-optimal power-<sup>fl</sup>ow model (ACOPF) provides a nonlinear system that describes the energy <sup>fl</sup>ow through each transmission line accurately, and it is theoretically the best approach to solve the SCUC (Carpentier 1985). The ACOPF is nonlinear, nonconvex, and an NP-hard mixed-integer optimization problem (Zohrizadeh et al. 2020). Although there are various approaches to global optimization, an exact solution to the ACOPF can be considered intractable for realistic networks (Watson et al. 2015). This has led to signi<sup>fi</sup>cant research into convex relaxations of the problem (Zohrizadeh et al. 2020). The linear relaxation is also referred to as the direct current (DC) optimal power-<sup>fl</sup>ow model (DCOPF), and versions of this are widely used among U.S. ISOs to compute the ef<sup>fi</sup>cient dispatch and prices (Eldridge et al. 2017).

In our paper, we focus on pricing and thus assume a generic DCOPF model that is given by a mixed-integer linear program. Appendix A provides an overview of the notation. In the abstract formulation, buyers and generators/sellers are again denoted by the sets I and ${ \mathcal { I } } ,$ respectively. The set of traded goods K can now be described as the Cartesian product $\mathcal { N } \times \mathcal { T }$ , where $\mathcal { N }$ represents a set of network nodes and T a set of time periods. Nodes are connected through a set of transmission lines L. The objective of DCOPF aims at maximizing welfare, taking into account buyers’ valuations (v) and generators’ variable and <sup>fi</sup>xed costs (c and $h ,$ respectively). Both buyers (2) and generators (1) can specify constraint matrices A and G and Q and $R ,$ respectively, in order to communicate their preferences and feasible bundles. DC power <sup>fl</sup>ows ( f ) are determined in (3) (with P as the inverse matrix of the power transfer distribution factors and W and Z as mappings of buyers and sellers to their respective nodes), with a requirement of aggregate balance (4) and a consideration of line <sup>fl</sup>ow limits (5). The decision variables include buying (x) and selling (y) quantities, the associated binary variables (d and $u ) ,$ , as well as power <sup>fl</sup>ows ( f ). As indicated by the integer multipliers r and $s ,$ the binary variables d and u can account for several categories such as start-up and commitment variables for generators:

$$
\max _ { \begin{array}{c} x, y, u, d, f \\ \text {s.t.} \end{array} } v ^ {\prime} x - c ^ {\prime} y - h ^ {\prime} u
$$

$$
A y + G u \geq b,\tag{DCOPF}
$$

(1)

$$
Q x + R d \leq e,\tag{2}
$$

$$
P f = W y - Z x,\tag{3}
$$

$$
\overline {{W}} y - \overline {{Z}} x = 0,\tag{4}
$$

$$
\underline {{F}} \leq f \leq \overline {{F}},\tag{5}
$$

$$
x \geq 0,\tag{6}
$$

$$
y \geq 0,\tag{7}
$$

$$
u \in \{0, 1 \} ^ {s J T},\tag{8}
$$

$$
d \in \{0, 1 \} ^ {r I T},\tag{9}
$$

$$
f \in \mathbb {R} ^ {L T}.\tag{10}
$$

For convenience, we de<sup>fi</sup>ne vector $x _ { i }$ to include only the buying quantities of buyer $i \in \mathcal { T }$ as nonzero components $( { \mathrm { i . e . , ~ } } \sum _ { i \in \mathcal { T } } x _ { i } = x )$ . Similarly, we de<sup>fi</sup>ne the vectors $d _ { i } ,$ $y _ { j \prime }$ and $u _ { j }$ for buyers $i \in \mathcal { T }$ and generators $j \in \mathcal { I }$ . The utility of buyer i is then de<sup>fi</sup>ned as $\pi _ { i } ( x _ { i } , \lambda ) = v ^ { \prime } x _ { i } - \lambda ^ { \prime } Z x _ { i } ,$ with λ being the market price vector. The utility of generator j is $\pi _ { j } ( y _ { j } , \lambda ) = \lambda ^ { \prime } W y _ { j } - c ^ { \prime } y _ { j } - h ^ { \prime } u _ { j }$ . Similarly, $x _ { t }$ and $y _ { t }$ are the vectors containing the buying and selling quantities of all buyers and generators, respectively, in period $t \in \tau$ as nonzero components. The vectors $x _ { i t }$ and $y _ { j t }$ consequently only include one nonzero component— namely, the particular quantity of buyer i and generator $j ,$ respectively, in period t.

The DCOPF model does not allow for nonlinear costs or nonlinear AC power <sup>fl</sup>ows. We also abstract from transmission network elements such as transformers, shunts, or auxiliary services. However, the DCOPF formulation provides the overall structure of an MIP used for unit commitment problems; this allows us to perform a meaningful analysis of different pricing rules in our experiments in Section 6.

## 5.2. PBE Pricing with Price-Inelastic Demand

We <sup>fi</sup>rst focus on the case of price-inelastic demand. This complies with the traditional notion of electricity as a basic and indispensable necessity. If demand x has no attached valuations, $v ^ { \prime } x$ can be removed from the objective function of DCOPF, and the generators cost will be minimized. Demand <sup>fl</sup>exibility can be taken into account (by Constraint (2)), as long as buyers are price inelastic. Let $x ^ { * } , u ^ { * } , y ^ { * } , d ^ { * } ,$ , and $f ^ { * }$ denote the optimal solutions to this modi<sup>fi</sup>ed problem, which is ef<sup>fi</sup>cient with demand-supply equivalence. As the buyers are price inelastic, there will always be a price pro<sup>fi</sup>le $\hat { \lambda } ^ { P B E } \in \mathbb { R } _ { \ge 0 } ^ { N T }$ over locations and time periods such that no generator incurs losses (see Proposition 1).

The following bilevel integer program, PBE-P, computes prices such that at the ef<sup>fi</sup>cient dispatch no generator makes a loss at any time (<sup>fi</sup>rst constraint) and that there are no negative congestion revenues (second constraint). The latter prevents that nodal prices are set low at demand-intensive nodes and high at supply-intensive nodes, implying missing money only as a result of nodal price discrepancies. In the <sup>fi</sup>rst constraint, individual rationality is based on hourly losses incurred by the respective market participant. Even if a loss in a certain hour is offset by a higher gain in the subsequent hour, the loss is compensated by a make-whole payment. The third constraint makes sure that incentives for generators to deviate from the ef<sup>fi</sup>cient solution are minimal. The term $\pi _ { j }$ describes the payoff that a generator $j \in \mathcal { I }$ would have at the prices λ if she could choose her dispatch such that it maximizes her payoff. The latter is computed in the lower-level optimization (fourth constraint). This model would lead to prices that are IR and BB, and it would minimize the gains by deviating from the ef<sup>fi</sup>cient solution by an individual. In a Walrasian equilibrium of a convex economy, coalitions of market participants also cannot deviate. We do not consider such blocking coalitions in this model:

$$
\begin{array}{l l} \min _ {\lambda , \pi , \gamma} & \sum_ {j \in \mathcal {J}} \gamma_ {j} \\ \text {s.t.} & \\ & \lambda^ {\prime} W y _ {j t} ^ {*} - c ^ {\prime} y _ {j t} ^ {*} - h ^ {\prime} u _ {j t} ^ {*} \geq 0 & \forall j \in , t \in \mathcal {T} \\ & \lambda^ {\prime} Z x ^ {*} - \lambda^ {\prime} W y ^ {*} \geq 0 \\ & \pi_ {j} - (\lambda^ {\prime} W y _ {j} ^ {*} - c ^ {\prime} y _ {j} ^ {*} - h ^ {\prime} u _ {j} ^ {*}) \leq \gamma_ {j} & \forall j \in \mathcal {J} \\ & \pi_ {j} = \max _ {y, u} (\lambda^ {\prime} W y _ {j} - c ^ {\prime} y _ {j} - h ^ {\prime} u _ {j}) & \text {s.t. (1),(7),(8)} \\ & & \forall j \in \mathcal {J}, \\ & \lambda \in \mathbb {R} _ {\geq 0} ^ {N T}, \pi \in \mathbb {R} _ {\geq 0} ^ {J}, \gamma \in \mathbb {R} ^ {J}. \end{array}\tag{PBE-P}
$$

Solving bilevel mixed integer programming problems is $\Sigma _ { 2 } ^ { p } \mathrm { . }$ -hard (Jeroslow 1985), a complexity class that is clearly intractable. Although this is no proof that the speci<sup>fi</sup>c problem PBE-P is in this complexity class, realistic problem sizes of PBE-P are very large, and the problems need to be solved in due time. For example, the time to compute allocation and pricing in European day-ahead markets is only 17 minutes (All NEMO Committee 2021).<sup>6</sup>

Given the associated practical complexity of solving PBE-P in the required time frames, we suggest an alternative based on ELMP, which will be described in Section 5.4.2 in greater detail. In essence, ELMP is a tractable heuristic where binary variables of the DCOPF (Constraints (8) and (9)) are relaxed to continuous vari ables and prices are retrieved from the duals of the nodal demand-supply constraints. ELMP aims at minimizing lost opportunity costs, and if a market is convex, it actually does. Therefore, instead of PBE-P, we solve PBE-A. The latter omits the lower-level optimization and instead minimizes the difference between the price vector that satis<sup>fi</sup>es the individual rationality constraints (λ) and the ELMP prices $( \lambda ^ { \mathrm { E L M P } } )$ ). Note that ELMP is computed by a linear program, and therefore $\lambda ^ { \mathrm { E L M P } }$ can be computed effectively with state-of-the-art linear programming solvers (see numerical results in Section 6.2):

$$
\begin{array}{l l} \min _ {\lambda} & \| \lambda - \lambda^ {\text { ELMP }} \| _ {1} \\ \text { s.t. } & \\ & \lambda^ {\prime} W y _ {j t} ^ {*} - c ^ {\prime} y _ {j t} ^ {*} - h ^ {\prime} u _ {j t} ^ {*} \geq 0 \quad \forall j \in \mathcal {J}, t \in \mathcal {T}, \\ & \lambda^ {\prime} Z x ^ {*} - \lambda^ {\prime} W y ^ {*} \geq 0, \\ & \lambda \in \mathbb {R} _ {\geq 0} ^ {N T}. \end{array} \tag {PE}\tag{PBE-A}
$$

Here, we use $\lVert \lambda - \lambda ^ { \mathrm { E L M P } } \rVert _ { 1 }$ in an attempt to minimize incentives to deviate from the ef<sup>fi</sup>cient dispatch. With an $L _ { 1 }$ norm in the objective, PBE-A can also be modeled as a linear program that can be solved in polynomial time. One can also minimize the squared Euclidean norm, which makes this a quadratic problem that might lead to less variation in the components of the price vector. Wolfe’s combinatorial algorithm is widely used to solve such problems. Even though this algorithm does not run in polynomial time in the worst case (De Loera et al. 2020), it is very effective in practice and can serve as an alternative.

## 5.3. PE Pricing with Price-Sensitive Demand

We now assume price-sensitive demand—that is, some or all of the buyers submit valuations v—as represented by the DCOPF. As we have shown, a PBE does not always exist for DCOPF. We can sacri-<sup>fi</sup>ce budget balance (BB) but still ensure EF and IR. As a result, market prices are still linear and anonymous (LA), but individual payments are not (no LAP). Let $x ^ { * } , y ^ { * } , u ^ { * } , d ^ { * } f ^ { * }$ be the optimal solution to DCOPF. We de<sup>fi</sup>ne the following problem to compute the minimal make-whole payments associated to a price vector λ:

$$
\begin{array}{r l} \min _ {\lambda , \delta^ {\mathcal {I}}, \delta^ {\mathcal {J}}} & \| \delta^ {\mathcal {I}} \| _ {1} + \| \delta^ {\mathcal {J}} \| _ {1} \\ \text {s.t.} & v ^ {\prime} x _ {i t} ^ {*} - \lambda^ {\prime} Z x _ {i t} ^ {*} + \delta_ {i t} ^ {\mathcal {I}} \geq 0 \quad \forall i \in \mathcal {J}, t \in \mathcal {T} \\ & \lambda^ {\prime} W y _ {j t} ^ {*} - c ^ {\prime} y _ {j t} ^ {*} - h ^ {\prime} u _ {j t} ^ {*} + \delta_ {j t} ^ {\mathcal {I}} \geq 0 \quad \forall j \in \mathcal {I}, t \in \mathcal {T}, \\ & \lambda^ {\prime} Z x ^ {*} - \lambda^ {\prime} W y ^ {*} \geq 0, \\ & \lambda \in \mathbb {R} _ {\geq 0} ^ {N T}, \delta^ {\mathcal {I}} \in \mathbb {R} _ {\geq 0} ^ {I T}, \delta^ {\mathcal {J}} \in \mathbb {R} _ {\geq 0} ^ {J T}. \end{array}\tag{PE- \( \alpha \)}
$$

The variables $\delta ^ { \underline { { \tau } } }$ and $\delta ^ { \mathcal { I } }$ represent the required make-whole payments to buyers I and generators ${ \mathcal { I } } ,$ respectively. Note that we again consider hourly losses for the calculation of make-whole payments, which slightly extends the requirements for makewhole payments compared with De<sup>fi</sup>nition 4 (which only asks for no aggregate losses over all hours). The optimal make-whole payments from PE-α are given as $\delta ^ { \mathcal { T } * }$ and $\delta ^ { \mathcal { I } * }$ . Again, the resulting price vectors are not unique, and we could formulate a bilevel integer program aiming to satisfy individual rationality and to minimize incentives to deviate to another

dispatch at these prices:

$$
\begin{array}{l l} \min _ {\lambda , \pi , \gamma , \delta^ {\mathcal {I}}, \delta^ {\mathcal {J}}} & \sum_ {i \in \mathcal {I}} \gamma_ {i} + \sum_ {j \in \mathcal {J}} \gamma_ {j} \\ \text {s.t.} & \\ & v ^ {\prime} x _ {i t} ^ {*} - \lambda^ {\prime} Z x _ {i t} ^ {*} + \delta_ {i t} ^ {\mathcal {I}} \geq 0 \quad \forall i \in \mathcal {I}, t \in \mathcal {T}, \\ & \lambda^ {\prime} W y _ {j t} ^ {*} - c ^ {\prime} y _ {j t} ^ {*} - h ^ {\prime} u _ {j t} ^ {*} + \delta_ {j t} ^ {\mathcal {I}} \geq 0 \quad \forall j \in \mathcal {J}, t \in \mathcal {T}, \\ & \lambda^ {\prime} Z x ^ {*} - \lambda^ {\prime} W y ^ {*} \geq 0, \\ & \delta^ {\mathcal {I}} = \delta^ {\mathcal {I} *}, \\ & \delta^ {\mathcal {J}} = \delta^ {\mathcal {J} *}, \\ & \pi_ {i} - (v ^ {\prime} x _ {i} ^ {*} - \lambda^ {\prime} Z x _ {i} ^ {*}) \leq \gamma_ {i} \quad \forall i \in \mathcal {I}, \\ & \pi_ {i} = \underset {x, d} {\max} (v ^ {\prime} x _ {i} - \lambda^ {\prime} Z x _ {i}) \quad \text {s.t. (2),(6),(9)} \\ & \forall i \in \mathcal {I}, \\ & \pi_ {j} - (\lambda^ {\prime} W y _ {j} ^ {*} - c ^ {\prime} y _ {j} ^ {*} - h ^ {\prime} u _ {j} ^ {*}) \leq \gamma_ {j} \quad \forall j \in \mathcal {J}, \\ & \pi_ {j} = \underset {y, u} {\max} (\lambda^ {\prime} W y _ {j} - c ^ {\prime} y _ {j} - h ^ {\prime} u _ {j}) \\ & \text {s.t. (1),(7),(8)} \quad \forall j \in \mathcal {J}, \\ & \lambda \in \mathbb {R} _ {\geq 0} ^ {N T}, \pi \in \mathbb {R} _ {\geq 0} ^ {I + J}, \gamma \in \mathbb {R} ^ {I + J}, \delta^ {\mathcal {I}} \in \mathbb {R} _ {\geq 0} ^ {I T}, \delta^ {\mathcal {J}} \in \mathbb {R} _ {\geq 0} ^ {J T}. \\ & (\mathrm{Re}, R) \end{array}\tag{PE-P}
$$

Similar to our discussion on the case with priceinelastic demand, we replace the bilevel integer program with a tractable linear program that minimizes the distance to ELMP prices, subject to having the minimal make-whole payments given by PE-α:

$$
\begin{array}{l l} \min _ {\lambda , \delta^ {\mathcal {I}}, \delta^ {\mathcal {J}}} & \| \lambda - \lambda^ {\text {ELMP}} \| _ {1} \\ \text {s.t.} & v ^ {\prime} x _ {i t} ^ {*} - \lambda^ {\prime} Z x _ {i t} ^ {*} + \delta_ {i t} ^ {\mathcal {I}} \geq 0 \qquad \forall i \in \mathcal {I}, t \in \mathcal {T}, \\ & \lambda^ {\prime} W y _ {j t} ^ {*} - c ^ {\prime} y _ {j t} ^ {*} - h ^ {\prime} u _ {j t} ^ {*} \geq 0 \qquad \forall j \in \mathcal {J}, t \in \mathcal {T}, \\ & \lambda^ {\prime} Z x ^ {*} - \lambda^ {\prime} W y ^ {*} \geq 0, \\ & \delta^ {\mathcal {I}} = \delta^ {\mathcal {I} *}, \\ & \delta^ {\mathcal {J}} = \delta^ {\mathcal {J} *}, \\ & \lambda \in \mathbb {R} _ {\geq 0} ^ {N T}, \delta^ {\mathcal {I}} \in \mathbb {R} _ {\geq 0} ^ {I T}, \delta^ {\mathcal {J}} \in \mathbb {R} _ {\geq 0} ^ {J T}. \end{array}\tag{PE-A}
$$

This basic formulation of PE-A (as well as PBE-A) might lead to prices that differ among nodes even though there is no congestion in the transmission net work. With a few additional constraints, one can make sure that two adjacent nodes have the same price if there is no congestion. For this purpose, one only has to add price equivalence constraints for edges adjacent to those nodes where there is no congestion. In our experimental evaluation, we observed that such constraints modify the price pro<sup>fi</sup>le and increase the necessary make-whole payments, yet the make-whole payments required by PE-A are still signi<sup>fi</sup>cantly lower compared with alternative pricing rules.

## 5.4. Comparison with Existing Pricing Rules

There is a signi<sup>fi</sup>cant literature on pricing rules for electricity spot markets; a detailed discussion of all proposals is beyond the scope of this paper. An excellent and up-to-date overview of pricing in electricity markets is provided by Liberopoulos and Andrianesis (2016). Note that the literature in their paper is entirely based on the assumption of price-inelastic demand.

In our discussion, we focus on IP pricing and ELMP because they are used by U.S. ISOs in practice. Furthermore, we consider AIC pricing, a recent proposal that also addresses the problem of signi<sup>fi</sup>cant make-whole payments. As introduced earlier, relevant criteria are EF, IR, BB, LA, and LAPs. Note that IP pricing, ELMP, and AIC satisfy EF and IR, which are widely considered essential on electricity markets. With price-inelastic demand, PBE-A provides a straightforward way to guarantee BB and LAP. In the case of price-sensitive demand, PE-A is the only pricing rule that minimizes make-whole payments under linear and anonymous prices. Let us now provide a brief description of IP, ELMP, and AIC pricing.

5.4.1. IP Pricing. IP pricing (O’Neill et al. 2005) was an early and widely adopted proposal for pricing on electricity markets. First, the ef<sup>fi</sup>cient dispatch is computed via DCOPF. Then the integer variables are <sup>fi</sup>xed to their optimal values, resulting in a linear program. The duals of the nodal balance constraints provide linear and anonymous market prices, while the duals associated to constraints with integer variables determine individual uplift payments. O’Neill et al. (2005) originally describe a problem with price-inelastic demand. IP pricing can, however, also be adapted to settings with price-sensitive demand (Madani et al. 2018). It was also extended to multiperiod, multinodal markets in many U.S. ISOs, including CAISO, PJM, or SPP. In practice, the uplift payments are restricted to be nonnegative make-whole payments. Thus, market participants can retain their pro<sup>fi</sup>ts, and only individual losses are compensated by make-whole payments to ensure individual rationality. Budget balance is violated as a result of the make-whole payments, and the prices do not constitute a competitive equilibrium.

5.4.2. ELMP Pricing. ELMP relaxes binary variables of the DCOPF to continuous variables and takes the duals of the relaxed problem as market prices. MISO introduced ELMP in 2011, but similar approaches were implemented by ISO New England (O’Neill et al. 2019). Similar to IP pricing, there are individual makewhole payments, and the stability of the solution is enforced via penalties. Lost opportunity costs (LOCs)

describe the forgone pro<sup>fi</sup>t from the most pro<sup>fi</sup>table alternative level of electricity production at the prices. In total, the make-whole payments and the required penalties yield the LOCs of a generator. ELMP pricing represents an approximation of convex hull pricing (CHP), as introduced by Gribik et al. (2007). CHP computes prices that indeed minimize LOCs, but it is computationally expensive and thus has not been implemented in the <sup>fi</sup>eld (Schiro et al. 2016). However, for simple problem formulations, ELMP and CHP prices are equivalent (Hua and Baldick 2017). Evidence by MISO suggests that lost opportunity costs can be reduced by ELMP pricing compared with IP pricing, yet the general economic properties of ELMP remain unclear (Schiro et al. 2016).

5.4.3. AIC Pricing. In a series of essays, O’Neill et al. (2019) challenge established pricing rules on electricity markets and criticize that the resulting make-whole payments lead to biased market prices. They suggest AIC pricing, which implements IP pricing as a <sup>fi</sup>rst stage. In a second step, the AIC price computation relaxes the integer variables of generators that make a loss for the actual AIC pricing run and adjusts their objective function coef<sup>fi</sup>cients to re<sup>fl</sup>ect the average costs; that is, it distributes the <sup>fi</sup>xed costs of a generator over the quantity allocated to the generator. In a stylized market with only a single period, this would eliminate the make-whole payments of the generators. In a market with multiple periods, O’Neill et al. (2020) suggest an iterative process comprising several pricing runs to achieve budget balance. The approach does not consider make-whole payments for the demand side but proposes price differentiation among buyers via Ramsey–Boiteux-like pricing.

AIC pricing provides an innovative new approach to electricity market pricing. Similar to PBE-A or PE-A, the goal is to eliminate or minimize make-whole payments. But there are also differences. First, PE-A minimizes make-whole payments for both sides of the market in a single optimization. Second, unlike AIC pricing, PE-A does not involve price differentiation on the demand side but sticks to linear and anonymous prices. Price differentiation among buyers can be a very useful tool to deal with the nonconvexities in a market. However, it is also challenging. First, personalized prices lead to some level of intransparency in the market compared with an anonymous linear price for all market participants. Again, not all information is contained in the public price signal. Second, there is a difference between differential and anonymous prices in terms of manipulability. Uniform multiunit auctions and the Walrasian mechanism are known to be strategy-proof in the large (Azevedo and Budish 2019). This means that with many participants, truthtelling is approximately optimal, and the impact of a single participant on the price becomes negligible with many participants. This is no longer the case if the payments of a participant are personalized. A pay-as-bid pricing scheme is manipulable, and bidders will not reveal their true preferences. The only exception is the Vickrey-Clarke-Groves payment rule, which is the unique payment rule that is dominant-strategy incentive compatible (Green and Laffont 1979).

Table 1. Base Case: Convex Supply

<table><tr><td></td><td>G1</td><td>G2</td></tr><tr><td>Max load (MW)</td><td>15</td><td>20</td></tr><tr><td>Offer price ($/MWh)</td><td>5</td><td>3</td></tr></table>

In our experiments we show that the make-whole payments necessary to achieve linear and anonymous prices are negligible even with price-sensitive demand. We argue that if make-whole payments are so low, there is no need to restrict to discriminatory prices for each buyer or many anonymous but nonlinear prices (say, for different volumes of electricity demanded), because the market price includes “almost” all information about supply and demand.

For our experiments in Section 6, we will ignore price differentiation in AIC but instead compute make-whole payments to allow for a comparison with other pricing rules. Besides, we consider only a single AIC pricing run, and not multiple iterations.

5.4.4. Alternative Proposals. Various other pricing rules have been suggested in the past two decades. Some, such as direct minimum uplift (DMU) pricing, refrain from linear and anonymous prices and are thus beyond the focus of this paper. Others, such as the equilibrium-constrained (EC) pricing framework by Azizan et al. (2020) are restricted to price-inelastic demand. Moreover, many rules have been investigated only under very speci<sup>fi</sup>c assumption (e.g., generalized uplift pricing, semi-Lagrangean pricing).

Toczyłowski and Zoltowska (2009) introduce the DMU approach, which postulates a bid-ask spread between the market prices for buyers and generators. DMU pricing aims to <sup>fi</sup>nd a spread that allows for minimal side payments and that compensates lost opportunity costs. The side payments are designed as uniform per-unit payments for buyers and sellers. However, the ISO has to give up a single linear price vector. DMU pricing has been proposed for multiperiod power <sup>fl</sup>ow problems with price-sensitive demand.

Table 2. Base Case: Price-Inelastic Demand

<table><tr><td>Hour</td><td>B1 (MWh)</td><td>B2 (MWh)</td></tr><tr><td> $t = 1$ </td><td>4</td><td>3</td></tr><tr><td> $t = 2$ </td><td>6</td><td>6</td></tr><tr><td> $t = 3$ </td><td>10</td><td>12</td></tr></table>

Table 3. Base Case: Dispatch

<table><tr><td>Hour</td><td>G1 (MWh)</td><td>G2 (MWh)</td><td>B1 (MWh)</td><td>B2 (MWh)</td></tr><tr><td> $t = 1$ </td><td>0</td><td>7</td><td>4</td><td>3</td></tr><tr><td> $t = 2$ </td><td>0</td><td>12</td><td>6</td><td>6</td></tr><tr><td> $t = 3$ </td><td>2</td><td>20</td><td>10</td><td>12</td></tr></table>

More recently, Azizan et al. (2020) propose the EC pricing scheme that is applicable to general nonconvex settings with price-inelastic demand. Dispatch and pay ments are determined simultaneously to achieve EF and IR, as well as to ensure no incentives to deviate, rendering penalties unnecessary. Consequently, the price and payment functions must be general enough and hence allow for nonlinear and personalized components. One upside is the broad applicability of their pricing framework to established price and payment functions. Moreover, the authors provide a polynomial-time approximation algorithm for general nonconvex cost functions. The authors do not account for price-sensitive demand. Therefore, their settings are restricted to those where a PBE is feasible. In contrast to PBE-A, equilibrium-constrained pricing gives up budget balance and linear and anonymous payment functions to ensure stability without further penalties. Similar to O’Neill et al. (2019), we instead argue for maintaining budget balance with linear and anonymous payments and treat lost opportunity costs as a secondary objective. In regulated electricity markets, penalties are an accepted means to achieve stability.

Generalized uplift pricing, introduced by Motto and Galiana (2002) and Galiana et al. (2003), has been proposed for a single-period problem with price-inelastic demand and seeks to <sup>fi</sup>nd minimum zero-sum uplift payments that ensure stability. Minimum zero-sum uplift pricing by Liberopoulos and Andrianesis (2016) seeks the minimum prices that ensure a PBE. In contrast to PBE-A, minimum zero-sum uplift pricing allows for uplift charges for pro<sup>fi</sup>table generators. Starting at marginal cost, it increases prices and redistributes the additional gains of pro<sup>fi</sup>table generators to the loss-making generators. It terminates as soon as individual rationality is ensured for every generator. The semi-Lagrangean pricing scheme by Araoz and Jornsten (¨ 2011) also achieves a PBE, but their formulation is restricted to price-inelastic demand. The primal-dual pricing rule by Ruiz et al. (2012) aims at uniform IR prices with priceinelastic demand by relaxing ef<sup>fi</sup>ciency. Finally, O’Neill et al. (2016) introduce the dual pricing algorithm, which starts with the dual of the IP pricing problem and adds restrictions to ensure individual rationality and budget balance. By employing Ramsey–Boiteux pricing, it results in personalized prices for buyers. In Section 6 we will focus only on IP pricing, ELMP, and AIC pricing for the reasons already mentioned.

Table 4. Base Case: Prices

<table><tr><td>Hour</td><td>IP($/MWh)</td><td>ELMP($/MWh)</td><td>AIC($/MWh)</td><td>PBE-A($/MWh)</td></tr><tr><td> $t = 1$ </td><td>3.00</td><td>3.00</td><td>3.00</td><td>3.00</td></tr><tr><td> $t = 2$ </td><td>3.00</td><td>3.00</td><td>3.00</td><td>3.00</td></tr><tr><td> $t = 3$ </td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td></tr><tr><td>MWP ($)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

Note. MWP states the total make-whole payments implied by each pricing rule.

Table 5. Nonconvexities: Dispatch

<table><tr><td>Hour</td><td>G1 (MWh)</td><td>G2 (MWh)</td><td>B1 (MWh)</td><td>B2 (MWh)</td></tr><tr><td> $t = 1$ </td><td>7</td><td>0</td><td>4</td><td>3</td></tr><tr><td> $t = 2$ </td><td>2</td><td>10</td><td>6</td><td>6</td></tr><tr><td> $t = 3$ </td><td>2</td><td>20</td><td>10</td><td>12</td></tr></table>

## 6. Numerical Experiments

In what follows, we compare the different pricing rules experimentally. We start with small illustrative examples before we report aggregate results for the IEEE RTS-96 system, which is frequently used as a benchmark.

## 6.1. Illustrative Examples

In our illustrative examples we go from simple to more complex environments. We start with a simple convex setting consisting of two generators, G1 and G2, and two buyers, B1 and B2, at a single node and over three time periods (i.e., hours). We will gradually extend this example to re<sup>fl</sup>ect nonconvexities as well as price-sensitive and <sup>fl</sup>exible demand-side bids. We will benchmark IP and ELMP pricing as established rules used by ISOs and further include AIC pricing as a promising rule that has not yet been employed in practice; these existing rules are compared with PBE-A and PE-A, respectively.

6.1.1. Base Case: Convex Supply, Price-Inelastic Demand. Generator G1 offers up to 15 MW for \$5/ MWh, and G2 offers up to 20 MW for \$3/MWh (see Table 1). Buyers B1 and B2 schedule price-inelastic demand according to Table 2.

Table 6. Nonconvexities: Prices

<table><tr><td>Hour</td><td>IP($/MWh)</td><td>ELMP($/MWh)</td><td>AIC($/MWh)</td><td>PBE-A($/MWh)</td></tr><tr><td>t = 1</td><td>5.00</td><td>3.50</td><td>6.14</td><td>6.14</td></tr><tr><td>t = 2</td><td>3.00</td><td>3.50</td><td>3.00</td><td>9.00</td></tr><tr><td>t = 3</td><td>5.00</td><td>6.10</td><td>9.00</td><td>9.00</td></tr><tr><td>MWP ($)</td><td>38.00</td><td>40.29</td><td>22.00</td><td>0.00</td></tr></table>

Note. MWP states the total make-whole payments implied by each pricing rule.

Table 7. Price-Sensitive Demand: Dispatch

<table><tr><td>Hour</td><td>G1 (MWh)</td><td>G2 (MWh)</td><td>B1 (MWh)</td><td>B2 (MWh)</td></tr><tr><td> $t = 1$ </td><td>5.5</td><td>0</td><td>4</td><td>1.5</td></tr><tr><td> $t = 2$ </td><td>2</td><td>10</td><td>6</td><td>6</td></tr><tr><td> $t = 3$ </td><td>2</td><td>14</td><td>10</td><td>6</td></tr></table>

The optimal solution is obviously to let G2 satisfy the entire demand in the <sup>fi</sup>rst two periods, as G1 satis<sup>fi</sup>es only the residual demand of 2 MWh in excess of the maximum load of G2 in the third period, as shown in Table 3. IP, ELMP, AIC, and PBE-A prices are identically set (see Table 4) and constitute a WE, PBE, and PE.

6.1.2. Nonconvexities. In Tables 5 and 6, we introduce nonconvexities for the generators; that is, G1 has a minimum load of 2 MW per period as well as no-load costs of \$8 that occur as <sup>fi</sup>xed costs when G1 is committed. G2 has a minimum load of 10 MW and no-load costs of \$10. Therefore, G2 can no longer satisfy the demand in the <sup>fi</sup>rst period and is replaced by G1. It is also assumed that G1 requires a minimum runtime of three periods. That is, if G1 is committed, it must sell at least its minimum load in every period. Consequently, the optimal dispatch now involves G1 satisfying the entire demand in t 1 and running at a minimum load in the remaining periods, whereas G2 satis<sup>fi</sup>es the residual demand.

Neither pricing rule yields a WE. IP, ELMP, and AIC result in individual losses, at least for some of the hours, and thus fail to produce a PBE. PBE-A avoids any make-whole payments and yields a PBE. Even if the aggregate pro<sup>fi</sup>ts were considered, AIC pricing cannot ensure individual rationality, at least after a single pricing run.

6.1.3. Price-Sensitive Demand. We now introduce price-sensitive demand in Tables 7 and 8. We assume that half of the price-inelastic demand is retained as price inelastic. For the remaining half, B1 bids \$10/MWh and B2 bids \$2/MWh in each period. The dispatch thus changes, as it is not welfare optimal to satisfy the entire demand. Because of the price-sensitive demand, we now use PE-A instead of PBE-A.

Table 8. Price-Sensitive Demand: Prices

<table><tr><td>Hour</td><td>IP($/MWh)</td><td>ELMP($/MWh)</td><td>AIC($/MWh)</td><td>PE-A($/MWh)</td></tr><tr><td>t = 1</td><td>5.00</td><td>3.50</td><td>6.45</td><td>6.45</td></tr><tr><td>t = 2</td><td>2.00</td><td>3.50</td><td>4.00</td><td>4.17</td></tr><tr><td>t = 3</td><td>3.00</td><td>3.50</td><td>3.71</td><td>8.58</td></tr><tr><td>MWP ($)</td><td>64.00</td><td>50.75</td><td>26.57</td><td>17.00</td></tr></table>

Note. MWP states the total make-whole payments implied by each pricing rule.

Table 9. Flexible Demand I: Dispatch

<table><tr><td>Hour</td><td>G1 (MWh)</td><td>G2 (MWh)</td><td>B1 (MWh)</td><td>B2 (MWh)</td></tr><tr><td> $t = 1$ </td><td>3.5</td><td>0</td><td>2</td><td>1.5</td></tr><tr><td> $t = 2$ </td><td>2</td><td>10</td><td>8</td><td>4</td></tr><tr><td> $t = 3$ </td><td>2</td><td>14</td><td>10</td><td>6</td></tr></table>

Under the welfare-optimal dispatch, no PBE is possible. In order to satisfy the price-inelastic fraction of demand, both generators need to produce at least at their minimum loads, and make-whole payments thus become inevitable. PE-A achieves the lowest aggregate make-whole payments (\$10.50 to G1 and \$6.50 to B2), which are as close to budget balance as possible.

6.1.4. Flexible Demand. We now additionally convert some of the in<sup>fl</sup>exible demand into <sup>fl</sup>exible demand. Buyer B1 has converted 2 MWh from t 1 and 1 MWh from t 2 into a shiftable volume of 3 MWh that can be satis<sup>fi</sup>ed in an arbitrary pattern over the considered time frame (see Table 9).

The shiftable volume of B1 is completely served in t 2 and replaces some of the price-sensitive demand of B2. This allows for a signi<sup>fi</sup>cant reduction in makewhole payments for PE-A (see Table 10). Assume now that B1 adds an additional 1 MWh from t 2 to the shiftable volume; making use of this <sup>fl</sup>exibility allows for PBE prices (see Tables 11 and 12).

This example also illustrates the advantages of demand-side bidding and bid languages that permit the expression of <sup>fl</sup>exibility dimensions.

6.2. Experiments Based on the IEEE RTS-96 System Finally, we report results of numerical experiments based on the IEEE RTS-96 system introduced by Grigg et al. (1999) in order to better understand prices in a larger and realistic test system. This system has been used in a variety of studies on electricity markets (Garcia-Bertrand et al. 2006, Morales et al. 2009, Zoltowska 2016, Hytowitz et al. 2020, Zocca and Zwart 2021) and includes nonconvexities (no-load costs, minimum loads, minimum runtimes), price-sensitive demand, as well as several nodes and time periods. Therefore, it is well suited to study prices and make-whole payments under different pricing schemes.

Table 10. Flexible Demand I: Prices

<table><tr><td>Hour</td><td>IP($/MWh)</td><td>ELMP($/MWh)</td><td>AIC($/MWh)</td><td>PE-A($/MWh)</td></tr><tr><td>t = 1</td><td>5.00</td><td>3.50</td><td>7.29</td><td>7.29</td></tr><tr><td>t = 2</td><td>2.00</td><td>3.50</td><td>4.00</td><td>9.00</td></tr><tr><td>t = 3</td><td>3.00</td><td>3.50</td><td>3.71</td><td>9.00</td></tr><tr><td>MWP ($)</td><td>64.00</td><td>44.75</td><td>22.57</td><td>7.00</td></tr></table>

Note. MWP states the total make-whole payments implied by each pricing rule.

Table 11. Flexible Demand II: Dispatch

<table><tr><td>Hour</td><td>G1 (MWh)</td><td>G2 (MWh)</td><td>B1 (MWh)</td><td>B2 (MWh)</td></tr><tr><td> $t = 1$ </td><td>3.5</td><td>0</td><td>2</td><td>1.5</td></tr><tr><td> $t = 2$ </td><td>7</td><td>0</td><td>4</td><td>3</td></tr><tr><td> $t = 3$ </td><td>2</td><td>18</td><td>14</td><td>6</td></tr></table>

Grigg et al. (1999) provide a stylized system topology, transmission network parameters, hourly (nodal) demand data, as well as characteristics of generating units. In accordance with Zoltowska (2016), we select the single-area, 24-node topology by Grigg et al. (1999) for a representative 24-hour winter day with 32 generators (total capacity of 6.81 GW) and 17 consumers (average hourly demand of 2.60 GWh). For data on (nonconvex) generation costs or demand valuations, we rely on the bid and offer curves provided by the cases studies of Garcia-Bertrand et al. (2006) and Zoltowska (2016) on this system. The experiments were conducted on an Intel<sup>VR</sup> Core<sup>TM</sup> i7-8565U CPU with 16 GB RAM.

Our base setting includes 32 generators with minimum and maximum loads, minimum runtimes, as well as no-load costs and an offer curve representing variable costs. The demand of the 17 consumers is assumed to be price inelastic at <sup>fi</sup>rst and later extended to price-sensitive and <sup>fl</sup>exible demand. Generators and consumers are embedded in a DC power <sup>fl</sup>ow model with 24 nodes. Appendix C provides heat maps of the hourly nodal prices, and Table 13 reports statistics on prices, make-whole payments (MWPs), as well as the magnitude of penalties necessary to avoid generators to deviate from the ef<sup>fi</sup>cient dispatch. Note that instead of penalties an ISO could also just prohibit deviations from the ef<sup>fi</sup>cient dispatch. In all scenarios we will see that the make-whole payments for PBE-A (in case of price-inelastic demand) or PE-A (in case of price-sensitive demand) are zero or very low compared with other pricing rules. Also, the makewhole payments for AIC prices are reduced compared with IP pricing, but they remain signi<sup>fi</sup>cant after a single pricing run and with hourly loss compensation. Make-whole payments per generator can be found in Appendix B.

Table 12. Flexible Demand II: Prices

<table><tr><td>Hour</td><td>IP($/MWh)</td><td>ELMP($/MWh)</td><td>AIC($/MWh)</td><td>PE-A($/MWh)</td></tr><tr><td> $t = 1$ </td><td>5.00</td><td>3.50</td><td>7.29</td><td>7.29</td></tr><tr><td> $t = 2$ </td><td>5.00</td><td>3.50</td><td>6.14</td><td>6.14</td></tr><tr><td> $t = 3$ </td><td>3.00</td><td>3.50</td><td>3.56</td><td>9.00</td></tr><tr><td>MWP ($)</td><td>38.00</td><td>43.75</td><td>10.89</td><td>0.00</td></tr></table>

Note. MWP states the total make-whole payments implied by each pricing rule.

Table 13. IEEE RTS Statistics with Price-Inelastic Demand

<table><tr><td></td><td>Price mean</td><td>Price std. dev.</td><td>MWP sell</td><td>MWP buy</td><td>Penalty sell</td><td>Penalty buy</td><td>MWP/total cost (%)</td><td>Computation time (s)</td></tr><tr><td>IP</td><td>22.32</td><td>8.81</td><td>35,749.28</td><td>0.00</td><td>0.00</td><td>0.00</td><td>4.63</td><td>1.39</td></tr><tr><td>ELMP</td><td>22.62</td><td>6.40</td><td>6,193.37</td><td>0.00</td><td>2,460.20</td><td>0.00</td><td>0.80</td><td>1.39</td></tr><tr><td>AIC</td><td>29.62</td><td>16.92</td><td>26,114.72</td><td>0.00</td><td>46,095.51</td><td>0.00</td><td>3.38</td><td>2.68</td></tr><tr><td>PBE-A</td><td>23.35</td><td>7.53</td><td>0.00</td><td>0.00</td><td>17,966.49</td><td>0.00</td><td>0.00</td><td>1.46</td></tr></table>

Under price-inelastic demand, a PBE (De<sup>fi</sup>nition 2) is achieved only by PBE-A. All other pricing rules require make-whole payments to ensure individual rationality. Classical IP pricing requires high make-whole payments to the generators, resulting in a violation of budget balance for the market operator. AIC prices are high on average, especially in the peak periods t 18 and t 19 (see Figure C.1 in Appendix C), contributing to a large standard deviation of the prices at the same time. The price peaks allow for overall pro<sup>fi</sup>tability for the generators, but as discussed before, individual periodic losses are still compensated, resulting in make-whole payments during low-price periods. By contrast, ELMP produces a smooth price pro<sup>fi</sup>le with little volatility and low lost opportunity costs (as re<sup>fl</sup>ected by the sum of make-whole payments and penalties). PBE-A adjusts this price pro<sup>fi</sup>le only slightly in order to ensure a PBE, mainly by increasing prices at the nodes 101 and 115, where most of the otherwise unpro<sup>fi</sup>table generators are situated. As a consequence, the price average and standard deviation are slightly increased, but no makewhole payments are required outside the market price. Penalties are necessary but are still lower than the lost opportunity costs required under IP or AIC pricing.

Next, we consider price-sensitive demand, taking into account the bid curves as described by Garcia-Bertrand et al. (2006). In particular, each buyer submits some minimum price-inelastic demand and a piecewise-constant demand curve on top of that. Accounting for buyer valuations naturally decreases prices compared with the price-inelastic case, which is also evident from Table 14 and Figure C.2 in Appendix C.

It is not possible to achieve a PBE in this environment. IP prices produce the lowest average price and standard deviation. Similar to the price-inelastic case, it diverges most from budget balance, with makewhole payments amounting to 2.5% of the total incurred generation costs. ELMP prices are higher on average, resulting in lower make-whole payments for the generators. However, these prices do not minimize total make-whole payments. PE-A requires make-whole payments of only \$112.41. Only IP prices are, on average, lower than PE-A prices, and the total lost opportunity costs of PE-A (as re<sup>fl</sup>ected by the sum of make-whole payments and penalties) are minimal among the pricing rules under consideration. PE-A prices are minimal in make-whole payments, closest to stability, and imply low and smooth price pro<sup>fi</sup>les.

Finally, we introduce demand <sup>fl</sup>exibility. Tables 15 and 16 re<sup>fl</sup>ect prices where 20% of the previous priceinelastic demand is converted to either shiftable pro-<sup>fi</sup>les or shiftable volumes. Here, each shiftable demand is a randomly sampled <sup>fi</sup>ve-hour interval of inelastic demand that can be shifted as a pro<sup>fi</sup>le by four hours (shiftable pro<sup>fi</sup>le), or the aggregate volume can be satis<sup>fi</sup>ed within the original <sup>fi</sup>ve hours in an arbitrary fashion (shiftable volume).

In both cases, welfare gains can be realized by using the demand-side <sup>fl</sup>exibility in a welfare-maximizing fashion. The increase in make-whole payments for the buyers is a result of the modeling decision to assign the highest valuation in the bid curve to the formerly priceinelastic and now price-sensitive and <sup>fl</sup>exible demand. As the <sup>fl</sup>exible demand needs to be satis<sup>fi</sup>ed within the boundaries set by the <sup>fl</sup>exibility parameters, this can create a loss on the part of the buyer if her highest valuation is still below the generation cost. This results in signi<sup>fi</sup> cantly higher make-whole payments for buyers. Again, PE-A has by far the lowest make-whole payments and little price volatility, among other things.

The numerical tests indicate that PBE-A and PE-A can substantially reduce or even eliminate makewhole payments compared with conventional pricing schemes. As a result, there are no or only very low side payments that are not re<sup>fl</sup>ected in the public market price anymore. Approaching budget balance comes at the expense of higher penalties to ensure a stable market outcome. As discussed in the previous sections, we argue that penalties are less of a concern, because they are already established and enforced in highly regulated electricity markets (O’Neill et al. 2020).

Table 14. IEEE RTS Statistics with Price-Sensitive Demand

<table><tr><td></td><td>Price mean</td><td>Price std. dev.</td><td>MWP sell</td><td>MWP buy</td><td>Penalty sell</td><td>Penalty buy</td><td>MWP/total cost (%)</td><td>Computation time (s)</td></tr><tr><td>IP</td><td>19.63</td><td>5.03</td><td>14,272.57</td><td>0.33</td><td>0.00</td><td>0.42</td><td>2.52</td><td>1.57</td></tr><tr><td>ELMP</td><td>21.02</td><td>5.35</td><td>490.39</td><td>781.43</td><td>257.43</td><td>803.04</td><td>0.22</td><td>1.55</td></tr><tr><td>AIC</td><td>21.27</td><td>6.36</td><td>11,048.85</td><td>945.38</td><td>0.00</td><td>0.00</td><td>2.12</td><td>2.96</td></tr><tr><td>PE-A</td><td>20.85</td><td>5.23</td><td>0.00</td><td>112.43</td><td>929.52</td><td>804.66</td><td>0.02</td><td>1.66</td></tr></table>

Table 15. IEEE RTS Statistics with 20% Shiftable Pro<sup>fi</sup>les

<table><tr><td></td><td>Price mean</td><td>Price std. dev.</td><td>MWP sell</td><td>MWP buy</td><td>Penalty sell</td><td>Penalty buy</td><td>MWP/total cost (%)</td><td>Computation time (s)</td></tr><tr><td>IP</td><td>19.63</td><td>5.03</td><td>14,275.82</td><td>9,116.75</td><td>0.00</td><td>0.00</td><td>4.14</td><td>1.76</td></tr><tr><td>ELMP</td><td>20.74</td><td>5.14</td><td>1,034.49</td><td>21,420.72</td><td>257.43</td><td>0.00</td><td>3.97</td><td>1.71</td></tr><tr><td>AIC</td><td>20.51</td><td>5.76</td><td>11,882.69</td><td>20,773.64</td><td>0.00</td><td>0.00</td><td>5.78</td><td>3.27</td></tr><tr><td>PE-A</td><td>20.42</td><td>4.92</td><td>188.54</td><td>322.96</td><td>929.52</td><td>538.11</td><td>0.09</td><td>1.84</td></tr></table>

## 7. Conclusions

Electricity markets have seen signi<sup>fi</sup>cant change among U.S. ISOs recently. Although all ISOs moved to mixedinteger programming in order to determine the ef<sup>fi</sup>cient dispatch, there is still signi<sup>fi</sup>cant discussion about outof-market make-whole payments paid by the ISOs to some of the generators. These payments can be signi<sup>fi</sup>- cant, and they distort the market price signals, as has been pointed out by the U.S. FERC and domain experts. We show that, with the standard assumption of priceinelastic demand and demand-supply equivalence, no make-whole payments are necessary.

With the advent of variable energy sources, demand response has become increasingly important. To adequately re<sup>fl</sup>ect <sup>fl</sup>exibility on the demand side, ISOs need new bid formats that can lead to additional nonconvexities and price-sensitive demand. We prove that in such markets, zero make-whole payments are impossible in general. From this insight, we introduce the PE-A pricing rule that minimizes make-whole payments and compare it to existing payment rules used by ISOs and the AIC pricing rule. Rather than trying to mimic competitive equilibrium prices based on linear relaxations of the underlying nonconvex allocation problem, we treat envy-freeness as a second-order design goal and optimize these objectives directly. The results show that high side payments on electricity markets, as they are challenged by regulators, can be either avoided or reduced substantially.

The experiments provide evidence that prices under PE-A do not increase on average compared with established pricing rules, and the changes in the overall payments of market participants are very small. Moreover, make-whole payments are avoided or are negligible in all experiments that we ran. The new pricing rules are based on optimization problems that can be solved in polynomial time and whose principles are easy to understand and communicate. The new pricing rule is also general, with out dependencies on the speci<sup>fi</sup>cs of the underlying allocation problem, and can be applied to other nonconvex markets as well.

## Acknowledgments

We are grateful for <sup>fi</sup>nancial support from the German National Science Foundation (Deutsche Forschungsgemeinschaft, DFG) BI 1057/1-9.

## Appendix A. Notation for DCOPF

We use the following notation in our model formulation.

Table 16. IEEE RTS Statistics with 20% Shiftable Volumes

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Sets
- $\mathcal{I} = \{1, \dots, I\}$: Buyers (index $i$)
- $\mathcal{J} = \{1, \dots, J\}$: Generators (index $j$)
- $\mathcal{T} = \{1, \dots, T\}$: Time periods (index $t$)
- $\mathcal{N} = \{1, \dots, N\}$: Nodes (index $n$)
- $\mathcal{L} = \{1, \dots, L\}$: Lines (index $l$)
</div>

## Parameters

$v \in \mathbb { R } ^ { I T } ;$ Buyer valuations

$c \in \mathbb { R } ^ { J T } \colon$ Generator variable cost

$h \in \mathbb { R } ^ { s J T }$ : Generator <sup>fi</sup>xed costs

$A \in \mathbb { R } ^ { m \times J T } ;$ : Generator constraint matrix I

$G \in \mathbb { R } ^ { m \times s J T }$ : Generator constraint matrix II

$b \in \mathbb { R } ^ { m } ;$ : Generator constraint right-hand side

$Q \in \mathbb { R } ^ { k \times I T } \colon$ : Buyer constraint matrix I

$R \in \mathbb { R } ^ { k \times T T }$ : Buyer constraint matrix II

$e \in \mathbb { R } ^ { k }$ : Buyer right-hand side

$P \in \mathbb { R } ^ { N T \times L T }$ : Inverse power transfer distribution factor matrix (calculated from the susceptance and network incidence matrix; it also includes the reference node)

$W \in \mathbb { R } ^ { N T \times J T }$ : Generator to node and period mapping matrix

$Z \in \mathbb { R } ^ { N T \times I T }$ : Buyer to node and period mapping matrix

$\overline { { W } } \in \mathbb { R } ^ { T \times J T }$ : Generator to period mapping matrix

$\overline { { Z } } \in \mathbb { R } ^ { T \times I T } ;$ : Buyer to period mapping matrix

<table><tr><td></td><td>Price mean</td><td>Price std. dev.</td><td>MWP sell</td><td>MWP buy</td><td>Penalty sell</td><td>Penalty buy</td><td>MWP/total cost (%)</td><td>Computation time (s)</td></tr><tr><td>IP</td><td>19.98</td><td>5.29</td><td>12,725.92</td><td>10,491.12</td><td>0.00</td><td>0.00</td><td>4.18</td><td>1.83</td></tr><tr><td>ELMP</td><td>21.04</td><td>5.36</td><td>436.60</td><td>22,686.77</td><td>257.43</td><td>0.00</td><td>4.16</td><td>1.74</td></tr><tr><td>AIC</td><td>21.66</td><td>6.65</td><td>10,888.60</td><td>35,141.68</td><td>0.00</td><td>0.00</td><td>8.29</td><td>3.34</td></tr><tr><td>PE-A</td><td>20.74</td><td>5.17</td><td>564.35</td><td>198.47</td><td>741.80</td><td>687.45</td><td>0.14</td><td>1.84</td></tr></table>

Figure B.1. Make-Whole Payments with Price-Inelastic Demand  
![](/api/attachments/993CDZD6/fulltext/images/41722c126a0a1759c7674bfb801409938522295886e37c047c3963b294f6446b.jpg)  
${ \overline { { F } } } \in \mathbb { R } ^ { L T } ;$ Upper <sup>fl</sup>ow limits $\underline { { F } } \in \mathbb { R } ^ { L T } ;$ : Lower <sup>fl</sup>ow limits

## Decision Variables

$x \in \mathbb { R } ^ { I T }$ : Buying quantities

C $d \in \{ 0 , 1 \} ^ { r I T } ;$ : Buy-side binary variables (r as the integer multiplier to account for several binaries such as different dimensions of <sup>fl</sup>exibility, etc.)

$y \in \mathbb { R } ^ { J T }$ : Selling quantities

$u \in \{ 0 , 1 \} ^ { s J T } ;$ : Generator commitment and other binaries (s as the integer multiplier to account for several binaries such as commitment, start-up, etc.)

$\bullet f \in \mathbb { R } ^ { L T }$ : Line <sup>fl</sup>ows

## Appendix B. Make-Whole Payments

Figures B.1–B.4 (see the online version for better visualization) provide histograms of make-whole payments per generator (in dollars) in the different environments with price-inelastic, price-sensitive, and <sup>fl</sup>exible demand (shiftable pro<sup>fi</sup>les and shiftable volumes) for the IEEE RTS-96 system. With IP

Figure B.2. Make-Whole Payments with Price-Sensitive Demand  
![](/api/attachments/993CDZD6/fulltext/images/cab878faf11a2e45fb944be53715ba61bef30feca6167935d6b6b6665223317e.jpg)

Figure B.3. Make-Whole Payments with 20% Shiftable Pro<sup>fi</sup>les  
![](/api/attachments/993CDZD6/fulltext/images/7e4be0e394d4153592dc3e74a95361323be6fa0cfa9dcfaf04ccfe44c82bf3b1.jpg)  
pricing, ELMP, and AIC, some generators receive very high make-whole payments that are not re<sup>fl</sup>ected in the public prices. With PBE-A/PE-A, such make-whole payments are negligible.

## Appendix C. Heat Maps of Prices

The heat maps in Figures C.1–C.4 describe hourly nodal prices (in dollars per megawatt-hour) for different nodes across the day for the IEEE RTS system. Darker color describe higher prices. Each panel describes the outcome of one pricing rule (IP, ELMP, AIC, and PBE-A or PE-A) for the environments with price-inelastic demand, pricesensitive demand, 20% shiftable pro<sup>fi</sup>les, or 20% shiftable volumes. In general, the prices with price-sensitive and <sup>fl</sup>exible demand tend to be higher. Interestingly, the prices of PBE-A/PE-A and ELMP tend to be similar in spite of signi<sup>fi</sup>cantly lower make-whole payments with PBE-A/ PE-A.

Additional experiments can be found in the online supplement.

Figure B.4. Make-Whole Payments with 20% Shiftable Volumes  
![](/api/attachments/993CDZD6/fulltext/images/b7125fd5704a39228a2480453586bb23c73396204f2e66a4e669b762d9ab2ca1.jpg)

![](/api/attachments/993CDZD6/fulltext/images/42c7e235dbee06ae1cb9f4712f3e8c859f42336503ee6c0b174939c7e08a6ecc.jpg)

![](/api/attachments/993CDZD6/fulltext/images/9969867ae742910419b6ffba314dca33a18448fb586fe371bf4cdbdd3318543b.jpg)

Figure C.1. IEEE RTS Prices with Price-Inelastic Demand  
![](/api/attachments/993CDZD6/fulltext/images/c6d49b211be26b52661b08abcffeacb3500fb25ce25ede1f61dd2dc9420fc00c.jpg)

![](/api/attachments/993CDZD6/fulltext/images/15152bfaf04fc5484d5ce14b4929835551365606ba4ff9830a1f8fae439651be.jpg)

![](/api/attachments/993CDZD6/fulltext/images/16c040be370d3596691f36957451874187dd183378a5261e8b356303054762d8.jpg)

![](/api/attachments/993CDZD6/fulltext/images/a930433d94755d991e8c6b2c5909c72c5a580b9c41593535be923535131ae50c.jpg)

Figure C.2. IEEE RTS Prices with Price-Sensitive Demand  
![](/api/attachments/993CDZD6/fulltext/images/1343d61eb87e54bc3bb786b181681240da9d782f81ef64b61e04aebdb6f88d44.jpg)

![](/api/attachments/993CDZD6/fulltext/images/0094fb28bc90afcacf98dfe0d0d5928addb7a015ecfb7a2ceb83f4de679ec4ea.jpg)

Figure C.3. IEEE RTS Prices with 20% Shiftable Pro<sup>fi</sup>les  
![](/api/attachments/993CDZD6/fulltext/images/368352e35c76063d686769efd09fae6f54b8d300a3d95a60e3f3a369ec9a268a.jpg)

## Endnotes

<sup>1</sup> See https://www.misoenergy.org/stakeholder-engagement/stake holder-feedback/msc-elmp-iii-whitepaper-20190117/ (accessed October 13, 2020).

<sup>2</sup> See https://www.ferc.gov/industries-data/electric/electric-powermarkets/energy-price-formation (accessed March 1, 2021).

<sup>3</sup> This co-optimization of energy and ancillary services differs from European markets, where reserves are cleared in separate markets.

<sup>4</sup> See https://www.misoenergy.org/stakeholder-engagement/MISO-Dashboard/update-to-demand-response-deployment-tools/ (accessed May 25, 2022).

<sup>5</sup> Much of the literature on pricing in electricity markets and their current implementations suggests that the results are a CE. As introduced earlier, a CE requires envy-freeness and budget balance, but budget balance is not satisfied here.

<sup>6</sup> Prior to August 7, 2021, the allowed computation time was only 12 minutes.

## References

Adomavicius G, Gupta A (2005) Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2):169–185.

Adomavicius G, Curley S, Gupta A, Sanyal P (2012) Effect of information feedback on bidder behavior in continuous combinatorial auctions. Management Sci. 58(4):811–830.

Adomavicius G, Curley S, Gupta A, Sanyal P (2020) How decision complexity affects outcomes in combinatorial auctions. Produc tion Oper. Management 29(11):2579–2600.

All NEMO Committee (2021) CACM annual report 2020. Accessed December 13, 2021, https://www.nemo-committee.eu/assets/<sup>fi</sup>les NEMO\_CACM\_Annual\_Report\_2020\_deliverable\_1\_pub.pdf.

Antonopoulos G, Vitiello S, Fulli G, Masera M (2020) Nodal pricing in the European Internal Electricity Market. EUR Technical Report 30155, Publications Of<sup>fi</sup>ce of the European Union, Luxembourg.

Araoz V, Jornsten K (2011) Semi-Lagrangean approach for price dis-¨ covery in markets with non-convexities. Eur. J. Oper. Res. 214(2): 411–417.

Arrow KJ, Debreu G (1954) Existence of an equilibrium for a com petitive economy. Econometrica 22(3):265–290.

Ashour Novirdoust A, Bichler M, Bojung C, Buhl HU, Fridgen G, Gretschko V, Hanny L, et al. (2021) Electricity spot market design 2030–2050. White paper, Fraunhofer FIT, Sankt Augustin, Germany.

Azevedo EM, Budish E (2019) Strategy-proofness in the large. Rev. Econom. Stud. 86(1):81–116.

Azevedo EM, Weyl EG, White A (2013) Walrasian equilibrium in large, quasilinear markets. Theoret. Econom. 8(2):281–290.

Azizan N, Su Y, Dvijotham K, Wierman A (2020) Optimal pricing in markets with nonconvex costs. Oper. Res. 68(2): 480–496.

Baldwin E, Klemperer P (2019) Understanding preferences: Demand types, and the existence of equilibrium with indivisibilities. Econometrica 87(3):867–932.

Bichler M, Waldherr S (2017) Core and pricing equilibria in combinatorial exchanges. Econom. Lett. 157(August):145–147.

Bichler M, Fichtl M, Schwarz G (2021) Walrasian equilibria from an optimization perspective: A guide to the literature. Naval Res. Logist. 68(4):496–513.

Bichler M, Fux V, Goeree J (2018) A matter of equality: Linear pricing in combinatorial exchanges. Inform. Systems Res. 29(4): 1024-1043.

Bichler M, Fux V, Goeree JK (2019) Designing combinatorial exchanges for the reallocation of resource rights. Proc. Natl. Acad. Sci. USA 116(3):786–791.

Bichler M, Shabalin P, Ziegler G (2013) Ef<sup>fi</sup>ciency with linear prices? A game-theoretical and computational analysis of the combina torial clock auction. Inform. Systems Res. 24(2):394–417.

Bikhchandani S, Mamer JW (1997) Competitive equilibrium in an exchange economy with indivisibilities. J. Econom. Theory 74(2): 385–413.

Bikhchandani S, Ostroy JM (2002) The package assignment model J. Econom. Theory 107(2):377–406.

California ISO (2018) ISO at-a-glance. https://www.caiso.com/ Documents/CaliforniaISO-GeneralCompanyBrochure.pdf

California ISO (2021) 2020 annual report on market issues & performance. http://www.caiso.com/Documents/2020-Annual-Reporton-Market-Issues-and-Performance.pdf.

Caplice C, Shef<sup>fi</sup> Y (2003) Optimization-based procurement for transportation services. J. Bus. Logist. 24(2):109–128.

Carpentier J (1985) Optimal power <sup>fl</sup>ows: Uses, methods and devel opments. IFAC Proc. Vol. 18(7):11–21.

Cramton P (2003) Electricity market design: The good, the bad, and the ugly. Sprague RH Jr, ed. Proc. 36th Annual Hawaii Internat. Conf. System Sci. (IEEE, Piscataway, NJ), 54.

Cramton P (2017) Electricity market design. Oxford Rev. Econom. Pol icy 33(4):589–612.

De Loera JA, Haddock J, Rademacher L (2020) The minimum Euclidean-norm point in a convex polytope: Wolfe’s combinato rial algorithm is exponential. SIAM J. Comput. 49(1):138–169.

Eldridge B, O’Neill RP, Castillo A (2017) Marginal loss calculations for the DCOPF. Technical Report SAND2017-0563R, Sandia National Laboratory, Albuquerque, NM.

Eldridge B, O’Neill R, Hobbs BF (2019) Near-optimal scheduling in day-ahead markets: Pricing models and payment redistribution bounds. IEEE Trans. Power Systems 35(3):1684–1694.

European Commission Directorate-General for Energy (2016) Impact assessment study on downstream <sup>fl</sup>exibility, price <sup>fl</sup>exibility, demand response & smart metering. Final Report ENER/B3/ 2015-641, European Commission, European Union, Brussels.

Farrell MJ (1959) The convexity assumption in the theory of competitive markets. J. Political Econom. 67(4):377–391.

Gale D (1963) A note on global instability of competitive equili brium. Naval Res. Logist. Quart. 10(1):81–87.

Galiana FD, Motto AL, Bouffard F (2003) Reconciling social welfare, agent pro<sup>fi</sup>ts, and consumer payments in electricity pools. IEEE Trans, Power Sustems 18(2):452–459

Garcia-Bertrand R, Conejo AJ, Gabriel S (2006) Electricity market near-equilibrium under locational marginal pricing and minimum pro<sup>fi</sup>t conditions. Eur. J. Oper. Res. 174(1):457–479.

Garrido RA (2007) Procurement of transportation services in spot markets under a double-auction scheme with elastic demand. Transportation Res. Part B: Methodological 41(9):1067–1078.

Goetzendorff A, Bichler M, Shabalin P, Day RW (2015) Compact bid languages and core pricing in large multi-item auctions. Management Sci. 61(7):1684–1703.

Green J, Laffont J-J (1979) On coalition incentive compatibility. Rev. Econom. Stud. 46(2):243–254.

Gribik PR, Hogan WW, Pope SL (2007) Market-clearing electricity prices and energy uplift. Report, Harvard Electricity Policy Group, John F. Kennedy School of Government, Harvard Uni versity, Cambridge, MA.

Grigg C, Wong P, Albrecht P, Allan R, Bhavaraju M, Billinton R, Chen Q, et al. (1999) The IEEE Reliability Test System-1996. A report prepared by the Reliability Test System Task Force of the Application of Probability Methods Subcommittee. IEEE Trans. Power Systems 14(3):1010–1020.

Guo Z, Koehler G, Whinston A (2012) A computational analysis of bundle trading markets design for distributed resource allocation. Inform. Systems Res. 23(3, Part 1):823–843.

Herrero I, Rodilla P, Batlle C (2020) Evolving bidding formats and pricing schemes in USA and Europe day-ahead electricity markets. Energies 13(19): article 5020.

Hua B, Baldick R (2017) A convex primal formulation for convex hull pricing. IEEE Trans. Power Systems 32(5):3814–3823.

Hytowitz RB, Frew B, Stephen G, Ela E, Singhal N, Bloom A, Lau J (2020) Impacts of price formation efforts considering high renewable penetration levels and system resource adequacy targets. Technical Report NREL/TP-6A20-74230, National Renewable Energy Laboratory, Washington, DC.

IRENA (2019) Innovation landscape for a renewable-powered future: Solutions to integrate variable renewables. Report, International Renewable Energy Agency, Abu Dhabi, UAE.

Jeroslow RG (1985) The polynomial hierarchy and a simple model for competitive analysis. Math. Programming 32(2):146–164.

Kaneko M (1976) On the core and competitive equilibria of a market with indivisible goods. Naval Res. Logist. Quart. 23(2):321–337.

Ketter W, Peters M, Collins J, Gupta A (2016) A multiagent competitive gaming platform to address societal challenges. MIS Quart. 40(2):447–460.

Kim S (1986) Computation of a large-scale competitive equilibrium through optimization. Comput. Oper. Res. 13(4):507–515.

Koolen D, Qiu L, Ketter W, Gupta A (2018) The sustainability tipping point in electricity markets. Kim YJ, Agarwal R, Lee JK, eds. Proc. 38th Internat. Conf. Inform. Systems: Transforming Soc. Digital Innovation (Association for Information Systems, Atlanta), 4:2519–2536.

Leme RP (2017) Gross substitutability: An algorithmic survey. Games Econom. Behav. 106(November):294–316.

Liberopoulos G, Andrianesis P (2016) Critical review of pricing schemes in markets with non-convex costs. Oper. Res. 64(1): 17–31.

Liu Y, Holzer JT, Ferris MC (2015) Extending the bidding format to promote demand response. Energy Policy 86(November): 82–92.

Madani M, Ruiz C, Siddiqui S, Van Vyve M (2018) Convex hull, IP and European electricity pricing in a European power exchanges setting with ef<sup>fi</sup>cient computation of convex hull prices. Preprint, submitted March 30, http://arxiv.org/pdf/1804.00048v1.

Mas-Colell A, Whinston MD, Green JR (1995) Microeconomic Theory, Vol. 1 (Oxford University Press, New York).

McKenzie LW (1959) On the existence of general equilibrium for a competitive market. Econometrica 27(1):54–71.

Meeus L, Verhaegen K, Belmans R (2009) Block order restrictions in combinatorial electric energy auctions. Eur. J. Oper. Res. 196(3): 1202-1206.

Monitoring Analytics LLC (2019) State of the market report for PJM. Independent Market Monitor for PJM Report, Monitoring Analytics, LLC, Southeastern, PA.

Morales JM, Pineda S, Conejo AJ, Carrion M (2009) Scenario reduction for futures market trading in electricity markets. IEEE Trans. Power Systems 24(2):878–888.

Motto A, Galiana FD (2002) Equilibrium of auction markets with unit commitment: The need for augmented pricing. IEEE Trans. Power Systems 17(3):798–805.

NEMO Committee (2020) EUPHEMIA public description: Single price coupling algorithm. Report, NEMO Committee, Madrid, Spain.

O’Neill RP, Chen Y, Whitman P (2020) The one-pass average incremental cost pricing approach with multi-step marginal costs, ramp constraints and reserves. Working paper, Advanced

Research Projects Agency–Energy, U.S. Department of Energy, Washington, DC.

O’Neill RP, Castillo A, Eldridge B, Hytowitz RB (2016) Dual pricing algorithm in ISO markets. IEEE Trans. Power Systems 32(4): 3308–3310.

O’Neill RP, Sotkiewicz PM, Hobbs BF, Rothkopf MH, Stewart WR (2005) Ef<sup>fi</sup>cient market-clearing prices in markets with nonconvexities. Eur. J. Oper. Res. 1(164):269–285.

O’Neill R, Hytowitz RB, Whitman P, Mead D, Dautel T, Chen Y, Eldridge B, et al. (2019) Essays on average incremental cost pricing for independent system operators. Working paper, Washington, DC.

Ottesen SØ, Tomasgard A (2015) A stochastic model for scheduling energy <sup>fl</sup>exibility in buildings. Energy 88(August):364–376.

Ottesen SØ, Tomasgard A, Fleten S-E (2016) Prosumer bidding and scheduling in electricity markets. Energy 94(January):828–843.

Petrakis I, Ziegler G, Bichler M (2013) Ascending combinatorial auctions with allocation constraints: On game-theoretical and computational properties of generic pricing rules. Inform. Systems Res. 24(3):768–786.

Purchala K (2018) EU electricity market: The good, the bad and the ugly. Accessed March 1, 2021, https://www.pse.pl/documents 31287/20965583/PSE\_16 102018\_The\_good\_the\_bad\_the\_ugly.pdf.

Reihani E, Motalleb M, Thornton M, Ghorbani R (2016) A novel approach using <sup>fl</sup>exible scheduling and aggregation to optimize demand response in the developing interactive grid marke architecture. Appl. Energy 183(December):445–455.

Ruiz C, Conejo AJ, Gabriel SA (2012) Pricing non-convexities in an electricity pool. IEEE Trans. Power Systems 27(3):1334–1342.

Schiro DA, Zheng T, Zhao F, Litvinov E (2016) Convex hull pricing in electricity markets: Formulation, analysis, and implementation challenges. IEEE Trans. Power Systems 31(5): 4068–4075.

Shah D, Chatterjee S (2020) A comprehensive review on day-ahead electricity market and important features of world’s major elec tric power exchanges. Internat. Trans. Electrical Energy Systems 30(7):Article e12360.

Starr RM (1969) Quasi-equilibria in markets with non-convex preferences. Econometrica 37(1):25–38.

Stott B, Jardim J, Alsac¸ O (2009) DC power <sup>fl</sup>ow revisited. IEEE Trans. Power Systems 24(3):1290–1300.

Toczyłowski E, Zoltowska I (2009) A new pricing scheme for a multi-period pool-based electricity auction. Eur. J. Oper. Res 197(3):1051–1062.

Valogianni K, Ketter W (2016) Effective demand response for smart grids: Evidence from a real-world pilot. Decision Support Systems 91(November):48–66.

Van den Bergh K, Delarue E, D’haeseleer W (2014) DC power <sup>fl</sup>ow in unit commitment models. TME Working Paper WP EN2014- 12, KU Leuven Energy Institute, Leuven, Belgium.

Watson J-P, Cesar ASM, Castillo A, Laird C, O’Neill R (2015) Security-constrained unit commitment with linearized AC optimal power <sup>fl</sup>ow. Technical report, Sandia National Laboratory, Albuquerque, NM.

Xia M, Koehler GJ, Whinston AB (2004) Pricing combinatorial auc tions. Eur. J. Oper. Res. 154(1):251–270.

Zocca A, Zwart B (2021) Optimization of stochastic lossy transport networks and applications to power grids. Stochastic Systems 11(1):34–59.

Zohrizadeh F, Josz C, Jin M, Madani R, Lavaei J, Sojoudi S (2020) A survey on conic relaxations of optimal power <sup>fl</sup>ow problem. Eur. J. Oper. Res. 287(2):391–409.

Zoltowska I (2016) Demand shifting bids in energy auction with non-convexities and transmission constraints. Energy Econom. 53(1):17–27.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
