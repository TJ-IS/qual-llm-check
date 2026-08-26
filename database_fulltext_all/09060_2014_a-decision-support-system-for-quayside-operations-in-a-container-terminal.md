---
otero_id: 9060
otero_key: "HQ4NDTNA"
title: "A decision support system for quayside operations in a container terminal"
authors: "Evrim Ursavas"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for quayside operations in a container terminal

Evrim Ursavas

Department of Operations, Faculty of Economics and Business, University of Groningen, The Netherlands

## a r t i c l e i n f o

Article history: Received 23 April 2013 Received in revised form 21 December 2013 Accepted 8 January 2014 Available online 18 January 2014

Keywords: Quayside operations Berth allocation Crane scheduling Container terminal operations

## a b s t r a c t

This paper proposes a decision support system for optimizing operations on the quayside of a container terminal. Due to the existence of multiple parties involved in the decision making processes within port operations, it is essential to pay attention to each parties' concerns and demands which by nature are frequently con<sup>fl</sup>icting with each other. This calls for a DSS that offers the <sup>fl</sup>exibility of adjusting the balance within con<sup>fl</sup>icting objectives, guiding the decision maker towards the <sup>fi</sup>nal decision. Consequently, this study provides a DSS that determines the berthing and crane allocations simultaneously. To show the practical application of the DSS presented, a real life case study at a container terminal has been conducted. Implementation of the model shows that improvements ranging from 10% to 25% on service time and costs can be attained.

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

The prolonged economic recession together with weak economic growth is leading container terminals to follow a cautious approach when serving their customers. Before the economic crisis, where more optimistic <sup>fi</sup>gures were prospected, concentrating on satisfying these customers to the highest level has been the more focused approach to gain share in the market. Nowadays, the necessity for considering cost issues while providing quality service to the customers has increased.

The decisions for operations within the terminal depend on the balance of in<sup>fl</sup>uence between terminal operators and shipping companies. From the terminal operator's perspective operating for high productivity and container throughput at low costs is a critical element to stay competitive. However, from the shipping companies' perspective low turnaround time and reliability regarding adherence to promised handling times are more critical elements. Hence, there are different views existing between the parties involved at the container terminals [24,29]. With shipping companies on one side and terminal operators on the other, each having its own concerns and demands and which by nature are frequently con-<sup>fl</sup>icting with each other, the decision makers call for supporting instruments that help them to attain a balance among those differing intentions. Yet, recent literature on quayside operations within a container terminal does not provide adequate support to resolve the issue via practical considerations. Subsequently, this study attempts to provide a decision support tool that determines the berthing and crane allocations simultaneously under multiple objectives.

At a container terminal, vessels are docked on a berth where containers are loaded/unloaded by cranes at the quayside. These containers are then transferred to a storage area called yard. The focus of this study is at the quayside operations. The <sup>fi</sup>rst concern is the allocation of berths to the arriving vessels. Berth allocation (BAP) drives the port management process and the major objective for this process is to determine the optimal location and optimal berthing time for the vessels. The next problem, quay crane allocation (CAP) and crane scheduling (CSP) determine the assignment sequence of quay cranes to a container ship in ful<sup>fi</sup>lling pre-speci<sup>fi</sup>ed objectives and satisfying various constraints. Without a doubt, outputs for these three decisions have enormous impact on port performance measures such as waiting times, service times and operating costs. The turnaround time of ships in ports, involving waiting times and service times, is a direct common concern to the shipping companies, whereas, on the supply side, operations should not be managed without recognizing the fact that the bottom line for terminal operations is cost. One of the two components of this cost linked with terminal assets such as quay length, cranes and land is <sup>fi</sup>xed and can rarely be controlled within short run. Labor hours, on the other hand, may be seen as the key variable in the near-term. It should also be noted that, labor cost is rather important especially in Europe and the U.S., where man power is scarce and expensive. Managing operations so as to conserve this scarce resource is axiomatic where the share of port labor varies between 50 and 75% of total terminal operating costs [25]. It can be observed that different operating conditions in time can lead to different cost outcomes. For instance, most terminals will run a second shift as necessary to turn the vessel, but this comes with a cost. These late evening or second shifts are expensive and third or night shifts are still more expensive. It is then advisable for port operators to concentrate on costs controlled by minimizing labor, particularly on the second and third shifts.

In light of the above considerations, this study proposes a novel approach for the three problems, BAP, CAP and CSP, through a methodology based on multiple objectives. It should be noted that by the newly formulated integer linear programming formulation, optimal berthing times, berth allocations to vessels, berthing positions, crane assignments, crane schedules and their identities are calculated simultaneously, which puts the integration forward in this study, within the deepest ones in the literature. The literature on quayside operations is extended by better representing the real world implementation through embracing further facts linked with crane speci<sup>fi</sup>cations. Quay cranes are usually of two types: rail-mounted quay cranes (RMQCs) and rubber-tired quay cranes (RTQCs). These two differ in terms of their crane-crossing restrictions and container handling rates. Another point that should be considered for the RMQCs is the crane reach distance restrictions that stem from the fact these cranes moving along the rail have physical restrictions due to their connecting devices such as cables. Further, container terminals may follow dynamic crane assignment policy where crane assignments may vary during the service time of vessel. That is, instead of assuming <sup>fi</sup>xed handling time of the vessels, this study suggests an optimizing method that considers the handling time as a function of crane allocations in each time segment. Handling the practical realizations, a new bi-objective integer problem is proposed using a constraint handling method to obtain the non-dominated berth–crane assignments and schedules as Pareto optimal front via an interactive approach. Through the use of the decision support system the decision maker has the prospect to evaluate different planning solutions that simultaneously consider the shipping companies' and the terminal op erators' interests with differing in<sup>fl</sup>uences. For each different setting of balance between terminal operators and shipping companies, the decision maker will obtain different costs and service time outputs. The user is able to control the density of the alternative solutions and evaluate the trade-offs among them. So, the developed DSS employs an architec ture to facilitate the generation and comparison of user intervened solutions. The DSS will also detect solutions where for instance, the same service time can be attained with lower costs. This is done through the designed cutting plane algorithm within the DSS where dominated solutions are eliminated and ef<sup>fi</sup>cient solutions are presented. The decision maker will choose among these ef<sup>fi</sup>cient solutions according to the present preferences or necessities. By offering the decision maker the <sup>fl</sup>exibility of adjusting the balance within con<sup>fl</sup>icting objectives, the port may continue to attract customers and also retain a recessionproof working environment.

The next section provides the related literature. In Section 3, the details of the model developed for the aforementioned problem are provided. Section 4 puts forward the decision support system. Section 5 reports the computational experiments via a case study. In the last section, the concluding remarks are presented.

## 2. Related work

Operations within a container terminal can be grouped into three main parts as quayside, yardside and transfer tasks within the terminal [32]. On the quayside, berth allocation (BAP), crane allocation (CAP) and crane scheduling problems (CSP) deal with the optimal assignment of berths and cranes together with optimal berthing and service times. The need for effective decision making strategies for managing these container terminal operations has become apparent and therefore has attracted many researchers into the subject [29,30]. Consequently, in the past, decision support systems that deal with the operations and planning of containers have been developed by researchers in the <sup>fi</sup>eld. [1,22,23,28]. Bandeira et al. [1] proposed a decision support system that integrates the <sup>fl</sup>ow of full containers with the <sup>fl</sup>ow of empty containers. They have modeled the problem as a multiple-depot vehicle scheduling problem. The problem is tackled in two interconnected stages where <sup>fi</sup>rst allocation and movement of containers are determined without considering transportation times and then unfolding this static solution in a time schedule. Murty et al. [22] developed a decision support system where a variety of interrelated daily decisions at a container terminal is analyzed. The aim of these decisions is to minimize the berthing time of vessels, the resources needed for handling the workload, the waiting time of customer trucks, and the congestion on the roads and at the storage blocks and docks inside the terminal as well as to make the best use of the storage space. Ngai et al. [23] discussed the development of a prototype system in a container depot with the use of radio frequency identi<sup>fi</sup>cation (RFID) features. The decision support system enables tracking of the locations of stackers and containers improving the visibility of operations data and control processes together with the support of mobile commerce activities. Shen and Khoong [28] proposed a decision support system using network optimization to model empty container repositioning. The system works on a rolling horizon approach where two algorithms are suggested to minimize the impact of changes in the demand and supply of empty containers on decisions taken in previous periods.

