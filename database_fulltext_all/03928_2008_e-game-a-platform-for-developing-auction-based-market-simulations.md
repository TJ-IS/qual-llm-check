---
otero_id: 3928
otero_key: "SH5MSWPT"
title: "e-Game: A platform for developing auction-based market simulations"
authors: "Maria Fasli; Michael Michalakopoulos"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# e-Game: A platform for developing auction-based market simulations

Maria Fasli <sup>⁎</sup>, Michael Michalakopoulos

University of Essex, Department of Computer Science, Wivenhoe Park, Colchester, CO4 3SQ, UK

Received 14 February 2006; received in revised form 18 May 2007; accepted 10 June 2007 Available online 23 June 2007

## Abstract

Trading in electronic markets has been the focus of intense research over the last few years within Computer Science and Economics. This paper discusses the need for tools to support the design and implementation of electronic market simulations or games. Such games emulate real life problems and can be used in order to conduct research on market infrastructure, negotiation protocols and strategic behaviour. To this end, we present the e-Game platform which was developed to support the design, implementation and execution of market simulations involving auctions. How the development of market games is aided is demonstrated with an example game.

Keywords: Market simulations; Electronic markets; Auctions

## 1. Introduction

The deployment of agent-based and multi-agent systems for conducting business online has been the focus of intense research over the last few years.

Future electronic marketplaces have been envisioned as being populated by autonomous intelligent entities — software, trading, e-agents — which represent their owners and conduct business on their behalf. Unlike “traditional” software, agents are personalized, semiautonomous and continuously running entities [19]. Generally speaking, electronic exchanges involve three main phases: firstly potential buyers and sellers must find each other or meet in a marketplace, secondly they need to negotiate the terms of the transaction and, finally, they execute the transaction and the goods/monetary resources change hands. Agent technology can be used in all three phases, from matchmaking to negotiation and payment systems. As agents encode their users' preferences they can negotiate for goods and services on their behalf. Future e-markets are thus fully automated from end-toend: finding potential business partners, negotiating terms and conditions of transactions and contracts, signing and monitoring contracts, payment, and even dispute resolution will all be done automatically by software agents. In theory, the only time users become involved is in specifying their portfolios and preferences or stipulating their strategies.

But despite their increased popularity, the huge potential of agents and multi-agent systems remains largely untapped. The reasons for the slow uptake of agent technology, in particular with regards to e-commerce applications, are manyfold. Firstly, there is a lack of standardization that permeates the field of agents and multi-agent systems. This inevitably raises concerns as users would like to use standard and stable technologies.

Secondly, there are inherent issues with trust [10]. Trust becomes very important if an agent's actions can cause its user physical, financial, or even psychological harm [4]. Disclosing personal, financial or other sensitive information to an agent and delegating to it the task of conducting business on one's behalf involves a number of risks. Thirdly, although constructing agents to carry out single negotiation tasks is easy, developing flexible agents that can operate in highly dynamic and volatile environments that electronic markets are is non-trivial. For instance, developing trading agents to take part in auctions for a single good is relatively simple, but in reality customers or businesses may have to negotiate for a bundle of perhaps interrelated goods being traded in different auctions following different rules [1]. Developing agents that can compete in complex markets and participate in simultaneous auctions offering complementary and substitutable goods is difficult. This is further complicated by the fact that the successful performance of a trading agent does not only depend on its strategy, but on the strategy of the other agents as well. Designing efficient and effective bidding strategies is difficult since real world data about trading agents are hard to obtain.

This paper discusses one way that the last problem can be addressed. In particular, we advocate the need for tools to support the design and implementation of electronic market simulations or games for conducting research on market infrastructures, negotiation protocols and strategic behaviour. Given the increasing popularity of auctions for online negotiations, we present a platform that provides the facilities for developing electronic market games that involve auction protocols. The rest of the paper is organized as follows. First we discuss the motivation behind this line of work. The following section presents the architecture and the most significant features of the e-Game platform. Game development and the facilities provided by e-Game to aid this along with an example game are discussed next. A discussion of the related work with regards to electronic marketplaces and trading agent platforms follows. The paper ends with a discussion on further work and the conclusions.

## 2. Motivation

The shift from traditional markets to fully automated electronic ones where entities such as individuals, organizations and businesses are represented by software agents and conduct business on their behalf, alludes to a number of problems. The first fundamental problem is that of the infrastructure that is required in place in order for such electronic markets to be fully functional and enable participants first to find and then to interact with each other. The second problem is facilitating interactions among participants. In essence, this means identifying and deploying appropriate protocols or mechanisms that would enable participants to reach desirable outcomes. Unquestionably, there is no unique protocol that could be applied to all negotiation situations. Each domain has its own characteristics and therefore it is impossible to impose a unique protocol as the panacea for all negotiation situations. The third problem, is how to build efficient and effective trading agents and endow them with strategies that will enable them to participate and compete in highly complex and volatile electronic markets. The fourth problem has to do with the provision of appropriate legislative measures as users need to be assured that any legal issues relating to agents trading electronically are fully covered, just as they are in traditional trading practices [10].

Without doubt, designing and implementing electronic markets is a complex and intricate process [21]. Agents represent their users and strive to achieve their objectives, that is they try to maximize their utility without necessarily caring about the welfare of others or the system as a whole. In situations of strategic interdependence, if agents can take advantage of the mechanism they will, irrespective if this leads to inefficient outcomes in the market. Mechanism design explores such interactions among rational self-interested agents with the view of designing protocols such that when agents use them according to some stability solution concept (dominant strategy equilibrium, Nash equilibrium, mixed strategies Nash equilibrium), then desirable social outcomes follow [20,22]. Most attention in mechanism design has focused on centralized mechanisms: agents reveal their preferences to a central mechanism which then computes the optimal solution given these preferences. In addition, traditional mechanism design is underpinned by a set of assumptions [7] that may not be realistic for computational agents in complex environments.<sup>1</sup> The most crucial assumption is that agents are rational and hence can compute their complete preferences over all possible outcomes. Agents are also assumed to be knowledgeable: they know and understand the protocols and also abide by them. Another limiting assumption is that the society of agents participating in the mechanism is closed. Furthermore, the communication channels among agents are assumed to be faultless and in fact the communication costs are not taken into account. These assumptions are problematic, in particular, in the context of e-commerce being conducted by software agents since [7]:

• agents have bounded memory and limited computational resources;

• electronic marketplaces are open and dynamic environments in which agents may appear or disappear for a number of reasons;

• in such open markets with heterogeneous agents, semantic interoperation among all agents cannot be guaranteed;

• although highly desirable, a machine-understandable specification of all interaction protocols and rules cannot be taken for granted in an open environment;

• centralized mechanisms may be unable to compute the outcome because the problem may simply be intractable;

• communication channels cannot be guaranteed to be faultless and associated communication costs cannot simply be ignored.

Therefore, although traditional mechanism design offers us insights into designing protocols for agent negotiation, its applicability to complex scenarios is inherently limited. The complexity of electronic marketplaces may place them beyond the analytical power of mechanism design. But, even in seemingly well-understood environments, using simple protocols without prior careful design and experimentation, can unfortunately lead to expensive failures or inefficient outcomes, as the conduct of the 3G mobile phone licence auctions in some countries in Europe has amply demonstrated [15]. Hence, developing marketplaces without careful consideration and experimentation can be costly and carries high risks. Moreover, testing trading agents and strategies in real life complex marketplaces is difficult, impractical and also carries high risks. Users — individuals, organizations, businesses — need inexpensive and safe ways to evaluate the appropriateness and applicability of protocols in particular situations and the effectiveness and robustness of strategies.

One approach to alleviate these problems is to implement and experiment with market simulations. The intrinsic value of simulations in other domains such as medicine and military as well as in education is wellestablished and accepted. Using market simulations offers a number of advantages. Firstly, simulations allow the interested parties to test market mechanisms and strategies in a safe environment. An organization which considers adopting a particular auction protocol and creating an electronic marketplace can test its appropriateness in this particular domain by experimenting through simulation.

The behaviour of participants and their strategies in the marketplace can also be studied in simulations. The strengths and weaknesses of strategies can be assessed as well as the impact of using different strategies on the marketplace as a whole. The effectiveness of strategies under different market conditions can also be explored. Secondly, using market simulations is also a relative inexpensive means of testing protocols and strategies. When one considers the potential cost of using inappropriate strategies in a marketplace or a negotiation protocol that may be easy to manipulate in a particular situation, experimenting and testing using simulations can significantly reduce the risk of expensive or embarrassing failures. Thirdly, employing market simulations allows for the testing of different market settings and configurations and the testing of even extreme conditions and how these affect both the marketplace as a whole as well as individual participants. Extreme behaviours can also be simulated. In essence, simulations offer a powerful tool which together with formal analysis can offer us valuable insights into the workings of market infrastructures, the use of protocols as well as the effectiveness of strategies.

Using market simulations may offer the only way to actually approach these problems in a systematic way. Although enormous amounts of trading data are available in financial markets, information on the traders' strategies is not, whereas in other types of markets and newly created markets no data may be available. Guided first by theory and following a detailed analysis of a given domain, one can proceed to choose appropriate negotiation protocols and design and implement a market simulation, and finally verify the appropriateness of the protocols used through experimentation. The same applies to negotiation strategies.

Despite the fact that simulations are in general useful, there is an inherent limitation in developing and experimenting with simulations on one's own. The results of such experiments conducted by a single person or organization may lack the touch of realism, since the bidding strategies explored may not necessarily reflect diversity in reality. This is the central idea and major motivation behind the International Trading Agent Competition [24] which features artificial trading agents competing against each other in market-based scenarios. Currently two scenarios are available and run as part of the competition: the Supply Chain Management game and the Market Design game. Arguably, such efforts are invaluable, but ideally, we would like open-source platforms where market-based scenarios could be implemented and researchers have the opportunity to build and test their trading agents against those of others. Of course, one should not underestimate the problem of building a user base for such games. Nevertheless, platforms or tools that would allow researchers and developers to design and implement their own marketplaces are currently lacking. Our work aims to address this lack of tools.

Another motivation behind this line of work is its potential applications in education. Teaching intelligent agents and multi-agent systems involves covering a wide range of topics including architectures, coordination and cooperation as well as negotiation among agents. Using practical examples and providing realistic scenarios where agent technology could be applied is highly desirable. Ideally, we would like students or others that would like to be trained in this area to have a hands-on experience in an electronic marketplace. However, experimenting in real markets is not possible. The use of market simulations offers the only realistic alternative if one wants to provide students with the opportunity to practice. To this end, our work offers a configurable tool that can be used to enhance the students' learning experience by allowing them to put into practice principles taught and experiment with realistic scenarios. Instructors may develop games with a particular focus, whereas students can either make a contribution to the agent design or the design of games.

## 3. e-Game

e-Game (electronic Generic auction marketplace) is a configurable online auction server in which participants may be humans or software agents. It is a generic platform that can be extended to support many types of auctions. Additionally, e-Game is designed to support market simulations analogous to those of TAC [24] which can be designed and developed by third parties.

e-Game is based on a modular architecture separating the interface layer from the data processing modules and the database (Fig. 1). e-Game consists of the following major components. The e-Game package provides the functionality for both the Web and the Agent interfaces, since these two are merely a presentation layer for the same set of auction related commands (submitting bids, checking price quotes, etc.). The Game API is targeted towards the game developer who needs methods to schedule different auctions, generate different agent parameters, submit bids (when the game manager acts as the auctioneer for instance) and write the scores at the end of the game. Game Managers implement the rules of various market games that have been developed and run on the platform. The Auctioneer Processes implement the various auction protocols while the Scheduler is responsible for starting up auctions and games. The database is used to model the auction space (auction type, startup, closing time, clearing rules), as well as the user data (registration, user bids, auctions the user created). It also stores information regarding the market simulations (which game started which auctions, ids of players, scores). It provides fault tolerance, in that the events queue can be reconstructed if there is a problem with the Auctioneers or the Scheduler. Its modularity and expandability are further strengthened by adopting the object-oriented paradigm for its components. The platform has been developed in JAVA in order to gain the benefits of platform independence and transparency in networking communication and object handling.

