---
otero_id: 19756
otero_key: "XUGYFMYC"
title: "A novel decision support system for optimizing aircraft maintenance check schedule and task allocation"
authors: "Qichen Deng; Bruno F. Santos; Wim J.C. Verhagen"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113545"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

Qichen Deng <sup>a,\*</sup>, Bruno F. Santos <sup>a</sup>, Wim J.C. Verhagen <sup>b</sup>

<sup>a</sup> Section of Air Transport and Operations, Delft University of Technology, the Netherlands <sup>b</sup> Royal Melbourne Institute of Technology, Australia

## A R T I C L E I N F O

Keywords: Decision support Aircraft maintenance Task allocation Dynamic programming Bin packing

## A B S T R A C T

Modern aircraft have thousands of parts, systems, and components that need to be recurrently inspected or replaced. To keep the fleet airworthy, maintenance planners have to schedule the maintenance checks for each aircraft and the associated tasks. In practice, these two complex problems are solved following the experience of planners. resulting in sub-efficient solutions. This paper presents the first decision support system (DSS) devel: oped for optimizing both aircraft maintenance check schedule and task allocation. The DSS integrates aircraft maintenance check scheduling, task allocation to each maintenance check, and shift planning in the same framework. The practical relevance of the DSS is illustrated through three test cases. The results show that the DSS can be used not only to optimize maintenance plans but also to study future maintenance policies. The results reveal substantial improvements in all key performance indicators compared with the planning approach followed by a partner airline.

## 1. Introduction

Aircraft maintenance is a sequence of activities, including overhaul, repair, inspection, or modification of an aircraft or aircraft systems, components, and structures to ensure an aircraft retains an airworthy condition. In the aviation industry, a commercial aircraft must undergo regular maintenance to prevent component and system failures during operations. Many of the aircraft maintenance activities take place after an aircraft has been operating certain flight hours (FH), flight cycles (FC), or calendar days (DY). The FH, FC, and DY are known as usage parameters to indicate aircraft utilization. The maximum usage pa rameters allowed in operation are defined as inspection intervals.

Modern aircraft have thousands of parts, systems, and components that need to be recurrently inspected, serviced, and replaced. Many airlines adopt a top-down approach to plan aircraft maintenance:

## • Step 1 – Maintenance Check Scheduling

First group major maintenance tasks with the same or similar in spection intervals into letter checks: A-, B-,<sup>1</sup> C- and D-check, as showed in Table 1. Each check type is coupled with an elapsed time (time required for the execution of tasks within letter checks + time estimated for other tasks). Maintenance planners then create a letter check schedule (3–5 years for C-/D-check and 6–12 months for Acheck) according to pre-defined elapsed time of each check type. The letter checks are performed in the hangar.

## • Step 2 – Maintenance Task Allocation

Although some tasks can quickly be packaged into the letter checks, a large number of other tasks (e.g., more than 70% for an Airbus A320 aircraft) are dephased from the inspection intervals of these checks. It means that they either have to be manually allocated by maintenance operators to different maintenance events based on the suitability of the task to that check and the urgency of performing the task.

Despite the rapid expansion of the global air travel industry and the increase of fleet size, the advances in aircraft maintenance planning (AMP) have been struggling to keep up with the times. In practice, AMP involves scheduling maintenance checks to each aircraft, allocating tasks to each check, planning the workforce for each task, inventory optimization, and coordination of maintenance tools. For small airlines, AMP is not so demanding and can be done manually according to the experience of maintenance planners. For large airlines, the AMP problem becomes more complex – maintenance planners have to spend several days or weeks on scheduling maintenance activities because of the lack of efficient tools. Since, on average, 9%—10% of the total cost of airlines goes to aircraft maintenance, which is equivalent to about \$2.5 M per aircraft per year [2], the savings derived from efficient AMP can be very substantial.

Table 1  
Aircraft letter check and corresponding inspection interval [1].

<table><tr><td>Check type</td><td>Interval</td><td>Maintenance tasks</td></tr><tr><td>A-check</td><td>2–3 months</td><td>External visual inspection, filter replacement, etc.</td></tr><tr><td>B-check</td><td>-</td><td>Rarely mentioned in practice</td></tr><tr><td>C-check</td><td>18–24 months</td><td>Inspection of the individual systems and components</td></tr><tr><td>D-check</td><td>6–10 years</td><td>Inspection of most structurally significant items</td></tr></table>

To facilitate the AMP process, many companies engage in developing AMP systems. For example, Ref. [3] developed one of the first AMP tools to improve maintenance efficiency and reduce associated cost. After that, many companies followed and developed various tools, e.g., Sol umina MRO from iBASEt, Airline Suite from C.A.L.M Systems INC., WinAir from AV-Base Systems, and Maintenix from IFS, etc. To our best knowledge, all the available commercial tools focus on managing and tracking the status of the maintenance tasks, providing a valuable computer-aid solution to manual planning. However, none of them has the function of producing an optimized maintenance schedule automatically.

AMP is challenging due to the lack of optimization approaches for planning maintenance checks and associated tasks, even though there are many available computer-aid solutions. Two distinct limitations in the current academic and industrial state of the art can be discerned. as further discussed in Section 2: 1) a lack of decision support system (DSS) to optimize the maintenance check (A-, B-, C- and D-checks) schedule; 2) a lack of DSS for optimizing aircraft maintenance check and task execution in an integrated manner. In the literature, there is no work integrating the two problems in a single optimization framework.

In 2015, the AIRMES project was launched by Clean Sky Joint Un dertaking, a public-private partnership between the European Com mission and the European aeronautics industry, to optimize end-to-end maintenance activities within an airline operator’s environment [4]. We developed a DSS during the project to automate the maintenance planning process and provide maintenance check scheduling optimiza tion, optimal task allocation, and shift planning in one comprehensive solution. The contribution of our research is threefold:

• The DSS integrates aircraft maintenance check scheduling, mainte nance task allocation, and work shift planning in the same frame work. In practice, these processes are solved using different tools, while in the literature, these are seen as three different problems handled separately.

• We demonstrate that the DSS can improve aircraft utilization and reduce maintenance costs, compared with the current practice of airlines. It reduces the time needed for AMP from days or hours to 20–30 min.

• We also present the usefulness of the DSS in helping airlines evaluate different aircraft maintenance strategies before implementation.

This paper presents the architecture of the resulting DSS and the corresponding optimization modules for maintenance check schedule, task allocation, and shift planning. We also discuss the applicability of the DSS by presenting the results from a case study with one major European airline and several industry partners. The case study validates the utility of the DSS for both maintenance planning optimization and future scenario analysis.

The outline of this paper is as follows: Section 2 gives an overview of the relevant literature on the aircraft maintenance domain. The DSS architecture is presented in Section 3, aircraft maintenance check scheduling optimization, task allocation, and shift planning as well as their corresponding algorithms. Section 4 describes the demonstration exercise with data from the partner airline. The last section summarizes the research with concluding remarks and gives an outlook on future work.

## 2. Related work

The aviation industry is extremely competitive in Europe. The average net profit of airlines usually represents only up to 4%–5% of revenues and about 9%—10% of the total cost goes to aircraft mainte nance [2]. Efficient AMP is one useful way of reducing maintenance costs. The benefit of efficient AMP is two-fold: on the one hand, the increased aircraft availability indicates that there will be more aircraft available for commercial operations, and eventually, generating more revenues; on the other hand, it decreases the number of aircraft main tenance inspections, and therefore, reduces the maintenance operation costs in the long term. This section reviews the previous research on AMP from long-term planning (3–5 years) to short-term planning (several days to weeks).

## 2.1. Long-term aircraft maintenance planning

Long-term AMP aims to generate an aircraft heavy maintenance schedule (C- and D-checks) before determining the tasks within each check, also known as aircraft maintenance check scheduling (AMCS). It is indispensable since C-check has an interval of 18–24 months, and Dcheck is usually scheduled once every 6 years; airlines need a C- and Dcheck schedule to further plan the A- and B-checks and the associated tasks for all the (A-, B-, C-, and D-) checks. In 1977, Air Canada devel oped one of the first DSSs for the long-term AMCS, called AMOS [3]. AMOS was considered a computer-aid manual planning approach since the developers did not see the value of finding an optimal solution that could rapidly become obsolete due to uncertainty. It helped Air Canada reduce the time for planning a 5-year C-check schedule for its fleet from 3 weeks to a few hours. Besides, Ref. [3] defined the long-term (3–5 vears) planning, and it is the only available reference of the long-term AMP category before 2020.

Following this research direction, Ref. [5] proposed a dynamic pro gramming (DP) based methodology for long-term AMCS within the AIRMES project in 2020, adopting the assumptions, problem formula tion presented in [3]. It aimed to optimize the aircraft maintenance check schedule for the future 3–5 years. This work is the first step to wards building an integrated AMP framework, focusing on long-term AMP. The DP-based methodology generates an optimized 4-year schedule for both light and heavy maintenance within 15 min. The optimized maintenance check schedule can be further used to plan the maintenance tasks within each check and daily work shift.

## 2.2. Short-term aircraft maintenance planning

In contrast to the little available literature about long-term AMCS, there are many studies on short-term AMP in the topics of aircraft maintenance routing, maintenance personnel management, and main tenance task scheduling. The reason is that by optimizing short-term maintenance activities, airlines can see tangible benefits in a few days or weeks.

## 2.2.1. Aircraft maintenance routing

Aircraft maintenance routing (AMR) is to design flight routes for every aircraft to meet the maintenance requirements set by Federal Aviation Administration (FAA) and individual airline companies. Extensive research works have contributed to AMR through flight schedule design [6,7], determining routes flown by each aircraft [8–10], fleet assignment (assigning an aircraft model for each flight) [11–13], tail assignment (determining which aircraft should fly which segment) [14–16], or even addressing the aircraft routing in conjunction with crew pairing [17–19]. These studies usually consider aircraft mainte nance as an operational requirement but did not plan the maintenance checks or tasks.

## 2.2.2. Maintenance personnel planning

Maintenance personnel planning (MPP) is one of the main research directions of short-term AMP. An effective maintenance workforce supply can reduce operations costs while ensuring aviation safety and punctuality. It has attracted lots of attention from both industry and academia. Early in 1994, KLM Royal Dutch Airline and Erasmus Uni versity Rotterdam developed a DSS to smooth the workload of aircraft maintenance personnel by increasing the number of peaks of workloads and reducing the peak length [20]. It helped KLM improved the utili zation of maintenance technicians (the ratio of productivity labor-hours to total available labor-hour). After that, many researchers envisioned the potential benefits and continued the MPP study, such as optimizing the workforce supply [21–23], or minimizing the total labor cost [24,25]. However, MPP usually assumes that maintenance tasks are given rather than planning the tasks.

