---
otero_id: 21165
otero_key: "GSZ3CRZF"
title: "A knowledge-based decision support system for the management of parts and tools in FMS"
authors: "Mustafa Özbayrak; Robert Bell"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00128-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A knowledge-based decision support system for the management of parts and tools in FMS

Mustafa O<sup>¨</sup> zbayrak <sup>a,</sup>\*, Robert Bell <sup>b</sup>

<sup>a</sup>Department of Systems Engineering, Brunel University, Uxbridge, Middlesex, UB8 3PH, UK <sup>b</sup>Department of Manufacturing Engineering, Loughborough University, Loughborough, Leics, LE11 3TU, UK

Accepted 28 May 2002

## Abstract

Flexible manufacturing systems (FMS) are very complex systems with large part, tool, and information flows. The aim of this work is to develop a knowledge-based decision support system (KBDSS) for short-term scheduling in FMS strongly influenced by the tool management concept to provide a significant operational control tool for a wide range of machining cells, where a high level of flexibility is demanded, with benefits of more efficient cell utilization, greater tool flow control, and a dependable way of rapidly adjusting short-term production requirements. Development of a knowledge-based system to support the decision making process is justified by the inability of decision makers to diagnose efficiently many of the malfunctions that arise at machine, cell, and entire system levels during manufacturing. In this context, this paper proposes three knowledge-based models to ease the decision making process: an expert production scheduling system, a knowledge-based tool management decision support systems, and a tool management fault diagnosis system. The entire system has been created in a hierarchical manner and comprises more than 400 rules. The expert system (ES) was implemented in a commercial expert system shell, Knowledge Engineering System (KES) Production System (PS). <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: FMS; DSS; Tool management; Part scheduling; Systems diagnosis; Knowledge-based systems

## 1. Introduction

Increasing global competition has made many manufacturing companies recognize that competitive manufacturing in terms of low cost and high quality is crucial for success. In an attempt to improve their competitive edge, manufacturers have for some time been turning to flexible manufacturing systems (FMS). Management of tools and parts is recognized as a critical issue in the operation of FMS. Although new technologies, such as sophisticated machining facilities, factory-wide intelligent handling mechanisms, and hierarchical cell control systems, have increased the flexibility and provided system users with a significant infrastructure, many systems have failed to take advantage because of increasing complexity in operation and control of machining cells.

Part and tool flows, two major dynamic entities, are the key factors for managing successful manufacturing. Stecke and Kim [19] formulated the tool allocation problem as a nonlinear programming model. Positioning of tools in the magazine and the magazine capacity were considered as primary constraints. Balancing the assigned machine processing times and maximising the tool density of each magazine with the tool allocation are the objectives of the formulation. Coleman et al. [7] studied tool management and job allocation in flexible machining cells using work-oriented strategies. This spreadsheetbased model presents and investigates strategies for tool management and job allocation in a demanddriven system. The paper’s major concern is to measure the effects of tool management strategies on machining cells under the influence of job allocation rules. Coleman et al. [8] developed a similar model of tool management and job allocation in machining cells using tool-oriented strategies. This paper presents a tool-oriented approach to provide further tooling economy. The model employs a clustering algorithm to identify part and tool groups. These clustered groups are allocated to a particular machining cell configuration with respect to the additional constraints of balancing the overall work load per machine and managing tool kit exchange under limited tool magazine capacity.

Amoaka-Gyampah et al. [3] compared tool management strategies and part selection rules. They described four tool management strategies and three part selection rules, two concentrating on tooling and the rest on earliest due date (EDD). They also developed a simulation model and used five performance measures. Although this paper primarily deals with tool management in FMS, all of the performance measures used focus on the part and general system spectrum, neglecting major tool management performance criteria such as tool requirements and tool inventory. Rahimifard and Newman [16] developed a multischeduler system that schedules the jobs, fixtures, and tools. This simulation-based work uses the traditional part and tool scheduling strategies along with careful planning and scheduling of fixtures within a highly automated flexible cell. Three planning strategies are considered, namely workpiece-dominated planning strategy, tooldominated planning strategy, and fixture-dominated planning strategy when the schedule of the three concerned dynamic entities. The paper argues that the simultaneous assignment planning of these three dynamic entities has great advantages in terms of cell performance and cell control and presents the several simulation results and performance measures.

Acaccia et al. [1] developed an expert simulation of tool distribution for factory automation and discussed tooling integration in flexible manufacturing for a short-term manufacturing period. Tool dispatching is considered, in an integrated environment, to be delivering the required tools at the right time to the right station while keeping plant flexibility and other performance criteria of the system. Acaccia et al. [2] proposed another expert system (ES) approach to provide an expert scheduling system for tool stock to satisfy long-term production requirements. An expert simulation system algorithm has been developed to satisfy production requirements as well as keep the tool stock level reasonably low. An extensive and more detailed literature survey of TMS can be found in Ref. [13]. There are some researches that offer decision support solutions to part scheduling, fault diagnosis, or system design in flexible manufacturing systems [6,10,11,15,17,18]. However, none of the papers found in the literature deals with the decision support system (DSS) for the integrated management of tool and part flows in FMS. There is a shortage of research in DSS for integrated tool and part flow management as well as cell control and tool management system operation diagnosis.

In this paper, we aim to apply a knowledge-based decision support system (KBDSS) to short-term scheduling in FMS, strongly influenced by tool management concept to provide a significant operational control tool for a wide range of machining cells, where a high level flexibility is demanded, with benefits of more efficient cell utilization, greater tool flow control and a dependable way of rapidly adjusting short-term production requirements. The development of a knowledge-based system to support the decision making process was justified by the inability of decision makers to efficiently diagnose many malfunctions, which arose at machine, cell, and entire system levels during manufacturing operations. In this context, this paper proposes three integrated knowledge-based models to ease the decision making process by providing an expert aid both at design and at operational levels. These are the knowledge-based production scheduling, the knowledge-based tool management strategy selection (KBTMSS) system, and the knowledge-based manufacturing and tool management fault diagnosis system.

## 2. A need for a knowledge-based decision support system

Many systems employ different software solutions for manufacturing problems and then try to integrate them through a user interface. This approach is the case for part and tool scheduling in many industrial organizations and often fails because of lack of compatibility between the components of the solution provided. This is mainly because part scheduling is seen as a major issue and tool management is often treated as secondary on the assumption that tools are always available on the processing machine at the required time and quantity. This misconception leads to underestimation of the severity of the problem and often causes low equipment utilization, poor performance and even sometimes total loss of confidence in the system. However, timely availability of tools at the required place, time, and quantity is a major concern of part scheduling, especially in automated systems, and without incorporating a tooling concept, part scheduling can suffer from improper functioning.

When poor performance is realized or malfunction is detected, it is the responsibility of the operations manager to recognize the symptoms and analyze the symptomatic information to find the source of the problem.

Because the processes in manufacturing organizations are very complex, involving many interacting parameters, a systematic search approach with a proper feedback system is vital for detecting the problem and providing the proper solution as soon as possible. The expert may not be available immediately to attend to the problem, or the organization may not even have a competent expert for every problem that may arise [15]. Under pressure of time and loss of production, a quick response can play a vital role in bringing the system back to normal. This calls for an intelligent diagnosis system. Diagnosis is defined as systematic identification of malfunction by means of the symptoms.

Expert systems can use human-like reasoning to diagnose problems and provide remedies. Their ability to manipulate domain-specific knowledge and how to use knowledge to create a reasoning tree, tracing reasoning backward as well as forward, needing only a minor change in the knowledge base to adapt to new situations, make expert systems a good candidate to combine with a DSS to create a complete system.

