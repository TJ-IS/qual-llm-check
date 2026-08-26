---
otero_id: 14378
otero_key: "34J8P5DD"
title: "The theory and experiments of designing cooperative intelligent systems"
authors: "Parag C. Pendharkar"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.028"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# The theory and experiments of designing cooperative intelligent systems

Parag C. Pendharkar

Information Systems, School of Business Administration, Penn State University at Harrisburg, 777 West Harrisburg Pike, Middletown, PA 17057, United States

Available online 13 June 2005

## Abstract

In this paper, we identify the business problems that lend themselves to the design of cooperative intelligent systems and empirically demonstrate the design and application of a multi-agent intelligent system for production scheduling. Our experiments suggest that a multi-agent system where agents coordinate their actions generally performs better than a multiagent system where agents do not coordinate their actions. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Genetic algorithms; Cooperative intelligent systems; Distributed artificial intelligence; Learning; Multi-agent systems

## 1. Introduction

Cooperative intelligent systems is one of the dynamic research areas in information systems [3,29]. Several researchers have shown that cooperative intelligent systems can be used for low maintenance cost decision support applications that allow decision-makers to take complex decisions [29]. However, not all business problems are suitable for the design of cooperative intelligent systems and the design of cooperative intelligent systems requires consideration of several factors.

Cooperative intelligent systems are also called distributed artificial intelligence (DAI) systems [25]. DAI consists of two sub-fields distributed problem-solving (DPS) and multi-agent systems (MAS) [5]. A DPS system consists of a set of independent geographically dispersed computer systems (problem-solvers) that share <sup>b</sup>solutions<sup>Q</sup> to solve a problem that none of the independent computer systems can solve independently. Both data and knowledge, in a DPS system, are geographically dispersed. Unlike the distributed database systems and the inter-organizational systems (IOS), a DPS system shares solutions and not data. In a DPS system, problem-solvers that will work together on a given problem and the solutions that will be shared by problem-solvers are usually known. A multi-agent system (MAS) is a set of geographically dispersed computer systems that <sup>b</sup>dynamically<sup>Q</sup> work together, through communication, to solve problems that none of the independent computer systems can solve independently. Unlike a DPS system, computer systems that will work together to solve a given problem are not known in a MAS and are decided dynamically. Further, communication among computer systems in a MAS can be data, hypotheses and knowledge.

Multi-agent systems are of considerable complexity with respect to their functionality and structure [43]. For most application tasks, even in simple environments, it is difficult to determine the behavioral repertoire of an agent in a multi-agent system [43]. For example, determining behavioral repertoire of an agent in a multi-agent system requires a decisionmaker to have a priori knowledge of future environmental requirements, knowledge of the availability of each agent at each environmental state in the future and knowledge about how agents will interact in response to the future environmental requirements [43]. The lack of availability of a priori knowledge necessitates the design of an adaptive system that can react to uncertain dynamic situations. A MAS offers features such as parallelism, robustness and scalability, which cannot be handled by centralized systems [43]. In particular, a MAS is used in domains that require integration of knowledge from multiple sources, resolution of different interests and goal conflicts [43]. Learning coordination in a MAS requires that agents adapt, adjust and learn to work with others agents to solve problems. The key issues of learning effective coordination in a MAS are the information exchange scheme and the coordination strategies between loosely coupled agents to achieve effective overall system performance.

Given the complexity of designing a MAS, the current research aims to address the following issues. (1) What types of business situations are suitable for deploying a multi-agent system? And, (2) what are different design considerations related to a multi-agent system design? We answer both of these questions through literature review and an empirical demonstration of a multi-agent intelligent system for a production scheduling environment. The rest of the paper is organized as follows: in Section 2, we review available literature in cooperative intelligent systems (DPS and MAS) area. In Section 3, we describe a production scheduling problem, a framework for genetic algorithm (GA)-based learning and different types of coordination groups, and propose a general multiagent coordination strategy. In Section 4, we detail the results of our simulation experiments and statisti cal analyses. In Section 5, we conclude the research by describing significance of our research and highlighting possible future extensions.

## 2. Overview of distributed problem-solving and multi-agent systems

Traditional work in artificial intelligence and decision support systems has been limited to problemsolving in the context of a single knowledge base. Research in the DPS, on the other hand, has focused on problem-solving related to a group of decentralized and loosely coupled knowledge bases. A DPS system has several advantages over a single, monolithic, centralized problem-solving system [5,15,34,35]. These advantages are—(1) faster problem-solving by exploiting parallelism, (2) reducing communication by transmitting only high-level partial solutions rather than raw data to a central site, (3) increased flexibility by creating problem-solvers, with different abilities, to solve the current problem and (4) increased reliability by allowing other problem-solvers to replace failed ones [13,43]. The distributed control makes a DPS system suitable to problems that transcend highly specialized functional boundaries [11].

There are several applications of the DPS that were reported in the literature. Among the popular applications are electronic meeting systems (EMS) and distributed meeting scheduling system (DMSS) [12]. A study by Nour and Yen [26] provides a DPS concep tual base for developing an EMS. The study presents a new conceptual framework where an EMS was at the center of three other large variables called fundamental elements. The EMS proposes self-reliance and interdependence as fundamental issues for effective decision-making. Both self-reliance and interdependence provide a useful perspective towards decisionmaking by achieving <sup>b</sup>global coherence with local control<sup>Q</sup> [17]. Hewitt [17] noted that having both self-reliance and interdependence often led to conflict because of the following reasons.

(1) Asynchrony enables the decision-makers more impervious to communication failures and allows them to be more self-reliant.

(2) Autonomous decision-making enables the participants in an EMS to react immediately to changing circumstances.

(3) Anonymity, task decomposition based on group preferences and specialization can increase diversity and robustness, and eliminate bottlenecks.

A few researchers proposed a DMSS for scheduling a meeting between different managers based on their personal schedules [7,32]. The DMSS had to decide a common meeting time by considering different managers schedules and preferences. The scheduling problem was complicated, as the privacy of the personal schedules had to be maintained. Bui et al. [7] proposed a Bayesian classifier-based DMSS system so that inter-agent communications can be minimized. The Bayesian classifier learnt about the other agents preferences based on the previous interactions and reduced the future need for communication.

Weiss [41] proposed a Dissolution and Formation of Groups (DFG) algorithm to solve the problem of learning appropriate sequences of action sets in a reactive multi-agent system. Collective learning and adaptation was achieved through credit assignment and group development. In a given environmental state, action selection was achieved through a competition between the agents and groups on the basis of their estimated goal relevance. The winner of the competition was allowed to become active and change the environment. Appropriate sequences of actions were learnt through repeated execution of the DFG algorithm cycle.

In another study of learning to coordinate actions in the block world, Weiss [42] suggested two more algorithms called ACtion Estimation (ACE) and Action Group Estimation (AGE). The ACE algorithm was similar to the DFG algorithm with a new term called minimum estimate added to it. The experimental results of the application of ACE and AGE algorithms showed that both the AGE and the ACE algorithms performed significantly better than a random walk algorithm. The performance of the AGE algorithm was better than the ACE highlighting the importance of goal relevance of an action.

A few researchers [8,16,30] had applied the concept of the multi-agent learning to mobile robots, intelligent manufacturing, predator–prey environments and load balancing. Bull et al. [8] examined the performance of genetic algorithms (GAs) within a multi-agent environment. The task was that of evolving the gait of a simulated wall-climbing quadruped by evolving the controllers of each leg. To facilitate the necessary communication between the agents, researchers used a GA to evolve the rules of the Pittsburgh-style classifier system [37]. The classifier systems were altered to enable them to post messages to each other. Three different configurations were compared. Namely,

