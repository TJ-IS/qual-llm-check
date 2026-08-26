---
otero_id: 21778
otero_key: "3RAKP769"
title: "Interface agents: caveat mercator in electronic commerce"
authors: "Daniel G. Conway; Gary J. Koehler"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00046-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interface agents: caveat mercator in electronic commerce

Daniel G. Conway <sup>1</sup>, Gary J. Koehler )

Decision and Information Sciences, Warrington College of Business, Stuzin 351, UniÕersity of Florida, P.O. Box 117169, GainesÕille, FL 32611-7169, USA

Accepted 18 August 1999

## Abstract

Electronic commerce has opened new opportunities for buyers and sellers. Consumers can do things in an on-line environment that are simply not possible in face-to-face transactions. In this paper, we push this observation by examining and using a new type of software agent to convert merchant interfaces into middleware thus enabling one to assess and optimize their interactions with all the computing support available in today’s Decision Support System DSS environments.Ž . q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Software agents; Internet gaming; Agent blocking; Software interfaces

## 1. Introduction

Electronic commerce has opened new opportunities for buyers and sellers. Buyers have on-line search capabilities for finding products and services, for comparing prices and for ease of purchase. Sellers can reach and service more customers at lower costs and provide on-line support. However, anyone can easily start an electronic enterprise — both legitimate companies and others. As a result, many consumers have concerns about vendor viability, trust-worthiness of the companies and quality of products or services. Most already worry about secure transactions. As a result, many buyers have taken a caÕeat emptor — buyer beware — approach to electronic commerce.

We explore the converse issue — the issue of caÕeat mercator — seller beware. Consumers can do things in an on-line environment that are simply not possible otherwise. In an on-line environment, consumers have computing resources not normally available in face-to-face transactions. Financial investors have long known this — computers can monitor prices across markets and find arbitrage opportunities that would be impossible to spot, to then compute optimal responses and to execute actions within the brief windows of opportunity available.

A more pertinent example of caveat mercator is Andersen Consulting’s BargainFinder agent 2 . Bar-<sup>w</sup> <sup>x</sup> gainFinder searched a number of CD outlets on the Internet locating the best price of a desired item. Eventually a number of these vendors realized their profitability was dropping and took measures to block BargainFinder’s interactions. This is a simple example of caveat mercator. The emerging Internet environment opened buyer opportunities not faced by real-world merchants. These opportunities resulted from inexpensive searching and comparison capabilities.

Although BargainFinder illustrates a caveat mercator situation, we wish to explore a more complex setting where computing and decision making resources are also employed. These tools enable an agent to discover hard-to-see opportunities — or opportunities never exploited when the tools could not be used or not used effectively. These may not be anticipated by merchants nor easily thwarted. BargainFinder was blocked by merchants who stood to lose. This blocking was easy since BargainFinder worked from a central site. Jango 16 circumvented<sup>w</sup> <sup>x</sup> this by working from user sites.

Typically software agents are long-lived, semi-autonomous, proactive, and adaptive. An ideal consumer agent would interact with a merchant’s agent to find goods, negotiate price, etc. These agents would have to learn and adapt to changing conditions while still striving towards the overall goals of their owner see Ref. 14 for a good survey of agentŽ <sup>w</sup> <sup>x</sup> usage in electronic commerce ..

Unfortunately, most on-line consumer-merchant interactions still require direct manipulation of an interface. We take this as a given and propose a software agent that knows how to interact with interfaces. This reduces any merchant application to middleware that can be manipulated in the same manner a human would manipulate it. More importantly, our agent can be endowed with Decision Support System Ž . DSS and AI capabilities in ways never anticipated by merchants.

This research proposes a software agent that works directly through a merchant’s web-site interface. This agent treats an e-commerce site as middleware and responds with mouse clicks, typed text, etc. just as a human might. We call this an interface agent. This behavior hides the software agent’s activities making it appear as if a human was dealing with the application. However, the software agent can easily bring to bear sophisticated information processing and decision-making tools.

We propose that our interface agent can exploit opportunities not present in face-to-face transactions. To test this hypothesis, we developed a prototype and used it in hundreds of thousands of transactions to exploit an opportunity not practical in similar, direct human interactions. Indeed, the very number of transactions undertaken would not have been possible by direct human interactions.

This study shows that an interface agent can seriously compromise a merchant’s business. Furthermore, we explore measures merchants might take to protect themselves. However, none of our proposals is fool proof. Our results indicate that caveat mercator is a serious consideration. Companies should understand this threat before launching an e-commerce business. This paper brings to light both new DSS opportunities made possible by an inter-Ž face agent and exposes the need for businesses to. understand and counter this IT-based threat.

In Section 2 we briefly review agent literature and propose our interface agent. In Section 3 we discuss our test environment, give relevant background information and describe our specific implementation. We tested this model in a real-world setting. Following a long tradition in Artificial Intelligence research, we focused on a gaming environment. The setting we chose to study was Internet Gaming. Besides being fun, it presented an environment that exhibited all the attributes we sought. In Section 4 we show the results of the usage of our software agent. Section 5 presents methods that merchants can use to block traditional unwanted agents. It is important to understand these tactics to see what advantages an interface agent provides. Surprisingly, these and many common security methods are impotent against interface agents. We present some possible steps merchants might employ against interface agents. Finally, in Section 6 we present our conclusion and directions for future research.