## 3.1. Interfaces and scheduler

e-Game allows both users and software agents to participate in auctions and games and as such has two interfaces to the outer world: the Web and the Agent interfaces, similarly to [27].

![](/api/attachments/SH5MSWPT/fulltext/images/80b50c850ed513b0ae59de7d4fb12255fd96a1ffe81ae445b9815ebf52b92f08.jpg)  
Fig. 1. The architecture of e-Game.

The Web interface allows users to register, create new auctions using a number of parameters (auction type, quote generation, clearing and closing mechanism), submit bids, search based on a series of attributes (auctioned item, status of auction, user's participation in an auction) and view their profile.

The Agent interface provides agent developers the same functionality with the Web interface with respect to auctions plus an additional set of commands for participating in market games. Agents connect to the Agent interface using the TCP protocol and submit their commands using FIPA ACL messages [11,29]. A subset of the FIPA ACL performatives are used in e-Game to make requests (request: when an agent submits a bid), communicate the results of actions (inform: when e-Game informs an agent about the result of its bid submission) and refuse requests (refuse: when an invalid action has been requested). The content of the message follows the FIPA Semantics Language, which is formally defined in [11]. It is feasible however, to use a different contentlanguage, for example XML, by developing the appropriate parser and plugging it in the existing system. The purpose of adopting FIPA ACL as a communication language is twofold. First, FIPA ACL contributes towards common standards among different agent platforms — if agent technology is to become widely adopted, it is necessary for agents (their developers) to adopt a common communication protocol. Second, in an educational environment, FIPA ACL offers the opportunity to become familiar with certain issues related to agent communication. For every command an agent submits, e-Game returns an appropriate result together with a command status value that indicates the outcome of the command. The full set of commands is documented in the website.

The majority of functions that users and agents perform are identical and are implemented in a single package which is shared between the two interfaces. The advantage of such an approach is that both components can be easily extended with the minimum effort in terms of implementation and testing.

The Scheduler runs in parallel with the Web and Agent interfaces and is responsible for starting auctions, games and passing bids to the appropriate Auctioneer processes. The auctions can be scheduled by users or by a specific GameManager handler according to a market scenario's rules, whereas games are scheduled by users. The Scheduler has been designed to be fault-tolerant; if it is brought off-line for some reason, when it is restarted it can reconstruct its lists of events by looking into the database for pending events.

## 3.2. Auction support and implementation

Auctions are one of the oldest form of markets and some pinpoint their origin to Babylon in 500 BC. Nowadays all sorts of goods and services are being traded in auctions ranging from paintings to spectrum licences. With the advent of the World Wide Web, auctions have become extremely popular as the means for conducting consumer-to-consumer (C2C) negotiations. Auction sites such as eBay [8] have been reporting millions of dollars in transactions from auction sales. Auctions are also popular in business-to-business negotiations and have also been used by governments to sell spectrum and TV licences, rights to drill for oil and for privatizing government owned companies.

There are two self-interested parties in an auction: the bidders and the auctioneer. One of the main features of auctions is that the task of determining the value of a commodity is transferred from the vendor (auctioneer) to the market (bidders), leading to a fairer allocation of resources based on who values them most. Auctions can be used for the sale of a single item, multiple units of a homogeneous item as well as interrelated goods [9]. Typically, the conduct of an auction involves the following stages:

• Registration. Buyers and sellers register with an auction house.

• Bidding phase. The participants bid according to the rules of the particular auction protocol used. A bid indicates a bound on the bidders' willingness to buy or to sell a good.

• Bid processing. The auctioneer checks the validity of a bid according to the rules of the auction used and updates its database (manual or electronic).

• Price quote generation. The auction house via the auctioneer or by other means may provide information about the status of the bids. A bid quote is the highest outstanding effective offer to buy while an ask quote is the lowest outstanding effective offer to sell.

• Clearance (or Matching). Through clearance, buyers and sellers are matched and the clearing price (transaction price) is set.

• Transaction phase. The transaction takes place: the buyer pays and receives the good/service.

Auction protocols are generally classified depending on whether multiple buyers and sellers are allowed (single/double), the bidders have information on each other's bids (open/closed), the flow of prices (ascending/descending) and how the bidders form their valuations (private/common/correlated value). More complex auction formats allow participants to negotiate on more than one dimensions of a good or on multiple interrelated goods.

Among the most well-known single-side auctions are the English, Dutch, FPSB and Vickrey. The English auction is an open-outcry and ascending-price auction which begins with the auctioneer announcing the lowest possible price (which can be a reserved price). Bidders are free to raise their bid and the auction proceeds to successively higher bids. When there are no more raises the winner of the auction is the bidder of the highest bid. The Dutch auction is an open and descending-price auction. The auctioneer announces a very high opening bid and then keeps lowering the price until a bidder accepts it.

The FPSB (First-Price Sealed-Bid) and Vickrey (uniform second-price sealed-bid) auctions have two distinctive phases: the bidding phase in which participants submit their sealed bids, and the resolution phase in which the bids are opened and the winner is determined. In the FPSB auction the highest bidder wins and pays the amount of its bid, while in the Vickrey auction the higher bidder wins, but pays the second-highest bid.

One of the most commonly used double-side auctions is the Continuous Double Auction (CDA). The CDA is used in commodity and stock markets. Multiple buyers and sellers can participate in such auctions and a number of clearing mechanisms can be used. For instance, in the stock market, clearing takes place as soon as bids are matched.

e-Game supports the four basic single-side auction formats, single seller auctions as well as double auctions (Table 1). These basic types of auctions can be further refined by allowing the user to define additional parameters that include [28]:

• Price quote calculation: Upon arrival of new bids, at fixed periods or after a certain period of buy/sell inactivity.

• Auction closure: At a designated date and time or after a period of buy/sell inactivity.

• Intermediate clearing: Upon arrival of new bids, at fixed periods or after a certain period of buy/sell inactivity.

• Information revelation: Whether the price quotes and the closing time are revealed or not.

By changing the parameters of an auction such as closing time and the amount of information revealed regarding bids, the basic functionality of an auction can be modified. This in turn has an effect on the users' or agents behaviour.

Table 1  
Auctions supported by e-Game

<table><tr><td>Auction type</td><td>Sellers</td><td>Units</td><td>Buyers</td></tr><tr><td>English</td><td>1</td><td>1</td><td>Many</td></tr><tr><td>Vickrey</td><td>1</td><td>1</td><td>Many</td></tr><tr><td>FPSB</td><td>1</td><td>1</td><td>Many</td></tr><tr><td>Dutch</td><td>1</td><td>1</td><td>Many</td></tr><tr><td>Single seller</td><td>1</td><td>Many</td><td>Many</td></tr><tr><td>Double</td><td>Many</td><td>Many</td><td>Many</td></tr></table>

Auctions are carried out by the respective Auctioneer classes. Each Auctioneer is started by the Scheduler and implements a specific auction protocol. Therefore, there are as many Auctioneer classes, as the number of auction protocols supported by e-Game. Since all Auctioneers perform alike actions, they inherit the basic behaviour and state from a BasicAuctioneer class. Once an auction starts, the BasicAuctioneer class is responsible for generating the auction's events based on the choices the user made during the setup. At any moment in time there may be a number of similar or different classes of active Auctioneers, each one handling a different auction.

The implementation of these auctions is based on the Mth and (M + 1)st price clearing rules. The clearing rules for the auctions are just special cases of the application of the Mth and (M + 1)st clearing rules. However, much depends on the initial set up performed by the user. For instance to achieve a chronological order clearing in an auction one can set up the intermediate clearing periods to take place as soon as a bid is received and thus the parameterized auctioneer will attempt to perform intermediate clearings upon the arrival of a new bid. As in classical chronological matching, if a portion of the bid cannot transact, it remains as a standing offer to buy (or sell). The implementation of the Mth and (M+ 1) st clearing rules uses ordered lists.

A recent addition to e-Game is the support for multiattribute auctions. The implementation of this type of auction differs from the single and double-side formats. The scoring of each attribute can be determined either by using a built-in evaluator (a class implementing a simple interface), or writing a new one. Built-in evaluators can be used to assign a score to an attribute based on: a) its value (e.g. price); b) its proximity to a target-value (e.g. delivery date); c) particular values that are preferred to others (discreet values with predefined scores). Once all attributes of a bid are evaluated and assigned a score, a weighted sum assigns a utility to the bid. The algorithm that is used to determine the winner is based on [3].

