---
otero_id: 21325
otero_key: "JR3D6M5T"
title: "Decision-making algorithms in two-level complex operation system"
authors: "Jerzy Józefczyk"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00098-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision-making algorithms in two-level complex operation system

Jerzy Jo´zefczyk\*

Institute of Control and Systems Engineering, Wroclaw University of Technology, Janiszewski St. 11/17, 50-370 Wroclaw, Poland

Available online 15 August 2003

## Abstract

A two-level manufacturing operation system composed of two interconnected subproblems, i.e. scheduling of independent, non-preemptive tasks on unrelated moving executors as well as motion control of a group of moving executors performing the tasks is investigated. As the performance index of the two-level system, the makespan is assumed. Three heuristic solution algorithms for the two-level system are presented. The first algorithm ensures the current modification of solutions for the scheduling subproblem during the decision procedure of the two-level system. In the second one, an iterative approach is applied, which consists in successive implementation of the solution algorithms for both subproblems. The third algorithm uses on-line procedure, which enables determination of the best solution in the current step of the decision procedure. Comparisons of the algorithms as well as a numerical example are also presented. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Scheduling; Simulation; Decision-making systems; Flexible manufacturing systems; Vehicle scheduling

## 1. Introduction

For complex operation systems composed of operations (tasks, jobs), which are mainly characterized by execution times, different decision-making problems are solved including scheduling and allocation. It is assumed that the execution times for tasks are not given a priori but they are direct or indirect results of solving the decision-making problems, which consist in controlling the execution of tasks under consideration. Taking into account the control of task execution in operation system makes it more complex on the one hand and closer to reallife applications on the other hand. Complex manufacturing systems like flexible manufacturing systems are the main application area for systems under consideration. In such systems, the movement of different elements should be taken into account and, roughly speaking, the movement is the subject of control. The movement of plants to be produced as well as the movement of executors being the performers of technological tasks can be distinguished as the most important cases. Further investigation will be confined to the second case. Then, each task consists of two parts: driving-up of the executor towards the plant to perform the job (transportation task) and the execution of the job to forward the performance of the plant (technological task). Both parts should be controlled. One can easily notice that two decision-making subproblems, i.e. solving the selected subproblem for operation system and control of the execution of tasks are interconnected. It is convenient to describe them in the form of a two-level decision-making system. The first subproblem being the more strategic one is placed at the upper level. For such a general and complex problem, particular decision-making subproblems can be generated and investigated as well as different solution algorithms can be derived and applied. The idea of the two-level decision-making system for complex manufacturing operation system has been first introduced in Ref. [2]. It corresponds to the development of the area of complex operation systems, e.g. Refs. [1,11 – 13].

Now, it is assumed that task scheduling is considered as the upper level decision-making subproblem. Moreover, at the lower level, only the motion of executors is investigated and the control of job performance is not taken into account (Fig. 1). The subproblems from both levels taken separately have been intensively studied and described in detail in numerous papers, e.g. Refs. [2 –7,10]. The presentation as well as evaluation of solution algorithms both exact and approximate can be found therein.

The main objective of the paper is to present and compare via computer simulation three approximate decision-making algorithms for a two-level system. The description of algorithms for subproblems is omitted. The selected results of the computer simulation, which verifies the solution algorithms for the two-level systems, are also given. In the next section the problem is stated. Then, in Section 3, heuristic control algorithms are presented. Section 4 comprises results of the computer simulation. Final remarks complete the paper.

![](/api/attachments/JR3D6M5T/fulltext/images/3b1a507f595559db216ed7c9716589026116a409f35091b3aa60c68999c2d02c.jpg)  
Fig. 1. Two-level complex operation system with scheduling of tasks and motion control of a group of executors.

## 2. Problem formulation

The decision-making problem for the two-level system is stated as the optimization problem. This formulation is preceded by a short presentation of the subproblems from both levels.

## 2.1. Upper level subproblem

The movement of executors, which is taken into account, makes the scheduling problems more difficult. It leads to problems of task scheduling with moving executors, which can be treated as a general ization of classical scheduling problems. In order to explain more precisely the idea of task scheduling with moving executors the main notions will now be introduced. The basic notion is the task, which can be understood like in the scheduling theory but having its own meaning by reason of the fact that the movement of executors is taken into account. The executor is usually a technological device, which performs tasks at a place called workstation located on the plane or in space. From among all workstations, a depot is distinguished, where each executor starts and ends its work, and where no task is performed. The main idea of the generalized scheduling problem under consideration is the following. To perform the task the executor should drive-up to the workstation. Therefore, each task is twofold and consists in driving-up to the workstation and performing of $\mathrm { ~ a ~ } j o b$ at this workstation. Generalizing the term ‘task’ leads to generalization of execution times, which are the main data for every scheduling problem. Then the execution time is the sum of the driving-up time and the time the job is performed. Such a generalization defines a new scheduling problem in which not only a subset of tasks for each executor should be derived but also the routes of executors are to be determined. The neces sity of determining the routes results from the fact that the order of performing tasks by an executor has an influence on the quality of scheduling for the whole set of tasks. Versions with moving executors can be formulated and solved for all known classical sched uling problems. In the paper, a simple scheduling problem with independent, non-preemptive tasks and unrelated executors as well as the same ready times is considered. However, it deals with the situation when each executor to perform the job should drive-up to a