The foundation of this paper is based on sound and effective DSS theories and practices. The use of knowledge-based modelling provides the appropriate framework for the management of parts and tools in an automated manufacturing system. Although there exists a variety of part/tool management papers [5,7,8,16,21] to the best of our knowledge, this is the first study of its kind in this area. KBDSS, as it pertains to this paper, attempts to coordinate parts and tool scheduling activities. The DSS consists of three nested knowledge-based systems and aims to

1. Schedule the jobs according to the highest priority ranking,

2. Provide a basis for selecting the best tool issue strategy for a particular hardware configuration on the basis of user-selected decision criteria, and

3. Provide an expert aid to diagnose and remedy possible tooling-originated manufacturing problems both at the design and at the operational levels.

Part and tool management concerns are coordinated in advance of any actual manufacturing. The management of parts and tools also considers other operational issues, which will be outlined in subsequent sections of this paper. The methodology used here may also be used for any other automated manufacturing configuration provided that proper minor modifications are made for each particular situation.

This paper contributes to the DSS research in two ways. Firstly, effective part and tool management requires accurate functional specifications of user requirements in all stages of the operations. There are formal methods for carrying out such functional specifications but they are system specific, time consuming and often difficult to implement, especially in random environments. Thus, the complexity and the random nature of the problem make it an ideal candidate for a DSS development effort. Secondly, the dynamic nature and the complexity of tooling and synchronisation with parts in automated systems require particular attention in order to guarantee streamlined manufacturing. Yet again, different hardware organizations require different tooling strategy implementations even in the same manufacturing period depending on the workload and tool traffic to gain an advantage from the hardware of the organization. This is a very complex task and requires an online information feedback to alter the tooling strategy when necessary. This need makes a DSS the only alternative to solve the problem efficiently. In addition to problem complexity, semistructured or ill-structured data and transient output, which occur often in any manufacturing system, require a well-structured decision support mechanism to ease the decision making process. The KBDSS provides comprehensive support at all stages through interactive feedback with a high degree of control. Three nested knowledgebased systems offer a complete decision support system by scheduling the jobs under a tooling constrain, by calculating tool requirements and the tool inventory level for each of the issue strategies practiced, by selecting the most suitable tooling strategy for a particular cell configuration, and finally by providing an expert aid to diagnose and remedy possible malfunctions at workstation, cell, and entire manufacturing system levels at design as well as operational levels. The knowledge-based modules are integrated through an ORACLE relational database management system (RDBMS) to retrieve from the various modules and to provide the necessary data and knowledge.

## 3. Part and tool flow problems in FMS

Part scheduling is one of the most important factors that affect cell performance. Because all the jobs use the same finite (limited) resources such as machines, materials, tools, time, etc., the competition for resources makes part flow a vital function for successful manufacturing [21]. Part flow function has been considered with an aim to examine the effects of part flow on tool flow in FMS. No attempt is made to develop optimal rules but part flow is incorporated to maximise the efficiency of the KBDSS.

As pointed out in Refs, [3,5,9,11], tooling and tool magazine capacity have a significant impact and are the major constraints for part batching and scheduling.

## 3.1. Part scheduling under a tooling constraint

As indicated by several researchers [3,5,21], the part allocation, machine balancing, production ratio, and tool allocation problems are closely related. Unless they are considered simultaneously, the solution proposed would be insufficient. Part scheduling should satisfy timely assignment of manufacturing operations as well as determine what set of orders should be ready for processing at a particular station at a particular time, deciding on the sequence in which they will be run and calculating the resulting start and finish times for each operation. On the other hand, tool management aims at allocating the right tools for the right job at the right place, at the right time, and at the right quantity. Because manufacturing operations require a large number of tools on different work centres, it is vital to allocate the limited number of tools to the work centres with limited capacity magazines.

Some of the criteria considered by the different scheduling programs may conflict and cause substantial manufacturing chaos. It is thus necessary to consider solution procedures for the part scheduling and tool allocation problems simultaneously. However, it is often very difficult to determine the best part and tool schedule combination relative to all relevant criteria.

In this study, four scheduling rules, namely shortest processing time (SPT), longest processing time (LPT), earliest due date (EDD), and first come first served (FCFS), are used to schedule the parts of a multicell FMS. Three different workpiece-oriented tooling strategies, namely full kitting (FK), differential kitting (DK), and single tools kitting (STK), two tool-oriented tool issue strategies that are full clustering (FC) and differential clustering (DC) strategies and one hybrid strategy that is a combination of workpiece-oriented and tool-oriented approaches, are used to allocate the tools to the limited capacity work centres (Fig. 1). Tool magazine capacity (in this study, 20 and 40 pockets), pallet capacity (10 each, 20 each and 40 each), and the automated guided vehicle (AGV) (one-vehicle and two-vehicle systems) are the finite resources in the system. A separate dedicated tool transport system is also in use to carry tools between machines and cellbased tool stores.

## 3.2. Tool management—an overview

The essential role of tool management is the timely scheduling of tools to satisfy a short-term to mediumterm manufacturing task. The heart of a typical tool

![](/api/attachments/GSZ3CRZF/fulltext/images/6c11c5e965115fa2cce05766ea270dbdc7ba88afc1ef74a094e4f2dfaebc7648.jpg)  
Fig. 1. Tool management and issue strategies.

management system is the tool list, which is derived from the machining schedule, the starting point and controlling factor of all the cells’ activities and events. The machining list, at the highest level, consists of order numbers, due dates, priorities and required quantities. The machining list may be subdivided into partial orders (individual workpieces) and stored in the form of order waiting queues or work schedules. These schedules exist for every machine in the cell and specify the sequence of operations for a particular workpiece and the required tool sequence (the tool list). The tool lists not only determine the schedules for tool transfer and tool changing but also the gross tool requirement. A net tool requirement is established by examining the tool store contents for the appropriate tools, which have adequate residual tool life, and by introducing new tools where necessary to service the machining schedule. The generated tooling requirement is placed in the tool room, which is responsible for supplying the required tools. The organization of the tool room to manage these required tools depends upon the facilities supplied and the manpower used. As orders are being processed, the currently completed number of workpieces is recorded and updated. The consequences of these completed workpieces on the lists is an indication of which tools are no longer required or can no longer be used due to reaching their life limit. This in turn activates the tool transfer schedule and new tools may be introduced into the system.

## 4. A KBDSS for the management of part and tool flows

Knowledge-based systems collect the small fragments of human know-how into a knowledge base, which is then used to reason through a problem. A different problem, within the domain of the knowledge base, can be solved using the same program without reprogramming. The ability of these systems to explain the reasoning process through back-traces and to handle levels of confidence and uncertainty provides an additional feature that conventional programming tools do not have.

This KBDSS is aimed at providing a powerful design and operation aid for both parts and tools management. It acts as an aid to cell management, which may either work alongside operating cell-oriented part and tool management system or be used to assess a part/tool management solution within a cell or a total factory environment.

The main components of KBDSS are a knowledgebased part scheduling system, a knowledge-based tool management strategy selection system, and a knowledge-based manufacturing and TMS diagnosis system. All modules are integrated both with each other and through a centralised relational database management system. Both part scheduling and strategy selection modules are fed by tool requirements planning (TRP) module, which is created in a spreadsheet environment. Fig. 2 illustrates the structure of the proposed intelligent DSS for part and tool flow management systems.

The KBDSS is a decision tree-based system, which uses the shallow knowledge of the cell operations manager and shop floor staff in the form of IF. . .THEN THEN rules. Fig. 3 shows the input/output relationships between the KBDSS modules and the other elements of the tool and part flow management. KBDSS starts with job scheduling. The batch size decision is based on a simple IF. . .THEN rule set that automatically determines the batch size that the machine can afford and still contain all the necessary tools. Because tool requirements are mainly determined by the adopted tool issue strategy, the scheduling module only considers the basic tool requirements, which are determined by process planning, in order to compare the number of tools required with machine magazine capacity and transporter capacity. The part scheduling algorithm sequences and schedules the jobs according to the user-preferred scheduling rule. The inputs of this module are part, tool, machine, and pallet data and user-selected rules placed into manufacturing database. The outputs of this module, which are job list for cells and manufacturing workstations, are the main input to TRP. TRP calculates tool requirements and all other tooling-related performance measures and is the subject of a different paper [14].

