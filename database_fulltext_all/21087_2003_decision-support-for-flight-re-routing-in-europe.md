---
otero_id: 21087
otero_key: "JR2WD388"
title: "Decision support for flight re-routing in Europe"
authors: "P.A. Leal de Matos; P.L. Powell"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00066-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Decision support for f light re-routing in Europe<sup>\$</sup>

P.A. Leal de Matos <sup>a,</sup>\*, P.L. Powell <sup>b,1</sup>

<sup>a</sup>SAEG-Instituto Superior Te´cnico, Centre for Business Studies, Av. Rovisco Pais, 1049-001 Lisbon, Portugal <sup>b</sup>Centre for Information Management, School of Management, University of Bath, Bath BA2 7AY, UK

Accepted 31 January 2002

## Abstract

Congestion has plagued air traffic in the US and in Europe for the last 20 years. To protect air traffic control from overloads, air traffic flow management tries to anticipate and prevent overloads and to limit resulting delays. This paper focuses on understanding the requirements for developing re-routing decision support systems (DSS). It identifies participants in re-routing decisions and investigates the concept of, and need for, a re-routing decision support system. A re-routing demonstrator is discussed as a first step in the development of a DSS and a demonstrator for pre-tactical and tactical re-routings is described. User feedback is presented and issues of automation and complexity of re-routing DSS are discussed. Finally, the integration of re-routing DSS in future air traffic management systems is addressed. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Air traffic flow management

## 1. Introduction

Congestion has plagued air traffic in the US and in Europe for the last 20 years. To protect air traffic control (ATC) from overloads, a planning activity called air traffic flow management (ATFM) tries to anticipate and prevent overloads and limit resulting delays.

The capacity of an ATC sector is the number of flights that the relevant air traffic control team is able to supervise per time period. When the traffic expected to cross a sector exceeds capacity, delays occur. For example, over 20% of flights were delayed in European airspace in September 2000 due to ATC capacity constraints [16]. The departure delay per delayed flight exceeded 20 min. Approximately 49% of air transport delays are attributable to the problems of air traffic management comprising both ground delays and consequential (or ‘reactionary’) delays [15]. Delays increase the costs of airlines and passengers and it is claimed that delays caused by a lack of capacity cost airlines and passengers more than o5700 m (\$5300 m) in 1999 [15,17]. This estimate does not take into account the cost of the heavier burden on air traffic controllers and other elements of the air transport system. The role of ATFM is to limit the extent and impact of ATC delays.

This paper responds to the decision support needs identified by Leal de Matos and Ormerod [28]. It attempts to understand the issues involved in ‘institutionalising’ decision support systems (DSS) within the ATFM environment [34]. The paper focuses on understanding the requirements for developing re-routing decision support systems. It first identifies the participants in the re-routing domain. Then the concept and need for a re-routing decision support system are investigated. A re-routing demonstrator is discussed as a first step in the development of a DSS and a demonstrator for pre-tactical and tactical re-routings is described. User feedback on the demonstrator is presented and issues of automation and complexity of re-routing DSS are discussed. Finally, the integration of re-routing DSS into future air traffic management systems is addressed.

## 2. Background

The ATFM function has a number of options available to it to limit congestion. These control actions range from departure delays to re-routing flights. Departure delay, or ground-delay, delays departures heading to congested areas. If delays are unavoidable, it is safer and cheaper to delay flights on the ground than in the air. Flights can be re-routed to by-pass already over-loaded airspace or to prevent overloads occurring.

In the US, the Air Traffic Control System Command Center co-ordinates flow management, but US congestion is experienced mostly at airports [11]. In Europe, with many countries each with their own airspace, co-ordinated air traffic control and flow management is more difficult. Many flights in Europe are short but have to cross several airspaces and so congestion results not only at airports, but also in the airspace at the junction points of air routes. Thus, the thrust of air traffic management and control efforts in Europe has been to integrate and centralise control activities. The Central Flow Management Unit (CFMU) in Brussels was created in 1989 to provide air traffic flow management for the countries of the European Civil Aviation Conference (ECAC).

Leal de Matos and Ormerod [28], using action research at the CFMU, investigate the differences in time-scale and organisation of ATFM between the US and Europe. In the US most planning is done in the hours before a flight departs, whereas in Europe planning starts 6 months before departure and involves not only flow managers but also different national administrations, area control centres and aircraft operators’ representatives. This range of stakeholders with divergent interests makes ATFM in Europe more problematic than in the US. US researchers tend to term planning before take-off ‘strategic’ and after the flight take-off ‘tactical’. In Europe, strategic planning covers the period from 6 months to a few days before departure, pre-tactical planning occurs on the 2 days before departure, and tactical planning takes place on the day of departure until take-off. Measures affecting airborne flights are strictly in the realm of air traffic control rather than ATFM.

At pre-tactical and tactical levels, flow managers in Europe handle congestion by negotiating increases in capacity with ATC, by allocating slots to aircraft, and by vertical or horizontal re-routings. Slot allocation is, in practice, the same as ground-delay. A departure slot, usually at a later time than initially scheduled, is issued to flights heading for congested locations. Slots can be at airports, air traffic control sectors or just airspace junction points. The slot allocation program is called a regulation. Contrary to the US, a European flight is often subject to several regulations.

There is some computer-based support for these activities but it is not comprehensive. The CFMU uses TACT, a computer-assisted system for ground-delay allocation in the tactical phase of ATFM. TACT is linked to an automatic system for flight plan processing (IFPS) that provides detailed, updated information on predicted demand. All flights departing from European airports that are going to fly in controlled airspace have to send a flight plan to IFPS up to a few hours before scheduled departure. Past traffic data is kept in the TACT archives and used for strategic and pre-tactical planning. However, traffic patterns can change significantly from one season to the other or even from one week to the next. Europe lacks reliable traffic forecasts to support planning, especially at strategic and pre-tactical levels.

At a more structural level of planning, the CFMU is supported by simulation studies at the experimental centre of the European Organisation for the Safety of Air Navigation (EUROCONTROL). These range from the evaluation of new flow control procedures to the testing of contingency routing schemes. For the other flow management measures, there are no support tools available. Many decisions are taken by consulting maps, building charts and tables, or by combining figures that flow managers obtain from different sources. The problem is currently acute because many European flow managers have only recently been appointed and lack operational experience.

## 3. Support for ATFM decisions

