---
otero_id: 17655
otero_key: "EQZ59NCC"
title: "A microcomputer assistant for the development of vehicle routing and scheduling heuristics"
authors: "Jean-Yves Potvin; Guy Lapalme; Jean-Marc Rousseau"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90073-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A microcomputer assistant for the development of vehicle routing and scheduling heuristics

Jean-Yves Potvin and Guy Lapalme
Université de Montréal, Montreal, Que, H3C 3J7, Canada

Jean-Marc Rousseau

Giro Inc., 75, rue Port-Royal Est, Montreal, Que, H3L 3T1, Canada

A microcomputer vehicle routing and scheduling system aimed at supporting algorithm designers is described. The system is called Micro-ALTO and stems from the experience gained with a previous system running on specialized hardware. The paper focuses on the graphic and interactive features of Micro-ALTO and shows how we used the current microcomputer technology so as to provide a sophisticated environment to the user.

Keywords: Vehicle routing; Vehicle scheduling; Heuristic algorithm; Algorithm development; Algorithmic framework.

## 1. Introduction

Creating algorithms that generate cost-effective routes involves numerous decisions relating to:

(a) the objectives that must be emphasized (e.g. number of routes, total route length, quality of customer service).

(b) the problem's characteristics that are of interest (e.g. distribution of the customers in the area to be serviced, number and type of transportation vehicles, physical and operational constraints).

(c) the metrics to be used for guiding the route generation process (e.g. distances or travel

![](/api/attachments/EQZ59NCC/fulltext/images/bfddd74b4d1b90631926174eb8caf4508ee90eb9e8c2fcd323bcedeb7c705e17.jpg)  
Jean-Yves Potvin is Associate Researcher at the Centre de Recherche sur les Transports of Montreal University. He received a Ph.D. degree in Computer Science from Montreal University in 1987. He then completed a post-doctoral fellowship at Carnegie-Mellon University (CMU). He is currently interested in applying artificial intelligence techniques to complex transportation problems.

Correspondence to: J.-Y. Potvin, Centre de Recherche sur les Transports, Université de Montréal, C.P. 6128, Succ. A, Montreal, Quebec, H3C 3J7, Canada.

![](/api/attachments/EQZ59NCC/fulltext/images/23dbc8eb41cfa116a019da218001e9805b710f0c7e40db3b3fc1663fa3767426.jpg)

![](/api/attachments/EQZ59NCC/fulltext/images/1bd9796d75a190a1529aaf2c659b4cee5a39a2be5f2fea475846d08b65fd2948.jpg)

Guy Lapalme is Full Professor at the Department of Computer Science and Operations Research of Montreal University. He received a Ph.D. degree in computer science from Montreal University. He works in the application of artificial intelligence techniques in the domains of transportation problems and macromolecule modeling. He is also interested in the use of functional and logic programming for natural language generation.

Jean-Marc Rousseau is vice-president of Giro Inc., a company located in Montreal that produces software for solving routing and scheduling problems in the transportation domain. He is also adjunct professor at the Department of Computer Science and Operations Research of Montreal University. He received a Ph.D. degree in operations research from M.I.T and has published many papers in international journals relating to transportation problems.

times between customers, detours or delays for servicing new customers).

(d) the overall problem-solving strategy (e.g. building many routes in parallel or building routes one by one).

Consequently, the development of a computer system aimed at supporting such decisions has been the focus of our work for the last four years. A first implementation of such a system was completed in 1989 on a Xerox AI workstation [12]. The system, called ALTO, was the basis of a doctoral dissertation and, consequently, little effort was put on user-friendliness and interactive-graphic features. The system however included the first version of a general algorithmic framework to be “filled-in” with user-defined mathematical formulas so as to create new algorithmic behaviors. The system also provided an environment for applying the newly created algorithms to vehicle routing problems specified by the user.

The development of the general algorithmic framework greatly facilitated the design of new algorithms. In this regard, it provided greater flexibility and extended standard routing softwares, like RoadNet or Truckstops, where the algorithm is a priori designed (“black-box approach”) and offers numerical control parameters to the user. Within ALTO, the specific algorithms for solving routing problems were not a priori defined, but user-defined.

It would be beyond the scope of this paper to describe in detail the theoretical basis of the system, in particular ways to specify mathematical formulas for creating complex algorithms. Details relating to the specification language for creating new formulas as well as descriptions of complex algorithmic specifications may be found in $[8,11,12]$ . In this paper, we will rather focus on the main characteristics of a new microcomputer implementation that we have just completed in the Allegro CommonLisp environment of the MacIntosh. The new implementation is much more user-friendly than the previous version and includes many interactive-graphic features for supporting algorithm designers in their difficult task. Overall, the main contribution of Micro-ALTO is in the harmonious integration of interactive-graphic features and network algorithms to aid in decision making.

The rest of the paper is organized as follows. Section 2 first defines the class of vehicle routing problems that we are addressing. Sections 3, 4, 5 and 6 then describe how algorithmic development is supported in the current microcomputer environment. This is done by following the user through a “natural” sequence of actions, that is: definition of the transportation network, specification of the routing problem and specification of the problem-solving strategy. Finally, some performance considerations and concluding remarks are made in the last two sections.

## 2. Description of the class of vehicle routing problems

As it is well known, most vehicle routing problems are NP-hard and cannot be solved optimally in polynomial time. Heuristic (or approximate) problem-solving strategies are thus widely used for solving large, real-life problems. Robust heuristics exist for unconstrained problems, like the Traveling Salesman Problem $[1,7,15]$ . However, in complex situations involving numerous constraints, the behavior of heuristic algorithms is much more unpredictable, and a decision support system for guiding the algorithm designer in his(her) task can provide great benefits.

