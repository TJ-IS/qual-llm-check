---
otero_id: 1346
otero_key: "BY48U6PG"
title: "A framework for designing policies for networked systems with uncertainty"
authors: "Surya Pathak; Mark McDonald; Sankaran Mahadevan"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.01.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for designing policies for networked systems with uncertainty

Surya Pathak <sup>a,</sup>⁎, Mark McDonald <sup>b</sup>, Sankaran Mahadevan b

<sup>a</sup> Business Program, University of Washington, Bothell, WA, 98011, United States

<sup>b</sup> Department of Civil and Environmental Engineering, Vanderbilt University, Nashville, TN, 37235, United States

## a r t i c l e i n f o

Article history: Received 26 November 2007 Received in revised form 15 January 2010 Accepted 20 January 2010 Available online 28 January 2010

Keywords: Policy design Transportation network System of systems Optimization Uncertainty Agent-based modeling Network systems Lyapunov exponent

## a b s t r a c t

This paper presents a framework to design policies for networked systems. The framework integrates model building, stability analysis of dynamic systems, surrogate model generation and optimization under uncertainty. We illustrate the framework using a transportation network benchmark problem. We consider bounded rational users and model the network using software agents. We use Largest Lyapunov exponents to characterize stability and use Gaussian process model as an inexpensive surrogate, facilitating computational ef<sup>fi</sup>ciency in policy optimization under uncertainty. We demonstrate scalability by solving a traf<sup>fi</sup>c grid policy design problem and show how the framework lends itself towards carrying out stability versus performance tradeoffs.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

During the past decade there has been a growing interest in developing conceptual, methodological and analytical approaches for studying large scale inter-disciplinary problems that are embedded in networks at multiple levels and multiple domains [36]. Such systems typically consist of networks that have multiple decision makers and exhibit operational and managerial independence, geographical distribution, and emergent behavior [15]. Modern transportation and supply networks, critical infrastructure networks, energy and power networks [36] display such properties. For example, transportation networks in US metropolitan cities typically have multiple modes of transportation (roadways with passenger cars, buses, and subway and ferry system). Collections of these individual networks are used by numerous users, who display different kinds of user behavior (risk averse, risk taking, rational, bounded rational). The individual networks are managed by independently governed units with managerial independence and are affected by changes in the surrounding uncertain environment resulting in distinct <sup>fl</sup>ow patterns (on each of these systems). Similar properties are observed in supply networks in which multiple independent organizations displaying heterogeneous behavior while operating under an uncertain environment to ful<sup>fi</sup>ll customer demand, display distinct patterns of product and information <sup>fl</sup>ow and changing topological structures.

While research in the <sup>fi</sup>eld of policy design for real life networked system has evolved from the initial days of drawing in<sup>fl</sup>uence diagrams [35], it is still considered a challenge to integrate the above mentioned dynamisms within a policy design framework that can accommodate complex network topologies, diverse user behavior and rich set of system-user interactions [36]. In this paper we suggest an approach that follows the same trend of model building, model analysis and decision making as used by multitude of researchers [3,7,8,24,30,34–36] and presents comprehensive additions in the form of stability analysis and surrogate model representation to better address the non-linearity and dynamism in real life networked systems. The four step approach can be summarized into a logical framework as (See Fig. 1):

1. Modeling of system behavior along with user behavior: while our framework is not limited to any particular modeling methodology we demonstrate our example problems using agent based simulations to capture how system response changes as individual users interact with the network in order to achieve their goal, and how the individual user behavior is impacted by the system state.

2. Analyzing system response behavior for stability conditions: recent literature on large scale system design [3,37] suggests that optimal solutions in networked systems should be carried out in the stable region of operations in order for the optimal policy to be effective. Design of policy in chaotic regime defeats the purpose of an optimal policy design approach. Thus we ensure that the set of input and decision variables being considered yields stable system response behavior before optimizing policy variables.

![](/api/attachments/BY48U6PG/fulltext/images/286180a62e3fc39f1d11396e071e6eb362150a728fef11265f4c656c74d738c4.jpg)  
Fig. 1. Framework for policy optimization in network systems.

3. Constructing an inexpensive surrogate for the expensive agentbased simulation: The computational effort associated with the use of agent-based modeling (ABM) for optimization in the presence of uncertainty is enormous. Three types of iterative analyses are required: system and user simulation, uncertainty analysis and optimization. Construction of a surrogate model reduces the computational expense and facilitates the estimation of expected value of the system response behavior which can then be used further in the optimization process.

4. Optimizing policy variables through stochastic optimization: as described above network systems typically have multiple types of uncertainties associated with them. In order to design an optimal policy for such systems a stochastic optimization approach where the problem formulation includes system response variables, the input variables and the decision (policy) variables and their stochastic characteristics is necessary. Use of a surrogate model representation further reduces the complexity of implementing optimization routines as full grid searches become feasible. We demonstrate this with our two examples later in the paper.

In order to illustrate our framework we use a popular benchmark problem as a veri<sup>fi</sup>cation problem in the transportation network literature called the Braess network [6] that has been widely used by researchers [12,13,25,36,37,42,53]. The Braess network consists of a single origin-destination (OD) pair and four nodes. We later use a single random input (random demand) and a single policy control variable (<sup>fl</sup>ow split at the origin node) to illustrate each of the four steps mentioned above. First we use an agent-based modeling (ABM) approach for modeling the Braess network with multiple users with bounded rational behavior [54]. Second, we compute the Largest Lyapunov exponent (LPE) [20,46,47,50] to analyze the stability of the system response behavior. Next, we estimate a closed functional form of the overall system cost (system response behavior) using a Gaussian process (GP) surrogate estimation technique [43]. Finally we perform stochastic optimization to <sup>fi</sup>nd the value for the <sup>fl</sup>ow-split policy variable that minimizes the total system cost in the network. We then illustrate scalability of our framework by designing policies for a traf<sup>fi</sup>c grid with 25 signalized intersections, 80 links and 10 times the number of users as compared to the veri<sup>fi</sup>cation problem. We also introduce stability response surfaces as a trade off tool while selecting policies for a network system

While the individual tools used in this framework are proven and tested individually; to the best of our knowledge, they have never been used together to methodically approach policy design problems for networked systems. The primary contribution of this paper is the synthesis of model-based network system representation, stability analysis of dynamic systems, surrogate model reconstruction and optimization under uncertainty (OUU) within an overarching framework, enabling design of stable policies for network systems. Strengths of this framework include the ability to use any modeling approach for representing the system. We impose no constraints except for the requirement that a system model can be used to generate training data for stability analysis and surrogate model reconstruction (in the form of time series representation of dependent and independent variables). A novel aspect of this research is the stability analysis of the dynamic system responses and surrogate reconstruction of a stability surface. As shown in the later sections with one of our complex network (a hypothetical urban traf<sup>fi</sup>c grid) demonstrations, stability surfaces can be used for making tradeoffs between different policy aspects in a networked system along with ensuring that the designed policies are selected from a stable operating zone. The integration of Gaussian Process Models (GP) in this framework enables construction of the stability surface while also allowing us to use a cheap surrogate representation of the system in the optimization process. The inexpensive computation time provided by the GP model allows us to use very simple optimization routines such as line searches and full grid searches.

Section 2 presents the background literature on network system modeling and simulation. Section 3 introduces the Braess network (veri<sup>fi</sup>cation problem) and policy design formulation. Section 4 presents detailed step by step illustration of the agent-based model for the Braess system. Section 5 presents the LPE analysis while Section 6 discusses the surrogate model construction. Section 7 presents a stochastic optimization approach for <sup>fi</sup>nding the optimal design value for the policy variable. Section 8 then illustrates scalability of our framework. Section 9 concludes and suggests future research.

## 2. Background

