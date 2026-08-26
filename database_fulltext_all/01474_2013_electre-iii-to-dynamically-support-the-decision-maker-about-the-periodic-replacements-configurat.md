---
otero_id: 1474
otero_key: "FUDEAHWN"
title: "ELECTRE III to dynamically support the decision maker about the periodic replacements configurations for a multi-component system"
authors: "Antonella Certa; Mario Enea; Toni Lupo"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.044"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ELECTRE III to dynamically support the decision maker about the periodic replacements con<sup>fi</sup>gurations for a multi-component system

Antonella Certa ⁎, Mario Enea, Toni Lupo

Dipartimento di Ingegneria Chimica, Gestionale, Informatica, Meccanica, Università degli Studi di Palermo, 90128 Palermo, Italy

## a r t i c l e i n f o

Article history: Received 7 May 2012 Received in revised form 23 October 2012 Accepted 30 December 2012 Available online 17 January 2013

Keywords: Multi-objective optimization ELECTRE III, periodic maintenance policy Multi-component system Non-homogeneous Poisson process

## a b s t r a c t

The problem tackled by the present paper concerns the selection of the elements of a repairable and stochastically deteriorating multi-component system to replace (replacements configuration) during each scheduled and periodical system stop within a <sup>fi</sup>nite optimization cycle, by ensuring the simultaneous minimization of both the expected total maintenance cost and the system unavailability. To solve the considered problem, a combined approach between multi-objective optimization problem (MOOP) and multi-criteria decision making (MCDM) resolution techniques is proposed. In particular, the ε constraint method is used to single out the optimal Pareto frontier whereas the ELECTRE III multi-criteria decision support method is proposed to support the selection of the replacements con<sup>fi</sup>guration that represents the best compromise among the considered objectives. The proposed approach is sequentially applied at each scheduled system stop by allowing the dynamic updating of the information about the decisional context in which the decision maker has to operate. To illustrate the whole procedure a numerical case study is solved for different hypothesized scenarios related to the importance attributed by the decision maker to the system unavailability and the maintenance cost objectives.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

A particular kind of preventive maintenance policy for multicomponent systems is the periodic one. In such a maintenance policy, each system element can be replaced during scheduled and periodic stops of the system disregarding of its failure history and repaired when the failure occurs. The periodic maintenance policy represents for its easy implementation, especially in large and complex multicomponent systems, the most used maintenance policy [23]. For example, systems such as power plants, gas turbine plants, and petroleum re<sup>fi</sup>neries are commonly subjected to scheduled and periodic stops during which preventive maintenance can be eventually performed and, in addition, the potential and hidden failures are detected and repaired.

In the literature, in order to determine the parameters characterizing a periodic maintenance policy, different models have been developed considering one or more objectives to reach. The most treated objective in the periodic maintenance policy models is the minimization of the total maintenance cost. For example Bris et al. [3] develop an optimization model, considering the system elements periodically inspected and maintained, aiming to <sup>fi</sup>nd out the optimal maintenance policy for each element by minimizing the cost function and respecting an availability constraint. In order to solve the problem, the Authors propose a genetic algorithm, whose structure includes the inspection time and the time length between two consecutive maintenance interventions for each element. Caldeira, Duarte et al. [4] propose a mathematical programming model for a series system, with elements characterized by a Weibull hazard function, to calculate the optimum frequency to perform preventive maintenance actions for each element. The aim is the minimization of the maintenance cost so that the total downtime, in a certain period of time, does not exceed a <sup>fi</sup>xed value. Certa et al. [10] formulate a constrained mathematical model to solve the problem of determining both the optimal number of periodic inspections within a <sup>fi</sup>nite time frame and the system elements to replace during each scheduled inspection. Furthermore, the maintenance policy has to ensure a very high system reliability level with the minimum total maintenance cost. Taghipour et al. [20] develop a model able to <sup>fi</sup>nd out the optimal periodic inspection intervals over a <sup>fi</sup>nite time horizon considering a system composed of elements subjected to soft and hard independent failures. Hard failures are instantaneously detected and <sup>fi</sup>xed while soft failures can be detected and <sup>fi</sup>xed only at the scheduled inspections. The model takes into account as objective to optimize the expected total cost arising from soft and hard failures incurred over the optimization time horizon and a recursive procedure is adopted to solve it. More recently, Taghipour et al. [19] develop a model aiming to determine the optimal periodicity of the inspection intervals of a reparable system subjected to hidden failures over <sup>fi</sup>nite and in<sup>fi</sup>nite optimization time. The proposed objective function is the minimization of the expected total cost. A failed system element may be replaced or minimally repaired with a probability dependent on the elements age. Recursive procedures are developed to calculate the probabilities of failures, the expected number of minimal repairs and the expected downtime of the system.

Considering production systems, a suitable parameter for evaluating the maintenance policy effectiveness is its stationary availability, also de<sup>fi</sup>ned as the expected time percentage in which the system is functioning. Therefore, for this kind of systems, also the stationary availability maximization represents another objective to be reached. Vaurio [22] studies the average unavailability of standby units under several sets of assumptions concerning the renewal ef<sup>fi</sup>ciency of tests and repairs. Cassady et al. [7] tackle the problem to single out the set of elements on which to operate at periodic scheduled breaks, in order to maximize the system availability and to respect a maintenance cost constraint. The maintenance activities must be completed within an allotted time. The problem is formulated by a mathematical model and solved for two simple systems. Also Tsai et al. [21] develop an algorithm to <sup>fi</sup>nd out an optimal maintenance policy for a multi-component system. In particular, the Authors consider a preventive maintenance policy that takes simultaneously into account three actions: the mechanical service, aiming at alleviate the strength degradation; the repair activity, addressed to partially restore a degraded component and the replacement activity, settled to recover a component to its original condition. For each element the preventive maintenance intervals are investigated on the base of the system availability maximization and the minimum interval value is chosen for programming the periodic maintenance policy.

In the light of the previous considerations, the expected total main tenance cost and the system unavailability are herein considered as objective functions to be optimized in order to develop a periodic maintenance policy for a multi-component system over a <sup>fi</sup>nite optimization cycle. Moreover, since the cost and the system unavailability objectives could take a different relative importance depending on the operative context in which the decision maker has to operate, the problem is formulated and faced by means of tools belonging to the multi-objective optimization problem (MOOP) and the multi-criteria decision making (MCDM) techniques. In particular, being the two objective functions contrasting one each other, it is not possible to <sup>fi</sup>nd out a single optimal solution corresponding to the best result for both the considered objectives but an optimal Pareto frontier, that is a set of non-dominated trade-off solutions, can be described. Each optimal solution represents an optimal replacements con<sup>fi</sup>guration for the related objectives trade-off level. Clearly, the optimization procedure should generate a number of non-dominated solutions among which the decision maker should select the most attractive one. Therefore, as stressed by Campanella [5], it is important to support the decision maker in the choice of the solution that represents for she/he the best compromise among the considered objectives. For such motivation an ef<sup>fi</sup>cient combined procedure based on integration between the MOOP and the MCDM techniques is herein proposed.

