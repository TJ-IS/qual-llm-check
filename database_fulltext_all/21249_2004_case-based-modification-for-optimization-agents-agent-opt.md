---
otero_id: 21249
otero_key: "3HC6KGH2"
title: "Case-based modification for optimization agents: AGENT-OPT"
authors: "Yong Sik Chang; Jae Kyu Lee"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00026-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Case-based modification for optimization agents: AGENT-OPT

Yong Sik Chang<sup>a</sup>, Jae Kyu Lee<sup>b,</sup>\*

<sup>a</sup> International Center for Electronic Commerce, 207-43, Cheongryang, Seoul 130-012, South Korea

<sup>b</sup>Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-43, Cheongryang, Seoul 130-012, South Korea

## Abstract

For the effective implementation of an inter-organizational supply chain on the Web, many optimization model agents need to be embedded in the distributed software agents. For instance, many suppliers make requests to a delivery scheduler who manages a model warehouse at the e-hub. The scheduler deals with the scheduling of many truckers and each trucker’s agent must have its own routing optimization models. Since the formulations in the model warehouse vary depending upon the requirements, it is impossible to formulate all combinations in advance. Therefore, we need a case-based model modification scheme that can generate the required formulation from the semantically specified requirement in the agent communication language.

This research deals with the issues of the architecture of an optimization model agent system AGENT-OPT, modeling request language in XML, optimization model representation in semantic-level objects using UNIK-OPT, a method of selecting a base model, an optimization model modification language (OMML), and rule-based modification reasoning. The approach is applied to the delivery scheduling to study the effect of base model selection policies on the modification effort. To determine whether to start with a primitive model, full model, or the most similar model, we experimented with the sensitivity of proximity to the primitive model on 24 cases and discovered the threshold for choosing the most efficient base model. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Agent; Case-based model formulation; Optimization; Delivery scheduling; Supply chain

## 1. Introduction

For the effective implementation of an inter-organizational supply chain on the Web, many optimization models need to be embedded in distributed software agents. For instance, when there are many suppliers that need delivery from a group of truckers, we need a third party to schedule the optimal delivery for truckers and suppliers. Since each delivery may have different requirements, the predefined models may not be able to cover the variety of modeling requests from the suppliers. Consequently, the third party delivery scheduler needs to maintain a model warehouse [6] with the capability to formulate the optimization model based on the modeling request specified in XML messages, see Fig. 1.

Since it is reasonable to assume that the scheduler has some predefined models, we can apply the casebased modification approach for the formulation of models. Our primary concern here is how to automate the modification process effectively and efficiently. To automate the formulation process, we need to resolve the following issues.

![](/api/attachments/3HC6KGH2/fulltext/images/a4fe801049b65161343b7650f2df81b1733825dbe66d0f4c052418dc8bb1ccd7.jpg)  
Fig. 1. Scenario of optimization agent and model warehouse for delivery scheduling.

1. Design of an appropriate architecture for the optimization agent

2. Representation of the optimization models so that they can incorporate the modeling request and perform modification accordingly

3. Selection of a base model to start the modification

4. Design of an optimization model modification language (OMML)

5. Design of a standard modeling request language in XML

6. Interpretation of the modeling request language to the base model selection and its modification

7. Rule-based reasoning for the modification

To fulfill the goals, we perform the following research.

1. Design the AGENT-OPT as an architecture for the optimization agent. This architecture needs to specify the modeling request messages and the internal architecture of agents.

2. Adopt the UNIK-OPT to represent the linear programming and integer programming (IP) models in the structured objects [20,24]. The illustrative application domain is the delivery scheduling.

3. Adopt modification commands that add and delete the objects of constraints, blocks of terms, variables, constants, and indices in UNIK-OPT.

4. Evaluate the performance of the three approaches for the selection of a base model: the primitive model, full model, and most similar model approaches. The base model implies an existing model selected for the modification. The primitive model is a model that has only the mandatory constraints and the full model is the one with all possible requested constraints. The most similar model is the most similar case among the existing models to the modeling request.

5. Specify the modeling request language for the delivery order in XML message form. The messages are transformed to the factors of the base model selection and model modification. For the delivery scheduling, there are two types of messages: delivery order and resource specification.

6. Specify the rules for the model modification. The restrictions between objects for the valid model should also be identified. The rules and restrictions are used to execute the modification.

The following sections describe the above issues. Section 2 reviews the literature on case-based model modification. Section 3 presents the optimization model for automatic modification and Section 4 describes the modification commands. Section 5 describes the modification process beginning with a primitive model and Section 6 contrasts the full model and the most similar model approaches to the primitive model approach. Section 7 analyzes the conditions when an approach is most efficient. Section 8 describes the architecture of AGENT-OPT that adopts the proposed approaches.

## 2. Literature on case-based model formulations

There is a considerable amount of research on model management systems (MMS) [5,11] that supports the various phases of the modeling life-cycle. The importance of MMS is resurrected as the necessity for a model warehouse arises in the Web-based hub [6]. Earlier research studied the representations of models and the reasoning methods in order to map specific problems with the model structure.

From the perspective of data and object management, network data modeling [18], relational data modeling [3], entity-relationship data modeling [4], and object-oriented data modeling [14,21,30,35] approaches were attempted. Liang proposed a framework that included both relational and network concepts [31]. On the other hand, from the perspective of Artificial Intelligence, researchers adopted knowledge representation techniques to represent models and focused on automating the modeling processes. These representations are based on predicate calculus [7], semantic information net [11], knowledge abstraction [9], first order logic [10,19], structured modeling [12,13,36,38], rule-based formulation [23,28], and frame [2,20,22,24].

It is very difficult to formulate a model from scratch. It is reasonable, therefore, to modify the existing models on the case-based reasoning approach. Case-based planning was proposed by Vellore et al. [39]. Modeling by analogy was researched by Blanning [3], Ishikawa and Terano [15], Kedar-Cabelli [16], Liang [32], Liang and Konsynski [34], and Winston [40]. Both analogical and case-based reasoning methods rely on encapsulating episodic knowledge to guide complex problem solving. The former emphasizes the process of modification, adaptation and derivation, whereas the latter emphasizes the organization, hierarchy indexing and retrieval of case memory [8]. Modeling by analogy builds a new model through feature mapping on conceptual, structural, and functional similarities. However, it is not efficient when modification of the model structure is required. As Liang pointed out, this approach is relatively rigid and the computational cost may be excessive particularly when large-scaled, because feature mapping is theoretically NP-complete [33]. Instead of mapping a new problem to the stored model counterpart, Binbasioglu [1] proposed the process analogy approach. This approach designs a model without model structure modification from reusable model pieces. Nevertheless, it is rare for stored models to be reused without structural modification.

