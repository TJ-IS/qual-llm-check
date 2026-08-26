---
otero_id: 16236
otero_key: "JM9FQ2EM"
title: "Providing Utility to Utilities: The Value of Information Systems Enabled Flexibility in Electricity Consumption"
authors: "Gilbert Fridgen; Lukas Häfner; Christian König; Thomas Sachs"
year: "2016"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00434"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 17 Issue 8 SPECIAL ISSUE: Information Systems Solutions for Environmental Sustainability

Article 1

8-26-2016

# Providing Utility to Utilities: The Value of Information Systems Enabled Flexibility in Electricity Consumption

Gilbert Fridgen , gilbert.fridgen@uni.lu

Lukas Häfner , lukas.haefner@fim-rc.de

Christian König , christian.koenig@fim-rc.de

Thomas Sachs , thomas.sachs@uni-bayreuth.de

Follow this and additional works at: https://aisel.aisnet.org/jais

IS Solutions for Environmental Sustainability Special Issue: Research Paper

ISSN: 1536-9323

# Providing Utility to Utilities: The Value of Information Systems Enabled Flexibility in Electricity Consumption

Gilbert Fridgen Information Systems and Sustainable IT Management, University of Bayreuth, Germany gilbert.fridgen@uni-bayreuth.de

Christian König FIM Research Center, University of Augsburg, Germany christian.koenig@fim-rc.de

Lukas Häfner FIM Research Center, University of Augsburg, Germany lukas.haefner@fim-rc.de

Thomas Sachs Information Systems and Sustainable IT Management, University of Bayreuth, Germany thomas.sachs@uni-bayreuth.de

## Abstract:

As the transition to renewable energy sources progresses, the integration of such sources makes electricity production increasingly fluctuate. To contribute to power grid stability, electric utilities must balance volatile supply by shifting demand. This measure of demand response depends on flexibility, which arises as the integration of information systems in the power grid grows. The option to shift electric loads to times of lower demand or higher supply bears an economic value. Following a design science research approach, we illustrate how to quantify this value to support decisions on short-term consumer compensation. We adapt real options theory to the design—a strategy that IS researchers have used widely to determine value under uncertainty. As a prerequisite, we develop a stochastic process, which realistically replicates intraday electricity spot price development. With this process, we design an artifact suitable for valuation, which we illustrate in a plug-in electric vehicle scenario. Following the artifact’s evaluation based on historical spot price data from the electricity exchange EPEX SPOT, we found that real options analysis works well for quantifying the value of information systems enabled flexibility in electricity consumption.

Keywords: Demand Response, Load Shifting, Design Science Research, Electricity Spot Price Model, Real Options.

## 1 Introduction

Faced with growing environmental concerns and a dependence on exporters of fossil commodities, several countries have begun transitioning their power supply from fossil and nuclear sources to renewable resources, such as solar and wind. The shift toward these intermittent energy sources makes electricity production increasingly fluctuate (Ludig, Haller, Schmid, & Bauer, 2011). For example, non-forecasted wind prompts peaks in electricity supply, which can destabilize the power grid and require costly balancing efforts. By itself, adjusting the supply curve through electricity storage would not be sufficient to balance the highly volatile supply and demand nor to offset the strain on the power grid, which has prompted the idea of intervening on the side of consumption as well (Palensky & Dietrich, 2011).

Business research describes “demand-side management” (DSM) as activities that influence the timing and magnitude of consumer demand for electricity to accommodate fluctuations of electricity production. Researchers consider DSM as an umbrella term (Feuerriegel & Neumann, 2014) and another common term, “demand response” (DR), as a subclass of such activities. Through incentives or varied electricity prices, DR activities induce changes in electricity consumption (Albadi & El-Saadany, 2008). Such measures tend to span minutes or hours, and electricity consumers decide to participate in DR programs voluntarily (Palensky & Dietrich, 2011). For our approach, we use the term DR, which includes load control.

“Advanced metering infrastructure” (AMI)—systems for measuring, collecting, transmitting, and analyzing energy usage data—is the IT enabling DR. AMI combines smart meters, which measure electricity consumption in time intervals, load control switches, and bidirectional communication streams between electric utilities and consumers (Callaway & Hiskens, 2011; Li et al., 2013). As such, utilities can remotely control demand by, in particular, emitting control signals to initiate the deferral of electricity consumption to times of higher supply or lower demand—a process called “load shifting” (LS). In this paper, we employ the term “utility” to refer to an electric power company that engages in procuring and distributing electricity for sale to consumers. By allowing utilities to influence when certain appliances draw on electricity, consumers provide them with flexibility. Figure 1 depicts the actors. One case example for LS would be postponing the charging process of a plug-in electric vehicle (PEV). Other conceivable LS examples can apply to household appliances with significant consumption, such as dish and clothes washers, dryers, electric heating, and air conditioning. Independent of the considered object for LS, the flexibility consumers provide bears economic value because it allows utilities to procure electricity when it is cheap on the electricity market (the “spot market” is the segment utilities make intraday trades on) and vice versa. As such, utilities gain the option to react to fluctuating spot market prices for electricity and realize a profit when shifting loads to times of a lower price. Other reasons such as saving the dispatch of expensive balancing power and lower strain on distribution grids may further motivate a utility to use LS.

![](/api/attachments/JM9FQ2EM/fulltext/images/d154bc8ddb389a67d80e4d815297bc6ac5cf741b98d8c6f462acd27b651e9195.jpg)  
Figure 1. Actors and Relationships

Nonetheless, the tools to shape consumption provided through DR do come at a price. First, utilities need to invest in information systems (IS) that provide the transmission medium for signals and information, support decisions on when to shift loads, and initiate and control the process. Operating this infrastructure causes further costs. Second, utilities need to “buy” the flexibility consumers provide—they must offer consumers compensation for giving away the right to have their appliances at their complete disposal. An option would be for utilities to make consumers dynamic compensation offers in real time. As a result, to reach profitability, a utility needs methods to quantify the economic value of individual IS-enabled LS measures in consideration of electricity market information. In our vision, every time a consumer uses AMI to signal loads to be deferrable, utilities will be able to determine how much shifting them over the course of some hours is worth. Utilities will employ algorithms that will enable them to decide on LS initiation and duration. Intensified by the expansion of smart grids, AMI, and corresponding regulation, the opportunities for applying DR and deploying its capabilities for a sustainable energy transition will grow.

One can regard the flexibility a consumer offers to a utility as an option to shift loads; it enables the utility to decide whether to deliver the load immediately or later. From a temporal point of view, this flexibility is short term. It encompasses the number of hours (rather than days or weeks) the consumer is willing to wait for the load. In this paper, we focus on identifying a model capable of grasping this situation, the aforementioned “intraday” option in particular. Simultaneously, we note that electricity markets feature fluctuating prices, which imply an elevated risk. Therefore, we see the need to apply a dynamic investment methodology. To determine the option’s value, established option valuation methods come into consideration. With electricity as a tangible, non-financial product, assessing the option’s value by means of real options seems promising because real options analysis (ROA) captures flexibility of action and enables one to valuate dynamic investments under uncertainty by modeling volatility (Amram & Kulatilaka, 1999; Dixit & Pindyck, 1995; Trigeorgis, 1996).

From the overarching research objective described above, we derive our research question:

RQ: How can one quantify the monetary value of IS-enabled, short-term flexibility in consumer demand for electricity using real options analysis?

Our research objective covers a relevant real-world problem because an answer could facilitate profitable LS decisions for utilities and help stabilize the equilibrium of electricity supply and demand. We apply design science research (DSR), which is “inherently a problem solving process” (Hevner, March, Park, & Ram, 2004). We pursue a corresponding approach to design an IS-enabled artifact that is applicable to various electricity markets worldwide, such as those in the United States and Europe. DSR seems to be a suitable approach for this undertaking because it provides a profound scheme for developing and communicating our artifact (Gregor & Hevner, 2013). We process electricity prices as the key information for our ROA. Thus, in many scenarios, our artifact needs to cope with a condition of uncertainty: LS comprises the course of some hours (i.e., intraday) during which price development is uncertain.

Real options theory features adequate model-theoretic requirements and numerous applications in IS research (Benaroch & Kauffman, 1999) and the energy sector (Ronn, 2003). Thus, we consider real options theory to be a rigorous kernel theory (in the terms of Gregor & Hevner, 2013) to underpin our artifact. In the course of our search process, we set up a stochastic model for electricity spot price development and, thereby, address a prerequisite of ROA (Ullrich, 2013). The model realistically captures seasonal price patterns and short-term effects of several hours and days but is straightforward to apply. We further design an algorithm that one can integrate into decision support systems (DSS) for short-term compensation offers. To that end, we model and evaluate a deferral option, which is an established type of a real option. For analytic assessment, we use Cox, Ross, and Rubinstein’s (1979) the binomial tree model, which guides LS initiation and duration. We further evaluate the artifact’s effectiveness in a simulation based on historical data, which is a valid and rigorous design-evaluation method (Hevner et al., 2004). Finally, we attempt to generalize insights gained from our research and, thereby, underpin our research contribution.

This paper proceeds as follows: in Section 2, we discuss related work. In Section 3, we overview electricity markets (i.e. market instruments, market segments, and market differences). In Section 4, we design our model. After formulating the problem setting, we present necessary assumptions and distinguish two cases: electricity procurement from hour-ahead markets or from real-time markets. For the former, we develop a simple valuation method for LS flexibility. With regard to real-time procurement, we develop an appropriate stochastic process to describe electricity spot market prices based on the concept of a geometric Brownian motion. We use this stochastic process to model and assess a deferral real option. Following a binomial tree approach, our ROA reveals a monetary value for IS-enabled flexibility in electricity consumption on realtime markets. We demonstrate this approach in Section 5, describing how we evaluated our method for real-time markets. In Section 6, we conclude the paper by discussing its contributions, addressing limitations, and presenting an outlook on further research.

## 2 Related Work

Paving the way for valuation of flexible loads in IS-supported DR is a contribution to “energy informatics” (EI). As a subfield of IS research, EI should apply “information systems thinking and skills to increase energy efficiency” (Watson, Boudreau, & Chen, 2010). We address this claim with our objective, which is to enhance the decision logic of IS for load control to increase the efficiency of electricity consumption and realize economic potential. Watson et al. (2010) suggest finding practical solutions to economize electricity consumption, which we develop in a valuation method applicable to short-term LS decisions. Goebel et al. (2014) and Strüker and van Dinther (2012) identify the need to quantify DR’s economic potential. We focus on meeting this requirement to enable decisions on investment in technologies and compensations that facilitate LS on a level of consumer supply. We revise and extend our prior work (Fridgen, Häfner, König, & Sachs, 2014, 2015) by developing our real-time model’s capability to account for short-term influences on electricity prices. Furthermore, we broaden our research by giving respect to hour-ahead markets to achieve a more general approach for utilities. Rigorously following DSR methodology, we extensively evaluate our artifact via simulation and sensitivity analyses and quantify the savings potential when shifting flexible loads under real circumstances.

Some scholars have determined the value of flexible loads by taking simulation approaches. Biegel, Hansen, Stoustrup, Andersen, and Harbo (2014) describe requirements for aligning flexible appliances with the electricity spot market. They also give an estimate of the cost and revenue, which depend on the magnitude of consumption. Vytelingum, Voice, Ramchurn, Rogers, and Jennings (2011) introduce an adaptive algorithm for micro-storage management in smart grids. Conducting simulations, they show that their approach can generate energy cost savings for an average consumer. Similarly, Rieger, Thummert, Fridgen, Kahlen, and Ketter (2016) determine potential electricity cost savings of up to 10 percent, which they attribute to their cooperative DR approach. Based on statistical data, Feuerriegel and Neumann (2014) derive an optimization problem for when to shift loads, which they then evaluate in a simulation. Goebel (2013) investigates a particular case of DR application: controlled charging of a fleet of plug-in electric vehicles. By simulation, the author finds that utilities with an intelligent charging schedule can secure a savings potential. Similarly, Kahlen and Ketter (2015) develop the algorithm “FleetPower” for balancing the power grid with a fleet of plug-in electric vehicles. Constituting a virtual power plant, the algorithm decides in real time whether to let cars for rent or to use them as an operating reserve for balancing the grid. The authors’ simulation reveals that current developments in the energy sector enable “FleetPower” to generate significant savings. From a reproduction of household load profiles, Gottwalt, Ketter, Block, Collins, and Weinhardt (2011, p. 8172) conclude that “an individual household can expect rather low benefits of an investment in smart appliances”. However, they consider the provided flexibility in electricity consumption highly valuable to utilities.

