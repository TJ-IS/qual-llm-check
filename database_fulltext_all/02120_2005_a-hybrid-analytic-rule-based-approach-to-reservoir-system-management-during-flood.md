---
otero_id: 2120
otero_key: "TMPQGEZA"
title: "A hybrid analytic/rule-based approach to reservoir system management during flood"
authors: "A. Karbowski; K. Malinowski; E. Niewiadomska-Szynkiewicz"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid analytic/rule-based approach to reservoir system management during flood

A. Karbowski\*, K. Malinowski, E. Niewiadomska-Szynkiewicz

Institute of Control and Computation Engineering, Warsaw University of Technology, ul. Nowowiejska 15/19, 00-665 Warsaw, Poland

Received 28 March 2002; received in revised form 28 September 2003; accepted 1 October 2003 Available online 26 November 2003

## Abstract

The article presents an approach to real-time operation of a water retention reservoir during flood. Water releases are calculated repetitively on the basis of two-variant inflow forecasts and some expert knowledge. During every intervention of the control algorithm, an optimization problem with the expected value type performance index is solved. In the paper, the basic characteristics of trajectories of outflows resulting from the application of this control method are analyzed. Afterwards, the results of the series of simulation experiments based on a large set of historical data concerning a big Polish reservoir are presented.

<sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Water systems management; Forecasts; Flood control; Expert systems; Stochastic systems

## 1. Introduction

The main objective of a single retention reservoir management during flood is minimization of damages evoked by high water levels (large flows) downstream the reservoir.

Usually, these damages are a monotonically increasing function of the flow below the reservoir (both the peak and the volume greater than some threshold flows). However, in many practical situations, there are no uncontrollable side inflows in the vicinity of the reservoir and the river embankments are resistant enough and then the most important factor influencing the damages is the culminant flow. Thus, in such cases, from the mathematical point of view, to minimize the damages, it is sufficient to minimize the peak of the release from the reservoir.

In most publications concerning flood control, in both single and multiple reservoir systems, two inflow models were applied. The most popular approach consists in representing inflows by deterministic forecasts. Hence, the control problem is simply a deterministic optimization problem. Such problems were solved analytically in one reservoir case with simplified [3] and full [4] description of constraints, or numerically with the help of linear [12] or nonlinear programming [9,10]. The second approach consists in representing inflows as Markov processes and generating optimal control policies through stochastic dynamic programming algorithm, usually after transforming the problem to LQG formulation (i.e., problems with linear dynamics, quadratic cost and Gaussian, independent between subsequent time stages, disturbances), without [11] or with constraints [2].

However, in practice, we usually deal with something lying between these two approaches, namely with probabilistic forecasts, that is, with two [5] or, rather rarely, several predicted sequences of inflows with probabilities attached to them. Sometimes the worst case approach is used [7], but it is too pessimistic. It is known, that simple repetitive optimization of release trajectories does not always lead to good results [8] and two-stage feedback control is more useful. In this approach, at every time of intervention, we consider not one, but several forecasts of the disturbance and assume, that after the current optimization, there will be one more future optimization. At this future time, we will know, which of the currently considered inflow forecasts is actually the true one. In this way, during the next intervention, we will be solving a deterministic optimization problem.

Since forecasts are calculated with errors, it might be also useful to augment the employed mechanisms with some expert knowledge. Experts may at least assess the risk of implementing the release policies proposed by a computer, taking into account both the possibility of evoking an artificial flood by improper operation of the reservoir and too big influence of the reservoir management during flood—that is, in abnormal conditions—on the management in the rest of the year. Most of the time, the reservoirs are used to provide water supply to different users, to maintain desired flows in river channels and, most of them, to produce electricity. From the point of view of these additional functions of a reservoir, it is useful to decrease the capacity reserve and to have the reservoir full after the flood. These goals would not be in a conflict with the flood operations, if the inflow forecasts were perfect before the actual flood starts. Of course, this is impossible. Fortunately, the experts know about it and have their methods to solve this dilemma. Hence, we propose here an application to the calculated release proposal some additional expert rules of ‘‘if-then-else’’ type. This approach is something different than the most popular one, presented e.g., in Ref. [1], where the conditions of the rules define a quadrant in the Cartesian product of inflow and storage (one of four combinations ‘‘small’’ and ‘‘big’’) and the proposed release is simply a linear function of inflow with the optimized coefficient. The quadrants are joined smoothly with fuzzy operators. In our case, expert rules constitute a kind of postprocessing. The basic optimization of releases is performed earlier on the basis of numerical calculations.

## 2. Deterministic optimal control problem

As it was mentioned before, an important part of the flood control system is solution at some time instant s of the deterministic optimal control problem, in a single reservoir case, with the peak release as the objective. Denoting the inflow forecast by $\bar { d } ^ { \tau } ,$ , we may formalize this problem as follows:

$$
\min _ {u} \left[ J ^ {\tau} (u) = \max _ {t \in [ \tau , t, f ]} u (t) \right]\tag{1}
$$

$$
\dot {w} (t) = \bar {d} ^ {\tau} (t) - u (t)\tag{2}
$$

$$
w (\tau) = w _ {r} ^ {\tau}\tag{3}
$$

$$
w _ {\mathrm{min}} \leq w (t) \leq w _ {\mathrm{max}} \quad t \in [ \tau , t _ {\mathrm{f}} ]\tag{4}
$$

$$
u _ {\mathrm{min}} \leq u (t) \leq u _ {\mathrm{max}} (w (t))\tag{5}
$$

where [s,t<sub>f</sub>]-optimization horizon $( \tau \geq t _ { 0 } )$ , with $[ t _ { 0 } , t _ { \mathrm { f } } ]$ -control horizon (flood duration); u(.)-release from the reservoir over time period $[ \tau , t _ { \mathrm { f } } ] ; ~ \bar { d } ^ { \tau } ( . ) \cdot$ forecast of the inflow over time period $\left[ \tau , \ t _ { \mathrm { f } } \right]$ calculated at time s; w(t)-storage of the reservoir at time $t ; [ w _ { \mathrm { m i n } } , \ : w _ { \mathrm { m a x } } ] \mathrm { - r a n g e }$ of admissible storages; $u _ { \mathrm { m i n } } { - } \mathrm { l o w e r }$ release constraint; $u _ { \mathrm { m a x } } ( w )$ -upper release constraint (a function of storage); $w _ { \tau } ^ { r }$ actual storage at time s.

To assure the existence of solutions, we assume, that in the case when the reservoir is full, i.e., $w ( t ) = w _ { \mathrm { m a x } } ,$ it can pass any possible inflow, that is

$$
u _ {\max} (w _ {\max}) \geq \max _ {t \in [ \tau , t _ {\mathrm{f}} ]} \mathrm{d} (t)
$$

The problem is very easy to solve numerically, but to understand it deeper, it is useful to try to obtain its analytical solution.

From the point of view of the optimal control theory, problem (1) – (5) is quite complicated because of an untypical performance index (1) of the min-max type and presence of constraints on state values (4), and mixed, on control and state (5).

Rigorous analysis of this problem (considering deterministic, multiple peak inflow hydrograph $\bar { d } ^ { \tau } ( . ) )$ was given in Ref. [4]. The basic feature of the optimal release curves resulting from this analysis is that the maximal release $( { \mathrm { i . e . , ~ } } J ^ { \tau } ( { \hat { u } } ) { = } \operatorname* { m a x } _ { t \in [ \tau , t \mathrm { f } ] } ~ { \hat { u } } ( t ) )$ is realized as a constant function on one or more time intervals. The end points of these intervals are related to changes of the set of active constraints.

The second feature is that, usually, there are infinitely many optimal release curves (it is rather a typical thing in minimax problems), and the only common feature among them is that they are equal on the period when the maximal value of the performance index is realized.

The typical solution of the problem (1) – (5) is depicted in Fig. 1.

One may notice, that in the presented case both lower and upper state constraints (In Eq. (4)) were active- the first constraint is on the interval between 95th and 100th hour of the flood and the second after 170th hour.

Solving problem (1) – (5), we can obtain, for a given initial condition $w _ { r } ^ { \tau }$ and a forecast of inflow $\bar { d } ^ { \tau } ( . )$ , an optimal release trajectory uˆ (t) for $t { \in } [ \tau , \tau + \Delta t ]$ . Hence, we have, in this way, defined a control rule

$$
\hat {u} = \mathcal {R} (w _ {r} ^ {\tau}, \bar {d} ^ {\tau})\tag{6}
$$

## 3. Two-stage stochastic control algorithms

Before presenting two-stage algorithms for reservoir control during flood, we will make the following assumptions:

 The forecasting module calculates repetitively at time instants $\tau = t _ { 0 } , t _ { 0 } + \Delta t , t _ { 0 } + 2 \Delta t , . . . ,$ , inflow forecasts of two types (it is consistent with the guidelines of Polish water authorities):

 ‘‘small flood’’ (SF) forecast, which is calculated under the assumption that from now on there will be no rainfall in the river basin upstream the reservoir,

 ‘‘large flood’’ (LF) inflow forecast, which takes into account possible future precipitation,

