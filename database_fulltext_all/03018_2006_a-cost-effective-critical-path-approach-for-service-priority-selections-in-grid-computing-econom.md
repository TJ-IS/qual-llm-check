---
otero_id: 3018
otero_key: "Z4SPTJAR"
title: "A cost-effective critical path approach for service priority selections in grid computing economy"
authors: "Mei Lin; Zhangxi Lin"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 1628– 1640

www.elsevier.com/locate/dss

# A cost-effective critical path approach for service priority selections in grid computing economy

Mei Lin <sup>a,⁎</sup>, Zhangxi Lin <sup>b,1</sup>

<sup>a</sup> Center for Research in Electronic Commerce, McCombs School of Business, The University of Texas at Austin, Austin, TX 78712, United States <sup>b</sup> Rawls College of Business Administration, Texas Tech University, Lubbock, TX 79409-2101, United States

Received 27 December 2004; received in revised form 9 January 2006; accepted 4 February 2006 Available online 29 March 2006

## Abstract

The increasing demand for grid computing resources calls for an incentive-compatible pricing mechanism for differentiated service qualities. This paper examines the optimal service priority selection problem for a grid computing services user, who is submitting a multi-subtask job for the priced services in a grid computing network. We conceptualize the problem into a prioritized critical path method (CPM) network, identify it as a time–cost tradeoff problem, and differentiate it from the traditional problem by considering a delay cost associated to the total throughput time. We define the optimal solution for the prioritized CPM network as the globally cost-effective critical path (GCCP), the optimal critical path for the solution that minimizes the total cost. As the exponential time complexity of GCCP makes the problem practically unsolvable, we propose a locally cost-effective critical path (LCCP) based approach to the prioritized CPM problem with a heuristic solution. The locally optimized priority constituting the configuration for LCCP can provide a lower bound for the throughput time of GCCP with the same time complexity as that for a traditional CPM problem. To further improve the quality of the solution, we conceive a priority adjustment algorithm named Noncritical Path Relaxation (NPR) algorithm, to refine the priority selections of the nodes on the non-critical paths. A discussion of the effects of the users' priority selections on the grid network pricing is provided to elicit future research on the computing resource pricing problem on the service-side

Keywords: Grid computing; Internet resources pricing; Critical path method (CPM); Time–cost tradeoff; Heuristic algorithm; Computational complexity

## 1. Introduction

With its fast growth, grid computing now means more than “donating CPU time for greater good” with the emergence of data grid and application grid. In fact, most of the computing resources could be “gridified” and become sharable via the Internet. According to a study by Insight Research [16], worldwide grid computing spending is predicted to increase at 81% each year, from \$250 million in 2003 to \$4.89 billion in 2008. So far, the applications and developments of grid computing have extended far beyond the original intent. The representative applications of grid computing system include Folding@Home project, which utilizes largescale distributed computing to simulate protein folding in order to study related diseases (http://www.stanford.

edu/group/pandegroup/folding/), distributed.net project that currently encompasses thousands of computers over the world (http://www.distributed.net/), and Intel Pentium IV processor-based systems, which supported the real-time collaboration and intelligence gathering in the war against terrorism [17]. Although there may be doubts about whether Great Global Grid (GGG) is to replace WWW, the proliferation of grid computing is clearly foreseeable [23].

The grid computing literature has covered a wide range of research issues from the context of the commercialized grid services to the internal provision of grid computing services. However, all research efforts in network resource pricing of grid are focused on the service provider's problem — how to price their computing services. The client side problem has not been well tackled. When a grid computing network is no longer freely accessible and each server charges users a differentiated price according to the requested service quality, in either social welfare maximization or profit maximization context, users will inevitably face an optimization problem: how to properly choose service priorities for each of their grid computing subtasks in a computing job, so that the total cost with regard to the price at each server and the cost due to the overall throughput delay will be minimized.

This paper is intended to tackle the user-side problem of how to optimize service priority selections in submitting a multi-subtask job to the computational grid with multi-priority services at different prices, and make theoretical contribution with the setup of multi-priority pricing system. First, we review the related literature in grid computing. Second, we conceptualize a prioritized CPM model for the problem, and identify it as a time– cost tradeoff problem. Third, we propose a locally costeffective critical path approach to solve the problem. Fourth, we propose a heuristic algorithm, Non-critical Path Relaxation algorithm, for refining the priorities on the non-critical paths corresponding to a given critical path. Finally, we discuss the implication of this user-side problem research on solving the server-side optimum pricing problem.

## 2. Related background literature

The notion of “making money on the Internet” triggered the gold rush in the cyber world a decade ago; today, the dream of “making money on the grid network” is generating a similar kind of interest and. By operating paid grid computing services, grid service providers will be able to refuel their businesses and improve services by reinvesting the profits to more advanced grid technology, which will further benefit grid network users with better values. The propensity will make the high-performance grid computing services, including CPUs, software, databases, and other hardware, into commodities; and a new Internet-based electronic market, a grid computing market, will emerge. The commoditization of grid computing services and components will eventually embrace the advent of the grid computing economy [18]. Realizing this trend, many in the academic area have started to research the issues in commercializing grid computing in the late 1990s. For example, Buyya and Vazhkudai [3] proposed the model of Compute Power Market, which utilizes a resource management and job scheduling system for Internet-based grid computing; Wolski et al. [25] raised the concept of G-commerce – the electronic commerce for computing resource owners to sell their resources in the computational grid. The key point in these ideas lies in resource allocation – how to efficiently allocate computing resources on the Internetbased market with the economic mechanism [10,19].

The same idea is applicable to the nonprofit-oriented grid services, including those provided by organizations to the internal users and those provided by non-profit organizations on the Internet to the public. Internet and intranet service providers have been looking for ways to improve quality-of-service (QoS) [4,8,9,13]. When the utilization of the grid outgrows its capacity, it will inevitably encounter the QoS problem in servicing large volume of requests — the same issue that the Internet has been struggling with. The problem in grid computing services in an organization is not only inherited from that of the overexploited network bandwidth, but is also caused by the excessive demand for the services of CPU, data resources, and other networked instruments. This is also a typical public good problem, referring to the one in the commodity market, where free riders overexploit the public services without any costs [13]. The resulted congestion will finally wear away the benefits from grid computing.

In the last several decades, great efforts in the engineering approach have been made for the performance of shared computing resources, such as processor sharing research (e.g. Ref. [2]), and network bandwidth and QoS improvement (e.g. Refs. [8,9]). However, the problems such as those in Internet congestion control still remain [21]. Since the early 1990s, increasing research has been conducted in economic network resource allocation mechanisms that support usage-based pricing with incentive compatibility. It has been revealed that previous pure engineering approaches are insufficient for solving the public good problem, in which the freely available computing resources will always lead to inefficiency of the resource allocation due to the lack of an incentive compatible mechanism [4]. In 1997, Gupta et al. [11] proposed a network traffic pricing model based on first-infirst-out (FIFO) bandwidth service scheme; and later, Lin et al. [20] derived an optimum pricing model for packetswitched networks using round-robin bandwidth service scheme. Both models assume that a benevolent social planner sets up optimum prices for computing services in order to maximize social welfare of the digital economy. The theoretical outcomes have been well supported by experimental results.

In both contexts mentioned above – the commerciaized grid services or internal provision of grid computing services – pricing the services will become a final resolution to the public good problem [3,13]. Since theoretical research has presented convincing results, recent research focus of network resource pricing is shifting toward the implementation of the resource pricing mechanism. Based on the idea of Compute Power Market, a broker-based architecture for the serviceoriented grid computing system, Nimrod-G, has been conceived [1]. Nimrod-G manages all operations associated with remote execution for user-defined QoS requirements by employing a resource broker for scheduling parametric computations on the resources spanning five continents. For organizational network resource management, an implementation scheme of intranet resource pricing system named iRUM has been proposed [12]. iRUM manages service requests using a dynamic priority pricing approach in order to maximize the service social welfare of the network. Targeted at the grid computing network, the technical details for implementation of resource pricing system based on a web services environment have been explored [21], in which implementation issues of the pricing system with heterogeneous computing services are addressed. These efforts are paving the way to the eventual implementation of a resource pricing system for a grid computing network.

To complement the literature that focus primarily on the server-side problems, we approach the user-side problem with the assumption of a multi-priority pricing system, where each node on the grid offers different levels of service priorities at different prices. We target the problem of how to properly choose service priorities for each of their grid computing subtasks in a computing job, so that the total cost with regard to the price at each node and the cost incurred by the overall throughput delay will be minimized. Due to the NP-hard nature of the problem, the scope of this paper will be limited to the discussion of a heuristic solution for the critical path problem in a prioritized critical path method (CPM) network and the adjustment of the priorities on the noncritical path nodes.

## 3. Problem conceptualization

Consider a grid network with multi-priority computing services that include CPU, bandwidth, data access, software and other hardware sharing. We conceptualize all these services into logical servers, where users can submit computing jobs that are divided into multiple subtasks, and pay for the services at the chosen priorities. A computing job is consisted of segments, which are referred to as subtasks in this paper. Some of these subtasks are parallel, meaning they are without interdependencies, hence can be executed simultaneously. Some other subtasks must be run sequentially, because, for example, the output of one subtask is the input of another. The nature of parallelization among certain number of subtasks is necessary for successful job submission into a grid system; otherwise, the computing job can just be processed sequentially on one machine. We let there be as many logical servers as there are subtasks; so that each subtask can be represented by a logical server, while certain physical servers will be accessed more than once. Thus, we assume that the number of physical servers is large enough to accommodate the number of subtasks that need to be run simultaneously at any given time, so that the waiting time for an available physical server is negligible.

Further, services of different priorities are dynamically priced in accordance with their usage load — the higher the load, the higher the price. In the steady state, each logical server is able to provide the expected throughput time of any subtask at each service priority. We assume that the expected throughput times and the corresponding prices at different priority levels are available to the users, who can then choose priority levels for the subtasks at different logic servers based on urgency of the subtasks relative to the completion of the job, and the value of the subtasks to the users. The higher priority costs more, but has a shorter throughput time, which yields a lower delay cost. The objective of this problem is to select the optimum priority for the service at each logic server, so that the total cost, including the costs incurred from the overall throughput time and the services at each node, can be minimized. If a subtask is extremely sensitive to service delay, the highest priority should be chosen for it, and vice versa. But, in many situations a user can choose a moderate priority that does not cost too much but the throughput time is short enough to minimize costs.

The parallelization and the dependencies of the subtasks can be characterized by an acyclic directed graph, where each node is a subtask and the connecting arrows show the dependencies between the subtasks. The logical servers representing to the subtasks form a grid network with multi-priority service levels, which can be conceptualized into a prioritized CPM network [15]: At each node of the network, there are several service priorities, each of which is associated with an expected service throughput time and a service cost. Thus, given a service priority at each node, there exists a critical path — a series of nodes that constitute the longest path in terms of throughput time from the starting node to the end node. Binding to this critical path, the throughput time of all non-critical paths – the series of nodes connected one after another, where the start node and the end node of this path are the only ones on the critical path – have no effect on the total throughput time of the task as long as they are within the length restriction of the corresponding portions of the critical path.

There are three possible situations where the priorities of nodes could be further optimized from any arbitrarily configured CPM network, in which the service priority of each node has been selected, and consequently the critical path can be identified:

1) if the priority of a node on a non-critical path can be lowered and the resulting throughput time of that non-critical path is still within the length restriction of the corresponding section of the critical path;

