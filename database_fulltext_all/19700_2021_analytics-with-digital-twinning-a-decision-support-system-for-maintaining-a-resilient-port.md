---
otero_id: 19700
otero_key: "ASMAP633"
title: "Analytics with digital-twinning: A decision support system for maintaining a resilient port"
authors: "Chenhao Zhou; Jie Xu; Elise Miller-Hooks; Weiwen Zhou; Chun-Hung Chen; Loo Hay Lee; Ek Peng Chew; Haobin Li"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113496"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analytics with digital-twinning: A decision support system for maintaining a resilient port

![](/api/attachments/ASMAP633/fulltext/images/afff7db020449d82d8ef8a0cdeaeb4b792ad6382fc88862efa4a468022b98c76.jpg)

Chenhao Zhou <sup>a</sup>, Jie Xu <sup>b,\*</sup>, Elise Miller-Hooks <sup>c</sup>, Weiwen Zhou <sup>c</sup>, Chun-Hung Chen <sup>b</sup>, Loo Hay Lee <sup>a,d</sup>, Ek Peng Chew <sup>a</sup>, Haobin Li <sup>a</sup>

<sup>a</sup> Department of Industrial Systems Engineering and Management, National University of Singapore, Singapore

<sup>b</sup> Department of Systems Engineering & Operations Research, George Mason University, United States

<sup>c</sup> Department of Civil, Environmental and Infrastructure Engineering, George Mason University, United State

<sup>d</sup> Centre for Maritime Studies, National University of Singapore

## A R T I C L E I N F O

Keywords: Port resilience Digital-twinning-driven analytics Decision support systems Port performance Simulation-optimization Maritime transport

## A B S T R A C T

In this paper, a Decision Support System (DSS) with digital twinning-based resilience analysis is proposed as a modern tool for port resilience computation and updating. The proposed DSS assesses the resilience of a port under possible disruptive events given its design, operations and potential pre-defined post-event recovery ac tions to mitigate the impact of the disruption. Digital twinning provides the fidelity required to realistically predict port performance with taken post-event recovery actions under various possible disruptive events. In addition to hedging against impacts from probabilistically known disruption events, this approach also enables inclusion of ordinary operational uncertainties within the resilience evaluation. This is not generally feasible with other existing resilience quantification approaches. To tackle computational challenges of applying a digital twin for real-world size applications, an optimal computing budget allocation policy is adopted to improve computational efficiency. Results of numerical experiments using a real-world size port demonstrate the effec tiveness of the proposed DSS and criticality of accounting for ordinary uncertainties in operations in resilience estimation.

## 1. Introduction

Ports play a critical role supporting global and regional trade as the primary interface for cargo flows between land and sea. Hazards and other causes of disruption can significantly impact their operations. To aid in minimizing hazard impacts, a resilience concept is adopted to evaluate port readiness and potential adaptation strategies for improved continuation of performance in the face of any number of potential hazard scenarios. Building on work by Chen and Miller-Hooks [14] for larger, rail-based intermodal networks, Nair et al. [46] recognized that a port’s resilience comes from an ability to quickly and cost-effectively restore functionality to near pre-event levels. This characteristic de pends on the port’s design, operations and post-event response capacity. Resilience is computed through a mathematical modeling approach that embeds within its constraints details of operational strategy or readiness option, it is necessary to predict the impact of disruptions on port op erations and probable effectiveness of recovery actions to mitigate a disruption event’s impacts. Such prediction requires detailed models of the operations and impact effects on the facilities that are difficult to capture in closed mathematical form. For this purpose, a decision sup port system (DSS) for port resilience quantification is developed that exploits digital twinning capabilities and advances in simulationoptimization. Building on the mathematical modeling approach, the digital twin replaces relevant constraints in the model to capture oper ational details, enabling replication of the multitude of complex, inter acting activities, and greater realism in resilience estimation.

Glaessgen and Stargel [28] described the digital twin concept as integrating physical models through multi-physics, multi-scale and stochastic simulation, and exploiting data received from both historical records and sensor updates. Digital twinning seeks to replicate or “mirror” real life of that which it twins. Improvements in computing technologies have enabled digital twinning of detailed systems to sup port complex decision making in various areas, including production planning and condition monitoring in manufacturing [31,53], fault detection in marine applications [16,33], and building energy man agement [25]. This paper seeks to expand its application to port

resilience analysis.

Recent green port initiatives have stimulated the electrification of container terminals in new developments or upgrades at ports in Rot terdam, Dubai, Shanghai and Singapore. Although electrification significantly reduces terminal emissions, it leads to new vulnerabilities in port operations caused by power supply disruption. Fig. 1 illustrates a typical terminal layout, where power substations are built along the wharf to distribute power supply for terminal lighting and powering vessels, equipment and other supporting devices. When power supply is insufficient, the port must shut down some equipment. Because of complex interactions among equipment and processes, it is likely not clear what is the best allocation of the limited power that would maxi mally preserve the performance of the port, and a mathematical modeling approach as used in prior port resilience studies will not fully capture the operational details needed for such determination. Addi tionally, power disruptions are relatively rare and the electrification of ports is a recent phenomenon. Consequently, many port operators do not have prior experience with power disruptions. Adaptations taken in terms of re-allocation of limited power to preserve or restore function ality are key to the port’s resilience. Yet, without assistance from a reliable DSS, port operators would likely suspend operations altogether until power supply is restored to normal levels.

The DSS proposed herein enables the computation of the port’s resilience to a given disruption or set of possible disruption scenarios, along with the selection of the best post-disruption action to take for any given scenario. An added methodological contribution is the inclusion of ordinary operational uncertainty in modeling post-disruption opera tions, which is made possible via the use of the digital twin. The approach enables evaluation of numerous potential recovery actions that provide adaptive capacity, a key component of resilience. This evaluation, however, requires numerous simulation runs. Because dig ital twin runs are time-consuming, there are important trade-offs be tween making enough runs for accurate estimates and computation time. For real-world size applications, especially when used to support real-time operations, efficient run designs with good statistical accuracy are needed. It is likely that with insufficient runs to guarantee statistical accuracy the DSS will select a sub-optimal recovery action for a given scenario and, simultaneously, develop an incorrect (reduced) resilience assessment. To tackle this computational challenge, the proposed DSS integrates a state-of-the-art simulation-optimization method known as optimal computing budget allocation (OCBA) (Chen and Lee [12,13]) to determine the number of simulations to be executed for each candidate recovery action under a given simulation budget.

OCBA formulates its own optimization problem, where the decision variables are the numbers of simulation runs for each recovery action, and the objective function is the estimated probability of correctly selecting the best action using noisy simulation estimates. For a given simulation budget, e.g., constrained by the time-window that a port operator needs to respond to a disruption, OCBA solves this optimization problem and determines the number of simulation runs to spend on each scenario. It aims to achieve the highest probability of correctly selecting the best action among all possible simulation fixed-budget allocation schemes. As demonstrated in a case study, OCBA reduces the number of runs required to accurately identify the best recovery action and, thus, makes the application of the high-fidelity digital twin approach feasible.

Generally, this study shows how a traditional industry like maritime logistics can be transformed through a new era of Industry 4.0 or In dustrial Internet. Instead of relying on experience-based decision mak ing by human operators, using various data sources, the proposed DSS can be part of a digitized Terminal Operating System (TOS) that effi ciently performs planning, control, and monitoring of a modern port. The DSS can be integrated into the TOS as a planning-level module. In the event of a power shortage, the DSS collects and compiles information on future activities, human resources, and equipment resources from other TOS modules and recommends actions to the port operator. The proposed DSS provides such a capability, enabling a port operator to optimally configure equipment to minimize the impact of a power disruption event. This study may further stimulate the development of digital-twin enabled decision support in other traditional industries.

The remainder of the paper is organized as follows: Section 2 reviews literature related to decision support for maritime systems, digital twinning, and recent relevant developments in resilience assessment. The DSS is described in Section 3. Section 4 presents results from numerical experiments and conclusive remarks are offered in Section 5.

## 2. Literature review

The maritime industry is a mature, but traditional industry in which decisions associated with the majority of activities, including key op erations, rely heavily on human experience. In recent years, DSSs have been proposed to aid decision-making at ports and in maritime shipping to achieve greater efficiency and higher levels of throughput with lower total cost. Fagerholt [21] introduced a DSS for vessel fleet schedule planning. This tool has been used successfully by several shipping companies. Similarly, Fazi et al. [24] developed a DSS to generate schedules for the transportation of containers by barge from sea to inland terminals. A model-driven DSS was developed to evaluate oper ational policies and manage equipment taking an overall terminal perspective in [35]. Fazi [23] most recently proposed a DSS framework for the stowage of maritime containers in the context of inland shipping. Also, recently, Irannezhad et al. [32] presented a prototype DSS for horizontal and vertical cooperation among freight agents involved in port logistics.

![](/api/attachments/ASMAP633/fulltext/images/ef12635f4cc40cd7b60cbe12f703ab2a279572297bc3800a351c11844757271a.jpg)  
Fig. 1. Terminal layout under disruption caused by power shortage.

