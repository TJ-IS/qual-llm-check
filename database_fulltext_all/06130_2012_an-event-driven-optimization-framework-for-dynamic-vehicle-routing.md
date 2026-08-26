---
otero_id: 6130
otero_key: "VMKKGCBS"
title: "An event-driven optimization framework for dynamic vehicle routing"
authors: "Victor Pillac; Christelle Guéret; Andrés L. Medaglia"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.06.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An event-driven optimization framework for dynamic vehicle routing

Victor Pillac <sup>a,b</sup>, Christelle Guéret <sup>a</sup>, Andrés L. Medaglia <sup>b,</sup>⁎

<sup>a</sup> LUNAM Université, École des Mines de Nantes, IRCCyN UMR CNRS 6597, Nantes, France

<sup>b</sup> Centro para la Optimización y Probabilidad Aplicada (COPA) & CEIBA, Departamento de Ingenieria Industrial, Universidad de los Andes, Bogotá, Colombia

## a r t i c l e i n f o

Article history: Received 7 July 2011 Received in revised form 24 May 2012 Accepted 14 June 2012 Available online 29 June 2012

MSC: 90-04 90B06 68U35 68W10 90C59

## a b s t r a c t

The real-time operation of a <sup>fl</sup>eet of vehicles introduces challenging optimization problems. In this work, we propose an event-driven framework that anticipates unknown changes arising in the context of dynamic vehicle routing. The framework is intrinsically parallelized to take advantage of modern multi-core and multi-threaded computing architectures. It is also designed to be easily embeddable in decision support systems that cope with a wide range of contexts and side constraints. We illustrate the flexibility of the framework by showing how it can be adapted to tackle the dynamic vehicle routing problem with stochastic demands.

Keywords: Dynamic vehicle routing Event-driven framework Multiple scenario approach Online stochastic optimization VRPSD

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The problem of operating a <sup>fl</sup>eet of vehicles arises in many contexts, from pickup and delivery of goods to relocation of trucks in carrier companies. More speci<sup>fi</sup>cally, Vehicle Routing Problems (VRPs) deal with the design of a set of minimal-cost vehicle routes that serve the demand for goods or services of a group of geographically spread customers, satisfying operational constraints. From an information perspective, such problems generally include two dimensions: evolution and quality of information [40]. Information evolution relates to the fact that in some problems the information available to the planner may change during the execution of the routes, for example with the arrival of new customer requests. Information quality re<sup>fl</sup>ects possible uncertainty on the available data, for instance, when the demand of a customer is only known as a range estimate of its real demand. In addition, depending on the problem and the available technology, vehicle routes can either be designed a-priori or online. Based on these dimensions, Table 1 identi<sup>fi</sup>es four categories of routing problems.

The static and deterministic category includes the classical Vehicle Routing Problem (VRP) as de<sup>fi</sup>ned by Dantzig [15] in which all information is known beforehand and with certainty. In contrast, problems from the static and stochastic class are characterized by input partially known as random variables, which realizations are only revealed during the execution of the routes. Additionally, it is assumed that routes are designed a-priori and only minor changes are allowed afterward. A common example is the VRP with Stochastic Demands (VRPSD), in which customer demands are uncertain. We refer the interested reader to the surveys by Cordeau et al. [12], Baldacci et al. [2], and Laporte [27] for a recent review of these two classes of problems.

In dynamic and deterministic problems, also referred to as online problems, part or all of the input is unknown and revealed dynamically and unpredictably during the design or execution of the routes. On the other hand, dynamic and stochastic problems include partial stochastic knowledge on the dynamically revealed information. For these problems, vehicle routes are rede<sup>fi</sup>ned in an ongoing fashion, requiring technological support for real time communication between the vehicles and the decision maker (e.g., mobile phones and global positioning systems). Techniques for both classes are reviewed in the studies by Ichoua et al. [25] and Pillac et al. [37].

Dynamism in routing can emerge from different aspects of the problem. The most common source of dynamism is the arrival of new customers with a demand for goods or services. Other researchers consider dynamically revealed demands for a set of known customers, dynamic travel times, and vehicle availability.

Taxonomy of vehicle routing problems by information evolution and quality.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Information quality</td></tr><tr><td>Deterministic input</td><td>Stochastic input</td></tr><tr><td rowspan="2">Information evolution</td><td>Input known beforehand</td><td>Static and deterministic</td><td>Static and stochastic</td></tr><tr><td>Input changes over time</td><td>Static and deterministic</td><td>Dynamic and stochastic</td></tr></table>

Fig. 1 illustrates the Dynamic Vehicle Routing Problem (DVRP), in which new customers appear while the vehicle is executing its route. Before the vehicle leaves the depot (at time $t _ { 0 } ) ,$ , an initial route plans to visit the currently known customers (A, B, C, D, E). While the vehicle executes its route, two new customers (X and Y) appear (at time $t _ { 1 } )$ and the initial route is adjusted to accommodate them. Finally (at time t ), the executed route is (A, B, C, D, Y, E, X). This example reveals that dynamic routing requires to adjust the routes in an ongoing fashion, which implies real-time communication between vehicles and the dispatching center.

Until recently, the lack or high cost of real-time communication technologies steered vehicle routing research away from dynamic problems [16]. Nevertheless, recent advances in communication and geolocation technologies now allow companies to economically track their <sup>fl</sup>eet in real time. These new technologies lead to the development of Intelligent Transport Systems (ITS), and more precisely Advanced Fleet Management Systems (AFMS), that combine hardware and software solutions to provide real time information on the <sup>fl</sup>eet, customers, and road networks.

The development of ITS and AFMS creates new challenges and opportunities for operations research. The advent of these systems demands a new class of ef<sup>fi</sup>cient optimization algorithms to handle various dif<sup>fi</sup>cult aspects of <sup>fl</sup>eet management. Nevertheless, Crainic et al. [13] suggest that while the hardware part of ITS has considerably evolved, the corresponding Decision Support Systems (DSSs) and optimization models have not yet reached their maturity.

From a practical perspective, we can identify the following desirable characteristics of a dynamic routing DSS:

• Event-driven. Organizations are expected to react quickly to changes in their environment. Having a DSS which is periodically updated implies longer reaction delays. Thus, a DSS should be driven by the same transactional events that keep the business operating (e.g., customer requests).

• Parallelized. As dynamic routing requires fast decisions, the underlying optimization algorithms should be parallelized, taking advantage of the now ubiquitous parallel (and distributed) computing architectures able to perform several tasks concurrently.

