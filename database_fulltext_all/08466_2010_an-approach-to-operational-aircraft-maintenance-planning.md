---
otero_id: 8466
otero_key: "C9AJTZSZ"
title: "An approach to operational aircraft maintenance planning"
authors: "N. Papakostas; P. Papachatzakis; V. Xanthakis; D. Mourtzis; G. Chryssolouris"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.11.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach to operational aircraft maintenance planning

N. Papakostas, P. Papachatzakis, V. Xanthakis, D. Mourtzis, G. Chryssolouris ⁎

Laboratory for Manufacturing Systems and Automation, Department of Mechanical Engineering and Aeronautics, University of Patras, Patras 265 00, Greec

a r t i c l e i n f o

Article history: Received 6 May 2008 Received in revised form 16 November 2009 Accepted 30 November 2009 Available online 4 December 2009

Keywords: Decision support systems Arti<sup>fi</sup>cial intelligence Aircraft maintenance Multiple criteria analysis Operational risk assessment

## a b s t r a c t

This paper describes a short-term planning methodology of the line maintenance activities of an airline operator, at the airports, during turn-around time (TAT). The proposed methodology supports decision making for deferring maintenance actions that affect the dispatching of the aircrafts, aiming at high <sup>fl</sup>eet operability and low maintenance cost. Based on health assessment and additional information regarding operational and economical constraints at the operator's <sup>fl</sup>eet level, a multi-criteria mechanism evaluates a set of generated maintenance plan alternatives. An alternative is de<sup>fi</sup>ned as the possible allocation of all deferred maintenance tasks to a set of suitable airport resources. The selected decision making criteria are cost, remaining useful life (RUL), operational risk and <sup>fl</sup>ight delay. A series of experiments is conducted in order to validate and test the approach.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Airline operators' scheduling logistics deal with the following four areas [24]: a) the schedule preparation, where airlines identify a list of <sup>fl</sup>ight legs along with departure and arrival times; b) the <sup>fl</sup>eet assignment problem, whose objective is to identify the aircraft types that will be <sup>fl</sup>ying speci<sup>fi</sup>c <sup>fl</sup>ight legs; c) the aircraft routing area, where aircrafts (tail numbers) are assigned to routes and d) the disruption recovery problem, whose obiective is to react to all operational disruptions due to extreme weather conditions, breakdowns or equipment failures that may take place during the daily operation. Long-term maintenance plans are developed in the context of the <sup>fi</sup>rst three areas. However, any unexpected events occurring daily upset these plans and lead to less effective maintenance policies. Taking into consideration the estimations reported by the industry of aeronautics, the maintenance activities range from 10% to 20% of an operator's direct operating costs depending on the <sup>fl</sup>eet size, age and usage. According to the International Civil Aviation Organization [14], the average <sup>fi</sup>gure is 11% but this average includes individual <sup>fi</sup>gures as high as 25%. The contribution of the maintenance costs to the average direct operating costs has not been reduced signi<sup>fi</sup>cantly over the last two decades. Additionally, 80% of the inspection and access activities do not lead to a repair that would be increasing the overall cost.

Aircraft operability is considered a major requirement by each airline operator. The occurrence of unscheduled maintenance can introduce costly delays and cancellations if the problem cannot be recti<sup>fi</sup>ed in a timely manner. Aircraft operability is the aircraft's ability to meet the operational requirements in terms of operational reliability (the percentage of scheduled <sup>fl</sup>ights, which depart and arrive without incurring a chargeable – technical – operational interruption), operational risk (the risk of causing additional costs by unscheduled maintenance events) and costs (maintenance and operational). The trade-off is very complex and priorities may vary a lot depending on the airline's policy.

## 1.1. Basic concepts

The process of line maintenance takes place within the turnaround time (TAT) between two <sup>fl</sup>ights with the aim to guarantee in time and reliable aircraft dispatch. The line maintenance process includes a routine check, post-<sup>fl</sup>ight inspection and malfunction recti<sup>fi</sup>cation to be performed en-route and at base stations during transit, turn-around or night stop. Within TAT, a GO/NOGO decision is typically taken with respect to the aircraft's next <sup>fl</sup>ight. The current GO/NOGO decision making process is based on the assessment of the MMEL (Manufacturer Minimum Equipment List), namely the certi<sup>fi</sup>- cation of the proper functionality of the aircraft's minimum number of critical components. If all MMEL relevant constraints could be satis<sup>fi</sup>ed, the aircraft status would become a GO and the aircraft would be able to perform the next <sup>fl</sup>ight turn. Today's decision support process is reactive and is based on unscheduled maintenance, during which, a troubleshooting process identi<sup>fi</sup>es the real root-cause, so that the necessary maintenance actions may then be carried out.

## 1.2. State of the art

A number of publications address airline planning problems (<sup>fl</sup>eet assignment, aircraft routing, maintenance management, etc.) particularly, in the Operations Research literature. In [24], one of the relevant and most recent publications as to the work of this paper, an operational aircraft maintenance routing problem formulation is addressed with the use of a branch-and-price algorithm aiming at minimizing the number of the aircraft's unused legal <sup>fl</sup>ying hours. The problem formulation includes maintenance resource availability constraints, where a branch-and-price algorithm is used for exploring the ef<sup>fi</sup>- ciency of the maintenance routing solutions. In [25], overviews of the recent advances in models and approaches that have been developed for the <sup>fl</sup>eet assignment problem (FAP) are presented, integrating maintenance activities as well. Similarly, in [8] and [9], an overview of the extensive use of operations research and management science methodologies, including <sup>fl</sup>eet scheduling and maintenance routing, is given in all the areas of airline operations. Quana et al. [23] address a cost effective multi-objective preventive maintenance-scheduling problem at aircraft service centers using evolutionary algorithms. Dijkstra et al. [11] investigate a capacity planning problem of the aircraft maintenance personnel with the use of mathematical models and approximation techniques based on Lagrangian relaxation. In [12], a combination of a dynamic programming approach (to cope with the <sup>fl</sup>eet assignment problem) together with a heuristic technique (to solve the embedded maintenance schedule problem) is presented. In [30], a mathematical programming model is described for optimizing maintenance person-power allocation in order for flight schedule punctuality to be ensured. In [26], the obiective is to minimize the aircraft maintenance cost and all associated costs incurred, based on a mathematical formulation for modelling the maintenance-scheduling problem and for using a combination of “depth <sup>fi</sup>rst search” and “random search” in order for a solution to be derived. Gopalan and Talluri [13] propose the use of Eulerian graphs, involving concepts, such as: <sup>fl</sup>eet assignment, maintenance opportunities and <sup>fl</sup>ight numbering, which are taken into consideration when making a decision for a <sup>fl</sup>ight schedule. In [10] with a given set of <sup>fl</sup>ights and speci<sup>fi</sup>ed maintenance locations, durations, and needed frequency, Lagrangian relaxation and sub-gradient optimization are used in order for the aircraft rotation problem to be solved by maximizing the bene<sup>fi</sup>t derived from speci<sup>fi</sup>c connections made.