The second module in the KBDSS is the KBTMSS. It is not always possible to find a tool management strategy that perfectly suits the available hardware and operational environment. Therefore, it is important to find a strategy that makes it easier to solve the problem as well as satisfy manufacturing requirements. This module’s main inputs are TRP and manufacturing database as well as user-selected decision criteria. The details of the module are presented in Section 4.3.

![](/api/attachments/GSZ3CRZF/fulltext/images/f90bf4d610c396ed8c90fad1f36fe142de5872ffb8aed2e1f283004f3b5586d3.jpg)  
Fig. 2. Structure of knowledge-based decision support system for the management of parts and tools in FMS.

![](/api/attachments/GSZ3CRZF/fulltext/images/2af85c2276c0e60b2cb10bd94dbc43caacb5f885f3dd39fc36d68bd187227e3c.jpg)  
Fig. 3. Logical and input/output relationships of KBDSS.

The last KBDSS module created is the manufacturing and TMS diagnosis system, which assesses the performance of TMS and provides feedback during the design and operational stages on both manufacturing and organizational problems. The module requires inputs from three other modules, namely the scheduling system, TRP, and the strategy selection system (Fig. 3). Because the system is dynamic, these inputs are updated through the relational database system. The module supports four main hardware and operational problem groups: manufacturing cell problems, manufacturing workstation problems, tool store problems, and tooling problems. The most likely problem areas with supporting questions and possible solutions are stored in the knowledge base. To be able to make a decision, the rules embedded in the DSS are fired and solutions may be selected from among the output provided through the relational database by the input modules. The details of this module are presented in Section 4.3.1.

## 4.1. Part release and expert part batching

Only static part launching, where all the parts to be processed must be available when they are required, is considered. Pallets are assumed to be ready and loaded with components before transportation to the machines. No extra parts are permitted to leave or reenter during manufacture.

This type of part release mechanism is most evident in highly automated unmanned systems for short-term production and it is intended to meet the requirements of this type of system [7].

Because the scheduling mechanism is a separate module, which feeds to tool requirements planning, any external part release mechanism may also be accepted to generate the machining lists.

Part batching is an important factor in an FMS. All the jobs, which will be accomplished, use the same finite resources such as machines, materials, tools, time, labour, etc. Competition for resources makes batching a vital function for manufacturing and needs particular attention [20].

There are two main system design constraints to decide the batch size. These are magazine capacity and transporter capacity [7,8].

Especially large batches need a great number of tools on the machine. Small magazine capacity presents a serious problem to deciding the batch size. Small batches frequently result in a very large number of tool changes and inefficient tool life utilization as well as longer throughput time. Larger batches face the magazine capacity as well as transporter capacity constraints.

In case of practicing a kitting strategy in particular, the transporter capacity creates a major problem. This constraint may be overcome by running the transporter frequently but then the lead time and machine idle time increase [19]. Ideally, it is thought that the transporter should transfer all the necessary tools needed by the job and should bring the returned tools back at one visit. However, frequent transporter visit is accepted and is not counted as a constraint in deciding the batch size.

A number of rules are applied consistently throughout the batching process. The data required as input are a sequence of job assigned to each machine for every accepted manufacturing period, a list of alternative machines that have the capability of processing the jobs, the status of all machines (available or idle), processing times, available tool lives, number of tool requirements for each batch, magazine capacity, and tool transporter capacity.

The decision mechanism is built up by the following rules:

The first rule determines the number of transfer batches or jobs required from each process batch of a particular part type. The process batches are the total manufacturing requirement of each part type for the given manufacturing period. The rule is

IF process batch size is less than or equal to available pallet capacity

THEN keep process batch size as it is

ELSE split the process batch into transfer batches until available pallets satisfy the constraint.

The second rule checks the already automatically calculated tool requirements and the magazine capacity or empty pockets. The rule is

IF tool requirement is less than or equal to available magazine pocket

THEN release the job to the available machine ELSE reduce the batch size until its tool requirement matches the available magazine pockets THEN release the job to the available machine.

The routine decided by the above rules does not seek to optimize. Instead, it seeks the batch size that satisfies the necessary constraints. This does not necessarily mean that the required tools are the optimum tool quantity but rather that the magazine capacity is large enough to hold all the necessary tools.

## 4.2. Knowledge-based scheduling system

In the algorithm presented below, once the sequencing rule is selected, all the jobs are scheduled to the available machines according to their respective technological capability. The manufacturing conditions considered in the rule-based scheduling system are listed below:

1. A job is a visit to a machine (an operation)

2. A job has suboperations that require a tool set

3. A job returns to the job list on completion of suboperations

4. Operation precedence must be preserved

5. A job is a transfer batch quantity

6. A number of jobs of the same type may exist in the list due to the process batch quantity

7. The job is picked in relation to the sequencing rule adopted

8. The number of times a job is released depends on item 7, required quantity, pallet capacity and pallet quantity

9. Jobs are specified in pallet quantities

10. A job priority of 0 is greater than job priority of 1

Because expert system logic may process backward as well as forward, Fig. 4 depicts the backward chaining logic to release a job.

First, a job is found that has the preferred entering hardware conditions. The job is then given an operation consideration factor (OCF) of 1. Because each batch is considered as a job, the pallets are checked. If pallet capacity is enough to allow the transfer of the job to the system, then the job is transferred. If the pallet capacity is not enough, then the second highest priority job is assigned and a new OCF of 1 is given.

After that, the earliest start time of the first available pallet is checked and is assigned as a job start time. At the same time, the machine available time is checked and compared with the pallet start time. If the machine available time is not matched with the job start time, another job is released. Job and pallet available times are modified and should be less than or equal to machine available time, otherwise another job is selected.

The new pallet’s earliest start time is checked and the clock is updated until the pallets have returned one assignment. If the first pallet available time is much longer than the clock start time, then a delay time is calculated. If the delay time is too long, this job is abandoned and another job is sought, which has an OCF of 0. This situation is repeated until there are no jobs that have an OCF equal to 0. The related rules in the knowledge base are given Appendix A.

The rule-based system developed in this work is based on user-preferred sequencing rules. Before jobs are released, the expert system asks the user which one of the four sequencing rules is preferred. Then, jobs are released to the machines or machine groups, which form the manufacturing cell following the logic described in the previous paragraph.

The rule base outlined above plays a critical role in the expert scheduling system. It is implemented using the Knowledge Engineering System (KES) production system (PS) shell [12].

## 4.2.1. Part scheduling algorithm

The part scheduling algorithm is presented to show the background of the rule-based scheduling module built. The production scheduler first sequences the jobs according to the preferred scheduling rule. Then, there is a search for the first available machine from all machines capable of doing all the necessary processing. Then, the first available job is released to the machine based on the logic presented above. This procedure is repeated until all the jobs have been scheduled. The logic of the algorithm is depicted in Fig. 4 and is described below. The notation used is:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
i tool index from 1 to T tool types
j job index from 1 to J jobs
o operations index from 1 to O
m machine index from 1 to M machines
p index set of pallets, p=1,..., P
 $T_{m}$  available time for machine m,  $m\in M$ $X_{ojpm}$  =1 if operation o of job j of pallet p assigned machine m
=0 otherwise
 $Z_{ojp}$  =1 if operation o of job j of pallet p is assigned
=0 otherwise
</div>

![](/api/attachments/GSZ3CRZF/fulltext/images/632925d1a5287288c752096972e2d01337b77ea91da8f2ac5a5b5e90417f3acd.jpg)  
DB = Database, O.C.F. = Operations Consideration Factor  
Fig. 4. Knowledge-based logic of scheduling.