Research on decision support for ATFM is about a decade old. Odoni [36,37] defines the ATFM problem domain, identifies some of the major issues, and suggests decision support needs, mostly based on the US situation. Leal de Matos and Ormerod [28] provide similar European mapping work. Research has concentrated on tactical optimisation models for allocating ground-delays for the US case, with congestion limited to airports. Andreatta and Romanin-Jacur [5] address the case of one airport where congestion lasts for a single time period. Terrab and Odoni [43] present an exact solution method for one airport, several periods and deterministic capacity. Richetta and Odoni [40] provide a linear programming solution to a multi-period single airport case where capacity is stochastic. Vranas et al. [49] and Navazio and Romanin-Jacur [35] present integer formulations for a network of airports, taking into account the interdependency between operations at different airports. Formulations exist to deal with dynamic situations [39,50].

There is research on optimisation models where congestion also affects en-route sectors [29,44]. Helme [21] describes a multicommodity network flow formulation. Vranas [48] proposes optimisation models for allocating tactical ground-delays in Europe accounting for flights crossing several congested airspace elements while Bertsimas and Stock Patterson [9] model the allocation of ground-delays and also speed control of airborne traffic.

In assessing the applicability of optimisation approaches to ATFM, a key question is why none of the models proposed in the literature for the allocation of ground-delays has been implemented in a system for use in practice. Several research projects commissioned by the Federal Aviation Authority (FAA) or EUROCONTROL have looked at optimisation approaches, but they have not got beyond the prototype stage. The following reasons for not using optimisation models have been identified [6,36 – 38].

. The difficulty in defining an aggregate optimisation function that will satisfy all stakeholders.

. The long execution time of optimisation models. Most of these models are integer, and, therefore, timeconsuming to solve to optimality. However, this problem can be mitigated by using approximate methods (i.e., methods that provide a reasonably good solution in substantially less time) or by developing integer formulations whose value is very close if not the same as the one provided by the corresponding linear relaxation [4].

However, Odoni [38] supports the use of optimisation approaches for two reasons: (1) they provide ‘benchmarks’ against which the performance of a current system can be compared, and thus address questions such as whether there is ample or little room for improvement over current practice; and (2) optimisation algorithms can lead to the identification of generic types of ATFM strategies and eventually to the development of easier-to-understand and more user-friendly heuristic algorithms implementing these strategies. Andreatta et al. [6] and Brunetta et al. [12] describe heuristics for allocating ground-delays based on priority rules. The heuristic is less time-consuming than exact models and easier for users to grasp.

There is also literature on simulation approaches to ATFM. There are simulation systems whose main functions are to represent and predict the capacity and demand of the air traffic system, and to highlight congestion problems [14,19,53]; and to explore different strategies and system improvements [1,13,18,19]. Most of the literature in the second category is concerned with long-term strategies (e.g. to study the impact of building a new airport or perform sensitivity analysis of changes in traffic control procedures) or the analysis of flow management policies at a pre-feasibility stage. It is not concerned with producing and evaluating specific congestion-relieving strategies on a daily basis.

There is work exploring the application of artificial intelligence techniques to ATFM. Research on the application of knowledge-based systems has been reported at the FAA by Kornecki [24] and Winer [53] who describe the development of a knowledgebased system prototype for traffic flow management called SMARTFLO. Weigang et al. [52] describe two expert system prototypes for air traffic flow management in Brazil: one reschedules airline timetables to smooth traffic peaks at airports during rush-hours and another predicts congestion and proposes mitigating actions. Bayles and Das [8] describe a prototype system for ATFM that is based on the use of casebased reasoning.

However, research on decision support models and systems for re-routing flights at the strategic, pretactical and tactical levels of ATFM is in its infancy. A re-routing demonstrator and optimisation models for re-routing air traffic flows formed part of a CFMU project [26]. Flight re-routing is included in optimisation models as a variation on, or as part of, a global ATFM problem. Tosˇic et al. [45] describe an integerprogramming model that allocates both ground-delays and routes to individual flights. Bertsimas and Stock Patterson [9] propose variations to their ATFM model to support re-routing of soon-to-depart or airborne flights. A EUROCONTROL project, CARAT, provides the prototype of a tool to support re-routing individual flights [31].

This paper responds to the decision support needs identified by Leal de Matos and Ormerod [28] as part of a larger action research project carried out at the CFMU. It focuses on the design of re-routing decision support systems. Thus, the basic ATFM ‘problem’ is well understood but as there is little extant work upon which to base any DSS. Murphy and Adam [34] argue that for a DSS to be successful, it needs to be institutionalised within the organisation. Institutionalisation is more than having a working system, it is about understanding both the role of the technology and of the DSS staff in assisting decision makers. Murphy and Adam [34, p.1082] argue that ‘institutionalisation forces us to realise that the development of a DSS is not a one-off thing, but is something that happens in the context of a relationship that exists between DSS staff and managers’. In the nascent European ATFM context, a re-routing demonstrator illustrating different decision support possibilities can thus help define the role of re-routing DSS and of how they can assist decision-makers. In addition, the process of developing the demonstrator facilitates the relationship between DSS staff and decision-makers and their commitment to the DSS.

The first requirement is to identify the participants in the re-routing domain. Understanding stakeholders’ needs will enable the construction of useful and usable DSS.

## 4. Participants in re-routing decision support systems

The participants in the development and operation of DSS have been identified in different ways. Turban [46] considers users (usually decision-makers); intermediaries who assist the decision-maker to use the system or manipulate the system on their behalf (while this role has diminished as software has become more user-friendly, ‘chauffeured’ use of systems is a feature of top management use of DSS); builders; technical support; and toolsmiths. Alter [2], in contrast, considers: users who communicate directly with the DSS, decision-makers who use the DSS output, intermediaries who interpret the output for the decision-maker and maintainers who look after the technical aspects. Bidgoli [10] stresses the overlaps of these roles and their dependency on the problem scope. He considers three roles for the design, implementation and utilisation of DSS:

User—the individual, department, or organisational unit for whom the DSS is designed. The DSS has to address the requirements of the user.

 Designer—this role may be divided into two:

\- Managerial designer who defines the management issues.

\- Technical designer who is concerned with technical issues of DSS design and use.

Intermediary—liaison between the user and the DSS. During the design phase the intermediary may interpret the user’s needs to the designer. Later, the intermediary may explain the system’s assumptions and limitations to the user.