(1) heterogeneous agents, each evolving within their own separate populations via separate ${ \mathrm { G A s } } ,$

(2) homogeneous agents, where all agents evolve within a single population via a single GA, and

(3) hereditary endo-symbiotic agents, in which one agent <sup>b</sup>carries<sup>Q</sup> the other agents’ gnomes and where all such carriers evolve within a single population.

Based on the multiple simulation runs, the researchers observed that heterogeneous multi-agent systems performed better than both the other multi-agent systems and an equivalent single agent system for the task. The argument was made in favor of heterogeneous multi-agent systems.

Atlan et al. [1] proposed a general system to infer symbolic policy functions for distributed reactive scheduling in non-stationary environments. An original distributed scheduling heuristic model was used with a genetic programming system to infer scheduling strategies. The purpose was to determine heuristic policies that are local, near optimal and robust with respect to perturbations. The researchers reported an initial success, but the robustness of their method with respect to larger problem size still remains an issue.

Other research on learning in the multi-agent systems had focused on problems involving artificial life (predator and prey) and load balancing. Haynes et al. [16] used <sup>b</sup>strongly typed genetic programming<sup>Q</sup> (STGP) to evolve cooperation of strategies. The prob lem consisted of four predators trying to capture a prey by surrounding it from four directions on a grid world. The goal of this research was to achieve agent (predator) cooperation and control, and to ensure the efficiency of the agents to capture the prey. The results of the simulation runs indicated that the STGP implementation was far superior to manually derived algorithms and that of general genetic programming.

Multi-agent reinforcement learning [19] was applied in the context of a load balancing in a distributed system [30]. The main focus of this study was to find out the results of interplay between basic adaptive behavior parameters and their effect on the system efficiency. A set of rules was encoded and fitness was assigned based on two criteria-optimization of resource usage and fairness of resource usage. The problem was to balance the load on a set of networked PCs and workstations. The results of the simulation runs indicated that the success of multi-agent learning comes from the mode of communication between the agents. Shaw [33] in his empirical study reported that, in order for the MASs to be successful, two factors are important: (1) agents need enough data to work and (2) there should be enough agents to pursue different solution paths.

Several applications of learning and coordination in the MASs were reported in literature [2,7,20,21,45]. Ciancarini [9] introduced a reference architecture called the PageSpace for designing interactive multiagent applications on the Internet. There are several agents on the Internet–user interface agents, personal home agents, agents that implement applications and agents that interoperate with legacy systems are a few examples. A coordination language called the Linda controlled the interactions of these agents. The coordination technology was integrated with a standard web technology and the JAVA programming language. Sun and Peterson [38] developed heuristics to partition a task among different agents and schedule agents based on partitioning. Bui [6] proposed an agentbased framework for supporting collaborative work among humans and non-human teleworkers (software agents). The proposed framework allowed geographically dispersed organization to distribute work across the Internet and embed intelligent software agents for distributed decision-making.

Sikora and Shaw [36] provided a framework for designing multi-agent system applications. According to their framework, a multi-agent system consists of an overall performance measure p and several individual agent performance measures $\pi _ { i } s$ . Assuming n agents, each agent $i \in \{ 1 , . . , n \}$ in a multi-agent system has its internal behavior model, which defines the role of the agent and how it would react to the changing environment. The individual agents interact to improve the overall performance of the system. Sikora and Shaw [36] identified three synthesis functions that relate the individual performance of the agents to the overall performance measure p. The three synthesis functions were as follows.

1. Competitive synthesis: when agents were brought together to work asynchronously on the same problem and the best solution among them was chosen as the group solution. Mathematically, this was represented as, $\pi { = } \operatorname* { m a x } ( \pi _ { 1 } , \pi _ { 2 } , . . . , \pi _ { n } )$

2. Additive Synthesis: When goals of the system were decomposed into independent sub-goals and are assigned to individual agents, the group performance was given by sum of individual performances of the agents. Mathematically, this was represented as, $\boldsymbol { \pi } { } = \sum { } \left( \pi _ { I } , \pi _ { 2 } , . . . . , \pi _ { n } \right)$

3. Cooperative synthesis: when goals of agents were conflicting, the group system performance was a more complicated function, $\phi$ , of the agents individual performance measures. Mathematically, this was represented as, $\pi { = } \phi ( \pi _ { 1 } , \pi _ { 2 } , . . . , \pi _ { n } )$

Malone and Crowston [23] defined coordination as management of dependencies. Building on Malone and Crowston [23] work, Sikora and Shaw [36] identified three main types of interdependencies in multiagent systems. These three dependencies were:

1. Temporal interdependency: The activities of the agents may be dependent on each other. For example, agent A cannot start its activity until agent B has finished its activity. The temporal interdependencies arise due to sequencing and synchronization problems.

2. Resource interdependency: The agents may share a common resource (money, storage space, etc.). Thus, the amount of resource available to agent A may depend on its usage by the other agents.

3. Sub-goal interdependency: Whenever a task is decomposed between several agents, agents may have to communicate the results of their partial solutions to each other and partial solutions may have to be integrated into the final solution. The inter-agent communications and information exchanges lead to sub-goal interdependencies.

Malone et al. [24] showed that there are three major kinds of dependencies that require coordination.

![](/api/attachments/34J8P5DD/fulltext/images/f82812d1ff07808f03b476fb0fcd414aafb02037a075646e65fdb10e2c33566f.jpg)  
Fig. 1. Basic types of dependencies [24].

Malone et al. [24] called these dependencies as fit, sharing and flow dependencies. Fig. 1 illustrates the dependencies identified by Malone et al. [24] study. Flow dependencies arise when one activity uses a resource produced by another activity. Sharing dependencies arise when a resource needs to be shared by multiple activities and fit dependencies arise when the resources produced by multiple activities have to fit together in some way. According to Malone et al. [24], <sup>b</sup>Just in Time<sup>Q</sup>, <sup>b</sup>Economic Order Quantity<sup>Q</sup> and detailed advance planning approaches are suitable coordination mechanisms for managing flow dependency. For sharing dependency, first come first serve, priority order, budgets and market-like bidding mechanism are all suitable coordination mechanism. Simulation approach and Microsoft’s Daily Build approach are suitable for fit dependency.

Schneeweiss [31] proposed a framework for classifying distributed decision-making systems. Using two dimensions of information asymmetry and conflict (team characteristics) between independent decision-making systems, Schneeweiss [31] identified four different categories of distributed decision-making systems. Fig. 2 illustrates these four categories.

The systems studied in the DAI can be categorized as team-based systems in symmetric information and non-team-based systems. The MAS may be categorized as principal agent system, whereas the DPS system may be either constructional or antagonistic hierarchical system in Schneeweiss [31] classification.

Lesser [20] summarized three major challenges in building multi-agent systems. According to Lesser [20], <sup>b</sup>The first principle relates to the need to view the performance of a multi-agent system in terms of an interdependent set of criteria in which there is rarely a way to optimize all criteria simultaneously. This principle, usually called <sup>d</sup>satisficing<sup>T</sup> behavior [36] was developed as a way of explaining how large organizations function<sup>Q</sup>. The second principle was related to the flexibility in agent problem-solving. Lesser [20] noted <sup>b</sup>. . .hard-coded assumptions about the character and availability of information and resources are typically avoided<sup>Q</sup>. The third principle was related to need to exploit the efficiencies of organized behavior in coordinating large agent societies. According to Lesser [20], <sup>b</sup>Organizing the agents in terms of roles and responsibilities can significantly decrease the computational burden on coordinating their activities since fewer options and constraints that need to be evaluated in order to make appropriate coordination decisions<sup>Q</sup>.

