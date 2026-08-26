---
otero_id: 22003
otero_key: "XNPKNUQY"
title: "Using a spatial decision support system for solving the vehicle routing problem"
authors: "C.D Tarantilis; C.T Kiranoudis"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00103-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using a spatial decision support system for solving the vehicle routing problem

\* C.D. Tarantilis, C.T. Kiranoudis

Section II: Process and Systems Analysis, Design and Development, Department of Chemical Engineering, Zografou Campus, National Technical University of Athens, Iroon Polytexneou 9, GR 157 80 Athens, Greece

Received 30 March 2000; received in revised form 27 December 2000; accepted 02 May 2001

## Abstract

Recent technological advances in Operational Research and Information Technology have enabled the development of high quality spatial decision support systems (SDSS). They constitute a new scientific area of information systems applications developed to support semi-structured or unstructured decisions, paying much attention to the spatial dimension of data to be analyzed, such as the location and shape of, and relationships among, geographic features. This paper presents a SDSS to coordinate and disseminate tasks and related information for solving the vehicle routing problem (VRP) using a metaheuristic method termed: backtracking adaptive threshold accepting (BATA). Its architecture involves an integrated framework of geographical information system (GIS) and a relational database management system (RDBMS) equipped with interactive communication capabilities between peripheral software tools. The SDSS was developed for Windows 98 platforms, focusing on the detailed road network of Athens. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Geographical information systems; Spatial decision support systems; Vehicle routing problem; Logistics management

## 1. Introduction

This paper presents a spatial decision support system (SDSS) to coordinate and disseminate tasks and related information for solving the vehicle routing problem (VRP) using a metaheuristic method termed backtracking adaptive threshold accepting (BATA).

In this important problem, a fleet of homogeneous vehicles with a fixed carrying capacity, located on a central depot, must deliver order quantities of the same or different products, to a number of customers.

If the distance between each pair of customers is known, the problem is to find vehicle tours in such a way that:

 The total distance traveled by the vehicles is minimized.

 The capacity of a vehicle cannot be exceeded.

 A single vehicle supplies each customer’s demand.

The number of vehicles is unlimited, meaning that the SDSS can handle an unlimited number of customers. The capacity of vehicles and the demand of the products are defined by record files in the database. In order to order products, customers place ‘‘on-line’’ via a Web page.

The architecture of the SDSS involves an integrated framework of geographical information system (GIS) technology equipped with interactive communication capabilities between peripheral software tools. Its rationale is based on the development of a distributed environment for the integration of software applications that share data and operations through a common database repository and which can support a large-scale organization’s manipulation and retrieval of data. This effort is chiefly based on careful definitions of data type objects and the construction of focused methods to manipulate them. In fact, there are many opportunities presented by such a system for new, current and future users. They benefit from the consistent behavior and feel of the system, minimizing frustration and time-spent in learning the mechanical aspects of the programs, since similar user interfaces are implemented to all tasks. By using and developing focused applications for specific object types, users and programmers alike benefit from an increase in application reusability.

The structuring of the data, assure the programmer that only specific object types are available. This allows applications to grow and develop or remain operational even if the object definitions evolve and change. The use of objects even protects the user from having to know the differences between diverse applications that perform the same function. Future users benefit because the consistency imposed upon a project allows history maintenance and retrieval mechanisms to be incorporated. Users can also take advantage of the information obtained from an old project in any new project developments.

The SDSS manages to overcome efficiently the technical and managerial difficulties faced during the implementation of the system with ad hoc connections between the GIS, the evolving database management system (DBMS), and the routing methods used for calculating the shortest paths between all pairs of customers and routing plans.

## 2. The evolution of the vehicle routing systems (VRS)

In the mid-1960s, VRP solutions were based on non-computerized methods, where routes were designed manually by using paper maps that provide locations of customers to be routed as geographical reference points. By the early 1970s, vehicle routing heuristics [13,15,18,24,39,40] were used to produce routes together with skilled manual intervention by experienced routing decision makers who had considerable knowledge of local condition and of the relative importance of the various constraints. From the early 1980s every VRS was seen as a decision support system (DSS), due to its links to the database management system in order to organize large amounts of data (customer specific orders, size of the vehicle fleet, etc.) and the use of a visual interface needed to support problem specific decisions [1,4–7,20,28,31,32,35].

During the same time period, the area of IS gave birth to systems for analyzing, storing and displaying spatially or geographically related data. These systems were generally implemented on UNIX workstations and termed GIS [29]. However, the vehicle routing DSSs of that period started by integrating geographical data and focusing on spatial dimension of the VRP by linking to external information sources, such as public mapping agencies and raster images of paper maps [8]. The growth of GISs was rapid in the 1990s when personal computers became powerful and capable of supporting such systems and the increasing volume of digital spatial data became available [12,21,26,33,34]. However, the traditional GIS could not support routing efficiently since it provided routines only for finding shortest paths Even today only a limited number of GIS products provide more effective routing techniques, thus, increasing the need for developing DSSs that will incorporate effective methods for solving real life (large) vehicle routing problems, combined with spatial techniques drawn from the field of GIS [9, 10,37]. Such systems are characterized as VRP– SDSS and they support semi-structured or unstructured vehicle routing decision making by displaying features such as road network, administrative boundaries, complex path constraints, paying much attention on spatially referenced data [11,27,38]. At this point, it is important to make clear that pure spatial data refers to information stored on maps and to information about the relationships of entities in space while spatially referenced data refers to thematic or applied data such as customer addresses coded by ZIP code or vehicle routes designed by street address [17].

