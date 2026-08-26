---
otero_id: 17407
otero_key: "ANVHQT3M"
title: "Microcomputer-based heuristic approach to vehicle routing for after-sales servicing"
authors: "Mario T. Tabucanon; La-ead Kovavisaruch; Kanchit Malaivongs"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0040-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Microcomputer-based heuristic approach to vehicle routing for after-sales servicing

Mario T. Tabucanon $^{a,*}$ , La-ead Kovavisaruch $^{a}$ , Kanchit Malaivongs $^{b}$

$^{a}$ Division of Industrial Engineering and Management, Asian Institute of Technology, P.O. Box 2754, Bangkok 10501, Thailand $^{b}$ Division of Computer Science, Asian Institute of Technology, P.O. Box 2754, Bangkok 10501, Thailand

## Abstract

A heuristic approach, based on a microcomputer, for solving vehicle routing problem for after-sales service technicians is presented. The “saving algorithm” is modified to incorporate the interactive aspect of the problem. The proposed method is then applied to a real-world problem of fielding technician for after-sales servicing of microcomputers in a big city.

Keywords: Vehicle routing; After-sales servicing

## 1. Introduction

One of the vital strategies in business is to keep customers satisfied by rendering excellent after-sales service for repair and maintenance of machines or equipment. Servicing may be offered in two classes – one for new customers which is customarily free-of-charge extending over a certain period of time, and the other for old customers which is on a fee-charging basis depending on the type of service rendered.

Most customer requests for servicing are made through telephone. The responsible person in the service centre then makes arrangements and schedules visit of a technician. With this simple procedure, indeed, several operational problems can occur. The most obvious circumstance, and usually the most problematic, is the unavailability of a technician, thereby causing service delays. Another problem could be that when few customers call for service, inefficient routing of service technicians may unnecessarily increase travel time. There is, therefore, a need to develop a more effective method for solving this type of problems through the use of a microcomputer.

The paper presents a solution method which tries to determine the fastest path and best sequence for technicians to visit customers. A heuristic procedure is used based on a microcomputer. The method is then applied to a case of a computer servicing firm.

The problem under consideration is similar to a travelling salesman problem, which is a classical vehicle routing problem, in that it requires determination of a minimal cost (time or distance) cycle that passes exactly once through each “node” in the “graph”. Works of Roberts and Flores (1966), Tillman and Hering (1971), and Lin and Kernighan (1973) are some of the related developments in this area.

Clarke and Wright (1964) introduced a heuristic approach called the “saving algorithm”, which is basically an “exchange” procedure in the sense that in each step, one set of tour is exchanged for a better set. Holmes and Parker (1976) extended the work of Clarke and Wright. They introduced a method which can be called “reconsidering” method. After a link (distance, time or cost) is considered to join in a tour, it can be deleted (or prohibited) later if another link provides a better tour.

New approaches to solve combinatorially complex problems utilize artificial intelligence requiring heuristic search intrinsically in knowledge-base operations, especially for logical and analogical reasoning mechanisms as reported by Glover and Greenbery (1989). Some of these emerging approaches are Genetic algorithms [see for example Oliver, Smith and Holland (1987)], Neural networks [see for example Hopfield and Tank (1985) and Greenbery (1988)], Simulated annealing [see for example Cerny (1985) and Kirkpatrick, Gelatt and Vecchi (1983)], Tabu search [see for example Glover (1977, 1986), Hansen (1986), Hansen and Jaumard (1987), Hertz and de Werra (1987) and Hertz, de Werra and Widmer (1988)], and Target analysis [see for example Glover (1986) and Glover, Klingman and Philips (1988)].

## 2. Methodology

An important consideration in routing problems is the computational burden associated with the various solution techniques. Computational burden increases with the problem size. A measure of problem size is the number of nodes. Routing (and scheduling) problems can be categorized into two: (1) those that can use polynomially-bounded algorithm, a procedure whose computational burden increases only polynomially with problem size; and (2) those for which no polynomially-bounded algorithms have yet been found. The latter category of problems are called "NP-hard" whose computational burden increases exponentially with problem size in the worst case.

As a travelling salesman problem, the after-sales servicing problem is “NP-hard” and thus a heuristic approach is appropriate [see for example Papadimitriou and Steiglitz (1982)]. The appropriateness of a heuristic procedure is further justified by some typical characteristics of servicing problems including the following:

(i) Geographical position of customers to be visited by a technician during the day are mostly unknown beforehand. Only a few of them are precisely known at the beginning of the working day; others are assigned interactively as events transpire.

(ii) There are specific requirements to be considered including acknowledgement of customer request with promise of servicing within a specified period of time.

(iii) Since the system is characteristically interactive, the computer program running time is very important. Using an exact algorithm is time-consuming, especially with a microcomputer, and subsequently leads to longer (worse) response time to service customers.

The method presented in this paper is an extension of the saving method of Clarke and Wright and as later modified by Holmes and Parker. The reasons for using this algorithm are explained as follows: The main concept is to improve the solution by inserting nodes. This special feature precisely fits the real-life problem under consideration as customers to be serviced are continually added as event transpire. With a maximum delay time limitation inherent in the problem, the algorithm allows generation of more than one route in the same geographical area. This is particularly suitable when the additional nodes (or customers) are scattered all over a big city. The saving approach is modified to incorporate the interactive nature of the problem.

## 2.1. The saving approach

Clarke and Wright's saving approach can be briefly described as follows: Consider a simple (trivial) problem involving one terminal and two demand points. Let the terminal node be labelled (1) and the demand points by nodes labelled (2) and (3). Further, assume that the parameters of the system are known such that demands, interpoint travel costs and vehicle capacities are given. Let a feasible solution to assign demand point (2) to one vehicle and demand point (3) to another vehicle. Depicted graphically in Fig. 1a, the two routes are $1 \to 2 \to 1$ and $1 \to 3 \to 1$ with total inter-point travel cost $C_1 = c_{12} + c_{21} + c_{13} + c_{31}$ . Fig. 1b shows that a single route exists with two former routes combined. The cost of the new route, $C_2$ , can be given as $c_{12} + c_{23} + c_{31}$ . In the routes of both figures, directionality is maintained which is important for nonsymmetric problems. The two solutions depicted in Fig. 1 differ in cost by an amount $C = C_1 - C_2 = c_{21} + c_{13} - c_{23}$ . If $C > 0$ then saving in cost can be found by combining the two demand points assuming that the single vehicle is of sufficient capacity. Hence, if there exists some (i,j) not on a current route such that $c_{ij} < (c_{ix} + c_{xj})$ where (i,x) and (x,j) are on current routes, the total cost of a current solution can be reduced by exchanging (i,j) for (i,x) and (x,j).

Unfortunately, the iterative process of Clarke and Wright can lead to major sub-optimization. For example, in Fig. 2a, the nodes are labelled such that (1) is the terminal, and (2) to (6) are the demand points. The values in brackets represent requirements at each of the five demand points and the labels on all edges represent the cost of travel between points (i) and (j). The solid edges represent a solution with three routes. If all costs are symmetric and all vehicles have a capacity of ten, then the graph shows that the joining of (3)

(a)  
(b)  
![](/api/attachments/ANVHQT3M/fulltext/images/e2074a11a39f7486bfd2618e53d58e73132aa9e79cdf86b6e69ca766e0443654.jpg)

![](/api/attachments/ANVHQT3M/fulltext/images/c569f9d8b105292603a863bef1e4b8a80f52c79eba5bba90e376fb2aca6cde70.jpg)  
Fig. 1. Illustration of arc replacement scheme leading to potential saving in route structure.

![](/api/attachments/ANVHQT3M/fulltext/images/aa610327f3a1680b9d70a6029935cf2fb2fd72448d5e2cd02ec99d31e881f5fb.jpg)  
Fig. 2. Illustration of sub-optimal solution and revised optimal solution.

and (4) yields the maximum saving over all pairs. In this case at least two vehicles are necessary to service the remaining points with a total of 87. However, if edge (3,4) is prohibited from any solution, edge (2,3) and (4,5) will replace (3,4), (2,1) and (5,1). Two routes result which are feasible yield a total cost of 76 (Fig. 2b). The condition giving rise to such an illustration obviously do not require unreasonable problem parameters and so a relatively obvious extension made by Holmes and Parker is given to the basic approach.

The selection of a particular joint may cause demand points to be “locked” into a particular route which results in an under-utilized vehicle without enough excess capacity to service additional demand points which, in turn, tends to force the other points to be serviced by new vehicles hence, creating additional routes of low utilization. Holmes and Parker adapted the basic approach in order to compensate the bottleneck. Their algorithm can be described by the following steps:

Step 1: Initialization

1.1 Construct an initial cost matrix, C, such that $C = [c_{ij}]$ , $i,j = 1,2\ldots,n$ where n is the number of demand points plus the terminal when i = j, let $c_{ij} = 0$ .

1.2 Determine the demand of each point $q_{i}$ , the number of vehicles available of type k, $T_{k}$ and the capacity of each $C_{k}$ .

1.3 Initialize the suppression counter L at 1 and the maximum suppression number, L'.

Step 2: Construct the saving matrix and the initial solution

2.1 Compute $s_{i,j}$ such that $s_{i,j} = c_{i,1} + c_{1,j} - c_{i,j}$ for all $i,j = 2,3,\ldots,n$ and $i$ not equal to $j$ . If $s_{i,j} < 0$ , set $s_{i,j} = 0$ for all $i = j$ .

2.2 Let $s_{i,1} = s_{1,j} = -1$ , for all $i,j = 2,3,\ldots,n$ . Note throughout that $s_{i,j} = -1$ indicate the presence of $(i,j)$ in a current solution.

2.3 Compute the cost K of the initial solution, such that

$$
\mathrm{K} = \sum \mathrm{c} _ {\mathrm{i}, 1} + \sum \mathrm{c} _ {1, \mathrm{j}}
$$

Step 3: Determine a candidate pair

3.1 Find the ordered pair $i^{*}, j^{*}$ with the greatest feasible saving such that $s_{i,j}^{*} = \max\left[s_{i,j}\right]$ where (i,j) is defined over all ordered pairs such that $s_{i,1}$ and $s_{1,j}$ not equal to 0.

![](/api/attachments/ANVHQT3M/fulltext/images/9a75266bd09506bfad93ac42fc02a623954e2e19b4ac30d8f3f16093b81321c7.jpg)  
Fig. 3. The logical flowchart of Holmes and Parker's "Saving Method".

3.2 If $s_{i,j}^{*} = 0$ , go to step 5.

Step 4: Join the points i\* and j\* on a route

4.1 If neither of the points is on a route, construct a new route $z$ and compute the required demand $Q_{z}$ such that $Q_{z} = q_{i}^{*} + q_{j}^{*}$ go to step 4.4

4.2 If one of the points is currently assigned to a route, say z, attempt to join the unassigned point to z. Compute the total demand $Q_{z}$ such that $Q_{z} = Q_{z} + q_{i}^{*}$ ; go to 4.4.

4.3 If both points are currently assigned to routes, say u and v, attempt to join routes into one route, z. Compute the total demand $Q_{z}$ where $Q_{z} = Q_{u} + Q_{v}$ ; go to step 4.4.

4.4 Check the capacity restrictions. Select the smallest $C_{k}$ such that $C \geq Q_{z}$ and proceed to

4.5. If no such $\mathbf{C}_{\mathbf{k}}$ exists, set $s_{i,j} = 0$ and return to step 3.

4.5 Update the number of vehicles available, $T_{k}$ , such that $T_{k} < -T_{k} - 1$ . If routes are joined, increment the appropriate number of vehicles available for the previous size used on this route.

4.6 Compute the new solution cost such that $\mathbf{K} < -\mathbf{K} - s_{i,j}^{*}$ and return to step 3. Update the saving matrix such that $s_{i,j} = -1$ and $s_{j,1} = s_{i,1}^{*} = s_{1,j}^{*} = 0$ .

Step 5: Save the best solution

5.1 If this is the first solution, save the cost $K'$ , such that $K' = K$ . Maintain all routes and the order in which points were joined; go to step 6.

5.2 If this is not the first solution and $\mathbf{K} \leqslant \mathbf{K}'$ , set $\mathbf{K}' = \mathbf{K}, \mathbf{L} = 1$ and $s_{i,j} = 0$ in the matrix of step

![](/api/attachments/ANVHQT3M/fulltext/images/f490555ad1a7cbc8a1a4b0beb4b6afca203328db3a69bf607c8847c208d3fcda.jpg)  
Fig. 3 (continued)

![](/api/attachments/ANVHQT3M/fulltext/images/c8499c0eb878dbcbbad1595523e55c9ace93029b4dea4b5d7457959122f0a1ae.jpg)

2.1. Note that $(i',j')$ is the pair just suppressed and, further, that $(i',j')$ remains suppressed in all subsequent solutions; go to step 5.4.

