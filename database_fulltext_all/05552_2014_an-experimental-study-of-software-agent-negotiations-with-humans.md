---
otero_id: 5552
otero_key: "R7Y462J4"
title: "An experimental study of software agent negotiations with humans"
authors: "Rustam Vahidov; Gregory Kersten; Raafat Saade"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Rustam Vahidov ⁎, Gregory Kersten, Raafat Saade

Department of Supply Chain & Business Technology Management, John Molson School of Business, Concordia University, Montreal, Quebec, Canada

a r t i c l e i n f o

Article history: Received 24 January 2014 Received in revised form 6 May 2014 Accepted 19 June 2014 Available online 28 June 2014

Keywords: Electronic negotiations Software agents Software–human negotiations Experimental studies

## a b s t r a c t

Electronic negotiations allow participants to negotiate online and use analytical support tools in making their decisions. Software agents offer the possibility of automating negotiation process using these tools. This paper aims at investigating the prospects of agent-to-human negotiations using experiments with human subjects. Various types of agents have been con<sup>fi</sup>gured using the following tactics: individualistic, neutral, yielding, yielding-then-individualistic, and absolute tit-for-tat. These agents were paired up with human counterparts for negotiating product sale. A set of hypotheses has been proposed involving the performance of agents, as well as humans in terms of objective, as well as subjective measures. Overall, the <sup>fi</sup>ndings speak in favor of agent-managed negotiations.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Negotiation is a powerful and <sup>fl</sup>exible mechanism that allows two or more parties to search for acceptable agreements. While negotiations are less structured than other mechanism families, i.e., catalogs and auctions, they nonetheless allow for the parties to be actively involved in the process of exchange. Online negotiations supported by electronic negotiation systems (ENS) allow spatially separated parties exchange offers over the internet [21]. ENS can be used to structure the offer exchange to a different degree (e.g., by requiring an explicit speci<sup>fi</sup>cation of issues and options or exchanging plain text only). They may also incorporate analytical toolboxes for supporting negotiators in their preparation and conduct of negotiations, as well as post-negotiation analysis. This support can range from tools used to capture and model the negotiator's preferences, to provide active advice and critique, and even to automate the negotiation on behalf of human principals.

While a bulk of research on the design and evaluation of ENS has been produced in the recent past, in reality only few commercial sites offer such capabilities to their customers. One such commonly known website that allows customers to make (a limited number of) offers is Priceline.com. Other examples include car dealer sites with the “make us an offer” option. In B2B exchanges, a site like Alibaba lists available products with the possibility to send a message to the supplier containing offers. Yet, negotiations do not represent a dominant model of exchange in either B2C or B2B segments.

A possible explanation to the scarcity of negotiating websites is that negotiations imply a relatively high cognitive load, especially if multiple issues are involved (e.g. price, warranty, product attributes, shipment, etc.). This load may translate into a prohibitive cost when day-to-day transactions involving people who are not negotiation experts are concerned. Additionally, with multiple issues involved, because of bounded rationality of human decision makers, as well as psychological factors they may end up making less consistent decisions.

Automated negotiations as a <sup>fi</sup>eld that was established over the past couple of decades [1,20] promise to relieve human beings from the above efforts, while taking advantages of the bene<sup>fi</sup>ts offered by negotiation mechanism. Software agents are autonomous active software units that facilitate negotiation automation by employing various negotiation strategies and tactics. The potential role of agents in B2C and B2B transactions, negotiations in particular has long been recognized [16,18,33].

According to Lin and Kraus [28] agents can alleviate negotiationrelated efforts, help people with limited negotiation skills, and also help with training successful negotiators. Yan and Singhal [53] give the following bene<sup>fi</sup>ts of using negotiation agents as follows: time saving with lower opportunity costs; fewer negative effects, and more ef<sup>fi</sup>cient settlements. While past work on design and study of agentto-agent negotiations has been substantial, relatively little experimental work has been done in assessing the potential of human customer vs. software agent negotiations in terms of objective as well as subjective variables.

The purpose of this work is to investigate the prospects of human– software agent negotiations in experimental settings. This is an important question as it relates to the prospects of employing software negotiation agents in practice. To this end an electronic negotiation system incorporating software agents has been built. The system was used in experiments with human subjects to measure such outcomes as utility of agreements and number of agreements. Additionally, such subjective variables as satisfaction and perceived usefulness were also measured.

The remainder of the paper is organized as follows. The next section reviews the relevant past work on negotiation software agents' tactics, designs, frameworks, and experimental studies. The following section discusses theoretical model for the study and puts forward hypotheses based on the past work and expectations from negotiating agents. The paper further describes the ENS and con<sup>fi</sup>guration of software agents used in the experiments. Next, the experimental setup is described, including the negotiation case. The paper further presents the results of the experiments, including the hypotheses tests. The paper concludes with the discussion of <sup>fi</sup>ndings, limitations, and directions for future research.

## 2. Background

Yang and Singhal [53] distinguish the following three categories of agent involvement in negotiations: (1) human-to-human negotiations with agents providing active support; (2) agent-to-agent negotiations where the process is fully automated, and (3) human-to-agent negotiations, where one party is a software agent, while the other one is a human. Research in the <sup>fi</sup>rst category concerns use of agents as advisors to help human negotiators cope with complex multi-issue negotiations and stay in line with their declared preference structures and concession-making policies. Examples include the work on Aspire agent [24] and eAgora marketplace [6]. Experimental study involving eAgora system showed that human negotiators using advise-giving agents performed better in complex (multi-issues) tasks than unaided human negotiators [46]. Research in second category, as mentioned earlier, has been extensive and is beyond the scope of the current paper. The third category is most suitable for the work presented here, and we will discuss past studies on human–agent negotiations further in the section.

Lomuscio et al. [31] propose a classi<sup>fi</sup>cation scheme for automated negotiations. Part of this classi<sup>fi</sup>cation includes cardinality of negotiations as consisting of two parts: negotiation domain: single vs. multiple issues; and number of participants: one-to-one, one-to-many, and many-to-many. The latter category includes complex scenarios involving simultaneous interactions of many buyers with many sellers. Continuous double auctions come closest to theses setups among the widely used exchange mechanisms. One-to-many scenarios involve multi-bilateral negotiations with one side (buyer or seller) interacting with multiple counter-parts at the same time. Examples of relevant work include: [35,45,48,49,51]. In this work we are primarily interested in one-to-one negotiations where one party is an agent, while the other is a human.

Another component of the classi<sup>fi</sup>cation scheme according to Ref. [31] is agent characteristics, with bidding strategy being one of the components. The latter relates to the negotiation strategy/tactics and it has considerable implications for the negotiation performance. In Ref. [32] the following set of tactics for agents was introduced: stalemate (no concession), tough (small concessions), moderate (moderate concessions), soft (large concessions) and compromise (complete concession). Faratin et al. [12] have introduced families of tactics that could be <sup>fl</sup>exibly de<sup>fi</sup>ned for software agents. According to the authors, the tactics are used to decide on what offer to make at a given point in the negotiation process. Negotiation strategies, on the other hand, refer to the choice of tactics based on history, context, and other variables.

The tactics were divided into three categories: behavior-dependent, time-dependent, and resource-dependent. The <sup>fi</sup>rst family bases its choice of offer on the moves made by the parties. Various forms of tit-for-tat tactics had been presented in this category. Time-dependent tactics model concession-making as a function of time elapsed between the beginning of negotiation and the estimated ending point. Functions that dictated small concessions in the beginning (negative second derivative over time) corresponded to tougher competitive behavior, and were named (perhaps, somewhat controversially) boulware tactics. Those that implied early large concessions were named conceder tactics. Time-dependent strategies were employed in early experiments using Kasbah marketplace [4,5]. Resource-dependent tactics aimed at adjusting concession levels based on a given resource scarcity. In Ref. [34] an idea of evolving agent strategies using the above set of tactics in genetic algorithms has been advanced, along with simulation results. Recently, a model for a negotiation agent taking into account the dynamics of the market (including the number of participants and changing objectives) has been proposed [41]. The model, however, was limited to single-issue negotiations.

The weakness of time-and resource-dependent tactics is lack of accounting for the counterpart's actions, which has a strong in<sup>fl</sup>uence in human-to-human negotiations. Tit-for-tat family of tactics considers the counterpart's moves and one such tactic has been proposed in Ref. [42]. Here, agents exchange their concession priority vectors, with the negotiators attempting to meet their counterpart's priority, while using their utility gain from a previous offer by the opponent as an upper limit for their concessions.

