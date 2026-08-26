---
otero_id: 15410
otero_key: "JYYAD9GF"
title: "Queuing network model of uniformly distributed arrivals in a distributed supply chain using subcontracting"
authors: "Vidhyacharan Bhaskar; Patrick Lallement"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2010.11.029"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Queuing network model of uniformly distributed arrivals in a distributed supply chain using subcontracting

Vidhyacharan Bhaskar <sup>a,</sup>⁎, Patrick Lallement <sup>b</sup>

<sup>a</sup> Department of Electronics and Communication Engineering, S.R.M. University, Kattankulathur, Kancheepuram Dt. — 603203, Tamilnadu, India <sup>b</sup> Institut Charles Delaunay, Universite de Technologie de Troyes, 12 Rue Marie Curie, 10000 Troyes, France

## a r t i c l e i n f o

Article history: Received 30 January 2010 Received in revised form 7 November 2010 Accepted 21 November 2010 Available online 26 November 2010

Keywords: Average queue lengths Average response times Average waiting times Utilizations Steady-state probability Supply chain

## a b s t r a c t

In this paper, a supply chain (four-input three-stage queuing network) receives uniformly distributed orders from clients. An input order is represented by two stochastic variables, occurrence time and the quantity of items to be delivered. The objective of this work is to compute the minimum response time, and thus the average number of items (optimum capacity) that can be delivered with this response time. Performance measures such as average queue lengths, average response times, and average waiting times of the jobs in the supply chain, and in the equivalent single-server network are derived, plotted and discussed.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. Overview

Queuing models have been used to investigate supply chain problems for many years. They consider the average arrival rate of orders, the average customer service rate, the cost to the order waiting time (customer dissatisfaction), and the cost to operate customer service points, and strive to minimize the business cost.

Current generation enterprises, such as global supply chains, virtual enterprises and e-businesses are driving research in the area of enterprise modeling framework suitable for a distributed environment. Each company is at the center of a network of suppliers and customers. Supply chain could be de<sup>fi</sup>ned as a network of connected and interdependent organizations mutually and co-operatively working together to control, manage, and improve the <sup>fl</sup>ow of materials and information from suppliers to end users [1]. In [2], the joint equilibrium distribution of queue sizes and equilibrium state probabilities in a network of queues containing N service centers and R classes of customers is derived. In [3], the authors analyze the memory interference caused by several processors simultaneously using several memory modules. The assumptions and results of the simple model are tested against some measurements of program behavior and simulations of systems using memory references from real programs.

## 1.2. Literature review

Numerous research work has been done on the areas of modeling e-businesses, enterprise systems, assembly and manufacturing systems using queuing networks.

When the clients are heterogeneous goods (simple customers, shops, stores, etc), the quantity of orders may vary widely and have to be modeled as a stochastic variable. Without any additional information about the economical context, the best way is to assume a uniform distribution for the quantity of orders, thus characterizing the quantity of orders to lie between a minimum and maximum value. In this case, any input (order) to the queuing system has to be represented by two stochastic variables, one for the time of occurrence, and one for the quantity to deliver. This constitutes the main improvement of this paper over [4], [5] and [6].

In [7], the focus is on characterizing the average end-to-end delay and maximum achievable per node throughput in random access multihop wireless ad hoc networks with stationary nodes. The random access multihop wireless networks can be modeled as G/G/1 queuing network and uses the diffusion approximation to evaluate closed form expressions for the average end-to-end delay. A lot of focus on queuing models of manufacturing systems, and many approximations for evaluating the performance of queuing networks are carried out in [8] and [9]. A discrete-time Markov chain is developed in [10] to model the routing of new emails through a contact center. The fundamental

A1, A2, A3, A4 are Activities

matrix of the absorbing Markov chain developed in [10], is used to obtain the average number of visits an email makes to a particular node before getting resolved.

Supply chain (SC) is a concept which can be considered analogous to a pipeline of physical and informational <sup>fl</sup>ows between suppliers and customers. From an operational point of view, this pipeline works like a process of activities, and these activities are distributed. So, the term “chain” could be replaced by the term “network” [11].

Queuing network model is a very useful tool to analyze the system performance from an abstract model. In [12], concise descriptive summaries of the various queuing models are detailed in the manufacturing context. Since the supply chain management (SCM) is a market-driven concept, it is necessary to adopt the customer's point of view. For this reason, the “process” concept [13] is represented as an object initiated with an objective expressed generally in terms of quantity, quality, and delay. Among these attributes, the delay is generally the most critical one. In this paper, the term “process” is referred to as “treatment of orders”. It re<sup>fl</sup>ects the fact that when considering the performance of a SCM system, the inputs are the “orders” and the outputs are the “goods”. A process is composed of activities that use resources which are networkcon<sup>fi</sup>gured. There are other processes in industrial systems, such as supply or maintenance, that can be considered to be collaborative processes of the main process.

Queuing models are used to obtain apriori information not only about important performance measures like queue lengths, response times, and waiting times, but also other performance measures like: (a) probability that any delay will occur, (b) probability that the total delay is greater than a predetermined value, (c) probability that all service facilities will be idle, (d) expected idle time of the total facility, and (e) probability of turnaways due to insuf<sup>fi</sup>cient waiting accommodation. Some kind of queuing problems involve determining the appropriate number of service facilities to cover expected demand, as well as determining the ef<sup>fi</sup>ciency of servers and the number of servers of different types at the service facilities [14]. In [15], the performance evaluation of an assembly system with components or sub-assemblies feeding into a kitting and assembly stage framework is studied. In that example, the quantity of the orders was considered as a constant.

Decision problems often consist of numerous smaller decisions that are aggregated and interleaved while spanning multiple domains, paradigms, and other perspectives. In [16], the authors propose and implement a framework and architecture that uses different pillars of <sup>fl</sup>exibility in decision making and independence of components to support the decision making process.

In [17], the authors compute approximations for response time distributions for queuing networks with Poisson or phase-type arrival processes and general service time distributions. In [18], it is shown that price dynamics are more complicated than simply balancing consumption demands, capacities for transformation, and raw material supplies. These patterns of price dynamics are identi<sup>fi</sup>ed, which explain their cause and propose rules linking initial market conditions with the occurrence of these patterns.

In [20], the problem of assigning the best service rate to minimize the expected delay under a cost constraint is considered. Also studied are systems with several types of customers, general service time distributions, stochastic or deterministic routing, and a variety of service regimes.

Fig. 1 illustrates how the logical concept is mapped to the “physical system”. In this <sup>fi</sup>gure, successive activities represent stages (or steps) in a given process. Each of them is realized in a site with speci<sup>fi</sup>c resources. In the general case, from a given activity output, there are many possible connections to the next activity. If sites are geographically scattered (sites of the same company, subcontractors), a transport activity must be inserted between two transformation activities. In manufacturing systems, the production nomenclature means “assembling of components” and “convergence of physical <sup>fl</sup>ows” to a <sup>fi</sup>nal point.

![](/api/attachments/JYYAD9GF/fulltext/images/9aa746e63fe697b7c1671130cb8b6f6235173dbdf1a6436c341ff5ed1c419210.jpg)  
Fig. 1. Physical <sup>fl</sup>ow diagram in the supply chain.

When the treatment of orders is made, their evaluation consists in a comparison between the objective and the result. The global challenge of the process approach is: a) to initialize correctly, each process objective with a realistic delay value. The delay objective to be assigned represents the expected value of the delay (or lead-time) plus a security margin. It can be derived from the statistics (average response time) or from the actual state of the system in terms of waiting times and service times at the nodes. In this case, it is necessary to convert all waiting activities and services to be executed in a global throughput time, and to choose the route that minimizes the lead-time. The same evaluation results may also be useful for b) a negotiation with a potential client during an e-business or an ecommerce transaction. For the company, it represents the lead-time promised for a given order.

The main challenge of the SCM system is to improve the performance while reducing the costs (generally in terms of tradeoffs). The challenge addressed in this paper is to represent a physical network of resources with a queuing model. Each resource is modeled as a server and waiting activities are in a queue. More precisely, an activity is a logical object which contains attributes such as: reference process (order number), quantity to produce, and objective delay. Throughout this paper, we assume that a process will correspond to each order. By the virtualization induced using process approach, the object process tracks the physical <sup>fl</sup>ow. Among classical performance measures obtained by a queuing representation (average queue length, average response time, etc.), this will lead to estimating a minimum lead-time. The computing challenge is to determine the best strategy to setup a process in terms of delay measures. This ef<sup>fi</sup>ciency is measurable with the number of processes which ful<sup>fi</sup>l their objective.

All processes are supervised and need to be controlled. The control is generally performance-centric, which means that during the life of a process cycle, a drift situation can be detected between the result and the objective, and corrections can be applied. Since processes are in competition to access resources, and since resources are capacitylimited, the drift situation can be due to breakdown problem of a resource, set-up times, and activities (inventory, transport) of interfaces. One of the correction variables is the possibility to reroute the physical <sup>fl</sup>ow from one node to an alternative resource for the next activity (if several ways are possible). This local challenge is similar to point a), except that the route includes the breakpoint. This is a routing problem and is similar to those that have been addressed in the <sup>fi</sup>eld of telecommunication networks.

## 1.3. Organization of the paper

The objective of this paper is to compute the minimum response time for the delivery of an item to the <sup>fi</sup>nal destination along the three stages of the queuing network. The average number of items that can be delivered with this response time constitute the capacity of the network. Section 2 describes the supply chain (textile manufacturing system) and discusses some more papers on Literature survey. Section 3 presents a queuing network approach to model a textile manufacturing system. Closed-form expressions are derived for utilizations for each node (queue and server) in the network. Section 4 derives, plots and discusses performance measures like average response times, average queue lengths, and average waiting times of individual nodes and different paths in the network. This section also discusses the average queue lengths, average response times, and equivalent service rate of the equivalent single-queue, single-server network. Section 5 describes the numerical results. Finally, Section 6 presents the Conclusions.

## 2. Supply chain description

## 2.1. Textile manufacturing system

Supply chain constitutes basic activities like (i) Knitting, (ii) Making, and (iii) Distribution (the central warehousing). The Warehouse corresponds to a European Warehouse. For performance evaluation, the supply chain is modeled by a process with these three activities (three stages). In fact, these activities may be supported by operational resources physically distributed in many sites and interlinked by transportation. Consider Fig. 2.

• Knitting locations are in L1 (France), L2 (Morocco), and C (Contractor).

• Making locations are in L1 and L2, L3 (Morocco), and L4 (Tunisia). The warehouse location is in L1.

There are routing choices for the physical <sup>fl</sup>ows at two steps of the processes. They are at:

• Knitting: From S to L1 or L2, from S to L2 or C,

• Making: From L1 to L1 or L3, (or) from L2 to L2 or L4.

![](/api/attachments/JYYAD9GF/fulltext/images/b2e03d2b80802f97eab350e52ba3c5f0425b3c0562100a404ce98b747e962959.jpg)  
Fig. 2. Block diagram for queuing formulation of the network of processes (4-input network).

Each resource is modeled as a queue where batches are waiting to be processed (see Fig. 2). The routing decision may be performed considering the estimated throughput delay from $S _ { 1 }$ to $S _ { 4 } .$ This delay includes the manufacturing delay (depending on the batch quantities to be processed) and also the total waiting times in all the downstream queues. Comparing with the routing problem in telecommunication networks (IP networks), the problem is not a hop by hop problem [19], but we consider the whole route to make the decision.

We can easily separate the global problem to the example given in this paper by providing this example as an illustration of a more general issue. It is interesting to focus on processes which use resources that are network-con<sup>fi</sup>gured. In other words, those orders which follow a particular distribution on the arrival rate will be con<sup>fi</sup>gured to the network. We can thus propose an interest to queuing modeling by considering the arrival and departure processes modeled using a particular distribution.

For each output of L1 and L2 in stage I, there are two possible connections (two routes), and this example is like any assembling system. The output of L1 of stage I is connected to nodes L1 and L3 of stage II, whereas the output of L2 of stage I is connected to nodes L2 and L4 of stage II. Finally, the departures from servers, A11 and A13 arrive at $S _ { 1 } ,$ and the departures from servers A12 and A14 arrive at $S _ { 1 } .$ Thus, the nodes in different paths are not cross-linked. It is important to deal with this special case to accommodate the case of “urgent orders” and “regular orders”. Urgent orders correspond to orders which require quick processing and regular orders correspond to orders which require normal processing. The orders can be routed appropriately to L1 and L2 of stage I, and subsequently to L1, L2, L3, and L4 of stage II for processing.

In order to make a comparison of this special industrial system to a more generic supply chain, the service times and order arrivals can have a different distribution than that considered in this paper. For example, the service time could be modeled as a Lognormal distribution proposed to model supplier delay. A G/M/1 or $G / G / 1$ queue could be used to model a generic supply chain. The global challenge is to be able to estimate an “apriori” performance measure which is necessary to propose a suitable Quality of Service (QoS) (for e.g., minimum response time) to the client.

The various kinds of dif<sup>fi</sup>culties in modeling the SCM system using queues other than M/M/1 queue are described as follows:

1) M/M/1 queues have Poisson arrival process and exponentially distributed service times. State description for M/M/1 queuing model is simple as one needs just a number in the system denoting the system state. This is possible because the exponential service time distribution is memoryless. For M/G/1 queues, where the arrival process is Poisson, but service times have a general (arbitrary) distribution, the general state description would require speci<sup>fi</sup>cations on both the number in the system and the amount of service already provided to the customer currently being served.

2) The G/M/1 queue is the dual of M/G/1 queue, where the arrival process is a general one, but the service times are exponentially distributed. The state descriptions are found under equilibrium conditions at the time instants just before job arrivals to the system. The state distributions are also valid for the departure instants (just after a job leaves the system) as Kleinrock's principle is applicable to this system. The state distributions are not valid at arbitrary time instants (or ergodic, time-average results, since Poisson Arrival See Time Averages (PASTA) will not be applicable to the system $( \mathrm { i . e . }$ , the arrival process is not Poisson).