We go beyond the scope of these authors’ works by developing an entire valuation rather than a pure simulation method. Serving as the kernel theory to our artifact, real options theory was derived from financial option valuation, which is a well-developed methodology. IS researchers have applied ROA in numerous cases (Benaroch & Kauffman, 1999; Ullrich, 2013). So far, in the energy sector, researchers have widely applied ROA to evaluate electricity-generation projects (Deng & Oren, 2003; Martinez-Cesena, Azzopardi, & Mutale, 2013; Ronn, 2003). Converging to our objective, some scholars have argued that research should use the capabilities of real options to assess the monetary value of IS-enabled flexibility in electricity consumption with respect to uncertainty in electricity prices. Sezgen, Goldman, and Krishnarao (2007, p. 108) stress the need to quantify “the economic value of investments in technologies that manage electricity demand in response to changing energy prices”. We consider Sezgen et al.’s (2007) method for ROA an important contribution. However, their model suits thermal energy storage technologies and cannot capture intraday flexibility. Sezgen et al. (2007) leave such flexibility to follow-up work. Oren (2001) designs a real options approach to hedge against price risk in the electricity spot market. He concludes that the unadjusted model does not suffice to replicate electricity spot price development and leaves the formation of more realistic models to further research.

Both approaches cannot evaluate short-term LS realized through IS, which is a real-world use case and integral part of our research question. Nonetheless, similarly to Sezgen et al. (2007) and Oren (2001), our artifact sets on electricity prices, which means we need to consider their stochastic price movement to derive an appropriate valuation method. While Sezgen et al. (2007) and Oren (2001) build their models based on the assumption of a regular geometric Brownian motion process for electricity prices, our spot price model incorporates realistic time-dependent mean price levels and meanreverting properties to enable short-term LS decisions.

Beyond the literature on real options modeling of electricity consumption, other scholars have also studied the prerequisite to stochastically model electricity spot market prices. Coulon, Powell, and Sircar (2013) develop a model that accounts for the complex relationship between electricity spot market prices and underlying factors. In particular, Coulon et al. (2013) capture three stochastic factors (gas price, load and available capacity) to account for electricity price dynamics and a switching regime for modeling price spikes. While this approach seems to suit to hedge portfolios of generating assets and load-serving obligations, it is too complex for our purpose in that we only need to estimate future price developments and not their ultimate causes. Fanone, Gamba, and Prokopczuk (2013) build a non-Gaussian stochastic process for day-ahead electricity prices. Using data from the European electricity exchange, the authors model current developments in the German day-ahead market by considering negative electricity prices. Huisman, Huurman, and Mahieu (2007) introduce a panel model for hourly electricity prices in day-ahead markets. They build a stochastic process that describes price differences while considering uncertainty with hourspecific mean price levels and mean-reverting properties. However, since the authors model panels of 24 prices that simultaneously result from day-ahead auctions, the single prices are not an intraday movement or a time series. A set 24-hour pricing panel is not appropriate for our purposes. Other approaches to model electricity price development by stochastic means include Weron, Bierbrauer, and Trück (2004), Deng and Jiang (2005), Kim and Powell (2011), Schneider (2012), and Benth, Klüppelberg, Müller, and Vos (2014). After analyzing these studies, we concluded that no included approach met the requirements for our research question without overstepping bearable complexity for our valuation method. Since we focus on valuating short-term consumption flexibility in a comprehensible and assessable way, we built our own appropriate process for electricity price movements.

## 3 Overview of Short-term Electricity Markets

## 3.1 Market Instruments

Utilities secure medium- to long-term supply for base and, partially, peak loads far in advance through generation capacity, bilateral supply contracts, and/or acquired futures contracts. Nonetheless, ultimately, they need to bring fluctuating demand in line with supply in the short term. Accordingly, for LS scenarios, short-term market instruments with a timeframe similar to the granted flexibility are relevant to consider. In this section, we describe the structures we observe in European and North American power systems. However, not all markets feature every market instrument.

Utilities balance their short-term demand and supply actively with physically delivered electricity market instruments and passively with the help of external “balancing power” the system operator controls (Biegel et al., 2014). Figure 2 illustrates the typical instruments available for adjusting to consumption in the short term.

![](/api/attachments/JM9FQ2EM/fulltext/images/d378a8a5d2aabf814caea489c9210c099fd8829761dbe27583a5b9de878c99d2.jpg)  
Figure 2. Market Instruments for Adjustment to Consumption

Dispatching balancing power is costly, much more expensive than electricity spot market prices (Strüker & van Dinther, 2012). Therefore, actively adjusting power to deal with fluctuating consumption via purchasing a sufficient volume of physical electricity contracts is the preferred means for utilities in need for additional electricity supply and our subject of research. “Physical electricity contracts” are standardized contracts on the physical delivery of a certain amount of electricity over a specified period. Further, “actual consumption or production as part of contract fulfillment” (Benth, Saltyte Benth, & Koekebakker, 2008) characterize such physical electricity contracts.

Utilities, just like other market participants, commonly trade physical electricity contracts on electricity spot markets close to the time of delivery. Integrating renewable energy sources into the grid increases utilities’ demand for spot market flexibility due to these sources’ volatile electricity production. This demand is expressed in rising trading volumes on electricity spot markets (e.g., EPEX SPOT, 2015). We focus our research to the perspective of a utility that conducts intraday trades on the spot market to procure additional physical electricity contracts in order to balance its short-term demand and supply. Whenever such a utility seizes flexibility to shift loads to another period, it secures savings as high as the difference in spot market prices. In other scenarios, that utility could possibly offer gained capacity on the spot market or on the market for balancing power with higher margins. However, because this latter market type is complex, difficult to predict, and differs between countries, taking a close look at it would exceed this paper’s scope.

The small flexibility of electricity production, restricted by technical and regulatory constraints, can even cause negative spot prices for the physical electricity contracts (Schneider, 2012). At times, for example, a surge in wind power may coincide with little demand for electricity or slow reduction of conventional power plant capacity. The regulatory framework in Germany, which has given electricity generated from renewable sources feed-in guarantees and precedence over conventional sources, is an origin to such issues (Frondel, Ritter, Schmidt, & Vance, 2010). Additionally, the share of renewable energy sources in Germany’s electricity production has risen constantly (Kiesel, 2015) and, thus, caused increasing price volatilities (Nicolosi & Fürsch, 2009). Therefore, negative prices have appeared more frequently in Germany than in other markets. Researchers expect negative prices to occur more frequently in the future (Brijs, de Vos, de Jonghe, & Belmans, 2015). DR is a powerful response to negative electricity prices. First, procuring physical electricity contracts at times of negative prices will prove especially valuable for load delivery. Second, ISenabled LS can help bring electricity consumption into line with fluctuating production, which will counteract excess supply. Nonetheless, the extent of the increase in non-positive electricity spot prices remains uncertain. In fact, due to regulatory frameworks, it could remain a phenomenon limited to few electricity markets, such as the German-Austrian market. Our spot market data analysis suggested that, so far, negative spot prices have proven to be exceptions. Hence, we do not work on integrating them in this paper’s artifact. As such, we note that the value derived in our model is set on the lower bound of DR’s potential.

## 3.2 Market Segments

Utilities trade physical electricity contracts sequentially on three interconnected types of short-term markets: day-ahead, hour-ahead, and real-time electricity markets (Umutlu, Dorsman, & Telatar, 2011). Spot markets, which in our definition (corresponding to Wilson, 2002) signify the intraday market, often comprise both hour-ahead and real-time segments; in other environments, they are limited to the latter.

Day-ahead and hour-ahead markets are, technically speaking, forward markets in which participants trade electricity contracts in advance for specific times of the day. On a “day-ahead market”, two-sided blind auction mechanisms determine the price levels for physical electricity contracts on electricity delivery in the following day’s timeframe (between midnight and midnight). Supplying and demanding parties place commitment bids (each of which comprise load volume and price) regarding single hours or blocks of hours of the following day. After the day-ahead market closes for submissions, the market operator integrates bids into intersecting supply and demand curves, which results in a panel of electricity contract prices for each hour of the following day. To quote blocks of hours, one simply averages the respective single-hour prices. That panel provides the starting point for the electricity spot markets and power transmission planning. Spot markets enable participants to continuously trade electricity contracts in shorter periods before delivery. This way, in reaction to prediction errors or other deviations from their plans, market participants can further balance their schedules by selling or purchasing replacement energy.

The “hour-ahead market” bridges the gap between the end of the auction on the day before delivery and the actual delivery hour the contractors have agreed on. Participants can purchase physical electricity contracts for any future delivery hour of the day, starting shortly after the market operator has quoted the day-ahead prices. Since one can purchase contracts in advance without exposure to uncertain price movements, this form of procurement mitigates risk. The market design may include “gate closure”, indicating that a contract’s trade on the hour-ahead market is to terminate at a fixed time before the delivery hour.

The “real-time market” is the segment for settling remaining deviations from day-ahead or hour-ahead schedules as electricity consumption fluctuates throughout the day. Participants trade electricity for immediate or the earliest possible delivery. Therefore, considering marginal costs, they “can bid the prices they require (offer) to increase (decrease) their generation, or decrease (increase) their consumption” (Umutlu et al., 2011, p. 113).

As we mention above, we focus on intraday (i.e., spot) markets for procuring electricity, which are suitable for modeling short-term flexibility in electricity consumption. If hour-ahead markets are available, they provide the first option to procure electricity in advance at reduced exposure to price risk. Procuring electricity from the real-time markets close to the time of consumption is the second option.

## 3.3 Market Differences

Hour-ahead markets exist in most deregulated European power systems but generally not in U.S. power systems. An exception is California, where the California Independent System Operator provides an hour ahead market segment. Power system operators for the northeastern states of the US (ISO-NE and PJM) and for Texas (ERCOT), for instance, operate real-time instead of hour-ahead markets. The three largest European spot markets incorporate hour-ahead segments, each of which allows participants to trade electricity across several countries’ power grids: the Amsterdam Power Exchange (APX) for the Netherlands, United Kingdom, and—with the closely associated market Belpex—Belgium; the European Power Exchange (EPEX SPOT) for France, Germany, Austria, and Switzerland; and Nord Pool Spot for the Scandinavian and Baltic countries.

In these hour-ahead markets, participants typically trade physical electricity contracts in hourly units. Hence, the market introduces 24 new single-hour electricity contracts daily following a day-ahead auction. For select countries, participants can also purchase finer granularities on APX (30-minute units for UK), Nord Pool Spot, and EPEX SPOT (15-minute units for Austria, Germany and Switzerland). At all times, the next available electricity contract fulfills the function of real-time trade because it accomplishes earliest possible load delivery. Therefore, in European hour-ahead markets, one can compare the final spot price for an electricity contract at market closure to a real-time price, although there is no designated real-time market before the spot market closes and balancing power trade remains. For reasons of data availability, we study final spot prices for electricity contracts from EPEX SPOT’s hour-ahead market, which serve as a substitute for real-time prices.

## 4 Model

## 4.1 Problem Setting

We use the electricity markets and market instruments we describe in Section 3 as the basis for evaluating IS-enabled, short-term flexibility in electricity consumption. Utilities have three reasons in particular to get to know the monetary value of this flexibility before taking DR actions. First, they must cover technological investments such as AMI and operating costs for IS infrastructure, administration, and consumer relations. Second, they have to compensate consumers for releasing some of their flexibility. Third, utilities should monetarily compensate themselves to reward the business hazards of DR. For instance, DR involves risks about general consumers’ acceptance, opportunity costs through expended capital and operational risks such as technical breakdowns.

To summarize, a utility needs a DR business case that provides a basis to estimate cash flows from LS. Because we expect that AMI will enable several business cases for utilities besides DR (e.g., deducing accurate load profiles to improve generation capacity and power transmission planning), we are convinced that more than one single case will justify necessary investments and operating costs for IS infrastructure.

## 4.2 Assumptions and Case Distinction

We consider single-hour physical electricity contracts with our valuation method because single-hour contracts are the most common unit of short-term electricity trade. Such a contract comprises the delivery of a certain amount of electricity during a 60-minute period starting on the hour. To deliver loads, utilities procure one or several of such electricity contracts. If a utility needs more than one single-hour contract due to a multi-hour consumption pattern or a high amount of required electricity, the utility may procure all electricity contracts at the same time.

Assumption 1: A utility purchases all single-hour electricity contracts necessary to deliver a load at once.

One can transfer our model to half- or quarter-hourly contracts without losing its meaning. Nevertheless, we assume a common basis of single-hour electricity contracts for generality. Furthermore, we need to assume that the utility can expend electricity contracts as purchased from the markets without transmission restrictions.

Assumption 2: Utilities face no physical restrictions in procuring and delivering electricity.