## 3. Distributed component software

The architecture of the SDSS is based on distributed component software. Distributed environments for the integration of software applications that share a common database repository, encourages the development of small tightly focused applications that perform specialized tasks. This allows the re-use of software components and the development of a consistent user interface. The creation of huge and monolithic applications is avoided, enabling the development of more adaptable tools. There is also the possibility of synergy being developing through the use of many small tools. These use an architecture and application dependent object format to achieve an integrated environment. The use of object oriented techniques allows users to tailor the system to their demands and needs. Distributed software systems, allow project managers to divide a project, yet still maintaining the integrity of the whole. Different people or groups can each be given a particular part of the project, and be able to work on it independently of others. Each team member, however, can access other people’s work through the facilities provided by the system.

## 4. The architecture of the SDSS

The architecture of the SDSS is shown in Fig. 1; it consists of five modules:

 The geographical information system (GIS).

 The database management system (DBMS) (Microsoft SQL Server).

 The network analysis tool (NAT).

 The vehicle routing optimization tool (VROT).

 The user interface.

The GIS is characterized by the interactive communication to a DBMS and individual software tools that perform all necessary numerical calculations, and all cartographical and graphical tasks related to a VRP. The GIS used (ESRI ArcView GIS) is the background information system of the SDSS, since it includes all the necessary cartographic information, etc. The cartographic information is derived from general maps, updated with suitable photogrammetric methods, with various levels of analysis and accuracy. The development platform was Windows 98 for PCs.

The DBMS (Microsoft SQL Server) is the heart of the SDSS; it has a two-fold role. Within its relational infrastructure are stored, regional and operational, spatial and non-spatial data related to depot and customers with their addresses, as well as the road network, road maps, and transportation facilities of the region. In addition, it serves as the common repository of all tools to store and exchange data within each application. In particular, each tool retains its own part of the database for interaction with the user. The level and complexity of database transparency to each tool depends on the access privileges of each application for each specific task.

The NAT determines the shortest paths, expressed in terms of distance traveled, within a specific road network.

The VROT uses BATA to determine the best routing plan (which vehicle should deliver to which customers and in which order), minimizing simultaneously the total distance traveled by vehicles.

The user interface is the only module visible to user. Many research studies in the past have underlined the role of the interface in comprehension and acceptability of a SDSS [30]. The interface of the SDSS allows user to interact with data and methods used to solve VRP while it transforms user query and update requests into appropriate sequences of commands to the other modules. The transformation of a user query is achieved by providing parameters in predefined queries, while it allows the updating of forms and the direct manipulation of data by simply clicking on the appropriate interface buttons.

## 5. Data management of the SDSS

Data management plays major role in the function ing of the distribution system. This role becomes more important when the system is large, with a detailed road network like that of Athens, as demonstrated in Fig. 2.

In order to produce the proposed routing plan, the SDSS uses information about:

 The locations of the depot and the customers within the road network of Athens (their coordinates in the map of Athens).

![](/api/attachments/XNPKNUQY/fulltext/images/d649d94feb4e13d74af44f2da75589df17667336359c42712c9fcc2b6bf81430.jpg)  
Fig. 1. The architecture of data exchanged within the SDSS.

 The customer demand.

 The capacity of the vehicles.

 The spatial characteristics of road segments of the network.

 The topography of the road network.

 The speed of the vehicle, considering the characteristics of the road and the area within which it moves.

The combination of geometric/cartographic and quality/descriptive data, derived from the analysis of the detailed network of Athens, is collected, manipulated and visualized by the SDSS.

Consequently, the SDSS combines, in real time, the available spatial data, tools for modeling, spatial, nonspatial, and statistical analysis mechanisms, image processing, etc. thus, forming a scalable, extensible and inter-operable application environment.

![](/api/attachments/XNPKNUQY/fulltext/images/1e6bdf1b94078a73ddaefc63aadff0d94459c56afb271a8c078ff279075d2dd4.jpg)  
Fig. 2. The road network of the Athens.

## 6. Planning and development of the spatial decision support system

The SDSS workflow consists of three business functions.

## 6.1. Validation and verification of addresses of customers

The validation and verification of addresses of customers helps to provide an accurate estimation of travel times or distances traveled. In the case of the bound in the total route duration, underestimates of travel time may lead to failure of the programmed routing plan whereas overestimates can lower the efficiency of the use of drivers and vehicles, and create unproductive waiting times also [2].

## 6.2. Development of economical vehicle routes

## 6.2.1. Maintenance of routing data

The SDSS consists of a Central Database, representing cartographic information and communicating with tools for entering and manipulation data.

## 6.2.2. Analysis and representation of spatial information

The software for spatial analysis and representation of cartographic information is the Desktop ESRI Arc-View GIS 3.0. The demand for accuracy and level of detailed representation of the data depends on the specific task. The depot, customer, vehicle and other characteristics must be entered with an accuracy of about 1:500 or 1:1000. The surrounding areas of depot and customers and the neighboring activities need less accuracy of the scale 1:2000–1:5000. Consequently, the best solution is a combination of them, with an emphasis on the application of digital photogrammetric methods either for updating extant maps or for compiling new ones.

It is exactly because high accuracy is sometimes needed in small parts of whole area that the possibility of applying simple photogrammetric methods. After that, more detailed and accurate spatial information can be added to the particular points of interest, by applying more complicated methods, such as stereoplotting using large-scale airphotos or even terrestrial measurements. Such information is represented in the graphical environment of the ArcView software:

 At the first level, the whole of the road network of interest.

 At the second level, the neighborhood of a customer or depot.

 At the third level, the diagram of the installation of the depot and the customers.

