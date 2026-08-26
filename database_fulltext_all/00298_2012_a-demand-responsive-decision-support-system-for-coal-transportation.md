---
otero_id: 298
otero_key: "CKWK65UU"
title: "A demand-responsive decision support system for coal transportation"
authors: "Erhan Kozan; Shi Qiang Liu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A demand-responsive decision support system for coal transportation

Erhan Kozan ⁎, Shi Qiang Liu

School of Mathematical Sciences, Queensland University of Technology, 2 George St GPO Box 2434, Brisbane Qld 4001 Australia

a r t i c l e i n f o

Article history: Received 17 May 2011 Received in revised form 21 July 2012 Accepted 17 August 2012 Available online 29 August 2012

Keywords: Coal train scheduling Decision support system Coal stockpiles Coal shipment Mine transportation

## a b s t r a c t

In this paper, a demand-responsive decision support system is proposed by integrating the operations of coal shipment, coal stockpiles and coal railing within a whole system. A generic and <sup>fl</sup>exible scheduling optimisation methodology is developed to identify, represent, model, solve and analyse the coal transport problem in a standard and convenient way. As a result, the integrated train-stockpile-ship timetable is created and optimised for improving overall ef<sup>fi</sup>ciency of coal transport system. A comprehensive sensitivity analysis based on extensive computational experiments is conducted to validate the proposed methodology. The mathematical proposition and proof are concluded as technical and insightful advices for industry practice. The proposed methodology provides better decision making on how to assign rail rolling-stocks and upgrade infrastructure in order to signi<sup>fi</sup>cantly improve capacity utilisation with the best resource-effectiveness ratio. The proposed decision support system with train-stockpile-ship scheduling optimisation techniques is promising to be applied in railway or mining industry, especially as a useful quantitative decision making tool on how to use more current rolling-stocks or whether to buy additional rolling-stocks for mining transportation. © 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Australia is the world's largest coal exporting country and produced around <sup>fi</sup>ve hundred million tonnes of coals in 2008–2009 [22]. Railways play a vital role in transporting the coal from mines to ports, where the majority of the coal is transported by rail. Many large coal mining operations in Queensland heavily rely on the rail network to transport coal from various mines to coal terminals at ports for shipment. The coal mining railway system performs two main tasks: delivering empty wagons to the mines at sidings; and collecting the full wagons of coal from mines and transporting them to the port. The transport sector has an important effect on the overall costs of a coal mining system.

Over the last few years, due to the fast growing demand, the coal transport system including coal railway network and port terminal is becoming one of the worst industrial bottlenecks in Australia. As reported in 2007–2009, “furious coal producers blamed sheer incompetence by the state-owned railway for the backlog when more than 150 ships were anchored off the east coast — waiting to load coal” [41]. The bottleneck was costing mining companies millions of dollars on demurrage charges per month, threatening hundreds of jobs in the industry and risking the future of exports to key Asian customers. As a result, it was announced that “Australian Rail Track Corporation hoped to double capacity on its national freight network by switching to a \$500 million computerised management system” [42] and “the port facility at Abbot Point is currently expanding from 25 mtpa capacity to 50 mtpa with further potential to expand to beyond 100 mtpa” [22].

Many practical issues of system interoperability need to be considered when decisions are made about whether to upgrade the rail network or build a new corridor that should be consistent with the port expansion projects. For example, Queensland Rail Network identi<sup>fi</sup>ed a range of potential expansion plans for upgrading the rail/port infrastructure [22]. However, the rail industry recommends that rail capacity be underwritten and constructed to meet industry demand ahead of underwritten port expansion projects. In this way, the undesirable impacts of construction of new rail capacity on existing throughput should be minimised or reduced. This also eliminates the unbalanced situation of port capacity being available without enough rail capacity in place to match.

In central Queensland, there are currently three major coal export ports (i.e. Abbot Point, Hay Point and Gladstone) servicing central Queensland supported by four major rail corridors, i.e., Goonyella, Newlands, Blackwater and Moura [22]. The port precincts at Gladstone and Hay Point have a plan for signi<sup>fi</sup>cant expansion. However, it appears that the total coal export demand before 2020 would be still met by three existing major port precincts. This means that the central Queensland coal supply chain will probably remain concentrated on four existing major rail corridors at least in the medium term, which may lead to strategic risks associated with route diversity, increasing congestion and system interoperability [22]. As throughput demand increases on each major rail corridor, the railing capacity should be successively augmented to match the growing demand. When a rail corridor is serviced at saturation, future expansion may be able to continue on the existing corridor by adding sections of the third and fourth tracks (i.e. increasing the capacity of crossing loops). Strategically in the long term, it may be necessary to build a new rail corridor instead to meet the expansion demand. At this stage, it may be a better option to generate more reliable and more ef-<sup>fi</sup>cient transport systems under the given capacity of existing rail and port infrastructure.

In this background, both rail and port industries in Australia demand more new features in the planning and scheduling process and are keen to implement better modelling and solution techniques, in order to improve ef<sup>fi</sup>ciency and capability of railing coal from various mines to ports. By generating better operating schedules, it is possible to increase the utilisation rate of the coal transport system and reduce the transportation cost and demurrage charges. The current situation provides great incentives for pursuing better optimisation and control strategies for the operation of the whole coal transport system. Operating a coal transport system ef<sup>fi</sup>ciently requires a series of complicated planning and scheduling problems to be solved. As railways and ports are the most critical infrastructure of this transport system, the foremost amongst these planning and scheduling problems are train scheduling, ship berthing, coal stockpile management, determination of train services (railing roundtrips), assignment of empty rolling-stocks (locomotives and wagons) to train services, and loading/unloading operations.

To the best of our knowledge, limited numbers of research papers on the integrated coal transport system are published in the literature, maybe due to its considerable complexity or the protection of its substantial commercial value by industrial practitioners or consultation companies. Abdekhodaee et al. [1] integrated the operations in a coal rail network with operations in a coal terminal system, because the infrastructures of these two systems are tightly connected under a high service demand. They developed mixed integer programming models to analyse the integrated systems and then discussed the advantages and disadvantages of this integration. However, they mentioned that their proposed mathematical programming models are quite complicated and too dif<sup>fi</sup>cult to be exactly solved. For other sub-systems especially about the optimisation of coal train timetables, they only provided the simulation approaches to analyse three railing policies. Singh et al. [36] reported a decision-support tool for the coal supply chain of Hunter Valley Coal Chain (HVCC) in Australia. They presented the underlying mathematical models implemented in this decision-support tool along with simulation modelling and approximation algorithms used to identify the capacity requirements and make effective capacity improvement. However, to simplify their models, they made many assumptions especially without considering the capacity constraints of the coal rail network. In addition, they did not provide any approaches that can optimise coal train schedules.

The following recent literature has addressed the train scheduling problems. Zhou and Zhong [39] dealt with a double-track train scheduling problem with multiple objectives by a branch-and-bound algorithm with an effective dominance rule and a beam search algorithm with utility evaluation rules. The performance of the proposed solution approaches is evaluated by a Beijing-Shanghai high-speed railroad case study. Caprara et al. [10] incorporated several additional constraints into a mathematical model for a fundamental train timetabling problem using Lagrangian heuristic. Carey and Crawford [11] used heuristic algorithms to assist in the task of <sup>fi</sup>nding and resolving con<sup>fl</sup>icts in draft train schedules. Yuan and Hansen [38] proposed a stochastic model to estimate the knock-on delays of trains with a case study in the Dutch railway. Salido [35] modelled train scheduling problems as constraint satisfaction problems (CSP). Abril et al. [3] presented a technique to solve the CSPs modelling for train scheduling problems by distributing the constraint network in tree structures. Liebchen [28] reported that the optimised timetable based on the results of the periodicevent-scheduling problem had been implemented in Berlin railway. Chung et al. [13] addressed a train sequencing problem in the Korean railway and proposed a hybrid genetic algorithm to solve the problem.

D'Ariano et al. [16] studied reactive train scheduling problem when some train operations are perturbed. D'Ariano, et al. [17] further examined new approaches to improve punctuality of <sup>fl</sup>exible timetable without diminishing the capacity usage of a rail network. Cacchiani et al. [9] proposed LP relaxation methods for the periodic and non-periodic train timetabling problems. Li et al. [27] presented a discrete-event simula tion method based on travel-advance strategy for train scheduling. Zografos and Androutsopoulos [40] presented a decision support system for assessing alternative distribution routes with the hazardous materials. Cheng and Yang [12] adopted a fuzzy Petri Net method to for mulate the decision rules of train dispatchers in Taiwan's railway network. Lee and Chen [26] presented a decomposing heuristic algorithm both for train pathing and train timetabling problems. Kuo et al. [24] de termined elastic freight train timetable with multi-commodity by a train slot selection model. Fischetti et al. [19] improved the robustness of given train timetables for an Italian railway company using four different methods based on linear programming and stochastic programming techniques. Corman et al. [14] described a tabu search algorithm with rescheduling and rerouting strategies to set up a real-time traf<sup>fi</sup>c management system. Corman et al. [15] extended their research to consider two objectives that minimise train delays and maximise train punctuality. Krasemann [23] developed a fast heuristic to effectively deliver the train re-scheduling solution to a railway traf<sup>fi</sup>c distur bance management problem. Min et al. [32] developed a column generation-based algorithm to resolve train con<sup>fl</sup>icts in Seoul metropol itan railway network. Burdett and Kozan [6] developed capacity analysis techniques for estimating the absolute traf<sup>fi</sup>c carrying ability of a railway system under various operational conditions. Burdett and Kozan [7,8] dealt with inserting additional train services into existing train timetables by constructive and metaheuristic algorithms based on an extended disjunctive graph model. Liu and Kozan [29] proposed a new scheduling model, “blocking parallel-machine job-shop scheduling (BPMJSS)”, which solves single-line train scheduling problems in a standard and convenient way. In the model, trains, single-track sections and multiple-track sections, respectively, are synonymous with jobs, single machines and parallel machines, and an operation is regarded as the movement/traversal of a train across a section. Furthermore, Liu and Kozan [30] investigated train scheduling problems with priority when both passenger and freight trains are simultaneously traversed in a single-line rail network. In this case, no-wait conditions arise be cause the prioritised (passenger) trains should traverse continuously without any interruption. In comparison, non-prioritised (freight) trains are allowed to enter the next section immediately if possible or to remain in a section until the next section on the routing becomes available.