5.3 If $\mathbf{K} > \mathbf{K}'$ , let $\mathbf{L} < -\mathbf{L} + 1$ .

5.4 Maintain the routes formed and the order in which points were joined.

Step 6: Suppress specified pairs

6.1 If $L < L'$ , suppress the pair of points joined next in the current best solution, say $(i^{-}, j^{-})$ such that $s_{ij^{-}} = 0$ in the matrix of step 2.3 and return to step 3.

6.2 If $\mathbf{L} = \mathbf{L}'$ or if all joined pairs in the current solution have been suppressed, terminate the procedure.

Fig. 3 shows the flow chart of this adapted algorithm.

## 2.2. Proposed procedure

The system is designed as a microcomputer-based interactive system for the assignment and routing of maintenance technicians. The backbone of the system is a heuristic model, the Clarke and Wright as extended by Holmes and Parker's "saving approach". Some modifications are made at the beginning and the end of this "saving approach" in order to fit the interactive aspect of the problem. The proposed system is divided into two phases, as follows (also see Fig. 4):

Phase I: Initialization

Step 1: The first step involves preparing and verifying the data for the street network which turns out to be the most time-consuming step. Without an accurate representation of the street network and a correct enumeration of the distance measurement, time-conversion and other characteristics, the remainder of the procedure may give inaccurate and meaningless results.

![](/api/attachments/ANVHQT3M/fulltext/images/60169f6ec75ebff77569fd8d93356d24fb8938d82d36f08e28146f35609e3217.jpg)  
Fig. 4. The logical flowchart of proposed procedure.

Step 2: Knowing the street network and customers' location, the relationship of these nodes are constructed and kept in the data files. For the flexibility of the system, the nodes and their interrelationships can be modified (through the screen) whenever there are changes.

Step 3: A shortest-path model is used in this step to find out the shortest distance along the street from one customer (or node) to the other. The result from this model which is in matrix form will be kept for use in the next phase.

Phase I is used for the system setup in the beginning only. Once the necessary information is recorded in the files, this phase is skipped in daily-runs except when there are changes in the network, such as when: (a) the traffic system is changed from one-way to two-way or vice versa, (b) a customer moves to another location, and (c) new customers come into the system. Whenever there is a change in the network, the shortest-path model has to be recomputed.

## Phase II: Daily-Run Routine

Step 1: Check the status of the system whether it is the first run of the day. If it is, customers who made requests are inputed to the system. Otherwise, old information which is kept in the log file from previous run plus new information on additional requests are loaded.

Step 2: From these input data, a submatrix is extracted from the big matrix obtained in step 3 of phase I. This submatrix contains the shortest distance from one node to the others.

Step 3: The saving algorithm is performed using the matrix obtained from step 2. This step is repeated until it violates the constraints, i.e., the maximum specified response time. The sequences for visited customers and the routing are created in this step.

Step 4: The output of the solution consists of:
- The number of technicians needed which implicitly gives the number of routes.

\- The sequence of customers to be served in each route, the name of the street along the route, and the estimated time used in each route.

\- The total travel time of the routes.

Step 5: All information obtained in the current run are kept in the log file for use in the next runs. These include date, time, customer code, junction nodes, possible delay time for this customer, failure type and estimated repair time for this failure. This is very important for the overall procedure. If the previous status is not kept, the iterative and interactive aspect of the system can not be fulfilled.

Major modifications are made to the original algorithm in this phase. The adaptations provide the iterative and interactive nature of the model. If there are additional requests from customers during the working day, it allows to run the program any time in order to build a new solution. This phase is run several times a day depending on how often and how many additional requests are called in during the day. It is also limited by the time and number of technicians available. All these conditions can be adjusted by the decision maker at a certain satisfactory level (Fig. 4).

## 2.3. Computer system design

In designing the microcomputer-based system, certain considerations are taken into account for practical implementation, as follows:

1. Simplicity and ease of use: The system will be used several times in a day, therefore, the main concern lies on simplicity and ease of use for the end-users. A menu-driven system is introduced here.

2. Response time: The computer response time in this system is critical. Quicker response time is better from the users' point of view.

3. Improvability: The system is limited to some specifications due to time constraint. There may be a motivation to expand or modify the system in the future. Hence, it is designed such that it is easy to modify without any major rearrangements.

