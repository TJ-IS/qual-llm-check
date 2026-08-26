---
otero_id: 1512
otero_key: "Q4WRKQFK"
title: "Rescheduling of elective patients upon the arrival of emergency patients"
authors: "Ergin Erdem; Xiuli Qu; Jing Shi"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Rescheduling of elective patients upon the arrival of emergency patients

Ergin Erdem <sup>a</sup>, Xiuli Qu <sup>b</sup>, Jing Shi <sup>a,</sup>⁎

<sup>a</sup> Department of Industrial and Manufacturing Engineering, North Dakota State University, Fargo, ND 58108, USA

<sup>b</sup> Department of Industrial and Systems Engineering, North Carolina A&T State University, 1601 E. Market Street, Greensboro, NC 27411, USA

## a r t i c l e i n f o

Article history: Received 30 November 2011 Received in revised form 5 July 2012 Accepted 11 August 2012 Available online 21 August 2012

Keywords: Elective surgery Rescheduling Emergency admission Operating room Mixed integer linear programming Genetic algorithm

## a b s t r a c t

In this study, a mixed integer linear programming (MILP) model is developed for rescheduling elective patients upon the arrival of emergency patients by considering two types of clinical units, namely operating rooms and post-anesthesia care units (PACUs). The model considers the overtime cost of the operating rooms and/or the PACUs, the cost of postponing or preponing elective surgeries, and the cost of turning down the emergency patients. The results indicate that a mainstream commercial solver can ef<sup>fi</sup>ciently <sup>fi</sup>nd an optimal solution in a particular scenario with light elective surgery load, but becomes very inef<sup>fi</sup>cient in searching optimal solutions in all other scenarios. As such, a genetic algorithm is developed to ef<sup>fi</sup>ciently obtain the approximately optimal solutions in those scenarios that are dif<sup>fi</sup>cult for the commercial solver. In the genetic algorithm, a novel chromosome structure is proposed and applied to represent the feasible solutions to the MILP model. It is shown that for the scenarios with heavy load of elective surgeries, the genetic algorithm can <sup>fi</sup>nd approximate optimal solutions signi<sup>fi</sup>cantly faster than the commercial solver. In practice, the two solution methodologies should be used jointly to provide hospitals a solid tool for making sound and timely decisions in admitting emergency patients and rescheduling elective patients.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due to the mounting costs, the healthcare industry is in urgent need of ef<sup>fi</sup>ciently allocating the scarce resources in the presence of con<sup>fl</sup>icting objectives [1,2]. Decision tools have been developed in literature to improve the ef<sup>fi</sup>ciency of healthcare delivery services such as improving the prognosis associated with coronary surgeries [3], predicting the length of stay based on the injury severity index to improve bed planning [4], predicting the amount of blood transfusion for surgical patients during peri-operative stage [5], and increasing the throughput and decreasing the variability of open access appointment systems by a mean-variance model [6].

Operating rooms are considered to be one of the major revenue sources and the cost centers of healthcare facilities. The resources allocated to operating rooms are costlier than those allocated to other clinical units in healthcare settings. The fact urges researchers and practitioners to pay special attention to managing and scheduling operating rooms and therefore allocating the resources in the best way possible [7–9]. The admission of emergency patients is an important issue for operating rooms. It might become a hindrance for the entire system if without adequate resources, which will result in the delay of elective surgeries and the disruptions of patient <sup>fl</sup>ow. A concerted effort is required for optimal allocation of resources to mitigate the disruptions [10]. This could be achieved by sound rescheduling decisions of elective surgeries in a timely manner upon the arrival of emergency patients. The overall goals of rescheduling include, but are not limited to, ensuring the patient safety and optimal patient outcome, increasing the utilization of staff and equipment, reducing the delays, and enhancing overall staff, patient, and surgeon/physician satisfaction.

The clinic resources located downstream in the patient <sup>fl</sup>ow should be considered for effectively managing operating rooms, but this is a very complicated and challenging issue. For instance, after surgery, usually a patient recovers from the effects of the anesthesia at a PACU. In order to transfer the patient to the PACU, the resources should be available. Otherwise, the transfer might be delayed, which usually leads to the disruption of surgery schedule in the operating rooms. Meanwhile, the admission of emergency patients might disrupt the current schedule of elective surgeries and thus require the elective surgeries to be rescheduled. In this study, we aim at developing an integrated decision making model for rescheduling the elective patients upon the arrival of emergency patients under various constraints such as the availability of beds and/or supporting staff at PACUs. The objective is to minimize the costs incurred due to the disruptions.

## 2. Literature review

The urgency of surgery admissions plays an important role in planning and managing the operating rooms. The surgeries can be usually categorized as emergent, urgent, or elective surgeries. The emergency patients need to be operated immediately upon the admission. In case of urgent admissions, the patient condition can be stabilized to a certain extent, and the surgery can take place after a certain period of time (i.e., a couple of hours). Generally, the admission of emergency or urgent patients to medical facilities is unplanned. If no adequate dedicated resources are allocated for those patients, disruptions are likely to occur for the current schedule of elective surgeries. In the literature, numerous studies have been conducted to develop mathematical models for the management of operating rooms with special emphasis on scheduling elective and/or emergency patients [11–13]. Usually, those studies assume that elective surgeries and emergency surgeries have their own dedicated operating rooms.

There are a few scheduling studies considering elective and nonelective cases which share the operating rooms [14]. Lamiri et al. [15,16] study the problem of scheduling operating rooms which are shared between elective and emergency surgeries by assuming uncertain demands for emergency surgeries. The set of elective surgeries scheduled is determined such that the patient related costs and the expected overtime utilization costs of operating rooms are minimized. Wullink et al. [17] develop discrete event simulation models to compare two resource allocation policies. One policy is to allocate the reserved capacity in different operating rooms, while the other is to reserve a dedicated operating room for emergency surgeries. It is found that the two policies have their advantages and limitations depending on patient composition and various other factors. Similarly, Bhattacharya et al. [18] examine the case where an operating room might be reserved only for the urgent and semi-urgent surgeries. By using the waiting time of surgeons as a performance measure, the study concludes that reserving a dedicated operating room might improve the performance of the overall system. Denton et al. [19] propose some sequencing rules based on heuristics and a stochastic optimization model to hedge against uncertainty related with the surgery durations. Hans et al. [20] develop a robust loading schedule to increase the utilization of the operating rooms and reduce overtime practices. By making use of the portfolio effect (i.e., minimizing the total variability by clustering surgeries with similar variability in terms of surgery durations in the same operating room/day), constructive and local search heuristics are employed to create the corresponding surgery schedule by reducing the required slack. Pham and Klinkert [21] adopt a job shop scheduling approach for sequencing elective and add-on surgeries in which the emergency surgeries are considered in the context of the add-on surgeries. They formulate a mixed integer linear programming (MILP) model and employ make-span as performance measure which is presented in the objective function.

Marcon and Dexter [22] investigate various sequencing rules for PACUs, establish the relationship in terms of economic impact between operating rooms, and study the effect of overutilization in those units. It is pointed out that the practice of scheduling the longest case <sup>fi</sup>rst in the operating rooms actually increases the load on the PACUs in terms of staf<sup>fi</sup>ng requirements and causes overutilization in operating rooms. Ballard and Kuhl [23] develop a discrete event simulation model that takes both PACUs and operating rooms into consideration. The performance measures include the number of each patient type seen, their times in system, and the utilizations for operating rooms, surgery teams, nurses, and any other constraining resource. Cardoen et al. [24] develop an MILP model to minimize the total amount of disturbance in terms of the deviation in total surgery time and the number of blocked beds at PACUs. A leveling approach is provided for the beds located in the operating rooms and PACUs which aims at distributing the surgery workload throughout the days and operating rooms such that disturbance is minimized. In addition, Cardoen et al. [25] develop an exact branch and price approach for the case sequencing problem in operating rooms and apply a dynamic programming algorithm to solve the pricing sub-problem with the consideration of PACU capacity. This approach is used to sequence the cases of the surgeries in a day-care facility with respect to several types of performance criteria such as peak use of recovery beds, the occurrence of recovery overtime, and the violation of various patient and surgeon preferences.

Dexter et al. [26] discuss the strategies for preventing the delay of ad mission to PACUs. They emphasize the adjustment of PACU staff work schedules to reduce the delays to those units especially in the presence of the unoccupied beds at those units. They also discuss the importance of sequencing of the surgical cases in operating rooms to reduce the delayed admissions and the reduction of the stay time at the PACUs.

However, there are even less studies that investigate in-situ rescheduling of elective patients upon the arrival of emergency patients in literature [27]. Kim et al. [28] discuss the potential bene<sup>fi</sup>ts and challenges of various bed allocation policies in intensive care unit by employing the simulation model based on historical data. In order to have more <sup>fl</sup>exible schemes, they consider the case of rescheduling, where elective surgeries might be canceled or postponed to make better use of available resources in intensive care units. Pham and Klinkert [21] develop a general perspective for the rescheduling problem by extending the classical mathematical modeling formulation for job-shop scheduling so that the make-span of surgeries is mini mized. Adan et al. [2] develop a slack planning scheme in operating rooms to account for emergency cases. If the current capacity of operating rooms is exceeded, the corresponding options of postponing an elective surgery or diverting an emergency admission to another healthcare center are also considered. Performance measures are developed by taking into account the patient service and hospital ef<sup>fi</sup>ciency. Augusto et al. [29] investigate the case of letting the patients recover in operating room beds in case of lack of resources in the downstream clinic units. They develop an MILP model and employ Lagrangean-relaxation heuristic approach to solve the model. Although surgery rescheduling is addressed, the emergency admissions are not considered in their study.

To the best of our knowledge, no study has addressed rescheduling of elective patients due to emergency admissions by considering the constraints of downstream capacity and the overall disruption to the original elective surgeries. As such, we aim to bridge this research gap in this study. The contributions of this research are threefold. First, the problem is formulated as a mixed integer linear programming model, and we develop a genetic algorithm, with innovative chromosome representations, as a solution approach. Second, the solutions to this complex problem can be obtained ef<sup>fi</sup>ciently by the genetic algorithm, in particular, within an affordable amount of time required by the practical need. Third, the incorporation of downstream clinical units also helps alleviate bed blocking problem which is regarded as a major impediment for ef<sup>fi</sup>cient and effective operating room practices. Bed-blocking occurs when the patients cannot be transferred from operating rooms to PACUs because of the lack of available beds at the PACUs. For instance, in order to transfer two patients whose surgeries are concluded at the same time, two empty PACU beds are needed. If there is only a single available bed at the PACUs, only one patient can be transferred, whereas the other patient needs to wait until someone is discharged from the PACUs. Clearly, bed blocking could lead to disruptions of surgery schedule and cause inef<sup>fi</sup>ciencies.

## 3. Problem de<sup>fi</sup>nition

Here, we consider two distinct categories of patient admissions for surgical procedures. The <sup>fi</sup>rst category is elective surgeries, which are already scheduled. The schedule of elective surgeries is treated as an input in our study. The second category is emergency patient admissions. If an emergency patient is admitted, in the presence of shared operating rooms and surgical teams, the elective surgeries might need to be rescheduled. Upon the request for admitting emergency patients, the decision makers in a hospital must provide timely decisions on (1) whether to admit or divert the emergency patients, and (2) how to adjust the schedule for elective surgeries if any emergency patients are admitted.