Step 0: Initialise all the variables, i.e., set current time $t = 0$ and set jobs $J _ { j } { = } 0$ . If operation belongs to first job’s predecessor, job is job none.

Step 1: Priority sequencing: Sequence all the jobs according to priority rule practiced, i.e., EDD, SPT, LPT, and FCFS.

Step 2: Find the first available machine $m ,$ which satisfies the following conditions: $T _ { m } { = } \operatorname* { m i n } T _ { m }$ and $\begin{array} { r } { T _ { m } = \sum _ { j \in J } \sum _ { o \in O } \sum _ { m \in M } P _ { j o m } } \end{array}$

Step 3: Try pallets from the list formed in Step 1. Send the first pallet to the first available machine, which must satisfy the following conditions: $X _ { o j p m } = 1$ and $Z _ { o j p } = 1$ . If Step 3 is successful, go to Step 5, else go to Step 4.

Step 4: If no more operations require machine $m ,$ then remove machine m from M. Go to Step 2 until M is empty (all pallets have been assigned), else delete machine m temporarily until next sequence has been made and go to Step 2.

Step 5: Update job priority, pallet processing time, machine available time, and process factor, delete operations of the pallet from the waiting list, and go to Step 6.

Step 6: If all pallets finish operations, then stop, else go to Step 2.

Pallet p of job j’s tool content i is identical to pallet p of job $j ^ { \circ } \mathbf { s }$ tool content iV. Then, the pallet that requires fewer tools goes first. If all tool types are exactly the same, jobs are selected randomly amongst the identical tools used. This rule has been created by using the principles of internal scheduling, which is based on clustering algorithm.

## 4.3. KBTMSS system

The KBTMSS is designed to select the most convenient tool management (TM) as well as tool issue strategies for the related hardware configuration. The module is supported by both the TRP module and the manufacturing database.

The expert system is logic based and stores the entire knowledge base in the form of a disk file that has no size limitation. The rules in the knowledge base are framed from database clauses, containing the necessary conditional descriptions. The inference engine makes a goal-directed search and it has been developed such as to be capable of accepting further inclusion of rules and conditions in the knowledge base.

## 4.3.1. Structure of strategy selection

The strategy selector in the expert system considers the three main tool management approaches and then the six tool issue strategies, each of which is a substrategy of one of the three higher level strategies. Fig. 1 shows the strategy relations. The manufacturing database consists of a number of submodules: job database, station database, pallet database, strategy database and cluster database. The data used in the expert system are based on experimentally determined output, which is produced by using the TRP module and transferred through the manufacturing database. The database depending on the TRP module can be updated and modified throughout the manufacturing period.

The expert system is further capable of including the following user-selected single or multiple operational goals: minimum tool requirement, minimum tool flow, minimum tool inventory, minimum production throughput time, and maximum machine utilization.

The module could be updated, modified or replaced as a whole by a more suitable and compatible knowledge base as and when required.

Alternative choices and recommendations are presented to the user during consultation with the system. During consultation, the user is asked for details of the hardware facilities such as magazine capacity, transportation mechanism, scheduling rules applied, etc. The system then follows predetermined steps to reach a conclusion for the hardware configuration and the control mechanism applied on the shop floor. The consultation flow indicates that the system assumes that the user has a certain degree of tool management knowledge and experience in order to choose or select a preferred value or answer for the questions asked when prompted with a range of recommended values. If the user wants the expert system to choose a specific TM or tool issue strategy due to his/her own particular reason(s), the expert system can be forced to chose the desired strategy by putting the specific default values in the attributes section. This can also prevent the expert system from asking many questions before reaching a conclusion.

## 4.3.2. Decision criteria

Because the expectation from a system is different from organization to organization, the criteria for selection vary. KBTMSS can provide decision aid at a number of stages such as determining overall system approach, the best generic or specific tool management strategy, and expert advice on specific tool management problems or intelligent assistance during the decision process. The module also gives detailed reasoning about the decision. The user is associated to use his/her expertise for KBTMSS during the description of either the TM hardware configuration or the operating of the system. This is needed in order to reduce the unknowns and the complexity of the mechanism as well as provide a better decision environment.

The decision criteria used the following: minimum tool requirements (captive tools), minimum tool flow, tool inventory, maximum machine utilization, and maximum throughput time.

The criteria are set according to common sense and the surveyed tool management literature [13].

The user may choose one or more criteria to make the decision. Although most of the criteria are dependent on each other, an individual criterion may be used as well.

## 4.3.3. Strategy selection decision process

KBTMSS is a menu-driven software implementation, which could be used either as a freestanding set of software tools or a part of the integrated design facility. The logic of the strategy selection module alongside DSS is depicted in Fig. 5.

KBTMSS has been designed to make decisions for users about tool management system design. There are two advantages in the use of KBTMSS. First, an expert system can represent domain-specific knowledge related to strategies as well as represent the hardware configuration of the manufacturing system explicitly. Second, an expert system can provide a satisfying rather than an optimal decision. This is necessary because close relationships of the decision criteria mean that in many instances it is too difficult to reach an optimal solution. There are three steps to reach the final decision in the KBTMSS model. First, KBTMSS starts asking a range of questions to acquire knowledge of the manufacturing environment. Because the hardware configuration is a major constraint to adopting a strategy, it is important to know what kind of environment is going to be worked in. For example, the single tools strategy by its nature needs a relatively large magazine capacity as well as a specifically designed or dedicated tool transporter system. If these conditions are not satisfied, it is very difficult to apply this strategy. Examples of the rule, which describe these conditions, are constructed as follows in the attributes section and the rules section:

![](/api/attachments/GSZ3CRZF/fulltext/images/302712330ce16e5064402c6b76d55d39805992bd6348801132e910d849e348fa.jpg)  
Fig. 5. Knowledge-based strategy selection and decision support system logic.

Once the KBTMSS recognizes the environment and what kind of strategies are applicable, it is ready to make the second main decision. In the second step, the expert system makes the decision for the tool management strategies. At this stage, KBTMSS again asks a range of questions to know what type of control and planning systems is in use in the manufacturing system. For example, if the manufacturing system uses a scheduling system in which meeting due dates is essential, it is not possible to apply the tool-oriented strategies, which have their own sequencing and scheduling system.

At the beginning of the third step, KBTMSS has the idea of what kind of environment is worked in and what type of control and planning system is practiced. In the third step, KBTMSS is ready to select the most appropriate tool issue strategy on the basis of (one or more) user-selected criteria.

The strategy can be selected for either the overall manufacturing system or a cell or only for a single specific workstation. These alternatives are needed due to differences between the hardware configurations placed in the manufacturing systems. For example, if one of the several machines placed in a cell does not have a large magazine capacity, there is no point to practice the tool-oriented strategies or single tools strategy on that particular machine.

The criteria play a crucial role at this stage. The user is asked to choose the preferred criteria. For example, if there is a pressure on the manufacturing system to meet the due date, the throughput time may be selected.

4.4. Knowledge-based manufacturing and TMS diagnosis system

Diagnosis is a three-step operation. Firstly, determine the exact cause(s) of an error, a failure, or an incorrect decision. Secondly, recognize the symptoms, analyze the symptomatic information, and interpret the various messages and indications. Finally, supply a remedy to correct the fault/error or suggest the best possible solution or the best possible decision that can be made under emerging circumstances with the supporting reasoning.

This process is highly complex and requires a certain degree of expertise at several stages. However, a well-structured diagnosis system would help to create a successful decision support system. Therefore, the classification of the possible malfunctions and possible solutions under an expert supervision is required. If this can be achieved, indeed a diagnosis system can play a vital role to ease the decision process.

This diagnosis system is more concentrated on checking the feasibility of decisions made related to tool management issues during the operation of the system in a manufacturing facility incorporating hardware operational problems.

