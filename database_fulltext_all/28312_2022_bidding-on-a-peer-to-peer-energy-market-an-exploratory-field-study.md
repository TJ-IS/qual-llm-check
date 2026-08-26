---
otero_id: 28312
otero_key: "4JY2ANWN"
title: "Bidding on a Peer-to-Peer Energy Market: An Exploratory Field Study"
authors: "Anselma Wörner; Verena Tiefenbeck; Felix Wortmann; Arne Meeuw; Liliane Ableitner; Elgar Fleisch; Inês Azevedo"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1098"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bidding on a Peer-to-Peer Energy Market: An Exploratory Field Study

Anselma Worner,¨ <sup>a,</sup>\* Verena Tiefenbeck,<sup>a,b</sup> Felix Wortmann,<sup>c</sup> Arne Meeuw,<sup>c</sup> Liliane Ableitner,<sup>a</sup> Elgar Fleisch,<sup>a,c</sup> Ines Azevedoˆ <sup>d</sup>

<sup>a</sup> ETH Zurich, 8092 Zurich, Switzerland; <sup>b</sup> University of Nuremberg, 91054 Erlangen, Germany; <sup>c</sup> University of St. Gallen, 9000 St. Gallen, Switzerland; <sup>d</sup> Stanford University, Stanford, California 94305

\*Corresponding author

Contact: awoerner@ethz.ch, https://orcid.org/0000-0003-3369-6334 (AW); verena.tiefenbeck@fau.de, https://orcid.org/0000-0001-8827-5575 (VT); felix.wortmann@unisg.ch (FW); arne.meeuw@unisg.ch (AM); lableitner@ethz.ch (LA); elgar.<sup>fl</sup>eisch@unisg.ch (EF); iazevedo@stanford.edu (IA)

Received: July 8, 2020 Revised: March 9, 2021; September 17, 2021; December 6, 2021 Accepted: December 8, 2021 Published Online in Articles in Advance: June 9, 2022

https://doi.org/10.1287/isre.2021.1098

Copyright: © 2022 The Author(s)

Abstract. Moving toward sustainable energy systems to address climate change is one of the key challenges of our generation. To that end, investments in renewable energy and balancing renewable supply and energy demand on the larger scale are crucial. One mechanism to create price signals for demand balancing, as well as for consumer engagement, is to establish trading platforms (or peer-to-peer (P2P) markets) through which household can directly buy and sell renewable energy. However, residential consumers are typically lay users with little or no previous exposure to the complexity and the dynamics involved in energy markets. More so, empirical research on consumer engagement in the energy sector indicates that individuals tend to act against their stated proenvironmental intentions and to lose interest in energy management systems particularly quickly—calling into question regulatory efforts to foster P2P markets to push the transition to renewable energy. We have implemented the <sup>fi</sup>rst empirical study worldwide that analyzes bidding behavior in a real-world P2P energy market, in which users bid for solar energy via an auction mechanism. For the duration of an entire year, users could interact with the market using a web app. The prices settled on the P2P market directly impacted participants’ electricity bills. We provide unique empirical evidence showing that (1) participants were willing to engage in energy trading and that (2) they understood the market mechanism surprisingly well and exhibited learning effects. Still, bidding behavior did not re<sup>fl</sup>ect their stated intention of paying a price premium for local solar energy. The market outcomes reveal that P2P energy markets can indeed have a positive impact on balancing demand and supply, thereby addressing the fundamental challenge of distributed renewable energy systems.

History: Alok Gupta, Senior Editor; Pallab Sanyal, Associate Editor.

Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute thi work as “Information Systems Research. Copyright © 2022 The Author(s). https://doi.org/10.1287/ isre.2021.1098, used under a Creative Commons Attribution License: https://creativecommons.org licenses/by/4.0/."

Funding: This work was supported by the Swiss Federal Of<sup>fi</sup>ce of Energy [Grant SI/501660-01] and by the Quartierstrom consortium. Additional funding for one of the authors was provided by the Bavarian State Ministry of Science and the Arts in a program coordinated by the Bavarian Research Institute for Digital Transformation (bidt).

Keywords: green IS P2P markets electronic markets market design sustainable energy systems

## 1. Motivation and Introduction

Distributed renewable energy generators, together with an electri<sup>fi</sup>cation of transport and heating, play a pivotal role in cutting greenhouse gas emissions (Siler-Evans et al. 2013, International Energy Agency 2018), and therefore in mitigating climate change (United Nations 2019). One way to foster the diffusion of renewable energy generators among private consumers is peer-to-peer (P2P) markets in which owners of photovoltaic (PV) panels can sell solar energy to their neighbors (Gholami et al. 2016). In the past few years, many countries have drafted or implemented legislation to accommodate P2P energy markets to encourage such user-centric market models. For instance, a recent European Union directive required all member states to implement laws ensuring that consumers have the option to trade electricity between households by 2021 (European Commission 2018). Policy makers thereby aim to make renewable energy resources more accessible and attractive to consumers and to reconsider dynamic pricing as a mechanism to induce short-run demand response in electricity markets, where demand and supply are both highly variable (Bollinger and Hartmann 2020). Given the opportunity to sell their renewable energy on accessible online platforms, private consumers may start leading the way toward a radically transformed energy market and, possibly, toward more ef<sup>fi</sup>cient resource use (Bapna et al. 2004, Guo et al. 2012, Einav et al. 2016).

The success of such P2P markets hinges on consumers’ acceptance of and engagement with these interactive systems. However, the assumptions and empirica <sup>fi</sup>ndings that are valid in other online markets may not hold for the energy context. First, consumer-centric market design is a novelty in the energy sector, in which consumers are used to perceiving electricity as a commodity that does not require any active management from their side. Second, most individuals are lay users with limited understanding of the energy sector (Wilcox 2000, Chen et al. 2021). Given their hitherto passive role, there was no need for consumers to develop an understanding of topics such as the market logic of supply and demand, or physical grid limitations and abstract measurement units like kilowatt hours. Third, interaction with the P2P electricity market is voluntary for consumers (as opposed to systems designed for professional traders), and engagement with the market competes with many alternative ways for consumers to spend their free time. Fourth, the monetary sums per transaction are very small, and even in total, relatively small sums are at stake. Hence, dedicating hours to optimizing one’s bidding strategy and energy consumption patterns in a P2P energy market may not necessarily pay off. Finally, in contrast to one-time auctions where no bidding means no participation in the auction, electricity platforms involve a long-term interaction with recurring clearing periods. Because consumers will obviously not update their bidding preferences every 15 minutes, the design of the platform needs to de<sup>fi</sup>ne rules for bids in subsequent time steps and defaults in the absence of active choices being made. For all these reasons, it remains unclear whether P2P energy markets really are a viable means to achieve the goal of engaging consumers and pushing the transition toward renewable energy. To address this gap, we present the <sup>fi</sup>rst <sup>fi</sup>eld study that investigates an information system (IS)-enabled marketplace for P2P energy trading in the real world. We <sup>fi</sup>rst evaluate whether consumers actually engage in P2P trading of energy (Section 4.1). Next, we examine their bidding behavior to understand whether they are able to deal with the complexity of an auction market in this context, and whether they follow a cost-minimizing strategy or are willing to pay a price premium for locally generated solar electricity (Section 4.2). Finally, we investigate the ef<sup>fi</sup>ciency of the P2P market and whether it creates incentives for consuming (and generating) renewable energy (Section 4.3).

