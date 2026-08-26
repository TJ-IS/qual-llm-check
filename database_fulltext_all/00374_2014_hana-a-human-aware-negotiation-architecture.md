---
otero_id: 374
otero_key: "XMT56ZUV"
title: "HANA: A Human-Aware Negotiation Architecture"
authors: "Angela Fabregues; Carles Sierra"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Angela Fabregues ⁎, Carles Sierra

Artificial Intelligence Research Institute (IIIA-CSIC), Campus Universitat Autònoma de Barcelona, E-08193 Bellaterra, Spain

a r t i c l e i n f o

Available online 5 June 2013

Keywords: Multiagent systems Agent architecture Automated negotiation Practical reasoning Search&negotiation Diplomacy Game

## a b s t r a c t

In this paper we propose HANA, a software architecture for agents that need to bilaterally negotiate joint plans of action in realistic scenarios. These negotiations may involve humans and are repeated along time The architecture is based on a BDI model that represents the uncertainty on the environment as graded beliefs, desires and intentions. The architecture is modular and can easily be extended by incorporating different models (e.g. trust, intimacy, personality, normative…) that update the set of beliefs, desires or intentions. The architecture is dynamic as it monitors the environment and updates the beliefs accordingly. We introduce an innovative search&negotiation method that facilitates HANA agents to cope with huge spaces of joint plans. This method implements an anytime search algorithm that generates partial plans to feed the negotiation process. At the same time the negotiation guides the search towards joint plans that are more likely to be accepted.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Since the development of software shifted towards networked systems in the mid 90s a lot of work has been done on automated bilateral negotiations [13,26]. In most previous work autonomous software agents, usually sel<sup>fi</sup>sh, interact using utility maximisation strategies [20,27,37]. These strategies usually work well when negotiation happens between software agents but not necessarily when humans are involved in the negotiations as recent work shows [25]. This is in part because humans do not follow a constructivist sort of rationality [8,41]. For instance, human decisions depend a lot on their social relationships [40], on emotions [14] and are contextualised in a particular culture [15].

Our long term research goal is to build software agents capable of negotiating with humans in complex real scenarios, more concretely, on how to negotiate joint plans of action among software agents and humans when bilateral negotiations can be intermingled. In this work we contribute to this agenda by formally describing the negotiation problem and by providing a concrete agent architecture. The architecture contains a number of elements that make it suitable for non-constructivist negotiations — by incorporating emotions, and apt for negotiating over large spaces of joint plans — by concurrently negotiating and searching for solutions. The architecture is inspired by an ecological type of rationality [18] as developed in the LOGIC theory of agency [40] and goes beyond it by proposing a concrete computational solution.

More concretely, we address in this paper the complex problem of simultaneous, repeated and bilateral negotiations in competitive environments. The agents are either software or human agents that compete but can occasionally co-operate. The negotiation objects are joint plans of action. We are specially interested in negotiation domains that have a very large set of potential joint action plans as these are those with potential commercial interest (e.g. time tabling, team formation, supply chain management, gaming). In these scenarios, agents (and humans) need to negotiate joint action plans to improve their outcome. For instance, two teachers swapping time slots in their class schedules, or two members of a potential team negotiating the tasks to be performed. The environment is generally observable but the internal state of the other agents and their negotiations are usually private, that is, every agent can see the messages that it sends or receives but not the messages exchanged between any two other agents. In open systems, that is, systems that allow unrestricted access of autonomous entities (either software agents or humans), reaching agreements on joint action plans is the way to <sup>fi</sup>gure out what our counterparts will do, and even this is only to a certain extent as in some domains defection is possible. For instance, in Diplomacy, the case study used in this paper, a promise made by a player to perform a certain action may not materialise.

Negotiations are usually time framed. There is a deadline by which a negotiation process has to be <sup>fi</sup>nished. When these deadlines are tight, negotiators need to search quickly for good enough negotiation proposals instead of looking for optimal proposals. For large solution spaces it is either not possible or too long to <sup>fi</sup>nd them. This is, in fact, very common in humans' everyday life. Humans do not hesitate to take good enough decisions instead of waiting to be sure that the decision to take is the best one. Humans behave well in uncertain and competitive environments, as we are unsure of what the others will do and taking decisions quickly may be advantageous as the more time we wait the less opportunities to close a deal may be there. If an agent waits too long others may have reached agreements that are incompatible with the plans the agent likes.

The scenarios we are interested in witness repeated negotiations, for instance teachers negotiate every semester, or members of teams negotiate tasks for each problem to solve. These repeated interactions permit agents to build relationships, check whether the agreements are kept and act accordingly. If an agent breaks an agreement, it may become untrustworthy and the other agent involved in the agreement may penalise it [21,24]. A good way to penalise an agent is ignoring it, rejecting every proposal it makes as it makes little sense to reach agreements with someone that is untrustworthy: it will probably break the deal.

In summary, we address the problem of simultaneous bilateral negotiation of joint plans of action in competitive environments with repeated negotiation encounters and repeated rounds of plan execution. In these environments negotiation speed is crucial because as time goes by the number of available joint plans that can be accepted decreases.

The paper is structured as follows. We start providing a formal speci<sup>fi</sup>cation of the problem including the negotiation protocol and our case study in Section 2. Then, we introduce the agent architecture in Section 3 and describe its components in Sections 4, 5 and 6. Finally, we conclude with a discussion and future work in Section 7.

## 2. Resource negotiation problems

In this section we formalise bilateral resource negotiation problems (RNP), that is, scenarios where agents negotiate about which actions to perform on the resources they control. The environment is dynamic, as it changes due to the uncontrollable actions of others. At each point in time its state contains a partition of the resources where each set of the partition corresponds to the resources controlled by a particular agent. The actions executed by agents make the environment evolve. We model this evolution as a transition function between environment states. We assume without loss of generality that actions are performed synchronously at particular points in time. Also, we assume that negotiations between agents are iterative over a two-step process: (i) agents sign agreements on what actions to perform, and (ii) they execute the actions of the agreements. In the following two subsections we provide the formal speci<sup>fi</sup>cation of the environment and the negotiation protocol, and in the last subsection we introduce the game Diplomacy as an example of RNP. Diplomacy will be the case study used throughout the paper.

## 2.1. Environment

We consider environments that are fully observable and regulated by a set of rules (physical or otherwise) that determine their evolution. Environments are populated by agents A that control resources R and are always in one of several possible states.

De<sup>fi</sup>nition 1. Given a set A of agents and a set R of resources, an environment state ${ \pmb { \omega } } \subseteq { \sf A } \times { \pmb { R } }$ is a set of agent–resource pairs. We denote by W the set of all possible environment states. that is $W = 2 ^ { \tt A \times R } .$

$\langle \alpha , r \rangle \in \omega$ means that agent α controls resource r and thus is the only agent that can act upon it.<sup>1</sup> We assume the existence of a <sup>fi</sup>nite set of operators Op that agents can apply to the resources they control. For instance, consuming the resource or transforming it. We thus de<sup>fi</sup>ne the set of possible actions as follows.

De<sup>fi</sup>nition 2. The set of actions is the set $A = \mathsf { A } \times O p \times R .$

We restrict the model to environments where no more than one operator can be applied to a resource simultaneously. This naturally leads to the de<sup>fi</sup>nition of compatibility between actions.

De<sup>fi</sup>nition 3. Two actions $a , b \in A$ such that $a = \langle \alpha , o p _ { a } , r _ { a } \rangle$ and $b =$ $\langle \beta , ~ o p _ { b } , ~ r _ { b } \rangle$ , are compatible, denoted by comp(a, b), if and only if $o p _ { a } = o p _ { b }$ implies $r _ { a } \neq r _ { b } .$

Controlling a resource means that only the agent that controls the resource can act upon it. This is our notion of action feasibility.

De<sup>fi</sup>nition 4. An action $a = \langle \alpha ,$ op, $r ) \in A$ is feasible in state $\omega \in W ,$ denoted by feasible(a, ω), if and only $i f \langle \alpha , r \rangle \in \omega$

Actions are naturally grouped in sets, that we call plans, that without losing generality we can assume are executed at a given instant of time. Note that an agent can control more than one resource.

De<sup>fi</sup>nition 5. A plan $p \subseteq A$ is a set of actions. The set of all possible plans is denoted by $P = 2 ^ { A }$

We extend the notion of feasibility to plans in a natural way.

De<sup>fi</sup>nition 6. Given a state $\omega \in W$ we say that plan $p \in P$ is feasible in state ω, denoted feasible(p, ω), if and only if for all a $. b \in p ,$ feasible(a, ω) and comp(a, b) hold. The set of all feasible plans in state ω is denoted by $P ^ { \omega } .$

Two feasible plans are compatible if their actions are pair-wise compatible. That is, if its union is feasible.

De<sup>fi</sup>nition 7. Given a state ω ∈ W and plans $p , q \in P ,$ we say that plans p and q are compatible, denoted comp(p, q), if and only if their union is feasible, that $i s , \mathsf { c o m p } ( p , q ) \Leftrightarrow p \cup q \in P ^ { \omega }$

When an action is selected for each resource the plan is complete.

De<sup>fi</sup>nition 8. Given a state $\omega \in W$ and a plan $p \in P ,$ we say that plan p is a complete plan for ω if and only if feasible(ω, p) holds and for all $\langle \alpha , r \rangle \in \omega$ then 〈α, op, r〉 ∈ p for some $o p \in O p .$ . We denote the set of all complete plans for state ω by $\overline { { P } } ^ { \omega } \subseteq P ^ { \hat { \omega } }$ and by $\overline { { P } } _ { \alpha } ^ { \omega }$ the projection of complete plans for α.

Now we have all the ingredients to de<sup>fi</sup>ne environments as a type of deterministic transition system. That is, as a <sup>fi</sup>nite state machine with an initial state, with a set of <sup>fi</sup>nal states, and with complete plans labelling the arcs between states.

