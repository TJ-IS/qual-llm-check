---
otero_id: 152
otero_key: "QC4U9FQV"
title: "Application of complex adaptive systems to pricing of reproducible information goods"
authors: "Moutaz Khouja; Mirsad Hadzikadic; Hari K. Rajagopalan; Li-Shiang Tsay"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Application of complex adaptive systems to pricing of reproducible information goods<sup>☆</sup>

Moutaz Khouja <sup>a,⁎</sup>, Mirsad Hadzikadic <sup>b,1</sup>, Hari K. Rajagopalan <sup>c,2</sup>, Li-Shiang Tsay <sup>d</sup>

<sup>a</sup> Business Information Systems and Operations Management Department, The Belk College of Business Administration,

The University of North Carolina at Charlotte, Charlotte, NC 28223, United States

<sup>b</sup> College of Information Technology, The University of North Carolina at Charlotte, Charlotte, NC 28223, United States <sup>c</sup> School of Business, Francis Marion University, Florence, SC 29501, United States

<sup>d</sup> Department of Computer Science, Hampton University, Hampton, Virginia 23668, United States

Received 1 August 2005; accepted 1 February 2007 Available online 13 October 2007

## Abstract

Piracy of copyrighted information goods such as computer software, music recordings, and movies has received increased attention in the literature. Much of this research relied on mathematical modeling to analyze pricing policies, protection against piracy, and government policies. We use complex adaptive systems as an alternative methodology to analyze pricing decisions in an industry with products which can be pirated. This approach has been previously applied to pricing and can capture some aspects of the problem which are difficult to analyze using traditional mathematical modeling. The results indicate that advances in technology make a skimming strategy the least preferable approach for producers. Further, improvements in technology, more specifically data communications and the Internet, will erode the profitability of a skimming strategy. The analysis also indicates that complex adaptive systems may provide a useful method for analyzing problems in which interactions between participants in the systems, i.e. consumers, sellers, and regulating agencies, are important in determining the behavior of the system. © 2007 Elsevier B.V. All rights reserved.

Keywords: Information goods; Pricing; Piracy; Complex adaptive systems

## 1. Introduction

Piracy of copyrighted products has become a major problem for many firms. Tolerating some piracy may increase the consumer base for a product and creates positive network externalities, which refer to a case where a consumer's utility from a software increases with the number of its users [21,25]. In that respect, having more consumers use a software makes it more valuable to others. These positive aspects are less important in the recorded music and movie industries. Conner and Rumelt [10] examined protection strategies in the presence of positive network externalities. Their analysis indicates that, in the presence of positive network externalities, a strategy of no protection can result in lower price and increased profit. The authors show that network externalities have a strong effect under three conditions: (1) The software is complicated and difficult to master, (2) the software allows or demands extensive user customization, or (3) the software is useful for multiple-user data processing or formal networking. For example, a user would rather use Microsoft Word over Word Perfect if most users are using Microsoft Word for word processing. This is because using the software makes it easier for a user to share documents with others. Some users may therefore be willing to pay more for Microsoft Word. However, in case of music and movies the three conditions identified by Conner and Rumelt [10] are not present.

Industries susceptible to piracy are usually dominated by monopolists who obtain monopoly power through copyright and intellectual property protection. Like other monopolies, they are viewed unfavorably because they tend to charge higher prices than what would prevail under competition. For example, while Napster was being shut down after having been accused of contributing to piracy, major record labels in the music industry, such as Sony, and EMI, were accused of violating fair trade practices by threatening retailers not to advertise compact disks (CDs) below certain prices [4].

Among the industries suffering from piracy, recorded music seems to be the worst hit. Pirating music has become much easier due to digitization, the adoption of compression technologies such as MP3, and easy access to digitized music files on the Internet. The Recording Industry Association of America's (RIAA) 2003 statistics show that both the number and the dollar value of CD sales have declined since 2001. In 2003, sales of music CDs were \$11.2 billion compared to a peak of \$13.2 billion in 2000. Also, since the launch of Napster in 1999, sales of CD singles have been decreasing at a remarkable rate till 2002. This is, in part, due to the fact that compressing one song into an MP3 file makes it easy to swap. Although Napster, once the most popular music-swapping site, was shut down in an effort to prevent piracy by the big record labels, alternative file sharing through P2P networks, such as Kazaa, WinMX, and Gnutella, immediately replaced Napster. These P2P networks do not require a central server to store files, thus avoiding possible litigation.

The marketing and economics literature delineates the different pricing strategies a firm can follow under different conditions [22]. These conditions include degree of product differentiation, the competitive situation, and the nature of demand. Skimming and penetration are the classic strategies for pricing new products [22,29]. A skimming strategy is one in which a firm sets a high initial price and then systematically reduces it. In a monopoly market, which is the case for many information goods, the monopolist is certain that the entire market demand is its own. Therefore, a skimming strategy can be used to exhaust the market [12]. The initial price is aimed at consumers for whom obtaining the product early is important and who are willing to pay a premium for early ownership. As this segment becomes saturated, price is reduced to increase the appeal of the product [11]. This strategy is most appropriate when products are highly differentiated, a segment of the market is price-insensitive, and there are limited economies to scale or learning curve effects. Pricing in a skimming strategy maximizes profit based on what the market can bear and the product's worth to buyers [11,21]. The increased margins which skimming brings should be balanced against the decreased sales volume.

Since a skimming strategy is suitable when a company has a temporary monopoly position [22], it is ideal for producers of copyrighted products such as movies and music recordings. These firms enjoy a natural monopoly position and can skim the market for as long as their intellectual property is protected. However, piracy may erode monopoly power even without competitors entering the market.

Determining prices in a market where some piracy is unavoidable is a complex problem which is difficult to analyze using traditional mathematical modeling. The difficulty arises in modeling the act of piracy itself. For a consumer to pirate a product, the following prerequisites are needed: 1) the consumer does not have a copy of the product, 2) the value the consumer attaches to the product exceeds the cost of the copying medium and the risk of being caught and penalized, 3) the consumer prefers pirating to purchasing a legitimate product (because his/her reservation price is not met or the expected gain from piracy exceeds the expected gain from purchase), 4) the consumer knows another consumer, i.e. neighbor, with a reproducible copy, and 5) the consumer or one of his/her neighbors has access to the duplication technology. Therefore, the rate of piracy at a point in time depends on the diffusion of both legitimate and pirated copies (when copies can be made from copies) in the market up to that point and on consumer connectivity. We define consumer connectivity as the number of neighbors, physical or via a computer network, that a consumer can share copies with. Complex adaptive systems (CAS) and agent-based modeling (ABM), which is a flexible approach to modeling CAS, may provide a useful methodology for analyzing pricing decisions under piracy. CAS and ABM have been previously applied to pricing problems in a two-firm market where consumers' purchase decisions are solely based on price [34].

The objectives of this paper are to 1) provide an alternative methodology for analyzing the problem of piracy, 2) find an optimal monopolist's pricing strategy in a market where some piracy is unavoidable, 3) investigate the impact of piracy on consumers, monopolists, and artists, and 4) evaluate the applicability of CAS to business problems, and more specifically pricing.

The key results are 1) consumer connectivity has a strong impact on optimal pricing strategy, 2) strong consumer connectivity erodes the profitability of a skimming strategy, 3) requiring a legitimate product to make a copy does not significantly lessen the impact of piracy on profit when consumer connectivity is strong, 4) deterrent piracy controls must significantly increase consumers' risk and cost of piracy to be effective, and 5) CAS offer an effective platform for understanding the combined effects of many variables on pricing.