The package is composed of a main program and a set of subprograms or procedures. The functions include data entry, data modification, shortest-path computation, reporting, time-distance conversion, and most importantly, assignment and routing processing.

## 3. Case application

The methodology is applied in a large computer concern in a big city. To protect confidentiality, the name of the company is not mentioned here. The model is used with the following specific conditions: (1) the assignment is done only once in the morning; (2) if the technicians cannot finish the assigned jobs within working hours of the day, postponement to the next working day is allowed; (3) eight working hours is set as the maximum delay response time; and (4) four technicians are available for the field. Table 1 shows a comparison of results between the existing manual and the proposed microcomputer-based systems. Incomplete jobs from the previous day and the customers who call in before 8:30 AM are assigned in the first assignment at 8:30 AM. The next run is operated when there are enough accumulated request calls in the waiting list (three or four customers are assumed here). Normally, there are less calls in the morning and, hence, the time gap between two assignments is made longer in the morning than in the afternoon. The last assignment is not made later than 4:00 PM.

Comparison of complete jobs by manual and developed system

<table><tr><td rowspan="2">Day No.</td><td rowspan="2">Total req. calls</td><td colspan="2">Complete Jobs</td><td rowspan="2">Diff.</td></tr><tr><td>Manual</td><td>Computer</td></tr><tr><td>1</td><td>16</td><td>11</td><td>16</td><td>5</td></tr><tr><td>2</td><td>18</td><td>12</td><td>18</td><td>6</td></tr><tr><td>3</td><td>21</td><td>16</td><td>20</td><td>4</td></tr><tr><td>4</td><td>27</td><td>17</td><td>20</td><td>3</td></tr><tr><td>5</td><td>8</td><td>8</td><td>8</td><td>0</td></tr><tr><td>6</td><td>15</td><td>14</td><td>15</td><td>1</td></tr><tr><td>7</td><td>17</td><td>17</td><td>17</td><td>0</td></tr><tr><td>8</td><td>20</td><td>15</td><td>18</td><td>3</td></tr><tr><td>9</td><td>19</td><td>12</td><td>19</td><td>7</td></tr><tr><td>10</td><td>23</td><td>18</td><td>18</td><td>0</td></tr><tr><td>11</td><td>10</td><td>10</td><td>10</td><td>0</td></tr><tr><td>12</td><td>21</td><td>17</td><td>18</td><td>1</td></tr><tr><td>13</td><td>7</td><td>7</td><td>7</td><td>0</td></tr><tr><td>14</td><td>14</td><td>14</td><td>14</td><td>0</td></tr><tr><td>15</td><td>14</td><td>10</td><td>14</td><td>4</td></tr><tr><td>16</td><td>21</td><td>17</td><td>20</td><td>3</td></tr><tr><td>17</td><td>5</td><td>5</td><td>5</td><td>0</td></tr><tr><td>18</td><td>24</td><td>15</td><td>19</td><td>4</td></tr><tr><td>19</td><td>29</td><td>17</td><td>16</td><td>-1</td></tr><tr><td>20</td><td>16</td><td>16</td><td>15</td><td>-1</td></tr><tr><td>21</td><td>23</td><td>12</td><td>20</td><td>8</td></tr><tr><td>22</td><td>21</td><td>14</td><td>21</td><td>7</td></tr><tr><td>23</td><td>10</td><td>8</td><td>10</td><td>2</td></tr><tr><td>24</td><td>24</td><td>20</td><td>18</td><td>-2</td></tr><tr><td>25</td><td>5</td><td>5</td><td>5</td><td>0</td></tr><tr><td>26</td><td>17</td><td>12</td><td>17</td><td>5</td></tr><tr><td>27</td><td>19</td><td>16</td><td>19</td><td>3</td></tr><tr><td>28</td><td>23</td><td>15</td><td>18</td><td>3</td></tr><tr><td>29</td><td>16</td><td>11</td><td>16</td><td>5</td></tr><tr><td>30</td><td>16</td><td>12</td><td>16</td><td>4</td></tr><tr><td>31</td><td>19</td><td>15</td><td>19</td><td>4</td></tr><tr><td>32</td><td>26</td><td>12</td><td>17</td><td>5</td></tr><tr><td>33</td><td>24</td><td>18</td><td>18</td><td>0</td></tr><tr><td>34</td><td>12</td><td>7</td><td>12</td><td>5</td></tr><tr><td>35</td><td>20</td><td>6</td><td>17</td><td>11</td></tr><tr><td>36</td><td>30</td><td>23</td><td>20</td><td>-3</td></tr><tr><td>37</td><td>21</td><td>15</td><td>18</td><td>3</td></tr><tr><td>38</td><td>17</td><td>16</td><td>17</td><td>1</td></tr><tr><td>39</td><td>11</td><td>10</td><td>11</td><td>1</td></tr><tr><td>40</td><td>5</td><td>5</td><td>5</td><td>0</td></tr><tr><td>41</td><td>16</td><td>16</td><td>16</td><td>0</td></tr><tr><td>42</td><td>18</td><td>14</td><td>18</td><td>4</td></tr><tr><td>43</td><td>11</td><td>10</td><td>11</td><td>1</td></tr><tr><td>44</td><td>14</td><td>12</td><td>14</td><td>2</td></tr><tr><td>45</td><td>20</td><td>17</td><td>18</td><td>1</td></tr><tr><td>Total</td><td>783.00</td><td>589.00</td><td>698.00</td><td>109.00</td></tr><tr><td>Average</td><td>17.40</td><td>13.09</td><td>15.51</td><td>2.42</td></tr><tr><td>Std.dev.</td><td>6.16</td><td>4.16</td><td>4.31</td><td>2.82</td></tr><tr><td colspan="2">% Complete jobs</td><td>75.2%</td><td>89.1%</td><td></td></tr></table>