## 6.2.3. Use of routing tools

The main tools that have been developed for the SDSS are:

 The NAT, which provides solutions to problems of effectively determining shortest paths, expressed in terms of distance traveled, within a specific road network, using Dijkstra’s algorithm. This is used in two phases during the process of determining the routing plan.

 First, Dijkstra algorithm computes the shortest paths between all possible pairs of depot and customers, so that BATA will find the best routes connecting them. The objective of the VRP is to find the best vehicles routes, knowing the travel distances between all possible pairs of nodes.

 Second, it determines the shortest path between two nodes (depot or customer) in the best routing plan, as determined by BATA previously. The GIS performs all graphical tasks, such as roads, road intersections, locations of the depot and customers, etc. Attributes such as the type and condition of the road, the population density of each urban block, etc. are supplied by the DBMS.

 The VROT, which uses BATA to determine the best routing plan (which vehicles should deliver to which customers and in which order), minimizing the total distance traveled by the vehicles.

## 6.3. Strategic analysis and representation of a vehicle routing plan

This process involves activities that tend to be strategic and less structured than the operational procedures. The SDSS helps planners and managers view information in a new way and examine issues, such as:

 Average cost per vehicle, and route.

 Vehicle and capacity utilization.

 Service level and cost.

 Modification of the existing routing scenario by adding or subtracting customers, etc.

The interface of the SDSS provides a variety of analyzed geographic data capabilities. Moreover, it can represent each vehicle route separately, cutting it out of the final routing plan and allowing the user to see the road network and locations of the depot and customers in full detail.

## 7. Technical management of the spatial decision support system

## 7.1. Connections between the GIS and DBMS

The ‘‘translation’’ of a polyline geographical object from GIS coordinates into a DBMS node and link uses entity relationship diagram (ERD), shown in Fig. 3, written in a related Avenue script. Each polyline object is characterized by an up-stream and a downstream node, its length, name, transport and traffic characteristics.

![](/api/attachments/XNPKNUQY/fulltext/images/3391ec95479b3a32ffce576e2e758ebfc39196e4b6830a68331acdc79a453925.jpg)  
Fig. 3. The entity relationship diagram.

For up-stream and down-stream nodes:

If node (x, y) exists in node table of the DBMS then select its maximum primary key from node table of the DBMS else insert into the node table the node (x, y) and get its primary key.

For links, after repeating the same procedure for both the up-stream node and down-stream node of the selected link:

Insert a new link entity that has as up-stream node primary key and down-stream node primary key the numbers retrieved as mentioned above. Insert also all link characteristics.

The transformation process for a customer or depot of the network is slightly different.

Select the closest node to the customer or depot we want to transform by calculating their distance. Insert the selected customer into the Customer table of the DBMS

## 7.2. Connections between the DBMS and routing methods

After translating the digital physical network into the mathematical network, we have to represent the network in a Cþþ structure (see Fig. 4). The way that an input network is represented is vital to the performance of the routing methods. Our representation describes the connection between the nodes of the network in the forms of arrays of nodes. The rationale is to transfer the content of the Node table in an array of nodes and then, for every node of this initial array, to search for the nodes to which the selected node points. This operation is carried out by selecting the links that have the same up-stream node primary key with the selected node of the initial array of nodes. Since the Link table also contains the down-node primary key of each link, we get information about the nodes to which the selected node points. After defining those nodes we transfer them into an array, and the same procedure is repeated until we form similar arrays for every node of the initial array.

A matter of interest is the implementation of Dijkstra algorithm. The algorithm begins at the specified node, termed the ‘‘source’’. Each node can be in a permanently, or temporarily labeled state or in an unreached state. The permanently and the temporarily labeled nodes are placed in two different arrays. The output of this algorithm is the shortest paths from the source node to all other nodes. Repeated application of this method, though each node of the network finds the shortest path tree associated with each and every one of the network’s nodes.

## 7.3. Finding the shortest path

Step 1: The arrays of permanently and the temporarily labeled nodes are empty. Consider the source node s as permanently labeled. Store the source node in the array of permanently labeled nodes.

![](/api/attachments/XNPKNUQY/fulltext/images/ba8dca23e55fd2048e11dafade111b302969835e3625a1c0e32c2d411126a457.jpg)  
Fig. 4. Cþþ network representation.

Step 2: Examine all links $( s _ { \mathrm { N } } , j )$ out of the source node.

 If node j is permanently labeled, go to the next link.

 If node j is unreached, then set label ðjÞ ¼ label ðpredecessorÞ þ length (predecessor, j), and store it in the array of the temporarily labeled nodes.

 If j is temporarily labeled, then set label ðjÞ ¼ min {label (j), label ðpredecessorÞ þ length (predecessor, j)}, and store in the array of the temporarily labeled nodes.

Step 3: Select the minimum labeled node from the array of the temporarily labeled nodes and remove it to the array of the permanently labeled nodes. Repeat the same procedure, characterizing the minimum labeled node as $s _ { \mathrm { N } } .$ , until the array of the temporarily labeled nodes becomes empty. The output of this procedure is the array of the permanently labeled nodes.

Using this method, the computational performance of the shortest path procedure is very efficient since the algorithm checks just the array of the temporarily labeled nodes. Characteristic of this excellent performance is that the algorithm finds the shortest paths from one to all other nodes of network, in 0.02 s. for a typical road network of 10 000 roads.