Because procuring electricity from both hour-ahead and real-time markets pertains to our research question, we develop a method to accommodate both cases. Hour-ahead markets enable one to procure electricity contracts in advance for hours during the LS window. Because procuring electricity contracts in advance reduces price risk compared to the real-time market, utilities ought to prefer procuring electricity on hourahead markets. Therefore, we distinguish between the two markets based on whether a utility has access to an hour-ahead market. We discuss hour-ahead procurement in Section 4.3. When an hour-ahead market does not exist, utilities need to procure electricity from the real-time market—a case more complex to evaluate. We discuss and formalize an appropriate deferral real option in Section 4.4. A third case is that the LS window spans more hours than electricity contracts are available for hour-ahead procurement. We discuss this case in Section 4.5.

Figure 3 summarizes the three cases. It depicts an example of a LS decision that a utility has to make just before 1 p.m. In the first two cases, the LS window spans until the evening. Load delivery may first possibly start at 1 p.m. Whether an hour-ahead market is available to the utility determines hour-ahead or real-time procurement. In a third scenario, the LS window spans until the next morning, which means some singlehour contracts are unavailable for hour-ahead procurement until a day-ahead auction yields the panel of electricity prices for the next day (which is, for example, at 3 p.m. on EPEX SPOT). In Figure 3, we depict single-hour contracts as squares (similarly to Figure 2); dark-shaded squares indicate example contracts a utility might decide to procure.

![](/api/attachments/JM9FQ2EM/fulltext/images/4bd954d82f456bdec43521d62a6a28b5683693f65d5763e084fae6213e165238.jpg)  
Figure 3. Case Distinction in Example LS Scenarios

## 4.3 Valuation with Hour-ahead Procurement Available

In considering hour-ahead procurement possibilities, we broaden the approach applied in our previous work (Fridgen et al., 2015). A consumer that offers flexibility in when they consume electricity still expects the utility to start delivering a load not later than a certain time. This specified time is <sub>T</sub> hours from the first possible delivery hour, which indicates LS’s maximum duration. is the beginning of the next hour. Ceteris paribus, the utility has no spare electricity on hand, which leaves it with no option to instantly deliver a load apart from choosing balancing power. The next available single-hour contract is the utility’s earliest possibility to procure necessary electricity.

Assumption 3: Delivering a load can begin on the next hour at the earliest.

We further assume that a utility that intends to adjust its supply situation can procure replacement energy from the hour-ahead market up to the beginning of the hour it needs to deliver a load. The assumed situation comes close to reality at APX, on which a utility may procure physical electricity contracts up to five minutes before beginning to deliver a load. In other markets that terminate trade earlier (gate closure), a utility might respond by purchasing extra electricity contracts in anticipation of additional loads coming in after the gate closes. Future research could integrate such an approach into our valuation method.

Assumption 4: In hour-ahead markets, electricity contracts are available for purchase up to zero minutes before the beginning of the delivery hour (technically speaking, without early gate closure).

Just before $\mathrm { t } = 0$ , one can observe prices for several single-hour electricity contracts in the LS window on the hour-ahead market. First, one can observe the spot price $\mathsf { S } _ { 0 } ^ { 0 }$ for delivery beginning in $\mathrm { t } = 0$ during the first possible delivery hour. Second, one can observe a number of prices ${ \sf S } _ { 0 } ^ { \sf t }$ for the following hours’ contracts. Henceforth, we notate the time one observes a spot price in subscript and the delivery time in superscript.

If the utility can deliver the required load over the course of one hour, it selects the cheapest single-hour contract available from the hour-ahead market in $\mathrm { t } = 0$ to schedule load delivery and can, thereby, mitigate its exposure to price changes. In its decision, the utility follows a minimum consideration:

$$
\min \{S _ {0} ^ {0}, \dots , S _ {0} ^ {\mathrm{T}} \} = \min _ {t \in \{0, \dots , T \}} \{S _ {0} ^ {t} \}\tag{1}
$$

In the event that the utility needs to deliver the load over the course of more than one hour, it can adjust the optimal procedure as follows. The adjustment depends on whether the utility may pause and split the delivery between non-consecutive hours. If doing so is possible, the utility simply selects the lowest-priced electricity contracts during the LS window in the appropriate quantity, which is similar to Equation 1. If the utility must deliver the load uninterruptedly, it should regard the average prices of sets of consecutive singlehour contracts. The utility then selects the set of consecutive contracts with the lowest average price again according to Equation 1.

We define $\mathrm { A } _ { \mathrm { x } }$ as a set of all combinations of consecutive delivery hours between $\mathrm { t } = 0$ and $\mathrm { t } = \mathrm { T }$ (respecting constraints). $\mathsf { a } _ { \mathrm { x } , \mathrm { t } ^ { * } } \in \mathsf { A } _ { \mathrm { x } }$ are the elements of $\mathrm { A } _ { \mathrm { x } }$ , where $\mathrm { t } ^ { * } \in [ 0 , \mathrm { T } ]$ denotes the beginning of delivery. We need to minimize the price sum of these delivery hour combinations:

$$
\min _ {t ^ {*}} \bigl \{\sum_ {t \in [ t ^ {*}, t ^ {*} + x - 1 ]} S _ {0} ^ {t} \bigr \}\tag{2}
$$

For example, if a utility has to initiate a load delivery between the beginning of the next hour $( \mathrm { t } = 0 )$ and three hours in the future $( \mathrm { ~ T ~ } { = } 3 \mathrm { ~ } )$ for the duration of two consecutive hours, then we have $\mathrm { A _ { x } } = \{ \mathrm { a _ { 2 , 0 } } , \mathrm { a _ { 2 , 1 } } , \mathrm { a _ { 2 , 2 } } , \mathrm { a _ { 2 , 3 } } \}$ . Therefore, we search the minimum sum of two consecutive prices; that is, min $\{ ( \mathrm { S } _ { 0 } ^ { 0 } + \mathrm { S } _ { 0 } ^ { 1 } ) , ( \mathrm { S } _ { 0 } ^ { 1 } + \mathrm { S } _ { 0 } ^ { 2 } ) , ( \mathrm { S } _ { 0 } ^ { 2 } + \mathrm { S } _ { 0 } ^ { 3 } ) , ( \mathrm { S } _ { 0 } ^ { 3 } + \mathrm { S } _ { 0 } ^ { 4 } ) \}$

We can expect the utility to realize a monetary advantage through LS, which we—for simplicity—present in the single-hour delivery case. Without flexibility, the utility would need to pay the next hour’s spot price $\mathsf { S } _ { 0 } ^ { 0 }$ From an ex ante perspective, the utility’s decision on LS yields a monetary advantage . is the difference of the minimum procurement price according to Equation 1 and the next hour’s spot price ${ \sf S } _ { 0 } ^ { 0 } \mathrm { . }$ :

$$
V = \max \{S _ {0} ^ {0} - S _ {0} ^ {0}, \dots , S _ {0} ^ {0} - S _ {0} ^ {\mathrm{T}} \} = \max \{0, \dots , S _ {0} ^ {0} - S _ {0} ^ {\mathrm{T}} \}\tag{3}
$$

This monetary advantage is the value of LS flexibility in the hour-ahead electricity market. In a generalized formula, we obtain:

$$
V = \max _ {t \in \{0, \dots , T \}} \left\{S _ {0} ^ {0} - S _ {0} ^ {t} \right\}\tag{4}
$$

## 4.4 Valuation with Real-time Procurement

## 4.4.1 Spot Market Data Analysis

Power systems with real-time instead of hour-ahead markets require one to acknowledge the uncertainty in how intraday prices develop. With real options theory serving as the kernel theory to our artifact, we model a utility’s flexibility to shift loads as a deferral option. Single-hour electricity contracts constitute the underlying asset to this real option (in the following: “underlying”). To analytically assess the deferral option’s value, one requires a stochastic process that appropriately depicts the uncertainty in the underlying price’s development (Benaroch & Kauffman, 1999; Ullrich, 2013). We developed a stochastic process and a valuation model for real-time markets in previous work (Fridgen et al., 2014, 2015). Because this model cannot account for short-term influences on spot prices, we develop an extension in this paper to closer depict spot market reality in the stochastic process.

To determine what real-world factors our stochastic process should respect, we study a time series of historical spot market price data from the German-Austrian market area of EPEX SPOT. The high and increasing capacity of renewable energy sources in this market (Würzburg, Labandeira, & Linares, 2013) is groundbreaking and will be exemplary for other electricity markets in the future. In 2013, the trading volume on the EPEX SPOT intraday markets amounted to 19.7 TWh for the German-Austrian market area (EPEX SPOT, 2015). In comparison, the gross national electricity consumption amounted to 599.4 TWh in Germany (Kiesel, 2015) and 64.5 TWh in Austria (Bundesministerium für Wissenschaft, Forschung und Wirtschaft, 2015). Hence, the German-Austrian intraday market held a 3.0 percent market share in 2013. This share is notable considering that utilities prefer medium- to long-term commitments to secure the major share of electricity supply (which is non-responsive to DR efforts). Also, this share is rapidly increasing: EPEX SPOT’s latest numbers (as of 2015) indicate a trading volume of 26.4 TWh in 2014, which equals a 33.9 percent growth that one can attribute to the transition of electricity generation to renewable energy sources (EPEX SPOT, 2015). Rising trading volume in the intraday market and its location in the core of the interconnected European power grid, which may influence other markets in the future (Würzburg et al., 2013), make the German-Austrian market an interesting object to study.

Market participants trade electricity for the German and Austrian grid in one shared market separate from the other market areas. Quoted in Euro per megawatt hour (€/MWh), single-hour physical electricity contracts are the traded objects. Spot prices are initially the outcome of auctions on the day-ahead market and, thereafter, are impacted by intraday trade up to 15 minutes before delivery.

We retrieved our data set from Thomson Reuters Datastream. Our query yielded final spot market prices for 24 hours on weekdays. To be able to measure sensitivity of DR savings potential to seasonality and historical reference timespans, we conducted statistical analyses on various years (10, 5, 3, and 1) of spot market prices before and including the boundary date 31 May 2014. Because electricity production and consumption are typically linked to the season (Benth et al., 2014), we distinguished between summer, winter, and intermediate seasons. Spring and autumn jointly make up the intermediate season because they are comparable in terms of climatic conditions. From the obtained historical data, we established an hour-to-hour series of electricity spot market prices.

Table 1 depicts the descriptive statistics for the three-year period. This period’s boundary dates encompassed three summers (Jun-Aug; 2011-2013), three winters (Dec-Feb; 2011/12-2013/14), and six intermediate seasons (Mar-May, Sep-Nov; 2011-2014) in the meteorological sense. Over all regarded periods, we observed similar daily patterns in spot price movement. Nonetheless, between the ten- and one-year periods, the overall price means continuously decreased from 48.90 to 39.11 €/MWh mostly due to the rising share of renewable energy sources in electricity production. More and more energy producers integrating renewable energy sources into the grid have impacted electricity market prices (International Energy Agency, 2013). For instance, since 2011, renewable sources have contributed electricity equal to more than a fifth of gross consumption in Germany. To account for this significant trend, we should generally focus on analyzing data over a shorter time series. However, the regarded time series should be long enough to eliminate non-representative influences.

Table 1. Descriptive Statistics for Time Series of Spot Market Prices

<table><tr><td></td><td>Summer</td><td>Winter</td><td>Intermediate</td><td>Overall</td></tr><tr><td colspan="5">Chronology</td></tr><tr><td>Time intervals</td><td>Jun-Aug</td><td>Dec-Feb</td><td>Mar-May, Sep-Nov</td><td>1 Jun 2011-31 May 2014</td></tr><tr><td>Total days</td><td>276</td><td>271</td><td>549</td><td>1,096</td></tr><tr><td colspan="5">Spot prices</td></tr><tr><td>No. of observations</td><td>4,731</td><td>4,658</td><td>9,404</td><td>18,793</td></tr><tr><td>No. of positive values</td><td>4,731</td><td>4,599</td><td>9,394</td><td>18,724</td></tr><tr><td>Mean (€/MWh)</td><td>45.51</td><td>43.98</td><td>44.43</td><td>44.95</td></tr><tr><td>Std. deviation (€/MWh)</td><td>12.32</td><td>23.58</td><td>15.39</td><td>15.55</td></tr><tr><td>Maximum (€/MWh)</td><td>130.27</td><td>210.00</td><td>121.97</td><td>210.00</td></tr><tr><td>Minimum (€/MWh)</td><td>3.02</td><td>-221.99</td><td>-49.06</td><td>-221.99</td></tr><tr><td colspan="5">Hour-to-hour returns</td></tr><tr><td>No. of returns</td><td>4,731</td><td>4,587</td><td>9,389</td><td>18,707</td></tr><tr><td>Mean</td><td>-0.0001</td><td>0.0031</td><td>-0.0003</td><td>0.0006</td></tr><tr><td>Standard deviation</td><td>0.1346</td><td>0.3184</td><td>0.1929</td><td>0.2193</td></tr></table>