Micro-ALTO currently solves a class of problems known as “node routing problems” [1]. Here, a demand or service request is located on specific nodes of the transportation network. Such nodes are typically called stops or customers. A fleet of vehicles must then service those customers at minimum cost and satisfy various physical and/or operational constraints.

Based on this generic definition, many different types of node routing problems may be found in the literature. Given the multiplicity of such problems, the current implementation only addresses a subclass of those problems with the following characteristics:

(a) Micro-ALTO addresses either pick-up or (exclusive) delivery problems. Mixed problems with pick-up and delivery within the same route are not allowed.

(b) A fleet of vehicles is housed at one central origin (depot). The maximum fleet size is not specified “a priori” and the fleet can be heterogeneous.

(c) The service demand at each customer is known. It must be entirely collected or delivered by the vehicle servicing the customer.

(d) One single route, starting and ending at the depot, is created for each vehicle.

(e) One or more of the following (optional) constraints can be considered:

i) maximum capacity for each vehicle
ii) maximum travel time (or distance) for each vehicle

iii) single time window at each customer.

(f) The overall objective is to minimize operational costs and/or maximize service quality, subject to the stated constraints (e.g. minimize total travel time, optimize service time with respect to the “ideal” service time at each customer, etc.).

Those characteristics are found in many real-world settings. If other minor characteristics or constraints are also present in a particular setting, the system can still be useful for developing insights about the kind of algorithms that can be successfully applied to such problems (e.g. an additional constraint asking for a given customer to be serviced by a given vehicle does not modify the very nature of the problem, whereas Dial-a-Ride problems are fundamentally different from the class of routing problems that Micro-ALTO can handle).

## 3. Computer-aided algorithmic design for vehicle routing

Supporting algorithmic design in the vehicle routing domain requires a good interactive and graphic environment because the designer needs to test his(her) new algorithms on various problems in order to evaluate their relative strengths and weaknesses.

![](/api/attachments/EQZ59NCC/fulltext/images/0af553760065f9f5d8b3ec99a08dff510fcd510a2ee4731d9ccb81b7208c15d5.jpg)  
Fig. 1. Micro-ALTO screen.

In this regard, Figure 1 shows a typical Micro-ALTO screen. In the window on the right hand side of the screen, a transportation network is displayed. The black square is the depot and the white squares are customers to be serviced. Zoom-in facilities, within user-defined polygons or via fixed increments, are provided for close examination of small areas within the transportation network (see Figure 3, for example). Each node can also be reduced or enlarged as desired.

The window on the left hand side of the screen displays either the current user-defined formulas embedded within the algorithmic framework (as it is the case here) or informations about customers, vehicles, routes, etc. The small window under the network is the Lisp executive. It is used for typing Lisp commands within the Allegro Common Lisp environment.

Pull-down menus appear when selections are made in the menu bar above the windows. The current available selections are:

(a) “File” for loading and saving network, distance matrix and problem specification files (cf. standard MacIntosh “File” selection).

(b) “Edit” for cutting and pasting informations displayed on the screen (cf. standard MacIntosh “Edit” Selection).

(c) “Global” for modifying characteristics of sets of routing objects (e.g. if the same demand value is to be put in every customer node). When a modification to a single object is desired, that object must be pointed to with the mouse. A dialog window for describing that object then appears on the screen and provides a means to modify the object’s content via user-editable fields (see section 5).

(d) “Heuristic” for filling-in the algorithmic framework and applying it to a given problem. This pull-down menu also includes a route editor to manually modify the current solution (e.g. customer nodes can be added or removed from a route by clicking on them with the mouse).

(e) “Solution” for storing and fetching the routes generated by the user-defined algorithms.

(f) “Graph” for editing transportation networks (i.e. moving nodes around, adding and deleting nodes and links).

(g) "Windows" is the standard MacIntosh selection for accessing the various windows on the screen.

In the following, we will describe more precisely some of the features presented above and explain how the expert algorithm designer can use them in the current Micro-ALTO environment. This is done by following a typical user through the most “natural” sequence of events, that is: definition and/or editing of a transportation network, specification of a routing problem, specification and application of a problem-solving strategy.

## 4. Phase 1: Definition of a transportation network

Every real vehicle routing problem is based on an underlying road infrastructure (either urban, regional or national), whose description comes from raw geographical data stored in Statistic Canada Area Master Files in Canada and U.S. Census Tiger files in United States. Such an infrastructure can however be hidden from the computer system, by inputting only the useful information extracted or derived from the raw data files. In our context, for example, we need only to evaluate the distance matrix (i.e. the length of the shortest path between each pair of customers). This matrix, along with the description of the depot, the fleet of vehicles and the customers, is all that is needed for describing a vehicle routing problem. It would thus have been possible to leave out all the details relating to the management of real networks, by providing our system with pre-calculated distance matrices.

During the development phase of the system, however, real mail pick-up problems located in Montreal were submitted to us by Canada Post Corporation, and we felt at that time that the ability to use the description of the real urban transportation network could be of value. Such an ability to display and manipulate real network structures is certainly not so important with respect to the aim of Micro-ALTO, which is to support algorithmic design, but this “add on” is in practice very interesting, as we discovered later.

To this end, we should mention the following benefits:

(1) The ability to generate distance matrices that reflect the structure of the underlying road networks. Since the road infrastructures can now be stored within the system, a procedure for evaluating the shortest paths between customers which account for specific characteristics of the underlying network, like one-way streets and U-turn or left-turn penalties and prohibitions, was subsequently added to the system. With this new feature, Micro-ALTO is now much more autonomous, since it does not rely anymore on pre-calculated distance matrices. This ability to generate distance matrices, along with the ability to update the road infrastructures via a user-friendly graphic interface (see point 2, below), provides us with a data base of networks and distance matrices that are always up to date for experimenting with new algorithms.

