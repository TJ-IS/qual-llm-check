---
otero_id: 13128
otero_key: "VDNMEP68"
title: "A web spatial decision support system for vehicle routing using Google Maps"
authors: "Luís Santos; João Coutinho-Rodrigues; Carlos Henggeler Antunes"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A web spatial decision support system for vehicle routing using Google Maps

Luís Santos <sup>a,d</sup>, João Coutinho-Rodrigues <sup>b,d,</sup>⁎, Carlos Henggeler Antunes <sup>c,d</sup>

<sup>a</sup> ISA—Intelligent Sensing Anywhere, Estádio Cidade de Coimbra, 92, 3030-320 Coimbra, Coimbra, Portuga

<sup>b</sup> Department of Civil Engineering, Faculty of Sciences and Technology, Polo II, University of Coimbra, 3030-788 Coimbra, Portugal

<sup>c</sup> Department of Electrical Engineering and Computers, University of Coimbra, Faculty of Sciences and Technology, Polo II, 3030-290 Coimbra, Portugal

<sup>d</sup> Researcher at R&D Unit INESC-Coimbra, R. Antero Quental 199, 3000-033 Coimbra, Portugal

## a r t i c l e i n f o

Article history: Received 23 December 2009 Received in revised form 2 June 2010 Accepted 3 November 2010 Available online 11 November 2010

Keywords: Vehicle routing Spatial decision support systems Google Maps™ Heuristics

## a b s t r a c t

This article presents a user-friendly web-based spatial decision support system (wSDSS) aimed at generating optimized vehicle routes for multiple vehicle routing problems that involve serving the demand located along arcs of a transportation network. The wSDSS incorporates Google Maps<sup>™</sup> (cartography and network data), a database, a heuristic and an ant-colony meta-heuristic developed by the authors to generate routes and detailed individual vehicle route maps. It accommodates realistic system speci<sup>fi</sup>cs, such as vehicle capacity and shift time constraints, as well as network constraints such as one-way streets and prohibited turns. The wSDSS can be used for “what-if” analysis related to possible changes to input parameters such as vehicle capacity, maximum driving shift time, seasonal variations of demand, network modi<sup>fi</sup>cations, and imposed arc orientations. Since just a web browser is needed, it can be easily adapted to be widely used in many realworld situations. The system was tested for urban trash collection in Coimbra, Portugal.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. The importance and impacts of vehicle routing problems

The transportation of goods and services imposes considerable costs on both the public and private sectors of the economy as well as the environment. More ef<sup>fi</sup>cient vehicle routing can improve a <sup>fi</sup>rm's competitive advantage, increase the ef<sup>fi</sup>ciency of supplying public services, and reduce energy consumption, traf<sup>fi</sup>c congestion and air pollution, which are growing problems in many urban areas. Vehicle travel increased substantially in recent decades. Total vehicle miles of travel (VMT) in the United States increased 63% between 1980 and 1997 and it has more than doubled between 1970 and 2000. The rate of growth in VMT has exceeded signi<sup>fi</sup>cantly the rate of population growth, employment growth, and economic growth over the last decade of the 20th century [7]. In China total motorized passenger-km rose sixfold between 1980 and 2003, and freight distance increased nearly <sup>fi</sup>vefold in that period [30]. In cities, the movement of goods may account for 20 to 30% of the total vehicle miles traveled, and for 16 to 50% of all air pollutants resulting from transportation [6]. Urban freight transportation is on one hand an important economic activity but on the other hand is rather disturbing (traf<sup>fi</sup>c congestion, noise and other environmental impacts). Issues related to freight transportation are pertinent in an urban context (where the number of vehicles, congestion and pollution levels are increasing fast) and therefore they need to be well understood and quanti<sup>fi</sup>ed.

In what concerns environmental impacts, some recent studies emphasize the optimization of route choice based on the lowest total fuel consumption and thus the emission of ${ \mathsf { C O } } _ { 2 }$ [8]. However, many see the need for a threefold strategic approach: improving fuel economy, decreasing VMT and lowering the carbon content of fuels. Woodcock et al. [30] also refer to several main strategies jointly required for moving to low-carbon transport, being shortening trip distances one of them. Similar <sup>fi</sup>ndings are also supported by other authors (e.g., [27]) stating that currently there are no costeffective technological solution available for mass deployment to reduce CO emissions, so the only way is to increase the use of alternative fuels, greater ef<sup>fi</sup>ciency in fuel use, increased occupancy and load factors, and through reducing the distances travelled. This research may be included in this global strategy, as a contribution for reducing miles traveled in vehicle routing problems in an urban setting.

In what concerns transportation and injuries, Woodcock et al. [30] mentioned that, because of the growth in traf<sup>fi</sup>c, many people are exposed to levels of kinetic energy that can result in serious injury, being estimated that in 2002 1.2 million people were killed and 50 million people were injured in road-traf<sup>fi</sup>c crashes, and these <sup>fi</sup>gures continue to rise. Moreover, heavy goods vehicles are twice as likely to be involved in fatal crashes than are cars, per kilometer travelled. Therefore, reducing VMT is also an important issue in what concerns these types of risks imposed on people's health