The special case of negative spot prices occurred rarely: 69 hourly prices, an insignificant share of 0.37 percent of our data, valued less or equal to zero. Therefore, an assumption to exclude those negative prices hardly affected our data set.

Assumption 5: The modeled real-time market allows no negative spot prices.

This assumption is technically necessary to apply ROA since traditional option pricing models are designed for capital markets. On capital markets, negative prices cannot exist due to investors’ limited liability (i.e., the investors may lose all they have invested but not more than that). In our context, this simplifying assumption will not harm since negative spot prices would only further increase LS savings.

One can expect electricity spot prices to drift toward a season-specific, long-term mean (so-called “mean reversion”, Benth et al., 2014). To form seasonal and time-specific expectations, we determined average daily price curves (see Figure 4). These price curves are representative of days in winter, summer, and intermediate seasons in accordance with the historical data from EPEX SPOT. Following typical human electricity-consumption patterns, each price curve’s minimum is in the morning hours in the spot price for electricity contracts for delivery from 4 a.m. onward. A sharp increase during the morning hours is typical until the price curves reach a plateau around 8 a.m. The price curves tend to decline in the afternoon. In the darker seasons, a substantially elevated price level occurs between 5 p.m. and 9 p.m. From 10 p.m. on, price curves for all seasons take a steady downward slope throughout the night.

We equip our stochastic process to follow the described patterns. In particular, we transformed the spot price series into geometrical hour-to-hour returns. “Returns”, a term we adopted from financial markets, depict the change (slope) in a price curve, which provides a measure for movement in electricity spot prices from hour to hour. We defined geometrical returns <sub>( )</sub> as follows, with <sub>( )</sub> being the observed spot price at hour <sub>t</sub> and <sub>t − 1</sub> indicating the previous hour:

$$
R (t) = \lg \frac {S (t)}{S (t - 1)}\tag{5}
$$

Because we excluded negative and zero spot price values from the data set, we computed geometrical returns only on positive spot prices. Table 1 also depicts descriptive statistics for these hour-to-hour returns. Standard deviations, measures for “volatility” as we phrase it in the following paragraphs, provide an indication of spot price fluctuations depending on the season. Winter featured the highest volatility of returns. This volatility documents the variability in demand or supply from hour to hour, which utilities and grid operators need to balance.

![](/api/attachments/JM9FQ2EM/fulltext/images/68061d1b7321472630be411047e6ea8bf0d5599cd6af6d1327fd6add2ec3e256.jpg)  
Figure 4. Historical Average Daily Price Curves

## 4.4.2 Adjustment of a Geometric Brownian Motion Process

A stochastic process to depict the spot price development of hourly physical electricity contracts should incorporate mean reversion. The “square-root diffusion process” (Cox, Ingersoll, & Ross, 1985) and the “Ornstein–Uhlenbeck process” (Uhlenbeck & Ornstein, 1930; Vasicek, 1977) are common mean-reverting processes for continuous-time valuation. Both require constant mean and volatility, which would not be adequate for an intraday approach because the long-term means and volatilities of single-hour contract spot prices differ considerably from hour to hour. In addition, continuous-time valuation cannot adequately consider trade in hourly increments. As such, one cannot use existing mean-reverting processes to replicate short-term spot price movement in volatile electricity markets. Instead, from an intraday perspective, a discrete-time model suffices to simulate electricity prices.

To reach an appropriate stochastic process, we modify a “geometric Brownian motion” (GBM). A GBM is a simple stochastic process that describes deterministic and uncertain changes of an underlying value—in our case, the electricity spot price —as a function of time . The term , also called “drift”, describes the expected value change of the process during one time step (here, the expected spot price change in one hour). We use $\mu \geq 0$ as the expected relative return to express the drift as a fraction of its current value <sub>S(t)</sub>. The term <sub>σS(t)dW(t)</sub> describes uncertain changes. In this construct, <sub>σ</sub> specifies the volatility of returns, which controls for the influence of coincidence. <sub>( )</sub>, a so-called “Wiener process” (Merton, 1997), models normally distributed returns. We assume a Gaussian distribution for the previously described spot price returns, which their distribution approximately resembles.

Assumption 6: The relative changes in electricity spot prices (returns) are normally distributed.

For rigor, we apply this assumption, which is common in financial markets. Finance research usually assumes Gaussian distribution, although some papers have shown that the assumption does not always hold true (e.g., Fama, 1965). Similarly, researchers have repeatedly used this assumption in electricity markets (Hellström, Lundgren, & Yu, 2012; Huisman & Mahieu, 2003). The assumption helps to depict reality, which it comes close to, even though electricity price distributions at times are not Gaussian and instead feature heavy tails (Mayer, Schmid, & Weber, 2015; Weron, 2009). In the light of our results, we consider this limitation acceptable.

In summary, the following equation describes the GBM of <sub>S(t)</sub>:

$$
\mathrm{d} S (t) = \mu S (t) \mathrm{d} t + \sigma S (t) \mathrm{d} W (t)\tag{6}
$$

Because we apply a discrete-time model, we can use single hourly increments. As a result, one can regard the value change in spot prices <sub>S</sub> as an absolute difference, and the returns of the Wiener process follow a standard normal distribution <sub>N(0,1)</sub>:

$$
\mathrm{dt} = 1, \quad \mathrm{dS(t)} = \mathrm{S(t+1)} - \mathrm{S(t)}, \quad \mathrm{dW(t)} = \mathrm{N(0,1)}\tag{7}
$$

Altogether, in discrete time, the following equation describes the modeled GBM:

$$
S (t + 1) = S (t) (1 + \mu) + \sigma S (t) N (0, 1)\tag{8}
$$

We sought to size the process appropriately so that it would cope with significant intraday patterns in the historical spot price data. Therefore, we set the drift on every hour so that the process reverts toward the long-term mean until the next discrete time step <sub>t + 1</sub>. Hence, continuing the expected relative return <sub>µ</sub> introduced above, is the time-dependent expected relative return of the process. One determines it by using the long-term mean of <sub>S(t + 1)</sub>; namely, $\dot { \mathsf { S } } ( { \mathsf { t } } + 1 )$ . We scale this long-term mean with , an adjustment factor that allows the stochastic process to account for short-term effects. This scaling is reasonable since temporary and unexpected environmental conditions, such as fluctuations of current electricity demand and production, events (e.g., soccer world cup finals), holidays, or weather, can influence the development of electricity spot prices. If several hours’ electricity prices on a specific day are far above their long-term mean, for example, this pattern will likely continue in the next hours. Therefore, the integration of into our model is a major extension compared to the model from our prior work (Fridgen et al., 2015). As a factor for adjusting the mean-reversion speed of <sub>µ(t)</sub>, we further introduce $\Theta \in \dot { [ 0 , 1 ] }$

$$
\mu (t) = \theta \frac {\alpha \dot {S} (t + 1) - S (t)}{S (t)}\tag{9}
$$

Assume $\theta = 1 ;$ doing so sets the expected relative return such that the expected value for the next hour’s electricity spot price equals its adjusted historical mean at that hour, which signifies complete reversion to the adjusted mean. Accordingly, <sub>θ = 0</sub> implies no reversion toward the mean whereby only uncertainty drives the process. Uncertainty depends on a standard Wiener process and on the volatility of hour-to-hour returns, which we obtained from the historical data in accordance with Equation 5. Due to large differences in historical volatility, one should consider the time of day for this parameter, too. Thus, our model considers average, time-dependent historical returns and time-dependent historical volatilities <sub>σ</sub>̇ <sub>(t)</sub>:

$$
S (t + 1) = S (t) + \theta (\alpha \dot {S} (t + 1) - S (t)) + \dot {\sigma} (t) S (t) N (0, 1)\tag{10}
$$

In summary, the spot price expected for the next hour equals the current hour’s spot price, which converges toward the adjusted long-term mean for the next hour (speed-weighted through the meanreversion factor) and integrates a standard normally distributed source of uncertainty. At time <sub>t + 1</sub>, one has to adjust historical return and volatility to the new time of day, which technically creates a new GBM. As a result, we can compare the stochastic process over several discrete time steps to a chain of single-period stochastic processes (with mean reversion and volatility constant for one time step). We refer to this chain as “modified GBM”.

Figure 5 illustrates the resulting process chain through a randomly generated curve for a summer day, compares it to the respective historical average price curve, and illustrates the influence of . The diagram demonstrates how simulated spot prices evolve stochastically around long-term means (for simplicity, we neutralize the adjustment of long-term means here; i.e., ). The law of large numbers indicates that a simulation that averages a sufficient quantity of randomly generated modified GBM should yield the initial average price curves. Our simulation confirms that the expected value of the modified GBM approximates to historical data. This observation indicates that our process provides a realistic base for a subsequent monetary valuation of consumption flexibility.

![](/api/attachments/JM9FQ2EM/fulltext/images/5be739eef680890b7c480770469237234ee7c06b6c63b0518d145a5899eaecfd.jpg)  
Figure 5. Summer Day Simulation of Modified GBM with Different Mean-reversion Speeds

## 4.4.3 Binomial Tree for Spot Price Prediction

We derive a binomial expression of our modified GBM in Equation 10 to assess a deferral option’s value. Cox et al.’s (1979) traditional binomial tree model approximately simulates discrete-time movements of an arbitrary standard GBM (Rostek, 2009). It is a common approach for valuing discrete options and suits ROA (Hilhorst, Ribbers, van Heck, & Smits, 2008). As found in the traditional binomial tree model, $\mathrm { t } = 0$ is our ROA’s starting point, a point in time at which the algorithm has to make a decision about whether to initiate LS. <sub>( )</sub> is the spot price observable on the electricity market at this time; thus, it is known. For any following point in time, spot prices are unknown. The tree forks at each discrete point in time <sub>t</sub>, which reflects the uncertainty in electricity spot price movement.

In each node, spot price movement may continue in either an upward or a downward direction. We define $\mathbf { u } _ { \mathrm { t } } \geq 1$ and ${ \mathrm { d } _ { \mathrm { t } } } \leq 1 \ ( \mathsf { w i t h \ u _ { \mathrm { t } } d _ { \mathrm { t } } } = 1 )$ as the time-dependent factors for up and down movements of the electricity spot price <sub>S(t)</sub>, respectively. Upward or downward movements are not equally likely: $\mathsf { p } _ { \mathrm { t } }$ depicts the time-dependent probability that the process will move into the upside scenario. In our case, this parameter indicates the probability that the electricity spot price will increase in the next hour. $1 - \mathsf { p } _ { \mathrm { t } }$ is the time-dependent probability for the downside scenario.

Assumption 7: Utilities are risk-neutral in their procurement decisions.

Under the assumption of risk-neutrality, Cox et al. (1979) obtain the following equations:

$$
u _ {t} = e ^ {\dot {\sigma} (t) \sqrt {\Delta t}}, d _ {t} = e ^ {- \dot {\sigma} (t) \sqrt {\Delta t}}, p _ {t} = \frac {e ^ {r _ {f} \Delta t} - d _ {t}}{u _ {t} - d _ {t}}\tag{11}
$$

equals for single-hour time steps. Cox et al. (1979) use the parameters in Equation 11 to derive two possible upcoming prices for $\mathrm { S ( t ) } { : \mathrm { S } _ { \mathrm { u } } ( \mathrm { t } + 1 ) } = \mathrm { S ( t ) } \mathrm { u } _ { \mathrm { \Omega } }$ and $\mathrm { S } _ { \mathrm { d } } ( \mathrm { t } + 1 ) = \mathrm { S } ( \mathrm { t } ) \mathrm { d } _ { \mathrm { t } }$ . Since this model builds on the assumptions of risk neutrality and no arbitrage, it allows drifting only in form of the risk-free interest rate $\boldsymbol { \mathrm { r _ { f } } }$ (with $\mathrm { u _ { t } } > 1 + \mathrm { r _ { f } } > \mathrm { d _ { t } } )$ . This restriction is reasonable because Cox et al. (1979) developed their model for pricing financial options in complete and perfect capital markets where arbitrage opportunities would disappear infinitely fast. However, participants in electricity markets are in large part not able to use arbitrage opportunities since utilities usually have to get and deliver electricity exactly at the time of (exogenous) demand. This difference between financial and electricity markets justifies the existence of a mean-reversion property in electricity markets and raises the question of how we can consider mean-reversion in the binomial model without endangering the validity of the given formulas. We modify the traditional model in two aspects. First, we set $\boldsymbol { \mathrm { r } } _ { \mathrm { f } } = 0$ since interest drilled down to one hour is insignificantly low. Second, we treat our mean-reverting property (drift) similar to discrete dividend payments in capital markets, which is a valid application of the traditional model. Indeed, anticipating a discrete future payment in the world of securities is comparable to anticipating expected price movements in a risk-neutral electricity market.

