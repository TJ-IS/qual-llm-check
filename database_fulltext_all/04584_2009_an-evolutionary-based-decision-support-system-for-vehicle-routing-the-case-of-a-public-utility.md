---
otero_id: 4584
otero_key: "YHGTDZVX"
title: "An evolutionary-based decision support system for vehicle routing: The case of a public utility"
authors: "Jorge E. Mendoza; Andrés L. Medaglia; Nubia Velasco"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.019"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An evolutionary-based decision support system for vehicle routing: The case of a public utility

Jorge E. Mendoza <sup>a,b</sup>, Andrés L. Medaglia <sup>a,</sup>⁎, Nubia Velasco

<sup>a</sup> Centro de Optimización y Probabilidad Aplicada (COPA), Industrial Engineering Department, Universidad de los Andes, Colombia

<sup>b</sup> Équipe Systèmes Logistiques et de Production, IRCCyN (UMR 6597), École des Mines de Nantes, France

## a r t i c l e i n f o

Article history: Received 22 October 2007 Received in revised form 28 July 2008 Accepted 18 November 2008 Available online 3 December 2008

Keywords: Distance constrained vehicle routing problem Decision support systems Evolutionary algorithms Memetic algorithms

## a b s t r a c t

Customer-related processes in a public utility, such as meter replacement programs, demand a large number of auditing visits to customer sites. The proposed decision support system (DSS) helps the operating manager to plan these visits by integrating commercial systems such as SAP/R3 and ArcGIS with a custom-made distance-constrained routing module. This module includes a modi<sup>fi</sup>ed Clarke and Wright savings heuristic and two memetic algorithms, along with two integer-programming clustering models whose function is to balance the workload. The system was tested on ten real-world distance-constrained vehicle routing instances ranging from 323 to 601 nodes.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Bogotá, the largest city in Colombia with nearly 7,000,000 inhabitants, is also the ninth largest in the Americas [53]. The city's water and sewer company, Empresa de Acueducto y Alcantarillado de Bogotá (EAAB), serves 1,713,147 households and 360,513 commercial and industrial clients in the metropolitan area.

To better serve its customers, EAAB has divided the city into <sup>fi</sup>ve independent business units or service zones, the operation of each of which is outsourced to a third-party contractor that executes activities like water meter replacement; service suspension, connection, and reconnection; water meter readings; and the calculation and distribution of water bills. However, according to local regulations, public utilities must audit all operations outsourced to third parties, so in the case of EAAB, the role of an auditor includes visiting clients recently serviced by the contractor to verify that the work was executed properly.

Before the proposed decision support system was implemented, the auditing routes were designed independently for each activity. Every day, one activity (e.g., service suspension) was selected based on its cumulative number of visits. The data preparation step for the route design process involved manual downloading and merging up to <sup>fi</sup>ve different data sets from the enterprise information system. Then, the routes were designed based on the sequence used for reading meters and distributing bills as follows. Service zones are divided into portions, each comprising a cluster of customers who share the same hydraulic circuit and whose meters are read on the same day. These portions, which are labeled by letters that do not necessarily express geographical proximity, are further divided into smaller reading routes identi<sup>fi</sup>ed by the portion letter plus a number representing geographic position within that portion. When a new client is connected to EAAB's network, it is geographically referenced and assigned a reading unit, a logical sequence within a reading route that clearly identi<sup>fi</sup>es the client's service zone, portion, reading route, and sequence within the route. Auditing routes were built by sorting the client list based on reading units. Clients were then assigned to auditors until each auditor's workday capacity is reached. Finally, the routes were manually distributed among auditors, aiming to achieve a balanced workload.

Fig. 1 illustrates the current routing method for two days with a maximum workload per auditor of eight visits. On day 1, thirteen clients are visited due to a suspension, while on day 2, only 3 clients are visited due to a meter replacement. The bottom part of the <sup>fi</sup>gure outlines the routes produced from the sorted list of clients. From the multiple route crossings we can conclude that there is room for improvement in the current routing method.

To address this problem, this paper presents EAAB Vehicle Routing Tools (EAAB-VRT), a DSS designed to improve the ef<sup>fi</sup>ciency of the EAAB auditing process. Speci<sup>fi</sup>cally, the system integrates a friendly graphical user interface (GUI) with a decision module and existing enterprise and geographic information systems like SAP/R3 and ArcGIS.

Day1: suspensions

<table><tr><td>Client ID</td><td>Reading Unit</td><td>Client ID</td><td>Reading Unit</td></tr><tr><td>1</td><td>S23579</td><td>2</td><td>A26642</td></tr><tr><td>2</td><td>A26642</td><td>8</td><td>A29874</td></tr><tr><td>3</td><td>D29675</td><td>9</td><td>B26734</td></tr><tr><td>4</td><td>T21452</td><td>12</td><td>C21267</td></tr><tr><td>5</td><td>F26785</td><td>3</td><td>D29675</td></tr><tr><td>6</td><td>Q25534</td><td>7</td><td>E21324</td></tr><tr><td>7</td><td>E21324</td><td>5</td><td>F26785</td></tr><tr><td>8</td><td>A29874</td><td>10</td><td>G24352</td></tr><tr><td>9</td><td>B26734</td><td>13</td><td>H26545</td></tr><tr><td>10</td><td>G24352</td><td>11</td><td>K29143</td></tr><tr><td>11</td><td>K29143</td><td>6</td><td>Q25534</td></tr><tr><td>12</td><td>C21267</td><td>1</td><td>S23579</td></tr><tr><td>13</td><td>H26545</td><td>4</td><td>T21452</td></tr></table>

Route 1

Route 2

Day 2: meter replacements

<table><tr><td>Client ID</td><td>Reading Unit</td><td>Client ID</td><td>Reading Unit</td></tr><tr><td>1</td><td>Q22258</td><td>3</td><td>B27681</td></tr><tr><td>2</td><td>S29818</td><td>1</td><td>Q22258</td></tr><tr><td>3</td><td>B27681</td><td>2</td><td>S29818</td></tr></table>

Route 1

![](/api/attachments/YHGTDZVX/fulltext/images/8e51f75c856a3b068b2ee3ae0283be248b965fff45cbb9c6485d2a4dc26b5c08.jpg)  
Fig. 1. Example of the current route building process at EAAB.

The paper is organized as follows. Section 2 de<sup>fi</sup>nes the routing problem and the relevant notation. Section 3 reviews the literature on methods for solving routing problems related to that of EAAB and outlines work on DSS for vehicle routing. Section 4 presents an overview of EAAB-VRT. Section 5 describes the implemented routing algorithms, and Section 6, the implemented clustering models. Section 7 presents the computational experiments using a set of instances built with real-world data. Section 8 concludes the paper.

## 2. Problem de<sup>fi</sup>nition

The vehicle routing problem (VRP) faced by EAAB has the following key characteristics. First, auditors start and end their routes at the same depot; namely, EAAB's operation center. Second, every auditor is assigned one route per shift. Third, EAAB can schedule as many shifts as needed to complete the auditing visits. Fourth, every shift lasts 6 h (excluding breaks). Fifth, all auditors are quali<sup>fi</sup>ed to execute every activity. Sixth, a service time is associated with each visit that depends on the activity being performed. Lastly, because the average speed of vehicles is assumed to be constant, both the service time and the shift duration can easily be transformed into a distance equivalent. Such a problem is known in the vehicle routing literature as the distanceconstrained vehicle routing problem (DVRP). The reader should be aware that the acronym DVRP has also been used on the literature for another VRP variant, namely, the dynamic vehicle routing problem, which is out of the scope of this work.

Formally, the DVRP can be de<sup>fi</sup>ned on a complete and undirected graph $G = ( { \mathcal { N } } , { \mathcal { E } } )$ , where $\mathcal { N } = \{ 0 , . . . , n \}$ is the node set and the edge set. Nodes $i = 1 \ldots n$ are the clients, and node i=0 is the operation center (depot). The service time at node i is denoted by $t _ { i \cdot }$ A distance $d _ { e }$ is associated with edge $e = ( i , j ) = ( j , i ) \in \mathcal { E }$ and represents the travel <sup>E</sup>distance between nodes i and j. Assuming the same constant speed for every vehicle, this travel distance is transformed into travel time. The DVRP is to <sup>fi</sup>nd a set of vehicle routes (being | | a decision variable), <sup>R R</sup>where a route is a tour that begins at the depot, traverses a subset of the client nodes following a sequence, and ends at the depot. Each client node must be visited by exactly one route, and the total length of each route $l _ { r }$ including travel and service times, cannot exceed the maximum duration L. Finally, the routes should be chosen so that the total distance over all routes is minimal.

