---
otero_id: 15106
otero_key: "JY2BXW7W"
title: "Using AI and games for decision support in command and control"
authors: "Joel Brynielsson"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using AI and games for decision support in command and control

Joel Brynielsson

Royal Institute of Technology, SE-100 44 Stockholm, Sweden

Swedish National Defence College, PO Box 27805, SE-115 93 Stockholm, Sweden

Accepted 9 June 2006

Available online 30 October 2006

## Abstract

Developers of tomorrow's command and control centers are facing numerous problems related to the vast amount of available information obtained from various sources. On a lower level, huge amounts of uncertain reports from different sensors need to be fused into comprehensible information. On a higher level, representation and management of the aggregated information will be the main task, with prediction of future course of events being the uttermost goal. Unfortunately, traditional agent modeling techniques do not capture situations where commanders make decisions based on other commanders' reasoning about one's own reasoning. To cope with this problem, we propose a decision support tool for command and control situation awareness enhancements based on game theory for inference and coupled with traditional AI methods for uncertainty modeling. © 2006 Elsevier B.V. All rights reserved.

Keywords: Bayesian network; Influence diagram; Game theory; Bayesian game; Command and control; Situation awarenes

## 1. Introduction

The goal of any situation awareness system is to keep track of and use available information in a proper and timely manner to support planning and decision-making [12]. Due to huge amounts of data the establishment of situation awareness must be seen as an information fusion process starting with sensory data that is propagated upwards being fused into comprehensible information. However, merely presenting a comprehensible description of the situation, the situation picture, does not give a complete understanding of the development of a situation. Hence, the last step in the fusion process is the prediction step where one tries to predict opponent plans and suggest future courses of actions.

The challenges and difficulties when it comes to prediction are fundamentally different depending on available time and resources. In this paper we focus on long-term operative decision-making in command centers. These situations arise in command and control (C2) [5] where the decision situation is characterized by its multi-agent planning perspective where one wants to make predictions using historic events as well as make look-ahead predictions using assumptions regarding future events. The typical civilian example scenario is a disaster relief scenario and the typical military example is a C2 scenario where commanders make long-term decisions on the operative level. In a data fusion context these situations belong to “threat prediction” according to the so-called JDL model [28,32], which is used to structure information fusion processes. This has been recognized in for example Ref. [18] where the authors suggest the use of game-theoretic algorithms for the estimation process in higher level data fusion. Indeed, game-theoretic reasoning should be used for multi-agent decision-making in command centers that need to make decisions regarding long-term goals. After all, game theory is not just another tool in a toolbox — it is the toolbox itself.

There is a current discussion regarding the relevance of decision theory for human decisions, based on the perception that human decision-makers in experiments do not seem to follow the theory. While the discussion is highly relevant and potentially troublesome, we observe that there are no serious alternatives and we rely on Weibull's defense saying that the experiments where violations are observed are often designed so that it is questionable whether the perceived subject utility of outcomes represents what the designer had in mind [31].

One goal of artificial intelligence (AI) [27] has been to create expert systems, i.e., systems that can, provided the appropriate domain knowledge, match the performance of human experts. Such systems do not yet exist, other than in highly specific domains, but AI research has implied that researchers from widely differing fields have come together in order to solve questions regarding knowledge representation, decision-making, autonomous planning, etc. The results provide a good ground for the construction of C2 decision support systems. During the last decade, the intelligent agent perspective has lead to a view of AI as a system of agents embedded in real environments with continuous sensory inputs. We believe that this is a viable way to reason about command and control decision-making and we adopt the agent perspective throughout this paper.

The basic elements that we use for reasoning about uncertainty are random variables. General joint distributions of more than a handful such variables are impossible to handle efficiently, and the way to model distributions as Bayesian networks (BN) [19] has become a key tool in many modeling tasks. An im portant, but often overlooked, problem is that of constructing the BN which requires knowledge from domain experts. An interesting approach using causal maps is however announced in Ref. [21]. An influence diagram is a natural extension to a BN, incorporating decision and utility nodes in addition to chance nodes [13]. It represents decision problems for a single agent. Decision nodes represent points where the decision-maker has to choose a particular action. Utility nodes represent terminal nodes where the usefulness for the decisionmaker is calculated. Influence diagrams can be evaluated bottom-up by dynamic programming to obtain a sequence of maximum utility decisions.

A problem with ordinary AI tools is that they do not capture “gaming situations” where one wants to reason about opposing agents acting according to beliefs about one's own actions. This situation is not possible to model in an influence diagram or BN without additional machinery [27].

In this paper we illustrate the game-theoretic analysis techniques with a concrete example on the tactical level. Section 2 describes the example in a readable fashion. Section 3 introduces game-theoretic reasoning and discusses the building blocks in more detail. Section 4 gives a brief definition of a C2 multi-agent decisionmaking architecture, based on influence diagrams and game theory. Section 5 discusses how to address the gaming problem arisen in the scenario and solves it. Section 6 addresses the problems and possibilities that the ambiguities typical for a game-theoretic solution pose. In Section 7 we discuss computational issues along with a short survey on the current computational complexity status for equilibria computation. Finally, Section 8 concludes and discusses future research.