Therefore, we need a more flexible and efficient method that will automatically modify the models. In this study, we adopt UNIK-OPT [24], which represents the optimization models—both the linear and integer programming models—in structured objects. Since the underlying design principle of UNIfied Knowledge (UNIK) was the representation of optimization models so as to integrate with rules [27], its object-oriented representation is suitable for modification. The earlier version UNIK-LP, which focused on the linear programming, did not assist the eXclusive OR (XOR) relationship of variables and the IF –THEN relationships between constraints. These higher-level representations mean it should be extended to integer programming models, thus the system UNIK-IP [41] was developed. UNIK-RELAX [17] was also developed to identify the characteristics of model structure and to plan the Lagrangian relaxation procedure to solve IP models.

## 3. Representation of optimization model formulation in objects

To apply the CBR approach to the optimization model formulation, we need to represent the model cases in such a way that they semantically understand the modeling requests and modification commands. UNIK-LP [24], a subsystem of UNIK-OPT for linear programming, represents the model in objects semantically (see Fig. 2) and transforms them to mathematical notations and tabular form for solving. As a result, UNIK-OPT is suitable for representing the CBR approach.

The linear programming models can be extended to IP by adopting the expressions like XOR and IF – THEN relationships between variables and between constraints. UNIK-IP [41], the extension of UNIK-LP for integer programming, can express such relationships and transform them to valid integer programming model formulations for IP solvers.

![](/api/attachments/3HC6KGH2/fulltext/images/1afc1a5943fe244d69cc1fd1865d29832eca596017826e71277543abf7091a2f.jpg)  
Fig. 2. Structure of linear programming model by UNIK-OPT.

The multi-depot vehicle routing problem (M-VRP) [20] with time windows in Eqs. (1) – (11) can be expressed in UNIK-OPT as Fig. 3. The top-level object M-VRP specifies the model with the attributes of DIRECTION of Minimization, a block of terms total traveling distance BOT in the OBJECTIVE, and nine CONSTRAINTs. The CONSTRAINT drop<sub></sub>in<sub></sub>constraint in Eq. (2) is composed of the OPERATOR of Equal, the block of terms drop in BOT on the left-hand side (LHS) of the equality operator and one<sub></sub>BOT on the right-hand side (RHS). The index of the constraint is flow<sub></sub>in<sub></sub>index with the range of $[ 1 , \ldots , n ]$ . The IF–THEN constraint in Eq. (9) is expressed as a pair of constraints.

$$
\text { Min } \sum_ {i = 1} ^ {n + m} \sum_ {j = 1} ^ {n + m} \sum_ {k = 1} ^ {v} d _ {i j} X _ {i j k}\tag{1}
$$

subject to

$$
\sum_ {i = 1} ^ {n + m} \sum_ {k = 1} ^ {v} X _ {i j k} = 1 \quad \text {   for   } j = 1, 2, \dots , n\tag{2}
$$

$$
\sum_ {j = 1} ^ {n + m} \sum_ {k = 1} ^ {v} X _ {i j k} = 1 \quad \text {   for   } i = 1, 2, \dots , n\tag{3}
$$

$$
\sum_ {i = 1} ^ {n + m} X _ {i h k} - \sum_ {j = 1} ^ {n + m} X _ {h j k} = 0 \quad \text {   for   } h = 1, 2, \dots , n + m,\tag{4}
$$

$$
\sum_ {i = 1} ^ {n + m} q _ {i} \sum_ {j = 1} ^ {n + m} X _ {i j k} \leq p _ {k} \quad \text {   for   } k = 1, 2, \dots , v\tag{5}
$$

$$
\sum_ {i = n + 1} ^ {n + m} \sum_ {j = 1} ^ {n} X _ {i j k} \leq 1 \quad \text {   for   } k = 1, 2, \dots , v\tag{6}
$$

$$
\sum_ {j = n + 1} ^ {n + m} \sum_ {i = 1} ^ {n} X _ {i j k} \leq 1 \quad \text {   for   } k = 1, 2, \dots , v\tag{7}
$$

$$
\begin{array}{l} Y _ {i} - Y _ {j} + (m + n) X _ {i j k} \leq n + m - 1 \text { for } 1 \leq i \neq j \leq n \\ \text { and } 1 \leq k \leq v \end{array}\tag{8}
$$

$$
\begin{array}{l} \text {   If   } X _ {i j k} \geq 1, \text {   then   } T _ {i} + t _ {i j} \leq T _ {j} \quad \text {   for   } i = 1, 2, \dots , n, \\ j = 1, 2, \dots , n, k = 1, 2, \dots , v \end{array}\tag{9}
$$

$$
\mathrm{et} _ {i} \leq T _ {i} \leq \mathrm{lt} _ {i} \quad \text { for } i = 1, 2, \dots , n\tag{10}
$$

$$
X _ {i j k} = 0 \text {   or   } 1 \text {   for   all   } i, j, k\tag{11}
$$

where $i , j ,$ h: index of delivery points and depots $\{ 1 , 2 , . . . , n ^ { + } m \}$ ; k: index of vehicles $\{ 1 , 2 , . . . , \nu \}$ ; n: number of delivery points; $m \colon$ number of depots; v: number of vehicles; $d _ { i j } .$ traveling distance between delivery points/depots i and $j ; q _ { i } \mathrm { : }$ demand at delivery point $i ; \ p _ { k } \colon$ capacity of vehicle $k ; ~ t _ { k } \colon$ maximum traveling time allowed for a route of vehicle $k ; ~ t _ { i j } . \mathrm { : }$ traveling time between delivery points i and $j ;$ et<sub>i</sub>: earliest delivery time at delivery point i; $\operatorname { l t } _ { i \colon }$ latest delivery time at delivery point $i ; X _ { i j k } ; 1$ if pair $i , j$ is in the route of vehicle k and 0 otherwise; $T _ { i \cdot }$ arrival time at delivery point $i ; Y _ { i } .$ real number that breaks subtours.

UNIK-OPT generates the formulation by interacting with human model builders. Once the semantic formulation in Fig. 3 is generated, UNIK-OPT can automatically transform it to the mathematical notation forms in Eqs. (1) – (11).

![](/api/attachments/3HC6KGH2/fulltext/images/c31a3036adf48ae8e72fe32447ca260c3385477fb04bdacef474f107b9990d82.jpg)  
Fig. 3. Multi-depot VRP model expressed in UNIK-OPT.

## 4. Modification language of optimization models