Henceforth, depending on the context, we refer to the route r ∈ either as an ordered set of arcs $r = \{ ( i _ { 1 } , i _ { 2 } ) , . . . , ( i _ { k - 1 } , i _ { k } ) , . . . , ( i _ { n _ { r - 1 } } , i _ { n _ { r } } ) \}$ or as a sequence of nodes $r { = } ( i _ { 1 } { , } . . . i _ { n _ { r } } )$ , where $i _ { k } \in \mathcal N$ and $n _ { r }$ is the number of client nodes in route r.

## 3. Literature review

Despite its wide practical applicability, the DVRP has received little attention in the vehicle routing problem literature [48,12], although Laporte et al. [25] presented two exact algorithms based on cutting planes and branch and bound that could solve instances of up to 60 clients to optimality. More recently, Li et al. [26] proposed a greedy tour partitioning heuristic to compute a worst case solution for DVRP instances when the distance from the depot to the farthest client is less than half the distance constraint.

In contrast, the closely related and more general distanceconstrained capacitated VRP (DCVRP), which considers not only the distance constraint but also vehicle capacity limits, has received more attention. The early work on the DCVRP included that of Christo<sup>fi</sup>des, Mingozzi and Toth [8], who tested <sup>fi</sup>ve different heuristics on a set of now classical capacitated VRP (CVRP) and DCVRP benchmark instances (hereafter, CMT). The results obtained for the DCVRP were later improved by other heuristics, speci<sup>fi</sup>cally the algorithms proposed by Fisher and Jaikumar [17], and Paessens [35]. However, the best quality results for the DCVRP have been achieved using metaheuristics.

Among the most successful metaheuristics for the DVRP are the simulated annealing (SA) and tabu search (TS) algorithms of Osman [34], which are based on a rich neighborhood named λ interchange. Taillard [46] also proposed a TS algorithm in which the search is parallelized by decomposing the problem into subproblems that can be solved independently. A similar decomposition approach was used by Reinmann et al. [41] who proposed D-Ants, a savings-based ant system (AS) which repetitively constructs smaller instances (subproblems) and use their solutions to guide the search of the intelligent agents. Gendreau et al. [19] proposed taburoute, a TS algorithm with a special neighborhood structure based on a generalized insertion procedure. More recently, Toth and Vigo [49] proposed the granular TS based on a highly restricted neighborhood scheme that leads the algorithm to a more ef<sup>fi</sup>cient search by only evaluating promising moves at each iteration. In addition, Li et al. [27] proposed the recordto-record travel method to solve very large instances. However, to the best of our knowledge, the algorithm that has provided the best overall results to date is the active guided evolution strategies metaheuristic of Mester and Bräysy [31]. Their metaheuristic, besides solving the classical CMT instances, successfully solves challenging sets of popular CVRP and DCVRP benchmark instances like the large scale VRP (LSVRP) instances of Golden et al. [22] and the very large scale VRP (VLSVRP) instances of Li et al. [27]. Furthermore, metaheuristics are also known to be the best approaches to solve large instances of the VRP with time windows (VRPTW) [6], a problem where each client expects a visit to happen within a given time interval (window). The DVRP in hand can be seen as a particular case of the VRPTW where all clients share the same time window given by the driver's shift and the vehicle capacity is unlimited.

Until very recently, genetic algorithms (GAs), with the notable exception of the VRPTW, were considered noncompetitive for routing problems [11,47]. However, recent implementations have shown that GAs can be a valid alternative for solving other routing problems. For example, the genetic vehicle representation (GVR) introduced by Pereira et al. [37] has proven <sup>fl</sup>exible and robust for routing problems. Speci<sup>fi</sup>cally, the authors reported a maximum gap of 3.5% with respect to the best known solutions in a set of classical benchmark instances for the CVRP by Augerat [3] (set A) and Christo<sup>fi</sup>des and Eilon [7]. Similarly, Baker and Ayechew [4] presented both a pure GA and a hybrid GA enhanced with a local search (LS) procedure. On the CMT instances for the pure GA, they reported an average gap of 2.49% with respect to the best known solutions; for the hybrid algorithm, they reported an average gap of 0.50%, and they did report best known solutions for some instances. More recently, Alba and Dorronsoro [1], using what the call a cellular GA, reached eight new best solutions for Van Breedam's [50] CVRP instances and one for the LSVRP set. However, the best known solutions for some LSVRP instances and for most CMT instances have been produced by the memetic algorithm (MA) proposed by Prins [39] whose implementation is based on a clever partition or split of the chromosomes based on a shortest path reformulation. MAs are genetic algorithms that comprise a local search procedure to favor intensi<sup>fi</sup>cation on the genetic search [32]. Thus, well-designed GAs and MAs have become a valid competitive alternative to embed at the core of a decision support system for vehicle routing.

Such routing processes, as those arising in the case of EAAB, need to be routinely solved on a daily or weekly basis. As a result, DSSs have been particularly successful in this area [15]. For example, Basnet et al. [5] presented a stand-alone application for constructing milk collection routes between farmers and dairy facilities in New Zealand. This routing problem consisted of a multidepot capacitated VRP that was solved using the sweep algorithm [21] and the farthest insertion heuristic [45] on a cluster-<sup>fi</sup>rst, route-second approach. Similarly, as part of a system developed to deal with two different routing problems at a major American retailer, Weigel and Cao [51] reported an implementation that directly integrated information from a geographical information system (GIS) with a set of optimization algorithms. To solve the routing problems, the system used a multipleinsertion heuristic [43] to generate an initial solution, which was later improved by a tabu search algorithm. Another DSS, outlined by Nussbaum et al. [33], was implemented to solve a complex fuel distribution problem for a Chilean company. In this case, the routes designed for fuel distribution were subject to tanker capacity, shift durations, delivery time windows, and tanker/client allocation constraints. Unlike the other implementations, this DSS based its

decision module on compiled historical expert knowledge rather than optimization techniques. More recently, Faulin et al. [16] proposed LOGDIS, a DSS designed to solve a routing problem at a frozen food company in Spain that had to distribute products to a large number of clients located in towns outside the city in which the depot was located. After comparing the solutions of real-world instances obtained with different construction heuristics and a mixed integer program, they chose to implement a savings heuristic. With a focus on physical architecture, Gayialis and Tatsiopoulos [18] reported a completely different approach, an information technology-based DSS (IT-DSS) for vehicle routing that uses commercial IT applications instead of custom-developed modules. Their work is particularly relevant to this paper in that we also integrate existing commercial tools into EAAB-VRT.

A  
![](/api/attachments/YHGTDZVX/fulltext/images/907917c0f14cb850b8aceb7253d6ec4d1372552c7e18c826af2730ff9654c29c.jpg)

![](/api/attachments/YHGTDZVX/fulltext/images/b12120a254186a43a2cc79ef8078a3f480962b20e18246ecf354abff3a92a9b3.jpg)  
Fig. 2. EAAB-VRT Architecture.

Implementations of DSSs to solve different routing problems in the speci<sup>fi</sup>c case of public utilities have also been reported in the literature. For instance, Wunderlich et al. [52] presented a DSS solution for routing meter readers at the Southern California Gas Company. This problem of routing meter readers and designing billing cycles in public utilities has also been discussed by Stern and Dror [44] and more recently by Groër et al. [23], who, while offering no speci<sup>fi</sup>c DSS implementations, certainly introduced tools that could be embedded into the decision module of a system to enhance public companies' decision processes. Likewise, Ghose et al. [20] reported a GIS-based DSS to support the design of ef<sup>fi</sup>cient waste collection routes in India, and Jung et al. [24] described the design and implementation of a DSS for planning mail pickup and delivery routes for the Korean post of<sup>fi</sup>ce. More recently, Perrier et al. [38] surveyed the use of several DSSs for snow plowing in different countries, and Ray [40] introduced a Webbased DSS for designing routes to move oversized and overweight vehicles through the state highways of Delaware, USA. Nevertheless, despite this large body of work on the use of DSSs for vehicle routing and certain applications for public decision making, the literature includes no reports on the use of a DSS for vehicle routing in a water and sewer utility like EAAB.

To <sup>fi</sup>ll this void, this research aims to expand the set of decisionmaking tools available to public utilities for distance-constrained vehicle routing.

## 4. EAAB-VRT

EAAB-VRT impacts the current decision process described in Section 1 by improving the visit planning phase along with a better route design and allocation to auditors. As shown in Fig. 2(A), EAAB-VRT is comprised of two modules, namely, the planning module and the routing module tied by a friendly GUI.

The planning module consists of a set of SAP/R3 transactions and Microsoft Excel (MSE) macros that allow the integration of visits from all activities on the same planning period. Before EAAB-VRT, this integration was not possible due to the long processing time required by manual merging of data sources. After evaluating different alternatives involving the operation managers and the auditors, it was decided to de<sup>fi</sup>ne a new planning horizon of one week and to mix visits with different activities in the same auditing route.

