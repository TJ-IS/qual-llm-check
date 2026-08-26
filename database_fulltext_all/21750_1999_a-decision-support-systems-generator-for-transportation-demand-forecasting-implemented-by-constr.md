---
otero_id: 21750
otero_key: "KNT6JNN5"
title: "A decision support systems generator for transportation demand forecasting implemented by constraint logic programming"
authors: "Cristina Fierbinteanu"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00030-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support systems generator for transportation demand forecasting implemented by constraint logic programming

Cristina Fierbinteanu )

Graduate School of Information Systems, UniÕersity of Electro-Communications, 1-5-1 Chofugaoka, Chofu, Tokyo 182-8585, Japan

Accepted 21 June 1999

## Abstract

In this paper we propose a framework for a decision support systems DSS generator for constrained search problems,Ž . implemented by constraint logic programming CLP . We illustrate this concept by the implementation of a DSS generatorŽ . for transportation demand forecasting. The user interface of the DSS generator is an intelligent, graphical editor that supports the construction of a specific DSS from basic building blocks. Additional constraints are specified as distinct building blocks, and the constraint solver of the host CLP language is extended with domain-specific constraint manipulation. The design of the system is based on ontological modeling. The originality of our approach, which achieves the transition from custom imperative programming to declarative programming in the field of transportation demand forecasting, consists of the model of the generator, as well as of the constraint logic solver for network flow problems. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems generator; Constraint logic programming; Transportation demand forecasting; Ontology; Computational geometry; Network flows

## 1. Introduction

This paper describes the implementation by constraint logic programming CLP of a decision Ž . support systems DSS generator for transportationŽ . demand forecasting. Problems in the field of transportation planning, including transportation demand forecasting, are unstructured, for the following reasons: the amount of data mainly socio-economicŽ and geographical data is very big; the variety of . data is very large, so that it is impossible to take all of it into consideration within a single estimation;

geographical considerations are needed. Moreover, the requirements imposed on the solution are often contradictory, so that the interaction of a human expert with the computer system is essential in the decision-making process, conducted in an iterative trial and error manner. For these reasons, a DSS generator, rather than a specific DSS, is necessary. A DSS generator is a software environment which provides the capabilities to build a specific DSS easily. Advantages consist of short development time, immediate feedback from the user, and improved users understanding of the system.

The original contribution of our approach consists of the model of a DSS generator for constrained search problems, developed within the constraint logic paradigm, and the development of a constraint logic solver for network flow problems. The user interface of the DSS generator is an intelligent, graphical editor that allows the user to construct a specific DSS from basic building blocks. It is to be remarked that additional constraints are specified as distinct building blocks, rather than being incorporated within the implementation of the algorithms. The building blocks constitute a transportation systems ontology for demand forecasting.

CLP is descended from logic programming, to which it adds efficiency by using constrained search abilities. Refs. 4,11,13 provide excellent reviews of <sup>w</sup> <sup>x</sup> the theoretical bases of CLP and constraint satisfaction problems. The implementation of the DSS generator by CLP has the advantage of being declarative, while keeping efficiency within admissible bounds. The complex logical constraints that characterize the actual transportation demand forecasting problem could hardly be modelled in the traditional mathematical programming framework. For our implementation, we have used the CLP language CHIP. ŽCHIP is an acronym for ‘‘Constraint Handling In Prolog’’. It was originally developed at ECRC in Munich, Germany, and it is now marketed by COSYTEC. 15 .. <sup>w</sup> <sup>x</sup>

## 2. DSS Generator for constrained search problems

Constrained search problems e.g., scheduling, Ž planning, resource allocation, placement, routing. appear frequently at different levels of decision. They are usually characterized by technical, environmental or political constraints, which make them unstructured, and in most of the cases are difficult to solve NP-complete . Traditional mathematical pro- Ž . gramming approaches linear programming, integer Ž and mixed integer programming are deficient in the. following ways: their representation of constraints is artificial commonly using 0–1 variables , their com- Ž . puting time in the presence of many constraints is very long due to combinatorial explosion , and they Ž . cannot process various constraints applied to the main problem. Thus, the most used approach consists in developing specific software, written in a procedural language like FORTRAN or $\mathrm { { C } , }$ to solve each particular problem. However, the use of procedural languages brings the following well known disadvantages: the development time of the programs is very long and the programs are very complex, hence difficult to maintain and adapt to rapid changes of requirements.