Knowledge-based methodology is largely accepted as a design tool. However, because it calls for validation and testing during each iteration, it is used more as a diagnosis and analysis tool especially when developing systems for uncertain environment [4].

The knowledge-based manufacturing and TMS diagnosis are developed specifically to assess the tool management design and operation performance in flexible manufacturing systems. Because a very large number of outputs are generated by the KBDSS, regarding the many different tool management activities in a multilevel manufacturing environment, it is needed to test the reliability of KBDSS.

Because many rules, strategies and decisions are involved and small but important steps are taken in a tool management design effort, it is important to have expert advice at each step of the design process. The KBDSS and meeting the system requirements using the KBDSS must be reliable in order to solve the problem adequately. It is difficult to find the source of problems especially in chain events and in environments in which many factors are involved. Also, it is equally difficult to implement the available set of knowledge correctly, all at once, without further review and modification. As knowledge is collected and stored into the knowledge base, it must be evaluated and tested against the system requirements as well as the expectations of how the system is to perform and/or what knowledge the system is to contain [4]. Thus, during each step of the decision process, the decisions must be validated and supported by an expert for analysis of the available decision process output.

## 4.4.1. Structure of performance analysis module

The system is twofold. One is for performance analysis and the other is for manufacturing system and TMS diagnosis. The output analysis is part of the integrated KBDSS and is fed and updated through other design modules as well as the manufacturing database.

The system performance analyzer measures the output collected from the expert scheduling, TRP and strategy selection modules for the overall system, individual cells, workstations, tool stores and tool transporters against the user-accepted tolerances. The knowledge-based output analysis module makes the analysis easier by recognizing similarities between the real system requirements and the interpretation of real system in the rule-based environment. The system always compares the output gathered from the other modules against the user requirements. At this stage, the user requirements and specified tolerances play a crucial role in assessing the system output.

System output can be tested against formally proven and reliable real company output and justified by comparison with the real manufacturing system output or specified limits.

The performance analysis has been classified into seven groups:

Manufacturing workstation utilization: Because workstations are the major components of an automated manufacturing system, it is common sense as well as a logical conclusion that the machine utilization is very important and that high utilization is one of the indicators of the success of the manufacturing system.

Central tool store (CTS) utilization: This work primarily considers tool management issues. Therefore, it is important to consider the CTS as a basis of performance analysis, which indicates the degree of tool flow and tooling activities at factory level.

Secondary tool store (STS) utilization: STS is designed as a bridge between individual machines and CTS and it has two-way traffic as well as being the place where the main cell level tooling activities take place. Thus, it is important to consider STS performance as a major part of the part and tool flow management.

Primary tool store (PTS) utilization: PTS is the machine level tool store and supplies the tools that are used directly in operations. PTS is one of the major system design constraints, which may cause tool flow bottlenecks or serious production bottlenecks on the machine. It is the unique performance indicator for tool management at machine level.

Tool utilization: Tool utilization mostly depends on the adopted tool issue strategy. It significantly affects tool inventory and tool flow level and it is one of the most important factors in tool management.

Transport utilization: Because all the hardware elements are integrated with each other in FMS, the failure of one element may cause serious problems. In order to apply the tool issue strategies, the hardware requirements must be satisfied. The tool transport mechanism is one of the unique components of the part and tool flow, which is constrained by several factors such as capacity, speed and form of transport. It is thought that transportation should be considered as a basis of performance analysis.

Throughput and lead time report: Throughput time is a criterion not only for part and tool flow management but also for the whole manufacturing system. Because it is the basis of all the time-related activities, throughput time and its extension, lead time, are accepted as performance criteria.

The system gives a broad report for the key criteria for the applied strategy, which has been selected/ suggested by the KBTMSS module.

The system starts by giving a menu of the listed alternatives for examination of the desired manufacturing system parameters. For example, if the first alternative, workstation utilization, is chosen, the diagnosis module triggers the machine utilization section. This first determines the number of machines available and then determines which machine belongs to which cell if the manufacturing system is a multicell system. After the identification of machine numbers and machine groups, diagnosis system lists the knowledge about each individual machine giving the utilization percentage, cumulative worked time, processed jobs, sister tools used and spent tools.

It is a great help to have this level of information about the system, which gives an opportunity to the user to intervene with the system if needed. The jobs and the tools distributed to each machine and each cell can be easily envisaged. The other diagnosis parameters can be viewed with the same level detail.

## 4.4.2. TMS diagnosis

TMS diagnosis is the second main function of the diagnosis module. It is designed to support the decision process by providing feedback for both hardware and organizational problems. Because operational issues are dynamic, the knowledge stored requires updates from the other feeding modules, viz., expert scheduling, TRP and KBTMSS. This is achieved through the relational database, ORACLE, which links the three supporting modules to the diagnosis module. An optional data file, which is fed by the three modules, can also feed into the output analysis module.

The module supports four main hardware and operational problems:

\- manufacturing cell problems,

\- manufacturing workstation problems,

\- tool store problems, and

\- tooling problems.

The most likely problem areas with the supporting questions and possible solutions are stored in the global attributes section. When the initial menu triggered the related problem area, to be able to make a decision, the rules section fires the related attributes as well as the associated questions. Answers may be selected from among the output provided by the other modules or, if the user does not want to answer a relatively large number of questions, the output gathered from other modules can be attached as a default value to the related questions.

The rule section will reach a conclusion according to the given answer or specified default values. Because every possible problem stored in the knowledge base is answered by another rule, if the user asks the output analysis to provide a solution for the related problem, output analysis will prompt the related rule and will suggest a solution. Also, the problem as well as the solution can be justified by asking output analysis.

One of the problem rules is:

J:jobs

then

reassert tool store problem = tool magazine capacity insufficient endif.

The following rule is provided as a solution to the problem rule presented above:

Possible problem areas may be different in each organization and it is straightforward to change, add or

\The following rules provide solutions to manufacturing problems

Tool magazine insufficient problem solution:

y tool store problem = tool magazine capacity insufficient then

reassert remedy = reduce the transfer batch size<0.4>|

remove the worn\_broken\_or\_not needed tools from magazine<0.3>|

increase the usable tool life percentage<0.1>|

increase the tool magazine capacity<0.1>.

endif.

delete any attribute as well as change solution attributes. Also, any rule can be easily changed, deleted or added to make the output analysis module compatible with the system worked in.

## 5. Manufacturing database

Databases are defined as the collection of information that can be accessed by both end-users and application programs. A large amount of data for parts, tools, machines, operations, cells and other ancillary functions have to be manipulated among several computer programs in the part and tool flow management. The data set has to have a certain format and be internally consistent. In addition, updating the data set has to be easy. Therefore, a relational database management system is one of the major parts of the design facility.

A commercial database system, ORACLE, has been used to store the manufacturing data set and to support the other design models. The database serves as a store for all those parameters common to all the decision support modules. The shared information essentially includes jobs, workstations, tools, tool stores and cell data organized in a relational hierarchy such that, for example, tools are related to jobs and jobs may be related to workstations.

The database management system is configured into 10 blocks. These are the cell, part, tool, workstation, jobs, operation, pallet, primary tool store, secondary tool store, batch, and system blocks. Each block is connected through one or more reference data.

All the blocks can be run in any sequence and for any number of times, so that each block can be processed individually without going into detail. Once the data have been input, it is possible to edit any individual data entry without requiring the whole data record again.

Each block has its own menu system and access to data is done by querying the data. Also, the next and previous record can be easily reached by soft-key dialogue. The data handling, querying and referencing related data in another block is made much easier because of the software used.

Section 6 containing a worked example includes the step-by-step explanation of the insertion of data and the study of output data.

## 6. An experimental study and discussions

