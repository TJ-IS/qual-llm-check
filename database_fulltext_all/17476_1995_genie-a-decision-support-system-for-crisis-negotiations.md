---
otero_id: 17476
otero_key: "27GJX42A"
title: "GENIE: A decision support system for crisis negotiations"
authors: "Jonathan Wilkenfeld; Sarit Kraus; Kim M. Holley; Michael A. Harris"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00027-p"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# GENIE: A decision support system for crisis negotiations \*

Jonathan Wilkenfeld $^{a,*}$ , Sarit Kraus $^{b,1}$ , Kim M. Holley $^{a}$ , Michael A. Harris $^{c}$

$^{a}$ Dept. of Government and Politics, University of Maryland, College Park, MD 20742 USA

$^{b}$ Dept. of Mathematics and Computer Science, Bar Ilan University, Ramat Gan 52900 Israel

$^{c}$ Inst. for Advanced Computer Studies, University of Maryland, College Park, MD 20742 USA

## Abstract

Decision support systems can play a role in improving the ability of decision makers to act as utility maximizers in crisis situations. This paper demonstrates the ability of one such decision support system, GENIE, to help decision makers maximize their objectives in a crisis negotiation. GENIE is described in detail, followed by the presentation of preliminary experimental results evaluating its effectiveness in crisis management and abatement. The experimental results show that GENIE users, as compared to non-users, are more likely to identify utility maximization as their primary objective and to achieve high utility scores. Experiments in which GENIE users participate are also more likely to end in agreement among the parties, rather than in an outcome in which one of the parties opts out of the negotiation.

Keywords: Decision support systems; Negotiation; International crisis; Hostage crisis; Simulations; User interface; Evaluation; Utility; Experiments

## 1. Introduction

Decision makers are frequently overwhelmed by the vast amounts of information which they must consider. Often, they are forced to make partially informed decisions which ignore critical issues because of the complexity of the situation being analyzed. This tendency becomes even more pronounced in situations of crisis.

In international relations, for example, the characteristics of a crisis include threat to basic values, finite time for response, and high probability of involvement in military hostilities. These elements all contribute to the possibility that individual decision makers will be overwhelmed with detail and possibly unable to identify optimal outcomes [48]). The vast literature of crisis decision making has shown that situations of intense crisis can create a reduced span of attention, cognitive rigidity and a distorted perspective of time (see [17] for an excellent review of the crisis decision making literature). These factors combine to make utility maximization difficult in a crisis situation.

Decision support systems (DSSs) can play a crucial role in the crisis decision making process by allowing the decision maker to navigate large amounts of information quickly and to explore interrelationships between factors which may influence the decision. A DSS can also facilitate the simultaneous evaluation of multiple positions in crisis negotiations. This can play a decisive role in real time negotiations by allowing the supported parties to rapidly formulate dynamic strategies and quickly evaluate their opponents' proposals. The basic argument in this paper is that the employment of a DSS by a crisis decision maker facilitates the identification of utility maximizing strategies on the part of an individual actor. $^{2}$ This paper tests the ability of one such decision support system, GENIE, to help decision makers maximize their objectives in a crisis situation and thus achieve utility maximization. GENIE $^{3}$ will be described in detail, followed by the presentation of preliminary experimental results evaluating its effectiveness in crisis management and abatement.

## 2. Related work on decision support and negotiation

Computer technology has been utilized in the aid of decision makers since the early 1970s. Eventually grouped under the heading of decision support systems (DSS), they come in a variety of different forms. They vary from relatively simple spreadsheet-like packages to state of the art blends of artificial intelligence and operations research technologies (these packages are detailed in the DSS literature including [44] [31] [41] [16] [45] [1]). While the main thrust of the development of DSSs has been to aid managers in the business world, DSSs can be applied to a variety of different situations in which decision makers deal with complex and difficult decision tasks.

One area in which DSS methodology has found increasing application has been the negotiation context. Specialized packages, referred to as negotiation support systems (NSSs), form a subset of the vast DSS literature. NSSs also come in a wide variety of different forms (for a review of some of the available NSS packages see $[19]$ ). The methods used range from conflict analysis and mathematical models to artificial intelligence methodology. Approaches to negotiation support take three basic forms: support for the entire negotiation group; mediation support; and support for individual negotiators.

## 2.1. Support for entire negotiation group

A group of decision makers involved in joint problem solving may need to reach agreement and resolve conflicts under conditions where each of them may have incomplete information, different sub-goals, and different perspective on the problem. Conflicts may arise over differing assumptions about the nature of the problem the group faces, conflicting evaluation criteria, differences over which issues to focus on and in which order, and competition over the use of limited resources required by group members to solve their portions of the problem.

A number of NSSs have been designed to support the entire negotiation group, by allowing information exchange about decision makers' goals, assumptions and evaluation criteria. These packages are generally referred to as group decision support systems (GDSS) [43].

Most GDSSs provide the group members with facilities to convey information, including features for representing members' positions; structured agendas that guide the group through a discussion of the conflict; utilities for problem definition; and structures to promote member participation (e.g., [33,14,20]).

There are GDSSs that, in addition to providing facilities for information exchange, help the decision makers to generate arguments and justifications that the group members can convey to each other. One such package, PERSUADER [43], uses artificial intelligence techniques (case-based reasoning) and decision theory methods (multi-attribute utilities). PERSUADER is able to incrementally propose modifications to proposal to help parties narrow their divergent views. It can help the parties communicate arguments and justifications and also suggest suitable arguments. PERSUADER is an intelligent DSS which learns from past negotiation cases and uses this knowledge as well as actors' preferences in determining the proposed compromise [43].

Another package, DENEGOT [30], is a distributed planning framework that bases conflict resolution on decentralized negotiation. Negotiation is viewed as a distributed search through potential compromises where each group member brings into the negotiation specific constraints on what it considers an acceptable resolution. It provides near-optimal compromises that can be achieved with tolerable amounts of computation.

## 2.2. Mediation support

Some NSSs have been designed to support a third party mediator or to act as mediators themselves by suggesting solutions to the negotiation problem. Representative of packages designed to support a third party mediator is MEDIATOR [18]. This NSS uses a data base-centred approach to consensus seeking. Each participant employs a DSS, PREFCALC, to form an individual utility analysis of the negotiation scenario. A mediator then assists in consensus seeking by aiding the players in building a group joint problem representation of the negotiation. Using this joint representation, a consensus is formed. MEDIATOR has been applied to hostage crisis situations in [9]. In these situations of intense hostility, players do not share their utility analysis. Instead, the human mediator creates the database based upon his/her understanding of the parties' positions.

NEGO [21] is an interactive system which uses multi-objective linear programming techniques to establish proposals from each of the individual participants. It then forms a sequence of compromise proposals based on relaxed participant demands. When a compromise proposal is produced that satisfies the revised set of demands, the problem is solved.

MCBARG [46] acts as a mediator by allowing the parties to examine and learn from the model and then to select a preferred outcome. The NSS then takes these results and finds a way to improve the status quo in terms of these preferences. The result is a single negotiating text which can be improved upon by utilizing it as the new status quo and running another iteration.

Two additional negotiation support systems which aid mediation, ISES and SAM [37], have been developed by the MIT Project on Modelling for Negotiation Management. ISES allows users to transfer proposals, in the form of lists of parameters, and then run a simulation model to determine the effects of the proposals. SAM allows users to select important norms and then run a simulation to determine the outcomes to which these negotiation norms would lead. The parties can then take these outcomes together as a group and determine which best supports their negotiating goals.

DecisionMaker: the Conflict Analysis Program $[10]$ makes use of conflict analysis methodology to determine possible compromise solutions. A single user could also ask DecisionMaker what the likely moves of opponents will be given a world state. DecisionMaker would take this state and determine how actors would manipulate it to reach one of the conflict equilibria.

## 2.3. Support for individual negotiators

A third approach to negotiation support is to provide support to individual negotiators. These systems represent stand-alone DSSs which are designed to aid one party to a negotiation in determining a successful course of action. Examples of these systems include NEGOTIATOR, MATCH and NEGOPLAN.