Research in maintenance planning has often been associated with relevant maintenance procedures in nuclear plants. In [19], a genetic algorithm (GA) implementation is utilized for optimizing the components maintenance periods. In [17], a maintenance risk–cost model is established for maintenance optimization in a nuclear power plant using a GA. In [28], a maintenance-scheduling solution that optimizes both cost and reliability simultaneously by using an evolutionary algorithm has been described.

An increasingly competitive marketplace in aeronautics, where a number of applications are claimed to provide decision support for maintenance planning, has been developed over the last years. AIRBUS claims that with AIRMAN<sup>®</sup>, one of the most widely known commercially available Maintenance Information Systems, maintenance actions can be planned according to the <sup>fl</sup>eet schedule [1]. Boeing claims that AHM can provide support to make <sup>fi</sup>x-or-<sup>fl</sup>y decisions and to avoid maintenance related schedule delays [2]. Mxi Technologies claims that Maintenix<sup>®</sup> [21] processes signi<sup>fi</sup>cant amounts of data, yielding numerous performance indicators including maintenance hours per <sup>fl</sup>ight hour, maintenance incurred <sup>fl</sup>ight delays, inventory ef<sup>fi</sup>ciency as well as various reliability metrics such as the mean time between failures, removals, and unscheduled removals (MTBF, MTBR, and MTBUR, respectively). These market tools integrate information from various data sources and provide a well developed user interface environment for data retrieval and visualisation on assisting the planner to make a decision. Decision support systems addressing similar problems in other domains include the ones dealing with the dynamic vehicle refuelling problem, where the objective is to minimize the cost of buying fuel in a given route by selecting optimal truck stops and quantities [27], as well as agent-based systems for addressing the distributed constrained scheduling problem, for improving the supply chains' level of cooperation [18].

Although much progress has been accomplished over the last decade and more sophisticated Maintenance Information and Decision Support Systems have been implemented, most of these approaches have limitations. GO/NOGO decisions are not directly supported and the academic demonstrators so far supporting this kind of functionality have limited intelligence without concurrently taking into consideration parameters such as possible <sup>fl</sup>ight delay, cost consequences and actual remaining useful life of aircraft systems and components. Another aspect the paper addresses is the time and the effort required for the maintenance engineer, at line maintenance, to go through the information available and to make the best possible decision for a maintenance task allocation between two <sup>fl</sup>ights. These arguments are also supported by the fact that there is a lack for communication between operational planning and maintenance planning, resulting in high operational costs and low operational reliability despite the materialization of operational and maintenance planning approaches into software systems [29].

Despite the similarity of all these studies, none has addressed the problem as this paper has. Most of these studies focus on long-term planning problems rather than on short-term operational decisions. In the few studies that are relevant, the actual remaining useful life of the aircraft components, the maintenance cost, the risk for an unscheduled event and the resource constraints (i.e., <sup>fl</sup>ight delay or maintenance opportunity) at the maintenance stations have not been considered concurrently. In practice, most of the current approaches batch the multiple maintenance requirements, corresponding to the aircraft's components, into a package. The remaining <sup>fl</sup>ying hours of this package are de<sup>fi</sup>ned as the minimum of the remaining <sup>fl</sup>ying hours of the components belonging to this package [24]. Furthermore, the time variable, including arrivals, TAT, departures and possible delays is not taken into account at full extent, considering the overnight stations only and therefore excluding possible maintenance actions that could take place during the TAT.

This paper discusses a maintenance decision support framework based on previous research carried out by Chryssolouris et al. [4–7], for addressing short-term operational maintenance decisions at line maintenance and for deferring maintenance actions that affect the aircrafts' dispatching. The major driver is the requirement for high <sup>fl</sup>eet operability and the inevitable requirement for low maintenance costs. Based on health assessment information and additional information on operational and economical constraints at aircraft and <sup>fl</sup>eet level, the short-term planning of the operational maintenance activities at line maintenance is modelled and executed. At the next level, the long-term scheduled maintenance planning could be controlled accordingly.

The software development of the maintenance planning framework described in the context of this paper <sup>fi</sup>ts well in the Decision Support layer of the Open System Architecture — Condition Based Maintenance (OSA-CBM) speci<sup>fi</sup>cations promoted by the MIMOSA organization. The OSA-CBM speci<sup>fi</sup>cation is a standard architecture for moving information into a condition-based maintenance system. The reasons that this architecture has been selected are that as concluded from [15], [16] and [22], future developments on maintenance head towards the diagnostics, prognostication and Condition Based Maintenance (CBM) technology and systems.

## 1.3. Description of the problem and the proposed approach

Scheduling the maintenance activities at Line Maintenance combines the information from health assessment procedures with the data available related to the <sup>fl</sup>ight operations, the maintenance costs, the maintenance resources availability and the overall maintenance programme in order for the most ef<sup>fi</sup>cient maintenance schedule, according to the operator's maintenance policy, to be generated.

The proposed approach takes advantage of concepts and techniques originating from the multi-criteria decision making models as well as from simulation, in order for different maintenance plans to be produced and evaluated.

Based on the approach introduced by Chryssolouris et al. [3,6] for addressing decision making problems in manufacturing, the steps followed at each decision point, where a decision should be made for the aircraft's maintenance tasks, are:

• identify required maintenance tasks;

• determine decision criteria and weights for evaluating alternatives (maintenance plans);

• form alternatives (maintenance plans); and

• determine the consequences of the different alternatives and their utility.

When the aircraft arrives at the airport, the line maintenance process is initiated, including maintenance data acquisition, aircraft status assessment as well as maintenance decision tasks to be executed. If all MMEL relevant constraints could be ful<sup>fi</sup>lled, the aircraft status would become a GO and the aircraft would be able to perform the next <sup>fl</sup>ight turn. The proposed approach supports the decisions that should be made for the aircraft's pending maintenance tasks (that can be deferred): the decision may refer either to the tasks that are to be released and executed at the current airport or to be executed at the successive airports.

According to the proposed approach, at any point of time and location that a maintenance decision should be made concerning the maintenance tasks that can be deferred by the Line Maintenance engineer, a set of feasible alternatives is produced constituting a decision matrix [6]. An alternative is the possible allocation of pending maintenance tasks to suitable resources either at the current or at successive airports, desirably, within the timeframe of the respective component's remaining useful life (RUL) prediction. A suitable resource is an airport station capable of dispatching a speci<sup>fi</sup>c maintenance task. A maintenance task may represent a standalone activity or a group of activities together (e.g., disassembly, inspection and/or replacement) for a particular aircraft component or subsystem. The availability of each station is expressed in terms of person-power per speci<sup>fi</sup>c time period, taking into account the demand posed by other airline operators and aircrafts.

Each decision alternative constitutes of Y maintenance tasks assignments, denoted as $R _ { i , j } , T _ { y } .$ . An assignment $R _ { i , j } , T _ { y }$ is the assignment of task $T _ { y }$ on station i of airport j. The total number of different alternatives (TNA) that can be investigated is equal to:

$$
T N A = \prod_ {y = 1} ^ {Y} r _ {y}\tag{1}
$$