## 3.3. Game Manager

The GameManager class provides the basic functionality for initializing, controlling and evaluating the progress and the outcome of a market game. Within the GameManager, a game can be divided into three distinct phases:

(1) In the initialization phase, initial resources and future auction events are generated. The resources are allocated to the agents via the TCPServer and the auction events are placed in the Scheduler 's event list.

(2) In the main phase, the various aspects of the game are controlled in an agent-like manner. This means that the developer can embed certain market behaviour in their GameManager serving the scenario's purposes. For example, it may be appropriate to ensure a ceiling in the prices of some auctions, or buy goods for which agents show no preference.

(3) In the closing phase, the GameManager calculates the scores of the participating agents, and stores the results in the database.

Each game may support an arbitrary number of participating agents. If this number is not matched in a game, the GameManager can fill in the slots with dummy agents which are provided for each game by the developer.

## 4. Developing market simulations

The distinguishing feature of e-Game as an auction platform is that it supports the design, development and execution of market simulations or games that involve auctions analogous to those of the Trading Agent Competition. In essence, e-Game enables developers to implement self-contained market scenarios which are executed as independent components by the platform.

Market simulations can be classified into three categories [12]:

(1) Primitive markets: buyers and sellers interact directly with each other and there are no intermediaries.

(2) Facilitated markets: middle agents such as auctioneers, banks etc. are present in the market to facilitate interactions between buyers and sellers.

(3) Regulated and embedded markets: there are regulator agents whose role is to control the interactions among agents having in mind the social welfare and not only the welfare of individual agents. There may be agents that vary some variables such as availability of goods in the market and interest rates such that they affect the behaviour of others.

We concentrate in the latter two types of market simulations as we are interested in markets with various types of middle agents and how interactions between buyers and sellers can be facilitated. It is the developer's responsibility to ensure that a game is realistic, fair and nontrivial. Transparency is enforced by publishing the logfiles and auction outcomes. When designing a new market simulation, a developer should consider the following issues:

• Realism: The more realistic the auction scenario is, the more comprehensible it will be to the people who wish to develop agents to participate in it. Ideally, the auction-based market scenario should describe a realistic situation, which may be encountered in everyday life (holiday planning, buying interrelated goods, scheduling of resources).

• Strategic challenge: the game should present difficult strategic challenges that artificial agents may encounter and which require strategic reasoning.

• Efficient use of e-Game: Ideally, the game should not be based on a single type of auction: there is range of auctions to choose from which can be further parameterized. Using different types of auctions raises more challenges for the participants, who will have to lay out different strategies depending on the auction type and the information available at run time.