In this study, we focus on the admission decision of emergency cases such as trauma incidents according to the operations of a local

Table 1

hospital. For these emergency cases, medical intervention should be performed within an hour to decrease the mortality rates due to trauma effects [30,31]. This practice is so called the “Golden Hour” of trauma [32]. Usually, when an emergency call is received, the closest medical centers are noti<sup>fi</sup>ed regarding the trauma incident by emergency medical services (EMS). At the same time, an emergency medical team is dispatched, arrives at the scene, gains access to, assesses, stabilizes, and triages the patients. On the average, it takes around 35–45 min from dispatch to departure from the scene [31]. This amount of time is essentially the time window in which the corresponding decisions should be made at a particular medical facility.

If an emergency patient is admitted, he/she needs to be operated immediately and the changes are made in the elective surgery schedule accordingly. If the patient is not admitted, there will be no changes to the elective surgery schedule. These decisions are made under a variety of constraints so that the costs incurred due to the disruptions are minimized. The constraints include surgical team availability (e.g., surgeon, scrubbers, technician, and anesthetists), operating room availability, lunch hour and over-time hour constraints for operating rooms, overutilization constraints at PACUs, and PACU bed availability. Meanwhile, the cost items include the costs of postponing and preponing elective surgeries, the opportunity cost of diverting (or not admitting) the patients, the overtime and overutilization costs of operating rooms and PACUs, respectively. The overtime hours are de<sup>fi</sup>ned as the extended working hours beyond the regular working hours for operating rooms with accompanying resources such as surgical teams. Overutilization is de<sup>fi</sup>ned in terms of the additional beds and supporting equipment/staff members needed in the PACUs. It might be the case that elective surgeries scheduled beyond a particular threshold limit cannot be rescheduled in the time window ranging from the current time to the threshold preponement limit. For instance, it is generally not possible to reschedule an elective surgery, originally scheduled on Wednesday to 9:00 am on Monday if an emergency patient is admitted at 8:00 am on Monday. This restriction is especially valid when giving a short notice is not possible.

## 4. Mathematical programming model

In order to make the optimal decisions on emergency surgery admission and elective surgery rescheduling, we develop an MILP model to capture the patient <sup>fl</sup>ow between operating rooms and downstream clinic units. In this study, it is assumed that the elective surgeries have already been assigned to the time slots and the operating rooms. The objective of the MILP model is to minimize the costs associated with postponing and preponing the elective surgery patients, declining the emergency patients, and overtime/overutilization of operating rooms and PACUs.

## 4.1. Notations

The indices and decision variables used in the MILP model are de-<sup>fi</sup>ned in Table 1, and the parameters are summarized in Table 2.

## 4.2. MILP model formulation

$$
\begin{array}{l} \min \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {J} \sum_ {t = t _ {s}} ^ {T + 1} \sum_ {t ^ {\prime} = t _ {s}} ^ {T + 1} g _ {i t ^ {\prime}} C _ {j t t ^ {\prime}} m _ {i j} x _ {i t} + \sum_ {h = 1} ^ {H} \sum_ {j = 1} ^ {J} r _ {j} m _ {h j} ^ {\prime} \left(1 - x _ {h t _ {s}} ^ {\prime}\right) \\ + \sum_ {d = 1} ^ {D} C ^ {O R} O _ {d} ^ {O R} + C ^ {P A C U} O ^ {P A C U} \end{array}
$$

$$
\begin{array}{l} \text {s.t.} \sum_ {i = 1} ^ {I} \sum_ {t \in T _ {d} ^ {A} \cup T _ {d} ^ {B}} \sum_ {j = 1} ^ {J} m _ {i j} O _ {j} x _ {i t} + \sum_ {h = 1} ^ {H} \sum_ {t \in T _ {d} ^ {A} \cup T _ {d} ^ {B}} \sum_ {j = 1} ^ {J} m _ {h j} ^ {\prime} O _ {j} x _ {h t} ^ {\prime} \leq B _ {d} ^ {O R} \\ + O _ {D} ^ {O R}, \text {for} d = 1, \dots , D \end{array}\tag{1}
$$

ð<sup>2</sup>Þ

Notation for indices, sets, and decision variables

<table><tr><td colspan="2">Indices</td></tr><tr><td>d:</td><td>Day index; d∈{1, ..., D}</td></tr><tr><td>H:</td><td>Emergency patient index; h∈{1, ..., H}</td></tr><tr><td>i:</td><td>Elective patient index; i∈{1, ..., I}</td></tr><tr><td>j:</td><td>Surgery type; j∈{1, ..., J}</td></tr><tr><td>t:</td><td>Time period index; t∈{1, ..., T+1}, where T+1 indicates the time period outside the scheduling horizon</td></tr><tr><td>t&#x27;:</td><td>Auxiliary time period index; t&#x27;∈{1, ..., T+1}</td></tr><tr><td colspan="2">Sets</td></tr><tr><td> $T_{d}^{A}$ :</td><td>Set of regular working hours during day d</td></tr><tr><td> $T_{d}^{B}$ :</td><td>Set of overtime hours during day d</td></tr><tr><td> $T^{C}$ :</td><td>Set of the time period at which it is not possible to perform surgeries</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td> $O_{d}^{OR}$ :</td><td>Overtime amount of operating rooms during day d</td></tr><tr><td> $O^{PACU}$ :</td><td>Amount of additional beds/equipment placed at PACUs</td></tr><tr><td> $s_{it}$ :</td><td> $\left\{\begin{array}{ll}1, & \text{if elective patient } i \text{ occupies a bed at PACU at time period } t \\ 0, & \text{otherwise}\end{array}\right.$ </td></tr><tr><td> $s^{\prime}_{ht}$ :</td><td> $\left\{\begin{array}{ll}1, & \text{if emergency patient } h \text{ occupies a bed at PACU at time period } t \\ 0, & \text{otherwise}\end{array}\right.$ </td></tr><tr><td> $x_{it}$ :</td><td> $\left\{\begin{array}{ll}1, & \text{if the surgery starts at the beginning of time period } t \\ 0, & \text{otherwise}\end{array}\right.$ </td></tr><tr><td> $x^{\prime}_{ht}$ :</td><td> $\left\{\begin{array}{ll}1, & \text{if the surgery starts at the beginning of time period } t \\ 0, & \text{otherwise}\end{array}\right.$ </td></tr><tr><td> $y_{it}$ :</td><td> $\left\{\begin{array}{ll}1, & \text{if elective patient } i \text{ has a surgery at time period } t \\ 0, & \text{otherwise}\end{array}\right.$ </td></tr><tr><td> $y^{\prime}_{ht}$ :</td><td> $\left\{\begin{array}{ll}1, & \text{if emergency patient } h \text{ has a surgery at time period } t \\ 0, & \text{otherwise}\end{array}\right.$ </td></tr></table>

## Notation for the parameters.

<table><tr><td colspan="2">Parameters</td></tr><tr><td> $B^{PACU}$ :</td><td>Current capacity of PACUs during the scheduling horizon (in terms of beds/equipment)</td></tr><tr><td> $B_{d}^{OR}$ :</td><td>Current capacity of operating rooms during day  $d$  (in terms of hours)</td></tr><tr><td> $C^{PACU}$ :</td><td>Unit expansion cost of PACUs during the planning period ($/bed and equipment)</td></tr><tr><td> $C^{OR}$ :</td><td>Unit overtime cost of operating rooms ($/h)</td></tr><tr><td> $C_{jtt}$ :</td><td>Cost of moving an elective surgery of type  $j$  scheduled at time period  $t'$  to time period  $t$ </td></tr><tr><td> $D$ :</td><td>Number of days in the scheduling horizon</td></tr><tr><td> $git$ :</td><td> $\begin{cases} 1, & \text{if elective patient } i \text{ is scheduled to have a surgery at time} \\ & \text{period } t \\ 0, & \text{otherwise} \end{cases}$ </td></tr><tr><td> $H$ :</td><td>Number of emergency patients requesting surgeries</td></tr><tr><td> $I$ :</td><td>Number of elective patients having surgeries scheduled in the scheduling horizon</td></tr><tr><td> $J$ :</td><td>Number of the types of surgeries that could be performed in the facility</td></tr><tr><td> $m_{ij}$ :</td><td> $\begin{cases} 1, & \text{if elective patient } i \text{ requests a surgery of type } j \\ 0, & \text{otherwise} \end{cases}$ </td></tr><tr><td> $M'_{hj}$ :</td><td> $\begin{cases} 1, & \text{if emergency patient } h \text{ requests a surgery of type } j \\ 0, & \text{otherwise} \end{cases}$ </td></tr><tr><td> $N$ :</td><td>Number of operating rooms in the facility</td></tr><tr><td> $O_{j}$ :</td><td>Operating time for a surgery of type  $j$  (hours)</td></tr><tr><td> $r_{j}$ :</td><td>Cost of turning down an emergency patient requesting a surgery of type  $j$ </td></tr><tr><td> $S_{j}$ :</td><td>Length of stay at PACUs for a patient receiving a surgery of type  $j$  (hours)</td></tr><tr><td> $t_{s}$ :</td><td>Reference starting time (i.e., the time when the emergency patient arrives and the model is run)</td></tr><tr><td> $T$ :</td><td>Number of time periods in the scheduling horizon</td></tr><tr><td> $U^{PACU}$ :</td><td>Upper limit of the overutilization of PACUs (bed/equipment)</td></tr><tr><td> $U^{OR}$ :</td><td>Upper limit of the overtime utilization of operating rooms (hours)</td></tr><tr><td> $\lambda_{t}$ :</td><td>Number of beds occupied at PACUs at time period  $t$  from the previous scheduling cycle</td></tr><tr><td> $\mu_{jt}$ </td><td>Number of surgical teams available for performing surgeries of type  $j$  at time period  $t$ </td></tr><tr><td> $\Omega$ </td><td>Preponement time threshold</td></tr></table>

$$
\sum_ {i = 1} ^ {I} \sum_ {t \in T _ {d} ^ {B}} \sum_ {j = 1} ^ {J} y _ {i t} + \sum_ {h = 1} ^ {H} \sum_ {t \in T _ {d} ^ {B}} \sum_ {j = 1} ^ {J} y _ {h t} ^ {\prime} = O _ {d} ^ {O R}, \text {   for   } d = 1, \dots , D\tag{3}
$$

$$
\sum_ {t \in T ^ {c}} y _ {i t} = 0, \text {   for   } i = 1,..., I\tag{4}
$$

$$
\sum_ {t \in T ^ {C}} y _ {h t} ^ {\prime} = 0, \text {   for   } h = 1,..., H\tag{5}
$$

$$
\sum_ {t = t _ {s}} ^ {T + 1} x _ {i t} = 1, \text {   for   } i = 1,..., I\tag{6}
$$

$$
x _ {i t} \leq g _ {i t}, \text {   for   } i = 1, \dots , I; t = t _ {s}, \dots , t _ {s} + \Omega - 1\tag{7}
$$