Bidgoli’s [10] definition of roles and distinction between decision-maker and user is useful in the context of European ATFM. Participants in the development of re-routing DSS can be identified as follows.

(1) The users are the flow managers based at the CFMU in Brussels; flow managers’ experience varies.

(2) There are two groups of decision-makers in rerouting control measures: flow managers and airlines. In addition, there are others who can influence rerouting decision-making: air traffic controllers and national administrations. Therefore, re-routing DSS need to support both decision-maker sets and take into account the constraints imposed by others.

(3) The designer of a re-routing DSS is, at a first stage, the EUROCONTROL Experimental Centre and, in a second stage, the software team developing the system.

(4) The intermediary is the CFMU User Requirements Section.

Taking into account the roles of the participants, it is possible to articulate the functions of a re-routing DSS. The following section then develops a demonstrator incorporating the views of users, airlines and URS staff.

## 5. Need for a re-routing demonstrator

In this section, the need for a re-routing demonstrator is expanded. Differences between the re-routing demonstrator and a prototype are discussed.

Prototyping is a popular development method. Watson et al. [51] show that 80% of firms develop executive information systems by prototyping methods. A prototype is a ‘quick and dirty’ version of a system. Prototypes attempt to address the difficulties of formulating and articulating requirements reliably and completely before proceeding with system design and implementation [22]. Turban [46] describes two types of prototypes: ‘throwaway’ and ‘evolutionary’. A ‘throwaway’ is a pilot test programme developed to achieve a better understanding of system performance and users’ requirements. Once the pilot test is complete, the prototype is discarded and the design starts. An ‘evolutionary’ prototype is a mini-system that is refined iteratively over a long trial period and hopefully will end up as the finished system [25]. In practice, a prototype approach may have elements of both types, some parts are discarded and redesigned, others are incorporated in the design of the final system. In contrast, Hirschheim et al. [22] distinguish between ‘horizontal’ prototypes and ‘vertical’ prototypes. The former provides the user with interfaces to give the feel of the system but without much of the computational functions, while the latter provides some functionality via a connected subset of functions yet constricted in scope.

Turban [46] identifies five distinct features of prototyping:

1. learning is explicitly integrated into the design process;

2. short intervals between iterations of the prototype;

3. involvement of users. Users provide expertise and are key players in successful implementation;

4. the initial prototype must be ‘low cost’;

5. prototyping by-passes the information requirements definition. It allows requirements to evolve as experience is gained.

Other authors also emphasise the learning role of prototypes. Avison and Fitzgerald [7] see prototypes as learning models that aid system design, and argue that, with a prototype, users can discover what they want from the system and learn what is feasible. Prototyping can be an iterative process, by which users’ suggestions and requirements are, step by step, incorporated into the prototype. Often users do not know or cannot articulate their requirements but building a prototype can progressively reveal them. Avison and Fitzgerald [7] identify situations where prototypes are particularly useful:

 the application area is not well defined.

 the cost of rejection by users would be high and it is essential to ensure that the final version has got users’ needs right.

 there is a requirement to assess the impact of prospective information systems.

Hirschheim et al. [22] add that prototypes may be necessary if modelling the current system is likely to perpetuate unsatisfactory ways of working.

Compared to conventional feasibility studies, prototypes (1) are cheaper; (2) move the project forward in that a basic system is available for use, and the logic and structure of the DSS already implemented; and (3) are concrete whereas the feasibility study is an abstraction [23]. Finally, evolutionary learning through interaction with partial implementations helps the technology to become embedded into the social perception and sense-making process [22].

However, there are potential shortcomings of prototyping. Alter [3] identifies prototypes as:

 encouraging inadequate problem analysis. Prototypes may encourage the overlooking of the systems analysis stage of a project.

users may not give up the prototype, thinking it an adequate version of the final system. It may also generate confusion about whether or not the system is complete and maintainable.

 requiring ‘superprogrammers’ able to work with different prototyping tools and languages.

The flexibility of prototyping allows developers to be more sensitive to users’ needs yet prototypes may heighten expectations beyond what may be deliverable. To manage user expectations, Mallach [32] recommends developers take time to identify to users the missing features of a prototype and explain the consequences if they are skipped. Long [30] adds that prototyping may require greater involvement of key users who are already busy and that the shortcuts involved in prototyping sometimes undermine the final system’s technical foundations. McLeod [33] concurs adding that the emphasis on speed characteristic of prototyping may lead to inadequate control of cost and documentation. However, proper project management and a policy of establishing and enforcing budget limits and documentation standards can prevent these problems. Prototyping can also extend the development schedule because of a tendency to make minute changes to the prototype that do not really improve final usability [32].

The importance of prototyping is recognised in air traffic management. The director of the FAA Aviation Research [55, p.9] highlights the role of prototyping in reducing risks in system development: ‘Prototyping lets us explore how to best implement a new concept or how to build a system during all phases of system development—from early research to detailed design. It allows us to address and resolve many of the major risks in the early stages of a programme. In essence, we can study how a proposed system of people and machines will behave before we have to make firm design decisions that could be very difficult and costly to change later.

Other Air Traffic Management (ATM) researchers, for example, Hansman and Johnson [20] present prototyping as a key element in an integrated humancentred systems approach. This approach considers people ‘as a functional component of the closed loop information system’. They stress the role of prototypes in exploring different system options.

A further function of prototyping is to encourage user participation in design and development, and, thereby, increase commitment. Hansman and Johnson [20] discuss the ownership that a user community have if involved early in the development. However, there are different degrees of user participation: the user might have a consultative role, with the systems analyst making the decisions and specifying the system, or the user might have a decision-making role with the systems analyst as facilitator. Avison and Fitzgerald [7] identify two diverse views of systems development: the conventional versus the humanoriented, the former specialises in aspects of technology, whereas the latter is more interested in the organisation as a whole and the user as a creator in that environment.

This view is also related to the socio-technical approach [7] that recognises the interaction of technology and people in any technical system and the need to optimise them jointly. This approach can lead to systems that are not necessarily the most efficient from a technical viewpoint but that work better in practice. Hirschheim et al. [22] argue, however, that prototyping is still firmly in the functionalist paradigm though it can support social relativism.

