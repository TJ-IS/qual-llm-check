---
otero_id: 9312
otero_key: "57RGABKE"
title: "A decision support framework for home health care transportation with simultaneous multi-vehicle routing and staff scheduling synchronization"
authors: "Jamal Abdul Nasir; Yong-Hong Kuo"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113361"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support framework for home health care transportation with simultaneous multi-vehicle routing and staf scheduling synchronization

![](/api/attachments/57RGABKE/fulltext/images/bed61fa9d5425cbba9dc5659054e8a3bf892af105064853b20cc8213a083b504.jpg)

Jamal Abdul Nasir, Yong-Hong Kuo

Despartment of Industrial and Manufacturing Systems Engineering, The University of Hong Kong, Hong Kong

## A R T I C L E I N F O

Keywords: Shared healthcare mobility Home health care Decision support system Hybrid genetic algorithm Synchronization Vehicle routing

## A B S T R A C T

Due to the ageing population and the prevalence of chronic diseases, Home Health Care (HHC) practices are significantly increasing in developed countries to provide coordinated health related services to patients at their homes. Accordingly, the scope of HHC services is also expanding from typical nursing and postoperative care at home to cover all types of needs of elderly patients (e.g., personal care, drug delivery and meal services). This paper aims to address the pressing demand for HHC services and develop a novel and efective mathematical model and solution methodology for supporting health care service delivery decisions. Our decision support framework captures the real needs of HHC services, including the challenges of creating simultaneous schedules and route plans for a set of HHC staf and Home Delivery Vehicles (HDVs) under the requirements of synchronization between HHC staf and HDVs visits, multiple visits to patients, multiple routes of HDVs and pickup/ delivery visits related precedence for HDVs. A Mixed Integer Linear Programming (MILP) model is developed to characterize the optimization problem. Considering the computational complexity of the problem, a Hybrid Genetic Algorithm (HGA) is proposed to suggest HHC planning decisions. The model formulation and proposed HGA are examined on real-life instances for demonstrating its practicality and randomly generated test instances for assessing the scalability of the proposed approach. The results show the efectiveness and eficiency of our solution methodology. Experimental results indicate that the proposed algorithm provided a good performance even with an increasing number of required synchronized services, whereas the heuristic tactics facilitate the HGA to produce better-quality solutions in a significantly shorter time. Our framework is expected to contribute to an important aspect of shared healthcare mobility.

## 1. Introduction

The Home Health Care (HHC) service sector is among the fastgrowing areas in medical services. The elderly population, disabled citizens and other specific segments of the society who are unable or unwilling to use the conventional health care facilities are very well suited for HHC services. Furthermore, HHC services are particularly important nowadays during pandemic outbreaks as citizens may not be able to travel to access healthcare facilities [1]. In HHC services, health care professionals and nursing staf visit the patients at their homes and provide essential services such as medical tests, wound care, administration of medicine dosage, therapy services, and typical domestic help services. The prominent factors behind the surge in HHC demand are the ageing population, outspread of chronic diseases, diminishing scope of family care due to extended working hours, and increasing push from governments to improve the quality of life and health care services. The World Health Organization (WHO) report mentions that this fast pace of population ageing will cause a sharp increase in the number of elderly citizens in many low and middle income countries, resultantly some of them will be observing a doubling in the total number of care dependent population by 2050 [2].

HHC patients are served with practical considerations, such as ser vice time window, required services, service providers' qualifications, and other related constraints. Besides the requirement of typical HHC services, most of the HHC patients also need home delivery of medi cines, pickup service for blood samples, delivery of test reports, and home meal delivery service. These home delivery services can provide a smooth care experience and reduce the unwanted movements of elderly or critically sick patients. HHC companies and organizations perform diferent logistic activities every day, comprising the delivery of medicines or medical devices from a drugstore to patients, and carrying the biological samples from patients' residence to the laboratory [3]. Much of the research focuses on either HHC worker assignment, scheduling and route planning [4–8] or HHC delivery problems in the context of drug deliveries and the provision of communal services [9–12]. Though some studies have considered the combined availability of HHC and home delivery services while planning routes for drug delivery vehicles, they assumed homogeneous vehicles and assigned HHC nurses to drive/ accompany the vehicles to deliver drugs and perform HHC related services [13]. Despite the fact that such an approach simplifies the combination of both types of these services, except some special cases this approach may not be feasible in real settings due to the following reasons: (i) requirement of heterogeneous vehicles and multiple visits to provide a variety of home delivery services to each patient (e.g., drug delivery, meal delivery, and collection of biological samples); (ii) HHC services (e.g., personal care, rehabilitation services and postoperative treatment services) require longer care sessions to perform the task, hence the vehicle idle time and parking cost can become unbearable; (iii) HHC nurses and domestic helpers are skilled for their respective specialized duties, thus it may be dificult for them to drive the home delivery vehicles (HDVs); (iv) similarly, drivers of HDVs may not be able to execute the specialized HHC related services. Whereas, considering the dificulty of elderly and palliative care patients, the presence of HHC staf is necessary at the time of home delivery visits fo handling the material and information resources for the assigned patient. Therefore, it will be more appropriate to investigate the coordinated and synchronized visits while developing simultaneous separate routes for these two types of services. To the best of our knowledge, no efort has taken place to integrate and synchronize these two related services for HHC patients in the existing HHC literature. Health care costs are one of the most serious concerns in terms of economic complications in this era [14]. New methods are needed to assist the integration of patient preferences in creating visits for health care staf or the synchronization of human and material resources in interrelated health and communal services to be ofered in a region [15].

In this paper, we introduce a special structure for the HHC problem, which develops scheduling and routing plans for both HHC staf and HDVs simultaneously. The synchronization among the visits associated with the HHC routes and HDVs routes, service dependent HDVs visits to enforce the precedence among pickup (supply) and delivery (demand) points and multi routes based HDVs schedules are the key characteristics of this work. We assume that four diferent types of HHC services are being ofered (personal care, rehabilitation services, postoperative care and domestic help services) and each nurse is skilled for more than one HHC service but it is not mandatory to be skilled for all the services. Whereas, three diferent home delivery services are available, namely drug delivery, blood sample collection and meal delivery service. Each vehicle is dedicated to provide a single specific type of service. Each patient requires only one HHC service and it can be provided by a single HHC nurse. However, patients can get multiple home delivery services. Thus a patient can receive a single HHC nurse visit and more than one home delivery vehicle visits. Consequently, the maximum number of available service visits are equal to four (1HHC visit+3HDVs visits) for each patient. The restrictions related to patient time windows, route length and maximum working hours are also considered in this pro. blem. HHC nurses visit the patients following the given time windows. From the perspective of synchronization, the HDVs must reach the patient location after the arrival of the HHC nurse and before the ending of the HHC service to ensure the pickup/delivery of items in the presence of the health care staf. Furthermore, drug delivery vehicles must visit the pharmacy before visiting the first patient in their route. while biological samples collection vehicles must visit the hospital after visiting the last patient in their route and before reaching the depot. We assume that meal delivery items are available for vehicles at the depot. Fig. 1 shows the structure of the synchronized HHC and home delivery problem.

The main contributions of this study to the existing HHC literature are as follows: (1) The HHC routing and scheduling problem (HHCRSP) introduced in this article is unique as, to the best of our knowledge, it is the first model that envisions HHC services and HDV services as two separate types of services. The two diferent types of services are performed by the diferent staf because of operational/capability constraints. Consequently, our MILP model suggests two distinct sets of routes simultaneously (one for each type of service) and develops scheduling plans for nurses and HDVs considering synchronization requirements; (2) while the total number of nurses and HDV routes are important in minimizing total service costs, they are not included in the objective function of other models. Our HHCRSP model not only includes them in the objective function, but also introduces multi-trip route constraints (13–17) for HDVs. To our knowledge, the multi-trip route constraints are not studied in the existing HHCRSP literature. Additionally, we include unique constraints in our model to synchro nize the HDV schedules with the HHC schedules in such manner that hard time windows for HDV services depend on the schedule of HHC nurse. This enables simultaneous services to take place at each patient node; (3) Our mathematical formulation address practical challenges raised by heterogeneous vehicles, multi HDVs visits at each patient location, multiple routes based planning for HDVs and pickup-delivery visits related precedence. We argue that our HHC structure better re flects real-life situations and satisfy patients' actual needs; (4) We propose a hybrid genetic algorithm (HGA) to solve large-sized problem instances. The algorithm utilizes the synchronization characteristics of the problem to establish an innovative problem-specific solution representation. Moreover, the crossover operators and two heuristic methods (solution feasibility reform heuristic (SFRH) and visits reassignment heuristic (VRH)) utilize the structure of the HHC problem and synchronization characteristics to increase the solution eficiency and quality. We compare the performance of our HGA to existing GA based solutions. We perform extensive sensitivity analysis to demonstrate the efectiveness of the HGA; (5) We demonstrate our modeling approach using a realistic application in Hong Kong.

The remainder of the paper is organized as follows: Section 2 presents the literature review. A description of the problem and the mathematical model are presented in Section 3. Section 4 illustrates the proposed HGA to solve the problem. Computational experiments and results are discussed in Section 5. Finally, conclusion and future research are given in Section 6.

## 2. Literature review

The HHCRSP studied in this article is an extension of the classica vehicle routing problem with time windows (VRPTW) that focuses on HHC and home delivery practices. Scheduling and routing problems are well covered in the literature related to the travelling salesman problem [16–18] and VRPTW [19–21]. The HHCRSP generalizes VRPTW but the presence of many HHC specific constraints and a variety of goals in the objective function makes it a very complicated optimization problem. The first studies for the HHCRSP are accredited to Begur et al. [22] and Cheng and Rich [6]. Begur et al. [22] proposed a decision support system for the HHCRSP problem. They considered the workload balance for the employees and solved the problem by a construction and improvement heuristic. Cheng and Rich [6] extended the previous HHCRSP problem by including full time and part-time nurses and they modelled the problem as VRPTW. From these two initial studies and related HHC literature, it is quite apparent that HHCRSP covers a variety of characteristics related to HHC services. To the best of our understanding, no standard version of HHCRSP exists thus the HHCRSP models represent the diversity of HHC operations. These models investigate the HHCRSP with respect to diferent constraints, planning horizons, solution methods and objective functions.

The HHCRSP can be categorized as either a single-period or multiperiod considering the planning horizon that can be a single working day or multiple days of a week or a month [23]. Originally, the HHCRSP was solved on a daily planning horizon [24]. Realistic constraints have been included in the HHCSRP as it evolved over time.

![](/api/attachments/57RGABKE/fulltext/images/8d5f97b99d6e84311ca3ce0b6c9c3385737fa81987ff2b98cc4c6f58557b3002.jpg)  
Fig. 1. Synchronization between HHC and home delivery vehicle routes.

Presently, the daily HHCRSP models are formulated by taking into account the workload balance for caregivers [25], interdependent services [4], shared visits [26,27], multiple modes of transportation [28], lunch breaks and overtime [29], home carer visit preferences [30] and patient's preferences [31]. Some researchers also considered the timedependent travel time [32], environmental concerns [33–35], stochastic travel and service times [12,36,37], quantitative thresholds based decision rules [38] and development of decision support tools [29,39] for their daily HHCRSP.

HHCRSP has been extended to cover weekly or monthly planning horizons to account for practical requirements. Multiperiod HHCRSP models focus on short-to mid-term planning while assigning nurses to patients and creating scheduling plans [40–47]. The multi-period planning horizon also allows the model to incorporate patient preferences (e.g., continuity of care) and a balanced workload for the caregivers while creating the schedules over the entire planning hor izon. Many researchers considered continuity of care and/or workload balance for the caregiver assignments [7,48–51] and acceptance of new patients while conserving high continuity for existing patients [52] in the context of HHC. Besides continuity of care, some studies addressed the dynamic nature of patient arrivals [53–56] and stochastic demands [48,57,58]. Some authors also considered strategic-level decisions such as districting based assignment of nurses considering travel load and workload features [59–61] and resource (staf, technical resource) di mensioning [57,62,63].

Many diferent approaches have been proposed to solve HHCRSP. These solution approaches can roughly be divided into two categories 1) exact methods based solution approaches and 2) heuristic or metaheuristic framework based approaches. Exact methods such as branch and-price framework [30,64] and metaheuristic methods like particle swarm optimization [65], Variable Neighborhood Search (VNS) based methods [4,5,26,66], Tabu search [3], genetic algorithm [3,13], variable neighborhood descent [67], and two-phase solution algorithm [68] have been used to solve single-period HHCRSPs. Authors have used exact methods such as branch-price and-cut algorithm [69], integer linear programming [49,50,70], hierarchical solution containing two linear programming models [40], as well as metaheuristic approaches such as greedy randomized adaptive search procedure [41,71], a two stage solution approach combining a constraint programming basedheuristic and an adaptive large neighborhood search [42], a two-phase algorithm with the consideration of two objectives [45] and a set partitioning heuristic [24] to solve multi-period HHCRSPs. More detailed discussion about the HHCRSP models can be found in the recently published surveys [23,72,73] that extensively cover the HHCRSPs.

In practice, the HHC patients and isolated elderly residents not only need HHC services but also require home delivery services for drugs, meals and health test reports. We extend the HHC research literature by including heterogeneous home delivery services along with new HHC features such as multiple services, interdependent services/visits, and synchronization requirements into our HHCRSP model. The HHCRSP studied in this paper is a single period (daily planning horizon) problem and formulated as a Mixed Integer Linear Programming (MILP) model to address the requirements of the HHC services along with the heterogeneous home delivery services simultaneously. Consequently, our HHCRSP model lies in the category of single period HHCRSP literature that addresses the provision of home delivery services and considers temporal dependence and synchronization constraints. Table 1 shows recent literature that deals with the home delivery services for HHC or addresses synchronization requirements.