We propose a DSS generator implemented by CLP, which provides an alternative approach to solve constrained search problems. Unlike traditional approaches, CLP provides for a natural representation of heterogeneous constraints and allows domainspecific heuristics to be used on top of generic solving techniques. Within our framework, the user can specify a DSS in a pictorial manner Fig. 1 , byŽ . assembling building blocks which are parts of a transportation system ontology 14 . The implemen-<sup>w</sup> <sup>x</sup> tation of a generator is possible by CLP because in this framework constraints can be added to a main algorithm without having to change this main algorithm, as opposed to mathematical programming, where the constraints together with the main problem call for the design of a new algorithm. In other words, ‘‘In constraint programming we state the problem requirements; we do not need to specify how to meet these requirements. Constraints do not require us to envision how the information is to be used’’ 5 . <sup>w</sup> <sup>x</sup>

Fig. 2 shows the software structure and the total computational mechanism of the DSS generator 2 .<sup>w</sup> <sup>x</sup> At the center there is an ontology defining the concepts and relationships necessary and sufficient to describe the domain to be reasoned about, in a manner suitable for a particular class of tasks. The constraint solver of the CLP language has to be extended with constraints which are relevant to the studied domain, but cannot be found among the general constraints provided by the constraint solver. To illustrate the proposed concept of DSS generator, we chose the domain of transportation planning, specifically the field of transportation demand forecasting. In this case, we need to extend the constraint solver with network flow specific constraint manipulation and provide a transportation system ontology. Although our center of interest has been transportation demand forecasting, the framework of a DSS generator developed within a declarative paradigm Ž . Fig. 2 is general, and can be used for any domain characterized by unstructured constrained search problems, on condition that a corresponding ontology and the required extension of the general constraint solver are provided.

![](/api/attachments/KNT6JNN5/fulltext/images/d06bfc7c90c90a61ec9c11e83fc5002c2462fc6d93e34b4fc4acbe9b20a7a51a.jpg)  
Fig. 1. User interface of the DSS generator.

The user interface of the generator is an intelligent, graphical editor for DSS definitions. To create a definition, the user selects the building blocks one by one from a menu, then defines the connections by means of the mouse. At any moment, he can add, delete, replace building blocks on the specific DSS scheme. In order to achieve clarity, a scheme can be organized on different levels. That is, a few building blocks can be grouped together and represented by a single block on a higher level of the scheme. We say that the graphical editor is intelligent, in the sense that it validates the connections defined by the user, so that they comply with the definition of the com ponents’ interfaces. In order to achieve this validation, a type is associated with each input and output terminal for every component of the ontology. Once a DSS definition is completed, the user can decide to run it, or save it for future use and<sup>r</sup>or modification. The execution of a definition would cause the generator to assemble the ontology components, interface elements, algorithms, and constraints, into a single program, representing the implementation of a specific DSS.

![](/api/attachments/KNT6JNN5/fulltext/images/b9c70d848b7a53cba30e5f58911aca65b51fe4e0f6ee635057d082128eddea7b.jpg)  
Fig. 2. Software structure of the DSS generator.

## 3. Transportation planning and demand forecasting

Demand forecasting is the central step within the transportation planning process Fig. 3 , leading toŽ . the choice and implementation of one system among several transportation alternatives that are being analysed. The transportation consequences of each transportation alternative considered as candidate are predicted and constitute the basis of the decisionmaking process.

Fig. 4 shows the structure of the most commonly used transportation demand forecasting model. The model identifies four components of travellers’ behaviour 7 : the decision to travel for a given purpose <sup>w</sup> <sup>x</sup> Ž . Ž trip generation , the choice of destination trip distribution. Ž , the choice of travel mode modal choice. Ž , and the choice of route or path network assignment..

The trip generation stage estimates the number of trips originating and terminating in each zone, separately for each trip purpose. This estimation is based on regional socio-economic characteristics, predicted for the future year for which the analysis is being made. Such data future population, spatial Ž pattern of activities, etc. is available from national . and state planning organizations. In Japan, socioeconomic data is available in mesh form aggregatedŽ <sup>2</sup> within 0.5 or 1.0 km area from a number of. national census survey statistics.

The trip distribution stage achieves the connection between origins and destinations, taking as input transportation network characteristics e.g., dis- Ž tances, travel times, out-of-pocket costs, location of stations, etc. , user characteristics e.g., value of . Ž time , and the estimated number of trips available. from the previous stage. The result of the trip distribution stage is a matrix of trips by origin, destination, and purpose.

![](/api/attachments/KNT6JNN5/fulltext/images/859211337e65a989a8ae509377b119f47dcaf4bc7fcf00de0ee2690664fddfe5.jpg)  
Fig. 3. Transportation planning and demand forecasting.

![](/api/attachments/KNT6JNN5/fulltext/images/0a733bf2a7ca7eca0a753155ac57f40db697013daff687429a3e19d314014276.jpg)  
Fig. 4. Transportation demand forecasting model.

