---
otero_id: 21105
otero_key: "33DGG89V"
title: "Soccer strategies that live in the B2B world of negotiation and decision-making"
authors: "Fernando Ramos; Ma.de los Angeles Junco; Enrique Espinosa"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00083-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Soccer strategies that live in the B2B world of negotiation and decision-making

Fernando Ramos, Ma. de los Angeles Junco, Enrique Espinosa

Divisio´n de Ingenierı´a y Arquitectura, Campus Ciudad de Me´xico, Instituto Tecnolo´gico y de Estudios Superiores de Monterrey, Calle del Puente 222 Ejidos de Huipulco, 14380 Me´xico D.F., Mexico

Received 13 February 2002; received in revised form 13 February 2002; accepted 10 April 2002

## Abstract

Decision-making within electronic business processes is frequently swamped by conflictive situations. Dynamism in real-life negotiation poses challenges when creating models of how business people interact and settle down strategic differences. Dispute resolutions are not fully addressed by current e-business decision-support systems (DSS). To attack this problem, we resort to an analogous model: soccer match strategies. These games are dynamic thrive with conflicts. Both worlds are mapped using a model in which agents cooperate toward common goals. As a result, we show a functional analogy between collaborative strategies in a soccer match and business-to-business processes. We present Java-based soccer and B2B simulators. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Soccer; e-Business; B2B; Agents; Conflict negotiation

## 1. Introduction

Due to the fact of the dynamic nature of modern business environments, a decision-making process is frequently characterized by conflicting situations. Fric tions derived from opposing interests, as well as competition, and other troublesome situations resulting from unlawful practices are all common, and expected, in human relations. It is expected, however, that humans will learn from their mistakes. An additional ingredient appears when a business operation is virtual, and physically distributed. Ajit Kambil stated in his 1997 IEEE Computer paper: ‘‘Traditional mechanisms for dispute resolution and influence are local, so the Internet, which has no national or geographic boundaries, presents new problems’’ [15]. Previously, Jacob Marschak [16] established a common framework for collaborative risk in corporate environments. In this paper, he suggests that organizational success depends not only on the individual decisions made, but also on externalities not under the control of the members of the organization. Such factors include competitive pressure, the price of capital and labor, regulatory issues, and other socioeconomic variables.

Depending on how fast the diverse actors can adhere to their evolving environment, that is, how fast they can learn from previous experiences, or failures, they will survive the non-monotonic evolution of things.<sup>1</sup> Once again, interaction models take a front seat in a real scenario. It is therefore natural that mainstream, AIrelated, electronic business procedures, commonly referred to by the industry as Business Intelligence [14], should address all these issues as well. Nowadays, the arrival of technology for building e-businesses is making way for old, but best, practices [11] to be automated. Consider, as an example, the IDEAL Approach to Internet-based negotiation [10]. This is a negotiation scheme based on a substantial exchange of proposals and counter-proposals in a rule-based environment. There is a competition between teams of people or companies for imposing criteria to others. The very nature of rules implies the inclusion of the Closed World Assumption [18], a view that is contrary to human conflict characterization, since business conflicts are not only of an operational or functional nature. All these are dynamic and uncertain domains hardly conceivable in a set of rules [7]. Another example is the Dynamic Evaluation Approach to virtual conflicts by Zhuge and Shi [24]. Once again, a groups-that-compete approach, similar to the one used in IDEAL, is characterized in military groups. The notion of group-togroup conflicts is really not adequate in e-business domains, because negotiations during stock market activity and strategy meetings in companies must, and will, consider singular contributions, even though such people form belong to [possibly conflicting] groups. This issue is critical—to look for common good, and to perform actions as a team, to reach such objectives. Opposing phenomena and people still exist, and affect the fabric of the production workplace. Such premise is key in our proposal, since it considers continuous changes in thought and action that make the underlying model for evaluating interactions among the members of the business group a considerably more complex one. Consequently, conflicting situations could take a long time to be solved, or could not be solved at all. Uncertain outcomes to professional efforts are also commonplace in social, political, and emotional arenas like e-commerce.

We therefore suggest that traditional methods for negotiation take into account situations within static environments [2,4,9]. Generally, a negotiation is viewed as a two-way exchange of information with evaluation on each end-point. This does not necessarily mean teamwork, although a protocol and a strategy may exist. If an agent evaluates its environment independently of others, then its view of things will be monotonic, and static, as a result. If it learns, it will probably be through a knowledge acquisition schema, rather than through adaptive (i.e. introspective) conduct. Finally, the above considerations are not built within a typical distributed decision-making framework. They do not reflect real dynamic group situations.

Agent communities can simulate such environments. We now present the main contribution of this paper: an agent-wise approach to characterizing business-to-business activity, which formalizes in an original way, an analogy between soccer and business strategies. Later, we present an actual soccer simulator written in Java, plus a second one, a natural evolution of the first, placed as a B2B simulator that emphasizes corporate collaboration crafted for evidencing strategic decisions while running a business. Evaluations, conclusions, and future directions of the overall effort are finally presented.

## 2. Dynamics in soccer

Models belonging to the cooperation within a soccer match, and the domains of interaction between players, ball, and goals, are typically dynamic and full of conflicting situations [1]. A soccer domain is well suited as a complex environment that allows the research community to develop several areas of Artificial Intelligence and Robotics. The properties that make simulated robotic soccer a good dynamic environment are [12,21]:

 Enough complexity to be realistic, it is not a deterministic world.

 Ability to support reactive agents.

 Agents modeling other agents.

 Cooperative and competitive behaviors.

 Agents should be able to communicate.

 Possibility of executing real time distributed decisions.

 A real team behavior should be supported by a coordination mechanism.

 Machine learning models need to be developed to improve the performance of the system.

In a group of interacting agents, where conflicts may arise, strategies will be conceived to achieve a mutually beneficial win-to-win situation, and construction, transfer and assimilation of meaning for dynamic/distributed interaction plus learning may be appropriate vehicles to achieve all of the above. Therefore, the soccer domain can be mapped into business environments by building an adequate characterization model. Negotiation among heterogeneous actors should usually require bringing data and decision support procedures down to earth.

In Ref. [12], we developed a distributed rational decision-making model for soccer agents. Besides, to visualize the contribution of all of the agents involved in a given play, we developed a matrix representation of a Q-learning model that serves to evaluate the risk and utility relationship of an action applied to a given situation. Additionally, our research shows that a Nash solution using the matrix Q-learning representation provides a way of evaluating joint-actions and allows agents to identify the best global utility. We used a Qlearning reinforcement-learning model because it is a non-policy model and has been demonstrated that it is a better method for reactive robotic applications in a simulated dynamic world. Q-learning is known as an off-policy temporal difference control [22].

The one-step Q-learning used is defined by [13]:

$$
\begin{array}{c} Q (s _ {t}, a _ {t}) \leftarrow Q (s _ {t}, a _ {t}) + \alpha \Big [ r _ {t + 1} + \gamma \max _ {a} Q (s _ {t + 1}, a) \\ - Q (s _ {t}, a _ {t}) \Big ] \end{array}\tag{1}
$$