$$
\sum_ {t = t _ {s} + 1} ^ {T + 1} x _ {h t} ^ {\prime} = 0, \text {   for   } h = 1,..., H\tag{8}
$$

$$
\sum_ {i = 1} ^ {I} x _ {i t} + \sum_ {h = 1} ^ {H} x _ {h t} ^ {\prime} \leq N, \text {   for   } t = t _ {s},..., T\tag{9}
$$

$$
\sum_ {i = 1} ^ {I} y _ {i t} + \sum_ {h = 1} ^ {H} y _ {h t} ^ {\prime} \leq N, \text {   for   } t = t _ {s},..., T\tag{10}
$$

$$
\sum_ {i = 1} ^ {I} m _ {i j} y _ {i t} + \sum_ {h = 1} ^ {H} m _ {h j} ^ {\prime} y _ {h t} ^ {\prime} \leq \mu_ {j t}, \text {   for   } j = 1,..., J; t = t _ {s},..., T\tag{11}
$$

$$
\begin{array}{l} y _ {i t ^ {\prime}} \geq m _ {i j} x _ {i t}, \text {   for   } i = 1, \dots , I; j = 1, \dots , J; t = t _ {s}, \dots , T, t ^ {\prime} \\ = t, \dots , t + O _ {j} - 1 \end{array}\tag{12}
$$

$$
\begin{array}{l} y _ {h t ^ {\prime}} ^ {\prime} \geq m _ {h j} ^ {\prime} x _ {h t} ^ {\prime}, \text {   for   } h = 1,..., H; j = 1,..., J; t = t _ {s},..., T, t ^ {\prime} \\ = t,..., t + O _ {j} - 1 \end{array}\tag{13}
$$

$$
\begin{array}{l} s _ {i t ^ {\prime}} \geq m _ {i j} x _ {i t}, \text {   for   } i = 1,..., I; j = 1,..., J; t = t _ {s},..., T, t ^ {\prime} \\ = t + O _ {j},..., t + O _ {j} + S _ {j} - 1 \end{array}\tag{14}
$$

$$
\begin{array}{l} s _ {h t ^ {\prime}} ^ {\prime} \geq m _ {h j} ^ {\prime} x _ {h t} ^ {\prime}, \text { for } h = 1,..., H; j = 1,..., J; t = t _ {s},..., T, t ^ {\prime} \\ = t + O _ {j},..., t + O _ {j} + S _ {j} - 1 \end{array}\tag{15}
$$

$$
\sum_ {i = 1} ^ {I} s _ {i t} + \sum_ {h = 1} ^ {H} s _ {h t} ^ {\prime} + \lambda_ {t} \leq B ^ {\text { PACU }} + O ^ {\text { PACU }}, \text {   for   } t = t _ {s},..., T\tag{16}
$$

$$
O _ {d} ^ {O R} \leq U ^ {O R}, \text {   for   } d = 1, \dots , D\tag{17}
$$

$$
O ^ {P A C U} \leq U ^ {P A C U}\tag{18}
$$

$$
s _ {i t}, x _ {i t}, y _ {i t} = 0 \text { or } 1, \text { for } i = 1,..., I; t = t _ {s},..., T,\tag{19}
$$

$$
s _ {h t} ^ {\prime}, x _ {h t} ^ {\prime}, y _ {h t} ^ {\prime} = 0 \text {or} 1, \text {for} h = 1, \dots , H; t = t _ {s}, \dots , T,\tag{20}
$$

$$
O _ {d} ^ {O R} \geq 0 \text {   and   integer,   for   } d = 1,..., D\tag{21}
$$

$$
O ^ {P A C U} \geq 0 \text { and   integer. }\tag{22}
$$

The objective function (1) consists of four terms. The <sup>fi</sup>rst term determines the cost of preponing or postponing the elective surgeries. The second term captures the opportunity cost of turning down the emergency patients in terms of the lost revenue. The third term is the overtime cost of operating rooms, while the fourth term represents the marginal cost of placing additional beds and equipment, and hiring additional staff for providing enough PACU capacity.

Constraints (2) ensure that the total time to perform elective and emergency surgeries on each day does not exceed the total time of regular working hours and overtime of the operating rooms. Constraints (3) determine the total overtime of the operating rooms on each day. Constraints (4) and (5) enforce that no elective or emergency surgeries are performed outside the regular working hours and possible overtime hours. Constraints (6) assign a starting time to each surgery except the surgeries postponed beyond the scheduling horizon, which is represented by time period T+1. Constraints (7) prevent that the elective surgeries scheduled beyond Ω hours from the current time $t _ { s }$ are rescheduled in time window $[ t _ { s } , t _ { s } + \varOmega - 1 ]$ . These constraints ensure the time needed by a patient to respond the change of the starting time of his/her surgery schedule, which includes the time to inform the patient of the change and the time for the patient to travel to the hospital. Constraints (8) guarantee that emergency surgeries are performed immediately. Constraints (9) and (10) ensure that the total number of new-starting and ongoing surgeries at any time period does not exceed the maximum number of the operating rooms, while constraints (11) guarantee that the total number of ongoing surgeries of each type at any time period does not exceed the number of surgical teams that are capable of performing the surgeries of this type. Constraints (12) and (13) determine the time of performing each elective or emergency surgery, respectively. Constraints (14) and (15) indicate that the bed/equipment at the PACUs will be occupied by each elective or emergency patient, respectively, for a speci<sup>fi</sup>ed time period in order to recover from surgery. Constraints (16) enforce the PACU capacities. Constraints (17) enforce the limit of the operating room overtime on each day, which constraint (18) stipulates the limit of the number of additional beds/equipment that could be added to the PACUs due to various considerations such as rules, regulations, space restrictions, etc.

## 5. Solution approaches

## 5.1. Solving the MILP model using GAMS

The MILP model developed in the previous section involves the use of the binary variables as well as integer variables. The problem size increases exponentially with the increases in the number of patients and the type of surgeries. In addition, the increase in the number of operating rooms also increases the problem size. The model has been implemented in a mainstream commercial optimization software package, GAMS with CPLEX solver. Unfortunately, it is found that the solver cannot provide ef<sup>fi</sup>cient solutions for many scenarios using an Intel Quad Core PC—optimal solutions cannot be obtained even in 1 week of running time. Clearly, the excessive computation time negatively affects the applicability of this approach and damages its potential merits. As mentioned earlier, the decisions should be made within 35–45 min— the shorter, the better. Thus, extending computation time beyond that amount of time to improve the solution quality is not an option. Rather than searching for the exact optimal solutions, a genetic algorithm is developed to obtain near optimal solutions in an affordable amount of time.

## 5.2. Genetic algorithm

Fig. 1 shows the steps of the genetic algorithm to solve the MILP model. The notation in the genetic algorithm is summarized in Table 3. In the algorithm, the <sup>fi</sup>rst generation of chromosomes consists of the current elective surgery schedule and φ−1 chromosomes representing the random schedule of emergency patient and elective patients. Then, each new generation is obtained by applying the crossover and mutation operators on the chromosomes in the current generation, repairing new off-springs, and selecting the new generation from combined pool. The algorithm stops when the maximum generation limit is attained or the objective function value of the best feasible solution reaches 0.

## 5.2.1. Representation of the solution

The chromosome representation for a solution consists of four parts. The <sup>fi</sup>rst part represents the sequence of the elective patients/ surgeries. For example, the <sup>fi</sup>rst part of a chromosome is “4 5 9 13 4

![](/api/attachments/Q4WRKQFK/fulltext/images/c8641fdfa4fdb6c0fd44d8229cb15b022dcb6c76a454c3da173c85fb31825597.jpg)  
Fig. 1. Flowchart for the proposed genetic algorithm.

45… 37 2 43 34”, which indicates that elective patient 4 is the <sup>fi</sup>rst patient to be operated, whereas elective patient 34 is the last person who will undergo surgery in an operating room. The second part represents the number of open slots before a patient's surgery by repeating the patient identi<sup>fi</sup>cation for the same amount of time. For example, the second part of a chromosome is “5 5 3 4 4 6 7 18 20 32 34 38 42”, which indicates that there are two empty time slots just before the start of surgery for patient 5. There is an open time slot before the surgery of patient 3. There are two open time slots before the surgery start for patient 4. There is one open time slot before the start of the surgery for patients 6, 7, 18, 20, 32, 34, 38, and 42. For the patient IDs not listed in the second part of a chromosome, there is no open time slot before their surgeries. The third part of a chromosome governs the number of the surgeries performed in each operating room during a

## Table 3

Notation for genetic algorithm parameters.

<table><tr><td>Parameter</td><td>Notation</td></tr><tr><td>Number of parent pairs selected for crossover, or offspring pairs created</td><td> $\pi$ </td></tr><tr><td>Mutation probability for first part of chromosome structure</td><td> $\tau_1$ </td></tr><tr><td>Mutation probability for the second part of chromosome structure</td><td> $\tau_2$ </td></tr><tr><td>Mutation probability for the third part of chromosome structure</td><td> $\tau_3$ </td></tr><tr><td>Mutation probability for the fourth part of chromosome structure</td><td> $\tau_4$ </td></tr><tr><td>Number of chromosomes/solutions selected for the next generation by elitist selection</td><td> $v$ </td></tr><tr><td>Number of chromosomes/solutions selected for the next generation by roulette wheel selection</td><td> $\varphi -v-1$ </td></tr><tr><td>Population size</td><td> $\varphi$ </td></tr><tr><td>Limit on maximum generation number</td><td> $X$ </td></tr><tr><td>Repair probability</td><td> $\psi$ </td></tr></table>

given day. For example, for the planning cycle of 3 days used in our case study, the <sup>fi</sup>rst four numbers in the third part indicate the number of patients operated in the <sup>fi</sup>rst operating room on the <sup>fi</sup>rst, second and third days and outside the planning cycle, respectively, and the second set of 4 numbers represents the numbers of the patients operated in the second operating room, etc. An example of the third part is “4 2 2 0 3 1 3 0 3 2 2 1 2 2 2 0”, which demonstrates that in the <sup>fi</sup>rst operating room, 4 patients are operated on the <sup>fi</sup>rst day, 2 patients are operated on the second day, 2 patients are operated on the third day, and no patients are operated outside the planning cycle. Each bit in the fourth part indicates whether an emergency patient is admitted or not, and the operating room assigned for surgery if the emergency patient is admitted. The length of the fourth part of a chromosome depends on the number of emergency patients arriving at that particular time period. For instance, the fourth part of a chromosome consists of three bits “5 3 0”, which indicate that the <sup>fi</sup>rst emergency patient is operated in Operating Room 5, whereas the second patient is operated in Operating Room 3, and the third emergency patient is turned down and not operated in the hospital.

## 5.2.2. Evaluating the fitness of chromosomes

