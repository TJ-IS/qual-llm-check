---
otero_id: 4402
otero_key: "ZDM52RSA"
title: "A PAM approach to handling disruptions in real-time vehicle routing problems"
authors: "Xiangpei Hu; Lijun Sun; Linlin Liu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A PAM approach to handling disruptions in real-time vehicle routing problems

Xiangpei Hu, Lijun Sun ⁎, Linlin Liu

Institute of Systems Engineering, School of Management and Economics, Dalian University of Technology, Dalian City 116023, Liaoning Province, China

## a r t i c l e i n f o

Article history: Received 13 January 2011 Received in revised form 6 November 2012 Accepted 4 December 2012 Available online 22 December 201

Keywords: Knowledge representation Object-oriented modeling Local search algorithm Disruption Real-time Vehicle Routing Problem (RVRP)

## a b s t r a c t

During the urban distribution process, unexpected events may frequently result in disruptions to the current distribution plan, which need to be handled in real-time vehicle routing. In this paper, a knowledge-based modeling approach, PAM (disruption-handling Policies, local search Algorithms and object-oriented Modeling), is developed, which combines the scheduling knowledge of experienced schedulers with the optimization knowledge concerning models and algorithms in the <sup>fi</sup>eld of Operations Research to obtain an effective solution in real time. Experienced schedulers can respond to different disruptions promptly with heuristic adjustment based on their experience, but their solutions may be inaccurate, inconsistent, or even infeasible. This method is limited when the problem becomes large-scale. The model-algorithm method can handle large-scale problems, but it has to prede<sup>fi</sup>ne a speci<sup>fi</sup>c disruption and a speci<sup>fi</sup>c distribution state for constructing a model and algorithm, which is in<sup>fl</sup>exible, time-consuming and consequently unable to promptly obtain solutions for responding to different disruptions in real time. PAM modeling approach combines the advantages and eliminates the disadvantages of the two methods aforementioned. Computational experiments show that solutions achieved by this modeling approach are practical and the speed of achieving the solutions is fast enough for responding to disruptions in real time.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Real-time Vehicle Routing Problems (RVRP) play a very important role in the area of urban distribution, because unexpected events, such as customer's demand changes (demand increasing or order cancelling), delivery time window changes (advancement or postponement), disabled roads induced by traf<sup>fi</sup>c accidents or traf<sup>fi</sup>c jams, and vehicle breakdowns constantly result in disruptions to the current distribution plan, which need schedulers to handle these disruptions by readjusting vehicle routes in real time to improve vehicles' ef<sup>fi</sup>ciency and enhance service quality. The objective of disruption handling is to <sup>fi</sup>nd a feasible solution to accommodate the changes and to minimize the negative impacts on the existing distribution process. It does not aim to reduce travel time but minimize the increase of travel time, and it does not aim to increase customer satisfaction but attempts to minimize customer dissatisfaction. In practice, experienced schedulers can respond to different kinds of disruptions promptly. However, they often use intuitive approach to make a simple adjustment, which may not feasible or often be accompanied by inaccuracies and unsuitable for large-scale problems. Another method for handling a disruption is to construct a model and corresponding algorithm [13,21–23,38], which can achieve proper results when solving large-scale problems. Unfortunately, the distribution state changes constantly with the distribution process. For example, Fig. 1 shows that the distribution state could change from (a) at time $t _ { 1 }$ to (b) at time $t _ { 2 } ,$ and from (b) at time t to (c) at time $t _ { 3 }$ with the distribution process. Moreover, disruptions are diverse and can occur at different distribution states. For example, in Fig. 1, a demand-increasing disruption occurs at the distribution state at time $t _ { 1 } ,$ while $\mathtt { a }$ vehicle-breakdown disruption occurs at the distribution state at time $t _ { 2 } .$ Different models and algorithms may be needed to handle diverse disruptions under different distribution states in real time. However, constructing a model and algorithm necessitates the prede<sup>fi</sup>nition of a speci<sup>fi</sup>c distribution state and a speci<sup>fi</sup>c disruption, so this method is in<sup>fl</sup>exible, time-consuming and consequently unable to promptly obtain solutions for responding to different disruptions in real time.

This research proposes a knowledge-based modeling approach, PAM, by combining the scheduling knowledge of experienced schedulers with the Operations Research (OR) knowledge concerning models and algorithms. As the modeling approach exerts the advantages of experienced schedulers and the model-algorithm method, and eliminates their disadvantages, it can dynamically and effectively handle disruptions in RVRP. The remaining part of the paper is organized as follows. Section 2 reviews the related work. Section 3 states the problem and preliminaries. Section 4 proposes the framework of the modeling approach and the representation methods for scheduling knowledge, algorithms and models. Section 5 designs computational experiments and tests the ef<sup>fi</sup>ciency and effectiveness of the modeling approach. Finally, in Section 6, conclusions are drawn and further study is introduced.

![](/api/attachments/ZDM52RSA/fulltext/images/f5b58b72a355f11f453c66866912d7b8c3cd38ffdbbef5b4708b63e6c11c9922.jpg)  
Fig. 1. Different distribution states and diverse disruptions occurring with the distribution process.

## 2. Related work

The methods by which scheduling knowledge, algorithms and models are organized in the modeling approach is one of the foci of the research, which is concerned with the methods used to represent them. Since the early 1980s, a great number of representation methods for modeling and decision making have been presented by researchers in the <sup>fi</sup>elds of Decision Support System (DSS) and OR. Traditional representation methods include logical, network, procedural and frame-based schemes [34]. Methods extended from traditional ones include Production Rules [31], Hierarchical (Tree-like) [11,20], Petri Nets [15], etc. Besides these, in recent years, objectoriented methods have been adopted by many modeling systems [4,32,33,37]. As Nault and Storey have proved, different types of problems are best served by different representation techniques [35], it is necessary to employ different types of knowledge structures to capture different types of information [36]. Therefore, based on the characteristics of the scheduling knowledge, the algorithms, and the models included in the modeling process, different representation methods are respectively adopted for them in the research.

The way in which scheduling knowledge, algorithms and models cooperate in the problem-solving process of the modeling approach is another focus of the research, which is related to the modeling method. A branch for modeling and solving optimization problems is the algebraic modeling language, which was pioneered by GAMS [6], AMPL [17], AIMMS [2,3], and followed by some complementary methods, like AMPL extension language [12], Structure-conveying Modeling Language [9] etc. These methods separated the data from the model, which enabled <sup>fl</sup>exibility of input parameters so the model could be used by various but similar problems. However, these modeling methods can only solve static problems. As solving different disruptions occurring frequently under different distribution states during the distribution process is a dynamic and real-time problem, a different modeling approach is needed.

Existing researches with regard to handling disruptions in the area of RVRP focus on the following aspects: algorithms, models, and DSS. With respect to the problem of new customer requests, Ichoua et al. [23] proposed a vehicle diversion strategy and employed the Tabu search algorithm to solve it. Yang et al. [44] proposed a mixedinteger programming formulation for the of<sup>fl</sup>ine version of the problem and then considered and compared <sup>fi</sup>ve rolling horizon strategies for the real-time version. With respect to the problem of vehicle breakdowns, Li et al. [27,28] developed a Lagrangian relaxation based-heuristic to obtain the strategy for rescheduling one or more vehicles to serve a particular trip and other service trips originally scheduled for the disabled vehicle. Besides these literatures, which focus purely on algorithms and models, there are some researches involving the design of DSS for real-time vehicle routing or rerouting, such as the systems designed by Li et al. [26], Zeimpekis and Giaglis et al. [45–47], Giaglis et al. [18], Fleischmann et al. [16], and Du et al. [14]. In these DSSs, algorithms and models are <sup>fi</sup>xed for solving a de<sup>fi</sup>ned problem with a <sup>fi</sup>xed distribution state, which is in<sup>fl</sup>exible for responding to disruptions occurring under different distribution states in real time. In summary, these researches are gradually improving the optimization techniques in the area of RVRP. However, few of them can solve different disruptions occurring under different distribution states, as most of them use a speci<sup>fi</sup>c model and algorithm to solve a speci<sup>fi</sup>c kind of disruption under a prede<sup>fi</sup>ned distribution state. The objective and constraints of the model are usually <sup>fi</sup>xed, which is unsuitable for the dynamic and real-time problem. In order to overcome this shortcoming, this research develops a modeling approach <sup>fl</sup>exible in objectives and constraints, which change according to variable conditions.

## 3. Problem statement and preliminaries

Since RVRP has many variants, we de<sup>fi</sup>ne the initial problem as Vehicle Routing Problems with Hard Time Windows (VRPHTW). There is one depot, which owns enough homogenous goods and m homogenous vehicles. Dispatched vehicles are usually fully loaded in order to deal with unexpected increased demands. The quantity of customer i's demand is $d _ { i } ,$ and the total delivered quantity in one route must be less than or equal to the capacity of a vehicle, q. The service for customer i should be started within a time window [e , l ], in which $e _ { i }$ and $l _ { i }$ respectively stand for the earliest and the latest start time of unloading goods at customer i's location. Initially, a distribution plan will be generated by one of existing methods of VRPHTW [10]. In other words, the original solution could be mathematically formulized by formulas (1)–(6). Where K is the set of m vehicles; N is the set of n customers involved in this distribution period, while 0 and n+1 stand for the depot respectively denoting the start point and the end point; $c _ { i j }$ is the shortest travel distance between nodes i and $j ; a _ { i k }$ is the time when vehicle k would actually arrive at customer i according to the current plan; s is the service time of customer i; $t _ { i j k }$ is the travel time of vehicle k from customer i to customer $j ;$ $x _ { i j k = }$ 0 otherwise: 1 if vehicle k travels from i to j; <sub>. Formula (1) ensures the least</sub>