(2) The ability to edit real road networks. Although real networks do not change much over time, Micro-ALTO allows updates to such networks, via addition or deletion of nodes and arcs (e.g. if a new street is built, if a two-way street is transformed into a one-way street, etc.). All modifications are done by working directly on the graphic representation of the network. For example, if the user wants to delete a node, he (she) first selects the “delete node” command in the graphic editor menu and then the node to be deleted by clicking on it with the mouse. That node will automatically disappear as well as all its incident links. Once again, we must emphasize that even if the user is working on a bitmap image, any modifications to that image are automatically reflected in the underlying network structure.

(3) The ability to generate new transportation networks. With Micro-ALTO, the user can interactively create brand new transportation networks from scratch via the editing facilities. Those networks do not necessarily reflect real road infrastructures but are useful for defining new transportation contexts for testing user-defined algorithms. Such networks are useful in particular for “theoretical studies” aimed at evaluating the robustness of a given algorithm in various contexts (e.g. symmetric versus highly non symmetric distance matrices).

(4) The ability to relocate the depot or the customer nodes within a transportation network. Since the underlying network is now available, it is possible to superimpose on it many different routing problems that do not necessarily reflect real situations, but are nonetheless useful for testing the robustness of new algorithms. The user can thus interactively add new customer nodes, delete existing customer nodes or relocate the depot or the customers within a given transportation network before reevaluating the distance matrix, so as to set a new context for the tested algorithm.

(5) The ability to generate exact network paths. When a user-defined algorithm is applied to a given routing problem, it typically generates a set of routes, that is, a set of sequences of customers. With the availability of the underlying network, we can now display the exact path that a vehicle must follow in order to go from one customer to the next in its route, rather than display the route in “crow-fly” mode. This ability is useful in urban contexts in particular, because the shape of the routes is often an important criterion for evaluating the success of a given algorithm, and exact routes better support such a subjective assessment.

As an example, if we assume that a vehicle cannot service a customer located “on the other side of the street”, (i.e. the vehicle’s crew is not allowed to cross the street), specific arcs must be specified so as to force a proper access to each customer. Those access arcs are interactively selected by the user or are read from a problem specification file (see section 5). In Figure 2a, we show a portion of a real urban network with one-way and two-way streets. The underlying network structure is derived by assigning a node to each intersection and one or two arcs for portions of one-way and two-way streets between two intersections. In Figure 2a, the nodes are shown as little circles and the arcs as arrows pointing in the direction of the traffic flow. Two customers are located in this area. Customer 1 is located at an intersection and is thus assigned to the node representing that intersection (little circle with number 1). It is made accessible via arcs a and b. Customer 2 is located on another street between two intersections. In such a case, this customer is assigned to the intersection that is to be crossed after its service (little circle with number 2), and this node is made accessible through arc c only, so as to constrain the vehicle to be on the “right” side of the street.

In such a situation, we can see that the exact shortest path from customer 1 to customer 2, as depicted in Figure 2b, is much different from the crow-fly path of Figure 2c. Since pre-calculated distance matrices only provide shortest distances between customers and not the exact paths, it is not possible to generate such an exact path without knowledge of the underlying network structure.

Figure 3 shows how an exact route and a crow-fly route looks within the Micro-ALTO environment. It also illustrates the zooming capabilities of the system, since the area shown is a small portion of the transportation network of Figure 1. In the current implementation, routes can be displayed all at once or one by one. The latter facility is particularly useful for routes with time-window constraints. Typically, those routes are tangled (“spaghetti-like”) because time issues are taken into account in addition to geographical issues. By providing an ability to display each

(a)  
![](/api/attachments/EQZ59NCC/fulltext/images/12a7fd43e15711549a9d2542a05f2b3569f40ba5e5ca2f77ff9a8a9d16db78b5.jpg)

(b)  
![](/api/attachments/EQZ59NCC/fulltext/images/8eb33144011ff2b54b7ffc03d209a691339391824b5ccd071b39229a836ccd7e.jpg)

![](/api/attachments/EQZ59NCC/fulltext/images/7badcde8d8e462de5908312ace0e745e13b251fbf94320f5f5c3992856fb827e.jpg)  
Fig. 2. Exact path versus crow-fly path.

![](/api/attachments/EQZ59NCC/fulltext/images/8873072307337b28378f2c404d888b6bcb51c0cce4551e837a614857f91ed71d.jpg)

![](/api/attachments/EQZ59NCC/fulltext/images/2c68f363981522e47c7556d0d3cecd4d1e3b67b7f14c56f65194ef41e7dada77.jpg)  
Fig. 3. Route for a vehicle in exact mode and crow-fly mode.

route individually, it is much easier to follow the sequence of customers within a given route.

Currently, the network description as well as the distance matrix are stored in main memory. It is thus not possible to work with very large networks (like the whole road network of Montreal). However, with 4 Megabytes of memory, we were able to easily accommodate networks with 500 nodes and 750 unidirectional and bidirectional links. Those are the largest networks that we had to work with (they represent the road infrastructure of the various postal zones of Montreal). By extrapolation, we estimate that a network with up to 1000 nodes and 1500 links can be stored within 4 Megabytes of memory. Although those numbers can look modest to the practitioner, it is important to remember that Micro-ALTO is mainly a testbed for designing and experimenting with new algorithms. Accordingly, it is seldom necessary to work with very large networks. Theoretical problems or scaled-down versions of real routing problems can often be used for assessing the merits of user-defined problem-solving strategies. Once a proper algorithm has been identified within the Micro-ALTO environment, this algorithm can then be implemented and run on any desired platform

In summary, Micro-ALTO offers the following features relating to the management of transportation networks:

(1) display of networks

(2) modification to the nodes
- add
- delete
- move
- modify access arcs
(3) modification to the arcs
- add
- delete
- modify length
- modify prohibition or penalty for left-turns and U-turns