To summarize, we add the discrete mean reversion to the two possible upcoming prices, an approach that resembles discrete dividend payments in Cox et al.’s (1979) original model. Initially observing <sub>S(0)</sub> in $\mathrm { t } = 0$ we obtain the following period’s spot prices <sub>S(1)</sub>:

$$
S _ {u} (1) = S (0) u _ {0} + \theta (\alpha \dot {S} (1) - S (0)), \quad S _ {d} (1) = S (0) d _ {0} + \theta (\alpha \dot {S} (1) - S (0))\tag{12}
$$

Both parts of Equation 12 represent the risk-neutral binomial expression of Equation 10 in consideration of our assumptions and modifications. Figure 6 depicts an exemplified binomial tree model for three future periods. In a generalized form, we introduce $\mathsf { S } _ { \mathrm { Z } _ { \mathrm { t } - 1 } } ( \mathrm { t } )$ for $\mathrm { t } > 0$ as the general expression for arbitrary nodes in the tree. In an according recursion formula, $\mathrm { Z } _ { \mathrm { t } - 1 }$ indicates the composition (“history”) of all time-dependent factors for up and down movements $\mathbf { z } _ { \mathrm { n } } \in \{ \mathrm { u } _ { \mathrm { n } } , \mathrm { d } _ { \mathrm { n } } \}$ , which the algorithm has calculated over all passed time steps $\mathrm { n } = \{ 0 , \ldots , \mathrm { t } - 1 \}$ up to that period <sub>t</sub> (e.g., ${ \sf Z } _ { 2 } = \left\{ { \bf z } _ { 0 } , { \bf z } _ { 1 } , { \bf z } _ { 2 } \right\}$ in ). As we explain above, we need to avoid negative prices in the binomial tree model and, therefore, set the lowest possible price to zero:

$$
S _ {Z _ {t - 1}} (t) = \max \left\{S _ {Z _ {t - 2}} (t - 1) * z _ {t - 1} + \theta (\alpha \dot {S} (t) - S _ {Z _ {t - 2}} (t - 1)); 0 \right\}\tag{13}
$$

![](/api/attachments/JM9FQ2EM/fulltext/images/0bf249ff04ae898d7f7eb704de66c8ea97e39efc6542978028d5f535785b9fd3.jpg)  
Figure 6. Binomial Tree Model for an Exemplified Scenario

For example, if we wish to model the spot price in <sub>t = 2</sub> after two up-movements, we obtain: $\mathrm { S } _ { \mathrm { Z } _ { 0 } } ( 1 ) =$ $\operatorname* { m a x } \{ \mathsf { S } ( 0 ) * \mathsf { u } _ { 0 } + \mathsf { \boldsymbol { \theta } } ( \alpha \dot { \mathsf { S } } ( 1 ) - \mathsf { \boldsymbol { S } } ( 0 ) ) ; 0 \}$ with $\mathrm { Z } _ { 0 } = \{ \mathrm { u } _ { 0 } \}$ (first period) and $\mathrm { S } _ { \mathrm { Z } _ { 1 } } ( 2 ) = \mathrm { m a x } \{ \mathrm { S } _ { \mathrm { Z } _ { 0 } } ( 1 ) * \mathrm { u } _ { 1 } + \mathsf { \boldsymbol { \theta } } ( \alpha \dot { \mathrm { S } } ( 2 ) -$ $\mathrm { S } _ { \mathrm { Z } _ { 0 } } ( 1 ) ) ; 0 \}$ with $\mathrm { Z } _ { 1 } = \{ \mathrm { u } _ { 0 } , \mathrm { u } _ { 1 } \}$ (second period). Note that is the price that is (in this example) currently observable on the electricity spot market.

This modified GBM is a chain of single-period stochastic processes according to Equation 10, each calibrated in every time step. It conveys a plausible depiction of the spot price development of single-hour electricity contracts, with time-dependent historical mean prices and volatilities of the hour-to-hour returns reflecting intraday patterns. We consider IS implementation in the LS context to be able to cope with the high complexity <sub>(2</sub><sup>t</sup><sub>)</sub> involved in the binomial tree. Heuristics may help to obtain analytical results for longer periods under consideration if necessary.

To appraise the binomial tree’s applicability, we apply it to a simple real-world scenario. Our example depicts the charging process of a plug-in electric vehicle (PEV). The commuting user of the PEV reaches the workplace at 8 a.m. $\left( \mathrm { t } = 0 \right)$ on a winter day and connects it to a power outlet. The user gives the utility the right to defer the charging process throughout the morning provided the vehicle is ready for reuse at 1 p.m. For this example, we assume that the car can fully charge in one hour due to the charging outlet’s charging speed or the car battery’s remaining capacity. Hence, the utility can procure the necessary electricity as one single-hour contract but must initiate the process no later than noon. The utility hourly decides to either initiate the charging or defer the load by another hour. It may use its LS right at 8 a.m., 9 a.m., 10 a.m., and 11 a.m. In case the utility has not released the load by 11 a.m. , the LS window closes: at noon, the utility must initiate the charging process because the deferral option has expired at 11 a.m.

## 4.4.4 Value Determination

Although the concept of real options is distinct from financial options in the type of the underlying, ROA reverts to financial options in one respect: one can valuate a real option by replicating it as a financial option (Copeland & Antikarov, 2003). We can model the designed deferral option as a call option. A call option is a right, but not an obligation, to buy an object (e.g., an asset) at a previously fixed price. This technical model is interpretable in the short-term LS context: to serve a load, a utility must procure electricity from the real-time market. The timing of this investment is variable; through LS, the utility gains the right to defer the purchase of the necessary electricity contracts. Up to the option’s expiration in time , while the right to defer is valid, the utility can decide to buy the next available electricity contract on the spot market and emit the initiating control signal for load delivery through AMI. Exercising the option during that time span means expecting a monetary advantage compared to initiating the load at the latest possible time. The latter is the period after expiration <sub>(T</sub> <sub>+</sub> <sub>1)</sub>: if the utility has not served the load by expiration <sub>T</sub>, in the following period, it will be obliged to do so because the right to defer has expired.

We set the exercise or strike price equal to the adjusted long-term mean at one hour after the deferral option’s expiration so that exercising the option (i.e., serving the load) any earlier will precipitate an expected monetary advantage:

$$
\mathrm{K} = \alpha \dot {\mathrm{S}} (\mathrm{T} + 1)\tag{14}
$$

We compute as the ratio between the sum of realized spot prices at the recent hours before the initial period <sub>( )</sub>, and the sum of corresponding long-term means:

$$
\alpha = \frac {\sum_ {x = 1} ^ {n} S (0 - x)}{\sum_ {x = 1} ^ {n} \dot {S} (0 - x)}\tag{15}
$$

Note that, since we use ROA, <sub>α</sub> has to be constant for each process simulation because common option pricing models presume a constant strike price <sub>K</sub>.

Specifically, one models a deferral option as an American call. This type of a call option features the characteristic of being exercisable at any period during its lifetime. Therefore, a DSS using this model would need to execute three steps iteratively to optimally procure electricity from the market:

1) Model the electricity spot price pursuant to Section 4.4.3

2) Calculate option values for every node in the binomial tree by going through it systematically in reverse, from end nodes to root (i.e., to the point in time at which one has to make the decision), and

3) Decide whether exercising the option is preferable at the current hour. If not, the system would wait for the next hour’s spot price to become observable, then update the information and start again at step 1.

This procedure iterates until the option expires.

Regarding step 2, one needs to assign option values to every node in the tree to make the decision between exercising the option at the current point in time and waiting until the next hour. Considering the leaves of the tree (also known as end nodes) at expiration , either: 1) the expected spot price in is higher than strike price <sub>K</sub>, which means the mandatory delivery in <sub>T + 1</sub> would be preferable and would render the option worthless; or 2) the expected spot price in is below (or equal to) the strike price, which indicates one would prefer exercising the option. Again, one can use the composition of all states $\mathrm { Z _ { T - 1 } }$ to refer to individual nodes. Depending on $\mathrm { Z _ { T - 1 } }$ , the option values $\mathrm { C } _ { \mathrm { Z } _ { \mathrm { T } - 1 } } ( \mathrm { T } )$ for the leaves of the binomial tree equal the differences between the strike price and the respective current spot prices (i.e., the expected monetary advantage) unless the option is worthless:

$$
C _ {Z _ {T - 1}} (T) = \max \bigl \{K - S _ {Z _ {T - 1}} (T); 0 \bigr \}\tag{16}
$$

Proceeding from to $\mathrm { T } - 1 \ \mathrm { [ T - m ] }$ , another possibility exists. Since the option has not expired yet, it may be preferable not to exercise said option but to wait until period $\left[ \mathrm { T } - \mathrm { m } + 1 \right]$ . Since we have already calculated the option values for this following period, we can constitute an expected value using the probability for an upside or downside scenario from Equation 11.

With the two aforementioned possibilities, one determines the option value in each node as the maximum of either the value of exercising the option or the value of deferring the decision until the next hour. This procedure yields the following general formula for an m-th recursion, with $\in \{ 1 , \ldots , \mathrm { T } \}$

$$
C _ {Z _ {T - m - 1}} (T - m) = \max \left\{ \begin{array}{c} K - S _ {Z _ {T - m - 1}} (T - m); \\ p _ {T - m} * C _ {Z _ {T - m - 1}, u _ {T - m}} + (1 - p _ {T - m}) * C _ {Z _ {T - m - 1}, d _ {T - m}} \end{array} \right\}\tag{17}
$$

Generally, for each node in the binomial tree, we can determine the theoretical value of exercising (i.e., serving the load) at particular times and compositions of states. After having computed all option values from <sub>t = T</sub> down to <sub>t = 0</sub>, the DSS can finally suggest whether exercising the option to procure electricity from the market at the current point in time is preferable—in other words, worth more than waiting considering the expected value of the whole binomial tree. If exercising the option at the current point in time is not preferable, the system would wait for the next hour’s spot price to become observable and calculate an updated binomial tree to decide on exercising the option again. This procedure iterates until the algorithm exerts the option or the option expires. We can finally derive the value of LS by comparing the spot price at the starting point of the option (at which point the utility would have served the load without using the consumer’s flexibility) to the realized purchasing price that the DSS chooses.

On a remaining note, Ullrich (2013) identifies necessary assumptions for validly applying financial option pricing models for ROA. The author surveys existing publications and concludes that many authors that apply option pricing models neglect requirements. We verified our ROA method for real-time markets as being a valid application of financial option pricing models because it meets several important requirements. Following Ullrich (2013), we first confirm that our real-time model fulfills the assumption of a “complete market” because the electricity markets enable continuous trade of our model’s underlying object (physical electricity contracts). Second, the spot prices for physical electricity contracts evolve according to several tied single-period GBMs with corresponding constant variances. Third, the strike price is visible to the algorithm and constant throughout the option’s duration. Fourth, the maturity of the option is also visible and specified because it derives from the length of the LS window, with defined times of possible exercise.

## 4.5 Contracts Unavailable for Hour-ahead Procurement

The availability of electricity contracts in hour-ahead markets is limited. For a given day, the 24 single-hour contracts only become available following the day-ahead auction (e.g., 3 p.m. on the previous day at EPEX SPOT). Therefore, the LS window might span more hours than electricity contracts are available for procuring on the hour-ahead market, which is typically the case if a consumer grants LS flexibility beyond midnight before the following day’s contracts become available.

Consider an example of a utility that needs to make an initial LS decision at 1 p.m., which is before the hourahead markets of EPEX SPOT and Nord Pool Spot open for the following day. A consumer grants flexibility to defer a load until the next morning. At 1 p.m., it is not possible for the utility to take electricity contract spot prices for delivery hours after midnight into consideration. Such spot prices for early morning hours are, however, often lower than for delivery hours during the day or evening (see Section 4.4.1).

If the utility would limit itself to procuring electricity contracts available at 1 p.m., the utility could only schedule load delivery before midnight and would, therefore, cede the savings potential of later delivery hours. Instead, it should employ the valuation method for procuring contracts from the real-time market to assess the value of LS beyond midnight. The spot price for the last contract available in hour-ahead trade becomes <sub>( )</sub> in the model. The utility then calculates and compares the LS value based on real-time procurement to the riskless alternatives in the hour-ahead market. It decides for the more rewarding option. If LS beyond midnight appears more rewarding, the utility revisits this decision hourly, particularly once the spot prices for the following day’s electricity contracts become observable in the hour-ahead market. We refrain from presenting the case in more detail since it combines the static hour-ahead and dynamic realtime procurement cases.

