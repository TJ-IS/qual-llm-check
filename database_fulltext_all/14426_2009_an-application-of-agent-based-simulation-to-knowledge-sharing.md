---
otero_id: 14426
otero_key: "BC95JH9R"
title: "An application of agent-based simulation to knowledge sharing"
authors: "Jing Wang; Kholekile Gwebu; Murali Shanker; Marvin D. Troutt"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An application of agent-based simulation to knowledge sharing

Jing Wang <sup>a</sup>, Kholekile Gwebu <sup>a</sup>, Murali Shanker <sup>b</sup>, Marvin D. Troutt <sup>b,</sup>⁎

<sup>a</sup> Decision Sciences Department, Whittemore School of Business and Economics, University of New Hampshire, United States

<sup>b</sup> Department of Management & Information Systems, College of Business, Kent State University, United States

## a r t i c l e i n f o

Article history: Received 31 July 2006 Received in revised form 12 September 2008 Accepted 28 September 2008 Available online 12 October 2008

Keywords: Agent-based modelling Simulation Knowledge sharing Complex adaptive systems

## a b s t r a c t

This paper explores knowledge sharing using an agent-based simulation model. Built using Repast, our application allows managers to simulate employee knowledge-sharing behaviors by making parametric assumptions on employee decision strategies and organizational interventions that affect identi<sup>fi</sup>ability, bene<sup>fi</sup>ts, and costs. Our results show that in the presence of non-linear and adaptive interaction, unintended and unpredictable outcomes might occur, and that knowledge sharing results from the complex interaction between employee behavior and organizational interventions.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

Knowledge constitutes a key strategic resource for <sup>fi</sup>rms [23,33,48], and companies invest heavily to facilitate the exchange of knowledge among employees. However, organizations often face dif<sup>fi</sup>culties when trying to encourage knowledge-sharing behaviors [9,12]. This raises the issue of how organizations can effectively encourage individual knowledge-sharing behavior.

Many systems in the business domain fall into the category of a complex adaptive system. Complex Adaptive Systems (CAS) are de<sup>fi</sup>ned as dynamic systems consisting of a network of interacting actors like humans, processes, etc., that adapt to constantly changing environments [29]. For example, many economic systems are complex because 1) they are made of a network of interacting actors (humans, processes, environment, etc.) and 2) they reveal dynamic, collective behavior that emerges from the individual actors' activities. These systems are also adaptive because they contain actors who achieve their goals by adapting to the environment over time [29].

Similarly, examining the effect of a <sup>fi</sup>rm's objectives and individual employee actions on organizational knowledge sharing is a complex system. By considering individual employees (actors) and their interactions, knowledge sharing emerges not only from the interplay between the intervention (contextual environment) and the employees, but also from the complex interactions among individual employees who hold that knowledge. Conceptualizing organizational knowledge sharing as a complex adaptive system has important implications for managers and researchers alike. It suggests that the essence of knowledge sharing is not just what organizations plan, but also what individuals do. This perspective challenges the traditional management approach of planning and control, and acknowledges that sharing knowledge involves activities that can neither be supervised nor forced on people [35], and that the availability of sophisticated technologies does not guarantee success in knowledge management initiatives [9].

One problem with modeling complex adaptive systems such as knowledge sharing is that non-linear and adaptive interactions in these systems are often too complex to be captured by traditional analytical techniques [29,4]. Many conventional models are also limited in their ability to capture cross-level impacts. Currently, twoby-two game settings dominate the modeling of CAS as they allow results by deduction [4], and they are tractable [44]. However, such approaches make limiting assumptions on interdependencies, strategies, and on the multiplicity of players, which contradict real-life situations [44]. Further, game theory assumes rational choices or optimization principles. In reality, individuals are adaptive, rather than fully rational, and they lack the necessary behavioral sophistication to derive optimal solutions [29].

Recent advances in agent-based simulation offer new opportunities to examine complex systems like organizational knowledge sharing. With intelligent agents as its building blocks, an agent-based simulation approach naturally accommodates such systems by modeling actors and components as software agents. As a wide range of computer-based algorithms can be adopted, interaction and adaptive behavior can also be easily modeled.

In this paper, we use an agent-based simulation model to get a better understanding of how employees' actions, and organizational interventions that affect the costs of not sharing knowledge, the benefits of sharing knowledge, and a <sup>fi</sup>rm's ability to determine whether or not an employee has shared knowledge (identifiability), interact to in<sup>fl</sup>uence organizational knowledge sharing. Our objective is twofold: We <sup>fi</sup>rst build a simulation model to demonstrate the importance and feasibility of using an agent-based simulation approach to model knowledge sharing, and secondly, to demonstrate that the agentbased approach and other techniques such as data mining can be combined to develop potent management analysis tools to study organizational knowledge sharing.

The remainder of this paper is structured as follows. The next section provides a brief overview of organizational knowledge sharing, and agent-based modeling. In the following section, we develop an agent-based simulation model for knowledge sharing. This is followed by the results section, which shows that knowledge sharing results from the complex interaction between organizational objectives and employee actions. The last section presents our conclusion.

## 2. Related research

## 2.1. Organizational knowledge sharing

Shared knowledge is a particular case of a public good [9], where every user bene<sup>fi</sup>ts from it, regardless of their contribution, and the knowledge does not diminish with use [37,42]. But, individuals may not contribute, particularly when there is little penalty for not contributing. From an individual's perspective, it is rational to not contribute. But, if all individuals act rationally and do not contribute, the public good ceases to exist, and ultimately all individuals are worse off. In other words, individual rationality leads to collective irrationality, a dilemma that could arise in organizational knowledge sharing.

Thus, if organizations are to bene<sup>fi</sup>t, it is important for them to understand how different interventions affect knowledge sharing. Some approaches include providing incentives for sharing knowledge, and the use of knowledge management systems [24,18,16]. These mechanisms affect knowledge sharing by impacting the benefits of sharing and costs of not sharing. Favorable bene<sup>fi</sup>ts for sharing, and higher costs for not sharing, are likely to improve knowledge-sharing behaviors [24,18,15]. As knowledge sharing comes with participation costs, e.g., time, effort, power, and money, reducing these costs is likely to encourage knowledge sharing behaviors [9]. Knowledge management systems can be embedded seamlessly in employees' work <sup>fl</sup>ow to reduce such costs. Finally, for incentives to work, organizations must be able to identify between those who share and those who do not share knowledge. When an individual's anonymity is preserved, and no record of past interaction exists, there is a strong incentive for them to not contribute, as they can bene<sup>fi</sup>t from knowledge shared by others, but not be penalized for not contributing [4,37,5]. Therefore, increasing identifiability and disseminating information about individuals' actions is another important intervention to facilitate knowledge sharing. Conversely, an approach such as pay-for-performance may discourage knowledge sharing among employees, as it reinforces the belief that knowledge is valuable, and sharing it dilutes their accomplishments [9,30].

Despite organizational interventions, knowledge sharing cannot be forced onto people [27,9]. Researchers have realized that organizational knowledge sharing is a complex product of an individual's behavior in a given organizational and social situation [9]. The premise of knowledge sharing as the product of complex people-situation interaction suggests that a complete understanding of organizational knowledge sharing will necessarily involve not only individuals who hold the knowledge, but also understanding organizational interventions that facilitate knowledge sharing, and the way in which each of these components interacts with the others. This complex and interactive nature of knowledge sharing suggests that this phenomenon is a complex adaptive system [29].

The next section provides a brief review of agent-based simulation and its advantages in modeling CAS.

## 2.2. Agent-based modeling and simulation for business problems

A software agent is a computer program that is situated in some environment and is capable of autonomous action in this environment in order to meet its design objectives [51]. Agents possess four distinct characteristics [52]: Autonomy, which is the ability to operate without direct human intervention, interactivity, the ability to interact, communicate, and cooperate with other agents, reactivity, the ability to monitor and respond to changes in the environment in which they reside, and, proactiveness, which is the ability to take initiatives when necessary and exhibit goal-oriented or opportunistic behavior.