## 2. Software agents

An intelligent agent is a software entity that possesses some type of intelligence and performs autonomous operations for a human see Brenner et al. Ž <sup>w</sup> <sup>x</sup> 4 for example . Agents must interact with an envi- . ronment. This necessitates communication, cooperation and coordination. An agent is evaluated on its capability to learn, to goal-seek, to react to the environment, to provide autonomous behavior, and to move about a networked environment.

![](/api/attachments/3RAKP769/fulltext/images/50a1cc77386617f7dd8f0b9cf04ff3cbc6417419d7ef02252ba1a1f5ac2299f5.jpg)  
Fig. 1. Interface agent.

Many types of agents have been studied 4 . Infor-<sup>w</sup> <sup>x</sup> mation agents perform intelligent, directed searches Žsuch as BargainFinder 2 . Cooperation agents work<sup>w</sup> <sup>x</sup>. in multi-agent software and human environmentsŽ . Ž . often distributed to solve complex problems or to negotiate see, for example, Pinson et al. 18 .Ž <sup>w</sup> <sup>x</sup>. Transaction agents oversee the details of transactions including security, payments, trustworthiness and the like. Most electronic commerce applications include a transaction agent.

We propose an agent that knows how to communicate through other software interfaces see Fig. 1 . Ž . This aspect makes the agent’s activities indistinguishable from a human agent’s activities. Fig. 1 show, a software agent that works through an interface provided by a merchant. This interface may be a web page, a Java applet, a C<sup>qq</sup> or Visual Basic application or the like.

Consider the agent architecture shown in Fig. 2. The specific implementation we explored runs in Microsoft Windows environments and is discussed in the following. Under Windows, applications can be viewed as a hierarchical nesting of windows. Our interface agent determines the main window handle of the running target application and then parses Ž . through sub-windows, as required, navigating to components with which it needs to interact likeŽ buttons, text fields, icons, links, etc. We have also. programmed our agents to load an application complete with establishing an IP connection, loading a browser and then loading a web page. The agent then monitors the connection to assure continued connectivity.

![](/api/attachments/3RAKP769/fulltext/images/e6a8b16fcd71a721982013f90cc4e91f6bf093d0ad617f2dbf96589383658bbd.jpg)  
Fig. 2. Agent architecture.

The agent has sensors to discern the environment. As just discussed, one sensor monitors the connection. We use two other sensors. To sense the state of an application, our agent reads the bitmap image of the target window and uses various filtering and pattern recognition mechanisms to understand the information. A third sensor watches the arriving IP packets and watches for various patterns of interest. This is accomplished with a standard network monitor or sniffer that writes a file whenever certain patterns are observed in a packet. The software agent watches for the appearance of these files. As anŽ alternative, sniffer activities could be built directly into the software agent..

Our agent’s actuators had to interact directly with an application’s interface. To interact with a window, our agent posts messages either mouse click Ž events or keyboard events to the appropriate sub- . window and position. These latter activities are indistinguishable from a human posting these same types of events directly.

An assessment module decides on the required activity. Activities may be navigational e.g., clickŽ through a menu or link, connect to an ISP, etc. ,. informational e.g., enter username and password orŽ . require a decision. In the navigational or informational cases, an environment control component is triggered to perform the appropriate activities. When decisions are required, a DSS is invoked. Both components interact with the actuator component to undertake the desired activity.

The assessment component also acts as a monitor. This activity checks expected outcomes against actual outcomes to verify that the system and merchant application are behaving as expected.

Layering above the user interface has several advantages which we explore in Section 5. One concern is a possible degradation of performance. However, we found that an interface agent does not appear to hinder the performance of the application as the bottleneck is generally in the network.

The following case demonstrates the method’s strength. We use our interface agent on Internet casinos interfaces to play blackjack. The specific on-line casino discussed used a Java interface and the communication from the applet to the web server was not in cleartext. Strangely, some of the communication from the web server to the applet was in cleartext, providing us with the important information concerning reshuffle points which our network sniffer detected and relayed to our software agent’s monitor. We continue by describing the decision support system used to play blackjack.

## 3. Case example: Internet blackjack

We illustrate our approach using a novel setting where consumers can gain a dramatic advantage over the seller of an on-line service. Over the last 2 years on-line casino gaming has appeared on the Internet. This is a big market 5 . Some estimates put Internet<sup>w</sup> <sup>x</sup> gambling at US\$10 billion by the year 2000 seeŽ Roger 19 . At the time of our research, Internet <sup>w</sup> <sup>x</sup> . casino gambling was not illegal, although there was debate on this. US Senator Jon Kyl R. Arizona Ž . introduced a bill called the Internet Gambling Prohibition Act of 1997 on March 19, 1997 seeŽ www.ljx.com<sup>r</sup>internet<sup>r</sup>gamblebill.html . Kyl’s bill. goes beyond current laws by banning all Internet betting, not just sports betting.

