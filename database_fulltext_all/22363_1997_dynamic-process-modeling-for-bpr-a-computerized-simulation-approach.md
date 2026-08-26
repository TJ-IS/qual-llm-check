---
otero_id: 22363
otero_key: "N7PXHY7K"
title: "Dynamic process modeling for BPR: A computerized simulation approach"
authors: "Hee-Woong Kim; Young-Gul Kim"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00015-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research

# Dynamic process modeling for BPR: A computerized simulation approach $^{1}$

Hee-Woong Kim, Young-Gul Kim\*

Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-43 Cheongryang, Dongaemoon, Seoul 130-012, South Korea

## Abstract

Business Process Redesign (BPR) projects are considered to be high risk due to their high management complexity, enterprise-wide impact, and steep project cost. This paper describes a technique that should reduce that risk by developing a systematic process redesign method that we call Dynamic Process Modeling (DPM). It integrates customer-oriented process modeling with computerized visual process simulation to promote better understanding of the required process and determine its performance through simulation of the proposed redesign alternatives prior to selection and implementation. We compare DPM with four other implementation-level process modeling methods using eight criteria to demonstrate its effectiveness in a real-world hospital BPR case. © 1997 Elsevier Science B.V.

Keywords: Dynamic process modeling; Customer-oriented process model; Performance evaluation; Visual simulation; Business process redesign

## 1. Introduction

Business organizations in the 1990s are facing an ever-increasing uncertainty and unprecedented volatility of the external environment. Increased competition has led many organizations to the “fundamental rethinking and radical redesign of their age-old business processes” called Business Process Redesign (BPR) [4], or Business Reengineering (BR) [10]. Such efforts tend to be complex, have larger enterprise-wide impact, and steeper project cost than the traditional IS development projects today. Despite isolated success stories at several firms [12], many organizations have encountered serious problems during their BPR implementations with widely mixed results [8, 9]. So BPR should always be considered a high-risk project from the firm's perspective.

In this paper, we try to show how to reduce the risk of BPR projects by two means: process modeling and computerized simulation. The first is a technique for understanding, representing, and, when necessary, redesigning the fundamental business processes. Lack of a disciplined method to model business processes has been a problem in many BPR efforts $[2]$ . An ideal process modeling method for BPR would provide a simple but expressive modeling mechanism that reflects the customer orientation and cross-functional nature of BPR [3]. One such method, the Event-Process Chain (EPC) modeling method [14], was extended here. By sacrificing the conceptual-level clarity and readability of the EPC model, the Extended EPC (EEPC) model can represent the more detailed implementation-level process dynamics by supporting additional modeling elements.

Despite the massive resource investment and its enterprise-wide impact, many firms have been quick to ‘drastically redesign’ their major business processes without a thorough analysis of the impact of the change. All too often, instead of ‘dramatic performance improvement’ they end up with impractical and irrevocable process change that is hard to justify. Computerized process simulation may help to resolve such a problem. By simulating the expected performance of the proposed alternatives, it will be possible to choose the best $[15, 20, 22]$ .

Finally, by integrating EEPC modeling and computerized process simulation techniques with performance-based guidelines, an innovative BPR methodology called Dynamic Process Modeling (DPM) is introduced and a real-world hospital case used as an illustration.

## 2. The dynamic process modeling method

DPM has three components, as shown in Figure 1. We use the EEPC model for process representation, simulation, and work analysis [18, 19, 21].

![](/api/attachments/N7PXHY7K/fulltext/images/144ae2ed065ca425498440015ee4495a0c657bdff9c1163ceea0a15ee9a5213c.jpg)  
Fig. 1. DPM method components.

![](/api/attachments/N7PXHY7K/fulltext/images/c4d51b6118f6432bad51eb1cf21525505b0cc7c730d90aa8bb9f8eef207b3218.jpg)  
Fig. 2. Examples of EPC constructs.

## 2.1. Event-process chain(EPC) model

EPC modeling originates from the idea of the event-transaction diagram, which is a graphical formalism used to model the dynamic portion of an organization's global information schema [13]. By adopting a strong customer perspective, EPC modeling supports BPR in identifying and redesigning critical business processes at the conceptual level. By hiding all customer-independent internal processing activities, it facilitates the identification of process bottlenecks that result in lengthy process cycle time and a subsequent loss of customer satisfaction.

An EPC diagram has four constructs: event, process, branching, and wait. Figure 2 gives examples of these constructs, which are drawn in two dimensions, with place dimension vertically and time dimension horizontally. These are the dimensions that should comprise the core context for BPR, where processes are frequently spread over functional boundaries and cycle time measurement is often a crucial part of the process redesign.

