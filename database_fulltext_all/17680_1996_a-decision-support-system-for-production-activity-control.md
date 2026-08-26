---
otero_id: 17680
otero_key: "ZRJY3M5F"
title: "A decision support system for production activity control"
authors: "Bernard Grabot; Jean-Claude Blanc; Chantal Binda"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00003-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for production activity control

Bernard Grabot $^{*}$ , Jean-Claude Blanc, Chantal Binda

Ecole Nationale d'Ingénieurs de Tarbes, Avenue d'Azereix, BP 1629, 65016 Tarbes Cedex, France

## Abstract

The increase of manufacturing system flexibility makes variations in routings, operations, machines or operators possible. These degrees of freedom may be used at the Production Activity Control (PAC) level in order to react to unpredictable events such as machine failures, absence of operators or changes in the workshop environment. In order to manage these degrees of freedom, we suggest a Decision Support System that should make the choice of solutions easier in order to reduce the consequences of a failure. This DSS complements the scheduling module of the PAC system since it may be used, either in order to slightly modify an existing schedule, or to choose the scheduling hypothesis. This DSS uses fuzzy logic and theory of possibility because of the imprecision and uncertainty of the information managed, first to model the objectives, then to spread the expected consequences of an imprecisely known event.

The DSS has successively been prototyped with the SuperCard $^{TM}$ environment on a Macintosh microcomputer, then with the Oracle $^{TM}$ data base on a Sun Sparcstation.

Keywords: Decision support; Production management; Production activity control; Fuzzy logic; Data base

## 1. Introduction

To meet the pressure of the markets requiring more and more customized and cost-effective products, shop-floors have provided themselves with increasingly versatile and effective production means (numerical control machines, automated storehouses, automatic guided vehicles...). However, the individual efficiency of these resources is limited if production is not properly managed. This paper deals with shop-floors short-term production and inventory control, often called Production Activity Control or “PAC”, which is certainly the part of production and inventory control, the implementation of which is the most difficult.

Production Activity Control is a field of application in which many theoretical and practical works have been carried out. Moreover, there are solutions to classical problems such as production scheduling or shop-floor monitoring for most of the shop-floors' types. Nevertheless these solutions solve only partly the problem of PAC which more and more requires decision support.

The PAC level is located in the general scope of the production management system in section 2, where the problem of the reaction to unexpected events is emphasized. The principles of the Decision Support System we suggest are described in section 3. This system, based on the modeling of the workshop objectives through fuzzy logic, includes a module of constraint propagation that allows to assess the consequences of a perturbation on the objectives. The implementation of the system is shortly described in section 4, and an example of its use is given.

## 2. The context of Production Activity Control

The production management system is a complex structure of decision centers that aims at satisfying conflicting objectives such as customer's satisfaction, work in progress minimization, cost minimization or optimization of the resource use. Most of the time, the market constraints impose a hierarchical structure that has a substantial influence on the decision makings.

## 2.1. Decisional structure of Production Management

The main problem in Production Management is to organize the manufacturing resource use at middle-term or short-term on the base of imprecise and uncertain orders. The multiplicity of the products and resources is often managed through a hierarchical decision structure where a global decision is progressively refined until operational decisions are made. According to the MRP (Manufacturing Resource Planning) method $[1]$ this decisional structure is as follows:

— the customers send orders consisting in a reference of a product, a quantity of products and a lead time. The main decision consists, at that level, in making a realistic master production schedule that combines these firm orders with the production forecast. A list of orders (firm or forecasted) with delivery dates results from this level;

— this master production schedule allows to compute which components are necessary in order to perform the manufacturing operations (Requirement Planning). The output of this level is the dates of availability required for each product component;

— the period of time when each manufacturing operation should be performed by a work center is then assessed. The estimated capacity required for each work center for a given period is then computed (Capacity Requirement Planning);

— if overloads are detected, they are solved, either by an extension of the capacity (over-time, sub-contracting) or by load smoothing. A list of orders with realistic starting dates and firm precise delivery dates results from this level;

— a schedule is then computed in order to precisely allocate manufacturing orders to resources;

— a follow-up is performed in order to provide the previously described levels with up-to-date information.

Many formalization works have been performed in order to improve the efficiency of this decision making sequence. A convenient modeling frame is to consider this decisional structure as a hierarchized set of decision centers exchanging decision frames. A decision center, Dj, receives a decision frame from another center, Di, located at a higher level. This decision frame contains the current state of the decision variables (i.e. the result of the previously made decisions), as well as the objectives to satisfy at level j and the means under responsibility of the decision center, plus a responsibility frame which gives the limits allowed on the use of these means. The result of a decision making is another decision frame, transmitted to one or several decision center Dk, located at lower levels and depending on Dj [2] (see Fig. 1). The decision center level is characterized by its “horizon”, i.e. by the validity duration of the decision making, and its “period” defined as the lapse of time until a decision is called into question. For instance, a schedule that plans the workshop activity for two weeks and is updated every three days has an horizon of two weeks and a period of three days. The period is determined in accordance with the frequency of disturbances and with the robustness of the decision makings. It allows to adapt the workshop to these events.