Researchers from diverse domains such as transportation system design [13,53], supply network design [11,36], and more recently super network (overlapping transportation and supply networks) [37,42] and emergency response network design [3] have attempted to design optimal economic and operational control policies for network systems. For example, in transportation network and supply network design, the approaches include: system and user equilibrium behavior models (logit and probit models) [13,53], variational inequality formulations that consider multiple user types and multiple classes of networks (super networks), and system dynamics formulations for time dependent problems [37]. Several solution approaches such as stochastic programming, discrete time and discrete event simulations and multidisciplinary optimization methods [24,27,40] have been considered. Additionally researchers in facility network layout design [14,17,44] have considered uncertainty associated with demand generation, <sup>fi</sup>xed costs, transportation between nodes etc. while suggesting numerous solution approaches for designing optimal solutions/policies such as dynamic programming [28], lagrangian heuristics [1], genetic algorithms [4], and tabu-search [2] to name a few.

Carley and Kamneva [8] have developed a dynamic network analysis and optimization approach for improving organizational policy design while addressing some of the above mentioned issues. They represent network systems in the form of a relationship matrix between the nodes of the network and use Monte Carlo and simulated annealing-based heuristic optimization methods to minimize vulnerabilities (de<sup>fi</sup>ned by underlying metrics such as workload distribution, resource distribution etc.) in the relationship matrix. This approach takes a mission-driven perspective and as the missions change a new relationship matrix is fed into the optimizer which yields a new set of results. Mohapatra and Sharma [35] have used an alternative approach for policy design using modal control theory. They treat policy variables as control variables by delinking them from other system variables. Provided that this reduced system is linear and controllable, it is possible to synthetically generate control policies by modal control theory to ensure any prescribed degree of stability. These theoretical control policies then can be used to design realistic policy decisions. One of the possible limitations of this approach is the assumption that policy variables can be completely delinked.

While research in these areas has advanced the state of the art in optimal policy design for networked systems, there are limitations in the form of <sup>fi</sup>xed and static network topologies, assumption of <sup>fi</sup>xed and perfectly rational user behavior (or <sup>fi</sup>rm behavior in the case of organizational networks), sealed-off nature of the solutions (limited ability to combine micro-level user behavior with macro level parameters) [21], lack of stability considerations while designing the solutions, and mathematical intractability for larger scale problems. In reality, network systems such as mentioned above display dynamic emergent behavior [7] in the form of evolving topologies [26,40], diverse system response (such as equilibrium <sup>fl</sup>ow patterns in a traf<sup>fi</sup>c network or population dynamics in a supply network), bounded rational user behavior [9,54] and instability and chaos [10].

Additionally, network systems have multiple sources of uncertainty associated with them. There are aleatory uncertainties in the form of random demand (varying number of users using a transportation network), and randomness in speed, <sup>fl</sup>ow or density (the three are interrelated). There is epistemic uncertainty associated with the information <sup>fl</sup>ow in the network and individual user behavior. For example in a transportation network, information provided to users in the form of advanced traveler information systems (ATIS) may be uncertain. Also individual users lack the knowledge of how the rest of the users are behaving. Thus a user while taking a decision makes adjustments based on his/her perception of the state of the system and how the other users are behaving. Thus network policy optimization needs to properly account for the various sources of uncertainty in addition to addressing the challenges mentioned above.

## 2.1. Model based representation

A networked system can be modeled using many different approaches. We discuss the pros and cons of some popular approaches in this section.

## 2.1.1. Equation-based approaches

Traditional paradigms for modeling networks include user equilibrium, based on the concepts of equilibrium in n-person games [38], and system optimality [55], in which the total system cost, represented in terms of input and decision variables is minimized. Nash equilibrium assumes self-interested behavior and perfectly rational users, while system optimality implies that all decisions are made by a central authority. Although both user equilibrium and system optimality assumptions are useful in the design and analysis of network systems, both assumptions are too restrictive. Typically in network-based systems the behavior is driven by multiple classes of users [37] who are locally optimal in their decision making and are seldom fully rational in their behavior. Thus, if the user behavior assumptions are incorrect, the resulting behaviors observed from changes in network policies could be signi<sup>fi</sup>cantly different from what is expected.

Another network system modeling technique is to use system dynamics [22] that uses concepts of stocks and <sup>fl</sup>ows along with feedback and time delay relationships to model the dynamic behavior of network systems. System dynamics is extremely useful for identifying the important variables and causal linkages in a system. Whether game-theoretic or system dynamics-based, one of the major limitations of the equation-based methods is their need for mathematical representation of both system and user behavior. The number of decision sub-problems that need to be analyzed grows very large and quickly becomes mathematically intractable as the underlying network system grows larger and more complex. Also multiple classes of users with heterogeneous decision making capabilities further increase the dif<sup>fi</sup>culty in the equation-based approach.

## 2.1.2. Agent-based approaches

Agent-based modeling (ABM) is yet another technique that can be used for representing network-based systems. An agent in an ABM model is a persistent entity with an internal state which interacts with other agents, mutually modifying each others' states [21,52]. Thus an agent-based model consists of a collection of agents and their states, the rules governing the interactions of the agents, and the environment within which they operate. The state of an agent can be arbitrarily simple, such as position, or the color of a cell in a cellular automaton [21,52]. States can also be extremely complicated, including, possibly, sophisticated internal models of the agent's world [52]. Agent-based models typically utilize a bottoms-up approach and represent entities, their behaviors and their interactions while investigating emergent behavior, as compared to equationbased models that typically model aggregate system behavior. Thus ABMs are very well suited for capturing heterogeneous classes of users and multiple autonomous decision makers displaying bounded rational behavior, typical constituents of a network-based system. ABMs have been used in multiple disciplines such as e-commerce [29], power market design [57], social sciences [5], operations management [40], complexity science [52], and computer science [45], for solving problems with similar characteristics as described above. We utilize agent based models in this paper for representing the traf<sup>fi</sup>c networks. Using agents allows us to model bounded rational user behavior which is a key attribute of a real life network system.

## 2.2. Simulation as a common formalism

Whether network systems are modeled using equation-based approaches or using ABMs they share a common problem characteristic; they have interactions among users and environment which results in emergent patterns over time. For example, in supply networks, the topology of the network emerges over time driven by <sup>fi</sup>rm-to-<sup>fi</sup>rm interactions [40], and in transportation networks traf<sup>fi</sup>c <sup>fl</sup>ow behavior emerges over time driven by individual decisions made by users. Simulation methods [61] are capable of capturing the time dependent structural and behavioral emergence as well as the information exchange between the multiple components of such network systems. Particularly, discrete-time simulation formalism captures the notion of time-dependent emergence of network systems whereas discrete event formalism captures exchange of information between multiple components [61]. In the case of equation-based approaches, the discrete-time or discrete-event formalisms are typically represented with explicit algebraic, differential and/or difference equations. In the case of ABMs high level computer languages provide support for modeling discrete-time (e.g. thread based design [31]) and discrete-event formalisms (e.g., message passing [19]). In most real-world network system problems a hybrid approach combining both discrete-time and discrete-event formalisms is needed. One of the highlights of our framework as suggested earlier is that it is agnostic to the modeling methodology.

![](/api/attachments/BY48U6PG/fulltext/images/7242ae3673999bda52dbfeed59fbe668b3b95add916349b8dc4f9db741aaca95.jpg)  
Fig. 2. The Braess network.

## 3. Example network system: Braess network

As mentioned previously we use the well-known Braess network in Fig. 2 [6,36] to illustrate the suggested policy design metaframework in Fig. 1. The Braess network is a well benchmarked system in the transportation literature and one of the primary reasons behind selecting such a network was to use results from previous studies [36] as a means of verifying the agent-based representation of the network system. Though the Braess network is a simpli<sup>fi</sup>ed version of a networked system, consisting of a single road network and multiple bounded rational users, it preserves the characteristics of large complex network systems, namely, autonomous and bounded rational decision makers, user-network interactions and dynamic and emergent system equilibrium (traf<sup>fi</sup>c <sup>fl</sup>ow patterns). In particular, each individual user interacts with the rest of the system by playing a game in the form of making optimal travel choices based on the underlying decision logic and the current network <sup>fl</sup>ow (Fig. 2).