## 2.2. Extended EPC(EEPC) model

An EEPC has five elements, as shown in Table 1 – Event, Process, Branching, Flow, and Wait. EVENT is a change important to the customer; that is, any person or organization, internal or external. If change is implicit and not perceived by the customer, it does not need to be modeled. But if the change is perceived by the customer and affects the customer's next activity, then it must be modeled explicitly. An event is represented by a circle with its name and TBC (time between creation), where TBC is the event creation interval that is mainly used for simulation purposes. For example, consider a process where the customer visits a restaurant; if 10 customers arrive at the restaurant during one hour, then TBC is 0.1 h per customer.

Table 1
EEPC Elements

<table><tr><td>Component</td><td>Notation</td><td>Component</td><td>Notation</td></tr><tr><td>EVENT</td><td>TRC<img src="/api/attachments/N7PXHY7K/fulltext/images/6b897b7fe06c340752d88f124a0abb9d6a3b649a02c3e5029b0aaecbef75983f.jpg"/></td><td>FLOW</td><td>[Customer object], moving time→</td></tr><tr><td>PROCESS</td><td>processing_timeP_name</td><td>WAIT</td><td>[Waiting time]W→</td></tr><tr><td>BRANCHING</td><td>Cond. Cond iCond j</td><td colspan="2"></td></tr></table>

A PROCESS is an activity or a series of activities. Activities performed solely by the server organization without customer involvement are not of interest, and thus not shown on the EEPC diagram. Time for such activities is treated as a wait in service. For example, if a customer orders food at a restaurant, the time between ordering and receiving the food is treated as a wait: the customer did not need to know details of how the order was processed inside the kitchen. Process is represented by a rectangle including its name and processing time.

BRANCHING is a conditional splitting of an event-process flow into sub-flows. Branching is represented by a diamond box with the branching condition inside it.

FLOW is the movement of a customer object between events and processes. The object is any entity of interest to the server organization that, on behalf of the customer, passes through the organization's internal processes or events. For example, if a customer orders a dish in the restaurant, the order slip becomes a customer object. Both customer and customer objects are treated as the arriving objects from system entry to exit in the discrete-event simulation. Flow component is represented by an arrow line showing the customer object optionally and its moving time.

WAIT is the customer's average delay before the start of an event or process due to a queue, internal process, or other condition of the server. Again, using the restaurant example, even though the internal process of the kitchen is hidden at the top level EPC diagram, it can be exploded into a lower level EPC. WAIT is represented by symbol W in a circle, along with the waiting time.

Figure 3 is a simple EEPC diagram illustrating the customer's visiting process at a restaurant. The modeling constructs are drawn on two dimensions: station dimension vertically and time dimension horizontally. Customers receive service as they move through these processes and events. The left column identifies the station with its number of servers. Customers arrive at this restaurant at two-minute intervals (E1). If there is a seat available, the customer will take the seat and place an order (P1). On average, there is a ten-minute wait (W1). After finishing the meal (P2), the customer will pay (P3) and exit (E2) the restaurant.

![](/api/attachments/N7PXHY7K/fulltext/images/58f19f0c612f091ae52b408354d963563adac3683b6a05b8d80cff688ffa25ac.jpg)  
Fig. 3. EEPC Diagram for a customer's visit to a restaurant.

## 2.3. Performance evaluation

Performance of a process is evaluated using a computerized simulation. With user-friendly and powerful simulation tools available, a visual (animation) approach is preferred. The visual approach moves icons to illustrate the changes to the customer and customer objects through the process. This perspective allows users (analysts, decision makers, managers, etc.) to verify and validate the simulation model [11].

For performance evaluation, we chose three factors – station's utilization, customer's delay time at a station, and cycle time – they may be calculated by the formulae in Table 2. The first factor is the utilization of each station. It indicates how much work is performed relative to its work capacity, which depends on the number of servers and working time. When process redesign takes place, stations with too low or too high utilization are targeted for redesign. Stations with low utilization should have more work load or over-loaded stations should transfer some of their excess work capacity to others.

The second factor is the customer's delay time at a station, which is the average of the sum of the moving time to the station and the waiting time for service. For example, after eating, the customer walks to the cashier (moving time) and waits in line to pay for the meal (waiting time). When redesigning business processes, the delay time at each station should be reduced as much as possible, because it directly affects customer satisfaction.