place (workstation), where this job should be done. All assumptions made for the classical scheduling problem are valid. For example, each task can be performed by one executor only. Moreover, it is assumed that at every workstation only one task can be performed and each executor should begin and end its movement at a common workstation called the depot for executors (the depot). No distinction between the set of tasks and the set of workstations in notation is introduced. Both sets are denoted by $H = \{ 1 , 2 , \dots . . , H \}$ where H is the number of tasks and workstations. Among workstations, the depot for executors is distinguished. It is the workstation where no job is performed and that is the beginning and the end of the route of each executor. The depot is denoted by $h = H + 1$ . Then $\pmb { \bar { H } } = H \cup \{ H + 1 \}$ is the set of workstations with the depot. Analogously, R and R are the set of executors and the number of executors, respectively. The execution time $\tau _ { h }$ of the task h is the Rdimensional vector with elements $\tau _ { r , h }$ . These elements are the execution times of the task h performed by different executors $r { \in } R .$ . The individual time $\tau _ { r , h }$ is the sum of the time $\overline { { \tau } } _ { r , h }$ the job h is performed at workstation h by the executor r and the driving-up time $\hat { \tau } _ { r , g , h }$ the executor r reaches the workstation h from the other workstation g. Consequently, the following equation holds $\tau _ { r , h } = \bar { \tau } _ { r , h } + \hat { \tau } _ { r , g , h } .$ . To formulate the scheduling problem in terms of the optimization, let us define a decision variable as a threedimensional binary matrix

where

$$
\gamma = \left[ \gamma_ {r, g, h} \right] _ {\substack {r = 1,2,\ldots ,R \\ g,h = 1,2,\ldots ,H + 1}},
$$