where $r _ { y }$ is the total number of candidate airport stations that could be used for carrying out maintenance task $T _ { y } .$

The proposed approach employs two search parameters [3,6]:

• the maximum number of alternatives MNA (MNA≤TNA), which represents the upper limit of the alternatives generated and evaluated and

• the sampling rate (SR), which represents the number of times an alternative is simulated; since duration of <sup>fl</sup>ights, maintenance times and departure delays are considered being stochastic variables following a statistical distribution, an increased sampling rate would normally lead to more accurate estimates of the alternatives' performance.

Each time a decision point is reached, i.e. when an aircraft is brought to a landing and one or more components are considered for maintenance, MNA alternatives are randomly generated and each one of them is simulated SR times.

Fig. 1 depicts the short-term planning process for supporting decisions in order for the TAT maintenance actions to be executed. This process has been implemented in the form of a software system. Based on the list of tasks for which a decision should be made, a set of feasible alternatives is identi<sup>fi</sup>ed. The alternatives are simulated SR times and their average performance against each criterion is estimated in the form of a decision matrix (Table 1). The alternative with the best utility is the one eventually proposed by the system.

The following indices and variables are used in the proposed approach:

<table><tr><td>x</td><td>the aircraft identity identifier</td></tr><tr><td>y</td><td>the running number of pending tasks for aircraft x</td></tr><tr><td> $R_{i,j}$ </td><td>the resource i at the airport j</td></tr><tr><td> $RTS_{i,j,p}$ </td><td>the start time of period p of the resource i at the airport j</td></tr><tr><td> $RTE_{i,j,p}$ </td><td>the end time of period p of the resource i at the airport j</td></tr><tr><td> $RTP_{i,j,p}$ </td><td>the person-power available during period p of the resource i at the airport j</td></tr><tr><td>i</td><td>the running number of resources at the j airport</td></tr><tr><td>j</td><td>the running number of airports</td></tr><tr><td> $T_y$ </td><td>the maintenance task y</td></tr><tr><td colspan="2"> $t(T_y,R_{i,j})^{start}$ ,  $t(T_y,R_{i,j})^{comp}$  start and completion time of the dispatch of maintenance task y in  $R_{i,j}$ </td></tr><tr><td> $t_y^{dur}$ </td><td>the time required for the completion of the maintenance task y</td></tr><tr><td> $t_y^{person}$ </td><td>the person-power required for the completion of the maintenance task y</td></tr><tr><td> $t_y^{rul}$ </td><td>the due time of  $T_y$  according to the airline&#x27;s policy</td></tr><tr><td> $t(T_y,R_{i,j})^{rul}$ </td><td>the remaining useful life of the component corresponding to task  $T_y$ , which is allocated to the resource  $R_{i,j}$ </td></tr><tr><td> $Al_k$ </td><td>the alternative k</td></tr><tr><td>k</td><td>the running alternative number</td></tr><tr><td> $Cost(Al_k)$ </td><td>the overall performance value of alternative k against the cost criterion</td></tr><tr><td> $RUL(Al_k)$ </td><td>the overall performance value of alternative k against the RUL criterion</td></tr><tr><td> $Risk(Al_k)$ </td><td>the overall performance value of alternative k against the operational risk criterion</td></tr><tr><td> $fd(Al_k)$ </td><td>the overall performance value of alternative k against the flight delay criterion</td></tr><tr><td> $Utility(Al_k)$ </td><td>the overall performance value of alternative k against the four criteria used.</td></tr></table>

Summing up, at each decision point, i.e., when the aircraft is expected to land or during inspection, the mechanism can be activated for the deferred tasks, in order to be identi<sup>fi</sup>ed where each task is to be dispatched.

## 1.3.1. Alternatives and utility

The possible execution of each alternative results in different economical and operational risk consequences. As already mentioned an alternative is de<sup>fi</sup>ned as the possible allocation of pending maintenance tasks to suitable resources either at the current or at successive airports.

In calculating the performance of the alternatives (i.e., utility), let us assume the situation in which there are K decision alternatives denoted $A l _ { 1 } , A l _ { 2 } , . . . , A l _ { k } , . . . , A l _ { K } .$ Four criteria have been identi<sup>fi</sup>ed as being suitable for the evaluation process of the alternatives: cost, operational risk, flight delay and remaining useful $l i f e \mathrm { ~ - ~ } R U L$ . The objective of a maintenance engineer would be to minimize, if possible, all four criteria. The consequences of the assignments can be measured taking into consideration the average values of the SR samples of each alternative for the selected C criteria.

![](/api/attachments/C9AJTZSZ/fulltext/images/80c5f54a8c68e76c57dcf37d0883719072079f8e511c55dbbba7c873e6a73b05.jpg)  
Fig. 1. Maintenance alternatives generation and evaluation at a decision point.

These values are then normalised according to Eq. (2).

$$
\overline {{c _ {c , k}}} = \frac {c _ {c} ^ {\max} - c _ {c , k}}{c _ {c} ^ {\max} - c _ {c} ^ {\min}}\tag{2}
$$

where, $c _ { c } ^ { \mathrm { m a x } } , c _ { c } ^ { \mathrm { m i n } }$ are the maximum and minimum values observed for criterion c for all K alternatives. Consequently, the utility of each alternative can be calculated according to Eq. (3), having combined the consequences of all criteria with weights w .

$$
u _ {k} = \sum_ {c = 1} ^ {C} w _ {c} \cdot \overline {{c _ {c , k}}}.\tag{3}
$$

In case that the alternative with the best utility allocates tasks at the current airport stations, then the respective tasks could be selected by the maintenance engineer for execution in the current airport at the current decision point. If the alternative with the best utility does not include assignments for the current airport, then the tasks may not be executed at the current airport and the decision for their allocation could be transferred to the next decision point (one of the next bases).

## 1.3.2. Constraints

In this paper, we adapt and extend the constraints model introduced by Sarac et al. [24] to account for the different components' maintenance requirements as well as for the time aspects, including the exact arrival, departure and maintenance times in addition to possible <sup>fl</sup>ight delays. The number of suitable airports' maintenance stations is <sup>fi</sup>nite, while their available person-power is limited and provided to other airline operators and aircrafts as well.

An example of an airport's resource of person-power availability is depicted in Fig. 2. The maintenance engineer is aware of this information and constitutes input to the proposed system.

If $Q _ { i , j , y }$ is equal to 1 when the task y is dispatched to airport j and resource i and 0 otherwise, then for each alternative $A l _ { k } \mathrm { : }$

$$
R T P _ {i, j, p} \geq \sum_ {y = 1} ^ {Y} (t _ {y} ^ {\text { person }} \cdot Q _ {i, y}), \forall p: R T S _ {i, j, p} \leq t (T _ {y}, R _ {i, j}) ^ {\text { start }} \land R T E _ {i, j, p} \geq t (T _ {y}, R _ {i, j}) ^ {\text { comp }}.\tag{4}
$$