The optimization models represented in UNIK-OPT need elementary commands to modify them. Lee and Lee [25] have developed an OMML for UNIK-OPT. Primitive commands for OMML are ADD and DELETE for all sorts of objects, as illustrated in Table 1. UPDATE is a hybrid command that is composed of DELETE and ADD.

The effort to perform each modification command $L _ { i } ,$ denoted by $E ( L _ { i } )$ , is estimated by the number of related objects as listed in the far right column of Table 1. The command for higher-level objects naturally requires greater effort because it is associated with many lower level objects. We have assumed that the effort required for the ADD and DELETE operations are the same.

To execute the commands in practice, the ADDed objects must ascertain if they are redundant or not, and the ADDed/DELETEd objects must ascertain whether they require other objects to validate the model.

## 5. Modification with a primitive model

Now, we need to modify an optimization model (called a base model) with the modification commands explained in Section 4. We will consider three approaches to select a base model: the primitive model, full model, and most similar model approaches. This section describes the primitive model approach. The other two approaches will be explained and contrasted in the following sections.

## 5.1. Factors for primitive model selection and modification

The primitive model is a model that consists of only the necessary constraints for a problem domain. Thus, by nature, the primitive models are not substitutional each other. Suppose we have three primitive models for the problem of delivery scheduling as listed in Table 2. Factors for the selection of the primitive model are the ‘relationship between depot and visit’ and the ‘purpose of visit.’ One of the primitive models can be selected as a base model. Suppose we have selected the M-VRP as a base model.

To formulate a model, we can modify a base model according to the modification factors listed in Table 3. In this example, the entities relevant to the modification are the constraints on the vehicle, delivery time, penalty for tardiness, and sequences in routing. There are 13 factors in this example. A full model implies a model constructed of a primitive model with all of the modification factors as constraints.

Illustrative commands of optimization model modification language  
Table 3  
Modification factors in delivery scheduling

<table><tr><td>ID</td><td>Commands of OMML</td><td> $E(L_{j})$ </td></tr><tr><td> $L_{1}$ </td><td>ADD_BOT BOT_name TO OBJECTIVE_FUNCTION</td><td>6</td></tr><tr><td> $L_{2}$ </td><td>DELETE_BOT BOT_name FROM OBJECTIVE_FUNCTION</td><td>6</td></tr><tr><td> $L_{3}$ </td><td>ADD_CONSTRAINT Constraint_name</td><td>8</td></tr><tr><td> $L_{4}$ </td><td>DELETE_CONSTRAINT Constraint_name</td><td>8</td></tr><tr><td> $L_{5}$ </td><td>ADD_CONSTRAINT IF Constraint_name THEN Constraint_name</td><td>15</td></tr><tr><td> $L_{6}$ </td><td>DELETE_CONSTRAINT IF Constraint_name THEN Constraint_name</td><td>15</td></tr><tr><td> $L_{7}$ </td><td>ADD_BOT BOT_name IN {LHS|RHS} OF CONSTRAINT Constraint_name</td><td>6</td></tr><tr><td> $L_{8}$ </td><td>DELETE_BOT BOT_name IN {LHS|RHS} OF CONSTRAINT Constraint_name</td><td>6</td></tr><tr><td> $L_{9}$ </td><td>ADD_INDEX{{Index_name Range}|{Consecutive_index_names Range}}TO CONSTRAINT Constraint_name</td><td>2</td></tr><tr><td> $L_{10}$ </td><td>DELETE_INDEX Index_name Range TO CONSTRAINT Constraint_name</td><td>2</td></tr><tr><td> $L_{11}$ </td><td>ADD_INDEX Index_name Range TO BOT BOT_name</td><td>2</td></tr><tr><td> $L_{12}$ </td><td>DELETE_INDEX Index_name Range TO BOT BOT_name</td><td>2</td></tr></table>

Factors for identifying primitive models in delivery scheduling domain

<table><tr><td>Categories</td><td>Factors</td><td></td><td>Candidates of primitive model</td></tr><tr><td rowspan="2">Relationship between depot and visit</td><td>1:m_relationship</td><td> $P_{1}$ </td><td>M-VRP, multi-depot pickup and delivery (M-PDP)</td></tr><tr><td>m:n_relationship</td><td> $P_{2}$ </td><td>transportation problem</td></tr><tr><td rowspan="2">Purpose of visit</td><td>delivery_only</td><td> $P_{3}$ </td><td>M-VRP, transportation problem</td></tr><tr><td>pickup_and_delivery</td><td> $P_{4}$ </td><td>M-PDP</td></tr></table>

<table><tr><td>Entities</td><td>Factors</td><td></td><td>Required constraints</td></tr><tr><td rowspan="8">Vehicle</td><td>maximum_</td><td> $M_{1}$ </td><td rowspan="2">maximum time each vehicle travels in a route</td></tr><tr><td>traveling_time</td><td></td></tr><tr><td>maximum_</td><td> $M_{2}$ </td><td rowspan="2">maximum distance each vehicle travels in a route</td></tr><tr><td>traveling_distance</td><td></td></tr><tr><td>maximum_number_</td><td> $M_{3}$ </td><td rowspan="2">maximum number of visiting points for each vehicle</td></tr><tr><td>of visiting_points</td><td></td></tr><tr><td>fixed_cost_of_</td><td> $M_{4}$ </td><td rowspan="2">fixed cost to utilize a vehicle</td></tr><tr><td>utilizing_vehicles</td><td></td></tr><tr><td rowspan="4">Time</td><td>delivery_time_ window</td><td> $M_{5}$ </td><td>delivery time window during which a vehicle has to arrive</td></tr><tr><td>depot_departure_ time_window</td><td> $M_{6}$ </td><td>time window during which a vehicle has to depart a depot</td></tr><tr><td>depot_return_ time_window</td><td> $M_{7}$ </td><td>time window during which a vehicle has to return to the depot</td></tr><tr><td>service_time</td><td> $M_{8}$ </td><td>service time for a vehicle at a delivery point</td></tr><tr><td rowspan="2">Penalty</td><td>penalty_for_tardy_ arrival_time</td><td> $M_{9}$ </td><td>penalty for a vehicle&#x27;s tardy arrival</td></tr><tr><td>penalty_for_ exceeded_routing_ duration</td><td> $M_{10}$ </td><td>penalty for an exceeded routing duration time for a vehicle</td></tr><tr><td rowspan="3">Route</td><td>first_visit</td><td> $M_{11}$ </td><td>requirement to visit a point first in a route</td></tr><tr><td>last_visit</td><td> $M_{12}$ </td><td>requirement to visit a point last in a route</td></tr><tr><td>precedence</td><td> $M_{13}$ </td><td>traveling order between consecutive visiting points</td></tr></table>

## 5.2. Actions and rules for modification in delivery scheduling

