---
otero_id: 12818
otero_key: "JA2AAEVB"
title: "Energy-aware decision support for production scheduling"
authors: "Stathis Plitsos; Panagiotis P. Repoussis; Ioannis Mourtos; Christos D. Tarantilis"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.09.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Energy-aware decision support for production scheduling<sup>-,--</sup>

Stathis Plitsos<sup>a,</sup>\*, Panagiotis P. Repoussis<sup>b,</sup> <sup>c</sup>, Ioannis Mourtos<sup>a</sup>, Christos D. Tarantilis<sup>a</sup>

<sup>a</sup>Athens University of Economics and Business, Department of Management Science & Technology, 76 Patision Avenue, Athens 10434, Greece <sup>b</sup>Athens University of Economics and Business, Department of Marketing & Communication, 76 Patision Avenue, Athens 10434, Greece <sup>c</sup>Stevens Institute of Technology, School of Business, 1 Castle Point on Hudson, Hoboken, NJ 07030, USA

## A R T I C L E I N F O

Article history: Received 27 October 2015 Received in revised form 7 July 2016 Accepted 19 September 2016 Available online xxxx

Keywords: Energy-aware production scheduling Job-shop Parallel machines Local search Hierarchical optimization Textile industry

## A B S T R A C T

Manufacturing companies are forced to become energy-aware under the pressure of energy costs, legislation and consumers’ environmental awareness. Production scheduling remains a critical decision making process, although demanding in computational terms and sensitive on data availability and credibility. Hence the interest in incorporating energy-related aspects in production scheduling. We propose a decision support system (DSS), composed by an Iterated Local Search algorithm that offers hierarchical optimization over multiple scheduling objectives and is energy-aware in terms of both the constraints incorporated and the objectives to be optimized, plus a generic yet concise data model whose entities are extracted from the literature and actual user requirements. The use of this DSS by two textile manufacturers shows that i supports eficiently energy-aware scheduling decisions.

© 2016 Elsevier B.V. All rights reserved

## 1. Motivation

Public and industry concerns over energy eficiency and environmental sustainability have grown considerably over the last decade. Particularly in the industrial sector, energy eficiency becomes an even more important pillar since it accounts for more than one third of energy consumption worldwide [1] of which the manufacturing sector accounts for about 73%. Despite these numbers, industrial practices towards energy-eficient manufacturing have traditionally been viewed as a ‘cost of business’, and positioned as the voluntary responsibility of companies. Nowadays, this perception is changing as stricter legislation, industrial standards and energy costs require that companies not only adopt a strategy of minimal compliance, but also treat such a strategy as a catalyst for sustainable practices. Furthermore, consumers are becoming increasingly aware of whether the product they purchase comes from a sustainable source and is produced through eco-friendly methods that, ideally, guarantee minimum environmental impact [2]. Betraying the consumer’s confidence can damage a company and its brand image [3]. Altogether, legal compliance, energy costs and customers increasing ecological awareness [4] are driving companies towards measurable energy improvements, thus strongly motivating our research effort.

Although the manufacturing sector has advanced towards energy eficiency, the derived economic benefits have not been fully exploited [5]. Both academic and business studies indicate that there is an “energy eficiency gap” and highlight that there are strong barriers that impede energy-eficient manufacturing. Systems supporting relevant decisions can help minimize these barriers by monitoring energy consumption and carbon emissions, thus pinpointing areas for savings [6] as a basis for energy-based optimization and intelligent decision making. Several enterprise systems have been enhanced by energy management capabilities, although typically limited to energy monitoring, analysis and reporting [4]. These Energy Management Systems (EMS) do not support management decisions in a coherent way due to a lack of integration of information from shop-floor to top-floor [7]. Apparently, apart from the gap between industrial needs and the academic literature [4,8], there is also a gap between the solutions available and the support of sophisticated decision making such as production scheduling [9].

Indeed, scheduling is an important decision-making process in manufacturing that drills down to deciding on (i) which tasks to execute, (ii) where to process the production tasks and in which sequence and (iii) when to execute the production tasks. Typically these decisions are strongly coupled, thus ideally to be taken simultaneously [10]. Due to the complexity and the increasing production volumes, such decisions cannot be addressed without an automated optimization support. This functionality is typically considered part of a Manufacturing Execution System (MES) [10] and is normally supported by an Enterprise Resource Planning (ERP) system through data exchange. Still, scheduling remains computationally complex and data intensive, because it requires not only production data but also the availability status of machines, personnel or energy resources, possibly in real-time. In fact, the more complex a scheduling system is, the more information to be collected and managed [10], and the more competitive the algorithms to be used for obtaining valid schedules of good quality.

Our study focuses on energy-aware flexible shop scheduling environments and is also motivated by the scarce optimization algorithms (and the limited background on the data required) for energy-aware support at the shop floor. The adopted production scheduling framework is as generic as possible and takes into account various operational aspects including constraints on energy consumption (e.g., electricity, gas) and personnel or machine availability. Assuming that a manufacturing process comprises several process steps, the machines of each step share and consume one or more energy resources; hence, relevant constraints can be imposed in one or more process steps, with the maximum level per resource varying across the scheduling horizon (e.g., as implied by flexible electricity pricing). The goal is to find the optimum schedules under different scenarios of resource constraints, accounting for the minimization of both direct and indirect energy consumption.

The Iterated Local Search (ILS) used here introduces new compound moves and an adaptive perturbation mechanism to optimize over energy or temporal scheduling criteria. Energy-related criteria include the total energy consumed by machines during production and idle time (direct energy) along with the energy consumed by subsidiary equipment (indirect energy). Temporal criteria include the makespan, the total flow time and the total machine idle time. We note that even temporal criteria target implicitly both the direct and indirect energy consumption. That is, minimizing the makespan increases throughput and reduces the number of shifts thus reducing the indirect energy consumption (e.g., heating); minimizing total flow time reduces production time, hence the direct energy consumption (e.g., machine gas consumption); and minimizing total idle time reduces the energy consumed by machines in idle mode.

Our ILS algorithm can optimize over any subset of these criteria in a hierarchical manner. Indicatively, hierarchical optimization over the three temporal criteria appears both appropriate and suficient in our two pilots in textile manufacturing, because these end-users wish to target both energy and other production aspects like cost or personnel. What is critical in terms of DSS design is that our algorithmic and modeling approach remains versatile in terms of handling energy-awareness in the objectives to be optimized. Furthermore, by imposing time-varying restrictions on the energy consumption of machines, our algorithm provides schedules that alleviate energy peaks by distributing more ‘uniformly’ the consumption across time. Hence, energy-awareness in our cases amounts not only to energydriven optimization objectives but also to energy-consumption constraints.

However, even that does not sufice for an energy-aware DSS. To the best of our knowledge, an explicit description of the data entities supporting energy-aware production scheduling is at the moment not available, although scheduling-related entities were presented early enough (e.g., [11]). To identify these data entities, we formulate a set of user requirements as acquired from the academic literature and validated within the textile manufacturing domain. The algorithm is aligned with these entities and remains operative even if certain data (e.g., personnel availability) are missing