![](/api/attachments/34J8P5DD/fulltext/images/a2ced24b9c0613d1784b8b0bf3f3060190eac5d190c4f0fae1fcc49a759d9548.jpg)  
Fig. 2. Classification of distributed decision-making systems (Schneeweiss [31]).

Table 1 The criteria for designing multi-agent systems

<table><tr><td>Criterion</td><td>Reference</td></tr><tr><td>Conflicting multiple objectives</td><td>[4,20,35,45]</td></tr><tr><td>Dynamic demand and bottlenecks</td><td>[1,8,16,19,20,31,39]</td></tr><tr><td>Hard to use optimization models</td><td>[8,20,31,34,35]</td></tr><tr><td>Non-team-based decision-making</td><td>[8,7,17,21,32,33]</td></tr><tr><td>Asymmetric decision-making information</td><td>[8,12,17,32,34,42,44]</td></tr></table>

Wellman and Hu [44] studied the concept of learning and equilibrium in a MAS. According to Wellman [44], an agent in a MAS is challenged by dynamic environment and its ability to learn the behavior of other agents. Wellman [44] characterized an agent’s learning process in terms of the dynamics of conjectures about the effects of its actions. Wellman [44] introduced a concept of conjectural equilibrium where agents in a MAS reach an equilibrium in terms of consistency of conjectures within and across agents.

Based on review of the literature, Table 1 illustrates a set of criteria that may be used to identify business situations that are amenable for the design of multiagent systems.

Table 2 illustrates evaluation criteria for a multiagent system. A good MAS incorporates most of the criteria identified in Table 2.

## 3. The multi-agent intelligent system design problem in manufacturing and a framework for GA-based learning in distributed artificial intelligence

For our empirical research, we chose a problem of factory floor scheduling through the application of group technology [40]. The factory floor scheduling problem satisfies all but the non-team-based decisionmaking criterion (Table 1) of the multi-agent system design. We consider non-preemptive scheduling of multiple jobs over multiple machines, and use and extend Bhattacharyya and Koehler’s [4] genetic algorithm-based learning simulation model [2,4]. The specific design considerations of our research were following:

(1) propose different types of coordination groups and

(2) develop adaptive multi-agent coordination strategies and show the existence of conjectural equilibrium.

The Sycara et al. [39] framework for an inherently decentralized organization with factory floors divided into work areas [4] was adopted for our research. Agents with independent decision-making capabilities controlled the work areas. A typical job had to undergo several operations across various work areas and schedules for job completion were built incrementally. Incremental schedules had stated objectives, and dispatching decisions considered locally relevant and globally (system-wide) consistent criteria [4]. Thus, our framework not only considered multiple and often conflicting criteria, but also considered coordinated decision-making across various stated objectives.

For current research, multi-agent coordination capabilities were added to the original Bhattacharyya and Koehler [4] system. Factory floor entities (queues, servers, job areas, dispatchers), knowledge bases, coordination groups and performance criteria were modeled as objects. Fig. 3, adapted and modified from Bhattacharyya and Koehler [4], illustrates the framework used in our research. In Fig. 3, there are four main components. These components are a simulation subsystem, which models the environment, and intelligent dispatchers (intelligent agents), which have decisionmaking capabilities. We added a coordination group to the original Bhattacharyya and Koehler’s [4] system. A coordination group uses tax-based coordination mechanism among the dispatchers in the coordination group. We use certain managerial objectives to evaluate performance of dispatchers. A dispatcher has a knowledge base and uses a genetic algorithm-based learning to update the rules in the knowledge base at periodic intervals of time. Fig. 4 illustrates a dispatcher.

Table 2  
A system evaluation criteria for a multi-agent system

<table><tr><td>Criterion</td><td>Reference</td></tr><tr><td>Flexibility to change managerial objectives</td><td>[4,20]</td></tr><tr><td>Use of heuristic global search approaches</td><td>[4,16,19,31]</td></tr><tr><td>Non-static learning scheme</td><td>[1,4,16,31]</td></tr><tr><td>Existence of conjectural equilibrium</td><td>[45]</td></tr></table>

![](/api/attachments/34J8P5DD/fulltext/images/4c11bee11a44d339f715b3f259c84af3a8966cc8907a8580f428303d55648632.jpg)  
Fig. 3. A DAI framework for GA-based learning.

As mentioned before, decisions taken by dispatchers were evaluated based on predefined managerial objectives. The evaluation of decisions was carried out either at an intermediate point or at the end of the job’s sequence of operations. Typically, intermediate points reflect local decision objectives. The incorporation of intermediate payoffs was considered out of the scope of the current research. Genetic learning was based on the payoffs [37]. Various payoff functions were modeled to reflect different managerial objectives.

Coordination among the dispatchers occurred in a coordination group. Each coordination group had one coordinating dispatcher and at least two dependent dispatchers. Dispatchers, within a coordination group, coordinated using a credit assignment scheme. The extent of coordination was determined by the tax structure. The role of coordination was to achieve coherence of actions between the agents by generating hypothesis about the other agents’ behaviors and trading off the level of coordination (in terms of taxes). The agents were utility maximizers and coordinated their actions to maximize individual utilities. The tax was a part of individual utility that an agent paid to the coordinating agent (defined below) [41]. After the tax payments, individual utilities were adjusted to reflect tax payments. In a dynamic environment, taxes were updated periodically based on short-term performance of a dependent agent. The knowledge representation and inference scheme for the current research was same as the one used in Bhattacharyya and Koehler [4].

![](/api/attachments/34J8P5DD/fulltext/images/2675a68b303b2b55048b12f2bc2e2f0cfae7785b1d0811d7f3d4233d4e0fcfe5.jpg)  
Fig. 4. An intelligent dispatcher (agent).

## 3.1. Definition of coordination group

In a factory floor, different network configurations are possible. In order to cover a wide range of possible configurations, the following agents were defined:

Definition 1 (Coordinating agent). An intelligent dispatcher was a coordinating agent if it received taxes from any other dispatcher. The payoffs for the coordinating agent consisted of instant payoff of its performance criteria, global payoff at the end of job sequence and part of total payoff from the dependent machines (see next definition).

Definition 2 (Dependent agent). An intelligent dispatcher was a dependent agent if it paid tax to any other dispatcher.

A coordination group consisted of a coordinating machine and dependent machines. In Fig. 5, dispatchers connected to machines 6 and 11 are coordinating agents, and dispatchers connected to machines 5, 1, 2, 8, 9, 3, 7, 4 and 10 are dependent agents.

## 3.2. Types of coordinating groups

For the current research, three basic types of coordination groups, similar to Malone et al. [24], were defined. The three coordination groups cover a large range of dependencies that may occur in a factory floor. These dependencies may be one machine supplying the jobs to or receiving the jobs from another machine (one to one), one machine supplying jobs to many other machines (one to many) and many machines supplying jobs to a single machine (many to one).

Based on the three possible combinations, three coordination groups were identified. These three coordination groups were an inward fork coordination group (many–one), an outward fork coordination group(one–many) and a straight line coordination group (one–one), respectively. Fig. 6 illustrates these three coordination groups. In each coordinating group, there was one coordinating agent and one or more dependent agents. A coordinating agent, labeled as <sup>b</sup>C<sup>Q</sup> in Fig. 6, considered the requests to process the jobs of interest for the dependent agents. The dependent agents paid a <sup>b</sup>tax<sup>Q</sup> to the coordinating agent when the coordinating agent processed a job of their interest. A <sup>b</sup>tax<sup>Q</sup> was fraction of the total payoff that an agent paid to the coordinating agent for coordination. In Fig. 6, a dotted line and an arrow show the direction of the payment of taxes. The taxes that the dependent agents paid were a variable number.