We need to associate the factors with actions to construct modification rules. The ADD modification actions are described in Table 4 and are activated by the modification factors listed in Table 3. The constructed modification rules are the following and the AND/OR graph derived by the rules are depicted in Fig. 4.

$$
\begin{array}{l} \text { Rule   i:   IF   M_{i} , THEN   A_{i} for i = 1,2,3,4,5,11,12,} \\ 1 3; \end{array}
$$

$$
\text { Rule   } j \text {: IF } M _ {j} \cap A _ {5}, \text { THEN } A _ {j} \text { for } j = 6, 7, 8, 9;
$$

$$
\text { Rule   10:   IF   } M _ {1 0} \cap A _ {6} \cap A _ {7}, \text {   THEN   } A _ {1 0}.
$$

The actions can be expressed by the combination of OMML commands as specified in Table 5. Note the

Modification actions in mathematical programming notational form

<table><tr><td colspan="2">Modification actions</td><td>Mathematical expressions</td></tr><tr><td>ADD_maximum_traveling_time_constraint</td><td> $A_1$ </td><td>Add Eq. (12) to M-VRP. $\sum_{i=1}^{n+m} \sum_{j=1}^{n+m} t_{ij} X_{ijk} \leq t_k$  for  $k = 1,2,\ldots,v$  (12)</td></tr><tr><td>ADD_maximum_traveling_distance_constraint</td><td> $A_2$ </td><td>where  $t_k$ : maximum traveling time allowed for a route of vehicle  $k$ .Add Eq. (13) to M-VRP. $\sum_{i=1}^{n+m} \sum_{j=1}^{n+m} d_{ij} X_{ijk} \leq l_k$  for  $k = 1,2,\ldots,v$  (13)</td></tr><tr><td>ADD_maximum_number_of_visiting_points_constraint</td><td> $A_3$ </td><td>where  $l_k$ : maximum traveling distance allowed for a route of vehicle  $k$ .Add Eq. (14) to M-VRP. $\sum_{i=1}^{n} \sum_{j=1}^{n} X_{ijk} \leq u_k$  for  $k = 1,2,\ldots,v$  (14)</td></tr><tr><td>ADD_fixed_cost_of_utilizing_vehicle_BOT</td><td> $A_4$ </td><td>where  $u_k$ : maximum number of visiting points allowed for a vehicle  $k$ .Add Eq. (15) to objective function of M-VRP. $\sum_{i=1}^{n+m} \sum_{j=1}^{n} \sum_{k=1}^{v} f_k X_{ijk}$  (15)</td></tr><tr><td>ADD_delivery_time_window_constraint</td><td> $A_5$ </td><td>where  $f_k$ : fixed cost of utilizing vehicle  $k$ .Add Eqs. (16) and (17) to M-VRP.If  $X_{ijk} \geq 1$ , then  $T_i + t_{ij} \leq T_j$  for  $i = 1,2,\ldots,n$ , $j = 1,2,\ldots,n$ ,  $k = 1,2,\ldots,v$  (16) $et_i \leq T_i \leq lt_i$  for  $i = 1,2,\ldots,n$  (17)</td></tr><tr><td>ADD_depot_departure_time_window_constraint</td><td> $A_6$ </td><td>where  $et(lt)$ : earliest(latest) delivery time allowed at visit  $i$  and  $T_i$ : time variable at visit  $i$ .Add Eqs. (18) and (19) to M-VRP.If  $X_{ijk} \geq 1$ , then  $T_{ik}^{depart} + t_{ij} \leq T_j$  for  $i = n+1,\ldots,n+m$ , $j = 1,2,\ldots,n$ ,  $k = 1,2,\ldots,v$  (18) $et_i^{depart} \leq T_{ik}^{depart} \leq lt_i^{depart}$  for  $i = n+1,\ldots,n+m$ ,  $k = 1,2,\ldots,v$  (19)where  $T_{ik}^{depart}$ : time at which a vehicle  $k$  departs a depot  $i$ . $A_6$  is meaningful after  $A_5$  is actuated.</td></tr><tr><td>ADD_depot_return_time_window_constraint</td><td> $A_7$ </td><td>Add Eqs. (20) and (21) to M-VRP.If  $X_{ijk} \geq 1$ , then  $T_i + t_{ij} \leq T_{jk}^{return}$  for  $i = 1,2,\ldots,n$ , $j = n+1,\ldots,n+m$ ,  $k = 1,2,\ldots,v$  (20) $et_i^{return} \leq T_{ik}^{return} \leq lt_i^{return}$  for  $i = n+1,\ldots,n+m$ ,  $k = 1,2,\ldots,v$  (21)where  $T_{ik}^{return}$ : time at which a vehicle  $k$  returns to depot  $i$ . $A_7$  is meaningful after  $A_5$  is actuated.</td></tr><tr><td>ADD_service_time_BOT</td><td> $A_8$ </td><td>Add Eq. (22) to the left-hand side of consequence part of Eq. (20) $s_i$  (22)</td></tr><tr><td>ADD_penalty_for_tardy_arrival_time_BOT</td><td> $A_9$ </td><td>where  $s_i$ : service time at delivery point  $i$ .  $A_8$  is meaningful after  $A_5$  is actuated.Add Eq. (23) to the objective function of M-VRP. $\sum_{i=1}^{n} a(T_i - lt_i)$  (23)where  $a$  is a constant.  $A_9$  is meaningful after  $A_5$  is actuated.</td></tr></table>

(continued on next page)

Table 4 (continued)

<table><tr><td>Modification actions</td><td></td><td>Mathematical expressions</td></tr><tr><td>ADD_penalty_for_exceeded_routing_duration_BOT</td><td> $A_{10}$ </td><td>Add Eq. (24) to the objective function of M-VRP. $\sum_{i=n+1}^{n+m}\sum_{k=1}^{v}b(T_{ik}^{\text{return}} - T_{ik}^{\text{depart}})$  (24)</td></tr><tr><td>ADD_first_visit_constraint</td><td> $A_{11}$ </td><td>where b is a constant.  $A_{10}$  is meaningful after  $A_6$  and  $A_7$  are actuated.Add Eq. (25) to M-VRP. $\sum_{i=n+1}^{n+m}\sum_{k=1}^{v}X_{ijk}=1 \quad \text{for } j\in F$  (25)</td></tr><tr><td>ADD_last_visit_constraint</td><td> $A_{12}$ </td><td>where an element of the set F is a point required to visit first in a route.Add Eq. (26) to M-VRP. $\sum_{j=n+1}^{n+m}\sum_{k=1}^{v}X_{ijk}=1 \quad \text{for } i\in L$  (26)</td></tr><tr><td>ADD_precedence_constraint</td><td> $A_{13}$ </td><td>where an element of the set L is a point required to visit last in a route.Add Eq. (27) to objective function of M-VRP. $X_{ijk}=1 \quad \text{for } (i,j)\in P$  (27)where P is a set of consecutive visiting points with precedence constraints.</td></tr></table>