In Ref. [26] simulation studies involving two-issue negotiations were performed for comparing the performance of a range of tactics. The <sup>fi</sup>ndings imply that absolute tit-for-tat and boulware tactics performed better than most others. Filzmoser [14] has compared a set of negotiation strategies in a simulation environment using agents, which incorporated preferences of human subjects from the dataset of past negotiation experiments. He compared the performance of agents with the outcomes obtained by human negotiators in those past experiments. No direct agent–human negotiations were performed. The offer generation strategies included monotonic, strictly monotonic, least cost issue, and lexicographic ones. These were combined with concession strategies, and with the aforementioned tit-for-tat strategy by Shakun for a total of nine strategies. The comparison of agents performance with human performance in the past had produced mixed results [14].

Lin and Kraus [28] have discussed the possibility of designing agents that could pro<sup>fi</sup>ciently negotiate with human counter-parts. The challenge of designing such agents, according to the authors includes bounded rationality and incomplete information [28]. The authors proposed several guidelines for agent designers, including randomization (to prevent manipulation of an agent by an opponent), having concession strategy, and maintaining a database of past interactions (for modeling the opponents). In Ref. [53] a set of propositions that could serve as guidelines for designing negotiation agents has been advanced. The authors stated that better outcomes can be achieved by: making a tough initial offer; making simultaneous equivalent (to an agent) offers; making monotonously decreasing concessions (based on Raiffa's [39] suggestion on signaling “approaching the limit”); making large concession in the <sup>fi</sup>nal offer; and using strategic delays.

There also have been a number of publications describing design of negotiation systems incorporating agent and human participants. Shaman is a framework that envisages integration of heterogeneous market mechanisms and platforms with decision support tools and agents for facilitating negotiations among agents, as well as human participants [23]. An architecture for a coordination and negotiation platform that incorporates agents and may incorporate humans has been proposed in Ref. [10] and further elaborated in Ref. [11]. Based on Belief–Desire–Intention philosophy the agents negotiate over plans bilaterally and simultaneously, and their actions lead to the evolving environment. An illustration is presented using the Diplomacy game. In Ref. [38] a methodology called STRATUM has been presented to facilitate practical construction of agent-enhanced negotiation systems. Its purpose, according to the authors was to bridge the gap between automated negotiation theory and practice. Use of agent to human negotiations has also been proposed for the purposes of training [27].

In Ref. [29] a simulation environment for testing various negotiation strategies called Genius involving software agent as well as human users has been described. The environment allows for con<sup>fi</sup>guring general, non-domain-speci<sup>fi</sup>c agents. Designs for negotiating agents that would incorporate opponent modeling were proposed in Refs. [30,36]. In these approaches the agents negotiated with different opponents and kept the database of past interactions. Using a learning algorithm the agents estimated the probability of the offer acceptance in their decision-making process. Along similar lines, predicting opponent moves in response to considered offers using neural networks has been proposed in Ref. [3] and further extended to more general cases in Ref. [3].

Faratin et al. [13] proposed an alternative to modeling an opponent: employing similarity-based criteria. Instead of explicitly modeling an opponent they advanced an approach whereby for a chosen concession step, among multiple competing offers the one that is most similar distance-wise to the opponent's previous offer is chosen. The approach was demonstrated using simulations.

A number of experimental studies involving human and agents in commerce settings focusing on objective as well as subjective aspects of negotiations have been reported. An early experimental study matching humans with agent counter-parts involved AutONA agents [2]. The agents negotiated on price and volume while following the so-called alpha-beta tactics, based the last bid and ask, as well as the most recent change to the ask. While the agents did not signi<sup>fi</sup>cantly outperform humans, the authors concluded that the AutONA model passed the limited Turing test, in a sense that it did not allow for manipulation by the human counterparts.

In Ref. [19] the authors have described an agent representing a salesperson that employed persuasion and negotiation techniques while interacting with a customer. Persuasion was based on the customer–agent dialogue with the involvement of pre-de<sup>fi</sup>ned arguments organized into a tree. First, the agent would try to convince a customer to accept an offer. If this did not work, the agent would go into bargaining mode and determine what concession should be made. Price was the single issue in the negotiations. Using the case of a used car sale, the authors conducted both lab and online experiments. Their <sup>fi</sup>ndings suggested that persuasion increased buyers' product valuation and willingness to pay. Negotiation increased the seller's surplus.

Some studies have focused on the effects of incorporating emotional and cultural aspects in agents. In Ref. [8] a study was conducted examining the effects of agents' expression of emotions on the negotiator's concession behavior. In this study human subjects were paired up with agents that expressed anger, neutrality, or happiness during negotiations using both with verbal and non-verbal expression mode. The subjects were aware that they were negotiating with machines. As expected “angry” agents were able to gain more concessions from the human opponents, than the “happy” ones.

An approach to designing agents that could adapt to negotiators from different cultures has been proposed in Ref. [17]. The agents were trained using past datasets containing past instances of interactions of people from different cultures. The “colored trails” game was used for experiments, and the agents were able to outperform human players. The “colored trails” game was also used in studying human– agent collaboration, where humans and agents formed groups to perform tasks and had to negotiate over the distribution of rewards [50]. The results showed that humans offered less rewards to agents than they did to other humans. In Ref. [52] effects of framing in human–agent negotiations were studied. The results did not support the expectations that framing had a signi<sup>fi</sup>cant impact on negotiation satisfaction.

The current work investigates the impact of different tactics employed by software agents on agent-to-human in multi-issue negotiations. It also compares the performance of agent–human dyads with human– human dyads. Various types of agents following different strategies have been con<sup>fi</sup>gured for the comparison of their performance.

Subjective measures have also been employed to assess the perceptions on the human side.

## 3. Research model and hypotheses

The purpose of this paper is to assess the effectiveness of different software agents by comparing their performances against human counterparts. A theoretical framework for such systematic investigation should emanate from the studies of marketplaces, as well as systems implementing these marketplaces. An appropriate starting point for such development is Vernon Smith's framework developed for experimental economics [43]. In this model microeconomic environment relates to the participating agents (not particularly “software” agents) and kinds of goods/services to be traded. The institution de<sup>fi</sup>nes rules according to which trades take place. Taken together the environment and the institution constitute the microeconomic system. The resulting agent behavior leads to certain type of system performance that is measured by important economic criteria.

While Smith's model is applicable to a wide range of exchange types, another framework, called TIMES has been proposed to target speci<sup>fi</sup>- cally electronic exchanges [22]. Since these exchanges are implemented by software systems, the framework incorporates subjective assessment aspects in addition to the economic measures. The framework draws upon information systems literature, in particular the tasktechnology <sup>fi</sup>t [15], technology acceptance [7], and end user computing satisfaction [9] models. TIMES is an acronym referring to <sup>fi</sup>ve essential independent constructs including task, individual, mechanism, environment, and system. The “task” refers to the complexity of the exchange task, e.g. number of issues involved. “Individual” relates to the features of the traders that are relevant for a given context, e.g. level of competitiveness. “Mechanism” re<sup>fl</sup>ects the type of exchange used, e.g. Dutch auction. “Environment” captures such contextual characteristics as type of market and type of product. Finally, “System” relates to speci<sup>fi</sup>c features of the software system in which the marketplace is embedded, e.g. preference modeling tools. These components through their interplay are expected to impact economic outcomes, as well as subjective perceptions. The latter are important, since they are critical for system acceptance by the users.

While TIMES is general enough to be applicable to various forms of electronic markets, it does not explicitly incorporate software agents, or provides any guidance on their treatment. Using TIMES to study agent negotiations depends, primarily, on the focus of study. For example, if human principal/agent interactions constitute such focus, then agent type/capabilities could be considered as part of system features. In our case, though, agents are participants in the market and their performance is of the primary interest. Thus, they <sup>fi</sup>t under the “individuals” category of independent variables. Other independent components of TIMES will not be manipulated in the study, and will be kept constant. They will be detailed further in experimental setup and system description parts.

The dependent part of TIMES includes both objective, as well as subjective variables. Since the work focuses on agents' performance, the most important variables include utility of outcomes, and proportion of agreements. TIMES is a framework, rather than a theoretical model, and thus serves as a reference source that allows for certain degree of freedom in generating research expectations. Subjective variables in TIMES include ease of use, usefulness, and goal achievement and satisfaction. The latter is affected by the achieved outcomes. In our study instead of this component we introduce two related ones: satisfaction with the outcome, and satisfaction with the process. Such a re<sup>fi</sup>nement allows us to test hypotheses related to the outcome, as well as the experience with the opponent. We consider direct effects of agent negotiation styles on these two variables.

In designing agent negotiation behaviors we de<sup>fi</sup>ne the following timedependent tactics: “individualistic,” “neutral,” “yielding” (“conceder”), and “individualistic-then-yielding.” Additionally, an absolute tit-for-tat is included from the behavior-based family of tactics. Absolute tit-for-tat simply mirrors the concessions made by the opponent on all the issues. A control group includes human negotiators which would follow whatever tactics they choose to. Individualistic tactic represents a more competitive behavior whereby an agent delays making large concessions until closer to the negotiation deadline. Yielding tactic dictates making large concessions early and represents the case where an agent is anxious to get an agreement. In a neutral tactic the rate of concessionmaking is constant throughout the negotiation period. Individualisticthen-yielding represents the combined strategy whereby an agent follows a hard tactic <sup>fi</sup>rst, but midway through the negotiations switches to the yielding tactic. The rationale behind this tactic is to take advantage of the high utility agreements made by anxious counter-parts, while also attempting to make deals with more stubborn opponents who are willing to negotiate for longer periods. The concessions here are de<sup>fi</sup>ned in regards with the total utility of the offers. The total utility is de<sup>fi</sup>ned as a weighted average of the utilities of individual issue values (see, e.g. [12]).

Additionally we also included one behavior-dependent tactic, absolute tit-for-tat. In this tactic, no utility is calculated; the agent simply reciprocates the counter-parts moves on all the issues. In other words the agent makes the same concession on a given issue as the last concession by the counterpart.

Our <sup>fi</sup>rst set of hypotheses concerns the utility of agreements achieved by the agents. We argue that agents following hard strategies will have higher utilities of agreements. One of the propositions for the design of agents advanced in Ref. [53] claims that making tough initial offer would lead to better outcomes. Alternatively, it has been argued in the past by researchers that large initial concessions would lead to the opponent's expectation of further large concessions and smaller concessions on the part of the opponent [25]. Therefore, we propose the following hypotheses:

H1a. Agents following “individualistic” tactic will achieve agreements with higher utility than those following “yielding” tactic.

H1b. Agents following “individualistic” tactic will achieve agreements with higher utility than those following “neutral” tactic.

H1c. Agents following “neutral” tactic will achieve agreements with higher utility than those following “yielding” tactic.

Use of “individualistic-then-yielding” tactic initially follows the tough schedule, but then switches to the more conceding pattern. So it attempts to <sup>fi</sup>rst grab the better offers, and only later becomes more yielding. Thus, we hypothesize that:

H1d. Agents following “individualistic-then-yielding” tactic will achieve agreements with higher utility than those following “yielding” tactic.

H1e. Agents following “individualistic-then-yielding” tactic will achieve agreements with higher utility than those following “neutral” tactic.

Since we have listed a number of bene<sup>fi</sup>ts of software agents compared to human negotiators, we would expect that agents, overall will outperform human negotiators playing the same role (e.g. sellers). However, because some tactics are con<sup>fi</sup>gured to make large concessions initially, one would not expect that all types of agents will achieve better agreements than humans. Thus, we hypothesize that:

H1f. Most of the agent types employing different tactics will achieve significantly better agreement utilities than human negotiators.

Thus, if, for example three out of <sup>fi</sup>ve tactics outperform human negotiators, the hypothesis will be supported. Additionally, we expect that all of the agents following different tactics will perform not worse than humans on the same side of negotiations:

H1g. None of the tactics employed by agents will do significantly worse than human negotiators.

The next set of hypotheses concerns the proportion of agreements made by negotiators. Naturally, one would expect that more conceding tactics would generate higher agreement rates:

H2a. Agents following “yielding” tactic will achieve higher proportion of agreements than those following “individualistic” tactic.

H2b. Agents following “yielding” tactic will achieve higher proportion of agreements than those following “neutral” tactic.

H2c. Agents following “neutral” tactic will achieve higher proportion of agreements than those following “individualistic” tactic.

Since, compared to individualistic tactic the individualistic-thenyielding does dictate making considerable concessions midway through the allocated negotiation period, one would expect that it would lead to more agreements than the individualistic tactic:

H2d. Agents following “individualistic-then-yielding” tactic will achieve higher proportion of agreements than those following “individualistic” tactic.

Tit-for-tat tactic as de<sup>fi</sup>ned in this work is least predictable from the outcome perspective. This is because, it simply mirrors the opponent's moves. In essence a human opponent would be playing against itself. This also implies, that the interests of the agent and its opponent would be directly opposing. For example, if a human is willing to make a concession on one issue, but reluctant to do so on the other issue, so will be the tit-for-tat agent. In essence this would lead to distributive negotiations. Since other types of strategies may explore integrative possibilities, we expect that tit-for-tat agents will make fewer agreements compared to other types of agents, as well as humans:

H2e. “Tit-for-tat” agents will have significantly lower agreement proportion than most of the agent categories employing time-dependent tactics.

The following two hypotheses are similar to H1f and H1g regarding the comparison between agent and human negotiators. Here we expect that, overall agents will achieve more agreements, since the agents are not affected by psychological factors, and they will continue negotiating without quitting prematurely.

Table 1  
Preferences of sellers and buyers (excluding price).

<table><tr><td>Issue Levels</td><td>Buyer&#x27;s utility</td><td>Seller&#x27;s utility</td></tr><tr><td colspan="3">Monitor type</td></tr><tr><td>17 inch</td><td>0</td><td>100</td></tr><tr><td>19 inch</td><td>20</td><td>70</td></tr><tr><td>22 inch</td><td>80</td><td>45</td></tr><tr><td>24 inch</td><td>100</td><td>0</td></tr><tr><td>Weight</td><td>15</td><td>10</td></tr><tr><td colspan="3">Hard drive</td></tr><tr><td>160 GB</td><td>0</td><td>100</td></tr><tr><td>320 GB</td><td>80</td><td>60</td></tr><tr><td>500 GB</td><td>90</td><td>30</td></tr><tr><td>750 GB</td><td>100</td><td>0</td></tr><tr><td>Weight</td><td>7</td><td>5</td></tr><tr><td colspan="3">Service plan</td></tr><tr><td>1-year</td><td>50</td><td>100</td></tr><tr><td>2-year</td><td>80</td><td>50</td></tr><tr><td>3-year</td><td>90</td><td>33</td></tr><tr><td>4-year</td><td>100</td><td>0</td></tr><tr><td>Weight</td><td>10</td><td>20</td></tr><tr><td colspan="3">Loaded Software</td></tr><tr><td>MS Office Starter</td><td>0</td><td>100</td></tr><tr><td>MS Office Home</td><td>85</td><td>50</td></tr><tr><td>MS Office Professional</td><td>100</td><td>0</td></tr><tr><td>Weights</td><td>13</td><td>15</td></tr></table>

Individualistic tactic.  
![](/api/attachments/R7Y462J4/fulltext/images/398b68bb2a5a542093c075f88c370a1e6e022567dbbaff1782b45d7f74510f34.jpg)  
Fig. 1. Individualistic tactic

H2f. Most of the agent types employing different tactics will achieve a significantly better agreement rate than human negotiators.

H2g. None of the tactics employed by agents will achieve a significantly lower agreements rate than human negotiators.

Thus, if three out of four other tactics achieve signi<sup>fi</sup>cantly higher rate of agreements, the hypothesis will be supported. The hypothesis expresses a general expectation that absolute tit-for-tat, leading to distributive negotiations would tend to generate, overall, fewer agreements than time-dependent tactics.

In addition to considering rate of concession-making in timedependent strategies we have also taken into account how the offers are generated. When a decision is made about the concession amount, which means the chunk of overall utility an agent is willing to give up, there is still a need to choose a concrete offer to be generated. In this regard, the dual concern model [37] mentioned above may serve as a useful reference structure. In this two-dimensional model one dimension re<sup>fl</sup>ects the concern for self, while the other relates to the concern for the opponent. Five con<sup>fl</sup>ict management styles are de<sup>fi</sup>ned based on one's positioning along the dimensions.

Neutral tactic  
![](/api/attachments/R7Y462J4/fulltext/images/a2fe493cd17034fd6cab7f067a087d778a1f6497d11d467a2510bcf893e134ae.jpg)  
Fig. 2. Neutral tactic.

![](/api/attachments/R7Y462J4/fulltext/images/5f7eafe6bcd0e1ca02bb8776241a9e4e1ec7f50e292acf6a61cd38558359ace9.jpg)  
Fig. 3. Yielding tactic.

The concession-making time-dependent strategies above relate to the “concern for self” or “assertiveness” dimension. Offer-generation procedures for a given utility level can be related to the “concern for the other” dimension. In [13] an offer-generation method has been proposed that generates an offer most similar to the opponent's previous offer from all possible candidates at a given utility level. The authors believed that this method would lead to a higher agreement rate. We can employ a similar approach for time-dependent tactic agents by taking opponent's last offer as an initial point in the search for the next offer, and then trying to modify it so that it corresponds to the required utility level. We call it “reactive” offer generation, as it tries to accommodate the opponent's moves. As a contrast we could also employ a “passive' approach whereby an agent generates a new offer based on its own past offer, without considering the opponent's moves. This passivevs.-reactive dimension loosely corresponds to the “concern for the other” dimension. One would expect that the agents adopting higher concern for the opponent would be able to make more agreements than those who do not. Thus, we have the following hypotheses:

Individualistic-then-yielding tactic  
![](/api/attachments/R7Y462J4/fulltext/images/9274656ca2c0ea258f159cfce385c16fa0ca0a155ecdf45dfb0fae02bab10003.jpg)  
Fig. 4. Individualistic-then-yielding tactic.

Table 2  
Anchor points for de<sup>fi</sup>ning curves.

<table><tr><td>Tactic</td><td> $P_0$ </td><td> $P_1$ </td><td> $P_2$ </td><td> $P_3$ </td></tr><tr><td>Individualistic</td><td>(0, 100)</td><td>(100, 98)</td><td>(100, 10)</td><td>N/A</td></tr><tr><td>Neutral</td><td>(0,100)</td><td>(53, 53)</td><td>(100, 10)</td><td>N/A</td></tr><tr><td>Yielding</td><td>(0, 100)</td><td>(20, 17)</td><td>(100, 10)</td><td>N/A</td></tr><tr><td>Individualistic-then-yielding</td><td>(0, 100)</td><td>(51, 99)</td><td>(47, 0)</td><td>(100,10)</td></tr></table>

H3a. Agents following “individualistic” tactic with “reactive” offer generation will achieve higher proportion of agreements than those following “passive” approach.

H3b. Agents following “neutral” tactic with “reactive” offer generation will achieve higher proportion of agreements than those following “passive” approach.

H3c. Agents following “yielding” tactic with “reactive” offer generation will achieve higher proportion of agreements than those following “passive” approach.

H3d. Agents following “individualistic-then-yielding” tactic with “reactive” offer generation will achieve higher proportion of agreements than those following “passive” approach.

The last set of hypotheses relates to the subjective variables relevant for the system adoption as described by the TIMES framework. Our grand expectation is that agents will not score worse on these variables than humans when rated by their opponents. The rationale is as follows. Since human-to-human negotiations through electronic facilities are becoming common (for example, a company representative can use chat on their website to negotiate with a customer) and accepted, then, if agents are perceived to be not worse than human counterparts, then agent-handled negotiations will not have a lower acceptance rate than human-handled ones.

H4a. Agents will not have a lower score on perceived usefulness, ease of use, satisfaction with the outcome, and satisfaction with the process than human negotiators as perceived by their counterparts.

Table 3  
Negotiation outcomes (cases with agreement only).

<table><tr><td rowspan="2">Category</td><td rowspan="2">No. of cases</td><td colspan="2">Seller utility</td><td colspan="2">Buyer utility</td><td rowspan="2">Final price, $</td></tr><tr><td>Mean</td><td>St.D.</td><td>Mean</td><td>St.D.</td></tr><tr><td>Individualistic</td><td>48</td><td>63.2</td><td>17.4</td><td>44.9</td><td>20</td><td>1259.27</td></tr><tr><td>Neutral</td><td>63</td><td>43.8</td><td>15.3</td><td>69.7</td><td>17.8</td><td>1034.16</td></tr><tr><td>Yielding</td><td>76</td><td>36.5</td><td>15.3</td><td>79.0</td><td>17.6</td><td>932.79</td></tr><tr><td>IY</td><td>58</td><td>40.4</td><td>21</td><td>71.9</td><td>22.9</td><td>1009.14</td></tr><tr><td>Tit-for-tat</td><td>22</td><td>72.4</td><td>14.6</td><td>36</td><td>15.5</td><td>1278.41</td></tr><tr><td>Human-human</td><td>17</td><td>35.9</td><td>17.9</td><td>73.0</td><td>19.2</td><td>1056.49</td></tr></table>

Kwon and Weingart [25] have studied the effects of concessionmaking on the negotiation judgments by the opponent. They claimed that rapid concession-making often leads to lower valuation of the achieved agreement by the opponent: the phenomenon known as “buyer's remorse.” Subsequently, they hypothesized that delayed concessions would result in higher satisfaction with the outcome than rapid ones. They further proposed that systematic and regular concession-making would lead to higher satisfaction with the process and the opponent. The following hypotheses aim to test the above expectations:

H4b. Subjects negotiating with “yielding” agents will have a lower satisfac tion with the outcome than those negotiating with “individualistic” ones.

H4c. Subjects negotiating with “individualistic” agents will have a higher satisfaction with the process than those negotiating with “yielding” ones.

## 4. Negotiation case and system description

Our target subject group included university students taking a course in introduction to Information Technology. Therefore, the case had to be selected with care, so that it is familiar to the students, and is in line with the content of the course. The negotiation case developed for the experimental study concerned the sale of a desktop computer, which complies with the above requirements. There were <sup>fi</sup>ve issues including the price, type of monitor, hard drive size, service plan, and software loaded. Each option for each issue had a corresponding level of utility (attractiveness), these levels being different for the buyers vs. sellers.

<table><tr><td>Time-dependent agents work according to the following algorithm.</td></tr><tr><td>1. The agent makes the first offer, which is of highest utility to it.2. Agent checks the status of negotiations and counterparts offer every N hours (3 in our case). If an offer has been sent by a counterpart:a) If the negotiations were closed (either with an agreement or without) agent stops.b) If an agent receives and offer with a rating higher or equal to the agent’s desired rating at this moment agent accepts an offer;c) Otherwise it sends a counter-offer.</td></tr><tr><td>To generate an offer an agent uses the following algorithm:</td></tr><tr><td>1) Passive agents take their own last offer as starting point. Reactive agents accept the last opponent’s offer as the starting point. The agent tries to modify the starting point to bring it to the level of target utility as given by its tactic curve. On every step an agent randomly modifies an option value for one issue.2) The direction of the change: if the previous attempt generated an offer with utility below the curve the direction is “+”, otherwise it&#x27;s “-”3) The termination criteria: either 1000 total attempts or 100 attempts without improvement in the approximation of the curve, whichever happens first.</td></tr></table>