• Flexible. The landscape of vehicle routing problem variants is vast. Thus, a DSS should be easily extensible to account for operational constraints in a continuously evolving environment.

In this paper, we propose an application-oriented optimization framework for dynamic and stochastic vehicle routing that is eventdriven, parallelized and <sup>fl</sup>exible. The rest of this document is organized as follows. Section 2 reviews the literature on dynamic routing optimization techniques and related decision support systems. Section 3 describes the proposed framework, Section 4 illustrates its application to the dynamic VRPSD, and Section 5 presents the corresponding experimental results. Finally, Section 6 concludes this paper and discusses how the framework can be generalized and extended to other dynamic optimization settings.

## 2. Literature review

A growing body of research has been carried out on dynamic routing, leading to new optimization techniques and innovative DSSs. In this section we will review some of the most signi<sup>fi</sup>cant contributions in the dynamic routing <sup>fi</sup>eld.

## 2.1. Dynamic routing

A wide range of techniques have been developed to address the dynamic nature of routing problems. Dynamic methods can be divided in two categories: non-anticipative, which only react to updates in the problem data; and anticipative, which take into account knowledge on the dynamically revealed information to anticipate the future. Non-anticipative methods are designed for dynamic and deterministic problems. They generally are a direct adaptation of static methods such as integer programming [48], large neighborhood search [20], tabu search [4,18,23], genetic algorithms [7,21], or ant colony optimization [33]. Conversely, anticipative methods often make better decisions by using stochastic information available in the form of probability distributions. Anticipative methods are further classi<sup>fi</sup>ed into one of two families: stochastic modeling or sampling.

Anticipative methods based on stochastic modeling accurately describe the problem's stochasticity. In an early work, Powell et al. [38] formulated the DVRP as a Markov Decision Process (MDP). Nevertheless, the exponential growth of the state and action spaces causes traditional MDPs to stall. This problem has led to the development of Approximate Dynamic Programming (ADP). The main idea behind ADP is to decompose the time in decision epochs. At each decision epoch the goal is to minimize the current deterministic cost plus an approximation of the expected future cost. This technique has been successfully applied to different dynamic <sup>fl</sup>eet management problems [19,39,45] and vehicle routing with stochastic demands [35]. The strength of ADP is that it accurately encapsulates stochastic information in the model, but at the expense of a higher complexity and stronger assumptions on the probability distributions.

On the other hand, anticipative methods based on sampling are to some extent simpler, but require more effort to capture the problem's stochasticity. These methods sample the probability distributions to generate scenarios that are used to make decisions. Such approaches include the dynamic sample scenario hedge heuristic proposed by

![](/api/attachments/VMKKGCBS/fulltext/images/847f1ddadea0ba7644b61943edda36fe4142f49d043dbb03edaed04564d31ed8.jpg)  
Fig. 1. Example of dynamic vehicle routing

Hvattum et al. [22], the tabu search heuristics proposed by Ichoua et al. [24] and Attanasio et al. [1], and the Multiple Scenario Approach (MSA) proposed by Van Hentenryck and Bent [47].

Among the anticipative methods based on sampling, MSA is unique in the sense that it provides a more general framework for dynamic problems. More speci<sup>fi</sup>cally, MSA maintains a pool of scenarios with realizations of the problem random variables and a solution to the corresponding deterministic problem. A distinctive feature of MSA is that the next customer to visit is selected based on the whole scenario pool by means of a decision process. The algorithm starts by initializing the scenario pool based on the currently known information. Periodically, MSA updates the scenario pool to re<sup>fl</sup>ect the current environment state, selects the next customer, and optimizes the scenarios. As new information is disclosed, some scenarios might become obsolete and are removed from the pool, leaving space to new ones.

The strength of MSA is that optimization is performed on scenarios and only requires to solve a static and deterministic problem. Therefore this approach is very <sup>fl</sup>exible as it can virtually be adapted to any problem, provided an optimization algorithm for its static and deterministic version. Nonetheless, its integration in a real-world context is far from trivial, especially considering communication between the method and its environment. Additionally, the fact that it relies on time steps induces delays between the arrival of new information and its processing.

## 2.2. Decision support systems for dynamic routing

There exists a wide range of DSSs for the operation of a <sup>fl</sup>eet of vehicles, as surveyed by Zak [49]. In the following paragraphs we will focus on dynamic routing DSS and review the body of research in this area.

The operation of a <sup>fl</sup>eet of vehicles in an urban area is a key component of city logistics [46], and the core subject of various DSSs developments. For instance, Fleischmann et al. [17] presented an event-based DSS that takes into account changing travel times and the arrival of new customers in the context of a local area courier service. The framework continuously optimizes a single routing plan in which new customers are inserted either with an assignment model or insertion algorithms. A similar problem was addressed by Attanasio et al. [1] who showed that the proposed DSS allows for an ef<sup>fi</sup>cient operation (low administrative cost) as the <sup>fl</sup>eet size (number of couriers) increases, a key competitive advantage in this sector. Comparable conclusions were drawn by Petrakis et al. [36] for the dynamic routing and scheduling of <sup>fi</sup>eld technicians. Likewise, Barcelo et al. [3] presented a <sup>fl</sup>exible DSS for vehicle routing and scheduling in city logistics and its application to the delivery of goods in two Italian cities. Their DSS includes a real time traf<sup>fi</sup>c simulator, connection to common GIS systems, and various routing models and optimization modules. Dahl and Derigs [14] studied the effectiveness of a DSS that allows for cooperation between carriers, increasing the utilization of vehicles. In a different context, Zeimpekis et al. [50] developed a DSS that takes into account unexpected events such as traf<sup>fi</sup>c conditions or vehicle breakdowns to re-optimize an existing distribution schedule. Li et al. [28] also studied vehicle breakdowns in an application to waste collection in Brazil.

Dynamic DSSs generally rely on speci<sup>fi</sup>c technology to ensure the communication between vehicles and the dispatching center [50]. In contrast Bieding et al. [9] propose a DSS based on a WAP (Wireless Application Protocol) server and mobile phones to manage the delivery of newspapers. The use of web technologies for DSS is promising, as highlighted by the study of Bhargava et al. [8], especially for dynamic routing, as it allows users to access the DSS with mobile devices such as cell phones or tablet computers.

As pointed out by Crainic et al. [13], there is a gap between state-of-the-art optimization techniques and the optimizers embedded in real-life DSSs. This may be explained by the complexity and level of specialization of certain approaches, that render dif<sup>fi</sup>cult their extension and integration in an application-oriented context. To address this issue, we propose a <sup>fl</sup>exible optimization framework, based on MSA, easily embeddable in any DSS for dynamic routing.