The paper is organized as follows. Section 2 offers a review of the literature. In Section 3, we introduce CAS and describe their use in problem solving. In Section 4, we develop a CAS for analyzing a monopolist's pricing policy in a market with piracy. In Section 5, we discuss the results from several experiments conducted using the developed system. Section 6 concludes with summary of findings and future research on applying CAS to business problems.

## 2. Literature review

Piracy has had a major impact in the computer software industry. Research on software piracy mainly deals with pricing, copyright protection, and government policies. Nascimento and Vanhonacker [21] found that a skimming strategy is optimal in the absence of piracy. Using the diffusion of innovation model, they also found that copy protection is recommended when sales grow faster than piracy and the cost of protection does not significantly increase the marginal cost. Givon, Mahajan and Muller [13] showed a positive side to piracy with a software diffusion model.

Prasad and Mahajan [25] examined the relationship between the rate of software diffusion and piracy to determine the price and the piracy level that should be tolerated. The authors examined three cases: A monopoly, a monopoly with multiple generations of software, and a competitive market. Their results indicate that a monopoly should have little piracy protection at the early stages of the software's life and impose maximum protection in the second half of the life cycle. For multigeneration software monopolist, the first generation should have less protection than in the monopoly case only if profit margins are expected to decline in subsequent generations. For the competitive case, less protection should be used than in the monopoly case. Haruvy, Mahajan, and Prasad [17] examined how piracy affects the adoption of subscription software. In this model the producer determines the price and the protection level which maximize the discounted profit stream over the product's life. The results indicate that moderate tolerance for piracy can speed up adoption and enables the producer to charge higher prices. Tolerance for piracy decreases when market penetration is quick, information is imprecise, and positive network externalities are low.

Sundararajan [31] analyzed optimal pricing and piracy protection for a monopolist using price discrimination among consumers who are willing to buy variable quantities of a digital good. The author shows that the optimal pricing schedule can be characterized as a combination of zero-piracy pricing and piracy-indifferent pricing schedules. Other findings by network externality-based studies [10,28,32] also indicate that allowing piracy can make the producer more profitable when positive network externality exists.

Chen and Png [7] developed a model that incorporates a piracy penalty set by the government. The monopolist determines price and piracy monitoring rate. Users can buy the product, pirate it, or not use it. The authors show that changes in pricing and monitoring rates have qualitatively different effects on consumers. They also show that from a social welfare perspective, price reductions are better than increased monitoring. Chen and Png [8] extended the model to include a tax on copying media and equipment and a government subsidy for legitimate purchases. Consumers are divided into ethical and unethical groups. The results indicate that taxing the copying media is better from a social welfare standpoint than penalizing piracy, and that the best government policy is to subsidize legitimate purchases. Belleflamme [2] considers a case in which copies are of lower quality than originals. He shows that although diffusion through piracy increases social welfare, this comes at the expense of the producer's profits, which may be insufficient to cover the creation cost.

Chellappa and Shivendu [5] analyzed the implications of variable technology standards in the movie industry. They concluded that when piracy is prevalent, maintaining separate technology standards between different regions is beneficial to the producer. In addition, it is not only the producer who incurs losses due to global piracy but also the consumers in regions where quality is important. In a more recent study, Chellappa and Shivendu [6] assume that consumers are not fully aware of the true fit of an information good to their tastes until consumption. In this model, piracy offers a consumption opportunity before purchase. The authors develop a two-stage model of a market composed of heterogeneous consumers in their marginal valuation for quality and their moral costs. Some consumers pirate the product in the first stage and based on that experience update their fit-perception which may cause them to reevaluate their buying/pirating decision in the second stage. An important result from the model is that piracy losses are more severe for products that are overvalued in the market and ultimately do not live up to their reputation rather than for products that have been undervalued in the market and turn out to be a good surprise.

Papadopoulos [23] investigated the relationship between price, copyright law enforcement, and formation of black markets. Data for music recordings was used to fit a regression model to estimate the relationship between legitimate music recording price, black market distribution channels and piracy. The author found that piracy in a country is most strongly related to the ratio of average hourly wage to the average sound recording price and to a lesser degree, to a black market efficiency index. Wang [38] analyzed motion picture piracy and found a positive relationship between perceived cost– benefits of a pirated copy and intent to purchase a pirated copy. The likelihood of purchasing a pirated copy is not dependent on individual income but rather on the perceived benefit relative to the cost of a pirated copy. In addition, the results indicate a negative relationship between the variables of perception of performance risk, ethical concern regarding piracy, and perception of social norms opposed to piracy and the intent to purchase a pirated copy. Other recent behavioral studies on piracy in the music and software industry have been undertaken by Chiou, Huang, and Lee, [9] and Moores and Chang [20], respectively.

Related to copyright protection, an interesting finding by Gopal and Sanders [14] is that deterrent controls, which employ educational and legal campaigns, protect the producer's profit better than preventive controls that use technology to make piracy difficult. Also, deterrent controls were shown to be superior from social welfare perspective.

A unique aspect of the music and movie industries is the royalty system. Record labels usually pay per unit royalty to artists ranging from 5% to 25% of the sale price or a fixed amount per unit sold. An artist who gets royalty was once considered one of the victims of piracy. However, a recent report from Pew Internet &

American Life Project reveals that many artists do not feel that digital file sharing hurts them [26].

Many of the above models have focused on one or two aspects of piracy in order to maintain mathematical tractability. For example, some models have focused on network externalities, some on price and protection level, some on price and government policy, and some on varying technology standards. Incorporating several piracy aspects into a single model complicates the analysis and makes insights into the interaction effects of these factors difficult to obtain. Piracy is a dynamic problem in which the time element is essential. The level of piracy at a point in time depends both on the number of legitimate and pirated copies of the product available in the market. This makes the time of price changes to increase revenue a critical part of decision making. Finally, products susceptible to piracy are usually shortlived products with consumer interest waning quickly over time. All of these aspects make CAS and ABM a useful alternative methodology for incorporating the many aspects of piracy.

Despite the fact that CAS were introduced over 30 years ago [18,19], there is little research on their use for solving business problems. This is may be due in part to the difficulty in representing key elements of business problems such as key levers, constituent “agents”, negotiations, rewards, fitness, etc. There have been some attempts to advance the state of knowledge of applying CAS to business problems. For example, Ben Said, Bouron, and Drogoul [3] used agent-based modeling (ABM) in a consumer market. The authors proposed a set of behavioral primitives for consumer agents which include imitation, conditioning, mistrust, and innovativeness. The system incorporates opinion leaders whose opinions are highly valued by consumers. Consumers learn over time and genetic algorithms are used for the evolution of consumers. The authors use ABM to provide operational and conceptual richness to capture a broad range of consumer behavior. This study illustrates the difficulty in capturing and generalizing key elements of agents' behavior.

ABM and CAS have been used to analyze pricing decisions under limiting assumptions without piracy. Tesauro and Kephart [34] analyzed pricing decisions of two firms selling an identical product. Consumers were assumed to behave deterministically and prefer the product with lower price. Sellers alternate in setting price for each period with full knowledge of the competitor's price and profit. The authors investigated the effects of using Q-learning on the sellers' behavior. Q-learning is an algorithm that incorporates long-term rewards into reinforcement. The results indicate that pricing policies derived with Q-learning reduce price wars and increase profitability. The results support earlier conclusions on the benefits of incorporating long-term consequences of actions into the learning reinforcement [33,37]. ABM has been used in other business applications such as to study the performance of a supplier selection models [36] and explore bidding strategies for market-based scheduling [27].

