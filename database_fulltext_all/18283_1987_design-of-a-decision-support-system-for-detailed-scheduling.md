---
otero_id: 18283
otero_key: "ZEPHDZY8"
title: "Design of a decision support system for detailed scheduling"
authors: "Nur Evin Özdemirel; Ahmet ЦSatir"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90003-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design of a Decision Support System for Detailed Scheduling

Nur Evin Özdemirel

Arizona State University, Department of Industrial and Management Systems Engineering, Tempe, Arizona 85287, U.S.A.

and

Ahmet Şatır

Concordia University, Department of Decision Sciences and M.I.S., Montreal, Quebec, H3G 1M8, Canada

Design of a decision support system (DSS) based on a simulation model of the detailed scheduling activities in a tractor manufacturing company is dealt with. The system analysis phase of the design process is overviewed briefly. The main decision points involved and the problems faced in the production planning and control subsystem are presented. Expectations from a DSS for detailed scheduling are discussed and performance measures are defined. The links between computer programs are shown. Utilization of the DSS designed for production planning and control oriented decision making is discussed using decision tables.

Keywords: Decision Support Systems, Detailed Scheduling, Simulation, Decision Tables.

## 1. Introduction

A decision support system (DSS) is considered to be an extensible system with intrinsic capability to support ad hoc data analysis and reduction as well as decision modelling activities. Although consensus has not been reached on the terminology used in the field of information systems, certain features can be attributed to a DSS as opposed to a management information system (MIS), though some authors $[4,11,13]$ do not differentiate between them but prefer to consider DSS within the context of MIS. It is our view that supporting system for structured problems are the subject of MIS, whereas DSS deals with ill structured problems emphasizing decision making rather than data processing $[9,10]$ . It is generally agreed that a DSS aids decision making at the strategic level where the problems are largely ill structured and incorporate factors from the external environment. Thus, the modelling process for a DSS incorporates the uncertainty factor compared to modelling in MIS, resulting in differences in the design process

![](/api/attachments/ZEPHDZY8/fulltext/images/ecb6ea1dbc06bd4a316fe45d0638fade1a7623dae6db10f815241b67837f663e.jpg)

Nur Evin Özdemirel is a Ph.D. student in the Department of Industrial and Management Systems Engineering at Arizona State University. She received her B.S. and M.S. degrees in industrial engineering from Middle East Technical University, Ankara, Turkey. Her research interest focuses on design of expert systems for production planning and control.

![](/api/attachments/ZEPHDZY8/fulltext/images/8ea5f2196692f02cca0cd02db51596f5ea27497ae3bac447193762a8ffcba6c5.jpg)  
ter, Institute of Science and Technology, England. His articles have appeared in, among others, International Journal of Production Research, Omega, Transportation Research and Journal of the Operational Research Society. His research interests include operations planning and control issues in flexible manufacturing and just-in-time production systems.

[1,3,7]. Various quantitative and qualitative models are used for a DSS [2,5] as well as simulation models [6,8,12].

A typical design methodology for a DSS involves the following steps: (i) analysis of the existing system activities and definition of the problem(s), (ii) analysis of information requirements, (iii) developing tasks and procedures to provide the information needed for decision making (designing a data base and related software), (iv) implementation, and (v) evaluation of the system. The first four stages of the design methodology are discussed here in the context of a detailed scheduling subsystem in a tractor manufacturing company. Although detailed scheduling is an operational decision making area with implications in the short term, the decision support system designed also incorporates decision making in the medium and long term that is associated with the consequences of the short term detailed scheduling decisions.

## 2. System Analysis

## 2.1 The Company

The DSS for detailed scheduling is designed for a tractor manufacturing company. Three models are manufactured at a capacity of 20,000 tractors per year. A tractor is made of approximately 2000 parts. One-third of these (corresponding to nearly half the value) are manufactured within the company, while the rest is subcontracted. Production processes are carried out in six departments: foundry, sheet metal workshop, machine shop, heat treatment, assembly and painting departments. The DSS is designed for the detailed scheduling decisions for the machine shop. In this workshop, operations are performed on turning, milling, and drilling machines in seven production lines; three of these are for line production and consist of special purpose machines, whereas the remaining four are of the batch production type, consisting of general purpose machines, mainly conventional. There are 196 machines in the shop for machining 675 parts.

2.2 Current Production Planning and Control Activities

