---
otero_id: 15464
otero_key: "MC2NFGS8"
title: "Cooperative planning in express carrier networks — An empirical study on the effectiveness of a real-time Decision Support System"
authors: "Sascha Dahl; Ulrich Derigs"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2011.02.018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cooperative planning in express carrier networks — An empirical study on the effectiveness of a real-time Decision Support System

Sascha Dahl, Ulrich Derigs ⁎

Department of Information Systems and Operations Research, Universität zu Köln, Albertus-Magnus-Platz, D 50969 Köln, Germany

## a r t i c l e i n f o

Article history: Received 6 August 2010 Received in revised form 15 December 2010 Accepted 27 February 2011 Available online 16 March 2011

Keywords: Cooperative planning Carrier networks Dynamic vehicle routing problem Simulation

## a b s t r a c t

For small transportation <sup>fi</sup>rms cooperation in a carrier network is a proper mean to overcome the inef<sup>fi</sup>ciencies from deadheading. To be successful, such a network has to secure two different but equally important aspects: the partners have to be aware of speci<sup>fi</sup>c consolidation potentials through order exchange which is an optimization and communication problem, and, the partners have to experience incentives to contribute actively to the network which is the problem of <sup>fi</sup>nding a fair cost/pro<sup>fi</sup>t allocation schema for order exchanges. In this paper we discuss the experience with the development of a Decision Support System for a speci<sup>fi</sup>c express carrier network. We illustrate how the consolidation potentials in such a network with autonomously planning carriers can be exploited and cost effectiveness can be improved substantially through the use of a suitable distributed Decision Support System if the two success factors awareness and fairness are addressed properly.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

During the last years, transportation <sup>fi</sup>rms are faced with increasing cost pressure and revenue erosion at the same time. Large transportation companies are able to realize a high utilization of their vehicles and acceptable operational cost by consolidating and combining orders to ef<sup>fi</sup>cient roundtrips. Small carriers serving ad-hoc one-way shipping orders only are faced with the problem of low volume of shipments with less than truckload trips as well as dead head trips due to an imbalance among locations. This leads to cost ineffective transportation plans and/ or may result in non-competitive prices.

Such small-sized companies may compensate their competitive disadvantage by allying with partners to a cooperation network to establish a more pro<sup>fi</sup>table portfolio of orders. In such a network each partner plans his orders and his vehicle <sup>fl</sup>eet independently with the option to exchange orders with partners. Partners charge their own customers based on a speci<sup>fi</sup>c price function. The carrier operating an order for a partner receives a monetary compensation, which has been speci<sup>fi</sup>ed in a generally agreed upon compensation schema.

For such a network to be successful and sustainable there are a number of critical factors: on the strategical level the choice of the right set of partners yielding enough consolidation potential as well as mutual trust is a cardinal point. On the operational level awareness is essential, i.e. existing potentials have to be detected and communicated, a task which calls for the establishment of a proper information and communication system supporting cooperative planning. Another success factor is the establishment of a compensation schema which puts incentives to both partners involved in exchanging orders and which is considered to be fair by all network partners.

The issue of reducing transportation cost by collaboration and forming alliances has been investigated in the scienti<sup>fi</sup>c literature with respect to different aspects like different transportation markets or modes i.e. airfreight [7], shipping [1], trucking [8], intermodal freight transportation [16], supply chain management [18] as well as decision level, i.e. from evaluating strategic aspects in alliance formation [2] to pricing/revenue management and allocation of cost bene<sup>fi</sup>ts [4,10–12].

Most developments concern design questions and propose models which are based on theoretical foundations stemming from game theory, combinatorial auctions and network <sup>fl</sup>ow. Refs. [10,13] present approaches for a problem where intra-enterprise in and outsourcing decisions on bundles of logistic services i.e. bundles of transportation requests from customers in a pro<sup>fi</sup>t center structured forwarding company have to be made. In both approaches the cost difference through exchanging requests is evaluated for numerous bundles of requests. Then the optimal distribution of the bundles among the pro<sup>fi</sup>t centers is determined via a combinatorial auction. Both approaches propose mechanisms for sharing the resulting pro<sup>fi</sup>t increase among the centers.

Our development was driven by the necessity to control cost effective transportation in an established collaborative network of independent express couriers on the operational level where decisions on the exchange of orders have to be made instantaneously. In our problem environment the situation is highly dynamic such that at no point in time planning of a <sup>fi</sup>xed set of orders/requests is possible as it is assumed in Refs. [10,12]. Hence the focus was on implementing rational decision models which allow on-line algorithms within an effective Decision Support System.