3) For M/E /1 or $E _ { k } / E _ { k } / 1$ queues, where $E _ { k }$ is the Erlang distribution with k phases, the probability of packet loss or the probability of packet delay can be determined according to various assumptions made to <sup>fi</sup>nd if the blocked orders are aborted (Erlang B) or blocked orders are queued until served (Erlang C) [Erlang B and Erlang C formulas are in everyday use for traf<sup>fi</sup>c modeling or transportation applications].

4) For G/G/1 and G/G/m queues (m is the number of servers), only when the offered traf<sup>fi</sup>c is high (i.e., utilization, ρ, gets close to 1), the distribution of the waiting time will be approximately exponentially distributed. The waiting times become very large as ρ≈1. For other values of offered traf<sup>fi</sup>c, the distribution of the waiting time has a general distribution, thus making state descriptions not valid at arbitrary time instants. Thus, it is reasonable to use M/M/1 queues to offer a simple and feasible solution to the given SCM problem.

The importance of minimum response time estimation in the supply chain network is given below:

In a distributed hard real-time system, such as the supply chain problem, communication between tasks on different processors must occur in bounded time. The inevitable communication delay is composed of both the delay in transmitting a message on the communication media, and also the delay in delivering the data to the destination task. A simple delivery approach is considered in this paper, the arrival of an “order” generates an interrupt called “ondemand” approach. As soon as the order arrives at the source node, it is routed to all intermediate nodes leading to the destination node. The objective is to <sup>fi</sup>nd the path between the source node and the destination node which provides the minimum response time.

The shortest path problem in the dynamic supply chain network considered in this paper is a problem of sending an order from an origin node to a destination node with the least delay over a network that has no perfect, permanent <sup>fi</sup>xed structure, and which is subjected to varying volumes of traf<sup>fi</sup>c. The optimal path connecting the origin and destination nodes through several intermediate nodes is called the shortest path since it produces the least response time. Once a shortest path is identi<sup>fi</sup>ed, care should be taken to see that all incoming orders are not dumped onto this path, thereby causing congestion on the shortest path route. ${ \mathsf { S } } 0 ,$ it is advisable to increase the service rate or reduce the service time of servers on all nonshortest path routes, thereby redistributing the incoming orders to balance the load (offered traf<sup>fi</sup>c).

A man–machine system is modeled and analyzed in [21] using graphical simulation software package. The validated model is used for evaluating alternate routings to <sup>fi</sup>nd out the optimum route. A multi-layered queuing network that models a client–server system where clients and servers communicate via synchronous and asynchronous messages is discussed in [22].

Closed-form solutions have been derived for the response time distributions through a particular path in open product-form queuing networks in [23]. The research goal in [24] is to develop a simulation model of overhead monorail conveyor systems and statistical methods for the analysis and multi-objective optimization of the manufacturing process. For closed product-form queuing networks with n customers, the Sevcik–Mitrani arrival theorem in [25] states that an arriving customer would see the network in equilibrium with one less customer. Suri suggested the use of queuing theory to provide quick solutions to supply chain problems in [26].

A model of a closed queuing network within which customer routing between queues depends on the state of the network is presented in [27]. For queuing network models, Little's theorem and steady-state probabilities are de<sup>fi</sup>ned in [28]. In some supply chains, orders are generated by important applicants (for e.g., supermarkets). Whitt described in [29], the Queuing Network Analyzer (QNA), a software package developed at Bell Laboratories to calculate approximate congestion measures for a network of queues.

Concurrent Engineering is a systematic approach to integrate concurrent design of products and their related processes. In [30], the characteristics of fuzzy, multi-stage evaluation, and decision making in concurrent product development processes are analyzed and a decision support system for product design in concurrent Engineering is presented.

In [32], a transformation technique is proposed from Uni<sup>fi</sup>ed Modeling Language (UML) to queuing network model. This approach avoids the need for a prototype implementation since we can determine the overall performance from the architectural design description. The research in [31] is motivated by the arbitrary nature of customer orders and dynamic changes of demand patterns and the ability to overcome such uncertainty by enterprise collaboration. Demand and capacity sharing protocols have been designed in [31] to <sup>fi</sup>nd ef<sup>fi</sup>cient demand and capacity sharing decisions in the collaborative network.

## 3. Queuing network description

We shall consider one type of product (tee-shirt) in the supply chain given in Fig. 2. Orders arrive in one portal, but processes can start in two places. There are three stages (i.e., three activities). They are: Knitting, Making and Delivery, which can be realized in four sites. Because of the network structure, different routes are possible depending on the traf<sup>fi</sup>c, which implies transport activity is necessary. All physical <sup>fl</sup>ows converge to a central warehouse. The analysis of the four-input, three-stage queuing network follows:

## 3.1. Stage I

There are 4-inputs in the queuing network considered in Fig. 2. The arrival rates at the 4-inputs are $\lambda _ { 1 } , \lambda _ { 2 } ,$ λ and $\lambda _ { 4 }$ respectively. The arrival rate at source $S _ { 1 } \mathrm { i } s \left( \lambda + \delta \right)$ . The probability of arrivals at $S _ { 2 }$ and $S _ { 3 }$ are $s _ { 1 }$ and s respectively. The arrival rates at $S _ { 2 }$ and $S _ { 3 }$ are λ and δ respectively. If we assume that the probability of arrivals at $S _ { 2 }$ and $S _ { 3 }$ are equal, then $\lambda = \delta = { \textstyle \frac { 1 } { 2 } } ( \lambda + \delta ) = { \textstyle \frac { 1 } { 2 } } \lambda ^ { ( 0 ) } = { \textstyle \frac { 1 } { 2 } } \lambda ^ { ( e ) }$ , where $\boldsymbol { \lambda } ^ { ( 0 ) }$ and $\lambda ^ { ( e ) }$ are the minimum arrival rates for the <sup>fi</sup>rst two inputs and last two inputs, respectively, of the birth–death process shown in Fig. 3. The probability of arrivals at $Q _ { 4 }$ and $Q _ { 5 }$ are $q _ { 1 }$ and $q _ { 2 }$ respectively. The probability of arrivals at $Q _ { 2 1 }$ and $Q _ { 2 0 }$ are $r _ { 1 }$ and $r _ { 2 }$ respectively.

Let $\lambda _ { 1 } ( = \lambda q _ { 1 } )$ be the arrival rate of jobs at $Q _ { 4 }$ , and let $\lambda _ { 2 } ( = \lambda q _ { 2 } )$ be the arrival rate at $Q _ { 5 } .$ Let the service rates of servers A4 and A5 be $\mu _ { 1 }$ and $\mu { \prime } _ { 1 }$ respectively. After getting serviced at server A4, the jobs arrive at the queues $Q _ { 8 }$ and $Q _ { 1 5 }$ with probabilities $p _ { 1 }$ and $p _ { 2 }$ respectively. So, the arrival rate at $Q _ { 8 }$ is $\lambda _ { 1 } p _ { 1 }$ , and the arrival rate at $Q _ { 1 5 }$ is $\lambda _ { 1 } p _ { 2 } .$ . Jobs which get serviced by server A5 arrive at the queues $Q _ { 1 7 }$ and $Q _ { 1 8 }$ with

![](/api/attachments/JYYAD9GF/fulltext/images/de3217edf92c480e4b5dfc1d386f053cb58f9740527fcb6481db2fe634e7f479.jpg)  
Service A: Production & Delivery

Occurrence: Poissonian law justified

Quantity: Stochastic

Delay: QoS

Average Queue Length: $N _ { \mathit { s y s } }$

Average Waiting time: $W _ { s y s }$

![](/api/attachments/JYYAD9GF/fulltext/images/fcd8bc5c795c422c6773d97604d961792f269e837b3e21203b54e539a40c830a.jpg)

Average Response time: $R _ { \mathit { s y s } }$

Service time:

Service time is initialized when the first production operation begins. It is closed when the items are available in the delivery stocks.

probabilities $p _ { 3 }$ and $p _ { 4 }$ respectively. So, the arrival rate at $Q _ { 1 7 }$ is λ p , and the arrival rate at $Q _ { 1 8 }$ is $\lambda _ { 2 } p _ { 4 }$

Let $\lambda _ { 3 } ( = \delta r _ { 1 } )$ be the arrival rate of jobs at $Q _ { 2 1 } ,$ , and let $\lambda _ { 4 } ( = \delta r _ { 2 } )$ ) be the arrival rate at $Q _ { 2 0 } .$ . Let the service rate of servers A21 and A20 be μ and $\mu _ { 2 } ^ { \prime }$ respectively. Let the service rates of A3, A6, A22 be $\mu _ { 5 } , \mu _ { 6 } ^ { \prime } ,$ and $\mu _ { 2 2 } ^ { \prime }$ respectively. Jobs which get serviced by server A3 enter the queues $Q _ { 1 7 }$ and $Q _ { 1 9 }$ with probabilities $p _ { 5 }$ and $p _ { 6 }$ respectively. Similarly, jobs which get serviced by server A22 enter the queues $Q _ { 8 }$ and $Q _ { 1 6 }$ with probabilities $p _ { 7 }$ and $p _ { 8 }$ respectively.

## 3.2. Stage II

• The total arrival rate of jobs at queue, $\boldsymbol { Q } _ { 8 } ,$ is $( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } )$ . Jobs with this arrival rate get serviced by server A8 whose service rate is $\mu _ { 8 } .$

• The total arrival rate at $Q _ { 1 7 } \mathrm { i s } ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } )$ . The jobs get serviced by server $A 1 7 ,$ , whose service rate is $\cdot \mu _ { 1 7 } ^ { \prime }$ . Jobs with arrival rate, $( \lambda _ { 2 } p _ { 3 } +$ $\lambda _ { 3 } p _ { 5 } )$ , get serviced by server A9 whose service rate is $\mu { \prime } _ { 9 } .$

• The arrival rate at $Q _ { 1 5 }$ is $( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } )$ . Jobs at queue, $Q _ { 1 5 } ,$ , get serviced by server A15 whose service rate is $\mu _ { 1 5 }$ . Since $Q _ { 1 5 }$ and Q are in serial connection, the arrival rate at $Q _ { 7 }$ is also $( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } )$ . The service rate of server A7 is $\mu _ { 7 }$

• The arrival rate at $Q _ { 1 8 }$ is $( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6 } )$ . Jobs at queue, $Q _ { 1 8 } ,$ get serviced by server $A 1 8$ whose service rate is $\mu ^ { \prime } { \boldsymbol { 1 8 } } \cdot$ . Since $Q _ { 1 8 }$ and $Q _ { 1 0 }$ are in serial connection, the arrival rate at $Q _ { 1 0 }$ is also $( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6 } )$ The service rate of server A10 is $\mu ^ { \prime }$ .

## 3.3. Stage III

• Jobs getting serviced by server $A 8 ,$ arrive at queue, $Q _ { 1 1 }$ with arrival rate, $( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } )$ , and get serviced by server A11 whose service rate is $\mu _ { 1 1 }$

• Jobs getting serviced by server A9, arrive at $Q _ { 1 2 }$ with arrival rate, $( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } )$ , and get serviced by server $A 1 2 ,$ , whose service rate is $\mu { ' } _ { 1 2 }$

• Jobs getting serviced by server A7, arrive at $Q _ { 1 3 }$ with arrival rate, $( \lambda _ { 2 } p _ { 4 } + \lambda _ { 4 } p _ { 8 } )$ , and get serviced by server A13, whose service rate is $\mu _ { 1 3 } .$

• Jobs getting serviced by server A10, arrive at $Q _ { 1 4 }$ with arrival rate, $( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6 } )$ , and get serviced by server A14, whose service rate is $\mu ^ { \prime } { } _ { 1 4 } .$

Finally, jobs after service completion at servers A11, A12, A13, and A14 arrive at the sink, $S _ { 4 } ,$ , with departure rate, $( \lambda + \delta )$ . For satisfactory management and control requirements, it is required that $\mu _ { 1 } = \mu _ { 1 } ^ { \prime }$ and $\mu _ { 8 } = \mu ^ { \prime } { } _ { 9 } = \mu _ { 7 } = \mu ^ { \prime } { } _ { 1 0 } .$ . Fig. 4 represents the overall system in terms of (i) Production, and (ii) Delivery.

A node is de<sup>fi</sup>ned by a queue and its corresponding server.

The nodes in Stage I are: (Q<sub>4</sub>, A4), (Q<sub>5</sub>, A5), (Q<sub>21</sub>, A21), (Q<sub>3</sub>, A3), $( Q _ { 2 0 } , A 2 0 ) , ( Q _ { 6 } , A 6 ) , ( Q _ { 2 2 } , A 2 2 ) .$

$$
\begin{array}{l} \text { The   nodes   in   Stage   II   are: } (Q _ {8}, A 8), (Q _ {1 7}, A 1 7), (Q _ {9}, A 9), (Q _ {1 5}, A 1 5), \\ (Q _ {7}, A 7), (Q _ {1 8}, A 1 8), (Q _ {1 0}, A 1 0). \end{array}
$$

The nodes in Stage III are: $( Q _ { 1 1 } , A 1 1 ) , ( Q _ { 1 2 } , A 1 2 ) , ( Q _ { 1 3 } , A 1 3 ) , ( Q _ { 1 4 } ,$ A14).

![](/api/attachments/JYYAD9GF/fulltext/images/2324b29ad733de2f4be58944f2964e0b9df2b24652d9e35013a6b63447020f2c.jpg)  
GLOBAL SERVICE

Each activity belongs to a speci<sup>fi</sup>c process. Each activity is an object which describes a speci<sup>fi</sup>c task that the resource has to do. Here, Ai's are the differential activities carried out in this industrial system. The activities, A4, A5, A3, and A6 are called “Knitting”, activities A7, A8, A9 and A10 are called “Making”, and activities A11, A12, A13, A14, A15, A17, A18, A20, A21, and A22 are called “Transporting”.