## 5 Evaluation

## 5.1 Evaluation Approach

DSR methodology calls for evaluating a developed artifact to provide evidence that the artifact is useful (Gregor & Hevner, 2013). To assess its usefulness, we again distinguished between our models for hourahead and real-time procurement. The first model (see Section 4.3), which deals with procuring electricity from the hour-ahead market, involves a simple choice between available electricity contracts. No disadvantages can result from following this logic, so we did not additionally evaluate the model. For the second model (see Section 4.4), which deals with procuring electricity from the real-time market, the developed dynamic valuation method incorporates a stochastic price model and a binomial tree model. Following Hevner et al. (2004, p. 86), “the selection of evaluation methods must be matched appropriately with the designed artifact and the selected evaluation metrics”. Possible evaluation methods for DSR include a case study, optimization, simulation, or informed argument. We took an ex post perspective and compared the prices a utility pays to procure electricity for an arbitrary load delivery with and without LS flexibility. A negative difference can result. The virtual savings our model achieved in many different simulated scenarios indicate the method’s effectiveness.

Based on historical data from EPEX SPOT, we tested a set of random LS scenarios that could have occurred in the past. We randomly drew a date and time at which a consumer could have granted LS flexibility. Then we took the historical spot price at the initiating date and time as the starting point to the operations in our model. Historical statistics provided spot price means and return volatilities appropriate for the season and the hour of the day. On this basis, we used our modified GBM to forecast spot price development. A second draw generated the length of the LS window. With values between 1 and 12 hours from the initiating time, we considered the deferral of delivery long enough to realistically cover most LS scenarios yet short enough to avoid distorting simulation results with overly optimistic or unrealistic scenarios. Up to the latest possible delivery hour, a historical spot price series provided the necessary benchmark for decisions.

Following our method, we then generated a binomial tree and employed our recursive formulae to derive the value of the deferral option—at first, for the initiating period. In each period, the algorithm repeatedly decided on initiating or postponing load delivery. Reiterating until the model indicated that delivery was preferable, the algorithm derived the time of load delivery. By comparing the historical spot price at this chosen hour to the initial spot price, we calculated the saving (positive or negative) that would have been realized in the simulated scenario by adhering to our method. Running through LS scenarios that could have occurred over three recent years (1 June 2011 to 31 May 2014), we repeated this approach 500,000 times. Although 10,000 simulation runs already showed similar overall results, a larger number increased the results’ quality for sensitivity analyses.

Table 2. Evaluation Parameters

<table><tr><td>Parameter</td><td></td><td>Value</td></tr><tr><td>Simulation runs</td><td></td><td>500,000</td></tr><tr><td>Evaluation data count</td><td></td><td>18,794</td></tr><tr><td>Historical reference timespan (a)</td><td></td><td>Randomized</td></tr><tr><td>Date and time of LS initiation</td><td> $t_0$ </td><td>Randomized</td></tr><tr><td>Expiration, or LS window length (h)</td><td>T</td><td>Randomized</td></tr><tr><td>Mean-reversion speed</td><td>θ</td><td>Randomized</td></tr><tr><td>Adjustment reference interval (h)</td><td></td><td>Randomized</td></tr><tr><td>Adjustment factor</td><td>α</td><td>Computed</td></tr><tr><td>Risk-free interest rate</td><td> $r_f$ </td><td>0</td></tr><tr><td>Time increment (h)</td><td>Δt</td><td>1</td></tr></table>

To automate this simulation, we implemented the created artifact prototypically in the form of an Excel workbook supported by Visual Basic for Applications (VBA) macros. Table 2 depicts the evaluation parameters we employed. Among these parameters, we randomized the historical reference timespan (10, 5, 3, or 1 years) for seasonal statistics, the mean-reversion speed (between 0 and 1, inclusive) and the reference interval for computing the adjustment factor <sub>α</sub> (1 to 48 recent hours or no adjustment at all), to compare those parameter values as the basis for LS decisions.

## 5.2 Results and Discussion

Summarizing all scenario results of our ex post simulation, we determined the average (AV) savings a utility would have realized by seizing LS flexibility and the corresponding standard deviations (SD) that depict volatility. Figure 7 illustrates the distribution of absolute savings in a histogram. The interval of 0–2 €/MWh that depicts small savings featured the most observations. However, we saw a high frequency of scenarios (12.8%) with savings ≥ 20 €/MWh. LS based on our prediction also sometimes turned out negative when spot prices developed in a direction other than predicted. Yet, one can see that our approach provided a benefit in the majority of scenarios (72.3%). We also computed relative savings, which express the realized absolute savings at load delivery as a fraction of the respective spot prices at LS initiation $( \frac { \mathsf { S } _ { 0 } - \mathsf { S } _ { \mathrm { t } } } { \mathsf { S } _ { 0 } } )$ . On average, LS according to our designed method yielded positive results in a relevant magnitude. It achieved average savings of 4.93 €/MWh (or 11%) over all randomized input parameters. The standard deviation amounted to 17.51 €/MWh or 39 percent of the initial spot price $\mathsf { S } _ { 0 } ,$ , which, in turn, averaged to 44.45 €/MWh (or 100%).

![](/api/attachments/JM9FQ2EM/fulltext/images/b03d3ada7bb87a8b17d00934dc376dfd826eeddb76c89b33afbd9478d00a9ace.jpg)  
Figure 7. Histogram of Absolute Savings (in Intervals of 2€/MWh)

To discuss our evaluation results, we distinguish between sensitivity in the scenarios and in the model parameters. Table 3 contains results regarding scenario sensitivity

We observed the lowest relative savings in summer scenarios. This result might be related to low volatility in electricity prices in the summer (12.32 €/MWh, c.f. Table 1) since less differences in spot prices over a LS window mean less savings potential. However, a counterargument is the observation that volatility in intermediate seasons was similarly low (15.39 €/MWh), while intermediate season scenarios featured the highest average savings.

We further observed that realizable savings rose as the length of the LS window increased. Accordingly, we conducted a Wilcoxon signed-rank test for matched pairs. This statistical test indicated to maintain the null hypothesis of the averaged relative savings being dependent on the according deferral option maturities. We additionally measured a Pearson product-moment correlation coefficient of 0.9953 between the LS window length and averaged relative savings. Hence, the monetary value of LS flexibility increases for every additional period in the LS window.

Table 3. Ex Post Simulation Results (Scenario Sensitivity)

<table><tr><td></td><td>AV absolute savings (€)</td><td>SD absolute savings (€)</td><td>AV relative savings (%)</td><td>SD relative savings (pp)</td><td>Scale (rel. savings)</td></tr><tr><td>Overall</td><td>4.93</td><td>17.51</td><td>11.1</td><td>39.4</td><td>1.00</td></tr><tr><td colspan="5">Season</td><td></td></tr><tr><td>Summer</td><td>4.32</td><td>12.42</td><td>9.5</td><td>27.4</td><td>0.86</td></tr><tr><td>Intermediate</td><td>5.43</td><td>15.57</td><td>12.2</td><td>35.1</td><td>1.10</td></tr><tr><td>Winter</td><td>4.54</td><td>24.22</td><td>10.4</td><td>55.4</td><td>0.94</td></tr><tr><td colspan="6">LS window length (h)</td></tr><tr><td>1</td><td>1.74</td><td>17.01</td><td>3.9</td><td>38.2</td><td>0.35</td></tr><tr><td>2</td><td>2.68</td><td>17.14</td><td>6.0</td><td>38.4</td><td>0.54</td></tr><tr><td>3</td><td>3.30</td><td>17.59</td><td>7.4</td><td>39.5</td><td>0.67</td></tr><tr><td>4</td><td>3.82</td><td>17.13</td><td>8.6</td><td>38.6</td><td>0.77</td></tr><tr><td>5</td><td>4.44</td><td>17.44</td><td>10.0</td><td>39.1</td><td>0.90</td></tr><tr><td>6</td><td>4.92</td><td>17.32</td><td>11.1</td><td>39.0</td><td>1.00</td></tr><tr><td>7</td><td>5.30</td><td>17.53</td><td>12.0</td><td>39.6</td><td>1.08</td></tr><tr><td>8</td><td>5.87</td><td>17.73</td><td>13.2</td><td>39.9</td><td>1.19</td></tr><tr><td>9</td><td>6.25</td><td>17.92</td><td>14.1</td><td>40.4</td><td>1.27</td></tr><tr><td>10</td><td>6.62</td><td>17.74</td><td>14.9</td><td>40.0</td><td>1.35</td></tr><tr><td>11</td><td>7.25</td><td>17.88</td><td>16.3</td><td>40.2</td><td>1.47</td></tr><tr><td>12</td><td>7.65</td><td>17.76</td><td>17.3</td><td>40.1</td><td>1.56</td></tr></table>

To study the sensitivity of savings to our model parameters, we analyzed simulation results in dependence of changes in parameter values. Table 4 depicts a selection of the tested parameters.

First, we generated scenarios with four historical reference timespans for seasonal statistics and intraday patterns. We discuss our observations even though no statistical comparison was valid due to the small, discrete sample. We saw no substantial difference between the three more recent timespans (1, 3, and 5 years) in average relative savings. A reference timespan of 10 years seemed to result in lower savings. This finding suggests that the more recent timespans describe similar situations in the EPEX SPOT market and, therefore, better suit basing LS decisions on. In contrast, 10 years may be too long a timespan to account for developments such as the fast growing integration of renewable energy sources.

Second, we checked whether adjusting the seasonal spot price levels to short-term effects by using the adjustment factor <sub>α</sub> increased savings. A statistical t-test of a sample of average relative savings under short-term adjustment (48 reference intervals forming $\mathfrak { a } \ne 1 )$ against the relative savings without adjustment $( \alpha = 1 )$ indicated to reject the null hypothesis of the means being equal $( \mathsf { p } = 0 . 0 0 0 ^ { \star \star \star } )$ . As such, we can infer that the adjustment factor is a relevant component to our model. With short-term adjustment present, results were superior compared to no adjustment, even though one cannot judge how many hours should optimally serve as the reference interval to this adjustment. Short-term effects, such as the amount of current electricity demand and production, events (e.g., soccer world cup finals), holidays, or weather, seem to influence spot prices, and adjusting the model expectations seems prudent.

Third, we checked if introducing mean reversion toward the long-term mean increased savings. Indeed, a statistical t-test of a sample of average relative savings under mean reversion (100 mean-reversion speeds $0 < \Theta < 1 )$ against relative savings without mean reversion (<sub>θ = 0</sub>) indicated to reject the null hypothesis of the means being equal $( \mathsf { p } = 0 . 0 0 0 ^ { \star \star \star } )$ . As such, we can infer that mean reversion is a relevant component to our model. Spot price prognosis benefits from considering intraday patterns and, thus, contributes to our model’s decision value. However, one cannot determine an optimum for the mean-reversion speed parameter $0 < \Theta < 1$ with sufficient significance.

Table 4. Selected Ex Post Simulation Results (Model Sensitivity)