The proposed application provides a step in the longterm process of effectively applying CAS to business problems. It includes the identification of a) appropriate agents, b) their key properties, c) mechanisms for agents' learning, d) agents' goals, e) fitness functions, and f) key performance indicators. The subsequent steps in the development of CAS for solving business problems include refinements to the proposed CAS to better capture the above key elements, the addition of more agents to the system such as government and regulating agencies, and implementing learning for all agents in the system.

## 3. Agent-based modeling and Complex Adaptive Systems

Complex Adaptive Systems and ABM are bottom– up approaches for analyzing and understanding complex systems. We focus on a particular implementation of Complex Adaptive Systems (CAS) known as ABM. Entities in the system are modeled as agents whose behavior mimics that of real entities. Agents act according to their rules/schema. Agents can have a high degree of heterogeneity or be very similar. The actions and interactions of the agents in the system result in an aggregate behavior of the system [35]. Agents in business models are the actual players in the system, which include firms, consumers, and regulatory agencies. One can view ABM as social simulation, which is now possible due to increased computing power [30].

Several advantages of using CAS and ABM have been given in the literature. While these advantages may not be unique to CAS, their combination makes this method attractive. ABM does not require assumptions with regard to the behavior of the system [35]. Agents also provide a useful approach for modeling entities in many social problems [1]. The use of ABM enables us to use the wealth of information about agents' behavior, motives, and interactions to examine the consequences in terms of aggregate system behavior. Agents also provide a method for modeling heterogeneity [35].

CAS exhibit complex non-linear behavior brought about by interaction of agents. Agents influence the behavior of the system while, at the same time, the system influences the behavior of individual agents. The agents interact with the environment as well. CAS are networked in the sense that agents interact with their neighbors and, occasionally, distant agents, and non-linear in the sense that the whole is greater than the sum of its parts.

The main properties of CAS include self-organization, emergence, and adaptation. Ant colonies, networks of neurons, the Internet, the brain, and the global economy are a few examples where the behavior of the whole is much more complex than the behavior of its parts. Agents are autonomous entities with limited perception of their environment. They are guided by few simple rules and act locally. Agents' overall status and behavior can be tracked and evaluated. The performance of the overall system is derived from the effectiveness of the individual agents and their interaction. Agents may or may not have a history of their previous interactions and the ability to learn from them. Information about their past performance is used by the agents to determine the type and the degree of improvement in their behavior.

Agent interactions are mostly local; namely, they communicate with their immediate neighbors. Occasionally, as they move about, some agents get a chance to interact with other agents exhibiting plausible properties, regardless of the distance between the two agents. Their behavior is driven by a few, well-chosen rules. It is the interaction between agents, as well as the interaction between the agents and the environment that gives rise to the complexity of the system as a whole.

## 4. Complex adaptive systems and pricing under piracy

The proposed system is developed for a firm that has a monopoly for a copyrighted product. Each consumer has his/her value for the product. Thus, each consumer has his/her reservation price for the product, which is the maximum price he/she is willing to pay. This value is known to the consumer prior to consuming the product. While this assumption is similar to assumptions in some models in the literature [8], others authors assume that consumers update their fit-perception of the product after sampling it [6]. If the selling price is equal to or below the reservation price, a consumer will buy the product. If the selling price is higher than the reservation price, there is a probability that he/she may pirate the product. The pirating probability depends on several factors including access to copies that can be pirated, the availability of duplication technology, and the cost of the copying medium. A consumer's decision to pirate also depends on the penalty for pirating and the probability he/she assigns to being caught. Finally, the probability of pirating is an increasing function of the difference between the selling price and copying cost. The goal of the firm is to maximize total profit by periodically adjusting prices over the finite life of the product.

In applying CAS to pricing, or any similar problem, one must first identify the agents in the system and their rules. Agents in this problem include one seller and N consumers. IF/THEN rules are used to describe an agent — the IF part of the rule being the condition or state, and the THEN part is the action. Agents need not be homogenous and each agent has its own rules. The effectiveness of the pricing strategy is measured using the seller's profit. The following assumptions are made:

1. There is only one seller.

2. The goal of the seller is to maximize profits over the life of the product.

3. Advertising cost is a fixed amount per advertising campaign.

4. Consumers have complete information about the current price.

5. Each consumer may obtain only one copy of the product, legitimate or pirated.

The following notation is used:

t $1 , 2 , 3 , . . . , T ,$ a period index,

$i$ $1 , 2 , 3 , . . . , N ,$ a consumer index,

$Z _ { t }$ profit for period t,

$P _ { t }$ unit selling price during period t,

$\mathcal { Q } _ { t }$ number of legitimate products sold in period t, $q _ { t }$ number of pirated copies made in period $t ,$

$r _ { i , t }$ reservation price of consumer i in period $t ,$

$R _ { i }$ the risk cost consumer i assigns to pirating the product,

$d$ the cost of pirating which includes the cost of the storage medium and excludes the risk cost,

$c _ { i , t }$ probability of consumer i pirating the product in period $t ,$

$h _ { i }$ the number of neighbors of consumer i,

$A _ { t }$ advertising cost incurred in period $t , A _ { t } { = } A$ if $P _ { t } \neq P _ { t - 1 }$ and 0 otherwise.

$O _ { t }$ per period operating cost incurred for the product, $\pi _ { t }$ sum of all reservation prices of consumers without the product at the beginning of period $t ,$

$\pi _ { 1 }$ total reservation prices of all consumers prior to the introduction of the product,

$g$ $1 , 2 , 3 , . . . , G ,$ an index of an action the seller may implement at the beginning of a period,

j 1, $2 , . . , J ,$ a state condition of the system assessed at the end of each period, $\rho _ { g , j , t }$ the weight assigned to state/action pair $j / g$ at the at the end of period t.

All variables indexed by t are dynamic in terms of being recalculated each period in the simulation. All parameters indexed by t are dynamic in terms of the simulation being able to handle changes in their values from one period to the next. For many of these parameters $( r _ { i , t } , O _ { t } ,$ and $A _ { t } ) ,$ , the values are kept the same during a run of the simulation for the experiments in order to focus on the effects of piracy.

## 4.1. Seller's schema

Similar to industry practice, we assume the seller monitors sales and profit performance. As this data becomes available each period, which can be a week, a month, or a quarter, decisions are made and implemented. Therefore, we implement a periodic review system in which time increases in discrete units. A life cycle consists of $T$ periods. For example, a movie released on DVD may have a life cycle of up to 5 months with price changes allowed monthly. At the end of each period, the seller will have one of three states $( \mathrm { i } . \mathrm { e } . , j { = } 1 , 2 , 3 )$

1. the profit has increased from previous period: $Z _ { t } > Z _ { t - 1 } ,$

2. the profit has decreased from previous period: $Z _ { t } { < } Z _ { t - 1 }$ ， or

3. the profit is the same as in the previous period: ${ \cal Z } _ { t } { = } { \cal Z } _ { t - 1 }$

The seller may implement one of the following actions at the beginning of period t:

1. keep the current price unchanged (i.e. do nothing),

2. discontinue the product,

3. change the price to $P _ { t - 1 } ( 1 \pm 0 . 0 5 k ) , k \in [ 1 , 2 , 3 , 4 , 5 , 6 ] .$

