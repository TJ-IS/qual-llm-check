---
otero_id: 10652
otero_key: "UWE97E9K"
title: "Implementing an agent trade server"
authors: "Magnus Boman; Anna Sandin"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 318 – 327

www.elsevier.com/locate/dsw

# Implementing an agent trade server

Magnus Boman <sup>a,T</sup>, Anna Sandin

<sup>a</sup> Swedish Institute of Computer Science (SICS) AB, Box 1263, SE-16429 Kista, Sweden, and The Royal Institute of Technology, Dept. of Computer and Systems Sciences, Forum 100, SE-16440 Kista, Sweden <sup>b</sup> Swedish Institute of Computer Science (SICS) AB, Box 1263, SE-16429 Kista, Sweden

Available online 3 March 2005

## Abstract

An experimental server for stock trading autonomous agents is presented and made available, together with an agent shell for swift development. The server, written in Java, was implemented as proof-of-concept for an agent trade server for a real financial exchange.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Trading agent; Agent server; Financial exchange; Complex order; Agent programming

## 1. Introduction

There are always investors seeking to place orders more complicated than can be accepted by the software of a financial exchange (F/X) system, regardless of its current level of sophistication. To some of these investors, the agent metaphor is a means to implementing combinatorial, temporal, contingent, bundle, or otherwise complex orders. In general, a trading agent is a piece of encapsulated software that codes the preferences of its owner. The responsibility delegated to an agent can vary between very limited, in which the agent acts chiefly as a decision support system serving its owner, to full, in which the agent may act autonomously. In theoretical research, trading agents have been used in idealized games [30], artificial markets [29], and competitions such as the Trading Agent Competition [12] (see http://www.sics.se/tac/). To economists, trading agents are speculating noise traders (traders with non-rational expectations and potentially zero intelligence) [7], often subjected to the Efficient Market Hypothesis and the Rational Expectations Hypothesis [24], since the empirical evidence against the accompanying assumptions are directed almost exclusively towards human traders [23]. In the system of trading agents we consider (cf. Ref. [4]), the agents interact with the same order book as the human traders, resulting in a system only slightly more complex than an F/X is today, but still extremely difficult to analyze (cf., e.g., Ref. [16]). From an academic perspective, the introduction of agents in the actual exchange of real stocks is a formidable challenge in that it prompts research in real-time control, agent programming, decision analysis, user interaction, privacy, and security. Its theoretical models must go beyond agent-based computational finance [19] and agentbased computational economics [33], since the economics described is out-of-equilibrium [1], and already simulation studies are highly complex [20,25,2,8]. From a commercial perspective, the concept is promising in that it enables implementation of new services in the service portfolio of the F/X. A vast range of commercial efforts has helped renew and refine the concept of an electronic F/X, including ambitious liquidity-moving approaches, such as Opti-Mark [22,6,11]. This fact notwithstanding, there has been no technical platform for real stock trading agent development and no special-purpose server generally available. We rectify this matter by making available our documented Java software [32] for such a platform. We have also implemented an experimental server for supporting agent trading of stocks, an Agent Trade Server (ATS), which was made available in January 2003. The conceptual development [26] was initiated in 2001 in cooperation with OM (now OMX), the world’s largest supplier of software to stock exchanges [31], and OM filed a U.S. patent application on the ATS concept [28]. On February 21, 2003, the application was expanded and as per November 15, 2004, processing has begun also in Australia, Singapore, and Japan. In that month, OMX also confirmed that they have developed a product based on the designs specified in the patent [5].

The ATS was built not with commercial operation in mind, but as proof-of-concept, and permission to run agents on the ATS has been restricted to select Swedish universities and research institutes. That said, the third party APIs for OM’s SAXESS interface provided for much inspiration. We have not designed the ATS for any particular market design. Instead, all agents must abide by the rules of the F/X. The submarket emerging from ATS operations will depend on the agents’ business logic. Whether or not investors will find the ATS attractive will to a large extent depend on pricing and other commercial or political concerns. As an example of a positive driver, the lowest transaction cost offered by net broker services available to Sweden fell in 2003 by more than 75%.

The following section briefly describes the role that software, and agent software in particular, plays in an electronic F/X. In Section 3, the architecture of our

ATS is explained. In Section 4, the issue of logging and other forms of keeping history is highlighted. The various business roles, i.e. those interested in the logs, are also discussed. We end with our conclusions and directions for future research.

## 2. Development of financial exchange software

Trading of stocks is normally done through a broker, as shown in Fig. 1. The trader can be a professional investor, a day trader, or any other person using stocks as a means to invest. The broker could be a bank, an Internet broker or some other financial institution. The figure is simplified: orders can also be placed by walking into a bank and filling out a form, IP phones are no requirement, the computer used is often a PDA, etc. Each broker communicates with the core of the F/X via a gateway, over leased lines (at Stockholmsb<sup>f</sup>rsen, the Swedish stock exchange, backed up by an ISDN connection, as well as OMnet, a fibre-optic MetroLAN option). The requirement of general availability of the F/X poses difficult security problems, which will only be dealt with at the rudimentary level here, since commercial use of an ATS would add many security constraints enforced outside the scope of the system we consider (cf. Ref. [21]). In Fig. 1, the dissemination of information from the F/X to the outside world is not shown. Suffice to say here that stock exchange dissemination is an elaborate system of latencies and routing, in order to secure fairness, and that such information is an important part of the feedback from core to broker, and from broker to trader.

Suppliers of software to an electronic exchange system are basically of two kinds: those that provide software serving the core (the order book), and those that provide software for those interacting with the core (the traders). In most countries, the software supplier in the first category also competes in the second category. OM provides two software products (CLICK and SAXESS), as well as trading stations. The bulk of the software aimed at traders and brokers is however developed by third party software houses. We would like to complicate Fig. 1 slightly by considering individuals as service provisioners [9], thus introducing a third kind of software developer (see Fig. 2). We anticipate that end-user software development in the form of trading agents will be an increasingly important part of the future F/X service portfolio.

![](/api/attachments/UWE97E9K/fulltext/images/5747ac405f24776d390a1450a6a8a4162375837a6551e818169e2bf00331bf27.jpg)  
Fig. 1. A schematic view of the current trade information flow.

The third party software pertains to the trading applications used. In order to use the SAXESS system today, the broker needs a member SAXESS trade

![](/api/attachments/UWE97E9K/fulltext/images/76440c52fd3fcee0f4b7a5f55e8d68f934e5268d65d6a5cc18326f85f87084ee.jpg)  
Fig. 2. Three kinds of software development.

application. Each such application must be certified, to guarantee smooth operation alongside all other running applications. The OM application offered is SAXESS Trade, an NT-based client-server solution with the trading data being maintained on an SQL server. There are currently about two dozen certified alternatives. Each application connects to a SAXESS trade server, which is in turn connected to the core. The transaction protocol used is XTP (open eXchange Transaction Protocol) 2.40, an OSI Layer 7 protocol. The Session Layer protocol used is XMP (eXchange Message Protocol). The transactions involving the core are governed by a C program, essentially matching the stack of sell orders with the stack of buy orders. It is important to note that the matching is deterministic. The ATS concept is not a suggested alternative to the SAXESS (or any other) trade server currently in use, but a complement (see Fig. 3). Note that brokers may still be used, for example for legal reasons, when delegating trading to an agent. While delegating the right to place orders in itself does not introduce non-determinism in the marketplace, there is nothing that per se stops an agent developer to introduce non-determinism in the business logic of the agent. Security control of agent software is done at the time of agent certification and testing, and also online in the ATS. Online checks include the validity of software signatures (which block unauthorized modifications), policy file checks (which keep unsigned agents from executing on the ATS), and authentication and encryption (which guarantee confidentiality). Performance and scalability issues include ATS parsing 4.of agent orders and round trip time of confirmations from ATS to agents, including calculation latencies. We have made preliminary investigations into intelligent trading agents that are aware of particularly interesting network states, such as the parts of a trading day in which the network load is at its peak (cf. Ref. [13]).

![](/api/attachments/UWE97E9K/fulltext/images/269ea897c4a9d6b8bdec58c4e31dcf4da27d1ce5655582935fb9cb671947ac50.jpg)

In SAXESS, each trade application must also connect to a dedicated Distributed Dissemination Server (DDS). With an ATS running together with a SAXESS trade server, the owner of the F/X has the option to either route all traffic feedback through the existing DDS channels, or to complement the DDS with ATS traffic feedback. In particular, the agents running on the ATS could subscribe to ATS traffic feedback of various sorts, and at variable cost. Even non-professional traders are no strangers to varying levels of sophistication of the individually specified trading constraints built on feedback. The stop loss service offered by Internet brokers (such as Avanza; see http://www.avanza.com) is a case in point.

The ATS concept provides the third party software houses with a business opportunity, viz. to provide software for the agents trading on the ATS. This involves coding investor preferences and encapsulating these into agents, where after the agents are placed on the ATS, without disclosure. Preference elicitation is as always difficult, but suffice to say here that investors will come in many varieties, from those that have developed advanced agents on their own, to those that have no clue on agent programming. A template agent can be coded based on the investor filling out a fairly simple questionnaire. The size and structure of such template agents is simple, and the first agent shell for our ATS has already been written [17]. After the agent is placed on the ATS, there remains the challenge of providing software services for notification [27] and (depending on security issues) possibly for termination of agents. Investors no doubt require interfaces for a variety of modalities, and will most likely in the future include support for web services (cf. Ref. [10]) and roaming [3].

## 3. An agent trade server architecture

We developed the ATS in-house at SICS, in order to allow for free experimentation with agent software and simultaneously adjusting and adding software to the server. A jar-file containing an agent can be run locally or remotely. Each trading agent executes in his own thread. The three server packages implemented (cf. Fig. 4) are described in turn below. The choice of Java was motivated, among several factors, by smooth compatibility with small devices, such as Java-enabled cell phones. While there is no theoretical reason to limit any sandbox environment for agent development to only one language, Java currently seems the most practical first choice. For instance, Java’s policy files are useful for defining the boundary between ATS and agent, and Java security allows for basic signing of agent software.

## 3.1. se.sics.ats.core

This package represents the interface towards the agents, and is distributed to agent developers. Initially, the list of agent developers will most likely overlap considerably with the list of certified SAXESS members, and the principles for testing will be similar. The next step is then to automate the certification process so that individual agent developers can submit agents to the ATS. Since there are legal and practical reasons for the market owner not to certify every single developer, there is room here for traditional as well as agent brokerage. The class AgentComponent specifies all ATS interfacing demands on the agent. For instance, the agent must have functionality for starting and stopping. The class AgentContext is the agent’s handle on the server. AgentContext is inspired by and adheres to the SAXESS Trade API for third party software development, based on Microsoft’s Component Object Model (COM).

![](/api/attachments/UWE97E9K/fulltext/images/80c00cd3026fcbb7f6e2a6fd4a18aaf2d92b3650e22c4e44b9c4bc3e0c185c1e.jpg)  
Fig. 4. The three ATS packages implemented.

## 3.2. se.sics.ats.reference

This package contains the implementation of the ATS itself. It contains log handlers and socket transceivers.

## 3.3. se.sics.ats.data

This package represents the interface towards the stock exchange. This is where the ATS will connect to the core of the F/X. For now, it contains a parser which, like the connection, can easily be replaced by another. It now parses data disseminated through the WWW (more specifically, it parses http://www. stockholmsborsen.se). The ATS thus uses real stock exchange data, albeit with a delay of up to 15 min. We have limited its capability at the outset to the most traded stocks on the Stockholmsb<sup>f</sup>sen A-list. The package also simulates an order book.

## 4. Agent shell execution

We can now specify the <sup>b</sup>Agent<sup>Q</sup> rectangle from Fig. 4 above by explaining theagent shell. We first turn to some more abstract aspects of ATS management, however.

## 4.1. Roles

In our proof-of-concept implementation work, we have felt the need for a division of labor between agent developers and ourselves: the ATS developers. In order to leave the core software unchanged—a requirement from OM, and most likely from any market owner—we also need to define the role of ATS administrator. The regulation of trade in SAXESS is today done through surveillance of the Trading Engine (SaxView), as well as through the official trading control and supervisory functions units. These units operate on the core and will be used also for agent trading. In addition, the ATS administrator must store and sign certificates for authenticated agent software developers.

In addition, there are new business roles in the future scenario of commercially available ATS services, perhaps including dedicated agent brokers. We have enabled this new business role by implementing an object relating agent brokers and their agents. This object maintains references, deducts brokerage fees, and supplies data for notification services. For security reasons, the agent broker object is placed in the same execution environment as the ATS. The only agent manipulation granted the object is the killing of an agent thread, should this become necessary.

## 4.2. Logs

The ATS administrator must monitor the actions of all agents on the ATS, and activity logs are therefore needed. These logs are likely to be processed only automatically, but in case of system failure or suspected illicit agent action, manual inspection may be required. For this reason, the responsibility for logging should not be distributed, but should be the responsibility of the ATS administrator. Each agent should be allowed read and write access to its own action logs, since logs provide interesting information on top of the generally available trade statistics. Logged information could be used for machine learning, which could occur offline or online, depending on the agent business logic. An excerpt from a log of a simple agent, to be discussed further in the next subsection, is shown in Fig. 5. The full source code of the agent, as well as the full log, has been published [17]. Since all stakeholders are potentially interested in parsing the log, it is in XML format. For instance, the ATS administrator might like to find the agent responsible for some illegal action on the ATS. Analogously, an agent broker might seek to attribute errors to the ATS implementation, using logs as evidence. The error log of Java exceptions and String objects is kept separate from all other logged data.

## 4.3. se.sics.ats.agent

The structurally designed agent shell packages are intended as support for ATS agent development, and their JavaDoc is publicly available [18]. We give an abstract overview here of the low coupling design, so that the role of the shell in our implementation of the ATS is made clear. Agents extend the abstract

```xml
M. Boman, A. Sandin / Decision Support Systems 42 (2006) 318–327

<logfile>
<status invoked_by="start" date="20030211" time="14:01:01:239">
    <portfolio total_value="0.0" />
    <account value="10000.0" />
</status>

event type="getAsk" date="20030211" time="14:01:01:259">
    <variable name="symbol" value="SICS" />
    <variable name="returned_value" value="100.0" />
</event>

event type="subscribe" date="20030211" time="14:01:01:269">
    <variable name="property" value="SP_ASK" />
    <variable name="symbol" value="SICS" />
</event>

<event type="property_changed" date="20030211"
    time="14:01:18:364">
    <variable name="property" value="SP_ASK" />
    <variable name="symbol" value="SICS" />
    <variable name="value" value="101.0" />
</event>

<event type="createOrder" date="20030211" time="14:01:18:374">
    <variable name="order_id" value="OID-Daytrader1044968478364" />
    <variable name="property" value="ORDER_TYPE_BID" />
    <variable name="creation_date" value="20030211 14:01:18:364" />
    <variable name="price" value="101.0" />
    <variable name="symbol" value="SICS" />
    <variable name="quantity" value="10" />
</event>

<event type="enterOrder" date="20030211" time="14:01:18:374">
    <variable name="order_id" value="OID-Daytrader1044968478364" />
    <variable name="property" value="ORDER_TYPE_BID" />
    <variable name="creation_date" value="20030211 14:01:18;364" />
    <variable name="price" value="101.0" />
    <variable name="symbol" value="SICS" />
    <variable name="quantity" value="10" />
</event>

<event type="orderClosed" date="20030211" time="14:01:18:384">
    <variable name="order_id" value="OID-Daytrader1044968478364" />
    <variable name="property" value="ORDER_TYPE_BID" />
    <variable name="creation_date" value="20030211 14:01:18:364" />
    <variable name="price" value="101.0" />
    <variable name=symbol" value=SICS" />
    <variable name=symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'symbol'shtml>
```  
Fig. 5. Excerpt from a log of Daytrader, a simple agent running on the ATS.

TradeAgent class (see Fig. 6), which handles all ATS interaction, including the final methods initialize and start, invoked by the ATS [32]. The agent (SubAgent) gets information about stocks through various get methods, or by subscribing to stock changes (cf. Fig. 5). The latter alternative is the one used by most non-artificial stock traders today, and so subscription procedures and costs have already been carefully designed at most exchanges.

![](/api/attachments/UWE97E9K/fulltext/images/a398fc7bc7871173d5a9a39f042ec110cb1b9b5e4c281e24d5cea8a934220799.jpg)  
Fig. 6. The agent shell package structure.

Agents place orders using the Order object, and its interface OrderListener [32]. An order is created by calling the method createOrder. The OrderListener then implements the methods orderCancelled and orderClosed, which result in account updates and logging, as demonstrated in Fig. 5. The account and portfolio maintenance should in any commercial implementation of the ATS be handled by standard F/X middleware. Similarly, the AgentBroker has only minimal functionality in this version of the ATS.

## 5. Conclusions and further research

We have described a proof-of-concept implementation of a running agent trade server, which has already served as a blueprint for future implementations intended for live use on a real financial exchange. We have also constructed and described an agent shell, currently in use for server implementation of agents of increasing complexity. Experimental agent developers are also providing the first anecdotal evidence of the quality of our implementation. We intend to engage more developers before a formal evaluation is made, but recently completed work has shown that the size of an agent with a sophisticated business logic is manageable [15]. Analyses of robustness, resilience and real-time aspects of the ATS and of more advanced ATS agents have limited value until commercial adoption, or at least limited live tests, can be made. That said, we have already implemented various demonstrators for notifying services, to be used for presenting agent logs to the agent brokers and agent owners [27]. While professional trading is a highly collaborative activity [14], the agents in our set-up model each other only in a weak sense, based solely on their bidding. There are several multi-agent system aspects that deserve attention, such as multiple agent submission for teamwork, or even for manipulative purposes. Finally, the effects on the entire financial system as a result of wide adoption of agent trade deserve investigation.

## Acknowledgments

The authors would like to thank Jesper Johansson and Michael Poijes, who wrote the first agent shell and some of the server software, and kindly provided log data. David Lyb<sup>7</sup>ck and Ulf Essler contributed important comments and fruitful discussions. The Vinnova project TAP on accessible autonomous software provided the authors with the time required for this study.

## References

[1] W.B. Arthur, Out-of-equilibrium economics (unpublished draft) (Aug. 2004).

[2] K. Bertels, M. Boman, Agent-based social simulation in markets, Electronic Commerce Research 1 (1–2) (2001) 149–158.

[3] M. Boman, M. Bylund, F. Espinoza, M. Danielson, D. Lyb<sup>7</sup>ck, Trading agents for roaming users, Proc. Tokyo mobile roundtable, Hitotsubashi Univ., Tokyo, 2002, CD-rom.

[4] M. Boman, S. Johansson, D. Lyb<sup>7</sup>ck, Parrondo strategies for artificial traders, in: N. Zhong, J. Liu, S. Ohsuga, J. Bradshaw (Eds.), Intelligent Agent Technology, World Scientific, Singapore, 2001, pp. 150–159.

[5] J.-P. Carbonnier, OMX patent may threaten algo trading, Dealing with Technology 1 (27) (2004).

[6] E.K. Clemons, B.W. Weber, Restructuring institutional block trading—an overview of the OptiMark system, Proc. HICSS 6—organizational systems and technology, IEEE Computer Society, 1998, pp. 301– 310.

[7] J.B. De Long, A. Shleifer, L.H. Summers, R. Waldmann, The survival of noise traders in financial markets, Journal of Business 64 (1991) 1– 19

[8] J. Doyne Farmer, S. Joshi, The price dynamics of common trading strategies, Journal of Economic Behavior and Organ ization 49 (2002) 149– 171.

[9] F. Espinoza, Individual service provisioning, Ph.D. thesis, Dept of Computer and Systems Sciences (Stockholm Univ, 2003).

[10] M. Fan, J. Stallaert, A.B. Whinston, A web-based financia trading system, IEEE Computer 32 (4) (1999) 64 – 70.

[11] C. Gerber, J. Teich, H. Wallenius, J. Wallenius, A simulation and test of OptiMark’s electronic matching algorithm and its simple variations for institutional block trading, Decision Support Systems 36 (2004) 235–245.

[12] A. Greenwald, The 2002 trading agent competition—an overview of agent strategies, AI Magazine 24 (1) (2003) 83–91.

[13] V. Hauser and J. Orrhult, Network monitoring for networking agents, Master’s thesis, report No. 02-01-DSV-SU, Dept of Computer and Systems Sciences (Stockholm Univ, 2002).

[14] C. Heath, M. Jirotka, P. Luff, J. Hindmarsh, Unpacking collaboration—the interactional organisation of trading in a city dealing room, in: G.D. Michelis, C. Simone, K. Schmidt (Eds.), Proc. ECSCW’93, Kluwer Academic, 1993, pp. 155– 170.

[15] D. Hilmersson, SmartTrader—implementing an advanced business logic agent for agent trade servers, Master’s thesis (Mid-Sweden Univ, 2004)

[16] P. Jefferies, M. Hart, P. Hui, N. Johnson, From market games to real-world markets, European Physical Journal. B, Condensed Matter Physics 20 (1) (2001) 493–501.

[17] J. Johansson, M. Poijes, Agent shell for stock market systems, Master’s thesis, report No. 03-26-DSV-SU, Dept of Computer and Systems Sciences (Stockholm Univ, 2003).

[18] J. Johansson, M. Poijes, DayTrader Agent javaDoc, http:// www.dsv.su.se/\~mich-poi/trade<sup>\_</sup>agent/javadoc/ (2003).

[19] B. LeBaron, Agent-based computational finance—suggested readings and early research, Journal of Economic Dynamics and Control 24 (2000) 679– 702.

[20] M. Lettau, Explaining the facts with adaptive agents—the case of mutual fund flows, Journal of Economic Dynamics and Control 21 (1997) 1117– 1147.

[21] J. Long, M.J. Yuan, A.B. Whinston, Securing a new era of financial services, IT Professional in Finance 5 (4) (2003) 15– 21.

[22] W. A. Lupien, J. T. Rickard, Crossing network utilizing optimal mutual satisfaction density profile, US Patent No. 5689652 (1997).

[23] T. Lux, Herd behaviour bubbles and crashes, Economic Journal 105 (1995) 881–896.

[24] T. Lux, M. Ausloos, Market fluctuations I: scaling, multiscaling and their possible origins, in: A. Bunde, J. Kropp, H.-J. Schellnhuber (Eds.), Science of Disaster—Scaling Laws Governing Weather, Body, Stock-Market Dynamics, Springer-Verlag, 2002, pp. 373– 409.

[25] T. Lux, M. Marchesi, Scaling and criticality in a stochastic multi-agent model of a financial market, Nature 397 (1999) 498– 500.

[26] D. Lyb<sup>7</sup>ck, M. Boman, Agent trade servers in financial exchange systems, ACM Transactions on Internet Technology 4 (3) (2004) 329–339.

[27] S. Nylander, M. Bylund, M. Boman, Mobile access to realtime information—the case of autonomous stock brokering, Personal and Ubiquitous Computing 8 (2004) 42 – 46.

[28] OMX, An automated semi-deterministic trading system, filed to US Patent and Trademark Office (March 2002).

[29] R.G. Palmer, W.B. Arthur, J.H. Holland, B. LeBaron, P. Tayler, Artificial economic life—a simple model of a stockmarket, Physica D: Nonlinear Phenomena 75 (1–3) (1994) 264– 274.

[30] J. Rust, J.H. Miller, R. Palmer, Characterizing effective trading strategies—insights from a computerized double auction tournament, Journal of Economic Dynamics and Control 18 (1994) 61–96.

[31] R. Sales, First Europe, now the world, wall street and technology, http://www.wallstreetandtech.com/showArticle. jhtml?articleID=14703470 (August 2001).

[32] A. Sandin, AgentTradeServer javaDoc, http://www.sics.se/ \~sandin/ats/doc/ (2002).

[33] L. Tesfatsion, Agent-based computational economics—growing economies from the bottom up, Artificial Life 8 (1) (2002) 55– 82.

Magnus Boman is a professor in Intelligent Software Services at the Royal Institute of Technology. He also leads the Userware research laboratory at the Swedish Institute of Computer Science. Boman has published journal papers in computer science, mathematics, philosophy, physics, economics, law, and management. Application domains include decision analysis, decision theory, program trading, intelligent buildings, constraint programming and norms, conceptual modelling, complex systems analysis, time geography, interactive narratives, robot design, and mobile and ubiquitous computing. He helped start and is still on the organizing committee for the Mobility Roundtable Series, and serves on the editorial board for the Robotics and Autonomous Systems journal.

Anna Sandin has a masters degree in Computer Science. Research fields catching her attention are ubiquitous computing and trading agents. Sandin is currently working as a software designer at Ericsson AB.