## 2.2.3. Maintenance task scheduling

Maintenance task scheduling (MTS) refers to allocating maintenance tasks to time slots so that the tasks can be executed before due dates. It includes task scheduling for aircraft line maintenance (coordinating maintenance tasks to be carried out at the gate during turnaround time and the required maintenance resources), daily hangar maintenance, or work shift. There are some studies addressing the MTS for line mainte nance, such as spreading the workload more uniformly across shifts [26], improving aircraft availability and reducing maintenance costs [27], or optimizing both workforce and tasks [28]. MTS for line main tenance planning has an operational nature. It only focuses on opti mizing a limited number of maintenance tasks during aircraft turnaround time.

Task scheduling for daily aircraft hangar maintenance can be seen in [29]. According to the authors, optimizing the daily hangar mainte nance tasks to be executed 24 h beforehand also maximizes the avail ability of fighting jets for the missions of the next day. The authors call attention to the fact that if we want to plan the daily maintenance task for each letter check, we have to look into a planning horizon longer than 24 h, especially for the C-/D-check. Besides, the daily maintenance task plan bridges the gap between AMCS and associated work shift planning. That is, we can better plan each morning/afternoon/evening shift and prepare the tools and aircraft spare parts if we know the daily maintenance tasks in advance. Hence, Ref. [30] proposed a bin packing approach to determine daily maintenance tasks (for each A-/B-/C-/Dcheck) given a long-term (3–5 years) maintenance check schedule for AIRMES. As a result, it gives a long-term (3–5 years) plan of mainte nance tasks for each day and a heterogeneous fleet of aircraft.

## 2.3. Concluding remarks for literature review

To our best knowledge, most of the studies in the AMP domain focus either on AMR or MPP, assuming that the maintenance tasks are given. There are some studies on MTS, vet most of them focus on line main. tenance problems. The long-term and short-term AMP was not yet considered in a single framework, nor was a DSS presented in the literature addressing the AMP. Synthesizing the literature review gives rise to two challenges in the AMP domain:

1. No DSS for aircraft maintenance planning optimization (AMPO) is presented in the academic literature that can generate an optimally integrated maintenance check and task execution plan at the fleet level.

2. Commercial DSSs addressing the fleet maintenance check level are relatively rare. Even so, they do not optimize the maintenance check schedule.

In practice, maintenance planners have to spend a significant amount of time and effort scheduling the aircraft letter checks and coordinating associated tasks execution activities. It can happen that with the aid of current DSSs, the maintenance planners still obtain an inefficient plan; this may, in the long-term, result in more letter checks and higher operation costs.

The DSS presented in this paper contributes to bridging two main research streams, long-term and short-term AMP, by integrating the AMCS problem and its methodology presented in [5], the MTS problem and the associated algorithm presented in [30], and a shift planning approach into the same framework.

## 3. System architecture

To address the challenges identified in Section 2, we developed a DSS specifically for AMP using the programming language Python and for Windows operating system. The DSS is a stand-alone software prototype and has already been converted to an executable file. It can be run on any individual PC without installation or a license. The DSS consists of three components (layers), a database, a model, and a graphical user interface (GUI):

\- Database: Store the input data, including the maintenance planning document (MPD) for aircraft manufacturers, fleet status, operational constraints, and available workforce from airlines.

\- Model: Process input data, optimize the aircraft maintenance check schedule and maintenance task execution plan.

\- Graphical User Interface (GUI): Allow users to interact with the DSS and visualize the planning results and the associated KPIs.

In this section, we present the structure of the DSS layer by layer, as illustrated in Fig. 1. We begin with description of database layer (Section 3.1) and input, followed by a detailed introduction of the optimization models and algorithm (Section 3.2). In Section 3.3, we outline the GUI of the DSS.

## 3.1. Database and input data

The database stores the input in the format of comma-separated values (CSV) and output in Excel. We classify the input into four categories:

## 3.1.1. Maintenance planning document

The maintenance planning document (MPD) is provided by the aircraft manufacturer. It specifies the maintenance tasks according to the aircraft structure, systems, and components, as well as correspond ing inspection intervals (as described in Table 1). The MPD gives strict criteria for aircraft maintenance – all letter checks and tasks have to be performed before the corresponding usage parameters reached their maximums (intervals). Any violation of maintenance task execution will prevent the aircraft from flying because of safety concerns.

## 3.1.2. Fleet status

We use Table 2 to illustrate the structure input data. The column Fleet shows the aircraft type. Tail No. indicates the aircraft tail number. Before and Next represent the previous and next letter checks respectively. DY, FH and FC are the usage parameters of the fleet. fh/day and fc/day are the average daily utilization of the fleet. Phase-In indicates when an aircraft starts in commercial operation. This is relevant information as old aircraft will phase out after a certain number of checks, and meanwhile, airlines have new aircraft in operation. If an aircraft will phase out, we give “− 1” to its next A-/C-/D-check, meaning that no more A-/

![](/api/attachments/XUGYFMYC/fulltext/images/86af9821e3b2cd990b0ba84c3c430ee9a49892d5dc57f2e7f78fbdd96ac90a85.jpg)  
Fig. 1. Architecture of the decision support system for AMPO.

Table 2  
An example of fleet status with respect to aircraft C-Check on 01/07/2020.

<table><tr><td>Fleet</td><td>Tail</td><td>Before</td><td>Next</td><td>DY</td><td>FH</td><td>FC</td><td>fh/day</td><td>fc/day</td><td>Phase-In</td></tr><tr><td>A320</td><td>AC-1</td><td>C 12.1</td><td>-1</td><td>212</td><td>2391</td><td>963</td><td>10.3</td><td>4.2</td><td>12/01/1998</td></tr><tr><td>A319</td><td>AC-2</td><td>C 10.1</td><td>C 11.1</td><td>607</td><td>6439</td><td>2600</td><td>9.9</td><td>4.1</td><td>08/06/1998</td></tr><tr><td>A321</td><td>AC-3</td><td>—</td><td>C 1.1</td><td>0</td><td>0</td><td>0</td><td>10.1</td><td>4.2</td><td>01/03/2021</td></tr></table>

C-/D-check needs to be scheduled. If the phase-in date of an aircraft is later than the current date, this aircraft only starts flying from the phase in date, and before that, its usage parameters remain 0.

## 3.1.3. Operational constraints

The operational constraints can be divided into two categories: commercial constraints and maintenance constraints. The operations center of airlines defines the commercial constraints. For example, the operations center may limit the availability of the aircraft to perform maintenance during commercial peak seasons (e.g., during the summer or specific holidays), or it may impose an earlier time limit to the maintenance check of a specific aircraft following the end of a leasing contract or the chartering of an aircraft to third parties.

The maintenance constraints are defined by the maintenance department, which specifies the maintenance capacity according to available maintenance resources, e.g., maintenance tools, workforce, and aircraft spare parts. This capacity is expressed as maintenance slots per day that define how many aircraft can be at the hangar for a specific type of maintenance. Furthermore, other maintenance constraints may apply, such as that no heavy checks can start on the same day to avoid high demanding works in parallel or that some aircraft already have maintenance predefined before computing the schedule. The latter takes place, e.g., when part of the maintenance program is executed by thirdparties or partially depends on third-parties, not being subject to rescheduling. A typical example of this is the replacement of landing gears or engines. Besides, maintenance task execution follows the sequence of opening the access panel, inspection, maintenance, and closing the access panel.

## 3.1.4. Workload of each task and available workforce

The workload of each task is provided by the airline. Each task as sociates a task code, a set of skill types required to perform the task, labor hours for each skill type defined by the MPD. If there are urgent unscheduled tasks, they can be added to the input with corresponding duration, workforce, and due dates.

The available workforce is the input given by airlines and divided per skill types (e.g., engines and flight control systems, avionics, aircraft metallic structure, and painting, etc.). The available workforce includes the total number of maintenance technicians per skill type, the number of hours a technician work per day on average, and the number of available technicians on each week in the year. The available workforce constrains the task allocation to maintenance checks because it is limited per day, according to the daily workforce schedule. Since aircraft maintenance work is usually ongoing 24 h every day, airlines divide the daily workforce into three groups of workers to perform their duties and call those groups morning shift, afternoon shift, and night shift. In the input data, the maintenance planners of airlines have to specify the maximum number of technicians in one shift and also for one task.

## 3.2. Optimization model and algorithms

The model layer has three optimization models in total: a mainte nance check scheduling model (AMPO-1 in Fig. 1), a maintenance task allocation model (AMPO-2), and a shift planning model (AMPO-3). The design of the model layer follows the top-down approach. The DSS first generates an optimal aircraft maintenance check schedule in AMPO-1, then allocates the maintenance tasks to each maintenance check in AMPO-2. After that, it plans the shifts according to the maintenance tasks to be executed in each letter check.

The reason for following the top-down approach is that it is impos sible to plan the work shifts before knowing the task execution or plan all maintenance tasks one after another for the entire fleet without knowing the maintenance check schedule. The maintenance check schedule indicates in which letter check a maintenance task could be allocated without violating the safety regulation defined by the MPD. The work shifts can only be planned based on the maintenance check schedule and the tasks to be executed within each check. The overall optimization process entails the following seven steps:

## Step I: Extract maintenance check and task inspection interval

The Model component extracts the maintenance check interval and inspection intervals of all tasks from the MPD stored in the database. The inspection intervals are the maximum DY/FH/FC allowed in commercial operation.

Step II: Collect DY/FH/FC of each aircraft and remaining utilization of all systems and components

The Model component loads the fleet status (current DY/FH/FC for each check type since its previous execution) and average aircraft daily utilization (FH/day and FC/day) stored in the database (the second step in the model layer of Fig. 1). It also collects the usage parameters of all aircraft systems and components and computes the remaining utiliza tion of each system and component. For example, consider a component of an aircraft with max usage parameters 120 DY, 1000 FH, and 600 FC, and this aircraft has daily utilization of 10 FH/day and 5 FC/day. Given current usage parameters 500 FH and 250 FC, the remaining utilization of this component would be 50 days.

Step III: Identify maintenance opportunities and detailed operational constraints