The last action has 12 possible price changes resulting in a total of 14 possible actions $( \mathrm { i } . { \mathrm { e } } . \ g { = } 1 , . . . 1 4 )$ Multiples of $5 \%$ change is most common in practice. The above states and actions result in 42 state/action pairs. The initial selling price is user specified. However, a search for the best initial price can be incorporated. The seller advertises the product at the beginning of each period with a price change. At the end of each period, the seller detects the state of the system and takes an action, which is chosen probabilistically based on the weights assigned to each state/action pair.

To ensure that each action has an equal probability of being selected for each state at the beginning of a run, the initial weights of each state/action pair is set to 0.01. After executing the selected action, the weight of the selected state/action pair is changed based on its profit performance. During the run of the simulation, the weight assigned to the most profitable state/action pair increases until it has a probability close to 100% of being selected. The speed of convergence depends on the relative profitability of other state/action pairs. If one state/action pair is significantly more profitable than others, then the probability of selecting this state/action pair approaches 100% very quickly. If there are many state/action pairs with only slightly lower profit than the best state/action pair, then this convergence will take many runs of the simulation.

Fig. 1 shows flowcharts explaining the simulation for one product lifecycle (a run of the simulation includes many lifecycles). Every period, buyers interested in the product make decisions on buying, pirating, or waiting. The buyer's process is interrupted at the end of the period to let the seller evaluate the pricing strategy. Based on the change in profit during the period, actions are rewarded and a decision on which action to implement is made. The selection of actions depends on the weights of each state/action pair for the occurring state. A life cycle ends only when the seller implements the “discontinue the product” action. If the seller chooses discontinue the product, the lifecycle ends and all parameters are reset except for the weights of the state/action pairs which the seller retains since they were learned from past experience.

We consider two costs: An operating cost incurred every period, and an advertising cost incurred only when there is a price change. Since we deal with information goods, per unit cost of production is very small and, without loss of generality, we assume it to be zero. Therefore, the profit per period is:

![](/api/attachments/QC4U9FQV/fulltext/images/86f922f4796cf9027876b935915414d5c82a72b1a79e0059c0100d6d4cb73d3a.jpg)  
Fig. 1. Flowchart of the simulation.

