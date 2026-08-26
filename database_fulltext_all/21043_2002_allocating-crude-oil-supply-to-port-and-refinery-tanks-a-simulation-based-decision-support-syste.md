---
otero_id: 21043
otero_key: "RA2BVHVB"
title: "Allocating crude oil supply to port and refinery tanks: a simulation-based decision support system"
authors: "Massimo Paolucci; Roberto Sacile; Antonio Boccalatte"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00133-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Short communication

# Allocating crude oil supply to port and refinery tanks: a simulation-based decision support system

Massimo Paolucci \*, Roberto Sacile, Antonio Boccalatte

Department of Computer, Communication and System Sciences (DIST), University of Genova, Via Opera Pia 13, 16145 Genova, Italy

Received 1 February 2001; received in revised form 1 June 2001; accepted 1 July 2001

## Abstract

This work focuses on the problem of allocating the crude oil loads of tanker ships to port and refinery tanks (PRT). Two discrete scheduling aspects mainly influence this process: the tankers’ arrivals and the sequence of crude lots processed in the refinery. A simulation-based approach that can be applied as a simulator of the physics of the crude oil flow in the refinery system, as a learning support for personnel training, and as a decision support system (DSS) is proposed. The results of the application of the implemented system on a real small – medium-sized refinery system are presented. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Crude oil supply; Simulation model; Crude oil allocation; Decision support system

## 1. Introduction

Refinery management is subject to many global economic and local practical factors that can alter previously planned workloads. For example, it is well known that the crude oil market often shows critical and quite unpredictable price variations. However, many critical local and last minute situations—such as the lack of available jetties or tanks, the delay of the tanker ship arrival, changes in the production plan that are again unpredictable—can occur and even play an important role. In this scenario, for example, after a previously planned decision ‘‘to buy’’ a tanker load for distillation just prior to or at the tanker’s arrival, a decision maker may sell the load to another company because the delay in the tanker discharge is deemed too high (e.g., since another tanker is using the only available jetty) or because demurrage costs may be considered unacceptable.

Fig. 1 outlines the salient production/distribution elements of an oil company, with arrows depicting the material flow associated with the refinery process. The refinery receives crude oil from tankers at the port, where usually more than one jetties are available. A pipeline connects the jetties to a number of crude storage tanks that are present both at the port and at the refinery. Depending on the storage and production policies, the crude oil is pumped to the refinery crude distillation units to be distilled. At the refinery, other tanks store distilled oil and a subsequent distribution network provides the refined products to other retailers.

On a monthly basis (usually over a time span of 3 or 6 months), the refinery management plans the crude oil supply according to market forecasts, seasonal uses and market trends. This plan determines the tanker arrival sequence at the ports. Two distinct scheduling aspects mainly influence the allocation of crude oil to port and refinery tanks (CO-2-PRT), the tankers’ arrivals and the sequence of crude lots to be processed in the refinery. A correct allocation of CO-2-PRT plays an important role in absorbing the different dynamics of these two aspects.

![](/api/attachments/RA2BVHVB/fulltext/images/dacb536407055b33e1643fe88231d6313185a74e5f13216740ca81d6c8fdbfa9.jpg)  
Fig. 1. The structure of a generic refining oil company.

This work focuses on the two grey boxes of Fig. 1, that is, on the decisional problems relevant to the CO 2-PRT allocation.

Several constraints hinder the CO-2-PRT allocation problem. Crude oil loads of different qualities should generally be segregated. This means that in order to avoid contamination, different crude oil qualities are assigned to different tanks. Hence, the PRT are often partitioned into subsets devoted to the various types of oil. Changing the assignment of a tank to a different crude oil type is a long and arduous task for many reasons: for example, an empty tank always has a residual that may be left to avoid the use of the oil residual deposited in the bottom of the tank or imposed by the floating tank roof system used to prevent the dangerous development of gas. Thus, a set-up procedure must be performed before storing a different kind of crude oil into a tank.

In addition, it is not possible to pump oil in and out of the tank at the same time, nor is it possible to pump crude oil from a tanker into more than one tank at a time.

These constraints obviously influence the processing times of oil discharging and transferring operations with consequent economic effects.

The PRT input and output are respectively represented by the sequence of tanker arrivals at the port site and by the transfers from the refinery tanks to the distilling plant. Both the input and output processes are defined a priori: the ships arrive following a preset calendar and the distilling plant is fed as dictated by the production scheduling plans. However, these processes are generally affected by stochastic disturbances that can influence the system behaviour. For example, ship arrivals are only confirmed about 2 days ahead of time, and the exact arrival time is not known with certainty; in addition, refinery production plans may be adapted according to market variations. For these reasons, the definition of a detailed plan for oil allocation over a long time span is rather difficult.

By contrast, refinery processes and operations are generally slow: for example, either a transfer process or the production of a specific oil product generally lasts for hours if not for days. This means that a decision about a certain kind of production can affect system processes for a long time. In addition, the distillation process can follow any one of the several alternatives during the mixing of crude oil components. This allows for a certain level of flexibility in plant feeding, even if the most efficient mix alternative is generally the one already specified in the production plan.

In the CO-2-PRT allocation problem, there are two primary objectives:

 to minimise the tanker download time, avoiding idle time waiting for tank availability; and

 to allocate the crude oil supplies to appropriate tanks in order to minimise the amount of unaccepted (and hence sold) crude oil.

Deciding and unloading without interruption the quantity of a tanker load that can be accepted and the selling of what remains usually achieve the first objective. To reach the second objective, company managers must take decisions on the basis of their experience, ultimately exploring alternatives by relaxing certain constraints. For example, company managers usually exclude the possibility of changing the destination (type of stored crude oil) for a tank, but if needed, they do resort to this approach.

