---
otero_id: 10062
otero_key: "2FM4MKSK"
title: "On the impact of real-time information on field service scheduling"
authors: "Ioannis Petrakis; Christian Hass; Martin Bichler"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the impact of real-time information on <sup>fi</sup>eld service scheduling

Ioannis Petrakis ⁎, Christian Hass, Martin Bichler

Department of Informatics, TU München, Germany

## a r t i c l e i n f o

Available online 25 January 2012

Keywords: Routing Heuristics Real-time

## a b s t r a c t

Mobile phone operators need to plan and schedule <sup>fi</sup>eld force personnel for maintenance and repair tasks on mobile phone base stations across the country on a daily basis. In this paper, we will introduce the <sup>fi</sup>eld force scheduling problem with priorities. Motivated by the rising popularity of mobile <sup>fi</sup>eld force management solutions, we compare online and of<sup>fl</sup>ine heuristics as well as hybrids to solve the problem. The results help understand the bene<sup>fi</sup>ts of dynamic scheduling based on real-time position information as compared to traditional daily of<sup>fl</sup>ine planning.

© 2012 Elsevier B.V. All rights reserved

## 1. Introduction

Arguably, one of the most important planning problems in many large service organizations is the allocation of employees to tasks. This problem comes in many variants, such as project scheduling, staff scheduling, and rostering [18,9,42]. The assignment of the <sup>fi</sup>eld workforce to tasks that are spatially distributed is different, because the planner needs to take into account travel times and routing constraints.

In this paper, we will focus on a particular task assignment problem, which arises when the mobile workforce has to accomplish spatially distributed tasks with different priorities, deadlines, and skill requirements. As a real-world example, we will use the daily planning problem of a European mobile phone provider. The operator has almost 20,000 mobile phone base stations, which require maintenance and irregular upgrades or need to be repaired immediately in the event of a failure. Several hundred engineers carry out these tasks. Each day, the engineers start at their home location, complete around three to <sup>fi</sup>ve tasks, and return to their home. Each task requires a speci<sup>fi</sup>c skill, and each engineer possesses a number of skills. Tasks also have deadlines and priorities, which depend on the nature of the task (e.g., service-affecting disturbances have high priority compared to regular maintenance). Every morning the scheduler assigns tasks to <sup>fi</sup>eld engineers and suggests a route for the day, which may be later modi<sup>fi</sup>ed. We will refer to this problem as field service scheduling with priorities (FSSP).

The planning problem has similarities with different types of vehicle routing problems (VRP), such as the Multi-Depot Vehicle Routing Problem (MDVRP) [4] or the Pickup and Delivery Problem (PDP) [39]. These problems are NP-hard and can only be solved exactly for rather small instances, as has been shown in experimental analyses [23,24,1]. The FSSP has a number of notable differences to the MDVRP. For example, in each depot only one vehicle (engineer) is located; the same vehicle must be routed each day, resulting in exactly one route for each vehicle and day; the customers (tasks) require skills and have deadlines and associated penalties for violating these deadlines; there are no truck load capacities for each vehicle, but service and travel times as well as hard overtime limits need to be considered instead. Some of these differences have a profound impact on the design of speci<sup>fi</sup>c algorithms to solve the problem.

Priorities and deadlines do not only in<sup>fl</sup>uence the design of an offline algorithm for the planning stage each morning. Urgent tasks arising during the day need to be allocated to a <sup>fi</sup>eld engineer as soon as possible, which causes deviations from the planned schedule. Overall, the computational complexity of the planning problem and the stochastic nature of travel times and service times for individual tasks remains a challenge for respective optimization and decision support systems in industry.

IT solutions have signi<sup>fi</sup>cantly changed <sup>fi</sup>eld service scheduling. Mobile devices and GPS lead to real-time data about the location of <sup>fi</sup>eld force engineers. Having a mobile solution integrated with automated task assignment enables dynamic route scheduling throughout the day, as engineers can be reassigned or rerouted. Software for field service management, also referred to as mobile workforce optimization, combines mobile technology with dynamic scheduling and assignment of tasks [29]. Apart from the manual allocation of tasks to mobile engineers, respective software typically provides rule-based heuristics to automatically route engineers and schedule their tasks. Unfortunately, little is published on dispatching rules and algorithms used for respective dynamic scheduling solutions. In most combinatorial optimization problems, dynamic aspects are not very well studied [39]. However, there have been a number of proposals in the academic literature to handle dynamism in traditional VRPs, ranging from simple assignment rules to solving the planning problem repeatedly (see Section 2).

In this work, we suggest and analyze static (of<sup>fl</sup>ine) and dynamic (online) algorithms to solve the FSSP. Of<sup>fl</sup>ine algorithms generate static routes once a day in the morning, whereas online algorithms can process new tasks arriving throughout the day immediately and update routing schedules in real time. Some of these heuristics are adapted from successful algorithmic approaches to related VRPs.

While different algorithmic approaches will lead to different results, the analysis will provide a better understanding of the benefits of mobile field service management solutions with dynamic scheduling. From a managerial point of view, this should provide evidence whether the introduction of dynamic scheduling solutions lead to significant cost savings or not. The experimental analysis is based on real-world data of a European mobile phone provider, but we conjecture that the situation is representative for other mobile phone providers or other industries with distributed repair and maintenance tasks such as in the utilities industries. The degree of dynamism, i.e., the frequency with which new tasks arrive throughout the day, will be a treatment variable in the experiments.

We will <sup>fi</sup>rst provide a succinct formal problem description of this planning problem in the telecommunication industry. Unfortunately, standard branch-and-cut approaches can only solve very small instances of the problem, as is the case for most large VRPs. Therefore, we will suggest heuristics for the FSSP that can be used to solve the problem statically every morning or dynamically throughout the day, if the tasks are not known a priori. Several heuristics are based on those which have recently been applied successfully for related VRPs. Finally, we will provide the results of an experimental evaluation based on real-world data, in which we compare static, dynamic, and hybrid scheduling approaches, allowing us to evaluate the relative ef<sup>fi</sup>ciency of these approaches. While there are differences among different algorithmic approaches, the main differences stem from the availability of real-time information throughout the day. We will further analyze the robustness of our results and of the different heuristics with respect to different treatments, such as different proportions of urgent tasks or arrival rates.

In contrast to existing literature in vehicle routing, our primary goal is not to develop new algorithmic approaches to solving the problem, but to get an understanding of the efficiency gains of dynamic scheduling made possible by real-time availability of location information about field force engineers as compared to static scheduling at fixed time intervals without such information available. While different scheduling algorithms will lead to somewhat different results, we conjecture that the differences between static and dynamic scheduling will be on the same order of magnitude in similar applications.

The managerial impact of dynamic or static scheduling is substantial. Already in our base scenario the total costs (travel times and deadline penalties) were 2.68 times higher than the costs of the online heuristic. In contrast, for the hybrid heuristic, which imitates a human dispatcher scheduling manually throughout the day, costs were 44% higher than those of the online heuristic in the base scenario. These numbers can change depending on the number of new tasks arriving every day, the number of engineers, and the deadline penalties, which is why we describe a number of different scenarios in our experimental evaluation. Nevertheless, given that the operation of <sup>fi</sup>eld force personnel causes costs in the order of millions of dollars annually for any telecom operator, this decision has signi<sup>fi</sup>cant managerial impact. We show that the savings in operational costs through online scheduling can be substantial, when compared with a pure offline planning solution. A skilled human dispatcher can reduce this cost difference signi<sup>fi</sup>cantly, however.

## 2. Related literature

The FSSP is related to the class of vehicle routing problems (VRP) [7]. A number of variants have been developed over time. In the Multi-Depot Vehicle Routing Problem (MDVRP) a company has several depots from which it may serve customers. The objective is to minimize the vehicle <sup>fl</sup>eet and the sum of travel times. The total demand for commodities has to be served from several depots. The

MDVRP, in particular the version with time windows, has a number of similarities to the FSSP, where the depots are the home locations of engineers and the customers are the tasks in the mobile base stations.

## 2.1. Multi-depot VRPs

There are a number of computational results on the MDVRP often based on benchmark problems [17]. For example, exact solutions have been proposed by [1]. Only instances with 200 customers and <sup>fi</sup>ve depots could be solved within 6 h. Many different heuristic approaches and metaheuristics have been used for the MDVRP, but a detailed review of the different approaches would be beyond the scope of this article. It should be noted, however, that tabu search algorithms are responsible for many good solutions of the benchmark instances mentioned above [4]. More recently, [32] suggested a rather general heuristic for different types of VRPs. These types of VRPs are transformed into a general model and solved using the adaptive large neighborhood search method [37,38].

MDVRPTW is an extension of the MDVRP which allows for time windows. There has been much less research on this problem compared to the general MDVRP. Tabu search has also led to good results for the MDVRPTW [5]. A number of recent advances have been made based on variable neighborhood search heuristics [33,34].

While there are similarities, there are also a number of differences between FSSP and the MDVRPTW. In MDVRPTW all customers need to be visited and the obiective is to minimize the vehicle fleet and travel time. In FSSP, an engineer tries to visit as many tasks as possible (weighted by priority) on the same day with a given <sup>fi</sup>xed number of engineers. All tasks that could not be completed on the same day will be rescheduled with new tasks the next day. In the MDVRPTW the time windows (TW) are binding as they typically correspond to opening hours or time slots agreed with the customer. A schedule visiting a customer outside a time window is infeasible. In FSSP there are no <sup>fi</sup>xed time windows for visiting a base station, but there are penalties for being late. This is sometimes referred to as “soft time windows” in VRPTWs. In MDVRPTW the vehicles may have to wait at the customer's location for the start of the time window. This cannot occur in FSSP as the tasks can be accomplished as soon as they arise and are reported. Other differences are that in FSSP there is only a single vehicle in each depot or home location and there are no load constraints on the vehicle. In contrast, skill sets of different drivers (engineers) need to be considered. Finally, one needs to consider service times for different tasks, which are not always an issue in VRPs. For the design of heuristics these differences matter.