Eq. (4) implies that the total amount of the person-power required for dispatching the tasks of the alternative $A l _ { k }$ should not exceed the available person-power in the existing resources per period coinciding with the start and the end of each task $T _ { y } .$ The start time of each maintenance task $T _ { y }$ is therefore the closest time to an aircraft's arrival at the airport j, satisfying the person-power availability of resource i, while:

$$
t (T _ {y}, R _ {i, j}) ^ {\mathrm{comp}} = t (T _ {y}, R _ {i, j}) ^ {\mathrm{start}} + t _ {y} ^ {\mathrm{dur}}.\tag{5}
$$

## 1.3.3. Cost criterion

The costs related to aircraft maintenance encompass a number of different factors, which can be classi<sup>fi</sup>ed into the following categories:

<table><tr><td>Alt</td><td>Cost</td><td>RUL</td><td>Operational risk</td><td>Flight delay</td><td>Utility</td></tr><tr><td> $Al_{1}$ </td><td> $Cost(Al_{1})$ </td><td> $RUL(Al_{1})$ </td><td> $Risk(Al_{1})$ </td><td> $fd(Al_{1})$ </td><td> $Utility(Al_{1})$ </td></tr><tr><td> $Al_{2}$ </td><td> $Cost(Al_{2})$ </td><td> $RUL(Al_{2})$ </td><td> $Risk(Al_{2})$ </td><td> $fd(Al_{2})$ </td><td> $Utility(Al_{2})$ </td></tr><tr><td> $Al_{3}$ </td><td> $Cost(Al_{3})$ </td><td> $RUL(Al_{3})$ </td><td> $Risk(Al_{3})$ </td><td> $fd(Al_{3})$ </td><td> $Utility(Al_{3})$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $Al_{k}$ </td><td> $Cost(Al_{k})$ </td><td> $RUL(Al_{k})$ </td><td> $Risk(Al_{k})$ </td><td> $fd(Al_{k})$ </td><td> $Utility(Al_{k})$ </td></tr></table>

![](/api/attachments/C9AJTZSZ/fulltext/images/e547e1b2d6bdea336f26c3d146374705ede0d1dc692e8f56f10bb2cd8919573a.jpg)  
Fig. 2. Available person-power per period for an airport resource (station).

• Equipment and facility costs. These include the costs of equipment necessary for the maintenance processes, the facilities used for hosting the equipment, for maintaining the infrastructure, for hiring equipment, etc.

• Supplies and logistics costs. Costs of components, logistics and transportation including excess inventory and backlog.

• Personnel costs. The labour cost required for the execution of the maintenance tasks, including costs of overtime, extra shifts, subcontracting, hiring maintenance engineers and technicians.

• Overhead. This is a part of the cost that is not directly attributable to the maintenance operations, nonetheless, it is required.

A “techno-economical” model [3] is used in Eq. (6) for modelling the impact of the maintenance attributes on the cost of aircraft maintenance. The overall contribution of these attributes is proportional to the operating time.

$$
\begin{array}{l} \text {Maintenance} \\ \text {cost per task} \\ \text {per component} \end{array} = \left( \begin{array}{c} \left(\text {Equipment rate + Labour rate + Overhead rate}\right) \\ \times \text {Operating time per component}\right) \\ + \text {Component procurement costs} \end{array}\tag{6}
$$

where:

Maintenance cost per task per component the cost of completing a maintenance activity for a component on a speci<sup>fi</sup>c resource.

Equipment rate the rate related to ground equipment and to the costs of facilities.

Labour rate the labour rate at the airport where the task can be executed. Overhead rate the rate of the overheads including Maintenance Management costs.

Operating time per component $( t _ { y } ^ { d u r } )$ the duration in minutes, required for the related maintenance task to be executed at the respective airport.

Component procurement costs the cost related to the respective component's procurement and transportation costs.

$$
C o s t (A l _ {k}) = \frac {\sum_ {s = 1} ^ {S R} \sum_ {y = 1} ^ {Y} C o s t (T _ {y} , R _ {i , j}) _ {s}}{S R}\tag{7}
$$

where $C o s t ( T _ { y } , R _ { i , j } ) _ { s }$ is the consequence cost value of the $T _ { y } , R _ { i , j }$ assignment with respect to the cost criterion for the $s ^ { \mathrm { t h } }$ sample of alternative Al .

## 1.3.4. RUL criterion

The RUL criterion takes into consideration the time during which the respective maintenance task is completed against the operator's due date policy for maintenance or replacement. The de<sup>fi</sup>nition of the due date is based on the respective components' probability of failure and on the operator's policy, $\mathrm { e . g . }$ , for components with soft degradation curve, a loose due date policy may be applied, while components that degrade fast may follow a more conservative due date policy. This criterion is used in order for the RUL to be considered during the alternatives' assessment, aiming at minimizing the remaining useful life or the degree of exceeding the due time of the components.

$$
R U L (T _ {y}, R _ {i, j}) = t (T _ {y}, R _ {i, j}) ^ {\mathrm{rul}}.\tag{8}
$$

The variable $t ( T _ { y } , R _ { i , j } ) ^ { \mathrm { r u l } }$ represents the remaining useful life of task $T _ { y }$ when it is allocated to the resource $R _ { i , j }$

The RUL criterion value of an alternative $k , R U L ( A l _ { k } )$ , is calculated by the following equation:

$$
R U L \left(A l _ {k}\right) = \frac {\sum_ {s = 1} ^ {S R} \sum_ {y = 1} ^ {Y} \left\{w r _ {y} \cdot \left| R U L \left(T _ {y} , R _ {i , j}\right) _ {s} \right| \right\}}{S R}\tag{9}
$$

where $w r _ { y }$ is the weight per task, re<sup>fl</sup>ecting the relative importance, in terms of RUL, of different components.

## 1.3.5. Operational risk criterion

The operational risk (OR) stands for the risk of disrupting the <sup>fl</sup>eet operational plan and causing additional costs due to unscheduled maintenance events. The operational risk assessment is the estimation of both cost and probability of unscheduled maintenance events that interrupt the <sup>fl</sup>eet operational plan. The expected values as de<sup>fi</sup>ned in the probability theory are used for modelling the operational risk function. Particularly, the expected value of a random variable is the sum of the probability of each experiment's possible outcome, multiplied by the outcome value (or payoff). Comparatively, the expected gain of a maintenance task allocation regarding the operational risk could be a measure of the cost of scheduled and unscheduled events of the respective allocation, weighted by the probability of failure. The symbolic expression of this concept is simple:

$$
R i s k (T _ {y}, R _ {i, j}) = [ D V (T _ {y}, R _ {i, j}) \cdot D P (T _ {y}, R _ {i, j}) ] + [ U n D V (T _ {y}, R _ {i, j}) \cdot U n D P (T _ {y}, R _ {i, j}) ]\tag{10}
$$

where,