The next step of the demand forecasting model Ž . modal choice is concerned with the estimation of the proportion of travelers that would select a specific transportation mode the share of each availableŽ transportation mode , while the. network assignment stage allocates trips, by mode, to particular routes through the transportation network of the respective mode.

The solution of the trip generation problem mainly requires computational geometry algorithms 8 , <sup>w</sup> <sup>x</sup> while for trip distribution, modal choice and network assignment, network flow algorithms 1 are exten-<sup>w</sup> <sup>x</sup> sively used.

## 4. Transportation system ontology for demand forecasting

The DSS generator introduced in this paper is the first declarative approach of transportation demand forecasting. Our purpose has been to develop a modelling framework for doing sketch planning to assist transportation policy and investment decisions. This framework is more flexible than today’s current suite of models and can be used interactively and intuitively by managers without the help of a traffic modelling practitioner.

In order to achieve this goal, we first needed a method to organize the heterogeneous transportation planning domain knowledge and to specify domain specific problem solving methods. To describe transportation planning data, we use a domain ontology, that is, a set of concept definitions which give better structure to the domain knowledge. An essential feature of this ontology is that it implements topology, that is spatial relationships among entities. The domain ontology is implemented as a constraint database, which stores socio-economic, transportation network, and zoning data.

Domain-specific problem-solving methods are specified using a task ontology, that is, a collection of building blocks that can be used to construct a skeleton of a specific DSS. The task ontology is implemented as a library of Prolog-like rules, classified into algorithms, elements for building user interfaces, and constraints. There are two main groups of algorithms: computational geometry algorithms and network flow algorithms.

Specific DSS generation is done in two steps: first by assembling algorithms and menus into an intermediate program, then, at runtime of this code, adding user-defined constraints to obtain the desired specific DSS. The input to the first step of DSS generation is a graphical description of the intended system, given by the end-user. This description is accomplished by filling in the generic blocks of a skeleton DSS with concrete problem solving methods. For example, the skeleton DSS could specify the following sequence of generic actions: i zoning, Ž . Ž . Ž . ii data aggregation, and iii network assignment Ž . Fig. 5 . Based on his specific knowledge, the domain expert could specify a zoning method determined by administrative regions boundaries, mesh data aggregation and a network assignment along shortest paths. Alternatively, zoning could be performed by Voronoi diagrams, data aggregation done at administrative region level, and network assignment achieved according to a maximum flow optimization criterion. When filling in the skeleton DSS, the end-user can also specify which of the concrete problem solving methods would accept user-defined constraints at runtime.

![](/api/attachments/KNT6JNN5/fulltext/images/9c82cae6823a5653f5e89979aea916465c0499477c09f5d9d2abc9ca6461e8d7.jpg)  
Fig. 5. Specific DSS definition using the ontology.

In the second step of DSS generation, user-defined constraints are added to the program. The end-user specifies the additional constraints through a menu-driven interface, characteristic to each particular problem-solving method.

The main challenge in the design of the ontology was the identification of its components, which was a difficult process because there was no similar approach to which we could have related. We identified the components by examining different types of transportation planning problems and extracting their similarities and structures.

The knowledge of each ontology component includes types of constraints that can be added by the user of a specific DSS. Unlike conventional approaches, component functions in our ontology are flexible, in the sense that the interpretation of the component behaviour can differ for different implementations in specific DSS. For example, the flow assignment function uses different labelling strategies, according to the optimization criterion specified by the end-user. The choice of the labelling strategy Ž . heuristic is done by the system, based on the type of assignment required.

In order to support system modularity, the algorithm components of the task ontology must be incremental and general. That means adding new constraints does not invalidate the preconditions of an algorithm, nor it requires the solving process to start again from scratch. The system generation that we propose relies on these properties of CLP algorithms, which are not owned by traditional operations research OR algorithms. Ž .

## 5. The CLP implementation of the DSS generator

## 5.1. Implementation of the computational mechanism

There are two types of connections between the building blocks of a diagram representing the description of a specific DSS: serial connections, symbolizing data passing, and parallel connections, symbolizing a choice to be made when the specific DSS is run. In Fig. 1, serial connections are represented by single, directed lines, while parallel connections are represented by double, undirected lines. Serial connections are implemented by file manipulation. The basis for the implementation of parallel connections is embedded into the object oriented design of the system. For the object-oriented analy-Ž sis and design, we have used the Coad<sup>r</sup>Yourdon method 10 . We illustrate this affirmation by a  . practical example.

The most significant parallel connection is the connection between an algorithm definition block and a constraints specification block. Let us consider the connection between the block MinCostFlow and the block AddConstr in Fig. 1. Within the object oriented model, link objects know their head, tail, capacity, cost, fixed cost, time to traverse, and flow. The attribute flow is a domain variable corresponding to the flow on the respective link. An additional constraint defining, for example, an upper bound Bound on the set of links $\{ a , b , c \}$ is translated into the CHIP statement:

$$
a @ f l o w + b @ f l o w + c @ f l o w \# <   = B o u n d.\tag{1}
$$

When the specific DSS is run, the user can define this additional constraint by selecting the path ‘Link Set, Upper Bound’ from a pull-down menu named ‘Additional Constraints’. The selection of the links involved in the constraint $( a , b , c )$ is performed using the mouse and the value of the bound Bound is directly input from the keyboard. Constraints are dynamically added to or removed from the program using the clauses ‘‘assert’’ and ‘‘retract’’, available in CHIP. Our example above is implemented by the following fragment of code:

a@flow+b@flow+c@flow #<sup>-</sup>=Bound,

min\_cost\_flow(From,To,Productions,

Attractions,Nodes,Links ..

It is to be remarked that the code of the main flow assignment algorithm needs not to be changed when additional constraints are formulated by the user at the runtime of a specific DSS.

The symbol $\#$ represents the treatment of the constraints in an active way, either by solving them or by reducing the value generation by constraint propagation. For comparison, consider a traditional logic programming language like PROLOG, where the constraints are used in a passive way, that is for testing values generated by enumeration.

5.2. Implementation of the transportation demand forecasting ontology

Fig. 6 summarizes the categorization of the DSS generator’s functions by the type of CLP implementation.

The main features of the CHIP system are finite domain variables and linear terms over rational variables. In addition, demon-driven computation is possible, providing the means for defining constraints with user programs. Many different arithmetic and symbolic constraints are provided within the finite domain solver. Typical examples of problems that can be directly expressed using the built-in constraints of this solver are scheduling, time tabling and rostering. We have used the built-in symbolic constraints of the finite domain solver for the modelling of problems concerning facility location and other problems in the computational geometry field. For network flow types of problems, we have developed original heuristics for variable ordering and constraint propagation, as well as redundant constraints to speed the search. We have used update demons and the conditional propagation mechanism of CHIP for the implementation of these heuristics.

## 5.3. CLP heuristics for network flow assignment

Our approach of network flow problems by constraint logic is based on finite domain objects. Flow values are assumed integer and a domain variable is associated with the flow on each arc of the network. The mass balance constraint is expressed by equality constraints. Unfortunately, the built-in search procedure is very inefficient for this simple approach. In order to speed up the search, we have developed a few specific labelling strategies, presented below. These strategies can be broadly classified into two categories, that is: i dynamic ordering of the flow Ž . variables, using flow excesses reducing methods and distance labels, and ii construction of redundantŽ . constraints. In order to obtain bounds on the total flow we use the rational constraint solver of CHIP.

<table><tr><td>FUNCTION CATEGORY</td><td>CHIP IMPLEMENTATION</td></tr><tr><td>location problems with spatial constraints</td><td>symbolic, built-in constraints</td></tr><tr><td colspan="2">Examples: warehouses(Cities,Costs,Capacities,Solution,Cost).voronoi(Set_of_points,Locations,N,Area_min,Area_max).</td></tr><tr><td>miscellaneous shortest path algorithms</td><td>set of arithmetic constraints</td></tr><tr><td colspan="2">Examples: shortest_path(From,To,Path).first_n_shortest_paths(From,To,N,Shortest,Heuristic,Path2).</td></tr><tr><td>miscellaneous flow assignment algorithms(including network equilibrium assignment)</td><td>arithmetic constraints+original heuristics usingconditional propagation,update demons andredundant constraints</td></tr><tr><td colspan="2">Examples: min_cost_flow(From,To,Productions,Attractions,Flow).set_conervation_constraints(Outflows,Inflows,Productions,Attractions).constrain_path(Path,Flow_value,Flow_vars,Star).set_flow(Star,Outflow_vars,Link,Value).</td></tr><tr><td>heuristics for variable ordering</td><td>preprocessing of constraint graph</td></tr><tr><td colspan="2">Example: minimal_bandwidth_ordering(Nodes,Edges,MBWO,K).</td></tr><tr><td>resource allocation algorithms</td><td>specific constraint propagationtechniques implemented byupdate demons</td></tr><tr><td colspan="2">Example: allocate(Jobs,Starts,Intervals,Durations,Resources,Bound).</td></tr></table>

Fig. 6. Function categories by type of CPL implementation.

For each node n we define the node excess as the difference between the sums of the instant maximum values in the domains of the incoming arcs and that of the outgoing arcs Eq. 2 . The idea of nodeŽ Ž ..

![](/api/attachments/KNT6JNN5/fulltext/images/3ed9c0381ecc0449a12776a11280768e28f500f58da4c792b431e7b5fb756c61.jpg)  
Fig. 7. Zoning algorithm represented by the graphical editor.

excesses is borrowed from generic preflow-push algorithms for maximum flow problems 1 .<sup>w</sup> <sup>x</sup>

$$
e (n) = \sum_ {k} \max _ {-} \operatorname{dom} \left(x _ {k n}\right) - \sum_ {k} \max _ {-} \operatorname{dom} \left(x _ {n k}\right)\tag{2}
$$

The main idea of the labelling algorithm is to eliminate flow excesses. We always assign values to the variables from the largest value in the domain downwards in decreasing order. The node with the maximum flow excess is chosen to be labelled first. As the values of the excesses, which are calculated by update demons, change when constraint propagation occurs, the ordering of the nodes is dynamic.

Once we have chosen the node to label first, we still have to decide which of its adjacent arcs to label. We have experimented with different orderings. The best results were obtained when ordering the arcs going out from the node by the distance of their head to the sink. The incoming arcs were ordered by the distance of their tail to the source. This strategy corresponds to sending flow from the source to the sink on the shortest path. For a network with 17 nodes and 63 arcs, a labelling procedure using a static ordering of the nodes and no special ordering of arcs took 300,320 ms to find a solution. ŽAll the experiments described in this paper were performed using a UltraSparc based SUN machine.. A labelling algorithm using a dynamic ordering of the nodes by the value of their excesses found a solution in 3930 ms, about 75 times faster.

Our experiments have also shown that the time required to generate a solution depends on the number of bidirectional arcs in the network. For instance, the cpu time required to determine the maximum flow in a network with 21 nodes and 47 arcs, among which 7 bidirectional, was 220 ms; when we doubled the number of bidirectional arcs, the time to generate a solution was more than four times bigger with theŽ number of bidirectional arcs increased to 16, the solution was generated in 940 ms ..

![](/api/attachments/KNT6JNN5/fulltext/images/3265e4c7d36a2ba728c014e4ea2ba68ad5249e14f1de958bb294c48f5585382c.jpg)  
Fig. 8. Voronoi diagram: case 1.

In order to improve further the efficiency of the search, we looked for redundant constraints adding heuristics. Our experiments showed that in some cases the propagation of the mass balance constraint is improved by introducing a redundant constraint which states that the flow of a minimum cut equals the total flow from the source to the sink a well-Ž known property of the maximum flow in a network .. In the case of the network considered above, with 21 nodes and 63 arcs, the cpu time decreased from 940 to 880 ms when we introduced a redundant constraint on a minimum cut. Minimum cuts are determined prior to labelling, using the rational solver of CHIP.

5.4. Additional constraints in computational geometry algorithms

In transportation demand forecasting, we need to define zones as trip origins and<sup>r</sup>or destinations. Socio-economic data, available in mesh form from national census survey statistics, is then aggregated on each zone, and the result of the aggregation is attributed to a special point within the area, called the zone center. For example, the total population of an administrative region could be considered to be concentrated in the region’s center of gravity. In this case, zones are defined by administrative regions, and the zone centers are defined by their gravity centers. Zoning, that is, the definition of zones and their respective centers, is an important step in the process of forecasting the demand for transportation, as the results of the forecast are significantly influenced by the shapes and sizes of the zones, as well as by the choice of the zones’ centers. Several components of the DSS generator allow the user to define different zoning procedures. One of the most useful among these components is the construction of Voronoi diagrams. Fig. 7 shows a possible zoning algorithm defined in the DSS generator’s environment.

![](/api/attachments/KNT6JNN5/fulltext/images/340a19ea282bd35b5c7ec0b563021267d41dc4801b2913a08b785d29ada641c0.jpg)  
Fig. 9. Voronoi diagram: case 2.

The component voronoi\_diagram is implemented by a predicate of the form:

voronoi(Set\_of\_points,Locations,N,

Area\_min,Area\_max).

Set\_of\_points is a list of points from which we want to choose a set of cardinality N, Locations, and build its Voronoi diagram. In addition, the area of each Voronoi polygon is constrained to the interval [Area min, Area max]. Typical additional constraints are relative to the points that can be chosen, for example the user can specify the minimum and maximum number of points that have to be chosen from a certain subset of the available set of points. For each constraint of this type, a predicate of the form:

among([At\_least,At\_most],Locations,

Subset).

is added to the database. For example, the user-defined constraints: at least one point has to be chosen from the subset 28, 29, 30 , at least one point and at 4 most two points can be chosen from the subset <sup>w</sup> <sup>x</sup> 4–6 , exactly two points have to be chosen from the subset 7–9 , and one point has to be chosen from <sup>w</sup> <sup>x</sup> the subset 10–12 , are translated into the following <sup>w</sup> <sup>x</sup> predicates added to the program:

among([1,1],Locations,[28,29,30]),

among([1,2],Locations,[7,8,9]),

among([2,2],Locations,[10,11,12]),

among([1,1],Locations,[13,14,15]).

Constraint propagation is taken into account by the constraint programming language, so no additional code is necessary. Also, it is remarkable that the main code of the algorithm computing the

![](/api/attachments/KNT6JNN5/fulltext/images/e2069a33269643fa3009f41d8469aacaa5d9f6297aaefa56c132ab5f8602a513.jpg)  
Fig. 10. Feasible flow determination with additional constraints on transportation links.

Voronoi diagram needs no change, no matter the additional constraints added by the user when the specific DSS is run. Other additional constraints that can be added at runtime concern minimum<sup>r</sup>maximum distances between the center points of two adjacent zones Voronoi polygons . Figs. 8 and 9 Ž . show the results of a specific DSS implementing a Voronoi diagram calculation, with different constraints concerning the physical areas of the Voronoi polygons, and different runtime added constraints concerning the choice of points constraints of the Ž type ‘‘among’’, presented above ..

5.5. Additional constraints in network flow algorithms

The constraint programming approach of network flow problems is essentially different from the classical approaches 3 . A variable is associated with the<sup>w</sup> <sup>x</sup> flow on each link, and the nodes’ mass balance constraints are stated as equality constraints, handled by the constraint programming language. Within this framework, constraints added by the user at the runtime of a specific DSS can be taken into account in the determination of the solution, without any modifications in the algorithm solving the unconstrained problem. For example, in the case of the determination of a feasible flow Fig. 10 , possibleŽ . additional constraints are: link flow lower<sup>r</sup>upper bounds, limitations on the usage of some links someŽ links cannot be used , cost limits..

![](/api/attachments/KNT6JNN5/fulltext/images/bc1da486958ee43b86b1c6f6e24081b48737960dcf4bcdd3f1a1cb28bd9db53c.jpg)  
Fig. 11. Definition of the specific DSS.

If we denote by X the flow on a certain link, additional constraints concerning bounds will be declared by expressions of the type:

X #<sup>F</sup>Upper\_bound,

X #<sup>G</sup>Lower\_bound,

and handled by the constraint propagation mechanism of the language. Links’ usage and costs limitations are also declared by means of arithmetic constraints in the host language. As in the case of additional constraints for computational geometry algorithms, it is to be remarked that the code of the main flow assignment algorithms needs not to be changed when additional constraints are added by the user at the runtime of a specific DSS.

## 6. Case study

We have experimented with a transportation network described by the following facts:

station Line, Station number, Id, Name, X, Y,( Node number),

cross Line1, Station1, Line2, Station2, Name, ( Transfer time),

connect Arc number, Node1, Node2, Time,( Cost, Fixed cost).

The network is made up of 1029 nodes and 9602 arcs and covers an area of approximately 900 km<sup>2</sup>. The purpose of the study is to determine the utilities and transportation shares of the relevant paths from a selected origin to a selected destination, within a given geographical area. First, mesh data aggregation is performed on each administrative region, and competitive paths from that region to the selected destination are computed. The utility of each relevant path is calculated using the formula $U = c _ { 1 }$ )Time<sup>q</sup> $c _ { 2 } * c o s t + c _ { 3 } * N u m b e r \_ o f \_ ~ c h a n g e s + c _ { 4 } *$