This particular problem is a constrained minimization problem. The representation scheme of the solutions discussed in Section 5.2.1 could not guarantee that a chromosome always represents a feasible solution. The constraints that are not enforced by the representation scheme include the availability of the surgical teams, the constraints satisfying that the operating room is not utilized during lunch hours, the availability of the corresponding beds in the downstream of the clinic <sup>fl</sup>ow (i.e., the PACUs), the constraint satisfying that the operating rooms do not operate after the overtime hours. For example, it might be the case that two surgeries of the same type can start simultaneously according to the chromosome representation, although only one surgery team is available to perform that particular surgery. The chromosome structure allows such a schedule although it is not feasible according to constraints (11). In order to overcome this problem, the weights associated with the violation of the corresponding constraints are added to the objective function. In other words, the constraint violation is penalized by including the penalty terms in the objective function.

## 5.2.3. Selecting the best-fit individuals for crossover operator for reproduction

After the <sup>fi</sup>tness value of each chromosome is calculated, the next step is choosing the members of the population for crossover operation. For this purpose, we make use of the combination of roulette wheel selection with the elitist selection. A chromosome representing the original surgery schedule (i.e., rejecting the emergency patients, and performing the elective surgeries according to the original schedule) is always selected for the crossover operation. This scheme would allow the variations of the solutions derived from the original schedule to be represented as offsprings.

## 5.2.4. Crossover operator

For each generation, a certain number of chromosomes/solution pairs are selected for crossover operation. From those pairs, the <sup>fi</sup>rst part of the chromosome for the offsprings is created using the partial mapped crossover (PMX) operator [33]. This is because the traditional crossover operator might yield offsprings that have duplicate patients or some patients might not be represented in the chromosome solutions for the <sup>fi</sup>rst part of chromosome representation. Literature indicates that PMX operator provides consistent results in terms of the solution quality as compared to other approaches such as order and cycle crossover operators [34].

For the second and third parts of chromosomes, the two-point traditional crossover operator is selected because it generally provides better results as compared with the single point crossover operator [35]. In the two-point crossover operator, two crossover points are selected and the corresponding bits between these two points are copied to the offspring from the <sup>fi</sup>rst parent. The bits outside those crossover sites are copied from the second parent. The second offspring is formed in the same manner by replacing the roles of the <sup>fi</sup>rst and second parents.

For the fourth part of chromosomes, the crossover operator is selected based on the length of that particular chromosome part. If only one emergency arrival is considered for admission, one of the parents is selected randomly and the corresponding value is copied to the offspring. If two emergency patients at a time are considered for admission, the single point crossover operator is implemented. Otherwise, the two point crossover operator is used. Note that, for this part, the traditional crossover operator might lead to infeasible solutions where two emergency patients occupy the same operating room at the same time. In order to overcome this problem, the traditional crossover operator is <sup>fi</sup>rst applied. After crossover, if more than one emergency patient is assigned to the same operating room, then those excessive patients are assigned randomly to other operating rooms such that only one patient can undergo surgical treatment in each operating room.

## 5.2.5. Mutation operator

For the <sup>fi</sup>rst two parts of the chromosomes, the mutation operator is applied on a bit-by-bit basis. For each bit, a random number uniformly distributed between 0 and 1 is generated. For the <sup>fi</sup>rst part, if the generated random number is smaller than $\tau _ { 1 } ,$ the second bit is picked randomly, and these two bits are exchanged. In practice, it corresponds to switching the locations of two patients in the sequence of the patients represented in the solution. For the second part, which indicates empty time slots in the schedule, if the generated random number is smaller than $\tau _ { 2 } ,$ another random number will be generated. If the second random number generated is smaller than or equal to 0.5, the bit is deleted from the chromosome, indicating that the length of vacant time for the operating room before the surgery represented by this bit is reduced by one time unit. If the second random number generated is greater than 0.5, an additional copy of this bit is added to the chromosome. In other words, the length of vacant time for that operating room before the patient's surgery is increased by one time unit.

For the third part of the chromosomes, which represents the number of surgeries performed in each operating room during a given day, mutation occurs in the form of generating a random number distributed uniformly between 1 and $( T + 1 ) \times N ,$ , and replacing the bit randomly selected with this new number. For the fourth part of the chromosomes, which represents whether the emergency patients are admitted or not, mutation occurs in the form of generating a random number distributed uniformly between 1 and N+1 for each bit in that part, and replacing the corresponding number in the bit with this new number.

## 5.2.6. Repair operator

After the crossover and mutation operators are applied to produce offsprings, the repair operator is performed on the newly generated chromosomes with certain probability. A uniformly distributed random number between 0 and 1 is generated for each chromosome, and if the random number is smaller than ψ, the repair operator is applied. The repair operator in general works for reducing the overall infeasibility by two different schemes. The <sup>fi</sup>rst scheme is that if the surgery for a particular patient is scheduled to in an infeasible time period (e.g., the lunch time), the surgery is delayed until the return of working hours to reduce the infeasibility associated with the solution. Another scheme for the repair operator is to prepone the surgery that is scheduled later to reduce the vacant time between those surgeries. Although the repair mechanisms do not guarantee the feasibility because of various other constraints, they serve as an attempt to decrease the overall infeasibility.

## 5.2.7. Replacing least-fit chromosomes with new offsprings

The elitist selection and the roulette wheel selection are combined to select the offsprings and parents in the next generation. After the <sup>fi</sup>tness values of the offpsrings are calculated, the parents and offsprings are ranked in descending order of the <sup>fi</sup>tness function value. The <sup>fi</sup>rst υ chromosomes in the list are selected for the next generation. Additionally the remaining $\varphi - v - 1$ number of solutions are selected based on the roulette wheel selection.

The last chromosome included in the new generation is the original elective surgery schedule. This approach helps generate variations that likely produce lower objective function values $( \mathrm { i . e . } ,$ , better <sup>fi</sup>tness function values). This is because the solutions developed from the original elective schedule more likely yield solutions that honor the original schedule of elective surgeries, therefore reducing overall objective function value and increasing the corresponding <sup>fi</sup>tness function value.

## 5.3. Genetic algorithm parameters

The genetic algorithm parameters are decided based on literature recommendations and pilot runs. Grefenstette [36] shows that the bit-by-bit mutation rate around 0.01 provides better results, especially in terms of the off-line performance which measures the average <sup>fi</sup>tness function value of the best solution found throughout the generations and emphasizes improving the best solution found in every generation [37]. De-Jong [38] demonstrates that long term performance is improved by selecting a population size between 50 and 100. Grefenstette [36] also indicates that the crossover rate of 0.45 provides better results in terms of the off-line performance as well. The population sizes varying between 30 and 80 are reported to provide better results. It has also been indicated that the performance of PMX improves with the increasing population size and is robust with respect to the mutation rate [34]. In this study, we refer to the literature for the initial ranges of the parameter values and employ pilot runs for <sup>fi</sup>ne tuning of those parameters. As a result, the values presented in Table 4 are selected for implementing the proposed genetic algorithm.

Regarding penalizing scheme in evaluating the <sup>fi</sup>tness function, we adopt the approach developed by Joines and Houck [39] where the penalty coef<sup>fi</sup>cients can be calculated as follows,

$$
g _ {w} (\chi) = (\rho_ {w} \chi) ^ {\alpha}\tag{23}
$$

where $g _ { w } ( \chi )$ is the corresponding penalty coef<sup>fi</sup>cient for constraint w at generation $\chi ,$ and $\rho _ { u }$ and α are the constant values. This enables a wider search at the initial generations with lower penalty coef<sup>fi</sup>cients, and toward the end of the execution of genetic algorithm with increased penalty coef<sup>fi</sup>cients. It is found that the values of 1.25 for $\rho _ { w }$ and 0.5 for α give the best result in this study, and they are also within the suggested ranges of Ref. [39].

Meanwhile, Taheri et al. [40] estimate that the admission of one emergency patient will generate an additional revenue of \$16,603 in the downstream clinic unit. Olejarz [41] reports an average cost of \$4000/day for an additional bed/equipment of PACU, Park and Dickerson [42] report the <sup>fi</sup>gure in the range of \$15–\$25/min for operating room related costs for overtime hours. Vogel et al. [43] estimate an incremental delaying cost of \$3798/day for bypass graft surgical operation. Table 5 summarizes the cost parameters and penalty functions for the MILP model and genetic algorithm.

The <sup>fi</sup>tness function of each chromosome is calculated as,

$$
f _ {q} = \frac {1 6 , 6 0 3}{o b j _ {q}}, o b j _ {q} \neq 0,\tag{24}
$$

where $f _ { q }$ is the <sup>fi</sup>tness function of solution $q ,$ and obj is the objective function value of the solution. Since the problem is a minimization type problem, a lower objective function value indicates a better solution which is re<sup>fl</sup>ected by a higher <sup>fi</sup>tness function value. As such, the objective function value is inverted in Eq. (24). In this equation, the value of 16,603 is used as a numerator for calculating the <sup>fi</sup>tness function in which the original elective surgery schedule will yield a <sup>fi</sup>tness function value of 1 if no additional costs are involved in terms of exceeding the current capacity of the operating room and the PACUs. This value is the cost of turning down an emergency patient according to the literature [40]. In a sense, Eq. (24) provides a normalizing scheme where all the objective function values are scaled down with a reference value of 1 that corresponds to the original elective surgery schedule with no overtime in operating rooms and no overutilization of PACUs, under the assumption that the emergency patient is not admitted.

## 6. Scenarios and results

## 6.1. Scenario generation

In order to assess the performances of the solution approaches, we develop scenarios for solving instances of rescheduling elective patients upon the admission request for emergency patients. The solutions provided by the genetic algorithm are compared with the best feasible solution found by the CPLEX solver in GAMS (version 23.2.1), and this gives us the opportunity to assess the quality of the genetic algorithm solutions. A key criterion to evaluate the effectiveness of a solution approach is whether it is capable of providing near optimal or optimal solutions in a limited time window. As mentioned earlier, the work is developed based on the settings of a local hospital, which has 86 staffed beds and performs about 7000 surgeries every year. It usually deals with emergency cases that require immediate attention such as trauma, and it has a 24-hour emergency department with Level II trauma designation. As such, the decisions need to be made within a limited time window of around 35–45 min.

Table 4  
Genetic algorithm parameters.

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td> $\pi$ </td><td>15</td></tr><tr><td> $\tau_1$ </td><td>1%</td></tr><tr><td> $\tau_2$ </td><td>1%</td></tr><tr><td> $\tau_3$ </td><td>1%</td></tr><tr><td> $\tau_4$ </td><td>1%</td></tr><tr><td> $v$ </td><td>10</td></tr><tr><td> $\varphi -v-1$ </td><td>49</td></tr><tr><td> $\varphi$ </td><td>60</td></tr><tr><td> $X$ </td><td>10,000</td></tr><tr><td> $\psi$ </td><td>50%</td></tr></table>

Table 5  
Cost parameters and penalty functions for the MILP model and genetic algorithm