## 8. Backtracking adaptive threshold accepting (BATA) method

In the late 1970s, several algorithms were developed for solving VRP for very small numbers of variables and constraints [3,14,22,23,25]. Later, since exact algorithms did not perform well for large numbers of nodes, mainly due to computational complexity, many researchers focused on heuristic methods that searched for near optimal solutions at a reasonable computational cost, without any guarantees of optimality.

The classic heuristics used to improve a vehicle routing plan are the tour improvement procedures. These can improve a VRP solution by introducing changes in the plan, taking a node (customer) from its position in the routing plan and moving it to another position in the same or different vehicle routes. These methods are also characterized as local search methods because they involve initialization of the solution search space with some arbitrary solution (a routing plan) and then they proceed to try to improve it by successively moving from the current solution to a neighboring one. This is derived when an exchange of edges (road segments) or nodes (customers) converts one tour into another by using just a single move.

The methods used by BATA are the 2-Opt [16], 1-1 and 1-0 Exchange [36].

## 8.1. 2-Opt move

Suppose a single route consists of the following set of nodes $\Nu _ { 1 }$ in the given order $\bullet _ { 1 } = ( 0 , 1 , \ldots , k , 0 )$ , and let $A _ { 1 } = \{ ( i , i + 1 ) ; ( j , j + 1 ) \}$ g be a set of two edges in $\Nu _ { 1 }$ that form a criss-cross. 2-Opt move eliminates any criss-cross and reverses a section of the route by deleting the branches $( i , i + 1 ) , ( j , j + 1 )$ and replacing them with its supplement $( i , j ) , ( i + 1 , j + 1 )$ to reconstruct the route. In multiple routes, edges $( i , i + 1 )$ and $( j , j + 1 )$ belong to different routes but they again form a criss-cross. 2-Opt move is applied exactly in the same way as in the case of multiple routes. This is demonstrated in Fig. 5(a).

## 8.2. 1-1 Exchange move

This move swaps two nodes from either the same or different routes. Consequently, if the initial tour consists of the set of nodes $( 0 , \ldots , i - 1 , i , i + 1 , \ldots ,$ $j - 1 , j , j + 1 , \dots , 0 )$ , the improved one is constructed as $( 0 , \ldots , i - 1 , j , i + 1 , \ldots , j - 1 , i , j + 1 , \ldots , 0 )$ The same procedure is conducted in the case of multiple routes. This is demonstrated in Fig. 5(b).

## 8.3. 1-0 Exchange move

?This move transfers a node from its position in one route to another in either the same or a different route. Consequently, while the initial tour is $( 0 , \ldots , i , i +$ $1 , \dots , j - 2 , j - 1 , j , j + 1 , \dots , 0 )$ , the improved one is constructed as $( 0 , \ldots , i , j , i + 1 , \ldots , j - 2 , j - 1 , j +$ $1 , \ldots , 0 )$ . This is demonstrated in Fig. 5(c).

These moves are continually used to improve the solution until it is ascertained that no move can give an improved vehicle routing plan (solution). So, supposing that $s ^ { \prime } \in N ( s )$ , where $N ( s )$ is the neighborhood of a solution s that contains all the solutions that can be reached by a single move termed as neighbors, no improvement can be made to the current solution s (routing plan) if

$$
c (s) \leq c (s ^ {\prime})\tag{1}
$$

$\forall s ^ { \prime } \in N ( s )$ . Then it is said that s is a local minimum of c, where c is the cost function of the problem. Since the tour improvement procedures terminate when a local optimum is reached, new methods were developed, termed metaheuristics, to solve hard combinatorial problems such as the VRP, achieving high computational speeds in producing good solutions and preventing the search from becoming trapped prematurely in a local optimum.

BATA is such a metaheuristic method based on threshold accepting rationale [19]. The main characteristic of this class of methods is that it can accept every move that leads to a new solution, which is not necessarily better, but not much worse than the current solution. More specifically, if s is the current solution, the proposed next solution $s ^ { \prime } \in N ( s )$ is accepted only if the move acceptance criterion

$$
c (s ^ {\prime}) - c (s) <   T _ {\mathrm{h}}\tag{2}
$$

is satisfied, where $N ( s )$ is the neighborhood of solution s and $T _ { \mathrm { h } } > 0$ is a control parameter, in the same units as the cost function, called threshold.

The definition of the threshold value plays an important role in preventing the search from becoming trapped prematurely in a local minimum. In fact, if there is no new proposed solution $s ^ { \prime } \in N ( s )$ (local minimum), then the value of the threshold can interfere with and transform the inequality (1) into (2), satisfying the move acceptance criterion, while at the same time allowing the method to perform a local search, thus, seeking better solutions. In addition, it is worth observing that in the inequality constraint (2) the value of the threshold determines the size of the variation between the proposed and the current solution. Therefore, during the optimization process the threshold is gradually lowered in such a way that a move that would make the current solution much worse is never accepted.

![](/api/attachments/XNPKNUQY/fulltext/images/4a6dc7002a7eea41467c5eba2b3ab34d1521b4b787d1428fc0eea0fecb066e1c.jpg)  
2-Opt for single route  
(a)

![](/api/attachments/XNPKNUQY/fulltext/images/08ca9f9bf4a20060943627a833ca4e14d850fc26f79763ffea038c70a1a04506.jpg)  
2-Opt for multiple routes