![](/api/attachments/KNT6JNN5/fulltext/images/d6ef5086c23958941a82cfc145e86e40a92dd1cf71d5b66bbefe0e32529869f0.jpg)  
Fig. 12. Mesh data.

Access\_time, where the model parameters, estimated within a previous model calibration stage, have the following values: $c _ { 1 } = \mathrm { - } 0 . 0 9 7 0 , c _ { 2 } = \mathrm { - } 0 . 0 0 2 5$ $c _ { 3 } = - 0 . 8 2 1 2$ $c _ { 4 } = - 0 . 0 9 8 4 .$ . The proportion of travellers that will select a specific path i is then estimated using the multinomial logit model 7 , with<sup>w</sup> <sup>x</sup> the relationship: $p ( i ) = \mathbf { e } ^ { U _ { i } } / \Sigma _ { x } \mathbf { e } ^ { U _ { x } }$ , where U <sup>s</sup> utility associated with path i.

The definition of the system and a sample output are presented in Appendix A. The output listing also shows the cpu time required by the generation of each path. The average time to determine the first two shortest paths between an origin and a destination was about 25 s.

## 7. Evaluation in comparison with traditional methods

The determination of a shortest path using commercial packages implementing standard network flow algorithms would take a few milliseconds, thus performing better than our system. However, in comparison with current models used for transportation demand forecasting, our system has the following advantages.