$$
Z _ {t} = \left\{ \begin{array}{l l} Q _ {t} P _ {t} - A - O _ {t} & \quad \text {   If   } P _ {t} \neq P _ {t - 1} \\ Q _ {t} P _ {t} - O _ {t} & \quad \text {   Otherwise   } \end{array} \right.\tag{1}
$$

We tested three reinforcement learning methods:

Short-term profit reinforcement method (STPRM): The weight of a state/action pair at the end of a period is increased by the amount:

$$
\Delta_ {g, j, t} = \frac {Z _ {t}}{\pi_ {1}} = \frac {Q _ {t} P _ {t} - O _ {t} - A u (| P _ {t} - P _ {t - 1} |)}{\sum_ {i = 1} ^ {N} r _ {i , 1}}\tag{2}
$$

if $\Delta _ { g , j , t } { > } 0$ , where $u ( x )$ is a unit step function defined as $u ( x ) { = } 1 { \mathrm { i f ~ } } x { > } 0$ and 0 otherwise. Under this reinforcement scheme, each state/action pair is rewarded based on the profit it brings in the current period relative to the maximum total profit the product can bring.

Medium-term profit reinforcement method (MTPRM): For each consumer who obtains a copy of the product, $r _ { i }$ is set to zero since he/she is no longer willing to pay anything for the product. The weight of a state/action pair is increased by the amount:

$$
\Delta_ {g, j, t} = \frac {Z _ {t}}{\pi_ {t - 1}} = \frac {Q _ {t} P _ {t} - O _ {t} - A u (| P _ {t} - P _ {t - 1} |)}{\sum_ {i = 1} ^ {N} r _ {i , t - 1}}\tag{3}
$$

if $\Delta _ { g , j , t } { > } 0$ . Under this scheme, each action is rewarded based on the profit it brings in the current period relative to the total remaining profit the product can bring at the time the action is implemented.

Long-term profit dynamic reinforcement method (LTPDRM): The weight of a state/action pair is increased by the amount:

$$
\begin{array}{r l} \Delta_ {g, j, t} & = \frac {Z _ {t} + \pi_ {t}}{\pi_ {t - 1}} \frac {t}{E} 0. 0 0 1 \\ & = \frac {Q _ {t} P _ {t} - O _ {t} - A u (| P _ {t} - P _ {t - 1} |) + \sum_ {i} ^ {N} r _ {i , t}}{\sum_ {i = 1} ^ {N} r _ {i , t - 1}} \frac {t}{E} 0. 0 0 1 \end{array}\tag{4}
$$

if $\Delta _ { g , j , t } { > } 0$ , E is the total number of product life cycle runs. Under this reinforcement scheme, a state/action is rewarded based on the sum of profit it brings in the current period and the amount of profit it leaves in the market relative to the total profit remaining in the market at the time the action was implemented (i.e. in the previous period). In this scheme a time pressure giving actions some time before rewards get large is used so that no action is eliminated from consideration early in a run.

For all three reinforcement methods, at the end of period $t ,$ if $\Delta _ { g , j , t } { > } 0$ , then the weight of state/action pair $j / g$ is increased according to:

$$
\rho_ {g, j, t} = \rho_ {g, j, t - 1} + \Delta_ {g, i, t} \quad \text {   for   } g \text {   and   } j \text {   of   } t - 1\tag{5}
$$

Therefore, when the same condition occurs again, an action's chance of being selected increases with the profit it has provided in the past. If $\begin{array} { r } { \Delta _ { g , j , t } \le 0 . } \end{array}$ , then a penalty is charged to the state/action pair by decreasing its current weight by 10%. Hence, if $\Delta _ { g , j , t } \leq 0$ , then

$$
\rho_ {g, j, t} = 0. 9 0 \rho_ {g, j, t - 1} \quad \text { for   } g \text {   and   } j \text {   of   } t - 1\tag{6}
$$

Therefore, when the same state is realized in the future, this action has a lower probability of being selected. The selection of an action for a state is therefore based on the following procedure: If state $j$ occurs, then the probability of selecting action g is given by the weight of state/action pair $j / g$ divided by the sum of the weights for all state/action pairs of state $j ,$ which can be written as:

$$
p _ {g, j, t + 1} = \frac {\rho_ {g , j , t}}{\sum_ {x = 1} ^ {G} \rho_ {x , j , t}} \quad \text {   if   state   } j \text {   occurs   in   period   } t\tag{7}
$$

## 4.2. Rules — N consumer agents

There are N consumers and all have complete information about the current selling price. Each consumer has his/her own reservation price. Usually, companies use past information or surveys to measure reservation prices. We assume that reservation prices have a normal distribution with known mean and standard deviation. However, the system can deal with any known distribution. A consumer purchases the product if his/her reservation price is met, if the reservation price is not met then a consumer may pirate the product (with some probability) if a neighboring consumer has a copy, or wait.

A consumer pirates the product according to the following scheme. When the selling price is higher than the reservation price of a consumer who knows an agent with a copy, he/she may pirate the product. The pirating probability is calculated using.

$$
c _ {i, t} = \min \left\{\max \left\{\frac {P _ {t} - R _ {i} - d}{r _ {i , t}}, 0 \right\}, 1 \right\}\tag{8}
$$

Table 1  
Parameters used in numerical experiments

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Market size</td><td>10,000 consumers</td></tr><tr><td>Reservation prices, $</td><td>N~(15,3)</td></tr><tr><td>Initial price, $</td><td>8, 10, 12, 13.5, 15, 16.5, 18</td></tr><tr><td>Risk cost, $</td><td>N~(6,2), N~(3,1), 0</td></tr><tr><td>Cost of copying medium, $</td><td>1, 2</td></tr><tr><td>Number of neighbors</td><td>0, 1, 2, 4, 8, 16</td></tr><tr><td>Advertising cost, $</td><td>900, 3600</td></tr><tr><td>Operating cost per period, $</td><td>1200, 4800</td></tr><tr><td>Pirating technology</td><td>Copy from original, copy from copy</td></tr><tr><td>Seller&#x27;s reinforcement method</td><td>STPRM, MTPRM, LTPDRM</td></tr></table>

Eq. (8) implies that if the sum of the copying and consumer risk costs is greater than the selling price, then the consumer will not pirate. Otherwise, the probability of pirating increases as the difference between the selling price and the sum of the copying and risk costs increases. For each buyer, a uniform random variable is drawn from the interval [0,1] and if the number is smaller than $c _ { i , t } ,$ then he/she pirates. We assume that consumers' pirating risk costs are random variables from a normal distribution, however the system can handle any specified distribution.

We deal with two cases of the technology of piracy. In the first one, copies can be made only from legitimate copies and making copies from copies results in unacceptable degradation in quality. This is the case with audio and videocassette tapes and will be referred to as copy from original (CFO). In the second case, copies can be made from legitimate copies or from other copies without significant degradation in quality. This is the case with digital media such as music CDs and digital video disks (DVD) and will be referred to as copy from copy (CFC).

We assume that a consumer may be connected to other consumers (neighbors) and use different sizes of neighborhoods to observe the effects of technology. In the past, a consumer needed to have a physical legitimate copy of a product in order to copy it. The Internet and file compression technologies have eliminated such a requirement. This implies that a consumer's neighborhood is no longer defined by his/ her physical space, but rather by his/her technological network. If the number of neighbors is one, then a consumer located at coordinate $( x _ { i } , y _ { i } )$ has a neighbor at $( x _ { i } , y _ { i } + 1 )$ . If there are two neighbors, then there is an additional neighbor at $( x _ { i } , y _ { i } - 1 )$ . For four neighbors, there are two additional neighbors at $( x _ { i } + 1$ , y ) and $( x _ { i } - 1 , y _ { i } )$ . If a consumer has eight or sixteen neighbors, then they are located closest to him/her on the twodimensional grid.

## 5. Results from running the system and managerial implications

The system was developed using JBuilder 9 on a PC with a Pentium 4 and 1.0 GHz. Several experiments were conducted to test the system and examine the managerial insights it provides. The system was run with the parameters shown in Table 1.

The total number of parameter combinations (including the pirating technology and the seller's reinforcement method) is $7 \times 3 \times 2 \times 6 \times 2 \times 2 \times 2 \times 3 =$ 6048. The system was run with each possible parameter combinations for the same randomly generated population of consumers. Each run consisted of 1000 product life cycles, each with duration T (the time from the introduction of the product until the “discontinue the product” action is selected). Therefore, the simulation allows the seller to learn from selling many similar products each having a product life cycle of several periods (weeks or months). The seller's behavior and results from the most profitable life cycle, which was the most frequently occurring (learned) seller's behavior for majority of problems, was used for the analysis.

Of the three seller reinforcement methods, LTPDRM (long-term profit dynamic reinforcement method) and STPRM (short-term profit reinforcement method) were found to perform best. Surprisingly, MTPRM (mediumterm profit reinforcement method) did not perform as well as STPRM. The differences in the total maximum profits from using the different reinforcement methods were small. For example, LTPDRM outperformed STPRM by 1.55% (in terms of profit) for the CFC case whereas STPRM outperformed MTPRM by 0.68%. Since LTPDRM and STPRM performed best, we use the results from them for the analysis.

## 5.1. Identifying a good pricing strategy

The system can be used to identify a good, possibly optimal, pricing strategy for the seller. For example,

Table 2  
Identifying a good pricing strategy using CAS

<table><tr><td>Number of neighbors</td><td>Optimal pricing</td><td>Number of pirated products</td><td>Number of legitimate products</td><td>Profit</td></tr><tr><td>0</td><td>$16.50→$13.20→$9.90</td><td>0</td><td>9584</td><td>$103,889</td></tr><tr><td>1</td><td>$13.50→$9.45</td><td>1123</td><td>8740</td><td>$93,920</td></tr><tr><td>2</td><td>$12.00</td><td>975</td><td>8414</td><td>$92,568</td></tr><tr><td>4</td><td>$12.00</td><td>1228</td><td>8414</td><td>$92,568</td></tr><tr><td>8</td><td>$12.00</td><td>1378</td><td>8414</td><td>$92,568</td></tr><tr><td>16</td><td>$12.00</td><td>1478</td><td>8414</td><td>$92,568</td></tr></table>

![](/api/attachments/QC4U9FQV/fulltext/images/70625100c80e576e4fcfa7c9bd1c5d09eb210928263e5996e418c4ede66b1661.jpg)  
Fig. 2. Profit as a function of initial price for different consumer connectivity CFC and STPRM, $\scriptstyle A _ { t } = \$ 3600$ , O = \$4800, $R _ { i } = 6 ,$ , and $d { = } \mathbb { S } 1$

Table 2 shows the optimal pricing strategy for $E ( R _ { i } ) =$ $\ S 6 . 0 0 , d { = } \ S 1 . 0 0 , { \cal O } { = } \ S 4 8 0 0 , { \cal A } { = } \ S 3 6 0 0 , \mathrm { C F O } ,$ , and LTPDRM. As the table shows, under no piracy (i.e. zero neighbors), it is best to introduce the product at a price of \$16.50, reduce the price to \$13.5 in the next period, and then to \$9.90 in the last period before discontinuing the product. The total profit in this case is \$103,889. If each consumer is connected to two neighbors, then it is best to use a single price of \$12.00 and the total profit is \$92,568. It is possible to use different initial prices to find a better strategy for each level of consumer connectivity. For example, for the case of 1 neighbor, since \$13.50 was the best initial price out of the seven tested initial prices, an experiment with initial prices between \$12.00 and \$15.00 with increments of \$0.50 can be performed.

## 5.2. Piracy and the effectiveness of skimming strategies

Piracy reduces the effectiveness of a skimming strategy, which the literature indicates to be the most suitable strategy for monopolists with no piracy. Before improvements in technology led to increased piracy, firms operated on or close to the top curve of Fig. 2 (i.e. little or no piracy). However, as the curve shows, starting with a high price and reducing that price over time is less effective as the number of neighbors increases. When the number of neighbors is 4 or more, which is common nowadays due to the Internet, it is best to use a single price of \$12 per unit. The skimming strategy may be very suboptimal when the number of neighbors is large.

## 5.3. Impact of consumer connectivity on profit

The number of neighbors, i.e. connectivity of consumers, has a strong effect on profits in both the CFO and CFC cases. Fig. 3 shows the profit for both CFC and CFO for different number of neighbors for an initial price of \$16.50. As the figure shows, the effect of consumer connectivity on profit is strongest when the number of neighbors is small (less than 8 neighbors). The worst scenario for the monopolist is when consumers have high connectivity and copies can be made from copies. Unfortunately this is the situation many firms face today due to the availability of most products in digitized form, the good quality of compression technology, the decreased cost of bandwidth, and the low cost of CD burners. In this respect, piracy reduces the monopoly power firms in the music and movie industries enjoyed in the past.

## 5.4. Impact of consumer connectivity and initial price on diffusion of pirated copies

The number of neighbors has a strong impact on the rate of diffusion of pirated copies in the market, especially when the initial price is high. As Fig. 4 shows, a significant increase in the number of pirated copies begins to appear for 4 neighbors as compared to 2 and 1— neighbors at an initial price of about \$13.50. The implies is that while the number of copies in the market may remains relatively unchanged, using high initial price changes the mix of these products in favor of pirated copies.

## 5.5. Impact of copying medium and risk costs on profit

In many cases, firms selling reproducible products such as music CDs increase their deterrent controls to curtail piracy and to maintain a skimming approach to the market. Some governments have even added a tax on the copying medium and equipment to deter piracy and compensate the sellers [5]. The success of a skimming strategy will largely depend on the ability of a firm to increase the piracy risk cost of consumers. Fig. 5 shows that the increase in the risk cost has to be large in order for it to have an impact on the success of a skimming strategy. At an initial price of \$18.00, an increase of consumer pirating risk cost from 0 to an average of \$6.00 and an increase in the copying medium cost from \$1 to \$2 result in about \$5000 increase in profit. For this investment in deterrent control to be successful, the additional revenue from taxing the copying medium and the additional \$5000 increase in profit must be larger than the expenditure on deterrent controls needed to increase the risk cost. This may explain the strength of the campaigns of the record labels in litigating against individual pirates to substantially increase their assessment of the risk of being caught and the size of the penalties. However, Fig. 5 indicates that decreasing the initial price is much more effective in increasing profit than increasing the expenditure on piracy controls.

![](/api/attachments/QC4U9FQV/fulltext/images/a27ac1343ca8136c96a9d99854288df61baf49bfd1f15291843c89f28181577d.jpg)  
Fig. 3. Profit as a function of number of neighbors STPDRM, $A _ { t } =$ \$3600, O=\$4800, R =6, d=\$1 and $P _ { 1 } { = } \$ 16.50$

![](/api/attachments/QC4U9FQV/fulltext/images/b54f59199e30b5618cde88c084fa78a3a9a48acc5da13404e468f72cee95b82e.jpg)  
Fig. 4. Diffusion of pirated copies as a function of initial price for different consumer connectivity CFC, STPRM, A<sub>t</sub>= \$3600, O= \$4800, R =6, and d=\$1.

## 5.6. Piracy is becoming a more significant factor with time

In the early 1990s, the major technology for music and movie distribution was magnetic tapes (audio or video). By the late 1990s, CDs became the standard technology for music distribution. Now, digital video disks DVD is the standard technology for movie distribution. These changes led significant improvement in the ability of consumers to make good copies from other copies. At the same time, the Internet allows music files to be transmitted between consumers without physical contact. Increased bandwidth and decreasing cost will soon allow the same for transmission of movies. Therefore, a consumer can have a neighbor providing a product for piracy who is located in a different geographical region. Fig. 6 shows the significant combined effect of consumer connectivity and reproduction technology on profit. Earlier technology is represented by the CFO and N = 1 whereas modern technology is represented by CFC and N =16. At high initial prices, such as 10% above the mean reservation price (i.e. \$16.50), the decrease in profit due to improved consumer connectivity and reproduction technology is \$44,949 (51%). Even for an initial price equal to the average reservation price (i.e. \$15), the decrease in profit is \$25,966 (12%).

![](/api/attachments/QC4U9FQV/fulltext/images/0972a5968df73c2e611f9eaf9119a88c693ee69a00895313a5bec65e16723ea1.jpg)  
Fig. 5. Profit as a function of initial price for different copying and risk costs CFC, STPRM, A =\$3600, O=\$4800, and N=4.

![](/api/attachments/QC4U9FQV/fulltext/images/eaaf3c93f41a66a51248e765a68853166d96199b29b2cbd1abd31824745f66b2.jpg)  
Fig. 6. Combined impact of the consumer connectivity and technology on profit STPRM, A =\$3600, O=\$4800 R =6, and d=\$2.

## 5.7. Piracy and consumer welfare

From a social welfare perspective, it is optimal to allocate products to all consumers with positive utilities. Assuming the seller uses a profit-maximizing price, Fig. 7 shows the number of consumers with a copy of the product, legitimate or pirated, as a function of the initial price. As the figure shows, piracy mitigates the effect of the monopolist's pricing on product diffusion. As the monopolist raises the initial price in an attempt to skim the market, consumers respond by pirating the product rather than waiting until the selling price drops to or below their reservation prices. It is noteworthy that the total number of consumers who obtain the product remained stable at about 10,000 over all initial prices in the range of \$8–\$18. This switch of many consumers to piracy has empirical support in the literature. Peitz and Waelbroeck [24] used the data from the International Federation of the Phonographic Industry (IFPI) World Report of 2003 to investigate the legitimacy of the RIAA's claim that music downloads are causing a large decrease in music sales. Analysis of the data shows that music downloading alone could have caused as high as a 20% reduction in music sales worldwide between 1998 and 2002. This effect does not include the effects of CD burning and organized piracy which may account for another significant amount of lost sales.

![](/api/attachments/QC4U9FQV/fulltext/images/f1ba5222e35659e9876adb93686c2e2a7df1379a3514fcc159adedeb901aee5c.jpg)  
Fig. 7. Piracy and product diffusion STPRM, $A _ { t } { = } \$ 3600$ , O=\$4800 $R _ { i } = 6 ,$ and d=\$1.

## 5.8. Piracy and decrease of royalty for the creator

Creators of reproducible goods, such as music writers, singers, and actors, are frequently different from the monopolist selling the product. Creators usually receive royalty for each legitimate product sold. This royalty can be a fixed amount per unit sold or a percentage of the price. Incorporating this royalty as a fixed amount per unit sold does not change the reward structure of the monopolist, whereas having it as a percentage of the selling price may change the reward structure. If the monopolist acts based on the STPRM and \$3 of royalty is paid to the creator per legitimate product sold, then the total royalty paid to the creator is shown in Fig. 8. As the figure shows, the creator's royalty suffers only a small decrease because of a high initial price when there is only one neighbor and copies can be made only from legitimate products. Again, this was the scenario creators had before digitization, the Internet, and compression technologies. The decline in royalty due a high initial price (i.e. a skimming strategy) is much more significant for high consumer connectivity (N=16) and improved copying technology (CFC).

![](/api/attachments/QC4U9FQV/fulltext/images/ec0187287a6cf10705bed3468fe6e00da8530d2f2595dcc17e5fe0fdf8041939.jpg)  
Fig. 8. Piracy and creator's royalty STPRM, $\scriptstyle A _ { t } = \ S 3 6 0 0 .$ , O=\$4800 $R _ { i } = 6 ,$ and d=\$1.

The results from the system are robust over repeated runs in the sense that the best pricing strategy for each problem (i.e. parameter combination) and the learned (i.e. most frequently used) pricing strategy were the same for over 90% of the problems. In other words, the same profit-maximizing behavior seems to be learned by the seller for most problems. In addition, in an experiment where a new consumer population was generated for each run of a problem, the seller's pricing behavior in terms of the number of price drops remained the same as in the single consumer population runs. The exact prices and profit amounts were different due to the randomness of each newly generated consumer population.

The choice of the initial weight to assign to each state/ action pair and penalty scheme may have an impact on how quickly the simulation converges to the best pricing policy. However, its impact on the resulting best pricing policy and best profit identified by the simulation should be negligible. We experimented with different initial weights and penalties and found the results to be robust. For example, for problems with CFO, LTPDRM and 1 neighbor, initial weights of 0.005 and a penalty of 15% resulted in best profits within 0.1% of the profits obtained with initial weights of 0.001 and penalty of 10% for 160 out of the 168 problem instances.

The developed system can incorporate additional real world aspects such as 1) declining interest in the product over time, which can be incorporated as a downward trend in the average reservation price over time, 2) effects of Internet technology, which can be modeled as random connections between consumers in the system, 3) effects of legal and education campaigns to deter piracy, which can be modeled as decreases in consumers' probability to pirate, and 4) the effects of injecting some bad copies in the market to discourage piracy, which some firms have used to deter piracy. Furthermore, we assumed that consumers considers piracy only if their reservation prices are not met. The system can deal with other possibilities such as a consumer deciding whether to pirate or purchase the product based on the expected gain, or try to pirate first and only purchase if unable to pirate, or can use a mix of these and other rules. However, this will lead to different results in terms of the experiments. In short, the proposed system is flexible enough to handle many aspects of the problem that would have been difficult to incorporate using different problem solving approaches.