Overall, this paper contributes to decision support for energyeficient manufacturing by (a) a metaheuristic algorithm that hierarchically optimizes flexible shop scheduling problems, (b) a set of data requirements in the form of a data model, (c) the integrated deployment of the above as a web-service and (d) the evaluation of the proposed DSS in real settings and the tangible benefits obtained by its use.

The remainder of this paper goes as follows; Section 2 provide the background motivating our study. Section 3 presents the production scheduling problem followed by the user and data requirements plus the algorithmic scheme. Section 4 discusses the application of the proposed DSS along with implementation issues and Section 5 presents the evaluation and the benefits using data from a real context.

## 2. Background

It is being increasingly acknowledged that energy-intensive manufacturers need tools and methods to optimize their processes by considering energy-related criteria [4]. Indicatively, accurate changes on resources or processes can reduce energy usage [12]. Prior studies have been conducted to evaluate the energy-burden of different process steps [13] and then used as a roadmap to identify modifications in these steps; however, such modifications impose a significant investment because they involve radical changes in the manufacturing process [14]. A less costly alternative is the modification of production settings like the temperature of machines; although several studies focus on such changes [14], these changes usually concern specific processes and have side-effects such as lower product quality [8].

The optimization of energy use via production scheduling has received attention only recently. An early attempt formulates a multi-objective optimization problem for an electroplating line [15]. Another study has shown that up to 65% of the energy consumption comes from non-productive machine modes (e.g., stand-by or idling) [16]. Embedding energy aspects into scheduling can be tackled by both exact and heuristic approaches. Exact methods like mathematical programming obtain optimal solutions but require considerable time given that the job-shop and flow-shop scheduling problems are -hard [17]. Indeed, by integrating energy constraints in a set of 100 instances, Artigues et al. [18] show that the solution time for a mixed integer programming model is high. This is also outlined by Fang et al. [19] by testing an exact method against heuristic algorithms to minimize the makespan, the peak consumption and the carbon footprint of the production process.

Metaheuristic methods trade optimality for time, i.e., they provide high-quality solutions within reasonable time. Their current state-of-the-art for production scheduling algorithms includes genetic and hybrid evolutionary algorithms [8,20]. Indicatively, Shrouf et al. [21] focus on scheduling on a single machine, taking into account the variable energy cost during daytime, and use a genetic algorithm. Rager et al. [20] use a combination of genetic and memetic algorithms to acquire schedules minimizing the energy demand of multiple parallel machines by first splitting production orders into operations that have constant energy demand; this results in a schedule defined by the underlying ‘identical parallel machine’ environment and the resource-leveling objective. Notably, the approach of Rager et al. [20] has been tested in textile manufacturing, i.e., the dying stage of yarns.

The problem addressed here is more generic: it includes various operational constraints (e.g., parallel unrelated machines, sequencedependent set-up times) and is applicable with minor modifications to most shop scheduling environments with multiple process steps. Also, the proposed algorithm incorporates novel local search components and re-start mechanisms to escape from local optima. Moreover, this algorithm performs hierarchical optimization over multiple objectives, i.e., energy-related (total energy) and temporal ones (makespan, total flow time and total idle time). Let us note that hierarchical optimization in manufacturing typically covers two criteria [8,19,20] and has never targeted total idle time in a hierarchical fashion; an approach that covers three criteria appears in the human resources allocation domain [22]. Another innovative feature of our algorithm is that it deals effectively with several (possibly time-varying) energy consumption constraints, thus encompassing the sharing of one or more renewable energy resources (e.g., electricity, gas, steam) by multiple parallel machines.

To identify the entities that build up the data model, we collect relevant requirements for production scheduling from the literature [10] and validate them from requirements extracted from the two textile manufacturers that are the end-users of our DSS plus several other textile producers (mostly SMEs). Then, we utilize the framework of Zampou et al. [9] regarding the integration of data from enterprise systems (ERP, MES, EMS) and offer a coherent data model for energy-aware production scheduling. Let us again note that the proposed algorithm is insuficient if not relying on appropriate data, and vice-versa: the data entities to be incorporated in our data model are selected exactly because they are required for supporting scheduling decisions.

## 3. Problem definition, data requirements and the algorithm

This section presents the modules of the proposed DSS, namely the scheduling problem with resource constraints (Section 3.1), the data requirements (Section 3.2) and the ILS algorithm (Section 3.3).

## 3.1. Energy-aware production scheduling problem with resource constraints

Production scheduling can be defined as the allocation of available production resources over time to perform a series of activities. Suppose that a set of unrelated parallel machines $M _ { j } ( j = 1 , \ldots , m )$ have to process a set of production orders or jobs $J _ { i } ( i = 1 , \ldots , n ) .$ Each job i has a release date, a due date and consists of a k number of operations $O _ { i 1 } , \ldots , O _ { i k _ { i } }$ , while each operation $O _ { i j }$ is associated with a subset of machines $\mu _ { i j }$ and a machine-dependent processing time $p _ { i j } .$ At any time, each job can be processed by at most one machine and each machine can process at most one job.

Once a job is processed on a machine, it cannot be interrupted before completion. Additionally, whenever a machine finishes the processing of an operation, a set-up (changeover) time occurs before processing the next operation/job. The length of the set-up can be sequence dependent (i.e., the set-up depends on the job just completed and on the one about to be started) and/or machine dependent (with or without a predefined frequency). Overall, the objective is to find a sequence for the processing of the jobs in the machines so that a given objective function is optimized. A schedule is for each job an allocation of one or more time intervals to one or more machines. To that end, the associated scheduling problem is to find a schedule that satisfies a given set of precedence restrictions among the operations of each job and respects its due and release dates.

The above production scheduling problem can be formalized as flexible multi-processor job-shop scheduling problem with unrelated parallel machines, due dates, and set-up times that depend on both the job sequence and the machine. There is significant research work on production scheduling problems with parallel machines and makespan minimization [23] but significantly fewer for unrelated parallel and sequence-dependent set-up times. Note that minimizing the makespan on already two identical machines is -hard. We refer to Rocha et al. [17] for mixed integer mathematical formulations as well as exact and metaheuristic solution approaches.

Additionally, we consider machine availabilities, shifts and energy resource constraints in our framework. Regarding the former, each machine is coupled with a number of qualified employees. There are three shifts per day, while the person-shift allocation plan is known in advance. Hence, based on this employees’ qualifications and the available personnel per shift, one can determine the machine availability during the scheduling horizon.