(4) load and save network files

(5) display exact routes

From the above discussion, we can see that our system exhibits features that are found in Geographic Information Systems (GIS). However, it is not really competitive with GIS's that are now commercially sold, both with respect to the features or commands available and the amount of data that it can handle. The GIS features of Micro-ALTO have been selected with respect to our overall objective, namely, to build a tool that would facilitate and accelerate as much as possible the development of new and efficient vehicle routing algorithms.

## 5. Phase 2: Specification of the vehicle routing problem

Once the structure of the underlying network has been defined, a new vehicle routing problem can be superimposed on that structure. The current system allows interactive definition of new problems by specifying the followings:

(1) location of the depot in the transportation network.

(2) location of customers in the transportation network.

(3) specification of the value of each customer's characteristics. Those characteristics are: the demand (e.g. quantity of a product) to be picked up or delivered, the dwell time, the desired service time and the time window.

(4) specification of the size and composition of the fleet of vehicles. This implies the ability to create or delete vehicles and to specify the value of their characteristics. Those characteristics are: the speed, capacity, maximum travel distance and scheduling horizon.

In the current implementation, the above transformations are done via “dialog windows” that are associated with each node in the transportation network. The purpose of a dialog window is much the same as a “form” in GIS terminology. It is implemented as a special type of window which contains active regions. Those regions include standard buttons (rounded rectangles), radio buttons (small circles) and editable text box (text inside a rectangular area).

For example, in the upper part of the window displayed in Figure 4, there are three standard buttons for selecting alternative actions relating to the content of the window (like "Ok" to save the content of the window). Radio buttons are used for specifying values with a small finite number of disjoint alternatives (see Figure 4, under "type:", "label:" or "font:"). Finally, text boxes are used for typing general alphanumeric data (see Figure 4, besides "number:", "identifier:" and "coordinates:").

![](/api/attachments/EQZ59NCC/fulltext/images/f53c7f750967a4edcc1b27c47f4b19ee759cf3f6e1afb6525d42297016226df4.jpg)  
Fig. 4. Dialog window for a simple transition node.

![](/api/attachments/EQZ59NCC/fulltext/images/19a30df016a52313ad92df0a1f68f1c40665ecda34f23931ca8c0e2754b71734.jpg)  
Fig. 5. Dialog window for a customer.

Three distinct dialog windows are defined in the current environment, according to the node type, which is either a depot, a customer or a simple transition node. A dialog window pops up when the user clicks on a specific node with the mouse and, depending on the node type, a dialog window for a simple transition node (Figure 4), a customer (Figure 5) or a depot (Figure 6) appears on the screen.

As shown in the dialog window of Figure 4, values for characteristics that are common to all node types can be interactively defined by the user, like the node identifier, its coordinates and various parameters about the node display (within the box entitled “display”). More importantly, the node type can be modified so as to transform a simple transition node into a depot or a new customer. For example, if the user selects the “customer” radio button by clicking on it with the mouse (this action automatically turns off the “node” radio button), and then selects the button “Ok” so as to save the content of the window, the simple transition node transforms itself into a customer and additional characteristics for describing a customer appears at the bottom of the original window (see Figure 5). Initially, each additional characteristic has a default value, but those values are user-editable. Currently, the value of the following characteristics can all be modified by the user: demand, dwell time, desired service time and time window.

Alternatively, if the new selected type is “depot”, a window for specifying the fleet of vehicles appears at the bottom of the original window (see Figure 6). The list of all current vehicles is displayed on the left hand side of the new window under “Vehicles” (cf. vehicles V1, V2, V3, V4 in Figure 6). Any vehicle in this list can be selected in order to display and eventually modify the value of its various characteristics, which are shown on the right hand side of the window. The characteristics currently associated with each vehicle are: capacity, speed, maximum travel distance, scheduling horizon (“start time” and “end time”) and an identifier.

New vehicles can also be interactively created by first specifying on the right hand side the desired value for each characteristic and then, by clicking in the button “Create”, a new vehicle with the specified characteristics is created and added to the current list. Alternatively, vehicles can be deleted by selecting the appropriate vehicles in the list and by clicking in the button "Delete". Finally, vehicles are made active or inactive (i.e. are made available or not for servicing the routes) by selecting them in the list and by clicking in the toggle button "Activate" to activate or deactivate them. In addition, two other buttons are provided for activating or deactivating all vehicles at once.

![](/api/attachments/EQZ59NCC/fulltext/images/481bda1159e4a5cc086d60378fa4e1e6e81e4a97c179eab178070aad4a5ab259.jpg)  
Fig. 6. Dialog window for a depot.

The description of each customer along with the description of the depot and the fleet of vehicles can all be saved in a problem specification file for future use. User-defined algorithms exploit those informations for generating routes, along with the distance matrix which is derived from the problem specification and the underlying network structure.

## 6. Phase 3: Specification of the problem-solving strategy

The availability of many different heuristic strategies for solving complex vehicle routing problems is an important concern because the behavior of a given heuristic tends to vary a lot from one problem to the other. Moreover, evaluation of any solution is a subjective assessment that can also vary over time and from one organization to the other.

Within Micro-ALTO, the set of available strategies can be dynamically modified and expanded by the user according to his (her) own needs. Specification of new algorithms is done at two distinct levels. At the lower level, the basic components (procedures) of the desired algorithms are defined. In the current implementation there are four such components, thereafter called “generic operators”. Each operator stands for a general class of problem-solving procedures that are commonly found as ingredients of more complex vehicle routing algorithms. Specific procedures are then created from those generic ones by specifying formulas and/or values for numerical parameters. In a way, each generic operator is a kind of template from which numerous specific procedures can be generated.

At the upper level, the user-defined components are then combined so as to create complete algorithms. In the following, we will explain how specific procedures can be created from the generic templates and how to combine those components so as to build complete algorithms.