$$
\gamma_ {r, g, h} = \left\{ \begin{array}{l l} 1, & \text { if   executor } r \text { performs   task } h \text { after   driving - up   from   workstation } g, \\ 0, & \text { otherwise. } \end{array} \right.
$$

As a performance index, the makespan is used

$$
Q (\gamma) = \max _ {r = 1, 2, \dots , R} \left\{\sum_ {h = 1} ^ {H + 1} \sum_ {g = 1} ^ {H + 1} \gamma_ {r, g, h} \left(\bar {\tau} _ {r, h} + \hat {\tau} _ {r, g, h}\right) \right\}.\tag{1}
$$

ð3Þ

For the decision matrix $\gamma ,$ the following constraints are imposed

ð2Þ

$$
\gamma_ {r, h, h} = 0, r \in \boldsymbol {R}, h \in \bar {\boldsymbol {H}},\tag{4}
$$

$$
\sum_ {r = 1} ^ {R} \sum_ {g = 1} ^ {H + 1} \gamma_ {r, g, h} = 1, h \in \boldsymbol {H},
$$

$$
\gamma \in S,\tag{5}
$$

where

$$
\boldsymbol {S} = \left\{\gamma : \sum_ {g \in \bar {\boldsymbol {H}} _ {S}} \sum_ {h \in \bar {\boldsymbol {H}} _ {S}} \gamma_ {r, g, h} \leq \bar {H} _ {S} - 1, \right.
$$

$$
\left. \bar {\boldsymbol {H}} _ {S} - \text { any   non - empty   sub - set   of } \bar {\boldsymbol {H}}, r \in \boldsymbol {R} \right\},
$$

$$
\sum_ {g = 1} ^ {H + 1} \gamma_ {r, g, p} = \sum_ {h = 1} ^ {H + 1} \gamma_ {r, p, h}, r \in \boldsymbol {R}, p \in \bar {\boldsymbol {H}},
$$

$$
\sum_ {h = 1} ^ {H} \gamma_ {r, H + 1, h} = 1, r \in \boldsymbol {R}.\tag{6}
$$

They ensure that each task is executed as well as the routes for executors are continuous, form the Hamiltonian cycle and have no subcycles. The admissible matrix $\gamma$ contains information about routes of executors, which being the essential result of solving the upper level problem, can be denoted by the elements of matrix c, which are equal to one [10]. Such elements for fixed $r , r = 1 , 2 , . . . , R$ should be taken into account to determine the route of the corresponding executor. The routes form sequences of workstations with the depot as the beginning and the end. They are denoted by ${ \cal M } _ { r } \mathrm { = }$ $( m _ { r } ( j ) ) _ { j = 1 , 2 , . . . M _ { r } } ,$ where $m _ { r } ( j )$ and $M _ { r }$ are the $j \mathrm { t h }$ element of the route and length of the route, respectively. The value of the current element of $M _ { r }$ , i.e. $m _ { r } ( j ) = h _ { \colon }$ 4 $j = 1 , 2 , \dots M _ { r }$ is equal to the index of workstation (task) for which $\gamma _ { r , m _ { r } ( j - 1 ) , m _ { r } ( j ) } = 1$ , where $m _ { r } ( 0 ) = H + 1$ . Moreover, if the executor enters the workstation $m _ { r } ( j )$ , it should also leave this workstation. Thus,

$$
\begin{array}{l} \gamma_ {r, m _ {r} (j - 1), m _ {r} (j)} \\ = 1 \Rightarrow (\exists ! m _ {r} (j + 1) \in \bar {\boldsymbol {H}}) (\gamma_ {r, m _ {r} (j), m _ {r} (j - 1)} = 1). \end{array}
$$

$\mathrm { S o } ,$ using the form of the matrix $\gamma ,$ the routes $M _ { r }$ can be easily determined in the iterative way.

The upper level subproblem can be formulated as follows. For given sets H<sup>¯</sup> , R, matrices of times

$$
\bar{\boldsymbol{\tau}} = \hat{\boldsymbol{\tau}} = [\bar{\boldsymbol{\tau}}_{r,h}]_{\substack{r = 1,2,\ldots ,R\\ h = 1,2,\ldots ,H + 1}}
$$

and

$$
\begin{array}{c} \hat {\boldsymbol {\tau}} = \hat {\boldsymbol {\tau}} = \left[ \hat {\tau} _ {r, g, h} \right] _ {r = 1, 2, \dots , R} \\ g, h = 1, 2, \dots , H + 1 \end{array}
$$

determine: the matrix c, admissible in the sense of $( 2 ) ,$ (3), (4), (5) and (6), and consequently the routes $M _ { r }$ $r = 1 , 2 , \ldots . R$ to minimize the performance index (1).

## 2.2. Lower level subproblem

The control of a group of executors (vehicles) really consists of the motion control of individual executors and the traffic control (coordination) of a group of executors to avoid collisions with stationary and moving obstacles. It is obvious that the motion control of individual executor, which consists in reaching a final state for a given initial state, cannot be set irrespective of other executors, because the control algorithm has to know their positions (the states, in general).

The group of R moving executors (e.g. mobile robots) is considered. The vehicles move in the common working space. Let $\boldsymbol { x } _ { r } ( t ) { = } [ \boldsymbol { y } _ { r } ( t ) ^ { \mathrm { T } } , ~ \dot { \boldsymbol { y } } _ { r } ( t ) ] ^ { \mathrm { T } }$ $r = 1 , 2 , \ldots . R$ be the state vectors for executors, where $y _ { r } ( t )$ and ${ \dot { y } } _ { r } ( t )$ are l-dimensional vectors of positions and velocities, respectively. The control variables are defined as the l-dimensional vector $u _ { r } ( t )$ . Using known methods of modeling driving mechanisms, after discretization one can obtain their description in the form of the following difference equations

$$
x _ {r, v + 1} ^ {(i)} = f _ {r} ^ {(i)} (x _ {r, v}, u _ {r, v}), i = 1, 2, \dots 2 l, v = 0, 1, 2, \dots\tag{7}
$$

with the initial state $\boldsymbol { x } _ { r , 0 } ^ { ( i ) } \triangleq \boldsymbol { x } _ { r } ^ { ( i ) } ( \underline { { t } } _ { m _ { r } ( j ) } ) , ~ j = 1 , 2 , . . . , M _ { r }$ where v denotes a discrete time moment and $\underline { { t } } _ { m , ( j ) }$ is the moment the execution of the $m _ { r } ( j ) \mathrm { t h }$ element of route $M _ { r }$ starts or equivalently the execution of task $h = m _ { r } ( j )$ begins. Denoting by $\bar { t } _ { m , ( j ) }$ the moment the executor r reaches the workstation $h = m _ { r } ( j )$ one can determine the connection between final and initial states for consecutive elements of the route $M _ { r }$ as $x _ { r } ^ { ( i ) } \ ( \bar { t } _ { m , ( j \mathrm { ~ - ~ } 1 ) } ) = x _ { r } ^ { ( i ) } ( \underline { { t } } _ { m , ( j ) } ) , j = 1 , 2 , . . . , M _ { r }$ Moreover, the following equation holds $\underline { { { t } } } _ { m _ { r } ( j _ { + 1 } ) } = \bar { t } _ { m _ { r } ( j ) } + \bar { \tau } _ { r , m _ { r } ( j ) }$ ， which means that after reaching the current workstation $h = m _ { r } ( j )$ the executor is able to cover the next distance only when the time $\bar { \tau } _ { r , h }$ has elapsed.

The constraints imposed on control and state variables are very important from the point of view of the control problem under investigation. They have the form of intervals for control variables and for the part of the state vector corresponding to the velocities, i.e.

$$
u _ {r, v} ^ {(i)} \in \boldsymbol {U} _ {r} ^ {(i)} = [ \underline {{u}} _ {r} ^ {(i)}, \bar {u} _ {r} ^ {(i)} ], v = 0, 1, 2, \dots , i = 1, 2, \dots , s,\tag{8}
$$

and

$$
\begin{array}{l} x _ {r, v} ^ {(i)} \in X _ {r} ^ {(i)} = [ \underline {{x}} _ {r} ^ {(i)}, \bar {x} _ {r} ^ {(i)} ],   v = 0, 1, 2, \ldots , \\ i = l + 1, l + 2, \ldots , 2 l, \end{array}\tag{9}
$$

where ends of all intervals are known values. For the other part of the state vector, which corresponds to the position of the modeled mechanism, common constraints are imposed in the form

$$
y _ {r, v} \in Y _ {r, v},\tag{10}
$$

i.e. for every v the position of the rth executor should belong to an admissible area. This area can be determined as

$$
\begin{array}{l}\mathbf{Y}_{r,v} = \left\{y_{r,v} = [x_{r,v}^{(1)},\ldots ,x_{r,v}^{(l)}]^{T}:y_{r,v}\in \mathbf{X}^{(1)}\times \mathbf{X}^{(2)}\right.\\ \left.\times \ldots \times \mathbf{X}^{(l)} - \left(\bigcup_{\substack{s = 1\\ s\neq r}}^{R}\mathbf{D}_{s,v}\cup \bigcup_{h = 1}^{\bar{H}}\bar{\mathbf{D}}_{h}\right)\right\} , \end{array}
$$

where $\pmb { X } ^ { ( i ) } = [ \underline { { x } } ^ { ( i ) } , \bar { x } ^ { ( i ) } ] , i = 1 , 2 , . . . , l , \pmb { D } _ { s , \nu }$ is a forbidden area for the sth executor in the vth step, $\bar { D } _ { h } , h { = } 1 , 2 , . ~ . , \bar { H }$ are areas occupied by stationary obstacles. These constraints are dynamic ones and are connected with the necessity of avoiding collisions with other executors, which are treated as moving obstacles. Any other moving obstacles are not investigated. To evaluate the movement of the rth executor covering the $m _ { r } ( j ) \mathrm { t h }$ distance a local performance index is proposed. It consists in determining in every control step v such a decision $u _ { r , \nu }$ as to obtain the maximum approach to the final state, and it has the form

$$
\begin{array}{c} Q _ {r, v} (u _ {r, v}) = \sum_ {i = 1} ^ {2 l} \beta_ {i} \big [ x _ {r} ^ {(i)} (\overline {{t}} _ {m _ {r} (j)}) - x _ {r, v + 1} ^ {(i)} \big ] ^ {2} \\ = \sum_ {i = 1} ^ {2 l} \beta_ {i} \big [ x _ {r} ^ {(i)} (\overline {{t}} _ {m _ {r} (j)}) - f _ {r} ^ {(i)} (x _ {r, v}, u _ {r, v}) \big ] ^ {2}, \end{array}\tag{11}
$$

where $\beta _ { i } , \ i = 1 , 2 , . . . , 2 l \mathrm { - g i v e n }$ non-negative coefficients. For this case, in order to finish the control procedure, it is necessary to use the stop condition, which can be expressed in the following form

$$
\left[ \sum_ {i = 1} ^ {2 l} (x _ {r} ^ {(i)} (\bar {t} _ {m _ {r} (j)}) - x _ {r, v} ^ {(i)}) ^ {2} \right] ^ {\frac {1}{2}} <   \varepsilon_ {r},\tag{12}
$$

where $\varepsilon _ { r }$ is a given accuracy of reaching the final state. The performance index (11) together with the stop condition (12) corresponds to the so called ‘point-topoint’ control strategy.

A local control problem for the rth executor and current, i.e. $m _ { r } ( j ) \mathrm { t h }$ element of the route $M _ { r }$ is formulated as follows. For the given model (7) with initial and final states as well as positions of all workstations in Cartesian coordinates determine admissible sequence of control decisions $\displaystyle \big ( u _ { r , \nu } \big ) _ { \nu = 0 , 1 , 2 . . }$ <sub>.</sub> in the sense of 8), (9) and (10) to minimize the performance index (11), until the stop condition (12) is fulfilled. To solve the subproblems for all executors, the areas $Y _ { r , \nu }$ should be known, which is connected with determination of the coordination algorithm. Different approaches to the coordination of moving executors are presented in Refs. [8 – 10].