## 6. Conclusion and suggestions for future research

Experiments indicate that CAS and ABM are useful tools for firms in pricing products under piracy. The system can be used to identify the best pricing policy in terms of the best initial price and subsequent price changes. Numerical experiments suggest that under moderate to strong piracy, which is characterized by high consumer connectivity and ability to make copies from copies, the skimming strategy becomes unprofitable and it is better to have a single price. In addition, discouraging piracy by taxing the copying medium and equipment and by increasing deterrent control may not work well. Specifically, the results suggest that for this kind of control to work, consumers' perception of the probability of being caught and the size of the penalty they will incur must substantially increase.

Interestingly, piracy causes the number of products, legitimate or pirated, in the market to be relatively independent of the monopolist's pricing policy. If the monopolist raises prices, consumers respond by more piracy. In this respect, piracy erodes the power monopolists have had in some industries. The ultimate victim of piracy may be the creator of the information good who gets a fixed dollar amount per legitimate product sold in royalty. Therefore, many consumers thinking that piracy is a victimless crime may be mistaken, especially for products like music CDs.

The proposed system has several limitations. The product modeled in this system does not lose value since the time of its release. This implies that the product does not undergo deterioration and is not subject to obsolescence. An inventoried item subject to obsolescence incurs little or no physical damage until moment of obsolescence, whereas an inventoried item subject to deterioration will degrade overtime, thereby reducing its market value [15]. Furthermore, learning on the part of consumers is not incorporated into the system. Some consumers, after observing pricing patterns of products, may be willing to wait for one or more price reductions before purchasing a product.