2) if the priority of a node on the critical path can be lowered and the cost of the increased overall throughput time is less than the cost reduction from lowering the priorities on the critical path and possibly on the affected non-critical paths; and

3) if an alternative critical path obtained by changing priorities at some nodes can provide a better solution with a lower total cost.

As a combination of priority selections is associated with service costs and total throughput time, the above problem falls under the time–cost tradeoff problem category [5,7,14,24]. Therefore, we can formulate the grid computing priority selection problem by following the formulation of the time–cost tradeoff problem by De et al. [6] in conjunction with the special characteristics of our problem.

A prioritized CPM network characterizing the dependencies and the throughput times of the subtasks can be represented in the AON (activity-on-node) form [15]. The starting node and the end node, b and e respectively, are symbolic with throughput time $0 ;$ the other nodes have non-zero throughput times, denoted by the set M. Each node represents a subtask to be processed by a logical server; and the arcs indicate the sequence in which the subtasks are processed. Then, this CPM network, which is also essentially an acyclic directed graph, can be denoted as $G = ( V , E )$ , consisting of nodes $V = \{ b , e \} \cup M ,$ and an arc set $E = \{ ( x , y )$ | there is an arc from node x to y, and $x , y \in V { \big . }$ . For every node $m \in M ,$ $K _ { m }$ is the set of service priority levels at $m , H _ { m }$ is a set of pairs: $\{ ( p _ { k } ^ { m } , t _ { k } ^ { m } ) \mid k \in K _ { m } \}$ , where $p _ { k } ^ { m }$ is service price at priority k, and $t _ { k } ^ { m }$ is service throughput time at priority k. The number of priority levels at a node is $| K _ { m } |$

Regarding the setting of the priority levels at each node, we assume that the greater the $k ,$ the lower the priority of the service. So, k = 1 is the highest possible priority, and $k { = } | K _ { m } |$ is the lowest priority at node m. A given subtask at any node m with priority $k \in K _ { m } ,$ , is associated to a pair $( t _ { k } ^ { m } , p _ { k } ^ { m } ) \in H _ { m }$ . If each unit service delay will incur a cost c to the user, the expected cost with service priority $k$ at node m can be expressed as $C _ { m } { = } c ~ t _ { k } ^ { m } { + } p _ { k } ^ { m }$ , when the delay at node m impacts the overall throughput time (i.e. node m is on the critical path), and $C _ { m } { = } p _ { k } ^ { m }$ , if node m is on the non-critical path. Fig. 1 illustrates the relationship between cost and priority for three typical types of subtasks.

Denote $\Theta = \times _ { m \in M } K _ { m }$ as the product set containing all possible combinations of priority selections for the nodes in the prioritized CPM network G. Let $\sigma \in \Theta$ be a configuration of the network with the selection of a particular priority for each activity node. So, the priority at a given node m can be written as $\sigma _ { m } ,$ which can also be presented as $k ( \sigma , m )$ . Denote a path between nodes x and y as $P _ { ( x , y ) } { = } ( x , y ; P )$ , where $P \subset M ,$ is the set of nodes on that path between x and $y ,$ and does not include nodes x and $y ;$ and use $\Omega _ { ( x , y ) } ^ { M } = \{ { \cal P } _ { ( x , y ) } \}$ to represent the set of all possible paths between nodes x and y. Thus, the optimality problem of prioritized CPM network can be formalized as solving for a set of optimal priorities $\sigma ^ { * } \in \Theta$ , with the resulting critical path $P _ { ( b , e ) } ^ { * } ( \sigma ^ { * } ) { = } ( b , ~ e ; ~ P ^ { * } ( \sigma ^ { * } ) ) { \in } { \varOmega ^ { M } } _ { ( b , e ) }$ with properly selected priority for each node, such that the total cost, including the delay cost and the price paid for the service at each node, is minimized.

Let $T ( \sigma )$ and C(σ) be the overall time and cost for the configuration $\sigma .$ . The traditional time–cost tradeoff problem with the budget constraint is to minimize the total time with a cost constraint $B \colon$

Find $\sigma ^ { t | c }$ such that $\begin{array} { r } { T ( \sigma ^ { t | c } ) = \operatorname* { m i n } _ { \sigma \in \Theta } ~ \{ T ( \sigma ) : C ( \sigma ) { \leq } B \} } \end{array}$

<sup>ð Þ ¼ f ð Þ ð Þ g</sup>The version with the deadline constraint is to minimize the total cost given a due time $D \colon$

Find $\sigma ^ { c | t }$ such that $\begin{array} { r } { C ( \sigma ^ { c | t } ) = \operatorname* { m i n } _ { \sigma \in \Theta } ~ \{ C ( \sigma ) : T ( \sigma ) { \le } D \} } \end{array}$

The above two problems were proved to be NP-hard

[7] and have attracted decades of research effort in finding feasible algorithms. For example, Meyer and Shaffer [22], and Crowston [5] have presented their solutions in the mixed integer linear programming approach; Harvey and Patterson [14] combine the planning, scheduling, and control stages of solving process in order to consider different alternatives provided for each node and different resulting costs. In 1995, De et al. [6] provide a good survey of several approaches to the discrete time–cost tradeoff problem and some network reduction algorithms used in the approaches for problem solving and complexity analysis.

![](/api/attachments/Z4SPTJAR/fulltext/images/5c2cb85e344944ea9ac25a93e3c16930c7c0d1e5f6a2be6cf1127fb05a590ec7.jpg)  
Fig. 1. The optimum service priority for different types of service request at node m (the smaller k, the higher the priority).

A recent research work by Skutella [24] is worth detailing. Skutella approaches the problem by first constructing a linear relaxation of the problem, then finding the solution of the linear problem, and rounding the linear solution to yield the final solution. It is the first approximation algorithm for discrete time–cost tradeoff problem, and a solution within a certain factor α of the optimal solution can be obtained. Furthermore, Skutella points out that a problem with a single budget or deadline restriction may not be practical at all times, and that the performance guarantee for the approximation algorithm is somewhat weak. Thus, bicriteria approximation algorithms are presented for solving an integer programming problem – whose setup is slightly different from the budget or the deadline problem – with tolerances for time and budget at the same time.

The prioritized CPM problem for the grid computing network services is the same as that of the traditional time–cost tradeoff problem, since at each node the higher priority has a shorter throughput time and a higher price. However, in our problem C(σ) also includes a positive delay cost for the total throughput time, representing user's value of time, while in the traditional problem the throughput time is not counted as cost but just a constraint. The total delay cost for a grid computing job is only affected by the length of the critical path, or the total throughput time. Therefore, when a critical path is determined, no extra delay cost will incur if the priorities on the nodes of the non-critical paths are lowered in accordance to the time constraints set by the corresponding sections of the critical path. Since the cost at each node on the critical path is expressed in $c ^ { * } t _ { k } { ^ { + } p } _ { k } ,$ where throughput time $t _ { k }$ is negatively correlated to service price $p _ { k }$ regarding priority $k ,$ it is not always a strictly decreasing function of priority. Thus, the optimal priority of a node in our problem is conditionally determined by a specific user's unit delay cost and the problem with no time constraints is non-trivial compared to the traditional problem.

We tackle the prioritized CPM network problem with a heuristic approach implemented in two steps: solving a locally cost-effective critical path (to be covered in Section 4), and refining node priority selections on noncritical paths after the locally cost-effective critical path is determined (to be covered in Section 5).

## 4. The cost-effective critical-path approach

## 4.1. Arc reduction

Before we proceed to the cost-effective critical path approach, it is a good practice to reduce the graph to its simplest form, if it is not already so. As Fig. 2 shows, if there is more than one path between nodes $x _ { 1 }$ and $x _ { n } ,$ arc $( x _ { 1 } , x _ { n } )$ can be reduced. This is because the throughput time for the path of nodes $x _ { 1 } , x _ { 2 } , . . . ,$ and $x _ { n }$ is always greater than the length of the direct path between node $x _ { 1 }$ and $x _ { n } .$ . Arc reduction can significantly reduce the number of paths. In terms of subtasks of a computing job, this reduction can be understood as follows: $x _ { n }$ needs input from $x _ { n - 1 }$ as well as $x _ { 1 }$ in order to start processing; in the same time, the output of $x _ { I }$ is needed by $x _ { 2 } ,$ , whose output is then needed by the following node and eventually connecting to $x _ { n - 1 } ; \mathrm { S o } .$ , instead of passing from $x _ { 1 }$ to $x _ { n }$ directly, it is equivalent for the output of $x _ { 1 }$ to be passed to $x _ { n }$ through the nodes $x _ { 2 }$ to $x _ { n - 1 }$ eliminating an extra connection.

## 4.2. An integer programming model

After arc reduction, we can formulate the prioritized CPM problem in grid computing priority selection. Denoting the total throughput time from the start node $b$ to any node x as $T _ { x } ,$ , we have the following model in the integer programming form:

$$
\min C = \sum_ {m \in M} \sum_ {k \in K _ {m}} p _ {k} ^ {m} \cdot x _ {k} ^ {m} + c \cdot T _ {e}\tag{1}
$$

Subject to the following constraints:

$$
\begin{array}{l} \bullet \sum_ {k \in K _ {m}} x _ {k} ^ {m} = 1, \forall m \in M, \text { where } x _ {k} ^ {m} \in \{0, 1 \} \forall m \in M, k \in K _ {m}; \\ \bullet T _ {b} = 0; \\ \bullet T _ {j} \geq T _ {i} + \sum_ {k \in K _ {i}} t _ {k} ^ {j} \cdot x _ {k} ^ {j}, \quad \forall j \in V \setminus \{b \}, \quad (i, j) \in E. \end{array}
$$

Due to the complexity added by the number of priorities at each node, the above problem is impractical to solve when the grid is large. Therefore, we propose a cost-effective critical path approach for modeling the priority selection problem in grid network services. We will show that this approach can lead to an efficient algorithm that is feasible to yield a heuristic solution.

## 4.3. Globally cost-effective critical path (GCCP)

Definition 1. Globally cost-effective critical path (GCCP), denoted as $P _ { ( b , e ) } ^ { * } ( \sigma _ { G } ^ { * } ) = ( b , e ; P ^ { * } ( \sigma _ { G } ^ { * } ) ) \in P _ { ( b , e ) } ^ { M } ,$ is a critical path in the grid network, in which $\boldsymbol { \sigma } _ { G } ^ { * }$ specifies the optimal configuration of the priority of each node in $M ,$ such that total cost of service is minimized.

If a user can identify the set of nodes in the GCCP $P _ { ( b , e ) } ^ { * } ( \sigma _ { G } ^ { * } )$ for his job, he can apply the time constraints preset by the GCCP to solve for the optimum $k _ { m }$ in the nodes of the non-critical paths by minimizing $p _ { k } ^ { m }$ as long as the resulting lengths of the non-critical paths are within the constraints set by the corresponding sections of the GCCP. Accordingly, we define a noncritical path as a series of nodes connected one after another, where the start node and the end node are the only ones on the GCCP. In our notations, we distinguish the non-critical paths from the critical path, by denoting a non-critical path as $N _ { ( x , ~ y ) } { = } ( x , ~ y ; ~ N )$ associated to a section of the critical path $R _ { ( x , y ) } ^ { * } ( \sigma _ { G } ^ { * } ) =$ (x, y; $R ^ { * } ( \sigma _ { G } ^ { * } ) )$ such that $R ^ { * } ( \sigma _ { G } ^ { * } ) \subseteq P ^ { * } ( \sigma _ { G } ^ { * } )$ , and N∩ $R ^ { * } ( \sigma _ { G } ^ { * } ) { = } \emptyset$ . Thus, the user's cost minimization problem can be alternatively defined as the following with regard to the GCCP:

$$
\min _ {\sigma \in \Theta} C = \min _ {\sigma \in \Theta} \left[ \sum_ {s \in P ^ {*} (\sigma)} \left(c t _ {k (\sigma , s)} ^ {s} + p _ {k (\sigma , s)} ^ {s}\right) + \sum_ {m \in M \backslash P ^ {*} (\sigma)} p _ {k (\sigma , m)} ^ {m} \right]\tag{2}
$$

$\mathrm { s . t . } \sum _ { n \in N } t _ { k ( \sigma , n ) } ^ { n } \le \sum _ { s \in R ^ { * } ( \sigma ) } t _ { k ( \sigma , s ) } ^ { s }$ for every non-critical path $N _ { ( x , \ y ) } { = } ( x , y ; N )$ <sup>ð Þ</sup>associated to $R _ { ( x , y ) } ^ { * } ( \sigma ) { = } ( x , y ; R ^ { * } ( \sigma ) )$ with nodes $x , y \in P _ { ( b , e ) } ^ { * } ( \sigma )$

The solution based on the GCCP is the configuration $\sigma _ { G } ^ { * } \in \Theta$ , such that $\boldsymbol { \sigma } _ { G } ^ { * }$ minimizes the total cost of the prioritized CPM network with the GCCP.

## 4.4. Locally cost-effective critical path (LCCP)

Definition 2. A locally cost-effective CPM network is the configuration $\sigma _ { L } ^ { o }$ that contains the locally optimized priorities that minimize the cost at each node:

$$
\forall m \quad k (\sigma_ {L} ^ {o}, m) = \operatorname{argmin} _ {k \in K _ {m}} (c t _ {k} ^ {m} + p _ {k} ^ {m}).
$$

Definition 3. A locally minimized cost expressed as $C _ { m } ^ { * } { = } c t _ { k ( \sigma _ { L } ^ { o } } ^ { m } , \mathbf { \Sigma } _ { m ) } { + } p _ { k ( \sigma _ { L } ^ { o } } ^ { m } , \mathbf { \Sigma } _ { m ) }$ is the service cost at node m with the locally optimal priority $k ( \sigma _ { L } ^ { o } , m )$ .

![](/api/attachments/Z4SPTJAR/fulltext/images/849a3868e28429950863a8ecb6210f92889c9c0b471d035863cdd8dc808af9f4.jpg)  
Fig. 2. Arc reduction.

Definition 4. The critical path of a locally cost-effective CPM network is called locally cost-effective critical path (LCCP) and denoted as $P _ { ( b , e ) } ^ { * } ( \sigma _ { L } ^ { o } ) { = } ( b , e ; P ^ { * } ( \sigma _ { L } ^ { o } ) )$

We denote $\sigma _ { L } ^ { P } { = } ( k ( \sigma _ { L } ^ { o } , \ s ) \ \mid \ s \in P _ { ( b , e ) } ^ { * } ( \sigma _ { L } ^ { o } ) )$ as the configuration of the nodes on the LCCP, Note that LCCP is not necessarily equivalent to GCCP. So the solution based on LCCP is,

$$
\begin{array}{c} \min C \\ \sigma^ {\prime} \in \Theta (M \backslash P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {o})) \end{array} = \sum_ {s \in P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {o})} \left(c t _ {k (\sigma_ {L} ^ {o}, s)} ^ {s} + p _ {k (\sigma_ {L} ^ {o}, s)} ^ {s}\right) + \min _ {\sigma^ {\prime} \in \Theta (M \backslash P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {o}))} \left(\sum_ {m \in M \backslash P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {o})} p _ {k (\sigma^ {\prime}, m)} ^ {m}\right)\tag{3}
$$