## 2.2. Dynamic VRPs

The dynamic version of the FSSP is a main concern of this paper. Most of the existing VRP research has been focused on problems of a deterministic and static nature. The increasing role of real-time information on traf<sup>fi</sup>c network conditions have all led to a rise in the number of freight and <sup>fl</sup>eet management systems that are operating under dynamic conditions. In dynamic and stochastic routing models, decisions must be made before all information needed is known. Some of the models deal with a priori optimization in which a solution is generated for stochastic problems prior to the receipt of information regarding the realization of its random elements. The general approach is to generate an a priori solution that has the least cost in an expected sense. Other approaches involve making decisions and observing outcomes on a continuous, rolling horizon. [11] reports that very few cases of commercial routing software with dynamic routing are known and most are focused on the design of static routes. Designing a real-time routing algorithm depends to a large extent on the degree of dynamism of the problem as de<sup>fi</sup>ned by [28].

There has been some work on dynamic versions of the VRPs (DVRP) [25] with and without the consideration of time windows but not speci<sup>fi</sup>cally on the dynamic MDVRP. Algorithms can be broadly divided into simple policies or rules, insertion procedures, and metaheuristics. [25] evaluates simple policies such as First Come First Serve or Nearest Neighbor policies based on [2] in a dynamic or partially dynamic setting. Insertion procedures insert new tasks in the best position of the current routes on the basis of a rolling horizon [36] or double horizon [31]. More recent work is based on metaheuristics, where a sequence of static VRPs is solved [16]. A survey of different types of DVRPs and solution concepts can be found in [12]. While the basic problem is different to the FSSP, some approaches to addressing the dynamism can be applied here as well.

## 2.3. Field workforce scheduling by British telecom and commercial off-the-shelf software

British Telecom (BT) has reported on a <sup>fi</sup>eld workforce scheduling project [26,27]. They had to schedule 20,000 engineers and the rulebased scheduling applications from various vendors were not able to address the scale and the complexity of the requirements. BT therefore developed a heuristic based on constraint-based reasoning and simulated annealing. They reported a saving of \$150 million per annum on engineer, and controller, and other workforce-related costs, such as vehicles, equipment, tools, training, and administration. Unfortunately, little has been published on the details of the algorithms and the respective experimental results. Also, the BT problem focused on engineers with customer interaction and therefore has a number of characteristics that are beyond the FSSP. For example, some tasks needed to be completed within an agreed-upon time window, as access to customer premises may be granted only to certain individuals at certain times. Furthermore, task duration depended on the engineer's experience and skills. Also, some tasks had to be sequenced in time or had to be performed in parallel.

As indicated in the introduction, nowadays there are several commercial software packages focusing on <sup>fi</sup>eld service management [29], but little is known about the dispatching rules and algorithms used. A notable exception is IBM/Ilog Dispatcher, which is based on constraint programming [19]. While constraint programming is a powerful approach to generating many good feasible solutions, we aim for a single “best” proposal every morning in the of<sup>fl</sup>ine setting.

## 3. The <sup>fi</sup>eld service scheduling with priorities problem

The FSSP can be described as follows: a number of n spatially distributed tasks must be served exactly once by one of m engineers. Engineers have one shift and accomplish one tour per day. They start their tours from their particular home bases, visit locations to ful<sup>fi</sup>ll particular tasks, and return back home. Each tour has a soft and a hard time limit. Soft time limits cause additional costs (overtime), whereas hard time limits must not be broken. The assignment of a task to an engineer is only possible if the engineer has a certain skill required by the task. Each task has a duration (service time) and its service must begin prior to its due date (deadline), otherwise penalty costs are charged (deadline penalties). The priority of a task is re<sup>fl</sup>ected by its “penalty factor”; hence the deadline penalties of a task are calculated by the time of delay multiplied by its penalty factor.

The goal of the FSSP is to minimize the sum of the following three goals:

1. Transportation costs measured by the total travel time (in minutes),

2. Deadline penalties, measured by the sum over all delayed tasks deadline penalties (delay time in minutes multiplied by the penalty factor),

3. Overtime costs, measured by the total overtime (in minutes).

All three goals have minutes as the unit of measure. The delay time of high-priority tasks is however multiplied by a penalty factor greater than one to account for the fact that violation of these deadlines is less preferable to the mobile phone provider compared to additional travel time. There is a large body of literature on multi-objective optimization, and several ways on how the objective function could be designed. The objective function introduced below was designed according to practical considerations

We now formalize the Field Service Scheduling with Priorities (FSSP) as a mixed integer program in order to provide a succinct formal description of the problem. Our problem formulation assumes full information setting (i.e. the service times of the tasks and their report dates are known in advance). Hence the solution represents the ex-post optimal solution. We consider a multigraph $G = \{ V , E \}$ , where the vertex set is divided into two disjoint subsets $V = \{ D , C \}$ . Set $D =$ $\{ 0 , 1 , . . m - 1 \}$ represents the locations of the engineers' homes. The set of engineers coincides with the set D as each engineer has his own home location. Set $C = \{ 0 , 1 , . . n - 1 \}$ represents the tasks' locations. T denotes the set of days. $E = \{ ( i , j ) ^ { k , t } \}$ with $i , j \in V , k \in D , t \in T$ and $i \neq j$ is the arc set and $c _ { i j } = c _ { j i }$ the travel time from i to j. We assume symmetric and Euclidean distances among different locations. $R ^ { s o f t }$ denotes a soft time limit of a tour in hours. If the soft limit is exceeded, overtime is calculated. $R ^ { h a r d }$ de<sup>fi</sup>nes a hard time limit of a tour. Its violation is not allowed by any means. $S = \{ s _ { 0 } , s _ { 1 } , . . . s _ { m a x } \}$ denotes the whole skill set and $S _ { k }$ S the skill set of engineer k. The skill required by task i is $s _ { i \cdot }$ Let $s _ { k , i } = 1$ if and only if $s _ { i } \in S _ { k }$ , that is if and only if the engineer k possesses the skill that task i requires, otherwise $s _ { k , i } = 0$ . Symbol $p _ { i } , i { \in } C$ denotes the penalty factor of task i and $d _ { i } , i \in C ,$ , denotes the service time that an engineer must spend to complete it. The shift start of all engineers on day t is $b _ { t \cdot }$ The time when a task is reported, i.e. when it becomes known, is $e _ { i } , i { \in } C . \mathrm { A s }$ the formulation assumes a full information setting, this time coincides with the earliest possible start time of servicing the task. The deadline of a task i is denoted by l . The decision variables $a _ { i } , i \in C ,$ , represent the arrival time at task i. The binary decision variables $x _ { i j k t } , i \in V ,$ $j \in V , k \in D , t \in T$ are equal to 1 if and only if the engineer k on day t travels from node i direct to node j. Finally, the symbol $\{ \cdot \} ^ { + }$ is equivalent to max{∙,0}.

$$
\begin{array}{l} \min \Big (\sum_ {i \in V} \sum_ {j \in V} \sum_ {k \in D} \sum_ {t \in T} c _ {i j} x _ {i j k t} + \sum_ {i \in C} \{(a _ {i} - l _ {i}) \} ^ {+} p _ {i} \\ \quad + \sum_ {k \in D} \sum_ {t \in T} \sum_ {i \in C} \sum_ {j \in D} \Big \{\Big (a _ {i} + d _ {i} + c _ {i j} - \Big (b _ {t} + R _ {\text {soft}} \Big) \Big) x _ {i j k t} \Big \} ^ {+} \Big) \end{array}\tag{1}
$$

s.t.

$$
\sum_ {i \in V / \{j \}} \left(x _ {i j k t} - x _ {j i k t}\right) = 0 \quad \forall j \in V, k \in D, t \in T\tag{2}
$$

$$
\sum_ {j \in C} x _ {i j i t} \leq 1 \quad \forall i \in D, t \in T\tag{3}
$$

$$
\sum_ {j \in C} x _ {i j k t} = 0 \quad \forall i \in D, k \in D / \{i \}, t \in T\tag{4}
$$

$$
\sum_ {i \in V} \sum_ {k \in D} \sum_ {t \in T} x _ {i j k t} = 1 \quad \forall j \in C\tag{5}
$$

$$
\sum_ {t \in T} \left(1 - s _ {k j}\right) x _ {i j k t} = 0 \quad \forall i \in V, j \in C, k \in D\tag{6}
$$

$$
e _ {i} \leq a _ {i} \quad \forall i \in C\tag{7a}
$$

$$
a _ {j} \geq \left(b _ {t} + c _ {i j}\right) x _ {i j i t} \quad \forall i \in D, j \in C, t \in T\tag{7b}
$$

$$
a _ {j} \geq \left(a _ {i} + d _ {i} + c _ {i j}\right) x _ {i j k t} \quad \forall i \in C, j \in C, k \in D, t \in T\tag{7c}
$$

$$
\left(a _ {i} + d _ {i} + c _ {i j}\right) x _ {i j j t} \leq b _ {t} + R _ {\text { hard }} \quad \forall i \in C, j \in D, t \in T\tag{7d}
$$

$$
x _ {i j k t} \in \{0, 1 \} \quad \forall i \in V, j \in V, k \in D, t \in T.\tag{8}
$$