The home delivery problems from the perspective of HHC include drug delivery at home [3,9,11] and meal delivery [10,74]. These studies focused on the home delivery issues and did not cover the combined HHC and home delivery services in their models as we studied in our problem. Only two research articles [13,34] considered the avail ability of both HHC services and home delivery services but they did not consider the meal delivery service and assumed that the assigned nurse drove the vehicles and perform all the tasks (e.g., delivery of drugs, collection of biological samples, and HHC services). Compared to our work, instead of service-specific heterogeneous vehicles, their models contain homogenous vehicles [13] or general-purpose vehicles [34]. They also did not allow multiple visits and their models only cover one type of routes (single trip vehicle routes) without any interdependent visits and synchronization constraints. The multi-trip vehicle routes are absent in the studies except [10,33] and these two articles also did not formulate the heterogeneous multi-trip route scheduling constraints in their models as we used in this study. On the contrary, our model contains two diferent types of routes, HHC nurse routes (single trips) and HDV routes (multiple trips) and we consider syn chronization among all planned visits for diferent routes at each patient location. Though the single-trip vehicle routes for providing both HHC and home delivery services simplifies the problem, it is only applicable in some specialized situations. In practice, the provision of all services (drug delivery, meal delivery, collection of biological samples and HHC services) through a single establishment is unrealistic, hence we argue that modeling approaches are needed where diferent stakeholders can provide their services using their own existing resources (vehicles, nurses) under coordinated plans and synchronized schedules.

The impact of synchronization and dependent services in the context of HHC services is not widely considered in the literature [4,75–77]. Our model difers from existing models in three important ways. Firstly, we incorporate multi-trip vehicle routes. The HHC services (rehabilitation services, postoperative care and domestic help services) take more time compared to home delivery services $\mathrm { e . g . , }$ , meal delivery and drug delivery. Consequently, home delivery vehicles can complete more trips in a day as compared to a HHC nurse. The inclusion of multi-trip HDV routes in our model not only increases the eficient utilization of resources but also makes the problem more realistic. Secondly, most existing models employ synchronization constraints for a single service where patients need two caregivers to perform a particular task, while our model uses synchronization constraints to synchronize the schedules for services provided by diferent types of routes (HHC routes, HDV routes) and it can synchronize four diferent services at one node (1HHC service $\mathrm { v i s i t } + 3 \mathrm { H D V } s$ service visits). Hence our model enables a situation where simultaneous services take place at each patient node $( \boldsymbol { \mathrm { e . g . } }$ , a HHC nurse with long service duration than HDVs receives drugs form a HDV and administers medicine dosage). In other words, HHC nurses follow the predefined hard time windows and the time interval at which a HHC nurse begins its service at a patient node to the end of service becomes the hard time windows for the HDy services. Thirdly, our HHCRSP model considers the number of HDV routes and HHC nurses in the objective function. This is not necessarily the case in other models.

Table 1  
Characteristics of related HHC/HDVs literature.

<table><tr><td rowspan="2">Article</td><td colspan="5">Objective</td><td colspan="7">Constraints</td><td rowspan="2">HVR</td><td rowspan="2">MTVR</td><td rowspan="2">SHVR</td><td rowspan="2">CS</td></tr><tr><td>TT/D</td><td>TRC</td><td>NN</td><td>NVR</td><td>PR</td><td>TD</td><td>SYN</td><td>NW</td><td>TW</td><td>NQ</td><td>MS</td><td>VRL</td></tr><tr><td>[9]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[11]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>X</td></tr><tr><td>[76]</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[77]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[10]</td><td>X</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>X</td><td>-</td><td>X</td><td>-</td><td>X</td></tr><tr><td>[4]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[30]</td><td>-</td><td>X</td><td>-</td><td>-</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td></tr><tr><td>[3]</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[34]</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>X</td><td>X</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[13]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>[33]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>-</td><td>-</td><td>-</td><td>X</td><td>-</td><td>X</td></tr><tr><td>[75]</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>This study</td><td>-</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

TT/D, Travel time/Distance; TRC, Travel cost; NN, Number of nurses; NVR, Number of vehicle routes; PR, Preferences; TD, Temporal dependence; SYN, Synchronization; NW, Nurse workload regulations; TW, Time windows; NQ, Nurse qualifications; MS, Multiple services; VRL, Vehicle route length; HVR, Heterogeneous vehicle routes; MTVR, Multi-trip vehicle routes per day; SHVR, Separate HHC and HDV routes; $\mathbf { C } S ,$ Case study.

This study includes most of the important features related to HHCRSP and home delivery services as summarized in Table 1. The HGA developed to address the computational complexity in this study is diferent from other Genetic Algorithm (GA) based methods proposed to solve HHCRSP [3,13] in many diferent ways: (1) the use of patients to visits dependency matrix to encode the synchronized visits is novel as it establishes links between visits and has a central role in creating synchronized schedules; (2) the crossover operators exploit the problem characteristics and deploy synchronized visits-based horizontal swap strategy that is problem-specific and absent in general GA implementations; (3) two heuristic methods, SFRH and VRH, are employed in HGA. SFRH operates at two levels to find feasible assignments for infeasible solutions and visits reassignment heuristic attempts to balance the total assignments for each route. These heuristics are designed considering special characteristics of our problem and they prove their efectiveness for HGA in Section 5.7.

## 3. Problem description and mathematical model

Let $G = ( N o , A )$ be a directed graph, where No and A are the sets of all nodes and arcs used in the model, respectively. The sets of patients, nurses, and HDVs are denoted by $P , N ,$ and $V ,$ respectively. The origin node and the destination node are denoted by O and D respectively for every route. A hospital node H and a pharmacy node Q are considered in this work. Thus, the collection of node $N _ { o } = P \cup \{ O , D , H , Q \}$ . In our motivating example, HDVs travel from the origin node, visit the patients, and finally return to the destination node at the end of the route; within the route, they may visit the hospital or the pharmacy, depending on the type of service to deliver. There are travel time and distance associated with each arc $( j , k ) \in A ,$ , denoted by $t _ { j k }$ and $d _ { j k }$ respectively. A setup time is needed whenever vehicle $\nu \in V$ starts a new route.

Let S be the set of HHC services being ofered by the nurses and $p _ { i s }$ indicate if nurse i is competent for service $s \in S$ (1 if competent; 0 otherwise). Similarly, let VS represent the set of HDVs services and $V _ { P g \nu }$ indicates if home delivery service $g \in V S$ is provided by vehicle $\nu \in V ( 1$ if provided; 0 otherwise). In the application which motivates our work, there are three types of services – biological sample collection, drug delivery and meal delivery – which are respectively represented by the numeric values of $g = 1 .$ , 2 and 3. Each patient $j \in P$ may request HHC service $s \in S$ to be ofered by a nurse $( q _ { j s } = 1$ if needed; 0 otherwise) and home delivery service $g \in V S$ to be delivered by a vehicle $( V q _ { g j } = 1$ if needed; 0 otherwise). If any service is requested by patient $j \in P ,$ the nurse must visit within the time window $[ p e _ { j } , p f _ { j } ]$ . The time for a nurse to perform service type s ∈ S is T and the dwell time for vehicle $\nu \in V$ at a patient location is $s d _ { \nu }$ . To ensure that the nurses and vehicles will not be overloaded, maximum total service time and route length are set to L and RL respectively. R and $r g _ { \nu }$ represent the set of HDVs routes and setup time to start a new route for vehicle $\nu \in V$ respectively. M is a suficiently large number. Our model considers three types of costs: travelling cost, fixed cost of a vehicle, and fixed cost of a nurse. Their unit costs are represented by C, F, and B, respectively.

This MILP formulation requires both integer and continuous decision variables for assignment and scheduling purposes respectively. $y _ { i j k } = 1$ , if nurse i ∈ N moves along arc $( j , k ) \in A ; ($ 0 otherwise. $x _ { r \nu j k } = 1$ , if vehicle $\nu \in V$ takes route $r \in R$ and moves along arc $( j , k ) \in A ; 0$ otherwise. $u _ { r \nu } ~ = ~ 1$ , if route $r \in R$ is assigned to vehicle $\nu \in V ; 0$ otherwise. $z _ { i } = 1$ , if HHC nurse i ∈ N has been assigned to a patient; 0 otherwise. $s t _ { r \nu j }$ determines the arrival time of vehicle $\nu \in V$ at node $j \in N o$ for route $r \in R$ and $s _ { i j }$ denotes start time of nurse $i \in N$ at node $j \in P . \ S R _ { r \nu }$ and $E R _ { r { \nu } }$ determine the start time and end time respectively for route $r \in R$ with vehicle $\nu \in V .$

## 3.1. Mathematical model

Our mathematical model is as follows:

$$
\begin{array}{l} \min \underbrace {C \left(\sum_ {r \in R} \sum_ {v \in V} \sum_ {(j , k) \in A} d _ {j k} x _ {r v j k} + \sum_ {i \in N} \sum_ {(j , k) \in A} d _ {j k} y _ {i j k}\right)} _ {\text {Route Travel Cost (RTC)}} \\ + \underbrace {F \sum_ {r \in R} \sum_ {v \in V} u _ {r v} + B \sum_ {i \in N} z _ {i}} _ {\text {Route Assignment Cost (RAC)}} \end{array}\tag{1}
$$

Subject to

HHC nurses' and HDV routes' construction and assignment:

$$
\sum_ {i \in N} \sum_ {(j, k) \in A} y _ {i j k} = 1 \quad \forall j \in P\tag{2}
$$

$$
\sum_ {r \in R} \sum_ {v \in V} \sum_ {(j, k) \in A} x _ {r v j k} V p _ {g v} = V q _ {g j} \quad \forall j \in P, g \in V S\tag{3}
$$

$$
\sum_ {(O, k) \in A} (x _ {r v O k} + y _ {i O k}) = \sum_ {(j, D) \in A} (x _ {r v j D} + y _ {i j D})
$$

$$
= u _ {r v} + z _ {i} \quad \forall v \in V, r \in R, i \in N\tag{4}
$$

$$
\sum_ {(j, h) \in A} y _ {i j h} - \sum_ {(h, k) \in A} y _ {i h k} = 0 \quad \forall h \in P, \quad \forall i \in N\tag{5}
$$

$$
\sum_ {(j, h) \in A} x _ {r v j h} - \sum_ {(h, k) \in A} x _ {r v h k} = 0 \quad \forall   h \in N _ {o} \backslash (O \cup D), \quad \forall   v \in V, \quad \forall   r \in R\tag{6}
$$

Synchronization of HHC nurses' and HDVs' schedules:

$$
s _ {i j} + \left(T _ {s} q _ {j s} + t _ {j k}\right) y _ {i j k} \leq s _ {i k} + M \left(1 - y _ {i j k}\right) \quad \forall i \in N, \quad \forall (j, k) \in A,
$$

$$
\forall s \in S\tag{7}
$$

$$
s t _ {r v j} + (s d _ {v} + t _ {j k}) x _ {r v j k} \leq s t _ {r v k} + M (1 - x _ {r v j k}) \quad \forall (j, k) \in A,
$$

$$
\forall v \in V, \quad \forall r \in R\tag{8}
$$

$$
s t _ {r v j} + M \left(1 - x _ {r v j k}\right) \geq s _ {i j} \quad \forall (j, k) \in A, \quad \forall i \in N, \quad \forall v \in V, \quad \forall r \in R\tag{9}
$$

$$
s t _ {r v j} \leq \sum_ {i \in N} s _ {i j} + \sum_ {s \in S} T _ {s} q _ {j s} \quad \forall j \in P, \quad \forall v \in V, \quad \forall r \in R\tag{10}
$$

$$
s t _ {r v j} \leq M \sum_ {(j, k) \in A} x _ {r v j k} \quad \forall j \in P, \quad \forall v \in V, \quad \forall r \in R\tag{11}
$$

Assignment of HDVs to routes:

$$
\sum_ {v \in V} u _ {r v} \leq 1 \quad \forall r \in R\tag{12}
$$

Start and end times of routes:

$$
- M (1 - x _ {r v O j}) + S R _ {r v} \leq s t _ {r v j} - t _ {O j} x _ {r v O j} \leq M (1 - x _ {r v O j}) + S R _ {r v} \quad \forall
$$

$$
j \in N o, \quad \forall v \in V, \quad \forall r \in R\tag{13}
$$

$$
S R _ {r v} \leq M \quad u _ {r v} \quad \forall v \in V, \quad \forall r \in R\tag{14}
$$

$$
s t _ {r v j} \leq E R _ {r v} - (s d _ {v} + t _ {j _ {D}}) x _ {r v j D} \leq s t _ {r v j} + M (1 - x _ {r v j D}) \quad \forall j \in N o,
$$

$$
\forall v \in V, \quad \forall r \in R\tag{15}
$$

$$
E R _ {r v} + u _ {r v} r g _ {v} \leq M (1 - u _ {r ^ {\prime} v}) + S R _ {r ^ {\prime} v} \quad \forall v \in V, \quad \forall r <   r ^ {\prime} \in R\tag{16}
$$

$$
E R _ {r v} \leq M u _ {r v} \forall v \in V, \forall r \in R\tag{17}
$$

Maximum total service time and route length:

$$
L z _ {i} \geq \sum_ {s \in S} \sum_ {(j, k) \in A} T _ {s} q _ {j s} y _ {i j k} \quad \forall i \in N\tag{18}
$$

$$
R L u _ {r v} \geq \sum_ {(j, k) \in A} d _ {j k} x _ {r v j k} \quad \forall v \in V, \quad \forall r \in R\tag{19}
$$

Time windows:

$$
p _ {i s} s _ {i j} \geq p e _ {j} \sum_ {(j, k) \in A} q _ {j s} y _ {i j k} \quad \forall j \in P, \quad \forall i \in N, \quad \forall s \in S\tag{20}
$$

$$
s _ {i j} \leq p f _ {j} \sum_ {(j, k) \in A} y _ {i j k} \quad \forall j \in P, \quad \forall i \in N\tag{21}
$$

Precedence relationship between pick up and delivery tasks:

$$
x _ {r v O Q} = u _ {r v} \quad \forall r \in R, \quad \forall v \in \{v ^ {\prime} \in V: V q _ {2 v ^ {\prime}} = 1 \}\tag{22}
$$

$$
x _ {r v H D} = u _ {r v} \quad \forall r \in R, \quad \forall v \in \{v ^ {\prime} \in V: V q _ {1 v ^ {\prime}} = 1 \}\tag{23}
$$

Nature of variables:

$$
y _ {i j k}, x _ {r v j k}, u _ {r v}, z _ {i} \in \mathbb {B} \quad \forall i \in N, (j, k) \in A, r \in R, v \in V\tag{24}
$$

$$
s t _ {r v j}, s _ {i j}, S R _ {r v}, E R _ {r v} \geq 0 \quad \forall r \in R, v \in V, j \in P, i \in N\tag{25}
$$

Objective function (1) minimizes the total travel cost and route assignment cost for both nurse and vehicle routes. Constraints (2) ensure that only one HHC nurse can visit a patient. Constraints (3) guarantee that each patient can receive his/her requested HHC service, provided by the appropriate HDVs. Constraints (4) ensure that the routes of vehicles and nurses start and end at the origin and destination nodes, respectively. Constraints (5) and (6) ensure the continuity of each HHC nurse route and HDVs route respectively. Constraints (8) determine the service start time of a HHC nurse at a patient location. Constraints (7)–(11) enforce the synchronization between the HHC nurse routes and HDV routes. Constraints (12) assign HDVs to routes. Constraints (13)–(17) determine the arrival times and service start times at each location of HDVs routes. Constraints (18) and (19) impose the total working hours and route length limits for the HHC nurses and HDVs respectively. Constraints (20) and (21) ensure that the patient time windows are respected in the schedules of HHC nurse routes. Constraints (22) and (23) fix the precedence requirement for pick up/ delivery dependent visits in case of HDV routes. Constraints (24) and (25) impose binary and non-negativity conditions on the corresponding decision variables.

## 4. Solution method

The mathematical model presented in Section 3 is an MILP which could possibly be solved by of-the-shelf integer programming solvers (such as CPLEX and Gurobi). However, for problems of practical sizes, solution times could be unacceptably long due to the large numbers of decision variables and constraints. In our work, a HGA is developed to obtain solutions in a reasonable amount of time.

## 4.1. Solution representation

The structure of our HHC problem requires a representation of two diferent types of home visits (i.e., heterogeneous caregivers and vehicles), multiple visit requirements at each patient location, pick up/ delivery visits related precedence, synchronization between visits and multiple routes for vehicles. Consequently, it is challenging to develop and adopt a solution representation scheme that covers all the aspects. Thus, we develop a unique group encoding scheme for the chromosome which exploits the structure of the HHC problem.

In the HGA, each required service by a patient is represented as a separate visit and then the HDVs visits are synchronized with the HHC nurse visits through a binary Patient-to-Visits Dependency Matrix (PVDM). Patient visits can be classified into two categories: (i) independent visits and (ii) dependent visits. Taking into account these two categories the complete set of patient visits is divided into four subsets. The first subset $V H _ { 1 }$ consists of visits by HHC nurses to perform HHC services. The visits by the HHC nurses are independent as these visits only follow the patient time windows and do not depend on any other visit. The second, third and fourth subsets can be represented as $V H _ { p } , p = 2 , 3 , 4$ respectively. These three subsets contain those types of visits in which patients require one, two and three HDVs services respectively. These three subsets belong to the category of dependent visits as these visits are synchronized with the HHC nurse visits. These visits must also meet pickup-delivery visits related precedence requirements for certain services. An individual solution S is represented by an array of integers of length n (i.e., the total number of visits). Solution S is sorted by these four subsets in the following form: $S _ { i } \in V H _ { p }$ if p = min $\{ p ^ { \prime } : i \le | \cup _ { g = 1 } p ^ { \prime } V H _ { g } | \ \}$ } and $S _ { i } \neq S _ { j } \forall i \neq j .$ In other words, starting from first to the last subset, the first subset precedes the second and so on. In second part of the solution representation scheme, the indices of service operators (i.e., nurses and HDVs) are also stored in which first lists the nurses and then HDVs in a similar fashion. To make one complete solution, the service operators are randomly assigned to the patient visits. If there are n visits, then a completely encoded chromosome can be defined as an array $\mathbf { \Psi } _ { a } = ( a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . , a _ { n } ) ^ { T } ;$ , where a denotes the route assigned to patient visit i.