## 3. Proposed framework

The framework, called jMSA, is a <sup>fl</sup>exible, parallel, and event-driven Java implementation of the multiple scenario approach. The proposed framework has been designed to facilitate and accelerate the development and deployment of MSA-based algorithms embeddable in DSSs. This section presents the proposed framework in detail.

## 3.1. Scenarios and decisions

Scenarios capture uncertainty in MSA. Each scenario contains a realization of the random variables, and a solution to the static and deterministic problem de<sup>fi</sup>ned by this realization. For instance, in the Dynamic VRPSD (DVRPSD), in which vehicles can be dynamically rerouted, each scenario contains a realization of the customer demands; while in the DVRP, it contains a set of sampled (potential) customers, aside from the known customers. An optimization algo rithm is used to solve the static and deterministic routing problem de<sup>fi</sup>ned by both actual and sampled data. Virtually, any optimization algorithm can be used to optimize scenarios. Nonetheless, it should be fast enough to be able to optimize the whole scenario pool between two events. Additionally, as the same scenario may be optimized more than once, it should be capable of escaping from local optima to further improve the solution.

Fig. 2 illustrates how scenarios are generated for the DVRP. Solely based on the actual customers, the optimal tour would be (A, B, E, D, C), which ignores two zones (gray areas) where customers are likely to appear. By sampling the customer spatial distributions, customers X, Y and Z are generated, and the new optimal tour is (C, X, Y, B, A, Z, E, D). Removing the sampled customers leads to the tour (C, B, A, E, D) which is sub‐optimal based on a myopic cost evaluation, but leaves room to accommodate new customers at a lower cost.

Another key element in MSA is the decision process, which de<sup>fi</sup>nes how to select the next customer to serve based on the information of the scenario pool. MSA's accuracy relies to a great extent on the decision process, being the most common algorithms expectation, consensus, and regret. The expectation algorithm [10] evaluates the cost of visiting each customer <sup>fi</sup>rst, by forcing its visit and reoptimizing each scenario. The consensus algorithm [6] selects the customer appearing <sup>fi</sup>rst with the highest frequency. Finally, the regret algorithm [5] approximates the cost of visiting each customer <sup>fi</sup>rst.

![](/api/attachments/VMKKGCBS/fulltext/images/d4cd9d5f445f4400912cafdebf39e6cc309fabef4ba944ad233830d04e293b29.jpg)  
Fig. 2. Scenario generation in MSA.

The jMSA framework uni<sup>fi</sup>es these decision processes in the generic Algorithm 1, in which a subset of candidate customers (line 1) is evaluated against the scenario pool (line 5) to select the best one (line 9). The evaluation of each customer re<sup>fl</sup>ects how desirable it is to serve it <sup>fi</sup>rst depending on the objective. In most routing problems, the customer with the highest evaluation should be the one that ensures the lowest expected routing distance when visited <sup>fi</sup>rst.

Algorithm 1. A general algorithm for the decision process in jMSA

```txt
Input: scenario pool P, set of pending customers R
Output: r* the next customer to serve
1: C←selectCandidates(R, P)
2: f*←-∞, r*←∅
3: for all r∈C do
4:    f←0
5:    for all s∈P do
6:    f←f+evaluateRequestProfit(r, s)
7:    end for
8:    if f>f* then
9:    f*←f, r*←r
10:    end if
11: end for
12: return r*
```

## 3.2. Event-driven interaction

The original description of MSA is implicitly based on the discretization of time in intervals. This implies a time lag between an update in the problem data, such as the arrival of a new customer, and the response of the system, corresponding to the time before the next time interval. Consequently, in jMSA we propose a description of MSA from an event-driven perspective, suitable for its integration as a component of a real-world decision support system.

Fig. 3 illustrates a typical sequence of events while routing a single vehicle in a dynamic context. The environment refers to the real-world, the DSS is assumed to be based on the MSA algorithm, and active (idle) times are represented with a continuous (dotted) segment. While the vehicle is parked at the depot, the MSA procedure initializes a scenario pool based on the currently known customers. Once the vehicle is ready (<sup>fi</sup>rst dotted arrow), MSA analyzes the scenario pool and instructs the vehicle to service customer A (<sup>fi</sup>rst double-headed arrow). While the vehicle is traveling toward customer A, MSA generates and reoptimizes the scenario pool. When the vehicle reaches its destination, an event is sent to the system (second dotted arrow) and triggers an update of the scenario pool. The remaining service time is used by MSA to reoptimize the pool until the vehicle is ready to depart. This event (third dotted arrow) triggers the decision procedure, which recommends visiting customer B (second double-headed arrow). At some point in time while the vehicle is traveling to B, an event (last dotted arrow) triggers an update of the scenario pool. Such event could be the arrival of a new customer in the DVRP, or an update in the traf<sup>fi</sup>c information in the case of routing with dynamic travel times.

![](/api/attachments/VMKKGCBS/fulltext/images/71b9343fda3fcae6da2e28e74f94af06ec35bba3b4ecd578fc26c319b80a3eac.jpg)  
Fig. 3. Time line of events for the dynamic routing of a single vehicle

The main advantage of this event-driven interaction between the environment and the system is that it increases the responsiveness of the DSS by feeding real-time information to the system and communicating decisions without delay.

## 3.3. Framework design

As illustrated in Fig. 4, the proposed framework is divided in two layers: a kernel, common to all dynamic combinatorial optimization problems; and a problem layer, with problem-speci<sup>fi</sup>c components.

The central component of the kernel is the MSAProcedure, which contains the logic of the algorithm and instantiates all other components. The MSAProcedure is con<sup>fi</sup>gured via the GlobalParameters that can be set programmatically or via a con<sup>fi</sup>guration <sup>fi</sup>le.

The event-driven behavior is modeled using two elements: events and event handlers. Fig. 5 shows how events drive the framework. The MSA procedure continuously dequeues events from the event queue, and then processes them by using the corresponding event handler in the event handler manager.

Events are designed to increase the framework responsiveness. To ensure that important events are handled <sup>fi</sup>rst, events are prioritized and the event queue is sorted accordingly. Additionally, some events are preemptive, meaning that the handling of a non-preemptive event is always aborted in favor of a preemptive event.