• Fairness with regards to specifications: In a market simulation different agents with most probably different strategies will try to accomplish a certain goal. Though, in principle, the goal will be similar for every agent (for example, provide a holiday package conforming to the client's preferences), the achievement of individual goals will give different utilities for each agent. One should consider specifications that give everyone the opportunity to achieve the maximum utility.

• Fairness with regards to agent design: Agents with a more appropriate bidding strategy should manage to achieve a better outcome, than agents with “naive” and “simplistic” strategies. When “naive” strategies actually represent corresponding actions in real life (for which people can actually reason such as tit-fortat outperforming more complex strategies), this prerequisite does not hold. However, the purpose of introducing this requirement is that there should not be any flaws in the market game that would allow non-realistic strategies to outperform rational ones.

• Computational efficiency: The handler of an auction game should have the ability to operate in a real-time manner. Ideally, there should not be any algorithms that take a long time to run, especially at critical time points. However, such algorithms could be used at the end of the game when an optimal allocation may be required and scores have to be calculated.

• Communication efficiency: As little communication as possible should be required in order to reach a desirable outcome.

Since e-Game allows both users and software agents to join auctions, games which enable humans to participate alongside software agents can be developed. Such experiments may be run in order to draw comparisons between humans and software agents with respect to laying out a strategy to maximize utility. Moreover, games with human participants can be run to test selected predications of economic and game theory and psychology and the effects of particular mechanisms and conditions in the market on participants and their strategies [6].

## 4.1. Game development

Game development is simplified by extending the GenericGame class that is provided by e-Game. Developers need to be familiar with the Java programming language and provide the implementation for a number of processes in the form of methods that are part of a game. During the design stage, the developer has to describe the game specification which includes the set up of the environment in terms of duration, objectives, number of agents, initial information provided to agents, auctions and their set up, and utility functions. Broadly speaking, the implementation of a game involves the following phases:

• Generation of parameters. In this phase of the game, a number of parameters may be generated which may include for instance client preferences, initial endowments, other information regarding the state of the market, scheduled auctions, availability of goods and other resources and any other data the developer wants to communicate to each agent in the beginning of the game. The agents are responsible for retrieving this information and using it in their decision making.

• Execution. e-Game acts as the auctioneer and runs the auctions that have been set up as part of the game and it may also simulate other entities in the market. Agents are allowed to submit bids according to the rules of the game. Information is revealed according to the parameters specified in the setup. The agents are responsible for retrieving information on the status of their bids and auctions and making decisions accordingly.

• Score calculation. Success is usually measured in terms of a utility function, while clearly, the performance of an agent depends on its strategy. The utility function along with appropriate methods to calculate this for the agents have to be provided by the developer. At the end of a game and based on the goods obtained and other information (i.e. client preferences, penalties), e-Game calculates and publishes the score for each agent.

The developer can also provide a sample agent that the participants can use as the basis to build on. This can also act as a “dummy” to fill in one or more of the available player slots when a game runs and not enough players have registered for playing. Finally, the developer may also provide an applet to be loaded at runtime which graphically represents progress during the game, so that participants and also others can observe it.

In order to integrate a new game into the e-Game platform one needs to provide the class file, together with an XML file that describes general properties of the game such as the name of the game, the name of the implemented classes (game, applet), a short description for the game, its duration in seconds, the number of allowed participants and the resources (items) that the game uses. This information is then parsed by the GameImporter application and is stored in the database. Users can browse the website and view all the installed games, together with appropriate links to schedule new instances, watch a current game and view previous scores. When a new game is scheduled, the Scheduler receives the corresponding event and at the appropriate time starts the user defined GameManager class in a different JVM (Java Virtual Machine). At the end of a game, participants can view scores and resources obtained by each agent.

When taking into account the time and effort it takes to develop a new game two aspects need to be considered. Firstly, the design phase, where the developer needs to decide what the game will be about (e.g. a game where the agents compete for complementary items, a game where agents mostly interact with each other in double auctions), and secondly, the development phase, which may also include a simple dummy agent, and a monitoring applet. The design phase is a crucial one, as one has to think of an interesting scenario and then come up with appropriate parameters to define the game (number of players, available goods, number and types of auctions). A fairly simple market scenario can usually be implemented in about 2000 lines of code, a dummy agent in 500–900 lines and a monitoring applet in 500–1000 lines. The time it takes for development depends on the skills of the developer, however, it must be noted that after the development of one game, the time required to develop subsequent games is reduced as a result of code re-use.

(a)

<table><tr><td>Client</td><td>MB2</td><td>MB3</td><td>C2</td></tr><tr><td>1</td><td>130</td><td>160</td><td>245</td></tr><tr><td>2</td><td>120</td><td>180</td><td>275</td></tr><tr><td>3</td><td>145</td><td>200</td><td>220</td></tr><tr><td>4</td><td>110</td><td>190</td><td>285</td></tr><tr><td>5</td><td>118</td><td>175</td><td>263</td></tr></table>

(b)  
![](/api/attachments/SH5MSWPT/fulltext/images/c6173d97ae055e2a02d5cad02449a2da1f41880f11b8b23ba89c33e1e0169751.jpg)  
Fig. 2. The CMG game: (a) example of client preferences, (b) auction schedule.

## 4.2. An example game

In this section we will briefly discuss an example market game (note: this game has been developed for teaching purposes) to provide the reader with an idea of the type of market simulations that can be created on e-Game. In the Computer Market Game (CMG) six supplier agents compete against each other in order to provide fully assembled PCs to each of their five respective clients. For simplicity, there are only three types of components that are necessary to construct a properly working PC: a motherboard, a case and a monitor. There are three types of motherboards, each one bundled with CPUs of 1.0 GHz (MB1), 1.5 GHz (MB2) and 2.0 GHz (MB3). There are two types of cases, the first with a DVD player (C1) and the second with a DVD/RW drive (C2). There is only one type of monitor.

In the beginning of the game each agent receives its clients' preferences in terms of a bonus which each client is willing to pay to upgrade to a better PC configuration (i.e. using components MB2, MB3 or C2). An example of preferences for an agent j is given in Fig. 2 (a). Accordingly, the first client of agent j offers 130 units for motherboard MB2 and 160 for the MB3 one. For obtaining the better case (C2) the client offers 245 units. The bonus values are generated in the following ranges: $\mathrm { M B 2 } = [ 1 0 0 . . 1 5 0 ] , \mathrm { M B 3 } = [ 1 5 0 . . 2 0 0 ] , \mathrm { C 2 } = [ 2 0 0 . . 3 0 0 ] .$

The various components are available in limited quantities (Table 2) and are traded in auctions during the 9 minutes that the game lasts. Fig. 2 (b) illustrates the auctions' schedule; the dotted part of the lines indicates that the auctions may close anytime during that period, but the exact closing time is not revealed to the agents. An agent's success in this game depends on the satisfaction of its clients. An individual client i's utility (CU<sub>i</sub>) is:

$$
\mathrm{CU} _ {i} = 1 0 0 0 + \mathrm {MB\_Bonus} + \mathrm {C\_Bonus}
$$

The agent obtains 1000 monetary units for each client allocated an assembled PC plus any bonus for upgrading to a better motherboard or case. If no completed PC is allocated to a client, then the utility is 0. For any components bought surplus to requirements, the agent pays a penalty which is perceived as a storage cost and is determined at the beginning of the game as a random value in [150..300]. An agent's utility function is then defined as follows:

$$
\mathrm{AU} = \sum_ {i = 1} ^ {5} \left(\mathrm{CU} _ {i}\right) - \text { Expenses } - \text { Penalties }
$$

In creating a strategy for this game, one has to take into account that customers give different bonuses for upgrading to better components, but the availability of components is limited. Hence, prices in auctions may vary depending on the competition. Moreover, on failing to acquire a particular good, one may have to consider switching auctions and bidding for alternative goods, but the timing of the auctions is critical. Clearly, an agent should attempt to provide a PC to each one of its clients or to as many as possible, while at the same time trying to minimize costs. There are obvious interdependencies between goods, as a complete PC requires three components. Critically, an agent's success, does not only depend on its own strategy, but that of the other agents too; albeit an agent does not have any means of knowing the identity of the other players or monitoring their bids.

Table 2  
Component availability and auctions

<table><tr><td>Component</td><td>Quantity</td><td>Auction type</td></tr><tr><td>MB1</td><td>17</td><td>Mth Price</td></tr><tr><td>MB2</td><td>8</td><td>Mth Price</td></tr><tr><td>MB3</td><td>5</td><td>Mth Price</td></tr><tr><td>C1</td><td>20</td><td>Mth Price</td></tr><tr><td>C2</td><td>10</td><td>Mth Price</td></tr><tr><td>Monitor</td><td>30</td><td>Continuous single seller</td></tr></table>

![](/api/attachments/SH5MSWPT/fulltext/images/55c4184609b557a8ff0067684f3f645b36ea26d97513adbe7343ac0c07b33c5b.jpg)  
Fig. 3. The CMG game applet.

The original version of the CMG game did not include any penalties. In the process of using the game with a group of students who had to develop agents as part of their coursework, we discovered that a significant number of agents were buying more than they needed in an effort to deprive the market of various goods and therefore lower the utility of the others. To this end, we extended the agent's utility function to account for penalties in the form of storage costs for extra components.

The implementation of the above scenario includes an XML file describing the general properties of the game (names of game and applet classes, number of players, duration of the game, auctioned resources), together with the appropriate classes. A user-defined GameManager schedules the auctions at the beginning of the game by implementing the method startupGame and using the scheduleAuction methods. The initial client preferences are generated by implementing the method generateParameters. The utility of each agent at the end of the game is determined by examining the winning bids for each auction/agent. Finally, any language resources used are freed-up in the closeGame method. To complete the development of the game, one may choose to write an applet to enable users to view their agents' progress, as well as a “dummy” agent which would be used to fill in empty slots. The applet for CMG is illustrated in Fig. 3. A number of games have been developed based on the e-Game infrastructure by us but also by students. The games are publicly accessible from the website<sup>2</sup>.

## 5. Related work

Among the first efforts to create electronic marketplaces was Kasbah [5]. Kasbah allowed users to create personalized buyer and seller agents that could trade goods on their behalf through a number of parameters which included:

• desired date to buy (sell) the good by;

• desired price that the user would like to buy for (sell) the good;

• highest (lowest) acceptable price, which represented the highest (lowest) price that the user would be willing to pay (accept) for the good.

Users controlled the agents' behaviour by specifying their “strategy” in terms of a price-raise or price-decay function for buyer and seller agents respectively. A price-raise (price-decay) function specified how the agent would raise (lower) its price over time and could take three possible forms: linear, quadratic and cubic. Users were only able to create agents based on the “templates” provided by Kasbah and could not implement new functionality or agents in different languages. The marketplace had the role of the facilitator among agents. Once an agent posted an advert for selling a good, the marketplace would return a list of buyers that were interested in the same good. Kasbah would also notify the respective buyers that a new seller had entered the market. Interested parties would then communicate and negotiate deals directly. Users had the final say in authorizing the deals that their agents had previously reached.

MAGMA was another prototype electronic marketplace [25]. Unlike Kasbah, the idea behind MAGMA was to provide the necessary infrastructure and services for building virtual marketplaces such as banking, advertising and mechanisms for secure payments and transportation of goods. The MAGMA marketplace consisted of trader agents, an advertising server, a relay server and a bank. The trader agents' role was to engage in negotiations to buy and sell goods and services. The advertising server provided advertising and retrieval services while the relay server facilitated communication between the different entities in the system. The negotiation mechanism used in MAGMA was the Vickrey auction (second-price sealedbid). In contrast to Kasbah, agents in MAGMA could be written in potentially different languages as long as they complied with the MAGMA API.

AuctionBot was a flexible and scalable auction server capable of supporting both human and software agents, which was implemented at the University of Michigan to support research into auctions and mechanism design [27]. It included a Web interface that allowed users to create, monitor and participate in auctions via web forms and a TCP/IP interface that allowed software agents to connect and participate in auctions. The submitted bids were stored in a database while a scheduler (daemon process) was used to continually monitor the database for auctions that had events to process or bids to verify. An auctioneer process would load the auction parameters and the set of current bids from the database and would then validate bids as necessary and could do one clear and/or one price quote each time it run. A number of auctions were implemented and the system was capable of running many auctions in parallel. Auctions could be parametrically defined (closing time, timing of clear and/or quote events etc.) offering great flexibility. Information in terms of price and bid quotes could be provided depending on the auction setup. Information about past transactions could be optionally revealed. The Mth and (M + 1)st price rules were used as the basis for all auctions and their implementation was based on the 4-heap algorithm [26].

The Trading Agent Competition [24] is a non-profit organization whose aim is to promote research into trading agents and electronic markets by providing a platform for agents competing in well-defined market games with an emphasis on developing successful strategies for maximizing profit in constrained environments. The competition has been running since 2000 and for the first three years it was based on the AuctionBot infrastructure. Since 2003 the underlying infrastructure for the games and the competition has been provided by a team of researchers at the Swedish Institute of Computer Science. Currently, there are two games: the supply chain management (SCM) game and the more recent Market Design (CAT) game (introduced in 2007). The former simulates a supply chain management environment, while in the latter agents are brokers whose goal is to attract potential buyers and sellers as customers, and then to match these. Although the TAC servers are to some extent configurable, this is limited to defining certain parameters — there are no provisions for developing new games in a systematic way.

Arguably, along the first attempts to construct and experiment with an agent-based financial market framework is the Santa Fe Artificial Stock Market Model [2,16]. Other approaches to electronic marketplaces and financial exchange systems include the Agent Trade Server [18], and the Fishnarket [23]. In [12], another approach to developing e-commerce simulation games which builds on and extends the Zeus framework is presented.

The most important feature of e-Game and what distinguishes it as a platform from other efforts such as those described above is that it provides independent developers the facilities to design, implement and run auction-based market simulations. Unlike JASA [14] for instance, e-Game does not simply provide the facilities for scheduling, running or conducting experiments on the use of strategies in standalone auctions. Individual users/ developers can write their own GameManager and define complete market scenarios together with accompanying applets and agents that can be inserted and run on top of the e-Game infrastructure. The development of these modules is completely separate from the rest of the system. By making use of existing classes and implementing simple interfaces, users can develop new games quickly. The process of integrating new games with e-Game is fully automated: since the user-developed classes implement certain (simple) interfaces and inherit from existing classes, e-Game can access these methods without needing to know the rest of the user-defined methods that implement the game's rules. Moreover, e-Game provides the facility of having humans participate in complex market simulations as well as humans playing against software agents. This may be useful in designing strategies and examining strategy efficiency and complexity [6]. One could study the benefits from using agents in complex markets in a systematic way. For example, in a simple game-scenario, a human may do better than an agent, but it would be interesting to pit humans against software agents and study what happens when the scenario gets more complicated (penalty points, allocation problems etc.). A version suitable for human users for the CMG game has already been developed and laboratory-based experiments have been run with three different groups of participants.

## 6. Concluding remarks

The deployment of software agents in electronic commerce would bring about significant advantages: it would eliminate the need for continuous user involvement, reduce the negotiation time and transaction costs and potentially provide for more efficient allocation of goods and resources for all parties involved. This paper discussed the need for tools to support the design and development of market simulations that could be used to conduct research on market infrastructure, negotiation protocols and strategies as well as for educational purposes. To this end, we described a tool that facilitates these.

e-Game is a generic auction platform that allows users as well as agents to participate in auctions and auction-based market games. The aim of the e-Game project is to offer the infrastructure for running complex market simulations and conducting experiments with different bidding strategies. As such, this paper serves as an invitation to agent researchers and developers to use the e-Game platform to develop and test their ideas.

Apart from using the platform for designing and running complex market experiments, it can also be used in teaching issues in negotiation protocols, auctions and strategies. Students can have a hands-on experience with a number of negotiation protocols and put into practice the principles taught. Currently e-Game is used in two courses on agents and multi-agent systems and forms the basis of coursework in which students have to implement agents for the CMG and other games.

e-Game has been extensively tested by users scheduling and bidding in a variety of auctions simultaneously. Two servers are currently in operation and so far more than 3500 instances of the CMG game in which six agents are connected have been scheduled and run. The individual auctions that e-Game can run do not have limits to the number of bids or bidders that they can accept. The TCPServer could practically support many agents, which could be participating in different games at the same time. The platform is in use by approximately 30 users every year (undergraduate and graduate students) who work either on the development of trading agents or the design and development of games.

There are a number of possible avenues for future development. In a fully automated marketplace, agents not only negotiate, but also undertake the task of discovering opportunities to conduct business. This aspect of automation can be achieved by extending the Agent Interface so as to provide the same functionality with the Web Interface; this would allow the agents to perform searches about the scheduled auctions or even set-up their own auctions. Another possible extension is to make games more dynamic by allowing agents to initiate auctions during a game and act as sellers of goods that they already own. Although e-Game's components were developed in Java, a web services interface can also be built that would allow game developers to have access to e-Game's API using the programming language of their choice. Finally, we are considering the possibility of introducing a rule-based specification as in [17] to describe complex market-based scenarios.

## Acknowledgement

An earlier version of this work appeared in Fasli M. and Michalakopoulos M. Designing and Developing Electronic Market Games. In Advanced Intelligent Paradigms in Computer Games, Baba, Jain and Handa (eds) © Springer–Verlag Berlin Heidelberg 2007.

## References

[1] A. Andersson, M. Tenhunen, F. Ygge, Integer programming for combinatorial auction winner determination, Proceedings of the Fourth International Conference on Multi-Agent Systems (ICMAS-00), IEEE Computer Society, Boston, MA, 2000, pp. 39–46.

[2] W.B. Arthur, J. Holland, B. LeBaron, R. Palmer, P. Tayler, Asset pricing under endogenous expectations in an artificial stock market, in: W.B. Arthur, S. Durlauf, D. Lane (Eds.), The

Economy as an Evolving Complex System II, Addison–Wesley Longman, Reading, MA, 1997, pp. 15–44.

[3] M. Bichler, The Future of e-Markets: Multidimensional Market Mechanisms, Cambridge University Press, Cambridge, 2001.

[4] T.W. Bickmore, J. Cassell, Relational agents: a model and implementation of building user trust, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI 2001), ACM Press, Seattle, WA, 2001, pp. 396–403.