To assist decision makers at their convenience, researchers in multi-disciplines such as operations research (OR), arti<sup>fi</sup>cial intelligence (AI) and information technology (IT) successively presented the structures, frameworks, mechanisms or architectures on the use of scheduling optimisation techniques to systematically set up the decision support systems for industry practice. Hee and Lapinski [20] gave a precise de<sup>fi</sup>nition of a decision support system, that is, “a decision support system is a computerised part of information systems that consult decision makers with their tasks by modelling the effects of actions that decision makers propose and generating the actions that optimise speci<sup>fi</sup>c objective functions”. They also discussed the components in the architecture of a decision support system, including “mathematical models to describe the effects of actions, algorithms to obtain the optimal actions with respect to speci<sup>fi</sup>c criterions, human-computer-interaction (HCI) modules such as database to input values of parameters and graphic user interfaces to view the actions”. Then, they presented a so-called job-shop scheduler to illustrate the speci<sup>fi</sup>cation of such a decision support system. Hsu et al. [21] described a decision support system called mixed-initiative scheduling workbench that embodies OR, AI and HCI characteristics. Due to the complex nature of scheduling environments, they classi<sup>fi</sup>ed practical scheduling constraints as “hard” that must be satis<sup>fi</sup>ed due to feasibility requirements and “softer” that may be violated if necessary. According to their observations, they indicated that the design of human-computer scheduling systems require the knowledge, expertise and judgement accumulated from years of experience, which are valuable assets of a <sup>fi</sup>rm. Wezel and Jorna [37] proposed a so-called scheduling-expertise-concept (SEC) framework that enables faster development of scheduling systems, due to the need of reuse of conceptual and technical information. Ozbayrak and Bell [33] developed a knowledge-based decision support system, which consists of three hierarchical subsystems (i.e., an expert production scheduling subsystem, a knowledge-based tool management subsystem and a fault diagnosis subsystem), to assists managers in making short-term scheduling decisions in <sup>fl</sup>exible manufacturing systems. Fagerholt [18] described a computer-based decision support system for vessel <sup>fl</sup>eet scheduling, based on the accumulated experience in shipping companies. However, this systems focus on the interaction between the system and the end-users rather than the application of optimisation techniques. Petrovic et al. [34] presented a decision support tool for multi-objective job-shop scheduling based on a genetic algorithm, in which some what-if attributes such as aspiration levels, batch sizes and <sup>fi</sup>tness functions can be tuned up by decision makers using linguistic quanti<sup>fi</sup>ers. Lamptey et al. [25] developed an optimisation-based decision support tool to support scheduling decisions for highway pavement. This system can provide an indicator of what and when preventive maintenance treatments are needed and thus help decision makers to evaluate highway pavement monetary needs in an optimal manner. Abrahams and Ragsdale [2] introduced a decision support system for patient scheduling with the administration of travel vaccine. Under the scenarios of three different time windows, the solution techniques in complex scheduling procedures include greedy heuristics based on the dispatching rules such as <sup>fi</sup>rst-in-<sup>fi</sup>rst-out (FIFO) or sorted costs (SORT) or RANDOM; binary integer programming with CPLEX; and evolutionary optimiser based on genetic algorithms. In conclusion, the development of practical decision support systems with state-of-the-art scheduling optimisation methodologies has received more and more attentions from both the research community and the industries in the last two decades.

To the best of our knowledge, this paper is among the <sup>fi</sup>rst attempts to investigate the integration of trains, ships and stockpiles operations and propose a demand-responsive decision support system especially by extending state-of-the-art train-scheduling methodologies to deal with the real-world coal shipment problems.

## 2. Problem de<sup>fi</sup>nitions

## 2.1. Overall coal supply chain

The overall supply chain for coal export includes the following main components: suppliers (e.g. mining companies); mines; railway network; coal terminals at ports; offshore facilities (e.g. berth), ships; and overseas ports. Several coal mining companies may share coal and other train networks while some of them share coal export terminals as well.

There are mainly <sup>fi</sup>ve stages in overall coal supply chain from mines to ports: i) the coal is loaded by mining excavators and trucks in mine sites; ii) the coal is deposited in cones ready for rail transportation in mine sites; iii) different brands of coal are transported by rail from mines to ports; iv) the coal is unloaded and stacked to stockpiles at coal terminal; and v) the coal is loaded onto ships by conveyors. A typical user of coal supply chain operates several mines in various locations and can provide a customer with a variety of coal brands (e.g., bituminous coal, sub-bituminous coal, anthracite coal, lignite coal). Users negotiate on prices, amount and brand of coals and particularly over a time window, in which coal commodities should be available for shipping from the coal terminal at port. The timewindow information is communicated to mines, the railway industry and ports by the users, and to offshore transportation systems by the overseas purchasers. All the required coal commodities of different brands are excavated at mines, deposited by trucks, transported by rail, then unloaded, collected, stacked, reclaimed at coal terminal and loaded onto the ships at berth.

## 2.2. Rail network integrated with coal terminal

The coal rail network depicted in Fig. 1 consists of a set of single-track sections and a set of multiple-track sections referred to as Crossing Loops (or Sidings).

In practice, the coal railway track operates in such a way that only one train can occupy a single-track section at a time, whereas more than one train can run at a crossing loop (i.e. multiple-track section) at a time, provided that its capacity limit is regarded. Crossing loops are places where trains can stop or slow down in order to let another train overtake or cross it, or where trains can stop to load or unload cargoes, alight passengers and manoeuvre crew. Usually, a traversing track section (e.g. Section A or B in Fig. 1) is necessarily delimited by at least two signals: one at the beginning and the other at the end of the section, which will control when a train either can or cannot traverse on a section. This control is to avoid two trains traversing on the same track section simultaneously.

The coal terminal at the port has two major responsibilities: to receive various brands of coal in various quantities via the coal rail network and to deliver them to incoming ships. The coal terminal consists mainly of storage areas called stockpiles as depicted in Fig. 1.

In a demand-responsive time window, there are different brands of coal in different quantities coming from various mines by a group of trains to the coal terminals, where various brands of coal are unloaded by bottom dump to pits and then deposited to a stockyard via conveyors. Subsequently they are loaded onto ships waiting at berth. In most coal export ports, the berth can accommodate loading of at most three massive ships at a time. Usually a ship carries more than one coal brand, and ship loading will commence only when all consignment is ready at the terminal.

Usually, a ship that is waiting in the queue is assigned to berth once all consignment become ready at coal terminal. After a ship has berthed, coal is reclaimed from an appropriate stockpile by the reclaimers to the conveyors and then is loaded onto the ship. However, there may be some exceptions in that a portion of coal may be available after ship berthing due to the possibility of direct transferring coal from an arrival train to the ready ship without being stored in the stockpiles. This situation is called direct loading. In this case, the capacity of coal terminal may be not necessary to be taken into account. However, this process is slow and hard to control as one ship waits arrivals of several trains to complete the loading and the demurrage cost of delaying coal shipment is prohibitive. Direct loading cases will not be used in this study.

## 2.3. Integration of train arrivals, coal stacking and coal shipment

Based on an example with three coal brands (three coal stockpiles) and eight roundtrips, the relationship between stock levels, coal stacking process and arrivals of trains is illustrated in Fig. 2.

In coal railing service, one empty train (locomotives and empty wagons) with the current earliest ready time at the port is assigned, then departs from the port, traverses for some sections and arrives at the speci<sup>fi</sup>ed mine site, loads the coal at mine, then traverses in a reverse section sequence, returns to the port and unloads the coal at port. After unloading, each empty train will be sent to the train depot before starting its next coal railing service. Thus, we de<sup>fi</sup>ne one coal railing service as a coal train roundtrip. In a demandresponsive time window, a <sup>fl</sup>eet of coal train roundtrips is conducted to transport different brands of coal from mines and then stack them in stockpiles at the coal terminal. Stacking a brand of coal in a stockpile should start at a time point when a train assigned to transport the corresponding brand of coal arrives at the coal terminal. The stock level is changed in correspondence with the arrival time and coal tonnage of the arrival train. To be ready for ship loading, the <sup>fi</sup>nishing time of coal stacking process is synchronised with a time point when all brands of coal have been transported from mines to the coal terminal by a <sup>fl</sup>eet of roundtrips.

![](/api/attachments/CKWK65UU/fulltext/images/ceaed9c798708deb068eefd57f9268e58ec7a6089f0bc0c07e1b8499ad364455.jpg)  
Fig. 1. A sample integrated coal transport system.

![](/api/attachments/CKWK65UU/fulltext/images/f62dd017c15f404cc4736036eb566de36e7e00d3d6adcaf824d510e0bab2bde4.jpg)  
Fig. 2. Integration of train arrivals, coal stacking and coal shipment.

There are three main types of yard machines: stackers, reclaimers and dual-function machines. Stackers transfer coal from the conveyors to stockpiles for storing. Reclaimers transfer coal back to the conveyors for shipping. Most yard machines are dual-function machines because they can carry out both tasks. Note that two stacker-reclaimer machines cannot work on the same stockpile simultaneously. Each coal brand (e.g. Brand A) is associated with its own stockpile (e.g. Stockpile A) in the coal terminal as shown in Fig. 2. To guarantee suf<sup>fi</sup>ciently high robustness to minimise the disturbances of coal shipment, a stockpile is stacked in such a way that all the required coal commodities should be ready before loading the coal onto the ship.

## 2.4. An integrated rail-stockpile-ship coal transport timetable

For illustration, an integrated 2-train 4-roundtrip rail-stockpileship coal transport timetable is displayed by a string chart shown in Fig. 3.

For a typical coal train roundtrip, an empty train with the current earliest ready time at the port is assigned, then departs from the port, traverses and arrives at the speci<sup>fi</sup>ed mine, loads the coal at mine, returns to the port and unloads the coal at port for coal stacking in stockpiles. The starting time of coal stacking is synchronised with the arrival time of a roundtrip at port. With the service of a <sup>fl</sup>eet of coal train roundtrips, the coal shipment begins after the required coal commodities have been railed to coal terminal and stacked in stockpiles at port.

In real-life scenarios, the starting time of coal shipment is usually negotiated by demands from overseas customers. Then, the due date of stacking all brands of coal commodities at coal terminal is determined by the ship berthing time. Later, the order of coal brands and tonnages required by port authority is sent to mining companies. Finally, to complete coal railing service in a demand-responsive window, railway industry assigns a certain number of rolling-stocks (locomotives and wagons) to perform a <sup>fl</sup>eet of coal train roundtrips to transport the corresponding tonnages of coal from various mines to a coal terminal at port.

The coal transport decision-support system operates in a rolling horizon way as illustrated in Fig. 4.

According to the above analysis, the main operational activities of coal terminal and coal rail network are able to be synchronised in an integrated demand-responsive coal transport decision-support system. When making decisions on coal railing service, we should simultaneously consider the coal shipment demands, coal stockpile management and their impacts on the whole system. This is because it would increase uncertainty and additional costs if each element of coal supply chain system is optimised individually. The methodology proposed in this paper optimises the overall coal supply chain as a whole system rather than individual parts so that better decisions can be made.