cost; formula (2) ensures that one customer would be served by one vehicle; formula (3) ensures that each vehicle starts from and ends at the depot; formula (4) ensures that a vehicle travels in a node must travel out it; formula (5) ensures the time window constraint and formula (6) ensures the capacity constraint.

$$
\min \sum_ {k = 1} ^ {m} \sum_ {i = 0} ^ {n} \sum_ {j = 1} ^ {n + 1} c _ {i j} x _ {i j k}.\tag{1}
$$

$$
\sum_ {k = 1} ^ {m} \sum_ {j = 1} ^ {n} x _ {i j k} = 1 \forall i \in N; i \neq j;\tag{2}
$$

$$
\sum_ {j = 1} ^ {n} x _ {0 j k} = \sum_ {i = 1} ^ {n} x _ {i (n + 1) k} = 1 \quad \forall k \in K;\tag{3}
$$

$$
\sum_ {i = 0} ^ {n} x _ {i h k} - \sum_ {j = 1} ^ {n + 1} x _ {h j k} = 0 \forall h \in N; k \in K; h \neq i \neq j;\tag{4}
$$

$$
x _ {i j k} = 1 \Rightarrow \left\{ \begin{array}{l l} a _ {0 k} = e _ {0}; \\ a _ {j k} = a _ {i k} + s _ {i} + t _ {i j k}; \\ e _ {j} \leq a _ {j k} \leq l _ {j}; \\ e _ {0} \leq a _ {(n + 1) k} \leq l _ {0}. \end{array} \right. \quad \forall i \in N;   \forall j \in N;   i \neq j;   \forall k \in K\tag{5}
$$

$$
\sum_ {i = 1} ^ {n} d _ {i} \sum_ {j = 1} ^ {n + 1} x _ {i j k} \leq q \quad \forall k \in K.\tag{6}
$$

When vehicles are delivering goods based on the scheduled plan, a disruption occurs and thus needs to be handled by a real-time decision process. For example, in Fig. 2(a), at time $t _ { 1 } ,$ customer 7 changed its demand from 2 to 3, which cannot be satis<sup>fi</sup>ed by vehicle $\nu _ { 1 } ,$ , so the decision process would <sup>fi</sup>nd a feasible solution to adjusting the initial distribution plan, which let vehicle $\nu _ { 3 }$ serve the increased quantity and a new routing plan was generated simultaneously (Fig. 2(b)) (In Fig. 2, the numbers out of brackets denote customers, while those in brackets denote the demands and time windows; such as customer 1's demand is 3, and its required service time window is [0,2]. The vehicle's capacity is 10.). The objective of the decision process is not to obtain a solution subject to the initial problem's constraints, but to minimize increased travel time or travel costs induced by disruptions, or to minimize customer dissatisfaction induced by untimely deliveries.

As the scheduling knowledge from experienced schedulers and the optimization knowledge concerning algorithms and models are elements of the modeling approach, several preliminaries about these types of knowledge should be de<sup>fi</sup>ned before developing the approach.

3.1. Preliminary 1. Three principles used in practice by experienced schedulers should be obeyed by the modeling approach.

In practice, a distribution corporation usually regards the current distribution plan as the best solution before a disruption occurs, so the corporation is unwilling to change the plan. As drivers have been informed of this plan, substantially changing it may result in poor morale. Accordingly, it is necessary to keep distribution plan original as much as possible when handling a disruption, which is expressed by Principle 1.

3.1.1. Principle 1: When handling a disruption occurring in a route, keep the regular sequence of customers in another route as much as possible.

Principle 1 is used to guide the development of rules in policy sets. Under its guidance, only when an intra-route algorithm cannot eliminate or decrease the negative effects of a disruption, will the development of a rule mapping an inter-route algorithm be considered. In other words, in a same policy set, a rule involving an intra-route operation in its conclusion will have priority over a rule involving an inter-route operation for handling a same kind of disruption.

In practice, a customer's additional demand will not be rejected unless there is no way to satisfy it within the same distribution period, which is expressed by Principle 2.

![](/api/attachments/ZDM52RSA/fulltext/images/1a7f3f5cd57471c0cf73688783b0009f6fa0863f44c577a7fb2971b1394d5be7.jpg)  
(b) new routing scheme after adjustment

$$
t _ {l}
$$

Fig. 2. An example of disruption management problem with the original solution.

3.1.2. Principle 2: When a customer proposes additional demand, try to satisfy it within the same distribution period.

This principle is used to guide the development of rules for handling Demand-Increasing (DI) disruptions. These rules are contained in P-DI policy set, the details of which can be found in Table 1 in Section 4.2.1.

As satisfying the demands of customers is the most important goal of a distribution, in order to achieve practical solutions, the time window constraints of some customers could be violated and the optimization objective could be changed under some conditions. However, for making the solution ef<sup>fi</sup>cient and effective, the violation and the change should comply with Principle 3.

3.1.3. Principle 3: A distribution plan with on-time deliveries has priority over one with time-violation deliveries, while the one with time-violation deliveries has priority over one with missed deliveries.

Principle 3 is used to guide the modeling process to construct suitable objectives and constraints under corresponding conditions.

3.2. Preliminary 2. Only local search algorithms will be contained in the modeling approach.

In the modeling approach, only local search algorithms will be contained. Larsen et al. argued that in dynamic settings, waiting for a long time in order to get a high quality solution is not possible, because the dispatcher wishes to know the solution to the current problem as soon as possible (preferably within minutes or seconds) [25]. The running-time constraint implies that rerouting and reassignments are often done by using local improvement heuristics like insertion and k-interchange [25]. Giaglis et al. also had the similar viewpoint that local plan adjustment may provide more cost-effective solutions without unnecessarily disturbing the overall initial plan [18]. Although the outcome of local search algorithms depends on initial solutions, it is not a limitation here, as the initial solution is the current distribution plan which is a solution with high quality produced by a metaheuristic algorithm, e.g. tabu search, genetic algorithms, evolution strategies [5]. More speci<sup>fi</sup>cally, local search algorithms can be divided into two categories [13]: intra-route algorithms, which exchange or insert nodes or links within a route; and inter-route algorithms, which in contrast do that between routes.

## 3.3. Preliminary 3. Two objectives and two constraints should be formulated explicitly.

As we know, if <sup>fi</sup>rstly a company promised that the goods could be delivered within the desired time windows, but due to a disruption, it had to deliver in advance or late, those affected customers must be dissatis<sup>fi</sup>ed. Therefore, after a disruption occurs, the decision process of disruption handling will <sup>fi</sup>rstly try to obtain a solution that can satisfy all customers, in which case the objective of the disruption handling is to minimize the increased travel distance with the premise that all customers' time windows could be obeyed. However, if this kind of solution cannot be gained, in order to achieve practical solutions, the time window constraints of some customers could be violated. In the latter case, the objective will be to minimize customer dissatisfaction induced by untimely deliveries. The prioritization of the objectives well explains Principle 3. Furthermore, regardless of time constraints, the constraint of vehicle capacity should be satis<sup>fi</sup>ed as it is a hard constraint.

In the former case, the objective is labeled as Otd, which is represented by formula (7), and the constraint of time window is labeled as Ctw, which could be expressed by formula (8). Where, Set K stands for the set of the remaining vehicles that are still on the road serving the remaining customers. Set $N _ { r }$ stands for the set of the remaining customers. The meanings of other variables and parameters are the same as those detailed before. This objective and constraint are in accordance with the ones generating the original solution.

$$
\text { Otd } \min \sum_ {k \in K _ {r}} \sum_ {i \in N _ {r}} \sum_ {j \in \{N _ {r}, (n + 1) \}} c _ {i j} x _ {i j k}.\tag{7}
$$

$$
\text { Ctw } x _ {i j k} = 1 \Rightarrow \left\{ \begin{array}{l l} a _ {0 k} = e _ {0}; \\ a _ {j k} = a _ {i k} + s _ {i} + t _ {i j k}; \\ e _ {j} \leq a _ {j k} \leq l _ {j}; \\ e _ {0} \leq a _ {(n + 1) k} \leq l _ {0}. \end{array} \right. \quad i \in N _ {r}, j \in N _ {r}, a n d i \neq j; k \in K _ {r}.\tag{8}
$$

In the latter case, the objective is labeled as Otv. Although traditional researches all imposed a penalty for the violation of a time window, it is hard to set the coef<sup>fi</sup>cient of the penalty for customers individually in practice. However, in real-world operation, each customer has a maximum tolerance of time violation, which is easier to be gained. A customer's dissatisfaction is related to the maximum tolerance and the time violation. For example, if a customer's tolerance is 10 min, while the delivery is 15 min later, his/her dissatisfaction will be high. However, if the case happened on a customer with 60 min tolerance, the dissatisfaction will be lower than the former one. Based on this idea, we de<sup>fi</sup>ned customer dissatisfaction by the ratio of the time violation to the maximum tolerance, which is a more operable method than setting the coef<sup>fi</sup>cient of the penalty. We name the ratio the degree of time violation, which can be calculated by formula (9). Therefore, Otv could be calculated by formula (10). Where $S _ { i k }$ represents the degree of time violation of customer i by vehicle k. $\varDelta t _ { i }$ stands for the maximum tolerance of time violation of customer i. The meanings of other variables and parameters are the same as those appeared before.

$$
S _ {i k} = \left\{ \begin{array}{l l} \sum_ {j = 1} ^ {n + 1} x _ {i j k} \cdot \frac {e _ {i} - a _ {i k}}{\Delta t _ {i}}, & a _ {i k} <   e _ {i}; \\ 0, & e _ {i} \leq a _ {i k} \leq l _ {i}; \\ \sum_ {j = 1} ^ {n + 1} x _ {i j k} \cdot \frac {a _ {i k} - l _ {i}}{\Delta t _ {i}}, & a _ {i k} > l _ {i}. \end{array} \right.\tag{9}
$$

$$
\text { Otv } \min \sum_ {k} \sum_ {i} S _ {i k}, i \in N _ {r}; k \in K _ {r}.\tag{10}
$$

In the soft time window application of Taillard et al. [43], the service time is not allowed to be earlier than the early time window, but the late time window can be violated at expense of a penalty. In formula (9), both of early and late time windows can be violated, that is because there are studies on those Vehicle Routing Problems with Soft Time Windows (VRPSTW) that both early and late time windows can be violated. For example, in Calvete et al.'s study [7], delivery starts as soon as the vehicle arrives at the customer location, and the vehicle leaves the customer as soon as the delivery has been completed. In Ioannou et al.'s research [24], vehicles are allowed to service customers before and after the earliest and latest time window bounds, respectively. In studies of Balakrishnan [1], Chiang and Russell [8], due to the maximum waiting time, not all services could start after the earliest time; some services violated the earliest time. Balakrishnan [1] argued that it is reasonable in practice due to restrictions on the time a vehicle is allowed to park at a customer's loading zone or due to limits imposed on the total idle time of any vehicle. Besides these studies, it is common sense that drivers prefer <sup>fi</sup>nishing all work as soon as possible to goo<sup>fi</sup>ng in cabs waiting for the arrival of the time when they are allowed to start the service. Hence, formula (9) adopted this kind of soft time window that both early and late time windows can be violated.

Besides the above mentioned two objectives and one constraint, there is a hard constraint, vehicle's capacity that should be obeyed by all cases. In the modeling process, this constraint is labeled as Cc, which is expressed by formula (6).

Table 1 P-DI Policy set.

/\*\*facts: customer(Cno,Initial\_demand,Increaseddemand,Cv,Distribution\_state); vehicle(Route\_no,Capacity,Redundant,Used\_state). Meanings of variables: Cno: the customer's No; Initial\_demand: the initial demand of the customer (this variable will not be used by the P-DI policy set, but will be used by other policy sets); Increaseddemand: the additional demand that the customer wants after the distribution starts; Cv: the vehicle's No. that is in charge of this customer's initial task; Distribution\_state: it stands for that a customer has been served (instantiated by 1), not be served (instantiated by 0) or being served (instantiated by 2); Route\_no: it is the same as the vehicle's No. that is in charge o the route; Capacity: the vehicle's capacity; Redundant: the vehicle's redundant load in current distribution period; Used\_state: it stands for that a vehicle's state is used (instantiated by 1) or unused (instantiated by 0). \*\*/ /\*\*Before rules are presented, some functional predications are de<sup>fi</sup>ned as follows\*\* /\*check all vehicles' state\*/ check AVstate:- vehicle(\_,\_,\_,Used\_state), Used\_state=1. /\*check other vehicles' state\* check\_OVstate(Cv):- vehicle(Route\_no,\_,\_,Used\_state), Route\_no\=Cv, Used state =1. /\*check if all vehicles' redundant load can satisfy the increased demand\* checkARedundantLoad(IncreasedDemand):- vehicle(\_,\_,Redundant,1), Redundant>=IncreasedDemand. /\*check if other vehicles' redundant load can satisfy the increased demand\* check\_ORedundantLoad(Cv, IncreasedDemand):- vehicle(Route\_no,\_,Redundant,1), Route\_no\=Cv, Redundant>=IncreasedDemand. /\* Rule 1: IE the initial demand of the customer who induced the DI disruption has been delivered. AND there is no less than one vehicle's redundant load that can satisfy the increased de: mand, THEN insert the increased demand into a suitable routes.\*/ pDI(Operation,Cno,Quantity,Cv):- customer(Cno,\_,IncreasedDemand,Cv,1), vehicle(\_,\_,Redundant,1) (Redundant>=IncreasedDemand), Quantity is IncreasedDemand, Operation="Insert". /\* Rule 2: IF the initial demand of the customer who induced the DI disruption has been delivered, AND there is no single vehicle's redundant load that can satisfy the increased demand, THEN split the increased demand by the quantity of the redundant loads of vebicles on the road and insert these split quantities to their corresponding routes.\* pDI(Operation,Cno,Quantity,Cv):- customer(Cno,\_,IncreasedDemand,Cv,1) not(checkARedundantLoad(IncreasedDemand)), Quantity is IncreasedDemand, Operation =."Insert-split" /\* Rule 3: IF the initial demand of the customer who induced the DI disruption has been delivered, AND all vehicles' states are unused, THEN the increased demand should be postponed to the next distribution period. \*/ pDI(Operation,Cno,Quantity,Cv):- customer(Cno,\_,IncreasedDemand, Cv,1), not(check\_AVstate) Quantity is IncreasedDemand, Operation =."New-dispatching" /\* Rule 4: IF the initial demand of the customer who induced the DI disruption has not been delivered, AND there is no less than one vehicle's redundant load that can satisfy the difference between the increased demand and the redundant load of the vehicle in charge of the customer according to the original distribution plan, THEN insert the difference to another route.\*/ pDI(Operation,Cno,Quantity,Cv):- customer(Cno,\_,IncreasedDemand,Cv, Distribution\_state) Distribution\_state\=1, vehicle(Cv,\_,Available\_load,\_) Quantity is (IncreasedDemand-Available\_load), vehicle(Route\_no,\_,Redundant,1), Route\_no\=Cv, Redundant> Quantity, Operation="Insert". /\* Rule 5: IF the initial demand of the customer who induced the DI disruption has not been delivered AND there is no single vehicle's redundant load that can satisfy the difference between the increased demand and the redundant load of the vehicle in charge of the customer according to the original distribution plan, THEN split the difference by the quantity of the redundant loads of other vehicles on the road, and insert these split quantities to their corresponding routes.\*/ pDI(Operation,Cno,Quantity,Cv):- customer(Cno,\_,IncreasedDemand,Cv, Distribution\_state), Distribution\_state\=1, not(check\_ORedundantLoad(Cv, IncreasedDemand)), vehicle(Cv,\_,Available\_load,\_) Quantity is (IncreasedDemand-Available\_load), Operation =."Insert-split" /\* Rule 6: IF the initial demand of the customer who induced the DI disruption has not been delivered, AND all other vehicles' states are unused, THEN postpone the difference between the increased demand and the redundant load of the vehicle in charge of the customer to the next distribution period. \*/ pDI(Operation,Cno,Quantity,Cv):- customer(Cno IncreasedDemand Cy Distribution, state) Distribution\_state\=1, vehicle(Cv,\_,Available\_load,1), not(check\_OVstate(Cv)), Quantity is (IncreasedDemand-Available\_load), Operation=“New-dispatching.”

Formulas (6), (7), (8), (9), and (10) are incomplete models, they express the part of a model that the modeling process for disruption adjustment should explicitly formulate. The other parts that stand for the conservation of the <sup>fl</sup>ow constraints in RVRP would be implicitly expressed by local search heuristics in the modeling process.

## 4. The modeling approach

## 4.1. The framework of the modeling approach

The framework of the modeling approach consists of three major parts, disruption-handling Policies (P), local search Algorithms (A) and object-oriented Modeling (M). We name it PAM modeling approach. The P part originates from scheduling knowledge, which consists of concrete scheduling rules. The A part contains the two kinds of heuristic algorithms, intra-route local search algorithms and inter-route ones, which were mentioned in Preliminary 2. The models in M part contain the two objectives (Otd and Otv) and two constraints (Ctw and Cc) that were mentioned in Preliminary 3, and thus the M part will construct the components of these objectives and constraints corresponding to a speci<sup>fi</sup>c problem during the modeling process. The relationship among the three parts is explained in detail in the following paragraph.

Disruption-handling policies are developed based on Principle 1 and Principle 2. They link the situation of a disruption to the choice of local search algorithms. A local search algorithm has two functions in the modeling approach. Complying with Principle 3, it is <sup>fi</sup>rstly used to check if a feasible solution satisfying current constraints can be obtained by a test run. If it cannot, relaxed constraints will be checked. The relaxation process will iterate until the <sup>fi</sup>nal objective and constraints are identi<sup>fi</sup>ed. Secondly, with the <sup>fi</sup>nal running, it can <sup>fi</sup>nd out the near optimal solution based on the identi<sup>fi</sup>ed objective and constraints. Object-oriented modeling is the model construction process, which will construct the constraint components for the algorithm's test run and constructs the components of the corresponding objective and constraints for the algorithm's <sup>fi</sup>nal run. The relationships among P, A, and M can be brie<sup>fl</sup>y described by Fig. 3, in which Pf, Af and Mf indicate the functions of P, A and M respectively, and arrows indicate the directions from a part's output to another part's input.

As algorithms for RVRP are heuristic, they can exert some part of a model's function. For example, the conservation of the <sup>fl</sup>ow constraints in a model of RVRP can be guaranteed in the implementation of a heuristic algorithm. Only the objectives and some constraints needing calculation should be explicitly formulated when an algorithm runs. The process for identifying the objectives and the constraints corresponding to a speci<sup>fi</sup>c problem will be achieved by Af1 of the A part collaborating with the Mf1 of the M part.

As policies relate the scheduling knowledge from experienced sched ulers for qualitatively handling a disruption to suitable optimization algorithms, the PAM framework combines both advantages of Knowledgedriven DSS and Model-driven DSS [39]. The P part can suggest or recommend operations for further generating a new distribution plan, which is in accordance with the aim of a Knowledge-driven DSS [39], while the A and M parts can make algorithms and models accessible to a non-technical specialist, which is in accordance with the aim of a Model-driven DSS [40]. Moreover, the PAM framework has been beyond an expert system, as the P part operates like an expert system while the A and M parts exert the power of optimization in OR to make more effective decisions. Although some frameworks for real-time decision problems of vehicle dispatching or routing, which are similar to the problem discussed in this paper, were proposed in the discipline of OR (such as frameworks proposed by Séguin et al. [41] and Giaglis et al. [18]), they are too general and can only be used to guide the development of more speci<sup>fi</sup>c frameworks. In contrast, the PAM framework is speci<sup>fi</sup>c to the operational level, and thus it is more suitable for solving practical problems.

As the question of how the modeling approach is ef<sup>fi</sup>ciently and effectively realized depends on the representation methods for policies, algorithms and models, Section 4.2 will propose these methods.

## 4.2. Representation methods

## 4.2.1. Representation method for policies

As rules are claimed to be both natural and plausible, thereby providing a means of representation that is very similar to the structure of fundamental mechanisms of human cognition [35], they are used to represent policies. As the scale of rules is not large, a tree-like graphical representation [29] was used at the designing stage to display combinations of various conditions. This representation can make sure that all possibilities are covered and simultaneously no two rules can be validated as true at the same time. The inherence of tree-like representation ensures that conditions are different between any two nodes, and they cannot be true at the same time due to exclusion of the branching conditions [29]. In order to evaluate the quality and performance of the rules, we tested them by examples that covering all inputs and that can lead to the failure of reasoning. During the testing process, experienced schedulers were also involved for evaluating the reasoning results. Finally, rules are implemented in Prolog programming language. Table 1 shows the representation of rules for handling DI disruptions.

As a rule just qualitatively de<sup>fi</sup>nes what kind of operation should be used, the realization of the operation depends on the related algorithm and corresponding models, as indicated in the framework of PAM (Fig. 3). Although different rules could map different situations to the same algorithm (for example, Rule 1 and Rule 4 in Table 1 map different situations to the Insertion algorithm), the domains in which the algorithm will operate, and the models used to evaluate the neighborhood solutions generated by the algorithm would not be the same. Hence, representing algorithms and models with proper methods are also important for the modeling approach.

## 4.2.2. Representation method for algorithms

Local search algorithms have the common running process consisting of the following 6 steps [19].

![](/api/attachments/ZDM52RSA/fulltext/images/3569e3422a1387eb2ec658bf430e6aa54713d2aa2f70aea5e53c042f63bef2b3.jpg)  
Fig. 3. The relationships among P, A and M.

Step 1 de<sup>fi</sup>nes the initial solution, which is the start point of a local search algorithm. The component INITIALIZATION is used to obtain the necessary parameters. It is the basic input of an algorithm. Besides, it is the interface between a rule and an algorithm. The component is necessary for separating the data from the <sup>fl</sup>ow of an algorithm.

Step 2 generates the neighborhood solutions. This task needs an OPERATOR to de<sup>fi</sup>ne how a neighborhood solution is created. Different algorithms have different operators. For local search algorithms, all operations can be summarized into two categories, deleting roads i.e. links from the current routes, or adding roads to the current routes. Therefore, we use two facets, “Deletedroads” and “Added-roads”, which are the sets that aggregate the deleted roads and the added roads respectively, to describe this component.

Step 3 selects the feasible solutions from the neighborhood solutions. The ful<sup>fi</sup>llment of the task depends on the component of FEASIBILITY, which is used to check if the constraints can be satis-<sup>fi</sup>ed by a neighborhood solution. This component is realized by the constraints of the model that will be constructed by the modeling process in Section 4.3.

Step 4 selects a most suitable solution from the feasible solutions as the next current solution for generating next neighborhood solutions. The component of EVALUATOR is used to compare the feasible solutions with the current solution and <sup>fi</sup>nd out the better one. The component is realized by the optimization objective of the model constructed by the modeling process in Section 4.3.

Step 5 checks whether the recursive condition has been reached or not, as algorithms will recursively run until some condition is reached. The component of RECURSIVE-CONDITION de<sup>fi</sup>nes the condition. Its data type is Boolean, in which “true” means continuing the recursion, while “false” means stopping the recursion.

Step 6 con<sup>fi</sup>rms the selected solution as the current solution until the recursion <sup>fi</sup>nishes. This task will be ful<sup>fi</sup>lled by the component of OUTPUT.

Besides the six components mentioned above, the identi<sup>fi</sup>er of an algorithm is necessary. We use NAME as an algorithm's identi<sup>fi</sup>er, which is used to link the conclusion of a rule to the corresponding algorithm, and to locate the other six components of the algorithm.

The above analysis shows that a local search algorithm can be made from the seven components, NAME, INITIALIZATION, OPERATOR, FEASIBILITY, EVALUATOR, RECURSIVE-CONDITION, and OUTPUT. Besides, a generic procedure is needed for controlling the <sup>fl</sup>ow of algorithms. As frames provide a convenient way to combine declarations and procedures within a knowledge representation scheme [35], it is suitable for representing algorithms. Hence we created a frame-based representation method. As analyzed above, the representation should contain two parts. One part is the seven components used to modularize an algorithm. The other part is a generic procedure used to control the <sup>fl</sup>ow of algorithms. The generic procedure will be instantiated by the seven components of the algorithm that is con<sup>fi</sup>rmed by a rule.

Table 2 takes Insertion algorithm as an example to show the modularization of an algorithm. Table 3 de<sup>fi</sup>nes the generic procedure. Compared with other local search algorithms (such as 2-opt [30], λ-exchange), the Relocate algorithm and the Insertion algorithm only change the solution one time, so they are exclusively de<sup>fi</sup>ned in the generic procedure.

## 4.2.3. Representation method for models

As Pillutla and Nag argued, a problem characterized by the presence of natural entities and using special algorithms as optimization techniques is suitable for using object-oriented model representation [37]. In our research, the natural entities are customers, vehicles, roads, orders etc., while the special algorithms are local search algorithms. Therefore, models will be represented by an object-oriented scheme, which suits the real-world case and facilitates the model construction and solution process. Moreover, object-oriented model representation method can directly handle the data in the database.

```txt
Table 2
Modularization of Insertion algorithm.

NAME
<Insertion>
INITIALIZATION
Customer- to-be-inserted: j
Untraveled-roads: {{start-node, end-node, vehicle-id}}
OPERATOR
For {{a_i, i, r_i}} ⊂ Untraveled-roads
Deleted-roads: {{a_i, i, r_i}}
Added-roads: {{a_i, j, r_i}, [j, i, r_i]}
Flag {{a_i, i, r_i}}
/* i stands for customer i. r_i stands for the route that customer i belongs to. a_i stands for the anterior customer of i. Flag marks the subset that has been examined in the set of untraveled-roads */
RECURSIVE-CONDITION: Boolean
If ∃ {{a_i, i, r_i}} ⊂ Untraveled-roads has not been examined, True;
Otherwise, False
FEASIBILIT: Boolean
Check C
EVALUATOR: real
Calculate O
OUTPUT(Untraveled-roads)
Untraveled-roads deduct Deleted-roads plus Added-roads
/*C and O stand for the constraints and objective of the model that will be constructed by the modeling process*/
```

Based on the object-oriented idea, a model can be decomposed into two levels, the model-component level and the model-element level [19]. The model-component level contains Objectives and Constraints. An objective or a constraint component consists of model elements. Model elements contain the following objects: Entities and their Sets (E&S), Entity Attributes (EA), Entity Relations (ER) and Operators (O). Entities include customers, vehicles, roads, and planned routes. An entity set is the aggregation of a kind entity or its subset. The E&S objects denote the identi<sup>fi</sup>cations of parameters or variables. The values of EA denote the values of parameters. EA objects include two kinds, Static Entity Attributes (SEA) and Dynamic Entity Attributes (DEA). The values of SEA represent properties of an entity, such as a customer's demand, a vehicle's capacity, and a road's distance, which are stored in the system's database. The values of DEA are calculated in the process of routing and scheduling, for example, the values of a . ER objects denote 0-1 variables in models.

```txt
Table 3
Generic procedure.

Define current-cost ←∞
    new-cost ← 0
    current-tour ← Untraveled-roads
    temporary-tour ← Untraveled-roads
    A ← NAME

INITIALIZATION

While RECURSIVE-CONDITION do

Begin

OPERATOR

If FEASIBILITY then
    new-cost ← EVALUATOR
    If (new-cost<current-cost) then
    current-cost ← new-cost
    If A=<Relocate> or A=<Insertion> then
    current-tour ← OUTPUT(temporary-tour)
    Else

    current-tour ← OUTPUT(current-tour)

End

Put out current-tour
```

For example, if the road identi<sup>fi</sup>ed by i-j is planned to be traveled by the vehicle identi<sup>fi</sup>ed by h, the value of the variable $x _ { i j h }$ will be 1. This kind of relation will be indicated by the representation of current distribution system's state [42]. The O objects are the computational and comparison notations, like max, min, ≥, etc.

In general, the architecture of the model decomposition and representation described above can be illustrated by Fig. 4 [19]. The left part of the <sup>fi</sup>gure re<sup>fl</sup>ects the “part-of” relation, which means that a model element is a part of a model component, while a model component is a part of a model. The middle part of the <sup>fi</sup>gure re<sup>fl</sup>ects the “kind-of” relation, which means that an objective or a constraint is a kind of the model component, while an E&S, EA, ER or O is a kind of the model elements and a SEA or DEA is a kind of the EA. The right part of the <sup>fi</sup>gure indicates the corresponding formulas de<sup>fi</sup>ned in Section 3. This object-oriented representation can support the modeling process ef<sup>fi</sup>ciently by methods and operations attached to the model component or the model element.

The name of a method is pre<sup>fi</sup>xed by “M-”. For example, the method for constructing the constraint Ctw is named M-Ctw, and the method used to obtain the value of a Static Entity Attribute is named M-Obtain-SEA(). A method can use other methods to realize its function. For instance, method M-Ctw uses method M-Obtain-SEA() and M-Obtain-DEA(). Entities and entity attributes will be gotten directly from the system's database. For example, the value of the Customer(supposed-start-time) will be read from the table named “DynamicRouting” in database, while Customer(latest-start-time) and Customer(earliest-start-time) will be read from the table named “Customer”. An attribute name is consistent with a column name in the table, and the ID of an entity will be used to locate it. Taking the construction of formula Ctw for example, Fig. 5 shows the process. The top-down dashed arrows at the right side of the <sup>fi</sup>gure denote the transferring directions of some necessary parameters, while the bottom-up real line arrows at the left side indicate the transferring directions of the results of model constructing.

## 4.3. The process of modeling

In urban distribution process, several types of disruptions from three sources could happen (see Table 4). As the effect of postponed delivery time, advanced delivery time, reparable vehicle breakdown and road construction to the current distribution is time violation (TV), the same kind of policy set P-TV is applicable to these disruptions. Besides, other four policy sets, P-DI, P-OC, P-DR, and P-DV, are respectively used to handle demand-increasing (DI), order-canceling (OC), disabled-road (DR), and disabled-vehicle (DV) disruptions. Before the modeling process starts, there should be a graphical user interface (GUI) for entering the disruption and its related data. This interface was developed according to the sources, disruption types and input values in Table 4. Fig. 6 shows an example of GUI for entering a DI disruption and its related data, which indicates that the source of this kind of disruption is customers, and it is a demand-increasing disruption, and the two parameters, the customer's ID identifying who brought out the disruption, and the increased quantity are needed to be inputted.

After the input values are obtained by the P part of PAM modeling process, the input-checking rules will <sup>fi</sup>rstly function. These rules contains two parts, one part is to check if the input parameters are valid, while the other part is to check if a disruption is indeed incurred by this event. Table 5 lists rules of these two parts in P-DI policy set implemented by WPI-Prolog language.

After a disruption is con<sup>fi</sup>rmed by the input-checking rules, pDI/4 rules de<sup>fi</sup>ned in Table 1 will be matched to <sup>fi</sup>nd out the suitable operations, and then the modeling process involving the A and M parts will start. Supported by the representations of policies, algorithms and models, the modeling and problem-solving process can be illustrated by Fig. 7.

Three major tasks are ful<sup>fi</sup>lled by the modeling process, matching a rule successfully, getting the most suitable algorithm, and achieving the suitable model components by using several components of the algorithm and the operation Check. The operation Check is used to check if the constraints can be satis<sup>fi</sup>ed. Its result is true or false standing for whether the constraints can be satis<sup>fi</sup>ed or not. This operation is attached to the constraints, Cc and Ctw, in the objectoriented knowledge representation for model. According to Principle 3, there will be four combinations of objectives (using O stands for objectives) and constraints (using C stands for constraints), C=Cc and O=Otv, C=Cc&Ctw and O=Otd, C=Ctw and O=Otd, C=ϕ and O=Otv, among which only one of them will be con<sup>fi</sup>rmed <sup>fi</sup>nally. C=ϕ means that no constraints need to be checked. After the objective and constraints are con<sup>fi</sup>rmed, the algorithm will be instantiated completely and the generic procedure will work to get the <sup>fi</sup>nal result. Fig. 8 shows the GUI for displaying the computational result of the example shown by Fig. 6.

The implementation of the modeling process integrates three development platforms, Delphi for implementing GUI, SWI-Prolog for implementing rules, and Visual Studio 2005 for implementing algorithms and constructing models in C++ programming language. The algorithms and models implemented by C++ are built to DLL,

![](/api/attachments/ZDM52RSA/fulltext/images/827095c296b85166a6cc05eb226cee8f96a35b847fe73214771ac0075a362439.jpg)  
Fig. 4. The object-oriented representation method for models.

![](/api/attachments/ZDM52RSA/fulltext/images/63d928f5d746cd48e69d5876a39ca13aa303414528c6f00f0672b8d2eb8a6335.jpg)  
Fig. 5. The process of constructing the model component of Ctw.

which can be called by the interface module developed with Delphi. The communication between the SWI-Prolog and C++ is bridged by Python language. C++ uses the lib of boost.python to access Python, and Python accesses SWI-Prolog by the lib of pyswip, by which process the reasoning results of the Prolog will be returned to the C++ module for the further modeling process.

Table 4  
Disruption sources, disruption types, input values and corresponding policy sets.

<table><tr><td>Sources</td><td>Disruption types</td><td>Input values</td><td>Corresponding policy set</td></tr><tr><td rowspan="4">Customers</td><td>Demand Increasing</td><td>Customer ID, Increased quantity</td><td>P-DI</td></tr><tr><td>Order Canceling</td><td>Customer ID</td><td>P-OC</td></tr><tr><td>Postpone Delivery Time</td><td>Customer ID, Postponed Time</td><td>P-TV</td></tr><tr><td>Advance Delivery Time</td><td>Customer ID, Advanced Time</td><td>P-TV</td></tr><tr><td rowspan="2">Vehicles</td><td>Disabled Vehicle</td><td>Vehicle ID</td><td>P-DV</td></tr><tr><td>Reparable Vehicle Breakdown</td><td>Vehicle ID, Delayed Time</td><td>P-TV</td></tr><tr><td rowspan="2">Roads</td><td>Disabled Road</td><td>Road ID</td><td>P-DR</td></tr><tr><td>Recoverable Road</td><td>Road ID Delayed Time</td><td>P-TV</td></tr></table>

## 5. Computational experiments

## 5.1. Design of experiments

As there are no benchmark problems for disruptions in RVRP, this paper generates a set of disruption problems based on Professor Cordeau's VRP benchmark problems obtained from a website. The benchmark problems for Capacitated Vehicle Routing Problem with Time Windows (CVRPTW) are used, which include 56 problem description <sup>fi</sup>les (http://neo.lcc.uma.es/radi-aeb/WebVRP/data/instances/ cordeau/C-vrptw.zip) and 56 solution <sup>fi</sup>les (http://neo.lcc.uma.es/radiaeb/WebVRP/data/instances/cordeau/C-vrptw-sol.zip). These problems are grouped by C type, R type and RC type. Problem sets C have the clustered customers. Sets R have the customers' locations generated uniformly and randomly over a square. Sets RC have a combination of randomly placed and clustered customers. In order to comprehensively test the ef<sup>fi</sup>ciency and effectiveness of the PAM modeling approach, the experimental data will be generated for the three types. We selected C101 and C104 from C type, R104 and R107 from R type, RC104 and RC108 from RC type. The reason for selecting these problems is that their solutions contain the same amount of routes, 10, which require the service of 10 vehicles. As in practice a distribution center or corporation usually owns a limited number of vehicles, we assume that this number is 10. In practice, DI disruption is the most frequently occurring one in some special distribution industries. For example, in the oil distribution industry, those industries that produce services not goods and need oil as fuel, like restaurants, hotels, etc. are not willing to store oil because the storage of oil has potential dangerousness. They usually order a small quantity with high frequency. In this case, increasing demand is the most frequent disruption. Accordingly, in the computational experiment, we will test the PAM modeling approach under the

![](/api/attachments/ZDM52RSA/fulltext/images/192b475acb82ffba20ed35826008f8b89c7db4c2b519ec3685cf0764afcc82d2.jpg)  
Fig. 6. An example of GUI for entering a DI disruption and its related data

## Table 5

```prolog
Input-checking rules in P-DI policy set.
/*First part: parameter checking*/
read_customer_id(C) :-
    readln(CC),
    [C | _] = CC,
    customer(C,_,_,_,_).
read_amount(V) :-
    readln(VV),
    [V | _] = VV,
    V > 0.
readparams(C, V) :-
    read_customer_id(C),
    read_amount(V).
/*Second part: disruption checking*/
check_AVstate :-
    vehicle(_,_,_,Us),
    Us = 1.
demand_increasing_disruption_finished(Cid, Inc) :-
    customer(Cid,_,_,Veh,_), 
    vehicle(Veh,_,Red,_), 
    Inc > Red.
demand_increasing_disruption_unfinished(Cid,Inc) :-
    customer(Cid,_,_,_,1),
    Inc > 0,
    vehicle(_,_,_,1).
demand_increasing_disruption_Afinished(Cid,Inc) :-
    customer(Cid,_,_,_,1),
    Inc > 0,
    not(check_AVstate).
demand_increasing_disruption(Cno,IncreasedDemand) :-
    demand_increasing_disruption_finished(Cno,IncreasedDemand);
    demand_increasing_disruption_unfinished(Cno,IncreasedDemand);
    demand_increasing_disruption_Afinished(Cno,IncreasedDemand).
```

circumstance of DI disruptions. Another assumption is that vehicles will be fully loaded before they start their distribution tasks in order to respond to unexpected increased demands, so the redundant load of a vehicle is de<sup>fi</sup>ned as the difference between the vehicle's capacity and the total demands in the route to be served by the vehicle.

Before a disruption occurs, the distribution plan will be executed following the 10 routes. As disruptions occur randomly, in order to ensure an environment close to the real world, the time when and the position where the disruption occurs will be generated randomly as follows.

For a selected problem, <sup>fi</sup>rst of all, pseudo-random number generator generates an integer, i, among [1,100] as the customer's no. who brings out the demand-increasing requirement. Then, the route v which customer i belongs to in the corresponding solution <sup>fi</sup>le will be found out. The time when the demand-increasing event occurs is a randomly generated integer that is bigger than 0 and less than the latest time of the depot's time window. Moreover, in order to ensure that the event must result in a disruption, the boundary of the increased demand should also be speci<sup>fi</sup>cally de<sup>fi</sup>ned according to the distribution state as follows. If the distribution for the initial demand of customer i has been <sup>fi</sup>nished, the quantity of the demand will be an integer generated among [1, 100]. Otherwise, the demand will be an integer that is bigger than the redundant load of the vehicle serving the route v (using $r l _ { \nu }$ to represent the redundant load) and less than max(100, 1.5∗rl ).

100 DI disruptions will be generated respectively by the above mentioned method for each problem of C101, C104, R104, R107, RC104, and RC108. In order to limit the length of the paper, Table 6 just lists a part of such generated data. For example, in the route numbered 9 in problem C101, customer 75 increased its demand by the quantity of 24 at the time of 105 (see the second row in Table 6). For each disruption, manual method and PAM modeling approach will be used individually to obtain a <sup>fi</sup>nal solution.

The manual method for handling this kind of disruptions is de<sup>fi</sup>ned as follows:

If the initial demand of customer i has not been served or if it is being served, the following steps will be taken.

Step 1. Assign all of the redundant load of the vehicle on the route v, $\boldsymbol { r l } _ { \nu } ,$ to customer i;

Step 2. Assign the quantity of min $( r l _ { v _ { e } } , q _ { u } )$ to vehicle $\nu _ { e }$ and insert it to the end of the queue being served by the vehicle. $( q _ { u }$ represents the remaining unsatis<sup>fi</sup>ed quantity; vehicle $\nu _ { e }$ stands for the vehicle that can come back to the depot <sup>fi</sup>rst after <sup>fi</sup>nishing all its initial tasks among the remaining vehicles, $r l _ { v _ { e } }$ represents vehicle ${ \nu _ { e } } ^ { \prime } s$ redundant load.)

![](/api/attachments/ZDM52RSA/fulltext/images/1fc07035ba964c7dd40f9103a840c39b8f217af9d176007ddbca688ecc6b5c25.jpg)  
Fig. 7. The modeling and problem-solving process for handling a disruption.

Step 3. Repeat Step 2 until the total increased demand is satis<sup>fi</sup>ed or all vehicles' redundant loads become 0.

If the initial demand of customer i has been <sup>fi</sup>nished, handle the increased demand by Step 2 and Step 3.

The above rules are from schedulers who just can qualitatively handle DI disruptions. As these rules are also heuristic, they will be simulated and implemented by C++. In this research, by developing the PAM modeling approach, we optimize these rules by combining OR optimization techniques. Rules in P-DI policy set de<sup>fi</sup>ned in Table 1 will be used by PAM modeling approach in this case. As the disruption data is generated randomly, the input interface of the PAM modeling system will not be used during the experiment. For the reasoning process, the generated data and the data related with the current distribution state will be transformed to facts by C++ and transferred to the dynamic fact-base of SWI-Prolog by pyswip with the function of prolog.assertz(). The experiment is conducted in a computer with the 32 bits Windows 7 operating system running on the following hardware: CPU—Intel Dual Core with 2.8 GHz, 2.00 GB of RAM.

![](/api/attachments/ZDM52RSA/fulltext/images/0344c8b9a2098299527ff264cbd2db4e2c99c962c3f5f2a4194c20566583cc93.jpg)  
Fig. 8. The computational result of the example shown by Fig. 6.

## 5.2. Analysis of the results

The results of the two different methods are aggregated respectively by the six problems, C101, C104, R104, R107, RC104, and RC108. Table 7 compared the results of the two methods from the following 5 criteria (M stands for the manual method):

1) “Average cost”: It means that for the 100 DI disruptions in a problem, the average increased travel distance of the 100 solutions achieved respectively by the two methods compared with the original solution to the problem.

2) “Average amount of the affected customers”: In a solution to a DI disruption, in order to try to satisfy all demands, some customer's time windows have to be violated. This kind of customers is de<sup>fi</sup>ned as the affected customers. The criterion compares the average amount of the affected customers of the 100 solutions achieved respectively by the two methods.

Table 6  
A part of experimental data

<table><tr><td>Problem type</td><td>Route No</td><td>Position</td><td>Occurring time</td><td>Increased demand</td></tr><tr><td>C101</td><td>9</td><td>75</td><td>105</td><td>24</td></tr><tr><td>C101</td><td>8</td><td>93</td><td>116</td><td>12</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>C104</td><td>10</td><td>75</td><td>753</td><td>34</td></tr><tr><td>C104</td><td>9</td><td>93</td><td>116</td><td>12</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>R104</td><td>9</td><td>75</td><td>78</td><td>48</td></tr><tr><td>R104</td><td>10</td><td>93</td><td>31</td><td>67</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>R107</td><td>1</td><td>75</td><td>200</td><td>48</td></tr><tr><td>R107</td><td>6</td><td>93</td><td>178</td><td>112</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>RC104</td><td>8</td><td>75</td><td>92</td><td>114</td></tr><tr><td>RC104</td><td>6</td><td>93</td><td>199</td><td>83</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>RC108</td><td>2</td><td>75</td><td>118</td><td>90</td></tr><tr><td>RC108</td><td>5</td><td>93</td><td>216</td><td>83</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

3) “Average total degree of time violation”: In a solution to a DI disruption, the total degree of time violation will be calculated by formulas (9) and (10), in which the value of Δt is set to be $\Delta t _ { j } = l _ { j } - e _ { j } .$ . This criterion compares the average total degree of time violation of the 100 solutions achieved respectively by the two methods.