The objective function (1) is the sum of travel time, deadline penalties, and overtime. Flow conservation constraint (2) ensures that an engineer entering a task or a home location is leaving it too. Constraint (3) ensures that every home location can be left only once each day. Constraint (4) is necessary for the assignment of engineers to their homes. Constraint (5) ensures that each task is visited exactly once. Constraint (6) is the skill constraint. Constraint (7a) ensures that the arrival time at a task will be after the task has been reported. Constraints (7b) and (7c) ensure that the arrival time of an engineer at task j is after his departure time from his previous location plus the travel time from the previous location to task j. Constraint (7d) ensures that the duration of a tour doesn't exceed a prede<sup>fi</sup>ned amount. Separate sub-tour elimination constraints are not necessary since the calculation of arrival times (Constraints (7a)–(7d)) provide comparable functionality as node-potential-based sub-tour elimination constraints, initially proposed by [30] for the Traveling Salesman Problem and used by [22] for the Multi-Depot Vehicle Routing Problem. Constraint (8) imposes binary values for the <sup>fl</sup>ow variables x . This problem formulation has similarities to the multi-depot vehicle routing problem [3,4,6].

Note that the formulation can be easily transformed into a MIP. The objective function can be rewritten without the symbol $\{ \cdot \} ^ { + }$ and the multiplication of decision variables in the third summand. For this, we introduce auxiliary variables $z _ { i } , i \in C$ and $o _ { j t } , j { \in } D , t { \in } T$ for the delay time of a task and the overtime of an engineer on a given day respectively.

$$
\min \left(\sum_ {i \in V} \sum_ {j \in V} \sum_ {k \in D} \sum_ {t \in T} c _ {i j} x _ {i j k t} + \sum_ {i \in C} z _ {i} p _ {i} + \sum_ {k \in D} \sum_ {t \in T} o _ {k t}\right)\tag{1'}
$$

$$
a _ {i} \leq l _ {i} - z _ {i} \forall i \in C\tag{9}
$$

$$
\sum_ {i \in C} \left(a _ {i} + d _ {i} + c _ {i j} - b _ {t} - R _ {\text { soft }}\right) x _ {i j j t} \leq o _ {j t} \forall j \in D, t \in T\tag{10}
$$

$$
z _ {i} \geq 0 \forall i \in C\tag{11}
$$

$$
o _ {j t} \geq 0 \forall j \in D, t \in T\tag{12}
$$

The non-linear Constraints (7c) and (7d) can be easily linearized too, since $x _ { i j k t }$ is binary [8]. Let M be a large constant. Then Eqs. (7c) and (7d) can be rewritten as:

$$
a _ {i} + d _ {i} + c _ {i j} - a _ {j} \leq \left(1 - x _ {i j k t}\right) M \forall i \in C, j \in C, k \in D, t \in T\tag{7c'}
$$

$$
a _ {i} + d _ {i} + c _ {i j} - b _ {t} - R _ {\text { hard }} \leq \left(1 - x _ {i j j t}\right) M \forall i \in C, j \in D, t \in T.\tag{7d'}
$$

We have implemented the formulation with CPLEX 12.2, but could only solve some problems with up to 3 engineers and 12 tasks in about an hour. But we also found instances of same size which caused “out of memory” exceptions. We used an Apple iMac Core i7 2.93 GHz, model end of 2010.

## 4. Heuristics for the FSSP

Due to limited scalability of exact branch-and-cut approaches and the tight time limits for scheduling which is performed every morning, we will now focus on heuristics to solve the FSSP. Several of these heuristics are inspired by successful approaches to solving VRPs. We distinguish three types: of<sup>fl</sup>ine, online, and hybrid heuristics. Of<sup>fl</sup>ine (or static) heuristics create a plan only once in the morning and do not change it during the day. Online (or dynamic) heuristics assign the tasks dynamically throughout the day. Hybrid heuristics combine both approaches. An initial plan is created in the morning which can be changed during the day, but only if urgent tasks arise. Task duration and the arrival of new tasks over time are the stochastic elements of FSSP which heuristics need to consider. We work with estimates of service times and travel times rather than modeling the problem as a stochastic optimization problem.

We have implemented a number of custom algorithms based on successful heuristics for the TSP and VRP problems and also customized meta-heuristics for the FSSP, in order to <sup>fi</sup>nd out if some approaches dominate others. Our implementation is available upon request.

## 4.1. Objective function used in the heuristics

Every heuristic which compares costs incurred by the different candidate solutions (i.e., sets of routes) it generates, uses the objective function presented above as the evaluation function with a main adjustment. This is necessitated by the fact that, unlike classic VRPs, in FSSP the solution of each heuristic must be evaluated on a daily basis, as routes are generated daily. In contrast to other VRPs there is no constraint that every task must be visited. Therefore, solutions to a heuristic might just postpone all tasks and thus minimize travel and overtime costs. However, <sup>fi</sup>eld force engineers are available and the planner should try to use their time ef<sup>fi</sup>ciently each day. In this paper, we will introduce costs for tasks that remain unassigned each day, so-called unassignment costs. These costs are added to the evaluation function. Details on the individual parameters for our experiments will be speci<sup>fi</sup>ed in Section 5.

4.2. Least Insertion Costs (LIC) and Conditional Least Insertion Costs (CLIC)

Tour-building insertion heuristics have been widely used for VRPs [40]. The next task to be assigned is selected by means of a selection criterion, while the insertion criterion determines the best position for insertion [41]. Our insertion heuristic for the FSSP, Least Insertion Costs (LIC), sorts the tasks according to their due dates (selection criterion) and inserts them one by one in the position where the insertion costs are minimal (insertion criterion). Let $\Delta _ { t } ^ { e }$ denote the insertion costs de<sup>fi</sup>ned as the additional costs incurred by inserting task t between two adjacent nodes in engineer e's route in the best position. The best position is the one where the additional costs are minimal over all possible insertion positions within the route of engineer e. Possible insertion positions are between two adjacent nodes. We set $\Delta _ { t } ^ { e } = \infty$ if task t cannot be inserted in the route of e (due to skill or overtime constraints). The task t is inserted in the route of the best engineer: $e ^ { * } = \arg \operatorname* { m i n } _ { { } } ( e ) ( \varDelta _ { t } ^ { e } )$ . The costs of a route are calculated by using the evaluation function described in Section 4.1.

Conditional Least Insertion Costs (CLIC) is a variant of LIC, whereby the pre<sup>fi</sup>x “Conditional” refers to the fact that it ignores a task from the actual daily planning if its unassignment costs are lower than its actual insertion costs to the best possible route. Thus, the visit of a task will be postponed until the day when an engineer passes close enough to the task or the task becomes urgent. In contrast, without this condition, LIC assigns tasks whenever it is possible.

## 4.3. Opportunity Costs (OC, aka Regret — 3)

The OC heuristic, based on Ropke and Pisinger's k-Regret algorithm [38], sorts the tasks in descending order according to their opportunity costs and sequentially inserts them at their lowest-cost insertion position, like LIC. Opportunity costs (regret measures) try to predict what will be lost if a given task is not immediately inserted within its best route [35] and in the simplest case they are equal to the difference in insertion costs between the second best and the best route. Note that each route is assigned to an engineer, which means that opportunity costs are also a measure to be decided among engineers. A generalized regret measure considering every alternative, e.g. not only the difference between the second best and the best route but also between the third best and the best route, has been used by Potvin and Rousseau for the VRPTW [35]. We implemented a variant of this regret measure which considers differences between the three best engineers, since in our FSSP instances the tasks can in most cases be assigned to one of the three best engineers: $\begin{array} { r } { 0 \mathsf C ( t ) = \sum _ { h = 2 } ^ { 3 } \left( \Delta _ { t } ^ { h } - \Delta _ { t } ^ { 1 } \right) } \end{array}$ , where $\Delta _ { t } ^ { h }$ denotes the insertion costs of task t to the route of its h-best engineer (an engineer has one route per day). Considering more than three would weaken the “opportunity costs” notion of the measure. I $\mathsf { f } \ \Delta _ { t } ^ { 3 }$ or $\Delta _ { t } ^ { 2 }$ are in<sup>fi</sup>nite, our heuristic does not consider them, but adds a constant value such that all tasks with fewer available engineers have higher opportunity costs and thus are preferred. The reason is that these tasks are more “constrained” and if their assignment is postponed, it may become impossible to assign all of them.

The original k-Regret heuristic was designed for VRP problems without due dates and penalty costs. Hence, we extended our heuristic to take these FSSP-speci<sup>fi</sup>c properties into account. Our algorithm divides all tasks into three sets according to their due dates, and then applies a separate run of the default OC algorithm on each of them. During the <sup>fi</sup>rst run only the most urgent tasks with a deadline of less than 24 h are considered. The second run processes tasks with a deadline expiring during the next 2 days. Finally all remaining tasks are considered.

## 4.4. Heuristic based on the linear assignment problem (LAP)

The nonlinear generalized assignment problem has been used by VRP heuristics for clustering purposes. After the clustering phase, the routing phase constructs routes by solving the TSP in each cluster [10]. Our heuristic follows a new approach: it uses the well-known linear version of the assignment problem<sup>1</sup> to directly construct routes instead of the two-phase approach, which is not applicable to the FSSP without extensive modi<sup>fi</sup>cations (due to multiple depots, priorities, and skills). In each iteration the LAP is ef<sup>fi</sup>ciently solved using the Hungarian Algorithm [21] and each engineer is assigned maximally one task. Afterwards, his current position is updated according to his assigned task's position. The costs of an assignment of a task to an engineer are set to the travel time between the current position of the engineer and the position of the task. If an engineer doesn't possess the skill to perform a task or his overtime after the assignment exceeds the limit of 30 min, costs are set to in<sup>fi</sup>nity. The tasks are classi<sup>fi</sup>ed in due-date time intervals (e.g., 4 h, 10 h, 1 day, 3 days, all) with the <sup>fi</sup>rst one consisting of tasks of utmost urgency. During the <sup>fi</sup>rst run only tasks having a due date ending in 4 h are considered. During the second run tasks of the second interval are considered and so on. The granularity of the due-date time intervals directly in<sup>fl</sup>uences to which extent the deadlines vs. the travel times are optimized.

## 4.5. Hybrid heuristic (HOC)

As a mixture between of<sup>fl</sup>ine and online heuristics, we implemented a hybrid one which simulates the behavior of a dispatcher, who plans routes in the morning and schedules urgent tasks on demand throughout the day. This resembles the process in many companies: i) the dispatcher interferes only when new urgent tasks emerge. Urgent tasks are those with a due date within 24 h; ii) the dispatcher can request the current position of an engineer; iii) the dispatcher always tries to assign incoming urgent tasks to the closest engineer possessing the required skill; iv) if overtime restrictions are violated, the dispatcher will postpone other tasks from the engineer's schedule to the next day. For initial routes HOC is based on the OC algorithm, due to the fact that OC outperformed other heuristics without timeconsuming post-optimization.