In the main, treatment of berth and cranes in isolation from each other leads to suboptimal results. Our focus in this review path will be on the studies on quayside operations that simultaneously tackle those problems. A detailed recent survey work provided by Bierwirth and Meisel [2] presents a state-of-art research on the topic. It may be seen that the level of integration for those problems may vary within studies. Mainly, integration of the CAP with either BAP or CSP models is commonly observed. The integration of the three problems together may be seen as the deepest level of integration. With the integration of BAP and CAP, the identities of speci<sup>fi</sup>c cranes that are assigned to vessels are not determined but the number of crane assignments is. Works by Meisel and Bierwirth [19–21], Giallombardo et al. [7], Hendriks et al. [11], Liang et al. [14], Bierwirth and Meisel [2], Han et al. [10], and Blazewicz et al. [3] may generally be considered within this category. These papers present the optimization models to decide on the berthing time, the berthing position, and the number of cranes for each vessel. In practice, the speci<sup>fi</sup>c cranes used for the service of vessels need to be determined additionally.

On a deeper integration level, Park and Kim [26] worked on BAP, CAP and CSP problems with a two-phase solution procedure. The <sup>fi</sup>rst phase determines the berthing position and time of each vessel as well as the number of cranes assigned to each vessel at each time segment. Quay crane scheduling is then constructed in the second phase based on the solution found from the <sup>fi</sup>rst phase. Following, study by Imai et al. [13] also considers BAP, CAP and CSP in the same manner, where the integration among the problem is weaker compared to a uni<sup>fi</sup>ed model. Functional integration among the stated problems is also adapted by Meier and Schumann [17] and Meisel [18]. Zhang et al. [31] use the sub-gradient optimization technique to solve the problem of BAP, CAP and CSP together. Related with this study, the newly formed model presented in this paper deals with the three problems in a uni<sup>fi</sup>ed modeling approach and extends the literature by considering different crane handling rates and crane movement restrictions.

The study presented in this work furthermore adapts a multiobjective approach. Accordingly, relevant recent works may be summarized as follows: for the BAP problem, a bi-objective approach that considers the minimization of delay of ships' departure and minimization of the total service time is implemented by Imai et al. [12]. To form the non-inferior solution set, they follow the weighting method where all objectives are combined into a single one by assigning weights and by changing the weights in a systematic fashion. Golias et al. [8] differentiate the service level given to customers with different priorities using the multi-objective approach via an evolutionary algorithm. Later, again for the BAP problem, they propose a non-numerical ranking preference method [9]. Cheong et al. [4] model the berth allocation problem tackling three objectives: makespan, waiting time, and degree of deviation from a predetermined priority schedule. Multi-objective evolutionary algorithm is used to <sup>fi</sup>nd the Pareto ef-<sup>fi</sup>cient frontier. Studies discussed above do not deal with the crane allocation or the crane scheduling problem. It should also be remarked that the solution set provided by the above works is not guaranteed to be optimal.

Crane scheduling problem is later incorporated by the study of Cheong et al. [5]. Multi-objective evolutionary algorithm approach is followed to solve the two objectives of waiting time and handling time of ships. Most related work to the study in this paper is by Liang et al. [15]. In their bi-objective crane and berth allocation model, they aim to minimize the sum of the handling time of containers and the number of crane movements concurrently. They propose a hybrid genetic algorithm to form the Pareto frontier. They realize their computational experiments by a real world case study of Shanghai container terminal.

This study works on the berth allocation, crane allocation and crane scheduling problems concurrently, while considering two objectives of total service time minimization and labor cost minimization. The former works in the literature are leaded in the perspective of real world representation. With the formulated mathematical model, cranes with different speci<sup>fi</sup>cations may be considered in compliant with their characteristics. Those cranes may differ in terms of their technical speci<sup>fi</sup>cations regarding their container handling rates or their movement restrictions. Hence, mimicking the real world decisions, particular cranes may be favored to another in convenient cases. The approach put forward is capable of solving real life instances of weekly schedules. To solve the bi-objective integer problem an iterative algorithm incorporating the branch and cut solution embedded in an interactive constraint handling scheme is developed. The constraint handling method developed is based on the ε-constraint idea where instead of combining the objectives with weights, only one of the original objectives is minimized while the others are rearranged as constraints [6].

The next section is dedicated to explaining the details of the mathematical model embedded in the developed decision support system.

## 3. Model description

This research offers a newly formulated model that combines the BAP, CAP and CSP problems. The combined problem can be represented in a three-dimensional space shown in Fig. 1. The rectangles symbolize the vessels whose dimensions are vessel-length including the safety margin, assigned cranes and handling time. The problem is the positioning of the vessels in the decision space without overlapping with each other while minimizing the total service time of the ships and minimizing the labor cost.

In the spatial dimension, the <sup>fi</sup>gure shows three berths (Q1, Q2, Q3) with different lengths. Vessels are allowed to overlap either in time or in quay dimensions but not both, such as vessel i (v ) and vessel j (v ), which are berthed at the same location but at different time periods. In the crane axis, we have seven cranes that are either RMQC or RTQC.

![](/api/attachments/HQ4NDTNA/fulltext/images/0e424638a63645ba6744958c49d69d3d7e334d368090b2159af9a859acac1cba.jpg)  
Fig. 1. Berth–crane–time space

The bi-objective optimization model will now be presented. The assumptions of the model are as follows:

## Assumptions

(1) There are discrete berths with speci<sup>fi</sup>ed lengths. A vessel may be assigned to any of them in a position compliant to the vessel length.

(2) There are different types of cranes. RMQCs can move along the dedicated quay line obeying crane crossing con<sup>fl</sup>icts and crane reach limitations, RTQCs are also capable of moving between quays.

RMQCs can move along the quay where it is located obeying crane crossing limitations and crane reach distances, whereas the RTQCs are furthermore capable of moving between berths. These different types of cranes serve with different handling rates. As opposed to studies that do not approach the three BAP, CAP and CSP problems in a uni<sup>fi</sup>ed manner, handling time and number of cranes to be assigned to the ship are not known in advance. Handling time depends on the number of cranes allocated to a vessel which is dynamic throughout the service time. For instance, a vessel can start to be served by only one crane and end up being served by three cranes. Therefore, the ships do not have to wait until a speci<sup>fi</sup>ed number of cranes are available. This prevents suboptimal solutions resulting from misleading crane unavailability assumption. In Fig. 1, during the periods 4 to 6, vessel k $( \nu _ { k } )$ is served by crane number 5 and at time period 6, by the addition of crane 7, number of cranes assigned to the ship is increased to two. The total handling time for $\boldsymbol { v _ { k } }$ is $f _ { k } - b _ { k } = 5$

(3) Different crane handling rates may be re<sup>fl</sup>ected in the model.

(4) Crane allocation is dynamic throughout the handling period of a vessel. The number and type of cranes assigned are <sup>fl</sup>exible and vessel handling time is dependent on crane allocations.

(5) A vessel can be assigned to a limited number of cranes at each time period.

(6) There is a due time associated with each vessel.

The indices, parameters, decision variables and the integer linear programming model are de<sup>fi</sup>ned below:

Notation:

<table><tr><td colspan="2">Indices:</td></tr><tr><td>i=(1,...,I)</td><td>set of vessels</td></tr><tr><td>j=(1,...,J)</td><td>set of RMQC and RTQC</td></tr><tr><td>p=(1,...,p)</td><td>set of RMQC</td></tr><tr><td>j*=(p+1,...,J)</td><td>set of RTQCs, where last J-p cranes are assumed to be portable</td></tr><tr><td>k=(1,...,K)</td><td>set of berths</td></tr><tr><td>t=(1,...,T)</td><td>time periods</td></tr><tr><td>s=(1,...,S)</td><td>shifts</td></tr></table>

Input parameters: $l _ { i }$ vessel length including the safety margin for the vessel $Q _ { k }$ length of berth k $a _ { i }$ arrival time of vessel i $N _ { i 0 }$ number of containers initially on the vesse $U _ { i }$ maximum number of cranes that can be assigned to a vessel simultaneously. $C { \dot { C } } { \dot { } }$ set of berths not covered by crane j $M$ large constant $m$ constant $0 \leq m \leq 1$ $R _ { j }$ container handling rate of jth crane $b _ { s }$ beginning time period of shift s $f _ { s }$ ending time period of shift s $c _ { s }$ cost factor of shift s $d _ { i }$ cutoff date of vessel i (if applicable)

Decision variables:

$P H _ { i t }$ 1 if vessel i has remaining containers at time t

$$
Y H _ {i t}
$$

1 if vessel i is served at time t

Auxiliary variables:

$y _ { i j t k }$ 1 if crane j is allocated to vessel i at time t at berth k