De<sup>fi</sup>nition 9. A state transition system is a tuple

$$
\Omega = \left\langle \mathcal {A}, R, O p, W, P, \mathbf {T}, \omega_ {0}, W _ {f} \right\rangle
$$

where:

– A is a set of agents

– R is a set of resources

$$
- W = 2 ^ {A \times R} i.
$$

$- \ P = 2 ^ { \mathsf { A } \times O p \times R } \ i$ is a set of plans

– T: W × P → W is a transition function such that $\mathbf { T } ( \omega , p )$ is defined for all p∈P<sup>ω</sup>

$$
- \omega_ {0} \in W
$$

– W p W is the set of <sup>fi</sup>nal states.

The evolution of such a transition system is determined by a history of complete plans<sup>2</sup> being executed moving the state of the system away from the initial state and eventually reaching a <sup>fi</sup>nal state.

De<sup>fi</sup>nition 10. Given a transition system $\Omega = \langle \mathsf { A } , R , O p , W , P , \mathsf { T } , \omega _ { 0 } , W _ { f } \rangle$ a history is a sequence of complete plans $H = \langle p _ { 0 } , p _ { 1 } , . . . , p _ { n } \rangle ,$ such that for all $0 < i < n , \mathrm { \bf ~ T } ( . . . ( \mathrm { \bf T } ( \omega _ { 0 } , \mathrm { \bf ~ p } _ { 0 } ) , . . . ) , \mathrm { \bf ~ p } _ { i - 1 } ) = \omega _ { i }$ and $p _ { i } { \in } \overline { { P } } ^ { { \omega } _ { i } }$ . A history then implicitly defines an environment state history that is a sequence of states $W _ { H } = \langle \omega _ { 0 } , { \bf T } ( \omega _ { 0 } , p _ { 0 } ) , { \bf T } ( { \bf T } ( \omega _ { 0 } , p _ { 0 } ) , p _ { 1 } ) , . . . \rangle$ that we refer to as $W _ { H } = \langle \omega _ { 0 } , \omega _ { 1 } , \omega _ { 2 } . . . \rangle .$

## 2.2. Negotiation protocol

We de<sup>fi</sup>ne the negotiation in an RNP to be bilateral and satisfy a particular protocol. As an environment contains many agents, multiple bilateral negotiations can take place even simultaneously. The set of plans over which two agents negotiate is the set of feasible plans containing just actions performed by them. The plans involving up to two agents are called negotiation options, or options to simplify.

De<sup>fi</sup>nition 11. A feasible plan $\delta \in P ^ { \omega }$ is called a negotiation option $i f$ and only if

$$
0 <   | \{\alpha \in \mathcal {A} | \langle \alpha , o p, r \rangle \in \delta \} | \leq 2.
$$

We denote by ${ \mathcal { O } } ^ { \infty } \subseteq P ^ { \omega }$ the set of negotiating options in state ω and by $\mathcal { O } _ { \alpha , \beta } ^ { \omega } \subseteq P ^ { \omega }$ <sup>O</sup>the negotiation options involving α and $\beta .$

When two agents enact a negotiation protocol, they propose options that involve the two agents. Agents alternate on the sending of proposals and accepting or rejecting them until time expires. The possible messages exchanged between two agents are called negotiation utterances.

De<sup>fi</sup>nition 12. Given a transition system $\Omega = \langle \mathrm { A } , \boldsymbol { R } , O p , \boldsymbol { W } , P , \mathbf { T } , \omega _ { 0 } , \boldsymbol { W _ { f } } \rangle , a$ negotiation utterance in a state ω ∈ W is a tuple $\mu = \langle \theta , \alpha , \beta , \delta \rangle$ where $\theta \in \{ { \mathrm { p r o p } } 0 { \mathrm { s e } } ,$ , accept, reject}, $\alpha \in \mathtt { A }$ is the source and $\beta \in \mathsf { A }$ is the receiver of the utterance and $\delta \in \mathcal { O } _ { \alpha , \beta } ^ { \mathrm { c o } }$ . We denote by $M _ { \alpha , \beta } ^ { \mathrm { { \omega } } }$ the set of all possible <sup>O</sup>negotiation utterances between α and $\beta$ in state ω.

In the following we indistinctively represent utterances as tuples or predicates, e.g. 〈propose, α, β, $\delta \rangle \equiv p r o p o s e ( \alpha , \beta , \delta )$ . We de<sup>fi</sup>ne negotiation dialogues as sequences of utterances sorted by time.

De<sup>fi</sup>nition 13. Given a transition system Ω, a negotiation dialogue Ψ in state ω between α and β is a sequence $\Psi = \langle \mu _ { 0 } , \mu _ { 1 } , \dots , \mu _ { n } \rangle$ such that $\mu _ { i } \in M _ { \alpha , \beta } ^ { \mathrm { c o } }$ for all $0 \leq i \leq n .$

The negotiation protocol illustrated in Fig. 1 determines what can be said and in which order. Dialogues are formed as sequences of utterance so that each one is feasible with respect to the protocol. The next de<sup>fi</sup>ni tion determines what utterances are feasible given a partial dialogue.

De<sup>fi</sup>nition 14. Given a state $\omega \in W ,$ a dialogue $\Psi = \langle \mu _ { 0 } , \mu _ { 1 } , \dots , \mu _ { n - 1 } \rangle$ and an utterance $\mu _ { n } = \langle \theta , \alpha , \beta , \delta \rangle$ we say that $\mu _ { n }$ is feasible for dialogue Ψ, denoted by feasible(Ψ, μ ), if and only if:

• Ψ = 〈〉 ⇒ θ = propose

$$
\bullet \mu_ {n - 1} = \langle \text { propose }, \beta , \alpha , \delta \rangle \Rightarrow \theta \neq \text { propose }
$$

$$
\bullet \mu_ {n - 1} \neq \langle \text { propose }, -, -, \rangle \Rightarrow \theta \neq \text { propose }
$$

![](/api/attachments/XMT56ZUV/fulltext/images/d2f48751cf2e46f923367f47194d19ba6c7bb6ed7017590bb004d5708f4b0897.jpg)  
Fig. 1. Negotiation protocol. Proposals are replied by accepts and rejects. It is not possible to send a proposal when a previous one is not yet replied. [t<sub>max</sub>] represent the end of the negotiation round.

The outcome of a successful negotiation that ended with an accept is a set of commitments on future actions to be performed by the negotiating agents. When an option being offered by agent α is accepted by agent β, it means that agents α and β commit to perform their actions in the option.

De<sup>fi</sup>nition 15. Given a negotiation dialogue $\Psi = \langle \mu _ { 0 } , \mu _ { 1 } , \dots , \mu _ { n } \rangle$ we say that an action $a \in A$ is a commitment $i f \mu _ { i } = \langle a c c e p t , . . , . . , \delta \rangle \in \Psi$ and $a \in \delta .$ We denote by $C ^ { \Psi }$ the set of commitments in Ψ.

## 2.3. Case study: Diplomacy

To illustrate the application of the agent architecture to a concrete case and to perform experiments we use The Diplomacy $\mathsf { G a m e } . ^ { 3 }$ It is an example of the class of problems we intend to solve. It involves several players that repeatedly negotiate. All players perform their actions at the same time and the actions are made public so anyone can check whether its negotiating counterparts honoured the commitments reached at negotiation time. Its popularity,<sup>4</sup> the absence of random moves, the key role of negotiations during the game and the existence of literature on the strategy and tactics<sup>5</sup> make it the perfect case study to study concurrent bilateral negotiations. To perform experiments involving humans and software agents we have developed a testbed based on this game called DipGame that is freely available at http://www.dipgame.org [9,11].

Diplomacy is played by seven players that control units spread over a map of Europe. Each player incarnates one of seven Great Powers: England, France, Italy, Germany, Austria, Russia and Turkey. The map is divided into several provinces that can be occupied by at most one unit. Players should strategically move their units over the map in order to build more units and thus eventually conquer Europe, which in practical terms means controlling at least eighteen provinces. The game spans several years and a year is composed of different phases. We focus on the movement phase of each year when players decide which movements should each one of their controlled units perform. The allowed movements of a unit are: (i) to hold, (ii) to move to an adjacent province, (iii) to hold and support a holding unit, and (iv) to hold supporting a moving unit. Supports are the only way to strengthen a unit that takes part in a battle. A battle happens when two (or more) units aim at being in the same province as a result of their movements (unit orders). As mentioned before, the announcement of orders is simultaneous. The movements over the board and the outcome of battles affect the creation of new units and thus determine the progress of players in the game. An in-depth description of the game can be found in [38].