## 2.3. Two-level control problem

As the performance index for the two-level system the upper level criterion is considered, which means that the time optimum problem in the sense of makespan is solved. For the lower level decisionmaking subproblem the accuracy condition (11) is imposed, and the driving-up times $\hat { \tau } _ { r , g , h }$ are only the indirect result of this level decision making. Therefore, the matrix $\hat { \tau }$ depends on $\pmb { u } \overset { \Delta } { = } \{ ( u _ { r , \nu } ) _ { \nu = 0 , 1 , 2 , . . . , }$ $r = 1 , 2 , \ldots . R \}$ , where u is the set of control variables for executors. Consequently, the following equations hold $\hat { \boldsymbol { \tau } } = G ( \boldsymbol { u } ) , \boldsymbol { Q } ( \gamma , \hat { \boldsymbol { \tau } } ) = \boldsymbol { Q } ( \gamma , G ( \boldsymbol { u } ) ) = \boldsymbol { Q } ( M , \boldsymbol { u } ) { \overset { \Delta } { = } } \boldsymbol { Q } _ { \mathrm { M , u } } ,$ where $M _ { = } ^ { \underline { { \Delta } } } \{ M _ { r } ; r = 1 , 2 , . . . , R \}$

Finally, for given data of the subproblems at both levels, the two-level control problem consists in determination of routes M to minimize the performance index (1) as well as of motion control variables u for individual executors, which satisfy the ‘‘point-topoint’’ strategy.

## 3. Solution algorithms

The subproblems at both levels are interconnected, which means that results from one level can be treated as data for the other level. Namely, routes are the data for the subproblem of motion control of a group of executors, and driving-up times, being the indirect results obtained at the lower level, can be treated as the data for the upper level subproblem. To manage this interconnection, several heuristic decomposition algorithms have been proposed. Three of them are considered in the paper. The first one uses the time decomposition procedure and allows applying current modifications of routes. It is called adaptive algorithm. The second one, i.e. iterative algorithm consists in solving successively both subproblems in an iterative procedure until the stop condition is fulfilled. The last algorithm called on-line algorithm operates according to the local strategy and ensures the best performance of the complex system in the current step of decision making.

## 3.1. Adaptive algorithm

The adaptive algorithm enables a modification of routes during the decision-making procedure. The term ‘event’ is crucial. It consists in completing at least one task. Then it is necessary to decide whether routes of executors should be modified or whether they are valid for the next decision step. Let us assume that n and $M _ { r } ( n )$ denote the current event or the current decision step and the route of the executor r in the step $n ,$ respectively. We introduce the following subsets of tasks: H(n) – not completed until step $n \ ( H ( 0 ) = H )$ $H ^ { \prime } ( n )$ – being performed in step n according to scheduling algorithm from previous step, H <sup>U</sup>(n) – not started till step n, $H ^ { \prime \prime \prime } ( n ) \cdot$ –just completed in step n. Let $\Delta ( n )$ be the duration of step n. Consequently, $\scriptstyle H ^ { \prime \prime } ( n ) =$ $H ^ { \prime \prime } ( n - 1 ) - ( H ^ { \prime } ( n ) - \ H ^ { \prime \prime \prime } ( n ) )$ . For tasks from the subsets ${ \pmb H } ^ { \prime } ( n )$ and $H ^ { \prime \prime \prime } ( n ) .$ , new execution times are calculated according to $\tau _ { r , h } ( n ) = \tau _ { r , h } ( n - 1 ) - \Delta ( n )$ For tasks from the subset $H ^ { \prime \prime } ( n )$ , no modifications are introduced, i.e. $\tau _ { r , h } ( n ) = \tau _ { r , h } ( n - 1 )$ . All times $\tau _ { r , h } ( n )$ form the matrix of execution times $\hat { \tau } ( n ) = \bar { \tau } ^ { + }$ $\scriptstyle { \hat { \tau } } ( n )$ . The modifications refer also to constraints [6]. The tasks from the set $H ^ { \prime } ( n )$ should not be taken into account in the scheduling subproblem, because they are just being performed. The workstations corresponding to the tasks from the sets $H ^ { \prime } ( n )$ or $H ^ { \prime \prime \prime } ( n )$ are the beginnings of new routes. Then the scheduling subproblem consists in minimizing the modified performance index