We will denote these forecasts, accordingly, by $\bar { d } ^ { \tau } \mathrm { s F }$ and $\bar { d } _ { \mathrm { ~ \tiny ~ L F } } ^ { \tau }$ and the probabilities of their occurrence by $p _ { \mathrm { \Delta S F } } ^ { \tau }$ and $p _ { \mathrm { ~ L F } } ^ { \tau }$ Of course, they satisfy the condition $d ^ { \tau } { } _ { \mathrm { S F } } ( t ) < d ^ { \tau } { } _ { \mathrm { L F } } ( t ) , \forall t \in ( \tau , t _ { \mathrm { f } } ]$

 It is assumed at time s, that the next intervention after the current one will be performed at time $\tau _ { 1 } = \tau + \Delta t \in ( \tau , t _ { \mathrm { f } } )$ and until that time the constant release u¯ will be realized.

![](/api/attachments/TMPQGEZA/fulltext/images/a0bedc516e87a14227694b87ad506f264d9ac9c653d490340d67507809a7c7c7.jpg)  
Fig. 1. Typical solution of the problem (1) – (5) (flood in 1972 at Roz˙no\`w reservoir); s—beginning of the control horizon; t —end of the control horizon.

 It is assumed at time s that at time $\tau _ { 1 } ,$ we will know which of the currently considered two inflow forecasts is the true one. So, it is supposed that at $\tau _ { 1 } ,$ , the last intervention will be performed (because there is no need to repeat optimization after time $\tau _ { 1 }$ , if everything is known at $\tau _ { 1 } )$ . The optimal release $\tilde { u } _ { i } , ~ i \in \ \{ S F , \ L F \}$ within period $[ \tau _ { I } , \ t _ { \mathrm { f } } ]$ 4 assuming that the ith forecast is the real one, is calculated according to rule (6), that is as

$$
\tilde {u} _ {i} = \mathcal {R} (w _ {1 i} (\bar {u}), \bar {d} _ {i} ^ {\tau_ {1}})\tag{7}
$$

where

$$
w _ {1 i} (\bar {u}) = w _ {r} ^ {\tau} + \int_ {\tau} ^ {\tau_ {1}} \left[ \bar {d} _ {i} ^ {\tau} (t) - \bar {u} \right] d t\tag{8}
$$

is the predicted storage of the reservoir at time $\tau _ { 1 }$ and $\bar { d } _ { i } ^ { \bar { \tau } 1 }$ is the forecast $\bar { d } _ { i } ^ { \tau }$ due to the ith scenario, $i { \in } \{ S F , L F \}$ , cut to interval $\left[ \tau _ { 1 } , t _ { \mathrm { f } } \right]$

In this way, any constant release $\bar { u }$ on interval $[ \tau , \tau _ { 1 } )$ implies two different release trajectories $\tilde { u } _ { \mathrm { S F } } , \tilde { u } _ { \mathrm { L F } }$ on interval $[ \tau _ { 1 } , t _ { \mathrm { f } } ]$ that would be optimal for considered SF and LF forecasts $( \mathrm { F i g . } 2 )$ . Desired value of the initial release $\hat { \bar { u } }$ can be calculated in two ways. They stem from two different strategies of minimization of current and future damages under uncertainty. These strategies may be formulated as follows:

Strategy S1

Implement control $\hat { \bar { u } } _ { \mathrm { S 1 } }$ assuring, that the maximal of current (imminent) and expected future damages will be minimal. This control is determined by solving at every time $\tau ,$ the following two-stage optimization problem (for simplicity we omit the current time index s)

$$
\min _ {\bar {u}} \max [ \bar {u}, p _ {\mathrm{SF}} q _ {\mathrm{SF}} (\bar {u}) + p _ {\mathrm{LF}} q _ {\mathrm{LF}} (\bar {u}) ]\tag{9}
$$

where

$$
\begin{array}{l} q _ {i} (\bar {u}) = \max _ {t \in [ \tau_ {1}, t _ {f} ]} \tilde {u} _ {i} (t) \\ \quad = J \big (\mathcal {R} (w _ {1 i} (\bar {u}), \bar {d} _ {i} ^ {\tau_ {1}}) \big), i \in \{S F, L F \} \end{array}\tag{10}
$$

![](/api/attachments/TMPQGEZA/fulltext/images/664b650bf8de64b95833e47872b87ee9f30edd5c09e0166f87a21ff4d44cd7e6.jpg)  
Fig. 2. The principle of 2-stage control—decisions considered at time s. Notation: $\tilde { u } _ { \mathrm { L F } }$ —cutting release level for LF forecast calculated at time $\tau ,$ u¯ —cutting release level for SF forecast calculated at time $\tau , \tilde { u } _ { \mathrm { L F } }$ —release after time $\tau _ { 1 } ,$ calculated under the assumption that in interval [s, s<sub>1</sub>] the release u¯ will be realized and at time $\tau _ { 1 }$ the LF forecast will be valid; u˜ —release after time $\tau _ { 1 } ,$ calculated under the assumption that in interval $[ \tau , \tau _ { 1 } ]$ the release u¯ will be realized and at time $\tau _ { 1 }$ the SF forecast will be valid. The marked fields show the variations of the policy (u¯, $\tilde { u } _ { \mathrm { L F } } )$ and $( \bar { u } , \tilde { u } _ { \mathrm { S F } } )$ from $\bar { u } _ { \mathrm { L F } }$ and $\bar { u } _ { \mathrm { S F } }$

Strategy S2

Implement control $\hat { \bar { u } } _ { \mathrm { S } 2 }$ guaranteeing that the expected value of maximal future release will be minimal. The following optimization problem corresponds to this strategy:

$$
\min _ {\bar {u}} \left[ p _ {\mathrm{SF}} \max (\bar {u}, q _ {\mathrm{SF}} (\bar {u})) + p _ {\mathrm{LF}} \max (\bar {u}, q _ {\mathrm{LF}} (\bar {u})) \right]\tag{11}
$$

The determination of optimal controls $\hat { \bar { u } } _ { \mathrm { S 1 } }$ ant $\hat { \bar { u } } _ { \mathrm { S } 2 }$ is illustrated in Fig. 3.

The possibility of defining these two strategies results from the characteristics of the expected value of maximum of several arguments. In most optimal control problems, we deal with indices formulated as sums of stage costs. Because the expected value operator is linear, the expected total cost over the whole horizon is then equal to the sum of the expected stage costs. In the case of the maximumover-time performance index, as considered here, the situation is different, since, in general

$$
E \max (a, b) \neq \max (E a, E b)
$$

The first strategy S1 is related to the max $\mathbf { ( \mathrm { E a ; E b ) } }$ approach and can be given the following motivation:

We know, that except the current one, we will take, after some time, one more decision. The damages in the nearest future depend on our current policy (the value u¯ of the release that will be realized just after making the decision). We do not know, what the further damages will be, because we do not know the future inflow. Thus, we will estimate them using their expected value. Because the total damages will be equal to the maximum of the nearest and the further damages, we will look now for such a release, for which this maximum is minimal.

On the contrary, the second strategy S2 can be described in the following way:

Because in the future we will intervene one more time, the whole control horizon can be divided into two parts: from this moment until the time of the next intervention and from the time of the next intervention until the end of the horizon. For a given inflow forecast particular damages will occur. We will find such a release, that the expected value of those damages is minimal.

We can already see a practical drawback of the second argumentation. The performance index can easily be determined by the nearest damages, which can be assessed accurately, since we decide upon the value of u¯ at this very moment, while the further damages (i.e., after time $\tau _ { 1 } ) ,$ , depend on unknown inflow, more precisely on very inaccurate forecasts. While calculating the value of expression (11), the ‘‘origin’’ of the damages (the first or the next interval of the control horizon) is not taken into account. For example, it may occur, that someone will assign such a big probability to a high forecast, that the S2 strategy will simply mean the worst case control.

![](/api/attachments/TMPQGEZA/fulltext/images/71088461dec4401007671c5f630e97462a1bb475494b916db2de45e31b3a4f83.jpg)  
Fig. 3. Determination of the optimal releases corresponding to strategies S1 and S2. It is shown, that the optimal release $\bar { \hat { s _ { 2 } } }$ for the strategy S2 even for quite a big value of the probability of $p _ { \mathrm { L F } }$ equals $\boldsymbol { \bar { u } } _ { \mathrm { S F } } ,$ , that is the optimal release for SF inflow forecast. At the same time, the optimal release $\bar { \hat { S 2 } }$ for the strategy S1 lies between $\bar { u } _ { \mathrm { S F } }$ and $\boldsymbol { \bar { u } } _ { \mathrm { L F } } ,$ closer to one or the second end of the interval, depending on the probabilities $p _ { \mathrm { S F } }$ and $p _ { \mathrm { L F } } .$

It is obvious, that (see Fig. 3)

$$
\bar {\hat {s}} _ {1} \in (\bar {u} _ {\mathrm{SF}}, \bar {u} _ {\mathrm{LF}})\tag{12}
$$

for all 0 < p<sub>SF</sub>, p<sub>LF</sub> < 1; p<sub>SF</sub> + p<sub>LF</sub> = 1.

On the contrary, an important characteristic of the control computed according to strategy S2 is ‘‘sticking’’ of the optimal solution to the ends of the interval $[ \bar { u } _ { \mathrm { S F } } , \bar { u } _ { \mathrm { L F } } ]$ . If both forecasts are equally probable, and even, when more probable is the bigger (LF) forecast, it may happen, that the optimal release u<sup>ˆ</sup>¯<sub>S2</sub> will be the one corresponding to the smaller (SF) forecast (Fig. 3). Yet, it can be very dangerous, because the reservoir may be filled too early-for instance, before the peak of the actual inflow. For some combination of probabilities $p _ { \mathrm { S F } }$ and $p _ { \mathrm { L F } } ,$ it may also happen, that either $\bar { u } _ { \mathrm { S F } }$ or $\boldsymbol { \bar { u } } _ { \mathrm { L F } }$ will be chosen, that is, there will occur frequent ‘‘jumps’’ that are always unwelcome.

The strategy S1 is devoid of these drawbacks and produces more ‘‘balanced’’ release trajectory, which makes use of more information, including both forecasts-SF and LF.

## 4. Additional expert protection mechanisms

Due to a very high level of uncertainty with respect to the inflow to a reservoir (caused by large errors in meteorological forecasting of future precipitation) and its violent character, and also, because it is rather a rare phenomenon (big flood usually occurs once for many years), the mechanisms described above might be insufficient. First of all, very inaccurate, too high inflow forecasts may induce very high releases; which in the case, when the actual inflows are much smaller, is equivalent to evoking a man-made flood. Because most of the reservoirs are used also for other than flood control purposes, as water supply to different users, maintenance of desired flows in river channels, and, possibly, the production of electricity, it will cause additional big losses related to the shortage of the water stored after flood.

To avoid, or rather to minimize the probability of such situations, some protection mechanisms may be proposed [6].

Briefly, these mechanisms consist in projection of the optimal solution $\hat { \bar { u } }$ (either $\hat { \bar { u } } _ { \mathrm { S 1 } }$ or $\hat { \bar { u } } _ { \mathrm { S } 2 } \mathrm { \bar { ) } }$ of the twostage control problem discussed in the previous section, onto some intervals resulting from an analysis of the risk of evoking a manmade flood and too big evacuation of the reservoir.

The projection algorithm takes into account such parameters of every water retention reservoir as:

QD-admissible flow, i.e., the maximal discharge which does not create serious damage downstream of the reservoir.

QU-useful outflow, which is desirable to be maintained during normal operating conditions.

RV-mandatory reserve capacity to be maintained during the conservation control period.

and some parameters characterizing the present and predicted for the nearest future situation. These parameters are:

$w _ { \textit { r } } ^ { \tau }$ -current storage of the reservoir (measured), $d ( \tau )$ -current inflow to the reservoir (measured), u¯ -cutting release for underestimated (SF) forecast,

$\bar { d } _ { \mathrm { S F } } ^ { \tau \mathrm { c u l } }$ -peak of the SF forecast, i.e.,

$$
\bar {d} _ {\mathrm{SF}} ^ {\tau c u l} = \max _ {t \in [ \tau , t _ {\mathrm{f}} ]} \bar {d} _ {\mathrm{SF}} ^ {\tau} (t)\tag{13}
$$

$\bar { u } ^ { \mathrm { m } }$ -maximal evacuating release which, if it is implemented from the current time s during $\Delta t$ (that is until the next intervention at $\tau + \Delta t )$ , will still make it possible to restore the mandatory storage $w _ { r } ^ { \tau } = w _ { \mathrm { m a x } } - \mathrm { R V } ;$ it is calculated for the worst case, that is while assuming that the lower boundary for the inflow, i.e., the SF forecast, will actually happen, from the equation:

$$
\begin{array}{l} w _ {r} ^ {\tau} + \int_ {\tau} ^ {t _ {f}} \bar {d} _ {\mathrm{SF}} ^ {\tau} (t) \mathrm{d} t - \bar {u} ^ {m} \Delta t - \mathrm{QU} [ t _ {\mathrm{f}} - (\tau + \Delta t) ] \\ = w _ {\max} - \mathrm{RV} \end{array}
$$

The expert decision rule can now be expressed as follows:

$$
\hat {\bar {u}} ^ {*} = \left\{ \begin{array}{l l} \min [ \max (\mathrm{QU}, \bar {u} ^ {\mathrm{m}}), \max (\mathrm{QD}, \bar {u} _ {\mathrm{SF}}) ] & \text { when } \mathrm{d} (\tau) <   \mathrm{QD} \\ & \text { and } w _ {r} ^ {\tau} \leq w _ {\max} - \mathrm{RV} \\ \max [ \mathrm{QD}, \min (\bar {\hat {a}} _ {\mathrm{SF}} ^ {\tau_ {\mathrm{cul}}}) ] & \text { otherwise } \end{array} \right.\tag{14}
$$

The first expression in Eq. (14) concerns the period, when the inflow is still below the threshold level QD and the reservoir has free capacity higher than RV. The biggest danger in this period is the possibility of evacuating the reservoir too much because of too high inflow forecasts. Because of that, the high inflow (LF) forecast is completely ignored, and the decision is based only on the measurements and the low (SF) forecast. The sense of the proposed projection is to ensure that the resulting release will be admissible (i.e., higher than QU—it is guaranteed by the first inner maximization), and it will exceed the threshold level QD only, when for sure the flood will be bigger than QD (because only in that case the cutting level for the SF forecast $\bar { u } _ { \mathrm { S F } }$ is greater than QD). At the same time, the resulting release cannot be greater than the maximal value $\bar { u } ^ { \mathrm { { - m } } }$ , that allows for restoring the mandatory capacity $w _ { \mathrm { m a x } } - R V$ after the next intervention and before the end of flood (that is in time period $[ \tau + \Delta t , t _ { \mathrm { f } } ] )$ . So, in the worst case, from the point of view of the possibility of too big evacuation of the reservoir, when the lowest forecast $\bar { d } _ { \mathrm { S F } } ^ { \ \tau }$ will actually happen, we will be able to refill the reservoir until the mandatory level $w _ { \mathrm { m a x } } - \mathrm { R V } .$

The second expression in Eq. (14) concerns the remaining part of the flood period, i.e., when the inflow is higher than QD or the reserve is smaller than the mandatory one RV. The projection assures then that the release is not less than QD and at the same time not greater than the peak of the SF forecast. If the release proposal resulting from one of the mechanisms presented in the previous section belongs to this interval, it is implemented. If not, its projection on the interval specified in Eq. (14) replaces it. More argumentation and discussion of the presented protection mechanisms may be found in Ref. [6].

## 5. Case study results

Presented control algorithms were used to simulate the operation of the Roz˙no\`w reservoir, which is located on the Dunajec river in the southern part of Poland. It is one of the biggest Polish reservoirs having capacity of $1 7 1 \times 1 0 ^ { 6 } \ \mathrm { m } ^ { 3 }$ . The simulation was performed on a set of historical data containing 50 hydrographs of summer floods from years 1899 to 1987. These hydrographs were of different duration (from 72 to 900 h) with peak flows between 405 and 3237 $\mathrm { m } ^ { 3 } / \mathrm { s }$ . Simulations were performed under the following conditions:

 initial storage of the reservoir $w ( t _ { 0 } ) = 9 0 \times 1 0 6 \ \mathrm { m } ^ { 3 }$

 time period between subsequent interventions $\Delta t = 3$ h

 forecasting horizon $\Delta t ^ { \prime } = 4 8 \ 1$ h

 admissible flow $\mathrm { Q D } { = } 9 0 0 ~ \mathrm { m } ^ { 3 } / \mathrm { s }$

Forecasts $( \mathrm { i . e . }$ , the sequence of pairs $\bar { d } _ { \mathrm { S F } } ^ { \tau } , ~ \bar { d } _ { \mathrm { L F } } ^ { \tau }$ for $\tau = t _ { 0 } , ~ t _ { 0 } + \Delta t , ~ t _ { 0 } + 2 ~ \Delta t , . ~ . . )$ were calculated due to two different models (so-called forecast dummies) prepared in two: Cracow and Warsaw divisions of the Institute of Meteorology and Water Management. We will denote them by, accordingly, CFM (Cracow Forecasting Model) and WFM (Warsaw Forecasting Model). These dummy forecast mechanisms were supposed to imitate the work of the actual real-time forecasting models. The imitation is understood here as producing forecasts with errors of the same distribution as the actual real-time forecasting routines.

The WFM is related to characteristics of existing operating forecasting routines while the CFM concerns improved techniques, which will replace WFM. The average instant error for forecasts calculated according to CFM was equal to 0.8% for LF forecast and 4.35% for SF forecast, while in the case of WFM, the appropriate errors were equal to 6.93% and 8.36%. The standard deviation of this errors in all cases was in interval 1.3–1.5 of the average error.

Since it is impossible to know exactly the values of p<sub>SF</sub>, $p _ { \mathrm { L F } }$ (actually, they are provided by subjective assessment), we performed simulations for different combinations of these probabilities covering the whole range [0,1].

![](/api/attachments/TMPQGEZA/fulltext/images/8e65a0bac142bc5fcb67f507446a5856225db4e2abc673c0da3068b10fc29fc1.jpg)  
trad. instructionstrategy S1strategy S2S1/S2 + prot. mech  
Fig. 4. Average reduction of the maximal discharge from Roz˙no´w reservoir for forecasts calculated due to CFM.

The simulation results are presented in Fig. 4 (CFM) and Fig. 5 (WFM).

For comparison, they are shown on the background of characteristics of the traditional instruction (i.e., the instruction that is still applied; it uses only LF forecast). The shapes of the resulting hydrographs for typical small and large actual floods in case when $p _ { \mathrm { S F } } { = } p _ { \mathrm { L F } } { = } 0 . 5$ are presented in Figs. 6–9.

The conclusions which can be drawn are the following:

 In the case of good forecasts (see Fig. 4), the proposed algorithms are much better than the traditional instruction, assuring about 25% greater reduction of the peak of inflow (equal to 40% reduction). The best results are achieved when the probability of SF is smaller than 0.5, but not very small (about 0.3).

![](/api/attachments/TMPQGEZA/fulltext/images/666e27b4169d8c5660f6899d32b02732b94f7b2e16d442675888bc85914e872d.jpg)  
trad. instructionstrategy S1strategy S2S1/S2 + prot. mech  
Fig. 5. Average reduction of the maximal discharge from Roz˙no´w reservoir for forecasts calculated due to WFM.

![](/api/attachments/TMPQGEZA/fulltext/images/d8293102518487dbe6427a213450d54f568ebe854d951895cbbee2ab3aa3aef8.jpg)  
Fig. 6. Typical shapes of hydrographs obtained for different control algorithms and forecasts due to CFM for large actual flood with equal probabilities of SF and LF.

 The deterioration of the quality of forecasts causes very big decrease of the reduction of the peak of inflow (see Fig. 5). The proposed mechanisms in their pure form do not bring any improvement in relation to the traditional management and quite often are simply worse (their provide 10–12% of reduction, while traditional instruction 18%). In such situation, it is eligible to ‘‘stiffen’’ the instruction by supplementary security constraints. Then, we can double the reduction to the level 27%.

 Figs. 4 and 5 show that the ‘‘probabilities’’ attached to forecasts influence the effects of control, but fortunately, only to some extent. It is rather a good feature of the proposed instructions, since, as it was explained above, the actual probabilities are not known, and the values p<sub>SF</sub> and $p _ { \mathrm { L F } }$ that we use, are based on a subjective assessment.

![](/api/attachments/TMPQGEZA/fulltext/images/db09866dbc0b390c28fdcb8925141d0867b4f4f8671ce000337d434d73b10daa.jpg)  
Fig. 7. Typical shapes of hydrographs obtained for different control algorithms and forecasts due to WFM for large actual flood with equal probabilities of SF and LF.

![](/api/attachments/TMPQGEZA/fulltext/images/629d9cf3523a0481a46db79c4570398ccfa59b79be23f92972eff36ae5bfa95b.jpg)  
Fig. 8. Typical shapes of hydrographs obtained for different control algorithms and forecasts due to CFM for small actual flood with equal probabilities of SF and LF.

 Traditional instruction proved to be insensitive to changes in the quality of forecasts. In both cases (see Figs. 4 and 5), it produces the reduction of peak of practically the same level (about 18%). It means that this instruction is robust and insensitive to bad forecasts, but, on the other hand, it does not ‘‘consume’’ good forecasts, when (like in the deterministic case) it is not very difficult to achieve a big reduction of damages.

![](/api/attachments/TMPQGEZA/fulltext/images/abe848a39a3c9dad97d3290b3155d88e342a62f6acff0cac4a0344b2436217c7.jpg)  
Fig. 9. Typical shapes of hydrographs obtained for different control algorithms and forecasts due to WFM for small actual flood with equal probabilities of SF and LF.

 In almost all cases, in a big range of probabilities, strategy S1 proved to be better than strategy S2.

 Additional protection mechanisms turned out to be so strong, that practically after their application all differences between releases resulting from two strategies S1 and S2 disappeared. They are useful, however, only in the case of bad forecasts.

Let us consider now the shape of hydrographs resulting from the application of the considered mechanisms to data concerning one the biggest flood in Poland in XXth century, from 1958, and to the ‘‘average’’ flood in 1965.

It is seen that for the big flood of 1958 and good forecasts (CFM—see Fig. 6), the additional protection mechanisms do not induce too big changes between the releases resulting from different strategies (the flood is ‘‘cut’’ efficiently independently of the instruction, always better than in the case of the traditional instruction), while for bad forecasts (WFM—see Fig. 7), these mechanisms improve noticeably the effects of control. In the case of small 1965 flood (see Figs. 8 and 9), the mechanisms improve the effects of control for bad forecasts (WFM—see Fig. 9) and deteriorate (not too much) for good forecasts (CFM—see Fig. 8), the obtained release, however, still does not exceed the admissible level QD.

## 6. Conclusions

The effective operation of retention reservoirs during flood is a big challenge to control engineers. Due to a high level of inaccuracy of inflow forecasts, the applied control mechanisms have to be more complicated than in other cases.

This may be obtained through the application of properly defined two-stage control scheme and introduction of some elements of intelligent control. The first component allows for more robust reaction to the uncertainty of inflows in terms of current and future releases (and the damages related to them). The second component takes into account the risk of too big evacuation of the reservoir and evoking a man-made flood.

The results of the series of simulations fully confirmed the effectiveness of such a mixed analytical/rule-based approach.

## Acknowledgements

The work reported in this paper was supported by KBN grant No. 7 T11A 022 20.

## References

[1] F.J. Chang, C. Li, Real-coded algorithm for rule-based flood control reservoir management, Water Resources Management 12 (3) (1998) 185– 198.

[2] A.P. Georgakakos, D.H. Marks, A new method for the realtime operation of reservoir systems, Water Resources Research 23 (7) (1987) 1376–1390.

[3] W.C. Hughes, Flood control release optimization using methods from calculus, Journal Of Hydraulic Division ASCE 97 (5) (1971) 691 – 704.

[4] A. Karbowski, Optimal control of single retention reservoir during flood; analytical solution of deterministic, continuoustime problems, Journal of Optimization Theory and Applications 69 (1) (1991) 55– 81.

[5] R. Krzysztofowicz, L. Duckstein, Preference criterion for flood control under uncertainty, Water Resources Research 15 (3) (1979) 513– 520.

[6] K. Malinowski, J. Z<sup>˙</sup> elazin´ski, Reservoir systems: operational flood control, in: M.G. Singh (Ed.), Systems and Control Encyclopedia Supplementary vol. 1,Pergamon, New York, 1990, pp. 495– 503.

[7] J.L. Marien, J.M. Damazio, F.S. Costa, Building flood control curves for multipurpose multireservoir systems using controllability conditions, Water Resources Research 30 (4) (1994) 1135– 1144.

[8] E. Niewiadomska-Szynkiewicz, K. Malinowski, A. Karbowski, Predictive methods for real-time control of flood operation of a multireservoir system: methodology and comparative study, Water Resources Research 32 (9) (1996) 2885–2895.

[9] R. Pytlak, K. Malinowski, Optimal Scheduling of Reservoir Releases During Flood: Deterministic Optimization Problem, Part 1 and Part 2. Journal of Optimization Theory and Applications, 61 (3) (1989) pp. 409 – 432 and 433 – 449.

[10] O.I. Unver, L.W. Mays, Model for real-time optimal flood control operation of a reservoir system, Water Resources Management 4 (1) (1990) 21 – 26.

[11] S.A. Wasimi, P.K. Kitanidis, Real-time forecasting and daily operation of a multireservoir system during floods by linear quadratic Gaussian control, Water Resources Research 19 (6) (1983) 1511 – 1521.

[12] J.S. Windsor, Optimization models for the operation of flood control systems, Water Resources Research 9 (5) (1973) 1219– 1226.

![](/api/attachments/TMPQGEZA/fulltext/images/a479e7cf93575df6686a9dc1672ebaf367ab277322b53cd5b444160f781d8d5c.jpg)

Andrzej Karbowski, Doctor of technical sciences, MEng (1983), Ph. D (1990) in Control and Computer Engineering. Since 1983 with Warsaw University of Technology, lecturer on optimal control in risk conditions and parallel and distributed computing. Since 2001 he is also with Research and Academic Computer Network (NASK). He was involved in a number of research projects including three EU projects. He is the author of over 50 journal and

conference papers and co-author of one book. His scientific interests concentrate on optimal control in risk conditions, decomposition and parallel implementation of numerical algorithms, computer networks, environmental systems management.

![](/api/attachments/TMPQGEZA/fulltext/images/b6125f0e62f07811dd35f509b6d41b446e78dd2981d643ae16e8f6acf6f3304a.jpg)

Krzysztof Malinowski, Professor of technical sciences, MEng (1971), PhD (1974), DSc (1978), ordinary professor of control and information engineering and the head of Control and Optimization of Complex Systems Group at Warsaw University of Technology (at the Institute of Control and Computational Engineering), member of the Polish Academy of Sciences. Director of the Institute of Control and Computations Engineering 1984 – 1996, Dean of

the Faculty of Electronics and Information Technology 1996 – 1999. Since 2001 he is also with Research and Academic Computer Network (NASK). Visiting professor at the University of Minnesota in 1978 – 1979, served as a consultant to the Decision Technologies Group of UMIST in Manchester.

He was involved in a number of research projects including several EU projects. He is the author or co-author of four books and over 130 journal and conference papers. His current interests are control, simulation and optimization of complex systems, computer networks.

![](/api/attachments/TMPQGEZA/fulltext/images/3b360c1e6c9401388b0df2fd496324be86067f278da4b0f95ed8914471c0676b.jpg)

Ewa Niewiadomska-Szynkiewicz, Doctor of technical sciences, MEng (1986), Ph. D. (1996) in Control and Computer Engineering. Since 1987 with Warsaw University of Technology, lecturer on simulation technologies and optimization techniques. Since 2001 she is also with Research and Academic Computer Network (NASK). She was involved in a number of research projects

including three EU projects. She is the author of over 50 journal and conference papers and co-author of one book.

Her current interests are: global optimization, computer simulation, parallel simulation, computer networks and environmental systems management.