Table 5  
Table 4 Results of testing hypotheses H1a–H1g.

<table><tr><td>Hypothesis</td><td>Tactic 1</td><td>Tactic 2</td><td>Mean difference</td><td>p-Value</td><td>Outcome</td></tr><tr><td>H1a</td><td>Individualistic</td><td>Yielding</td><td>26.7</td><td>0.00</td><td>Supported</td></tr><tr><td>H1b</td><td>Individualistic</td><td>Neutral</td><td>19.4</td><td>0.00</td><td>Supported</td></tr><tr><td>H1c</td><td>Neutral</td><td>Yielding</td><td>7.2</td><td>0.10</td><td>Not supported</td></tr><tr><td>H1d</td><td>IY</td><td>Yielding</td><td>3.9</td><td>0.50</td><td>Not supported</td></tr><tr><td>H1e</td><td>IY</td><td>Neutral</td><td>-3.4</td><td></td><td>Not supported</td></tr><tr><td>H1f</td><td>Individualistic</td><td>Humans</td><td>27.3</td><td>0.00</td><td>Not supported</td></tr><tr><td></td><td>Neutral</td><td></td><td>7.9</td><td>0.50</td><td></td></tr><tr><td></td><td>Yielding</td><td></td><td>0.6</td><td>0.50</td><td></td></tr><tr><td></td><td>IY</td><td></td><td>4.5</td><td>0.50</td><td></td></tr><tr><td></td><td>Tit-for-tat</td><td></td><td>36.5</td><td>0.00</td><td></td></tr><tr><td>H1g</td><td>Humans</td><td>All agents</td><td>-</td><td>-</td><td>Supported</td></tr></table>