![](/api/attachments/ZRJY3M5F/fulltext/images/eb32b77bae70fd22386ce24414b2ca4a8a68968859aaf0337180899ac082db52.jpg)  
Fig. 1. Structure of decision centers.

Since failures and unexpected events are constantly occurring, this decisional structure works in closed loop thanks to follow-up information sent to the different decision centers with various aggregation levels.

Two kinds of tools should be used by the decision centers:

— reports, in order to compare the current objective satisfaction with the required one;

— decision supports, such as decision tables or simulation tools, in order to forecast the consequences of a decision making.

Since they highly depend on the controlled workshop, the operational levels of the production management system are not covered by production management methods such as MRP, or have their degrees of freedom very restricted in just-in-time methods (e.g. production in lines, product families, mass production, and so on). Production Activity Control does not depend on a precise production management method, and is nowadays a key point of productivity and reactivity improvement.

## 2.2. Conceptual model of a Production Activity Control module

Production Activity Control may be considered as operational levels of production management. In a synthetic way, PAC can be defined as the group of activities directly in charge of the management of planned order transformation into a set of outputs. It manages the very short-term detailed planning, execution and monitoring activities required to control the flow of an order from the time when this order is released by the planning system for execution until it is filled and its disposition completed $[3]$ .

Four main functions can be distinguished in PAC [4], [5]:

— the function “plan” considers the production plan and the objectives transmitted by the “father” decision-center. It implements techniques to adapt this production plan to the stated objectives and makes it operational on a time horizon and a fixed period. At a low level, the function “plan” mainly consists in scheduling. Its practical role is the choice of the routings, resource calendars, resources and starting date of each operation;

— the function “launch” breaks down, synchronizes and executes decisions taken within the PAC module. The decision variables are resource permutations, manufacturing order interruptions, and manufacturing orders permutations on a resource;

— the function “follow-up” collects all the results provided by sensors or “son”-decision-modules as well as the requests external to the shop-floor, processes them according to their types and aggregation levels and transmits them to other functions and to other PAC modules. There is no real decision making in this function, but an assessment of the satisfaction degree of the objectives given by the current workshop behavior;

— the function “react” allows a real-time adaptation of the decisions taken at different management levels. This function acts punctually, and not on a complete production plan when it adapts a plan that is not directly feasible or cannot be transmitted to the production system status. It can also re-launch the function “plan” after a disturbance or when the discrepancy between the real objective satisfaction and the required one is too high.

Fig. 2 shows a PAC module that can be defined on the base of these functions. This module can be implemented at various decisional levels as a macro-decision center.

The PAC role is essential, since it applies middle-term decision makings of the upper levels with the adaptations required by short term or real time disturbances. The application of the middle term decision makings including as few modifications as possible is significant since these decisions aim at optimizing the use of the resources (e.g. operator occupation, overtime or sequences of products on the resources, which influence the set-up times).

![](/api/attachments/ZRJY3M5F/fulltext/images/e434256636fc16c4e24afbea8e8dde40147c32ecfe45a8da8e34e20d6725cfbe.jpg)  
Fig. 2. Model of the PAC module.

## 2.3. Decision support in PAC module

The activities of the PAC module use various kinds of softwares, such as schedulers or follow-up softwares, but these softwares do not solve all problems, since the management of their degrees of freedom requires difficult decision makings.

Two main kinds of problems may result from an incorrect use of the PAC level:

— inadequate reactivity of the system, when the decision makings coming from upper levels are not modified to be adapted to the disturbances. In the most serious cases, the middle term decision makings become unrealistic in consideration of the real possibilities of the workshop, therefore the system is not controlled anymore;

— poor optimization of the resource use, when an opportunistic control based on the reaction to disturbances replaces the middle term levels.

According to our experience, the second problem arises much more often than the first one. As a matter of fact, the first performance criterion of a workshop is the daily production level, as well as the customers' satisfaction provided by this production. The optimization of the resource use is only considered afterwards, when accounting analyses become available. Moreover, these analyses are often used as statements rather than operational indicators.

A decision support at the PAC level should then include:

— a clear modeling of the workshop objectives, that could be used either at the follow-up level in order to build the decision center reports, or as a criterion in order to compare possible decision makings;

![](/api/attachments/ZRJY3M5F/fulltext/images/e1e2c58cbaf6ecd45d4aa5a6799e489741b966eaadda001a863bd436a759b6f6.jpg)  
Fig. 3. DSS modules.

— the management of the degrees of freedom used at the operational level in order to react to failures. This management should not be a substitute to scheduling, but should complement it:

— at a higher level, with the choice of new scheduling hypothesis (new starting dates, new resources or new calendars);

— at a lower level, with the adaptation of the schedule to small changes. As stated above, an adaptation is preferable to a deep modification in order to respect the workshop organization based on the previous schedule. In relation to the horizon and the period of decision makings described above, this support does allow to react to events but also makes the increase of the schedule period possible.

Several approaches are possible in order to manage these degrees of freedom. We describe in this paper a DSS based on a simulation approach, with a performance evaluation that uses fuzzy logic and the theory of possibility.