![](/api/attachments/34J8P5DD/fulltext/images/5b33f4f11d4db6e21fced117c57e31317d674446d03811d87ac25778de9155fd.jpg)  
Fig. 5. Group technology and manufacturing cells.

![](/api/attachments/34J8P5DD/fulltext/images/3dac4be83a595afe0e354e98af3ab503e309753ca3524b3c484e7f1361443c69.jpg)  
Fig. 6. Three basic types of coordination groups.

A factory floor was divided into different coordinating groups each of which can be a member of the universe of three coordinating groups. Depending on the type of coordinating group, a coordinating agent and the dependent agent were defined and <sup>b</sup>communication paths<sup>Q</sup> in terms of tax payments were established.

## 3.3. Payoffs to the agents

Central element of a multi-agent learning framework is an equilibrium concept. Unlike single-agent system where an agent maximizes its own utility, agents in multi-agent systems maximize their individual utilities simultaneously [44]. Thus, it was important to show that a given multi-agent coordination strategy will converge to a conjectural equilibrium [44]. We used an adaptive competitive agent strategy proposed by Wellman and Hu [44] to learn coordination in the multi-agent system [44].

Each agent was allowed to have its local and/or global payoff criteria based on the managerial objectives. Coordination was achieved by adjusting the payoff estimates of the individual agents in an additive utility function. The coordination mechanism was learning the weights (taxes) in an additive utility function that evaluated the total system payoff. The concept of learning of weights, in an additive utility function, is widely reported in literature. For example, Madni and Samet [22] used a multicategory pattern classifier for learning the weights in an additive utility function that evaluated messages in military command, control and communication situations. Farquhar [14] described similar other applications. For each dependent agent $A _ { i }$ that can receive or send a job from/to a coordinating agent $C , A _ { i }$ paid a tax $B _ { i }$ to agent C to consider processing jobs of its interest first. $B _ { i } \in [ 0 , 1 ]$ was a tax rate that determined the fraction of total payoff that a dependent agent paid to the coordinating agent. The payoff to the coordinating agent and the dependent agent was adjusted as follows:

$$
\prod_ {c} = \prod_ {A} + B _ {i} \prod_ {A}
$$

$$
\prod_ {A} = \prod_ {A} - B _ {i} \prod_ {A}
$$

where $\Pi _ { A }$ was the total payoff given to the dependent agent (local and global) and $\varPi _ { A } ^ { \prime }$ was the payoff received by the dependent agent. $B _ { i }$ was the tax rate that determined the fraction of dependent agent’s payoff to the coordinating agent and $\Pi _ { c }$ was the payoff received by the coordinating agent. All $B _ { i } \in [ 0 , 1 ]$

The coordination within a group was operationalized through the adjustments of the taxes. Taxes were adjusted periodically after a specified number of jobs passed through the system. The taxes were allowed to vary between 5% and 10% of the total payoff value to avoid big variations leading to chaotic randomized behavior arising from the jobs coming from the tail of the Poisson distribution. Initially, at the beginning of the simulation, taxes were set equal to zero. The new tax $B _ { \mathrm { n e w } }$ was calculated as follows:

B ¼ B - learn rateð $\boldsymbol { \Pi } _ { \mathrm { o l d } } - \boldsymbol { \Pi } _ { \mathrm { n o w } } )$ ; if 0:05Vjlearn rate $( \varPi _ { \mathrm { o l d } } - \varPi _ { \mathrm { n o w } } ) | { \leq } 0 . 1$ learn rateð Þ ¼P - P 0:05d; if jlearn rateð ÞjP - P V0:05 and learn rate $\dot { ( \vphantom { \sum }  } \Pi _ { \mathrm { o l d } } - I I _ { \mathrm { n o w } } \dot { ) } = 0 . 1 \delta ,$ ; if jlearn rate $( \dot { I } \mathrm { I I _ { o l d } } - I I _ { \mathrm { n o w } } ) | { \geq } 0 . 1$ d ¼ - 1 if P <sup>N</sup>P ; d ¼ 1 otherwise:

ð1Þ

In the beginning of the simulation run, $\scriptstyle \prod _ { \mathrm { o l d } } = B _ { \mathrm { o l d } } = 0$ and $\Pi _ { \mathrm { n o w } }$ was the average payoff across a specified number of initial jobs through the system. Learn rate was a number that was experimentally determined and was set so that, when multiplied with an approximate average of $( \varPi _ { \mathrm { o l d } } - \varPi _ { \mathrm { n o w } } )$ , it gave a product between 0.05 and 0.1. A knowledge base contained a set of condition action rules, which was defined as conjunction of atoms, predicates and condition action rules.

After describing the adaptive multi-agent coordination, we now illustrate the existence of conjectural equilibrium. The coordinating agent was always in two states: state 1—the coordinating agent was coordinating (tax <sup>N</sup> 0) and state 2—the coordinating agent was not coordinating (tax V 0). Since jobs kept coming in the system. The entire process was a continuous time stochastic process. Let $p _ { i j } ( t )$ represent the probability that the coordinating agent was in state $j$ at time t given that it was in state i at time 0. Since a coordinating agent can take only one of two states (state 1 = 1 and state $2 = 0 )$ , we had four probabilities: $p _ { 0 0 } ( t ) , p _ { 0 1 } ( t ) , p _ { 1 0 } ( t )$ and $p _ { 1 1 } ( t )$ . In order to derive the $p _ { i j } ( t )$ functions, we made following assumptions:

1. The process satisfied Markov property.

2. The process was stationary.

3. The probability of transition from a given state to other state in a short interval, $\Delta t ,$ was proportional to $\Delta t .$

In the event of no-breakdown of machines and for very small values of $\Delta t ,$ all the above-mentioned assumptions strictly hold. In regards to assumption 3, let

$$
p _ {0 1} (\Delta t) = x \Delta t
$$

$$
p _ {1 0} (\Delta t) = y \Delta t
$$

where x and y are constants of proportionality called cooperation rate and defection rate. Using a special case of the Chapman–Kolmogorov equations, we calculate the function value of $p _ { 0 1 } ( t ^ { + } \Delta t )$ or the probability that the agent was coordinating at time $t + \Delta t .$ , given that it was not coordinating at time 0, as follows:

$$
p _ {0 1} (t + \Delta t) = p _ {0 0} (t) p _ {0 1} (\Delta t) + p _ {0 1} (t) p _ {1 1} (\Delta t).
$$

Substituting linear approximations for $p _ { 0 1 } ( \Delta t )$ and $p _ { 1 1 } ( \Delta t ) { = } ( 1 { - } p _ { 1 0 } ( \Delta t ) )$ , we get

$$
p _ {0 1} (t + \Delta t) = p _ {0 0} (t) x \Delta t + p _ {0 1} (t) (1 - y \Delta t)
$$

$$
\frac {p _ {0 1} (t + \Delta t) - p _ {0 1} (t)}{\Delta t} = x p _ {0 0} (t) - y p _ {0 1} (t)
$$

$$
p _ {0 1} (t + \Delta t) - p _ {0 1} (t) = p _ {0 0} (t) x \Delta t - p _ {0 1} (t) y \Delta t
$$

Taking limit of both sides as $\Delta t {  } 0$