Agent-based modeling has become an increasingly attractive methodology in modeling various social and natural complex systems [4,43,17,45,14,50]. Several factors have contributed to the growing popularity of such models. A few of them being:

• They allow researchers to model CAS in a straightforward manner. Individual actors or components in real-world systems are modeled as software agents. Instructions are de<sup>fi</sup>ned for the behavior and interaction of the individual actor of a particular real-world system. No instructions are speci<sup>fi</sup>ed for the overall behavior of the studied system. Instead, the overall behavior emerges as a result of the interactions and actions of the individual agents representing the actors in the real system [4,17].

• They retain much of the <sup>fl</sup>exibility of linguistic modeling and the consistency and precision of the mathematical modeling techniques [29].

• They provide an alternative approach to model and incorporate a wide range of computer-based adaptive algorithms and thereby, provide a viable way to study systems with actors who are adaptive rather than fully rational [29,4].

• They have the ability to produce emergent results [4,29,43]. In the literature, emergent phenomena refer to outcomes arising at the level of the aggregate system that may not be foreseen by examining the elements of the system in isolation [43]. For example, when we study the structure of market share of a product, software agents can be constructed to model each individual customer's purchasing behavior. It is not self-evident how market share of this product would change by simply examining individual agents. However, patterns might emerge at the system level by running the simulation over a period of time.

In certain cases, analysis of the dynamic paths of the system may be of vital relevance to decision makers. For instance, in the resourcebased view of the <sup>fi</sup>rm, <sup>fi</sup>rms differ in their resource endowments and capabilities in important and durable ways, and this heterogeneity of <sup>fi</sup>rm capabilities and resources affect their competitive advantage and disadvantage [7,28]. If heterogeneity in <sup>fi</sup>rm resources and capabilities is so crucial, decision makers would probably be particularly interested in the path of how <sup>fi</sup>rm heterogeneity arises and evolves over time. Agent-based models can be used to analyze the path of the system within any timeframe. When an agent-based model is executed in a simulation, the unfolding behavior of the individual agents and the aggregate system can also be observed over time. Elements such as utility, risk aversion, available information, knowledge, and learning can be carefully and easily controlled. Through successive runs of the computer simulation, these elements can be reset to different values in order to study variations in outcome. The strategies of each individual agent and the resultant outcomes can be analyzed in great detail [29]. Parameter values can be manipulated to study how the path of the system reacts in response to exogenous shocks [43].

Further, agent-based simulation provides several advantages over other simulation architectures in modeling business problems. First, an agent is autonomous, pro-active, adaptive, socially interactive, and intelligently cooperative [32,34]. With agents as its building blocks, an agent-based simulation system can therefore offer sophisticated patterns of interaction [32] and additional automation and <sup>fl</sup>exibility [2,49]. Secondly, a multi-agent system (MAS) is well suited particularly for domains where multiple perspectives, goals, interactions or entities (such as different people and organizations) are involved [32,49]. Different or even con<sup>fl</sup>icting interests of parties can be modeled and ensured by different agents in the MAS. Finally, because agents are socially interactive, MAS are ideal for modeling fundamental problems where interaction, interdependency, emergence, and con<sup>fl</sup>icting interests are essential.

Bene<sup>fi</sup>ts and costs structure

<table><tr><td rowspan="2">Person (C)</td><td rowspan="2">Identity(I)</td><td colspan="2">Benefits</td><td colspan="2">Costs</td></tr><tr><td>Benefits from shared knowledge(R)</td><td>Incentives for contributing knowledge(S)</td><td>Penalty for not contributing(Q)</td><td>Costs for sharing knowledge and enforcing penalties on non-contributors(P)</td></tr><tr><td rowspan="2">Contributor</td><td>Known</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Not known</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td rowspan="2">Non-contributor</td><td>Known</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Not known</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr></table>

Note: Variable names are in parentheses.

The next section presents an agent-based simulation model for organizational knowledge sharing.

## 3. Model development

As discussed previously, both organizational interventions and individual employee behaviors affect knowledge sharing. Organizational interventions provide incentives and penalties that affect the benefits of sharing and costs of not sharing, respectively. To effectively apply such interventions, organizations must also be able to identify individuals who share or do not share knowledge. Thus, in our model, we consider interventions that affect: 1) Identity Transparency, which re<sup>fl</sup>ects the degree to which organizations are successful in identifying employees who share knowledge or not. Higher values indicate that the organization is able to identify a greater proportion of such employees. 2) Benefits of sharing, which provide incentives for contributing knowledge and gains from shared knowledge and 3) Costs of not sharing, which include interventions for not contributing knowledge and costs in enforcing penalties on non-contributors.

Just as organizations adopt different interventions to improve knowledge sharing, individuals may adopt different strategies to decide if they will or will not share knowledge [29,4]. In other words, these strategies determine the action, to share or to not share, for each individual. The agent-based simulation model developed below then examines the effect of both organization interventions and employee strategies on knowledge sharing. While our primary objective here is to examine how organizations can understand and increase knowledge sharing, we do not necessarily examine all decision strategies or organizational interventions that may in<sup>fl</sup>uence such behavior. Here, we restrict our attention to the above mentioned organizational interventions, and decision strategies that are commonly mentioned in the literature [4,9,29,37,24,18,5,46,6,40,19]. The next section presents our model description.

## 3.1. Model description

Based on our discussions above, Table 1 summarizes the variables affected by organizational interventions that we consider in our model: identity transparency, benefits, and costs.

All individuals bene<sup>fi</sup>t from the knowledge shared by others, but only those individuals who contribute knowledge and have their identities known bene<sup>fi</sup>t from the incentives given by the organization for knowledge sharing (Table 1). Individuals also incur costs. Those who contribute knowledge spend time and effort in sharing knowledge [9]. Prior work in social dilemmas indicates that those who contribute tend to punish non-contributive behavior even if the punishment is costly for them [37,19]. As such, contributors also incur costs to enforce penalties on non-contributors. Non-contributors bene<sup>fi</sup>t from the contribution of others, but incur costs for failing to contribute, but only if their identities are known. In our model, we do not assume complete transparency of players' identities. In fact, ambiguity of player identity is one of the features that distinguish a two-person game from an n-person public good dilemma. In a twoperson game, when one player defects, the other one knows who defected. But, as the number of players increases in a game, it gets easier to defect anonymously [37].

To fully understand knowledge sharing also requires consideration of individuals who hold the knowledge. At each decision point, an individual's problem is to choose an action, to contribute or not contribute, based on the information available to him. Based on prior research, Table 2 presents possible strategies employees may adopt when choosing their knowledge sharing actions.

At each decision point, individuals must determine whether or not to contribute knowledge. Regardless of their own or other individuals' past actions, individuals choosing the contribute and do not contribute strategies always take the same action. That is, they either contribute, or do not contribute knowledge, respectively. Individuals who use the repeat last action strategy take the same action, either to contribute or not contribute, that they did in their immediate previous decision. Some decision strategies require information from other individuals. For example, the mimic majority strategy requires knowledge of the actions of other individuals in the organization. As an individual's identity may not be known, this strategy re<sup>fl</sup>ects the perceived majority decision. That is, the action supported by the majority of known individuals.

While rational individuals seek to optimize gain, most of them lack the necessary skills, knowledge, and information to do so [29,4]. Hence, here we offer a mimic winners strategy, where agents learn from the winners to determine which action yields better bene<sup>fi</sup>ts, and a learn from past strategy, where agent learn from their own experience to determine which action yields better bene<sup>fi</sup>ts (Table 2). Clearly, not all individuals act rationally. Some adopt a herd mentality (mimic majority strategy in Table 2) and imitate the decisions of individuals around them [23,35,4]. A single individual may also change strategies over time, which may result in different actions. In our model, agents follow a non-persistent strategy. That is, at each decision point, agents are randomly assigned with one decision strategy from the possible strategies in Table 2.