estimated modification effort $E ( A _ { i } )$ , which is the sum of associated $E ( L _ { j } )$ , marked in Table 5. The primitive model layer, modification action layer, and specific model layer are depicted in Fig. 4.

The total number of valid models that can be generated by the modifications is the number of possible combinations of modification actions that do not violate the restrictions between actions. In the M-VRP, the primitive model can be modified to 2,418 models.

Suppose three modification factors (maximum traveling distance, delivery time windows, and service time) are selected as marked in Fig. 4. The formulated models can be stored and used for future case-based modifications.

## 6. The full model and most similar model approaches

This section describes the next two approaches: the full model and most similar model approaches. The primitive model approach only adds constraints (and associated objects). On the contrary, the full model approach performs the deletion of constraints and the most similar model approach may add and/or delete the constraints. If there are conflicting constraints that cannot coexist, we need to generate more than one full model. This can be a detriment to the full model approach because we have to prepare all combinations of full models in advance and select one as a base model. Fortunately, however, in this example, all modification factors can coexist because one full model can generate the entire spectrum of models.

In essence, we can apply the forward chaining approach [33] from the base model. In addition, the reasoning process must check the following restrictions:

1. Avoidance of redundancy: If the same objects already exist, do not add them again.

2. Avoidance of conflict: If some constraints cannot coexist, alert the model builder the conflict so that he or she will reconsider the modeling factors.

3. Assurance of completeness: If a model has missing constraints, BOTs, attributes, or indices, generate the missing objects to complete and validate the model [25].

Let us denote the model and actions as follows.

GM: goal model

PM: primitive model

FM: full model

![](/api/attachments/3HC6KGH2/fulltext/images/eaa490e179f32ad006ff3acd4f96c879991c7c8821ea4e07a7e3445d7274fcef.jpg)  
Fig. 4. AND/OR graphical relationship between primitive models, factors, actions, and formulated model.

SM: a similar case model $A { = } \{ A _ { i } \}$ : a set of actions

## 6.1. Primitive model approach

According to the primitive model approach, the example model M-VRP with three factors $M _ { 2 } , \ M _ { 5 } ,$ and $M _ { 8 }$ can be expressed as ${ \mathrm { G M } } { = } ( \mathrm { M } { \mathrm { - } } \mathrm { V R P } ; ~ A _ { 2 } , ~ A _ { 5 } ,$ $A _ { 8 } )$ . In UNIK-OPT, the model is specified as Fig. 5.

The two factors $M _ { 2 }$ and $M _ { 5 }$ activate $A _ { 2 }$ and $A _ { 5 } ,$ respectively, and $M _ { 8 }$ and $A _ { 5 }$ activate $A _ { 8 } .$ The modification has added two constraints and a BOT. The primitive model and the three activated modifications result in the goal model. In this case, the estimated modification effort is 63. Intuitively, the primitive model approach is effective when the goal model is similar to the primitive model.

## 6.2. Full model approach

The full model approach must identify the DELETE actions to be undertaken. The DELETE actions $( \sim A _ { i } )$

are defined as the reverse of ADD actions $( A _ { i } )$ . The DELETE action set can be derived by eliminating the ADDed actions in the primitive model approach.

fDELETE actions by the full model approachg ¼ fall actionsg  fADD actions by the primitive model approachg

Obviously, the full model approach is effective when the goal model is close to the full model. In this example, $\mathrm { G M = ( P M ; } A _ { 2 } , A _ { 5 } , A _ { 8 } ) { = } ( \mathrm { F M } ; \mathbf { \alpha } \sim A _ { 1 }$ ${ \sim } A _ { 3 } , \ { \sim } A _ { 4 } , \ { \sim } A _ { 6 } , \ { \sim } A _ { 7 } , \ { \sim } A _ { 9 } , \ { \sim } A _ { 1 0 } , \ { \sim } A _ { 1 1 } , \ { \sim } A _ { 1 2 } ,$ $\sim A _ { 1 3 } )$ and takes the estimated modification effort 182. This means the primitive model approach is more efficient in this example.

## 6.3. The most similar model approach

The modification from a similar model may require both ADD and DELETE actions. To avoid the deletion and addition of overlapped actions, the intersection of both types of actions are first identified. In this manner, purely ADD and DELETE actions are undertaken. To experiment with the most similar model approach, the other 23 models are used as candidates for the base model. Suppose SM=(M-VRP; $A _ { 3 } , \ A _ { 5 } , \ A _ { 8 } )$ . In this example, we are required to ADD $A _ { 2 }$ and DELETE $A _ { 3 } .$ . That is, $\operatorname { G M } { = } ( \operatorname { S M } ; A _ { 2 } , \sim A _ { 3 } )$ . It takes an estimated modification effort of 20. However, this approach requires selecting the most similar case as described in Section 7.

Table 5  
Modification actions in OMML commands