<table><tr><td></td><td>AV absolute savings (€)</td><td>SD absolute savings (€)</td><td>AV relative savings (%)</td><td>SD relative savings (pp)</td><td>Scale (rel. savings)</td></tr><tr><td>Overall</td><td>4.93</td><td>17.51</td><td>11.1</td><td>39.4</td><td>1.00</td></tr><tr><td colspan="6">Historical ref. timespan (a)</td></tr><tr><td>1</td><td>5.25</td><td>17.49</td><td>11.8</td><td>39.3</td><td>1.06</td></tr><tr><td>3</td><td>5.21</td><td>17.62</td><td>11.7</td><td>39.6</td><td>1.06</td></tr><tr><td>5</td><td>5.11</td><td>17.47</td><td>11.5</td><td>39.3</td><td>1.04</td></tr><tr><td>10</td><td>4.15</td><td>17.46</td><td>9.3</td><td>39.3</td><td>0.84</td></tr><tr><td colspan="6">Mean-reversion speed θ</td></tr><tr><td>0.00</td><td>3.13</td><td>17.30</td><td>7.0</td><td>39.0</td><td>0.64</td></tr><tr><td>0.05</td><td>3.81</td><td>17.52</td><td>8.6</td><td>39.4</td><td>0.77</td></tr><tr><td>0.10</td><td>4.29</td><td>17.22</td><td>9.7</td><td>38.8</td><td>0.87</td></tr><tr><td>0.15</td><td>4.51</td><td>17.98</td><td>10.2</td><td>40.6</td><td>0.92</td></tr><tr><td>0.20</td><td>4.45</td><td>17.10</td><td>10.0</td><td>38.5</td><td>0.90</td></tr><tr><td>0.25</td><td>4.43</td><td>17.58</td><td>10.1</td><td>40.0</td><td>0.91</td></tr><tr><td>0.30</td><td>4.81</td><td>18.51</td><td>10.8</td><td>41.8</td><td>0.98</td></tr><tr><td>0.35</td><td>4.86</td><td>17.74</td><td>10.9</td><td>39.8</td><td>0.98</td></tr><tr><td>0.40</td><td>4.78</td><td>17.59</td><td>10.8</td><td>39.6</td><td>0.97</td></tr><tr><td>0.45</td><td>5.06</td><td>17.47</td><td>11.4</td><td>39.3</td><td>1.03</td></tr><tr><td>0.50</td><td>4.76</td><td>17.31</td><td>10.7</td><td>39.0</td><td>0.97</td></tr><tr><td>0.55</td><td>4.97</td><td>16.99</td><td>11.1</td><td>38.0</td><td>1.00</td></tr><tr><td>0.60</td><td>5.07</td><td>17.41</td><td>11.4</td><td>39.0</td><td>1.02</td></tr><tr><td>0.65</td><td>5.10</td><td>17.50</td><td>11.5</td><td>39.3</td><td>1.03</td></tr><tr><td>0.70</td><td>5.08</td><td>17.03</td><td>11.4</td><td>38.3</td><td>1.03</td></tr><tr><td>0.75</td><td>5.32</td><td>17.10</td><td>11.9</td><td>38.3</td><td>1.08</td></tr><tr><td>0.80</td><td>5.22</td><td>16.66</td><td>11.7</td><td>37.2</td><td>1.05</td></tr><tr><td>0.85</td><td>5.18</td><td>17.29</td><td>11.7</td><td>38.9</td><td>1.05</td></tr><tr><td>0.90</td><td>5.11</td><td>17.88</td><td>11.5</td><td>40.3</td><td>1.04</td></tr><tr><td>0.95</td><td>5.26</td><td>16.82</td><td>11.8</td><td>37.8</td><td>1.07</td></tr><tr><td>1.00</td><td>5.31</td><td>17.42</td><td>11.9</td><td>39.0</td><td>1.07</td></tr><tr><td colspan="6">Adjustment ref. interval (h)</td></tr><tr><td>No adjustment</td><td>4.01</td><td>17.56</td><td>9.0</td><td>39.6</td><td>0.82</td></tr><tr><td>1</td><td>5.18</td><td>17.62</td><td>11.6</td><td>39.5</td><td>1.05</td></tr><tr><td>2</td><td>5.07</td><td>16.83</td><td>11.4</td><td>37.8</td><td>1.03</td></tr><tr><td>3</td><td>5.13</td><td>17.15</td><td>11.5</td><td>38.6</td><td>1.04</td></tr><tr><td>4</td><td>4.90</td><td>17.32</td><td>11.0</td><td>38.9</td><td>0.99</td></tr><tr><td>5</td><td>4.93</td><td>17.07</td><td>11.1</td><td>38.6</td><td>1.01</td></tr><tr><td>6</td><td>4.96</td><td>17.16</td><td>11.2</td><td>38.6</td><td>1.01</td></tr><tr><td>7</td><td>5.25</td><td>18.00</td><td>11.7</td><td>40.2</td><td>1.06</td></tr><tr><td>8</td><td>5.62</td><td>17.50</td><td>12.6</td><td>39.1</td><td>1.13</td></tr><tr><td>9</td><td>4.89</td><td>17.38</td><td>11.1</td><td>39.2</td><td>1.00</td></tr><tr><td>12</td><td>5.09</td><td>17.44</td><td>11.4</td><td>39.1</td><td>1.03</td></tr><tr><td>18</td><td>4.85</td><td>18.51</td><td>10.9</td><td>41.8</td><td>0.99</td></tr></table>

Table 4. Selected Ex Post Simulation Results (Model Sensitivity)

<table><tr><td>24</td><td>5.08</td><td>17.36</td><td>11.4</td><td>38.9</td><td>1.03</td></tr><tr><td>30</td><td>5.01</td><td>17.91</td><td>11.3</td><td>40.4</td><td>1.02</td></tr><tr><td>36</td><td>5.02</td><td>18.81</td><td>11.3</td><td>42.5</td><td>1.02</td></tr><tr><td>42</td><td>4.89</td><td>17.07</td><td>10.9</td><td>38.2</td><td>0.99</td></tr><tr><td>48</td><td>4.90</td><td>17.39</td><td>11.0</td><td>39.2</td><td>1.00</td></tr></table>

We observe that our decision support model resulted in average savings of positive, relevant magnitude. To study the impact of model training on the savings potential, we selected one exemplary set of input parameters: a historical reference timespan for seasonal statistics of one year, the mean-reversion speed = 0.75, and a reference interval for short-term adjustment of eight hours. As Table 4 shows, scenarios with each of these input parameters resulted (ceteris paribus) in the highest savings in an EPEX SPOT setting. We are aware that this combination will not automatically cause the highest savings overall. Yet, to provide a conservative indicator for our model’s usefulness, the trained parameter set resulted in average savings of 5.80 €/MWh (or 12.9%) as Table 5 shows. It also featured a 16 percent lower volatility. We note that, to achieve highest savings overall, one would have to analyze all combinations of model parameters by, for example, an ex post simulation similar to the one we conducted. In addition, when employing the model on another electricity market, one would also need to independently analyze the parameters.

Table 5. Selected Ex Post Simulation Results (Trained Parameter Set)

<table><tr><td></td><td>AV absolute savings (€)</td><td>SD absolute savings (€)</td><td>AV relative savings (%)</td><td>SD relative savings (pp)</td><td>Scale (rel. savings)</td></tr><tr><td>Reference</td><td>4.93</td><td>17.51</td><td>11.1</td><td>39.4</td><td>1.00</td></tr><tr><td colspan="6">Trained parameter set</td></tr><tr><td>Overall</td><td>5.80</td><td>14.86</td><td>12.9</td><td>33.1</td><td>1.17</td></tr><tr><td>12 hour LS window</td><td>8.52</td><td>17.16</td><td>19.2</td><td>38.8</td><td>1.73</td></tr></table>

Even though application scenarios and model assumptions differ, the savings that our models yield stand the comparison to other relevant DR literature. Feuerriegel and Neumann (2014) build a LS scenario for utilities that can procure futures derivatives and participate in day-ahead auctions. In their optimization scenario, they calculate that fully exploiting LS over windows of up to 24 hours would yield averaged absolute savings of 12.30 €/MWh. They further note that savings increase as LS windows get longer. If we assume an equal average LS window length of 12 hours and use the trained parameter set, we can compare our method. As Table 5 indicates, it would yield averaged absolute savings of 8.52 €/MWh. However, Feuerriegel and Neumann (2014) allow for shifting loads to a time earlier than the scheduled time, which enables higher flexibility and savings but is not possible in a real-time scenario. This difference weakens comparability, which one needs to respect when judging the lower amount our model potentially saves on real-time markets. Sezgen et al. (2007) calculate the option value of LS with the help of thermal energy storage systems, which enable LS also in day-ahead markets. In their average case for storage efficiency, the option to shift loads reaches a value of approximately 199,000 \$/MW over five years of operation (20 days a month), which equals 6.91 \$/MWh or 6.17 €/MWh (average exchange rate in June 2015). Our results are of similar magnitude, although Sezgen et al. (2007) designed their approach for day-ahead markets with according market differences. Fridgen, Mette, and Thimmel (2014) simulate the potential of LS in a realtime scenario in which electric vehicle drivers can use AMI to provide information about the start of their next trip to utilities that seek to flexibly deliver loads. In the given scenario, utilities’ savings on charging batteries average between 3.1 and 7.3 percent, which they can use to compensate customers. Our method can potentially save more. Finally, in a hypothetical ex post assessment, we computed that perfect information (in other words, price certainty) could have yielded a maximum of 21.5 percent relative savings. Given that our method saved 11.1 percent, we conclude that it worked quite well.

Altogether, we find the following generalizable insights. First, we conclude that one can use ROA to quantify the value of IS-enabled flexibility in electricity consumption. Second, the option to shift loads bears a positive value. Third, we deem our valuation method advantageous to current practice. We successfully conducted an additional proof-of-concept of our evaluation with real-time prices from the US and found similar results. As such, we see no reason to expect that our model does not apply to markets other than EPEX SPOT.

## 6 Conclusion

The transition to renewable energy sources entails DR efforts to balance increasingly volatile supply through shifting demand. In this paper, we establish a method to evaluate the flexibility of deferring electricity consumption at the time an individual consumer grants such flexibility. Utilities can use the ability to quantify the monetary value of LS when they decide on compensations for the consumer who approves LS. We present three cases that differ mainly in whether they involve an hour-ahead market. If a utility has the option to procure electricity contracts in advance, it can lock in a monetary advantage by purchasing the cheapest contract(s) out of the ones available for upcoming delivery hours of the day as long as they fall in the flexibility period that the consumer allots. Utilities can procure contracts ex ante in the short term on the hour-ahead markets of European electricity exchanges. In electricity exchanges with no hour-ahead market, utilities need to decide whether to deliver the load immediately or at a later point in time basing on predictions. One should be able to apply our generic real-time model to various electricity markets around the world, such as spot markets in the United States and Europe. We establish an appropriate artifact based on the theoretical foundation of real options theory. Addressing a prerequisite, we also develop a stochastic process replicating real-time spot price development in a simple and realistic manner.

Our formal modeling approach has some rather technical limitations. First, the stochastic process for our dynamic real-time market model cannot consider negative spot prices, which can arise in situations of excess supply. Second, we use a standard Wiener process to describe uncertainty, which implies a normal distribution. However, electricity prices feature rather heavy-tailed distributions. Third, anomalies such as technical breakdowns or faulty scheduling in electricity supply can cause immediate and unpredictable price movements (“spikes”) that our stochastic process cannot predict. For all three reasons, the modified GBM simplifies reality, but it proves useful by enabling ROA.

The value derived in our real-time model is typically set on a lower bound for three reasons: first, LS can substitute balancing power in some cases—a significant saving that exceeds the value calculated in our model. Second, preventing peak workload in distribution grids decreases necessary investments in expanding the power grid and in conventionally producing power. Thirdly, in a cautionary approach, we excluded negative electricity spot prices, which have occurred rarely so far but may occur more frequently in the future. To date, our hour-ahead market model is a static approach that does not consider changing external conditions while a utility shifts load. In future research, multiple simultaneously modeled real options for every hour of the intraday market could enhance the savings potential for utilities. Moreover, future research can help develop incentive-compatible tariff structures based on compensations that utilities can offer consumers. Scholars can design application systems for utilities that integrate our valuation model in algorithms. Although we identify ROA as an appropriate approach to identify the value of consumption flexibility, future research could compare the results with another methodology, such as dynamic stochastic optimization.

With our real options approach, we help assess the economic potential of IS-enabled, short-term flexibility in electricity consumption. Our results confirm that real options theory suits evaluating flexibility in IS research and energy informatics in particular. We see similarly promising applications in studying ondemand usage of, for example, cloud computing services and dynamic capacity allocation in business process management. As such, we provide a viable basis to further research consumption flexibility in IS domains and to valuate such flexibility in business practice.

## Acknowledgments

This research was (in part) carried out in the context of the Project Group Business and Information Systems Engineering of the Fraunhofer Institute for Applied Information Technology (FIT).

## References

Albadi, M. H., & El-Saadany, E. F. (2008). A summary of demand response in electricity markets. Electric Power Systems Research, 78(11), 1989-1996.

Amram, M., & Kulatilaka, N. (1999). Real options: Managing strategic investment in an uncertain world. Financial Management Association survey and synthesis series. Boston, MA: Harvard Business School Press.

Benaroch, M., & Kauffman, R. J. (1999). A case for using real options pricing analysis to evaluate information technology project investments. Information Systems Research, 10(1), 70-86.

Benth, F. E., Klüppelberg, C., Müller, G., & Vos, L. (2014). Futures pricing in electricity markets based on stable CARMA spot models. Energy Economics, 44, 392-406.

Benth, F. E., Saltyte Benth, J., & Koekebakker, S. (2008). Stochastic modelling of electricity and related markets. Singapore: World Scientific.

Biegel, B., Hansen, L. H., Stoustrup, J., Andersen, P., & Harbo, S. (2014). Value of flexible consumption in the electricity markets. Energy, 66, 354-362.