CAS methodology provides many opportunities for further analysis of pricing under piracy. Several extensions of our model are planned including 1) allowing agents to move in the system (such movement of consumers is common and it may lead to further diffusion of piracy), 2) incorporating consumers' declining interest in the product over time. For many information goods, life cycles are short and products compete with many others for limited consumer disposable income; consumers' declining interest in the product can be modeled as a stochastic downward trend in reservation prices over time. Such a decrease in the consumer interest can be incorporated in the simulation using new reservation prices given by ${ r _ { i , t } } \mathrm { { = } } { \delta _ { i } } { r _ { i , t - 1 } }$ every period, where $\delta _ { i }$ is generated from a uniform distribution on $[ a _ { I } , a _ { 2 } ]$ . For example, a range of [.95,1] implies that the reservation prices decrease on average by 2.5% every period, and 3) examining global piracy and its implications. Under global piracy there are many relatively homogenous agents within regions and heterogeneous agents between regions in terms of disposable income and cultural dimensions which influences piracy. Furthermore, there are considerable variations in the environments of different regions in terms of the existence and the degree of enforcement of piracy control laws. Varying technology and quality standards between regions further complicates the problem. Because of the complexity arising from all of these factors, CAS may be a good approach to understanding global piracy, which in turn will enable better decision making by policy makers.

For the proposed model to be used in industry, measures of the parameters must be obtained. Some parameter estimates such as the one for connectedness may be estimated based on available data. Internet access statistics may give a good idea of how connected consumers in a particular region are. For example, according to Internet World Statistics [16], 68.1% of Americans are Internet users. Other data such as assessment of consumer risk cost may require market research.

In developing CAS for pricing, several issues were found to be key to successfully applying this methodology to business problems. One important issue is designing the reward/reinforcement methods for firms. The key questions here include: 1) how should different actions be rewarded. Some actions may optimize short term performance, but significantly sub-optimize longterm performance, 2) how should the reward/reinforcement methods balance the objectives of having emergence to the best actions while at the same time not reinforcing actions quickly causing other good actions to be eliminated prematurely. For example, suppose two actions (A and B) out of several actions for the same state have the best long-term profits with action B having larger profit. If action A is selected more frequently in the beginning of the simulation than action B due to chance, then its future chances of being selected may increase very quickly relative to action B and may therefore emerge as the best action for that state. Another important issue is the representation of consumer agents. The key questions here are 1) is there a general approach for representing consumers which can be used in different applications, and 2) how do consumers learn from each other, market leaders, and other sources, and 3) how to incorporate consumers' memory into the system and how does that memory effect their behavior?

## References

[1] S.C. Bankes, Agent-based modeling: A revolution? Proceedings of the National Academy of Sciences 99 (Supplement 3) (2002) 7199–7200.

[2] P. Belleflamme, Pricing information goods in the presence of copying, Department of Economics at Queen Mary University of London, Working Paper, vol. 463, 2002, http://www.econ.qmul. ac.uk/papers/doc/wp463.pdf.

[3] L. Ben Said, T. Bouron, A. Drogoul, Agent-based interaction analysis of consumer behavior. Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems: part 1, Bologna, Italy, 2002, pp. 184–190.

[4] J. Bishop, Who are the pirates? The politics of piracy, poverty, and greed in a globalized music market, Popular Music and Society 27 (1) (2004) 101–106.

[5] R.K. Chellappa, S. Shivendu, Economic implications of variable technology standards for movie piracy in a global context, Journal of Management Information Systems 20 (2) (2003) 137–168.

[6] R.K. Chellappa, S. Shivendu, Managing piracy: pricing and sampling strategies for digital experience goods in vertically segmented markets, Information Systems Research 16 (4) (2005) 400–417.

[7] Y. Chen, I.P.L. Png, Software pricing and copyright enforcement: private profit vis-à-vis social welfare, Proceedings of the 20th International Conference on Information Systems, Charlotte, North Carolina, USA, 1999, pp. 119–123.

[8] Y. Chen, I.P.L. Png, Information goods pricing and copyright enforcement: welfare analysis, Information Systems Research 14 (1) (2003) 107–123.

[9] J.S. Chiou, C.Y. Huang, H.H. Lee, The antecedents of music piracy attitudes and intentions, Journal of Business Ethics 57 (2) (2005) 161–174.

[10] K.R. Conner, R.P. Rumelt, Software piracy: an analysis of protection strategies, Management Science 37 (2) (1991) 125–139.

[11] J. Dean, Pricing pioneering products, Journal of Industria Economics 17 (3) (1969) 165–179.