Dablanc [6] calls for improved logistics in European cities. Improved logistics also would bene<sup>fi</sup>t the United States of America where freight transportation costs account for approximately 6% of the gross domestic product (GDP) [15].

The importance of transportation problems has been acknowledged by the scienti<sup>fi</sup>c community. However, the optimization of transportation routing is computationally intractable for most realworld problems (e.g., [9,16]). This has justi<sup>fi</sup>ed the development of heuristic approaches to generate (optimal or near-optimal) solutions in acceptable computer times. As a consequence, the design and implementation of exact and heuristic solution algorithms for such problems constitute an interesting challenge for operations research (OR) and transportation science, both from a methodological perspective and practical decision support purposes to address all the issues mentioned above. The potential bene<sup>fi</sup>ts of OR models and methods applied to transportation systems, having in mind the implementation in practice, has constituted a research avenue followed by the authors, namely concerning the development of strategies to deal with real-world urban vehicle collection/ delivery problems [4,23] and new approaches for routing problems [22,24,25]. These methodological innovations were conveniently adapted and incorporated in the implementation of the web-based spatial decision support system (wSDSS) presented in this paper.

## 1.2. DSS and ICT in transportation problems

Due to the data requirements and the complexity of urban planning and transportation problems, there has been a growing interest in the use of decision support systems (DSS) to analyze them at the operational (e.g., [17,26]), the tactical (e.g., [18]) and the strategic planning levels (e.g., [5,29]). Adequate graphical interfaces are important to represent solutions in routing problems given their strong spatial component. Information and communication technologies (ICT) can play an important role for constructing tools embedding algorithms, graphical interfaces and access to remote data through the Internet. Due to the spatial nature of these problems, geographical information systems (GIS) have been a natural component of such DSS as they are important tools for collecting, organizing, and displaying spatial data in a large variety of planning applications, such as in vehicle routing problems [20,23]. Hans [11] enhanced the importance of the development of GIS for urban transportation planning and modeling, including networkbased urban transportation planning, and the incorporation of network data into a GIS framework in order to have a high-speed interactive system suitable for providing near real-time alternatives and policy analysis. Although transportation research has been “late to embrace GIS as a key technology to support its research and operational needs” [28], there has been an increase of such research in recent years. Much of this research also incorporates exact and heuristic solution algorithms with the GIS (e.g., [1,5,12,17,19,23,26]).

The development of decision support tools pro<sup>fi</sup>ting from state-ofthe-art ICT is an important avenue of research. World Wide Web technologies have transformed the design, development, implementation and deployment of DSS; however, it is recognized that the use of Web-based computation to deploy DSS applications for remote access remains less common [3]. In the <sup>fi</sup>eld of transportation, some recent developments can be found, e.g., Ray [21] has developed a webbased spatial DSS for managing the movement of oversize and overweight vehicles over highways.

The importance of ICT, besides GIS technology, is acknowledged in several <sup>fi</sup>elds related to transportation [2,14]. In what concerns transportation problems, the Internet enables the implementation of web-based GIS systems, allowing users to interact with networks, maps, and GIS tools through a browser (e.g., [20]). The Internet potentiates new approaches due to two principal reasons: the advanced capabilities offered, unique amongst other ICTs, and because of its widespread adoption [13].

On the other hand, the availability and price of adequate up-todate cartography has been a drawback in GIS-based systems. Furthermore, a network structure (de<sup>fi</sup>ned on maps) is required to be used as input data and also for running the routing optimization algorithms. Google Maps<sup>™</sup> services may overcome those limitations by providing access, through the Internet, to cartography and to road/ street network structures, as well as to important real data associated with roads and traf<sup>fi</sup>c restrictions (e.g., one-way streets, prohibited left and U-turns). In addition, it supplies travel times for each street or road based on the respective speed limits. Thus, exploring this particular ICT capabilities provided by the Internet coupled with Google Maps™ services is a promising avenue for developing web based spatial DSS incorporating speci<sup>fi</sup>c algorithms for routing optimization problems.

## 1.3. The aim of this research

In this article, we present a wSDSS integrating optimization methodologies (e.g., heuristics and ant-colony meta-heuristics) previously developed, improved and tested by the authors, designed for multiple vehicle routing problems [23–25]. These methodologies were adapted in order to satisfy several additional constraints of actual problems (as explained in the next section) before their integration into the system. The wSDSS was tested on a real-world multiple vehicle routing problem: trash collection in the City of Coimbra, Portugal. Although the application presented in this paper is a speci<sup>fi</sup>c one, the wSDSS is applicable to several public and private sector vehicle routing problems. The system can be used for short-term analysis (e.g., the design of daily vehicle routes) and long-term analysis (e.g., deciding how many vehicles to operate in a <sup>fl</sup>eet).

Several important design criteria for the wSDSS were de<sup>fi</sup>ned. First, it must generate ef<sup>fi</sup>cient vehicle collection routes quickly as demand patterns and routes can change seasonally or even daily. Second, the system must be intuitive enough to be used by people with little or no background in OR models and methods. Third, the wSDSS must generate individual route maps and directions for the drivers. Fourth, the system must be able to incorporate various operational and local network speci<sup>fi</sup>c conditions and constraints. Fifth, it is also desirable for the system to be able to analyze long-term decisions, such as the number (and/or size) of vehicles to operate and the length of an employee's work shift. Finally, the system must be “universal” (virtually usable at any place on Earth), using public access cartography and real road network data through the Internet (Google Maps<sup>™</sup>) via a standard browser (i.e., not requiring the installation of special client software).