In order to demonstrate how the proposed model works, we consider a short part list (17 parts), with variable transfer batches ranging from 2 to 40 components, and the corresponding tool list (56 tools), with different cutting tool lives, in a multicell flexible manufacturing system. Tool life measurement in manufacturing industry is based on time and is used on a simple decremental basis. The data set used was obtained from the typical work requirements of a real industrial flexible machining cell producing printing machine components. The related tool data were derived from individual part process plans. The system is run for three shifts and the machine tool magazines are empty at the beginning of a three-shift period for full kitting, differential kitting and resident kitting strategies. Single tools kitting strategy keeps one tool of each type on the magazine and therefore starts the manufacturing period with full capacity. However, the system is run continuously and the initial manufacturing conditions therefore have no effects on this three-shift period.

The tool carrier robot between the cell-based secondary tool store and the machines is unidirectional. All the parts are ready at the beginning of manufacturing period and part transfer is subject to required pallet availability and pallet capacity. The model was tested on a single-stage multifunctional manufacturing system, which consists of four identical machines, capable of processing any operation of the parts to be manufactured. The parts visit only one machine where all their operations are performed. Each part type has its process plan, which indicates the operations, and corresponding tool types required that range from 2 to 12 tools. Parts are released to machines according to one of the four scheduling rules adopted. Each tool has a limited cutting tool life and tools are exchanged either when their life has expired or when they are no longer required on the related machines.

The proposed knowledge-based decision support system starts with asking a range of questions to clarify the user’s intention for part scheduling as well as determining the user-specified scheduling criteria. The scheduling is based on the algorithm presented in Section 4.2.1. The required data set is obtained through a relational manufacturing database management system. The output of expert scheduling system is given in Appendix B.

The proposed expert scheduling system first provides the batch sequence list to the machines available and then the starting and finishing times for related batches on related machines. The tooling information such as kit number, kit size, tool list in related kit, basic tools, sister tools, and number of sister tools of each is extracted from the manufacturing database by the expert system. The sample output is provided in Appendix C.

The output can be manipulated by changing the rules and strategies entered at the expert system query stage such as the number of machines used, the part scheduling rule adopted, the part batch size, and the manufacturing period. Data can either be entered during online query or stored in manufacturing database and expert system can be fed through relational database.

The second step in the knowledge-based decision support system is to select the tool issue strategy, which best matches the hardware available. The structure and the logic of the expert strategy selection module were given in Sections 4.3, 4.3.1, 4.3.2 and 4.3.3. As it happen in the other DSS modules, strategy selection also obtains knowledge by querying the user or from the relational manufacturing database or from both sources. However, most importantly, the user must specify the one or more decision criteria provided by the expert system, which are important in strategy selection. The sample output of strategy selection is presented in Appendix D.

The third module is the knowledge-based manufacturing and TMS diagnosis module, which was described in Sections 4.4, 4.4.1 and 4.4.2. This module is two part. The first is a detailed tool management performance analysis based on userselected criteria. Criteria are set into two major sections: one is to measure hardware performance, such as machine utilization, transportation utilization, tool stores utilization, and tool life utilization and another is to measure operational performance such as job throughput time, manufacturing lead time, tool issue strategy, and tool distribution success. The module gives a detailed report related to either hardware facility performance or operational performance. This provides a basis to the user to interfere the system at the performance decline stages. This part is also supported by the second part of this module, which gives a detailed report of faults or malfunctions. The user can easily recognize the reason(s) for bad performance through the diagnosis module.

The second part of output analysis is operational and hardware fault detection and solution module. This part is designed to support the issues related to generic manufacturing cell problems as well as operational problems. Most of the problems are stored in the knowledge base and the expert system diagnoses the hardware and operational problems through this prestored information. However, feeding the manufacturing database or using the output generated, other expert system modules permit the system to query every aspect of online diagnostic such as fault diagnosis, fault detection, fault compensation, and fault prediction as well. The sample output of the module is presented in Appendix E.

## 6.1. Discussions

The work reported in this paper is mainly aimed at providing a sound decision support package to ease the decisions making process on the shop floor. The criteria considered to measure the system performance are classified into three major groups. These are part scheduling performance, tooling performance, and cell performance. The work falls into three main subsections. The first is the introduction of an expert part scheduling system design, which was implemented as experimental software and has been shown to be a powerful aid to DSS. It does not attempt to cover optimum part scheduling but offers a major part scheduling support system considering both major hardware, such as machines, pallets capacity, tools, and transporter constraints, and operational constraints such as availability of tools and pallets.

It is also aimed at satisfying complex technological constraints such as matching tool kit allocations, which is difficult to accomplish using by mathematical optimization techniques. This approach, besides providing an acceptable solution, provides the opportunity to describe the defaults of the information for practical industrial applications in a more detailed and convenient manner.

The most frequent problem faced in practical problems is to schedule the jobs to the machines without checking the required cutting tool availability. The major advantage of this expert part scheduling system is to release jobs considering the tool allocation or availability. This, in fact, allows a more accurate emphasis on machine utilization and manufacturing throughput time.

The OCF, which finds the highest priority job in the job list, is the major mechanism for a real-time job dispatch. The hour-to-hour changing of shop floor conditions are transferred into scheduling through the manufacturing database and the expert scheduling module releases the jobs considering the latest shop floor conditions such as machine status (idle/busy/ down), tool availability, tool magazine status and dynamic due dates of jobs.

Although there is a small probability of having the same priority for more than one job at the same time, it is nevertheless a likely situation in a manufacturing environment. In case of priority conflict, such as this, the expert scheduling system employs a simple rule to resolve the problem. It first checks the tool requirements of competing jobs and then the available tools on the machine magazine. It then gives higher priority to the job that requires less new tools and has more tool commonality between job tool kits and available tools on the machine magazine. If still there is a conflict, which is very unlikely, one of the jobs is given a random higher priority.

The second subsection is the strategy selection module, which produces two major outputs. First, the strategy selection for the desired environment, which may be a workstation, a cell or a factory. Second, a broad strategy report for each one of the strategies applied. It approaches the problem step by step, which makes it easier to make decisions or come to a conclusion. These steps are the following:

1. Recognition of hardware environment,

2. Recognition of operational and planning environment,

3. Recognition of strategies applied,

4. Recognition of user requirements including criteria, and

5. Making decisions.

Normally, a tool management system allocates the required tools to the right machines in the right quantity at the correct time according to a tool management strategy. The tooling strategy adopted is decided by considering the current job list and available cell hardware. The cell manager applies this strategy to determine the tool inventory, tool requirements planning and cell storage content in the shortterm. However, the dynamic nature of the shop floor, even in short-term, may require different tooling strategies at different stages of manufacturing to minimise TRP, tool inventory and captive tools in the cell store. A good tool management system should be able to shift the tooling strategy to the one that is more efficient, when the shop floor conditions change. This ability depends entirely on the level and quality of feedback provided by the support system. The KBDSS plays a crucial role at this point. It processes the information provided by the expert scheduling system, TRP, and knowledge-based diagnosis system through the relational database either as a result of shop floor manager customised query or as part of automated querying of the latest performance measures against default values. The cell manager may take further action and provide adjustments including shifting the tool issue strategy currently in practice.

The output analysis has the capability of analyzing output generated by the part and tool flow management system. The output is assessed against a predetermined set of criteria approved by the industrial company. These criteria could be specified by individual users or by a company. Because of the DSS flexibility, they can easily be replaced or changed. The software could be used entirely as an interactive analyzer canceling predetermined default values that as a result of this process might produce many unwanted prompts. Also, when the default values are specified to the attributes, it is possible to analyze the entire system without responding a single prompt.

The third major subsection of the DSS is designed to solve the major TMS design problems. Problem recognition is based on internal problem classification. These are cell, workstation, tool store, and tooling problems. The DSS has the flexibility to let the user specify their own criteria, problem and analysis areas and can easily be restructured by feeding it with a new set of attributes as well as rule sets in order to make it compatible with the working environment.