In the literature, in order to describe the Pareto frontier different approaches, with relation to maintenance problems, have been proposed. For example heuristic approaches like evolutionary algorithms have been developed. Those approaches often imply high computational time and they do not ensure the determination of the overall Pareto frontier. Hilber et al. [13] propose a multi-objective model to maximize customer satisfaction and minimize maintenance costs for a power delivery system. The aim is the determination of the optimal trade-off between preventive and corrective maintenance. Chang et al. [11] develop a multi-objective optimization model in order to carry out a proper preventive maintenance scheduling for a power supply substation that is able to provide an effective trade-off between reliability and maintenance cost. In particular, in order to solve the considered problem, they propose a multi-objective genetic algorithm and the minimum cut set method. Certa et al. [8] propose an exact algorithm addressed to the determination of the set of elements on which maintenance actions must be executed so as the system operates with a required reliability until the next scheduled inspection, minimizing both the maintenance total cost and the total maintenance time.

The most widely used approaches to describe the Pareto frontier are the weighted sum method and the ε constraint method [12]. The greatest dif<sup>fi</sup>culty in applying the <sup>fi</sup>rst one consists of setting suitable weight vectors to obtain optimal non-dominated solutions and moreover it is able to describe only the convex region of the frontier. To the contrary, the second approach overcomes the limitations of the previous one and it allows the complete description of the Pareto frontier. In any case, the determination of just a single point of the frontier using these methods requires the resolution of a mathematical programming problem. For the previous reasons the ε constraint method is herein chosen to describe the optimal Pareto frontier at each system stops. Also Certa et al. [9] propose the use the ε constraint method to <sup>fi</sup>nd out the optimal solutions in a multi-objective context related to a medium-term scheduling of periodic maintenance actions.

In order to select the best maintenance strategy the Analytic Hierarchy Process (AHP) multi-criteria method [18] is the decision support method more considered in the literature. Bevilacqua and Braglia [2] propose the use of the AHP for selecting the best maintenance strategy among preventive, predictive, condition-based, corrective and opportunistic maintenance alternatives for an important Italian oil re<sup>fi</sup>nery. Carnero [6] propose a model that carries out the decision regarding the selection of the diagnostic techniques and instrumentations in the predictive maintenance programs. The proposed resolution approach consists of a combination of tools belonging to the MCDM techniques, just like the AHP and the factor analysis (FA). Pariazar et al. [16] suggest the use of the AHP to select the maintenance strategy by considering cost, safety, execution capability as criteria of evaluation. Given the high number of considered criteria, they propose the AHP to reduce the inconsistency of the judgments of comparison that affects this methodology. Recently, Arunraj and Maiti [1] propose an approach based on the AHP and goal programming for the maintenance policy selection and they show a case study related to a benzene extraction unit of a chemical plant. Papakostas et al. [15] propose a methodology to support the decision maker about maintenance actions to carry out on an aircraft, aiming at high <sup>fl</sup>eet operability and low maintenance cost. In particular, a multi-criteria mechanism evaluates a set of maintenance plan alternatives.

The AHP is a compensative method, that is, with relation to a solution, a very bad score value in an objective can be compensated by high score values in the other objectives. This compensation feature could not be approved by the decision maker in the case in which the scores difference overcomes a value of threshold <sup>fi</sup>xed by she/ he. On the contrary, the ELECTRE III [17] is a non-compensative MCDM method and thus it is herein proposed as decision support method to select the solution that represents the best compromise among the considered objectives.

The present paper is organized as follows: in the next section the problem description is given; in Section 3 the mathematical formulation and the solution approach of the multi-objective problem is shown; in Section 4 the ELECTRE III method for the selection of the best maintenance strategy is presented; in Section 5 a numerical analysis related to a case study is presented and the related results are commented; <sup>fi</sup>nally, the conclusions close the work. Furthermore, all the steps necessary to execute the proposed combined procedure related to the case study are reported in the Appendix A.

## 2. Problem description

As mentioned before, it is herein considered a reparable and stochastically deteriorating multi-component system consisting of series components which can be composed by a single element or by series elements arranged in branches. In the <sup>fi</sup>rst case, a failure (hard failure) leads to the system downtime, whereas a failure of an element (soft failure) of a component composed by series elements arranged in branches does not imply the system failure. It is considered that during the system operative time both the hard and the soft failures are immediately detected and minimally repaired, during the system downtime for the hard type or while the system is working for the soft type. Instead, the replacement of system elements can be performed only during the scheduled and periodic system stops, whose duration has not been greater than the allotted time $T _ { a \cdot }$ In fact, as in many real systems, such as chemical processing facilities, and power plants, the replacement of system elements can be performed only during the scheduled system stops and within the allotted time $T _ { a \cdot }$ In fact, the presence of some operative and/or some technical constraints can make economic disadvantage or even impossible to perform the maintenance actions at any time [7]. For example in many industrial systems, in order to assure the respect of the production scheduling related to a given time interval, the duration of the maintenance activities, at each scheduled system stop, has not overcome the allotted time. Also the value of the interval $\mathrm { t _ { p } , }$ that is the time between two consecutive stops, arises from aspects linked to functional features of the system that, considering large and complex multi-component systems, is generally <sup>fi</sup>xed for the whole lifetime of the system.

Considering a <sup>fi</sup>nite optimization cycle of length $T ^ { * } ,$ that could be equal, for example, to the period covered by a contract of maintenance services for the providing of services for $T ^ { * } / t _ { p }$ number of scheduled system stops, the aim of the proposed approach is to single out the replacements con<sup>fi</sup>guration, that is the selected system elements to replace during each scheduled stop.

The proposed optimization methodology consists of splitting the solution procedure into two phases: the <sup>fi</sup>rst step consists of obtaining the set of non-dominated trade-off solutions (Pareto optimal solutions) within the whole space of the feasible ones. In the second step, the solutions belonging to the Pareto frontier are evaluated and compared in order to select the best one. The two-step approach is sequentially repeated at each system stop, since particular aspects as further information about the decisional context, or particular needs, or knowledge of practicable solutions, could be provided to the decision maker only in a second phase. So, it will be easier to select the solution representing the best compromise for all the considered objectives by choosing it from a restricted set of the non-dominated ones at the moment in which the decision has to be made. In such way, the proposed optimization approach is con<sup>fi</sup>gured as a dynamic optimization method in the time domain.