![](/api/attachments/XNPKNUQY/fulltext/images/67943fbdcb0a8281ffdd7e469b28e507cb41a20717867d94d5120021cc1451fd.jpg)  
1-1 Exchange for single route  
(b)

![](/api/attachments/XNPKNUQY/fulltext/images/da55282e08f8baf95a3109db7263584188684e0ed15a39692d46200e35a89441.jpg)  
1-1 Exchange for multiple routes

![](/api/attachments/XNPKNUQY/fulltext/images/0f1d68497362e625c938221a76109c225c6df282272db14f5e0ddc120d607756.jpg)  
1-0 Exchange for single route  
(c)

![](/api/attachments/XNPKNUQY/fulltext/images/cd08de45e0db1dea2abd9ffb44c1284e483d49e7c5561520984d471dcf2b23cc.jpg)  
1-0 Exchange for multiple routes  
Fig. 5. 2-Opt, 1-1 and 1-0 Exchange moves.

The innovation of BATA over a typical threshold accepting method is based on the fact that the value of threshold is not only lowered but also raised, or backtracked, when the move acceptance criterion is not satisfied. It is noted that the backtracking is related to such levels that the increase of the threshold value during the backtracking procedure is always smaller than its previous one, before backtracking turned out to be necessary. The basic steps of BATA are given in Fig. 6.

## 8.3.1. Step 1 (initialization phase)

In the initialization phase, a positive value of threshold is selected $( T _ { \mathrm { h } } > 0 )$ , and BATA starts with an initial solution (routing plan) where each vehicle services only one customer.

![](/api/attachments/XNPKNUQY/fulltext/images/30e4096bb7969aea48f79dfd277169d90e9a8cf4ef2c960bc71d9c1d6d6da1ab.jpg)  
Fig. 6. BATA method.

## 8.3.2. Step 2

The second step is separated into two phases.

8.3.2.1. Phase 1. In this phase, a local search is conducted in the inner loop by using a blend of 2-Opt, 1-1 and 1-0 Exchange moves. These moves depend on the exchange of edges or nodes performed to convert one tour into another. BATA is a stochastic method, therefore, the selection of the type of the move used to conduct local search in the inner loop is made stochastically, though a stochastic move generation algorithm. The main characteristic of the move that conducts a local search in the inner loop of BATA is that it is ‘‘biased uniformly distributed’’. This means that their selection follows the uniform distribution, but that the percentage of use of each can be decided by the user. Finally, the customers involved in the implementation of the moves are also chosen stochastically.

The performance of a local search starts in the inner loop.

 After applying a feasible move in the inner loop and producing a new proposed solution s<sup>0</sup>, the move acceptance criterion is examined.

 If inequality (2) is satisfied, then the current solution s is replaced by the new solution s<sup>0</sup>, otherwise the move selected is rejected.

 The same procedure is repeated for each of the moves selected in the inner loop, until the maximum number of feasible moves in the inner loop has been reached and the inner loop stopping-criterion is met.

8.3.2.2. Phase 2. BATA decides whether the value of the threshold will be backtracked or lowered; therefore, a threshold controlling procedure is conducted in the outer loop. After applying a number of feasible moves, as determined by the inner loop stopping criterion, the value of the threshold is lowered if the move acceptance criterion has been satisfied at least once in the inner loop. However, the value of the threshold $T _ { \mathrm { h } }$ is raised, or backtracked when there was no acceptance in the inner loop. The increase of the threshold value during the backtrack is always smaller than the prior one, providing the smallest possible value for the threshold in order to have some acceptances.

The iterations in the outer loop are stopped when one of the following criteria is met:

 the standard deviation over the average of the costs of all the moves in the last inner loop is less than or equal to a user specified tolerance, for example $\varepsilon _ { 1 }$ , for a consecutive number of outer loop iterations;

 the standard deviation over the average of the costs of all the moves in all the inner loops performed, is less than or equal to a user specified tolerance, for example $\varepsilon _ { 2 } .$ , for a sequential number of outer loop iterations;

 the maximum number of iterations (based on a time budget constraint) of the outer loop has been reached; or

 although the value of the threshold $T _ { \mathrm { h } }$ has been backtracked (raised), no feasible move was accepted in the outer loop for a number of consecutive iterations.

## 8.3.3. Step 3

Return the best solution found.

## 9. VRP solution methodology for applications to the Greater Athens

## 9.1. Basic characteristics of the region and the road network of Athens

Greater Athens is the target area of applications here. The integrated urban character of the region is ensured by: the existence of a common/shared infrastructure connecting all its parts, the common administrative framework, intercenter dependence of the everyday activities in the center of the city of Athens and Piraeus, as well as in the centers of a small number of regional centers clustering around the city center. The Municipality of Athens is at the center of the area.

The area of the region is about $5 4 4 \mathrm { k m } ^ { 2 } .$ , if only the build-up urban environment is taken into account, or a total of $1 4 5 0 \mathrm { k m } ^ { 2 } ,$ , if semi-rural areas, agricultural land, and forest preserves are included. This makes up to 35% of the area of Attica county and it includes three mountain ranges and four relatively high hills, which constitute important barriers to transport. The central region of the Greater Athens area, the Athens Basin, is the main urban part with more than 90% of its residential population. The Central Area of Athens is the central district bounded by the inner ring road of the city, with an area surface of 11.76 km<sup>2</sup>, in which traffic restriction apply, based on odd/even license plate numbers and total restriction of personal transportation in a very small part. In Athens there are about 28 km<sup>2</sup> of free parks and other open spaces. The estimated population of Athens for year 1997 was about 3 700 000 residents.