Furthermore, we assume that machines consume one or more energy resources, e.g., electricity, gas or steam. The consumption is directly related with the time elapsed, and may also depend on the machine mode, i.e., start-up, clean-up, stand-by and production mode. We consider the time spent during the first three modes, as ‘idle time’, which practically is a necessary, yet non-productive time. The amount of energy consumed by machines is considered as direct irrespectively of whether the machine is in idle or production mode; i.e., we differentiate between ‘direct productive’ and ‘direct idle energy, but both types are consumed directly by production machinery in the shop floor. However, there may also exist additional subsidiary energy-consuming equipment (e.g., air-conditions) in a shop floor related to the production process. As described in Zampou et al. [9], although these amounts of consumed energy are indirect, they are important and should be taken into account. Energy-aware production scheduling is expected to minimize both direct and indirect energy consumptions, while the restriction of energy peaks can be achieved by adding resource consumption constraints.

There are two types of objectives. Regarding the first, if we denote as $P _ { p r o d u c t i o n }$ the total energy consumed by machines during production time, as $P _ { i d l e }$ the one consumed by machines during idle time and as $P _ { i n d i r e c t }$ the energy consumed by subsidiary equipment, the objective to be minimized is total energy denoted as $P _ { t } = P _ { p r o d u c t i o n } +$ $P _ { i d l e } + P _ { i n d i r e c t }$ . The second type includes three temporal scheduling criteria, namely the makespan $C _ { m a x } ,$ , the total flow time (F ) and the total idle time $D _ { t } .$ . Any subset of these four objectives can be minimized hierarchically. Let us mention once more that temporal criteria are also related to energy consumption, e.g., the minimization of the makespan is expected to maximize the utilization of machines [19] and reduce the required shifts, thus also reducing P<sub>indirect</sub>.

In the remainder of the paper, we use the notation f g h to indicate the optimization hierarchy. For example, the $C _ { m a x } | F _ { t } | D _ { i }$ indicates that $C _ { m a x }$ is the primary objective, $F _ { t }$ is the secondary objective and $D _ { t }$ is the last objective in consideration; in a similar manner $P _ { t } | C _ { m a x }$ indicates that the primary objective is the total energy followed only by the makespan.

## 3.2. Data requirements & information flows

Production scheduling refers to several data entities, including the machines, the employees and the production orders. Indeed, such entities have been proposed in the production management literature from early on [11] until recently [24] or in the simulation literature [25], without however incorporating energy-related data.

Introducing energy-awareness in production scheduling implies including energy-related data in the data model, hence the entities proposed here can be classified into three information flows (see also [9]):

Operational flow: information regarding productions orders, the types of products and the materials used for each product.

Production process flow: information regarding the production processes, such as machines, process steps, production orders tracking.

Energy consumption flow: information regarding energy consumption measured by energy sensors or provided by energy audits.

Based on the description of the problem in Section 3.1 and the above flows, our proposed data model is shown in Fig. 1. We use blue color for operational, red for production process and green for energy consumption entities; black color distinguishes operational entities that are used only for scheduling. A detailed description is provided in Appendix A. Although the entities in this model refer to data existing already in ERPs, MESs or EMSs, its novelty is the combination of these flows as a prerequisite for supporting energy-aware scheduling decisions.

## 3.3. Iterated local search algorithm

ILS is a perturbation-based multi-restart local search metaheuristic algorithm introduced originally by Lourenço et al. [26], in which the initial solutions for local search are generated by perturbing local optimum solutions obtained during previous searches. Our implementation originates from a starting solution s, local search is initially applied until a local optimum solution s∗ is found. At this point, a random perturbation is applied that leads to an intermediate state s. Local search is triggered starting from s until a local optimum solution s is reached. If s improves s∗, then it becomes the next solution for local search; otherwise, the procedure is restarted from a new starting solution s. The oscillation between perturbation and local search is repeated for a number of iterations.

A sequential insertion-based construction scheme is adopted to generate starting heuristic solutions. At each iteration, one operation is selected and added in the permutation of a machine. The rule followed is to schedule the operation as early as possible. All available machines and all feasible insertion positions (with respect to machine availabilities, release and due dates, precedence relationships and resource constraints) for each operation are examined. The main effort is to schedule the operation that performs best with respect to the hierarchy of objectives. Based on this greedy criterion, a restricted candidate list of positions at the available machines is generated for each operation, and one position from this list is selected randomly. Note that every iteration the actual schedule partially constructed solution is updated.

An iterative improvement local search scheme is employed. In particular, the solution neighborhoods are generated by applying the relocate and exchange operators [27] on a representation based on the permutation of operations on the machines. Equal selection probability is assumed for each operator, while a best admissible strategy is followed for moving in the solution space. For the evaluation of the neighborhoods, a lexicographic search scheme has been developed that considers all feasible inter and intra machine move combinations. The main effort of this scheme is to expedite the process by avoiding unnecessary feasibility checks.

Lastly, a ‘ruin-and-recreate’ mechanism is applied for perturbation. In particular, a number of jobs is randomly removed from the schedule and the greedy randomized construction scheme described above is applied to reschedule them. The number of the rescheduled jobs is determined by a self-adapted length that is regulated based on the search progress.

## 4. Energy-aware production scheduling in the textile industry

In this section we describe the implementation details of the proposed DSS as part of the ARTISAN system [28], whose aim is the reduction of the energy use in textile manufacturers. The ARTISAN system integrates data from several enterprise systems and from real-time energy monitoring to assist the enterprises in reducing the total energy consumption through monitoring energy consumption per production order and also through energy-aware production scheduling. The entire ARTISAN system, including the DSS presented in this paper, has been installed and tested in two industrial partners, a small-to-medium enterprise (SME) focusing on the production of yarns and a large-size enterprise (LSE) with a vertical production line.

## 4.1. Decision support in the textile industry

Energy audits on the premises of the industrial users have shown that the most energy-consuming process in the textile manufacturing chain is the finishing mill. Hence, this particular process is to be optimized. In ARTISAN, the finishing mill is modeled as a multi-step production flow shop facility, where a production step is made up of one or more related and/or unrelated parallel machines (also called ‘machine groups’). The term ‘job’ refers to a production order and a product is also called an ‘article’. The speeds, capacities and programs/settings of the machines are known and they may depend - among others - on the articles and the process quantities (lot size). In addition, set-up times and costs are incurred (changeover time/cost) when machines have to be reconfigured and/or cleaned between operations on different articles. The length of the set-up can be sequence dependent or machine dependent.

Each machine directly consumes one or more limited resources, namely electricity, gas, steam, water and compressed air, that should not exceed certain thresholds per certain groups of machines or for the entire process. Steam is produced by a continuous steam production unit, while water is heated by a gas-powered combined heat and power unit. Both of them have a predefined capacity limitation. Regarding electricity, cost profiles as well as maximum capacities for different hours per day are provided. Additionally, limitations may also occur in terms of drainage or rinse water. Furthermore, there is indirect energy consumption from auxiliary energy conservation installations, each installation being associated to one or more machines or process steps. Let us observe that this production environment fits perfectly with the job-shop problem described in Section 3.1.