One very popular game offered by casinos is blackjack — a game known to have a positive expected value 13 for the player if played optimally <sup>w</sup> <sup>x</sup> Ž . see Appendix A for a summary of blackjack play . Playing blackjack optimally is not easy for a human being. One must track the state of the remaining cards and vary their playing and betting strategy. Optimal play depends only on the state of the deck, the dealer’s exposed card, one’s hand and the rules of play. Optimal bets depend on the current state of a blackjack deck, the rules of play and the current bank size of the bettor. The sheer number of states possible prohibits one from knowing optimal betting in a traditional casino setting where such information must be memorized. Optimal play beyond that for a full deck is virtually impossible to know with certainty. Both optimal betting and optimal play are approximated by professional blackjack players in real casinos see Griffin 13 .Ž <sup>w</sup> <sup>x</sup>.

However, in on-line casino gambling, one can employ computer-assisted play and betting with impunity and play optimally. We developed a blackjack agent having the architecture of Fig. 2 to play on our behalf. A DSS component was developed that quickly determines optimal bets and optimal play based on the house rules, the current deck-state, etc.

Many people have studied optimal blackjack play. In 1956 Baldwin et al. 1 determined the optimal<sup>w</sup> <sup>x</sup> strategy for games played with a full deck and only one hand of play per deck. To determine optimal play, in general, one can enumerate the tree of possible outcomes for the different actions available and pick the sequence of actions that leads to the highest expected payoff. Our DSS component follows this total enumeration approach, although we spent considerable effort optimizing this calculation.

For example, suppose the first round in a singledeck game yields a dealer’s up card of a nine and a player’s hand consisting of a 10 and a seven. Should the player take a hit, stand, double-down or surrender depending on which options the house rules Ž permit? If only hit and stand options are available, . one must determine which branch in the following tree has a higher expected value. Let E Ždealer’s up card, player’s total: cards seen be the expected . payoff on a one dollar bet . This function enumer-Ž . ates the outcomes possible under the particular dealer play that the casino offers dealer play follows a Ž fixed strategy that has minor variations from one casino to another ..

For the case where the player stands, the dealer can realize more than 550 possible hands. For example, 9, 10 is one outcome. Another is 9, 4, A, 2,Ž . Ž 5 . Enumerating through the different situations gives.

$$
E (9, 1 7: 7, 9, 1 0) = - 0. 4 1 6 1 1
$$

$$
E (9, 1 8: 7, 9, 1 0, \mathrm{A}) = - 0. 1 6 6 9 1
$$

$$
E (9, 1 9: 7, 9, 1 0, 2) = 0. 2 7 8 9 6 9
$$

$$
E (9, 2 0: 7, 9, 1 0, 3) = 0. 7 5 0 1 3 9
$$

$$
E (9, 2 1: 7, 9, 1 0, 4) = 0. 9 3 8 6 7 7
$$

The expected value for hitting is then $4 / 4 9$ $\left( - 0 . 1 6 6 9 1 \right) + 4 / 4 9 \ \left( 0 . 2 7 8 9 6 9 \right) + 4 / 4 9$ Ž .  0.750139 $+ 4 / 4 9 ( 0 . 9 3 8 6 7 7 ) + 3 3 / 4 9 ( - 1 ) = - 0 . 5 2 6 4 6 .$ Since the expected value for standing Ž . <sup>y</sup>0.41611 is higher, optimal play requires standing in this situation.

There are many blackjack betting schemes — most of which are heuristic see Refs. 3,7–Ž <sup>w</sup> 9,11,12,17 and 20 . A common scheme is based on <sup>x</sup> <sup>w x</sup>. a running count that is correlated with the expected outcome of the hand see Thorp 20 . One mightŽ <sup>w</sup> <sup>x</sup>. double or quadruple a base bet if the running point count goes above a certain value. A point count system assigns a value to each card denomination. A count starts at zero for a new deck for balancedŽ point count systems. A. running count is kept by adding the value of every card seen. AŽ true count converts this count by dividing by the size of the remaining deck. Desirable point count systems are . highly correlated with the expected outcome of each hand.

We equipped our DSS with betting that minimized gambler’s ruin probabilities. To handle the idiosyncrasies of an actual casino environment Ž . primarily, the limited bet ranges , this required the solution of a very large Markov Decision problem Žsee Ref. 6 for solution details and proofs . Let<sup>w</sup> <sup>x</sup> . $N _ { \mathrm { U } }$ be the absorbing states at the upper wealth target level, U, and $N _ { \mathrm { L } }$ be the absorbing states at the lower wealth level, L. A state was represented by the true count, the number of aces left in the deck, the number of cards left in the deck the current bank size. We solved