In order to explain how the developed approach works, Fig. 1 shows the sequential optimization approach. In particular $, j = 1$ is the current instant in which the optimization procedure is started. The optimal replacements con<sup>fi</sup>gurations set, that is the Pareto frontier solutions, for the <sup>fi</sup>rst scheduled stop $j = 1$ is singled out in order to minimize both the expected total maintenance cost and the system unavailability in an optimization time frame T that includes a certain number of next system scheduled stops. The choice of the number of the scheduled system stops is made in order to reach a good trade-off between the goal of extending the optimization temporal horizon to obtain solutions closer to the long-term optimal ones and the goal to assure acceptable computational time that rapidly grows up at increasing of the number of considered stops.

![](/api/attachments/FUDEAHWN/fulltext/images/455a8c98b9011c8a1ec3ac0902e5c0566cf523c58e07b672d5b739e4366e50e9.jpg)  
Fig. 1. Sequential optimization approach.

Successively, among the Pareto frontier solutions previously found out, the choice of the replacements con<sup>fi</sup>guration for the stop $j = 1$ that represents the best compromise between the cost and unavailability objectives, is made by means of the ELECTRE III method.

The optimization procedure will be again executed at $t = t _ { p }$ for the stop $j = 2$ by taking into account the replacements activities performed on the system during the previous one j=1 and considering one more time the optimization time frame T. In such a way the optimal replacements con<sup>fi</sup>gurations set for the scheduled stop $j = 2$ is singled out and, one more time again, among which the selection of the replacements con<sup>fi</sup>guration for the stop $j = 2$ is made by means of the ELECTRE III. Such optimization procedure will be sequentially repeated until the last stop $j = ( Q - 1 )$ will be reached.

Finally, at the end of the optimization cycle $j = Q ,$ it may be assumed that a major system overhaul will be performed and a new cycle will start again, then a new optimization procedure should be applied.

## 3. Mathematical problem formulation

The following basic nomenclature is hereafter used.

$i { = } 1 , 2 , . . . , N$ index representing a generic element;

$b = 1 , 2 , . . . B _ { i }$ index representing a generic branch of the component i; $k = 0 , 1 , . . . , ( P { - } 1 )$ index representing the last stop in which the replacement of the generic element has been performed. k takes value equal to zero if the generic element has never been replaced until the current stop;

$x _ { i , j }$ binary variable taking 1 if the element i is replaced at the stop j.

In order to obtain the optimal replacements con<sup>fi</sup>gurations set, that $\mathrm { i } s$ the Pareto frontier solutions for each system stop, the two following objective functions have to be optimized:

min C

ð<sup>1</sup>Þ

min U

ð<sup>2</sup>Þ

where C and U are the functions of the expected values of the total maintenance cost and the system unavailability respectively over the time frame value T that covers (P-1) system stops.

The cost function C can be expressed as:

$$
C = \sum_ {j = 1} ^ {P - 1} \left(C _ {j} + C _ {m. j}\right)\tag{3}
$$

where $C _ { m , j }$ is the cost of the minimal repair activities performed in the operative time between the stop j and the next one j+1 and $C _ { j }$ is the cost arising from the replacement of the selected elements performed during the stop j. The latter is given by the following relationship:

$$
C _ {j} = \sum_ {i = 1} ^ {N} \left(c _ {r i} + C _ {c p} \cdot t _ {r i}\right) \cdot x _ {i, j}\tag{4}
$$

with, $c _ { r i } , C _ { c p }$ and $t _ { r i }$ the spare parts cost, the unit time cost of the maintenance crew for replacement activities and the replacement time of the element i respectively.

In order to evaluate the duration of each system stop, it is herein assumed that the maintenance crews can operate in parallel during the replacement activities. That is, the maintenance crews can operate simultaneously each one on a different element belonging to the elements set to be replaced. In [14] an example of such strategy, that allows the reduction of the system stops duration, is described with relation to the maintenance global service contract between a maintenance services provider and the public company of the waste management of the City of Palermo (Italy).

In such condition, considering the stop j, the longest replacement time among those of the elements replaced determines the duration $T _ { j }$ of the considered system stop. Such condition is ensured by the following constraint:

$$
T _ {j} = \max \left\{t _ {r i} \cdot x _ {i, j} \right\} \quad \forall j, \forall i\tag{5}
$$

Moreover, in the considered optimization cycle of length $T ^ { * }$ it is supposed that the duration of each scheduled system stop has to be less or equal to the allotted time $T _ { a \cdot }$ Therefore the following constraint has to be satis<sup>fi</sup>ed:

$$
T _ {j} \leq T _ {a}
$$

$$
\forall j, \forall i\tag{6}
$$

The constraint (6) implies that, in the considered optimization cycle, the system elements characterized by a replacement time greater than the allotted time $T _ { a }$ cannot be replaced.

In the Eq. (3), $C _ { m , j }$ is the cost of the minimal repair activities performed in the operative time between the stop j and the next one j+1. It includes the costs of consumed materials, the allocated maintenance crews and, only in the case of hard failures, also those arising from the system downtime.

Instead, the cost of the minimal repair activities performed on the system components composed of series elements arranged in branches does not include the system downtime cost, since the failure on an own element (soft failure) does not imply the system failure.

In particular, considering a generic component $i _ { z } ,$ belonging to the set Z of the system components composed of series elements arranged in branches constituted of B branches (whose generic branch b is composed of $e _ { b }$ series elements), the related cost for the minimal repairs $C _ { m , i z , j }$ is given by the following equation:

$$
C _ {m, i _ {z}, j} = \sum_ {b = 1} ^ {B i} \sum_ {k = 1} ^ {e _ {b}} m _ {k, j} \cdot \left(c _ {m, k} + t _ {m, k} \cdot C _ {c m}\right) \quad \forall k \in i _ {z}\tag{7}
$$

with, $m _ { k , j } , c _ { m , k }$ and $t _ { m , k }$ the expected number of failures, the cost of the consumed materials related to the minimal repair activities and the minimal repair time of the element k respectively and $C _ { c m } ,$ , as before said, the unit time cost of the maintenance crew for minimal repair.

To the contrary, if the component i belongs to the set S of the system components composed by a single element, in addition the cost arising from the system downtime, that is $C _ { D T } ,$ has to be considered in the expression of its minimal repairs cost:

$$
C _ {m, i _ {s}, j} = \left\lfloor c _ {m, i _ {s}} + (C _ {D T m} + C _ {c m}) \cdot t _ {m, i _ {s}} \right\rfloor \cdot m _ {i _ {s}, j}\tag{8}
$$

Therefore, the cost of the minimal repair activities performed in the operative time between the stop j and the next one $j + 1 ~ C _ { m , j }$ is given by:

$$
C _ {m, j} = \sum_ {\forall i _ {z}} C _ {m, i _ {z}, j} + \sum_ {\forall i _ {s}} C _ {m, i _ {s}, j}\tag{9}
$$

Finally, the function of the expected system unavailability U over the time frame T can be expressed as:

$$
U = \sum_ {j = 1} ^ {P - 1} \sum_ {\forall i _ {s}} t _ {m, i _ {s}} \cdot m _ {i _ {s}, j}\tag{10}
$$

## 3.1. Expected number of failures and reliability calculation

The expected number of failures of the system elements, under the hypothesis of minimal repair of the hard and the soft failures, follows a non-homogeneous Poisson process (NHPP) with a power law intensity function. In such a case, its value for the element i, m<sub>i</sub>(t), considering the time period [0,t], is given by the following equation:

$$
m _ {i} (t) = \int_ {0} ^ {t} \lambda_ {i} (t) \cdot d t = \int_ {0} ^ {t} \frac {f _ {i} (t)}{R _ {i} (t)} \cdot d t = - \ln R _ {i} (t)\tag{11}
$$

being $\lambda _ { i } ( t ) , f _ { i } ( t )$ and $R _ { i } ( t )$ the failure rate, the probability density function and the reliability of the considered element respectively.

The reliability of the element $i , R _ { i , j } ( t )$ calculated at the generic scheduled stop j until the next one $j + 1$ , can be expressed as:

$$
R _ {i, j} = r _ {i, j, j} \cdot x _ {i, j} + \sum_ {k = 0} ^ {j - 1} \left(r _ {i, j, k} \cdot z _ {i, j, k}\right) \cdot \left(1 - x _ {i, j}\right)
$$

$$
\forall k / 0 \leq k <   j\tag{12}
$$

Whenever $x _ { i , j }$ is equal to 1, i.e. the element i is replaced during the stop j, its reliability value is given by $r _ { i , j , j } ( t )$ . On the contrary, if $x _ { i , j }$ is equal to zero, therefore the replacement of the element i has been performed during the stop k, with $k { < } j ,$ assuming $k = 0$ if the element i has not been replaced until the stop j. In such condition the reliability value of the element i is given by $r _ { i , j , k } ( t )$

According to the theory of the probability, the reliability value $r _ { i , j , j } ( t )$ in Eq. (12) is expressed by:

$$
r _ {i, j, j} = R _ {i, j} \left(t _ {j + 1} - t _ {j}\right) = R _ {i, j} \left(t _ {p}\right) \quad \forall j\tag{13}
$$

whereas the reliability value $r _ { i , j , k } ( t )$ , is given by the following equations:

$$
r _ {i, j, k} = \frac {R _ {i , j} (t _ {j + 1} - t _ {k})}{R _ {i , j} (t _ {j} - t _ {k})} = \frac {R _ {i , j} ((j + 1 - k) \cdot t _ {p})}{R _ {i , j} ((j - k) \cdot t _ {p})} \quad \forall j, \forall k \mid k \neq 0\tag{14}
$$

and

$$
r _ {i, j, k} = \frac {R _ {i , j} \left(t _ {j + 1}\right)}{R _ {i , j} \left(t _ {j}\right)} = \frac {R _ {i , j} \left(j \cdot t _ {p} + t _ {\text { start } , i}\right)}{R _ {i , j} ((j - 1) \cdot t _ {p} + t _ {\text { start } , i})} \quad \forall j \text {   and   with   } k = 0\tag{15}
$$

where $t _ { s t a r t , i }$ is the age of the element i at the beginning of the optimization procedure. The previous relationships do not take into consideration the system downtime caused by hard failure since the latter is negligible with respect to the interval $t _ { p } .$

By considering the Weibull probability distribution, with the shape parameter $\beta _ { i } > 1$ and the scale parameter $\eta _ { i } { > } 0 ,$ , the relations (13), (14) and (15) become:

$$
r _ {i, j, j} = \exp \left[ - \left(\frac {t _ {p}}{\eta_ {i}}\right) ^ {\beta_ {i}} \right] \quad \forall j\tag{16}
$$

$$
r _ {i, j, k} = \frac {\exp \left[ - \left(\frac {(j + 1 - k) \cdot t _ {p}}{\eta_ {i}}\right) ^ {\beta_ {i}} \right]}{\exp \left[ - \left(\frac {(j - k) \cdot t _ {p}}{\eta_ {i}}\right) ^ {\beta_ {i}} \right]} \quad \forall j, \forall k \mid k \neq 0\tag{17}
$$

$$
r _ {i, j, k} = \frac {\exp \left[ - \left(\frac {j \cdot t _ {p} + t _ {\text { start } , i}}{\eta_ {i}}\right) ^ {\beta_ {i}} \right]}{\exp \left[ - \left(\frac {(j - 1) \cdot t _ {p} + t _ {\text { start } , i}}{\eta_ {i}}\right) ^ {\beta_ {i}} \right]} \quad \forall j \text {   and   with   } k = 0\tag{18}
$$

Finally, the term z in Eq. (12) is a binary dummy variable that makes mutually exclusive the two conditions previously described, i.e. the two terms of the expression 12 related to the instant in which the element has been replaced, that is during the current stop j or during a previous stop. The previous requirements are ful<sup>fi</sup>lled by the following condition:

$$
z _ {i, j, k} = x _ {i, k} \cdot \prod_ {n = k + 1} ^ {j} \left(1 - x _ {i, n}\right) \quad \forall k / 0 \leq k <   j\tag{19}
$$

In such way, the following conditions are satis<sup>fi</sup>ed:

• When $x _ { i j }$ takes value equal to $1 , z _ { i j k }$ is equal to zero for any k;

• When $x _ { i j }$ is equal to zero, $z _ { i j k }$ is equal to 1 only for the stop k in which the last replacement of the element i has been performed.

## 3.2. Description of the Pareto frontier

In order to <sup>fi</sup>nd out the extreme Pareto optimal solutions, the Lexicographic Goal Programming (LGP) method is initially used (Deb, 2001). This method separately considers the two objective functions, thereby reducing the multi-objective problem into a mono-objective one. For example, these sequential steps determine the extreme solution of minimum cost:

• Minimizing C as a single objective problem obtaining $C ^ { m i n }$ ;

• Minimizing U, by imposing the value of C not greater than $C ^ { m i n } ,$ obtaining $\bar { U } ^ { \mathrm { m a x } }$

The procedure is analogously applied changing the objectives hierarchy to <sup>fi</sup>nd the other two bounds $\hat { C } ^ { m a x }$ and $U ^ { \mathrm { { m i n } } }$ of the extreme solution of minimum system unavailability. Once the extreme points of the Pareto frontier are determined, the ε constraint method is used to describe the whole Pareto optimal frontier. By using this method the multi-objectives optimization model described in Section 2.1 is modi<sup>fi</sup>ed in a single objective optimization model in which one of the two objectives has to be minimizing and restricting the remaining one within user speci<sup>fi</sup>ed values ε. In particular, to describe the Pareto frontier a multi-step optimization procedure has to be applied: in the <sup>fi</sup>rst step, minimizing C and imposing that the U function has to take a value less than $U ^ { \mathrm { m a x } } .$ In this way an optimal solution belonging to the Pareto frontier can be found. In the next step the procedure is repeated minimizing C and imposing that the U function has to take a value less than the one corresponding to the solution previously found. The procedure is repeated until the other Pareto frontier extreme solution is obtained. In such way, the ε constraint method ensures the determination of the whole Pareto frontier also in the presence of non-convex regions.