<table><tr><td></td><td>OMML expressions</td><td> $E(A_i)$ </td></tr><tr><td rowspan="2"> $A_1$ </td><td>ADD_CONSTRAINT maximum_traveling_time_constraint</td><td rowspan="2">10</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT maximumtraveling_time_constraint</td></tr><tr><td rowspan="2"> $A_2$ </td><td>ADD_CONSTRAINT maximumtraveling_distance_constraint</td><td rowspan="2">10</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT maximumtraveling_distance_constraint</td></tr><tr><td rowspan="2"> $A_3$ </td><td>ADD_CONSTRAINT maximum_number_of_visiting_points_constraint</td><td rowspan="2">10</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT maximum_number_of_visiting_points_constraint</td></tr><tr><td rowspan="4"> $A_4$ </td><td>ADD_BOT fixed_cost_of_utilizing_vehicle_BOT TO OBJECTIVE_FUNCTION</td><td rowspan="4">12</td></tr><tr><td>ADD_INDEX flow_out_index 1 n+m TO BOT fixed_cost_of_utilizing_vehicle_BOT</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO BOT fixed_cost_of_utilizing_vehicle_BOT</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO BOT fixed_cost_of_utilizing_vehicle_BOT</td></tr><tr><td rowspan="11"> $A_5$ </td><td>ADD_CONSTRAINT IF visit_constraint THEN compatibility_requirement_between_routes_and_time_constraint</td><td rowspan="11">47</td></tr><tr><td>ADD_INDEX flow_out_index 1 n TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX flow_out_index 1 n TO CONSTRAINT compatibility_requirement_between_routes_and_time_constraint</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO CONSTRAINT compatibility_requirement_between waypoints_and_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT compatibility_requirement_between waypoints_and_time_constraint</td></tr><tr><td>ADD_CONSTRAINT earliest_delivery_time_constraint</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO CONSTRAINT earliest_delivery_time_constraint</td></tr><tr><td>ADD_CONSTRAINT latest_delivery_time_constraint</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO CONSTRAINT latest_delivery_time_constraint</td></tr><tr><td rowspan="12"> $A_6$ </td><td>ADD_CONSTRAINT IF visit_constraint THEN compatibility_requirement_between waypoints_and_departure_time_constraint</td><td rowspan="12">51</td></tr><tr><td>ADD_INDEX flow_out_index n+1 n+m TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX flow_out_index n+1 n+m TO CONSTRAINT compatibility_requirement_between waypoints_and_departure_time_constraint</td></tr><tr><td>ADD_INDEX flow_in_index 1 n TO CONSTRAINT compatibility_requirement_between waypoints_and_departure_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT compatibility Raeriest_departure_time_constraint</td></tr><tr><td>ADD_INDEX flow_out_index n+1 n+m TO CONSTRAINT earliest_departure_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT earliest_departure_time_constraint</td></tr><tr><td>ADD_CONSTRAINT latest_departure_time_constraint</td></tr><tr><td>ADD_INDEX flow_out_index n+1 n+m TO CONSTRAINT latest_departure_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT latest_departure_time_constraint</td></tr><tr><td rowspan="14"> $A_7$ </td><td>ADD_CONSTRAINT IF visit_constraint THEN compatibility_requirement_between waypoints_and_return_time_constraint</td><td rowspan="14">51</td></tr><tr><td>ADD_INDEX flow_out_index 1 n TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX flow_in_index n+1 n+m TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT visit_constraint</td></tr><tr><td>ADD_INDEX flow_out_index 1 n TO CONSTRAINT compatibility Raeriest Return routes_and_return_time_constraint</td></tr><tr><td>ADD_CONSTRAINT IF visit_constraint THEN compatibility Raeriest Return routes_and_return_time_constraint</td></tr><tr><td>ADD_INDEX flow_in_index n+1 n+m TO CONSTRAINT compatibility Raeriest Return routes_and_return_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT compatibility Raeriest Return routes_and_return_time_constraint</td></tr><tr><td>ADD_CONSTRAINT earliest_return_time_constraint</td></tr><tr><td>ADD_INDEX flow_out_index n+1 n+m TO CONSTRAINT earliest_return_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT earliest_return_time_constraint</td></tr><tr><td>ADD_CONSTRAINT latest_return_time_constraint</td></tr><tr><td>ADD_INDEX flow_out_index n+1 n+m TO CONSTRAINT latest_return_time_constraint</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO CONSTRAINT latest_return_time_constraint</td></tr><tr><td> $A_8$ </td><td>ADD_BOT service_time_BOT IN LHS OF CONSTRAINT compatibility Raeriest Return routes_and_time_constraint</td><td>6</td></tr><tr><td rowspan="2"> $A_9$ </td><td>ADD_BOT penalty_for_tardy_arrival_time_BOT TO OBJECTIVE_FUNCTION</td><td rowspan="2">8</td></tr><tr><td>ADD_INDEX flow_out_index n n+m TO BOT penalty_for_tardy_arrival_time_BOT</td></tr><tr><td rowspan="3"> $A_{10}$ </td><td>ADD_BOT penalty_for_exceeded_routing_duration_BOT TO OBJECTIVE_FUNCTION</td><td rowspan="3">10</td></tr><tr><td>ADD_INDEX flow_out_index 1 n + m TO BOT penalty_for_exceeded_routing_duration_BOT</td></tr><tr><td>ADD_INDEX vehicle_index 1 v TO BOT penalty_for_exceeded_routing_duration_BOT</td></tr><tr><td rowspan="2"> $A_{11}$ </td><td>ADD_CONSTRAINT first_visit_constraint</td><td rowspan="2">10</td></tr><tr><td>ADD_INDEX flow_in_index first_visit_list TO CONSTRAINT first_visit_constraint</td></tr><tr><td rowspan="2"> $A_{12}$ </td><td>ADD_CONSTRAINT last_visit_constraint</td><td rowspan="2">10</td></tr><tr><td>ADD_INDEX flow_out_index last_visit_list TO CONSTRAINT last_visit_constraint</td></tr><tr><td rowspan="2"> $A_{13}$ </td><td>ADD_CONSTRAINT precedence_constraint</td><td rowspan="2">10</td></tr><tr><td>ADD_INDEX flow_out_index flow_in_index precedence_list TO CONSTRAINT precedence_constraint</td></tr></table>

## 7. Comparative performance of modification approaches

Let us compare the performance of three modification approaches with the 24 experimental model structures. The proximity of the experimental models to the primitive model is almost uniformly distributed between the primitive and full models as depicted in the horizontal axis of Fig. 6. The proximity is measured by the effort required to modify from the primitive model.

If we can measure the threshold of efficient approach, the optimization model agent can automatically identify the best approach for formulation. To measure the total effort of formulation $( E _ { \mathrm { { T } } } ;$ T implies total), we consider two types of efforts: base model selection effort $( E _ { \mathrm { { S } } } )$ and modification effort from the base model $( E _ { \mathrm { M } } )$ . On average, the experimental models have 10 delivery orders and 3 trucks. Since the UNIK-OPT modifies the models at a semantic level, the modification effort does not increase in proportion to the number of variables.

![](/api/attachments/3HC6KGH2/fulltext/images/bc265deaaf653a56d8a5459fe9906722ebfde022c885f437379aaf308f458875.jpg)  
Fig. 5. GM=(M-VRP; A<sub>2</sub>, A<sub>5</sub>, A<sub>8</sub>) expressed in UNIK-OPT.

(a) Base model selection effort  
![](/api/attachments/3HC6KGH2/fulltext/images/b229ce67cce8ce887bd08a807b49981395eff3ab564925250d100052993ba3e1.jpg)

(b) Modification effort  
![](/api/attachments/3HC6KGH2/fulltext/images/529c69b5e653ce4be0b31a4eaba3137ff550f791323a77eceec95b9cd0281d43.jpg)

(c) Total effort of formulation  
![](/api/attachments/3HC6KGH2/fulltext/images/8afcf000a026716af8749c3d4773008774e0388bd541739b9471d1ad4c47fdfc.jpg)  
Fig. 6. Sensitivity of proximity.