## 3. Principles of the Decision Support System

Fig. 3 shows the structure of the suggested DSS. This system supports the operator for three functions of PAC:

— the “follow-up” function, with the design of reports based on a modeling of the workshop objective satisfaction;

— the “react” function, with the use of degrees of freedom on the resources in order to minimize the effect of disturbances;

— the “launch” function, with the use of degrees of freedom such as starting dates of products or operation sequence.

The main modules of the DSS are the following:

— a database, allowing not only to store information about routings and resources but also follow-up information;

![](/api/attachments/ZRJY3M5F/fulltext/images/7699c28b0018da0430446f7003267ec2bcb8a453eb938027ae5ca8afa4aacda1.jpg)  
Fig. 4. Manufacturing data model.

![](/api/attachments/ZRJY3M5F/fulltext/images/12aafc24a107731d78286353ca63dadc8fd6f0a3b37b3cfcd39931ab527b31f4.jpg)  
Fig. 5. Scheduling data model.

— a “search for solution” module, that suggests different ways to react to an event;

— a simulation module, providing the performance allowed by potential decisions;

— a performance evaluation module, allowing to model the workshop objectives and to judge a real or potential situation in reference to these objectives. This module is based on the propagation of fuzzy temporal constraints. Fuzzy logic has also been used in order to model the workshop objectives since objective satisfaction may be partial.

## 3.1. Database

Since the DSS does not compute a schedule, but may only modify it, the required data structure is simpler than the one of an industrial scheduler. The DSS data model focuses on the degrees of freedom that may occur on resources or slack times. The conceptual model of the data structure is shown in Figs. 4, 5 and 6. It uses the entity-relationship model widely used for data modeling [6]. The conceptual model has been divided into three parts in order to be read more easily:

— the manufacturing data, describing routings, orders and resources (Fig. 4);

— the scheduling data, describing the result of the schedule in terms of operation planning (Fig. 5);

— the follow-up data, describing part localization and possible unavailability of resources (Fig. 6).

The manufacturing data model describes a routing as an alternation between machining or storage operations, and transport operations. A part type can be produced through one or several operations. In a routing, an operation can be immediately followed by another one or several ones if it is possible to choose. The types of resources required in order to perform the operations are listed (resource types are considered since these data are rather independent from the physical resources which are available in the workshop). Physical resources may belong to one or several kinds of resources (e.g. an operator may be considered as a vehicle if he can displace the parts).

The scheduling data model allows to store the schedule built by the “plan” PAC function. The schedule allocates physical resources to operations and defines a starting date and an end date for these operations.

The follow-up data model allows to store not only the localization of the parts and vehicles, but also the disturbances that may occur on the physical resources. These disturbances are interpreted as an unavailability time interval.

![](/api/attachments/ZRJY3M5F/fulltext/images/86ac9e136bf95f2ca006bdfdb356387d1c8255d7289aa46b25ba24a9a5f0e394.jpg)  
Fig. 6. Follow-up data model.

![](/api/attachments/ZRJY3M5F/fulltext/images/4f46d39b5e41f0a101d732332f42021af1e9b10bf1d9423a8e6ed8187a5d2532.jpg)  
Fig. 7. Membership function of the fuzzy set representing the “correct productions”.

## 3.2. Objective modeling

The principles of the decisional structure of a production system described in section 2.1 emphasize the definition of quantitative objectives in order to provide a target to decision making. The real implementation of these principles in actual workshops is very poor, since:

— the workshop objectives often remain implicit;

— their formalization is only important as an a posteriori statement but is not used as an operational tool, since it is very difficult to correlate an action to the objective satisfaction.

The “performance evaluation” module of the DSS aims at solving the first problem, whereas the simulation module described in next section deals with the second one.

Fig. 1 shows that the manufacturing objectives form a hierarchy. At the highest level, these objectives should be expressed in monetary units (i.e. cost price or benefits), but at the PAC level, objectives become operational and can be classified as follows:

<table><tr><td>objective</td><td>attribute</td><td>definition</td></tr><tr><td>machining quality</td><td>standard deviationaround required value</td><td> $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{\frac{i}{n}}}$ </td></tr><tr><td>respect ofdelivery dates</td><td>number of late orders,average lateness AL,average tardiness AT...</td><td> $\sum ((completion date job i)-(delivery date job i))$  $\text{AL} = \frac{i}{n}$  $\text{AT} = \sup(0, \text{AL})$ </td></tr><tr><td>respect ofquantities</td><td>percentage ofproduction achieved</td><td> $c = \frac{quantity of parts achieved}{quantity of parts required}$ </td></tr><tr><td>maximization ofthe resource use</td><td>utilization ratio</td><td> $u = \frac{open hours}{working hours}$ </td></tr><tr><td>minimization ofoverloads</td><td>percentage ofoverloads</td><td> $o = \frac{number of overload hours}{number of open hours}$ </td></tr><tr><td>minimization ofdirect cost</td><td>direct cost</td><td> $dc = \sum_{i} running time_i$  (in hours) x resource cost (per hour)</td></tr><tr><td>minimization ofscraps</td><td>scrap ratio</td><td> $s = \frac{number of scraps}{number of parts}$ </td></tr><tr><td>work in progressminimization</td><td>work in progress ratio</td><td> $w = \frac{number of parts produced}{average number of parts in the workshop}$ </td></tr><tr><td>flowtimeminimization</td><td>flowtime ratio</td><td> $f = \frac{\sum (operation duration i)}{flow time}$ </td></tr></table>

