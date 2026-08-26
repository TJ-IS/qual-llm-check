---
otero_id: 17648
otero_key: "DN6GCR8W"
title: "A prototype decision support system in hypermedia for operational control of hazardous material shipments"
authors: "Giampiero E.G. Beroggi; William A. Wallace"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90070-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A prototype decision support system in hypermedia for operational control of hazardous material shipments

Giampiero E.G. Beroggi

Delft University of Technology, 2600 GA, Delft, The Netherlands

William A. Wallace

Rensselaer Polytechnic Institute, Troy, New York 12180, USA

Recent advances in information technology, in particular satellite location and communications, have made real-time transit control of hazardous materials feasible. The information exchange between mobile units and control centers can include text, audio, graphics, and video. Extensive data analyses at the control centers can help vehicles carrying hazardous materials to assess driving conditions and select safe and cost-effective routes. A prototype decision-support system has been developed in HyperCard that can support an operator at a control center in risk assessment and route guidance. The paper also discusses issues of implementation and the need for further research.

Keywords: Decision support system; Hypermedia; Operational risk assessment; Hazardous material transportation; Real-time transit control

![](/api/attachments/DN6GCR8W/fulltext/images/a9e1ac0d9c0ecb99d362a9a417eafebd8d48d7a356910ea739efc8080aafb18e.jpg)

Giampiero Beroggi is an Assistant Professor in Systems Engineering and Policy Analysis at Delft University of Technology, Netherlands. His research interests include operational control of large scale systems, risk and environmental management, decision support systems and multicriteria models. He received his Ph.D. in Urban and Environmental Studies and his M.S. in Operations Research and Statistics from Rensselaer Polytechnic Institute, Troy, New York and

his Dipl. Ing. degree from the Swiss Federal Institute of Technology, Zurich, Switzerland.

## 1. Introduction

Recent advances in location and communications technology have made operational management of mobile units feasible. Headquarters or control centers know the exact location of vehicles, and two-way communications can provide the means for monitoring and dispatching them.

The major breakthrough in location technology is due to advanced satellite systems, which have now become available for commercial purposes. Accurate locating can be done with the Global Positioning System (GPS) of the U.S. Department of Defense. The system will consist eventually of 21 satellites which provide 3-D positioning accuracy of a few meters, 24 hours a day, and worldwide. The location data, as well as any other data about the mobile units, can be transferred to the headquarters via satellite or radio. Since the costs of hard- and software for such location systems are steadily dropping, private companies are starting to use this technology to better manage their truck fleet. Examples of satellite based tracking systems are Geostar and Omnitracs in the U.S., and Euteltracs in Europe.

The commercially available software packages that support these satellite tracking systems can handle up to several thousand vehicles on a mainframe. The software packages typically include messaging (sending messages via keyboard), reporting (automatic printing of reports), vehicle positioning / mapping (location of vehicles on a map in different colors for different statuses as well as overlay of customized maps), and vehicle tracking (display of travelled route). However, advanced decision support tasks, such as route selection or reasoning are not addressed.

![](/api/attachments/DN6GCR8W/fulltext/images/d05ded5c808a2f45ce1134d8929753647dcee090d9337877d8836815d1c2600f.jpg)

While hazardous material emergency response units take already advantage of these new capabilities by knowing immediately the exact location of the accident, the type of material involved, and the fastest route to get to the accident site, headquarters of hazardous material trucking companies are not supported in decision making. This refers to assessing hazardous driving conditions and selecting safe, cost-effective routes, using real-time data about the trucks' locations and the actual environmental conditions. The prototype decision support system (DSS) for hazardous material transportation (HMT) presented here addresses in a novel approach the decision making tasks of a truck company's headquarters using this new technology. It incorporates graphical display, advanced user interface, risk assessment procedures, and routing models. Real-time data input has only been simulated, since our focus was on the design of the DSS and the incorporation of decision models. A practical assessment of this prototype DSS was performed by presenting it to experienced dispatchers.

## 2. Operational decision support for hazardous material transportation