## 7.1. Accuracy of the modification effort estimator

The modification effort is estimated by the number of associated objects as defined in Table 4. To empirically evaluate the actual effort, we have executed the modification and measured the time in seconds. The estimates and actual execution times are fitted by a regression model and the resultant correlation is very high with $R ^ { 2 } { = } 0 . 9 9 2$ for the primitive model approach and 0.999 for the full model approach. Consequently, the estimator is good enough for the effort prediction.

## 7.2. Sensitivity of proximity

The effort for the base model selection, modification, and their total are plotted in Fig. 6.

The effort for the base model selection of the full model approach is about twice of that of the primitive model approach, while the most similar case approach takes about four times as long, as depicted in Fig. 6(a).

The modification efforts are depicted in Fig. 6(b). The relationship of the actual modification effort and proximity is fitted by the regression model (28). The estimates are summarized in Table 6.

a<sub>M</sub>, $\beta _ { \mathrm { M } } ,$ and t-values in modification effort estimation model

<table><tr><td>Approaches</td><td> $\alpha_{M}$ </td><td> $\beta_{M}$ </td><td>Hypothesis testing</td><td> $R^{2}$ </td></tr><tr><td>Primitive model</td><td>0.50</td><td>0.04</td><td> $H_{0}: \beta_{M} \leq 0, H_{a}: \beta_{M} > 0, t = 53.39 \geq t(24, 0.01) = 2.49$ </td><td>0.992</td></tr><tr><td>Full model</td><td>6.74</td><td>-0.03</td><td> $H_{0}: \beta_{M} \geq 0, H_{a}: \beta_{M} < 0, t = -137.71 \leq -t(24, 0.01) = -2.49$ </td><td>0.999</td></tr><tr><td>The most similar case</td><td>-0.26</td><td>0.01</td><td> $H_{0}: \beta_{M} \leq 0, H_{a}: \beta_{M} > 0, t = 6.39 \geq t(24, 0.01) = 2.49$ </td><td>0.630</td></tr></table>

$$
\text { Actual } E _ {\mathrm{M}} = \alpha_ {\mathrm{M}} + \beta_ {\mathrm{M}} \text { Proximity }\tag{28}
$$

The primitive model approach has a positive trend and the full model approach has a negative trend. The t-value of the primitive model approach is 53.39 and that of the full model approach is  137.71. Thus, the trends are statistically significant at the 1% level. Note that the most similar case approach also has a positive trend, which implies that as the complexity of constraints increases, the modification effort even from the most similar case increases.

The total efforts are depicted in Fig. 6(c). In this example, the most similar case approach is partially dominated by the other two approaches at near proximity 100. For the goal models, whose proximity is less than 107.3, the primitive model approach outperforms the most similar case approach. Otherwise, the full model approach outperforms the others. According to this, the primitive model approach performs best for the model $\mathrm { G M } { = } ( \mathrm { M } { \mathrm { - } } \mathrm { V R P } ; A _ { 2 } , A _ { 5 } , A _ { 8 } )$ . The performance pattern may differ depending upon the application domains. We need, therefore, to study the threshold with experimental data in advance or learn while using for each application domain. The benefit increases as the scale of model warehouse expands.

## 8. Architecture of AGENT-OPT

With the approaches described earlier, we can design the optimization agent AGENT-OPT as Fig. 7.

The problem solving process is depicted in Fig. 7. (1) The optimization modeling requester agent receives a problem statement from a modeling requester. (2) The requester agent generates a problem requirement

![](/api/attachments/3HC6KGH2/fulltext/images/e72a905b633235529c3bb74a6f7c7b012ddf9aa1e99d91ae194fe3446f46282e.jpg)  
Fig. 7. Architecture of AGENT-OPT and its application to delivery scheduling.

![](/api/attachments/3HC6KGH2/fulltext/images/66a0322314f2113e14d0e9b50578d65c029786a7811c462301ca07da3ea4a429.jpg)  
Fig. 8. Modeling request message from a modeling requester.

expressed in the modeling request language of XML as in Fig. 8 and transmits it to the optimization agent AGENT-OPT. (3) AGENT-OPT interprets the modeling request language to the base model selection and modification factors. (4) The agent selects a base model and identifies the necessary modification actions. (5) The agent modifies the base model to a goal model. (6) The agent solves the model by an IP solver (we used LINDO as the IP solver) and generates a solution message in XML to return it to the modeling requester.

## 9. Conclusion

We have developed a case-based modification scheme that can formulate optimization models automatically and designed a prototype tool AGENT-OPT that can manage a model warehouse. For the modification, the efficiency of the primitive model, full model, and most similar model approaches are compared, and the conditions when an approach is most efficient are discovered. Since Web-based hubs need to provide the optimization model management service to various clients, such as delivery schedulers and virtual manufacturing schedulers, we need to device architecture that can generate, reuse, and modify the various models already built. In the future, the hypertext descriptions of the optimization model can be supported by using the XRML approach [26].

We confirmed that the architecture AGENT-OPT, which uses the representation of UNIK-OPT, could be an answer to the requirements of a model warehouse and interactions with other software agents. We have designed the ontology for delivery scheduling problems, and validated the architecture. The approach should be applicable to other application domains of a model warehouse.

In terms of the application domain of delivery scheduling studied in the research, we should further investigate the relationship between schedule negotiations for infeasible solutions, delivery coordination by an intermediary with the protocols such as contract net protocol [37] and time-bounded negotiation protocol [29].

## References

[1] M. Binbasioglu, Process-based reconstructive approach to model building, Decision Support Systems 12 (2) (1994) 97 – 113.

[2] M. Binbasioglu, M. Jarke, Domain specific DSS tools for knowledge-based model building, Decision Support Systems 2 (3) (1986) 213 – 223.

[3] R.W. Blanning, A relational framework for model management in decision support systems, DSS-82 Transactions (1982) 16–28.

[4] R.W. Blanning, An entity-relationship approach to model management, Decision Support Systems 2 (1) (1986) 65 – 72.

[5] R.W. Blanning, Model management systems: an overview, Decision Support Systems 9 (1) (1993) 9 – 18.

[6] N. Bolloju, M. Khalifa, E. Turban, Integrating knowledge management into enterprise environments for the next generation decision support, Decision Support Systems 33 (2) (2002) 163–176.

[7] R. Bonczek, C. Holsapple, A. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[8] J. Carbonnel, Derivational analogy: a theory of reconstructive

problem solving and expertise acquisition, in: R. Michalski, et al. (Eds.), Machine Learning, vol. 2. Morgan Kaufmann, San Francisco, CA, 1986, pp. 371 – 392.