Fig. 8. Example of an operational objective modeling.

— the objectives related to the customer service, such as product quality, respect for delivery dates and quantities;

— the objectives related to the resource use, such as utilization ratio maximization or overload minimization;

— the objectives related to the product flow, like work-in-progress minimization or flowtime minimization;

— the objectives related to the resource/product couple, such as scrap ratio minimization or direct cost minimization (i.e. cost related to the resource use).

The satisfaction of these objectives is not binary: if a quantity objective is 1000 parts per day, it is not wise to consider that the manufacturing of 1001 parts completely satisfies the objective whereas the manufacturing of 999 parts does not satisfy it at all. Since the satisfaction of an objective is a matter of degree, we have chosen fuzzy logic as a modeling tool.

Fuzzy logic is based on the theory of fuzzy sets [7], which defines the membership of an object to a set as a degree belonging to the [0,1] interval instead of a binary value (0 or 1). A proposition such as “Today production is correct” may be modeled by the fuzzy set defined by the membership function $\mu$ of Fig. 7. If the production of the day is 800 parts, the membership degree of this production to the fuzzy set of the “correct productions” is $\mu(800)=0.6$ . “0.6” can also be interpreted as the satisfaction degree of the objective.

We have chosen to express the PAC level objectives with this technique, which requires:

— to define first qualitatively an objective as an imprecise proposition;

— to choose an attribute in order to valuate the objective;

— to choose a unit for the attribute values;

— to define a membership function, on the basis of the requirements of the decision centers that control PAC centers.

Fig. 8 gives some modeling examples of the operational objectives described above, however, the attributes and definitions that best suit the objectives have to be defined for each workshop, in accordance with the production management method which is used.