## 2. Scenario Härnösand

The scenario has been constructed by researchers, with some help from a domain expert, in order to be useful for specific research questions rather than being an example of a realistic C2 decision situation. A scenario map depicting the relevant units for the outlined decision problem can be seen in Fig. 1 along with the terminology we use when referring to the map. For simplicity, and as illustrated in Fig. 1, throughout the scenario description we refer to friendly and hostile forces as “blue” and “red” forces, respectively.

## 2.1. Northern Sweden 2020

Tension has grown gradually in the Baltic Sea during the last years. As a consequence, the Swedish armed forces have been provided with resources in order to maintain units that are on continuous alert. At the outbreak of the invasion, a number of events happen at the same time, some that are immediately considered as threats and some that may or may not be threats.

At 01:00 an enemy force disembarks 50 km north of the city of Härnösand. Reports from civilians make it likely that the force consists of two heavily armed tank companies and one mechanized infantry fighting company. At about the same time, the coast guard reports that a large leakage of oil has been discovered in the region and that several unidentified cargo ships have been sighted heading towards Härnösand. Our own troops, about the size of a battalion, reside in the proximity of Härnösand. The forces mainly consists of one tank company protecting the highway E4 approaching Härnösand from the southwest and one artillery formation located along the small road directly to the west of the city. Apart from these units, a staff company together with various resources for surveillance and reconnaissance are located in the center of Härnösand. Moreover, home guard patrols of varying size and equipment capabilities may be deployed locally on various places throughout the region.

![](/api/attachments/JY2BXW7W/fulltext/images/6b2f339bd6a2c039b71a88d76da4b8b84c5fb26985c572d96f3645bcfcb59480.jpg)  
Fig. 1. The map describes the blue battalion commander's view of the situation at the time for decision-making. The dotted arrows depict the red tank formation's choice to continue along the road versus its (potential) choice to travel through the terrain.

The (blue) commanders in Härnösand estimate, almost instantly, that the overall (red) enemy goal is to establish a bridgehead by gaining control over the harbor in Härnösand. This is a natural assumption as the Härnösand harbor is the only port in the area that allows for big vessels to approach in order to set off a large-scale invasion. The battalion's unmanned aerial vehicle (UAV) group is ordered to perform reconnaissance with focus on the main roads leading to Härnösand, i.e., the possible avenues of approach for other possible enemy units.

At 01:20 one of the two available UAVs spot a tank company southwest of Härnösand heading northeast on the highway E4. The battalion commander makes the assumption that the main goal for the tank company is to secure the bridge along the E4 to make it possible for more units to approach the city from the south at a later point of time.

At 01:30 a home guard patrol reports that enemy tanks have taken position at a petrol station located north of the city. At the same time the earlier mentioned bridge along the southwestern part of the E4 is being blown up by another home guard patrol.

At 01:32 the artillery unit located to the west of Härnösand directs fire towards the petrol station using coordinates that have been supplied by the home guard patrol. The home guard patrol later reports that a big fuel explosion has made the petrol station blow up as well as neutralizing several enemy tanks that were located within the petrol station at the time of the explosion. The tanks that are not damaged, about the size of a platoon, continue south.

At 01:45 reconnaissance personnel at the crossroad in Älandsbro, see Fig. 1, report that the remainder of the blown-up enemy tank company from the petrol station heads west while the intact enemy tank company continues south towards Härnösand.

## 2.2. The need for reasoning

At this point the blue battalion commander in Härnösand faces his first real problem where he needs to reason about the situation. Until now the commanders have been faced with several tasks that require the use of their units, C2 system, etc., but these tasks have all been straightforward with few real choices for the commanders to reason about.

The 01:45 report from Älandsbro, however, makes it apparent that the intact enemy tank company heading for Härnösand is approaching the city in order to, at one time or another, enter the city to seize control over it. It is also apparent that the enemy tanks heading west are left behind to take care of the blue artillery unit that, in the red commanders' view, needs to be neutralized. A fundamental principle in war, stated in the doctrine of most modern armies, is to never leave enemy forces behind as one advances.

The game-theoretic decision situation that has arisen concerns the red platoon heading west and is due to the incident at the petrol station that may indicate that the red tanks were in desperate need of fuel. There may, however, be other reasons to why one stops by at a petrol station. Moreover, even if there was a problem with the fuel, the tanks were maybe able to refuel before the petrol station was hit by artillery fire. The question regarding fuel becomes very important when about to give orders to the blue artillery unit regarding his course of action. If a tank is low on fuel it must use roads because of the many times higher fuel consumption required when moving through terrain.

The blue battalion commander has two possible courses of actions to propose to his artillery unit. Either he can prepare for a certain battle by digging trenches or he can choose to withdraw towards Härnösand using the road leading to the east. Digging trenches will compensate for the heavy enemy fire power and yield an even, but certain, battle. Withdrawal, on the other hand, is more risky. If the red tanks use the road and the blue artillery unit manages to get away, this will yield a small profit for the blue side who can gain from the information and people that are saved. However, if the blue artillery unit chooses to withdraw and the red tank platoon travels through the terrain and manages to intercept, the blue artillery unit will be annihilated and their weapons might be used for the forthcoming invasion of Härnösand.