Event handlers de<sup>fi</sup>ne at a very high level what actions are triggered by a given event. By design, these handlers do not contain any problem-speci<sup>fi</sup>c logic which is instead delegated to components. The component manager contains references to all components and acts as an interface between event handlers and problem-speci<sup>fi</sup>c implementations.

Fig. 6 illustrates how event handlers and components interact by means of the ScenarioGeneration event. First, GenerateHandler calls the generateScenario method of the ComponentManager that internally uses the registered ScenarioGenerator. Then it calls the optimizeScenario method, delegated to the instance of ScenarioOptimizer in use, and adds the scenario to the pool. The process repeats until the pool is full, moment when the event handling terminates by raising a ScenarioOptimization event that is further pushed to the event queue.

The framework includes a callback system that provides users with further control over the MSA procedure. Users may implement a callback simply by extending the Callback interface provided in the framework, and registering it in the MSA procedure. User-de<sup>fi</sup>ned callbacks are automatically invoked at speci<sup>fi</sup>c points of the procedure and allow customized uses such as logging to a <sup>fi</sup>le or dynamic parameter tuning.

Tied, yet decoupled to the kernel, the jMSA framework offers a problem-speci<sup>fi</sup>c layer containing components that provide readyto-use functionalities for common dynamic combinatorial optimization problems. Fig. 4 illustrates some components that could be combined for the DVRP. Consensus is an implementation of the consensus algorithm that is common to many dynamic problems solved under MSA; VRPScenario is an implementation of Scenario for routing problems containing a set of routes; VRPScenarioOptimizer is a generic solver for the VRP; and <sup>fi</sup>nally DVRPScenarioGenerator is the only component speci<sup>fi</sup>c to the DVRP that is responsible for the generation of new scenarios.

This two-layer architecture ensures <sup>fl</sup>exibility and extensibility. While kernel elements are de<sup>fi</sup>ned at a high level and are designed to be problem independent, the problem layer provides implementations for speci<sup>fi</sup>c problems. Thus, users only have to de<sup>fi</sup>ne or extend components, in particular for scenario generation and optimization, without worrying how they will be integrated in the MSA procedure.

![](/api/attachments/VMKKGCBS/fulltext/images/00894fdd4cc5cfdd1bc1cbd960a518b3a016e0591c6627a7741e1c99f8dceab1.jpg)  
Fig. 4. Design overview of the jMSA framework.

## 3.4. Parallelization via multi-threading

The ubiquitous presence of multi-core processors can be exploited in parallelizable algorithms such as MSA. Nevertheless, parallelization often comes at the price of a higher implementation complexity. The jMSA framework offers multi-threaded parallelization of the most time-consuming tasks, hiding it from the user. That is, under jMSA, users do not have to explicitly write a parallel algorithm, but simply rely on the ComponentManager which internally distributes tasks among different threads.

Fig. 7 illustrates how threads interact within the jMSA framework. At time $t _ { 0 }$ the MSA thread dequeues an OptimizePool event, and processes it with the corresponding OptimizeHandler. In parallel to the MSA thread, two other threads are started by the ComponentManager to optimize the scenarios of the pool. At $t _ { 1 } , \mathsf { a }$ preemptive NewCustomer and a Decision event are pushed by the environment, causing the MSA thread to prematurely abort the optimization. To avoid inconsistencies, the main thread waits for the pool executor to terminate, sends a signal to the callback thread to notify that the OptimizePool event was handled, and raises a GenerateScenarios event. Finally, the procedure dequeues the NewCustomer event, which has a higher priority than the Decision event, and processes it.

It is worth noting that aside from time-consuming tasks such as scenario generation and optimization, parallelization is also used to execute callbacks. Callbacks can be particularly useful when writing <sup>fi</sup>les or updating the state of a user interface as it does not affect the performance of the main algorithm. This behavior can be overridden using synchronous callbacks.

## 4. Application to the dynamic VRP with stochastic demands

This section illustrates the <sup>fl</sup>exibility of the jMSA framework on the Dynamic VRP with Stochastic Demands (DVRPSD), and we illustrate how under the proposed approach we can easily relax the assumptions on the demand distributions required by state-of-the-art approaches, thus leading us to the solution of a more general problem with jMSA.

![](/api/attachments/VMKKGCBS/fulltext/images/67d0c3ec9892816a3028f8706becad35373bc532700312dc0d40c4e80e38d043.jpg)  
Fig. 5. Event-driven MSA framework

![](/api/attachments/VMKKGCBS/fulltext/images/14e72624ea83f89daec36ad38e23cc506e5d4f15eed2551904d847de5efa17a6.jpg)  
Fig. 6. Interaction between the GenerateHandler and the different components.

## 4.1. Problem description

The fundamental difference between the classic VRP and the VRP with Stochastic Demands (VRPSD) is that in the latter customer demands are known as random variables. The randomness in the VRPSD implies that a customer demand realization might exceed the vehicle remaining capacity, leading to a route failure that requires a recourse action. An intuitive recourse action is for the vehicle to go back to the depot to restore its initial capacity and then resume its route [29], or to allow the service of additional customers before returning to the depot [34]. It is important to stress that in this context all customers are known beforehand and the only dynamically revealed information is the realization of the customer demands.

Uncertainty in the VRPSD has been addressed by various solution approaches, of which the two most studied are the Chance Constrained Programming (CCP) and the Stochastic Programming with Recourse (SPR). Both methods are based on a two-stage approach: the <sup>fi</sup>rst phase builds a robust routing plan; while the second phase takes recourse (corrective) actions as the realizations of the customer demands are unveiled. The conceptual difference between the two approaches lies in the objective of the <sup>fi</sup>rst-stage optimization: in CCP, the goal is to ensure an upper bound on the probability of a failure, regardless of the expected cost of the second phase; while SPR seeks the minimization of the total expected cost, including recourse actions.

The Dynamic VRPSD (DVRPSD) is an extension of the VRPSD in which it is possible to freely reroute vehicles upon new demand realizations, allowing more complex recourse actions. Literature on the DVRPSD is scarce, with the main contributions being the work by Novoa [34], Novoa and Storer [35], Secomandi [43], and Secomandi and Margot [44]. The only publicly available instances for the DVRPSD are those from Novoa [34], therefore we will use the same problem de<sup>fi</sup>nition de<sup>fi</sup>ned therein to allow a fair comparison between algorithms. In our work, as in all studies on the DVRPSD, we consider the single-vehicle case with discrete and uniformly distributed demand distributions. If at some point the realization <sup>^</sup>ξ of the demand of a customer exceeds the vehicle remaining capacity Q<sup>-</sup> , the vehicle serves the quantity Q<sup>-</sup> , and returns to the depot to restore its capacity. Afterward, a subsequent visit to the customer is planned to serve the remaining demand $\hat { \xi } - \bar { Q }$