The solution representation is illustrated by an example consisting of five patients, all of whom require HHC services. The first three patients require only one HDV service, while the fourth and fifth patients require two and three HDVs services respectively. Initially, each in dividual solution (chromosome) consists of two parts. The first part represents the sequence of the visits. Fig. 2 (a) shows the first part of the solution as an array which first stores the group of independent visits followed by the dependent visits. Fig. 2 (b) shows the second part of the solution as an array which first stores the group of HHC nurses followed by the HDVs. Hence the second part shows that five service operators are assigned to these visits. In order to make one complete solution, the service operators from part two are randomly assigned to the patient visits of part one. Fig. 2 (c) shows a completely encoded individual solution. In order to incorporate the synchronization, the visits of this individual solution are further interlinked through PVDM.

## 4.1.1. Patient to visits dependency matrix

The synchronization among corresponding visits is ensured through the introduction of PVDM. During the evaluation of the candidate solutions, PVDM interlinks the synchronized visits to the independent visits and then evaluates the schedules taking into account the synchronization requirement. Thus, PVDM ensures that the vehicle delivery visits to patients are performed during the same time duration when a HHC nurse is visiting the patient. The rows of PVDM represent the patients (P) while columns show the visits $( V t ) . P V D M _ { j w } = 1$ , if visit w ∈ Vt depends on patient j ∈ P, 0 otherwise. Similar to PVDM, a Route Dependent Matrix (RDM) is introduced to adjust the schedules in case of multiple routes assigned to a single HDV service operator. $R D M _ { e r } = 1 $ , if route $r \in R$ is linked to service operator $e \in S O ,$ 0 otherwise. An initial population of eighty chromosomes is randomly generated by randomly assigning the service operators to all the visits.

## 4.2. Fitness evaluation

The fitness evaluation procedure measures the goodness of each individual solution with respect to the set of constraints and the objective function. Each chromosome is decoded to obtain the routes and associated assignment details. The chromosome encoding/decoding scheme developed to represent this HHC problem exploits the group structure for each individual solution.

## 4.2.1. Solution split and merge

Let $V t = [ 1 , 2 , 3 , . . . , n ]$ be the set of n visits and $R = [ 1 , 2 , 3 , . . . , m ]$ be the set of candidate service operators (routes). Suppose that rr routes are utilized out of total m routes. The fitness evaluation process splits each solution S into rr groups and incorporates the feasibility requirements with respect to pickup-delivery visits related precedence. The origin and destination nodes are inserted at specific positions at this stage. The initial solution only assigns the service operator to the visits with respect to the chromosome encoding scheme. On the other hand, the solution split process assists to decode the initial solution and conduct the fitness evaluation. Consequently, each complete route (group) at this step includes the pharmacy node, hospital node and depot nodes depending upon the service provided by that route. The split and merge procedure is explained below:

Step 1: Sort each individual solution S in an ascending order of the index of assigned service operators. Create another array SS of the same length as S. Starting from the first service operator, retrieve the indices of corresponding visit assignments of each service operator from the prior unsorted solution S and store in SS.

Step 2: Divide the sorted solution S into rr groups. The size of each group is equal to the total number of visits assigned to that specific service operator. Enlist all the corresponding visits assigned to each group by extracting the assignment positions/indices for each group from the array SS. Each group represents a route r.

Step 3:. Update the sequence of each route by sorting the corresponding visits of each route r in ascending order with respect to the associated patient time windows.

Step 4: In order to incorporate the feasibility, add the origin and destination nodes in each route.

Step 5: For the dependent visits (pickup-delivery visits), add the pharmacy and hospital nodes to the HDVs routes at certain positions depending upon the service provided by that specific vehicle route.

Step 6:. On the completion of above mentioned Steps 1 to 5, calculate the cumulative route length for each route and cumulative workload for each HHC route.

Step 7: The schedules and routes for HHC nurses and HDVs are created by employing the following rules.

• Starting from the first visit in each route, determine if a specific visit w is dependent $( P V D M _ { j w } = 1 )$ through PVDM.

• Determine if the corresponding assigned route r is also dependent $( R D M _ { e r } = 1 )$ through RDM.

<table><tr><td>Patients</td><td>P1</td><td>P2</td><td>P3</td><td>P4</td><td>P5</td><td>P1</td><td>P2</td><td>P3</td><td>P4</td><td>P4</td><td>P5</td><td>P5</td><td>P5</td></tr><tr><td>Visits</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr></table>

Fig. 2 (a) Patients arrangement as independent and dependent visits

<table><tr><td>Nurses &amp; HDVs</td><td> ${N1}$ </td><td> ${N2}$ </td><td> ${V1}$ </td><td> ${V2}$ </td><td> ${V3}$ </td></tr><tr><td>Service operators</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr></table>

<table><tr><td>Visits</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>Service operators</td><td>2</td><td>1</td><td>2</td><td>2</td><td>1</td><td>4</td><td>3</td><td>3</td><td>5</td><td>4</td><td>5</td><td>3</td><td>4</td></tr></table>

Fig. 2 (c) A completely encoded individual solution  
Fig. 2. Solution representation.

• If $P W D M _ { j w } = 0 ;$ the start time $s _ { i w }$ at the first visit of a HHC nurse route will be equal to the earliest start time of corresponding patient time windows $( s _ { i w } = p e _ { j } )$

• If $P V D M _ { j w } = 1$ and $R D M _ { e r } = 0 .$ , the start time $s t _ { r w w }$ at the first assigned visit of a vehicle (HDV) route will follow the start and finish time of the corresponding HHC visit $\begin{array} { r l r } { ( s t _ { r w w } } & { { } \ge } & { s _ { i w } } \end{array}$ and $s t _ { r { \nu } w } \leq s _ { i w } + T _ { s } q _ { w s } )$

• If $P W D M _ { j w } = 1$ and $R D M _ { e r } = 1 $ , the start time $s t _ { r w }$ at the first assigned visit of a vehicle route will depend on the previous route finish time by the same vehicle $( s t _ { r ^ { \prime } \nu w } \ge E R _ { r \nu } + r g _ { \nu } + t _ { O w } )$ where $r \ > \ r .$

• For any consecutive visit k after visiting the first node, the $s _ { i k }$ and st will depend on the finish time at the current visit and travel time to the next visit. $( { \mathrm { e . g . , } s _ { i k } } = s _ { i w } + T _ { s } q _ { w s } + t _ { w k } )$

HGA assigns penalties if the route length or maximum workload limit is violated by any route, or if any service operator assignment to a specific visit violates the compatibility constraints (i.e., Constraints (3)) or time windows/synchronization constraints (i.e., Constraints (18)–(21)). The total fitness value for each solution S includes the total travelling cost for all the routes, routes assignment cost, and penalties. Let d denote the total distance covered by a route r ∈ rr and $z _ { r a } = 1$ , if route r ∈ rr is assigned to service operator a ∈ SO. We partition visits with penalties, VP, for each solution into two subsets. TW ⊆ VP denotes the set of visits with time windows penalty and $C M \subseteq V P$ denotes the set of visits with compatibility penalty. Moreover, OV denotes the set of routes which exceed the route length or workload limits. Let $\alpha , \beta$ and γ be the penalties for violation of time windows, compatibility, and overloaded routes (work load and route length), respectively. The fitness function (Z) for an individual solution can be expressed as follows:

$$
Z = \sum_ {r \in r r} \left(C d _ {r} + F \sum_ {a \in V} z _ {r a} + B \sum_ {a \in N} z _ {r a}\right) + \alpha | T W | + \beta | C M | + \gamma\tag{|OV|}
$$

(26)

Once the solution evaluation is complete, all the decoded parts of the solution are merged together to form the original encoded solution S. The specific visits which incurred penalties are contained in VP. After merging the routes to form the original solution, each individual solu tion S which contains an element in VP is made feasible through SFRH. SFRH operates on two levels for visits assignment. First, it matches the compatible service operators SO for the VP in an individual solution. Then it further digs deep to find all the compatible service operators for the corresponding visits which are assigned to SO extracted in the first level. The suitable replacement of service operators among the visits in the second level helps to find the compatible and less occupied service operator assignment options for VP in the first level. Through this iterative replacement of service operators considering compatibility, route length and maximum work durations, SFRH aims to find feasible and higher-quality solutions quickly. Fig. 3 illustrates the SFRH in detail. In order to keep the diversity in the population, some infeasible solutions are kept as it is in each generation.

## 4.3. Selection

We employ Roulette Wheel Selection (RWS) [78] to select the candidate solutions which take part in the crossover and mutation. Some of the good individual solutions may vanish during the application of genetic operators in the evolution process. Therefore, in order to conserve the diversity and maintain good solutions in the population, a few randomly selected solutions are kept unchanged in each generation.

Selection Probability = Fitness for solution(S)/ Sum of fitness values for all solutions.

## 4.4. Recombination

Recombination produces a successor population by inducing genetic changes in the source population through recombination operators, i.e., crossover and mutation [78].

## 4.4.1. Crossover

Each position in the chromosome represents a visit, while each in teger gene appears as the assigned service operator. The structure of the encoding method involves diferent types of visits (HHC visits, HDVs visits) along with synchronization and dependent visit constraints. If we employ the traditional crossover method, it may unavoidably create invalid child solutions due to the random displacement of the positions for synchronized and dependent visits. To diversify the population and conserve the problem characteristics, we employ two modified but simple crossover operators: Single point Crossover with Horizontal Swap (SCHS) and Double point Crossover with Horizontal Swap (DCHS). These two crossover operators are further combined with a visits reassignment heuristic to modify the newly produced ofspring. The SCHS and DCHS are implemented as follows:

• Step 1: Randomly select two individual solutions (parents). Depending upon the value of a uniform (0,1) random number, HGA proceeds to SCHS or DCHS.

• Step 2: In case of SCHS, utilize the synchronized visits' characteristics to group the visits into independent and synchronizationbased dependent visits. The synchronization-based dependent visits of the two parent solutions are exchanged, while the independent visits in the ofspring remain the same as in the respective parent solutions. However, in order to implement the DCHS, randomly select two positions along the chromosome. All the visits between these two positions are exchanged between parent 1 and parent 2.

• Step 3: Starting from the first visit in each ofspring, determine if a visit is independent or synchronization dependent. If a visit falls in the synchronization dependent category, then find the corresponding independent visit on which this specific visit depends. In case the service operator (integer value) assigned to the independent visit is higher than the synchronization based dependent visit, the service operators be tween these two visits will be exchanged. This horizontal swap strategy is particularly helpful to assign the service operators according to the solution representation. Only through this horizontal swap procedure, it can encourage that the HHC nurses are assigned to independent visits and HDVs service operators are assigned to synchronization-based dependent visits as the HDVs operators are placed after the HHC nurses in the service operators set developed during the solution representation. Fig. 4 (a) and Fig. 4 (b) show the two randomly selected solutions and the crossover positions for the SCHS and DCHS respectively. The crossover position for the SCHS is the boundary line between the independent visits and synchronization based dependent visits as shown in Fig. 4 (a). Fig. 4 (c) shows the implementation of horizontal swap strategy on the ofspring after the double point crossover, and Fig. 4 (d) shows the modified ofspring after the implementation of double point crossover and horizontal swap strategy. The horizontal swap strategy also works in a similar manner for the SCHS.

## 4.4.2. Visits reassignment heuristic (VRH)

The random assignment of routes during the population initialization stage and subsequent crossover operations may produce the solu tions in which some routes are overloaded with assignments, while some of the routes only have fewer assignments. We define a route as a sequence of stops for a given HHC nurse/HDV. To enhance the balance among the routes within a solution, a VRH is proposed. The ofspring created through crossover operators undergoes a process which eliminates the thin routes; overloaded routes are relieved by transferring some visits to other routes. The lower and upper route limits are calculated based on the average number of visits $A \nu g _ { s o } .$ . The visits assigned to the overloaded or very thin routes are reassigned to other compatible routes within the lower and upper limits. Fig. 5 shows the VRH procedure.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Data: Solution contating VP, associated parameters (e.g.  $[pe_{w}, pf_{w}]$ ,  $Vp_{gv}$ ,  $Vq_{gw}$ ,  $T_{s}$ ,  $q_{ws}$ , RL, L)

Result: A reformed feasible solution

1 Trace the original visits with penalties VP from the index of decoded solution
2 for all w = 1 to VP do
3 Find the service operators (SO) compatible with the requirements of  $VP_{w}$ 
4 for all i = 1 to SO do
5 Set the workload assigned to a HHC nurse  $SO_{i}$  equal to zero ( $L_{i} = 0$ ).
6 Set the route length covered for each HDV  $SO_{i}$  equal to zero ( $RL_{i} = 0$ ).
7 Extract all the visits already assigned (VAA) to the service operator  $SO_{i}$ 
8 Calculate the actual workload ( $L_{i}$ ) for  $SO_{i}$ 
9 Calculate the actual route length ( $RL_{i}$ ) for  $SO_{i}$ 
10 if  $L_{i} + T_{s}q_{ws} \leq L$  and  $RL_{i} + max(d_{wk}) \leq RL$  then
11 Replace the previously assigned operator to the  $VP_{w}$  with  $SO_{i}$ 
12 Move to next visit with penalty (w = w + 1)
13 else if  $L_{i} + T_{s}q_{ws} &gt; L$  and  $RL_{i} + max(d_{wk}) &gt; RL$  then
14 for all h = 1 to VAA do
15 Find all the service operators compatible (SOC) with the requirements of  $VAA_{h}$ 
16 if already assigned operator to the  $VAA_{h}$  is the only compatible option then
17 h = h + 1
18 else
19 for all f = 1 to SOC do
20 Calculate the total workload ( $L_{f}$ ) for each  $SOC_{f}$ 
21 Calculate the total route length ( $RL_{f}$ ) for each  $SOC_{f}$ 
22 if  $L_{f} + T_{s}q_{hs} \leq L$  and  $RL_{f} + max(d_{hk}) \leq RL$  then
23 Replace the previously assigned operator to the  $VAA_{h}$  with  $SOC_{f}$ 
24 Update the assigned visits list for both  $SO_{i}$  and  $SOC_{f}$ 
25 Update the  $L_{i}$  and  $L_{f}$  for  $SO_{i}$  and  $SOC_{f}$  respectively
26 Update the  $RL_{i}$  and  $RL_{f}$  for  $SO_{i}$  and  $SOC_{f}$  respectively
27 if  $L_{i} + T_{s}q_{ws} \leq L$  and  $RL_{i} + max(d_{wk}) \leq RL$  then
28 Replace the previously assigned operator to the  $VP_{w}$  with  $SO_{i}$ 
29 Move to next visit with penalty (w = w + 1)
30 else
31 First perform this check with remaining  $SOC_{f}$ 
32 If remaing  $SOC_{f}$  could not meet the condition then repeat this check with remaining  $VAA_{h}$ 
33 end
34 else
35 end
36 f = f + 1;
37 end
38 end
39 h = h + 1
40 end
41 end
42 i = i + 1
43 end
44 w = w + 1
45 end
</div>

Fig. 3. Solution feasibility reform heuristic.

## 4.4.3. Mutation

The mutation causes random variation in the characteristics of an individual solution. Thus the mutation operator adds diversity in the population by introducing random changes and helps the HGA to evade homogeneous population. We employed a mutation rate equal to 0.05 through a random mutation operator. The mutation operator randomly replaces the assigned service operator for any selected visit in the solution.

## 5. Computational experiments

We conducted a computational study on both randomly generated instances and realistic instances of HHC applications in Hong Kong to assess the computational performance of our proposed approach. The computational experiments were carried out further to examine the impacts of various scenarios. The mathematical model was implemented in OPL and solved through ILOG CPLEX 12.8. On the other hand, HGA was implemented in MATLAB. All the tests were performed on a computer with 2.67GHz Intel Core i5 and 6 GB of RAM. The reported results for the CPLEX were based on a single run of each test instance, while for HGA the best result out of five independent runs was reported due to its stochastic nature. The termination criteria for smallsize problem instances was computed as ten times the total patient visits, whereas no more than 500 iterations were used in this study except for the last instance (G) in the realistic instances where the maximum iterations limit was set at 1000. We created seven diferent sets (A-G) of test instances for the computational experiments. Their characteristics are shown in Table 2. Each HHC nurse was skilled in more than one HHC service, while each HDV provided only a single type of home delivery service out of three available services. Therefore, a separate visit by a compatible HDV was required for each home delivery service requested by a patient. Sets A and B consist of synchro nized double visits services (DS, 1 HHC service and 1 HDV service). Set C consists of synchronized triple visits services (TS, 1 HHC service and 2 HDVs services) along with the DS. While, Set D and rest of the sets require synchronized quadruple visits services (FS, 1 HHC service and 3 HDVs services) along with the DS and TS.

## 5.1. Computational experiments on randomly generated datasets

Four diferent sets (A–D) of randomly generated test instances were used to test the performances of the MILP model and the proposed HGA. Each set of A to D includes five instances, where their characteristics are shown in Table 2. The patients, depot, designated pharmacy and

![](/api/attachments/57RGABKE/fulltext/images/24de8e60b91b634ad682a8cb0e2a92b33a3367ca7b6c6d7f5b1cc1a9ad2cb548.jpg)  
S, Solution; O, Offspring; MO, Modified Offspring  
Fig. 4. Crossover with synchronized visits and horizontal swap strategy.

corresponding hospital were located at random localities in the area of 25 × 25 distance units. The travelling time $t _ { j k }$ was proportional to the Euclidean distance $d _ { j k } .$ Maximum workload limit for HHC nurses and route length limit for HDVs were kept at 420 min and 200 distance units respectively. The duration for patients' time windows was 180 min and all the time window values were randomly distributed within a plan ning period of nine hours. The service durations for the HHC services varied from 30 to 90 min. On the other hand, the HDVs service duration sd was five minutes and transition times rg for multi-route HDVs varied from 7 to 15 min. Fixed costs and travelling costs were similar to the local values charged in Hong Kong. The value of C was 4 Hong Kong Dollars (hkd) per unit of distance, whereas B and F were kept at 500 hkd and 700 hkd, respectively. The penalty value for penalties defined in the fitness function of HGA, α, β and $\gamma ,$ is kept at 1500 hkd, while the values for VRH parameters, lim1 and lim2, are kept at 1.7 and 0.3, respectively. The values for penalties and VRH parameters are based on the trial and error method. Starting from an initial value of 500 for penalty parameters and 1.1 and 0.1 for lim1 and lim2 respectively, these values are increased proportionally to their initial size. The final value for penalty parameters ensured feasibility for solutions over a number

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Data: New offspring from crossover
Result: Balance enhancement across the routes within a solution

1 Detrmine the average visits per service operator ( $Avg_{so}$ )
2 Detrmine the upper limit for assignments to a route ( $UL_{r} = Avg_{so} * lim1$ )
3 Detrmine the lower limit for assignments to a route ( $LL_{r} = Avg_{so} * lim2$ )
4 forall ii = 1 to 2 (child solutions) do
5 Find all the unique routes (r) utilized for each solution and the total number of visits assigned to each specific route
6 forall jj = 1 to number of routes do
7 if Visits assigned to a route  $r_{jj} &lt; LL_{r}$  then
8 Identify all the routes which contain assigned visits within the limits
9 Sort all these routes in ascending order of assigned visits
10 forall kk = 1 to number of routes which exist within the limits do
11 Determine the route  $r_{kk}$  which provides same service as the route  $r_{jj}$ 
12 Replace the assigned route with  $r_{kk}$  for all the visits which were previously assigned to  $r_{jj}$ 
13 Again find all the routes utilized for the solution and the total number of visits assigned to each specific route
14 Move to the next route ( $jj = jj + 1$ );
15 end
16 else if Visits assigned to a route  $r_{jj} &gt; UL_{r}$  then
17 Detrmine the extra number of visits  $num_{v}$  which are more than the  $UL_{r}$ 
18 Repeat all the steps (8-14) and replace the  $r_{jj}$  for all  $num_{v}$  visits with  $r_{kk}$ 
19 Again find all the routes utilized for the solution and the total number of visits assigned to each specific route
20 Move to the next route ( $jj = jj + 1$ )
21 end
22  $jj = jj + 1$ 
23 end
24 ii = ii + 1
25 end
</div>

Fig. 5. Visits reassignment heuristic.

Table 2  
The characteristics of the types of problem instances.

<table><tr><td>Inst.</td><td>Total patient visits required</td><td>Patients</td><td>Nurses</td><td>HDVs</td><td>Vehicle Routes</td><td>DS (%)</td><td>TS (%)</td><td>FS (%)</td><td>PDS</td><td>PTS</td><td>PFS</td></tr><tr><td>A</td><td>10</td><td>5</td><td>2</td><td>3</td><td>3</td><td>100</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td></tr><tr><td>B</td><td>20</td><td>10</td><td>2</td><td>3</td><td>3</td><td>100</td><td>0</td><td>0</td><td>10</td><td>0</td><td>0</td></tr><tr><td>C</td><td>33</td><td>15</td><td>3</td><td>3</td><td>3</td><td>80</td><td>20</td><td>0</td><td>12</td><td>3</td><td>0</td></tr><tr><td>D</td><td>46</td><td>20</td><td>4</td><td>3</td><td>3</td><td>75</td><td>20</td><td>5</td><td>15</td><td>4</td><td>1</td></tr><tr><td>E</td><td>59</td><td>25</td><td>5</td><td>3</td><td>3</td><td>70</td><td>20</td><td>10</td><td>18</td><td>5</td><td>2</td></tr><tr><td>F</td><td>75</td><td>30</td><td>6</td><td>3</td><td>3</td><td>60</td><td>30</td><td>10</td><td>18</td><td>9</td><td>3</td></tr><tr><td>G</td><td>132</td><td>60</td><td>12</td><td>6</td><td>9</td><td>85</td><td>10</td><td>5</td><td>51</td><td>6</td><td>3</td></tr></table>

Note: PDS, PTS, and PFS are the number of patients times DS(%), TS(%) and FS (%), respectively.

Table 3  
Computational performances of the MILP model (solved by CPLEX) and HGA.