The routing module is comprised of a set of routing algorithms and clustering models supported by several optimization engines. The routing algorithms are supported by JCW [30] and JGA [28], frameworks for the rapid development of savings-based routing heuristics and evolutionary algorithms, respectively. Both frameworks provide a collection of Java classes that can be easily extended and reused to generate various optimization applications. On the other hand, the clustering models are solved using Xpress-MP's mixed integer programming (MIP) optimizer, from Fair Isaac Corporation [13].

To plan the auditing operations, the user follows the process <sup>fl</sup>ow described in Fig. 2(B). The process begins by consolidating data from different sources. First, the system collects visit data from SAP/R3 for the weekly planning horizon. Then, using ArcGIS, it queries and geocodes each visit. Last, it compiles the data and transforms it into a DVRP instance. Once the instance is created, the user selects a solution approach from those available in the routing module (see Fig. 3(A)).

The output from the routing module is presented to the user as an MSE spreadsheet. Fig. 3(B) shows such a spreadsheet displaying a managerial perspective of the performance metrics for four alternatives. A more tactical yet graphical representation of the solution is shown in Fig. 3(C). This output is produced by RoutePlotter, a software component that allows some manual intervention on the routes by the decision maker. For instance, the user can move a node within a route or insert it on a different route. Even though RoutePlotter was originally developed for EAAB-VRT, it has such a broad range of applications, that it was packaged as an independent plug-in for MSE [29].

## 5. Evolutionary-based routing algorithms

The evolutionary algorithms embedded in EAAB-VRT follow the general structure presented in Algorithm 1. At each generation t, two genetic operators, namely, crossover and local search are applied on selected individuals of population $\mathcal { P } ( t )$ . The offspring produced by the genetic operators, $\mathcal { C } _ { c } ( \mathfrak { t } )$ and $\mathcal { C } _ { l s } ( t ) ,$ <sup>P</sup>, form a new children population (t). Both $\mathcal { C } ( t )$ <sup>C C C</sup>and (t) are then merged into an extended population ε(t), from where the best individuals are selected to become part of the new population (t+1). Since the whole population is replaced at <sup>P</sup>each iteration and the algorithms use a LS procedure to intensify the search, the evolutionary algorithms in EAAB-VRT can be de<sup>fi</sup>ned as generational memetic algorithms.

The reminder of this section focuses on detailed descriptions of the generation of the initial population, the genetic operators, and the tuning of the parameters.

## Algorithm 1. Pseudocode for the MA

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1:  $t \leftarrow 1$ 
2: initialize  $\mathcal{P}(t)$ 
3: evaluate  $\mathcal{P}(t)$ 
4: while  $t \leq T$  do
5: perform local search over  $\mathcal{P}(t)$  and generate  $\mathcal{C}_{ls}(t)$ 
6: cross  $\mathcal{P}(t)$  and generate  $\mathcal{C}_{c}(t)$ 
7:  $\mathcal{C}(t) \leftarrow \mathcal{C}_{ls}(t) \cup \mathcal{C}_{c}(t)$ 
8: evaluate  $\mathcal{C}(t)$ 
9:  $\mathcal{E}(t) \leftarrow \mathcal{P}(t) \cup \mathcal{C}(t)$ 
10: select  $\mathcal{P}(t+1)$  from  $\mathcal{E}(t)$ 
11:  $t \leftarrow t+1$ 
12: end while
</div>

## 5.1. Initial population

A solution of the DVRP is encoded into a multipermutation genotype known as the genetic vehicle representation (GVR) [37]. Speci<sup>fi</sup>cally, each permutation contains an ordered set of client visits representing an auditor's route.

To accelerate algorithmic convergence [42], the initial population of the implemented MAs is generated based on a distanceconstrained variant of the Clarke and Wright heuristic (C&W) [9]. The well-known C&W heuristic is based on the concept of savings. The algorithm starts from a trivial solution made up of n round trips from the depot to each client. At any given iteration two routes containing nodes i and j as extreme nodes (those connected to the depot) are merged generating a saving $s _ { i , j } = d _ { i , 0 } + d _ { 0 , j } - d _ { i , j }$ . The savings of all possible mergers are stored on a decreasingly sorted list known as the savings list. Moving from the top of the list, at each iteration the largest saving is selected and the route merger is done if feasible. Speci<sup>fi</sup>cally, in our distance-constrained variant a merge is said to be feasible only if the resulting route has a total distance lower than L.

The distance-constrained C&W is a deterministic algorithm, meaning that every time it runs, it obtains the same solution. We obtained a randomly generated initial population by introducing some noise into the algorithm's savings list. That is, every time we generate an individual, a fraction of the arcs are exchanged from their original position on the savings list. Then the deterministic distanceconstrained C&W is run and one solution for the DVRP is found and encoded.

This savings list alteration produces a perturbed solution compared to that given by the original heuristic. For instance, on a run with $\vert \mathcal { P } ( t ) \vert = P \vert = 2 0 0$ we found 159 different solutions with gaps on the <sup>P</sup>total distances ranging from −0.94% to 3.29% with respect to the solution of the original distance-constrained C&W. In conclusion, an initial population with good quality, yet diversi<sup>fi</sup>ed solutions.

A  
![](/api/attachments/YHGTDZVX/fulltext/images/f68ef00c546db754f5aca403c3e973a46c54f583a1ebee6e5cead22981d37ebc.jpg)

![](/api/attachments/YHGTDZVX/fulltext/images/259a481329f09dee672973102c5676568ddddcecad02469b90fecc5ae7465e3d.jpg)  
Fig. 3. DSS graphical user interface and output reports.

## 5.2. Crossover operator

The crossover operator is based on the GVR crossover proposed by Pereira et al. [37], in which a child inherits all the traits (routes) from one parent and a small portion of the genetic material (subroute) from the other parent (donor). To achieve this crossover, a subroute is randomly selected from the donor and inserted into the arc having the lowest insertion cost. In the child, duplicate nodes are eliminated, thereby preserving those in the inserting subroute. The insertion cost on arc $( i , j )$ of a subroute $r { = } ( i ^ { \prime } , { \ldots } , j ^ { \prime } )$ with initial node $i ^ { \prime }$ and terminal node j′ is denoted by $c _ { r } ( i , j )$ and calculated as follows:

![](/api/attachments/YHGTDZVX/fulltext/images/65e5bb42b1974ef9bf95e783b5350ab58ac8caf451b4be6f7c8a85bd0be35c20.jpg)  
Fig. 3 (continued ).

$$
c _ {r} (i, j) = d _ {(i, i ^ {\prime})} + d _ {(j ^ {\prime}, j)} - d _ {(i, j)}\tag{1}
$$

## 5.3. Local search operator

The local search procedure is inspired on the λ interchange [34]. When an individual is selected for LS, a random number of nodes $n ( r _ { 1 } ) { \leq } n _ { r }$ from route $r _ { 1 } \in \mathcal { R }$ are exchanged with $n ( r _ { 2 } ) { \leq } n _ { r _ { 2 } }$ nodes from route $r _ { 2 } \in \mathcal { R }$ (being $r _ { 1 }$ <sup>R</sup>and $r _ { 2 }$ randomly chosen from the selected individual).

Every time a given node i′ from route $r _ { 1 }$ is extracted, selection is based on the maximal possible savings calculated as follows:

$$
i ^ {\prime} \leftarrow \arg \max _ {i _ {k} \in r _ {1}} s (i _ {k})\tag{2}
$$

where $s ( i _ { k } )$ is de<sup>fi</sup>ned by

$$
s (i _ {k}) = d _ {(i _ {k - 1}, i _ {k})} + d _ {(i _ {k}, i _ {k + 1})} - d _ {(i _ {k - 1}, i _ {k + 1})}\tag{3}
$$

Once node $i ^ { \prime } \in r _ { 1 }$ is extracted, a decision must be made on the best place (arc) to insert it into $r _ { 2 } .$ This decision is based upon the minimal insertion cost de<sup>fi</sup>ned by

$$
\left(\hat {i}, \hat {j}\right) \leftarrow \arg \min _ {(i, j) \in r _ {2}} c _ {i ^ {\prime}} (i, j)\tag{4}
$$

where $c _ { i ^ { \prime } } ( i ^ { \prime } , j )$ is a special case of Eq. (1) in which both terminal nodes of the inserting subroute $r { = } \left( i ^ { \prime } \right)$ coincide. Under this condition, the insertion cost reduces to

$$
c _ {i ^ {\prime}} (i, j) = d _ {(i, i ^ {\prime})} + d _ {(i ^ {\prime}, j)} - d _ {(i, j)}\tag{5}
$$