where Q is the action-value function, $s _ { t }$ is the state at time $t , a _ { t }$ is the action taken at time t, a is the learning speed rate, r is the reward value received for taking an action given a state, and $\gamma$ is the discount factor.

Both a and c are values in the range [0..1]. The discount rate is the degree of backtracking a given set of reinforcements has with respect to their corresponding action values. The learning rate is a step size parameter and its value represents the speed of learning. If the value is low, the method performs more exploration and takes more time to find the optimal value. If the value is high, the method performs less exploration and learns faster but can skip (not see) better actions. In our team-strategy learning, we propose a matrix Q-learning where the agents evaluate the risk – utility relationship among several actions given the current state. The matrix Q-learning model represents joint-action vectors for several agents and, to accomplish that, we must change the traditional Qlearning formula (1) for the following formula:

$$
\begin{array}{l} \bar {Q} (s _ {t}, \bar {a} _ {i t}) \leftarrow [ I ] \Big (\bar {Q} (s _ {t}, \bar {a} _ {i t}) + \alpha \Big [ \bar {r} _ {t} \\ \quad + \gamma \max _ {\bar {a} _ {i t + 1}} \bar {Q} (s _ {t + 1}, \bar {a} _ {i t + 1}) - \bar {Q} (s _ {t}, \bar {a} _ {i t}) \Big ] \Big) \end{array}\tag{2}
$$

Thus, we are capable of taking into account several actions from different agents instead of only one action from a lonely agent.

As an example, Fig. 1 illustrates a three-agents’ situation: one in which agent 2 is the sender, agent 1 is the receiver, and agent 3 can perform an action that decreases the risk of the current state by attracting opponents or by performing an action that puts all agents in better positions for future situations.

Fig. 2a–c illustrates the information used to calculate the reward, $r ,$ for each agent, of the offensive team, in the situation illustrated in Fig. 1. We use a utility – risk-positioning function:

$$
\begin{array}{r l} r (\mathrm{CA}, a _ {m n}) & = \text { Utility } (\mathrm{CA}, a _ {m n}) - \text { Risk } (\mathrm{CA}, a _ {m n}) \\ & + \text { Positioning } (\mathrm{CA}, a _ {m n}) \end{array}\tag{3}
$$

where Utility represents how much the movement brings the player closer to the goal; Risk represents how risky the chosen action is. This calculation has to consider the number of opponents, their orientation and their proximity; Positioning represents how a given action helps the receiver player to evade its opponents and put it in a good receiving position; CA is the action chosen by the agent. In the context of soccer, actions include: indirect pass, direct pass, etc.; and $a _ { m n }$ is agent n on team m.

Using the information in Fig. 2a–c, we developed an action – reinforcement matrix for each agent involved in a play. Such matrix shows the relationship between the actions selected for each agent, and the reward expected of each action. For instance, the action – reinforcement matrix for agent 1, in the Fig. 1 situation, is illustrated in Fig. 3.

![](/api/attachments/33DGG89V/fulltext/images/bff3d73fb7e5fce5614d227548c7c9d43bc4cc88c74cb25ba62f9cacb420e3bd.jpg)  
Fig. 1. Three-agents’ situation: searching for better positions.

As illustrated in Fig. 3, actions 1, 4, 5, 7 and 8 are individually rational<sup>2</sup> [3] for agent 1. All actions that give the agent a positive utility will be considered to be in the negotiation set.<sup>3</sup> In this model, non-Pareto deals were included in the negotiation set to take into account exploration and exploitation of the Q-learning mechanism.

Agent 2 action values are shown in Fig. 4. As seen, movements by agent 2 are more accurate than those of other players because a sender agent has more risk of losing the ball. Thus, he has movements like 1/2 that means a movement between 1 and 2 explained in Fig. 4. Fig. 5 shows agent 2 (sender) utility values and Fig. 6 shows agent 2 risk values. Those values were obtained using Eq. (3).

Actions by agent 3 are evaluated in a different way because they do not participate directly in the current play between sender (agent 2) and the selected receiver (agent 1). Rather, its actions can influence future state-action values. It uses the utility of the action plus a value that represents how long this action puts it away from the opponent (see Fig. 7). It is necessary to take into account how much the action executed by agent 3 puts it in a good position allowing it to contribute on future plays (Fig. 8). In Fig. 7, repulsion values mean how far actions by agent 3 put it away from the opponent. In Fig. 8, good positioning values mean how actions by agent 3 put it closer to the current play and in a good position for future states.

If it is true that agent 2 selects movement 1/2 and agent 1 commits to perform movement 7 (looking to give it a chance for a risky, but high-utility, play), then the best options agent 3 can take are to perform movements 1 or 2. Nevertheless, if agent 2 selects movement 3 (to select a safer, low-utility, action), agent 3’s best options are to perform movements 2 or 3. Fig. 9 shows agent 3’s values for each possible movement. Movements 1, 2, 3, 5, 6, 7 and 8 are individually rational and all of them belong to the negotiation set.

![](/api/attachments/33DGG89V/fulltext/images/951efa816fb26d8b219577d9acdc0a700a9d0b12a8e83a721a2ea8c2c64fbd01.jpg)  
Fig. 2. Utility, risk and positioning values used to generate action-reinforcement matrix.

Once our model obtains the action–reinforcement matrix for each agent, we use a Nash solution called product maximizing mechanism in which the following conditions are satisfied [20]:

(1) The protocol is symmetrically distributed.

(2) The strategy is self-equilibrated.

(3) Given the protocol, if two agents play the strategy, they will agree on a deal that maximizes the product of their utilities. If there is more than a product-maximizing deal, they will agree on a deal that maximizes the sum of utilities. But, if there is more than one deal, the protocol will choose among those deals with some arbitrary probability.

Fig. 10 shows the results of using the product maximizing mechanism among several potential action–reinforcement values taken from the matrices of each agent in the example situation of Fig. 1. The numbers bordered in the matrix of Fig. 10 show the better action combination selection: nine in total, for the three agents participating in the play. As we can see, the combination of action numbers 7, 1/2 and 1 and 7, 1/2 and 2, for agents 1, 2 and 3, respectively, has the greatest reward according to the formula in Eq. (3). Besides, action combination with a reward of 6, bordered too, could be considered in the learning phase to deal with the exploration –exploitation payoff of the Q-learning model [22]. This allows the agents to exploit their better action combination options and sometimes explore other action combinations that have not had the greatest value in the initial learning phases, but that could improve while the agents are learning during the game.

![](/api/attachments/33DGG89V/fulltext/images/015839798e2139bfabc07aceb75b2c8b64d3df260549df5c921f14bfc4bc4b0d.jpg)  
Fig. 3. Action-reinforcement values for one agent.

The matrix of Fig. 10 is obtained using a decentralized decision-making process where the agents interchange messages using a Contract Net protocol [23]. This process can be explained as follows: the

![](/api/attachments/33DGG89V/fulltext/images/2724cf5131730b515692bc863f535ae54585c13d44ae8c56addf697e88d04de0.jpg)  
Fig. 4. Action-reinforcement values on agent 2.