$$
\begin{array}{l l} \text {Risk} (T _ {y}, R _ {i, j}) & \text {expected OR value for a (T_{y} ,R_{i,j}) allocation} \\ D V (T _ {y}, R _ {i, j}) & \text {desirable value, i.e., cost of scheduled events} \\ D P (T _ {y}, R _ {i, j}) & \text {probability of a desirable value} \\ U n D V (T _ {y}, R _ {i, j}) & \text {undesirable value, i.e., cost of unscheduled events} \\ U n D P (T _ {y}, R _ {i, j}) & \text {probability of an undesirable value} \end{array}
$$

The OR utility value of an alternative k, Risk(Al<sub>k</sub>), is calculated by the following equation:

$$
R i s k (A l _ {k}) = \frac {\sum_ {s = 1} ^ {S R} \sum_ {y = 1} ^ {Y} R i s k (T _ {y} , R _ {i , j}) _ {s}}{S R}.\tag{11}
$$

## 1.3.6. Flight delay criterion

An important criterion during the decision making process is the one related to the <sup>fl</sup>ight delay. It is important that the aircraft leave on time, or in case there is a delay, to be the least possible.

A delay measure is used for assessing the alternatives' performance in terms of the aircraft delay due to a maintenance action. The <sup>fl</sup>ight duration, the maintenance task duration and the departure delay are modelled as stochastic variables following a normal distribution [20], according to the data available for each speci<sup>fi</sup>c leg of a route. The

Table 3 Flight plan.

Table 4

<sup>fl</sup>ight delay value of an alternative $k , f d ( A l _ { k } )$ , is calculated by the following equation:

$$
f d (A l _ {k}) = \frac {\sum_ {s = 1} ^ {S R} \sum_ {l = 1} ^ {L} \left\{\max [ (A T _ {l , s} - A T _ {l} ^ {\text { due }}) , 0 ] + \max [ (D T _ {l , s} - D T _ {l} ^ {\text { due }}) , 0 ] \right\}}{S R}\tag{12}
$$

where $A T _ { l } ^ { \mathrm { d u e } } , D T _ { l } ^ { \mathrm { d u e } }$ the planned arrival and departure times per leg l of the route, and $A T _ { l , s } , D T _ { l , s }$ the actual arrival and departure times observed in the sample s of the alternative $A l _ { k } .$

## 2. Pilot case

The proposed decision support approach has been materialized in a prototype software framework. This software prototype consists of a java library (jar), utilizing XML <sup>fi</sup>les for handling the input and output data. A scenario follows that demonstrates the framework's capabilities.

## 2.1. Scenario

An aircraft has to perform a route consisting of a set of <sup>fl</sup>ights connecting 4 airports. One of them is the base airport. So it may have access to four (4) line maintenance facilities, and one (1) hangar facility at its own main base. The route concerns one day <sup>fl</sup>ights: FRANNCDGNNMUCNNMADNNFRA. Two (2) deferred tasks corresponding to two parts are considered with different degradation curves and a due date policy for inspection and maintenance. All the airports are capable of undertaking both maintenance tasks, having at least one suitable resource (station) for each task. The availability of each station is different and is expressed in terms of person-power available per speci<sup>fi</sup>c time period. The base airport (FRA) has two facilities. The maintenance tasks include inspection and the parts' maintenance. Both component parts are available at the base airport as well as at the other airports, but at a higher cost, in case they need to be replaced. It is assumed that when the aircraft is grounded, there is no degradation. We assume it is now 04:00 in the morning, the aircraft is located in the base airport (FRA) and the maintenance engineer has to decide in which airport station the two maintenance tasks will be carried out.

## 2.2. Maintenance tasks description

The types of activities addressed in today's TAT are GO or NOGO decision for the aircraft's next <sup>fl</sup>ight, based on the assessment of the MMEL (Manufacturer Minimum Equipment List). A major dif<sup>fi</sup>culty in proactively planning the Line Maintenance operations is to react shortly and decide, taking into consideration information related to the health assessment of the components, the availability of resources and alternative maintenance opportunities. Therefore, a major issue for the planning of the short-term maintenance activities is the ability to assess maintenance alternatives in the form of deferring tasks, in the main base or in the outer base, while being <sup>fl</sup>exible and adaptive to operational and economical constraints.

According to an assumed probability of failure, which leads to a due date, the two parts of the pilot case should be inspected and maintained within the next 10 <sup>fl</sup>ight hours (FH). The model assumes that both tasks, T1 and T2, are mutually independent (there are no pre-condition relations to force other sequences of maintenance events). Table 2 depicts the time requirements corresponding to every airport's suitable maintenance resource.

The <sup>fl</sup>ight plan to be considered in calculations along with the characteristics of the normal distributions representing the <sup>fl</sup>ight duration and the departure delay is depicted in Table 3.

Table 2  
Task duration per airport facility.

<table><tr><td>Airport</td><td>Resource ID</td><td>Task</td><td>Operation time mean, deviation (min)</td><td>Person-power required</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_1$ </td><td>60,10</td><td>1.0</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_2$ </td><td>40,5</td><td>1.0</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_1$ </td><td>70,10</td><td>1.0</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_2$ </td><td>60,20</td><td>1.0</td></tr><tr><td>CDG</td><td> $R_{CDG\_1}$ </td><td> $T_1$ </td><td>80,20</td><td>1.0</td></tr><tr><td>CDG</td><td> $R_{CDG\_1}$ </td><td> $T_2$ </td><td>70,10</td><td>1.0</td></tr><tr><td>MUC</td><td> $R_{MUC\_1}$ </td><td> $T_1$ </td><td>80,20</td><td>1.0</td></tr><tr><td>MUC</td><td> $R_{MUC\_1}$ </td><td> $T_2$ </td><td>60,10</td><td>1.0</td></tr><tr><td>MAD</td><td> $R_{MAD\_1}$ </td><td> $T_1$ </td><td>80,15</td><td>1.0</td></tr><tr><td>MAD</td><td> $R_{MAD\_1}$ </td><td> $T_2$ </td><td>80,15</td><td>1.0</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_1$ </td><td>60,10</td><td>1.0</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_2$ </td><td>40,5</td><td>1.0</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_1$ </td><td>70,10</td><td>1.0</td></tr></table>

Table 4 shows the availability of the airports' maintenance stations in terms of person-power. For instance, the station $\mathrm { R } _ { \mathrm { F R A } }$ <sub>\_1</sub> appears to be having 2 technicians available from 10:00 to 16:00 and from 21:00 to 10:00 next day.

## 2.3. Alternatives generation

In the case that the number of alternatives is large, and an exhaustive search may not be performed, the alternatives' generation mechanism takes advantage of the approach proposed in [4] and [5]. Two adjustable parameters, namely the maximum number of alternatives (MNA) and the sampling rate (SR) are used by the alternatives' generation mechanism for guiding the search through the solution space. MNA controls the number of alternatives formed and thus, the breadth of the search. The SR determines the accuracy of the consequences estimation procedure. These parameters allow the search to be tuned to the requirements of the problem and they may in<sup>fl</sup>uence the quality of the solution as well as the computational effort for making a decision.