In order to calculate the total utility of the offer the issues were assigned different weights. These were then used in an additive utility function to estimate the level of attractiveness of an offer. Agents used this information in order to decide on the acceptability of the received offers and generate offers.

All agents acted on the seller side, and they were not aware of the buyers' preference structures. The weights were slightly different for sellers than buyers to facilitate tradeoffs, which have been considered one of the key integrative negotiation characteristics [40]. Although the system allows users to specify their own preference structures, these were <sup>fi</sup>xed to be the same for all human users in order to control variation in the experiments. In particular, the difference between buyer and seller references was set in order to allow for integrative negotiations.

Since price is the only continuous issue, its best and worst values de-<sup>fi</sup>ne the range instead of individual options. The seller's range included \$700 (worst) to \$1550 (best), while the buyers' range was set from \$800 (best) to \$1450 (worst). The seller's weight for the price was set at 50%, while the buyer's at 55%. Table 1 shows the utility levels for options for other four (discrete) issues (on a 100% scale), as well as the issue weights for buyers and sellers.

As mentioned earlier, we have chosen to use <sup>fi</sup>ve different concession schedules, three of which were similar to those used in Kasbah experiments. These included: individualistic, neutral, yielding, individualisticthen-yielding, and tit-for-tat tactics. The individualistic agents tend to make smaller concessions in terms of utility of generated offers in the beginning of the negotiation period. However, as they approach the end of the period, they would start making larger concessions in search of an agreement (Fig. 1).