The total cost of the coal mining transport operations is very high, because some of the potential effects on the mining production system may be delaying the arrival of coal at the port, causing the mines to wait longer for empty wagons, and triggering off inef<sup>fi</sup>ciencies in the coal mining transport system due to the need of using more rolling-stocks. The main objective is to minimise total train travel time of a <sup>fl</sup>eet of coal train roundtrips with a reasonable number of rolling-stocks (locomotives and wagons) in a demand-responsive time window.

## 3. Mathematical Formulation

To analyse the structural properties of coal railing service in such an integrated coal transport system, the mathematical programming formulation is developed by considering roundtrips and track sections are synonymous with jobs and machines respectively. The action of a roundtrip passing through a section is de<sup>fi</sup>ned as a roundtrip (job) operation. The relationships are portrayed in more detail as follows.

![](/api/attachments/CKWK65UU/fulltext/images/c850c2ace80540a533adb18a65669cf8fdb587ff845a4d699f3928ab6c1786df.jpg)  
Fig. 3. Illustration of integrated coal transport timetable with 2 trains, 4 roundtrips, 2 stockpiles and 1 ship

![](/api/attachments/CKWK65UU/fulltext/images/177f52c64f134bb58c7a088c971f6dfdaca00ef7214e19df6ba2dc1146fc2ec1.jpg)  
Fig. 4. Rolling horizons of coal railing, coal stacking and coal shipment time windows.

▪ Jobs↔Coal Train Roundtrips

▪ Single Machines↔Single-Track Sections

▪ Parallel Machines↔Multiple-Track Sections

▪ Operations↔Roundtrip operations (The action of a roundtrip passing through a section is de<sup>fi</sup>ned as a roundtrip operation.)

▪ Operational processing time↔Sectional running time

Moreover, trains are different from stationary machines (i.e., railway track sections) and can be treated as other kinds of critical resources in the cyclic-job-shop-scheduling type environment with multiple resources and blocking constraints.

Fig. 5 is drawn to explain the time information of a coal train roundtrip operation, including the starting time, the sectional running time (processing time), the dwelling time, the blocking time, the completion time, the blocking time, the departure time, the occupying time due to train length, and the leaving time.

Note that the values of time parameters of a train process through the sections may be zero or non-zero, depending on the different scenarios. For example, the blocking time is non-zero only when a train has to wait on its current track section thus blocks this section for other roundtrips. The processing time of the train is dependent on the section length and train speed in this section. The dwelling times are predesignated and actually could be included into the processing times. In the coal train scheduling model, the dwelling times are considered as zero in most traversing sections excluding in the sections at mine and port. Thus, only the loading time at mine and the unloading time at port of a coal train roundtrip are nonzero dwelling times in the model.

The mathematical formulation of coal train scheduling is presented as follows.

## Parameters:

$n ^ { t }$ number of trains (i.e., locomotives and wagons) assigned for coal railing service in a demand-responsive time window; note the difference between $n ^ { t }$ and $n ^ { r } \left( n ^ { t } { \leq } n ^ { r } \right)$

$n ^ { r }$ number of roundtrips.

$m$ number of sections that consist of single-track sections and multiple-track sections.

$J _ { i }$ roundtrip $i ( i { = } 1 , 2 , . . . , n ^ { r } )$

$M _ { k }$ section k $( k = 1 , 2 , . . . , m )$

$h _ { k }$ number of units of section k; default is a single-track section as $h _ { k } = 1$

$$
\in_ {i}
$$

$u _ { k } ^ { l }$ the $l ^ { t h }$ unit of section k $( l = 1 , 2 , . . . , h _ { k } )$

$p _ { i l k }$ processing time (sectional running time) of roundtrip i on the $l ^ { t h }$ unit of section k.

$\omega _ { i l k }$ planned dwelling time of roundtrip i on the $l ^ { t h }$ unit of section $k ;$ default as zero excluding sections at mine and port. $\Omega _ { i l k }$ occupying time caused by the train length of roundtrip i on the $l ^ { t h }$ unit of section k.

$o$ the index of sequence position of an operation processed on one section.

$\alpha _ { i }$ coal loading time at the mine of roundtrip i.

$\beta _ { i }$ coal unloading time at port of roundtrip i.

sequence position index of the outbound operation at mine for roundtrip i.

![](/api/attachments/CKWK65UU/fulltext/images/c0763ee77090822b5c2569469ebc42a19b2f244669c5bfb7ffac77c7c67bd4e9.jpg)  
Fig. 5. Time parameters of a roundtrip operation.

ε<sub>i</sub> section index of the outbound operation at mine for roundtrip i.

$\eta _ { v }$ ready time of train υ available for starting service.

M a very large positive number.

$\rho _ { v }$ number of locomotives of train $v , v \in n ^ { t } .$

$\sigma _ { v }$ number of wagons of train $v , v \in n ^ { t }$

$w _ { i }$ coal tonnage of roundtrip $i , i \in n ^ { r } .$

$n ^ { s }$ number of ships, usually equal to the number of berths in a time window.

$\delta _ { \tau }$ coal shipment demand of ship $\tau , \tau \in n ^ { s } .$

## Variables:

$S _ { i l k }$ starting time of roundtrip i on the $l ^ { t h }$ unit of section k.

$b _ { i l k }$ blocking time of roundtrip i on the $l ^ { t h }$ unit of section k.

$C _ { i l k }$ completion time of roundtrip i on the $l ^ { t h }$ unit of section k $( C _ { i l k } = S _ { i l k } + p _ { i l k } ) .$

$D _ { i l k }$ departure time of roundtrip i on the $l ^ { t h }$ unit of section k $\left( D _ { i l k } = C _ { i l k } + \omega _ { i l k } + b _ { i l k } \right)$

$L _ { i l k }$ leaving time of roundtrip i on the $l ^ { t h }$ unit of section k $( L _ { i l k } =$ $D _ { i l k } + \Omega _ { i l k } )$

$L _ { i }$ leaving time of roundtrip i at the last section

$r _ { i o l k }$ = 1, if the $o ^ { t h }$ operation of roundtrip i requires the $l ^ { t h }$ unit of section $k ; = 0$ , otherwise.

$x _ { i l k }$ = 1, if roundtrip i is assigned to the $l ^ { t h }$ unit of section $k ; =$ $^ { 0 , }$ otherwise.

