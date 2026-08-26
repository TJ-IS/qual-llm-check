---
otero_id: 4774
otero_key: "EYVC35P6"
title: "Dynamic modeling of a disturbance in a multi-agent system for traffic regulation"
authors: "Flavien Balbo; Suzanne Pinson"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.06.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 41 (2005) 131 – 146

www.elsevier.com/locate/dsw

# Dynamic modeling of a disturbance in a multi-agent system for traffic regulation

Flavien Balbo<sup>a,b,\*</sup>, Suzanne Pinson<sup>a</sup>

<sup>a</sup>Lamsade, Paris Dauphine University, Place Mare´chal de Lattre de Tassigny, 75775 Paris Cedex 16, France <sup>b</sup>Inrets-Gretia, Institut National de Recherche sur les Transports et leur Se´curite´ 2, avenue du Ge´ne´ral Malleret-Joinville, F-94114 Arcueil cedex, France

Received 21 March 2003; received in revised form 7 June 2004; accepted 7 June 2004 Available online 12 August 2004

## Abstract

This paper presents the modeling of a disturbance on a public transportation line. The proposed model allows the synthesis, evaluation and update of available information in order to help human regulators in their monitoring task. It begins with a formal modeling of the disturbance concept. This modeling makes it possible to capitalize the knowledge available within a monitoring station and to follow up the evolution of the disturbances in real time. The paper goes on to propose a multi-agent representation of an incident allowing the integration of the disturbance processing within the activity of a network system. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Multi-agent system; Transport system; Disturbance modeling

## 1. Introduction

Over the last few years, with the increase of the number of passengers and lines number, transportation network management has become more and more complex. This change in scale of network activity has to be accompanied by technological changes to the management system. These changes are necessary for bus networks, as opposed to guided transportation (train and subway [14]), since vehicles move in urban traffic. For public transportation networks, the main efficiency criterion of their activity is their commercial speed. In France, the commercial speed average is 15 km/h whereas the ideal speed is about 22 km/h. For Union des Transports Publics (UTP), a 2 km/h increase represents a profit of 0.3 m for all the French provincial networks taken together. These economic studies underline the importance of an increase in speed.

As urban environment density increases, management techniques classically used by bus network regulators (the staff in charge of monitoring the bus network) became obsolete. While adapted decision support systems have been created for train [11] or subway [4] networks, bus regulators have no decision support system adapted to their needs. A variety of approaches have been used to model urban transportation networks (Operation Research methods, fuzzy theory, neural networks, genetic algorithms, intelligent agents). A review of the literature can be found in Refs. [1,2,13]. Regulators use systems known as Automatic Vehicle Monitoring systems (AVM) [9,12], which were developed in order to better ensure the success of the transportation plan. An AVM allows the management of vehicles located by sensors. AVM compares the actual positions of vehicles (captured by the sensors) with their theoretical positions in order to provide the regulator with an overview of the routes. In this way, the regulator can see whether the vehicles are running ahead of timetables or are running late. By comparing the theoretical information with the real one, the AVM system tries to detect delays and advances of buses on the network.

The use of an AVM is the first step to the computerization of the transportation network activity. However, this system is limited to coping with disturbances linked to unanticipated demands and to traffic conditions. Moreover, the collecting and shaping of data are insufficient to help regulators. Some research proposes solutions for particular points (management of connections [3], real-time schedule management [10]), but no system is able to manage all the difficulties dealing with the management of a bus network.