The re-routing demonstrator that was built and is discussed here was conceived within this framework as a learning tool to explore different functions and levels of aid with the users, the flow managers. Its need stems from: (1) the users (flow managers) of a re-routing tool having differing levels of experience and, therefore, different decision support needs; (2) a new system of centralised flow management being launched and the knowledge-base for re-routing control measures is still under construction; and (3) the different views on the degree of automation and functions appropriate to a re-routing tool.

The re-routing demonstrator provides a visual image of different re-routing decision support possibilities. It follows a script, based on a real traffic situation in Europe. It differs from a prototype in that:

 It offers different decision support possibilities rather than a ‘version 0’ of a future re-routing DSS. The demonstrator functions may result in separate re-routing DSS (for instance, a pretactical re-routings DSS and a tactical re-routings DSS).

 Only some of the algorithms behind the functions are embedded in the demonstrator.

However, the demonstrator has many features in common with a prototype: (1) it is a step forward in the development of DSS, and a first cut at the logic and algorithms of the system; (2) it represents the system in a tangible way; (3) it constitutes a pre-feasibility study into the development of DSS; (4) it is a learning tool; and (5) it is cheap to develop.

## 6. The demonstrator –user functions

The re-routing demonstrator is for pre-tactical and tactical re-routing. Its main window is shown in Fig. 1. The user functions range from simple queries to complex automated ones. There are seven functions: two provide information on routes, two are aimed at tactical re-routings and three at pre-tactical re-routings.

![](/api/attachments/JR2WD388/fulltext/images/0672ef26fd82ce5899f71c79bd8d0c20db7ccf752cc439fcb864b1262475874f.jpg)  
Fig. 1. Main window.

## Routes

(1) Route Congestion. This function allows a flow manager, already knowing the route, to obtain updated information on the nature of the delays, at a given time, on a given route. For any route, departure time and reference speed, the function provides an estimate of ground-delay. If there are no regulations affecting the route, the function provides the capacity still available on that route; that is, how many flights may be added to the route.

(2) Alternative Routes. This function enables the flow manager to know alternative routes avoiding (congested) airspace. The maximum number of alternative routes provided is four. Routes are selected according to flying time and the user can specify maximum flying times.

## Re-routing Flights—Tactical ATFM

(3) Routes for Flights. This function assists flow managers to reduce the ground-delay of a particular flight and provides alternative routes for the flight.

(4) Flights to Re-route. Given a seriously congested traffic volume, flow managers need to identify quickly which flights can be re-routed, that is, which have good alternative routes. The function identifies flights that can be re-routed.

## Re-routing Flows—Pre-tactical ATFM

(5) Routes for Flows. The flow manager has already defined which flow(s) to re-route and needs to know to which routes to allocate these in order to minimise overall delays. Given an airspace region, and a set of flows to re-route, the function assigns a route to each flow.

(6) Flows to Re-route. The flow managers need to know both which flows to re-route and onto which routes. Given an airspace region with serious congestion problems, this function generates flows to reroute and the corresponding routes.

(7) Contingency Re-routings. Identical to (6) but prompted by a contingency situation, where the capacity of an airspace element is substantially reduced.

The demonstrator was developed in Visual Basic and uses visual features including a small network to represent origin/destination areas, ATC sectors and routes, and colours to represent levels of delay. The demonstrator is based on three contiguous ATC sectors of Southern France, UM, H1H2 and N1N2, using traffic entering these sectors on 7/04/95 between 0800 and 1200 h. These are busy sectors, routes and times.

## 7. Models behind the functions

Fig. 2 shows the links between the different demonstrator functions. The functions to re-route flight and flows make use of the functions providing information on routes. The models for the functions range from information sorting and heuristics to optimisation. They are divided into: (1) Routes and Re-routing of Flights; (2) Re-routing of Flows.

## 7.1. Routes and re-routing flights

(1) Route Congestion: this is a sorting function which utilises only data currently available within CFMU’s TACT system.

. If there are no regulations on the route, it takes the minimum available capacity of all the capacitated airspace elements crossed by the route.

. If any of the airspace elements crossed by the route are regulated, it takes the delay of the most penalising regulation. This could be a ‘what if’ slot allocation or, if this is not possible, the most recent estimate of the average or the maximum delay of the most penalising regulation can be used.

(2) Alternative Routes: This uses standard ‘shortest route’ algorithms that are efficient in terms of both execution time and storage space. The model and algorithm for the re-routing demonstrator is provided in Ref. 26. Two decision criteria are used in the demonstrator to select the routes: one based on flying time and the other on the cost of re-routing.

![](/api/attachments/JR2WD388/fulltext/images/cf3208c210d4cf5ec219c65455cc9fbc8cf0dfa5df296a860c7bab5198dd9a37.jpg)  
Fig. 2. Structure of the demonstrator.

(3) Routes for Flights: The routes are chosen using a weighted time criterion:

$$
z _ {i j} = (d _ {i 0} - d _ {i j}) w 1 - (f _ {i j} - f _ {i 0}) w 2\tag{1}
$$

where $d _ { i 0 }$ is the ground-delay of flight i on the initial route, $d _ { i j }$ is the ground-delay of flight i on alternative route $j , f _ { i j }$ is the flying time of flight i on alternative route j and $\lvert f _ { i 0 }$ the flying time on the initial route. w1 and w2 are the weights given to ground-delay and flying time. The demonstrator uses w1 = 0.5 and w2 = 1. This function makes combined use of the functions < Route Congestion > and < Alternative Routes>.

(4) Flights to Re-route: The flights are selected applying the following filters, in turn:

 Flights whose ground-delay is longer than 45 min.

 Flights with alternative routes whose flying time is less than the maximum time specified.

 Flights whose alternative routes have capacity to accommodate them on a first-come first-served basis.

For each flight filtered the best route is selected. The flights are then sorted by decreasing order using function (1).

## 7.2. Re-routing flows

Flow re-routing is more complex to model. The modelling approach used is based on current ATFM practice, it assumes that flow managers have authority to issue re-routing measures applying to whole flows during a well-defined period, typically a day. Routes cannot be changed frequently nor allocated on an individual flight basis.

Flights are grouped into flows according to their origin-destination, and the problem of re-routing air traffic flows is solved in two stages: (1) Routes Problem: identify acceptable and alternative routes for each flow; (2) Assignment Problem: given a set of flows, a set of acceptable routes and a set of capacity constrained sectors, assign a route to each flow so that the total cost of re-routings and congestion is minimised.