The transport infrastructure in Athens consists of a road network with a total length of 2500 km. Its density is 5.5 km (road)/km<sup>2</sup> of urban area, within the Athens Basin, or 8.5 km/km<sup>2</sup> within the Municipality of Athens. Out of total 12% of these roads are dual carriageways, while 28% are one-way streets; 77% of these roads have one-lane in each traffic direction, 16.5% are two-lane roads and 6.5% are three-lane roads. The frequency distribution of roads according to total width (including side walk-ways) is 5.4% with widths of less than 7 m, 32.4% with width of 7–10 m, 35.7% with 10–15 m, 12.6% with 15–20 m and 13.9% with widths greater than 20 m. This road network is controlled by about 1000 signalized intersections and 40 intersections at grade.

All road traffic in Athens encounters significant traffic delays and low traffic speeds, which lead to large travel times. As a result of the increase in travel demand and the rapid increase in the use of private cars, during the last 25 years, there is currently a 2.6% average annual increase of traffic within the central areas, 3.5% increase within the rest of the main urban area (Athens Basin) and 7% increase within the suburban and semi-rural areas. Traffic congestion and delays are not helped by the fact that a significant percentage of roads are either of small width or at large grade. It has been estimated that the average traffic speed throughout the main urban areas is about 23 km/ h, while the average speed in the remote suburbs is 35 km/h and in the semi-rural areas 52 km/h.

## 9.2. Compilation of the chartographic background

The chartographic characteristics considered necessary for the operation of the SDSS are:

 The road network of the Greater Athens.

 The location of customers and depot.

 Detailed topographic diagrams of the centers of the city of Athens and Pireaus.

 Detailed topographic diagrams of the centers of suburbs of Athens and Pireaus (Peristeri, Nikea, Kifisia, Marousi).

 The rest land uses (rural areas, forests, military installations, industrial areas, etc.).

 Elevation contours, with a contour interval of 10 m.

The available data for the collection of the information were:

 Maps for general use at a scale of 1:5000, in analog form, which cover the whole area and include the necessary leveling. The date of the last updating of the various mapsheets varies between 1988 and 1997.

 Recent airphotos with stereoscopic coverage of the whole area, at a scale of 1:15 000.

 The ratified urban plans for the settlements, at scales of 1:500 and either of 1:1000 or 1:2000.

 Analog or digital topographic diagrams of the depot and customers, with the accuracy of the map scale 1:100 to 1:500.

Using our technical specifications, the creation of a two-level structure of the digital chartographic information was used:

 A general map of the whole region. Its compilation required two stages:

 The digitization through the ArcView software and its structural transformation into GIScoverages of necessary information in the analog maps of general use (i.e. road network, streams, contours, etc.).

 The updating and completion of the digitized data using recent airphotos. The continuous expansion of the urban sprawl of Athens mainly towards the north and the east, because of better environmental conditions, resulted in some of the digitized data being out of date. Changes were also noticed even at the road map data level, due to the construction of new roads leading to the newly-constructed airport of Spata. The use of digital rectification proved to be the most effective way to resolve this for the following reasons:

– The comparatively low accuracy demands.

– The availability of leveling data.

– The use of check points derived from the extant maps.

Twenty airphotos were used; they covered the whole region with significant side and forward overlap. From each photo, a proper part around its center was selected (a size of 7–12 cm on the image scale), so that a maximum error of 6 m on the ground (or 0.4 mm maximum radial displacement on the image) was achieved.

The photogrammetric rectifications were made by ARCHIS software of SISCAM, in an MS-Windows environment. For each rectification 8–10 well defined points on the analog maps of 1:5000 were used as control points. These points were crossroads, characteristic boundaries of large land parcels, etc.

A photomosaic was compiled for the whole region out of the rectified photos, by using the capabilities for raster geoprocessing of the module ARC GRID of GIS-software ARC/INFO of ESRI. The coordinate differences at the seams of images were within the necessary accuracy, making it possible to digitize the necessary planimetric characteristics from the unique raster file.

 A detailed map of the surrounding road network of each customer and the depot. The additional to the general map data were recorded in new coverages of the SDSS, for better manipulation of the data. The additional data were collected.

 By digitizing the blocks on the existing analog urban plans, included to the areas of interest.

 From the topographic diagrams of the locations of depot and customers. Those in analog form were scanned and the rest were properly adapted to the chartographic background by using common points (i.e. boundaries, roads, diagram orientation, etc.).

 From stereoplotting of individual parts of stereopairs for the surrounding road network of each customer and the depot that are not covered by the extant diagrams. This process was applied in four stereopairs for the collection of a limited number of planimetric data (boundaries, narrow roads). Control points that were used included well defined points on the large-scale topographic diagrams of each customer. The plotting was done on VMAP, the PC-based digital photogrammetric system. The discrepancies noticed between the photogrammetrically determined ground coordinates of check points and their coordinates as they are derived from the topographic diagrams, were less than 0.8 m.

The descriptive information that is related to the chartographic data was collected from:

 public agencies, such as the National Statistical Service of Greece, about the population density per urban block and employment, and Ministry of Transportation;

 existing studies for the transportation network in the Athens Greater area; and

 airphoto interpretation studies (classification of the road network, land use).

## 9.3. The VRP of Greater Athens