This procedure is repeated until all the $n ( r _ { 1 } )$ nodes from $r _ { 1 }$ are extracted and inserted into $r _ { 2 } .$ Subsequently, the roles of $r _ { 2 }$ and $r _ { 1 }$ are reversed, and the process is repeated until the $n ( r _ { 2 } )$ nodes from $r _ { 2 }$ are extracted and inserted into $r _ { 1 } .$

## 5.4. Reparation strategies

The genetic operators described in Sections 5.2 and 5.3 guarantee that no child will contain duplicate visits to client nodes. However, there is no guarantee that the genetic operators will generate children that meet the distance constraint. Thus, this section describes two strategies that not only repair the individuals so that they meet the distance constraint but also pack the nodes into the routes more ef<sup>fi</sup>ciently.

## 5.4.1. Split bin-packing strategy

The <sup>fi</sup>rst reparation strategy, split bin packing (SBS), is a two-phase procedure. In the <sup>fi</sup>rst phase, SBS iterates over an individual's routes checking for violations on the distance constraint. When a violation is found (i.e., $l _ { r } { > } L ) ,$ , the subroute exceeding the distance constraint is split to form a new route. This procedure is repeated until no routes exceed the distance constraint. Fig. 4 (top) shows an example in which the maximum route length is $L = 1 1 0$ , but $l _ { 2 } = 1 1 9 > 1 1 0$ so that the subroute containing nodes 5 and 8 is split into a new route.

Even though this <sup>fi</sup>rst phase generates solutions that satisfy the distance constraint, it can also generate an inef<sup>fi</sup>cient number of routes. Therefore, the second phase performs a <sup>fi</sup>rst-<sup>fi</sup>t bin-packing procedure [36] that reduces the number of routes by trying to systematically pack every route into a subsequent route. Beginning with the <sup>fi</sup>rst route, it checks for a feasible insertion point at the next possible route. If this <sup>fi</sup>ts, it inserts the whole route at a given position and begins again. This procedure is repeated until no more <sup>fi</sup>rst-<sup>fi</sup>t packing is possible. Fig. 4 (right) shows how route $r = ( 9 , 2 )$ is inserted into route $r { = } ( 1 )$ just between the depot and node 1. Then route $r = ( 1 1 , 4 , 7 )$ is inserted into route $r { = } ( 9 , 2 , 1 )$ just after node i=9. This second phase is responsible for reducing the number of routes from <sup>fi</sup>ve to three.

![](/api/attachments/YHGTDZVX/fulltext/images/35d4d01d06e0b8582acea57f9539d7038dc835561d3c4a4459149c07f89e1589.jpg)  
Fig. 4. Split bin-packing reparation strategy.

## 5.4.2. Prins split strategy

The second reparation strategy, the split procedure proposed by Prins (PSS) [39], requires that the GVR genotype be transformed into a single chromosome without route delimiters; that is, a permutation of nodes. From the chromosome, an auxiliary graph G′ is built and used to <sup>fi</sup>nd the optimal partition of the permutation into feasible routes. The directed graph $G ^ { \prime } { = } ( \mathcal { N } ^ { \prime } , \mathcal { A } )$ is composed of the node set $\mathcal { N } ^ { \prime } { = } \{ 0 , i _ { 1 } { , } . . . , i _ { k } { , } . . . , i _ { n } \}$ and <sup>N A</sup>the arc set . Nodes $i _ { 1 } . . . , i _ { n } \in \mathcal { N } | \{ 0 \}$ , and node 0 is an auxiliary node (by <sup>A</sup>convention node $i _ { 0 } { = } 0 )$ <sup>N</sup>. Each arc $( i _ { k } , i _ { k + n _ { r } } ) \in \mathcal { A }$ represents a feasible route r starting and ending at the depot and traversing the sequence of client nodes from $i _ { k + 1 }$ to $i _ { k + n _ { r } }$ with a tour length of $l _ { r }$ The split procedure consists of <sup>fi</sup>nding the set of arcs (i.e., routes) along the shortest path connecting 0 and $i _ { n }$ in $G ^ { \prime } .$

Fig. 5 shows the split procedure for the same example used to illustrate the SBS, where L=110. In the top of Fig. 5(A), a solution encoded on a GVR genotype is transformed into a single chromosome; Fig. 5(B) then presents the resulting graph, G′. Because arcs (0,9),(9,6), (6,3) and (3,1) form the shortest path from 0 to 1, they form the feasible routes shown in Fig. 5(C). In our implementation, the shortest path on $G ^ { \prime }$ is found using the algorithm described by Prins [39], adapted to handle distance constraints.

## 5.5. Parameter tuning

As Cordeau et al. [10] pointed out, a good VRP metaheuristics should also be characterized by <sup>fl</sup>exibility and simplicity. Therefore, to target simplicity, the proposed evolutionary algorithms use a minimal set of the parameters commonly used in MAs, namely, population size P; number of generations T; and the crossover and local search probabilities denoted by $p _ { c }$ and $p _ { l s } ,$ respectively.

Because the ef<sup>fi</sup>ciency (speed) and accuracy of a metaheuristic are strongly in<sup>fl</sup>uenced by the values of its parameters [14], we set the values for P, T, $p _ { c }$ and $p _ { l s }$ via a two-phase study. The <sup>fi</sup>rst phase focuses on solution accuracy examining a wide range of parameters, while the second phase uses a factorial design of experiments (DOE) to select the best possible parameter values. The result is a set of robust parameter values with a good balance between computational ef<sup>fi</sup>ciency and solution accuracy.

## 5.5.1. Phase I: exploring a wide range of parameters

After preliminary testing, the candidate values for the parameters were set at 100, 200, and 300 for $P ;$ 1000, 2000, and 3000 for T; and 0, 0.25, 0.50, 0.75, and 1 for $p _ { c }$ and $p _ { l s } .$ The exploration of these 225 $( = 3 \times 3 \times 5 \times 5 )$ ) combinations took a total CPU time of 354.99 h (14.79 days) on eight machines, ranging from a computer with an Intel Pentium 4 520 processor running at 2792.9 MHz with 512 Mbytes of RAM to a computer with an Intel Core 2 Duo E6700 processor running at 1596.1 MHz with 2048 Mbytes of RAM.

The impact of the parameters on the solution accuracy is measured as the improvement with respect to the results obtained by the distance-constrained C&W. On a single run of a large 510-node instance conducted for each combination of parameters, the results showed, as expected, that combinations with higher values of P and T achieve higher improvements, ranging from 3.00% to 3.89%. The experiment also showed that high values of $p _ { c }$ strongly contribute to the solution accuracy. For example at middle levels of P and T (i.e., 200 and 2000), values of ${ \dot { p } } _ { c }$ higher than 0.5 consistently produce solutions that outperform the distance-constrained C&W by at least 3%. In consequence, middle and high values of P, T, and $p _ { c }$ are chosen for further analysis in the second phase of the parameter-tuning study.

In contrast, because the in<sup>fl</sup>uence of $p _ { l s }$ is less clear, it cannot be argued that high values of $p _ { l s }$ have a positive effect on the solution quality. Moreover, as described in Section 5.3, the LS is a timeconsuming procedure. Indeed, a statistical analysis shows that an increment of 1% on $p _ { l s }$ increases the average CPU time by 2.2%. Based on these observations, $p _ { l s }$ is set to a low value equal to 10%.

## 5.5.2. Phase II: fine tuning the parameter set

Based on the results obtained in the <sup>fi</sup>rst phase, $\texttt { a } 2 ^ { 3 }$ factorial design with two replications (runs) was implemented. The factors (parameters) were set at two levels: P at 200 and 300; T at 2000 and 3000; and $p _ { c }$ at 0.50 and 0.75. The responses were the total distance (accuracy) and the CPU time (speed). The results suggested that, in terms of total distance, any factor level can achieve a good quality solution. Nevertheless, variations in factor levels have a signi<sup>fi</sup>cant impact on the CPU time. Moreover, further analysis of the results for the total distance response indicate that, despite the statistical signi<sup>fi</sup>cance, p and T×P have the greatest impact on solution quality. Additionally, the parameter p generates the greatest positive impact in terms of accuracy while simultaneously causing the least negative impact in terms of CPU time. Thus, $p _ { c }$ was set at the high level of 0.75. On the other hand, to increase the value of T×P, it is advisable to increase T over P because of its lower computational burden (CPU time response). Thus, T was set at its high level (3000), while P was set at its low level (200).

![](/api/attachments/YHGTDZVX/fulltext/images/636d1474fbec018937e7422ffb24d56ca0d2718cb650515182ec373052befd5c.jpg)  
Fig. 5. Example of Prins split reparation strategy.