[5] A. Chavez, P. Maes, Kasbah: an agent marketplace for buying and selling goods, Proceedings of the First International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology (PAAM-96), The Practical Application Company, London, UK, 1996, pp. 75–90.

[6] R. Das, J.E. Hanson, J.O. Kephart, G. Tesauro, Agent–human interactions in the continuous double auction, Proceedings of the Seventeenth International Joint Conference on Artificial Intelligence (IJCAI 2001), 2001, pp. 1169–1187.

[7] R.K. Dash, N.R. Jennings, D.C. Parkes, Computational-mechanism design: a call to arms, IEEE Intelligent Systems 18 (6) (2003) 40–47.

[8] eBay. See http://www.ebay.com/, 2006.

[9] M. Fasli, Agent Technology for e-Commerce, John Wiley and Sons, Chichester, 2007.

[10] M. Fasli, On agent technology for e-commerce: trust, security and legal issues, Knowledge Engineering Review 22 (1) (2007) 3–35.

[11] FIPA, Communicative Act Library Specification, 2002, See http:// www.fipa.org/specs/fipa00037/.

[12] M. Griss, R. Letsinger, Games at work-agent-mediated e-commerce simulation, Proceedings of the Fourth International Conference on Autonomous Agents (Agents 00), ACM Press, Barcelona, Spain, 2000.