## 4.6. Post-optimization: Variable Neighborhood Search (VNS)

Each heuristic that constructs tentative routes can additionally apply post-optimization to further improve the solution. Postoptimization can be conducted on the initial schedule in the morning and whenever the routes change in an online setting. We implemented a Variable Neighborhood Search (VNS) [15], as there are a number of positive results in the recent literature [33]. For example, VNS outperformed all other methods in an analysis of MDVRPTW, which is closely related to FSSP. The use of a variety of neighborhoods enables a wide exploration of the search space and requires much fewer parameters than for example tabu search [13,14].

We implemented three types of the VNS which differ in the level of randomness regarding the search: basic VNS, Variable Neighborhood Descent (VND), and Reduced VNS (RVNS). As RVNS has shown to be better than the other VNS types on almost every simulation run, we will only report on RVNS in this paper (Table 4-1). During the “shaking” step of each iteration, RVNS randomly chooses a neighbor. But in contrast to basic VNS, no local search is applied (hence the name Reduced VNS) and the move is carried out if it leads to an improvement. This virtue proved to be decisive for our FSSP instances, making RVNS the best post-optimization variant.

We now provide a succinct description of RVNS and comment on our concrete implementation for the FSSP. As already mentioned, RVNS uses a variety of neighborhoods. A neighborhood of solution x contains every solution reachable by the unique application of one operator on x. An operator prescribes one or more moves to be applied on one or more routes of a solution. A move can be the deletion of a task of a route, the insertion of a (previously unassigned) task to a route, or the relocation or the swapping of tasks on an inter-route basis, i.e. between different routes and not within a single route. $N _ { k } ( x )$ denotes the k-th neighborhood of the solution x $( k = 1 . . k _ { m a x } )$

We implemented 15 neighborhoods, which are described in Appendix A. Their ordering can affect the performance of the search [20]. The ordering which performed best in our experiments is based on the success rate of the neighborhoods and their size. When routes and tasks need to be selected in order to generate a new solution, only routes and tasks located in close vicinity are considered. By the calculation of distances between routes or a route and a task location, the center of gravity of the routes is used. The center of gravity coordinates of a route are de<sup>fi</sup>ned as the average coordinates of the nodes it includes (the start and end-node are considered as two separate nodes although they coincide). After the successful move from one solution to another, the TSP is solved to further improve the affected routes. Note that the TSP uses the objective function outlined in Section 4.1. Our implementation of RVNS stops after either the maximum running time or the maximum time since the last improvement is reached.

## 4.7. Online heuristics

All heuristics can operate both in of<sup>fl</sup>ine and online modus. In the online mode though, adjustments are necessary in order to dynamically handle new incoming tasks. Tentative routes are generated every morning and updated through the day when a new task is reported. Firstly, the online heuristics try to insert the new task in its lowest-cost insertion position. If this is impossible, for example because these routes cannot be extended any more within a day, the online heuristics try to replace another task with this one. This is only done if costs actually decrease. Hence, when the new task is urgent, it is very likely to be exchanged with a non-urgent one. If a heuristic also implements the RVNS post-optimization, the routes which are affected from the insertion of the new task as well as further routes in close proximity are post-optimized for a limited amount of time. Considering further non-affected routes is meaningful since the VNS prescribes inter-route neighborhoods and does not merely optimize each route separately.

<table><tr><td>Table 4-1RVNS following Hansen et al. [15].</td></tr><tr><td>Initialization:Select the set of the neighborhood structures  $N_{k}, k=1,...,k_{max}$  which will be used in the searchFind an initial solution xChoose a stopping condition (e.g. maximum total running time, maximum time since last improvement, maximum iterations, etc.)Repeat the following until the stopping condition is met:Set  $k=1$ Until  $k=k_{max}$  repeat the following steps:Shaking: Generate a point  $x'$  at random from the neighborhood  $N_{k}(x)$ Move or not. If  $x'$  is better than the incumbent  $x$ , set  $x=x'$  and  $k=1$ ; otherwise set  $k=k+1$ </td></tr></table>

## 5. Research design and data

In this section we report on the design of experiments based on a dataset from our mobile phone provider. The dataset contains the locations of 19,258 base stations, where tasks may emerge, and the home locations of 177 technicians. We used travel time estimates between two locations based on the Euclidean distance multiplied by an estimated average speed of 50 km/h, which has also been used by our industry partner in the past. The service times were stochastic and heuristics worked with the expected value.

The tasks in the dataset were classi<sup>fi</sup>ed in four categories determined by their nature and the given service level agreements on which their due dates, priorities, and time windows are based (see Table 5-1). The time windows indicate when the tasks can be reported.<sup>2</sup>

There are also <sup>fi</sup>ve types of skills. Tasks require a particular skill, while engineers possess particular skills (Fig. 5-1).

Skill 0 is required by all tasks which are incidents. The remaining skills concern planned work like integration or maintenance.

This led to the following independent variables in our experiments:

i. Position of the tasks and their report dates,

ii. the mean and standard deviation of workload, which is de<sup>fi</sup>ned by the number of tasks per engineer and day, and is normally distributed,

iii. the mean and standard deviation of the duration of tasks which is normally distributed and

iv. the percentage of high priority tasks which belong to category I (high priority).

Based on these independent variables we de<sup>fi</sup>ned eight treatment combinations or scenarios and conducted 20 repetitions with each of them (Table 5-2). The task positions and their arrival times are chosen randomly for each repetition and all other parameters are <sup>fi</sup>xed in a scenario. One repetition simulates 14 days with new tasks throughout the day, but is extended up to 30 days until all tasks of the <sup>fi</sup>rst 2 weeks are <sup>fi</sup>nished.

Table 5-1

<table><tr><td>Task category</td><td>Due date</td><td>Penalty factor</td><td>Time window</td><td># Tasks</td></tr><tr><td>(I) Service-affecting incident</td><td>4 h</td><td>10</td><td>00:00–24:00</td><td>5%</td></tr><tr><td>(II) Non-service-affecting incident</td><td>24 h</td><td>5</td><td>00:00–24:00</td><td>45%</td></tr><tr><td>(III) Service-affecting planned work</td><td>7 days</td><td>10</td><td>08:30–16:00</td><td>14%</td></tr><tr><td>(IV) Non-service-affecting planned work</td><td>7 days</td><td>1</td><td>08:30–16:00</td><td>36%</td></tr></table>

Scenario-0 (base scenario): the base scenario describes the parameters that could also be found in the data set of our industry partner. All 177 engineers are involved. Their shifts last from 08:00 am to 4:30 pm and during 1 day each worker has an average of four tasks to complete. The duration of the tasks is drawn from a normal distribution with a mean of 90 min and a standard deviation of 15 min. Therefore, the targeted utilization level of the engineers is 71% (90 min×4/8,5 h). The number of tasks is normally distributed with a standard deviation of 50 tasks (\~7%). The percentages of tasks belonging to each category can be found in Table 5-1.

Scenario-1 (increased workload): to analyze the characteristics of the heuristics under high workload, we increased the average number of tasks per engineer and day to <sup>fi</sup>ve tasks. The targeted utilization level is 88%. The spatial distribution of the tasks has a signi<sup>fi</sup>cant impact on the utilization.

Scenario-2A (low variability of task duration): the standard deviation for drawing the real task duration is set to 1 min, instead of 15 min in the base scenario. In other words, task duration is very predictable.

Scenario-2B (high variability of task duration): in contrast to Scenario-2A, the deviation of the service time is now increased to 30 min.

Scenario-3 (high variance of the number of tasks per day)

In this scenario the variance of the number of tasks per day is increased (standard deviation of 150 tasks). It can happen that the engineers cannot be fully occupied in 1 day due to a lack of available tasks and another day they may not be able to keep up with the workload. Such <sup>fl</sup>uctuations can happen if operators want to carry out a large number of technical updates on the base stations in one period, or due to weather conditions.

Scenario-4A (20% urgent tasks with high priority): the percentage of high priority tasks (service-affecting incidents) is increased from 5% to 20%. Thus the degree of dynamism of the scenario increases drastically, as more tasks are reported during the day and require immediate attention. This is a very relevant scenario for the mobile phone operator as the percentage of disturbances may increase drastically due to weather or other conditions.

Scenario-4B (40% urgent tasks with high priority): the percentage of high priority tasks is further increased to 40%.

