---
otero_id: 28355
otero_key: "WWVWA7FE"
title: "Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles"
authors: "Micha Kahlen; Karsten Schroer; Wolfgang Ketter; Alok Gupta"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0204"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

Micha Kahlen,<sup>a</sup> Karsten Schroer,<sup>b</sup> Wolfgang Ketter,<sup>a,b</sup> Alok Gupta<sup>c,</sup>\*

<sup>a</sup> Rotterdam School of Management, Erasmus University, 3062 Rotterdam, Netherlands; <sup>b</sup> Faculty of Management, Economics and Social Sciences, University of Cologne, 50931 Cologne, Germany; <sup>c</sup> Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455 \*Corresponding author

Contact: micha.kahlen@gmail.com, https://orcid.org/0009-0005-8302-6402 (MK); karsten.schroer@icloud.com, https://orcid.org/0000-0002-5443-1696 (KS); ketter@wiso.uni-koeln.de, https://orcid.org/0000-0001-9008-142X (WK); alok@umn.edu, https://orcid.org/0000-0002-2097-1643 (AG)

Received: March 23, 2022 Revised: December 15, 2022; April 3, 2023 Accepted: May 16, 2023 Published Online in Articles in Advance: July 10, 2023

https://doi.org/10.1287/isre.2022.0204

Copyright: © 2023 The Author(s)

Abstract. Motivated by the deep transformation of the transportation sector toward electric and shared mobility, this research develops a decision support system that enables real-time allocation of shared electric vehicles (SEVs) to either the rental market or aggregated as a virtual power plant to the electricity market. The multipurposing of SEVs beyond the traditional scope of mobility services can boost utilization and profitability for fleet operators while also facilitating the integration of variable rate renewable energy sources. This SEV setting embodies the problem of real-time multiproduct resource allocation via smart markets. We develop an approach that leverages highly digitalized real-time markets and intelligent decision making to enable dynamic multiproduct resource allocation. The tool continuously evaluates market attractiveness and strategically places iterative bids on the resource owner’s behalf until all resources have been committed for a specific period. Our key contributions are to provide a blueprint for similar multiproduct resource allocation settings and show its efficacy in the domain of SEV fleets by developing tailored analytics and machine learning-based solutions.

History: Paul A. Pavlou, Senior Editor; Martin Bichler, Associate Editor.

Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as “Information Systems Research. Copyright © 2023 The Author(s). https://doi.org/10.1287/isre.2022.0204, used under a Creative Commons Attribution License: https://creativecommons.org/licenses/by/4.0/.” Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.0204.

Keywords: smart markets • electric vehicles • virtual power plants • real-time decision making

## 1. Introduction

Our research is motivated by the ongoing technological transformation of transportation systems around the globe (Sperling 2018). Leading experts agree that the transportation system of the future will likely evolve around diverse types of vehicle platforms that are connected, autonomous, shared, and electric (Burns 2013, Mahmassani 2016, Ketter et al. 2022). Innovations in these four areas promise to provide answers to some of the key externalities of transportation, which include the contribution to climate change, the production of hazardous pollution (World Health Organization 2005), traffic accidents (World Health Organization 2018), and other inherent inefficiencies such as congestion (Cramton et al. 2018).

We focus on shared electric vehicles (SEVs) that are operated by a central fleet operator. They have become commonplace in many urban areas around the world and include electric car fleets (e.g., Car2Go or DriveNow), electric bicycle fleets (e.g., lime), or fleets of electric scooters (e.g., bird). “Shared” implies the consumption of mobilityas-a-service (MaaS) and mobility-on-demand (MoD)

(Bardhi and Eckhardt 2012, Sperling 2015). It has become a popular business model in recent years (Firnkorn and Mu¨ ller 2015). Operating fleets of SEVs offers novel challenges such as service area sizing, repositioning strategies or reservation management (He et al. 2019) but also opportunities to access new value pools. The opportunities are mainly related to the “electric” nature of SEVs. Electrification of transport implies convergence with the electricity sector. In this context, SEVs and their batteries constitute distributed energy resources that can actively participate in modern real-time and highly automated energy markets.

Although traditionally focused on providing mobility services only, such SEV fleets can now access new value pools by operating on the electricity market during times of low mobility demand. This can further boost utilization and profitability as it enables fleet operators to extract value from vehicles even during times and in locations where they would otherwise sit idle. This mul tipurposing of a previously single-product resource is enabled through the digital nature of electricity markets and modern mobility in general. Digitalization allows for automated and real-time evaluation of resource allocation opportunities by determining which purpose offers more value. Yet, implementing resource multipurposing strategies is not trivial. Fleet operators are faced with two main decision problems per each period:

1. How many SEVs to assign to the rental vs. the electricity market?

2. At what price to offer the SEVs in each market?

Both the rental market and the electricity market have close to real-time delivery periods. Therefore, any resource allocation decisions must be made quickly and at a high frequency. Such decision making involves the continuous evaluation of the tradeoffs between the two markets. Making these decisions requires deep knowledge of future market conditions such as demand and price, both per-period and per-market, and as resource availability and production costs for the period in scope. Further complexity arises as operators need to dynamically operationalize the allocation decisions depending on feedback from the markets such as cleared bids/asks and own resource availability at that point.

We argue that, in the case of SEV fleets managing realtime resource allocation challenges, state-of-the-art decision support system (DSS) that automate much of these continuous modeling and evaluation tasks (Bichler et al. 2010) are required. Such tools manage many of the aforementioned complexities and therefore enable multipurposing of resources. Given the paucity of research and methodologies in this domain, in this research, we develop FleetPower: a novel DSS for real-time multiproduct resource allocation.

On a general level, our DSS draws on and consolidates core aspects from three bodies of literature. These are (1) multiproduct resources, (2) market-based resource allocation, and (3) smart markets. Multiproduct resources are assets that can produce multiple products or provide a set of distinct services. Determining how to allocate such resources is known as “the multiproduct singlemachine problem” in operations research literature (Doll and Whybark 1973). Market-based resource allocation approaches use prices as coordination signals, with resources being awarded to agents who pay/ask the highest/lowest price depending on the objective (Shneidman et al. 2005). Smart, electronic markets (Bichler et al. 2010) and digital platforms (De Reuver et al. 2018) have emerged as dynamic and efficient ways to enable marketbased synchronization of demand and supply.

The digital nature of smart markets also allows for direct interaction of software agents and markets, thus creating the opportunity for agent-enabled exchange (Ketter et al. 2012, Peters et al. 2018). Smart markets enable the automation of real-time market-based resource allocation by using information systems (IS) such as bidding agents or other DSS (Adomavicius et al. 2009).

Using the concept of smart markets for multiproduct resource allocation is a novel perspective. Typically, smart market research has focused on how computerized markets can be designed to synchronize demand and supply within a sector (Bapna et al. 2008, Lu et al. 2019) and how DSS can assist market participants to achieve desired outcomes in these markets (Wooldridge and Jennings 1995, Adomavicius et al. 2009). Instead, using the context of SEV fleets, we show and evaluate how smart markets can be used to allocate multiproduct resources across markets operating with potentially asymmetric payoffs and diverse mechanisms. We make the case that smart markets enhance resource efficiency and utilization of multiproduct resources by providing a digital interface that, in combination with state-of the-art data-driven DSS, enable resource operators to allocate their resources to markets where they are valued the most.

Overall, we make the following core contributions:

• We propose a DSS for real-time multiproduct resource allocation across multiple smart markets in parallel. We thus contribute an artefact (Hevner et al. 2004) that allows for real-time resource allocation of existing multiproduct resources and/or the “multipurposing” of traditionally single-product resources.

• We apply this DSS to SEV fleets. Using state-ofthe-art machine learning and data analytics for demand prediction and pricing we demonstrate how our DSS can enable fleet operators to dynamically choose whether to keep a vehicle available for rental or to use its battery for electricity grid balancing services. We evaluate this tool by means of a rich simulation based on a unique combined data set of rental data and electricity balancing price data from three markets in Europe and the United States. We show utilization and profit gains enabled by real-time multipurposing of a previously single-product resource. As such our work addresses calls for increased involvement of the IS discipline in shaping a smart sustainable mobility future (Ketter et al. 2022).

• We discuss the general applicability of our findings and provide concrete examples of other application areas.

Our research follows the suggested framework of design science research by Hevner et al. (2004) or Rai (2017) in that we present and thoroughly evaluate an IS artifact for the increasingly relevant multiproduct resource allocation challenge.

The remainder of this research is structured as follows: In Section 2, we provide a concise review of the literature focusing on the areas of multiproduct resource allocation and market-based coordination and automated, agentenabled exchanges. Next, we elaborate on the context of the empirical study and the data (Section 3). Then, we introduce our DSS (Section 4) and evaluate this system on SEV fleets that can either offer rental or electricity services (Section 5). We end by discussing relevant impli cations and conclusions that can be drawn from the presented research (Section 6).

## 2. Background and Related Literature

We review three core streams of research on which our work is based. As we consider SEV fleets to be multiproduct resources, we review the relevant literature in this area. We also review the literature on market-based resource allocation. Finally, given the real-time and digital nature of the markets in scope, we review the smart market literature. In doing so, we outline the foundations for our DSS.

## 2.1. Multiproduct Resources

Multiproduct resources can be used to produce a range of different products and/or deliver a range of different services. They are characterized by the fact that only one type of product can be produced at a given time.

The research on multiproduct resource allocation is deeply entrenched in the operations management and operations research communities and focuses mostly on mathematical programming approaches to derive optimal solutions for production and inventory planning problems of multiproduct resources. Relevant studies have focused on the multiproduct news vendor problem, a variation of the textbook news vendor optimization problem. Niederhoff (2007) revisit the problem for independent demand distribution of products. Abdel-Aal et al. (2017) extend this work by considering the multiproduct, multimarket news vendor case, for which they propose a mathematical optimization model.

These models take key exogenous factors, such as market demand either as a deterministic input (Doll and Whybark 1973, Delporte and Thomas 1977), or assume a stochastic distribution (Niederhoff 2007, Abdel-Aal et al. 2017) as input for mathematical programming models. Based on these inputs, they then develop central optimization approaches to cost-optimize production of the required products/services on their machine or facility or to provision the required inventory most cost effectively. In our research, we develop a much more dynamic and flexible approach. We model anticipated future market conditions instead of assuming deterministic inputs or stochastic distributions. We also do not only focus on quantity but also consider price which is a key consideration in allocating resources to markets. We focus primarily on the question of where it is most profitable to commit our resources, a potentially much larger profitability lever than just reducing cost in internal operations. To do so, we directly engage with markets on a real-time basis that allows us to allocate resources much more flexibly, and when possible, even in real time. Practically, we consider the product markets themselves as resource allocation mechanisms. We take advantage of this consideration by placing products dynamically, when and where they are most valued. Markets can indeed be very effective resource allocation mechanisms. We will review why markets are a good candidate and should be taken advantage of when allo cating scarce resources in the following section.

## 2.2. Market-Based Resource Allocation

Efficient resource allocation deals with the allocation of available resources (or tasks) to agents and is a widely known problem across many disciplines, ranging from economics to operations management, control theory, and computer science (Malone and Crowston 1994). In most cases, an allocation of a resource can be considered most efficient when the resource or task is awarded to the agent who desires it most. On a general level, two approaches to resource allocation can be distinguished (Chevaleyre et al. 2006, Hazard et al. 2006): (1) central ized and (2) decentralized.