During a one-year framed <sup>fi</sup>eld study, we observed participants’ bidding behavior in an online auction market for solar energy. More precisely, 37 residential customers of a utility provider in a Swiss town formed a local P2P market. We designed, implemented, and deployed a trading platform using a blockchain system that ran on smart meters installed in the participants’ homes. Participants interacted with the P2P market using a web application. Our <sup>fi</sup>eld study allowed us to evaluate the bidding activity and continuous use of the system over the course of one year, and hence to investigate time effects including learning effects, fatigue, or loss of interest. Notably, the application enabled the participants to state the maximum price they were willing to pay for locally produced solar energy, as well as the minimum price at which producers were willing to sell. Unlike the intentional statements elicited in existing survey studies, which merely indicated theoretical willingness to pay (WTP), participants’ bidding behavior in this study directly in<sup>fl</sup>uenced their actual electricity bills. Our <sup>fi</sup>ndings thus complement conceptual and purely survey-based research on P2P energy markets. We further provide insights into the real-world impact in terms of market prices for electricity, as well as the resulting allocative ef<sup>fi</sup>ciency of the market. By allowing actual human participants to de<sup>fi</sup>ne consequential bids for electricity traded in a P2P market, we evaluate whether such bottom-up market mechanisms can ef<sup>fi</sup>ciently coordinate distributed energy resources at the household level.

The implications derived from our empirical insights can be instrumental for designing sustainable energy systems and regulatory frameworks for smart sustainable markets.

## 2. Related Work

Online auctions are some of the purest market design problems that arise in practice (Roth 2008), as they provide an ideal setting to study individuals’ bidding behavior. In the digital economy, involving private individuals in price-setting procedures via auctions has become feasible and increasingly popular (Bapna et al. 2003).

## 2.1. Bidding Behavior in Online Auctions

Although the theory on market design provides valuable guidelines for developing intuitions, mechanisms that work well under the simplifying assumptions about human behavior in theoretical models can fail in real-life challenges (Chen et al. 2021). Hence, the bidding behavior of individuals in online markets may deviate from theoretical predictions and might vary among individuals (Wilcox 2000). Most theoretical models do not account for bounded rationality, limited attention, learning effects, or bounded selfinterest, etc., which characterize human decision making in many real-world situations. Consequently, in recent years, scholars in many domains have turned to empirical experiments and <sup>fi</sup>eld studies to develop a more applicable and holistic understanding of behavior in online marketplaces (Ågerfalk 2014). In fact, empirical studies of online auctions have revealed the existence of time trends and heterogeneous bidder types based on bidders’ time of entry, time of exit, and number of bids (Bapna et al. 2004, Lu et al. 2016). For instance, Goes et al. (2012), Wang and Hu (2009), and Wilcox (2000) report that learning effects from previous experiences (i.e., bidders react to their performance in previous instances of an auction) occur for online auction websites in the retail domain. Additionally, Goes et al. (2012) <sup>fi</sup>nd indications for the “declining price anomaly,” which describes the phenomenon that market prices in sequential auctions of identical goods decline over time (McAfee and Vincent 1993, p. 1). Overall, these studies suggest that bidders’ previous experiences can have a signi<sup>fi</sup>cant impact on their behavior in online auctions.

## 2.2. Consumer Engagement in Energy Systems

Whereas these effects reveal how online auctions engages participants over time, empirical analyses of engagement programs in the energy sector report time trends of a different nature: high attrition rates, a rapid decline in engagement, and various forms of consumer inertia. The roll-out of millions of smart electricity meters across the globe had been driven by the hope that these meters would empower consumers to manage their energy resources more ef<sup>fi</sup>ciently (Ehrhardt-Martinez et al. 2010), but most programs report very modest engagement levels. In particular, programs that require consumers to repeatedly take action (like logging into a portal) typically report various forms of consumer inertia, including low initial take-up rates, high attrition rates (Buchanan et al. 2015, Golz and Hahnel ¨ 2016), a rapid decline in the use of the feedback portals or in-home displays provided (Strengers 2013, Golz and Hahnel¨ 2016), or participants’ tendency to stick to the default settings (Ebeling and Lotz 2015). This lack of active participation and user engagement in energy programs creates challenges for transitioning to more sustainable consumption patterns (Tiefenbeck et al. 2019)—after all, even the introduction of autonomous systems to optimize energy consumption patterns requires user adoption and investment in the <sup>fi</sup>rst place.

In the context of P2P energy markets, there is a lack of empirical research with a behavioral focus, as most existing studies on the topic (1) are conceptual, (2) focus on the technical implementation, or (3) are limited to stated intentions in the context of hypothetical scenarios. So far, bidding behavior in P2P energy markets is imputed either from survey-based research, economic theory, or highly simpli<sup>fi</sup>ed behavioral models. For instance, Mengelkamp et al. (2017a) analyze a time-discrete uniform double auction for solar energy in a simulated P2P market with standardized consumption pro<sup>fi</sup>les for which they construct arti<sup>fi</sup>cial bidding data. Survey studies investigating price preferences in P2P energy trading communities based on hypothetical scenarios provide mixed results. The results of studies by Hahnel et al. (2019) and Ecker et al. (2018) suggest very high interest in P2P markets and high potential uptake rates (e.g., of 77% among German homeowners). The former reports a high price elasticity for the largest cluster of participants, indicating the importance of <sup>fi</sup>nancial aspects and price preferences in P2P energy trading. By contrast, based on a representative sample of 489 German homeowners, Ecker et al. (2018) report a willingness to pay a price premium of 20% on average for generating energy from their own PV panels or battery storage systems.

Yet, survey results do not always provide a true representation of individual preferences (Fishbein and Ajzen 1975). Participants’ responses may be subject to the intention–behavior gap frequently observed in particular in the context of prosocial behavior (Carrington et al. 2014) or to a social desirability bias. Hence, consumers may not only often act against theoretical predictions, but even against their own stated intentions. These phenomena highlight the importance of collecting empirical evidence in the <sup>fi</sup>eld.

## 3. Study Design

We conducted a framed <sup>fi</sup>eld study to examine bidding in a real-world P2P energy market. The study took place in a town in Switzerland and lasted for one full calendar year, from January 7, 2019, through Janu ary 6, 2020 (Figure 1). It is one of the <sup>fi</sup>rst realizations in the world of a P2P electricity exchange in which households can engage in direct trading of solar energy using an information system.<sup>1</sup> We allowed participants to actively bid price preferences for locally produced solar energy and collected bids and asks at 15-minute intervals throughout the study. The <sup>fi</sup>eld study was conducted in collaboration with the local utility provider who served as a trusted local point of contact. Together with the academic researchers, they selected a community with a high penetration of residential PV panels. Forty-one households in this community were recruited through the mail for participation in the experiment, 37 of which agreed to participate. The sample (n 37) included 36 residential households and one retirement home. The majority of the participating households $( n _ { p } = 3 1 )$ ) either already had solar panels on their roofs or owned a share of a solar panel on the roof of their apartment building prior to the study; these participants were considered prosumers. The aggregate peak PV capacity was around 280 kW. In addition, $n _ { b } = 7$ prosumers owned (a share of) a home energy storage system (which were not actively controlled by the P2P trading platform). When electricity supply and demand within the microgrid were not balanced, the utility provider bought or sold excess capacities at the previously existing feed-in tariff (9.79 c./kWh)<sup>2</sup> and retail tariff (20.75 c./kWh), respectively. The P2P market thus operated in gridconnected mode (Halu et al. 2016).

Figure 1. (Color online) Course of the Field Study During the Year 2019  
![](/api/attachments/4JY2ANWN/fulltext/images/e2a9a963bdf886af21a38d5306f871d3fadd4d30f8adc9b8ce988178d97fce74.jpg)  
Notes. Reports on energy consumption and expenses/revenues were sent out every month by email. The analyses of bidding behavior exclud the month of April 2019. During that period, the bidding in the discriminatory double auction was interrupted by a one-month experiment in which participants faced a dynamic uniform price. Speci<sup>fi</sup>cally, the price-setting function (that allows participants to change their bids/asks) on the web application was disabled to test a different pricing mechanism. Given space constraints, the results are not included in this paper, but are available upon request.

