---
otero_id: 1518
otero_key: "6FCJ3DWT"
title: "A dynamic shipment matching problem in hinterland synchromodal transportation"
authors: "Wenjing Guo; Bilge Atasoy; Wouter Beelaerts van Blokland; Rudy R. Negenborn"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113289"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dynamic shipment matching problem in hinterland synchromodal transportation

![](/api/attachments/6FCJ3DWT/fulltext/images/d92ad045c219322a10a3117b8b54b56a87d10e724c3248fc7ed8e29008528407.jpg)

Wenjing Guo , Bilge Atasoy, Wouter Beelaerts van Blokland, Rudy R. Negenborn

Department of Maritime and Transport Technology, Delft University of Technology, Mekelweg 2, 2628CD Delft, the Netherland

A R T I C L E I N F O

Keywords: Hinterland synchromodal transportation Dynamic shipment matching Rolling horizon approach Heuristic algorithm

## A B S T R A C T

Hinterland intermodal transportation is the movement of containers between deep-sea ports and inland terminals by using trucks, trains, barges, or any combination of them. Synchromodal transportation, as an extension of intermodal transportation, refers to transport systems with dynamic updating of plans by incorporating real time information. The trend towards spot markets and digitalization in hinterland intermodal transportation gives rise to online synchromodal transportation problems. This paper investigates a dynamic shipment matching problem in which a centralized platform provides online matches between shipment requests and transport services. We propose a rolling horizon approach to handle newly arrived shipment requests and develop a heuristic algorithm to generate timely solutions at each decision epoch. The experiment results demonstrate the solution accuracy and computational eficiency of the heuristic algorithm in comparison to an exact algorithm. The proposed rolling horizon approach outperforms a greedy approach from practice in total costs under various scenarios of the system.

## 1. Introduction

Hinterland intermodal transportation is the movement of containers between deep-sea ports and inland terminals by using trucks, trains, barges, or any combination of them [17]. Compared with unimodal transportation, intermodal transportation has the flexibility to use different modes considering the specific characteristics of containers and in turn achieves better performance in costs, delays, and emissions [6]. However, due to the utilization of multiple modes, operating an intermodal transportation system is very complex. In intermodal transportation, barge and train services normally follow fixed time schedules and have limited free capacity [6]. Conversely, truck services are usually not scheduled and have time-dependent travel times as a result of road trafic congestion [18]. Therefore, constraints such as time compatibility between diferent services and capacity limitations of barge and train services need to be considered in intermodal transport planning.

Synchromodal transportation, as an extension of intermodal transportation, refers to transport systems with dynamic updating of plan ning by incorporating real-time information [9]. The trend towards spot markets and digitalization in hinterland intermodal transportation in creases the need for such online synchromodal transportation problems. In the literature, most of the existing studies assume that container shipments are only collected from large shippers based on long-term contracts. These contractual shipment requests are often fixed and known over a given planning period. Recently, quite a few studies [e.g.,21,22] have pointed out the trend towards spot markets in container transportation. Diferent from the former contracted requests, spot shipment requests arrive in real-time and require receiving transport solutions as soon as possible. Thanks to the development of digitalization and advanced information and communication technologies in logistic industries, information can be collected in real-time, and decisions can be made online [14]. Nevertheless, these new trends also introduce complexity in intermodal transport planning, unveiling the need for decision support systems adapted to dynamic contexts.

In this paper, we investigate a dynamic shipment matching (DSM) problem in which a platform provides online matches between shipment requests and transport services. We consider an online synchromodal matching platform that receives contractual and spot shipment requests from shippers, and receives transport services from carriers, as shown in Fig. 1. Shippers are the entities that are searching for services to transport their shipments. Examples of shippers include freight forwarders and ocean carriers. Carriers are the entities that provide transport services. Carriers could be truck, train or barge companies. We consider a network operator as the owner of the platform. A network operator could be a logistics service provider or an alliance formed by multiple carriers. The recent developments in information technologies such as cloud computing and Internet of Things allow realtime information sharing and container tracking, which facilitates the adoption of such a platform in practice.

![](/api/attachments/6FCJ3DWT/fulltext/images/a3911dacc3b0feafafd75c64b13194d1e82d5f961e442435d718aed03a6166d8.jpg)  
Fig. 1. Illustration of an online synchromodal matching platform. The platform provides online matches between shipment requests received from shippers and transport services received from carriers thanks to the developed rolling horizon approach.

The objective of the platform is to minimize the total cost of matching shipment requests and transport services over a given plan ning horizon. Due to the capacity limitation of barge and train services, decisions made for current requests may influence the decisions for future requests. Therefore, dynamic approaches that create online matching decisions for current requests are required. In this paper, we design a rolling horizon approach to handle dynamically revealed shipment requests and develop a heuristic algorithm to solve the DSM problem in a computationally eficient way.

The remainder of this paper is structured as follows. We discuss the relevant literature in Section 2. In Section 3, we formally describe the DSM problem. In Section 4, we explain the implementation of dynamic approaches. In Section 5, we present optimization algorithms. In Section 6, we describe the generation of instances and present the experiment results. Finally, in Section 7, we provide concluding remark and directions for future research.

## 2. Literature review

Over the past decades, diferent freight transport concepts have been proposed in the literature and in the industry: multimodality, in. termodality, co-modality, and synchromodality [9]. Although these concepts are often used interchangeably, there are subtle diferences between these terms: multimodality focuses on the utilization of mul. tiple modes; intermodality emphasizes the integration between dif ferent modes by using standard loading units; co-modality aims to have eficient utilization of resources; synchromodality, as an extension of intermodality, adds dynamic updating of transport plans over a network to benefit from real-time information [1]. In this section, the studies related to the DSM problem have been divided into two categories: hinterland intermodal transportation and synchromodality.

## 2.1. Hinterland intermodal transportation

Hinterland intermodal transportation is the provision of eficient, reliable, and sustainable services through integrated strategic and tactical planning at a network level. Strategic planning concerns the design of transportation network topologies, such as direct link, corridor, or hub-and-spoke [5]. Konings et al. [10] investigate the benefits of a huband-spoke network for hinterland transportation in turnaround times, waiting times, and the reliability of barge services. Containers at a seaport terminal that have diferent destinations in the hinterland would be transported together to the hub and after being regrouped and bundled with containers originate from other seaport terminals would continue their trip to their inland destination.

Tactical planning refers to optimally utilizing the given network by choosing transportation services, allocating their capacity to customer demands, and planning their itineraries and frequency [17]. Bhattacharya et al. [3] propose a mixed integer programming model to opti mize schedules for an intermodal transport network by taking into account the road trafic flow estimation. Zuidwijk and Veenstra [23] propose a single period model to allocate containers to a truck or barge and schedule the barge departure time considering container release time uncertainty and service transit time uncertainty. Crainic et al. [4] propose a service network design model to decide the optimal schedules for the services operated by a fleet of shuttles on the railway network connecting seaport terminals and inland terminals. Demir et al. [6] investigate a service network design problem with travel time uncertainty to decide on the routing of containers and the departure time of transport services.

## 2.2. Synchromodality

While intermodality focuses on ofline planning in which all forms of input information are required in advance and decisions are made before the start of transportation, synchromodality emphasizes online planning in which real-time information about the current state of the transport system can be taken into account in online planning processes [7]. Specifically, synchromodal transport planning deals with dynamic events that are not explicitly addressed in intermodal transportation, including the representation of real-time data, decisions, and system states [5]. The most common dynamic events are the arrival of new shipment requests, but container flows and travel times are possible dynamics as well.

In the literature, Fazi et al. [8] develop a decision support system for the optimal allocation of import containers to a heterogeneous fleet composed of barges and trucks. van Riessen et al. [19] design a decision tree to derive real-time decision rules for suitable allocation of containers to services. Rivera and Mes [16] propose an algorithm based on approximate dynamicm programming to assign newly arrived con tainers to either a barge or a truck. Although the above studies con sidered the utilization of multiple modes, none of them take into account the transshipment operations between diferent services. Research that models transshipment in synchromodal transportation, such as Li et al. [11] and Qu et al. [15], are usually designed for container flows. However, in practice, shippers would like to receive their shipments as a whole. Therefore, in this paper, we investigate the DSM problem from shipment requests' perspective, namely, decisions are designed as binary variables indicating the allocation of a specific shipment request to a specific service. Mes and Iacob [12] propose a greedy approach to select the cheapest services for dynamically arrived shipment requests but without the consideration of road trafic congestions. Due to the limited capacity of road infrastructures, trafic congestions exist during several periods of a day [18]. The variation of road travel times has been well investigated in the literature and therefore can be incorporated in the online synchromodal matching process.

## 2.3. Contributions

In the literature, the work most similar to our work is Li et al. [11], which proposes a rolling horizon approach to control container flows in a hinterland intermodal network by considering time-dependent truck travel times and time-schedules for trains and barges. In contrast to our work, Li et al. [11] focuses on aggregated container flows instead of specific shipment requests with time windows, and therefore uses the value of time instead of delay costs in the objective function to push containers move to their destinations.

The main contributions of this paper are as follows. First, we propose a rolling horizon approach to handle newly arrived shipment requests. The implementation of the rolling horizon approach relies on an optimization algorithm that can generate timely matching decisions at each decision epoch. In particular, we develop a heuristic algorithm to solve the DSM problem. Third, we conduct extensive experiments to assess the performance of the heuristic algorithm in comparison to an exact algorithm, and the performance of the rolling horizon approach in comparison to a greedy approach from practice. Briefly, we design, operationalize and validate an online matching platform in the context of synchromodal transportation.

## 3. Problem description