Brijs, T., de Vos, K., de Jonghe, C., & Belmans, R. (2015). Statistical analysis of negative prices in European balancing markets. Renewable Energy, 80, 53-60.

Bundesministerium für Wissenschaft, Forschung und Wirtschaft (BMWFW). (2015). Energiestatus Österreich 2015: Entwicklung bis 2013. Retrieved from http://www.bmwfw.gv.at/EnergieUndBergbau/ Energiebericht/Documents/Energiestatus%20%C3%96sterreich%202015.pdf

Callaway, D. S., & Hiskens, I. A. (2011). Achieving controllability of electric loads. Proceedings of the IEEE, 99(1), 184-199.

Copeland, T. E., & Antikarov, V. (2003). Real options: A practitioner’s guide. New York, NY: Cengage Learning.

Coulon, M., Powell, W. B., & Sircar, R. (2013). A model for hedging load and price risk in the Texas electricity market. Energy Economics, 40, 976-988.

Cox, J. C., Ingersoll, J. E., & Ross, S. A. (1985). A theory of the term structure of interest rates. Econometrica, 53(2), 385-407.

Cox, J. C., Ross, S. A., & Rubinstein, M. (1979). Option pricing: A simplified approach. Journal of Financial Economics, 7(3), 229-263.

Deng, S.-J., & Jiang, W. (2005). Levy process-driven mean-reverting electricity price model: The marginal distribution analysis. Decision Support Systems, 40(3-4), 483-494.

Deng, S.-J., & Oren, S. S. (2003). Incorporating operational characteristics and start-up costs in optionbased valuation of power capacity. Probability in the Engineering and Informational Sciences, 17(2), 155-181.

Dixit, A. K., & Pindyck, R. S. (1995). The options approach to capital investment. Harvard Business Review, 73(3), 105-115.

EPEX SPOT. (2015). 2014 power trading volumes grow by 10.4%. Retrieved from https://www.epexspot.com/document/30189/2015-01-13\_EPEX%20SPOT\_2014\_Annual%20Press %20Release+.pdf

Fama, E. F. (1965). The behavior of stock-market prices. The Journal of Business, 38(1), 34-105.

Fanone, E., Gamba, A., & Prokopczuk, M. (2013). The case of negative day-ahead electricity prices. Energy Economics, 35, 22-34.

Feuerriegel, S., & Neumann, D. (2014). Measuring the financial impact of demand response for electricity retailers. Energy Policy, 65, 359-368.

Fridgen, G., Häfner, L., König, C., & Sachs, T. (2014). Toward real options analysis of IS-enabled flexibility in electricity demand. In Proceedings of the 35th International Conference on Information Systems.

Fridgen, G., Häfner, L., König, C., & Sachs, T. (2015). The value of IS-enabled flexibility in electricity demand—a real options approach. In O. Thomas & F. Teuteberg (Eds.), Proceedings of the 12th International Conference on Wirtschaftsinformatik (pp. 993-1007).

Fridgen, G., Mette, P., & Thimmel, M. (2014). The value of information exchange in electric vehicle charging. In Proceedings of the 35th International Conference on Information Systems.

Frondel, M., Ritter, N., Schmidt, C. M., & Vance, C. (2010). Economic impacts from the promotion of renewable energy technologies: The German experience. Energy Policy, 38(8), 4048-4056.

Goebel, C. (2013). On the business value of ICT-controlled plug-in electric vehicle charging in California. Energy Policy, 53, 1-10.

Goebel, C., Jacobsen, H.-A., Razo, V., Doblander, C., Rivera, J., Ilg, J., Flath, H., Schmeck, C., Weinhardt, D., Pathmaperuma, H.-J., Appelrath, M., Sonnenschein, S., Lehnhoff, O., Kramer, T., Staake, E., Fleisch, D., Neumann, J., Strüker, K., Erek, R., Zarnekow, H. Ziekow, J., & Lässig, J. (2014). Energy Informatics. Business & Information Systems Engineering, 6(1), 25-31.

Gottwalt, S., Ketter, W., Block, C., Collins, J., & Weinhardt, C. (2011). Demand side management—a simulation of household behavior under variable prices. Energy Policy, 39(12), 8163-8174.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337-355.

Hellström, J., Lundgren, J., & Yu, H. (2012). Why do electricity prices jump? Empirical evidence from the Nordic electricity market. Energy Economics, 34(6), 1774-1781.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Hilhorst, C., Ribbers, P., van Heck, E., & Smits, M. (2008). Using Dempster-Shafer theory and real options theory to assess competing strategies for implementing IT infrastructures: A case study. Decision Support Systems, 46(1), 344-355.

Huisman, R., Huurman, C., & Mahieu, R. (2007). Hourly electricity prices in day-ahead markets. Energy Economics, 29(2), 240-248.

Huisman, R., & Mahieu, R. (2003). Regime jumps in electricity prices. Energy Economics, 25(5), 425-434.

International Energy Agency. (2013). World energy outlook 2013. Paris: OECD Publishing.

Kahlen, M. T., & Ketter, W. (2015). Aggregating electric cars to sustainable virtual power plants: The value of flexibility in future electricity markets. In Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence (pp. 665-671).

Kiesel, F. (2015). Bruttostromerzeugung in Deutschland ab 1990 nach Energieträgern. Retrieved from http://www.ag-energiebilanzen.de/index.php?article\_id=29&fileName=20150227\_brd\_stromerzeu gung1990-2014.pdf

Kim, J. H., & Powell, W. B. (2011). An hour-ahead prediction model for heavy-tailed spot prices. Energy Economics, 33(6), 1252-1266.

Li, Z., Yang, F., Mohagheghi, S., Wang, Z., Tournier, J. C., & Wang, Y. (2013). Toward smart distribution management by integrating advanced metering infrastructure. Electric Power Systems Research, 105, 51-56.

Ludig, S., Haller, M., Schmid, E., & Bauer, N. (2011). Fluctuating renewables in a long-term climate change mitigation strategy. Energy, 36(11), 6674-6685.

Martinez-Cesena, E. A., Azzopardi, B., & Mutale, J. (2013). Assessment of domestic photovoltaic systems based on real options theory. Progress in Photovoltaics: Research and Applications, 21(2), 250-262.

Mayer, K., Schmid, T., & Weber, F. (2015). Modeling electricity spot prices: Combining mean reversion, spikes, and stochastic volatility. The European Journal of Finance, 21(4), 292-315.

Merton, R. C. (1997). On the role of the Wiener process in finance theory and practice: The case of replicating portfolios. Proceedings of Symposia in Pure Mathematics, 60, 209-221.

Nicolosi, M., & Fürsch, M. (2009). The impact of an increasing share of RES-E on the conventional power market—the example of Germany. Zeitschrift für Energiewirtschaft, 33(3), 246-254.

Oren, S. S. (2001). Integrating real and financial options in demand-side electricity contracts. Decision Support Systems, 30(3), 279-288.

Palensky, P., & Dietrich, D. (2011). Demand side management: Demand response, intelligent energy systems, and smart loads. IEEE Transactions on Industrial Informatics, 7(3), 381-388.

Rieger, A., Thummert, R., Fridgen, G., Kahlen, M., & Ketter, W. (2016). Estimating the benefits of cooperation in a residential microgrid: A data-driven approach. Applied Energy, 180, 130-141.

Ronn, E. I. (Ed.). (2003). Real options and energy management: using options methodology to enhance capital budgeting decisions. London: Risk Books.

Rostek, S. (2009). Option pricing in fractional Brownian markets. Berlin, Germany: Springer.

Schneider, S. (2012). Power spot price models with negative prices. Journal of Energy Markets, 4(4), 77-102.

Sezgen, O., Goldman, C. A., & Krishnarao, P. (2007). Option value of electricity demand response. Energy, 32(2), 108-119.

Strüker, J., & van Dinther, C. (2012). Demand response in smart grids: Research opportunities for the IS discipline. In Proceedings of the 18th Americas Conference on Information Systems (AMCIS 2012) (Vol. 7).

Trigeorgis, L. (1996). Real options: Managerial flexibility and strategy in resource allocation. Cambridge, MA: MIT Press.

Uhlenbeck, G., & Ornstein, L. (1930). On the theory of the Brownian motion. Physical Review, 36(5), 823-841.

Ullrich, C. (2013). Valuation of IT investments using real options theory. Business & Information Systems Engineering, 5(5), 331-341.

Umutlu, G., Dorsman, A., & Telatar, E. (2011). The electricity market, day-ahead market and futures market. In A. Dorsman, W. Westerman, M. B. Karan, & Ö. Arslan (Eds.), Financial aspects in energy (pp. 109- 128). Berlin, Heidelberg: Springer.

Vasicek, O. (1977). An equilibrium characterization of the term structure. Journal of Financial Economics, 5(2), 177-188.

Vytelingum, P., Voice, T. D., Ramchurn, S. D., Rogers, A., & Jennings, N. R. (2011). Theoretical and practical foundations of large-scale agent-based micro-storage in the smart grid. Journal of Artificial Intelligence Research, 42, 765-813.

Watson, R. T., Boudreau, M.-C., & Chen, A. J. (2010). Information systems and environmentally sustainable development: Energy informatics and new directions for the IS community. MIS Quarterly, 34(1), 23-38.

Weron, R., Bierbrauer, M., & Trück, S. (2004). Modeling electricity prices: jump diffusion and regime switching. Physica A: Statistical Mechanics and its Applications, 336(1-2), 39-48.

Weron, R. (2009). Heavy-tails and regime-switching in electricity prices. Mathematical Methods of Operations Research, 69(3), 457-473.

Wilson, R. (2002). Architecture of power markets. Econometrica, 70(4), 1299-1340.

Würzburg, K., Labandeira, X., & Linares, P. (2013). Renewable generation and electricity prices: Taking stock and new evidence for Germany and Austria. Energy Economics, 40, S159-S171.

## About the Authors

Gilbert Fridgen is Professor of Information Systems and Sustainable IT Management at the University of Bayreuth, Deputy Director of the Project Group Business and Information Systems Engineering of the Fraunhofer Institute for Applied Information Technology (FIT), and Deputy Director of the Research Center Finance & Information Management. His research in Energy Informatics aims at advancing the transition towards sustainably energy systems. He especially addresses Demand Side Management, i.e. the dynamic adaption of electricity demand to the increasingly volatile energy production, spanning the boundaries between Management, Information Systems, and Engineering. His research is published in major outlets of all of the three disciplines. He was granted substantial research funds from European, German and State programs. The most important ones are SynErgie, a platform for the aggregation of industrial energy demand flexibility funded by the German Federal Ministry of Education and Research and ITPM2, a project on the value based management of IT projects funded by the German Research Foundation (DFG). He furthermore acquired funds for applied research projects in collaboration with major international enterprises.

Lukas Häfner is a doctoral candidate in the Project Group Business and Information Systems Engineering of the Fraunhofer Institute for Applied Information Technology (FIT) and at the Research Center Finance & Information Management. He studied Business Engineering at the Karlsruhe Institute of Technology (KIT) specializing in Finance, Game Theory and Operations Research. He gained practical experiences in several internships during his studies, and later in applied as well as public funded research projects in collaboration with major international enterprises. His research focuses on Decision Support Systems in Energy Informatics and Corporate Risk Management with the objective to empower operational as well as strategic decision makers with IS Technology.

Christian König, at the time of writing this paper, was a research assistant and postdoctoral fellow in the Project Group Business and Information Systems Engineering of the Fraunhofer Institute for Applied Information Technology (FIT) and at the Research Center Finance & Information Management. He studied information-oriented Business Administration at the University of Augsburg specializing in Finance & Information. He gained practical experiences in several internships during his studies, and later in applied research projects in collaboration with major international enterprises. His research focuses on IT Outsourcing, IT Risk Management, and Energy Informatics. In 2015, he finished his doctoral thesis in Business and Information Systems Engineering.

Thomas Sachs is a doctoral candidate at the Professorship of Information Systems and Sustainable IT Management at the University of Bayreuth, in the Project Group Business and Information Systems Engineering of the Fraunhofer Institute for Applied Information Technology (FIT), and at the Research Center Finance & Information Management. He studied Business Administration at the University of Bayreuth and EDHEC Business School specializing in Business Information Systems, Accounting, and Finance. He gained hands-on experience at KPMG IT Advisory, PwC Risk Assurance Solutions, and Deutsche Bank Group Technology, among others. Recently, he has also worked on applied research projects in collaboration with major international enterprises in manufacturing, transportation and consulting. His research focuses on Energy Informatics and Cloud Computing.

Copyright © 2016 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via e-mail from publications@aisnet.org.