Table 2  
Performance evaluation factors and functions

<table><tr><td>Factor</td><td>Function</td></tr><tr><td>Utilization of  $station_k$ </td><td> $\frac{working\ amount_k}{(working\ time_k \times number-of-servers_k)}$ </td></tr><tr><td>Customer&#x27;s delay at  $station_k$ </td><td> $\sum_{p=1}^{t}\sum_{j=1}^{n}\frac{(moving\ time_{jk}+waiting\ time_{jk})}{n}$ </td></tr><tr><td>Cycle time</td><td> $\sum_{p=1}^{t}\sum_{k=1}^{t}\sum_{j=1}^{n}\frac{(moving\ time_{jk}+waiting\ time_{jk}+processing\ time_{jk})}{n}$ </td></tr></table>

where k = station number k; j = the customer at the station; p = a station participating in the business process; t = total number of stations in the business process; n = total number of customers that have passed through at stationk; working\_amount\_k = server's actual processing time at stationk; working\_time\_k = arranged working time at stationk; number\_of\_servers\_k = total number of servers at stationk; waiting\_time\_jk = the jth customer's waiting time at stationk; processing\_time\_jk = service time for jth customer at stationk; moving\_time\_jpk = the jth customer's moving time in the process flow from station\_p to station\_k.

The third factor is the cycle time. Cycle time is the total amount of time customers spend in the entire business process from start to finish. It consists of moving time, waiting time, and processing time at all stations through which customers pass. To improve customer satisfaction, cycle time, not processing time, should be reduced [14].

## 2.4. Performance-based process redesign guidelines

Performance of a business process needs to be improved in two ways: first, to maximize customer satisfaction, and second, to do it as efficiently as possible. For customer satisfaction, we have focused on the process cycle time and its most critical component: delay time. For an organization's management efficiency, we aim to improve each station's utilization. Based on these two factors, we classify any process into four situations and propose redesign guidelines for each of them as shown in Figure 4.

In Situation 1, customers pass through a highly utilized station with a short delay time. Since the station is highly utilized, it is an ideal situation for management. It requires no redesign action (G1).

Situation 2 occurs when the station is highly utilized but customer delay time is long. To shorten the delay time, we need to look at the station's work load. If a long delay time exists without work overload, then we should attempt to minimize customer's moving/wait-/waiting time (G2). As a way to do this, we may be able to remove redundant processes. This will reduce the time that the customer waits in queues, moving times, and thus total cycle time. It may also be possible to rearrange the processes and/or events to occur in parallel.

If the long delay time results from overloading the station's work capacity in Situation 2, we may be able to increase its work capacity (G3). For this purpose, we may assign some of the work to a less utilized station. If the work capacity cannot be increased by any information technology or procedural change, then we should consider adding more servers, such as installing additional hardware.

In Situation 3, customers pass through a less busy station with short delay time. From the customers' perspective, they may receive service rapidly, possibly as soon as they arrive at the station. But it is not best from the management perspective, because the station is under-utilized. Therefore we should transfer some work from other over-loaded stations (G4).

<table><tr><td>High</td><td>Situation 1G1. No Action</td><td>Situation 2G2. Minimize moving/waiting timeG3. Increase the station&#x27;s work capacity</td></tr><tr><td>Utilization (Station)</td><td rowspan="2">Situation 3G4. Transfer some of work capacity</td><td rowspan="2">Situation 4G5. Change customers&#x27; arrival patternsG6. Check and redesign work policy</td></tr><tr><td>Low</td></tr><tr><td></td><td>Short</td><td>Delay time(Customer)Long</td></tr></table>

Fig. 4. Performance-based situations and their redesign guidelines.

Situation 4 occurs when customers experience long delays though the stations are under-utilized – the worst situation. This may result from either a peak-load condition or a batch-oriented work policy. If the peak-time rush is the cause, we may try to change the customers' arrival pattern (G5). For instance, providing incentives may be considered to move utilization to light loading situations. In the restaurant case, if most customers come during the 12:00 noon to 1:00 p.m., then offer a special price incentive to arrivals before noon or after 1:00 p.m.

On the other hand, the station's batch-oriented work policy may be the cause. For instance, if account adjustment and expense handling tasks are performed once a week in the accounting department, we should consider a move to interactive G6.

## 3. Comparison of process modeling methods

Process modeling for BPR can proceed at two levels: conceptual and implementational. At the conceptual level, the main characteristics of the target business processes are captured to produce a clear and simple model. To promote easy understanding and quick detection of process bottlenecks, complex process details are hidden. In contrast, the purpose of the implementation-level process modeling for BPR is to produce a rich and detailed model which can be used to test the performance and feasibility of the various alternatives.