$$
\begin{array}{c} v _ {\mathrm{s}} ^ {(n + 1)} = \max _ {B _ {\mathrm{L}} \leq w \leq B _ {\mathrm{U}}} P (w) _ {\mathrm{s}} + \sum_ {t \in v _ {\mathrm{s}}} P (w) _ {\mathrm{s}, \mathrm{t}} v _ {\mathrm{t}} ^ {(n)} \\ \mathrm{s} \notin N _ {\mathrm{L}} \cup N _ {\mathrm{U}} \end{array}
$$

where $P ( w ) _ { s }$ is the probability of attaining wealth U from state s with integer wager w and $v _ { \mathrm { s } }$ is the set of all non-absorbing states reachable from s. $v _ { \mathrm { s } } ^ { ( n ) }$ is the nth estimate of the probability of first attaining wealth U before dropping to wealth level L starting from state s. We determined the steady state solution $v ^ { * }$ which gives the actual probabilities.

Our objective, minimizing gambler’s ruin, generally yields timid play which was a goal of ours Ž since we were gambling with our own money .. ŽAfter our experimentation was completed, a breakthrough by Janecek 15 gave methods for computing<sup>w</sup> <sup>x</sup> bet sizes that maximize income growth subject to restricted betting ranges. These could easily be incorporated into our DSS ..