4) “Total rejected demands”: Limited by the capacity of a vehicle and the amount of vehicles, some of the increased demand cannot be satis<sup>fi</sup>ed in the current distribution period, which has to be rejected. This criterion compares the total rejected demands of the 100 solutions achieved respectively by the two methods.

5) “CPU seconds”: This criterion is only applied to PAM modeling approach. It records the running time of CPU for achieving a solution by PAM modeling approach, which is the time from generating facts by C++ and transferring them by pyswip to the dynamic fact-base of SWI-Prolog to outputting the <sup>fi</sup>nal result as Fig. 8 shows. Among the 100 CPU seconds for the 100 cases of a type of problem, MIN records the shortest one, and MAX records the longest one, while AVE records the average value of them. This criterion re<sup>fl</sup>ects if the PAM method can be employed in real time.

In Table 7, besides the results of these criteria, the improvement degree of PAM modeling approach than manual method is shown by the calculation of (M-PAM)/M for each criterion. For example, in problem C101, the average cost of the 100 solutions achieved by manual method is 103.83 while the average cost of the 100 solutions achieved by PAM method is 63.24, so the improvement degree of PAM method than manual method on this criterion is (103.83–63.24)/103.83= 39.09%. The remaining improvement degrees on the other three criteria can be analogically calculated. Table 7 indicates that the PAM modeling approach is much better than the manual method on the criteria 1)\~3) for all types of problems. Moreover, all of the maximum running times are less than 0.27 seconds and the average running times are less than 0.23 seconds, which means that PAM modeling approach can be employed in real time.