[12] E.J. Dockner, G.E. Fruchter, Dynamic strategic pricing and speed of diffusion, Journal of Optimization Theory and Applications 123 (2) (2004) 331–348.

[13] M. Givon, V. Mahajan, E. Muller, Software piracy: estimation of lost sales and the impact on software diffusion, Journal of Marketing 59 (1) (1995) 29–37.

[14] R.D. Gopal, G.L. Sanders, Preventive and deterrent controls for software piracy, Journal of Management Information Systems 13 (1997) 29–47 (Spring).

[15] S.K. Goyal, B.C. Giri, Recent trends in modeling of deteriorating inventory, European Journal of Operational Research 134 (1) (2001) 1–16.

[16] Internet World Statistics, 2006 http://www.internetworldstats. com/index.html.

[17] E. Haruvy, V. Mahajan, A. Prasad, The effect of piracy on the market penetration of subscription software, The Journal of Business 77 (2) (2004) S81–S108.

[18] J. Holland, Adaptation in Natural and Artificial Systems, University of Michigan Press, 1975.

[19] J. Holland, Hidden Order: How Adaptation Builds Complexity, Addison–Wesley, 1995.

[20] T. Moores, J. Chang, Ethical decision making in software piracy: initial development and test of a four-component model, MIS Quarterly 30 (1) (2006) 167–180.

[21] F. Nascimento, W.R. Vanhonacker, Optimal strategic pricing of reproducible consumer products, Management Science 34 (8) (1988) 921–937.

[22] P.M. Noble, T.S. Gruca, Industrial pricing: theory and managerial practice, Marketing Science 18 (3) (1999) 435–454.

[23] T. Papadopoulos, Pricing and pirate product market formation, Journal of Product & Brand Management 139 (1) (2004) 56–63.

[24] M. Peitz, P. Waelbroeck, The effect of internet piracy on music sales: cross-section evidence, Review of Economic Research on Copyright Issues 1 (2) (2004) 71–79.

[25] A. Prasad, V. Mahajan, How many pirates should a software firm tolerate? An analysis of piracy protection on the diffusion of software, International Journal of Research in Marketing 20 (4) (2003) 337–353.

[26] L. Rainie, M. Madden, Preliminary findings from a web survey of musicians and songwriters, Pew Internet & American Life Project, 2004.

[27] D.M. Reeves, M.P. Wellman, J.K. MacKie-Mason, A. Osepayshvili, Exploring bidding strategies for market-based scheduling, Decision Support Systems 39 (1) (2005) 67–85.

[28] O. Shy, J.F. Thisse, A strategic approach to software protection, Journal of Economics and Management Strategy 8 (2) (1999) 163–190.

[29] H. Simon, Pricing opportunities — and how to exploit them, Sloan Management Review 33 (2) (1992) 55–66.

[30] A. Srbljinović, O. Skunca, An introduction to agent based modeling and simulation of social processes, Interdisciplinary Description of Complex Systems 1 (1–2) (2003) 1–8.

[31] A. Sundararajan, Managing digital piracy: pricing and protection, Information Systems Research 15 (3) (2004) 287–308.

[32] L. Takeyama, The welfare implications of unauthorized reproduction of intellectual property in the presence of network externalities, Journal of Industrial Economics 62 (2) (1994) 155–166.

[33] G.J. Tesauro, J.O. Kephart, Foresight-based pricing algorithms in agent economies, Decision Support Systems 28 (1–2) (2000) 49–60.

[34] G.J. Tesauro, J.O. Kephart, Pricing in agent economies using multi-agent Q-learning, Autonomous Agents and Multi-Agent Systems 5 (3) (2002) 289–304.

[35] P. Twomey, R. Cadman, Agent-based modeling of customer behaviour in the telecoms and media markets, Info -, The Journal of Policy, Regulation and Strategy for Telecommunications 4 (1) (2002) 56–63.

[36] A. Valluri, D.C. Croson, Agent learning in supplier selection models, Decision Support Systems 39 (2) (2005) 219–240.

[37] J.M. Vidal, E.H. Durfee, Learning nested agent models in an information economy, Journal of Experimental and Theoretical Artificial Intelligence 10 (3) (1998) 291–308.

[38] C.C. Wang, Factors that influence the piracy of DVD/VCD motion pictures, Journal of American Academy of Business 6 (1) (2005) 231–237.

![](/api/attachments/QC4U9FQV/fulltext/images/7ecb79f4917148ba4e681e51e70598416be58518e4e0a3fd938ec211b7e906d2.jpg)  
Dr. Moutaz Khouja is a Professor of Operations Management in the Belk College of Business Administration at the University of North Carolina at Charlotte. He received his PhD in Operations Management from Kent State University. His publications have appeared in many leading journals including Decision Sciences, IIE Transactions, European Journal of Operational Research, International Journal of Production Research, International Journal of Production Economics, Journal of the Operational Research Society, and OMEGA.

![](/api/attachments/QC4U9FQV/fulltext/images/b28b0f492b47c5bdabbd48ae2cdbeed7a4ae88c1011d4286b8306a9c6e44554c.jpg)

Dr. Mirsad Hadzikadic joined the UNC Charlotte faculty in 1987 after receiving his Ph.D. in Computer Science from Southern Methodist University where he was a Fulbright Scholar. In addition to publishing his scholarship, he has made presentations at national and international conferences, leading information technology firms, and universities. His research/scholarship activities have been primarily focused on three areas: data mining, cognitive science, and medical informatics. From 1991 to 1997, he served as

the Director of the Department of Medical Informatics and Department of Orthopedic Informatics of the Carolinas HealthCare System. In 1998, he joined Deloitte and Touche Consulting Group as Manager in the Health Systems Integration Service Line. He returned full time to the University in January 1999 to assume the chair position in Computer Science and serve as Director of the Software Solutions Lab. Currently, he is serving as the Dean of the College of Computing and Informatics.

![](/api/attachments/QC4U9FQV/fulltext/images/26022cce316776fef4aa2d514247205a9e8bcfdc5de7c8a498b8534f34f1d63a.jpg)

Dr. Hari K. Rajagopalan earned his PhD in Information Technology from the University of North Carolina at Charlotte in 2006. Apart from his PhD he also has an MBA in Finance and an MS in Computer Science. His research interests include locating emergency response systems, pricing of digital products and obsolescence in the high technology industry. His research has published in the European Journal of Operational Research, Computers and Operations Research and other journals.

He is also an active participant at INFORMS, Decision Sciences and European Working Group in Transportation Meeting and Mini EURO Conferences. He is currently the Assistant Professor in Management at Francis Marion University.

![](/api/attachments/QC4U9FQV/fulltext/images/94956f42be0be9955b277aadf4b20ef8da76fb0b7d59a1c3cfb5f33afdf22f59.jpg)

Dr. Li-Shiang Tsay earned her M.S. and Ph. D. degrees in Computer Science and Information Technology from the University of North Carolina at Charlotte in 2003 and 2005, respectively. Her research has been published in journals and books including Foundations of Data Mining, Data Mining: Foundations and Practice, Encyclopedia of Data Warehousing and Mining, and Journal of Experimental and Theoretical Artificial Intelligence. Her research has also been presented at

international conferences including IEEE GrC, IEEE ICDM Workshop, IEEE/WIC/ACM, IIS, SPIE, and ISMIS. She has served and is serving on several Program Committees of international conferences, including ISMIS'06, IRMA'07, and RSEISP'07. She is an Assistant Professor of Computer Science at Hampton University since January 2006.