The red commander is neither uncertain about the status of himself (out of fuel or not) nor the status of the blue unit. The eventual choice to either travel using the road or to go through the terrain has got to do with that he does not know whether the blue artillery unit chooses to dig trenches or to withdraw. Also, even if the tanks are not out of fuel it should not be taken for granted that the best choice is to use the terrain to accomplish an interception, as the red tank platoon will then use a large amount of his fuel supplies which may prove fatal later on. Several historical examples of the out of fuel scenario exist, with the sinking of the German battle-ship Bismarck during WW2 being a famous example [7].

## 3. Game-theoretic reasoning

The decision situation that arises in the Härnösand scenario is characterized by its dependency on other actors' beliefs, desires and intentions. Standard AI tools for solving decision-making problems in complex situations, such as dynamic decision networks and influence diagrams, are not applicable for these kinds of situations. Game theory [24], on the other hand, provides a mathematical framework designed for the analysis of agent interaction under the assumption of rationality. In game theory one tries to identify the game equilibria, as opposed to traditional utility maximization principles. A game component in multi-agent decision-making thus uses rationality as a tool to predict the behavior of other agents. In C2 the need for such a game component becomes obvious in order to obtain full situation awareness [30]. In small-scale situations requiring rapid reaction this need is on the other hand not as obvious and the game component is maybe not needed here, since agents' choices to a large extent are driven by standard operating procedures obtained by training and developed using off-line game analyses. On this level, like in helicopter dogfights, successful development of strategies has been obtained with look-ahead in extensive form, i.e., perfect information game trees with zero-sum payoffs as reported in Ref. [15].

Decision-making in environments where multiple agents make decisions based on what they think the other agents might do is a difficult problem. The use of game theory for agent design has so far been limited due to lack of understanding and lack of standard implementation methods. We believe, however, that these barriers will be overcome as more research is focused on the use of game theory for agent design. The widely used AI book by Russell and Norvig [27] added a visionary section on game theory just recently and special journal issues devoted to game theory for agent design has started to appear [9,26]. This indicates that the ideas are new and still need to be investigated more thoroughly.

One of the earlier mentioned barriers that do exist when using traditional game theory for agent design is that it assumes that a player will definitely play a Nash equilibrium strategy. In some applications, such as the management of (own) mobile sensors [14] or the construction of algorithms for efficient network capacity sharing [1], where the game is a designed mechanism, this assumption is true. However, these situations must be considered being a small subset when looking at all the uncertain situations that occur in our everyday life, where uncertainty regarding both other actors and the world as a whole must be accounted for. In this paper we aim at solving this problem using the Bayesian game technique which is described below. Other problems with game theory for agent design are the lack of methods for combining game theory with traditional agent control strategies [27] and the lack of standard computational techniques for game-theoretic reasoning [16].

The extensive form of a game is a tree structure, where a non-terminal node can describe a chance move by nature (random draw) or a move possible for one of the participants, while a leaf node represents the end of the game and its payoff after evolving through the path to it. The immediate descendants of a non-leaf represent the alternative outcomes of a chance move (in which case the node is associated with a probability distribution) or the set of actions available for the player in turn at this point. This is adequate for leisure games like chess, a perfect information game. The chess game tree does not fit into any computer, though. A deterministic game with full information, like generalized chess or checkers, can be completely solved if its game tree can be traversed, by bottom-up dynamic programming.

In games with imperfect information, the exact position in the game tree may not be known to players. This is the case in leisure games of cards, where the hand of a player is only available to herself. The determination of optimal strategies must use a game tree where the decision alternatives are the same for a whole information set, i.e., a set of nodes for a player where the information available to her is the same. As an example, at the first bid of a game of contract bridge, each of the possible distributions of the cards not seen by the player is in the same information set. The bottom-up evaluation does not work, because at the lower levels of the game tree the players have information on the hidden information that was communicated by their opponents' choices of moves (like the initial round of bidding in bridge). This situation is solved by putting the game on strategic form, which means that each combination of moves for all of a player's information-equivalent nodes in the tree, and all chance moves, are listed with their payoffs. The payoff matrix is typically impossibly large, and games of this type, like standard variants of poker and bridge, have no known optimal solution.

The concept of a Bayesian game is fairly complex [11]. A Bayesian game is a game with incomplete information, that is, at the starting point of the game the players may have private information about the game that the others do not know of. Also, each player expresses its prior belief about the other players as a probability distribution over what private information the other players might possess. The private information is modeled by assigning a type set for each player consisting of the possible types the player may possess.

## 4. Modeling decision-making in command and control

In this section we define the proposed game component using game-theoretic notation from Ref. [20]. The objective is to specify a game that is suitable for threat prediction in the C2 domain. Our building blocks rest on the following criteria: 1) that the agents' decisions are based on their belief regarding the other agents' prior information, and 2) that the game is made up from an underlying well-established and realistic probabilistic model of the situation. We achieve the first criterion by the use of a Bayesian game with incomplete information, and the second criterion by representing the current situation awareness by the use of an influence diagram.