Ž . 1 It is more flexible, easy to extend with additional constraints.

Ž . 2 Specific DSS generation based on ontological modelling gives the advantage of eased application development.

Ž . 3 A better quality of solutions can be obtained with our model, as more side constraints and degrees of freedom existing in the practical situation can be considered.

Having in view our goal sketch planning , flexi-Ž . bility and eased application development take precedence over efficiency, as long as the latest is kept within reasonable bounds.

Moreover, further research aimed at discovering new strategies for speeding up the search for solutions in the case of network flow assignment promises to ensure for CLP tools an efficiency comparable to specific programs written in procedural languages. Already, for particular assignment problems, the efficiency of CLP tools successfully competes with that of traditional OR techniques. Some of these applica- Ž tions are described in the proceedings of the conferences on ‘‘Practical Applications of Constraint Technology — PACT’’ and ‘‘Principles and Practice of Constraint Programming —CP’’ ..

![](/api/attachments/KNT6JNN5/fulltext/images/751b4c9657e6749cc980d1d4d1689c3d6189801aa523b14a3671da8533bd9317.jpg)  
Fig. 13. Relevant path.

## 8. Conclusions

We have described the implementation by CLP of a DSS generator for transportation demand forecasting. As transportation planning problems, including transportation demand forecasting, are unstructured, the decision-making process in this field is conducted in an iterative trial and error manner. The tool suitable for this analysis method is a DSS generator, that is, a software environment which provides the capabilities to build a specific DSS easily. We have implemented our system, which constitutes an alternative approach to mathematical programming or specific software written in procedural languages, by CLP. The user interface of the DSS generator we have presented is an intelligent, graphical editor that supports the construction of a specific DSS from basic building blocks. Additional constraints are specified as distinct building blocks. The originality of our approach, which achieves the transition from custom imperative programming to declarative programming in the field of transportation planning, consists in the model of the generator’s user interface, as well as in its CLP implementation.