The remainder of this article is organized as follows. A brief description of the main characteristics of the routing problem is made in Section 2. The architecture of the wSDSS including some implementation details is presented in Section 3. Some illustrative results are presented and discussed in Section 4. A summary and conclusions are provided in the last section.

## 2. Background: The underlying routing problem

Vehicle routing is a common and costly problem faced by many private and public sector companies, with important economic, social and environmental aspects, as described in the Introduction. Basically, the wSDSS implemented addresses arc routing problems with applications in many real-world situations. Examples include the collection/distribution of goods along streets, street cleaning, water, gas, and electricity meter reading, pipe or road inspection, mail delivery, and the collection of urban solid waste [4]. Many of these applications can be structured as a capacitated arc routing problem (CARP), introduced by Golden and Wong [10]. In this problem demand occurs along the arcs, some arcs in the network may not require service (i.e., have no demand along them) and the vehicles have a capacity on the total demand that they can serve. Golden and Wong [10] proved that CARP belongs to the class of NP-hard problems.

The authors have recently addressed the CARP by developing a new improved path-scanning heuristic [24], and an ant-colony meta-heuristic approach [25]. Nevertheless, they have also recognized in previous research works that a real-world arc routing problem (e.g., an urban trash collection problem) cannot be approached exactly as a CARP because of various speci<sup>fi</sup>c operational conditions/constraints that complicate the vehicle routing problem [4,23]. Therefore, the algorithms implemented to deal with the formal CARP had to be adapted and extended to accommodate more requirements of the real-world problems. We refer to such a routing problem as the constrained CARP or C-CARP. These speci<sup>fi</sup>c operational conditions/constraints that differentiate C-CARP from CARP include:

1. One-way streets (i.e., the network includes directed arcs);

2. Prohibited turns (e.g., U-turns and left turns) at some network intersections;

3. The route “drop-off point” (i.e., the land<sup>fi</sup>ll in this case), which is not at the same location as the depot where the vehicles start and end their shifts;

4. Vehicles that can serve more than one route in a day (All routes for a particular vehicle must include a “drop-off point” - a land <sup>fi</sup>ll in this case. Only the last route for each vehicle must return to the starting depot immediately after visiting the “drop-off point.”);

5. The maximum shift duration for all vehicles in a day, which represents the maximum hours that the vehicle's crew can work that day.

The algorithms previously developed and validated for CARP were taken as good starting tools for implementing a wSDSS dedicated to routing problems. The description of the particularities of those underlying approaches is beyond the scope of this paper - the reader is referred to Santos et al. [24,25] for a more formal and detailed description of the particular heuristic and meta-heuristic approaches that were adopted to be included in the solver engine at the core of the wSDSS. However, to develop a solution procedure for C-CARP (considering all the conditions/constraints enumerated above), those heuristic and meta-heuristic approaches needed to be adapted conveniently.

Other general requirements, not directly related to routing problems, were taken into consideration in the design of the wSDSS, such as the remote access to digital maps and network data, as well as producing a web application only requiring an Internet browser. In what concerns the requirements related to the human–computer graphical interface, access to cartography and network data, Google Maps™ appeared to be the best tool due to its universal availability via the web and inherent possibilities of accessing remotely road network data and constraints. This has been perceived as an effective way of merging together the distinct vehicle routing methodologies developed by the authors mentioned above (after a convenient adaptation to the conditions/constraints of the C-CARP), by coupling them with Google Maps™ in order to obtain a functional (and easyto-use) prototype system able to be used by decision makers in real problems. This way, the use of ICT turned possible that sound methodologies could be used in practice for important routing problems by linking them together, providing an adequate userinterface to support spatial representations of the problems, and enabling the remote access to urban data through the Internet for feeding the algorithms.

## 3. Architecture of the wSDSS

## 3.1. Implementation details

The design criteria for the wSDSS were stated above. Input and output requirements were de<sup>fi</sup>ned as well as the desired analytical/ planning capabilities. These include the ability to generate solutions with algorithmic approaches embedded in the system (which are “transparent” for the user), generate maps and instructions for individual vehicle routes and system solutions, produce detailed tabular information about routes, and represent solutions using an Internet browser.

To achieve these objectives, the wSDSS requires raw data, data information management and analysis capabilities, and graphical display capabilities. Given these requirements and the spatial nature of the data, a system using Google Maps<sup>™</sup> services was considered to be the most appropriate. Consequently, the wSDSS was implemented incorporating state-of-the-art optimization algorithms (heuristic and meta-heuristic approaches as mentioned in Section 2), and accessing Google Maps<sup>™</sup> cartography and street networks data via the Internet. The data for each problem are stored in a database also accessible via the Internet. The schematic representation of the architecture and modus operandi of the implemented system is presented in Fig. 1. The ASP.Net web application framework, and the C# and JavaScript programming languages were used in the development of the system. The database was developed using the Microsoft SQL Server Express. The user accesses the wSDSS (the data of each problem and the algorithms operating on them) via an Internet browser.