Neutral tactic dictates that an agent concedes the constant amount of utility regardless of the time period, i.e. the concession schedule is linear (Fig. 2). Yielding tactic implies making large concessions in the very beginning of the negotiation period in search of a quick agreement. This represents the case where an agent is anxious to sell the product. However, as the agent quickly drops the utility close to the reservation levels, it cannot make large concessions later in the process (Fig. 3). Individualistic-then-yielding tactic models more complex behavior of the agents. In the beginning of the process an agent behaves competitively, however, in the middle of the negotiation period it changes its pro<sup>fi</sup>le to a collaborative one. Thus, there is an in<sup>fl</sup>exion point in an agent's schedule (Fig. 4).

Proportions of agreements.

<table><tr><td>Category</td><td>Agreements</td><td>No agreements</td><td>Proportion of agreements, %</td></tr><tr><td>Individualistic</td><td>48</td><td>43</td><td>52.7</td></tr><tr><td>Neutral</td><td>63</td><td>27</td><td>70.0</td></tr><tr><td>Yielding</td><td>76</td><td>17</td><td>81.7</td></tr><tr><td>IY</td><td>58</td><td>19</td><td>75.3</td></tr><tr><td>Tit-for-tat</td><td>22</td><td>29</td><td>43.1</td></tr><tr><td>Human-human</td><td>17</td><td>17</td><td>50.0</td></tr></table>

The <sup>fi</sup>nal strategy used was tit-for-tat. These agents do not rely on utility calculations. Rather, they watch the opponent moves and simply mirror them in composing counter-offers. In other words, when an opponent makes a new offer an agent determines the difference between this offer and the previous one made by the opponent, and applies the same difference to its own offer. If, say an opponent made a large change to a price, the agent would do the same.

Concession-making curves for time-dependent agents are de<sup>fi</sup>ned using Bezier curves. The following equations de<sup>fi</sup>ne these curves for the quadratic and cubic models:

$$
\mathbf {B} (t) = (1 - t) ^ {2} \mathbf {P} _ {0} + 2 (1 - t) t \mathbf {P} _ {1} + t ^ {2} \mathbf {P} _ {2}, t \in [ 0, 1 ].
$$

$$
\mathbf {B} (t) = (1 - t) ^ {3} \mathbf {P} _ {0} + 3 (1 - t) ^ {2} t \mathbf {P} _ {1} + 3 (1 - t) t ^ {2} \mathbf {P} _ {2} + t ^ {3} \mathbf {P} _ {3}, t \in [ 0, 1 ].
$$

Here the set of P points de<sup>fi</sup>nes the anchors for setting up the curves (they correspond to the dots in Figs. 1–4) These are sets for different agent types as shown in Table 2. The algorithm for time-dependent agents is shown in Fig. 5.

## 5. Variables and experimental setup

Current work investigates the objective outcomes of agent–human negotiations, as well as subjective variables capturing human perceptions of the process, outcomes and system. The objective variables included the utility of the agreements, and the proportion of agreements achieved. These relate to the economic bene<sup>fi</sup>ts of agent–human negotiations. The subjective variables included satisfaction with the outcomes, satisfaction with the process, ease of use, and perceived usefulness of the system. These are important indicators from the information systems literature, especially relating to the acceptance and use of the system by human users.

## Table 6

Results of testing hypotheses H2a–H2g.

<table><tr><td>Hypothesis</td><td>Tactic 1</td><td>Tactic 2</td><td>p-Value</td><td>Outcome</td></tr><tr><td>H2a</td><td>Yielding</td><td>Individualistic</td><td>0.000</td><td>Supported</td></tr><tr><td>H2b</td><td>Yielding</td><td>Neutral</td><td>0.046</td><td>Supported</td></tr><tr><td>H2c</td><td>Neutral</td><td>Individualistic</td><td>0.013</td><td>Supported</td></tr><tr><td>H2d</td><td>IY</td><td>Individualistic</td><td>0.002</td><td>Supported</td></tr><tr><td rowspan="4">H2e</td><td>Individualistic</td><td>Tit-for-tat</td><td>0.178</td><td>Supported</td></tr><tr><td>Neutral</td><td></td><td>0.002</td><td></td></tr><tr><td>Yielding</td><td></td><td>0.000</td><td></td></tr><tr><td>IY</td><td></td><td>0.000</td><td></td></tr><tr><td rowspan="5">H2f</td><td>Individualistic</td><td>Humans</td><td>0.471</td><td>Supported</td></tr><tr><td>Neutral</td><td></td><td>0.032</td><td></td></tr><tr><td>Yielding</td><td></td><td>0.001</td><td></td></tr><tr><td>IY</td><td></td><td>0.009</td><td></td></tr><tr><td>Tit-for-tat</td><td></td><td>-</td><td></td></tr><tr><td>H2g</td><td>Humans</td><td>Tit-for-tat</td><td>0.344</td><td>Supported</td></tr></table>

Table 7  
Results of testing hypotheses H3a–H3d.

<table><tr><td rowspan="2">Hypothesis</td><td rowspan="2">Tactic</td><td colspan="2">Proportion of agreements, %</td><td rowspan="2">p-Value</td><td rowspan="2">Outcome</td></tr><tr><td>Reactive</td><td>Passive</td></tr><tr><td>H3a</td><td>Individualistic</td><td>64</td><td>32</td><td>0.015</td><td>Supported</td></tr><tr><td>H3b</td><td>Neutral</td><td>68</td><td>72</td><td>-</td><td>Not supported</td></tr><tr><td>H3c</td><td>Yielding</td><td>83</td><td>80</td><td>0.441</td><td>Not supported</td></tr><tr><td>H3d</td><td>IY</td><td>83</td><td>69</td><td>0.128</td><td>Not supported</td></tr></table>

The subjects in the study were university students enrolled in the introductory course on information technology. Thus, the negotiation case was well in line with the learning objectives of the course. The treatments included pairing up the subjects with various types of agents described in an earlier section. We also paired up human sellers with human buyers in a control group. The experiment was conducted via the web, whereby subjects could perform their tasks from any location in an asynchronous mode during a <sup>fi</sup>ve-day period. The subjects were invited to join the negotiations via email containing the link to the system.

Human subjects were free to terminate the negotiation at any time without reaching an agreement with their counter-parts. After either reaching an agreement, or terminating the negotiations the human subjects were asked to complete a questionnaire measuring their perceptions of the outcome, process, and the system. Questions related to the satisfaction with the process and satisfaction with the outcome have been adopted from Ref. [44]. One <sup>fi</sup>nal question read: “I was negotiating with: 1) a human; 2) a computer: 3) not sure.”

## 6. Results and discussion

A total of 501 subjects have participated in the experiment and have completed the experimental task. For the analysis of the results we have selected only those negotiation instances, which featured at least four offers in total, which resulted in 436 usable observations. The rationale for this decision was to include only those cases where the subjects took the task seriously. Of these, 284 negotiations (65%) ended up in an agreement, while in 152 (35%) cases the agreement was not reached.

Table 3 shows the outcomes achieved by the different types of negotiators. These outcomes have been calculated only for those cases where an agreement has been achieved (for other cases the only outcome is “no agreement”). As one can see from the table, in terms of the seller utilities the agents have outperformed the human subjects, although, as we shall see this result was not always statistically signi<sup>fi</sup>cant.

Tit-for-tat agents have shown the highest utility values for the agreements, followed by the individualistic (competitive) agents. Yielding (conceding) agents have reached lowest-utility agreements.