NEGOTIATOR [6] can be used as a standalone DSS or as a portion of a group decision support system when integrated with communication software. It was designed in a three stage process which first examined the value of multiple-attribute utility (MAU) methodology and then that of neural network learning techniques. The final form of NEGOTIATOR fused neural network and MAU methodologies.

Another product of the Project on Modelling for Negotiation Management, MATCH [37], makes use of past precedent in supporting the negotiator. MATCH compares the negotiation situation with past situations and allows the user to determine what strategies have been used to what effect in similar situations.

NEGOPLAN [28] is an expert system shell designed to support a participant in a two party negotiation problem. It allows a user to define a model of the negotiation scenario using And/Or trees of Prolog-like facts. It then uses forward inference to anticipate opponent reactions to the user-proposed negotiating position. In this way, NEGOPLAN helps a negotiating party to try different negotiating positions and evaluate their consequences. NEGOPLAN has also been applied to a hostage crisis situation in [29].

GENIE, the subject of the present article, is an individual negotiation support system. While GENIE can be used by all participating decision makers in a crisis situation, each application of GENIE by a player operates individually, without any direct relation to the other applications (although participants can communicate their findings with each other). Also, GENIE does not act as a mediator, since it does not attempt to locate a solution to the negotiation problem. It can, however, be used to support a self-interested mediator as experimental results will later show. For these reasons, it is most similar to NEGOTIATOR, MATCH and NEGOPLAN. GENIE makes use of mathematical modelling techniques in order to aid the user in visualizing the negotiation situation and in considering what-if scenarios. GENIE shares the use of MAU modelling with NEGOTIATOR and the what-if approach with NEGOPLAN.

## 2.4. A comparison of GENIE and NEGOPLAN

The usage of GENIE is most similar to NEGOPLAN in that a user can explore various negotiation positions without making ‘judgments’ about the utility of the positions. GENIE and NEGOPLAN use different approaches to achieve the same goal. While NEGOPLAN uses artificial intelligence techniques to model the negotiation process, GENIE attempts to give the user a mental picture of the negotiation model through problem structuring and knowledge organization (See [34] for a detailed discussion of model visualization techniques for DSS). Both GENIE and NEGOPLAN require extensive work on the part of experts to define the negotiation model for a specific scenario. In GENIE this model is contained in the knowledge base module, whereas in NEGOPLAN it is contained in goal representation trees and rules.

A major function of GENIE is to present a complex negotiation model to the user in an easily understandable and organized manner. To achieve this, GENIE uses an interactive outline (see section 4.3) which presents the types of data in the model as outline topics and allows the user to interactively select the topics of interest. NEGOPLAN takes a somewhat more complex approach by attempting to use the negotiation model to generate possible stages of the negotiations. One advantage of GENIE's method of model visualization is that it provides increased flexibility in the investigation of negotiating positions. Because NEGOPLAN uses forward chaining, a user must start with an initial position and then investigate subsequent negotiating positions in the forward direction. With GENIE, a user can investigate any position almost instantly. This allows forward, backward, or random evaluation of positions during the formulation of a negotiating strategy. It also allows a negotiator to use GENIE to quickly evaluate opponent proposals during actual negotiations. Also, GENIE allows the user to view an arbitrary set of negotiating positions simultaneously, within limits on the cardinality of this set which are imposed to insure comprehensible graphic output. This may not be possible with NEGOPLAN because of its sequential generation of negotiation stages.

GENIE also differs from NEGOPLAN in its full information stipulation. NEGOPLAN is more flexible and allows for changes of the issues and preferences during the course of the negotiation by the addition of new rules and metafacts. GENIE does not allow this type of flexibility. It is more useful for negotiations in which the issues, but not necessarily the value the parties assign to outcomes, remain static. What is lost in flexibility, however, is made up for in visualization ability for the user.

## 3. Scenario and negotiation model

The implementation of GENIE which was tested in this article contains knowledge base and interface modules tailored to a hostage crisis situation involving India, Pakistan and Sikh hijackers. The brief description which follows will help the reader understand both the design features of GENIE and the preliminary experimental results (for additional discussion of the model and the underlying crisis framework, see $[25]$ and $[23]$ ).

## 3.1. The hostage crisis simulation

We have already noted that in the field of international relations, crisis situations are among those which could potentially benefit the most from the implementation of a DSS, due to the unique co-occurrence of the conditions of time pressure, high stakes, and potential violent activity.

For the purpose of developing the GENIE NSS, a hostage crisis situation was chosen as a typical case of multiparty negotiation. The scenario is based on the hypothetical hijacking of a commercial airliner enroute from Europe to India and its forced landing in Pakistan. The passengers are predominantly Indian and the hijackers are known to be Sikhs. The hijackers demand the release from Indian security prisons of up to 800 Sikh prisoners (see [22]). $^{4}$

The three parties must consider several possible outcomes: India or Pakistan launch military operations to free the hostages; the hijackers blow up the plane with themselves aboard; India and the Sikhs negotiate a deal involving the release of security prisoners in exchange for the hostages; Pakistan and the Sikhs negotiate a safe passage agreement; and the hijackers give up.

The specific issues to be negotiated are the following: India-Sikhs:

\- Number of security prisoners to be released by India in exchange for release of all of the hostages.

India-Pakistan:

\- Indian request for logistical information to enhance probability of success of an Indian military operation.

\- Indian request for assistance (or at least neutrality) during an Indian operation, to enhance probability of success.

\- Indian request that Pakistan deny the hijackers press access in order to prevent them from publicizing their message.

\- Pakistani request for Indian assistance during a Pakistan operation, to enhance probability of success. Pakistani request that India accept a Sikh offer.

Pakistan-Sikhs:

\- Hijackers' request for press access to publicize their cause.

\- Pakistani request that the hijackers give up or reach an agreement for safe passage.

\- Pakistani request that the hijackers accept an Indian offer.

In the simulation setting, actors negotiate these issues until an agreement is reached or a player opts out of the negotiations by launching a military operation (India or Pakistan) or blowing up the plane (Sikhs).

Each party to the negotiation has a set of objectives, and a certain number of utility points is associated with each (see [22]). Utility points were assigned in order to express a complex set of preferences in such a way that subtle distinctions can be made among them. In combining the range of utility points associated with each objective with the possible outcomes, a matrix is generated which yields a point output total for each outcome. We note that these payoff points are not utility functions (in the decision theory sense), but rather our description of the crisis. Each player will develop his/her set of preferences for the outcomes based on these utility points (see [8]).

Time is incorporated into the model both as a reference point for the calculation of utilities and probabilities, and as a differential factor for the three parties. In general, time works in favour of the hijackers, and against India and Pakistan. Time impacts on the probability of success and failure of an operation to free the hostages (whether it is day or night, whether there is time to train a rescue team, etc.), on publicity for the Sikh's cause (regardless of whether direct press access is granted), and deterioration over time in India and Pakistan's internal and external images (for more detail on the Hostage Crisis Simulation, see [23]).

## 3.2. The strategic negotiation model

In this section we will describe a strategic model of negotiation which is the basis for the development of the Hostage Crisis Simulation. Our framework is a model of alternative offers $[36]$ which focuses on the passage of time during the negotiation and the preferences of the players for different agreements as well as for opting out of the negotiations.

We assume that there are three players: the 'Initiator' of the crisis –the Sikh hijackers (Sik); the 'Participant' (against its will) in the crisis –India (Ind); and a 'Third party' –Pakistan (Pak). This model can be extended to any three player situations with similar characteristics [24,27].

