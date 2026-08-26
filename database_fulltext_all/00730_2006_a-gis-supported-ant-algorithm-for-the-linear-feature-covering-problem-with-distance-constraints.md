---
otero_id: 730
otero_key: "H2RXZQGQ"
title: "A GIS supported Ant algorithm for the linear feature covering problem with distance constraints"
authors: "Bo Huang; Nan Liu; Magesh Chandramouli"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.09.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A GIS supported Ant algorithm for the linear feature covering problem with distance constraints

Bo Huang <sup>a,\*</sup>, Nan Liu <sup>b</sup>, Magesh Chandramouli <sup>c</sup>

<sup>a</sup> Department of Geomatics Engineering, University of Calgary, Calgary, AB, Canada T2N 1N4 <sup>b</sup> Department of Statistics and Operations Research, University of North Carolina at Chapel Hill, NC 27599, United States <sup>c</sup> GIS Research Center, 100, Wenhwa Road, Feng Chia University, Taichung 407, Taiwan

Received 23 November 2004; received in revised form 7 July 2005; accepted 14 September 2005 Available online 21 October 2005

## Abstract

This paper analyzes a linear feature covering problem (LFCP) with distance constraints, and characterizes the problem by a fuzzy multi-objective (MO) optimization model. An integrated approach combining an Ant algorithm (LFCP-Ant) and a Geographic Information System (GIS) has been devised to solve the LFCP problem in large scale. The efficacy of the proposed approach is demonstrated using a case study of locating new fire stations in Singapore. A GIS has been used to transform the continuous problem into a discrete one, which is then solved using the LFCP-Ant. This algorithm employs a two-phase local search to improve both search efficiency and precision. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Ant algorithm; Linear feature covering problem; GIS; Two-phase local search

## 1. Introduction

A typical linear feature covering problem (Fig. 1) with distance constraints consists of m polylines (m is 5 in Fig. 1) and n points (shown as dots in Fig. 1 and termed as potential location. n is 8 in Fig. 1) located at a Cartesian plane. In such problems, polylines are considered as lines composed of one or more linear line segments. Given a critical distance R, a desired balance distance D, and an integer number p ( p is 4 in Fig. 1), the locations of p (out of n) points (for p new facilities)

are to be selected so that the total length of those polylines lying within distance R of at least one point is maximized. Also, the distance between each new point and its nearest point must also maximally approach the desired balance distance D. The aforementioned problem is a bi-objective optimization problem, i.e. a MO (Multi-Objective) optimization problem with two objectives. The problem simultaneously considers linear feature coverage maximization (termed as objective A) and distance balancing (termed as objective B). To facilitate the understanding of objective A, we may take the points as supply side while regard polylines as demand side. Without losing generality, we may suppose that the demands are uniformly generated from the polylines, hence maximizing the coverage of polylines is equivalent to satisfying the demands maximally. Besides objectives A and B, other objectives might also be considered, e.g. minimizing the maximum distance from a point to a linear feature. Nevertheless, such objectives are supplementary, and this paper addresses primarily the optimization problem with the aforementioned two objectives.

![](/api/attachments/H2RXZQGQ/fulltext/images/a130254ee9eedc3237aff8f4ff6b5bd14b59d87db492f6254cff005e8d25846f.jpg)  
Fig. 1. Linear feature covering problem.

Problems of this kind occur in a variety of practical applications, especially in locating emergency and protection facilities. Locating new fire stations under plan is an archetypal representation of such a problem. Fire stations offer the personnel and equipment for protecting lives and belongings, and their location considerably influences their emergency response and fire protection abilities. While situating fire stations, the following two factors must be considered: (1) The stations should be capable of providing <sup>d</sup>timely aid<sup>T</sup> when a road-accident or a mishap involving hazardous materials occurs; (2) There should be a reasonable distance between two fire stations [14], in order that any two fire stations may cooperate more easily and efficiently. Simply stated, all fire stations should be distributed <sup>b</sup>evenly<sup>Q</sup> over the land, so as to be able to provide necessary protection to the largest possible area.

Location problems with distance constraints have been studied by researchers during the past several decades. Cooper and Drebes [4] presented a set covering approach involving a heuristic procedure to determine the minimum number of centers to cover all customers. However, this objective is significantly different from those dealt in our MO problem and hence the approach adopted in [4] is not relevant for the case discussed herein. Watson-Gandy [15] provided three heuristics and their variations to solve the mpartial cover problem (maximal covering problem) on a Cartesian plane. Their objective was to situate m centers so as to maximize the sum of the weights of those points lying within a critical distance (R) of at least one center. Even though this appears to be in line with objective A considered in this paper, Watson-Gandy [15] has not considered objective B (distance balancing) in their work. In some discrete location problems, distance constraints also do exist, e. g. the set covering problem and the maximal covering problem [5]. Such discrete problems are usually formulated as an Integer Linear Programming Problem (ILPP) and solved either by branch-andbound approaches or Lagrangian relaxation heuristics. However, the demands in all these problems originate from nodes and hence the demand nodes can be easily recognized using a coordinate pair (x, y). It can be overtly judged if a demand node is covered by a supply facility (node). This is done by comparing the critical covering distance R with the Euclidean (network or user defined) distance between the two nodes. Nevertheless, in our case, we are dealing with polylines rather than points. The fire stations that are to be situated should serve accident locations uniformly distributed along particular routes and are not situated at points whose locations are known well in advance. This can hardly be expressed in a general mathematical equation and presents tremendous challenge in determining the percentage of polylines that have been covered. Simply put, it is hard to find a way to evaluate the objectives when the demand is originated from polylines. As will be discussed below, we solve this problem by discretizing the polylines into a series of connected cells. Although this makes it possible to model the whole problem in ILPP, the combinatorial complexity prohibits us to do so. This will be detailed later.