Regarding the optimization criteria, although total energy is important to be minimized, the energy consumed during machine idle time has been pointed out as critical by the experts (production engineers, floor managers, energy auditors) of the textile manufacturing domain in the context of the ARTISAN research project (see also [16]). This arises from the fact that machines cannot easily be shut down and then restarted in order to avoid energy consumption while producing nothing, while the energy consumption of several machines remains considerable even if idle. However, minimizing only the total idle time may increase the makespan (thus increasing production cost), although what a manufacturer seeks is the minimization of total direct and indirect energy consumed while sustaining cost. Consequently, the hierarchical minimization of the scheduling criteria described in Section 3.1 (even just the temporal ones) is, apart from a technical novelty, also a mandatory requirement.

## 4.2. User requirements and system functionality

Beyond the problem characteristics and the operational aspects, various user requirements have been taken into consideration. Although these requirements have been collected from the textile manufacturing domain, they are also identified as basic user requirements from the academic literature [10]. Specifically, a production scheduling software should provide schedules for short-term periods or for a specific subset of process steps and production orders (‘narrow scope’ schedules, as described by the end-users), along with master schedules for longer periods of time that affect all production orders in that period and all process steps (‘middle scope’ schedules). It is important that the user reviews such schedules and selects among several “simulated” schedules the one to be implemented in the shop floor. For each schedule, the user wishes to alter provisionally the factory environment settings, e.g., the availability of a machine. When unexpected events occur, such as machinery malfunctions, re-optimizing the master schedule is necessary. Last, schedules are expected to be provided in a reasonable amount of time and presented in Gantt charts.

![](/api/attachments/JA2AAEVB/fulltext/images/a9305a9de81188fcd4d0987c03b727647e7f7584ee71926fc3730051997c5b69.jpg)  
Fig. 1. Data model. (For interpretation of the references to color in this figure, the reader is referred to the web version of this article.)

The proposed DSS has been implemented in the form of three services in the ARTISAN system. The first two services are titled “Resource Constraint Shop Floor Scheduling at the process level ”(narrow scope schedules) and “Resource Constraint Multiprocessor Shop Floor Scheduling ”(middle scope schedules); apart from their scope, a major difference between them is that the second takes into account cross-processing resource limitations and capacity thresholds across the process steps. The third service, titled “Reactive Shop Floor Scheduling ”(middle scope), aims at assisting the user to responsively adjust the planned production schedule due to the occurrence of unexpected disturbing events (e.g., machine breakdown). Its primary scope is the on-demand re-optimization of the current production schedule as new information arrives. Apart from ordinary static information, this last service can exploit real-time data related to the tracking of production orders or the consumption of energy resources.

## 4.3. Implementation details

The successful industrial application of the proposed DSS depends on resolving many practical issues when embedding this DSS in an actual system, such as ease of use, data availability, application development and maintenance.

Regarding the ease of use, after consulting with the end-users via the waterfall model, the work-flow of the proposed services has been shaped. Fig. 2 is the service blueprint of one service along with some indicative screen-shots. The scenario of this service is the following: first the user defines the scheduling time horizon and then reviews and verifies the production orders that have due dates in this horizon. At any point, editing the production configuration is also important, e.g., excluding a machine. This allows the user to test several scenarios for the job floor, being able to include aspects like machine maintenance that are not explicitly formulated as part of the optimization problem. Following this, the user defines the objectives which the scheduling algorithm is to minimize in a hierarchical fashion (a single objective can also be defined). Once the algorithm provides the schedule, the user can review it as a Ganttchart and determine whether the produced schedule is “confirmed ”(to be executed) or “simulated ”(possibly after comparing it with other schedules that cover the same horizon). The work-flow of the rest services resembles this scenario with slight modifications, therefore not presented.

Data availability implies that the requested pieces of information are available and reliable. The integration of energy-monitoring aspects in a factory environment is a new requirement, hence it is expected that energy-related data may be absent. In fact, the smaller industrial user did not have an EMS and only recently started using metering equipment for electricity consumption; clearly, in the absence of credible energy data, our DSS is used to optimize over the temporal objectives. Beyond that, tracking of production orders on machines is not available in real-time for this user and has been inserted using historical data. Energy-constraints are set over machines and not over production orders. Furthermore, the required time for a machine to change from one operation (e.g. dyeing blue) to another (e.g. dyeing red) is not available (for both users) but have been manually inserted.

The integration of the DSS with the ARTISAN system and the existing systems, implies the implementation of interfaces enabling the data exchange between these systems. Apart from that, these interfaces ensure that changes on the DSS will not affect the proper function of individual components. This is an important aspect for the maintenance of the DSS.

## 5. Impact and benefits

This section presents the benefits from the use of the proposed DSS in textile manufacturing. Sections 5.1 and 5.2 present the structure of the production lines and the specific scheduling requirements of the two industrial users, namely an LSE (User A) and an SME (User B), including the hierarchy of the optimization criteria preferred by each user. Next, we discuss in Section 5.3 the pilot experimentation done in each end-user’s production site and report the reduction of energy consumption as calculated by both users. Further insightful experiments are discussed in Section 5.4 regarding energy constraints and Section 5.5 concerning the energy objective.

## 5.1. Large-size enterprise - industrial User A

For User A focus is given on the processes related to the finishing department, whose key characteristic is that most machines run on high temperatures. Therefore, the heating-up and the coolingdown consumptions are significant. In addition, it is a common practice that many machines work in standby mode for long periods of time, i.e., all week except weekends. All optimization scenarios are performed assuming a mid-term planning horizon (more than a month).

We examine a data set containing 642 production orders on 122 articles that have to go through 14 process steps having 38 machines in total. It is worth highlighting that this problem size is considered as very large-scale in the literature. No restrictions are imposed regarding the machine availability and no shortages are considered regarding the machine personnel across the shifts; i.e., machines are assumed to be constantly available. The machine capacity is the main bottleneck. User A prioritizes the optimization criteria as $C _ { m a x } | D _ { t } | F _ { t }$ so as to favor more the reduction of shifts (and thus indirect energy consumption) and then the reduction of the total idle time of machines (and thus the direct consumption arising from machines in standby mode); notably, this user is also interested in the hierarchy $D _ { t } | C _ { m a x } | F _ { t }$

## 5.2. Small-to-medium enterprise - industrial User B

The production in User B has fragmented production volumes, hence it becomes dificult to maintain a continuous production schedule. In particular, the small production lots cause frequent stops of machineries for cleaning and set-up before the next order is processed. Therefore, the machine idle times can be significant but the total flow time is also important. To that end, User B selects the optimization hierarchy $D _ { t } | F _ { t } | C _ { m a x }$

We examine a data-set containing 33 production orders on 20 articles, each passing through 24 process steps and a total of 29 machines. The main restriction is represented by the personnel dedicated to so called ‘warp change’ and ‘loom preparation’. These workers are specialized, therefore the availability of the corresponding machines is linked to their presence per shift. All optimization scenarios are performed assuming a 30-day planning horizon. Hence, this is a medium-sized data set over a long horizon.