Moreover, as PAM modeling approach allows changing the objective and constraints in real time, it can obtain practical solutions to disruptions. However, the method, which uses the same optimization algorithms as PAM modeling approach does, but has no scheduling knowledge, will obtain impractical solutions, as the initial objective and constraints are not allowed to be relaxed. We name this method WSK (the abbreviation of “without scheduling knowledge”). Table 8 compared the two methods from the perspective of practice.

Table 7  
The comparison between the aggregation results of 100 DI cases obtained respectively by manual method and PAM modeling approach.

<table><tr><td>Problem type</td><td>Method</td><td>1) Average cost</td><td>2) Average amount of the affected customers</td><td>3) Average total degree of time violation</td><td>4) Total rejected demands</td><td>5) CPU(S)MIN/MAX/AVG</td></tr><tr><td rowspan="3">C101</td><td>M</td><td>103.83</td><td>2.44</td><td>41.03%</td><td>119</td><td>N/A</td></tr><tr><td>PAM</td><td>63.24</td><td>0.9</td><td>6.64%</td><td>119</td><td>0.1991/0.2504/0.2244</td></tr><tr><td>(M-PAM)/M</td><td>39.09%</td><td>63.11%</td><td>83.81%</td><td>0.00%</td><td></td></tr><tr><td rowspan="3">C104</td><td>M</td><td>99.09</td><td>3.3</td><td>89.02%</td><td>109</td><td>N/A</td></tr><tr><td>PAM</td><td>73.81</td><td>1.92</td><td>25.74%</td><td>109</td><td>0.1996/0.2488/0.2241</td></tr><tr><td>(M-PAM)/M</td><td>25.51%</td><td>41.82%</td><td>71.09%</td><td>0.00%</td><td></td></tr><tr><td rowspan="3">R104</td><td>M</td><td>82.85</td><td>1.37</td><td>34.14%</td><td>0</td><td>N/A</td></tr><tr><td>PAM</td><td>34.33</td><td>0.43</td><td>16.08%</td><td>0</td><td>0.2061/0.2488/0.2234</td></tr><tr><td>(M-PAM)/M</td><td>58.56%</td><td>68.61%</td><td>52.89%</td><td>N/A</td><td></td></tr><tr><td rowspan="3">R107</td><td>M</td><td>44.40</td><td>0.86</td><td>43.52%</td><td>105</td><td>N/A</td></tr><tr><td>PAM</td><td>35.06</td><td>0.26</td><td>0.96%</td><td>105</td><td></td></tr><tr><td>(M-PAM)/M</td><td>21.03%</td><td>69.77%</td><td>97.80%</td><td>0.00%</td><td>0.1994/0.2487/0.2249</td></tr><tr><td rowspan="3">RC104</td><td>M</td><td>103.16</td><td>1</td><td>8.82%</td><td>47</td><td>N/A</td></tr><tr><td>PAM</td><td>50.72</td><td>0.53</td><td>5.50%</td><td>47</td><td></td></tr><tr><td>(M-PAM)/M</td><td>50.84%</td><td>47.00%</td><td>37.63%</td><td>0.00%</td><td>0.1996/0.2630/0.2226</td></tr><tr><td rowspan="3">RC108</td><td>M</td><td>77.48</td><td>0.92</td><td>3.68%</td><td>100</td><td>N/A</td></tr><tr><td>PAM</td><td>61.17</td><td>0.62</td><td>2.35%</td><td>100</td><td></td></tr><tr><td>(M-PAM)/M</td><td>21.05%</td><td>32.61%</td><td>36.21%</td><td>0.00%</td><td>0.2003/0.2572/0.2240</td></tr></table>