s.t. $\sum _ { n \in N } t _ { k } ^ { n } \le \sum _ { s \in P } t _ { k } ^ { s } \sum _ { n \in N } t _ { k ( \sigma ^ { \prime } , n ) } ^ { n } \le \sum _ { s \in R _ { ( x , v ) } ^ { * } ( \sigma _ { L } ^ { o } ) } t _ { k ( \sigma _ { L } ^ { o } , s ) } ^ { s }$ for every non-critical path $N _ { ( x , y ) }$ <sup>ð Þ</sup>associated to $R _ { ( x , y ) } ^ { * } ( \sigma _ { L } ^ { o } ) { = } ( x , y ;$ $R ( \sigma _ { L } ^ { o } ) ) ^ { * }$ with node $x , \overset { \cdot } { y } { \in } P _ { ( b , e ) } ^ { * } ( ( \sigma _ { L } ^ { o } ) )$

Let $\sigma _ { \ L } ^ { * } { = } ( \sigma _ { L } ^ { P } , \sigma ^ { \prime } { ^ * } )$ be the optimal configuration for all nodes after lowering the priority of nodes on the noncritical paths within the time constraints set by the LCCP.

The total throughput time of configuration $\sigma _ { L } ^ { * }$ is the sum of the throughput time of the nodes in $P _ { ( b , e ) } ^ { * } ( \sigma _ { L } ^ { o } )$ Let us denote the total throughput time as,