$$
\lim _ {\Delta t \rightarrow 0} \left[ \frac {p _ {0 1} (t + \Delta t) - p _ {0 1} (t)}{\Delta t} \right] = \lim _ {\Delta t \rightarrow 0} \left[ x p _ {0 0} (t) - y p _ {0 1} (t) \right]
$$

The above equality can be represented as,

$$
\frac {\mathrm{d} p _ {0 1} (t)}{\mathrm{d} t} = x p _ {0 0} (t) - y p _ {0 1} (t)
$$

rearranging the terms and putting $p _ { 0 0 } ( t ) { = } 1 { - } p _ { 0 1 } ( t )$ we get

$$
\frac {\mathrm{d} p _ {0 1}}{\mathrm{d} t} = x - p _ {0 1} (t) (x + y)
$$

$$
\frac {\mathrm{d} p _ {0 1}}{\mathrm{d} t} = (x + y) \left(\frac {x}{x + y} - p _ {0 1} (t)\right)
$$

Solving the differential equation, we get

$$
p _ {0 1} (t) = \frac {x}{x + y} - \frac {x}{x + y} \mathrm{e} ^ {- (x + y) t}
$$

Similarly, we can solve for other three functions, which are as follows:

$$
\begin{array}{r l} p _ {1 0} (t) & = \frac {y}{x + y} - \frac {y}{x + y} \mathrm{e} ^ {- (x + y) t} p _ {0 0} \\ & = \frac {y}{x + y} + \frac {x}{x + y} \mathrm{e} ^ {- (x + y) t} p _ {1 1} (t) \\ & = \frac {x}{x + y} + \frac {y}{x + y} \mathrm{e} ^ {- (x + y) t} \end{array}
$$

Table 3  
Operation processing times for outward fork experiments

<table><tr><td>Operation number</td><td>Processing time</td></tr><tr><td>1</td><td>0.98</td></tr><tr><td>2</td><td>2.30</td></tr><tr><td>3</td><td>2.30</td></tr></table>

Table 4  
Operation processing times for inward fork experiments

<table><tr><td>Operation number</td><td>Processing time</td></tr><tr><td>1</td><td>1.00</td></tr><tr><td>2</td><td>1.00</td></tr><tr><td>3</td><td>0.53</td></tr></table>

The functions can be expressed in the matrix form as follows:

$$
\begin{array}{l} p (t) = \left[ \begin{array}{c c} p _ {0 0} (t) & p _ {0 1} (t) \\ p _ {1 0} (t) & p _ {1 1} (t) \end{array} \right] \\ = \left[ \begin{array}{c c} \frac {y}{x + y} + \frac {x}{x + y} \mathrm{e} ^ {- (x + y) t} & \frac {x}{x + y} - \frac {x}{x + y} \mathrm{e} ^ {- (x + y) t} \\ \frac {y}{x + y} - \frac {y}{x + y} \mathrm{e} ^ {- (x + y) t} & \frac {x}{x + y} + \frac {y}{x + y} \mathrm{e} ^ {- (x + y) t} \end{array} \right] \end{array}
$$

There are several desirable properties of these functions: (1) all functions converge smoothly to a fixed value between 0 and 1, and (2) convergence is rapid.

In the real world situation, x and y numbers could be estimated statistically. For example, if the coordination and no-coordination times followed a negative exponential distribution having a cumulative distribution of $1 - \mathrm { e } ^ { - \lambda t }$ , then the expected value of the distribution is 1 / k.

Distributed learning with coordination took place in the following way: initially, jobs entered the system and waited in the first machine’s queue. The dispatcher (agent) connected to the machine selected a job from its queue for processing. After the job was processed on one machine, it entered the queue of the other machine where it waited for the next dispatcher to select it. When a job came out of the system, a payoff was calculated for the job depending on the payoff criterion. The value of the payoff was assigned to all the rules in different dispatchers that had selected the job for which the payoff was computed. After all the dispatchers received a payoff, dependent agent(s) paid tax to the coordinating agent. The tax values were updated after a specified number of jobs passed through the system.

Table 5  
Operation processing times

<table><tr><td>Operation number</td><td>Processing time</td></tr><tr><td>1</td><td>0.95</td></tr><tr><td>2</td><td>1.00</td></tr></table>

![](/api/attachments/34J8P5DD/fulltext/images/544b9b7fdefbb274b49ea97e0049e8229f7a64b983b4404da8668ba72f67bfb2.jpg)  
Fig. 7. An outward fork distributed learning without coordination.

In multi-machine multi-agent environment, coordination groups were defined before running the simulation. The effectiveness of a particular coordination group was dependent its structure. For example, in outward fork coordination group, if dependent agents were selecting jobs from a common queue, then the dependent agents may be considered as competing against each other and the information they share was common information (competing in perfect information). However, inward fork coordination group was slightly different. In inward fork coordination group, dependent agents did not share common information and were competing with each other (competing in asymmetric information).

## 4. Experiments and results

The system performance we were measuring was the total system performance. The total system performance was the overall system performance over the different GA learning episodes. A quick convergence and low variability ensured a higher overall system performance. In dynamic environment, quick convergence to higher performance was an important issue as a real time response was needed for machine breakdowns and other system related changes.

![](/api/attachments/34J8P5DD/fulltext/images/993b9fab9acfb360d36d3f6444088fe33e4bb873b554b4bf85e6d9d2fba58fd9.jpg)  
Fig. 8. An outward fork distributed learning with coordination.

![](/api/attachments/34J8P5DD/fulltext/images/903b1df8dcd6ffe37a7cffd381731fe04eb27d85ab5f342eae68ccdd5f052320.jpg)  
Fig. 9. An inward fork distributed learning without coordination.

The performance in the current research was the final payoff received at the end of a job processing sequence. The final payoff was determined by the payoff function based on a managerial objective. In this study, two payoff functions were considered: tardiness of jobs and flow time of jobs. The overall payoff was sum of the payoffs for all the jobs processed in a given simulation run. The effectiveness of multi-agent learning was based on the design of coordination strategies, where an effective coordination mechanism may improve the overall system performance, but a naive mode of coordination may even deteriorate performance [30,33].

Separate experiments were carried out for different types of coordination groups under different objectives. The first set of experiments involved testing the effectiveness of coordination for the three basic configurations detailed in previous section. The second set of experiments involved testing the proposed coordination strategy for one largescale multi-stage realistic setup. For a single type of coordination group, results were averaged over 30 random runs using common random numbers to reduce variance [28]. One single run consisted of two simulation experiments: one each for coordinated distributed (CD) learning and distributed learning (DL) without coordination respectively. In general, there were two objectives (minimize flow time and minimize tardiness), three types of coordination groups (outward fork, inward fork and straight line coordination) and two approaches (CD and DL). A total of 480 simulation experiments were carried out [no. of objectives(2) \* different random runs(30) \* no. of different coordination groups(3) \* no. of different approaches(2)] + [no. of objectives(2) \* different random runs(30) \* one large realistic setup(1) \* no. of different approaches(2)]. The difference of means between the two different approaches for each ob jective and each type of coordination was tested using a paired comparison t-test. The processing times were determined in a manner such that each machine has a queue accumulation in front of it. Tables 3, 4 and 5 illustrate the processing times used for outward fork, inward fork and straigh line coordination group respectively. An exponentia arrival rate of 0.90 was considered for all experiments. The processing time for an operation on a job was allowed to vary up to 50% of the values given in Tables 3–5. We did not consider any breakdowns for the three different types of coordination groups. Figs. 7–12 illustrate different setups for our experi ments. The DL scenerios use Bhattacharyya and Koehler’s [4] distributed learning, and the CD scenerios used the learning proposed in this paper. Each simulation experiment considered 100 GA learning episodes. Tables 6 and 7 summarize the difference in means between CD and DL for each of the scenerios and two different managerial objectives. Since the objectives were to minimize tardiness and flow times, we used Maximize $\scriptstyle \left( { \frac { 1 } { 1 + \mathrm { t a r d i n e s s } } } \right)$ and Maximize $\scriptstyle \left( { \frac { 1 } { 1 + \operatorname { f l o w } \_ { \mathrm { i i m e } } } } \right)$ as the GA fitness functions.