In this table, “total increased demands of the 100 cases” stands for the summation of the increased demands of the 100 DI disruption cases of a type of problem. “Rejected demands” stands for the total demands rejected by the 100 solutions to the 100 DI disruptions. “Rejected rate”=rejected demands/total increased demands of the 100 cases×100%. For example, with respect to the problem type C101, the total increased demands of the 100 DI disruptions are 5567. The total demands rejected by the 100 solutions achieved by PAM method are 119 and the rejected rated is 2.14%, while the total demands rejected by the 100 solutions achieved by WSK are 4825 and the rejected rate is 86.67%. Table 8 illustrates that the solutions achieved by WSK method have high rejected demands and high rejected rate for all types of problems. That is because the method pursues optimal solutions that can satisfy the initial constraints of the problem, such as pursuing the least distance traveled, and complying with all customers' time windows. However, in order to get this kind of solutions, most increased demands have to be rejected, which will lead to the decline of customer satisfaction in the long run. Some customers may switch to the competitors of the distribution corporation due to the dissatisfaction, which will weaken the corporation. Contrastively, the solutions achieved by PAM modeling approach have very low rejected demands and rejected rate. By this modeling approach, customer satisfaction will be maintained in a high level, which is bene<sup>fi</sup>cial for enhancing customer loyalty to the corporation. In the long run, this is a great advantage for the distribution corporation.