The theory of Possibility provides a tool in order to compare the real workshop performance to the required objective. Let us assume that the daily expected production should be “perhaps between 800 and 900 parts, surely more than 700 parts and less than 1000 parts”. This proposition can be modeled by a trapezoidal possibility distribution $\pi_{P'}$ that can be compared to the objective thanks to two degrees [8]:

— a possibility degree, defined as:

$$
\Pi (P; P ^ {\prime}) = \sup _ {u \subset U} \min \left(\mu_ {P} (u), \pi_ {P ^ {\prime}} (u)\right)\tag{1}
$$

— a necessity degree, defined as:

$$
N (P; P ^ {\prime}) = \inf _ {u \subset U} \max \left(\mu_ {P} (u), 1 - \pi_ {P ^ {\prime}} (u)\right)\tag{2}
$$

where ‘u’ stands for the number of parts, $\mu_{P}$ is the membership function of the production objective and $\pi_{P'}$ the possibility distribution that has to be compared to the objective (see Fig. 9).

![](/api/attachments/ZRJY3M5F/fulltext/images/baa718b44f8ad57b2c096ef8317bdb6e34f884aef29b18bcac2e5a2edb3b5a4e.jpg)

![](/api/attachments/ZRJY3M5F/fulltext/images/84c85532d350ee50e89de78402a804e73321fc5cdc58c192bfb3abb71a7874fe.jpg)  
Fig. 9. Example of possibility and necessity degrees computations.

$\Pi(P; P')$ can be interpreted as the degree of overlapping of the fuzzy sets of values compatible with P with the fuzzy set of possible values of $P'$ . $N(P; P')$ is the inclusion degree of the set of possible values of $P'$ in the set of values compatible with P.

Since workshop management is essentially multi-objective, it is necessary to be able to combine elementary objectives in order to provide aggregated reports. In order to achieve this combination, we have chosen the weighted pattern matching method described in [9]. It allows to weigh the respective importance of the elementary objectives. An objective function is described as follows:

— elementary objectives are first chosen, related to costs, delays, work in progress and so on ...;  
— a global function is then defined, through the choice of weights and logical operators allowing to aggregate elementary objectives. Most of the time, elementary objectives are connected by AND logical links, that can be expressed by "min" operators in the theory of possibility. More complex operators can be defined if required: we can find in [10] a comparison of different operators that shows the robustness of an objective function when several classical operators are used.

If the possibility and necessity degrees of the elementary objectives are known (respectively noted $\Pi_{i}$ and $N_{i}$ ), the satisfaction degree of the global objective O is described by the global possibility and necessity measures of formulae (3) and (4):

$$
\Pi (O; O ^ {\prime}) = \min _ {i} \max \left(1 - w _ {i}, \Pi_ {i} \left(G _ {i}; G _ {i} ^ {\prime}\right) \right.\tag{3}
$$

$$
N (O; O ^ {\prime}) = \min _ {i} \max \left(1 - w _ {i}, N _ {i} \left(G _ {i}; G _ {i} ^ {\prime}\right) \right.\tag{4}
$$

where the $w_{i} \in [0,1]$ are the respective weights of the objectives.

For instance, let us define a simple objective by the following linguistic proposition:

"It is absolutely necessary to have an important level of production, and it is desirable to have a poor scrap level". This imprecise proposition can be quantified in associating weights to the "necessary" and "desirable" linguistic appreciations, and membership functions to "im-"portant level of production" and "poor scrap level" (this quantification has to be negotiated with the decision center from which comes the decision frame which contains this objective). Trapezoidal membership functions are often sufficient to express a correct expertise [8] since a high precision is rarely required for expert appreciations. Let us adopt the classical notation (a,b,c,d) for a trapezoidal function, where 'a' is the last point of the raising front, 'b' the first point of the falling front, 'c' the width of the raising front, and 'd' the width of the falling front. Let us assume that an "important level of production" can be modeled by the membership function (80,90,0,5)% with the definition of Fig. 9, and a "poor scrap level" is defined by (10,10,5,5)%. If "necessary" corresponds to a weight of 1 and "desirable" to a weight of 0.5, the objective function can then be modeled by:

$$
O = \text { Production } (8 0, 9 0, 0, 5) x (1) \text {   AND }
$$

$$
\text { Scrap } (1 0, 1 0, 5, 5) \mathrm{x} (0. 5).
$$

Assuming that the obtained values are (85,85,5,5)% for the production level and (15,15,5,0)% for the scrap ratio, formulae (1) and (2) give $\Pi(\text{production level}) = 1$ , $N(\text{production level}) = 1$ , $\Pi(\text{scrap level}) = 0.5$ , $N(\text{scrap level}) = 0$ . Formulae (3) and (4) give then $\Pi(O) = 0.5$ and $N(O) = 0.5$ . The value (1 - weight of the scrap objective) acts as a threshold beneath which the satisfaction degree of the elementary objective is no more taken into account in the computation of the global function. However, the computation remains possible if the production and scrap ratios are precisely known, e.g. the same result is obtained for a production ratio of 85% and a scrap ratio of 13%.

It is interesting to notice that this method can allow to define objectives in accordance with the production management method used: e.g., MRP gives a specific emphasis on the maximization of the resource use whereas just-in-time methods do not consider this objective, moreover OPT (Optimized Production Technology) [11] only considers it for bottlenecks. In the same way, an expression of the respect of delivery dates through a tardiness is sufficient in MRP (the fact that a job is in advance is not considered as negative) whereas it has to be expressed through the lateness in JIT methods, where neither orders in advance nor late orders are allowed.

## 3.3. "Search for solutions" module

This module uses the database described above in order to find adequate reactions to disturbances. The way to react to a disturbance depends on many factors, the first one being the origin of the disturbance. The main origins that can be considered at the PAC level are:

— the disturbances related to customer orders, i.e. order cancellation, order addition or modification of an order delivery date;

— the disturbances related to the parts or components, i.e. unavailability due to stockout or scraps;

— the disturbances related to the unavailability of resources, i.e. machine breakdowns or absence of operator.

Since the reaction to disturbances on parts and customer orders often requires a new schedule, we draw our attention to the unavailability of resources that can be treated under some conditions without deep changes of the schedule. In this context, two factors are substantial in order to find a proper way for reaction:

— the disturbance duration;

— the criticity of the involved resource, that depends on the existence of replacement resources.

In the first version of the DSS, solutions are searched in an algorithmic way and belong to three main categories:

— the waiting, until the resource is available again, then the return to the planned operations. The influence on the schedule directly depends on the disturbance duration;

— the use of the slack times that remain in the schedule. As a matter of fact, it is almost impossible to find a schedule that allows full machine loading because of the resource sharing. Slack times in the precise positioning of the operations are often available, however, they are quite difficult to find. The DSS module searches for free slack times, i.e. time intervals than only concern the positioning of the disturbed operation, or total slack times that also disturb the positioning of adjacent operations;

— the resource replacement.

If the disturbance concerns a machining operation, this resource replacement consists in:

— the replacement by another operator with an equal or higher ability, in case of the absence of an operator;

— the replacement by an equivalent machine, in case of a machine failure;

— the operation replacement;

— the routing replacement.

If the problem concerns a vehicle, the solutions are the replacement of the vehicle by another one, e.g. robot or A.G.V. by operator.

These procedures can be carried out thanks to the data models described in Figs. 4 to 6, which emphasize the possible replacements between the resources.

## 3.4. Simulation module

As described in Fig. 3, the objective of this simulation is to assess the modification of the schedule induced by the possible solutions to be tested. All the solutions listed in the previous section may be interpreted as changes in running times:

— if a maintenance operation is performed, its duration is added to the manufacturing operation that has been carried out when the failure occurred;

— if a new machine is required, a set-up time is added to the running time;

— if the unavailable machine and the replacement machine are not strictly similar (operation replacement), running times may be different (higher or lower).

The absence of operators may be considered similarly since the replacement of an operator may require time, and operators with different skills may require different amounts of time in order to achieve an operation.

The problem is to assess the repercussion of these changes on the schedule whereas the new durations may be imprecisely known (i.e. in the case of set-up times and of maintenance operations, or when operators perform unusual jobs). In order to carry out this, the precedence constraints between operations induced by the schedule are extracted thanks to the data, the storage of which is described in Fig. 5. These precedence constraints define a net analog to a PERT net where imprecise durations can be propagated thanks to the classical operations of fuzzy arithmetics [8].

The propagation of fuzzy precedence constraints requires the definition of ad hoc operations:

— if n operations $A_{1},\ldots,A_{i},\ldots,A_{n}$ have to be achieved before the operation B begins, the earliest starting date of the operation C is the maximum of the earliest end dates of the operations $A_{i}$ . Let us consider two fuzzy numbers T1 = (a1, b1, c1, d1) and T2 = (a2, b2, c2, d2). The maximum of T1 and T2 may be defined for instance as [8]:

$$
\begin{array}{l} (\max) (T 1, T 2) \approx (\max (a 1, a 2), \max (b 1, b 2), \\ \max (a 1 - c 1, a 2 - c 2), \\ \max (b 1 + d 1, b 2 + d 2) - \max (a 1, a 2); \end{array}\tag{5}
$$

— if an operation A has to be achieved so that an operation C starts, the starting date of operation C is the sum of the starting date of A (that may be imprecisely known) and of the duration of A. The sum of two fuzzy numbers is defined by:

$$
\mathrm{T} 1 (+) \mathrm{T} 2 = (\mathrm{a} 1 + \mathrm{a} 2, \mathrm{b} 1 + \mathrm{b} 2, \mathrm{c} 1 + \mathrm{c} 2, \mathrm{d} 1 + \mathrm{d} 2).\tag{6}
$$

Similarly, the computation of the latest end date of an operation requires the definition of the minimum and of the subtraction of two fuzzy numbers, which are respectively defined by:

$$
(\min) (T 1, T 2) \approx (\min (a 1, a 2), \min (b 1, b 2),
$$

$\min(a1 - c1, a2 - c2)$ ,

$$
\min (b 1 + d 1, b 2 + d 2) - \min (a 1, a 2)\tag{7}
$$

$$
\mathrm{T} 1 (-) \mathrm{T} 2 = (\mathrm{a} 1 - \mathrm{a} 2, \mathrm{b} 1 - \mathrm{b} 2, \mathrm{c} 1 + \mathrm{c} 2, \mathrm{d} 1 + \mathrm{d} 2).\tag{8}
$$

These operations have been defined in accordance with the corresponding operations between precise numbers, i.e. it is possible to combine fuzzy and precise numbers (a precise number ‘a’ may be defined with the membership function (a,a,0,0)).

![](/api/attachments/ZRJY3M5F/fulltext/images/267a46da3a7f16c4e37b3785e923210402418726844909208af8d71f0ec570cb.jpg)  
Fig. 10. Follow-up window.

This simulation based on constraint propagations allows not only to compute the new completion date of a job, but also the completion dates of the other jobs which were in progress when the failure occurred, since other jobs may be delayed because of the resource sharing.

This DSS has been implemented both on a Macintosh computer using the SuperCard $^{TM}$ environment and on a SUN Sparcstation with the Oracle $^{TM}$ database. These implementations are shortly described in next section, where an example is developed.

## 4. Implementation and use of the DSS

## 4.1. Design of the shell

The SuperCard $^{TM}$ environment is very close to HyperCard $^{TM}$ , which is an object oriented environment developed by Apple to make information management easier with the full benefit of the Macintosh interface facilities (color, mouse, menus, multiple windows...).

The database structure described in section 3.1 has been implemented in 24 tables which can be simultaneously visualized on the screen. The follow-up data table is always visible, and the events that occur (starting or end of operations, vehicle displacements...) are illustrated on an animated picture of the controlled workshop. Fig. 10 shows this picture on the case of the DSS designed for the ENIT flexible cell. This animation allows the operator to debug the schedule, and allows him to have an immediate understanding of the workshop state when a failure occurs.

When a schedule is simulated until its end, results with information such as the durations, the efficiency of the resource use or of the operators are provided. A Gantt chart is also available.

When a disturbance occurs, the DSS asks for the expected resource maintenance or absence of operator duration. This duration can be provided either precisely or through a fuzzy number. Then the “search for solutions” module looks for an adequate reaction to the disturbance as described in section 3.3. If the resource replacements are considered, the operator has to provide expected set-up times, in a precise or imprecise way.

When the possible solutions have been compared, the objective satisfaction described by the possibility and necessity degrees is converted into pie charts in order to be more easily understandable. Fig. 11 gives an example of interface where the satisfaction of six elementary objectives and their aggregation are shown. The whole surface of a pie chart corresponds to a complete satisfaction of an objective ( $\Pi = N = 1$ ). When the objective satisfaction is only partial, the necessity and possibility degrees define two sectors: a yellow sector for the possibility degree, and a green one for the necessity degree (respectively gray and black in Fig. 11).

![](/api/attachments/ZRJY3M5F/fulltext/images/7852a093bd687d50f79af730262396460d4d307473ee93bf925ed15773a05687.jpg)  
Fig. 11. Evaluation interface.

<table><tr><td>part</td><td>op.1 (duration, machine)</td><td>op. 2 (duration, machine)</td></tr><tr><td>A</td><td>P101(20, lathe)</td><td>P106(10, assembly)</td></tr><tr><td>B</td><td>P201(10, assembly)</td><td>P203(60, vert. center)</td></tr><tr><td>C</td><td>P301(10, assembly)</td><td>P303(70, hor. center)</td></tr><tr><td colspan="3"></td></tr><tr><td>part</td><td>op.3 (duration, machine)</td><td>op. 4 (duration, machine)</td></tr><tr><td>A</td><td>P111(50, hor. center)</td><td>P116(10, assembly)</td></tr><tr><td>B</td><td>P208 (10, assembly)</td><td>P213(40, lathe)</td></tr><tr><td>C</td><td>P308(40, vert. center)</td><td>P313(10, assembly)</td></tr></table>

Fig. 12. Part routings.

The implementation of the DSS on SuperCard is detailed in [12]. Another version of the DSS has been implemented using the Oracle $^{TM}$ relational data base in order to apply it in industrial environments.

## 4.2. Example

This example concerns the ENIT flexible cell, which includes a lathe, a vertical machining center, a horizontal machining center, an assembly station (in order to assemble parts on pallets) and a track mounted robot, that can feed all the machines. Three kinds of parts are considered, the manufacturing data of which are defined by variable routings.

We have chosen in this example to define an objective function through a direct cost and a delay objective, as defined in Fig. 8. Three parts are taken into account, which lead to six elementary objectives that may for instance be described as follows:

$$
\begin{array}{l l} \text {Costs:} & \text {part A: (320,400,10,10) } \\ & \text {part B: (450,550,0,20) } \\ & \text {part C: (600,700,0,50) } \end{array} \quad \begin{array}{l l} w _ {\mathrm{AC}} = 0. 9 \\ w _ {\mathrm{BC}} = 0. 8 \\ w _ {\mathrm{CC}} = 1 \end{array}
$$

where the $w_{ij}$ are the respective weights of the elementary objectives. In real cases the objective function should be negotiated with the decision center that controls the PAC level of the workshop, and may combine precise objectives, objectives defined as intervals or fuzzy objectives.

![](/api/attachments/ZRJY3M5F/fulltext/images/c36d6490e5fed7c78bbf3038d9d7673e89a6c4ac44ff223dcabb9fe0fee009d7.jpg)  
Fig. 13. Schedule of the example.

The considered routings are shown in Fig. 12, and the current schedule is given in Fig. 13.

Operation P303 on part C uses the horizontal machining center, which is supposed to be out of order for a duration defined by $(0,15,0,15)$ h/100, starting from the date of the beginning of operation.

According to the variable routings, operation P303 can be replaced by operation P319 that uses the lathe. The set-up duration is supposed to be (15,25,5,10) h/100, and the set-up cost (50,50,0,20).

Since there are no available slack times in the schedule, the system suggests two solutions:

(1) the resource replacement;

(2) the maintenance and the return to schedule. P303 duration is 70 h/100, and P319 85 h/100.

Taking into account the costs of the resource use and of the operator, the system provides the following results after propagation of the new durations:

## 4.2.1. Solution 1:

The simulation module gives the following delays:

part A: (170,180,25,10) h/100

part B: 130 h/100

part C: (180,190,35,10) h/100

The maintenance cost is not included, since maintenance is necessary in all cases and it is difficult to affect it to a specific part in direct costs,

part A: 399\$ part B: 503\$

part C: (608,608,0,20)\$.

## 4.2.2. Solution 2:

There is no set-up in that case, but the maintenance duration has to be added to the operation duration.

Delay: part A: (155,170,30,15) h/100

part B: 130 h/100

part C: (165,180,45,15) h/100.

Cost: part A: 399\$ part B: 503\$ part C: 650\$.

The degrees of satisfaction can be calculated as follows:

Cost: $\Pi = N = 1$ for each part in all the cases.

Delay:

$$
\begin{array}{c} \text {part A:} \Pi (O d 1, \text {sol1}) = 1, N (O d 1, \text {sol1}) = 1 \\ \Pi (O d 1, \text {sol2}) = 1, N (O d 1, \text {sol2}) = 0. 8 3 \end{array}
$$

part B: $\Pi = N = 1$ for each solution

$$
\begin{array}{c} \text {part C:} \Pi (O \mathrm{d} 3, \text {sol1}) = 0. 7 3, N (O \mathrm{d} 3, \text {sol1}) = 0. 2 \\ \Pi (O \mathrm{d} 3, \text {sol2}) = 0. 9 4, N (O \mathrm{d} 3, \text {sol2}) = 0. 3 3. \end{array}
$$

The reference to the global objective gives the following results:

— solution 1: $\Pi(O, \text{sol1}) = 0.73$ and $N(O, \text{sol1}) = 0.6$ ;

— solution 2: $\Pi(O, \text{sol2}) = 0.94$ and $N(O, \text{sol2}) = 0.6$ .

The necessity degrees are equal: the two solutions are very close according to the objective satisfaction. Nevertheless, the possibility degree of solution 2 is slightly higher than the one of solution 1: it is better to repair the machining center than to use the lathe.

The various solutions classified according to their possibility and necessity measures provide a basis for the decision making. The workshop manager may prefer not to follow this classification, since he may include occasional constraints which are not integrated in the classification as choice criteria.

This example is very simple and, in such a case, a decision could be made without any support. The full interest of the system appears when the number of machines, the number of jobs in progress, the schedule horizon and the number of degrees of freedom increase.

## 5. Conclusion

Halfway between management and manufacturing levels of production systems, production activity control is a key factor for the efficiency of companies. The reactivity of the PAC system to disturbances is a substantial point in order to insure the flexibility of the production system, but the tools which are now available do not provide a complete solution to the reaction problem. We suggest in this paper a Decision Support System that helps in the integration of the different functions of production activity control, and completes the schedule module of PAC.

In order to provide an efficient help, the key point is certainly to make the implicit workshop objectives explicit. Fuzzy logic may provide efficient tools in that purpose. Moreover, fuzzy logic aspects may be set transparent to the end user by using linguistic labels and modifiers in the front end of the system.

The implementation of this DSS in a real workshop is now in progress, and the first tests have shown the importance of expert knowledge in the workshop management. The “research for solutions” module has been completed by an expert system allowing to take into account imprecise information in order to eliminate some solutions and to implement complex decision makings, such as load re-allocation or sub-contracting management $[13]$ .

## References

[1] O. Wight, Production and Inventory Management in the Computer Age (Cahners Books, Boston, 1974).

[2] G. Doumeingts, D. Darricau and M. Roboam, Design methodology for advanced manufacturing systems, Computers in Industry, 9 (1987), 271–296.

[3] S.A. Melnyk and P.L. Carter, Identifying the Principles of Effective Production Activity Control, 29th International Conference of American Production and Inventory Control Society, St. Louis, MO, 1986, pp. 227–232.

[4] B. Archimède, Conception d'une architecture réactive, distribuée et hiérarchisée pour le pilotage des systèmes de production, PhD Thesis, Université de Bordeaux I, 1991.

[5] P. Huguet and B. Grabot, A conceptual framework for shop-floor production activity control, to be published in the International Journal of Computer Manufacturing (1994).

[6] P. Chen, The entity-relationship model: toward an unified view of data, ACM Transaction on Data Base Systems, 1 (1), (1976).

[7] L. Zadeh, Fuzzy Sets, Information and Control, 8 (1965), 338–353.

[8] D. Dubois and H. Prade, Possibility Theory, an Approach to Computerized Processing of Uncertainty (Plenum Press, New York, 1988).

[9] D. Dubois, H. Prade and C. Testemale, Weighted Fuzzy Pattern Matching, Fuzzy Sets and Systems, 28 (1988).

[10] A. Lehtimäki, A fuzzy decision aid for production control, in: Second IFSA Congress, Tokyo, 1987, July 20–25.

[11] E. Goldratt and J. Cox, The goal (North River Press, New York, 1986).

[12] B. Grabot, A decision support system for variable routings management in manufacturing systems, Fuzzy Sets and Systems, 58 (1993), 87–104.

[13] L. Geneste and B. Grabot, Inférence floue pour l'aide à la décision d'atelier, International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems, Paris, France, July 4–8, 1994.

![](/api/attachments/ZRJY3M5F/fulltext/images/0c466929e44ee2186bca3acebdae5255dde5c5d1b4dec8e2c9a1f94db0c5965b.jpg)

Bernard Grabot is Assistant Professor at the National Engineering School of Tarbes, France. He received a Ph.D. from the University of Bordeaux I in 1988. His research interests are in production management and production activity control, concerning in particular the use of fuzzy logic and possibility theory in decision support systems, performance assessment and scheduling. His articles have appeared in The International Journal of

Production Research, Computer Integrated Manufacturing and Journal of Intelligent Manufacturing.

![](/api/attachments/ZRJY3M5F/fulltext/images/43337d5ee65fd8cf70d76cca640dcd15f1788983ae89ea75683e6f011df63e56.jpg)

Jean-Claude Blanc received an Engineer diploma in Computer Science from INSA (Institut National des Sciences Appliquées, Toulouse, France) in 1980. He is now responsible of the Computer Science Department of the National Engineering School of Tarbes for 10 years, in charge of the implantation and management of software and computer networks in the school. He is involved in research works dealing mainly with decision

support for production systems and simulation.

![](/api/attachments/ZRJY3M5F/fulltext/images/348ec44494b413a6393dbf413b88483625db244fc01fe6626a0367dd9a35158f.jpg)

Chantal Binda received a Master in Economic Sciences from the University of Toulouse I, France, in 1991. She obtained a diploma of Specialised Studies (DESS) in Engineering and Management of Information Systems in 1992, and worked on the development of prototypes of Decision Support System using the Oracle DBMS during her training-course. She is now in charge of data-base applications in the National Engi

neering School of Tarbes.