## 4. Selection of the Pareto solution by means of ELECTRE III

In the present section the fundamental features that characterize ELECTRE III are given. As said before ELECTRE III (Roy, 1990) [17] is the multi-criteria method proposed for choosing the solutions, which are the replacements con<sup>fi</sup>gurations to perform during each system stop. ELECTRE III is a multi-criteria decision-making method that re<sup>fl</sup>ects the decision maker's preferences and it can be applied when a set of alternatives must be ranked according to a set of criteria con<sup>fl</sup>icting each other or when just the preferred has to be selected. The method is based upon pseudo-criteria. Using proper thresholds, a pseudo-criterion takes into account the uncertainty and ambiguity that can affect the evaluation of the objectives, so that, if the difference in the performance of two solutions is minimal, according to a certain criterion, such solutions can be considered indifferent with respect to that criterion. Another peculiarity that differentiates ELECTRE III from other multi-criteria methodologies as the AHP, is that, as previously said in the introduction, it is not compensative, which means that a very bad score in one objective function is not compensated by good scores in the other one. In other words, the decision maker will not choose a solution if it is very bad compared to another one, even on a single criterion. It is understandable as in the treated case that the decision maker can put on this kind of behavior since she/he could not be unwilling to choose a solution with respect to another one if it presents an objective function value (cost or unavailability) higher of a certain threshold with respect to the considered objective function value of the second solution, independently from the objective function value assumed by the other objective function. This threshold is called veto threshold. Therefore, in ELECTRE III the concept of outranking relation is very important: a solution outranks another solution if suf<sup>fi</sup>cient reasons exist to assert that the <sup>fi</sup>rst is as good as the second and good reasons to reject such assertions do not exist. The outranking relation is based upon a concordance/discordance principle. This principle consists of the veri<sup>fi</sup>cation of the existence of a concordance of criteria in favor of the assertion that one solution is as good as another and that a veri<sup>fi</sup>ably strong discordance among the score values that may reject the previous assertion does not exist.

For each considered criterion, in our case cost and system unavailability, the following thresholds are introduced:

• q indifference threshold;

• p preference threshold;

• v veto threshold.

where $\mathsf { q } < \mathsf { p } < \mathsf { V } .$

Those threshold values can be expressed in term of percentage of the score differences assumed by the solutions, with respect to the worst one under the considered criteria.

Therefore, the decision maker is involved to supply his/her preferences by choosing the indifference, preference and veto thresholds for each objective function. Furthermore, the method allows to assign a relative weight to the considered criteria and this fact permits to represent different scenarios related to the importance attributed by the decision maker depending on the operative context in which she/he operates.

## 5. Case study

In order to show how the combined approach works a numerical case study is solved. In particular, it is considered a multi-component system that is periodically stopped to perform inspection and replacement activities for which the stop interval $t _ { p }$ is equal to 800 time units (T.U.) and the allotted time $T _ { a }$ is equal to 20 T.U. The system is composed, from a reliability point of view, of seven components arranged in series (see Fig. 2). The <sup>fi</sup>rst component is constituted by two branches each one composed of two elements; the second component is a simple parallel component with three branches, while the other components are constituted by a single element. Totally, the system is composed of 12 elements.

As said before, the reliability behavior of the elements is modeled by Weibull distributions whose parameters η and β are reported in Table 1. Table 1 also shows the cost data, expressed in monetary units (M.U.), the time data expressed in time units (T.U.) and the age of the system elements $t _ { s t a r t , i }$ at the beginning of the optimization cycle of length equal to $T ^ { * } { = } 2 4 0 0$ T.U. All the data have been randomly generated within opportune ranges. For each step, the model is solved by the commercial software Lingo.

The chosen optimization time frame value T is supposedly equal to the optimization cycle of length $T ^ { * }$ and therefore, the number of the scheduled system stops in which to <sup>fi</sup>nd out the replacements con<sup>fi</sup>gurations and the number of the stops covered by the time frame T is equal to 3 (Fig. 3).

![](/api/attachments/FUDEAHWN/fulltext/images/afa4ee56aaeb147033224dcc14c9d39c4e30a4547fcc7ef72c40b7d644071d46.jpg)  
Fig. 2. Multi-component system reliability block diagram.

Table 1 Case study data.

<table><tr><td>Element</td><td> $t_{start,i}$ </td><td> $t_{ri}$ </td><td> $t_{mi}$ </td><td> $C_{ri}$ </td><td> $C_{mi}$ </td><td> $\eta_i$ </td><td> $\beta_i$ </td></tr><tr><td>1</td><td>100.00</td><td>9.07</td><td>1.57</td><td>7.33</td><td>1.46</td><td>987.96</td><td>1.92</td></tr><tr><td>2</td><td>300.00</td><td>11.19</td><td>1.98</td><td>9.22</td><td>1.86</td><td>2772.96</td><td>1.38</td></tr><tr><td>3</td><td>300.00</td><td>10.82</td><td>2.13</td><td>7.50</td><td>1.71</td><td>2591.76</td><td>1.23</td></tr><tr><td>4</td><td>100.00</td><td>8.65</td><td>3.63</td><td>10.20</td><td>4.24</td><td>883.06</td><td>1.95</td></tr><tr><td>5</td><td>200.00</td><td>17.48</td><td>3.35</td><td>10.52</td><td>2.69</td><td>1983.67</td><td>1.38</td></tr><tr><td>6</td><td>300.00</td><td>22.18</td><td>3.89</td><td>11.82</td><td>3.51</td><td>1448.87</td><td>1.41</td></tr><tr><td>7</td><td>100.00</td><td>12.17</td><td>2.06</td><td>7.79</td><td>2.01</td><td>813.92</td><td>1.33</td></tr><tr><td>8</td><td>300.00</td><td>18.75</td><td>3.63</td><td>10.96</td><td>3.06</td><td>1218.47</td><td>1.81</td></tr><tr><td>9</td><td>100.00</td><td>15.91</td><td>2.97</td><td>9.05</td><td>2.50</td><td>3226.68</td><td>1.33</td></tr><tr><td>10</td><td>100.00</td><td>11.58</td><td>2.21</td><td>10.66</td><td>1.83</td><td>1350.61</td><td>1.68</td></tr><tr><td>11</td><td>200.00</td><td>17.63</td><td>3.26</td><td>11.48</td><td>2.71</td><td>1955.64</td><td>1.20</td></tr><tr><td>12</td><td>300.00</td><td>9.83</td><td>1.72</td><td>9.35</td><td>1.52</td><td>1531.56</td><td>1.67</td></tr><tr><td> $C_{DTm}$ </td><td>50.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $C_{cm}$ </td><td>2.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $C_{cp}$ </td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>T</td><td>2400</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Two scenarios have been hypothesized and each one is linked to the relative importance that the decision maker assigns to the objectives. The relative importance, translated in weights, is chosen equal to $W _ { c } { = } 0 . 9$ and $W _ { u } = 0 . 1$ (scenario 1) and $W _ { c } { = } 0 . 1$ and $W _ { u } = 0 . 9$ (scenario 2) for the cost C and the system unavailability U respectively, since those values represent extreme decisional contexts, that is extreme operative needs, in which the decision maker could make the decisions. The other values that the decision maker has to choose are those of the thresholds. In this case it is assumed that, for each objective, the threshold values are chosen with relation to the range of the objective values of the extreme Pareto solutions analyzed for the particular stop and scenario. However, the choice of the threshold values is explained in more detail in Appendix A.