In this paper we describe our experience with the development and maintenance of pool.tour, a distributed real-time internet-based collaborative Decision Support System (DSS) for a large express courier network, and we analyze the impact of this system on the success factors mentioned above. In a <sup>fi</sup>rst development we implemented a system proposing order exchanges automatically which are pro<sup>fi</sup>table for both partners involved based on the established compensation schema. This technologically highly demanding system has been in use for about 2 years. Yet, the improvement over the formerly used approach where dispatchers had to assume potentials from their experience and to communicate proposals to partners over the phone was much lower than expected. An analysis of the business i.e. the order pool and the proposals generated showed that the system could only rarely <sup>fi</sup>nd consolidations i.e. insertions of orders in existing trips which were pro<sup>fi</sup>table for the acquiring as well as the operating partner but was only able to propose exchanges which result in separate trips. This unsatisfactory behavior motivated us to analyze the contractual compensation schema, to propose an alternative schema and to compare the result with the existing schema. For that purpose we performed a simulation study on the logged order pool over a signi<sup>fi</sup>cant duration of several weeks. Our analysis showed that the rather poor performance could be clearly attributed to the compensation schema. Using a rather straightforward cost based compensation schema within the model base of pool.tour network wide transportation cost could be decreased signi<sup>fi</sup>cantly, even down to the level reachable by centralized planning. Also the distribution of the pro<sup>fi</sup>t showed to be much fairer.

This paper is structured as follows. In Section 2 we give a short description of the transportation market and the speci<sup>fi</sup>c carrier network underlying our development and study, in the following referred to as the Cooperative Logistic Network (CLN) or simply network for short. In Section 3 we introduce the planning problem and the established compensation schema. Then, in Section 4, we shortly describe our Decision Support System pool.tour. In Section 5 we describe the motivation and the design of our simulation study for evaluating the effectiveness of pool.tour and in Section 6 we report the central results of this experience.

## 2. The cooperative logistic network

In 2001 the market value of the courier/express/parcel segment in Europe was about 36 billion Euro, and 30% of this volume was realized in Germany. In Germany close to 10,000 courier <sup>fi</sup>rms are specialized on this kind of general freight transport, yet, this number contains many one-person businesses which operate as subcontractors for larger companies only. CLN was founded in 2001 by logistics professionals for logistics professionals to unite small and medium-sized courier companies under a strong brand. It was created by a consortium of independent courier companies with a more strategically oriented organization in mind than traditional partner-based systems. All twelve founding shareholders were professionals in international procurement logistics, i.e. all partner companies had long term expertise in national and international deliveries and offered procurement logistics, less than truckloads (LTL) and complete truckloads, transportation of dangerous goods and customs service. With the Europe-wide business partners CLN is able to offer pickup and delivery of shipments anywhere in Europe, with availability 24 h a day, 365 days a year and guaranteed pickup anywhere in Germany within 60 min.

The purpose of CLN – as the purpose of every cooperation of freight forwarding companies – is to realize a pro<sup>fi</sup>table equilibrium between customer demand and available transport resources by interchanging customer requests among partners. Being a member of CLN allows the forwarding company to choose between two modes of ful<sup>fi</sup>llment for each task: To use own vehicles (self-ful<sup>fi</sup>llment) or to use a partner carrier who will then receive a compensation for the request ful<sup>fi</sup>llment.

The critical success factor for a freighter is the percentage of deadheads. According to experience this percentage had been up to 40% to 45% for the individual carriers before the cooperation, a number resulting from the high spatial diversity of the single requests and the inability to consolidate within the available time-frame, yet, a number much too high to allow competitive prices and suf<sup>fi</sup>cient pro<sup>fi</sup>t. A rough analysis of the business within the <sup>fi</sup>rst year of CLN's operation where cost reducing interchanges had been realized between the dispatchers occasionally via telephone conferencing had shown only a slight reduction of deadheads. Yet, expectation was that even with the full thrust of the cooperation, its mutual growth and coordination potential, the bottom line of deadheads would always remain around 30% due to the extreme short reaction time. All partners were aware of the fact that the two major make and break questions on the cooperation were constituted by the potential to bring the key performance indicator on deadheads closer to this bottom line and the discussion on how to split earnings among partners in a fair manner. This judgement on the key issues has led to the development of pool.tour, our DSS which supports cooperative planning as well as communication in this highly time-sensitive environment.

## 3. Modeling the planning situation

Let P be the set of partners in the network. Each partner $p { \in } \mathrm { P }$ is located at a speci<sup>fi</sup>c depot dep and operates a set of vehicles $V _ { p } .$ Each vehicle v is assigned to a vehicle class. Let VC be the set of vehicle classes and vc the vehicle class of vehicle v. All vehicles in a vehicle class ${ \mathsf { v c } } \in { \mathsf { V C } }$ share common physical and technical transportation capabilities as for instance capacity $\scriptstyle Q _ { \mathrm { v c } } ,$ average speed, cost rates for distance and time etc. The set of vehicle classes is assumed to be partially ordered with the semantic that a vehicle of a ‘larger’ class can always transport orders which require a ‘smaller’ vehicle class. Each partner $p { \in } P$ has acquired a set $O _ { p }$ of orders. Here, each order o is de<sup>fi</sup>ned by its pickup location $p _ { o } ,$ its delivery location $d _ { o } ,$ its capacity requirement ${ \mathrm { C a p } } _ { o }$ and a time window $[ e _ { o } , \ l _ { o } ]$ , which speci<sup>fi</sup>es the earliest time for pickup and latest time for delivery, respectively. From the capacity requirement one can determine $\mathtt { V C } _ { o }$ the minimum required vehicle class for the order. For each vehicle class ${ \mathsf { v c } } \in { \mathsf { V C } }$ two rates apply: $\mathsf { p r i c e } _ { \mathrm { v c } }$ the transportation price per km for the customer and $\mathrm { c o m p C o s t } _ { \mathrm { v c } }$ an internal cost rate per km used for compensation. For two locations x and y let $l ( x , y )$ denote their distance. Then the revenue $\operatorname { r e v } ( p , o )$ , which a partner p obtains from his customer after serving its order o, is calculated as follows:

$$
\operatorname{rev} (p, o) = \operatorname{price} _ {\mathrm{vc} _ {o}} \left[ \max \left(0; l \left(\operatorname{dep} _ {p}, p _ {o}\right) - l ^ {\text { fix }}\right) + l \left(p _ {o}, d _ {o}\right) \right].\tag{1}
$$

Thus, for picking up the order (pre haul leg) only the distance exceeding $l ^ { \mathrm { f i x } }$ is charged. Note, that each vehicle can transport more than one order at a time, as long as the total capacity is not exceeded, and that it is the task of the dispatching systems of the partners to combine orders to tours.

Let us <sup>fi</sup>rst assume the non-cooperative case, i.e. the special case of one partner p only. This problem of combining orders to tours is coined as Pickup and Delivery Vehicle Routing Problem with Time Windows (PDVRPTW) and well studied in the Operations Research literature. As a so-called rich variant of the classical Vehicle Routing Problem it is NP-complete and thus only heuristic methods are applicable for solving problem instances of practical size. Ef<sup>fi</sup>cient heuristic algorithms have been proposed by Ref. [14] and Ref. [5]. Now, a solution to a vehicle routing problem, also called a schedule, consists of a partition of the orders into clusters/tours which are assigned to the vehicles and an ordering/routing of the orders within a cluster. Here, a feasible schedule for the PDVRPTW has to obey the following properties:

• Each order $o \in { \cal O } _ { p }$ is assigned to exactly one vehicle/tour $\nu \in V _ { p } .$

• For each order $o \in { \cal O } _ { p }$ location $p _ { o }$ is visited before $d _ { o } .$

• Each order $o \in { \cal O } _ { p }$ is picked-up not earlier than $e _ { o } .$

• Each order $o \in { \cal O } _ { p }$ is delivered not later than $l _ { o } .$

• For each vehicle the load of the vehicle must not exceed its capacity $Q _ { \mathrm { v c } _ { \nu } }$ at any time on the route.

Note that due to the relatively short lead times the number of orders transported simultaneously on a vehicle is rather small and thus vehicle capacity is not a critical constraint for building feasible tours.

Under this static view, one assumes that a vehicle will always return to its depot after serving all orders of its tour. Yet, in the express carrier environment, due to the highly dynamic business all plans have to be adapted constantly and a vehicle may receive new orders on tour. Thus the problem to be solved is a Dynamic PDVRPTW (DPDVRPTW).

Ref. [3] presents an overview on this class of dynamic vehicle routing problems distinguishing different sub-classes. A basic and commonly used solution strategy is to adapt an algorithm that solves the static version of the problem. In one approach the static problem is solved each time a new information, i.e. an order, is revealed. In a second approach the current solution is only updated with heuristic methods. In our application we solve the DPDVRPTW modifying the heuristic PDVRPTW-solver called ROUTER (see Ref. [5]). ROUTER is a two-phase heuristic, which <sup>fi</sup>rst constructs good feasible solutions using a costbased cheapest insertion strategy and then applies a local search based metaheuristic for improvement in the second phase. In contrast to the assumption in Ref. [3] that generally, when time windows are present in a pickup and delivery vehicle routing problem, they are not tight, the extremely short lead time is a characteristic for our business. Therefore the application of the rather time-consuming improvement phase of ROUTER is discarded when solving the DPDVRPTW instances since its application would be unrealistic for practical use in a real-time environment with such narrow lead times. We have implemented the rolling horizon paradigm, i.e. at each time an order data change occurs a (static) instance is solved with all orders <sup>fi</sup>xed which are already in execution. Note that our problem cannot be treated as a stochastic VRP since no information on future request is known.

Now assume the collaborative case at CLN. Here, a carrier p has two options: to serve an order o with his own <sup>fl</sup>eet or to have it served by one of the partners. In the <sup>fi</sup>rst case, contribution to pro<sup>fi</sup>t $\mathrm { c t p } ( p , o )$ is calculated as usual, reducing revenue by the marginal imputed cost:

$$
\operatorname{ctp} (p, o) = \operatorname{rev} (p, o) - \Delta \operatorname{impCost} (p, o)\tag{2}
$$

where imputed cost is calculated based on the distance a vehicle has to drive and the time a vehicle spends for driving and/or waiting. Both terms are multiplied by the vehicle class speci<sup>fi</sup>c cost rates for distance and time.

In the second case, i.e. if one of the partners, say q, serves the order, the compensation comp $\cdot \mathrm { P } ( q , o )$ is determined according to a contractually agreed upon schema CS-P which distinguishes two cases:If the order is served by a dedicated tour, the calculation is similar to the revenue calculation above, with the only difference that twice the compensation cost rate is applied:

$$
\operatorname{comp} _ {\mathrm{CS} - \mathrm{P}} (q, o) = 2 \cdot \operatorname{compCost} _ {\mathrm{vc} _ {o}} \left[ \max \left(0; l \left(\operatorname{dep} _ {q}, p _ {o}\right) - l ^ {\text { fix }}\right) + l \left(p _ {o}, d _ {o}\right) \right].\tag{3}
$$

If the order is inserted into an already existing tour, and thus is combined ef<sup>fi</sup>ciently with other orders, the load distance $l ( p _ { o } , d _ { o } )$ plus the marginal distance caused by the service of o applies. This more complicated calculation is illustrated in Fig. 1 for the case that order o is combined with two other orders r and $s ,$ respectively. Here bold arrows indicate the trips with orders or load which are performed by the vehicle, while dashed arrows symbolize trips without load, i.e. deadheads for instance.

![](/api/attachments/MC2NFGS8/fulltext/images/8f336f2d265d88d0baee4609eb71d639a2eebda54b4aafa8394335b7b6d1180a.jpg)  
Fig. 1. Compensation with CS-P in case of combined order execution.

$$
\begin{array}{c} \operatorname{comp} _ {\mathrm{CS-P}} (q, o) = \operatorname{compCost} _ {\mathrm{vc} _ {o}} \left[ l \left(p _ {o}, d _ {o}\right) + l \left(p _ {r}, p _ {o}\right) + l \left(p _ {o}, d _ {r}\right) \right. \\ \left. - l \left(p _ {r}, d _ {r}\right) + l \left(p _ {s}, d _ {o}\right) + l \left(d _ {o}, d _ {s}\right) - l \left(p _ {s}, d _ {s}\right) \right] \end{array}\tag{4}
$$

Note, that in both cases the cost rate of the required vehicle class is applied, not the rate of the vehicle actually serving the order.

At <sup>fi</sup>rst sight the problem at CLN is similar to the problem domain treated in Refs. [10,12]. Yet, the approaches proposed are not applicable here because of two reasons. First, the dynamic occurrence of requests with extremely narrow time windows for pick up does not lead to a point in time with a real planning situation where for a <sup>fi</sup>xed set of orders an optimal exchange of bundles of orders could determined. Secondly, the established cooperation mechanism is to exchange single orders after bilateral negotiation. Thus the autonomy of the partners does not allow a central authority which is able and legitimate to reallocate orders.

## 4. Pool.tour — a Decision Support System

In general a Decision Support System (DSS) is an interactive computerbased system which supports decision makers in solving semi-structured problems [17]. According to the classical concept a DSS consists of three modules: database, modelbase and dialog component [17]. Yet, to be able to support planning by the dispatchers as described above this architecture has to be enhanced since several aspects are not addressed by the basic DSS-concept which is focusing on supporting a single decision maker only. First, a number of decision makers coming from different partner <sup>fi</sup>rms and thus following different individual objectives have to work together in a cooperative manner. A DSS for such a scenario is called a Group DSS [15]. In our planning environment support of communication between dispatchers is an essential requirement. Also, the problem requires to control the operation of many mobile units (vehicles) which themselves send messages on their geographical position via <sup>fl</sup>eet telematics. Ref. [15] classi<sup>fi</sup>es a DSS with such a functionality as Communications-Driven DSS. The dynamic of the business and the extremely short lead time between order entry and pickup time require the installation of a Real-Time DSS which is capable to react to the changing environment instantly. Since the users of the DSS are geographically spread over Europe a Distributed DSS [9] has to be developed.

Based on these requirements we have designed an interactive concept where the DSS integrates the decentralized databases of the partners' dispatching systems and uses a simple but fast and powerful on-line heuristic which is based on the current information on orders, planned tours and vehicle positions. The heuristic permanently generates proposals for inserting new orders into tours which are then communicated to the dispatchers in a pro-active manner. This concept is realized with an internet-based client–server-architecture where data, application logic and generation of the user interface are centralized while presentation and interaction with the dispatchers is performed through a web interface on the dispatchers' clients. Ref. [15] has characterized such a DSS as Web-Based DSS.

Fig. 2 shows the architecture of our DSS. The central DSS-database stores and manages all relevant data from orders, vehicles and vehicle routings from all partners as well as the current vehicle positions. This data is imported automatically and in real-time from the local dispatching systems of the partners as well as the database of the <sup>fl</sup>eet telematics provider using appropriate interfaces. The web interface allows the partners to search and <sup>fi</sup>lter the data with respect to different criteria. From this exposition the planning paradigm becomes apparent: decentralized planning of orders at each partner site with a central supporting system, the so-called proposal generator which searches and proposes options of pro<sup>fi</sup>table exchanges in real-time based on data from the individual dispatching systems and <sup>fl</sup>eet telematics.

The proposal generator is the core component ensuring awareness of consolidation potentials. It is activated automatically and in real-time in case a new order is inserted into the database or an order data is changed. Moreover the proposal generator can be called manually by the partners for every own order. After insertion of an order, ō say, in a <sup>fi</sup>rst step, the generator uses the cheapest insertion logic from ROUTER [5] to check all feasible positions for pickup and delivery in routings of vehicles of that partner, p say, who according to the current situation has to ful<sup>fi</sup>ll the order. In case of a new order this is the partner who has acquired the order and in the case of an order change this is the acquiring partner or the partner who accepted to overtake the order following an earlier proposal. Analogously, all feasible positions for pickup and delivery in vehicle routings of partners are identi<sup>fi</sup>ed and the position which results in the lowest compensation cost is selected. In these calculations the currently available information on vehicle positions is used.