The Routes Problem is solved using the function < Alternative Routes>. Leal de Matos [27] discusses different modelling approaches to the assignment problem and provides three integer programming models resulting from different ways of measuring congestion.

. Model 1 BALDIST—Congestion is measured by penalty variables activated whenever traffic demand is above the sector capacity. The model minimises the sum of the estimated cost of congestion and the cost of re-routing subject to capacity constraints and constraints on the assignment of routes to flows.

. Model 2 DELINT1—Congestion is measured by the number of ground-delayed flights. Ground-delay variables are included to support decisions on rerouting not to allocate ground-delays to individual flights. Therefore, unlike in BALDIST, flights ground-delayed can build up over time. The model minimises the sum of the estimated cost of grounddelay and the cost of re-routing subject to capacity and assignment constraints plus constraints defining and relating the two types of variables—assignment and ground-delay.

. Model 3 DELINT2—Congestion is measured by more detailed ground-delay variables than in DELINT1. This model takes into account not only the number, but also the length, of flights grounddelayed.

The three models were tested using real traffic data crossing the whole French upper airspace on 25/04/ 96, from 0300 to 2200 h, totalling 3582 flights. French airspace was chosen because it is the crossroads of European airspace, with 25% of all ECAC traffic, resulting in many sectors being congested. The period from 0300 to 2200 h is typical of periods to which re-routing control measures apply.

The execution time of the models is not as critical at pre-tactical ATFM as at tactical. However, the models have to provide relatively quick solutions to be useful. Both BALDIST and DELINT2 provide optimum solutions in fewer than 10 min. BALDIST is the most efficient in terms of execution time and size, and provides solutions whose value and resulting delays are almost as good as DELINT2’s. DELINT1 provides solutions not more than 0.8% from the optimum in fewer than 10 min, but is harder to solve, and is significantly larger than BALDIST. Therefore, its use was not recommended and its implementation not pursued.

## 8. Data requirements

Further evaluation of the feasibility of using BALDIST or DELINT2 in a re-routing DSS needs to take into account the size of the data component and the time required to prepare the data to run the optimisation models. The centralised systems at EUROCONTROL provide updated traffic and airspace data. The data is sufficient to run the routes and re-routing flight functions. However, development by CFMU of a function to support re-routing individual flights has revealed that the airspace database is incomplete.

The functions to re-route flows require several data processing operations prior to optimisation: flows have to be defined, alternative routes for each flow determined and represented in terms of the sectors they cross, and the traffic data grouped into flows and departure time intervals. These operations require either an experienced user to define relevant flows beforehand or a partly ‘intelligent’ system able to define flows.

## 9. Feedback

The demonstrator was constructed within the CFMU and its production was the result of interaction between the developer and flow managers. The finished demonstrator was made available to flow managers and staff at the CFMU in a series of structured sessions, and as a generally available tool. During the structured use sessions, feedback was collected by observation of users’ interaction with the system, and by individual and group debriefing sessions. These focussed on the usefulness of the functions provided and the modes of interaction between user and system. The debriefing discussions demonstrated that flow managers found all the demonstrator functions valid and useful. However, these sessions did reveal that flow managers concentrate on one decision criteria to the exclusion of the other available. Two decision criteria are used in the demonstrator: time and cost. In practice, it was discovered that flow managers used only time as a re-routing decision criterion. Therefore, they tended to ignore the cost criterion and information.

Most interest was shown in the pre-tactical functions. For tactical re-routings, functions need to be more detailed and take into account rules applying to the use of airspace (e.g. routes that are only open at certain times, and flight levels that can be used by aircraft on certain routes).

The demonstrator was used as a basis for CARAT, a project undertaken by EUROCONTROL’s Experimental Centre aimed at developing a re-routing DSS. The CFMU is now introducing a function that provides alternative routes for flights based on the CARAT prototype and that uses a ‘shortest route’ algorithm similar to the one proposed by Leal de Matos [26].

The demonstrator functions have different levels of complexity and represent different levels of aid to the flow manager. The next section uses these to discuss the level of automation and complexity required of a re-routing DSS.

## 10. Automation and complexity of re-routing DSS

Automation is ‘the automatically controlled operation of. . .a system. . .that takes the place of human organs of observation, decision and effort’ [41]. Problem complexity can best be defined in terms of structure. A problem is complex if its procedures are not standardised, the objectives cannot be clearly defined, or the input and output not clearly specified. The re-routing demonstrator functions can be mapped against a referential model of automation and complexity (Fig. 3).

![](/api/attachments/JR2WD388/fulltext/images/c10f56d4470fa158ad7adf04ddf3d686af69bbbf24d614e8294a7454a06597b8.jpg)  
Fig. 3. Complexity and automation.

The function < Flights to Re-route> is fairly structured in algorithmic terms, but is substantial in terms of automation, whereas < Routes for Flows> is more complex but requires more intervention from the flow manager.

Automation in air transport is a long-sought goal to achieve greater performance and reliability [41,55]. However, due to the non-repetitive and uncertain nature of many of the tasks, people still predominate. Even in highly automated environments such as piloting an aircraft, people are considered necessary for monitoring, detecting problems and intervening.

Supervisory control describes a situation where there is a co-operative relationship between human and machine [41]. The machine has some decision or control capability, but the human supervises it. Sheridan [41, p.1] provides an analogy between the supervisor’s interaction with subordinate human staff members and a person’s interaction with ‘intelligent automated subsystems; ‘a supervisor of humans gives directives that are understood and translated into detailed actions by staff subordinates. In turn, subordinates collect detailed information about results and present it in summary form to the supervisor, who must then infer the state of the system and make decisions for further actions. Automation and semiintelligent subsystems permit the same sort of interaction to occur between a human supervisor and the computer-mediated process’.

According to Sheridan [41], in the strictest sense, supervisory control means that the computer is an autonomous controller for some variables at least some of the time. More loosely, the computer transforms data from human to controlled process and from controlled process to human, but the computer never closes a control loop that excludes the human.

Supervisory control is associated with human-centred automation, where the human is the main element of the system [20,55]. Human-centred systems development is not straightforward. Hansman and Johnson [20] stress that unless the human is taken into account in the development process, system performance after automation may be worse. This issue is discussed in the DSS literature referring to complementary intelligence [54], it is important that the process of decision making with the DSS makes best use of the user skills and the system skills. Indeed, the underlying ideas behind prototyping ‘can be raced back to optimistic speculation about man-machine communication or man-machine symbiosis and co-operation’ [22, p.115].