## 5.3. On-site experimentation and evaluation

The proposed DSS has been evaluated in both industrial users by estimating the reduction in the energy consumption after the adoption of the optimized schedule. This has been calculated externally, using energy consumption data in combination with the optimized schedules offered. Overall, the schedules provided by the proposed DSS have a considerable impact on the energy consumption in both users. The calculation at User A has shown an average monthly reduction in energy consumption by 15.9% mainly by reducing the number of shifts hence the indirect energy consumption but also by reducing the idle time of machines. User B has reported a slightly higher reduction of 16.5% that is, to the largest part, attributed to much smaller idling times of machines. This is of no surprise, since User A has a large manufacturing site with very high fixed energy costs but a rather smooth production that utilizes machines quite well thus allowing for mediocre savings because of reducing the idle times. In contrast, User B has a smaller installation, in which fixed energy consumption is not particularly high; however, because of small lot sizes and fewer machines, it suffers from long idle times especially in some energy-intensive machines that consume in stand-by mode approximately the same energy as in production mode.

Besides the observed energy consumption at the industrial users, various computational experiments have been performed to study the interrelationships among the optimization objectives, and in particular between the total flow time $F _ { t }$ and the total idle time $D _ { t }$ . Table 1 shows the results obtained for three different monthly planning periods (first column, M1–M3) under different hierarchies (second column) for User A. The last three columns show the values (in thousands of minutes) for each objective.

S. Plitsos et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/JA2AAEVB/fulltext/images/97468aaecf78f7ac9b2c30d750ce2d3c907780e8002c0a29691e7fed267710ce.jpg)  
Fig. 2. Resource-constrained shop floor scheduling at the process level.

The results of Table 1 show that, for the dataset of User A, the selection of the optimization hierarchy can play a critical role. Although the value of the makespan is not varying significantly, the values of $F _ { t }$ and $D _ { t }$ are quite ‘in conflict’ and significantly affected by the choice of the optimization hierarchy. That is, whenever the focus is primarily given on minimizing $F _ { t } ,$ the idle times are significantly increased and vice versa. For example, in month M3 the lowest total flow time is 657,615 thousand minutes but is accompanied with a total of 131,496 thousand minutes of idle time. Instead, if we minimize first the total idle time, then we get a 48% improvement from 131,496 to 88,289 but with an increase of 3.7% regarding the total flow time from 657,615 to 683,585. The implication here is that if direct idle energy consumption is more critical, priority should be given to $D _ { t } ;$ if, to the contrary, the energy consumed by machines during production time dominates total energy consumption, then focus should be given to $F _ { t }$ regarding the optimization hierarchy. We should note that the results for User B are pretty similar but less illuminating since that user’s data set is quite small-sized.

Furthermore, a qualitative evaluation of the proposed services has been performed following the ISO/IEC 9126 standard for software quality. The personnel that has used these services has rated it in terms of eficacy (2.63/3), eficiency (2.68/3), understandability (2.51/3), satisfaction (2.63/3), learnability (2.44/3) and adaptability (2.40/3). These scores show that the proposed DSS meets in a satisfying degree the end-users’ expectations.

Results for monthly production schedules with different optimization priorities.

<table><tr><td>Month</td><td>Hierarchy</td><td> $C_{max}$ </td><td> $F_t$ </td><td> $D_t$ </td></tr><tr><td rowspan="2">M1</td><td> $F_t|C_{max}|D_t$ </td><td>8803</td><td>297,780</td><td>122,346</td></tr><tr><td> $D_t|C_{max}|F_t$ </td><td>8803</td><td>366,077</td><td>71,474</td></tr><tr><td rowspan="2">M2</td><td> $F_t|C_{max}|D_t$ </td><td>9201</td><td>403,351</td><td>103,536</td></tr><tr><td> $D_t|C_{max}|F_t$ </td><td>9201</td><td>470,706</td><td>64,300</td></tr><tr><td rowspan="2">M3</td><td> $F_t|C_{max}|D_t$ </td><td>8802</td><td>657,615</td><td>131,496</td></tr><tr><td> $D_t|C_{max}|F_t$ </td><td>8802</td><td>683,585</td><td>88,289</td></tr></table>

## 5.4. Effect of energy utility constraints

An additional set of computational experiments have been performed to study the effect of resource (utility) constraints on the optimization criteria. For this purpose, we have generated six indicative problem instances $I _ { 1 }$ to $I _ { 6 }$ based on the shop floor characteristics and the production scheduling attributes of both industrial users. Tables 2 and 3 summarize the results obtained. The first set of columns show the basic structural properties and the actual size of each problem instance in terms of number of jobs, operations and machines. The second set of columns indicate the hierarchy of objectives. In all experiments, we solved the $C _ { m a x } | F _ { t } | D _ { t }$ problem. The last set of columns provide the results obtained by solving the scheduling problem without any resource constraints $( R C _ { 0 } )$ and with up to 3 resource constraints (i.e., RC is instance $R C _ { 0 }$ with i resource constraints, $i \ = \ 1 , 2 , 3 )$ on the machine and process step level. The three renewable resources correspond to electricity, gas and high pressure steam. Without loss of generality we assume that the available parallel machines at each process step are identical, there are sequence dependent changeover (set-up) times, all production orders have the same release date and half of the production order have a due date earlier than the end of the planning horizon. To that end, the first group of problem instances $\left( I _ { 1 } \right.$ to $I _ { 3 }$ in Table 2) are identical to the second group of problems $( I _ { 4 }$ to $I _ { 6 }$ in Table 3); however, in the instances of the first group all machines are available at all times, while in the ones of the second group the availability of machines varies (up to 20% machine unavailability throughout the planning horizon).

Please cite this article as: S. Plitsos et al., Energy-aware decision support for production scheduling, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.017

Table 2  
Results with renewable resource constraints.

<table><tr><td rowspan="2" colspan="3">Instance</td><td rowspan="2">Criterion</td><td colspan="4">Resource constraints</td></tr><tr><td> $RC_0$ </td><td> $RC_1$ </td><td> $RC_2$ </td><td> $RC_3$ </td></tr><tr><td rowspan="3"> $I_1$ </td><td>Operations</td><td>100</td><td> $C_{max}$ </td><td>1037</td><td>1565</td><td>2755</td><td>3241</td></tr><tr><td>Jobs</td><td>10</td><td> $F_t$ </td><td>8779</td><td>13,740</td><td>23,005</td><td>25,327</td></tr><tr><td>Machines</td><td>20</td><td> $D_t$ </td><td>3621</td><td>6123</td><td>18,847</td><td>22,927</td></tr><tr><td rowspan="3"> $I_2$ </td><td>Operations</td><td>123</td><td> $C_{max}$ </td><td>1504</td><td>2269</td><td>3995</td><td>4320</td></tr><tr><td>Jobs</td><td>12</td><td> $F_t$ </td><td>12,378</td><td>19,373</td><td>32,437</td><td>35,711</td></tr><tr><td>Machines</td><td>20</td><td> $D_t$ </td><td>5395</td><td>9123</td><td>28,082</td><td>34,161</td></tr><tr><td rowspan="3"> $I_3$ </td><td>Operations</td><td>148</td><td> $C_{max}$ </td><td>2395</td><td>3615</td><td>6364</td><td>6881</td></tr><tr><td>Jobs</td><td>14</td><td> $F_t$ </td><td>20,894</td><td>32,701</td><td>54,752</td><td>60,278</td></tr><tr><td>Machines</td><td>20</td><td> $D_t$ </td><td>8437</td><td>14,267</td><td>43,914</td><td>53,420</td></tr></table>