Most on-line casinos have their own interface. Some, like IslandCasino $( \mathrm { U R L } = h t t p ; / /$ www. islandcasino.com., use Java applets. Others, like CasinoRoyale $( \mathrm { U R L } = h t t p \colon / /$ www.funscape. com., use HTML interfaces. And yet others, like Club Casino URL Ž . <sup>s</sup>http:<sup>rr</sup>www.clubcasino.com , have the user download an application to run on their computer while connected to the Internet . A typicalŽ . playing area is shown in Fig. 3.

![](/api/attachments/3RAKP769/fulltext/images/1daf10b7f9ac24963074f2d5796b5dbc5051f1134083114bd406a3eec5869326.jpg)  
Fig. 3. The results of a play at IslandCasino that involved two sequential split hands with no hits on any of them.

In Fig. 3, one can notice that several objects have to be sensed. Clearly, the displayed cards have to be identified. Often a message has to be read theŽ message here is ‘‘Player wins \$3’’ such as ‘‘Re- . shuffling’’ so that the deck state can be reset. One can also identify buttons that have to be clicked. The betting buttons raise or lower the prior bet. Other buttons such as deal, hit, stand, etc. are needed during play.

In this application, there is a caveat emptor concern. The on-line casinos might cheat. Casino cheating and fraud are very hard to detect in on-line environments, yet are trivial to implement. For example, a casino’s blackjack program could easily construct hits to a dealer or player’s hand from the remaining deck to alter the natural random out-Ž . come to the casino’s advantage. Furthermore, there are no official regulatory or auditing bodies overseeing this type of cheating. States hosting gambling have such regulatory agencies like Nevada’s State

Gaming Control Board. No such boards oversee on-line casinos — most of which operate out of offshore locations.

We added a monitoring component to check for possible cheating. The monitoring activity of our agent compares expected outcomes with actual outcomes. Our DSS engine computes the expected outcomes on all activities. These probabilities were tested against the actual frequencies using various statistical tests such as chi-square goodness of fit Ž and the Kolmogorov–Smirnov non-parametric test of equivalent distributions ..

## 4. Results

The optimal betting problem we employed required solving a Markov decision problem having many states. Below are estimates of the number of deck states for different reshuffle points in a singledeck game. A deck state is the combination of true count, the number of aces, and the number of cards left in the deck These were determined from a simulation study of over 100 million hands.

<table><tr><td>Reshuffle point</td><td>Estimated number of deck states</td></tr><tr><td>45</td><td>223</td></tr><tr><td>40</td><td>966</td></tr><tr><td>35</td><td>2160</td></tr><tr><td>30</td><td>3727</td></tr><tr><td>25</td><td>5624</td></tr><tr><td>20</td><td>7518</td></tr></table>

The total number of Markov states is the product of number of deck states times the bet spread size times the difference between the hi<sup>r</sup>lo wealth levels one operates within the low point is the point, Ž L in Section 3, where one leaves the game bankrupt and the upper level, U, is the target win level . For . example, when the reshuffle point is 30, the bet range US\$10–US\$50 and a lo<sup>r</sup>hi wealth range US\$2000, we have a problem of size $3 7 2 7 * 1 9 9 9 * 4 1 = 3 0 5 , 4 6 1 , 1 9 3$ states. These values for wealth limits and betting ranges are considered modest for a professional player.

We chose IslandCasino $\mathrm { ( U R L } = h t t p \colon / /$ www.islandcasino.com. to test our agent. The house rules at the time of our study were:

<sup>Ø</sup> The player may double-down on any two-card hand, even on non-ace split hands;

<sup>Ø</sup> Surrender is not permitted;

<sup>Ø</sup> The dealer must stand on a soft 17 hand;

<sup>Ø</sup> Reshuffling takes place between 30–39 cards remaining in the deck;

<sup>Ø</sup> Re-splitting may take place until there are three hands;

<sup>Ø</sup> The game is played with a single deck.

IslandCasino dealt more than one hand from a deck — usually with 30–40 cards remaining. This offers good odds for a player making optimal playing and wagering moves.

Fig. 4 shows the results of 28,910 hands of actual play by our agent with bets ranging from US\$1 to US\$10. This play was fully automated and was played through IslandCasino’s interface. Each hand took about 10–11 s to play. The total amount of time required for this study was about 85 h. This was spread over two machines playing simultaneously. As an aside, the agent’s monitor module did not detect any cheating by the casino.

![](/api/attachments/3RAKP769/fulltext/images/a603a5b0119395cca71a15fdeaaa9ebf7a73189d3be133d9d2708a5b86e90a07.jpg)  
Fig. 4. Results from 28,910 hands of actual play.

This 10–11 s of play per hand includes interpreting the screen determining the original cards dealt,Ž the new cards dealt during the hand’s play, the outcome, any status messages, etc. deciding how . much to bet, deciding how to optimally play the hand both with the original hand and any subse-Ž quent decisions as the hand was played-out , all the . back and forth communication to the casino, etc.

What did the casino do about this? We do not know if our agent precipitated any particular action, but over the course of nine months the casino made a number of changes these changes may have beenŽ made due to other pressures — there were changes of ownership, change of location and an FBI sting on a sports betting portion of the casino’s offering, presumably an illegal activity . At first, IslandCasino . played to about 20 cards remaining before reshuffling. This was an incredible player opportunity. In general, the player’s expected value increases with the depth of the reshuffle point. Over the remaining months, the reshuffle point was moved to about 30 then 37 cards remaining. Finally, IslandCasino started reshuffling after each hand. The game is an essentially break even one at this point. Actually, mostŽ Internet casinos offer deposit bonuses of 5–20% of a deposit. One only needs to wager each dollar of deposit and bonus once to keep the bonus. Hence, playing a break even game with an agent can still net a nice return. At one point during the year of our . research activity, IslandCasino posted the following rule:

All Internet wagers must be placed through the user interface provided by this casino on its Web pages.

Our software agent strictly played through the user interface provided.

## 5. Agent blocking mechanisms

As BargainFinder illustrated, software agents can be detrimental to merchants, and several techniques exist to discourage their usage. In the case of BargainFinder, a simple firewall can be used to restrict access from particular IP addresses. More complicated mechanisms exist as well, dealing with secure connections, encryption, and dynamic protocols. This section first describes these traditional approaches, which we show are largely impotent against an interface agent. We then explore ways to hamper an interface agent.

## 5.1. Traditional merchant protection schemes

In order for an agent to interact with a remote computer directly i.e., not through an interface ,Ž . protocols must be well defined on each end. In the case of the World Wide Web, that protocol is generally HTTP HyperText Transport Protocol . HTTP isŽ . a simple text-based application layer protocol and is used to transport HTML documents on TCP<sup>r</sup>IP networks. It is a well-known protocol and is especially easy to implement in Java or C<sup>qq</sup> based agents.

HTTP supports GET and POST data-passing requests. Consider the sign-on screen in Fig. 5. Part of the code behind this page is displayed below with formatting removed.

![](/api/attachments/3RAKP769/fulltext/images/1934b6198f610e8eaef7773f3fe68085f72b802b77ae0d020f8058436895d038.jpg)  
Fig. 5. Sign-on screen.

<sup>-</sup> FORM method <sup>s</sup>‘‘POST’’ action <sup>s</sup>‘‘http: <sup>rr</sup> 128.227.36.36 <sup>r</sup> cgi-bin <sup>r</sup> serverprogram.exe’’ <sup>)</sup> Stock Symbol: <sup>-</sup>INPUT type<sup>s</sup>text size<sup>s</sup>20 name <sup>s</sup>‘‘Name’’<sup>)</sup>Password:<sup>-</sup>INPUT type<sup>s</sup>password size<sup>s</sup>20 name<sup>s</sup>‘‘Password’’<sup>)-</sup>INPUT type<sup>s</sup> submit name<sup>s</sup>‘‘Submit’’ value<sup>s</sup>‘‘Enter Site’’<sup>)</sup> <sup>-r</sup>FORM<sup>)</sup>

The names of the GUI objects Name, Password,Ž Submit can be easily scanned for by an agent. These. requests typically send information from a browser to a web server in the form of cleartext variable<sup>r</sup>value parings, such as Symbol<sup>s</sup>CSCO& Password<sup>s</sup>MyPassword. Below is the actual text sent by this browser with lower-level protocol information removed and the transmitted cleartext information in bold as captured by a network sniffing device.

POST. <sup>r</sup> scripts <sup>r</sup> echome.exe.HTTP <sup>r</sup> 1.0..Referer: .http:<sup>rr</sup>128.227.36.36<sup>r</sup>cm.html..Connection:.Keep Alive.. User-Agent:.Mozilla <sup>r</sup> 4.51. en . WinNT;.I .<sup>w</sup> <sup>x</sup> Ž . .Host:.128.227.36.36..Accept:.image<sup>r</sup> gif,.image<sup>r</sup> xxbitmap, .image<sup>r</sup>jpeg,.image<sup>r</sup>pjpeg,.image<sup>r</sup>png,. <sup>r</sup> U ..Accept-Encoding:.gzip..Accept-Language:.en..Accept-Charset:.iso-8859-1,<sup>U</sup>,utf-8..Content-type:.application<sup>r</sup>x-www-form-urlencoded..Content-length:.54 . . . Name <sup>s</sup> CSCO & Password<sup>s</sup> MyPassword& Submit<sup>s</sup>Enter<sup>H</sup>Site..