As our research takes place in auctions, we focus on decentralized auction mechanism literature.

Auctions are negotiation mechanisms that elicit information from participants and facilitate dynamic assignment of items and payments to participants based on submitted information (Stro¨bel 2000, Anandalingam et al. 2005). Recently, with the advent of digital platforms and electronic markets, market-based approaches (especially auction formats, i.e., online auctions (Bapna et al. 2003)) have gained traction as the resource allocation mechanism of choice in many environments (Shneidman et al. 2005). Market based approaches include production scheduling and supply chain management (Fan et al. 2003), the allocation of road space (Cramton et al. 2018), the allocation of online advertising inventory, the dispatch of electrical power in electricity grids (Cramton 2017), and distributed task allocation in wireless senso networks (Edalat et al. 2012), to name a few.

## 2.3. Smart Markets

Digital market- and auction-based resource allocation mechanisms are computerized exchanges that facilitate automated resource and payment allocation. In IS research, these computerized resource allocation mechanisms have come to be known as electronic markets (Malone et al. 1987, Anandalingam et al. 2005), smart markets (Bichler et al. 2010), or automated exchanges (Ketter et al. 2009).

The respective body of research has extended to two main and interlinking fields. These are (1) the design and analysis of smart market mechanisms (Stro¨bel 2000; Bapna et al. 2004, 2008; Bichler et al. 2010; Lu et al. 2016, 2019) and (2) the design of DSS and intelligent software agents for market participants (Wooldridge and Jennings 1995, Adomavicius et al. 2009, Ketter et al. 2012).

The research on mechanism design and their analysis has focused mostly on cases in which a resource is auctioned via a single auction mechanism. Bapna et al. (2009) also consider the concept of overlapping auctions in which identical items can be sold in different, temporally overlapping auctions with different market mechanisms.

To the best of our knowledge the concept of allotting different types of items/services via a number of smart markets that operate varying mechanisms has not been studied. We address this gap in the presented research.

The second research stream is related to the design of DSS that enable successful interaction with smart markets.

Such agents learn individual preferences and act on them in a strategic way, continuously processing and evaluating information and translating it into actions (Peters et al. 2018).

The large majority of IS studies on bidding agents takes a buyer-centric view and investigates how agents can be devised that support the real-time bidding process in single- or double-sided exchanges (Adomavicius et al. 2009, Peters et al. 2018).

Limited research has been carried out on agents for sellers in general and in particular for such cases in which a seller or resource owner can produce multiple products/services from a single resource. Such cases are complex due to the temporal and format heterogeneity of exchanges that can be targeted by the seller. Yet, with the expansion of multisided automated exchanges such as online auctions and multisided platforms (Hagiu and Wright 2015), these cases have become highly relevant. This research addresses this gap. We look at smart markets from a resource owner point of view and particularly consider their potential in allocating resources efficiently across a variety of different product markets. The novelty of our work lies in our explicit focus on the seller perspective in the complex situation of a multiproduct, multimechanism scenario. In doing so, we also bridge the gap between the research on smart markets and agents on the one side and the previously reviewed stream of multiproduct resource allocation on the other side.

## 3. Real-Time Multiproduct Resource Allocation via Smart Markets

We now draw on the previous literature to develop a novel DSS for enabling multiproduct resource allocation for SEV fleets as both mobility resources and virtual power plant (VPP). Rudimentary trial implementations using private electric vehicles (EVs) in electricity balancing markets have already been successfully implemented (Next Kraftwerke 2018). Our case is therefore realistic and technically feasible. However, the management of such multipurposed resources is highly complex. The complexity arises from the diversity of both mechanisms and products. In terms of mechanism diversity, the relevant markets operate based on different bidding and payment rules. For example, bidding horizons for the individual service markets are heterogeneous. Balancing power must be committed one week prior to delivery while the rental market has instantaneous bidding and delivery. In the rental market, a fixed take-it-or-leave-it tariff policy is applied, whereas in the electricity market, resource allocation is facilitated via electronic auctions and pay-as-bid payments. In terms of product diversity, we consider the case of an SEV fleet offering two distinct services, personal mobility and electricity balancing, although more are theoretically possible (e.g., goods delivery services). The two services are distinct. First, resource value is location and time dependent in one market (i.e., the rental market) and purely time depen dent in the other market (i.e., the electricity market). Additionally, there is a large asymmetry in payoffs between the markets: A clear lead product exists, which incurs large opportunity costs in case of wrong allocation decisions that may arise from inaccurate forecasts of own resource availability. Finally, the perishable nature of the goods being sold adds complexity and incurs major penalties in case of nonfulfillment of commitments, requiring real-time decision making.

In the following sections, we present the necessary market design knowledge and data underlying our DSS for SEV fleets. We start by elaborating on the setting of carsharing and electricity balancing markets. We then introduce our data and present descriptive statistics.

## 3.1. Multiproduct Resource: SEV Fleets for Personal Mobility and Electricity Services

Carsharing is an increasingly popular business model (Firnkorn and Mu¨ ller 2011). Under a carsharing scheme, cars are rented for short durations as a mobility service. Unlike traditional car rental services, where customers keep possession of the car even during long unused hours, the idea of carsharing is to rent the cars for short one-way trips. Free-floating carsharing, a special type of carsharing, is a system under which users can pick up and drop off the vehicle anywhere within a specified ser vice area. Many operators of free-floating fleets employ SEVs. Clearly, while the cars are parked, carsharing companies incur investment and maintenance costs. This loss is unavoidable for traditional fossil fuel–based cars. SEVs can generate additional revenues by multipurposing as a VPP to partly offset these costs. VPPs, when used to provide balancing services to the grid, offer an alternative source of power when other power sources produce more or less electricity than had been committed, fo example, due to technical defects or weather-related issues, or if demand is higher or lower than anticipated.

When there is more supply of electricity than demand, downregulation is required to remove electricity that would otherwise destabilize the grid. When there is more demand than supply, upregulation is required to meet the incremental demand. The fact that EV batteries can be charged and discharged flexibly, without long ramp-up periods, makes them very suitable for balancing services.

Downregulation, or smart charging in the context of SEVs, means that SEV operators are given financial incentives to delay their charging times to hours of low demand for electricity to reduce electricity consumption during supply shortages (Valogianni et al. 2014).

Upregulation, or vehicle-to-grid (V2G), means that a vehicle supplies energy from its battery to the grid and turns into an energy producer for the duration of the discharge. SEV operators are paid a price premium when using V2G to feed electricity from the SEV’s battery back into the grid during hours of excess electricity demand. Charging stations and vehicles need to be able to convert power in both directions to support V2G; it is covered in the standard of the International Electrotechnical Commission for charging stations (IEC 62196). The advantage of V2G is that energy can be provided on demand when consumers need it and in a decentralized manner, which requires less electrical grid infrastructure. The disadvantages are that V2G affects vehicle battery life and that V2G capable charging stations are more expensive. For the purpose of this study, we assume that all charging stations have V2G. However, as we will find in this study, V2G is usually not commercially viable under current electricity market setup. It seems likely that V2G will mostly be used by private households to increase independence from the grid, primarily in areas where brown- and black-outs occur frequently, unless market setup changes. A recent study by Schill (2011), for example, considers an EV owner with an EV battery exposed to dynamic pricing on the German energy wholesale market and finds that yearly benefits per EV of \$176–\$203 are possible.

Previous research also investigated the use of EVs as VPPs for balancing services (Schill 2011, Vytelingum et al. 2011) when EVs are not in use and assumes perfect foresight of use patterns. Therefore, rental services and the balancing services are never considered in combination but in mutually exclusive, predefined time periods only. The assumption that rental transactions are perfectly known in advance contradicts the MoD concept. Our real-time multiproduct resource allocation framework creates a natural link between these two services by recognizing that the batteries of EVs are a single resource that needs to be allocated at any given point in time to one of these two distinct service sectors and that the two sectors are now in unprecedented competition with each other.

It must be stressed that charging station infrastructure availability is a precondition for up- or downregulation. As the number of charging stations increases, EVs are more likely to be connected to the grid and to be used as part of a VPP. Mak et al. (2013) and Avci et al. (2015) put forward an optimal spatial infrastructure design for battery-swapping stations that might be relevant to SEV fleet owners. However, we focus on conventional charging stations instead, which seem to be the prominent technology in the cities we study.

## 3.2. Markets: Electronic Rental and Electricity Balancing Markets

The offering of MaaS and MoD in a free-float carsharing setting is enabled by mobile apps, mobile purchases, and connected vehicles (Burns 2013). Building on these trends, carsharing providers have set up electronic rental markets in which customers can rent a vehicle based on a fixed take-it-or-leave-it tariff policy. All available vehicles are offered to customers via a mobile app interface along with key status information such as state of charge, loca tion, cabin cleanliness, and other factors. Customers can freely pick a suitable vehicle that best meets their mobility goals. These markets have an instantaneous bidding and delivery setup with limited reservation capability, consistent with the MoD concept. Usually, reserving a vehicle more than 1=4 hour in advance is not possible. In addition to a sign-up fee, members pay for the carsharing service on a use-basis only.

Electricity is either sold in long term markets or in day-ahead and intraday markets as delivery commitments hours or days before the electricity is generated. However, when a generator cannot meet its commitment or demand is unexpectedly high, there are control reserve markets to guarantee immediate replacement (known in the United States as the real-time market and in the European Union as the secondary control reserve market). These reserve markets require extremely fast reaction times (called “ramp rates”) from participating generators. SEVs possess large electrical batteries with available energy that is almost instantly accessible with hardly any ramp cost, making them very suitable for reserve purposes. For our case, we focus on the second ary control reserve market with a required ramp rate of 30 seconds (International Grid Control Cooperation 2014). We focus on this market because its energy prices are higher than in markets with longer ramp rates. Sec ondary reserve markets trade the residual electricity need that could not be predicted in the long-term, day ahead, and intraday markets. This residual demand needs to be met at virtually all costs to avoid black outs and hence the higher prices.

Control reserve markets are coordinated by electronic auctions in which participants place bids for up- or downregulation one week prior to fulfillment. The clearing mechanism is a multiunit, first-price, sealed-bid auction, which is settled on a “pay-as-bid” basis (International Grid Control Cooperation 2014). This mechanism allows sellers to efficiently offer electricity to the market participants that pay most for the electricity. The grid operator purchases the electricity and bills it to electricity producers that have a deficit or a surplus of electricity. Those producers are typically energy companies but could in rare instances also be other SEV fleets that cannot deliver due to incorrect forecasts.

In our work, we assume that bids can be placed separately for each $\Delta t = 1 / 4$ hour time period. This future state is desired by grid operators to reduce entry barriers of renewable energy sources (Agricola 2014). Some markets differentiate between a capacity price to participate in the auction and an energy price for electricity. In this work, our assumption regarding market design is that all markets operate on the basis of an energy price only.

Although the market design requires bids to be submitted one week in advance for planning purposes, the grid operator calls committed quantities as required 30 seconds before delivery. Afterward, the grid operator reimburses power producers/consumers based on the previously cleared pay-as-bid price. As an example, a visual representation of the clearing mechanisms for up regulation is presented in Figure 4.