The architecture consists of a probability distribution over the possible worlds, with each world encoded as an influence diagram according to Fig. 2. The whole architecture, depicted in Fig. 3, forms a game with incomplete information, i.e., a Bayesian game. The following steps constitute a brief description of the algorithm:

(1) We have a number of models of possible world states, encoded in the form of Bayesian game type profiles, that we need to consider. These models represent one agent's view of the other agents' views, i.e., it incorporates both the agent's own characteristics as well as the agent's subjective judgment of the other agents' characteristics. For example, an agent is probably certain regarding his own goals but less certain regarding the other agents' goals.

![](/api/attachments/JY2BXW7W/fulltext/images/3bcdf02e4e1ee699c55424dfac3b9d0b530ebdeebbbc5fe7b776b00a8a5d4716.jpg)  
Fig. 2. The C2 process modeled in an influence diagram. Terrain and doctrine data bases are examples of submodels that characterize a certain type profile.

![](/api/attachments/JY2BXW7W/fulltext/images/5ea163b03a98ba765161b6732ee53a998a5acde55e87634323415a4d95c5062d.jpg)  
Fig. 3. Architecture overview. Models are represented by influence diagrams that yield payoff values for a Bayesian game (see Fig. 5 for an example of the resulting game).

(2) Each model, depicted in Fig. 2, is represented by an influence diagram containing the agents' goals $( G _ { i } ) _ { ; }$ the agents' possible courses of actions (D<sub>i</sub>), the resulting world consequence (C ) and the agents' payoff (U ). Apart from these variables the influence diagram is connected to type profile specific subdiagrams containing terrain data bases, doctrine, etc.

(3) An important observation regarding the model in Fig. 2 that motivates the use of game theory is the fact that this model, seen as an ordinary influence diagram, does not account for situations when agents' try to make decisions that are influenced by other agents' decisions. That is, it is not capable of representing circular causal relationships between $D _ { 1 }$ and $D _ { 2 }$

(4) For each combination of the decision profile $D _ { 1 }$ $\ldots , D _ { n }$ we use the influence diagram to calculate utilities $U _ { 1 } , . . . , U _ { n }$ in order to create a strategic form game for each model.

(5) Using our prior belief regarding which model is accurate, we obtain a Bayesian game for the whole decision problem.

(6) Calculation of equilibria in the Bayesian game yields solutions for the decision variables $D _ { 1 } , . . . ,$ $D _ { n }$ in the form of mixed strategy Nash equilibria.

An underlying assumption for the above architecture is that the modified influence diagram in Fig. 2 is indeed a viable way to model the C2 process. We will not elaborate further about this issue but refer to previous work in Ref. [2,30]. The apparent gaming problem that arises in decision problems where multiple agents reason about each others' reasoning and the insufficiency of traditional AI techniques for modeling such situations is discussed further in for example Ref. [27].

## 5. Solving the Härnösand scenario

The Härnösand scenario possesses several levels of uncertainty which makes the situation ideal for gametheoretic reasoning. First of all, the blue player is uncertain regarding what game is actually being played, i.e., whether the red player is out of fuel or not. Modeling this prior information requires the use of a Bayesian game. The Bayesian property is often modeled using a historical chance node as a root node. This node differs from an ordinary chance node in that the outcome of this node has already occurred and is known to a subset of the players when the game model is formulated and analyzed. In our example there are only two edges going out from the root node. One of these edges corresponds to the extensive form game in Fig. 4(a) that models the situation when the red player has got enough fuel. The other edge corresponds to the extensive form game in Fig. 4(b) that models the out of fuel situation.

The uncertainty regarding the other player's decision is modeled via the use of information sets, i.e., the red player will not know in advance whether the blue player has chosen to dig trenches (D) or to withdraw (W) and therefore is uncertain about whether to try to intercept (T) or not (R), as his reward from this differs depending on the blue player's actions. The final expected payoffs depend on the opponents' beliefs and on our beliefs. In our model these beliefs are obtained from the influence diagram representing our current situation awareness, as laid out in Ref. [2].

We let $\alpha \in ( 0 ,$ , 1) denote the blue player's belief of the red player having enough fuel. Solving the game using the technique described by Harsanyi [11] involves introducing a historical chance node, a “move of nature,” that determines the red player's type, hence transforming the blue player's incomplete information about the red player into imperfect information. The Bayesian equilibrium of the game is then precisely the Nash equilibrium of this imperfect information game. The Harsanyi transformation of the Bayesian game is depicted in Fig. 5 on extensive form. Note that several decision nodes share the same label representing the uncertainties regarding players' types and choices. The normal way of solving such a game is to look at the strategic representation, as seen in Table 1.

![](/api/attachments/JY2BXW7W/fulltext/images/1f3e7032d8c354cea35428c0d2b803dfbca7e6b7585848b43c6a76cd2db377b2.jpg)  
Fig. 4. The resulting extensive game when the red force (a) has enough fuel and (b) when the red force is (almost) out of fuel.

![](/api/attachments/JY2BXW7W/fulltext/images/5b375e0ea25e27d5d20d756e6a1d46de72a13765a70d587e38156a5fc1c97b4e.jpg)  
Fig. 5. The Harsanyi transformation of the Bayesian game represented by the type profiles depicted in Fig. 4.

