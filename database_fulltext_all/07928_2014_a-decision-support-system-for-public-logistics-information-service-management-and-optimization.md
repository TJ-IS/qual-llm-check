---
otero_id: 7928
otero_key: "3MSNA43U"
title: "A decision support system for public logistics information service management and optimization"
authors: "Zhi-Hua Hu; Zhao-Han Sheng"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.12.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for public logistics information service management and optimization

Zhi-Hua Hu <sup>a,b,</sup>⁎, Zhao-Han Sheng b

<sup>a</sup> Logistics Research Center, Shanghai Maritime University, Shanghai 201306, China

<sup>b</sup> School of economics and management, Tongji University, Shanghai 200092, China

## a r t i c l e i n f o

Article history: Received 27 March 2012 Received in revised form 6 November 2013 Accepted 3 December 2013 Available online xxxx

Keywords: Decision support system Transportation Public information service Vehicle routing problem Empty load ratio

## a b s t r a c t

Transportation optimization usually aims at minimizing the empty load ratios (ELRs) of vehicles. Most Chinese vehicles for logistics are owned by individual entrepreneurs. Because China is very large, transport distances are typically long, and thus the ELR is very high. The ELR is the primary reason for high transport costs, considerable pollution, and high energy consumption. Many Chinese local governments try to build public transport information services that decrease the ELR. This work proposes a decision support system (DSS) for public logistics information service management and optimization (PLISMO) for vehicle drivers and owners, logistics customers and related logistics service providers and management institutes. The dynamic and real-time matching model between goods and vehicles, and the enabling technologies are important issues for the DSS for PLISMO. Therefore, intelligent positioning technologies are employed to acquire and manage the vehicle status. A model matching vehicles with goods is developed based on an assessment model of transport capability and service priority criteria. A multi-objective real-time scheduling model is devised to minimize the ELR. Based on the concepts and decision-making models for PLISMO, a DSS is created and the architecture of the system is investigated. The effectiveness of the DSS and decision-making models is demonstrated by a case of <sup>fi</sup>nished vehicle logistics (FVL). Analytical results show that the proposed DSS can reduce the ELR and logistics cost. This system helps governments construct DSSs for general PLISMO.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The Chinese economy has been transformed from a planned economy into a market economy. In the planned economy, door-to-door transport was common, and the supplies of goods were planned. Moreover, transport capability was short, such that logistics resources (e.g., vehicles) were utilized fully. After reforms, transport restrictions by the government were eliminated. At this time, China's automobile industry and its entire domestic economy began developing rapidly. Therefore, logistics requirements gradually increased, and transport capacity was challenged.

In the last ten years especially, while China's economy has boomed, logistics resources owned by companies or individuals have been abundant. However, due to the unbalanced distribution of logistics demands in China and the asymmetry of information, logistics resources and their capacity are not fully utilized. The empty load ratio (ELR) is high, such that transport resources are wasted and the environment is polluted. The ELR is the ratio of mileage without load to total mileage in the context of a full or less-than-full truck load. The ELR commonly measures the ef<sup>fi</sup>ciency of a route and waste. According to statistics, the ELR in China was low during the planned economy, and was high, almost reaching 50%, during the market economy; with the evolution of logistics requirements, transport capacity, and information technology, the ELR is dropping to roughly 40%. Notably, different vehicle types may have different ELRs (e.g. taxis have lower ELRs than trucks) and different areas with unbalanced logistics requirements and transport capacities have different ELRs. In China, as an economic indicator and environmental indicator, the ELR can be further minimized