Referring to Fig. 3, among the Pareto solutions found out for j=1, the choice of the replacements con<sup>fi</sup>guration is made by means of the ELECTRE III method. In such way, the two replacements con<sup>fi</sup>gurations will be chosen with relation to the two possible hypothesized scenarios.

The optimization procedure will be again executed for the next stop $j = 2 .$ The Pareto solutions are singled out taking into account the two replacements con<sup>fi</sup>gurations that can be performed on the system at j=1, considering one more time the optimization time frame T. The replacements con<sup>fi</sup>gurations for the stop j=2 will be chosen considering one more time again the two possible hypoth esized scenarios.

By iterating such procedure until the system stop j=3 is reached, all the decisions, that can be made during the considered optimization cycle, are determined. Table 2 shows all the replacements con<sup>fi</sup>gurations obtained for each system stop by reporting the elements to be replaced.

![](/api/attachments/FUDEAHWN/fulltext/images/dde18b4458b5a1fd2f9f8e72284523632990f16f24c5b54f7547595e496df54f.jpg)  
Fig. 3. Case study sequential optimization approach.

Table 2  
Replacements con<sup>fi</sup>gurations.

<table><tr><td>j=1</td><td>j=2</td><td>j=3</td></tr><tr><td rowspan="4">Scenario 1: (8,10,12)</td><td rowspan="2">Scenario 1: (8,10,11,12)</td><td>Scenario 1: (8,10,11,12)</td></tr><tr><td>Scenario 2: (8,9,10,11,12)</td></tr><tr><td rowspan="2">Scenario 2: (8,10,11,12)</td><td>Scenario 1: (8,10,11,12)</td></tr><tr><td>Scenario 2: (8,9,10,11,12)</td></tr><tr><td rowspan="4">Scenario 2: (8,10,11,12)</td><td rowspan="2">Scenario 1: (8,10,11,12)</td><td>Scenario 1: (8,10,11,12)</td></tr><tr><td>Scenario 2: (8,9,10,11,12)</td></tr><tr><td rowspan="2">Scenario 2: (8,9,10,11,12)</td><td>Scenario 1: (8,10,11,12)</td></tr><tr><td>Scenario 2: (8,9,10,11,12)</td></tr></table>

The total cost and the system unavailability values over the optimization cycle are shown in the Fig. 4 for all the decisions that can be made during the considered optimization cycle. In particular, each point is characterized by a triple of numbers in which the <sup>fi</sup>rst, the second and the third indicate the scenario hypothesized at the stop j=1, j=2 and j=3 respectively.

In Appendix A the sequential procedure applied to solve the case study is reported with more details.

## 6. Conclusions

The present paper aims to offer a useful methodological approach to dynamically support the decision maker in the selection of the elements of a multi-component system to replace during each scheduled and periodic stop.

Two objectives are considered to be reached, both to minimize over a <sup>fi</sup>nite optimization cycle, and in particular they are the expected total maintenance cost and the system unavailability. The developed approach combines the MOOP and the MCDM techniques. The optimal replacements con<sup>fi</sup>gurations for each system stop, i.e. the optimal Pareto frontier, are determined considering a <sup>fi</sup>nite optimization time frame that goes over the considered system stop, so to obtain the optimal solutions closer to the long-term optimal ones. Among these, the decision maker will choose the one that represents the best compromise between the considered objectives by means of the ELECTRE III method. The procedure is repeated for each scheduled system stop within the considered optimization cycle so as the information about the decisional context can be dynamically updated and therefore allowing, at each system stop, the selection of the replacements con<sup>fi</sup>guration most suitable to the decisional context.

The short computational time required by the combined approach makes the proposed procedure suitable to solve maintenance problems in real operative contexts in which the analysis focuses on large multicomponent system.

![](/api/attachments/FUDEAHWN/fulltext/images/aa0d183d557c819195585cf9aab38bc04ccfba1b0630842540dab3489b1399ad.jpg)  
Fig. 4. Total cost and system unavailability values over the optimization cycle.

## Appendix A

## A.1. System stop j = 1

The Pareto solutions are reported in Table A1.

Table A8  
Table A1  
Pareto solutions related to j=1.

<table><tr><td>Pareto solution</td><td>U</td><td>C</td><td>Replacements configuration</td></tr><tr><td>1</td><td>28.63</td><td>1857.53</td><td>8,12</td></tr><tr><td>2</td><td>27.66</td><td>1909.93</td><td>8,10,12</td></tr><tr><td>3</td><td>26.92</td><td>2017.70</td><td>8,10,11,12</td></tr><tr><td>4</td><td>26.64</td><td>2241.59</td><td>8,9,10,11,12</td></tr></table>

The objective values related to the extreme solutions, that is solution 1 and solution 4 in Table A1, differ in term of cost value of 17% with respect to worst value and of 7% in term of unavailability value. Therefore the following thresholds, reported in Table A2, are assumed.

Table A2  
Thresholds for ELECTRE III related to j=1.

<table><tr><td colspan="3">Cost thresholds (%)</td><td colspan="3">Unavailability thresholds (%)</td></tr><tr><td>Indifference</td><td>Preference</td><td>Veto</td><td>Indifference</td><td>Preference</td><td>Veto</td></tr><tr><td>3</td><td>10</td><td>15</td><td>1</td><td>4</td><td>6</td></tr></table>

By applying the ELECTRE III for each scenario the chosen solutions are those reported in Table A3.

Table A3  
Selected solutions for j=1.

<table><tr><td>Scenario</td><td>Chosen solution</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>3</td></tr></table>

## A.2. System stop j=2

Scenario 1 at the system stop j=1

The Pareto solutions are reported in Table A4.

Table A4  
Pareto solutions related to j=2 — scenario 1 at j=1.