Let R be the set of shipment requests. Each shipment request $r \in R$ is characterized by its announce time $T _ { r } ^ { \mathsf { a n n o u n c e } } \left( \mathrm { i . e . } \right.$ , the time when the platform receives the request), release time ${ \cal T } _ { r } ^ { \mathrm { r e l e a s e } } \left( \mathrm { i } . \mathrm { e } . \right.$ ., the time when the shipment is available for hinterland transportation) at origin terminal $o _ { r } ,$ , due time $T _ { r } ^ { \mathrm { { d u e } } } ( { \mathrm { i } } . { \mathrm { e } } .$ , the time that the shipment needs to be delivered) at destination terminal $d _ { r }$ and container volume $q _ { r } \left( \mathrm { i . e . } \right.$ , the number of containers). Delay in delivery is available but with a delay cost coeficient per container per hour overdue $c _ { r } ^ { \mathrm { \ d e l a y } }$ . The lead time of shipment request r is represented as, $L D _ { r } = \Gamma _ { r } ^ { \mathrm { d u e } } \ : - \ : \Gamma _ { r } ^ { \mathrm { r e l e a s e } }$

Shipment requests can be divided into two groups: contractual requests $R ^ { \mathrm { c o n t r a c t } }$ and spot requests $R ^ { \mathrm { { s p o t } } }$ . For a contractual request $r \in R ^ { \mathrm { c o n t r a c t } }$ , the network operator has long-term contracts with ship pers. Therefore, the announce time of contractual request r is, $T _ { r } ^ { \mathrm { a n n o u n c e } } { = } 0 .$ . All the information $\{ o _ { r } , \ d _ { r } , \ q _ { r } , \ r _ { r } ^ { \mathrm { { r e l e a s e } } } , \ r _ { r } ^ { \mathrm { { d u e } } } , \ c _ { r } ^ { \mathrm { { d e l a y } } } \}$ is known in a given planning horizon. Conversely, for a spot request $r \in R ^ { \mathrm { s p o t } }$ , the platform receives the request from spot markets in realtime. The information of the spot request $\{ o _ { r } , \ d _ { r } , \ q _ { r } , \ r _ { r } ^ { \mathrm { { r e l e a s e } } } , \ r _ { r } ^ { \mathrm { { d u e } } } ,$ $c _ { r } ^ { \mathrm { \tiny ~ d e l a y } } \}$ is unknown before its announce time.

Let S be the set of transportation services. According to the type of modes, services can be divided into two groups: time-scheduled barge and train services, and departure time flexible truck services.

Barge and train services have limited capacity and fixed time schedules but can help generating economies of scale. Each barge or train service $s \in S ^ { \mathrm { b a r g e } } \cup S ^ { \mathrm { t r a i n } }$ is characterized by its origin terminal $o _ { s } ,$ destination terminal $d _ { s } ,$ free capacity in terms of loading units $( \mathrm { i . e . }$ containers) $Q _ { s } ,$ , departure time (at origin terminal) $T D _ { s } ,$ arrival time (at destination terminal) $T \boldsymbol { A } _ { s } ,$ transport cost $c _ { s } ,$ and generation of carbon emissions $e _ { s } .$

Truck services have unlimited capacity, flexible departure times, and time-dependent travel times $t _ { s } ^ { \mathrm { \ t r u c k } } ( \gamma ) = \theta _ { s } ^ { \ m } \gamma \ + \ \eta _ { s } ^ { \ m } , \forall \ \gamma \in T ^ { m }$ , as shown in Fig. 2. Here, we let $\gamma$ be the departure time of truck services, and represents the set of time periods within a day. A time period can be defined by two consecutive breakpoints. Let $t _ { s } ^ { \mathrm { t r u c k } }$ be the travel time at non-peak periods, α and $\beta$ be trafic congestion coeficients. For time period $T ^ { 2 } \ = \ [ b _ { 2 } , \ b _ { 3 } ]$ , given the values $\tilde { b _ { 2 } } , \ b _ { 3 } , \ t _ { s } ^ { \mathrm { t r u c k } } , \ \alpha t _ { s } ^ { \mathrm { t r u c k } }$ , we can calculate the slope θ of the function and the intersection η with the yaxis. Each truck service $s \in S ^ { \mathrm { t r u c k } }$ is characterized by its origin $o _ { s } ,$ destination $d _ { s } ,$ time-dependent travel time $t _ { s } ^ { \mathrm { t r u c k } } ( \gamma )$ , transport cost $c _ { s } ,$ and generation of carbon emissions $e _ { s } .$

![](/api/attachments/6FCJ3DWT/fulltext/images/5b1c2467904a57f5110fe6c8bc8e10122067ecd1b21da9cd8cc345f800c50b2e.jpg)  
Fig. 2. Time-dependent travel times of truck services.

As spot shipment requests arrive in real-time, the platform provides online matches between shipment requests and transport services. A match is defined as a combination of a shipment and a service, which means the shipment will be transported by the service from the service's origin to the service's destination. Each shipment might be matched with multiple services, each service might be matched with multiple shipments. An illustrative example of shipment matching in synchromodal transportation is shown in Fig. 3. Matching decision 〈r1, s4〉 means shipment r1 will be transported by service s4 from terminal 1 to terminal $5 ;$ matching decision $\langle r 2 , s 1 \rangle , \langle r 2 , s 3 \rangle , \langle r 2 , s 7 \rangle$ means shipment $r 2$ will be transported by service combination [s1,s3, s7] from terminal 1 to terminal 6.

To model this problem, we make the following five assumptions. First, we assume the platform is centralized and the contracts among carriers, shippers, terminal operators, and the network operator have been made. Therefore, we do not consider fairness, pricing, and contracting strategies among players. Second, we do not model the accept/ reject decisions and consider only the accepted spot requests by the platform. Third, we assume that shippers require their shipments to be transported as a whole, thus shipments are unsplittable. Fourth, we assume shippers require to receive matching decisions before the release time of shipments. Therefore, the response time of request r is $\Delta T _ { r } ~ = ~ { \Gamma _ { r } ^ { \mathrm { \scriptsize ~ r e l e a s e } } } ~ - ~ { \Gamma _ { r } ^ { \mathrm { \scriptsize ~ a n n o u n c e } } }$ . Fifth, we assume the capacity of truck services is unlimited. Therefore, the synchromodal matching system always has feasible matches for newly arrived shipment requests. Last, we do not consider stochasticity of travel times in this paper. Instead, we use deterministic travel times for all services, and consider timedependent travel times for trucks, since the road trafic patterns have been well investigated in the literature [18].

![](/api/attachments/6FCJ3DWT/fulltext/images/8cffc28920970bc80496b84509d2070ca781e569a4aea46652a5703174d43741.jpg)  
Fig. 3. Illustrative example of shipment matching in synchromodal transportation.

![](/api/attachments/6FCJ3DWT/fulltext/images/a96c86fc52336748a0517489661fffff3f0daabad31d40c301f021d45a9609de.jpg)  
Fig. 4. Flow chart of the greedy approach.

## 4. Dynamic approaches

To handle newly arrived shipment requests, we need to design methodologies that can update the decisions based on dynamically revealed information. This paper proposes a rolling horizon approach for the DSM problem and uses a greedy approach as the benchmark. While the greedy approach makes matching decisions for each newly arrived shipment request and the decisions are fixed once they are made, the rolling horizon approach makes decisions at fixed time points for all active requests including newly received requests at the current time interval and the requests received at previous time intervals which have not expired yet, and the decisions are fixed only when the response for the request cannot be further postponed, namely, the request will ex pire before the next decision epoch.

## 4.1. Benchmark: greedy approach

Greedy approach (GA) is a simple, intuitive algorithm that makes fixed decisions at each step. In practice, a GA is often used for container transport planning [19]. By using the GA, a shipment request is assigned to the cheapest feasible service at the time of request arrival. Fig. 4 presents the flow chart of the GA applied in dynamic shipment matching. Specifically, the platform provides matches for all the contractual requests received before the planning horizon. After that, the platform books all the services matched with the contractual requests and updates the free capacity of barges and trains. A dynamic event, that is the arrival of a spot shipment request before the end of the planning horizon, triggers a new optimization process. After that, the platform books all the services matched with the spot shipment request, and updates the free capacity of barges and trains.

## 4.2. Rolling horizon approach

Rolling horizon approach (RHA) is a periodic reoptimization approach, which has been applied in many research fields, such as ridesharing problems [13] and parcel delivery problems [2]. Under a RHA, the system is optimized periodically at pre-specified points in time called optimization times. The length between two consecutive optimization times is called the optimization interval, h. The RHA is therefore executed at a given set of time points {0,h, 2h, …, T}. Here, T is the length of the planning horizon.

Under the RHA. plans are made using all known information within a planning horizon, but decisions are not finalized until necessitated by a deadline. Re-optimizing the system allows for enhancing the reliability of the system and improving its performance by incorporating the latest information. The flow chart of the RHA applied in the DSM problem is presented in Fig. 5. At each decision epoch, the system determines the matches for all active shipments. At time point t, shipment r is active if its announce time is earlier than t, and its release time is later than t. The matching plan for active shipment r made at time point t is fixed only if its release time is earlier than t + h, namely, the shipment request will expire before the next decision epoch. Thus, the system books all the services matched with this request, and updates the free capacity of barge and train services.

![](/api/attachments/6FCJ3DWT/fulltext/images/1a6f6a093886ec94002213a3c65304c4613e583bd541555073fa728046141c15.jpg)  
Fig. 5. Flow chart of the rolling horizon approach.

Table 1  
Notations used in this paper.