In our opinion, simulation models can be effectively applied to the CO-2-PRT allocation problem since they allow the comparison of several runs under different conditions and can be easily understood by human decision makers [1]. Simulation models also respond to personnel training needs. On the other hand, defining an optimization model based on a mathematical formulation of the problem to support a decision-making process is neither simple nor suitable. The use of the simulation model to provide decision support is a quite common approach in the decision support system (DSS) literature (e.g., in water management [7] and traffic control [8] contexts). However, using simulation models for optimization can be inefficient in many cases [2]. The most efficient way to face a decisional problem is by using a polynomial time optimization algorithm or an approximated heuristic one. As often happens in this context, it is not always simple to formulate a model that provides solutions which are considered reliable and acceptable. Decision makers often like to be directly involved in the ‘‘physics’’ of the problem: they may be sceptical of a response provided by a ‘‘black box,’’ as an optimization algorithm might seem, and they want to understand the rationale underlying the choices made while interacting with the support tool during the decisional processes.

While mathematical programming is suited and currently used for the long-term production planning in a refinery in the coming years, rapid decision processes, especially with quite heavy economic impact like CO-2-PRT allocation problems, are likely to be solved by skilled human planners rather than by computer software. In this respect, a simulation model is suited for the collection of the knowledge of human refinery planners, involving them in model validation and refinement phases, ultimately becoming a tool for both the training of new staff, as well as for the analysis of the effects of structural changes on the system’s performance (e.g., the availability of a new tank).

Simulation software that can provide trustworthy decisions and at the same time train new planners is a real need in a refinery. These are the reasons that led us to develop a DSS based on a simulation model. During the simulation, the decision makers can follow the evolution of the system model, stop it to change working conditions and directly verify the ‘‘real’’ feasibility of their actions. In this respect, our system is compliant with the major goal of any DSS as stated in Ref. [4], that is, to improve the effectiveness of the decisions.

In Section 2, the CO-2-PRT allocation problem and the DSS architecture are described. Two allocation policies are compared and discussed, and the results yielded by the analysis of some case studies are reported.

## 2. The definition of the CO-2-PRT allocation problem

The CO-2-PRT allocation problem can be described as a network model (Fig. 2). Each tanker arrival is described by the quantity, $q _ { i } ,$ and by the type $o _ { i }$ of the crude oil. The pumping system at the port allows the transfer of the shipload to the port storage facilities. These have a limited availability and a behaviour that can change over time: usually, one ship at a time can be served and the pumping rate depends on the tanker-pumping device.

The port storage subsystem includes several tanks that at a fixed time can be partitioned into different sets depending on the type/quality of the crude oil currently stored. However, during the whole CO-2- PRT allocation process, company decision makers could find it convenient to change the crude oil type stored in a tank and to perform the needed tank set-up operations. In order to empty a tank (but even for different reasons), some transfers between tanks of the same set may be ordered. Usually, these kinds of operations precede the arrival of a tanker and are carried out in order to set up the storage tank system to more efficiently receive the shipload.

The port storage subsystem is connected to the refinery subsystem by a pipeline that can transfer only one type of crude oil at a time. The pipeline usually allows the transfer of crude oil at a high rate compared to the other pumping systems, so it should not be considered a bottleneck of the whole system. An additional possibility (Fig. 2) is to unload the tanker through direct pumping into the refinery storage subsystem. This direct transfer is usually rejected since the possible pumping rate in this case is reduced compared to the nominal pumping capacity of the pipeline.

![](/api/attachments/RA2BVHVB/fulltext/images/e644191b357a14c6fd7bcb90a6577a4d3330bbb4cb7187a6ac73fc72a7eae092.jpg)  
Fig. 2. The CO-2-PRT allocation problem network representation.

With respect to the port subsystem, the refinery storage subsystem has a symmetrical behaviour. The outputs here are represented by the feeding system of the distilling plant, that is, by a sequence of transfers of quantities, $f _ { s } ,$ of crude oil of type $a _ { s } ,$ from the storage tanks of the refinery subsystem to the distilling plant and by the quantities $r _ { i }$ of crude oil that must be sold since they cannot be feasibly stored.

The crude oil scheduling problems described in previous works [6] and in some aspects also in Refs. [3,5] are quite similar to the CO-2-PRT allocation problem, but the approach adopted to solve it is different. Among the possible differences from the CO-2- PRT allocation problem dealt with in this work, in Ref. [6] no stochastic variations are taken into account, it is not possible to set-up a tank in order to change the type of crude oil that it can store, and possible transfers among tanks aiming at preparing the reservoir system to better stock new arrivals are not considered. The approach followed in Ref. [6] for the crude oil scheduling problem calls for the formulation and resolution of a mixed integer programming (MIP) problem. Time obviously plays a relevant role in the refinery system, as its state changes continuously with the processing of the storage operations. Moreover, the ‘‘crude oil segregation’’ constraint and the fact that the pumping operations must be performed one at a time (generally separated by set-ups) highlight the discrete (combinatorial) nature of the decisions. As a result, as also noted in Refs. [5,6], time discretization and integer (binary) variables rapidly increase the dimensions of the problem. To take the formulation to a reasonable size, simplifying hypotheses should be introduced (e.g., rather ample discretization of the time) and the whole problem should be split into two separate allocation problems at the refinery and the port sites that are solved sequentially using the solution of the first problem as input for the second. Finally, an optimization model could very hardly take into account the changing of the type of oil for a tank, that ${ \mathrm { i s } } ,$ the modification of a storage tank into another type. The reader can see how similar difficulties can arise, even considering a dynamic programming model that could be adopted to face the dynamic behaviour of the system.