$y _ { i i ^ { ' } l k }$ = 1, if both roundtrips i and i′ are assigned to the $l ^ { t h }$ unit of section k and roundtrip i precedes roundtrip i′ (not necessarily immediately $) ; = 0$ , otherwise.

$z _ { i i } { ' } _ { o l k }$ $= 1 , \mathrm { i f } \mathrm { t h e } o ^ { t h }$ operation of roundtrip i requires the $l ^ { t h }$ unit of section k and roundtrip i′ is scheduled on this same unit as its immediate same-machine successor; = 0, otherwise.

$\rho$ number of total locomotives in a time window.

$\sigma$ number of total wagons in a time window.

## 3.1. Mathematical Formulation

The objective function is to minimise total train travel time of all roundtrips for completing coal railing service in a demand-responsive time window.

Minimise max $_ i ( L _ { i } + \beta _ { i } ) )$

ð <sup>1</sup>Þ

Subject to:

$$
\sum_ {l = 1} ^ {h _ {k}} \sum_ {k = 1} ^ {m} r _ {i o l k} D _ {i l k} \leq \sum_ {l = 1} ^ {h _ {k}} \sum_ {k = 1} ^ {m} r _ {i, o + 1, l k} S _ {i l k}, o = 1, 2, \dots , m - 1, \forall i\tag{2}
$$

Eq. (2) restricts the starting time of the $( o + 1 ) ^ { t h }$ operation of roundtrip i to be no earlier than its departure time of the ${ \boldsymbol { o } } ^ { \hat { t h } }$ operation of roundtrip i.

$$
S _ {i l k} \geq L _ {i ^ {\prime} l k} + \mathrm{M} (y _ {i i ^ {\prime} l k} - 1), \forall i, i ^ {\prime}, l, k\tag{3}
$$

Eq. (3) restricts that both roundtrips i and i′ are processed on the $l ^ { t h }$ unit of section k and roundtrip i precedes roundtrip i′ (not necessarily immediately).

$$
S _ {i ^ {\prime} l k} \geq L _ {i l k} + \mathsf {M} (y _ {i ^ {\prime} i l k} - 1), \forall i, i ^ {\prime}, l, k\tag{4}
$$

Eq. (4) restricts that that both roundtrips i and i′ are processed on the $l ^ { t \hat { h } }$ unit of section k and roundtrip i′ precedes roundtrip i (not necessarily immediately).

$$
y _ {i i ^ {\prime} l k} + y _ {i ^ {\prime} i l k} \leq 1, \forall i, i ^ {\prime}, l, k\tag{5}
$$

Eq. (5) restricts that conditions that roundtrip i′ precedes roundtrip i or roundtrip i precedes roundtrip i′ on the $l ^ { t h }$ unit of section k are exclusive.

$$
\sum_ {l = 1} ^ {h _ {k}} \sum_ {k = 1} ^ {m} x _ {i l k} = 1 \quad \text { and } \quad x _ {i l k} + x _ {i ^ {\prime} l k} - 1 \leq y _ {i i ^ {\prime} l k} + y _ {i ^ {\prime} i l k} \forall i, i ^ {\prime}, l, k\tag{6}
$$

Eq. (6) restricts that each unit can process at most one roundtrip at a time.

$$
S _ {i l k}, p _ {i l k}, C _ {i l k}, \omega_ {i l k}, b _ {i l k}, D _ {i l k}, \Omega_ {i l k}, L _ {i l k} \geq 0, \forall i, l, k\tag{7}
$$

Eq. (7) satis<sup>fi</sup>es non-negativity condition.

$$
\begin{array}{l} \sum_ {i ^ {\prime} = 1} ^ {n ^ {r}} \sum_ {l = 1} ^ {h _ {k}} \sum_ {k = 1} ^ {m} r _ {i ^ {\prime} o l k} S _ {i l k} z _ {i i ^ {\prime} o l k} \geq \sum_ {l = 1} ^ {h _ {k}} \sum_ {k = 1} ^ {m} r _ {i, o + 1, l k} S _ {i l k}, \forall i, i ^ {\prime} | i \neq i ^ {\prime}; o \\ = 1, 2, \dots , m - 1 \end{array}\tag{8}
$$

$\operatorname { E q . }$ (8) de<sup>fi</sup>nes the blocking constraints. To satisfy the blocking constraints under parallel-machine job-shop environments, for each operation, the starting time of the same-machine successor should be greater or equal to the starting time of the same-job successor.

$$
\sum_ {l = 1} ^ {h _ {1}} S _ {i l 1} x _ {i l 1} \geq \min _ {v = 1, \dots , \tau} \eta_ {v}, \forall i\tag{9}
$$

Eq. (9) satis<sup>fi</sup>es that the starting time of a roundtrip should be greater than or equal to the earliest ready time of the trains assigned for coal railing service in a demand-responsive window.

$$
\sum_ {l = 1} ^ {h _ {\varepsilon_ {i}}} r _ {i \epsilon_ {i} l \varepsilon_ {i}} S _ {i l \varepsilon_ {i}} \leq \sum_ {l = 1} ^ {h _ {\varepsilon_ {i}}} r _ {i, \epsilon_ {i} + 1, l k} L _ {i l \varepsilon_ {i}} + \alpha_ {i}, \forall i\tag{10}
$$

Eq. (10) satis<sup>fi</sup>es that the starting time of inbound operation at mine should be greater than or equal to the leaving time of the outbound operation at mine plus the coal loading time, for any roundtrip.

$$
\sum_ {v = 1} ^ {n ^ {t}} \rho_ {v} \leq \rho \quad \text { and } \quad \sum_ {v = 1} ^ {n ^ {t}} \sigma_ {v} \leq \sigma\tag{11}
$$

Eq. (11) restricts the capacity of rail rolling-stocks (locomotives and wagons).

$$
\sum_ {i = 1} ^ {n ^ {r}} w _ {i} \geq \sum_ {\tau = 1} ^ {n ^ {s}} \delta_ {\tau}\tag{12}
$$

Eq. (12) guarantees that the total coal tonnage of $n ^ { r }$ roundtrips is delivered for satisfying the demand of coal shipments of $n ^ { s }$ ships in a demand-responsive time window.

The above mathematical programming model ensures that technological properties or critical constraints are satis<sup>fi</sup>ed in a coal transport system. This mathematical programming model for coal train scheduling is a typical job-shop-type disjunctive programming problem that can be decomposed into a set of subproblems [31]. Disjunctive programming is stated as linear programs with disjunctive constraints and logical conditions, involving the operations “and” (conjunction), $" 0 \Gamma "$ (disjunction), “complement $\mathbf { o } \mathbf { f } ^ { \prime }$ (negation), “if… then” (implication), etc. These operations applied to linear inequalities give rise to convex polyhedral sets and hence transform the problem of optimising a linear form subject to such constraints within the realm of linear programming. According to [4,5]'s research results about the convexity analysis of job-shop scheduling, there has a procedure for the sequential generation of the convex hull of feasible solutions to the job-shop system with additional constraints in disjunctive programming. This sequential convexi<sup>fi</sup>cation procedure operates upon two sets of elements, which satisfy both conjunctive constraints and disjunctive constraints that may include linear or nonlinear inequalities, integrality constraints, logical conditions, etc. This sequential convexi<sup>fi</sup>cation procedure consists of the following main steps. Firstly, a partial convex hull is formed by considering the constraints of an initial subsystem. Next, this partial convex hull is intersected with the solution set of a second subsystem that consists of constraints not included in the <sup>fi</sup>rst subsystem. Finally, the complete convex hull is obtained by iteratively intersecting and appending the constraints of the next subsystem to the previous partial convex hull. The above analysis proves that the set of solutions of our studied problem is a sequential intersection of partial convex hulls and the global optimal feasible solution may exist in a disjunctive programming model.

## 4. Solution Approach

## 4.1. Graph Models

We apply alternative graph and Gantt chart to analyse the feasibility of the train schedules step by step, as shown in Fig. 6.

In real-life environments, the train scheduling problem should consider blocking or hold-while-wait constraints, which means that a track section cannot release and must hold the train until next section on the routing becomes available. For example, as shown in

![](/api/attachments/CKWK65UU/fulltext/images/8af2e87fef38ceaf7e989dc7f1c42a888f3eea7d86559153492ef4385449ddff.jpg)

![](/api/attachments/CKWK65UU/fulltext/images/2c0a2edd5a08b351bbfd1be20f289278995c64c4360e0981700fcb316eebd682.jpg)  
(a) Blocking constraints analysis using alternative graph and Gantt chart

![](/api/attachments/CKWK65UU/fulltext/images/eb1c6235ef71645cdb5a716e80383b658579792fafc1c9fa0350b48d670026da.jpg)

(b) Infeasibility analysis for deadlock situation using alternative graph  
![](/api/attachments/CKWK65UU/fulltext/images/5ad58ee2bd51ac9c26a198f22c912f1ae1514d86d7b4ff28f142db14d0a116aa.jpg)  
(c) A deadlock-free schedule is achieved when two trains cross in a double-track section  
Fig. 6. Illustration of alternative graph and Gantt chart for train scheduling.

Table 2  
De<sup>fi</sup>nition of trains assigned for daily coal railing service.

<table><tr><td>Train ID</td><td>Ready Time (hr)</td><td>Departure Section Index</td><td>Departure Section Unit Index</td></tr><tr><td>0</td><td>0.00</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0.20</td><td>0</td><td>1</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>5</td><td>0.00</td><td>15</td><td>:</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>8</td><td>0.00</td><td>27</td><td>:</td></tr></table>

Fig. 6(a), operation 11 cannot be processed immediately after operation 7 until section $M _ { 3 }$ is released when operation 8 (the same-train successor of operation 7) can start to be processed on the inbound section $M _ { 4 } .$ . This implies that operation 7 has to block section M<sub>3</sub> due to the absence of buffer storage between sections $M _ { 3 }$ and $M _ { 4 } .$

Based on graph models, we analyse the deadlock and deadlockfree situations in a coal (single-line) rail network. As shown in Fig. 6(b), the deadlock situation is similar to a con<sup>fl</sup>ict when one outbound train and one inbound train are about to cross in a single-track section. The directed alternative graph of a blocking job-shop scheduling example with two trains and three sections in Fig. 6(b) shows that a cycle of operations $( \mathrm { i . e . , ~ } 0 _ { 1 } \mathrm { - } 0 _ { 2 } \mathrm { - } 0 _ { 3 } \mathrm { - } 0 _ { 5 } \mathrm { - } 0 _ { 4 } \mathrm { - } 0 _ { 1 } )$ is found, which implies that this schedule is infeasible (cyclic). For safety, the deadlock situation is strictly prohibited in train scheduling environments. In other words, the train schedule should be deadlock-free. Due to blocking conditions, the deadlock-free conditions may be guaranteed only when the resources are available in multiple units (i.e. multipletrack sections or crossing loop). If the single-track section (the single machine) M is changed to be a double-track section (the parallel machine with two units) $2 \mathrm { - } M _ { 2 } ,$ the deadlock-free status can be realised by obtaining such a feasible schedule shown in Fig. 6(c).

In real-life applications, industrial practitioners need to <sup>fi</sup>nd the preferable feasible solution for the large-size (e.g., 250 coal train roundtrips and 60 sections up to 30000 operations) cases in an economic and ef<sup>fi</sup>cient way. The challenges lie in providing representations that are expressive enough, guaranteeing good and fast solutions, and supporting ef<sup>fi</sup>cient constraint-based reasoning mechanisms. To make a good balance between computational complexity and solution quality and to easily identify the borders between theoretical and practical, we explore to propose a generic and <sup>fl</sup>exible methodology to model and solve the coal train scheduling problem in a standard and convenient way.

The problem is computationally intractable due to strong NPhardness, it cannot be solved by classical exact optimisation software packages; therefore the following integrated algorithm for coal transport decision-support system is developed for ef<sup>fi</sup>ciently <sup>fi</sup>nding the near-optimal or high-quality feasible solution. Due to considerable complexity, the fundamental framework of the integrated algorithm for a demand-responsive coal transport decision-support system is brie<sup>fl</sup>y described below.

De<sup>fi</sup>nition of track sections of a coal rail network.

<table><tr><td>Section ID</td><td>Number of Section Units</td><td>Section Length (km)</td><td>Section Description</td></tr><tr><td>0</td><td>2</td><td>6.5</td><td>Section at port</td></tr><tr><td>1</td><td>6</td><td>4.5</td><td>Depot</td></tr><tr><td>2</td><td>2</td><td>3</td><td>:</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>15</td><td>.</td><td>7.5</td><td>Section at Mine A</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>21</td><td>.</td><td>7.5</td><td>Section at Mine B</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>27</td><td>.</td><td>7.5</td><td>Section at Mine C</td></tr></table>

4.2. Integrated algorithm for coal transport decision-support system

Step 1 Apply the stockpiles strategy to determine the values of some critical supply-chain-management parameters, which will be used as an input data in coal train scheduling methodology.

1.1 Information collection and data validation from mine, railway and port operators.

1.2 Determine the total tonnages of coal to be railed from mines to coal terminal in a demand-responsive time window for determining the number of coal train roundtrips.

Step 2 Apply the SLEK constructive algorithm to build the initial feasible coal train timetable for a fleet of n coal train roundtrips.

2.1 Set the initial sequence of coal train roundtrips, containing only one coal train roundtrip that has the first priority determined by shipment demand or the longest traversing time.

2.2 Build the partial feasible train timetable using the SLEK constructive algorithm (see Appendix A for the detailed procedure of SLEK algorithm).

2.3 From $k  2 \ t o \ k  n \mathrm { : }$

2.3.1 Consider all possible combinations of $n { - } k + 1$ roundtrips (jobs) with k insertion positions to obtain a set of alternative permutation sequences of coal train roundtrips

2.3.2 Obtain the feasible coal train timetables of these alternatives and evaluate them;

2.3.3 Update the sequence of coal train roundtrips by selecting the best alternative that leads to the minimum makespan.

Step 3 Apply Tabu Search metaheuristic algorithm to optimise coal train timetable.

3.1 Generate an initial solution that is the solution constructed in Step 2.

3.2 Initialise a tabu list.

3.3 Perform a certain number of tabu search iterations:

3.3.1 Build up the neighbourhood based on the current solution.

3.3.2 Evaluate the neighbourhood and choose the best neighbour which is not a tabu or satisfies the aspiration criterion.

3.3.3 Set the best neighbour as the current solution and update the tabu list. If the stopping condition is met, go to Step 3.4.

3.4 Return the best solution found.

Step 4 View and evaluate the results. With adjusting the input data, do sensitivity analysis to find ways to improve the overall efficiency under various real-life scenarios.

## 5. Case Study

In this section, the proposed methodology is illustrated in depth by a case study and comprehensive sensitivity analysis is applied for identifying the key values, uncertainties, rationality and effects on the optimal decisions.

The data sets of this case study are established based on the reports of an Australian coal terminal [22]. Current onshore facilities at this coal terminal include a triplicate balloon loop for trains, one of which carries approximately 9,500 t (tonnes) coal. For such a typical coal train with the payload of 9,500 t, it contains 120 dump wagons with 5 locos. The best daily railing is about 205,000 t with 20 roundtrips. Coal unloading process is handled by bottom dump operation over two rail pits with separate takeaway conveyors, as shown in Fig. 1. Rail pits handles maximum 7,500 tonnes per hour. Conveyors belts is 1.6 m wide with 6.2 m/sec speed. Coal railed by trains can be temporarily stacked in the allocated locations in the coal stockpiles. The stockyard provides 4 stackers, 2 reclaimers and 6 dual stacker-reclaimers. The stack height is up to 13.2 m. The stockpiling rate is between 4,250 tph and 7,500 tph. The reclaiming rate is from 3,600 to 5,300 tph average per machine. The stockyard has 6 rows of stockpiles with a theoretical capacity of 1.5 million tonnes. The coal is reclaimed from the surge bins and then conveyed for loading through three ship loaders. There are three berths at this coal terminal. The largest shipment is about 210kt for the largest vessel with 240,000dwt (dead-weight tonnage). At this coal terminal, weekly shipping accommodates about 16 ships. Synchronised with Step 1 in the proposed algorithm in the previous section, in Table 4, the maximum number of roundtrips assigned for daily coal railing service is de<sup>fi</sup>ned as 20, because the best daily railing is 205,000 t with 20 roundtrips at this coal terminal.

Table 4  
Table 3  
De<sup>fi</sup>nition of coal railing routes.

<table><tr><td colspan="3">Route_A</td><td colspan="3">Route_B</td><td colspan="3">Route_C</td></tr><tr><td>Section Sequence</td><td>Train Speed (km/hr)</td><td>Train Direction</td><td>Section Sequence</td><td>Train Speed (km/hr)</td><td>Train Direction</td><td>Section Sequence</td><td>Train Speed (km/hr)</td><td>Train Direction</td></tr><tr><td>0</td><td>35.0</td><td>Outbound</td><td>0</td><td>35.0</td><td>Outbound</td><td>0</td><td>35.0</td><td>Outbound</td></tr><tr><td>1</td><td>60.0</td><td>Outbound</td><td>1</td><td>60.0</td><td>Outbound</td><td>1</td><td>60.0</td><td>Outbound</td></tr><tr><td>2</td><td>70.0</td><td>Outbound</td><td>2</td><td>70.0</td><td>Outbound</td><td>2</td><td>70.0</td><td>Outbound</td></tr><tr><td>:</td><td>:</td><td>Outbound</td><td>:</td><td>:</td><td>Outbound</td><td>:</td><td>:</td><td>Outbound</td></tr><tr><td>15</td><td>40.0</td><td>Outbound</td><td>:</td><td>:</td><td>Outbound</td><td>:</td><td>:</td><td>Outbound</td></tr><tr><td>15</td><td>35.0</td><td>Inbound</td><td>21</td><td>40.0</td><td>Outbound</td><td>:</td><td>:</td><td>Outbound</td></tr><tr><td>:</td><td>:</td><td>Inbound</td><td>21</td><td>35.0</td><td>Inbound</td><td>27</td><td>40.0</td><td>Outbound</td></tr><tr><td>2</td><td>65.0</td><td>Inbound</td><td>:</td><td>:</td><td>Inbound</td><td>27</td><td>35.0</td><td>Inbound</td></tr><tr><td>1</td><td>45.0</td><td>Inbound</td><td>:</td><td>:</td><td>Inbound</td><td>:</td><td>:</td><td>Inbound</td></tr><tr><td>0</td><td>30.0</td><td>Inbound</td><td>2</td><td>65.0</td><td>Inbound</td><td>:</td><td>:</td><td>Inbound</td></tr><tr><td></td><td></td><td></td><td>1</td><td>45.0</td><td>Inbound</td><td>:</td><td>:</td><td>Inbound</td></tr><tr><td></td><td></td><td></td><td>0</td><td>20.0</td><td>Inbound</td><td>2</td><td>65.0</td><td>Inbound</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>45.0</td><td>Inbound</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>30.0</td><td>Inbound</td></tr></table>

According to the above case study, the reasonable input data sets for the coal train scheduling problem are presented in Tables 1–5. Synchronised with Step 2 of the proposed integrated algorithm, Tables 1–5 are the input data for coal train scheduling, such as the de<sup>fi</sup>nition of trains (rolling-stocks), the de<sup>fi</sup>nition of track sections of a coal rail network, the de<sup>fi</sup>nition of coal railing routes, the de<sup>fi</sup>nition of roundtrips for daily coal railing service. The input data in Tables 1–5 can be transformed by the proposed SLEK constructive algorithm to the output result, namely, the feasible coal train timetable for a <sup>fl</sup>eet of coal train roundtrips. In Table 1, the <sup>fi</sup>rst column is the identity (ID) number of each train. The second column is the ready time of each train available to start coal railing service. The index of departure section of each train is given in the third column. In the case study, it is initially assumed that all trains depart from the port for daily coal railing service. All trains need to return to unload the coal at port within one day. Later, departure of different number of trains from both mines and port is investigated in sensitivity analysis.

In Table 2, the track sections of a coal rail network are de<sup>fi</sup>ned. The <sup>fi</sup>rst column gives the ID of each section. The number of section units is de<sup>fi</sup>ned in the second column. The third column presents the length of each section, measured in kilometre (km). The last column indicates whether this section is at port or at mine (e.g. Section 0 is at port and Sections 15, 21 and 27 are at three various mines).

In Table 3, the coal railing routes are de<sup>fi</sup>ned. For one coal railing route (e.g. Route\_A) departing from port, one train with the current earliest ready time at port is assigned, then departs from the port, traverses for some sections and arrives at the speci<sup>fi</sup>ed mine site (e.g. Mine A), loads the coal at mine, then traverses in a reverse section sequence, returns to the port and unloads the coal at port. For the de<sup>fi</sup>nition of each route (i.e. Route\_A, Route\_B and Route\_C) that departs from port, three columns are respectively given to de<sup>fi</sup>ne the section sequence, train speed (km/hr) and train direction (e.g. outbound or inbound) in each section. In a coal railing roundtrip, the train direction is changed from outbound to inbound in a mine section (e.g. Section 15 for Route\_A, Section 21 for Route\_B and Section 27 for Route\_C) after loading the coal.

De<sup>fi</sup>nition of roundtrips for daily coal railing service.

<table><tr><td>Roundtrip ID</td><td>Route Type</td><td>No. of Locos</td><td>No. of Wagons</td><td>Train Length (m)</td><td>Train Tonnages (t)</td><td>Loading Time at Mine(hr)</td><td>Unloading Time at Port (hr)</td></tr><tr><td>0</td><td>Route_A</td><td>5</td><td>120</td><td>2550</td><td>9,600</td><td>1.92</td><td>1.75</td></tr><tr><td>1</td><td>Route_B</td><td>5</td><td>110</td><td>2350</td><td>8,800</td><td>1.76</td><td>1.60</td></tr><tr><td>2</td><td>Route_C</td><td>4</td><td>100</td><td>2120</td><td>8,000</td><td>1.60</td><td>1.45</td></tr><tr><td>3</td><td>Route_A</td><td>5</td><td>115</td><td>2450</td><td>9,200</td><td>1.84</td><td>1.67</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>19</td><td>Route_C</td><td>4</td><td>101</td><td>2140</td><td>8,080</td><td>1.62</td><td>1.47</td></tr></table>

In Table 4, the de<sup>fi</sup>nition of coal train roundtrips for daily coal railing service is given. The <sup>fi</sup>rst column indicates the ID of each roundtrip. It is assumed that there are at most 20 roundtrips in total for daily service. The second column gives the route type for each roundtrip. For example, the route type of Roundtrip 1 is Route\_B, which means a train in this roundtrip will stop and load the coal in Mine B. The third column is the number of locos for this roundtrip. Determined by the coal tonnage to be railed, the number of wagons may be various with different roundtrips, as shown in the fourth column. The <sup>fi</sup>fth column calculates the train length (e.g. for Roundtrip 1, the train length is 5\*30+ 110\*20=2350 meters), in which the lengths of a loco and a wagon are respectively de<sup>fi</sup>ned as 30 m and 20 m. If the number of wagons is 120 and the payload of each wagon is 80 t, the total tonnages that a 5-loco train can carry is 120\*80=9,600 t, for example, for Roundtrip 0 as de<sup>fi</sup>ned in the sixth column. If the coal loading rate and unloading rate is 5,000 tph and 5,500 tph respectively, the loading time at the mine and unloading time at the port are calculated in terms of the formulae (i.e. train tonnages/loading rate or train tonnages/unloading rate), as shown in the last two columns. For example, the loading time at mine and the unloading time at port for Roundtrip 0 is 9,600 5,000=1.92 hours and 9,600/5,500=1.75, respectively.

Table 5  
The sensitive analysis of decisions on equipment and infrastructure upgrade

<table><tr><td>Cases</td><td>Makespan (hrs)</td><td>Efficiency improvement (%)</td></tr><tr><td>Original case</td><td>32.28</td><td>N.A.</td></tr><tr><td>Number of trains is increased from 5 to 10</td><td>18.92</td><td>(32.28-18.92)/32.28*100 = 41.39%</td></tr><tr><td>One bottleneck section is upgraded</td><td>18.81</td><td>(32.28-18.81)/32.28*100 = 41.73%</td></tr><tr><td>Sectional train speeds are increased by 10%</td><td>17.73</td><td>(32.28-17.73)/32.28*100 = 45.07%</td></tr></table>

![](/api/attachments/CKWK65UU/fulltext/images/c470e3be27c195cd3127683d1b881e97783056d21156251b0dca300f7e0403e1.jpg)  
Fig. 7. Sensitivity analysis on ef<sup>fi</sup>ciency improvement in terms of various numbers of trains for 20-roundtrip daily coal railing service.

Based on the above data sets, extensive computational experiments are performed for a coal transport system to make a better decision making on ef<sup>fi</sup>ciency improvement. Firstly, the proposed methodology can be used to compare train service costs and congestion costs with the various numbers of trains, and make quantitative advice on the investment of locos and wagons for improving coal railing service. The methodology can also be used for the decision making on identifying the bottleneck section. Entire corridor capacity can be considerably increased by only upgrading these type sections. These decisions include increasing the number of assigned trains in a demand-responsive time window, identifying and upgrading one bottleneck section, and increasing the sectional running speeds. For better comparison, the makespan values and the percentages of ef<sup>fi</sup>ciency improvement with various decisions are concluded in Table 5.

Initially 5 trains (rolling-stocks) are assigned and all depart from the port for 20 roundtrips as this is a realistic situation for daily coal railing service due to the fact that rolling-stocks are vital and expensive capital assets in coal railway industry. The initial coal train timetable is obtained and results in the makespan of 32.28 hours. While keeping the same order of roundtrips, if the number of assigned trains is increased from 5 to 10, the makespan of the new coal train timetable decreases from 32.28 to 18.81 hours and ef<sup>fi</sup>ciency improvement is calculated as (32.28-18.92)/32.28\*100=41.39% which is shown in

Table 5. For better decision making on the assignment of trains for 20-roundtrip daily coal railing service, the complete sensitivity analysis with various numbers of trains (i.e., 5 trains to 20 trains) is concluded in Fig. 7.

As summarised in Fig. 7, the assignment of 10 trains for a 20-roundtrip daily coal railing service is a desirable cost-effective case. It results in ef<sup>fi</sup>ciency improvement percentage by 41.39%, in comparison to the initial case with the assignment of only 5 trains. It is also found out that the ef<sup>fi</sup>ciency improvement becomes very marginal after the assignment of more than 10 trains. This indicates that the further ef<sup>fi</sup>ciency improvement cannot be greatly achieved after the saturation point (i.e., the assignment of 10 trains) is reached, due to the fact that the absolute maximum railing capacity of the overall coal rail network has been achieved at this saturation point.

Furthermore, a more sophisticated scenario is tested by departing trains from the port and mines instead of only from the port. In this case, the availability conditions of trains are much more complicated, as re<sup>fl</sup>ected from the integrated coal transport timetables shown in Figs. 8 and 9. The Gantt chart for the initial 15-roundtrip 28-section 9-train 3-ship integrated rail-stockpile-ship timetable is displayed in Fig. 8. The makespan of this initial coal train timetable obtained by the SLEK constructive algorithm is 17.25. Fig. 9 displays the Gantt chart for the optimised 15-roundtrip 28-section 9-train 3-ship rail-stockpile-ship timetable with the makespan of 14.46 found by metaheuristic algorithm. This results in ef<sup>fi</sup>ciency improvement by (17.25-14.46)/17.25\*100=16.17%, in comparison to the initial one with the makespan of 17.25.

![](/api/attachments/CKWK65UU/fulltext/images/7e2ea8b886a3bed4bbe2d31a06000859c10cf31ba9ba804e0c9e03e51a5cd992.jpg)  
Fig. 8. The initial 15-roundtrip 28-section 9-train 3-ship integrated coal transport timetable with the makespan of 17.25.

![](/api/attachments/CKWK65UU/fulltext/images/f6f934caf1d2cfdf4aeeeaba12ba5be777abfbb12af7be3327f2820c728e1d0f.jpg)  
Fig. 9. A near-optimal 15-roundtrip 28-section 9-train 3-ship integrated coal transport timetable with the makespan of 14.46

The extensive computational experimental in terms of different numbers of trains versus different numbers of roundtrips are conducted and the results are summarised in Table 6.

Ef<sup>fi</sup>ciency of the coal transport system is investigated for the different numbers of trains versus different numbers of roundtrips and results are summarised in Fig. 10.

According to the analysis in Fig. 10, makespans of different number of roundtrips using 7 trains are much larger than those of the same number of roundtrips with 9 trains. For example, for a 7-train 48-roundtrip case, the makespan is 129.98; in comparison, the makespan of 9-train 48-roundtrip case reduces to 50.56, which results in huge ef<sup>fi</sup>ciency improvement by (129.98-50.56)/129.98\*100=61.1%. It is also revealed that the railing ef<sup>fi</sup>ciency improvements for different numbers of roundtrips become very marginal if the number of trains is increased from 9 to 10. In this case, the assignment of 9 trains is regarded as a saturation point.

To the best of our knowledge, the integrated coal train scheduling problem is originated in this research and there are no results appropriate for comparison. Thus, the optimality performance of the solutions found by the proposed methodology can be evaluated by the lower bound. Here, we propose a formula to calculate the lower bound for the studied problem.

$$
L B = \sum_ {i = 1} ^ {2 n ^ {r}} p _ {i b} + \min _ {i \in n ^ {r}} \left(r _ {i} + \sum_ {j = 1} ^ {b - 1} p _ {i j} + \sum_ {j = b + 1} ^ {m} p _ {i j}\right)
$$

where $p _ { i j }$ is the sectional running time of an operation of Roundtrip i on Section $j ; r _ { i }$ is the ready time of Roundtrip $i ; u _ { j }$ is the number of units for each section $j ;$ b is the index of the bottleneck section that leads to the largest sum of processing times of operations. The lower bound is the maximum sum of the sectional running times of $n ^ { r }$ roundtrips on the bottleneck section plus the minimum sum of the sectional running times of other operations of a roundtrip. Based on extensive computational experiments, the average gap between the obtained solution and the lower bound is less than 10% for most instances, implying that the proposed algorithm may obtain the near-optimal or high-quality solutions.

Based on extensive computational experimental results and substantial sensitivity analysis, the following conceptual propositions are observed, analysed, validated and concluded as insightful and quantitative advices for improving capacity usage and operating ef<sup>fi</sup> ciency of coal transport system.

Proposition. The railing efficiency in a demand-responsive time window could be significantly improved with the assignment of additional trains but the further improvement becomes marginal after the saturation point is reached. There exists a resource-effectiveness ratio for determining the efficiency of train (rolling-stocks) usage for coal transport service:

$$
\Psi_ {\Delta_ {t}} = \frac {\mathrm{P} _ {\Delta_ {t}}}{\Omega_ {\Delta_ {t}}}
$$

$\Delta _ { t }$ is the number of additional trains. $P _ { \Delta _ { t } }$ is the extra benefit brought by efficiency improvement percentage (i.e., $\overset { \vartriangle } { \big ( } C _ { m a x } ^ { o r i } - C _ { m a x } ^ { o r i + \Delta _ { t } } \big ) / \bar { C } _ { m a x } ^ { o r i } \times 1 0 0 )$ due to the assignment of additional $\Delta _ { t } 1$ trains, where $C _ { m a x } ^ { o r i } { \dot { 1 } } s$ the original makespan and $\dot { C } _ { m a x } ^ { o r i + \Delta _ { t } } \dot { _ { 1 S } }$ the new makespan by assigning Δ trains more to the service in this demand-responsive time widow. $\Omega _ { \Delta _ { t } } i s$ the extra cost caused by assigning additional $\Delta _ { t }$ trains.

Proof. The cause of saturation point is that the absolute maximum capacity of railway network is reached. When trains depart only from port, the saturation point in this case study is close to the value of $( n ^ { t } = n ^ { r } / 2 )$ where $n ^ { t }$ is the number of trains and $n ^ { r }$ is the number of roundtrips. For example, the proof of Proposition is indicated in Fig. 7 that the further ef<sup>fi</sup>ciency improvement cannot be achieved after the saturation point (i.e., the assignment of $n ^ { t } = 1 0$ trains for $n ^ { r } { = } 2 0$ coal railing roundtrip in a demand-responsive time window). When trains depart both from mines and port, determination of the saturation point is much more dif<sup>fi</sup>cult; it can only be observed by extensive computational experiments and sensitivity analysis of train scheduling results by adjusting the input data (e.g., the different numbers of trains versus the different numbers of roundtrips). At the saturation point analysis, we have also considered time window length, number of roundtrips, loading time at mines, unloading time at port, capacity of crossing loops, traversing routes of roundtrips, departure of trains, etc. As shown in Fig. 10, the assignment of 9 trains is identi<sup>fi</sup>ed as the saturation point in this case. If the ratio $\Psi _ { \Delta _ { t } }$ is greater than one, it means that the added bene<sup>fi</sup>t brought by ef<sup>fi</sup>ciency improvement percentage is greater than the extra cost by assigning additional $\Delta _ { t }$ trains. Thus, it may be bene<sup>fi</sup>cial to assign more rolling-stocks (trains) for a <sup>fl</sup>eet of roundtrips in a demand-responsive time window.

Table 6  
Computational experiments results in terms of different numbers of trains versus different numbers of roundtrips when trains depart from port and mines.

<table><tr><td>Cases</td><td>Number of Trains</td><td>Number of Roundtrips</td><td>Initial Makespan</td><td>Best Makespan</td><td>CPU Times (seconds)</td><td>Improvement (%)</td></tr><tr><td>1</td><td>7</td><td>15</td><td>33.65</td><td>32.59</td><td>22</td><td>3.15</td></tr><tr><td>2</td><td>7</td><td>18</td><td>49.97</td><td>48.91</td><td>39</td><td>2.12</td></tr><tr><td>3</td><td>7</td><td>21</td><td>54.78</td><td>50.24</td><td>65</td><td>2.12</td></tr><tr><td>4</td><td>7</td><td>24</td><td>66.38</td><td>65.32</td><td>93</td><td>1.60</td></tr><tr><td>5</td><td>7</td><td>27</td><td>71.37</td><td>65.32</td><td>131</td><td>1.60</td></tr><tr><td>6</td><td>7</td><td>30</td><td>82.60</td><td>81.54</td><td>164</td><td>1.28</td></tr><tr><td>7</td><td>7</td><td>33</td><td>85.99</td><td>82.16</td><td>182</td><td>5.18</td></tr><tr><td>8</td><td>7</td><td>36</td><td>98.74</td><td>97.68</td><td>175</td><td>1.07</td></tr><tr><td>9</td><td>7</td><td>39</td><td>103.73</td><td>97.68</td><td>191</td><td>1.07</td></tr><tr><td>10</td><td>7</td><td>42</td><td>114.46</td><td>113.40</td><td>182</td><td>0.93</td></tr><tr><td>11</td><td>7</td><td>45</td><td>119.42</td><td>116.35</td><td>223</td><td>0.93</td></tr><tr><td>12</td><td>7</td><td>48</td><td>129.98</td><td>128.92</td><td>251</td><td>0.82</td></tr><tr><td>13</td><td>8</td><td>15</td><td>18.77</td><td>16.50</td><td>24</td><td>12.09</td></tr><tr><td>14</td><td>8</td><td>18</td><td>29.02</td><td>26.25</td><td>43</td><td>9.55</td></tr><tr><td>15</td><td>8</td><td>21</td><td>31.80</td><td>26.25</td><td>72</td><td>9.55</td></tr><tr><td>16</td><td>8</td><td>24</td><td>35.32</td><td>32.82</td><td>103</td><td>7.08</td></tr><tr><td>17</td><td>8</td><td>27</td><td>39.13</td><td>35.67</td><td>146</td><td>7.08</td></tr><tr><td>18</td><td>8</td><td>30</td><td>45.34</td><td>41.76</td><td>189</td><td>7.90</td></tr><tr><td>19</td><td>8</td><td>33</td><td>48.74</td><td>42.11</td><td>200</td><td>13.60</td></tr><tr><td>20</td><td>8</td><td>36</td><td>51.37</td><td>48.99</td><td>193</td><td>4.63</td></tr><tr><td>21</td><td>8</td><td>39</td><td>55.69</td><td>50.16</td><td>209</td><td>4.63</td></tr><tr><td>22</td><td>8</td><td>42</td><td>61.16</td><td>57.81</td><td>212</td><td>5.48</td></tr><tr><td>23</td><td>8</td><td>45</td><td>62.59</td><td>58.08</td><td>252</td><td>5.04</td></tr><tr><td>24</td><td>8</td><td>48</td><td>66.96</td><td>64.61</td><td>264</td><td>3.51</td></tr><tr><td>25</td><td>9</td><td>15</td><td>17.25</td><td>14.46</td><td>33</td><td>16.17</td></tr><tr><td>26</td><td>9</td><td>18</td><td>21.42</td><td>17.64</td><td>52</td><td>17.65</td></tr><tr><td>27</td><td>9</td><td>21</td><td>21.42</td><td>19.52</td><td>87</td><td>8.87</td></tr><tr><td>28</td><td>9</td><td>24</td><td>27.34</td><td>22.85</td><td>122</td><td>16.42</td></tr><tr><td>29</td><td>9</td><td>27</td><td>27.34</td><td>24.30</td><td>173</td><td>11.12</td></tr><tr><td>30</td><td>9</td><td>30</td><td>33.15</td><td>28.39</td><td>226</td><td>14.36</td></tr><tr><td>31</td><td>9</td><td>33</td><td>36.30</td><td>30.20</td><td>239</td><td>16.80</td></tr><tr><td>32</td><td>9</td><td>36</td><td>39.22</td><td>33.39</td><td>241</td><td>14.86</td></tr><tr><td>33</td><td>9</td><td>39</td><td>39.22</td><td>35.34</td><td>251</td><td>9.89</td></tr><tr><td>34</td><td>9</td><td>42</td><td>45.29</td><td>39.32</td><td>264</td><td>13.18</td></tr><tr><td>35</td><td>9</td><td>45</td><td>45.37</td><td>40.12</td><td>301</td><td>10.38</td></tr><tr><td>36</td><td>9</td><td>48</td><td>50.56</td><td>44.76</td><td>333</td><td>11.47</td></tr><tr><td>37</td><td>10</td><td>15</td><td>16.36</td><td>14.31</td><td>36</td><td>12.53</td></tr><tr><td>38</td><td>10</td><td>18</td><td>20.78</td><td>17.21</td><td>67</td><td>17.18</td></tr><tr><td>39</td><td>10</td><td>21</td><td>21.52</td><td>19.11</td><td>111</td><td>11.20</td></tr><tr><td>40</td><td>10</td><td>24</td><td>26.05</td><td>21.46</td><td>162</td><td>17.62</td></tr><tr><td>41</td><td>10</td><td>27</td><td>26.05</td><td>23.84</td><td>227</td><td>8.48</td></tr><tr><td>42</td><td>10</td><td>30</td><td>30.81</td><td>26.20</td><td>296</td><td>14.96</td></tr><tr><td>43</td><td>10</td><td>33</td><td>34.63</td><td>29.46</td><td>313</td><td>14.93</td></tr><tr><td>44</td><td>10</td><td>36</td><td>37.00</td><td>31.41</td><td>302</td><td>15.11</td></tr><tr><td>45</td><td>10</td><td>39</td><td>37.00</td><td>34.66</td><td>327</td><td>6.32</td></tr><tr><td>46</td><td>10</td><td>42</td><td>41.54</td><td>36.74</td><td>333</td><td>11.56</td></tr><tr><td>47</td><td>10</td><td>45</td><td>41.81</td><td>39.11</td><td>393</td><td>6.46</td></tr><tr><td>48</td><td>10</td><td>48</td><td>46.35</td><td>40.83</td><td>401</td><td>11.91</td></tr></table>

In summary, the proposition with the proposed train scheduling methodology could be applied as a useful quantitative decision making tool on how to use more current rolling-stocks or whether to buy additional rolling-stocks for mining transportation.

## 6. Conclusion

The coal railway industry is a capital intensive industry with large investment in infrastructure, equipment and employees. Operating a railway requires very complex decision-making processes due to the need to schedule several hundred roundtrips over thousands of kilometres distances. Even a small percentage of improvement in the ef<sup>fi</sup>ciency of the overall operation may bring signi<sup>fi</sup>cant <sup>fi</sup>nancial return. With the comprehensive sensitivity analysis, the proposed methodology is promising to provide the meaningful insights and quantitative advices on how to upgrade infrastructure and equipment, increase the railing capacity and improve the utilisation rate of coal rail network. As a result, the contribution of the proposed decision support system with train-stockpile-ship scheduling optimisation techniques to industry practice would be enormous.

The primary aim of this paper is to provide new modelling and solution techniques in the areas of strategic planning on coal shipment and operational scheduling on coal railing by developing an integrated demand-responsive decision support system. To this end, the operational capabilities in coal rail network will ultimately determine the performance of overall coal transport system. In a sense, scheduling models and algorithms at the operational level are the most important component of this comprehensive decision support system.

Alternative implementations of the proposed methodology have been investigated and alternative cases have been performed with detailed sensitivity analysis. The development of such an intelligent coal transport system may bring many bene<sup>fi</sup>ts towards achievements of some long-term goals including: i) determining the more ef-<sup>fi</sup>cient feasible operational coal train schedules; ii) increasing the railing capacity to the full potential so that after an event the system can still catch up and meet contract tonnages in a demand-responsive time window; iii) preparing the latent capacity to meet even the highest forecast tonnage demands; iv) offering accurate and quantitative advices on relatively balanced port and rail capacity expansion.