In the <sup>fi</sup>rst network depicted in Fig. 2, there are four nodes: (1, 2, 3, and 4), four links (a, b, c, and d), and a single O/D pair (1, 4). There are, hence, two paths available to travelers between this O/D pair: path $p _ { 1 } = ( \mathsf { a } , \mathsf { c } )$ and path $p _ { 2 } = ( \mathsf { b } , \mathsf { d } )$ . The user link travel cost functions are:

$$
c _ {a} (x _ {a}) = 1 0 x _ {a}, c _ {b} (x _ {b}) = x _ {b} + 5 0, c _ {c} (x _ {c}) = x _ {c} + 5 0, c _ {d} (x _ {d}) = 1 0 x _ {d}.
$$

The Total system cost C is the summation over the set of all paths P of user costs on each path p times the <sup>fl</sup>ow on that path, and is given by:

$$
C = C _ {p} ^ {*} f _ {p}, \forall p \in \text { all   paths } P, f _ {p} \text { is   the   total   flow   on   path } p\tag{1}
$$

where C is the cost of travel for all users, and $C _ { p }$ is the cost incurred by all users on a path, i.e.

$$
C _ {p} = \sum_ {i \in \mathfrak {R}} c _ {i} (x _ {i}) ^ {*} x _ {i}\tag{2}
$$

where $x _ { i }$ is the <sup>fl</sup>ow on link i and $c _ { i } ( x _ { i } )$ is the cost of travel over link i.

Assume a <sup>fi</sup>xed travel demand of 6. It is easy to verify that the equilibrium path <sup>fl</sup>ows are: $f _ { 1 } ^ { 1 4 } { = } f _ { 2 } ^ { 1 4 } { = } 3$ . Note that the superscripts indicate the origin and destination nodes and that the subscripts indicate the path taken. The equilibrium link <sup>fl</sup>ows are: $\scriptstyle x _ { a } = x _ { b } = x _ { c } = x _ { d } = 3$ , with associated equilibrium path travel costs: $C _ { 1 } ^ { 1 4 } { = } C _ { 2 } ^ { 1 4 } { = } 8 3 .$

Assume now that, as depicted in Fig. 2, a new link $" e "$ , joining node 2 to node 3 is added to the original network (thus giving rise to the Braess network), with user link cost function $\pmb { c } _ { e } ( \pmb { x } _ { e } ) = \pmb { x } _ { e } + \pmb { 1 0 } .$ The addition of this link creates a new path $p 3 = ( a , e , d )$ that is available to the travelers. Assume that the travel demand remains at 6 units of <sup>fl</sup>ow. Note that the original <sup>fl</sup>ow distribution pattern $f _ { 1 } ^ { 1 4 } { = } 3 , f _ { 2 } ^ { 1 4 } { = } 3$ and $f _ { 3 } ^ { 1 4 } = 0$ is no longer an equilibrium pattern, since at this level of <sup>fl</sup>ow the user cost on path p3, $C _ { 3 } ^ { 1 4 } { = } c _ { a } + c _ { b } + c _ { c } { = } 7 0$ . Hence, users from paths p1 and $p 2$ would switch to path $p 3 .$

![](/api/attachments/BY48U6PG/fulltext/images/f613388f7764b7710eb547aa395a5b0a6d27e3c71941775ad6f303fe95a4d316.jpg)  
Fig. 3. Netlogo screen shot for the ABM representation of the Braess system.

The equilibrium <sup>fl</sup>ow pattern on the new network is: $f _ { 1 } ^ { 1 4 } = 2$ $f _ { 2 } ^ { 1 4 } = 2$ , and $f _ { 3 } ^ { 1 4 } = 2 .$ . Hence the equilibrium link <sup>fl</sup>ows are: $x _ { a } = 4 ,$ $x _ { b } = 2 , x _ { c } = 2 , x _ { d } = 4 , x _ { e } = 2$ . The equilibrium user path travel costs are, $C _ { 1 } ^ { 1 4 } = C _ { 2 } ^ { 1 4 } = C _ { 3 } ^ { 1 4 } = 9 2$ . It can be veri<sup>fi</sup>ed that any reassignment of the path <sup>fl</sup>ows would yield a higher travel cost on a path, and hence an unstable <sup>fl</sup>ow pattern. Note that the travel cost increased for every user of the network from 83 to 92 without a change in the total demand, and that the system performance diminished as a result of the addition of the link.<sup>1</sup> Hence the total system cost, calculated as the sum of all link <sup>fl</sup>ows multiplied by all link travel times, would change from 498 to 552.

## 3.1. Policy design problem formulation for the Braess network

As seen in the previous section, the addition of a traveler choice worsens the overall system cost. We now introduce a traf<sup>fi</sup>c <sup>fl</sup>ow control mechanism at node 1 such that it will split the incoming traf<sup>fi</sup>c <sup>fl</sup>ow optimally between link a and link b, in order to reduce the overall system cost. For example, this could be achieved by a timed signal at the origin that stays on for a certain period of time for link a and b or by levying a toll on one of the links. To make the problem realistic we introduce a few enhancements to the above Braess network problem and present an optimization problem formulation for the policy design scenario.

1. Instead of having a static demand (as in the case of the benchmark problem presented in the previous section), we consider a Poisson process driving the demand Q. Further the average occurrence rate in the Poisson process is modeled as a normal random variable.

2. The individual users using the network are considered to be bounded rational. They only look one link ahead and select the lowest cost link available.

3. The suggested policy, in order to decrease the overall system cost, is to introduce a <sup>fl</sup>ow control variable T at node 1. Given an initial demand $\updownarrow ( T / 1 0 0 \textsuperscript { * } Q )$ users are forced to travel on link a and $( 1 - T / 1 0 0 ) \ ^ { * } Q$ users travel on link b. Users arriving at node 2 behave in a bounded rational way as described above and select the lowest cost link between c and e.

4. The policy design problem is then to design an optimal value for T such that the overall system cost for all users is minimized. Or in other words:

“Minimize the overall system cost with respect to the policy variable T such that the net flow on the network is conserved (flow constraints) and the net flow on any link is greater than equal to zero”

This can be formally represented as a stochastic optimization problem with equilibrium constraints:

minE<sub>ð</sub>C<sub>ð</sub>T<sub>ÞÞ</sub>

s:t: $\sum _ { p } f _ { p } ^ { r s } = Q ^ { r s }$ ∀r∈ℜ; s∈S

Agent Route Choice Behavior

$$
f _ {p} ^ {r s} \geq 0 \forall p \in P, r \in \mathfrak {R}, s \in S.
$$

## 4. Proposed policy design methodology

## 4.1. Agent-based representation of the Braess network