Let us observe that, as we add resource constraints, the quality of the schedules is significant affected and all optimization criteria are deteriorated; however, the effect on the total idle time appears much stronger as $D _ { t }$ gets many times higher. This is an indication that there is a trade-off between violating a constraint on energy consumption versus large machine idle or stand-by times. Moreover, once machine unavailability occurs (see Table 3), the effect of adding energy resource constraints is even greater.

## 5.5. Energy vs temporal objectives

Temporal objectives are related with both direct and indirect energy consumption, i.e., $C _ { m a x }$ is related to the minimization of $P _ { i n d i r e c t }$ and $D _ { t }$ to the minimization of $P _ { i d l e }$ . It becomes easy to see that if all machines are identical or only one machine is available per operation, then $P _ { d i r e c t }$ remains the same for all schedules, thus only $P _ { i d l e }$ and $P _ { i n d i r e c t }$ are relevant in terms of energy minimization. However, $P _ { d i r e c t }$ does vary significantly across flexible multiprocessing environments, where parallel machines are available at each process step and a particular operation may be processed by a faster (newer) or slower (older) machine with different energy consumption; often, the faster machine is not the most energy eficient one.

In this section we examine the trade-off between $P _ { t }$ and $C _ { m a x }$ (or $P _ { t }$ and $F _ { t } ) ,$ assuming a flexible production environment with parallel unrelated machines $( \mathrm { i . e . , }$ with different speed and energy consumption). Indicatively, we apply our algorithm to the instances called F15 and F19 in the benchmark data set of Fattahi et al. [29], properly modified to include electricity consumption. That is, one process step is assumed (with a maximum consumption limit) and a constant indirect energy demand of 3 kW. The processing times range from 40 to 250 min and the electricity demand from 5 to 50 kW; in addition, it is assumed that each machine requires 20% of the processing electricity consumption while idle. All machines are available at all times.

Table 3  
Results with renewable resource constraints (cont.).

<table><tr><td rowspan="2" colspan="3">Instance</td><td rowspan="2">Criterion</td><td colspan="4">Resource constraints</td></tr><tr><td> $RC_0$ </td><td> $RC_1$ </td><td> $RC_2$ </td><td> $RC_3$ </td></tr><tr><td rowspan="3"> $I_4$ </td><td>Operations</td><td>100</td><td> $C_{max}$ </td><td>1045</td><td>1737</td><td>2897</td><td>2979</td></tr><tr><td>Jobs</td><td>10</td><td> $F_t$ </td><td>9209</td><td>15,245</td><td>23,524</td><td>27,659</td></tr><tr><td>Machines</td><td>20</td><td> $D_t$ </td><td>5357</td><td>9364</td><td>19,811</td><td>25,765</td></tr><tr><td rowspan="3"> $I_5$ </td><td>Operations</td><td>123</td><td> $C_{max}$ </td><td>1515</td><td>2519</td><td>4201</td><td>4699</td></tr><tr><td>Jobs</td><td>12</td><td> $F_t$ </td><td>12,985</td><td>21,495</td><td>33,169</td><td>38,999</td></tr><tr><td>Machines</td><td>20</td><td> $D_t$ </td><td>7982</td><td>13,952</td><td>29,518</td><td>38,390</td></tr><tr><td rowspan="3"> $I_6$ </td><td>Operations</td><td>148</td><td> $C_{max}$ </td><td>2414</td><td>4012</td><td>6692</td><td>7487</td></tr><tr><td>Jobs</td><td>14</td><td> $F_t$ </td><td>21,917</td><td>36,283</td><td>55,987</td><td>65,828</td></tr><tr><td>Machines</td><td>20</td><td> $D_t$ </td><td>12,482</td><td>21,818</td><td>45,160</td><td>67,032</td></tr></table>

Table 4  
Results with hierarchical energy and temporal objectives.

<table><tr><td colspan="3">Instance</td><td>Hierarchy</td><td> $C_{max}$ </td><td> $F_t$ </td><td> $D_t$ </td><td> $P_t$ </td></tr><tr><td rowspan="4">F15</td><td>(n,m)</td><td>(7,7)</td><td> $C_{max}|F_t|D_t$ </td><td>519</td><td>3264</td><td>98</td><td>77</td></tr><tr><td> $r_{max}$ </td><td>∞</td><td> $F_t|C_{max}|D_t$ </td><td>590</td><td>3132</td><td>358</td><td>78</td></tr><tr><td> $max_i k_i$ </td><td>3</td><td> $P_t|C_{max}|F_t$ </td><td>750</td><td>4365</td><td>0</td><td>56</td></tr><tr><td>z</td><td>2.6</td><td> $P_t|F_t|C_{max}$ </td><td>842</td><td>4184</td><td>1</td><td>56</td></tr><tr><td rowspan="4">F15</td><td>(n,m)</td><td>(7,7)</td><td> $C_{max}|F_t|D_t$ </td><td>1002</td><td>4850</td><td>428</td><td>69</td></tr><tr><td> $r_{max}$ </td><td>70 (7 kW × m)</td><td> $F_t|C_{max}|D_t$ </td><td>902</td><td>4414</td><td>604</td><td>70</td></tr><tr><td> $max_i k_i$ </td><td>3</td><td> $P_t|C_{max}|F_t$ </td><td>1058</td><td>5033</td><td>7</td><td>57</td></tr><tr><td>z</td><td>2.6</td><td> $P_t|F_t|C_{max}$ </td><td>1061</td><td>4994</td><td>0</td><td>57</td></tr><tr><td rowspan="4">F19</td><td>n,m</td><td>(11,8)</td><td> $C_{max}|F_t|D_t$ </td><td>1109</td><td>9758</td><td>202</td><td>185</td></tr><tr><td> $r_{max}$ </td><td>∞</td><td> $F_t|C_{max}|D_t$ </td><td>1412</td><td>9179</td><td>702</td><td>199</td></tr><tr><td> $max_i k_i$ </td><td>4</td><td> $P_t|C_{max}|F_t$ </td><td>1570</td><td>12,773</td><td>0</td><td>156</td></tr><tr><td>z</td><td>2.3</td><td> $P_t|F_t|C_{max}$ </td><td>1653</td><td>12,631</td><td>47</td><td>157</td></tr><tr><td rowspan="4">F19</td><td>(n,m)</td><td>(11,8)</td><td> $C_{max}|F_t|D_t$ </td><td>2227</td><td>18,224</td><td>2239</td><td>211</td></tr><tr><td> $r_{max}$ </td><td>80 (7 kW × m)</td><td> $F_t|C_{max}|D_t$ </td><td>2374</td><td>14,460</td><td>2887</td><td>205</td></tr><tr><td> $max_i k_i$ </td><td>4</td><td> $P_t|C_{max}|F_t$ </td><td>2669</td><td>21,557</td><td>5</td><td>162</td></tr><tr><td>z</td><td>2.3</td><td> $P_t|F_t|C_{max}$ </td><td>2732</td><td>20,749</td><td>0</td><td>163</td></tr></table>