According to the report “The development of highway and waterway transportation industry: Statistical bulletin for 2012” (economic data are primarily from bulletins released by China's Ministry of Transport on the website http://www.moc.gov.cn) released by China's Ministry of Communications, by the end of 2012, China had built 4.2395 million km of road, an increase of 131.1 thousand km from 2011; the number of vehicles was 1339.89 million, an increase of 6.0% from 2011; road freight transport was 31.885 billion tons of goods, an increase of 13.1% from 2011, and turnover of goods was 5.953486 trillion tons km, an increase of 15.9% from 2011; average transport distance was 186.72 km; and investment in road construction was 1.451249 trillion Yuan, an annual increase of 0.3%. These statistics show that road transport has an important role in rapid development; second, the volume of goods and turnover rate is so large that there is ample room for optimization.

The architecture of a decision support system (DSS) for public logistics information service management and optimization (PLISMO) and its decision-making models for vehicle drivers and owners, logistics customers and service providers, and related management institutes are proposed to reduce the ELR and improve the match degree between vehicles and demands. Strategies, models, algorithms, and system architecture are designed. This work mainly contributes to the architecture of the PLISMO and its organizational mechanisms, the service matching model for vehicles and demands, the real-time scheduling model that predicts travel and minimizes the ELR, and the design of the prototype system for the PLISMO. Finally, the models and algorithms are veri<sup>fi</sup>ed by a case of <sup>fi</sup>nished vehicle logistics (FVL).

The remainder of this paper is organized as follows. Section 2 presents a literature review on public logistics service information system and routing problems with consideration of minimizing ELR. Section 3 describes the current situations in China. In Section 4, the DSS and models are developed. Section 5 elucidates a demonstrative case of FVL. Finally, the paper is concluded and directions for future research are given.

## 2. Literature review

(1) Public logistics service information system

Public logistics service information system (PLSIS) is generally used to share transport resources among customers and carriers. Hang [1] implemented a taxi calling system based on intelligent mobile terminal, by which passengers and taxi drivers can exchange information anytime. This system analyzes the randomly appeared personalized passenger transport demand and timely transfers it to the appropriate service provider, so as to fully use the existing taxi service. Taniguchi et al. [2] developed a persuasive communication program that provides publictransport-oriented choice for students. By a PLSIS, arrival information can be shared timely among customers and service providers related to logistics. Rahman et al. [3] noted that actual bus arrival times often deviated from the posted schedules due to a variety of factors; hence, providing real-time bus information can improve service quality.

Logistics systems can be assessed and optimized by integrating their PLSISs. The operational performance of public transport networks is an important aspect of urban planning and development. Mesbah et al. [4] explored the operational performance of public road transport using spatial and historical analysis at a network-wide level. The results help to <sup>fi</sup>nd solutions for improving the public transport system. Tang and Thakuriah [5] investigated the effects of real-time bus information system on ridership. To take account of other factors that might affect bus ridership, they used data on unemployment levels, gas prices, local weather conditions, transit service attributes, and socioeconomic characteristics in the proposed method. De Borger and Fosgerau [6] studied the interaction between pricing, frequency of service and information provision by public transport <sup>fi</sup>rms offering scheduled services under various regulatory regimes. Cheng [7] noted that more and more passengers using public transport system plan their trips by using PLSISs which are provided as website services. Farag and Lyons [8] noted that investments in and growing availability of various services provided by PLSISs make them popular. Policymakers and information service providers could bene<sup>fi</sup>t from a well understanding of factors affecting information use. Moreover, their study provided insights into the use of the PLSISs by applying attitude theory. Tibaut et al. [9] examined the interoperability of passenger information systems in Europe, and asserted that local information systems of public transport service providers should be interoperable with a nation's passenger information system.

Many PLSISs utilize data and function of intelligent transport systems. Jakubauskas [10] applied intelligent transport systems and services to create a multimodal public transport system aimed at improving its ef<sup>fi</sup>ciency. Lei and Church [11] de<sup>fi</sup>ned an extended GIS data structure to handle temporal elements of transit service, and developed a framework for supporting transit service analysis and planning.

Developments are already underway for the integration of information systems across different public transport modals and between PLSISs covering different regions. An integrated information service has a great potential to inform and in<sup>fl</sup>uence travel choices. Lyons [12] considered the prospect of providing travelers with multimodal information that integrates the driver information with public transport service information. PLSIS is a way to coordinate and integrate different transport modals. The European Commission launched a consultation on the ‘Development of Integrated Ticketing for Air and Rail Transport’, in 2008, with the objective of examining the organizational and technical opportunities related to the introduction of integrated ticketing as an important factor to generate demand for intermodal air– rail services. Amsler [13] proposed solutions for integrated ticketing for air and rail transport that coordinate with urban public transport.

Many public information systems are developed for supplier selection [14], investment [15], trading [16], <sup>fi</sup>eld service scheduling [17], and disaster management [18]. These systems are not focused by this work.

(2) Routing problems with consideration of minimizing ELR With the increasing availability of real-time information and communication systems in logistics, the need for appropriate planning algorithms arises. Customers in transport markets increasingly expect quicker and more <sup>fl</sup>exible ful<sup>fi</sup>llment of their orders, especially in the electronic marketplace. Fleischmann et al. [19] considered a dynamic routing system that dispatches a <sup>fl</sup>eet of vehicles according to customer orders arriving at random during the planning period by using dynamic travel time information. Routing in a stochastic and dynamic (timedependent) network is a crucial transportation problem. With the utilization of perfect online information of continuous realtime link travel time, Ardakani and Sun [20] proposed a new variant of adaptive routing problem, and developed an adaptive approach to tackle the continuous dynamic shortest path problem. Boriboonsomsin et al. [21] presented an eco-routing navigation system that determines the most eco-friendly route between a trip origin and a destination by using advanced traveler information systems. Mendoza et al. [22] developed a DSS that integrates commercial systems with a distance-constrained routing module. Suzuki [23] developed a DSS that helps motor carriers route vehicles. These vehicles visit all customers in time (without violating time-windows), and utilize the cheapest gas stations (cheapest truck stops in a region) as refueling points during a tour. Pillac et al. [24] designed an event-driven framework that anticipates unknown changes in a dynamic VRP.

ELR, empty trip, and empty movement are usually considered in optimizing vehicle routing solutions, and their effects on logistics are analyzed in literature. Empty vehicle traf<sup>fi</sup>c plays a critical role in the operating performance of vehicle systems [25]. Utilizing an empty backhaul vehicle on its way back to its domicile after a normal delivery trip has attracted many logistics carriers and third party logistics companies [26]. Johnson [27] presented analytical models to predict empty vehicle travel distance under popular vehicle dispatching rules for systems facing stochastic trip demands. Holguín-Veras and Thorson [28] developed new mathematical formulations that depicted the <sup>fl</sup>ow of empty commercial vehicles as a function of a given matrix of commodity <sup>fl</sup>ows based on probability principles and spatial interaction concepts. Gintner et al. [29] formulated the multiple-depot multiple-vehicle-type scheduling problem in public transport bus companies under the minimization of <sup>fl</sup>eet size and operational costs including costs for empty movements and waiting times. McKinnon and Ge [30] examined the recent trend in empty running by trucks in the UK and assess the potential for a further reduction in empty running in food supply chains. Bock [31] proposed a new real-time-oriented control approach to reduce empty vehicle trips. This approach integrates multimodal transportation and transshipments. Asef-Vaziri et al. [32] developed a global optimization model and a heuristic procedure for the design of a shortcut-enhanced unidirectional loop aislenetwork with pick-up and drop-off stations. The objective is to minimize the total loaded and empty trip distances. Chen et al. [33] studied the interactions between crane handling and truck transportation in a maritime container terminal by addressing them simultaneously. Yard trucks are shared among different ships. This sharing strategy helps to reduce empty truck trips in the terminal area. Empty container trucks may cause a de<sup>fi</sup>cit in transport capacity and contribute to congestion and emissions in the port territory.

Sharing logistics demands and transport resources is a typical strategy used for improving utilization of vehicles and eliminating empty trips. Islam et al. [34] introduced truck-sharing arrangements using a truck appointment system, which potentially reduces the number of empty-truck trips. Hunt and Stefan [35] considered the treatment of less-than-load movements and empty vehicles in a system for modeling commercial movements. This study reduces ELR by introducing a dispatching model for matching vehicles with goods.

## 3. The current situation in China

The characteristics of Chinese road transport are re<sup>fl</sup>ected in road transport conditions, logistics capacity of vehicles, development of logistics demands, mechanisms that match goods and vehicles, and related policies and regulations. After China's transportation department released its vehicle restrictions more than ten years ago, many companies and individuals have gained great pro<sup>fi</sup>t by providing transport services. However, road network information is not updated frequently. Realtime traf<sup>fi</sup>c status is not conveyed, which is an obstacle to real-time transport planning and monitoring systems. In terms of logistics demand, the amount of goods transported on roads is growing rapidly. China's major logistics demand in industry currently comes mainly from the companies themselves. Third-party logistics (3PL) is not well developed, especially to service manufacturer's logistics demands. For mechanisms that match vehicles and goods, systematic research is rare. Although some academics and logistics service providers have researched global scheduling and dispatching models, most of them failed or gave up.

Finally, the policies, regulations, and social culture surrounding social logistics transport are lagging behind China's booming economy. Currently, although a number of regulations and rules exist, their legitimacy and capability to serve industry are not guaranteed, and their enforcement is weak. Because of the imbalance between logistics demands among districts, an asymmetrical information distribution, and imperfect policies and regulations, a high ELR is typical, and overloading is a critical problem. Although some DSSs for PLISMO exist for stowage management and optimization, because of imperfect information, schedules are dif<sup>fi</sup>cult to keep. Therefore, the accuracy of information is important when attempting to decrease the ELR. Moreover, because of a lack of trust, DSSs for PLISMO are dif<sup>fi</sup>cult to extend.

To solve these problems, <sup>fi</sup>ve solutions have been utilized during the last 30 years in China, namely, parking lots, street sweeping, 3PL-based solutions, and alliance and PLISMO. Thirty years ago, generally every town in China had a parking lot, from which vehicles were dispatched. The parking lot is not only accommodation for drivers and vehicles, but also a general goods terminal for temporary storage. The use of original parking lot model has gradually declined. This solution required a large number of parking lots to cater to the transport market, and imposes a strict requirement on time for goods collection and vehicle dispatching. “Street sweeping” is metaphor for city taxi operations. During the last 15 years, the number of vehicles grew rapidly with the growth of logistics. Via information technology, vehicle owners and goods owners can connect, such that vehicle owners can acquire orders by keeping in touch with existing customers. This mode is <sup>fl</sup>exible and requires no additional costs. However, vehicles typically can obtain only one-way orders. The 3PL mode is important for effective utilization of transport resources. However, for the rapid development of the domestic economy, the number of vehicles, and logistics demand, the scale of 3PL is still not suf<sup>fi</sup>cient. Moreover, China is so wide that transport demands of different districts are not balanced. The 3PL enterprises focus mainly on self-owned <sup>fl</sup>eets and dynamically providing transport services to the entire society is dif<sup>fi</sup>cult. Alliances can extend logistics resources and vehicles for scheduling by 3PL. These resources and service capabilities can be reinforced by integrating logistics companies. The greatest success in China is the telephone taxi service system, which integrates various taxi service providers. The basic decision-making rule is to schedule the nearest available vehicles <sup>fi</sup>rst. Generally, taxi companies in the same city integrate into a group with a call center. Because urban populations can be dense, this alliance is particularly successful. However, the “nearest available <sup>fi</sup>rst” principle is dif<sup>fi</sup>cult to apply to road transport (full or less-than-full truckload) because travel distances are long, and dispatching and arrival times, and status of a truck as loaded or empty are dif<sup>fi</sup>cult to predict. The long distance transportations make the vehicles and related customers scattered in a wide space, so determining the status of vehicles and logistics demands is dif<sup>fi</sup>- cult. Finally, developing a model that matches vehicles and goods is complex, especially for <sup>fl</sup>exible modes of transport when multiple non-synchronous orders are assigned to a single vehicle.

The road transport market in China is weak: most enterprises are distributed throughout the country; the concentration degree is low; few national or leading brands exist; and transport products offered by many companies are commonly the same, such that service lacks diversity. Therefore, the four solutions (parking lots, street sweeping, 3PLbased solutions, and alliance) are not applicable. Currently, some DSSs for PLISMO have been developed to help assign goods to vehicles. The main objective is to minimize the ELR. These systems for PLISMO are supported by local governments, and they have good industrial bases to attract logistics companies and manufacturers. However, they do not make a large impact, likely due to the following reasons. First, because of long distance transportation, scattered vehicles and transportation demands in China, the systems for PLISMO cannot cover the transportation demands successfully, and matching vehicles with goods to be transported is dif<sup>fi</sup>cult. Second, the average distance of road transport orders is roughly 180 km, such that arrival or available time for vehicles is dif<sup>fi</sup>cult to predict. Therefore, the scheduling process cannot be precise and the range of resources that can be scheduled is limited. Thus, reducing cost and the ELR is challenging. Third, the system for PLISMO must be restricted to an area, whereas road transport businesses are inter-regional. Furthermore, coordination mechanisms and standard interfaces among different systems for PLISMO are poor. Vehicle drivers cannot dynamically register another system for PLISMO in a new area from the present system for PLISMO. Hence, the application area of the system for PLISMO is limited. Fourth, trust mechanisms for scheduling and organizing transport are lacking. Arrival and departure times estimated by vehicle owners and goods owners are often incorrect.

This work applied a novel DSS for PLISMO to solve these problems. Advanced information technologies are used to monitor and manage the status of logistics resources and processes. Processes of logistics services are redesigned and optimized. A dispatching model is constructed to match vehicles with goods. The DSS monitors vehicles and logistics orders, by controlling logistics processes, and optimizing the matching of vehicles and goods, routing and vehicle scheduling problems.

## 4. The DSS and models

## 4.1. Notations

1) $N E T = ( N , A )$ : a logistics network, where N is a node set and A is an arc set.

2) $X ( n ) , Y ( n ) ;$ the latitude and longitude of $n \in N .$

3) $S ( e ) , E ( e ) { \mathrel { : } }$ the two endpoints in N of $e \in A .$

4) T(e): travel time of $e \in A .$

5) SPT(na,nb): shortest travel time from na $\in N$ $n b \in N .$

6) G: a set of goods.

7) GC: a set of goods types.

8) GC(g): the type o ${ \dot { \boldsymbol { g } } } \in G .$

9) PS: a set of goods properties.

10) $G P _ { g , p } \colon$ the value of property $p \in P S$ of goods $g \in G .$

11) $G P _ { g } \mathrm { : }$ the property vector o $\complement { g } \in G .$

$$
c = M E G (a, b)
$$

13) $G C C _ { c a , c b } = 1$ , if two goods types ca, $c b \in G C$ are compatible; 0 otherwise.

14) V: a set of vehicles.

15) VC: a set of vehicle types.

16) VC(v): the type of $\nu \in V .$

17) ORG(v): the origin node of $\nu \in V .$

18) $V P _ { \nu } \mathrm { : }$ the property vector of $\nu \in V .$

19) $V P _ { \nu , p } \mathrm { : }$ the value of property $p \in P S$ of vehicle $\nu \in V .$

20) $V G _ { \nu , g } = 1$ , if vehicle $\nu \in V$ loads goods $g \in G ; 0 ,$ , otherwise.

21) $G ( \nu ) \colon$ a set of loaded goods of $v \in V .$

22) $V G C _ { c v , c g } = 1 _ { \cdot }$ , if type $c \nu \in V C$ matches $c g \in G C ;$ or else 0.

23) O: a set of orders.