Table 3 compares four implementation-level process modeling methods with DPM method:

Task-Actor [6], DEMO (Dynamic Essential Modeling of Organizations)-ABCD (Actor-Bank-Channel-Diagram) [5], DSADE (Dynamic Systems, Analysis, Design and Evaluation) [7], and VPM (Virtual Process Measurement) [16]. The proposed model is sometimes used primarily for process representation or used for simulation. Process nature specifies whether the process modeling scope can be cross-functional or only for a simple functional area. Modeling orientation describes whether the process is modeled from the customer or organizational perspective. Place and time dimension, along with the modeling constructs are related to the expressiveness of the model, while measurement and existence of the redesign guidelines signal the completeness of each method.

Task–Actor is a process representation model, composed of Task (What) and Actor (Who) elements. Although this is a systematic model used for specification, representation, and simulation, its modeling method is server-oriented and it suggests neither redesign nor change guidelines. DEMO–ABCD is also a dynamic model used to represent the structure of a system through the interactions between actors. However, it is an interaction diagram. It is only for analysis, without time or place dimension and it does not support any measurement. DSADE is an analytical methodology for enhancing Structured Systems Analysis and Design (SSAD), DFD techniques, and CASE tools. Although it supports performance measurements based on the process and simulation model from the server organization's perspective, it suggests neither redesign guidelines nor verification and validation steps. VPM is a simulation method for assessing IT value through the measurement of computer-based process representation. For this purpose, it provides simulation and visualization of organizational processes and it can assess the relative, multidimensional value of IT across the various designs. Although VPM supports a systematic simulation method with some redesign heuristics, the model is difficult for users to understand because it is not based on any process model.

Analysis of implementation-level process modeling methods

<table><tr><td></td><td>Task-actor model</td><td>DEMO-ABCD</td><td>DSADE</td><td>VPM</td><td>DPM</td></tr><tr><td>Model Type</td><td>Process and simulation</td><td>Process</td><td>Process and simulation</td><td>Simulation</td><td>Process and simulation</td></tr><tr><td>Process nature</td><td>Cross-functional</td><td>Functional</td><td>Functional</td><td>Cross-functional</td><td>Cross-functional</td></tr><tr><td>Modeling orientation</td><td>Server-oriented</td><td>Mixed</td><td>Server-oriented</td><td>Server-oriented</td><td>Customer-oriented</td></tr><tr><td>Place dimension</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Time dimension</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Measurement</td><td>Time throughput</td><td>None</td><td>Time cost</td><td>Time cost risk</td><td>Time utilization</td></tr><tr><td>Redesign guidelines</td><td>No</td><td>No</td><td>No</td><td>Redesign heuristics</td><td>Performance-based guidelines</td></tr><tr><td>Modeling constructs</td><td>Task actor flow</td><td>Actor transac&#x27;n Ext. bank g-link, e-link, I-link</td><td>Process branching flow</td><td>Task flow</td><td>Event process branching flow wait</td></tr></table>

Table 4  
Comparison between Discrete-event simulation modeling and DPM

<table><tr><td></td><td>Discrete-event simulation modeling</td><td>DPM with EEPC</td></tr><tr><td>Objective</td><td>Problem solving with performance evaluation</td><td>Business process analysis and redesign</td></tr><tr><td>Modeling orientation</td><td>Organization-oriented</td><td>Customer-oriented</td></tr><tr><td>Modeling</td><td>Interaction between events</td><td>Customer&#x27;s movement and interaction with server organization</td></tr><tr><td>User</td><td>Simulation specialist</td><td>Employee, Manager (Non-specialist), BPR/Simulation specialist</td></tr><tr><td>Redesign support</td><td>No</td><td>Performance-based redesign guidelines</td></tr></table>

The DPM can represent the organization's critical business processes over geographical (place) and dynamic (time) dimensions exclusively from the customer's perspective. EEPC diagrams are easy to construct and understand by end-users as well as IT professionals.

In addition to the above, we can compare DPM with the classical discrete-event simulation (DES) modeling (See Table 4). DES can be viewed as a model of the interaction of discrete events occurring in the system and the system's state variables. However, while DES modeling aims at problem solving with performance evaluation, DPM aims at BPR. We need a process modeling formalism that reflects a customer's perspective. Also, while the DES modeling may be performed only by the simulation specialist, BPR cannot be processed without the broad participation of employees and managers from non-IS departments. To communicate with them, an understandability of the process model is critical.