Scenario-5 (More tasks but shorter service time): this scenario differs substantially from the others as it contains many more tasks with shorter service durations. The number of tasks per day is doubled and the service duration reduced to 30 min. The targeted utilization level is only 47% while the distance to be covered by the engineers increases. We want to understand if the results of the initial scenarios carry over to workforce scheduling problems, where each traveling employee completes many short tasks per day.

To calculate the unassignment costs in our experiments, we assume that each unassigned task will be visited in 24 h (which may lead to additional deadline penalties) and cause 100 min of additional travel time.

![](/api/attachments/2FM4MKSK/fulltext/images/c9d7fa6bd066333f6f96bb5d949651993f24e363035cb009b90769f9adc5f774.jpg)  
Fig. 5-1. Skill distribution among task categories and engineers.

These values could be further optimized by using past data, e.g. by calculating the average additional travel time per task. Additionally, if the overtime of a route exceeds 30 min, the costs of the routes are set to in<sup>fi</sup>nity in order to avoid routes with larger overtime. Of course, the <sup>fi</sup>nal overtime after executing a plan may exceed 30 min due to the fact that the real task duration deviates from the estimate.

## 6. Results

To evaluate our computational results we use the objective function introduced in Section 3. In addition to the objective function values, we report on travel time and deadline penalties individually when appropriate. The calculation of deadline penalties is based on the delay and category of each task (see Section 3). We tested dozens of heuristics and heuristic combinations (e.g. next neighbor algorithms with different proximity measures which consider both spatial distance and deadlines or only one of them, cluster <sup>fi</sup>rst route second algorithms, and RVNS, VNS, VND with different parameters and different initial solutions such as OC, LAP, etc.), but due to space restrictions we report only on the results of the best ones. The net computation time needed to run the presented experiments was 1660 h on eight identical PCs (Intel Core 2, 2.67 GHz, 4 GB).

Table 5-2  
Independent variables in different scenarios (values different from base scenario underlined)

<table><tr><td>Scenario</td><td>#  $tasks^a$ </td><td>σ # $tasks^b$ </td><td>Task duration</td><td>σ task duration</td><td>Cat. I  $tasks^c$ </td><td>Description</td></tr><tr><td>0</td><td>4</td><td>50</td><td>90 min</td><td>15 min</td><td>5%</td><td>Base scenario</td></tr><tr><td>1</td><td rowspan="2">5/4</td><td>50</td><td>90 min</td><td>15 min</td><td>5%</td><td>Increased workload</td></tr><tr><td>2A</td><td>50</td><td>90 min</td><td>1 min</td><td>5%</td><td>More certainty about task duration</td></tr><tr><td>2B</td><td>4</td><td>50</td><td>90 min</td><td>30 min</td><td>5%</td><td>Less certainty about task duration</td></tr><tr><td>3</td><td>4</td><td>150</td><td>90 min</td><td>15 min</td><td>5%</td><td>Higher variance of tasks per day</td></tr><tr><td>4A</td><td>4</td><td>50</td><td>90 min</td><td>15 min</td><td>20%</td><td>Increased urgent high priority tasks</td></tr><tr><td>4B</td><td>4</td><td>50</td><td>90 min</td><td>15 min</td><td>40%</td><td>Increased urgent high priority tasks</td></tr><tr><td>5</td><td>8</td><td>50</td><td>30 min</td><td>15 min</td><td>5%</td><td>More tasks but lower task duration</td></tr></table>

<sup>a</sup> Average number of tasks per engineer and day.  
b σ means standard deviation of a normally distributed variable.  
<sup>c</sup> Cat. I tasks are urgent tasks with high priority.

Table 6-1  
Of<sup>fl</sup>ine heuristics' averages on the base scenario

<table><tr><td>Heuristic</td><td>Obj. function value</td><td>Travel time</td><td>Penalties</td></tr><tr><td>OCnRVNS</td><td>1,660,387</td><td>247,921</td><td>1,391,598</td></tr><tr><td>OC</td><td>1,702,559</td><td>282,729</td><td>1,393,506</td></tr><tr><td>CLIC</td><td>1,756,122</td><td>333,360</td><td>1,391,620</td></tr><tr><td>LAP</td><td>1,799,679</td><td>379,067</td><td>1,400,126</td></tr><tr><td>LIC</td><td>1,813,992</td><td>382,308</td><td>1,396,385</td></tr></table>

## 6.1. Overall comparison: online vs. offline vs. hybrid

Firstly, we note that there are dominant relationships among the heuristics across all repetitions in the sense that the rank of each particular heuristic stays mostly the same from repetition to repetition (the corresponding diagram can be found in Appendix B). This observation underpins the robustness of the results.

Table 6-1 provides an overview of the average values of the of<sup>fl</sup>ine heuristics in the base scenario and Table 6-2 of the online and hybrid heuristics. The unit of measure is minutes, as explained in Section 3.

Of<sup>fl</sup>ine heuristics lead to much higher costs (i.e. objective function values) than the online heuristics. The costs of the hybrid heuristic are close to the costs of the online heuristics. Compared to the best of<sup>fl</sup>ine heuristic, HOC incurs only 39% of its costs and dominates it in every metric, including running times (see Appendix C). The largest part of the costs in of<sup>fl</sup>ine heuristics, around 80% on average, is due to deadline penalties, which cannot be avoided because new and urgent tasks emerging throughout the day could not be considered immediately. In contrast, online heuristics incur much lower penalties and hence the largest part of their costs is due to travel time. Although one could expect travel time to increase in online heuristics, as deadlines of urgent tasks need to be considered, the travel times of OC, LAP, and LIC are even lower in the online setting of the base scenario.

We will now compare the best online heuristic, OCnRVNS,<sup>3</sup> the best of<sup>fl</sup>ine heuristic, which is again OCnRVNS, and the hybrid heuristic, HOC. The comparison is conducted on the base scenario and on scenarios 4A and 4B, where the percentage of urgent high priority tasks (category I) increases. This change should have a considerable impact on the comparison between the of<sup>fl</sup>ine, hybrid, and the online heuristics.

As depicted in Fig. 6-1, the gap between the costs of the heuristics widens as the degree of dynamism increases in scenarios 4A and 4B. The costs incurred by the hybrid heuristic are 44% higher than the online heuristic in the base scenario and 100% higher in scenario 4B. The costs of the of<sup>fl</sup>ine heuristic are already 2.68 times higher than the costs of the online heuristic in the base scenario. The travel times and deadline penalties are also provided in Table 6-3.

The hybrid and the online heuristic have almost identical travel times. The travel time of the of<sup>fl</sup>ine heuristic slightly increases as the proportion of urgent high-priority tasks increases. In scenario 4B it has a 7.5% higher travel time than the online heuristic. The online heuristic has by far the lowest deadline penalties. Even in the base scenario it produces only half of the penalties of the hybrid and 13% of the of<sup>fl</sup>ine

Table 6-2  
Online and hybrid heuristics' averages on the base scenario.

<table><tr><td>Heuristic</td><td>Obj. function</td><td>Travel time</td><td>Penalties</td></tr><tr><td>OCnRVNS</td><td>451,900</td><td>248,027</td><td>186,128</td></tr><tr><td>LICnRVNS</td><td>452,629</td><td>252,616</td><td>182,231</td></tr><tr><td>OC</td><td>498,557</td><td>274,609</td><td>203,923</td></tr><tr><td>LAP</td><td>546,295</td><td>367,659</td><td>162,445</td></tr><tr><td>LIC</td><td>582,115</td><td>351,028</td><td>211,044</td></tr><tr><td>HOC</td><td>649,475</td><td>245,707</td><td>388,621</td></tr></table>

## Objective function, best off line vs best online vs hybrid

![](/api/attachments/2FM4MKSK/fulltext/images/a1b516ea9efad50ba4604e69f8153f5c59f809762975699f3cde9206eb9486fc.jpg)  
Fig. 6-1. Objective function of best online, best of<sup>fl</sup>ine, and hybrid heuristic.

heuristic. As the number of high priority tasks increases, the penalty gap between the online and the other two heuristics widens.

The runtime of the of<sup>fl</sup>ine heuristics without post-optimization was 8 min at most in the base scenario, while the of<sup>fl</sup>ine RVNS heuristic lasted 64 min. Longer runtimes of the RVNS did not improve the results signi<sup>fi</sup>cantly. The online heuristics without post-optimization lasted at most 30 min and the online RVNS heuristics 172 min (that is about 12 min per simulated day in an analysis simulating 14 days). All running times can be found in Appendix C.

We will now examine the performance of the of<sup>fl</sup>ine and online heuristics separately.

## 6.2. Offline heuristics in the base scenario

Fig. 6-2 illustrates the performance of the of<sup>fl</sup>ine heuristics on the base scenario with regard to each component of the objective function. The percentages, to the right of the bars, represent the deviation<sup>4</sup> of each heuristic's objective function value from the value of the best of<sup>fl</sup>ine heuristic.

The best heuristic is the one with post-optimization (OCnRVNS) followed by its version without post-optimization (OC). Their lower costs are mainly due to their shorter travel times, although the travel time accounts for only 20% of the total costs. The deadline penalties do not vary signi<sup>fi</sup>cantly from heuristic to heuristic; the worst heuristic with respect to penalties deviates only 0.61% from the best one. This also demonstrates the dif<sup>fi</sup>culty of further decreasing deadline penalties in the of<sup>fl</sup>ine world without knowledge about future tasks and leads to a low improvement of the total cost from OC to OCnRVNS (2.54%), which is ascribed only to the decrease in travel time.

## 6.3. Comparison of offline heuristics in different scenarios