There exists a set of possible agreements between all possible pairs of players. $^{5}$ The negotiation procedure is as follows. The agents can take actions only at certain times in the set $T=\{0,1,2\ldots\}$ . In each period $t\in T$ one of the agents, say i, proposes an agreement to one of the other agents. That agent (j) either accepts the offer (chooses Yes) or rejects it (chooses No), or opts out of the negotiation (chooses Opt). Also, the third player who neither received nor made an offer may opt out of the negotiation (chooses Opt), or it can choose not to do anything (chooses Nop). $^{6}$ If the offer is accepted, without the third agent opting out, then the negotiation ends, and the agreement is implemented. Opting out by one of the agents also ends the negotiation. $^{7}$ After a rejection, the next agent then has to make a counteroffer, and so on. There are no rules which bind the agents to any previous offers they have made and there is no limit on the number of periods. The only requirement we make is that the length of a single period is fixed.

Formally, we denote by $\mathcal{A}$ the set of players, i.e., $\mathcal{A} = \{Sik,Ind,Pak\}$ . We assume that the set $S_{i,j}$ , $i,j\in \mathcal{A}$ , $i\neq j$ includes the possible agreements between players $i$ and $j$ . We also assume that $S_{i,j} = S_{j,i}$ and denote the set of all possible agreements by $S$ . If an agreement is never reached, and none of the players opts out, we assume the outcome to be Disagreement. If the players reach an agreement $s\in S$ in time $t\in \mathcal{T}$ we denote this outcome by $(s,t)$ . If one of the players opts out at time period $t\in \mathcal{T}$ we denote this outcome by (Opt, $t$ ).

A negotiation strategy for an agent is a function from the history of the negotiations to the present move (see formal definition in [27]).

In order to analyze such situations we use the notion of (subgame) perfect equilibrium (P.E.) (see [38]) which requires that the players' strategies induce an equilibrium in any subgame [27].

In analysing the Hostage Crisis case, we identified special conditions on the sets of possible agreements. In our case $S_{Ind,Pak} = \emptyset$ , i.e., there is no possible agreement between India and Pakistan that can end the crisis. There is only one possible agreement between the hijackers and Pakistan (hostages are freed and hijackers are granted free passage).

We assume that India holds W Sikh security prisoners and an agreement between the hijackers and India is a pair $(s_{Sik}, s_{Ind})$ where $s_{Sik}, s_{Ind} \in NI$ , $s_{Sik} \geq 1$ and $s_{Sik} + s_{Ind} = W$ . That is, an agreement between the hijackers and India is the division of the W prisoners between them. In the hostage crisis situation W = 800 (Sikh prisoners in Indian jails).

The last component of the model is the preference of the players on the set of outcomes. Each player has preferences over agreements reached at various points in time, and for opting out at various points in time. The time preferences and the preferences between agreements and opting out are the driving force of the model. Formally, we assume that player $i = \text{Sik}, \text{Ind}, \text{Pak}$ has a preference relation (complete, reflexive, and transitive) $1_i$ on the set $\{\{\mathbf{S} \cup \{\mathbf{Opt}\}\} \times \mathcal{T}\} \cup \{\text{Disagreement}\}$ .

We have identified several conditions that the preferences in the Hostage Crisis satisfy. We assume that these conditions are known to all players. That is, we have developed a model of complete information. An extension of this model which deals with incomplete information is described in [27].

## A0. Disagreement is the worst outcome.

A1. The prisoners are desirable: For any $(s_{Sik}, s_{Ind}), (r_{Sik}, r_{Ind}) \in S_{Sik,Ind}$ and $t \in T$ , if $r_i \geq s_i$ , (i = Sik, Ind) then $((r_{Sik}, r_{Ind}), t) l_t ((s_{Sik}, s_{Ind}), t)$ .

A2. Agreement's cost over time: Pakistan and India prefer reaching a given agreement (either Pakistan/Sikh or India/Sikh agreement) sooner rather than later. In particular, India prefers to release any given number of prisoners sooner rather than later, while the hijackers, through period 10, prefer to obtain any given number of prisoners later rather than sooner.