In sum, following this two-phase parameter tuning study, the values of the MA were set at p =0.10, p =0.75, P=200 and T=3000.

## 6. Clustering models

A second decision problem faced by EAAB is balancing the workload along the planning horizon, which may be achieved either by (1) assigning visits to workdays prior to the route-building phase (cluster-<sup>fi</sup>rst, route-second) or (2) assigning routes to the workdays (route-<sup>fi</sup>rst, cluster-second). This workload balancing problem can be solved by two clustering models in which a cluster represents one day of the planning horizon. The objective of these models is to concentrate the visits near a speci<sup>fi</sup>c area of the service zone in an attempt to facilitate collaboration among auditors.

## 6.1. Model 1: clustering visits into workdays

This model assigns visits to workdays prior to the route-building phase by constructing geographical clusters around client nodes that serve as centroids. The proposed model includes both a set of client nodes considered potential cluster centroids, , and a set of client <sup>I</sup>nodes to be visited during the planning horizon, $\mathcal { T } .$ Both and may contain the same elements. The parameter D denotes the number of workdays on the planning horizon used to plan all visits; and Q is the maximum number of visits assignable to the auditing crew (capacity) on a workday. Finally, $c _ { 0 , i }$ and $c _ { i , j }$ are the distances between the depot (EAAB operating center) and client node i, and between client nodes i and j, respectively. The binary decision variable, $y _ { i } ,$ takes the value of 1 if node i is selected as a cluster centroid and a value of 0, otherwise. The model also requires the de<sup>fi</sup>nition of the binary decision variable, $x _ { i , j } ,$ which takes the value of 1 if client node j is assigned to the cluster centroid i and the value of $^ { 0 , }$ otherwise. The clustering of visits into workdays is modeled as follows:

$$
\min Z _ {1} = \sum_ {i \in \mathcal {I}} \sum_ {j \in \mathcal {J}} c _ {i, j} \cdot x _ {i, j} + \sum_ {i \in \mathcal {I}} c _ {0, i} \cdot y _ {i}\tag{6}
$$

subject to

$$
\sum_ {i \in \mathcal {I}} x _ {i, j} = 1, j \in \mathcal {J}\tag{7}
$$

$$
x _ {i, j} \leq y _ {i}, i \in \mathcal {I}, j \in \mathcal {J}\tag{8}
$$

$$
\sum_ {j \in \mathcal {J}} x _ {i, j} {\leq} Q \cdot y _ {i}, i {\in} \mathcal {I}\tag{9}
$$

$$
\sum_ {i \in \mathcal {I}} y _ {i} = D\tag{10}
$$

$$
y _ {i}, x _ {i, j} \in \{0, 1 \}, i \in \mathcal {I}, j \in \mathcal {J}\tag{11}
$$

where the objective $Z _ { 1 }$ in Eq. (6) is the minimization of the sum of two terms: the distance between the cluster centroids and their assigned nodes, and the distance from the depot to all the cluster centroids. Constraint (7) guarantees that all client visits are assigned to a workday, constraint (8) avoids assigning client nodes to nodes not selected as cluster centroids, and constraint (9) guarantees that the number of visits assigned to a workday does not exceed the capacity of the auditing crew. Similarly, constraint (10) limits the total number of workdays in the planning horizon. Finally, relation (11) de<sup>fi</sup>nes the binary nature of the decision variables.

## 6.2. Model 2: clustering routes into workdays

This model assigns routes built on the routing phase to workdays by constructing clusters around the geographical gravity center of a route selected as a centroid. The proposed model therefore includes a set of routes to be clustered, as well as a set $\scriptstyle { \mathcal { T } } ^ { \prime }$ of nodes located at the <sup>R I</sup>geographical gravity centers of routes in . The parameter R denotes <sup>R</sup>the maximum number of routes schedulable on a working day, related to the number of auditors available. Finally, $c _ { r , 0 }$ and $c _ { r , i }$ are the distances between the geographical gravity center of route r and the depot (EAAB operating center), and between the gravity center of route r and node i, respectively. As in Section 6.1, the binary decision variable, $y _ { i } ,$ takes the value of 1 if node i is selected as a cluster centroid and a value of $^ { 0 , }$ otherwise. The binary decision variable, $x _ { r , i } ,$ takes the value of 1 if route r is assigned to the cluster centroid i but the value of 0, otherwise. The route clustering model follows:

$$
\min Z _ {2} = \sum_ {i \in \mathcal {I} ^ {\prime}} \sum_ {r \in \mathcal {R}} c _ {r, i} \cdot x _ {r, i} + \sum_ {i \in \mathcal {I} ^ {\prime}} c _ {0, i} \cdot y _ {i}\tag{12}
$$

subject to

$$
\sum_ {i \in \mathcal {I} ^ {\prime}} x _ {r, i} = 1, r \in \mathcal {R}\tag{13}
$$

$$
\sum_ {r \in \mathcal {R}} x _ {r, i} \leq R \cdot y _ {i}, i \in \mathcal {I} ^ {\prime}\tag{14}
$$

$$
y _ {i}, x _ {r, i} \in \{0, 1 \}, i \in \mathcal {I}, r \in \mathcal {R}\tag{15}
$$

where the objective $Z _ { 2 }$ in Eq. (12) is the minimization of the sum of the distance from the cluster centroids to the geographical gravity center of their assigned routes, plus the sum of the distance from the depot to all the cluster centroids. Constraint (13) guarantees that all routes are assigned to a workday, and constraint (14) restricts the number of routes that can be assigned to a workday. Finally, relation (15) de<sup>fi</sup>nes the binary nature of the decision variables.

## 7. Computational experiments

The experiments test four different combinations of the clustering models and routing algorithms. The two cluster-<sup>fi</sup>rst, route-second (clustering-routing) approaches — CR-C&W and CR-MA-PSS — both use Model 1 (see Section 6.1) in the clustering phase; however, in the routing phase, the former uses the distance-constrained C&W heuristic while the latter uses the MA with PSS reparation strategy. The two route-<sup>fi</sup>rst, cluster-second (routing-clustering) approaches — RC-MA-SBS and RC-MA-PSS — both use Model 2 (see Section 6.2) in the clustering phase and the common MA components described in Section 5 in the routing phase; however, as their names suggest, the <sup>fi</sup>rst uses the SBS reparation strategy, while the second uses the PSS.

We test the algorithms on ten instances ranging from 323 to 601 client nodes, built using real EAAB data from 10 weeks of operation. For all instances, the distance between clients is Euclidean; the vehicle speed is constant and equal to 28.3 km/h [2]; the planning horizon is one week and the number of available auditors for each workday is 6 (enough to ensure that all instances are feasible); and the duration of the auditors' shift is 6 h, which represents a maximum route length of L=169.8 km according to the average speed. Henceforth, the instances are named EAAB-X, where X is the number of client nodes to be visited.

The clustering phase was executed on a computer with an Intel Pentium M 725 processor running at 1596.0 MHz with 512 Mbytes of RAM, on a Windows XP Professional environment, while the routing phase was executed on a server with an Intel Xeon Woodcrest 5120 processor with 4 Gbytes of RAM, running Windows Server 64 bits. In every experiment using the MA, the algorithm was run with 20 different seeds and the reported solution corresponds to the best solution obtained in terms of total distance.

## 7.1. Performance metrics for EAAB

We report four performance metrics: total distance, CPU time, workload balance, and resource utilization. First, the total distance, calculated as $\textstyle \sum r _ { \in { \mathcal { R } } } l _ { r }$ , adds the distance covered by all the routes along <sup>R</sup>the whole planning horizon. Second, the CPU time considers the execution time of both the clustering and the routing phases. Third, the workload balance is a measure of how evenly the work is distributed along the planning horizon. In the case of EAAB, this balance is measured by the standard deviation of the fraction of visits assigned to each working day, calculated as

$$
\sigma = \sqrt {\frac {\sum_ {d = 1} ^ {D} \left(w _ {d} - \overline {{w}}\right) ^ {2}}{D}}\tag{16}
$$

where D denotes the number of workdays with planned visits, w is the fraction of visits assigned to workday d, and w<sup>—</sup> is the average fraction of visits per day. Lastly, the resource utilization is measured by the average usage factor along the planning horizon

$$
\overline {{\rho}} = \frac {\sum_ {d = 1} ^ {D} \rho_ {d}}{D}\tag{17}
$$

where $\rho _ { d }$ is the daily utilization factor, calculated as

$$
\rho_ {d} = \frac {w _ {d} \times n}{Q}\tag{18}
$$

where Q denotes the available capacity on one working day.

## 7.2. Results for EAAB instances

In terms of total distance the results show a signi<sup>fi</sup>cant improvement with respect to the current routing method used at EAAB. As Table 1 illustrates, the improvement ranges from 17.20% (EAAB-333) to