![](/api/attachments/33DGG89V/fulltext/images/54a779a7291e6f68c3362dab47ef3628eed25b433034f26bc98af46194cfb191.jpg)  
Fig. 5. Utility values on agent 2.

agent who has the ball can do any of the basic behaviors related to the soccer agents such as: send an indirect pass, send a direct pass, dribble, clear, and so on. If the behavior it decided to do includes the participation of other teammates, the passer sends a message of its intention to them. Each possible receiver evaluates its current state related to the passer information and sends back a response including a reward value and the requirements the passer needs to accomplish to let the receiver to do whatever he is committed to do. The passer evaluates all the reward values and the received requirements, the bid, and chooses a feasible teammate. Thus, the shooter neither needs to make an optimal world assumption of the teammates nor has prediction capabilities to predict other agent’s actions.

![](/api/attachments/33DGG89V/fulltext/images/a3e332bbe531e0aa954f0187653a7b638920093d7d01962867553ec0018ab76b.jpg)  
Fig. 6. Risk values by agent 2.

![](/api/attachments/33DGG89V/fulltext/images/b2af530c1d395c22a69ca1b6b1527668f37837055b2b20cf410db7efe41e84dd.jpg)  
Fig. 7. Repulsion values on agent 3.

![](/api/attachments/33DGG89V/fulltext/images/dd15b4728c8e241e787ca16389e9d11569c0eecf1b4fda657293c3853298f3a6.jpg)  
Fig. 8. Good positioning values on agent 3.

![](/api/attachments/33DGG89V/fulltext/images/36ec29d48026c9cdf3a1d51493b3de2866f1bf1454fa4e1678a4a7aba1583a31.jpg)  
Fig. 9. Agent 3’s action-reinforcement values.

Moreover, the decision taken by the shooter is rational in the sense that he evaluates all its teammates’ joint-actions and chooses the one that offers the following:

 Minor risk value

 Bid with major utility for the system

The minor risk value is calculated considering the number of opponents and the current position and orientation of them. The greatest utility is computed based on the distance to the team goal.

In Fig. 11, we illustrate the results obtained in our model. Here, the passer agent has the risk–utility information related to each possible receiver bid. The passer could select among several options according to the current state, depending of the values of a matrix similar to Fig. 10. If the team is closer to the opponent’s goal, the passer could select a risky jointaction bid to put the team in a goal situation (exploration). Otherwise, if the team is closer to their goal, the passer could select a safer joint-action bid (exploitation).

Besides, our model improved the performance of the system by taking into account the joint-action deal utilities of the passer and possible receiver players plus the contribution of the rest of the players to future plays.

In our example, the passer, agent 3, decides to send an indirect pass to agent 5. However, agent 4’s contribution is to move toward the opponent’s goal, trying to attract opponents far away from the main course of play and to be in a better position for future drives. As a result of the decentralized decisionmaking process, the passer sends the ball to one of its best options that is agent 5. The receiving area is selected by agent 5 and is part of the bid sent to the passer. Besides, agent 4 contributes to the current play by attracting opponents and moving to a better position for future actions.

After the agents decide their actions, all of the agents involved in the current play learn, using our matrix Q-learning mechanism, the state–actions relationship to help for future actions.

## 3. Mapping B2B and soccer

As explained before, a soccer environment consists of a set of agents that negotiate toward a common goal. As they pass the ball over to each other, fooling the enemy team along the way, they must be quick on making decisions in a distributed environment. Conflicts appear in the shape of enemy players, weather phenomena, emotional issues like screaming fans of the opposing team, or wrong decisions by the referees. Teamwork is weaved between the members of the team, in an attempt to work around these opposing events. The better the outcoming strategy, the higher the probability for success will be. This is what we call ‘‘solving conflicting situations’’. It is a premise that, if the objectives are reached, they must be collaboratively enjoyed. In other words, success must benefit all the actors in the enterprise. In particular, the overall target is to win the game. Particular strategies apply for scoring goals, depending on the current score, time left in the game, and ranking among all teams in the league. This scenario is conceptually equivalent to that within, say, a business meeting. Negotiation must take place among corporate players. Success implies pushing the company’s gross income to a desired level, or objective, something desired by all members of the corresponding company.

<table><tr><td></td><td>a1</td><td>a2</td><td>a3</td><td></td><td>r</td></tr><tr><td rowspan="15">movement number</td><td>5</td><td>2/3</td><td>2</td><td></td><td>-3</td></tr><tr><td>5</td><td>2/3</td><td>3</td><td></td><td>-2</td></tr><tr><td>5</td><td>3</td><td>2</td><td></td><td>0</td></tr><tr><td>5</td><td>3</td><td>3</td><td></td><td>0</td></tr><tr><td>6</td><td>2</td><td>1</td><td></td><td>-18</td></tr><tr><td>6</td><td>2</td><td>2</td><td></td><td>-18</td></tr><tr><td>7</td><td>1/2</td><td>1</td><td></td><td>9</td></tr><tr><td>7</td><td>1/2</td><td>2</td><td> $\rightarrow$ </td><td>9</td></tr><tr><td>7</td><td>1/2</td><td>3</td><td></td><td>6</td></tr><tr><td>7</td><td>2</td><td>1</td><td></td><td>-18</td></tr><tr><td>7</td><td>2</td><td>2</td><td></td><td>-18</td></tr><tr><td>7</td><td>2</td><td>3</td><td></td><td>-18</td></tr><tr><td>8</td><td>1/2</td><td>1</td><td></td><td>6</td></tr><tr><td>8</td><td>1/2</td><td>2</td><td></td><td>6</td></tr><tr><td>8</td><td>1/2</td><td>3</td><td></td><td>4</td></tr></table>

Fig. 10. Joint-action values for agents 1, 2 and 3.

![](/api/attachments/33DGG89V/fulltext/images/dc9cc3f7a0ec0726e54316c6ae190975b4afd8c23d2366d9aac44b52e4e4f2ac.jpg)  
Fig. 11. Distributed utility – risk-driven matrix.

In an attempt to find a correct equivalence relation, criteria were selected that describes similar, but not equal, operational contexts, as well as their related data. Our purpose is to establish a common reference from which to suggest that the heuristic for making negotiations among soccer players can also be applied to bargaining that takes place between two companies whenever externalities not under the control of the business agents take over. The need to overcome these obstacles triggers assimilation of unexpected knowledge, contradiction with previous axioms, and learning of methods to overcome the former. We now turn to the specific criteria, and their bound data, presenting it as an analogical relationship between soccer and B2B (Table 1).

To establish a correct computational characterization of a set of procedures originating in social sciences, we first resort to well-known and documented strategies for effective negotiation by CDR Associates of Boulder, CO, USA [5]. Under this methodology, negotiation stages include:

Table 1  
Analogical relationship among computer-based learning, soccer and B2B domains