Thus a proposal for an order exchange is generated if

$$
\operatorname{rev} (\overline {{p}}, \overline {{o}}) - \operatorname{comp} _ {\mathrm{CS} - \mathrm{P}} (v _ {i}, \overline {{o}}) > \operatorname{ctp} (v, \overline {{o}})\tag{5}
$$

which is equivalent to

$$
\operatorname{comp} _ {\mathrm{CS} - \mathrm{P}} (v _ {i}, \bar {o}) <   \Delta \text { impCost } (v, \bar {o})\tag{6}
$$

where v is the vehicle of partner p and v is the vehicle of the partner p for which the cheapest insert position was found. Now, the proposal is acceptable for the network partner p if

$$
\operatorname{comp} _ {\mathrm{CS} - \mathrm{P}} (p _ {i}, \overline {{o}}) > \Delta \operatorname{impCost} (p _ {i}, \overline {{o}})\tag{7}
$$

i.e. if the partner takes an advantage from serving o. The proposal together with the compensation amount to be paid is then communicated to partners p and p<sub>i</sub> via e-mail. Note that through this service the DSS also reduces communication effort and cost signi<sup>fi</sup>cantly.

## 5. Design of a simulation study for evaluating the effectiveness of pool.tour

The system described in Section 4 has been implemented in CLN and has been in use for about 2 years, i.e. during their daily planning the dispatchers received proposals for order exchanges. Yet, the experience with the use of the system was not satisfactory, i.e. the reduction in deadheads and the increase in contribution to pro<sup>fi</sup>t that materialized were far below expectation. When monitoring the system we could observe that the system was constantly detecting a signi<sup>fi</sup>cant number of proposals. Yet, a closer analysis revealed three problems: only a small fraction of the proposals concerned consolidations, i.e. the insertion of orders in existing tours, the majority of the proposals were not implemented by the dispatchers, and, a large number of obviously promising exchanges were not proposed.

According to the comment of the partners the reason for the second failure is the fact that for exchanges which would result in a separate deadhead tour for the receiving partner the compensation to be paid by the acquiring partner is too high, i.e. all partners are aware of carriers outside CLN who demand less compensation fee for such an order. Now, our hypothesis was that the speci<sup>fi</sup>c compensation schema CS-P which is implemented in CLN and hence in the proposal generator of pool.tour is causing the other de<sup>fi</sup>cits, too. We argued that the compensation schema CS-P disguises apparently costef<sup>fi</sup>cient exchange options by either setting the compensation fee too high for the acquiring partner or too low for the receiving partner. Thus the schema is unfair and hence irrational.

Therefore we decided to propose and evaluate an alternative compensation schema which observes the speci<sup>fi</sup>c situation of the business at all partners explicitly and whose fairness is comprehensible. Of course, such a substantial contractual change cannot be implemented without prior proof of concept, i.e. evidence of improvement. Therefore we decided to perform an extensive simulation study. The purpose of the study was not only to evaluate an alternative schema but also to analyze to which level the coordination potential is exploited. For that purpose we have simulated different organizational settings and scenarios. In all settings and scenarios we assume that the proposals generated by pool.tour are accepted and implemented by the partners.

![](/api/attachments/MC2NFGS8/fulltext/images/a221f10a7868e53e7dd83425559cf8c5da7d357509568d3b7e3f35f591271117.jpg)  
Fig. 2. DSS architecture.

## 5.1. Simulation data

For the simulation study we have used real data from our European-wide operating cooperative logistic network CLN consisting of about 50 carriers at the time of the study. We stored all orders over twelve randomly chosen weeks in 2008. By purpose we have chosen a period before the economic crisis with regular demand. At that time the network had a capacity of 8905 vehicles assigned to <sup>fi</sup>ve vehicle classes. This high number of vehicles re<sup>fl</sup>ects the fact that in this courier network each carrier has access to a virtually unlimited number of subcontractors. This carrier and vehicle data has been considered as static, while the order data is highly dynamic. To gather real order data we have timestamped and logged every change of order data for all carriers. Then we have eliminated all data changes re<sup>fl</sup>ecting order exchanges between carriers because such decisions are subjected to the planning approach in the simulation.

## 5.2. Alternative planning scenarios and methods