In addition to real-time information on supply and demand available through a web application, participants received monthly reports summarizing the information available on the web application. It included their energy consumption and production, the resulting expenses, and their share of local energy supply. This report also stated the participant’s average price bids, as well as the average bids and asks from all market participants. Participants who had often failed to purchase local electricity when it was available in the past month received a note stating, “X% of your electricity demand could have been met by local electricity. A local trade did not take place, as your bid price was too low/the producers’ asking price was too high to be matched.” Likewise, prosumers who had de<sup>fi</sup>ned a very high asking price received a similar message informing them of missed opportunities. The reports were sent out at the end of each month via email. After 6 months and again after 12 months (i.e., in July 2019 and January 2020), participants received a bill sent out by the utility provider, which contained a <sup>fi</sup>nancial summary of their local trading activities. The bill contained the same information as the monthly reports aggregated for six months, along with a payment slip to settle the resulting amount due. Electricity bills were based on the prices and trades arranged according to participants bids and asks in the auction. Their bidding behavior thus had actual monetary consequences, which had been communicated to the participants at an information event prior to the study (attended by 29 out of 37 households), through the mail, and via the user interface. In addition, all participants had signed a letter of consent in advance. Our <sup>fi</sup>eld study thus allows us to elicit price preferences from actual trading activity over the duration of an entire year.

## 3.1. Information System

Figure 2 gives an overview of the layers of the IS deployed to run the P2P energy market.

3.1.1. Infrastructure. To enable P2P trading among participants in real time, we deployed a distributed information system that was developed for the purpose of this study: We installed custom-built smart metering devices that measured electricity consumption in each household. Prosumers received a second smart meter for measuring electricity production from their PV panels, and owners of a battery storage system received a third device for measuring battery loads. In total, 75 metering devices were deployed. All devices were connected to the internet, and they measured electricity loads in time intervals of 15 minutes. The smart metering devices formed a private permitted blockchain and locally computed the P2P transactions using the market application described below, without requiring a central server. Each transaction among households was stored on the blockchain, which served as the basis for the electricity bills.

3.1.2. Application. Together with the electricity loads e measured by the smart meters, bid price $p _ { b }$ and asking price $p _ { s }$ (de<sup>fi</sup>ned by participants) were input to a time-discrete, iterative discriminatory double auction (Borenstein et al. 2002, Fabra et al. 2002) to allocate electricity trades within the market (Figure 3). Participants’ buy and sell orders for local electricity, $b _ { B } =$ $( p _ { b } , e ^ { + } )$ and $b _ { S } = ( p _ { s } , e ^ { - } )$ , were collected in 15-minute “clearing periods.” After the orders were collected, an auction mechanism was run to clear the market and determine the resulting electricity trades. The auction

![](/api/attachments/4JY2ANWN/fulltext/images/606305354ba456b26890f3c43a1bcb11facba87b82fa0200b42202ab765010ce.jpg)  
Figure 3. (Color online) Schematic Example of the Discriminative Double Auction  
Note. The decreasing, increasing, and dotted lines illustrate bids, asks, and clearing prices respectively.

Figure 2. (Color online) Overview of the System Architecture of the P2P Energy Market Deployed in the Field  
![](/api/attachments/4JY2ANWN/fulltext/images/07b13ee7f8498d244d6a641af4c1e11d93982b266b860c33d58b109c2aa8af9c.jpg)  
Note. The discriminatory double auction receives inputs from smart meters and the web application used by participants.

matched the buy order with highest bid and the sel order with lowest ask and progressed in descending/ ascending order through the entire order book (ties were resolved by a random draw); an example is provided in Figure 3. The transaction price for each matched trade is the mean of the bid and asking prices of the respective orders of a matched buyer–seller pair (“discriminatory/midpoint pricing”), $\begin{array} { r } { p = \frac { 1 } { 2 } \cdot \left( p _ { b } + p _ { s } \right) } \end{array}$ Prices thus re<sup>fl</sup>ect the availability of solar energy in near real time (Rosen and Madlener 2013). The auction applied a discriminatory pricing rule, which means that the transaction prices directly depend on participants’ own bids/asks (Fabra et al. 2002). Compared with a uniform market clearing price, participants thus have an immediate in<sup>fl</sup>uence on the prices they pay, which provides more direct and consequential feedback on their bidding behavior and can facilitate their understanding of the market mechanism. Furthermore, discriminatory price auctions for electricity tend to yield lower volatility in prices and reduce vulnerability to implicit collusion compared with uniform price auctions—at the cost of higher prices in off-peak periods (Fabra et al. 2002, Klemperer 2002, Rassenti et al. 2003).

3.1.3. User Interface. Participants received access to an individualized web application built for the purpose of this study. The application allowed them (1) to monitor real-time data on their energy consumption (and production, if applicable) and on their past trading behavior and (2) to place price bids. By adjusting a price slider element, they could express their WTP for solar electricity produced by their neighbors in the microgrid ${ p _ { b } } . ^ { 3 }$ Prosumers were also able to de<sup>fi</sup>ne their willingness to accept (WTA) $p _ { s } ,$ that is, their minimum asking prices for selling energy from their solar panels to other households, as opposed to selling it to the utility provider at the feed-in tariff (t<sub>f</sub>).

Figure 4. (Color online) Price Slider Elements in the Web Application for Prosumers in the P2P Market  
![](/api/attachments/4JY2ANWN/fulltext/images/03ff7d716649fa2d761f212e24214ca6b8c42103db3c4d5cdc1fd42286f85169.jpg)  
Note. The consumer version included only the buying slider on the left.

The feed-in-tariff and retail tariff of the utility provider were indicated on the slider elements for orientation, but the slider range also allowed participants to set their bids above retail price (expressing a preference for green/local electricity) or to offer solar energy for free within the neighborhood. The slider element is depicted in Figure 4, and a screenshot of the web application is available in Appendix A.

## 3.2. Data and Participants

The one-year data collection resulted in an extensive data set containing 15-minute load pro<sup>fi</sup>les, auction clearings and transactions from more than 35,000 periods, and the participants’ bidding behavior. The measured electricity demand of 37 participants and the generation pro<sup>fi</sup>les of the 31 prosumer households were cleaned of (potential) measurement errors (e.g., zero consumption when a smart meter was of<sup>fl</sup>ine). To gather supplementary information on participants preferences and their sociodemographics, we also conducted pre- and postexperimental surveys. Among the 32 participants who <sup>fi</sup>lled out the preexperimental survey, 30 were male, and the average age was 55.2 years (standard deviation (SD), 12.9). The average household size was 2.9 people (SD, 1.19). The retirement home had over 100 habitants, for which one representative interacted with the application and <sup>fi</sup>lled out the surveys. Twenty-one of the survey respondents were employed, 10 were retired, and 1 described herself as a stay-at-home mother. Seven households lived in apartments, and the others in single-family homes.

## 4. Experimental Results

This study creates a unique opportunity to evaluate bidding behavior in a P2P energy market. We observe real electricity consumption and production data, as well as the behavior of participating households in terms of their trading behavior and price preferences throughout all seasons.

## 4.1. Consumer Engagement

Research on consumer behavior suggests that consumer engagement in environmental and energy-conservation programs is very limited and short-lived. Given that engaging consumers actively in the energy transition is one of the key aims of establishing new market models such as P2P markets and dynamic prices (European Commission 2018, Hahnel et al. 2019), we examine con sumers’ engagement over time in this one-year study. Among the 37 participants who signed up for the P2P market through the mail, 28 registered for the web app, and 9 never did (we call them passive users). It is important to mention that four of these households do not even use email or did not provide us with an email address, so they were technically not able to sign up/sign into the web application that we provided. These four also did not participate in the surveys accompanying the study. However, they did participate in the P2P trading, buying and selling at the default bids; they were informed about the system through the mail upfront and received the respective remuneration for their trades.