The learn from the past and mimic winners strategies require calculating an individual's net bene<sup>fi</sup>t. All individuals bene<sup>fi</sup>t from shared knowledge (Table 1). If individual K is a non-contributor, then this shared-knowledge bene<sup>fi</sup>t is derived from the contribution of all contributors. But, if individual K is a contributor, then this sharedknowledge bene<sup>fi</sup>t is derived only from the contribution of other individual contributors. If their identities are known, contributors also bene<sup>fi</sup>t from the incentive S given by the organization. Costs for contributors arise from the time and effort required to share knowledge and to penalize non-contributors, while the costs for known non-contributors is the penalty enforced by the contributors and the organization. Individuals using the learn from the past strategy compare their net bene<sup>fi</sup>t for the last two decision points, and use the decision that led to the higher net bene<sup>fi</sup>t. For example, let individual i's decisions at point t−1 and t result in a net payoff of $B _ { t - 1 }$ and $B _ { t } ,$ respectively. At decision point t+1, using the learn from the past strategy, individual i will choose the same decision as at time t if $B _ { t } { \geq } B _ { t }$ . Otherwise, individual i will choose the decision made at $t - 1$ For the bene<sup>fi</sup>ts and costs structure of our model (Table 1), the net bene<sup>fi</sup>t $B _ { K }$ for individual K can therefore be expressed as follows:

Individual decision strategies on whether to contribute or not contribute

<table><tr><td>Strategy</td><td>Description</td></tr><tr><td>Contribute</td><td>Individuals share their knowledge regardless of their own or other individuals&#x27; previous actions</td></tr><tr><td>Do not contribute</td><td>Individuals do not share their knowledge regardless of their own or other individuals&#x27; previous actions</td></tr><tr><td>Repeat last action</td><td>Individuals choose the same action that they did previously</td></tr><tr><td>Mimic majority</td><td>Individuals imitate the actions used by the perceived majority of individuals</td></tr><tr><td>Learn from the past</td><td>Individuals compare their last two actions, and choose the one that led to a higher net benefit</td></tr><tr><td>Mimic winners</td><td>A strategy designed to imitate individuals who try to maximize their payoff. It uses data collected from all known agents in determining the best payoff</td></tr></table>

$$
\begin{array}{l} B _ {k} = \text { Benefit } - \text { Cost } \\ = \left\{ \begin{array}{l l} \left(R \times \sum_ {i, i \neq K} C _ {i} + S \times I _ {K}\right) - P & \text { if   individual   } K \text {   is   a   contributor } \\ \left(R \times \sum_ {i, i \neq K} C _ {i}\right) - (Q \times I _ {K}) & \text { if   individual   } K \text {   is   a   non   -   contributor } \end{array} \right., \end{array}\tag{1}
$$

where

R Bene<sup>fi</sup>t derived from an individual's shared knowledge

$S$ Incentive given by the organization for sharing knowledge

C 1 if individual i is a contributor

$$
C _ {i}
$$

i 0 otherwise

$P$ Cost for an individual contributor to share knowledge and enforce penalties on non-contributor

$Q$ Cost incurred by a non-contributor for not sharing knowledge 1 if identity of individual i is known $I _ { i }$ 0 otherwise

The mimic winners strategy involves calculating net bene<sup>fi</sup>ts for all agents whose identities are known. To make the next decision, we <sup>fi</sup>rst identify all known agents. The net payoff for each known agent is then calculated using Eq. (1). We then determine the average net bene<sup>fi</sup>t ${ \bar { B } } ^ { 1 }$ for all agents who are contributors, and ${ \bar { B } } ^ { 0 }$ for all agents who are noncontributors, respectively. Using the mimic winners strategy, an individual's action would be to contribute $\mathrm { i f } \ \overline { { B } } ^ { 1 } \geq \overline { { B } } ^ { 0 } ,$ , otherwise it is to not contribute. As we do not require complete identity transparency in our model, the average bene<sup>fi</sup>t can only be determined for agents whose identities are known.

Our model allows the <sup>fl</sup>exibility to include other organizationalspeci<sup>fi</sup>c interventions and decision strategies. Here, we restrict our implementation to the ones mentioned above. The next section presents the simulation model.

## 3.2. The simulation model

The Recursive Porous Agent Simulation Toolkit (Repast) is an open source modeling framework that permits researchers to create agent-based simulations [41]. Although Repast was originally developed to simulate social behavior, it has been successfully employed by a myriad of researchers in <sup>fi</sup>elds as diverse as political science [13], archeology [11], biology [3], economics [8] and <sup>fi</sup>nance [10] just to name a few. The popularity of Repast may be attributed to its vast library of objects that provide researchers in different <sup>fi</sup>elds the <sup>fl</sup>exibility to create sophisticated models then run and display the results of agent-based simulations. Repast is well suited for social networks and interactions, and is used to build our model. Fig. 1 shows a representative graphical user interface (GUI) of our application.

![](/api/attachments/BC95JH9R/fulltext/images/42de17329ece3aa0158fe3422ce13080e9325df2524f7adab61785986c9a8bc7.jpg)  
Fig. 1. Parameter inputs.

Table 3  
Experimental factors

<table><tr><td>Factor</td><td>Factor levels</td></tr><tr><td>Number of individuals (N)</td><td>300</td></tr><tr><td>Initial percentage of contributors</td><td>50%</td></tr><tr><td>Identity transparency (I)</td><td>50%</td></tr><tr><td></td><td>90%</td></tr><tr><td colspan="2">Costs</td></tr><tr><td>Cost for sharing knowledge and enforcing penalties</td><td>3</td></tr><tr><td>on non contributors (P)</td><td>5</td></tr><tr><td>Cost for not contributing (Q)</td><td>2</td></tr><tr><td></td><td>4</td></tr><tr><td colspan="2">Benefits</td></tr><tr><td>Incentive for contributing (S)</td><td>3</td></tr><tr><td></td><td>5</td></tr><tr><td>Benefit from contributed knowledge (R)</td><td>0</td></tr><tr><td></td><td>1</td></tr><tr><td></td><td>2</td></tr><tr><td></td><td>4</td></tr><tr><td></td><td>8</td></tr><tr><td></td><td>12</td></tr></table>

Fig. 1 shows the user interface for specifying the initial conditions of the simulation, which include the number of employees in the organization, and the initial percentage of individuals in the organization who start out as non-contributors. The run time conditions of the simulation can be speci<sup>fi</sup>ed by clicking on the drop down menu Run. By clicking on the Strategy Mix in Fig. 1, a different GUI is presented to specify the strategy mix that we outlined in Table 2. A similar GUI allows the user to specify the organizational interventions of identity transparency, benefits, and costs of Table 1.

## 4. Simulation experiment

A simulation experiment was designed to understand the long-term effect on knowledge sharing of three categories of variables affected by organizational interventions (Table 1) and six decision strategies (Table 2).

Before a simulation can be executed, it is important to verify and validate the model. Verification ensures that the simulation model is correctly coded, and the program performs as intended [39]. Our primary means of veri<sup>fi</sup>cation here is through tracing. Tracing is a type of dynamic testing that involves getting all intermediate outputs from a computer program automatically. This output is then compared with results calculated manually by the analyst [36]. In our simulation experiments, intermediate simulation outputs matched our manual calculations, thus supporting the veri<sup>fi</sup>cation of our model.

Before any simulation model can be used in an organization, it is important to validate the model for that organization. That is, it is important to ensure that the model is an accurate representation of the real-world system under study [39]. Here, it would require that we collect data on the input parameters, i.e., the bene<sup>fi</sup>ts and costs, and also the decision strategies used by different groups of individuals in the organization. The outputs of the simulation model can then be validated with the actual observations from the organization.

As our primary objective here is to understand knowledge sharing using agent-based simulation and not necessarily to validate it for a particular organization, the input data in our simulation experiments are arti<sup>fi</sup>cially generated. But, we discuss validation of our simulation results as part of our analysis in the following sections.

Our simulation experiment consisted of the following factors:

1. Initial conditions

a. Number of individuals (N)

b. Percentage of individuals who start out as non-contributors

2. Identity transparency (I)

3. Costs

a. Cost of sharing knowledge and enforcing penalties on noncontributors (P)

b. Cost of not contributing (Q)

4. Bene<sup>fi</sup>ts

a. Incentive given for contributing (S)

b. Bene<sup>fi</sup>t from contributed knowledge (R)

## 5. Decision strategy mix

Factors 1a and 1b specify the initial conditions of the simulation. For this research, we consider a medium size organization and <sup>fi</sup>x the value of N at 300. As we are interested in the long-run behavior of the system, factor 1b only affects the convergence rate to long-term behavior. As this factor largely affects only the computational time required to initialize initial conditions, without loss of generality, we <sup>fi</sup>x this value at 50% for all simulations. We then choose a conservative time to initialize initial conditions. Factor 2 is the proportion of individuals whose identity is known, and we consider this at two levels. Factors 3 and 4 de<sup>fi</sup>ne the costs and bene<sup>fi</sup>ts that we discussed inTable 1. We consider each of these factors at 2 levels, except for R, the bene<sup>fi</sup>t from contributed knowledge. Initial experiments suggested that the model was sensitive to values of R, so we consider this factor at 6 levels. The values of other factors were so chosen as to provide different ratios of bene<sup>fi</sup>ts to costs in our model (Table 3). The last factor, decision strategy mix, itself consists of a number of variables that can be changed (Table 4). In our model, to assign a strategy mix, we group individuals into two categories, those whose net payoff is currently non-negative, and those whose net payoff is negative. We then assign a strategy mix for each group. For an organization, this requires data collection on decision strategy mixes for each identi<sup>fi</sup>ed group in the organization. Here, we only consider a <sup>fi</sup>xed mix for the two identi<sup>fi</sup>ed groups in our model. The percentage of individuals in each group who follow a speci<sup>fi</sup>c strategy is shown in Table 4.

The values for repeat last action and learn from the past require further mention. Individuals who currently have a negative net bene<sup>fi</sup>t are unlikely to adopt as their current decision their immediate previous decision that led to a negative net bene<sup>fi</sup>t. Such individuals are more likely to look beyond their last decision, and choose the one that yielded a higher payoff in their previous decisions. In other words, individuals currently with a negative net bene<sup>fi</sup>t are more likely to use a learn from the past strategy than repeat last action, which resulted in their negative payoff. This is re<sup>fl</sup>ected in our strategy mix in Table 4, though our model allows us the <sup>fl</sup>exibility to consider other values. Thus, our simulation experiment consists of 96 treatments. The complete set of factors and their levels for our simulation is shown in Tables 3 and 4.

As we are interested in the long-run behavior of the system, we needed to initialize initial-condition statistics during the simulation. To facilitate this, our application generates three major outputs: 1) a visual display of agents playing the game, 2) a report that tracks variable values, and 3) a line chart that visually exhibits the trend (the number of contributors and non-contributors) over time. To identify initial conditions, we visually identi<sup>fi</sup>ed when the simulation appears to reach steady state behavior, and then initialized statistical counters at that time instant [39]. As steady state cannot be guaranteed for all parameter values in our simulation, we use a conservative value for initial conditions as part of the initialization of statistical counters. Fig. 2 shows an example graph of the number of contributors and noncontributors in our simulation. The vertical line indicates an approximate point at which statistical counters were initialized. Our simulation experiment consisted of 96 treatments. For each treatment combination, the simulation was run until the statistical counters