As discussed in [4], the minimum arrival rate of the birth–death process shown in Fig. 3 is $\Lambda _ { k } = \lambda ^ { ( 0 ) } = \lambda ^ { ( e ) } = \frac { 1 } { E ( z ) } = \frac { 2 ( \lambda + \delta ) } { b + a } = \frac { \bar { 4 } \lambda } { b + a } ,$ since λ=δ. The ratio

$$
\rho = \frac {\text { mean   arrival   rate }}{\text { mean   service   rate }} = \frac {\Lambda_ {k}}{\mu_ {k}} = \frac {1}{\mu E (z)} = \frac {4 \lambda}{\mu (b + a)} \forall a > 0, b > 0, b > a.\tag{1}
$$

The quantity, $\rho ,$ is an important parameter, called the traf<sup>fi</sup>c intensity of the system. Traf<sup>fi</sup>c intensity is expressed in Erlangs.

From the birth–death process for continuous-time homogeneous Markov chains, the steady-state probability of having k jobs in the system with batch arrivals is given by [28]

$$
\Pi_ {k} = (\exp (- (1 - \rho))) ^ {k} \Pi_ {0} = \exp (- k (1 - \rho)) \Pi_ {0} \forall a > 0, b > 0, b > a.\tag{2}
$$

It can be shown that the mean and variance of the number of customers in the system are

$$
E [ N ] = \sum_ {k = 0} ^ {\infty} k \Pi_ {k} = \Pi_ {0} \sum_ {k = 0} ^ {\infty} k \exp (- k (1 - \rho)) = \frac {1}{1 - \exp (- (1 - \rho))},\tag{3}
$$

$$
\sigma_ {N} ^ {2} = \sum_ {k = 0} ^ {\infty} (k - E (N)) ^ {2} \Pi_ {k} = \frac {\exp (- (1 - \rho))}{(1 - \exp (- (1 - \rho))) ^ {2}},\tag{4}
$$

respectively.

Using Eq. (1), the utilizations of the servers in Stage I are:

$$
\rho_ {1} ^ {(A 4)} = \frac {\lambda_ {1}}{\mu_ {1}} = \frac {\lambda^ {(0)} q _ {1}}{2 \mu_ {1}} = \frac {4 \lambda}{(b + a)} \frac {q _ {1}}{2 \mu_ {1}},
$$

$$
\begin{array}{l} \rho_ {1} ^ {\prime (A 5)} = \frac {\lambda_ {2}}{\mu_ {1} ^ {\prime}} = \frac {\lambda^ {(0)} q _ {2}}{2 \mu_ {1} ^ {\prime}} = \frac {4 \lambda}{(b + a)} \frac {q _ {2}}{2 \mu_ {1} ^ {\prime}}, \\ \rho_ {2 1} ^ {(A 2 1)} = \frac {\lambda_ {3}}{\mu_ {2}} = \frac {\lambda^ {(e)} r _ {1}}{2 \mu_ {2}} = \frac {4 \lambda}{(b + a)} \frac {r _ {1}}{2 \mu_ {2}}, \\ \rho_ {5} ^ {(A 3)} = \frac {\lambda_ {3}}{\mu_ {5}} = \frac {\lambda^ {(e)} r _ {1}}{2 \mu_ {5}} = \frac {4 \lambda}{(b + a)} \frac {r _ {1}}{2 \mu_ {5}}, \\ \rho_ {6} ^ {\prime (A 6)} = \frac {\lambda_ {4}}{\mu_ {6} ^ {\prime}} = \frac {\lambda^ {(e)} r _ {2}}{2 \mu_ {6} ^ {\prime}} = \frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {6} ^ {\prime}}, \\ \rho_ {2} ^ {\prime (A 2 0)} = \frac {\lambda_ {4}}{\mu_ {2} ^ {\prime}} = \frac {\lambda^ {(e)} r _ {2}}{2 \mu_ {2} ^ {\prime}} = \frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {2} ^ {\prime}}, \\ \rho_ {2 2} ^ {\prime (A 2 2)} = \frac {\lambda_ {4}}{\mu_ {2 2} ^ {\prime}} = \frac {\lambda^ {(e)} r _ {2}}{2 \mu_ {2 2} ^ {\prime}} = \frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {2 2} ^ {\prime}}. \end{array}\tag{5}
$$

The utilizations of the servers in Stage II are:

$$
\begin{array} { l } \rho _ { 8 } ^ { ( A 8 ) } = \frac { \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } } { \mu _ { 8 } } = \frac { \lambda ^ { ( 0 ) } q _ { 1 } p _ { 1 } + \lambda ^ { ( e ) } r _ { 2 } p _ { 7 } } { 2 \mu _ { 8 } } = \left( \frac { 4 \lambda } { b + a } \right) \frac { q _ { 1 } p _ { 1 } + r _ { 2 } p _ { 7 } } { 2 \mu _ { 8 } } , \\ \rho _ { 1 7 } ^ { ' ( A 7 ) } = \frac { \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } } { \mu _ { 1 7 } ^ { ' } } = \frac { \lambda ^ { ( 0 ) } q _ { 2 } p _ { 3 } + \lambda ^ { ( e ) } r _ { 1 } p _ { 5 } } { 2 \mu _ { 1 7 } ^ { ' } } = \left( \frac { 4 \lambda } { b + a } \right) \frac { q _ { 2 } p _ { 3 } + r _ { 1 } p _ { 5 } } { 2 \mu _ { 1 7 } ^ { ' } } , \\ \rho _ { 9 } ^ { ' ( A 9 ) } = \frac { \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } } { \mu _ { 9 } ^ { ' } } = \frac { \lambda ^ { ( 0 ) } q _ { 2 } p _ { 3 } + \lambda ^ { ( e ) } r _ { 1 } p _ { 5 } } { 2 \mu _ { 9 } ^ { ' } } = \left( \frac { 4 \lambda } { b + a } \right) \frac { q _ { 2 } p _ { 3 } + r _ { 1 } p _ { 5 } } { 2 \mu _ { 9 } ^ { ' } } , \\ \rho _ { 1 5 } ^ { ( A 1 5 ) } = \frac { \lambda _ { 1 } p _ { 2 } } { \mu _ { 1 5 } } = \frac { \lambda ^ { ( 0 ) } q _ { 1 } p _ { 2 } } { 2 \mu _ { 1 5 } } = \left( \frac { 4 \lambda } { b + a } \right) \frac { q _ { 1 } p _ { 2 } } { 2 \mu _ { 1 5 } } , \\ \rho _ { 1 6 } ^ { ( A 1 6 ) } = \frac { \lambda _ { 4 } p _ { 8 } } { \mu _ { 1 6 } } = \frac { \lambda ^ { ( e ) } r _ { 2 } p _ { 8 } } { 2 \mu _ { 1 6 } } = \left( \frac { 4 \lambda } { b + a } \right) \frac { r _ { 2 } p _ { 8 } } { 2 \mu _ { 1 6 } } , \\ \rho _ { 7 } ^ { ( A 7 ) } = \frac { \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } } { \mu _ { 7 } } = \frac { \lambda ^ { ( 0 ) } q _ { 1 } p _ { 2 } + \lambda ^ { ( e ) } r _ { 2 } p _ { 8 } } { 2 \mu _ { 7 } } = \left( \frac { 4 \lambda } { b + a } \right) \frac { q _ { 1 } p _ { 2 } + r _ { 2 } p _ { 8 } } { 2 \mu _ { 7 } } , \\ \rho _ { 1 8 } ^ { ' ( A 1 8 ) } = \frac { \lambda _ { 2 } p _ { 4 } } { \mu _ { 1 8 } ^ ' } = \frac { \lambda ^ { ( 0 ) } q _ { 2 } p _ { 4 } } { 2 \mu _ { 1 8} ^ ' } = \left( \frac { 4 \lambda } { b + a } \right) \frac { q _ { 2 } p _ { 4 } } { 2 \mu _ { 1 8} ^ ' }, \\ \rho _ { 1 9 } ^ { ' ( A 1 9 ) } = \frac { \lambda _ { 3 } p _ { 6 } } { \mu _ { 1 9} ^ ' } = \frac { \lambda ^ { ( e ) } r _ { 1 } p _ { 6 } } { 2 \mu _ { 1 9} ^ ' } = \left( \frac { 4 \lambda } { b + a } \right) \frac { r _ { 1 } p _ { 6 } } { 2 \mu _ { 1 9} ^ ' }, \\ \rho _ { 1 0 } ^ { ' ( A 1 0 ) } = \frac { \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6 } } { \mu _ { 1 0} ^ ' } = \frac { \lambda ^ { ( 0 ) } q _ { 2 } p _ { 4 } + \lambda ^ { ( e ) } r _ { 1 } p _ { 6 }}{ 2 \mu _ { 1 0} ^ ' } = \left( \frac { 4 \lambda } { b + a }\right) \frac { q _ { 2 } p _ { 4 } + r _ { 1 } p _ { 6 }}{ 2 \mu _ { 1 0} ^ ' }. \end{array}\tag{6}
$$

The utilizations of the servers in Stage III are:

$$
\begin{array}{r l} & {\rho_ {1 3} ^ {(A 1 3)} = \frac {\lambda_ {1} p _ {2} + \lambda_ {4} p _ {8}}{\mu_ {1 3}} = \frac {\lambda^ {(0)} q _ {1} p _ {2} + \lambda^ {(e)} r _ {2} p _ {8}}{2 \mu_ {1 3}} = \left(\frac {4 \lambda}{b + a}\right) \frac {q _ {1} p _ {2} + r _ {2} p _ {8}}{2 \mu_ {1 3}},} \\ & {\rho_ {1 1} ^ {(A 1 1)} = \frac {\lambda_ {1} p _ {1} + \lambda_ {4} p _ {7}}{\mu_ {1 1}} = \frac {\lambda^ {(0)} q _ {1} p _ {1} + \lambda^ {(e)} r _ {2} p _ {7}}{2 \mu_ {1 1}} = \left(\frac {4 \lambda}{b + a}\right) \frac {q _ {1} p _ {1} + r _ {2} p _ {7}}{2 \mu_ {1 1}},} \\ & {\rho_ {1 2} ^ {' (A 1 2)} = \frac {\lambda_ {2} p _ {3} + \lambda_ {3} p _ {5}}{\mu_ {1 2} ^ {'}} = \frac {\lambda^ {(0)} q _ {2} p _ {3} + \lambda^ {(e)} r _ {1} p _ {5}}{2 \mu_ {1 2} ^ {'}} = \left(\frac {4 \lambda}{b + a}\right) \frac {q _ {2} p _ {3} + r _ {1} p _ {5}}{2 \mu_ {1 2} ^ {'}},} \\ & {\rho_ {1 4} ^ {' (A 1 4)} = \frac {\lambda_ {2} p _ {4} + \lambda_ {3} p _ {6}}{\mu_ {1 4} ^ {'}} = \frac {\lambda^ {(0)} q _ {2} p _ {4} + \lambda^ {(e)} r _ {1} p _ {6}}{2 \mu_ {1 4} ^ {'}} = \left(\frac {4 \lambda}{b + a}\right) \frac {q _ {2} p _ {4} + r _ {1} p _ {6}}{2 \mu_ {1 4} ^ {'}}.} \end{array}\tag{7}
$$

## 4. Performance measures

The performance measures of a single-server are measured by the average queue lengths, average waiting times, average response times, and the average number of jobs in the system.

## 4.1. Average queue lengths

Using Eq. (3), the average queue lengths of servers in Stage I are:

$$
\begin{array}{l} E \Big [ N _ {1} ^ {(A 4)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {1} ^ {(A 4)} \Big) \Big)}, \\ E \Big [ N _ {1} ^ {' (A 5)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {1} ^ {'} (A 5) \Big) \Big)}, \\ E \Big [ N _ {2 1} ^ {(A 2 1)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {2 1} ^ {(A 2 1)} \Big) \Big)}, \\ E \Big [ N _ {5} ^ {(A 3)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {5} ^ {(A 3)} \Big) \Big)}, \\ E \Big [ N _ {6} ^ {' (A 6)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {6} ^ {' (A 6)} \Big) \Big)}, \\ E \Big [ N _ {2 2} ^ {' (A 2 2)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {2 2} ^ {' (A 2 2)} \Big) \Big)}, \\ E \Big [ N _ {2} ^ {' (A 2 0)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {2} ^ {' (A 2 0)} \Big) \Big)}. \end{array}\tag{8}
$$

The average queue lengths of servers in Stage II are:

$$
E \left[ N _ {8} ^ {(A 8)} \right] = \frac {1}{1 - \exp \left(- \left(1 - \rho_ {8} ^ {(A 8)}\right)\right)},
$$

$$
E \Big [ N _ {1 7} ^ {' (A 1 7)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {1 7} ^ {' (A 1 7)} \Big) \Big)},
$$

$$
E \left[ R _ {6} ^ {\prime (A 6)} \right] = \frac {E \left[ N _ {6} ^ {\prime (A 6)} \right]}{\lambda^ {(e)} r _ {2}} = \left(\frac {b + a}{4 \lambda r _ {2}}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {6} ^ {\prime (A 6)}\right)\right)},
$$

$$
E \Big [ N _ {1 0} ^ {\prime (A 1 0)} \Big ] = \frac {1}{1 - \exp \Big (- \big (1 - \rho_ {1 0} ^ {\prime (A 1 0)} \big) \Big)},\tag{11}
$$

$$
E \left[ R _ {2 2} ^ {\prime (A 2 2)} \right] = \frac {E \left[ N _ {2 2} ^ {\prime (A 2 2)} \right]}{\lambda^ {(e)} r _ {2}} = \left(\frac {b + a}{4 \lambda r _ {2}}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {2 2} ^ {\prime (A 2 2)}\right)\right)},
$$