During the one-year study, most active users made use of the price-setting functionality of the web application that allowed them to de<sup>fi</sup>ne their willingness to pay/willingness to accept as shown in Appendix C. By adjusting the price sliders, they overruled the default bids that were preselected for all participants in the study (based on the previous retail tariff $t _ { r } /$ feed-in tariff t ) of $p _ { b } = t _ { r } = 2 0 . 7 5 ~ \mathrm { c . / k W h }$ and $p _ { s } = t _ { r } =$ 9:79 ${ \mathrm { c . / k W h } }$ . Twenty-seven of the 28 active users de<sup>fi</sup>ned their own price bids at least once during the <sup>fi</sup>eld study. Moreover, many of these participants returned to the web application at some point to adjust their bids; in fact, 20 participants (43%) changed their bids more than 10 times throughout the year. Some of them adjusted their bids very frequently; there were even a few “power users,” with one participant adjusting their bids a total of 142 times throughout the year. Whereas consumers could only adjust a buy bid, the prosumer households tended to adjust their ask prices more often. This level of bidding activity is in stark contrast to consumers’ high propensity to stick to defaults when choosing their basic energy contracts, which has been observed in related work (Ebeling and Lotz 2015). Although it is not surprising that most price changes occurred in the <sup>fi</sup>rst months of the study, some of the participants returned every month to adjust their bids/asks. Remarkably, there was a resurgence in bidding activity over the summer months—even though bidding had been deactivated for one spring month in April, which could have caused users to lose interest in bidding.

## 4.2. Bidding Behavior and Learning Effects

Next, we examine the actual bids and asks that participants placed for local solar energy to learn about their preferences, and to examine whether they could cope with the complexity of the market. In the survey before the start of the <sup>fi</sup>eld study $( n = 3 2 )$ , a majority of the participants stated that they would be willing to pay a price premium for locally generated solar energy, indicating a willingness to pay an average increase of roughly 13%. These <sup>fi</sup>ndings are in line with existing survey-based literature in which participants state a higher willingness to pay for local/renewable energy (Ecker et al. 2018). Panel (a) of Figure 5 shows the participants’ average bid and asking prices over the entire year. The average bid price for electricity on the local market was $1 8 . 4 8 ~ \mathrm { c . / k W h ~ ( S D , ~ } 2 . 7 0 ) ;$ the average asking price was 13.01 c./kWh (SD, 3.38). This means that individuals who actively logged into the web app placed bids that were actually lower (or higher) than the default bid (or asking) prices de<sup>fi</sup>ned by the utility’s tariff. These observations reveal something very different than the survey responses would lead us to believe: Participants almost exclusively de<sup>fi</sup>ned bids below the utility’s electricity tariff, and thus hardly any participants offered (or were willing to pay) a price premium in the real market. Conversely, prosumers typically de<sup>fi</sup>ned asking prices above the feedin tariff offered by the utility (t ) for selling electricity on the local market. There is no evidence of a willing ness to accept less than the feed-in tariff to supply other households in the community. In particular, the bids by participants who stated a willingness to pay a price premium (lighter <sup>fi</sup>lled circles in Figure 5(b)) are not signi<sup>fi</sup>cantly different from the participants who stated that they were not willing to pay a price premium (darker circles). Similar to other <sup>fi</sup>eld studies in the energy domain, this provides evidence of an intention–behavior gap or a social desirability bias in the survey results (Carrington et al. 2014), calling into question the results from existing survey-based research on P2P energy markets and consumers’ willingness to pay for renewable energy. Figure 5(b) highlights that, not only on average, but also on the individual level, participants did not live up to their survey statements about offering a price premium for local solar energy.

Figure 5. (Color online) Bidding Behavior Observed  
(a)  
![](/api/attachments/4JY2ANWN/fulltext/images/233f8d1b48c1eb8fac8705245fb1e2627e9aeb70a69bedf90a7a7e5a18200290.jpg)

(b)  
![](/api/attachments/4JY2ANWN/fulltext/images/22c219b2dc0253639ad3c685cf24439ad995ca12e7f216b96dcd6fb0f134fecc.jpg)  
Notes. As shown in panel (a), contrary to their stated preferences for buying renewable energy, participants on average bid a price below th standard energy tariff of 20.75 c./kWh. In panel (b), each dot represents the average bid and ask by one participant (the identity line represent that WTP is equal to WTA; dots representing identical bids overlap).

On the other hand, we do not observe cost-minimizing behavior either, which theoretical models would predict in a competitive market. Assuming that individuals do not care about the origin of their energy supply, their utility function would be solely de<sup>fi</sup>ned by the cost of energy, which would result in prices equal to marginal costs of production in the long run (see also Appendix D). Thus, strictly cost-minimizing sellers would reduce their asking price p<sub>s</sub> to the feed-in tariff, which represents the marginal cost in the present setting (i.e., the opportunity cost of not selling to the utility).<sup>4</sup>

Over the course of the study, however, we observed a highly signi<sup>fi</sup>cant decrease in bids and asks; hence, participants moved closer to the competitive equilibrium in a market of cost-minimizing agents (i.e., to bidding at the feed-in tariff $t _ { f } )$ . The average bid in December was 4% lower than the average bid in January. The decline was even more pronounced in asks (12% decrease from January to December). In a qualitative analysis of individual bidding behavior, we identi<sup>fi</sup>ed 10 bidders who reduced the prices they bid over time, and 15 bidders who reduced their asking prices. Furthermore, 9 participants seemed to follow a seasonal pattern with their bids, that is, they bid lower prices in summer, and only 2 did with their asks. In addition, a handful of bidders changed their price settings over time but did not follow an obvious pattern, with prices that seem rather erratic. A thorough examination of demographic- and personality-related items did not reveal signi<sup>fi</sup>cant effects on the observed bids or explain variations in behavior.

However, we do <sup>fi</sup>nd that (1) the effects of market information, like the average prices de<sup>fi</sup>ned by all participants or the total sum of energy demand, were greater on asks than on bids, and that (2) the explanatory power of these variables was also much higher for asking pri ces. This matches the observation that participants changed their asks more often and the fact that there are many prosumers in the sample of participants for whom the selling side of the market is <sup>fi</sup>nancially more that the share of previous P2P sales shows a highly sig ni<sup>fi</sup>cant effect on asking prices which indicates that participants learned from their previous behavior and reduced their asks when they had been unsuccessful in previous auctions. Although evidence for learning effects has been found in other studies on sequential bidding in online auctions (Bapna et al. 2004, Goes et al. 2012), this is remarkable in a low-involvement, low-incentive domain like the present application. The overall trend toward the competitive equilibrium con<sup>fi</sup>rms the observation by Wilcox (2000) that experience in online auctions leads to behavior more consistent with gametheoretic predictions, despite participants’ intentions for paying more for local renewable energy.

In order to gain deeper insights into participants understanding of the market logic and its dynamics, we asked participants six comprehension questions about the market mechanism and pricing in the post experimental survey (e.g., “Would you recommend a befriended consumer to (a) increase, (b) decrease, (c) hold their bid if solar production on the P2P market increased?”; see Appendix B for an overview of topics covered in the survey). Interestingly, the majority of survey respondents correctly answered the comprehension questions around the market logic on the P2P market, which is somewhat surprising for lay users given the complexity of the market dynamics. On that basis, we conjecture that the market outcomes and the declining price trend do in fact re<sup>fl</sup>ect participants preferences rather than erratic behavior.