The <sup>fi</sup>rst step in the policy design process as discussed previously is to build an agent-based representation of the underlying network. We use the agent-based approach for representing the Braess network. ABMs are very well suited for capturing multiple autonomous decision makers displaying bounded rational behavior. We used Netlogo [58] version 3.1 to build the agent-based representation of the Braess network (Fig. 3). Nodes 1–4 are modeled as Netlogo patches (<sup>fi</sup>xed agents with attributes). Each patch contains information regarding its neighboring nodes and the current <sup>fl</sup>ow on each of the links between itself and its neighboring nodes. Each user is modeled as $\mathsf { a } \ \ " \mathrm { t u r t l e } \ "$ (agents in Netlogo) that have a set of internal state variables such as cost incurred and current position. One such state variable is start-link (referred to as T in the optimization problem formulation) that decides whether a user starts traveling on link a or link b. As mentioned previously, depending on the value of T, $( T / 1 0 0 ^ { * } Q )$ start on link a and $( 1 - T / 1 0 0 ) ^ { \ast } Q$ on link b. The start-link variable is set with a simple mechanism; let's say if $Q = 2 0 ,$ , and $T = 5 0 / 1 0 0$ (50% will travel on link a and 50% on link b), then a counter is initiated that counts till $T ^ { * } Q$ and all agents born into the system have their start-link variable set to link a (after which rest of them have their start-link assigned to b). At each demand generation period all the agents are generated and once the “move” command is issued in parallel to all agents, they wait for a period of time (seconds) governed by $\tt { a } \sim \tt { U }$ [0,3] before selecting a link based on the state of their internal start-link variable. This ensures that for every demand period T% split of the incoming demand occurs and the demand is loaded on to the network in a “random fashion”. The rules followed by each user can be summarized as:

Rule 1: User selects between the links a and b based on the internal state of their start-link variable.

Rule 2: An agent while deciding in a bounded rational way, always considers only the current <sup>fl</sup>ow on the possible link options and selects the link immediately ahead with the least cost.

The agent-based model is then cast within the discrete time simulation formalism [61]. At each simulation time instant a random number of users (generated from the Poisson distribution mentioned earlier) are loaded at Node 1. This represents the demand faced by the system. Each user (after waiting for a time speci<sup>fi</sup>ed by their internal wait variable) starts traveling on a link (a or b) based on the value of the respective start-link variable. Further when these users either reach Node 2 or 3 they select a link that will take them to node 4 (destination node). If a user reaches Node 3 it then proceeds on to Node 4 (only destination). A user who reaches Node 2 makes a selection between links c or e (using the bounded rational logic). Once a user selects a link it then travels on that link for a <sup>fi</sup>xed time (constant parameter in the simulation model). Depending on which links the users take the <sup>fl</sup>ows on the paths are calculated as follows. The <sup>fl</sup>ow on path $p _ { 1 }$ is the <sup>fl</sup>ow on link c. The <sup>fl</sup>ow on path $p _ { 2 }$ is <sup>fl</sup>ow on link b and <sup>fl</sup>ow on path $p _ { 3 }$ is <sup>fl</sup>ow on link e. System cost is then calculated based on Eqs. (1) and (2) and a running average is recorded. Thus the data collected from the agent-based discrete simulation model of the Braess network system is recorded as time series data, which we utilize to calculate an expected value of the system cost. The expected value is then used further in surrogate model estimation and rest of the policy design process.

## 4.2. Model verification

Before proceeding to the stability analysis, response surface estimation and policy optimization stages, it is important to formally verify the ABM representation of the Braess network. We followed the following veri<sup>fi</sup>cation steps:

1. We performed static and dynamic veri<sup>fi</sup>cation and testing as suggested by Fairley [18], and Sargent [49].

1.1. For static testing we used structured walkthroughs through the simulation code while considering a <sup>fi</sup>xed demand scenario.

1.2. For dynamic testing we used mixed traces as suggested by Fairley [18]. We set up simulations with demands of 1 and 2. We then followed the movement of the individual agents (user of the network) and ensured the decision logic is coded correctly.

2. We performed qualitative veri<sup>fi</sup>cation by simulating a traf<sup>fi</sup>c jam on link e. We accomplished this by increasing the travel time for any user on link e (10 times higher than users using link c). Although the links were not capacitated, this resulted in users to remain on that link for a long period of time as compared to link c. Thus after a critical mass was reached on link e any additional user coming at Node 2 found link c to be cheaper than link e and started choosing link c. This step further ensured that the agents were correctly comparing the cost incurred to travel on a link.

3. We performed quantitative veri<sup>fi</sup>cation by testing the model with the benchmark data from Nagurney and Dong [36], i.e., a static demand of 6 was used. The known result (from analyzing the equations) is an equal split between paths $p _ { 1 } , p _ { 2 }$ and $p _ { 3 }$ (<sup>fl</sup>ow of 2 on each path). Without using the <sup>fl</sup>ow control variable T we let the users select links at nodes 1, 2 and 3 based on their bounded rational logic. Equilibrium <sup>fl</sup>ow of 2 users for each path was observed along with the total system cost of 552 (same as [36]).

## 5. Analyzing stability of system response using Largest Lyapunov exponent characterization

For dynamic network systems that have multiple autonomous decision makers and depict evolutionary behavior, stability analysis is an important step. Designing policies for scenarios where the system shows unstable behavior may result in ineffective solutions. Dynamic systems are typically said to exist in three possible states, i.e., stable, marginally stable and unstable (chaotic) [59]. Chaos or instability in dynamic systems is identi<sup>fi</sup>ed by measuring the Largest Lyapunov exponent (LPE) [46]. Lyapunov exponents quantify the exponential divergence of initially close state-space trajectories and estimate the amount of chaos in a system [20,46,47,50]. In this paper we have used the algorithm and software (L1D2) developed by Rosenstein et al [46] to calculate LPE from the time series data (representing system response over time) generated from the agent-based simulations.<sup>2</sup>

## 5.1. LPE calculation for the Braess system using L1D2 software

L1D2 takes time series data from the system as inputs and generates natural log of the divergence between neighboring trajectories in the system at every point of the divergence time. LPE is evaluated by plotting the divergence data versus time to locate the linear “scaling” region on the plot. The Largest Lyapunov exponent, if it exists, is the slope over the scaling region. A positive value of LPE would suggest chaos and instability, a value=0 depicts steady state behavior. A valueb0 would depict a stable system. In case the resultant system behavior is unstable, the response surface should not be estimated at those points and the policy maker has to try other sets of input variables for which the system would show stable behavior. For steady state behavior we have used a tolerance level of ±0.01 for marking when a system should be considered in a chaotic zone. The tolerance level though is heuristically set is based on observations for

![](/api/attachments/BY48U6PG/fulltext/images/27ce7a398b2f13576131a5226a2867bee880a566fd3bd9b020c06c3e5c7a3240.jpg)  
Fig. 4. Latin hypercube sampling based design of experiment for Braess Network problem.

LPE values of known chaotic systems as mentioned in Rosenstein et al. [46].

In order to analyze the stability response of the agent-based model representation of the Braess network we designed 15 experiments with different values of Q and T. The system cost was recorded from each of the 15 experiments. We used a Latin Hypercube Samplingbased design of experiment in order to ef<sup>fi</sup>ciently sample the entire policy design space (we used the lhs function with correlation minimization in Matlab (version 7) to generate the design points as shown in Fig. 4). As mentioned previously Q was generated from a Poisson process with a normally distributed average occurrence rate.

Each experiment was executed on a cluster computing infrastructure available at the Advanced Computing Center for Research and Education (ACCRE) at Vanderbilt University and took 11 h of CPU time. We used an average of the last 100 system cost data points as the expected value of system cost from each of these experiments. Table 1 shows the results from the 15 experiments. LPE analysis was then performed using the L1D2 software as described previously using the time series data on system cost from the 15 experiments. The LPE value came out to be 0 up to two decimal places for each of the 15 experiments, indicating steady state behavior. Steady state behavior in dynamic systems indicates that the system is operating around a <sup>fi</sup>xed point. If the system is perturbed in the future it may display more stable behavior (−ve LPE) or unstable behavior (+ve LPE). Thus, systems in steady state display a weak notion of stability and any policy designed for such systems are effective only within the region of operation de<sup>fi</sup>ned by the input and control parameter space. Thus for the Braess network example, the designed policy can only be termed effective for the demand ranges where the system is stable.

Training data for response surface estimation on expected value of system cost for the Braess Network.