$$
T (\sigma_ {L} ^ {*}) = \sum_ {m \in P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {*})} t _ {k (\sigma_ {L} ^ {*}, m)} ^ {m} = \sum_ {m \in P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {P})} t _ {k (\sigma_ {L} ^ {P}, m)} ^ {m}.
$$

And the total cost of the configuration $\sigma _ { L } ^ { * }$ is,

$$
\begin{array}{l} C (\sigma_ {L} ^ {*}) = \sum_ {m \in P _ {(b, e)} ^ {*} (\sigma_ {L} ^ {P})} \Big (c t _ {k (\sigma_ {L} ^ {P}, m)} ^ {m} + p _ {k (\sigma_ {L} ^ {P}, m)} ^ {m} \Big) \\ \quad + \sum_ {m \in M \setminus P _ {(b, e)} ^ {*} (\sigma^ {\prime} *)} p _ {k (\sigma^ {\prime} *, m)} ^ {m}. \end{array}
$$

For the simplicity of notations, let $P _ { G } ^ { * } { = } P _ { ( b , e ) } ^ { * } ( \sigma _ { G } ^ { * } )$ 4 and let $P _ { L } ^ { * } { = } P _ { ( b , e ) } ^ { * } ( \sigma _ { L } ^ { * } )$

Proposition. Given any prioritized CPM network, the priority of each node in the optimum configuration based on the GCCP is not higher than the locally optimized priority.

Proof. For a node $m \in { \cal P } _ { G } ^ { * } \backslash \{ b , e \}$ on the GCCP, let $k _ { m }$ be the priority that is higher than the locally optimized priority. By lowering $k _ { m }$ to the locally optimized priority, the total cost of the resulting configuration will be lower, by the definition of locally optimized priority and possible further lowering of priorities of the non-critical path nodes. This is contradictory to the definition of GCCP. Therefore, the priorities of the nodes on $P _ { G } ^ { * }$ cannot be higher than the locally optimized priorities. □

According to the above proposition, we can further derive that when the GCCP overlaps a LCCP, the throughput time of the critical path of the GCCP is not shorter than that of LCCP.

However, when $P _ { L } ^ { * } \backslash \{ b , e \} \neq P _ { \ G } ^ { * } \backslash \{ b , e \}$ , it is possible that the throughput time of LCCP is longer than the throughput time of GCCP. For example, in Fig. 3, node A is on LCCP and has a longer locally cost minimized throughput time than that of node $B ;$ by raising the priority of $A ,$ the path $P _ { \mathrm { s h o r t } }$ via $B$ may become critical path, while B maintains its locally optimized priority. Let the cost increase from raising As priority be $c _ { A } ,$ , and cost decrease from reducing throughput time in the new critical path $P _ { \mathrm { s h o r t } }$ be $c _ { B } . \operatorname { I f } c _ { B } > c _ { A } ,$ , the new configuration with critical path $P _ { \mathrm { s h o r t } }$ has a shorter throughput time and a lower cost. Since there may exist a parameter setting for the CPM network, with which we can find a configuration to make $P _ { \mathrm { s h o r t } }$ the GCCP, then the throughput time of the GCCP is shorter than that of LCCP.

