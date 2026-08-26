---
otero_id: 17496
otero_key: "W7RPMVCQ"
title: "A DSS for empty container distribution planning"
authors: "W.S. Shen; C.M. Khoong"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00037-s"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS for empty container distribution planning

W.S. Shen, C.M. Khoong \*

Information Technology Institute, 11 Science Park Road, Singapore 0511, Singapore

## Abstract

A decision support system to solve a large-scale planning problem concerning the multiperiod distribution of empty containers for a shipping company is presented. The system proposed uses network optimization models. Besides optimizing on container positioning across ports, the system is also able to recommend cost-effective container leasing-in and off-leasing decisions. Furthermore, the system incorporates constraint relaxation techniques that minimize perturbations to the existing planning decisions in response to ad-hoc changes in demands and supplies of empty containers.

Keywords: Decision support systems; Distribution planning; Network optimization

## 1. Introduction

Distribution planning is concerned with the flow of materials from supply points to demand points with minimal costs. The essential decisions to be optimized are: when to distribute the materials; how much of which type of material to distribute and; to which customer to distribute the material to.

A core problem faced by shipping companies is the distribution of empty containers to the ports that need them. Imbalances in supply and demand patterns for empty containers arise from imbalances in the usage patterns of containers for cargo. Based on case studies of some major shipping firms, a decision support system (DSS) for solving such a distribution planning problem is proposed in this paper. The DSS is based on network optimization models and heuristics. This

DSS goes beyond the standard distribution planning models in two key aspects. The network model proposed here caters for the leasing-in and off-leasing of containers from external sources, and charges the cost of leasing the containers according to the duration of lease. In addition, two algorithms are suggested to minimize the impact of changes in demands and supplies of empty containers to decisions made on the network model.

Network optimization models are chosen because they offer two selling points. First, it allows users to conceptualize problems graphically. Second, there exist efficient algorithms for solving large-scale network optimization models.

While the empty container distribution planning problem is not new – see for instance $[1-5]$ , existing literature has so far focused mainly on the technical aspects of the problem, rather than the business aspects. This paper takes a business process perspective, with emphasis on the shipping industry. Furthermore, unlike previous work, a detailed treatment of leasing considerations and constraint relaxations is provided in the models in this paper.

This paper is organized as follows. In section 2, a description of the problem domain is given. In section 3, we present a deployment framework that gives an overview of the solution model proposed. Section 4 gives a detailed description of the network model and section 5 describes two methods of minimizing the changes to the network model as a result of changes in the supply and demand of empty containers. The conclusion indicate some implementation issues and future directions in this area.

## 2. Problem domain

Containers are used to carry cargo from one port to another all over the world. The movements of containers from one port to another, due to the transportation of cargo, will always result in some ports having a surplus of empty containers and some ports having a shortage of empty containers to meet demand requirements.

Ports are partitioned into geographical regions. Each region has a group of ports with one main port. By virtue of trade activities, each port may either be a demand port demanding more empty containers to ship out the outbound cargo, or a supply port having surplus empty containers. The planning of container movement within a region is carried out by the respective regional office. All imbalance situations as a result of regional planning are then fed back to the headquarters, where the inter-regional movement planning takes place.

The planning decisions made to remove imbalance situations are:

(a) to lease containers from a leasing company, known as leasing-in,

(b) to return containers to a leasing company, know as off-leasing,

(c) to bring in containers from other ports, known as positioning-in and

(d) to move containers out to other ports, known as positioning-out.

The operational constraints governing the planning process include:

(a) there are business contracts governing the volumes of leasing from a company,

(b) a maximum off-leasing limit per month is usually imposed by the leasing companies,

(c) there are restrictions on the number of vessel slots (capacity) allocated for empty containers.

For planning purposes, a standard unit of measure for container volume is typically used. The standard unit in the shipping industry is the twenty-foot equivalent (TEU), which corresponds to the size of a twenty-foot long container. For transactional convenience some shipping companies prefer to plan in terms of numbers of forty-foot containers, which are the dominant container type in shipping traffic today. When the plans translate into implementation, there remains flexibility in the use of container types, since two twenty-foot containers are equivalent in volume to one forty-foot container. The DSS presented in this paper assumes that a single type of container is used.

## 3. The DSS deployment framework