## 6.1. Specification of the problem-solving components

Modifications and additions to the set of available problem-solving components are done via user-defined formulas, which are aimed at creating specific procedures from four distinct procedural templates or generic operators. Since formulas are specified by the user with a high-level language that we built on top of Lisp, an infinite spectrum of different formulas, and thus an infinite spectrum of specific procedures, can be created within such a framework. Once defined, each specific procedure can then be saved in a bank for later use. There is a distinct bank associated with each generic operator, and all the procedures created from a given operator are stored in its bank.

In the current implementation, each generic operator appears as a dialog window with editable fields for the specification of the desired formulas and numerical parameters. A new procedure is automatically created when the content of the dialog window is saved in the environment.

In the following, we give a brief description of the four generic operators currently available within Micro-ALTO. The first operator, INIT, will be described in more detail to allow a better understanding of the basic concepts.

(1) Operator INIT is a general procedure for initializing new routes with “seed” customer nodes. It provides a means for specifying an orientation for each new route, as depicted in Figure 7. In this example, three routes R1, R2 and R3 are initialized. Customers 3 and 4 are used as seeds for initializing route R1, customers 5 and 6 for initializing route R2, and finally customer 7 initializes route R3. A distinct vehicle is then assigned to each route. Operator ADD (see its description below) can then be used to incorporate the remaining unrouted customers into the existing routes.

![](/api/attachments/EQZ59NCC/fulltext/images/8a324e13d4f5359ab46a5f92d087595d7e48784bad0be8c76b4207288fbe54bf.jpg)  
Fig. 7. General behavior of operator INIT.

In summary, one or more seeds must be selected from the set of unrouted customer nodes and a vehicle must be selected from the set of available vehicles in order to initialize a new route. This selection process is entirely driven by the user-defined formulas, as it is now explained.

The procedural template for operator INIT, which is depicted in Figure 8, is simply a loop that iterates over the routes to be created. At each cycle, it selects the seed customers and the vehicle, as specified by the user's formulas, for creating and initializing a new route. In the dialog window of Figure 8, the rectangular areas are editable text boxes. The user can thus specify the number of new routes to be created (e.g. the box besides "NbRoutes < -"), the subset of free customers to be considered for initializing the new routes (besides "SE-AL < -"), the formula for selecting the seed customers in the subset SE-AL (besides "S < -") and, finally, a formula for selecting a vehicle from the set of available vehicles (besides "V < -").

There is also a constraint section for setting the value of the parameters associated with the various types of constraints. Lambdacap relates to the capacity constraint, Lambdadist and Lambdatemps relate respectively to the maximum travel distance and travel time, Lambdafen1 and Lambdafen2 to the lower and upper bounds of the time window at each customer. When the value of a given parameter is set to NIL, the corresponding constraint is ignored. When the value of the parameter is a real or an integer number, that value is used for adjusting the corresponding constraint. As an example, the capacity constraint is adjusted according to the following formula:

Total demand on the route

## ≤ Lambdacap \* Capacity of the vehicle

Hence, a value of 1 for Lambdacap sets the usual capacity constraint, a value greater than 1 relaxes the constraint and a value smaller than 1 has an opposite effect by tightening it even more. The operator's behavior is obviously affected by the constraint settings. Operator INIT, for example, does not create a route when the assignment of seed customer nodes to a given vehicle, as specified by the user-defined formulas besides "V < -" and "S < -" respectively, implies the violation of some of the stated constraints.

In Figure 8, we see how a specific procedure has been created from the INIT procedural template. First, we must observe that no constraint is active, since all parameters are set to NIL. One new route is asked for, by selecting a seed in the whole set of unrouted customers (this is the meaning of setting the subset of unrouted customers SE-AL to E-AL). The formula besides “S < -” asks for the selection of the farthest un-routed customer from the depot. Here, the global variable O stands for the depot and P.DIST is a pre-defined function for evaluating the distance between two nodes. The MAXOBJ form acts as a “for S in SE-AL do P.DIST(O S)” statement, and returns the S for which the value of the function P.DIST is maximum. It thus iterates over all the unrouted customers in the set SE-AL, which happens to be the whole set of unrouted customers here, and selects the farthest unrouted customer from the depot. Finally, the vehicle is selected at random from the set E-VL of all available vehicles (assuming an homogeneous fleet).

![](/api/attachments/EQZ59NCC/fulltext/images/9d2de0abcfc6579ef881e8ad537ea93c14d13673c2a453f0b5a9dc50653ca728.jpg)  
Fig. 8. Dialog window for operator INIT.

Such a procedure reproduces the initialization phase of the farthest insertion algorithm $[15]$ . Of course, by modifying the various formulas and numerical parameters, many different behaviors can be reproduced. A brief description of the specification language for creating such formulas is provided in the Appendix at the end of the paper. The interested reader is referred to $[13]$ for a complete description of that language.

In the following, we describe in somewhat less details the remaining generic operators. It must be understood that each operator is provided to the user as a dialog window in much the same way as for INIT above. However, each generic operator represents a distinctive class of procedures and the templates are thus very different from one another.

(2) Operator ADD is a general procedure for iterative addition of new customers into the current routes (which were created with operator INIT). It is basically a loop that iterates over the set of unrouted customers and try to insert them into the existing routes. At each iteration, a customer and a route are selected, and the selected customer is inserted into the selected route. This process is repeated until a stopping criterion is met or when all unrouted customers have been considered in turn. If constraint parameters are active, the procedure inserts a customer only if all stated constraints are satisfied. Hence, many customers can remain unrouted at the end of the procedure, if the problem is tightly constrained. In such a case, the actual constraints can be relaxed or new routes can be created so as to accommodate the remaining customers.