<table><tr><td colspan="2">Sets</td></tr><tr><td>N</td><td>Terminals</td></tr><tr><td>R</td><td>Shipment requests</td></tr><tr><td>S</td><td>Transport services,  $S = S^{\text{barge}} \cup S^{\text{train}} \cup S^{\text{truck}}$ </td></tr><tr><td> $S_{i}^{+}$ </td><td>Transport services depart at terminal  $i \in N$ ,  $S_{i}^{+} = S_{i}^{-}$ barge $\cup S_{i}^{+}$ train $\cup S_{i}^{+}$ truck</td></tr><tr><td> $S_{i}^{-}$ </td><td>Transport services arrive at terminal  $i \in N$ ,  $S_{i}^{-} = S_{i}^{-}$ barge $\cup S_{i}^{-}$ train $\cup S_{i}^{-}$ truck</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$o_{r}$  Origin terminal of shipment request  $r \in R$ $d_{r}$  Destination terminal of shipment request  $r \in R$ $q_{r}$  Container volume of shipment request  $r \in R$ $\Gamma_{r}^{announce}$  Announce time of shipment request  $r \in R$ $\Gamma_{r}^{release}$  Release time of shipment request  $r \in R$ $\Gamma_{r}^{due}$  Due time of shipment request  $r \in R$ $c_{r}^{delay}$  Delay cost coefficient of request  $r \in R$  per container per hour overdue
 $o_{s}$  Origin terminal of service  $s \in S$ $d_{s}$  Destination terminal of service  $s \in S$ $Q_{s}$  Free capacity of service  $s \in S^{barge} \cup S^{train}$ $TD_{s}$  Departure time of service  $s \in S^{barge} \cup S^{train}$ $TA_{s}$  Arrival time of service  $s \in S^{barge} \cup S^{train}$ $t_{s}^{truck}$  Travel time of truck service  $s \in S^{truck}$  at non-peak periods
 $\alpha, \beta$  Road traffic congestion coefficients
 $b_{k}$  The  $k^{th}$  breakpoint of time-dependent travel time functions of truck services,  $k = \{1,2,\ldots,K\}$ $T^{m}$  The  $m^{th}$  time period within a day,  $T^{m} = [b_{m}, b_{m+1}]$ ,
 $m = \{1,2,\ldots,K - 1\}$ $\theta_{s}^{m}$  The slope of the travel time function of truck service s for time period  $T^{m}$ $\eta_{s}^{m}$  The intersection of the travel time function of truck service  $s \in S^{truck}$  for time period  $T^{m}$ $e_{s}$  Carbon emissions of service  $s \in S$  per container
 $c_{s}$  Transport cost of service  $s \in S$  per container
 $lc^{barge}$  Loading/unloading cost of barge services
 $lt^{barge}$  Loading/unloading time of barge services
 $lc^{train}$  Loading/unloading cost of train services
 $lt^{train}$  Loading/unloading time of train services
 $lc^{truck}$  Loading/unloading cost of truck services
 $lt^{truck}$  Loading/unloading time of truck services
 $c^{storage}$  Storage cost coefficient at terminals per container per hour
 $c^{emission}$  carbon tax coefficient per ton
M Large (enough) numbers used for binary constraints
</div>

Variables

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$x_{rs}$  A binary variable equal to 1 if request  $r \in R$  is matched with service  $s \in S$ , 0 otherwise
 $A_{ri}$  Arrival time of request  $r \in R$  at terminal  $i \in N$ $f_{ri}^{+}$  Loading cost of request  $r \in R$  at terminal  $i \in N$  per container
 $f_{ri}^{-}$  Unloading cost of request  $r \in R$  at terminal  $i \in N$  per container
 $w_{ri}$  Storage time of request  $r \in R$  at terminal  $i \in N$ $I_{r}^{delay}$  Delay of request  $r \in R$  at destination terminal  $d_{r}$ $t'_{rs}$  Travel time of truck service  $s \in S^{truck}$  with request  $r \in R$ $\tau_{rs}$  Departure time of truck service  $s \in S^{truck}$  with request  $r \in R$ $\tau'_{rs}$  Normalized departure time of truck service  $s \in S^{truck}$  with request  $r \in R$ ,
 $0 \leq \tau'_{rs} \leq 24$ $n_{rs}$  An integer variable used for normalizing departure time of truck service  $s \in S^{truck}$  with request  $r \in R$ $\zeta_{rs}^{k}$  A continuous variable used for linearizing the time-dependent travel time function of truck service  $s \in S^{truck}$ ,  $0 \leq \zeta_{rs}^{k} \leq 1$ $\xi_{rs}^{m}$  A binary variable used for linearizing the time-dependent travel time function of truck service  $s \in S^{truck}$
</div>

## 5. Optimization algorithms

In this section, we present two optimization algorithms to solve the DSM problem: an exact algorithm and a heuristic algorithm. While the exact algorithm aims to generate optimal solutions, the heuristic algorithm is designed to generate timely solutions. The notations used in

this paper are shown in Table 1.

## 5.1. Exact algorithm

In this section, we present a mixed integer linear programming model (MILP) for the DSM problem. The MILP model is solved by an exact algorithm which is the CPLEX solver. The objective function (Eq. (1)) minimizes the total costs for the matching of all shipments with services. The total costs consist of transport costs (including transit costs, transfer costs, and storage costs), delay costs, and carbon tax. We include delay costs to address the level of services (i.e., delayed deliveries). Considering carbon tax follows the trend towards sustain ability in the transport industry. In the literature, there exist several models for calculating emission charges. However, most of the models require detailed input data $( \mathbf { e . g . }$ , the mass of the vehicle, $\mathsf { a i r } ,$ and rolling resistance) which is in many cases not available. As an alternative, the activity-based method that multiplies the number of containers with the $C O _ { 2 }$ emission factor yields better feasibility in transportation practice and has been applied in many studies [6,18]. Therefore, this paper uses the activity-based method to charge $C O _ { 2 }$ emissions.

Minimize

$$
\begin{array}{r l} & {\sum_ {r \in R} \sum_ {s \in S} x _ {r s} q _ {r} c _ {s} + \sum_ {r \in R} \sum_ {i \in N} (f _ {r i} ^ {+} + f _ {r i} ^ {-}) q _ {r} + \sum_ {r \in R} \sum_ {i \in N} w _ {r i} q _ {r} c ^ {\mathrm{storage}}} \\ {+} & {\sum_ {r \in R} \Gamma_ {r} ^ {\mathrm{delay}} q _ {r} c _ {r} ^ {\mathrm{delay}}} \\ {+} & {\sum_ {r \in R} \sum_ {s \in S} x _ {r s} e _ {s} q _ {r} c ^ {\mathrm{emission}}} \end{array}
$$

subject to

$$
\sum_ {s \in S _ {o r} ^ {+}} x _ {r s} = 1, \forall r \in R,\tag{1}
$$

$$
\sum_ {s \in S _ {d _ {r}} ^ {-}} x _ {r s} = 1, \forall r \in R,\tag{2}
$$

(3)

$$
\sum_ {s \in S _ {i} ^ {+}} x _ {r s} = \sum_ {s \in S _ {i} ^ {-}} x _ {r s}, \forall r \in R, i \in N \backslash \{o _ {r}, d _ {r} \},\tag{4}
$$

$$
\sum_ {r \in R} x _ {r s} q _ {r} \leq Q _ {s}, \forall s \in S ^ {\mathrm{barge}} \cup S ^ {\mathrm{train}},\tag{5}
$$

$$
f _ {r i} ^ {+} = \sum_ {s \in S _ {i ^ {+}} ^ {\mathrm{barge}}} x _ {r s} l c ^ {\mathrm{barge}} + \sum_ {s \in S _ {i ^ {+}} ^ {\mathrm{train}}} x _ {r s} l c ^ {\mathrm{train}} + \sum_ {s \in S _ {i ^ {+}} ^ {\mathrm{truck}}} x _ {r s} l c ^ {\mathrm{truck}},
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \},\tag{6}
$$

$$
f _ {r i} ^ {-} = \sum_ {s \in S _ {i} ^ {\text { barge }}} x _ {r s} l c ^ {\text { barge }} + \sum_ {s \in S _ {l} ^ {\text { train }}} x _ {r s} l c ^ {\text { train }} + \sum_ {s \in S _ {l} ^ {\text { truck }}} x _ {r s} l c ^ {\text { truck }},
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \},
$$

$$
A _ {r o _ {r}} = \Gamma_ {r} ^ {\mathrm{release}}, \forall r \in R,\tag{7}
$$

$$
A _ {r i} \leq (T A _ {s} + l t ^ {\mathrm{barge}}) x _ {r s} + M (1 - x _ {r s}),\tag{8}
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \}, s \in S _ {i ^ {-}} ^ {\mathrm{barge}},\tag{9}
$$

$$
A _ {r i} \geq (T A _ {s} + l t ^ {\mathrm{barge}}) x _ {r s} + M (x _ {r s} - 1),
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \}, s \in S _ {i ^ {-}} ^ {\mathrm{barge}},\tag{10}
$$

$$
A _ {r i} \leq (T A _ {s} + l t ^ {\mathrm{train}}) x _ {r s} + M (1 - x _ {r s}),
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \}, s \in S _ {i} ^ {\mathrm{train}},\tag{11}
$$

$$
A _ {r i} \geq (T A _ {s} + l t ^ {\mathrm{train}}) x _ {r s} + M (x _ {r s} - 1),
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \}, s \in S _ {i} ^ {\text {train}},
$$

(12)

$$
A _ {r i} \leq \tau_ {r s} + t _ {r s} ^ {\prime} + l t ^ {\mathrm{truck}} x _ {r s} + M (1 - x _ {r s}),
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \}, s \in S _ {i} ^ {\mathrm{truck}},\tag{13}
$$

$$
A _ {r i} \geq \tau_ {r s} + t _ {r s} ^ {\prime} + l t ^ {\mathrm{truck}} x _ {r s} + 2 M (x _ {r s} - 1),
$$

$$
\forall r \in R, i \in N \backslash \{o _ {r} \}, s \in S _ {i} ^ {\mathrm{truck}},\tag{14}
$$

$$
A _ {r i} \leq (T D _ {s} - l t ^ {\mathrm{barge}}) x _ {r s} + M (1 - x _ {r s}),
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \}, s \in S _ {i ^ {+}} ^ {\mathrm{barge}},\tag{15}
$$