## Appendix A. Case study see Figs. 11–13( )

Output listing

Zone<sup>s</sup>kitahassakuchou

```txt
From = miyame
```  
To<sup>s</sup>shibuya

Shortest path<sup>s</sup>Ž . Ž . miyame, 15 satsukigaoka, 15 Ž . Ž . Ž aobadaieigyoucho, 15 shiratoridai, 15 tutujigaoka, 15 enokibashi, 15 aobadaieki, 15 aoba-. Ž . Ž . Ž daieki, 55 fujigaokaeki, 55 ichigaoeki, 55 . Ž . Ž . Ž . Ž . Ž . edaeki, 55 azaminoeki, 55 tamapurazaeki, 55 Ž . Ž . Ž . saginumaeki, 55 shibuya, 55 shibuya, 54 .

```txt
Time = 5173
```

Cost<sup>s</sup>763

```txt
Number of changes = 1
```

Second<sup>s</sup>Ž . Ž . miyame, 15 yamatanimidoridai, 15 Ž . Ž . Ž . yamashitashoumae, 15 oyamachou, 15 aoto, 15 Ž . Ž . Ž . Ž aoto, 28 renshouji, 28 chiyobashi, 28 kainosaka, 28 ishibashi, 28 ishibashi, 48 saedo, 48 yabune,. Ž . Ž . Ž .Ž 48 ikebe, 48 umedabashi, 48 negishimae, 48. Ž . Ž . Ž . Ž . Ž . Ž . higashikata, 48 maekouchi, 48 orimotocho, 48 Ž . Ž . Ž shinkaibashi, 48 shinkaibashi, 23 ookumachou, 23 ootake, 23 hinhaeorikaejo, 23 shinbaneshou, . Ž . Ž . Ž 23 toukyuujuutakumae, 23 shinhanebashi, 23 . Ž . Ž . Ž . Ž . Ž futoodutsumi, 23 futookaikanmae, 23 ooamichuugakkoumae, 23 ookurayamaekimae, 23 oo-. Ž . Ž kurayamaekimae, 54 tsunashimaeki, 54 tsuna-. Ž . Ž shimaekiiriguchi, 54 hiyoshiekinishiguchi, 54 hi. Ž . Ž yoshiekihigashi, 54 shibuya, 54. Ž .

Time<sup>s</sup>6441

Cost<sup>s</sup>1356

Number of changes<sup>s</sup>4

23 380 ms

```txt
From = yamatanimidoridai
```

```txt
To = shibuya
```