For all the above reasons and also bearing in mind that ship arrivals may be subject to stochastic variations and that, generally speaking, the actual system behaviour may be disturbed, the analysis of storage policies by means of a simulation model seems more appropriate.

Although many of the physical processes involved in the CO-2-PRT problem are continuous in nature, the decisions are taken according to specific events (e.g., the tanker’s arrivals, the start or the end of oil transfers, the tank set-ups, etc.). Let us indicate $t { = } 1 , . . . . T$ as the whole sequence of events, assuming the events known a priori, and let T be fixed in order to represent the system behaviour for a given period (say, 6 months or 1 year). Two sets of information represent the input and the output of the system.

. Information on tanker arrivals. These are the quantities $q _ { t ( i ) }$ of crude oil of type $o _ { t ( i ) } ,$ , where $t ( i )$ represents the event corresponding to the ith arrival; in addition, since the pumping speed can depend on the tanker, a pumping rate, $\mathrm { p r } _ { t ( i ) } ,$ must be considered.

. Information on the transfers of crude oil to the distilling units of the refinery. These are the quantities $f _ { t ( s ) }$ of crude oil of type $a _ { t ( s ) } ,$ where $t ( s )$ is the event corresponding to the beginning of the sth transfer.

The system state is characterised by a number of variables defining:

the type of crude oil stocked in a tank; several tank subsets $\mathrm { T S } _ { t } ^ { o }$ are defined which include the indexes of tanks that at the event t are compatible with the oth crude oil type; and

 the quantity $\nu _ { j t }$ of crude oil stocked in the jth tank at the time of event $t ;$

## and by several constant quantities:

 the tank capacity, cap<sub>j</sub>, expressed in $\mathrm { m } ^ { 3 }$ (although this quantity may vary slightly as a function of the temperature, it has been assumed as a constant);

 the pipeline pumping rate, ppr, and the one among the tanks at the same site, tpr; and

the set-up time, $\mathrm { s t } _ { j } ,$ to change the destination of a tank j (in general, this time may also depend on the initial and final type of crude oil since in certain cases, a limited level of blending between two different oils can be accepted).

The decision variables can be identified as the following.

. The crude oil transfers from the current tanker to a tank $j , y _ { t j } ,$ or between a pair of tanks j and $k , y _ { t j k } ,$ that begin at the occurrence of event $t ,$ that is, if t(i)

corresponds to the arrival of the ith ship, any oil transfers involving such a ship should have $t { \geq } t ( i )$

. The quantity, $r _ { t } ,$ of crude oil that (not being storable) is sold.

. The changes of the type of oil that can be stored in a tank j at time instant $t , \ x _ { t j } ^ { o } .$ These are binary variables that indicate if tank j should perform a set-up to be compatible with the oth type of oil. Note that the time instant at which such kind of event should occur is itself a decision variable.

The system behaviour is ruled by several constraints that are relevant to:

 the oil compatibility for the tanks (which conditions the composition of sets TS<sup>o</sup>);

 the dynamics of the transfer processes, i.e., allowing the computation of the relevant processing times;

 the material balance; and

the feasible use of the resources (i.e., involving the tank capacity, the minimum duration of the feeding operation, the impossibility of more than one loading or unloading operation at a time).

The objectives and the criteria of the CO-2-PRT allocation problem are many, so it becomes a multicriteria optimization problem. However, the objective of minimising the tanker service time is certainly the most critical one. Decisions that distribute the crude oil among the tanks even optimally, which avoid selling any excess of an arrived quantity but require to stop a ship longer than strictly necessary for discharging, are always rejected. Similarly, stopping the crude oil flow to the refinery distillation units should definitely be avoided. Other decision objectives that must be considered, in qualitative order of importance assigned by the company managers, are:

1. minimising the whole quantity of sold oil during the observed period $( O _ { 1 } ) ;$

2. minimising the number of set-ups due to changes of the type of oil allowed for a tank (O<sub>2</sub>);

3. minimising the number of simultaneous transfers among the tanks $( O _ { 3 } ) ;$

4. maximising the quantity of crude oil stored in each tank that is not completely filled $( O _ { 4 } )$

5. minimising the number of tanks used to discharge a ship $( O _ { 5 } ) ;$ and

6. minimising the number of tanks used to feed the refinery $( O _ { 6 } )$

Objective 4 aims at reducing the number of tanks used for discharging a ship and at filling as much as possible the tanks currently used. In this case, two different indexes, $O _ { 4 \mathrm { a } }$ and $O _ { 4 \mathrm { b } } ,$ can be defined, namely

$$
O _ {\mathrm{4a}} = \frac {\sum_ {i = 1} ^ {\mathrm{NS}} w _ {i} Q _ {i}}{N}
$$

where N represents the total number of tanks, $\mathcal { Q } _ { i }$ is the quantity of crude oil allocated into the ith tank, and $w _ { i }$ is the weight computed as

$$
w _ {i} = \frac {\operatorname{cap} _ {i}}{\max _ {j} \operatorname{cap} _ {j}}
$$

and

$$
O _ {4 \mathrm{b}} = \frac {\sum_ {i = 1} ^ {\mathrm{NS}} Q _ {i}}{\mathrm{NS}}
$$

where NS is the number of the tanks used only to discharge a tanker and, in this case, $\mathcal { Q } _ { i }$ represents the quantity of crude oil allocated into each of them. Index $O _ { 4 \mathrm { a } }$ favours the fact that larger tanks are filled before smaller ones. Greater values of index $O _ { 4 \mathrm { b } }$ are associated with situations for which a smaller number of tanks have been used to store the same quantity of crude oil.