The comparison of the rejected total increased demands and the rejected rate in the results obtained respectively by PAM method and WSK method.

<table><tr><td>Problem type</td><td>Total increased demands of the 100 cases</td><td>Method</td><td>Rejected demands</td><td>Rejected rate</td></tr><tr><td rowspan="2">C101</td><td rowspan="2">5567</td><td>PAM</td><td>119</td><td>2.14%</td></tr><tr><td>WSK</td><td>4825</td><td>86.67%</td></tr><tr><td rowspan="2">C104</td><td rowspan="2">5443</td><td>PAM</td><td>109</td><td>2.00%</td></tr><tr><td>WSK</td><td>5087</td><td>93.46%</td></tr><tr><td rowspan="2">R104</td><td rowspan="2">6070</td><td>PAM</td><td>0</td><td>0.00%</td></tr><tr><td>WSK</td><td>2813</td><td>46.34%</td></tr><tr><td rowspan="2">R107</td><td rowspan="2">6830</td><td>PAM</td><td>105</td><td>1.54%</td></tr><tr><td>WSK</td><td>1802</td><td>26.38%</td></tr><tr><td rowspan="2">RC104</td><td rowspan="2">5233</td><td>PAM</td><td>47</td><td>0.90%</td></tr><tr><td>WSK</td><td>2867</td><td>54.79%</td></tr><tr><td rowspan="2">RC108</td><td rowspan="2">5887</td><td>PAM</td><td>100</td><td>1.70%</td></tr><tr><td>WSK</td><td>3688</td><td>62.65%</td></tr></table>