Shortest path<sup>s</sup>Ž . Ž yamatanimidoridai, 15 miyame, 15 satsukigaoka, 15 aobadaieigyoucho, 15. Ž . Ž . Ž . Ž .Ž . shiratoridai, 15 tutujigaoka, 15 enokibashi, 15 Ž . Ž . Ž . aobadaieki, 15 aobadaieki, 55 fujigaokaeki, 55 Ž . Ž . Ž . ichigaoeki, 55 edaeki, 55 azaminoeki, 55 Ž . Ž . Ž tamapurazaeki, 55 saginumaeki, 55 shibuya, 55 shibuya, 54 . Ž .

```txt
Time = 5413
```

```txt
Cost = 789
```

Number of changes<sup>s</sup>1

## References

<sup>w</sup> <sup>x</sup> 1 R.K. Ahuja, T.L. Magnanti, J.B. Orlin, Network Flows, Theory, Algorithms, and Applications, Prentice-Hall, 1993.

<sup>w</sup> <sup>x</sup> 2 C. Fierbinteanu, The Implementation by Constraint Logic Programming of a Decision Support System Generator for Transportation Planning, Proc. of the 4th Int’l Conf. on the Practical Application of Constraint Technology, PAPPA-CT98, London, pp. 285–294, March 1998.

<sup>w</sup> <sup>x</sup> 3 C. Fierbinteanu, T. Okamoto, N. Nozue, Constraint Programming Approach of Network Flow Problems for Decision Support in Transportation Planning, Proc. of the 11th Int’l Conf. on Applications of Prolog, INAP-98, Tokyo, September 1998, pp. 100–106.

<sup>w</sup> <sup>x</sup> 4 D. Joslin, Constraints Archive URL:http:<sup>rr</sup>www.cirl.uoregon.edu<sup>r</sup>constraints<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 5 E.C. Freuder, In pursuit of the Holy Grail, ACM Computing Surveys 28 4es 1994 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 N. Nozue, S. Ishii, T. Shibata, Decision support system for transportation planning, Quarterly Report of RTRI 30 2Ž . Ž . 1989 .

7 C.S. Papacostas, P.D. Prevedouros, Transportation Engineering and Planning, Prentice-Hall, 1993.

<sup>w</sup> <sup>x</sup> 8 F.P. Preparata, M.I. Shamos, Computational Geometry, An Introduction, Springer, Berlin 1985.

<sup>w</sup> <sup>x</sup> 9 A. Reggiani, Design and management of transport networks. New approaches and experiments from a European and American perspective: an introduction, Transp. Res. Circ. 4 Ž . Ž . 6 1996 .

<sup>w</sup> <sup>x</sup> 10 M. Rosch, The Coad<sup>r</sup>Yourdon method: simplicity, brevity, and clarity — keys to successful analysis and design, in: A. Carmichael Ed. , Object Development Methods, Chap. 10, Ž . SIGS Books, New York, 1994.

<sup>w</sup> <sup>x</sup> 11 E. Tsang, Foundations of Constraint Satisfaction, Academic Press, 1993.

<sup>w</sup> <sup>x</sup> 12 G. Van Heijst, A.Th. Schreiber, B.J. Wielinga, Using explicit ontologies in KBS development, International Journal of Human–Computer Studies 46 2Ž . Ž . <sup>r</sup>3 1996 .

<sup>w</sup> <sup>x</sup> 13 P. Van Hentenryck, Constraint solving for combinatorial search problems: a tutorial, Proceedings of the First International Conference on Principles and Practice of Constraint Programming, Springer, Berlin, September 1995.

<sup>w</sup> <sup>x</sup> 14 J. Vanwelkenhuysen, R. Mizoguchi, Analysis of representational design decisions to create ontologies and guidelines, Journal of Japanese Society for Artificial Intelligence 11 2Ž . Ž . 1996 .

<sup>w</sup> <sup>x</sup> 15 COSYTEC, CHIP System Documentation, 1996.

![](/api/attachments/KNT6JNN5/fulltext/images/42dda6faf904e1f1f44f7f5715fa292d524b44617451a3bc18f638609da2172f.jpg)

Cristina Fierbinteanu is a Research Associate in the Information System Science Department at the Graduate School of Information Systems, University of Electro-Communications, Tokyo, Japan. She received her PhD in Information System Science from the University of Electro-Communications in September 1998, and MSc degree in Computer Engineering from the Polytechnical Institute of Bucharest, Department of Computers, in 1991. She was employed

at the Computer Center of the Romanian Railways National Society, as a System Analyst, between 1991 and 1993. In the same period she also worked as a part-time teaching assistant for the seminars of VLSI Design and Logic Control Design at the Department of Computers, Polytechnical Institute of Bucharest. This paper is the result of her research at the Railway Technical Research Institute, Tokyo, Japan, under the supervision of Professor Naotugu Nozue, between April 1994 and April 1998. The current research interests of Cristina Fierbinteanu are constraint programming in operations research, decision support systems and intelligent hypermedia.