<table><tr><td rowspan="3">Inst.</td><td colspan="6">MILP model (solved by CPLEX)</td><td colspan="6">HGA</td><td rowspan="3">Optimality gap (%)</td></tr><tr><td rowspan="2">Total cost</td><td rowspan="2">Time (sec)</td><td colspan="2">Route assignment cost</td><td colspan="2">Route travel cost</td><td rowspan="2">Total cost</td><td rowspan="2">Time (sec)</td><td colspan="2">Route assignment cost</td><td colspan="2">Route travel cost</td></tr><tr><td>HHC cost</td><td>HDVs cost</td><td>HHC cost</td><td>HDVs cost</td><td>HHC cost</td><td>HDVs cost</td><td>HHC cost</td><td>HDVs cost</td></tr><tr><td>A1</td><td>3168.89</td><td>3.00</td><td>700</td><td>1500</td><td>339.05</td><td>629.84</td><td>3198.04</td><td>4.66</td><td>700</td><td>1500</td><td>368.44</td><td>629.96</td><td>0.92</td></tr><tr><td>A2</td><td>3884.75</td><td>2.50</td><td>1400</td><td>1500</td><td>375.25</td><td>609.50</td><td>3884.88</td><td>4.30</td><td>1400</td><td>1500</td><td>375.04</td><td>609.84</td><td>0.00</td></tr><tr><td>A3</td><td>2665.62</td><td>3.50</td><td>700</td><td>1500</td><td>107.99</td><td>357.62</td><td>2727.80</td><td>4.60</td><td>700</td><td>1500</td><td>170.44</td><td>357.36</td><td>2.33</td></tr><tr><td>A4</td><td>3012.00</td><td>2.40</td><td>700</td><td>1500</td><td>236.99</td><td>575.85</td><td>3037.12</td><td>4.60</td><td>700</td><td>1500</td><td>268.40</td><td>568.72</td><td>0.83</td></tr><tr><td>A5</td><td>3143.72</td><td>2.47</td><td>700</td><td>1500</td><td>276.39</td><td>667.34</td><td>3168.20</td><td>4.23</td><td>700</td><td>1500</td><td>301.40</td><td>666.80</td><td>0.78</td></tr><tr><td>B1</td><td>4027.71</td><td>4.50</td><td>1400</td><td>1500</td><td>449.00</td><td>678.71</td><td>4184.28</td><td>9.90</td><td>1400</td><td>1500</td><td>502.68</td><td>781.62</td><td>2.70</td></tr><tr><td>B2</td><td>4139.67</td><td>4.87</td><td>1400</td><td>1500</td><td>478.66</td><td>761.02</td><td>4307.40</td><td>9.55</td><td>1400</td><td>1500</td><td>545.20</td><td>862.20</td><td>4.05</td></tr><tr><td>B3</td><td>4028.36</td><td>15.34</td><td>1400</td><td>1500</td><td>473.94</td><td>654.43</td><td>4136.52</td><td>9.54</td><td>1400</td><td>1500</td><td>534.08</td><td>702.42</td><td>2.68</td></tr><tr><td>B4</td><td>4143.82</td><td>6.00</td><td>1400</td><td>1500</td><td>541.27</td><td>702.55</td><td>4261.84</td><td>9.63</td><td>1400</td><td>1500</td><td>558.96</td><td>802.84</td><td>2.85</td></tr><tr><td>B5</td><td>4280.43</td><td>12.18</td><td>1400</td><td>1500</td><td>623.40</td><td>757.03</td><td>4538.16</td><td>9.95</td><td>1400</td><td>1500</td><td>705.36</td><td>932.84</td><td>6.02</td></tr><tr><td>C1</td><td>5306.11</td><td>7185.00</td><td>2100</td><td>1500</td><td>735.72</td><td>970.40</td><td>5602.20</td><td>18.47</td><td>2100</td><td>1500</td><td>812.68</td><td>1189.52</td><td>5.58</td></tr><tr><td>C2</td><td>5175.89</td><td>4400.00</td><td>2100</td><td>1500</td><td>733.68</td><td>842.21</td><td>5368.08</td><td>18.93</td><td>2100</td><td>1500</td><td>755.96</td><td>1012.14</td><td>3.71</td></tr><tr><td>C3</td><td>5217.77</td><td>7215.00</td><td>2100</td><td>1500</td><td>620.46</td><td>997.32</td><td>5501.60</td><td>17.84</td><td>2100</td><td>1500</td><td>730.76</td><td>1170.84</td><td>5.44</td></tr><tr><td>C4</td><td> $5392.77^a$ </td><td> $7200.00$ </td><td>2100</td><td>1500</td><td>668.44</td><td>1124.33</td><td>5784.04</td><td>18.91</td><td>2100</td><td>1500</td><td>717.84</td><td>1466.16</td><td>7.26</td></tr><tr><td>C5</td><td> $5377.96^b$ </td><td> $7200.00$ </td><td>2100</td><td>1500</td><td>718.38</td><td>1059.58</td><td>5716.92</td><td>18.73</td><td>2100</td><td>1500</td><td>845.72</td><td>1271.18</td><td>6.30</td></tr></table>

<sup>a</sup> Best integer solution found by CPLEX with an optimality gap of 2.32%. Best integer solution found by CPLEX with an optimality gap of 7.11%.

![](/api/attachments/57RGABKE/fulltext/images/d93fedf83b62934ecddf7bc8e4c95fd1a64fc07fbb676721a149187bcc503131.jpg)  
Fig. 6. Total distance resulting from the MILP and HGA solutions.

of experiments and the final values for lim1 and lim2 provided the best solutions for a number of initial tests.

## 5.2. Computational performance on small to medium instances

Computational results on instance sets A-C are provided in Table 3. CPLEX solved each of the instances from the first two instance sets (A & B) optimally in less than seven seconds, except that for two instances of set B it took a longer time (15.34 s, 12.18 s). For Set C of a larger size, solution time increases significantly. Optimal solutions could be ob tained only in three instances (C1 to C3) in 2 h, while only feasible solutions were obtained in the remaining two (C4 and C5). The solutions returned from CPLEX were used as benchmarks to assess the performance of the proposed HGA, which is also presented in Table 3. Optimality gap was used to assess the quality of HGA solutions and defined as:

## Total cost resulting from HGA solution Total cost resulting from MILP Total cost resulting from MILP

Best integer solution and the best bound were also used to measure the performance for some cases where CPLEX could not deliver the optimal solution. For small instances (i.e., sets A and B). HGA did not show benefits as CPLEX could solve all the problems to optimality in around 15 s. Nevertheless, HGA could also produce high-quality solutions (with small optimality gaps ranging from 0% to 6.02%) in less than 10 s. HGA demonstrated its outperformance when solving large instances (i.e., set C). All the C instances could be solved to within an optimality gap of 7.26% in less than 20 s, as compared with the long computational time of CPLEX (more than 4400 s).

Fig. 6 shows the value of total distance against each instance for MILP and HGA solutions. Although results reveal that both MILP and HGA utilized the same the number of routes for each instance the travelling distance shows interesting variations. For instances of Set A, MILP and HGA solutions provide very close solutions, in terms of total distance travelled. For instances of Sets B and C, the gaps between the total distances travelled by MILP and HGA solutions became larger. The travelling distances shown for both the MILP and HGA solutions vary within an instance set but show continuous upward surges when pro blem size increases, as more users are served in larger instances.

Table 4  
Computational eficiency and solution quality of HGA and CPLEX at the selected time points.

<table><tr><td rowspan="3">Inst. Type</td><td rowspan="3">Best Bound</td><td colspan="6">MILP model results</td><td rowspan="2" colspan="3">HGA</td></tr><tr><td colspan="2">2 Minutes</td><td colspan="2">5 Minutes</td><td colspan="2">7 Minutes</td></tr><tr><td>Total Cost CPLEX</td><td>Gap (%)</td><td>Total Cost CPLEX</td><td>Gap (%)</td><td>Total Cost CPLEX</td><td>Gap (%)</td><td>Time (sec)</td><td>Total Cost HGA</td><td>Gap (%)</td></tr><tr><td>C1</td><td>5136.52</td><td>5310.45</td><td>3.39</td><td>5306.90</td><td>3.32</td><td>5306.90</td><td>3.32</td><td>19.00</td><td>5602.20</td><td>9.07</td></tr><tr><td>C2</td><td>5051.39</td><td>5415.49</td><td>7.21</td><td>5271.89</td><td>4.37</td><td>5198.50</td><td>2.91</td><td>18.93</td><td>5368.08</td><td>6.27</td></tr><tr><td>C3</td><td>5093.08</td><td>5464.73</td><td>7.30</td><td>5436.19</td><td>6.74</td><td>5269.14</td><td>3.46</td><td>19.20</td><td>5501.60</td><td>8.02</td></tr><tr><td>C4</td><td>5203.86</td><td>5458.15</td><td>4.89</td><td>5408.24</td><td>3.93</td><td>5378.58</td><td>3.36</td><td>85.00</td><td>5784.04</td><td>11.15</td></tr><tr><td>C5</td><td>4997.40</td><td>5641.77</td><td>12.89</td><td>5618.80</td><td>12.43</td><td>5389.95</td><td>7.86</td><td>95.13</td><td>5716.92</td><td>14.40</td></tr><tr><td>D1</td><td>5090.50</td><td>7627.82</td><td>49.84</td><td>7592.86</td><td>49.16</td><td>7527.26</td><td>47.87</td><td>77.00</td><td>6471.81</td><td>27.14</td></tr><tr><td>D2</td><td>5012.23</td><td>7153.76</td><td>42.73</td><td>7025.70</td><td>40.17</td><td>6480.83</td><td>29.30</td><td>71.20</td><td>6379.00</td><td>27.27</td></tr><tr><td>D3</td><td>5030.78</td><td>7471.18</td><td>48.51</td><td>7446.44</td><td>48.02</td><td>7167.37</td><td>42.47</td><td>83.10</td><td>6565.76</td><td>30.51</td></tr><tr><td>D4</td><td>4997.66</td><td>7353.68</td><td>47.14</td><td>7353.68</td><td>47.14</td><td>6892.86</td><td>37.92</td><td>75.67</td><td>6976.68</td><td>39.60</td></tr><tr><td>D5</td><td>4770.49</td><td>7454.00</td><td>56.25</td><td>7454.00</td><td>56.25</td><td>7198.64</td><td>50.90</td><td>73.00</td><td>6289.08</td><td>31.83</td></tr></table>

## 5.3. Computational performance on medium to large instances

The previous experiments show that the computational complexity increases as the problem size increases. In particular, CPLEX required a long computational time to return optimal solutions for instance set C. To examine the computational performances of the MILP model and HGA on the medium-size problem instances, we performed additional experiments on Sets C and D. The best feasible solutions found by the CPLEX at three selected time points are reported.

Table 4 presents the objective values (i.e., total costs) and optim ality gaps resulting from CPLEX and HGA solutions at three selected time points (2, 5, and 7 min). In these experiments, we define the optimality gap as (best bound – best feasible solution)/best bound, where the best feasible solution is the objective value provided by the CPLEX at the selected time point or the HGA solution, depending on which one is lower. On account of CPLEX failure to provide feasible solutions for the set D within the selected time points, we ran the CPLEX with aggressive cuts for the set D instances. HGA provided solutions for all the instances in less than two minutes. Therefore, the same value of HGA solution is used to compute the gap at each selected time point for the respective instances. For all the instances of Set C, CPLEX provided better solution except Instance C2 (2 min). Still, the HGA solutions were comparable to CPLEX. In case of Set D, HGA provided better solutions as compared to CPLEX for almost all the cases except Instance D4 (7 min). The optimality gaps for all those cases where HGA performed better than the CPLEX for all the time points are shown as the bold value in Table 4. The gap diferences at all three time points were calculated by sub tracting the CPLEX optimality gap from the HGA optimality gap. The results are shown in Fig. 7, where the negative values show the cases which HGA outperformed CPLEX. In case of set C, the maximum difference across all the cases stood at 7.79 percentage points. The maximum gap diference between the CPLEX optimality gap and the HGA optimality gap stood at a much higher value (24.42 percentage points) across all cases of Set D. These results show the superiority of the HGA over CPLEX to deal with the medium-and large-size instances in a reasonable time.

![](/api/attachments/57RGABKE/fulltext/images/2fc53238387037d8ff619b1bab80d3cf4d6b94ffef65d4d8d1a193e01f9b06fa.jpg)  
Fig. 7. Optimality gap diference in terms of percentage points.

## 5.4. Solution improvement with SFRH

To assess the efectiveness of SFRH in the proposed solution algorithm, we ran several experiments using HGA with and without SFRH within HGA. The tests were performed with the previously developed problem instances of diferent sizes. Interestingly, the instances in the first two sets (A and B) could be solved to get the feasible solutions even in the absence of SFRH. However, without SFRH, HGA took a higher number of iterations to improve the solution even for these small-size instances. Figs. 8 and 9 compare the solution improvement by HGA with SFRH and without SFRH respectively. The experiments suggest that SFRH is useful for HGA to quickly identify better-quality solutions with a fewer number of iterations.

## 5.5. Synchronization and increased HDVs services impact

This subsection analyzes the efect of increased HDVs services and synchronization requirement on the total cost and computational time. We performed additional experiments using the first instance of the first three sets (A, B and C). This reference instance of each set is kept unchanged and observes the same characteristics as presented in Section 5.1 and Table 2. All the patients of this instance only require one HHC service and one synchronization-based HDV service, resultantly the share of DS is 100% because of no demand for TS and FS. This instance is used as a reference to determine the efect of changes in the proportion of DS, TS and FS for the rest of the four new instances in each set. For the remaining experiments, we transformed this reference instance of each set by changing the proportion of TS and FS for each consecutive instance produced. All these four new instances in each set only difer with respect to the proportion of DS, TS and FS, while all other characteristics remain the same as in the first instance.

![](/api/attachments/57RGABKE/fulltext/images/43b26a38146157183808e05be80ef1705393f48db677d04d8f18165b983e76a6.jpg)  
Fig. 8. HGA solution improvement results with SFRH for B1

![](/api/attachments/57RGABKE/fulltext/images/da32ff159e1d0bf04078fb5ca15c44623a561939964d29f4e10fb9c852a7357b.jpg)  
Fig. 9. HGA solution improvement results without SFRH for B1.

Table 5 illustrates the impact of variation in synchronized HDV service on total cost. We ran CPLEX to determine the optimal solutions as benchmark. In Instances C2 to C5, optimality was not proven and the best solutions found were used for comparison. HGA computed all the solutions eficiently within a reasonable time. Compared to CPLEX, the computational time of HGA was more stable, where the increase did not grow dramatically as the problem size increased. This suggests that HGA has the capability of solving the variants of the problem with a higher number of synchronization constraints more eficiently. As expected, the optimality gap presented in this table shows comparable results as reported in Table 3 for these sets.