In order to solve the game, we first look for equilibria in pure strategies. $( [ D ] , [ T ] )$ is not an equilibrium because at this outcome there is an incentive for the red player to change her action to $R .$ The strategy profile ([D], [R]), however, is not a stable point in the game because here the blue player can benefit from performing W instead of $D .$ Once again, though, ([W ], [R]) cannot be an equilibrium of the game since the red player can get 3α−1 instead of only −1 by performing $T$ instead of R. At ([W ], [T ]), a requirement for the blue player to be unwilling to change from $W$ to D is that $1 - 3 \alpha \geq \alpha ,$ , which is true for $\alpha \leq 1 / 4$ Hence, for $\alpha \leq 1 / 4$ the pure strategy profile $( [ W ] , [ T ] )$ is the unique game equilibrium, and for $\alpha { > } 1 / 4$ there are no equilibria in pure strategies and we have to look for equilibria in mixed strategies.

For $\alpha { > } 1 / 4 ,$ we let $q [ D ] + ( 1 - q ) [ W ]$ and $s [ R ] + ( 1 - s ) [ T ]$ denote the equilibrium strategies for the blue and the red player respectively, where $q$ denotes the probability that the blue player digs trenches and s the probability that the red player decides to travel on roads. A requirement for an equilibrium for the blue player is that his expected payoff is the same for both $D$ and $W ,$ i.e.,

$$
\begin{array}{l} s \cdot 0 + (1 - s) \cdot \alpha = s \cdot 1 + (1 - s) \cdot (1 - 3 \alpha) \\ \Rightarrow s = \frac {4 \alpha - 1}{4 \alpha}. \end{array}
$$

Similarly, to make the red player willing to randomize between R and $T , R$ and $T$ must give her the same expected utility against $q [ D ] + ( 1 - q ) [ W ]$ so that

$$
\begin{array}{l} q \cdot 0 + (1 - q) \cdot (- 1) = q \cdot (- \alpha) + (1 - q) \cdot (3 \alpha - 1) \\ \Rightarrow q = \frac {3}{4}. \end{array}
$$

Since this determines the value of both $q$ and s uniquely, there is exactly one equilibrium point in the game for all values of $\alpha ,$ which is also a property of all constant-sum two-player games [4,23].

We can now use the equilibrium strategy of the imperfect information game in order to derive the Bayesian equilibrium of the Bayesian game. A Bayesian equilibrium specifies a randomized strategy profile containing one strategy $\sigma _ { i } ( \cdot | t _ { i } )$ for all combinations of players and types. Hence, the unique Bayesian equilibrium for the whole game is