<table><tr><td></td><td>Soccer domain</td><td>Business to business (B2B) Environment</td></tr><tr><td>Strategic planning</td><td>Reactive planning. Domain knowledge.</td><td>Design a detailed plan for negotiation</td></tr><tr><td>Strategy structuring</td><td>Evaluating state–action relationships</td><td>Define issues and set an agenda</td></tr><tr><td>Presentation planning</td><td>Blackboard and negotiation model</td><td>Generate options for settlement</td></tr><tr><td>Negotiation supervisor</td><td>Game theory (Nash Equilibria)</td><td>Assess options for settlement</td></tr><tr><td>Settlement management</td><td>Conflict resolution</td><td>Final bargaining</td></tr></table>

U Evaluate and select a strategy to guide problem solving

U Make contact with other party or parties

U Collect and analyze background information

U Design a detailed plan for negotiation

U Build trust and cooperation

U Beginning the negotiation session

U Define issues and set an agenda

U Uncover hidden interests

U Generate options for settlement

U Assess options for settlement

U Final bargaining

We selected a subset of the most relevant steps (in bold, above), to soccer game milestones. This is summarized in Table 1.

We now turn to assess the reasons for choosing these options, and describe them fully in the sections below, thus offering methods for bringing down to earth the B2B – soccer analogy mechanism. The resulting algorithms are executed on Java applications for simulating business-process negotiation, a counterpart to the soccer device already presented in this paper, and elsewhere.

For the discussion in the following sections, we make use of the model in Fig. 12, a business framework oriented to establishing the relationships between the different sections of Porter’s Supply Chain that corresponds to designing a detailed plan for negotiation (in Table 1).

This model is an adaptation of one presented in Ref. [14]. A company has performed actions for positioning itself as a balanced entity when its selling and supply-chain teams actually cooperate in performing a true service and support.

At the same time, management, investment, and other regulating individuals weave their functionality with that of the operating departments of the company. The selling-service vs. management-operations crossing is characterized by the administration of all the knowledge at hand. This is where Artificial Intelligence meets Knowledge Management, in a domain called Business Intelligence by some top-ranked companies.

Common e-business units such as: Operating Resource Management Systems (ORMS), central corporate management (MGMT), Selling Chain Management (SLCM), Enterprise Resource Processing (ERP), Customer Relationship Management (CRM), Supply Chain Management (SCM), and Knowledge Tone Applications (KTA), appear in this model. Together, they constitute the backbone of any modern Internetbased business.

![](/api/attachments/33DGG89V/fulltext/images/5958bbf6e6732d2a71df11c70c5abdf0cb1350b5c295f2990bbb26dfde0f39db.jpg)  
Fig. 12. Establishing the relationships within Porter’s Supply Chain.

## 3.1. Strategic planning

In B2B, a plan must be correctly executed if the customer is going to be convinced of purchasing a product or service. In soccer, this is portrayed as evaluating state–action relationships as explained in Section 2. We will refer to Eq. (3) on calculating the reward for any given action performed by an agent:

$$
\begin{array}{r l} r (\mathrm{CA}, a _ {m n}) & = \text { Utility } (\mathrm{CA}, a _ {m n}) - \text { Risk } (\mathrm{CA}, a _ {m n}) \\ & + \text { Positioning } (\mathrm{CA}, a _ {m n}) \end{array}
$$

Taking into consideration that the major goal of a company is to perform well on sales, and therefore adding profit to the overall endeavor, and pinpointing that success in a market segment will depend on its rating among customers, we rewrite the above formula for reward, as a function of this Selling and Supply Chain process. This corresponds to defining issues and setting an agenda (in Table 1).

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{\text { k } \}}) & = U (\text { Sell }, a _ {\{\text { dotcom } \} \{\text { k } \}}) \\ & \quad - R (\text { Sell }, a _ {\{\text { dotcom } \} \{\text { k } \}}) \\ & \quad + P (\text { Sell }, a _ {\{\text { dotcom } \} \{\text { k } \}}) \end{array}\tag{4}
$$

where:

$$
\begin{array}{r l} & a _ {\{\text { dotcom } \} \{k \}} \\ & = \text { sales   agent   k   working   for   company   ``dotcom'' } \end{array}
$$

This means that the actual reward of the action ‘‘Sell’’ by a given company is made up of a teamwork effort, since, by Fig. 12, Utility (U) will depend directly on the enterprise strategies to establish a relationship with the client (the CRM segment). Likewise, Risk (R) will be proportional to the investment alternatives proposed by the CFO and other management personnel. Finally, all this will occur only if the firm is well positioned when performing a balanced selling-to-service operation. As a result, we expand Eq. (4) and its main components: utility, risk, and positioning, into:

$$
\begin{array}{l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{k \}}) = \{\text { PS } (\text { dotcom }, k) \\ \quad - \text { CM } (a _ {\{\text { dotcom } \} \{k \}}) \} \\ \quad - \{\text { EX } (\text { dotcom }) \\ \quad + \text { CS } (\text { Inv } _ {\text { passive }}) \} \\ \quad + \{\text { BL } (\text { svc }, \text { spp }) \} \end{array}\tag{5}
$$

where:

Sell Concrete strategic actions for selling in a supply-chain vs. customer relationship continuum. a{dotcom}{k} = agent k working for company ‘‘dotcom’’.

PS Profit company ‘‘dotcom’’ makes from sales by agent k.

CM Commission agent k gets from sales PS.

EX Expenses by company ‘‘dotcom’’.

CS Cost the company (‘‘dotcom’’) must exercise because of passive inventory Inv. If sales stabilize, or decrease, inventories will become a burden on the financial status of the corporation.

BL Balance between service (svc) and support (spp). This is a measurable indicator, which evaluates ratings commonly applied by strategic study manufacturers like the Gartner Group and Merryl Lynch, to companies using a technique called ‘‘Quality Pentagon’’. Hereby, functionality styles, vision, viability and technological capability are measured against service and support in a 1 –10 range. For example, top ERP developers like SAP, PeopleSoft, and Oracle, rate their competency using these types of studies [8].

![](/api/attachments/33DGG89V/fulltext/images/4d4e0a7b34eec5dd975cb1da286c5110959d2ef592255b7adad4c4d266621a26.jpg)  
Fig. 13. Positioning the corporate SLCM strategy.

Therefore, the risk involved in the selling chain procedure performed by a given agent can be planned in terms of the actions to be executed by the selling personnel. Moreover, several agents will be involved in a global sales strategy, and the e-business infrastructure will be an active player within. Actors may be distributed and heterogeneous. Consider Fig. 13. Positioning will be identified along the thick line that connects end-point strategies: those that emphasize the relationship with the customer, and those that give priority to the assembly of a delivery mechanism. Therefore, a measurable continuum for positioning is provided.

In Fig. 14, we turn toward specifying actions that an agent could execute to move itself along the above range of values. Just as in soccer, a player has a set of choices for passing the ball over to a teammate, a selling agent can ‘‘pass over the selling ball’’ over to fellow sales agents. This ‘‘pass’’ is really a domino effect of one player executing a [possibly] different selling procedure, and how that move impacts its teammates. The latter could, in effect, respond by continuing the same line of thought, or change the move. Conflicts could arise, as a group of people discusses over the best way to reach a common goal: selling

Fig. 14. Set of possible moves on selling.

more in a complex environment. Witness Fig. 15 for a global view of this collaborative activity.