## 4. Application of DPM method: Seoul Adventist Hospital case

The DPM method was applied to the Seoul Adventist Hospital. The hospital operates 17 departments and has 110 doctors and 406 beds. On average, about 1100 out-patients come to the hospital for doctor consultations each day. For our example, we picked the out-patient's process in the internal medicine department, examination room, and pharmacy, because it was representative of the most critical and time-consuming processes.

## 4.1. Analysis of performance: The current situation

The top level of the hospital's outpatient visit process is illustrated in Figure 5. It is initiated by a patient's arrival at the hospital (E1). Patients arrive at an interval of $0.45\mathrm{min}$ . Arrived patients register and pay the doctor's fee in advance (P1) after waiting in a queue. This process can be performed by one of the eight servers in an average processing time of $2\mathrm{min}$ (assumed to follow a normal distribution). 20.7 percent of the out-patients walk to the internal medicine department and the moving time follows a normal distribution with mean of $1\mathrm{min}$ and standard deviation of $0.5\mathrm{min}$ . Arriving at the internal medicine department's waiting room, the patient waits to be called. During that time, the patient chart will be delivered from the chart room to the department (W1); this takes about $30\mathrm{min}$ .

There are four doctors in the internal medicine department. Each out-patient consults one of them for about 10 min (P2). After the consultation, those who need additional step(s) – medicine or examination – have to pay in advance (P3) for the step(s). Arriving at the examination room, the patient submits the pre-paid slip (E2) and is examined(P4). Arriving at the pharmacy desk, the patient submits the prescription slip for medicine (E3). The amount of time the customer has to wait for medicine is represented as a wait (W2). If it has to be examined for unnecessary delays, the wait can be exploded into a lower level EEPC (Figure 6) where the prescription slip (customer object) takes the customer's (patient) role and goes through the internal pharmacy process. Any wait here can also be exploded further to trace the real process bottleneck(s). After receiving the medicine (E4), the patient leaves the hospital (E5).

![](/api/attachments/N7PXHY7K/fulltext/images/da5a27b6510a464d2b17df2db6b5e160a5ac685ce2c2f7b89027654f4ec29198.jpg)  
Fig. 5. EEPC diagram for internal medicine department's outpatient visit.

## 4.1.1. Process

There are two parts of the traffic that affect the performance of the visit process. First, there is the effect of other department processes (the pharmacy and examination department). Second, medicines or examinations are also requested by the in-patients ward. Since these two process traffics may affect the performance result, we include them in the simulation.

The current situation was simulated with SIMPROCESS II.5 [1], at a PC windows environment; this is an animation tool that enables us to visualize the behavior of the system and verify the simulation model.

In the hospital case, the simulation time is 8 h, because the hospital operates from 8 A.M. to 5 P.M. except for a 1 h lunch break. The number of replications can be set by choosing the desired risk $\alpha$ and the width of the $(1 - \alpha)$ confidence interval for the output variables selected. We set it at 19 times with a 95% confidence interval based on 3.87 as half width of the confidence interval and 8.66 as standard deviation.

From the simulation results, the cycle time of the process is 85.5 min. And patients seem to wait for too a long time at the internal medicine department (31.2 min) and at the pharmacy (21.9 min), while the utilization at the two stations are high (internal medicine department: 97.4%, pharmacy: 96.4%).

![](/api/attachments/N7PXHY7K/fulltext/images/eca194d55d377634c8e25bc06effedce63a38fd8a68752102dc28b9ea64391bc.jpg)  
Fig. 6. EEPC Diagram exploded from W2.

## 4.2. Validation of the simulation

The animation capability allows us to observe the simulation model in action. Also, it enables employees as well as simulation analysts to validate the model. The most definitive test of the validity of a simulation model is to establish that its output data closely approximate reality. This accuracy can be best established by some measure of the variability between the two outputs [17]. The most important result is the cycle time. To validate the simulation model, we obtained 50 observations from the internal medicine department using interviews. The comparison is given in Table 5.

To ascertain the validity, we performed a hypothesis test. Since both sample sizes were sufficiently large, we could assume that their underlying distributions were normal. For the two-tailed hypothesis test, we set two hypotheses $H_{0}(u1 - u2 = 0)$ and $H_{1}(u1 - u2 \neq 0)$ where u1 is the actual mean data and u2 is the simulated mean data. Thus, we could make the validation test with a 95% confidence interval where $\overline{X1}$ was the sample mean cycle time of the actual patient and $\overline{X2}$ was the sample mean cycle time of the simulated patient. According to the difference in mean time $(\overline{X1} - \overline{X2} = 1.56)$ and rejection region ( $|\overline{X1} - \overline{X2}| > 2.35$ ), we could not reject $H_{0}$ . Therefore we assume that the simulated situation was not significantly different from the actual one.