The empty container distribution problem described in section 2 can be decomposed into three levels of inter-related planning problem, namely terminal (port) planning, intra-regional planning, and inter-regional planning levels. This decomposition reflects the way a shipping company would organize its global business, and therefore prescribes the deployment framework of the distribution planning DSS. The framework is depicted in Fig. 1, showing the communications among the three levels of planning.

There are three types of communications in the deployment framework:

(a) communications between the terminal planning models and the intra-regional planning model;

(b) communications between intra-regional planning models and

![](/api/attachments/W7RPMVCQ/fulltext/images/3eb190920312000f00dd3938855fc0e582eddf035f5cc5403e06bea0e5bb175f.jpg)  
Fig. 1. DSS deployment framework.

(c) communications between the intra-regional and the inter-regional planning model.

## 3.1. Communication between the terminal planning model and the intra-regional planning model

At each terminal (port), there is a terminal manager responsible for the operations of his port. A critical decision making process of the terminal manager is the inventory-sizing of empty containers at his port. The main port, once receiving all the information from each port in the region then solves the intra-regional planning problem. The intra-regional problem is a minimum cost flow problem where the nodes represent the ports in the region and the arcs represent the intra-regional service routes. Once the intra-regional problem is solved, the information is communicated to each of the ports with instructions as to where to send surplus containers to and how a shortage in containers is resolved (leasing-in or positioning-in).

## 3.2. Communication between the intra-regional planning models

A region itself can have imbalances of surplus or shortage of containers. In such an event, a region first tries to solve its imbalances by communicating to its nearby regions. If this method proves unsuccessful, a region can then communicate with the inter-regional planning model (headquarters).

3.3. Communication between the intra-regional planning models and the inter-regional planning model

The headquarters, upon receiving all the information necessary, can then solve the inter-regional planning problem. The inter-regional problem is also a minimum cost flow problem. But here, the nodes represent the regions and the arcs represent the inter-regional service routes. Once the inter-regional problem is solved, the information is again communicated down to each region.

Note that the empty container distribution planning process is a complex iterative one. Each iteration involves three stages. First, the regional offices solve the respective intra-regional problems without considering external agents (leasing companies). The outcome of stage one provides the surplus/shortage condition of each region, for the inter-regional planning to take place in stage two. Any unrectified imbalance is solved at the regional level, this time considering the options of leasing-in or off-leasing. By this sequence of planning, intra-regional positioning is given the highest priority in rectifying imbalance situations, followed by inter-regional positioning, and lastly, leasing-in and off-leasing.

## 4. The network optimization model

As mentioned in section 3, the Inter-regional and Intra-regional Planning Models are minimum cost flow problems. This section describes the network structure of the basic model (for the intra-and inter-regional planning level) to solve the empty container flow problem over a multi-period planning horizon. We also discuss the execution of the basic model and provide some extensions to cater for demands that cannot be met and to allow prepositioning of empty containers.

## 4.1. The basic model

The basic model optimizes the flow of empty containers over a multiperiod planning horizon, based on costs of holding, positioning, and leasing containers. The model assumes that all customer demands have to be satisfied. A schematic example of the network structure is shown in Fig. 2. The example consists of four ports modeled as nodes (A, B, C and D) over a planning horizon of three days. The arcs represent flow of empty containers from one node to another. As the model is formulated as a pure network, each port is duplicated for each planning period.

Each port at any period (from period 1 to period 3) can be a supply port or a demand port or both. For example, port A in period 2 is expected to have a demand of 20 containers (represented by an arrow pointing away from the node) and customers are expected to return 5 containers (represented by output arrow in diagram). The supplies and demands for other ports are not represented in the diagram to avoid cluttering of the diagram.

Each arc has 2 attributes: the cost and capacity. The cost of the arc, gives the cost of transporting one container across the arc, while the capacity of the arc, represented by the square brackets, gives the lower and upper bounds on the number of units of containers that may flow through the arc. The cost and capacity attributes are not shown for all arcs in the diagram.

The arcs connecting a port to itself in the next period (for example A1 to A2) represent the flow of inventory to the next period. The arcs from one port to another (for example, from node A1 to C2) represent shipping schedules.