<table><tr><td>Experiment number</td><td>Q</td><td>T</td><td>C</td></tr><tr><td>1</td><td>19</td><td>0.5</td><td>112217.8</td></tr><tr><td>2</td><td>14</td><td>0.83</td><td>26146.76</td></tr><tr><td>3</td><td>18</td><td>0.3</td><td>204055.7</td></tr><tr><td>4</td><td>11</td><td>0.17</td><td>53417.57</td></tr><tr><td>5</td><td>5</td><td>0.7</td><td>974.16</td></tr><tr><td>6</td><td>7</td><td>0.63</td><td>2261.932</td></tr><tr><td>7</td><td>6</td><td>0.03</td><td>13593.98</td></tr><tr><td>8</td><td>13</td><td>0.1</td><td>131630.7</td></tr><tr><td>9</td><td>10</td><td>0.43</td><td>15234.65</td></tr><tr><td>10</td><td>15</td><td>0.57</td><td>36224.46</td></tr><tr><td>11</td><td>9</td><td>0.23</td><td>21852.12</td></tr><tr><td>12</td><td>1</td><td>0.37</td><td>72.583</td></tr><tr><td>13</td><td>2</td><td>0.77</td><td>154.7359</td></tr><tr><td>14</td><td>17</td><td>0.97</td><td>71074.74</td></tr><tr><td>15</td><td>3</td><td>0.9</td><td>457.6457</td></tr></table>

## 6. Surrogate model estimation

The next step in the policy design process is to develop a surrogate representation for the agent-based model in order to evaluate the objective function that could be used by an optimization technique for <sup>fi</sup>nding the exact value for T. There are numerous regression-based surrogate modeling techniques in the literature such as linear regression [16], non-linear regression [51], polynomial chaos models [23] and wavelet based models [41]. Linear, non-linear and polynomial chaos based regression techniques did not work well with the non-linear and transient system responses observed in the Braes network example. Though wavelet based regression methods have been used successfully for surrogate model estimation of systems with non-linear response behavior with transients (stock market time series analysis, [39]), but they are computationally intensive and typically the wavelet basis functions do not have a closed form representation (except the Haar wavelets, which is not suitable for regression), thus making the task of formulating and solving the optimization problems very hard and computationally intensive.

Gaussian process (GP) modeling is a powerful technique based on spatial statistics for interpolating data [43] that can be used to <sup>fi</sup>t virtually any functional form. GP models are increasingly being used as surrogates to expensive computer simulations for the purposes of optimization and uncertainty propagation [32,33]. As a predictor, the GP model is non-parametric, meaning that no explicit functional form is assumed (e.g. linear, quadratic, etc.). In addition, the method can <sup>fi</sup>t data based on multiple input variables, and has been shown to be effective for input dimensions as high as 30. Further, the method gives a direct estimate as to the uncertainty associated with the value of the unknown function at any untested location. This uncertainty estimate is given in terms of a variance (a.k.a. mean squared error), and is a function of the closeness of the new location to the existing data points.

## 6.1. Gaussian process surrogate model for the Braess network

The basic idea of the GP model is to model system response Y as a group of multivariate normal random variables [43,48]. A parametric covariance function is then constructed as a function of the system inputs, x. The covariance function is based on the idea that when the inputs are close together, the correlation between the outputs will be high. As a result, the uncertainty associated with the model's predictions is small for input values which are close to the training points, and large for input values which are not close to the training points. In addition, the mean function of the GP may capture largescale variations, such as a linear or quadratic regression of the inputs.

Training data for response surface estimation on expected average speed in the traf<sup>fi</sup>c grid problem.

<table><tr><td>Experiment number</td><td>Number of cars</td><td>Speed limit</td><td>Ticks per cycle</td><td>Average speed</td></tr><tr><td>1</td><td>140</td><td>0.17</td><td>31</td><td>0.116</td></tr><tr><td>2</td><td>113</td><td>0.30</td><td>11</td><td>0.267</td></tr><tr><td>3</td><td>7</td><td>0.83</td><td>21</td><td>0.43</td></tr><tr><td>4</td><td>127</td><td>0.70</td><td>15</td><td>0.31</td></tr><tr><td>5</td><td>73</td><td>0.90</td><td>17</td><td>0.432</td></tr><tr><td>6</td><td>20</td><td>0.50</td><td>37</td><td>0.301</td></tr><tr><td>7</td><td>47</td><td>0.03</td><td>29</td><td>0.064</td></tr><tr><td>8</td><td>60</td><td>0.77</td><td>23</td><td>0.388</td></tr><tr><td>9</td><td>180</td><td>0.97</td><td>39</td><td>0.034</td></tr><tr><td>10</td><td>153</td><td>0.43</td><td>13</td><td>0.232</td></tr><tr><td>11</td><td>33</td><td>0.57</td><td>27</td><td>0.308</td></tr><tr><td>12</td><td>193</td><td>0.63</td><td>25</td><td>0.194</td></tr><tr><td>13</td><td>167</td><td>0.23</td><td>33</td><td>0.138</td></tr><tr><td>14</td><td>87</td><td>0.37</td><td>35</td><td>0.212</td></tr><tr><td>15</td><td>100</td><td>0.10</td><td>19</td><td>0.111</td></tr></table>

Thus Y can be represented by a Gaussian process with mean β and covariance function de<sup>fi</sup>ned as:

$$
E [ Y (x) ] = \beta\tag{3}
$$

and

$$
C o v [ Y (x), Y (x ^ {*}) ] = \lambda c (x, x ^ {*} | \phi)\tag{4}
$$

where $c ( x , x ^ { * } | \Phi )$ is the correlation between x and x\*, ϕ is the vector of parameters governing the correlation function, and λ is the process variance. Following are the steps for estimating the surrogate representation:

1. Simulate system at m training points to generate system response behavior:

$$
Y = (Y (x _ {1}), \dots , Y (x _ {m})) ^ {T}\tag{5}
$$

In the Braess example $m = 1 5$ training points selected using the Latin Hypercube Sampling-based design process. Y represents system cost C as given by Eq. (1).

2. Construct a joint distribution of Y given by

$$
Y \sim N _ {m} (\beta_ {1}, \lambda R)
$$

whereRisam\*mmatrixof coorrelationsamongstthetrainingpoints:

ð<sup>6</sup>Þ

3. The expected value and variance at any input x are then given by

$$
E [ Y (x) ] = \beta + r ^ {T} (x) R ^ {- 1} (Y - \beta_ {1})\tag{7}
$$

and

$$
\operatorname{Var} [ Y (x) ] = \lambda \left(1 - r ^ {T} R ^ {- 1} r\right)\tag{8}
$$

where r is the vector of correlations between x and each of the training points. x is the vector of Q and T in the Braess problem domain. Please note that T (italicized) in the above Eqs. (7) and (8) refers to transpose of a matrix rather than our design variable T (non-italicized).

Using training data presented in Table 1 and the steps described above, we built a GP model estimate for the Braess network system. The GP model building scheme was developed and implemented in MATLAB [33] and was used for building the surrogate model shown in Fig. 5.

![](/api/attachments/BY48U6PG/fulltext/images/3488e02384a0a0e9ffa23c56133f9cc61b3c6c99488c18ae3ef971ec1310650a.jpg)  
Fig. 5. Plot of response surface using the GP surrogate model for Braess Network system.

## 7. Stochastic optimization of policy variable

As seen in Fig. 5, the surrogate model plot for the Braess network shows how the overall system cost worsens for low values of T and increased demand conditions. In order to determine an exact value for T we suggest a stochastic optimization problem formulation (since demand is stochastic) and solution using golden section search [56]. We decided to use such a simple approach as the visual plot of the response surface clearly shows the region around which we could expect to <sup>fi</sup>nd the optimal value for T. Thus the stochastic optimization problem is to minimize the expected value of the system cost with respect to T, and subject to the stochastic demand (Q) and the GP model. It can be formally stated as:

$$
\begin{array}{l} \underset {T} {\text {Min}} E [ C ] \\ s. t. \\ Q \geq 0 \\ E [ Y (x) ] = \beta + r ^ {T} (x) R ^ {- 1} (Y - \beta_ {1}) \end{array}
$$

where r, R and β are described by Eqs. (3), (6)–(8).

We use MATLAB's fminbnd golden section search algorithm to minimize the expectation of the system cost with respect to the decision variable T. The algorithm minimizes the expected value of the system cost, which is calculated in the manner described by the following MATLAB code. The function expected\_cost accepts T and a list of common random numbers (to aid by elimination of sample-tosample variance in estimation of the objective function) as an argument, and returns the expected system cost. The MATLAB code for this function is:

```matlab
function E=expected_cost(T, common_random_numbers)
    for i=1 to length(common_random_numbers)
    system_costs(i) = cost_function_GP(T, common_random_numbers(i,:));
    random_numbers(i,:));
    i=i+1;
    end
E=sum(system_costs)/i;
```

The expected cost function is optimized with the fminbnd solver routine.

Although golden section search does not guarantee global optima, in this case with the help of the response surface plot we were able to conclude decisively that T=0.73 is indeed the optimal value (Figs. 6).

## 8. Scalability demonstration

In order to address the issue of scalability we have solved a problem involving optimal control of traf<sup>fi</sup>c in a grid network of the type often found in urban central business districts (Fig. 7). Our grid problem involves 25 signalized intersections with identical cycles, in phase with each other, and a cycle speci<sup>fi</sup>ed by the modeler (from here on referred to as ticks per cycle). Such signal timing strategies are also encountered in the central business districts with uniform city blocks (Manhattan, Seattle, Chicago etc). Our grid has 25 nodes, 80 links, and approximately an order of magnitude more agents (ten times as compared to the Braess example).

![](/api/attachments/BY48U6PG/fulltext/images/950c13144322e8f3e66a700ab61a21912b4985caecef7b66e7d26ee0ad152cb1.jpg)

![](/api/attachments/BY48U6PG/fulltext/images/f046d380751c354b4609c162cf0d6c44063eb906acbe07e11a55339e40540f79.jpg)  
Fig. 7. Traf<sup>fi</sup>c grid.

## 8.1. Model building and data collection

We use a streamlined traf<sup>fi</sup>c grid model developed by Wilenski et al. in Netlogo [43]. The model uses software agents (as in the Braess example) for modeling individual users. As an initial condition of the simulation we position the cars randomly over the grid. Once the simulation begins the agents follow three simple rules:

Rule 1: Each time step, the cars attempt to move forward at their current speed. If their current speed is less than the speed limit and there is no car directly in front of them, they accelerate.

Rule 2: If there is a slower car in front of them, they match the speed of the slower car and decelerate.

Rule 3: If there is a red light or a stopped car in front of them, they stop.

The grid is shaped in the form of a torroid. In other words, the cars reappear at the beginning of a street after traversing the entire street. This simulates a constant population over the simulation time period. There can be number of implementations representing different scenarios, such as if new cars entered the grid at random locations and intervals. We chose the scenario where we are investigating a constant demand during a certain period of the day such as rush hour. We treat demand, i.e., the number of cars using the grid, as a random variable. The objective is to improve operating conditions (the expectation of the average speed over the network) by manipulating two variables, the cycle length (represented by ticks per cycle) for the red and green signals and the speed limit (set to 1.0). The expected travel speed over the network is a nonlinear and convex function of the cycle length, number of cars, and speed limit.

![](/api/attachments/BY48U6PG/fulltext/images/f29f799475f9fb5041c821567c41f7b5c307627c3969bff437d7b246cebe4613.jpg)  
Fig. 8. Plot of response surface using the GP surrogate model for traf<sup>fi</sup>c grid.

where the expectation (E) is calculated by Monte-Carlo simulation of the Gaussian Process surrogate model.

This problem was solved with only 15 agent-based simulations (at training points selected using a Latin Hypercube Sampling mechanism) (Table 2). Each agent-based simulation took approximately 40 s to run on a computer with 1 GB RAM with 5000 time steps. As mentioned above the simulation starts with a random placement of cars in the grid and we repeated each training point (inputs) a 1000 times <sup>fi</sup>nally taking the average value of the output (average speed of cars) as the training data (output). Thus it took 40,000 s (∼11 h) for collecting data at each training point.

## 8.2. Stability analysis

We perform a stability analysis and calculate the Largest Lyapunov Exponent for each training point using the Rosenstein algorithm [46] and L1D2 software as mentioned previously in the Braess example and ensured that the training data used for surrogate model building represent stable system states. We found the LPE values to be within the tolerance limit of (±0.01). Hence as in the case of the Braess example, we found the traf<sup>fi</sup>c grid system to exhibit weakly stable behavior (steady state) and the prescribed policy designs would be applicable within the range of the input variables (Number of cars, Speed Limit and Ticks per cycle).

## 8.3. Surrogate estimation and optimization

Next we proceeded to build a GP response surface using the training data and followed it up with extended prediction testing. We compared the GP model and simulation results at points other than the training points and found the surrogate to be highly accurate (within ±3% of the simulation runs). At this point we performed a grid search over the response surface involving 90 trial designs (policy scenarios), with 10,000 samples taken for each trial design to evaluate the average speed per scenario combinations. Recall that, randomness is introduced in the simulation by placing the initial start points of the cars on the grid in a random fashion. Using the surrogate model, this optimization was completed in 204 s. Such an approach would have been impossible to carry out with an expensive agent based simulation (∼1130 years). The optimal policy variable was found by simply taking the MAX of the average speed values obtained. The routine was implemented in MATLAB. The response surface and the MAX value is shown in Fig. 8.

From Fig. 9, optimal policy is to set the ticks per cycle at 20 and the speed limit at 1. An interesting question at this stage is whether the optimal solution is the most stable solution too? In order to address this question, we utilized the GP model technique (as per the process described previously) to build a stability response surface using the Lyapunov values calculated at the training points (and using cubic interpolation to build a response surface in MATLAB, as shown in Fig. 9). Fig. 9 shows that the optimal policy of 20 ticks per cycle and speed limit of 1 is not the most stable con<sup>fi</sup>guration. In fact setting the policy to 44 ticks per cycle and a speed limit between 0.3 and 1 results in the lowest Lyapunov exponent (−ve), indicating stability for the system but at the cost of reduced average speed. Thus approaching the policy design problem from two different angles we get two different answers. One solution yields higher average speed (0.375) but operates in a weekly stable zone (higher variance), while the other solution yields a lower average speed (max 0.21 for a speed limit of 1) but operates in a stable zone (lower variance as compared to the 20 ticks per cycle scenario). Based on our experience with the model we saw that once the zones of operation has been identi<sup>fi</sup>ed <sup>fi</sup>ne grain simulation runs can be used for scenario generations. Thus using this framework, policy designer can make structured and informed decisions based on their priorities.

## 9. Summary and future work

In this paper, we presented a framework to design stable policies for network systems by synthesizing agent-based modeling, stability analysis of dynamic systems, surrogate estimation using GP modeling and optimization under uncertainty (OUU) within an over-arching framework. We illustrated the framework using a popular benchmark problem from the transportation network literature, i.e., using Braess network [6]. Additionally we considered users with bounded rational behavior. We modeled individual users as software agents [21] in Netlogo [58] following two simple rules. The agent-based model (ABM) was implemented as a discrete time simulation, where at every simulation time instant, demand was loaded on to the system. We used Largest Lyapunov exponent (LPE) characterization of the system response behavior to identify the stability/instability/steady state characteristics of the network system for a given set of input and control parameters. Further, the paper demonstrated how a Gaussian process (GP) model [43,48] can be utilized to develop an inexpensive surrogate for the ABM model thus facilitating the optimization of the policy variable using stochastic optimization methods. The paper introduces the construction of stability response surfaces using Lyapunov values at a very limited set of training points and using it for trade-off analysis. The framework is completely agnostic to the underlying modeling methodology as it only assumes the presence of a limited set of training point data. Lastly, the framework presented in this paper is general and suitable for solving not only transportation problems, but also other problems such as supply networks, <sup>fi</sup>nancial networks and combined or super networks.