Identifying the upper and lower bound of an objective is one of the important focuses in optimization problems. The above discussion demonstrates that throughput time of LCCP can be the lower bound for the throughput time of GCCP, when $P _ { L } ^ { * } \{ b , e \} = P _ { G } ^ { * } \backslash \{ b , e \}$ , and that in general, the locally cost-effective configuration for the prioritized CPM network provides the lower bound for the throughput time of GCCP at each node. This consequently narrows down the search range for the GCCP.

## 4.5. Time complexity of solving LCCP

Denote the time complexity of the algorithm for solving traditional CPM problem as $T _ { 0 } ( n ) { = } O ( f ( n ) )$ , where $n { = } | M |$ is the number of nodes. Using brute-force approach, the time complexity is $T _ { \cal G } ( n ) = \prod _ { m \in { \cal M } } \vert K _ { m } \vert ^ { * }$ $O ( f ( n ) ) = O ( K _ { \operatorname* { m a x } } ^ { N } ) ^ { * } O ( f ( n ) ) , = O ( K _ { \operatorname* { m a x } } ^ { N } { } ^ { * } f ( n ) )$ ; where

![](/api/attachments/Z4SPTJAR/fulltext/images/828008f4b39bb55e5660a69f9169b350fd0aa3cc3eb835badc8a94e45a2e0609.jpg)  
Fig. 3. A counter case in which a more optimal configuration has a critical path shorter than LCCP.

$K _ { \mathrm { m a x } } = \mathrm { m a x } _ { m \in M } \{ | K _ { m } | \}$ : So, $T _ { G } ( n )$ falls under the exponential category. Similarly, the time complexity of the LCCP-based heuristic approach is,

$$
\begin{array}{l} T _ {L} (n) = \sum_ {m \in M} | K _ {m} | + T _ {0} (f (n)) \\ = O (n * K _ {\text { Max }}) + T _ {0} (f (n)) \\ = O (\max \{n * K _ {\text { Max }}, f (n) \}) \end{array}
$$

The computational complexity of our approach for solving LCCP is then derived to be $O ( f ( n ) )$ , because the linear form of $n ^ { * } K _ { \operatorname { M a x } }$ has the lowest complexity.

## 5. Non-critical Path Relaxation (NPR) algorithm

The locally cost-effective CPM network configuration achieved after simplifying the graph, configuring locally cost-effective CPM network, and identifying the LCCP may provide an acceptable heuristic solution with a much lower computational complexity compared to the optimization based on the GCCP. However, the non-critical paths may be at higher priorities than necessary — in other words, the time constraint set by the critical path may allow the priorities of the nodes on the non-critical paths to be further lowered. Speaking in terms of subtasks of a computing job, once the bottleneck is identified, the other subtasks can be processed at a slower rate to reduce cost, as long as it does not exceed the bottleneck time constraint. In this section, we propose a priority refining algorithm, Non-critical Path Relaxation (NPR) algorithm that can further improve the optimality of the solution and reduce the total cost of the nodes on the non-critical paths. The refinement of priority levels consists of two steps: 1) find all noncritical paths associated to the LCCP, and 2) reduce the costs of the services on these non-critical paths using Non-critical Path Relaxation (NPR) algorithm.

## 5.1. Solving all non-critical paths

Given an LCCP $P _ { L } ^ { * } { = } P _ { ( b , e ) } ^ { * } ( \sigma _ { L } ^ { * } )$ , we denote a noncritical path as $N _ { ( x , y ) } { = } ( x , y ; N ) ,$ , where $x , y \in P _ { L } ^ { * }$ are the only nodes of $N _ { ( x , y ) }$ that are on the critical path, thus $N \subseteq M \setminus \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$ . For any $N _ { ( x , y ) } , ( x , y ) \notin E ;$ otherwise, the arc between x and y can be reduced (see Fig. 2). Searching for non-critical paths can start from a node in $P _ { L } ^ { * }$ , using either forward or backward depth-first search. A non-critical path is found when the search reaches another node in $P _ { L } ^ { * }$ If the number of nodes in $P _ { L } ^ { * }$ is $n ,$ the maximum combination of nodes as the start and end nodes of all possible non-critical paths is $( n - 1 ) ( n - 2 ) / 2$ Let the total number of nodes in the prioritized CPM network be $| M | ,$ the maximum number of nodes on a path is $J ,$ and the number out-going arcs from a node is arbitrary, we can derive that the total number of paths between $( b , e )$ is less than $\left| M \right| ^ { J }$ . From an alternative view point, the presence of LCCP in the graph splits some of paths between $( b , e )$ into shorter segments that turns into the non-critical paths. If the number of nodes on the LCCP is bounded, it will not change the complexity of the number of non-critical paths. Thus, in general, the complexity in finding the number of non-critical paths with regard to the number of nodes is $T _ { N } ( | M | ) { = } O ( | M | ^ { J } )$

## 5.2. NPR algorithm

Before delving into the algorithm of optimizing each unit type, it is necessary to specify the quantity associated with each node. For any node s not on LCCP $P _ { L } ^ { * } , \mathrm { i . e . } s \in M \setminus \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$ , let $U _ { s } = \{ N ^ { s } { } _ { ( x , y ) } = ( x , y ;$ $N ^ { s } ) | x , y \in P _ { L } ^ { * }$ and $s \in N ^ { s } \}$ be the set of non-critical paths containing node $s ,$ and start and end at any two nodes x and y on the critical path; let $D _ { u }$ be the throughput time of any non-critical path $u = N ^ { s } { } _ { ( x , y ) } \in U _ { s } ,$ , and $T _ { u }$ be the throughput time of the section on the critical path that is between the same beginning node and end node of $N _ { ( x , y ) } ^ { s }$ inclusively. We can define an allowable relaxation with regard to each node $s \in M \backslash \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$ } as,

$$
A R _ {s} = \min _ {u \in U _ {s}} (T _ {u} - D _ {u})
$$

It is also necessary to have a quantity indicating the rate of savings in cost with respect to increase in time from a higher priority to a lower one for every node only on the non-critical paths. So, we construct $B _ { s }$ as a set of such payoffs for node $s \in M \backslash \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$

$$
B _ {s} = \left\{\left(d _ {i} ^ {s}, r _ {i} ^ {s}\right) \right\},
$$

where $\begin{array} { r } { d _ { i } ^ { s } = t _ { i } ^ { s } - t _ { k _ { s } } ^ { s } , r _ { i } ^ { s } = \frac { p _ { k _ { s } } ^ { s } - p _ { i } ^ { s } } { t _ { i } ^ { s } - t _ { k _ { s } } ^ { s } } , k _ { s } < i \leq | K _ { s } | } \end{array}$ ; and $k _ { s }$ is the locally optimized priority that locally minimizes the cost at node s for the subtask.

The optimization procedures are as follows:

1. $\forall s \in M \backslash P _ { L } ^ { * } \backslash \{ b , e \} \}$ find the priority level $k ^ { * } ( \mathrm { o f } s )$ for $B _ { s } = \{ ( d _ { i } ^ { s } , r _ { i } ^ { s } ) \}$ such that $s _ { k ^ { * 1 \mathrm { S } } } ^ { s }$ the maximum subject to $d _ { k } ^ { s } * \leq A R _ { s } .$ . If all $\boldsymbol { d } _ { i } ^ { s }$ in a $B _ { s }$ are greater than $A R _ { s } ,$ , then remove node s from S because its priority level cannot be lower.

2. Find node $h = \arg \operatorname* { m a x } _ { s \in M \backslash P } * \{ r _ { k } ^ { s } * \}$

3. Let $k _ { h } = k ^ { * }$ <sup>L</sup>to update the priority of node $h ,$ at which $r _ { k } ^ { h * }$ becomes the optimum.

4. $\forall u \in U _ { h } ,$ recalculate the throughput time $D _ { u }$ of the affected non-critical paths