The nodes Z11, Z12, Z21, Z22, Z31, Z32 and Z42 are dummy nodes introduced to the network model to cater for the leasing-in and off-leasing of containers. The arcs from node Z11 to each port in period 1 represent the containers leased-in by each port in that period. The arcs from each port in period 1 to node Z12 represent the containers that are off-leased in that period. Note that the arcs from the ports to the dummy leasing nodes are only represented in period 1.

Node Z11 has a demand of X containers (where X = number of containers leased from previous planning horizons that have not yet been returned). The arc from node Z12 to Z11 represent the containers that are off-leased in the first period. The arc has an upper bound of X. The arcs Zx2 to Zy1 (where x = 1, 2, 3, 4; y = 1, 2, 3 and x < y) represent the flow of containers that are off-leased. These arcs charge the leasing of containers according to the duration of leasing.

![](/api/attachments/W7RPMVCQ/fulltext/images/66c7cd25e5ec223b0c97b87453f073eb3e514cd7719af800c70719150946b7e9.jpg)  
Fig. 2. Schematic diagram of the network structure.

Node Z in the diagram is also a dummy node introduced into the network to ensure the balance of the supply and demand of containers in the planning horizon. The arcs to and from each node port to node Z represent the flow of containers to and from the ports to achieve the required ending inventory for each port. The arcs are assigned a penalty cost to penalize deviations from the required ending inventory. The arc from node Z to node Z42 represent the flow of containers to balance the leased-in containers that are to be returned in the future.

## 4.2. Executing the basic model

The basic model is executed iteratively to cater for any additional constraints or infeasibility that occurs during the planning process. In deciding to lease-in containers, there may be off-leasing constraints that have to be added to the model. Also, infeasible solutions (for example due to shortages in ship capacity) require input changes to overcome the infeasibility.

The basic model is also executed every period in a rolling horizon fashion. This is done to reduce the uncertainties of the deterministic aspect of the model (as suggested by Ouimet [6] in the review paper by Dejax and Crainic [3]) and any changes to the model such as cancelled demands or additional demands and constraints can be accommodated. However, complete recomputation of the model on decisions that have already been committed is avoided. This is because changes to too many committed decisions will hamper the smooth running of the terminals. Section 5 discusses in detail how the changes can be minimized.

## 4.3. Extensions to the basic model

## Modification to cater for situations where demands are not necessarily met

In situations where demands are not-necessarily met due to non-profitable demand or shortage of supply, the following changes are made to the network model (shown only for port D in Fig. 2):

For each port in the network (from period 1 to 3), a dummy node is created to act as the demand port (if the port has a demand). For each port, two arcs are created to model this problem. The first is an arc from a port to its corresponding dummy node with a lower and upper bound equal to the demand of the port for that period (for example, if the demand at port D in period 3 is 8, then the lower and upper bound for the arc is 8). The associated cost for the arc is zero. The second arc is from the dummy node Z, to each port node in period 1 to period 3 (only shown for node D3). The arc has a lower bound of zero (meaning all demands are met) and an upper bound of the demand for the port (meaning all demands are not met). This arc represents demand that are not met and as such has an upper bound of the demand for the port. The associated cost of the arc is the profit lost from the unmet demand.

## Modifications to cater for prepositioning of empty containers

To model a way of prepositioning excess empty containers so that future demands can be met, two additional arcs are added to the network between a port and its corresponding port in the next period (also only shown for port D in Fig. 2). The middle arc has a lower and upper bound of the ideal inventory level for the port. In the case of port D, the ideal inventory level is assumed to be 35. The top arc represents excess empty containers above the ideal inventory for the port. The arc has a lower bound of zero and an upper bound of the capacity of the port minus the ideal inventory level (for example, if the capacity of port D is 800 containers, then the upper bound is 800-35). The arc has an associated cost (higher than the inventory cost of keeping the containers) to penalize excess storage of empty containers above the ideal inventory level. The bottom arc is a back arc which corresponds to the number of empty containers short of the ideal inventory. The arc has a lower bound of zero (meaning the ideal inventory is fully met) and a upper bound of the ideal inventory (meaning the inventory brought forward to the next period is zero). The arc has an associated cost of the expected lost in revenue from future unmet demands.

## 5. The network model with constraint relaxation