Hansman and Johnson [20] mention three factors that affect performance in ATM: (1) situation awareness and attention limitation; (2) information overload and (3) human acceptance and understanding of the automation. These factors are also important to the development of re-routing DSS.

. Situation awareness and attention limitation: the ability to keep an adequate level of situation understanding. At the tactical level, traffic is volatile. Therefore, flow managers have to be aware of the traffic situation so that they can respond in useful time to possible congestion situations.

. Information overload: to prevent loss of situation awareness and multi-tasking capability due to excessive information, the quantity, format and pre-processing of information provided to flow managers has to be carefully assessed.

. Human acceptance and understanding of the automation: flow managers have to be actively involved in the development of DSS and accept the decision criteria used.

An important issue to consider in the interaction between the human and the machine is the type of influence the human has on machine-made decisions. In the context of the development of a computer system to support airport traffic management, Vo¨lkers and Bo¨hme [47] consider two types of human influence on an automatic planning system:

 direct influence- humans can modify or replace a computer-determined plan.

 indirect influence- humans can only change decision criteria or constraints, not computer determined plans.

Various factors have to be taken into account in deciding on the extent of human influence on a rerouting DSS:

 whether sufficient knowledge and experience is available to enable automation.

 the technical feasibility of automation.

 how acceptable automation is to the stakeholders in re-routing decisions.

 how fast and how frequently decisions have to be made.

In European ATFM, at tactical level, the environment is volatile, and decisions have to be made continually and quickly, 24 h a day. At pre-tactical level, 1–2 days before flights, there is time to rethink and review decisions and automation is not used to control traffic situations. The demonstrator functions to support the re-routing of flights are reasonably simple or standard to implement. The functions to support the flow re-routing require more complex algorithms and more expertise in defining the rerouting scope. Thus, a more automated DSS is more useful and more feasible for re-routing flights than for re-routing flows.

In European ATFM, there is already some supervisory control at the tactical level. The TACT system monitors the traffic situation and summarises it to the flow managers. When flow managers, based on that information, issue a slot allocation regulation, TACT allocates ground-delays automatically to flights. The airlines receive slot allocation messages directly from TACT, without human intervention. Flow managers can only intervene in the slot allocation by changing the parameters of the slot allocation regulation (e.g. increasing the number of slots, blocking a slot for a flight). That is, they can only have an indirect influence on computer-determined plans. This mode of supervisory control could also be adapted to re-routing individual flights at tactical level by:

1. flow managers deciding to activate the function < Flights to Re-route>.

2. the re-routing system identifying flights and sending a re-routing proposal to the airlines, without human intervention.

3. flow managers changing the parameters used in the re-routing function.

At the pre-tactical level, for re-routing flows, a DSS suggesting routing schemes that flow managers can check, amend and replace, as needed, is considered more useful and feasible.

The level of automation and complexity of a rerouting DSS is related to the approach taken in DSS development. The Computer Assisted Slot Allocation System at the CFMU is an example of a specific DSS [42]. Turban [46] describes three approaches to the development of DSS.

![](/api/attachments/JR2WD388/fulltext/images/c0eea130e291aa21a524054cd6ac410d433fe2843c0721ad550edfb7c24c83fc.jpg)  
Fig. 4. Implementation of re-routing functions.

. Quick-hit: a specific DSS is constructed when there is a recognised need, a high potential payoff, or a difficult problem. Costs and risks are low, the latest technology can be used, and DSS is constructed quickly using commercially available generators.

. Staged development: a specific DSS is constructed with some planning so that part of the effort in developing the first system can be reused in a future DSS. This can lead to the development of an in-house DSS generator.

. Complete DSS: a full-service, large-scale DSS is constructed. It is a lengthy process that may result in well-integrated tools but risks technological obsolescence.

Considering the uncertainty and infancy of rerouting control measures, staged development is most appropriate for the development of a re-routing DSS. The functions in the re-routing demonstrator are amenable to staged development (Fig. 4). For instance, in order to implement functions for re-routing flights and flows, functions must provide alternative routes and information on delays or spare capacity of routes. This development approach would provide results earlier than if a fully automated system was developed from scratch and be less risky.

The final aspect needing consideration is how the suggested tools will fit into the ATM environment. This is discussed in the next section.

## 11. Integration re-routing DSS in future European ATM environment

The development of re-routing DSS cannot be considered in isolation: future developments in European and world ATM need to be taken into account. These developments concern the nature of the ATM environment when the re-routing tools become available, possibly in the next 5 years, and how they will fit into that world. Re-routing tools cannot be developed only on the basis of present needs; those in 5–10 years must be anticipated.

Zellweger [55] presents examples of substantial investments made by the FAA in new systems that, when finally available, were either not needed or were outdated. Re-routing tools might become outdated before becoming available as shown below.

. In the European ATM Integration Programme there is a program for route network development and associated airspace structures. This aims to increase European ATC capacity through restructuring the air route network and associated airspace sectorisation. This new air route network will be more flow-oriented and have far fewer junction points. The implementation of this has already started and will extend into the next decade.

. Direct routings in upper airspace will probably mean more planning of sectors rather than routes.

. With progress in airlines’ standard flight planning systems it is possible that in the future, even small airlines will be able to work out alternative routes without assistance from ATFM. The only information they will need from ATFM is the likely ground-delay on certain routes. It is possible that functions in the demonstrator to provide alternative routes for individual flights will not be needed.

. Developments in collaborative decision making. This will also entail negotiation support systems to work in concert with the re-routing systems to allow rapid resolution of different stakeholder concerns. This will become increasingly important as airlines get more involved in the planning process. At present, airlines can already have access to TACT by means of specific terminals. However, this is read-only access and is limited to a sub-set of TACT information.

A key issue is how these re-routing tools will integrate with existing systems. The demonstrator functions can be divided into two groups: functions for re-routing individual flights at tactical level, and functions for re-routing flows. The detail and integration with TACT varies significantly between these. Rerouting flows addresses the distribution of traffic in a more aggregate way. The problem consists of routing sets of flights so that the total delay or cost is minimised and serious overloads are avoided; it is a master scheduling problem. Traffic forecasts can be used as input to these re-routings. At tactical level, for individual flights, re-routing functions need more detailed information in terms of flight profiles and specific slot allocation delays, and therefore to interact often with the part of TACT that allocates slots, CASA (Fig. 5).