5. Remove node h from set $M \backslash \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$

6. If $M \backslash \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$ } is empty, exit. Otherwise, proceed.

7. $\forall s \in M \backslash \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$ , recalculate $A R _ { s } = \operatorname* { m i n } _ { u \in U _ { e } } \left( T _ { u } – D _ { u } \right)$ 8. $\forall s \in M \backslash \{ P _ { L } ^ { * } \backslash \{ b , e \} \}$ , recalculate $B _ { s } = \{ ( d _ { i } ^ { s } , \bar { r } _ { i } ^ { s } ) \}$ 9. Go to step 1.

## 5.3. Computational complexity of the NPR algorithm

If $n { = } | M |$ is the total number of nodes, the computational complexity for each allowable relaxation calculation referring to a node is $T _ { A R } ( n ) { = } T _ { P } ( n ) { ^ { * } O } ( n ^ { 2 } )$ 5 where $T _ { P } ( n )$ is the complexity of the number of noncritical paths that pass the node with the same starting and ending nodes, and $O ( n ^ { 2 } )$ is the complexity of the number of critical path node pairs associated to the noncritical paths passing the node. Then the overall complexity of the algorithm can be derived as $T ( n ) { = } T _ { A R } ( n ) ^ { * } O$ $\mathrm { \bar { ( } } n ) { = } \dot { T } _ { P } ( n ) { ^ { * } O } ( \bar { n ^ { 3 } } ) , \forall s { \in } M \ \backslash \ \{ P x _ { L } ^ { * } \} \ \{ b , e \} \}$

The estimate of $T _ { P } ( n )$ is subject to different assumptions with regard to the number of arcs associated to a node and the number of nodes on the critical path. Generally, if the number of nodes in a non-critical path is arbitrary, we can show that $T _ { P } ( n )$ is exponential. First, let us check the maximum number of paths passing a node in a directed graph with n nodes between a start node and an end node. Suppose the nodes are divided into k groups each having x nodes, and the arcs from the nodes in one group directly link to the nodes in the next group without going to the third group because applying the Arc Reduction rule can effectively eliminate any shortcut among the groups (as shown in Fig. 2). Then by maximizing $x ^ { \check { k } } ,$ s.t. $x ^ { k } = n$ , we obtain $x = \mathbf { e } = 2 . 7 I 8 2 8$ , and $k { = } n / \mathrm { e }$ . The complexity of the number of paths in this situation is $O ( \mathrm { e } ^ { n / \mathrm { e } } )$ . In this way we can derive that the complexity of the number of non-critical paths that pass a given non-critical path node could be as bad as exponential when the number of nodes in any non-critical path is not constrained.

In practice, the number of nodes in a path in a grid computing network is bounded. The computational complexity of the NPR algorithm is then reduced. Following the same approach to the complexity analysis for solving LCCP non-critical paths, we can derive that $T _ { P } ( n ) { = } O ( n ^ { J - 1 } )$ when the number of nodes in any noncritical path is bounded by a constant J (excluding the two nodes in the critical path).

In summary, the LCCP-based heuristic approach for solving the prioritized CPM network can be characterized by the following steps:

1. Simplify the graph using the arc reduction technique.

2. Configure locally cost-effective CPM network.

3. Identify the LCCP.

4. Identify all non-critical paths associated to the LCCP.

5. Refine the priority levels of the nodes on these noncritical paths to further reduce total cost and improve the heuristic solution.

## 6. Implications of user's choice on grid network service pricing

The proposed cost-effective critical path approach for user-side decision making problem presented in previous sections has an important implication on the network resource pricing problem on the service provider side: it is difficult to price grid computing services optimally because of the complexity of the user-side optimization problem. This further implies that the general stochastic equilibrium defined by Gupta et al. [11] between users and service providers may not exist when they choose different optimization objectives.

The complexity of the decision-making in service priority selections in the grid network makes its resource pricing more difficult than that for linear network resource management problems, such as the network bandwidth pricing problem [11,20]. This is because of the externalities among different paths and the heterogeneity of priority selections for the nodes on the paths with different criticalities. Let us consider a typical grid computing economy involving rational users and service providers. A user submits a job consisting of multiple subtasks to the grid network only when the value of the job is greater than the total cost including the computing service costs and delay costs, as expressed in formula (2). We notice that a decision in submitting a job regarding service price levels on the critical path also affects subtask arrivals at the servers on the non-critical paths in the grid network. This makes the problem more complicated in comparison with the service in a single-server system, or in a network with serial services, such as routing.

In a grid computing service market, there are multiple grid service providers. If the type of jobs utilizing multiple grid computing services provided by different providers, a price change in anyone of these services may affect the load of other services via the consequent change of submission decisions, showing strong externalities among different services. If each service provider determines the price for their services independently and dynamically, the lack of effective communication among these service providers may cause unstable prices and service loads.

In the case of network service welfare maximization pricing, the optimum price is obtained by the first order condition from the objective function based on the aggregate utility of users in different servers [11,20], in which the effects of price change on the routes are all considered. When the same idea of general stochastic equilibrium is applied to grid network resource pricing, the delay cost is only counted for the nodes on the critical paths, while the prices for the nodes on both critical paths and non-critical paths contribute to the total service cost. This then complicates the optimum pricing problem.

Another point for grid network resource pricing is that the user's choice of GCCP or LCCP may affect the equilibrium. According to the discussion in Section 4, priority selections for GCCP may not necessarily match all locally optimized priorities. While the stochastic general equilibrium network traffic pricing model [11] is designed to maximize total service welfare with the optimum prices, which assumes that users' utilities are optimized at each server, it may not lead to the same equilibrium outcome in a grid computing economy, in which some of GCCP-based priority selections could deviate from the optimum.

As the GCCP-based optimization is practically infeasible because of computational complexity, the LCCPbased optimization becomes the next best choice. The localized objectives of LCCP-based approach match the objective function of stochastic general equilibrium model; and solving a LCCP is computationally feasible. If the LCCP-based approach is prevailing, it means that the user side and the service provider side will cooperate in the equilibrium of grid computing economy, when the decisions of optimum pricing are based on the stochastic general equilibrium. In the Appendix, we present a grid network service pricing model for the LCCP-based service priority selection, aiming at the total service welfare maximization. The expression of pricing formula (A-2) implies that,

1) Given that users make service request submission decisions based on the LCCP approach, the services of the grid network can be optimally priced according to the service request arrivals at each server.

2) Although the throughput time is no longer an issue for non-critical paths as it is for critical paths, it is weighted in the expected delay cost that affects the price level.

3) The service loads at some servers affect service prices at other servers, particularly when these two groups of servers are on the critical paths of different jobs.

## 7. Summary

As pricing becomes the inevitable trend in grid computing resource management from both profit-making and social welfare maximizing perspectives, an

Internet-based grid computing economy is emerging. Although the optimum grid service pricing is an important topic for service providers, little has been studied on the problems from the users' side. In this paper, we examined the problem that grid computing users are confronting — a decision problem of minimizing their grid service cost by optimizing service priority selection at each server, where a service provider set differentiated prices for different service priorities. We conceptualized a grid computing network for a specific multi-subtask job submitted into a prioritized CPM network, where each node is a virtual machine processing a subtask. We then identify this problem as a time–cost tradeoff problem, which is differentiated from traditional problem in that our formulation takes into account a delay cost in regard to the total throughput time, thus no budget or deadline constraint is necessary in finding the optimal solution.

Based on the setting of the model, we proposed a costeffective critical path approach to investigate the heuristic solution for the prioritized CPM problem. We found that the locally cost-effective critical path (LCCP), defined by minimizing a service cost with a locally optimized priority, can serve as the heuristic critical path that provides a lower bound for a globally cost-effective critical path (GCCP), which is defined as the optimal critical path among all possible solutions, if the two critical paths share the same node set. To refine the priority selections, we conceived an algorithm to refine priorities on the noncritical paths to further reduce the total cost. Finally, a discussion of the effects of the user's priority selections on the pricing of the grid is provided to highlight the importance of this research and to elicit further research on the service-side resource pricing problem.