$$
\left\{ \begin{array}{l} \sigma_ {\text { blue }} (\cdot | \text { blue }) = q [ D ] + (1 - q) [ W ] = 3 / 4 [ D ] + 1 / 4 [ W ], \\ \sigma_ {\text { red }} (\cdot | \text { red.enough fuel }) = s [ R ] + (1 - s) [ T ] \\ \qquad \qquad \qquad = (4 \alpha - 1) / (4 \alpha) [ R ] + 1 / (4 \alpha) [ T ], \\ \sigma_ {\text { red }} (\cdot | \text { red.out of fuel }) = [ R ], \end{array} \right.\tag{3}
$$

for $\alpha { > } 1 / 4$ and

$$
\left\{ \begin{array}{l} \sigma_ {\text { blue }} (\cdot | \text { blue }) = [ W ], \\ \sigma_ {\text { red }} (\cdot | \text { red.enough   fuel }) = [ T ], \\ \sigma_ {\text { red }} (\cdot | \text { red.out   of   fuel }) = [ R ], \end{array} \right.\tag{4}
$$

for $\alpha \leq 1 / 4$ . The solution graph is depicted in Fig. $^ { 6 , }$ showing how the equilibrium probabilities varies for different values of α.

From the red player's perspective, the intuition is that she should try to intercept with a greater probability when she is more likely to achieve a surprise effect, i.e., when the red player thinks the blue player thinks she is out of fuel she should, if possible, try to intercept with a greater probability. For $\alpha \leq 1 / 4$ the surprise effect is large enough to make the red player always try to intercept if her fuel permits.

From the blue player's perspective, his belief of the red player being able to intercept, $\operatorname { i . e . , \alpha , }$ and the probability that the red player actually tries to intercept, i.e., s(α), outweighs each other so that he tries to dig trenches or withdraw according to constant probabilities $q$ and $1 - q$ for $1 / 4 < \alpha \leq 1$ . For $\alpha \leq 1 / 4 ,$ , i.e., when he does not expect the red player to be able to intercept, the expected utility of a withdrawal becomes so large so that he always tries to withdraw.

It is important to look upon the Harsanyi transformed game matrix in Table 1 solely as an intermediary result which is used to solve the game. When analyzing the game, its origins must be taken into account. If one tries to interpret the Harsanyi transformed game matrix without considering the game's origins, it probably feels strange that the game matrix contains utility values that are functions of $\alpha ,$ i.e., a variable describing the blue player's belief of something the red player already knows with certainty. Instead, considering the origins of α, one should interpret the Harsanyi transformed matrix as the model that gives rise to the rational course of action given a subjective judgment of α. Hence, for the blue player α constitutes his own estimation regarding the red player's fuel situation. For the red player, on the other hand, α constitutes her estimate of the blue player's estimate. Therefore, despite that the true value of α is already known by the red player, α will still affect the blue player's rational course of action and, hence, also the red player's rational course of action.

The strategic form of the game in Fig. 5

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">red</td></tr><tr><td>R</td><td>T</td></tr><tr><td rowspan="2">blue</td><td>D</td><td>0, 0</td><td> $\alpha, -\alpha$ </td></tr><tr><td>W</td><td>1, -1</td><td>1-3 $\alpha$ , 3 $\alpha$ -1</td></tr></table>

![](/api/attachments/JY2BXW7W/fulltext/images/fc4dfc149504dde2055f56bbf0c11c3f4b4fe5c93f83f73d0e65cbe8f21b225f.jpg)  
Fig. 6. The graph shows how two players' equilibria, with probabilities indicated by q(α) and s(α) respectively, vary depending on their prior beliefs about the other player's private information α. The players differ in that the first player is speculating about what the second player knows, whilst the second player is speculating about the first player's speculation.

## 6. Solution interpretation

Nash equilibria, in the form of mixed strategies, as a solution to decision problems require a moment of thought. On the one hand, it is easy to argue that the equilibrium strategy is theoretically sensible. After all, the notion of Nash equilibria, building on the concept of rationality, defines precisely this. By using the idea of Bayesian games we are able to create alternative models regarding agents that are in some way “irrational.” Thus, by using Bayesian games we can counterattack any objections on the existing model by simply extending the model with a new submodel that models the objection in question. Of course, this also requires assigning a prior probability to the new submodel and re-evaluating the prior probabilities for the existing submodel, which makes sense if someone comes up with an objection (which is interpreted as a new model that we have not thought of before). If the objection is independent of the existing models, normalization is the natural way to reassign probabilities. Otherwise it is natural to let the prior probability of the new model be represented by a reduction of prior probabilities of the model or the models that it depends on. In most cases we believe that it is appropriate to have a separate model for the “uncertain case” that takes care of whatever we have not thought of. In that case the new model, provided it is independent of other existing models, typically reduces our overall uncertainty regarding the situation and thus causes a reduction of prior probability for the earlier mentioned “uncertain case.” Models that takes care of the rest, i.e., that represent options or possibilities that we are not yet aware of, are often found in proposed architectures for multi-agent modeling, see for example Ref. [10] where irrational behavior as well as lack of information is modeled in so-called “no information models.”

On the other hand, although representing the theoretically rational course of action, the Nash equilibrium poses several concerns regarding its interpretation. Looking at the Härnösand scenario, it is interesting to see how q and s vary depending on α which is depicted in the diagram in Fig. 6, i.e., how the solution to our decision problem varies significantly depending on our subjective beliefs regarding the out of fuel situation. How do we convince a commander that he should decide what to do by throwing a die that varies depending on q(α)? As an example, consider the situation when we do not know anything and assign equal probabilities to the two models (fuel or out of fuel). Then the blue player should dig trenches with probability q(1/2)=3/ 4 and the red player should choose to travel by roads with probability s(1/2)=1/2 although his fuel supply would allow for an interception. The conclusion regarding the Härnösand scenario is that a simple problem yields a solution that is difficult to understand intuitively. Unfortunately, this is quite typical (see for example Ref. [2] for another example) and we need to address the question of how to use the solution in a sensible way. To actually throw the die is part of the solution and if this is not performed the commander is not rational and, hence, will be outperformed by a rational opponent that is capable of modeling this behavior. Maybe it is easier to accept the opponent's randomized strategy as a prediction. Then the optimality of one's own randomized strategy is fairly easy to establish.

A modern interpretation of mixed strategy Nash equilibria stemming from behavioral game theory is that players need not actually randomize, as long as other players cannot guess what they will do [3]. Rather than considering the opponent's strategy being the throw of a die, one considers “an equilibrium in beliefs.” The underlying idea is to consider the opponent being part of a population of decision-makers who choose their strategies according to a frequency that corresponds to the mixed strategy equilibrium. Hence, the opponent's choice of strategy will coincide with his equilibrium strategy on average, making the players indifferent about which strategy they play. While the human perspective that characterizes behavioral game theory is opposite to that of the C2 decision-making perspective, this modern interpretation remains a tempting way to reason about an equilibrium solution.

## 7. Computational issues

Although the example in Section 5 was fairly easy to solve, it should be noted that this is often not the case. Solution methods for game-theoretic problems are, in most cases, intractable for the generic case. Two-player zerosum games form the exception. Since the two players' payoff matrices, A and −A respectively, are identical apart from the sign, the problem of calculating optimal mixed strategies x and y for the row and column player respectively can be solved via a polynomial time linear programming algorithm where the row player aims to maximize and the column player aims to minimize the sum $x ^ { T } A y .$ Apart from being computationally easy to find, the celebrated Minimax Theorem [4,23] states that the resulting equilibrium point is unique.

The most well-known solution method for general-sum two-player games, the Lemke–Howson algorithm [17,29], solves a linear complementarity problem [6]. The computational complexity for finding one equilibrium is still unclear. We know, according to Nash's theorem [22], that at least one equilibrium in mixed strategies exists but it is problematic to construct one. Lemke–Howson exhibits exponential worst case running time for some, even zerosum, games. However, this does not seem to be the typical case. Interior point methods that are provably polynomial are not known for linear complementarity problems arising from games [29]. Methods amounting to examining all equilibria, such as finding an equilibrium with maximum payoff, have unfortunately been proven NP-hard [8].

The perhaps most frustrating, but yet challenging, observation for the applied game-theorist is that most research and development seems to be directed towards finding one equilibrium instead of finding them all. Moreover, if one manages to find all equilibria the problem remains to rank these equilibria versus each other. Ranking strategies based on for example Pareto efficiency exist, but there does not seem to be a consensus in the literature. Ranking methods coupled with solution methods as a means to reduce the optimization problem in order to get hold of the right equilibrium are yet to be developed.

## 8. Conclusions

Gaming is inevitably an inherent part of command and control (C2) decision-making. In fact, for commanders wishing to optimize their decisions in complex multi-agent environments, understanding the rules of the game is often the same thing as understanding the decision problem itself. After all, this is what long-term planning is all about, i.e., taking into account one's knowledge or expectation of other decision-makers' behavior to form a systematic description of the outcomes that may emerge. By extending readily available and accepted single-agent reasoning engines in the form of Bayesian networks and its extensions into a “game component” we have constructed an architecture that we believe is well suited for C2 reasoning.

More realistic and complex scenarios are required to obtain full understanding of the difficulties and the possibilities that a game-theoretic solution yields. The solution concept in the form of mixed strategy Nash equilibria rests on well-established assumptions, but unfortunately the solution itself is often nontrivial and therefore some level of understanding of the underlying concepts is required. Further research is needed regarding how to establish such understanding. Our belief is that the development of game-theoretic tools must be made in parallel with the development of planning methods for C2 decision-making which will facilitate in establishing understanding as well as ensuring that the result matches the actual decision-making process. We believe the latter to be an important usability aspect that needs to be considered in further research and development.

Our ideas assume that each decision-maker is rational in the sense that he is aware of his alternatives, forms expectations about any unknowns, has clear preferences, and chooses his action deliberately after some process of optimization. The assumption of rationality is not undisputed, being under perpetual attack by experimental psychologists who point out severe limits to its application [25]. However, the use of Bayesian games can to a large extent compensate for irrational behavior by letting the commander maintain a belief over several, possibly “irrational,” opponent models. Hence, we claim that irrationality should be modeled in a rational manner and, likewise, that the solution should be interpreted in light of this rationally modeled irrationality

## Acknowledgments

Help with military correctness and realism is acknowledged to Magnus Sparf, formerly engaged jointly by the Swedish Armed Forces and the Swedish Defence Research Agency. The narrative in the Härnösand scenario has been developed in cooperation with Ronnie Johansson and Robert Suzić from the Decision Support Group at the Royal Institute of Technology. Furthermore, we would like to acknowledge the help of Stefan Arnborg and Klas Wallenius at the Royal Institute of Technology and Per Svensson at the Swedish Defence Research Agency for commenting on drafts at different stages. Lastly, the author wishes to greatly acknowledge the help from Mikael Stralje for painting the scenario map depicted in Fig. 1.

## References

[1] R. Azoulay-Schwartz, S. Kraus, Negotiation on data allocation in multi-agent environments, Autonomous Agents and Multi-Agent Systems 5 (2) (2002) 123–172.

[2] J. Brynielsson, S. Arnborg, Bayesian games for threat prediction and situation analysis, in: P. Svensson, J. Schubert (Eds.), Proceedings of the Seventh International Conference on Information Fusion (FUSION 2004), vol. 2, 2004, pp. 1125–1132, Stockholm, Sweden.

[3] C.F. Camerer, Behavioral game theory: experiments in strategic interaction, The Roundtable Series in Behavioral Economics, Princeton University Press, New Jersey, 2003.

[4] V. Chvátal, Linear Programming, W.H. Freeman and Company, New York, 1983.

[5] T.P. Coakley, Command and Control for War and Peace, National Defense University Press, Washington, District of Columbia, 1991.

[6] R.W. Cottle, J.-S. Pang, R.E. Stone, The Linear Complementarity Problem, Academic Press, 1992.

[7] E. Durschmied, The Hinge Factor: How Chance and Stupidity Have Changed History, Coronet Books, London, United Kingdom, 1999.

[8] I. Gilboa, E. Zemel, Nash and correlated equilibria: some complexity considerations, Games and Economic Behavior 1 (1) (1989) 80–93.

[9] P.J. Gmytrasiewicz (Ed.), Special issue on decision theory and game theory in agent design, Decision Support Systems, vol. 39 (2), 2005, pp. 151–252.

[10] P.J. Gmytrasiewicz, E.H. Durfee, Rational coordination in multiagent environments, Autonomous Agents and Multi-Agent Systems 3 (4) (2000) 319–350.

[11] J.C. Harsanyi, Games with incomplete information played by “Bayesian” players, Management Science 14 (3,5,7) (1967–1968) 159–182, 320–334, 486–502.

[12] J.D. Hicks, G. Myers, A. Stoyen, Q. Zhu, Bayesian-game modeling of C2 decision making in submarine battle-space situation awareness, 2004 Command and Control Research and Technology Symposium, San Diego, California, 2004.

[13] R.A. Howard, J.E. Matheson, Influence diagrams, in: R.A. Howard, J.E. Matheson (Eds.), Readings on the Principles and Applications of Decision Analysis, Strategic Decisions Group, Menlo Park, California, 1984, pp. 721–762.

[14] R. Johansson, N. Xiong, H.I. Christensen, A game theoretic model for management of mobile sensors, Proceedings of the Sixth International Conference on Information Fusion (FUSION 2003), Cairns, Australia, 2003, pp. 583–590.

[15] A. Katz, B. Butler, “Game commander” — applying an architecture of game theory and tree lookahead to the command and control process, Proceedings of the Fifth Annual Conference on AI, Simulation, and Planning in High Autonomy Systems (AIS94), Gainesville, Florida, 1994.

[16] D. Koller, A. Pfeffer, Representations and solutions for gametheoretic problems, Artificial Intelligence 94 (1) (1997) 167–215.

[17] C.E. Lemke, J.T. Howson Jr., Equilibrium points of bimatrix games, Journal of the Society for Industrial and Applied Mathematics 12 (2) (1964) 413–423.

[18] J. Llinas, C. Bowman, G. Rogova, A. Steinberg, E. Waltz, F.E. White Jr., Revisiting the JDL data fusion model II, in: P. Svensson, J. Schubert (Eds.), Proceedings of the Seventh International Conference on Information Fusion (FUSION 2004), vol. 2, 2004, pp. 1218–1230, Stockholm, Sweden.

[19] K.P. Murphy, Dynamic Bayesian networks: Representation, inference and learning, Ph.D. thesis, University of California, Berkeley (2002).

[20] R.B. Myerson, Game Theory: Analysis of Conflict, Harvard University Press, 1991.

[21] S. Nadkarni, P.P. Shenoy, A causal mapping approach to constructing Bayesian networks, Decision Support Systems 38 (2) (2004) 259–281.

[22] J.F. Nash, Non-cooperative games, Annals of Mathematics 2 (54) (1951) 286–295.

[23] J.v. Neumann, Zur Theorie der Gesellschaftsspiele, Mathematische Annalen (1928) 295–320.

[24] J.v. Neumann, O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press, New Jersey, 1944.

[25] M.J. Osborne, A. Rubinstein, A Course in Game Theory, MIT Press, Cambridge, Massachusetts, 1994.

[26] S. Parsons, M. Wooldridge, Game theory and decision theory in multi-agent systems, Autonomous Agents and Multi-Agent Systems 5 (3) (2002) 243–254.

[27] S.J. Russell, P. Norvig, Artifical Intelligence: A Modern Approach, Second Edition, Prentice Hall, Upper Saddle River, New Jersey, 2003.

[28] A. Steinberg, C. Bowman, F.E. White Jr., Revisions to the JDL data fusion model, Proceedings of SPIE AeroSense (Sensor Fusion: Architectures, Algorithms, and Applications III), vol. 3719, 1999, pp. 430–441, Orlando, Florida.

[29] B.v. Stengel, Computing equilibria for two-person games, in: R.J. Aumann, S. Hart (Eds.), Handbook of Game Theory with Economic Applications, Handbooks in Economics, vol. 3, Elsevier Science, 2002, pp. 1723–1759, Ch. 45.

[30] K. Wallenius, Support for situation awareness in command and control, in: P. Svensson, J. Schubert (Eds.), Proceedings of the Seventh International Conference on Information Fusion (FU-SION 2004), vol. 2, 2004, pp. 1117–1124, Stockholm, Sweden.

[31] J.W. Weibull, Testing game theory, in: S. Huck (Ed.), Advances in Understanding Strategic Behaviour: Game Theory, Experiments and Bounded Rationality, Palgrave Macmillan, Basingstoke, United Kingdom, 2004, pp. 85–104, Ch. 6.

[32] F.E. White Jr., A model for data fusion, Proceedings of the First National Symposium on Sensor Fusion, vol. 2, 1988, Orlando, Florida.

![](/api/attachments/JY2BXW7W/fulltext/images/fcc3491ede5f99014c6ff2f7c6c2b6bb61cd82efb6dc620f5f1a92ecd7532756.jpg)  
Joel Brynielsson is an assistant professor at the Swedish National Defence College. He earned his MSc degree in Computer Engineering and his PhD degree in Computer Science from the Roya Institute of Technology in Stockholm, Sweden. His research interests are in information and uncertainty management in command and control systems with publications appearing in journals and conferences devoted to information fusion, decision support, command and control, operations research, microworld research, and model-  
ing and simulation.