![](/api/attachments/34J8P5DD/fulltext/images/1cb86be5bd5417564dd36a1ef404c25964bdda288dbcdcc179c88c82fe8e3b02.jpg)  
Fig. 10. An inward fork distributed learning with coordination.

![](/api/attachments/34J8P5DD/fulltext/images/f000070b57d8599909755c84b723a9ff40c9552aa92299ae98452e0c32dedca8.jpg)  
Fig. 11. A straight line distributed learning without coordination.

![](/api/attachments/34J8P5DD/fulltext/images/f6f853d5b0172029ceee3f35c6cbabac6fc57e468429840437ca7786f8801e4c.jpg)  
Fig. 12. A straight line distributed learning with coordination.

The results in Tables 6 and 7 indicate that CD outperformed DL for the straight line and inward fork coordination schemes. However, for the outward fork coordination, results are either significant (tardiness) or not significant (flow time). One of the reasons for non-significant results for outward fork learning may be due to the sharing of same information about the jobs in the common queue. According to Shaw [33], one of the factors that improve performance of multi-agent systems is the number of hypotheses generated and the quality of input data. In general, with the increase in number of agents, the hypotheses generated by each agent increase, but the quality of inputs from each agent decreases. The similar behavior in performance can be attributed to the tradeoffs between the number of agents, common information sharing between the agents and quality of inputs from each agent. The common information sharing helped resolve the conflicts between the agents. The lack of conflicts and quick conflict resolution may have led to quick convergence and similar performance.

To improve generalization, we test our coordination scheme for a realistic setup adapted from a previous research reported in the literature [4]. A multi-stage shop floor with different queues and operations was considered. The simulated shopfloor setup used for testing the coordination scheme is shown in Fig. 13. An outward fork coordination group was defined with dispatcher attached to queue #6 being the coordinating agent and dispatchers attached to queues #7 and #8 as dependent agents. Unlike the previous experiments with the smaller configurations, machine breakdowns in the larger configuration were allowed. Processing times and arrival rates, shown in Table 8, were set so that queues accumulate over the coordinating machine, dependent agents and other machines that were not part of the coordination group such as machine serving queue #11. Separate experiments were conducted for each of the payoff criteria of minimizing tardiness and minimizing flow time. The queue accumulating machines #6, #7, #8 and #11 were the learning agents.

Table 6  
The t-test for difference in means for tardiness objective

<table><tr><td>Configuration</td><td>CD mean</td><td>DL mean</td><td>t-value</td><td>df</td><td>2-tail sig.</td></tr><tr><td>Outward fork</td><td>76,104.09</td><td>74,815.68</td><td>5.36</td><td>29</td><td>0.000*</td></tr><tr><td>Inward fork</td><td>177,003.60</td><td>176,595.30</td><td>5.35</td><td>29</td><td>0.000*</td></tr><tr><td>Straight line</td><td>89,991.84</td><td>87,621.88</td><td>7.13</td><td>29</td><td>0.000*</td></tr></table>

Table 7  
The t-test for difference in means for flow time objective

<table><tr><td>Configuration</td><td>CD mean</td><td>DL mean</td><td>t-value</td><td>df</td><td>2-tail sig.</td></tr><tr><td>Outward fork</td><td>13,698.12</td><td>13,927.00</td><td>-0.98</td><td>29</td><td>0.333</td></tr><tr><td>Inward fork</td><td>54,209.86</td><td>51,017.77</td><td>7.61</td><td>29</td><td>0.000*</td></tr><tr><td>Straight line</td><td>27,592.13</td><td>23,728.82</td><td>15.22</td><td>29</td><td>0.000*</td></tr></table>

A total of 120 experiments were conducted. The first 60 experiments were for flow time-based payoff with 30 runs for each of the 2 different learning approaches. Accordingly, the next 60 runs were for tardiness-based payoff. Setup times of 0.15 were considered for the change of operations on a machine. Machine breakdowns and repair times were calculated based on exponential rates shown in Table 9. Processing time for an operation was allowed to vary uniformly up to 50% about the values given in Table 9. Mean times for failure for tools numbered 1 through 4 were set high to avoid any failures during the simulation run. Tables 10 and 11 detail the results of the simulation runs and the t-tests on the difference of means.

The results indicated that there was a significant difference of means between the CD and the DL for the flow time-based objective. At 0.01 level of significance, CD performed the DL. This was not very consistent with the earlier results for smaller outward fork coordination, where there was no difference in CD and DL performance based on flow time-based objective. One of the problems with the earlier approach with smaller machine configurations was that machine breakdowns were not considered. In the current approach, machine breakdowns were considered. The incorporation of machine breakdown helped us to test the impact of speed of convergence in a multi-agent setting. For example, in a smaller outward fork configuration. it was observed that CD and DL showed a similar overall behavior expect for the fact that CD showed a quick initial convergence. For no breakdown case, a quick initial convergence had no impact over a long run. However, in case when machine breakdowns occur frequently, a quick convergence was a desirable property and may be viewed as a real time fault-tolerance mechanism. The overall effect of considering machine breakdowns showed that multi-agent coordination might be advantageous when machine breakdowns occur. The results of the tardiness-based objective indicated significant difference between CD and DL with CD performing better than DL at 0.01 level of significance.

![](/api/attachments/34J8P5DD/fulltext/images/3e6080afa2abb2081f00077b38fa5e1ebc4657906ff30d9f9fda73d815e57d85.jpg)  
Fig. 13. Multi-stage shop floor setup with an outward fork coordination group.

## 5. Summary, conclusions and future work

The focus of our research was to identify which types of business situations lend themselves to the design of cooperative intelligent systems and empirically demonstrate the design and application of multiagent system’s application for manufacturing. Using literature review, we developed a set of criteria that may be used to identify business situations that are suitable for the design cooperative intelligent systems. We then embarked on the design of a multi-agent system for manufacturing flow shop scheduling. We proposed a coordination scheme for a multi-agent system and tested it against an existing framework of multi-agent learning without coordination. The coordination scheme operated through a coordinating agent. The coordinating agent coordinated its actions with the other dependent agents by exchanging taxes. A tax was a percent of the total payoff that a dependent agent gave to the coordinating agent for coordinating its activities with the dependent agent. The total payoff was the combined performance of the agents for a given activity. The performance was determined by the managerial objective of the multiagent framework.

Table 8  
Operation processing times

<table><tr><td>Operation #</td><td>Processing time</td><td>Operation #</td><td>Processing time</td></tr><tr><td>1</td><td>0.06</td><td>10</td><td>0.06</td></tr><tr><td>2</td><td>0.06</td><td>11</td><td>1.65</td></tr><tr><td>3</td><td>0.46</td><td>12</td><td>1.65</td></tr><tr><td>4</td><td>0.46</td><td>13</td><td>0.06</td></tr><tr><td>5</td><td>0.46</td><td>14</td><td>0.06</td></tr><tr><td>6</td><td>0.06</td><td>15</td><td>0.15</td></tr><tr><td>7</td><td>0.06</td><td>16</td><td>0.075</td></tr><tr><td>8</td><td>0.69</td><td>17</td><td>0.06</td></tr><tr><td>9</td><td>0.06</td><td>18</td><td>0.06</td></tr></table>