Table 1  
Performance metrics: reduction (%) in total distance with respect to the current method, CPU time (s), workload balance σ (%), resource utilization ρ̄(%)

<table><tr><td>Instance</td><td>Metric</td><td>Cur. met.</td><td>CR-C&amp;W</td><td>CR-MA-PSS</td><td>RC-MA-SBS</td><td>RC-MA-PSS</td></tr><tr><td rowspan="4">EAAB-323</td><td>Reduction</td><td></td><td>52.57</td><td>54.50</td><td>56.47</td><td>55.67</td></tr><tr><td>CPU time</td><td></td><td>99.31</td><td>1756.49</td><td>2182.49</td><td>2406.93</td></tr><tr><td>σ</td><td>34.70</td><td>10.10</td><td>10.10</td><td>22.26</td><td>18.48</td></tr><tr><td> $\bar{\rho }$ </td><td>67.08</td><td>67.08</td><td>67.08</td><td>44.72</td><td>44.72</td></tr><tr><td rowspan="4">EAAB-326</td><td>Reduction</td><td></td><td>46.01</td><td>48.71</td><td>51.85</td><td>51.99</td></tr><tr><td>CPU time</td><td></td><td>114.25</td><td>1639.12</td><td>755.41</td><td>914.05</td></tr><tr><td>σ</td><td>37.04</td><td>8.70</td><td>8.70</td><td>18.63</td><td>19.53</td></tr><tr><td> $\bar{\rho }$ </td><td>65.63</td><td>66.04</td><td>66.04</td><td>65.63</td><td>65.63</td></tr><tr><td rowspan="4">EAAB-333</td><td>Reduction</td><td></td><td>17.20</td><td>51.09</td><td>52.16</td><td>52.19</td></tr><tr><td>CPU time</td><td></td><td>114.85</td><td>2099.55</td><td>2415.82</td><td>2402.96</td></tr><tr><td>σ</td><td>31.52</td><td>13.63</td><td>13.63</td><td>19.78</td><td>19.78</td></tr><tr><td> $\bar{\rho }$ </td><td>69.17</td><td>69.38</td><td>69.38</td><td>46.11</td><td>46.11</td></tr><tr><td rowspan="4">EAAB-343</td><td>Reduction</td><td></td><td>39.80</td><td>41.72</td><td>61.77</td><td>61.62</td></tr><tr><td>CPU time</td><td></td><td>115.03</td><td>2207.43</td><td>2509.29</td><td>2692.96</td></tr><tr><td>σ</td><td>28.53</td><td>13.23</td><td>13.23</td><td>11.83</td><td>11.83</td></tr><tr><td> $\bar{\rho }$ </td><td>71.25</td><td>71.25</td><td>71.25</td><td>47.50</td><td>47.50</td></tr><tr><td rowspan="4">EAAB-381</td><td>Reduction</td><td></td><td>46.42</td><td>47.81</td><td>50.89</td><td>51.05</td></tr><tr><td>CPU time</td><td></td><td>206.85</td><td>2117.79</td><td>991.30</td><td>1118.51</td></tr><tr><td>σ</td><td>22.53</td><td>2.32</td><td>2.32</td><td>10.72</td><td>24.48</td></tr><tr><td> $\bar{\rho }$ </td><td>75.83</td><td>76.25</td><td>76.25</td><td>50.56</td><td>75.83</td></tr><tr><td rowspan="4">EAAB-426</td><td>Reduction</td><td></td><td>43.42</td><td>45.82</td><td>48.71</td><td>48.45</td></tr><tr><td>CPU time</td><td></td><td>344.41</td><td>2763.02</td><td>1386.74</td><td>1345.69</td></tr><tr><td>σ</td><td>11.49</td><td>5.91</td><td>5.91</td><td>23.28</td><td>18.96</td></tr><tr><td> $\bar{\rho }$ </td><td>86.46</td><td>87.29</td><td>87.29</td><td>57.78</td><td>57.78</td></tr><tr><td rowspan="4">EAAB-491</td><td>Reduction</td><td></td><td>52.40</td><td>54.76</td><td>55.31</td><td>55.36</td></tr><tr><td>CPU time</td><td></td><td>2439.51</td><td>5342.4</td><td>1828.49</td><td>1676.18</td></tr><tr><td>σ</td><td>0.59</td><td>0.59</td><td>0.59</td><td>15.02</td><td>9.98</td></tr><tr><td> $\bar{\rho }$ </td><td>99.17</td><td>99.58</td><td>99.58</td><td>55.24</td><td>66.11</td></tr><tr><td rowspan="4">EAAB-510</td><td>Reduction</td><td></td><td>47.35</td><td>48.73</td><td>52.45</td><td>52.47</td></tr><tr><td>CPU time</td><td></td><td>535.35</td><td>3758.89</td><td>5739.44</td><td>4876.63</td></tr><tr><td>σ</td><td>23.93</td><td>13.30</td><td>13.30</td><td>15.99</td><td>16.00</td></tr><tr><td> $\bar{\rho }$ </td><td>70.69</td><td>70.83</td><td>70.83</td><td>70.69</td><td>70.69</td></tr><tr><td rowspan="4">EAAB-551</td><td>Reduction</td><td></td><td>47.45</td><td>50.88</td><td>48.61</td><td>48.41</td></tr><tr><td>CPU time</td><td></td><td>638.03</td><td>3142.61</td><td>2270.54</td><td>1882.23</td></tr><tr><td>σ</td><td>23.77</td><td>8.01</td><td>8.01</td><td>19.46</td><td>16.39</td></tr><tr><td> $\bar{\rho }$ </td><td>70.83</td><td>71.39</td><td>71.39</td><td>70.97</td><td>53.23</td></tr><tr><td rowspan="4">EAAB-601</td><td>Reduction</td><td></td><td>44.65</td><td>46.74</td><td>48.26</td><td>48.38</td></tr><tr><td>CPU time</td><td></td><td>1365.11</td><td>4557.76</td><td>2912.26</td><td>2240.68</td></tr><tr><td>σ</td><td>14.18</td><td>7.22</td><td>7.22</td><td>11.20</td><td>11.20</td></tr><tr><td> $\bar{\rho }$ </td><td>80.28</td><td>80.69</td><td>80.69</td><td>80.28</td><td>80.28</td></tr><tr><td rowspan="3">Average</td><td>Reduction</td><td></td><td>43.73</td><td>49.08</td><td>52.65</td><td>52.56</td></tr><tr><td>σ</td><td>22.83</td><td>8.30</td><td>8.30</td><td>16.82</td><td>16.66</td></tr><tr><td> $\bar{\rho }$ </td><td>75.64</td><td>75.98</td><td>75.98</td><td>58.95</td><td>60.79</td></tr><tr><td rowspan="3">Std. Dev.</td><td>Reduction</td><td></td><td>10.07</td><td>3.96</td><td>4.22</td><td>4.14</td></tr><tr><td>σ</td><td>11.31</td><td>4.51</td><td>4.51</td><td>4.57</td><td>4.55</td></tr><tr><td> $\bar{\rho }$ </td><td>10.41</td><td>10.53</td><td>10.53</td><td>12.32</td><td>12.79</td></tr></table>

61.77% (EAAB-343) — 200 km to 325 km in terms of absolute distance — with an average between 43.73% (CR-C&W) and 52.65% (CR-MA-SBS). These results indicate that by using EAAB-VRT the company could reduce the operating costs related to the route length (e.g., fuel cost) by nearly 50%.

The results also show that routing–clustering approaches are the best alternative for EAAB in terms of total distance. In 9 out of 10 instances these methods obtained the best solution. In addition, the average reduction for the routing–clustering approaches (52.61%) is larger than that obtained by the clustering–routing approaches (46.41%).

Focusing on the best-performing routing–clustering approaches, a further analysis on the reparation strategies (see last two columns of Table 1) shows that in 6 out of 10 times, the PSS dominates the SBS. However, in terms of total distance, this difference might not be signi<sup>fi</sup>cant. With regard to instance size and computational time, on instances with less than 400 client nodes, the SBS strategy results in shorter computational times than does the PSS; however, on larger instances (over 400 nodes), the PSS performs better. This observation tips the balance towards PSS over SBS in terms of computational scalability.

In terms of CPU time the clustering–routing approaches outperform the routing–clustering approaches. Speci<sup>fi</sup>cally, the CR-C&W approach reports the best CPU time for all instances other than EAAB-491. However, according to the person responsible for the auditing routes at EAAB, the increment in computing time of the routing– clustering algorithms is offset by the potential bene<sup>fi</sup>ts in terms of total distance discussed previously. Therefore, from the company's point of view, the routing–clustering approaches are affordable alternatives in terms of CPU time.