Badri et al. [1] stressed the need for a MO model in determining fire station locations. They employed a multiple criteria modeling approach via integer goal programming to evaluate potential sites in 31 subareas in the state of Dubai. Their model determines the location of fire stations and the areas the fire stations are supposed to serve. They considered 11 strategic objectives including travel times, travel distances and also other cost-related objectives. They also took into account several other technical and political criteria, or other factors satisfying certain system requirements. However, the integer goal programming used in [1] is not applicable for our problem since: (a) the objectives considered are different, and (b) if not discretized, the problem itself cannot be modeled into an integer goal programming problem; if discretized, it still would be a very large computational problem which cannot be solved using integer goal programming. Tzeng and Chen [14] used a fuzzy MO approach to determine the optimal number and sites of fire stations in Taipei’s international airport. Their paper utilized a genetic algorithm (henceforth called TC-GA) and compared with the brute force enumeration method. From literature review, we find that TC-GA [14] is the most pertinent approach, in view of the nature of our problem. Even though the results showed that the GA is appropriate for solving similar location problems, its efficiency in large scale problems is yet to be verified.

This paper explores a fuzzy MO model to characterize a large scale Linear Feature Covering Problem (LFCP). The continuous problem is transformed into a discrete one using a Geographic Information System (GIS). In the discretized problem, the polylines are represented by a string of discrete coordinate pairs, thus facilitating easy determination of their coverage. As such, a continuous optimization location problem is converted to a discrete combinatorial optimization problem. This discrete optimization problem is then solved using the LFCP-Ant, a novel Ant algorithm, which, to the best of our knowledge, has not been attempted before. This algorithm takes advantage of a two-phase local search to enhance search efficiency as well as accuracy.

The remainder of this paper is organized as follows. At the outset, the fuzzy MO formulation of the problem is presented. Then, a brief prologue to GIS and its application in converting a continuous plane and road lines into grid cells is given. This is followed by a detailed discussion of the proposed Ant algorithm, LFCP-Ant. A case study of determining the locations of new fire stations in Singapore using our proposed approach is then presented. A computational study between the LFCP-Ant and TC-GA in [14] is also carried out to benchmark the efficiency of LFCP-Ant. Finally, the paper concludes with a summary and outlook.

## 2. A fuzzy multi-objective model formulation

Of the several known methods to resolve MO optimization problems, the weighting method, the constraint method and the weighted minimax method are three common ones for characterizing Pareto optimal solutions for MO problems. Sakawa [12] provided a detailed review on these three methods applied to both MO linear and nonlinear programming problems. The fuzzy k transformation is a variant of the weighted minimax method, and it can be viewed as an equalweighted minimax method. The fuzzy MO optimization approach is used in this research since it is simple and more efficient when compared to traditional weighting methods related to utility functions for MO optimization [12].

The fuzzy MO optimization model of the LFCP with distance constraints is formulated as follows:

$$
\max _ {L} \lambda
$$

Subject to

$$
\lambda \leq \mu_ {i} [ L ], \forall i = A, B
$$

where L is a solution vector that represents the locations of new facilities; $\mu _ { i } [ L ]$ is the membership function of objective i which turns a given solution L to its achievement level (a real number between 0 and 1) against objective i. The larger the $\mu _ { i } [ L ]$ , the higher the achievement level of objective i. The fundamental idea of fuzzy MO optimization is to find the maximal achievement level among constraints of conflicting objectives [12].

In the above problem, the membership function of objective A is defined as:

$$
\mu_ {\mathrm{A}} (x _ {\mathrm{A}}) = \frac {x _ {\mathrm{A}} (L)}{x _ {\mathrm{A}} ^ {+}}
$$

where $x _ { \mathrm { A } } ( L )$ is the total length of linear features covered by at least one facility within the critical distance $R ; { x _ { \mathrm { A } } ^ { + } }$ is the total length of all linear features.

The membership function of objective B is defined as:

$$
\mu_ {\mathrm{B}} (L) = \min \{x _ {\mathrm{B}} (l), \forall l \in L \}
$$

where:

$$
x _ {\mathrm{B}} (l) = \left\{ \begin{array}{l l} 1 & \text {   If   } d _ {l} = D \\ (D ^ {\mathrm{U}} - d _ {l}) / (D ^ {\mathrm{U}} - D) & \text {   If   } D ^ {\mathrm{U}} d _ {l} > D \\ (d _ {l} - D ^ {\mathrm{L}}) / (D - D ^ {\mathrm{L}}) & \text {   If   } D > d _ {l} D ^ {\mathrm{L}} 0 \quad \text {   Otherwise   } \end{array} \right.
$$

where D is the desired distance; $D ^ { \mathrm { U } }$ and $D ^ { \mathrm { L } }$ are the tolerable upper bound and lower bound distance between two facilities, respectively; and $d _ { l }$ is the distance between the new facility located at l and its nearest counterpart (including all existing and new facilities).

## 3. GIS technology support

A GIS is a computer system designed to efficiently capture, store, update, manipulate, analyze, and display all forms of geographically referenced information [3]. ArcGIS, a comprehensive Geographic Information System developed by ESRI, Inc. is used in this research. ArcGIS offers a number of powerful spatial analysis functions; however, it does not provide a direct way to solve the LFCP proposed in this paper. Nevertheless, it can be used to pre-analyze the problems and evaluate the results. In our case, ArcGIS is used to convert a continuous plane into a raster map (grid map), wherein the map elements, e.g. polylines and polygons, are represented by a definite number of discrete cells under a grid coordinate system (Fig. 2).

The cell size is the principal factor to be considered when converting a map into a raster. The cell size should be neither too large nor too small since both are unsuitable for large scale applications. Extremely small cell-size leads to huge storage demands and causes computational burdens, while very large cellsize can lead to intolerable errors. After conversion, the continuous plane becomes a grid map and all map elements are defined as sets of cells represented in coordinate pairs. The continuous problem can now be treated in a discrete manner, like formulating a traditional ILPP. However, the ILPP method is not an efficient technique to solve large scale problems of combinatorial complexity [14]. For instance, we need to pick 6 locations from 26,875 (125  215) cells. It may not be a good choice to define 26,875 binary decision variables in order to use the ILPP method. Consequently, an Ant algorithm, i.e. LFCP-Ant, is proposed here instead of using a traditional ILPP for solving our large scale location problem.

![](/api/attachments/H2RXZQGQ/fulltext/images/351123cad8e54578f22c391e3a5062aa68ed42cb39fa551f87cf06e69a5794ba.jpg)  
Fig. 2. A linear feature and its raster representation.

Before the LFCP-Ant can be used, the MO optimization model and membership functions defined in Section 2 are re-interpreted as follows. On a grid map, the facilities are located in grid cells and their locations are represented as the centroids of the cells they site. Recall the objective A considered in LFCP is to maximize the linear features that can be served by certain facilities. In a grid map, $x _ { \mathrm { A } } ( L )$ is the total number of linear feature cells covered by at least one facility within the critical distance $R ; { x _ { \mathrm { A } } ^ { + } }$ is the total number of all linear feature cells. In the objective B considered in LFCP, the distance between two facilities can be measured as a Euclidean distance between the centroids of the cells where the two facilities are located. The membership function remains the same as introduced in Section 2.

## 4. LFCP-Ant: an improved Ant algorithm for the LFCP

The Ant Colony Optimization Metaheuristic (henceforth called the Ant algorithm), just like the GA methodology that simulates the natural selection wherein the fittest survive, is also inspired by nature. It emulates the behavior of an ant colony that finds the shortest route between the food source and its formicary location. The Ant algorithm is an adaptive construction heuristic that combines with a local search algorithm. The original Ant algorithm, AS (Ant System), was first brought forward by Dorigo [6]. Subsequently it drew a great deal of attention leading to various innovations on the original algorithm. Those improved or variant Ant algorithms include ACS (Ant Colony System) [8], Ants [11], MMAS (MAX–MIN Ant System) [13], Ant-Q [7], and ${ \mathrm { A S } } _ { \mathrm { r a n k } }$ (Rank-based Ant System) [2], etc. The Ant algorithm has been viewed as one of the most efficient approaches for well-known combinatorial problems, e.g. TSP (Traveling Salesman Problem), QAP (Quadratic Assignment problem) and VRP (Vehicle Routing Problem). The Ant algorithm proposed in this paper, LFCP-Ant, is innovative due to the following reasons: (1) it is designed to solve a novel multiobjective problem; and (2) it employs a new local search measure that adapts the Ant algorithm to excel in solving large scale location problems.

A certain number of artificial ants, equal to the number of the new facilities (i.e. p), are used in LFCP-Ant to represent the locations of the new facilities to be built. The movement of the artificial ants on the grid system is governed by certain principles that attempt to find the optimal (or sub-optimal) locations of the new facilities, within a certain number of iterations. The generic flowchart of the algorithm is given in Fig. 3. Like other Ant algorithms, LFCP-Ant consists of several key components, including the trace matrix, the solution construction rules, the two-phase local search and the diversion mechanism. These components will be detailed in the subsequent sections.

## 4.1. Trace matrix

The Ant algorithm uses a special mechanism called the <sup>d</sup>trace matrix<sup>T</sup> to store the historical <sup>b</sup>good<sup>Q</sup> information. In LFCP-Ant, the trace matrix is a two dimensional matrix corresponding to the grid system. Each cell of the matrix has a float value representing the <sup>b</sup>desirability<sup>Q</sup> of choosing the corresponding cell (i, j) of the grid system (i is the row number and j is the column number) as a probable location for one of the new facilities. LFCP-Ant determines the locations of the new facilities by controlling the artificial ants to sense such desirability and driving them to move to those desirable cells. The probability of an ant choosing a certain cell is a function of the <sup>b</sup>desirability<sup>Q</sup> of that cell. The larger the <sup>b</sup>desirability<sup>Q</sup> of the cell is, the higher the probability of the ant opting to move to that cell.

![](/api/attachments/H2RXZQGQ/fulltext/images/4ec7c4512f4a1e59f43b52b51af204685ec3c4b5a464d6692ba5cac0124ca75d.jpg)  
Fig. 3. The flowchart of LFCP-Ant.

The initial solution, based on the initial trace matrix devoid of any information, is to randomly pick six cells as the locations for the new fire stations. As no information is contained in the trace matrix when the algorithm is instigated initially, the same value is assigned to all feasible cells. This initial value for the feasible cells is usually the local enhancement level (as described below), while the infeasible cells are assigned a zero-value. Feasible cells refer to those which may serve as suitable sites for the purpose being considered (here, for situating fire-stations). On the other hand infeasible cells refer to those which are unsuitable for locating fire-stations, for instance those cells on water bodies, mountains, etc.

In compliance with an update policy, the trace matrix is updated as iterations occur when the Ant algorithm is executed. This update policy consists of two sub-routines, the global update and the local update. This mutual update policy takes complete advantage of the local as well as global information. The global update is to enhance the <sup>b</sup>desirability<sup>Q</sup> values of those cells that constitute the global best solution or the best solution ever found. The local update aims to fortify the <sup>b</sup>desirability<sup>Q</sup> of those cells that construct the local best solution, which is the best solution found in the local search process. The rationale of the matrix update policy is that the cells which form good solutions have higher probabilities of being the components of the optimal solution.

The mathematical formulation of the update policy is as follows.Local Update:

$$
\tau_ {i j} (t + 1) = \tau_ {i j} (t) + \Delta \tau_ {i j} ^ {\mathrm{local}} \cdot x _ {i j} (t)
$$

Global Update:

$$
\tau_ {i j} (t + 1) = \tau_ {i j} (t) + \Delta \tau_ {i j} ^ {\text { global }} \cdot y _ {i j} (t)
$$

where:

$\tau _ { i j } ( t )$ the <sup>b</sup>desirability<sup>Q</sup> value of the cell $( i , j )$ at iteration t;

$x _ { i j } ( t )$ a dummy variable, which equals 1 if the cell $( i , j )$ is included in the local best solution at iteration t, otherwise zero;

$y _ { i j } ( t )$ a dummy variable, which equals 1 if the cell $( i , j )$ is included in the global best solution at iteration t, otherwise zero;

$\Delta \tau _ { i j } ^ { \mathrm { \scriptsize ~ l o c a l } }$ and $\Delta \tau _ { i j } ^ { \mathrm { g l o b a l } }$ the local and global enhancement levels, respectively.

## 4.2. Rules for solution construction

The solution construction is based on the trace matrix. The construction is implemented in the form of a linear search through a roulette wheel with slots weighted in proportion to cell values in the trace matrix. In other words, the probability of choosing the cell $( i , j )$ as the location for one of the new facilities is calculated by:

$$
P _ {i j} (t) = \frac {\tau_ {i j} (t)}{\sum_ {\forall i} \sum_ {\forall i} \tau_ {i j} (t)}
$$

where $P _ { i j } ( t )$ is the probability of choosing cell $( i , j )$ at iteration t. Other notations are the same as those mentioned above. This formula indicates that the larger the cell value, the higher the probability that the cell will be included in the solution.

## 4.3. Two-phase local search

The local search is done immediately after the new solution construction; after which the local search repeatedly attempts to better the current solution by introducing local changes. If a better solution is found in the <sup>b</sup>neighborhood<sup>Q</sup> of the current solution, the current solution is replaced by the better one and a new search restarts from this better solution.

A two-phase local search algorithm is developed in the LFCP-Ant discussed here. At the first phase, multiple ants move concurrently in order to improve the objective achievement level; at the second phase, if better solutions are found in the first phase, each ant moves independently trying to refine the solution found in the first phase.

The first phase of the local search is called the neighborhood random search (NRS). Within iterations of the NRS, all the ants will simultaneously make a random move from their current cells to other cells within a limited distance, e.g. 3 km. Upon re-evaluation, if a better solution is found, the ants move to the cells that constitute the better solution; otherwise, the ants continue to remain on the original cells. The NRS is conducted for a certain number of iterations.

If better solutions are found in the first phase of local search, the second phase of local search, namely adaptive myopic neighborhood search (AMNS), is activated. In AMNS, each ant moves to every individual cell within a specific distance, e.g. 0.5 km, from its current position while other ants remain on their original cells. The program then checks whether the objective value has improved. If so, the ant will enter the cell that improves the objective value and a new AMNS starts.

The AMNS is a thorough and intensive local search method, as it carries on till no further movements of the ants can improve the objective value. The <sup>b</sup>myopic<sup>Q</sup> disadvantage of the AMNS lies in that it only considers the effect of moving only one ant, while not taking into account the interactive effect of multiple moving ants. Thus it might lose a better solution which can only be acquired by moving multiple ants concurrently. However, the AMNS is used in order to reduce the computation complexity. For example, supposing that an ant has n alternative cells to choose, the computation complexity of using the AMNS will be proportional to $k ^ { \cdot } n$ (k is the total number of ants); on the other hand, if moving multiple ants is considered, the computation complexity will be proportional to $n ^ { k } ,$ , which can be unbearable if n or k is large.

## 4.4. Evaporation

Evaporation is a commonly used measure in some other Ant algorithms, e.g. ACS (Ant Colony System) in [8], to force ants to forget the <sup>b</sup>bad<sup>Q</sup> information collected before and prevent the algorithm from falling into a local optimum. Towards the end of each iteration, the evaporation mechanism is activated in the Ant algorithm and controlled by a parameter named evaporation ratio. This leads to the reduction of cell values in the pheromone matrix. For example, if the evaporation ratio equals 10%, then the value of each cell in the pheromone matrix will be reduced to 90% of its original value.

## 4.5. Diversion mechanism

Diversion is a mechanism used in some Ant algorithms (e.g. [8]) to prevent the algorithms from falling into a local optimum. The mechanism is to be activated if the algorithm cannot make an improvement on the current best solution within the last N iterations, namely diversion step (DS). A counter called Inner Iteration Number (IIN) is used to record the number of iterations that the program has run within a DS (note that IIN V DS). The value of IIN determines whether the trace matrix should be re-initialized. It is noted that the diversion mechanism is an optional component of the proposed LFCP-Ant. If LFCP-Ant does not include diversion, then the algorithm will determine whether the stop criteria have been attained right after the evaporation.

## 5. Case study: locating new fire stations in Singapore

## 5.1. Background

In Singapore, the transportation of hazardous materials (HAZMATs) is governed by the National Environment Agency (NEA) and the Singapore Civil Defense Force (SCDF). According to the Environmental Pollution Control (Hazardous Substances) Regulations under the Environmental Pollution Act, as well as the Fire Safety Act, the authorities have specified the approved routes (SCDF routes) for transporting HAZMATs and other petroleum products (Fig. 4). These routes, which pass through the whole of Singapore, are planned so that the vehicles avoid densely populated areas and water catchment areas.

At present, there are 19 fire stations spread over the whole island of Singapore, each having a basic equipment of at least 1 fire engine, 1 red rhino and 1 ambulance. The current response time for a fire engine is 8 min; the time from the receipt of a call to the time of arrival of the fire engine on the accident site along the SCDF approved routes.

Emergency response has been given a renewed emphasis in the wake of September 11, 2001. In order to improve response efficiency, local authorities plan to construct six new fire stations, thus providing better coverage. As a result, the authorities intend to make the SCDF routes fall within a reach of 5 min from at least one fire station, and to aim to fine-tune the spatial distribution of all fire stations. This is to ensure that the distance between a new fire station and its nearest counterpart is within a range of 1–9 km, while the desired distance is 5.0 km. It is assumed that the probability of an accident is uniformly distributed along the SCDF routes. Stated precisely, this is a special case of the LFCP with distance constraints. However, the Singapore map is not an unlimited Cartesian plane, but an irregular plane with boundaries where fire stations can be sited. The capabilities of GIS are employed here since it is able to recognize those raster cells within the required boundaries and set them as the candidates for the locations of fire stations. Thus, we proposed to use the fuzzy MO optimization model established in Section 2 to characterize this problem, and resolved it by combining a GIS and the LFCP-Ant.

The parameters in the fuzzy MO optimization for this case are as follows: D (the desired distance) is 5.0 km; $D ^ { \mathrm { U } }$ (the tolerance upper bound) is 9.0 km; $D ^ { \mathrm { L } }$ (the tolerance lower bound) is 1.0 km; ${ x _ { \mathrm { A } } ^ { + } }$ (the total number of all uncovered SCDF route cells) is 1967. It must be noted that the SCDF route cells are micro cells as discussed subsequently.

![](/api/attachments/H2RXZQGQ/fulltext/images/6029f947269c1518506ad843e91437b1e22258978130c25a01a0ff9b326e64b5.jpg)  
Fig. 4. Existing fire stations and the SCDF routes in Singapore.

## 5.2. Macro and micro grid system

As stated previously, the cell size of the raster map is of paramount importance in converting a continuous map into a grid map. In order to keep the computations within a tolerable range and simultaneously ensure data accuracy, special considerations have been made. Two grid systems (micro and macro) of two cell sizes are used in this case. The micro raster map uses a small cell size of 25 m. The micro map consists of 1000 rows and 1726 columns, and is used to rasterize the SCDF routes and determine the number of route cells covered by at least one fire station in 5 min. The cell size of 25 m is precise enough to limit the errors arising when evaluating objectives to a small range.

The area where the fire stations are to be sited is represented by a macro raster map (125 rows  215 columns) using a larger cell size of 200 m. The map’s extent is snapped to the micro map to ensure that the macro grid coincides with the micro grid. The larger cell size of the raster map is determined by the regular size of the current fire stations and their surroundings in Singapore, which is around an area of 200 m  200 m. The macro map is used to reduce the computation burden and hence decrease the processing time involved.

In Fig. 5, the macro grid of 200 m  200 m is represented by the larger squares. The smaller squares (25 m  25 m) located within the larger macro squares constitute the micro grid. The location of a macro cell or a micro cell is represented by its centroid and the distance between two locations is measured as the Euclidean distance between the two corresponding centroids. During the implementation of LFCP-Ant, all ants run on the macro grid, i.e. the fire stations are located by macro grid cells. While evaluating objective A, micro cells are used. Whether or not the route cells are covered by the fire stations is determined by an all-or-nothing policy, i.e. if the distance between a macro cell and a fire station is less or equal to the critical distance R, then all the route cells (micro cells) in that macro cell are regarded as covered; otherwise, neither of the route cells are covered. In Fig. 5, on the micro grid, those route cells which are within the coverage of the fire station, i.e. within the buffer from the fire station, are shown in black. The route cells which lie outside the coverage are shown in grey. When evaluating objective B, the distance between two fire stations is simply measured as the Euclidean distance between the centroids of the sited cells. The membership function remains the same as in Section 2.

## 5.3. Calibration of the response time function

Fig. 4 shows the SCDF routes and the existing fire stations distributed in Singapore. Current regulations require that the fire engines reach any part of the SCDF approved routes within 8 min. The response time function of the fire station [9] is estimated as

![](/api/attachments/H2RXZQGQ/fulltext/images/a17efb9f286b8703a942b8851cd0544c55692fb993210418f520b9f3b189bf54.jpg)  
Fig. 5. The macro and micro grids.

$$
T = 1. 0 + K r
$$

where:

T response time of the fire station

r the distance in kilometers

1.0 (min) the operational readiness time (the time taken for the fire engine to leave the fire station upon receiving a call for emergency help) given by the SCDF

K the traffic impedance factor.

Using the data from the local fire stations and transport authorities, a trial experiment was conducted to estimate the value of K. The estimated response time function of fire stations was determined as:

$$
T = 1. 0 + 1. 3 2 \cdot r
$$

By substituting the desired response time (5 min) for the variable T, we obtain r = 3.03 km from the estimated function. Fig. 6 shows the buffer of 3.03 km from the fire stations, and the uncovered routes are displayed as those lying outside the buffers.

We found through prescreening that approximately 12 more stations are needed to cover all uncovered SCDF routes. However, only six ones are allowed to be built according to the SCDF plan, which indicates that not all uncovered SCDF routes can be covered in the final solution.

## 5.4. Computation results and discussion

A computational study between the LFCP-Ant and a GA proposed in [14] (i.e. TC-GA) has been carried out for benchmarking the LFCP-Ant. For solving problems of this kind, TC-GA is the only suitable approach found in the literatures. However, the encoding measure used in TC-GA is inappropriate in this case. Using their method, we would have to use a 15,388 bit string to represent one chromosome (solution), which is more than 113 times larger than the one (a 136 bit string) in TC-GA, and such encoding would then possibly cause the computer to run out of memory. Therefore, a more efficient encoding method has been devised. An integer array with the length as the number of the fire stations to be built is adopted to store the index (sequence number) of locations where the fire stations are to be set up. This way, an array with six integers can satisfy the requirements in our case. A typical encoding in our method versus its counterpart in TC-GA is shown in Fig. 7.

Except for the different encoding methods, the same TC-GA operators are adopted from TC-GA. Both TC-GA and LFCP-Ant were coded by C++ on a PC with Intel PIII processor (733 MHz) and 512MB of RAM running on a Windows XP system. The parameters of two algorithms are set as follows. The population number of TC-GA is 100. The global and local enhancement levels of Ant are set as 6.0 and 1.0, respectively. The NRS is limited in 100 iterations and the search radius is 3 km. The scope of the AMNS is within 0.5 km from the original ant location. The evaporation ratio is 10%.

![](/api/attachments/H2RXZQGQ/fulltext/images/595e3d46b0377bcfb1638e57cd8136823c8daf089b58fe3910da13deee609d56.jpg)  
Fig. 6. Uncovered SCDF routes outside buffers of fire stations.

Table 1  
![](/api/attachments/H2RXZQGQ/fulltext/images/c080fa6df8305c514562fd3098fc41746fc6ee1373f931c4370c0e74f888b6e9.jpg)  
6 integers: encoding method in this research  
Fig. 7. Comparison between two encoding methods.

In eight independent runs of the two algorithms, a random-start two-phase local search procedure that disregards the information contained in the trace matrix and an LFCP-Ant only using the second phase local search (AMNS) were conducted with the same time length (3600 s). The goals of these computations were to test the effect of the trace matrix and the first phase local search (NRS). No diversion mechanisms are included in the computation. Results including the objective k values (recall the MO optimization model in Section 2), the mean of k, and the coefficient of variation of k are listed in Table 1.

From the results it can be found that LFCP-Ant (LS) (or LFCP-Ant) outperforms TC-GA in all the eight independent runs. The best solution found by LFCP-Ant (LS) (0.650) is 20.15% better than the one found by TC-GA (0.541) and the average solution found by

Computational comparison among different algorithms

<table><tr><td>Run</td><td>TC-GA</td><td>RANDOM</td><td>LFCP-Ant (LS2)</td><td>LFCP-Ant (LS)</td></tr><tr><td>1</td><td>0.495</td><td>0.623</td><td>0.59</td><td>0.644</td></tr><tr><td>2</td><td>0.487</td><td>0.578</td><td>0.588</td><td>0.65</td></tr><tr><td>3</td><td>0.541</td><td>0.623</td><td>0.542</td><td>0.636</td></tr><tr><td>4</td><td>0.487</td><td>0.634</td><td>0.564</td><td>0.644</td></tr><tr><td>5</td><td>0.493</td><td>0.631</td><td>0.555</td><td>0.638</td></tr><tr><td>6</td><td>0.524</td><td>0.599</td><td>0.564</td><td>0.615</td></tr><tr><td>7</td><td>0.512</td><td>0.611</td><td>0.591</td><td>0.623</td></tr><tr><td>8</td><td>0.502</td><td>0.623</td><td>0.566</td><td>0.614</td></tr><tr><td>AVE(λ)</td><td>0.505</td><td>0.615</td><td>0.570</td><td>0.633</td></tr><tr><td>CoV(λ)</td><td>3.82</td><td>3.04</td><td>3.15</td><td>2.20</td></tr></table>

RANDOM—random-start two-phase local search procedure. LFCP-Ant (LS2)—LFCP-Ant using only the second phase local search.  
LFCP-Ant (LS)—the proposed LFCP-Ant.  
AVE(k)—mean value of k.  
Cov(k)—coefficient of variance of k.

LFCP-Ant (LS) (0.633) is 25.35% better than TC-GA (0.505). Moreover, the performance of LFCP-Ant (LS) is much more stable than TC-GA, as the coefficient of variance of the solutions acquired by LFCP-Ant (LS) (2.20%) is much lower than TC-GA (3.82%).

To illustrate the differences in the solution convergence processes of TC-GA and LFCP-Ant, a typical run of each algorithm using the same random number series is selected to plot the convergence curve, as shown in Fig. 8. LFCP-Ant has been found much smarter than TC-GA in finding solutions. One primary reason is that Ant is an adaptive heuristic combined with a built-in local search algorithm facilitating the process of searching for the local optimum; whereas TC-GA relies merely on a population based random search, which is insensitive to identifying good neighborhood solutions.

The results also evince that LFCP-Ant (LS) outperforms RANDOM in the seven independent runs but one, wherein its performance is still quite competitive. This interprets that the information contained in the pheromone matrix as well as its updating rules and the evaporation mechanism do help ants find good locations for siting facilities.

The RANDOM is found to outperform the TC-GA, which indicates that the local search measure proposed in this research does offer an effective solution. This can be attributed to the fact that the proposed local search measure is an intense spatial search procedure utilizing the information on the locations collected by artificial ants. This is not so blindfold as the reproduction and mutation operators in TC-GA, since these TC-GA operators just conduct pure mathematical operations without considering any available spatial information that should be useful. This may also explain why the LFCP-Ant (LS) heuristics using local search principles [10] is more efficient than the one using population search principles, i.e. GA, in solving this problem.

![](/api/attachments/H2RXZQGQ/fulltext/images/90d3ac8d366a515607636aa685318a0073eff2820171b583f740aec24ee8abc0.jpg)  
Fig. 8. Convergence in a typical run: TC-GA vs. LFCP-Ant.

The LFCP-Ant (LS2) using only the second phase local search was executed to verify any special effects due to the first phase local search. This first phase involves randomness and is typically handled by the Ant part. The results show that LFCP-Ant (LS2) performs rather badly than LFCP-Ant (LS) which employs the two-phase local search in terms of all the criteria used herein. Thus, the effectiveness of the first phase local search in improving the efficiency of the algorithm is validated.

Diversion mechanism is an optional component of LFCP-Ant, which could re-initialize the pheromone matrix when conditions are met, thereby preventing the algorithm from falling into local optimum. Three diversion steps (short, long and medium), which are set based on the maximal iteration number of LFCP-Ant (LS) in stagnancy, were used to test the efficacy of the diversion mechanism. The maximal iteration number in stagnancy is defined as the maximal iteration number in which the algorithm cannot make an improvement on the solutions it finds. As done before, eight independent runs of the LFCP-Ant with different diversion steps were administered within the same time length (3600 s) on a same computer. The computation results, as well as the maximal iteration number of LFCP-Ant (LS) in stagnancy (symbolized as I<sup>\`</sup>) in each runs, are shown in Table 2.

It is found from Table 2 that the maximal M is 100. This result indicates that if the diversion step is greater than this number, the diversion mechanism will be of no use until the algorithm finds a solution equally good as that found by the LFCP-Ant (LS). This is so since before that the pheromone matrix can never be re-initialized.

The LFCP-Ant (LS, D3) with the diversion step as 120 (long) produces the same results as LFCP-Ant (LS) without a diversion mechanism. The average solution (0.621) found by LFCP-Ant (LS, D1) with a short diversion step of 50 is rather worse than the one (0.633) found by LFCP-Ant (LS). These results reveal that: (i) if the diversion step is too large, then it might be of no use; (ii) if the diversion step is too small, then it tends to destroy the pheromone information before the information can be fully exploited.

A medium diversion step was calibrated to be around the mean (66) of M, and so the pheromone information is fully exploited before the pheromone matrix is re-initialized. LFCP-Ant (LS, D2), which is associated with the medium diversion step (70), performs better than LFCP-Ant (LS, D1) but a little worse when compared with LFCP-Ant (LS) devoid of the diversion mechanism. This reveals that the diversion mechanism may not help the proposed LFCP-Ant improve its efficiency in solving this kind of large scale location problems. This is so since the proposed LFCP-Ant may not be able to converge very quickly and it needs to take quite some time to accumulate the pheromone information before this information can possibly direct ants to arrive at an optimal (sub-optimal) solution.

Table 2  
Computational results of LFCP-Ant with different diversion steps

<table><tr><td>Run</td><td>LFCP-Ant (LS, D1)</td><td>LFCP-Ant (LS, D2)</td><td>LFCP-Ant (LS, D3)</td><td>M</td></tr><tr><td>1</td><td>0.623</td><td>0.623</td><td>0.644</td><td>78</td></tr><tr><td>2</td><td>0.613</td><td>0.637</td><td>0.650</td><td>89</td></tr><tr><td>3</td><td>0.625</td><td>0.636</td><td>0.636</td><td>58</td></tr><tr><td>4</td><td>0.636</td><td>0.641</td><td>0.644</td><td>79</td></tr><tr><td>5</td><td>0.623</td><td>0.639</td><td>0.638</td><td>75</td></tr><tr><td>6</td><td>0.606</td><td>0.601</td><td>0.615</td><td>100</td></tr><tr><td>7</td><td>0.623</td><td>0.649</td><td>0.623</td><td>15</td></tr><tr><td>8</td><td>0.620</td><td>0.614</td><td>0.614</td><td>36</td></tr><tr><td>AVE(λ)</td><td>0.621</td><td>0.630</td><td>0.633</td><td>66</td></tr><tr><td>CoV(λ)</td><td>1.43</td><td>2.52</td><td>2.20</td><td>N/A</td></tr></table>

LFCP-Ant (LS, D1)—the proposed LFCP-Ant with diversion step as 50 (short).  
LFCP-Ant (LS, D2)—the proposed LFCP-Ant with diversion step as 70 (medium).  
LFCP-Ant (LS, D3)—the proposed LFCP-Ant with diversion step as 120 (long).  
M—the maximal iteration number of LFCP-Ant (LS) in stagnancy. AVE(k)—mean value of k.  
Cov(k)—coefficient of variance of k.

Table 3  
The best objective achievement levels

<table><tr><td>Objective (i)</td><td>Achievement level ( $\mu_i$ )</td></tr><tr><td>A</td><td>0.654</td></tr><tr><td>B</td><td>0.650</td></tr></table>

Finally, the best solution obtained by LFCP-Ant (LS) in eight runs, which is also the best one found by all the algorithms used here, is shown in Table 3 and the corresponding locations of six new proposed fire stations are mapped in Fig. 9. The figure with a bold face in Table 3 is the critical objective which has the smaller achievement level of both.

Fig. 9 illustrates the optimal solution, where the squares represent the existing fire stations and the triangles the locations of the proposed fire stations.

## 6. Conclusion

This paper has presented a general fuzzy MO optimization model to describe the linear feature covering problem with distance constraints, and the solution through the use of a GIS-supported Ant algorithm. The Ant algorithm, i.e. LFCP-Ant, consists of a twophase local search mechanism, which makes it a universal meta-heuristic suitable for solving large-scale location problems upon a grid system. Computational comparison in the case study shows that LFCP-Ant is much more efficient and robust than the GA, TC-GA.

In this paper, the distance is measured in the Euclidean form. In order to achieve more accurate results, the network distance could be employed within the transportation network. However, using network distance will increase the complexity of the problem. When evaluating objectives, one needs to calculate the network distance through the original vector map. To calculate the network distance in terms of travelling time is a non-trivial task since it involves randomness, i.e. the traffic condition on the road changes anytime. Nevertheless, this idea could lead to a challenging, yet interesting research topic.

The two objectives considered are equally weighted. In the event of the local authorities changing their views and deciding to place different emphasis on any of these two objectives, the fuzzy MO model can easily be modified by assigning appropriate weights to the objectives. Furthermore, if other objectives need to be considered, the fuzzy MO modelling approach can incorporate them in an efficient and trouble-free way without destroying the original model structure. Even though this study uses only the basic functions of GIS, it has been demonstrated that integrating GIS and heuristics in location is indeed an efficient technique. The data attained from the GIS environment are fed into the heuristic algorithm, and the heuristics provides the optimal solution, which can be evaluated on a GIS platform. This continuous process serves as a prototype for the development of a decision support system incorporating both GIS and heuristic algorithms, which helps in decision making for emergency facility locations and other real-life spatial location problems.

![](/api/attachments/H2RXZQGQ/fulltext/images/6795c7c9cc9727b08ece48dbed1facfa07b42f14817ad4dae31d7929411a84b9.jpg)  
Fig. 9. Locations of the six new proposed fire stations.

## References

[1] M.A. Badri, A.K. Mortagy, A.A. Colonel, A multi-objective model for locating fire stations, European Journal of Operational Research 110 (1998).

[2] B. Bullnheimer, R.F. Hartl, C. Strauss, A New Rank Based Version of the Ant System—a Computational Study, Technical report, Institute of Management Science, University of Viena, 1997.

[3] R.L. Church, Geographical Information Systems and Location Science, Computers & Operations Research 29 (6) (2002).

[4] L. Cooper, C.B. Drebes, Formulation and Solution of Some Location-Allocation Problem, Report, vol. AM65-3, Department of Applied Mathematics and Computer Science, Washington University, St. Louis, MS, 1965, p. 63130.

[5] M.S. Daskin, Network and Discrete Location: Models, Algorithms, and Applications, John Wiley, New York, 1995.

[6] M. Dorigo. Optimization, Learning and Natural Algorithms, PhD Thesis, Politecnico di Milano, Italy, 1992.

[7] M. Dorigo, L.M. Gambardella, Ant-Q: a Reinforcement learning approach to the traveling salesman problem, Proc. of ML-95, 12th Int. Conf. on Machine Learning (Morgan Kaufmann), 1995, pp. 252– 260.

[8] M. Dorigo, L.M. Gambardella, Ant colony system: a cooperative learning approach to the traveling salesman problem, IEEE Transactions on Evolutionary Computation 1 (1) (1997).

[9] R.L. Haupt, S.E. Haupt, Practical Genetic Algorithms, John Wiley and Sons, New York, 1997.

[10] A. Hertz, M. Widmer, Guidelines for the use of meta-heuristics in combinatorial optimization, European Journal of Operational Research 151 (2003) 247–252.

[11] V. Maniezzo, Exact and Approximate Nondeterministic Treesearch Procedures for the Quadratic Assignment Problem,

Technical Report CSR, vol. 98-1, Computer Science, Univ. of Bologna, 1998.

[12] M. Sakawa, Fuzzy Sets and Interactive Multiobjective Optimization, Plenum Press, New York, 1993.

[13] T. Stu¨tzle, H. Hoos, The MAX–MIN ant system and local search for the traveling salesman problem, Proc. of ICEC’97—1997 IEEE 4th Int. Conf. on Evolutionary Computation, IEEE Press, US, 1997, pp. 308– 313.

[14] G.H. Tzeng, Y.W. Chen, The optimal location of airport fire stations: a fuzzy multi-objective programming and revised genetic algorithm approach, Transportation Planning and Technology 23 (1999).

[15] C.D. Watson-Gandy, Heuristic procedures for the m-partial cover problem on a plane, European Journal of Operational Research 11 (2) (1982).

Dr. Bo Huang is currently an Associate Professor in the Department of Geomatics Engineering, University of Calgary. Prior to this he was an Assistant Professor in the Department of Civil Engineering, National University of Singapore. He specializes in the design, implementation and application of Geospatial Information Systems (GIS). His research interests are focused on spatial optimization, spatiotemporal database, Web/wireless GIS, and image processing.

Mr. Nan Liu received his Bachelor of Engineering from Tsinghua University, China and Master of Engineering from National University of Singapore in 2004. He is currently pursuing his PhD program in the Department of Statistics and Operations Research, University of North Carolina at Chapel Hill, US.

Mr. Magesh Chandramouli completed his MEng in 2003 from the National University of Singapore and BE from College of Engineering, Anna University, India. He is presently working as a System Engineer in the R&D division of the GIS Research Center, Feng Chia University, Taiwan.