The forecasting horizon of one week for vehicle availability is a result of the secondary reserve market design as described previously.

## 3.3. Carsharing Data

We chose Car2Go data for our case study because it is a carsharing fleet with a global presence that uses the same vehicles (Smart ForTwo) across locations, thus allowing for a good comparison between countries. The selected markets (Stuttgart, Amsterdam, and San Diego) are particularly suited for the purpose of this research because they are heterogeneous in terms of their energy mix. California and Germany are both at the forefront of renewable energy production, whereas the Netherlands rely on electricity supply based largely on fossil fuels.

We tracked the location, state of charge, and transactions of I � 491 SEVs in Stuttgart, I � 343 in Amsterdam, and I � 367 in San Diego for 14 months. These cities had 232, 1,500, and 64 charging stations, respectively, during the period of study. The high number of charging stations in Amsterdam is related to government incentives. The rental prices across locations are similar but not identical, so we use the arithmetic mean of the prices for ease of comparison between locations.

The rental data were retrieved via a private application programming interface (API; which we were given access to by Daimler, the parent company of Car2Go). We retrieved a list of all EVs that were available for rental at the time of the query from the Car2Go website:

www.car2go.com. We downloaded the data, added a time stamp, and stored it in a database every 15 minutes from May 1, 2014, to June 29, 2015. This information contains the unique car name, the geographic coordinates of the vehicle’s parking position, the street name and zip code of that location (l), the state of charge of the battery (SoC), the state of the interior and exterior, and whethe the EV is currently charging. We infer certain information about the transaction, such as how long the EV was rented, how many kilometers were driven, and the profits $( \pi _ { m o b i l i t y } )$ by looking at the duration and timing of EV unavailability and the difference in the SoC level before and after the inferred rental. Although the number of kilometers that can be covered using average fuel consumption will depend on individual driving behavior and local conditions (therefore potentially affecting the accuracy of our estimates), we are confident that the differences will in fact be marginal, because all the journeys take place in an urban environment. We assume that a fully charged EV has a range of of 65 miles (105km) according to the EV Database.<sup>1</sup> Table 1 provides an extract of the raw data and the information that we infe from it.

A drawback of the data collection method is that there is a chance that a car may be returned and rented again to another customer within the $\Delta t = 1 / 4$ hour time period. However, for the sake of our analysis, the EV remains unavailable, so this does not have a significant influence on the overall estimation and results. We also observe that on several occasions particular EVs did not feature in the data for more than two days, although the maximum rental duration is two days. We speculate that these cars were either in maintenance, repair, or not in operation for some other reason. We therefore remove all rentals exceeding two days from the data set. For a graphical illustration of how the rentals are distributed across a city, see Figure 1, which indicates the spatial dimensionality of the rental market, where the value of the resource is location dependent.

We infer the location of charging stations based on the GPS coordinates of where cars were charged at least once during the period of study. We assume that if a car is parked at a charging station, it will be connected to the charging station. This is a sound assumption, because in many locations it is illegal for cars to park at a charging station when not plugged in.

Table 1. Raw Data Excerpt

<table><tr><td>Car ID i</td><td>Time t</td><td>State of charge (SoC/SoCmax)</td><td>Latitude</td><td>Longitude</td><td>Interior</td></tr><tr><td>Car#1</td><td>12.05.2014 17:00</td><td>71%</td><td>32.76393</td><td>-117.122</td><td>Good</td></tr><tr><td>Car#1</td><td>12.05.2014 17:15</td><td>71%</td><td>32.76393</td><td>-117.122</td><td>Good</td></tr><tr><td>Car#1</td><td>12.05.2014 18:00</td><td>60%</td><td>32.76556</td><td>-117.168</td><td>Good</td></tr><tr><td>Exterior</td><td>Street</td><td>Zip code l</td><td>City</td><td>Charging</td><td>Engine</td></tr><tr><td>Good</td><td>Felton St 4728</td><td>92116</td><td>San Diego</td><td>False</td><td>Electric</td></tr><tr><td>Good</td><td>Felton St 4728</td><td>92116</td><td>San Diego</td><td>False</td><td>Electric</td></tr><tr><td>Unacceptable</td><td>Fashion Valley Rd 1261</td><td>92108</td><td>San Diego</td><td>False</td><td>Electric</td></tr></table>

Note. From this extract, we infer that a customer drove 7 miles (12 km), rented the EV for 45 minutes, and paid \$14.99 (tariff for a full hour)

Figure 1. (Color online) Rental Frequency in Amsterdam  
![](/api/attachments/WWVWA7FE/fulltext/images/13747c80ea68b02795e877e74cb2c41788bc82e9b5677134723d605895412543.jpg)  
Note. The city center (middle), and business districts Zuidas (south west) and Amstel (south east) have particularly high densities of rental transactions.

## 3.4. Balancing Market Data

We use the secondary operating reserve/real-time market data from the energy market operators in Stuttgart,

Amsterdam, and San Diego for the same time horizon as for the Car2Go rental data. In Stuttgart, we use data from regelleistung.net, the German energy market operator; in Amsterdam, we use data from Tennet; and in San Diego, the data are retrieved from the California Independent System Operator. The data for Stuttgart contains the individual bids for up- and downregulation with the respective quantities and prices for each $\Delta t = 1 / 4$ hour time period. We form the demand and supply curves from these bids. For San Diego and Amsterdam, we only know the clearing prices, although this still allows us to infer that the bids and asks below the market price are accepted.

The prices for up- and down-regulation reserves $P _ { u p \_ r e g , t } ^ { * }$ and $P _ { d o w n \_ r e g , t } ^ { * }$ are quite variable (standard deviation ranging from $\overset { \cdot } { \sigma } = 0 . 0 2 \Phi / \mathrm { k W h }$ to σ � 0:09\$=kWh).

## 4. Decision Support System for Shared EV Fleets: FleetPower

We now present our conceptual multipurposing approach and evaluate it on the Car2Go fleets described previously. What results is a DSS that manages the multiproduct SEV fleet on the resource owner’s behalf. We name it FleetPower. It broadly covers the three core agent tasks as defined in Bichler et al. (2010) and consists of five consecutive phases (Figure 2). FleetPower considers and actively manages three distinct types of services that can be delivered by the individual SEV. These are as follows:

1. Mobility services

2. Electricity balancing services (upregulation)

3. Electricity balancing services (downregulation)

Figure 2. Framework for Real-Time Multiproduct Resource Allocation via Smart Markets  
![](/api/attachments/WWVWA7FE/fulltext/images/3b6f27bdb80abaa55840ac1c03dcce26ea06648e0e64dddadad8edff9a0a6dc5.jpg)  
Notes. Starting with the modelling of market demand and price levels and internal resource availability and cost, resources are planned and placed on the respective product markets p, with p ∈ {mobility, up\_reg, down\_reg}. Once quantities have cleared and actual vehicle availability is realized at the start of period t, a replanning is conducted and the final resource allocation is executed.

Table 2. Table of Notation

<table><tr><td>Variable</td><td>Description</td><td>Unit</td></tr><tr><td> $c_{p,t}$ </td><td>Actual unit cost for product p during time period t</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td> $\widehat{c}_{p,t}$ </td><td>Expected unit cost for product p during time period t</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td>d</td><td>Unit cost for battery depreciation</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td> $e_{charge}$ </td><td>Efficiency rate during charging</td><td> $\frac{\%}{100}$ </td></tr><tr><td> $e_{discharge}$ </td><td>Efficiency rate during discharging</td><td> $\frac{\%}{100}$ </td></tr><tr><td> $F_{p}$ </td><td>Fine / penalty for not serving the full committed quantity of product p</td><td>$</td></tr><tr><td>g</td><td>Avg. fleet exterior status feature set,  $g_{1}$ </td><td>percentage</td></tr><tr><td>h</td><td>Hour of the day feature set,  $h_{0},..,h_{23}$ </td><td>binary</td></tr><tr><td>i</td><td>Specific vehicle, i ∈ I and/or i ∈ J</td><td>index</td></tr><tr><td>I</td><td>Set of SEVs available in the fleet</td><td>set</td></tr><tr><td>J</td><td>Set of SEVs connected to a charging station at the start of t</td><td>set</td></tr><tr><td>o</td><td>Avg. fleet interior status feature set,  $o_{1}$ </td><td>percentage</td></tr><tr><td>p</td><td>Specific product or service, p ∈ S</td><td>index</td></tr><tr><td> $P_{p,t}^{*}$ </td><td>Actual clearing price for product p during time period t</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td> $\widehat{P}_{p,t}^{*}$ </td><td>Expected clearing price for product p during time period t</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td> $\overline{P}_{p}^{*}$ </td><td>Average energy price paid during the training period</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td> $Q_{p,t}^{*}$ </td><td>Actual demand for product p during time period t</td><td>kWh</td></tr><tr><td> $\widehat{Q}_{p,t}$ </td><td>Expected demand for product p during time period t</td><td>kWh</td></tr><tr><td> $Q_{p,t}$ </td><td>Actual availability of product p during time period t</td><td>kWh</td></tr><tr><td> $Q_{p,t}^{A}$ </td><td>Actual availability of product allocation p during time period t before Re-Planning</td><td>kWh</td></tr><tr><td> $\widehat{Q}_{p,t}^{A}$ </td><td>Expected availability of product p during time period t</td><td>kWh</td></tr><tr><td> $Q_{p,t}^{bid}$ </td><td>Bid quantity for product p during time period t</td><td>kWh</td></tr><tr><td>S</td><td>Set of all products or services, p = 1,..,S</td><td>set</td></tr><tr><td> $SoC_{i,t}$ </td><td>State of Charge of SEV i at the beginning of time period t</td><td>kWh</td></tr><tr><td> $SoC_{max,i}$ </td><td>Maximum capacity of SEV i</td><td>kWh</td></tr><tr><td>t</td><td>Time period t ∈ T</td><td>Index</td></tr><tr><td>T</td><td>Set of time periods</td><td>Set</td></tr><tr><td>w</td><td>Day of the week feature set, w0,..,w6</td><td>Binary</td></tr><tr><td>Δt</td><td>Duration of a time period t</td><td>Hours</td></tr><tr><td>δ</td><td>Discharging speed of charging stations</td><td>Kilowatts</td></tr><tr><td>γ</td><td>Charging speed of charging stations</td><td>Kilowatts</td></tr><tr><td> $\overline{\epsilon}$ </td><td>Average number of vehicles connected to a charging station</td><td>Integer</td></tr><tr><td> $\pi_{p,t}$ </td><td>Actual unit profit for product p during time period t</td><td> $\frac{\$}{kWh}$ </td></tr><tr><td> $\widehat{\pi}_{p,t}$ </td><td>Expected unit profit for product p during time period t</td><td> $\frac{\$}{kWh}$ </td></tr></table>

We describe the five phases of our framework for Car2Go in more detail in the following sections. For a table of notation, including measurement units, see Table 2.

## 4.1. Phase 1: Market and Operational Data Gathering