A good balance in the workload distribution along the planning horizon translates into low values of σ. As Table 1 shows, the clustering–routing approaches produce solutions with better workload balance. This <sup>fi</sup>nding can be explained by the fact that Model 1 (see Section 6.1) tends to generate clusters (workdays) with a homogeneous number of visits, whereas Model 2 (see Section 6.2) assigns a variable number of routes with a dissimilar number of visits to every workday. Thus, the clustering–routing approaches dominate not only in terms of number of best solutions obtained (i.e., 9 out of 10) but also in terms of average value of σ (8.30%) and its variability (4.51%).

Finally, a high utilization of available resources translates into high values of ρ<sup>—</sup>. As with workload balance, the clustering–routing approaches dominate (see ρ<sup>—</sup> in Table 1). Similarly to the case of workload distribution, Model 1 (see Section 6.1) forces the execution of the auditing visits on a minimal number of workdays, whereas Model 2 (see Section 6.2) includes no incentive or constraint(s) to guarantee the optimal use of available capacity.

In sum, EAAB-VRT offers the company a wide range of alternatives for designing their auditing routes. Each alternative satis<sup>fi</sup>es different organizational needs, with different tradeoffs between low operational costs, high resource utilization, quick planning response, and a balanced workload.

## 7.3. Literature benchmarks

To evaluate the performance of the proposed MA described in Algorithm 1 on classical benchmark problems, we adapted the DCVRP instances of CMT and LSVRP by removing the capacity constraint. We conducted 20 independent runs of the MA with each reparation strategy (SBS and PSS) on 17 instances ranging from 51 to 481 nodes. Since no results exist for this modi<sup>fi</sup>ed benchmark instances, we measured the effectiveness of the algorithms by computing the average improvement relative to the best solution of the initial population. The results show that the memetic effort generates an average improvement of 6.10% and 6.68% with the SBS and PSS reparation strategies, respectively. These <sup>fi</sup>ndings are encouraging since the average improvement of the best known solutions with respect to the results of the original C&W heuristic on the CMT problems is 6.71% [10] and 10.94% on the LSVRP instances [30]. Furthermore, a closer look to the survey of Cordeau et al. [11] on metaheuristics for the VRP supports the fact that the type of MAs embedded in EAAB-VRT are quite competitive in terms of CPU time. Last, but not least, the proposed MA seems to scale well as the problem size increases. This is a desirable property due to the fact that the EAAB instances are within the range of large scale vehicle routing problems.

## 8. Conclusions

This paper presents the design and implementation of EAAB-VRT an evolutionary-based decision support system, targeted to solve a distance-constrained vehicle routing problem at a public utility in Colombia. The proposed system integrates commercial solutions like SAP/R3 and ArcGIS with a customized routing module. The routing algorithms embedded in the system include a modi<sup>fi</sup>ed Clarke and Wright savings heuristic and a MA in which solutions are encoded using the genetic vehicle representation. Because the genetic operators produce infeasible children, we propose two different reparation strategies, the <sup>fi</sup>rst based on a bin-packing procedure; the second on Prins's split procedure [39]. EAAB-VRT also includes two clustering models based on integer programming to balance the workload along the planning horizon. The <sup>fi</sup>rst model allocates visits to workdays prior to a route-construction phase; the second assigns routes to the workdays following the route-construction phase.

The system was tested on ten real-world DVRP instances ranging from 323 to 601 nodes. Four different combinations of the routing algorithms and the clustering models were implemented: two cluster-<sup>fi</sup>rst, route-second approaches and two route-<sup>fi</sup>rst, cluster-second approaches. These tests report four performance metrics: total distance, CPU time, workload balance, and average resource utilization. The results show an average improvement of 49.50% (arithmetic mean of row Average reduction in Table 1) respect to the current routing method used at the utility, which would translate into savings of up to 200 km in the weekly routes (i.e., reduced fuel consumption). CPU times ranged from 100 s to 1.6 h depending on the instance size and the solution approach. The two cluster-<sup>fi</sup>rst, route-second approaches improve the workload balance over the current method in 9 out of 10 instances, while the cluster-<sup>fi</sup>rst, route-second approaches produce a slight improvement (0.34% on average) in the resource utilization factor of the current routing method.

Experiments on a modi<sup>fi</sup>ed set of well known benchmark instances for the DCVRP show that the proposed memetic search results on average improvements of 6.39% with respect to the best solution in the initial population.

The bene<sup>fi</sup>ts for the utility include not only the reduction of the total distance required to complete the auditing operation, but also streamlining the planning process. In addition, the development of EAAB-VRT did not represent additional IT costs for EAAB since the architecture of the system was based existing on software owned by the utility and software components developed by the authors.

Research currently underway include the development of multiobjective algorithms that simultaneously optimize not only total distance, but workload balance and resource utilization. Another goal in the short term is to identify routing problems faced by other business units at EAAB that could be handled by (extensions of) EAAB-VRT.

## Acknowledgments

The authors would like to thank the staff of the Dirección Comercial - Zona 2 at EAAB for their valuable help; Fair Isaac Corporation for providing us with licenses of the Xpress-MP optimization suite through the Academic Partner Program; professors Christelle Guéret and Bruno Castanier at École des Mines de Nantes for their generosity, insight and support; and the referees for their insightful comments and suggestions. This project was partially funded by grants 471-2007 from COLCIENCIAS/SENA and 02-2007 from CIFI at Universidad de los Andes.

## References

[1] E. Alba, B. Dorronsoro, Computing nine new best-so-far solutions for capacitated VRP with a cellular genetic algorithm, Information Processing Letters 98 (2006) 225–230.

[2] Alcaldía Mayor de Bogotá. Observatorio de movilidad. http://www.bogota.gov.co portel/libreria/php/decide.php?patron=01.010310 Last access: April 19 2008.

[3] P. Augerat. Approche polyèdrale du problème de tournées de véhicules. Ph.d thesis, Institut National Polytechnique de Grenoble-INPG, 1995.

[4] B.M. Baker, M.A. Ayechew, A genetic algorithm for the vehicle routing problem, Computers and Operations Research 30 (5) (2003) 787–800.

[5] C. Basnet, L. Foulds, M. Igbaria, Fleet manager: a microcomputer-based decision support system for vehicle routing, Decision Support Systems 16 (3) (1996) 195-207

[6] O. Bräysy, M. Gendreay, Vehicle routing problem with time windows, Part II: Metaheuristics, Transportation Science 39 (1) (2005) 119–139.

[7] N. Christo<sup>fi</sup>des, S. Eilon, An algorithm for the vehicle dispatching problem Operational Research Quarterly 20 (3) (1969) 309–318

[8] N. Christo<sup>fi</sup>des, A. Mingozzi, P. Toth, The vehicle routing problem, in: N. Christo<sup>fi</sup>des, A. Mingozzi, P. Toth, C. Sandi (Eds.), Combinatorial Optimization, Wiley, 1979, pp. 315–338.

[9] G. Clarke, J.V. Wright, Scheduling of vehicles from a central depot to a number of delivery points, Operations Research 12 (4) (1964) 568–581.

[10] J.F. Cordeau, M. Gendreau, G. Laporte, J.Y. Potvin, F. Semet, A guide to vehicle routing heuristics, Journal of the Operational Research Society 53 (5) (2002) 512–522.

[11] J.F. Cordeau, M. Gendreau, A. Hertz, G. Laporte, G. Sormany, New heuristics for the VRP, in: A. Langevin, D. Riopel (Eds.), Logistics systems: design and optimization, Springer, 2005, pp. 279–297.

[12] J.F. Cordeau, G. Laporte, M. Savelsbergh, D. Vigo, Vehicle routing, in: C. Barnhart, G. Laporte (Eds.), Handbooks in Operations Research and Management Science: Transportation, Elsevier, 2006, pp. 367–428.

[13] Fair Isaac Corporation http://www.dashoptimization.com Last access: July 17, 2008.

[14] A. Eiben, R. Hinterding, Z. Michalewicz, Parameter control in evolutionary algorithms, IEEE Transactions on Evolutionary Computation 3 (22) (1999) 124–141.

[15] S. Eom, The intellectual structure of decision support systems (1971 – 1989), Decision Support Systems 10 (1) (1993) 19–35.

[16] J. Faulin, P. Sarobe, J. Simal, The DSS LOGDIS optimizes delivery routes for FRILAC's frozen products, Interfaces 35 (3) (2005) 202–214.

[17] M.L. Fisher, R. Jaikumar, A generalized assignment heuristic for the vehicle routing problem, Networks 11 (2) (1981) 109–124.

[18] S.P. Gayialis, I.P. Tatsiopoulos, Design of an IT-driven decision support system for vehicle routing and scheduling, European Journal of Operational Research 152 (2) (2004) 382–398.