The increase in the percentage of TS and FS not only increases the number of required services at certain patient locations, but also con tributes to the increased cost and a higher number of synchronization constraints. Fig. 10 shows the percent increase in the total cost for the instances of each set in regards to the MILP solution. The percentage increase in total cost for each instance is measured by linking the cur rent total cost of a specific instance with the total cost value of the reference instance under 100% DS visits in each set. We observe that the total cost shows ascending behavior from the first to the last instances in each set. The results presented in Fig. 10 show that the maximum increase in the total cost among the three sets varies between 9% to 21% for MILP solutions. On the other hand, the percentage increase varies between 12% to 25% in case of HGA as shown in Fig. 11. The escalation in the computational time and substantial increase in the total cost with the increasing proportion of synchronized services is due to the higher complexity and larger size of the problem. This increase in total cost can also be credited to the increased visits required to provide multiple services. It is evident from the results that both the MILP model and HGA are sensitive to the number of service visits at each patient location and associated synchronization requirements attached to these visits.

![](/api/attachments/57RGABKE/fulltext/images/689c8e1b5800e47ec7fe7651adca032f49a5e18af883960bbeb43780bab7efea.jpg)  
Fig. 10. Impact of increase in synchronized HDVs services on total cost for MILP solution.

![](/api/attachments/57RGABKE/fulltext/images/240b33a83312597dd27330e416b2f4b2aabd3ba262ae9f325832a6894720288b.jpg)  
Fig. 11. Impact of increase in synchronized HDVs services on total cost for HGA.

Impact of variation in synchronized HDVs services on total cost

<table><tr><td rowspan="2">Inst. type</td><td colspan="3">Sync. HDVs services (%)</td><td colspan="3">MILP Model</td><td colspan="3">HGA</td><td rowspan="2">GAP (%)</td></tr><tr><td>DS (%)</td><td>TS (%)</td><td>FS (%)</td><td>Time (sec)</td><td>Total cost</td><td>Total distance</td><td>Time (sec)</td><td>Total cost</td><td>Total distance</td></tr><tr><td>A1</td><td>100</td><td>0</td><td>0</td><td>2.50</td><td>3884.75</td><td>246.19</td><td>4.30</td><td>3884.88</td><td>246.19</td><td>0.00</td></tr><tr><td>A2</td><td>60</td><td>20</td><td>20</td><td>5.04</td><td>3994.46</td><td>273.62</td><td>4.60</td><td>4092.24</td><td>298.06</td><td>2.45</td></tr><tr><td>A3</td><td>40</td><td>30</td><td>30</td><td>3.64</td><td>4038.63</td><td>284.66</td><td>4.92</td><td>4210.24</td><td>327.56</td><td>4.25</td></tr><tr><td>A4</td><td>20</td><td>40</td><td>40</td><td>2.83</td><td>4208.48</td><td>327.12</td><td>5.00</td><td>4351.04</td><td>362.76</td><td>3.39</td></tr><tr><td>A5</td><td>0</td><td>50</td><td>50</td><td>4.55</td><td>4225.36</td><td>331.34</td><td>5.00</td><td>4402.64</td><td>375.66</td><td>4.20</td></tr><tr><td>B1</td><td>100</td><td>0</td><td>0</td><td>4.50</td><td>4139.67</td><td>309.92</td><td>9.55</td><td>4307.40</td><td>351.85</td><td>4.05</td></tr><tr><td>B2</td><td>60</td><td>20</td><td>20</td><td>215.00</td><td>4409.13</td><td>377.28</td><td>10.00</td><td>4611.00</td><td>427.84</td><td>4.58</td></tr><tr><td>B3</td><td>40</td><td>30</td><td>30</td><td>220.00</td><td>4409.50</td><td>377.12</td><td>11.00</td><td>4568.80</td><td>417.19</td><td>3.61</td></tr><tr><td>B4</td><td>20</td><td>40</td><td>40</td><td>198.00</td><td>4433.53</td><td>383.38</td><td>13.00</td><td>4650.80</td><td>437.70</td><td>4.90</td></tr><tr><td>B5</td><td>0</td><td>50</td><td>50</td><td>580.00</td><td>4505.98</td><td>401.49</td><td>13.15</td><td>4838.00</td><td>484.50</td><td>7.37</td></tr><tr><td>C1</td><td>100</td><td>0</td><td>0</td><td>4400.00</td><td>5175.89</td><td>393.97</td><td>18.47</td><td>5368.08</td><td>442.02</td><td>3.71</td></tr><tr><td>C2</td><td>60</td><td>20</td><td>20</td><td> $7200.00$ </td><td> $5460.93^a$ </td><td>465.23</td><td>21.18</td><td>5821.44</td><td>555.36</td><td>6.60</td></tr><tr><td>C3</td><td>40</td><td>30</td><td>30</td><td>7200.00</td><td> $5650.70^a$ </td><td>512.67</td><td>23.31</td><td>6057.76</td><td>614.44</td><td>7.20</td></tr><tr><td>C4</td><td>20</td><td>40</td><td>40</td><td>7200.00</td><td> $5916.95^a$ </td><td>579.24</td><td>23.40</td><td>6384.12</td><td>696.03</td><td>7.90</td></tr><tr><td>C5</td><td>0</td><td>50</td><td>50</td><td>7200.00</td><td> $6261.57^a$ </td><td>665.39</td><td>24.90</td><td>6711.24</td><td>777.81</td><td>7.18</td></tr></table>

![](/api/attachments/57RGABKE/fulltext/images/d20c741948e654b17e4957a545a73bc476ab4e6115b4c3f8089c743416064475.jpg)  
Fig. 12. Patients, depot, hospital and pharmacy locations of the realistic instances.

## 5.6. Experiments on realistic instances