The aim of our decision support system named Syste\`me Automatique de Traitement des Incidents en Re´seaux (SATIR) is to propose an adapted answer to the real-time problem of bus network management. We had chosen a multi-agent paradigm as basis for modeling SATIR. Remember that a multi-agent approach is well adapted to model bus network activities where autonomous entities, called agents, appear and disappear on network, interact with each other in an open, uncertain, dynamic environment [17]. The autonomy of a multi-agent system and its ability to adapt and react are essential in the field of transportation where the environment is dynamic and uncertain [16]. Few transportation models are based on the multi-agent paradigm because one of the difficulties in both the design and the understanding of MASs comes from the lack of central controls and the ensuing conflicting, uncertain, incomplete and delayed knowledge coming from the agents. Lind and Fischer [11] used the multi-agent approach for transportation scheduling and simulation in a railroad scenario. Bre´zillon et al. [4] has designed a simulator to help human regulators of the Parisian subway. Other researchers [7,8,18] use MAS to model coordination intermodal transportation, shipping and air cargo transport.

However, these systems present several drawbacks: they are mostly simulation systems that are not integrated into the decision support system, and they are not directly fed with real-time data coming from vehicle sensors. The multi-agent paradigm makes it easier to solve the difficulties of network management in real time: managing the inconsistencies of the data of the sensors that locate the vehicles, assessing a disturbance according to its context, proposing feasible solutions. This paper focuses on the dynamic modeling of a disturbance in the SATIR system; the other parts of SATIR is reported in [1,2].

The first section presents the concept of disturbance as well as our multi-agent model of a transportation network. The second section presents the formal model of a disturbance, explains how changes in the network are measured and shows how the disturbance model is integrated into our multi-agent system. The third section gives initial results; the last section proposes a conclusion.

## 2. The needs for a decision support system

In urban transportation control, human regulators are located in a control center. They have to manage the transportation network under normal operating conditions (where are the buses located?) and also under disturbed conditions (where are disturbances (bus delays, bus advances) located?, What action has to be taken to solve the problem?).

In most networks, vehicles are located through sensors which provide real-time information. This information represents a huge amount of data (data arrives every 40 s). Furthermore, it may be incomplete (a sensor breaks down) or uncertain (the quality of the data is sometimes poor). This data is collected through the Automatic Vehicle Monitoring system (AVM). AVM compares the actual positions of the vehicles (captured by the sensors) with their theoretical positions in order to provide the human regulator with an overview of the routes. In this way, the regulator can see whether the vehicles are running ahead of schedule or are running late.

Fig. 1 shows the AVM management of real-time information coming from sensors and the output of the system. Each line is represented two ways with its stops and its running buses. Each bus location is represented by (1) a number for its theoretical position coming from the theoretical schedule, (2) a colored square for its real location detected by the system. This real location may be erroneous due to sensor breakdowns. Stops are represented by black dots. The gap between the theoretical position and the real position gives an information about the bus delays or advances. Colors give the importance of the delays or advances.

Problems arise when a vehicle may not be announced on stops he has served thus generating a false alarm (declared as late while it passed over the stop) and erroneous output on the screen.

## 2.1. The disturbance diagnosis context

As explained above, regulators use an AVM system to detect disturbances on the network, i.e., information about advances and delays of vehicles. Some AVM systems propose more sophisticated detections like detection of the delay on the next departure. However, this disturbance diagnosis process has several limitations:

<sup>!</sup> Lack of a global vision: The splitting up of monitoring by line and the high number of the lines to be monitored (each regulator tracks 13 lines with 5–20 buses running during the day) prevent global management of the network.

<sup>!</sup> Lack of space–time dimension: Primary alarms on the advance/delay of each bus provide too instantaneous a picture of line conditions. Monitoring all these alarms in their space–time development is almost impossible and leads to extra work for regulators.

Each regulator has to monitor more lines than he materially can see on his screen. The regulators first activity is to choose which lines to observe (for the transportation network under study, each regulator can handle 3 lines out of 13). This complex process involves various information sources (the AVM system for real-time information, theoretical timetables, information coming from drivers or from other regulators, etc.) [6]. An experimented regulator uses his knowledge of the line structure (the position in the city, the presence of difficult areas) and of the demand structure to determine the most critical lines according to the schedule. Since this kind of information is less available to novice regulators, they are less efficient in solving disturbance problems.

![](/api/attachments/EYVC35P6/fulltext/images/eb242468bff4e0452c47b9d579fc1400ed4aba35369d1c1cb69811b32bfd2a84.jpg)  
Fig. 1. Real-time information in a bus transportation network.

As soon as a disturbance is chosen by the regulator, he has to complete his knowledge of the problem. This process is complex because disturbances evolve independently along three axes [15]:

<sup>!</sup> Time: this axis measures the seriousness of a disturbance according to the timetable. For example, a stop near a university should be monitored with timetables corresponding to arrivals and departures of students.

<sup>!</sup> Space: this axis measures the seriousness of a disturbance according to its position on the network. For example, some locations are known to be critical. A disturbance at these locations is more difficult to manage.

<sup>!</sup> Shape: this axis measures the consequences a disturbance may have on the network activity. For example, a vehicle running for its last journey is less critical than if it has to operate a connection.

To determine its importance, a disturbance must be evaluated according to these three axes. For example, a vehicle having off-peak hour difficulties in a suburb (a disturbance that is not critical a priori) may cause a real problem if bus frequency is such that users have to wait a long time for the next bus.

These three criteria underline the difficulty of the regulation task. The regulator has not only to establish a diagnosis on the current state problem, but also to consider its possible evolution along these three axes.

We have designed a dedicated decision support system to answer these problems. It takes into account the data coming from the existing information system (AVM system) and the environment characteristics that are as follows:

<sup>!</sup> Open environment : vehicles <sup>b</sup>appear<sup>Q</sup> and <sup>b</sup>disappear<sup>Q</sup> from the information system according to their activity or the regulator’s needs.

<sup>!</sup> Uncertain environment: in most networks, vehicles are located through sensors that provide information that may be incomplete (a sensor breaks down), or uncertain (sometimes the quality of the data is poor).

<sup>!</sup> Dynamic environment: information concerning the location of vehicles is collected every 40 s (in our network) and represents a large data stream.

A multi-agent system has been defined to manage the transportation network under normal conditions (network monitoring, dynamic schedule management, data inconsistencies management) as well as under disturbed conditions [2]. To allow the appropriate management of information related to a disturbance, we model the whole disturbance process in a dynamic way, from its beginning to its end. We integrate this disturbance model in our Multi-Agent Decision Support System (MADSS).

## 2.2. A multi-agent system (MAS) to model network activity

As said before, a decision support system is needed by regulators to diagnose disturbances on bus lines (buses running late, running early, etc.), detect inconsistency in positioning data sent by buses to the central regulator dynamically compute schedules, and monitor and process disturbances.

In order to detect the delay of a vehicle in the network, the time when the bus is theoretically due has to be compared with the current time. Timetable management involves three steps: (1) making up the theoretical timetables; (2) monitoring the network activity (modifying the timetables according to where the vehicles actually are); (3) managing the inconsistencies of the data coming from the sensors that locate the vehicles.

To automate these three functions, we have proposed two categories of agents as part of our multi-agent system [2]:

<sup>!</sup> the STOP agents, that represent the theoretical structure of the network (organized in lines and routes) and compute the theoretical timetables.

<sup>!</sup> the BUS agents, that represent the dynamic part of the network. Every BUS agent is the abstraction of an actual vehicle running on the transportation network and reports its movements to the STOP agents.

We have chosen to allow the agents to compute the theoretical timetables themselves in order to ensure that the multi-agent system is autonomous. The STOP agents have the knowledge used by the graph makers (traffic problems and passenger flow) to make up a timetable. This knowledge is also used in the assessment process and in the search for solutions to a disturbance. Ten minutes before a vehicle departure, the STOP agents compute its timetable, taking into account the time of the day.

When a vehicle passes at a stop on the network, a warning message is sent from the BUS agent to the STOP agent concerned. The STOP agent updates its timetable by removing this vehicle from the list of vehicles due. A STOP agent which does not receive any message detects an anomaly and triggers the disturbance processing presented in this paper.

## 3. Disturbance modeling

In this section, we present our modeling of a disturbance process and its integration within our multi-agent model.

The aim of our disturbance model, called Incident model, is threefold:

1. Automatically search for and collect information necessary for regulators to analyze and solve the problem. This collected information constitutes the decision context [5].

2. Dynamically update this knowledge over time: we propose a formal modeling of the information sets and the way they change according to changes on the network.

3. Summarize relevant information through several indicators.

Whereas the classical AVM systems propose an instantaneous image of the network state that regulators have permanently to analyze, our system integrates data updates in the disturbance model allowing an incident to be analyzed from its beginning to its end.

## 3.1. Definition of a disturbance

Describing a disturbance using the delay of a vehicle is not enough. For example, a vehicle may be running late, but the distance between the previous and the following vehicles is preserved. In this case, a regulator will not take the disturbance into account. He will be more interested in a vehicle with a shorter delay, but which leads to an imbalance along the line. To measure qualitatively the importance of a delay, we have taken into account its consequences on the activity of the network.

For this purpose, we have defined three information sets, also called areas (Fig. 2):

<sup>!</sup> A Successor area: This area brings together all the stops waiting for the successor of the late bus, it measures the risk assessment of a bus train (the late vehicle is caught up by the following one).

<sup>!</sup> A Critical area: This area brings together all the stops where the vehicle is late, it measures the risk assessment of a gap (the late vehicle is left behind by the preceding bus).

<sup>!</sup> A Predecessor area: This area brings together all the stops where the late vehicle is due but not yet late, it measures the risk assessment of a gap (the late vehicle is left behind by the preceding bus).

By drawing a distinction between the predecessor and critical areas, it is possible to compare incidents in terms of seriousness. For two incidents with the same number of points between the late bus and its predecessor, the incident with the greatest number of stops in the Critical area is considered as the most serious.

The set of these three areas constitutes the model that we call the Incident model (Fig. 2). The

![](/api/attachments/EYVC35P6/fulltext/images/6067e056ff09f3913eca2f492599838eed7e762106b30a340270415aadb97b2c.jpg)  
Fig. 2. Representation of a disturbance.

Incident model gathers in a single entity all the information necessary to manage a given disturbance thus helping the regulator to do its diagnosis job.

## 3.2. Formal model of a disturbance

Data arrive every 40 s which implies that the three areas involved in the Incident model have to be updated through cycles. Our model is used to verify the coherence of stops transition from one area to the other. We verify that the transitions of stops from one area to the other are related to the moves of the vehicles that have caused them.

Fig. 3 shows three successive disturbances on a line. Our model has to answer questions like: how are identified the components of these disturbances in terms of stops? How are managed the transitions of stops between two disturbances? If a new bus arrive (for instance the bus #811 for the disturbance #2), how is taken into account this bus arrival? If a bus leaves the network (for instance, the bus #806 for the disturbance #3), how is taken into account this bus leaving?

![](/api/attachments/EYVC35P6/fulltext/images/9ff2d52cba90636265c3a5eab7708ce27d15455d385572934d3fb3a8f0368683.jpg)  
Fig. 3. Static picture of disturbances on a line.

## 3.2.1. Some definitions

In this section, the main definitions used to construct the Incident model are introduced. They are important first to bring generality to our disturbance model for diagnosis analysis on a transportation system and then to precisely define the stops belonging to a given area at each cycle. Our aim is to evaluate the network evolution under a space–time point of view, that is:

n over a period of time, which stops belong to an area of the Incident model (critical, predecessor, successor area).

n for a given part of the network, how many disturbances are located in this part during a period of time?

## Definition 1: Position relation

A vehicle has to be identified according to its position in time and space.Let b be a bus; it is located at time t at the stop $a _ { i k } ^ { L } \mathrm { . }$

position : $B ^ { L } \times T {  } A _ { i } ^ { L }$

position $( b , t ) = a _ { i k } ^ { L }$

$A _ { i } ^ { L }$ is the set of stops on the line L and the route i and $B ^ { L }$ the set of buses on the line $L . \ a _ { i k } ^ { L } \ ( k ^ { \mathrm { i e m e } }$ stop on route i of line L) is the last stop where the vehicle was located.

## Definition 2: WaitingArea set

A WaitingArea is the set of stops waiting for a bus b at time t on route i of line L:

$$
\begin{array}{l} \text { WaitingArea } (b, t) \\ = \left\{a _ {i k} ^ {L} \in \text { Current   Trip } (b, t) \mid \text { position } (b, t) \right. \\ = a _ {i k ^ {\prime}} ^ {L}, k > k ^ {\prime} \} \end{array}
$$

The relation CurrentTrip represents the journey (a route with a schedule) of a bus b running at time t.

## Definition 3: NextBusWaitingArea set

To model a disturbance, we need to know the stops that a particular vehicle has to serve and which will not be served by another vehicle before its passage.

This area is related to the given bus and its preceding one. This set (called NextBusWaitingArea) is built using the difference between the WaitingArea sets of the two vehicles concerned.

$$
\begin{array}{l} \text { Next   BusWaiting   Area } (b, t) \\ = \left\{a _ {i k} ^ {L} \in \left[ \text { WaitingArea } (b, t) - \text { WaitingArea } \left(b _ {\mathrm{p}}, t\right) \right] \right\} \end{array}
$$

If b has no predecessor, $b _ { \mathrm { p } } { = } \mathrm { n u l l } .$

These preliminary definitions are useful to define the stop sets involved in the Incident model at each cycle.

## Definition 4: CriticalArea set

Let delay $( a _ { i k } ^ { L } , b , t )$ be a predicate meaning that t is greater than the theoretical time of bus b at stop $a _ { i k } ^ { L }$

The critical area of a bus b at time t is defined as follows:

$$
\begin{array}{l} \text { CriticalArea } (b, t) \\ = \left\{a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b, t) \mid \text { delay } \left(a _ {i k} ^ {L}, b, t\right) \right\} \end{array}
$$

CriticalArea(b,t) groups the stops of NextBusWaitingArea(b,t) for which the bus b is late at time t.

## Definition 5: PredecessorArea set

When the CriticalArea(b,t) exists, PredecessorArea of a bus b at time t is defined as follows:

$$
\begin{array}{l} \text { PredecessorArea } (b, t) \\ = \left\{a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b, t) \mid \neg \text { delay } \left(a _ {i k} ^ {L}, b, t\right) \right\} \end{array}
$$

PredecessorArea(b,t) is defined as the set of stops of CriticalArea(b,t) and NextBusWaitingArea(b,t) at time t.

## Definition 6: SuccessorArea set

When the CriticalArea(b,t) exists, SuccessorArea of a bus b with regard to its successor $_ { b } \cdot$ , at time t is defined as follows:

$$
\begin{array}{r l} \text { SuccessorArea } (b, t) & = \left\{a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b ^ {\prime}, t) | b ^ {\prime} \right. \\ & = \text { successor } (b) \} \end{array}
$$

This area is defined according to the successor of the bus responsible for the disturbance.

## Definition 7: Incident set

The Incident relation is the grouping of the areas described above:

$$
\begin{array}{r l} \text { Incident } (b, t) & = \text { CriticalArea } (b, t) \\ & \cup \text { PredecessorArea } (b, t) \\ & \cup \text { SuccessorArea1 } (b, t) \end{array}
$$

Incident(b, t) dynamically change from one cycle to the other which means that the number of stops in each area is modified according to the move of buses on the network.

## 3.2.2. Use of the Incident model

In this section, we want to show that the choice of sets to aggregate data improve the space–time analysis of a disturbance process in spite of any unexpected events appearing on the network. In the following, we give an example of a space analysis of the network and we show how the dynamic process of a disturbance is managed.

3.2.2.1. Space analysis of a network. To identify the stops linked to a disturbance caused by vehicle b over a period of time (between $t ^ { \prime }$ and $t ^ { \prime \prime } )$ we make the union (without doubles) of the disturbance states between $t ^ { \prime }$ and $t ^ { \prime \prime } \colon$

$$
\begin{array}{l} \text {DisturbedArea} (b, t ^ {\prime}, t ^ {\prime \prime}) = \left\{a _ {i k} ^ {L} \in \text {Incident} (b, t) \mid k ^ {\prime} \right. \\ \quad = \text {position} (b, t ^ {\prime}), k ^ {\prime \prime} \\ \quad = \text {position} (b, t ^ {\prime \prime}), t ^ {\prime} <   t <   t ^ {\prime \prime}, k ^ {\prime} <   k <   k ^ {\prime \prime} \} \end{array}
$$

Over the life cycle of a disturbance, this set gives the number of stops linked to the disturbance. This set may be used to visualize the disturbance on the network. The study of this set on a given part of the network (a finite set of stops) noted s gives us the following evaluation:

Card B<sup>s</sup> ð Þ [ DisturbedArea $( b _ { i } , t ^ { \prime } , t ^ { \prime \prime } ) \colon$ stops of s related to a i¼0 disturbance between $t ^ { \prime }$ and $t ^ { \prime \prime } .$

$\bigcap _ { i = 0 } ^ { \mathrm { C a r d } ( B ^ { s } ) }$ DisturbedArea $( b _ { i } , t ^ { \prime } , t ^ { \prime \prime } )$ : stops of s related to all disturbances between $t ^ { \prime }$ and $t ^ { \prime \prime } .$

These two results are used to visualize the stops linked to the problematic areas.

3.2.2.2. Example of a disturbance follow-up. This part illustrates how our model is used to follow the progression of a disturbance. Let us suppose that he initial situation is the following one: the bus $b _ { \mathrm { r } }$ is late and responsible for the disturbance, the bus $b _ { \mathrm { p } }$ precedes it and $b _ { \mathrm { s } }$ succeeds it. For each of these vehicles, there is a set NextBusWaitingArea(b<sub>x</sub>, t) with $( b _ { x } { = } b _ { \mathrm { p } } , \operatorname { o r } b _ { \mathrm { r } } \operatorname { o r } b _ { \mathrm { s } } ) .$

We describe the kinematics of a disturbance in the case where there is no change in the order of vehicles (no appearance or disappearance):

Creation of an Incident. At time $t ,$ an Incident is created if:

$$
\begin{array}{c} \exists a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b _ {\mathrm{r}}, t) \land \text { delay } (a _ {i k} ^ {L}, b _ {\mathrm{r}}, t) \land \\ \neg (\exists \text { CriticalArea } (b _ {\mathrm{r}}, t)) \end{array}
$$

An Incident is created if a stop that is waiting for a vehicle (not already linked to a disturbance) detects a delay with respect to the schedule.

According to the previous definitions:

CriticalArea $\left( b _ { \mathrm { r } } , t \right)$

$$
= \left\{a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b _ {\mathrm{r}}, t) | \text { delay } (a _ {i k} ^ {L}, b _ {\mathrm{r}}, t) \right\}
$$

PredecessorArea $\left( b _ { \mathrm { r } } , t \right)$

$$
\begin{array}{l} = \left\{a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b _ {\mathrm{r}}, t) \right. \\ \left. \mid \neg \text { delay } (a _ {i k} ^ {L}, b _ {\mathrm{r}}, t) \right\} \end{array}
$$

SuccessorArea $\left( b _ { \mathrm { r } } , t \right)$

$$
= \left\{a _ {i k} ^ {L} \in \text { NextBusWaitingArea } (b _ {\mathrm{s}}, t) \mid b _ {\mathrm{s}} \right.
$$

¼ successorð Þg b

The Successor area can be empty if:

<sup>!</sup> The Successor of $b _ { r }$ is unknown: it may occur if journeys are spaced out over large time intervals. In our multi-agent organization, only buses having announced their departure by asking for the creation of a schedule shortly before the departure are known. If an incident is detected whereas the schedule for the following bus has not yet been calculated, this vehicle is unknown.

<sup>!</sup> NextBusWaitingArea(b<sub>s</sub>, t) is empty: it may occur if two vehicles form a bus train (i.e., convoy), no stop is waiting for the successor.

Change of vehicle position. As described before, the content of a stop area is modified at each cycle by the move of the vehicles that surround it. The contents of ${ \mathrm { C r i t i c a l A r e a } } ( b _ { \mathrm { r } } , \ t )$ and PredecessorArea $\left( b _ { \mathrm { ~ r ~ } } t \right)$ are modified in relation to the moves of $b _ { \mathrm { r } }$ and $b _ { \mathfrak { p } }$ (according to the definition of NextBusWaitingArea) while SuccessorArea $( b _ { \mathrm { r } } , t )$ depends on $b _ { \mathrm { r } }$ and $b _ { \mathrm { s } } .$

The creation of the sets depends of the following events at time $t ^ { \prime } { : }$ the move of the bus $b _ { \mathrm { p } } ,$ , the move of the bus $b _ { \mathrm { r } } ,$ the move of the bus $b _ { \mathrm { s } }$

<sup>!</sup> The move of the bus $b _ { \mathrm { p } } \mathrm { : }$

position $( b _ { \mathsf { p } } , t ^ { \prime } ) { = } a _ { i k } ^ { L }$

We distinguish four possibilities for stops $a _ { i k } ^ { L }$ of NextBusWaitingArea(b<sub>p</sub>, t) verifying condition $k { \le } k ^ { \prime } { : }$

1. Wait $\mathsf { e d B u s } ( a _ { i k } ^ { L } , \ b _ { \mathrm { r } } , \ t ^ { \prime } ) \wedge \neg \mathrm { d e l a y } ( a _ { i k } ^ { L } , \ b _ { \mathrm { r } } , \ t ^ { \prime } ) \Rightarrow a _ { i k } ^ { L } \in$ PredecessorArea $( b _ { \mathrm { r } } , \ t ^ { \prime } )$ . Stops have a normal transition, from one waiting zone to the next.

2. WaitedBus $( a _ { i k } ^ { L } , b _ { \mathrm { r } } , t ^ { \prime } ) \wedge \mathrm { d e l a y } ( a _ { i k } ^ { L } , b _ { \mathrm { r } } , t ^ { \prime } ) \Rightarrow a _ { i k } ^ { L } \in \mathrm { C r i t - }$ ica $\mathrm { | A r e a ( } b _ { \mathrm { r } } , t ^ { \prime } ) .  { b _ { \mathrm { p } } }$ itself is late and the delay of $b _ { \mathrm { r } }$ is such that the new stops are put directly in the critical area.

3. Waited $\mathrm { B u s } ( a _ { i k } ^ { L } , b _ { \mathrm { s } } , t ) \Rightarrow a _ { i k } ^ { L } { \in } \mathrm { S u c c e s s o r A r e a } ( b _ { \mathrm { r } } , t ^ { \prime } )$ Two vehicles are sufficiently close to each other (bus train) so that stops are waiting $b _ { \mathrm { s } }$ at time $t ^ { \prime } .$

4. WaitedBus $( a _ { i k } ^ { L } , ~ b _ { \nu } , ~ t ^ { \prime } ) ^ { \wedge }$ position $( b _ { y } ) { = } a _ { i k ^ { \prime \prime } } ^ { L } \Lambda$ position $( b _ { \mathrm { s } } ) { = } a _ { i k ^ { \prime \prime } } ^ { L } \mathrm { ~ } _ { 1 } ^ { ! } k ^ { \prime \prime } { < } k ^ { \prime \prime \prime \prime } { \Rightarrow } a _ { i k } ^ { L }$ <sup>a</sup>NextBusWaiting $\mathrm { A r e a } ( b _ { y } ,$ tV).

Three vehicles are sufficiently close to each other so that stops are waiting for a vehicle $b _ { y }$ that is not linked to the disturbance and that is located after $b _ { \mathrm { s } } .$

<sup>!</sup> The move of the bus $b _ { \mathrm { r } }$ :

position $( b _ { \mathrm { r } } , t ^ { \prime } ) { = } a _ { i k } ^ { L }$

We distinguish two cases for stops $a _ { i k } ^ { L }$ of Next-BusWaitingArea $( b _ { \mathrm { r } } , t )$ verifying $k { \le } k ^ { \prime }$

1. WaitedBus(a<sub>ik</sub><sup>L</sup> ${ \cal J } _ { \mathrm { s } } , t ^ { \prime } ) { \sf \Rightarrow } a _ { i k } ^ { L } \in \mathrm { S }$ uccessor $( b _ { \mathrm { r } } , t ^ { \prime } )$ . Stops have a normal transition, from one waiting area to the next.

2. WaitedBu $\scriptstyle : ( a _ { i k } ^ { L } , \ b _ { x } , \ t ^ { \prime } ) \land \mathtt { p o s i t i o n } ( b _ { x } ) = a _ { i k ^ { \prime \prime } } ^ { L } \land \mathtt { p o s }$ ition $( b _ { \mathrm { s } } ) { = } a _ { i k ^ { \prime \prime \prime \prime } } ^ { L } \mathrm { ~ } _ { \mathrm { i } } ^ { 1 } k ^ { \prime \prime } { < } k ^ { \prime \prime \prime \prime } { \Rightarrow } a _ { i k } ^ { \ L } { \in } \mathrm { N e } \mathrm { x }$ xtBusWaitingArea $( b _ { x } , \ t ^ { \prime } )$

Vehicles $b _ { \mathrm { s } }$ and $b _ { \mathrm { r } }$ are sufficiently close to each other (bus train) so that stops are waiting for another bus $b _ { x }$ located after $b _ { \mathrm { s } }$ at time $t ^ { \prime } .$

In initial NextBusWaitingArea $( b _ { \mathrm { r } } , t )$ , stops can also move from PredecessorArea $\left( b _ { \mathrm { r } } , t \right)$ to CriticalArea $( b _ { \mathrm { r } } , t ) \colon$

$$
\begin{array}{r l} & a _ {i k} ^ {L} \in \text { PredecessorArea } (b _ {\mathrm{r}}, t) \wedge \text { delay } (a _ {i k} ^ {L}, b _ {\mathrm{r}}, t ^ {\prime}) a _ {i k} ^ {L} \\ & \quad \in \text { CriticalArea } (b _ {\mathrm{r}}, t) \end{array}
$$

<sup>!</sup> The move of the bus $b _ { \mathrm { s } } \mathrm { : }$

This case is the easiest one because the served stops are no longer taken into account by the model.

## 3.3. Indicators related to the disturbance consequences

As explained before, the Incident model brings together information on a disturbance. In this section, we show how this knowledge gives the regulator a qualitative disturbance evaluation. We propose to measure the risk of a bus train and the risk of a gap. These two indicators are based on the theoretical difficulties that the given vehicles may meet on a network subsection.

A data table is associated with each stop of the network for each period of time (classified from 0 (fluid) to 2 (heavy traffic)). These data are used to define the theoretical state of traffic and of passenger demand. These theoretical data are used to compute schedules. For instance, at the stop $p _ { 1 }$ the estimated value of traffic is 1 (the circulation is normal) and the estimated value of flow of passengers is 2 at 8 pm $( p _ { 1 }$ may be a school).

The disturbance dynamics may lead to a gap between supply and demand; when the late vehicle has to answer a strong demand, the following one deals with a weaker one. That is why we suggest to modify the initial values of the theoretical passenger flow evaluation according to their link to the areas of the disturbance. The value must be reduced for the stops in the Successor area and increased for the stops in the Critical and Predecessor areas. After various observations, we have chosen a progression indicator $I p ( y )$ for each area y, so as to take into account the seriousness of the passenger flow in the area y. It varies from 1 to 1.

Let y be an area, x the number of stops in this area, $T ( k )$ the traffic evaluation of the kth stop of the area y and $F ( k )$ the passenger flow evaluation of the kth stop of the area $y .$ The progression coefficient measures the disturbance state compared to an average situation (where $T ( k )$ and $F ( k )$ are equal to one for each k):

Let y<sub>NBW</sub>=NextBusWaitingArea(b, t)

$$
\begin{array}{l} x _ {\mathrm{NBW}} = \operatorname{Card} \left(y _ {\mathrm{NBW}}\right) \\ k _ {0} = \text { minimum } \left\{k \mid a _ {i k} ^ {L} \in (\text { NextBusWaitingArea } (b, t) \right\} \\ \text { Progression\_Coef } \left(x _ {\mathrm{NBW}}, y _ {\mathrm{NBW}}\right) \\ = \frac {\sum_ {k = k _ {0}} ^ {k _ {0} + x _ {\mathrm{NBW}}} \left[ \left(F \left(a _ {i k} ^ {L}\right) * \left(1 + I p \left(y _ {\mathrm{NBW}}\right)\right)\right) + T \left(a _ {i k} ^ {L}\right) \right] - 2 x _ {\mathrm{NBW}}}{x _ {\mathrm{NBW}}} \end{array}
$$

If this coefficient is positive, it means that the bus may slow down in the area, otherwise, it means that the area may allow the bus to make up for lost time.

We compare the progression coefficients of the areas linked to a disturbance to evaluate the risk of a bus train (Rbt) and the risk of a gap (Rgap).

(1) Risk of a bus train: Rbt

Let us consider the case where the first vehicle may be slowed down but not the following one. If the first vehicle is the late bus, then the risk of a bus train can be computed. If the first vehicle is the predecessor of the late bus, then a possible modification of the disturbance is identified. The actual disturbance may disappear and the predecessor may create a new disturbance. To calculate the risk of a bus train, we compute the difference between the Successor area progression coefficient and the Critical area progression coefficient.

$$
\begin{array}{l} \text { Let } y _ {\mathrm{c}} = \text { CriticalArea } (b, t) \\ y _ {\mathrm{s}} = \text { SuccessorArea } (b, t) \\ x _ {\min} = \text { minimum } (\text { Card } (\text { CriticalArea } (b, t)), \\ \text { Card } (\text { SuccessorArea } (b, t))). \\ \text { Rbt } (b, t) \\ = \frac {[ \text { Progression\_Coef } (x _ {\min} , y _ {\mathrm{c}}) - \text { Progression\_Coef } (x _ {\min} , y _ {\mathrm{s}}) ]}{\text { Card } (y _ {\mathrm{c}})} \end{array}
$$

![](/api/attachments/EYVC35P6/fulltext/images/80e13126c1967756ab9b286c6f1c609cbd18d812a209eb45eea58c5827e78d0f.jpg)  
Fig. 4. Dynamic organization of agents.

Since an Incident moves on the network, the number of stops in each area varies from one cycle to the other. Furthermore, to obtain comparable measures, the number of stops must be the same in the two areas. Consequently, we have chosen to compute the progression coefficient for a number of stops (noted $x _ { \mathrm { m i n } } )$ equal to the minimum number of stops in the two areas. The greater the number of stops belonging to the SuccessorArea is, the lower the risk value.

## (2) Risk of a gap: Rgap

The first vehicle may accelerate but not the following one. If the first vehicle is the predecessor of a late bus, the risk of a gap is identified. If the first vehicle is the late bus, then a possible disturbance modification is identified. The actual disturbance may disappear and the successor may create a new disturbance. To compute the risk of a gap, we compute the sum of the progression coefficient of the CriticalArea and of the PredecessorArea. The risk of a gap takes into account the number of stops between the late bus and the previous vehicle.

Let b be the late bus at time $t , x _ { \mathrm { c } }$ be the number of stops in the CriticalArea(b, t) and $x _ { \mathrm { p } }$ the number of stops in the PredecessorArea(b, t).

$$
\text { Let } y _ {\mathrm{p}} = \text { PredecessorArea } (b, t)
$$

$$
\begin{array}{r l} \operatorname{Rgap} & = \left[ \text { Progression\_Coef } (x _ {\mathrm{c}}, y _ {\mathrm{c}}) + \text { Progression\_Coef } (x _ {\mathrm{p}}, y _ {\mathrm{p}}) \right] * [ x _ {\mathrm{c}} + x _ {\mathrm{p}} ] \end{array}
$$

3.4. Integrating the disturbance model into the multiagent system

The multi-agent paradigm is well suited to integrate data management and data modeling. In order to dynamically model the disturbance process, we have defined two new types of agents. This section describes these new agents and their organization within our MADSS.

The initial organization of the multi-agent system (in lines and routes) is completed with a hierarchical organization of the agents (Fig. 4). At each level of the hierarchy, information is aggregated by the agents. The two new types of agents are the STOPAREA agents and the INCIDENT agent.

The lowest level of the hierarchy is composed of the elementary entities, the STOP agents. The middle level is composed of the STOPAREA agents that make a first information synthesis. They collect basic information such as theoretical traffic evaluation (T(k)) and passenger flow ( F(k)) from the STOP agents linked to them and they compute the progression coefficient. The INCIDENT agent represents the top of the hierarchy where risks are computed and contains the interface between regulators and the system.

This organization is dynamic because at each cycle, STOP agents move from one area to the other within the hierarchy, and from and towards the outside of the organization, according to traffic direction.

The process of hierarchy creation takes place in three stages:

<sup>!</sup> Stage 1: A STOP agent that detects a delay creates the INCIDENT and STOPAREA agents necessary to solve the problem.

<sup>!</sup> Stage 2: This STOP agent sends messages to STOP agents that are expecting the late bus or its following one. These receiver STOP agents send messages to the STOPAREA agent to which they depend.

![](/api/attachments/EYVC35P6/fulltext/images/2e36e4cd38ed35bd3c3122190a7b6d818d73641d2315d16afeb6ebd0df805908.jpg)  
0-2526-5051-75□76-100  
Fig. 5. Success rate of the predictive power of the risk of a bus train.

![](/api/attachments/EYVC35P6/fulltext/images/397e51cd765a8e21fa3c895a80ef1a12528e916ac48c5de3c116565eef90082f.jpg)  
Fig. 6. Success rate distribution.

<sup>!</sup> Stage 3: The STOPAREA agent contacts the BUS agents linked to the disturbance, the late vehicle and its following one, to inform them about the disturbance that has been detected.

Each disturbance content depends of the network activity and mostly on the appearance and disappearance of the vehicles. As an example, let us consider the following case: the planned insertion of a new vehicle by a regulator. The new vehicle is inserted between the late bus and its following one. The fact that the new vehicle becomes the following bus of the late vehicle modifies the content of the Successor area. The STOP agents that detect a modification of the next vehicle they are waiting for, contact the STOPAREA agent concerned to inform it about this event. This agent reacts by considering the new vehicle as the vehicle related to its area. The STOPAREA agent sends a message to these STOP agents to tell them that they are not linked anymore to the disturbance (the stops situated between the new successor and the former one).

When the disturbance disappears, this organization survives during some cycles to keep the continuity of the disturbance process. After this period, the created agents related to the disturbances disappeared too.

## 4. Experimental results and analyses

A prototype has been implemented in C++. The prototype has been tested using real data from the Brussels Intercity Company network (STIB). They were recorded on tapes for around 30 buses, on one line, over 8 days and represent more than 43.000 data. Our SATIR system was run on these data; it detected 300 disturbances and it recorded the disturbances data on files.

In the experiments we present here, we first give the results of the disturbances assessment then we show how some of these results are displayed to the regulators through the interface of the system.

## 4.1. Disturbance assessment

In this section, the disturbance evaluation is discussed based on two points of view: a statistical point of view: what is the predictive power of our indicators? and a qualitative point of view: are our indicators useful to sharply analyze a disturbance process?

## 4.1.1. Statistical assessment

To test the predictive power of our indicators, the first step is to obtain a coherent set of disturbance data. Since we have to deal with a huge amount of data, we have limited our study to only one bus line which is problematic. From these data, we have eliminated the data corresponding to incoherent disturbances (for instance, the disturbances related to a localization problem) and also those related to very short disturbances which are not meaningful. We want to know if our indicators are able to predict the behaviour of a disturbance after a number n of cycles (remember that each cycle lasts around 40 s). In this example, we have chosen n=7 (around 5 mn). After this consolidation of data, about 50% of the initial number of disturbances is kept.

![](/api/attachments/EYVC35P6/fulltext/images/e09bc116ae081aceb79c97c4b7579a154aa341f7a573ce7c370a85602effc4ba.jpg)  
Fig. 7. Evolution of a disturbance linked to a problematic network section.

![](/api/attachments/EYVC35P6/fulltext/images/899e908d81069af2ac9a6873674b810dff061f033807586554c31cf16e388734.jpg)  
Fig. 8. Evolution of the risk of a bus train.

For the risk of a bus train, a success is an increase (decrease) of the number of buses in the Successor area, seven cycles after a negative (positive) value of the Rtb indicator has been computed.

With this criteria, we see that the results are promising (Fig. 5) because the successful predictions represent 62.8% of the studied cases (44.19%+ 18.6%). Among the 62.8% of successful cases, Fig. 6 shows that 70% are over 60% and 40% are over 70%.

## 4.1.2. Qualitative assessment

In this section, we propose a qualitative assessment of a disturbance process. Two types of incidents are analyzed: the first characterizes a disturbance linked to a problematic section on the network, the second characterizes a disturbance linked to a vehicle.

4.1.2.1. Analysis of a disturbance linked to a problematic network section. Fig. 7 displays the evolution of the number of stops in the three Incident model areas.

If we analyze more precisely the evolution of the critical area, we may distinguish four steps:

(1) Cycles 0 to 22: the number of stops increases in an important way (from 3 to 8), which means that the late vehicle increases its delay.

(2) Cycles 22 to 30: at the end of this period the number of stops in the area is equal to 4 which means that the vehicle has caught its delay.

(3) Cycles 30 to 35: the number of stops is around 7 at the end of this period which means that the vehicle increases its delay again.

(4) Cycles 35 to 70: the number of stops stays around 8 which means that the vehicle does not catch up its delay. The decrease of the predecessor area at the end of the disturbance (Fig. 7 after cycle 55) is due to the arrival of the predecessor vehicle to the terminus (no new stop is added to the predecessor area).

This behaviour may be explained by analyzing the behaviour of the Successor and Predecessor areas through the study of our indicators (Figs. 8 and 9). The disturbance is created then the number of stops increases in the Critical area because the late vehicle is stopped. After this, the late vehicle is freed (at cycle 22) and the number of stops in the Critical area decreases (from 8 to 5) before stabilizing around 7 stops. The stops lost by the Critical area are gained by the Successor area and stabilize around 6.

![](/api/attachments/EYVC35P6/fulltext/images/2d5d13364f075d1007e04aaa4dc2c13e4a5307f7ce05c57fe3b3ff2c249916fe.jpg)  
Fig. 9. Evolution of the risk of a gap.

![](/api/attachments/EYVC35P6/fulltext/images/76dce4778458326bb0162e0d53caafd866136e0e7bd008607064c42d1671d89c.jpg)  
Fig. 10. Evolution of a disturbance linked to a vehicle.

These indicators values may help the regulator to decide when to intervene on the network. Fig. 8 shows that, if the regulator decides to intervene if the risk of a bus train or a gap increases over several cycles with value greater than 2, he has to intervene around cycle 10. The decrease of the risk after cycle 15 illustrates the risk of transfer of the disturbance from the current late bus towards the following one.

Fig. 9 shows the evolution of the risk of a gap. Since its value is less than 2, this means that the disturbance does not require any intervention from the regulator.

4.1.2.2. Analysis of a disturbance linked to a vehicle. Fig. 10 shows the evolution of a disturbance linked to a late vehicle on the network.

If we analyze more precisely the evolution of the critical area, we may distinguish four steps:

(1) Cycles 0 to 20: the number of stops evolves between 3 and 5 which means that the disturbance is stable.

(2) Cycles 20 to 37: the disturbance worsens with an increase of the number of stops from 5 to 9.

(3) Cycles 37 to 70: the disturbance remains stable with an important number of stops (an average of 8.2 stops).

(4) Cycles 70 to 90: the number of stops in the critical area increases after cycle 77. These gained stops come from the predecessor area because the predecessor vehicle has arrived at the terminus.

This vehicle seems to have had a problem at cycle 20 which creates its delay. Nevertheless, the reason of the problem seems to be punctual. The study of the risk indicators confirms this hypothesis (Figs. 11 and 12).

We see that the risk of a bus train increases up to the cycle 40 and after cycle 53. We deduce that the

![](/api/attachments/EYVC35P6/fulltext/images/bc9958ed926ee4cbd73f86e22e3e823f6778cfa46506fd074eba554a4d6ddedf.jpg)  
Fig. 11. Evolution of the risk of a bus train.

![](/api/attachments/EYVC35P6/fulltext/images/6fabd2bb5cdc29258acbcf0e134ccfc74bc253d99dee3c7bdd92b2cd8a55a051.jpg)  
Fig. 12. Evolution of the risk of a gap.

successor vehicle has no difficulty to progress. If the decision criteria for a regulator to intervene is the risk value greater than 2, Fig. 11 shows that he would intervene several times, for example at cycles 35 and 65. The risk of a bus train is not stable because the number of stops is small and the delay of the late vehicle is important. Fig. 12 shows the evolution of the risk of a gap. We see that the seriousness of this disturbance is high during two periods (cycles 20 and 60) each of them would have justified an intervention of the regulator.

![](/api/attachments/EYVC35P6/fulltext/images/4bd3a8f41ae07384c3b191bd94826d7aac46dc12e393c17551332e755d1123ab.jpg)  
Fig. 13. The regulator interface of the network incident management system.

These two examples illustrate how our Incident model allows a very sharp disturbance evaluation. Existing systems detect the vehicle delay but do not put the seriousness of these delays into perspective. Thanks to the Incident model, the regulators are able to know the real difficulties of a vehicle.

We have undertaken two types of validation: face validity with the users of our SATIR system, that is, the regulators and the decision makers in charge of the STIB network and predictive validity. As we said before, we ran our system on the data recorded by the STIB. The system detected more than 300 disturbances while the regulators were able to detect only 10% of the disturbances. It can be explained by the fact that when operators detect a disturbance, they immediately try to solve it which is time-consuming, preventing them to detect other disturbances.

## 4.2. Interface with the regulator

The interface shown in Fig. 13 is proposed to the regulators. This interface produces a summary of all the data related to the problems on the network. It contains the list of disturbances detected on the network, their identification, their location, their starting time (right top of the figure), their seriousness (disturbance analysis), the identification of the bus involved (schedule information).

One of the advantages of our system is that the regulator has no longer to choose the lines to be monitored. The interface guides him towards lines with problems. For every disturbance, the regulator has access to its description by clicking on the reference of the late vehicle (here 54814) and of the following one (here 54816). The information concerns its timetable. The assessment of the risks is given by a triangle, the distortion of which informs the regulator of the relative seriousness of the risks. If the letter (P) appears in the lists of disturbances, then some solutions have been proposed to reduce the problem (see Ref. [1] for a detailed presentation of solution formation).

## 5. Conclusion

In this paper, we have presented a decision support system that represents a global approach to the regulation task on a transportation network. The originality of our approach is the dynamic modeling of a disturbance process from its beginning to its end and its integration in a multi-agent system. We have defined a model, called the Incident model, that allows information synthesis that is useful for decision making. Through this model, knowledge relative to the network structure and knowledge relative to the network dynamics (stored in STOP agents and in BUS agents, respectively) are gathered within a single entity. This entity allows the follow-up of the disturbance over space and time; it is deleted when the disturbance is solved.

We have defined two measures of risk linked to a disturbance. These measures are based on the study of a priori progression difficulties of vehicles involved with the disturbance and take into account the intrinsic dynamics of a disturbance.

The system has been tested using real data from the Brussels Intercity Company network (STIB). It presents several advantages over existing ones: more disturbances are detected and more information is provided to the regulators in terms of risk (risk of a bus train, risk of a gap, seriousness of a disturbance). This information allows them to take quicker and more accurate decisions. More research has to be done in several directions: (1) adding more knowledge to each agent of the system and fully testing and validating the system, (2) considering using our system as a simulator in order to validate new timetables and to serve as a training tool, (3) adding an economic planning module to propose a solution to regulators according to the risk of the problem getting worse.

## References

[1] F. Balbo, ESAC: un Mode\`le d’Interaction Multi-Agent utilisant l’Environnement comme Support Actif de Communication. Application a\` la gestion des Transports Urbains, PhD thesis, Universite´ Paris IX Dauphine, (Jan., 2000).

[2] F. Balbo, S. Pinson, Towards a multi-agent modelling approach for urban public transportation systems, in: A. Omicini, P. Petta, R. Tolksdorf (Eds.), Engineering Societies

in the Agents Worlds II, LNAI 2203, Springer Verlag, Prague, 2001, pp. 160 – 174.

[3] J.H. Bookbinder, A. De´silets, Transfer optimization in a transit network, Journal of Transportation Science 26 (2) (1992 May) 106–118.

[4] P. Bre´zillon, C. Gentile, I. Saker, M. Secron, SART: a system for supporting operators with contextual knowledge, in: Federal University of Rio de Janeiro (Ed.), Proceedings International and Interdisciplinary Conference on Modeling and Using Context (CONTEXT 97), Brazil, 1997, pp. 106 – 118.

[5] P. Bre´zillon, J.C. Pomerol, Contextual Knowledge and Proceduralized Context, in Proceedings AAAI Workshop on Reasoning in Context for AI Application. AAAI Technical Report WS-99-14, AAAI Press, Menlo Park, CA, (USA, Orlando, 1999).

[6] M. Caruso, Observation du Poste de Travail de Re´gulateur dans un P.C. d’Autobus, le re´seau de la STIB a\` Bruxelles Internal Report, Institut National de Recherche sur les Transports et leur Se´curite´ (INRETS) (1997, Oct.).

[7] P. Funk, G. Vierke, H.J. B<sup>q</sup>rckert, A Multi-Agent Perspective on Intermodal Transport Chains, DFKI Technical Memo 06, (1998).

[8] Y. Goldsmith, L.R. Phillips, S.V. Spires, A Multi-Agent System for Coordinating International Shipping, Agent Mediated Electronic Trading, St Paul, Minneapolis, USA, 1998 (May).

[9] B.G. Khorovitch, G. Catalano, P. H<sup>f</sup>flinger, M. Leprince, Aspects techniques et e´conomiques de syste\`mes d’aide la de´cision, Transport Public, Union Internationale des Transports Publics, vol. 91, International Congress, Stockholm, 1991, p. 49e.

[10] Y. Li, J.M. Rousseau, F. Wu, Real–Time Scheduling on a Transit Bus Route, collection: Centre de Recherche sur le Transport (CRT) No 768; DIRO Pub. No 771 (24p.), (Apr. 1991).

[11] J. Lind, K. Fischer, Transportation Scheduling and Simulation in a Railroad Scenario: A Multi-Agent Approach, DFKI Technical-Memo-05 (1998).

[12] E. Morlok, E. Bruun, B. Blackmon, Advanced Vehicle Monitoring and Communication Systems for Bus Transit: Benefits and Economic Feasibility, Final Report September 91, Revised March 93, Office University Research and Training Program, Office of Technical Assistance Federal Transit Administration Washington, DC 20590.

[13] J. Niittym<sup>7</sup>ki, M. Pursula, Special issue: artificial intelligence on transportation systems and science, European Journal of Operational Research 131 (2) (2001) 229– 308.

[14] J.-C. Pomerol, B. Roy, C. Rosenthal-Sabroux, Developing an <sup>d</sup>intelligent<sup>T</sup> DSS for the multicriteria evaluation of railway timetables, problems and issues, Journal of Decision Systems 5 (3–4) (1996) 249 – 267.

[15] G. Scemama, E. Gaudin, Informatisation de la de´cision dans l’exploitation du transport, atouts des technologies avance´es du traitement de l’information, Recherche Transports Se´curite´ (RTS) 61 (1998 (Oct.–Nov.)) 53 – 72.

[16] R. Schleiffer, Transportation Reasearch part C: emerging technologies (special issue), Volume 10C, Numbers 5–6: Intelligent agents in traffic and transportation, 2002, 202 pp.

[17] G. Weiss, Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence, MIT Press, 1999.

[18] K. Zhu, M.W. Ludema, R.E.C.M. van der Heijden, Air cargo transport by multi-agent based planning, 33rd Hawaii International Conference on System Sciences, USA, Hawaii, 1998.

Flavien Balbo is Assistant Professor in Computer Science at University Paris 9-Dauphine. He received a MSc in Applied Mathematical Science and a PhD in Computer Science from Paris 9 University. He is associate researcher at INRETS (National Institute of Transport and Security). His primary research focuses on the real time Decision problem. His other research interests include multiagent system and specially interaction within a multi-agent system.

Suzanne D. Pinson is Professor of Computer Science in University Paris 9-Dauphine. She is Head of the Research Group in Artificial Intelligence and Decision Processes at the CNRS LAMSADE laboratory. She received a MS and a PhD in Computer Science from Paris 6 University as well as a MS in Computer Science and Operational Research from Northwestern University, Evanston, IL. She wrote a book on Cluster Analysis and has published numerous papers on Data Analysis, Knowledge Based Systems, Distributed Artificial Intelligence, Multi-Agent Systems. She is on the editorial board of several international journals. Suzanne Pinson area of research concern Distributed Decision Making and Multi-Agent Systems, more precisely, coordination and cooperation in MAS based on decision theory approach Other research interests include framework for the development of management and financial distributed decision support systems.