We have analyzed the impact of alternative organizational settings: the collaborative planning approach supported by our DSS, a non-collaborative planning scenario where each carrier plans and operates his own orders only and a centralized approach imitating the situation that all resources and orders belong to one carrier. The non-collaborative scenario requires to solve a set of Dynamic Pickup and Delivery Vehicle Routing Problems with Time Windows (DPDVRPTW), one for each partner, while the centralized approach requires to solve a single Dynamic Pickup and Delivery Vehicle Routing Problem with Time Windows and Multiple Depots (DPDVRPTWMD) (see Ref. [14]). As already mentioned we have solved the non-collaborative scenario problems modifying the heuristic PDVRPTW-solver ROUTER (see Ref. [5]). In our work, we found that the real-world problem instances resulting from the centralized planning approach can be solved by this modi<sup>fi</sup>cation of the ROUTER-insertion heuristic considering all orders already planned to be <sup>fi</sup>xed and continuously evaluating the cheapest insertion position for each incoming or updated order. This approach mimics a realistic planning procedure in the dispatch and thus the solutions can be seen as the results achievable by a realistic practical solution method respecting the high dynamic for the centralized organizational setting. In that sense they build the reference for our simulation results. Based on these solutions as bottom line, plans resulting from DSS-simulation can be evaluated to examine the effects on total cost, distribution of orders, etc.

## 5.3. Alternative compensation schema

The compensation schema determines whether a speci<sup>fi</sup>c collab oration through an order exchange is of advantage for both partners involved. Hence, the design of the compensation schema with respect to incentiveness and fairness is a key factor for the overall performance of the network. An analysis of the effect of alternative compensation schemata and a comparison with alternative planning approaches as reference will certainly help to improve the potentials of the collaboration and to establish mutual trust. While in Ref. [12] pro<sup>fi</sup>t is shared based on the exchange of single bundles, Ref. [13] uses the Shapley value as a mechanism to share the dividend of cooperation among the participating couriers. Ref. [10] proposes a <sup>fl</sup>exible mechanism to distribute total cost savings obtained from the exchange of bundles after solving the combinatorial auction problem. Here the trade-off between cost saving through outsourcing and cost increase through insourcing can be in<sup>fl</sup>uenced by adjusting the ratio between in and outsourcing.

Our approach is based on the evaluation of exchanging single requests and here we have analyzed the impact of two different compensation concepts: the one presently used by CLN and implemented in pool.tour (CS-P) and another simple marginal cost-based schema (CS-CB):

$$
\operatorname{comp} _ {C S - C B} (q, o) = \frac {1}{2} [ \Delta \text { impCost } (p, o) + \Delta \text { impCost } (q, o) ]\tag{8}
$$

i.e. we calculate the marginal imputed cost obtained from cheapest insertion of o into the transportation plans of p and q respectively. Schema comp is incentive compatible in the sense that whenever there is the potential for decreasing the total networkwide cost through an exchange then there is also a positive gain from it for each of the involved carriers. Note that schema CS-CB can easily be parameterized to implement alternative distributions of the revenue between the acquiring and operating partner.

## 6. Simulation results

In a <sup>fi</sup>rst scenario (scenario without outsourcing) the simulation and the optimization procedures are based on the assumption that all transport requests must be ful<sup>fi</sup>lled within CLN, i.e. it is not possible to have transportation requests executed by eventually less costly subcontractors from the spot market. Fig. 3 shows the networkwide total imputed cost per week which occurs when simulating the four different settings introduced above: collaborative planning with the compensation schemata CS-P and CS-CB, respectively, as well as isolated planning and centralized planning. Moreover the mean value over all simulation periods is given. Note that we have normalized the results, i.e. all cost values are stated as percentage of the cost arising from the isolated planning setting.

![](/api/attachments/MC2NFGS8/fulltext/images/08b34f011a14768575cb7d9be7f9b1fb90c400a4876bf38222858f13def9b95c.jpg)  
Fig. 3. Relative cost, scenario without outsourcing, 100% = cost with isolated planning.

Collaborative planning with the compensation schema CS-P leads to a mean cost level of 95.77%, i.e. a cost decrease of 4.23% compared to isolated planning. Using the cost-based compensation schema CS-CB cost can be reduced signi<sup>fi</sup>cantly to a cost level of 86.15%, i.e. the cost decrease is 13.85%. Even in the case of centralized planning we can see that with the use of realistic planning methods the additional cost reduction to a level of 85.93% is only marginal, i.e. the maximal cost decrease achievable by cooperating is 14.07%. Note that over the sample data all these values have only small variances and their relative order and difference are stable.

These results are rather signi<sup>fi</sup>cant. They support the estimation and experience of the partners that cooperation with their compensation schema CS-P and traditional manual planning and communication by phone could only reduce cost marginally. They manifest that there is a substantial bottom line of cost resulting from inef<sup>fi</sup>ciencies caused by the imbalance of orders with respect to location and time which cannot be avoided even under centralized cooperative planning. Yet, most important, the results clearly demonstrate that the choice of the compensation schema is crucial for the economical success of the cooperation network. Collaborative planning with the simple, well understandable and easily applicable compensation schema CS-CB leads to a signi<sup>fi</sup>cant decrease of network-wide total cost compared to CS-P. Yet, what is even more important is the result that by simply applying the cost-based compensation schema CS-CB the CLN network can exhaust nearly all cost saving potentials and reach the cost level of centralized planning.

Fig. 4 displays the corresponding values for a second scenario (scenario with outsourcing) where we assume that transportation requests may be executed by subcontractors from the spot market. To allow a comparison of both scenarios all values are again normalized relative to the cost resulting from isolated planning without outsourcing.