The procedural template for operator ADD allows the user to specify formulas for the following actions: selection of a route in the set of existing routes, selection of the next unrouted customer to be considered for insertion, selection of a location within the selected route for the insertion of the selected customer, and specification of a stopping criterion. As an example, formulas can be created so as to obtain the following behavior: select the last route created by operator INIT, select the unrouted customer which is the farthest from the selected route and insert that customer at the minimum detour location. In this way, we get the insertion phase of the farthest insertion algorithm. By combining such a procedure with the initialization procedure of Figure 8, we then obtain the complete farthest insertion algorithm [15].

(3) Operator MERGE is a general procedure aimed at merging routes together. At each iteration, it selects a pair of routes and merges them together into a single larger route. This process is repeated until a stopping criterion is met or when all pairs of routes have been considered in turn. If constraint parameters are active, the procedure merges routes only if all stated constraints are satisfied. Hence, many routes can remain unchanged at the end of the procedure, if the problem is tightly constrained. In the current implementation, routes are merged by concatenating them together. Hence, if route R1 services customers 1, 2, 3 in that order and route R2 services customers 4 and 5, the resulting route is either 1, 2, 3, 4, 5 or 4, 5, 1, 2, 3, depending on feasibility considerations (that is, if the first route is not feasible, the system generates the second one if it is feasible).

The procedural template for operator MERGE allows the user to specify formulas for the following actions: selection of a pair of routes from the set of all existing routes, selection of a vehicle for servicing the enlarged route and specification of a stopping criterion. As an example, formulas can be created to select pairs of routes with maximum savings [3].

(4) Operator EXCHANGE is aimed at modifying the sequence of customer nodes into existing routes. It can reproduce the well known 2-opt,

3-opt and Or-opt arc exchange procedures, as well as node exchange procedures [1,9,10].

In the procedural template for operator EXCHANGE, the user can specify the type of exchange and the criteria for deciding if the solution, after an arc or node exchange, is better than the previous solution. The user can ask, for example, for a 2-opt exchange procedure aimed at minimizing the total travel distance. Other criteria can be used as well like: distributing the demand evenly among the routes, minimizing the total route time or optimizing the service time at each customer with respect to their stated desired time. Within the quality formula, the user can also define a weighted sum of various criteria. As for the previous operators, the procedure will exchange arcs or nodes only if all stated constraints are satisfied.

Overall, the four generic operators provide a very flexible framework for specifying vehicle routing algorithms. The ability to relax any stated constraint (via the constraint parameters) proves also to be very useful. For example, if the number of available vehicles is set a priori and is too small to service all customers and satisfy all constraints, a problem-solving strategy can be designed so as to either generate only strictly feasible routes at the expense of leaving some customers apart or, alternatively, relaxations to some of the stated constraints can be introduced in order to accommodate all customers (assuming that slight violations of some constraints, like time windows, are tolerable).

Now that we have described in turn each generic operator, as well as ways to use them for creating specific procedures, we will explain how those procedures can be incorporated into complete algorithms.

## 6.2. Specification of complete algorithms

Once all the desired procedures have been created, they must then be incorporated into a complete algorithm. For combining procedures together, Micro-ALTO offers a 'batch mode' or an "interactive mode". They are both discussed in the following.

(1) In batch mode, the procedures are incorporated and called from a standard user-defined Lisp program which represents the whole algorithm. This mode is very flexible and allows for complex control structures (like a loop construct for iterative application of a given procedure until some condition is met, conditional application of specific procedures, etc...). It however requires some knowledge of the Lisp programming language (apart from our own specification language for creating the specific procedures from the generic operators).

In batch mode, Micro-ALTO simply provides an editor window for creating the Lisp program and a special function for calling the desired user-defined procedures within such a Lisp program. Once defined, the program can then be run on various problems. We call it “batch mode” because there is no way to see intermediate results, namely, the partial routes as they are built by the successive application of the various procedures embedded in the program. Hence, only the final routes are displayed on the screen.

![](/api/attachments/EQZ59NCC/fulltext/images/ccf009637ea38bfc4abb0fb6dfb13d3707c45fc9654b572db09754263fd5f51c.jpg)  
Fig. 9. Incremental problem-solving.

(2) The interactive mode is an attractive alternative mode, because the user can interactively ask for the application of individual procedures to the current set of routes and look at the resulting routes on the screen. In this way, it is possible to see how the routes evolve, as each procedure is applied in turn. If a given procedure does not produce the expected results, it is always possible to backtrack to the previous state (i.e. the previous set of routes) and try some other procedure. A complete algorithm, here a sequence of user-defined procedures, is thus incrementally built by trials and errors, until a satisfactory behavior is obtained.

Figure 9 illustrates this incremental approach to algorithmic design. A specific user-defined procedure is seen here as a single step along the path from the initial problem state to a final goal state (i.e. from the empty set of routes to the final set of routes where every customer is serviced and all stated constraints are satisfied). Along this path, we thus find partial routes that are to be “augmented” or improved. The interactive mode, with its backtracking mechanism, allows a dynamic exploration of various sequences of user-defined procedures in order to identify interesting algorithms. Once a good algorithm has been identified, the corresponding sequence of user-defined procedures can then be saved for future use.

6.3. Specification of classical vehicle routing algorithms

Although Micro-ALTO is mainly used for designing new algorithms, it can also simulate many classical algorithms, if appropriate formulas are provided. In section 6.1, for example, we showed formulas for the initialization phase of the farthest insertion algorithm. We also explained how the following insertion phase of this algorithm could be specified within the framework of operator ADD. As a matter of fact, the following well know vehicle routing algorithms can all be specified within our algorithmic framework:

<table><tr><td>1. Insertion Algorithms [1,15]</td><td>NearestFarthestCheapestQuickConvex HullGreatest AngleDifference XRatioNearestNeighbor</td></tr><tr><td></td><td>Algorithms of Solomon [16]Algorithm of Potvin and Rousseau [14]</td></tr><tr><td>2. Clarke and Wright Algorithm</td><td>Parallel algorithm [3]Sequential algorithm [6]</td></tr><tr><td>3. Clustering algorithms</td><td>Sweep algorithm [5]Algorithm of Ferland and Rousseau [2]</td></tr></table>

The ability to reproduce known algorithms can be of value for comparing their merits on various kinds of problems and discover their respective strengths and weaknesses.

## 7. Performance considerations

Since Micro-ALTO offers a general framework for specifying vehicle routing algorithms, it can be easily understood that flexibility was, by far, our main concern. It is also obvious that a specialized algorithm, with a lot of programming hacks, will always run faster than the same algorithm specified within the Micro-ALTO environment. Nonetheless, we provide here some computational results in order to give an idea of the time magnitude for solving problems.

First, we should mention that the minimum configuration for running the system is a Mac + with a hard disk and 4 Megabytes of RAM. However, it is advisable to install the system on a MacII with either 4 or 8 Megabytes of RAM, because the interaction with the system is then much faster. Also, larger screens are available for the MacII microcomputers, and this proves to be useful for displaying large “real-life” networks.

The following computation times were obtained on a MacIICX with 4 Megabytes of memory. The algorithms were applied to the Bourassa postal zone, located in the north of Montreal, which includes 425 nodes, 643 unidirectional and bidirectional links, one central depot and 37 customers (postal stations).