The number of technicians needed is affected by two parameters: frequency of program runs and maximum delay response time. The number of technicians needed increase with the number of assignments because when a particular technician in the field cannot finish the jobs in time, additional customers must be assigned to another technician. This is also affected by the maximum delay time parameter. Fig. 5 shows the relationship between the number of technicians and the maximum delay time with different number of customers. It can be observed that when the delay time is shortened, more technicians are needed to supply faster service. Conversely, the number of technicians needed decreases when the delay time is longer. Moreover, more technicians are needed to service customers calling from different places than when the customers are from the same area.

![](/api/attachments/ANVHQT3M/fulltext/images/e267a6d81a84ef89bbf38602506c9d2b56306a774a9383d979c0807d7f1eaf18.jpg)  
Fig. 5. Number of technicians needed with different maximum delay time.

It is also found that the sequencing of customers may be changed from the previous assignment when there are additional customers assigned to the same technician, or the customer who is served by the first technician at first time is changed to a second route at second run. In effect, reassignment of technicians is admissible. The reason is that the system tries to find out the best solution with the shortest travel time at each run in the procedure. When there are additional nodes, the previous routes may be destroyed and the new sequences which are better off are built. This procedure ensures that service levels increase with the dynamic nature of the assignment. Most customers can be served in the same day of their request. In the empirical results, four hours for maximum delay time is suggested so that it does not exceed five technicians with current request rates in a day. However, management may change these policy parameters from time to time under different environments. The number of technicians made available and the speeds with which the customer should be acknowledged depends on their satisfaction.

Another parameter of the model, maximum suppression level, is also tested. This parameter is set for the termination of the heuristic model when a certain level of satisfaction is obtained. Three different levels, (4, 6 and 8) are set for testing. The results reveal that the route sequences are changed by different levels of suppression and that it is better off (meaning shorter travel time) when higher levels are used (8 instead of 4). However, the difference is not large.

In the Holmes and Parker algorithm, two criteria are used for program termination: (1) when all node pairs have been exhausted from suppression, the procedure is terminated, and (2) if there are still some node pairs that can be suppressed by further iterations, the program will be terminated by the maximum level of suppression. Fig. 6 shows the result of computer time used by different number of nodes. This is also compared with different suppression level set at the initial step. From the graph, it is obvious that the computer time increases as the size of problem (or nodes) increases. It also shows that when suppression level increases, it affects the computer time in the same direction.

![](/api/attachments/ANVHQT3M/fulltext/images/0a75c42cb5ff60e253aa1d657a035e414221dcad2f05190761f113b058583da1.jpg)  
Fig. 6. Computer time used by different number of nodes with different maximum suppression level. (Based on NEC IV microcomputer, an IBM-PC compatible whose total compilation time for the program is 1 min. and 10.47 sec.)

## 4. Concluding remarks