![](/api/attachments/CKWK65UU/fulltext/images/0fbbc2d24b28e5e9774ea31416ba2f8d9b09016e2f4aa987e25210b7f40b10f3.jpg)  
Fig. 10. Analysis of the system ef<sup>fi</sup>ciency in terms of different numbers of trains versus different numbers of roundtrips when trains depart from port and mines.

As for future scope of this research, the proposed methodology will be transferred and applied to other mining industries such as iron ore instead of coal mining industry. In addition, the proposed methodology will be extended to take a different perspective on robust and reactive scheduling by immunising deterministic train scheduling models against infeasibility caused by stochastic perturbations in model parameters and various dynamic factors due to the fact that unexpected events or accidents often occur in real-life train scheduling environments. More research works are needed to analyse and adopt more realistic constraints and speci<sup>fi</sup>ed requirements such as delay costs, stockpile rehandling, blending, shipment due windows, maintenance activities, etc. These future research directions will have the potential to lead to considerable theoretical and practical advancements in the <sup>fi</sup>elds of planning and scheduling, transportation and mining optimisation. As a result, more signi<sup>fi</sup>cant gains in optimal cost-effectiveness can be achieved for railway and mining industries.

## Appendix A. Pseudo codes of SLEK constructive algorithm

## Algorithm 1. Main procedure of SLEK constructive algorithm