## 3. The decision support system

We have implemented a DSS allowing the decision makers to determine a feasible allocation policy by simulating different scenarios such as different sequences of tanker arrivals, different tank planning, strategic allocations and allowing system reconfigurability and flexibility.

Typical applications of the system are:

 to test the monthly plan with special reference to critical physical aspects, such as tanker arrivals and tank allocations;

 to test the marketing strategies, such as ‘‘selling’’ a tanker or buying a ‘‘new’’ unplanned one; and

 to train personnel behaviour to face simulated unpredictable events.

In order to satisfy the previous requirements, we have implemented the system on a PC platform using a tool with a friendly graphical user interface (GUI), allowing users to understand immediately the evolution of the system. In addition, we needed to develop a set of modules defining parts of the refinery, which can be repeated in the same plant or in other applications in a sort of an object-oriented approach.

In this section, we show the detailed problem definition, the DSS architecture and its modules.

## 3.1. The DSS architecture

As with any DSS tool [4], three main components characterise our system architecture: the user interface, the simulation model and the data repository. The first two components have been developed with Extend V4 (ImagineThat, http://www.imaginethat.- com), a simulator development tool, while the third one has been implemented using a relational database management system (RDBMS) (Ms SQL Server version 7.0).

The user interface is a graphic interface that allows the definition of the layout of the refinery plants according to predefined (both system and custom) modules and the definition of the system state. After its start, the DSS can evolve to new states that are graphically displayed. For example, the crude oil of a tanker has been divided into lots (represented by barrel-shaped icons), which correspond to the crude oil quantity that is transferred during an animation time step, previously defined by the user.

Decision makers can configure the evolution of the DSS into the two following modalities.

. Manual: the user can decide new strategies at each single step of the system evolution. This configuration is very useful for training purposes.

. Automatic: the user can choose a strategy for the allocation of the tanks among the ones defined a priori. If $\nu _ { j t }$ is the level of tanker j at the occurrence of event t and TS<sup>o</sup> is the set of available tanks which can be used for the oth type of crude oil, two simple heuristics have been implemented in the current version of the system:

Maximum Available Capacity First (Max ACF), which aims at favouring the use of the minimum number of tanks to stock a shipload. Such a policy selects the next tank that should be used as:

$$
j ^ {*} = \underset {j \in \mathrm{TS} _ {t} ^ {o}} {\arg \max} \left[ \operatorname{cap} _ {j} - v _ {j t} \right]
$$

Minimum Available Capacity First (Min ACF), which gives priority to completely fill the maximum number of tanks, i.e., it aims at reducing the ‘‘fragmentation’’ of the free capacity of the storage system:

$$
j ^ {*} = \underset {j \in \mathrm{TS} _ {t} ^ {o}} {\arg \min} \left[ \operatorname{cap} _ {j} - v _ {j t} \right].
$$

In both modalities, each event occurring while the DSS is running is stored in a series of tables defined in the RDBMS. This is useful for many applications such as, for example, further statistical analysis, training of personnel by cases and the definition of specific system behaviours.

## 3.2. The DSS subsystems

The DSS user interface and simulation model have been developed using Extend V4, which allows the development of simulators through visual composing the relevant system structure by connecting the blocks associated with the various system components. A block can correspond to an elementary system component or to a ‘‘hierarchical block,’’ that is, a subsystem that is, in turn, defined by other blocks (both elementary and hierarchical). Each block is made up of four main elements: code, graphic aspect, dialogue window and input/output connectors. The block code is a C-language-like function defining the block behaviour that is invoked on the occurrence of events relevant for the block (i.e., the arrival of an item that must be processed). The connectors are the links that make the block communicate with other blocks. Two classes of connectors are defined in Extend: the value connectors devoted to the information flow in the system and the item connectors used to represent the flow of physical items.

Several hierarchical blocks associated with the higher level refinery system components, which have been designed by dividing the model complexity on other hierarchical sub-levels, make up the DSS simulation model.

In the following paragraphs, we introduce the main subsystems of the CO-2-PRT allocation problem described as Extend blocks.

## 3.2.1. The harbour subsystem

Four modules constitute a harbour subsystem (Fig. 3).

3.2.1.1. Ship Generator block. It generates the entity associated to a tanker arrival and it is made up of four main sub-blocks.

![](/api/attachments/RA2BVHVB/fulltext/images/a71a9fcc6d41809822a47c7cee5c944d3eb0b39ecd1be9805641ece90b65789f.jpg)  
Fig. 3. The harbour subsystem.

. A standard Item Generator Extend block allowing the definition of an a priori schedule for the item arrivals. This solution has been adopted since we assume to know, for the period of analysis, the planned arrivals, which could, however, be stochastically modified. The a priori arrival schedule is an item table reporting the expected arrival time and other relevant tanker attributes such as the crude oil type, the quantity of crude oil loaded and the maximum pumping capacity.

. A standard Random Generator Extend block which is devoted to the generation of a random disturbance of the tanker arrivals. This disturbance corresponds to a delay that is represented by a positive truncated normal distribution.

. A standard processing/delay block which delays the tanker arrival by the time provided by the random generator block.

3.2.1.2. Port block. It represents the physical area where the download of the crude oil from the tanker is performed. Made of standard Extend blocks, it is a block that performs various simple operations, namely keeping track of tanker arrivals as a First In First Out (FIFO) queue, generating the flow of crude oil lots to make the system animation evolve smoothly according to the tanker load, the pump flow capacity and the user-defined animation step. In other words, the port block receives an item corresponding to a tanker in the input and produces a sequence of items corresponding to crude oil lots in the output in order to allow to the user the desired visual control over the discrete event system evolution.

3.2.1.3. End block. This block is responsible for the release of the item associated with the tanker when the downloading operations are completed.

3.2.1.4. Router block. This is one of the most important blocks of the system. According to the crude oil type, this block was able to route it to the assigned tank. The automatic/manual configuration is set up in the dialog of this block, and whenever the automatic mode is selected, the allocation strategy that must be used should be specified.

## 3.2.2. The tank storage subsystems

The system includes two tank storage subsystems, one at the port and the other at the refinery site, each of which is made up of a number of tank blocks that have been implemented as new elementary blocks.

The main parameters that characterise a tank block (Fig. 4) are:

 the crude oil type assigned to the tank,

 the crude oil level and  the maximum and minimum capacities (a tank cannot be safely emptied without an appropriate set-up procedure).

![](/api/attachments/RA2BVHVB/fulltext/images/4de235dd288abdf05592fa3d898a30710f934d315991856f655206156de92a79.jpg)  
Fig. 4. The tank block.

Different colours are associated with the tanks to highlight the tank state: green if crude oil is being pumped from the tank, red if crude oil is being pumped to the tank and grey for temporarily inactive tanks.

## 3.2.3. The refinery plant subsystem

Taking crude oil from tanks as input, the refinery subsystem generates distilled oil that is the output of the system. A maximum of three tanks can be assigned as input, and for each of them, the definition of the crude oil flow rate has to be specified. The mix of different crude oil types can be automatically assigned by choosing the production of a specific distilled product (Fig. 5).

## 3.2.4. Virtual repository of unstored crude oil block

The unstored crude oil—that represents the amount of crude oil that could not be stored and, for example, must be sold to another company—plays an important role in the evaluation of the system’s performance and is thus virtually stored in a repository. This virtual repository is modelled as a virtual tank coloured in blue.

## 3.2.5. Control panel block

Although the model is hierarchically structured and all blocks can be browsed to inspect their sub-blocks, reaching the structure of a specific block can be quite complex. The control panel provides a dialogue box, which is divided into zones with a direct access to the blocks, which are important for the evolution and the customization of the DSS. This block is the core of the DSS user interface.

## 4. Results

The DSS has been tested on an actual small – medium crude oil refinery system (about 1000000 $\mathrm { m } ^ { 3 }$ of crude oil refined per year) with rather critical logistic constraints due to the environmental and geographic characteristics of the area. The refinery is located inland, about 50 km from the harbour area. A first set of five tanks is located in the refinery area, playing the role of direct input to distillation. Another set of four tanks is located in the harbour area and is used as the main repository of the crude oil discharged from the tankers. The second tank set is generally fed by the first one via an oil pipeline, which allows the transfer of one kind of crude oil at a time, thus requiring the identification of a suitable sequence of transfers that should be physically separated. However, a direct connection between the port jetty and the remote set of tanks is also possible and can be used only if strictly necessary as in this case where the pumping rate is reduced. The refinery production plant is always fed by the local set of tanks. Fig. 6 shows the

![](/api/attachments/RA2BVHVB/fulltext/images/df8933dad6ea31812a5f5ff9cf8ac0294f43d94580d25bbf1091891e944c8968.jpg)  
Fig. 5. The refinery plant subsystem.

![](/api/attachments/RA2BVHVB/fulltext/images/25749ea60e2ddc187a0233b7f9023741ebc8f770e0b37967bffc8678cc9db3b8.jpg)  
Fig. 6. The small – medium-sized refinery layout on which we have tested the system.

Extend system layout on which we have tested our DSS. In this figure, the six main system components can be recognized. These are (in left to right and top– down order) the harbour, the tank storage, the refinery plant, the control panel, the virtual repository and the two tank storage subsystems.

Three different crude oil types, low pour point, sweet and sour, can arrive to the refinery plant exclusively by ships (with a load capacity between 15 000 and 80 000 tons). These types should be kept segregated, but they can be transferred at the same rate.

In this context, we have tested the system under several different conditions. Here, we report the most significant results obtained, validating the system as:

 a simulator of the physical system, where we have calibrated and verified the accuracy of the model, comparing it with real historical data;

 a learning support, where experts have tested the possibility to follow different strategies and to compare them with previously made real decisions; and

 a DSS, where we have tested the possibility to implement automatic decision policies in the system.

## 4.1. Model validation as a simulator of the physical system

We first validated the accuracy of the model on the basis of a set of historical data collected by the company. The purpose of the validation tests was to verify whether the model was able to follow the evolution of the real system.

The CO-2-PRT allocation model was tested upon 1 year of historical data, which included the arrival of 25 tankers. These data include the level of the tanks and the crude oil types at the beginning of each working day and the transfer operations, which correspond to about 500 crude oil main transfers among the tanks.

Table 1  
Initial state of the tanks

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Sour</td><td>12764</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Sweet</td><td>8386</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>15901</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sour</td><td>433</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>8218</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Sweet</td><td>1132</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Sweet</td><td>9068</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>56812</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>60500</td><td>61871</td></tr></table>

Table 2  
State of the tanks at the end of the discharge of tanker 1

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Sour</td><td>16111</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Low pour point</td><td>16124</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>15901</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sweet</td><td>12355</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>11282</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Low pour point</td><td>14605</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>28259</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>21703</td><td></td><td></td></tr></table>

In correspondence to each tanker arrival, we reproduced the same real sequence of operations, both transfers and refinery feedings, in order to force the model to follow the evolution of the real system. The results obtained at the end of the unloading of each tanker were quite accurate since a mean difference in the tank levels of about 1% was measured between the simulated and the real systems. This difference was considered as acceptable and it could be yielded by several factors: in the real system, there are some temporal latencies between consecutive operations which were not taken into account in the model, such as the difference in the starting time of the pumping operations due to human factors.

Table 3  
State of the tanks at the arrival of tanker 2

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Low pour point</td><td>16111</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Sour</td><td>1938</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>1801</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sour</td><td>9514</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>1318</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Sour</td><td>317</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>11448</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>21703</td><td></td><td></td></tr></table>

Table 4  
State of the tanks at the end of the discharge of tanker 2

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Low pour point</td><td>8111</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Sour</td><td>1938</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>16048</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sour</td><td>16282</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>7231</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Sour</td><td>14605</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>61871</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>21703</td><td></td><td></td></tr></table>

## 4.2. Model validation as a learning support

We validated our system as a learning tool. Actually, in the considered context, an exhaustive set of predefined rules that enables decision makers to take the most suitable decisions in different situations cannot be identified. The skill acquired by decision makers during a long daily experience cannot always be easily transferred to inexperienced personnel as a set of formal rules, and a long time on field training is usually needed. Furthermore, a direct learning from possible mistakes is obviously undesirable. For these reasons, the possibility of generating different scenarios corresponding to different sequences of crude oil arrivals and allowing personnel training are greatly appreciated. Specifically, the characteristics allowing personnel training are the following.

. Learning by previous errors: to analyse the decisions really taken in the past in order to test possible alternatives with better performances.

. Learning by hypothesis: to test different what-if scenarios both in the current structure of the industrial plant (for example, the effects of the introduction of a new tank) and in the current planning of tanker arrivals in the short to mid-term (for example, the purchase of a new tanker).

We tested several possible configurations and the users particularly appreciated the training features. A meaningful example is presented here, namely the simulation of a real situation where a tanker load was completely sold. This could have been avoided with a different solution to the CO-2-PRT allocation problem.

The situation considered includes three tanker arrivals within 1 month. Tanker 1 is loaded with $5 3 9 3 8 \ \mathrm { m } ^ { 3 }$ of low pour point crude oil. Tanker 2 is loaded with $9 1 6 3 9 ~ \mathrm { { m } } ^ { 3 }$ of sour crude oil. Tanker 3 is loaded with $1 1 8 3 5 \ \mathrm { m } ^ { 3 }$ of sweet crude oil. Table 1 reports the state of the reservoirs at the beginning of the period of observation, whereas Table 2 reports the state of the reservoirs at the end of the discharge of tanker 1 in the real system. Table 3 reports the state at the instant of tanker 2 arrival: this table has been included to show that the state may be different from the one in Table 2 due to several reasons (for example, the plant has refined some of the oil stored in the tanks, some of the oil has been transferred between the tanks, etc.). Tables 4 and 5, respectively, report the state at the end of discharging tanker 2 and tanker 3 (corresponding to the final system state). This simulation effectively reproduced the real system where the oil load of tanker 1 was partially sold (40%), tanker 2 was completely discharged and tanker 3 was completely sold.

State of the tanks at the end of the discharge of tanker 3 (the final state of the simulation)

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Sour</td><td>16111</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Sour</td><td>16214</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>16048</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sour</td><td>16282</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>11282</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Sour</td><td>14605</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>61871</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>21703</td><td></td><td></td></tr><tr><td>Sold sour</td><td></td><td>0</td><td></td><td></td></tr><tr><td>Sold sweet</td><td></td><td>11835</td><td></td><td></td></tr></table>

Table 6  
State of the tanks at the end of the discharge of tanker 1

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Sour</td><td>16111</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Low pour point</td><td>16124</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>15901</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sweet</td><td>12355</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>11282</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Low pour point</td><td>14605</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>28259</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>4594</td><td></td><td></td></tr></table>

Considering the same initial system state, sequence of arrivals and requirements of crude oil feeding in the same time interval, we tested different sequences of operations in order to enhance the objective of reducing the amount of sold crude oil (that is, the most relevant criteria considered in this context). Here, we report the alternative operation sequence that was judged to be the most effective by domain experts. In particular, Tables 6–8 describe the state of the tanks after the discharge of tankers 1–3, respectively.

As can be observed, the improvement achieved with the alternative sequence can be quantified in the following way.

With the real sequence, 21% of the total crude oil supplied was sold, whereas only 11% of the total was sold with the simulated sequence.

The amount of the sold crude oil of tanker 1 was reduced from 40% to 9%; for tanker 2, it was raised from 0% to 14%; and for tanker 3, it was discharged in full instead of being sold.

Table 7  
State of the tanks at the end of the discharge of tanker 2

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Sweet</td><td>1823</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Low pour point</td><td>8214</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>16048</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sour</td><td>16282</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>11282</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Low pour point</td><td>14605</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>61871</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>4594</td><td></td><td></td></tr><tr><td>Sold sour</td><td></td><td>13070</td><td></td><td></td></tr><tr><td>Sold sweet</td><td></td><td>0</td><td></td><td></td></tr></table>

Table 8  
State of the tanks at the end of the discharge of tanker 3 (the final state of the simulation)

<table><tr><td>Tank ID</td><td>Site</td><td>Crude oil type</td><td>Available oil [ $m^3$ ]</td><td>Available capacity [ $m^3$ ]</td></tr><tr><td>S1</td><td>Refinery</td><td>Sweet</td><td>13658</td><td>16111</td></tr><tr><td>S2</td><td>Refinery</td><td>Low pour point</td><td>8214</td><td>16214</td></tr><tr><td>S3</td><td>Refinery</td><td>Sour</td><td>16048</td><td>16048</td></tr><tr><td>S4</td><td>Refinery</td><td>Sour</td><td>16282</td><td>16282</td></tr><tr><td>S5</td><td>Refinery</td><td>Sour</td><td>11282</td><td>11282</td></tr><tr><td>S102</td><td>Port</td><td>Low pour point</td><td>14595</td><td>14595</td></tr><tr><td>S105</td><td>Port</td><td>Low pour point</td><td>14605</td><td>14605</td></tr><tr><td>S109</td><td>Port</td><td>Low pour point</td><td>60979</td><td>60979</td></tr><tr><td>S112</td><td>Port</td><td>Sour</td><td>61871</td><td>61871</td></tr><tr><td>Sold low pour point</td><td></td><td>4594</td><td></td><td></td></tr><tr><td>Sold sour</td><td></td><td>13070</td><td></td><td></td></tr><tr><td>Sold sweet</td><td></td><td>0</td><td></td><td></td></tr></table>

## 4.3. Model validation as a DSS

One of the main advantages of the support system is that it can provide guidance to the decision makers by proposing the CO-2-PRT allocation plans generated by heuristic decision policies. Since end-users always like to have full control of the system, the use of fully automatic policies seems more appealing for applications of personnel training rather than as an operative tool. In our opinion, using a ‘‘black box’’ approach for short/mid-term decisions is useless for both an expert and a young planner. On the other hand, if the DSS policies can be easily described, they can be useful to analyse their effects.

This is the case of the two policies that were introduced in Section 3.1. We verified them using the same testing conditions as for the validation described in Section 4.2 and by comparing the results to those previously reported. The quantity of sold oil at the end of both policy simulations (Max and Min ACF) was 49 771 $\mathfrak { m } ^ { 3 }$ (92% of Low Poor Point of tanker 1) and was greater than the two previous simulations even though only one type of oil has been sold.

Table 9 compares the different strategies with the results obtained for the real operation sequence and the alternative one whose effects were shown in Section 4.2, reporting the values obtained in the real case for the six different objectives indicated in Section 2, as well as the values of the simulated cases. More specifically, the results obtained in correspondence of the discharge of the three ships are shown for objectives 4 and 5 and are indicated by the ship number in brackets. In Table 9, the values of $O _ { 4 \mathrm { b } }$ and $O _ { 5 }$ for ship 3 are not computed since the ship’s load was completely sold. Finally, the average values for objectives $O _ { 4 \mathrm { a } }$ and $O _ { 4 \mathrm { b } }$ are reported.

As can be observed from Table 9, the alternative strategy generally shows better performances than the one really used, whereas the Max and Min ACF strategies both had poorer performances. These two latter automatic strategies performed quite similarly for the considered case and, in particular, they provided the same value for the most important objective $O _ { 1 }$ . However, the performance of the Max and Min ACF strategies may ultimately depend on the sequence of load arrivals: for example, we verified that by changing the sequence used for all the previous validation tests so that tanker 2 with a larger load arrives first, the Max ACF strategy yields a better $O _ { 1 }$ performance.

Table 9  
The evaluation of the different strategies according to the objective defined in Section 2

<table><tr><td colspan="2"></td><td>Real</td><td>Alternative</td><td>Max ACF</td><td>Min ACF</td></tr><tr><td>Sold oil</td><td> $O_{1}$ </td><td>33538</td><td>17664</td><td>49771</td><td>49771</td></tr><tr><td>Setups</td><td> $O_{2}$ </td><td>7</td><td>6</td><td>0</td><td>0</td></tr><tr><td rowspan="7">Transfers</td><td> $O_{3}$ </td><td>8</td><td>8</td><td>3</td><td>3</td></tr><tr><td> $O_{4a} (1)$ </td><td>11848</td><td>12559</td><td>13397</td><td>13482</td></tr><tr><td> $O_{4a} (2)$ </td><td>15687</td><td>15769</td><td>14293</td><td>14058</td></tr><tr><td> $O_{4a} (3)$ </td><td>16415</td><td>16111</td><td>14638</td><td>14368</td></tr><tr><td> $O_{4b} (1)$ </td><td>57616</td><td>47552</td><td>140713</td><td>143927</td></tr><tr><td> $O_{4b} (2)$ </td><td>40332</td><td>51424</td><td>34718</td><td>34718</td></tr><tr><td> $O_{4b} (3)$ </td><td>/</td><td>217534</td><td>185427</td><td>185427</td></tr><tr><td rowspan="3">Tanks×ship (i)</td><td> $O_{5} (1)$ </td><td>3</td><td>4</td><td>1</td><td>1</td></tr><tr><td> $O_{5} (2)$ </td><td>5</td><td>4</td><td>5</td><td>5</td></tr><tr><td> $O_{5} (3)$ </td><td>/</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Feeding tanks</td><td> $O_{6}$ </td><td>12</td><td>11</td><td>9</td><td>10</td></tr><tr><td>Average  $O_{4a}$ </td><td></td><td>14650</td><td>14813</td><td>14109</td><td>13969</td></tr><tr><td>Average  $O_{4b}$ </td><td></td><td>48974</td><td>105503</td><td>120286</td><td>121357</td></tr></table>

## 5. Conclusions

In this paper, the main characteristics of a system for modelling, testing and supporting the decisions for the allocation of the crude oil to the port and refinery tanks of an oil company have been presented. As discussed, several reasons motivate the use of a simulation model for the proposed system, one of which is the possibility to use it for different goals. For example, the off-line use of the DSS as a learning/training support tool (e.g., to test different what-if scenarios and decision rules)—an aspect often neglected in the DSS literature—has been particularly appreciated. In addition, the opportunity to model the CO-2-PRT allocation problem as an MIP problem has been considered and discussed. However, the simplifications that must be introduced to yield a workable model and the difficulties that decision makers must interact with, prompted us to consider a simulationbased DSS that is more likely to be accepted by the managers of oil companies.

The proposed DSS allows the verification of the consequences of decisions about the CO-2-PRT allocation problem before the actual arrival of tanker ships in order to optimise several performance factors that have a direct influence on the production and management of the oil company. Specifically, the system aims at reducing the quantity of crude oil that the company must sell because it is unable to store it. Taking into account the sequence of tanker arrivals, the DSS provides company managers with a tool for defining an allocation policy for time intervals that exceed a day-by-day policy.

In its current version, the DSS includes two simple heuristic policies to select the tanks to be used to discharge a tanker, and it is possible to improve it by introducing new, more complex, discharging and allocation rules.

In the paper, some results have been provided from the test of the DSS on a small –medium refinery company with limited storage facilities. As the results highlight, the DSS actually allows the determination of different solutions for the CO-2-PRT allocation problem that outperform the solution identified by the company decision makers. This fact is particularly true whenever the operational conditions become critical as for the cases in which the company managers decide to sell a tanker load in order to avoid a drastic reduction of the storage capability of the system: it is not rare that in such critical situations, a load is entirely sold to avoid decisions that could become too constraining for the management of future arrivals. The possibility to experiment more strategies in advance, extending the effect of decisions to the future, is a utility that was greatly appreciated by company managers.

As already noted, the two simple tank selection policies used to automatically generate the solutions are quite far from actually assisting decision makers, and they can currently be considered as a support tool for the management of ordinary situations instead of critical ones. However, these policies represent a starting point for the study of more complex strategies that can provide decision makers with solutions that are both feasible and acceptable.

## References

[1] J. Banks, J.S. Carson, B.L. Nelson, Discrete Event System Simulation, Prentice-Hall, NJ, 1996.

[2] M.C. Fu, Optimization via simulation, Annals of Operations Research 53 (1994) 199– 247.

[3] H. Lee, J.M. Pinto, I.E. Grossmann, S. Park, Mixed-integer linear programming model for refinery short-term scheduling of crude oil unloading with inventory management, Industrial & Engineering Chemistry Research 35 (1996) 1630 – 1641.

[4] G.M. Marakas, Decision Support Systems in the Twenty-First Century, Prentice-Hall, NJ, 1999.

[5] J.M. Pinto, M. Joly, L.F.L. Moro, Planning and scheduling models for refinery operations, Computers & Chemical Engineering 24 (2000) 2259–2276.

[6] N. Shah, Mathematical programming techniques for crude oil scheduling, Computers & Chemical Engineering 20 (1996) 1227 – 1232(Suppl.).

[7] G.R. Stahl, J.C. Elliott, ‘New generation’ computer models for risk-based water planning and management, Water Supply 17 (3) (1999) 289– 295.

[8] J. Wahle, O. Annen, Ch. Schuster, L. Neubert, M. Schreckenberg, A dynamic route guidance system based on real traffic data, European Journal of Operational Research 131 (2) (2001) 302– 308.

![](/api/attachments/RA2BVHVB/fulltext/images/e9a94c324048a879cb3473d1724c2dff722c827bf74540f8701c1e6d23678ce2.jpg)

Massimo Paolucci received his PhD in Electronic and Computer Science at the Department of Communications, Computer and Systems Sciences (DIST) of the University of Genoa in 1990. Currently, he is working as an assistant professor at DIST. He worked in the fields of knowledge representation, in particular dealing with the problem of the treatment uncertainty in expert systems, decision support systems and multi-attribute decision making. His

main research interests are focused on operational research problems relevant to the logistics and industrial automation as well as the environment. In addition, he is also involved in research activities on information systems and database. His professional experiences have been mainly carried out in the field of database management and design.

![](/api/attachments/RA2BVHVB/fulltext/images/1438c363ccffef17a05a6d4f5d290ffc9f72087fb20aaad2af102de6ff47c68a.jpg)

Roberto Sacile received a Laurea degree in Electronics Engineering in 1990 at the University of Genova and a PhD in 1994 at Politecnico of Milan. He is currently an assistant professor at the Faculty of Engineering of the University of Genova, handling the courses of ‘‘Fundamentals of Computer Science’’ and ‘‘Geographic Information Systems.’’ His research interests focus on decision support systems and agent technology with special reference to their integration and application to territorial and geographic information systems, environmental monitoring and protection, manufacturing information systems and health care systems. He is the author of more than 100 technical papers in refereed journals and conferences.

![](/api/attachments/RA2BVHVB/fulltext/images/96e13c678f49744dfc10a1806fa1fc8af5dc9fe62e700eddbc3df209a7392565.jpg)

Antonio Boccalatte is a professor of «Database Management Systems» at the Faculty of Engineering. He is the author of more than 70 scientific papers presented at international congress or published on international revues. His research interests include the following.

<sup>.</sup> System architecture and artificial intelligence: Particularly related to the study of data flow and multiprocessor

architectures. He had also published international papers on scheduling algorithms, fault-tolerant architectures and fault-tolerant operating systems. He also worked on natural languages and scene recognition.

Decision support systems and database: Design and development of graphical user interface for decision support systems and on the integration of relational database with DSS. Scheduling algorithms for medium and short-term production in a production environment based on orders. Use of object-oriented programming and Petri Nets for information system modelling and development.