Table 4  
Percentage mix of strategies for each group

<table><tr><td>Decision strategy</td><td>Non-negative net benefit (%)</td><td>Negative net benefit (%)</td></tr><tr><td>Contribute</td><td>1</td><td>1</td></tr><tr><td>Do not contribute</td><td>1</td><td>1</td></tr><tr><td>Repeat last action</td><td>32</td><td>0</td></tr><tr><td>Mimic majority</td><td>33</td><td>33</td></tr><tr><td>Learn from the past</td><td>0</td><td>33</td></tr><tr><td>Mimic winners</td><td>33</td><td>32</td></tr></table>

Notes:

![](/api/attachments/BC95JH9R/fulltext/images/1cade43e3120f55fea52a239ef025d95968fd7ac384c69bfb1258c66e04dfc1a.jpg)  
Fig. 2. Identifying initial conditions.

were initialized for initial-conditions, and then the simulation continued until we had collected data over 1000 decision points. The average value over these 1000 decision points represented one sample point in our analysis. This procedure was then independently repeated 10 times for each treatment combination. Thus, over the course of the simulation, we collected a total of 960 independent samples. The results in the following sections are based on these 960 sample values.

## 5. Results

Organizations are interested in understanding how different factors affect knowledge sharing. To facilitate this, our simulation model provides detailed output that allows an organization to observe how changes in input parameters affect knowledge sharing over time.

Here we concentrate on the outputs of the simulation. Table 5 presents the average proportion of non-contributors at each factor level across the 960 independent samples. As this was a balanced design, each factor level average, except for R, is calculated from n=480 sample points. As there are six levels of R, factor level averages are calculated from n=160 sample points. The total number of individuals was <sup>fi</sup>xed at N=300.

Average proportion of non-contributors; standard deviation in ()

<table><tr><td>Factor</td><td></td><td>Factor levels</td></tr><tr><td rowspan="2">Identity transparency $(F=7.38, p=.0067)^{1}$ </td><td>I=50%</td><td>.5114 (.4260)</td></tr><tr><td>I=90%</td><td>.4771 (.4448)</td></tr><tr><td colspan="3">Costs</td></tr><tr><td rowspan="2">Cost for sharing knowledge and enforcing penalties on non-contributors $(F=164.27, p<.0001)^{1}$ </td><td>P=3</td><td>.4133 (.4303)</td></tr><tr><td>P=5</td><td>.5751 (.4264)</td></tr><tr><td rowspan="2">Cost for not contributing $(F=165.89, p<.0001)^{1}$ </td><td>Q=2</td><td>.5755 (.4262)</td></tr><tr><td>Q=4</td><td>.4129 (.4305)</td></tr><tr><td colspan="3">Benefits</td></tr><tr><td rowspan="2">Incentive for contributing $(F=164.74, p<.0001)^{1}$ </td><td>S=3</td><td>.5752 (.4260)</td></tr><tr><td>S=5</td><td>.4132 (.4304)</td></tr><tr><td rowspan="6">Benefit from contributed knowledge $(F=661.65, p<.0001)^{2}$ </td><td>R=0</td><td>.0703 (.0816)</td></tr><tr><td>R=1</td><td>.1623 (.3070)</td></tr><tr><td>R=2</td><td>.2375 (.2969)</td></tr><tr><td>R=4</td><td>.5820 (.3439)</td></tr><tr><td>R=8</td><td>.9557 (.0720)</td></tr><tr><td>R=12</td><td>.9574 (.0055)</td></tr><tr><td>Overall</td><td></td><td>.4942 (.4358)</td></tr></table>

1 — Factor level mean differences are statistically signi<sup>fi</sup>cant at the 0.05 level F statistic, and p-values in ().  
2 — All means are statistically less than the maximum value of 0.9574 at the 0.05 level, except for R=8.

Table 5 shows that when identity transparency was set at the 50% level, 51.14% of the individuals were non-contributors. At the 90% level, the percentage of non-contributors dropped to 47.71%. These results agree with previous studies that show that increased identity transparency produces smaller proportion of non-contributors [1,25,26,38], though the magnitude of reduction here may not be as large as expected. In our model, this is expected. The net bene<sup>fi</sup>t objective function in Eq. (1) shows that only individuals whose identity is known bene<sup>fi</sup>t from S the incentive given for contributing. Thus, for contributors to bene<sup>fi</sup>t from this, their identity has to be known, and we would expect that the larger the bene<sup>fi</sup>t, the greater the proportion of contributors. This is clearly seen in Table 6A, which shows the average proportion of non-contributors across identity transparency. When S=3, and I=50%, 59.51% of all individuals are non contributors, and for I=90%, 55.53% are non-contributors. Comparing this for S=5, we have 42.76% and 39.88%, respectively, a signi<sup>fi</sup>cant reduction. Thus, increasing the incentive S decreases the proportion of non-contributors, and for a <sup>fi</sup>xed S, the proportion of non-contributors is lower when identity transparency is at 90% compared to 50%.