In order for an agent to work directly with a merchant server, the agent would have to be aware of the names for the corresponding GUI objects. This information is of no interest to the human users, and frequent changes to the object names would not hinder the user in any way. The agent, however, would have to guess which object represented which human action and could be fooled by a dynamic naming scheme from the server. All of the HTTP protocol information above can be handled by readily available routines.

If Internet cookies were involved, it would create additional complications for the direct agent. Cookies are stored client-side information used most often to simulate a continuous session http is connection-Ž less or function as a server database key, where the . database would be used to track user preferences or history. These complications would be mostly programmatic, though there may be clever ways to use cookies to deter agents.

A merchant could further complicate an agent’s work by requiring a secure connection, via secure sockets or s-HTTP. This may force the software agent’s developer into mastering topics such as public and private key encryption, hashing functions, and third party digital certificates. Again, Java has some nice tools for performing these tasks, but the learning curve is not trivial.

Finally, if the merchant used Java applets, Java’s remote method invocation, or another distributed object protocol CORBA over IIOP for communica-Ž . tion, they could freely use encryption or change protocols for each request without changing the user interface. This would create a significant challenge for agent developers and the development process itself may tip off the merchant to the agent’s purposes.

An interface agent is immune to these merchant strategies since the interface agent deals only with the web-page interface as a human would whichŽ . does not require direct interactions with the merchant’s server. The interface agent’s input cannot be distinguished from human input. Whether the client application were driven by HTML, VBScript, JavaScript, or Java Applets, the approach would be identical, so there would be no need to adjust the agent even if the merchant went to XML and stylesheets for example. Furthermore, as the agent works, one can visually monitor and validate the process.

Nor is any knowledge of the latest security mechanisms necessary since the interface agent deals only with the web-page interface — not the encrypted streams between the client and server. For example, graphical user interface objects and windowing mechanisms typically remain constant independent of web application, whereas protocols, security, and merchant naming techniques can change rapidly between applications or even within an application. For this reason, an agent that communicates with the windowing mechanisms can be quickly modified to interact with a different application. This distinction was important in our study. Each of the hundreds of target casino merchants has different protocols, security, and architectures, each which would require a significant modification to a traditional electronic commerce agent. With the interface agent, modifications are less traumatic.

## 5.2. Possible merchant protection schemes against an interface agent

Because this particular agent iterates through client-side windowing process names and addresses, the merchant would have no control over the creation or protection of the GUI objects, only screen placement, color, and other design features. A merchant could dynamically change the user interface itself so the interface agent would have to be continuously updated. However, if done frequently, this would likely frustrate conventional users and is thus considered poor design. It also imposes a continuous redesign effort by the merchant. The secret then is to create a stable user interface that disrupts the agent.

If a user interface incorporates complex graphics, a human user could more readily absorb the inherent information than could a completely automated agent performing image recognition and parsing of graphical objects. This poses a temporary stumbling block, at best. Although a completely automated agent might find this challenging, an interface agent could be trained to match portions of images with a set of important cases. These cases can be prepared by a human agent who performs the recognition of important portions of the image. In any case, transmitting large, complex images impose a potential performance obstacle. Image files are typically much larger than text files.

The matching abilities of image recognition software may allow for simple disruptions. For example, if the interface agent always begins a search for matching pixels at a particular location, the merchant could slightly alter this location programmatically to confuse the agent. It is unlikely a user would notice a shift of a few pixels between sessions, but this could pose a significant obstacle to the agent. A similar mechanism could be used regarding subtle color alterations. Of course, both of these maneuvers can be overcome by a slightly more sophisticated filtering and recognition component in the agent.

If timing is involved, there may be mechanisms available to the merchant to change the speed or order of an interface so as to disrupt the timing of the agent. For example, if an agent began its response as the applet was being drawn, it could attempt to send a click message to a button that the interface has not yet created. Again, the timing would have to be subtle so as not to disrupt the user. Also, if a critical message is momentarily displayed, the agent may not always catch it with its scan of the application image. Of course, a human user might miss it too.

Merchants should track the behavior of the customers as well. For example, in our study, if a customer is playing blackjack for 100 straight hours without a break it did happen in our study , itŽ . should trigger an alert. Of course, an agent can simply program such delay mechanisms or other simulated human behavior to defeat such triggers.

In the blackjack example, the casino was simply forced to change the rules of the game to reduce it to a breakeven expected payoff by reshuffling after every hand. This had the effect of making the game significantly less attractive to both professional and casual players, especially considering the other available casinos and their rules.