<table><tr><td>Date</td><td>GMT/flight</td><td>From-to</td><td>Duration (min) mean, deviation</td><td>Departure delay (min) mean, deviation</td></tr><tr><td>1/11/09</td><td>0600-0645/FL100</td><td>FRA-CDG</td><td>45,5</td><td>10,3</td></tr><tr><td>1/11/09</td><td>0830-0950/FL101</td><td>CDG-MUC</td><td>80,10</td><td>20,5</td></tr><tr><td>1/11/09</td><td>1200-1400/FL102</td><td>MUC-MAD</td><td>120,10</td><td>30,10</td></tr><tr><td>1/11/09</td><td>1600-1800/FL103</td><td>MAD-FRA</td><td>120,10</td><td>20,5</td></tr></table>

Available person-power per airport station and period.

<table><tr><td>Airport</td><td>Resource ID</td><td>P1</td><td>P2</td><td>P3</td><td>P4</td><td>P5</td><td>P6</td></tr><tr><td rowspan="2">FRA</td><td rowspan="2"> $R_{FRA\_1}$ </td><td>00:00-05:00</td><td>-07:30</td><td>-10:00</td><td>-16:00</td><td>-21:00</td><td>-10:00n</td></tr><tr><td>1.0</td><td>0.0</td><td>1.0</td><td>2.0</td><td>1.0</td><td>2.0</td></tr><tr><td rowspan="2">FRA</td><td rowspan="2"> $R_{FRA\_2}$ </td><td>00:00-06:00</td><td>-10:00</td><td>-16:00</td><td>-22:00</td><td>-10:00n</td><td></td></tr><tr><td>1.0</td><td>2.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td></td></tr><tr><td rowspan="2">CDG</td><td rowspan="2"> $R_{CDG\_1}$ </td><td>00:00-06:00</td><td>-11:00</td><td>-14:00</td><td>-22:00</td><td>-10:00n</td><td></td></tr><tr><td>0.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td></td></tr><tr><td rowspan="2">MUC</td><td rowspan="2"> $R_{MUC\_1}$ </td><td>00:00-06:00</td><td>-11:00</td><td>-15:00</td><td>-22:00</td><td>-10:00n</td><td></td></tr><tr><td>0.0</td><td>2.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td></td></tr><tr><td rowspan="2">MAD</td><td rowspan="2"> $R_{MAD\_1}$ </td><td>00:00-06:00</td><td>-15:00</td><td>-18:00</td><td>-21:00</td><td>-10:00n</td><td></td></tr><tr><td>1.0</td><td>2.0</td><td>1.0</td><td>2.0</td><td>0.0</td><td></td></tr></table>

Table 5  
Cost criterion data.

<table><tr><td rowspan="2">Airport</td><td rowspan="2">Resource ID</td><td rowspan="2">Task</td><td colspan="3">Cost rates (€/min)</td><td rowspan="2">Parts cost of T1 (€)</td><td rowspan="2">Parts cost of T2 (€)</td></tr><tr><td>Equipment rate</td><td>Labour rate</td><td>Overhead rate</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_1$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_2$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_1$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_2$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr><tr><td>CDG</td><td> $R_{CDG\_1}$ </td><td> $T_1$ </td><td>10</td><td>10</td><td>5</td><td>300</td><td>200</td></tr><tr><td>CDG</td><td> $R_{CDG\_1}$ </td><td> $T_2$ </td><td>10</td><td>10</td><td>5</td><td>300</td><td>200</td></tr><tr><td>MUC</td><td> $R_{MUC\_1}$ </td><td> $T_1$ </td><td>5</td><td>5</td><td>5</td><td>300</td><td>200</td></tr><tr><td>MUC</td><td> $R_{MUC\_1}$ </td><td> $T_2$ </td><td>5</td><td>5</td><td>5</td><td>300</td><td>200</td></tr><tr><td>MAD</td><td> $R_{MAD\_1}$ </td><td> $T_1$ </td><td>10</td><td>10</td><td>5</td><td>300</td><td>200</td></tr><tr><td>MAD</td><td> $R_{MAD\_1}$ </td><td> $T_2$ </td><td>10</td><td>10</td><td>5</td><td>300</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_1$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_1}$ </td><td> $T_2$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_1$ </td><td>5</td><td></td><td>5</td><td>200</td><td>200</td></tr><tr><td>FRA</td><td> $R_{FRA\_2}$ </td><td> $T_2$ </td><td>5</td><td>5</td><td>5</td><td>200</td><td>200</td></tr></table>

The total number of alternatives for the example is given by Eq. (1) and is equal to 49.

## 2.3.1. Cost criterion

In Table 5, the cost data are provided for the calculation of the cost of each alternative, using Eq. (6). Indicative cost rates are considered.

## 2.3.2. RUL criterion

Fig. 3 depicts the RUL for the 7 alternatives out of a total 49, where both tasks are dispatched in the same airport station.

The present case examines a loose due date policy at 75% of the probability of failure regarding the remaining useful life of the parts. Table 6 shows the nominal RUL values, based on the respective due date policy, while Table 7 shows the weight factor per task: the component of T1 is more important, in terms of RUL, than the respective component of T2.

Table 6  
RUL criterion nominal values calculation.

<table><tr><td>Airport</td><td>Due date of part of T1 (75%)</td><td>RUL (min)</td><td>Due date of part of T2 (75%)</td><td>RUL (min)</td></tr><tr><td>FRA</td><td>13:00</td><td>185</td><td>09:00</td><td>75</td></tr><tr><td>CDG</td><td>13:00</td><td>140</td><td>09:00</td><td>30</td></tr><tr><td>MUC</td><td>13:00</td><td>60</td><td>09:00</td><td>-50</td></tr><tr><td>MAD</td><td>13:00</td><td>-60</td><td>09:00</td><td>-170</td></tr><tr><td>FRA</td><td>13:00</td><td>-180</td><td>09:00</td><td>-290</td></tr></table>

Table 7  
Criteria weights.

<table><tr><td>Cost</td><td>RUL</td><td>Operational risk</td><td>Flight delay</td></tr><tr><td rowspan="3">30%</td><td>40%</td><td rowspan="3">20%</td><td rowspan="3">10%</td></tr><tr><td>wr $_{1}$ =70%</td></tr><tr><td>wr $_{2}$ =30%</td></tr></table>

## 2.3.3. Operational risk criterion

The values of the operational risk criterion, calculated using Eqs. (10) and (11), are considered as follows:

$D V ( T _ { y } , R _ { i j } )$ is assumed to be the cost of the respective scheduled event as calculated for the cost criterion

$D P ( T _ { y } , R _ { i j } )$ is assumed to be equal to $1 0 0 \% - U n D P ( T _ { y } , R _ { i j } )$

$U n D V ( T _ { y } , R _ { i j } )$ is the cost related to an unscheduled event (hire last moment personnel, any extra costs, etc.) and is assumed in this case that it is in principle twice as much as the respective scheduled event cost

$U n D P ( T _ { y } , R _ { i j } )$ is the probability of failure during arrival time (Fig. 3).

## 2.3.4. Flight delay criterion

Flight delays may be caused when the maintenance tasks are carried out in stations whose availability is low. Delays taking place in one leg of the route may be propagated to the next legs of the route as well, leading to large – overall – departure and arrival delays.