$B V _ { i t k }$ 1 if vessel i assigned to berth k at time t

$N _ { i t }$ total number of containers to be handled for vessel i at time t $\Delta _ { i k }$ 1 if vessel i is assigned to berth k

$T e m p H _ { i t }$ an auxiliary variable formulating the link between $y _ { i j t k }$ and $Y H _ { i t }$

The model:

$$
f _ {1} (l a b o r): \min \sum_ {s} \sum_ {i} \sum_ {t = b _ {s}} ^ {t = f _ {s}} (t - a _ {i}) \cdot c _ {s} \cdot Y H _ {i t}
$$

$$
f _ {2} (t i m e): \min \sum_ {i} \sum_ {t = a _ {i}} P H _ {i t}
$$

$$
l _ {i} \cdot \Delta_ {i k} \leq Q _ {k} \quad \forall i, k\tag{1}
$$

$$
\sum_ {k} \Delta_ {i k} = 1 \quad \forall i\tag{2}
$$

$$
\sum_ {i} \sum_ {k} y _ {i j t k} \leq 1 \quad \forall j, t\tag{3}
$$

$$
\sum_ {j} \sum_ {k} y _ {i j t k} \leq U _ {i} \cdot P H _ {i t} \quad \forall i, t\tag{4}
$$

$$
\sum_ {i} B V _ {i t k} \leq 1 \quad \forall t, k\tag{5}
$$

$$
\sum_ {j} y _ {i j t k} \leq U \cdot B V _ {i t k} \quad \forall i, t, k\tag{6}
$$

$$
B V _ {i t k} \leq \Delta_ {i k} \quad \forall i, t, k\tag{7}
$$

$$
N _ {i t + 1} \leq M \cdot P H _ {i t} \quad \forall i, t, t \neq T\tag{8}
$$

$$
N _ {i t} - \sum_ {j} \sum_ {k} R _ {j} \cdot y _ {i j t k} = N _ {i, t + 1} \quad \forall i, t, t \neq T\tag{9}
$$

$$
\sum_ {j} \sum_ {t = a _ {i}} y _ {i j t k} \geq m \cdot \Delta_ {i k} \quad \forall i, k\tag{10}
$$

$$
\sum_ {j} \sum_ {t = a _ {i}} \sum_ {k ^ {\prime} \neq k} y _ {i j t k ^ {\prime}} \leq M \cdot (1 - \Delta_ {i k}) \quad \forall i, k\tag{11}
$$

$$
\sum_ {j} \sum_ {t = a _ {i}} y _ {i j t k} \leq M \cdot \Delta_ {i k} \quad \forall i, k\tag{12}
$$

$$
\sum_ {j} \sum_ {t = a _ {i}} \sum_ {k ^ {\prime} \neq k} y _ {i j t k ^ {\prime}} \geq m \cdot (1 - \Delta_ {i k}) \quad \forall i, k\tag{13}
$$

$$
\sum_ {i} \sum_ {j ^ {\prime} \geq j + 1} \sum_ {k ^ {\prime} \leq k - 1} y _ {i j ^ {\prime} t k ^ {\prime}} \leq M \cdot \left(1 - \sum_ {i} y _ {i j t k}\right) \quad \forall j \leq p, t, k\tag{14}
$$

$$
Y H _ {i t} \leq T e m p H _ {i t} \quad \forall i, t\tag{15}
$$

$$
\sum_ {j} \sum_ {k} y _ {i j t k} \geq m \cdot T e m p H _ {i t} \quad \forall i, t\tag{16}
$$

$$
\sum_ {j} \sum_ {k} y _ {i j t k} \leq M \cdot T e m p H _ {i t} \quad \forall i, t\tag{17}
$$

$$
Y H _ {i t} \geq m \cdot T e m p H _ {i t} \quad \forall i, t\tag{18}
$$

$$
N _ {i, T} \leq 0 \quad \forall i\tag{19}
$$

$$
\sum_ {t \succ d _ {i}} y _ {i j t k} = 0 \quad \forall i, j, k\tag{20}
$$

$$
\sum_ {j} \sum_ {k \in C C (j)} y _ {i j t k} = 0 \quad \forall i, t\tag{21}
$$

$$
y _ {i j t k}, \Delta_ {i k}, P H _ {i t}, Y H _ {i t}, T e m p H _ {i t}, B V _ {i, t, k} \in \{0, 1 \} \quad \forall i, j, t, k\tag{22}
$$

$$
N _ {i t} \text {   urs.   } \forall i, t.\tag{23}
$$

The <sup>fi</sup>rst objective $f _ { 1 }$ minimizes the labor cost. The cost for labor is proportional to the cost factor of the shift the vessel is handled in and the duration time the vessel is moored at the berth. The second objective $f _ { 2 }$ minimizes the service time of a vessel. This service includes the waiting time for the vessel to be serviced and the handling time while being serviced by quay cranes.

Constraint set (1) assures that the allocation of a vessel does not exceed the quay length Constraint set (2) ensures that all arriving vessels are giving service. Constraint set (3) does not allow any crane to be allocated to more than one vessel. Constraint set (4) guarantees that the total number of cranes allocated in a time period cannot go above the maximum number of cranes that can be allocated to a vessel. By constraint set (5), no more than one vessel is allowed to moor at a berth at a time period. Constraint set (6) guarantees that the value of $B V _ { i t k }$ at the considered berth–vessel pair is set to 1 if a vessel is given service at the dock at a given time. By constraint set $( 7 ) , B V _ { i t k }$ is linked with $\Delta _ { i k } .$ By constraint set (8), a vessel's $P H _ { i t }$ value is set to 1, if the vessel has arrived and there are remaining containers to be handled. In constraint set (9) the number of containers to be handled in each vessel is decreased by its crane handling rate at each period. Constraint sets (10) through (13) assure that a vessel is docked at a single berth and the vessel is not allowed to change berths during service. Constraint set (14) handles the crane passing constraints for static cranes. If a crane j is serving a vessel at berth $k ,$ then no other crane with a larger crane id can serve a vessel at a berth that is positioned to its right. This constraint is set only for RMQCs since RTQCs are not restricted by berthing positions. Constraints set (15) to (18) formulate the equations for solving the total handling time of each vessel. If a $y _ { i j t k }$ assignment exists for a vessel at a given time, the vessel handling time variable, $Y H _ { i t } ,$ , is set to 1. Constraints set (19) guarantee the handling of all the containers on a vessel. By constraint set (20) the service time of a vessel is aimed to <sup>fi</sup>nish before the strict due date agreed by both parties. Constraint set (21) prevents the assignment of cranes to berths where crane reach is not possible.

The developed mathematical model is embedded into the decision support system. The details of the DSS and the solution algorithm are explained in the following section.

## 4. The decision support system

The developed DSS employs an architecture to facilitate the generation and comparison of user intervened solutions. The software is designed to run in a PC environment under Microsoft Windows. The main components of the DSS contain the user interface for input parameters, user re-evaluation and report visualization, the database management system for storing the data related with the terminal such as vessels, berth structures and cranes and the core of the DSS where the model is solved in compliance with the solution algorithm. Microsoft Access is used as the database. Gurobi solver is used for solving the optimization model. The procedures and the interaction with the optimization algorithm are developed by VBA. With regard to the requirements of the decision makers, the <sup>fl</sup>exibility of the DSS has been seen as an important value. Consequently, the structure is formed to allow for a high degree of user interaction. The solution methodology followed for solving the bi-objective problem is an interactive method that uses an iterative algorithm consisting of branch and cut solutions embedded in a constraint handling scheme based on an improved epsilon-constraint method.

Fig. 2 illustrates the interactive solution algorithm. The algorithm starts with the generation of the payoff table where two different ways of developing the table are proposed to the decision maker: traditional and lexicographic.

In the traditional payoff table formation the optimal value of each objective is determined separately and the value of the other function is recorded accordingly. The second alternative, lexicographic optimization may be used in cases where one objective has a clear priority ordering compared to the other objective. In that case, while <sup>fi</sup>nding the optimal value of the objective with lower priority, the optimal value of the higher priority objective is added into the formulation, allowing the optimal value for the objective to be retained persistently [16].

With the constraint handling method, one of the original objectives is minimized while the others are transformed into constraints. For bi-objective model, values $B _ { 1 }$ and $B _ { 2 }$ shown in Fig. 2 give the range for the objective criteria. The choice of the criteria that will be selected to be treated as constraint depends on the problem. The next step is to divide the range into intervals that will be used to determine the RHS value of the objective function left as a constraint. The frequency of the intervals will determine the number of solutions presented to the decision maker. The mathematical model presented in the previous section will be solved to attain these solutions.