<table><tr><td>Pareto solution</td><td>U</td><td>C</td><td>Replacements configuration</td></tr><tr><td>1</td><td>30.24</td><td>2157.82</td><td>8,10,12</td></tr><tr><td>2</td><td>28.10</td><td>2194.53</td><td>8,10,11,12</td></tr><tr><td>3</td><td>26.64</td><td>2355.16</td><td>8,9,10,11,12</td></tr></table>

The objective values related to the extreme solutions, that is solution 1 and solution 3 in Table A4, differ in term of cost value of 9% with respect to worst value and of 12% in term of unavailability value. Therefore the following thresholds, reported in Table A5, are assumed.

Table A5  
Thresholds for ELECTRE III related to j=2 — scenario 1 at j=1.

<table><tr><td colspan="3">Cost thresholds (%)</td><td colspan="3">Unavailability thresholds (%)</td></tr><tr><td>Indifference</td><td>Preference</td><td>Veto</td><td>Indifference</td><td>Preference</td><td>Veto</td></tr><tr><td>2</td><td>4</td><td>6</td><td>3</td><td>6</td><td>9</td></tr></table>

By applying the ELECTRE III for each scenario the chosen solutions are those reported in Table A6.

Table A6  
Selected solutions for j=2 — scenario 1 at j=1.

<table><tr><td>Scenario</td><td>Chosen solution</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>2</td></tr></table>

Scenario 2 at the system stop $j = 1$

The Pareto solutions are reported in Table A7.

## Table A7

Pareto solutions related to j=2 — scenario 2 at j=1.

<table><tr><td>Pareto solution</td><td>U</td><td>C</td><td>Replacements configuration</td></tr><tr><td>1</td><td>29.98</td><td>2144.08</td><td>8,10,12</td></tr><tr><td>2</td><td>28.10</td><td>2192.75</td><td>8,10,11,12</td></tr><tr><td>3</td><td>26.64</td><td>2355.16</td><td>8,9,10,11,12</td></tr></table>

The objective values related to the extreme solutions, that is solution 1 and solution 3 in Table A7, differ in term of cost value of 9% with respect to worst value and of 11% in term of unavailability value. Therefore the following thresholds, reported in Table A8, are assumed.

Thresholds for ELECTRE related to j=2 — scenario 2 at j=1.

<table><tr><td colspan="3">Cost thresholds (%)</td><td colspan="3">Unavailability thresholds (%)</td></tr><tr><td>Indifference</td><td>Preference</td><td>Veto</td><td>Indifference</td><td>Preference</td><td>Veto</td></tr><tr><td>3</td><td>6</td><td>8</td><td>3</td><td>6</td><td>8</td></tr></table>

By applying the ELECTRE III for each scenario the chosen solutions are those reported in Table A9.

Table A9  
Selected solutions for j=2 — scenario 2 at j=1.

<table><tr><td>Scenario</td><td>Chosen solution</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>3</td></tr></table>

A.3. System stop j = 3

Scenarios 1 and 2 at j=2 — scenario 1 at j=1

The Pareto solutions are reported in Table A10.

## Table A10

Pareto solutions related to j=3 — for both the scenarios at j=2 — scenario 1 at j=1.

<table><tr><td>Pareto solution</td><td>U</td><td>C</td><td>Replacements configuration</td></tr><tr><td>1</td><td>30.69</td><td>2282.58</td><td>8-10-12</td></tr><tr><td>2</td><td>28.82</td><td>2331.25</td><td>8-10-11-12</td></tr><tr><td>3</td><td>28.52</td><td>2407.74</td><td>8-9-10-12</td></tr><tr><td>4</td><td>26.64</td><td>2456.40</td><td>8-9-10-11-12</td></tr></table>

The objective values related to the extreme solutions, that is solution 1 and solution 4 in Table A10, differ in term of cost value of 7% with respect to worst value and of 13% in term of unavailability value.

Therefore the following thresholds are assumed. Since, as it is possible to note from the Table A6, the chosen solutions at j=2 by hypothesizing both the scenarios are coincident, the only following objective thresholds set has to be assumed (Table A11).

Thresholds for ELECTRE III related to j=3 — for both the scenarios at j=2 — scenario 1 at j = 1.

<table><tr><td colspan="3">Cost thresholds (%)</td><td colspan="3">Unavailability thresholds (%)</td></tr><tr><td>Indifference</td><td>Preference</td><td>Veto</td><td>Indifference</td><td>Preference</td><td>Veto</td></tr><tr><td>2</td><td>4</td><td>6</td><td>4</td><td>8</td><td>12</td></tr></table>

By applying ELECTRE III for each scenario the chosen solutions are those reported in Table A12.

Selected solutions for j=3 — for both the scenarios at j=2 — scenario 1 at j=1.

<table><tr><td>Scenario</td><td>Chosen solution</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>4</td></tr></table>

Scenario 1 at j=2 — scenario $2 \ : a t j = 1$

The Pareto solutions are reported in Table A13.

Pareto solutions related to j=3 — scenario 1 at j=2 — scenario 2 at j=1.

<table><tr><td>Pareto solution</td><td>U</td><td>C</td><td>Replacements configuration</td></tr><tr><td>1</td><td>30.69</td><td>2282.58</td><td>8-10-12</td></tr><tr><td>2</td><td>28.82</td><td>2332.00</td><td>8-10-11-12</td></tr><tr><td>3</td><td>28.52</td><td>2410.00</td><td>8-9-10-12</td></tr><tr><td>4</td><td>26.64</td><td>2456.40</td><td>8-9-10-11-12</td></tr></table>

The objective values related to the extreme solutions, that is solution 1 and solution 4 in Table A13, differ in term of cost value of 7% with respect to worst value and of 13% in term of unavailability value. Therefore the following thresholds, reported in Table A14, are assumed.

Thresholds for ELECTRE III related to j=3 — for scenario 1 at j=2 — scenario 2 at j=1.

<table><tr><td colspan="3">Cost thresholds (%)</td><td colspan="3">Unavailability thresholds (%)</td></tr><tr><td>Indifference</td><td>Preference</td><td>Veto</td><td>Indifference</td><td>Preference</td><td>Veto</td></tr><tr><td>2</td><td>4</td><td>6</td><td>4</td><td>8</td><td>12</td></tr></table>

By applying ELECTRE III for each scenario the chosen solutions are those reported in Table A15.

Selected solutions for j=3 — for scenario 1 at j=2 — scenario 2 at j=1.

<table><tr><td>Scenario</td><td>Chosen solution</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>4</td></tr></table>

Scenario 2 at j=2 — scenario $2 \ : a t j = 1$

The Pareto solutions are reported in the Table A16.

Pareto solutions related to j=3 — scenario 2 at j=2 — scenario 2 a $j = 1 .$