24) OT: a set of temporary orders for generating the candidate set of orders.

25) NS(o), NE(o): the origin and destination nodes of $o \in O .$

26) $T S ( o ) = [ T S L _ { o } , T S U _ { o } ]$ and $T E ( o ) = [ T E L _ { o } , T E U _ { o } ] ;$ : the time-windows at the origin and destination nodes of $o \in O .$

27) T(o): the handling time at the origin and destination nodes of $o \in O .$

28) $G ( o ) { \mathrm { : } }$ the goods of order $o \in O .$

29) $M P ( \nu , g , p ) \in [ 0 , 1 ] ;$ the property matching state for $\nu \in V , g \in G$ on $p \in P S .$

30) MP(v,g): the property matching status between $v \in V$ and $g \in G .$

31) agg ∈ {max, min,mean, ⋯}: an aggregation operator.

32) MVG(v,gto): compatibility between $\nu \in V$ and $g t o \in G .$

33) MGG(v,gto): compatibility between goods $g t o \in G$ and the loaded goods of $v \in V .$

34) M(v,gto): a function matching $\nu \in V$ with the goods to be loaded $( g t o \in G )$ . It synthesizes the status of matching vehicles with goods, compatibility between goods and types of vehicles, and the compatibility between loaded goods and the goods to be loaded.

35) $C N _ { \nu } \colon \mathfrak { c }$ list of nodes that vehicle $\pmb { \nu } \in V \mathrm { { v i s i t s } }$

$$
C T _ {v, n}:
$$

$$
v \in V
$$

$$
n \in N.
$$

37) $C T W _ { \nu , n } = [ C T W L _ { \nu , n } , C T W U _ { \nu , n } ] \colon$ a time-window for $\nu \in V$ at n ∈ N.

38) ON: a set of new orders to be loaded.

39) $D M _ { o a , o b } \mathrm { : }$ the distance from $o a \in O$ to $o b \in O .$

40) $T M _ { o a , o b } \mathrm { : }$ a tag indicating violating the time-window between oa, $o b \in O ,$ one for yes and zero for not.

41) DMMAX: maximum value in DM.

42) TMMAX: maximum value in TM.

43) DMMIN: minimum value in TM.

44) $D T M _ { o a , o b } \mathrm { : }$ the value aggregating DM and TM.

45) $V N O M _ { v , o } \mathrm { : }$ a degree matching $\nu \in V$ with $o \in O N .$

46) $V N O D _ { \nu , o } \mathrm { : }$ a degree matching $\nu \in V$ with $o \in O N$ considering servicing time-window and tag of violating the time-window.

47) $V N O O R G _ { \nu , o } \mathrm { : }$ the distance from the origin of $\nu \in V$ to the position of the new order $o \in O N$ to be loaded.

## 4.2. Framework of the DSS

Compared to the other four solutions (Section 3), this DSS for PLISMO is superior in reducing the high ELR in China; it also reduces cost and environmental pollution. The DSS has the following features. First, the two sides of a transport service, goods and vehicles, are managed; second, a logistics network based on a geographic information system (GIS) is used for scheduling tasks; third, a set of models for matching vehicles with goods, and real-time scheduling, are developed; managerial tools for orders and vehicles are provided to vehicle drivers and owners, logistics customers and service providers, and related management institutes; and, fourth, a set of common modules, primarily including <sup>fi</sup>nance management, human resource management, information management, and trust management, are provided to control the business <sup>fl</sup>ow in the DSS for PLISMO. Fig. 1 presents these functions and roles. The modules are organized in the database, resource and information management, scheduling and decision, and common modules. The DSS has three interfaces for PLISMO: the customer management interface, transport management interface, and vehicle terminal interface. The remainder of this section details scheduling and decision models, as well as the features that make this DSS different from traditional transport management systems.

As mentioned, the DSS uses the logistics network based on GIS to support routes scheduling and visualization. The digital map used by the GIS contains layers of roads. A graph model, denoted as $N E T = ( N , A ) ,$ for the logistics network is constructed from these layers. In Algorithm 1 (see Appendix A for the complete de<sup>fi</sup>nition), the steps for constructing a graph model from a map are elucidated. In practical application, the network can be changed dynamically to match real situations. Therefore, managerial tools for this network model are provided in the DSS. However, this work does not focus on these aspects. The graph is perfectly connected here. Travel time between nodes na and nb is SPT(na,nb).

The resource management system manages the goods relationship, which is the basis for matching vehicles with goods and scheduling vehicles for logistics demands. Goods are commonly transported in a unit package. The goods in each package are from the same type or compatible types. Goods relationship management includes management of goods properties, and a relationship model for types that cannot be put together. The set of goods types is GC. For each $g \in G ,$ , de<sup>fi</sup>ne $G C ( g ) \in G C$ as its type. Moreover, a property vector specifying the goods properties is PS. Then, fo $\cdot g \in G ,$ its properties are represented by $G P _ { g , p } ,$ a vector. $_ \mathrm { O r } ,$ its individual property is denoted as $G P _ { g , p } ,$ , where $p \in P S .$ Here, $G P _ { g , p }$ has three data types: a real or integer number (e.g., weight); an interval with boundaries (e.g., the temperature requirement); or a twodimensional (2D) or three-dimensional (3D) space (e.g., the size of goods or a package). Two packages may be packed into one by a merging function. The merging principles are designed according to speci<sup>fi</sup>c properties in the vector, as de<sup>fi</sup>ned in Eq. (1). Based on the above de<sup>fi</sup>nitions, the compatibility matrix between different types of goods is denoted as $G C C _ { c a , c b } \in \{ 0 , 1 \}$

$$
G P _ {g c} = M E G \left(G P _ {g a}, G P _ {g b}\right)\tag{1}
$$

Vehicle capacity for speci<sup>fi</sup>c goods types is de<sup>fi</sup>ned for matching. $V C ( \nu ) \in V C$ represents the type of vehicle v. The origin point of v is $O R G ( \nu ) \in N ,$ . In 3PL and other logistics systems, vehicles may come from more than one origin node. The de<sup>fi</sup>nitions of VP and $V P _ { \nu , p }$ are similar to those for $G P _ { g }$ and $G P _ { g , p } ,$ where $p \in P S .$ . Before matching vehicle types with goods types, the load matrix between vehicles and goods is de<sup>fi</sup>ned as $V G _ { v , g } \in \{ 0 , 1 \}$ }. Goods $g \in G$ can be loaded by no more than

Please cite this article as: Z.-H. Hu, Z.-H. Sheng, A decision support system for public logistics information service management and optimization, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.12.001

Z.-H. Hu, Z.-H. Sheng / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/3MSNA43U/fulltext/images/c6b6ab0cbc1c9c65bd51cf2a444ec808614a46ed6e5833f6490585c26ef9fcd2.jpg)  
Fig. 1. Framework of the proposed DSS for PLISMO.

one vehicle, as restricted by Eq. (2). If the constraint of Eq. (3) is met, the goods g is not yet loaded on to any vehicle until now. To represent the loaded goods on a vehicle directly, G(v) is derived by Eq. (4).

$$
\forall g \in G, \sum_ {v \in V} V G _ {v. g} \leq 1\tag{2}
$$

$$
\forall g \in G, \sum_ {v \in V} V G _ {v, g} = 0\tag{3}
$$

$$
G (v) = \left\{g \mid V G _ {v. g} = 1, \forall g \in G \right\}, v \in V\tag{4}
$$

The data for an order provide the origin and target nodes in the logistics network, a set of goods, time-windows for departure from the origin and arrival at the target. The set of orders is denoted as O. For any $o \in O ,$ de<sup>fi</sup>ne $N S ( o ) \in N$ and $N E ( o ) \in N ;$ de<sup>fi</sup>ne $T S ( o ) = [ T S L _ { o } , T S U _ { o } ]$ and $T E ( o ) = [ T E L _ { o } , T E U _ { o } ]$ , where $T S L _ { o } , T S U _ { o } , T E L _ { o } ,$ and $T E U _ { o }$ are real numbers. and $T S L _ { o } \leq T S U _ { o }$ and $T E L _ { o } \leq T E U _ { o }$ . Moreover, the prepositions $T ( o ) \in R$ and $G ( o ) \in G$ derive the handling time and goods for order $o \in O .$

## 4.3. Service matching

## 4.3.1. Property matching

The matching criteria differ for different properties. For a property $p \in P S ,$ a matching function $M P ( \nu , g , p )$ computes the matching degree between $\nu \in V$ and $g \in G$ As the value increases, the matching degree increases. If p is weight, $M ( v , g , p )$ is de<sup>fi</sup>ned as Eq. (5). If the property is not related to the match, set the value to 1. By aggregating properties in P, the matching result for property can be aggregated by Eq. (6), where agg is an aggregation operator such as min or max. An operator has a speci<sup>fi</sup>c decision attitude towards risk. Eq. (6) de<sup>fi</sup>nes a matching function for the properties of the relationship between goods and vehicles. The properties describe the real-time status of a vehicle. The matching criterion for types of goods and vehicles is $V G C _ { c \nu , c g } \in \{ 0 , 1 \}$

## 4.3.2. Goods compatibility

Goods compatibility is the compatibility between a vehicle and goods, or between loaded goods and goods to be loaded. Differing from property matching constraints, goods compatibility deals with hard constraints for loading. Hard constraints cannot be avoided during loading or storing goods. Goods to be loaded gto are in the set G, and a vehicle v is used from the set V. The known data for the compatibility matching model are introduced as follows. First, the compatibility between vehicle and goods, M(v,gto) is de<sup>fi</sup>ned as the matching degree between gto and v. Second, the matching relationship between types of gto and v is derived according to VGC, as in Eq. (7). Third, for the compatibility between goods to be loaded and loaded goods, $V G _ { \nu , g }$ is set to one when $g \in G | g t o$ represents loaded goods; and the compatibility between goods to be loaded and loaded goods is derived as $G C C ,$ as in Eq. (8).