$$
\begin{array}{l} Q (\gamma (n)) = \max _ {r = 1, 2, \dots , R} \Bigg \{\sum_ {h = 1} ^ {H ^ {\prime \prime} (n) + 1} \sum_ {g = 1} ^ {H ^ {\prime \prime} (n) + 1} \gamma_ {r, g, h} (n) \\ \qquad \times (\bar {\tau} _ {r, h} + \hat {\tau} _ {r, g, h} (n)) \Bigg \}, \end{array}\tag{13}
$$

subject to modified (2), (3), (4), (5) and (6). To solve this subproblem, the routes $M _ { r } ( n )$ with the beginning in $h ^ { \prime } ( n )$ and the end in $h = H + 1$ are derived. To be more precise, $\pmb { M } _ { r } ( n ) { = } ( m _ { r } ( 1 , n ) , m _ { r }$ $( 2 , n ) , . . . , m _ { r } ( M _ { r } ( n ) , n ) )$ , where $m _ { r } ( 1 , n ) = h ^ { \prime } ( n )$ for $h ^ { \prime } ( n ) { \in } M _ { r } ( \mathrm { n - 1 } )$ and $m _ { r } ( M _ { r } ( n ) , n ) = H + 1$ . When events take place (i.e. when tasks are completed) the expected time moments $t ^ { h } ( n )$ can be easily calculated in an iterative way using the term ${ t ^ { h } } ( n ) = { \bar { t } } ^ { m _ { r } ( j , n ) } { = } { \underline { { t } } } ^ { m _ { r } ( j - 1 , n ) } + { \tau _ { r , h } } ^ { = } { = } { \underline { { t } } } ^ { m _ { r } ( j - 1 , n ) } + { \bar { \tau } } _ { r , h } +$ $\hat { \tau } _ { r , m _ { r } ( j - 1 , n ) , m _ { r } ( j ; n ) } , j = 1 , . . . , M _ { r } ( n )$ where $m _ { r } ( j , n )$ consists in execution of task h and $m _ { r } ( 0 , n )$ is equal to 0. The number of such time moments denoted by $Z ( n )$ is not greater than $H + R .$ After ordering, the time moments $t ^ { h } ( n )$ give a sequence ${ \pmb T } ( n )$ . In each step, the condition ${ \cal T } ( n ) = { \cal T } ( n - 1 )$ , $n = 1 , 2 , \ldots$ , i.e. $t ^ { z } ( n ) = t ^ { z } ( n - 1 )$ for all $z = 1 , 2 , . . . . Z$ is checked. If it is fulfilled the route from the former step is executed, otherwise the new scheduling subproblem should be solved. To start the algorithm the initial matrix of drivingup times ${ \hat { \tau } } \left( 0 \right)$ is determined by calculating the collision-free movement between every pair of workstations. Then the adaptive decision-making algorithm for the two-level complex operation system under consideration has the following form (Fig. 2).

For given $\bar { H } ( 0 ) , R , \hat { \tau } ( 0 ) , \bar { \tau } , n = 0$

1. Solve the scheduling subproblem with moving executors to obtain $\gamma ( n )$ or equivalently $M ( n )$ . Next determine the sequence ${ \pmb T } ( n )$ and the number $Z ( n )$

2. Check if $H ( n ) { \mathrm { > } } 0$ . If it is fulfilled go to next step, otherwise stop the algorithm.

3. Solve the motion control subproblem of a group of executors to determine u(n).

![](/api/attachments/JR3D6M5T/fulltext/images/8d0c9406093433439daa8e51211ea49eab64c4be82725276782217d16cedbd70.jpg)  
Fig. 2. Block scheme of the adaptive algorithm.

![](/api/attachments/JR3D6M5T/fulltext/images/b0b6ddfbd075f5515e943321acc67d1e2108c0d476513bbd4487c4734624eff0.jpg)  
Fig. 3. Block scheme of the iterative algorithm.

4. Observe moments $t ^ { z } ( n )$ and calculate ${ \hat { \tau } } ( n ) , \tau ( n )$ as well as $H ( n )$

5. Check if $( \forall h ^ { \prime } ( n ) { \in } H ^ { \prime \prime \prime } ( n ) ) ( t ^ { z } ( n ) { = } t ^ { h ^ { \prime } ( n ) } ( n - 1 ) )$ . If it is fulfilled set $n = n + 1$ and go to step 2, otherwise go to step 1.

## 3.2. Iterative algorithm