![](/api/attachments/VMKKGCBS/fulltext/images/7a0f4cc852ae9054a52bcc04bf7c33a0e8e697287d661626dd4bd3165310242a.jpg)  
Fig. 7. Multiple threads interacting in jMSA.

## 4.2. Scenarios and decisions

In the context of the DVRPSD, scenarios contain different realizations of the customer demands, along with a feasible routing for these values. Given that the vehicle can go back to the depot during its service, a scenario can contain different routes that will be executed in a sequential order by the same vehicle.

The fact that customer locations are identical across scenarios suggests that different scenarios might have similar routes. Therefore, we use the consensus algorithm to select the next customer to visit. Let us consider the scenario pool of Fig. 8. The customers who have already been served (4 and 1) appear <sup>fi</sup>rst in all scenarios, while customers 2, 3, 5, and 6, appear in varying order depending on the scenario sampled demands. Considering that customer 2 appears <sup>fi</sup>rst in 2 out of 4 scenarios, by consensus it is selected as the next customer to visit. With the notations from Algorithm 1, the function selectCandidates (line 1) returns the set of unserved customers while evaluateRequestProfit (line 6) returns 1 if customer r appears <sup>fi</sup>rst in the scenario; 0, otherwise. It is worth noting that the consensus decision might recommend the vehicle to return to the depot for a preventive replenishment, that ${ \mathrm { i } } s ,$ before the vehicle runs out of capacity.

## 4.3. Optimization

To optimize scenarios we use an Adaptive Variable Neighborhood Search (AVNS), which is an extension of the Variable Neighborhood Search (VNS) [32]. The main difference between AVNS and VNS is that neighborhoods are not explored sequentially, but randomly selected with a bias depending on their previous performance. Our implementation uses an average ratio of the improvement to time as a metric of neighborhood performance, and maintains this information between calls to the optimization procedure. Neighborhoods with a better performance are more likely to be explored <sup>fi</sup>rst, leading to a self-tuning algorithm. Our MSA scheme bene<sup>fi</sup>ts from this automatic self-tuning behavior as the optimization procedure is called numerous times on similar instances (i.e., scenarios).

Algorithm 2 presents an outline of the AVNS algorithm. The algorithm initializes with the whole set of neighborhood structures (line 2), then it selects a neighborhood (line 4) to randomly perturb the current solution (line 5), and improves it by applying a local search procedure (line 6). If the new solution is improving (line 8) then it becomes the current solution (line 9), and the set of active neighborhood structures is reset (line 1). Otherwise, the current neighborhood is removed from the set of active neighborhoods (line 12). At each iteration, the performance of the current neighborhood is updated (line 7). This process iterates until all neighborhoods have been explored with no improvement.

![](/api/attachments/VMKKGCBS/fulltext/images/b82163c9db006762edf7a61e73e044acb790230c6edeaba76d520afb768d8762.jpg)  
Fig. 8. Example of the decision process by consensus in a 4-scenario pool. Each scenario contains customers who have been visited (in white) and customers yet to be visited (in gray).

Algorithm 2. The Adaptive Variable Neighborhood Search algorithm

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: feasible solution x, evaluation function z, and set of neighborhood structures  $N = \{N_{1}, ..., N_{K}\}$ 

Output: best solution found  $x^{**}$ 

1:  $x^{**} \leftarrow x$ 

2:  $N_{c} \leftarrow N$ 

3: while  $N_{c} \neq \emptyset$  do

4:  $N \leftarrow \text{selectNeighborhood}(N_{c})$ 

5:  $x' \leftarrow \text{shake}(N, x)$ 

6:  $x' \leftarrow \text{localSearch}(x')$ 