Because we are the first group of researchers tackling this type of prioritized CPM problem, the LCCP/GCCP based approach proposed in this paper should also be the first one in the research literature of this problem. The application of the proposed approach can be generalized to the similar problem, such as supply chain management, where each node on the chain may have a set of several pairs of start and finish times with different costs. The supply chains then effectively resemble a grid of nodes and can be modeled as a prioritized CPM network, where our approach and the algorithm are applicable.

This paper provides a starting point for the further research with several open issues, such as finding the upper bound of GCCP and a feasible algorithm that can solve the GCCP for the prioritized CPM problem with a reasonable computational complexity. Also, the LCCP approach proposed in this paper can serve as a benchmark for algorithm validation.

## Appendix A. A Service Pricing Model for Grid Computing Network

The network traffic pricing model aimed at service welfare maximization has been extensively discussed in [11,19,20]. In this grid computing network pricing model we only focus on the different perspectives from the previous model. Therefore, we discuss the simplified situation but without losing the explanatory power.

Consider a multi-priority grid computing network $( \psi , \varPhi )$ , where $\scriptstyle \Psi = \{ 1 , . . . , m , . . . \}$ is a server set and $\varPhi =$ $\{ K _ { m } | \ m \in \psi \}$ is the priority set with every element corresponding to each server m inΨ. Let b and e be the start and end point of a grid computing job. When a user submits a computing job, which is composed of multiple subtasks, to a server subset $M \subseteq \Psi ,$ his service priority selection problem can be modeled as a prioritized CPM network defined in Section 2. We assume that each subtask of a job consumes only one unit of service at any server. In this way, the demand to a specific priority at a server can be simplified as the summation of the subtasks arriving at the server.

## Notations:

$i \in I -$ User

$\scriptstyle  j \in J -$ Job type. A job may consist of multiple subtasks. If two jobs are of the same type, they have the same composition of such task. That is, subtasks in the same order of the two jobs have the same size with regard to the service time.

$q _ { j m } \in Q -$ The size of the subtask of type-j job server m. Jobs of the same type have the same number of subtasks, each being serviced by the same server but differentiated in service priority selections because of different unit delay costs and different gross values perceived by users.

$m \in { \cal M } \mathrm { ~ - ~ } \mathrm { ~ A ~ }$ server in the prioritized CPM network. $M \subseteq \Psi$

$k _ { m } \in K _ { m } -$ Server m's service priority.

$\lambda _ { i j }$ The exogenous arrival rate of type-j job submitted by user i when there is no cost for the service.

$\nu _ { i j }$ The gross value of type-j job submitted by user i

$\delta _ { i j } -$ The unit delay cost of type-j job submitted by user i

$U _ { i j } -$ The utility of type-j job submitted by user i $R { = } ( r _ { m k q } ) _ { | \psi | \times K \times | Q | }$ — Price matrix, where $K { = } m a x \{ | K m | \}$ and $r _ { m k q }$ is the price for a size-q subtask using priority-k service at server m

$x _ { i j m k q }$ — The service status variable for the server on a critical path. $x _ { i j m k q } = 1$ when a size-q subtask in type-j job is submitted by user i to the priority-k service of server m; $x _ { i j m k q } = 0$ otherwise.

y<sub>ijmkq</sub> — The service status variable for the server on a non-critical path. $y _ { i j m k q } = 1$ when a size q subtask in type-j job is submitted by user i to the priority-k service of server m; $y _ { i j m k q } = 0$ otherwise.

$\pi ( R ) { = } ( { \pi } _ { i j } ) _ { | I | \times | J | } \ { - } ^ { { \bf \delta } }$ The status variable matrix for submission decisions, where πij is type-j job submitted by user i. $\pi i j = 1$ if user i submits type-j job, which happens only when utility $U _ { i j } { > } 0 ; \pi _ { i j } { = } 0$ otherwise.

${ \varphi _ { i j } } \mathrm { { = } } { \lambda _ { i j } } { \pi _ { i j } } { ( R ) }$ — The actual arrivals of type-j jobs submitted by user i.

$G ( R ) { = } ( g _ { m k q } ( R ) ) _ { \mid \psi _ { \mid } \times K \times \mid Q \mid } -$ The service load matrix for a server m, where $\scriptstyle g _ { m k q } ( R ) = \sum _ { I , J } \lambda _ { i j } ( x _ { i j m k q } +$ $y i j m k q ) q \pi i j ( R )$ is the service load of size-q subtasks at priority-k service of server m given service price matrix R.

$\tau _ { m k } ( q , R )$ — The throughput time with priority-k service of server m for a size-q subtask given service price matrix R. τmk(q, $R ) { = } F m k ( q , G ( R ) )$ , where $F _ { m k } ( \cdot )$ is the unit throughput time function for priority-k service and its value depends on the service loads at different priority classes at server m, provided that service throughput time is linear to the subtask size.

$T = ( t _ { i j } ( R ) ) _ { | I | \times | J | } \ -$ The matrix of total throughput time, where $t i j ( R )$ is the total throughput time for type-j job submitted by user i.

Other notations are the same as those previously defined.

We can obtain:

1) The total throughput time for a type-j job submitted by user i:

$$
\begin{array}{l} t _ {i j} (R) = \sum_ {m \in P _ {i j}} \sum_ {K m} \sum_ {Q} x _ {i j m k q} \tau_ {m k} (q, R) \\ = \sum_ {m \in P _ {i j}} \sum_ {K m} \sum_ {Q} x _ {i j m k q} F _ {m k} (q, G (R)), \\ = \sum_ {m \in P _ {i j}} \sum_ {K m} F _ {m k} (q _ {j m}, G (R)), \end{array}
$$

where $P _ { i j }$ is the LCCP of type j job submitted by user i 2) The expected utility:

$$
\begin{array}{l} U _ {i j} = \pi_ {i j} (R) [ v _ {i j} - t _ {i j} \delta_ {i j} - \sum_ {m \in M, k \in K m} \sum_ {Q} (x _ {i j m k q} \\ + y _ {i j m k q}) r _ {m k q} ] \end{array}
$$

3) The total revenue from grid network services:

$$
\begin{array}{l} \prod = \sum_ {m \in \Psi ,} \sum_ {k \in K m} \sum_ {Q} g _ {m k q} (R) r _ {m k q} \\ = \sum_ {m \in \Psi ,} \sum_ {k \in K m} \sum_ {Q} \sum_ {I, J} \lambda_ {i j} (x _ {i j m k q} \\ + y _ {i j m k q}) q \pi_ {i j} (R) r _ {m k q} \end{array}
$$

4) The total service welfare:

$$
\begin{array}{l} W = \prod + \sum_ {I, J} U _ {i j} \\ = \sum_ {m \in \Psi} \sum_ {k \in K m} \sum_ {Q} \sum_ {I, J} g _ {m k q} (R) r _ {m k q} \\ \quad + \sum_ {I, J} \lambda_ {i j} \pi_ {i j} (R) [ v _ {i j} - t _ {i j} \delta_ {i j} - \sum_ {m \in \Psi} \sum_ {k \in K m} \sum_ {Q} (x _ {i j m k q} \\ \quad + y _ {i j m k q}) r _ {m k q} ] \\ = \sum_ {m \in \Psi} \sum_ {k \in K m} \sum_ {Q} \sum_ {I, J} g _ {m k q} (R) r _ {m k q} \\ \quad + \sum_ {I, J} \lambda_ {i j} \pi_ {i j} (R) [ v _ {i j} - t _ {i j} \delta_ {\bar {i j}} ] \\ \quad - \sum_ {m \in \Psi} \sum_ {k \in K m} \sum_ {Q} \sum_ {I, J} g _ {m k q} (R) r _ {m k q} \\ = \sum_ {I, J} \lambda_ {i j} \pi_ {i j} (R) [ v _ {i j} - t _ {i j} \delta_ {\bar {i j}} ] \end{array}
$$