For this algorithm, one iteration, denoted by $\eta ,$ means solving decision subproblems at both levels, i.e. scheduling subproblem to obtain the routes M as well as the subproblem of motion control of a group of executors (shortly: motion control) to obtain in consequence a matrix of driving-up times $\hat { \tau } .$ . The routes and driving-up times, which have been obtained for the iteration g, $\eta = 0 , 1 , \ldots$ are denoted by $M ( \eta )$ and $\hat { \tau } ( \eta )$ , respectively. The values of $\hat { \tau } ( \eta )$ can be obtained from the plant, i.e. from the complex manufacturing system, or from its simulation model –after applying control signals $\pmb { u } ( \eta )$ . To determine the starting point of the algorithm in the form of times $\hat { \tau } ( 0 )$ a simulation model has been applied for the case of collision-free movement of executors. From the point of view of a control system, with a group of moving executors as a control plant, collisions among executors can be treated as disturbances. The necessity of collision avoidance causes the difference of decision-making results in the two-level system in consecutive iterations. The structure of decision-making system under consideration, when the iterative method is applied is presented in Fig. 3.

![](/api/attachments/JR3D6M5T/fulltext/images/a1801ac2f8ba276876b4193299c04a5b855588408b910c275ad5ea0dce752aaf.jpg)  
Fig. 4. Block scheme of the on line algorithm.

![](/api/attachments/JR3D6M5T/fulltext/images/013812605125171764ffdfac8403c68ec320f835f38c7255f27b77ed7c7832cf.jpg)  
Fig. 5. Dependence of T on H for $R = 2 \colon ( \mathrm { a } )$ iteration algorithm with stop condition (14), (b) adaptive algorithm, (c) iteration algorithm with stop condition (15), (d) on-line algorithm.

For terminating the iterations it is necessary to apply stop conditions. Two stop conditions are proposed. In the first one the values of the performance index $Q _ { \mathrm { M , u } } ( \eta )$ for the last $\eta _ { 0 }$ iterations are taken into account, i.e.

$$
\sum_ {k = \eta - \eta_ {0}} ^ {\eta} \zeta^ {\eta - k} (Q _ {\mathrm{M}, \mathrm{u}} (k - 1) - Q _ {\mathrm{M}, \mathrm{u}} (k)) <   \bar {\varepsilon},\tag{14}
$$

where $\zeta \in [ 0 , 1 ]$ –memory factor, e¯–accuracy of the iterative algorithm.

The second stop condition reflects the situation when

$$
\hat {\boldsymbol {\tau}} (\eta) = \hat {\boldsymbol {\tau}} (\eta - 1), \eta = 1, 2, \dots .\tag{15}
$$

Eq. (15) should be understood as the equality of all admissible driving-up times, i.e. $\hat { \tau } _ { r , g , h } ( \eta ) = \hat { \tau } _ { r , g , h } ( \eta - 1 )$

The iterative algorithm for current iteration g, $\eta = 0 , 1 , \dotsc$ . is presented as follows.

For given H<sup>¯</sup> , $R , \hat { \tau } ( 0 ) , \bar { \tau } , \eta = 1$

1. Solve the motion control subproblem to obtain $\pmb { u } ( \eta )$

![](/api/attachments/JR3D6M5T/fulltext/images/5a46a18992c0de2aa8dbcb56dbeece31a6e879dddab854b0321f700aca1b2853.jpg)  
Fig. 6. Dependence of $\mathcal { Q } _ { \mathrm { M , u } }$ on H for R = 2: (a) iteration algorithm with stop condition (14), (b) adaptive algorithm, (c) iteration algorithm with stop condition (15), (d) on-line algorithm.

![](/api/attachments/JR3D6M5T/fulltext/images/a3f69cc73a5bff00293dc6c81b82df542f5661dcca32003fd3ceb214e97e9f83.jpg)  
Fig. 7. Dependence of T on H for R = 4: (b) adaptive algorithm, (d) on-line algorithm.

2. Calculate $\hat { \tau } ( \eta )$ using the simulation model.

3. Solve the scheduling problem with moving executors to obtain c(g) or equivalently $M ( \eta )$

4. Verify the stop condition (14) and/or the stop condition (15). If at least one of the stop conditions is not fulfilled set $\eta = \eta + 1$ and go to step 1. Otherwise, stop the algorithm with $M ( \eta )$ and $Q _ { \mathrm { M , u } } ( \eta )$ as the results.

The values of elements of tˆ (0) are calculated using simulation model without collisions $\left( \mathrm { F i g } . \ 3 \right)$ . It means that the motion of all executors for all possible distances between workstations is started and appropriate driving-up times are calculated. The separate solution algorithms are determined to obtain solutions in steps 1 and 3. They have been described in more detail, e.g. in Refs. [4,5].

## 3.3. On-line algorithm

This algorithm can be treated as the special case of the adaptive one. In the current decision step it consists in mapping tasks from the set $H ^ { \prime \prime } ( n )$ to free executors which belong to the set $\pmb { R } ^ { \prime \prime } ( n )$ . The mapping is performed according to a heuristic rule. Let us denote by $h _ { r } ( n )$ the index of workstation, where there is a free executor from the set $\pmb { R } ^ { \prime \prime } ( n )$ . The algorithm is composed of five steps (Fig. 4).

1. Fix $n = 0 , \ H ^ { \prime \prime } ( 0 ) { = } H , \ R ^ { \prime \prime } ( 0 ) { = } R , \ h _ { r } ( 0 ) { = } H { + } 1$ $r = 1 , 2 , \ldots . , R .$

![](/api/attachments/JR3D6M5T/fulltext/images/a124ad45a69fb1e36fbf5ac41bb1e7e3707e1db73b1e4c8a09099092a1613406.jpg)  
Fig. 8. Dependence of $\mathcal { Q } _ { \mathrm { M , u } }$ on H for R = 4: (b) adaptive algorithm, (d) on-line algorithm.

![](/api/attachments/JR3D6M5T/fulltext/images/9091d52898491dbc33d5c16cb1867a73031cd4e37db261c193dc0e45aaf9e32c.jpg)  
Fig. 9. Dependence of T on R for H = 12: (a) iteration algorithm with stop condition (14), (b) adaptive algorithm, (c) iteration algorithm with stop condition (15), (d) on-line algorithm.