The proposed microcomputer-based system offers certain advantages. It can be operated as many times as the user wishes with only few seconds of response time. The maximum service time delay can be changed accordingly with much ease. The system also provides information on sequence of customers to be visited, the route, total route time and the number of technicians.

In this paper, no specific comparison is made between the heuristic and an exact algorithm in the case study for two reasons. Firstly, it was not practically possible to derive an exact solution within a reasonable time duration, and secondly, it would seem suffice to refer the reader to the work of Holmes and Parker (ref.13) as far as the efficiency and accuracy of the algorithm is concerned.

To be implementable, the computation time acceptable to the user must necessarily be one which is comfortably lower than the mean intercall time between customers. The present situation of the system underconsideration is quite the case.

## References

[1] Cerny, V., Thermodynamical Approach to the Travelling Salesman Problem: An Efficient Simulation Algorithm, Journal of Optimization Theory and Applications, Vol. 45, 1985, p. 41–52.

[2] Clarke, G. and J.W. Wright, Scheduling of Vehicles from a Central Depot to a Number of Delivery Points, Operations Research, Vol. 12, 1964, p. 568–581.

[3] Glover, F., Heuristics for Integer Programming Using Surrogate Constraints, Decision Sciences, Vol. 8, 1977, p. 156–166.

[4] Glover, F., Future Paths for Integer Programming and Links to Artificial Intelligence, Computers and Operations Research, Vol. 13, 1986, p. 533–549.

[5] Glover, F., Tabu Search, Technical Report, Centre for Applied Artificial Intelligence, University of Colorado, Boulder, CO, U.S.A., 1987.

[6] Glover, F., D. Klingman and N.V. Phillips, A Network-related Nuclear Power Plant Model with an Intelligent Branch-and-bound Solution Approach, Technical Report, CBDA 139, University of Texas, Austin, TX, U.S.A., 1988.

[7] Glover, F. and H.J. Greenberg, New Approaches for Heuristic Search: A Bilateral Linkage with Artificial Intelligence, European Journal of Operational Research, Vol. 39, 1989, p. 119–130.

[8] Greenberg, H.J., Learning Networks, Final Report, Mathematics Clinic, University of Colorado, Denver, CO, U.S.A., 1988.

[9] Hansen, P., The Steepest Ascent Mildest Heuristic for Combinatorial Programming, Proceedings of the Congress on Numerical Methods in Combinatorial Optimization, Capri, Italy, 1986.

[10] Hansen, P. and B. Jaumard, Algorithms for the Maximum Satisfiability Problem, RUTCOR Research Report, Rutgers, New Brunswick, NJ, U.S.A., 1987.

[11] Hertz, A. and D. de Werra, Using Tabu Search Techniques for Graph Colouring, Computing, Vol. 39, 1987, p. 345–351.

[12] Hertz A., D. de Werra and M. Widmer, Some New Applications of Tabu Search, Proceedings of the 13th International Symposium on Mathematical Programming, Tokyo, 1988.

[13] Holmes, R.a. and R.G. Parker, A Vehicle Scheduling Procedure Based Upon Saving and a Solution Perturbation Scheme, Operational Research Quarterly, Vol. 27, No. 1, 1976, p. 83–92.

[14] Hopfield, J.J. and D.W. Tank, Neural Computation of Decisions in Optimization Problems, Biological Cybernetics, Vol. 52, 1985, p. 141–152.

[15] Kirkpatrick, S., C.D. Gelatt, Jr. and M.P. Vecchi, Opti-

mization by Simulated Annealing, Science 220, 1983, p.671–680.

[16] Lin, S. and B.W. Kernighan, An Effective Heuristic Algorithm for the Travelling Salesman Problem, Operations Research, Vol. 20, 1973, p. 498–516.

[17] Oliver, I.M., D.J. Smith and J.R.C. Holland, A Study of Permutation Crossover Operators on the Travelling Salesman Problem, Technical Report, Texas Instruments Ltd., Dallas, TX, U.S.A., 1987.

[18] Papadimitriou, C.H. and K. Steiglitz, Combinatorial Optimization, Prentice-Hall, 1982, p. 371.

[19] Robert, S.M. and B. Flores, An Engineering Approach to the Travelling Salesmen Problem, Management Science, Vol. 13, No. 3, 1966.

[20] Tillman, F.A. and R.W. Hering, A Study of a Look Ahead Procedure for Solving the Multiterminal Delivery Problem, Transportation Research, Vol. 5, 1971, p. 225–229.