1: initialize the results using given data of roundtrips, sections and trains

2: for each roundtrip do

3: get the index of this roundtrip

4: get the route type of this roundtrip

5: choose the earliest available train based on current train information

6: set the information of the current roundtrip by Algorithm 2

7: update the information of sections by Algorithm 8

8: update the information of trains by Algorithm 9

9: end for

## Algorithm 2. Roundtrip-Information-Set Algorithm

1: get the index of the current roundtrip

2: get the indexes of starting (iThStart) and ending (iThEnd) operations of this roundtrip

3: set the index of the current operation, iThCur=iThStart.

4: while (iThCurb= iThEnd) do

5: get the ready time (RTime) of the current operation

6: set the starting time (ETime) of the current operation by Algorithm 3

7: get the processing time (PTime) of the current operation

8: get the dwelling time (WTime) (i.e., loading time at mine or unloading time at port if existing) of the current operation

9: set the completion time (CTime) of the current operation: CTime=ETime+PTime+WTime

10: set the blocking time (BTime\_Pre) of the immediate predecessor (if existing) of the current operation: BTime\_Pre=ETime – CTime\_Pre

11: set the departure time (DTime\_Pre) of the immediate predecessor (if existing) of the current operation: DTime\_Pre= CTime\_Pre+BTime\_Pre