(1) We first generated the distance matrix for the above problem. It is, by far, the most time-consuming task and, for that reason, distance matrices are usually saved in files for later use. Although generating a distance matrix has nothing to do with running user-defined vehicle routing algorithms, it nevertheless gives an idea of the speed of our shortest path algorithm in the Allegro Common Lisp environment of the MacIntosh (the shortest path algorithm is an adaptation of the well-known Dijkstra's algorithm [4]).

It took 702.9 seconds to generate the whole distance matrix. People working with the same algorithm, implemented in “C” on an IBM-PC microcomputer with a floating point coprocessor, did obtain the same time magnitude. Since the IBM-PC is less powerful than the MacIICx, we certainly did lose some computation speed by implementing Micro-ALTO in Allegro Common Lisp. However, we had two good reasons for doing this:

(a) The Allegro Common Lisp environment is very rich for developing programs with nice user interfaces.

(b) Common Lisp is an interpreted language, so the formulas within the algorithmic template do not need to be recompiled when they are modified by the user.

(2) After generating the distance matrix, we designed a nearest insertion algorithm within the Micro-ALTO framework and applied it to the above problem. It took 15.0 seconds to get the solution. A further 2-opt post-optimization exchange procedure took 10.95 seconds and a final 3-opt exchange procedure took 40.15 seconds. Those computation times, which include the route display, look reasonable given the overall generality and flexibility of our system.

Overall, our feeling is that the modest computation speed of the system, due to the generality of its approach, is largely overweighted by its flexibility and ease of use.

## 8. Concluding remarks

In this paper, we have described an integrated system for computer-aided algorithmic design in the vehicle routing domain. This system allows interactive display and editing of transportation networks, as well as interactive specification of vehicle routing problems and problem-solving strategies. Although a natural sequence of events is to first build (or read from a file) some transportation network, then specify a vehicle routing problem and finally solve the problem, Micro-ALTO allows much more flexibility. It is always possible to “loop around” and redefine either the network structure or the routing problem before a new problem-solving phase (see Figure 10). Moreover, since Micro-ALTO offers a general algorithmic framework, many different problem-solving strategies can be tested on any given problem.

![](/api/attachments/EQZ59NCC/fulltext/images/b4509239db05d40af0ceb700d5bde871e2a237b66b6bd9b701e67de8363708f8.jpg)  
Fig. 10. Flexibility of Micro-ALTO.

The system thus provides a very flexible environment for experimenting with various problem-solving strategies in various routing contexts. Micro-ALTO is currently used, as an example, for designing and testing new heuristic algorithms for vehicle routing and scheduling problems with time window constraints (VRSPTW). With the help of Micro-ALTO, we discovered a very powerful route building procedure for VR-SPTW problems. A description of that algorithm, as well as numerical results on the standard set of problems of Solomon [16], may be found in [14]. Other interesting applications of the system, in particular mail pick-up problems for postal vehicles, are described in [11]. Finally, since a large number of classical heuristic algorithms can be specified within the Micro-ALTO framework, the system is also used as a pedagogical tool for graduate students at the Computer Science Department of Montreal University.

## Acknowledgements

We would like to thank Pierre St-Vincent and Patrice Bergeron for the hours spent at implementing Micro-ALTO. We would also like to thank the Natural Sciences and Engineering Research Council of Canada (NSERC), as well as the Fonds pour la Formation de Chercheurs et l'Aide a la Recherche (FCAR) of the Quebec government for their financial support.

## References

[1] L. Bodin, B.L. Golden, A. Assad, M. Ball, Routing and Scheduling of Vehicles and Crews: The State of the Art, Computers and Operations Research 10(2), pp. 63–211 (1983).

[2] L. Chapleau L., J.A. Ferland, J.M. Rousseau, Clustering for Routing in Densely Populated Areas, European Journal of Operational Research 20, pp. 48–57 (1985).

[3] G. Clarke G., J. Wright, Scheduling of Vehicles from a Central Depot to a number of Delivery Points, Operations Research 12, pp. 568–581 (1964).

[4] E.W. Dijkstra, A Note on two Problems in Connexion with Graphs, Numer. Math. 1, pp. 269-271 (1959).

[5] B. Gillett, L. Miller, A Heuristic Algorithm for the Vehicle Dispatch Problem, Operations Research 22, pp. 340-349 (1974).

[6] B.L. Golden, Evaluating a Sequential Vehicle Routing Algorithm, AIIE Trans. 9, pp. 204–208 (1977).

[7] B.L. Golden, W.R. Stewart, Empirical Analysis of Heuristics, In: E.L. Lawler, J.K. Lenstra, A.H.G. Rinnoy Kan, D.B. Schmoys Eds, The Traveling Salesman Problem: A Guided Tour of Combinatorial Optimization, pp. 207–249 (John Wiley and Sons, 1985).

[8] G. Lapalme G., J.Y. Potvin, J.M. Rousseau, A General Heuristic for Node Routing Problems, In: H.A. Eiselt and G. Pederzoli Eds, Advances in Optimization and Control, pp. 124–143, (Springer-Verlag, 1988).

[9] S. Lin, Computer Solutions of the Traveling Salesman Problem, Bell System Tech. J. 44, pp. 2245–2269 (1965).

[10] I. Or, Traveling Salesman-type Combinatorial Problems and their Relation to the Logistics of Blood Banking, Ph.D. Thesis, Dept. of Industrial Engineering and Management Sciences, Northwestern University (1976).

[11] J.Y. Potvin, Un Système Informatique pour le Développement et l'Expérimentation d'Algorithms de Génération de Tournées, Thèse de Doctorat, Publication du Centre de Recherche sur les Transports, no. 522, Université de Montréal (1987).

[12] J.Y. Potvin, G. Lapalme, J.M. Rousseau, ALTO: A Computer System for the Design of Vehicle Routing Algorithms, Computers and Operations Research 16(5), pp. 451–470 (1989).

[13] J.Y. Potvin J.Y., P. St-Vincent, Manuel d'Utilisation du Système ALTO pour le Micro-ordinateur MacIntosh, Publication du Centre de Recherche sur les Transports, no. 748, Université de Montréal (1991).

[14] J.Y. Potvin, J.M. Rousseau, A Parallel Route Building Algorithm for the Vehicle Routing and Scheduling Problem with Time Windows, European Journal of Operational Research 66(3), pp. 331–340 (1993).

[15] D. Rosenkrantz, R. Sterns, P. Lewis, An Analysis of several Heuristics for the Traveling Salesman Problem, SIAM J. Comp. 6, pp. 563–581 (1977).

[16] M.M. Solomon, Algorithms for the Vehicle Routing and Scheduling Problems with Time Window Constraints, Operations Research 35(2), pp. 254–265 (1987).

## Appendix

Micro-ALTO provides a high level language for the specification of user-defined formulas within its algorithmic framework. In the following, we describe the main features of the language and give examples for each one of them. It should be noted that the symbolism that is used is based on French, and is thus not always very meaningful for the English reader (e.g. N-AT means total number of customers, that is, Nombre d'Arrêts Total in French).

## (a) Variables

Various global variables are available to the user, and the value of those variables are automatically updated by the system, so as to accurately reflect the current situation. Such variables can be freely incorporated within the user-defined formulas. Below are some examples:

O depot

N-AT total number of customers

N-VT total number of vehicles

N-R current number of routes

NOUV.R last route(s) created by operator INIT

(b) Sets

Standard sets of routing elements are available to the user. Those sets are also automatically updated by the system so as to accurately reflect the current situation (e.g. if an unrouted customer is added to a route by operator ADD, that customer is automatically removed from the set of unrouted customers and added to the set of routed customers). We give below some examples of such standard sets.

E-AL set of unrouted customers

E-AR set of routed customers

$E - R$ set of routes

E-S set of seed customers

E-V set of vehicles

E-VR set of vehicles that are currently servicing a route

## (c) Set Operators

Set Operators are provided for manipulating the standard sets introduced above. Basically, those operators are designed for iterating over sets of elements so as to return one or more element(s) or value(s) from that set. Here are some examples.

## (MAXOBJ ELEM SET FUNCTION)

Returns the ELEMENT in SET for which the value of FUNCTION is maximum. FUNCTION can be any function provided by the Micro-ALTO environment (see point (d) below) or by the Common Lisp Language.

For example (MAXOBJ A-L E-AL (P.DEM A-L)) returns the customer in E-AL with highest demand. Here A-L is simply a local variable that iterates over the set E-AL, and consequently, any other name for that variable could have been chosen. P.DEM is a predefined function returning the demand of its customer argument.

(MINOBJ ELEM SET FUNCTION)

Returns the ELEMENT in SET for which the value of FUNCTION is minimum.

(MAXVAL ELEM SET FUNCTION)

Returns the maximum value of FUNCTION when applied to each ELEMENT in SET.

(MINVAL ELEM SET FUNCTION)

Returns the minimum value of FUNCTION when applied to each ELEMENT in SET.

(SOUS-ENS ELEM SET FUNCTION)

Returns the subset of ELEMENTs in SET that satisfies FUNCTION (which must be a predicate).

## (d) Functions

A very rich library of predefined functions and predicates is provided to the user for creating his(her) formulas. In the following, we only give a few examples.

(P.DIST CUSTOMER1 CUSTOMER2)

Distance between CUSTOMER1 and CUS-TOMER2.

(P.DETOUR CUSTOMER1 CUSTOMER2 CUSTOMER3)
Extra-mileage when inserting CUSTOMER3 between CUSTOMER 1 and CUSTOMER2.

(P.DEMTOT ROUTE)

Total demand on ROUTE.

(P.PRED CUSTOMER)

If CUSTOMER is in a route, the predecessor of CUSTOMER in that route.

(P.DERNIER? CUSTOMER)

If CUSTOMER is in a route, is it the last customer in that route?

## (e) Mathematical and logical operators

Standard mathematical and logical operators are available to the user like: +, -, \*, /, AND, OR, NOT.