The SDSS for solving the VRP has been used very successfully several times in different types of applications, such as routing for taxi-companies, delivery of meals, couriers, and routing for a newspaper industry. It solves the problem of finding a set of optimal routes, defined on a road network of Greater Athens, through a set of customers, for a fleet of homogeneous capacitated vehicles to satisfy the delivery requirements of customers. Each vehicle started at the distribution center (depot) and after satisfying the demand of each customer it visits, returned back to the depot. The capacity of a vehicle could not be exceeded, and a single vehicle supplied each customer’s demand. The objective was to find the set of vehicle routes, minimizing the total distance traveled by the vehicles, subject to the constraints.

In order to define each vehicle routing scenario, we fill following parameters in predefined query forms:

 The node number of the depot.

 The node numbers of customers to be serviced.

 The capacity of vehicles used.

 The customers’ demands.

 The time limit on the length of the route.

 The traffic speed.

 The node number of the erased or added node in the cases of creating a new vehicle routing scenario.

The SDSS exploits this information and combines it with the spatial characteristics of the area of Greater Athens, generating automatically the vehicle routing plan and representing it with an efficient graphical way, as it is shown in Fig. 7.

Finally, the results of the problem are demonstrated in a tabular way, which is used to answer questions about:

 Customers that form each route.

 Vehicles that deliver to customers.

 The order in which the vehicles deliver to customers.

 The length and duration (or distance traveled) in each route.

 The total length and duration (or distance traveled) of all routes developed.

 Capacity utilization of the vehicles used.

## 10. Advantages of the proposed SDSS

Although several commercial SDSSs for solving the VRP have been developed, very few have publicly informed possible users about their technical characteristics, due to lack of incentives or restrictions on proprietary information. Unfortunately, the majority of the VRSs that have been published belong to the previous system generation

The benefits of using a commercial VRP–SDSS are generally known: transport cost reduction, improved customer service, effective strategic planning, less reliance on individual skills, tighter control of distribution, effective support of semi-structured or unstructured vehicle routing decision making by the displaying road network, administrative boundaries, complex path constraints and paying attention to spatially referenced data. However, the real advantages come from the technical characteristics and methods used in finding the vehicle routes, since these factors determine the general system’s efficiency. Thus, the advantages of an SDSS are mainly:

![](/api/attachments/XNPKNUQY/fulltext/images/b270df8cd271cee28a900b5ec0de4b167facad445314210ee1f603406bbe8644.jpg)  
All together  
Fig. 7. A vehicle routing plan developed by the proposed SDSS.

 The efficient representation of the network, allowing the fast implementation of routing methods.

 The performance of the BATA method in vehicle routing applications, which can solve real life (large) vehicle routing problems quickly and efficiently.

information in solving VRP using the BATA method. The architecture of the SDSS is based on an integrated framework of GIS and RDBMS technology systems equipped with interactive communication capabilities between software tools. The SDSS was developed for a Windows 98 system for PCs and was applied in the area of Greater Athens.

## 11. Conclusions

This paper presents a SDSS that coordinates and disseminates tasks and related spatial and non-spatial

## References

[1] A.A. Assad, B. Golden, R. Dahl, M. Dror, Evaluating the effectiveness of an integrated system for fuel delivery, in:

J. Eatman (Ed.), Proceedings of the S.E. TIMS Conference, Myrtle Beach, September 1983, pp. 153–160.

[2] A.A. Assad, in: B.L. Golden, A.A. Assad (Eds.), Modeling and Implementation issues in Vehicle Routing, Elsevier, New York, 1991, pp. 7–46.

[3] M.L. Balinski, R.E. Quandt, On an integer program for a delivery problem, Operations Research 12 (2), 1964, pp. 300– 304.

[4] L.C. Barbosa, R.G. Hirko, Integration of algorithmic aids into decision support systems, MIS Quarterly 4, 1980, pp. 1– 12.

[5] C. Basnet, L. Foulds, M. Igbaria, FleetManager: a microcomputer-based decision support system for vehicle routing, Decision Support Systems 16, 1996, pp. 195–207.

[6] W. Bell, L. Dalberto, M. Fisher, A. Greenfield, R. Jaikumar, R. Mack, P. Prutzman, Improving the distribution of industrial gases with an on-line computerized routing and scheduling system, Interfaces 13 (6), 1983, pp. 4–23.

[7] S. Belardo, P. Duchessi, J.P. Seagle, Microcomputer graphics in support of vehicle fleet routing, Interfaces 15 (6), 1985, pp. 84–92.

[8] L.D. Bodin, D.J. Salamone, The development of a microcomputer based system for vehicle routing and its use for solving spatial and temporal problems, Mathematical and Computer Modeling 11, 1988, pp. 558–562.

[9] L. Bodin, L. Levy, Visualization in Vehicle routing and scheduling problems, in: Proceedings of the ORSA/TIMS Meeting, Detroit, October 1994.

[10] J. Brandon, H. Slavin, E. Ziering, Geographic information systems as a platform for O.R., in: Proceedings of the ORSA/ TIMS Meeting, OR, April 1992.

[11] B. Cao, Solving Vehicle routing problems with time windows from the real-world, in: Proceedings of the INFORMS Meeting, Montreal, April 1998.

[12] J. Chakrapani, D. Honeycutt, J. Sandhu, Tutorial: Introduction to geographic information systems and basic applications, in: Proceedings of the ORSA/TIMS Meeting, Detroit, October 1994.

[13] N. Christofides, S. Eilon, An algorithm for the vehicle dispatching problem, Operational Research Quarterly 20, 1969, pp. 309–318.