To eliminate the dominated solutions and present ef<sup>fi</sup>cient solutions to the decision maker, a cutting plane approach is designed. That is, to search for alternative optimal outcomes to $f _ { 1 }$ and present the best of those with respect to $f _ { 2 } ,$ a sub-problem that minimizes $f _ { 2 }$ is formed by imposing the value of the created solution as a bound to the integer model. The sub-problem becomes:

![](/api/attachments/HQ4NDTNA/fulltext/images/53436a50482d4952176a35330c304fcf1ec90a04247304d89175ac99d1220fc3.jpg)  
Fig. 2. Flowchart diagram of the solution algorithm.

$$
\begin{array}{l} \min f _ {2} (t i m e) \\ s t \\ f _ {1} (l a b o u r) \leq Z _ {f _ {1}} ^ {e} \\ \dots \end{array}\tag{24}
$$

where $Z _ { f _ { 1 } } ^ { e }$ is the value of f , at iteration e, in the master problem. In cases where a value less than the former value to $f _ { 2 }$ is detected, the related solution is presented to the decision maker as the ef<sup>fi</sup>cient solution.

Later, the decision maker will choose among these solutions according to the present preferences or necessities. Subsequently, the new solution set will be formed from the search space around the selected solution by incorporating the selected solution's objective value as bounds to the objective function. This upper bound is computed as:

$$
U B _ {f _ {1}} ^ {e + 1} = z _ {f _ {1}} ^ {e} + \lambda \left(z _ {f _ {1}} ^ {e} - z _ {f _ {1}} ^ {\min}\right)\tag{25}
$$

where $U B _ { f _ { 1 } } ^ { e + 1 }$ is the upper bound of the next iteration $\boldsymbol { \mathcal { Z } } _ { f _ { 1 } } ^ { e }$ is the objective function value of the preferred solution and $z _ { f _ { 1 } } ^ { \operatorname* { m i n } }$ is the minimum value of the objective function $f _ { 1 } .$ Here λ parameter may be chosen as a value between 0 and 1 depending on the desired tightening of the search space. This iterative solution methodology will continue until the decision maker is satis<sup>fi</sup>ed with the result.

In summary, the DSS will start by offering the payoff table to the user. Next, the user will determine the density of the solutions each considering a different level of balance between cost and time objectives. The mathematical model presented in the previous section will be solved to acquire these solutions. The user will carry on by picking solutions according to the present preferences and consequences with regard to the con<sup>fl</sup>icting objectives of the parties involved. The DSS will continue generating solutions intensi<sup>fi</sup>ed around the region that closer re<sup>fl</sup>ect these preferences until the user is satis<sup>fi</sup>ed with the results. In the next section, the use and operation of the DSS will be elucidated by examples.

## 5. Case study

A real life case study has been conducted showing the practical use of the solution methodology presented. The aim of the case study is to clearly demonstrate the features and capabilities of the DSS and clarify the potential use of it by the container terminals.

The container terminal analyzed is at the Port of Izmir in Turkey with a container handling capacity of approximately 1 million TEUs (Fig. 3).

![](/api/attachments/HQ4NDTNA/fulltext/images/616e3df5bd4b08d6a4ac04f2118a6ba8fb67dfeadb93442afb0740e51e526b27.jpg)  
Fig. 3. Port of Izmir.

Based on the data taken from the terminal, the application is simulated and the model proposed is used to optimize the simultaneous assignment of berths and cranes to the incoming container vessels. Table 1a and Table 1b illustrate the weekly data taken from the port in November, 2011. Table 1a gives vessel related information and Table 1b puts forward the information related to berths and cranes. Crane reach capabilities are shown in Table 1b. For instance, RMQC number 1 cannot reach beyond berth 4.

The terminal operates with weekly Expected Time of Arrivals (ETA) provided by the lines and constructs a berthing schedule. The time segment is set as 1 h. This is compliant with the practice where arrivals and departures are commonly taken as integral [31]. If not, they can be rounded down or up to the nearest integer value. In practice, arrival times are rounded down and departures are rounded up. There are three shifts within 24 h. Day shift is between 07:00 and 15:00, evening shift is between 15:00 and 24:00 and night shift is between 00:00 and 7:00. Operating expenses at evening shift are higher than day shift and night shift is the most costly shift. Proportional cost data for each shift is 1, 3.1, 4.8 units for day, evening and night shifts respectively. It should be noted that it is possible for the handling of a vessel to span several shifts.

An issue that is seen in real life implementations is that according to the vessel demands and the terminal circumstances due-dates may be agreed upon by contracts. This due-date is treated as a cut-off date for the shipping companies and terminal operators. The shipping companies still prefer service that is provided earlier than this strict deadline. It is the decision makers aim to provide service that is given before this boundary. The decision support tool is designed with the <sup>fl</sup>exibility to incorporate such restrictions. If such a deadline exists, this time limit is entered into the model. The model, when run, will then aim to give solutions in which the service is provided within the shortest time period which should be tried to be kept earlier than this due-date. If there is no such deadline, the tool will again aim for solutions with fast service times. This is particularly important for high priority vessels where they may be guaranteed berthing within 2 h of arrival. In general, the terminal af<sup>fi</sup>rms the service to be completed within 24 h after arrival. This feature is also a service guarantee level that the terminals are trying to accomplish to be competent. It should be noted that it is still possible for vessels to have a service time longer than 24 h of arrival. These issues that are faced in practice can be handled through the use of the proposed decision support tool. The due dates for the proposed case are shown in Table 1a.

The berth structure is discrete, and the whole quay area, which is 1330 m in length, is partitioned into 7 berths. These berths differ in lengths; hence the vessels are required to obey these physical restrictions. The last two berths are smaller in size and vessels MRS1, MAR1, VDB2 and MAR2 cannot be docked in those berths. There are <sup>fi</sup>ve RMQCs and two RTQCs, with handling rates equal to 50 TEUs/h and 40 TEUs/h, respectively. It should be pointed out that the model allows for different crane rates for each separate crane, that is, cases where RMQCs or RTQCs with different speci<sup>fi</sup>cations may also be re<sup>fl</sup>ected. For this instance, maximum allowable number of cranes assigned to the vessels is 4. In other instances this may vary from vessel to vessel.

The implemented model has 289,255 constraints and 217,723 variables of which 214,020 of them are discrete. The execution time for each instance is reported to have less than 1 CPU s. However the observed real time is between 30 s (for corner points) and 3 h (for points lying in the center of the Pareto frontier). These run times have been found reasonable by the decision makers in the port to form weekly schedules.

According to the solution algorithm presented in Fig. 2, the decision maker will <sup>fi</sup>rst choose between the two alternatives for forming the payoff table. Here, we make our experiments with the conventional payoff table formation. For the problem presented in this paper, f (labor) is nominated as objective function and f (time) as constraint. As seen in the payoff tables shown for iterations, in Fig. 4, the range for the objective function and for f is 600 and 705 units and f is 78 and 99 time periods. The range of f is divided into intervals. The number of points may be determined interactively. As more points are demanded the computational time for generating the optimal solutions will be increased. It should also be noted that the number of solutions generated in each iteration need not be constant. The decision maker may start with fewer solutions that cover the whole Pareto front quickly and then increase the frequency if more detailed information is required in the subsequent iterations. The solutions are then presented to the user. Fig. 4 shows a sample schedule of berths and cranes presented to the user for a solution. The vessels shown with rectangles are differentiated by their colors and the relevant key is given beside the schedule. Numbers within rectangles show the speci<sup>fi</sup>c cranes assigned at the corresponding time period.

Table 1a  
Input for the case study (vessels).