The Production Planning and Control Department of the company makes and updates the following decisions throughout the year: annual production quantities, monthly production plans, parts to be subcontracted, overtime and/or extra shift working, order quantities and ordering frequency, and detailed scheduling. An information flow diagram of the current production planning and control activities as carried out in the company is illustrated in Fig. 1. In this figure, information originates from one activity and goes to another. The lower part of each block merely denotes the subsystem in which the activity is performed.

The difficulties encountered in production planning and control are the result of external and internal factors. The two external entities, TRAKMAK and (outside) firms, are both sources for uncertainty in production planning and control. The customer order servicing and the demand forecast on which other planning activities are based, is made by TRAKMAK, a service company which is a subsidiary of the same corporation. Lack of cooperation between the two companies and frequent updating of the demand forecast by TRAKMAK have a destabilization effect on production planning. The delays caused by vendors and subcontractors in delivering materials and parts are an external source of problems in production planning and materials management. Internally, production planning suffers from the poor decision made on subcontracting and detailed scheduling. These are the two areas in the company where decisions are based on experience and intuition, hence no structured decision models are employed.

The lack of timely feedback on the production status is an important deficiency in the information flow. The time lag in detecting the delays and the critical parts not only makes the schedule out-of-date, but also adversely affect the next period's schedule. This, a major concern for the production planning and control department, is dealt with here by predicting the delays and the critical parts through a simulation model, thus being able to remedy the situation.

![](/api/attachments/ZEPHDZY8/fulltext/images/f5f7057601d2dc433fa2110ef2a73bfbd811a3ffb00f4a0f4bd7c6f5d7c65d33.jpg)  
Fig. 1. Information flow diagram of production planning and control activities.

## 3. Information Requirements

The external factors are assumed to remain effective upon production planning in the short term. Among the internal factors open to revisions and redesign, detailed scheduling in the machine shop was chosen as the subject function for which a decision support system should be designed. The choice is appropriate because of the benefits that a well designed detailed scheduling system would bring, and also for the potential improvements in those subcontracting decisions which are closely related to scheduling decisions. A DSS based on a structured scheduling model will also improve the feedback obtained from the shop floor.

The following are the DSS requirements:

(i) sequencing and timing routines for the processing of batches of parts in various machines, based on priority rules and lot sizing techniques;

(ii) predicting the possible critical parts and the machines causing bottlenecks;

(iii) simulating the machine shop operations for overtime and/or extra shifts, subcontracting, and purchasing new machines; and

(iv) providing data and statistics by means of periodic reports comparing the schedule and the actual performance of the machine shop.

A simulation model was developed to support the detailed scheduling decisions. This paper focusses on the decision making aspects of detailed scheduling; programming details of the model will not be discussed. The performance measures for parts and machines are: work-in-process inventory levels in machine queues, total and average waiting times of batches in machines queues, throughput time of a batch, ratio of total batch waiting to throughput time, total and average waiting and throughput times, expected on hand inventory of parts at the end of the scheduling period, utilization rate of a machine, and average and total time elapsed for service in case of breakdowns.

The links between the computer programs used are shown in Fig. 2. The 'input generator' program, written in PL/I, provides the 'scheduling' program with updated data on parts and machines, initialized machine shop status and changes in operational parameters. The 'scheduling' program (written in Fortran IV) simulates the machine shop operations. The schedule obtained from this program is used as an input to the 'report generator' program. This program, written in PL/I,

![](/api/attachments/ZEPHDZY8/fulltext/images/7c6c7c7cba25ae051ddd1c0a3e6d7269078fcdf7f834be271cdbb74901a869a2.jpg)  
Fig. 2. Programs used in detailed scheduling.

provides a number of reports to be utilized in the decisions making process regarding various aspects of detailed scheduling. In cases of delay or any other discrepancy from the schedule as reported by the workshops, the 'crash' program is run to revise the schedule. This program, also written in PL/I, is efficient in the sense that only those parts and machines that are affected by the revision are reported.

![](/api/attachments/ZEPHDZY8/fulltext/images/bd007c6a884524275d0c43fb3641d647415a6c29f84ff78d719a54dea72dafb7.jpg)  
Fig. 3. Information flow in the detailed scheduling subsystem and interactions with other departments.

## 4. Features of the DSS