## 3.2. Strategy structuring

The actual execution of the procedure and actions targeted at reaching the predefined goals takes place in soccer as a series of moves of players and football. To avoid chaos, a set of rules is obeyed. In the case of B2B, the regulating precepts are commonly called best practices [11]. These are a set of industryaccepted behavior patterns that presumably help the organization reach its goals. An electronic business will attempt to automate such best practices.

This automation process is analogous to the previously described situation where agents decide their actions, and all of the agents involved in the current play learn, using a matrix Q-learning mechanism, the state – actions relationship to help for future actions. A selling agent that decides to make a move informs all other agents of its intentions using a Contract Net Protocol. In turn, these other agents evaluate the implications of the play, in terms of its reward value. What this value becomes depends on the risk, positioning, and utility factors described in Section 3.1. The specific quantities assigned to each element will depend on market conditions, cultural issues, traditions, and extraordinary events (i.e. eventualities that form a non-monotonic environment). For example, consider:

$$
\left\{\mathrm{EX} (\text { dotcom }) + \mathrm{CS} \left(\mathrm{Inv} _ {\text { passive }}\right) \right\}\tag{6}
$$

Hereby, CS is a variable that could contribute to throw a large Risk (R) because the cost of idle inventories is high in a country with a very dynamic economy. Otherwise, if cultural [best] practices indicate that there are mechanisms to restore value to old or outdated goods, then the risk factor could effectively be lower. All this information must pass on from playing agent to its receivers. Witness Fig. 15. Agent 4 decides to sell with an emphasis on CRM practices, and informs its intentions to agents 3, 2 and 1. In a dynamic economy, the latter could evaluate the risk implied by this action, identify a list of [CRM] steps that would enable the proposal, and send it back to agent 4 along with the corresponding reward value. Finally, agent 4 will choose from its options, and select agent 1 because this one is the closer one to its own way of things.

## 3.3. Presentation planning

In B2B, the consumer, whether an end-point client, or a top-level executive, must be presented with some kind of convincing and attractive media that persuade her to purchase the goods at stake. In soccer, data are molded, and reshaped in a blackboard structure in which visual and audible data coming from the agents are stored and can be consulted for the agents to have the needed information for the decision-making.

![](/api/attachments/33DGG89V/fulltext/images/03bf67d298f9d9ee12a59f030747afd1c065d7d7d762c3b37cc45976bf913300.jpg)  
Fig. 15. Domino effect on collaborative selling actions.

![](/api/attachments/33DGG89V/fulltext/images/f71c97670ed1b26ec0a6a489ba7cf0919fc5a2fd6295299cb51629f8f907515d.jpg)  
Fig. 16. Negotiation on market behavior, Step 1.

## 3.4. Negotiation supervisor

The above events cannot happen forever. A base case must be found so that searches for a correct strategy will eventually end. In other words, an agreement must be set among the players, or actors. In soccer matches, a single play can occur with multiple repetitions of corporal, and geographical changes (i.e. the football changes position, as do the players). If a local success is achieved, the strategy will end, and give way to another round. A global success may be the scoring of a goal. In B2B, such local and global victories (or defeats) may refer to financial, marketing, or integration procedures. Witness Figs. 16–21. They represent a negotiation procedure based on the strategic planning and structuring, plus presentation planning and negotiation supervision.

In the above example, we provide the following state–action matrix of Don Taco, a restaurant franchise specializing in Mexican Cuisine. The initial state is that a B2B agent a1 will suggest the company perform a Selling Chain Management (SLCM) approach to increasing profit, rather than improving its current Supply-Chain Management (SCM) mechanisms. We arrive at this first conclusion by pointing out the best indicator of risk in the Nash Equilibrium submatrix (Table 2):

Table 3 State – action matrix for CARSO taking over Don Taco scenario, Step 2

a5

$$
\left[\begin{array}{c c c c}\mathrm{a1}&2 2&3 2&6\\\mathrm{a4}&2 8&3 0&5\\\mathrm{a6}&2 9&2 6&5\\\mathrm{a7}&1 8&2 5&5\end{array}\right]\rightarrow \left[\begin{array}{c}- 4\\+ 3\\+ 8\\- 2\end{array}\right]
$$

The matrix was obtained as follows:

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{2 \}}) & = \{\text { PS } (2 0 \text { M }) - \text { CM } (1 \text { M }) \} \\ & \quad - \{\text { EX } (4 0 \text { M }) \\ & \quad + \text { CS } (1 0 \text { M }) \} + \{\text { BL } (8) \} \\ & = 1 9 - 5 0 + 8 = - 2 3 \end{array}\tag{7a}
$$

Eq. (7a) suggests that market data pinpointed a 20- million (20 M) profit with a 1 M commission for its sales force, plus a 40-M operational expense company-wide, a 10-M passive-inventory cost (resulting from lack of efficiency in marketing-service delivery), and a poor industry rating in service-support balance. Likewise:

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{3 \}}) & = \{\text { PS(22   M) - CM(3   M)} \} \\ & - \{\text { EX(18   M) + CS(7   M)} \} \\ & + \{\text { BL(8) } \} = 1 9 - 2 5 + 8 = 2 \end{array}\tag{7b}
$$

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{4 \}}) & = \{\text { PS(23   M) } - \text { CM(3   M) } \} \\ & - \{\text { EX(15   M) } + \text { CS(6   M) } \} \\ & + \{\text { BL(8) } \} = 2 0 - 2 1 + 8 = 7 \end{array}\tag{7c}
$$

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{5 \}}) & = \{\text { PS } (2 5 \text { M }) - \text { CM } (5 \text { M }) \} \\ & - \{\text { EX } (1 0 \text { M }) + \text { CS } (5 \text { M }) \} \\ & + \{\text { BL } (8) \} = 2 0 - 1 5 + 8 = 1 3 \end{array}\tag{7d}
$$

This means that, initially, the buyer company wanted to take actions toward a balance between its

Stock Exchange Investment: Prudential selecting options for Grupo CARSO investing on Don Taco franchise. STEP 2: Switch to ERP-prone strategy.

![](/api/attachments/33DGG89V/fulltext/images/bc33e6dbc47c30a833c244ecf0fc709930862fc3bc53841b1160589875676e34.jpg)  
Fig. 17. Negotiation on market behavior, Step 2.

![](/api/attachments/33DGG89V/fulltext/images/7d6d5343ffe3b93c16c6a0d41db545d97e84bdd4f5999baacc3d4a830cb7985f.jpg)  
Fig. 18. Negotiation on stock exchange, Step 3.

selling and manufacturing strategies, but found out that the best choice, given the current data on the market, is to ${ \bf g 0 }$ for a better selling (SLCM) strategy. Actions geared for agents ${ \bf a } _ { 3 }$ and $\mathtt { a } _ { 4 }$ are also feasible, so using the exploration and exploitation tradeoff formerly described in the soccer Q-learning method, CARSO may find out that there actually are several options to choose from, even though there is a better one. A more conservative approach, Pareto Optimal-$i t y ,$ would tell the company to fetch only the best option, that of agent $\mathtt { a } _ { 5 }$ . This is not our current strategy, however. Ours is called Rationality, which means to select among Non-negative Utility Actions [3].