All contributors, regardless of their identity, incur a cost P to share knowledge and to enforce penalties on non-contributors (Eq. (1)). We would thus expect that as this cost increases, there will be fewer contributors. This is seen clearly in Table 6C, which shows that when P increases from 3 to 5, the proportion of non-contributors increases, regardless of the identity transparency. When I=50%, increasing P from 3 to 5, increases the proportion of non-contributors from 42.80% to 59.47% (Table 6). When I=90%, this increase is from 39.86% to 55.54%. Table 6A also shows that either increasing the incentive S or reducing the cost P, regardless of the identity transparency, reduces the number of non-contributors. For example, when I=50%, S=3, and P=5, a scenario with the smallest incentive for contributing and the greatest cost for sharing knowledge, 70.98% of all agents are noncontributors. Conversely, when the incentive is the greatest and the cost the least, i.e., S=5 and P=3, only 37.55% of agents are noncontributors. A similar reduction is seen when identity transparency is at 90%. Here the proportion of non-contributors reduces from 67.09% (S=3, P=5) to 35.76% (S=5, P=3).

Table 6B shows a similar pattern. Increasing Q the cost for not contributing, or reducing P, regardless of the identity transparency, produces fewer non-contributors. For example, when I=50%, P=5, and Q=2, a situation with the highest penalty and the least cost for not contributing, 70.95% of all agents are non-contributors. But, when P=3, and Q=4, only 37.51% are non-contributors. A similar result is seen for I=90%. As both Q and S have similar effect on our objective (Eq. (1)), one adds to the bene<sup>fi</sup>t, and the other to the cost, changing either of the values produces a similar change in the proportion of non-contributors. For example, when I=50% and P=3, changing S from 3 to 5, reduces the proportion of non-contributors from 48.05% to 37.55%. A similar change is noted when we change Q from 4 to 2. These results provide further validation for our model, and support existing studies, which show that the greater the personal return from contribution and the lower the return from not contributing, the higher the level of cooperation [12,37,31].

Table 7  
Table 6  
Average proportion of non-contributors across identity transparency I

<table><tr><td rowspan="3"></td><td colspan="6">Identity transparency (I)</td></tr><tr><td colspan="3">50%</td><td colspan="3">90%</td></tr><tr><td>P=3</td><td>P=5</td><td>Total</td><td>P=3</td><td>P=5</td><td>Total</td></tr><tr><td colspan="7">A:</td></tr><tr><td>S=3</td><td>.4805</td><td>.7098</td><td>.5951</td><td>.4397</td><td>.6709</td><td>.5553</td></tr><tr><td>S=5</td><td>.3755</td><td>.4797</td><td>.4276</td><td>.3576</td><td>.4400</td><td>.3988</td></tr><tr><td colspan="7">B:</td></tr><tr><td>Q=2</td><td>.4808</td><td>.7095</td><td>.5951</td><td>.4414</td><td>.6703</td><td>.5559</td></tr><tr><td>Q=4</td><td>.3751</td><td>.4799</td><td>.4276</td><td>.3558</td><td>.4406</td><td>.3982</td></tr><tr><td colspan="7">C:</td></tr><tr><td>Total</td><td>.4280</td><td>.5947</td><td>.5114</td><td>.3986</td><td>.5554</td><td>.4771</td></tr></table>

On average, 49.42% of all individuals were non-contributors (Table 5). Clearly, the factor that produces the greatest increase in the percentage of non-contributors is R, the shared bene<sup>fi</sup>t from contributed knowledge (Table 5). There is a strong correlation of 0.7916 between R and the proportion of non-contributors, and changing the value of R from 0 to 12 increases the proportion of non-contributors from 7.03% to 95.74%. Although higher bene<sup>fi</sup>ts from shared knowledge yield higher payoffs for all, from an average payoff of −1.75 when R=0 to 3592.25 when $R = 1 2 ,$ , non-contributors particularly bene<sup>fi</sup>t from this, as they receive all the bene<sup>fi</sup>ts of shared knowledge, but few of their costs (Eq. (1)). As such, non-contributors experience higher bene<sup>fi</sup>ts than contributors as R increases, thus suggesting an increase in non-contributors as R increases.

While similar results exist in other domains, for example, the spite dilemma suggests that people are more concerned about their relative ranking among their peers than the absolute amount of payoff they receive [47], in our model, none of the agents adopt such a decision strategy (Table 2). To understand why the proportion of noncontributors increases when the shared bene<sup>fi</sup>t increases requires insight into the interrelationship between costs and bene<sup>fi</sup>ts (Eq. (1)), and the decision strategies (Table 2).

At any particular decision point, agents adopt one of six strategies (Table 2). Agents who adopt contribute, do not contribute, or repeat last action strategies do not directly use the shared bene<sup>fi</sup>t value R in making their decision on whether to contribute or not. For example, all agents who use the contribute strategy, contribute. Similarly, agents using the repeat last action use the same decision they did previously. Agents with the mimic majority strategy rely on the actions of other known agents before making their decision, and are only indirectly affected by the value of R. Agents adopt the learn from the past strategy only when there is a negative net bene<sup>fi</sup>t (Table 4), and this is more likely to happen for small values of R. For larger values of R, few agents follow this strategy, so it has minimal impact on the overall proportion of non-contributors. Table 7 shows the average proportion of known non-contributors and contributors for each decision strategy across all values of R. When R=0 and the average net bene<sup>fi</sup>t is negative, 24.70% of all known agents follow the learn from the past (Table 7). But, for all other values of R, where the average net bene<sup>fi</sup>t is non-negative, less than 1% of agents follow this strategy. Thus, the impact of this strategy on the overall proportion of noncontributors is small for most values of R.

Table 8  
Average relative bene<sup>fi</sup>t for known agents

<table><tr><td>R</td><td> $\overline{B}^{1}-\overline{B}^{0}$ </td></tr><tr><td>0</td><td>3</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>1</td></tr><tr><td>4</td><td>-1</td></tr><tr><td>8</td><td>-5</td></tr><tr><td>12</td><td>-9</td></tr></table>

Now, consider those agents who follow the mimic winners strategy. Agents who follow this strategy compare the average net bene<sup>fi</sup>t ${ \overline { { B } } } ^ { 1 }$ for all known agents who are contributors with ${ \bar { B } } ^ { 0 }$ the average net bene<sup>fi</sup>t for all known agents who are non-contributors, and choose to contribute if the relative bene<sup>fi</sup>t $( \overline { { B } } ^ { 1 } - \overline { { B } } ^ { 0 } ) { \geq } 0 .$ . In other words, agents following the mimic winners strategy become contributors when the relative bene<sup>fi</sup>t for all known agents is non-negative. For our model (Eq. (1)) this happens for smaller values of R. Table 8 shows the average relative bene<sup>fi</sup>t for all known agents at the end of the simulation, and clearly shows that smaller values of R lead to greater relative bene<sup>fi</sup>ts. Thus, as R increases, the relative bene<sup>fi</sup>t decreases, and we would expect to see a greater portion of agents who use the mimic winners strategy to become non-contributors. This can be seen in Table 7, where the proportion of known non-contributors for the mimic winners strategy increases as R increases. When R=0, where the average relative bene<sup>fi</sup>t is 3 (Table 8), 21.23% of all known agents follow the mimic winners strategy, with 2.21% being non-contributors, and the rest,19.03%, as contributors. Now, consider when R=12 (Table 7), with an average relative bene<sup>fi</sup>t of −9 (Table 8). Here, 17.88% of known agents who follow the mimic winners strategy are non-contributors, and only 1.66% are contributors, a signi<sup>fi</sup>cant change. Thus, agents following the mimic winners strategy are directly affected by the level of R, actually, by the relative bene<sup>fi</sup>t, which in turn affects those agents who use the mimic majority strategy. As the proportion of non-contributors among the agents who follow the mimic winners strategy increases, it signi<sup>fi</sup>cantly increases the proportion of agents who are non-contributors, thereby changing the majority of agents from contributors to non-contributors. Agents following the mimic majority strategy then adopt the non-contribution strategy of this new majority. The values in Table 7 show a strong correlation of 0.9853 between the proportion of non-contributors in the mimic winners and mimic majority strategy, thus supporting our observations. Given the above results, the average proportion of noncontributors can be predicted using simple linear regression with two independent variables, R and a dummy variable, coded as 1 if the relative bene<sup>fi</sup>t is non-negative and 0 otherwise. Table 9 shows the results, and indicates that nearly 96.55% of the variation can be explained by the two independent variables. Positive coef<sup>fi</sup>cients for R and a negative coef<sup>fi</sup>- cient for the dummy variable indicate that higher values of R and smaller relative bene<sup>fi</sup>t lead to a greater proportion of non-contributors.