Figure 6. (Color online) Number of Price Changes by Month  
![](/api/attachments/4JY2ANWN/fulltext/images/dc50d6926a733bd39946960605e7212ee0bd53ccffdbc16fd84c3f8c74dfefed.jpg)  
Note. Market inef<sup>fi</sup>ciency (dashed line) declines as price changes decrease.

## 4.3. Balancing of Supply and Demand

Given the preferences and learning effects we observed, we further examine whether the resulting market prices successfully created incentives for balancing renewable supply and energy demand. To that end, we examine quantitative and qualitative evidence for the distal impact of the P2P energy market in terms of energy allocation, ef<sup>fi</sup>ciency, and price signalling.

First, the data collected reveal that the matching of buyers’ WTP and sellers’ WTA in our local market was highly ef<sup>fi</sup>cient. Prosumer households consumed 34% of the electricity they generated themselves (see Table 1), and, using the P2P market, the community purchased another 28% of their electricity from their neighbors. Our analyses show that with the given load curves, an increase of only two percentage points, that is, to 30% peer trades, would have been mathematically possible when ignoring participants’ WTA/WTP, revealing a very high allocative ef<sup>fi</sup>ciency in this market. Despite this fact, 38% of the generated solar electricity was still sold to the utility company. As discussed below, there is a substantial mismatch between when energy is consumed and when PV energy is generated. In the absence of larger systems that allow for storing or shifting loads at scale, these numbers indicate that the share of prosumers in the sample was too large compared with pure consumers; hence, in the majority of sunny hours, the supply on the P2P market exceeded local demand. To put this into perspective, Figure 6 sets bidding activity in relation to the allocative ef<sup>fi</sup>ciency of the market. The bars depict the number of price changes per month; the dotted line (plotted on the y-axis on the right) re<sup>fl</sup>ects the allocative inef<sup>fi</sup>ciency occurring as a result of mismatching price bids on the market. After a peak in June (when an additional 8% of the total consumption could have been covered in the local market if WTA and WTP had matched), market inef<sup>fi</sup>ciency decreased again, and from September onward, inef<sup>fi</sup>ciency was lower than it was from January to March. We attribute this to the learning effects described above.

Based on the observed bids, trades among peers cleared at an average price of $\bar { \hat { p _ { t } } } = 1 5 . 6 5 ~ \mathrm { c . / k W h }$ (SD, 1.86). Figure 7 shows average daily electricity prices for consumers on the market in winter (as an example, January) and in summer (as an example, July), as wel as the average consumption and generation pro<sup>fi</sup>le. The prices depicted are the prices consumers in this market incurred on average and thus are weighted averages of the transaction prices from the auction and the utility retail tariff $t _ { r } = 2 0 . 7 5$ . Taking local trades and electricity purchased from the utility together, participants incurred a total average price of $\bar { \hat { p _ { c } } } = 1 9 . 0 1 \ \mathrm { { \bar { c } . / k W h } }$ (SD, 2.65) throughout the year. The black curve illustrates the fact that average prices dropped during the day when solar power was available, hence creating an incentive for consuming solar energy when it was available. Even so, the monthly graphic is still an aggregated visualization of average price signals per month, whereas the actual P2P transaction prices varied every 15 minutes, immediately signalling changes in demand and supply. As was to be expected, the transaction prices for solar energy decreased over the summer months and increased in the winter months, when supply of solar energy was limited and demand for electricity was higher. In summer, average market prices even dropped below the prosumers’ average asking price. This can be explained by the large share of prosumer households in our participant sample, which led to an oversupply of solar power during very sunny hours. In those instances, only the prosumers with the lowest asking prices were matched with the few net consumers who actually demanded electricity—granting consumers a considerably higher market power during sunny hours. As participants incurred small <sup>fi</sup>nancial bene<sup>fi</sup>ts from buying energy from their peers rather than from the utility provider, they were able to save money when consuming energy during midday hours. The most successful bidding strategy was to offer solar electricity at the lowest price close to the feed-in tariff. For consumers, savings in this study ranged between 8% and 14% (mean, 10.5%; SD, 2.0%) of their electricity bills, whereas prosumers earned an additional income of 6%–110% (mean, 52.1%; SD, 23.5%) for their energy sold, although the revenues for prosumers are much lower in absolute terms. Note that monetary savings greatly depend upon the energy and feed-in tariffs established by the local utility company.

Table 1. Overview of Trades of Energy Produced (Panel A) and Consumed (Panel B) on the P2P Market

<table><tr><td>Panel A: Buyers of the energy produced by the market participants</td><td>kWh (%)</td></tr><tr><td>Self-consumption (own home)</td><td>82,425 (34%)</td></tr><tr><td>P2P market</td><td>69,357 (28%)</td></tr><tr><td>Utility provider</td><td>92,291 (38%)</td></tr><tr><td>Total</td><td>244,073 (100%)</td></tr><tr><td>Panel B: Sellers of the energy consumed by the market participants</td><td>kWh (%)</td></tr><tr><td>Self-consumption (own home)</td><td>82,425 (21%)</td></tr><tr><td>P2P market</td><td>69,357 (18%)</td></tr><tr><td>Utility provider</td><td>239,436 (61%)</td></tr><tr><td>Total</td><td>391,217 (100%)</td></tr></table>

Figure 7. (Color online) Electricity Consumption (Bars in Background), Solar Generation (Bars with Peak Around 0:00 PM), and Average Prices (Black Line) in Winter (January) and Summer (July)  
![](/api/attachments/4JY2ANWN/fulltext/images/b1192d5270c06305014556f430c8e06019f242166737396a1dd618fba3834987.jpg)  
Note. Transaction prices within the P2P exchange re<sup>fl</sup>ect availability of local energy.

![](/api/attachments/4JY2ANWN/fulltext/images/cad85ded9da0db8f261f35c4793fa633d7fc7a3a7ce7ec668171af815abb7c16.jpg)

In addition to the dynamic price signals emerging from participants’ bidding behavior, the market outcomes reveal a mismatch between times of solar generation and consumption peaks in the local grid. The average load curves shown in Figure 7 illustrate that considerable load shifting efforts are required to minimize electricity consumption from the grid. Although the monetary expenses for electricity, and thus the potential savings, are low relative to other household expenses, interviews conducted after the withinsubject experiment revealed that several participants made efforts to consume energy during sunny hours rather than in the evening (Ableitner et al. 2020). In line with this, 15 of the 19 survey participants in the postexperimental survey stated that sustainability was an essential driver for them to participate in P2P trading (4.31/5 on a Likert scale).

## 5. Discussion and Future Work

The idea of P2P energy markets is, among other factors, driven by the aim of actively engaging consumers in the energy market and raising their understanding of and interest in the topic of energy supply, in order to establish sustainable energy systems that rely on decentralized renewable energy resources (Mengelkamp et al. 2017b, Hahnel et al. 2019). In stark contrast to the lack of consumer engagement observed in many other energy management platforms and environmental programs (Buchanan et al. 2015, Golz and Hahnel¨ 2016)—and contrary to popular intuition—participants of this study utilized the opportunity to repeatedly engage with and in<sup>fl</sup>uence prices on the P2P energy market. Whereas existing energy management systems typically provide a one-directional <sup>fl</sup>ow of information, the P2P market enables participants to state their price preferences and, thus, to actively in<sup>fl</sup>uence trading on the local market. This role is novel for consumers in the energy sector and grants them unprecedented autonomy, which is known to be an important driver of intrinsic motivation (Deci and Ryan 2012). At the same time, the bidding feature offered participants the opportunity to playfully explore the effects of their price bids almost immediately (in terms of local trades realized or not, and if so, at what price), thereby enabling effective learning and competence development through the transformation of experience (Kolb 1984, Deci and Ryan 2012). Overall, the presented evidence suggests that P2P trading can, in fact, successfully activate consumer engagement, which is absolutely vital for inducing a transition to renewable energy on a larger scale. Beyond the frequency of engagement, the bidding data observed indicates that even lay users can do a reasonably good job of approaching competitive market prices when bidding on a P2P energy market.