<table><tr><td>Pareto solution</td><td>U</td><td>C</td><td>Replacements configuration</td></tr><tr><td>1</td><td>29.87</td><td>2239.62</td><td>8-10-12</td></tr><tr><td>2</td><td>27.99</td><td>2305.55</td><td>8-10-11-12</td></tr><tr><td>3</td><td>26.64</td><td>2456.40</td><td>8-9-10-11-12</td></tr></table>

The objective values related to the extreme solutions, that is solution 1 and solution 3 in Table A16, differ in term of cost value of 9% with respect to worst value and of 11% in term of unavailability value. Therefore the following thresholds, as shown in the Table A17, are assumed.

Thresholds for ELECTRE III related to j=3 — scenario 2 at j=2 — scenario 2 at j=1.

<table><tr><td colspan="3">Cost thresholds (%)</td><td colspan="3">Unavailability thresholds (%)</td></tr><tr><td>Indifference</td><td>Preference</td><td>Veto</td><td>Indifference</td><td>Preference</td><td>Veto</td></tr><tr><td>3</td><td>6</td><td>8</td><td>3</td><td>6</td><td>9</td></tr></table>

By applying the ELECTRE III for each scenario the chosen solutions are those reported in Table A18.

Selected solutions for j=3 — scenario 2 at j=2 — scenario 2 at j =1.

<table><tr><td>Scenario</td><td>Chosen solution</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>3</td></tr></table>

## References

[1] N.S. Arunraj, J. Maiti, Risk-based maintenance policy selection using AHP and goal programming. Safety Science 48 (2010) 238-247.

[2] M. Bevilacqua, M. Braglia, The analytic hierarchy process applied to maintenance strategy selection, Reliability Engineering and System Safety 70 (2000) 71–83.

[3] R. Bris, E. Châtelet, F. Yalaoui, New method to minimize the preventive maintenance cost of series–parallel systems, Reliability Engineering and System Safety 82 (2003) 247-255.

[4] J.A. Caldeira Duarte, J.C. Taborda, J.T. Craveiro, T.P. Trigo, Optimization of the preventive maintenance plan of a series components system, International Journal of Pressure Vessels and Piping 83 (2006) 244–248.

[5] G. Campanella, A framework for dynamic multiple-criteria decision making, Decision Support Systems 52 (1) (2011) 52–60.

[6] M.C. Carnero, Selection of diagnostic techniques and instrumentation in a predictive maintenance program, a case study, Decision Support Systems 38 (4) (2005) 539–555.

[7] C.R. Cassady, E.A. Pohl, W.P. Murdock Jr., Selective maintenance modelling for industrial systems Journal of Ouality in Maintenance Engineering 7 (2) (2001) 104–117

[8] A. Certa, G. Galante, T. Lupo, G. Passannanti, Determination of Pareto frontier in multi-objective maintenance optimization, Reliability Engineering and System Safety 96 (2011) 861–867.

[9] A. Certa, M. Enea, G. Giacomo, T. Lupo, A multi-objective approach to optimize a periodic maintenance policy in: H. Pham (Ed.). Proceedings of the 18th ISSAT International Conference on Reliability and Quality in Design, July 26–28, 2012, (Boston) - ISBN: 978-0-9763486-8-9

[10] A. Certa, G. Galante, T. Lupo, A. Passannanti, G. Passannanti, A model for a periodic preventive maintenance policy for a series parallel system, Proceedings of the 19th FAIM International Conference on Flexible Automation and Intelligent Manufacturing, July 6–8, 2009, pp. 1026–1033, (Middlesbrought, UK), ISBN 978-0-9562303-3-1

[11] C.S. Chang, F. Yang, Inspection frequencies for substation condition-based maintenance, NPTS 2007: Proceedings of the Naval Platform Technology Seminar, Singapore May 16–17.

[12] K. Deb, Multi-objective optimization using evolutionary algorithms, John Wiley & Sons, New York 2001

[13] O. Hilber, V. Miranda, M. Matos, L. Bertling, Multiobjective optimization applied to maintenance policy for electrical networks, IEEE Transactions on Power System 22 (4) (2007).

[14] T. Lupo, An effective opportunistic maintenance policy for a global service International Journal of Service Science 3 (2010) 179–193.

[15] N. Papakostas, P. Papachatzakis, V. Xanthakis, D. Mourtzis, G. Chryssolouris, An approach to operational aircraft maintenance planning, Decision Support Systems 48 (4) (2010) 604–612.

[16] M. Pariazar, J. Shahrabi, M.S. Zaeri, Sh. Parhizi, A combined approach for maintenance strategy selection, Journal of Applied Sciences 8 (23) (2008) 4321–4329.

[17] B. Roy, The outranking approach and the foundations of ELECTRE methods, in: C.A. Bana e Costa (Ed.), Reading in Multiple Criteria Decision Aid, Springer Verlag, Berlin, 1990, pp. 155–183.

[18] T.L. Saaty, Fundamentals of decision making and priority theory with the analytic hierarchy process, RWS Publication, Pittsburg (PA), 2000.

[19] S. Taghipour, D. Banjevic, Periodic inspection optimization models for a reparable system subjected to hidden failure, IEEE Transactions on Reliability 60 (1) (2011) 275–285.

[20] S. Taghipour, D. Banjevic, A.K.S. Jardine, Periodic inspection optimization model for a complex repairable system, Reliability Engineering and System Safety 95 (2010) 944–952.

[21] Y.T. Tsai, K.S. Wang, L.C. Tsai, A study of availability-centered preventive maintenance for multi-component systems, Reliability Engineering and System Safety 84 (2004) 261–270.

[22] J.K. Vaurio, Availability and cost functions for periodically inspected preventively maintained units, Reliability Engineering and System Safety 63 (1999) 133–140

[23] H. Wang, A survey of maintenance policies of deteriorating systems, European Journal of Operational Research 139 (2002) 469–489.

Antonella Certa received the Master's degree in Management Engineering in 2004 and the Ph.D. degree in the Economic Analysis, Technology Innovation and Management of the Development Policy Studies Program in 2008 from the University of Palermo. She is currently a researcher and she is a professor of Industrial Plants at the Department of Production Engineering of the University of Palermo (divison of Agrigento). Dr. Certa's research interests are mainly focused on project management, multi-criteria analysis and maintenance optimization models.

Lupo Toni received the Master's degree in mechanical engineering from the University of Palermo, Italy in 1996, and the Ph.D. degree in Industrial Engineering from the same university in 2003. He is currently a researcher at the Department of Production Engineering of the University of Palermo and he is a professor of Quality Industrial Management. His research interests are in reliability optimization, and statistical method of reliabilit modeling. Dr. Lupo is a member of the Italian Association of Mechanical Technology.

Mario Enea is a full professor at the University of Palermo in Project Management, Industrial Plant Management and Applied Economics for Engineering. His research <sup>fi</sup>elds include production management, scheduling problems related to project management, optimal layout problems, environmental impact evaluation and waste management