According to the input constraints from the operation center and maintenance department of airlines, the Model component identifies the maintenance opportunities. The maintenance opportunities indicate the time-window when a specific check type is allowed to be performed and the corresponding check capacity. Table 3 presents a format of main tenance opportunities stored in the database after input processing:

For a specific maintenance check type, if a time window is not within any Start Date and End Date in Table 3, it means that the associated capacity for this period is 0.

Step IV: Generate optimal aircraft maintenance check schedule (AMPO 1)

After processing and loading the input data, the user can specify the planning horizon for aircraft maintenance check scheduling (AMCS) optimization. The default planning horizon is three years to ensure that it includes at least one C-check for each aircraft, but the user can choose from two to six years.

The model formulation of AMPO-1 can be seen in Appendix A. Currently, there is only one obiective function within the DSS for AMCS minimizing the unused flight hours of the entire fleet [3] for a period specified by the user. It is possible to add more objectives or even multiobjectives later on. The optimal letter check schedule is generated using a dynamic programming (DP) based methodology, as presented in [5]. The idea is to check whether the maintenance capacity in the future is sufficient or not for each maintenance action (e.g., performing a C-check or several A-checks). This methodology follows a forward induction approach, incorporating a maintenance priority solution to deal with the multi-dimensional action vector, as well as a discretization and state aggregation strategy to reduce outcome space at each time stage. If the input data does not lead to a feasible maintenance check schedule, the DSS will suggest the best dates for adding necessary maintenance slots to make it feasible.

Step V: Generate optimal task allocation for maintenance checks for each aircraft (AMPO-2)

Table 3  
An example of maintenance opportunities stored in database.

<table><tr><td>Fleet</td><td>Check type</td><td>Start date</td><td>End date</td><td>Capacity</td></tr><tr><td>A320</td><td>C-/D-Check</td><td>Oct-1 – 2017</td><td>May-31-2018</td><td>3</td></tr><tr><td>A320</td><td>A-Check</td><td>Every Monday</td><td>Every Friday</td><td>1</td></tr><tr><td>A320</td><td>A-Check</td><td>Sep-26-2017</td><td>Sep-26-2017</td><td>2</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr></table>

Once the AMPO-1 plans the optimal letter check schedule for the entire fleet, the DSS allocates the maintenance tasks to each letter check, assuming that there are sufficient aircraft spare parts and maintenance tools. The task allocation aims at minimizing the total cost in task execution, subject to the daily available workforce. It adopts an algo rithm based on the worst-fit decreasing (WFD) [30]. The task allocation algorithm treats the maintenance resources within each check as bin and the maintenance tasks as items. It consists of:

• Bin Definition: The task allocation within AMPO-2 divides the entire aircraft letter check schedule into time segments (bins) according to the number of parallel maintenance checks. For example, in Fig. 2, C1.2, C12.1, C7.1, C7.2, and C9.1 are the maintenance checks. T1–T7 are the bins defined by the AMPO-2. The sizes of the bins (time segments) are determined based on the aircraft maintenance resources, i.e., the number of maintenance technicians working during the time periods of the bins (the available workforce per day is given in the input).

• Bin Selection: The heuristic algorithm sorts the time segments ac cording to the associated capacity (maintenance resources), from highest to lowest. When the algorithm selects a bin to allocate a maintenance task, it always starts with the bin with the highest remaining capacity. The availability of bin (time-segment) depends on the aircraft having letter checks during that time-segment. In the example of Fig. 2, T1 is only available for aircraft (AC) 16, T2 is available for both AC-16 and AC-17, etc.

• Item Allocation: The algorithm allocates the items (tasks) following the rules of “the most urgent item (task) first”. Each maintenance task must be allocated before its due date; otherwise, it generates extra capacities and notifies the DSS user.

The model formulation of AMPO-2 is presented in Appendix B, the task allocation algorithm is described in detail in [30]. For the mainte nance tasks that have to be executed in a strict order, the task allocation algorithm groups those tasks into a package, and this task package is also considered as one item (one big task). After that, the algorithm allocates the item (task package) to a bin (time segment of a maintenance check). In this way, it ensures that all tasks within the package will be executed. For instance, the maintenance tasks presented in Table 4 have to be executed in the order of:

$$
1 2 0 0 - \mathrm{A} \rightarrow 1 2 0 0 - \mathrm{B} \rightarrow 1 2 0 0 - \mathrm{C} \rightarrow 1 2 0 0 - \mathrm{D}\tag{1}
$$

In this example, technicians have to execute task 1200-A (open the panel at component xxx) first. Otherwise, they cannot continue to inspect or replace the component xxx. After the technicians complete the task 1200-C, they have to execute 1200-D (close the panel at component xxx). The task allocation algorithm groups these four tasks into one package and label it as “Item 1200”, providing information of the sequence when presenting the results to the user.

Step VI: Integrate the optimal maintenance check schedule and task allocation plan

In this step, the DSS first creates a folder for each aircraft with the name “aircraft tail number + Time + Date”, and decouples the entire maintenance check schedule obtained from AMPO-1 according to aircraft tail numbers. In each folder, it saves the associated maintenance checks in the format of Excel. Next, the DSS organizes all the mainte nance tasks from AMPO-2 within the same letter check in one table in CSV format and puts this CSV file in the folder according to the aircraft tail number of the letter check. The user can compare or keep track of the historical optimization results according to the time and date in the folder name.

Step VII: Plan the maintenance workforce and shifts (AMPO-3)

<table><tr><td></td><td>04-21</td><td>04-24</td><td>04-27</td><td>04-30</td><td>05-03</td><td>05-06</td><td>05-09</td><td>05-12</td><td>05-15</td><td>05-18</td><td>05-21</td><td>05-23</td><td>05-27</td><td>05-30</td><td>Check</td></tr><tr><td>AC-1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td></td><td></td><td>C1.2</td></tr><tr><td>AC-5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>C12.1</td></tr><tr><td>AC-16</td><td colspan="2">T1</td><td colspan="2">T2</td><td colspan="4">T3</td><td>T4</td><td></td><td></td><td></td><td></td><td></td><td>C7.1</td></tr><tr><td>AC-17</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>C7.2</td></tr><tr><td>AC-21</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>T6</td><td>T7</td><td></td><td></td><td>C9.1</td></tr></table>

Fig. 2. Overlapping maintenance checks are divided into several time segments (bins) in AMPO-2 - i.e., T1, $\mathrm { T } 2 , . . . , \mathrm { T } 7 .$

Table 4  
An example of tasks that have to be executed in the order of $\mathbf { A } \to \mathbf { B } \to \mathbf { C } \to \mathbf { D } .$

<table><tr><td>Fleet</td><td>Tail No.</td><td>Date</td><td>Item</td><td>Description</td></tr><tr><td>A320</td><td>AC-1</td><td>Mar-19-2019</td><td>1200-A</td><td>Open the panel at aircraft component xxx</td></tr><tr><td>A320</td><td>AC-1</td><td>Mar-19-2019</td><td>1200-B</td><td>Inspect aircraft component xxx</td></tr><tr><td>A320</td><td>AC-1</td><td>Mar-19-2019</td><td>1200-C</td><td>Replace component xxx</td></tr><tr><td>A320</td><td>AC-1</td><td>Mar-19-2019</td><td>1200-D</td><td>Close the panel at aircraft component xxx</td></tr></table>

The Model component also has an algorithm (AMPO-3) to plan the shift (morning/afternoon/night), create job cards, and estimate the workload after the AMPO-2 completes the task allocation for all letter checks. Due to the uncertainty associated with the workforce available per shift in the long term, the optimal maintenance check schedule and task execution plan may quickly become obsolete. Thus, the AMPO-3 only creates the work shifts and job cards for the initial weeks (1–2 weeks) of the planning horizon.

The shift planning algorithm allocates the maintenance tasks to each shift, respecting the workforce available per shift and the sequence of opening access panel, inspection, maintenance, and closing access panel (and this is the only task execution sequence we have to follow in both AMPO-2 and AMPO-3 according to the specification of our airline partner). Fig. 3 illustrates the workflow of shift planning function (AMPO-3). AMPO-3 first assigns the tasks of opening the access panel to the morning shift. If there is no available workforce left in the morning shift, it continues to assign those tasks to the afternoon shift (or even night shift) until all the tasks of opening access panels are allocated. Next, the algorithm assigns the inspection works, and after that, the maintenance tasks. The tasks of closing the access panel are allocated at last. The shift planning process continues until it loops over the task execution plans of all maintenance checks. When it finishes, the DSS will store the results in the database according to the aircraft tail number of the tasks.

## 3.3. Graphical user interface

The GUI serves the purpose of interacting with DSS users. The DSS users can load input data, start the AMPO, visualize the optimization results and associated KPIs, change operational constraints (planning horizon, the number of maintenance slots, or reserve slots for specific maintenance activities), and export the output data via the GUI. Those actions are the basic requirements for the GUI from the DSS users, identified by the AIRMES project group.

The GUI of the DSS has a single main window, divided into five screens. The user can see the maintenance check schedule of all aircraft for the entire planning horizon on a daily basis or per hangar view on different screens. The GUI also displays key performance indicators (KPIs), the tasks allocated per maintenance check, the workforce assigned per day (of the first few weeks), the identification of the maintenance interval tolerances used, the maintenance slots generated as additional to the given capacity. The user can also use the GUI to set the planning horizon, modify the start dates of specific maintenance checks, and change the operational constraints, such as adding/reducing maintenance slots or reserve maintenance slots for other maintenance activities. We use Figs. 4 and 5 to illustrate the main features of the DSS.

In ${ \mathrm { F i g . ~ } } 4 ,$ the marker ① indicates the main screen of the DSS. The main screen displays the aircraft maintenance check schedule per day per aircraft, computation time, and the number of extra maintenance slots created during optimization for a specific planning horizon. The marker ② indicates the $2 ^ { \mathrm { n d } }$ screen of the DSS. The $: 2 ^ { \mathrm { n d } }$ screen displays the maintenance check schedule for the entire fleet in the hangar view. The marker ③ indicates the screen of displaying the KPIs, including the mean FH, mean $\mathrm { F C } ,$ total maintenance checks, distribution of unused FH and FC for each check type, and the number of merged A- in $\mathrm { C } { \mathrm { - } } / \mathrm { D } { \mathrm { - } }$ Checks.