Comparison between actual and simulation data about cycle time

<table><tr><td>Factor</td><td>Actual data</td><td>Simulation data</td></tr><tr><td>Mean time</td><td>87.0 min</td><td>85.5 min</td></tr><tr><td>Standard deviation</td><td>9.2 min</td><td>8.7 min</td></tr><tr><td>Sample size</td><td>50</td><td>221</td></tr></table>

## 4.3. Redesign and performance evaluation

Using our proposed redesign guidelines, we investigated which of the stations incur long delay times. From the performance evaluation (Table 6), delay times at the internal medicine department (31.2 min) and the pharmacy (21.9 min) are longer than those at other stations. And, the utilizations of those two stations are high (97.4%, 96.4%). These two, therefore, belong to Situation 2 – long delay time and high utilization. We need to redesign the processes between these two stations.

Table 6  
Performance evaluation results about current case and redesign Case 1

<table><tr><td>Evaluation factor</td><td>Classification</td><td>Current case</td><td>Case 1</td><td>Comparison</td></tr><tr><td rowspan="4">Station&#x27;s utilization</td><td>Reception desk</td><td>82.0%</td><td>34.7%</td><td>-47.3%</td></tr><tr><td>I.M. department</td><td>97.4%</td><td>98.8%</td><td>+1.1%</td></tr><tr><td>Pharmacy</td><td>96.4%</td><td>78.0%</td><td>-18.3%</td></tr><tr><td>Examination room</td><td>71.4%</td><td>77.0%</td><td>-5.6%</td></tr><tr><td rowspan="4">Delay time</td><td>Reception desk</td><td>5.8 min</td><td>0.2 min</td><td>-5.6 min</td></tr><tr><td>I.M. department</td><td>31.2 min</td><td>47.4 min</td><td>+16.2min</td></tr><tr><td>Pharmacy</td><td>21.9 min</td><td>1.2 min</td><td>-20.7 min</td></tr><tr><td>Examination room</td><td>1.6 min</td><td>1.2 min</td><td>-0.4 min</td></tr><tr><td rowspan="2">Cycle time</td><td>Mean time</td><td>85.5 min</td><td>61.1 min</td><td>-24.3 min</td></tr><tr><td>Standard deviation</td><td>8.7 min</td><td>5.6 min</td><td></td></tr></table>