India has a number $c_{Ind} < 0$ such that $^{8}$ : For any $(s_{Sik}, s_{Ind}), (r_{Sik}, r_{Ind}) \in S_{Sik,Ind}$ and $t_1, t_2$ $\in \mathcal{T}, ((s_{Sik}, s_{Ind}), t_1) l_{Ind}((r_{Sik}, r_{Ind}), t_2)$ iff $(s_{Ind} + c_{Ind} * t_1) \geq (r_{Ind} + c_{Ind} * t_2)$ . The hijackers, through period 10, prefer any agreement later rather than sooner. In particular, the hijackers have two constants $c_{Sik} > 0$ and $c_{Sik}' < 0$ such that: let $t_1, t_2 \in \mathcal{T}$ , and we will assume that for $i = 1, 2$ , $t_i = t_i^1 + t_i^2$ where if $t_i \geq 10$ , $t_i^1 = 10$ , otherwise then $t_i^2 = 0$ . For any $(s_{Sik}, s_{Ind}), (r_{Sik}, r_{Ind}) \in S_{Sik,Ind}$ , $((s_{Sik}, s_{Ind}), t_1) l_{Sik}((r_{Sik}, r_{Ind}), t_2)$ iff $(s_{Sik} + c_{Sik} * t_1^1 + c_{Sik}' * t_1^2) \geq (r_{Sik} + c_{Sik} * t_2^1 + c_{Sik}' * t_2^2)$ .

A3. Opting out over time: India and Pakistan prefer to opt out sooner rather than later. The hijackers, through period 10, prefer opting out later rather than sooner.

We note that assumption (A2) does not hold for Opt and the preferences of the players for opting out in different periods of time do not change in a stationary way. Furthermore, the preferences of a player for opting out versus an agreement fluctuate across periods of time in a non-stationary fashion. $^{10}$ In the case of the Hostage Crisis this is due to different rates of change over time in the probabilities associated with success or failure of the actions taken when opting out.

A4. Possible agreement: The hijackers and Pakistan prefer any possible agreement over opting out. In the first period there is at least one agreement between the hijackers and India which all players prefer over opting out.

A5. Preferences for agreements: While the Sikhs prefer any agreement between themselves and India (victory for the Sikhs) to any agreement between themselves and Pakistan (i.e., defeat for the Sikhs), both India and Pakistan prefer a Sikh/Pakistan agreement at any time to any Sikh/India agreement or opting out.

The above assumptions (especially A2 and A3) demonstrate that time is an important element in the strategic model $[27]$ . Specifically, we propose that although the hijackers gain utility over time, there is a point at which the process is reversed and the hijackers begin to lose over time (in the Hostage Crisis, this can be due to factors such as a shift in media sympathy from the plight of the Sikh prisoners to the deteriorating circumstances of the hostages on board the aircraft).

We have formally shown [24] that if there is a time period in which the hijackers start to lose over time and if the players use perfect equilibrium strategies, then agreement will be reached in this time period (period 10 in the Hostage Crisis scenario) between the hijackers and Pakistan (for a description of specific applications of the strategic model of negotiation see [25]).

## 4. GENIE

GENIE $^{11}$ is a specifically customized version of a larger problem domain that focuses on n-player, time variant negotiations with full information. Although GENIE was specifically developed with the hostage crisis in mind, its basic design allows for modification to handle any scenario of this type. In the past, we have modified GENIE to fit different hostage crisis scenarios including moving the hostage crisis from the Middle East setting to East Asia. Modifiability is achieved through the use of modular design as suggested by Fumás [12]. GENIE was designed in three basic modules: the knowledge base module (see section: 4.2), the interface module (see section: 4.3), and the display module (see section: 4.4). This design allows for the quick modification of the DSS by replacing the existing knowledge base with another one, in the same well-defined format, and thereby modelling a different scenario. $^{12}$

## 4.1. Information in GENIE

GENIE assumes full information on the part of all parties to the negotiation. That is, the players have full knowledge of their own objectives and their associated utilities, as well as those of their opponents. Although the decision to assume full information was made in order to simplify aspects of the original strategic model of negotiation upon which this DSS is based, $^{13}$ there are strong justifications for its application in this case. First, while there is complete information about objectives and outcomes, there is incomplete information about the state of the world. That is, the content of bilateral messages exchanged by players is not known. In the hostage crisis scenario, the extent of information shared between India and Pakistan is not known by the Sikhs. Second, in crises involving actors which are participants in long, protracted conflict situations, there is a high degree of knowledge about the objectives and utilities of the other parties. That is, the hostage crisis situation is not among parties which have been randomly thrown together. Rather, the participants have interacted in a conflict situation over a long period of years, and are well known to each other.

Finally, both the experimental work which has been initiated with GENIE, as well as its training function, require that complete information on objectives and outcomes be provided. In particular, when individual players will be taking part in more than one run of the hostage crisis simulation, each time perhaps from the perspective of a different actor (India, Pakistan, Sikhs), it will be important that each time through we will be able to assume that they are working from the same knowledge base. The only way to ensure that is to provide all information to all players from the outset. Multiple plays with different roles is particularly useful when GENIE is used for negotiation training.

## 4.2. The knowledge base

The version of GENIE tested in this article contains a knowledge base tailored to the hostage crisis situation. The knowledge base contains full information regarding the objectives of the three players and how each of six possible outcomes impacts on these objectives. It also contains information regarding the effects of world state parameters –such as time and the Sikhs gaining access to the press –upon the ability of the parties to achieve the relevant objectives (for a complete listing of these objectives and the associated point totals, see [22]).

When a query is made to the knowledge base, multi-attribute utility (MAU) analysis methodology is utilized. The value of each objective is determined given the outcome and world state the user is considering. These values are then tallied to produce a utility score for that actor for that outcome given the state of the negotiation.

MAU methodology is widely used in negotiation support technology in such packages as DecisionMap, ExpertChoice and Aborist [2] as well as the NSS, NEGOTIATOR, discussed above. Despite this wide use, the method has been criticized. Three major criticisms were offered in [42]. First, MAU requires that all criteria be mutually exclusive and independent. Second, differences in culture make it difficult to accurately assess the preferences of the other actors. Third, the technique provides a static view of negotiation and does not allow alteration of the preferences during the course of negotiations.

![](/api/attachments/27GJX42A/fulltext/images/74bd6860860849b33cb100351b4d07f3e7da3c95b4b24465dcaf511f28259c3e.jpg)  
Fig. 1. The GENIE interface.

MAU analysis does not claim to produce perfect modelling of the negotiation situation. However, it is unlikely that human decision makers could do better than the simplifications offered by MAU methods when complex and interrelated criteria are involved. Human negotiators would also share the difficulties associated with determining preferences of actors of different cultures.

As for the static nature of the MAU model, GENIE is currently implemented for a hostage crisis situation, a short term, high pressure situation in which preferences are not likely to change to any great extent. The GENIE model does, however, allow the user to change world state parameters which affect the degree to which different outcomes satisfy each parties' objectives.

In sum, the MAU analysis utilized by GENIE aids a decision maker in acting as a utility maximizer by providing a method for evaluating conflicting goals.

## 4.3. Interface

GENIE is designed to be used by crisis participants who have little or no knowledge of computers, and who would not normally be expected to resort to their use in decision making situations. Therefore, the interface was designed to be menu driven and mouse supported. Among the advantages of menu-driven systems are the ease with which novice users can navigate powerful and complex systems, and the opportunity to use increasingly sophisticated features as the user's skill and comfort levels increase (See [40]). The mouse allows flexibility when dealing with complex screens that have many fields. Overall, as we will see below, GENIE provides all the features needed for negotiation in a single environment.

GENIE's interface presents the user with a main menu bar with five choices: SCENARIO, OUTCOMES, MESSAGES, ACTIONS, and SYSTEM. Along with the main menu bar is an information screen which reports the current status of the simulation. Fig. 1 presents a display of the main menu bar, and the items contained in the five pull-down menus.

\- SCENARIO – produces a list of topics about which a user can get information, including a description of the current situation, the objectives of the various actors, the rules of the simulation, guidelines on negotiation strategy, and the method of calculating probabilities and outcomes.

\- OUTCOMES –the central decision making mechanism of the DSS. Selection of SET VIEWING OPTIONS displays the interactive outline (see section 4.3.1), SET RISK ATTITUDES allows for experimentation with the risk attitudes of the other parties to the crisis (see section 4.4.3), and SHOW GRAPHS provides the user with various types of graphical presentations of the utilities associated with various outcomes, for him/herself, as well as for the other parties (see section 4.4).

\- MESSAGES - prompts the users for connection to the communications portion of the DSS (see below), allowing for direct communications among the crisis participants.

\- ACTIONS -provides the users with a list of available options, some of which are irreversible, and some of which will have the effect of ending the simulation.

\- SYSTEM -allows the user to update parameters and to exit the system, either permanently or for a break (in which case all changes to that point are saved to a file).

During the simulation, players negotiate through the exchange of electronic mail messages. Communications for the negotiation simulation are handled by the POLNET II electronic conferencing system, designed to support the ICONS foreign policy simulations developed at the University of Maryland (See [5,32,47,49]). POLNET II allows simulation participants who are not face-to-face to communicate with each other and the game manager via electronic mail messages. GENIE allows a player to enter the POLNET II environment and, by selecting the menu item MESSAGES, conduct negotiations, and then quickly return. Upon return, the environment is exactly as it was immediately before the call to POLNET II (i.e., all options remain set the way the user left them). This facilitates the rapid evaluation of offers made by other parties as well as the dynamic formulation of negotiation strategies.

The following section presents a detailed description of the interactive outline, the operational heart of the GENIE NSS.

## 4.3.1. Interactive outline (outcomes)

GENIE is designed to provide the user with a clear mental picture of the model contained in the knowledge base. This is a difficult task since the model of the scenario being analyzed is complex, with numerous interdependencies among data objects. The task is further complicated when the model contains large amounts of numeric information. Research $[34]$ has shown that images and symbolic representations are much more easily assimilated than is textual information. This would suggest representing the structure and content of the model in some symbolic form. The problem is then to find a concise symbolic representation for the model. $^{14}$

GENIE combines its data management and modelling capability in one mouse-supported screen (OUTCOMES) which enables a user to quickly set parameters for the viewing of information. This screen not only provides quick access to information items in the knowledge base, but also allows the user to form a mental picture of the entire simulation. With this outline, the user can then brainstorm and experiment with different options to form a personalized strategy for utility maximization.

One data management feature of GENIE which is critical to any successful DSS is the ability of the user to control the complexity of the queries and responses from the DSS. Novice users who ask the DSS simple questions should not be flooded with screens of complex charts and graphs. At the same time, advanced users should have the facilities to develop sophisticated strategic models. GENIE's interface allows a user to define one or more hypothetical states of the world and then to investigate possible future actions based on these states. The user can explore outcomes resulting from his/her own actions as well as those of his/her opponents. Also, a user can switch viewpoints to see things from the point of view of one or more of his/her opponents. This is possible, since the model assumes full information. A simultaneous display of these viewpoints allows the user to formulate a strategy which takes into account possible opponent actions. The system employs a model specific interactive outline with information categories which a user can select to see graphic information about the scenario. This outline gives the user access to the major model visualization and data management features of the system which include: multiple frames of reference, time variant outcome projections, and multiple world state definitions.

The interactive outline screen presented in Fig. 2 is organized into three main categories: viewpoints, information items, and world states. All of the model visualization capabilities of the system are contained within these three categories.

The viewpoints section allows the user to specify the point of view for all subsequent queries to the knowledge base. The parties involved in the negotiations are listed. The user can interactively select one or more of these parties to define a set of viewpoints. When more than one viewpoint is selected, information corresponding to each is displayed simultaneously. This facilitates the development of strategies based on a comparative analysis of the outcomes for some or all of the parties involved.

Having fixed the viewpoint(s), the user can then move to the information items section of the outline. This gives the user a list of all of the possible types of information that can be requested during the course of the negotiations. As seen in Fig. 2, the crisis may end in a deal for the release of Sikh security prisoners being held in India, a Sikh/Pakistan agreement for safe passage, the Sikhs blowing up the plane or surrendering, or an Indian or Pakistani operation. The user may select any number of these outcomes to investigate, again facilitating comparative analysis. In the case of an Indian/Sikh deal, the user must uniquely identify the decision(s) to be investigated by specifying the exact number of security prisoners to be released in exchange for the hostages. Note that since the model contains information about decisions that can be made by any of the parties, each party that is supported by the system can ask for information about all decisions, not just those that he/she can personally make.

Once the frame(s) of reference and decision(s) are fixed, the user can then move to the world states section. Here, a user specifies parameters that define the hypothesized state of the world at the time the decision(s) previously specified takes effect. These parameters are time, press access, Pakistani behaviour in the event of an Indian operation, and Indian behaviour in the event of a Pakistani operation (these aspects of the model are discussed in the description of the Hostage Crisis Simulation in 3.1 above). They constitute aspects of the model which are negotiable among the parties.

The organization of the interactive outline reveals the main structure of the model by emphasizing the dependence of the decision(s) on the state of the world at the time they are made. The identification and investigation of these dependencies is a critical step in the formulation of a rational negotiating strategy. One of the powerful features of the system is that it allows a user to vary world state parameters. Often decision makers have some influence over the state of the world (i.e., they have influence over some of the parameters in the world state definition). During strategy formulation, a decision maker may want to find out whether it is worth it to expend energy to change the world state. For example, in the hostage crisis scenario, the Sikhs could decide that they will blow up the plane and kill all of the hostages. In this case they should try to influence the state of the world so that at the time of the action, they (or their cause) receive maximum benefit. Influencing the state of the world could mean waiting a certain amount of time or convincing Pakistan to allow press coverage. GENIE lets a user select multiple values for a given parameter and then simultaneously view the selected decision outcomes based on the different states. This provides the user with a powerful tool to evaluate the effects of differing world state variables upon the negotiation and furthers the possibility of utility maximization.

![](/api/attachments/27GJX42A/fulltext/images/336c382429c33b9787e10b5dd5c1103ada78cda42853f861185b072e46ada5ef.jpg)  
Fig. 2. The interactive outline.

## 4.4. Display module

GENIE provides the user with two different graphic output options. A user can select information about outcomes for one specified time period. This results in the display of bar graphs representing the utility point totals associated with that outcome from the selected viewpoints given the selected world states as shown in Fig. 3. These bar graphs provide the user with the specific point totals in an easy-to-read graphic output which allows the user to quickly evaluate the relative utility values of different outcomes. In addition to this information about point totals associated with outcomes, the bar graph display also provides the user with the exact probabilities associated with the potential outcomes of military operations (success, partial success, and failure), as well as the possibility of projecting expected utilities. $^{15}$

Fig. 4 presents a second graphic option open to the user, in the form of time series graphs. A user selects these graphs by choosing multiple time periods. Selection of Display Graphs then results in line graphs being drawn for the different outcomes from the selected points of view. This option allows a user to quickly evaluate the role of time given the current state of negotiations.

In addition to these graphic functions, GENIE provides two analytical functions: the projection option and scratch pad.

## 4.4.1. The projection option

Successful negotiation requires that an agent identify actions that will be most beneficial to him/her while taking into account the possible actions/reactions of his/her opponents. A mutually beneficial resolution (MBR) to a negotiation scenario is a resolution which is beneficial to either all of the parties or some subset of the parties. In other words, MBRs are suggestions for possible compromise solutions to a crisis.

Identification of mutually beneficial resolutions is a computationally intensive task which would be difficult for a negotiating agent without access to automated support. This is especially true when the values associated with the outcomes are changing with time. For example, assume that India wants to evaluate the following four possible outcomes: Indian operation is successful, Indian operation is partially successful, Indian operation fails, and making a deal with the Sikhs to release a specific number of security prisoners. Moreover, assume that the agent wants to investigate these outcomes over 20 time periods. India would have to calculate the values of each of these outcomes for each time period for itself and for each of the other parties in the negotiation. This would require the Indian agent to make 2400 calculations. These calculations alone are burdensome and don't even account for the time needed to search for MBRs.

The projection option allows an agent to select outcomes to investigate and then displays information for those outcomes with high ranking payoffs. Fig. 5 presents a typical projection option display. This projection information can be automatically calculated for each of the players in the negotiation. Once the values are calculated and displayed the system searches through the calculated values looking for mutually beneficial resolutions. When an MBR is found, it is highlighted for easy identification by the user. The user can specify which sets of actors to consider in the MBR. The user can examine the MBR for all three players, or if it is determined in the course of negotiations that one player is a weak or irrational negotiator, the user can eliminate this player from the set and view the MBRs between only two actors.

## 4.4.2. The scratch pad

Before discussing the scratch pad feature, we must introduce the notion of reservation price. The reservation price of a negotiating agent is the payoff that the agent can insure him/herself in the worst possible case. In a negotiation scenario, an agent who ‘leaves the table’ is said to have opted-out of the negotiations. For example, in the hostage crisis simulation, the hijackers can opt-out of the negotiations by attempting to blow up the plane. Their reservation price is the payoff value that can be obtained from a worst case scenario of opting-out. Game theory suggests that a player involved in a negotiation scenario should construct a strategy based on his/her reservation price ([35]).

![](/api/attachments/27GJX42A/fulltext/images/3926fe4c19f3368aee5588bf0152b3151dc9ede1f8d0743bc55832165cd13b65.jpg)  
Fig. 3. Bar graphs.

![](/api/attachments/27GJX42A/fulltext/images/0df31ad6d4f6d8da44a797ee3f73ff82ce36be6d6aac62fb022803eeda31c375.jpg)  
Fig. 4. Line graphs.

The scratch pad feature displayed in Fig. 6 helps a negotiating agent to compare the payoff obtained from a negotiated settlement with that obtained from opting-out of the negotiation. It automatically calculates a player's reservation price and finds the optimal time period for a player to opt-out of the negotiations. It also determines a negotiated settlement that has an equivalent or higher payoff than opting-out in the optimal time period.

For example, assume that in the India-Pakistan-Sikh scenario, the Sikhs propose a deal with India to release all of the hostages in exchange for the release of a specified number of Sikh security prisoners. It would be useful for India to know the expected return from alternative outcomes, launching an operation or the Sikhs blowing up the plane. They could then know the worst possible thing that could happen to them should they not accept the deal. The expected payoff from this worst possible event can be said to be the reservation price of the Indian agent. If the

![](/api/attachments/27GJX42A/fulltext/images/bc2f637a5e0e8be34a40bb2c6a052fbd2477042fab9e9f8f28d064b9e7b9b48c.jpg)  
Fig. 5. The projection option.

![](/api/attachments/27GJX42A/fulltext/images/013992f31dc40b409205dd41456edeed03819cac79b1d687b72ca3449dad59f6.jpg)  
Fig. 6. The scratch pad.

payoff from the proposed deal is less than the reservation price of the Indian player then the Indian player may choose to reject the proposal. $^{16}$ The scratch pad feature is an automated tool for calculating reservation prices. It allows a user to explore a specified range of time periods, $^{17}$ and calculate a reservation price based on values obtained from an expected worst case scenario of opting-out.

## 4.4.3. Modelling risk attitude

Attitude towards risk becomes an important consideration when a player is trying to predict the actions of an opponent. Seeing an opponent's options in a given situation does not give the user any idea about how the opponent values these outcomes. GENIE has a feature which helps the user form an approximation of an opponent's view of the world. It allows a user to fix an attitude towards risk for each opponent in the negotiation. The values for attitude towards risk are: risk neutral, risk averse, and risk prone. It can be shown [[11], p. 177-178] that a person's attitude towards risk determines the shape of his/her utility function. A risk averse person has a concave utility function, a risk prone person has a convex utility function, and a risk neutral person has a linear utility function. We use these functions in the models of risk attitude. Through the course of negotiations, the user can estimate the opponents' risk attitudes and then set the DSS to display the opponents' utility scores for risky outcomes given the associated utility functions.

## 4.5. Evaluation of design features of GENIE

The various features of GENIE discussed above were designed to provide the user with powerful yet easily-mastered tools to increase his/her effectiveness as a crisis negotiator and thus increase the probability of achieving a utility maximizing outcome. The interactive outline allows the user to visualize the model and select information to be displayed. Graphic output facilitates the evaluation of alternative outcomes in different world states. The projections option helps the user find mutually beneficial outcomes, while the scratch pad feature determines reservation prices. These tools provide the user with the ability to understand and analyze the complex information contained in the model.

It would be useful to assess the extent to which the design features of GENIE facilitate effective crisis decision making. In the next section, we discuss experimental results designed to assess performance when the DSS is employed. But another strategy is to evaluate GENIE according to criteria set out in the literature of DSS design. One such list is provided by Shneiderman [40] –the eight ‘golden rules’ of dialogue design.

1. Consistency -All selections are made by clicking the mouse next to the item selected. When the user is finished viewing output, pressing escape returns the user to the main menu, regardless of which graphic or analytic tool has been used.

2. Frequent or advanced users can take shortcuts – Use of a mouse-supported screen allows the knowledgeable user to jump around to make desired changes to a past request without going through each piece of information sequentially.

3. Every action gives information feedback -When an item is selected, a check mark appears. When graphic output is selected, the screen displays it.

4. The dialogue yields closure –When the user selects all information of interest, he/she can click on 'okay' to bring him/her to the analytical and graphic tools selection menu.

5. Errors are handled simply -Error windows are displayed with suggestions on possible corrections.

6. Reversal of action achieved easily -Simply pointing and clicking on the selected item will turn it off.

7. Internal locus of control -All choices that can be made are clearly displayed in an easy-to-visualize format.

8. Short term memory load reduced -All information appears on a single easily organized screen, subdivided into sections with a limited number of items to consider in each.

Pulldown menus, on-line documentation, fully-integrated communications software and text editor, and simplified exit and re-entry procedures are among the additional features enhancing the comfort levels for both novice and experienced users. Overall, GENIE's features mask the powerful computational and display technology in its design, allowing the user to focus on the analytic problem at hand without having to worry about the technology behind it.

## 5. Experimental results

Previous experimental work on the usefulness of decision support systems in the decision process have produced mixed results. A review of the management literature by Benbasat, DeSanctis and Nault [3] found that the DSS had a positive impact in some studies, a negative impact in others and produced mixed results in a third set. The negotiation support system literature has tended to be more system descriptive rather than experimental.

To examine the general proposition that GENIE helps negotiators to act as utility maximizers and thus to improve their performance in simulated crisis situations, a set of carefully designed experiments was conducted. The proposition would be well supported if experimental results showed that the users of the decision support system, as compared to non-users, placed more emphasis upon utility maximization in their negotiating goals and were more capable of realizing this goal in the negotiating situation. $^{18}$ A stronger motivation for utility maximization by the DSS users would not in itself guarantee that DSS users would be capable of actually maximizing that utility. The DSS user would also need to be capable of persuading the other players to negotiate an agreement rather than opt out, i.e., convincing them of the Pareto-optimal nature of the mutually beneficial resolution involving agreement. This ability should translate itself into higher utility scores for the group as a whole as well as for the DSS user.

## 5.1. Research design

Undergraduate students in senior level political science courses at the University of Maryland with international negotiation as a major theme were recruited for participation in simulation exercises based on the Hostage Crisis (see Section 3.1 above). This allowed us to evaluate the impact of GENIE on students who would be more advanced in their negotiating skills and more aware of the international context of such negotiations.

The students were randomly assigned to either a DSS or non-DSS treatment. The non-DSS students were not told of the existence of the DSS. Both groups were informed that they would receive a cash payment based upon the number of utility points they earned in the negotiation. The DSS students received two hours of training and practice on GENIE. Non-DSS participants received written materials including all the information that forms the knowledge base for the DSS, and took part in a two hour training program detailing how this information could be used to calculate the utilities of different actions from different viewpoints.

At the end of training, the students in both groups took identical quizzes to test how well they could calculate the utility of certain outcomes. The quiz was designed to test the subjects' ability to calculate the utility of different actions in different situations for all three roles, the probability of success in a military operation and the expected utility of opting out. The scores of the two groups differed by only three percentage points. A one-tailed t-test resulted in a p-value of 0.355 allowing us to conclude that there was no significant difference between the two groups. In training situations free from the pressure of the negotiation process, non-DSS subjects and DSS subjects performed equally well when determining the utilities of specific outcomes.

In light of experimental findings that skilled negotiators in competition with other skilled negotiators do not necessarily achieve higher outcomes for themselves than do unskilled negotiators facing unskilled opponents, it was decided that only one DSS user would be assigned per experimental simulation. Pakistan was selected to be the DSS user in the experimental groups. Pakistan in this scenario is an interested third party which can play the role of mediator and is, therefore, significantly different from the other two roles. All of the non-DSS students were randomly assigned to their roles. Finally, after the experiment ended, the participants were each given a post-simulation questionnaire which asked questions about motivation, strategy and information usage during the simulation.

Fifty-seven students participated in preliminary experimental runs of the Hostage Crisis Simulation. They were divided into groups of three, with each group having one Indian official, one Pakistani official, and one Sikh hijacker. In ten of these groups, the Pakistani player was trained on use of the DSS and had access to it throughout the simulation (treatment group). In the remaining nine groups, none of the players had access to the DSS (control group). Non-DSS subjects in the treatment and control groups were not informed of the existence of the DSS.

## 5.2. Analysis

A set of interrelated propositions guided our experimental work:

1. DSS users are more likely than non-DSS users to identify utility maximization as their primary objective in a crisis negotiation situation.

The underlying assumption here is that the DSS enhances the ability of a decision maker to explore options and compare the utilities of different possible outcomes. Crisis decision makers, faced with large quantities of raw information and short decision time, can use a

Table 1  
Subject's negotiation goals

<table><tr><td></td><td>DSS user</td><td>Non-DSS</td></tr><tr><td>Maximize utility</td><td>2.3</td><td>3.6</td></tr><tr><td>1-tail t = 2.02 p = 0.061</td><td>SD = 0.9</td><td>SD = 1.7</td></tr><tr><td>Upholding principle</td><td>4.4</td><td>1.9</td></tr><tr><td>1-tail t = -3.62 p = 0.003</td><td>SD = 1.6</td><td>SD = 1.1</td></tr></table>

DSS to evaluate alternative outcomes, and thus improve their probability of achieving high utility scores. Non-DSS users, faced with the same mass of information and time constraints, may be unable to act as utility maximizers and will, instead, choose other, less objective and less quantifiable motivations.

One of the post-simulation questions asked participants to rank the motivations for their negotiation behaviour. Choices included maximizing their utility, upholding a principle, distrust of other players, and reaction to threats or incentives or positive statements by other players. It was found that DSS users were more strongly motivated by utility maximization than non-DSS users (t = 2.02, p = 0.061) (see Table 1). Non-DSS users tended to rank upholding principle more highly than DSS users (t = -3.62, p = 0.003).

Since individuals were randomly assigned to the treatment groups, one can conclude that the existence or non-existence of the DSS accounts for this difference in motivation. The non-DSS users appear to have been overwhelmed by the vast amount of information available to them and the difficulty of calculating the utility of different actions under the pressures of the negotiation. This inability to calculate their utility during the negotiation led them to irrationally rely upon deeply held principles even though they were being paid according to the number of utility points scored. The DSS user, aided by the analytical tools of the DSS, was able to calculate utilities quickly and efficiently and was, therefore, able to act as a utility maximizer.

## 2. DSS users will achieve higher utility scores than will non-DSS users.

Not only does access to the DSS encourage the actors to be motivated by utility maximization as a goal, but they will be more successful than their non-DSS counterparts in actually achieving higher utility scores as outcomes. However, as we will see below, the ability of the DSS user to achieve these higher scores depends to a large degree on the performance of its non-DSS crisis partners. As we see from Table 2, the Pakistani players who had access to the DSS tended on average to score higher than the Pakistani players in the control group. The average score for a Pakistani with access to the DSS was 599 (out of a possible 1000) while the average for a Pakistani without access to the DSS was only 471. Due to the relatively small sample size, these results are not significant, but they are in the predicted direction. A MANOVA with dependent variables score, utility maximization and upholding principle and independent variable DSS found that the DSS had an effect upon score at a p = 0.083 level.

## 3. Experiments in which there is a DSS user present will produce higher overall utility scores (across all three players) than experiments with no DSS user.

In addition to facilitating the achievement of a higher score for the individual DSS user, the existence of the DSS should ensure an overall better result for all three of the participants in the crisis simulation (i.e., the sum of the outcomes of all three crisis participants). Our assumption is that the DSS user will use his/her superior ability to project data and examine outcomes to subtly move the negotiation toward a mutually beneficial resolution, since that is the kind of situation in which the DSS user's own utility is maximized.

Table 2  
Utility scores

<table><tr><td>Simulation type</td><td>India</td><td>Pakistan</td><td>Sikh</td><td>Group</td></tr><tr><td>Experimental (DSS)</td><td>443</td><td>599.3</td><td>567.2</td><td>1609.8</td></tr><tr><td>n = 10</td><td>SD = 109.3</td><td>SD = 182.7</td><td>SD = 184.8</td><td>348.8</td></tr><tr><td>Control: (non-DSS)</td><td>454</td><td>470.9</td><td>472.9</td><td>1397.4</td></tr><tr><td>n = 9</td><td>SD = 120.4</td><td>SD = 281.1</td><td>SD = 222.5</td><td>SD = 471.8</td></tr><tr><td>1 tailed t-test</td><td>t = 0.2</td><td>t = -1.19</td><td>t = -1.01</td><td>t = -1.12</td></tr><tr><td></td><td>p = 0.43</td><td>p = 0.12</td><td>p = 0.16</td><td>p = 0.14</td></tr></table>

As a whole, the group tended to score higher when a Pakistani player with the use of the DSS was present (see the Group column in Table 2). When totalling the scores of all three players, groups in which there was no DSS user present scored on average 1397 (out of a possible 3000), while groups with a Pakistani player who utilized the DSS scored an average of 1610 points.

4. Experiments in which there is a DSS user present are more likely to end in agreement (as opposed to opting out) than are experiments with no DSS user. Since the achievement of an agreement among the crisis participants yields the highest mutual utility point total, and since use of the DSS facilitates the examination of utility maximization strategies, we should expect experiments with DSS users to achieve agreements more often than experiments with no DSS user. Participants in experiments in which Pakistan had access to the DSS tended to reach agreement more often than those in which none of the players had access to the DSS. Of the ten simulations with the DSS, seven ended in agreement and three ended with one of the parties initiating military action. Of the nine control simulations, four ended in agreement and five in military action. A difference of proportions test found that the two resulted in a p level of 0.121. Although the difference between our experimental and control group is not statistically significant at our small sample size, we do observe that a higher proposition of agreements occurred in DSS sessions. This could lead us to the conclusion that Pakistani use of the DSS aided all three players in reaching an agreement. This result is particularly interesting in light of the fact that in none of the experimental sessions did Pakistan chose to explicitly share concrete information about the utility of various actions for one or more of the players and none of the DSS users chose to overtly disclose their possession of the DSS.

## 5.3. Summary of experimental results

In all, these preliminary experiments support the conclusion that GENIE can help a negotiator to practice utility maximization. Although sufficient information and training was given to the non-DSS subjects to allow them to calculate utilities at the same level as DSS users, in a high pressure negotiation situation, DSS users were more capable of utility maximization.

Possession of the DSS by a self-interested third party aided that party in maximizing its own utility as well as in raising the utility of the group as a whole. On average, DSS users tended to achieve a higher utility rating than non-DSS participants. Additionally, with the aid of the DSS, the Pakistani player was better able to achieve an agreement among the players than was his/her non-DSS Pakistani counterpart. Even those participants who did not have the DSS, but who participated in a simulation where the Pakistani player had access to the DSS, tended as a group to score somewhat better than those in the control group. DSS users were more likely to list utility maximization as a strong motivation for their negotiating behaviour than non-DSS users who were more likely to rely upon deeply held principles. The complexity of information under the pressures of negotiation resulted in non-DSS users behaving irrationally and relying upon deeply held principles rather than maximizing their utility.

## 6. Conclusion

Ghiaseddin [13] provides an in-depth description of the characteristics of a successful DSS. Such a system should have the following functional capabilities: modelling, data management, and support of all decision making activities. In addition, he states that a DSS implementation should provide personalized support, security and integrity, transferability, and evolving capabilities for the support of increasingly complex demands. In this article, we have attempted to demonstrate that the use of the GENIE negotiation support system can aid crisis negotiators in identifying utility maximizing goals and in developing strategies to achieve these goals. In so doing, it meets the criteria which Ghiaseddin has discussed. $^{19}$ The features of GENIE as they relate to utility maximization were reviewed and a set of experiments testing its effectiveness in a controlled environment was presented. The features of GENIE do provide the user with a strong set of tools which aid in the search for utility maximizing goals and strategies. However, in a complex negotiating situation, this identification alone does not guarantee that the individual will be able to be successful in achieving utility maximization. The actions of the other negotiators affect the ability of the DSS supported negotiator to achieve his/her goals. Despite this fact, the experimental results show that the DSS users generally achieved higher utility scores, and groups in which DSS users participated achieved higher overall group scores.

## References

[1] S. Alter, 1980, Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley.

[2] S.J. Andriole, 1989, Handbook of Decision Support Systems, Tab Books Inc..

[3] I. Benbasat, G. DeSanctis, and B. Nault, 1993. Empirical research in managerial support systems: A review and assessment, In C.W. Holsapple and A.B. Whinston, editors, Recent Developments in Decision Support Systems, Springer-Verlag.

[4] K. Binmore, A. Rubinstein, and A. Wolinsky, 1986, The Nash bargaining solution in economic modelling, Rand Journal of Economics, 17(2):176–188.

[5] R. Brecht, R. Noel, and J. Wilkenfeld, 1984, Computer simulation in the teaching of translation and international studies, Foreign Language Annals, 17:6.

[6] T. Bui, 1992, Building DSS for negotiators: A three-step design process, IEEE, pages 164–173.

[7] J.D. Cooke, J.M. DeSantic and T.A. Peck III, 1989, The C-Scape Interface Management System Manual, Oakland Group Inc..

[8] J. Doyle, 1989, Reasoning, representation, and rational self-government, In Proc. of the 4th International Symposium on Methodologies for Intelligent Systems, pages 367–380.

[9] G.O. Faure and M.F. Shakun, 1988, Negotiating to free hostages: A challenge for negotiation support systems, In Evolutionary Systems Design: Policy Making under Complexity and Group Decision Support Systems, pages 219–245, Holden-Day.

[10] N.M. Fraser and K.W. Hipel, 1988, Negotiation support systems for conflict analysis, Managerial Decision Support Systems, pages 13–21.

[11] S. French, 1986, Decision Theory: An Introduction to the Mathematics of Rationality, Ellis Horwood Limited.

[12] V.S. Fumas, 1987, Strategy planning: Implications for the design of DSS, In C.W. Holsapple and A.B. Whiston, editors, Decision Support Systems: Theory and Application, pages 429–449, Springer-Verlag.

[13] N. Ghiaseddin, 1987, Characteristics of a successful DSS user's needs vs. builder's needs, In C.W. Holsapple and A.B. Whiston, editors, Decision Support Systems: Theory and Application, pages 159–184, Springer-Verlag.

[14] P. Gray, D. Vogel, and R. Beaulair, 1990, Assessing gdss empirical research, European Journal of Operational Research, 46:162–176.

[15] M. Harris, S. Kraus, J. Wilkenfeld and E. Blake, 1991, A decision support system for generalized negotiations, In Proceedings Thirteenth Annual Conference of the Cognitive Science Society, pages 382–387, Lawrence Erlbaum Associates.

[16] J. Hawgood and P. Humphreys, editors, 1987, Effective Decision Support Systems, The Technical Press.

[17] O.R. Holsti, 1989, Crisis decision making, In P.E. Tetlock, J.L. Husbands, R. Jervis, P.C. Stern, and C. Tilly, editors, Behaviour, Society and Nuclear War, pages 8–84, Oxford University Press.

[18] M. Jarke, M. Jelassi and M. Shakun, 1987, Mediator: Towards a negotiation support system, European Journal of Operational Research, 31:314–334.

[19] M.T. Jelassi and A. Foroughi, 1989, Negotiation support systems: An overview of design issues and existing software, Decision Support Systems, 5:167–181.

[20] L. Jessup and D. Tansik, 1991, Decision making in an automated environment: The effect of anonymity and proximity with a group decision support system, Decision Sciences, 22:266–279.

[21] G. Kersten, 1985, Nego: Group decision support system, Information and Management, 8:237–246.

[22] S. Kraus and J. Wilkenfeld, 1990, An automated strategic model of negotiation, In Proceedings of AAAI-90 Workshop on Reasoning in Adversarial Domains, Boston.

[23] S. Kraus and J. Wilkenfeld, 1990, Modelling a hostage crisis: Formalizing the negotiation process, Technical Re-

port UMIACS TR 90-19 CS TR 2406, Institute for Advanced Computer Studies, University of Maryland.

[24] S. Kraus and J. Wilkenfeld, 1991, Negotiations over time in a multi agent environment: Preliminary report. In Proc. of IJCAI-91, Australia, To appear.

[25] S. Kraus and J. Wilkenfeld, 1993, A strategic negotiations model with applications to an international crisis, IEEE Transaction on Systems Man and Cybernetics, 23(1):313–323.

[26] S. Kraus and J. Wilkenfeld, 1993, The updating of beliefs in negotiations under time constraints with uncertainty. In Proc. of IJCAI93 Workshop on Artificial Economics, pages 57–68, Also presented in BISFAI93.

[27] S. Kraus, J. Wilkenfeld, and G. Zlotkin, 1994, Multiagent negotiation under time constraints, Artificial Intelligence Journal, In Press.

[28] S. Matwin, S. Szpakowicz, Z. Koperczak, G.E. Kersten and W. Michalowski, 1989, Negoplan: An expert system shell for negotiation support, IEEE Expert, 4(4):50–62.

[29] W. Michalowski, G.E. Kersten, Z. Koperczak, S. Matwin and S. Szpakowicz, 1988. Negotiating with a terrorist: Can an expert system help? In M.G. Singh, K.S. Hindi, and D. Salassa, editors, Managerial Decision Support Systems, pages 193–200, North-Holland.

[30] T. Moehlman, V. Lesser and B. Buteau, 1992, Decentralized negotiation: An approach to the distributed planning problem, Group Decision and Negotiation, 2:161-191.

[31] S.S. Nagel, 1992, Applications of Decision-Aiding Software, St. Martin's Press.

[32] R. Noel, D. Crookall, J. Wilkenfeld and L. Schapira, 1987, Network gaming: A vehicle for intercultural communications, In D. Crookall, C. Greenblat, A. Coote, J. Klabbers, and D. Watson, editors, Proceedings of the International Simulation and Gaming Association, Pergamon Press, Oxford.

[33] M. Poole, M. Holmes and G. Desanctis, 1991, Conflict management in a computer-supported meeting environment, Management Science, 37(8):926–953.

[34] W. Pracht, 1990, Model visualization: Graphical support for DSS problem structuring and knowledge organization, Decision Support Systems, 6:13–27.

[35] H. Raiffa, 1982, The Art and Science of Negotiation, Harvard University Press.

[36] A. Rubinstein, 1982, Perfect equilibrium in a bargaining model, Econometrica, 50(1):97–109.

[37] D.K. Samarasan, 1993. Analysis, modelling and the management of international negotiations, Theory and Decision, 34:275–291.

[38] R. Selten, 1975, Re-examination of the perfectness concept for equilibrium points in extensive games, International Journal of Game Theory, 4:25–55.

[39] A. Shaked and J. Sutton, 1984. Involuntary unemployment as a perfect equilibrium in a bargaining model, Econometrica, 52(6):1351–1364.

[40] B. Shneiderman, 1992, Designing the User Interface: Strategies for Effective Human-Computer Interaction, Addison Wesley.

[41] H.G. Sol and J. Vecsenyi, editors, 1990, Environments for Supporting Decision Processes, North-Holland.

[42] B.I. Spector, 1993, Decision analysis for practical negotiation application, Theory and Decision, 34:183–199.

[43] K.P. Sycara, 1993, Machine learning for intelligent support of conflict resolution, Decision Support Systems, 10:121–136.

[44] C.E. Thompson, 1989, Decision Support Systems: A Bibliography, 1980-1984, volume 1745 of Public Administration Series, Vance Bibliographies.

[45] J. Wessels and A.P. Wierzbicki, editors, 1991, User-Oriented Methodology and Techniques of Decision Analysis and Support, Springer-Verlag.

[46] A.P. Wierzbicki, L. Krus and M. Makowski, 1993, The role of multi-objective optimization in negotiation and mediation support, Theory and Decision, 34:201–214.

[47] J. Wilkenfeld, 1983, Computer-assisted international studies, Teaching Political Science, page 10.

[48] J. Wilkenfeld, M. Brecher and S. Moser, 1988, Crises in the Twentieth Century: Handbook of Foreign Policy Crises, Oxford: Pergamon Press.

[49] J. Wilkenfeld and J. Kaufman, 1993, Political science: Network simulation in international politics, Social Science Computer Review, 11:464–476.

![](/api/attachments/27GJX42A/fulltext/images/73516e1800352c49886d9a464541901c4c593b9c288f435e60d658571b587e6f.jpg)

Jonathan Wilkenfeld is Professor and Chair of the Department of Government and Politics at the University of Maryland at College Park. He received his Ph.D. in political science from Indiana University in 1969. He is a specialist in foreign policy decision making and the analysis of international crisis. In recent years, his work has focused on the development of simulations of international negotiation for both teaching and research

purposes. He and Sarit Kraus are currently principal investigators on a National Science Foundation grant for the development of automated negotiators in multi-agent environments.

![](/api/attachments/27GJX42A/fulltext/images/b652d5fa6662b89890c81ff9bca801af98222dd29e01d691bf6f184473303c94.jpg)

Sarit Kraus is a Senior Lecturer in the Department of Mathematics and Computer Science, Bar Ilan University, Ramat Gan, Israel and Adjunct Assistant Professor at the Institute for Advanced Computer Studies, University of Maryland, College Park. Her research interests include the Development of Intelligent Systems, Distributed AI, Automated Negotiation, Planning, User Interfaces and Decision Support Tools. Kraus received

her Ph.D. in Computer Science from the Hebrew University of Jerusalem in 1989. Her dissertation was titled: 'Planning and Communication in a Multi Agent Environment'. After completing her doctorate, she spent two years at the University of Maryland at College Park before joining Bar-Ilan University.

![](/api/attachments/27GJX42A/fulltext/images/06898d70c50450cb0f68bb92be827d2524b759a27d251c95976343b442f4db53.jpg)

Kim Holley received her B.S. in Mathematics, Computer Science and Philosophy from Ashland University and her M.A. in International Peace Studies from the University of Notre Dame. She is now a doctoral student in Government and Politics at the University of Maryland, College Park where her research focuses on conflict resolution and negotiation with a special interest in the role which technology can play in the resolution of

international and communal conflict.

Michael Harris received his B.S. degree in Mathematics and Computer Science from the University of Maryland at College Park, and an M.A. in applied Mathematics from UMCP in 1991. Currently, he is working in the field of computer simulation and modelling.