As expected, in the outsourcing scenario cost are systematically lower than the respective cost without outsourcing for all settings. Every solution of the scenario without outsourcing remains feasible, yet, the option of outsourcing extends the solution space. For isolated planning as well as collaborative planning with compensation schema CS-P allowing outsourcing reduces cost signi<sup>fi</sup>cantly by 5.8% and 4.6%, respectively. In the settings of collaborative planning with compensation schema CS-CB and centralized planning cost are only slightly reducible through outsourcing, i.e. the reduction is only 0.64% and 0.55%, respectively.

This different behavior of the four settings can be explained as follows: in the <sup>fi</sup>rst setting of isolated planning outsourcing is the only possibility to reduce the number of unpro<sup>fi</sup>table transportation. Now, applying compensation schema CS-P similar reductions which exist within the network remain invisible. In contrast, applying the costbased compensation schema CS-CB such cost savings existing within the network are made explicit and allow the more ef<sup>fi</sup>cient allocation of transport orders within the network to an extent, that the cost levels with and without outsourcing differ only slightly. Thus, when applying CS-CB outsourcing does not pay any more and the network offers to the partners the entire market potential for collaboration. And this is what triggered the motivation and strategy of forming the network.

So far, our simulations have shown that for the network as a whole collaborating using a proper compensation schema like CS-CB pays. Now, a second aspect is the fairness of the compensation schema. This aspect is the focus of the following analysis where we have measured the pro<sup>fi</sup>t gains for the individual network partners resulting from their participation in the network. For that purpose we have calculated for every partner p and for every week an indicator $\Delta \mathrm { g } _ { \overline { { p } } }$ which is a proxy for the gain with respect to contribution to pro<sup>fi</sup>t. Δg measures the difference between $\mathrm { c l P } _ { \overline { { p } } }$ the cost occurring in the isolated planning setting and ${ \mathsf { c C P } } _ { \overline { { p } } }$ the cost occurring in the cooperative planning setting. Now this value is corrected by adding the compensation payments p received from network partners and subtracting the compensation payments of $\overline { { p } }$ to other network partners. These compensation payments are obtained from the results of the simulation, i.e. the cooperation proposals/transactions computed. Let R denote the set of all compensation payments and $r _ { p , q }$ the compensation which partner p has to pay partner q. Then the indicator is calculated as follows:

$$
\Delta g_{\overline{p}} = \operatorname{cIP}_{\overline{p}} - \operatorname{cCP}_{\overline{p}} + \sum_{\substack{r_{q,p}\in R:\\ p = \overline{p},q\neq \overline{p}}}r_{q,p} - \sum_{\substack{r_{p,q}\in R:\\ p = \overline{p},q\neq \overline{p}}}r_{p,q}.\tag{9}
$$

Fig. 5 shows the distribution of the cooperation pro<sup>fi</sup>t among the individual network partners for the scenario without outsourcing. Fig. 5(a) gives the distribution using collaborative planning with the compensation schema CS-P, whereas Fig. 5(b) gives the distribution

![](/api/attachments/MC2NFGS8/fulltext/images/f1920eb5874e4f7dc732b9229ab396a9e746986f87c958781b81d968c417283e.jpg)  
Isolated planning Collaborative planning CS-P Collaborative planning CS-CB Centralized planning

Fig. 4. Relative cost, scenario with outsourcing, 100% = cost with isolated planning in the scenario without outsourcing.

![](/api/attachments/MC2NFGS8/fulltext/images/bf723bbd159dbc1ad25581612cd9c3b64691d82ba5e6e221dabb89170fe24a01.jpg)

![](/api/attachments/MC2NFGS8/fulltext/images/a82b362eb8e0c6070cb1927bb31b5d9dddd558e2a3a1923db2018621045af583.jpg)  
Fig. 5. (a)+(b): Pro<sup>fi</sup>t distribution, collaborative planning without outsourcing, mean value over all simulation periods.

using CS-CB. In the case of CS-P only a rather small number of network partners receive the bulk of the (relatively small) cooperation pro<sup>fi</sup>t. On the other hand, using CS-CB the (relatively larger) pro<sup>fi</sup>t is distributed much more equally and thus more fairly among all network partners: The number of partners which gain a positive pro<sup>fi</sup>t is signi<sup>fi</sup>cantly larger and the pro<sup>fi</sup>t is distributed more evenly. Thus, with respect to the equality principle from the theory of distributive fairness (see Refs. [6,19]) the pro<sup>fi</sup>t allocation resulting from CS-CB is more fair than the one resulting from CS-P. Furthermore, the absolute pro<sup>fi</sup>t each partner receives is larger than in CS-P, since the total amount to divide is larger.

## 7. Conclusion

In this paper we have presented an empirical analysis of the effectiveness of a Collaborative Decision Support System in an express carrier network. Due to the highly time sensitive planning environment supporting awareness of consolidation potentials has been identi<sup>fi</sup>ed as a critical success factor and has led to the development and implementation of pool.tour, a technically complex Decision Support System whose core is a real-time proposal generator. The experience of 2 years of operation and the results of our simulation analysis have demonstrated the dominant importance of the choice of an adequate compensation schema. It is another critical success factor for the cooperation network, for the potential of materializing the overall cost reduction as well as for the fairness of pro<sup>fi</sup>t distribution within the network. Our simulation reveals that with the support of a real-time DSS based on an adequate compensation schema the network is able to work close to the level obtainable by centralized planning. In a sense this is the strongest possible empirical result. Thus, the compensation schema has to be regarded as the primal design parameter of decision support with respect to economic success and stability of the network. It can make or break the network.