[9] D.R. Dolk, B.R. Konsynski, Knowledge representation for model management systems, IEEE Transactions on Software Engineering, SE-10:6 (1984) 619 – 628.

[10] A. Dutta, A. Basu, An artificial intelligence approach to model management in decision support systems, IEEE Computer 17 (9) (1984) 89–97.

[11] J.J. Elam, J.C. Henderson, L.W. Miller, Model management systems: an approach to decision support in complex organizations, Proceedings of the First International Conference on Information System, 1980, pp. 98– 110.

[12] A.M. Geoffrion, Introduction to structured modeling, Management Science 33 (5) (1987) 547 – 588.

[13] A.M. Geoffrion, The formal aspects of structured modeling, Operations Research 37 (1) (1989) 30 – 51.

[14] S.Y. Huh, Model-base construction with object-oriented constructs, Decision Sciences 24 (2) (1993) 409 – 434.

[15] T. Ishikawa, T. Terano, Analogy by abstraction: case retrieval and adaptation for inventive design expert systems, Expert Systems with Applications 10 (3/4) (1996) 351 – 356.

[16] S.T. Kedar-Cabelli, Toward a Computational Model of Purpose-Directed Analogy, Kaufmann, Analogica, CA, 1988.

[17] C.S. Kim, J.K. Lee, Automatic structural identification and relaxation for integer programming, Decision Support Systems 18 (3 – 4) (1996) 253 – 271.

[18] B. Konsynski, D.R. Dolk, Knowledge abstractions in model management, DSS-82 Transactions (1982) 187– 202.

[19] R. Krishnan, A logic modeling language for automated model construction, Decision Support Systems 6 (3) (1990) 123–152.

[20] R.V. Kulkarni, P.R. Bhave, Integer programming formulations of vehicle routing problems, European Journal of Operational Research 20 (1985) 58– 67.

[21] B. Le Claire, R. Sharda, An Object-oriented Architecture for Decision Support Systems, 1990 ISDSS Conference Proceedings, 1990, pp. 567 – 586.

[22] J.S. Lee, Structure frame based model management system, Unpublished doctoral dissertation, University of Pennsylvania, 1989.

[23] J.S. Lee, A model base for identifying mathematical programming structures, Decision Support Systems 7 (2) (1991) 99 – 105.

[24] J.K. Lee, M.Y. Kim, Knowledge-assisted optimization model formulation: UNIK-OPT, Decision Support Systems 13 (2) (1995) 111– 132.

[25] J.K. Lee, B.Y. Lee, Integrated management system for optimization and heuristic models, Working paper, KAIST, 2002.

[26] J.K. Lee, M.M. Sohn, eXtensible Rule Markup Language— Toward the Intelligent Web Platform, Communications of the ACM, 2002 (forthcoming).

[27] J.K. Lee, Y.U. Song, Unification of linear programming with a rule-based system by post-model analysis approach, Management Science 41 (5) (1995) 835– 847.

[28] J.S. Lee, C.V. Jones, M. Guignard, MAPNOS: mathematical programming formulation normalization system, Expert Systems With Applications 1 (1990) 367– 381.

[29] K.J. Lee, Y.S. Chang, J.K. Lee, Time-bounded negotiation framework for electronic commerce agents, Decision Support Systems 28 (4) (2000) 319– 331.

[30] M.L. Lenard, An object-oriented approach to model management, Decision Support Systems 9 (1) (1993) 67 – 73.

[31] T.P. Liang, Integrating model management with data management in decision support systems, Decision Support Systems 1 (1) (1985) 221– 232.

[32] T.P. Liang, Modeling by analogy: a case-based approach to automated linear program formulation, IEEE, (1991) 276 – 283.

[33] T.P. Liang, Analogical reasoning and case-based learning in model management systems, Decision Support Systems 10 (2) (1993) 137–160.

[34] T.P. Liang, B.R. Konsynski, Modeling by analogy: use of analogical reasoning in model management systems, Decision Support Systems 9 (1) (1993) 113 – 125.

[35] W.A. Muhanna, An object-oriented framework for model management and DSS development, 1990 ISDSS Conference Proceedings (1990) 553– 565.

[36] S.J. Park, H.D. Kim, Constraint-based metaview approach for modeling environment generation, Decision Support Systems 9 (4) (1993) 325– 348.

[37] R.G. Smith, The contract net protocol: high-level communication and control in a distributed problem solver, IEEE Transactions on Computer 29 (1980) 1104 – 1113.

[38] Y. Tsai, Model integration using SML, Decision Support Systems 22 (4) (1998) 355– 377.

[39] R.C. Vellore, A. Sen, A.S. Vinze, A Case-Based Planning Approach to Model Formulation, 1990 ISDSS Conference Proceedings, 1990, pp. 353 – 382.

[40] W.L. Winston, Operations Research, 3rd ed., Duxbury Press, Belmont, CA, 1994.

[41] K. Yeom, J.K. Lee, Logical representation of integer programming models, Decision Support Systems 18 (3 – 4) (1996) 227– 251.

![](/api/attachments/3HC6KGH2/fulltext/images/44c40c0cec1606d6ac6fb80aebf3ab26e87270f3d293cfe33d4fcfd9404373a1.jpg)

Yong Sik Chang has received a PhD from the Graduate School of Management at Korea Advanced Institute of Science and Technology (KAIST) and serves as a principal researcher at International Center for Electronic Commerce (ICEC). He received his BS (1988) from Sogang University and MS (1991) from Pohang Institute of Science and Technology (POSTECH). He has industrial experiences of developing MIS and elec-

tronic commerce applications. His current research focus is the electronic commerce, model management, and multi-agent systems.

![](/api/attachments/3HC6KGH2/fulltext/images/80a41646f6f5768b542e3feff94268bac753d970d73ba125d266c15d95a40dea.jpg)

Jae Kyu Lee is a Professor of Management Information Systems at Korea Advanced Institute of Science and Technology and a Director of the International Center for Electronic Commerce. He received a PhD from the Wharton School, University of Pennsylvania. He was Chair of the International Conference on Electronic Commerce (ICEC 1998 and ICEC 2000) and the Third World Congress on Expert Systems

(1996). He has authored several books on electronic commerce and expert systems and published numerous papers in the following journals: Management Science, CACM, DSS, Expert Systems with Applications, International Journal of Electronic Commerce, Decision Science, and many others. Currently, he is an Editor-in-Chief of the Journal Electronic Commerce Research and Applications and Editorial Member of various international journals like Decision Support Systems, Expert Systems with Applications, International Journal of Electronic Commerce, and so on. His main research interests are in the fields of electronic commerce and intelligent information systems.