5) The welfare maximization problem for the grid network is:

$$
\begin{array}{l} \text { Max } W (\pi , T) \\ = \sum_ {I, J} \lambda_ {i j} \pi_ {i j} (R) [ v _ {i j} - t _ {i j} \delta_ {i j} ] \text { s.t. } t _ {i j} (R) \\ = \sum_ {m \in P _ {i j}} \sum_ {k \in K m} F _ {m k} (q _ {j m}, G (R)) \text { and } g _ {m k q} (R) \\ = \sum_ {I, J} (x _ {i j m k q} \\ + y _ {i j m k q}) q \pi_ {i j} (R), m \in \Psi , k \in K _ {m}, \text { and } q \in Q \end{array}\tag{A - 1}
$$

FOC with regard to $\pi _ { i j } { \mathrm { : } }$

$$
\begin{array}{l} v _ {i j} - \sum_ {m \in P _ {i j}} t _ {i j} \delta_ {i j} \geq \sum_ {s \in I, w \in J} \lambda_ {s w} \pi_ {s w} (R) \\ \delta_ {s w} \sum_ {n \in P _ {s w}} \sum_ {k \in K n} \sum_ {a \in \Psi} \sum_ {b \in K a} \sum_ {c \in Q} \\ [ c (x _ {i j a b c} + y _ {i j a b c}) \partial F _ {n k} (q _ {w n}, G) / \partial g _ {a b c} ] \\ \text { if } \pi_ {i j} (R) = 1. \end{array}
$$

$$
v _ {i j} - \sum_ {m \in P} t _ {i j} \delta_ {i j} <   0 \text {   if   } \pi_ {i j} (R) = 0.
$$

Following the approach in [11,20], we can obtain the optimum grid network service pricing formula:

$$
\begin{array}{l} r _ {m k q} = q \sum_ {s \in I, w \in J} \varphi_ {s w} \delta_ {s w} \sum_ {n \in P _ {s w}} \sum_ {k \in K n} \\ [ \partial F _ {n u} (c _ {w n}, G) / \partial g _ {m k q} ] \end{array}\tag{A - 2}
$$

## References

[1] D. Abramson, R. Buyya, J. Giddy, A computational economy for grid computing and its implementation in the Nimrod-G resource broker, Future Generation Computer Systems 18 (8) (2002) 1061–1074.

[2] P. Barta, F. Németh, R. Szabó, J. Bíró, Call admission control in generalized processor sharing schedulers with tight deterministic delay bounds, Computer Communications 26 (2) (2003) 65–78.

[3] R. Buyya, H. Stockinger, J. Giddy, D. Abramson, Economic models for management of resources in grid computing, Proceedings of International Conference on Commercial Applications for High-Performance Computing, SPIE Press, Denver, Colorado, USA August 20–24, 2001.

[4] D.D. Clark, Adding service discrimination to the internet, Telecommunication Policy 20 (1996) 169–181.

[5] W.B. Crowston, Decision CPM: network reduction and solution, Operational Research Quarterly 21 (1970) 435–452.

[6] P. De, E.J. Dunne, J.B. Ghosh, C.E. Wells, The discrete time– cost tradeoff problem revisited, European Journal of Operational Research 81 (1995) 225–238.

[7] P. De, E.J. Dunne, J.B. Ghosh, C.E. Wells, Complexity of the discrete time–cost tradeoff problem for project networks, Operations Research 45 (1997) 302–306.

[8] S. Floyd, Kevin Fall, Promoting the use of end-to-end congestion control in the internet, IEEE/ACM Transactions on Networking 1998.

[9] L. Gommans, C.D. Laat, B.V. Oudenaarde, A. Taal, Authorization of a QoS path based on generic AAA, Future Generation Computer Systems 19 (6) (2003) 1009–1016.

[10] J. Gomoluch, M. Schroeder, Performance evaluation of marketbased resource allocation for grid computing, Concurrency and Computation: Practice and Experience 2004, p. 00:1–6.

[11] A. Gupta, D.O. Stahl, A.B. Whinston, A stochastic equilibrium model of internet pricing, Journal of Economic Dynamics and Control 21 (1997) 697–722.

[12] A. Gupta, D.O. Stahl, A.B. Whinston, Managing computing resources in intranets: an electronic commerce perspective, Decision Support Systems 24 (1998) 55–69.

[13] A. Gupta, D.O. Stahl, A.B. Whinston, The economics of network management, Communications of the ACM 42 (1999) 57–63.

[14] R.T. Harvey, J.H. Patterson, An implicit enumeration algorithm for the time/cost tradeoff problem in project network analysis, Foundations of Control Engineering 4 (1979) 107–117.

[15] F.S. Hillier, G.J. Lieberman, Introduction to Operations Research, McGraw Hill, New York, 2001.

[16] Insight Research Corporation, Grid Computing — An Opportunity for Telecom Revenue Growth, , May 27 2003 http://www. insight-corp.com/pr/5\_27\_03.asp.

[17] Jonathan Kantor, Winning the Battle for ROI in the War on Terrorism, 2003, http://cedar.intel.com/cgi-bin/ids.dll/content content.jsp?cntKey=Generic+Editorial%3a%3apentium4\_ terrorism&cntType=IDS\_EDITORIAL&catCode=BYM.

[18] C. Kenyon, G. Cheliotis, Architecture requirements for commercializing grid resources, Proceedings of the 11th IEEE International Symposium on High Performance Distributed Computing HPDC-11 2002 (HPDC'02).

[19] Z. Lin, P.S. Ow, D.O. Stahl, A.B. Whinston, Exploring traffic pricing for the virtual private network, The Proceedings of WITS'99 December 11–12 1999, Charlotte, North Carolina

[20] Z. Lin, D.O. Stahl, A.B. Whinston, A traffic-pricing model for the packet-switching network with prioritized round-robin

queueing, The 5th INFORMS-CIST November 5 2000, San Antonio.

[21] Z. Lin, H. Zhao, S. Ramanathan, Pricing web services for optimizing resource allocation — an implementation scheme, Web2003, Seattle, WA December 13–14 2003.

[22] W.L. Meyer, L.R. Shaffer, Extending CPM for multiform project time–cost curves, Journal of the Construction Division, Proceedings of the ASCE, vol. 91 1965, pp. 45–65.

[23] D. Mielke, The great grid revolution, Telecommunications 37 (5) (2003) 15–17.

[24] M. Skutella, Approximation algorithms for the discrete time–cost tradeoff problem, Mathematics of Operations Research 23 (4) (Nov. 1998) 909–929.

[25] R. Wolski, J.S. Plank, J. Brevik, T. Bryan, Analyzing marketbased resource allocation strategies for the computational grid, The International Journal of High Performance Computing Applications 15 (3) (Fall 2001) 258–281.

Mei Lin is a doctoral student at the Center for Research in Electronic Commerce in the McCombs School of Business at the University of Texas at Austin. She has a Bachelor of Science in computer sciences and a Bachelor of Science in applied mathematics, received in 2004 from the University of Texas at Austin. She is currently conducting research in the areas of P2P networks, grid computing, online auctions, and reputation systems.

Zhangxi Lin is an associate professor at the Rawls College of Business Administration, Texas Tech University. He received an MEng degree in computer science from Tsinghua University in 1982, an MS degree in economics in 1996 and a PhD. degree in information systems in 1999 from the University of Texas at Austin. He is also an adjunct professor for Tongji University, and the Director of Research Center for the Next-generation Internet, Fujian University of Technology. His research interests include electronic commerce, data communications, information economics, and IT strategy. He has published papers in Information Systems Research, Decision Support Systems, Communications of AIS, Information Technology and Management, Information Systems Management, and Journal of Global Information Management.