$$
E \left[ N _ {9} ^ {\prime (A 9)} \right] = \frac {1}{1 - \exp \left(- \left(1 - \rho_ {9} ^ {\prime (A 9)}\right)\right)},
$$

$$
E \Big [ N _ {7} ^ {(A 7)} \Big ] = \frac {1}{1 - \exp \Big (- \big (1 - \rho_ {7} ^ {(A 7)} \big) \Big)},
$$

$$
E \left[ R _ {2} ^ {\prime (A 2 0)} \right] = \frac {E \left[ N _ {2} ^ {\prime (A 2 0)} \right]}{\lambda^ {(e)} r _ {2}} = \left(\frac {b + a}{4 \lambda r _ {2}}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {2} ^ {\prime (A 2 0)}\right)\right)}.
$$

$$
E \left[ N _ {1 5} ^ {(A 1 5)} \right] = \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 5} ^ {(A 1 5)}\right)\right)},
$$

The average response times in Stage II are:

$$
E \left[ R _ {8} ^ {(A 8)} \right] = \frac {E \left[ N _ {8} ^ {(A 8)} \right]}{\lambda^ {(0)} q _ {1} p _ {1} + \lambda^ {(e)} r _ {2} p _ {7}} = \left(\frac {b + a}{4 \lambda (q _ {1} p _ {1} + r _ {2} p _ {7})}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {8} ^ {(A 8)}\right)\right)},\tag{9}
$$

$$
E \left[ R _ {1 7} ^ {\prime (A 1 7)} \right] = \frac {E \left[ N _ {1 7} ^ {\prime (A 1 7)} \right]}{\lambda^ {(0)} q _ {2} p _ {3} + \lambda^ {(e)} r _ {1} p _ {5}} = \left(\frac {b + a}{4 \lambda \left(q _ {2} p _ {3} + r _ {1} p _ {5}\right)}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {1 7} ^ {\prime (A 1 7)}\right)\right)},
$$

$$
E \Big [ N _ {1 6} ^ {(A 1 6)} \Big ] = \frac {1}{1 - \exp \Big (- \big (1 - \rho_ {1 6} ^ {(A 1 6)} \big) \Big)},
$$

$$
E \left[ N _ {1 8} ^ {\prime (A 1 8)} \right] = \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 8} ^ {\prime (A 1 8)}\right)\right)},
$$

$$
E \Big [ R _ {1 0} ^ {\prime (A 1 0)} \Big ] = \frac {E \Big [ N _ {1 0} ^ {\prime (A 1 0)} \Big ]}{\lambda^ {(0)} q _ {2} p _ {4} + \lambda^ {(e)} r _ {1} p _ {6}} = \Big (\frac {b + a}{4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6})} \Big) \frac {1}{1 - e x p \Big (- \Big (1 - \rho_ {1 0} ^ {\prime (A 1 0)} \Big) \Big)},
$$

$$
E \Big [ N _ {1 9} ^ {' (A 1 9)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {1 9} ^ {' (A 1 9)} \Big) \Big)}.
$$

$$
E \left[ R _ {9} ^ {\prime (A 9)} \right] = \frac {E \left[ N _ {9} ^ {\prime (A 9)} \right]}{\lambda^ {(0)} q _ {2} p _ {3} + \lambda^ {(e)} r _ {1} p _ {5}} = \left(\frac {b + a}{4 \lambda \left(q _ {2} p _ {3} + r _ {1} p _ {5}\right)}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {9} ^ {\prime (A 9)}\right)\right)},
$$

The average queue lengths of servers in Stage III are:

$$
E \left[ N _ {1 3} ^ {(A 1 3)} \right] = \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 3} ^ {(A 1 3)}\right)\right)},
$$

$$
E \left[ R _ {7} ^ {(A 7)} \right] = \frac {E \left[ N _ {7} ^ {(A 7)} \right]}{\lambda^ {(0)} q _ {1} p _ {2} + \lambda^ {(e)} r _ {2} p _ {8}} = \left(\frac {b + a}{4 \lambda (q _ {1} p _ {2} + r _ {2} p _ {8})}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {7} ^ {(A 7)}\right)\right)},
$$

$$
E \Big [ N _ {1 1} ^ {(A 1 1)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {1 1} ^ {(A 1 1)} \Big) \Big)},
$$

$$
E \Big [ N _ {1 2} ^ {' (A 1 2)} \Big ] = \frac {1}{1 - \exp \Big (- \Big (1 - \rho_ {1 2} ^ {' (A 1 2)} \Big) \Big)},\tag{10}
$$

$$
E \left[ R _ {1 5} ^ {(A 1 5)} \right] = \frac {E \left[ N _ {1 5} ^ {(A 1 5)} \right]}{\lambda^ {(0)} q _ {1} p _ {2}} = \left(\frac {b + a}{4 \lambda q _ {1} p _ {2}}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {1 5} ^ {(A 1 5)}\right)\right)},
$$

$$
E \left[ R _ {2 1} ^ {(A 2 1)} \right] = \frac {E \left[ N _ {2 1} ^ {(A 2 1)} \right]}{\lambda^ {(e)} r _ {1}} = \left(\frac {b + a}{4 \lambda r _ {1}}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {2 1} ^ {(A 2 1)}\right)\right)},
$$

$$
E \left[ R _ {5} ^ {(A 3)} \right] = \frac {E \left[ N _ {5} ^ {(A 3)} \right]}{\lambda^ {(e)} r _ {1}} = \left(\frac {b + a}{4 \lambda r _ {1}}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {5} ^ {(A 3)}\right)\right)},
$$

$$
E \left[ N _ {1 4} ^ {\prime (A 1 4)} \right] = \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 4} ^ {\prime (A 1 4)}\right)\right)}.
$$

$$
E \left[ R _ {1} ^ {\prime (A 5)} \right] = \frac {E \left[ N _ {1} ^ {\prime (A 5)} \right]}{\lambda^ {(0)} q _ {2}} = \left(\frac {b + a}{4 \lambda q _ {2}}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1} ^ {\prime (A 5)}\right)\right)},
$$

$$
E \Big [ R _ {1 6} ^ {(A 1 6)} \Big ] = \frac {E \Big [ N _ {1 6} ^ {(A 1 6)} \Big ]}{\lambda^ {(e)} r _ {2} p _ {8}} = \Big (\frac {b + a}{4 \lambda r _ {2} p _ {8}} \Big) \frac {1}{1 - e x p \big (- \big (1 - \rho_ {1 6} ^ {(A 1 6)} \big) \big)},
$$

## 4.2. Average response times

$$
E \left[ R _ {1 8} ^ {\prime (A 1 8)} \right] = \frac {E \left[ N _ {1 8} ^ {\prime (A 1 8)} \right]}{\lambda^ {(0)} q _ {2} p _ {4}} = \left(\frac {b + a}{4 \lambda q _ {2} p _ {4}}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {1 8} ^ {\prime (A 1 8)}\right)\right)},\tag{12}
$$

$$
E \left[ R _ {1 9} ^ {\prime (A 1 9)} \right] = \frac {E \left[ N _ {1 9} ^ {\prime (A 1 9)} \right]}{\lambda^ {(e)} r _ {1} p _ {6}} = \left(\frac {b + a}{4 \lambda r _ {1} p _ {6}}\right) \frac {1}{1 - e x p \left(- \left(1 - \rho_ {1 9} ^ {\prime (A 1 9)}\right)\right)}.
$$

Using Little's theorem in [28], the average response times in Stage I are:

$$
E \left[ R _ {1} ^ {(A 4)} \right] = \frac {E \left[ N _ {1} ^ {(A 4)} \right]}{\lambda^ {(0)} q _ {1}} = \left(\frac {b + a}{4 \lambda q _ {1}}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1} ^ {(A 4)}\right)\right)},
$$

The average response times in Stage III are:

$$
E \left[ R _ {1 3} ^ {(A 1 3)} \right] = \frac {E \left[ N _ {1 3} ^ {(A 1 3)} \right]}{\lambda_ {1} p _ {2} + \lambda_ {4} p _ {8}} = \left(\frac {b + a}{4 \lambda (q _ {1} p _ {2} + r _ {2} p _ {8})}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 3} ^ {(A 1 3)}\right)\right)},
$$

$$
E \left[ R _ {1 1} ^ {(A 1 1)} \right] = \frac {E \left[ N _ {1 1} ^ {(A 1 1)} \right]}{\lambda_ {1} p _ {1} + \lambda_ {4} p _ {7}} = \left(\frac {b + a}{4 \lambda (q _ {1} p _ {1} + r _ {2} p _ {7})}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 1} ^ {(A 1 1)}\right)\right)},
$$

$$
E \left[ R _ {1 2} ^ {\prime (A 1 2)} \right] = \frac {E \left[ N _ {1 2} ^ {\prime (A 1 2)} \right]}{\lambda_ {2} p _ {3} + \lambda_ {3} p _ {5}} = \left(\frac {b + a}{4 \lambda (q _ {2} p _ {3} + r _ {1} p _ {5})}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 2} ^ {\prime (A 1 2)}\right)\right)},
$$

$$
E \left[ R _ {1 4} ^ {\prime (A 1 4)} \right] = \frac {E \left[ N _ {1 4} ^ {\prime (A 1 4)} \right]}{\lambda_ {2} p _ {4} + \lambda_ {3} p _ {6}} = \left(\frac {b + a}{4 \lambda \left(q _ {2} p _ {4} + r _ {1} p _ {6}\right)}\right) \frac {1}{1 - \exp \left(- \left(1 - \rho_ {1 4} ^ {\prime (A 1 4)}\right)\right)}.\tag{13}
$$

## 4.3. Average waiting times

The average waiting times in Stage I are:

$$
E \left[ W _ {1} ^ {(A 4)} \right] = E \left[ R _ {1} ^ {(A 4)} \right] - \frac {1}{\mu_ {1}} = \frac {(b + a) \mu_ {1} - 4 \lambda q _ {1} \left(1 - \exp \left(- \left(1 - \rho_ {1} ^ {(A 4)}\right)\right)\right)}{4 \lambda q _ {1} \mu_ {1} \left(1 - \exp \left(- \left(1 - \rho_ {1} ^ {(A 4)}\right)\right)\right)},
$$

$$
E \left[ W _ {1} ^ {\prime (A 5)} \right] = E \left[ R _ {1} ^ {\prime (A 5)} \right] - \frac {1}{\mu_ {1} ^ {\prime}} = \frac {(b + a) \mu_ {1} ^ {\prime} - 4 \lambda q _ {2} \left(1 - \exp \left(- \left(1 - \rho_ {1} ^ {\prime (A 5)}\right)\right)\right)}{4 \lambda q _ {2} \mu_ {1} ^ {\prime} \left(1 - \exp \left(- \left(1 - \rho_ {1} ^ {\prime (A 5)}\right)\right)\right)},
$$

$$
E \left[ W _ {2 1} ^ {(A 2 1)} \right] = E \left[ R _ {2 1} ^ {(A 2 1)} \right] - \frac {1}{\mu_ {2}} = \frac {(b + a) \mu_ {2} - 4 \lambda r _ {1} \left(1 - \exp \left(- \left(1 - \rho_ {2 1} ^ {(A 2 1)}\right)\right)\right)}{4 \lambda r _ {1} \mu_ {2} \left(1 - \exp \left(- \left(1 - \rho_ {2 1} ^ {(A 2 1)}\right)\right)\right)},
$$

$$
E \left[ W _ {5} ^ {(A 3)} \right] = E \left[ R _ {5} ^ {(A 3)} \right] - \frac {1}{\mu_ {5}} = \frac {(b + a) \mu_ {5} - 4 \lambda r _ {1} (1 - \exp (- (1 - \rho_ {5} ^ {(A 3)})))}{4 \lambda r _ {1} \mu_ {5} (1 - \exp (- (1 - \rho_ {5} ^ {(A 3)})))},
$$

$$
E \Big [ W _ {6} ^ {' (A 6)} \Big ] = E \Big [ R _ {6} ^ {' (A 6)} \Big ] - \frac {1}{\mu_ {6} ^ {\prime}} = \frac {(b + a) \mu_ {6} ^ {\prime} - 4 \lambda r _ {2} \left(1 - \exp \left(- \left(1 - \rho_ {6} ^ {' (A 6)}\right)\right)\right)}{4 \lambda r _ {2} \mu_ {6} ^ {\prime} \left(1 - \exp \left(- \left(1 - \rho_ {6} ^ {' (A 6)}\right)\right)\right)},
$$

$$
E \left[ W _ {2 2} ^ {\prime (A 2 2)} \right] = E \left[ R _ {2 2} ^ {\prime (A 2 2)} \right] - \frac {1}{\mu_ {2 2} ^ {\prime}} = \frac {(b + a) \mu_ {2 2} ^ {\prime} - 4 \lambda r _ {2} \left(1 - \exp \left(- \left(1 - \rho_ {2 2} ^ {\prime (A 2 2)}\right)\right)\right)}{4 \lambda r _ {2} \mu_ {2 2} ^ {\prime} \left(1 - \exp \left(- \left(1 - \rho_ {2 2} ^ {(A 2 2)}\right)\right)\right)},
$$

$$
E \left[ W _ {2} ^ {\prime (A 2 0)} \right] = E \left[ R _ {2} ^ {\prime (A 2 0)} \right] - \frac {1}{\mu_ {2} ^ {\prime}} = \frac {(b + a) \mu_ {2} ^ {\prime} - 4 \lambda r _ {2} \left(1 - \exp \left(- \left(1 - \rho_ {2} ^ {\prime (A 2 0)}\right)\right)\right)}{4 \lambda r _ {2} \mu_ {2} ^ {\prime} \left(1 - \exp \left(- \left(1 - \rho_ {2} ^ {\prime (A 2 0)}\right)\right)\right)}.\tag{14}
$$

The average waiting times in Stage II are:

$$
\begin{array}{l} E \Big [ W _ {8} ^ {(A 8)} \Big ] = E \Big [ R _ {8} ^ {(A 8)} \Big ] - \frac {1}{\mu_ {8}} = \frac {(b + a) \mu_ {8} - 4 \lambda (q _ {1} p _ {1} + r _ {2} p _ {7}) \big (1 - \exp \big (- \big (1 - \rho_ {8} ^ {(A 8)} \big) \big) \big)}{4 \lambda (q _ {1} p _ {1} + r _ {2} p _ {7}) \mu_ {8} \big (1 - \exp \big (- \big (1 - \rho_ {8} ^ {(A 8)} \big) \big) \big)}, \\ E \Big [ W _ {1 7} ^ {\prime (A 1 7)} \Big ] = E \Big [ R _ {1 7} ^ {\prime (A 1 7)} \Big ] - \frac {1}{\mu_ {1 7} ^ {\prime}} \\ = \frac {(b + a) \mu_ {1 7} ^ {\prime} - 4 \lambda (q _ {2} p _ {3} + r _ {1} p _ {5}) \big (1 - \exp \big (- \big (1 - \rho_ {1 7} ^ {\prime (A 1 7)} \big) \big) \big)}{4 \lambda (q _ {2} p _ {3} + r _ {1} p _ {5}) \mu_ {1 7} ^ {\prime} \big (1 - \exp \big (- \big (1 - \rho_ {1 7} ^ {\prime (A 1 7)} \big) \big) \big)}, \\ E \Big [ W _ {9} ^ {\prime (A 9)} \Big ] = E \Big [ R _ {9} ^ {\prime (A 9)} \Big ] - \frac {1}{\mu_ {9} ^ {\prime}} = \frac {(b + a) \mu_ {9} ^ {\prime} - 4 \lambda (q _ {2} p _ {3} + r _ {1} p _ {5}) \big (1 - \exp \big (- \big (1 - \rho_ {9} ^ {\prime (A 9)} \big) \big) \big)}{4 \lambda (q _ {2} p _ {3} + r _ {1} p _ {5}) \mu_ {9} ^ {\prime} \big (1 - \exp \big (- \big (1 - \rho_ {9} ^ {\prime (A 9)} \big) \big) \big)}. \end{array}
$$

$$
\begin{array}{l} E \Big [ W _ {7} ^ {(A 7)} \Big ] = E \Big [ R _ {7} ^ {(A 7)} \Big ] - \frac {1}{\mu_ {7}} = \frac {(b + a) \mu_ {7} - 4 \lambda (q _ {1} p _ {2} + r _ {2} p _ {8}) \big (1 - \exp \big (- \big (1 - \rho_ {7} ^ {(A 7)} \big) \big) \big)}{4 \lambda (q _ {1} p _ {2} + r _ {2} p _ {8}) \mu_ {7} \big (1 - \exp \big (- \big (1 - \rho_ {7} ^ {(A 7)} \big) \big) \big)} \\ E \Big [ W _ {1 0} ^ {' (A 1 0)} \Big ] = E \Big [ R _ {1 0} ^ {' (A 1 0)} \Big ] - \frac {1}{\mu_ {1 0} ^ {'}} \\ \qquad = \frac {(b + a) \mu_ {1 0} ^ {'} - 4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6}) \big (1 - \exp \big (- \big (1 - \rho_ {1 0} ^ {' (A 1 0)} \big) \big) \big)}{4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6}) \mu_ {1 0} ^ {'} \big (1 - \exp \big (- \big (1 - \rho_ {1 0} ^ {' (A 1 0)} \big) \big) \big)}, \\ E \Big [ W _ {1 5} ^ {(A 1 5)} \Big ] = E \Big [ R _ {1 5} ^ {(A 1 5)} \Big ] - \frac {1}{\mu_ {1 5}} = \frac {(b + a) \mu_ {1 5} - 4 \lambda q _ {1} p _ {2} \big (1 - \exp \big (- \big (1 - \rho_ {1 5} ^ {(A 1 5)} \big) \big) \big)}{4 \lambda q _ {1} p _ {2} \mu_ {1 5} \big (1 - \exp \big (- \big (1 - \rho_ {1 5} ^ {(A 1 5)} \big) \big) \big)}, \\ E \Big [ W _ {1 6} ^ {(A 1 6)} \Big ] = E \Big [ R _ {1 6} ^ {(A 1 6)} \Big ] - \frac {1}{\mu_ {1 6}} = \frac {(b + a) \mu_ {1 6} - 4 \lambda r _ {2} p _ {8} \big (1 - \exp \big (- \big (1 - \rho_ {1 6} ^ {(A 1 6)} \big) \big) \big)}{4 \lambda r _ {2} p _ {8} \mu_ {1 6} \big (1 - \exp \big (- \big (1 - \rho_ {1 6} ^ {(A 1 6)} \big) \big) \big)}, \\ E \Big [ W _ {1 8} ^ {' (A 1 8)} \Big ] = E \Big [ R _ {1 8} ^ {' (A 1 8)} \Big ] - \frac {1}{\mu_ {1 8} ^ {'}} = \frac {(b + a) \mu_ {1 8} ^ {'} - 4 \lambda q _ {2} p _ {4} \big (1 - \exp \big (- \big (1 - \rho_ {1 8} ^ {' (A 1 8)} \big) \big) \big)}{4 \lambda q _ {2} p _ {4} \mu_ {1 8} ^ {'} \big (1 - \exp \big (- \big (1 - \rho_ {1 8} ^ {' (A 1 8)} \big) \big) \big)}, \\ E \Big [ W _ {1 9} ^ {' (A 1 9)} \Big ] = E \Big [ R _ {1 9} ^ {' (A 1 9)} \Big ] - \frac {1}{\mu_ {1 9} ^ {'}} = \frac {(b + a) \mu_ {1 9} ^ {'} - 4 \lambda r _ {1} p _ {6} \big (1 - \exp \big (- \big (1 - \rho_ {1 9} ^ {' (A 1 9)} \big) \big) \big)}4 \lambda r _ {1} p _ {6} \mu_ {1 9} ^ {'} \big (1 - \exp \big (- (\mathbf {\Phi} (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi})) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf{\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\mathbf {\Phi}) (\texttt {.}) \\ . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . & . | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
\end{array}\tag{15}
$$

The average waiting times in Stage III are:

$$
\begin{array}{l} E \Big [ W _ {1 1} ^ {(A 1 1)} \Big ] = E \Big [ R _ {1 1} ^ {(A 1 1)} \Big ] - \frac {1}{\mu_ {1 1}} = \frac {(b + a) \mu_ {1 1} - 4 \lambda (q _ {1} p _ {1} + r _ {2} p _ {7}) \big (1 - e x p \big (- \big (1 - \rho_ {1 1} ^ {(A 1 1)} \big) \big) \big)}{4 \lambda (q _ {1} p _ {1} + r _ {2} p _ {7}) \mu_ {1 1} \big (1 - e x p \big (- \big (1 - \rho_ {1 1} ^ {(A 1 1)} \big) \big) \big)}, \\ E \Big [ W _ {1 2} ^ {' (A 1 2)} \Big ] = E \Big [ R _ {1 2} ^ {' (A 1 2)} \Big ] - \frac {1}{\mu_ {1 2} ^ {\prime}} \\ \qquad = \frac {(b + a) \mu_ {1 2} ^ {\prime} - 4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6}) \big (1 - e x p \big (- \big (1 - \rho_ {1 2} ^ {' (A 1 2)} \big) \big) \big)}{4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6}) \mu_ {1 2} ^ {\prime} \big (1 - e x p \big (- \big (1 - \rho_ {1 2} ^ {' (A 1 2)} \big) \big) \big)}, \\ E \Big [ W _ {1 3} ^ {(A 1 3)} \Big ] = E \Big [ R _ {1 3} ^ {(A 1 3)} \Big ] - \frac {1}{\mu_ {1 3}} = \frac {(b + a) \mu_ {1 3} - 4 \lambda (q _ {1} p _ {2} + r _ {2} p _ {8}) \big (1 - e x p \big (- \big (1 - \rho_ {1 3} ^ {(A 1 3)} \big) \big) \big)}{4 \lambda (q _ {1} p _ {2} + r _ {2} p _ {8}) \mu_ {1 3} \big (1 - e x p \big (- \big (1 - \rho_ {1 3} ^ {(A 1 3)} \big) \big) \big)}, \\ E \Big [ W _ {1 4} ^ {' (A 1 4)} \Big ] = E \Big [ R _ {1 4} ^ {' (A 1 4)} \Big ] - \frac {1}{\mu_ {1 4} ^ {\prime}} \\ \qquad = \frac {(b + a) \mu_ {1 4} ^ {\prime} - 4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6}) \big (1 - e x p \big (- \big (1 - \rho_ {1 4} ^ {' (A 1 4)} \big) \big) \big)}{4 \lambda (q _ {2} p _ {4} + r _ {1} p _ {6}) \mu_ {1 4} ^ {\prime} \big (1 - e x p \big (- \big (1 - \rho_ {1 4} ^ {' (A 1 4)} \big) \big) \big)}. \end{array}\tag{16}
$$

4.4. Average queue lengths in different paths

The average number of jobs in path X<sub>1</sub> (A4,A8,A11) is

$$
E \left[ N _ {X _ {1}} \right] = E \left[ N _ {1} ^ {(A 4)} \right] + E \left[ N _ {8} ^ {(A 8)} \right] + E \left[ N _ {1 1} ^ {(A 1 1)} \right].\tag{17}
$$

The average number of jobs in path $X _ { 2 }$ (A4,A15,A7,A13) is

$$
E \left[ N _ {X _ {2}} \right] = E \left[ N _ {1} ^ {(A 4)} \right] + E \left[ N _ {1 5} ^ {(A 1 5)} \right] + E \left[ N _ {7} ^ {(A 7)} \right] + E \left[ N _ {1 3} ^ {(A 1 3)} \right].\tag{18}
$$

The average number of jobs in path $X _ { 3 }$ (A5,A17,A9,A12) is

$$
E \Big [ N _ {X _ {3}} \Big ] = E \Big [ N _ {1} ^ {\prime (A 5)} \Big ] + E \Big [ N _ {1 7} ^ {\prime (A 1 7)} \Big ] + E \Big [ N _ {9} ^ {\prime (A 9)} \Big ] + E \Big [ N _ {1 2} ^ {\prime (A 1 2)} \Big ].\tag{19}
$$

The average number of jobs in path $X _ { 4 }$ (A5,A18,A10,A14) is

$$
E \Big [ N _ {X _ {4}} \Big ] = E \Big [ N _ {1} ^ {\prime (A 5)} \Big ] + E \Big [ N _ {1 8} ^ {\prime (A 1 8)} \Big ] + E \Big [ N _ {1 0} ^ {\prime (A 1 0)} \Big ] + E \Big [ N _ {1 4} ^ {\prime (A 1 4)} \Big ].\tag{20}
$$

The average number of jobs in path X (A21,A3,A17,A9,A12) is

$$
E \left[ N _ {X _ {5}} \right] = E \left[ N _ {2 1} ^ {(A 2 1)} \right] + E \left[ N _ {5} ^ {(A 5)} \right] + E \left[ N _ {1 7} ^ {\prime (A 1 7)} \right] + E \left[ N _ {9} ^ {\prime (A 9)} \right] + E \left[ N _ {1 2} ^ {\prime (A 1 2)} \right].\tag{21}
$$

The average number of jobs in path $X _ { 6 }$ (A21,A3,A18,A10,A14) is

$$
E \left[ N _ {X _ {6}} \right] = E \left[ N _ {2 1} ^ {(A 2 1)} \right] + E \left[ N _ {5} ^ {(A 5)} \right] + E \left[ N _ {1 8} ^ {\prime (A 1 8)} \right] + E \left[ N _ {1 0} ^ {\prime (A 1 0)} \right] + E \left[ N _ {1 4} ^ {\prime (A 1 4)} \right].\tag{22}
$$

The average number of jobs in path $X _ { 7 }$ (A20,A6,A22,A8,A11) is

$$
E \left[ N _ {X _ {7}} \right] = E \left[ N _ {2} ^ {\prime (A 2 0)} \right] + E \left[ N _ {6} ^ {\prime (A 6)} \right] + E \left[ N _ {2 2} ^ {\prime (A 2 2)} \right] + E \left[ N _ {8} ^ {(A 8)} \right] + E \left[ N _ {1 1} ^ {(A 1 1)} \right].\tag{23}
$$

The average number of jobs in path $X _ { 8 }$ (A20,A6,A22,A15,A7,A13) is

$$
\begin{array}{c} E \Big [ N _ {X _ {8}} \Big ] = E \Big [ N _ {2} ^ {\prime (A 2 0)} \Big ] + E \Big [ N _ {6} ^ {\prime (A 6)} \Big ] + E \Big [ N _ {2 2} ^ {\prime (A 2 2)} \Big ] + E \Big [ N _ {1 5} ^ {(A 1 5)} \Big ] \\ + E \Big [ N _ {7} ^ {(A 7)} \Big ] + E \Big [ N _ {1 3} ^ {(A 1 3)} \Big ]. \end{array}\tag{24}
$$

## 4.5. Average response times in different paths

The global throughput delay from $S _ { 1 }$ to $S _ { 4 }$ in Fig. 2 can be chosen to be the minimum of the response times of the eight paths shown below. The global throughput delay represents the order's cycle. This can be done by

• considering that orders are independently and equally routed from $S _ { 1 }$ to $S _ { 4 } ,$ and

• optimizing the route by taking into account the present state of the network.

The average response time in path $X _ { 1 } ~ ( A 4 , A 8 , A 1 1 )$ is

$$
E \left[ R _ {X _ {1}} \right] = E \left[ R _ {1} ^ {(A 4)} \right] + E \left[ R _ {8} ^ {(A 8)} \right] + E \left[ R _ {1 1} ^ {(A 1 1)} \right].\tag{25}
$$

The average response time in path $X _ { 2 } \ ( A 4 , A 1 5 , A 7 , A 1 3 )$ is

$$
E \left[ R _ {X _ {2}} \right] = E \left[ R _ {1} ^ {(A 4)} \right] + E \left[ R _ {1 5} ^ {(A 1 5)} \right] + E \left[ R _ {7} ^ {(A 7)} \right] + E \left[ R _ {1 3} ^ {(A 1 3)} \right].\tag{26}
$$

The average response time in path $X _ { 3 } \ ( A 5 , A 1 7 , A 9 , A 1 2 )$ is

$$
E \left[ R _ {X _ {3}} \right] = E \left[ R _ {1} ^ {\prime (A 5)} \right] + E \left[ R _ {1 7} ^ {\prime (A 1 7)} \right] + E \left[ R _ {9} ^ {\prime (A 9)} \right] + E \left[ R _ {1 2} ^ {\prime (A 1 2)} \right].\tag{27}
$$

The average response time in path $X _ { 4 } \ ( A 5 , A 1 8 , A 1 0 , A 1 4 )$ is

$$
E \Big [ R _ {X _ {4}} \Big ] = E \Big [ R _ {1} ^ {\prime (A 5)} \Big ] + E \Big [ R _ {1 8} ^ {\prime (A 1 8)} \Big ] + E \Big [ R _ {1 0} ^ {\prime (A 1 0)} \Big ] + E \Big [ R _ {1 4} ^ {\prime (A 1 4)} \Big ].\tag{28}
$$

The average response time in path $X _ { 5 } \ ( A 2 1 , A 3 , A 1 7 , A 9 , A 1 2 )$ is

$$
E \Big [ R _ {X _ {5}} \Big ] = E \Big [ R _ {2 1} ^ {(A 2 1)} \Big ] + E \Big [ R _ {5} ^ {(A 5)} \Big ] + E \Big [ R _ {1 7} ^ {\prime (A 1 7)} \Big ] + E \Big [ R _ {9} ^ {\prime (A 9)} \Big ] + E \Big [ R _ {1 2} ^ {\prime (A 1 2)} \Big ].\tag{29}
$$

The average response time in path $X _ { 6 }$ (A21,A3,A18,A10,A14) is

$$
E \Big [ R _ {X _ {6}} \Big ] = E \Big [ R _ {2 1} ^ {(A 2 1)} \Big ] + E \Big [ R _ {5} ^ {(A 5)} \Big ] + E \Big [ R _ {1 8} ^ {\prime (A 1 8)} \Big ] + E \Big [ R _ {1 0} ^ {\prime (A 1 0)} \Big ] + E \Big [ R _ {1 4} ^ {\prime (A 1 4)} \Big ].\tag{30}
$$

The average response time in path $X _ { 7 }$ (A20,A6,A22,A8,A11) is

$$
E \Big [ R _ {X _ {7}} \Big ] = E \Big [ R _ {2} ^ {\prime (A 2 0)} \Big ] + E \Big [ R _ {6} ^ {\prime (A 6)} \Big ] + E \Big [ R _ {2 2} ^ {\prime (A 2 2)} \Big ] + E \Big [ R _ {8} ^ {(A 8)} \Big ] + E \Big [ R _ {1 1} ^ {(A 1 1)} \Big ].\tag{31}
$$

The average response time in path $X _ { 8 }$ (A20,A6,A22,A15,A7,A13) is

$$
\begin{array}{c} E \Big [ R _ {X _ {8}} \Big ] = E \Big [ R _ {2} ^ {\prime (A 2 0)} \Big ] + E \Big [ R _ {6} ^ {\prime (A 6)} \Big ] + E \Big [ R _ {2 2} ^ {\prime (A 2 2)} \Big ] + E \Big [ R _ {1 5} ^ {(A 1 5)} \Big ] \\ + E \Big [ R _ {7} ^ {(A 7)} \Big ] + E \Big [ R _ {1 3} ^ {(A 1 3)} \Big ]. \end{array}\tag{32}
$$

4.6. Equivalent network

From [5], the queue lengths and response times of the equivalent network are given by

$$
\begin{array} { l } E \Big [ N _ { \mathrm{sys} } \Big ] = \frac { \rho _ { \mathrm{sys} } } { 1 - \rho _ { \mathrm{sys} } } = E \Big [ N _ { \mathrm{eq} } ^ { ( 1 3 ) } \Big ] + E \Big [ N _ { \mathrm{eq} } ^ { ( 1 4 ) } \Big ] = \frac { \lambda _ { 1 } } { \mu _ { 1 } - \lambda _ { 1 } } \\ + \frac { 2 ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) [ \mu _ { 8 } + \mu _ { 1 1 } - 2 ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) ] } { [ \mu _ { 8 } - ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) ] [ \mu _ { 1 1 } - ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) ] } \\ + \frac { 2 ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) } { \mu _ { 1 3 } - ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) } \\ + \frac { 2 ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) [ \mu _ { 8 } + \mu _ { 1 5 } - 2 ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) ] } { [ \mu _ { 1 5 } - ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) ] [ \mu _ { 8 } - ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) ] } \\ + \frac { \lambda _ { 2 } } { \mu _ { 1 } - \lambda _ { 2 } } + \frac { \lambda _ { 3 } ( \mu _ { 2 } + \mu _ { 5 } - 2 \lambda _ { 3 } ) } { ( \mu _ { 2 } - \lambda _ { 3 } ) ( \mu _ { 5 } - \lambda _ { 3 } ) } \\ + \frac { 2 ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) } { [ \mu _ { 1 7 } ^ { ' } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [ \mu _ { 8 } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [ \mu _ { 1 2 } ^ { ' } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] } \\ \times   \left\{ [ \mu _ { 8 } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [ \mu _ { 1 2 } ^ { ' } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] \right. \\ +   [   [ \mu _ { 1 7 } ^ { ' } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [ \mu _ { 8 } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] \\ +   [   [ \mu _ { 1 7 } ^ { ' } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [   [ \mu _ { 1 2 } ^ { ' } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5} ) ]   ] \\ +   [   [ \mu _ { 1 8 } ^ { ' } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ] [ \mu _ { 8 } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ] [   [ \mu _ { 1 4 } ^ { ' } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ]   ] \\ +   [   ( \mu _ { 8 } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) )   (   [   [   (\mu _ { 1 4} ^ {\prime} - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) )   ]   ] \\ +   [   (   [   (\mu _ { 1 8} ^ {\prime} - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) )   ]   (   [   [   (\mu _ { 1 4} ^ {\prime} - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) )   ]   ] \\ +   [   (   [   (\mu _ { 1 s} ^ {\prime} - ( \lambda _ { s} p ) + (   [   (\mu _ {\mathrm{e}} ^ {\prime} - ( \lambda_{ s}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ s}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ s}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ s}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ s}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [   (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\prime} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\sim} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\sim} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\sim} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\sim} - ( \lambda_{ t}p ) + (   [    (\mu_{ s} ^{\sim} - ( \lambda_{ t}\tag{33}
$$

But, $\rho _ { \mathrm { s y s } } = \frac { \lambda + \delta } { \mu _ { \mathrm { s y s } } }$ . So, the equivalent service rate of the equivalent single-queue-single-server network is

$$
\mu_ {\text { sys }} = \lambda + \delta + \frac {1}{D 1 5},\tag{34}
$$

where

$$
\begin{array} { l } \bullet D 1 5 = \lambda _ { 1 } D 1 5 a + ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) D 1 5 b + ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) D 1 5 c + \\ \lambda _ { 2 } D 1 5 d + \lambda _ { 3 } D 1 5 e + ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) D 1 5 f + ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6 } ) D 1 5 g + \\ \lambda _ { 4 } D 1 5 h , \\ \bullet D 1 5 a = \frac { 1 } { \mu _ { 1 } - \lambda _ { 1 } } , \\ \bullet D 1 5 b = \frac { 2 [ \mu _ { 8 } + \mu _ { 1 1 } - 2 ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) ] } { [ \mu _ { 8 } - ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) ] [ \mu _ { 1 1 } - ( \lambda _ { 1 } p _ { 1 } + \lambda _ { 4 } p _ { 7 } ) ] } , \\ \bullet D 1 5 c = \frac { 2 } { \mu _ { 1 3 } - ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) } + \frac { 2 [ \mu _ { 8 } + \mu _ { 1 5 } - 2 ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) ] } { [ \mu _ { 1 5 } - ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) ] [ \mu _ { 8 } - ( \lambda _ { 1 } p _ { 2 } + \lambda _ { 4 } p _ { 8 } ) ] } , \\ \bullet D 1 5 d = \frac { 1 } { \mu _ { 1 } - \lambda _ { 2 } } , \\ \bullet D 1 5 e = \frac { \mu _ { 2 } + \mu _ { 5 } - 2 \lambda _ { 3 } } { ( \mu _ { 2 } - \lambda _ { 3 } ) ( \mu _ { 5 } - \lambda _ { 3 } ) } , \\ \bullet D 1 5 f = \frac { 2 } { [ \mu _ { 1 7 } ^ { \prime } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [ \mu _ { 8 } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] [ \mu _ { 1 2 } ^ { \prime } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ] } \times \\ [ ( \mu _ { 8 } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ) ( \mu _ { 1 2 } ^ { \prime } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5 } ) ) + ( \mu _ { 1 7 } ^ { \prime } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5} ) ) ( \mu _ { 8 } - \\ ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5} ) ) + ( \mu _ { 1 7 } ^ { \prime } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5} ) ) ( \mu _ { 1 2 } ^ { \prime } - ( \lambda _ { 2 } p _ { 3 } + \lambda _ { 3 } p _ { 5} ) ) ] \\ \bullet D 1 5 g = \frac { 2 } { [ \mu _ { 1 8 } ^ { \prime } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ] [ \mu _ { 8 } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ] [ \mu _ { 1 4 } ^ { \prime } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ] } \times \\ [ ( \mu _ { 8 } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ) ( \mu _ { 1 4 } ^ { \prime } - ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ) + ( \mu _ { 18} ^ { \prime } - ( \lambda _ { 2 } p _ {4 } + \lambda _ { 3 } p _ {6} ) ) ( \mu _ { 14} ^ { \prime} - \\ ( \lambda _ { 2 } p _ { 4 } + \lambda _ { 3 } p _ { 6} ) ) + ( \mu _ { 18} ^ { \prime } - ( \lambda _ { 2 } p _ {4 } + \lambda _ { 3 } p _ {6} ) ) ( \mu _ { 8 } - ( \lambda _ {2 } p _ {4} + \lambda _ {3 } p _ {6} ) ) ] \\ \bullet D   |   |   | h = | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
\end{array}
$$