<table><tr><td>Ship id</td><td>Ship name</td><td>Arrival time (ai)</td><td>Vessel length (li)</td><td>Due time (di)</td><td>Total number of loading/unloading container in TEU (Ni0)</td></tr><tr><td>1</td><td>MSC1</td><td>November 7th 06:15</td><td>169</td><td>31</td><td>330</td></tr><tr><td>2</td><td>NPT</td><td>November 7th 17:00</td><td>182</td><td>42</td><td>873</td></tr><tr><td>3</td><td>MRS1</td><td>November 8th 00:30</td><td>203</td><td>49</td><td>358</td></tr><tr><td>4</td><td>HMS1</td><td>November 8th 00:00</td><td>184</td><td>49</td><td>517</td></tr><tr><td>5</td><td>WW1</td><td>November 8th 01:50</td><td>117</td><td>50</td><td>122</td></tr><tr><td>6</td><td>KPE1</td><td>November 8th 02:25</td><td>155</td><td>51</td><td>621</td></tr><tr><td>7</td><td>VDB1</td><td>November 8th 08:50</td><td>211</td><td>57</td><td>210</td></tr><tr><td>8</td><td>ORK1</td><td>November 8th 17:30</td><td>174</td><td>66</td><td>1336</td></tr><tr><td>9</td><td>WND1</td><td>November 8th 18:30</td><td>173</td><td>67</td><td>380</td></tr><tr><td>10</td><td>LYQ1</td><td>November 8th 21:50</td><td>168</td><td>70</td><td>349</td></tr><tr><td>11</td><td>MAR1</td><td>November 9th 02:00</td><td>217</td><td>74</td><td>885</td></tr><tr><td>12</td><td>MSC2</td><td>November 9th 03:15</td><td>178</td><td>76</td><td>214</td></tr><tr><td>13</td><td>MRS2</td><td>November 9th 16:30</td><td>169</td><td>89</td><td>668</td></tr><tr><td>14</td><td>HMS2</td><td>November 10th 00:40</td><td>160</td><td>97</td><td>236</td></tr><tr><td>15</td><td>WW2</td><td>November 10th 18:45</td><td>188</td><td>115</td><td>1310</td></tr><tr><td>16</td><td>KPE2</td><td>November 11th 05:30</td><td>183</td><td>126</td><td>573</td></tr><tr><td>17</td><td>VDB2</td><td>November 11th 10:20</td><td>222</td><td>131</td><td>615</td></tr><tr><td>18</td><td>ORK2</td><td>November 11th 15:35</td><td>149</td><td>136</td><td>401</td></tr><tr><td>19</td><td>WND2</td><td>November 12th 09:45</td><td>156</td><td>155</td><td>608</td></tr><tr><td>20</td><td>LYQ2</td><td>November 12th 10:15</td><td>188</td><td>156</td><td>130</td></tr><tr><td>21</td><td>MAR2</td><td>November 13th 07:15</td><td>242</td><td>176</td><td>1830</td></tr></table>

The decision maker then selects the preferred solution among the presented ones. Fig. 5 shows the progress of the solution algorithm in each iteration. In case solution D is selected the required upper bound is inserted into the model. The new upper bound to the objective function is computed as 666 by the use of Eq. (25) (λ parameter is chosen as 0.4). The new payoff table will be formed and then the algorithm will continue following similar principles with the next iterations by increasing the density of the solutions around the preferred region. The algorithm will be terminated when the user is satis-<sup>fi</sup>ed with the results.

More data from July 25th, 2011 to November 7th, 2011 is used to test the performance of the algorithm. On average, 375 separate runs of the model are observed to assess the algorithm. The results given in Table 2 show the running time range considering each solution in the Pareto.

Fig. 6 demonstrates the relation between the number of vessels and the relevant average running times. The number of vessels served within a week changes between 17 and 24 and the running times are between 7004 and 10,450 s (worst time). Generally, increased number of vessels will lead to higher running times of the algorithm. This may be observed in weeks September 26th and October 17th, where 24 vessels are served and running times are relatively higher. Also, the arrival sequence of the vessels and the number of containers on vessels are other important factors that affect the performance of the algorithm. For instance, the reason of longer running times in weeks October 24th and October 31th is due to the fact that arrival schedule of the vessels highly overlaps with each other. A more balanced spread of the vessel arrival schedule on the weekly time period leads to faster running times. In the main, the running times are highly related with the parameters and the demonstrated computational times are found to be reasonable and acceptable for practical use by the terminal operators of the port.

Table 1b  
Input for the case study (berths and cranes).

<table><tr><td></td><td></td><td>Berth id</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td></td><td></td><td>Berth length in m (Q $_q$ )</td><td>230</td><td>220</td><td>220</td><td>210</td><td>150</td><td>150</td><td>150</td></tr><tr><td>Crane type</td><td>Crane id</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RMQC</td><td>C1</td><td rowspan="7">Crane reach (berths covered by cranes)</td><td colspan="4"></td><td></td><td></td><td></td></tr><tr><td>RMQC</td><td>C2</td><td colspan="4"></td><td></td><td></td><td></td></tr><tr><td>RMQC</td><td>C3</td><td colspan="4"></td><td></td><td></td><td></td></tr><tr><td>RMQC</td><td>C4</td><td colspan="4"></td><td></td><td></td><td></td></tr><tr><td>RMQC</td><td>C5</td><td colspan="4"></td><td></td><td></td><td></td></tr><tr><td>RTQC</td><td>C6</td><td colspan="4"></td><td></td><td></td><td></td></tr><tr><td>RTQC</td><td>C7</td><td colspan="4"></td><td></td><td></td><td></td></tr></table>

It is also important to consider the decision support system's use in larger ports. In ports, where large amount of containers are handled annually, the DSS is designed to be implemented separately for each terminal. As an example, within the Port of Rotterdam, the largest port in Europe, 12 main container terminals are available [27]. The ECT Delta Container Terminal, one of the biggest terminals within the port, with a capacity of approximately 4.5 million TEUs, is again divided into four terminals: the APM Terminal, Delta Dedicated East Terminal, Delta Dedicated West Terminal and the Delta Barge Feeder Terminal. The model should be applied individually for each of those parts by carefully adjusting the parameters.

Main characteristics observed in such terminals are that commonly the number of vessels, number of containers within a vessel (due to larger vessels being served) and also number of cranes within the terminal show variations. When the number of containers on a vessel is high, more crane work is required. In terminals with suf<sup>fi</sup>cient capabilities, for large vessels, number of cranes working simultaneously can be increased considerably, such as up to 12. This would reasonably shorten the service time of the vessels. These features should be adjusted carefully in the DSS for use in every terminal. With those facts, to have a general insight and to further test the performance and the scalability of the DSS, additional experiments based on the vessel arrival workload and terminal characteristics of typical large container terminals are performed. The number of vessels served on a weekly basis is increased up to the level of 34. For instance, for the Uniport Container Terminal within the Port of Rotterdam in the Netherlands, the number of vessels to be served weekly is on average 32.09 ranging from 28 to 34 by considering weekly data between July 1 and December 8, 2013. For the next experiments, vessel arrival schedule of week September 23rd, 2013 realized at Uniport Container Terminal is used for testing purposes. The arrival schedule is shown in Fig. 7. The rectangles represent the vessels arriving at the speci<sup>fi</sup>ed dates and times.

![](/api/attachments/HQ4NDTNA/fulltext/images/4face9324f89ea1c563ae7c3d9af6f1b8bdf9e60721c61b531e8a55781e1da3b.jpg)