## 6. Conclusions and further study

This research proposes a modeling approach named PAM to handling disruptions in real-time vehicle routing problems. From the theoretical perspective, the modeling approach combines the scheduling knowledge (i.e. disruption-handling policies) of experienced schedulers with the optimization knowledge concerning algorithms and models, which can exert the advantages of them and eliminate their disadvantages. This modeling approach overcomes the de<sup>fi</sup>ciencies of using manual method alone, which usually cannot obtain the high quality solutions. Further, it overcomes the hurdle of using the model-algorithm method alone, which usually cannot obtain practical solutions. It provides a new way for solving complicated decision-making problems in the area of operations management. From the practical perspective, the PAM modeling approach can handle disruptions in real time to support the decision-making process in vehicle routing problems. It allows the objective and constraints to be changed according to the practical principles acquired from experienced schedulers, which can get practical and effective solutions that are much better than those obtained by a purely manual method or by the optimization techniques without scheduling knowledge.

A limitation of the research is that as this system is initially devel oped for the aim of handling demand-increasing disruptions, only these rules in P-DI policy set have been checked for their completeness, consistency and performance by involving scheduling experts and OR experts. Other rules were developed roughly by ourselves and needs to be checked further. Another limitation is that only one disruption can be handled at a time by the current version of the modeling system. Even if more than one disruption may occur simultaneously in practice, they have to be processed one by one. Therefore, further research will focus on perfecting this modeling system, including checking rules in other rule sets to perfect the knowledge base and utilizing vehicle on-board computers to develop distributed GUIs to make the system handle more events simultaneously.

## Acknowledgments

This work has been partially supported by the grants from the National Natural Science Funds for Distinguished Young Scholar (no. 70725004), Natural Science Foundation of China (nos. 71201014,

70890080/83, 70801008), and the Fundamental Research Funds for the Central Universities (no. DUT11RC(3)41). The authors also gratefully acknowledge the helpful comments and suggestions from the reviewers, who have great contributions to the improvement of the presentation and the quality of the paper. Special thanks are given to Dr. Amy Z. Zeng from Worcester Polytechnic Institute (WPI), Worcester, Massachusetts, USA, and to Mr. Jason Lippard, who graduated from University of Northern Iowa in English Teaching major, USA, for their valuable advice and contribution during the revision of the paper.

## References

[1] N. Balakrishnan, Simple heuristics for the vehicle routing problem with soft time windows, Journal of the Operational Research Society 44 (1993) 279–287.

[2] J. Bisschop, AIMMS-Optimization Modeling, Paragon Decision Technology, 2007.

[3] J. Bisschop, R. Entriken, AIMMS the modeling system, Paragon Decision Technology, 1993.

[4] Z. Boufriche-Boufaida, A purely object-oriented approach for rule-based paradigms, Expert Systems with Applications 14 (1998) 483–492.

[5] O. Bräysy, M. Gendreau, Vehicle routing problem with time windows, Part II: metaheuristics, Transportation Science 39 (2005) 119–139.

[6] A. Brooke, D. Kendrick, A. Meeraus, GAMS-A User's Guide: Release 2.25, The Scienti<sup>fi</sup>c Press, 1992.

[7] H.I. Calvete, C. Galé, M.-J. Oliveros, B. Sánchez-Valverde, A goal programming approach to vehicle routing problems with soft time windows, European Journal of Operational Research 177 (2007) 1720–1733.