<table><tr><td></td><td>Penalty function</td><td>Cost coefficients</td></tr><tr><td>After hours operation</td><td>Eq. (23) with $\rho_{w} = 1.25,$  $\alpha = 0.5$ </td><td></td></tr><tr><td>Exceeding the regular + overtime capacity of the post anesthesia care units</td><td>Eq. (23) with $\rho_{w} = 1.25,$  $\alpha = 0.5$ </td><td></td></tr><tr><td>Exceeding the regular capacity but not overtime capacity of the post anesthesia care units</td><td></td><td>$4000/bed-day [41]</td></tr><tr><td>Operating during lunch hour in the operating rooms (lunch time)</td><td>Eq. (23) with $\rho_{w} = 1.25,$  $\alpha = 0.5$ </td><td></td></tr><tr><td>Exceeding the upper limits of the availability of the surgical team</td><td>Eq. (23) with $\rho_{w} = 1.25,$  $\alpha = 0.5$ </td><td></td></tr><tr><td>Overtime hours for the operating rooms</td><td></td><td>$1500/h [42]</td></tr><tr><td>Turning down the patient for the emergency admission</td><td></td><td>$16,603 [40]</td></tr><tr><td>Operating the patient other than designated day (e.g., Wednesday instead of Monday)</td><td></td><td>$3798/day [43]</td></tr><tr><td>Operating the patient outside the scheduling horizon</td><td></td><td>$11,394 [43]</td></tr><tr><td>Operating elective patient scheduled beyond the preponement threshold inside the specified time window</td><td>Eq. (23) with $\rho_{w} = 1.25,$  $\alpha = 0.5$ </td><td></td></tr></table>

As shown in Table 6, we design four problem scenarios by varying (a) number of operating rooms and (b) current elective patient load based on the available capacity. There are two levels regarding the number of operating rooms, namely, 4 rooms (a setting for most small hospitals) and 8 rooms (a setting for the medium to medium-large sized hospitals). Also, there are two levels of overtime practice with regards to the elective patient load, namely, moderate (patient load of 80%) and high patient load featuring the use of overtime utilization (patient load of 110%). Note that Scenarios 3 and 4 overall re<sup>fl</sup>ect the typical operations of the local hospital.

The original elective patient schedules of Scenarios 1–4 are obtained based on the block scheduling practices of the local hospital. In this scheme, certain time blocks (i.e., consecutive time slots in the same operating room) are scheduled for certain type of surgeries to increase the ef<sup>fi</sup>ciency of operating rooms by reducing the total turnover time for speci<sup>fi</sup>c type of surgery.

Based on the data collected, we identify ten main surgery types performed in the local hospital as shown in Table 7. It is assumed that upon the arrival of emergency patients, the rescheduling of elective patients up to 3 days is considered. This is again in concert with the current practices implemented in the local hospital. For instance, if an emergency patient is admitted on Monday, the elective surgeries up to Wednesday of the same week could be rescheduled. Shuf<sup>fl</sup>ing the elective surgery schedule more than 3 days ahead is not preferable by the hospital because it increases patient inconvenience.

Table 7 also shows the average durations and frequencies for the ten categories of surgeries. The total duration of surgeries include the setup time required for preparing operating rooms for subsequent surgeries, the preparation time of patients for the surgery (e.g., the time required for administering anesthesia to patients), the time required for moving patients out of operating rooms, as well as the duration of the actual surgery. In addition, the average time of emergency surgeries is approximately 120 min according to the hospital record. Meanwhile, the general problem parameters used for all the scenarios are listed in Table 8. Note that the average stay in PACUs is also obtained from the historical data of the hospital, and the time in PACUs generally does not vary with respect to the type of surgeries.

Table 8  
Table 7 Percentage of surgery types.  
Table 6  
Input parameters for the four scenarios.

<table><tr><td>Problem parameters</td><td>Scenario 1</td><td>Scenario 2</td><td>Scenario 3</td><td>Scenario 4</td></tr><tr><td>Number of operating rooms</td><td>4</td><td>4</td><td>8</td><td>8</td></tr><tr><td>Elective patient load</td><td>80%</td><td>110%</td><td>80%</td><td>110%</td></tr><tr><td>Number of PACU beds</td><td>4</td><td>4</td><td>8</td><td>8</td></tr><tr><td>Overtime practices</td><td>2 h (15:00–17:00) for 3 operating rooms</td><td>2 h (15:00–17:00) for 3 operating rooms</td><td>2 h (15:00–17:00) for 5 operating rooms</td><td>2 h (15:00–17:00) for 5 operating rooms</td></tr></table>

## 6.2. Comparison of solution approaches

The CPLEX solver in GAMS (ver. 23.2.1) is adopted to solve the four scenarios. For the scenarios in which the optimal solutions cannot be reached, the best near optimal solutions obtained within a predetermined amount of computation time (i.e., 6 h in this study) are reported. In the meantime, we also implement the genetic algorithm to obtain solutions for the four scenarios. A comparison of the solution quality in terms of the objective function value provided by the commercial solver and the genetic algorithm along with the corresponding computation times is provided in Table 9.

The results indicate that, in general, the solution qualities of the two approaches are comparable. For Scenario 2, the genetic algorithm not only is signi<sup>fi</sup>cantly more ef<sup>fi</sup>cient than the commercial solver, but also generates a slightly better objection function value. For Scenarios 1 and 4, both approaches obtain the same objective function values. The computation times of the genetic algorithm are less than 50 min, while the times of using the commercial solver are 6 h, for both scenarios. For Scenario 3 in which both approaches end up with an objective function value of 0, the genetic algorithm <sup>fi</sup>nds the solution in less than 35 min while it only takes a fraction of second for the commercial solver. An objective function value of 0 indicates the ultimate lower bound, where the optimality of solution is guaranteed provided that it is feasible. The corresponding physical meaning is that, when an emergency patient is admitted, no overtime hours for operating rooms is utilized, no additional beds/corresponding resources are assigned to the PACUs, and all elective patients are scheduled to be operated in the same day as initially scheduled. In addition, Table 9 indicates that the computation time for genetic algorithm increases with the number of operating rooms and the patient load. However, this trend is not observed when the commercial solver is used.

To further illustrate the evolution of objective function values of best feasible solutions reported by GAMS, Fig. 2(a)–(c) is plotted for Scenarios 1, 2, and 4 respectively. The main purpose is to investigate if the solutions obtained within about 45 min (or the decision time window) by the commercial solver are already close to the <sup>fi</sup>nal results obtained after 6 h as shown in Table 9. If this is the case, the genetic algorithm approach will be less attractive. For this purpose, it can be in fact observed that for Scenarios 1, 2, and 4, the solutions obtained after running for 1 h in GAMS are 10–50% worse than the <sup>fi</sup>nal solutions found by the genetic algorithm. This shows the heuristic approach is indeed a viable option to ef<sup>fi</sup>ciently obtain the solution of rescheduling.

<table><tr><td>Surgery type</td><td>Average duration for the surgery, minutes</td><td>Percentage, %</td></tr><tr><td>Cardio-Vascular (CV)</td><td>240</td><td>5</td></tr><tr><td>Ear-Nose-Throat (ENT)</td><td>60</td><td>15</td></tr><tr><td>General Surgery</td><td>120</td><td>25</td></tr><tr><td>Hand</td><td>60</td><td>5</td></tr><tr><td>Neurology</td><td>240</td><td>5</td></tr><tr><td>Obstetrics and gynecology (OB/GYN)</td><td>120</td><td>10</td></tr><tr><td>Ophthalmology</td><td>60</td><td>5</td></tr><tr><td>Orthopedics</td><td>120</td><td>15</td></tr><tr><td>Podiatry</td><td>120</td><td>5</td></tr><tr><td>Urology</td><td>60</td><td>10</td></tr></table>

## 6.3. Expanded results for the genetic algorithm approach

We also examine the evolution of solution quality with respect to the number of generations using the genetic algorithm. For the purpose of brevity, the objective function values of the incumbent solutions as well as the average objective function values are provided in Fig. 3 only for Scenario 4.

As it can be seen in Fig. 3, the incumbent <sup>fi</sup>tness function value jumps during the execution of the algorithm, which indicates that better feasible solutions are found. Meanwhile, the increase of the average <sup>fi</sup>tness function value follows that of <sup>fi</sup>tness function value of the incumbent solution with some lag. Initially, the lags are longer suggesting the diversity in the population. However, toward the end of the run, the lag length decreases and the average <sup>fi</sup>tness function value <sup>fl</sup>uctuates in a relatively small range. An interesting observation is that during a certain initial period, the average <sup>fi</sup>tness function value is higher than the incumbent <sup>fi</sup>tness function value, which can be explained by the fact that the best feasible solution is declared as incumbent whereas the average <sup>fi</sup>tness function is calculated over the entire population which can include some infeasible solutions as well. Also, after the subsequent increase in the incumbent <sup>fi</sup>tness function value around generation number 350, the average <sup>fi</sup>tness function value never exceeds the incumbent <sup>fi</sup>tness function value. This is in part related with the penalizing scheme. When the number of generations increases, the corresponding penalty coef<sup>fi</sup>cients increase exponentially. After a certain point, the infeasible solutions are penalized severely and the infeasibility is discouraged. It is somewhat analogous to the simulated annealing approach where initially the moves that lead to infeasible solutions are encouraged with a Metropolis function, whereas later due to the decreasing simulated temperatures, those moves are discouraged due to the decreasing transition probabilities.

The following example elaborates the change of surgery schedule after the admission of the emergency patient under Scenario 4. Based on the solution provided for Scenario 4, the schedule does not change for Operating Rooms 2 and 4. However, the admission results in the changes in the current elective surgery schedule for Operating Rooms 1, 3, 5, 6, 7, and 8. The original and modi<sup>fi</sup>ed elective surgery schedules upon admission of an emergency patient for Operating Room 7 are pro vided in Tables 10 and 11, respectively. For the purpose of brevity, the original and updated schedules for other operating rooms are summarized in Appendix A.

General problem parameters.

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Average stay in PACU</td><td>60 min</td></tr><tr><td>Emergency arrivals</td><td>1 for the Scenarios 1–4. In all cases, a trauma patient is brought to the hospital at the first day of the scheduling period.</td></tr><tr><td>Preponement time threshold</td><td>2 h</td></tr></table>

Solution quality and computation times obtained by two approaches.

<table><tr><td>Scenario</td><td>Objective function value of the best solution found by GAMS in 6 h</td><td>Objective function of best solution found by genetic algorithm</td><td>Computation time of GAMS</td><td>Computation time of genetic algorithm</td></tr><tr><td>1</td><td>3000</td><td>3000</td><td>360 min</td><td>15.18 min</td></tr><tr><td>2</td><td>23,298</td><td>22,596</td><td>360 min</td><td>18.22 min</td></tr><tr><td>3</td><td>0</td><td>0</td><td>0.12 s</td><td>33.64 min</td></tr><tr><td>4</td><td>40,692</td><td>40,692</td><td>360 min</td><td>47.86 min</td></tr></table>

(a)  
![](/api/attachments/Q4WRKQFK/fulltext/images/87fc6aac5d5cde39aedbf4e1549b8df6615e1168d30f410da8ede7050844c6a7.jpg)

(b)  
![](/api/attachments/Q4WRKQFK/fulltext/images/ac71cc3d81978317080a1f4944d90cf83fc131c8f0d7121cda630b15b7710ab4.jpg)

![](/api/attachments/Q4WRKQFK/fulltext/images/820b82c4cd40c562c7b7771f8ed837f8ff34d2b50960103ebabab49658ced253.jpg)  
Fig. 2. Progression of objective function value of the best feasible solution for (a) Scenario 1, (b) Scenario 2, and (c) Scenario 4.