[13] P. Hedström, R. Swedberg, Social Mechanisms: An Analytical Approach to Social Theory, Cambridge University Press, Cambridge, 1998.

[14] JASA, Java Auction Simulator API, 2007, See http://www.csc.liv. ac.uk/\~sphelps/jasa/.

[15] P. Klemperer, How (not) to run auctions: the European 3G telecom auctions, European Economic Review 46 (4–5) (2002) 829–845.

[16] B. LeBaron, W.B. Arthur, R. Palmer, Time series properties of an artificial stock market, Journal of Economic Dynamics and Control 23 (1999) 1487–1516.

[17] K. Lochner, M. Wellman, Rule-based specifications of auction mechanisms, Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS'04), IEEE Computer Society, New York, NY, 2004, pp. 818–825.

[18] D. Lybäck, M. Boman, Agent trade servers in financial exchange systems, ACM Transactions on Internet Technology 4 (3) (2004) 329–339.

[19] P. Maes, R. Guttman, A. Moukas, Agents that buy and sell: transforming commerce as we know it, Communications of the ACM 42 (3) (1999) 81–91.

[20] A. Mas-Colell, M.D. Whinston, J.R. Green, Microeconomic Theory, Oxford University Press, Oxford, 1995.

[21] D. Neumann, C. Weinhardt, Domain-independent eNegotiation design: prospects, methods, and challenges, Proceedings of the