Table 4 shows the results of group 1 hypotheses testing (those related to the utility of agreements). As expected, the individualistic tactic-following agents have signi<sup>fi</sup>cantly outperformed those following neutral or yielding tactics, thus supporting hypotheses H1a–H1b. The hypotheses comparing the performance of neutral and individualistic/ yielding (IY) tactics with the yielding one (H1c–H1d) were not supported, although the difference was in the right direction. Furthermore, IY tactic did not outperform the neutral one. Thus H1e was not supported either. In the case of neutral vs. yielding the signi<sup>fi</sup>cance of the difference in utilities was 0.1, which could be due to the speci<sup>fi</sup>c parameters of the curve. In case of the IY tactic, there are two possible explanations. First, as we mentioned, we have excluded negotiation cases which had less than four offers exchanged. This might have eliminated many cases where the opponents have made agreements in the very early stages of negotiations. Second, many subjects may have started actively participating in the negotiations at later stages, by which time the IY tactic has moved from the individualistic phase to the yielding one. It would be interesting to see what the results would be if the transition from one tactic to another takes place later in the allocated time period.

The hypothesis H1f that stated that most agent types will outperform their human “colleagues” was not supported, as only individualistic and tit-for-tat agents have reached signi<sup>fi</sup>cantly better agreements than humans, despite the fact that other types of agents have also outperformed humans, albeit, marginally. However, from the same results we can conclude that the hypothesis H1g was supported, i.e. none of the agent types performed signi<sup>fi</sup>cantly worse than humans.

Next we examine the second group of hypothesis. Table 5 shows the proportions of agreements for different compositions of dyads. The largest proportion of agreements was reached in the yielding agent category. This is an intuitive result, since yielding agents make large concessions early in the negotiations process, and thus they have a higher chance of making a deal with the human counterparts. It is interesting to see that human-to-human dyads have a second-lowest record in terms of proportion of agreements made. Thus, the majority of agentinvolved dyads have reached more agreements than purely human dyads. Individualistic agents were able to reach an agreement in 53% of cases. IY agents have made agreements in 75% of cases, higher than neutral category. The lowest number of agreements was achieved in tit-for-tat category.

![](/api/attachments/R7Y462J4/fulltext/images/7f664089233defbb10ff5c975ea4083c830b08bde1807c4a653153f3f24f7f5a.jpg)  
Fig. 6. “I was negotiating with…” agent–human dyads vs. human–human dyads.

Table 8 Factor analysis results.

<table><tr><td rowspan="2">Items</td><td colspan="4">Factors</td></tr><tr><td>PU</td><td>EU</td><td>SO</td><td>SP</td></tr><tr><td>PU1</td><td>.671</td><td>.192</td><td>.211</td><td>.137</td></tr><tr><td>PU2</td><td>.813</td><td>.128</td><td>.206</td><td>.134</td></tr><tr><td>PU3</td><td>.830</td><td>.165</td><td>.248</td><td>.179</td></tr><tr><td>EU1</td><td>-.032</td><td>-.626</td><td>-.062</td><td>-.084</td></tr><tr><td>EU2</td><td>.202</td><td>.841</td><td>.068</td><td>.088</td></tr><tr><td>EU3</td><td>.192</td><td>.807</td><td>.048</td><td>-.024</td></tr><tr><td>SO1</td><td>.181</td><td>.078</td><td>.590</td><td>.275</td></tr><tr><td>SO2</td><td>.201</td><td>.076</td><td>.819</td><td>.116</td></tr><tr><td>SO3</td><td>.249</td><td>.058</td><td>.778</td><td>.207</td></tr><tr><td>SP2</td><td>.140</td><td>.080</td><td>.184</td><td>.687</td></tr><tr><td>SP4</td><td>.231</td><td>.053</td><td>.392</td><td>.586</td></tr></table>

The bold font indicates items loading on the corresponding factors. Generally, one expects the values in bold to be higher than others.

Table 6 shows the results of H2 hypotheses testing using chi-square tests. As one can see all of the hypotheses have been supported. Namely, as expected, the yielding tactic has reached signi<sup>fi</sup>cantly higher rates of agreement than both individualistic and neutral strategies (H2a–H2b). Neutral and IY agents have had higher proportion of agreements than individualistic ones (H2c–H2d). Furthermore, as expected, the tit-fortat tactic was inferior to all other tactics in terms of agreement rate (H2e). This, as mentioned earlier. is due to the fact that tit-for-tat tends to lead to the distributive, rather than integrative negotiations. Yielding, neutral, and IY agents have reached signi<sup>fi</sup>cantly higher rate of agreements than humans, thus providing support for the hypothesis H2f. The only tactic that was inferior to humans in this respect was tit-for-tat. The difference, however was not signi<sup>fi</sup>cant, which leads to the support of H2g.

The third group of hypotheses posited that reactive agents, i.e. those that considered the opponent's offer while generating a counter-offer, would make more agreements than the passive ones. As one can see from Table 7, this turned out to be the case only for the individualistic tactic (H3a). A possible explanation is that other agents made their concessions rapidly, and thus quickly made offers that were attractive to the opponents anyway.

In order to compare the subjects' perceptions a questionnaire was used with three items per construct measuring perceived usefulness, perceived ease of use and satisfaction with the outcome, and four items measuring satisfaction with the process. Initial results of the factor analysis did not reveal a convincing pattern, and two items (satisfaction with the process) were dropped from the analysis. Subsequently, factor analysis resulted in an acceptable pattern of loadings (Table 8). We have then used factor scores to compare across different categories. Results are shown in Table 9.