![](/api/attachments/Q4WRKQFK/fulltext/images/057b25039b2544d1a1c1c81e13c2b065f1fa59bd9092bf111b3d08d1f8e8ef32.jpg)  
Fig. 3. Progression of <sup>fi</sup>tness function values with respect to the number of generations.

The new schedule incorporates the corresponding changes for the 8 elective patients. Note that the inclusion of a patient is indicated in bold, italic and underlined letters in the tables, whereas the deletion is indicated by the strikethrough letters. ENT Pat. 32, who is originally scheduled for surgery at 15:00–16:00 in Operating Room 3 on Monday, is now rescheduled to 14:00–15:00 in Operating Room 7 on the same day. On the contrary, it can be seen that, most of the elective patients other than Neurology Pat. 84 and Orthopedics Pat. 90 are shifted from overtime (15:00–17:00) to regular time hours (07:00–11:00 and 12:00–15:00). This helps decrease the overtime related costs thereby decreasing the objective function value. In addition, the Neurology Pat. 84 is removed from the current scheduling horizon and considered for rescheduling for the next horizon. On the other hand, Orthopedics Pat. 90 is preponed from Tuesday 12:00–14:00 to Monday 9:00–11:00 within the same operating room. This move increases the objective function value by \$3798.

## 6.4. Further discussion

The solution approach of using a commercial solver to solve the MILP model and that of adopting the genetic algorithm generate fairly consistent results in terms of the solution quality. In the situations where the patient load is low, usually no additional cost function is introduced. In these cases, using the commercial solver to solve the MILP model might provide the optimal solution in the fraction of seconds.

Original elective surgery schedule for Operating Room 7 in Scenario 4.

<table><tr><td>Operating Room 7</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Neurology Pat. 84</td><td>ENT Pat. 86</td><td>General Surgery Pat. 92</td></tr><tr><td>8:00–9:00</td><td>Neurology Pat. 84</td><td>ENT Pat. 87</td><td>General Surgery Pat. 92</td></tr><tr><td>9:00–10:00</td><td>Neurology Pat. 84</td><td>ENT Pat. 88</td><td>General Surgery Pat. 93</td></tr><tr><td>10:00–11:00</td><td>Neurology Pat. 84</td><td>ENT Pat. 89</td><td>General Surgery Pat. 93</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>General Surgery Pat. 85</td><td>Orthopedics Pat. 90</td><td>Ophthalmology Pat. 94</td></tr><tr><td>13:00–14:00</td><td>General Surgery Pat. 85</td><td>Orthopedics Pat. 90</td><td>Ophthalmology Pat. 95</td></tr><tr><td>14:00–15:00</td><td></td><td>Ophthalmology Pat. 91</td><td>Ophthalmology Pat. 96</td></tr><tr><td>15:00–16:00 (Overtime)</td><td></td><td></td><td></td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td></td><td></td></tr></table>

Table 11  
Updated surgery schedule for Operating Room 7 in Scenario 4 after emergency admission.

<table><tr><td>Operating Room 7</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8.00</td><td>Neurology Pat. 84Pat.1 (Emergency)</td><td>ENT Pat. 86</td><td>GeneralSurgery Pat. 92</td></tr><tr><td>8:00–9:00</td><td>Neurology Pat. 84Pat.1 (Emergency)</td><td>ENT Pat. 87</td><td>GeneralSurgery Pat. 92</td></tr><tr><td>9:00–10:00</td><td>Neurology Pat. 84Orthopedics Pat. 90</td><td>ENT Pat. 88</td><td>GeneralSurgery Pat. 93</td></tr><tr><td>10:00–11:00</td><td>Neurology Pat. 84Orthopedics Pat. 90</td><td>ENT Pat. 89</td><td>GeneralSurgery Pat. 93</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>General Surgery Pat. 85</td><td>Orthopedics Pat. 90Urology Pat. 65</td><td>Ophthalmology Pat. 94</td></tr><tr><td>13:00–14:00</td><td>General Surgery Pat. 85</td><td>Orthopedics Pat. 90Urology Pat. 66</td><td>Ophthalmology Pat. 95</td></tr><tr><td>14:00–15:00</td><td>ENT Pat. 32</td><td>Ophthalmology Pat. 91</td><td>Ophthalmology Pat. 96</td></tr><tr><td>15:00–16:00(Overtime)</td><td></td><td></td><td></td></tr><tr><td>16:00–17:00(Overtime)</td><td></td><td></td><td></td></tr></table>

When the patient load is high, it is very likely that additional cost <sup>fi</sup>gures are introduced by employing overtime in operating rooms or expanding the capacity of PACUs, and the commercial solver approach becomes inef-<sup>fi</sup>cient and provides signi<sup>fi</sup>cantly inferior solutions within the decision time window of 35–45 min compared with the genetic algorithm. On the other hand, although the genetic algorithm can always provide comparable solutions within the time window for all scenarios, it is still important to use both solution approaches in practice, and they should complement each other. This is because the commercial solver can save a signi<sup>fi</sup>cant amount of computation time for some scenarios, and any time saving will be appreciated by the hospital staff and patients. Also, in practice, both approaches can be set up to run successively during the given day, and the process might be automated such that the results of the previous run are fed as the input for the subsequent run.

Another aspect is that the suggested model can also be used as a decision making tool for assessing and improving the original elective surgery schedule with regard to resource usage. Based on the rescheduling results of Scenario 4, it can be found that the model and the solution approaches are able to increase the system ef<sup>fi</sup>ciency by shifting elective surgery patients from overtime hours to regular hours. Even without the admission of the emergency patients, it can be adopted as a standalone approach for evaluating and improving the current elective surgery schedule with some modi<sup>fi</sup>cations to the MILP model and the genetic algorithm code. In that case, the purpose of shifting the elective surgeries is to better utilize the available resources. With proper modi<sup>fi</sup>cations, the model can be also extended to assess the current elective surgery schedule with regard to block scheduling practices that might be applied in other healthcare settings.

All the four scenarios presented deal with the admission of one emergency patient arriving at the beginning of a work day. In fact, the proposed model and solution approaches can also handle multiple emergency patients arriving at the same time. This might be especially important for the cases where more than one patient requiring emergency surgeries might be brought to one hospital due to various reasons, such as traf<sup>fi</sup>c accidents and terrorist attacks involving the injury of multiple people. Based on the available capacity, it can make decisions on whether to admit those patients. Depending upon the case settings, some emergency patients might be turned down while others might be admitted.

## 7. Conclusive remarks

This research addresses the issue of emergency patient admission and rescheduling of elective patients by considering the availability of various resources, including the capacity of downstream clinic units.

The problem is formulated as an MILP model. Due to the size of the problem and the accompanying problem structure, the computation time for solving the instances of the complex scenarios might be excessively long by using a mainstream commercial optimization package. To overcome this challenge, a heuristic approach based on genetic algorithm is proposed. The genetic algorithm features a new chromosome structure to represent solutions, which is comprised of four different sub-structures. Four different scenarios featuring 4 and 8 operating rooms and 80% and 110% patient loads are solved by the two solution approaches, respectively. A comparison between the two approaches is made in terms of computation times and the objective function values of the best solutions obtained.

For the problem instances where the best feasible solution is optimal, the solution approach based on the commercial solver is more ef<sup>fi</sup>cient. However, for the problem instances involving high patient loads, the genetic algorithm approach is usually able to generate superior solution qualities within the decision time window. Therefore, it is suggested that the two approaches should be used jointly in practice so that more ef<sup>fi</sup>cient operations can be achieved in managing the operating rooms under the demand of emergency patient admission.

## Appendix A

Table A.1: Original elective surgery schedule for Operating Room 1 in Scenario 4.

<table><tr><td>Operating Room 1</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>General Surgery Pat. 2</td><td>General Surgery Pat. 7</td><td>CV Pat. 12</td></tr><tr><td>8:00–9:00</td><td>General Surgery Pat. 2</td><td>General Surgery Pat. 7</td><td>CV Pat. 12</td></tr><tr><td>9:00–10:00</td><td>General Surgery Pat. 3</td><td>General Surgery Pat. 8</td><td>CV Pat. 12</td></tr><tr><td>10:00–11:00</td><td>General Surgery Pat. 3</td><td>General Surgery Pat. 8</td><td>CV Pat. 12</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Podiatry Pat. 4</td><td>General Surgery Pat. 9</td><td>General Surgery Pat. 13</td></tr><tr><td>13:00–14:00</td><td>Podiatry Pat. 4</td><td>General Surgery Pat. 9</td><td>General Surgery Pat. 13</td></tr><tr><td>14:00–15:00</td><td>Podiatry Pat. 5</td><td>General Surgery Pat. 10</td><td>General Surgery Pat. 14</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>Podiatry Pat. 5</td><td>General Surgery Pat. 10</td><td>General Surgery Pat. 14</td></tr><tr><td>16:00–17:00 (Overtime)</td><td>Urology Pat. 6</td><td>ENT Pat. 11</td><td>Ophthalmology Pat. 15</td></tr></table>

Table A.2: Original elective surgery schedule for Operating Room 2 in Scenario 4.

<table><tr><td>Operating Room 2</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>General SurgeryPat. 16</td><td>General SurgeryPat. 20</td><td>General SurgeryPat. 24</td></tr><tr><td>8:00–9:00</td><td>General SurgeryPat. 16</td><td>General SurgeryPat. 20</td><td>General SurgeryPat. 24</td></tr><tr><td>9:00–10:00</td><td>General SurgeryPat. 17</td><td>General SurgeryPat. 21</td><td>General SurgeryPat. 25</td></tr><tr><td>10:00–11:00</td><td>General SurgeryPat. 17</td><td>General SurgeryPat. 21</td><td>General SurgeryPat. 25</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>General SurgeryPat. 18</td><td>General SurgeryPat. 22</td><td>General SurgeryPat. 26</td></tr><tr><td>13:00–14:00</td><td>General SurgeryPat. 18</td><td>General SurgeryPat. 22</td><td>General SurgeryPat. 26</td></tr><tr><td>14:00–15:00</td><td>General SurgeryPat. 19</td><td>General SurgeryPat. 23</td><td>General SurgeryPat. 27</td></tr><tr><td>15:00–16:00(Overtime)</td><td>General SurgeryPat. 19</td><td>General SurgeryPat. 23</td><td>General SurgeryPat. 27</td></tr><tr><td>16:00–17:00(Overtime)</td><td></td><td></td><td></td></tr></table>

Table A.3: Original elective surgery schedule for Operating Room 3 in Scenario 4.