![](/api/attachments/JR2WD388/fulltext/images/af5d2309c22712b92d0b01a595f511a6d4ac379710907fbf3a72a8d1dc71db8e.jpg)  
Fig. 5. Integration CASA/Re-routing.

## 12. Conclusions

This paper has investigated the development of rerouting DSS. A re-routing demonstrator is discussed and described. The level of automation and complexity of re-routing DSS are analysed based on the functions developed in the demonstrator. This reveals there is scope for decision support systems to assist re-routing flights in Europe because of their potential to respond quickly and consistently to complex problems. They can also provide training and support to less experienced staff. The format of such a DSS needs further investigation, and issues such as the user interface remain under-researched.

A DSS for re-routing flights has to take into account that the users of the tool, flow managers, have differing levels of experience and, consequently, different decision support needs and that different views on the degree of automation of a re-routing tool prevail. Also, given the novelty of centralised ATFM, the knowledgebase for re-routing control measures is still under construction.

The re-routing demonstrator is a tangible representation of different decision support possibilities and an assessment of their pre-feasibility. The demonstrator user functions can be broken down into two groups: functions to re-routing flights at tactical level, and functions for re-routing flows at pre-tactical level. The demonstrator functions represent different levels of automation and complexity ranging from those that sort data on routes to more complex ones suggesting flights to re-route. Feedback from users indicates that all functions in the demonstrator could be of use and suggests ways forward in the development of re-routing DSS.

The demonstrator functions providing data on routes and decision support for re-routing flights at tactical level use simple or standard algorithms. However, as the feedback suggests, the database for rerouting flights will need to include detailed rules on the use of airspace. The demonstrator functions to support pre-tactical re-routings are more complex and require knowledge that is scarce.

Given this, and the different time-scales for pretactical and tactical re-routings, a higher level of automation of DSS for tactical re-routings is more useful and feasible than for pre-tactical. For tactical re-routings a form of supervisory control is suggested. For pre-tactical re-routings manual control with the DSS providing advice is proposed.

Given the infancy of centralised European ATFM, the most appropriate approach to the development of a re-routing DSS is staged development, starting with the simpler functions and incrementally developing the more complicated ones. Finally, the development of a re-routing DSS has to be seen in the context of future developments in the European air traffic management environment such as changes to the air route network and associated airspace structure and progress in the airlines’ standard flight planning systems.

## References

[1] M. Adams, S. Kolitz, J. Milner, A. Odoni, Evolutionary concepts for decentralized air traffic flow management, Air Traffic Control Quarterly 4 (4) (1996) 281 – 306.

[2] S. Alter, Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading, MA, 1980.

[3] S. Alter, Information Systems: A Management Perspective, Addison-Wesley, Reading, MA, 1996.

[4] G. Andreatta, L. Brunetta, Multi-airport ground holding problem: a computational evaluation of exact algorithms, Operations Research 46 (1) (1998) 57– 64.

[5] G. Andreatta, G. Romanin-Jacur, Aircraft flow management under congestion, Transportation Science 21 (4) (1987) 249– 253.

[6] G. Andreatta, L. Brunetta, G. Guastalla, Flow management problem: recent computational algorithms, Control Engineering Practice 6 (6) (1998) 727 – 733.

[7] D. Avison, G. Fitzgerald, Information Systems Development—Methodologies, Techniques, and Tools, Blackwell Scientific, Oxford, 1988.

[8] S. Bayles, B. Das, Using artificial intelligence to support traffic flow management problem resolution, Proceedings of 1994 American Association for Artificial Intelligence— Technical Report WS-94-01, AAAI Press, Boston, MA, 1994.

[9] D. Bertsimas, S. Stock Patterson, The air traffic flow management problem with enroute capacities, Operations Research 46 (3) (1998) 406– 422.

[10] H. Bidgoli, Decision Support Systems—Principles and Practice, West Publishing, St. Paul, 1989.

[11] G. Booth, Flow management in the United States, Proceedings of Advanced Technologies for Air Traffic Flow Management, Deutsche Forschungsanstalt fu¨r Luft- und Raumfahrt e.V., Bonn, 1994.

[12] L. Brunetta, G. Guastalla, L. Navazio, Solving the multi-airport ground holding problem, Annals of Operations Research 81 (1998) 271– 287.

[13] J. DeArmon, A. Lacher, Aggregate flow directives as a ground delay strategy: concept analysis using discrete-event simulation, Air Traffic Control Quarterly 4 (4) (1996) 307 – 323.

[14] EUROCONTROL, Capacity Plan 1998 for the European Air Navigation Services, EEC Note N. 3/98, EEC Task R13, EATCHIP Task PLC-4-E1, (1998).

[15] EUROCONTROL, Special Performance Review Report on Delays (Jan – Sept 1999)—PRR 2, (1999).

[16] EUROCONTROL, Delays to Air Transport in Europe in September 2000, CODA (2000).

[17] Flight International, EURO ATC delays could rise by 70%, 13 – 19 October, p. 10 (1999).

[18] B. Flynn, A. Tibichte, J. Hoffman, ATFM Performance Analysis and Simulation Capability, ATFM Pilot Study Report, EEC task AT64, EEC Note N. 7/94, EUROCONTROL Experimental Centre (1994).

[19] I. Frolow, J. Sinnott, National airspace system demand and capacity modeling, Proceedings of the IEEE 77 (11) (1989) 1618– 1624.

[20] R. Hansman, J. Kuchar, E. Johnson, Human centered development of information systems and decision aids in advanced air traffic management systems, Advanced Workshop on Air Traffic Management, Capri, Italy, 1995.

[21] M. Helme, Reducing air traffic delay in a space-time network, IEEE International Conference on Systems, Man and Cybernetics 1 (1992) 236– 242.

[22] R. Hirschheim, H. Klein, K. Lyytinen, Information Systems

Development and Data Modeling: Conceptual and Philosophical Foundations, Cambridge Univ. Press, Cambridge, 1995.

[23] P. Keen, Value analysis: justifying decision support systems, in: R. Sprague, H. Watson (Eds.), Decision Support Systems Putting Theory into Practice, Prentice-Hall, New Jersey, 1989, pp. 65 – 81.

