---
otero_id: 15240
otero_key: "RN98AUFA"
title: "Agent-assisted supply chain management: Analysis and lessons learned"
authors: "William Groves; John Collins; Maria Gini; Wolfgang Ketter"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Agent-assisted supply chain management: Analysis and lessons learned

William Groves <sup>a,</sup>⁎, John Collins <sup>a</sup>, Maria Gini <sup>a</sup>, Wolfgang Ketter <sup>b</sup>

<sup>a</sup> Department of Computer Science and Engineering, University of Minnesota, United States

<sup>b</sup> Rotterdam School of Management, Erasmus University, The Netherlands

## a r t i c l e i n f o

Article history: Received 24 September 2012 Received in revised form 29 August 2013 Accepted 16 September 2013 Available online 25 September 2013

Keywords: Decision support systems Supply chain management Key performance indicators Economic simulation Software agents Trading Agent Competition

## a b s t r a c t

This work explores “big data” analysis in the context of supply chain management. Speci<sup>fi</sup>cally we propose the use of agent-based competitive simulation as a tool to develop complex decision making strategies and to stress test them under a variety of market conditions. We propose an extensive set of business key performance indicators (KPIs) and apply them to analyze market dynamics. We present these results through statistics and visualizations. Our testbed is a competitive simulation, the Trading Agent Competition for Supply-Chain Management (TAC SCM), which simulates a one-year product life-cycle where six autonomous agents compete to procure component parts and sell <sup>fi</sup>nished products to customers. The paper provides analysis techniques and insights applicable to other supply chain environments.

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

Supply-chain management is becoming increasingly sophisticated, driven by expectations of greater business agility and more closely coupled processes within as well as across organizations. For example, in smart markets participants have to use computational tools to understand the market characteristics and to anticipate market needs [1]. Central to smart markets are software agents with adjustable autonomy, i.e. programs capable of autonomous or semi-autonomous decision making, which are used to assist humans.

While many supply-chain business transactions are regulated by long-term contracts, it is critical to develop strategies that can anticipate and adapt to changes in the underlying market conditions [2]. Studies based on analytical methods simplify the problems (e.g., a single supplier and a single retailer) for tractability [3] and do not model how adaptive strategies affect market dynamics. Testing adaptive strategies in real-world markets can be risky, making it impossible to do the rigorous experiments needed to understand the interactions between competitors' strategies and the market. Competitive simulation environments, such as the Trading Agent Competition for Supply-Chain Management (TAC SCM), described in Section 3, overcome these obstacles and enable users to perform rigorous evaluation of strategies under varied market conditions. Agent modeling, which is at the core of these simulation environments, is more robust and <sup>fl</sup>exible than centralized strategies based on traditional optimization methods in scenarios that have high complexity and uncertainty [4,5].

This work makes two major contributions. The <sup>fi</sup>rst is to highlight the advantages of using a competitive simulation environment, where software agents compete in a market with other agents, for developing complex decision making strategies. Simulation and serious games are routinely used as educational support for students and professionals. Software agents are capable of playing such games (e.g., [6]) and can <sup>fi</sup>nd good, often optimal, policies, but their use so far has been limited, despite their advantages.

The adoption of agent-based design forces the practitioners to specify precisely the decision processes and enables a thorough exploration of the interactions between competitors' strategies and market conditions. This kind of experimentation can elucidate unexpected, unintended, and undesirable high-level side effects of low-level business decisions. The phenomena we observe in TAC SCM emerge from the interactions among the competing agents and are not inherent in the design of the simulation. Running many simulations with different agents and market conditions is the only way to observe the effects of such interactions.

In TAC SCM, the software agents developed by different research groups are available for others to use. Since those agents use a variety of decision making methods, their availability makes TAC SCM a particularly rich testbed for exploration and assessment of decision strategies. For these reasons we think agent-based simulation will provide great dividends.

The second contribution is an extensive set of automated supplychain key performance indicators (KPIs). Using TAC SCM as a testbed, we show how to compute the KPIs relevant to autonomous supply chains from data for guiding strategic, tactical, and operational decision making.

The paper is organized as follows. We present related literature (Section 2) and introduce TAC SCM (Section 3). We describe brie<sup>fl</sup>y the KPIs (Section 4), followed by the KPIs for procurement (Section 5), production (Section 6), and sales (Section 7). Section 8 provides lessons learned from TAC SCM applicable to real-world supply chains. We conclude with thoughts on how these analysis tools could be applied to other markets.

## 2. Related work

Agent-based systems have long been proposed for managing business complexity (e.g., [7]). They are valuable for Smart Business Networks [8], which extend traditional business processes to systems that are integrated across organizations, where agents are used to support complex managerial decision making. Agent-based experimentation can <sup>fi</sup>nd strategies for traditional operations research situations [4,9]. The advantages over non-agent methods are that agents' strategies are easier to understand due to the use of <sup>fi</sup>rst principles in the design of the decision processes, do not assume a static environment, and are more robust to modeling errors.