![](/api/attachments/C9AJTZSZ/fulltext/images/5a6fe00fef101c54d4b2e9452e8a61f394fecac3557a676b55a981f7feee092c.jpg)  
Fig. 3. Operator's due date policy for a maintenance action.

Table 8 Best alternatives.

<table><tr><td>Alternative rank</td><td>Assignment, leg</td><td>Maintenance task</td><td>Resource/airport</td><td>Utility (%)</td></tr><tr><td rowspan="2">1</td><td> $T_1R_{MUC\_1}$ , 3</td><td>T1</td><td>Base/MUC</td><td>89.26</td></tr><tr><td> $T_2R_{FRA\_1}$ , 1</td><td>T2</td><td>Hangar/FRA</td><td></td></tr><tr><td rowspan="2">2</td><td> $T_1R_{MUC\_1}$ , 3</td><td>T1</td><td>Base/MUC</td><td>83.50</td></tr><tr><td> $T_2R_{FRA\_2}$ , 1</td><td>T2</td><td>Base/FRA</td><td></td></tr><tr><td rowspan="2">3</td><td> $T_1R_{MUC\_1}$ , 3</td><td>T1</td><td>Base/MUC</td><td>82.81</td></tr><tr><td> $T_1R_{MUC\_1}$ , 3</td><td>T2</td><td>Base/MUC</td><td></td></tr></table>

## 2.3.5. Criteria weights

The criteria weights are shown in Table 7. Different sets of criteria weights could re<sup>fl</sup>ect the different operator's maintenance policies.

## 2.4. Results

An experiment is conducted in order to test and validate the approach. In the speci<sup>fi</sup>c example presented in this paper, the solution space is exhaustively searched, since the overall number of possible alternatives is rather low. A sampling rate (SR) equal to 10 was used, meaning that every alternative has been simulated 10 times, using different values for the <sup>fl</sup>ight duration, maintenance duration and departure delay, following the characteristics of the statistical distribution representing these variables (Tables 2 and 3). The best three alternatives yielding the highest utility are presented in Tables 8 and 9.

All three alternatives make sense. For the best ranked alternative, in particular, it should be noted that although $\mathrm { R } _ { \mathrm { F R A } _ { - } 1 }$ and $\mathsf { R } _ { \mathrm { F R A } \_ 2 }$ seem to be the less expensive options for both tasks, the availability of $\mathsf { R } _ { \mathrm { F R A } _ { - } 1 }$ at the beginning of the route is limited and in case it was selected for carrying out T1, the remaining useful life would still be high. $\mathrm { R _ { M U C _ { - } } }$ <sub>1</sub> seems to be a good alternative for T1, since the RUL obtained is just above its due time, while the operational risk is still low, compared to what it would be if $\mathrm { R } _ { \mathrm { F R A \_ } } .$ was selected in the last leg of the route.

## 3. Discussion

Examining the different criteria used, the cost criterion is related to the operator's costs and is used for representing the scheduled event costs. The operational risk criterion is used for modelling the unscheduled event consequences. As a component approaches the end of its life during a maintenance alternative, the utility of the alternative, due to the operational risk criterion, decreases in principle, since the possibility to have an unscheduled event is high. The flight delay depends strongly on the availability of the resources at each airport. The RUL criterion introduces the use of the component's useful life that helps the operator determine the components' due date policies. The weight factors per task employed may be used for re<sup>fl</sup>ecting the relative importance of different components in terms of RUL.

Today's decision support process is reactive in principle and mostly focuses on resolving unscheduled maintenance activities (troubleshooting). This research work aims at reducing unscheduled maintenance events and probably any inevitable consequences (e.g., <sup>fl</sup>ight delay and high maintenance cost) by providing an operational maintenance planning decision making framework, where short-term maintenance decisions are analyzed in terms of the selected criteria. The framework is highly bene<sup>fi</sup>cial for components whose condition is continuously monitored. In order to accommodate the different policies followed by operators and maintenance engineers, an innovative aspect introduced by the proposed research is the development of a framework that introduces criteria weights, thus allowing for the modelling of the speci<sup>fi</sup>c operator's maintenance policy. The decision matrix facilitates the overall process of evaluating maintenance alternatives, leading to the selection of the best alternative (the one with the best utility). The deployment of the proposed framework requires an installation phase, during which different scenarios and <sup>fl</sup>ight plans have to be executed in order for the criteria weights per component to be analyzed and <sup>fi</sup>ne-tuned. The resource availability at the airports' stations as well as the time aspects are all introduced in detail. The sampling mechanism employed is of high importance, since it can detect how uncertainty and delays may propagate to the remaining legs of an aircraft's route.

Table 9  
Best alternatives criteria performance.

<table><tr><td>Alternative rank</td><td>Cost [€]</td><td>RUL [min]</td><td>OR [€]</td><td>Flight delay [min]</td></tr><tr><td>1</td><td>2260.0</td><td>62.6</td><td>2968.2</td><td>150.3</td></tr><tr><td>2</td><td>2589.0</td><td>65.8</td><td>3322.2</td><td>160.8</td></tr><tr><td>3</td><td>2639.1</td><td>57.2</td><td>4110.0</td><td>151.2</td></tr></table>

The major point of the approach proposed is that based on the health assessment information (RUL) and on additional information related to operational (<sup>fl</sup>ight delay) and economical variables (cost, operational risk) at the operator's level, the performance of the maintenance planning activities at Line Maintenance can be improved. The proposed approach has been evaluated in the context of the Research Project TATEM [29], where the proposed planning framework has been tested against a number of use cases for different aircraft health monitored components and operational scenarios.

## Acknowledgments

The work presented in this paper is partially supported by the Integrated Project “Technologies and techniques for new maintenance concepts — TATEM” [29], which is funded by the European Commission.

The authors would also like to specially thank Dr. Matthias Buderath from EADS Germany for his support in carrying out this work.

## References

[1] AIRBUS AIRMAN™, AIRBUS, available online from: http://www.content.airbusworld.com/SITES/Customer services/html/acrobat/brochure airman.pdf [accessed 5 May 2008]

[2] Boeing Airplane Health Management, Boeing, available online from: http://www. boeing.com/commercial/ams/mss/brochures/airplane\_health.html [accessed 5 May 2008].

[3] G. Chryssolouris, Manufacturing Systems: Theory and Practice, 2nd EditionNew York, Springer-Verlag, 2005

[4] G. Chryssolouris, K. Dicke, M. Lee, On the resources allocation problem, International Journal of Production Research 30 (12) (1992) 2773–2795.

[5] G. Chryssolouris, J. Pierce, K. Dicke, A decision-making approach to the operation of <sup>fl</sup>exible manufacturing systems, International Journal of Flexible Manufacturing Systems 4 (3–4) (1992) 309–330.

[6] G. Chryssolouris, M. Lee, K. Dicke, An approach to short interval scheduling for discrete parts manufacturing, International Journal of Computer Integrated Manufacturing 4 (3) (1991) 157–168.