[19] M. Gendreau, A. Hertz, G. Laporte, A tabu search heuristic for the vehicle routing problem, Management Science 40 (10) (1994) 1276–1290.

[20] M.K. Ghose, A.K. Dikshit, S.K. Sharma, A GIS based transportation model for solid waste disposal: a case study on Asansol municipality, Waste Management 26 (11) (2006) 1287–1293.

[21] B.E. Gillet, L.R. Miller, A heuristic algorithm for the vehicle dispatch problem, Operations Research 22 (2) (1974) 340–349.

[22] B. Golden, E. Wasil, J. Kelly, I. Chao, The impact of metaheuristics on solving the vehicle routing problem: algorithms, problem sets, and computational results, in: T. Crainic, G. Laporte (Eds.), Fleet management and logistics, Kluwer, 1998, pp. 33–56.

[23] C. Groër, B. Golden, E. Wasil, The balanced billing cycle vehicle routing problem, Route 2007, International Workshop on Vehicle Routing and Transportation, 2007, Atlanta, GA. USA.

[24] H. Jung, K. Lee, W. Chun, Integration of GIS, GPS, and optimization technologies for the effective control of parcel delivery service, Computers and Industrial Engineering 51 (1) (2006) 154–162.

[25] G. Laporte, M. Desrochers, Y. Norbert, Two exact algorithms for the distanceconstrained vehicle routing problem, Networks 14 (1) (1984) 161–172.

[26] C.L. Li, D. Simchi-Levi, M. Desrochers, On the distance-constrained vehicle routing problem, Operations Research 40 (4) (1992) 790–799.

[27] F. Li, B. Golden, E. Wasil, Very large-scale vehicle routing: new test problems, algorithms, and results, Computers and Operations Research 32 (5) (2005) 1165–1179.

[28] A.L. Medaglia, E. Gutiérrez, JGA: an object-oriented framework for rapid development of genetic algorithms, in: Jean-Phillipe Rennard (Ed.), Handbook of Research on Nature Inspired Computing for Economics and Management, Idea Publishing Group, 2006.

[29] J. E. Mendoza, A. L. Medaglia, and N. Velasco. RoutePlotter: MS Excel add-in for visualization and analysis of vehicle routes. http://copa.uniandes.edu.co/soft-optirouteplotter,html Last access: July 11. 2007.

[30] I.E. Mendoza, C. Guéret, A.I, Medaglia, N. Velasco, I.G. Villegas, ICW: an obiectoriented framework for the rapid development of vehicle routing heuristics based on savings, Congreso Latino Ibero Americano de Investigación de Operaciones (CLAIO), Cartagena, Colombia, 2008

[31] D. Mester, O. Bräysy, Active guided evolution strategies for large-scale capacitated vehicle routing problems, Computers and Operations Research 34 (10) (2007) 2964–2975.

[32] P. Moscato, Memetic algorithms: a short introduction, in: D. Corne, M. Dorigo, F. Glover (Eds.), New ideas in optimization, McGraw-Hill, 1999, pp. 219–234.

[33] M. Nussbaum, M. Sepulveda, A. Cobian, J. Gaete, J. Cruz, A fuel distribution knowledge-based decision support system, International Journal of Management Science 25 (2) (1997) 225–234.

[34] I. Osman, Metastrategy simulated annealing and tabu search algorithms for the vehicle routing problem, Annals of Operations Research 41 (4) (1993) 421–451.

[35] H. Paessens, Saving algorithms for the vehicle routing problem, European Journal of Operational Research 34 (3) (1988) 336–344.

[36] G. Parker, Deterministic scheduling theory, Chapman & Hall, London, UK, 1995.

[37] F.B. Pereira, J. Tavares, P. Machado, E. Costa, GVR: a new genetic representation for the vehicle routing problem, Proceedings of AICS 2002 — 13th Irish Conference on Arti<sup>fi</sup>cial Intelligence and Cognitive Science, 2002.

[38] N. Perrier, A. Langevin, J. Campbell, A survey of models and algorithms for winter road maintenance. part IV: vehicle routing and <sup>fl</sup>eet sizing for plowing and snow disposal Computers and Operations Research 34 (1) (2007) 258–294

[39] C. Prins, A simple and effective evolutionary algorithm for the vehicle routing problem, Computers and Operations Research 31 (12) (2004) 1985–2002.

[40] J. Ray, A web-based spatial decision support system optimizes routes for oversize/ overweight vehicles in Delaware Decision Support Systems 43 (4) (2007 1171–1185.

[41] M. Reinmann, K. Doerner, R.F. Hartl, D-Ants: savings based ants divide and conquer the vehicle routing problem, Computers and Operations Research 31 (4) (2004) 563–591.

[42] C. Reeves, Genetic algorithms, in: F. Glover, A. Kochenberg (Eds.), Handbook of Metaheuristics, Kluwer Academic Publishers, 2003, pp. 55–82.

[43] M. Solomon, Algorithms for the vehicle routing and scheduling problem with time window constraints, Operations Research 35 (2) (1987) 254–265.

[44] H. Stern, M. Dror, Routing electric meter readers, Computers and Operations Research 6 (4) (1979) 209–223.

[45] M.M. Syslo, N. Deo, J.S. Kowalik, Discrete Optimization Algorithms, Prentice-Hall Englewood Cliffs, NJ, 1983.

[46] E.D. Taillard, Parallel iterative search methods for vehicle routing problems, Networks 23 (8) (1993) 661–673.

[47] J. Tavares, F.B. Pereira, P. Machado, E. Costa, On the in<sup>fl</sup>uence of GVR in Vehicle Routing, Proceedings of the 2003 ACM Symposium on Applied Computing, SAC, Melbourne FL, USA, 2003, pp. 753–758.

[48] P. Toth, D. Vigo, An overview of vehicle routing problems, in: P. Toth, D. Vigo (Eds.), The Vehicle Routing Problem, SIAM, 2002, pp. 1–51.

[49] P. Toth, D. Vigo, The granular tabu search and its application to the vehicle routing problem, Journal on Computing 5 (4) (2003) 333–346.

[50] A. Van Breedam. An analysis of the behavior of heuristics for the vehicle routing problem for a selection of problems with vehicle related, customer-related, and time related constraints. PhD thesis, University of Antwerp, RUCA, Belgium, 1994.

[51] D. Weigel, B. Cao, Applying GIS and OR techniques to solve Sears technician dispatching and home delivery problems, Interfaces 29 (1) (1999) 112–130.

[52] J. Wunderlich, M. Collete, L. Levy, L. Bodin, Scheduling meter readers for southern California gas company, Interfaces 22 (3) (1992) 22–30.

[53] www.citymayors.com. The largest cities in the world by land area, population and density. http://www.citymayors.com/statistics/largest-cities-population125.html Last access: July 11, 2008.

Jorge E. Mendoza, M.Sc., Ph.D. (student) Holds a M.Sc. in Industrial Engineering (2006) from Universidad de los Andes and a B.Sc. in Industrial Engineering (2004) from Universidad Industrial de Santander (Bucaramanga, Colombia). Currently he is a joint Ph.D. student in the Department of Industrial Engineering at Universidad de los Andes and the Ecole des Mines de Nantes (France). His research interests include scheduling, vehicle routing problems, and software development.

Andrés L. Medaglia, Ph.D. He is an Associate Professor of Industrial Engineering at the Universidad de los Andes (Bogotá, Colombia) and director of the research center Centro para la Optimización y Probabilidad Aplicada (COPA). He holds a Ph.D. (2001) in Operations Research from North Carolina State University (USA). Since 1999 and until the completion of his postdoctoral fellowship, he worked as an optimization specialist developing Web-based decision support systems for the Supply Chain Center at SAS Institute Inc. His current research interests include multiobjective evolutionary optimization and optimization applications to logistics and project selection. His research has been published in Annals of Operations Research, Automation in Construction, Building and Environment, European Journal of Operational Research, Fuzzy Sets and Systems, Interfaces, Journal of Heuristics, Socio-Economic Planning Sciences, and The Engineering Economist. He currently serves in the editorial boards of the Journal of Industrial and Management Optimization. MSEM. and The Open Operational Research Journal as Vice-president of the Latin-Ibero American Federation of Operations Research Societies (ALIO). url: http://wwwprof.uniandes.edu.co/ \~amedagli.

Nubia Velasco, Ph.D. Holds a Ph.D. (2006) in Applied Production and Automation (in French, Automatique et Productique Appliqués) at the Université de Nantes in France. Currently she is an Assistant Professor of Industrial Engineering at the Universidad de los Andes. Her research interests include evolutionary optimization, metaheuristics and optimization applied to logistics, and particularly, to the vehicle routing problem and health care systems.