In the following we analyze whether the results of the base scenario carry over to other scenarios. Table 6-4 compares the performance of the heuristics as deviation from the best ones (marked as 0.00%) in each scenario.

Table 6-3  
Travel time and penalties of best online, best of<sup>fl</sup>ine, and hybrid heuristic. In brackets are the changes in % in comparison to OCnRVNS (of<sup>fl</sup>ine).

<table><tr><td rowspan="2">Heuristic</td><td colspan="3">Travel time</td><td colspan="3">Penalties</td></tr><tr><td>0</td><td>4A</td><td>4B</td><td>0</td><td>4A</td><td>4B</td></tr><tr><td>OCnRVNS (offline)</td><td>247,921</td><td>253,179</td><td>264,764</td><td>1,391,598</td><td>5,529,457</td><td>10,900,636</td></tr><tr><td>HOC (hybrid)</td><td>245,707(0.9↓)</td><td>250,641(1.0↓)</td><td>250,868(5.3↓)</td><td>388,621(72.1↓)</td><td>1,461,296(73.6↓)</td><td>3,223,505(70.6↓)</td></tr><tr><td>OCnRVNS (online)</td><td>248,027(0.0↑)</td><td>247,633(2.2↓)</td><td>246,471(6.9↓)</td><td>186,128(86.6↓)</td><td>697,929(87.9↓)</td><td>1,478,210(86.4↓)</td></tr></table>

OCnRVNS always performs best followed either by the OC or the CLIC. Note that the ranking of the heuristics OCnRVNS>OC>CLI-C>LAP>LIC (“>” denotes “performs better than”) can be found in all scenarios except 1 and 4B, where OCbCLIC. CLIC always outperforms LIC, which advocates the usage of unassignment costs. This is important, since unassignment costs are also extensively used in the post-optimization.

Fig. 6-3 depicts for each scenario the average changes across all repetitions compared to the base scenario.

The 25% increase in the number of tasks in scenario 1 leads to a 30% increase in the objective function compared to the base scenario. In scenario 2A the objective function value decreases by 3%, which is due to savings produced by the lower variance of the task duration. In contrast, in scenario 2B, the objective function increases by 3%. In scenario 3 the stronger variance in the number of tasks per day leads to a 3% increase in total costs. When the volume of very urgent tasks (deadlines in 4 h) increases to 20% and 40% (instead of 5%) in scenarios 4A and 4B respectively, the objective function values increase by 237% and 548% respectively. This is a result of the fact that tasks with short deadlines cannot be considered immediately when planning tasks of<sup>fl</sup>ine every morning. Finally, in scenario 5 the objective function value increases on average by 81% due to the dif<sup>fi</sup>culty of handling in time the increased number of tasks (96% increase in deadline penalties). Travel time only increases by 30%.

## 6.4. Online heuristics

Fig. 6-4 depicts the performance of the online heuristics relative to each other in the base scenario 0.

Two groups of heuristics can be identi<sup>fi</sup>ed. The <sup>fi</sup>rst group consists of heuristics with post-optimization, which dominate the second group of heuristics without post-optimization. OC is the best heuristic of the second group and deviates about 10% from the <sup>fi</sup>rst group. The contribution of post-optimization in the online world is therefore four times higher than in the of<sup>fl</sup>ine world (10.32% vs. 2.54%). In contrast to the of<sup>fl</sup>ine setting, online heuristics optimize routes not only in the morning but during the whole day.

![](/api/attachments/2FM4MKSK/fulltext/images/c8e66053dd3c1c483a617e0995dd48b936e203c08c5dc1abe33fc145b9addad6.jpg)  
Fig. 6-2. Of<sup>fl</sup>ine heuristics, base scenario.

Table 6-4  
Deviations (in %) from best heuristic, of<sup>fl</sup>ine heuristics, all scenarios.

<table><tr><td>Deviations of objective function</td><td>0</td><td>1</td><td>2A</td><td>2B</td><td>3</td><td>4A</td><td>4B</td><td>5</td><td>Average</td></tr><tr><td>LIC</td><td>9.25%</td><td>6.55%</td><td>9.18%</td><td>9.36%</td><td>9.06%</td><td>2.86%</td><td>2.09%</td><td>7.74%</td><td>4.82%</td></tr><tr><td>CLIC</td><td>5.77%</td><td>2.76%</td><td>5.69%</td><td>5.87%</td><td>5.91%</td><td>1.61%</td><td>1.04%</td><td>2.92%</td><td>2.59%</td></tr><tr><td>OC</td><td>2.54%</td><td>15.99%</td><td>2.51%</td><td>2.61%</td><td>2.61%</td><td>0.74%</td><td>1.07%</td><td>0.90%</td><td>2.43%</td></tr><tr><td>OCnRVNS</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>LAP</td><td>8.39%</td><td>11.48%</td><td>8.87%</td><td>7.95%</td><td>7.84%</td><td>2.29%</td><td>1.81%</td><td>10.77%</td><td>5.05%</td></tr></table>

Underlined entries indicate the best solutions and bold are percentages below 2%.

![](/api/attachments/2FM4MKSK/fulltext/images/54834e5ef45e08815cca75c3ab57b268d21a357b3bc0c42ddaa3c100a795f28e.jpg)  
Fig. 6-3. Of<sup>fl</sup>ine heuristics, average changes in scenarios.

Interestingly, the quality of the start solution has little impact on the <sup>fi</sup>nal solution when using post-optimization. The two RVNS heuristics yield almost the same results although the starting solution of OC is better than the starting solution of LIC.

With respect to travel time, the best heuristics are again the ones with the RVNS post-optimization and the best one of the remaining heuristics is the OC. The worst heuristic is LAP due to its due-time intervals that put an emphasis on deadlines. This is the reason why this heuristic has the lowest deadline penalties.

## 6.5. Comparison of online heuristics in different scenarios

Again, we compare the robustness of the results by analyzing scenarios 1 to 5. Table 6-5 shows the performance of the heuristics in terms of deviation from the best result.

In the online setting, the best heuristics are always the ones with post-optimization, whereby OCnRVNS achieves the best result in all but two scenarios. The best heuristic without post-optimization on average is the OC, as in the of<sup>fl</sup>ine setting.

Fig. 6-5 depicts for each scenario the average changes across all heuristics and repetitions compared to the base scenario.

![](/api/attachments/2FM4MKSK/fulltext/images/14f970c9b95bd6cd4994c53389e4c7e3b3691db1d00ba45cd8fd0261aa6e7e36.jpg)  
Fig. 6-4. Online heuristics, base scenario.

In scenario 1 the number of tasks increases by 25% and leads to an average increase of 62% in the objective function value due to the high increase in deadline penalties. In scenario 2A the objective function value decreases by 13% while in 2B it increases by 18%. These values were higher than with of<sup>fl</sup>ine heuristics. Hence, the accurate prediction of the task duration is more important in an online setting. The reason is presumably that in the online world the information about the real duration of a task, which is revealed upon task completion, can be exploited by adjusting the remaining schedule of the tour. In scenario 3, the stronger variance of the number of tasks leads to an increase of 4%. In scenarios 4A and 4B, which prescribe more high priority tasks, total costs increase by 106% and 273% respectively. These numbers are much lower than in the of<sup>fl</sup>ine setting. In scenario 5, the objective function value stays almost the same, whereas in the of<sup>fl</sup>ine setting it increases by 81%. Therefore, the online heuristics can handle scenarios with many more tasks of short duration much better.

## 7. Conclusions

Maintenance and repair jobs at base stations of mobile phone operators lead to a widespread planning problem in the telecom industry. This problem has not been described in the literature, but is a special case of vehicle routing problems as can be found in other service industries as well. Nowadays, mobile <sup>fi</sup>eld service scheduling solutions are available on the market which provide real-time information about the location of each engineer and allow for dynamic scheduling of tasks throughout the day. In this paper, we want to understand the ef-<sup>fi</sup>ciency gains of having this information available as compared to daily of<sup>fl</sup>ine scheduling every morning, which is a widespread practice.

For this purpose, we <sup>fi</sup>rst de<sup>fi</sup>ned the <sup>fi</sup>eld service scheduling problem with priorities (FSSP) as a mixed integer program and described its relation to other vehicle routing and planning problems. FSSP has similarities to the Multi-Depot Vehicle Routing Problem with Time Windows, but also distinct differences which have an impact on the design and the performance of the heuristics in solving the problem. We introduced a variety of of<sup>fl</sup>ine and online heuristics for this new problem, which are based on successful approaches to other vehicle routing problems. These algorithms were evaluated based on a real-world data set and on different scenarios in order to understand the robustness of the results.

Changes in scenarios 1 to 3 (online)  
Table 6-5  
Deviations (in %) from best heuristic, online heuristics, all scenarios.

<table><tr><td>Deviations of objective function</td><td>0</td><td>1</td><td>2A</td><td>2B</td><td>3</td><td>4A</td><td>4B</td><td>5</td><td>Average</td></tr><tr><td>LAP</td><td>20.89%</td><td>4.61%</td><td>32.04%</td><td>3.36%</td><td>10.32%</td><td>5.04%</td><td>9.34%</td><td>25.81%</td><td>10.83%</td></tr><tr><td>LIC</td><td>28.81%</td><td>49.56%</td><td>33.64%</td><td>15.77%</td><td>22.00%</td><td>23.90%</td><td>24.82%</td><td>9.88%</td><td>25.83%</td></tr><tr><td>OC</td><td>10.32%</td><td>18.97%</td><td>8.80%</td><td>3.09%</td><td>6.95%</td><td>9.98%</td><td>7.20%</td><td>10.22%</td><td>8.88%</td></tr><tr><td>OCnRVNS</td><td>0.00%</td><td>0.85%</td><td>0.00%</td><td>2.67%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>LICnRVNS</td><td>0.16%</td><td>0.00%</td><td>2.00%</td><td>0.00%</td><td>0.28%</td><td>2.84%</td><td>1.01%</td><td>1.18%</td><td>0.67%</td></tr></table>