## 6. Conclusions and future research

This research successfully demonstrated a new type of software agent which converts merchant interfaces into middleware, thus enabling one to assess and optimize their interactions with all the computing support available in today’s DSS environments.

One area of future research is the need for describing and developing tools to automate the training of the agent to interact with a new interface. All intelligent software agents either have domain knowledge loaded into the agent’s knowledge base or are equipped with learning capabilities. We used a combination approach where the graphical data was first captured and interpreted by the authors. The interface agent would then perform pattern recognition searching for these pre-specified objects. Learning new interfaces should not be very difficult since most graphical user interface components are well defined and constitute a relatively small set.

The interface agent’s usage of a client-side merchant application is completely indistinguishable from a human agent’s usage. It operates through the merchant’s interface. However, an astute merchant might notice that a customer is making exceptionally good decisions. To the extent that the merchant can ban such individuals, our agent can also be targeted. However, it is relatively easy to disguise our agent’s activities. Many optimal actions have little incremental value over sub-optimal actions. The agent might select sub-optimal even naive actions in these casesŽ . while still using optimal actions in more lucrative situations.

Optimality itself is a good disguise. Indeed, we saw many situations where the optimal actions looked naive compared to normal ‘‘expert’’ play. For example, consider the completely contrived case where the dealer has an up card of an 8. The player has a hand totaling 19 and there are 4 cards remaining in the deck — all of them aces. Most players not tracking the deck’s state would stand on a 19 vs. an 8. However, hitting the 19 results in a win a guaran- Ž teed 20 vs. a final dealer’s total of 19 where stand- . ing results in a push a 19 vs. a 19 .Ž .

There is a well-known statement ‘‘pigs get fat but hogs get slaughtered.’’ A software agent can operate 24 h a day, 7 days a week. This is ‘‘hog’’ activity. However, one can run a software agent 24 h a day, 7 days a week by running a few minutes under each of a large number of different accounts possibly on Ž different, widely dispersed machines ..

We have illustrated the value of an interface agent with Internet casinos. Other areas of potential caveat mercator should be identified. Even in the Internet casino environment, other games can be played with positive expected value such as certain video poker games 10 . Many other opportunities exist. One can<sup>w</sup> <sup>x</sup> imagine the simultaneous arbitrage across various auction sites. At the least, new electronic commerce initiatives need to understand this possibility.

Conversely, good strategies to thwart interface agents need to be discovered. Otherwise, a significant threat to electronic commerce exists, as illustrated by our research. This threat is not something most merchants understand. They have not been exposed to a real-world counterpart of this cyberspace nuance. For example, traditional casinos operated for hundreds of years before limited versions of optimal play of blackjack were discovered. It took years for casinos to evolve effective strategies to thwart savvy players knowing how to employ these methods.

It is important to note that not all adverse agent activities are viewed as such. For example, many merchants found BargainFinder’s activities unavoidable and sought other, more traditional, strategies to cope — like being a loss-leader making money on ancillary services, or bundling. So merchants may need to rethink their business plans and find ways to accept the new realities of commerce but still make money.

As a reviewer pointed out, another situation yielding caveat mercator concern could arise from consumers interacting with each other, perhaps collusively, perhaps just learning as a group.

## Appendix A. The game of blackjack

Blackjack is played between a dealer and from one to seven players. On the Internet or on video blackjack machines, typically only one player is allowed which is the case we consider here. A player places a bet and then he and the dealer initially receive two cards. One of the dealer’s cards is exposed called the dealer’s up card . Ž .

If the dealer’s exposed card is an ace, the player may place a side bet called an insurance bet of upŽ . to half of his initial bet. If the dealer also has a 10-valued card these are tens, jacks, queens andŽ kings , he has a natural blackjack and the player. wins the insurance bet which pays two to one. The player loses his current bet unless he too has a natural blackjack. Without insurance, the player having a blackjack would push in this situation — he neither wins nor loses. In any case, if a dealer has a natural blackjack, the player loses his bet unless he too has a natural blackjack. If the dealer does not have a natural blackjack but the player does, the player wins 1.5 times his current bet.

In hands with no blackjacks, a player has several possible strategies. He may split his hand into two new hands if his two cards are the same denomination. These two hands each are given an additional card. He may recursively split these except for split aces which get no further action a split ace receiv-Ž ing a 10-valued card is not considered a natural blackjack . Most casinos restrict the number of re-. splits. On a new hand, a player may double-down which means he doubles his bet and receives only one additional card. Some casinos limit the hands, which may be doubled, and may restrict doubling to non-split hands.

Finally, the player may repeatedly hit a hand Ž . which still totals less than 22 . A ‘‘hit’’ means he gets another card. He eventually stands on his current hand total at his discretion or busts and loses with a hand totaling more than 21. The total of a hand is the sum of the value of each card. Aces count one or 11, 2’s through 9’s count their face value. Ten-valued cards count as 10. If the player exceeds a total of 21, he loses.