Several additional works proposed a DSS for use at the operational level. Ursavas [54] created a DSS that determines a joint berthing and crane allocation strategy. Wong et al. [58] and Lee et al. [34] developed DSSs for speed optimization in liner shipping. Optimizing speeds can reduce fuel use and emissions. DSSs were also developed in recent works to make berth and equipment allocation decisions in bulk terminals [48] and container stacking allocation decisions in container terminals [41].

With the rapid technological developments of the last several years, it is now possible to simulate complex industrial systems and develop and run digital twins in real-time settings. Digital twins offer an ability to complete off-line”what-if” analysis in a close-to-reality virtual envi ronment before implementing tested actions in actual operations. Mansouri et al. [42] reviewed dozens of articles in the literature on decision support to enhance environmental sustainability in maritime shipping. Among the 26 papers reviewed that focused on modeling, five used simulation. Furthermore, simulation-based decision support has been developed for different purposes, including: operational changes to minimize environmental impact of port activities [9]; operational and tactical decision-making on cargo flows between sea and dry ports [22]; and truck arrival coordination at port gates [66].

Applying digital twin technologies in operations requires computa tional speed. To reduce the digital twin run times for this purpose, simulation-optimization has emerged as a promising area. In simulationoptimization, the objective function of an optimization problem is approximated rather than computed exactly (see Andradottir ´ [3], Fu et al. [26] and Xu et al. [60] for background). A comprehensive review on simulation-optimization in maritime operations can be found in [67]. For performance improvement, simulation-optimization was adopted for designing a terminal gate system [62], vehicle control at terminal gates [18,57,66], yard crane scheduling [30], storage space assignment [40], berth allocation [36,55], quay crane scheduling [1,37,63], and more. For high-level planning purposes, simulation-optimization has been applied for fleet sizing and empty container repositioning in [19,20,59], container supply chain network design in [29] and terminal resource configuration in [39].

Port resilience, an ability to efficiently restore port functionality to pre-event levels, relies on both planning- and operational-level de cisions. At the planning level, recovery actions must be designed and preparations must be taken to enable their implementation should they be called for in an event. In the past decade, an increasing number of researchers have developed metrics, models and solution methods for post-disaster resilience quantification in the context of a variety of civil infrastructure lifelines and services. Few works, however, focus on ports. Nair et al.’s work (building on work by Chen and Miller-Hooks [14]), one of the earliest works on resilience measurement for a transportation application, focused on the resilience of ports and other intermodal connections [46]. This work provides the basis for the solution frame work development herein. Nair et al. modeled port operations through a network conceptualization of physical entities and processes, and used a network throughput ratio as a measure of resiliency. They generated thousands of hazard events as input. Mathematical representation of the operations was comprehensive, but simplistic in comparison to the digital-twin based methodology described herein. Moreover, it assumed deterministic knowledge of all aspects of port operations except the occurrence of a disaster event and its impacts. That is, all activities, e.g. vessel berthing, container stacking and train car loading, were all assumed to occur with a deterministically-known, constant rate. The approach described herein accounts for uncertainty in foreknowledge of these and other workings of a port as is the case in both ordinary and

extraordinary circumstances.

Three other relevant works on resilience of either in-land or seaports include: Pant et al. [47], Shafieezadeh and Burden [50], and Alyami et al. [2]. Pant et al. [47] proposed and evaluated several measures for prioritizing repairs for an inland waterway port using simulation to replicate port operations. A metric based on an integral of post-event performance over time was proposed for measuring seaport seismic resiliency in (Shafieezadeh and Burden [50]) and a fuzzy rule-based method for use in evaluating post-disruption criticality for container terminals was proposed by Alyami et al. [2]. The aim of this latter work is to reduce some of the stringency needed by exact methods associated with knowledge of uncertain quantities, such as risk.

While additional works consider resilience and/or reliability in the context of the larger maritime system or a port network (see Asadabadi and Miller-Hooks [4] for more detail), the authors know of no prior work that has attempted port resilience computation with the granularity enabled by digital twinning. Nor has any prior work accounted for or dinary operational uncertainties in evaluating port resilience. The DSS with digital twinning-based resilience analysis described herein fills these gaps. It further creates the possibility of real-time port resilience computation and updating, which has not been considered previously in the literature.

## 3. Decision support system for port resilience analysis

The architecture of the proposed DSS is presented in Fig. 2. The DSS has two key modules: recovery analysis and resilience analysis. For a given physical environment and disruption scenario(s), the recovery analysis module, enabled by digital twinning, evaluates candidate re covery actions. The resilience analysis module uses these outputs from the recovery analysis module to compute user-defined resilience met rics, which are then provided to the terminal manager to evaluate the resilience level of the terminal under potential disruption scenarios.

The DSS includes three additional units that support the generation of the physical environment: (1) terminal configurations that parame terize equipment, layout, and operational processes; (2) disruption scenarios with their physical and operational impacts and occurrence probabilities; and (3) candidate recovery actions with their effects. These provide input to the recovery and resilience analysis modules.

In general, the DSS offers port resilience assessment from two as pects. In a planning phase, it assesses the resilience to the chosen po tential scenarios given its design, operations and post-event actions made to be at the ready. When the port is in operation, the DSS is applied on a portion of a larger TOS to aid in choosing the post-event actions for which to prepare. It identifies which actions to take given limited, postevent resources and disruption event impact realization. Adaptive ac tions taken post-event are key to any system’s resilience. Next, Sections 3.1 and 3.2 provide details on the enabling technologies of the recovery analysis module, the digital twin for a container terminal and OCBA for reducing the computational effort needed to identify best recovery ac tions to mitigate disruption impacts through smart simulation run de signs. The resilience analysis module is discussed in Section 3.3.

The specification of the physical environment, generation of disruption scenarios and the corresponding sets of candidate recovery actions are exogenous to the DSS itself. These components are thus not discussed in this section. Section 4 presents a case study on power supply shortage disruptions and shows how disruption scenarios and recovery actions are specified for resilience assessment of a real-life size port.

## 3.1. Digital twinning

Fundamental to digital twinning is discrete event simulation (DES), a technology that has been widely adopted as a practical tool for system performance evaluation for maritime as well as other industries. A highfidelity DES model can describe a complex system that closely mirrors the real system, capturing details of model component operations, interactions between components and system dynamics.

![](/api/attachments/ASMAP633/fulltext/images/e473aad56974adea01c86835161bd9ae39886c102f220b6c3f6d58365f28b262.jpg)  
Fig. 2. Proposed DSS architecture for maintaining a resilient port.

Maritime studies using commercial DES software abound in the literature. Some examples include: AutoMod [49,64], Arena [10,57], em-Plant [11], Modsim [27] and FlexTerm [61].

Although these software products provide user-friendly interfaces and animation capabilities, they lack flexibility for integration with external analysis algorithms. Therefore, the digital twin used in the DSS is developed using an open-source O<sup>2</sup>DES.Net DES framework ([39],a). O<sup>2</sup>DES.Net has been successfully used to model operations of terminal horizontal transport networks [65] and terminal gate systems [66]. With the integration of an external simulation-optimization algorithm, O<sup>2</sup>DES.Net was also used to optimize terminal configuration [39].

Fig. 3 depicts the hierarchical structure of the digital twin model for a container terminal. At the highest level, the model is made up of a terminal module, a vessel generator, and an external truck generator. Within the terminal module, there are three components: 1) quay area, which includes berth management and quay crane (QC) operations; 2) yard area, which includes yard space management and yard crane (YC) operations; and 3) traffic network, which connects quay and yard areas by way of automated guided vehicles (AGVs). Each component has entities representing terminal equipment or resources. For example, the quay area consists of several QC sub-models. Instead of using a single server to represent a QC, the sub-model consists of multiple servers to represent the hoist, trolley and gantry, along with their interactions (see Li et al. [38] for details). The yard area follows the same structure, where the YC sub-model consists of multiple servers. The traffic network is repre sented by a network of servers based on the method in [66]. Each server corresponds to a segment of the road network, and the service rate is dynamically adjusted according to the number of AGVs using the server to simulate traffic congestion.

![](/api/attachments/ASMAP633/fulltext/images/2f0a6d484ed1b972008a160c128e6e7798559c6b14455f558c6be2f4b8701c5b.jpg)  
Fig. 3. Container terminal digital twin modeling.

The overall simulation logic is depicted in Fig. 4. There are three types of container activities, including import, export and transshipment operations. Importing activities discharge containers from vessels to the yard block and eventually to external trucks. Exporting activities first receive containers from external trucks and load them to the yard block, and then load the containers from the yard block onto vessels. Trans shipment activities are between vessels and the yard block. These three activities can be further summarized into two major container flows, i.e., the discharging flow, consisting of container movements from vessels to the yard block, and loading, which moves in the opposite direction of discharging flows.

The discharging and loading operations are both initialized by the vessel generator. When a new vessel is generated and docks at the berth, containers for discharging and loading are generated and scheduled. From the container’s perspective, each container passes through multi ple simulation components while simultaneously interacting with re sources within the component. Using discharging as an example, when a vessel arrives, a set of QCs is assigned to the vessel for a duration that ends when all planned activities are complete. A discharging operation will trigger the QC to pick up the container, move it from sea side to land side, and then wait for the arrival of an empty AGV for retrieval, Once the container is discharged to the AGV, the AGV is scheduled to travel to its destination at the yard block. Shortly before AGV arrival at the yard block, the container will schedule a YC for pickup. When the container is lifted from the AGV, the AGV is released to respond to another request. Once the container is stored in the yard block, the YC is released and the discharging operation finishes. The loading operation has the opposite sequence of activities. Corresponding to this, details of the uncertain quantities in the digital twin model are given in Table A.4 in the Appendix.