First, the DSS gathers information about the rental and balancing markets for the products $p \in S ,$ , where $S =$ {mobility, up\_reg, down $_ { - } r e g \}$ . The quantity Q for all products is measured in kilowatt-hours (kWh). This allows for a clean comparison between the electricity that is used for driving and the electricity that is sold on the energy markets. We determine the expected demand $\widehat { Q } _ { p , t } ^ { \dagger }$ and the expected price $\widehat { \boldsymbol { P } } _ { p , t } ^ { * }$ on each market. Then, we determine the expected product availability $\widehat { Q } _ { p , t } ^ { A }$ and the expected cost to serve each market $\widehat { c } _ { p , t }$ . As aforementioned, one peculiarity of the rental market $( p = m o b i l i t y )$ is that demand, cost, and profitability is dependent on the location l. We therefore include a locational dimension for all variables related to the mobility sector. l is defined as a zip code. In the Netherlands, complete zip codes are street level granular. To keep the zip codes roughly consistent in size to the United States and Germany, we only consider the numerical part of Dutch zip codes and leave out the letters; for example, if the Dutch zip code is 1234 AB, we would use only the 1234.

Drawing on Schroer et al. (2022), we apply various machine learning algorithms, including linear regression, support vector machine (SVM) regression, bagged tree-based regression, and random forest regression, to forecast the expected rental demand at a specific time and location $\widehat { Q } _ { m o b i l i t y , l , t } ^ { * }$ . We do not consider time series models, because commitments are due one week in advance in the reserve market. The expected mobility demand $\widehat { Q } _ { m o b i l i t y , l , t } ^ { * }$ is determined as a function of four distinct feature sets:

$$
\widehat {Q} _ {\text { mobility }, l, t} ^ {*} = \phi (\mathbf {w}, \mathbf {h}, \mathbf {o}, \mathbf {g}),\tag{1}
$$

where $\mathbf { w } = \{ w _ { 0 } , w _ { 2 } , \ldots , w _ { 6 } \}$ is the day of week, $\mathbf { h } =$ $\{ h _ { 0 } , h _ { 2 } , \ldots , h _ { 2 3 } \}$ is the hour of day, $\mathbf { o } = \left\{ \boldsymbol { o } _ { 1 } \right\}$ is the average fleet interior status, and $\mathbf { g } = \{ g _ { 1 } \}$ is the average fleet exterior status. These independent variables have been encoded as binary variables, or in the case of o and g, scaled to a range of zero to one. Figure 3 provides an example from the city of Amsterdam, which illustrates feature sets w, h by location. There are significant differences between locations: For example, on a Sunday morning in Amsterdam in location $l { = } z { \mathrm { i p } }$ code 1012 (central train station), the rental likelihood of 5%–10% is much higher than in l� zip code 1014 (periphery), where the likelihood is less than 1%. For most zip codes, either a random forest regression or a bagged tree-based regression had the best predictive accuracy with an average root mean squared error (RMSE) of 1.02 in Stuttgart, 0.59 in Amsterdam, and 1.92 in San Diego. For a detailed description of the model selection approach, see Online Appendix A.1. For an overview of model parameterization and performance, refer to Online Appendix A.2.

As outlined previously, the EV market share in the up- and downregulation markets are marginal. Therefore, total expected demand for upregulation $\widehat { Q } _ { u p \_ r e g , t } ^ { * }$ and downregulation $\widehat { Q } _ { d o w n \_ r e g , t } ^ { * }$ is not a constraint for the resource allocation in resource planning (phase 2), and we refrain from predicting these values. For the expected rental market price $\widehat { P } _ { m o b i l i t y } ^ { * } , \mathsf { a }$ forecast is also not required as prices are deterministic and fixed.

The expected unit price for upregulation $\widehat { P } _ { u p \_ r e g , t } ^ { * }$ is determined as follows:

$$
\widehat {P} _ {u p \_ r e g, t} ^ {*} = \widehat {c} _ {u p \_ r e g, t} + \widehat {\pi} _ {u p \_ r e g, t},\tag{2}
$$

where $\widehat { c } _ { u p \_ r e g , t }$ is the expected unit cost the fleet operator incurs for selling up regulation, and $\widehat { \pi } _ { u p \_ r e g , t }$ is the expected unit profit margin that is parameterized by maximizing the overall profits for all previous time peri ods of the training data set. The unit profit margin makes sure that there is a careful consideration between the tra deoff of having a higher per unit profit at the risk that the market may not clear a pricey bid versus a lower per unit profit with a higher chance that the cheaper bid may be cleared by the market.

The expected unit price for down regulation $\widehat { P } _ { d o w n \_ r e g , t } ^ { * }$ is determined as follows:

$$
\widehat {P} _ {d o w n \_ r e g, t} ^ {*} = P _ {e l e c t r i c i t y, t} ^ {*} - (\widehat {c} _ {d o w n \_ r e g, t} + \widehat {\pi} _ {d o w n \_ r e g, t}).\tag{3}
$$

The logic of deriving $\widehat { P } _ { d o w n \_ r e g , t } ^ { * }$ is different from deriving $\widehat { P } _ { u p \_ r e g , t } ^ { * }$ . In the case of downregulation, we want to ensure that we offer less than what we would pay by charging at the guaranteed wholesale electricity tariff $P _ { e l e c t r i c i t y , t } ^ { * }$ . We therefore use $P _ { e l e c t r i c i t y , i } ^ { * }$ as a reference point. The profit-maximizing bid is then computed by deducting the cost of providing down regulation (defined in Equation (12)) plus a maximizing profit margin that has been learned over a two-month rolling training period. The two-month training set choice is data driven. We have a total of 14months of data. To be able to consider the effects over a whole year, we only have two months of data for the first months. For intermonth comparability, we used the same rolling time window for all consequent months as well.

When predicting expected product availability $\widehat { Q } _ { p , t } ^ { A } ,$ we already take into account a part of resource replanning (phase 4). In its essence, the issue we are dealing with is a classification problem. We have to decide how

## Figure 3. Rental Likelihood

![](/api/attachments/WWVWA7FE/fulltext/images/4cee3f6667d0406b75e0065f64246295b4581dbc63db46c2bac22c66ba1ec317.jpg)  
Notes. Rental likelihood plot indicating when EVs are rented out in Amsterdam, based on the day of the week, hour of the day (1=4 hour period), and zip code of where they were parked. There is a distinct difference in rental likelihoods, for instance, between the central station (1012) and the periphery (1014).

each of the EVs i should be classified into the different classes $p \in S$

To predict the energy storage available for mobility $\widehat { Q } _ { m o b i l i t y , l , t } ^ { A } ,$ , upregulation $\widehat { Q } _ { u p \_ r e g , t } ^ { A } ,$ and downregulation $\widehat { Q } _ { d o w n \_ r e g , t } ^ { A } ,$ we apply similar machine learning algorithms as for $Q _ { m o b i l i t y , l , t } ^ { * }$ . The expected availability of storage for mobility $\widehat { Q } _ { m o b i l i t y , l , t } ^ { A }$ (how much energy is stored in all vehicles at location l and time t) is determined analogous to Equation (1) by

$$
\widehat {Q} _ {m o b i l i t y, l, t} ^ {A} = \phi (\mathbf {w}, \mathbf {h}, \mathbf {o}, \mathbf {g}).\tag{4}
$$

A random forest regression model had the highest predictive accuracy for most zip codes with an average RMSE of 44.03 in Stuttgart, 33.43 in Amsterdam, and 143.08 in San Diego (see Online Appendix A.3 for details).

To predict the expected availability of storage for upregulation $\widehat { Q } _ { u p \_ r e g , t } ^ { A } ,$ that is, how much energy is stored in all vehicles and could be accessed for up regulation at time t, we first need to define the availability of storage for upregulation $Q _ { u p \_ r e g , t } ^ { A } \mathrm { : }$

$$
Q _ {u p \_ r e g, t} ^ {A} = \sum_ {i = 1} ^ {J} m i n (\delta_ {i, t} * \Delta t, S o C _ {i, t} * (1 - e _ {d i s c h a r g e})),\tag{5}
$$

where J is the set of vehicles i connected to a charging station at the start of period $t , \delta _ { i }$ is the discharging speed of the charging station to which vehicle i is connected at time $t , S o C _ { i , t }$ is the current SoC of a specific SEV i at the beginning of period $t ,$ and $e _ { d i s c h a r g e }$ is the efficiency rate for discharging taking into account any energy transmission losses during the discharging process.

Next, based on this definition of the available storage for upregulation, we predict the expected availability of storage for upregulation $\widehat { Q } _ { u p \_ r e g , t } ^ { A }$ using the following setup:

$$
\widehat {Q} _ {u p \_ r e g, t} ^ {A} = \phi (\mathbf {w}, \mathbf {h}, \mathbf {o}, \mathbf {g}).\tag{6}
$$

A bagged tree-based regression model had the highest predictive accuracy with an average RMSE of 10.37 in Stuttgart, 7.40 in Amsterdam, and 6.19 in San Diego (see Online Appendix A.4 for details).

The availability of storage for downregulation $Q _ { d o w n \_ r e g , t } ^ { A }$ (how much energy the vehicles can be maximally charged with and be accessed for down regulation at time t) is determined by

$$
Q _ {d o w n \_ r e g, t} ^ {A} = \sum_ {i = 1} ^ {J} m i n \left(\gamma_ {i, t} * \Delta t, \sum_ {i = 1} ^ {J} \frac {S o C _ {m a x , i} - S o C _ {i , t}}{1 - e _ {c h a r g e}}\right),\tag{7}
$$

where $\gamma _ { i , t }$ is the charging speed of the charging station to which vehicle i is connected at time t, and $e _ { c h a r g e }$ is the efficiency rate for charging to account for energy conversion losses during the charging process; $S o C _ { m a x , i }$ is the maximum battery capacity of vehicle i.

Next, based on this definition of the available storage for downregulation, we predict the expected availability of storage for down regulation $\widehat { Q } _ { d o w n \_ r e g , t } ^ { A }$ by

$$
\widehat {Q} _ {d o w n \_ r e g, t} ^ {A} = \phi (\mathbf {w}, \mathbf {h}, \mathbf {o}, \mathbf {g}).\tag{8}
$$

Highest predictive accuracies were obtained with a SVM in Stuttgart (RMSE � 7.98) and San Diego (RMSE � 5.03), whereas in Amsterdam, a bagged tree-based regression better captured the local demand patterns (RMSE � 6.65; see Online Appendix A.5 for details).

The expected unit cost to produce the respective services $\widehat { c } _ { p , t }$ <sub>t</sub> in a specific period are quite heterogeneous and need to be considered for each market separately. We do not consider the vehicle’s investment cost but only the operational cost that set the three different markets apart from each other.

The expected unit cost for mobility services $\widehat { c } _ { m o b i l i t y }$ are determined by

$$
\widehat {c} _ {m o b i l i t y, t} = d + \overline {{P}} _ {t r a i n, t} ^ {*},\tag{9}
$$

where d is the unit cost for battery depreciation, and $\overline { { P } } _ { t r a i n , t } ^ { * }$ is the average energy price paid over the course of the training period, which we define as a two-month moving window. By this definition, $\widehat { c } _ { m o b i l i t y , t }$ is only time dependent and does not depend on the location. This also results in a time-dependent unit profit for mobility $\widehat { \pi } _ { m o b i l i t y , t }$ <sub>t</sub> due to the fixed rental price. Only the expected rental demand $\widehat { Q } _ { m o b i l i t y , l , t } ^ { * }$ depends on the location. The expected unit cost for upregulation services $\widehat { c } _ { u p \_ r e g , t }$ are determined by