Three basic coordination groups were proposed and used in our study. The three different types of coordination groups were inward fork, outward fork and straight-line. The three different coordination groups corresponded to three different types of dependencies between the agents. In an inward fork coordination group, many to one relationship was modeled. There were two agents that coordinated their actions with one coordinating agent. In an outward fork coordination group, one to many relationship was modeled. There was one coordinating agent that coordinated its actions with two dependent agents. The straight-line coordination modeled one to one relationship with one coordinating agent that coordinated its actions with one dependent agent.

Table 9  
Machine breakdown and repair time

<table><tr><td>Tool number</td><td>Mean time to failure</td><td>Mean time to repair</td></tr><tr><td>6</td><td>10,000</td><td>5.00</td></tr><tr><td>7</td><td>30,000</td><td>7.50</td></tr><tr><td>8</td><td>1000</td><td>7.50</td></tr><tr><td>9</td><td>4000</td><td>1.0</td></tr><tr><td>10</td><td>4000</td><td>1.0</td></tr><tr><td>11</td><td>4000</td><td>7.0</td></tr></table>

Table 10  
The t-test for difference in means for tardiness objective

<table><tr><td>CD mean</td><td>DL mean</td><td>t-value</td><td>df</td><td>2-tail sig.</td></tr><tr><td>179,288.60</td><td>177,807.30</td><td>6.43</td><td>29</td><td>0.000*</td></tr></table>

\* Significant at 99%.

A generalized framework of coordination was applied to a manufacturing shop floor environment. The agents in the manufacturing shop floor were the dispatchers that dispatched jobs over a machine. The agents contained a knowledge base of dispatching rules and a genetic algorithm that learns new dispatching rules over time. Genetic learning worked through the survival of the fittest principle. The fitness of the rules, upon their evaluation, was determined by the performance objectives. The performance objectives that were considered here were minimizing flow time of jobs and minimizing tardiness of jobs. Separate experiments were conducted for each of the individual payoff functions. Two different sets of experiments were conducted. The first set of experiments involved testing the coordination strategy for three different types of coordination groups under ideal conditions with no breakdowns in machines. The second set of experiments involved testing coordination for a realistic larger configuration [4] with machine breakdowns.

The results of the experiments indicated the overall utility of coordination. At 0.01 level of statistical significance, differences were found between the performance of no-coordination-based learning and coordination-based learning in all cases except for outward fork coordination group with minimize flow time objective and no machine breakdowns. The inconsistency in results with regard to outward fork for flow time objective may be explained by the basic difference between the structural representation of outward fork coordination group and the inward fork and straight line coordination groups.

The results of our study are generalizable for the conditions set in our experiments. However, much can be done to improve the generalizability and results of our study. For example, in the current research, a <sup>b</sup>prescriptive<sup>Q</sup>, rather than a <sup>b</sup>descriptive<sup>Q</sup>, <sup>Q</sup>, approach to multi-agent coordination was used. The agents coordinated to maximize their own individual utilities. Some DAI researchers were critical of using the individualistic approach to designing systems. Gasser [15] said <sup>b</sup>society comes first<sup>Q</sup> and opposed the individualistic and psychological approach to DAI systems. AI researchers have long considered that AI was concerned with individual mind (individual intention, action, etc.) and DAI was concerned with social actions (collective mind, intention, etc.) and mental states which are shared, joint, and sometimes collective [27]. From the critical standpoint, the current research ignored social relations and long-term commitments. Issues such as coordination and dependence that were independent of agent awareness and choice were not considered in the current research. These issues need consideration in the future if the <sup>b</sup>social<sup>Q</sup> view of the agent was to be adopted.

Given that the collective group performance relied upon the objective structure of interdependence among individual agents, our research approach (individual intention, action, etc. of agents) offered several advantages over adopting the <sup>b</sup>social<sup>Q</sup> view of the agent. Some of the advantages were:

1. Agents do not imply mutual belief of the overall plan.

2. Mutual dependence between dependent agent and cooperative agent (as both share the common goal) ruled out the situations of competition [10,18].

Table 11  
The t-test for difference in means for flow time objective

<table><tr><td>CD mean</td><td>DL mean</td><td>t-value</td><td>df</td><td>2-tail sig.</td></tr><tr><td>25,973.76</td><td>25,768.25</td><td>5.06</td><td>29</td><td>0.000*</td></tr></table>

\* Significant at 99%.

The common goal assumption helped resolve the conflict (tax structure) between the agents as the social norm appears to be <sup>b</sup>higher taxes should result in higher future overall payoff<sup>Q</sup> and <sup>b</sup>no to very limited cheating between the agents (breakdowns)<sup>Q</sup>. This norm may cease to exist when agents do not share common goals and/or have their own local goals. Local goals may induce competition and conflict between the agents in the current framework and conflict resolution using the current coordination scheme might be limited. Future work needs to be done in investigation coordination where agents in multiagent framework do not share common goal.

Most of the experiments in the current research assumed that the belief about mutual dependence holds true. Under the assumption of mutual dependence, each agent believed that it depends on other agents to achieve its goal. The mutual dependence fostered cooperation between the agents. In most cases, under the assumption of mutual dependence, coordination worked rather well and no misunderstandings occurred. In the case where some of the agents failed to perform (machine breakdowns), the mutual dependence assumption was violated. A dependent agent was cheated (as a result of coordinating agent breakdown). The question of cheating raises a number of questions such as, can a coordination group be efficient if some of the agents spend all their resources without being adequately rewarded or without being able to achieve their own goals? How can a self-interested agent decide to do something for the group, which may cost it more than it gains? How does an agent cope with cheating (machine break downs)? Are social norms that prevent cheating required? (this may need to change an individualistic agent to approach to a <sup>b</sup>social agent<sup>Q</sup> approach proposed by critics). It appears that the mutual dependence assumption was the single most important success factor of the proposed coordination scheme. The mutual dependence assumption with limited or no cheating encouraged the agents to coordinate and resolve conflicts (in terms of adjustment of taxes) and speed up the convergence. Serious violations to the mutual dependence assumptions might be a potential pitfall for the current coordination scheme and need future investigation. Some of the avenues for the extension of the current coordination scheme are: (1) redesign the coordination scheme that penalizes an coordinating agent for cheating (breakdowns) and (2) develop a set of norms regulating the coordination between the agents in a way that is beneficial for the whole group and not for any agent in particular.

## References

[1] L. Atlan, J. Bonnet, M. Naillon, Learning distributed reactive strategies by genetic programming for the general job shop problem, Proceedings of the Seventh Annual Florida Artificial Intelligence Research Symposium, 1993.

[2] Aytug Haldun, S. Bhattacharyya, G.J. Koehler, J.L. Snowdon, A review of machine learning in scheduling, IEEE Transactions on Engineering Management 41 (2) (1994).

[3] R. Bhaskar, P.C. Pendharkar, Wisconsin division of narcotics uses multi-agent information system for drug crime investigation, Interfaces (1999) 77 – 87.

[4] S. Bhattacharyya, G.J. Koehler, Learning by objectives for adaptive shop-floor learning, Decision Sciences 29 (2) (1998) 347– 376.

[5] A.H. Bond, L. Gesser (Eds.), Readings in Distributed Artificial Intelligence, Morgan Kaufmann, San Mateo, CA, 1988.

[6] T. Bui, Building agent-based corporate information systems: an application to telemedicine, European Journal of Operational Research 122 (2000) 242–257.