The average response time of the equivalent node is

$$
E \left[ R _ {\text { sys }} \right] = \frac {E \left[ N _ {\text { sys }} \right]}{\lambda + \delta},\tag{35}
$$

where $\lambda _ { 1 } = \lambda q _ { 1 } , \lambda _ { 2 } = \lambda q _ { 3 } , \lambda _ { 3 } = \delta r _ { 1 } , \mathtt { a n d } \lambda _ { 4 } = \delta r _ { 2 } .$

The average waiting time of the equivalent node is

$$
E \Big [ W _ {\mathrm{sys}} \Big ] = E \Big [ R _ {\mathrm{sys}} \Big ] - \frac {1}{\mu_ {\mathrm{sys}}},\tag{36}
$$

where $E [ R _ { \mathrm { s y s } } ]$ and $\mu _ { \mathrm { s y s } }$ are shown in Eqs. (35) and (34) respectively.

Thus, the 4-input queuing network comprising several queues and servers can be expressed as a single-queue and a single-server with arrival rate $( \lambda + \delta )$ . The average queue length, average response time and average waiting time are given by (33), (35) and (36) respectively.

## 5. Numerical results

5.1. Queue lengths of the most optimal path in the 4-input network with and without weights

## 5.1.1. No weights

Let $\lambda + \delta$ be the total number of arrivals in the 4-input queuing network at source $S _ { 1 }$ and leaving the network at sink $S _ { 4 } .$ In the example considered in this section, the arrival rate, $\lambda + \delta = 2 , 4 , . . . , 2 0$ . The values of a and b are 2 and 10 respectively. The other speci<sup>fi</sup>cations include

• Probability of arrivals at queues $Q _ { 4 }$ and $Q _ { 5 } { \mathrm { ~ a r e ~ } } ( q _ { 1 } , q _ { 2 } ) = ( 0 . 5 , 0 . 5 )$ respectively.

• Probability of arrivals at queues $Q _ { 2 1 }$ and $\mathrm { Q } _ { 2 0 } \mathrm { ~ a r e ~ } ( r _ { 1 } , r _ { 2 } ) = ( 0 . 5 , 0 . 5 )$ respectively.

• Probability of arrivals at sources $( S _ { 2 } , S _ { 3 } )$ are $( s _ { 1 } , s _ { 2 } ) = ( 0 . 5 , 0 . 5 )$

$$
(p _ {1}, p _ {2}), (p _ {3}, p _ {4}), (p _ {5}, p _ {6})
$$