For the cell control, the performance measures including cell diagnosis are compared with threshold default values constantly and the changing performance monitored with data being transferred to the manufacturing database with necessary expert advice. This gives an invaluable support to the cell manager to make the decisions.

## 6.2. Benefits of using KBDSS

The present knowledge-based system development is aimed at providing a comprehensive support to ease the decision process primarily on part scheduling, tool management and cell control.

As discussed earlier, part scheduling, tool management, and cell control would normally require extensive support from different operations experts to make correct decisions about when such support is needed. Therefore, an integrated solution considering all contributing elements and technologies is the most appropriate approach. This has been attempted in this paper. Unavailability of such expertise support can lead to undesirable results including incorrect solutions, waste of time, and cost penalties.

Increasing market pressure has lead to reducing manufacturing lead time and product costs whilst producing high-quality product. Lack of expert support at different stages can be very costly for a manufacturing system. Furthermore, seeking and acquiring such expertise from outside of the company, such as temporary consultancy support, can be very expensive and not always appropriate.

A knowledge-based decision support tool, such as the one described in this paper that has already captured the expertise required, could be a viable alternative solution to the problem areas described in this paper.

Having such a tool available at all times will allow the cell manager to be more quickly providing solutions for the part scheduling, tooling management, and cell control problems without relying on external support. This will lead to speedier decisions, shorter response time, shorter down time for equipment and improved manufacturing.

## 7. Summary and conclusions

In this paper, we have proposed a knowledge-based decision support system for the intelligent management of parts and tools in flexible manufacturing systems. The proposed system is a hierarchical system, which supports the manufacturing environment ranging from a single standalone workstation to multicell multimachine manufacturing system.

This study of KBDSS is designed to assist shop floor managers in making decisions quicker with minimum error. In addition to intelligent job and tool releasing capability, KBDSS provides powerful manufacturing system diagnosis as well as a best tool issue strategy selection mechanism for different cell hardware structure. The user requires either minimal or no prior knowledge to use KBDSS because system is a complete DSS to schedule, diagnose and select strategy in a flexible manufacturing facility. KBDSS adopts a modular modelling approach to construct the DSS model. This guarantees the robustness of the built model. A comprehensive example presented in this paper shows that KBDSS gives satisfactory results for offline evaluation as well as opening a promising new direction for applying KBDSS for online dispatching, diagnosing, and strategy selection in an FMS environment.

## Appendix A

Sample scheduling system rules

```txt
\*** determine which jobs are feasible
forall J:jobs do
if (inclass(J>job_op predecessor, jobs)=true and
    J>job_op predecessor>process_factor = 1 and
    J>job_op predecessor # "none" and
    J>op_number gt 1 and
    J>op_number = 1 and
    J>process_factor = 0)
then
    reassert J>feasible = true.
    message combine ("job:",J,"is feasible").
else
    reassert J>feasible = false
message combine("job:",J,"is not feasible
endif.
endforall.
```

and the job selection is decided by the following rules:

```txt
\*** job rule1 selecting a feasible highest priority job rule:
J:jobs
if
    J>lowest priority number = true and
    J>feasible = true
then
    reassert chosen job = J.
endif.
\*** job rule2 finding the lowest priority job rule:
JX:jobs, JY:jobs
if
    JX#JY and
    JX>job priority le JY>job priority
then
    reassert JY>lowest priority number = false.
endif.
\*** erase the 'lowest priority number' attribute value of each job to force their determination each time
determined(chosen stn>current stn release_value) = false
then
    chosen stn>current stn release_value = 0.
endif.
```

The above rules search for jobs, which have the ‘‘lowest priority number’’ expert system attribute set to ‘‘true’’ and the ‘‘feasible’’ attribute set to ‘‘true’’. The ‘‘feasible’’ attribute is determined considering job’s predecessor and process factor. The ‘‘lowest priority number’’ is always initialised by being erased. This enables the ‘‘lowest priority number’’ to be determined each time.

The decision for the station chosen is determined by the rule:

```txt
S: stations
if    S>lowest candidate mc priority_est = true
then    reassert chosen stn = S.
endif.
```

The rule that decides which job or station starts first is as follows:

```txt
if
chosen job>job start time ge chosen stn>stn available time then
reassert chosen job>job start time = chosen stn>stn available time. else
reassert chosen job>job start time = chosen job>job start time. endif.
```

## Appendix B

Knowledge Engineering System (KES), Release 3.0. Copyright 1990, Software Architecture & Engineering, Inc. Loading the knowledge base "Tmsdss.pkb".

KNOWLEDGE BASED \*

DECISION SUPPORT SYSTEM

大 PART and TOOL FLOW MANAGEMENT \*

大 Loughborough University of Technology \*

Kbfile: TMSDSS.KB

Data Files: Jobs.Dat, Pallet.Dat, Stn.Dat, Tool.Dat, Clus.Dat, Strat.Dat

There are:17 jobs to be scheduled to available 4 manufacturing workstations.

What is the scheduling period?

(Enter a number)

=? 1440

=? EDD

What would you like to do?

1. Job Scheduling System

2. Tool Management Strategy Selection System

3. Manufacturing and TMS Diagnosis System

4. Quit

What would you like to do?

1. Schedule jobs to manufacturing workstations

2. View job release to manufacturing cells

3. View job release to manufacturing workstations

4. Quit

job: none is not feasible

job: job1 is feasible

job: job17 is feasible

The feasible job released into cell is : job1

The station selected for its manufacture is : station1

This job had its preceding operation in job list : none

job was released to cell: 1

job1 has now been completed on station1

The feasible job released into cell is : job17

The station selected for its manufacture is : station2

This job had its preceding operation in job list : job14

job17 has now been completed on station2

job was released to cell: 17

Type 'c' to continue or 's' to stop.

## Appendix C

Station Job Release Table \* \* \*

```txt
Station : station2
Cell : 1
Release Value : 4
Job : job9
Start Time : 762.40002
Finish Time : 1151.2
Kit ID : Kit11
Kit Size : 10
Tool List : T5320, T5321, T1001, T1117, T3120, T1050, T2060
NoOf Basic Tools : 7
Sister Tools : T1050, T1117, T2060
NoOf Sister Tools : 1,1,1
Kit Cost : 0 (No data supplied)
```

Station : station4 Cell Release Value Job : job13 Start Time : 639.5 Finish Time : 668.5 Kit ID : Kit15 Kit Size Tool List : T1247, T1157, T3160, T5050 NoOf Basic Tools Sister Tools : None NoOf Sister Tools : 0 Kit Cost : 0 (No data supplied)

Type 'c' to continue or 's' to stop.

Appendix D
What would you like to do?
1. Job Scheduling System
2. Tool Management Strategy Selection System
3. Manufacturing and TMS Diagnosis System
4. Quit
=? 2
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\* Welcome to Expert Tool Management Strategy Selection \*\*\*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Please enter one or more criteria you wish as a basis for selection...
0. None
1. Minimum tool requirement,
2. Minimum tool flow
3. Minimum tool inventory,
4. Minimum production throughput time
5. Maximum machine utilisation
(Enter a number)
=? 1
(Enter a number)
=? 0 (None)
......
......
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\* The best strategy is "Hybrid Strategy" for this job list \*\*\*
\*\*\* and cell configuration \*\*\*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Type 'c' to continue or 's' to stop.

## Appendix E