2. For successive executors from 1 until $R ^ { \prime \prime } ( n ) { \mathrm { : } }$

(a) select the task $h ^ { * }$ of the least number which fulfils the inequality

$$
\bar {\tau} _ {r, h ^ {*}} + \hat {\tau} _ {r, h _ {r} (n), h ^ {*}} \leq \bar {\tau} _ {r, h} + \hat {\tau} _ {r, h _ {r} (n), h}, h \in \boldsymbol {H} ^ {\prime \prime} (n), h \neq h ^ {*}
$$

and assign it to the executor $r ,$

(b) set ${ \cal H } ^ { \prime \prime } ( n ) { = } { \cal H } ^ { \prime \prime } ( n ) - \{ h ^ { * } \}$

If n>0 go to step 4, otherwise go to step 3.

3. Run the lower level control algorithm.

4. Observe the event $n ,$ determine the set $\pmb { R } ^ { \prime \prime } ( n )$ as well as the workstation $h _ { r } ( n )$ for $r = 1 , 2 . . . , R ^ { \prime \prime } ( n )$ and set $n = n + 1$ . If $\scriptstyle H ^ { \prime \prime } ( n ) > 0$ , i.e. if the set $H ^ { \prime \prime } ( n )$ is nonempty go to step 2, otherwise go to step 5.

5. If $\pmb { R } ^ { \prime \prime } ( n ) = \pmb { R }$ finish the motion control algorithm. Otherwise, assign the task $h = H + 1$ to all executors belonging to the set $\pmb { R } ^ { \prime \prime } ( n )$ and go to step 4.

The local heuristic rule from step 2 allows finding for the consecutive executors the tasks with the shortest execution times. Other local strategies can also be applied.

## 4. Simulation experiments

To verify the heuristic algorithms a computer program has been developed and used for simulation. The approximate algorithms have been applied for solving the subproblems of both levels. The calcula-

![](/api/attachments/JR3D6M5T/fulltext/images/5d528f8be50f4fe35ab886372e948bee8a4d9067df2c81cea5a9e49aa43c468e.jpg)  
Fig. 10. Dependence of $\mathcal { Q } _ { \mathrm { M } , \mathrm { u } }$ on R for H = 12: (a) iteration algorithm with stop condition (14), (b) adaptive algorithm, (c) iteration algorithm with stop condition (15), (d) on-line algorithm.

![](/api/attachments/JR3D6M5T/fulltext/images/77b0b4f692310e1ccb9b34c5953213ee3a0f66d589eb2d0e32ce9c928f9cb546.jpg)  
Fig. 11. Layout of workstations and routes of executors for the online algorithm.

tions have been conducted for $R \geq 2$ and $H \leq 1 6$ . The matrix $\scriptstyle { \hat { \tau } }$ of the times jobs are performed at workstations has been generated randomly according to the rectangular distribution. The workstations have been uniformly placed in a square working space. The examples of results are given in Figs. 5–10. The performance index $\mathcal { Q } _ { \mathrm { M , u } }$ and the time of computation $T$ serve as the basis for comparison purposes for different number of tasks H and for different number of executors R. Considering the performance index for R = 2 all algorithms differ a little, i.e. both iterative algorithms are slightly better than other ones and the on-line algorithm changes in a non-regular way (Fig. 6). For $R = 4 ,$ , the on-line algorithm is better than the adaptive one (Fig. 8). Consequently, the iterative algorithm with stop condition (14) is the best one and the adaptive algorithm is not recommended as far as the quality of scheduling is considered. The same conclusion results from Fig. 10. However, taking into account the time of computation T (Figs. 5, 7 and 9), the on-line algorithm is the best one and both iterative algorithms (especially the version with stop condition (14)) are very time-consuming. Concluding, one can formulate the opinion that the iterative algorithm with stop condition (14) should be used when the computation time is not limited. Otherwise, the on-line algorithm is recommended.

<table><tr><td colspan="13">Table 1Times  $\bar{\tau}_{r,h}$ </td></tr><tr><td rowspan="2"> $r$ </td><td colspan="12">h</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>10</td><td>11</td><td>61</td><td>22</td><td>26</td><td>50</td><td>29</td><td>19</td><td>32</td><td>35</td><td>14</td><td>38</td></tr><tr><td>2</td><td>65</td><td>32</td><td>56</td><td>29</td><td>51</td><td>60</td><td>53</td><td>28</td><td>19</td><td>29</td><td>37</td><td>24</td></tr></table>

Table 2  
Numerical example—results

<table><tr><td>Algorithm</td><td> $M_r$ </td><td> $Q_{\text{M,u}}$ </td><td>T [s]</td></tr><tr><td>Adaptive</td><td> $M_1 = (13,1,5,7,11,9,3,13),$  $M_2 = (13,4,6,8,12,10,2,13)$ </td><td>494</td><td>468</td></tr><tr><td>On-line</td><td> $M_1 = (13,2,1,7,11,5,6,13),$  $M_2 = (13,4,8,12,10,9,3,13)$ </td><td>526</td><td>472</td></tr><tr><td>Iterative</td><td> $M_1 = (13,1,5,7,11,9,3,13),$  $M_2 = (13,2,4,8,12,10,6,13)$ </td><td>430</td><td>1356</td></tr></table>