If the player has not yet lost by exceeding a hand Ž total greater than 21 or won with a natural black-. jack, the dealer must keep hitting till his total exceeds 16. A variation requires the dealer to keep hitting a soft 17 e.g., a hand totaling 17 when an ace Ž is counted as an 11 . If the dealer’s hand exceeds 21, . he loses. Otherwise, the one with the higher total wins. Equal totals are pushes — nobody wins.

## References

<sup>w</sup> <sup>x</sup> 1 R.R. Baldwin, W.E. Cantey, H. Maisel, J.P. McDermott, The optimum strategy in blackjack, Journal of the American Statistical Association 51 275 1956 429–439.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 BargainFinder URL: http:<sup>rr</sup>bf.cstar.ac.com<sup>r</sup>bf.

<sup>w</sup> <sup>x</sup> 3 L. Breiman, Optimal gambling systems for favorable games, Proc. 4th Berkeley Symp. Math. Stat. Prob. 1 1961 65–78.Ž .

<sup>w</sup> <sup>x</sup> 4 W. Brenner, R. Zarneko H. Wittig, Intelligent Software Agents, Springer-Verlag, New York, 1998.

<sup>w</sup> <sup>x</sup> 5 D.G. Conway, G.J. Koehler, Internet gaming: scope, issues, and opportunities. Department of Decision and Information Sciences, University of Florida, Gainesville, FL, 1998.

<sup>w</sup> <sup>x</sup> 6 D.G. Conway, G.J. Koehler, Solving the Blackjack Betting Problem, Department of Decision and Information Sciences, University of Florida, Gainesville, FL, 1998.

<sup>w</sup> <sup>x</sup> 7 S. Ethier, S. Tavare, The proportional bettor’s return on investment, Journal of Applied Probability 20 1983 563– Ž . 573.

<sup>w</sup> <sup>x</sup> 8 T.S. Ferguson, Betting systems which minimize the probability of ruin, Journal of the Society of Industrial and Applied Mathematics 13 3 1965 795–818.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 M. Finkelstein, R. Whitley, Optimal strategies for repeated games, Advances in Applied Probability 13 1981 415–428.Ž .

<sup>w</sup> <sup>x</sup> 10 L. Frome, M. Guberman, America’s National Game of Chance. Compu-Flyers, Las Vegas, NV, 1992.

<sup>w</sup> <sup>x</sup> 11 G. Gottlieb, An optimal betting strategy for repeated games, Journal of Applied Probability 22 1985 787–795.Ž .

<sup>w</sup> <sup>x</sup> 12 P.A. Griffin, Different measures of win rate for optimal proportional betting, Management Science 30 12 1984Ž . Ž . 1540–1547.

<sup>w</sup> <sup>x</sup> 13 P.A. Griffin, The Theory of Blackjack, 4th edn. Huntington Press, Las Vegas, NV, 1988.

14 R. Guttman, A. Moukas, P. Maes, Agent-mediated electronic commerce: a survey, to appear, Knowledge Engineering Review, June 1998.

<sup>w</sup> <sup>x</sup> 15 K. Janecek, Optimal Growth in Gambling and Investing, Thesis, Charles University, Prague, January, 1999.

<sup>w</sup> <sup>x</sup> 16 Jango URL: http:<sup>rr</sup>www.jango.com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 17 J.L. Kelly, A new interpretation of information rate, The Bell System Journal, July, 1956, pp. 917–926.

<sup>w</sup> <sup>x</sup> 18 S.D. Pinson, J.A. Louca, P. Moraitis, A distributed decision support system for strategic planning, Decision Support Systems 20 1997 35–51.Ž .

<sup>w</sup> <sup>x</sup> 19 W. Roger, Prohibition for net gambling, Interactive Week, April 8, 1997.

<sup>w</sup> <sup>x</sup> 20 E. Thorp, Beat the Dealer: A Winning Strategy for the Game of Twenty One, Blaisdell Publishing, New York, 1962.

![](/api/attachments/3RAKP769/fulltext/images/f7b22711f72a91989583753a54c2f38bc9bd41a727be7cfebc57d827f5c6b1a7.jpg)  
Daniel G. Conway is assistant professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. He has published in Annals of Operations Research, IMA Journal of Mathematics Applied to Industry, and Computers and Operations Research. His current research interests involve e-commerce, telecommunications and related areas.

![](/api/attachments/3RAKP769/fulltext/images/7a5ef4dc4166e385de222d156e0b44d83239a35bf9728cd9ff8f82de7e074abc.jpg)

Gary J. Koehler is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. He was recently Professor and Area Head at the Krannert Graduate School of Management at Purdue University. He has published in Decision Support Systems, Operations Research, Management Science, ORSA Journal on Computing, EÕolutionary Computations, SIAM Journal on Control

and Optimization, Annals of Operations Research, European Journal of Operational Research, Decision Sciences, Annals of Mathematics and Artificial Intelligence, Computers and Operations Research, Complex Systems, Neural Networks, IEEE Transactions on Engineering Management, Managerial and Decision Economics, Naval Research Logistics Quarterly, Discrete Applied Mathematics, Journal of Finance and others. His current research interests are in e-commerce related areas.