![](/api/attachments/33DGG89V/fulltext/images/59760301b49db3343bef42a3a97f1caad16a95a82bbe7f553273221880f1c6e9.jpg)  
Chart 1. Income vs. spending in Step 3.

Once the appropriate steps have been taken, the company behaves in a certain way in the market, and new indicators are fed to the management team, probably from the stock market, and strategic studies

$$
\left[\begin{array}{c c c c}\mathrm{a1}&2 3&3 1&5\\\mathrm{a2}&2 5&2 9&4\\\mathrm{a3}&2 2&3 1&5\\\mathrm{a4}&2 3&2 9&5\\\mathrm{a7}&2 0&1 9&4\end{array}\right]\rightarrow \left[\begin{array}{c}- 3\\0\\- 4\\- 1\\5\end{array}\right]
$$

![](/api/attachments/33DGG89V/fulltext/images/dd4aa9b19ab39fe0a73f90edd7144b24d7bafc38cdf9fb4cdbf685f851f9c284.jpg)  
Fig. 19. Negotiation on stock exchange, Step 4.

firms. It’s time for the next ‘‘play’’ in the game, so the Nash Equilibrium is recalculated:

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{1 \}}) & = \left\{\mathrm{PS} (3 8 \mathrm{M}) - \mathrm{CM} (1 6 \mathrm{M}) \right\} \\ & - \left\{\mathrm{EX} (2 1 \mathrm{M}) + \mathrm{CS} (1 1 \mathrm{M}) \right\} \\ & + \left\{\mathrm{BL} (6) \right\} = 2 2 - 3 2 + 6 \\ & = - 4 \end{array} \tag {8}\tag{8a}
$$

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{4 \}}) & = \{\text { PS(36   M) - CM(8   M)} \} \\ & - \{\text { EX(17   M) + CS(13   M)} \} \\ & + \{\text { BL(5) } \} = 2 8 - 3 0 + 5 = 3 \end{array}\tag{8b}
$$

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{6 \}}) & = \{\text { PS(41   M) - CM(12   M)} \} \\ & \quad - \{\text { EX(15   M) + CS(11   M)} \} \\ & \quad + \{\text { BL(5) } \} = 2 9 - 2 6 + 5 = 8 \end{array}\tag{8c}
$$

$$
\begin{array}{r l} r (\text { Sell }, a _ {\{\text { dotcom } \} \{7 \}}) & = \left\{\mathrm{PS} (3 5 \mathrm{M}) - \mathrm{CM} (1 7 \mathrm{M}) \right\} \\ & - \left\{\mathrm{EX} (1 4 \mathrm{M}) + \mathrm{CS} (1 1 \mathrm{M}) \right\} \\ & + \left\{\mathrm{BL} (5) \right\} = 1 8 - 2 5 + 5 \\ & = - 2 \end{array} \tag {8d}
$$

All of which yields (Table 3):

This time, the market reacted to the actions taken during step 1, and determined that, a correction in the company’s strategy should gear toward paying close attention to the supply-chain efficiency, by tightening the integration of its resources, in an Enterprise Resource Processing (ERP) approach. This contrasts suggestions by members of the board, or external consultants, that a more customer-related strategy be applied, since on the previous run of the company’s status, the consensus was to push toward CRM. The

$$
\begin{array}{l} \text {Table 5} \\ \text {State - action matrix for CARSO taking over Don Taco scenario,} \\ \text {Step 4} \end{array}
$$

$$
\left[\begin{array}{c c c c}\mathrm{a2}&2 1&2 3&5\\\mathrm{a3}&2 2&2 6&5\\\mathrm{a4}&2 4&3 1&6\\\mathrm{a6}&2 3&2 6&5\end{array}\right]\rightarrow \left[\begin{array}{c}+ 3\\+ 1\\- 1\\+ 2\end{array}\right]
$$

Table 7  
![](/api/attachments/33DGG89V/fulltext/images/a2872aef0548a0a4d3cd47b08881e5b03626f3ec3430dd425b88c2279c4e003d.jpg)  
Fig. 20. Negotiation on stock exchange, Step 5.

reasons for this shift are as follows. Eq. (7d) describes growing gross income with high expenditures on sales force, which reflect little operational spending and low passive inventories, a result of efficient sales, but with few results on positioning. Therefore, management decided to apply [again] the best possible solution, and chose to increase operational expenditures by 50%, even at the risk of elevating passive inventory by roughly 200% (Eq. (8c)). However, this aims at obtaining higher sales, and thus increasing gross income by almost 75%, partially due to the former target of optimizing the CRM goals. Industry pointers now position the company in a 5 grade-point marker (out of 10), which is a 20% net gain. Thus, at least partially, the strategies have proven satisfactory, and the new shift is justified in managerial terms (Fig. 17).

On the next round of performance check, we come across the scenario in Fig. 18. In an attempt to increase profit, the management team has decided to shoot for a careful revision of the same SCM–SLCM balance strategy. The state –action matrix analysis reveals a better chance for positioning if the CRM operation is slightly boosted.

State – action matrix for CARSO taking over Don Taco scenario, Step 5  
Income vs. spending in Step 5  
![](/api/attachments/33DGG89V/fulltext/images/6d93d24b3f6ae459de40f2c155da86eea38c8e2bc9c5abb4074dae439e299f46.jpg)

![](/api/attachments/33DGG89V/fulltext/images/c0672c773b5c2e838ff4418bf2243fa3426506ffc52672a581e6cea138cbfe47.jpg)  
Fig. 21. Negotiation on stock exchange, Step 6.

This, however, implies a risk in higher spending due to projected gross profit increases, as shown below.

Average income possibilities rose 44% over those declared in step 2. Alongside, gross income average was almost identical, only 5% lower in step 3, but sufficient to trigger discomfort in the board of investors. The best action set features a subtle adjustment to the customer relationship strategy.

These minor changes can be technical, and not strategic at all. They also deliver the promise of a better positioning grade in the short term. A close review of all possible moves depicts consistency between income and spending. Chart 1 reveals the relationships as extracted from Table 4.

On the next iteration, the fourth one, management loses confidence, since positioning is not improving, with a 35-M spending spree. Therefore, new actions are fabricated so as to lower spending, and attempting to keep revenues at the same time. Overall, the projections are that expenditures will increase on the 40% range, whereas profit will only increase in the 10% boundary. Positioning will not benefit at all, and the best recommendation is to push for a re-engineering of the ERP structure.

Fig. 19 proves that the efforts undertaken in step 2 (Fig. 17) are being considered again, but for different reasons. The accumulation of knowledge, business learning, and trial-and-error behavior are thus evidenced, as a non-monotonic organizational behavior is identified: going back to a line of action that was previously tried, and corrected. The new course of action is described in the state–action matrix shown in Table 5.