<table><tr><td></td><td colspan="2">Berths</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Timeline</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="10"></td><td>00:00</td><td>73</td><td></td><td>37</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>01:00</td><td>74</td><td></td><td>1236</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>02:00</td><td>75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>03:00</td><td>76</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>04:00</td><td>77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>05:00</td><td>78</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>06:00</td><td>79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>07:00</td><td>80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>08:00</td><td>81</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>09:00</td><td>82</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="23">November 10th</td><td>10:00</td><td>83</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11:00</td><td>84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12:00</td><td>85</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13:00</td><td>86</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14:00</td><td>87</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15:00</td><td>88</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16:00</td><td>89</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17:00</td><td>90</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18:00</td><td>91</td><td></td><td></td><td></td><td>1245</td><td></td><td></td><td></td></tr><tr><td>19:00</td><td>92</td><td></td><td></td><td></td><td>156</td><td></td><td></td><td></td></tr><tr><td>20:00</td><td>93</td><td></td><td></td><td></td><td>1245</td><td></td><td></td><td></td></tr><tr><td>21:00</td><td>94</td><td></td><td></td><td></td><td>2457</td><td></td><td></td><td></td></tr><tr><td>22:00</td><td>95</td><td></td><td></td><td></td><td>1345</td><td></td><td></td><td></td></tr><tr><td>23:00</td><td>96</td><td></td><td></td><td></td><td>1345</td><td></td><td></td><td></td></tr><tr><td>00:00</td><td>97</td><td></td><td></td><td></td><td>1245</td><td></td><td></td><td></td></tr><tr><td>01:00</td><td>98</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>02:00</td><td>99</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>03:00</td><td>100</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>04:00</td><td>101</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>05:00</td><td>102</td><td></td><td></td><td></td><td></td><td>2567</td><td></td><td></td></tr><tr><td>06:00</td><td>103</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>07:00</td><td>104</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>08:00</td><td>105</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="25">November 11th</td><td>09:00</td><td>106</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10:00</td><td>107</td><td></td><td></td><td></td><td>1237</td><td></td><td></td><td></td></tr><tr><td>11:00</td><td>108</td><td></td><td></td><td></td><td>1235</td><td></td><td></td><td></td></tr><tr><td>12:00</td><td>109</td><td></td><td></td><td></td><td>1235</td><td></td><td></td><td></td></tr><tr><td>13:00</td><td>110</td><td></td><td></td><td></td><td>67</td><td></td><td></td><td></td></tr><tr><td>14:00</td><td>111</td><td></td><td></td><td></td><td>2567</td><td></td><td></td><td></td></tr><tr><td>15:00</td><td>112</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4567</td></tr><tr><td>16:00</td><td>113</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4567</td></tr><tr><td>17:00</td><td>114</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4567</td></tr><tr><td>18:00</td><td>115</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19:00</td><td>116</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20:00</td><td>117</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21:00</td><td>118</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22:00</td><td>119</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>23:00</td><td>120</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>00:00</td><td>121</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>01:00</td><td>122</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>02:00</td><td>123</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>03:00</td><td>124</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>04:00</td><td>125</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>05:00</td><td>126</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>06:00</td><td>127</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>07:00</td><td>128</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>08:00</td><td>129</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>09:00</td><td>130</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4567</td></tr><tr><td rowspan="22">November 12th</td><td>10:00</td><td>131</td><td></td><td></td><td></td><td>1234</td><td></td><td></td><td></td></tr><tr><td>11:00</td><td>132</td><td></td><td></td><td></td><td>2345</td><td></td><td></td><td></td></tr><tr><td>12:00</td><td>133</td><td></td><td></td><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td>13:00</td><td>134</td><td></td><td></td><td></td><td>1267</td><td></td><td></td><td></td></tr><tr><td>14:00</td><td>135</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15:00</td><td>136</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16:00</td><td>137</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17:00</td><td>138</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18:00</td><td>139</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19:00</td><td>140</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20:00</td><td>141</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21:00</td><td>142</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22:00</td><td>143</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>23:00</td><td>144</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>00:00</td><td>145</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>01:00</td><td>146</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>02:00</td><td>147</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>03:00</td><td>148</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>04:00</td><td>149</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>05:00</td><td>150</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>06:00</td><td>151</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>07:00</td><td>152</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td rowspan="16">November 13th</td><td>08:00</td><td>153</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>09:00</td><td>154</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>10:00</td><td>155</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>11:00</td><td>156</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>12:00</td><td>157</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>13:00</td><td>158</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>14:00</td><td>159</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>15:00</td><td>160</td><td></td><td></td><td></td><td></td><td>2345</td><td></td><td></td></tr><tr><td>16:00</td><td>161</td><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td></tr><tr><td>17:00</td><td>162</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18:00</td><td>163</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19:00</td><td>164</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20:00</td><td>165</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21:00</td><td>166</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22:00</td><td>167</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>23:00</td><td>168</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 4. Berth and crane schedules.

<table><tr><td rowspan="4">Iteration 1</td><td rowspan="4">Labour cost</td><td>iteration=1 f1 f2</td></tr><tr><td>min f1 78 705</td></tr><tr><td>min f2 99 600</td></tr><tr><td>Point D with service time=87 and labour cost=636 is selected.</td></tr><tr><td rowspan="4">Iteration 2</td><td rowspan="4">Labour cost</td><td>iteration=2 f1 f2</td></tr><tr><td>min f1 82 666</td></tr><tr><td>min f2 99 600</td></tr><tr><td>Point D with service time=91 and labour cost=618 is selected.</td></tr><tr><td rowspan="4">Iteration 3</td><td rowspan="4">Labour cost</td><td>iteration=3 f1 f2</td></tr><tr><td>min f1 84 652</td></tr><tr><td>min f2 99 600</td></tr><tr><td>Point E with service time=92 and labour cost=614 is selectedThe decision maker is satisfied with the solution, hence the algorithm terminates.</td></tr></table>

Fig. 5. Solution methodology progress

The scenarios are designed to re<sup>fl</sup>ect the performance in terminals with different crane capacities. For example, the APM Terminal within the Port of Rotterdam in the Netherlands holds 14 cranes and the Uniport Container Terminal works with 9 cranes. Respectively, different scenarios are prepared using 9 and 14 cranes. It is also vital to see the performance under different workloads of container volumes. Hence, settings with different container volumes are arranged. Average annual container volumes of 1,800,000, 2,400,000 and 3,000,000 TEUs are investigated separately. Consequently, settings with similar arrival schedules are examined with different crane capacities and container volumes to further assess the model behavior in large terminals.

The details of the experiments and the results are presented in Table 3.

Setting A tests a weekly workload of 34.500 containers with 9 cranes. Scenario B tests the same workload with 14 cranes. Experiments C and D test 46,000 containers with 9 and 14 cranes, respectively. Settings E and F, test 57,700 containers with 9 and 14 cranes. For these settings, the number of constraints ranges between 501,976 and 571,884 and the number of variables ranges between 464,547 and 518,272. Among those, between 458,556 and 511,601 are discrete variables. The execution times are reported to be between 1486 and 2853 CPU s. However, the observed real time is between 55 s and 5 h. As analyzed previously through the case study data of the container terminal in the Port of Izmir and shown in Fig. 6, with the increased number of vessels higher running times were expected. With the added number of vessels in these additional experiments running times are increased accordingly up to 5 h. On the other hand, increased number of cranes within the terminal allows for less workload for each crane. Also the possibility of having more cranes working simultaneously leads to the improvement of the results. As can be seen in Table 3, the number of cranes has an important effect on the service time and the labor cost. For instance, by comparing the results of Settings A and B we can see that the service time has been decreased to 121 from 127 by the availability of 5 additional cranes within the terminal. In general, as the average number of containers handled increases, the service time and the labor costs increase accordingly. This can be noticed in settings where the service times and labor costs are higher compared to their lower volume setting pairs. Overall, as expected, the computational results indicate that the behavior of the system is highly affected by all the parameters and the results show variability with the complexity of the system. Approximately, the DSS requires between 10 and 18.000 s to run depending on the scenario being solved. Given the complexity of the problem and its intended use for forming of<sup>fl</sup>ine weekly plans these times can be considered acceptable.

Table 2  
Extended experimental results for the Port of Izmir.

<table><tr><td>Week</td><td>Number of vessels</td><td>Total number of containers</td><td>Worst time (s)</td><td>Best time (s)</td></tr><tr><td>July 25th</td><td>19</td><td>11.350</td><td>8.750</td><td>26</td></tr><tr><td>August 8th</td><td>20</td><td>12.350</td><td>8.956</td><td>21</td></tr><tr><td>August 15th</td><td>18</td><td>10.055</td><td>7.589</td><td>24</td></tr><tr><td>August 22th</td><td>17</td><td>10.370</td><td>7.265</td><td>20</td></tr><tr><td>August 29th</td><td>19</td><td>11.050</td><td>8.450</td><td>26</td></tr><tr><td>August 29th</td><td>18</td><td>11.325</td><td>7.004</td><td>15</td></tr><tr><td>September 5th</td><td>17</td><td>9.994</td><td>6.984</td><td>10</td></tr><tr><td>September 12th</td><td>20</td><td>10.784</td><td>7.156</td><td>15</td></tr><tr><td>September 19th</td><td>21</td><td>10.952</td><td>8.500</td><td>17</td></tr><tr><td>September 26th</td><td>24</td><td>13.789</td><td>10.450</td><td>60</td></tr><tr><td>October 3rd</td><td>23</td><td>12.127</td><td>9.231</td><td>30</td></tr><tr><td>October 10th</td><td>23</td><td>11.863</td><td>8.805</td><td>32</td></tr><tr><td>October 17th</td><td>24</td><td>12.589</td><td>10.122</td><td>55</td></tr><tr><td>October 24th</td><td>22</td><td>11.965</td><td>9.923</td><td>38</td></tr><tr><td>October 31th</td><td>20</td><td>11.879</td><td>9.765</td><td>32</td></tr></table>

To evaluate whether the model results would improve the current situation of the port or not, the results of the model are compared with the actual data of the Port of Izmir. It has been stated by the port managers that cost data related with labor is highly variable and subject to changes according to the season, availability of workers, national holidays and strikes. So, when comparing model results with the real data this data was adjusted carefully for each case. For the period between July 25th and November 15th, weekly improvements ranged from 10% to 25% on service time and cost. It should be noted that, the extent of improvements is dependent on the decision maker's choices and preferences while executing the solution algorithm. In cases where the user opts for solutions where cost is assessed with higher signi<sup>fi</sup>cance, the improvement between the actual and simulated outputs for the cost side tends to be higher. On the other hand, when service time is prioritized the model results tend to be more superior to the actual outputs in terms of the shipping companies' perspective.