• The service rate speci<sup>fi</sup>cations of different servers in the network are $\mu _ { 1 } = \mu _ { 1 } ^ { ' } = 1 5 , \mu _ { 2 } = \mu _ { 2 } ^ { ' } = 1 2 , \mu _ { 5 } = 1 6 , \mu _ { 6 } ^ { ' } = 1 4 , \mu _ { 2 2 } ^ { ' } = 1 5 ,$ $\mu _ { 8 } = \mu _ { 7 . } = \mu _ { 9 } ^ { ' } = \mu _ { 1 0 } ^ { ' } = \mu _ { 1 9 } ^ { ' } = \mu _ { 1 4 } ^ { ' } = 9 ,$ $\mu _ { 1 7 } ^ { ' } = \mu _ { 1 8 } ^ { ' } = \mu _ { 1 2 } ^ { ' } = \mu _ { 1 3 } = 8 , \mu _ { 1 5 } = 6 , \mu _ { 1 6 } = 7 , \mathrm { a n d } \mu _ { 1 1 } = 1 1 .$

For each value of $( \lambda + \delta )$ , the utilizations, average queue lengths, average response times, and average waiting times in all the nodes of the 4-input queuing network are computed. The average queue lengths in paths $X _ { 1 }$ to $X _ { 8 }$ are computed from Eqs. (17) to (24) respectively. The average response times in paths $X _ { 1 }$ to $X _ { 8 }$ are computed from Eqs. (25) to (32) respectively.

The minimum of the average response times is computed. It is found that for all arrival rates, the minimum response time corresponds to path $X _ { 2 } .$ The nodes in path $X _ { 2 }$ are $( Q _ { 4 } , A 4 ) , ( Q _ { 1 5 } , A _ { 1 5 } ) , ( Q _ { 7 } , A 7 )$ , and $( Q _ { 1 3 } , A 1 3 )$ . The average queue length corresponding to path X is noted.

## 5.1.2. Incorporating weights

When weights are incorporated, the service rates of $A 4 , A 5 , A 2 1 ,$ A20, A3, A6, A22, A8, A9, A7, and A10 are halved from their original values in part (1) [no weights section]. All other speci<sup>fi</sup>cations remain unchanged. The arrival rate, $\lambda + \delta = 2 , 4 , . . . , 2 0$ . The values of a and b are 2 and 10 respectively. The utilizations, average queue lengths, average response times and average waiting times in all the nodes are computed for each value of λ+δ. The minimum response time and its corresponding queue length are noted. It is found that for all arrival rates, the minimum response time corresponds to path X . The nodes in path $X _ { 2 }$ are $( Q _ { 4 } , A 4 ) , ( Q _ { 1 5 } , A _ { 1 5 } ) , ( Q _ { 7 } , A 7 )$ , and $( Q _ { 1 3 } , A 1 3 )$ . It is found that as the arrival rate increases, the queue length increases for the cases with and without weights. Comparing the queue length curves in Fig. 5, it can be observed that for a particular arrival rate, the queue length corresponding to the no weight case is lower than that of the case including weights. This is because, when weights are included, the service rates of some servers are halved, which means that the service times of those servers are doubled. Because of this reason, queue lengths are generally larger for the case incorporating weights as compared to the no weight case.

5.2. Queue lengths in the equivalent single-queue, single-server network with and without weights

## 5.2.1. No weights

Let λ+δ be the total number of arrivals at the equivalent singlequeue, single-server system as shown in Fig. 3. In the example considered in this section, the arrival rate is $\lambda + \delta = 1 , 2 , . . . , 1 4$ . The service rate speci<sup>fi</sup>cations of different servers in the network are $\mu _ { 1 } = \mu _ { 1 } ^ { ' } = 1 5 , ~ \mu _ { 2 } = \mu _ { 2 } ^ { ' } = 1 2 , ~ \mu _ { 5 } = 1 6 , ~ \mu _ { 6 } ^ { ' } = 1 4 , ~ \mu _ { 2 2 } ^ { ' } = 1 5 , ~ \mu _ { 8 } =$ $\mu _ { 9 } ^ { ' } = \mu _ { 7 } = \mu _ { 1 0 } ^ { ' } = \mu _ { 1 4 } ^ { ' } = \mu _ { 1 9 } ^ { ' } = 9 , \mu _ { 1 5 } = 6 , \mu _ { 1 8 } ^ { ' } = \mu _ { 1 7 } ^ { ' } = \mu _ { 1 2 } ^ { ' } = \mu _ { 1 3 } =$ $8 , \mu _ { 1 6 } = 7 ,$ , and $\mu _ { 1 1 } = 1 $ 1. The probabilities, $( p _ { 1 } , p _ { 2 } ) , ( p _ { 3 } , p _ { 4 } ) , ( p _ { 5 } , p _ { 6 } ) , ( p _ { 7 } ,$ p<sub>8</sub>), $( q _ { 1 } , q _ { 2 } ) , ( r _ { 1 } , r _ { 2 } )$ and $( s _ { 1 } , s _ { 2 } )$ are (0.3, 0.7), (0.4, 0.6), (0.2, 0.8), $( 0 . 1 , 0 . 9 ) , ( 0 . 5 , 0 . 5 ) , ( 0 . 5 , 0 . 5 )$ , and (0.5,0.5) respectively. For each value of λ+δ, the average queue length of the equivalent queue, and the average response time of the equivalent queue are computed from Eqs. (33) and (35) respectively. The service rate of the equivalent server is computed from Eq. (34).

## 5.2.2. Incorporating weights

When weights are incorporated, the service rates of $A 4 , A 5 , A 2 1$ A20, A3, A6, A22, A8, A9, A7, and A10 are halved from their original values in part Eq. (1) [no weights section]. All other speci<sup>fi</sup>cations remain unchanged. The arrival rate is $\lambda + \delta = 1 , 2 , . . . , 1 4 .$ The average queue length and average response time of the equivalent queue are computed from Eqs. (33) and (35) for each value of $\lambda + \delta .$ The service rate of the equivalent server is computed from $\operatorname { E q . }$ (34). The average queue lengths for the cases with and without diversity are plotted in Fig. 6.

Comparing the queue length curves in Fig. 6, it can be observed that the queue lengths for the case with weights, are higher than those for the no weight case. This is because, for the case when weights are incorporated, the service rates of some of the servers are halved from their original value. Hence, the service times of those servers are doubled. This leads to increase in average response time and hence the average queue length.

A comparison of the response times and waiting times of jobs in the equivalent single-queue, single-server network for the cases with and without weights is shown in Fig. 7. Clearly, the response times and waiting times are slightly larger for the case incorporating weights as compared to the no weight case. This is again attributed to the fact that when the service rates of the equivalent server is halved, the service time for servicing the jobs entering the equivalent queue is is doubled. Thus, the response times and waiting times ought to be larger for the case incorporating weights. The equivalent service rate for the system when weights are not included is $\mu _ { s y s } = 1 4 . 9 8 0 4$ , and for the case incorporating weights, it is $\mu _ { s y s } = 1 0 . 8 2 0 8 5$ , which also explains the behavior of the curves in Figs. 6 and 7.

![](/api/attachments/JYYAD9GF/fulltext/images/70b3958426cf2d859caf6ad9e96bbd5694bc07814e0d36a07f1d79d4896ed6fb.jpg)  
Fig. 5. Queue lengths for nodes in path $X _ { 2 }$ in the 4-input network with and withou weights.

![](/api/attachments/JYYAD9GF/fulltext/images/1012c02a40e70527c40a5edd04c54e670466b41089a678bf55a922edb6ffea53.jpg)  
Fig. 6. Queue lengths in the equivalent single-queue, single-server network with and without weights.

## 6. Conclusions

In this paper, the most optimal path for routing items is path $X _ { 2 }$ because it produces the least response time for the given set of speci<sup>fi</sup>cations (probability of entering a new path, arrival and service rates). The nodes in the optimal path, $X _ { 2 } ,$ are $( Q _ { 4 } , A 4 ) , ( Q _ { 1 5 } , A 1 5 ) , ( Q _ { 7 } , A 7 )$ and $( Q _ { 1 3 } , A 1 3 )$ . The choice of the optimal path depends on the speci<sup>fi</sup>cations used in numerically evaluating the response time of the queuing network model. The total number of items in the corresponding nodes of the most optimal path constitutes the capacity of the 4-input network. Decision for routing is made at the last node in each stage of the network as to which path to choose for obtaining the least response time. Performance measures such as average queue lengths are derived and plotted. Performance measures such as average response times, average waiting times and steady-state probabilities are also derived.

![](/api/attachments/JYYAD9GF/fulltext/images/9bcb259dbe523b864a8972cbe2f26404e61fd894be391bf7d158c1108c5c9ba8.jpg)

![](/api/attachments/JYYAD9GF/fulltext/images/e46ca6ac76296878257fd702a420e9de03c894f0567d509c399c7e3a22d749c9.jpg)  
Fig. 7. Response times and waiting times in the equivalent single-queue, single-server network with and without weights

The industrial system is modeled as an equivalent single-queuesingle-server system. Performance measures such as average queue lengths, average response times and average waiting times are derived and plotted. The service rate of the equivalent server is computed for the case with and without weights. For both the 4-input network and the equivalent single-queue, single-server network, for the same arrival rate, it is feasible to serve more customers for the no weight case as compared to the case when weights are included.

## Appendix A

In this section, the expressions for the steady-state probabilities of having a certain number of jobs in the system for each of the models is presented. The steady-state probabilities of jobs in Stage I are: [28]

$$
\begin{array}{l} \Pi_ {1} ^ {(A 4)} (k _ {1}) = \left(1 - \rho_ {1} ^ {(A 4)}\right) \left(\rho_ {1} ^ {(A 4)}\right) ^ {k _ {1}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {q _ {1}}{2 \mu_ {1}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {q _ {1}}{2 \mu_ {1}}\right) ^ {k _ {1}}, \\ \Pi_ {1} ^ {\prime (A 5)} (k _ {1} ^ {\prime}) = \left(1 - \rho_ {1} ^ {\prime (A 5)}\right) \left(\rho_ {1} ^ {\prime (A 5)}\right) ^ {k _ {1} ^ {\prime}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {q _ {2}}{2 \mu_ {1} ^ {\prime}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {q _ {2}}{2 \mu_ {1} ^ {\prime}}\right) ^ {k _ {1} ^ {\prime}}, \\ \Pi_ {2 1} ^ {(A 2 1)} (k _ {2 1}) = \left(1 - \rho_ {2 1} ^ {(A 2 1)}\right) \left(\rho_ {2 1} ^ {(A 2 1)}\right) ^ {k _ {2 1}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {r _ {1}}{2 \mu_ {2}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {r _ {1}}{2 \mu_ {2}}\right) ^ {k _ {2 1}}, \\ \Pi_ {5} ^ {(A 5)} (k _ {5}) = \left(1 - \rho_ {5} ^ {(A 5)}\right) \left(\rho_ {5} ^ {(A 5)}\right) ^ {k _ {5}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {r _ {1}}{2 \mu_ {5}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {r _ {1}}{2 \mu_ {5}}\right) ^ {k _ {5}}, \\ \Pi_ {6} ^ {\prime (A 6)} (k _ {6} ^ {\prime}) = \left(1 - \rho_ {6} ^ {\prime (A 6)}\right) \left(\rho_ {6} ^ {\prime (A 6)}\right) ^ {k _ {6} ^ {\prime}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {6} ^ {\prime}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {6} ^ {\prime}}\right) ^ {k _ {6} ^ {\prime}}, \\ \Pi_ {2 0} ^ {\prime (A 2 0)} (k _ {2 0} ^ {\prime}) = \left(1 - \rho_ {2} ^ {\prime (A 2 0)}\right) (\rho_ {2} ^ {\prime (A 2 0)}) ^ {k _ {2 0} ^ {\prime}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {2} ^ {\prime}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {2} ^ {\prime}}\right) ^ {k _ {2 0} ^ {\prime}}, \\ \Pi_ {2 2} ^ {\prime (A 2 2)} (k _ {2 2} ^ {\prime}) = \left(1 - \rho_ {2 2} ^ {\prime (A 2 2)}\right) (\rho_ {2 2} ^ {\prime (A 2 2)}) ^ {k _ {2 2} ^ {\prime}} = \left(1 - \frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {2 2} ^ {\prime}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {r _ {2}}{2 \mu_ {2 2} ^ {\prime}}\right) ^ {k _ {2 2} ^ {\prime}}. \end{array}\tag{37}
$$

The steady-state probabilities of jobs in Stage II are:

$$
\begin{array} { r l } \Pi _ { 8 } ^ { ( A 8 ) } ( k _ { 8 } ) & = \left( 1 - \rho _ { 8 } ^ { ( A 8 ) } \right) \left( \rho _ { 8 } ^ { ( A 8 ) } \right) ^ { k _ { 8 } } = \left( 1 - \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 1 } p _ { 1 } + r _ { 2 } p _ { 7 } } { 2 \mu _ { 8 } } \right) \left( \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 1 } p _ { 1 } + r _ { 2 } p _ { 7 } } { 2 \mu _ { 8 } } \right) ^ { k _ { 8 } } , \\ \Pi _ { 1 7 } ^ { ( A 7 ) } \left( k _ { 1 7 } ^ { \prime } \right) & = \left( 1 - \rho _ { 1 7 } ^ { ( A 7 ) } \right) \left( \rho _ { 1 7 } ^ { ( A 7 ) } \right) ^ { k _ { 1 7 } ^ { \prime } } \\ & = \left( 1 - \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 2 } p _ { 3 } + r _ { 1 } p _ { 5 } } { 2 \mu _ { 1 7 } ^ { \prime } } \right) \left( \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 2 } p _ { 3 } + r _ { 1 } p _ { 5 } } { 2 \mu _ { 1 7 } ^ { \prime } } \right) ^ { k _ { 1 7 } ^ { \prime } , } \\ \Pi _ { 9 } ^ { ( A 9 ) } \left( k _ { 9 } ^ { \prime } \right) & = \left( 1 - \rho _ { 9 } ^ { ( A 9 ) } \right) \left( \rho _ { 9 } ^ { ( A 9 ) } \right) ^ { k _ { 9 } ^ { \prime } } \\ & = \left( 1 - \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 2 } p _ { 3 } + r _ { 1 } p _ { 5 } } { 2 \mu _ { 9 } ^ { \prime } } \right) \left( \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 2 } p _ { 3 } + r _ { 1 } p _ { 5 } } { 2 \mu _ { 9 } ^ { \prime } } \right) ^ { k _ { 9 } ^ { \prime } , } \\ \Pi _ { 1 5 } ^ { ( A 1 5 ) } ( k _ { 1 5 } ) & = \left( 1 - \rho _ { 1 5 } ^ { ( A 1 5 ) } \right) \left( \rho _ { 1 5 } ^ { ( A 1 5 ) } \right) ^ { k _ { 1 5 } } = \left( 1 - \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 1 } p _ { 2 } } { 2 \mu _ { 1 5 } } \right) \left( \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 1 } p _ { 2 } } { 2 \mu _ { 1 5 } } \right) ^ { k _ { 1 5 } , } \\ \Pi _ { 1 6 } ^ { ( A 1 6 ) } ( k _ { 1 6 } ) & = \left( 1 - \rho _ { 1 6 } ^ { ( A 1 6 ) } \right) \left( \rho _ { 1 6 } ^ { ( A 1 6 ) } \right) ^ { k _ { 1 6 } } = \left( 1 - \frac { 4 \lambda } { ( b + a ) } \frac { r _ { 2 } p _ { 8 } } { 2 \mu _ { 1 6 } } \right) \left( \frac { 4 \lambda } { ( b + a ) } \frac { r _ { 2 } p _ { 8 } } { 2 \mu _ { 1 6 } } \right) ^ { k _ { 1 6 } , } \\ \Pi _ { 7 } ^ { ( A 7 ) } ( k _ { 7 } ) & = \left( 1 - \rho _ { 7 } ^ { ( A 7 ) } \right) \left( \rho _ { 7 } ^ { ( A 7 ) } \right) ^ { k _ { 7 } } = \left( 1 - \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 1 } p _ { 2 } + r _ { 2 } p _ { 8 } } { 2 \mu _ { 7 } } \right) \left( \frac { 4 \lambda } { ( b + a ) } \frac { q _ { 1 } p _ { 2 } + r _ { 2 } p _ { 8 } } { 2 \mu _ { 7 } } \right) ^ { k _ { 7 } , }, \\ \Pi _ { 1 8 } ^ { ( A 1 8 ) } ( k _ { 1 8 } ^ { \prime } ) & = \left( 1 - \rho _ { 1 8 } ^ { ( A 1 8 ) } \right) ( \rho _ { 1 8 } ^ { ( A 1 8 ) }) ^ { k _ { i n   g   ' }} = \left( 1 - \frac { 4 \lambda}{ ( b + a )} \frac { q _ { 2 } p _ { 4 } } 2 \mu _ { i n   g   '   ' }\right) \left( \frac { 4 \lambda}{ ( b + a )} \frac { q _ { 2 } p _ { 4 }}{2 {\mu_ {\mathrm{in}}   '   ' }\mathrm{in}   ' }\right) ^ {{k_{ i n   g   '}} .} \\ \Pi _  i n   g   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   " , \\ & = \left(1 - {\rho_ {\mathrm{in}    o} ^ {(A l o)}}\right) ( {\rho_ {\mathrm{in}    o} ^ {(A l o)}}) ^ {{k_{ i n} ^{    '}}} \\ & = \left(1 - {\frac {4 \lambda}{( b + a )}} \frac {{q_ {\mathrm{in}    o} p_ {\mathrm{in}    o} + r_ {\mathrm{in}    o} p_ {\mathrm{in}    o}}{2 {\mu_ {\mathrm{in}    o} ^{    '}} }}\right) (\frac {{4} {\lambda}}{(b + a)} \frac {{q_ {\mathrm{in}    o} p_ {\mathrm{in}    o} + r_ {\mathrm{in}    o} p_ {\mathrm{in}    o}}{2 {\mu_ {\mathrm{in}    o} ^{    '}} }}) ^ {{k_{ i n} ^{    '}}} . \\ & = [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ] [ c ]. \\ & = [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ] [ d ], \\ & = [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ] [ e ]. \\ & = | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
\end{array}\tag{38}
$$

The steady-state probabilities of jobs in Stage III are:

$$
\begin{array}{c} \Pi_ {1 3} ^ {(A 1 3)} (k _ {1 3}) = \Big (1 - \rho_ {1 3} ^ {(A 1 3)} \Big) \Big (\rho_ {1 3} ^ {(A 1 3)} \Big) ^ {k _ {1 3}} \\ = \Big (1 - \frac {4 \lambda}{(b + a)} \frac {q _ {1} p _ {2} + r _ {2} p _ {8}}{2 \mu_ {1 3}} \Big) \Big (\frac {4 \lambda}{(b + a)} \frac {q _ {1} p _ {2} + r _ {2} p _ {8}}{2 \mu_ {1 3}} \Big) ^ {k _ {1 3}}, \end{array}
$$

$$
\begin{array}{c} \Pi_ {1 1} ^ {(A 1 1)} (k _ {1 1}) = \Big (1 - \rho_ {1 1} ^ {(A 1 1)} \Big) \Big (\rho_ {1 1} ^ {(A 1 1)} \Big) ^ {k _ {1 1}} \\ = \Big (1 - \frac {4 \lambda}{(b + a)} \frac {q _ {1} p _ {1} + r _ {2} p _ {7}}{2 \mu_ {1 1}} \Big) \Big (\frac {4 \lambda}{(b + a)} \frac {q _ {1} p _ {1} + r _ {2} p _ {7}}{2 \mu_ {1 1}} \Big) ^ {k _ {1 1}}, \end{array}
$$

$$
\begin{array}{c} \Pi_ {1 2} ^ {\prime (A 1 2)} \Big (k _ {1 2} ^ {\prime} \Big) = \Big (1 - \rho_ {1 2} ^ {\prime (A 1 2)} \Big) \Big (\rho_ {1 2} ^ {\prime (A 1 2)} \Big) ^ {k _ {1 2} ^ {\prime}} \\ = \left(1 - \frac {4 \lambda}{(b + a)} \frac {q _ {2} p _ {3} + r _ {1} p _ {5}}{2 \mu_ {1 2} ^ {\prime}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {q _ {2} p _ {3} + r _ {1} p _ {5}}{2 \mu_ {1 2} ^ {\prime}}\right) ^ {k _ {1 2} ^ {\prime}}, \end{array}
$$

$$
\begin{array}{c} \Pi_ {1 4} ^ {\prime (A 1 4)} \Big (k _ {1 4} ^ {\prime} \Big) = \Big (1 - \rho_ {1 4} ^ {\prime (A 1 4)} \Big) \Big (\rho_ {1 4} ^ {\prime (A 1 4)} \Big) ^ {k _ {1 4} ^ {\prime}} \\ = \left(1 - \frac {4 \lambda}{(b + a)} \frac {q _ {2} p _ {4} + r _ {1} p _ {6}}{2 \mu_ {1 4} ^ {\prime}}\right) \left(\frac {4 \lambda}{(b + a)} \frac {q _ {2} p _ {4} + r _ {1} p _ {6}}{2 \mu_ {1 4} ^ {\prime}}\right) ^ {k _ {1 4} ^ {\prime}}. \end{array}\tag{39}
$$

## References

[1] J. Aitken, Supply chain integration within the context of a supplier association, PhD thesis, Cran<sup>fi</sup>eld University, 1998.

[2] F. Baskett, K. Chandy, R. Muntz, F. Palacios, Open, closed, and mixture network of queues with different classes of customers, Journal of ACM 22 (2) (1975) 248–260.

[3] F. Baskett, A. Smith, Interference in multiprocessor computer systems with interleaved memory, Communications of the ACM 19 (6) (June 1976).

[4] V. Bhaskar, P. Lallement, Activity routing in a distributed supply chain: performance evaluation with two inputs, Journal of Network and Computer Applications 31 (4) (Nov. 2008) 402–428.

[5] V. Bhaskar, P. Lallement, A four-input three-stage queuing network model approach to model an industrial system, Journal of Applied Mathematical Modelling 33 (8) (Aug. 2009) 3465–3487.

[6] V. Bhaskar, P. Lallement, Modelling a supply chain using a network of queues, Journal of Applied Mathematical Modelling 34 (8) (Aug. 2010) 2074–2088

[7] BisnikN. , AbouzeidA. , Queuing network models for delay analysis of multihop wireless and ad hoc networks, International Conference on Communications and Mobile Computing (2006) 773–778.

[8] J.A. Buzacott, Y. Kahyaoglu, Flexibility and robustness in manufacturing, International Journal of Manufacturing, Technology and Management 2 (2000) 546–558.

[9] J.A. Buzacott, J.G. Shanthikumar, D.D. Yao, Jackson network models of manufacturing systems, Stochastic models and analysis of manufacturing systems, Springer, 1994, pp. 1–45.

[10] M. Chinnaswamy, M. Kamath, On queuing network models of service systems, IE Research Conference, Atlanta, GA, May 2005.

[11] M. Christopher, Logistics and Supply chain management, third editionPrentice Hall, Inc., NJ, 2005.

[12] M.K. Govil, M.C. Fu, Queuing theory in manufacturing: a survey, Journal of Manufacturing Systems 18 (3) (1999).

[13] J. Heskett, Logistics: essential to strategy, Harvard Business Review 85 (6) (1977) 85–96.

[14] F. Hillier, G. Liebermann, Introduction to operation research, eighth editionMc-Graw Hill, Inc., NY, 2005.

[15] Y. Leung, M. Kamath, Performance analysis of a single-stage assembly system, INFORMS Annual meeting, Detroit, MI, Oct. 1994.

[16] A. Liew, D. Sundaram, Flexible modelling and support of inter-related decisions, Journal of Decision Support Systems 46 (4) (Mar. 2009) 786–802.

[17] V. Mainkar, Solutions of large and non-Markovian performance models, PhD dissertation, Department of Computer Science, Duke University, Durham, NC, 1994.

[18] T. Moyaux, P. McBurney, M. Wooldridge, A supply chain as a network of auctions, Journal of Decision Support Systems 50 (1) (Dec. 2010) 176–190.

[19] C. Perkins, P. Bhagwat, Routing over multihop wireless network of mobile computers, SIGCOMM' 94: Computer Communications Review, Oct. 1994, pp. 234–244.

[20] P. Pollett, Resource allocation in general queuing networks with applications to data networks, Technical report, Department of Mathematics, University of Queensland, Queensland 4072, Australia, 1998.

[21] R. Raja, K.S. Rao, Performance evaluation through simulation modeling in a cotton spinning system, Journal of Simulation Modeling: Practice and Theory 15 (9) (Oct. 2007) 1163–1172.

[22] S. Ramesh, H.G. Perros, A multi-layer client–server queuing network model with synchronous and asynchronous messages, IEEE Transactions on Software Engineering 26 (11) (Nov. 2000) 1086–1100.

[23] R. Schassberger, H. Daduna, Sojourn times in queuing networks with multiserver models Journal of Applied Probability 24 (1987) 511–521

[24] SerguyevichS.V. , RosalesM.G.O. , GarciaJ.M. , QuintanaL.A.Z. , LopezR.P. , Chain conveyor system simulation and optimization, th IASTED International Conference on Modeling and Simulation, 2006, pp. 172–177

[25] K. Sevcik, J. Mitrani, The distribution of queuing network states at input and output instants, Journal of the ACM 28 (1981) 358–371.

[26] R. Suri, Quick response manufacturing, Productivity press, Portland, OR, 1998

[27] D. Towsley, Queuing network models with state-dependent routing, Journal of the ACM 27 (2) (April 1980) 323–337.

[28] K. Trivedi, Probability and statistics with reliability, queuing and computer science applications, Prentice Hall, Inc., Englewood Cliffs, NJ, 1982

[29] W. Whitt, The queuing network analyzer, The Bell System Technical Journal 62 (9) (Nov. 1983).

[30] L. Xu, Z. Li, S. Li, F. Tang, A decision support system for product design in concurrent engineering, Journal of Decision Support Systems 42 (4) (Jan. 2007) 2029–2042.

[31] S. Yoon, S. Nof, Demand and capacity sharing decisions and protocols in a collaborative network of enterprises, Journal of Decision Support Systems 49 (4) (Nov. 2010) 442–450

[32] H. Youn, S. Jang, E. Lee, Deriving queuing network model for UML for software performance prediction, Fifth International Conference on Software Engineering Research Management and Applications, Aug. 2007, pp. 125–131.

![](/api/attachments/JYYAD9GF/fulltext/images/58ee06a3523685b4bee1f4cb92c07f2a5fd2de997ad988f2a7b02707737c5601.jpg)

Vidhyacharan Bhaskar received the B.Sc. degree in Mathematics from D.G. Vaishnav College, Chennai, India in 1992, M.E. degree in Electrical & Communication Engineering from the Indian Institute of Science, Bangalore in 1997, and the M.S.E. and Ph.D. degrees in Electrical Engineering from the University of Alabama in Huntsville in 2000 and 2002 respectively. During 2002–2003, he was a post-doc fellow with the Communications research group at the University of Toronto. From Sep. 2003 to Dec. 2006, he was an Associate Professor in the Département Génie des systèmes d'information et de Télécommunication at the Université de Technologie de Troves France Since January 2007, he is Professor and Associate Dean of

the Department of Electronics and Communication Engineering at S.R.M. University. Kattankulathur, India. His research interests include wireless communications, signal processing, error control coding and queuing theory. He has published 36 International Journal papers, presented 12 Conference papers in various International Conferences, and co-authored a book on MATLAB. He is also an active reviewer of refereed Journals like the IEEE Transactions on Communications, IEEE Transactions on Wireless Communications, IEEE Communication Letters, IEEE Transactions on Vehicular Technology, International Journal of Network and Computer Applications, International Journal of Applied Mathematical Modeling, International Journal of Computer Communications, International Journal of Electronics and Communication Engineering (AeUe), Wireless Personal Communications Journal, and International Journal of Computers and Electrical Engineering. Dr. Bhaskar's name was recently nominated for inclusion in the upcoming 2011 Edition of Who's Who in the World, which is scheduled for publication in November 2010.

Patrick Lallement is an Associate Professor in the University of Technology of Troyes (UTT) since 1994. He holds the “maîtrise” degree in telecommunications from the Limoges University in 1982 and the PhD degree from the University of Technology of Compiegne (UTC) in 1986. His research interest addresses the performance/ malfunctioning characterization of dynamical systems in stochastic environment, uncertainty representation risk evaluation and quantitative simulation