Diplomacy is an RNP. The agents are the players (powers) and the units are the resources that they control. The operators that can be applied to resources are the different types of orders, that is, the name of unit movements according to the rules of the game (http:// en.wikibooks.org/wiki/Diplomacy/Rules). Unit orders are the actions. During a movement phase the agents concurrently enact bilateral negotiations to reach agreements over the movements that they may jointly perform (e.g. getting the support of another player's unit to strengthen one of our units that will most probably get into battle in exchange of moving another of our units away from a certain province). At the end of a negotiation round all the agents announce their actions and as a consequence the board state changes.

The negotiation that takes place during the movement phases is usually performed in a natural language – English, for instance – as it is a game that is normally played by humans. The DipGame testbed contains a web application that allows people to talk to other people and to software agents by using a formal language. The formal language is a standard of communication among software agents using the testbed.<sup>6</sup> A standard is needed as software agents may be developed by different programmers. The testbed incorporates a translation library from (a reduced set of) English to the formal language and vice versa [9]. To illustrate the notion of plan we use the simplest of the formal languages and a simple ontology that only allows to represent orders [11].

In Fig. 2 we graphically represent two plans, in Fig. 2a an individual plan for France and in Fig. 2b a joint plan between Italy and Austria.

The plan for France is to move from Paris to Burgundy, from Brest to Mid-Atlantic Ocean and from Marseilles to Spain. Thus the plan p = {a , a , a } is a set of movements expressed in the formal language as<sup>7</sup>:

$$
a _ {1} = \operatorname{mto} (\text { Unit } (\text { fra }, \text { Region } (\text { par }, \text { amy })), \text { Region } (\text { bur }, \text { amy }))
$$

a = mto(Unit(fra, Region(bre, <sup>fl</sup>t)), Region(mao, sea))

$$
a _ {3} = \operatorname{mto} (\text { Unit } (\text { fra }, \text { Region } (\text { mar }, \text { amy })), \text { Region } (\text { spa }, \text { amy }))
$$

In Diplomacy we cannot move the same unit to two different regions at the same time. This is an example of incompatibility of actions. Thus, given the action $a _ { 4 }$ below, comp(a , a ) does not hold and therefore neither feasible(p) holds if p contains a and $a _ { 4 }$ nor comp({a }, {a }) holds.

$$
a _ {4} = \operatorname{mto} (\text { Unit } (\text { fra }, \text { Region } (\text { par }, \text { amy })), \text { Region } (\text { gas }, \text { amy }))
$$

Assuming that Austria controls only two units, Fig. 2b illustrates an example of a joint plan for Austria $p = \{ a _ { 5 } , a _ { 6 } , a _ { 7 } , a _ { 8 } \}$ where actions are represented as:

$$
a _ {5} = \operatorname{mto} (\text { Unit(ita,   Region(tyr,   amy)),   Region(ven,   amy)) }
$$

$$
\begin{array}{l} a _ {6} = \sup (\text { Unit } (\text { aus }, \text { Region } (\text { tri }, \text { flt })), \text { mto } (\text { Unit } (\text { ita }, \text { Region } (\text { tyr }, \text { amy })), \\ \text { Region } (\text { ven }, \text { amy })) \end{array}
$$

$$
a _ {7} = \operatorname{mto} (\text { Unit } (\text { aus }, \text { Region } (\text { vie }, \text { amy })), \text { Region } (\text { tyr }, \text { amy }))
$$

$$
\begin{array}{l} a _ {8} = \sup (\text { Unit(ita,   Region(mar,   amy)) }, \text { mto(Unit(aus,   Region(vie,   amy)),Region(tyr,   amy))) } \end{array}
$$

Given this plan, Italy could propose Austria different options:

• propose(ita, aus, [Commit(aus,ita, Do(a ))]). Italy proposes Austria a deal where Austria commits to support the Italian move from Tyrol to Venice. As Italy does not give anything in exchange it may not be effective.

• propose(ita, aus, [Commit(ita,aus, Do(a )), Commit(aus,ita, Do(a ))]). This looks more balanced but Italy is actually not providing anything bene<sup>fi</sup>cial to Austria.

• propose(ita, aus, [Commit(ita,aus, Do(a )), Commit(aus,ita, Do(a )), Commit(aus,ita, Do(a<sub>7</sub>)), Commit(ita,aus, $\mathsf { D o } ( a _ { 8 } ) ) | )$ . This proposal is more balanced as Italy is also helping Austria.

Which one of these options should Italy actually send to Austria is what the architecture of a software agent and its negotiation strategy determine.

## 3. Agent architecture

In this section we propose a software architecture to build agents capable of participating in RNPs. We introduce here its main modules and then we give details for each of them in subsequent sections. We refer to the architecture as HANA and to the agents designed according to HANA as HANA agents.<sup>8</sup> The architecture is graphically represented in Fig. 3.

In Section 2 we assumed that RNPs happen in fully observable environments that agents can perceive and where agents can execute actions whose (deterministic) consequences are also observable. Furthermore, the environment allows for agents to exchange messages. Thus, the <sup>fi</sup>rst component of HANA is an interface module that situates the agents in their environment, that is, it allows to observe the environment state, observe and execute actions, and exchange messages with other agents. In other words, this module contains the sensors and actuators of the agent. Which actions to execute and which messages to send are decided by the negotiation module.

The design philosophy behind HANA is to provide some means to negotiate as humans do, as the negotiation counterparts could be humans. In particular, there are two capabilities that we think realistic agents should show: dealing with emotions and dealing with uncertainty, [28]. The architecture incorporates emotions as this is an important part of the non-constructivist rationality approach, we need to understand emotional reactions of the other negotiators. Although the environment is fully observable, the actions to be executed by the other agents can only be guessed analysing the other agents' previous behaviour. To cope with this uncertainty, we decided to represent the world as a graded BDI model, that is, with graded beliefs, desires and intentions following the g-BDI model [5]. In Section 4 we provide a more in-depth description of the world model module that is the one containing the emotions and BDI components.

The space of plans and negotiation options that an agent can execute and propose, respectively, is potentially huge, as for example in The Diplomacy Game. Thus, we assume that the space is large enough and the negotiation time short enough to preclude obtaining the optimal. That means that any architecture for this type of negotiation needs to give the means to look for good enough solutions. Moreover, the longer it takes to decide what to propose the less probable it is for the proposal to be accepted. As time goes by, the agents reach agreements that increase the amount of commitments and reduce the set of options compatible with the commitments. The increase of acquired commitments increases in turn the probability that our desired plans will not be compatible any longer. Consequently, the architecture must allow to start the negotiation from the very beginning of a negotiation round. Dealing with huge solution spaces is not an inconvenience for human agents, e.g. in playing Chess or Go. Humans do work with good enough solutions in their everyday lives. Time constraints, boredom, or tiredness makes humans accept good enough solutions. To start negotiating from the very beginning, HANA proposes to perform a search&negotiation

(b) Joint plan

(a) Plan  
![](/api/attachments/XMT56ZUV/fulltext/images/70179800eea78bf385c0e02fa1ca871cd62a08e03f882efbf9486960d00a2514.jpg)  
Fig. 2. Two examples of plans.

method that assumes the plan search to go hand in hand with the negotiation. The plan search module executes an anytime algorithm that provides a periodically updated ranking of good enough plans. The ranking takes into account the commitments obtained by the negotiation module. And the negotiation module proposes options generated from the previously found good enough plans that contain actions to be executed by other agents. In this way, HANA agents can start the negotiation from the very beginning, proposing options that, once negotiated, will provide new information – because the option will be accepted or rejected – to focus the search on the generation of new and better evaluated plans. As can be seen in Fig. 3, the plan and option evaluators depend not only on the commitments but on the whole world module. Thus, those evaluation functions are also updated taking into account the intentions generated from new observations. The intentions trigger the decisions of the agent. In the following sections we provide a more in-depth description of the modules, their components and the decisions to be taken by the agent.

The execution of HANA consists of several concurrent processes for: the interface (to receive messages and observe the results of actions and the environment state), the world model (to update the world model given the perceived changes), the plan search (to continuously update the ranking of plans), and the negotiation (to generate options from plans and determine what to do next).

## 4. World model

For negotiation decisions to be effective they need to be based on an accurate assessment of the state of the environment and on the preferences of the other agents. Although the environment may be precisely known in certain domains, the preferences of others may be unknown, or may be uncertain. Moreover, specially in competitive scenarios, agents may lie about their preferences. This imposes the requirement that the world model has to be based on some uncertainty reasoning mechanism. During the last decade, some of the most successful representation models have been based on BDI representations.

Most work on BDI models has concentrated on providing agent-oriented programming frameworks and languages such as Jason [2], Jack [42], AgentSpeak [6,33], 3APL [19] or 2APL [7]; and on logical approaches to the BDI model such as modal logic [34], <sup>fi</sup>rst-order logic [33], or belief degrees [30,32]. BDI is based on the theory of human practical reasoning [3] and has well-founded logical semantics [35]. The work of Casali et al. [5] on what they denoted by g-BDI, gives a powerful generic representation for degrees of belief, degrees of desire (preferences) and degrees of intention (active goals). We adapt this work to our problem and incorporate the beliefs, desires and intentions as the main components of the world model.

![](/api/attachments/XMT56ZUV/fulltext/images/143bf9b0d8e8b7b9124cb7e46df93d2fcad9c46b06d36274d4466fa41cc0815e.jpg)  
Fig. 3. Graphical representation of HANA. Arrows represent data <sup>fl</sup>ows. Coloured boxes represent the modules that form part of the agent, and white boxes are components of those modules.

We consider that desires and intentions are derived from beliefs. What happens in the world determines whether we desire it to change into a different world and whether we intend to make that happen. In this section we concentrate on how HANA agents represent their beliefs about the next environment state. The most important aspect of the uncertain evolution of the world is what an agent expects to happen in the environment due to the decisions of other agents. This is so because the natural evolution of environments is subject to shared knowledge on physical laws and thus known by every agent. Therefore, the evolution of the world can be due to either actions, A, or utterances, M, of other agents. We denote those events (actions and utterances) by Φ = M ∪ A. The agent has at all time a belief degree assigned to every element of Φ meaning how certain is the agent that that event will happen. We decided to model these degrees as probabilities because the data for them comes from the previous interactions with the other agents and thus those data can be statistically processed. Axiomatics on how to represent probabilities are provided in [5].

De<sup>fi</sup>nition 16. Given $\Phi = M \cup A ,$ a belief is a tuple $\langle \alpha , \ \varphi , \ \vartheta \rangle \in$ $\mathsf { A } \times \Phi \times [ 0 , 1 ]$ where ϑ is α's belief degree on φ happening. We denote by B the set of all possible beliefs and by $\mathtt { B _ { \alpha } } \subseteq \mathtt { F }$ B the set of possible beliefs $o f \alpha ^ { 9 }$

We de<sup>fi</sup>ne the feasibility of φ ∈ Φ as an extension of the feasibility on utterances and actions.

De<sup>fi</sup>nition 17. Given the current state $\omega \in W$ and the current dialogue Ψ, we de<sup>fi</sup>ne feasibility for $\varphi \in$ Φ as:

$$
\text { feasible } (\varphi) = \left\{ \begin{array}{l l} \text { feasible } (\omega , \varphi) & \text { if } \quad \varphi \in A \\ \text { feasible } (\psi , \varphi) & \text { if } \quad \varphi \in M. \end{array} \right.
$$

The particular type of problem studied here gives some restrictions on over what it is feasible to happen. All agents know the physical laws of the world, thus they all know that non feasible events will not happen. The degree of belief on a non feasible event would be then the minimum, 0. Also for plans: non feasible plans will not happen as those plans contain non feasible or non compatible actions. In the following we show two constraints for values of the belief model that are derived from the notion of feasibility and compatibility. In particular, only one operator can be applied to a resource. Two feasible actions operating on the same resource are non compatible and, thus, they cannot both happen at the same time. As we decided to represent degrees as probabilities, the summation of probabilities on all those actions to be operated on the same resource must be 1:

$$
\forall \omega \cdot \forall \langle \alpha , r \rangle \in \omega \cdot \sum_ {\{a _ {i} = \langle \alpha , o p _ {i}, r \rangle | \text {feasible} (a _ {i}, \omega) \text {and} o p _ {i} \in O p \}} B _ {\alpha} (a _ {i}) = 1.\tag{1}
$$

Moreover, the negotiation protocol proposed in this work imposes that only feasible utterances are possible.

$$
\forall \psi \cdot \sum_ {\{\mu_ {i} | \text {feasible } (\psi , \mu_ {i}) \}} B _ {\alpha} (a _ {i}) = 1.\tag{2}
$$

For a given environment state ω, the belief degree of α on an action a happening is $B _ { \alpha } ( a )$ . Recall that plans are considered sets of actions that are to be executed at the same time. The belief on the execution of a feasible plan $p = \{ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } \} \in P ^ { \omega }$ is thus naturally modelled according to HANA as the belief on the conjunction of the execution of each action that is then modelled as the product:

$$
B _ {\alpha} (p) = B _ {\alpha} (a _ {1} \wedge a _ {2} \wedge \dots a _ {n}) = \prod_ {a _ {i} \in p} B _ {\alpha} (a _ {i}).\tag{3}
$$

When new observations of the environment are made, HANA agents update their beliefs. From the many possible belief review functions available in the literature [1,17,32] HANA uses a recency based belief revision de<sup>fi</sup>ned as follows.

De<sup>fi</sup>nition 18. Given an agent $\alpha \in \mathsf { A } c$ a belief review function, denoted by $\sigma \colon 2 ^ { \mathrm { B } \alpha } \times 2 ^ { \mathrm { B } \alpha }  2 ^ { \mathrm { B } \alpha }$ is any function satisfying:

$\sigma ( \mathsf { B } ^ { \prime } , \mathsf { B } ^ { \prime \prime } ) = \mathsf { B } ^ { \prime \prime \prime }$

• B′ is the original belief set

• B″ is a new belief set

• $ [ \mathbf { f }  \boldsymbol { \varphi } , \vartheta  \in \mathbf { B } ^ { \prime } ,  \boldsymbol { \varphi } , \vartheta  \in \mathbf { B } ^ { \prime \prime } $ and $\vartheta \neq \vartheta ^ { \prime }$ then $\langle \varphi , \vartheta ^ { \prime } \rangle \in \mathbf { B } ^ { * }$

• If $\langle \varphi , \vartheta \rangle \in \mathbf { B } ^ { \prime }$ and $\langle \varphi , \rangle \not \in { \bf B } ^ { \prime \prime }$ then $\langle \varphi , \vartheta \rangle \in \mathbf { B } ^ { * }$

• Nothing else belongs to $\boldsymbol { \mathrm { B } } ^ { * }$

• B‴ is the normalization $^ { 1 0 } 0 \mathrm { f ~ B } ^ { \ast }$

Desires, intentions and emotions<sup>11</sup> are also updated via a similar update method that for brevity we omit here. The arrows in Fig. 3 show the in<sup>fl</sup>uence between the different motives: changes in the environment provoke updates in the belief set that generate updates in the emotions that update the desires. The new set of beliefs and desires determines new intentions.

The world model architecture allows to represent complex behaviours as next example show.

Example 1. The HANA agent Revenger plays Diplomacy and is configured to have a sensitive and aggressive personality. It comes to believe that the agent Beth is an enemy as it executed a movement that attacks one of Revenger's units and never accepted any proposal in the past three negotiation rounds. Its personality rules for revenge trigger a desire (with a high degree) to damage Beth that will in turn give an intention (again with high degree) to attack one of Beth’s units although it is a very difficult task and there are other alternative plans that would be easier to reach and would give Revenger a higher rational utility.

Although only a few components in Fig. 3 are interconnected to build up the world model of HANA agents (beliefs, desires, intentions and emotions), other models might be incorporated. The world model is based on multicontext systems [5] that are modular structures that allow for an easy interconnection of different (logical) models, using transition functions between them, to build even more complex agents. For instance, a trust model may impact on intentions as the intention degree to satisfy a desire via a plan with an untrustworthy agent should be low. Also, a social model might impact on intentions as we might want to have a higher intention degree on plans involving an agent with whom we would like to increase the level of intimacy [40] than otherwise.

As de<sup>fi</sup>ned in Section 2.2, the agents must ful<sup>fi</sup>l a negotiation protocol in order to be able to negotiate with other agents. The rules or constraints that the protocol provides can be incorporated in the agent as internal norms to follow. This is done according to HANA with a high desire degree on ful<sup>fi</sup>lling the negotiation protocol and some transition functions between this desire and several beliefs that modify the degree of what we call basic intentions: reply δ (when the agent believes that it received proposal δ), propose (when there is time left in the negotiation round) and executeActions (when we are approaching the end of the negotiation round).

## 5. Plan search

The interplay between search and negotiation is the most important contribution of HANA. In most multi-issue negotiation problems the space of potential solutions is determined by the admissible values of issues, that is, potential solutions are elements of the Cartesian product of the admissible values for each issue [12]. Differently, in RNPs the space of potential solutions is de<sup>fi</sup>ned as the combination of feasible actions that are compatible. Only certain subsets of the space of actions constitute feasible solutions and <sup>fi</sup>nding which ones are feasible is not straightforward. Good and bad solutions are not placed together nicely as in continuously valued attributes (e.g. if a certain low price is good, nearby low prices will be similarly good). Sometimes a small change in a plan makes it go from excellent to catastrophic. Moreover, the space of potential solutions in real domains is frequently huge. What HANA brings in to address in this type of negotiation problem is a search&negotiation method that enables the negotiation to start as soon as possible over reasonably good solutions. We explain the details of how solutions are sought in this section.

The outcome of the search process is a continuously refreshed ranking of candidate plans. The plan ranking is made by the plan generator, thanks to a utility function that represents the preferences of the agent and that is implemented within a component of the architecture called plan evaluator, see Fig. 3. Preferences are determined by the world model and thus take into account personality traits or relationships between agents for instance, not just an individual position improvement.

Every agent α in a state transition system Ω must decide what actions to perform, that is, what complete plan $\overline { { p } } _ { \alpha }$ to perform. Remember that given a state ω, next state ω′ is computed by a state transition function T: $W \times P \to W . \ : T ( \omega , \overline { { p } } )$ is de<sup>fi</sup>ned for complete plans, $\overline { { p } } { \in } \overline { { P } } ^ { \omega }$ <sup>ð Þ</sup>that are those that can be obtained from the union of complete plans for every agent controlling resources in the current state: ${ \overline { { p } } } = \bigcup _ { \beta \in { \mathcal { A } } } { \overline { { p } } } _ { \beta } .$ To decide what plan to perform, α must know what utility every plan would provide. If α knew the plans of the other agents, $Q = \bigcup _ { \beta \in \mathcal { A } } \bigcup _ { \{ \alpha \} } \overline { { p } } _ { \beta } ,$ it could compute the utility of α performing the complete plan $\overline { { p } } _ { \alpha }$ using its utility function. $\mathcal { U } _ { \alpha } \colon W \to [ 0 , 1 ]$ , as:

$$
\mathcal {U} _ {\alpha} (\omega , \overline {{p}} _ {\alpha}) = \mathcal {U} _ {\alpha} (T (\omega , Q \cup \overline {{p}} _ {\alpha})).
$$

However, whilst agents may have a clear idea of their preferences and hence can build up a utility function, it is usually impossible to know what the plans of other agents will be. Therefore, instead of using the deterministic transition function, T: $W \times P \to W ,$ α has to use a probabilistic state transition function.

De<sup>fi</sup>nition 19. Given a transition system $\Omega = \langle \mathsf { A } , R , O p , W , P , \mathsf { T } , \omega _ { 0 } , W _ { f } \rangle$ a probabilistic transition function, denoted by T(ω′|ω, $p ) \in \mathbb { P } ( W )$ is any conditional probability distribution over W given $\omega \in W$ and $p \in P ,$ such that for every complete plan $\overline { { p } } { \in } \overline { { P } } ^ { \omega }$ then $\mathbb { T } ( \mathbf { T } ( \omega , \overline { { p } } ) | \omega , \overline { { p } } ) =$ 1 and $\mathbb { T } \big ( \pmb { \omega } ^ { \prime } | \pmb { \omega } , \overline { { p } } \big ) = 0$ for all ω $\mathbf { \Pi } ^ { \prime } { \neq } \mathbf { T } ( \omega , \overline { { p } } )$

In RNPs the state transition function T: $W \times P \to W$ is <sup>fi</sup>xed and common to all the agents. Instead, a probabilistic transition function has to be particular for each agent as it necessarily depends on the interpretation of the past behaviours of other agents. Therefore, we will denote by $\mathbb { T } _ { \alpha } ( \omega ^ { \prime } | \omega , p )$ the probabilistic transition function of agent α. Then, the utility of a plan, complete or not, for an agent can be estimated as follows:

$$
E [ \mathcal {U} _ {\alpha} (\boldsymbol {\omega}, p) ] = \sum_ {\boldsymbol {\omega} _ {i} \in W} \mathbb {T} _ {\alpha} (\boldsymbol {\omega} _ {i} | \boldsymbol {\omega}, p) \times \mathcal {U} _ {\alpha} (\boldsymbol {\omega} _ {i})\tag{4}
$$

The complexity here relies on the evaluation of $\mathbb { T } _ { \alpha } ( \omega ^ { \prime } | \omega , p )$

We can identify the problem of learning the probabilistic state transition function for all complete plans for a given agent $\alpha \in \mathsf { A }$ as a Markov Decision Process (MDP) [22]. A MDP is a tuple 〈S, A, L: $A \times S \times S \to [ 0 , 1 ] , \ R \colon A \times S \times S \to [ 0 ,$ 1]〉, where S is a <sup>fi</sup>nite set of states, A is a <sup>fi</sup>nite set of actions, $L ( a , s , s ^ { \prime } )$ is the probability that action a in state s will lead to state s′, and $R \left( a , s , s ^ { \prime } \right)$ is the immediate reward received after transition to state s′ from state s with transition probability $L ( a , s , s ^ { \prime } )$ . The interpretation as an MDP is based on having $S = W , A = P , L = \mathbb { T }$ and $R ( p , \omega , \omega ^ { \prime } ) = \mathcal { U } _ { \alpha } ( \omega ^ { \prime } ) - \mathcal { U } _ { \alpha } ( \omega )$ . Learning <sup>U U</sup>requires a wealth of data that is usually not available and an initially random behaviour that may produce very negative outcomes in RNPs. Moreover, there is a required feature for any MDP problem that is not veri<sup>fi</sup>ed in our case: the Markov property. The transition function could depend on the past as other agents could learn from previous states and modify their decision function.

We propose an alternative to model the problem as an MDP that is to infer the probability state transition function from beliefs on the execution of plans as de<sup>fi</sup>ned in Section 4. From belief degrees on particular actions happening we can compute the belief degree of complete plans. Also, beliefs easily integrate other sources of information that are missing in a MDP, such as emotions or previous commitments. That is, the belief degree on an action happening may be determined, for instance, by knowing that the other agent is of a revenge type or that the other agent reached an agreement with another agent whom we trust and told us so. Moreover, as new sources of information can be easily incorporated into the world model this makes the architecture highly <sup>fl</sup>exible and modular. For all those reasons we de<sup>fi</sup>ne the expected utility not for a plan in particular but for a set of beliefs held in a particular state as follows:

De<sup>fi</sup>nition 20. We define the expected utility for $\alpha \in \mathsf { A }$ holding the set of beliefs $\mathtt { B ^ { \prime } } \subseteq \mathtt { B } _ { \alpha }$ in state ω $\mathbf { \Omega } ) \in W$ as:

$$
E \Big [ \mathcal {U} _ {\alpha} \Big (\boldsymbol {\omega}, \mathcal {B} ^ {'} \Big) \Big ] = \sum_ {\omega_ {i} \in W} \left(\frac {\sum_ {T _ {(\omega , \overline {{p}})} ^ {\overline {{p}} \in \overline {{P}} ^ {\omega}} B ^ {'} (\overline {{p}})} (\overline {{\omega , \overline {{p}}}}) - \omega_ {i}}{\sum_ {\overline {{p}}} \in \overline {{P}} ^ {\omega} B ^ {'} (\overline {{p}})} \times \mathcal {U} _ {\alpha} (\boldsymbol {\omega} _ {i})\right).\tag{5}
$$

The previous de<sup>fi</sup>nition does not require that α has made up his decision of what actions to perform. That is, the equation can be used at the beginning of the negotiation process — when α is still uncertain on what to do, and when all the bi-lateral negotiation processes have been <sup>fi</sup>nished and α knows what to do. The expected utility of a plan p is computed at any time assuming that the plan will be executed: $E [ \mathcal { U } _ { \alpha } ( \omega , \dot { \sigma ( \mathrm { B } ^ { \prime } , \{ \langle \alpha , a , \dot { 1 } \rangle | a \in p \} } ) ) ] . ^ { 1 2 }$ Actually, the richer <sup>U</sup>the world model the more accurate the utility functions can be. We measure the level of information in a belief set as the average of Shannon's entropy among the probability distributions of actions to be operated on resources. Notice that the higher the uncertainty the higher the entropy and thus, the less information.

De<sup>fi</sup>nition 21. The uncertainty on a set of beliefs $\mathtt { B ^ { \prime } } \subseteq \mathtt { B } _ { \alpha }$ given the set of predicates Φ that partition it, is measured as:

$$
\mathcal {H} \left(\mathcal {B} ^ {\prime}\right) \frac {1}{| \Phi |} \sum_ {\phi \in \Phi} \left(\frac {1}{\ln | \phi |} \sum_ {\langle \alpha , \varphi_ {i}, \vartheta_ {i} \rangle \in \phi} \vartheta_ {i} \ln \vartheta_ {i}\right).\tag{6}
$$

The uncertainty on actions to be executed is usually high at the beginning of a negotiation round, as an agent does not have enough information about each agent decisions, to 0 when the complete plan is actually performed and observed by all agents. Negotiation is the means to reduce the uncertainty on the belief model. By reaching agreements on negotiation options agents commit to the execution of their actions in the negotiating option and thus reduce the uncertainty by making equal to zero the probability of executing incompatible actions on the same resource.<sup>13</sup>

The task of the plan search module is to <sup>fi</sup>nd good enough plans to be executed by the agent, but also to provide good enough plans to negotiate with other agents. Plans to be executed are complete plans for the agent, that is, plans containing actions involving all the resources controlled by the agent in the current environment state. The plans to negotiate with other agents are extensions of those complete plans containing actions to be performed by other agents.

De<sup>fi</sup>nition 22. Given a transition system $\Omega = \langle \mathsf { A } , R , O p , W , P , \mathsf { T } , \omega _ { 0 } , W _ { f } \rangle$ and the current state $\omega \in W , a$ joint plan in state ω is a plan $p \in P ^ { \omega }$ involving at least two agents, |{α|〈α, op, $r \rangle \in p \} | \geq 2$ , and complete for one of them, that is, there is $\overline { { p } } \in \cup _ { \alpha \in \mathcal { A } } \overline { { P } } _ { \alpha } ^ { \omega }$ such that $\overline { { p } } \subseteq \mathsf { p }$ We denote the set of joint plans in ω by $\hat { P } ^ { \omega }$ <sup>A</sup>and the set of joint plans with a complete plan for α by $\hat { P } _ { \alpha } ^ { \omega }$ .

The bilateral nature of the interactions forces options to contain actions to be done by, at least, two agents. In HANA, joint plans involving more than two agents can be negotiated (either concurrently or sequentially) proposing several options generated from the joint plan. In Section 6 we explain how options are generated from joint plans. In this section we focus on the plan search. As introduced before, plans can be evaluated by their expected utility. Notice that this measure assumes that the plan will be executed. When joint plans are evaluated, we can also assume that the HANA agent will execute its part of the plan. Even so, we must be cautious about the actual execution of the actions in the plan assigned to other agents. We de<sup>fi</sup>ne the confidence of a plan in order to measure the degree of belief on the execution of a joint plan assuming that the HANA agent will perform its part of the plan.

De<sup>fi</sup>nition 23. Given a set of beliefs $\mathtt { B ^ { \prime } } \subseteq \mathtt { B } _ { \alpha }$ held by agent $\alpha \in \mathsf { A } ,$ , and a feasible plan $p \in p ^ { \omega } ,$ , α'’s confidence on p is de<sup>fi</sup>ned as:

$$
\mathcal {C} _ {\alpha} \left(\mathcal {B} ^ {\prime}, p\right) = B \left(\{\langle \beta , o p, r \rangle | \langle \beta , o p, r \rangle \in p \text {   and   } \beta \neq \alpha \}\right).
$$

Note that for al $\overline { { { p } } } _ { \alpha } \mathrm { e } \overline { { { P } } } _ { \alpha } ^ { \omega } , \mathcal { C } _ { \alpha } \big ( \boldsymbol { B } ^ { \prime } , \overline { { { p } } } _ { \alpha } \big ) = 1 . ^ { 1 4 }$

<sup>C B ¼</sup>The output of the plan search is a plan ranking. The con<sup>fi</sup>dence measure can be used by HANA agents to rank joint plans. HANA agents can rank the joint plans by their utility (how good are they for me), <sup>fi</sup>ltering out those joint plans that do not reach a minimum level of con<sup>fi</sup>dence (the agent does not think that other agents will perform their actions in the plan). This minimum level of con<sup>fi</sup>dence may increase as time goes by and the negotiation round deadline approximates in order to focus on joint plans in which con<sup>fi</sup>dence is high.

To generate plans we need a search algorithm that is: (i) capable to search in a huge space of solutions — as required by most real scenarios, (ii) anytime — as required by the time bounds, (iii) capable to generate several solutions instead of just one — we are looking for several plans, and (iv) guided by a dynamic heuristic — as the set of beliefs evolves with the agent interaction. We decided to implement HANA's plan generator with an evolutionary algorithm that constantly optimises the set of plans in the ranking. Concretely we use a genetic algorithm (GA) as these algorithms allow to ef<sup>fi</sup>ciently explore large spaces of solutions and produce successive populations of solutions that are increasingly better adapted to the environment even when it is changing along the search process. For us, each single solution, a chromosome in the GA, represents a complete or joint plan for the agent. The idea is to generate the plan ranking from the current population of solutions taking all or a subset of the best ones, preferably the latter. This population is updated generation after generation by the crossover, mutation and selection operators. It is important to guarantee the feasibility of the generated plans when applying crossover and mutation. The evaluation of a chromosome is done by the <sup>fi</sup>tness function that computes the expected utility of the plan represented by the chromosome. Fitness proportionate selection is used to give more chances to good plans to take part of crossovers. HANA's genetic search allows to set the probability of genes being mutated. We use this to focus the search on the joint plans looking for other agent actions that can nicely extend the best complete plans. In fact, to represent plans of diverse sizes, we use chromosomes with sizes equal to the size of complete plans and let some genes to have a void value meaning the resource corresponding to that gene has no assigned action. The probability of void values per gene can also be adjusted. The initial population does not need to be randomised. We set the initial population and stop the search at any time saving the current population. In this way, we can resume the computation later on. It is possible to use elitism to keep the best plans alive generation after generation. Elitism in the plan generation provides the minimum stability needed to avoid an erratic performance of the agent during negotiation. The idea is to keep the plan search running all the time but it can be stopped and restarted if it is necessary.

In conclusion, in this section we have argued the need of using data from the world model to evaluate plans. We described how plans are evaluated and how the evaluation functions change as new observations update the world model usually reducing the agent's uncertainty. And <sup>fi</sup>nally, we explained the necessary features that a plan generation should have and how we implemented the plan generation in HANA agents to generate the ranking of plans.

## 6. Negotiation

The negotiation module uses the ranking of plans and the world model to decide how to negotiate and what actions to perform, that is, what messages to send to other agents and what actions to execute over the environment. The world model and the plan search have independent processes that make the world model data and the plan ranking evolve along time. The negotiation module is controlled by another process that periodically takes a snapshot of both previous processes' data structures. We de<sup>fi</sup>ne this snapshot as a negotiation state.

De<sup>fi</sup>nition 24. A negotiation state is a tuple

$$
s = \left\langle \alpha , \omega , t, \mathcal {B} _ {\alpha} ^ {t}, \mathcal {D} _ {\alpha} ^ {t}, \mathcal {I} _ {\alpha} ^ {t}, P _ {\alpha} ^ {t} \right\rangle
$$

where:

$\alpha \in \mathsf { A }$ is an agent

$\omega \in W$ is an environment state

• t is a time instant

$\boldsymbol { \mathrm { B } } _ { \alpha } ^ { t } , \mathcal { D } _ { \alpha } ^ { t } ,$ and $\mathrm { I } _ { \alpha } ^ { t }$ are the beliefs, desires and intentions of α at time t

$P _ { \alpha \colon } ^ { t } P ^ { \omega } \mapsto [ 0 , 1 ]$ is a plan ranking

We denote the set of all possible negotiation states by S. Taking a snapshot, the negotiation use data from world model and plan ranking and perform a negotiation step while the plan search is looking for even better plans.<sup>15</sup> The work<sup>fl</sup>ow of the negotiation process is as follows:

1. Takes a snapshot of the current negotiation state.

2. Generates a ranking of negotiation options.

3. Executes the agent's intentions included in the world model.

4. Goes to (1) to continue with a new negotiation state.

The negotiation process uses the option generator to build a ranking of negotiating options satisfying De<sup>fi</sup>nition 11. Options are generated from the plan ranking $P _ { \alpha } ^ { t }$ as combinations of actions in joint plans $\hat { p } { \in } \hat { P } _ { \alpha } ^ { \omega }$ that are included in the plan ranking $P _ { \alpha } ^ { t } ( \hat { p } ) \neq \perp$ . Options are evaluated by the option evaluator that computes the next expected negotiation state assuming the acceptance of a given option $\delta \in { \mathcal { O } } _ { \alpha } ^ { \omega } .$ . The simplest way to generate the ranking of options, $\mathcal { O } _ { \alpha \mathrm { : } } ^ { t } \mathcal { O } ^ { \omega } \mapsto [ 0 , 1 ]$ is as follows:

$$
\mathcal {O} _ {\alpha} ^ {t} (\delta) = f (n e x t (s, \delta))
$$

where $s \in S$ is the current negotiation state $f \colon S \mapsto [ 0 , 1 ]$ is a negotiation state evaluation function, next: $S \times \mathcal { O } _ { \alpha } ^ { \omega } \mapsto S$ computes the next expected negotiation state, and $\exists \hat { p } \in \hat { P } _ { \alpha } ^ { \omega }$ such that $\delta { \underline { { \subseteq } } } { \hat { p } }$ and $P _ { \alpha } ^ { t } ( \hat { p } ) \neq \perp$

An alternative is to apply a <sup>fi</sup>lter and generate the option ranking using only the joint plans with value over a threshold $\nu > 0 .$ . That is, using every plan $\hat { p } { \in } \hat { P } _ { \alpha } ^ { \omega }$ such that $P _ { \alpha } ^ { t } ( \hat { p } ) > \nu .$

Given the negotiation state $s = \langle \alpha , \omega , t , \mathrm { B } _ { \alpha } ^ { t } , \mathcal { D } _ { \alpha } ^ { t } , \mathrm { I } _ { \alpha } ^ { t } , P _ { \alpha } ^ { t } \rangle$ and the option δ, an example of the next expected negotiation state next(s, δ), for a HANA agent that always honours its commitments and fully trusts the other agents, could be the negotiation state $s ^ { \prime } = \langle \alpha , \omega , t ^ { \prime } , \tilde { \mathrm { B } } _ { \alpha } ^ { t ^ { \prime } } , \mathcal { D } _ { \alpha } ^ { t ^ { \prime } } , \mathrm { I } _ { \alpha } ^ { t ^ { \prime } } , P _ { \alpha } ^ { t ^ { \prime } } \rangle$ such that $\begin{array} { r } { \mathsf { B } _ { \alpha } ^ { \mathrm { ~ } t ^ { \prime } } = \sigma ( \mathsf { B } _ { \alpha } ^ { t } , } \end{array}$ {〈α, a, 1〉|a ∈ δ)}) and $P _ { \alpha } ^ { \mathrm { \Delta } t ^ { \prime } } = \{ p | p \in P _ { \alpha } ^ { t }$ and comp(p, δ)}. The desires and intentions would be updated according to this new set of beliefs.

HANA provides several evaluation functions for negotiation states. Other functions can be used. In general, the richer the world model the more sophisticated the evaluation functions can be. The following functions assume the basic world model with beliefs on actions.

• Quality of information. The higher the quality of the information that we can reach in a negotiation state, the better. A well informed state contains joint plans that can reduce the uncertainty about the other agents' actions. The higher the uncertainty reduction the better. A natural way to evaluate the quality of information is to de<sup>fi</sup>ne it as 1 minus the average uncertainty of De<sup>fi</sup>nition 21.

$$
f _ {H} (s) = \max _ {p \in P _ {\alpha} ^ {t}} \left(1 - \mathcal {H} \left(\sigma \left(\mathcal {B} _ {\alpha} ^ {t} \{\langle \alpha , a, 1 \rangle | a \in p \}\right)\right)\right)\tag{7}
$$

• Independence. The more independent an agent is the better. If an agent can reach a high utility by its own means the better the negotiation state is. This measure depends on the complete plans for the agent that have been found so far, $\overline { { { P } } } _ { \alpha } ^ { t } = \Big \{ p \Big | p { \in } \overline { { { P } } } _ { \alpha } \mathrm { a n d } P _ { \alpha } ^ { t } ( p ) { \neq } \bot \Big \} . \mathrm { A }$ state is as good as the best state the agent can reach by its own means, this is the maximum expected utility to be obtained by assuming we chose one of the complete plans for agent α\:

$$
f _ {\mathcal {U C}} (s) = \max _ {\overline {{p}} \in \overline {{P}} _ {\alpha} ^ {t}} E \left[ \mathcal {U} _ {\alpha} \left(\omega , \sigma \left(\mathcal {B} _ {\alpha} ^ {t} \{\langle \alpha , a, 1 \rangle | a \in \overline {{p}} \}\right)\right) \right].\tag{8}
$$

• Opportunity. The more utility to be obtained with joint plans the better. Finding joint plans that give high utility is actually the reason of the whole negotiation process. Any state that has joint plans with high expected utility is a good state. This measure is similar to the previous one but using joint plans $\hat { P } _ { \alpha } ^ { t } = \left\{ p \middle | p \in \hat { P } _ { \alpha } \mathrm { a n d } P _ { \alpha } ^ { t } ( p ) \neq \bot \right\}$

$$
f _ {\mathcal {U} J} (s) = \max _ {\hat {p} \in \hat {P}} \alpha^ {t} E \left[ \mathcal {U} _ {\alpha} \left(\omega , \sigma \left(\mathcal {B} _ {\alpha} ^ {t} \{\langle \alpha , a, 1 \rangle | a \in \hat {p} \}\right)\right) \right].\tag{9}
$$

• Confidence. The more con<sup>fi</sup>dence in the available plans the better. Having a high con<sup>fi</sup>dence in the plans found during the search the less uncertainty there is on what will happen.

$$
f _ {\mathcal {C}} (s) = \max _ {p \in P _ {\alpha} ^ {t}} \left\{\mathcal {C} _ {\alpha} \Big (\mathcal {B} _ {\alpha} ^ {t}, p \Big) \Big | p \in P ^ {\omega}, P _ {\alpha} ^ {t} (p) \neq \bot \right\}.\tag{10}
$$

Each of these different measures, or a combination of them, allows to evaluate negotiation states and thus rank the available options. When to use each measure or how to combine them is what determines an agent's negotiation strategy. HANA allows to de<sup>fi</sup>ne strategies combining these measures. The other key element of the negotiation strategy is the aspiration level, i.e. the minimum evaluation value, that the agent has for options to be acceptable. The options above the aspiration level should be accepted, otherwise, rejected. At the beginning of a negotiation round agents would usually request a high aspiration value. As time goes by and the deadline approaches, agents become less demanding and decrease their expectations in order to reach some agreements that improve, even in a low amount, their negotiation state. HANA allows to de<sup>fi</sup>ne the way the aspiration level decreases as the next de<sup>fi</sup>nition shows.

De<sup>fi</sup>nition 25. Given a negotiation state s, a deadline $t _ { m a x } ,$ and current time t, the aspiration level, denoted $\mathsf { A } ( s , t )$ , is defined as:

$$
\mathcal {A} (s, t) = g _ {\text { min }} (s, t) + \left(\frac {t _ {\text { max }} - t}{t _ {\text { max }}}\right) ^ {\tau} \cdot (1 - g _ {\text { min }} (s, t))
$$

where $\tau \in [ 0 , 1 ]$ ] is the aspiration decay rate and $g _ { m i n } ( s , t )$ is the minimum value that can be guaranteed.

The negotiation strategy is then determined by <sup>fi</sup>xing values for $g _ { m i n } ( s , t )$ . HANA allows to de<sup>fi</sup>ne these functions as linear combinations of the measures de<sup>fi</sup>ned before. That is,

$$
g _ {m i n} (s, t) = w _ {1} (t) \cdot g _ {1} (s) + w _ {2} (t) \cdot g _ {2} (s) + \dots + w _ {n} (t) \cdot g _ {n} (s)
$$

where every $g _ { i } ( s ) \in [ 0 , \ 1 ]$ is a measure over the state s and $\sum \textit { i } _ { \mathrm { ~  ~ { ~ \mathrm { ~  ~ } ~ } } }$ . Next we discuss a few negotiation strategies:

• Conservative. An agent can guarantee a minimum utilitarian value with its own actions that corresponds to $g _ { m i n } ( s ) = f \mathcal { U } \mathcal { C } ( s )$ . This <sup>UC</sup>strategy is convenient at the end of a negotiation round as it concedes maximally towards the guaranteed minimum.

• Informative. A convenient strategy at the beginning of a negotiation round is to increase the agent's information quality. This facilitates to explore the space of options and reduce uncertainty in the negotiation. The more information an agent has the more probable its future proposals will be accepted. This can be achieved by $g _ { m i n } ( s ) = f _ { H } ( s )$

• Dynamic. A combination of the previous two starting with informative and ending with conservative.

$$
g _ {m i n} (s, t) = w _ {1} (t) \cdot f _ {H} (s) + w _ {2} (t) \cdot f _ {\mathcal {U C}} (s)
$$

$$
\text { where } w _ {1} (t) = \frac {t _ {\max} - t}{t _ {\max}} \text { and } w _ {2} (t) = 1 - w _ {1} (t).
$$

As introduced in Section 4, the HANA agents have three basic intentions that are: reply δ, propose and executeActions. Desires and intentions are graded and are represented similarly to how beliefs are represented. The basic intentions are mutually incompatible, thus the aggregation of their degrees is always 1. HANA agents satisfy the negotiation protocol de<sup>fi</sup>ned in Section 2 providing transition functions from beliefs and desires to intentions. Those transition functions update the degrees of the basic intentions whenever a message is sent or the deadline is reached. The negotiation process executes the current basic intention with the highest degree.

At the beginning of the negotiation round, the highest basic intention is always to propose: propose: I<sup>t</sup> (propose) > I<sup>t</sup> (reply δ) ∧ $\mathrm { I } _ { \alpha } ^ { \mathrm { t } } ( \mathrm { p r o p o s e } ) > \mathrm { I } _ { \alpha } ^ { \mathrm { t } }$ (executeActions). That is also the case when there is no proposal received and there is time left before the timeout. Whenever the highest basic intention is propose, the negotiation process executes the following sentences proposing the best option only when it is better than the current aspiration of the agent:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Ensure: s is the current negotiation state
 $\delta\leftarrow\arg\max_{\delta\in\mathcal{O}_{\alpha}^{\omega}}\mathcal{O}_{\alpha}^{t}(\delta)\ \text{selects the best ranked option}$ 
if  $\mathcal{O}_{\alpha}^{t}(\delta) &gt; \mathcal{A}(s,t)$  then
    propose( $\delta$ ) {the interface module sends a message proposing  $\delta$ }
end if
</div>

When a proposal is received, the highest basic intention becomes to be reply δ that is to reply the received proposal on the negotiating option δ. Then, the negotiation process accepts the proposal only when the next expected state provided by δ has a better evaluation than the current aspiration of the agent:

Ensure: f: S ↦ [0,1] is the negotiation state evaluation function Ensure: s is the current negotiation state

s′ ← next(s, δ) {computes the next expected state}

if f(s′) > A(s, t) then

accept(δ) {the interface module sends a message accepting δ} else

reject(δ) {the interface module sends a message rejecting δ} end if

Finally, when the timeout is reached, the highest basic intention is to executeActions. Then, the negotiation protocol automatically cancels all ongoing negotiations and the HANA negotiation process selects the best complete plan from the plan ranking and executes it:

$$
\begin{array}{l} \overline {{P}} _ {\alpha} ^ {t} \leftarrow \Big \{p \Big | p \in \overline {{P}} _ {\alpha} ^ {\omega} \text { and } P _ {\alpha} ^ {t} (p) \neq \bot \Big \} \\ \overline {{p}} \leftarrow \arg \max _ {\overline {{p}} \in \overline {{P}} _ {\alpha} ^ {t}} E \big [ \mathcal {U} _ {\varepsilon} (\omega , \sigma (\mathcal {B} _ {\alpha} ^ {t}, \{\langle \alpha , a, 1 \rangle | a \in \overline {{p}} \})   \{\text { available   complete   plan   with   highest   utility } \} \\ \text { execute } (\overline {{p}})   \{\text { the   interface   module   executes   all   actions   in } \overline {{p}} \} \end{array}
$$

Other intentions can be used by the negotiation strategy when desired. For example, a HANA agent with a trust model incorporated can generate the intention to not negotiate with agent β. In that case, Algorithm 25 should be modi<sup>fi</sup>ed to reject any proposal from β. And the plan evaluation of the plan search module should be modi<sup>fi</sup>ed to poorly evaluate joint plans with plans including β. The HANA architecture is designed to be able to incorporate new models in the world module and adjust the rest of the components. The architecture is <sup>fl</sup>exible and allows to create a high diversity of different agents.

## 7. Discussion and future work

In this paper we have proposed HANA, an architecture for agents involved in Resource Negotiation Problems (RNP). These problems consider realistic multiagent scenarios where agents need to bilaterally negotiate joint plans of action possibly with humans repeatedly throughout time. The aim of introducing RNP is to challenge the research community to study complex real negotiation scenarios involving humans specially those where the negotiation is about actions. The majority of current work focusses on the negotiation of a <sup>fi</sup>xed number of issues. Codifying an RNP as a multi-issue negotiation problem (every resource being an issue and the values being the concrete action on the resource) would force the negotiation process to deal with very large and sparse negotiation objects. This would not be a practical approach. In [4] a classi<sup>fi</sup>cation of automated negotiation is made which does not consider plans as possible negotiation objects. Although RNPs are dif<sup>fi</sup>cult problems we think that the automated negotiation research topic is mature enough to start facing the challenge.

One of the most compelling issues when researching in realistic scenarios with humans is experimentation. To support this task we have built the DipGame testbed [9] based on The Diplomacy Game<sup>16</sup> facilitating the development of software agents and the execution of experiments. This initiative is gaining relevance in the multiagent systems community. Several research departments from around the world are currently using DipGame and the number of registered users is increasing — 50 user registrations during the last two months.<sup>17</sup>

The architecture that we propose in this paper includes a BDI agent model. This BDI model deals with uncertainty using graded beliefs, desires and intentions [5]. The architecture is designed with the negotiation and the plan search modules executing concurrently. The negotiation module uses the best plans found so far by the search module to generate negotiation options, and the plan search module uses the commitments derived from proposals accepted by the negotiation module to prune the search space and improve the evaluation of the plans. HANA is a modular architecture that can be easily extended incorporating new behaviour models of personality, trust, relationships, etc. The idea of this architecture is to provide a skeleton for agents. Then, by <sup>fl</sup>eshing out this skeleton, researchers in negotiation can easily integrate different behaviour models to build an agent with good skills in order to negotiate with humans.

In the LOGIC negotiation model agents act in response to a need [40]. Whenever there is a need, a LOGIC agent selects whom to negotiate with, prepares a negotiation strategy with relevant information (legitimacy) and computes the acceptable options.

Differently from our work, no information is provided about how the negotiation options are generated from the needs. Here, we also provide details about how to evaluate options. LOGIC, as most negotiation methods, assumes that all possible negotiation partners have similar capabilities and thus selecting a partner does not depend on the concrete proposal to make. Here, instead, proposals determine which agents we should interact with as the capabilities of the negotiation partners can be different.

Our work is similar to [16] in that HANA also studies negotiation of joint plans of action involving several agents, is based on BDI agent models and assumes uncertainty in the actual outcome of plans. However, differently from [16], HANA agents can deal with uncertainty in their mental state by the use of a graded BDI model, it assumes the collaborations to be sporadical and it gives details of how plans are formulated and options negotiated.

Other interesting works that study negotiation and planning in multiagent systems are [23,29]. Both provide a logical framework and make assumptions (e.g. turn-taking dialogues and shared goals) that are dif<sup>fi</sup>cult to <sup>fi</sup>nd in human-aware scenarios. HANA focusses on those scenarios and provide a <sup>fl</sup>exible architecture for automated negotiation agents.

In the future we would like to study the use of a personality model like the one presented in [31] to select how the agents should emotionally react to observations by generating appropriate intentions. Analysing the personality of other agents is specially challenging as our agent counterparts can be humans. Another interesting model to incorporate is the relationship model described in [40] where intimacy levels are computed for each other agent and some strategies to reach a certain desired intimacy level are provided. The next behaviour model we plan to extend the architecture with is a trust model. The concept of trust is really important to perform negotiations. In environments where there is no trust among agents, negotiation cannot take place as the negotiators will not be able to believe on the actual execution of the agreement. We plan to incorporate a version of Sierra and Debenhams' trust model [39] (i) to provide beliefs on the agent's trust on other agents, (ii) to update the belief set from reached commitments, (iii) to provide the intentions to negotiate or not with a given agent, and (iv) to exclude from the plan ranking those joint plans with actions assigned to agents whom the HANA agent distrusts.

## Acknowledgements

Research is supported by the Agreement Technologies CONSOLIDER project under contract CSD2007-0022 and INGENIO 2010, by the Agreement Technologies COST Action, IC0801, and by the Generalitat de Catalunya under the grant 2009-SGR-1434. This work is also supported under project CBIT, which is funded by Spain's Ministry of Science and Innovation under grant number TIN2010-16306 and under ERA-NET project ACE.

## References

[1] C.E. Alchourròn, P. Gärdenfors, D. Makinson, On the logic of theory change: partial meet contraction and revision functions, Journal of Symbolic Logic 50 (1985) 510–530.

[2] R.H. Bordini, J.F. Hübner, M. Wooldridge, Index, 2007. 269–273.

[3] M.E. Bratman, Intention, Plans, and Practical Reason, Cambridge University Press, 1999.

[4] R. Buttner, A classi<sup>fi</sup>cation structure for automated negotiations, Proc. of the 2006 IEEE/WIC/ACM Int. Conf. on Web Intelligence and Intelligent Agent Technology (WI-IATW '06), IEEE Computer Society, Washington, DC, USA, 2006, pp. 523–530.

[5] A. Casali, L. Godo, C. Sierra, A graded BDI agent model to represent and reason about preferences, Arti<sup>fi</sup>cial Intelligence 175 (2011) 1468–1478.

[6] M. d'Inverno, M. Luck, Engineering AgentSpeak(L): a formal computational model, Logic and Computation 8 (3) (1998) 233–260.

[7] M. Dastani, 2APL: a practical Agent Programming Language, Autonomous Agents and Multi-Agent Systems 16 (3) (2008) 214–248.

[8] J. Debenham, C. Sierra, An agent supports constructivist and ecological rationality, Proc. 2009 IEEE/WIC/ACM Int. Conf. on Intelligent Agent Technology, Milano, 2009, pp. 255–258.

[9] A. Fabregues, C. Sierra, DipGame: a challenging negotiation testbed, Journal of Engineering Applications of Arti<sup>fi</sup>cial Intelligence 24 (2011) 1137–1146.

[10] A. Fabregues, J. Madrenas, C. Sierra, J. Debenham, Supplier performance in a digital ecosystem, Proc. of the IEEE Int. Conf. on Digital Ecosystems and Technologies (IEEE-DEST 2009), Istanbul, 2009, pp. 466–471.

[11] A. Fabregues, D. Navarro, A. Serrano, C. Sierra, DipGame: a testbed for multiagent systems (demonstration). Proc, of 9th Int. Conf, on Autonomous Agents and Multiagent Systems (AAMAS 2010). 2010, pp. 1619–1620.

[12] P. Faratin, C. Sierra, N.R. Jennings, Negotiation decision functions for autonomous agents, Robotics and Autonomous Systems 24 (3–4) (1998) 159–182.

[13] S.S. Fatima, M. Wooldridge, N.R. Jennings, An agenda-based framework for multi-issue negotiation, Arti<sup>fi</sup>cial Intelligence 152 (1) (2004) 1–45.

[14] D. Fessler, K.J. Haley, Genetic and cultural evolution of cooperation, The Strategy of Affect: Emotions in Human Cooperation, 2003. 7–36 , (Ch.).

[15] Y. Gal, B. Grosz, S. Kraus, A. Pfeffer, S. Shieber, Agent decision-making in open mixed networks, Arti<sup>fi</sup>cial Intelligence 174 (2010) 1460–1480.

[16] B.J. Grosz, L. Hunsberger, S. Kraus, Planning and acting together, AI Magazine 20 (4) (1999) 23–34.

[17] S.O. Hansson, A Textbook of Belief Dynamics: Solutions to Exercises, Kluwer Academic Publishers, Norwell, MA, USA, 2001.

[18] F.A. Hayek, The Fatal Conceit : The Errors of Socialism (The Collected Works of F. A. Hayek), University Of Chicago Press, 1991.

[19] K. Hindriks, M. d'Inverno, M. Luck, Architecture for agent programming languages, Proc. of the 14th European Conf. on Arti<sup>fi</sup>cial Intelligence (ECAI 2000), 2000, pp. 363–367.

[20] K.V. Hindriks, C. Jonker, D. Tykhonov, Towards an open negotiation architecture for heterogeneous agents, Proc, of the 12th Int Workshop on Cooperative Information Agents, Prague, 2008, pp. 264–279.

[21] A. JØsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[22] L.P. Kaelbling, M.L. Littman, A.R. Cassandra, Planning and acting in partially observable stochastic domains, Artificial Intelligence 101 (1998) 99–134

[23] A.C. Kakas, P. Torroni, N. Demetriou, Agent planning, negotiation and control of operation, of the 16th European Conf. on Arti<sup>fi</sup>cial Intelligence (ECAI 2004), 2004 pp. 28-32.

[24] D. Kim, D. Ferrin, H. Rao, A trust-based consumer decision-making model in electronic commerce: the role of trust, perceived risk, and their antecedents, Decision Support Systems 44 (2) (2008) 544–564.

[25] R. Lin, S. Kraus, From research to practice: Automated negotiations with people http://u.cs.biu.ac.il/linraz/Papers/linetal-practice.pdf.

[26] R. Lin, S. Kraus, J. Wilkenfeld, J. Barry, Negotiating with bounded rational agents in environments with incomplete information using an automated agent, Arti<sup>fi</sup>cial Intelligence 172 (2008) 823–851.

[27] N. Matos, C. Sierra, N.R. Jennings, Negotiation strategies: an evolutionary approach Proc. Int. Conf. on Multi-agent Systems (ICMA'S 98), 1998. 182–189.

[28] M. Minsky, The emotion machine: from pain to suffering, Proc. of the 3rd Conf. on Creativity & cognition (C&C '99), ACM, 1999, pp. 7–13.

[29] P. Pardo, P. Dellunde, L. Godo, Argumentation-based negotiation in t-delp-pop, Proc. of the 14th Int. Conf. of the Catalan Association for Arti<sup>fi</sup>cial Intelligence (CCIA 2011), vol. 232, 2011, pp. 177–186.

[30] S. Parsons, P. Giorgini, An approach to using degrees of belief in BDI agents, Proc. of the Int. Conf. on Information Processing and Management of Uncertainty in Knowledge-Based Systems, 1999.

[31] L. Peña, J.-M. Peña, S. Ossowski, Representing emotion and mood states for virtual agents, Proc. of the 9th German Conf. on Multiagent system technologies, 2011, pp. 181–188.

[32] P. Pilotti, A. Casali, C. Chesñevar, An approach to automated agent negotiation using belief revision, Proc. of the12th Argentine Symposium on Arti<sup>fi</sup>cial Intelli gence (40th JAIIO), Córdoba, Argentina, 2011, pp. 202–221.

[33] A.S. Rao, AgentSpeak(L): BDI agents speak out in a logical computable language, Proc. of the 7th European workshop on Modelling autonomous agents in a multi-agent world (MAAMAW '96), 1996, pp. 42–55.

[34] A.S. Rao, M.P. Georgeff, Modeling rational agents within a BDI-architecture, Proc. of the 2nd Int. Conf. on Principles of Knowledge Representation and Reasoning (KR'91), 1991, pp. 473–484.

[35] A.S. Rao, M.P. Georgeff, Decision procedures for BDI logics, Journal of Logic and Computation 8 (3) (1998) 293–342.

[36] W. Revelle, K.R. Scherer, Personality and Emotion, in: Oxford Companion to the Affective Sciences, Oxford University Press, 2010.

[37] J. Rosenschein, G. Zlotkin, Rules of Encounter, MIT Press, 1998.

[38] R. Sharp, The Game of Diplomacy, 1978. , (http://www.diplom.org/diparch/god.htm).

[39] C. Sierra, J.K. Debenham, Trust and honour in information-based agency, Proc. of the 5th Int. Conf. on Autonomous Agents and Multi-agent Systems (AAMAS 2006) 2006 pp. 1225-1232

[40] C. Sierra, J. Debenham, The logic negotiation model, Proc. of 6th Int. Conf. on Autonomous Agents and Multiagent Systems (AAMAS 2007), 2007, pp. 1026–1033.

[41] V.L. Smith, Constructivist and ecological rationality in economics, American Economic Review 93 (3) (2003) 465-508

[42] M. Winikoff, Jack intelligent agents: an industrial strength platform, Multi-Agent Programming, vol. 15, Springer, 2005, pp. 175–193.

![](/api/attachments/XMT56ZUV/fulltext/images/77b1c784ec20232ccb0e91ecd2d8677667ed6b2f39fef45f3ac8e4eb10cf8efc.jpg)  
Angela Fabregues is a software engineer that holds a PhD in Computer Science elaborated at the Arti<sup>fi</sup>cial Intelligence Research Institute of the Spanish Research Council (CSIC). She gained a First Class Honors bachelor in computer engineering in 2005, and she was awarded with The Google Anita Borg Memorial Scholarship in 2007. Her main research inter ests are in automated negotiation with humans and trust.

![](/api/attachments/XMT56ZUV/fulltext/images/106ac9b4abc808c4f28f677446dd5d5f480b79b22b1dfff3cd15e0efefd5b186.jpg)  
Carles Sierra is Research Professor of the Spanish National Research Council (CSIC). He is Vice-Director of the Arti<sup>fi</sup>cial Intelligence Research Institute in Barcelona and has made contributions to several areas of AI, specially on Multiagent Systems: Trust and Reputation models Negotiation mecha: nisms and Electronic Institutions