[14] N. Christofides, The vehicle routing problem, RAIRO 10, 1976, pp. 55–70.

[15] G. Clarke, J.W. Wright, Scheduling of vehicles from a central depot to a number of delivery points, Operations Research 12, 1964, pp. 568–589.

[16] G. Croes, A method for solving traveling salesman problems, Operations Research 6, 1958, pp. 791–812.

[17] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14, 1995, pp. 219–235.

[18] G.B. Dantzig, J.H. Ramser, The truck dispatching problem, Management Science 6 (1), 1959, pp. 80–91.

[19] G. Dueck, T. Scheuer, Threshold accepting: a general purpose optimization algorithm appearing superior to simulated annealing, Journal of Computational Physics 90, 1990, pp. 161–175.

[20] S. Evans, J. Norback, The impact of a decision support system for vehicle routing in a food service supply situation, Journal of the Operational Research Society 36, 1985, pp. 467–472.

[21] A.S. Fotheringham, P. Rogerson, GIS and Spatial Analysis: Report on the Specialist Meeting, National Center for Geographic Information and Analysis, Report 92-11, San Diego, April 1992.

[22] B.A. Foster, D.M. Ryan, An integer programming approach to the vehicle scheduling problem, Operational Research Quarterly 27, 1976, pp. 367–384.

[23] W.M. Garvin, H.W. Crandall, J.B. John, R.A. Spellman, Applications of linear programming in the oil industry, Management Science 3, 1957, pp. 407–430.

[24] T.J. Gaskell, Bases for vehicle fleet scheduling, Operational Research Quarterly 18, 1967, pp. 218.

[25] B. Golden, T.L. Magnanti, H.Q. Nguyen, Implementing Vehicle Routing Problems Networks 7, 1977, pp. 113–148.

[26] M. Goodchild, R. Haining, S. Wise, Integrating GIS and spatial data analysis: problems and possibilities, Geographical Information Systems 6 (5), 1992, pp. 407–423.

[27] M.D. Gould, P.J. Densham, Spatial Decision Support Systems: A Bibliography, National Center for Geographic Information and Analysis, Technical Paper 91-9, Buffalo, June 1991.

[28] M. Igbaria, R.H. Spraque Jr., C. Basnet, L. Foulds, The impact and benefits of a DSS: the case of FleetManager, Information and Management 31, 1996, pp. 215–225.

[29] P. Keenan, Using a GIS as a DSS generator, in: J. Darzentas, J.S. Darzentas, T. Spyrou (Eds.), Perspectives on DSS, University of the Aegean, Greece, 1996, pp. 33–40.

[30] P. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems 22, 1998, pp. 65–71.

[31] G. Laporte, I.H. Osman, Routing problems: a bibliography, Annals of Operations Research 61, 1995, pp. 227–262.

[32] D.J. Maquire, An overview and definition of GIS, in: D.J. Maquire, M.F. Goodchild, D.W. Rhind (Eds.), Geographical Information Systems, 1991, pp. 9–20.

[33] D.F. Marble, Some Thoughts on the Integration of Spatial Analysis and Geographic Information Systems 2, 2000, pp. 31–35.

[34] P.A. Rogerson, A.S. Fotheringham, Research Initiative 14: GIS and Spatial Analysis, Closing Report, University of Buffalo, November 1995.

[35] J.M. Rousseau, Customization versus a general purpose code for routing and scheduling: a point of view, in: B.L. Golden, A.A. Assad (Eds.), Vehicle Routing: Methods and Studies, 1991, pp. 469–479.

[36] C.D.J. Waters, A solution procedure for the vehicle scheduling problem based on iterative route improvement, Journal of the Operational Research Society 38, 1987, pp. 833–839.

[37] D. Weigel, B. Cao, Solving real-world routing problems by using GIS and optimization techniques, in: Proceedings of the INFORMS Meeting, Dallas, October 1997

[38] D. Weigel, B. Cao, Applying GIS and OR techniques to solve Sears technician-dispatching and home-delivery problems, Interfaces 29 (1), 1999, pp. 112–130.

[39] A. Wren, A. Holliday, Computer scheduling of vehicles from one or more depots to a number of delivery points, Operational Research Quarterly 23, 1972, pp. 333–344.

[40] P. Yellow, A computational modification to the savings method of vehicle scheduling, Operational Research Quarterly 21, 1970, pp. 281–283.

![](/api/attachments/XNPKNUQY/fulltext/images/d591b87a85c6561da9a1df9509be09a44a1e751cf8606b782f79d8238e2d87f4.jpg)

C. D. Tarantilis is a Research Assistant at the Department of Chemical Engineering of the National Technical University of Athens. He received a Diploma degree in Mathematics from the University of Patras and a Master of Science degree in Operational Research from London School of Economics. His research interests are in transportation and logistics, decision support systems, combinatorial optimization, mathematical programming and approximation algorithms.

![](/api/attachments/XNPKNUQY/fulltext/images/3e53d8c2087bb45d95c0dffc6848de9144074f1edd7d27519947f2836dbbad5f.jpg)

C.T. Kiranoudis is a Lecturer of Process Design and Systems Analysis at the Department of Chemical Engineering, National Technical University of Athens. He holds a Diploma degree in Chemical Engineering and a PhD degree in Non-Linear Mathematical Programming from the same University. His current research focuses on design and control of chemical processes and plants, numerical analysis, mathematical

programming, risk analysis and development of information systems.