<table><tr><td>Operating Room 3</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Orthopedics Pat. 28</td><td>Hand Pat. 34</td><td>OB Pat. 41</td></tr><tr><td>8:00–9:00</td><td>Orthopedics Pat. 28</td><td>Hand Pat. 34</td><td>OB Pat. 41</td></tr><tr><td>9:00–10:00</td><td>Orthopedics Pat. 29</td><td>Hand Pat. 35</td><td>OB Pat. 42</td></tr><tr><td>10:00–11:00</td><td>Orthopedics Pat. 29</td><td>Hand Pat. 35</td><td>OB Pat. 42</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Orthopedics Pat. 30</td><td>ENT Pat. 36</td><td>Podiatry Pat. 43</td></tr><tr><td>13:00–14:00</td><td>Orthopedics Pat. 30</td><td>ENT Pat. 37</td><td>Podiatry Pat. 43</td></tr><tr><td>14:00–15:00</td><td>ENT Pat. 31</td><td>ENT Pat. 38</td><td>ENT Pat. 44</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>ENT Pat. 32</td><td>ENT Pat. 39</td><td>ENT Pat. 45</td></tr><tr><td>16:00–17:00 (Overtime)</td><td>ENT Pat. 33</td><td>ENT Pat. 40</td><td>ENT Pat. 46</td></tr></table>

Table A.4: Original elective surgery schedule for Operating Room 4 in Scenario 4.

<table><tr><td>Operating Room 4</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>CV Pat. 47</td><td>CV Pat. 50</td><td>Neurology Pat. 53</td></tr><tr><td>8:00–9:00</td><td>CV Pat. 47</td><td>CV Pat. 50</td><td>Neurology Pat. 53</td></tr><tr><td>9:00–10:00</td><td>CV Pat. 47</td><td>CV Pat. 50</td><td>Neurology Pat. 53</td></tr><tr><td>10:00–11:00</td><td>CV Pat. 47</td><td>CV Pat. 50</td><td>Neurology Pat. 53</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Hand Pat. 48</td><td>OB Pat. 51</td><td>Orthopedics Pat. 54</td></tr><tr><td>13:00–14:00</td><td>Hand Pat. 48</td><td>OB Pat. 51</td><td>Orthopedics Pat. 54</td></tr><tr><td>14:00–15:00</td><td>Hand Pat. 49</td><td>OB Pat. 52</td><td>Orthopedics Pat. 55</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>Hand Pat. 49</td><td>OB Pat. 52</td><td>Orthopedics Pat. 55</td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td></td><td></td></tr></table>

Table A.5: Original elective surgery schedule for Operating Room 5 in Scenario 4.

<table><tr><td>Operating Room 5</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Orthopedics Pat. 56</td><td>OB Pat. 60</td><td>Podiatry Pat. 67</td></tr><tr><td>8:00–9:00</td><td>Orthopedics Pat. 56</td><td>OB Pat. 60</td><td>Podiatry Pat. 67</td></tr><tr><td>9:00–10:00</td><td>OB Pat. 57</td><td>OB Pat. 61</td><td>Podiatry Pat. 68</td></tr><tr><td>10:00–11:00</td><td>OB Pat. 57</td><td>OB Pat. 61</td><td>Podiatry Pat. 68</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>OB Pat. 58</td><td>Urology Pat. 62</td><td>OB Pat. 69</td></tr><tr><td>13:00–14:00</td><td>OB Pat. 58</td><td>Urology Pat. 63</td><td>OB Pat. 69</td></tr><tr><td>14:00–15:00</td><td>OB Pat. 59</td><td>Urology Pat. 64</td><td>OB Pat. 70</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>OB Pat. 59</td><td>Urology Pat. 65</td><td>OB Pat. 70</td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td>Urology Pat. 66</td><td></td></tr></table>

Table A.6: Original elective surgery schedule for Operating Room 6 in Scenario 4.

<table><tr><td>Operating Room 6</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Urology Pat. 71</td><td>Orthopedics Pat. 76</td><td>Urology Pat. 79</td></tr><tr><td>8:00–9:00</td><td>Urology Pat. 72</td><td>Orthopedics Pat. 76</td><td>Urology Pat. 80</td></tr><tr><td>9:00–10:00</td><td>Urology Pat. 73</td><td>Orthopedics Pat. 77</td><td>Urology Pat. 81</td></tr><tr><td>10:00–11:00</td><td>Urology Pat. 74</td><td>Orthopedics Pat. 77</td><td>Urology Pat. 82</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Orthopedics Pat. 75</td><td>Orthopedics Pat. 78</td><td>Hand Pat. 83</td></tr><tr><td>13:00–14:00</td><td>Orthopedics Pat. 75</td><td>Orthopedics Pat. 78</td><td>Hand Pat. 83</td></tr><tr><td>14:00–15:00</td><td></td><td></td><td></td></tr><tr><td>15:00–16:00 (Overtime)</td><td></td><td></td><td></td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td></td><td></td></tr></table>

Table A.7: Original elective surgery schedule for Operating Room 8 in Scenario 4.

<table><tr><td>Operating Room 8</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>ENT Pat. 97</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 107</td></tr><tr><td>8:00–9:00</td><td>ENT Pat. 98</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 107</td></tr><tr><td>9:00–10:00</td><td>ENT Pat. 99</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 108</td></tr><tr><td>10:00–11:00</td><td>ENT Pat. 100</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 108</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>ENT Pat. 101</td><td>Ophthalmology Pat. 104</td><td>ENT Pat. 109</td></tr><tr><td>13:00–14:00</td><td>ENT Pat. 102</td><td>Ophthalmology Pat. 105</td><td>ENT Pat. 110</td></tr><tr><td>14:00–15:00</td><td></td><td>Ophthalmology Pat. 106</td><td>Urology Pat. 111</td></tr><tr><td>15:00–16:00 (Overtime)</td><td></td><td></td><td></td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td></td><td></td></tr></table>

Table A.8: Updated surgery schedule for Operating Room 1 in Scenario 4 after emergency admission.

<table><tr><td>Operating Room 1</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>General Surgery Pat. 2</td><td>General Surgery Pat. 7</td><td>CV Pat. 12</td></tr><tr><td>8:00–9:00</td><td>General Surgery Pat. 2</td><td>General Surgery Pat. 7</td><td>CV Pat. 12</td></tr><tr><td>9:00–10:00</td><td>General Surgery Pat. 3</td><td>General Surgery Pat. 8</td><td>CV Pat. 12</td></tr><tr><td>10:00–11:00</td><td>General Surgery Pat. 3</td><td>General Surgery Pat. 8</td><td>CV Pat. 12</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Podiatry Pat. 4</td><td>General Surgery Pat. 9</td><td>General Surgery Pat. 13</td></tr><tr><td>13:00–14:00</td><td>Podiatry Pat. 4</td><td>General Surgery Pat. 9</td><td>General Surgery Pat. 13</td></tr><tr><td>14:00–15:00</td><td>Podiatry Pat. 5</td><td>General Surgery Pat. 10</td><td>General Surgery Pat. 14</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>Podiatry Pat. 5</td><td>General Surgery Pat. 10</td><td>General Surgery Pat. 14</td></tr><tr><td>16:00–17:00 (Overtime)</td><td>Urology Pat. 6</td><td>ENT Pat. 11</td><td>Ophthalmology Pat. 15</td></tr></table>

Table A.9: Updated surgery schedule for Operating Room 3 in Scenario 4 after emergency admission.

<table><tr><td>Operating Room 3</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Orthopedics Pat. 28</td><td>Hand Pat. 34</td><td>OB Pat. 41</td></tr><tr><td>8:00–9:00</td><td>Orthopedics Pat. 28</td><td>Hand Pat. 34</td><td>OB Pat. 41</td></tr><tr><td>9:00–10:00</td><td>Orthopedics Pat. 29</td><td>Hand Pat. 35</td><td>OB Pat. 42</td></tr><tr><td>10:00–11:00</td><td>Orthopedics Pat. 29</td><td>Hand Pat. 35</td><td>OB Pat. 42</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Orthopedics Pat. 30</td><td>ENT Pat. 36</td><td>Podiatry Pat. 43</td></tr><tr><td>13:00–14:00</td><td>Orthopedics Pat. 30</td><td>ENT Pat. 37</td><td>Podiatry Pat. 43</td></tr><tr><td>14:00–15:00</td><td>ENT Pat. 31</td><td>ENT Pat. 38</td><td>ENT Pat. 44</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>ENT Pat. 32</td><td>ENT Pat. 39</td><td>ENT Pat. 45</td></tr><tr><td>16:00–17:00 (Overtime)</td><td>ENT Pat. 33</td><td>ENT Pat. 40</td><td>ENT Pat. 46</td></tr></table>

Table A.10: Updated surgery schedule for Operating Room 5 in Scenario 4 after emergency admission.

<table><tr><td>Operating Room 5</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Orthopedics Pat. 56</td><td>OB Pat. 60</td><td>Podiatry Pat. 67</td></tr><tr><td>8:00–9:00</td><td>Orthopedics Pat. 56</td><td>OB Pat. 60</td><td>Podiatry Pat. 67</td></tr><tr><td>9:00–10:00</td><td>OB Pat. 57</td><td>OB Pat. 61</td><td>Podiatry Pat. 68</td></tr><tr><td>10:00–11:00</td><td>OB Pat. 57</td><td>OB Pat. 61</td><td>Podiatry Pat. 68</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>OB Pat. 58</td><td>Urology Pat. 62</td><td>OB Pat. 69</td></tr><tr><td>13:00–14:00</td><td>OB Pat. 58</td><td>Urology Pat. 63</td><td>OB Pat. 69</td></tr><tr><td>14:00–15:00</td><td>OB Pat. 59</td><td>Urology Pat. 64</td><td>OB Pat. 70</td></tr><tr><td>15:00–16:00 (Overtime)</td><td>OB Pat. 59</td><td>Urology Pat. 65</td><td>OB Pat. 70</td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td>Urology Pat. 66</td><td></td></tr></table>

Table A.11: Updated surgery schedule for Operating Room 6 in Scenario 4 after emergency admission.

<table><tr><td>Operating Room 6</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>Urology Pat. 71</td><td>Orthopedics Pat. 76</td><td>Urology Pat. 79</td></tr><tr><td>8:00–9:00</td><td>Urology Pat. 72</td><td>Orthopedics Pat. 76</td><td>Urology Pat. 80</td></tr><tr><td>9:00–10:00</td><td>Urology Pat. 73</td><td>Orthopedics Pat. 77</td><td>Urology Pat. 81</td></tr><tr><td>10:00–11:00</td><td>Urology Pat. 74</td><td>Orthopedics Pat. 77</td><td>Urology Pat. 82</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>Orthopedics Pat. 75</td><td>Orthopedics Pat. 78</td><td>Hand Pat. 83</td></tr><tr><td>13:00–14:00</td><td>Orthopedics Pat. 75</td><td>Orthopedics Pat. 78</td><td>Hand Pat. 83</td></tr><tr><td>14:00–15:00</td><td>Urology Pat. 6</td><td>ENT Pat. 40</td><td>ENT Pat. 46</td></tr><tr><td>15:00–16:00 (Overtime)</td><td></td><td></td><td></td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td></td><td></td></tr></table>

Table A.12: Updated surgery schedule for Operating Room 8 in Scenario 4 after emergency admission.