As an example, for the week November 7, the actual departure dates which are the date and time the vessel leaves the port are given in Table 4. Here, the time used for the actual handling operations is important to evaluate the model's performance. Delays or interruptions due to unforeseen occasions such as temporary low ef<sup>fi</sup>ciency of operators, health issues and internal terminal traf<sup>fi</sup>c congestion during the handling operations should be extracted as much as possible. Related times are shown under the column heading “time on handling”. The next column shows the number of hours passed the due dates, computed by subtracting the departure dates from the agreed due dates. According to this data, there were 4 vessels (ORK1, VDB2, ORK2 and MAR2) that had exceeded its due date time with 5, 6, 1 and 3 h respectively. Delays not directly related with the terminal operations, such as for vessels NPT and WW2, are excluded from these records. These delays are due to customs, security, inspections, weather conditions, clearance or late arrival of export containers. As explained previously, during the use of the DSS, it would be the decision maker's choice to determine the level of balance between service time and labor costs. For this case, avoiding delays could be seen of utmost importance. Accordingly a solution that could prevent delays is preferred. With those features, the DSS results shown in Table 4 give a solution with reduced delays. Vessels ORK1, VDB2, ORK2 and MAR2 can be serviced within their due dates. For vessels NPT and WW2 where interruptions due to external factors are known, the handling time could be reduced by 2 h for each vessel. The detailed schedule is shown in Fig. 4. A four hour delay could cost a shipping company as much as \$50,000, an amount which would consequently be passed on to the importers and exporters. This economic impact further underlines the importance of using effective decision support tools for container terminals.

## 6. Concluding remarks

Current economic situation has led container terminals to re-evaluate their decision making strategies. Steps to reduce operating costs have seemingly become more important. With labor costs having a major in-<sup>fl</sup>uence on the total expenses, this study proposes an interactive decision support tool for decision makers to help make the balance between customer service quality and cost considerations concentrating on labor expenses. The problem focused is the simultaneous berth allocation and crane scheduling problem in consideration of two objectives that needs to be satis<sup>fi</sup>ed.

![](/api/attachments/HQ4NDTNA/fulltext/images/d148b9b362ada30ab4c9e672a41a68ba9bb95314caaeafc2791c946f271f4d33.jpg)  
Fig. 6. Number of vessels and running times.

Table 3  
![](/api/attachments/HQ4NDTNA/fulltext/images/203aca745d549a1a51690f2f5c58123799f899ffcbde1ed53c8babe1f1f7687c.jpg)  
Fig. 7. Arrival schedule for additional experiments.

Extended experimental results for different settings.

<table><tr><td>Setting</td><td>Number of cranes</td><td>Annual TEU volume</td><td>Service time</td><td>Labor cost</td><td>CPU time (s)</td></tr><tr><td>A</td><td>9</td><td>1,800,000</td><td>127</td><td>959</td><td>2233</td></tr><tr><td>B</td><td>14</td><td>1,800,000</td><td>121</td><td>841</td><td>1486</td></tr><tr><td>C</td><td>9</td><td>2,400,000</td><td>144</td><td>1146</td><td>1493</td></tr><tr><td>D</td><td>14</td><td>2,400,000</td><td>124</td><td>823</td><td>2581</td></tr><tr><td>E</td><td>9</td><td>3,000,000</td><td>228</td><td>1980</td><td>2180</td></tr><tr><td>F</td><td>14</td><td>3,000,000</td><td>157</td><td>1357</td><td>2853</td></tr></table>

The literature is extended by better re<sup>fl</sup>ecting practical considerations and a new bi-objective integer programming model has been formulated. The three quayside decision problems, berth allocation, crane allocation and crane scheduling that have huge in<sup>fl</sup>uence on port performance measures such as waiting times, service times and operating costs are tackled concurrently to limit suboptimal solutions. Embracing further facts linked with crane speci<sup>fi</sup>cations adds to the body of knowledge making the model more convenient for real-world use. Cranes with different technical speci<sup>fi</sup>cations with regard to their container handling rates, crane reach or their movement restrictions can be re<sup>fl</sup>ected within the solution. This feature also makes the model convenient for use in different types of berth layouts such as indented berth structure that is used for fast-handling of mega-container ships. Further, dynamic crane assignment policy where crane assignments may differ during the handling of the vessel is implemented within the model proposing an optimizing method that considers the handling time as a function of crane allocations in each time segment. With this solution technique, a vessel may start to be served as soon as minimum acceptable number of cranes is present, avoiding solutions that lead them to wait until a speci<sup>fi</sup>ed number of cranes are available. This prevents suboptimal solutions resulting from misleading crane unavailability assumption.

Table 4  
Actual data and model data evaluation.

<table><tr><td>Ship id</td><td>Ship name</td><td>Arrival time (ai)</td><td>Departure time</td><td>Time on handling (actual)</td><td>Passed due date (actual)</td><td>Time on handling (DSS)</td></tr><tr><td>1</td><td>MSC1</td><td>November 7th 06:15</td><td>November 7th 23:15</td><td>2</td><td>0</td><td>2</td></tr><tr><td>2</td><td>NPT</td><td>November 7th 17:00</td><td>November 9th 00:30</td><td>7</td><td>7</td><td>5</td></tr><tr><td>3</td><td>MRS1</td><td>November 8th 00:30</td><td>November 8th 16:15</td><td>3</td><td>0</td><td>2</td></tr><tr><td>4</td><td>HMS1</td><td>November 8th 00:00</td><td>November 8th 15:15</td><td>4</td><td>0</td><td>4</td></tr><tr><td>5</td><td>WW1</td><td>November 8th 01:50</td><td>November 8th 11:55</td><td>1</td><td>0</td><td>1</td></tr><tr><td>6</td><td>KPE1</td><td>November 8th 02:25</td><td>November 9th 00:15</td><td>5</td><td>0</td><td>4</td></tr><tr><td>7</td><td>VDB1</td><td>November 8th 08:50</td><td>November 8th 21:00</td><td>3</td><td>0</td><td>2</td></tr><tr><td>8</td><td>ORK1</td><td>November 8th 17:30</td><td>November 9th 22:15</td><td>12</td><td>5</td><td>7</td></tr><tr><td>9</td><td>WND1</td><td>November 8th 18:30</td><td>November 9th 15:10</td><td>4</td><td>0</td><td>3</td></tr><tr><td>10</td><td>LYQ1</td><td>November 8th 21:50</td><td>November 9th 08:20</td><td>4</td><td>0</td><td>3</td></tr><tr><td>11</td><td>MAR1</td><td>November 9th 02:00</td><td>November 9th 22:45</td><td>8</td><td>0</td><td>8</td></tr><tr><td>12</td><td>MSC2</td><td>November 9th 03:15</td><td>November 9th 17:00</td><td>3</td><td>0</td><td>2</td></tr><tr><td>13</td><td>MRS2</td><td>November 9th 16:30</td><td>November 10th 15:40</td><td>4</td><td>0</td><td>4</td></tr><tr><td>14</td><td>HMS2</td><td>November 10th 00:40</td><td>November 10th 13:30</td><td>4</td><td>0</td><td>2</td></tr><tr><td>15</td><td>WW2</td><td>November 10th 18:45</td><td>November 12th 06:00</td><td>9</td><td>11</td><td>7</td></tr><tr><td>16</td><td>KPE2</td><td>November 11th 05:30</td><td>November 12th 05:40</td><td>5</td><td>0</td><td>3</td></tr><tr><td>17</td><td>VDB2</td><td>November 11th 10:20</td><td>November 12th 16:45</td><td>11</td><td>6</td><td>5</td></tr><tr><td>18</td><td>ORK2</td><td>November 11th 15:35</td><td>November 12th 17:00</td><td>5</td><td>1</td><td>3</td></tr><tr><td>19</td><td>WND2</td><td>November 12th 09:45</td><td>November 13th 02:30</td><td>6</td><td>0</td><td>4</td></tr><tr><td>20</td><td>LYQ2</td><td>November 12th 10:15</td><td>November 12th 17:25</td><td>3</td><td>0</td><td>1</td></tr><tr><td>21</td><td>MAR2</td><td>November 13th 07:15</td><td>November 14th 10:30</td><td>13</td><td>3</td><td>10</td></tr></table>