[24] A. Kornecki, AI for air traffic, IEEE Potentials 13 (3) (1995) 11 – 14.

[25] K. Lantz, The Prototyping Methodology, Prentice Hall, Englewood Cliffs, NJ, 1986.

[26] P. Leal de Matos, Re-routing Study, Internal Report, Central Flow Management Unit—EUROCONTROL (1995).

[27] P. Leal de Matos, Development of Decision Support Models for European Air Traffic Flow Management, unpublished PhD Thesis, University of Warwick, UK (1998).

[28] P. Leal de Matos, R. Ormerod, Application of operational research to European air traffic flow management, European Journal of Operational Research, 1999.

[29] K. Lindsay, E. Boyd, R. Burlingame, Traffic flow management modeling with the time assignment model, Air Traffic Control Quarterly 1 (3) (1993) 255 – 276.

[30] L. Long, Management Information Systems, Prentice-Hall, Toronto, 1989.

[31] P. Loubieres, Computer Aided Route Allocation Tools (CAR-AT) Phase 1: Modelisation and Algorithms, EUROCONTROL Experimental Centre Internal Report (1996).

[32] E. Mallach, Understanding Decision Support Systems and Expert Systems, Irwin, Burr Ridge, Illinois, 1994.

[33] R. McLeod, Management Information Systems, Science Research Associates, Chicago, 1990.

[34] C. Murphy, F. Adam, Routinising DSS in organisations, Proceedings of 6th European Conference on Information Systems, Aix-en-Provence. (June 1998) 1071–1085.

[35] L. Navazio, G. Romanin-Jacur, The multiple connections, multi-airport ground holding problem: models and algorithms, Transportation Science 32 (1998) 268 – 276.

[36] A. Odoni, Flow management problem in air traffic control, in: A. Odoni, L. Bianco, G. Szego¨ (Eds.), Flow Control of Congested Networks, NATO ASI Series, Series F: Computer and Systems Science vol. 38, Springer, Berlin, 1987, pp. 145–161.

[37] A. Odoni, Issues in air traffic flow management, Proceedings of Advanced Technologies for Air Traffic Flow Management, Deutsche Forschungsanstalt fu¨r Luft- und Raumfahrt e.V., Bonn, 1994.

[38] A. Odoni, Flow management in transition, Air Traffic Control Quarterly 4 (4) (1996) 225 – 227.

[39] O. Richetta, Optimal algorithms and a remarkably efficient heuristic for the ground-holding problem in air traffic control, Operations Research 43 (5) (1995) 758 – 770.

[40] O. Richetta, A. Odoni, Solving optimally the static groundholding policy problem in air traffic control, Transportation Science 27 (3) (1993) 228–238.

[41] T. Sheridan, Telerobotics, Automation, and Human Supervisory Control, MIT Press, Cambridge, MA, 1992.

[42] R. Sprague, A framework for the development of decision support systems, MIS Quarterly, December 1980, pp. 1 – 11.

[43] M. Terrab, A. Odoni, Strategic flow management for air traffic control, Operations Research 41 (1) (1993) 138– 152.

[44] V. Tosˇic, O. Babic, M. Cangalovic, Ð. Hohlacov, Some models and algorithms for en route air traffic flow management, Transportation Planning and Technology 19 (2) (1995) 147–164.

[45] V. Tosˇic, O. Babic, M. Cangalovic, Ð. Hohlacov, A Model to Solve En Route Air Traffic Flow Management Problem: A Temporal and Spatial Case, unpublished report, University of Belgrade (1995).

[46] E. Turban, Decision Support and Expert Systems, Management Support Systems, Macmillan, New York, 1990.

[47] U. Vo¨lkers, D. Bo¨hme, Dynamic planning for airport surface traffic management, Advanced Workshop on Air Traffic Management, Capri, Italy, 1995.

[48] P. Vranas, Optimal slot allocation for European air traffic flow management, Air Traffic Control Quarterly 4 (4) (1996) 249 – 280.

[49] P. Vranas, D. Bertsimas, A. Odoni, The multi-airport groundholding problem in air traffic control, Operations Research 42 (2) (1994) 249 – 261.

[50] P. Vranas, D. Bertsimas, A. Odoni, Dynamic ground-holding policies for a network of airports, Transportation Science 28 (4) (1994) 275 – 291.

[51] H. Watson, R. Watson, S. Singh, D. Holmes, Development practices for executive information systems: findings of a field study, Decision Support Systems 14 (2) (1995) 171 – 184.

[52] L. Weigang, C. Pinto Alves, N. Omar, An expert system for air traffic flow management, Journal of Advanced Transportation 31 (3) (1997) 343–361.

[53] D. Winer, Simulation and optimization in flow planning and management, in: L. Bianco, A. Odoni (Eds.), Large-Scale Computation in Air Traffic Control, Springer, Berlin, 1993, pp. 67 – 82.

[54] L. Young, A corporate strategy for decision support systems, in: R. Sprague, H. Watson (Eds.), Decision Support Systems Putting Theory into Practice, Prentice-Hall, New Jersey, 1989, pp. 185– 192.

[55] A. Zellweger, Technology evolution and its impact on air traffic management, Advanced Workshop on Air Traffic Management, Capri, Italy, 1995.

Paula Leal de Matos works for the performance strategic planning and forecasting component of Eurocontrol—the European organisation for the safety of air navigation. She previously taught economics and management at the Technical University of Lisbon and worked for the UK National Air Traffic Services. Her first degree is in Economics awarded by the Technical University of Lisbon. She also holds an MSc in Operational Research and Statistics from the Lisbon Faculty of Science and a PhD in Business and Industrial Relations from the University of Warwick, UK. The subject of her PhD was the development of decision support models for European air traffic flow management. Her work has appeared in the Journal of the Operational Research Society, the European Journal of Operations Research, International Journal of Advanced Manufacturing Technology and OR Insight.

Philip Powell is Professor of Information Management and Director of the Centre for Information Management at the University of Bath. Formerly, Professor of IS, University of London, and Director of the IS Research Unit at Warwick Business School. Prior to becoming an academic he worked in insurance, accounting and computing. He is the author of four books on information systems and financial modeling. He has published numerous book chapters and his work has appeared in over 60 international journals. He is Managing Editor of the Information Systems Journal, Book Reviews Editor of the Journal of Strategic Information Systems, and on a number of other editorial boards. He is President-elect of the UK Academy for Information Systems.