<table><tr><td colspan="4">a1</td></tr><tr><td> $\begin{bmatrix} a2 & 14 & 21 & 5 \\ a3 & 26 & 26 & 4 \\ a4 & 20 & 21 & 4 \\ a5 & 16 & 24 & 5 \\ a6 & 32 & 29 & 3 \\ a7 & 28 & 24 & 3\end{bmatrix}$ </td><td> $\rightarrow$ </td><td> $\begin{bmatrix} -2 \\ +4 \\ +3 \\ -3 \\ +6 \\ +7\end{bmatrix}$ </td><td></td></tr></table>

![](/api/attachments/33DGG89V/fulltext/images/6934ac5d943945bffdd9a1b95e069ab83630ede91a177d052ca36f8133e647cd.jpg)  
Fig. 22. Negotiation settlement.

The risk is relatively low, and management acts moderately. Now, this passiveness shows up in the next step, where net profit actually turns out to be 10% lower than the reported amounts for step 3. On the other hand, expenditures do balance out and settle on levels similar to those reported on the second iteration. The results are conclusive, and the management team decides that only a true balance between SCM and SLCM will bring prosperity. Q-learning has shown to be a decision-support system (DSS) in the context of B2B operations, and the next policies the company takes are geared toward this symbolic balance between production and selling forces. Fig. 20 describes graphically this balancing tendency. Consequently, the company places equivalent efforts into selling and into servicing active customers, boosting its positioning within the industrial segment, and this is reflected in projected figures, as shown in Table 6.

Once again, the profit vs. spending ratio is kept consistent, as shown in Table 7.

A final analysis of the company’s performance is run in step 6 (Fig. 21). The inertia for balancing SCM and SLCM finally makes way for a stabilization of the corporate action diversity. As in the soccer match, a goal has been reached when spending rates are proven to be final, and cannot be forced down while keeping viability within the corporation. However, at the same time, income is also increased, and stable, lowering the risk of sudden drops in the profit margin (Table 8).

Throughout this simulation of a non-monotonic agent behavior, policy changes have also followed a pattern. Consider Fig. 22, in which a measurement of strategy vs. shifts in actions derived from corporate decisions is presented. The left-hand sequence of steps (1 –6) indicates that early shifts were strong, but tended to soften as the management team Q-learned about its business, its risks, utilities, and overall pros and cons. The differential in change diminished, until it settled down. This process of reaching a state of common good is similar to the premises stated in the soccer match simulator. Table 9 shows the decrease in shift differential and its consequent result in settlement. It is relevant to point out that it may happen that this differential never converges, and so the game may turn out to be one of extremes. This is further noted in Section 5.

Table 9 Settlement process through differential decrease  
![](/api/attachments/33DGG89V/fulltext/images/8eba10e39cb87dfc07367560399c236d744c7de5a585f412a23d8d10fbf76db1.jpg)

## 3.5. Settlement management

Resolving conflicts means that all parts (e.g. teams) will confront a reality: that there has been a definition of the intended goals, and someone has succeeded in reaching those goals before others have. In all cases, some sort of termination must be set to the negotiation process. Ideally, such finale implies a settlement that may eventually lead to final bargaining (the last two B2B entries in Table 1). In this case, the goals have been to reach stability in profit and spending. To reach those goals, strategic vehicles such as ERP, SCM, CRM and SLCM tools and actions have been applied. The amount of priority a given tool has been given is dependent on its relative contribution toward the good of the many (i.e. all those business actors in this scenario).

We shall emphasize that, in this paper, our scenarios take into consideration only a natural flow of events, and complete corporate independence. That is, no external forces, like the ones presented in Section 1, have been characterized at all. We shall leave this as future work on negotiating multi-agents for e-business. Such factors may include economic crises, corruption, dumping, trade barriers, and war. Hereby, the only forces acting upon all decisions are the ones taken within the company itself.

![](/api/attachments/33DGG89V/fulltext/images/b50a2d8a90a3d02c579aa0c53c68fe078bc789916bef19bdfea7fa1823cafeec.jpg)  
Fig. 23. Java-based soccer match applet: offensive strategy in progress.

![](/api/attachments/33DGG89V/fulltext/images/fd273e8086cbf28115a0bd73048dce86f1d15003084c9d17bff98deb290f1872.jpg)  
Fig. 24. Java-based soccer match applet: goal scored.

We now turn to make a deeper integration of the three models being presented in this paper. Section 5 will describe our proposed merger of two current projects: the soccer simulator [17], described in Section 4, and an e-business infrastructure and training needs diagnose information system [6].

## 4. Soccer and Java-based simulator

The simulator software presents an actual soccer match. It emphasizes Q-learning for achieving an offensive team strategy, although not a defensive one. In Fig. 23, a play in progress can be witnessed. In Fig. 24, a goal has been scored. Understanding the soccer game metaphor is straightforward, but the underlying collaboration strategy for the offensive players is not.

Plays are always characterized in one direction, that is, from left to right. The opposing team does not really ‘‘play the game’’, and poses no real threat to the game (except for positioning the enemy players, who might get in the way). Some of these problems will be solved in the next version of the Q-learning B2B simulator.

## 5. Toward a B2B and Java-based simulator

We now turn our attention to the implementation of the strategy structuring and negotiation supervision of the [analogically conceived] B2B soccer match described in Sections 3.2 and 3.4, respectively. Consider the business run in Figs. 16–21. The user will witness a very similar field, and game in progress. However, they will see enemies taking over the ball, and ‘‘kicking’’ it toward the opposing field. Fig. 25 describes play steps 2, 3 and 4 (Figs. 17 – 19) in a simplified fashion. Control of the flow of events was turned to the ‘‘enemy’’ (i.e. shift toward an opposing strategy) two times.

As was mentioned in Section 3.4, it may happen, given specific risk calculation circumstances, that the

![](/api/attachments/33DGG89V/fulltext/images/4168304830df79606fbc28c2306ac83ee6b897d8c07db93f2935779c9a2f8eae.jpg)  
Fig. 25. Java-based B2B-through-soccer simulator.

strategy shift differential decrease (witness Table 9) never converges, and so the game may turn out to be one of extremes. By extremes, we now mean that the ball constantly changes hands, and SCM or SLCM goals are constantly reached. Fig. 25 describes such possibilities.

![](/api/attachments/33DGG89V/fulltext/images/5074cfdcc5b182bf8f1c572c5d5910c38d5a150d8e13ed917311ba90bd4a96f4.jpg)  
Fig. 26. Java-based soccer simulator with controls.

The exact method for the receiver to ‘‘lose the ball’’ currently is the following: If an inverse best risk (e.g. passing trajectory) is calculated in such a way that it depicts a change in direction, the nearest opponent to the receiving agent is chosen as the ‘‘stealer’’. Thus, the opposing team is said to take away control of the actions. On the other hand, if current conditions allow it, the match may reach a stable condition such as the one referred to in Figs. 16–21. In such a case, losing the ball will become less and less possible, so that eventually an idle state may occur. If this happens, no end-goals (SCM or SLCM) may be reached at all, at least temporarily. These deadlocks are acceptable in the B2B world and represent normal ups and downs a company may experience throughout its lifetime. They are, furthermore, another example of the non-monotonic nature of the evolutionary process followed by e-business procedures.