Taken together, we conducted the <sup>fi</sup>rst empirical study that provides evidence that consumers can cope with the complexity of a P2P energy market, and that digital platforms for energy trading can provide a viable means of better understanding the dynamics of energy systems and of getting consumers to engage with the topic. Our study thus highlights that a market mechanism derived from theory can produce a practically viable, primarily local energy market, even in a context with lay participants and with a high imbalance in supply and demand. Our results further reveal that participants’ bidding behavior does not re<sup>fl</sup>ect their previously stated intentions to pay a price premium for local solar energy. These <sup>fi</sup>ndings call into question existing survey studies about P2P scenarios (Ecker et al. 2018, Hahnel et al. 2019) and emphasize the importance of empirical studies in this context. It is dif<sup>fi</sup>cult to fathom what ultimately caused the discrepancy between participants’ stated preferences for local solar energy and their bidding behavior. Participants’ answers in the preexperimental survey (and in other related research) may have been subject to social desirability bias. It is also plausible that they were caught up in the competitive nature of known market logic or did not realize that their bidding behavior was counterproductive to actively supporting renewable energy generation. However, although participants’ stated intentions did not materialize, they also did not act in a purely cost-minimizing way, that is, bidding the feed-in tariff. Still, our evidence shows that long-term bidding behavior is consistent with predictions on rational bidding behavior and exhibits learning effects (Wilcox 2000, Wang and Hu 2009, Goes et al. 2012). The decline in price bids and increasing ef<sup>fi</sup>ciency indicates a tatonnementˆ (gentle convergence) toward the competitive equilibrium (Gode and Sunder 1993), in which the price for solar energy is close to the feed-in tariff.

Finally, our analyses indicate that the prices in this P2P market provide ef<sup>fi</sup>cient signals to shift electricity consumption to times of local renewable production. By contrast, today’s energy markets, with their regulated and fairly rigid feed-in tariffs, do not provide ef<sup>fi</sup>- cient price signals for local balancing: information about when and to what extent supply and demand match in a local area is not available to the individual households, nor is it of consequence for the <sup>fi</sup>nancial returns on solar or battery installations. This is highly problematic for future energy markets that greatly rely on distributed resources to balance distribution grids, to meet climate targets, and to accommodate added loads from heat pumps and electric vehicles. Precise market signals are essential to increase the diffusion of renewable generators (and storage systems) where required, as well as to limit incentives for their adoption where there is already a large overproduction. Our study suggests that local P2P energy markets are able to provide precise market signals to ef<sup>fi</sup>ciently and dynamically coordinate investments and to better balance local demand and supply. Our study presents <sup>fi</sup>rst qualitative evidence on the potential of P2P energy markets in terms of energy balancing; more research is needed to assess these effects quantitatively. To that end, a considerably larger sample and a control group will be required to control for unrelated shifts in demand.

Despite our best efforts, given the technical and operational complexity involved in conducting a <sup>fi</sup>eld study of this nature, there are limitations to our <sup>fi</sup>ndings. Most critically, the sample of 37 participating households (including one retirement home) is not representative of the larger population. All participants live in the same town, and they are customers of the local utility provider. Given that the experiment had an impact on participants’ electricity bills, they had to opt into the study at the invitation of their utility provider. The results may thus be subject to volunteer selection bias (Tiefenbeck et al. 2019). Furthermore, the large proportion of prosumers is not representative of most neighborhoods today. It is conceivable that early adopters of new technologies, like solar PV systems, are overrepresented in the sample. Moreover, the resulting imbalance of electricity demand and solar supply during sunny hours may have biased participants’ behavior. Whereas, to the best of our knowledge, this study is the <sup>fi</sup>rst to empirically observe P2P energy trading with real <sup>fi</sup>nancial consequences for participants, future research should address these issues. To increase the trading volume and liquidity on the P2P market, as well as to reduce transactions with the utility provider, P2P markets should integrate more consumer households and diversify the sources of distributed electricity production by including, for example, local wind or hydropower generators.

Overall, the <sup>fi</sup>nancial incentives at stake in our study were fairly small, particularly for consumers. Consequently, it is crucial to investigate whether the results regarding engagement and bidding behavior can be generalized to the broader public. At the same time, the monetary incentives created by dynamic price signals will likely become more relevant in the future because of the electri<sup>fi</sup>cation of transport and heating. Future research needs to assess how the associated imminent rise in household expenses on electricity will affect participants’ behavior.

Future research should also examine bidding behavior beyond the prices de<sup>fi</sup>ned by participants. As a <sup>fi</sup>rst step in that direction, we have conducted a simulation evaluating the impacts of different bidding strategies and load pro<sup>fi</sup>les with different community sizes and consumer–prosumer ratios. Appendix D provides more details and compares the bidding behavior observed with the market outcomes of (a) a pure cost-optimizing strategy and (b) a green strategy with price premiums. Beyond that, to foster the broad diffusion of P2P energy markets, future research (and practitioners) must also identify a viable business model for setting up and operating these markets. Likewise, the acceptance of decision support systems or smart agents for P2P markets is a promising area for future research. Decision support systems could help individuals to bene<sup>fi</sup>t from dynamic price incentives by actively scheduling loads to balance the energy system on a local level (Ketter et al. 2018, Avci et al. 2019, Bollinger and Hartmann 2020). In particular, smart agents controlling storage devices according to the individual household’s preferences can leverage real-time market signals to improve the environmental and monetary impact of P2P trading (Ansarin et al. 2020). Of course, local load balancing according to such price signals will require an extent of automation to match the volatility of renewable generation.

One strategy could rely on autonomous agents that point out the environmental consequences of market interactions. For instance, these systems could factor in long-term external costs of different energy sources. They could thus alleviate the zero-marginal-cost dilemma that renewable generators face, without going back to topdown control of externally de<sup>fi</sup>ned tariffs.

In summary, P2P energy markets emerge as a viable means for engaging consumers in the energy transition and for coordinating and incentivizing renewable energy resources, even in a setting with high imbalance in supply and demand. Such markets thus provide a promising alternative to top-down regulations and government subsidies (Siler-Evans et al. 2013). Our <sup>fi</sup>ndings show that the autonomy of consumers and prosumers through active market participation may lead to an unprecedented level of engagement in the energy market.

## Acknowledgments