[7] G. Chryssolouris, J. Pierce, K. Dicke, An approach for allocating manufacturing resources to production tasks, Journal of Manufacturing Systems 10 (5) (1991) 368–382.

[8] M. Clarke, B. Smith, Impact of operations research on the evolution of the airline industry, Journal of Aircraft 41 (1) (2004) 62–72.

[9] M. Clarke, D. Ryan, Airline industry operations research, Encyclopedia of Operations Research and Management Science, Kluwer Academic Publishers, 2001.

[10] L.W. Clarke, E.L. Johnson, G.L. Nemhauser, Z. Zhu, The aircraft rotation problem, Annals of Operations Research 69 (1997) 33–46.

[11] M. Dijkstra, L. Kroon, J. van Nunen, M. Salomon, A DSS for capacity planning of aircraft maintenance personnel, International Journal of Production Economics 23 (1-3) (1991) 69-78

[12] W. El Moudani, F. Mora-Camino, A dynamic approach for aircraft assignment and maintenance scheduling by airlines, Journal of Air Transport Management 6 (4) (2000) 233–237.

[13] R. Gopalan, K. Talluri, Mathematical models in airline schedule planning: a survey, Annals of Operations Research 76 (1998) 155–185

[14] ICAO, ATMCP-WG/C/2-WP/003, ICAO, (2004) available online from: http://www. icao.int/ [accessed 5 May 2008].

[15] IEEE-SA Std. 1451 and Std. 1232, IEEE-SA, available online from: http://standards. jeee,org/regauth/1451/index,html [accessed 5 May 2008]

[16] ISO 13373-1:2002, ISO 13373-2:2005, ISO 13374-2:2007, ISO, available online from: http://www.iso.org/[accessed 5 May 2008]

[17] T. Jiejuan, M. Dingyuan, X. Dazhi, A genetic algorithm solution for a nuclear power plant risk–cost maintenance model, Nuclear Engineering and Design 229 (1) (2004) 81–89.

[18] F. Lin, H. Kuo, S. Lin, The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems Decision Support Systems 45 (2008) 795–810.

[19] M. Marseguerra, E. Zio, Optimizing maintenance and repair policies via a combination of genetic algorithms and Monte Carlo simulation, Reliability Engineering and System Safety 68 (1) (2000) 69–83.

[20] E.R. Mueller, G.B. Chatterji, Analysis of Aircraft Arrival and Departure Delay Characteristics, AIAA's Aircraft Technology, Integration, and Operations Technical, Los Angeles, 2002.

[21] Mxi Maintenix®, Mxi Technologies Ltd, available online from: http://www.mxi. com/template.php?unique=205 [accessed 5 May 2008].

[22] OSA-CBM V3.1L, MIMOSA, available online from: http://www.mimosa.org/, [accessed 5 Mav 2008].

[23] G. Quana, G. Greenwoodb, D. Liuc, S. Huc, Searching for multiobjective preventive maintenance schedules: combining preferences with evolutionary algorithms, European Journal of Operational Research 177 (3) (2007) 1969–1984

[24] A. Sarac, R. Batta, C. Rump, A branch-and-price approach for operational aircraft maintenance routing, European Journal of Operational Research 175 (3) (2006) 1850–1869.

[25] H. Sherali, E. Bish, X. Zhu, Airline <sup>fl</sup>eet assignment concepts, models, and algorithms, European Journal of Operational Research 172 (1) (2006) 1–30.

[26] C. Sriram, A. Haghani, An optimization model for aircraft maintenance scheduling and re-assignment, Transportation Research. Part A, Policy and Practice 37 (1) (2003) 29–48.

[27] Y. Suzuki, A decision support system for dynamic vehicle refuelling, Decision Support Systems 46 (2009) 522–531.

[28] A. Tam, W. Chan, J. Price, Maintenance scheduling to support the operation of manufacturing and production assets, The International Journal of Advanced Manufacturing Technology 34 (3–4) (2006) 399–405.

[29] TATEM — Technologies and Techniques for New Maintenance Concepts (FP6 EU Integrated Project; EC contract no. AIP3-CT-2004-502909), available online from: http://www.tatemproject.com [accessed 5 May 2008]

[30] S. Yan, Ta-Hui Yang, Hsuan-Hung Chena, Airline short-term maintenance manpower supply planning, Transportation Research. Part A, Policy and Practic 38 (9–10) (2004) 615–642.

Nikolaos Papakostas is a Project Manager at the Laboratory for Manufacturing Systems and Automation and has been involved in a signi<sup>fi</sup>cant number of R&D projects, related to Manufacturing, Industrial Planning, Control, Supply Chain Management and involving IT development. He has more than 50 publications in international scienti<sup>fi</sup>c journals and refereed conferences. He has worked as IT Manager in large industrial companies and as Project Manager in SAP R/3 implementation projects. He received a Ph.D. in Engineering (2000) and a Diploma (M.S.) in Mechanical Engineering (1995).

Polyzois Papachatzakis is a Project Manager at the Laboratory for Manufacturing Systems and Automation and has been involved in a signi<sup>fi</sup>cant number of R&D projects, related to Production Management, Maintenance, Planning and Control, and Supply Chain Management. He has worked as Project Manager in software and industrial consulting companies. He received an MSc in Computer Integrated Manufacturing (1995) and a Diploma (M.S.) in Mechanical Engineering (1993). He is currently working on a Ph.D. in the area of new maintenance concepts and methodologies.

Vagelis Xanthakis is a Research Engineer at the Laboratory for Manufacturing Systems and Automation and has been involved in a signi<sup>fi</sup>cant number of R&D projects, related to Manufacturing, Maintenance, Planning and Control, and Supply Chain Management and involving IT development. He received a Diploma (M.S.) in Electrical Engineering (2005). He is currently working on a Ph.D. in the area of enterprise-wide collaborative production management, planning and control.

Dimitris Mourtzis (M.S. in Mechanical Engineering and Ph.D. in Engineering), is Lecturer at Department of Mechanical Engineering and Aeronautics, University of Patras, Greece. He is an Associate Member of the International Academy for Production Research (CIRP) since 2005 and member of the International Federation of Automatic Control (IFAC) – TC 5.2 – Manufacturing Modelling for Management and Control. His main <sup>fi</sup>eld of research is Design and Production Planning and Control of Manufacturing Systems. He has more than 60 publications in international scienti<sup>fi</sup>c journals and refereed conferences.

George Chryssolouris is the Director of the Laboratory for Manufacturing Systems and Automation (LMS) at the Department of Mechanical Engineering and Aeronautics at the University of Patras. He has more than 350 publications in international scienti<sup>fi</sup>c journals and refereed conferences and is the author of two books published by Springer Verlag. He was the recipient of SME's Frederick W. Taylor Research Medal (2001) and he was elected President of the, Paris based, International Academy for Production Engineering (CIRP) in 2006–07. He received a Ph.D. (Dr.-Ing.) in Engineering from the University of Hannover, Germany (1979) and a Diploma (M.S.) in Mechanical/Electrica Engineering from the National Technical University of Athens, Greece (1975).