7: updatePerformance( $N, x, x'$ )

8: if  $z(x') &lt; z(x)$  then

9:  $x \leftarrow x'$ 

10:  $N_{c} \leftarrow N$ 

11: else

12:  $N_{c} \leftarrow N_{c} \setminus \{N\}$ 

13: end if

14: if  $z(x') &lt; z(x^{*})$  then

15:  $x^{*} \leftarrow x'$ 

16: end if

17: end while

18: return  $x^{**}$
</div>

In our experiments we used the two neighborhoods structures Or-opt and string-exchange for the perturbation, and a Variable Neighborhood Descent (VND) based on swap and 2-opt as local search. A more detailed description of these neighborhoods can be found in the paper by Irnich et al. [26]. The initial solution is obtained by a Clarke and Wright (CW) heuristic [11] in which the saving list is randomized, as presented in Mendoza et al. [30], leading to the CW+AVNS algorithm.

## 4.4. Failure handling

A route fails when a customer demand exceeds the vehicle's remaining capacity. Thus, the MSA procedure becomes aware of a route failure as soon as a Resource event is raised upon the arrival at the customer location. As a consequence, the route failure handling must be de<sup>fi</sup>ned at the event handler level, by checking if the demand of the current customer is larger than the vehicle remaining capacity, and updating the scenario pool accordingly.

## 4.5. User interface

To illustrate the use of callbacks we developed a user interface shown in Fig. 9. The main panel (right) presents in real time the unserved (white) and served (dark gray) customers, the vehicle desti nation (light gray), and the executed route (arrows). The left panel displays a log of events of jMSA and echoes the con<sup>fi</sup>guration settings. By means of a callback registered in the MSA procedure, all the information in the interface is updated in real time.

## 5. Computational experiments on the DVRPSD

The benchmark instances for the DVRPSD used in this work were initially proposed by Novoa [34] and later used in Novoa and Storer [35]. In this work we consider the larger problems with 30, 40, and 60 customers uniformly distributed in a 1×1 square grid with discrete uniform demands. For each problem size, there are ten combinations of <sup>fi</sup>ve different client locations and demand distributions by two vehicle capacities, leading to a complete testbed of 30 instances. Optimal values where obtained using the COIN-OR Symphony VRP solver [41,42].

![](/api/attachments/VMKKGCBS/fulltext/images/a197404d1d479b86ce87d20228c4f296ffdc04a2f9cbccb0be63ce7ea9d65694.jpg)  
Fig. 9. A graphical user interface for jMSA.

To assess the optimization component in isolation, we conducted an experiment on 100 different demand realizations for all 30 instances. Fig. 10 presents the distribution of gaps to optimal values for CW+AVNS and a CW+2-opt heuristic used for comparison. Note that CW+AVNS clearly dominates CW+2-opt, with 90% of all instances solved with a gap of less than 4%. Additionally, CW+AVNS runs relatively fast, with average CPU times between 50 ms and 650 ms for the larger instances.

To facilitate the comparison between approaches for the DVRPSD, we report the results in terms of value of information [31]. The value of information for instance I, namely I , is the gap between the cost of <sup>Vð Þ</sup>the <sup>fi</sup>nal solution returned by the algorithm z(I) and the a-posteriori optimal solution ${ z ^ { * } } ( I )$ , and it is calculated as follows:

$$
\mathcal {V} (I) = \frac {z (I) - z ^ {*} (I)}{z ^ {*} (I)}.\tag{1}
$$

![](/api/attachments/VMKKGCBS/fulltext/images/af62734c523f1b2a5ef04c20d8a044def090a3d6bee5f93d1b87544fe7fdf2e3.jpg)  
Fig. 10. Optimal gap distribution of the CW+AVNS algorithm vs. CW+2-opt for all Novoa [34] instances.

As in Novoa and Storer [35], we ran 100 simulations with different demand realizations for each instance, using the jMSA framework as a black box. This means that an external simulator was used to send events to the MSA procedure simulating the vehicle route execution. The results reported by Novoa and Storer [35] being aggregated, we report the average value of information by using average solution values in Eq. (1).

Table 2 presents the results for the 30 benchmark instances, each column representing 500 runs (100 runs for each of the 5 instances with the same size and capacity). MSA dominates the algorithm proposed by Secomandi [43] (1s\_n2\_r), and outperforms the best performing algorithms reported by Novoa and Storer [35] (1s\_stostat\_r, 2s\_stostat\_r) for instances with 30 and 60 customers, and a vehicle capacity of 137 and 175. Additionally, MSA shows better overall results with an average gap of 3.3% against 4.8% for 2s\_stostat\_r, 5.8% for 1s\_stostat, and 13.6% for 1s\_n2\_r. Aside from the performance in terms of value of information, it is important to stress that MSA runs continuously, and the next customer to visit is selected in a fraction of a second, while the other algorithms can take up to several minutes to make such decision, limiting their deployment and applicability in a real-world online DSS.

Aside from direct numerical comparison, the strength of our approach relies on the lack of strong assumptions on demand distributions. To illustrate this point, we adapted the testbed instances by changing the demand distribution from a discrete uniform distribution to a left-truncated normal distribution $\left( \mathcal { N } _ { L T \geq 0 } \right)$ as follows

$$
\mathcal {U} _ {i n t} (a, b) \rightarrow \mathcal {N} _ {L T \geq 0} \left(\frac {a + b}{2}, \frac {b - a + 2}{6}\right).\tag{2}
$$

Note that Eq. (2) ensures that the demand will be between a−1 and $b + 1$ with probability 0.997, and truncates negative values.

Table 3 highlights the robustness of MSA which shows consistent performance when demand distributions are changed from uniform (discrete) to normal (continuous). Furthermore, the results are as expected slightly better, with a reduction of 0.3% in the overall average value of information, which is due to the smaller variance. It is important to stress that to conduct this experiment in jMSA the only change required was to use a different random number generator, which illustrates the <sup>fl</sup>exibility of our approach. Other approaches based on stochastic modeling [34,35,43] are not as <sup>fl</sup>exible and depend on distributional assumptions, thus limiting their application scope.

Table 2  
Comparison of average value of information. Values in bold indicate the best performing algorithm for a subset of instances

<table><tr><td rowspan="2">Algorithm</td><td colspan="7">Instance set (size, capacity)</td></tr><tr><td>(30, 137)</td><td>(30, 87)</td><td>(40, 183)</td><td>(40, 116)</td><td>(60, 274)</td><td>(60, 175)</td><td>Average</td></tr><tr><td>1s_n2_r [43]</td><td>12.3%</td><td>11.8%</td><td>11.1%</td><td>12.9%</td><td>13.9%</td><td>19.6%</td><td>13.6%</td></tr><tr><td>1s_stostat_r [35]</td><td>4.7%</td><td>5.1%</td><td>3.7%</td><td>5.3%</td><td>3.5%</td><td>12.3%</td><td>5.8%</td></tr><tr><td>2s_stostat_r [35]</td><td>3.5%</td><td>3.6%</td><td>3.0%</td><td>5.4%</td><td>2.8%</td><td>10.7%</td><td>4.8%</td></tr><tr><td>jMSA</td><td>0.9%</td><td>4.1%</td><td>3.5%</td><td>6.3%</td><td>2.9%</td><td>2.0%</td><td>3.3%</td></tr></table>

Table 3  
Comparison of average VI for discrete uniform and normal distributions.

<table><tr><td rowspan="2">Algorithm</td><td colspan="7">Instance set (size, capacity)</td></tr><tr><td>(30,137)</td><td>(30,87)</td><td>(40,183)</td><td>(40,116)</td><td>(60,274)</td><td>(60,175)</td><td>Average</td></tr><tr><td>Uniform</td><td>0.9%</td><td>3.9%</td><td>3.5%</td><td>6.3%</td><td>2.9%</td><td>2.0%</td><td>3.3%</td></tr><tr><td>Normal</td><td>0.7%</td><td>3.6%</td><td>3.4%</td><td>6.2%</td><td>2.2%</td><td>1.9%</td><td>3.0%</td></tr></table>

## 6. Conclusions

In this paper we presented the design and implementation of jMSA, an object-oriented event-driven framework for the Multiple Scenario Approach (MSA). By doing a high-level abstraction of MSA to a problem independent level, we modeled it as an event-driven process that allows high reactivity to changes occurring in online and highly dynamic operational environments. We implemented jMSA as a <sup>fl</sup>exible framework that is easily embeddable in decision support systems. By design, jMSA includes a callback system that gives the user further control over MSA and allows complex interactions with third party components. Additionally, we integrated into the framework the parallelization of time consuming tasks with no compromise for the framework user, which is a key aspect considering the wide availability of multi-core personal computers.

We illustrated the use of jMSA on the Dynamic VRP with Stochastic Demands (DVRPSD). The optimization of scenarios is performed by an Adaptive Variable Neighborhood Search (AVNS) which improves an initial solution generated with a randomized Clarke and Wright heuristic. The strength of AVNS is that it automatically adjusts its search scheme depending on the problem's structure by keeping track of the neighborhood performance throughout the execution of the MSA procedure. Computational experiments show that our approach is competitive with state-of-the-art algorithms that take full advantage of the stochastic aspects, while it provides a more <sup>fl</sup>exible scheme that can be used to tackle problems with different demand distributions.

## Acknowledgments

Financial support for this work was provided by the CPER (Contrat de Projet Etat Region) Vallée du Libre, and the Centro de Estudios Interdisciplinarios Básicos y Aplicados en Complejidad (CeiBA, Colombia). This support is gratefully acknowledged. The authors would also like to thank Olivier Péton from the École des Mines de Nantes for his insightful comments. Finally, the constructive comments of the Editor-in-Chief, Dr. Andrew B. Whinston, and the review process of DSS led us to an improved paper.

## References

[1] A. Attanasio, J. Bregman, G. Ghiani, E. Manni, Real-time <sup>fl</sup>eet management at Ecourier Ltd, In: V. Zeimpekis, C.D. Tarantilis, G.M. Giaglis, I. Minis (Eds.), Dynamic Fleet Management, vol. 38, Springer, US, 2007, pp. 219–238.

[2] R. Baldacci, P. Toth, D. Vigo, Recent advances in vehicle routing exact algorithms, 4OR: A Quarterly Journal of Operations Research 5 (2007) 269–298.

[3] J. Barcelo, H. Grzybowska, S. Pardo, Vehicle routing and scheduling models, simulation and city logistics, In: V. Zeimpekis, C.D. Tarantilis, G.M. Giaglis, I. Minis (Eds.), Dynamic Fleet Management, vol. 38, Springer, US, 2007, pp. 163–195.

[4] A. Beaudry, G. Laporte, T. Melo, S. Nickel, Dynamic transportation of patients in hospitals, OR Spectrum 32 (2010) 77–107.

[5] R.W. Bent, P. Van Hentenryck, Regrets only! online stochastic optimization under time constraints, In: Proceedings of the 19th National Conference on Arti<sup>fi</sup>cial In telligence (AAAI-04), AAAI Press, 2004, pp. 501–506

[6] R.W. Bent, P. Van Hentenryck, Scenario-based planning for partially dynamic vehicle routing with stochastic customers, Operations Research 52 (2004) 977–987.

[7] I. Benyahia, J.Y. Potvin, Decision support for vehicle dispatching using genetic programming, IEEE Transactions on Systems Man and Cybernetics Part A – Systems and Humans 28 (1998) 306–314.

[8] H.K. Bhargava, D.J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems 43 (2007) 1083–1095

[9] T. Bieding, S. G¨ortz, A. Klose, On line routing per mobile phone : A case on subse quent deliveries of newspapers, In: J.A. Nunen, M.G. Speranza, L. Bertazzi (Eds.), Innovations in Distribution Logistics, vol. 619, Springer, Berlin Heidelberg, 2009, pp. 29–51.

[10] H. Chang, R. Givan, E. Chong, On-line scheduling via sampling, In: Proceedings of the Arti<sup>fi</sup>cial Intelligence Planning and Scheduling (AIPS), 2000, pp. 62–71.

[11] G. Clarke, J.W. Wright, Scheduling of vehicles from a central depot to a number of delivery points, Operations Research 12 (1964) 568–581.

[12] J.F. Cordeau, G. Laporte, M.W. Savelsbergh, D. Vigo, Vehicle routing, In: C. Barnhart G. Laporte (Eds.) Transportation yol 14 Elsevier 2007 pp. 367-428

[13] T.G. Crainic, M. Gendreau, J.Y. Potvin, Intelligent freight-transportation systems: Assessment and the contribution of operations research, Transportation Research Part C: Emerging Technologies 17 (2009) 541–557.

[14] S. Dahl, U. Derigs, Cooperative planning in express carrier networks an empirical study on the effectiveness of a real-time decision support system, Decision Support Systems 51 (2011) 620–626.

[15] G. Dantzig, J. Ramser, The truck dispatching problem, Management Science 6 (1959) 80–91.

[16] B. Eksioglu, A.V. Vural, A. Reisman, The vehicle routing problem: A taxonomic review, Computers and Industrial Engineering 57 (2009) 1472–1483.

[17] B. Fleischmann, S. Gnutzmann, E. Sandvoss, Dynamic vehicle routing based on online traf<sup>fi</sup>c information, Transportation Science 38 (2004) 420–433.

[18] M. Gendreau, F. Guertin, J.Y. Potvin, E. Taillard, Parallel tabu search for real-time vehicle routing and dispatching, Transportation Science 33 (1999) 381–390.

[19] G. Godfrey, W.B. Powell, An adaptive dynamic programming algorithm for dynamic <sup>fl</sup>eet management, I: Single period travel times, Transportation Science 36 (2002) 21–39.

[20] A. Goel, V. Gruhn, A general vehicle routing problem, European Journal of Operational Research 191 (2008) 650–660.

[21] A. Haghani, S. Jung, A dynamic vehicle routing problem with time-dependent travel times, Computers and Operations Research 32 (2005) 2959–2986.

[22] L.M. Hvattum, A. Lokketangen, G. Laporte, Solving a dynamic and stochastic vehicle routing problem with a sample scenario hedging heuristic, Transportation Sci ence 40 (2006) 421–438.

[23] S. Ichoua, M. Gendreau, J.Y. Potvin, Vehicle dispatching with time-dependent travel times, European Journal of Operational Research 144 (2003) 379–396.

[24] S. Ichoua, M. Gendreau, J.Y. Potvin, Exploiting knowledge about future demands for real-time vehicle dispatching, Transportation Science 40 (2006) 211–225.

[25] S. Ichoua, M. Gendreau, J.Y. Potvin, Planned route optimization for real-time vehicle routing, In: V. Zeimpekis, C.D. Tarantilis, G.M. Giaglis, I. Minis (Eds.), Dynamic Fleet Management, vol. 38, Springer, US, 2007, pp. 1–18

[26] S. Irnich, B. Funke, T. Gru¨ nert, Sequential search and its application to vehicle-routing problems, Computers and Operations Research 33 (2006) 2405–2429.

[27] G. Laporte, Fifty years of vehicle routing, Transportation Science 43 (2009) 408–416.

[28] I.O. Li. D. Borenstein. P.B. Mirchandani. A decision support system for the single-depot vehicle rescheduling problem, Computers and Operations Research 34 (2007) 1008–1032.

[29] J.E. Mendoza, B. Castanier, C. Guéret, A.L. Medaglia, N. Velasco, A memetic algorithm for the multi-compartment vehicle routing problem with stochastic demands, Computers and Operations Research 37 (2010) 1886–1898.

[30] J.E. Mendoza, A.L. Medaglia, N. Velasco, An evolutionary-based decision support system for vehicle routing: The case of a public utility, Decision Support Systems 46 (2009) 730–742.

[31] S. Mitrovi´c-Mini´c, G. Laporte, Waiting strategies for the dynamic pickup and delivery problem with time windows, Transportation Research Part B: Methodological 38 (2004) 635–655.

[32] N. Mladenovic, P. Hansen, Variable neighborhood search, Computers and Operations Research 24 (1997) 1097–1100.

[33] R. Montemanni, L.M. Gambardella, A.E. Rizzoli, A.V. Donati, Ant colony system for a dynamic vehicle routing problem, Journal of Combinatorial Optimization 10 (2005) 327–343.

[34] C. Novoa, R. Storer, An approximate dynamic programming approach for the vehicle routing problem with stochastic demands, European Journal of Operational Research 196 (2009) 509–515.

[35] C.M. Novoa, Static and dynamic approaches for solving the vehicle routing problem with stochastic demands, Ph.D. thesis, Lehigh University, 2005.

[36] I. Petrakis, C. Hass, M. Bichler, On the impact of real-time information on <sup>fi</sup>eld service scheduling, Decision Support Systems 53 (2012) 282–293.

[37] V. Pillac, M. Gendreau, C. Guéret, A.L. Medaglia, A review of dynamic vehicle routing problems, In: Technical Report 2011-62, CIRRELT, 2011.

[38] W.B. Powell, A comparative review of alternative algorithms for the dynamic vehicle allocation problem, In: B. Golden, A. Assad (Eds.), Vehicle Routing: Methods and Studies, 1988, pp. 249–291.

[39] W.B. Powell, H. Topaloglu, Fleet management, In: S.W. Wallace, W. Ziemba (Eds.), Applications of Stochastic Programming, vol. 5, SIAM, 2005, pp. 185–215.

[40] H. Psaraftis, A dynamic-programming solution to the single vehicle many-to-many immediate request dial-a-ride problem, Transportation Science 14 (1980) 130–154. [41] T. Ralphs, Symphony user manual, 2006.

[42] T. Ralphs, L. Kopman, W. Pulleyblank, L. Trotter, On the capacitated vehicle routing problem, Mathematical Programming 94 (2003) 343–359.

[43] N. Secomandi, A rollout policy for the vehicle routing problem with stochastic demands, Operations Research 49 (2001) 796–802

[44] N. Secomandi, F. Margot, Reoptimization approaches for the vehicle-routing problem with stochastic demands, Operations Research 57 (2009) 214–230.

[45] H. Simao, J. Day, A. George, T. Gifford, J. Nienow, W.B. Powell, An approximate dynamic programming algorithm for large-scale <sup>fl</sup>eet management: A case applica tion, Transportation Science 43 (2009) 178–197.

[46] In: E. Taniguchi, R. Thompson, T. Yamada, J. van Duin (Eds.), City Logistics: Network Modelling and Intelligent Transport Systems, Pergamon, 2001.

[47] P. Van Hentenryck, R. Bent, Online stochastic combinatorial optimization, MIT Press, 2006.

[48] J. Yang, P. Jaillet, H. Mahmassani, Real-time multivehicle truckload pickup and delivery problems, Transportation Science 38 (2004) 135–148.

[49] J. Zak, Decision support systems in transportation, In: J. Kacprzyk, L.C. Jain, L.C. Jain, C.P. Lim (Eds.), Handbook on Decision Making, vol. 4, Springer, Berlin Heidelberg, 2010, pp. 249–294.

[50] V. Zeimpekis, I. Minis, K. Mamassis, G.M. Giaglis, Dynamic management of a delayed delivery vehicle in a city logistics environment, In: V. Zeimpekis, C.D. Tarantilis, G.M. Giaglis, I. Minis (Eds.), Dynamic Fleet Management, vol. 38, Springer, US, 2007, pp. 197–217.

Victor Pillac holds a M.Sc. (2009) in Software Engineering for Decision Support from the École des Mines de Nantes (France). Since 2009, he is a joint Ph.D. student in the Industrial Engineering Department at Universidad de Los Andes (Colombia) and École des Mines de Nantes (France). He worked as software engineer intern at Planora, a Canadian company developing a decision support system for planning human resources. He also worked at Constraint Technologies International (Australia), where he designed and developed a decision support system for the optimization of long term manpower planning. His research interests include manpower planning, vehicle routing, and software development.

Christelle Guéret is an Associate Professor of Operations Research at the École des Mines de Nantes (France) and member of the research laboratory IRCCyN (Nantes, France). She received her Ph.D. in Systems Control from the Université de Technologie de Compiègne (France) in 1997. Her research interests focus on the optimization of logistic and production systems, in particular, on scheduling and vehicle routing problems. Her research has been published in INFORMS Journal on Computing, Transportation Science, Computers & Operations Research, Annals of Operations Research, European Journal of Operational Research, and the Journal of the Operational Research Society. She has been vice-president of the French Operations Research Society (ROADEF) from 2008 to 2011.

Andrés L. Medaglia is an Associate Professor of Industrial Engineering at Universidad de los Andes (Bogotá, Colombia) and director of the research center Centro para la Optimización y Probabilidad Aplicada (COPA). He holds a Ph.D. (2001) in Operations Research from North Carolina State University (USA). Since 1999 and until the completion of his postdoctoral fellowship, he worked as an optimization specialist developing Web-based decision support systems for the Supply Chain Center at SAS Institute Inc. His current research interests include the development and application of optimization techniques to logistics, project selection, and engineering design. His research has been published in Annals of Operations Research, Automation in Construction, Building and Environment, Computers & Operations Research, Computers & Structures, Decision Support Systems, Engineering Applications of Arti<sup>fi</sup>cial Intelligence, European Journal of Operational Research, Fuzzy Sets and Systems, Interfaces, Journal of Heuristics, Operations Research Letters, Socio-Economic Planning Sciences, The Engineering Economist, and Transportation Science, among others. He has served as Secretary and Vice‐president of the Latin-Ibero American Association of Operations Research (ALIO); and as Vicepresident of Central/South America for the Institute of Industrial Engineers (IIE). He currently serves the editorial board of the Journal of Industrial and Management Optimization.