```txt
What would you like to do?
1. Job Scheduling System
2. Tool Management Strategy Selection System
3. Manufacturing and TMS Diagnosis System
4. Quit
=? 3

What would you like to do?
1. TMS Output Analysis
2. Manufacturing and TMS Operational Problems & Fault Detection =? 1
What would you like to do?

1. Manufacturing Workstation Utilization
2. CTS Utilization
3. STS Utilization
4. PTS Utilization
5. Tool Utilization Level
6. Transporter Utilization
7. Throughput & Lead Time Report =? 1

*************************** Workstation Utilization Table ***************************
Station :Station_1
Group :1
Jobs Done :3
Utilization :73.254
Worked :1054.86
...
...
Station :Station_4
Group :2
Jobs Done :4
Utilization :92.85
Worked :1337.15

What would you like to do?
```

1. TMS Output Analysis

2. Manufacturing and TMS Operational Problems & Fault Detection

=? 2

What would you like to do?

1. Manufacturing Cell Problem

2. Manufacturing Workstation Problem

3. Tool Store Problem

4. Tooling Problems

5. Justify Manufacturing Problems

6. Justify Workstation Problem

7. Justify Tool Store Problem

8. Justify Tooling Problem

9. Provide Solution

10. Justify Solution

11. Exit

=? 4

What amount of tool should be available for the next batch?

(Enter a number)

=? 12

What is the size\_of cell tool inventory?

(Enter a number)

=? 300

What is the current critical tool size?

(Enter a number)

=? 12

What is the sister tool size for batch?

(Enter a number)

The TRP kit size recommendation for this job is

=? 12

Would you like to see the list\_of tools that will be assigned for this job?

(Enter Yes or No)

=? No

No Tooling Problem has been discovered

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Type 'c' to continue or 's' to stop

## References

[1] G.M. Acaccia, F. Campolonghi, R.C. Michelini, R.M. Molfino, Expert simulation of a tool-dispatcher for factory automation, International Journal of Computer Integrated Manufactur ing 2 (3) (1989) 131– 139.

[2] G.M. Acaccia, R.C. Michelini, R.M. Molfino, G. Raffaelli, An expert scheduler for tool stock management in a CIM environment, AdvancedManufacturing Engineering 1 (1989) 203 – 209.

[3] K.A. Amoaka-Gyampah, J.R. Meredith, A. Raturi, A comparison of tool management strategies and part selection rules for flexible manufacturing systems, International Journal of Production Research 30 (4) (1992) 733–748.

[4] E.P. Andert, Integrated knowledge-based system design and validation for solving problems in uncertain environments, International Journal of Man-Machine Studies 36 (1993) 357– 373.

[5] A.S. Carrie, D.T.S. Perera, Work scheduling in FMS under tool availability constraints, International Journal of Production Research 24 (6) (1986) 1299– 1308.

[6] F.T.S. Chan, B. Jiang, N.K.H. Tang, The development of intelligent decision support tools to aid the design of flexible manufacturing systems, International Journal of Production Economics 65 (2000) 73 – 84.

[7] P. Coleman, M. O<sup>¨</sup> zbayrak, R. Bell, Tool management and job allocation in flexible machining cells, part 1: work oriented strategies, Proceedings of IMechE Part B. Journal of Engineering Manufacture vol. 210 (5B), British Institute of Mechanical Engineers (IMechE) 1996, pp. 405 – 416.

[8] P. Coleman, M. O<sup>¨</sup> zbayrak, R. Bell, Tool management and job allocation in flexible machining cells, part 2: tool oriented strategies, Proceedings of IMechE Part B.Journal of Engineering Manufacture vol. 210 (5B), British Institute of Mechanical Engineers (IMechE) 1996, pp. 417– 425.

[9] S. Ghosh, S.A. Melynk, G.L. Ragatz, Tooling constraints and shop floor scheduling: evaluating the impact of a sequence dependency, International Journal of Production Research 30 (6) (1992) 1237– 1253.

[10] A. Goh, Y.-K. Koh, D.S. Domazet, A rule-based support for work flows, Artificial Intelligence in Engineering 15 (2001) 37 – 46.

[11] T.W. Graver, L.F. McGinnis, A tool provisioning problem in FMS, International Journal of Flexible Manufacturing Systems 1 (1989) 239– 254.

[12] Knowledge Engineering Systems (KES) Production System (PS) User Manual, Template Software, VA, 1993.

[13] M. O<sup>¨</sup> zbayrak, P. Coleman, R. Bell, Tool management for flexible manufacturing facilities: a literature review, Interna-

tional Journal of Production Research (2001), submitted for publication.

[14] M. O<sup>¨</sup> zbayrak, B.R.B. De Souza, R. Bell, Design of a tool management system for a flexible machining facility, Proceedings of IMechE Part B. Journal of Engineering Manufacture vol. 215 (5B), British Institute of Mechanical Engineers (IMechE) 2001, pp. 353– 370.

[15] S.A. Patel, A.K. Kamrani, Intelligent decision support system for diagnosis and maintenance of automated systems, Computers and Industrial Engineering 30 (2) (1996) 297 – 319.

[16] S. Rahimifard, S.T. Newman, Simultaneous scheduling of workpieces, fixtures and cutting tools within flexible machining cells, International Journal of Production Research 35 (9) (1997) 2379 – 2396.

[17] C.S. Shukla, F.F. Chen, An intelligent decision support system for part launching in a flexible manufacturing system, International Journal of Advanced Manufacturing Technology 18 (2001) 422–433.

[18] J.P. Son, J.H. Park, Y.Z. Cho, An integrated knowledge representation scheme and query processing mechanism for fault diagnosis in heterogeneous manufacturing environments, Robotics and Computer-Integrated Manufacturing 16 (2000) 133– 141.

[19] K.E. Stecke, I. Kim, Formulation and solution of non-linear integer production planning problems for flexible manufacturing systems, Management Science 29 (1983) 273 – 288.

[20] A.T. Unal, A.S. Kiran, Batch sequencing, IIE Transactions 24 (4) (1992) 73 – 83.

[21] J.A. Ventura, F.F. Chen, Grouping parts and tools in flexible manufacturing systems production planning, International Journal of Production Research 28 (6) (1990) 1039–1056.

![](/api/attachments/GSZ3CRZF/fulltext/images/983a24bdaf31b7455a640ca929412d3f0778aea7eeadc46e5799c6bea90a9046.jpg)

Mustafa O<sup>¨</sup> zbayrak is a lecturer in the department of Systems Engineering at Brunel University. He received his PhD in Manufacturing Engineering from Loughborough University of Technology (LUT). He also holds BS and MS both in Industrial Engineering. His primary areas of research interest include modelling and analysis of production systems, supply chain management, operations scheduling, application of artificial intelligence to manufacturing, and

the multiagent system applications to planning and control problems of manufacturing systems. Dr. O<sup>¨</sup> zbayrak has published extensively in the areas of planning and control of manufacturing systems, expert systems applications, and manufacturing systems.

![](/api/attachments/GSZ3CRZF/fulltext/images/ef3d6105e068705d4fb1adbb329bcad2dd09f75b0f9a2c9b1294f0f9dda5185b.jpg)

Robert Bell is a professor emeritus in the Department of Manufacturing Engineering at Loughborough University. Professor Bell graduated from UMIST in Electrical Engineering in 1954, with MS in Textile Technology in 956. Graduate trainee at Metropolitan Vickers 1956 – 1958. Research engineer at UMIST in machine tool research 1958 – 1960. Teaching and research in the field of machine tool engineering at UMIST 1960–1975. Appointed

Reader in 1972. Awarded DSc in 1975. Appointed Professor of Manufacturing Technology at LUT in 1978. Established research in flexible manufacturing systems with particular emphasis given to modelling methods for cell design. Contemporary research interests concerned with the role of product and manufacturing models in computer-integrated engineering, concepts for factory modelling, and research into tool management systems. A major additional interest has been the international activities in Intelligent Manufacturing Systems (IMS), being a member of the European and International Technical Committees throughout the feasibility study. A further major interest has been support for academic development under the aegis of the ODA and UN, with assignments in Brazil, Hong Kong, India, Mexico, Singapore, Sri Lanka, and Turkey.