![](/api/attachments/BY48U6PG/fulltext/images/399f32a1b986ce2d997a033580ba88e3d502f9372a4a00fe929d22939ec5be39.jpg)  
Fig. 9. Plot of stability response surface for the traf<sup>fi</sup>c grid.

While we feel that the framework is a step forward towards addressing the challenges of policy design for networked systems, it has certain limitations. Designing policies for networked systems is effectively an optimal control problem [36]. Optimal control problems come in two varieties, open loop and closed loop. Open loop control systems use predetermined policies. Real-time information about the current state of the network is not used to modify the control. Such open loop strategies are popularly used in transportation network research [53]. In principle open loop control problems can be solved by discretizing control variables over time and using the optimizer to manipulate these vectors. Thus the solutions generated hold true over a range of the input and policy variables (thus the static nature). A more sophisticated approach would be to use closed loop feedback during the optimization process, simultaneously as the system evolves. This framework does not lend itself towards solving closed loop control problems and further research is needed that seems to be beyond the scope of just one paper.

In future research, we will apply the current framework to solve policy design problems in multiple class, multiple mode super networks as suggested by Nagurney et al. [37]. Also system dynamics [22] and cellular automaton [60] modeling can be used in place of ABMs. One of the most important characteristics of realworld network-systems problem is the presence of aleatory uncertainties such as randomness in the demand function, as well as epistemic uncertainties such as imperfect information, at various decision making levels. In this paper we have shown how aleatory uncertainties in the network system can be handled. Future research needs to investigate how epistemic uncertainties at the information level as well at the model level (lack of complete information about the system itself) could be speci<sup>fi</sup>cally considered while designing policies. For example, policy designers may lack knowledge of exact user behavior while users may lack knowledge of the operational state of the system. The agent-based approach could potentially be used to model intelligent and adaptive decision making behavior at the individual user level in order to address the uncertainty arising due to the lack of speci<sup>fi</sup>c knowledge. The exact method of modeling such mechanisms in ABMs and their impacts on network policy design needs to be investigated future research.

## Acknowledgments

We thank the IGERT program and Advanced Computing Center for Research at Vanderbilt University for supporting our research. Additionally we thank John McFarland at the South Western Research Laboratories for help with the Gaussian Process modeling in MATLAB and Dr. Michael T. Rosenstein, Senior Research Scientist at the Department of Computer Science, University of Massachusetts, Amherst for valuable suggestions and help with the Lyapunov exponent computation.

## References

[1] M.C. Agar, S. Salhi, Lagrangean heuristics applied to a variety of large capacitated plant location problems, Journal of the Operational Research Society 49 (1998) 1072–1084.

[2] K.S. Al-Sultan, M.A. Al-Fawzan, A tabu search approach to the uncapacitated facility location problem, Annals of Operations Research 86 (1999) 91–103.

[3] R.G. Aldunate, F. Pena-Mora, G.E. Robinson, Collaborative distributed decision making for large scale disaster relief operations: drawing analogies from robust natural systems, Complexity 11 (2) (2005).

[4] O. Alp, E. Erkut, Z. Drezner, An ef<sup>fi</sup>cient genetic algorithm for the p-median problem, Annals of Operations Research 122 (2003) 21–42.

[5] R. Axelrod, The complexity of cooperation: agent-based models of competition and collaboration, Princeton University Press, 1997.

[6] D. Braess, Uber ein Paradoxon der Verkehrsplanung, Unternehmensforschung 12 (1968) 258–268.

[7] K.M. Carley, Smart agents and organizations of the future, in: L.L.a.S. Livingstone (Ed.), The Handbook of New Media, Sage, Thousand Oaks, CA, 2002.

[8] K.M. Carley, N. Kamneva, A network optimization approach for organizational design, Carnegie Melon Uni\versity, Pittsburgh, 2004.

[9] G.L. Chang, H.S. Mahmassani, Travel time prediction and departure time adjustment behavior dynamics in a congested traf<sup>fi</sup>c system, Transportation Research B 22 (3) (1988) 217–232.

[10] T.Y. Choi, K.J. Dooley, M. Rungtusanatham, Supply networks and complex adaptive systems: control versus emergence, Journal of Operations Management 19 (3) (2001) 351–366.

[11] S. Chopra, P. Meindl, Supply chain management: strategy, planning, operation, 2nd ed.Prentice Hall, 2003.

[12] M.G. Cojocaru, P. Daniele, A. Nagurney, Projected dynamical systems, evolutionary variational inequalities, applications, and a computational procedure, in: A.M.A. Chichuluun, P.M. Pardalos, L. Pitsoulis (Eds.), Pareto Optimality, Game Theory and Equilibria, Springer, Berlin, Germany, 2007.

[13] C.J. Daganzo, J. Laval, J.C. Munoz, Some ideas for freeway congestion mitigation with advanced technologies, Traf<sup>fi</sup>c Engineering Control 43 (10) (2002) 397–403.

[14] M.S. Daskin, Network and discrete location: models, algorithms, and applications, J Wiley and Sons, Inc, New York, 1995.

[15] D.A. DeLaurentis, R.K. Callaway, A system-of systems perspective for future public policy, Review of Policy Research 21 (6) (2004) 829–837.

[16] N.R. Draper, H. Smith, Applied regression analysis, Wiley Series in Probability and Statistics, Wiley, 1998.

[17] H.A. Eiselt, C.L. Sandblom, Decision analysis, location models, and scheduling problems, Springer-Verlag, Berlin, 2004.

[18] R.E. Fairley, Dynamic testing of simulation software, Proceedings of the 1976 Summer Computer Simulation Conference, Washington D.C., 1976.

[19] J. Farley, in: M. Loukides (Ed.), Java Distributed Computing, 1st ed., O'Reilly Media, Sebastopol, CA, 1998.

[20] J.D. Farmer, J.J. Sidorowich, Predicting chaotic time series, Physics Review Letters 59 (1987) 845

[21] J. Ferber, Multi-agent systems: an introduction to distributed arti<sup>fi</sup>cial intelligence, Addison-Wesley, Harlow, England, Don Mills, Ont., 1999

[22] J.W. Forrester, Industrial dynamics, MIT Press, Cambridge, MA, 1961.

[23] R.G. Ghanem, P.D. Spanos, Stochastic <sup>fi</sup>nite elements: a spectral approach, Springer-Verlag, 1991.

[24] G. Guariso, M. Hitz, H. Werthner, An integrated simulation and optimization modeling, environment for decision support, Decision Support Systems 16 (1996) 103–117.

[25] J.N. Hagstrom, R.A. Abrams, Characterizing Braess's paradox for traf<sup>fi</sup>c networks IEEE Intelligent Transportation Systems Conference Proceedings, Oakland (CA) USA, IEEE, 2001.

[26] C.M. Harland, R.C. Lamming, J. Zheng, T.E. Johnsen, A taxonomy of supply networks, Journal of Supply Chain Management 37 (4) (2001) 21–28.

[27] Y.C. Ho, X.R. Cao, Perturbation analysis of discrete event dynamics, Perturbation analysis of discrete event dynamics, 1991

[28] M. Hribar, M.S. Daskin, A dynamic programming heuristic for the p-median problem, European Journal of Operational Research 101 (1997) 499–508.