<table><tr><td>Operating Room 8</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td></tr><tr><td>7:00–8:00</td><td>ENT Pat. 97</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 107</td></tr><tr><td>8:00–9:00</td><td>ENT Pat. 98</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 107</td></tr><tr><td>9:00–10:00</td><td>ENT Pat. 99</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 108</td></tr><tr><td>10:00–11:00</td><td>ENT Pat. 100</td><td>Neurology Pat. 103</td><td>Orthopedics Pat. 108</td></tr><tr><td>11:00–12:00</td><td></td><td></td><td></td></tr><tr><td>12:00–13:00</td><td>ENT Pat. 101</td><td>Ophthalmology Pat. 104</td><td>ENT Pat. 109</td></tr><tr><td>13:00–14:00</td><td>ENT Pat. 102</td><td>Ophthalmology Pat. 105</td><td>ENT Pat. 110</td></tr><tr><td>14:00–15:00</td><td>ENT Pat. 33</td><td>Ophthalmology Pat. 106</td><td>Urology Pat. 111</td></tr><tr><td>15:00–16:00 (Overtime)</td><td></td><td></td><td></td></tr><tr><td>16:00–17:00 (Overtime)</td><td></td><td></td><td></td></tr></table>

## References

[1] D.A. Etzioni, J.H. Liu, M.A. Maggard, C.Y. Ko, The aging population and its impact on the surgery workforce, Annals of Surgery 238 (2) (2003) 170–177.

[2] I. Adan, J. Bekkers, N. Dellaert, J. Jeunet, J. Vissers, Improving operational effectiveness of tactical master plans for emergency and elective patients under stochastic demand and capacitated resources, European Journal of Operational Research 213 (1) (2011) 290–308.

[3] D. Delen, A. Oztekin, L. Tomak, An analytic approach to better understanding and management of coronary surgeries, Decision Support Systems 52 (3) (2012) 698–705.

[4] S. Walzcak, W.W. Pofahl, R.J. Scorpio, A decision support tool for allocating hospital bed resources and determining required acuity of care, Decision Support Systems 34 (4) (2003) 445–456.

[5] S. Walzcak, J.E. Scharf, Reducing surgical patient costs through use of an arti<sup>fi</sup>cial neural network to predict transfusion requirements, Decision Support Systems 30 (2) (2000) 125–138.

[6] X. Qu, R.L. Rardin, J.A.S. Williams, A mean-variance model to optimize the <sup>fi</sup>xed versus open appointment percentage in open access scheduling systems, Deci sion Support Systems 53 (3) (2012) 554–564.

[7] F. Dexter, R.H. Epstein, Operating room ef<sup>fi</sup>ciency and scheduling, Current Opinion in Anesthesiology 18 (2005) 195–198.

[8] M. van Houdenhoven, J.M. van Oostrum, G. Wullink, E. Hans, J.L. Hurink, J. Bakker, G. Kazemier Fewer intensive care unit refusals and a higher capacity utilizatior by using a cyclic surgical case schedule, Journal of Critical Care 23 (2) (2008) 222–226.

[9] A. Macario, T.S. Vitez, B. Dunn, T. McDonald, Where are the costs in perioperative care?: analysis of hospital costs and charges for inpatient surgical care, Anesthesiology 83 (6) (1995) 1138–1144

[10] S. Glauberman, H. Mintzberg, Managing the care of health and the cure of disease— part I: differentiation, Health Care Management Review 26 (2001) 56–69.

[11] A. Jebali, A.B.H. Alouane, P. Ladet, Operating rooms scheduling, International Journal of Production Economics 99 (2006) 52–62.

[12] E. Marcon, S. Kharraja, G. Simonnet, The operating theatre planning by the follow-up of the risk of no realization, International Journal of Production Economics 85 (2003) 83–90.

[13] A. Testi, E. Tanfani, G. Torre, A three-phase approach for operating theatre schedules, Health Care Management Science 10 (2007) 163–172.

[14] B. Cardoen, E. Demeulemeester, J. Belien, Operating room planning and scheduling: a literature review, European Journal of Operational Research 201 (3) (2010) 921-932

[15] M. Lamiri, X. Xie, A. Dolgui, F. Grimaud, A stochastic model for operating room planning with elective and emergency demand for surgery, European Journal of Operational Research 185 (2008) 1026–1037.

[16] M. Lamiri, X. Xie, S. Zhang, Column generation for operating theatre planning with elective and emergency patients, IIE Transactions 40 (2008) 838–852.

[17] G. Wullink, M. van Houdenhoven, E.W. Hans, J.M. van Oostrum, M. van der Lans, G. Kazemier, Closing emergency operating rooms improves ef<sup>fi</sup>ciency, Journal of Medical Systems 31 (2007) 543–546.

[18] T. Bhattacharyya, M.S. Vrahas, S.M. Morrison, E. Kim, R.A. Wiklund, R.M. Smith, H.E. Rubash, The value of the dedicated orthopedic trauma operating room, The Journal of TRAUMA Injury Infection and Critical Care 60 (6) (2006) 1336–1341.

[19] B. Denton, J. Viapiano, A. Vogl, Optimization of surgery sequencing and scheduling decisions under uncertainty, Health Care Management Science 10 (2007) 13–24.

[20] E. Hans, G. Wullink, M. van Houdenhoven, G. Kazemier, Robust surgery loading European Journal of Operational Research 185 (2008) 1038–1050

[21] D.-N. Pham, A. Klinkert, Surgical case scheduling as a generalized job shop scheduling problem, European Journal of Operational Research 185 (2008) 1011–1025.

[22] J.E. Marcon, F. Dexter, Impact of surgical sequencing on post anesthesia care unit staf<sup>fi</sup>ng, Health Care Management Science 9 (2006) 87–98.

[23] M. Ballard, M.E. Kuhl, The use of simulation to determine maximum capacity in the surgical suite operating room, in: L.F. Perrone, F.P. Wieland, J. Liu, B.G. Lawson, D.M. Nicol, R.M. Fujimoto (Eds.), Proceedings of the 2006 Winter Simulation Conference, 2006, pp. 433–438.

[24] B. Cardoen, E. Demeulemeester, J. Beliën, Optimizing a multiple objective surgical case sequencing problem, International Journal of Production Economics 119 (2) (2009) 354–366.

[25] B. Cardoen, E. Demeulemeester, J. Beliën, Sequencing surgical cases in a day-care environment: an exact branch-and-price approach, Computers and Operations Research 36 (9) (2009) 2660–2669.

[26] F. Dexter, R.H. Epstein, E. Marcon, R. de Matta, Strategies to reduce delays in admission into a postanesthesia care unit from operating rooms, Journal of Perianesthesia Nursing 20 (2) (2005) 92–102.

[27] F. Guerreiro, R. Guido, Operational research in the management of the operating theatre: a survey, Health Care Management Science 14 (1) (2011) 89–114.

[28] S.-C. Kim, I. Horowitz, K.K. Young, T.A. Buckley, Flexible bed allocation and performance in the intensive care unit, Journal of Operations Management 18 (4) (2000) 427–443.

[29] V. Augusto, X. Xie, V. Perdomo, Operating theatre scheduling with patient recovery in both operating rooms and recovery beds, Computers and Industrial Engineering 58 (2) (2010) 231–238.

[30] A.A. Baez, P.L. Lane, B. Sorondo, E.M. Giraldez, Predictive effect of out-of-hospital time in outcomes of severely injured young adult and elderly patients, Prehospital and Disaster Medicine 21 (6) (2006) 427–430.

[31] E.T. Wilde, Do emergency medical system response times matter for health outcomes? Working Paper, Columbia University 2011, source: http://www,be wyu edu/divecon/econ/douglas/seminar/Wilde%28WP%29EMS.pdf, accessed 23 August 2011.

[32] J.C. Sacra, R. Martinez, Trauma Systems, in: W.R. Roush (Ed.), Principles of EMR Systems, second edn., American College of Emergency Physicians, Texas, 2009, p. 41.

[33] B.P. Buckles, P.E. Petry, R.I. Kuester, Schema survival rates and heuristic search in genetic algorithms, in: Tools for Artificial Intelligence Proceedings of the 2nd International IEEE Conference, 1990, pp. 86–91.

[34] B.F. Al-Dulaimi, H.A. Ali, Enhanced traveling salesman problem solving by genetic algorithm technique (TSPGA), World Academy of Science Engineering and Technology 38 (2008) 296–302

[35] S.N. Sivanandam, S.N. Deepa, Introduction to Genetic Algorithms, <sup>fi</sup>rst edn. Springer-Verlag, Heidelberg, 2008.

[36] J.J. Grefenstette, Optimization of control parameters for genetic algorithms, IEEE Transactions on Systems, Man, and Cybernetics 16 (1) (1986) 122–128.

[37] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, <sup>fi</sup>rst edn Addison-Wesley Publishing Company Inc., Boston, MA, 1989.

[38] K.A. De Jong, Analysis of the behavior of a class of genetic adaptive systems. Dissertation, University of Michigan, Ann Arbor, MI, 1975.

[39] J. Joines, C.R. Houck, On the use of non-stationary penalty functions to solve nonlinear constrained optimization problems with GA's, in: Proceedings of IEEE, International Conference on Evolutionary Computation, 1994, pp. 579–584.

[40] P.A. Taheri, P.M. Maggio, J. Dougherty, C. Neil, S. Fetyko, D.R. Harkins, D.A. Butz, Trauma center downstream revenue: the impact of incremental patients within a health system, The Journal of Trauma 62 (3) (2007) 615–619.

[41] D. Olejarz, ICU capacity boosted to largest in Michigan, Henry Ford News Henry Ford Health System, 2009. online resource, located at: http://www.henryfordhealth.org body.cfm?id=46335&action=detail&ref=986. Accessed 21 July 2011.

[42] K.W. Park, C. Dickerson, Can ef<sup>fi</sup>cient supply management in the operating room save millions? Current Opinion in Anesthesiology 22 (2009) 242–248.

[43] T.R. Vogel, V.Y. Dombrovskiy, S.F. Lowry, In-hospital delay of elective surgery for high volume procedures: the impact on infectious complications, Journal of the American College of Surgeons 211 (6) (2010) 784–790

Ergin Erdem is a Ph.D. candidate in the Department of Industrial & Manufacturing Engineering at North Dakota State University. He obtained his B.S. and M.Sc. degrees from the Middle East Technical University, Ankara, Turkey, He has been actively involved in various healthcare process improvement projects at regional and national levels. His research interests include decision making and optimization for healthcare operations, healthcare information systems, and metaheuristic methods for optimization.

Xiuli Qu is an Assistant Professor in the Department of Industrial and Systems Engi neering at North Carolina A&T State University. She received her Ph.D. in Industrial Engineering from Purdue University, West Lafayette, IN, USA. Her research interests include healthcare engineering, data mining, reverse supply chain management, modeling and op timization of homeland security issues. She has had papers published in International Jour nal of Production Economics, European Journal of Operations Research, Health Care Management Sciences, Computers and Industrial Engineering, and among others

Jing Shi is an Associate Professor in the Department of Industrial Engineering & Manufacturing Engineering at North Dakota State University. He received his Ph.D. in Industrial Engineering from Purdue University, West Lafayette, IN, USA. His research interests include modeling and optimization for healthcare systems, health informatics, renewable energy modeling, and wireless sensor network/RFID applications. He has authored and co-authored more than 100 papers, which are published in refereed journals and conference proceedings.