Table 4 summarizes the experiments considering both energy and temporal objectives. For each problem instance, we present the results obtained with and without resource constraints. The first set of columns show the basic properties, i.e., the number of jobs (n) and the number of machines (m), the maximum number of operations per machine (max k ), the average number of machines per operation (z), and the maximum resource limit $( r _ { m a x } )$ in kW. Next, each row indicates the hierarchy of objectives. After solving the $C _ { m a x } | F _ { t } | D _ { t }$ and the $F _ { t } | C _ { m a x } | D _ { t }$ problems without considering $P _ { t } ,$ we set $P _ { t }$ as the primary objective and we solve both hierarchies $P _ { t } | C _ { m a x } | F _ { t }$ and $P _ { t } | F _ { t } | C _ { m a x } .$ . Note that $P _ { t }$ is measured in thousands of kWh.

Clearly in all cases there is a significant difference when $P _ { t }$ is taken into account. Looking at instance F15 without resource constraints, the total energy drops from 77 to $5 6 ( \mathit { \_ { - 2 7 . 3 \% } } )$ , while $C _ { m a x }$ increases from 519 to 750 (+30.8%) and $F _ { t }$ from 3132 to 4184 (+25.1%); the figures for F19 are analogous. These numbers strongly indicate that, in flexible manufacturing settings, temporal objectives might not be enough to capture the energy component, and thus the various energy consumptions need to be explicitly considered. Moreover, once a resource constraint is added, the effect on the total energy consumption is even greater. Interestingly, the increased $P _ { t }$ values are due not to machine idling, as $D _ { t }$ becomes almost 0 once $P _ { t }$ is the primary objective; that is, $P _ { t }$ is mainly due to the $P _ { d i r e c t }$ component and somewhat due to the $P _ { i n d i r e c t }$ one. This is consistent to the fact that a large part of the energy consumption arises from non-productive machine modes [16], and reinforces the intuition of our end-users (see Sections 5.1 and 5.2) on the role of idle time in generating energy-aware production schedules.

## 6. Concluding remarks

In this study we present an energy-aware production scheduling DSS as designed, implemented and evaluated in a real context. In short, this paper contributes to decision support for energy-eficient manufacturing by a metaheuristic algorithm that hierarchically optimizes flexible job-shop scheduling problems over a variety of energy and temporal criteria, a set of data requirements, the integrated deployment of this DSS as a web-service and the evaluation of the DSS in real settings. Therefore, apart from examining theoretical aspects regarding the design of an energyaware DSS and the interplay among different objectives, our work presents the significant tangible benefits obtained from the use of such a system in textile manufacturing. That ${ \mathrm { i } } s ,$ the applicability of the proposed DSS, as deployed in two significantly different users and production environments, is shown to be both feasible and effective.

## Acknowledgements

We would like to thank the reviewers for valuable suggestions towards further emphasizing this papers relevance to energy-aware optimization.

## Appendix A. Description of data entities

Employee: Models each employee that works in the enterprise.

MachinePersonnel: Displays which employee can work on which machine.

Shift: Models the shifts of the employees within a facility.

ShiftEmployee: Displays which employee is assigned to which shift.

Resource: Models the consumable resources, e.g., electrical energy, gas, steam.

CostProfile: The time-varying cost profile per resource across time.

ResourceBoundary: The maximum resource consumption per machine.

Sensor: Models each metering device measuring the consumption of a resource.

SensorMachineGroup: Maps a group of machines to a sensor.

ResourceConsumption: Models the direct energy consumption.

Machine: Models each machine that exists in a production environment.

MachineAvailability: Models the availability of a machine.

Specs: Models the specifications of a machine for a product.

Process: Models a process of the manufacturing procedure.

ProcessStep: Models a part of a process.

Product: Models the products.

ProductStepSequence: Models the process step sequence for a product.

TimeFences: The time fences of a product in a process step.

ProductMachineSequence: Models the machine sequence for a product.

OperationType: Models the different operation types that may occur during the processing of a product across a machine sequence.

ProductOperationType: Models the sequence of operation types across machines for a product.

ChangeOverTime: Models the changes over time, of all possible combinations of OperationTypes.

ProductionOrder: Models the production orders that have been placed.

Schedule: Models the schedules that may be produced.

ScheduledProductionOrder: Maps production orders over different possible schedules.

ScopeType: An enumeration defining every possible scope type for a schedule within the system.

OptimizationType: An enumeration defining every possible optimization type for a schedule.

ScheduleType: An enumeration defining the two different types of schedule.

## References

[1] N. Weinert, S. Chiotellis, G. Seliger, Methodology for planning and operating energy-eficient production systems, CIRP Ann. Manuf. Technol. 60 (1) (2011) 41–44.

[2] J. Manget, C. Roche, F. Münnich, Capturing the Green Advantage for Consumer Companies, The Boston Consulting Group. 2009, 1–2.

[3] ECR-Europe, ECR Europe blue book-using traceability in the supply chain to meet consumer safety expectations, 2004.

[4] K. Bunse, M. Vodicka, P. Schönsleben, M. Brülhart, F.O. Ernst, Integrating energy eficiency performance in production management-gap analysis between industrial needs and scientific literature, J. Clean. Prod. 19 (6) (2011) 667–679.

[5] L. Mundaca, Markets for energy eficiency: exploring the implications of an EU-wide tradable white certificate scheme, Energy Econ. 30 (6) (2008) 3016-3043

[6] H.L. De Groot, E.T. Verhoef, P. Nijkamp, Energy saving by firms: decision-mak ing, barriers and policies, Energy Econ. 23 (6) (2001) 717–740.

[7] K. Vikhorev, R. Greenough, N. Brown, An advanced energy management framework to promote energy awareness, J. Clean. Prod. 43 (2013) 103–112.

[8] C. Pach, T. Berger, Y. Sallez, T. Bonte, E. Adam, D. Trentesaux, Reactive and energy-aware scheduling of flexible manufacturing systems using potential fields, Comput. Ind. 65 (3) (2014) 434–448.