In the $2 ^ { \mathrm { n d } }$ screen, the DSS user can further see the maintenance tasks of each check. If the DSS user selects a maintenance check, a dialogue box will be popped up to display the aircraft tail number, maintenance check label, current DY, FH, and FC. The user can click the button “Show Tasks”, as indicated by marker ④ in Fig. 5. The DSS will display a list of maintenance tasks within the check and a figure that shows the work load distribution and the work shifts. The user can also change the start date of a specific check by clicking the button indicated by marker ⑤. The DSS will re-optimize the entire schedule according to the new specification from the user.

## 4. Demonstration and evaluation

The DSS was demonstrated and validated in a demonstration exer cise organized as part of the AIRMES project, on 51 aircraft, in March 2019. The exercise was carried out in collaboration with one of the major European airlines and one of the leading aircraft manufacturers and observed by the Clean Sky 2 Joint Undertaking partners involved in the related research effort.

This exercise aimed to validate the value of the DSS and demonstrate its applicability, primarily for AMP optimization and the study of future maintenance scenarios. For this reason, two test cases were performed and discussed. In the first test case, we aimed to validate the DSS and benchmark its performance by comparing the solution obtained with the maintenance schedule of the airline. In the second test case, we inves tigated the current considerations of the airline about its future main tenance policies and fleet developments. The results were checked and validated by the airline experts, providing valuable insights to the airline on future maintenance limitations and solutions.

## 4.1. Standard aircraft maintenance check scheduling optimization on fleet maintenance data

We received the input for AMCS on March $1 9 ^ { \mathrm { t h } }$ 2019 and optimized the A- and C-checks for the A320 family of our airline partner from

![](/api/attachments/XUGYFMYC/fulltext/images/301cb815d9063ce2a923bcd6ef232be7b7707c41f070e09c39ea8b3851eae325.jpg)  
Fig. 3. Workflow of shift planning (AMPO-3).

March $2 0 ^ { \mathrm { t h } }$ 2019 to December $3 1 ^ { \mathrm { s t } } 2 0 2 1$ , under the same operational constraints as the airline. According to the requirements of our airline partner, D-checks are merged within C-check in the following pattern:

$$
\mathrm{C} - 1, \quad \mathrm{C} - 2, \underbrace {\mathrm{C} - 3} _ {\mathrm{D} - \text { check }}, \quad \mathrm{C} - 4, \quad \mathrm{C} - 5, \underbrace {\mathrm{C} - 6} _ {\mathrm{D} - \text { check }}, \mathrm{C} - 7, \quad \mathrm{C} - 8, \underbrace {\mathrm{C} - 9} _ {\mathrm{D} - \text { check }}, \dots\tag{2}
$$

We compared our results with the maintenance schedule available at the airline (Airline Schedule). According to the results illustrated in Figs. 6 and 7, the AMPO-1 of the DSS outperforms the planning approach of the airline. The AMPO-1 results in 6946.5 FH for C-check and 705.1 FH for A-check, higher than 6783.8 FH and 701.1 FH from the main tenance schedule of the airline, but the result of AMPO-1 has one fewer C-check and three fewer A-checks. Our airline partner also checks the maintenance check schedule obtained using the DSS and agrees that the

DSS generates a better schedule than the maintenance planners. Besides, the AMPO-1 of the DSS optimizes both the aircraft A- and C-check schedule for 2019–2021 within only 10 min. It means that the DSS user can run the DSS to update its aircraft maintenance check schedule if there are changes instead of manually shuffling the A-/C-checks to make another feasible one.

From a saving and revenue management perspective, since airlines spend on average \$150 K–\$350 K on a C-check [1] and \$10 K–\$15 K on an A-check, one fewer C-check and three fewer A-checks in total can result in a potential saving of \$0.1 M–\$0.4 M for the considered time horizon of roughly three years. Furthermore, a C-check lasts about 1–4 weeks, and an A-check lasts 24 h in this case study. One reduced Cchecks and three fewer A-checks are equivalent to about 10–31 days of aircraft availability for commercial operations. This may generate a

AlRMES - Aircraft Maintenance Planning Optimization

File Function View About

![](/api/attachments/XUGYFMYC/fulltext/images/97428f92821e5c71469ede9e3e8fc5446a1ea6dcc563c867dfb165e99ead6511.jpg)  
Fig. 4. Main screen of the DSS.

![](/api/attachments/XUGYFMYC/fulltext/images/dbdf09838876b6110d5d26564b4f2abf442ea6c54d29baf35b1105694dde1808.jpg)  
Fig. 5. The 2<sup>nd</sup> screen of the DSS.

![](/api/attachments/XUGYFMYC/fulltext/images/ae579614d7228d8af887b7b2573f3b520b67494d4b20aad60cf22eb5889ceb51.jpg)

![](/api/attachments/XUGYFMYC/fulltext/images/0652d0d7b94ede857f679241c58fc897aeff9c38042149d18964cd1a9239c0f1.jpg)

![](/api/attachments/XUGYFMYC/fulltext/images/125839cac292840d8685cd0c0a632732eb2421d89c3846f772ef726cc13df6a8.jpg)

![](/api/attachments/XUGYFMYC/fulltext/images/1a6f4e2354d7d1c25aabd298ec4186982d3e0517b505c3cc0b0562f30f8ba035.jpg)

![](/api/attachments/XUGYFMYC/fulltext/images/0c3ac7cd3b0a19be4861c776e3f2eebd40dc018871d0734a0d36629108ab44cb.jpg)

![](/api/attachments/XUGYFMYC/fulltext/images/bbdc27be288a042239648d55537ef50de54d7f7595d245fe3e812e438bf694f8.jpg)

Fig. 6. The KPIs of maintenance check schedule of the airline. We used the DSS to load the maintenance check schedule of the airline directly and visualized the results on the interface.  
![](/api/attachments/XUGYFMYC/fulltext/images/85b3d6f0b9636cf91b064226221e0ca8a99f6c41e1599e36cee28c3dabeb6c0f.jpg)  
Fig. 7. The KPIs of maintenance check schedule from the AMPO-1 of the DSS.

considerable amount of revenue for the airline. According to an eco nomic evaluation performed by another Clean Sky project, the imple mentation of the DSS can potentially reduce the base maintenance costs by 2.7% for point-to-point carrier airlines, 0.5% for large hub and spoke carrier airlines, and 2.4% for small hub and spoke carrier airlines.

Following the demonstration of AMPO-1, we continued to test the task allocation (AMPO-2) of the DSS. The AMPO-2 allocated the main: tenance tasks using the optimal maintenance check schedule created by the AMPO-1. It addressed the task allocation for maintenance check schedule of Mar 20<sup>th</sup> 2019–Dec 31<sup>st</sup> 2021 within 10 min. The outcome of AMPO-2 is an optimal task allocation plan for the entire fleet and all letter checks, including over 60,000 tasks. An example of the outcome from AMPO-2 can be seen in Fig. 8. To verify the AMPO-2, we compared the optimal task allocation plan with the results from a commercial optimization solver. The comparison showed that the AMPO-2 produces results within an optimality gap of only 0.028%. Our airline partner also validated the optimal task allocation plan and its feasibility by bench marking our solution with the task allocation solution they had for the following year. The maintenance planners of the airline stated that the results from optimal task allocation are feasible for practical implementation.

After the AMPO-2 completed the optimal task allocation for all maintenance checks, the AMPO-3 planned the work shifts and creates job cards for technicians. Our airline partner set the horizon of shift planning for two weeks. Fig. 9 shows an example of the results from AMPO-3. The $1 ^ { \mathrm { s t } }$ column shows the aircraft tail number. The $2 ^ { \mathrm { n d } }$ and $3 ^ { \mathrm { r d } }$ columns indicate the date and work shifts. The $4 ^ { \mathrm { t h } }$ column describes the item or action, and the $5 ^ { \mathrm { t h } }$ column tells the maintenance planner where the maintenance work is in the aircraft. The last eight columns imply the workload needed for each skill type. The airline evaluated the work shifts after the demonstration and indicated that the work shifts of the first 2–3 days are almost the same as they planned, yet the difference becomes dramatic in the second week. It is worth mentioning that, fo example, if a task requires one labor-hour for a specific skill type, it can be one technician spending an hour, or two technicians spend half an hour, or even four technicians spend 15 min performing the task.

## 4.2. Evaluation of aircraft maintenance strategies using the DSS

In the second test case, we used the DSS to evaluate different maintenance strategies before implementation. Each strategy is modeled as a test scenario, and all scenarios are compared to the baseline scenario (Airline Schedule). Three maintenance strategies (test scenarios) were proposed by the airline:

1. Scenario 1: increase the number of daily C-check slots from three to four but shorten the period in which C-checks can be performed from the current October–May to November–March;

2. Scenario 2: increase the fleet size from 51 to 66 aircraft without changing the maintenance periods or number of slots available;

3. Scenario 3: increase the fleet size from 51 to 66 aircraft but now increasing the A-check slots by one on Fridays.

Table 5 shows the KPIs from test scenarios. We also include the KPIs from the previous demonstration and use the airline schedule as the baseline scenarios. First of all, without considering other costs, we see the benefit per aircraft from implementing the DSS (DSS Schedule) compared with the baseline scenario (Airline Schedule) for a 3-year planning horizon:

$$
\text { C - Check }: \quad \underbrace {2 0 . 6} _ {\text { gain }} + \underbrace {4 . 9} _ {\text { saving }} - \underbrace {0} _ {\text { cost }} = 3 0. 9 \mathrm{K}\tag{3}
$$

$$
\text { A - Check }: \quad \underbrace {5 . 7} _ {\text { gain }} + \underbrace {0 . 7} _ {\text { saving }} - \underbrace {0} _ {\text { cost }} = 6. 4 \mathrm{M}\tag{4}
$$

The KPIs of Scenario 1 indicate that shortening the C-check periods

![](/api/attachments/XUGYFMYC/fulltext/images/73d658d3633302b91a1e1cd2b5274893d0c15fd4a4524292944918c3597cc5c2.jpg)  
Fig. 8. Results of optimal task allocation (AMPO-2).