$$
A _ {r i} \leq (T D _ {s} - l t ^ {\mathrm{train}}) x _ {r s} + M (1 - x _ {r s}),
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \}, s \in S _ {i ^ {+}} ^ {\mathrm{train}},\tag{16}
$$

$$
A _ {r i} \leq \tau_ {r s} - l t ^ {\mathrm{truck}} x _ {r s} + M (1 - x _ {r s}),
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \}, s \in S _ {i ^ {+}} ^ {\mathrm{truck}},\tag{17}
$$

$$
\tau_ {r s} ^ {\prime} = \tau_ {r s} - 2 4 n _ {r s}, \forall r \in R, s \in S ^ {\mathrm{truck}},\tag{18}
$$

$$
\tau_ {r s} ^ {\prime} = \sum_ {k} \zeta_ {r s} ^ {k} b _ {k}, \forall r \in R, s \in S ^ {\mathrm{truck}},\tag{19}
$$

$$
\sum_ {k} \zeta_ {r s} ^ {k} = 1, \forall r \in R, s \in S ^ {\mathrm{truck}},\tag{20}
$$

$$
t _ {r s} ^ {\prime} = \sum_ {k} \zeta_ {r s} ^ {k} (\theta_ {s} ^ {m} b _ {k} + \eta_ {s} ^ {m}), \forall r \in R, s \in S ^ {\mathrm{truck}},\tag{21}
$$

$$
\sum_ {m} \xi_ {r s} ^ {m} = 1, \forall r \in R, s \in S ^ {\mathrm{truck}},\tag{22}
$$

$$
\zeta_ {r s} ^ {1} \leq \xi_ {r s} ^ {1}, \forall r \in R, s \in S ^ {\text { truck }},\tag{23}
$$

$$
\zeta_ {r s} ^ {k} \leq \xi_ {r s} ^ {k - 1} + \xi_ {r s} ^ {k},
$$

$$
\forall r \in R, s \in S ^ {\text { truck }}, k \in \{2, 3,... K - 1 \},\tag{24}
$$

$$
\zeta_ {r s} ^ {K} \leq \xi_ {r s} ^ {K - 1}, \forall r \in R, s \in S ^ {\mathrm{truck}},\tag{25}
$$

$$
w _ {r i} \geq (T D _ {s} - l t ^ {\mathrm{barge}}) x _ {r s} - A _ {r i},
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \}, s \in S _ {i ^ {+}} ^ {\mathrm{barge}},\tag{26}
$$

$$
w _ {r i} \geq (T D _ {s} - l t ^ {\mathrm{train}}) x _ {r s} - A _ {r i},
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \}, s \in S _ {i ^ {+}} ^ {\text {train}},\tag{27}
$$

$$
w _ {r i} \geq \tau_ {r s} - l t ^ {\mathrm{truck}} x _ {r s} + M (x _ {r s} - 1) - A _ {r i},
$$

$$
\forall r \in R, i \in N \backslash \{d _ {r} \}, s \in S _ {i ^ {+}} ^ {\text { truck }},\tag{28}
$$

$$
\Gamma_ {r} ^ {\mathrm{delay}} \geq A _ {r d _ {r}} - \Gamma_ {r} ^ {\mathrm{due}}, \forall r \in R.\tag{29}
$$

Constraints (2)–(4) manage the inflow of shipments at their origin terminal, outflow at destination terminal, and flow conservation at transshipment terminal. Constraints (5) ensure that the total container volumes of shipments carried by service s ∈ $S ^ { \mathrm { b a r g e } } \cup S ^ { \mathrm { t r a i n } }$ do not exceed its free capacity. Constraints (6)–(7) represent the loading and unloading cost of request r per container generated at terminal i. Constraints (8) assume that the arrival time of request r at origin terminal is the release time. Constraints (9)–(12) ensure that the arrival time of request r at terminal i is the arrival time of service $s \in S ^ { \mathrm { b a r g e } } \cup \mathbf { \bar { \Sigma } } S ^ { \mathrm { t r a i n } }$ plus unloading time, if request r is transported by service s entering terminal i. Constraints (13)–(14) ensure that the arrival time of request r at terminal i is the sum of departure time of service $s \in S ^ { \mathrm { t r u c k } }$ with request r at terminal $o _ { s } ,$ travel time of truck service s, and unloading time, if request r is transported by truck service s entering terminal i. In constraints (14), we use 2M instead of M in the right-hand side to make sure the value of $A _ { r i }$ will not be influenced by the constraints when $x _ { r s } = 0$ and $\tau _ { r s } = M .$ Constraints (15)–(17) ensure that the arrival time of request r at terminal i is earlier than the departure time of service $s \in S$ minus loading time, if request r is transported by service s leaving terminal i. Constraints (18)–(25) are imposed to linearize the time-dependent travel time functions of truck services. Constraints (26)–(28) ensure that the storage time of request r at terminal i is the departure time of service s minus the arrival time of request r at terminal i and minus loading time, if request r is transported by service s leaving terminal i. Constraints (29) are imposed to calculate the late deliveries of request r at destination terminal d . We do not penalize earlier deliveries but only late deliveries.

## 5.2. Heuristic algorithm

Due to the computational complexity of the matching problem, the exact algorithm proposed in Section 5.1 approach cannot generate feasible solutions for realistic instances. Therefore, this paper proposes a preprocessing-based heuristic algorithm to reduce the computational complexity. The algorithm consists of three steps: preprocessing of path generation in which no request-specific characteristics are taken into account, preprocessing of feasible matches in which request-specific characteristics $( \mathrm { i . e . }$ , release time and due time) are considered, and binary integer programming to generate ‘optimal’ solutions.

## 5.2.1. Preprocessing of path generation

We define a path as a combination of services. A path p can consist of a single service or multiple services. For example, a path p consists of a barge service s and a truck service $s _ { 2 } ,$ thus, $\boldsymbol { p } = [ s _ { 1 } , s _ { 2 } ]$ . We define L as the largest number of services in a path. Due to fixed schedules of barge and train services, some of the service combinations are infeasible. Let ${ P _ { i j } } ^ { l }$ be the set of feasible paths with l services that depart at terminal i ∈ N and arrive at terminal $j \in N , l \in \{ 1 , . . . , L \} . \mathrm { A }$ path $p \in { P _ { i j } } ^ { l }$ is feasible only if all the services in path $p = [ s _ { 1 } , . . . , s _ { l } ]$ satisfies spatial and time compatibility: for service $s _ { n } , s _ { n + 1 } \in p , n \in \{ 1 , . . . , l - 1 \}$ , the destination terminal of service $s _ { n }$ should be the same as the origin terminal of service $s _ { n + 1 } ;$ the arrival time of $\dot { s } _ { n }$ plus unloading and loading time at the transshipment terminal should be earlier than the departure time of service $s _ { n + 1 }$

Based on the above principles, feasible paths with maximum L services are generated by using the ofline preprocessing algorithm presented in Algorithm 1. The algorithm starts with determining the feasible paths for each origin-destination pair with just one service, and subsequently combines these paths with a single service to create feasible paths with two services, three services, and so on. For each feasible path, we record the virtual departure and arrival time points of all the services in the path by calling the AUXILIARYTIMEPOINTS as described in Algorithm 2. The virtual departure (arrival) time points of barge and train services are the departure (arrival) time of these services minus (plus) loading (unloading) time. Instead of determining the departure time of truck services to avoid trafic congestion, we define the virtual departure time points of truck services as the virtual arrival time points of their previous services to reduce computational complexity. The time-dependent travel time of truck services is calculated based on the virtual departure time point plus loading time. To examine whether a path $p ^ { \prime } \ = \ [ s _ { 1 } , . . . , s _ { l - 1 } , s ] \in { \cal P } _ { i j } ^ { \ l }$ is feasible, we check the time compatibility between path $p ~ = ~ [ s _ { 1 } , . . . , s _ { l - 1 } ] ~ \in ~ P _ { i o _ { s } } { } ^ { l - 1 }$ and service $s \in { S _ { j } } ^ { - }$ by calling the TIMECOMPATIBLE1 as described in Algorithm 3.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. Path generation algorithm.

Input: Set of transportation services S, set of terminals N, the largest number of services in a path L, index  $l \in \{1, 2, ..., L\}$ .

Output: Set of feasible paths  $P = P^{1} \cup \ldots P^{l} \cup \ldots P^{L}$ ,  $P_{ij}^{l} \subseteq P^{l}$  represents the set of feasible paths with l services that depart at node i, and arrive at node j. Auxiliary time points  $MT_{p}^{l} = \left[MT_{p}^{l1}, ..., MT_{p}^{l(2l)}\right]$ .

Initialize: Let  $P \leftarrow \emptyset$ ,  $MT_{p}^{l} \leftarrow [0]$ ,  $l \leftarrow 1$ .

1: for node  $i \in N$ , node  $j \in N$  do

2:    for service  $s \in S$  do

3:    if origin  $o_{s} = i$  and destination  $d_{s} = j$  then

4:    $p \leftarrow [s]$ 

5:    $P_{ij}^{l} \leftarrow P_{ij}^{l} \cup \{p\}$ 

6:    $MT_{p}^{l} \leftarrow AUXILIARYTIMEPOINTS(p)$ 

7:  $l \leftarrow l + 1$ 

8: while  $l \leq L$  do

9:    for node  $i \in N$ , node  $j \in N$  do

10:    for service  $s \in S$  do

11:    if origin  $o_{s} \neq i$  and destination  $d_{s} = j$  then

12:    for feasible path  $p \leftarrow [s_{1}, ..., s_{l-1}] \in P_{io_{s}}^{l-1}$  do

13:    if TIMECOMPATIBLE1( $p, s$ ) = 1 then