Let us consider a simple numerical example. Two executors (R = 2) perform tasks at 12 workstations $( H { = } 1 2 )$ . The layout of workstations is presented in Fig. 11. The matrix $\scriptstyle { \hat { \tau } }$ of times jobs are performed at workstations are given in Table 1. For distances between workstations (Fig. 11) and for times from matrix tˆ the conventional units are used. The example may be treated as an illustration of a transportation process in a discrete manufacturing system, where the elements of matrix $\scriptstyle { \hat { \tau } }$ are the times of unloading the executors. After applying all control algorithms described in the paper the results presented in Table 2 have been obtained. Apart from Table 2 the routes M for the on-line algorithm are also presented in Fig. 11.

## 5. Final remarks

In the paper, a global approach to solving a complex decision-making problem in a complex operation system, which is formulated in the form of a two-level system, has been proposed. The task scheduling characterized by the execution times as well as the motion control of executors performing these tasks are considered together, which is the original contribution of the investigation presented. Till now such problems for discrete manufacturing systems have been considered and solved separately. More effective computer tools for execution of decision-making algorithms enable us to investigate the subproblems together. The investigation conducted allows only heuristic solution algorithms to be determined. Three such algorithms have been presented. Their computational efficiency and sensitivity to the changes of the data have been verified and compared via computer simulation. The results of investigations, presented also in other works (e.g. Refs. [6,10]), seem to be a good basis for designing decision-making algorithms for complex manufacturing operation systems. The problem of determining the approximate or even exact solution algorithms is still open. Moreover, for further investigations at least two issues are worth mentioning:

1. The general two-level complex manufacturing system can contain different subproblems at both levels. At the upper level not only scheduling problems but also other decision-making problems for complex operation system, e.g. allocation problems, could be investigated. Analogously, at the lower level many control problems can be located and solved. They concern not only transportation tasks like those presented in the paper but also technological tasks.

2. Complex decision-making problems can be stated in different ways. The form of performance index is very important for the two-level system as a whole. In the paper, the criterion from the upper level has been chosen. However, decision making in the two-level complex operation system is a multi criteria problem and to solve it adequate methods and algorithms should be applied.

## Acknowledgements

The research was supported by the Polish State Committee for Scientific Research under the grant 7 T11A 039 20.

## References

[1] Y. Dumas, J. Desrosiers, E. Gelinas, M.M. Solomon, An optimal algorithm for the travelling salesman problem with time windows, Operations Research 43 (2) (1995) 367– 371.

[2] J. Jo´zefczyk, Two-Level Control Algorithm for Mobile Executors in Flexible Manufacturing Systems, Proceedings of 10th International Conference on Systems Engineering, Coventry University, Coventry, UK, 1994.

[3] J. Jo´zefczyk, On the functional decomposition approach to the problem of tasks scheduling on moving executors, Proceedings of 11th International Conference on Systems Engineer ing, Las Vegas University, Las Vegas, USA, 1996.

[4] J. Jo´zefczyk, An algorithm for scheduling tasks on moving executors, Proceedings of 1st IFAC Workshop on Manufactur-

ing Systems: Modelling, Management and Control (Vienna, Austria), 1997.

[5] J. Jo´zefczyk, Knowledge based motion control of a group of mobile executors in the two-level complex operation system, in: S. Nahavandi, M. Saadat (Eds.), Proceedings of 2nd World Manufacturing Congress WMC 1999, International Computer Science Conventions, Canada, 1999, pp. 167–173.

[6] J. Jo´zefczyk, Algorithms for decision making in two-level manufacturing operation system, Proceedings of 14th International Conference on Systems Engineering, vol. 1, Coventry University, Coventry, UK, 2000.

[7] J. Jo´zefczyk, Scheduling tasks on moving executors to minimise the maximum lateness, European Journal of Operational Research 131 (2001) 171–187.

[8] J. Jo´zefczyk, Application of knowledge based pattern recognition to movement control of a group of vehicles, International Journal of Knowledge-Based Intelligent Engineering Systems 6 (4) (2002) 192–198.

[9] J. Jo´zefczyk, Application of Knowledge Based Pattern Recognition in the Control System of a Group of Executors, in: R. Vallee, J. Rose (Eds.), Proceedings of 11th International Congress of Cybernetics and Systems, Brunel University, Uxbridge, UK.

[10] J. Jo´zefczyk, Knowledge Based Two-Level Control of a Group of Mobile Executors, Integrated Computer-Aided Engineering (to be published).

[11] A. Langevin, M. Desrochers, J. Desrosiers, S. Gelinas, F. Soumis, A two-commodity flow formulation for the traveling salesman and the makespan problems with time windows, Networks 23 (1993) 631–640.

[12] A. Mingozzi, L. Bianco, S. Ricciardelli, Dynamic programming strategies for the travelling salesman problem with time window and precedence constraints, Operations Research 45 (3) (1997) 365–377.

[13] R.T. Nelson, R.T. Sarin, R.L. Daniels, Scheduling with multiple performance measures: the one machine case, Management Science 32 (1986) 464– 479.

![](/api/attachments/JR3D6M5T/fulltext/images/58b861c946e7b08f0d2a4e54de861c02c3ca09820d84e2ed3df8c5141353b8df.jpg)

Jerzy Jo´zefczyk was born in 1956. He graduated in automatic control system from Wroclaw University of Technology, in 1980. He received the PhD degree in Computing Science from Poznan University of Technnology, in 1987, and Dr. Sci. degree in Automation and Robotics from Systems Research Institute of Polish Academy of Sciences, Warsaw, in 1996.

From 1980 to 1987, he was a doctorate student and research assistant in Institute of

Control and Systems Engineering Wroclaw University of Technology. From 1988 to 2001, he was associate in the same institute and since 2002 full professor.

His research interests include operations research, complex control systems and artificial intelligence.

Prof. Jo´zefczyk has been the Scientific Secretary of the Committee of Automation and Robotics of Polish Academy of Sciences since 1988.