## References

[1] R. Agarwal, O. Ergun, L. Houghtalen, O.O. Ozener, Collaboration in cargo transportation, in: A. Chaovalitwongse, F. Roberts (Eds.), Optimization and Logistics Challenges in the Enterprise, Springer, 2006.

[2] J. Antes, U. Derigs, M. Zils, Strategic airline alliances portfolio analysis, Avmark Aviation Economist 16 (1999).

[3] G. Berbeglia, J.F. Cordeaub, G. Laporte, Dynamic pickup and delivery problems, European Journal of Operational Research 202 (2010) 8–15.

[4] A. Boyd, Airline alliances, OR/MS Today 25 (1998) 28–31.

[5] U. Derigs, T. Döhmer, Indirect search for the vehicle routing problem with pickup and delivery and time windows, OR Spectrum 30 (2008) 149–165.

[6] M. Deutsch, Justice and con<sup>fl</sup>ict, in: M. Deutsch, P.T. Coleman, E.C. Marcus (Eds.), The Handbook of Con<sup>fl</sup>ict Resolution: Theory and Practice, Jossey-Bass, San Francisco, 2006, pp. 43–68.

[7] O. Ergun, L. Houghtalen, J. Sokol, Designing mechanisms for the management of carrier alliances, to appear in Transportation Science

[8] O. Ergun, G. Kuyzu, M. Savelsbergh, Reducing truckload transportation costs through collaboration, Transportation Science 41 (2007) 206–221.

[9] A. Gachet, P. Haettenschwiler, A decentralized approach to distributed decision support systems, Journal of Decision Support Systems 12 (2003) 141–158.

[10] O. Gujo, M. Schwind, J. Vykoukal, The design of incentives in a combinatorial exchange for intra-enterprise logistic services, IEEE Joint Conference on E-Commerce Technology (CEC'07) and Enterprise Computing, E-Commerce and E-Services (EEE'07), Tokyo, Japan, 2007.

[11] L. Houghtalen, Designing allocations mechanisms for carrier airlines, Doctoral Thesis, Georgia Institute of Technology, 2007.

[12] M.A. Krajewska, H. Kopfer, Collaborating freight forwarding enterprises. Request allocation and pro<sup>fi</sup>t sharing, OR Spectrum 28 (2006) 301–317.

[13] M.A. Krajewska, H. Kopfer, G. Laporte, S. Ropke, G. Zaccour, Horizontal cooperation among freight carriers: request allocation and pro<sup>fi</sup>t sharing, Journal of the Operational Research Society 59 (2008) 1483-1491.

[14] D. Pisinger, S. Ropke, A general heuristic for vehicle routing problems, Computers & Operations Research 34 (2007) 2403–2435.

[15] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Quorum Books/Greenwood Publishing, Westport, 2002

[16] C. Püttmann, Collaborative planning in intermodal freight transportation, in: R. Koschke, O. Herzog, K.H. Rödiger, M. Ronthaler (Eds.), INFORMATIK 2007. Informatik trifft Logistik. Band 1, GI Edition — Lecture Notes in Informatics (LNI), Köllen, Bonn, 2007, pp. 62–65.

[17] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, 1982

[18] H. Stadtler, A framework for collaborative planning and state-of-the-art, OR Spectrum 31 (2009) 5–30.

[19] N.A. Welsh, Perceptions of fairness, in: A.K. Schneider, C. Honeyman (Eds.), The Negotiator's Fieldbook: The Desk Reference for the Experienced Negotiator, American Bar Association, Chicago, 2007, pp. 165–174.

Ulrich Derigs is professor and director of the Information Systems and Operations Research Department at the University of Cologne, Germany. His research interests are in the areas of network optimization, combinatorial optimization and mathematical programming with emphasis on ef<sup>fi</sup>cient algorithms and data-structures as well as on decision and data modeling and includes the development of planning methods and decision support systems especially in the area of transportation and logistics as well as banking and <sup>fi</sup>nance. His research was funded by the Deutsche Forschungsgemeinschaft (DFG), Deutscher Akademischer Austauschdienst (DAAD), several private companies and the government. Ulrich Derigs ranks 20th in the 2009 Handelsblatt-Ranking of 2100 professors for Business Administration and Management in Germany, Austria and the German-speaking part of Switzerland regarding life-time research performance.

Sascha Dahl studied Information Systems at the University of Cologne, Germany, from 1999 to 2004 and specialized in Operations Research, Decision Support Systems, Supply Chain Management and Production. From 2004 to 2009 he worked as a research assistant at the Information Systems and Operations Research Department at the University of Cologne. Sascha Dahl received his doctoral degree in 2009. His research interests are operational planning and control of inter-organizational cooperations decentralized optimization, mechanism design. auction and game theory as well as logistic problems, especially dynamic vehicle routing problems