Average proportion of known non-contributors (non-C) and contributors (C) by decision strategy

<table><tr><td rowspan="3">R</td><td colspan="10">Decision strategy</td></tr><tr><td>Don&#x27;t contribute</td><td>Contribute</td><td colspan="2">Mimic majority</td><td colspan="2">Learn from the past</td><td colspan="2">Mimic winners</td><td colspan="2">Last action</td></tr><tr><td>Non-C</td><td>C</td><td>Non-C</td><td>C</td><td>Non-C</td><td>C</td><td>Non-C</td><td>C</td><td>Non-C</td><td>C</td></tr><tr><td>0</td><td>0.0086</td><td>0.0066</td><td>0.0000</td><td>0.2285</td><td>0.0140</td><td>0.2330</td><td>0.0221</td><td>0.1903</td><td>0.0000</td><td>0.0361</td></tr><tr><td>1</td><td>0.0083</td><td>0.0066</td><td>0.0242</td><td>0.1900</td><td>0.0049</td><td>0.0004</td><td>0.0357</td><td>0.1803</td><td>0.0246</td><td>0.1782</td></tr><tr><td>2</td><td>0.0082</td><td>0.0066</td><td>0.0240</td><td>0.1900</td><td>0.0028</td><td>0.0001</td><td>0.0614</td><td>0.1506</td><td>0.0392</td><td>0.1640</td></tr><tr><td>4</td><td>0.0080</td><td>0.0064</td><td>0.0955</td><td>0.1085</td><td>0.0065</td><td>0.0001</td><td>0.1240</td><td>0.0788</td><td>0.0995</td><td>0.0908</td></tr><tr><td>8</td><td>0.0077</td><td>0.0062</td><td>0.1898</td><td>0.0010</td><td>0.0098</td><td>0.0002</td><td>0.1796</td><td>0.0158</td><td>0.1678</td><td>0.0092</td></tr><tr><td>12</td><td>0.0077</td><td>0.0061</td><td>0.1908</td><td>0.0000</td><td>0.0102</td><td>0.0002</td><td>0.1788</td><td>0.0166</td><td>0.1675</td><td>0.0091</td></tr></table>

Table 9 Linear regression results

<table><tr><td>Term</td><td>Estimate</td><td>p-value</td></tr><tr><td>Intercept</td><td>0.9251</td><td>0.0000</td></tr><tr><td>R</td><td>0.0042</td><td>&lt;.0001</td></tr><tr><td>Relative benefit indicator</td><td>-0.8304</td><td>0.0000</td></tr></table>

R<sup>2</sup> = 0.96557.

Thus, our simulation model allows us to explore and understand the complex interaction between bene<sup>fi</sup>ts and costs (Eq. (1)), and decision strategies (Table 4) on organizational knowledge sharing. While our results are consistent with previous studies, organizations also face challenges in deciding how and when incentives and penalties should be administered to encourage knowledge sharing. For example, if an organization already has incentives in place, what should they do next to increase knowledge sharing? To answer such questions, we apply data mining techniques to our simulation results. Speci<sup>fi</sup>cally, we apply partitioning, also known as decision or regression trees, to our simulation output [21]. Partitioning allows us to systematically analyze our output to detect unknown relationships. It works by creating a successive tree of partitions according to a relationship between the dependent and independent variables [21]. In our case, the independent variables are the different factors of Table 3, and our dependent variable is the proportion of non-contributors. A partitioning algorithm seeks to predict the dependent variable by searching through all possible groupings of the independent variables, recursively forming a tree of decision rules until the desired <sup>fi</sup>t is obtained. The set of decision rules can then be used to decide how incentives and penalties should be implemented to increase knowledge sharing.

Fig. 3 shows a tree of decision rules that resulted by applying a partitioning algorithm to our simulation results. The top node indicates that in the whole sample, approximately 49.42% of all individuals were non-contributors. As expected, R, the bene<sup>fi</sup>t from shared contribution, is the single best predictor of the proportion of noncontributors. When the shared bene<sup>fi</sup>t is high, RN4, nearly 96% of the individuals in the sub-sample are non-contributors, compared to 58% when R=4. The proportion of non-contributors is even lower, only 15.67%, when Rb4. When R≥4, no further predictors (splits) will signi<sup>fi</sup>cantly reduce the number of non-contributors. Thus, if the organization has a high value for the shared bene<sup>fi</sup>t, other incentives or penalties will be ineffective in increasing knowledge sharing.

When the initial shared bene<sup>fi</sup>t is low (Rb4), the organization can improve knowledge sharing by increasing Q, the cost for not contributing. When Q=4, only 6% of the remaining individuals are noncontributors, as compared to 25.11% when Q=2 (Fig. 3). When the cost for not contributing is low (Q=2), knowledge sharing can be improved by increasing S, the incentive for contributing, followed by reducing the cost P for enforcing penalties on non-contributors. When incentives for contributing is low (S=3), the organization should <sup>fi</sup>rst reduce P, the cost of enforcing penalties on non-contributors, followed by further reducing R. Thus, when incentives for contributing are low (S=3), and the cost of enforcing penalties is high (P=5), there is little bene<sup>fi</sup>t for contributors, and nearly 73.31% of agents are non-contributors. Contributions can be encouraged here by further reducing the bene<sup>fi</sup>t from shared contribution R. When R=0, 26.21% of agents are noncontributors, but for R =1 or 2, 96.86% of agents in the sub-sample are non-contributors. When S=3, and the cost of enforcing penalties is small, P =3, only 11.26% of agents are non-contributors. This can be further reduced by reducing R the bene<sup>fi</sup>t from shared contribution. In general, increasing the personal bene<sup>fi</sup>t for contribution, by reducing the cost P and increasing S, while at the same time, increasing the cost Q for non-contributors, produces the largest percentage of contributors. In the best case, only 5% of all individuals in the subsample are non-contributors (Fig. 3). The model shown in Fig. 3 explains nearly 85% (R<sup>2</sup> = 0.848) of the variation in the dependent variable.

![](/api/attachments/BC95JH9R/fulltext/images/3cfb60585f2fb26abf1a72f4b6c0f3f7b1ea2ba257ed98d2b05c898f400dd4fa.jpg)  
Fig. 3. Partition tree-proportion of non-contributors

The results in Fig. 3 show a sequence of logical steps that an organization can follow to increase knowledge sharing. Such analysis, especially when the interactions between factors are not clear, provides the organization with insights on how and where to concentrate efforts to improve knowledge sharing. Importantly, using agent-based simulation models allows us to explore more complex knowledgesharing relationships, and provides insight into results that may not be obvious with other approaches.

The objective of this paper was to explore knowledge sharing using an agent-based simulation model. Effort was made to ensure that our model assumptions were based upon established theories and knowledge. Factors that in<sup>fl</sup>uence cooperative behaviors, and agents' strategy choices, were extracted from <sup>fi</sup>ndings reported in prior research. Our results support previous studies, and validate our model assumptions. One result indicates that the greater the personal bene<sup>fi</sup>t from contributions, the higher the levels of knowledge sharing. This result supports previous empirical studies [37,20]. Other experimental studies have also found that contributions are more likely when individuals have the ability to punish the defectors [37]. This is in agreement with our simulation result that indicates that lowering the cost for sharing knowledge and enforcing penalties reduces the proportion of non-contributors.