[8] W.-C. Chiang, R.A. Russell, A metaheuristic for the vehicle-routeing problem with soft time windows, Journal of the Operational Research Society 55 (2004) 1298–1310.

[9] M. Colombo, A. Grothey, J. Hogg, K. Woodsend, J. Gondzio, A structure-conveying modelling language for mathematical and stochastic programming, Mathematica Programming Computation 1 (2009) 223–247.

[10] J.-F. Cordeau, G. Desaulniers, J. Desrosiers, M.M. Solomon, F. Soumis, The VRP with time windows, in: P. Toth, D. Vigo (Eds.), The Vehicle Routing Problem, SIAM Monographs on Discrete Mathematics and Applications, SIAM Publishing, 2002, pp. 157–193.

[11] M.Y. Day, R.T.H. Tsai, C.L. Sung, C.C. Hsieh, C.W. Lee, S.H. Wu, K.P. Wu, C.S. Ong, W.L. Hsu, Reference metadata extraction using a hierarchical knowledge representation framework, Decision Support Systems 43 (2007) 152–167.

[12] M. Desrochers, C.V. Hones, J.K. Lenstra, M.W.P. Savelsbergh, L. Stougie, Towards a model and algorithm management system for vehicle routing and scheduling problems. Decision Support Systems 25 (1999) 109–133

[13] T.C. Du, E.Y. Li, D. Chou, Dynamic vehicle routing for online B2C delivery, Omega 33 (2005).33-45

[14] T. Du, F.K. Wang, P.Y. Lu, A real-time vehicle-dispatching system for consolidating milk runs, Transportation Research Part E: Logistics and Transportation Review 43 (2007) 565–577.

[15] A. Fay, A fuzzy knowledge-based system for railway traf<sup>fi</sup>c control, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 13 (2000) 719–729.

[16] B. Fleischmann, S. Gnutzmann, E. Sandvoß, Dynamic vehicle routing based on online traf<sup>fi</sup>c information, Transportation Science 38 (2004) 420–433.

[17] R. Fourer, D.M. Gay, B.W. Kernighan, A modeling language for mathematical programming, Management Science 36 (1990) 519–554.

[18] G.M. Giaglis, I. Minis, A. Tatarakis, V. Zeimpekis, Minimizing logistics risk through real-time vehicle routing and mobile technologies: research to date and future trends, International Journal of Physical Distribution and Logistics Management 34 (2004) 749–764.

[19] X. Hu, L. Sun, Knowledge-based modeling for disruption management in urban distribution, Expert Systems with Applications 39 (2012) 906–916.

[20] X.P. Hu, L.J. Sun, T.T. Hu, An approach to knowledge representation for vehicle routing problems, in: Proceedings of International Conference on Management Science & Engineering (13th) 1-3, 2006, pp. 487–492.

[21] X.P. Hu, M.F. Huang, A.Z. Zeng, An intelligent solution system for a vehicle routing problem in urban distribution, International Journal of Innovative Computing, Information and Control 3 (2007) 189–198.

[22] X.P. Hu, Y.X. Li, J.W. Guo, L.J. Sun, A.Z. Zeng, A simulation optimization algorithm with heuristic transformation and its application to vehicle routing problems, International Journal of Innovative Computing, Information and Control 4 (2008) 1169–1181.

[23] S. Ichoua, M. Gendreau, J.Y. Potvin, Diversion Issues in Real-Time Vehicle Dispatching, Transportation Science 34 (2000) 426–438

[24] G. Ioannou, M. Kritikos, G. Prastacos, A problem generator-solver heuristic for vehicle routing with soft time windows, Omega 31 (2003) 41–53.

[25] A. Larsen, O.B.G. Madsen, M.M. Solomon, Classi<sup>fi</sup>cation of dynamic vehicle routing systems, in: V. Zeimpekis, C.D. Tarantilis, G.M. Giaglis, I. Minis (Eds.), Dynamic Fleet Management: Concepts, Systems, Algorithms & Case Studies, Springer, Berlin Heidelberg, 2007, pp. 19–40.

[26] J.Q. Li, D. Borenstein, P.B. Mirchandani, A decision support system for the single-depot vehicle rescheduling problem, Computers and Operations Research 34 (2007) 1008–1032.

[27] J.Q. Li, P.B. Mirchandani, D. Borenstein, A Lagrangian heuristic for the real-time vehicle rescheduling problem, Transportation Research Part E: Logistics and Transportation Review 45 (2009) 419–433.

[28] J.Q. Li, P.B. Mirchandani, D. Borenstein, Real-time vehicle rerouting problems with time windows, European Journal of Operational Research 194 (2009) 711–727.

[29] A. Ligęza, Logical support for design of rule-based systems. reliability and quality issues. Available at http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1. 53.2007&rep=rep1&type=pdf Jun. 7 2012.

[30] S. Lin, B.W. Kernighan, An effective heuristic algorithm for the traveling-salesman problem, Operations Research 21 (1973) 498–516.

[31] J. Llorens, J. Morato, G. Genova, RSHP: an information representation model based on relationships, in: E. Damiani, L.C. Jain, M. Madravio (Eds.), Soft Computing in Software Engineering, Springer, Berlin Heidelberg, 2004, pp. 221–250.

[32] J. Ma, An object-oriented framework for model management, Decision Support Systems 13 (1995) 133–139.

[33] W.A. Muhanna, An object-oriented framework for model management and DSS development, Decision Support Systems 9 (1993) 217–229.

[34] J. Mylopoulos, An overview of knowledge representation, Proceedings of the workshop on Data abstraction, databases and conceptual modeling 11 (1981) 5–12

[35] B.R. Nault, V.C. Storey, Using object concepts to match arti<sup>fi</sup>cial intelligence techniques to problem types, Information Management 34 (1998) 19–31.

[36] S.J. Noronha, V.V.S. Sarma, Knowledge-based approaches for scheduling problems: a survey, IEEE Transactions on Knowledge and Data Engineering 3 (1991) 160–171.

[37] S.N. Pillutla, B.N. Nag, Object-oriented model construction in production scheduling decisions, Decision Support Systems 18 (1996) 357–375.

[38] J.Y. Potvin, Y. Xu, I. Benyahia, Vehicle routing and scheduling with dynamic travel times, Computers and Operations Research 33 (2006) 1129–1137.

[39] D.J. Power, Specifying an expanded framework for classifying and describing decision support systems, Communications of the Association for Information Systems 13 (2004) 158–166

[40] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (2007) 1044–1061.

[41] R. Séguin, J.-Y. Potvin, M. Gendreau, T.G. Crainic, P. Marcotte, Real-time decision problems: an operational research perspective, The Journal of the Operational Research Society 48 (1997) 162-174

[42] L.J. Sun, X.P. Hu, Y. Fang, M.F. Huang, Knowledge representation for disruption management problems in urban distribution systems, International Journal of Innovative Computing, Information and Control 6 (2010) 4145–4156.

[43] É. Taillard, P. Badeau, M. Gendreau, F. Guertin, J.-Y. Potvin, A Tabu search heuristic for the vehicle routing problem with soft time windows, Transportation Science 31 (1997) 170–186.

[44] J. Yang, P. Jaillet, H. Mahmassani, Real-time multivehicle truckload pickup and delivery problems, Transportation Science 38 (2004) 135–148.

[45] V. Zeimpekis, G.M. Giaglis, A dynamic real-time vehicle routing system for distribution operations, in: G.J. Doukidis, A.P. Vrechopoulos (Eds.), Consumer Driven Electronic Transformation, Springer, Berlin Heidelberg, 2005, pp. 23–37.

[46] V. Zeimpekis, G.M. Giaglis, Urban dynamic real-time distribution services: Insights from SMEs, Journal of Enterprise Information Management 19 (2006) 367-388.

[47] V. Zeimpekis, G.M. Giaglis, I. Minis, A dynamic real-time <sup>fl</sup>eet management system for incident handling in city logistics, Vehicular Technology Conference 5 (2005) 2900–2904.

Dr. Xiangpei Hu is a Professor of Management Science and Engineering at Dalian University of Technology, Dalian, China. He received his Ph.D. of Management Science and Engineering, M.S. of Information Management, and B.S. of Management Science and Engineering from Harbin Institute of Technology, Harbin, China. His current research interests include Decision Support Systems, Service Science, and Operations Research. His work has been published in Computer and Operations Research, Engineering Optimization, International Journal of Knowledge and Systems Science, and Intelligent Information Management Systems and Technologies.

Dr. Lijun Sun is a postdoc in Institute of Systems Engineering at Dalian University of Technology, China. She received her Ph.D. of Management Science and Engineering, and M.S. of Systems Engineering from Dalian University of Technology, and her B.S. of Business Management from China University of Petroleum. Her current research interests include Decision Support Systems, Knowledge Engineering and Management, and Service Science. Her work has been published in Expert Systems with Applications, International Journal of Knowledge and Systems Science, Intelligent Information Management Systems and Technologies, and International Journal of Innovative Computing Information and Control.

Mr. Linlin Liu is a doctoral student of Management Science and Engineering in Institute of Systems Engineering at Dalian University of Technology, Dalian, China. He received his B.S. of Software Engineering from Dalian University of Technology. His current research focus is Distribution and Logistics Management.