In order to minimize changes to the commitments made, two strategies are presented. The first strategy aims to minimize the total cost of relaxation. The second strategy aims to minimize the number of relaxation. The second strategy assumes that the cost of relaxing a constraint is extremely high and is only performed when there is no other alternative (i.e., the solution would be infeasible without relaxing arcs).

## 5.1. Minimizing the total cost of relaxation

For this strategy, as commitments are made on decisions, changes are made to the network model described in section 4.1.

If the commitments made can be relaxed with a penalty cost, the following changes are made (referring to Fig. 3):

(1) The upper and lower bound of the original arc (arc a) is changed to reflect the commitment made. For example if a commitment was made to ship 10 empty containers from port A to port B then both the upper and lower bounds for the arc are set to 10 provided it is within the original bounds of the arc.

(2) An additional arc (arc b) with the same direction as the original arc is created (for adding additional containers). The cost of the arc is the penalty cost for changing the commitment made. The lower bound of the arc is set to zero and the upper bound is set to the maximum change allowed.

![](/api/attachments/W7RPMVCQ/fulltext/images/dc3222be040701fd44917abea5829e285e7c764206cba112e99ba75cdb545044.jpg)  
Fig. 3. Changes to arcs with commitments that can be relaxed.

![](/api/attachments/W7RPMVCQ/fulltext/images/cc4d99343bd499f46441606f67742f877c9fde3919b7f66cb0bc3d442f4d1a06.jpg)  
Fig. 4. Changes to arcs with commitments that cannot be relaxed.

(3) A second arc (arc c) is added in the opposite direction of the original arc (for cancelling the commitments made). The cost of the arc is again the penalty cost for the commitment made (can be different from the penalty cost of the arc in 2.). The lower bound of the arc is set to zero and the upper bound has a maximum of the commitment made (i.e., maximum of 10 containers).

If the commitment made may not be relaxed, the upper and lower bound of the arc is changed to reflect the commitment made as in the case where the commitment may be relaxed. Fig. 4. depicts the change made for commitments that cannot be relaxed.

The intra-regional and inter-regional models are then executed using the rolling horizon method and the model will minimize the total cost of distributing the empty containers to each port. Arcs with no commitments made may be changed freely without incurring additional costs.

## 5.2. Minimizing the number of relaxations

There are two ways of solving this problem. The first alternative was to built a fixed charge network flow model which charges a fixed cost to an arc if the flow in that arc is greater than zero. Unfortunately, this method requires the model to be formulated as an integer program, and as such, it is an NP-Hard problem. The second alternative was to develop a heuristic to find the minimum number of relaxation that had to be performed.

Using the second alternative, as commitments are made, changes are made on the arc to reflect the commitment made as in Fig. 4. The model is then executed in a rolling horizon fashion. If the solution is feasible, the process is repeated (updating demand and supplies) and executing the model for the next cycle. If the solution is not feasible, we then determine the minimum number of relaxation that has to be undertaken to make the solution feasible.

## Heuristic to minimize number of relaxations

Assume the model that is infeasible is Model A. Also assume that the infeasible solution is caused by a shortage of X containers and the port known as the problem node. The heuristic can be thus executed in the following algorithm:

Heuristic algorithm.

(1) Construct a replica of model A (call it model B)

-Process commitments that can be relaxed (as in Fig. 3)

-Change cost of rest of the arcs to zero

(2) Determine the cost of each committed arc that can be relaxed

-Assume (in Fig. 3), node B is the problem node then arcs $a$ and $c$ are assigned a cost of zero and arc $b$ is assigned $\mathbf{C}_{ij}$ where

$$
\mathrm{C} _ {\mathrm{ij}} = \mathrm{w} _ {1} \mathrm{PCAP} _ {\mathrm{ij}} + \mathrm{w} _ {2} \mathrm{DIST} _ {\mathrm{ij}} + \mathrm{K},
$$

where

$PCAP_{ij}=cost associated to the capacity of the arc$

$DIST_{ij}=cost associated to the duration from node i to the problem node$

$w_{1}, w_{2} =$ user defined values

$$
\mathrm{K} = \text { constant }, > 0
$$

(3) Model B is then executed to determine the relaxations to be performed.

If only one arc needs to be relaxed, an optimal solution is found

Else if the user is satisfied with the solution, a satisficing solution is obtained