12: get the occupying time (OTime\_Pre) of the immediate predecessor (if existing) of the current operation

13: set the leaving time (LTime\_Pre) of the immediate predecessor (if existing) of the current operation: LTime\_Pre=DTime\_Pre+ OTime\_Pre

14: maybe change the current operation after <sup>fi</sup>ne-tuning all the predecessors (if existing) of the current operation by Algorithm 4

15: iThCur=iThCur+1

16: end while

## Algorithm 3. Set-Earliest-Starting-Time Algorithm

1: get the section index on the current operation

2: get the number of units on this section

3: for each section unit do

4: get the number of scheduled operations on this section unit

5: for each scheduled operation on this unit do

6: if the current operation could be inserted before/after this scheduled operation

7: set the earliest starting time accordingly

8: set the insertion position and section unit index

9: break

10: end if

11: end for

12: choose the section unit that leads to the earliest starting time

13: end for

## Algorithm 4. Fine-tune Algorithm

1: get the index of the current operation: iThCur

2: get the index of the starting operation: iThStart

3: for each operation iThOper from iThCur to iThStart do

3: check whether this operation is con<sup>fl</sup>icting by Algorithm 5

4: if this operation is con<sup>fl</sup>icting

5: eliminate the con<sup>fl</sup>ict by Algorithm 6

6: adjust the blocking time of the immediate predecessor of this con<sup>fl</sup>icting operation by Algorithm 7

7: end if

8: else

9: set iThCur=iThOper+ 1

10: break and return to Algorithm 2

11: end else

12: end for

## Algorithm 5. Check-Con<sup>fl</sup>ict Algorithm

1: get the index of section unit of the current checked operation (iThCur)

2: get the starting time (ETime\_Cur) and leaving time (LTime\_Cur) of the current operation

3: get the number of scheduled operation on this section unit

4: for each scheduled operation on this section unit do

5: get the starting time (ETime\_Sch) and leaving time (LTime\_Sch) of the scheduled operation

6: if ((ETime\_Sch>= ETime\_Cur && ETime\_SchbLTime\_Cur) || (ETime\_Cur>= ETime\_Sch && ETime\_CurbLTime\_Sch))

7: set the current checked operation as con<sup>fl</sup>icting

8: update the ready time of this operation: RTime\_Cur= max(ETime\_Cur, LTime\_Sch)

9: break

10: end if

11: end for

## Algorithm 6. Eliminate-Con<sup>fl</sup>ict Algorithm

1: get the index of the con<sup>fl</sup>icting operation

2: get the index of section unit of the con<sup>fl</sup>icting operation

3: get the updated ready time of the con<sup>fl</sup>icting operation

4: get the number of scheduled operations on this section unit

5: for each scheduled operation on this unit do

6: if the current operation could be inserted before/after this scheduled operation based on the updated ready time

7: set the earliest starting time accordingly

8: set the insertion position and section unit index

9: break

10: end if

11: end for

## Algorithm 7. Tune-up Algorithm

1: get the updated starting time of the con<sup>fl</sup>icting operation

2: get the completion time (CTime\_Pre) of the immediate predecessor