According to our redesign guideline (G2. Minimize customer's waiting time) in Situation 2, we consider performing process/event in parallel. That is, the medicine request/examination is transmitted electronically to the pharmacy or the examination room during the patient's consultation with the doctor. Also, we consider automating most of the activities inside the pharmacy to shorten the processing time. By the time the patient arrives at the pharmacy, the medicine is already waiting, etc.

The internal medicine department is also a redesign target, as it falls into Situation 2. According to the redesign guideline (G3), we should increase the station's work capacity. This depends on the number of doctors, because consultation, by nature, is a manual process. Since adding more servers (doctors) usually incurs high organizational costs, we need to recommend such an alternative very carefully and only after all other alternatives are tried.

Next, we consider patients at the reception desk. Since the current registration is performed manually, it is slow and time-consuming. Also, there are redundant tasks (P1, P3) in Figure 5. According to the redesign guideline (G2. Minimize customer's waiting time) in Situation 2, we integrated the registration (P1) and payment processes (P1, P3) and turned it into an event by issuing each patient a smart card with all personal health history and bank account information. When the patient arrives at the doctor's office, after checking this card at the reception desk with the registration system server, he or she is registered and the consultation history data are available. Also, all expenses can be handled through the bank account. All these changes are reflected in redesign Case 1.

Figure 7 shows the redesigned process for Case 1. It was simulated and its performance evaluation data were summarized. According to the simulation, the cycle time is shortened from 85.5 to 61.1 min. Patient's delay times at each station are shortened, except at the internal medicine department. And the utilization of the reception desk is reduced from 82% to 35% with the help of IT, the smart card.

Redesign Case 1 reveals some improvements in cycle time, patient's delay time, and utilizations of stations. But, we can expect more improvement because Case 1 still shows a long delay time at the internal medicine department and low utilization of the reception desk. Patients at the internal department still belong to Situation 2 – long delay time and high utilization. For redesign Case 2, we decided to increase the station's work capacity according to the suggested action guideline (G3. Increase the station's work capacity). Since the doctor's consultation work cannot be automated, we added two more doctors in redesign Case 2. Also, for patients at the reception desk (Situation 3 – low utilization and short delay time), we reduced the number of servers at the reception desk from 8 to 3 according to the guideline G4. (Transfer some of the work capacity.)

Performance evaluation results of redesign Case 2 and its comparison with the current situation are summarized in Table 7. The cycle time is shortened from 85.5 min to 18.2 min. Customer's delay times at each station are significantly shorter. Also, work load balancings among stations are more even, except for the reception desk that is now automated.

![](/api/attachments/N7PXHY7K/fulltext/images/c8c123d771c2f40a46a48f31b57d9ae0bc4b7c62093bbbc53c1e8d3e4a958af2.jpg)  
Fig. 7. EEPC Diagram for the outpatient visit process: Redesigned Case 1.

Table 7  
Performance evaluation results about redesign Case 2

<table><tr><td>Factors</td><td>Classification</td><td>Current case</td><td>Case 2</td><td>Comparison</td></tr><tr><td rowspan="4">Station&#x27;s utilization</td><td>Reception desk</td><td>82.0%</td><td>92.4%</td><td>+13.5%</td></tr><tr><td>I.M. department</td><td>97.4%</td><td>65.9%</td><td>-31.6%</td></tr><tr><td>Pharmacy</td><td>96.4%</td><td>79.5%</td><td>-16.8%</td></tr><tr><td>Examination room</td><td>71.4%</td><td>78.4%</td><td>-3.6%</td></tr><tr><td rowspan="4">Delay time</td><td>Reception desk</td><td>5.8 min</td><td>0.9 min</td><td>-4.8 min</td></tr><tr><td>I.M. department</td><td>31.2 min</td><td>2.4 min</td><td>-28.8 min</td></tr><tr><td>Pharmacy</td><td>21.9 min</td><td>1.3 min</td><td>-20.6 min</td></tr><tr><td>Examination room</td><td>1.6 min</td><td>1.5 min</td><td>-0.2 min</td></tr><tr><td rowspan="2">Cycle time</td><td>Mean time</td><td>85.5 min</td><td>18.2 min</td><td>-67.3 min</td></tr><tr><td>Standard deviation</td><td>8.7 min</td><td>2.1 min</td><td></td></tr></table>

## 5. Conclusion

In this research, we suggested a dynamic process modeling (DPM) method to support firms interested in redesigning their business processes with the help of a simulation technique. Such a modeling method enables us to model, not only the static elements of the process, but also its dynamic aspects. The dynamic process model – EEPC – can help while modeling and redesigning the business process entirely. Animated simulation techniques based on the model enabled us to perform evaluations. And the EEPC model, a customer-oriented cross-functional process model, is easy to use in communicating with non-IS employees or managers, though the discrete-event simulation model is rather difficult for the non-specialists to use.

To demonstrate the practicality of the method, we applied it to a real hospital. As this reveals, the DPM method reduces the risk of BPR by providing a better understanding of the target business process from the customer's viewpoint and showing how performance is affected by the proposed alternatives.

However, the hospital example we used oversimplifies the situation experienced in industry. First, although there are various satisfaction-related factors in industry, we selected only three general factors (delay time, utilization, cycle time). In real BPR projects, we need to consider each business-specific factor. Second, the example did not deal with the cost issue. In a real project, we should compare each alternative in terms of the trade-off between cost and other tangible and intangible benefits. Third, process-related data are not easy to obtain. For example, the station's capacity is required for the simulation. But each station's capacity is frequently not fixed or is hard to calculate because a server is often involved in more than one process and it may need to be performed by more than one server. The best method is the use of existing corporate data. However, this is seldom possible.

## Acknowledgements

The authors wish to thank the chairman of the editorial board, Professor Edgar H. Sibley, for his encouragement and thoughtful editorial help for this paper.

## References

[1] CACI Products Company, SIMFACTORY II.5 and SIMPROCESS manual, 1993.

[2] J.R. Caron, S.L. Jarvenpaa and D.B. Stoddard, “Business reengineering at CIGNA corporation: Experiences and lessons from the first five years,” MIS Quarterly, 17(3) (1994), pp.233–250.

[3] T. Davenport and M. Beers, “Managing information about processes,” Journal of Management Information Systems, 12(1) (1995), pp.57–80.

[4] T. Davenport and J.E. Short, "The new industrial engineering: Information technology and business process redesign," Sloan Management Review, Summer, 1990, pp.11–27.

[5] Jan L.G. Dietz, “Business modeling for business redesign,” Proceedings of the 27th Hawaii International Conference on Systems Sciences, Vol. IV, 1994, pp.723–732.

[6] R.C.J. Dur and P.W.G. Bots, “Dynamic modeling of organizations using task/Actor Simulation,” Dynamic Modeling of Information Systems II, Elsevier Science Publishers, 1992, pp.49–74.

[7] W.R. Eddins and R.L. Crosslin, “Using modeling and simulation in the analysis and design of information systems,” Dynamic Modeling of Information Systems, Elsevier Science Publishers, 1991, pp.61–88.

[8] V. Grover, S. Jeong, W. Kettinger, and J. Teng, “The implementation of business process reengineering,” Journal of Management Information Systems, 12(1) (1995), pp.109–144.

[9] G. Hall, J.; Rosenthal, and J. Wade, "How to make reengineering really work," Harvard Business Review, July-August 1993, pp.119-131.

[10] M. Hammer, “Reengineering work: Don’t automate, obliterate,” Harvard Business Review, July–August 1990, pp.104–112.

[11] S.V. Hoover and R.F. Perry, SIMULATION: A Problem-Solving Approach, Addison-Wesley, 1989.

[12] T. Housel, C.; Morris, and C. Westyland, “Business process reengineering at Pacific Bell,” Planning Review, May/June, 1993, 28–33.

[13] Y.G. Kim, “Global information schema to support information resource management,” Proc. of the 2nd International DSI Meeting, 1993, pp.645–648.

[14] Y.G. Kim, “Process modeling for BPR – Event-Process Chain Approach,” Proceedings of International Conference on Information Systems, 1995, pp.109–121.

[15] P.J. Kiviat, “Simulation, technology, and the decision process,” ACM Transactions on Modeling and Computer Simulation, 1(2) (1991), pp.89–98.

[16] M.E. Nissen, “Valuing IT through virtual process measurement,” Proceedings of International Conference on Information Systems, 1994, pp.309–323.

[17] J.L. Ringuest, “A chi-square static for validating simulation-generated responses,” Com. and Ops. Res., 13(4) (1986), pp.379–385.

[18] P. Sachs, “Transforming work: Collaboration, learning, and design,” Communications of the ACM, 38(9) 1995, pp.36–45.

[19] L. Schuman, “Making work visible,” Communications of the ACM, 38(9) (1995), pp.56–64.

[20] J.W. Van Meel, “Towards a safer Amsterdam: Dynamic modeling supporting organizational change,” Proceedings of the 26th Hawaii International Conference on Systems Sciences, 1995, pp.438–447.

[21] S. Wang, "Object-oriented task analysis," Information and Management, 29 (1995), pp.331-341.

[22] J.R. Warren, R.L. Crosslin, and P.J. MacArthur, "Simulation modeling for BPR," Information Systems Management, 12(4) (1995), pp.32-42.

![](/api/attachments/N7PXHY7K/fulltext/images/c29d42b4333f1705fb56aff7716172478b8bd6de3f2c942a7e28fb7a0a0a9e65.jpg)

Hee-Woong Kim is a Ph.D student at the Graduate School of Management of the Korea Advanced Institute of Science and Technology in Seoul. He received his B.S. and M.S. degrees in Industrial Engineering from the Pohang University of Science and Technology, Korea. His research areas are: IS Architecture Development, Process Modeling, and Simulation. He has published in Information and Management, Decision Sup-

port Systems, and Korean Journal of MIS Research. He has presented several papers at HICSS, DSI conference, and European Simulation Symposium.

![](/api/attachments/N7PXHY7K/fulltext/images/b616b9f66b1ff73207b9ced78e0dc31741bcad637ac73454ddd2fc9513cc8719.jpg)

Young-Gul Kim is an associate professor at the Graduate School of Management of the Korea Advanced Institute of Science and Technology in Seoul. He received his B.S. and M.S. degrees in Industrial Engineering from the Seoul National University, Korea and Ph.D Degree in MIS from the University of Minnesota. His active research areas are: IS Architecture Development, Data and Process Mod-

eling, and IT management. He has published in Communications of the ACM, Information and Management, Database, Journal of MIS, and Information Systems Management. Also, he has presented several papers at ICIS, HICSS, and DSI conferences.