For smooth coordination and operations, terminals often rely on the

![](/api/attachments/ASMAP633/fulltext/images/0440d72e3380515db73eabe210a6eb24432702993b6a125892c48a1b3a952b22.jpg)  
Fig. 4. Digital twin modeling logic.

TOS to make planning and scheduling decisions for vessels, vehicles and containers. Since resources are shared among all activities, highly complex interactions occur and it is necessary to apply experience-based operational policies. Examples of such policies include that: 1) the number of QCs assigned to a vessel depends on the vessel’s length and workload; 2) a pool of vehicles is assigned to serve a specific vessel; 3) the number of vehicles in the pool is dynamically determined by the vessel workload; 4) vehicles follow a first-available-first-serve policy for service by cranes; and 5) containers are allocated to the yard following a 80–20 rule, which stipulates that 80% of containers to be loaded onto a departing vessel must be allocated to yard locations within 20% of the vessel-to-yard range (defined as the maximum distance from the departing vessel to any point in the yard via the traffic network). Most of the policies used in this model are based on actual approaches used by operators at some of the world’s busiest ports.

The digital twin has two groups of input parameters that define runtime control and experimental scenarios. Primary run-time control pa rameters include days of the warm-up period, days of the running period, and a random number seed. A warm-up period is needed, because the simulation is initialized from an empty terminal, i.e., no vessel is moored and all equipment is idle, including all vehicles parked at the wharf. After the warm-up period, the simulation is run for addi tional time to output the actual operational statistics. The random number seed of each simulation run is also set to produce independent and identically distributed (IID) observations.

Experimental scenario parameters include the total number of acti vated equipment/resources, such as the total number of AGVs, QCs, berths, and yard blocks. As a yard block is vertical to the wharf, YCs cannot move to other yard blocks. Hence, the number of YCs per block is fixed.

There are numerous performance indicators that may provide pertinent output data for a container terminal, and each terminal operator may have its own preferred indicators. Commonly used in dicators include: terminal throughput, ship turnaround time, ship waiting time, gross quay crane rate, and berth-on-arrival (BoA) rate (or the BoA ratio) [17,43,52]. User preferences can guide the customization of the digital twin output.

Input parameters and output measures are not limited to these items. The open-source nature of O<sup>2</sup>DES.Net allows the tuning of other parameters, such as arrival vessel pattern (including vessel type, vessel length, draught, workload, arrival rate), external truck arrival rate, and other equipment parameters.

The digital twin model developed by the Center of Excellence in

Modeling and Simulation for Next Generation Ports (C4NGP) with support and input from Maritime and Port Authority of Singapore and port operators in Singapore, including the simulation logic, model pa rameters, and simulation results, has been verified and validated by port operators using actual system-level port performance measurements of BoA and gross crane rates for a target annual throughput.<sup>1</sup>

The digital twin model used in this paper was further upgraded to include battery-powered AGVs and a facility allocation strategy for assigning AGVs to charging stations at regular intervals.

## 3.2. Optimal computing budget allocation

The value of each recovery action in mitigating the effects of a disruption scenario on the port is assessed using the digital twin. Benefiting from the granularity of the digital twin and its outputs, thi study explicitly considers ordinary operational uncertainty and, as part of resilience computation, performs multiple IID simulation replications to estimate the chosen key performance indicator (KPI). This KPI may be the expected throughput, machine utilization or a measure of on-time performance, for example. The KPI used in the case study is a function of the number of BOAs. The KPI of action x is estimated by the sample average from N(x) simulation replications:

$$
\overline {{{Y}}} (x) = \frac {\sum_ {n = 1} ^ {N (x)} Y _ {n} (x)}{N (x)},\tag{1}
$$

where $Y _ { n } ( x )$ is the nth IID simulation estimate of the KPI for x. For a set of I candidate recovery actions $X = \{ x _ { i } , i = 1 , . . . , I \}$ , the best action is selected as

$$
\widehat {i} ^ {*} = \arg \max _ {i = 1, \dots , I} \overline {{Y}} (x _ {i})\tag{2}
$$

Denote the action that achieves the highest KPI by x \*. As N(x) in creases, $\overline { { Y } } ( \boldsymbol { x } )$ converges to the true KPI with a rate of $O ( 1 / \sqrt { N } )$ under mild conditions, and thus the correct selection will be achieved when $\widehat { \widehat { i } } ^ { * } = \widehat { i } ^ { * }$ . However, when the simulation budget is limited, there may be significant estimation errors in ${ \overline { { Y } } } ( { \boldsymbol { x } } )$ and thus selecting the best action is subject to error, $\mathrm { i . e . , } \stackrel { \wedge ^ { * } } { i } \neq i ^ { * }$ . This problem is especially relevant when a computationally expensive digital twin model is used to evaluate a large number of recovery actions. In the DSS, if the probability of incorrect selection is high, the recovery analysis module would then frequently return sub-optimal recovery actions, and the resilience analysis module would produce erroneous estimates of resilience level.

To address this problem, the recovery analysis module integrates OCBA, a state-of-the-art simulation optimization algorithm, to optimally determine $N ( x _ { i } ) , i = 1 , . . . , I .$ Given a total simulation budget of $T$ rep lications, OCBA computes an allocation scheme that maximizes the probability of correct selection (PCS), $\mathbb { P } \Big ( \uparrow \ ' = i \ ' \Big )$ . Let $\delta ( x _ { i } ) = Y ( x _ { i } ^ { * } ) - Y$ (x<sub>i</sub>) for any $i \neq i ^ { * }$ . Under the assumption that the sampling distribution of Y (x ) is normal with mean $Y ( x _ { i } )$ and variance $\sigma ^ { 2 } ( x _ { i } )$ , and is independent across actions, the asymptotically optimal allocation of simulation budget satisfies

$$
\frac {N (x _ {i})}{N (x _ {l})} = \left(\frac {\delta (x _ {l}) / \sigma (x _ {l})}{\delta (x _ {i}) / \sigma (x _ {i})}\right) ^ {2}, i, l \neq i ^ {*},
$$

$$
N (x _ {i ^ {*}}) = \sigma (x _ {i ^ {*}}) \sqrt {\sum_ {x _ {i} \neq x _ {i ^ {*}}} \frac {N ^ {2} (x _ {i})}{\sigma^ {2} (x _ {i})}}.\tag{3}
$$

By the central limit theorem, the normal sampling distribution assumption holds approximately as the BoA rate is obtained from the average of many random samples generated during simulation runs. When OCBA is implemented, sample means and sample variances calculated from $N _ { 0 }$ initial simulation replications are used as estimates of δ(x ) and σ(x ), i.e. $\overline { { \delta } } ( x _ { i } ) = \overline { { Y } } ( x _ { i ^ { \ast } } )$ − Y(x ) and sample standard devia tion s(x ) are used as estimates of δ(x ) and $\sigma ( x _ { i } )$ in (3). N(x ) can be readily obtained through solution of (3). Because of estimation errors in $\overline { { \delta } } ( x _ { i } )$ and $\overline { { \sigma } } ( x _ { i } )$ , it is not recommended to compute the allocation of the total simulation budget using $\overline { { \delta } } ( x _ { i } )$ and $\overline { { \sigma } } ( x _ { i } )$ estimated from these $N _ { 0 }$ initial replications. Instead, a sequential procedure is used to incre mentally allocate simulation budget. The procedure starts with $N _ { 0 }$ replications allocated to each solution to obtain initial estimates of $\delta ( x _ { i } )$ and σ(x ). Then $N ( x _ { i } )$ are computed through solution of (3). The procedure then allocates the next simulation replication to the solution with the largest deficit, i.e., the solution with the largest $\begin{array} { r } { N ( x _ { i } ) \mathrm { ~ - ~ } N _ { 0 } . } \end{array}$ The procedure then updates $\overline { { \delta } } ( x _ { i } ) , \ \overline { { \sigma } } ( x _ { i } )$ , and $N ( x _ { i } ) .$ , and calculates the new allocation. It keeps iterating until the simulation budget has been exhausted. See Chen and Lee [12] for more details.

Experimental results from application of the DSS on a case study in the next section will show the effectiveness of applying the OCBA within the recovery analysis module and, ultimately, resilience computation in the resilience analysis module.

## 3.3. Resilience analysis

For a given disruption scenario s and set of candidate recovery ac tions $X ( s ) = \{ x _ { 1 } , . . . , x _ { I } \}$ , the recovery analysis module returns the best recovery action $x _ { i } { } ^ { * }$ and the corresponding post-disruption performance of the port $Y ( x _ { i } ^ { * } ) .$ Denote pre-event performance as $Y _ { 0 } .$ Miller-Hooks et al. [44] and Chen and Miller-Hooks [14] defined the resilience level of an intermodal freight transportation network as a network’s capa bility to resist and recover from a disruption or disaster.They suggest a resilience metric that uses a ratio of post-event to pre-event performance levels. Following this definition and approach, the resilience level of the port under disruption scenario s is computed as