## 6. Implications and conclusions

In this paper, we examined knowledge sharing through agentbased simulation. We used a basic case of knowledge sharing and constructed a simpli<sup>fi</sup>ed model to illustrate the feasibility and potential bene<sup>fi</sup>ts of the agent-based approach. Our model demonstrates that irrational and adaptive behaviors can be approached through agent-based simulation. In comparison with traditional modeling techniques, an agent-based simulation modeling offers several unique features. It retains much of the <sup>fl</sup>exibility of linguistic modeling, and the consistency and precision of mathematical modeling techniques. It is well suited for analysis of complex adaptive systems and emergent phenomena. Our simulation results demonstrate that in the presence of non-linear and adaptive interaction, unintended and unpredictable outcomes might emerge at the systems level. For example, we observe that lowering the bene<sup>fi</sup>ts from shared knowledge signi<sup>fi</sup>cantly increases the level of contribution. This observation seems counterintuitive and contradicts some of the studies that indicate that an increase in the marginal value of a public good leads to a higher level of contribution [22]. Such studies typically argue that an increase in the marginal value of a public good results in two distinct types of returns for the contributor: internal return, as it reduces the net cost of making a contribution, and external return, as it increases the bene<sup>fi</sup>t of a contribution to others. The level of cooperation increases as many people are motivated by altruism and they are sensitive to the cost of helping others in the provision of public goods [22]. However, previous empirical and theoretical research has mostly been restrictive in their <sup>fi</sup>ndings by their conditions and assumptions. Assuming that the higher marginal value of a public good is a return, rather than a vulnerability to the contributor, may not be appropriate to situations in which individuals compete and are concerned with not only their own payoff but also their payoff relative to that of others. This is illustrated in our model by the agents who follow the mimic winners strategy, and who base their decision on the relative bene<sup>fi</sup>t rather than the absolute payoff. Importantly, our model allows us to understand the complex interaction between costs, bene<sup>fi</sup>ts, and decision strategies. Such outcomes are dif<sup>fi</sup>cult to foresee by examining a component of the system in isolation, so an agent-based simulation approach like ours provides a viable way to observe emergent states that are hard to predict, as in knowledge sharing.

Hence, from a managerial perspective, the agent-based simulation approach assists the identi<sup>fi</sup>cation of unintended negative outcomes. In situations characterized by dynamic complexity, such as those involving knowledge sharing, this approach offers a systems perspective and sensitizes researchers to the possibility of interaction and outcomes that are dif<sup>fi</sup>cult to predict. The results generated from our simulation model help managers attend to the possible negative effects of increasing the value of shared knowledge by rewarding individual performance. It helps managers rethink their human resource policies to align individual bene<sup>fi</sup>ts with organizational competitive advantages. Further, as demonstrated in the Results section, the agent-based simulation approach can be combined with other techniques such as data mining to develop a potent management analysis tool that provides the organization with insights on what interventions are more effective than others.

As a further model enhancement, a measure of distance between individuals might also be incorporated. It is reasonable to assume that identities of contributors or non-contributors are more likely to be known by those individuals in their social networks. The potential effects of such a distance–identity interaction feature might be studied by extending our present model. For example, the mimic winners strategies require global information. But, it is more likely that employees have such information in only their social network. Then, how does the size and characteristics of such network in<sup>fl</sup>uence decision strategies, and therefore knowledge sharing? Further, assumptions on organization interventions can also be relaxed to extend our model. For example, our model assumes a constant rate for bene<sup>fi</sup>ts and costs (Eq. (1)). But, this is unlikely to be true in some organizations, where bene<sup>fi</sup>ts and costs may not only be non-linear, but also dynamically changing based on other organizational conditions.

Our argument for the potential of the agent-based simulation approach does not imply that this methodology should replace other traditional analytical techniques. Rather, a wide range of techniques for model development and empirical assessment should be used, and, in many cases, insightful comparisons can result when multiple approaches are used to tackle a single research question. Future research can explore the use of adaptive techniques like genetic algorithms and cased-based reasoning as part of agent-based simulations.

## References

[1] R. Albanese, D.D. van Fleet, Rational behavior in groups: the free-riding tendency, The Academy of Management Review 10 (2) (1985) 244–255.

[2] A. Aldea, R. Bañares-Alcántara, L. Jiménez, A. Moreno, J. Martínez, D. Riaño, The scope of application of multi-agent systems in the process industry: three case studies, Expert Systems with Applications 26 (1) (2004) 39–47.

[3] C. Athale, Y. Mansury, T.S. Deisboeck, Simulating the impact of a molecular ‘decision-process’ on cellular phenotype and multicellular patterns in brain tumors, Journal of Theoretical Biology 233 (4) (2005) 469–481.

[4] R. Axelrod, The Complexity of Cooperation: Agent-Based Models of Competition and Collaboration, Princeton University Press, Princeton, N.J., 1997.

[5] R. Axelrod, Effective choice in the prisoner's dilemma, Journal of Con<sup>fl</sup>ict Resolution 24 (1) (1980) 3–25.

[6] A.V. Banerjee, A simple model of herd behavior, Quarterly Journal of Economics 107 (3) (1992) 797–817.

[7] J. Barney, Firm Resources and Sustained Competitive Advantage, Journal of Management 17 (1) (1991) 99–120.

[8] A.J. Bertie, S.F. Himmelweit, A.B. Trigg, Social norms, cognitive dissonance and broadcasting: how to in<sup>fl</sup>uence economic agents, in: C. Bruun (Ed.), Advances in Arti<sup>fi</sup>cal Economics: the Economy as a Complex Dynamic System, Ch. 17, Springer-Verlag, Heidelberg, 2006.

[9] G.W. Bock, R.W. Zmud, Y.G. Kim, J.N. Lee, Behavioral intention formation in knowledge sharing: examining the roles of extrinsic motivators, Social–Psychological Forces and Organizational Climate, MIS Ouarterly 29 (1) (2005) 87–111.

[10] T. Bossomaier, D. Jarratt, M.M. Anver, J. Thompson, J. Cooper, Optimisation of client trust by evolutionary learning of <sup>fi</sup>nancial planning strategies in an agent based model, Proceeding of the The 2005 IEEE Congress on Evolutionary Computation, 2005.

[11] P. Brantingham, A neutral model of stone raw material procurement, American Antiquity 68 (3) (2003) 487–509.

[12] Á. Cabrera, F.E. Cabrera, Knowledge-sharing dilemmas, Organization Studies 23 (5) (2002) 687–710.

[13] L. Cederman, Modeling the size of wars: from billiard balls to sandpiles, American Political Science Review 97 (1) (2003) 135–150.

[14] L.C. Chen, K.M. Carley, D. Fridsma, B. Kaminsky, A. Yahja, Model alignment of anthrax attack simulations, Decision Support Systems 41 (3) (2006) 654–668.

[15] C.M. Chiu, M.H. Hsu, E.T.G. Wang, Understanding knowledge sharing in virtual communities: an integration of social capital and social cognitive theories, De cision Support Systems 42 (3) (2006) 1872–1888.

[16] T.H. Davenport, D.W. De Long, M.C. Beers, Successful knowledge management projects, MIT Sloan Management Review 39 (2) (1998) 43–57.

[17] P.J. Deadman, Modelling individual behaviour and group performance in an intelligent agent-based simulation of the tragedy of the commons, Journal of Environmental Management 56 (3) (1999) 159–172.

[18] J.H. Dyer, K. Nobeoka, Creating and managing a high-performance knowledgesharing network: the Toyota case, Strategic Management Journal 21 (3) (2000) 345–367.

[19] E. Fehr, S. Gachter, Cooperation and punishment in public goods experiments, American Economic Review 90 (4) (2000) 980–994.

[20] R. Garud, A. Kumaraswamy, Vicious and virtuous circles in the management of knowledge: the case of Infosys Technologies, MIS Quarterly 29 (1) (2005) 9–33.