3: set the new blocking time (BTime\_Pre) of the immediate predecessor: BTime\_Pre=ETime\_Cur – CTime\_Pre

4: set the new departure time (DTime\_Pre) of the immediate predecessor of the current operation: DTime\_Pre=CTime\_Pre+BTime\_Pre

5: get the occupying time (OTime\_Pre) of the immediate predecessor of the current operation

6: set the new leaving time (LTime\_Pre) of the immediate predecessor of the current operation: LTime\_Pre=DTime\_Pre+OTime\_Pre

## Algorithm 8. Update-Sections Algorithm

1: get the index of the current scheduled roundtrip

2: get the number of operations of the current scheduled roundtrip

3: for each operation do

4: get the index of section unit on this operation

5: get the insertion position index on this section unit

6: update the sequence of operation information on this section unit according to insertion position index

7: end for

## Algorithm 9. Update-Trains Algorithm

1: get the index of the current train (rolling-stock)

2: update the indexes of section and section unit on which this train is currently staying

3: update the available time of the current train

## References

[1] A. Abdekhodaee, S. Dunstall, A.T. Ernst, L. Lam, Long term capacity planning at hunter valley coal chain: models and algorithms, in: Presented at the Proceeding of the Fifth Asia Paci<sup>fi</sup>c Industrial Engineering and Management Systems Conference, Gold Coast, Australia, 2004.

[2] A.S. Abrahams, C.T. Ragsdale, A decision support system for patient scheduling in travel vaccine administration, Decision Support Systems (2012), http://dx.doi.org/10 1016/j.dss.2012.05.007.

[3] M. Abril, M.A. Salido, F. Barber, Distributed search in railway scheduling problems, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 21 (2008) 744–755.

[4] E. Balas, Disjunctive programming: Properties of the convex hull of feasible points, Discrete Applied Mathematics 89 (1998) 3–44.

[5] E. Balas, J.M. Tama, J. Tind, Sequential convexi<sup>fi</sup>cation in reverse convex and disjunctive programming, Mathematical Programming 44 (1989) 337–350

[6] R.L. Burdett, E. Kozan, Techniques for absolute capacity determination in railways, Transportation Research. Part B 40 (2006) 616–632.

[7] R.L. Burdett, E. Kozan, Techniques for restricting multiple overtaking con<sup>fl</sup>icts and performing compound moves when constructing new train schedules. Mathe: matical and Computer Modelling 50 (2009) 314-328.

[8] R.L. Burdett, E. Kozan, A disjunctive graph model and framework for constructing new train schedules, European Journal of Operational Research 200 (2010 85–98.

[9] V. Cacchiani, A. Caprara, P. Toth, A column generation approach to train timetabling on a corridor, A Quarterly Journal of Operations Research 6 (2008) 125–142.

[10] A. Caprara, M. Monaci, P. Toth, P.L. Guida, A Lagrangian heuristic algorithm for a real-world train timetabling problem, Discrete Applied Mathematics (2006) 738–753.

[11] M. Carey, I. Crawford, Scheduling trains on a network of busy complex stations, Transportation Research. Part B 41 (2007) 159–178.

[12] Y.-H. Cheng, L.-A. Yang, A Fuzzy Petri Nets approach for railway traf<sup>fi</sup>c control in case of abnormality: Evidence from Taiwan railway system, Expert Systems with Applications 36 (2009) 8040–8048

[13] J.W. Chung, S.M. Oh, I.C. Choi, Ahybrid genetic algorithm for train sequencing in the Korean railway, Omega 37 (2009) 555–565.

[14] F. Corman, A. D'Ariano, D. Pacciarelli, M. Pranzo, A tabu search algorithm for rerouting trains during rail operations, Transportation Research. Part B 44 (2010) 175–192.

[15] F. Corman, A. D'Ariano, D. Pacciarelli, M. Pranzo, Assessment of <sup>fl</sup>exible timetables in real-time traf<sup>fi</sup>c management of a railway bottleneck, Transportation Research. Part C 20 (2010) 79–94.

[16] A. D'Ariano, D. Pacciarelli, M. Pranzo, A branch and bound algorithm for scheduling trains in a railway network, European Journal of Operational Research 183 (2007) 643–657.

[17] A. D'Ariano, D. Pacciarelli, M. Pranzo, Assessment of <sup>fl</sup>exible timetables in real-time traf<sup>fi</sup>c management of a railway bottleneck, Transportation Research. Part C 16 (2008) 232–245.

[18] K. Fagerholt, A computer-based decision support system for vessel <sup>fl</sup>eet scheduling - experience and future research, Decision Support Systems 37 (2004) 35–47.

[19] M. Fischetti, D.S. Salvagnin, A. Zanette, Fast approaches to improve the robustness of a railway timetable, Transportation Science 43 (2009) 321–335.

[20] K.M.v. Hee, A. Lapinski, OR and AI approaches to decision support systems, Decision Support Systems 4 (1988) 447–459.

[21] W.-L. Hsu, M.J. Prietula, G.L. Thompson, A mixed-initiative scheduling workbench integrating AI, OR and HCI, Decision Support Systems 9 (1993) 245–257.

[22] H. van der Klauw, Coal Rail Infrastructure Master Plan: Queensland Rail, Australia 2009.

[23] J.T. Krasemann, Design of an effective algorithm for fast response to the re-scheduling of railway traf<sup>fi</sup>c during disturbances, Transportation Research. Part C 20 (2012) 62–78.

[24] A. Kuo, E. Miller-Hooks, H.S. Mahmassani, Freight train scheduling with elastic demand, Transportation Research. Part E 46 (2010) 1057–1070.

[25] G. Lamptey, S. Labi, Z. Li, Decision support for optimal scheduling of highway pavement preventive maintenance within resurfacing cycle, Decision Support Systems 46 (2008) 376–387.

[26] Y. Lee, C.-Y. Chen, A heuristic for the train pathing and timetabling problem Transportation Research. Part B 43 (2009) 837–851.

[27] F. Li, Z. Gao, K. Li, L. Yang, Ef<sup>fi</sup>cient scheduling of railway traf<sup>fi</sup>c based on global information of train, Transportation Research. Part B 42 (2008) 1008–1030.

[28] C. Liebchen, The <sup>fi</sup>rst optimized railway timetable in practice, Transportation Science 42 (4) (2008) 420–435

[29] S.Q. Liu, E. Kozan, Scheduling trains as a blocking parallel-machine job shop scheduling problem, Computers and Operations Research 36 (2009) 2840–2852.

[30] S.Q. Liu, E. Kozan, Scheduling Trains with Priorities: A No-Wait Blocking Parallel-Machine Job-Shop Scheduling Model, Transportation Science 45 (2) (2011) 175–198.

[31] S.Q. Liu, E. Kozan, A hybrid shifting bottleneck procedure algorithm for the parallel-machine job-shop scheduling problem, Journal of the Operational Research Society 63 (2) (2012) 168–182.

[32] Y.-H. Min, M.-J. Park, S.-P. Hong, S.-H. Hong, An appraisal of a columngeneration-based algorithm for centralized train-con<sup>fl</sup>ict resolution on a metropoli tan railway network, Transportation Research. Part B 45 (2011) 409–429.

[33] M. Ozbayrak, R. Bell, A knowledge-based decision support system for the management of parts and tools in FMS, Decision Support Systems 35 (2003) 487–515.

[34] D. Petrovic, A. Duenas, S. Petrovic, Decision support tool for multi-objective job shop scheduling problems with linguistically quanti<sup>fi</sup>ed decision functions, Decision Support Systems 43 (2007) 1527–1538.

[35] M.A. Salido, A non-binary constraint ordering heuristic for constraint satisfaction problems, Applied Mathematics and Computation 198 (2008) 280–295.

[36] G. Singh, D. Sier, A.T. Ernst, R. Oyston, P. Welgama, Long term capacity planning at hunter vallev coal chain: models and algorithms, in: The 2oth national conference of Australian Society for Operations Research incorporating the 5th international intelligent logistics system conference, Gold Coast, Australia, 2009.

[37] W.V. Wezel, R.J. Jorna, The SEC-system reuse: support for scheduling system development, Decision Support Systems 26 (1999) 67–87.

[38] J. Yuan, I.A. Hansen, Optimizing capacity utilization of stations by estimating knock-on train delays Transportation Research. Part B 41 (2007) 202-217

[39] X. Zhou, M. Zhong, Bicriteria train scheduling for high-speed passenger railroad planning applications, European Journal of Operational Research 167 (2005) 752–771.

[40] K.G. Zografos, K.N. Androutsopoulos, A decision support system for integrated hazardous materials routing and emergency response decisions, Transportation Research, Part C 16 (2008) 684–703.

[41] The Australian, \$1bn rail logiam hits exports http://www.theaustralian.com au/news nation/bn-rail-logiam-hits-exports/story-e6frg6nf-1111113615425 May 26. 2007.

[42] The Australian, \$500m system to boost freight rail, http://www.australianit.news. com.au/story/0,23874700-15306,00.html June 17, 2008.

Erhan Kozan is the Chair Professor of Operations Research in the Discipline of Mathematical Sciences, Queensland University of Technology (QUT), Australia. He has had 37 years of industrial, managerial, teaching and research experience in the areas of operations research. Professor Kozan has acted as principal investigator for over 25 long-term industrial projects, and 18 competitive national and international research grants since 1996 in the area of health, <sup>fi</sup>nance, metal production, car and truck production, railways, seaport transportation, logistics and supply chain. He is the author of a book, ten softwares and over 200 journal papers, and conference papers. He is the editor/associate editor of seven journals and works as a referee of over 30 international journals. He has supervised over 30 postgraduate research students. He is currently supervising three PhD students in the transportation area. He established the Operations Research Group\_QUT in 1996. He is the former president of the Asia Paci<sup>fi</sup>c Industrial Engineering and Management Society and the Australian Society for Operations Research. He is an expert in disciplinary research across operations research and scheduling theory. His current research focuses on the area of healthcare process optimisation, mining scheduling and train scheduling.

Shi Qiang Liu is currently working as a research fellow in the Discipline of Mathematical Sciences at Queensland University of Technology (QUT). He had been awarded the PhD degree in Operations Research from (QUT). His PhD thesis was nominated for the University Outstanding Doctoral Thesis Award. He received the New Outstanding Researcher Medal and the Dean's Award for the Academic Excellence at QUT. He obtained his Master of Engineering in Industrial & Systems Engineering from the National University of Singapore. He has pub lished more than 15 papers in international journals including Transportation Science, International Journal of Production Economics, Computers and Operations Research, Journal of the Operational Research Society, Advances in Engineering Software, and Asia-Paci<sup>fi</sup>c Journal of Operational Research. He has a solid background in planning and scheduling, arti<sup>fi</sup>cial intel ligent, optimisation algorithms, simulation and network <sup>fl</sup>ow modelling.