$$
\widehat {c} _ {u p \_ r e g, t} = d + \overline {{P}} _ {t r a i n, t} ^ {*} + \sum_ {j = 0} ^ {k} \widehat {\pi} _ {m o b i l i t y, t + j} * \lambda_ {u p \_ r e g, t + j},\tag{10}
$$

where the summation term incorporates the cost of not being able to serve mobility customers during the current time period t and not being able to serve customers in future periods $t + j$ until the committed vehicles have been recharged. The variable k is the total number of periods it takes to recharge the ${ \mathrm { E V } } \mathbf { s } ,$ rounded to the nearest full period (<sup>1</sup> hour). The variable k is defined as

$$
k = \text { round } \left(\frac {Q _ {u p , t} ^ {b i d}}{I * \delta * \Delta t}\right),
$$

where $Q _ { u p \_ r e g , t } ^ { b i d }$ is the bid quantity for upregulation; $\widehat { \pi } _ { m o b i l i t y , t + j }$ are the expected opportunity costs. The costs are measured in terms of revenue a fleet owner would have earned per kilowatt hour in the respective periods $t , t + 1 , t + 2 , \ldots , t + k$ if the fleet lost out on rentals while committed to the upregulation market in period t or while recharging in subsequent periods $t + 1 , t + 2 ,$ $\cdots , t + h$ . The variable $\lambda _ { u p \_ r e g }$ acts as a quantity weighting factor for the computation of the total opportunity cost over the k+ 1 periods. We define $\lambda _ { u p \_ r e g }$ as follows:

$$
\begin{array}{l} \lambda_ {u p \_ r e g, t + j} = \\ \left\{ \begin{array}{l l} 0, & \text {if} Q _ {u p \_ r e g, t} ^ {b i d} \leq 0 \\ \frac {Q _ {u p \_ r e g , t} ^ {b i d}}{\Delta \widehat {Q} _ {m o b i l i t y , t + j} ^ {A}}, & \text {if} 0 <   Q _ {u p \_ r e g, t} ^ {b i d} <   \Delta \widehat {Q} _ {m o b i l i t y, t + j} ^ {A} \\ 1, & \text {if} \Delta \widehat {Q} _ {m o b i l i t y, t + j} ^ {A} \leq 0 \\ 1, & \text {if} Q _ {u p \_ r e g, t} ^ {b i d} \geq \Delta \widehat {Q} _ {m o b i l i t y, t + j} ^ {A}, \end{array} \right. \end{array}\tag{11}
$$

where $\begin{array} { r } { \Delta \widehat { Q } _ { m o b i l i t y , t + j } ^ { A } = \sum _ { l = 1 } ^ { L } ( \widehat { Q } _ { m o b i l i t y , l , t + j } ^ { A } - \widehat { Q } _ { m o b i l i t y , l , t + j } ^ { * } ) } \end{array}$ is the delta in expected available versus required SoC to fulfill the mobility demand across all locations. The fraction $\frac { Q _ { u p \_ r e g , t } ^ { b i d } } { \Delta Q _ { m o b i l i t y , t + j } ^ { A } }$ thus describes the share of lost rentals in period t + j that is attributable to the upregulation in period t. The opportunity cost therefore only applies if there is more demand for mobility services than can be served by the SEV fleet.

When determining the bidding price in Equation (10), the variable $\lambda _ { u p \_ r e g }$ acts as a weighting factor. If $\lambda _ { u p \_ r e g , t + j }$ is zero, then the profits that could be earned by renting the vehicles are not priced into the upregulation bidding price at all, for example, when there is a surplus of vehicles in the night. If $\bar { \lambda _ { u p \_ r e g , t + j } }$ is one, then the full expected profits from rentals are priced into the up regulation bidding price, for example, during rush hour. This is a key factor in deciding how to commit the resources when there is insufficient energy stored in the vehicles to meet the demand in both markets. Specifically, $Q _ { u p \_ r e g , t } ^ { b i d } \le 0$ is a hypothetical case. When we do not bid on the upregulation market, we also do not need to determine a component of the price at which to bid. If, however, $0 < \hat { Q } _ { u p \_ r e g , t } ^ { b i d } < \Delta \widehat { Q } _ { m o b i l i t y , t + j } ^ { \ - { \scriptsize \Omega } ^ { \ - { \scriptsize \Lambda } } } ,$ then the closer the bid quantity comes to what is expected to be available, the more likely it becomes that we need to reject a rental customer. Therefore, the factor λ approaches one as the bid quantity approaches the energy that is available. If $\bar { \Delta { Q } } _ { m o b i l i t y , t + j } ^ { - 1 } \dot { \leq } 0 .$ , then the model predicts that there is already a shortage of energy for mobility. Every additional unit that is assigned to the up regulation market will therefore very likely incur the cost of rejecting a rental customer. Therefore, the full unit cost of a lost rental $( \lambda _ { u p \_ r e g , t + j } = 1 )$ is incorporated in the bid price in Equation (10). Last, if $Q _ { u p \_ r e g , t } ^ { b i d } \geq \Delta \widehat { Q } _ { m o b i l i t y , t + j } ^ { A } ,$ then even though there were vehicles available in excess of mobility, more than what is predicted to be available is committed as a bid. Consequently, it is very likely that we may need to reject a rental customer and we need to incorporate the unit cost of lost rentals $( \lambda _ { u p \_ r e g , t + j } = 1 )$ ).

$\widehat { c } _ { d o w n \_ r e g , t }$ is determined by

$$
\widehat {c} _ {d o w n \_ r e g, t} = \widehat {\pi} _ {m o b i l i t y, t} * \lambda_ {d o w n \_ r e g, t}.\tag{12}
$$

We do not include the battery depreciation cost d here, which is considered for energy outflows to avoid double counting. Again, the expected average profit from rental market is an important cost consideration as it ensures that SEVs are less likely to be committed for downregu lation when it is probable that they will be rented out. Again we apply a weighting factor to determine what proportion of the unit profits should be allocated. We define $\lambda _ { d o w n \_ r e g , t }$ as follows:

$$
\begin{array}{l l} \lambda_ {d o w n \_ r e g, t} = \\ \left\{ \begin{array}{l l} 0, & \text {if} Q _ {d o w n \_ r e g, t} ^ {b i d} \leq 0 \\ \frac {Q _ {d o w n \_ r e g , t} ^ {b i d}}{\Delta \widehat {Q} _ {m o b i l i t y , t + j} ^ {A}}, & \text {if} 0 <   Q _ {d o w n \_ r e g, t} ^ {b i d} <   \Delta \widehat {Q} _ {m o b i l i t y, t + j} ^ {A} \\ 1, & \text {if} \Delta \widehat {Q} _ {m o b i l i t y, t + j} ^ {A} \leq 0 \\ 1, & \text {if} Q _ {d o w n \_ r e g, t} ^ {b i d} \geq \Delta \widehat {Q} _ {m o b i l i t y, t + j} ^ {A}. \end{array} \right. \end{array}\tag{13}
$$

## 4.2. Phase 2: Resource Planning

In this phase, all product markets $p \in S$ are ranked in a pecking order based on profitability. Based on the previously calculated expected clearing prices $\widehat { P } _ { p , t } ^ { * } ,$ in combination with expected production cost ${ \widehat { c } } _ { p , t } ,$ an expected unit profit $\widehat { \pi } _ { p , t }$ is either derived directly or computed from a rolling two-month training data set. The tool then allocates storage quantities to each of these markets depending on profitability and expected demanded quantities. Because the charging and discharging cost already include the cost of forgone rentals (see Equations (10) and (12)), the cheapest bids to charge and discharge are submitted to the market according to the pecking order until the expected available quota for the quantities $\widehat { Q } _ { u p \_ r e g , t } ^ { \scriptscriptstyle A }$ and $\widehat { Q } _ { d o w n \_ r e g , t } ^ { A }$ are fulfilled. Only if the quantities are cleared are the corresponding vehicles withdrawn from the rental market, which clears at a later point in time. Both discharging and charging bids can be submitted for the same period independently because a market will never require both up- and downregulation at the same time. Only one bid is submitted to each respective market for a time period due to a minimum lot size. It means that an SEV fleet owner can only participate in a market if the owner can offer at least a certain quantity. Because we consider relatively small fleets, the fleet itself cannot meet the minimum lot size today. However, this issue will diminish in the future when there will be more EVs. Additionally, if small fleets want to participate they can join forces with aggregators that aggregate multiple small energy producers (e.g., rooftop solar, small wind turbines) to quantities that can participate in the market. Therefore, this is only a theoretical problem, and not considering lot size allows us to study the problem in isolation.

## 4.3. Phase 3: Tendering

In the tendering phase, the information from resource planning (phase 2) is submitted as bids to the upregulation $\langle Q _ { u p \_ r e g , t } ^ { b i d } , \widehat { P } _ { u p \_ r e g , t } ^ { * } \rangle$ , downregulation $\langle Q _ { d o w n \_ r e g , t } ^ { b i \bar { d } } ,$ $\widehat { P } _ { d o w n \_ r e g , t } ^ { * } \rangle$ , and rental $\langle Q _ { m o b i l i t y , l , t } ^ { b i d } , \widehat { P } _ { m o b i l i t y , t } ^ { * } \rangle$ markets. Because of the varying clearing horizons, bids to the balancing markets are submitted first. All remaining quantities will be automatically made available on the rental market at the fixed price.

The DSS submits bids $\langle Q _ { u p \_ r e g , t } ^ { b i d } , \widehat { P } _ { u p \_ r e g , t } ^ { * } \rangle$ to the upregulation market for each respective time period t. The quantity submitted corresponds to the quantity determined in planning (phase 2) with the expected clearing prices from market and operational data gathering (phase 1). Figure 4 shows an exemplary bid quantity and bid price, broken down into its various components, and puts it in comparison with other bids in the auction. It shows how the price is constructed based on the cost to charge the battery $\overline { { P } } _ { t r a i n , t } ^ { * } ,$ the battery depreciation $d ,$ the expected rental profits that could be earned with the vehicle instead as opportunity cost $\begin{array} { r } { \sum _ { j = 0 } ^ { k } \widehat { \pi } _ { m o b i l i t y , t + j } * \lambda _ { u p \_ r e g , t + j } , } \end{array}$ and the expected unit profits derived from the training period $\bar { \widehat { \pi } } _ { u p \_ r e g , t }$ to make a profit in the pay-as-bid auction. In this example, our ask is cleared as we can offer the electricity required by the market at a cheaper price than other asks. The tool also submits bids $\langle \dot { Q } _ { d o w n \_ r e g , t } ^ { b i d } , \widehat { P } _ { d o w n \_ r e g , t } ^ { * } \rangle$ to the downregulation market for each respective time period t. Also here, the quantity submitted corresponds to the quantity determined in planning (phase 2) with the expected clearing prices from market and operational data gathering (phase 1).

## 4.4. Phase 4: Resource Replanning

In the resource replanning phase, the fleet owner provisions sufficient EVs to match the quantity of energy that has been committed. If the fleet owner offered to sell more vehicles at time period t than are available, and replacement vehicles cannot be found, the fleet owner has to make a tradeoff between the markets in real time. To make that decision, the fleet owner needs to evaluate the profits $\pi _ { p , t }$ and penalties or fines $F _ { p , t }$ associated with not fulfilling commitments.

During the resource replanning phase, the fleet owner knows the actual demand for mobility $\begin{array} { r } { \sum _ { l = 1 } ^ { L } Q _ { m o b i l i t y , l , t } ^ { * } , } \end{array}$ , as well as the cleared quantities $\boldsymbol { Q } _ { u p \_ r e g , t } ^ { * }$ and $Q _ { d o w n \_ r e g , t } ^ { * }$ and prices $P _ { u p \_ r e g , t } ^ { * }$ and $\bar { P _ { d o w n \_ r e g , t } ^ { * } }$ for each market. Replanning may be required when the available vehicles cannot meet a commitment on a market. This would for example be the case in a situation where $\begin{array} { r } { \sum _ { l = 1 } ^ { L } Q _ { m o b i l i t y , l , t } ^ { A } < } \end{array}$ $\begin{array} { r } { \sum _ { l = 1 } ^ { L } Q _ { m o b i l i t y , l , t } ^ { * } . } \end{array}$ Because of the planning horizon of up to one week in the reserve market, prediction errors are not uncommon. For example, we see in the actual data that a customer rented a vehicle that the DSS in our simulation decided to commit to the up- or downregulation market. First, the tool checks whether another EV is available in the immediate vicinity. We assume that a customer would be indifferent between renting another vehicle approximately 250m away if a vehicle was committed to up- or downregulation markets. The willingness to walk measured in terms distance to the originally requested vehicle is drawn from a normal distribution with a mean of $\mu = 2 5 0$ m and a standard deviation of $\sigma { = } 1 0 0 \mathrm { m }$ . This value seems realistic to us, but we have also tested a mean of $\mu = 1 0 0$ and $\mu = 5 0 0 \mathrm { m }$ with no significant difference in results. Distance is computed as the great-circle distance between the coordinates that was calculated using the haversine formula (Robusto 1957).

Figure 4. Market Clearing Process  
![](/api/attachments/WWVWA7FE/fulltext/images/c4c197cce63ef9e80e1c4dd9340251abbc12683a190a60e8b5b2611e51cbc58a.jpg)  
Notes. The graph shows the supply curve for the purchase of energy to bridge a deficit in the grid; in this example, an additional 1200 kWh is required. As our SEV bid provides this electricity cheaper than bid 16, which is the last partially cleared bid, the market agrees to buy $Q _ { u p \_ r e g } ^ { * } =$ 300 kWh from the fleet.

Because a fleet owner incurs high penalties when not meeting the full committed quantities in the balancing markets, and, if failing to deliver repeatedly, will be excluded entirely from the market for reliability reasons, we need to ensure that the tool gives priority to fulfill commitments on the balancing services market at all times. To ensure this, we assume the following penalties for $F _ { m o b i l i t y } = \$ 0$ and $F _ { u p \_ r e g } = \Phi 9 , 9 9 9 , F _ { d o w n \_ r e g } = \Phi 9 , 9 9 9 .$ . In our evaluation, we incur the penalty whenever we predict that sufficient vehicles for regulation are available and then commit these vehicles. However, consequently, once the timeslot arrives, we do not have sufficient vehicles with capacity to meet that commitment. For each vehicle and timeslot in which we cannot meet the commitments, the penalties are incurred and count into the profit and losses. The amount is an arbitrary high number chosen in such a way that violating the penalty threshold would not be part of an optimal solution.

The penalties for up- and downregulation are only applied if on average less than 95% of the committed quantity can be delivered. The 95% threshold is common in regulation markets. After the replanning, the actual allocations $\begin{array} { r } { \sum _ { l = 1 } ^ { L } Q _ { m o b i l i t y , l , t } , Q _ { u p \_ r e g , t } , } \end{array}$ , and $Q _ { d o w n \_ r e g , }$ are known.

## 4.5. Phase 5: Execution

During the execution phase, the individual allocation of the vehicles to the respective markets is executed in real time. This includes accounting for realized profits. The system is executed and accounted for in a simulation environment that is parameterized using real data on availability of vehicles and their movements in the three markets we consider and is supplemented with data on electricity prices from the respective reserve markets. A discrete event simulation is most suitable for evaluating our strategies, as we are dealing with a complex dynamic system that can be analyzed in discrete time periods but which would require considerable time and financial resource to build in the real world due to the required technical updates in the existing charging and battery infrastructure.

By participating in the market, we may have an influence on market equilibrium, and this might in turn lead other market participants to behave differently. However, we argue that there is no endogeneity problem from reactions to our market participation as the asks and bids of other participants are aligned with their preferences. Discriminatory-price multiunit auctions are not incentive compatible, but our approach will work with any mechanism. For example, the uniform-price multiunit auction can be designed to be posterior regret-free; that is, even though the mechanism is not incentive compatible a priori, no one could benefit from not bidding their true valuation when evaluating allocation ex post (Bapna et al. 2005). Under these mechanisms, other market participants have no incentive to alter their behavior in response to new market entrants. Our methodology will also work well with this kind of mechanism. Although the profits may be different, the structural results will not change.

## 5. Evaluation and Results

In this section, we will discuss the business case and will evaluate the DSS’s decisions in terms of accuracy, incurred penalties, vehicle utilization, and profits achieved in each market.

The DSS developed in this paper makes decisions to maximize gross profits without knowing which rental transactions are going to happen in the future. Because of this uncertainty, the algorithm necessarily makes errors in the bidding process. Therefore, we evaluate the decision accuracy of our model. The error matrix (Table 3) shows how the tool committed its resources to the respective markets $Q _ { m o b i l i t y } , Q _ { u p \_ r e g } ,$ , and $Q _ { d o w n \_ r e g }$ (where $Q _ { u p \_ r e g }$ and $Q _ { d o w n \_ r e g }$ was combined into a single $Q _ { V ~ P P }$ for clarity). The error matrix compares what commitments were made against which commitments would have been optimal given perfect foresight. For a discussion on how our local predictions are influenced by nonrecurring events such as election days or sport games, see Online Appendix B.1.

The seemingly low accuracy of the model ranging from 20% to 58% versus the perfect foresight case can be explained by the stratified sampling approach that favors markets depending on the payoffs and penalties. At the expense of the accuracy for predictions of resource availability for the up- and downregulation market, which is between 17% and 56%, our model strategically increases the accuracy of mobility demand and supply predictions to 99%–100% depending on location, due to the comparably higher profits to be earned on the mobility market. Although there are slight differences per location, we see a consistently high accuracy across locations. The forecasting accuracy is favored by the fact that the setting allows us to forecast aggregate vehicle availability at a ZIP code level. Correspondingly, ZIP codes with fewer vehicles are generally more difficult to forecast than ZIP codes with many vehicles. An additional facilitating factor is a distinct seasonal pattern in vehicle availability, which our model takes advantage of.

Table 3. Confusion Matrix (%)

<table><tr><td rowspan="2">Optimal</td><td colspan="2">Stuttgart</td><td colspan="2">Amsterdam</td><td colspan="2">San Diego</td></tr><tr><td>VPP</td><td>Rented</td><td>VPP</td><td>Rented</td><td>VPP</td><td>Rented</td></tr><tr><td>VPP</td><td>53.00%</td><td>42.28%</td><td>28.11%</td><td>68.12%</td><td>16.89%</td><td>80.27%</td></tr><tr><td>Rented</td><td>0.07%</td><td>4.64%</td><td>0.00%</td><td>3.76%</td><td>0.01%</td><td>2.83%</td></tr></table>

Notes. The matrix shows the accuracy of FleetPower’s decisions for EVs parked at a charging station. Because of the asymmetric pay-off the algorithm is trained not to bid for a VPP when rental transactions occur.

The appropriate tradeoff between the accuracies reflects that errors in committing SEVs to a VPP when they could be rented out are the most significant in terms of their impact on profitability due to the asymmetric payoffs. Because of the high prediction accuracy for mobility demand, the DSS only loses out on rental transactions in 0%–0.07% of all transactions depending on the location due to resource shortages. The key to high accuracy in market and operational data gathering (phase 1) is the weighting in favor of the rentals. The weighting allows us to have an impeccable accuracy for rentals, with high monetary rewards. This comes at the expense of the accuracy to predict when vehicles are available to sell electricity, but because of the significantly lower returns from selling electricity, it does not impact the profitability nearly as much. Therefore, the model would be more likely to reserve the vehicles for rentals in ZIP codes with few vehicles and therefore higher uncertainty but with a high accuracy for rentals as a result.

Once in resource replanning (phase 4), we favor upand downregulation markets due to the high penalties $F _ { u p \_ r e g }$ and $F _ { d o w n \_ r e g }$ . Therefore, the tool is always able to deliver at least 95% of all $Q _ { u p \_ r e g } ^ { * } , \mathrm { a n d } Q _ { d o w n \_ r e g } ^ { * }$ and hence avoids penalties on these markets. This, however, comes at the cost of bidding significantly fewer $Q _ { u p \_ r e g } ^ { b i d }$ and $Q _ { d o w n \_ r e g } ^ { b i d } ,$ which is a good way to avoid penalty costs effectively.

Committing SEVs to the up- and downregulation market enhances the utilization of the vehicles. The utilization increases from 3% to 5% when using the vehicles for mobility services only to 7% to 35% when applying our proposed framework to use the vehicles for up- and downregulation services next to the mobility business, depending on the city. The committed quantities $Q _ { p } ^ { b i d }$ on the respective markets are a lower bound of utilization as not all bids are cleared by the market. Although utilization gives a good overview over the quantities committed to the up- and downregulation markets on top of the mobility market, it does not reflect the payoffs. Using the vehicle for one service may be much more ben eficial than for another. To evaluate the asymmetric pay offs appropriately, we therefore consider the total profits with and without VPPs and the profitability by market.

Figure 5 shows the gross profits by market of Car2Go in Stuttgart, Amsterdam, and San Diego over time. Although the gross profits (white bar) in San Diego are volatile throughout the year, there is a clear seasonal pat tern in the winter period in Amsterdam and Stuttgart. The additional benefits from using the fleet as a VPP consistently increase profits during the entire year but is more pronounced in Stuttgart and San Diego. Committing vehicles to the down regulation market consistently increases profits each month (gray bar) compared with the base case of participating in a mobility market only. Committing vehicles to the up regulation market increases profits only marginally (black bar). If we break down the annual gross profits per SEV, taking the example of Stuttgart, fleet owners make \$3,900 from the rentals of an average SEV, save \$163 by charging during cheaper time periods, and make an additional \$14 from discharging electricity to the grid.

The error matrix (Table 4) illustrates how the DSS benefits from committing its resources to the respective markets. The matrix also provides insights on how the system compares to a naive strategy where the vehicles are always made available for rentals. The table shows the actual condition on the y axis and the condition predicted by FleetPower on the x axis. The value in column 2/row 2 shows the total profit from rental instances where FleetPower predicted that the vehicles should be made available for rental. Column 1/row 2 shows the total losses where FleetPower predicted it would have been more profitable to commit vehicles to an up- or downregulation market, whereas it was more profitable to rent them. The profits from up- and downregulation in these cases are so low that they are negligible. In this case, rental customers were turned away, and the corresponding rental revenues did not materialize. The combination of row 2 therefore represents a naive strategy. Row 1 shows what can be gained on top of the naive strategy. Column 2/row 1 shows \$0 losses in all regions. Because of the high penalties for $F _ { u p \_ r e g }$ and $F _ { d o w n \_ r e g } ,$ FleetPower never predicts that a vehicle should be rented while it is actually needed on the up- or downregulation market. Therefore, the high penalties do not materialize. Column 1/row 1 therefore represents what is gained on top of a naive, rental only strategy and demonstrates, in combination with what one would lose in column 1/row 2, an overview over the benefits of such a strategy. For a visual representation of the profits, see Figure 6, which shows that in Stuttgart, the rentals earned \$1,915,000, but \$31,000 in rentals (2,173 transactions) had to be turned away in favor of an additional \$118,000 profits on the energy market. Therefore, the net gain of analytics in this case is \$87,000 per year or 4.4%. Amsterdam and San Diego exhibit a similar pattern.

Figure 5. Yearly Profits  
![](/api/attachments/WWVWA7FE/fulltext/images/e74c9218361420ed4fe337ad4cc07afd59c46c273b317c601498895c7e362ff7.jpg)

![](/api/attachments/WWVWA7FE/fulltext/images/652747fa746bf27b277ab83872e82e27e072f73e96769bff5eec59b57dc2abcf.jpg)  
Note. The profits from offering VPP power on the real-time market increases the gross profits of Car2Go consistently.

![](/api/attachments/WWVWA7FE/fulltext/images/a6c0076e8b885a353908aa1b8a03fd90461d204d75a2bafd4834959544bb1511.jpg)

Table 4. Confusion Matrix (in \$1,000)

<table><tr><td rowspan="2">Optimal</td><td colspan="2">Stuttgart</td><td colspan="2">Amsterdam</td><td colspan="2">San Diego</td></tr><tr><td>VPP</td><td>Rented</td><td>VPP</td><td>Rented</td><td>VPP</td><td>Rented</td></tr><tr><td>VPP</td><td>118</td><td>0</td><td>21</td><td>0</td><td>13</td><td>0</td></tr><tr><td>Rented</td><td>-31</td><td>1915</td><td>-1.4</td><td>1092</td><td>-0.7</td><td>396</td></tr></table>

Notes. The matrix shows the monetary impact of FleetPower’s decisions. The added value from VPP exceeds by far the losses from lost rentals in all cities.

As can be seen, the system’s decisions have resulted in profits in all three cities. In particular, the earnings from EVs that act as VPPs exceed the opportunity cost of lost rentals by far. In the other cities, the use of FleetPower increases gross profits by 1.8% in Amsterdam and 3% in San Diego. We attribute these differences to the price levels in the case of Amsterdam and in the case of San Diego as stemming from a lack of charging infrastructure. We analyze how a better availability of charging stations in the future may affect these results in Online Appendix B.2.

With current energy prices, 93% of the additional gross profits due to VPPs are earned by committing vehicles to the downregulation market; in many cases, the grid needs to urgently get rid of surplus electricity with the effect that Car2Go actually pays less than the industrial electricity tariff and is even paid to charge its EVs in some timeslots.

Although Car2Go consumes a substantial amount of surplus energy from the downregulation market, it discharges its SEVs only infrequently in Stuttgart and San Diego and never in Amsterdam. Because of the low prices on the upregulation market, the cost of battery wear and mobility cannot be covered, with the consequence that bids to discharge SEVs are cleared infrequently. The following example illustrates this use case. The average rental transaction earns \$15/kWh of energy driven, whereas the industrial electricity tariff is \$0.1/kWh. Therefore, the electricity price would have to increase by a factor of 75 from \$0.1/kWh to \$7.5/kWh for rentals and V2G to achieve economic parity. In the reserve market data, we do see that prices can get that high on occasion. However, the highest price we observe in the balancing market in the period under consideration is \$5.99/kWh in isolated time slots. This explains why we rarely see that selling electricity back to the grid is profitable in our study.

The robustness of the results is discussed in the online appendix. In the online appendix, we analyze how introducing more renewable energy sources may affect demand and how competition from other EVs may affect supply. We find that more volatile prices from the introduction of more renewable energy sources will significantly and positively affect the business case (Online Appendix B.3). At the same time, we find that competition from other EV fleets will not significantly affect the business model. Even if all vehicles in a given market were EVs, they would not be able to balance the entire market alone (Online Appendix B.4).

Figure 6. Profit Waterfall Chart  
![](/api/attachments/WWVWA7FE/fulltext/images/5c3717b216499f7ff7f822fb472e7fb8576e81ea7ddec732f8241f45fe6f2a66.jpg)

![](/api/attachments/WWVWA7FE/fulltext/images/83e249d87596be4648bc82adcaea879f57c679ac03ca5a40a28b2e73801887b4.jpg)

![](/api/attachments/WWVWA7FE/fulltext/images/6068b9b7bad77617fc8c4c4b13eec8a428af5051f574d311787085d04a0ac19c.jpg)  
Note. Although rental profits are the largest contributor to the bottom line, VPP profits are a valuable additional source of income for the carshar ing operator and make up for opportunity cost from rejected rentals or VPPs.

## 6. Discussion and Future Work

We presented a DSS for real-time multiproduct resource allocation via smart markets entitled FleetPower that enables operators of SEV fleets to allocate resources more profitably across multiple markets. We now discuss the key conclusions that can be drawn from this research. We also elaborate on the relevance and generalizability of our findings. We end with suggestions for future work.

FleetPower follows a five-phase blueprint architecture. The key peculiarity of the SEV case is that mobility markets have a local component in which a geographical dimension plays a vital role. The key to the successful operation of the DSS for SEV fleets lies in the realization that all three services (renting, upregulation, and downregulation) being offered in fact rely on the same resource, that is, the battery SoC as measured in kilowatt hours.

One week prior to delivery we gather market and internal information in real time to estimate demand, price levels, and expected margins per each market, as well as own resource availability based on which markets are ranked according to attractiveness for each period. Using state-of-the-art machine learning algorithms, we achieve high accuracies of 99% in this initial prediction. FleetPower then strategically bids in the markets by learning margin levels that would have been profitable in the past. At gate closure of the electricity balancing markets, resources for which bids were not cleared are placed on the rental market again. At the start of period t, any discrepancies between commitments and resource availability are detected and managed. Because of the strong predictive performance of our approach and having included a strong penalty factor for overpredicting resource availability in the electricity balancing markets where high penalties apply, we experience resource shortages in the balancing markets in only 0%–0.07% of cases depending on location.

Overall, we achieve utilization improvements measured in terms of productive versus idle time for each SEV of 233%–700% depending on the market. This translates to gross profit improvements for the SEV fleet by 1.8% and 4.4%, depending on the city, representing an increase in annual gross profit of up to \$86,000. The discrepancies in relative improvements can be explained by the highly asymmetric profitability levels between the markets, with electricity balancing services being significantly less profitable in most cases. We show that V2G profitability depends on the interplay between the bid price that is set for V2G, whether the market accepts that bid price, and the probability of a rental. If V2G electricity is offered at a high price and the market accepts this offer due to high demand, then V2G can be profitable in two cases: either when the high price is higher than the rental profit, which happens in isolated cases only, or when the probability of a rental transaction for a specific location and time is very low, which occurs quite frequently. We compare the DSS’s performance across Stuttgart, Amsterdam, and San Diego and are able to show that the proposed framework is effective across different geographies. We are also able to demonstrate how profitability is affected by the charging infrastructure in place and by the price levels on the balancing markets.

At a higher level of abstraction, we show that digital market-based exchanges provide an ideal interface with additional revenue pools for multiproduct resources. By interfacing with smart goods and/or service markets, operators of multiproduct resources can dynamically evaluate where to commit which type of product in what quantity and at what price with a view to maximizing resource utilization and profitability. This is enabled by intelligent DSS that tap into the ubiquitous data flows stemming from smart markets, processing them for realtime autonomous decision making. The digital nature of smart markets then allows for a direct interaction of soft ware agents and markets, thus creating the opportunity for fully autonomous agent-enabled multiproduct resource allocation.

We argued that this type of decision support can be useful in terms of improving allocation decisions. In particular, in cases where multiproduct resources exist but are not managed in real time. However, in terms of enabling multipurposing of resources in situations where single-product resources can be turned into multiproduct resources, the inherent complexities become manageable through the use of DSS. We expect such opportunities to arise more often in the future as smart markets, such as digital platform economies (Constantinides et al. 2018), become more common in key sectors. Our DSS readily generalizes beyond the field of multiproduct SEVs. We characterize possible application fields for our presented DSS by considering two dimensions: (1) diversity of possible products/services that can be produced with/from the resource and (2) diversity of market mechanisms by which these products/services are sold. The first dimension pertains to how many pro ducts and services can be offered by the resource and how distinct these individual products and services are in terms of required inputs (materials, machinery time, labor, etc.). The second dimension embodies the number of different mechanisms and the distinctiveness in mechanism design regarding bidding schedule, and payment rules and other market design features.

Our DSS can handle all degrees of product and mechanism diversity. However, it is especially applicable to high complexity situations with high diversity of products/services and high diversity of market mechanisms (highlighted in Figure 7). As opposed to other, perhaps less complex situations, the management of diverse mechanisms in combination with diverse products will in most cases surpass human abilities, and thus necessitates the use of our blueprint for a DSS. We see particularly large potential benefits in low utilization environments where, through interfacing with smart electronic markets and platforms in real time, new applications for a specific resource become accessible and implementable with state-of-the-art DSS. An additional beneficial criterion is resource flexibility. Our DSS is likely to work well in situations where resources are physically flexible enough to switch between product types at very short notice with limited switching time and cost to take maximum advantage of the real-time nature of smart markets. We list selected examples to which our configuration of DSS could apply:

• A freelance gig economy worker can dynamically choose where to offer her work based on price signals. For example, she might choose to offer ride-hailing services during a certain period of the day and offer other services, such as food delivery, during low demand periods. Our DSS can provide a pecking order of these markets per each period and enable the gig economy worker to place offers within each market accordingly so as to maximize utilization and profitability of her resource, the working time. Since value is locationdependent in both product markets, the framework would need to incorporate a geographical dimension when evaluating market attractiveness.

Figure 7. Characterization of Application Fields  
![](/api/attachments/WWVWA7FE/fulltext/images/688fe060e866d872e75f3bd9892e511190b003b014c8563c943166805eed9145.jpg)  
Note. Our DSS applies in particular to high-complexity situations characterized by high product diversity and high market mechanism diversity.

• A shared autonomous taxi could one day either be used to provide personal mobility or goods mobility (Ketter et al. 2022). Similarly to the case presented in this research, the framework could be employed to dynamically evaluate and compare market attractiveness in each period and each location. Indi vidual vehicles could then be allocated to each mark correspondingly.

• A combined heat and power (CHP) generation unit can produce power and heat at the same time with variable proportion. Beyond a certain required heat and power base share, CHP plants can either produce heat or power. Although markets for electricity are already digital and close to real time, this is not yet the case for the heating market, which operates largely on long-term bilateral contracts. As this market evolves, real-time multiproduct resource allocation becomes possible and DSS can be developed using our tool as blueprint.

In the future, three avenues of further research could prove particularly fruitful. First, an implementation of FleetPower in a real-world setting could provide valuable insight regarding the real-world performance of our framework and its adaptation to the case of SEV fleets. This setting could be complemented with a study on how SEV fleets may integrate with aggregators who potentially derive synergies by coupling the SEVs with other energy sources.

Second, the application of the proposed DSS to other multiproduct resource situations with different characteristics to the one tested in this research could be useful to validate the generalizability of the framework and test its performance in other, perhaps less favorable situations. For example, a “worst-case” scenario could be tested that involves a resource that is already managed as a multiproduct resource and already operates at high levels of utilization. The achieved improvements versus the status quo in this situation could be an indication for a lower bound on our framework’s achievable benefits. An example for such a case could be a traditionally managed CHP plant. Similarly, a resource with more potential outlet markets could be tested to evaluate how valid solution approaches can be designed along each of the framework components that can deal with the associated increase in complexity.

Third, we see research potential regarding the characteristics of smart market mechanisms that enable and/o ease multiproduct resource allocation. Understanding how smart markets can and should be designed to enable and promote multiproduct resource allocation is relevant for policy makers who wish to maximize social welfare by enabling better resource allocation as well as market operators who wish to attract new market participants. A subordinate question is which mechanisms work well in combination and why. The answer could be important criteria for resource owners when selecting markets to participate in. One specific policy question that deserves further research is the market requirement to submit bids one week in advance. A forecasting horizon shorter than one week would allow SEVs to make even more accurate vehicle availability forecasts. Information such as recent vehicle availability or even weather data (e.g. more people may rent vehicles when it rains) could complement seasonal patterns. In this paper we show that the accuracy of our predictive model is already very high due to stable seasonal patterns and comes at the expense of bidding conservatively for V2G. A shorter forecasting horizon would allow SEVs to bid with more certainty about vehicle availability and therefore less conservatively for V2G, which could increase V2G profits significantly.

## Acknowledgments

This paper is a significantly revised and expanded version of a dissertation (Kahlen 2017).

## Endnote

<sup>1</sup> See https://ev-database.org/car/1132/Smart-EQ-fortwo-coupe (accessed July 6, 2019).

## References

Abdel-Aal MA, Syed MN, Selim SZ (2017) Multi-product selective newsvendor problem with service level constraints and market selection flexibility. Internat. J. Production Res. 55(1):96–117.

Adomavicius G, Gupta A, Zhdanov D (2009) Designing intelligent software agents for auctions with limited information feedback. Inform. Systems Res. 20(4):507–526.

Agricola AEA (2014) DENA ancillary services study 2030. Security and reliability of a power supply with a high percentage of renewable energy. Technical report, German Energy Agency, Berlin.

Anandalingam G, Day RW, Raghavan S (2005) The landscape of electronic market design. Management Sci. 51(3):316–327.

Avci B, Girotra K, Netessine S (2015) Electric vehicles with a battery switching station: Adoption and environmental impact. Man agement Sci. 61(4):772–794.

Bapna R, Goes P, Gupta A (2003) Analysis and design of businessto-consumer online auctions. Management Sci. 49(1):85–101.

Bapna R, Goes P, Gupta A (2005) Pricing and allocation for quality differentiated online services. Management Sci. 51(7):1141–1150.

Bapna R, Chang SA, Goes P, Gupta A (2009) Overlapping online auctions: Empirical characterization of bidder strategies and auction prices. Management Inform. Systems Quart. 33(4):763–767.

Bapna R, Goes P, Gupta A, Jin Y (2004) User heterogeneity and its impact on electronic auction market design: An empirical exploration. Management Inform. Systems Quart. 28(1):21–43.

Bapna R, Goes P, Gupta A, Karuga G (2008) Predicting bidders’ willingness to pay in online multiunit ascending auctions: Analytical and empirical insights. INFORMS J. Comput. 20(3):345–355.

Bardhi F, Eckhardt GM (2012) Access-based consumption: The case of car sharing. J. Consumer Res. 39(4):881–898.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets. Inform. Systems Res. 21(4):688–699.

Burns LD (2013) Sustainable mobility: A vision of our transport future. Nature 497(7448):181–182.

Chevaleyre Y, Dunne PE, Endriss U, Lang J, Lemaˆıtre M, Maudet N, Padget J, Phelps S, et al. (2006) Issues in multiagent resource allocation. Informatica 30(1):3–31.

Constantinides P, Henfridsson O, Parker GG (2018) Introduction: Platforms and infrastructures in the digital age. Inform. System Res. 29(2):381–400.

Cramton P (2017) Electricity market design. Oxford Rev. Econom. Pol icy 33(4):589–612.

Cramton P, Geddes R, Ockenfels A (2018) Set road charges in real time to ease traffic. Nature 560:23–25.

De Reuver M, Sørensen C, Basole RC (2018) The digital platform: A research agenda. J. Inform. Tech. 33(2):124–135.

Delporte CM, Thomas LJ (1977) Lot sizing and sequencing for N products on one facility. Management Sci. 23(10):1070–1079.

Doll CL, Whybark DC (1973) An iterative procedure for the singlemachine multi-product lot scheduling problem. Management Sci. 20(1):50–55.

Edalat N, Tham CK, Xiao W (2012) An auction-based strategy for distributed task allocation in wireless sensor networks. Comput Comm. 35(8):916–928

Fan M, Stallaert J, Whinston AB (2003) Decentralized mechanism design for supply chain organizations using an auction market. Inform. Systems Res. 14(1):1–22.

Firnkorn J, Mu¨ ller M (2011) What will be the environmental effects of new free-floating car-sharing systems? The case of car2go in Ulm. Ecological Econom. 70(8):1519–1528.

Firnkorn J, Mu¨ ller M (2015) Free-floating electric carsharing-fleets in smart cities: The dawning of a post-private car era in urban environments? Environment. Sci. Policy 45:30–40.

Hagiu A, Wright J (2015) Multi-sided platforms. Internat. J. Industrial Organ. 43:162–174.

Hazard CJ, Wurman PR, Andrea RD (2006) Alphabet soup: A testbed for studying resource allocation in multi-vehicle systems. AAAI Workshop on Auction Mechanisms Robot Coordination (AAAI, Washington, DC), vol. 17.

He L, Mak Hy, Rong Y (2019) Operations management of vehicle sharing systems. Hu M, ed. Sharing Economy (Springer Nature, Berlin), 461–484.

Hevner AR, March ST, Park J, Ram S (2004) Design science in infor mation systems research. MIS Quart. 28(1):75–105.

International Grid Control Cooperation (2014) What is control energy? (Prequalification). Regelleistung.net. Accessed June 20, 2023, https:// www.regelleistung.net/en-us/General-info/What-is-control energy-Prequalification

Kahlen MT (2017) Virtual Power Plants of Electric Vehicles in Sustainable Smart Electricity Markets (Erasmus Research Institute of Management, Rotterdam, Netherlands).

Ketter W, Schroer K, Valogianni K (2022) Information systems research for smart sustainable mobility: A framework and call for action. Inform. Systems Res., ePub ahead of print September 19, https://pubsonline.informs.org/doi/abs/10.1287/isre.2022.1167.

Ketter W, Collins J, Gini M, Gupta A, Schrater P (2009) Detecting and forecasting economic regimes in multi-agent automated exchanges. Decision Support Systems 47(4):307–318.

Ketter W, Collins J, Gini M, Gupta A, Schrater P (2012) Real-Time tactical and strategic sales management for intelligent agents guided by economic regimes, Inform, Sustems Res. 23(4):1263-1283.

Lu Y, Gupta A, Ketter W, van Heck E (2016) Exploring bidder heterogene ity in multichannel sequential B2B auctions. MIS Quart. 40(3):645–662.

Lu Y, Gupta A, Ketter W, van Heck E (2019) Dynamic decision making in sequential business-to-business auctions: A structural econometric approach. Management Sci. 65(8):3853–3876.

Mahmassani HS (2016) Technological innovation and the future of urban personal travel. Schofer J, Mahmassani HS, eds. MOBIL-ITY 2050: A Vision for Transportation Infrastructure (Northwestern University Transportation Center, Evanston, IL), 41–62

Mak H, Rong Y, Shen ZM (2013) Infrastructure planning for electric vehicles with battery swapping. Management Sci. 59(7):1557–1575.

Malone TW, Crowston K (1994) The interdisciplinary study of coor dination. ACM Comput. Surveys 26(1):87–119.

Malone TW, Yates J, Benjamin RI (1987) Electronic markets and elec tronic hierarchies. Comm. ACM 30(6):484–497.

Next Kraftwerke (2018) Next Kraftwerke and Jedlix launch initiative to use electric car batteries for grid stability. Accessed June 20, 2023, https://www.next-kraftwerke.com/news/next-kraftwerke-jedlixlaunch-initiative-to-use-electric-car-batteries-for-grid-stability.

Niederhoff JA (2007) Using separable programming to solve the multi-product multiple ex-ante constraint newsvendor problem and extensions. Eur. J. Oper. Res. 176(2):941–955.

Peters M, Saar-Tsechansky M, Ketter W, Williamson SA, Groot P, Heskes T (2018) A scalable preference model for autonomous decision-making. Machine Learn. 107(6):1039–1068.

Rai A (2017) Diversity of design science research. MIS Quart. 41(1):iii–xviii.

Robusto C (1957) The cosine-haversine formula. Amer. Math. Monthly 64(1):38–40.

Schill W (2011) Electric vehicles in imperfect electricity markets: The case of Germany. Energy Policy 39(10):6178–6189.

Schroer K, Ketter W, Lee TY, Gupta A, Kahlen M (2022) Data-driven competitor-aware positioning in on-demand vehicle rental networks. Transportation Sci. 56(1):182–200.

Shneidman J, Ng C, Parkes DC, AuYoung A, Snoeren AC, Vahdat A, Chun B (2005) Why markets could (but don’t currently) solve resource allocation problems in systems. Accessed June

20, 2023, https://www.usenix.org/legacy/event/hotos05/final\_ papers/full\_papers/shneidman/shneidman.pdf.

Sperling D (2015) Between public and private mobility: Examining the rise of technology-enabled transportation services. Technical report, National Academies of Sciences, Washington, DC.

Sperling D (2018) Three Revolutions: Steering Automated, Shared, and Electric Vehicles to a Better Future (Island Press, Washington, DC).

Stro¨bel M (2000) On auctions as the negotiation paradigm of elec tronic markets. Electronic Marketing 10(1):39–44.

Valogianni K, Ketter W, Collins J, Zhdanov D (2014) Enabling sustainable smart homes: An intelligent agent approach. Proc. 35th Internat. Conf. on Inform. Systems (Association of Information Sys tems eLibrary), 1–20.

Vytelingum P, Voice T, Ramchurn S, Rogers A, Jennings N (2011) Theoretical and practical foundations of large-scale agent-based micro-storage in the smart grid. Artificial Intelligence Res. 42: 765–813.

Wooldridge M, Jennings NR (1995) Intelligent agents: Theory and practice. Knowledge Engrg. Rev. 10(2):115–152.

World Health Organization (2005) Health effects of transport-related air pollution. Technical report, World Health Organization, Geneva.

World Health Organization (2018) Global status report on road safety. Technical report, World Health Organization, Geneva.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