The wSDSS was tested in the City of Coimbra (an old Portuguese city of about 120 000 inhabitants, with an historical center). As usual in old cities, an important central core zone exists in Coimbra where the road network is dense and characterized by a broad variety of streets in terms of width and number of lanes, with very narrow and one-way streets, high traf<sup>fi</sup>c, and endemic congestion problems. That urban core area of Coimbra, including its historical center, with the highest demand per area and the most complex routing options, has been selected as a challenging test <sup>fi</sup>eld for the trash collection problems tackled using the wSDSS.

## 3.2. wSDSS interface

The interface is supported by a standard web browser window where the map of Google Maps<sup>™</sup> occupies the central area. A bar with drop-down menus is displayed on the top of the map area offering four main menus: “Edit Networks,” “Shortest Paths,” “Solve Problem” and “Show Results.” A left-hand sidebar exists where editable <sup>fi</sup>elds to be <sup>fi</sup>lled in become available for inputting data and buttons appear, consistently with the options selected in the main menus (as described in Section 3.3). A right-hand sidebar supports lists with the representation of results available after solving a problem (as described in Section 3.4).

## 3.3. wSDSS input

Among other features, the system includes different menus that provide several possibilities of input data edition. Problem parameters either related to arcs (such as arc traversal times and service demand) or related to vehicles (such as capacities, maximum shift times, relative costs) can be edited in the wSDSS environment using the corresponding boxes that are displayed on the left-hand sidebar after selecting an input command in a main menu (as shown in Fig. 2). The menu “Edit Networks” offers two options: “Create arcs” and “Modify data.” By choosing “Create arcs” an area for arc creation is displayed on the left-hand sidebar of the window; an arc is created by clicking on two points on the map (see “A, B” arc in Fig. 2). This makes the wSDSS to display automatically on the map the arc de<sup>fi</sup>ned by these two points. The two nodes' coordinates, arc length and arc travel time

![](/api/attachments/VDNMEP68/fulltext/images/2b67c52280c23e707891a9262f34a284ec54382deaf73bbe3c68ca80ba659da9.jpg)  
Fig. 1. Architecture of the wSDSS: Schematic representation and data/control <sup>fl</sup>ows.

values are automatically downloaded from Google Maps<sup>™</sup> in order to <sup>fi</sup>ll in the corresponding <sup>fi</sup>elds. However, the user can freely edit those parameter values. The values of other parameters, as arc service time, arc demand and arc orientation, can also be de<sup>fi</sup>ned by the user. In what concerns arc orientation, the change of a particular characteristic of a road might be needed. For instance, in a steep road it may be inappropriate going up for a truck (e.g., a trash collection vehicle). Therefore, a constraint forcing such a vehicle going down the road may be included (by selecting the appropriate option in the “Type of the arc” area), even if this does not apply to the general traf<sup>fi</sup>c. This actually occurs in Coimbra which is a rather hilly city. At any time the user can also update any editable data by choosing “Modify data” in the “Edit Networks” menu and editing the editable parameters displayed on the left-hand sidebar.

The shortest paths between any pair of nodes of the network under study, as required by the algorithms, are evaluated by the system by coded requests to Google Maps<sup>™</sup> services using the menu “Shortest paths” in the menu bar. This way, all turn restrictions, one-way

# Routing Optimization

![](/api/attachments/VDNMEP68/fulltext/images/bfa254ed7278ed67bf5c1ebf4427144f61ed38f10a5a79773237641953a1cdfd.jpg)  
Fig. 2. “Edit networks” menu and “Create arcs” panel (left-hand sidebar).

Final point: Lat:40.218863834488594 Lng:-8.422050476074218 Draw the arc Remove points

Arc length (m): 339 Arc time (min:s): 0:27 Service time (min:s): 0 :0 Arc demand (kg): 0

Type of the arc: ©Not oriented Oriented (as represented) Oriented (reversed)

streets, etc., are considered in the shortest path calculations by using real network data, as usually provided by GoogleMaps™. After being calculated, the shortest paths are stored in the database and are ready to be accessed at anytime by the heuristic and meta-heuristic algorithms embedded into the system.

After choosing “Solve problem” in the menu bar, data about trucks and crews must be entered in an editable table (on the left-hand sidebar area) where the user may add lines (Fig. 3). In this table, values as the number of types of trucks, the respective capacity, the shift time limit, and a real parameter (“Coeff”), which is used to differentiate the relative cost of each type of truck, are entered. In the area below the “Type of trucks” table, the user is allowed to choose either the minimization of total length or the minimization of the number of trucks to be used (see Fig. 3). A maximum CPU time allowed to obtain the solution by the system can also be de<sup>fi</sup>ned (a small value means the willingness to obtain a solution in a reduced computational time, with less iterations of the ant-colony metaheuristic, at the cost of an eventual degradation of the respective quality).

A route for a vehicle is constrained by the volume of trash it can carry (i.e., vehicle capacity) and the time it takes to serve the route (maximum employee shift time). A vehicle may serve more than one route in a day as long as the total routing time for the vehicle is less than the maximum employee shift time. The routing heuristic and meta-heuristic approaches embedded in the wSDSS enforce both the vehicle capacity and total service time constraints for each vehicle.