To solve the problem an interactive improved ε-constraint method based solution algorithm is developed to acquire the berth–crane assignments and schedules as Pareto frontier. The decision makers are able to take decisions according to the influence of labor costs and service time signi<sup>fi</sup>cance. With this multi-solution approach, decision maker is offered the <sup>fl</sup>exibility of adjusting the balance within con<sup>fl</sup>icting objectives. The model offers the option of the assessment of different policies of berth–crane assignments, by assuring a proper service level while detecting forms of reducing costs related to the operation. To achieve maximum <sup>fl</sup>exibility, the system is designed with a good level of parameterization, letting the decision maker to use the system under numerous possible settings that may appear in practice. The decision support tool enables the decision maker to examine a number of solutions, guiding her towards the <sup>fi</sup>nal decision.

An important issue that may arise in real life practice is the occurrence of unexpected events. These may be due to unpredictable weather conditions, inaccurate container information, inconsistent task handling times, machine breakdowns and extended service times at the hub ports for transhipment vessels. With the current deterministic structure of the system, the decision maker may react to the changes by updating the schedule through embedding into the model the current acquired information so far. This reactive scheme of the decision support system may be seen as a limitation of the system and may further be enhanced to allow for re<sup>fl</sup>ecting the presence of uncertainty while planning the container terminal operations. However, the stochastic feature of vessel arrivals and handling times adds to the complexity of the above-mentioned problem. Indeed, this considerably increased complexity will be a major challenge to manage for further research.

## Acknowledgments

I sincerely acknowledge the generous assistance and valuable information provided by the employees of Port of Izmir, especially by Metin Ozyılmaz who provided excellent information and support throughout the project. Further gratitude is due to the anonymous referees and the editor for their very helpful comments and suggestions which greatly improved the quality of the paper.

## References

[1] D.L. Bandeira, J.L. Becker, D. Borenstein, A DSS for integrated distribution of empty and full containers Decision Support Systems 47 (4) (2009) 383–397

[2] C. Bierwirth, F. Meisel, A survey of berth allocation and quay crane scheduling problems in container terminals, European Journal of Operational Research 202 (3) (2010) 615–627.

[3] J. Blazewicz, T.C.E. Cheng, M. Machowiak, C. Oguz, Berth and quay crane allocation: a mouldable task scheduling model, Journal of the Operational Research Society 62 (2011) 1189-1197

[4] C.Y. Cheong, K.C. Tan, D.K. Liu, C.J. Lin, Multi-objective and prioritized berth allocation in container ports, Annals of Operations Research 180 (2010) 63–103

[5] C.Y. Cheong, M.S. Habibullah, R.S.M. Goh, X. Fu, Multi-objective optimization of large scale berth allocation and quay crane assignment problems, Proc. SMC, 2010, pp. 669–676.

[6] M. Ehrgott, Multicriteria Optimization, Springer, 2005, ISBN 3-540-21398-8

[7] G. Giallombardo, L. Moccia, M. Salani, I. Vacca, The tactical berth allocation problem with quay crane assignment and transshipment-related quadratic yard costs, Proceedings of the European Transport Conference (ETC), 2008, pp. 1–27.

[8] M.M. Golias, M. Boilé, S. Theofanis, Service time based customer differentiation berth scheduling, Transportation Research Part E 45 (6) (2009) 878–892.

[9] M.M. Golias, M. Boilé, S. Theofanis, A.H. Taboada, A multi-objective decision and analysis approach for the berth scheduling problem, International Journal of Information Technology Project Management 1 (1) (2010) 54–73.

[10] X. Han, Z. Lu, L. Xi, A proactive approach for simultaneous berth and quay crane scheduling problem with stochastic arrival and handling time, European Journal of Operational Research 207 (2010) 1327–1340.

[11] M.P.M. Hendriks, M. Laumanns, E. Lefeber, J.T. Udding, Robust periodic berth planning of container vessels, in: H. Kopfer, H.-O. Guenther, K.H. Kim (Eds.), Proceedings of the Third German Korean Workshop on Container Terminal Management: IT-based Planning and Control of Seaport Container Terminals and Transportation Systems 2008, pp. 1-13

[12] A. Imai, J.-T. Zhang, E. Nishimura, S. Papadimitriou, The berth allocation problem with service time and delay time objectives, Maritime Economics & Logistics 9 (2007) 269–290.

[13] A. Imai, H.C. Chen, E. Nishimura, S. Papadimitriou, The simultaneous berth and quay crane allocation problem, Transportation Research Part E 44 (5) (2008) 900-920

[14] C. Liang, Y. Huang, Y. Yang, A quay crane dynamic scheduling problem by hybrid evolutionary algorithm for berth allocation planning Computers and Industria Engineering 56 (3) (2008) 1021–1028.

[15] C. Liang, J. Guo, Y. Yang, Multi-objective hybrid genetic algorithm for quay crane dynamic assignment in berth allocation planning, Journal of Intelligent Manufacturing 22 (2011) 471–479.

[16] G. Mavrotas, Effective implementation of the ε-constraint method in multi-objective mathematical programming problems, Applied Mathematics and Computation 213 (2) (2009) 455–465.

[17] L. Meier, R. Schumann, Coordination of interdependent planning systems, a case study, in: R. Koschke, O. Herzog, K.-H. Rodiger, M. Ronthaler (Eds.), Lecture Notes in Informatics (LNI), 2007, pp. 389–396.

[18] F. Meisel, Seaside Operations Planning in Container Terminals, Physica-Verlag, 2009. [19] F. Meisel, C. Bierwirth, Integration of berth allocation and crane assignment to im- [19] F. Meisel, C. Bierwirth, Integration of berth allocation and crane assignment to im-

prove the resource utilization at a seaport container terminal, in: H.-D. Haasis, H. Kopfer, J. Schonberger (Eds.), Operations Research Proceedings, Springer, Berlin, 2005, pp. 105–110.

[20] F. Meisel, C. Bierwirth, Heuristics for the integration of crane productivity in the berth allocation problem, Transportation Research Part E 45 (1) (2009) 196–209.

[21] F. Meisel, C. Bierwirth, The berth allocation problem with a cut-and-run option, in: B. Fleischmann, K.H. Borgwardt, R. Klein, A. Tuma (Eds.), Operations Research Proceedings 2008, Springer, Berlin, 2009, pp. 283–288.

[22] K.G. Murty, J.Y. Liu, Y.W. Wan, A decision support system for operations in a container terminal. Decision Support Systems 39 (3) (2005) 309–332

[23] E.W.T. Ngai, T.C.E. Cheng, S. Au, et al., Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2007) 62–76.

[24] T. Notteboom, Review of Network Economics 3 (2) (2004), http://dx.doi.org/10.2202/ 1446-9022.1045(ISSN (Online) 1446-9022).

[25] T. Notteboom, Dock labour systems in North-West European seaports: how to meet stringent market requirements? Proceedings of the International Forum on Shipping, Ports and Airports (IFSPA), 2012.

[26] Y.M. Park, K.H. Kim, A scheduling method for berth and quay cranes, OR Spectrum 25 (2003) 1–23.

[27] Port Statistics, Port of Rotterdam Authority, 2012. (May 2013).

[28] W.S. Shen, C.M. Khoong, A DSS for empty container distribution planning, Decision Support Systems 15 (1) (1995) 75–82.

[29] R. Stahlbock, S. Voß, Operations research at container terminals: a literature update, OR Spectrum 30 (2008) 1–52.

[30] D. Steenken, S. Voß, R. Stahlbock, Container terminal operation and operations research — a classi<sup>fi</sup>cation and literature review, OR Spectrum 26 (2004) 3–49.

[31] C. Zhang, L. Zheng, Z. Zhang, L. Shi, A.J. Armstrong, The allocation of berths and quay cranes by using a sub-gradient optimization technique, Computers & Industrial Engineering 58 (2010) 40–50.

[32] I.F.A. Vis, R. De Koster, Transshipment of containers at a container terminal: an overview, European Journal of Operational Research 147 (2003) 1–16

![](/api/attachments/HQ4NDTNA/fulltext/images/956b0b4af3abd4e0eaec4ab2265efc21e50d4f5a18245499e3ec058bc8a58b45.jpg)  
Evrim Ursavas University of Groningen, Groningen, The Netherlands, Assistant Professor of Department of Operations, Faculty of Economics and Business, e.ursavas@rug.nl. Research: Maritime logistics, container terminal operations, management information systems, decision support systems, simulation, heuristic optimization.

Teaching: Maritime logistics, Systems Analysis and Design, Management Information Systems, Quality Engineering, Simulation, Supply Chain Management, Logistics.