13th International Workshop on Database and Expert Systems Applications (DEXA'02), IEEE Computer Society, Aix-en-Provence, France, 2002, pp. 680–686.

[22] D.C. Parkes. Iterative Combinatorial Auctions: Achieving Economic and Computational Efficiency. PhD thesis, University of Pennsylvania, 2001.

[23] J.A. Rodríguez, P. Noriega, C. Sierra, J. Padget, FM96.5 A Javabased electronic auction house, Proceedings of the Second International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology (PAAM-97), The Practical Application Company, London, UK, 1997, pp. 207–224.

[24] TAC, Trading Agent Competition, 2006, See http://www.sics.se/tac/.

[25] M. Tsvetovatyy, M.L. Gini, B. Mobasher, Z. Wieckowski, MAGMA: an agent-based virtual market for electronic commerce, Journal of Applied Artificial Intelligence 11 (6) (1997) 501–523.

[26] P.R. Wurman, W.E. Walsh, M.P. Wellman, Flexible double auctions for electronic commerce: theory and implementation, Decision Support Systems 24 (1) (1998) 17–27.

[27] P.R. Wurman, M.P. Wellman, W.E. Walsh, The Michigan Internet AuctionBot: a configurable auction server for human and software agents, Proceedings of the Second International Conference on Autonomous Agents (Agents 98), ACM Press, St. Paul, MN, 1998, pp. 301–308.

[28] P.R. Wurman, M.P. Wellman, W.E. Walsh, A parameterization of the auction design space, Games and Economic Behavior 35 (1) (2001) 304–338.

[29] Y. Zou, T. Finin, L. Ding, H. Chen, R. Pan, TAGA: Trading Agent Competition in Agentcities, Proceedings of the Trading Agent Design and Analysis Workshop Held in Conjunction with the Eighteenth International Joint Conference on Artificial Intelligence (IJCAI), 2003.

Maria Fasli is a Senior Lecturer in the Department of Computing and Electronic Systems at the University of Essex. She obtained her Ph.D. in Computer Science from Essex in 2000. Her current research interests lie in agents and their theoretical foundations and practica applications. She has published papers on logics for reasoning agents, formal models of multi-agent systems, trading agents, computational models of trust, web search assistants and web service discovery and composition. She is the author of “Agent Technology for E-commerce” (John Wiley and Sons, 2007). Her interests extend to technologyenhanced learning and she was also awarded a National Teaching Fellowship by the HEA UK, for her innovative approaches to learning and teaching.

Michael Michalakopoulos received his B.Sc. in Information Engineering from the Technological Educational Institute of Athens, Greece, his M.Sc. in Software Engineering from Essex University, UK and his Ph.D. in Computer Science, also from Essex University. His research interests include computational trust, e-learning and negotiation protocols. He is currently a Research Officer at the Department of Computing and Electronic Systems at the University of Essex. He has worked on a variety of projects as a software developer and system analyst.