Underlined entries indicate the best solutions and bold are percentages below 2%.

![](/api/attachments/2FM4MKSK/fulltext/images/c5de57afd5f6e76e73edae0b4b935f04cb887b2776777f0d13397dedff109b0b.jpg)

![](/api/attachments/2FM4MKSK/fulltext/images/979ed456ace2ea3d51a7bb9ec2b5fd352b95ed1f52522756d20b8941b13bc88b.jpg)  
Fig. 6-5. Online heuristics, average changes in scenarios.

The best heuristics were the ones adding the post-optimization heuristic Reduced Variable Neighborhood Search (RVNS), which outperformed other post-optimization routines (such as basic VNS and VND). The contribution of RVNS was also signi<sup>fi</sup>cant in the online world, where deadline penalties were lower. RVNS improved the best heuristic (OC) by more than 10% and other heuristics such as LIC by more than 25%. The results were robust against modi<sup>fi</sup>cations of the base scenario.

The best of<sup>fl</sup>ine and online heuristics were compared to each other and to a hybrid heuristic. The results of this comparison indicate that online heuristics lead to substantially lower costs than pure of<sup>fl</sup>ine heuristics, which is also due to the deadline penalties in our objective function. Even without such penalties the differences are signi<sup>fi</sup>cant. Travel times are often also lower when using online heuristics.

Interestingly, the hybrid heuristic achieves considerably lower total costs than the of<sup>fl</sup>ine heuristics. It is close to the costs of online heuristics, especially when the degree of dynamism is low. The hybrids simulate the planning process in companies where all routes are planned in the morning, but a dispatcher assigns urgent tasks. This indicates that if a skilled dispatcher is available in a company which plans the routes once a day and assigns urgent jobs throughout the day, the savings in travel and overtime costs might be lower and an operator needs to weigh the investment and maintenance costs for the mobile workforce management solution and the costs of manual intervention. In mobile workforce management systems, the effort of the human dispatchers will be much reduced, as urgent tasks are handled and assigned automatically. Note that additional costs for introducing and maintaining mobile <sup>fi</sup>eld service scheduling systems or manual dispatching have not been considered in this paper as they tend to vary considerably and we only focus on ef<sup>fi</sup>ciency gains in routing the engineers. These costs are typically known at the time of deciding between a mobile <sup>fi</sup>eld service scheduling and a manual dispatching solution. Our study can help in calculating each business case by providing estimates of the ef<sup>fi</sup>ciency gains of one system over the other.

## Appendix A. Neighborhoods in RVNS

Our neighborhoods are divided into two large categories, depending on whether they are allowed to change the status of a task from unrouted (i.e. not yet planned in a route) to routed (and vice versa) or not. The <sup>fi</sup>rst category is labeled $\ " \mathrm { U R } ^ { \prime \prime }$ (Unrouted, Routed) and the second with “IR” (Inter-Route). In the following Table A-1, the neighborhoods together with their size are listed (m denotes the number of unassigned tasks considered, k the number of tasks in a route, and R1, R2, R3 denote routes). As already mentioned, the routes considered by a neighborhood are selected randomly. As a <sup>fi</sup>rst exemplary calculation of the size, consider the neighborhood UR1\_Insert\_1. We have m unassigned tasks which can be inserted at k possible positions. Hence its size is ${ \bf O } ( { \bf k } \times { \bf m } )$

Table A-1. Neighborhoods

<table><tr><td>UR1_Insert_1</td><td>Insert one unrouted task to R1</td><td> $O(k \times m)$ </td></tr><tr><td>UR1_Remove_1</td><td>Remove a routed task from R1</td><td> $O(k)$ </td></tr><tr><td>UR1_Swap_1</td><td>Remove a routed task from R1 and insert an unrouted task to R1</td><td> $O(k^2 \times m)^a$ </td></tr><tr><td>UR1_Swap_2</td><td>Remove two routed tasks from R1 and insert two unrouted tasks to R1</td><td> $O(2 k^3 \times m^2)^b$ </td></tr><tr><td>UR1_Swap_21</td><td>Remove one routed task from R1 and insert two unrouted tasks to R1</td><td> $O(2 k^2 \times m^2)$ </td></tr><tr><td>UR1_Swap_12</td><td>Remove two routed tasks from R1 and insert one unrouted task to R1</td><td> $O(k^3 \times m)$ </td></tr><tr><td>UR2_Relocate_1</td><td>Insert an unrouted task to R1, move a task from R1 to R2</td><td> $O(k^2 \times m)$ </td></tr><tr><td>UR2_Swap_1</td><td>Insert an unrouted task to R1, move a task from R1 to R2, remove a task from R2</td><td> $O(k^3 \times m)$ </td></tr><tr><td>IR2_Relocate_1</td><td>Move a task from R1 to R2</td><td> $O(k^2)$ </td></tr><tr><td>IR2_Swap_1</td><td>Move a task from R1 to R2 and a task from R2 to R1</td><td> $O(k^3)$ </td></tr><tr><td>IR2_Relocate_2</td><td>Move two tasks from R1 to R2</td><td> $O(k^2)$ </td></tr><tr><td>IR2_Swap_2</td><td>Move two tasks from R1 to R2 and two tasks from R2 to R1</td><td> $O(k^5)$ </td></tr><tr><td>IR2_Swap_12</td><td>Move one task from R1 to R2 and two tasks from R2 to R1</td><td> $O(k^4)$ </td></tr><tr><td>IR3_Relocate_1</td><td>Move a task from R1 to R2 and a task from R2 to R3</td><td> $O(k^3)$ </td></tr><tr><td>IR3_Swap_1</td><td>Move a task from R1 to R2, a task from R2 to R3 and a task from R3 to R1</td><td> $O(k^4)$ </td></tr></table>

<sup>a</sup>Note that the insertion position of the unrouted task must not be the position of the task to be removed. This holds for every neighborhood where tasks are swapped.  
<sup>b</sup>Exemplary calculation: selection of two routed tasks costs O(k<sup>2</sup>), selection of two unrouted tasks $0 ( \mathrm { m } ^ { 2 } ) ,$ then the two unrouted tasks are inserted O(k+k) (the insertions occur sequentially and each one costs O(k)), all together O(k<sup>2</sup> x m<sup>2</sup> $\textbf { x } 2 \textbf { k } ) =$ ${ \sf { O } } ( { \sf { k } } ^ { 3 } { \mathrm { ~ x ~ m } } ^ { 2 } )$

## Appendix B. Performance of all heuristics on the twenty repetitions of base scenario

The intention of the plot (Figure B-1) is to analyze the robustness of the results across the 20 repetitions of the base scenario. It can be ob served that the rank of each particular heuristic stays mostly the same from repetition to repetition. Most line intersections are due to the two RVNS heuristics, which perform very similarly since the initial solution (OC or LIC) is not decisive in our setting.

![](/api/attachments/2FM4MKSK/fulltext/images/63dbb047e99c85bcbb72754d4986e5140e86b2cc9ec85d778db39f546e63c998.jpg)  
Figure B-1: 20 repetitions of the base scenario.

## Appendix C. Additional results

Table C-1. Running times in seconds

<table><tr><td colspan="9">Running time in s</td></tr><tr><td></td><td>0</td><td>1</td><td>2A</td><td>2B</td><td>3</td><td>4A</td><td>4B</td><td>5</td></tr><tr><td>CLIC (off)</td><td>161.45</td><td>449.55</td><td>153.05</td><td>161.85</td><td>219.00</td><td>174.05</td><td>183.15</td><td>1747.10</td></tr><tr><td>LIC (off)</td><td>190.30</td><td>412.25</td><td>181.70</td><td>190.95</td><td>233.55</td><td>207.60</td><td>209.90</td><td>1673.00</td></tr><tr><td>LAP (off)</td><td>483.10</td><td>1334.40</td><td>474.35</td><td>483.85</td><td>604.65</td><td>466.40</td><td>437.80</td><td>926.75</td></tr><tr><td>OC (off)</td><td>491.05</td><td>1263.20</td><td>483.15</td><td>483.80</td><td>587.00</td><td>502.30</td><td>529.65</td><td>1685.95</td></tr><tr><td>HOC</td><td>1251.35</td><td>2379.50</td><td>1266.60</td><td>1252.75</td><td>1379.10</td><td>1279.20</td><td>1314.85</td><td>3836.00</td></tr><tr><td>LIC (on)</td><td>1339.00</td><td>1988.10</td><td>1235.55</td><td>1312.90</td><td>1458.75</td><td>1388.20</td><td>1405.60</td><td>4602.10</td></tr><tr><td>OC (on)</td><td>1390.45</td><td>3096.95</td><td>1383.35</td><td>1366.40</td><td>1586.10</td><td>1412.15</td><td>1423.65</td><td>4502.45</td></tr><tr><td>LAP (on)</td><td>1742.55</td><td>4414.45</td><td>1628.20</td><td>1722.75</td><td>2137.70</td><td>1701.45</td><td>1719.05</td><td>4273.30</td></tr><tr><td>OCnRVNS (off)</td><td>3722.00</td><td>5050.45</td><td>3714.95</td><td>3712.60</td><td>3924.70</td><td>3742.50</td><td>3802.70</td><td>4957.20</td></tr><tr><td>OCnRVNS (on)</td><td>9569.40</td><td>17,413.60</td><td>9329.80</td><td>9887.85</td><td>10,659.55</td><td>9758.80</td><td>9436.05</td><td>16,252.75</td></tr><tr><td>LICnRVNS (on)</td><td>9684.35</td><td>16,941.45</td><td>9398.60</td><td>9962.25</td><td>10,840.45</td><td>9810.90</td><td>9374.25</td><td>15,932.30</td></tr></table>