To illustrate the scalability and performance of our proposed methodology for practical use, we conducted computational experiments on a real dataset from Hong Kong. In Hong Kong, several Integrated Home Care (IHC) service teams work under the supervision of the Government to provide the care and home based support to the elderly and other specific patients with diferent types of disabilities. Some of the services provided by these IHC service teams include re habilitation services, nursing care, home respite services, escort service, provision of meal, and laundry service. We took a IHC agency (St. James' Settlement) in the central and western district of Hong Kong as the origin/destination node (O). A pharmacy (Q) and a nearby hospital (H) were also selected in this case study. Fig. 12 shows the locations of O, O and H through red circles. The patient locations are shown by blue markers. On the basis of this data, seven new problem instances (A-G) were constructed. The distance matrix used in this set of computational experiments was constructed through the Google Distance Matrix API, with the driving times chosen. The values for the remaining parameters were assigned in a similar way as explained in Section 5.1. The char acteristics of these instances are same as given in Table 2.

Table 6 shows the computational results on the realistic instances. We realize that the solution times of the MILP model and HGA on Instances A and B are similar to those in Table 3. The comparable solution times among Instances A and B in both datasets were due to the similar problem sizes. However, as the problem size increased (i.e., Instances C G) the CPLEX computational time increased significantly. We also note that CPLEX could not even compute the lower bound for the last in stance after a run time of two hours. Conversely, HGA was able to find solutions for all the instances in a reasonable computational time. The largest problem instance (G) was solved in 10.56 min by HGA, de monstrating its capability of managing large real-life problems. Among all instances where a lower bound could be obtained (i.e., Instances A to F), the optimality gap remained was bounded by 4.53%. The computational results demonstrate the eficiency of HGA and its solution quality. For illustration purposes, Fig. 13 depicts the routes for transporting the ten patients of Instance B. In Table 7, we provide the distance covered and routes utilized for each instance. These numbers resulted from the MILP model and HGA are of a realistic scale and, therefore, reflect the efectiveness of the approaches.

## 5.7. HGA performance against variable neighborhood search and GA implementations

To better understand the performance of our HGA with respect to other metaheuristic methods, we compared the solutions of HGA with the Variable Neighborhood Search (VNS) and other simple implementations of GA. The basic concept behind VNS [79] is the combination of a shaking procedure, which systematically performs changes in the neighborhood structures, and a local search method. The use of shaking procedure helps VNS to explore the neighborhoods in a preset order without getting trapped in local optima. VNS begins with an initial solution and then depending upon the neighborhood operators a set of neighborhood solutions is defined. A randomly picked solution out of the defined solutions is improved by implementing the shaking procedure and local search until the stopping criterion is reached. More details about VNS can also be found in Hansen and Mladenović [79] and Trautsamwieser et al. [5]. To construct the feasible initial solution, the service operators are randomly assigned to all

Performance of MILP model and HGA on the realistic instances.

<table><tr><td rowspan="3">Inst.</td><td colspan="6">MILP Model</td><td colspan="6">HGA</td><td rowspan="3">GAP (%)</td></tr><tr><td rowspan="2">Total cost</td><td rowspan="2">Time (sec)</td><td colspan="2">Route assignment cost</td><td colspan="2">Route travel cost</td><td rowspan="2">Total cost</td><td rowspan="2">Time (sec)</td><td colspan="2">Route assignment cost</td><td colspan="2">Route travel cost</td></tr><tr><td>HHC cost</td><td>HDVs cost</td><td>HHC cost</td><td>HDVs cost</td><td>HHC cost</td><td>HDVs cost</td><td>HHC cost</td><td>HDVs cost</td></tr><tr><td>A</td><td>2268.80</td><td>4.62</td><td>700</td><td>1500</td><td>26.40</td><td>42.40</td><td>2278.40</td><td>4.35</td><td>700</td><td>1500</td><td>31.60</td><td>46.80</td><td>0.42</td></tr><tr><td>B</td><td>3057.60</td><td>20.78</td><td>1400</td><td>1500</td><td>61.60</td><td>96.00</td><td>3080.00</td><td>9.87</td><td>1400</td><td>1500</td><td>76.40</td><td>103.60</td><td>0.73</td></tr><tr><td>C</td><td>3789.79</td><td>608.00</td><td>2100</td><td>1500</td><td>77.20</td><td>112.60</td><td>3829.30</td><td>17.00</td><td>2100</td><td>1500</td><td>90.85</td><td>138.25</td><td>1.04</td></tr><tr><td>D</td><td> $3835.62^a$ </td><td>7200.00</td><td>2100</td><td>1500</td><td>112.48</td><td>123.14</td><td>3901.80</td><td>60.00</td><td>2100</td><td>1500</td><td>121.40</td><td>180.40</td><td>1.73</td></tr><tr><td>E</td><td> $4490.24^b$ </td><td>7200.00</td><td>-</td><td>-</td><td>-</td><td>-</td><td>4687.60</td><td>91.07</td><td>2800</td><td>1500</td><td>147.60</td><td>240.00</td><td>4.40</td></tr><tr><td>F</td><td> $5235.66^b$ </td><td>7200.00</td><td>-</td><td>-</td><td>-</td><td>-</td><td>5472.07</td><td>113.14</td><td>3500</td><td>1500</td><td>166.27</td><td>305.80</td><td>4.52</td></tr><tr><td>G</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>9950.45</td><td>634.94</td><td>7000</td><td>2000</td><td>438.94</td><td>511.51</td><td>-</td></tr></table>

<sup>a</sup> Best integer values is reported as CPLEX did not deliver optimal solution for this instance.  
<sup>b</sup> Best bound is reported as CPLEX did not deliver optimal solution or best integer value for these instances.

![](/api/attachments/57RGABKE/fulltext/images/cce6a103788aae91738556ae298ec2f7562758d7830b3465033cb970f1c6cc08.jpg)  
Fig. 13. Routes constructed for instance B. The solid lines (red, green) represent the HHC nurse routes, while the dotted lines represent the HDV routes. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Table 7  
Travelling distance and number of routes utilized for the realistic instances.

<table><tr><td rowspan="2">Inst.</td><td colspan="3">MILP Model</td><td colspan="3">HGA</td></tr><tr><td>Total distance</td><td>HHC routes</td><td>HDVs routes</td><td>Total distance</td><td>HHC routes</td><td>HDVs routes</td></tr><tr><td>A</td><td>17.20</td><td>1</td><td>3</td><td>19.60</td><td>1</td><td>3</td></tr><tr><td>B</td><td>39.40</td><td>2</td><td>3</td><td>45.00</td><td>2</td><td>3</td></tr><tr><td>C</td><td>47.45</td><td>3</td><td>3</td><td>57.32</td><td>3</td><td>3</td></tr><tr><td>D</td><td>58.91</td><td>3</td><td>3</td><td>75.45</td><td>3</td><td>3</td></tr><tr><td>E</td><td>-</td><td>-</td><td>-</td><td>96.90</td><td>4</td><td>3</td></tr><tr><td>F</td><td>-</td><td>-</td><td>-</td><td>118.018</td><td>5</td><td>3</td></tr><tr><td>G</td><td>-</td><td>-</td><td>-</td><td>249.186</td><td>10</td><td>4</td></tr></table>

the visits and then the resulting solution is made feasible by the im plementation of SFRH as mentioned in Section 4.2.1 before feeding it to the VNS. Two diferent neighborhood structures were utilized by employing the 2-exchange operator and cross-exchange operator. The 2- exchange operator establishes new neighborhood structure by ex changing a segment of two visits from one route to another, while the cross-exchange operator swaps a random segment of visits between two routes. In case of cross exchange operator, the segment length varies between one and the maximum number of visits in a route. We used 2- opt [80] local search method along the shaking procedure to improve the new solution. The resulting new solutions are only accepted if they are feasible and better than the previous solutions. The process con tinues until all the neighborhoods are explored and solution is not improving anymore. Besides, we also performed experiments with two simple implementations of GA, GA with SFRH (GAF) and GA, on the real dataset instances described in Section 5.6. In case of GAF, two important heuristic components, the VRH and synchronization visits based horizontal swap strategy for crossover operators, were left out from the already implemented HGA algorithm. For GA, we also ignored the SFRH along with two other heuristic components unimplemented in GAF.

Table 8 compares the performance of HGA with VNS, GAF and GA. Total cost (hkd), cpu time (sec) and the number of iterations to reach the lowest cost solution (ILCS) for concerned solution method are presented in this Table against each solution approach. To compare the solution quality of each algorithm against HGA, we also computed the relative gap through this expression:

## Total cost resulting from VNS/GAF/GA solution Total cost resulting from HGA solution Total cost resulting from HGA solution

Considering the relative gap between HGA and VNS, the VNS only performed better for one instance (B) and for other smaller instances the VNS performed same as HGA. However, for large instances (D-G) the HGA outperformed the VNS. Moreover, the VNS consumed more time than HGA and computational time rises significantly for the large instances. While GAF performed similar to HGA for the first two instances the relative gap is high for the rest of the instances except instances C and F. As for as GA is concerned, it only delivered feasible solution for the first two instances and failed to provide feasible solutions for the large instances. Clearly, the computational eficiency measures as shown in Table 8, time and ILCS, are better for HGA than the GAF and GA. It indicates that the heuristic components of HGA, VRH, SFRH and synchronization based horizontal swap strategy, assist it to find better solutions eficiently for large real-life problem instances.

## 5.8. Solution resilience analysis

The departure time-dependent large variation in travel times between diferent points in a route can cause delays and violation of synchronization requirements. To assess the impact of variation in travel times on the schedules, we obtained travel times from the Google Maps API for HDVs routes of instance B and C at four diferent time points of the day. The accumulated travel time for all the nodes included in the origin-destination trip of each route is calculated separately for the four-time points. We computed the standard deviation (Sd) and mean travel time (Mtr) in minutes for the HDV routes of both instances as reported in Table 9. Travel time for a time point (TTP) shows the time required to cover a route at a particular time point. The maximum standard deviations for the routes of instance B and C are 5.12 and 6.12 respectively. These Sd values are computed for the ac cumulated travel times considering whole routes. Thus, the variation in travel times is not high and the standard deviation for travel times remains low in this studied problem which makes the schedules reliable and less fragile. This low variation in travelling time can also be attributed to the fact that almost all of the patients are in one district of the city.

Table 8  
HGA performance against VNS, GAF and GA.

<table><tr><td rowspan="2">Inst.</td><td colspan="3">HGA</td><td colspan="3">VNS</td><td colspan="4">GAF</td><td colspan="4">GA</td></tr><tr><td>Total cost</td><td>Time</td><td>ILCS</td><td>Total cost</td><td>Time</td><td>Gap</td><td>Total cost</td><td>Time</td><td>ILCS</td><td>Gap</td><td>Total cost</td><td>Time</td><td>ILCS</td><td>Gap</td></tr><tr><td>A</td><td>2278.40</td><td>4.35</td><td>2</td><td>2278.40</td><td>40</td><td>0.00</td><td>2278.40</td><td>10</td><td>3</td><td>0</td><td>2278.40</td><td>10</td><td>17</td><td>0</td></tr><tr><td>B</td><td>3080.00</td><td>9.87</td><td>5</td><td>3072.00</td><td>350</td><td>-0.26</td><td>3080.40</td><td>15</td><td>7</td><td>0.01</td><td>3080.40</td><td>15</td><td>30</td><td>0.013</td></tr><tr><td>C</td><td>3829.30</td><td>17.00</td><td>10</td><td>3829.30</td><td>700</td><td>0.00</td><td>3839.30</td><td>22</td><td>12</td><td>0.26</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>3901.80</td><td>60.00</td><td>5</td><td>3923.45</td><td>1250</td><td>0.55</td><td>4576.00</td><td>70</td><td>5</td><td>17.28</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>E</td><td>4687.60</td><td>91.07</td><td>7</td><td>5370.20</td><td>1675</td><td>14.56</td><td>5372.40</td><td>93</td><td>10</td><td>14.61</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>F</td><td>5472.07</td><td>113.14</td><td>295</td><td>5486.40</td><td>3580</td><td>0.26</td><td>5474.80</td><td>119</td><td>305</td><td>0.05</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>G</td><td>9950.45</td><td>634.94</td><td>375</td><td>10,680.68</td><td>9250</td><td>7.34</td><td>10,976.85</td><td>758</td><td>450</td><td>10.32</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 9  
Variation in travel times for routes.

<table><tr><td rowspan="2">Routes</td><td colspan="6">Instance B</td><td colspan="6">Instance C</td></tr><tr><td>TTP1</td><td>TTP2</td><td>TTP3</td><td>TTP4</td><td>Mtr (min)</td><td>Sd (min)</td><td>TTP1</td><td>TTP2</td><td>TTP3</td><td>TTP4</td><td>Mtr (min)</td><td>Sd (min)</td></tr><tr><td>Route1</td><td>47.00</td><td>39.71</td><td>39.16</td><td>49.30</td><td>43.79</td><td>5.12</td><td>47.00</td><td>40.25</td><td>42.90</td><td>52.14</td><td>45.57</td><td>5.18</td></tr><tr><td>Route2</td><td>33.00</td><td>28.79</td><td>26.68</td><td>36.47</td><td>31.24</td><td>4.37</td><td>50.00</td><td>42.80</td><td>44.77</td><td>56.48</td><td>48.51</td><td>6.12</td></tr><tr><td>Route3</td><td>33.00</td><td>28.68</td><td>29.70</td><td>35.26</td><td>31.66</td><td>3.03</td><td>37.00</td><td>30.82</td><td>32.64</td><td>40.86</td><td>35.33</td><td>4.51</td></tr></table>

Table 10  
Impact of delays on solution resilience.

<table><tr><td rowspan="3">Instance</td><td rowspan="3">Initial routes</td><td rowspan="3">Initial TC</td><td colspan="7">Impact of delay</td></tr><tr><td colspan="2">10 (min)</td><td colspan="2">30 (min)</td><td colspan="2">60 (min)</td><td rowspan="2">Total routes</td></tr><tr><td>TC</td><td>AR</td><td>TC</td><td>AR</td><td>TC</td><td>AR</td></tr><tr><td>A</td><td>1</td><td>2278.40</td><td>2278.40</td><td>0</td><td>2278.40</td><td>0</td><td>2995.35</td><td>1</td><td>2</td></tr><tr><td>B</td><td>2</td><td>3080.40</td><td>3080.40</td><td>0</td><td>3080.40</td><td>0</td><td>3798.60</td><td>1</td><td>3</td></tr><tr><td>C</td><td>3</td><td>3829.30</td><td>3829.30</td><td>0</td><td>4541.85</td><td>1</td><td>5243.70</td><td>1</td><td>5</td></tr></table>

Furthermore, to analyze the impact of unexpected delays on the solution fragility, a restructuring heuristic method (RHM) is used to insert the delays in the previously found schedules and to restructure these schedules by allowing the delays. We examined the various levels of unexpected delays in the nurse routes. The HGA solutions obtained in Section 5.6 are used in this analysis as the original solutions. To conduct this analysis, RHM only inserts nurse arrival delays in the first and third visits of every HHC nurse route and if a HHC nurse cannot serve any of the remaining patients within their defined time window then such remaining visits are assigned to a new nurse route (NR). If the new NR is unable to cater all the unvisited patients of the original routes, then another new NR is created for the remaining patients and this process continues until all the visits are scheduled. Table 10 shows the impact of varying levels of unexpected delays (10 min, 30 min, 60 min) on total cost (TC) and solution resilience for the first three real dataset instances (A, B and C). Initial routes, initial TC, TC under the delays, additional routes (AR) and the total number of routes under delays are presented in this table. It is observed that the original solutions remain intact if a delay of only 10 min occurs for all the HHC nurse routes of these three instances. In case of 30 min delay, the solutions of instance A and B show resilience whereas Instance C requires an additional route to compensate for the impact of the delay. Moreover, as we increase the delay to 60 min, the schedules of all three instances become fragile. The increase in TC is due to the inclusion of additional routes because of unexpected delay. This analysis shows that the five solutions (solution without an increase in TC) absorb the small to medium delays (10 min, 30 min) without showing any fragility. Consequently, these five solu tions become more resilient as compared to the original lowest cost solutions. Additionally, the solutions with only one AR are not only significantly less fragile as compared to the other solutions but also acceptably close to the original lowest cost solutions.

The purpose of our integrated HHC and HDVs scheduling approach is to facilitate service delivery for elderly HHC patients by delivering them the necessities and communal services through proper coordination between HHC and HDVs services. The computational results show that the MILP model and HGA can efectively address the problem to integrate the HHC services with the HDVs visits under the complex constraints related to synchronization, multiple services, pickup-delivery visits based-precedence, and multi routes schedules for HDVs.

## 6. Conclusion

The new variant of the HHC problem studied in this article promises a coordinated approach that brings more flexibility for elderly HHC patients to collect and dispatch the home delivery of necessary items during the presence of a home healthcare worker and according to patient specified time windows. It also permits multiple synchronized home delivery services, pickup-delivery visits-based precedence constraints and multiple routes-based schedules for the delivery vehicles. A mathematical model was developed and the solution to the model determines the optimal number of HHC nurses, routes of HHC nurses and delivery vehicles, and synchronized schedules considering the HHC nurse and delivery vehicle visits. Moreover, a hybrid genetic algorithm was developed featuring a novel solution representation scheme and problem-specific crossover operators along with special heuristic procedures. To evaluate the performance of the HGA, extensive computational tests were performed using diferent variations of randomly generated problem instances and varying demand for synchronized home delivery services. The computational results show the efectiveness of the mathematical model and HGA to solve the problem. The results also confirm the sensitivity of the MILP model and HGA in terms of cost and computational time against the increase in the number of synchronization-based multiple HDVs services. The heuristic procedures, SFRH and VRH, assisted the HGA to find better solutions with a fewer number of iterations. The modeling approach is demonstrated through a realistic application in Hong Kong.

The home care operations are subject to uncertainties which may appear due to stochastic HHC service durations and uncertain travel times due to road congestion. Thus synchronization requirements, dependencies and unexpected delays can cause route failures and limit the potential of this study. We intend to include these uncertain parameters in our future research to tackle more realistic situations with resilient solutions.

## Acknowledgment

This research is supported by HMRF Grant, 14151771 from Food and Health Bureau, Hong Kong, the SAR Government, Early Career Scheme27200419 from Research Grants Council (RGC) of Hong Kong, and HKU Seed Fund for Basic Research grant201910159164.

## References

[1] T.-M. Choi, Innovative “bring-service-near-your-home” operations under coronavirus (covid-19/sars-cov-2) outbreak: Can logistics become the messiah? Transport. Res. Part E Logist. Transport. Rev. 101961 (2020).

[2] World Health Organization, World Report on Ageing and Health, WHO Press, Geneva, 2015.

[3] R. Liu, X. Xie, V. Augusto, C. Rodriguez, Heuristic approaches for a special simultaneous pickup and delivery problem with time windows in home health care industry, IFAC Proc. Vol. 45 (6) (2012) 345–350 14th IFAC Symposium on Information Control Problems in Manufacturing.

[4] D.S. Mankowska, F. Meisel, C. Bierwirth, The home health care routing and sche duling problem with interdependent services, Health Care Manage. Sci. 17 (1) (2014) 15–30.

[5] A. Trautsamwieser, M. Gronalt, P. Hirsch, Securing home health care in times of natural disasters, OR Spectr. 33 (3) (2011) 787–813.

[6] E. Cheng, L.J. Rich, A home health care routing and scheduling problem, Technica Report TR98–04, Department of CAAM, Rice University, Houston, USA, 1998.

[7] E. Lanzarone, A. Matta, A cost assignment policy for home care patients, Flex. Serv. Manuf. J. 24 (4) (November 2011) 465–495.

[8] H. Allaoua, S. Borne, L. Létocart, and R.W. Calvo. A matheuristic approach for solving a home health care problem. Electr. Notes Discrete Math., 41:471–478, 2013.

[9] S. Chahed, E. Marcon, E. Sahin, D. Feillet, Y. Dallery, Exploring new operational research opportunities within the home care context: The chemotherapy at home, Health Care Manage, Sci, 12 (2) (2009) 179–191.

[10] O. Braysy, W. Dullaert, P. Nakari, The potential of optimization in communal routing problems: Case studies from Finland, J. Transp. Geogr. 17 (6) (2009) 484–490.

[11] R.B. Bachouch, A. Guinet, S. Hajri-Gabouj, A model for scheduling drug deliveries in a French homecare, International Conference on Industrial Engineering and Systems Management. JESM' 2009, 2009, p. 10 pages. Montréal. Canada

[12] Y. Shi, T. Boudouh, O. Grunder, D. Wang, Modeling and solving simultaneous delivery and pick-up problem with stochastic travel and service times in home health care, Expert Syst. Appl. 102 (2018) 218–233.

[13] Y. Shi, T. Boudouh, O. Grunder, A hybrid genetic algorithm for a home health care routing problem with time window and fuzzy demand, Expert Syst. Appl. 72 (2017) 160-176.

[14] A.S. Abrahams. C.T. Ragsdale. A decision support system for patient scheduling in travel vaccine administration, Decision Supp. Syst. 54 (2012) 215–225.

[15] A. Matta, S. Chahed, E. Sahin, Y. Dallery, Modelling home care organisations from an operations management perspective, Flex. Serv. Manuf. J. 26 (2014).

[16] L. Shen, Computer solutions of the traveling salesman problem, Bell Syst. Tech. J. 44 (10) (1965) 2245–2269.

[17] G. Reinelt, Tsplib—a traveling salesman problem library, ORSA J. Comput. 3 (4)

[18] D.L. Applegate, R.E. Bixby, V. Chvatál, W.J. Cook, The Traveling Salesman Problem: A Computational Study, Princeton University Press, 2006.

[19] N.A. El-Sherbeny, Vehicle routing with time windows: An overview of exact, heuristic and metaheuristic methods, J. King Saud Univ. Sci. 22 (3) (2010)

[20] N. Kohl, J. Desrosiers, O.B.G. Madsen, M.M. Solomon, F. Soumis, 2-path cuts for the vehicle routing problem with time windows. Transport, Sci, 33 (1) (1999) 101–116

[21] O. Bräysy, M. Gendreau, Vehicle routing problem with time windows, part I: Route construction and local search algorithms, Transp. Sci. 39 (1) (2005) 104–118.

[22] S.V. Begur, D.M. Miller, J.R. Weaver, An integrated spatial DSS for scheduling and routing home-health-care nurses. Interfaces 27 (4) (1997) 3–48

[23] C. Fikar, P. Hirsch, Home health care routing and scheduling: A review, Comput. Operat, Res, 77 (2017) 86–95.

[24] F. Grenouilleau, A. Legrain, N. Lahrichi, L.-M. Rousseau, A set partitioning heuristic for the home health care routing and scheduling problem, Eur. J. Operat. Res. 275 (1) (2019) 295–303.

[25] S. Bertels, T. Fahle, A hybrid setup for a hybrid scenario: Combining heuristics for the home health care problem, Comput. Oper. Res. 33 (10) (2006) 2866–2890.

[26] S. Frifita, M. Masmoudi, J. Euchi, General variable neighborhood search for home healthcare routing and scheduling problem with time windows and synchronized visits. Electr, Notes Discrete Math. 58 (2017) 63–70

[27] K. Thomsen, Optimization on Home Care, Master's thesis Informatics and

[28] G. Hiermann, M. Prandtstetter, A. Rendl, J. Puchinger, G. Raidl, Metaheuristics for solving a multimodal home-healthcare scheduling problem, CEJOR 23 (2015) 89-113.

[29] A. Kandakoglu. A. Sauré, W. Michalowski, M. Aguino, J. Graham, B. McCormick, A decision support system for home dialysis visit scheduling and nurse routing, Decis. Support. Syst. 130 (2020) 113224.

[30] M.S. Rasmussen, T. Justesen, A. Dohn, J. Larsen, The Home Care Crew Scheduling

Problem: Preference-based visit clustering and temporal dependencies, Eur. J. Operat. Res. 219 (3) (2012) 598–610.

[31] K. Braekers, R.F. Hartl, S.N. Parragh, F. Tricoire, A bi-objective home care scheduling problem: Analyzing the trade-of between costs and client inconvenience, Eur, J. Operat, Res, 248 (2) (2016) 428–443.

[32] K.-D. Rest, P. Hirsch, Daily scheduling of home health care services using timedependent public transport, Flex. Serv. Manuf. J. 28 (2016) 495–525.

[33] C. Fikar, P. Hirsch, A matheuristic for routing real-world home service transport systems facilitating walking, J. Cleaner Prod. 105 (2015) 300–310.

[34] A.M. Fathollahi-Fard, M. Hajiaghaei-Keshteli, R. Tavakkoli-Moghaddam, A bi-ob jective green home health care routing problem, J. Cleaner Prod. 200 (2018) 423–443.

[35] A. Mohammad, S. Mohammad, J. Mirzapour Al-e, et al., A green delivery-pickup problem for home hemodialysis machines; sharing economy in distributing scarce resources, Transport. Res. Part E Logist. Transport. Rev. 134 (2020) 101815.

[36] R. Liu, B. Yuan, Z. Jiang, A branch-and-price algorithm for the home-caregiver scheduling and routing problem with stochastic travel and service times, Flex. Serv. Manuf, J. 31 (2019) 989–1011

[37] Y. Shi, T. Boudouh, O. Grunder, A robust optimization for a home health care routing and scheduling problem with consideration of uncertain travel and service times, Transp. Res. Part E Logist. Transport. Rev. 128 (2019) 52–95.

[38] J.A. Nasir, C. Dang, Quantitative thresholds based decision support approach for the home health care scheduling and routing problem, Health Care Manage. Sci. 23 (2019) 215–238.

[39] P. Eveborn, P. Flisberg, M. Ronnqvist, Laps care an operational system for staf planning of home care, Eur. J. Oper. Res. 171 (3) (2006) 962–976.

[40] V. Borsani, A. Matta, G. Beschi, F. Sommaruga, A home care scheduling model for human resources, 2006 International Conference on Service Systems and Service Management, volume 1, 2006, pp. 449–454.

[41] Y.F. Shao, J.F. Bard, A.I. Jarrah, The therapist routing and scheduling problem, IIE Transactions 44 (10) (2012) 868–893

[42] S. Nickel, M. Schröder, J. Steeg, Mid-term and short-term planning support for home health care services, Eur. J. Operat. Res. 219 (3) (2012) 574–587.

[43] Y.-J. An, Y.-D. Kim, B.J. Jeong, S.-D. Kim, Scheduling healthcare services in a hom healthcare system, J. Oper. Res, Soc. 63 (11) (2012) 1589–1599.

[44] A. Trautsamwieser, P. Hirsch, A branch-price-and-cut approach for solving the medium-term home health care planning problem, Networks 64 (3) (2014) 143-159.

[45] P.A. Mava Duque, M. Castro. K. Sörensen. P. Goos. Home care service planning. the case of landeliike thuiszorg. Eur. J. Operat. Res. 243 (1) (2015) 292–301

[46] S.E. Moussavi, M. Mahdjoub, O. Grunder, A matheuristic approach to the integration of worker assignment and vehicle routing problems: Application to home healthcare scheduling, Exp. Syst. Appl. 125 (2019) 317–332.

[47] J. Rivera, V. Zapata, Optimization Approaches for a Home Healthcare Routing and Scheduling Problem, (2020), pp. 75–101 01.

[48] G. Carello, E. Lanzarone, A cardinality-constrained robust model for the assignment problem in home care services, Eur. J. Oper. Res. 236 (2) (2014) 748–762.

[49] P. Cappanera, M.G. Scutellà, P. Cappanera, M.G. Scutellà, Joint assignment, scheduling, and routing models to home care optimization: A pattern-based approach, Transport. Sci. 49 (4) (2015) 830–852.

[50] J. Wirnitzer, I. Heckmann, A. Meyer, S. Nickel, Patient-based nurse rostering in

[51] M. Lin, K.S. Chin, X. Wang, K.L. Tsui, The therapist assignment problem in home healthcare structures, Exp, Syst, Appl, 62 (2016) 44–62.

[52] F. Grenouilleau, N. Lahrichi, L.-M. Rousseau, New decomposition methods for home care scheduling with predefined visits, Comput. Oper. Res. 115 (2020) 104855

[53] M. Demirbilek, J. Branke, A. Strauss, Dynamically accepting and scheduling patients for home healthcare, Health Care Manage, Sci, 22 (2018) 140–155

[54] J.A. Nasir, C. Dang, Solving a more flexible home health care scheduling and routing problem with joint patient and nursing staff selection, Sustainability 10 (1 (2018).

[55] S. Nickel, M. Schröder, J. Steeg, Mid-term and short-term planning support for home health care services, Eur, J. Oper, Res, 219 (3) (2012) 574–587.

[56] A.R. Bennett, A.L. Erera, Dynamic periodic fixed appointment scheduling for home health, IIE Trans. Healthcare Syst. Eng. 1 (1) (2011) 6–19.

[57] C. Rodriguez, T. Garaix, X. Xie, V. Augusto, Staff dimensioning in homecare services with uncertain demands, Int J Prod Res, 53 (24) (2015) 7396–7410

[58] M.I. Restrepo, L.-M. Rousseau, J. Vallée, Home healthcare integrated stafing and scheduling, Omega 95 (2020) 102057

[59] M. Blais, S.D. Lapierre, G. Laporte, Solving a home-care districting problem in an urban setting, J. Oper. Res. Soc. 54 (11) (2003) 1141–1147.

[60] E. Benzarti, E. Sahin, Y. Dallery, Operations management applied to home care services: Analysis of the districting problem, Decis. Support. Syst. 55 (2) (May 2013) 587–598.

[61] M. Lin, K.-S. Chin, F. Chao, K.-L. Tsui, An efective greedy method for the meals-onwheels service districting problem. Comput. Indust. Eng. 106 (2017) 1–19.

[62] J.A. Nasir, S. Hussain, C. Dang, An integrated planning approach towards home health care, telehealth and patients group based care, J. Netw. Comput. Appl. 117 (2018) 30–41.

[63] C.R. Busby. M.W. Carter. A decision tool for negotiating home care funding levels ir ontario, Home Health Care Serv. Quart. 25 (3–4) (2006) 91–106.

[64] R. Liu, B. Yuan, Z. Jiang, Mathematical model and exact algorithm for the home care worker scheduling and routing problem with lunch break requirements, Int. J. Prod, Res, 55 (2) (2017) 558–575

[65] C. Akjiratikarl, P. Yenradee, P.R. Drake, Pso-based algorithm for home care worker scheduling in the UK, Comput. Indust. Eng. 53 (2007) 559–583.

[66] A. Trautsamwieser, P. Hirsch, Optimization of daily scheduling for home health care services, J. Appl. Oper. Res. 3 (2011) 124–136.

[67] O. Bräysy, P. Nakari, W. Dullaert, P. Neittaanmäki, An optimization approach for communal home meal delivery service: A case study, J. Computat. Appl. Math. 232 (1) (2009) 46–53.

[68] S. Yalçındağ, A. Matta, E. Şahin, J.G. Shanthikumar, The patient assignment problem in home health care: using a data-driven method to estimate the travel times of care givers, Flexible Serv. Manufact. J. 28 (1–2) (2016) 304–335.

[69] A. Trautsamwieser, P. Hirsch, A branch-price-and-cut approach for solving the medium-term home health care planning problem, Networks 64 (3) (2014) 143–159.

[70] V. De Angelis, Planning home assistance for aids patients in the city of Rome, Italy, Interfaces 28 (3) (1998) 75–83.

[71] J. Bard, Y. Shao, A. Jarrah, A sequential grasp for the therapist routing and scheduling problem, J. Sched. 17 (2) (2014) 109–133.

[72] M. Cissé, S. Yalçındağ, Y. Kergosien, E. Şahin, C. Lenté, A. Matta, Or problems related to home health care: A review of relevant routing and scheduling problems, Oper. Res. Health Care 13–14 (2017) 1–22.

[73] M. Di Mascolo, M.-L. Espinouse, Z. El Hajri, Planning in home health care structures: A literature review. JFAC-PapersOnLine 50 (1) (2017) 4654–4659.

[74] M. Lin, K.-S. Chin, F. Chao, K.-L. Tsui, An efective greedy method for the meals-on wheels service districting problem, Comput. Indust. Eng. 106 (2017) 1–19.

[75] J. Decerle, O. Grunder, A.H. El Hassani, O. Barakat, A memetic algorithm for a home health care routing and scheduling problem, Oper. Res. Health Care 16 (2018) 59–71.

[76] Y. Kergosien, C. Lenté, J.-C. Billaut, Home health care problem: An extended multiple traveling salesman problem, Proceedings of the 4th Multidisciplinary International Scheduling Conference: Theory and Applications (MISTA 2009), 2009, pp. 85–92.

[77] D. Bredström, M. Rönnqvist, Combined vehicle routing and scheduling with temporal precedence and synchronization constraints, Eur. J. Oper. Res. 191 (1) (2008) 19–31.

[78] D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning 1st edition, Addison-Weslev Longman Publishing Co., Inc, Boston, MA, USA. 1989

[79] P. Hansen, N. Mladenović, Variable neighborhood search, in: H.F. Glover, G. Kochenberger (Eds.), Handbook of Metaheuristics, 57 Springer, New York, 2003, pp. 145–184.

[80] G.A. Croes, A method for solving traveling salesman problems, Oper. Res. 6 (1958 791-812.

Jamal Abdul Nasir is a Post-doctoral fellow in the Department of Industrial and Manufacturing Systems Engineering, the University of Hong Kong. He received his B.Sc. degree in Industrial Engineering and Management from the University of the Punjab, Pakistan and M.S. degree in Industrial and Systems Engineering from Korea Advanced Institute of Science and Technology, South Korea. Dr. Nasir earned his Ph.D. in Systems Engineering and Engineering Management from the City University of Hong Kong. During the period, he also worked as an Industrial Engineer at Interloop Limited, Pakistan. His current research interests include systems modeling and optimization, health care service delivery, supply chain systems and transportation planning. He tends to work on application-oriented research problems that try to bring cutting-edge research ideas to main stream practice. His research draws tools from operations research, predictive analytics and queuing theory.

Yong-Hong Kuo is Assistant Professor in the Department of Industrial and Manufacturing Systems Engineering, the University of Hong Kong (HKU). He earned his B.Sc. in Mathematics, with a minor in Risk Management Science, and M.Phil. and Ph.D. in Systems Engineering and Engineering Management, from the Chinese University of Hong Kong (CUHK). During the period, he also worked at the University of California at Berkeley as Visiting Researcher and Oak Ridge National Laboratory as Visiting Student. Prior to joining HKU, he was Research Assistant Professor at Stanley Ho Big Data Decision Analytics Research Centre at CUHK. His research spans theory and application of mathematical modeling and optimization techniques for decision problems encompassing the field of management science. He is interested in modeling problems. devising effective and eficient solution methodologies and by using these tools to improve operations, help system design and derive managerial insights. His current research focus is on the use of big data for decision-making problems in service delivery systems, where most of my applications are within the domains of logistics and transportation services and healthcare service delivery. His research, with his role as Principal Investigator, has been supported by a number of funding agencies, including Hong Kong Research Grants Council, Health and Medical Research Fund, Microsoft Research Asia, and Macao Science and Technology Development Fund. His publications have appeared in journals including Discrete Optimization, IIE Transactions, Production and Operations Management, and Transportation Research Part B & C.