14:    $p' = [s_{1}, ..., s_{l-1}, s]$ 

15:    $P_{ij}^{l} \leftarrow P_{ij}^{l} \cup \{p'\}$ 

16:    $MT_{p'}^{l} \leftarrow AUXILIARYTIMEPOINTS(p')$ 

17:    $l \leftarrow l + 1$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2. AUXILIARYTIMEPOINTS.

Input: Feasible path  $p = [s_{1}, ..., s_{l}]$ .

Output: Auxiliary time points  $MT_{p}^{l} = \left[MT_{p}^{l1}, ..., MT_{p}^{l(2n)}, ..., MT_{p}^{l(2l)}\right], n \in \{1, ..., l\}$ .

Initialize: Let  $MT_{p}^{l} \leftarrow [0], n \leftarrow 1$ .

1: while  $n \leq l$  do

2: if  $s_{n} \in S^{truck}$  then

3: if n = 1 then

4:  $MT_{p}^{l(2n-1)} \leftarrow 0$ 

5: else

6:  $MT_{p}^{l(2n-1)} \leftarrow MT_{p}^{l(2n-2)}$ 

7: Travel time of truck service  $s_{n} \leftarrow$  calculate time-dependent travel time function of truck service  $s_{n}$ 

8:  $MT_{p}^{l(2n)} \leftarrow MT_{p}^{l(2n-1)}$  plus loading time plus travel time of truck service  $s_{n}$  plus unloading time

9: else

10:  $MT_{p}^{l(2n-1)} \leftarrow$  departure time of service  $s_{n} \in S^{barge} \cup S^{train}$  minus loading time

11:  $MT_{p}^{l(2n)} \leftarrow$  arrival time of service  $s_{n} \in S^{barge} \cup S^{train}$  plus unloading time

12:  $n \leftarrow n + 1$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: node  $i \in N$ , service  $s \in S \setminus S_{i}^{+}$ , feasible path  $p = [s_{1}, ..., s_{l-1}] \in P_{io_{s}}^{l-1}$ .
Output: z, equal to 1 if path p and service s is time compatible, 0 otherwise.
Initialize: Let  $z \leftarrow 0$ .
1: if  $s \in S^{barge} \cup S^{train}$  then
2: if  $MT_{p}^{2(l-1)} \leq$  departure time of service s minus loading time then
3:  $z \leftarrow 1$ , return z
4: else
5:  $z \leftarrow 1$ , return z
</div>

A match $\langle r , p \rangle$ is defined as a combination of shipment $r \in R$ and path $p = [ s _ { 1 } , . . . , s _ { l } ] , p \in P ,$ which means shipment r will be transported by the services included in path p. The match $\langle r , p \rangle$ is feasible only if it satisfies spatial and time compatibility: the origin of shipment r should be the same as the origin of service $s _ { 1 } ,$ the destination of shipment r should be the same as the destination of service $s _ { l } ^ { \star }$ the release time of shipment r should be earlier than the virtual departure time point of service $s _ { 1 } .$

We define Φ as the set of feasible matches, $c _ { r p }$ as the cost of matching shipment r with path $p .$ Algorithm 4 is designed to create the feasible matches. For shipment r and path $p = [ s _ { 1 } , . . . , s _ { l } ] \in P _ { o _ { r } d _ { r } } { } ^ { l } ,$ , the time compatibility between r and $p$ is checked by calling TIMECOMP-ATIBLE2, as presented in Algorithm 5. If $s _ { 1 } , . . . , s _ { n }$ are truck services, the virtual departure and arrival time points of these truck services need to be updated sequentially. After the updating, if the virtual arrival time point of $s _ { n }$ is less than the virtual departure time point of service $s _ { n }$ $\mathbf { \Sigma } _ { + 1 } \in S ^ { \mathrm { b a r g e } } \cup S ^ { \mathrm { t r a i n } }$ , match $\langle r , p \rangle$ is feasible. If $s _ { 1 }$ is a barge or train service, and the release time of shipment r is less than the virtual departure time point of service $s _ { 1 } ,$ then match $\langle r , p \rangle$ is feasible.

## Algorithm 4. Feasible match generation algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\sum_{r \in R} \sum_{p \in \Phi_{rs}} y_{rp} q_r \leq Q_s, \forall s \in S^{\text{barge}} \cup S^{\text{train}},$ (32)  
$y_{rp} \in \{0,1\}, \forall r \in R, p \in \Phi_r,$ (33)  
where $\Phi_{rs} = \{p \in \Phi_r | s \in p\}$. Constraints (31) ensure that only one feasible path will be assigned to each shipment. Constraints (32) ensure that the total volume of
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Set of feasible paths P, set of shipment requests R, the largest number of services in a path L, index  $l \in \{1, 2, ..., L\}$ , set of auxiliary time points MT, objective function (1).
Output: Set of feasible matches  $\Phi = \Phi_{1} \cup \Phi_{2}... \cup \Phi_{r}... \cup \Phi_{R}$ .
Initialize: Let  $\Phi \leftarrow \emptyset, l \leftarrow 1$ 
1: for shipment request  $r \in R$  do
2:    for  $l \in \{1, 2, ..., L\}$  do
3:    for feasible path  $p = [s_{1}, s_{2}, ..., s_{l}] \in P_{ord_{r}}^{l}$  do
4:    if TIMECOMPATIBLE2(r, p) = 1 then
5:    $\Phi_{r} \leftarrow \Phi_{r} \cup \{p\}$ 
6:    $c_{rp} \leftarrow$  Calculate the objective function

Algorithm 5. TIMECOMPATIBLE2.
Input: shipment request  $r \in R$ , feasible path  $p = [s_{1}, ..., s_{l}] \in P_{ord_{r}}^{l}$ , auxiliary time points  $MT_{p}^{l} = \left[MT_{p}^{l1}, ..., MT_{p}^{l(2n)}, ..., MT_{p}^{l(2l)}\right], n \in \{1, ..., l\}$ .
Output: z, equal to 1 if r and p is time compatible, 0 otherwise.
Initialize: Let  $z \leftarrow 0, n \leftarrow 2$ .
1: if  $s_{1} \in S^{truck}$  then
2: update  $MT_{p}^{l1} \leftarrow$  release time of shipment request r
3: update travel time of truck service  $s_{1} \leftarrow$  calculate time-dependent travel time function truck service  $s_{1}$ 
4: update  $MT_{p}^{l2} \leftarrow MT_{p}^{l1}$  plus loading time plus travel time of truck service  $s_{1}$  plus unloading time
5: while  $n \leq l$  do
6: if  $s_{n} \in S^{truck}$  then
7: update  $MT_{p}^{l(2n-1)} \leftarrow MT_{p}^{l(2n-2)}$ 
8: update travel time of truck service  $s_{n} \leftarrow$  calculate time-dependent travel time function truck service  $s_{n}$ 
9: update  $MT_{p}^{l(2n)} \leftarrow MT_{p}^{l(2n-1)}$  plus loading time plus travel time of truck service  $s_{n}$  plus unloading time
10: else
11: if  $MT_{p}^{l(2n-2)} \leq MT_{p}^{l(2n-1)}$  then
12:    $z \leftarrow 1$ , return z
13: else
14: return z
15:  $n \leftarrow n + 1$ 
16: else
17: if release time of shipment request  $r \leq MT_{p}^{l1}$  then
18:    $z \leftarrow 1$ , return z
</div>

## 5.2.3. Binary integer programming

Based on the above preprocessing procedures, the objective function is updated to minimize the total costs for the matching of shipments with feasible paths. Let $y _ { \eta }$ be a binary decision variable equal to 1 if shipment r is matched with path $p ,$ and 0 otherwise. The mathematical formulation translates into a binary integer programming (BIP) model:

Minimize

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\sum_{r \in R} \sum_{p \in \Phi_r} c_{rp} y_{rp}$ (30) subject to $\sum_{p \in \Phi_r} y_{rp} = 1, \forall r \in R,$ (31)
</div>

shipments assigned to service s ∈ $S ^ { \mathrm { b a r g e } } \cup S ^ { \mathrm { t r a i n } }$ does not exceed its free capacity.

## 6. Numerical experiments

In this section, we first evaluate the performance of the optimization algorithms and compare the GA with the RHA. Then, we investigate the impact of diferent objective functions and optimization intervals. All algorithms were implemented in MATLAB ${ \mathrm { R } } 2 { 0 } 1 7 { \mathrm { a } } ,$ and all experiments were performed on a computer with 2.50 GHz Intel Core i5-7200U CPU and 8 GB RAM. CPLEX 12.6.3 was used as an IP solver.

![](/api/attachments/6FCJ3DWT/fulltext/images/a558553944568d172c82c1873691ad6b648f505303a2201eee6509b24aed3d3a.jpg)  
Fig. 6. The topology of an intermodal network in Europe.

## 6.1. Generation of test instances

In practice, diferent companies have diferent network sizes. For example, Combi Terminal Twente (https://www.ctt-twente.nl/ en/, accessed: 2020-03-16) provides container transports from the port of Rotterdam to 3 inland terminals in the Netherlands and Germany with 7 barges, 3 trains and 40 trucks per week. European Gateway Services (EGS, https://www.europeangatewayservices.com/ en, accessed: 2020-03-16) ofers above 40 trains and 30 barges per week between the Ports of Rotterdam and Antwerp and 11 inland terminals in the Netherlands, Belgium, Germany, and Austria. Every year, approximately 1,000,000 TEU is transported within the EGS network. To show the application of the model, we consider a hinter land intermodal network in Europe to carry out the numerical experi ments, as shown in Fig. 6. The network consists of three deep-sea terminals (nodes 1, 2, 3) and seven inland terminals (nodes 4, 5, 6, 7, 8, 9, 10) which are connected by 116 transport services, including 49 barges, 33 trains, and 34 trucks. The length of the planning horizon was set to one week. The coeficients used in the experiments were derived from Riessen et al. [20] and Li et al. [11], as shown in Table 2. Here, the transit cost of services is a linear function of the transit time t and distance d.

We generated several instances to represent diferent characteristics of shipments within the given network. We use $\mathrm { E U } \mathrm { ~ - ~ } n _ { 1 } \mathrm { ~ - ~ } n _ { 2 }$ to represent an instance with n contractual requests and n spot requests. The average container volume of contractual requests is 20 TEU, and the average container volume of spot requests is 5 TEU. We set the arrival frequency to 20, 10, 6 and 4 min for instances with 400, 800, 1200 and 1600 spot requests, respectively. Regarding the time-dependent travel times, we set $b _ { 1 } = 0 , \ b _ { 2 } = 5 , \ b _ { 3 } = 7 , \ b _ { 4 } = 9 , \ b _ { 5 } = 1 3 , \ b _ { 6 } = 1 7 ,$ b =19, b =21, b =24, α=2, β=1.5. The detailed information of services and instances used in this paper is available at https:// surfdrive.surf.nl/files/index.php/s/cCrpmO1dy8ls7if.

## 6.2. Performance of the heuristic algorithm

To compare the performance of the heuristic algorithm presented in Section 5.2 with the exact algorithm presented Section 5.1, we generated 8 instances of the DSM problem with diferent numbers of shipment requests. In the exact algorithm, we set the large enough number M to 168. In the heuristic setting, we let the largest number of services in a path L be 1, 2, 3 and 4, respectively. We use heuristic-L to represent the heuristic algorithm with setting L. The number of variables (i.e., N.var) and constraints (i.e., N.con) for the instances under diferent algorithms is presented in Table 3.

We consider two performance indicators: total costs (obj: €) and computation time (CPU: seconds). The computation time of heuristics includes the time of generating feasible matches and the time of solving the BIP model. We use ‘gap’ to represent the %gaps in total costs between diferent algorithms, which is given by (objective value − benchmark value) ∗ 100/benchmark value. Table 4 summarizes the performance for all instances. It shows that the small instances with up to 30 contractual requests are still solvable by using the exact algorithm. However, the computation time increases dramatically from 27 to 5647 s. In comparison, extending L from 1 to 3, the gaps in total cost between the heuristic algorithm and the exact algorithm decreases to 0.00%. The computation time of the heuristic algorithm with a maximum of 3 services in a path (Heuristic-3) is no more than 1 s.

For instances with above 700 total requests, we cannot obtain feasible solutions with the exact algorithm. The limitation in these instances is not the computation time but rather the memory since the size of the problems becomes too large to read. In contrast, all these large instances can be solved by using the heuristic algorithm with a maximum of 3 services in a path within 176.24 s, and the gaps in total costs between heuristic-3 and heuristic-4 are 0.00%.

## 6.3. Performance of the dynamic approaches

In this section, we aim to compare the performance of two dynamic approaches: the GA and the RHA. Both of them work with Heuristic-3. We set the length of the optimization interval under the RHA to 1 h.

We generated 4 groups of instances with diferent demand densities represented by the ratio between demand and supply: EU-100-400 (40%), EU-200-800 (80%), EU-300-1200 (120%), and EU-400-1600 (160%). Here, demand is the total container volumes of shipments, supply is the total free capacity of barge and train services. Each group includes 10 instances with the same ratio between demand and supply. We use the GA as the benchmark. Fig. 7(a) shows that the RHA has lower total costs in all the groups of instances, and the reduction in total costs increases with the demand density. The reason is that the higher the ratio between demand and supply, the competition between shipment requests is higher. The proposed RHA better allocates limited barge and train capacity to more suitable shipment requests which might arrive later in the system.

We generated another 4 groups of instances with diferent degrees of dynamism (DOD). In this paper, we define the DOD as the ratio between the number of spot containers and the number of total containers. Thus, the DOD for instance EU-300-400 is (400 ∗ 5)/ (300 ∗ 20 + 400 ∗ 5) = 25%. The DOD for instance EU-300-400, EU-200-800, EU-100-1200, EU-0-1600 are therefore 25%, 50%, 75% and 100% respectively. Each group includes 10 instances with the same DOD. Fig. 7(b) shows that the RHA also has better performance in all the groups of instances compared to the GA, and the improvement is increasing further with a higher DOD. Interestingly, when the matching system is 100% dynamic, the variance of the performance of the RHA becomes the largest. The reason is when the system is fully dynamic, the performance of the reoptimization-based RHA becomes uncertain.

To investigate the performance of the GA and the RHA under different lead time scenarios, we generated 3 groups of instances with diferent lead times of spot requests: EU-100-1200 (24), EU-100-1200 (48), and EU-100-1200 (72). Each group consists of 10 instances with the same lead time setting. Fig. 7(c) shows that the RHA has better performance than the GA in terms of total costs for all groups of instances and the improvement is larger for longer lead times. Longer lead times provide more flexibility for the RHA to re-optimize the decisions as new requests are received and the capacity can be allocated more efectively.

Similarly, we varied the response time of shipment requests from 1 h to 24 h for 3 groups of instances: EU-100-1200 (1), EU-100-1200 (12), and EU-100-1200 (24). Fig. 7(d) shows that the larger the response time, the better the performance of the RHA is in reducing total costs since it has more time to update decisions for all requests until their release times.

## 6.4. Impact of diferent objective functions and optimization intervals

In this section, we use the RHA and Heuristic-3 to investigate the impact of diferent objective functions and the length of the optimization interval.

## 6.4.1. Impact of diferent objective functions

We investigate the impact of diferent objective functions under instance EU-1000-0. The utilization of barges and trains is defined as the ratio between the utilized capacity of barge and train services multiplied by corresponding transit distances and the utilized total capacity of all services multiplied by corresponding distances. Table 5 shows that diferent objective functions generate diferent matching solutions. Comparing case 11 with cases 1 to 10, we observe that the total cost is the lowest when the objective function includes all elements. When we minimize the transit cost (case 1) or the carbon tax (case 5), the utilization of barges and trains is favored as they are cheaper and environmental friendlier than trucks. On the other hand, minimizing the transfer (case 2), storage (case 3) or delay (case 4) cost favors the utilization of trucks as they are faster in general and have flexible departure times. Comparing case 11 with cases 6 to 10, we see that the transit cost has the largest influence on the matching decisions while carbon tax has the smallest impact. However, it is predictable that the carbon tax coeficient will increase in the near future because of the increasing environmental issues and the enforced regulations. Under a restrict emission policy, such as case 14, including the carbon tax in the objective function can greatly afect the utilization of barges and trains. It is also interesting to observe that there is a clear trade-of between delay and carbon emissions as it is what is happening in real life.

## 6.4.2. Impact of the length of the optimization interva

To test the impact of the length of the optimization interval in the RHA, we used 4 instances with diferent DOD: EU-300-400 (25%), EU-

## Table 2

Experimental setting.

<table><tr><td>Coefficient</td><td>Truck</td><td>Barge</td><td>Train</td></tr><tr><td>Transit cost (€/TEU-km-h)</td><td>30.98 t + 0.2758d</td><td>0.6122 t + 0.0213d</td><td>7.54 t + 0.0635d</td></tr><tr><td>Carbon emission (kg/TEU-km)</td><td>0.8866</td><td>0.2288</td><td>0.3146</td></tr><tr><td>Loading/unloading cost (€/TEU)</td><td>3</td><td>18</td><td>18</td></tr><tr><td>Loading/unloading time (h)</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Carbon tax (€/ton)</td><td>8</td><td>8</td><td>8</td></tr><tr><td>Storage cost (€/TEU-h)</td><td>1</td><td>1</td><td>1</td></tr></table>

Table 3  
Number of variables and constraints for the instances under diferent algorithms

<table><tr><td rowspan="2">Instances</td><td colspan="2">Exact algorithm</td><td colspan="2">Heuristic-1</td><td colspan="2">Heuristic-2</td><td colspan="2">Heuristic-3</td><td colspan="2">Heuristic-4</td></tr><tr><td>N.var</td><td>N.con</td><td>N.var</td><td>N.con</td><td>N.var</td><td>N.con</td><td>N.var</td><td>N.con</td><td>N.var</td><td>N.con</td></tr><tr><td>EU-5-0</td><td>4185</td><td>4221</td><td>26</td><td>18</td><td>54</td><td>25</td><td>66</td><td>25</td><td>68</td><td>25</td></tr><tr><td>EU-10-0</td><td>8370</td><td>8408</td><td>28</td><td>24</td><td>209</td><td>63</td><td>684</td><td>82</td><td>944</td><td>82</td></tr><tr><td>EU-20-0</td><td>16,740</td><td>16,676</td><td>84</td><td>61</td><td>428</td><td>85</td><td>1125</td><td>91</td><td>1488</td><td>91</td></tr><tr><td>EU-30-0</td><td>25,110</td><td>24,963</td><td>112</td><td>66</td><td>564</td><td>104</td><td>1646</td><td>105</td><td>2235</td><td>105</td></tr><tr><td>EU-700-0</td><td>585,900</td><td>580,996</td><td>2504</td><td>767</td><td>13,725</td><td>780</td><td>36,449</td><td>781</td><td>56,777</td><td>781</td></tr><tr><td>EU-1000-0</td><td>837,000</td><td>829,916</td><td>3279</td><td>1067</td><td>18,108</td><td>1082</td><td>49,908</td><td>1082</td><td>79,805</td><td>1082</td></tr><tr><td>EU-1300-0</td><td>1,088,100</td><td>1,079,016</td><td>4473</td><td>1367</td><td>25,377</td><td>1380</td><td>69,202</td><td>1381</td><td>109,758</td><td>1381</td></tr><tr><td>EU-1600-0</td><td>1,339,200</td><td>1,327,942</td><td>6032</td><td>1667</td><td>33,742</td><td>1680</td><td>91,020</td><td>1681</td><td>143,859</td><td>1681</td></tr></table>

Table 4  
Performance of the heuristic algorithm with diferent L.

<table><tr><td rowspan="2">Instances</td><td colspan="2">Exact algorithm</td><td colspan="2">Heuristic-1</td><td colspan="2">Heuristic-2</td><td colspan="2">Heuristic-3</td><td colspan="3">Heuristic-4</td></tr><tr><td>Obj</td><td>CPU</td><td>%gap</td><td>CPU</td><td>%gap</td><td>CPU</td><td>%gap</td><td>CPU</td><td>Obj</td><td>%gap</td><td>CPU</td></tr><tr><td>EU-5-0</td><td>4386</td><td>27.01</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.15</td><td>0.00</td><td>0.60</td><td>4386</td><td>0.00</td><td>0.28</td></tr><tr><td>EU-10-0</td><td>25,988</td><td>213.06</td><td>32.89</td><td>0.03</td><td>0.00</td><td>0.11</td><td>0.00</td><td>0.45</td><td>25,988</td><td>0.00</td><td>0.80</td></tr><tr><td>EU-20-0</td><td>44,198</td><td>1704.98</td><td>29.56</td><td>0.02</td><td>0.05</td><td>0.13</td><td>0.00</td><td>0.43</td><td>44,198</td><td>0.00</td><td>0.65</td></tr><tr><td>EU-30-0</td><td>65,126</td><td>5647.03</td><td>28.52</td><td>0.02</td><td>0.00</td><td>0.13</td><td>0.00</td><td>0.60</td><td>65,126</td><td>0.00</td><td>0.94</td></tr><tr><td>EU-700-0</td><td colspan="2">Out of memory</td><td>17.49</td><td>1.37</td><td>0.17</td><td>8.21</td><td>0.00</td><td>25.47</td><td>1,060,077</td><td></td><td>38.43</td></tr><tr><td>EU-1000-0</td><td colspan="2"></td><td>18.37</td><td>2.60</td><td>0.25</td><td>16.46</td><td>0.00</td><td>45.22</td><td>1,017,669</td><td></td><td>78.94</td></tr><tr><td>EU-1300-0</td><td colspan="2"></td><td>19.03</td><td>6.12</td><td>0.42</td><td>34.15</td><td>0.00</td><td>94.62</td><td>1,042,481</td><td></td><td>158.57</td></tr><tr><td>EU-1600-0</td><td colspan="2"></td><td>18.36</td><td>10.55</td><td>0.17</td><td>63.22</td><td>0.00</td><td>176.24</td><td>1,020,075</td><td></td><td>302.41</td></tr></table>

![](/api/attachments/6FCJ3DWT/fulltext/images/43080422b25bfdd8d5fe9a1835c138dd836e2cb116bc598f3ca5388db327982d.jpg)  
(a)

![](/api/attachments/6FCJ3DWT/fulltext/images/6a5cf759b3592ae316ea6e1b504a0ee3aa11fd1dc768fdb06f8e8dce4244672d.jpg)  
(b)

![](/api/attachments/6FCJ3DWT/fulltext/images/a780ff1c0bcf1993bf7f7b2d23da48164edccf49398e76b9e55a8f23af2ec635.jpg)  
(c)

![](/api/attachments/6FCJ3DWT/fulltext/images/5eaec3ec716de36a36e833e3ec2f1fb88dc5fbfa4a069172c355d53646a506e7.jpg)  
(d)  
Fig. 7. Comparison between the rolling horizon approach and the greedy approach.

Table 5  
Impact of diferent objective functions.

<table><tr><td>Case</td><td>Carbon tax coefficient (€/ton)</td><td>Objective  $function^a$ (min.)</td><td>Total cost (€)</td><td>OF1 (€)</td><td>OF2 (€)</td><td>OF3 (€)</td><td>OF4 (€)</td><td>OF5 (€)</td><td>Delay (TEU-h)</td><td>Carbon emission (kg)</td><td>Utilization of barges and trains (%)</td><td>Utilization of trucks (%)</td></tr><tr><td>1</td><td>8</td><td>OF1</td><td>4,478,714</td><td>598,864</td><td>328,458</td><td>137,798</td><td>3,406,214</td><td>7379</td><td>39,170</td><td>922,429</td><td>71.47</td><td>28.53</td></tr><tr><td>2</td><td></td><td>OF2</td><td>1,473,382</td><td>1,411,229</td><td>47,622</td><td>0</td><td>0</td><td>14,530</td><td>0</td><td>1,816,311</td><td>0.00</td><td>100.00</td></tr><tr><td>3</td><td></td><td>OF3</td><td>1,618,747</td><td>1,499,961</td><td>103,374</td><td>0</td><td>0</td><td>15,412</td><td>0</td><td>1,926,482</td><td>0.04</td><td>99.96</td></tr><tr><td>4</td><td></td><td>OF4</td><td>1,617,409</td><td>1,495,824</td><td>105,960</td><td>245</td><td>0</td><td>15,379</td><td>0</td><td>1,922,413</td><td>0.42</td><td>99.58</td></tr><tr><td>5</td><td></td><td>OF5</td><td>4,432,293</td><td>601,621</td><td>324,498</td><td>144,863</td><td>3,353,948</td><td>7364</td><td>40,167</td><td>920,491</td><td>72.06</td><td>27.94</td></tr><tr><td>6</td><td></td><td>OF2,3,4,5</td><td>1,473,382</td><td>1,411,229</td><td>47,622</td><td>0</td><td>0</td><td>14,530</td><td>0</td><td>1,816,311</td><td>0.00</td><td>100.00</td></tr><tr><td>7</td><td></td><td>OF1,3,4,5</td><td>1,042,644</td><td>648,402</td><td>313,266</td><td>72,066</td><td>1112</td><td>7799</td><td>11</td><td>974,863</td><td>67.96</td><td>32.04</td></tr><tr><td>8</td><td></td><td>OF1,2,4,5</td><td>1,028,388</td><td>668,393</td><td>270,732</td><td>80,338</td><td>972</td><td>7953</td><td>10</td><td>994,084</td><td>65.78</td><td>34.22</td></tr><tr><td>9</td><td></td><td>OF1,2,3,5</td><td>1,803,565</td><td>656,501</td><td>260,772</td><td>69,829</td><td>808,619</td><td>7844</td><td>8624</td><td>980,454</td><td>66.71</td><td>33.29</td></tr><tr><td>10</td><td></td><td>OF1,2,3,4</td><td>1,017,693</td><td>695,156</td><td>252,702</td><td>60,783</td><td>880</td><td>8172</td><td>9</td><td>1,021,544</td><td>63.76</td><td>36.24</td></tr><tr><td>11</td><td></td><td>Total cost</td><td>1,017,675</td><td>692,118</td><td>254,448</td><td>62,114</td><td>850</td><td>8145</td><td>9</td><td>1,018,154</td><td>64.05</td><td>35.95</td></tr><tr><td>12</td><td>100</td><td>Total cost</td><td>1,110,869</td><td>684,140</td><td>260,790</td><td>64,039</td><td>972</td><td>100,929</td><td>10</td><td>1,009,287</td><td>64.78</td><td>35.22</td></tr><tr><td>13</td><td>500</td><td>Total cost</td><td>1,507,925</td><td>658,359</td><td>284,862</td><td>72,431</td><td>1162</td><td>491,111</td><td>12</td><td>982,222</td><td>66.94</td><td>33.06</td></tr><tr><td>14</td><td>1000</td><td>Total cost</td><td>1,995,063</td><td>643,700</td><td>298,386</td><td>78,945</td><td>8159</td><td>965,872</td><td>88</td><td>965,872</td><td>68.48</td><td>31.52</td></tr></table>

Bold to emphasis the significance of bold values.  
<sup>a</sup> OF1: Transit cost; OF2: Transfer cost; OF3: Storage cost; OF4: Delay cost; OF5: Carbon tax; OF2,3,4,5: Transfer cost + Storage cost + Delay cost + Carbon tax; OF1,3,4,5: Transit cost + Storage cost + Delay cost + Carbon tax; OF1,2,4,5: Transit cost + Transfer cost + Delay cost + Carbon tax; OF1,2,3,5: Transit cost + Transfer cost + Storage cost + Carbon tax; OF1,2,3,4: Transit cost + Transfer cost + Storage cost + Delay cost.

200-800 (50%), EU-100-1200 (75%) and EU-0-1600 (100%). For each instance, we vary the length of the optimization interval h from 0.1 to 10 h.

We use optimization intervals of 1 h as the benchmark. Fig. 8 shows that reducing h allows the system to react more quickly to new in formation, which in turn leads to improved solutions. This is especially the case for instances with a high DOD. However, excessively reducing h does not improve the performance of the RHA. It is seen that below 1 h of optimization intervals does not bring values as expected since the response times are set as a minimum of 1 h. Therefore, decision makers can improve the matching quality by choosing a proper h-value.

## 7. Conclusion and future research

In this paper, we introduced an online synchromodal matching problem in which a platform aims to provide optimal matches between shipment requests and transport services. We proposed a rolling horizon approach and a heuristic algorithm to support the online decisionmaking process. We validated the heuristic algorithm and the rolling horizon approach on an intermodal network in Europe. The results indicate that the heuristic algorithm is eficient in large instances of the matching problem, and can be used under dynamic contexts. The rolling horizon approach has been proved to outperform a greedy approach in reducing total costs under various scenarios.

![](/api/attachments/6FCJ3DWT/fulltext/images/6121d30bf846df07a03bb7d2a2803719af9526ed05ad6b4cc6a7747ed491b374.jpg)  
Fig. 8. Impact of the length of the optimization interval.

In conclusion, the proposed online matching platform will support decision makers to optimize the matching of shipments and services considering the trade-of between transport cost, delay, and carbon emissions thanks to the developed rolling horizon approach. In other words, with the proposed approach, the use of barges, trains, and trucks can be managed more efectively taking into account their impact on transport time, cost and emissions together with diferent time sensitivities of shipments.

This work can be extended in several directions. During the day, the number of trucks available to the matching platform is quite dynamic. Therefore, combining the dynamics of truck services in the synchromodal matching model is a further research direction. Considering the multiple uncertainties that exist in synchromodal transportation, future research can be carried out on stochastic and dynamic shipment matching. Furthermore, the origins and destinations of containers are usually located in diferent countries. Thus, looking into models with an integrated network combining international and inland transport is a promising research direction. Besides, in this paper, the online matching platform is controlled in a centralized way. However, in practice, multiple operators are present and they may not all be willing to give authority to a central platform. The coordination mechanism among them and incentives to stimulate cooperation are part of future research.

## CRediT authorship contribution statement

Wenjing Guo:Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Writing - review & editing, Visualization.Bilge Atasoy:Conceptualization, Formal analysis, Visualization, Writing - review & editing, Supervision.Wouter Beelaerts van Blokland:Conceptualization, Writing - review & editing, Supervision.Rudy R. Negenborn:Conceptualization, Writing - review & editing, Supervision.

## Acknowledgments

This research is financially supported by the China Scholarship Council under Grant 201606950003 and the project “Complexity Methods for Predictive Synchromodality” (project 439.16.120) of the Netherlands Organisation for Scientific Research (NWO).

## References

[11 T. Ambra. A. Caris. C. Macharis. Towards freight transport system unification: re: viewing and combining the advancements in the physical internet and synchromodal transport research. International Journal of Production Research 57 (6) (2018).1606-1623

[2] A.M. Arslan, N. Agatz, L. Kroon, R. Zuidwijk, Crowdsourced delivery—a dynamic pickup and delivery problem with ad hoc drivers, Transportation Science 53 (1) (2019).222–235

[3] A. Bhattacharya, S.A. Kumar, M. Tiwari, S. Talluri, An intermodal freight transport system for optimal supply chain logistics, Transportation Research Part C: Emerging Technologies 38 (2014) 73–84.

[4] T.G. Crainic, P. Dell’Olmo, N. Ricciardi, A. Sgalambro, Modeling dry-port-based

freight distribution planning, Transportation Research Part C: Emerging Technologies 55 (2015) 518–534.

[5] T.G. Crainic, K.H. Kim, Chapter 8 intermodal transportatio, Transportation, Elsevier, 2007, pp. 467–537.

[6] E. Demir, W. Burgholzer, M. Hrušovský, E. Arıkan, W. Jammernegg, T. Van Woensel, A green intermodal service network design problem with travel time uncertainty, Transportation Research Part B: Methodological 93 (2016) 789–807

[7] E. Demir, M. Hrušovský, W. Jammernegg, T. Van Woensel, Green intermodal freight transportation: bi-objective modelling and analysis, International Journal of Production Research 57 (19) (2019) 6162–6180.

[8] S. Fazi, J.C. Fransoo, T. Van Woensel, A decision support system tool for the transportation by barge of import containers: a case study, Decision Suppor Systems 79 (2015) 33–45

[9] R. Giusti, D. Manerba, G. Bruno, R. Tadei, Synchromodal logistics: an overview of critical success factors, enabling technologies, and open research issues, Transportation Research Part E: Logistics and Transportation Review 129 (2019) 92–110.

[10] R. Konings, E. Kreutzberger, V. Maraš, Major considerations in developing a huband-spoke network to improve the cost performance of container barge transport in the hinterland: the case of the port of Rotterdam, Journal of Transport Geography 29 (2013) 63–73.

[11] L. Li, R.R. Negenborn, B. De Schutter, Intermodal freight transport planning – a receding horizon control approach, Transportation Research Part C: Emerging Technologies 60 (2015) 77–95.

[12] M.R.K. Mes, M.E. Iacob, Synchromodal transport planning at a logistics service provider, Logistics and Supply Chain Innovation, Springer International Publishing, 2015. pp. 23–36.

[13] A. Najmi, D. Rey, T.H. Rashidi, Novel dynamic formulations for real-time ride sharing systems, Transportation Research Part E: Logistics and Transportation Review 108 (2017) 122–140.

[14] V. Pillac, M. Gendreau, C. Guéret, A.L. Medaglia, A review of dynamic vehicle routing problems, European Journal of Operational Research 225 (1) (2013) 1–11

[15] W. Qu, J. Rezaei, Y. Maknoon, L. Tavasszy, Hinterland freight transportation re planning model under the framework of synchromodality, Transportation Research Part E: Logistics and Transportation Review 131 (2019) 308–328

[16] A.P. Rivera, M. Mes, Service and transfer selection for freights in a synchromodal network, Lecture Notes in Computer Science, Springer International Publishing, 2016, pp. 227–242.

[17] M. SteadieSeifi, N. Dellaert, W. Nuijten, T. Van Woensel, R. Raoufi, Multimodal freight transportation planning: a literature review, European Journal of Operational Research 233 (1) (2014) 1–15.

[18] P. Sun, L.P. Veelenturf, M. Hewitt, T. Van Woensel, The time-dependent pickup and delivery problem with time windows. Transportation Research Part B Methodological 116 (2018) 1–24.

[19] B. van Riessen, R.R. Negenborn, R. Dekker, Real-time container transport plannin with decision trees based on ofline obtained optimal solutions, Decision Support Systems 89 (2016) 1–16.

[20] B. van Riessen, R.R. Negenborn, R. Dekker, G. Lodewijks, Service network design for an intermodal container network with flexible transit times and the possibility of using subcontracted transport, International Journal of Shipping and Transport Logistics 7 (4) (2015) 457

[21] H. Wang, X. Wang, X. Zhang, Dynamic resource allocation for intermodal freigh transportation with network effects: approximations and algorithms. Transportation Research Part B: Methodological 99 (2017) 83–112

[22] X. Wang, Optimal allocation of limited and random network resources to discrete stochastic demands for standardized cargo transportation networks, Transportation Research Part B: Methodological 91 (2016) 310–331.

[23] R.A. Zuidwijk, A.W. Veenstra, The value of information in container transport, Transportation Science 49 (3) (2015) 675–685

Wenjing Guo is a PhD researcher at Delft University of Technology. Her research interests include operations research, intermodal transportation, dynamic optimization, stochastic optimization, and distributed optimization. Her main ambition is to combine advanced approaches with practical applications considering the trend towards sustainability, ecommerce, and digitalization in freight transportation. She received her MSc degree from Wuhan University of Technology in 2013 in the area of agent-based nego tiation strategies in agricultural supply chains which received the excellent Master Thesis Award.

Bilge Atasoy is an assistant professor at TU Delft within the Department of Maritime and Transport Technology. Her main research interests lie at the intersection of optimization and behavioral models. She applies the scientific methodologies in the field of various transport and logistics problems in order to increase sustainability and efficiency. One of the application areas is transport and logistics over water where fleet management models are developed to optimize several decisions (e.g., fleet size, needed capacity, routes and schedules for vessels). Prior to joining TU Delft. Bilge was a research scientist at MIT at the Intelligent Transportation Systems (ITS) Lab where she is now a research afiliate. At MIT she led several research projects in the areas of real-time optimization, travel behavior and choice-based optimization. Bilge obtained her PhD from EPFL in November 2013 in the area of integrated supply and demand models in transportation problems which received the best PhD Thesis Award from the Swiss Operations Research Society. She received her MSc and BSc degrees in Industrial Engineering from Bogazici University, Istanbul, in 2009 and 2007, respectively.

Wouter Beelaerts van Blokland researches theories supporting Advanced Operation and Production Management such as Lean manufacturing, value chain and system, (maintenance) supply chains and value creation by innovation. Central theme is perfor mance measurement with KPI's regarding the flow of components or sub systems through processes, to support the process performance regarding the coordination of assets and resources. Currently he is assistant professor at Delft University of Technology within the section Multi-Machine Engineering, part of the department Marine & Transpor Technology of the faculty of Mechanical, Marine and Materials engineering. He achieved his PhD at the Delft University of Technology in 2010. After working in the drive and control and aerospace industry he started this PhD in 2004 with the faculty of Aerospace Engineering to research the efect of leveraging value on suppliers by aircraft manufacturers for the co-development and co-production of aircraft. In that time he started td lecture on Lean Operations Performance Assessment and Value Engineering from which several start-up companies were initiated such as “Type22” and Fly Aeolus. He was nominated for the Delft Entrepreneurial Scientist Award 2010, category Entrepreneurial Motivator and principal lecturer to the team on the project “Formation Flver", which wor the National Prize on aeronautics (2011) in the Netherlands.

Rudy R. Negenborn is a full professor in Multi-Machine Operations & Logistics. He is head of the Section Transport Engineering & Logistics of Department Maritime & Transport Technology. His research interests include intelligent infrastructures & logistics, decision making and coordination for transport technology (including smart vessels) in general, whereby he proposes multi-agent system and model predictive control approaches that benefit from real-time information availability and the potential of communication. As such, his research anticipates the massive introduction of sensing, computation, and communication technologies. This is materialized into innovative solutions for smart equipment, transport hubs, ports and (synchromodal) transport networks. H has over 200 peer reviewed academic publications. He leads NWO, EU and industry funded research, and is on the editorial board of the series on “Intelligent Systems, Control and Automation: Science and Engineering”. He was moreover general chair of the 6th International Conference on Computational Logistics, has acted as member of the organizing committee of several other international conferences (including IEEE control conferences and maritime systems & logistics conferences) and was guest editor of special journal issues on autonomous vessels and computational logistics. In addition, he is the editor of the books “Intelligent Infrastructures”, “Distributed Model Predictive Control Made Easy”, and “Transport of Water versus Transport over Water”.