Within the context of the DSS designed, Fig. 3 illustrates the information flow in the scheduling subsystem and the interactions with other departments. The content of reports and the decision making areas which these reports support are given in Table 1. The time horizon of the reports is given as daily, monthly and quarterly. Daily reports provide feedback as to the implementation aspects of the schedule. They record what happened without providing any scheduling projections. The first two monthly reports summarize the performance on machine and batch basis, respectively. The other four monthly reports and three quarterly reports provide various detailed scheduling projections based on the immediate past performance (e.g. breakdown machinery, work in process status) and future predictions (e.g. demand for the final product, pattern of machinery breakdown). The planning horizon of these reports may seem long for an activity such as detailed scheduling with short term implications. However, some decisions made to correct the deficiencies observed and/or predicted may require actions with medium and long-term commitments, such as establishing an extra shift or buying new machinery. Thus, even longer-term reports may be required. The small final product range (three models with the majority of parts being common to all models) of the company studied results in (relatively) dedicated shop floor operations, thus increasing the reliability of the simulation results. In operational environments with a larger product range, a volatile demand and flexible machinery, the planning time horizon of the reports becomes shorter.

Table 1
Reports generated to support decision making

<table><tr><td rowspan="2">Report</td><td rowspan="2">Data Arrangement</td><td rowspan="2">Content of the Report</td><td colspan="2">Decision Making Area</td></tr><tr><td>Planning</td><td>Control</td></tr><tr><td>Daily ReportsSummary of daily work report</td><td>By machine</td><td>Part, batch &amp; operation numbers finished processingScheduled starting &amp; finishing times of operationsActual starting &amp; finishing times of operationsDelays with respect to schedule</td><td></td><td>Monitoring daily production to update schedule when necessary</td></tr><tr><td>Monthly ReportsSchedule on the basis of machines</td><td>By machine</td><td>Starting &amp; finishing times of operations performedUtilization rates of machinesTime elapsed for service in case of breakdownWaiting times of parts in machine queues</td><td>Machine loadingEvaluating alternative manpower strategiesMaintenance scheduling</td><td>Measuring capacity utilization</td></tr><tr><td>Schedule on the basis of parts</td><td>By part &amp; batch no.</td><td>Starting &amp; finishing times of operations of batches &amp; remaining process timesThroughput times of batchesTotal waiting times of batches spent in machine queues</td><td>Preparing job orders</td><td>Monitoring the work in processMeasuring throughput time performance</td></tr><tr><td>Expected waiting time of batch for each operation report</td><td>By part &amp; batch no.</td><td>Waiting times of batches in machine queues for each operation</td><td>Revising the schedule</td><td>Identifying machines and operations which cause delays</td></tr><tr><td>Expected work in process reportMonthly Reports (cont'd)</td><td>By machine type &amp; by week</td><td>Part, batch and operation numbers of batches waiting in machine queues at end of week &amp; remaining process time</td><td>Making overtime decisions</td><td>Monitoring machine queues, identifying machines causing bottlenecks</td></tr><tr><td>Expected inventory status report</td><td>By part number</td><td>Inventory on hand at beginning of monthBatch sizes of partsThroughput times of each batch &amp; increases in on-hand inventory</td><td>Making purchasing decisions</td><td>Inventory control</td></tr><tr><td>Expected throughput times &amp; waiting times report</td><td>By part &amp; batch no.</td><td>Throughput times &amp; waiting times of each batch in machine queuesRatio of waiting time to throughput timeTotal and average waiting times and throughput times of parts</td><td>Reviewing priority rule(s) and batch sizes</td><td>Measuring throughput time &amp; waiting time performance of parts</td></tr><tr><td>Quarterly Reports</td><td></td><td></td><td></td><td></td></tr><tr><td>Expected throughput time &amp; waiting time performance of parts report</td><td>By part no.</td><td>Number of batches of partsTotal &amp; average waiting time and throughput time per batchRatio of average waiting time to average throughput time</td><td>Making long term decisions as subcon-tracting, employing an extra shift or capacity expansion</td><td></td></tr><tr><td>Expected machine performance report</td><td>By machine type</td><td>Number of machinesPart numbers processed at the machine &amp; number of batchesWaiting time of each partTotal waiting time of parts &amp; average waiting time per partAverage utilization rates of machines</td><td>Making long term decisions as subcon-tracting, employing an extra shift or capacity expansion</td><td></td></tr><tr><td>Tractor demand forecast report</td><td>By tractor type</td><td>Demand forecast of TRAKMAK for each tractor type for next six months</td><td>Making long term decisions as subcon-tracting, employing an extra shift or capacity expansion</td><td></td></tr></table>

A decision support mechanism based on the reports generated is summarized in a series of tables. Six possible cases (deficiencies) that may occur in detailed scheduling are defined in terms of certain combinations of predictions obtained from the simulation model. The prediction of a deficiency is denoted by a 'Y' in Table 2, whereas an 'N' implies that particular deficiency has not been predicted. The list of predictions is not exhaustive and can easily be extended. The reports from which the deficiencies can be detected are indicated by an 'X' in Table 3. In most cases, a number of reports need to be studied to detect a particular deficiency. The decisions to be made to correct each deficiency are given in Table 4 with their respective priorities, the highest priority being '1'.

Two cases are briefly discussed in order to illustrate the use of the decisions tables. Case 1 occurs when the predicted throughput time performance is poor and the expected on-hand-inventory level is low for most of the parts, whereas waiting times in machine queues are within acceptable limits. There are four monthly and one quarterly report from which such a case can be detected. This implies the existence of (a few) machines that cause bottlenecks in production. The possible decisions that can be made to remedy such a situation may have short, medium, and long term implications. The first priority is given to working overtime at machines causing the bottleneck. The simulation model developed will provide the new performance measures in the short term taking into account this decision. Decisions with medium and long term implications will be considered if the predicted performance of the

Table 2
Deficiencies that may occur in detailed scheduling

<table><tr><td rowspan="2">Prediction of the simulation model</td><td colspan="6">Case</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Throughput time performance is poor and expected on hand inventory level is low for most of the parts.</td><td>Y</td><td>Y</td><td></td><td></td><td></td><td>Y</td></tr><tr><td>Throughput time performance is poor and expected on hand inventory level is low for some of the parts.</td><td></td><td></td><td>Y</td><td>Y</td><td></td><td></td></tr><tr><td>Waiting time in machine queues is long for most of the parts.</td><td>N</td><td>Y</td><td></td><td></td><td></td><td></td></tr><tr><td>Waiting time in machine queues is long for some of the parts.</td><td></td><td></td><td>N</td><td>Y</td><td></td><td>Y</td></tr><tr><td>Work in process inventory in some machine queues is large and waiting time of parts for processing is long.</td><td></td><td></td><td></td><td></td><td>Y</td><td></td></tr><tr><td>Machine utilization rates are low.</td><td></td><td></td><td></td><td></td><td></td><td>Y</td></tr></table>

Table 3
Reports used to detect deficiencies

<table><tr><td rowspan="2">Planning horizon of the reports</td><td rowspan="2">Reports generated</td><td colspan="6">Case</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td rowspan="6">Monthly</td><td>Schedule on the basis of machines</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>Schedule on the basis of parts</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Expected waiting time of each batch for each operation report</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Expected work in process report</td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>Expected inventory status report</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Expected throughput times and waiting times report</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td rowspan="2">Quarterly</td><td>Expected throughput time and waiting time performance of parts report</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Expected machine performance report</td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr></table>

shop floor does not significantly improve. The next decision is then to subcontract some of the parts. Working an extra shift is the last decision that can be taken with the lowest priority. The expected performance of the shop floor in case of the execution of each decision will again be simulated and various reports on performance measures will be generated. The procedure repeats itself until an acceptable performance is achieved. The rationale behind the particular ranking of decisions for this case is the preference made in overcoming the problem by taking measures having short term implications in the anticipation that the deficiency is a temporary one, probably caused by the breakdown of a machine(s).

The deficiency in Case 6 not only involves the prediction of poor throughput time, low on hand inventory levels, and long waiting times in machine queues, but also the machine utilization rates are low. A contradiction observed in this situation is the concurrent occurrence of long waiting times in machine queues and low machine utilization rates. There are basically two actions that can be taken to tackle the problem. The best reviews the priority rule used for detailed scheduling. Changing the lot sizes is a second alternative if the new priority rule(s) used cannot overcome the predicted deficiency. The rationale behind the ranking of decisions for this case is the generally accepted supposition in the theory and the practice of detailed scheduling that correlates the operational performance of a machine shop to the priority rule rather than the lot sizing.

<table><tr><td rowspan="2">Decision</td><td colspan="6">Case</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Review priority rule</td><td></td><td>1</td><td></td><td></td><td></td><td>1</td></tr><tr><td>Review batch sizes</td><td></td><td>2</td><td>1</td><td>2</td><td></td><td>2</td></tr><tr><td>Make some parts critical by assigning a higher priority</td><td></td><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td>Work overtime at some of the machines</td><td>1</td><td>3</td><td>2</td><td>3</td><td>1</td><td></td></tr><tr><td>Subcontract some parts</td><td>2</td><td>4</td><td>3</td><td></td><td></td><td></td></tr><tr><td>Subcontract some processes</td><td></td><td></td><td></td><td></td><td>2</td><td></td></tr><tr><td>Work extra shift</td><td>3</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>Purchase new machines</td><td></td><td></td><td></td><td></td><td>3</td><td></td></tr></table>

## 5. Concluding Remarks

The DSS designed for detailed scheduling activities of a tractor manufacturing company was discussed with emphasis on the procedural and implementation aspects with medium and long term implications on shop flor operations. The decision tables should be regarded as tools reducing the level of uncertainty in the process of decision making. However, there will still be a degree of uncertainty to consider. A sound feedback on the actual performance of the shop floor based on the 'Summary of daily work report', and thus the use of the crash program, is a prerequisite for the success of the DSS.

Recent years have witnessed a dramatic development in computer and communication technology. The impact in the manufacturing sector has been substantial. Coupled with computer aided design (CAD) and computer aided manufacturing (CAM), the flexible manufacturing systems (FMS) are capable of performing multiple functions using flexible, programmable multi-purpose equipment and robots. These developments are now merging towards the fully automated factory. Computer integrated manufacturing (CIM) is the product of this merger, a combination of hardware, software, knowledge based expert systems and communications technology to provide on-line variable program automation.

The traditional mode of manufacturing and the associated operations management techniques have to be modified extensively in order to remain competitive in highly volatile international markets. Dss play an important role in this transfer from a traditional manufacturing to a CIM environment that is largely supported by knowledge based expert systems. Our DSS concentrated only on the preliminary aspects of the detailed scheduling dimension of such a transfer for a tractor manufacturing company. The approach followed can also be used for other manufacturing environments with relevant modifications depending on the details of their operating systems.

## Acknowledgements

The authors wish to thank the staff of the Production Planning and Control Department of the Company, which prefers to remain anonymous, for facilitating the analysis of their system and providing the operational data. They would also like to thank the referees and the Editor who gave some excellent suggestions for revising earlier drafts of this paper.

## References

[1] G.N. Arnovick and L.G. Gee: Design and Evaluation of Information Systems. Information Processing and Management, 14, 6 (1978), 369–380.

[2] D. Avramovich, T.M. Cook, G.D. Langston and F. Sutherland: A Decision Support System for Fleet Management: A Linear Programming Approach. Interfaces, 12, 3 (1982), 1–9.

[3] R.B. Cooper and E.B. Swanson: Management Information Requirements Assessment: The State of the Art. ACM SIGBDP Data Base, 10, 6 (1979), 5–11.

[4] G.B. Davis: Management Information Systems - A Fifteen Year Perspective. ACM SIGBDP Data Base, 11, 3 (1980), 10-11.

[5] J. Hansen, L.E. Heitger and L. McKell: Computer Aided Modelling of DSS. Journal of Operational Research Society, 29, 8 (1978), 789–802.

[6] S.K. Jain: A Simulation Based Scheduling and Management Information System for a Machine Shop. Interfaces, 6, 1 (1975), 81–96.

[7] P.G.W. Keen: Adaptive Design for Decisions Support Systems. ACM SIGBDP Data Base, 12, 1–2 (1980), 15–25.

[8] G.R. Martins: Better Simulation Models for Decisions Support. ACM SIGBDP Data Base, 12, 1-2 (1980), 47-54.

[9] L.B. Methlie: Data Management for DSS. ACM SIGBDP Data Base, 12, 1–2 (1980), 41–45.

[10] J.H. Moore and M.G. Chang: Design of Decisions Support Systems. ACM SIGBDP Data Base, 12, 1–2 (1980), 8–13.

[11] T. Naylor: DSS or whatever Happened to MIS? Interfaces, 12, 4 (1982), 92–94.

[12] D.S. Surh, G.T. Mackulak and M.P. Deisenroth: An Application of Simulation Techniques to Information Systems Analysis. Computers and Industrial Engineering, 6, 1 (1982), 63–72.

[13] A. Vazsonyi: DSS, Computer Literacy and Electronic Models. Interfaces, 12, 1 (1982), 74–78.