[29] N. Kang, S. Han, Agent-based e-marketplace system for more fair and ef<sup>fi</sup>cient transaction, Decision Support Systems 34 (2002) 157–165.

[31] B. Lewis, D.J. Berg, Threads primer: a guide to multithreaded programming, Prentice Hall, Upper Saddle River, NJ, 1995.

[32] J.D. Martin, T.W. Simpson, A study on the use of kriging models to approximate deterministic computer models, Proceedings of DETC'03 ASME 2003 Design Engineering Technical Conferences and Computers and Information in Engineering Conference Chicago Illinois USA 2003

[33] J. McFarland, S. Mahadevan, V. Romero, L. Swiler, Calibration and uncertainty analysis for expensive computer simulations with multivariate output, Proceedings of the 9th AIAA Non-Deterministic Approaches Conference, Schaumburg, IL, 2008.

[34] L.W. Miller, N. Katz, A model management system to support policy analysis, Decision Support Systems 2 (1) (1986) 55–63.

[35] P.K.J. Mohapatra, S.K. Sharma, Synthetic design of policy decisions in system dynamics models: a modal control theoretical approach, System Dynamics Review 1 (1)(1985) 63–80

[36] A. Nagurney, J. Dong, Supernetworks: decision-making for the information age, Edward Elgar Publishers Cheltenham, England 2001

[37] A.D. Nagurney, D. Parkes, P. Danniele, The internet, evolutionary variational inequalities, and the time-dependent Braesss paradox, Computational Management Science 4 (2007) 243–281.

[38] J.F. Nash, Equilibrium points in n-person games, Proceedings of National Academy of Science 36 (1950) 48–49.

[39] Z. Pan, X. Wang, A stochastic non-linear regression estimator using wavelets, Computational Economics 11 (1998) 89–102.

[40] S.D. Pathak, D.M. Dilts, G. Biswas, On the evolutionary dynamics of supply network topologies, IEEE Transactions on Engineering Management 54 (4) (2007) 662–672.

[41] D.B. Percival, A.T. Walden, Wavelet methods for time series analysis, Cambridge University Press, Cambridge, 2000.

[42] Q. Qiang, A. Nagurney, A uni<sup>fi</sup>ed network performance measure with importance identi<sup>fi</sup>cation and the ranking of network components, Optimization Letters 2 (1) (2008) 313–426.

[43] C. Rasmussen, Evaluation of Gaussian processes and other methods for non-linear regression, University of Toronto, Toronto, 1996.

[44] C.S. ReVelle, H.A. Eiselt, Location analysis: a synthesis and survey, European Journal of Operational Research 165 (1) (2005) 1–19.

[45] C.W. Reynolds, Flocks, herds, and schools: a distributed behavioral model, in computer graphics, SIGGRAPH '87 Conference Proceedings, 1987.

[46] M.T. Rosenstein, J.J. Collins, C.J.D. Luca, A practical method for calculating largest Lyapunov exponents from small data sets, Physica D 65 (1993) 117–134.

[47] M. Sano, Y. Sawada, Measurement of the Lyapunov spectrum from a chaotic time series, Physics Review Letters 55 (1985).

[48] T.J. Santner, B.J. Williams, W.I. Noltz, The design and analysis of computer experiments, Springer-Verlag, New York, 2003.

[49] R.G. Sargent, Verifying and validating simulation models, Proceedings of 1996 Winter Simulation Conference, 1996.

[50] S. Sato, M. Sano, Y. Sawada, Practical methods of measuring the generalized dimension and the largest Lyapunov exponent in high dimensional chaotic systems, Progress of Theoretical Physics 77 (1987).

[51] G.A.F. Seber, C.J. Wild, Nonlinear regression, John Wiley and Sons, New York, 1989.

[52] C.R. Shalizi, Methods and techniques of complex systems science: an overview, in: T.S. Deisboeck, J.Y. Kresh (Eds.), Complex Systems Science in Biomedicine, Springer, New York, 2006.

[53] Y. Shef<sup>fi</sup>, Urban transportation networks: equilibrium analysis with mathematical programming methods, Prentice-Hall, Englewood Cliffs, New Jersey, 1985.

[54] H.A. Simon, Models of man: social and national, Wiley, New York, 1957.

[55] S.C. Dafermos, F.T. Sparrow, The traf<sup>fi</sup>c assignment problem for a general network, Journal of Research of the National Bureau of Standards 73 (B) (1969) 91–118.

[56] R.J. Stuart, N. Peter, Arti<sup>fi</sup>cial intelligence: a modern approach, 2nd ed.Prentice Hall, Upper Saddle River, N.J., 2003

[57] T. Sueyoshi, G.R. Tadiparthi, An agent-based decision support system for wholesale electricity market, Decision Support Systems 44 (2008) 425–446.

[58] U. Wilensky, NetLogo, Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL, 1999.

[59] G.P. Williams, Chaos theory tamed, vol. xvii, Joseph Henry Press, Washington, D.C., 1997, p. 499.

[61] B.P. Zeigler, H. Praehofer, T.G. Kim, 2nd ed., Theory of modeling and simulation: integrating discrete event and continuous complex dynamic systems, vol. xxi, Academic, San Diego, California, 2000, p. 510.

[60] S. Wolfram, A new kind of science Wolfram Media, , 2002.

![](/api/attachments/BY48U6PG/fulltext/images/fda03a23161462ef8fd9e5dc8513474081907a9726e165783aeeae6dcd4ccad3.jpg)

Dr. Surya Pathak is an Assistant Professor of Operations Management in the Business Program at University of Washington Bothell. He received his PhD in Interdisciplinary Management of Technology from Vanderbilt University in 2005. He is currently conducting research in the area of policy design for large-scale systems, complex adaptive supply networks, decision making under risk and uncertainty, supply network design, and supply relationship management. His methodological orientations include agent-based simulations and cellular automaton models on grid computing infrastructure along with mathematical modeling, robust and reliability-based design optimization, archival data analysis, and game theoretic modeling techniques for investigating policy implications in diverse domains, such as manufacturing and health care supply networks, transportation networks, and super networks. He is a founding member of the Center for Supply Network Science at Arizona State University, at Tempe, Arizona. Dr. Pathak's work has been published or is under consideration in the IEEE Transactions on Engineering Management, Journal of Operations Management, International Journal of Production Research, Decision Support Systems, Journal of Supply Chain Manage ment, Decision Sciences and Transportation Research Records

![](/api/attachments/BY48U6PG/fulltext/images/e438ac0bfc67ac822fb93f68770cdfa7ac057cddd93d725251a0229d180561c2.jpg)

Dr. Mark Philip McDonald is an Assistant Professor of Civil and Environmental Engineering at Vanderbilt University. He has earned the BCE from Auburn University in 2003, the MSCE from the University of California, Berkeley in 2004, and the PhD from Vanderbilt University in 2008. His research interests include optimal design, uncertainty analysis, and decision making under uncertainty for complex systems, particularly systems of systems.

![](/api/attachments/BY48U6PG/fulltext/images/b6f541231ace7e579085737d926c70d8d12f1f6955bb557d1ebec12f68b641e4.jpg)

Dr. Sankaran Mahadevan is Professor of Civil and Environmental Engineering, and Director of Vanderbilt University's NSF-funded multidisciplinary graduate program in Reliabil ity and Risk Engineering and Management. He received his PhD in 1988 fromGeorgia Institute of Technology. His research contributions are in model-based simulation mechanical systems durability, reliability and risk assessment, design optimization and model validation techniques, with applications to civil infrastructure, automotive and aerospace systems. His research has been funded by NSF, NASA, DOD, DOE, FAA, GM, DaimlerChrysler, Union Paci<sup>fi</sup>c, and Oak Ridge, Sandia and Idaho National Laboratories. Hi research is documented in more than 300 publications.