<table><tr><td rowspan="2">Aircraft</td><td rowspan="2">Date</td><td rowspan="2">Shift</td><td rowspan="2">Item</td><td rowspan="2">Block</td><td colspan="8">Skill Type and Required Labor-Hours</td></tr><tr><td>S 1</td><td>S 2</td><td>S 3</td><td>S 4</td><td>S 5</td><td>S 6</td><td>S 7</td><td>S 8</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Morning</td><td>Open panel ‘734’</td><td>—</td><td>0.6</td><td>0.2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Morning</td><td>Open panel ‘151KW’</td><td>—</td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Morning</td><td>Open panel ‘312AR’</td><td>—</td><td>0.1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Afternoon</td><td>251100-TP-1</td><td>INSP</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2.0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Afternoon</td><td>575161-01-2</td><td>INSP</td><td>0.8</td><td>0</td><td>0</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.1</td><td>0</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Afternoon</td><td>792000-C4-2</td><td>LUB</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Night</td><td>575164-01-4</td><td>ABAC</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Night</td><td>575164-01-4</td><td>INSP</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td></tr><tr><td>AC-1</td><td>09-20-2018</td><td>Night</td><td>575164-01-4</td><td>FEAC</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr></table>

Fig. 9. An example of work shifts planned by AMPO-3.

Summary of KPIs from the airline schedule $( 3 ^ { \mathrm { r d } }$ column), the AMCS optimization for the first test case $( 4 ^ { \mathrm { t h } }$ column), and the different scenarios from the second test case $( 5 ^ { \mathrm { t h } } - 7 ^ { \mathrm { t h } }$ column). The “Airline Schedule” serves as the baseline scenario. “Gain” represents the potential income generated per aircraft from having more days for commercial operations (due to more/few days for A- or C-checks) compared with the baseline scenario. “Saving” represents the reduction of maintenance costs per aircraft due to more/fewer checks. “Cost” represents the costs per aircraft for creating extra slots.

<table><tr><td colspan="2">KPIs 20/03/2019-31/12/2021</td><td>Airline schedule</td><td>DSS schedule</td><td>Scenario 1</td><td>Scenario 2</td><td>Scenario 3</td></tr><tr><td rowspan="7">C-check</td><td>Average FH</td><td>6783.8</td><td>6946.5</td><td>6959.8</td><td>6543.8</td><td>6012.3</td></tr><tr><td>Average FC</td><td>2896.4</td><td>2954.8</td><td>2955.4</td><td>2802.5</td><td>2570.2</td></tr><tr><td>Total Checks</td><td>72</td><td>71</td><td>69</td><td>73</td><td>76</td></tr><tr><td>Extra Slots</td><td>0</td><td>0</td><td>61</td><td>0</td><td>0</td></tr><tr><td>Gain [$]</td><td>-</td><td>26.0 K</td><td>78.0 K</td><td>-20.1 K</td><td>-80.4 K</td></tr><tr><td>Saving [$]</td><td>-</td><td>4.9 K</td><td>14.7 K</td><td>-3.8 K</td><td>-15.2 K</td></tr><tr><td>Cost [$]</td><td>-</td><td>0</td><td>66.0 K</td><td>0</td><td>0</td></tr><tr><td rowspan="7">A-check</td><td>Average FH</td><td>701.1</td><td>705.1</td><td>665.0</td><td>690.6</td><td>664.3</td></tr><tr><td>Average FC</td><td>300.8</td><td>302.5</td><td>285.6</td><td>292.7</td><td>281.6</td></tr><tr><td>Total Checks</td><td>764</td><td>761</td><td>811</td><td>929</td><td>967</td></tr><tr><td>Extra Slots</td><td>3</td><td>3</td><td>4</td><td>75</td><td>9</td></tr><tr><td>Gain [$]</td><td>-</td><td>5.7 K</td><td>-89.9 K</td><td>-243.8 K</td><td>-299.9 K</td></tr><tr><td>Saving [$]</td><td>-</td><td>0.7 K</td><td>-11.5 K</td><td>-31.3 K</td><td>-38.4 K</td></tr><tr><td>Cost [$]</td><td>-</td><td>0</td><td>0.7 K</td><td>40.9 K</td><td>3.4 K</td></tr><tr><td colspan="2">Total benefit per aircraft</td><td>-</td><td>37.3 K</td><td>-75.4 K</td><td>-339.8 K</td><td>-437.3 K</td></tr></table>

According to our airline partner:  
1) One day of operation generates on average \$97.5 K of revenue.  
2) The A-check of an A320 family aircraft lasts one working day and costs on average \$12.5 K.  
3) The C-check of an A320 family aircraft lasts on average 13.6 working days (slots).  
4) One fewer A-(C-)check means the entire fleet can have 1(13.6) more days for operations.  
5) The C-check of an A320 family aircraft costs on average \$250 K (\$18.4 K per working day).  
6) The cost of creating one extra A-/C-check slot is three times as one normal slot.

while increasing the C-check capacity, as considered by the airline, is not enough to cope with the C-check demand from the current fleet size and leads to a loss of \$75.4 K in total per aircraft for two check types. Although it gains \$78.0 K from more days of commercial operations compared with the baseline scenario (Airline Schedule) and saves \$14.7 K because of performing fewer C-checks, the airline needs to spend \$66.0 K per aircraft on creating extra C-check slots (non-existent daily slots are added to the schedule, representing moments that technicians have to work extra-time or that additional workforce has to be hired). The majority of loss comes from A-check due to grounding aircraft more often for A-checks (− \$89.9 K from commercial operations and -\$11.5 K for performing more A-check) and creating more extra A-check slots (− \$0.7 K). The reason is that the optimization algorithm of AMPO-1 tries to ground the aircraft for A-check more often to defer the need for a C-check. For example, consider an aircraft with a C-check interval of 7500 FH/730 DY and an average daily operation of 15 FH. If this aircraft has no A-check, it will be grounded and performed a C-check after 500 days since the FH usage parameter reaches 7500 FH before the DY usage parameter reaches 730 DY. If there is one A-check scheduled before the C-check (A-check lasts one day). this aircraft can have the Ccheck after 501 days, Similarly, if the aircraft is scheduled two A-checks it can have the C-check after 502 days, and so forth. Based on the results of the Scenario 1 evaluation, we suggested that the airline should use its current maintenance strategy rather than the new one (described in Scenario 1).

For Scenario 2, we observed that the current A-check capacity is not sufficient to handle the increased A320 fleet size according to the results shown in Table 5. Eventually, it leads to a huge loss, − \$339.8 K, on average per aircraft. Apart from the loss from C-check due to fewer commercial operations (− \$20.1 K) and performing more C-check (− \$3.8 K), A-check contributes most to the loss, − \$243.8 K from com mercial operations and -\$31.3 K from performing more A-checks. Be sides, it needs to spend \$40.9 K on average per aircraft on creating extra A-check slots.

To cope with the soaring A-check demand from increased fleet size, the airline proposes to add one A-check slot on Friday, as described in Scenario 3. According to the DSS results, creating one additional aircraft A-check slot on Friday (Scenario 3) significantly reduces the need for extra A-check capacity from 75 to 9 compared with Scenario 2, meaning that the cost of creating extra slots is reduced (from \$40.9 K to \$3.4 K). However, it also increases the number of checks for both check types, resulting in a huge revenue loss from commercial operations. The total loss increases by $4 3 7 . 3 ~ - ~ 3 3 9 . 8 ~ = ~ 9 7 . 5 \mathrm { K }$ on average per aircraft compared with Scenario 2. We found out that the optimization algorithm schedules C-check more frequently to provide more opportunities to merge the A-checks in C-checks (since the airline primarily wanted to avoid creating extra slots). Based on the results of Scenario 2 and Sce nario 3, we suggested that adding one A-check slot per week is not sufficient for the increase of fleet size, and the airline should consider adding more A-check slots to cope with the increased maintenance check demand.

## 5. Conclusion

This paper presents a novel decision support system (DSS) that ad dresses aircraft maintenance planning optimization in an integrated fashion, automating repetitive tasks while enabling fast, efficient, human-in-the-loop decision making for optimized planning purposes. First of all, the DSS is capable of optimizing the aircraft maintenance check schedule. Secondly, based on the optimal maintenance check schedule, the DSS allocates maintenance tasks to each maintenance check considering the overlapping situation (having multiple checks on going in the same period). Thirdly, the DSS plans the work shift respecting the task sequence in practice. It can potentially help airlines improve their maintenance planning efficiency, reduce the related maintenance operation costs, and even assess their maintenance stra tegies. Therefore, the DSS makes significant contributions relevant to both scientific research and industry application.

The DSS bridges the gap between long-term AMCS and short-term shift planning. It integrates aircraft maintenance check scheduling, maintenance task allocation and, work shift planning in the same plat form. A demonstration exercise with a major European airline shows that the DSS can generate a comprehensive optimal maintenance plan for a planning horizon of three years within half an hour. It means air lines can use the DSS to reduce the time needed for aircraft maintenance planning from several days to about 30 min. More importantly, considering the uncertainty that might impact aircraft utilization or maintenance activities, we make it possible for the maintenance plan ners to run the DSS in a short time to update the current plan. Whenever there are changes in the aircraft maintenance tasks or maintenance ac tivities, maintenance planners can quickly make new decisions using the DSS and re-organize the tools, workforce or promptly prepare the aircraft spare parts.

Besides, the demonstration exercise results show that the DSS

## Appendix A. AMPO-1 model formulation

reduces the number of A-/C-checks by three/one while increasing the expected average FH of A-/C-check by 2.4%/0.6% for a planning hori zon of 3 years compared with the maintenance check schedule made using the planning approach of the airline. The reduced A- and C-checks could lead to a significant saving in maintenance costs. The improved aircraft utilization also indicates that there will be more aircraft avail able for day-to-day commercial operations to generate additional reve nue. After the demonstration exercise, the DSS was tested and classified by the Clean Sky Joint Undertaking partners to be at a Technology Readiness Level Six (TRL 6). Nevertheless, the tool still has some limi tations that have to be addressed in the future if a higher TRL is aimed:

Aircraft maintenance check scheduling model • The primary goal of AIRMES was on the development of the opti mization algorithms, so future efforts should focus on improving the GUI.

• Define requirements and specifications that will facilitate direct integration of the DSS with other information systems used by air lines, including the development of the Application Programming Interface (API) and, potentially, a Software Development Kit (SDK).

• Include the number of aircraft spare parts in the constraints in the task allocation (AMPO-2) model.

Another interesting direction is to incorporate condition-based maintenance (CBM) by taking health prognostics and diagnostics into consideration when developing maintenance plans. Although including CBM in the DSS will increase model complexity and computation time, it will prepare the tool to cope with a current trend in the aircraft main tenance research and operational communities.