Just as the soccer metaphor tends to be easily understood by most people, the B2B procedure depends on criteria that are more complex than a mere desire to reach the opposing goalie. It is not commonplace, as it depends on business information that may be hard to grasp. Therefore, usercentered information accompanies the next simulator, and is shown next to the playing field (witness Fig. 26).

## 6. Conclusions and future work

The basis for our work is the negotiating and learning models tested in our simulator. These will be further tried in the small robot league of the RoboCup contest [19]. Once we have incorporated the defensive strategies to the soccer simulation, we will blend it into a B2B problem simulator that includes not only cooperation among the agents, as explained in Section 4, but competition, too. An explanation of this follows.

The soccer simulator implemented the negotiating and learning model explained in Section 2. As a future work in the soccer simulator, we will include defensive strategies using the matrix Q-learning and the distributed decision-making model but with different intention: to defend the goal area and to take away the ball from the opposite team. This can be fit into the analogous business model, too. For example, since the current simulator does not provide new options (i.e. players) for passing the ball, this will be added as a bonus feature for allowing dynamic solving of more complex problems, or conflicts. Conflicts are currently described by changes in the differential decrease (Table 9). However, they are only pinpointed, not solved. It is not the purpose of the simulator to provide strategies for solving conflicts. This may be yet another feature to add in a later version.

As said in Section 3.4, the soccer simulation takes into consideration only a natural flow of events, and complete corporate independence. That is, no external forces, like the ones presented in Section 1, have been characterized at all. Although the B2B simulator does implement the notion of ‘‘enemy player’’, as shaped by SLCM-to-SCM tug of war, still it is a singlecompany process. Future work includes adding the capacity to perform multiple-business interaction and human phenomena such as error, incompetence, and corruption. Handling these phenomena requires the analysis of large volumes of information. Therefore, a final trend in the evolution of our work will be the addition of tools for data mining and Business Intelligence.

Ideally, future work will involve finishing up the characterization of all the original business procedures set by CDR Associates. The remaining issues are:

U Evaluate and select a strategy to guide problem solving

U Make contact with other party or parties

U Collect and analyze background information

U Build trust and cooperation

U Beginning the negotiation session

U Uncover hidden interests

In this paper, we have shown practical uses for an idea that stemmed from analogical thinking of a commonplace scenario: soccer, and its recharacterization as another common, but largely ignored area of thinking, collaborative work in business domains. The development of simulators in both scenarios will allow us to build realistic tools for performing in groups that need to develop skills in distributed business conflict resolution in ways that sportspeople already do.

## References

[1] R. Axelrod, The complexity of cooperation, Agent-Based Models of Competition and Collaboration, Princeton Univ. Press, Princeton, NJ, 1997, ISBN: 0-691-01567-8.

[2] A. Bartelt, W. Lamersdorf, Agent-oriented concepts to foster the automation of e-business, Database and Expert Systems Applications, Proceedings, 11th International Workshop, IEEE, 2000, pp. 775– 779.

[3] K. Binmore, Teorı´a de Juegos, McGraw Hill, Espan˜a, 1994, pp. 167 – 208.

[4] S. Das, S. Yost, M. Krishnan, Effective use of Web-based communication tools in a team-oriented, project-based, multi-disciplinary course, in: Frontiers in Education Conference, 1999, FIE ’99, 29th Annual, vol. 2, IEEE, 1999, pp. 13A2 14– 13A2/17.

[5] Effective Negotiation Techniques. Course by CDR Associates. Published on the web at: http://www.lead.org/lead/training/international/usa/1999/docs/papers/effective<sup>\_</sup>negotiation<sup>\_</sup>techniques.htm.

[6] E. Espinosa, et al., DICNE: A Diagnoser for E-Business Infrastructure Requirements Definition, Keynote Address at the YUINFO-2001, University of Belgrade, Yugoslavia, March 2001.

[7] E. Espinosa, F. Ramos, A constructivist learning studio based on cognitive time analysis, in: W. Chin, F. Patricelli, V. Milutinovic (Eds.), Electronic Business and Education: Electronic Business and Education Recent Advances in Internet Infrastructures, Kluwer, USA, 2001, pp. 33–89, Hardbound, ISBN 0-7923-7508-4, August.

[8] Gartner Group, Conference Presentation no. SYM9ERP-Vend1099Kpond, 1999.

[9] A.Q. Gates, P.J. Teller, A. Bernat, S. Cabrera, C.K. Della-Piana, A cooperative model for orienting students to research groups, in: Frontiers in Education Conference, 1999, FIE ’99, 29th Annual, vol. 2, IEEE, 1999, pp. 13A4/6 – 13A411.

[10] J. Hammer, C.B. Huang, Y.H. Huang, C. Pluempitiwiriyawej, M. Lee, H. Li, L. Wang, Y. Liu, S.Y.W. Su, The IDEAL approach to Internet-based negotiation for e-business, Data

Engineering, 2000, Proceedings, 16th International Conference, IEEE, 2000, pp. 666–667.

[11] L. Harden, B. Heyman, R. Bruner, Net Results: 2. Best Practices for Web Marketing, 1st edn., Prentice Hall, USA, 2001.

[12] A. Junco, F. Ramos, Improving multi-agent coordination with an approach based on a distributed rational decision making model, International Journal of Knowledge-Based Intelligent Engineering Systems (IJKBIES), (2001) 268–278, October.

[13] L.P. Kaelbling, M. Littman, A.W. Moore, Reinforcement learning: a survey, Journal of Artificial Intelligence Research 4 (1996) 237– 285.

[14] R. Kalakota, M. Robinson, E-Business: Roadmap to Success, 2nd edn., Addison-Wesley, USA, 2001.

[15] A. Kambil, Doing business in the wired world, IEEE Computer, IEEE, 1997, pp. 56 – 61, May

[16] J. Marschak, Problems in Information Economics, Economic Information, Decision, and Prediction: Selected Essays, vol. 2, pp. 63 – 76.

[17] F. Ramos, M.A. Junco, Learning team strategies for multiagent systems environments, YU INFO 2001, International Symposium on Information Technologies, March, 2001.

[18] R. Reiter, On Reasoning by Default, Proceedings of Theoretical Issues in Natural Language Processing—2, University of Illinois, Urbana, Champaign, 1978, pp. 210 – 218.

[19] Robo Cup at: http://www.robocup.org/02.html.

[20] J. Rosenschein, G. Zlotkin, Rules of Encounter, The MIT Press, Cambridge, 1998.

[21] P. Stone, M. Veloso, A layered approach to learning client behaviors in the robocup soccer server, Applied Artificial Intelligence 12 (1998) 165– 188.

[22] R. Sutton, A. Barto, Reinforcement Learning, An Introduction, The MIT Press, Cambridge, 1998.

[23] G. Weiss, Multiagent Systems, A Modern Approach to Distributed Artificial Intelligence, The MIT Press, Cambridge, 1999.

[24] H. Zhuge, X. Shi, Dynamic evaluation approach for virtual conflict decision training, IEEE Transactions on Systems, Man and Cybernetics—Part C 30 (3) (2000) 374 – 380, August.