[9] E. Zampou, S. Plitsos, A. Karagiannaki, I. Mourtos, Towards a framework for energy-aware information systems in manufacturing, Comput. Ind. 65 (3) (2014) 419–433.

[10] I. Harjunkoski, C.T. Maravelias, P. Bongers, P.M. Castro, S. Engell, I.E. Grossmann, J. Hooker, C. Méndez, G. Sand, J. Wassick, Scope for industrial applications of production scheduling models and solution methods, Comput. Chem. Eng. 62 (2014) 161–193.

[11] S.N. Pillutla, B.N. Nag, Object-oriented model construction in production scheduling decisions, Decis. Support. Syst. 18 (3) (1996) 357–375.

[12] S. Karnouskos, A.W. Colombo, J.L.M. Lastra, C. Popescu, Towards the energy eficient future factory, Industrial Informatics, 7th IEEE International Conference, IEEE. 2009, pp. 367–371.

[13] Y. Sakamoto, Y. Tonooka, Y. Yanagisawa, Estimation of energy consumption for each process in the Japanese steel industry: a process analysis, Energy Convers. Manag. 40 (11) (1999) 1129–1140.

[14] Z. Bi, L. Wang, Optimization of machining processes from the perspective of energy consumption: a case study, J. Manuf. Syst. 31 (4) (2012) 420–428.

[15] C. Subai, P. Baptiste, E. Niel, Scheduling issues for environmentally responsible manufacturing: the case of hoist scheduling in an electroplating line, Int. J. Prod Econ. 99 (1) (2006) 74–87.

[16] T. Devoldere, W. Dewulf, W. Deprez, B. Willems, J.R. Duflou, Improvement potential for energy consumption in discrete part production machines, Advances in Life Cycle Engineering for Sustainable Manufacturing Businesses Springer. 2007, pp. 311–316.

[17] P.L. Rocha, M.G. Ravetti, G.R. Mateus, M.P. Pardalos, Exact algorithms for a scheduling problem with unrelated parallel machines and sequence and machine-dependent setup times, Comput. Oper. Res. 35 (2008) 1250–1264.

[18] C. Artigues, P. Lopez, A. Haït, The energy scheduling problem: Industrial case-study and constraint propagation techniques, Int. J. Prod. Econ. 143 (1) (2013) 13–23.

[19] K. Fang, N. Uhan, F. Zhao, J.W. Sutherland, A new approach to scheduling in manufacturing for power consumption and carbon footprint reduction, J. Manuf. Syst. 30 (4) (2011) 234–240.

[20] M. Rager, C. Gahm, F. Denz, Energy-oriented scheduling based on evolutionary algorithms, Comput. Oper. Res. 54 (2015) 218–231.

[21] F. Shrouf, J. Ordieres-Meré, A. García-Sánchez, M. Ortega-Mier, Optimizing the production scheduling of a single machine to minimize total energy consumption costs, J. Clean. Prod. 67 (2014) 197–207.

[22] A. Certa, M. Enea, G. Galante, C. Manuela La Fata, Multi-objective human resources allocation in r&d projects planning, Int. J. Prod. Res. 47 (13) (2009) 3503–3523.

[23] M. Pinedo, Scheduling: Theory, Algorithms and Systems, Prentice-Hall, Englewood Cliffs, NJ, 1995.

[24] R.R. Farrell, T.C. Maness, A relational database approach to a linear programming-based decision support system for production planning in secondary wood product manufacturing, Decis. Support. Syst. 40 (2) (2005) 183–196.

[25] N. Ruiz, A. Giret, V. Botti, V. Feria, An intelligent simulation environment for manufacturing systems, Comput. Ind. Eng. 76 (2014) 148–168.

[26] H.R. Lourenço, O.C. Martin, T. Stützle, Iterated Local Search, Operations Research & Management Science Springer. 2003.

[27] G. Zobolas, C. Tarantilis, G. Ioannou, A hybrid evolutionary algorithm for the job shop scheduling problem, J. Oper. Res. Soc. 60 (2009) 221–235.

[28] ARTISAN Project, http://www.artisan-project.eu/.

[29] P. Fattahi, M. Mehrabad, F. Jolai, Mathematical modeling and heuristic approaches to flexible job shop scheduling problems, J. Intell. Manuf. 18 (2007) 331–342.

Stathis Plitsos is currently a PhD candidate at the Athens University of Economics and Business, Department of Management Science and Technology. He is also a researcher in the ADOPT group of the ELTRUN research center at the Athens University of Economics and Business. He holds an MSc. in Information Systems from the same university and a BSc. in Computer Science from the University of Athens. His research is focused in the areas of Combinatorial Optimisation and Integer Programming. He has participated in several EU and national research projects and has published in research conferences and scientific journals.

Dr. Panagiotis Repoussis is Lecturer at the Department of Marketing and Communi cation, School of Business at Athens University of Economics and Business (Athens, Greece) and visiting Assistant Professor at the School of Business at Stevens Institute of Technology (New Jersey, USA). His scientific interests apply in the areas of production and service operations management, freight transportation, logistics, and supply chain management, and he has published a number of articles on the design, development and application of models and algorithms to aid rigorous decision making in operational planning and scheduling of resources. He is currently board member at the College of Service Operations of the Production and Operations Management Society. He has been also involved as researcher and principal investigator in various NSE and FU funded research projects and his research has been funded by non-profit organizations and private companies in the EU and the USA.

Please cite this article as: S. Plitsos et al., Energy-aware decision support for production scheduling, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.017

S. Plitsos et al. / Decision Support Systems xxx (2016) xxx–xxx

Dr. Ioannis Mourtos is an Assistant Professor in “Mathematics of Operations Research” at the Department of Management Science and Technology, Athens University of Economics and Business. He studied Computer Engineering and Informatics at the corresponding department of the University of Patras and obtained both his MSc and PhD from the Operational Research Department, London School of Economics and Political Science. He has worked as a Lecturer at the Department of Economics, University of Patras. His research is focused in the areas of Combinatorial Optimisation and Integer Programming, examining also the integration of Integer Programming with Constraint Programming algorithms. He has published in Operations Research journals like Mathematical Programming, Informs Journal on Computing, SIAM Journal on Discrete Mathematics Operations Research Letters, European Journal of Operational Research and Discrete Mathematics, for several of which he has served as a reviewer. He has also participated in national and European research projects.

Dr. Christos Tarantilis is a Professor of Management Science at the Department of Management Science and Technology of the Athens University of Economics and Business. His research interests lie in the area of computational decision-making and applications in production and service management, transportation and logistics, supply chain management. He is also member of the editorial board (e.g. the “Networks” journal-Wiley) and guest editor (e.g. the “Computers and Operations Research” journal-Elsevier) in well-known academic journals, chairman and member of the scientific committee of international scientific conferences. Prof. Tarantilis has more than 130 scientific papers in international academic journals, books and conferences.