Operational control of hazardous material transportation refers to the activities needed to monitor and guide shipments of discrete hazardous material units in a transportation system from origin to destination in real-time. These activities can be divided into geographical data analysis and route selection. These two tasks have been incorporated only for strategic tasks to different extents into Geographical Information Systems (GIS's) and Decision Support Systems. For example, Haz-Trans, developed at the Vanderbilt Engineering Center for Transportation Operations Research (VECTOR) at Vanderbilt University in Nashville, Tennessee, is designed to help corporations devise optimal routes for transporting hazardous materials from their plants to waste sites by considering transportation costs, road conditions, local regulations, and the population put at risk in case of an accident [1]. Another example is the prototype risk management system called IRIMS (Ispra Risk Management Support System) developed by the Joint Research Center, Commission of the European Community, Ispra, Italy [7]. The system consists of several modules for environmental assessment, risk analysis, and routing. Both systems, however, are not designed for processing real-time data received via satellite systems, but address mainly strategic and planning issues, while this prototype system takes advantage of the readily available real-time data.

The transportation system chosen for this research is a road network, and the mobile units are assumed to be trucks of a company's fleet. Real-time transit control is performed by an operator (dispatcher) at a control center (headquarters). The operator monitors on a screen the simulated movement of the vehicles and analyses data about the status of the vehicles and changes in the environment, which are also simulated.

For many events that cause changes in environment and vehicle conditions appropriate actions can be planned in advance. However, some events occur unexpectedly and cannot be planned in advance. Such unexpected events are called real-time events (RTE's). In cases of a RTE, the operator must be supported fast and efficiently in risk assessment and route guidance. Examples of RTE's are storms and traffic accidents.

An entity on the road network is defined as a physical object of interest, such as a hospital, vehicle, bridge, urban area, or intersection. A RTE causes a change in risk or cost of such an entity. A change in risk can be due to hazardous driving conditions and a change in cost can reflect a traffic jam.

The operator at the headquarters will be concerned with two major tasks: sensing and reasoning [3]. Sensing refers to monitoring the transportation system for any RTE's. Reasoning refers in the case of managing a hazardous material truck fleet to real-time risk assessment and route selection. The operator must in case of a RTE assess hazardous driving conditions and then determine safe and cost-effective routes.

Most of the time, however, no RTE is present and the operator is merely monitoring the movement of the hazardous material units on a screen, without actively intervening. The dynamic task and decision flow for operational control of hazardous material transportation is shown in Figure 1.

RTE's, such as bad weather or traffic accidents, are by definition unpredictable. Therefore, data about RTE's can be limited both in quantity and quality. The first task for the operator in case a RTE occurs is to filter and process any incoming data in order to decide whether the event significantly affects safety or operating costs of at least one entity. If the event is not considered to be serious, the operator goes back to the monitoring tasks. If the event is deemed serious, the RTE is called perceived. The next decision is to determine whether enough data is available to determine which links on the transportation network are affected. While a road accident usually affects only one link, bad weather can affect a region.

If more information is needed to determine which links are affected, but the event is perceived as very serious, the operator must immediately alert all vehicles; otherwise the operator will gather and process more data. When the affected links have been determined, the RTE is called located. As soon as the RTE is located, the DSS can automatically determine the affected vehicles so that selective guidance of the vehicles can be given. The affected vehicles are those whose planned route goes through the region affected by the RTE.

Once the affected links and vehicles have been determined, the risks and costs for the affected links must be assessed. The operator might want more data on the event to do these assessments. However, the operator cannot spend too much time gathering and/or processing additional data since the affected vehicles continue to move steadily closer to the affected region. As long as no rerouting is done, the vehicles keep moving on their “old” route, passing potential rerouting points. The DSS computes a minimal ( $T_{min}$ ) and a maximal ( $T_{max}$ ) decision time for risk and cost assessment. $T_{min}$ is the time it takes the vehicle to reach the end of the link, which is also the first point at which the vehicle can be rerouted; $T_{max}$ is the time it takes the vehicle to reach the affected region.

![](/api/attachments/DN6GCR8W/fulltext/images/b12ecf2237454ee2c84622b6b8cd2cf36ace682da2f6b8bdd0985f0443ea03f1.jpg)  
Fig. 1. Task and decision flow for real-time HMT control.

When risks and costs of the affected links have been assessed, the RTE is called assessed. The DSS can then compute new optimal routes for those vehicles that are affected by this RTE, i.e., those vehicles that have at least one link of their planned route affected by the RTE. The system can then suggest (1) stopping a vehicle and waiting until the RTE is over, (2) rerouting a vehicle to avoid hazardous driving conditions, or (3) continuing a shipment on the planned route if the RTE is not too dangerous. The new routes are presented to the operator who then communicates the new routes to the drivers.

All vehicles that have been stopped or rerouted because of a RTE must also be advised on what route to take once a RTE is over. The DSS might suggest that some vehicles go back to their initial route, that others stay on the reroute, and that still others take a different route altogether.

Special consideration must be given to vehicles that enter the control area when several RTE's are already in progress. They may have entered the area on routes that were optimal given the RTE's in progress, but once they are in the area, they must be assumed to be affected by all ongoing RTE's, just as are the vehicles that were already in the area when each RTE occurred. Similarly, once each RTE is over, all vehicles in the area must be advised on new optimal routes.

## 3. System overview

## 3.1. The programming environment

A hypermedia environment was chosen for this prototype DSS so that text, graphics, audio, and video could be used. It also has the advantage of being easily extendable for user-specific purposes. Hypermedia is a powerful concept that has changed the way of organizing information and procedures (objects). While objects are traditionally processed in a sequential way, the hypermedia concept is based on a graph structure. The nodes (objects) can contain text, graphics, executable programs, or any other form of multimedia information and procedures (e.g., video and sound). The oriented links represent relationships between two nodes, which can consist of sending a message, linking nodes, activating a successor node, “jumping” to another node, or any other relation. Hypertext and hypermedia have been the subject of research, writing, and experimentation for more than 20 years [8].

The DSS was written in HyperCard on a Macintosh SE/30. A great advantage of HyperCard over other prototyping environments is that it supports text processing and drawing. Its fully developed programming language, Hypertalk, can also read and write data to other files or applications. HyperCard is very well suited for prototyping, since the modular structure of the programming environment and the available high-level commands significantly cut down the development time and reduce the chances of error. In order to improve execution speed for the algorithms, external commands (XCMD) compiled in lower level languages have been included. The data about vehicle location and status can be received via Macintosh's serial port and are controlled by HyperCard with some XCMD's. Another reason for developing the DSS on the microcomputer level is that hardware costs are low and the DSS becomes highly portable. This makes testing and future implementation of the DSS into companies' headquarters easier to achieve $[2]$ .

The HyperCard environment supports the graphical interface strongly. A Hypertalk script can be attached to a “button,” which the user can activate by clicking with the mouse on it. The activated buttons execute whatever has been defined by the script, which is also called the message handler. A script can create a link to another application, execute a program, or display a graphic. In addition, message handlers (scripts) can be placed at different levels, organized in a hierarchical structure, so that messages can be received at any lower level. The object hierarchy in HyperCard is the following: buttons and fields → cards → backgrounds → stacks → Home stack → HyperCard.

The prototype DSS has been developed within a HyperCard stack. A stack is a collection of several cards which can continuously be added to the stack. Several cards can share the same background. Each card can contain button and fields that are technically both objects, able to handle and send messages. In addition, graphics can be added to each card, either on the background or on the foreground.

![](/api/attachments/DN6GCR8W/fulltext/images/5e9b6f0ff000d61905ec21960ac620824d7ccdb9d1f0c42a4e03bfb1a7262afa.jpg)  
Fig. 2. The basic graph structure of the DSS.

![](/api/attachments/DN6GCR8W/fulltext/images/30a7471f0b65837cc2e30126749c68c3f245d81205ebad938e20ec1f57820e23.jpg)  
Fig. 3. The Monitoring Screen.

Figure 2 shows the basic graph structure for this DSS. The names in bold indicate objects at different levels. The objects on the top level are the buttons 'New RTE', 'Delete RTE', 'Route', and 'Vehicle i'. The objects on the next lower level are the cards 'Monitor Card', 'RTE New Card', 'RTE i Card', 'Vehicle i Card', and the n link cards. The object on the lowest level is the 'Stack.' Each object has at least one script written in Hypertalk. In addition, some scripts use external commands. The scripts start with "on message" and end with "end message." The message can refer to system messages, e.g., the mouse input, such as "mouseUp", "mouseDown", "mouseStillDown", and "mouseWithin", or to user-defined messages, such as "assessPreferences", "newRTE" and "deleteRTE".

## 3.2. Overview of the DSS

For this DSS, a road network consisting of 69 links from the Capital District region of New York State has been chosen. To allow for various transportation environments, selected highways, rural roads, and inner-city roads have been considered. To include longer distances, the map has been distorted so that the links do not necessarily have the same scale. However, to make the simulation realistic, the vehicles have been assigned a lower speed on links that are actually longer than they appear on the map.

The card containing the monitoring screen shows the road network on which three vehicles move. Figure 3 shows the Monitoring Screen.

The vehicles are either on the road or at a place at the top right of the screen reserved for when they are not on the road (“parking-place”). Information about the vehicles can be obtained by clicking on them. If a vehicle is on the road, its “parking-place” shows either an “OK” or a blinking “RR”. The “OK” occurs when the vehicle’s route is based on all ongoing real-time events. The blinking “RR” occurs when the vehicle’s route has to be updated either due to a new RTE or due to the deletion of a RTE. Information about a link can be obtained by clicking on it. The actual time and date are displayed at the right bottom of the screen.

The buttons on the right of the map can be clicked by the user with the mouse to activate different menus. A vehicle is initialized by clicking on the vehicle at the parking place. The monitoring of the movement of the vehicles can be activated or deactivated by clicking on the button “Monitor”. A RTE can be defined by clicking on the button “Not-Assessed RTE’s” and a RTE can be deleted by clicking on the button “Assessed RTE’s”. If the field above the button “Not-Assessed RTE’s” shows a blinking “Yes”, then a RTE has been located (region and name are defined and affected vehicles determined) or deleted, but the affected links have not yet been assessed. The field underneath the button “Assessed RTE’s” shows a nonblinking “Yes” if there are any assessed RTE’s. In order to route or reroute a vehicle, the operator must click on the button “Route”. The button “Dispatch” allows the operator to dispatch information to the vehicles.

Data and information about each vehicle is held on a special card and can be checked at any time. This refers to the start time of the shipment, origin, destination, cargo, planned route, and the real-time event affecting the vehicle's route.

A new real-time event (NRTE) is a real-time event for which the links have not yet been assessed (i.e., the event is located but not yet assessed). After the vehicle is initialized, the “optimal” route can be determined, but only if there aren’t any NRTE’s. This is so because a NRTE indicates that risk or cost values of some links might change and a reassessment of the routes must be done. The new vehicle should wait until all NRTE’s are assessed in order not to be rerouted soon after it begins its trip. If no NRTE is present, the vehicle can be routed.

If the vehicle is on the road, the operator can choose between the two menus: "Show Info" and "Re-Route". Rerouting can also only be done when no NRTE's are present. Routing (or rerouting, which is the same process) can have different motivations. The first one comes from the operator and is consequently called "voluntary". This refers to routing a new vehicle that has been idle or to checking alternate routes, eventually on a subnetwork. The second motivation is due to the definition of a new or the deletion of an ongoing real-time event and is called “imposed”. No matter what the motivation is, the process of determining a route is the same in all the cases.

## 3.3. The movement of the vehicles

The movement or the continuous location of the vehicles on the transportation network is simulated. It is performed by the message handler, which is called the “mover” in this context. When the mover is activated, it processes each vehicle in a serial mode; i.e., it moves the vehicles one by one. The delay between each vehicle’s processing depends on the mover’s speed, which can also be altered. This is especially important when running the program on computers with different processing frequencies.

When other tasks must be performed by the message handler, such as routing or defining a new real-time event, the mover must be set to idle. When reactivating the mover, the operator has the choice between two menus: "New-Start" and "Re-Start". While the first neglects the time elapsed during which the mover was idle, the second takes this time into account. Choosing the second menu, the mover "jumps" the vehicles to the location they would be in if the mover had not been deactivated for a certain time; i.e., it simulates a parallel processing of multiple handlers. This is especially interesting if time constraints must be simulated for the assessment phase and other processes. While the operator performs tasks other than monitoring, the vehicles move along their routes.

The speed of the simulated vehicle movement depends on a “delayer” called TC (transit control). While the mover wants to move a vehicle at each processing step for one-tenth of the distance between two nodes, the delayer tells the mover to move the vehicle only each $(TC + 1)$ -th processing step for one-tenth of the distance. Therefore, the higher the TC, the slower the vehicle moves. The move counter is called K and has value 1 at the beginning of a link and value 10 when the vehicle reaches the end of a link. Therefore, a vehicle on a link with a delayer TC of 3 takes 40 processing steps by the mover to travel through the link.

The “jump” for when the elapsed time must be considered after monitoring is resumed is computed for two different situations. The first situation is when the vehicle is still on the link it was at the time monitoring was set to idle. In this case, the “jump” occurs by replacing K with $K + dt$ , where

$$
d t = \operatorname{round} \left(d t ^ {\prime} / (T C + 1)\right),
$$

$$
\text { and } d t ^ {\prime} = \text { round } (\text { elapsed   time } / 1 0).
$$

The reason to divide the elapsed time by 10 is that the “jump” should correspond approximately to the distance the vehicle would travel in the elapsed time and depends also on the computer’s processor.

The second situation in which the “jump” is considered is when the delay was long enough for the vehicle to move past the end of the link it was on at the time the mover was set to idle (i.e., $(K + dt) > 10$ ). In this case, the “jump” is determined in the following way: delete the trunc $((k + dt)/10)$ first links of the route; replace k with $(k + dt)-10$ trunc $((k + dt)/10)$ .

Once this DSS will be connected to a satellite tracking systems that updates continuously the vehicles' locations, the mover will not be needed any more. The coordinates of the vehicles will be transferred via satellite or radio to a file of the system. Hypercard then reads these coordinates and transfers them to the local coordinate system and places the vehicles to these new places on the map. Since the vehicles are represented by buttons, the locations can be changed using a Hypertalk script:

set loc of button "vehicle r" to x, y.

The actual position of a vehicle can be check at any time by the script

get the loc of button "vehicle r".

The locations of the vehicles can therefore also be checked in relation to other elements of the map; e.g., one could easily determine the closest emergency response unit or the remaining distance to the planned destination.

## 4. Operational risk assessment

It was mentioned above that RTE's can be at three different levels, as far as the state of knowledge is concerned. The lowest level of a RTE is when the operator knows that the RTE is present but cannot determine the affected region (perceived RTE). An example is a major weather change that has not yet been located. A RTE in this premature stage will be registered by the operator, and if the RTE is of very serious concern, the operator will warn all vehicles.

If sufficient information is available to identify the affected region, the RTE is called “located” or “new” (NRTE). Only at this stage does it become subject to analysis, since the affected links and the affected vehicles can be determined. A vehicle is affected by a RTE if at least one link of its planned route falls into the affected region. If sufficient information is available to assess the new costs and risks of the affected links, the RTE is said to be assessed, and it is abbreviated as simply RTE.

Each NRTE and RTE has its own card, on which information about the event is held. The operator can view, retrieve, change, or delete information about any event. Two pop-down menus on the monitoring card deal with real-time events, one with NRTE's and the other with RTE's. Above the NRTE button and below the RTE button is a field indicating "No" if there is no event present or "Yes" if there is at least one event present.

As long as an event is a NRTE, the operator is kept on alert. He or she must gather more information to assess the affected links. Therefore, if there are any NRTE's, the field above the button for NRTE's shows a blinking "YES"; otherwise, it shows a nonblinking "No". Another alert refers to the affected vehicles. As soon as a vehicle is determined to be affected by an event, its "parking-place" blinks with "RR", which stands for reroute; otherwise, the "parking-place" shows a non-blinking "OK".

A real-time event always enters the DSS as a NRTE, and if sufficient information is available to assess the affected links, it is transformed to a

RTE. If the assessment is postponed, the operator is alerted. By clicking on the NRTE button, a pop-down menu appears, which shows the menus "New" and the names of the NRTE's already defined, if there are any. The operator is then asked if the affected region has been marked using a special graphic tool that allows one to draw using the mouse. If this is the case he is asked to enter the name of the NRTE. After this has been done, the message handler automatically puts the name, graph, and time into the appropriate information card. It thereafter determines the affected links and vehicles. The affected vehicles have a blinking "RR" in their "parking-place". The system computes $T_{min}$ (time to reach the end of the link it is on right now) and $T_{max}$ (time to reach the first link of the affected region) for each affected vehicle and puts this information into the information card of the NRTE. The units of both $T_{min}$ and $T_{max}$ are not seconds, minutes, or hours but rather the number of jumps simulating the movement of the vehicles. Using the same notations as introduced for the vehicle movement, the two times are defined in the following way:

$$
\mathrm{T} _ {\min} = \mathrm{TC} ^ {\prime} + (1 0 - k - 1) ((\mathrm{TC} + 1),
$$

where $\mathrm{TC}'$ is actual TC-value $\in [0, \mathrm{TC}]$ , and

$$
\mathrm{T} _ {\max} = 1 0 \left[ \left(\sum (\mathrm{TC} + 1)\right) - (\text { first   TC } + 1) \right] + \mathrm{T} _ {\min},
$$

where $\sum$ goes from 1st link to last link

before 1st link in affected region.

It takes the vehicle $T_{min}$ to reach the end of the link, and it takes the vehicle $T_{max}$ to reach the first link that lies (at least partly) within the affected region. $TC_{1}$ and $TC_{2}$ are the link-specific delayers for the mover. If $T_{min} = T_{max} = 0$ , then the vehicle is already within the affected region. In this case, the handler alerts the operator.

Fig. 4. Minimal and Maximal Decision Time.  
![](/api/attachments/DN6GCR8W/fulltext/images/8b92c7ad062f4e1d1aa164763ca879862879a4ab3660f60023ff0d5f92b5881a.jpg)

When the system is connected to the satellite tracking system, the speed of the vehicles is not known. To compute $T_{min}$ and $T_{max}$ , the system will use average travel times for the links. The average travel time from the vehicle's location to the end of the link is $T_{min}$ , and the average travel time to the first link affected by the RTE is $T_{max}$ .

After the RTE is located, the message handler asks whether the affected links can be assessed; i.e., whether the NRTE can be transformed to a RTE. If this is not the case, the message handler exits; i.e., it becomes idle and it can be reactivated by clicking on another button. If the operator wants to assess the affected links, the NRTE is transformed to a RTE. This means that the event's name is transferred from the NRTE to the RTE list and that the message "Yes" stops to blink if the NRTE list is empty. The operator is then automatically presented the list of the affected links for assessment. Once all the links are assessed, the message handler becomes idle. The next step is to recompute routes for the affected vehicles. If the assessment of the links is postponed, the pop-down menu of the NRTE button shows the names of all the NRTE's. If one of these names is chosen, the operator has the choice of assessing the links or deleting the NRTE. If a NRTE is deleted, the information card is deleted, and if no other NRTE's are present, the blinking "Yes" turns into a nonblinking "No".

The menu “Assessment” refers to the process of assessing the links whose risk and cost values might change either due to the occurrence of a new real-time event or because an ongoing real-time event is over. The menu can be chosen in three different instances. After a new real-time event has been located, the handler asks the operator if the operator also wants to assess the affected links. If this is not the case, the assessment of the affected links is postponed. Selecting NRTE from the pop-down menu, the operator is asked if he or she wants information about the NRTE or if he or she wants to assess the affected links. If the operator does not feel ready to assess the links, he or she can request information about the NRTE. A button called “Assessment” will blink on the information card as long as this NRTE has not been assessed.

No matter in which instance the operator decides to assess the affected links, the handler presents the operator with a card showing all the affected links. By clicking the appropriate button, the assessment process is initialized. This means that for each link a card (corresponding to this link) is presented to the operator (see Figure 5). The card tells the operator information about the link: name, length, coordinates, etc. A map shows where the link is located.

Risk and cost assessment is done according to the preference assessment procedure [4]. Preference assessment considers humans' limitations in risk and cost assessment in an operational environment, where information is usually incomplete and inaccurate. The preference assessment spectrum consists of four risk-preference classes, one cost-preference class, and two preference classes for both risks and costs. The latter two preference classes either close a link because it is too dangerous or too expensive, or they neglect cost or risk aspects. Costs are changed simply by entering the appropriate dollar amount. Risk-preferences can be significantly dependent on the travel length or not. For example, the risk-preference of shipping a certain hazardous material in a heavy snow storm is significantly dependent on the travel time, while the shipment of the same material on a highway with low traffic density and good weather is not dependent on the travel time. The risk-preference value for road segments that depend strongly on the segment length is assumed to be identical with the segment length (in miles). The risk-preference value for entities that are not length-dependent is entered by clicking the button "Points".

![](/api/attachments/DN6GCR8W/fulltext/images/73047d08d95058347c128c37e27a148e35088a439dcbe5cfa4806b8afd698905.jpg)  
Fig. 5. Preference Assessment Card.

The five preference classes considered here are therefore the following, where “<” means “less preferred than”:

$$
\begin{array}{l} \alpha <   \text { high - risk } _ {\mathrm{L}} <   \text { high - risk } _ {\neg \mathrm{L}} <   \text { cost } <   \text { low - risk } _ {\mathrm{L}} \\ <   \text { low - risk } _ {\neg \mathrm{L}} <   \omega . \end{array}
$$

The class $\alpha$ stands for entities that are too dangerous or too costly. Therefore, a link with such an entity cannot be considered for the route. The class $\omega$ stands for entities that can be neglected for both risk and cost. The subscript “L” indicates that the risk-preference is significantly dependent on the link length, while “ $\neg L$ ” indicates that the risk-preference is not dependent on the link length.

The dispatcher assesses cost- and risk-preferences for each entity on the links one-by-one. Once the assessment for one link is done, the handler presents the operator the next link, until all the affected links are assessed. An example is given in Figure 5. The link is affected by the two RTE's 'Snow' and 'Accident.' The operator increases the operational costs by \$1,000 to account for the expected delay due to these two RTE's. The three miles through the urban area are assessed as high-risk and the other 143 miles are assessed as low-risk. One low-risk value is assigned to the one bridge and the one intersection on the link.

## 5. Route selection process

The route determination process is performed on a special card. The operator can reduce the network to a subnetwork by simply selecting graphically with the mouse the appropriate region or links. The system then determines automatically the links that belong to this subnetwork.

The algorithm for finding an optimal route is similar to the classical shortest-path algorithm $[5]$ but is based on the preference algebra $[4]$ . It determines the optimal route (considering the two criteria ‘risk’ and ‘cost’) from the origin of the vehicle to its planned destination by combining links according to the following priorities: (1) it never takes a ‘closed’ link, (2) among the ‘open’ links, it avoids as much as possible the high-risk links, (3) if there are no high-risk links (or for ties), it takes the most economical route, and (4) if there are still ties, it avoids as much as possible the low-risk links.

The mathematical description of the routing problem is based on a mixed calculus defined by the preference algebra. The overall link-preference, which is determined by assessing each entity on the link one-by-one, depends on the cargo and on the time of day. Links are connections between two nodes on the road-network. An example of a node is an intersection. The decision variables of this routing problems are the links of the network, which can be part of the optimal route or not.

The objective of this decision problem is to find the optimal route among the feasible routes, i.e., the route with highest overall preference given the assessment of risk and cost in real-time by the dispatcher. The constraints of this decision problem refer to the flow conservation and to the condition that the links that have been closed by the dispatcher must be avoided.

For demonstration purposes, the routing algorithm is written in Hypertalk. However, to improve execution speed, the algorithm should be written as an external routine in C or Pascal.

Once the node-sequence of the optimal route from origin to destination is computed, the handler puts the solution into the information card of the appropriate vehicle. If the path-finding process referred to rerouting, the operator is presented with both the old route and the newly computed route graphically, as well as the overall risk and cost values of the routes. The operator can then select which route he or she wants to suggest to the driver. If the path-finding process referred to “routing” and the operator does not like the computed route, he or she can either alter the preferences for certain links and/or choose another subnetwork and then reroute the vehicle.

## 6. Assessment of the DSS

The practical assessment of the DSS was performed with the help of experienced dispatchers at Chemical Leaman Tank Lines, Inc., at its headquarters in Exton, PA, and at its regional dispatch center in Albany, NY. In a first phase, the system as currently designed was introduced to the persons participating in the assessment. The basic tasks of monitoring, definition of real-time events, risk assessment, and routing were introduced. This phase aimed at the assessment of the models and the user interface.

In a second phase, a simulated scenario was run to assess the task and decision flow, as well as the ease of use. The occurrence of real-time events was simulated while the three vehicles were on their route. Since some of the vehicles' routes went through the affected region, those vehicles had to be rerouted. The simulated run lasted about 20 minutes. In the third phase, the evaluation of both models and DSS were performed by discussing with the operators the design of the DSS and expected benefits if this DSS were to be integrated in their daily operations.

The initialization of the vehicles corresponds to the dispatching tasks with which the operators are very familiar. The drivers' names, the type of cargo, and origin and destination are assigned to each truck. However, the possibility of monitoring the vehicles on a screen was new to the operators and very much appreciated. The first new task that the DSS provides is support in route selection. The possibility of choosing a sub-network, to which the vehicle is restricted, gives more flexibility. However, for the case in which many vehicles have to be routed or rerouted, a repetition of this process might be time consuming and confusing. More automation is appropriate (especially when more than three vehicles must be guided) but has not been considered in this prototype version of the DSS.

Defining a NRTE made intuitive sense to the operators. The graphical capabilities of the hypermedia environment facilitate crucial tasks, such as selecting affected links, and are much more convenient than searching in a list or on a map for the desired links. The RTE information card provides the important information about the name of the RTE, the time it occurred, the affected links, and especially the affected vehicles and the time available for rerouting them. While operators in traditional settings would need to check a road map to see which vehicles are affected by the RTE, the automatic assessment by the DSS has the advantage of saving time and avoiding errors.

The principles of assessing the affected links in conjunction with the principles for route selection were easily introduced by using the descriptive formulation for route selection given above. The operators readily understood the principles involved but would require more training before they would feel comfortable with the process of preference assessment. With appropriate training, the “average” operator should be able to use the DSS easily and effectively.

The appropriateness of ordinal measures for risk assessment has been underlined by remarking that governmental efforts for operational emergency response aim at the same direction. Instead of assessing numeric risk values, the emergency responder is more interested in prioritized alert levels, the location of the sensitive objects (hospitals, schools, ground water) and the properly equipped response units.

Considering that risk and cost assessment is required only in very specific and infrequent cases, the major tasks of the operator will be monitoring and automatic assessment; i.e., either the RTE is known or the dispatcher assigns to all links the same preference (e.g., close the link). It became clear that too much flexibility can confuse the dispatcher in stress situations and also that dull tasks such as monitoring and searching for disruptions should be automated as much as possible. This fact has also been noted by Hopkin [6], who studied the automation capabilities for air traffic control.

The overall assessment of the DSS and its underlying decision models was very positive. Automation certainly has to be emphasized more for practical use of the DSS. However, for training purposes, the DSS as currently designed with three units is appropriate. Only an assessment in a real application within a pilot study will show how much automation is appropriate and how much flexibility an experienced dispatcher wants.

## 7. Further research

Further research is needed to answer several open questions concerning managerial aspects of operational hazardous material transportation. While modelling aspects have been investigated thoroughly, the design of the decision-support system must be tested further. In addition, an experimental assessment of the DSS has to be considered. However, since both the decision support approach and the decision tasks are novel, a complete experimental assessment of the DSS is difficult to design. The benefits of this decision aid will be shown only through implementation in the hazardous material shipping industry and improvement of safety and economic aspects. Therefore, the assessment of this DSS is best done by a pilot study in a large-scale setting. The goal will be to show the DSS's practical realism and to answer managerial questions. After the completion of this subsequent step, the DSS for operational tasks presented here should make a major contribution to the safe shipment of hazardous materials.

## Acknowledgements

The research was supported by the United States National Science Foundation under a rapid-assessment grant from the Natural and Manmade Hazard Mitigation Program, by the Swiss National Science Foundation, and by the Swiss Academy of Engineering Sciences.

## References

[1] M. Abkowitz, P.D.-M. Cheng and M. Lepofsky, Ship it by GIS, Civil Engineering, (April 1990) 64–66.

[2] S. Belardo, K.R. Karwan and W.A. Wallace, Managing the Response to Disasters Using Microcomputers, Interfaces, 14, (1984) 29–39.

[3] G.E.G. Beroggi and W.A. Wallace, Closing the Gap: Transit Control for Hazardous Material Flow, Journal of Hazardous Materials, 27/1, (1991) 61–75

[4] G.E.G. Beroggi, Modelling Real-Time Decision Making for Hazardous Material Transportation, Ph.D. Dissertation, University Microfilm International, No. 9202173, 300 N Zeeb Road, Ann Arbor, MI (1991).

[5] G.B. Dantzig, On the Shortest Route Through a Network, The Mathematical Association of America, Studies in Graph Theory, Part I, (1975) 89–93.

[6] V.D. Hopkin, Man-Machine Interface Problems in Designing Air Traffic Control Systems, Proceedings of the IEEE, special issue on air traffic control, (November 1989) 1634–1642.

[7] R.J. Peckham, P. Haastrup and H. Otway, A Computer-Based System for Risk Management Support, Decision Support Systems, 4, (1988) 481–489.

[8] N. Yankelovich, B.J. Haan, N.K. Meyrowitz and S. Drucker, Intermedia: The Concept and the Construction of a Seamless Information Environment, IEEE Computer, (January 1988) 81–96.

[9] W.A. Wallace and F. De Balogh, Decision Support Systems for Disaster Management, Public Administration Review, special issue, (1985) 134–146.