Finally, it is worth mentioning that although the DSS is tailored to aircraft maintenance planning optimization, it can also be adjusted to address similar problems, such as train or bus maintenance planning for the coming days or weeks, or to match the maintenance demand with operation timetables. For example, the main screen of the DSS can be changed to display daily operation hours and maintenance duration. The algorithm described in [5] can be adapted for similar maintenance scheduling or even more general scheduling problems (e.g., vehicle routing or production planning) since the idea of the algorithm is to estimate the consequence of each possible (maintenance) action before making a decision. For such applications, the DSS framework can be maintained.

## CRediT authorship contribution statement

Qichen Deng: Conceptualization, Methodology, Software, Valida tion, Formal analysis, Writing - original draft. Bruno F. Santos: Writing - review & editing, Supervision, Project administration, Funding acquisition. Wim J.C. Verhagen: Writing - review & editing, Project administration, Funding acquisition.

This research work is part of AIRMES project, which received fund ing from the Clean Sky 2 Joint Undertaking under the European Union’s Horizon 2020 Research and Innovation Programme under grant agree ment No 681858. We would like to show gratitude to the associated AIRMES partners for providing their aircraft maintenance data and validation of the proposed methodology and its practical relevance. For more information, please visit www.airmes-project.eu.

## Acknowledgements

objective function and constraints. A detailed description of the aircraft maintenance check scheduling (AMCS) model and the associated optimization algorithm can be found in [5].

$$
\min _ {\pi} \sum_ {t = t _ {0}} ^ {T} \sum_ {k \in K} \sum_ {i = 1} ^ {N} \left[ \chi_ {i, t} ^ {k} \left(I _ {k - \mathrm{FH}} ^ {i} - \mathrm{FH} _ {i, t} ^ {k}\right) + \left(1 - \chi_ {i, t} ^ {k}\right) P _ {a} \theta_ {i, t} ^ {k} + P _ {d} \eta_ {i, t} ^ {k} \right]\tag{A.1}
$$

subject to:

$$
\widetilde {z} _ {i, t} ^ {k} = \left\{ \begin{array}{l l} 0 & \text { if } z _ {i, t} ^ {k} = t - 1 \\ z _ {i, t} ^ {k} & \text { otherwise } \end{array} \right.\tag{A.2}
$$

$$
\widetilde {\delta} _ {i, t} ^ {k} = \left\{ \begin{array}{l l} 0 & \text { if } z _ {i, t} ^ {k} = t - 1 \\ 1 & \text { otherwise } \end{array} \right.\tag{A.3}
$$

$$
\widetilde {M} _ {t} ^ {k} = \sum_ {h} M _ {h, t} ^ {k} - \sum_ {i = 1} ^ {N} \widetilde {\delta} _ {i, t} ^ {k}\tag{A.4}
$$

$$
z _ {i, t + 1} ^ {k} = \left\{ \begin{array}{l l} t + L _ {i} ^ {k} \left(y _ {i, t} ^ {k}\right) & \text { if } \chi_ {i, t} ^ {k} = 1 \\ \widetilde {z} _ {i, t} ^ {k} & \text { otherwise } \end{array} \right.\tag{A.5}
$$

$$
\delta_ {i, t + 1} ^ {k} = \left\{ \begin{array}{l l} 0 & \text { if } \chi_ {i, t} ^ {k} = 1 \\ \widetilde {\delta} _ {i, t} ^ {k} & \text { otherwise } \end{array} \right.\tag{A.6}
$$

$$
\Delta \mathrm{DY} _ {i, t + 1} ^ {k} = \underbrace {\left(\mathrm{DY} _ {i , t} ^ {k} + 1\right)} _ {\mathrm{DY} _ {i, t + 1} ^ {k}} - \underbrace {\left[ I _ {k - \mathrm{DY}} ^ {i} + \left(1 - \theta_ {i , t} ^ {k}\right) e _ {k - \mathrm{DY}} ^ {i} - \varepsilon_ {i , t} ^ {k - \mathrm{DY}} \right]} _ {\text { actual   DY   interval   of   type } k \text { check }}\tag{A.7}
$$

$$
\Delta \Psi_ {i, t + 1} ^ {k} = \underbrace {\left(\Psi_ {i , t} ^ {k} + \psi_ {i , t}\right)} _ {\text { usage   parameters   of } t + 1} - \underbrace {\left[ I _ {k - \Psi} ^ {i} + \left(1 - \theta_ {i , t} ^ {k}\right) e _ {k - \Psi} ^ {i} - \varepsilon_ {i , t} ^ {k - \Psi} \right]} _ {\text { actual   interval   of } \Psi (\Psi \in \{\mathrm{FH}, F C} \}\tag{A.8}
$$

$$
\eta_ {i, t + 1} ^ {k} = \left\{ \begin{array}{l l} 1 & \chi_ {i, t} ^ {k} = 0, \max \left\{\Delta \mathrm{DY} _ {i, t + 1} ^ {k}, \Delta \mathrm{FH} _ {i, t + 1} ^ {k}, \Delta \mathrm{FC} _ {i, t + 1} ^ {k} \right\} > 0 \\ \widetilde {\eta} _ {i, t} ^ {k} & \text { otherwise } \end{array} \right.\tag{A.9}
$$

$$
\mathrm{DY} _ {i, t + 1} ^ {k} = \left(1 - \delta_ {i, t} ^ {k}\right) \left(\mathrm{DY} _ {i, t} ^ {k} + 1\right)\tag{A.10}
$$

$$
\Psi_ {i, t + 1} ^ {k} = \left(1 - \delta_ {i, t} ^ {k}\right) \left[ \Psi_ {i, t} ^ {k} + \left(1 - \delta_ {i, t} ^ {\mathrm{K} \backslash k}\right) \psi_ {i, t} \right]\tag{A.11}
$$

$$
\varepsilon_ {i, t + 1} ^ {k - \mathrm{DY}} = \left\{ \begin{array}{l l} \max \Bigl \{0, \Psi_ {i, t} ^ {k} - I _ {k - \mathrm{DY}} ^ {i} \Bigr \} & \text { if } \chi_ {i, t} ^ {k} = 1 \\ \varepsilon_ {i, t} ^ {k - \mathrm{DY}} & \text { otherwise } \end{array} \right.\tag{A.12}
$$

$$
\varepsilon_ {i, t + 1} ^ {k - \Psi} = \left\{ \begin{array}{l l} \max \Bigl \{0, \Psi_ {i, t} ^ {k} - I _ {k - \Psi} ^ {i} \Bigr \} & \text { if } \chi_ {i, t} ^ {k} = 1 \\ \varepsilon_ {i, t} ^ {k - \Psi} & \text { otherwise } \end{array} \right.\tag{A.13}
$$

$$
\theta_ {i, t + 1} ^ {k} = \left\{ \begin{array}{l l} 1 & \text { if } m a x \Big \{\varepsilon_ {i, t + 1} ^ {k - \mathrm{DY}}, \varepsilon_ {i, t + 1} ^ {k - \mathrm{FH}}, \varepsilon_ {i, t + 1} ^ {k - \mathrm{FC}} \Big \} > 0 \\ 0 & \text { otherwise. } \end{array} \right.\tag{A.14}
$$

$$
y _ {i, t + 1} ^ {k} = \left\{ \begin{array}{l l} y _ {i, t} ^ {k} + 1 & \text { if } \chi_ {i, t} ^ {k} = 1 \\ y _ {i, t} ^ {k} & \text { otherwise } \end{array} \right.\tag{A.15}
$$

$\mathbf { L } _ { \mathrm { i } } ^ { \mathrm { k } } \left( \mathbf { y } _ { \mathrm { i , t + 1 } } ^ { \mathrm { k } } \right)$ is the elapsed time specified by airline.

(A.16)

$\mathrm { f h } _ { i , t + 1 } ^ { k }$ is estimated according to historical aircraft FH.

(A.17)

$\mathrm { f c } _ { i , t + 1 } ^ { k }$ is estimated according to historical aircraft FC.

(A.18)

$$
\mathrm{DY} _ {i, t + 1} ^ {k} \leq I _ {k - \mathrm{DY}} ^ {i} + \left(1 - \theta_ {i, t} ^ {k}\right) e _ {k - \mathrm{DY}} ^ {i} - \varepsilon_ {i, t} ^ {k - \mathrm{DY}}\tag{A.19}
$$

$y _ { i , ~ t } ^ { k }$ Next maintenance label for of type k check of aircraft i on the day t

$M _ { h , \ t } ^ { k }$ Binary variable to indicate if a type k check can be performed in hangar h on the day t

$z _ { i , ~ t } ^ { k }$ The end date of type k check of aircraft i

Q. Deng et al.

Decision Support Systems xxx (xxxx) xxx

$$
\Psi_ {i, t + 1} ^ {k} \leq I _ {k - \Psi} ^ {i} + \left(1 - \theta_ {i, t} ^ {k}\right) e _ {k - \Psi} ^ {i} - \varepsilon_ {i, t} ^ {k - \Psi}\tag{A.20}
$$

$$
\chi_ {i, t} ^ {k} \leq \frac {\sum_ {\tau = t} ^ {t + L _ {i} ^ {k} \left(y _ {i , t} ^ {k}\right)} M _ {h , \tau} ^ {k}}{L _ {i} ^ {k} \left(y _ {i , t} ^ {k}\right)}, \quad t \in [ t _ {0}, T ]\tag{A.21}
$$

$$
\sum_ {i = 1} ^ {N} \delta_ {i, t} ^ {k} \leq \sum_ {h} M _ {h, t} ^ {k}, \quad t \in [ t _ {0}, T ]\tag{A.22}
$$

$$
\sum_ {i = 1} ^ {N} \chi_ {i, t} ^ {k} \leq \left\{ \begin{array}{l l} 1 & \text {   if   } d _ {k} > 0 \text {   and   } \sum_ {i = 1} ^ {N} \chi_ {i, \tau} ^ {k} = 0, \forall \tau \in [ t - d _ {k}, t) \\ M _ {t} ^ {k} & \text {   otherwise   } \end{array} \right.\tag{A.23}
$$

The objective of the aircraft maintenance check scheduling is to minimize the sum of the total unused flight hours $\chi _ { i , \ t } ^ { k } ( I _ { k \mathrm { - F H } } ^ { i } \mathrm { ~ - ~ } \mathrm { F H } _ { i , \ t } ^ { k } )$ of all maintenance checks and for the entire fleet over the planning horizon $[ t _ { 0 } , T ] . P _ { a }$ is the penalty of using maintenance interval tolerance (using tolerance is allowed when there is no feasible maintenance check schedule found during the optimization). $P _ { d }$ is the cost of creating an extra maintenance slot.

Constraints (A.2)–(A.6) update the available maintenance slots of all letter check types before scheduling aircraft letter checks. Constraints $\mathrm { ( A . 7 ) - }$ (A.18) update the utilization of each aircraft, depending on the maintenance check decision of day t (how many aircraft will be scheduled maintenance checks and how many checks should be performed for each check type). Constraints (A.19)–(A.23) ensure that the number of maintenance check scheduled are no larger than the available slots.

We proposed a dynamic programming (DP) based methodology to address the AMCS. First of all, we find out how many possible actions $( \mathrm { i } . \mathrm { e } . ,$ , how many checks can be performed for each check type) of a day. Secondly, for each possible action, we calculate if the number of available slots in the future is sufficient after performing the action. Among the possible actions, we only keep the ones that require minimal extra slots and the associated fleet status after performing the action and then move forward to the next day using the new fleet status. The detail of the DP-based methodology can also be found in [5].

Nomenclature

$$
\mathrm{DY} _ {i, t} ^ {k}
$$

$$
\mathrm{FC} _ {i, t} ^ {k}
$$

$$
\mathrm{FH} _ {i, t} ^ {k}
$$

$$
L _ {i} ^ {k} (y _ {i},
$$

$$
\left. \begin{array}{c} k \\ t \end{array} \right)
$$

$$
M _ {t} ^ {k}
$$

<table><tr><td colspan="2">AMCS model parameters</td></tr><tr><td> $d_k$ </td><td>Minimum interval between the start dates of two type  $k$  checks.</td></tr><tr><td> $e_{k-DY}^i$ </td><td>Maximum DY tolerance of type  $k$  check interval of aircraft  $i$ </td></tr><tr><td> $e_{k-FH}^i$ </td><td>Maximum FH tolerance of type  $k$  check interval of aircraft  $i$ </td></tr><tr><td> $e_{k-FC}^i$ </td><td>Maximum FC tolerance of type  $k$  check interval of aircraft  $i$ </td></tr><tr><td> $fc_{i,t}$ </td><td>Average daily FC usage for aircraft  $i$  at day  $t$ </td></tr><tr><td> $f_{h_i,t}$ </td><td>Average daily FH usage for aircraft  $i$  at day  $t$ </td></tr><tr><td> $I_{k-DY}^i$ </td><td>Interval of type  $k$  check of aircraft  $i$  in terms of DY</td></tr><tr><td> $I_{kFH}^i$ </td><td>Interval of type  $k$  check of aircraft  $i$  in terms of FH</td></tr><tr><td> $I_{k-FC}^i$ </td><td>Interval of type  $k$  check of aircraft  $i$  in terms of FC</td></tr><tr><td> $P_d$ </td><td>Cost for creating one extra maintenance slot</td></tr><tr><td> $P_a$ </td><td>Penalty for an aircraft using the tolerance</td></tr></table>

<table><tr><td colspan="2">Other parameters</td></tr><tr><td>h</td><td>Hangar indicator</td></tr><tr><td>i</td><td>Aircraft indicator</td></tr><tr><td>k</td><td>Maintenance check type indicator, k ∈ K = {A,B,C,D}</td></tr><tr><td>N</td><td>Total number of aircraft</td></tr><tr><td>nk</td><td>The number of hangars for type k check</td></tr><tr><td>t</td><td>Indicator of calendar day</td></tr><tr><td>T</td><td>Final day in planning horizon</td></tr><tr><td>t0</td><td>First day in planning horizon</td></tr></table>

$$
\delta_ {i, t} ^ {k}
$$

$$
y _ {i} ^ {k},
$$

$$
M _ {t} ^ {k} = \sum_ {h} M _ {h,} ^ {k}
$$

$$
\begin{array}{c} \mathcal {E} _ {i} ^ {k - \mathrm{DY}} \\ \varepsilon_ {i} ^ {t} \end{array}
$$

$$
\begin{array}{c} \varepsilon_ {i, t} \\ k - \mathrm{FH} \\ \varepsilon_ {i, t} \end{array}
$$

$$
\varepsilon_ {i, t} ^ {k - \mathrm{FC}}
$$

$$
\eta_ {i, t} ^ {\kappa}
$$

(continued on next page)

(continued )

<table><tr><td colspan="2">Decision variables and related attributes:</td></tr><tr><td></td><td>Binary variable to indicate if aircraft  $i$  is grounded and waiting for a slot of type  $k$  check on the day  $t$ </td></tr><tr><td> ${\theta }_{i,t}^{k}$ </td><td>Tolerance usage indicator of type  $k$  check of aircraft  $i$  on the day  $t$ </td></tr><tr><td> ${\chi }_{i,t}^{k}$ </td><td>Binary variable to indicate if aircraft  $i$  starts a type  $k$  check on the day  $t$ </td></tr><tr><td> $x_{t}$ </td><td>Available action on the day  $t$ </td></tr><tr><td> $\pi$ </td><td>Scheduling policy</td></tr><tr><td> $\Psi$ </td><td> $\Psi \in \{ \text{FH, FC} \}$ </td></tr><tr><td> ${\Psi }_{i,t}^{k}$ </td><td> ${\Psi }_{i,t}^{k} \in \{ {\mathrm{{FH}}}_{i,t}^{k},{\mathrm{{FC}}}_{i,t}^{k}\}$ </td></tr><tr><td> ${\psi }_{i,t}^{k}$ </td><td> ${\psi }_{i,t}^{k} \in \{ {\mathrm{{fh}}}_{i,t}^{k},{\mathrm{{fc}}}_{i,t}^{k}\}$ </td></tr></table>

## Appendix B. AMPO-2 model formulation

## Aircraft maintenance task allocation model

In Appendix B, we present the model formulation of AMPO-2 (aircraft maintenance task allocation for each letter check) of the DSS and briefly explain the objective function and constraints. A detailed description of the task allocation model and the associated solution approach can be found in [30].

min c<sup>t</sup><sub>i,k</sub> ⋅x<sup>t</sup><sub>i,k</sub> k∈K i∈N<sub>k</sub> t∈R<sub>i,k</sub>

(B.1)

subject to:

$$
\sum_ {t \in R _ {i, k}} x _ {i, k} ^ {t} = 1, \quad \forall i \in N _ {k}, \quad \forall k \in K\tag{B.2}
$$

$$
\sum_ {k \in K} \sum_ {i \in N _ {k}} \sum_ {j \in J} G R _ {i, k} ^ {j} \cdot x _ {i, k} ^ {t} \cdot \sigma^ {j, l} \leq \overline {{G R}} _ {t} ^ {l}, \quad \forall t \in T _ {k}, \quad \forall l \in J\tag{B.3}
$$

$$
\sum_ {m \in R _ {p, k}} d ^ {m} \cdot x _ {p, k} ^ {m} - \sum_ {t \in R _ {i, k}} d ^ {t} \cdot x _ {i, k} ^ {t} \leq \overline {{d}} _ {i, k}, \forall i \in N _ {k}, \forall p \in O _ {i, k}, \forall k \in K\tag{B.4}
$$

$$
\sum_ {m \in R _ {p, k}} f h ^ {m} \cdot x _ {p, k} ^ {m} - \sum_ {t \in R _ {i, k}} f h ^ {t} \cdot x _ {i, k} ^ {t} \leq \overline {{{{f h}}}} _ {i, k}, \forall i \in N _ {k}, \forall p \in O _ {i, k}, \forall k \in K\tag{B.5}
$$

$$
\sum_ {m \in R _ {p, k}} f c ^ {m} \cdot x _ {p, k} ^ {m} - \sum_ {t \in R _ {i, k}} f c ^ {t} \cdot x _ {i, k} ^ {t} \leq \overline {{f c}} _ {i, k}, \forall i \in N _ {k}, \forall p \in O _ {i, k}, \forall k \in K\tag{B.6}
$$

$$
x _ {i, k} ^ {t} \in \{0, 1 \}, \quad \forall k \in K, \quad \forall i \in N _ {k}, \quad \forall t \in T _ {k}\tag{B.7}
$$

The objective function (B.1) aims at minimizing the total de-escalation costs, which can be calculated by comparing how earlier the task item is allocated when compared with its desired due day [31]:

$$
c _ {i, k} ^ {t} = \frac {O _ {-} d a y _ {i} - d ^ {t}}{\text { interval } _ {i}} \cdot \left[ \sum_ {j \in J} \left(\sum_ {l \in J} G R _ {i, k} ^ {l} \cdot \sigma^ {l, j}\right) \cdot \text { labor\_rate } _ {j} + \text { other\_costs } _ {i} \right]\tag{B.8}
$$

Constraint (B.2) guarantees that each task item is allocated exactly once. Constraints (B.3) ensures that the available labor hours for each skill type is not exceeded in each of the maintenance time segments. The other three set of constraints (B.4)–(B.6) are the maintenance time-intervals constraint.

We developed a task allocation heuristic based on the worst-fit decreasing algorithm (WFD). First of all, we divide the entire maintenance check schedule into several time segments, according to the periods of overlapped maintenance checks $( \mathrm { i . e . } ,$ , periods that several aircraft having the same type of maintenance checks). Next, we sort the time segments according to their associated available labor-hours in descending order. After that, we allocate each maintenance task to the last possible segment before its due dates. The detail of the task allocation can be found in [30].

Nomenclature

Sets

i: task indicator

$K \colon$ set of aircraft.

$N _ { k } .$ set of task items for aircraft k $( k \in K )$

$T _ { k } \mathrm { : }$ set of time segments for aircraft k $( k \in K )$

$R _ { i , k } \mathrm { : }$ set of time segments for task item $i ( i \in N _ { k } )$ of aircraft $k \left( k \in K \right)$

$J ;$ set of skills.

$O _ { i , k }$ unit set with the task item that follows task item $i ( i \in N _ { k } )$ of aircraft $k \left( k \in K \right)$

$c _ { i , k } ^ { t } \mathrm { : }$ cost of allocating task item $i ( i \in N _ { k } )$ from aircraft $k \left( k \in K \right)$ to maintenance opportunity belonging to time segment $t \left( t \in T _ { k } \right)$

$\overline { { G R } } _ { t } ^ { j } \mathrm { : }$ amount of available labor hours of skill type $j \in J )$ at time segment t.

GR<sup>j</sup> : amount of labor hours of skill type j prescribed to perform task item i of aircraft k.

$\sigma ^ { j , l _ { \bullet } }$ “non-routine rate” indicating the amount of labor hours needed from skill type l for every labor-hour prescribed from skill type j (note: $\sigma ^ { j , j } \geq$ $1 . 0 \quad \forall j \in J )$

$\overline { { d } } _ { i , k } \mathrm { : }$ maximum number of days between rescheduling task item $i \left( t \in T _ { k } \right)$ for aircraft k $( k \in K )$

$d ^ { t } \colon$ number of days from the start of the planning horizon till maintenance opportunity belonging to time segment t.

$\overline { { f h } } _ { i , k } \mathrm { : }$ maximum number of flight-hours between rescheduling task item i for aircraft k.

$f h ! :$ number of accumulated flight-hours from the start of the planning horizon till maintenance opportunity belonging to time segment t.

$\overline { { f c } } _ { i , k } \mathrm { : }$ maximum number of flight-cycles between rescheduling task item i for aircraft k.

$f c ! ^ { t . }$ number of accumulated flight-cycles from the start of the planning horizon till maintenance opportunity belonging to time segment t.

O\_day : total days of aircraft operations from the start of the planning horizon to the due date of performing task item i, following the task fix interval and if no resource constraints are considered.

interval : average fix interval for task item i measured in days.

labor\_rate<sub>j</sub>: labor rate, per hour, of skill type ${ \mathfrak { i } } \left( { \mathfrak { j } } \in J \right)$

other\_costs : non-labor costs associated with task item $i ( i \in N _ { k } )$ of aircraft $\mathfrak { c } \left( k \in K \right)$ , such as costs of spare parts and tooling. Decision variables

x<sup>t</sup> $k \colon 1$ if task item i is assigned to maintenance opportunity belonging to time segment t for aircraft $k ,$ and 0 otherwise.

## References

[1] S. P. Ackert, Basics of Aircraft Maintenance Programs for Financiers, http://airc raftmonitor.com/uploads/1/5/9/9/15993320/basics\_of\_aircraft\_maintenance\_pro grams\_for\_financiers\_\_\_v1.pdf, (Accessed on September 28, 2017) (2010).

[2] IATA’’s Maintenance Cost Task Force, Airline Maintenance Cost Executive Commentary Edition 2019, https://www.iata.org/contentassets/bf8ca67c8bcd4 358b3d004b0d6d0916f/mctg-fy2018-report-public.pdf. (Accessed on September 11, 2020) (2019).

[3] N.J. Boere, Air Canada saves with aircraft maintenance scheduling, Interfaces 7 (3) (1977)1–13, https://doi.org/10.1287/inte.7.3.1.

[4] European Commission, Airline Maintenance Operations Implementation of an E2E Maintenance Service Architecture and Its Enablers, https://cordis.europa.eu/pr oiect/rcn/200486/factsheet/en. (Accessed on September 26. 2019) (2015). URI http://www.airmes-project.eu.

[5] Q. Deng, B.F. Santos, R. Curran, A practical dynamic programming based methodology for aircraft maintenance check scheduling optimization, Eur. J. Oper. Res. 281 (2020) 256–273, https://doi.org/10.1016/j.ejor.2019.08.025.

[6] T.A. Feo, J.F. Bard, Flight scheduling and maintenance base planning, Manag. Sci. 35 (12) (1989) 1415–1432, https://doi.org/10.1287/mnsc.35.12.1415

[7] J. L. Higle, A. E. C. Johnson, Flight Schedule Planning with Maintenance Considerations, http://citeseerx.ist.psu.edu/viewdoc/download? doi=10.1.1.542.3117.rep=rep1,type=pdf, (Accessed on March 5, 2021) (2005)

[8] L. Clarke, E. Johnson, G. Nemhauser, Z. Zhu, The aircraft rotation problem, Ann. Oper. Res. 69 (1997) 33–46, https://doi.org/10.1023/A:1018945415148.

[9] M. Bas¸dere, U. Bilge, Operational aircraft maintenance routing problem with remaining time consideration, Eur. J. Oper. Res. 235 (1) (2014) 315–328.

[10] Z. Liang, W.A. Chaovalitwongse, H.C. Huang, E.L. Johnson, On a new rotation-tour network model for aircraft maintenance routing problem, Transp. Sci. 45 (1) (2011) 109–120.

[11] C. Barnhart, N.L. Boland, L.W. Clarke, E.L. Johnson, G.L. Nemhauser, R.G. Shenoi, Flight string models for aircraft fleeting and routing, Transp. Sci. 32 (3) (1998) 208–220.

[12] W.E. Moudani, F. Mora-Camino, A dynamic approach for aircraft assignment and maintenance scheduling by airlines, J. Air Transp. Manag. 6 (4) (2000) 233–237, https://doi.org/10.1016/S0969-6997(00)00011-9.

[13] Z. Liang, W.A. Chaovalitwongse, A network-based model for the integrated weekly aircraft maintenance routing and fleet assignment problem. Transp. Sci. 47 (4) (2013) 493–507

[14] C. Sriram, A. Haghani, An optimization model for aircraft maintenance scheduling and re-assignment, Transp. Res, A 37 (1) (2003) 29–48

[15] S. Gabteni, M. Gronkvist, ¨ A hybrid column generation and constraint programming optimizer for the tail assignment problem, in: International Conference on Integration of Artificial Intelligence (AI) and Operations Research (OR) Techniques in Constraint Programming. 2006. https://doi.org/10.1007/11757375 9.

[16] N. Safaei, A.K. Jardine, Aircraft routing with generalized maintenance constraints, Omega 80 (2018)111–122. https://doi.org/10.1016/i.omega.2017.08.013.

[17] A.M. Cohn, C. Barnhart, Improving crew scheduling by incorporating key maintenance routing decisions, Oper. Res, 51 (3) (2003) 343–507, https://doi,org/ 10.1287/opre.51.3.387.14759.

[18] N. Papadakos, Integrated airline scheduling, Comput. Oper. Res. 36 (2009) 176–195, https://doi.org/10.1016/j.cor.2007.08.002

[19] J. Díaz-Ramírez, J.I.H.F. Trigos, Aircraft maintenance, routing, and crew scheduling planning for airlines with a single fleet and a single maintenance and crew base, Comput. Ind. Eng. 75 (2014) 68–78, https://doi.org/10.1016/j. cie 2014.05.027

[20] M.C. Diikstra. L.G. Kroon. M. Salomon. J.A.E.E.V. Nunen. L.N.V. Wassenhove Planning the size and organization of KLM’s aircraft maintenance personnel, Interfaces 24 (6) (1994) 47–58, https://doi.org/10.1287/inte.24.6.47.

[21] H.K. Alfares, Aircraft maintenance workforce scheduling – a case study, J. Qual. Maint. Eng. 5 (2) (1999) 78–89, https://doi.org/10.1108/13552519910271784.

[22] T.-H. Yang, S. Yan, H.-H. Chen, An airline maintenance manpower planning model with flexible strategies, J. Air Transp. Manag. 9 (2003) 233–239, https://doi.org 10.1016/S0969-6997(03)00013-9.

[23] D.E. Ighraywe, S.A. Oke, A non-zero integer non-linear programming model for maintenanceworkforce sizing, Int. J. Prod. Econ. 150 (2014) 204–214, https://doi org/10.1016/j.ijpe.2014.01.004.

[24] P.D. Bruecker, J.V. den Bergh, J. Beli¨en, E. Demeulemeester, A model enhancement heuristic for building robust aircraft maintenance personnel rosters with stochastic constraints, Eur. J. Oper. Res. 246 (2015) 661–673, https://doi.org/10.1016/j. eior,2015.05.008

[25] C.I. Permatasari, Yuniaristanto, W. Sutopo, M. Hisjam, Aircraft maintenance manpower shift planning with multiple aircraft maintenance licenced, in: IOP Conference Series: Materials Science and Engineering, 2019, https://doi.org 10.1088/1757-899X/495/1/012023, 495 012023.

[26] P. Gupta, M. Bazargan, R.N. McGrath, Simulation model for aircraft line maintenance planning, in: Annual Reliability and Maintainability Symposium, 2003.

[27] N. Papakostas, P. Papachatzakis, V. Xanthakis, D. Mourtzis, G. Chryssolouris, An approach to operational aircraft maintenance planning, Decis. Support. Syst. 48 (4) (2010) 604–612, https://doi.org/10.1016/j.dss.2009.11.010.

[28] J. Beli¨en, E. Demeulemeester, Philippe, D. Bruecker, J.V. den Bergh, B. Cardoen, Integrated staffing and scheduling for an aircraft line maintenance problem, Comp. Operat. Res. 40 (2013) 1023–1033, https://doi.org/10.1016/j.cor.2012.11.011.

[29] N. Safaei, D. Banjevic, A.K.S. Jardine, Workforce-constrained maintenance scheduling for military aircraft fleet: a case study, Ann. Oper. Res. 186 (2011) 295–316, https://doi.org/10.1007/s10479-011-0885-4.

[30] M. Witteman, Q. Deng, B.F. Santos, A bin packing approach to solve the aircraft maintenance task allocation problem, Eur. J. Operat. Res. 2021 (2021), https:/ doi.org/10.1016/i.eior,2021.01.027.

[31] N. Hölzel. C. Schröder. T. Schilling, V. Gollnick, A maintenance packaging and scheduling optimization method for future aircraft. in: Air Transport and Operations Symposium, 2012, https://doi.org/10.3233/978-1-61499-119-9-343

Oichen Deng is currently a PhD candidate at the Delft University of Technology, Section of Air Transport and Operations. His research focuses on optimizing aircraft maintenance check schedule and maintenance task execution at the fleet level. His work entails the development of a decision support system for aircraft maintenance planning optimization.

Bruno F Santos is an assistant professor at the Delft University of Technology, Faculty of Aerospace Engineering, in the group of Air Transport and Operations. His research focuses on airline operations, including optimizing aircraft availability and maintenance schedule, airline network and fleet planning, aircraft and crew scheduling, and disruptions management.

Wim J.C. Verhagen is a senior lecturer at RMIT University, and formerly an Assistant Professor of Maintenance Operations in the Air Transport and Operations Section at the Delft University of Technology. His research focuses on aircraft maintenance operations with specific attention to the development of knowledge-based maintenance systems, predictive algorithms, and optimization models to improve the efficiency of aircraft maintenance planning, execution, and support.