Else increase the cost of the arc with the least number of used capacity (other than the arc with the highest cost) by the maximum value of $C_{ij}$ . Used capacity is defined as the number of containers that flowed through the relaxation arc.

Repeat Step 3.

(4) Once a solution is obtained, model A is then modified to reflect the relaxations performed. It is then executed to determine the flows of all other arcs (with no commitments) in the model.

## 6. Conclusion

The network optimization model proposed is solved using AMPL. An Excel spreadsheet frontend serves as the interface with the user for data input and output. Codes written in C generate models for AMPL from input data, and extract AMPL optimization results for output to Excel.

The proposed DSS described above can also be applied to land transportation systems (e.g.

![](/api/attachments/W7RPMVCQ/fulltext/images/3084c0d023cc023113ba17b473b44bdbf593dbcc1692e4eb17cbe56a37b6f90f.jpg)  
Fig. 5. Business processes relating to the container division.

(trucking companies). However, for both land and sea systems, further work needs to be carried out on the related business processes (see Fig. 5). For example, in the functional area, DSSs need to be developed for the Cargo Division which decides the loaded container movement, Line and Crew Scheduling Division, Ship routing and liasoning with Port Authorities to control container loading and unloading.

From the technology standpoint, techniques such as artificial intelligence and forecasting can be used to support and complement the solutions generated by the DSS. Rule-based expert systems can help in deciding how loading and unloading of containers should be carried out onto and from a ship. Constraint programming can be used in the scheduling of ships and crew while case based reasoning can be used to decide user defined variables in estimating the cost of relaxing an arc (in section 5.2). Forecasting techniques enable more accurate predictions of future demands for empty containers and will ultimately lead to better prepositioning of empty containers to the various ports.

The globalization of shipping businesses may also point to needs for group decision support systems (GDSS) and other computer-supported cooperative work (CSCW) software. The opportunities for advanced computer technologies in this domain are vast and challenging.

## References

[1] Ahuja, R.K., Magnanti, T.L., and Orlin, J.B., Network Flows: Theory, Algorithms, and Applications (Prentice Hall, Englewood Cliffs, NJ, 1993).

[2] Aronson, J.E. (1989), A survey of dynamic network flows. Annals of Operations Research 20 (1989) 1–66.

[3] Crainic, T.G., Gendreau, M., and Dejax, P., Dynamic and

stochastic models for the allocation of empty containers. Operations Research 41 (1993) 102–126.

[4] Dejax, P.J., and Crainic, T.G., A review of empty flows and fleet management models in freight transportation. Transportation Science 21 (1987) 227–247.

[5] Mendiratta, V.B., and Turnquist, M.A., Model management of empty freight cars. Transportation Research Record 838 (1982) 50–55.

[6] Ouimet, G.P., Empty freight car distribution. Master Thesis, Queen's University, Kingston, Ontario, Canada, 1972. Ratcliffe, L.L., Vinod, B., and Sparrow, F.T., Optimal prepositioning of empty freight cars. Simulation (June 1984) 269–275.

![](/api/attachments/W7RPMVCQ/fulltext/images/a6440f58f0c32c9ac2721dcf1887f2a9651360c66c6f32f7989d4b7916a66289.jpg)  
Wong Shaw Shen has been involved in the design and development of distribution planning and scheduling systems since 1993. He joined the Information Technology Institute in 1994., where he contributes to a focused effort in logistics management applications. He obtained his B.Sc. (Hons.) degree in computer and information sciences from the National University of Singapore.

![](/api/attachments/W7RPMVCQ/fulltext/images/cbc6bd61a206d559d8a4b83713af5c2166b0693cc5a7e9bd60642ecd9dcd1b77.jpg)

Chan Meng Khoong is a specialist in DSS development and business process reengineering (BPR) in the Information Technology Institute. He regularly provides consultancy to user organizations on BPR, DSS feasibility studies, and system design. He is the principal investigator in the development of manpower planning, manpower scheduling, and distribution planning systems. He maintains active research interests in operations man-

agement, optimization, artificial intelligence, BPR, and theoretical computer science. He has authored more than 60 technical publications in journals, books, and conference proceedings. He sits on IFIP Technical Committee 7 (System Modelling & Optimization), and is a member of the ACM, IEEE Computer Society, ORSA, and Singapore Computer Society.