Remark on Table C-1: the running time of the online heuristics depends on how long the operations regarding a new incoming task last. For the insert operation we allowed at most two seconds and for the possible swap operation four seconds (see Section 4.7). The post-optimization routine, used by two of the online heuristics, was in this case restricted to the affected route and routes in close proximity and lasted two seconds. Hence the online handling of a new task lasted at most eight seconds. Further results can be provided by the <sup>fi</sup>rst author.

## References

[1] R. Baldacci, A. Mingozzi, A uni<sup>fi</sup>ed exact method for solving different classes of vehicle routing problems, Mathematical Programming 120 (2009) 347–380.

[2] D. Bertsimas, G. Van Ryzin, A stochastic and dynamic vehicle routing problem in the Euclidean plane, Operations Research 39 (1991) 601–615.

[3] L. Bodin, A. Assad, M. Ball, Routing and scheduling of vehicles and crews — the state of the art, Computers and Opertions Research, Special Issue 10 (2) (1983) 63–212.

[4] J.-F. Cordeau, M. Gendreau, G. Laporte, A tabu search heuristic for periodic and multi-depot vehicle routing problems, Networks 30 (1997) 105–119.

[5] J.F. Cordeau, G. Laporte, A. Mercier, An improved tabu search algorithm for the handling of route duration constraints in vehicle routing problems with time windows, Journal of the Operational Research Society 55 (2004) 542–546.

[6] T.G. Crainic, G. Laporte, Fleet Management and Logistics, Kluwer Academic Publishers, 1998.

[7] G.B. Dantzig, J.H. Ramser, The truck dispatching problem, Management Science 6 (1959) 80–91.

[8] J. Desrosiers, Y. Dumas, M.M. Solomon, F. Soumis, Time constrained routing and scheduling, in: M.O. Ball, C.L. Monma, G.L. Nemhauser (Eds.), Handbooks in Operations Research and Management Science 8: Network Routing, Elsevier Science Publishers, Amsterdam, 1995, pp. 35–139.

[9] A.T. Ernst, H. Jiang, M. Krishnamoorthy, D. Sier, Staff scheduling and rostering: a review of applications, methods and models, European Journal of Operationa Research 153 (2004) 3–27.

[10] M. Fisher, M. Jaikumar, A generalized assignment heuristic for vehicle routing, Networks 11 (1981) 109-124

[11] T. Flatberg, G. Hasle, O. Kloster, E.J. Nilssen, A. Riise, Dynamic and stochastic vehicle routing in practice, Dynamic Fleet Management, Operations Research/Computer Science Interfaces, Springer, 2007, pp. 45–68.

[12] G. Ghiani, F. Guerriero, Real-time vehicle routing: solution concepts, algorithms and parallel computing strategies, European Journal of Operational Research 15 (2003) 1–11.

[13] F. Glover, Tabu search — part I, ORSA Journal on Computing 1 (1989) 190–206.

[14] F. Glover, Tabu search — part II, ORSA Journal on Computing (1990) 4–32.

[15] P. Hansen, N. Mladenovic, Variable neighborhood search: principles and applications, Journal of Operational Research 130 (2001) 449–467.

[16] F.T. Hanshar, B.M. Mobuki-Berman, Dynamic vehicle routing using genetic algorithms, Applied Intelligence 27 (2007) 89–99.

[17] HEC Montreal, www.hec.ca/chairedistributique/data2010.

[18] C. Heimerl, R. Kolisch, Scheduling and staf<sup>fi</sup>ng multiple projects with a multiskilled workforce, OR Spectrum (2009) 1–26.

[19] P. Hofstedt, A. Wolf, Einführung in die Constraint-Programmierung, Springer, Berlin, Heidelberg, 2007.

[20] B. Hu, G.R. Raidl, Variable neighborhood descent with self-adaptive neighborhood-ordering, Proceedings of the 7th EU/MEeting on Adaptive, Self Adaptive, and Multi-Level Metaheuristics, Malaga, Spain, 2006.

[21] H.W. Kuhn, The Hungarian method for the assignment problem, Naval Research Logistic Quarterly, vol. 2, 1955, pp. 83–97.

[22] R.V. Kulkarni, P.R. Bhave, Integer programming formulations of vehicle routing problems, European Journal of Operational Research 20 (1985) 58–67.

[23] G. Laporte, Y. Nobert, D. Arpin, Optimal solutions to capacitated multidepot vehicle routing problems, Congressus Numerantium 44 (1984) 283–292.

[24] G. Laporte, Y. Nobert, S. Taillefer, Solving a family of multi-depot vehicle routing and allocation problems, Transportation Science 22 (1988) 161–172.

[25] A. Larsen, O. Madsen, M. Solomon, Partially dynamic vehicle routing — models and algorithms, Journal of the Operational Research Society 38 (2002) 637–646.

[26] D. Lesaint, C. Voudouris, N. Azarmi, Dynamic workforce scheduling for British Telecommunications plc, Interfaces 30 (2000) 45–56.

[27] D. Lesaint, C. Voudouris, N. Azarmi, I. Alletson, B. Laithwaite, Field workforce scheduling, BT Technology 21 (2003) 23–26.

[28] K. Lund, O. Madsen, J.M. Rygaard, Vehicle Routing Problems with Varying Degrees of Dynamism, Insititute of Mathematical Modelling, Technical University of Denmark, 1996.

[29] M. Maoz, Magic Quadrant for Field Sevice Management, Gartner Research, 2008.

[30] C.E. Miller, A.W. Tucker, R.A. Zemlin, Integer programming formulation, Journal of the ACM 7 (1960) 326–329.

[31] S. Mitrovic-Minic, R. Krishnamurti, G. Laporte, The double-horizon heuristic for the dynamic pickup and delivery problem with time windows, Transportation Science 38 (2004) 669–685.

[32] D. Pisinger, S. Ropke, A general heuristic for vehicle routing problems, Computers and Operations Research 34 (2007) 2403–2435.

[33] M. Polacek, R.F. Hartl, K. Doerner, A variable neighborhood search for the multi depot vehicle routing problem with time windows, Journal of Heuristics 10 (2004) 613–627.

[34] M. Polacek, S. Benkner, K. Doerner, R.F. Hartl, A cooperative and adaptive variable neighborhood search for the multi depot vehicle routing problem with time win dows, Business Research 1 (2008) 207–218.

[35] J.Y. Potvin, J.M. Rousseau, A parallel route building algorithm for the vehicle routing and scheduling problem with time windows, European Journal of Operational Research 66 (1993) 331–340.

[36] H. Psaraftis, Dynamic vehicle routing problems, Vehicle Routing: Methods and Studies, Elsevier, North-Holland, 1988, pp. 223–248.

[37] S. Ropke, D. Pisinger, A uni<sup>fi</sup>ed heuristic for a large class of vehicle routing problems with backhauls, European Journal of Operational Research 171 (2004) 750–775.

[38] S. Ropke, D. Pisinger, An adaptive large neighborhood search heuristic for the pickup and delivery problem with time windows, Transportation Science (2006) 455–472.

[39] M. Savelsbergh, M. Sol, The general pickup and delivery problem, Transportation Science 29 (1995) 17–29.

[40] M. Solomon, Algorithms for the vehicle routing and scheduling problems with time window, Operations Research 35 (1987) 254–265.

[41] A. Van Breedam, A parametric analysis of heuristics for the vehicle routing problem with side-constraints, European Journal of Operational Research 137 (2002) 348–370.

[42] M.C. Wu, S.H. Sun, A project scheduling and staff assignment model considering learning effects, International Journal of Advanced Manufacturing Technology 28 (2006) 1190–1195.

![](/api/attachments/2FM4MKSK/fulltext/images/d4de332806bf81c0d2641c5be74ce3622d27b6828fbf87d81f71c23144e37eef.jpg)

Ioannis Petrakis studied Electrical and Computer Engineering at the National Technical University of Athens. He then followed the Elite Graduate Program “Finance and Information Management” at the TU München and received his MSc with honors. He is currently working as a full-time research assistant at the Chair of Decision Sciences & Systems (DSS) of the TU München. His <sup>fi</sup>elds of interest include mechanism design, vehicle routing and data mining.

![](/api/attachments/2FM4MKSK/fulltext/images/19a7c9607ea0a83d01a359114faef15b87ae4ea533256b58cc03b6ee2ce5c4f0.jpg)

Christian Hass studied Information Systems at the TU München where he received his Bachelor of Science and later on his Master of Science. In his Master Thesis he analyzed and benchmarked linear (LP) solvers for the combinatorial allocation problem. Since September 2008 Christian has been working as a full-time research assistant at the Chair of Decision Sciences & Systems (DSS) of the TU München.

![](/api/attachments/2FM4MKSK/fulltext/images/8d0d7c9398d9dc6a9fbaeed602a9ca4ac80e3b42aae8fc7037d2e7a18ad038d5.jpg)

Martin Bichler is a full professor at the Department of Informatics at the TU München. He received his MSc in Information Systems from the Technical University of Vienna and his Ph. D. as well as his Habilitation from the Vienna University of Economics and Business Administration. Martin was working as a research fellow at UC Berkeley and as a research staff member at the IBM T. I Watson Research Center, New York. He has been involved in research and development in the areas of auction design, operations research, and information systems design