[7] H.H. Bui, S. Venkatesh, D. Kieronska, Learning other agents’ preferences in multi-agent negotiation using the bayesian classifier, International Journal of Cooperative Information Systems 8 (4) (1999) 275– 294.

[8] L. Bull, T.C. Fogarty, M. Snaith, Evolution in multi-agent systems: evolving communicating classifier systems for gait in a quadrupedal robot, International Conference on Genetic Algorithms, 1995.

[9] P. Ciancarini, Coordinating multiagent applications on the www: a reference architecture, IEEE Transactions on Software Engineering 24 (5) (1998) 362–375.

[10] R. Conte, M. Miceli, C. Castelfranchi, Limits and levels of cooperation: disentangling various types of prosocial interaction, in: Y. Demazeau, Muller (Eds.), Decentralized Artificial Intelligence, Elsevier Science Publishers, 1991.

[11] R. Davis, R.G. Smith, Negotiation as a metaphor for distributed problem solving, Artificial Intelligence 20 (1) (1983) 63– 109.

[12] Alan R. Dennis, Joey F. George, Len M. Jessup, Jay F. Nunamaker Jr., Douglas R. Vogel, Information technology to support electronic meetings, MIS Quarterly 12 (4) (1988) 591-624

[13] E.H. Durfee, V.R. Lesser, D.D. Corkill, Trends in cooperative distributed problem solving, IEEE Transactions on Knowledge and Data Engineering (1989) 63– 83.

[14] P.H. Farquhar, Applications of utility theory in artificial intelligence research, in: D.E. Brown, C.C. White III (Eds.), Operations Research and Artificial Intelligence: The Integration of Problem-Solving Strategies, Kluwer Academic Publishers, 1990, pp. 197– 214.

[15] L. Gasser, Knowledge and action at social and organizational level, American Association Artificial Intelligence, Fall Symposium, Asilomar, CA, 1991.

[16] T. Haynes, R. Wainwright, S. Sen, D. Schoenefeld, Strongly typed genetic programming in evolving cooperation strategies, International Conference on Genetic Algorithms, 1995.

[17] C. Hewitt, Open information systems semantics for distributed artificial intelligence, Artificial Intelligence 47 (1991) 79– 106.

[18] N. Jennings, On being responsible, in: E. Werner, Y. Demazeau (Eds.), Decentralized Artificial Intelligence, Elsevier/North Holland, 1992.

[19] L.P. Kaelbling, M.L. Littman, A.W. Moore, Reinforcement learning: a survey, Journal of Artificial Intelligence 4 (1996) 237–285.

[20] V.R. Lesser, Cooperative multiagent systems: a personal view of the state of the art, IEEE Transactions on Knowledge and Data Engineering 11 (1) (1999) 133–142.

[21] Y. Luo, D.N. Davis, K. Liu, A multi-agent decision support fo stock trading, IEEE Network 16 (1) (2002) 20– 27.

[22] A. Madni, M. Samet, Purcell, Adaptive models in information management, in: S.J. Andriole (Ed.), Applications in Artificial Intelligence, Petrocelli, Princeton, NJ, 1985, pp. 279 – 294.

[23] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87– 119.

[24] T.W. Malone, K. Crowston, J. Lee, B. Pentland, C. Dellarocas, G. Wyner, J. Quimby, C.S. Osborn, A. Bernstein, G. Herman, M. Klein, E. O’Donnell, Tools for inventing organizations: toward a handbook of organizational processes, Management Science 45 (3) (1999) 425– 443.

[25] B. Moulin, B. Chaib-Draa, An overview of distributed artificial intelligence, in: O’Hare, Jennings (Eds.), Foundations of Distributed Artificial Intelligence, John Wiley and Sons, 1996, pp. 3 – 55.

[26] M.A. Nour, D. Yen, Group, decision support systems towards a conceptual foundation, Decision Sciences 23 (1992) 55 – 64.

[27] G.N. O’Hare, N.R. Jennings, Foundations of Distributed Ar tificial Intelligence, John Wiley and Sons, New York, 1996.

[28] A. Ravindran, D.T. Phillips, J.J. Solberg, Operations Research, John Wiley and Sons, New York, 1987.

[29] S. Sarkar, M. Ramaswamy, Knowledge base decomposition to facilitate verification, Information Systems Research 11 (3) (2000) 260– 283.

[30] A. Schaerf, Y. Shoham, M. Tennenholtz, Adaptive load balancing: a study in multi-agent learning, Journal of Artificia Intelligence Research (1995) 475 – 500.

[31] C. Schneeweiss, Distributed decision making—a unified approach, European Journal of Operational Research 150 (2003) 237–252.

[32] S. Sen, E.H. Durfee, A formal study of distributed meeting scheduling, Group Decision and Negotiation 7 (3) (1998) 265–289.

[33] M.J. Shaw, Cooperative problem-solving and learning in multi-agent information systems, International Journal of Computational Intelligence and Organizations 1 (1) (1996) 21– 34.

[34] M.J. Shaw, A.B. Whinston, Learning and adaptation in distributed artificial intelligence, in: L. Gasser, M.N. Huhns (Eds.), Research Notes in Artificial Intelligence, vol. 2, Pitman, London, 1989, pp. 413– 429.

[35] R. Sikora, M.J. Shaw, A distributed problem-solving approach to inductive learning, Faculty Working Paper 91-0109, College of Commerce and Business Administration, University of Illinois at Urbana-Champaign, 1991.

[36] R. Sikora, M.J. Shaw, A multi-agent framework for the coordination and integration of information systems, Management Science 44 (11) (1998) S65 – S78.

[37] S.F. Smith, A learning system based on genetic adaptive algorithms, PhD Dissertation, University of Pittsburgh, 1980.

[38] R. Sun, T. Peterson, Multi-agent reinforcement learning: weighting and partitioning, Neural Networks 12 (1999) 727– 753.

[39] K. Sycara, S. Rothm, N. Sadeh, M. Fox, An investigation into distributed constraint-directed factory scheduling, Proceedings of Sixth IEEE Conference on AI Applications, Santa Barbara, CA. March, 1990.

[40] M.A. Vonderembse, G.P. White, Operations Management Concepts, Methods and Strategies, West Publishing Company, 1991.

[41] G. Weiss, Action selection and learning in multi-agent environments, Proceedings of the Second International Conference on Simulation of Adaptive Behavior, 1992.

[42] G. Weiss, Learning to coordinate actions in multi-agent systems, Distributed Artificial Intelligence (1994) 311 – 316.

[43] G. Weiss, Adaptation and learning in multi-agent systems: some remarks and a bibliography, Proceedings of IJCAI’ 95 Workshop, Montreal, Canada, 1995.

[44] M.P. Wellman, J. Hu, Conjectural equilibrium in multiagent learning, Machine Learning 33 (1998) 179–200.

[45] B.P. Yen, Communication infrastructure in distributed scheduling, Computers & Industrial Engineering 42 (2002) 149 – 161.

Parag C. Pendharkar is an Associate Professor of Information Systems at Penn State Harrisburg. His work has appeared or was accepted for publication in Annals of Operations Research, Communications of ACM, Computers and Operations Research, Decision Sciences, Decision Support Systems, European Journal of Operational Research, Expert Systems with Applications, IEEE Transactions on Professional Communication, Information and Management, Intelligent Systems in Accounting Finance and Management, Interfaces, International Journal of Human–Computer Studies, Multiple Valued Logic, Omega, as well as several other journals. Currently, he serves on the editorial board of the International Journal of Human–Computer Studies.