The results of MANOVA revealed that there were some differences in the factor scores (Wilk's lambda corresponded to signi<sup>fi</sup>cance 0.00). These differences were subsequently attributed to the satisfaction with the process and outcome variables. Most notably (and understandably) satisfaction with the outcome was signi<sup>fi</sup>cantly lower for the titfor-tat and individualistic tactics when compared to other agent tactics (which provides support for H4b). Satisfaction with the process was signi<sup>fi</sup>cantly lower for tit-for-tat tactic when compared to the yielding tactic. None of the agent tactics has resulted in signi<sup>fi</sup>cantly lower levels of perceived usefulness, ease of use, satisfaction with the outcome and the process when compared to human negotiations, thus supporting hypothesis H4a. However, the hypothesis H4c was not supported. Apparently, negotiating easier deals was perceived by the subjects as more enjoyable process than negotiating the tough ones. The overall conclusion is, since agents were not perceived as being worse than humans on subjective variables, introduction of agent-managed negotiations customers is not likely to negatively affect customer perceptions as compared with traditional human-to-human negotiations.

Fig. 6 shows the results of the question related to whether the participants guessed correctly if they were negotiating with humans or computers. The left side shows the results from human–agent dyads, and the right side shows human–human ones. The leftmost bar in each group indicates the number of responses that read “human,” the middle one relates to “computer” responses, and the last one shows “not sure” responses.

As Fig. 6 shows, the majority of subjects in the agent–human dyads were not sure if they were interacting with the humans or agents (183 responses). This was followed by the group of subjects who had thought they were negotiating with other humans (114). The smallest group consisted of those who guessed correctly that they were interacting with agents (65). It is interesting to note that some subjects in the human-to-human dyads thought they were interacting with a computer (2 out of 30) (Fig. 6).

The distribution of answers depended on the type of the agent tactic employed (Table 10). For example, in IY category much larger proportion of subjects thought they were negotiating with a human counter-part as compared to those who had an impression they were dealing with a machine (25 vs. 8). This can be explained by the fact that IY concession schedule results in more complex behavior, less obvious behavior that could be more readily ascribed to humans, rather than machines. Similar, though less prominent results were obtained in individualistic agent category (33 vs. 15). On the other hand, the yielding category was the only one where the number of “human” vs. “machine” responses was equal (21 each). Perhaps, the subjects expected their human counterparts to be more competitive, rather than conceding. The small number of entries for the human category (“Agent” column) does not allow us to conduct statistical comparisons (Tables 9 and 10).

Table 9 Comparison of factor scores.

<table><tr><td rowspan="2"></td><td colspan="4">Factor</td></tr><tr><td>Perceived usefulness</td><td>Perceived ease of use</td><td>Satisfaction with the outcome</td><td>Satisfaction with the process</td></tr><tr><td>Individualistic</td><td>-.051</td><td>.026</td><td>-.284</td><td>-.007</td></tr><tr><td>Neutral</td><td>-0.16</td><td>-.006</td><td>.188</td><td>.013</td></tr><tr><td>Yielding</td><td>-0.08</td><td>-.079</td><td>.354</td><td>.151</td></tr><tr><td>IY</td><td>.293</td><td>-.027</td><td>.152</td><td>.062</td></tr><tr><td>Tit-for-tat</td><td>-.131</td><td>.127</td><td>-.568</td><td>-.300</td></tr><tr><td>Human</td><td>-0.001</td><td>.032</td><td>-.105</td><td>-.185</td></tr></table>

Table 10  
The number of human vs. agent counter-part answers.

<table><tr><td rowspan="2">Negotiator: human vs. agent</td><td colspan="3">“I was negotiating with...”</td></tr><tr><td>Human</td><td>Agent</td><td>Not sure</td></tr><tr><td>Individualistic</td><td>33</td><td>15</td><td>37</td></tr><tr><td>Neutral</td><td>21</td><td>14</td><td>46</td></tr><tr><td>Yielding</td><td>21</td><td>21</td><td>41</td></tr><tr><td>Amen./Obst.</td><td>25</td><td>8</td><td>35</td></tr><tr><td>Tit-for-tat</td><td>14</td><td>7</td><td>24</td></tr><tr><td>Human</td><td>20</td><td>2</td><td>8</td></tr></table>

## 7. Conclusions

The purpose of this work was to experimentally investigate the feasibility and bene<sup>fi</sup>ts of using autonomous agents in negotiations with humans. To this end an electronic marketplace that can support both human-to-human and agent-to-human negotiations was built. The system allows con<sup>fi</sup>guring negotiation agents by providing preference structures, reservation levels and tactics to be employed. Five different agent tactics have been used: individualistic, neutral, yielding, individualistic-then-yielding (time-dependent tactics), and absolute tit-for-tat (a behavior-dependent tactic). These tactics were used by the agents acting as sellers while negotiating with human counterparts, who acted as buyers. Additionally, a small group of human “sellers” was paired up with human “buyers” for comparison of agent performance. Overall, the expectations were, as expressed in the hypotheses, that most agent types will outperform human negotiators in terms of utility and proportion of agreements. We also expected that more conceding tactics would lead to higher proportion of agreements, but lower utilities.

The results indicate that while most agent types did better than humans on utility scale, this <sup>fi</sup>nding was statistically signi<sup>fi</sup>cant only for two types of agents: individualistic and tit-for-tat. At the same time, none of the agents did signi<sup>fi</sup>cantly worse than human negotiators. In terms of agreement rates most agent types have outperformed human–human dyads, and none of them showed worse performance than humans. More competitive tactics led to higher agreement utilities, albeit lower agreement rates. However, the agreement ratio was significantly higher for the competitive agents who made “reactive” offers, than for the competitive agents who made “passive” offers. This indicates, that competitors may increase the probability of reaching an agreement by choosing offers that are similar to their counterparts offers.

The lowest proportion of agreements was generated by tit-for-tat agent. Furthermore, for the individualistic tactic considering the opponent's offers in counter-offer generation has led to higher proportion of agreements compared to ignoring them. The analysis of subjective variables frequently used in IS literature shows that humans who negotiated with agents did not perceive their cases differently from those involved in human-to-human dyads in terms of usefulness, ease of use, and satisfaction with the process or with the outcome.

The above results are encouraging and have practical implications. The <sup>fi</sup>ndings suggest that use of agents in e-negotiations may lead to an improved performance as compared with humans, and to better agreement rates. Depending on a given business context and situation agent tactics could be adjusted to shift either towards higher pro<sup>fi</sup>t (utility) end, or towards higher likelihood of deals. Taking into account that human–human negotiations through electronic media do take place (e.g. as part of a chat between a customer and a customer care representative), it is encouraging to <sup>fi</sup>nd that agent-led negotiations are not perceived as being worse on important subjective system acceptancerelated variables.

When employed by human decision-makers agent con<sup>fi</sup>guration interface can act as a decision support tool for choosing appropriate preference structure, aspiration and reservation levels, as well as agent tactics. In spirit, such an action-oriented decision support is close to so-called “situated DSS” model [47], where decision implementation is integrated as part of the system. A particularly interesting setup would be providing DSS interface for managing multiple negotiating agents [45].

One possible limitation of the current work is use of undergraduate students as subjects. However, we feel that the experimental task we have selected was <sup>fi</sup>tting their level of knowledge and experience, as well as the course they were taking at the time. Another limitation is that the subjects were not rewarded based on their performance. However, assignment of such rewards based on utilities would be dif<sup>fi</sup>cult to explain, especially for those cases where no agreement was reached.

One natural direction of future research would be to select a different negotiation case (e.g. in supply chain context), different type of subjects (e.g. graduate students) and see if <sup>fi</sup>ndings would be the same. Another attractive opportunity is to develop strategies, using which an agent could <sup>fl</sup>exibly adapt its current tactic, use a mixture of tactics, or even add issues in the course of negotiations.

## References

[1] C. Beam, A. Segev, Automated negotiations: a survey of the state of the art, Wirtschaftsinformatik 39 (3) (1997) 263–268.

[2] A. Byde, M. Yearworth, K.-Y. Chen, C. Bartolini, Autona: a system for automated multiple 1-1 negotiation JEEE International Conference on E-Commerce CEC 2003, (IEEE, 2003), 2003, pp. 59–67.

[3] R. Carbonneau, G.E. Kersten, R. Vahidov, Predicting opponent's moves in electronic negotiations using neural networks, Expert Systems with Applications 34 (2) (2008) 1266–1273.

[4] A. Chavez, D. Dreilinger, R. Guttman, P. Maes, A real-life experiment in creating an agent marketplace, in: H. Nwana, N. Azarmi (Eds.), Software Agents and Soft Computing Towards Enhancing Machine Intelligence, Springer Berlin, Heidelberg, 1997, pp. 160–179.

[5] A. Chavez, P. Maes, Kasbah: An Agent Marketplace for Buying and Selling Goods, First International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology, Practical Application Company, London, 1996, pp. 75–90.

[6] E. Chen, R. Vahidov, G.E. Kersten, Agent-supported negotiations in the e-marketplace, International Journal of Electronic Business 3 (1) (2005) 28–49

[7] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of information technology: a comparison of two theoretical models, Management Science 35 (8) (1989) 982–1003.

[8] C.M. de Melo, P. Carnevale, J. Gratch, The effect of expression of anger and happiness in computer agents on negotiations with humans, Autonomous Agents and Multi-Agent Systems AAMAS, 2011, pp. 937–944, (International Foundation for Autono mous Agents and Multiagent Systems Richland, SC, Taipei, Taiwan).

[9] W.J. Doll, G. Torkzadeh, The measurement of end-user computing satisfaction, MIS Quarterly 12 (2) (1988) 259–274.

[10] A. Fabregues, C. Sierra, Proceedings of the 2010 conference on Arti<sup>fi</sup>cial Intelligence Research and Development: Proceedings of the 13th International Conference of the Catalan Association for Arti<sup>fi</sup>cial IntelligencePages 29-38IOS Press Amsterdam, The Netherlands, 2010.

[11] A. Fabregues, C. Sierra, HANA: a human-aware negotiation architecture, Decision Support Systems 60 (2014) 18–28

[12] P. Faratin, C. Sierra, N.R. Jennings, Negotiation decision functions for autonomou agents, Robotics and Autonomous Systems 24 (3–4) (1998) 159–182.

[13] P. Faratin, C. Sierra, N.R. Jennings, Using similarity criteria to make issue trade-offs in automated negotiations, Arti<sup>fi</sup>cial Intelligence 142 (2) (2002) 205–237

[14] M. Filzmoser, Automated vs human negotiation, International Journal of Arti<sup>fi</sup>cial Intelligence 4 (S10) (2010) 64–77

[15] D.L. Goodhue, R.L. Thompson, Task-technology <sup>fi</sup>t and individual performance, MIS Quarterly 19 (2) (1995) 213–236.

[16] R.H. Guttman, A.G. Moukas, P. Maes, Agent-mediated electronic commerce: a survey, Knowledge Engineering Review 13 (2) (1998) 147–159.

[17] G. Haim, Y.a. Gal, M. Gelfand, S. Kraus, A cultural sensitive agent for humancomputer negotiation Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems, vol. 1, International Foundation for Autonomous Agents and Multiagent Systems, Valencia, Spain, 2012, pp. 451–458.

[18] M. He, N.R. Jennings, H.-F. Leung, On agent-mediated electronic commerce, IEEE Transactions on Knowledge and Data Engineering 15 (4) (2003) 985-1003.

[19] S.-l Huang, F.-r. Lin, The design and evaluation of an intelligent sales agent for online persuasion and negotiation, Electronic Commerce Research and Applications 6 (3) (2007) 285-296

[20] N.R. Jennings, P. Faratin, A.R. Lomuscio, S. Parsons, M.J. Wooldridge, C. Sierra, Automated negotiation: prospects, methods and challenges, Group Decision and Negotiation 10 (2) (2001) 199–215.

[21] G. Kersten, S.J. Noronha, WWW-based negotiation support: design implementation, and use, Decision Support Systems 25 (1999) 135–154.

[22] G.E. Kersten, E. Chen, D. Neumann, R. Vahidov, C. Weinhardt, On comparison of mechanisms of economic and social exchanges: the Times model, in: H. Gimpel, N.R. Jennings, G. Kersten, A. Ockenfels, C. Weinhardt (Eds.), Negotiation and Market Engineering, Springer-Verlag, Berlin, Heidelberg, Germany, 2008, pp. 16–43.

[23] G.E. Kersten, R. Kowalczyk, H. Lai, D. Neumann, M.B. Chhetri, Shaman: software and human agents in multiattribute auctions and negotiations, in: H. Gimpel, N.R. Jennings, A. Ockenfels, C. Weinhardt (Eds.), Negotiation, Auctions, and Market Engineering, Springer Berlin, Heidelberg, 2008, pp. 116–149.

[24] G.E. Kersten, G. Lo, Aspire: an integrated negotiation support system and software agents for e-business negotiation, International Journal of Internet and Enterprise Management 1 (3) (2003) 293–315.

[25] S. Kwon, L.R. Weingart, Unilateral concessions from the other party: concession behavior, attributions, and negotiation judgments, Journal of Applied Psychology 89 (2) (2004) 263–278.

[26] C.-F. Lee, P.-L. Chang, Evaluations of tactics for automated negotiations, Group Decision and Negotiation 17 (6) (2008) 515–539.

[27] R. Lin, Y.a. Gal, S. Kraus, Y. Mazliah, Training with automated agents improves people's behavior in negotiation and coordination tasks, Decision Support Systems 60 (2014) 1–9.

[28] R. Lin, S. Kraus, Can automated agents pro<sup>fi</sup>ciently negotiate with humans? Communications of the ACM 53 (1) (2010) 78–88.

[29] R. Lin, S. Kraus, D. Tykhonov, K. Hindriks, C. Jonker, Supporting the design of general automated negotiators, in: T. Ito, M. Zhang, V. Robu, S. Fatima, T. Matsuo, H. Yamaki (Eds.), Innovations in Agent-Based Complex Automated Negotiations, Springer Berlin, Heidelberg, 2011, pp. 69–87.

[30] R. Lin, S. Kraus, J. Wilkenfeld, J. Barry, Negotiating with bounded rational agents in environments with incomplete information using an automated agent, Arti<sup>fi</sup>cial Intelligence 172 (6–7) (2008) 823–851.

[31] A.R. Lomuscio, M. Wooldridge, N.R. Jennings, A classi<sup>fi</sup>cation scheme for negotiation in electronic commerce, in: F. Dignum, C. Sierra (Eds.), Agent Mediated Electronic Commerce, Springer, 2001, pp. 19–33.

[32] F. Lopes, N. Mamede, A. Novais, H. Coelho, Negotiation tactics for autonomous agents, Database and Expert Systems Applications, 2001. Proceedings. 12th International Workshop on, (IEEE, 2001), 2001, pp. 708–714.

[33] P. Maes, R.H. Guttman, A.G. Moukas, Agents that buy and sell, Communications of the ACM 42 (3) (1999) 81-ff.

[34] N. Matos, C. Sierra, N.R. Jennings, Determining successful negotiation strategies: an evolutionary approach, International Conference on Multi Agent Systems, 1998, pp. 182–189, (International Foundation for Autonomous Agents and Multiagent Systems Richland, SC, Paris, France).

[35] T.D. Nguyen, N.R. Jennings, Managing commitments in multiple concurrent negotiations, Electronic Commerce Research and Applications 4 (4) (2005) 362–376.

[36] Y. Oshrat, R. Lin, S. Kraus, Facing the challenge of human–agent negotiations via effective general opponent modeling, Proceedings of The 8th International Conference on Autonomous Agents and Multiagent Systems, vol. 1, International Foundation for Autonomous Agents and Multiagent Systems, Budapest, Hungary, 2009, pp. 377-384.

[37] D. Pruitt, J. Rubin, Social con<sup>fl</sup>ict: Escalation, Stalemate, and Settlement, Random House, New York, 1986.

[38] I. Rahwan, L. Sonenberg, N.R. Jennings, P. McBurney, Stratum: A methodology for designing heuristic agent negotiation strategies, Applied Arti<sup>fi</sup>cial Intelligence 21 (6) (2007) 489–527.

[39] H. Raiffa, The art and science of negotiation, Harvard University Press, Cambridge, MA, 1982.

[40] H. Raiffa, J. Richardson, D. Metcalfe, Negotiation analysis, The Science and Art of Collaborative Decision Making, Harvard University Press, Cambridge, 2003.

[41] F. Ren, M. Zhang, A single issue negotiation model for agents bargaining in dynami electronic markets, Decision Support Systems 60 (2014) 55–67.

[43] V.L. Smith, Microeconomic systems as an experimental science, The American Economic Review 72 (5) (1982) 923–955.

[44] K.S. Suh, Impact of communication medium on task performance and satisfaction: an examination of media-richness theory, Information Management 35 (5) (1999) 295–312.

[45] R. Vahidov, Situated decision support approach for managing multiple negotiations, in: H. Gimpel, N.R. Jennings, G. Kersten, A. Ockenfels, C. Weinhardt (Eds.), Negotiation and Market Engineering, Lecture Notes in Business information ProcessingSpringer-Verlag, Berlin, Heidelberg, 2007, pp. 179–189.

[46] R. Vahidov, E. Chen, G. Kersten, Experimental assessment of agent-supported electronic negotiations, International Journal of Human Computer Interaction 29 (11) (2013) 764–774.

[47] R. Vahidov, G.E. Kersten, Decision station: situating decision support systems, Decision Support Systems 38 (2) (2004) 283–303.

[48] R. Vahidov, D. Neumann, Situated decision support for service level agreement negotiations, 41st Hawaii International Conference on System Sciences, HICSS, Waikoloa, Big Island, Hawaii, 2008

[49] B. Van de Walle, S. Heitsch, P. Faratin, Coping with one-to-many multi-criteria negotiations in electronic markets, 12th International Workshop on Database and Expert Systems Applications, 2001, pp. 747–751.

[50] A. van Wissen, Y. Gal, B.A. Kamphorst, M.V. Dignum, Human-agent teamwork in dynamic environments, Computers in Human Behavior 28 (1) (2012) 23–33.

[51] T.N. Wong, F. Fang, A multi-agent protocol for multilateral negotiations in supply chain management, International Journal of Production Research 48 (1) (2008) 271–299.

[52] Y. Yang, Y. See, A. Ortony, J. Tan, Subjective effectiveness in agent-to-human negotiation: a frame × personality account, in: P. McBurney, I. Rahwan, S. Parsons, N. Maudet (Eds.), Argumentation in Multi-Agent Systems, Springer Berlin, Heidelberg, 2010, pp. 134–149.

[53] Y. Yang, S. Singhal, Designing an intelligent agent that negotiates tactfully with human counterparts: a conceptual analysis and modeling framework, 42nd Hawaii International Conference on System Sciences, 2009, (IEEE, Hawaii).

Rustam Vahidov is a Professor of Business Technology Management at John Molson School of Business, Concordia University (Montreal, Canada) and holds Royal Bank of Canada Professorship in Inter-organizational Governance of IT. He received his PhD from Georgia State University. Dr. Vahidov has published papers in a number of journals, includ ing Journal of MIS, Decision Support Systems, Information and Management and others.

Gregory E. Kersten is a Professor of Business Technology Management at the Department of Supply Chain & Business Technology Management, John Molson School of Business, Concordia University (Montreal, Canada) and holds the Senior Concordia University Research Chair in Decision and Negotiation Systems. He is also the founder and director of the InterNeg Research Centre (http://interneg.concordia.ca).

Raafat Saade is an Associate Professor of Business Technology Management at the Department of Supply Chain & Business Technology Management, John Molson School of Business, Concordia University. His work has been published in a number of journals including Information & Management, Expert Systems with Applications, and many others.