[21] M. Gaudard, P. Ramsey, M. Stephen, Interactive data mining and design of experiments: the JMP partition and custom design platforms, White Paper, 2006 (26 July www.jmp.com/software/whitepapers/pdfs/372455\_interactive\_datamining.pdf).

[22] J.K. Goeree, C.A. Holt, S.K. Laury, Private costs and public bene<sup>fi</sup>ts: unraveling the effects of altruism and noisy behavior, Journal of Public Economics 83 (2) (2002) 255–276.

[23] R.M. Grant, Toward a knowledge-based theory of the <sup>fi</sup>rm, Strategic Management Journal 17 (1996) 109–122 (Winter Special Issue).

[24] A.K. Gupta, V. Govindarajan, Knowledge management's social dimension: lessons from Nucor Steel, Sloan Management Review 42 (1) (2000) 71–80.

[25] S.G. Harkins, P.R.E., Effects of task dif<sup>fi</sup>culty and task uniqueness on social loa<sup>fi</sup>ng, Journal of Personality and Social Psychology 43 (1982) 1214–1229 (June).

[26] S.G. Harkins, J.M. Jackson, The role of evaluation in eliminating social loa<sup>fi</sup>ng, Personality and Social Psychology Bulletin 11 (December) (1985) 457–465.

[27] F.A. Hayek, The use of knowledge in society, American Economic Review 35 (4) (1945) 519–530.

[28] C.E. Helfat, M.A. Peteraf, The dynamic resource-based view: capability lifecycles, Strategic Management Journal 24 (10) (2003) 997–1010.

[29] J.H. Holland, J.H. Miller, Arti<sup>fi</sup>cial adaptive agents in economic theory, American Economic Review 81 (2) (1991) 365–370.

[30] G. Huber, Transfer of knowledge in knowledge management systems: unexplored issues and suggested studies, European Journal of Information Systems 10 (2) (2001) 72–79.

[31] R. Isaac, J. Walker, Group-size effects in public-goods provision — the voluntary contributions mechanism, Ouarterly Journal of Economics 103 (1) (1988) 179–199.

[32] N.R. Jennings, K. Sycara, M. Wooldridge, A roadmap of agent research and development, Autonomous Agents and Multi-Agent Systems 1 (1) (1998) 7–38

[33] K.D. Joshi, S. Sarker, S. Sarker, Knowledge transfer within information systems development teams: examining the role of knowledge source attributes, Decision Support Systems 43 (2) (2007) 322–335.

[34] J.J. Jung, G.S. Jo, Brokerage between buyer and seller agents using constraint satisfaction problem models, Decision Support Systems 28 (4) (2000) 293–304.

[35] W.C. Kim, Procedural justice, strategic decision making, and the knowledge economy, Strategic Management Journal 19 (4) (1998) 323–338.

[36] J.P.C. Kleijnen, Veri<sup>fi</sup>cation and validation of simulation models, European Journal of Operational Research 82 (1) (1995) 145–162.

[37] P. Kollock, Social dilemmas: the anatomy of cooperation, Annual Review of Sociology 24 (1) (1998) 183–214.

[38] B. Latane, K.D. Williams, S.G. Harkins, Many hands make light the work: the causes and consequences of social loa<sup>fi</sup>ng, Journal of Personality and Social Psychology 37 (1979) 822–832.

[39] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, McGraw-Hill, Boston, 2000.

[40] M.W. Macy, Chains of cooperation: threshold effects in collective action, American Sociological Review 56 (6) (1991) 730–747.

[41] M.J. North, N.T. Collier, J.R. Vos, Experiences creating three implementations of the repast agent modeling toolkit, ACM Transactions on Modeling and Computer Simulation (TOMACS) 16 (1) (2006) 1–25

[42] M. Olson, The logic of collective action, in: C. Calhoun (Ed.), Contemporary Sociological Theory, Blackwell, Oxford, 2002.

[43] D.C. Parker, S.M. Manson, M.A. Janssen, M.J. Hoffmann, P. Deadman, Multi-agent systems for the simulation of land-use and land-cover change: a review, Annals of the Association of American Geographers 93 (2) (2003) 314–337.

[44] R.C. Picker, Simple games in a complex world: a generative approach to the adoption of norms, University of Chicago Law Review 64 (4) (1997) 1225–1292.

[45] W.C. Pitt, P.W. Box, F.F. Knowlton, An individual-based model of canid populations: modelling territoriality and social structure, Ecological Modelling 166 (1–2) (2003) 109–121.

[46] R.R. Prechter Jr., W.D. Parker, The <sup>fi</sup>nancial/economic dichotomy in social behavioral dynamics: the socionomic perspective, Journal of Behavioral Finance (2007) 84–108.

[47] T. Saijo, N. Hideki, The spite dilemma in voluntary contribution mechanism experiments, Journal of Con<sup>fl</sup>ict Resolution 39 (3) (1995) 535–560

[48] J.C. Spender, Making knowledge the basis of a dynamic theory of the <sup>fi</sup>rm, Strategic Management Journal 17 (1996) 45–82.

[49] P. Stone, M. Veloso, Multiagent systems: a survey from a machine learning perspective, Autonomous Robots 8 (3) (2000) 345–383.

[50] T.W. Wang, S.K. Tadisina, Simulating internet-based collaboration: a cost–bene<sup>fi</sup>t case study using a multi-agent model, Decision Support Systems 43 (2) (2007) 645–662.

[51] M. Wooldridge, Intelligent agents: the key concepts, in: V. Maík (Ed.), Multi-Agent-Systems and Applications II: 9th ECCAI-ACAI/EASSS 2001. Selected Revised Papers, Springer-Verlag, Heidelberg, 2002.

[52] M. Wooldridge, N. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995) 115–152.

![](/api/attachments/BC95JH9R/fulltext/images/6114cfeea2089917c597ab334b3f9ea3fbb9235e1c5dadbf8310796a496b4d3c.jpg)

Jing Wang is an assistant professor of Decision Sciences at the Whittemore School of Business and Economics, University of New Hampshire. Her research focuses on the area of Virtual Organizations, Open Source Software, and Agent-based Decision Support Systems. Her work ha been published in the Journal of Information Systems and Journal of Information Technology Theory and Application.

![](/api/attachments/BC95JH9R/fulltext/images/868623bd4138df616e944d06ab4d1fb7e92c3fe40190b168f6fcd8bb875a2e2a.jpg)

Kholekile L. Gwebu is an Assistant Professor of Decision Sciences at the University of New Hampshire. He holds a Ph.D. in Management and Information Systems from Kent State University. His current research interests include multi-attribute auctions, NYOP auctions and agent-based simulation. His papers have appeared in journals such as the Journal of Information Systems and Journal of Information Technology Theory and Application.

![](/api/attachments/BC95JH9R/fulltext/images/87954c524f1771372e06900b780a8da00c4ceb042d57a34b59932a55407b81e2.jpg)

Murali Shanker is a Professor in the Department of Management & Information Systems, Kent State University. He has published articles in journals like INFORMS Journal on Computer, IIE Transactions, Journal of the Operational Research Society, Decision Support Systems, and Decision Sciences His research interests lie in Distance Learning, Distributed Computing, Open Source, Simulation, and Neural-Network Modeling

![](/api/attachments/BC95JH9R/fulltext/images/aaf28e59091126a97f577f72b7fc243d3a9a3cfed40d7ecb087058a62ed41784.jpg)

Marvin D. Troutt is a Professor in the Graduate School of Management at Kent State University. He is a Fellow of the Decision Sciences Institute, His publications have appeared in Management Science, Operations Research, Decision Sciences, Naval Research Logistics, and similar journals. He received the 2005 Distinguished Scholar Award at Kent State University. He has served as Rehn Research Professor in Management at Southern Illinois University, Carbondale, Illinois. He served as Visiting Scholar in the Department of Applied Mathematics at the Hong Kong Polytechnic University 1994–95. His current interests include supply chain management, applied probability and applied optimization