## 4.3.3. A holistic matching model

Three matching-related models are presented as Eqs. (6)–(8). Based on Eqs. (6)–(8), a holistic matching model is devised in Eq. (9).

$$
M P (v, g, p) = \left\{ \begin{array}{l} 1, G P _ {g, p} \leq V P _ {v, p} \\ V P _ {v, p} / G P _ {g, p}, G P _ {g, p} > V P _ {v, p} \end{array} \right.
$$

$$
M P (v, g) = a g g _ {p \in P} M P (v, g, p)\tag{5}
$$

6

$$
M V G (v, g t o) = V G C _ {V C (v), G C (g t o)}\tag{7}
$$

$$
M G G (v, g t o) = a g g _ {\left(\forall g \in G \land V G _ {v, g} = 1\right)} G C C _ {G C (g), G C (g t o)}\tag{8}
$$

$$
M (v, g t o) = a g g (M P (v, g t o), M V G (v, g t o), M G G (v, g t o))\tag{9}
$$

## 4.4. Stowage scheduling

## (1) Stowage algorithm

The stowage plan allocates orders to vehicles based on the status of vehicles. A vehicle $\nu \in V$ has three states: $C N _ { \nu } \subseteq N ; C T _ { \nu , n } \in R ,$ and $C T W _ { \nu , n } = [ C T W L _ { \nu , n } , C T W U _ { \nu , n } ]$ for $n \in N .$ Algorithm 2 (see Appendix A for the complete de<sup>fi</sup>nition) provides the inputs and outputs of the stowage processes that consist of three steps. The <sup>fi</sup>rst step generates solutions by merging orders. The second step computes the matching matrix for vehicles and orders so possible stowage plans for orders and vehicles are determined based on other pre-computed properties. The third step assigns orders to vehicles via an allocation model. These processes can be repeated with different settings for order clusters in STEP 1 of Algorithm 2.

## (2) Order clustering and solution generation

The order clustering process generates candidate solutions to be optimized in STEP 3 in Algorithm 2. For orders oa and ob, the merged order is oc, which is added to the order set ON. The merging process utilizes data G, NS, NE, TS (TSL and TSU), TE (TEL and TEU) and T. Algorithm 3 (see Appendix A for the complete de<sup>fi</sup>nition) merges two orders. The procedure, based on compatibility checking results, may refuse to merge orders and return no order. Then, by merging functions or principles, the origin and destination nodes, property vector, time-windows, and the distribution orders are produced from two original orders.

A solution in STEP 1 of Algorithm 2 is a set of orders after merging some original orders. The merging process by clustering is supported by Algorithm 3. In Algorithm 2, after an order set is optimized, the termination process checks the criteria to determine whether Algorithm 2 should proceed or stop. If it proceeds, a new solution will be generated. Strategies for generating new solutions are now studied. Algorithm 3, like Algorithm 2, merges two orders into one. This is the basis of solution generation.

Before discussing the solution process, two matrices are discussed. First, the distance matrix, $D M _ { o a , o b } ,$ , is proposed in Eq. (10), where oa, ob ∈ OT. Here, distance is measured by travel time. Second, the time-window avoidance matrix, $T M _ { o a , o b } ,$ is proposed in Eq. (11).

From the de<sup>fi</sup>nitions of the two matrices, we assert that DM contains nonnegative values, whereas the value of TM can be any numerical value; a low value for DM indicates that the probability for merging two orders is high; when a value in TM is nonnegative, merging two orders is highly likely. Fig. 2 explains how the values of the two matrices determine merging probability.

These two matrices are normalized by Eq. (12), where oa, ob ∈ OT. The probability of merging oa and ob is determined by Eq. (13) by the rule of roulette wheel selection.

Algorithm 4 (see Appendix A for the complete de<sup>fi</sup>nition) details the solving steps. The number of pairs to be merged is a parameter. After each merging process, the matrices for the set of orders are recomputed

## (3) Matrix of degrees of matching vehicles with orders

What factors determine whether an order can be assigned to a vehicle? What about the degree matching a vehicle with an order? These questions are focused on here. The inputs of the matching process are a set of new orders (ON) and a set of vehicles (V). Other sets and values, a set of loaded order (OT) and a logistics network (NET), can be used. The following three factors determine whether o ∈ ON can be assigned to $\nu \in V .$ First, the matching degrees, including various compatibility degrees, should be maximized, as in Eq. (14). Second, when an order is assigned to a vehicle, the distance matrix must be minimized and the time-window avoidance matrix must be maximized. Eq. (13) computes DTM, whereas Eq. (15) maximizes DTM. In Eq. (15), DTM does not consider the fact that a route may be closed. After the assignment is derived, the route after the vehicle arrives at the destination node of this assignment will be reoptimized. Another measure that is commonly used in practice requires a vehicle return to its origin node. Third, the distance from the origin of $\nu \in V$ to the position of the new order $o \in O N$ to be loaded is assigned by the average distance of the vehicle's origin to the origin of every orders including the assigned orders and the new order o, as in Eq. (16), where $\nu \in V$ and $o \in O N$

![](/api/attachments/3MSNA43U/fulltext/images/6015f74e06cf1570143e4f8f08e33a7ba9d60ca656a911361dddd70bb98c47c3.jpg)  
Fig. 2. Merging probability according to distance matrix and time-window avoidance matrix.

## (4) Stowage model that minimizes the ELR

The objective of minimizing the ELR is de<sup>fi</sup>ned by Eq. (15). However, a good solution should maximize the matching degree and minimize distances to origins. A decision variable $\prime n o _ { v , n o } \in \{ 0 , 1 \}$ for $\nu \in V$ and $n o \in O N$ is de<sup>fi</sup>ned, where $\nu n o _ { \nu , n o } = 1$ if no is assigned to $\nu \in V ;$ 0 otherwise. The model is designed as a multi-objective mixed-integer linear programming model in Eq. (17a,b,c,d,e). In practical applications, the following strategies improve model feasibility. First, some virtual vehicles can be added to the set of vehicles. Therefore, orders assigned to a new vehicle cannot be dealt with at this time. Second, in the stage of generating the set of orders (Section 4.4), some orders are merged to reduce the number of <sup>fi</sup>nal orders in the model. By Eq. (18), three objectives are aggregated into one objective. The model is then transferred to an integer linear programming model.

$$
D M _ {o a, o b} = S P T (N E (o a), N S (o b)),\tag{10}
$$

$$
T M _ {o a, o b} = \left(T E U _ {o b} + T S L _ {o b}\right) / 2 - T (o a) - \left(T E U _ {o a} + T S L _ {o a}\right) / 2\tag{11}
$$

$$
D M _ {o a, o b} = D M _ {o a, o b} / D M M A X
$$

$$
T M _ {o a, o b} = \left(T M _ {o a, o b} - T M M I N\right) / T M M A X\tag{12}
$$

$$
D T M _ {o a, o b} = \left(\left(1 - D M _ {o a, o b}\right) + T M _ {o a, o b}\right) / 2\tag{13}
$$

$$
V N O M _ {v, o} = M (v, G (o)), v \in V, o \in O N\tag{14}
$$

$$
V N O D _ {v, o} = \max _ {v g \in G (v)} \left(D T M _ {G (o), v g}\right), v \in V, o \in O N\tag{15}
$$

$$
V N O O R G _ {v, o} = \text { mean } _ {v g \in G (v) \cup \{G (o) \}} \left(S P T _ {N S (v g), O R G (v)}\right)\tag{16}
$$

$$
[ \mathrm{M} 1 ] \text { Maximize }: z _ {m} = \sum_ {v \in V, n o \in O N} \left(V N O M _ {v, n o} \cdot v n o _ {v, n o}\right)\tag{17a}
$$

$$
\text { Minimize }: z _ {d} = \sum_ {v \in V, n o \in O N} \left(V N O D _ {v, n o} \cdot v n o _ {v, n o}\right)\tag{17b}
$$

$$
\text{Minimize}:z_{r} = \sum_{\substack{v\in V, no\in ON\\ \text{s.t.}}}\Big(VNOORG_{v,no}\cdot vno_{v,no}\Big)\tag{17c}
$$

$$
\forall v \in V, \sum_ {n o \in O N} v n o _ {v, n o} \leq 1\tag{17d}
$$

$$
\forall v \in O N, \sum_ {n o \in V} v n o _ {v, n o} = 1\tag{17e}
$$

$$
z = W _ {m} \cdot z _ {m} - W _ {d} \cdot z _ {d} - W _ {r} \cdot z _ {r}\tag{18}
$$

## 5. Case demonstration

This work assesses the effectiveness of the proposed DSS and models using a case of FVL. This work mainly contributes to the design of a DSS for PLISMO and decision models for vehicle drivers and owners, logistics service providers and related management institutes. Although various models are devised, they are all parts of the proposed DSS for PLISMO. Moreover, although FVL is used here as a case, the proposed system

Please cite this article as: Z.-H. Hu, Z.-H. Sheng, A decision support system for public logistics information service management and optimization, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.12.001

architecture and decision-making models can be used to construct a general DSS for PLISMO.

## 5.1. A case of FVL

In FVL, goods are <sup>fi</sup>nished vehicles, and special transporters load and transport the <sup>fi</sup>nished vehicles. As shown in the top-left <sup>fi</sup>gure in Fig. 3, the <sup>fi</sup>nished vehicles are distributed by a special transporter, which can load 1–24 vehicles by adjusting the framework or the inner structure components to be adaptive to speci<sup>fi</sup>c types of vehicles. Although the cells are designed to be able to carry many <sup>fi</sup>nished vehicle types, the design of the frame primarily determines the sets of loadable <sup>fi</sup>nished vehicle types. However, the design of new vehicles is far <sup>fl</sup>exible, and the transporter's <sup>fl</sup>exibility is limited after it is produced. In another aspect, the loaded <sup>fi</sup>nished vehicles may be damaged during the moving process of the transporter. In the bottom-left <sup>fi</sup>gure in Fig. 3, a motion simulation system is demonstrated to simulate the loading and unloading processes. In practice, by no support from mathematical models and algorithms, the planners or drivers of <sup>fi</sup>nished vehicles accumulate feasible matching patterns for transporter types and <sup>fi</sup>nished vehicle types by experiences.

In Fig. 3, a feasible solution is designed by incorporating the techniques of information processing, modeling and optimization. Due to the irregular containers of the transporter and packed <sup>fi</sup>nished vehicles, the methods developed for 3D bin-packing problem cannot be extended for matching <sup>fi</sup>nished vehicles with transporters. Fig. 3 presents three routines for matching patterns of loading <sup>fi</sup>nished vehicles. First, a process of matching pattern discovery is a base to discover new matching patterns by three steps (2D virtual matching test, 3D virtual matching test, and manual matching test); second, the successful matching pattern can be saved to update the patterns database; third, existing patterns can be extracted from the database for the most ef<sup>fi</sup>cient usage. Its three-step approach <sup>fi</sup>rst generates feasible combinations of various types of <sup>fi</sup>nished vehicles by 2D bin-packing with irregular shapes of <sup>fi</sup>nished vehicles [36]. Comparing to 3D bin-packing problem and by determining the maximal number of packed vehicles, the method based on 2D bin-packing can produce feasible solutions during several minutes. Then, the generated feasible loading patterns should be tested by a simulation platform. These two steps are shown in the left two <sup>fi</sup>gures in Fig. 3. However, the principles and implementing details are not the interests in this work. Manual test is an expensive step to verify the solution and produce the suggestions and memos for the inner structure adjustment, and loading and binding approaches.

Comparing to manual test, the former two steps are entitled as virtual loading procedures. The model related to the solver is demonstrated in the following subsections.

Matching pattern between <sup>fi</sup>nished vehicles and transporters reduces the complexity for the packing problem with irregular container spaces (frame of transporter) and packed items (<sup>fi</sup>nished vehicle). To our knowledge, there are few research results on routing and scheduling with irregular container spaces and packed items in the community of 2D and 3D bin-packing. The irregular spaces and shapes increase the complexity of routing and packing problems. According to the shapes, the container space is usually separated into some small compartments (cells of transporter frame) for packed items (<sup>fi</sup>nished vehicle). In practice, the loading solution should satisfy the loading and unloading sequence with minimum handling cost according to the delivery orders [37,38]. However, in FVL, the re-marshaling time can be neglected comparing to the traveling times.

The method based on matching patterns is a practical solution to FVL. The loading likelihood can be optimized by 2D bin-packing approaches [39]. When the sizes of the packed items are diverse, but regular cubes, 3D bin-packing algorithms can be applied [40]. In another aspect, the information systems recorded the historical data, which contains the transporter and loaded <sup>fi</sup>nished vehicles. In the data warehouse, by rolling-up operations, the pairs of transporter type and the types of vehicles can be mined. Therefore, by information system, data warehouse and simply data mining technologies, the historical successful matching patterns can be searched. In this study, matching patterns is the combinations of various <sup>fi</sup>nished vehicles for a given transporter type. By matching patterns, a transporter can be suitable for many combinations of various types of <sup>fi</sup>nished vehicles.

## 5.2. Demonstrative experiments

For demonstration purposes, the FVL logistics network has 12 nodes. The orders and transporters are located at the nodes. To simplify the demonstration, the property vectors of goods and transporters are not considered. In this work, each transporter has eight cells and each cell can load a speci<sup>fi</sup>c set of <sup>fi</sup>nished vehicle types. Each cell can pack a <sup>fi</sup>nished vehicle (Fig. 3). When required, a loaded <sup>fi</sup>nished vehicle can move down to give a room to a <sup>fi</sup>nished vehicle to be loaded. Third, we assume that each order has only one <sup>fi</sup>nished vehicle, and only six vehicles and four orders are involved. Fourth, the time-windows are not considered. Fifth, each transporter only loads the <sup>fi</sup>nished vehicle of a single order. Moreover, the order takes over the <sup>fi</sup>rst cell that is

![](/api/attachments/3MSNA43U/fulltext/images/c57625f6b5d1f8f8cbca363d67d57036c5cc0540c0b09f0f1be156ba6b2d811e.jpg)  
Fig. 3. Matching patterns discovery and updating procedures.

Please cite this article as: Z.-H. Hu, Z.-H. Sheng, A decision support system for public logistics information service management and optimization, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.12.001

Matrix of shortest travel time.

<table><tr><td>Nodes</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>0</td><td>568</td><td>589</td><td>603</td><td>423</td><td>136</td><td>415</td><td>829</td><td>452</td><td>218</td><td>405</td><td>315</td></tr><tr><td>2</td><td>568</td><td>0</td><td>683</td><td>338</td><td>358</td><td>474</td><td>661</td><td>394</td><td>797</td><td>595</td><td>356</td><td>253</td></tr><tr><td>3</td><td>589</td><td>683</td><td>0</td><td>950</td><td>841</td><td>655</td><td>196</td><td>613</td><td>297</td><td>381</td><td>339</td><td>582</td></tr><tr><td>4</td><td>603</td><td>338</td><td>950</td><td>0</td><td>186</td><td>468</td><td>870</td><td>724</td><td>978</td><td>735</td><td>612</td><td>377</td></tr><tr><td>5</td><td>423</td><td>358</td><td>841</td><td>186</td><td>0</td><td>287</td><td>733</td><td>746</td><td>825</td><td>577</td><td>518</td><td>262</td></tr><tr><td>6</td><td>136</td><td>474</td><td>655</td><td>468</td><td>287</td><td>0</td><td>504</td><td>784</td><td>567</td><td>319</td><td>403</td><td>229</td></tr><tr><td>7</td><td>415</td><td>661</td><td>196</td><td>870</td><td>733</td><td>504</td><td>0</td><td>704</td><td>149</td><td>198</td><td>310</td><td>493</td></tr><tr><td>8</td><td>829</td><td>394</td><td>613</td><td>724</td><td>746</td><td>784</td><td>704</td><td>0</td><td>852</td><td>750</td><td>446</td><td>562</td></tr><tr><td>9</td><td>452</td><td>797</td><td>297</td><td>978</td><td>825</td><td>567</td><td>149</td><td>852</td><td>0</td><td>249</td><td>453</td><td>606</td></tr><tr><td>10</td><td>218</td><td>595</td><td>381</td><td>735</td><td>577</td><td>319</td><td>198</td><td>750</td><td>249</td><td>0</td><td>305</td><td>374</td></tr><tr><td>11</td><td>405</td><td>356</td><td>339</td><td>612</td><td>518</td><td>403</td><td>310</td><td>446</td><td>453</td><td>305</td><td>0</td><td>256</td></tr><tr><td>12</td><td>315</td><td>253</td><td>582</td><td>377</td><td>262</td><td>229</td><td>493</td><td>562</td><td>606</td><td>374</td><td>256</td><td>0</td></tr></table>

empty and <sup>fi</sup>t. Table 1 shows the matrix of the shortest travel times between the 12 nodes. The logistics network is a bidirectional graph.

The node set is $N = \{ 1 , 2 , \cdots , 1 2 \}$ and the arc set includes all possible connections between every pair of nodes. The set of transporters is $V = \{ 1 , 2 , 3 , 4 , 5 , 6 \} ;$ ; the set of origin nodes of the transporters is $O R I G I N = \{ 5 , 1 0 , 9 , 1 2 , 7 , 4 \}$ ; the set of the current positions of the transporters is {6,12,4,9,8,7}; and the set of destination nodes of current orders is {1,7,11,4,3,5}. Each transporter has eight cells, denoted as {1,2,3,4,5,6,7,8}. The set of <sup>fi</sup>nished vehicle types is {1,2,3}. The node set of orders to be loaded is {1,4,7,8}; the node set of these destinations for these orders is {9,8,3,2}; and the set of <sup>fi</sup>nished vehicle types of these orders is {2,1,3,3}.

Table 2 lists the matrix of compatibility between cells and <sup>fi</sup>nished vehicle types. In each cell, “1” means that the cell can contain the <sup>fi</sup>nished vehicle type; “0” otherwise.

Based on the matrix of compatibility, Table 3 provides the loadable matrix for the orders to be loaded onto transporters. The transporters with seven cells can accommodate all the three types of <sup>fi</sup>nished vehicles, except that transporter #3 cannot transport <sup>fi</sup>nished vehicles of types #3 and #4. The sequence following the vehicle number is a node sequence of “origin ➔ present ➔ destination” (Table 3); the sequence after the order number indicates the origin and destination nodes of the order.

Because we assume that each transporter has only loaded one <sup>fi</sup>nished vehicle and in the task only a single additional <sup>fi</sup>nished vehicle can be loaded, VNOD and VNOORG are computed simultaneously (Table 4). For each transporter-order pair, three routes are considered, where the number after ‘=’ is the route's travel time. Table 5 shows the routes with the shortest travel times.

Matrix of compatibility between transporter cells and <sup>fi</sup>nished vehicle types.

<table><tr><td>Vehicle</td><td>Cells</td><td colspan="3">Vehicle type</td><td>Transporter</td><td>Cells</td><td colspan="3">Vehicle type</td><td>Transporter</td><td>Cells</td><td colspan="3">Vehicle type</td></tr><tr><td></td><td></td><td>1</td><td>2</td><td>3</td><td></td><td></td><td>1</td><td>2</td><td>3</td><td></td><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td></td><td>2</td><td>1</td><td>0</td><td>0</td><td></td><td>2</td><td>0</td><td>0</td><td>1</td><td></td><td>2</td><td>1</td><td>1</td><td>0</td></tr><tr><td></td><td>3</td><td>1</td><td>1</td><td>0</td><td></td><td>3</td><td>1</td><td>0</td><td>1</td><td></td><td>3</td><td>0</td><td>1</td><td>0</td></tr><tr><td></td><td>4</td><td>1</td><td>0</td><td>1</td><td></td><td>4</td><td>0</td><td>1</td><td>1</td><td></td><td>4</td><td>0</td><td>1</td><td>0</td></tr><tr><td></td><td>5</td><td>1</td><td>1</td><td>1</td><td></td><td>5</td><td>1</td><td>1</td><td>0</td><td></td><td>5</td><td>1</td><td>0</td><td>0</td></tr><tr><td></td><td>6</td><td>1</td><td>1</td><td>0</td><td></td><td>6</td><td>0</td><td>1</td><td>1</td><td></td><td>6</td><td>1</td><td>0</td><td>0</td></tr><tr><td></td><td>7</td><td>1</td><td>1</td><td>1</td><td></td><td>7</td><td>0</td><td>1</td><td>0</td><td></td><td>7</td><td>0</td><td>1</td><td>0</td></tr><tr><td></td><td>8</td><td>0</td><td>0</td><td>1</td><td></td><td>8</td><td>0</td><td>0</td><td>1</td><td></td><td>8</td><td>0</td><td>1</td><td>0</td></tr><tr><td>4</td><td>1</td><td>1</td><td>0</td><td>0</td><td>5</td><td>1</td><td>1</td><td>1</td><td>0</td><td>6</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td></td><td>2</td><td>0</td><td>1</td><td>0</td><td></td><td>2</td><td>1</td><td>0</td><td>1</td><td></td><td>2</td><td>0</td><td>1</td><td>1</td></tr><tr><td></td><td>3</td><td>1</td><td>0</td><td>1</td><td></td><td>3</td><td>1</td><td>1</td><td>0</td><td></td><td>3</td><td>0</td><td>1</td><td>1</td></tr><tr><td></td><td>4</td><td>1</td><td>1</td><td>0</td><td></td><td>4</td><td>1</td><td>1</td><td>0</td><td></td><td>4</td><td>0</td><td>0</td><td>1</td></tr><tr><td></td><td>5</td><td>0</td><td>1</td><td>1</td><td></td><td>5</td><td>1</td><td>1</td><td>0</td><td></td><td>5</td><td>1</td><td>0</td><td>0</td></tr><tr><td></td><td>6</td><td>1</td><td>0</td><td>1</td><td></td><td>6</td><td>1</td><td>1</td><td>0</td><td></td><td>6</td><td>1</td><td>0</td><td>0</td></tr><tr><td></td><td>7</td><td>1</td><td>1</td><td>0</td><td></td><td>7</td><td>0</td><td>1</td><td>0</td><td></td><td>7</td><td>1</td><td>1</td><td>1</td></tr><tr><td></td><td>8</td><td>0</td><td>1</td><td>0</td><td></td><td>8</td><td>0</td><td>0</td><td>0</td><td></td><td>8</td><td>0</td><td>1</td><td>1</td></tr></table>

Table 3 Matrix of VNOM.

<table><tr><td rowspan="2"></td><td colspan="4">Orders to be loaded</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Vehicle</td><td> $1(1 \rightarrow 9)$ </td><td> $2(4 \rightarrow 8)$ </td><td> $3(7 \rightarrow 3)$ </td><td> $4(8 \rightarrow 2)$ </td></tr><tr><td> $1(5 \rightarrow 6 \rightarrow 1)$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $2(10 \rightarrow 12 \rightarrow 7)$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $3(9 \rightarrow 4 \rightarrow 11)$ </td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $4(12 \rightarrow 9 \rightarrow 4)$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $5(7 \rightarrow 8 \rightarrow)$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $6(4 \rightarrow 7 \rightarrow 5)$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

Based on the above analysis, [M1] is simpli<sup>fi</sup>ed to [M2] for demonstration purpose. The matrix VNODORG combines VNOD and VNOORG. Table 5 shows the results of VNODORG. Eq. (19c) checks the compatibility between transporters and orders.

$$
[ \mathrm{M} 2 ] \text { Maximize }: z = \sum_ {v \in V, n o \in O N} \left(V N O D O R G _ {v, n o} \cdot v n o _ {v, n o}\right)\tag{19}
$$

Subject to:

$$
\forall v \in V, \sum_ {n o \in O N} v n o _ {v, n o} \leq 1\tag{19a}
$$

$$
\forall v \in O N, \sum_ {n o \in V} v n o _ {v, n o} = 1\tag{19b}
$$

$$
\forall v \in V, \forall n o \in O N, v n o _ {v, n o} \leq V N O M _ {v, n o}.\tag{19c}
$$

By CPLEX, [M2] can be solved within 1 s. Table 5 presents assignment results in bolded and underlined fonts. The <sup>fi</sup>rst order is assigned to transporter #2; the second to #3; the third to #6; and the fourth to #5. Minimal total travel time is 5233 when all vehicles return to their origin nodes.

## 5.3. Extension for general PLISMO

The above demonstration case of FVL (Sections 5.1 and 5.2) describes a DSS that was developed for a very famous Chinese FVL service provider. Although FVL is a special form of logistics, this DSS is based on the matching patterns between transporters and finished vehicles, and the framework proposed in Fig. 1. The FVL service provider has a market share of at least 37% in China in the recent years. By utilization of the DSS for PLISMO, the ELR is reduced by more than 5%. By cooperation with other FVL service providers, the ELR was claimed to be reduced more than 20% (this results are imprecise because they are just compared with history data when no such DSS was used). Numerous <sup>fi</sup>nished vehicles are based nationwide. This FVL service provider's experience of constructing PLISMO is extended for general vehicle transportation purposes. The main differences exit in the de<sup>fi</sup>nitions of matching patterns between vehicles and goods to be transported. A DSS for PLISMO was developed based on the experiences from this FVL service provider for general goods transportation. Vehicle drivers and owners can register as members of the system. So the positions of vehicles are reported to the system by Global Positioning System (GPS) for matching with goods of orders to be transported and scheduling for transportation orders.

## 5.4. Managerial implications

The proposed DSS for PLISMO depends on the implementation of the devised decision-making models, the application of various technologies, and the operational strategies. Based on existing FVL, four implications for practitioners are discussed. First, the designs of GPS terminals must satisfy the following characteristics in addition to having the common functions: the positioning ef<sup>fi</sup>ciency and precise for vehicles can be improved; the service number for communication can be changed interactively by drivers; the GPS terminals provide interfaces to accept order assignments and routing results; and radio-frequency identi<sup>fi</sup>cation (RFID) or other identi<sup>fi</sup>cation technologies should be integrated to provide vehicle's property information and real-time loading information. Second, solving the trust problem and bene<sup>fi</sup>t allocation are important to successful applications of the DSS for PLISMO. The following points comment on the DSS for PLISMO: real-time positions can be acquired by GPS terminals and loaded orders; information related to location and order can be con<sup>fi</sup>rmed by the drivers and the DSS; mechanisms can be constructed to identify cheating problems and punish them by reducing the orders they are assigned to; and bene<sup>fi</sup>t allocation and order assignment should follow the principles of fairness and rationality, which should be carefully designed and guaranteed. Third, the following situations should be improved by designing mechanisms and applying advanced technologies. Healthy competition should be promoted by pricing supervision and logistics legislation. Inaccurate and overmuch information on orders or available vehicles should be prohibited by authentication and real-time location technologies. The DSS for PLISMO should be run by markets, not governmentrelated companies, to increase ef<sup>fi</sup>ciency and service quantity and reduce operational cost. Fourth, a hierarchical framework that supports various DSSs for PLISMO can cope with China's vastness, computational performance, and data management dif<sup>fi</sup>culties.

Matrix combining VNOD and VNOORG.

<table><tr><td rowspan="3">Vehicle</td><td colspan="4">Orders to be loaded</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>1(1→9)</td><td>2(4→8)</td><td>3(7→3)</td><td>4(8→2)</td></tr><tr><td rowspan="3">1(5→6→1)</td><td>(6→1→1→9→5)=1413</td><td>(6→1→4→8→5)=2209</td><td>(6→1→7→3→5)=1588</td><td>(6→1→8→2→5)=1717</td></tr><tr><td>(6→1→9→1→5)=1463</td><td>(6→4→8→1→5)=2444</td><td>(6→7→3→1→5)=1712</td><td>(6→8→2→1→5)=2169</td></tr><tr><td>(6→1→1→9→5)=1413</td><td>(6→4→1→8→5)=2646</td><td>(6→7→1→3→5)=2349</td><td>(6→8→1→2→5)=2539</td></tr><tr><td rowspan="3">2(10→12→7)</td><td>(12→7→1→9→10)=1609</td><td>(12→7→4→8→10)=2837</td><td>(12→7→7→3→10)=1070</td><td>(12→7→8→2→10)=2186</td></tr><tr><td>(12→1→9→7→10)=1114</td><td>(12→4→8→7→10)=2003</td><td>(12→7→3→7→10)=1083</td><td>(12→8→2→7→10)=1815</td></tr><tr><td>(12→1→7→9→10)=1128</td><td>(12→4→7→8→10)=2701</td><td>(12→7→7→3→10)=1070</td><td>(12→8→7→2→10)=2522</td></tr><tr><td rowspan="3">3(9→4→11)</td><td>(4→11→1→9→9)=1469</td><td>(4→11→4→8→9)=2800</td><td>(4→11→7→3→9)=1415</td><td>(4→11→8→2→9)=2249</td></tr><tr><td>(4→1→9→11→9)=1961</td><td>(4→4→8→11→9)=1623</td><td>(4→7→3→11→9)=1858</td><td>(4→8→2→11→9)=1927</td></tr><tr><td>(4→1→11→9→9)=1461</td><td>(4→4→11→8→9)=1910</td><td>(4→7→11→3→9)=1816</td><td>(4→8→11→2→9)=2323</td></tr><tr><td rowspan="3">4(12→9→4)</td><td>(9→4→1→9→12)=2639</td><td>(9→4→4→8→12)=2264</td><td>(9→4→7→3→12)=2626</td><td>(9→4→8→2→12)=2349</td></tr><tr><td>(9→1→9→4→12)=2259</td><td>(9→4→8→4→12)=2803</td><td>(9→7→3→4→12)=1672</td><td>(9→8→2→4→12)=1961</td></tr><tr><td>(9→1→4→9→12)=2639</td><td>(9→4→4→8→12)=2264</td><td>(9→7→4→3→12)=2551</td><td>(9→8→4→2→12)=2167</td></tr><tr><td rowspan="3">5(7→8→3)</td><td>(8→3→1→9→7)=1803</td><td>(8→3→4→8→7)=2991</td><td>(8→3→7→3→7)=1201</td><td>(8→3→8→2→7)=2281</td></tr><tr><td>(8→1→9→3→7)=1774</td><td>(8→4→8→3→7)=2257</td><td>(8→7→3→3→7)=1096</td><td>(8→8→2→3→7)=1273</td></tr><tr><td>(8→1→3→9→7)=1864</td><td>(8→4→3→8→7)=2991</td><td>(8→7→3→3→7)=1096</td><td>(8→8→3→2→7)=1957</td></tr><tr><td rowspan="3">6(4→7→5)</td><td>(7→5→1→9→4)=2586</td><td>(7→5→4→8→4)=2367</td><td>(7→5→7→3→4)=2612</td><td>(7→5→8→2→4)=2211</td></tr><tr><td>(7→1→9→5→4)=1878</td><td>(7→4→8→5→4)=2526</td><td>(7→7→3→5→4)=1223</td><td>(7→8→2→5→4)=1642</td></tr><tr><td>(7→1→5→9→4)=2641</td><td>(7→4→5→8→4)=2526</td><td>(7→7→5→3→4)=2524</td><td>(7→8→5→2→4)=2146</td></tr></table>

## 6. Conclusions

With large investment in warehousing and transport infrastructures, equipment and employees, logistics becomes a worldwide booming industry. Empty backhaul trip and low ELR are problems involved in very

## Table 5

Simpli<sup>fi</sup>ed matrix combining VNOD and VNOORG.

<table><tr><td rowspan="2"></td><td colspan="4">Orders to be loaded</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Vehicle</td><td> $1(1 \rightarrow 9)$ </td><td> $2(4 \rightarrow 8)$ </td><td> $3(7 \rightarrow 3)$ </td><td> $4(8 \rightarrow 2)$ </td></tr><tr><td> $1(5 \rightarrow 6 \rightarrow 1)$ </td><td>1413</td><td>2209</td><td>1588</td><td>1717</td></tr><tr><td> $2(10 \rightarrow 12 \rightarrow 7)$ </td><td> $\underline{1114}$ </td><td>2003</td><td>1070</td><td>1815</td></tr><tr><td> $3(9 \rightarrow 4 \rightarrow 11)$ </td><td> $\underline{1461}$ </td><td> $\underline{1623}$ </td><td>1415</td><td>1927</td></tr><tr><td> $4(12 \rightarrow 9 \rightarrow 4)$ </td><td>2259</td><td> $\underline{2264}$ </td><td>1672</td><td>1961</td></tr><tr><td> $5(7 \rightarrow 8 \rightarrow 3)$ </td><td>1774</td><td>2257</td><td>1201</td><td> $\underline{1273}$ </td></tr><tr><td> $6(4 \rightarrow 7 \rightarrow 5)$ </td><td>1878</td><td>2367</td><td> $\underline{1223}$ </td><td> $\underline{1642}$ </td></tr></table>

complex decision-making processes due to matching vehicles and goods, and dispatching vehicles for goods. The development of public logistics and transport service information systems that provide dynamic and real-time information on vehicles and goods is a base of the proposed DSS. The reduction of ELR contributes to minimizing the logistics cost, energy and pollution. Developing a framework of the proposed DSS for PLISMO, and related matching and stowage scheduling models, the proposed method is promising to provide the meaningful insights and quantitative advices on how to build a DSS for PLISMO by using optimization models and advanced information technologies. As a result, the contribution of the proposed DSS would be enormous.

The primary aim of this paper is to provide new formulations and system framework as an integral solution to a DSS for PLISMO. This work designs a DSS for PLISMO and decision-making models for vehicle drivers and owners, logistics service providers and related management institutes to decrease the ELR. First, developing a general property vector for goods and vehicles after analyzing some industrial applications, such as <sup>fi</sup>nished vehicle transport and food transport, is dif<sup>fi</sup>cult. New modeling solutions may exist to support different goods and vehicle types. These types of goods and vehicles can be used to design logistics standards. In a sense, the formulations at the operational level are the most important components of this DSS, whereas the proposed framework of the DSS for PLISMO provides comprehensive technologies for developing such as system.

The development of such a DSS may bring many bene<sup>fi</sup>ts towards achievements of some long-term goals including: minimizing the empty trips, oil consumption and pollution by sharing goods transport demands among vehicles; easing the process of applying advanced information technologies to logistics; developing added-value services based on the data accumulated by the DSS; facilitating the communication and control of vehicles and customers for security and ef<sup>fi</sup>ciency purposes.

As for future scope of this research, the proposed optimization models do not consider bene<sup>fi</sup>t allocation between the DSS for PLISMO and vehicle owners. The bene<sup>fi</sup>t allocation mechanism is important and suf<sup>fi</sup>ciently sensitive to canvass vehicles and orders for the DSS for PLISMO. Second, for solving the trust problem among vehicle drivers, customers and the DSS, rational mechanisms for punishment should be designed. Third, models in this work do not consider uncertainties and disruption recovery strategies. These features will generate many research topics. Our hope is that governments and industries pay attention to the ELR problem and to verify that the DSS for PLISMO is a

Please cite this article as: Z.-H. Hu, Z.-H. Sheng, A decision support system for public logistics information service management and optimization, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.12.001

practical solution of reducing ELR. Moreover, we appeal academics, device vendors, information service providers, logistics service providers, and other practitioners to focus on developing new ideas and practical DSSs for reducing ELR. These future research directions will have the potential to lead to considerable theoretical and practical advancements in the <sup>fi</sup>elds of dynamic routing, transportation and logistics optimization.

## Acknowledgment

The authors are grateful to the constructive and helpful comments of the anonymous referees. This study is partially supported by the National Nature Science of China (71101088, 71171129, 71390521), the China Postdoctoral Science Foundation (2011M500077, 2012T50442), the Science Foundation of Ministry of Education of China and Shanghai (10YJC630087, 20113121120002, 20123121110004, 14YZ100), and the Science and Technology Commission of Shanghai (12ZR1412800, 11510501900, 12510501600).

## Appendix A. Algorithms

## Algorithm 1. Construction of graph model from map

STEP 1 Merge layers into a single layer of the used digital map.

STEP 2 Cut intersected arcs of a new layer to make segments that are connected.

STEP 3 Verify and adjust the topology via a GIS editing tool.

STEP 4 Extract the arcs from segments of the road network, and save the arcs to A.

STEP 5 Generate the nodes from adjacent arcs; save the nodes to N; and generate X(n) and Y(n) for all nodes n ∈ N.

STEP 6 Compute the two endpoints and travel time according to the speed for each road segment.

determines which will be the <sup>fi</sup>rst to be delivered. The order is selected by the following rule: if $T S L _ { o a } + T S U _ { o a } \leq$ $T S L _ { o b } + T S U _ { o b }$ then oa ≺ ob. That is, if the order has the minimum time of the time-window at the origin point (by comparing the middle points of two time-windows), this order will be delivered <sup>fi</sup>rst. In the following steps, oa presents the <sup>fi</sup>rst order to be delivered.

STEP 4 Endpoint decision: the two endpoints of the new order are determined as follows: the origin point is $N S ( o c ) = N S ( o a ) ;$ and the destination point is $N E ( o c ) = N E ( o b )$

STEP 5 Time-window decision: the origin and destination timewindows of the new order are determined as follows: at the origin, $T S ( o c ) = T S ( o a )$ ; at the destination, $T E ( o c ) =$ TE(ob).

STEP 6 Order time decision: the time of a new order is the sum of time of the two orders, and travel time between the destination node of the <sup>fi</sup>rst order and the origin node of the second order: T(oc) = T(oa) + T(ob) + SPT(G(oa), G(ob)).

## Algorithm 4. Solution generation

Input: the set of orders (OT); the matrix of merged distances (DTM); and the number of pairs of merged orders (I).

STEP 7 Order replacement: use oc to replace the two orders: oa and ob.

Processes:

Output: set of merged orders (OT).

STEP 1 Choose a pair of orders randomly according to the matrix DTM. STEP 2 Merge orders: invoke Algorithm 3 to generate an order oc from oa and ob.

STEP 3 Replace orders: use oc to replace oa and ob in OT.

STEP 1 Order clustering and solution generation: generate the solution by merging orders by clustering techniques (O → OT), and update the origin, destination, list of passing nodes, and order processing time.

## Algorithm 2. Stowage

STEP 4 If the replaced pairs are less than I, GO TO STEP 1; otherwise, return OT.

Input: status of vehicles, orders and a logistics network.

STEP 2 Computation of the matching matrix: compute the matching matrix (VNOM) and distance matrix (VNOD) between vehicles (V) and new orders (ON), and calculate the time that is added for matching and the time-window avoidance degree.

Output: A stowage plan formed as Eqs. (2)–(4).

STEP 3 Stowage plan: set the model to produce the optimal stowage plan that assigns orders to vehicles.

Processes:

STEP 4 Termination: if the termination criteria are satis<sup>fi</sup>ed, output the stowage plan; otherwise, GO TO STEP 1.

## Algorithm 3. Merge two orders

Input: two orders, oa ∈ OT and ob ∈ OT; a logistics network.

Output: merged order oc ∈ OT.

Processes:

STEP 1 Compatibility check: generate the merging solution of orders by clustering techniques; if MGG(G(oa), G(ob)) = 1 is not satis-<sup>fi</sup>ed, set oc = Φ and return.

STEP 2 Property merging: merge the properties by $G P _ { G ( o c ) } =$ $M E G ( G P _ { G ( o a ) } , G P _ { G ( o b ) } )$

STEP 3 Decision on delivery order: for oa and ob, this process

## References

[1] S. Hang, On the taxi intelligent call system based on android platform, Journal of Theoretical and Applied Information Technology 50 (3) (2013) 704–708

[2] A. Taniguchi, S. Fujii, T. Azami, H. Ishida, Persuasive communication aimed at public transportation-oriented residential choice and the promotion of public transport, Transportation (2013) 1–15.

[3] M.M. Rahman, S.C. Wirasinghe, L. Kattan, Users' views on current and future real-time bus information systems, Journal of Advanced Transportation 47 (3) (2013) 336–354.

[4] M. Mesbah, G. Currie, C. Lennon, T. Northcott, Spatial and temporal visualization of transit operations performance data at a network level, Journal of Transport Geography 25 (2012)15-26

[5] L. Tang, P.V. Thakuriah, Ridership effects of real-time bus information system: a case study in the City of Chicago, Transportation Research Part C 22 (2012) 146–161.

[6] B. De Borger, M. Fosgerau, Information provision by regulated public transport companies, Transportation Research Part B 46 (4) (2012) 492–510.

[7] Y.H. Cheng, Evaluating web site service quality in public transport: evidence from Taiwan High Speed Rail, Transportation Research Part C 19 (6) (2011) 957–974

[8] S. Farag, G. Lyons, Explaining public transport information use when a car is available: attitude theory empirically investigated, Transportation 37 (6) (2010) 897–913.

[9] A. Tibaut, B. Kaučič, D. Rebolj, A standardised approach for sustainable interoperability between public transport passenger information systems, Computers in Industry 63 (8) (2012) 788–798.

[10] G. Jakubauskas, Research on application of intelligent transport systems in public transport Transport 25 (1) (2010) 107–109

[11] T.L. Lei, R.L. Church, Mapping transit-based access: Integrating GIS, routes and schedules, International Journal of Geographical Information Science 24 (2) (2010) 283–304.

[12] G.D. Lyons, Towards integrated traveller information, Transport Reviews 21 (2) (2001) 217-235

[13] Y. Amsler, Integrated ticketing for air and rail transport how to coordinate with urban public transport? Public Transport International 58 (4) (2009) 50–51.

[14] J. Lee, N. Bharosa, J. Yang, M. Janssen, H.R. Rao, Contracting cleaning services in a European public underground transportation company with the aid of a DSS, Decision Support Systems 43 (4) (2007) 1485–1498

[15] J. Muntermann, Towards ubiquitous information supply for individual investors: a decision support system design Decision Support Systems 47 (2) (2009) 82–92

Please cite this article as: Z.-H. Hu, Z.-H. Sheng, A decision support system for public logistics information service management and optimization, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.12.001

[16] K.-h. Lai, C.W.Y. Wong, T.C.E. Cheng, Bundling digitized logistics activities and its performance implications, Industrial Marketing Management 39 (2) (2010) 273–286.

[17] I. Petrakis, C. Hass, M. Bichler, On the impact of real-time information on <sup>fi</sup>eld service scheduling, Decision Support Systems 53 (2) (2012) 282–293.

[18] J. Lee, N. Bharosa, J. Yang, M. Janssen, H.R. Rao, Group value and intention to use—a study of multi-agency disaster management information systems for public safety, Decision Support Systems 50 (2) (2011) 404–414.

[19] B. Fleischmann, S. Gnutzmann, E. Sandvoß, Dynamic vehicle routing based on online traf<sup>fi</sup>c information, Transportation Science 38 (4) (2004) 420–433.

[20] M.K. Ardakani, L. Sun, Decremental algorithm for adaptive routing incorporating traveler information, Computers and Operations Research 39 (12) (2012) 3012–3020.

[21] K. Boriboonsomsin, M.J. Barth, W. Zhu, A. Vu, Eco-routing navigation system based on multisource historical and real-time traffic information JEEE Transactions on Intelligent Transportation Systems 13 (4) (2012) 1694–1704.

[22] J.E. Mendoza, A.L. Medaglia, N. Velasco, An evolutionary-based decision support system for vehicle routing: the case of a public utility, Decision Support Systems 46 (3) (2009) 730–742.

[23] Y. Suzuki, A decision support system of vehicle routing and refueling for motor carriers with time-sensitive demands, Decision Support Systems 54 (1) (2012) 758–767.

[24] V. Pillac, C. Guéret, A.L. Medaglia, An event-driven optimization framework for dynamic vehicle routing, Decision Support Systems 54 (1) (2012) 414–423.

[25] K. Behrens, P.M. Picard, Transportation, freight rates, and economic geography, Journal of International Economics 85 (2) (2011) 280–291.

[26] J. Yu, Y. Dong, Maximizing pro<sup>fi</sup>t for vehicle routing under time and weight constraints, International Journal of Production Economics 145 (2) (2013) 573–583.

[27] M.E. Johnson, Modelling empty vehicle traf<sup>fi</sup>c in AGVS design, International Journal of Production Research 39 (12) (2001) 2615–2633.

[28] J. Holguín-Veras, E. Thorson, Modeling commercial vehicle empty trips with a <sup>fi</sup>rst order trip chain model, Transportation Research Part B 37 (2) (2003) 129–148.

[29] V. Gintner, N. Kliewer, L. Suhl, Solving large multiple-depot multiple-vehicle-type bus scheduling problems in practice, OR Spectrum 27 (4) (2005) 507–523.

[30] A.C. McKinnon, Y. Ge, The potential for reducing empty running by trucks: a retrospective analysis, International Journal of Physical Distribution and Logistics Management 36 (5) (2006) 391–410.

[31] S. Bock, Real-time control of freight forwarder transportation networks by integrating multimodal transport chains, European Journal of Operational Research 200 (3) (2010) 733–746.

[32] A. Asef-Vaziri, M. Kazemi, K. Eshghi, M. Lahmar, An ant colony system for enhanced loop-based aisle-network design, European Journal of Operational Research 207 (1) (2010) 110–120.

[33] L. Chen, A. Langevin, Z. Lu, Integrated scheduling of crane handling and truck transportation in a maritime container terminal, European Journal of Operational Research 225 (1) (2013) 142–152.

[34] S. Islam, T. Olsen, M.D. Ahmed, Reengineering the seaport container truck hauling process: reducing empty slot trips for transport capacity improvement, Business Process Management Journal 19 (5) (2013) 752–782.

[35] J.D. Hunt, K.J. Stefan, Tour-based microsimulation of urban commercial movements, Transportation Research Part B 41 (9) (2007) 981–1013.

[36] A.M.D. Valle, T.A.D. Queiroz, F.K. Miyazawa, E.C. Xavier, Heuristics for twodimensional knapsack and cutting stock problems with items of irregular shape, Expert Systems with Applications 39 (16) (2012) 12589–12598.

[37] C. Duhamel, P. Lacomme, A. Quilliot, H. Toussaint, A multi-start evolutionary local search for the two-dimensional loading capacitated vehicle routing problem, Computers and Operations Research 38 (3) (2011) 617–640.

[38] L. Muyldermans, G. Pang, On the bene<sup>fi</sup>ts of co-collection: experiments with a multi-compartment vehicle routing algorithm, European Journal of Operational Research 206 (1) (2010) 93–103.

[39] S.C.H. Leung, X. Zhou, D. Zhang, J. Zheng, Extended guided tabu search and a new packing algorithm for the two-dimensional loading vehicle routing problem, Computers and Operations Research 38 (1) (2011) 205–215.

[40] A. Bortfeldt, A hybrid algorithm for the capacitated vehicle routing problem with three-dimensional loading constraints, Computers and Operations Research 39 (9) (2012) 2248–2257.

Zhi-Hua Hu, is an associate professor of Logistics Research Center, Shanghai Maritime University. He attained his PhD at Donghua University in 2009. His research directions include: logistics operational optimization, computational intelligence and algorithms.

Zhao-Han Sheng, is a professor of School of Management and Engineering, Nanjing University at China. His research directions include: supply chain management and complex system.