$$
R (s) = \frac {Y (x _ {i ^ {*}})}{Y _ {0}}.\tag{4}
$$

With this core capability, the proposed DSS supports advanced

Table 1  
Recovery actions for Scenarios 1 to 3.

<table><tr><td rowspan="2">ID</td><td colspan="2">Scenario 1</td><td colspan="2">Scenario 2</td><td colspan="2">Scenario 3</td></tr><tr><td>QCs</td><td>AGVs</td><td>QCs</td><td>AGVs</td><td>QCs</td><td>AGVs</td></tr><tr><td>1</td><td>29</td><td>36</td><td>25</td><td>30</td><td>21</td><td>24</td></tr><tr><td>2</td><td>28</td><td>44</td><td>24</td><td>38</td><td>20</td><td>32</td></tr><tr><td>3</td><td>27</td><td>52</td><td>23</td><td>46</td><td>19</td><td>40</td></tr><tr><td>4</td><td>26</td><td>60</td><td>22</td><td>54</td><td>18</td><td>48</td></tr><tr><td>5</td><td>25</td><td>68</td><td>21</td><td>62</td><td>17</td><td>56</td></tr><tr><td>6</td><td>24</td><td>76</td><td>20</td><td>70</td><td> $16^{\#}$ </td><td> $64^{\#}$ </td></tr><tr><td>7</td><td>23</td><td>84</td><td> $19^{\#}$ </td><td> $78^{\#}$ </td><td>15</td><td>72</td></tr><tr><td>8</td><td> $22^{\#}$ </td><td> $92^{\#}$ </td><td>18</td><td>86</td><td> $14^*$ </td><td> $80^*$ </td></tr><tr><td>9</td><td>21</td><td>100</td><td> $17^*$ </td><td> $94^*$ </td><td>13</td><td>88</td></tr><tr><td>10</td><td>20</td><td>108</td><td>16</td><td>102</td><td>12</td><td>96</td></tr><tr><td>11</td><td> $19^*$ </td><td> $116^*$ </td><td>15</td><td>110</td><td>11</td><td>104</td></tr><tr><td>12</td><td>18</td><td>124</td><td>14</td><td>118</td><td>10</td><td>112</td></tr><tr><td>13</td><td>17</td><td>132</td><td>13</td><td>126</td><td></td><td></td></tr><tr><td>14</td><td>16</td><td>140</td><td>12</td><td>134</td><td></td><td></td></tr><tr><td>15</td><td>15</td><td>148</td><td></td><td></td><td></td><td></td></tr><tr><td>16</td><td>14</td><td>156</td><td></td><td></td><td></td><td></td></tr></table>

Note: default actions are indicated with $\# ;$ the best post-event recovery actions are indicated with \*.

probabilistic resilience analysis. For example, if there is a probability distribution function $F ( \cdot )$ defined over the disruption scenario space ${ \mathcal { S } } ,$ the average resilience level of a port is given by

$$
R = \int_ {s \in \mathscr {S}} R (s) d F (s)\tag{5}
$$

With K IID scenarios sampled from $\mathcal { S }$ using $F ( \cdot ) ,$ , the DSS would then estimate R by

$$
\overline {{{R}}} = \frac {\sum_ {k = 1} ^ {K} R (s _ {k})}{K}.\tag{6}
$$

The resilience analysis module can also output data to plot histo grams showing the distribution of R(s) and better inform operators on the performance of the port under potential disruption scenarios in set ${ \mathcal { S } } .$

The generation of a disruption scenario set $\mathcal { S }$ and the associated candidate recovery actions $\{ X ( s ) , s \in \mathcal { S } \}$ is specified by the port oper ator and is external to the DSS. The case study reported in Section 4 provides one example on how $\mathcal { S }$ and $\{ X ( s ) , s \in \mathcal { S } \}$ may be specified. The focus herein is on showing the capability of the DSS to efficiently assess each R(s) for a given scenario s and set of recovery actions X(s).

## 4. Case study

This section presents a case study based on the knowledge gained from previous projects with port operators. It demonstrates the capa bility of the DSS in assessing port resilience under several potential power supply disruption scenarios. The physical infrastructure studied has 7 berths and a total berth length of 2700 m, as would be present at a medium to large terminal. The expected annual throughput is 7 million Twenty-foot Equivalent Units (TEUs), which is practically achievable and is based on knowledge gained from operator experience. Due to confidentiality considerations, the case study used realistic, but syn thetic data.

Average estimated BoA rates achieved by default and DSS-selected recovery actions.

<table><tr><td>Scenario ID</td><td>BoA rate under default action</td><td>BoA under DSS action</td><td>Inherent coping capacity</td><td>Resilience</td></tr><tr><td>1</td><td>79.39%</td><td>91.90%</td><td>80.53%</td><td>93.23%</td></tr><tr><td>2</td><td>60.92%</td><td>76.66%</td><td>61.80%</td><td>77.77%</td></tr><tr><td>3</td><td>43.39%</td><td>55.45%</td><td>44.01%</td><td>56.25%</td></tr></table>

Note: the BoA rate before disruption is 98.58%

## 4.1. Disruption scenarios and recovery actions

During a disruption due to a power supply shortage, instead of running equipment under rated capacity, a subset of the QCs and AGVs would need to be shut down. AGVs rely on charging stations for power and must be recharged at regular intervals. With fast charging tech nology, the recharging time for each AGV during the day is considered to be inconsequential. Hence, it is assumed that power demand by the traffic system is correlated to the number of AGVs. Unaffected re sources/equipment, such as berths and YCs, will be operated as usual. In reality, the shortage can have a much broader impact. For example, the reduced wireless communication connectivity would affect the remote control of equipment, and the reduced lighting level in the terminal area would affect equipment throughput rates.

In practice, the equipment configuration is set according to expert input, e.g., each berth (350 m to 400 m) is equipped with 4 to 5 QCs. The ratio between QC and AGV is also a fixed number. In this study, the default configuration is set as 32 QCs and 128 AGVs under normal operating circumstances. The ratio of AGVs to QCs is 4. One AGV re quires 150 kilowatts (kWs) and one QC requires 1,200 kWs. The total power demand is, thus, 57,600 kWs.

The BoA rate is used as the KPI in this study. Usually, customers such as vessel owners expect prompt berthing of their vessels upon arrival. BoA evaluates if the arriving vessel is able to berth at the terminal within a contracted time window (usually 2 h). Achieving a high BoA rate would not only benefit terminal business with more contracts, but also maintain well-managed sea channel flows, which is a big concern for local maritime authorities.

Three power supply disruption scenarios are investigated. In prac tice, many port operators would choose to suspend operations until power supply is restored to normal, because they lack experience in responding to power disruptions. By this action, the BoA rate and resilience level would both be 0. Another action deemed by port oper ators as reasonable would be to adjust the numbers of activated AGVs and QCs in the TOS to follow the same ratio as is used under standard operating conditions. Here, the default recovery action is set to create an AGV to QC ratio of approximately 4:1 subject to the reduced power supply. This choice of a 4:1 ratio is based on common industrial practice, and results of runs using this design ratio serve as a benchmark to evaluate the effectiveness of the proposed digital-twin enabled DSS. The three tested disruption scenarios and corresponding default actions are as follows:

• Scenario 1: 70% power shortage, power supply of 40,320 kW, 22 QCs and 92 AGVs, and ratio 4.18;

• Scenario 2: 60% power shortage, power supply of 34,560 kW, 19 QCs and 78 AGVs, and ratio 4.11; and.

• Scenario 3: 50% power shortage: power supply of 28,800 kW, 16 QCs and 64 AGVs, and ratio 4.

The port operator may also consider other combinations of QCs and AGVs that do not follow the routine 4:1 ratio. Because QC is the primary resource, the number of QCs varies between a minimum and maximum number incrementing by one, based on input from operators in Shanghai and Singapore ports. The remaining power supply is used for the AGVs. Table 1 lists all candidate recovery actions for the scenarios.

## 4.2. Experimental design

To obtain statistically valid estimates of the BoA rate. each simulation replication has a three-day warm-up period, followed by a one-day running period during which the BoA rate is measured. 1000 IID simulation replications were conducted to obtain estimates of the BoA rate under each recovery action. Simulations were conducted on a Dell Precision Tower 7810 machine running Windows 10 OS with an Intel Xeon Processor E5–2695 v4 (18 cores, 2.1GHz) and 64GB memory. Even with 30 simulation runs running in parallel, more than three days were required to finish all runs. The sample average BoA rates from the 1000 replications were used to select the best recovery action for each sce nario (indicated with \*) in Table 1. Note that default actions (indicated with #) were not the best recovery actions in all three scenarios.

Scenario 1  
![](/api/attachments/ASMAP633/fulltext/images/711111da8775da6dcb3bfcda742f3a3b3b60de89af3a69fd354e0f42a39a973a.jpg)  
(a) Scenario 1 average estimated BoA rates

Scenario 2  
![](/api/attachments/ASMAP633/fulltext/images/7128a284d202ee137f3e9a1cc6553eb6241a12081f8d2b2d08fcbe8670bcc201.jpg)  
(b) Scenario 2 average estimated BoA rates.

Scenario 3  
![](/api/attachments/ASMAP633/fulltext/images/4dfe5c11404e609d595d638bf14f6c0ea8b3556a54c28c7fce9bfa0fad9912c4.jpg)  
(c) Scenario 3 average estimated BoA rates.  
Fig. 5. Comparison between stochastic and deterministic solutions.

## 4.3. Recovery and resilience analysis

Table 2 reports BoA rates under different power disruption scenarios achieved by default and best recovery actions. Without the DSS, the default action would be to operate the AGVs and QCs following the routine 4:1 ratio subject to the reduced power supply. The table refers to the default approach as the inherent coping capacity of the port, defined as the ratio of the BoA rate under the default action to the pre-event BoA rate (98.58%). Port resilience is calculated using Eq. (4). The difference between resilience and inherent coping capacity values is due to the implementation of a best recovery action for the given scenario realization.

![](/api/attachments/ASMAP633/fulltext/images/796e25fa4a920bee6d0a00fb22094ac2787deb3bf1c0c7f30af12ab62ddef306.jpg)  
(a) Scenario 1 post-event BoA box plot.

![](/api/attachments/ASMAP633/fulltext/images/7a7bbc1dd336d1c3cf05808fcb4f6a0f2f7b17a7ffb9af283e8c5625d936dcba.jpg)  
(b) Scenario 2 post-event BoA box plot.

![](/api/attachments/ASMAP633/fulltext/images/6b904339eec91c63572c7c4b2eaf15b21eab5de35172f8e0149ea2084467810b.jpg)  
(c) Scenario 3 post-event BoA box plot.  
Fig. 6. Box plots of estimated BoAs with 1000 replications.

The results show that when the extent of the disruption is small, e.g., a 30% drop in power supply as in scenario 1, the port can maintain a BoA rate close to its pre-event level by implementing the best recovery action selected by the DSS, and, thus, outperforming the default action by 12.51%. For 40 and 50% decreases in power supply, the DSSrecommended recovery actions outperform the default action by 15.74% and 12.06%, respectively.

## 4.4. Value of the stochastic solution

The digital twin integrated in the DSS encompasses key sources of randomness in port operations, thus, accounting for true variation in ordinary operations. To examine the value of this fully stochastic approach, in this section, the best recovery actions selected by the sto chastic digital twin, referred to as stochastic solutions, are compared to the best actions selected by a deterministic version of the digital twin model. The deterministic digital twin model is adapted from the sto chastic digital twin model by fixing vessel arrival patterns (including vessel sizes and workloads), truck arrival patterns, and crane service rates to the mean values of the corresponding probability distributions obtained from the stochastic digital twin model.

This deterministic version of the digital twin model still contain some randomness embedded within it, because the digital twin model implements randomized operational decision rules for yard allocation and traffic management that are difficult to pre-set. Those randomized decision rules, if removed, could create significant traffic jams within the port, and thus, were not predetermined. 1000 IID simulation repli cations were run for each of the recovery actions under all three sce narios as was conducted in the earlier stochastic runs. Fig. 5 compares BoA rates for different recovery actions estimated by the stochastic and (mostly) deterministic digital twin models, respectively. Corresponding, detailed BoA rates can be found in Table B.5 in the Appendix.

It can be observed from Fig. 5 that sub-optimal recovery actions are suggested under scenarios 1 and 3 under the deterministic runs. In scenario 1, the deterministic model chose action 9 with an estimated BoA rate of 95.79%. However, the actual (if account properly for randomness in operations) BoA rate of action 9 is only 87.39%. In comparison, the stochastic model chose action 11 with an estimated BoA rate of 91.90%. For scenario 3, the deterministic model chose action 7 with BoA rate 52.59%. A BoA rate of 55.45% is achieved by the sto chastic model which identifies action 8 as optimal.

For scenario $^ { 2 , }$ while the solutions of both model versions coincide, the deterministic model incorrectly overestimates the BoA rate at 87.96% instead of 76.66% as estimated by the stochastic model. This estimate may lead port operators to mistakenly believe the port is resilient under this disruption scenario; they might fail to adequately respond to the disruption. This problem is greater under scenario $^ { 3 , }$ where the deterministic solution estimates a BoA rate of 72.35%, again leading the port operator to seriously underestimate the impact of a 50% power shortage. Based on predictions from the stochastic model, the BoA rate is only 55.45% rather than 72.35% even with the best sto chastic solution. Fig. 5 illustrates that the BoA rate is most often over estimated through use of deterministic assumptions.

In summary, comparisons with the deterministic digital twin demonstrate both the value of accounting for stochasticity in system operations that arise routinely, and the danger of assuming their mean values in assessing resilience whether or not randomness in the disruption event is considered. Despite its importance, this aspect may not have been previously considered in the resilience literature, and was not considered in port resilience previously.

## 4.5. Comparison of simulation policies

When a disruption occurs, a port operator must make a decision in a short time window. Therefore, it would not be practical to run 1000 replications to estimate the BoA rate for each recovery action. There is a need to reduce the number of runs while maintaining a similar level of accuracy in the results.

Fig. 6 shows box plots of post-event BoA rates for different recovery actions from the 1000 simulation replications. Using scenario 1 as an example, because the medians of the BoA rates (middle lines in the boxes) achieved by actions 1 to 7 are much lower than those of actions 9 to 12, intuitively far fewer simulation replications are needed for actions 1 to 7 than for actions 9 to 12. The question is then how many simulation replications are needed, and how should they be allocated across actions knowing that equal allocation is neither efficient nor necessary. In the following, results from two sets of experiments are reported to compare the efficiency gain achieved by OCBA compared to an equal allocation (EQ) approach.

To measure the PCS achieved by EQ or OCBA, EQ or OCBA would be applied to allocate a fixed simulation budget to all I actions. The best action would then be selected using simulation estimates. This proced ure would be repeated M times using different random number seeds each time to produce IID simulation output. Suppose out of those M experiments, EQ or OCBA correctly selected the best solution m times. The PCS (denoted by p) achieved by EQ or OCBA would then be esti mated by

$$
\widehat {p} = \frac {m}{M}.\tag{7}
$$

However, such an experimental procedure would incur a prohibi tively high computational workload, because M needs to be large to produce an accurate estimate of PCS. This is because the relative error of the PCS estimate in (7) is given by [45].

$$
\operatorname{RE} (\widehat {p}) = \frac {\sqrt {\operatorname{Var} (\widehat {p})}}{p} = \sqrt {\frac {1 - p}{M p}}.\tag{8}
$$

For example, when $p = 0 . 5 ,$ the M required to achieve a 5% relative error is $M = 4 0 0$ . If the simulation budget is 1000 runs in each experi ment, it would require 400,000 simulation runs to produce one reliable PCS estimate, a prohibitively high computational workload.

To maintain a manageable computational workload, instead of generating new IID simulation outputs, IID random samples from an empirical distribution for the simulated BoA rate are used in the experimental procedure to measure PCS. The empirical distribution is constructed as follows. For a given action x, denote by $Y ( x ) = \{ Y _ { 1 } ( x ) ,$ $Y _ { 2 } ( x ) , . . . , Y _ { N } ( x ) \}$ } a set of simulation outputs from N IID replications. The probability mass function $P _ { E } ( \cdot )$ of the empirical distribution for the simulation output Y(x) is given by

$$
P _ {E} (y) = \frac {1}{N} \sum_ {j = 1} ^ {N} \mathbb {I} \left(Y _ {j} (x) = y\right),\tag{9}
$$

where $\mathbb { I } ( \cdot )$ is the indicator function, i.e., $\mathbb { I } \big ( Y _ { j } ( x ) = y \big ) = 1$ when $Y _ { j } ( x ) <$ $y ,$ and 0 otherwise. Sampling from $P _ { E } ( \cdot )$ is equivalent to random sam pling with replacement from the set Y(x). This re-sampling technique is known as bootstrapping, and it produces statistically valid estimates of the PCS. While a large value of $M , \boldsymbol { \mathrm { e . g . } } M = 1 0 , 0 0 0$ , is typically required [6], the experimental procedure is still very efficient, because it no longer requires running the actual digital twin. In the following, for each scenario and action, estimated BoA rates from N = 1000 IID simulations were used to construct empirical distributions, and M is set to 10,000.

To examine the PCS achieved by EQ or OCBA as a function of simulation budget, the number of simulation replications allocated to any action, denoted as $N ,$ by EQ is varied from 10 to 60. The total simulation budget T is thus $T = N \times$ I replications, where I is the number of actions to evaluate $( I = 1 6 ,$ 14. and 12 for scenarios $1 , 2 ,$ and $^ { 3 , }$ respectively). OCBA allocates these $N \times I$ simulation replications to all I actions using the allocation policy described in Section 3.2. For OCBA, the initial number of replications is set to $n _ { 0 } = 1 0$

The measured PCS as a function of the number of simulation repli cations consumed by EQ/OCBA is plotted in Fig. 7. The total simulation budget for scenario 1 is $6 0 \times 1 6 = 9 6 0$ replications, because there are 16 recovery actions and the maximum N is 60. For scenarios 2 and $^ { 3 , }$ the total simulation budget is $6 0 ~ \times ~ 1 4 ~ = ~ 8 4 0$ and $6 0 ~ \times ~ 1 2 ~ = ~ 7 2 0$ respectively.

Fig. 7 reveals a substantial risk of selecting a sub-optimal action when there is not a statistically sufficient number of simulation repli cations. In scenarios 1 and 2, using the sample averages from 10 simu lation runs, the PCS values were both lower than 0.5. The values obtained for scenario 3 had only minimally better performance. Greater numbers of replications are required to achieve higher PCS values and realize the benefits of using a stochastic digital twin.

The outcome shows that with a given simulation budget of 60 rep lications per candidate action, EQ was only able to achieve a PCS of 0.65 for scenario 1, 0.52 for scenario 2, and 0.78 for scenario 3. In contrast, OCBA achieved a PCS of 0.88, 0.56, and 0.92 for scenarios $1 , 2 ,$ and $^ { 3 , }$ respectively. For scenarios 1 and 3, OCBA produces large improvements in PCS over EQ. Scenario 2 turned out to be challenging, because it has two actions (9 and 10) that are difficult to rank correctly. Even in thi scenario, though, OCBA outperforms EQ.

![](/api/attachments/ASMAP633/fulltext/images/38b169496c0debf77c64391468ab918c347227994ae7d8c3ea1d77ecc82fe0ce.jpg)  
(a) Scenario 1.

![](/api/attachments/ASMAP633/fulltext/images/e08a653e462e9c89c28a23de5b7e446ddc71cf167df001c9ed6f72908903a4bc.jpg)  
(b) Scenario 2.

![](/api/attachments/ASMAP633/fulltext/images/9cd8ae35d16e5cfddee25af5ea1d55a3220fcdec8fd42c9a6d6022a9e18eab8d.jpg)  
(c) Scenario 3.  
Figure 7: PCS achieved by EQ and OCBA.  
Fig. 7. PCS achieved by EQ and OCBA.

Table 3  
OCBA speed-up factors over EQ as a function of the number of EQ replications N.

<table><tr><td>Scenario ID</td><td>N = 20</td><td>N = 30</td><td>N = 40</td><td>N = 50</td><td>N = 60</td></tr><tr><td>1</td><td>1.33</td><td>1.76</td><td>2.00</td><td>2.27</td><td>2.61</td></tr><tr><td>2</td><td>1.43</td><td>1.88</td><td>2.11</td><td>2.00</td><td>2.31</td></tr><tr><td>3</td><td>1.54</td><td>1.88</td><td>2.11</td><td>2.08</td><td>2.40</td></tr></table>

Another perspective is to examine the speedup achieved by using OCBA over EQ. Table 3 summarizes the speed-up factor of OCBA over EQ. The speed-up factor is defined as the ratio between the number of replications that EQ used to achieve a specific PCS and the number of replications that OCBA spent to achieve the same PCS. For example, in scenario 1, with N = 60 and thus a total of 960 simulation runs expen ded, EQ achieved a PCS of 0.65. In comparison, OCBA only used 368 runs to achieve the same level of PCS. Then the speed-up factor is 960/ $3 6 8 = 2 . 6 1 $ . Speed-up factors for $N = 2 0 , 3 0 , 4 0 , 5 0 , 6 0$ are reported in Table 3.

For all three scenarios, as the simulation budget increases, the speed up factor obtained by using OCBA also increases. OCBA, therefore, achieves the largest speed-up factors at the most desirable (i.e. highest) PCS values. This is is ideal, because it enables reliable estimates.

## 5. Conclusions and future work

As disruptions can significantly impact port operations, maintaining a resilient port is essential. In this paper, a DSS is developed that ex plores digital twinning and simulation-optimization capabilities for resilience assessment with recovery action optimization. The digital twin replicates detailed port operations that cannot be captured through more traditional mathematical modeling approaches. Digital twinning also enables the modeling of uncertainty in the disruption events, as well as subsequent port recovery operations. The authors are not aware of any previous work in the resilience literature that computes resilience with the granularity enabled by digital twinning or that accounts for ordinary operational uncertainties in resilience computation. Outcomes of the case study showed that omitting ordinary operational uncertainty from port models embedded within a resilience estimation methodology can significantly overestimate resilience levels, erroneously suggesting to port operators that their port is resilient. Consequently, they might fail to adequately prepare for, or respond to, disruptions. In some cases, sub-optimal, post-event response action might also be applied.

The proposed framework integrates OCBA, a state-of-the-art simu lation-optimization algorithm, to improve the computational efficiency for real-world size applications. In a case study based on a real-world container terminal, three power supply disruption scenarios were analyzed. Power supply disruption is an understudied but important hazard for ports, especially as they become increasingly dependent on power for automated activities and use more clean energy solutions. This work shows that using the proposed DSS provides an optimal equipment configuration that may greatly alleviate the impact of a power supply disruption.

In the case study, compared to routine equipment configurations, the optimal configuration was able to increase the BoA rate by 15.74 per centage points. The value of including ordinary operational uncertainties within the resilience evaluation was demonstrated via comparisons with a mostly deterministic digital twin. Deterministic solutions were not only sub-optimal, but substantially underestimated (by up to 24.97 percentage points) the impact of disruptions, thus overestimating resilience levels. Such erroneous estimates may cause a port operator to fail to adequately respond to disruptions. Numerical results also showed that OCBA can reduce the amount of computations required by the DSS to make an accurate decision by as much as 2.40 times.

To further extend this work, there are several directions that might be explored. Examples follow:

(1) Chen and Miller-Hooks [14] pointed out that a port’s resilience relies on the ability to withstand the disruption event with min imal loss in function, which depends on effective preparedness, such as training, pre-determining operational modifications, and prepositioning resources. The proposed DSS framework can be extended to optimize such preparedness decisions as in [44]. As both preparedness analysis and recovery analysis require highfidelity simulation run evaluation, two-stage simulation budget allocation methods might help improve the overall computa tional efficiency. One procedure that may be used in this context is described in [56].

(2) For a complex industrial system like a container terminal, there is significant uncertainty in the outcome of a post-event recovery action. If a recovery action is implemented yet the outcome is not as expected, a second action may be warranted. This motivates further development of digital twinning functions to enable realtime recovery action implementation with feedback and adjustment.

(3) Brantley et al. [7,8] showed that when the underlying decision space can be approximated with a metamodel, such as a quadratic regression model Barton [5], the computational efficiency of OCBA can be significantly enhanced. Given the complexity of port operations, a polynomial metamodel may no longer provide adequate fit and more flexible metamodels, such as stochastic kriging, may be required Chen and Zhou [15]; Shen et al. [51]. However, the optimal allocation of the simulation budget is only understood for embedded metamodels with linear or quadratic form. Beyond these, optimal allocation is an open question. Further development of digital-twin enabled DSS may also stim ulate and benefit from research on OCBA with more flexible metamodels.

## Declarations of interest

No potential conflict of interest was reported by the authors.

## Funding

This research was made possible with funding support from Singapore Maritime Institute under grant no. SMI-2018-PE-01, the Air Force Office of Scientific Research under grant no. FA9550-19-1-0383, National Science Foundation under grant no. DMS-1923145, and the National Natural Science Foundation of China under Grant 71720107003 and 61603321

## Appendix A. Randomness in digital twin model

Randomness in digital twin model.

<table><tr><td>Module</td><td>Randomness</td></tr><tr><td>Vessel generatorExternal truck generatorQuay area</td><td>Three types of vessels have different parameters on length (uniform), workload (uniform), and inter-arrival time (exponential).Inter-arrival time follows exponential distribution.The number of QCs assigned to each vessel is based on the vessel length and workload using a lookup table.The QC single or twin lift is proportionally generated.Vehicle holding buffer has a finite capacity and queuing may occur.Distance between stowage and AGV, aiming time, and acceleration, deceleration, and max speed of gantry, hoist and trolley are used to compute an average loading/unloading time, which is then used to parameterize a gamma distribution model from which random loading/unloading times are drawn.</td></tr><tr><td>Quay craneYard area</td><td>The access points per yard block have finite capacity and queuing may occur.Container allocation follows the 80–20 rule, and the allocation is uniformly distributed in each range.Distance between stacking position and AGV, acceleration, deceleration, and max speed of hoist and trolley are used to compute an average loading/unloading time used to parameterize a gamma distribution model from which random loading/unloading times are drawn.</td></tr><tr><td>Yard craneTraffic network</td><td>ehicle congestion is simulated following Zhou et al. [67].A pool of vehicles is assigned to serve a specific vessel using a lookup table.The number of vehicles in the pool is dynamically determined based on vessel workload.</td></tr></table>

## Appendix B. Comparison between stochastic and deterministic solutions

Table B.5  
BoA rates estimated by stochastic and deterministic digital twin models.

<table><tr><td rowspan="2">ID</td><td colspan="2">Scenario 1</td><td colspan="2">Scenario 2</td><td colspan="2">Scenario 3</td></tr><tr><td>S-DT</td><td>D-DT</td><td>S-DT</td><td>D-DT</td><td>S-DT</td><td>D-DT</td></tr><tr><td>1</td><td>13.63</td><td>1.86</td><td>6.82</td><td>0.05</td><td>2.95</td><td>0</td></tr><tr><td>2</td><td>13.91</td><td>6.41</td><td>8.85</td><td>1.22</td><td>3.88</td><td>0.22</td></tr><tr><td>3</td><td>15.20</td><td>11.28</td><td>11.24</td><td>7.19</td><td>6.60</td><td>3.59</td></tr><tr><td>4</td><td>20.50</td><td>18.24</td><td>16.08</td><td>15.84</td><td>13.13</td><td>20.18</td></tr><tr><td>5</td><td>31.93</td><td>39.78</td><td>27.35</td><td>37.63</td><td>28.92</td><td>52.03</td></tr><tr><td>6</td><td>47.12</td><td>63.87</td><td>45.44</td><td>63.60</td><td>43.39#</td><td>68.36#</td></tr><tr><td>7</td><td>65.28</td><td>84.25</td><td>60.92#</td><td>81.38#</td><td>52.59</td><td>72.35**</td></tr><tr><td>8</td><td>79.39#</td><td>92.45#</td><td>71.57</td><td>87.65</td><td>55.45*</td><td>64.28</td></tr><tr><td>9</td><td>87.39</td><td>95.79**</td><td>76.66*</td><td>87.96**</td><td>52.01</td><td>57.38</td></tr><tr><td>10</td><td>91.26</td><td>95.42</td><td>76.56</td><td>83.76</td><td>46.78</td><td>52.89</td></tr><tr><td>11</td><td>91.90*</td><td>93.97</td><td>71.77</td><td>75.24</td><td>38.52</td><td>41.16</td></tr><tr><td>12</td><td>90.01</td><td>91.83</td><td>63.85</td><td>64.72</td><td>30.71</td><td>30.49</td></tr><tr><td>13</td><td>85.82</td><td>89.59</td><td>54.03</td><td>57.07</td><td></td><td></td></tr><tr><td>14</td><td>79.36</td><td>84.43</td><td>46.87</td><td>52.71</td><td></td><td></td></tr><tr><td>15</td><td>71.76</td><td>75.45</td><td></td><td></td><td></td><td></td></tr><tr><td>16</td><td>63.90</td><td>64.77</td><td></td><td></td><td></td><td></td></tr></table>

Note:  
(1) S-DT and D-DT denote solution obtained by stochastic and deterministic digital twin, respectively.  
(2) Default actions are indicated with #.  
(3) Best recovery actions according to S-DT are indicated with \*.  
(4) Best recovery actions according to D-DT are indicated with $^ { \ast \ast } .$

## References

[1] N. Al-Dhaheri, A. Jebali, A. Diabat, A simulation-based genetic algorithm approach for the quay crane scheduling under uncertainty, Simul. Model. Pract. Theory 66 (2016)122–138.

[2] H. Alyami, P.T.-W. Lee, Z. Yang, R. Riahi, S. Bonsall, J. Wang, An advanced risk analysis approach for container port safety evaluation, Marit. Policy Manag, 41 (7 (2014) 634–650.

[3] S. Andradottir, ´ Simulation optimization, in: Handbook of Simulation: Principles, Methodology. Advances. Applications, and Practice. 1998, pp. 307–333

[4] A. Asadabadi. E. Miller-Hooks, Maritime port network resiliency and reliability through co-opetition, Transp. Res. Part E: Logist. Transp. Rey, 137 (2020) 101916.

[5] R.R. Barton, Simulation optimization using metamodels, in: Proceedings of the 2009 Winter Simulation Conference (WSC). IEEE, 2009, pp. 230–238

[6] R.R. Barton, B.L. Nelson, W. Xie, Quantifying input uncertainty via simulation confidence intervals, INFORMS J. Comput. 26 (1) (2014) 74–87.

[7] M.W. Brantley. LH. Lee. C.-H. Chen, A. Chen, Efficient simulation budget allocation with regression, IIE Trans. 45 (3) (2013) 291–308

[8] M.W. Brantley, L.H. Lee, C.-H. Chen, J. Xu, An efficient simulation budget allocation method incorporating regression for partitioned domains, Automatica 50 (5) (2014) 1391–1400

[9] A. Bruzzone, M. Massei, F. Madeo, E. Tarone, Modeling environmental impact and efficiency in maritime logistics, in: Proceedings of the 2010 Summer Computer Simulation Conference, Society for Computer Simulation International, 2010, pp. 433–438.

[10] X. Cao, S. Wang, C. Zhou, N. Wu, Offshore platform for containerized cargo redistribution: a new concept and simulation-based performance study, in Maritime Policy & Management. 2020, pp. 1–21.

[11] D. Chang, Z. Jiang, W. Yan, J. He, Integrating berth allocation and quay crane assignments, Transp. Res. Part E: Logist. Transp. Rev, 46 (6) (2010) 975–990.

[12] C.-H. Chen, L.H. Lee, Stochastic Simulation Optimization: An Optimal Computing Budget Allocation 1, World scientific, 2011.

[13] C.-H. Chen, J. Lin, E. Yücesan, S.E. Chick, Simulation budget allocation for further enhancing the efficiency of ordinal optimization, Discrete Event Dynam. Syst. 10 (2000) 251–270.

[14] L. Chen, E. Miller-Hooks, Resilience: an indicator of recovery capability in intermodal freight transport, Transp. Sci. 46 (1) (2012) 109–123.

[15] X. Chen, Q. Zhou, Sequential experimental designs for stochastic kriging, in: Proceedings of the Winter Simulation Conference 2014, IEEE, 2014, pp. 3821–3832.

[16] A. Coraddu, L. Oneto, F. Baldi, F. Cipollini, M. Atlar, S. Savio, Data-driven ship digital twin for estimating the speed loss caused by the marine fouling. Ocean Eng 186 (2019) 106063.

[17] P. de Langen, M. Nidjam, M. van der Horst, New indicators to measure port performance, J. Mar. Res. 4 (1) (2007) 23–36.

[18] N.A.D. Do, I.E. Nielsen, G. Chen, P. Nielsen, A simulation-based genetic algorithm approach for reducing emissions from import container pick-up operation at container terminal, Ann, Oper, Res, 242 (2) (2016) 285–301.

[19] J.-X. Dong, D.-P. Song, Container fleet sizing and empty repositioning in liner shipping systems, Transp. Res. Part E: Logist. Transp. Rev. 45 (6) (2009) 860–877.

[20] J.-X. Dong, D.-P. Song, Quantifying the impact of inland transport times on container fleet sizing in liner shipping services with uncertainties, OR Spectr. 34 (1) (2012) 155–180.

[21] K. Fagerholt, A computer-based decision support system for vessel fleet scheduling—experience and future research, Decis. Support. Syst. 37 (1) (2004) 35–47.

[22] M.P. Fanti, G. Iacobellis, W. Ukovich, V. Boschian, G. Georgoulas, C. Stylios, A simulation based decision support system for logistics management, J. Comput. Sci. 10 (2015) 86–96.

[23] S. Fazi, A decision-support framework for the stowage of maritime containers in inland shipping, Transp. Res. Part E: Logist. Transp. Rev. 131 (2019) 1–23.

[24] S. Fazi, J.C. Fransoo, T. Van Woensel, A decision support system tool for the transportation by barge of import containers: a case study, Decis. Support. Syst. 79 (2015) 33–45.

[25] A. Francisco, N. Mohammadi, J.E. Taylor, Smart city digital twin–enabled energy management: toward real-time urban building energy benchmarking, J. Manag. Eng. 36 (2) (2020), 04019045.

[26] M.C. Fu, et al., Handbook of Simulation Optimization 216, Springer, 2015.

[27] L.M. Gambardella, M. Mastrolilli, A.E. Rizzoli, M. Zaffalon, An optimization methodology for intermodal terminal management, J. Intell. Manuf. 12 (5–6) (2001) 521–534.

[28] E. Glaessgen, D. Stargel, The digital twin paradigm for future nasa and us air force vehicles, in: 53rd AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics and Materials Conference 20th AIAA/ASME/AHS Adaptive Structures Conference 14th AIAA, 2012, p. 1818.

[29] J. He, Y. Huang, D. Chang, Simulation-based heuristic method for container supply chain network optimization, Adv. Eng. Inform. 29 (3) (2015) 339–354.

[30] J. He, Y. Huang, W. Yan, Yard crane scheduling in a container terminal for the trade-off between efficiency and energy consumption, Adv. Eng. Inform. 29 (1) (2015) 59–75.

[31] R.W.C. Hughes, Virtual simulation model of the new boeing Sheffield facility, in: Simulation for Industry 4.0, Springer, 2019, pp. 211–218.

[32] E. Irannezhad, C.G. Prato, M. Hickman, An intelligent decision support system prototype for hinterland port logistics, Decis. Support. Syst. 130 (2020) 113227.

[33] S.S. Johansen, A.R. Nejad, On digital twin condition monitoring approach for drivetrains in marine applications, in: ASME 2019 38th International Conference on Ocean. Offshore and Arctic Engineering. American Society of Mechanical Engineers Digital Collection. 2019.

[34] H. Lee, N. Avdin, Y. Choi, S. Lekhavat, Z. Irani, A decision support system for vessel speed decision in maritime logistics using weather archive big data, Comput. Oper. Res, 98 (2018) 330–342.

[35] P. Legato, R.M. Mazza, A decision support system for integrated container handling in a transshipment hub. Decis. Support, Syst. 108 (2018) 45–56.

[36] P. Legato, R.M. Mazza, D. Gullì, Integrating tactical and operational berth allocation decisions via simulation–optimization, Comput. Ind. Eng. 78 (2014) 84–94.

[37] P. Legato. R.M. Mazza. R. Trunfio. Simulation-based optimization for discharge/ loading operations at a maritime container terminal, OR Spectr. 32 (3) (2010) 543-567.

[38] H. Li, C. Zhou, B.K. Lee, L.H. Lee, E.P. Chew, A hierarchical modeling paradigm for multi-fidelity simulation of mega container terminals, in: System Integration (SII), 2017 IEEE/SICE International Symposium on. IEEE, 2017, pp. 247–252.

[39] H. Li, C. Zhou, B.K. Lee, L.H. Lee, E.P. Chew, R.S.M. Goh, Capacity planning for mega container terminals with multi-objective and multi-fidelity simulation optimization, IISE Trans. 49 (9) (2017) 849–862.

[40] W. Li, Z. Xiaoning, X. Zhengyu, Efficient container stacking approach to improve handling: efficiency in chinese rail-truck transshipment terminals. SIMULATION 96 (2019) 3–15

[41] S. Maldonado, R.G. Gonz´alez-Ramírez, F. Quijada, A. Ramírez-Nafarrate, Analytics meets port logistics: a decision support system for container stacking operations, Decis, Support, Syst, 121 (2019) 84–93.

[42] S.A. Mansouri, H. Lee, O. Aluko, Multi-objective decision support to enhance environmental sustainability in maritime shipping: a review and future directions, Transp. Res. Part E: Logist. Transp. Rev. 78 (2015) 3–18.

[43] P.B. Marlow, A.C.P. Casaca, Measuring lean ports performance, Int. J. Transp. Manag, 1 (4) (2003) 189–202.

[44] E. Miller-Hooks, X. Zhang, R. Faturechi, Measuring and maximizing resilience of freight transportation networks, Comput, Oper, Res, 39 (7) (2012) 1633–1643

[45] K. Nagaraj, J. Xu, R. Pasupathy, S. Ghosh, Efficient estimation in the tails of gaussian copulas, arXiv preprint (2016) arXiv:1607.01375.

[46] R. Nair, H. Avetisyan, E. Miller-Hooks, Resilience framework for ports and other intermodal components, Transp, Res, Rec, 2166 (1) (2010) 54–65.

[47] R. Pant. K. Barker, J.E. Ramirez-Marquez, C.M. Rocco. Stochastic measures of resilience and their application to container terminals, Comput. Ind. Eng. 70 (2014).183-194

[48] S. Pratap, A. Nayak, A. Kumar, N. Cheikhrouhou, M.K. Tiwari, An integrated decision support system for berth and ship unloader allocation in bulk material handling port, Comput, Ind. Eng, 106 (2017) 386–399.

[49] D. Roy, R. De Koster, R. Bekker, Modeling and design of container terminal operations, Oper. Res. 68 (2020) 686–715.

[50] A. Shafieezadeh, L.I. Burden, Scenario-based resilience assessment framework for critical infrastructure systems: case study for seismic resilience of seaports, Reliab. Eng. Syst. Saf. 132 (2014) 207–219.

[51] H. Shen, L.J. Hong, X. Zhang, Enhancing stochastic kriging for queueing simulation with stylized models, IISE Trans. 50 (11) (2018) 943–958.

[52] W.K. Talley, Performance indicators and port performance evaluation, Logist. Transp, Rey, 30 (4) (1994) 339.

[53] F. Tao, F. Sui, A. Liu, Q. Qi, M. Zhang, B. Song, Z. Guo, S.C.-Y. Lu, A. Nee, Digital twin-driven product design framework, Int. J. Prod. Res. 57 (12) (2019) 3935–3953.

[54] E. Ursavas, A decision support system for quayside operations in a container terminal, Decis. Support. Syst. 59 (2014) 312–324.

[55] E. Ursavas, Priority control of berth allocation problem in container terminals, Ann. Oper. Res. (2015) 1–20.

[56] T. Wang, J. Xu, J.-Q. Hu, A study on efficient computing budget allocation for a two-stage problem, Asia-Pacific J. Operat. Res. (2020), https://doi.org/10.1142/ S021759592050044X.

[57] W. Wang, Y. Jiang, Y. Peng, Y. Zhou, Q. Tian, A simheuristic method for the reversible lanes allocation and scheduling problem at smart container termina gate, J. Adv. Transp. (2018) 2018.

[58] E.Y. Wong, A.H. Tai, H.Y. Lau, M. Raman, An utility-based decision suppor sustainability model in slow steaming maritime operations, Transp. Res. Part E: Logist. Transp. Rev. 78 (2015) 57–69.

[59] X. Xing, P.R. Drake, D. Song, Y. Zhou, Tank container operators’ profit maximization through dynamic operations planning integrated with the quotationbooking process under multiple uncertainties, Eur. J. Oper. Res. 274 (3) (2019) 924–946.

[60] J. Xu, E. Huang, L. Hsieh, L.H. Lee, Q.-S. Jia, C.-H. Chen, Simulation optimization in the era of industrial 4.0 and the industrial internet, J. Simulat. 10 (4) (2016) 310–320.

[61] H. Yu, Y.-E. Ge, J. Chen, L. Luo, D. Liu, C. Tan, Incorporating container location dispersion into evaluating gcr performance at a transhipment terminal, Marit. Policy Manag. 45 (6) (2018) 770–786.

[62] Y. Yue, J. Chun, H. Lin, Optimal planning on gate system on container terminals based on simulation optimization method and case study. in: 2006 Internationa Conference on Management Science and Engineering. IEEE, 2006, pp. 342–347.

[63] Q. Zeng, A. Diabat, Q. Zhang, A simulation optimization approach for solving the dual-cycling problem in container terminals, Marit. Policy Manag. 42 (8) (2015) 806–826.

[64] C. Zhou, E.P. Chew. LH. Lee. D. Liu. An introduction and performance evaluation of the grid system for transshipment terminals, Simulation 92 (3) (2016) 277–293.

[65] C. Zhou. L.H. Lee. E.P. Chew. H. Li. A modularized simulation for traffic network in container terminals via network of servers with dynamic rates in: Proceedings of the 2017 Winter Simulation Conference, IEEE Press, 2017, p. 257

[66] C. Zhou, H. Li, B.K. Lee, Z. Qiu, A simulation-based vessel-truck coordination strategy for lighterage terminals, Transp. Res. Part C: Emerg. Technol. 95 (2018) 149–164.

[67] C. Zhou, H. Li, W. Liu, A. Stephen, L.H. Lee, E.P. Chew, Challenges and opportunities in integration of simulation and optimization in maritime logistics, in: 2018 Winter Simulation Conference (WSC), IEEE, 2018, pp. 2897–2908.

Chenhao Zhou, is a Research Assistant Professor of Department of Industrial Systems Engineering and Management in National University of Singapore. His research interests are transportation systems and maritime logistics using simulation and optimization methods. Email: zhou\_chenhao@u.nus.edu

Jie Xu (corresponding author), is currently an Associate Professor in the Department of Systems Engineering and Operations Research at George Mason University. His research interests are data analytics, simulation modeling, and stochastic optimization methods. Email: jxu13@gmu.edu

Elise Miller-Hooks, Professor, holds the Bill & Eleanor Hazel Endowed Chair in Infra structure Engineering in the Sid & Reva Department of Civil, Environmental, & Infra structure Engineering at George Mason University. Her expertise is in disaster planning and response, multi-hazard civil infrastructure resilience quantification, stochastic and dynamic network algorithms, intermodal passenger and freight transport, real-time routing and fleet management, paratransit and ridesharing, and collaborative and multi obiective decision-making. Email: miller@gmu.edu.

Weiwen Zhou, is currently a PhD student in Sid & Reva Department of Civil, Environ mental, & Infrastructure Engineering at George Mason University. His research interest is transportation system management under disruption. Email: wzhou5@gmu.edu

Chun-Hung Chen is a Professor of Systems Engineering and Operations Research at George Mason University. His research interests cover a wide range of areas including discrete-event systems modeling and simulation, stochastic simulation optimization, rareevent simulation, and decision making under uncertainty. His email address is cchen 9@gmu.edu.

Loo Hay Lee is currently an Associate Professor of Department of Industrial Systems Engineering and Management in National University of Singapore. His research interests are simulation-based optimization, maritime logistics and supply chain and digital Twin. Email: iseleelh@nus.edu.sg.

Ek Peng Chew is currently an Associate Professor of Department of Industrial Systems Engineering and Management in National University of Singapore. His research interests are in maritime logistics and supply chain and simulation optimization. Email: isecep@n us.edu.sg.

Haobin Li is currently Senior Lecturer at the Department of Industrial Systems Engi neering and Management in National University of Singapore. His research interests include simulation modeling, simulation based optimization, and their application in maritime and logistics sectors. Email: li\_haobin@nus.edu.sg.