The situation in Coimbra is additionally complicated by the fact that the route drop off point (a land<sup>fi</sup>ll) is not located at the depot where the vehicles start and end their shifts. The <sup>fi</sup>rst route starts at the depot and all routes must go to the land<sup>fi</sup>ll when completed. However, only the last route in a given vehicle's shift must return to the starting depot. The routing heuristic embedded in the wSDSS incorporates these operational speci<sup>fi</sup>cations.

## 3.4. wSDSS output

The primary output of the wSDSS is the design of ef<sup>fi</sup>cient vehicle routes including the respective graphical representation on maps. The wSDSS determines the number of vehicles and routes, as well as designs the individual routes satisfying the actual constraints related to the vehicles (e.g., load limit), crews (e.g., length of an employee's work shift), and streets network (e.g., one-way streets and prohibited turns).

A solution is obtained by minimizing the total vehicles length traveled, adopting a value of 6-h shift limit (which re<sup>fl</sup>ects current policy). The output includes system-wide data and individual vehicle data and maps. Summary system-wide and individual vehicle information are presented in Table 1, produced by the system. The solution uses 2 pre-de<sup>fi</sup>ned types of vehicles with different capacities (type 1 and type 2) and requires four shifts (one shift for vehicle type 1, and three shifts for vehicle type 2).

# R out ing Optimization

![](/api/attachments/VDNMEP68/fulltext/images/86ac2ea6c0f87d891166cd711872fd1513badac243ea47b1c7db2d97f0ea5499.jpg)  
Fig. 3. Setting the <sup>fl</sup>eet characteristics and trucks data input (left-hand sidebar).

The choice of the option “Show routes” on the menu “Show results” displays a list with the routes on the left-hand sidebar; by clicking on a speci<sup>fi</sup>c route of that list, the route is displayed on the map (Fig. 4), where light color (orange) lines represent arcs on the route that do not include pickups, and dark color (red) lines represent served arcs of the displayed route. Route directions are also shown by the wSDSS listed on the right-hand sidebar of the main window. This list of directions also shows the expected accumulated length, load, and time for the route as it progresses from arc to arc. This allows the crew to determine if they are “on-schedule” in terms of time and capacity utilization.

A detailed zoom of the corresponding location is shown in a box on the map (a detailed zoom of location 9 is represented in Fig. 5) by clicking on a number of the sequence of directions (on the right-hand sidebar).

## 4. Results and discussion

Sensitivity and what-if analysis are generally required in complex decision problems. In vehicle routing problems it is usually interesting to obtain answers about the impact of changes on the required resources (e.g., duration of the crews' work shift, capacities of vehicles

Global system summary and individual vehicle information: Solution S1 (minimizing total length, shift limit=6 h).

<table><tr><td colspan="11">Objective: Minimization of the total length</td></tr><tr><td>Truck type</td><td></td><td></td><td>Capacity</td><td></td><td></td><td></td><td>Shift limit (h:min)</td><td></td><td></td><td>Coefficient</td></tr><tr><td>1</td><td></td><td></td><td>16 (m3)|10500 (kg)</td><td></td><td></td><td></td><td>6:00</td><td></td><td></td><td>1</td></tr><tr><td>2</td><td></td><td></td><td>20 (m3)|13125 (kg)</td><td></td><td></td><td></td><td>6:00</td><td></td><td></td><td>1</td></tr><tr><td></td><td>Total</td><td>Route 1</td><td>Route 2</td><td>Truck type 1</td><td>Route 3</td><td>Truck type 2</td><td>Route 4</td><td>Truck type 2</td><td>Route 5</td><td>Truck type 2</td></tr><tr><td>Duration (h:min)</td><td>18:36</td><td>1:21</td><td>4:23</td><td>5:44</td><td>4:22</td><td>4:22</td><td>3:49</td><td>3:49</td><td>4:41</td><td>4:41</td></tr><tr><td>Service (kg)</td><td>52515</td><td>4338</td><td>10324</td><td>14662</td><td>12795</td><td>12795</td><td>12244</td><td>12244</td><td>12814</td><td>12814</td></tr><tr><td>Route length (m)</td><td>276725</td><td>24660</td><td>64987</td><td>89647</td><td>63530</td><td>63530</td><td>56748</td><td>56748</td><td>66800</td><td>66800</td></tr><tr><td>Serviced length (%)</td><td>25</td><td>17</td><td>23</td><td>22</td><td>27</td><td>27</td><td>30</td><td>30</td><td>23</td><td>23</td></tr><tr><td>Average speed (km/h)</td><td>15</td><td>18</td><td>15</td><td>16</td><td>15</td><td>15</td><td>15</td><td>15</td><td>14</td><td>14</td></tr></table>

# Rout ing Optimization

Truck type 1

Truck type 2

Serviced arc

![](/api/attachments/VDNMEP68/fulltext/images/bc29dfe73b9a0532cf26b43fcab5fbd99056a1e4273e544dfd95abd5a6ac1554.jpg)

<table><tr><td colspan="2">8. Na rotunda, 0,1 km seguir pela2.a saídapara R.Teófilo Braga</td></tr><tr><td>[7CHE]</td><td>Accum. values</td></tr><tr><td>Shift length (km)</td><td>4</td></tr><tr><td>Shift time (h:min)</td><td>0:8</td></tr><tr><td>Route demand (kg)</td><td>68</td></tr><tr><td>[6vow]</td><td>R. Teófilo Braga</td></tr><tr><td colspan="2">32 m (acerca do 5 seg.)</td></tr><tr><td colspan="2">1. Seguir 12 msudeste emfrente R.Teófilo Braga</td></tr><tr><td colspan="2">2. Curva ligeira 20 mà direita</td></tr><tr><td colspan="2">Estrada desconhecida</td></tr><tr><td colspan="2">Dados do mapa © 2008 Tele Atlas</td></tr><tr><td>[6vow]</td><td>Accum. values</td></tr><tr><td>Shift length (km)</td><td>4.1</td></tr><tr><td>Shift time (h:min)</td><td>0:9</td></tr><tr><td>Route demand (kg)</td><td>107</td></tr></table>

Fig. 4. Zoom of route 1.

and respective costs), or on the network (e.g., modifying traversal times or temporarily deleting arcs that become not available for truck access during road maintenance or other causes). The urban trash collection system planner may want to evaluate if changes in vehicle capacity and/or shift times affect the number of vehicles and routes required. The analysis of such trade-offs are important in the management of vehicle <sup>fl</sup>eets and required manpower. In our example, results were obtained (solution S1) by solving the problem with a shift limit of 6 h (Table 1) for two types of vehicles with different capacities. Five routes were generated, organized in three shifts for vehicle type 2 and one shift for vehicle type 1. The objective was the minimization of the total traveled vehicle length.

Solving again the problem by minimizing the number of trucks instead the total traveled length (with the remaining parameters unchanged), a similar solution to S1 (in terms of total length traveled, number of required shifts, and vehicles) was obtained (solution S2) with <sup>fi</sup>ve routes, organized in four shifts (one for vehicle type 1, and three for vehicle type 2). However, increasing the shift limit from 6 to 7 h, a different solution (S3) was obtained, with <sup>fi</sup>ve routes organized in three shifts (one for vehicle type 1, and two for vehicle type 2), with a slightly higher total length traveled (+1,2 %); see Table 2. In all the three solutions mentioned above equal costs were assumed for both vehicle types. Maintaining the shift limit of 6 h, minimizing the total traveled vehicle length and considering vehicle type 2 with a relative cost 50% higher than the cost of vehicle type 1, the system generates a solution with <sup>fi</sup>ve shifts using only vehicle type 1. In this case, the total traveled vehicle length obtained was 9% higher than in S1.

The analysis shows that utilizing 7-h shifts the network could be served by three shifts instead of four required by the current 6- h shifts. This change would require paying overtime to three crews but would require one less crew and one less vehicle. Thus, the system provides the planners relevant information for analyzing cost and reliability issues (i.e., less <sup>fl</sup>exibility in dealing with demand <sup>fl</sup>uctuation as there is less slack capacity in the system) associated with such a change.

As demonstrated, the implemented wSDSS can be used for both short-term analysis (e.g., the design of daily vehicle routes) and longterm analysis (e.g., how many vehicles to operate), only requiring an Internet browser.

## 5. Summary and conclusions

A web-based decision support system (wDSS) prototype using GoogleMaps™ and incorporating state-of-the-art heuristics and meta-heuristic approaches developed by the authors was presented. The wDSS was designed to be entirely accessed via an Internet browser. Several features make the system an innovative coupling of sound algorithmic approaches with modern information and communication technologies:

1. It extends a well-known routing problem (the CARP) by incorporating realistic system speci<sup>fi</sup>cs (such as shift time constraints, the possibility of considering the “drop-off point” not at the same location as the depot where the vehicles start and end their shifts),

# R o ut i n g O ptim i z a t i on

![](/api/attachments/VDNMEP68/fulltext/images/a1024e2a55d13dbfa374dce2a0c9dd1b156f7f9b1bba36ee961d45eafa156903.jpg)

<table><tr><td colspan="2">8. Na rotunda, 0,1 kmseguir pela2.a saídapara R.Teófilo Braga</td></tr><tr><td colspan="2">B R. Teófilo Braga</td></tr><tr><td colspan="2">Dados do mapa ©2008 Tele Atlas</td></tr><tr><td colspan="2">1 Accum. valuesShift length (km) 4Shift time (h:min) 0:8Route demand (kg) 68</td></tr><tr><td colspan="2">A R. Teófilo Braga32 m (acerca do 5 seg.)</td></tr><tr><td colspan="2">1. Seguir 12 msudeste emfrente R.Teófilo Braga</td></tr><tr><td colspan="2">2. Curva ligeira 20 mà direita</td></tr><tr><td colspan="2">B Estrada desconhecidaDados do mapa ©2008 Tele Atlas</td></tr><tr><td colspan="2">2 Accum. valuesShift length (km) 4.1Shift time (h:min) 0:9Route demand (kg) 107</td></tr></table>

Fig. 5. Speci<sup>fi</sup>c direction (selected on the right-hand side bar) highlighted on the map

and network constraints such as one-way streets and prohibited turns.

2. It requires only an Internet browser to be used that allows remote access to cartography, networks data, and algorithms via the web.

3. It uses state-of-the-art methodologies for routing problems previously developed by the authors [4,24,25], which were adapted to accommodate additional conditions/constraints of real-world routing problems.

4. It accesses maps and streets network data provided by Google Maps™ services and represents solutions (routes) graphically on

Google Maps™ cartography with lists of directions and the sequence of streets as they are traveled by the vehicle, displaying accumulated length, load, and time for the route as it progresses from arc to arc.

Although the SDSS was tested for an urban trash collection situation, which is an important actual problem in modern cities, it can be adapted to be used in other real-world problems of capacitated routing (e.g., street sweeping, snow cleaning vehicles, door-to-door collection/ delivery of goods, and inspection of streets or other infrastructures).

Global system summary and individual vehicle information: Solution S3 (minimizing nr of trucks, shift limit=7 h).

<table><tr><td colspan="10">Minimization of the nr. of trucks</td></tr><tr><td>Truck type</td><td colspan="4">Capacity</td><td colspan="3">Shift limit (h:min)</td><td colspan="2">Coefficient</td></tr><tr><td>1</td><td colspan="4">16 (m3)|10500 (kg)</td><td colspan="3">7:00</td><td colspan="2">1</td></tr><tr><td>2</td><td colspan="4">20 (m3)|13125 (kg)</td><td colspan="3">7:00</td><td colspan="2">1</td></tr><tr><td></td><td>Total</td><td>Route 1</td><td>Truck type 2</td><td>Route 2</td><td>Route 3</td><td>Truck type 2</td><td>Route 4</td><td>Route 5</td><td>Truck type 1</td></tr><tr><td>Duration (h:min)</td><td>18:36</td><td>5:24</td><td>5:24</td><td>3:28</td><td>3:24</td><td>6:52</td><td>3:28</td><td>2:52</td><td>6:20</td></tr><tr><td>Service (kg)</td><td>52515</td><td>12460</td><td>12460</td><td>12409</td><td>9625</td><td>22034</td><td>10420</td><td>7601</td><td>18021</td></tr><tr><td>Route length (m)</td><td>280031</td><td>73393</td><td>73390</td><td>46226</td><td>59392</td><td>105618</td><td>46225</td><td>54795</td><td>101020</td></tr><tr><td>Serviced length (%)</td><td>24</td><td>27</td><td>27</td><td>30</td><td>22</td><td>25</td><td>28</td><td>16</td><td>21</td></tr><tr><td>Average speed (km/h)</td><td>15</td><td>14</td><td>14</td><td>13</td><td>17</td><td>15</td><td>13</td><td>19</td><td>16</td></tr></table>

## References

[1] L. Alçada-Almeida, L. Tralhão, L. Santos, J. Coutinho-Rodrigues, A multiobjective p median modeling approach to locating shelters and evacuation routes fo emergencies in urban areas, Geographical Analysis 41 (1) (2009) 9–29.

[2] D. Banister, R. Hickman, How to design a more sustainable and fairer built environment: Transport and communications, IEE Proceedings: Intelligent Transport Systems 153 (4) (2006) 276–291.

[3] H.K. Bhargava, D.J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems 43 (4) (2007) 1083–1095.

[4] J. Coutinho-Rodrigues, N. Rodrigues, J. Clímaco, Solving an urban routing problem using heuristics: A successful case study, International Journal of Computer Applications in Technology 6 (2–3) (1993) 176–180.

[5] J. Coutinho-Rodrigues, J. Current, J. Climaco, S. Ratick, An interactive spatial decision support system for multiobjective HAZMAT location-routing problems Transportation Research Record 1602 (1997) 101–109.

[6] L. Dablanc, Goods transport in large European cities: Dif<sup>fi</sup>cult to organize, dif<sup>fi</sup>cult to modernize, Transportation Research Part A 41 (3) (2007) 280–285.

[7] EPA, Our Built and Natural Environments: Interactions between Land Use, Transportation, and Environmental Quality, United States Environmental Protection AgencyEPA 231-R-01-002, 2001 (Available online at), http://www.epa.gov/ smartgrowth/pdf/built.pdf.

[8] E. Ericsson, H. Larsson, K. Brundell-Freij, Optimizing route choice for lowest fuel consumption: Potential effects of a new driver support tool, Transportation Research Part C 14 (6) (2006) 369–383.

[9] M.R. Garey, D.S. Johnson, Computers and intractability: A guide to the theory of NP-completeness, W.H. Freeman, New York, 1979.

[10] B.L. Golden, R.T. Wong, Capacitated arc routing problems, Networks 11 (3) (1981) 305–315.

[11l Z. Hans R. Souleyrette GIS and network models: Issues for three potentia applications Journal of Advanced Transportation 29 (3) (1995) 355–373.

[12] M.K. Jha, P. Schonfeld, A highway alignment optimization model using geographic information systems, Transportation Research Part A 38 (6) (2004) 455–481.

[13] S. Kenyon, The impacts of Internet use upon activity participation and travel: Results from a longitudinal diary-based panel study, Transportation Research Part C 18 (1) (2010) 21–35.

[14] M.P. Kwan, M. Dijst, T. Schwanen, The interaction between ICT and human activity–travel behavior, Transportation Research Part A 41 (2) (2007) 121–124.

[15] MacroSys Research and Technology, Logistics Costs and U.S. Gross Domestic Product. Federal Highway Administration Department of Transportation8 Available online at, http://ops.fhwa.dot.gov/freight/freight\_analysis/econ\_methods lcdp\_rep/index.htm20058Accessed 25/8/2008.

[16] T.L. Magnanti, R.T. Wong, Network design and transportation planning: Models and algorithms, Transportation Science 18 (1) (1984) 1–55.

[17] J. Maria, J. Coutinho-Rodrigues, J. Current, Interactive destination marketing system for small- and medium-sized tourism destinations, Tourism: An Interdisciplinary Journal 53 (2005) 45–54.

[18] P.A.L. Matos, P.L. Powell, Decision support for <sup>fl</sup>ight re-routing in Europe, Decision Support Systems 34 (4) (2002) 397–412.

[19] J.E. Mendoza, A.L. Medaglia, N. Velasco, An evolutionary-based decision support system for vehicle routing: The case of a public utility, Decision Support Systems 46 (3) (2009) 730–742.

[20] Z.R. Peng, R. Huang, Design and development of interactive trip planning for webbased transit information systems, Transportation Research Part C 8 (1–6) (2000) 409–425.

[21] J.J. Ray, A web-based spatial decision support system optimizes routes for oversize/overweight vehicles in Delaware, Decision Support Systems 43 (4) (2007) 1171–1185.

[22] L. Santos, J. Coutinho-Rodrigues, J.R. Current, An improved solution algorithm for the constrained shortest path problem, Transportation Research Part B 41 (7) (2007) 756–771.

[23] L. Santos, J. Coutinho-Rodrigues, J.R. Current, Implementing a multi-vehicle multiroute spatial decision support system for ef<sup>fi</sup>cient trash collection in Portugal, Transportation Research Part A 42 (6) (2008) 922–934.

[24] L. Santos, J. Coutinho-Rodrigues, J.R. Current, An improved heuristic for the capacitated arc routing problem, Computers and Operations Research 36 (9) (2009) 2632–2637.

[25] L. Santos, J. Coutinho-Rodrigues, J.R. Current, An improved ant colony optimization based algorithm for the capacitated arc routing problem, Transportation Research Part B 44 (2010) 246–266.

[26] A. Simão, J. Coutinho-Rodrigues, J. Current, A management information system for urban water supply networks, ASCE Journal of Infrastructure Systems 10 (4) (2004) 176–180.

[27] P. Tapio, D. Banister, J. Luukkanen, J. Vehmas, R. Willamo, Energy and transport in comparison: Immaterialisation, dematerialisation and decarbonisation in the EU15 between 1970 and 2000, Energy Policy 35 (1) (2007) 433–451.

[28] J.C. Thill, Geographic information systems for transportation in perspective, Transportation Research Part C 8 (1–6) (2000) 3–12.

[29] F. Űlengin, Ş. Őnsel, Y. Topçu, E. Aktaş, K. Őzgur, An integrated transportation decision support system for transportation policy decisions: The case of Turkey, Transportation Research Part A 41 (1) (2007) 80–97.

[30] J. Woodcock, D. Banister, P. Edwards, A.M. Prentice, I. Roberts, Energy and transport, Lancet 370 (9592) (2007) 1078–1088.

Luis Santos is currently working in the Innovation Department of ISA (Intelligent Sensing Anywhere), Coimbra, Portugal. He received his Licenciate degree in applied mathematics (1995), his MSc degree in civil engineering/urban engineering (2000) and his PhD degree in civil engineering/urban, land use and transportation planning (2009) from the University of Coimbra. He has been a researcher at the Institute for Systems Engineering and Computers (INESC) since 1997. His research interests include spatial decision support systems, network design and optimization, vehicle routing, and transportation. He has published in scienti<sup>fi</sup>c journals such as Transportation Research (Part A and Part B), Computers and Operations Research, and Geographical Analysis.

João Coutinho-Rodrigues is currently a professor in the Department of Civil Engineering, Faculty of Sciences and Technology, University of Coimbra (where he has been since 1980) and a senior researcher in the Decision Support in Systems Engineering Group at INESC, Coimbra. He received his Licenciate degree in Civil Eng., his MSc degree in computer science and his PhD degree in civil eng. from the University of Coimbra. His research interests include decision support systems, multicriteria analysis, networks, GIS, and applications in urban/environmental/transportation engineering. He has published, among other journals, in Computers and Operations Research, Decision Support Systems, International Journal of Computer Applications in Technology, Journal of Business Logistics, Journal of Infrastructure Systems—American Society of Civil Engineers, Municipal Engineer, Transportation Research (Part A and Part B), Transportation Research Record, Geographical Analysis, Socio-Economic Planning Sciences, Water Power and Dam Construction.

Carlos Henggeler Antunes received the PhD degree in electrical engineering (optimization and systems theory) from the University of Coimbra. Coimbra. Portugal. in 1992. He is a professor in the Department of Electrical Engineering and Computers, University of Coimbra, and the director of the R&D Unit, INESC, Coimbra. His research interests include multiple objective programming, decision support systems, and energy planning.