The Association for Trading Agent Research (http://tradingagents. org) over the years has promoted the development of competitive agents for a variety of trading environments, including supply-chain management (TAC SCM) [10], price prediction [11], advertising auctions [12], and more. As a result, many teams have developed agents that have competed in the annual competitions and have shared them with the community. For a survey of decision strategies of many agents in the competition, consult [13].

In TAC SCM signi<sup>fi</sup>cant effort has gone into developing methods for agents to predict prices. Several agents use highly tuned prediction models, often based on speci<sup>fi</sup>c features of the market, since price prediction is needed to drive a pro<sup>fi</sup>table sales strategy (e.g., [13,14]). Economic regimes have been used to characterize economic conditions, such as scarcity or oversupply, and to inform both pricing and resource allocation decisions [15,2].

Literature on trading agents in continuous double auction markets [16] provided inspiration on visualizing supply and demand. Visualization is valuable to support human decision making. For example, tools to generate dynamically a graphical presentation of decision processes improve agent-assisted decision-making in the overall supply-chain [17].

This work differs from previous work on TAC SCM because we focus on TAC SCM as a testbed for business automation instead of concentrating on how to develop an agent to win the competition.

While there is much existing literature on supply chain KPIs [18–20] and their analysis [21,22], this paper presents KPIs speci<sup>fi</sup>cally relevant to autonomous supply chain processes. Some conventional KPIs are focused on measuring ef<sup>fi</sup>ciencies of real-world operations that may involve process failures. These kinds of failures (i.e. data entry errors or equipment failures), while important in real-world processes, are already well studied in the literature. This work focuses on aspects of performance due to the oligopoly market, price risk, and supply and demand uncertainty.

## 3. Background on TAC SCM

TAC SCM [10] simulates a one-year product life-cycle in a three-tier supply-chain, with eight parts suppliers, six competing manufacturing agents that produce different models of computers, and many end customers. These agents compete to purchase parts in the procurement market and to sell the <sup>fi</sup>nished goods in the sales market. TAC SCM was inspired by companies such as Dell and Gateway Computer, both using a direct sales model [10].

Several aspects of TAC SCM make it relevant to the study of real supply-chain management systems. The market is an oligopoly of six manufacturers, so agent actions generate strong effects on the market.

The supply and demand stochasticity is tuned to create situations of both excess supply as well as acute shortages. Supply and demand are only indirectly observable by the agents during the simulation, but agents affect each other indirectly through competition in the procurement and sales markets.

An agent must plan proactively: component parts must be ordered far in advance of delivery to minimize costs, but advanced purchases can force later sales that create losses. Sales commitments can only be made close to the delivery date, but the parts for upcoming sales should already be pre-ordered to take advantage of lower prices for long-term orders.

In both sales and procurement, there is uncertainty about which requests will actually be ful<sup>fi</sup>lled due to the competitive actions of the other agents as well as market stochasticity. To handle times when demand exceeds factory capacity, agents can build inventories, but they incur an opportunity cost as the mixture of products built may not be optimal at sales time.

In TAC SCM, all communications are done via explicit market requests and responses. This enables the simulator to capture every interaction and provides a wealth of data that can be used after the simulation to visualize and analyze the activities and decisions of each agent.

Since multiple experiments can use the same set of agents, the same group of agents can be observed operating under different market conditions (e.g., levels of supply and demand), something not possible in real systems. To simplify experimental work and achieve statistical signi<sup>fi</sup>cance with fewer runs, we use a version of the simulation server [23] which supports repeatable pseudo-random sequences of the stochastic market factors. This enables testing of different strategies under repeatable market conditions.

While TAC SCM is not an exact model of any real world market, even the design decisions and hard limits imposed by the simulation are valuable aspects that are present in real markets. Market design properties of the simulation include an oligopoly, no direct observation of competitor behavior, a <sup>fi</sup>xed component to product mapping, and no secondary market for goods. Hard limits include an oligopoly of exactly six agents, a preset simulation time limit, no availability of initial supplies, and lack of value of goods in the inventory at the end of the simulation. Removing those hard limits by randomizing experiments using a range of values would make numerical comparisons across experiments more dif<sup>fi</sup>cult.

These hard limits are inspired by real-world markets and focus the competition on challenging aspects. For example, the oligopoly aspect causes agents to have greater market power when compared to scenarios with many agents, which is a less interesting case. When TAC SCM is adapted to match new market scenarios, these properties can be changed as well. The environmental responses to agent actions were designed to emulate emergent behaviors of real-world markets (i.e. greater demand for a component will drive up its price). A key difference that should not be discounted is the additional transparency made possible by the simulation: real-world market experiments are often impossible to repeat, and being able to measure emergent market phenomena through repeated observation is invaluable.

The TAC SCM simulation server is open source and can be adapted as needed. Most agents are also freely available, as source or binary code, so they can be used as competitors when experimenting with new decision making processes. Also, logs are publicly available from the simulation server.<sup>1</sup>

The main tools for this analysis are based on a SQL database which is populated by the simulation logs.<sup>2</sup> Each experiment run contains over 500,000 messages requiring uncompressed storage of around 100 MB. We use SQL queries against the database to generate plots of data of interest. Our analysis toolkit provides a collection of over <sup>fi</sup>fteen modules constructed to facilitate agent analysis. For more information, please consult the Appendix.

## 4. Key performance indicators and analysis tools

Table 1 provides a set of KPIs relevant to analysis of automated supply chains. Each KPI lists the corresponding section where it is discussed in detail. The KPIs are organized by business module, indicating the role of each in the manufacturing enterprise.

Several KPIs are visible only at speci<sup>fi</sup>c levels of analysis. For this reason many visualizations involve data from individual simulation runs. The individual examples were not cherry-picked for rare elements but are intended to exemplify behaviors emergent in many simulation rounds.

## 5. Procurement

In TAC SCM, each day an agent can make multiple requests on the procurement market for each component, specifying quantities, due dates, and price constraints. Suppliers receive many such requests (RFQs) and must decide both an offer quantity and a unit price, subject to their own production constraints. Prices vary each day due to variations in supplier capacity and the volume of requests made by other agents. Requests to fully committed suppliers have higher per unit costs and may be delayed, while long lead time requests generally have lower costs. Factory capacities vary each day and additional short-term availability can appear at any time. When this happens, short-term requests can be ful<sup>fi</sup>lled at a low cost.

## 5.1. Supply and demand for components

A classic economic analysis is the application of the law of supply and demand depicted in Fig. 1 as two intersecting curves. The supply curve refers to the (usually increasing) marginal cost for supplying a good based on increases in the overall quantity offered. The demand curve refers to the (usually decreasing) marginal price for increases in the quantity demanded.

The plots in Fig. 1 show examples of supply and demand of an individual supply line in TAC SCM at various points in a simulation run. The supply line represents the ascending price-sorted set of component orders made in the last 10 days. The demand line is the descending pricesorted set of requests made on the current day (uncommitted quantities cause the demand line to be strictly wider on the x-axis than the supply line). The shape of the two lines is an indicator of the current market situation. When the lines are <sup>fl</sup>at, this is a tactical indicator that the offered price has been consistent for the recent past. When the lines are nearly perpendicular to each other, as in plot (b), this indicates a dramatic change in prices. The horizontal displacement between the two lines is an indicator of the current request volume. The overall horizontal displacement of the supply line indicates the current total demand for this component. This KPI visualization gives a human observer an intuitive understanding of the current supply market situation for the speci<sup>fi</sup>c component and can be used to validate the behavior of the agent or get insights into the market.

## 5.2. Cost variability of components

Tracking cost volatility for individual components is useful for observing supply shortages. In TAC SCM each product requires four components (CPU, memory, hard disk, motherboard); the CPU is the most expensive.

Agents often base sales on their expected inventories of CPUs and back<sup>fi</sup>ll non-CPU component inventories with short lead time purchases. This may explain the greater volatility for the non-CPU components, visible in Fig. 2. Note that the daily supply market volatility is higher for periods when the agents are not ful<sup>fi</sup>lling all the demand (before day 110 in the example). Volatility is lower for most components later in the simulation.

## 5.3. Purchase order lateness

In TAC SCM the production capacity varies for each component production line daily according to a random walk. The quoted price for each order depends on the ratio of committed capacity to estimated total supply line capacity between the current day and the delivery date. Prices generally increase as the supplier makes more commitments, but prices can move both up and down over time with the daily changes in the supply line capacity. This change affects both the ability of the supplier to ful<sup>fi</sup>ll committed orders (a production shortfall can occur if the capacity decreases over time) and the prices quoted for new requests. Previous commitments are satis<sup>fi</sup>ed in order of delivery date until the daily production is exhausted.

Fig. 3 displays the mean delivery delay for each component and delivery date. In this simulation run, the CPU components are rarely late but deliveries of non-CPU components are up to four days late. This is because agents are more likely to use short-term offers for non-CPU components. These short-term orders cause suppliers to operate at full supply line capacity, so slight reductions in supply line capacity can easily cause overcommitments resulting in late deliveries.

## 5.4. Strategic long and short lead time procurement mixture

Order lead times in the TAC SCM procurement market can extend to the end of the simulation run, which is 220 days from the start. Supplier prices tend to peak in the range of 8–15 days lead time. Agents can make long-term commitments, but if components are not used immediately on delivery, the agent must pay storage costs. Supplier orders also require a 10% down-payment, a signi<sup>fi</sup>cant cost for long lead time orders when interest rates are high. Normally, long-term prices are lower than short term prices, even when down-payment and storage costs are factored in, but long-term contracts are risky because agents may over-commit relative to the actual future demand.

Automated key performance indicators.

<table><tr><td>Level</td><td>Business module</td><td>Name</td><td>§</td><td>Literature reference</td></tr><tr><td>Strategic</td><td>Procurement</td><td>Supply and demand for components</td><td>5.1</td><td>Visualization from [16]; method from [24]</td></tr><tr><td>Strategic</td><td>Procurement</td><td>Cost variability of components</td><td>5.2</td><td>“Price variability” in [25]</td></tr><tr><td>Tactical</td><td>Procurement</td><td>Purchase order lateness</td><td>5.3</td><td>“Percentage of late deliveries” in [26]</td></tr><tr><td>Strategic</td><td>Procurement</td><td>Long/short lead time procurement mix</td><td>5.4</td><td>“Economic order quantity” in [26,27]</td></tr><tr><td>Tactical</td><td>Procurement</td><td>Tactical opportunistic procurement</td><td>5.5</td><td>“Probabilistic pricing” in [13]</td></tr><tr><td>Strategic</td><td>Production</td><td>Daily profit and loss</td><td>6.1</td><td>“Total cost”, “profit” in [28,26]</td></tr><tr><td>Tactical</td><td>Production</td><td>Inventory build-up</td><td>6.2</td><td>“Inventory investment” in [28]</td></tr><tr><td>Operational</td><td>Sales</td><td>Supply and demand for products</td><td>7.1</td><td>Visualization from [16]; method from [24]</td></tr><tr><td>Operational</td><td>Sales</td><td>Ratio of product demand to supply</td><td>7.2</td><td>Market-wide “fill rate” in [28,26]</td></tr><tr><td>Operational</td><td>Sales</td><td>Utilized to available product demand</td><td>7.3</td><td>“Fill rate” in [28,26]</td></tr><tr><td>Operational</td><td>Sales</td><td>Order cycle time</td><td>7.4</td><td>“Customer response time” in [18,28]</td></tr><tr><td>Operational</td><td>Sales</td><td>Product delivery lateness</td><td>7.5</td><td>“Average earliness/lateness of orders” in [28]</td></tr><tr><td>Tactical</td><td>Sales</td><td>Price variability</td><td>7.6</td><td>“Price variability” in [25,21]</td></tr><tr><td>Operational</td><td>Sales</td><td>Bid efficiency</td><td>7.7</td><td>“Bid efficiency” in [29]</td></tr><tr><td>Tactical</td><td>Sales</td><td>Profit margin</td><td>7.8</td><td>“Profit” in [28,26]</td></tr><tr><td>Tactical</td><td>Sales</td><td>Bidding price trends</td><td>7.9</td><td>“Response to changing environments” in [28]; “accuracy of forecasting techniques” in [18]</td></tr></table>

(a) day 4  
![](/api/attachments/RN98AUFA/fulltext/images/de51651a32e834e8a231ec7e309e35824a3c0ae34ac6e61a649b2451ba1eea17.jpg)

(b) day 61  
![](/api/attachments/RN98AUFA/fulltext/images/98c0fa1aeada10b0750ccdb57f3861069c4a3c174e4f3d575f787f0e789bbcda.jpg)

(c) day 118  
![](/api/attachments/RN98AUFA/fulltext/images/d399c7492cd5cfc1e9f3e6773f4fdcd61ddaa55eaa40f822ed2a27ca49be2f45.jpg)

(d) day 214  
![](/api/attachments/RN98AUFA/fulltext/images/91042993e293e8b3aef55cc72ebb318685fac943fb12cdb7a3ad041e6cf161cb.jpg)  
Fig. 1. Supply and demand in the procurement market for component #200 for lead times of 0 to 10 days from supplier Basus in tournament round tac01-#3454.

Computing long- and short-term procurement mixtures has been previously studied [30]. Finding the right mixture requires the ability to make dynamic adjustments, and it is also an important decision in real supply-chain systems. For instance, Hewlett Packard balances the long- and short-term procurement of parts for consumer printers [27]. A similar approach can be applied to other consumer goods markets.

For classi<sup>fi</sup>cation purposes, in TAC SCM we de<sup>fi</sup>ne short-term as a procurement order with a lead time of less than 10 days, initial procurement as a procurement initiated within the <sup>fi</sup>rst 10 days of the simulation run, and long-term as the remaining unclassi<sup>fi</sup>ed requests. This classi<sup>fi</sup>cation is to separate prede<sup>fi</sup>ned procurement schedules (initial) from market condition motivated (long-term) requests. Short-term requests may be either to ful<sup>fi</sup>ll sales over-commitments or to exploit low prices. Fig. 4 shows how the procurement mixture has varied for the top performing agents over the years of the competition. The proportion of initial procurement has increased steadily as agents have become more sophisticated. We suggest that this increase is a consequence rather than a cause of good agent performance.

## 5.5. Tactical opportunistic procurement

The general price trend in the procurement market is for high shortterm prices with price decreasing as lead time increases. This general trend, shown as “normal” in Fig. 5, is almost universal at the beginning of each simulation run. However, there are periods when the price trend is “inverted,” i.e. the short-term price is below the long-term price. These inversions occur when a supplier has had an unexpected increase in its manufacturing capacity.

![](/api/attachments/RN98AUFA/fulltext/images/079af556640519dcb56b986838aaa705a4cdbe5b98ec72d48096a03b9f51f1f1.jpg)

![](/api/attachments/RN98AUFA/fulltext/images/5656bba652cc48a3241280a642dae84e8c36c58eea347d66b2e6a6a6ff94a874.jpg)  
Fig. 2. Daily volatility for the mean price of components with lead time 6 for simulation run tac02-#3183. The volatility is measured as standard deviation of observed unit prices within a 10-day window for each component line

![](/api/attachments/RN98AUFA/fulltext/images/0abd58dc6c5f41fbc13f64587d87fa3d4cd88aadf603efb70893ecde5df54e23.jpg)

![](/api/attachments/RN98AUFA/fulltext/images/38701eb1d9978928b325cb15e19e80f3817682550217fc4572306f1297e5fe42.jpg)  
Fig. 3. Purchase order lateness time series for each component type in experiment tac02-#3183. The CPU component lines are shown in the upper plot, while the non-CPU component lines are in the lower plot.

In TAC SCM, agents can observe prices only by issuing RFQs to suppliers, but the competition limits the number of RFQs an agent can issue each day. Some of the available RFQs can be used not only to query suppliers for prices but also for opportunistic procurement, i.e. buy a part when it is signi<sup>fi</sup>cantly below the predicted price. These opportunities occur infrequently, due to short-term variations in supplier capacity, and often vanish in the next bidding cycle. Opportunistic procurement is applicable in other domains where spot market prices may be especially low.

We use this opportunistic strategy in our agent, MinneTAC [13], which consistently makes low quantity requests at a low reserve price (20% or more below the predicted price). The result of this strategy can be seen in Fig. 6, which shows prices for a single component type. The y-axis values are normalized to the mean price estimate on each day. The agent makes opportunistic requests when it is not very interested in acquiring parts. Usually this is unsuccessful, as we see by the price quotes labeled “Price Observation Events” However, when the bid succeeds the agent receives offers at low prices.

## 6. Production

In TAC SCM agents produce 16 product types, segmented into highend, medium-end, and low-end products. On each day, an agent must decide which product types to build, depending on its own inventories and factory capacity. An agent can sell products faster than its factory can produce, but, since the overall demand is often lower than the aggregate factory capacity of all the agents, to maximize pro<sup>fi</sup>t each agent has to plan what to produce.

![](/api/attachments/RN98AUFA/fulltext/images/8492bd070c0e7899250126c3b9321b73068ba4d3b28ecd73157c6154ffe74357.jpg)  
Fig. 4. Variation in the mean mixtures of initial (time unit ≤ 10), short term (time unit N 10 and lead time b 10), and long-term (time unit N 10 and lead time ≥ 10) procurement for the top 3 agents in TAC SCM. The y-axis represents the total volume of each type in a simulation run. The error bars show one standard deviation from the mean

## 6.1. Daily profit and loss

Aggregate measures, such as daily pro<sup>fi</sup>t and loss, can be used to discover areas that deserve further analysis. For example, Fig. 7 enables us to discover when agents spend the most and make the most pro<sup>fi</sup>t. Agents that perform well tend to spend more at the beginning than the weaker agents, and they tend to achieve consistently pro<sup>fi</sup>table days earlier than their opponents. In this case, TacTex took large losses around day 80 and unusually high pro<sup>fi</sup>ts around day 170. This is evidence of strategic behavior (see Section 6.2).

## 6.2. Inventory build-up

If an agent predicts signi<sup>fi</sup>cant pro<sup>fi</sup>t opportunities ahead, it may decide to build inventory in preparation for an aggressive selling period.

Fig. 8 shows a steady increase in demand over time (plotted is onesixth of the global demand) and a concurrent inventory buildup for agent TacTex, starting around day 140. The agent is able to increase its pro<sup>fi</sup>t by reducing sales until the sales price peaks around day 170 when it begins selling aggressively. This can be observed through the

![](/api/attachments/RN98AUFA/fulltext/images/cd904964667261348ff01bae686ffc9ec61d78f1c44c635b25dd7c11470bc7a8.jpg)  
Fig. 5. Set of common price vs. lead time relationships for individual components. Series observed in experiment tac02-#2069 for component 100 on days 20 (Normal), 67 (Inversion A), and 118 (Inversion B). The speci<sup>fi</sup>c values are not important, but illustrate common scenarios that agents can face in procurement

![](/api/attachments/RN98AUFA/fulltext/images/69c63a948ecdb90f7123897c3be1c3d157cd59f0bf4cc9b2e67e7f483aff21eb.jpg)  
Fig. 6. Opportunistic procurement events for MinneTAC plotted in proportion to agent's price estimate during experiment tac02-#2069. The y-axis values are normalized, 1.0 corresponds to the price estimate for each day. The remaining series are normalized by this value. The red line is the agent's current reserve price used in opportunistic procurement requests relative to the price estimate.

![](/api/attachments/RN98AUFA/fulltext/images/9d0d8665982849e2f23a162cde020ffc922f3d7f7d922da8db386f7d9e166dec.jpg)  
Fig. 7. Smoothed daily agent pro<sup>fi</sup>t and loss for experiment tac01-#3454. The top two scoring agents, TacTex and DeepMaize, are highlighted with thicker lines. DeepMaize experiences more consistent mean pro<sup>fi</sup>ts than the other agents.

sales velocity series which shows the number of units sold each day. The agent's procurement can be observed through the agent procurement impulses. Days with non-zero quantity procurement deliveries are shown with the height representing the total quantity. The agent's running inventory is also plotted. Manufacturers holding large inventories are well prepared for shocks in either supply or demand, but they incur additional storage costs. Lowering inventories can improve ef<sup>fi</sup>ciency but can increase the risk of overcommitment. Fig. 9 compares product and component inventories across agents. Inventories are biased almost exclusively towards components with low <sup>fi</sup>nished goods inventories. Spikes in the graph are caused by large deliveries.

## 7. Sales

In TAC SCM customers issue requests for quotes (RFQs) each day for the products they wish to buy, specifying model, quantity, delivery date, and maximum (reserve) price they are willing to pay. The longest lead time in this market is 12 days. Each agent must decide whether to bid on customer RFQs and at what price. Customers choose the lowest price bid. Customer demand varies from day to day independently in each of the market segments.

## 7.1. Supply and demand for finished products

Agents have a different cost basis for each product, different limits on their desired overall quantity to sell, and differing contention for factory capacity. We expect them to vary the amount and price offered for each request to achieve consistent sales quantities. In reality, the shape of supply in the sales market is entirely different: many agents quote a single price for each product regardless of RFQ parameters such as quantity or lead time.

![](/api/attachments/RN98AUFA/fulltext/images/9e17793465028431725947856c17584a59da3b9c347738d240a7085c94f13fbd.jpg)  
Timeunit (date on which components arrive or depart)  
Fig. 8. Component inventory, supply velocity, and sales velocity for agent TacTex for component 110 in tac01-#3454. As product demand increases (becomes more negative), the agent reduces sales velocity and increases procurement velocity. When the demand exceeds some threshold, the agent increases sales velocity as the per-unit price peaks.

![](/api/attachments/RN98AUFA/fulltext/images/d4e748c6b34c865aedeaf154a980cd020fd6bb6d16624ee22d4472fcbd8c04bc.jpg)  
Fig. 9. Component (positive), product (negative) inventories of tac02-#3183.

Early in the product life-cycle, components are scarce and expensive. Fig. 10 (a) shows a situation when agents are bidding only on the portion of demand above some price threshold. Later in the simulation the entire available demand is satis<sup>fi</sup>ed. Fig. 10 (b) shows what happens when agents bid the same price on all demand. One agent wins all the demand for a product on that day, and the second lowest price agent loses by just a few dollars. This is undesirable because an agent rarely has the capacity to serve 100% of the demand for any product. Randomizing offer prices achieves slightly more consistent sales volume and hence reduces daily order quantity volatility.

## 7.2. Ratio of product demand to supply

Another important KPI is the ratio between requested demand and total available supply. In TAC SCM often there is suf<sup>fi</sup>cient component supply to ful<sup>fi</sup>ll the demand, but at times some components are in short supply relative to the demand. The ratio of the total number of demand for a component type to its available supply for an entire game is shown for all component types in Table 2. Numbers in italics indicate a shortage.

## 7.3. Utilized to available product demand

Fig. 11 shows the shortfall of <sup>fi</sup>nished goods with respect to the demand, i.e. the amount of delivered units divided by the number of demanded units for each market segment. Early in the simulation not all the demand is satis<sup>fi</sup>ed, either because of supply shortages or because the reserve price is below the cost of components, but the demand is often completely satis<sup>fi</sup>ed as the product reaches the maintenance and extinction phases of the life cycle.

## 7.4. Order cycle time

The observed cycle time of orders, i.e. the time between a customer request and the <sup>fi</sup>nal delivery, re<sup>fl</sup>ects several tactical and strategic aspects.

Fig. 12 shows the committed orders each day, aggregated by mean order lead time and by mean delivery lead time. Some agents (TacTex and MinneTAC) ful<sup>fi</sup>ll orders as quickly as possible by shipping all the day after the order. This keeps storage costs down. The strategy of agents that ship closer to the due date more likely involves a just-intime procurement and production approach to avoid inventories of <sup>fi</sup>nished goods. It is notable that all agents often ship signi<sup>fi</sup>cantly before an order's due date. Fig. 12 shows the observed cycle time for each agent which may vary greatly.

## 7.5. Product delivery lateness

Agents have an incentive to ful<sup>fi</sup>ll sales commitments early if inventories are available to save storage costs. Between the earliest possible ful<sup>fi</sup>llment and the latest non-late ful<sup>fi</sup>llment (due date speci<sup>fi</sup>ed in the sale), there is often a large range of days for agents to deliver. Delivery lateness can be measured for a sales order by computing the difference between the requested delivery date and the date of ful<sup>fi</sup>llment. Fig. 13 shows the mean delivery lateness percentile for each agent and delivery date. As a post-hoc analysis, this can show an agent's willingness for (probabilistic) overcommitments.

## 7.6. Price variability

Sales market prices tend to vary differently depending on the level of competition. When the agents satisfy all demand, the observed mean prices for individual products become much more volatile.

This is observed in Fig. 14, where the normalized daily volatility for many products increases after day 120. This can occur because individual agents become more aggressive at lowering prices in order to sell surplus products. This increased price variability relates to observations about unful<sup>fi</sup>lled daily demand which was discussed in Section 7.3.

## 7.7. Bid efficiency

Bid ef<sup>fi</sup>ciency is de<sup>fi</sup>ned [29] as the ratio of the per unit price of the winning bid divided by the second lowest bid, or by the reserve price if there was no other bid. Measuring bid ef<sup>fi</sup>ciency is a valuable KPI because it is an indicator of how far agent pricing is from the optimal.

(a) day 4  
![](/api/attachments/RN98AUFA/fulltext/images/12cbc4b9725ca81cc7fb79d7cf309624110e7850826b10dfe45827f376f71a9d.jpg)

(b) day 89  
![](/api/attachments/RN98AUFA/fulltext/images/7462701b4b431b7ca8cfc506126995a235a76a3b6ddba71f4689b64b63cbc035.jpg)  
Fig. 10. Supply and demand for product #8 in experiment tac01-#3454. The demand line corresponds to the total market demand for that day, sorted by decreasing reserve price. The dotted lines correspond to each agent's offers (the y-axis value indicates the offer price). The agent with the lowest offer price for a given request will receive the order. Note that the right graph contains data from only 3 agents because no other agent made offers for this product on this day

Table 2  
Ratio of demand to capacity for component parts in game tac02-#3183.

<table><tr><td>Component</td><td>100</td><td>101</td><td>110</td><td>111</td><td>200</td><td>210</td><td>300</td><td>301</td><td>400</td><td>401</td></tr><tr><td>Ratio</td><td>1.184</td><td>0.847</td><td>0.892</td><td>1.048</td><td>1.019</td><td>0.984</td><td>0.841</td><td>0.761</td><td>1.112</td><td>1.077</td></tr></table>

Recall that in TAC SCM, a <sup>fi</sup>rst price auction is run independently for each customer request. Each request is visible to all agents, but settlement prices are not visible to other agents. Agents can increase price observability by spreading individual offer prices probabilistically about the predicted settlement price. Strong agents have generally high bid ef<sup>fi</sup>ciency, as shown in Table 3.

## 7.8. Profit margin

Pro<sup>fi</sup>t margin (computed as pro<sup>fi</sup>t/revenue) is a frequently used KPI to determine if a business venture is worth undertaking. In TAC SCM, agents are ranked according to their total pro<sup>fi</sup>t across multiple simulations. So, it is worth examining pro<sup>fi</sup>t margin to compare strategy performance.

Pro<sup>fi</sup>t margins for the 2010 tournament are shown in Table 4. Margin can be easily computed for an entire simulation, but it is dif<sup>fi</sup>cult to determine the margin for individual days because choices, such as long lead time component purchases, can affect pro<sup>fi</sup>t for multiple days. The agent with the highest pro<sup>fi</sup>t margin is often the winner of the overall tournament.

## 7.9. Bidding price trends

Agents that bid only within a small range of the previous day's price are considered price followers. In Fig. 15, this corresponds to bids near zero on the y-axis. Price following is a safe strategy to maximize pro<sup>fi</sup>t for individual winning bids. However, agents can attempt to move prices by taking risks and bidding far from the previous day's price.

In Fig. 15 we can see cases where agents are clearly attempting to drive prices either down (DeepMaize [13] between days 80 and 100) or up (TacTex [14] around day 130). This is shown by winning bids that are far from the zero value on the y-axis. The effect can be seen in the daily pro<sup>fi</sup>tability shown earlier in Fig. 7. In general, the product price change over one day is small (less than a 1% change in price). The <sup>fi</sup>gure shows that many bids are very close to the previous day mean price, but the bids far from the previous day's value can presage shifts in the mean sales price.

## 8. Lessons learned for real supply chains

There are several major lessons from our study that support the value of competitive simulations of supply chains for real-world supply chains.

## 8.1. Exploration of supply chain strategies

Measuring and assessing business agility in the real world can be risky. Environments such as TAC SCM can facilitate this measurement safely by simulating different market situations by varying, for instance, the competitors, initial conditions, or market mechanics. The collection of publicly available competitive agents (available from the public TAC SCM agent repository) is a major asset for such experimentation and exists only because of the competition.

## 8.2. Availability of a rich set of market data

The market data generated through years of TAC SCM simulation supports multiple types of analysis. These data are valuable because they contain a complete and detailed set of all actions (N500,000 messages) taken by all agents. This level of detail would be prohibitively expensive and typically not obtainable in real world markets.

The ability to study operations in a partially observable environment (while having a complete view in post-hoc analysis) is a fundamental contribution of TAC SCM. Agents' behaviors in TAC SCM have changed over several tournament years. For example, overall reliance on longterm procurement has increased while pro<sup>fi</sup>t margins have decreased. Manufacturers make long-term decisions that are usually pro<sup>fi</sup>table but increase risk due to future demand uncertainty. This can occur in real world markets from service industries, such as airlines, to manufacturing, such as consumer electronics.

## 8.3. Study of different types of risk and ways to mitigate them

Risk in TAC SCM, just as in real-life supply chains, comes in several forms, such as sales price and quantity, supply price and quantity, and supply lateness risk. Supply risks can be reduced by committing to component orders far in advance; but this still leaves an agent exposed to

![](/api/attachments/RN98AUFA/fulltext/images/2a71fcd40752e8161c3cfb0ce90b112a6df57d98cfa2cffbd19c72a68b67fe2f.jpg)  
Fig. 11. Utilized demand per market segment for simulation run tac02-#3183.

![](/api/attachments/RN98AUFA/fulltext/images/10ac2d6fd74045dc2017e0784614618b0f824dc1d4bb20202c19bf6b569c9143.jpg)  
Fig. 12. Mean sales delivery time for selected agents in experiment tac02-#3183

the risk of late deliveries from suppliers (Section 5.3). This risk can be mitigated by planning a minimum safety stock, but this can introduce additional costs. Increased competition between agents has caused higher (and greater variance in) prices. To mitigate these effects, agents have increased the levels of initial procurement to lock-in low prices and reduce dependence on short-term orders (Section 5.4). In sales, agents often bid on more requests than they can ful<sup>fi</sup>ll on average in order to probabilistically ensure suf<sup>fi</sup>cient orders. Overcommitment risk can be reduced by improving price predictions or bid ef<sup>fi</sup>ciency (Section 7.7).

## 8.4. Relevant KPIs and visualizations

The set of KPIs (Table 1) is, to our knowledge, the most complete set of KPIs focused on autonomous supply-chain management in the literature. The visualizations shown for TAC SCM can be similarly applied to real-world markets to facilitate meaningful tactical and strategic analysis. Some KPIs bene<sup>fi</sup>t from the complete observability provided by the simulation logs (for example, utilized to available product demand) so a sampling-based approach may be necessary to obtain all necessary observables. Given that production and sales data are increasingly available to businesses, this kind of tactical analysis is feasible.

![](/api/attachments/RN98AUFA/fulltext/images/ad4959d5ee70d3f5433439f1054cdbf50552348434a05507936513392d5c4c9e.jpg)  
Fig. 13. Delivery by percentile for selected agents in experiment tac02-#3183. A delivery the day after the sale is made corresponds to 100% on the graph. A delivery at the due dat corresponds to 0% on the graph. This visualization can be used as a barometer for the level of commitment each agent is experiencing.

![](/api/attachments/RN98AUFA/fulltext/images/54ec38f9869b6f1301024e2bb4bc657b7687f02ee2daad91bc165b58e6ce2a33.jpg)  
Fig. 14. Customer market normalized mean daily sales price volatility (1 day volatility) by market segment (low, med, high) in experiment tac02-#3183

Table 4  
Table 3  
Bid ef<sup>fi</sup>ciency per agent ordered by 2010 <sup>fi</sup>nal tournament rank.

<table><tr><td>Rank</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Agent</td><td>TacTex</td><td>DeepMaize</td><td>MinneTAC</td><td>Botticelli</td><td>Nanda</td><td>Mertacor</td></tr><tr><td>Bid efficiency</td><td>97.6%</td><td>98.0%</td><td>98.2%</td><td>97.4%</td><td>97.6%</td><td>97.0%</td></tr></table>

## 9. Conclusions and future work

When automating business processes, designers should be concerned with business agility and particularly with how the automated process will respond to situations where the standard assumptions of the market may be violated. The KPIs we present facilitate this process by providing characteristics to measure across the automated supply chain, and realistic simulation techniques (of which TAC SCM is an example) provide rich data sets over which to accurately measure behavior in different situations. Although TAC SCM may not match a particular real-world market scenario, these tools can provide valuable insights. For simulated scenarios, realism requires complexity.

Since the TAC SCM server is open-source, the simulation can be modi<sup>fi</sup>ed to suit a different supply chain. Changes that could be made easily include: varying the number of agents, number of components, product composition, number of simulation days to include very longterm (i.e. years) interactions, and changes to the demand to include seasonality. Another future modi<sup>fi</sup>cation is the creation of a mixedinitiative TAC SCM server with a human decision maker in the loop [31].

## Appendix A. Database storage and querying of simulation data

The tools that facilitate our analysis are based on a SQL database that is populated by the simulation logs. The package including the mechanism to populate the database and a wide range of visualization modules (including many used in this paper) are released as a tool for further research. To illustrate the power and expressiveness of this tool for further analysis, the sequence of two queries used to generate Fig. 11 is provided below:

## 1 Match each RFQ with any corresponding offers from agents

CREATE TABLE IF NOT EXISTS tmpcustrfqoffer AS

SELECT rfqs.simid AS simid, rfqs.timeunit AS timeunit, rfqs.sender AS sender, offers.sender AS receiver, rfqs.id AS rfqid, offers.id AS o<sub>fi</sub>d, rfqs.product AS product, rfqs.quantity AS rfqquantity, offers.quantity AS ofquantity,

offers.unitprice AS unitprice, rfqs.duedate AS rfqduedate, offers.duedate AS duedate, rfqs.penalty AS penalty, rfqs.reservePrice AS reservePrice

Pro<sup>fi</sup>t and pro<sup>fi</sup>t margin for 2010 tournament agents ordered by rank.

<table><tr><td>Agent</td><td>Rank</td><td>Revenue</td><td>Profit</td><td>Profit margin</td><td>σ (Profit margin)</td></tr><tr><td>TacTex</td><td>1</td><td>$107,796,862</td><td>$9,093,964</td><td>7.60%</td><td>7.39%</td></tr><tr><td>DeepMaize</td><td>2</td><td>$94,038,608</td><td>$6,519,828</td><td>6.05%</td><td>5.95%</td></tr><tr><td>MinneTAC</td><td>3</td><td>$74,029,046</td><td>$1,658,958</td><td>1.72%</td><td>7.18%</td></tr><tr><td>Botticelli</td><td>4</td><td>$95,897,236</td><td>-$2,061,129</td><td>-2.48%</td><td>5.17%</td></tr><tr><td>Nanda</td><td>5</td><td>$81,871,999</td><td>-$3,498,945</td><td>-4.91%</td><td>7.52%</td></tr><tr><td>Mertacor</td><td>6</td><td>$86,614,341</td><td>-$5,467,102</td><td>-8.48%</td><td>17.44%</td></tr></table>

![](/api/attachments/RN98AUFA/fulltext/images/abab1bf51067f5d1094e04569cc72f2c0bc4ab6d1938598341eace55c0bb18d2.jpg)  
Fig. 15. Bidding price trends for top 3 agents for product 8 in experiment tac02-#2069. Each point along an agent's series denotes an instance when the agent placed a winning bid (all winning bids for the selected agents are shown, bids of other agents are omitted for clarity). The y-axis value denotes the difference between the agent's bid price and the previous day mean winning bid price. Since daily price changes are small, the previous day's mean price is a good estimate of the current day's price.

FROM (SELECT \* FROM rfqs WHERE rfqs.sender <sub>=</sub> 9 AND rfqs.receiver <sub>=</sub> -1) AS rfqs INNER JOIN offers ON rfqs. sender <sub>=</sub> offers.receiver AND rfqs.id <sub>=</sub> offers.rfq AND (rfqs.timeunit) <sub>=</sub> offers.timeunit AND rfqs.simid <sub>=</sub> offers.simid

## 2 Match each accepted sales order with a corresponding row from Query 1

SELECT o.simid AS simid, o.timeunit AS timeunit, o.rfqduedate AS rfqduedate, o.duedate AS duedate, o.penalty as penalty, o.duedate-o.timeunit AS leadtime, o.product AS product, o.rfqquantity AS rfqquantity, o.ofquantity AS ofquantity, o.unitprice AS unitprice, o.sender AS sender, o.receiver AS receiver, o.rfqid AS rfqid, o.o<sub>fi</sub>d AS o<sub>fi</sub>d, r.id AS orid FROM tmpcustrfqoffer o LEFT OUTER JOIN orders r ON o.simid <sub>=</sub> r.simid AND o.timeunit + 1 <sub>=</sub> r.timeunit AND o.sender =

r.sender AND o.receiver <sub>=</sub> r.receiver AND o.o<sub>fi</sub>d <sub>=</sub> r.offer

## References

[1] M. Bichler, A. Gupta, W. Ketter, Designing smart markets, Information Systems Research 21 (4) (2010) 688–699.

[2] W. Ketter, J. Collins, M.L. Gini, A. Gupta, P.R. Schrater, Real-time tactical and strategic sales management for intelligent agents guided by economic regimes, Information Systems Research 23 (4) (2012) 1263–1283

[3] K. Kogan, C.S. Tapiero, Supply Chain Games: Operations Management and Risk Valuation, International Series in Operations Research & Management Science, Springer, 2010.

[4] M. Fan, J. Stallaert, A.B. Whinston, Decentralized mechanism design for supply chain organizations using an auction market, Information Systems Research 14 (1) (2003) 1–22.

[5] W. Ketter, J. Srour, Optimal or agile? Tradeoffs between optimization and agent based methods, INFORMS ORMS Today 36 (2) (2009) 22–25.

[6] S. Kimbrough, D. Wu, F. Zhong, Computers play the beer game: can arti<sup>fi</sup>cial agents manage supply chains? Decision Support Systems 33 (3) (2002) 323–333.

[7] M.J. North, C.M. Macal, Managing Business Complexity, Oxford University Press, USA, 2007.

[8] E. van Heck, P. Vervest, Smart business networks: how the network wins, Communications of the ACM 50 (6) (2007) 28–37.

[9] W. Walsh, M. Wellman, Decentralized supply chain formation: a market protocol and competitive equilibrium analysis, Journal of Arti<sup>fi</sup>cial Intelligence Research (JAIR) 19 (2003) 513–567.

[10] J. Collins, W. Ketter, N. Sadeh, Pushing the limits of rational agents: the trading agent competition for supply chain management, AI Magazine 31 (2) (2010) 63–80.

[11] D. Pardoe, P. Stone, The 2007 TAC SCM prediction challenge, in: W. Ketter, H.L. Poutré, N. Sadeh, O. Shehory, W. Walsh (Eds.), Agent-Mediated Electronic Commerce and Trading Agent Design and Analysis, Vol. 44 of LNBIPSpringer, 2010, pp. 175–189.

[12] P.R. Jordan, M.P. Wellman, Designing an ad auctions game for the trading agent competition, in: E. David, E. Gerding, D. Sarne, O. Shehory (Eds.), Agent-Mediated Electronic Commerce, Vol. 59 of LNBIPSpringer, 2010, pp. 147–162.

[13] J. Collins, W. Ketter, M. Gini, Flexible decision control in an autonomous trading agent, Electronic Research Commerce and Applications 8 (2) (2009) 91–105.

[14] D. Pardoe, P. Stone, An autonomous agent for supply chain management, in: G. Adomavicius, A. Gupta (Eds.), Handbooks in Information Systems Series: Business Computing, Elsevier, 2007, pp. 141–172.

[15] W. Ketter, J. Collins, M. Gini, A. Gupta, P. Schrater, Detecting and forecasting economic regimes in multi-agent automated exchanges, Decision Support Systems 47 (4) (2009) 307–318.

[16] D. Cliff, Minimal-intelligence agents for bargaining behaviors in market-based environments, Tech. Rep., HP Labs, 1997.

[17] J. Collins, W. Ketter, M. Gini, Flexible decision support in dynamic interorganizational networks, European Journal of Information Systems 19 (3) (2010) 436–448.

[18] A. Gunasekaran, C. Patel, E. Tirtiroglu, Performance measures and metrics in a supply chain environment, International Journal of Operations & Production Management 21 (1/2) (2001) 71–87.

[19] M. Christopher, Logistics and Supply Chain Management: Creating Value-Adding Networks, Pearson Education 2005.

[20] J. Kleijnen, M. Smits, Performance metrics in supply chain management, Operational Research Society (2003) 507–514

[21] B. Chae, Developing key performance indicators for supply chain: an industry perspective, Supply Chain Management 14 (6) (2009) 422–428.

[22] J. Cai, X. Liu, Z. Xiao, J. Liu, Improving supply chain performance management: a systematic approach to analyzing iterative KPI accomplishment, Decision Support Systems 46 (2) (2009) 512–521.

[23] E. Sodomka, J. Collins, M. Gini, Ef<sup>fi</sup>cient statistical methods for evaluating trading agent performance, Proc. of the Twenty-Second National Conference on Arti<sup>fi</sup>cial Intelligence, 2007, pp. 770–775.

[24] W. Groves, J. Collins, W. Ketter, M. Gini, Analyzing market interactions in a multi-agent supply chain environment, in: R. Sharman, H.R. Rao, T.S. Raghu (Eds.), Exploring the Grand Challenges for Next Generation E-Business, Vol. 52 of LNBIP Springer, 2010, pp. 44–58.

[25] P. Trkman, K. McCormack, Supply chain risk in turbulent environments—a conceptual model for managing supply chain network risk, International Journal of Production Economics 119 (2) (2009) 247–258.

[26] C. Shepherd, H. Günter, Measuring supply chain performance, International Journal of Productivity and Performance Management 55 (3/4) (2006) 242-258

[27] V. Nagali, J. Hwang, D.S.M. Gaskins, M. Pridgen, T. Thurston, P. Mackenroth, D. Branvold, P. Scholler, G. Shoemaker, Procurement risk management at Hewlett-Packard, Interfaces 38 (1) (2008) 51–60.

[28] B.M. Beamon, Measuring supply chain performance, International Journal of Operations & Production Management 19 (3) (1999) 275–292.

[29] P.R. Jordan, C. Kiekintveld, J. Miller, M.P. Wellman, Market ef<sup>fi</sup>ciency, sales competition, and the bullwhip effect in the TAC SCM tournaments, Workshop on Trading Agent Design and Analysis, 2006, pp. 99–111.

[30] C. Kiekintveld, J. Miller, P.R. Jordan, M.P. Wellman, Controlling a supply chain agent using value-based decomposition, Proc. of 7th ACM Conf. on Electronic Commerce, 2006, pp. 208–217.

[31] N.M. Sadeh, D.W. Hildum, D. Kjenstad, A. Tseng, Mascot: an agent-based architecture for dynamic supply chain creation and coordination, Production Planning and Control 12 (3) (2001) 212–223.

William Groves is a Ph.D. Candidate in Computer Science at the University of Minnesota. His articles have appeared in Computer Science conferences such as the International Joint Conference in Arti<sup>fi</sup>cial Intelligence (IJCAI) and the Autonomous Agents and Multi Agent Systems (AAMAS) conference. His current research interests include techniques for improving prediction performance in airline ticket price prediction and supply chains as well as visualization in “big data” domains

John Collins is a lecturer in Computer Science at the University of Minnesota. He has over 30 years of industry experience in product development, research, and consulting. Since 2002 he has been in academia, focused on trading agents and economic reasoning. From 2002 to 2009 he directed the University's Professional Masters program in Software Engineering. He has been involved in the Trading Agent Competition for Supply-Chain Management (TAC SCM) from its inception in 2003. He led a major revision of the speci <sup>fi</sup>cation in 2004 and 2005, served as Game Master for two years, chaired the 2007 TADA workshop, and is currently Operations Chair for TAC SCM, managing the competition infrastructure and user support. He serves on the Board of Directors of the Association for Trading Agent Research, and is an area editor for Electronic Commerce Research and Applications.

Wolfgang Ketter is an Associate Professor in the Department of Decision and Information Sciences at the Rotterdam School of Management at Erasmus University. He received his Ph.D. in Computer Science from the University of Minnesota in 2007. He founded and runs the Learning Agents Research Group at Erasmus (LARGE). The primary objective of LARGE is to research, develop, and apply autonomous and mixed-initiative intelligent agent systems to support human decision making in the area of business networks, electronic markets, and supply-chain management. He co-chaired the TADA workshop at AAAI 2008, was general chair of TAC 2009, and is member of the board of directors of the Association for Trading Agent Research since 2009. He is program co-chair of the International Conference of Electronic Commerce 2011. His research has been published in various information systems, and computer science journals such as AI Magazine, Decision Support Systems, Electronic Commerce Research and Applications, INFORMS OR/MS Today, and International Journal of Electronic Commerce. He serves on the editorial board of Electronic Commerce Research and Applications.

Maria Gini is a Professor at the Department of Computer Science and Engineering of the University of Minnesota. Her work has included coordinated behaviors among robots and in multi-agent systems, learning of opponent behaviors, and autonomous economic agents. She has coauthored over 200 technical papers. She is currently the chair of ACM Special Interest Group on Arti<sup>fi</sup>cial Intelligence (SIGART), and a member of the board of the International Foundation of Autonomous Agents and Multi-Agent Systems. She is on the editorial board of numerous journals, including the Journal of Autonomous Agents & Multi-Agent Systems, Electronic Commerce Research and Applications, Web Intelligence and Agent Systems, Autonomous Robots, and Integrated Computer-Aided Engineering She is a Fellow of the Association for the Advancement of Arti<sup>fi</sup>cial Intelligence and an ACM Distinguished Scientist.