The authors thank the senior editor, Alok Gupta; the associate editor; and the reviewers for their valuable feedback during the review process of this manuscript. Special thanks go to Sandro Schopfer, the utility company EW Walenstadt, and their chief executive of<sup>fi</sup>cer, Christian Duerr, for their efforts in conducting this <sup>fi</sup>eld study. The authors thank all members of the research consortium (see https://quartierstrom.ch for details) for their efforts in launching and supporting the project, as well as Konstantin Hopf for providing valuable input data for some of the simulations.

## Appendix A. User Interface

Figure A.1. (Color online) User Interface  
![](/api/attachments/4JY2ANWN/fulltext/images/4f57995d0b53d8bb3dc9ea5c9bfa749a3272a45d4b4454ad162d503b40b3feb6.jpg)

![](/api/attachments/4JY2ANWN/fulltext/images/fa292d0521764912e057f0f876c382ec0484ab4e5798db75221106554e4953f6.jpg)

![](/api/attachments/4JY2ANWN/fulltext/images/dd0ca4bda13482dd5edc79bae615c625b3cf3f58c35f6fbfab8d2131a0b279fa.jpg)  
Note. The <sup>fi</sup>gure shows the “Your Energy Data” page of the web application that participants used during the <sup>fi</sup>eld study; see also Ableitner et al. (2020).

## Appendix B. Surveys

As outlined in the article, we administered pre- and poststudy surveys to the participants. The following lists provide an overview of the survey data collected:

Prestudy survey:

Demographics: age, gender, education, employment, household income, household size, children in the household

<sub>•</sub> Housing situation: type and age of building, owner or tenant, passive house

Local attachment (3 items)

<sub>•</sub> Ownership of PV system, battery storage, heat pump, electric water heater

<sub>•</sub> Annual electricity bill (estimate of typical amount)

Intention to use the web app, different sources of motivation (5 items)

Motivation to participate in the study (9 items)

<sub>•</sub> Willingness to pay a price premium for PV-generated electricity and for locally generated electricity (4 items)

Likelihood of investing in a PV system, battery storage, community infrastructure in the next 10 years (3 items)

Environmental attitude (1 items)

Computer literacy, technology readiness index, af<sup>fi</sup>nity to numbers (23 items)

<sub>•</sub> Political orientation and past donations to sustainability projects

<sub>•</sub> Trading experience (2 items)

Self-ef<sup>fi</sup>cacy (10 items)

<sub>•</sub> Privacy concerns (8 items)

Risk behavior (6 items)

Mid- and poststudy surveys:

General assessment

Conversations about the local energy market with others (3 items)

Intention to use the portal in the next month

Usability (12 items)

Usage purpose and usage triggers (12 items)

Likelihood of investing in a PV system, battery storage, community infrastructure in the next 10 years (3 items)

(Electric) mobility (5 items)

<sub>•</sub> Usability of the reduced portal in April without price setting (5 items)

<sub>•</sub> Free-text questions about price limits and bidding strategy (3 questions)

Comprehension of market mechanics (6 items)

Factors in<sup>fl</sup>uencing bidding strategy (7 items)

<sub>•</sub> Preference regarding price setting versus automatic price determination

<sub>•</sub> Preference regarding automated service for price setting (5 items)

## Appendix C. Observed Data

## Appendix D. Simulation of Benchmark Strategies

To put the results observed in the <sup>fi</sup>eld study into context and evaluate the sensitivity of the market outcomes of this market design to a larger sample of consumption pro-<sup>fi</sup>les, we ran a simulation of P2P energy trading with realworld load pro<sup>fi</sup>les from 223 other households.

The data are net-metered with a 15-minute resolution. The data cover the entire year of 2018; however, we use the month of September for our simulations. Energy consumption and production in that month are close to the year round monthly averages, and bidding behavior does not change as much (as it did during the spring months) after September in our study. We simulate varying community sizes and prosumer shares. At each step of the simulation, each household is represented by an agent that posts a bid with the net energy demand obtained from its speci<sup>fi</sup>c load pro<sup>fi</sup>le, as well as a price preference. After posting, the double auction mechanism is run to allocate trades and deter mine prices. The price preferences submitted by the agents were varied for different simulation setups. We apply a simulation model as a “risk-free, cost-effective environment” (Bapna et al. 2003, p. 245) to understand the potential impact of extreme forms of bidding behavior. To put the bidding behavior observed in the <sup>fi</sup>eld study $( p _ { \hat { b } } , p _ { \hat { s } } )$ into context, we model two benchmark strategies that span a spectrum from cost-oriented to green preferences:

Figure C.1. (Color online) Absolute Number of Price Bid Changes by Participant  
![](/api/attachments/4JY2ANWN/fulltext/images/f5ac769d4c3bd075f668349591fc323dd22c27df8bf55b14eff081f225ff3b03.jpg)  
Note. Participants adjusted their price bids between 0 and 142 times during the one-year study.

Figure D.1. (Color online) Simulation of Different Bidding Strategies in a Market of 40 Participants with 50% Prosumers, Aggregated to an Average Day in September  
![](/api/attachments/4JY2ANWN/fulltext/images/4a8d17217d28f6886095d9defbac71e7b42a8644ddc3949d141b137c156e1a22.jpg)  
Note. Average prices in the observed empirical behavior fall in between the two extreme cases; volumes traded are almost identical (indicating high ef<sup>fi</sup>ciency of the observed bids)

a. As described above (see in Section 4.2), the equilibrium price for solar energy under perfect competition would be the opportunity cost. $p _ { b , r a t } = t _ { f } + \epsilon$ with $\epsilon = 0 . 0 0 1$ as a cost-minimizer strategy for the buying side and $p _ { s , r a t } = t _ { f }$ for the selling side, that is, assuming individuals have no preference for green electricity sourcing.

b.  In the preexperimental survey, as well as <sup>Green strategy:</sup>in the related literature, many consumers state a willingness to pay more for local or renewable energy. We thus de<sup>fi</sup>ne the bid prices for buying in the green strategy to be $p _ { b , g r e e n } = t _ { r } + 0 . 1 0 t _ { r }$ $p _ { s , g r e e n } = p _ { \hat { s } }$ remains as observed in the <sup>fi</sup>eld.

Figure D.1 shows the average prices for buying electricity on the simulated market with 40 households and 20 prosumers (i.e., similar size, but lower prosumer share than in the <sup>fi</sup>eld study) on an average day in September. The <sup>fi</sup>gure illustrates that the bidding behavior that we observed in the <sup>fi</sup>eld study (not surprisingly) produced a result in between what we ob served in Scenarios a (bright solid line) and b (dashed line). However, the simulation also shows that the difference be tween the observed behavior in the <sup>fi</sup>eld (black solid line) and that with the green strategy is smaller. In turn, there is a rela tively large margin to the cost-minimizer strategy. In the simu lated model, average prices for consumers in Scenario a result in 16.26 c./kWh (SD, 5.29), and those in scenario b result in 18.83 c./kWh (SD, 2.79), and sampling from the bidding strategies we observed in the <sup>fi</sup>eld results in 18.16 c./kWh (SD, 3.37). Remarkably, there is hardly any difference in the volumes traded in different strategies, which indicates the high level of allocative ef<sup>fi</sup>ciency achieved on this market in the <sup>fi</sup>eld.

## Endnotes

$^ 1 \mathrm { \ A }$ conference article based on preliminary results of this same study was published in the Proceedings of the International Conference on Information Systems (Worner et al.¨ 2019).

<sup>2</sup> Electricity prices are indicated in centimes (c.), that is, $\frac { 1 } { 1 0 0 }$ Swiss Francs (CHF) per kilowatt hour.

<sup>3</sup> We will use the superscript ˆ for data points collected in our field study throughout this paper.

Although initial investments may be high, the marginal costs of renewable energy generation are generally low or close to zero (Koolen et al. 2017). In the case of solar panels, a prosumer does not incur a marginal cost for an additional unit of electricity being produced on his or her roof.

<sup>5</sup> These are excluded for brevity, but available upon request.

## References

Ableitner L, Tiefenbeck V, Meeuw A, Worner A, Fleisch E, Wortmann¨ F (2020) User behavior in a real-world peer-to-peer electricity market. Applied Energy 270:115061.

Ågerfalk PJ (2014) Insuf<sup>fi</sup>cient theoretical contribution: A conclusive rationale for rejection? Eur. J. Inform. Systems 23(6):593–599.

Ansarin M, Ghiassi-Farrokhfal Y, Ketter W, Collins J (2020) Crosssubsidies among residential electricity prosumers from tariff design and metering infrastructure. Energy Policy 145:111736.

Avci E, Bunn D, Ketter W, van Heck E (2019) Agent-level determinants of price expectation formation in online double-sided auctions. Decision Support Systems 124:113068.

Bapna R, Goes P, Gupta A (2003) Replicating online Yankee auc tions to analyze auctioneers’ and bidders’ strategies. Inform. Systems Res. 14(3):244–268.

Bapna R, Goes P, Gupta A, Jin Y (2004) User heterogeneity and its impact on electronic auction market design: An empirical explo ration. MIS Quart. 28(1):21–43.

Bollinger BK, Hartmann WR (2020) Information vs. automation and implications on pricing. Management Sci. 66(1):1–25.

Borenstein S, Bushnell JB, Wolak FA (2002) Measuring market inef<sup>fi</sup> ciencies in California’s restructured wholesale electricity mar ket. Amer. Econom. Rev. 92(5):1376–1405.

Buchanan K, Russo R, Anderson B (2015) The question of energy reduction: The problem(s) with feedback. Energy Policy 77:89–96.

Carrington MJ, Neville BA, Whitwell GJ (2014) Lost in translation: Exploring the ethical consumer intention–behavior gap. J. Bus. Res. 67(1):2759–2767.

Chen Y, Cramton P, List J, Ockenfels A (2021) Market design, human behavior and management. Management Sci. 67(9):5317–5348.

Deci EL, Ryan RM (2012) Self-Determination Theory. In Van Lange PAM, Kruglanski AW, Higgins ET, eds. Handbook of Theories of Social Psychology (Sage Publications Ltd., London), 1:416–436. https://doi.org/10.4135/9781446249215.n21.

Ebeling F, Lotz S (2015) Domestic uptake of green energy promoted by opt-out tariffs. Nature Climate Change 5(9):868–871.

Ecker F, Spada H, Hahnel UJ (2018) Independence without control: Autarky outperforms autonomy bene<sup>fi</sup>ts in the adoption of pri vate energy storage systems. Energy Policy 122:214–228.

Ehrhardt-Martinez K, Donnelly KA, Laitner S, York D, Talbot J, Friedrich K (2010) Advanced metering initiatives and residential feedback programs: A meta-review for household electricitysaving opportunities. Report, American Council for an Energy Ef<sup>fi</sup>cient Economy, Washington, DC.

Einav L, Farronato C, Levin J (2016) Peer-to-peer markets. Annu. Rev. Econom. –

European Commission (2018) Renewable Energy Directive II. Directive (EU) 2018/2001 of the European Parliament and of the Council of 11 December 2018 on the promotion of the use of energy from renewable sources (Text with EEA relevance.) PE/ 48/2018/REV/1 https://eur-lex.europa.eu/legal-content/EN/ TXT/?uri=uriserv:OJ.L\_.2018.328.01.0082.01.ENG&toc=OJ:L:2018: 328:TOC.

Fabra N, Von Der Fehr NH, Harbord D (2002) Modeling electricity auctions. Electricity J. 15(7):72–81.

Fishbein M, Ajzen I (1975) Belief, Attitude, Intention, and Behavior: An Introduction to Theory and Research (Addison-Wesley, Reading, PA).

Gholami R, Watson RT, Hasan H, Molla A, Bjørn-Andersen N (2016) Information systems solutions for environmental sustainability: How can we do more? J. Assoc. Inform. Systems 17(8): 521–536.

Gode DK, Sunder S (1993) Allocative ef<sup>fi</sup>ciency of markets with zero-intelligence traders: Market as a partial substitute for indi vidual rationality. J. Political Econom. 101(1):119–137.

Goes PB, Karuga GG, Tripathi AK (2012) Bidding behavior evolution in sequential auctions: Characterization and analysis. MIS Quart. 36(4):1021–1042.

Golz S, Hahnel UJJ (2016) What motivates people to use energy ¨ feedback systems? A multiple goal approach to predict longterm usage behaviour in daily life. Energy Res. Soc. Sci. 21:155– 166.

Guo Z, Koehler GJ, Whinston AB (2012) A computational analysis of bundle trading markets design for distributed resource allocation. Inform. Systems Res. 23(3-part-1):823–843.

Hahnel UJ, Herberz M, Pena-Bello A, Parra D, Brosch T (2019) Becoming prosumer: Revealing trading preferences and decision-making strategies in peer-to-peer energy communities. Energy Policy 137: 111098.

Halu A, Scala A, Khiyami A, Gonzalez MC (2016) Data-driven´ modeling of solar-powered urban microgrids. Sci. Adv. 2(1): e1500700.

International Energy Agency (2018) Renewables 2018. Report, Inter national Energy Agency, Paris.

Ketter W, Collins J, Saar-Tsechansky M, Marom O (2018) Information systems for a smart electricity grid. ACM Trans. Management Inform. Systems 9(3):1–22

Klemperer P (2002) What really matters in auction design. J. Econom. Perspect. 16(1):169–189.

Kolb DA (1984) Experiential Learning: Experience as the Source of Learning and Development (FT Press, Upper Saddle River, NJ), https://books.google.de/books?id=jpbeBQAAQBAJ&dq=Kolb+ DA+(1984)+Experiential+Learning:+Experience+as+The+Source +of+Learning+and+Development.&lr=&source=gbs\_navlinks\_s.

Koolen D, Ketter W, Qiu L, Gupta A (2017) The sustainability tipping point in electricity markets. Proc. Internat. Conf. Inform. Systems (Association for Information Systems, Atlanta).

Lu Y, Gupta A, Ketter W, Heck EV (2016) Exploring bidder heterogeneity in multichannel sequential B2B auctions. MIS Quart. 40(3): 1–18.

McAfee RP, Vincent D (1993) Declining price anomaly. J. Econom. Theory 60(1):191–212.

Mengelkamp E, Staudt P, Garttner J, Weinhardt C (2017a) Trading on local energy markets: A comparison of market designs and bidding strategies. Proc. 14th Internat. Conf. Eur. Electricity Market (Institute of Electrical and Electronics Engineers, Piscataway, NJ).

Mengelkamp E, Garttner J, Rock K, Kessler S, Orsini L, Weinhardt¨ C (2017b) Designing microgrid energy markets. A case study: The Brooklyn microgrid. Applied Energy 210:870–880.

Rassenti SJ, Smith VL, Wilson BJ (2003) Discriminatory price auctions in electricity markets: Low volatility at the expense of high price levels. J. Regulatory Econom. 23(2):109–123.

Rosen C, Madlener R (2013) An auction design for local reserve energy markets. Decision Support Systems 56:168–179.

Roth AE (2008) What have we learned from market design? Econom. J. 118(527):285–310.

Siler-Evans K, Azevedo IL, Granger Morgan M, Apt J (2013) Regional variations in the health, environmental and climate bene<sup>fi</sup>ts of wind and solar generation. Proc. Natl. Acad. Sci. USA 110(29):11768–11773.

Strengers Y (2013) Smart Energy Technologies in Everyday Life: Smart Utopia? (Springer, Berlin).

Tiefenbeck V, Worner A, Sch¨ ob S, Fleisch E, Staake T (2019) Real-¨ time feedback promotes energy conservation in the absence of volunteer selection bias and monetary incentives. Nature Energy 4(1):35–41.

United Nations (2019) Sustainable development goals. Accessed April 8, 2019, https://www.un.org/sustainabledevelopment/ sustainable-development-goals/.

Wang X, Hu Y (2009) The effect of experience on internet auction bidding dynamics. Marketing Lett. 20:245–261.

Wilcox RT (2000) Experts and amateurs: The role of experience in internet auctions. Marketing Lett. 11(4):363–374

Worner A, Ableitner L, Meeuw A, Wortmann F, Tiefenbeck V (2019)¨ Peer-to-peer energy trading in the real world: Market design and evaluation of the user value proposition. Proc. Internat. Conf. Inform. Systems (Association for Information Systems, Atlanta).

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
