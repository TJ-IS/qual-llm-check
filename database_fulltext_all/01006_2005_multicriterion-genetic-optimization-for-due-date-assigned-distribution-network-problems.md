---
otero_id: 1006
otero_key: "D9XE29VA"
title: "Multicriterion genetic optimization for due date assigned distribution network problems"
authors: "Felix T.S. Chan; S.H. Chung"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Multicriterion genetic optimization for due date assigned distribution network problems

Felix T.S. Chan\*, S.H. Chung

Department of Industrial and Manufacturing Systems Engineering, The University of Hong Kong, Pokfulam Road, Hong Kong, China

Available online 10 May 2004

## Abstract

This paper focuses on the demand due date factor in multiechelon distribution network problems and its impact on the production scheduling in manufacturing plants. A reliable demand due date is critical in winning of customer orders. However, this may usually require high collaboration among entities in the network. Mismatching of one single schedule may seriously influence the reliability. In this connection, holistically optimizing the schedule of each entity among the network is essential. In addition, on time delivery may induce high operating cost. A trade-off between earliness, on time, and tardiness should also be considered. Hence, a multicriterion genetic optimization methodology is developed to holistically optimize them. It determines the optimized schedule to collaborate each entity to fulfill the demands. For enabling multicriterion decision-making, the proposed algorithm combines analytic hierarchy process with genetic algorithms (GAs). The problem is divided into two parts— (i) demand allocation and transportation problem, and (ii) production scheduling problem. The optimization approach is applied to iteratively optimize part (i), and then part (ii). Three experiments have been carried out, and the computation results show that the effect of due date is critical, and the ability of the proposed algorithms in taking trade-off between earliness and tardiness. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Due date; Genetic algorithms; Analytic hierarchy process; Distribution network; Production scheduling

## 1. Introduction

In this paper, the main focus is on the demand due date factor for multiechelon distribution network problems and its impact on the production scheduling in manufacturing plants. Distribution problems deal with distribution from a number of sources to a number of destinations. With globalization getting prevalent in recent years, distribution networks for the flow of products between suppliers and end customers are becoming more complex than as they existed decades ago. Efficient integration of these facilities has been recognized to be an important strategic weapon to increase and maintain competitive strength, especially for the companies that have adopted JIT production approach [3,19,33].

Ideally, a good distribution network design can help companies to have better value-addition, reduce costs, and increase customer service level by determining optimal links between each node and the traffic flow routine [18,21,27]. Adequate simplification and construction of links can reduce the total traveling distance of the network. In addition, it enhances the scheduling of the carrier loading/unloading points and the routines. Management of procurement, production, and distribution activities as a whole among the network has been recognized as an important issue [28]. Integration of these activities includes the area of buyer and vendor, production planning and inventory control, distribution and logistics, production – distribution, and inventory and distribution, etc. [5,11,17]. Concurrently, planning the production capability, production capacity, production costing, rough production scheduling, and demand due date can provide goods and services to the customer at lower cost and higher customer service level [32]. Failure of integration may result in inefficient utilization of resources, overloaded/idle capacity, long production lead time, high in-transit inventory level, larger buffer stock, and unreliable due date assignment and achievement (earliness and tardiness).

For a company to make profit and maintain competitive, minimization of cost expenditures is crucial. For these objectives, customer service level weighs equally important [16]. Customer service level can be measured by customer response time, ability to respond to market changes, consistent order cycle time, accuracy of order fulfillment rate, short delivery time, flexibility in order quantity, flexibility in product specification, accuracy of information system, etc. [4]. Among these, shorter and reliable due dates are critical for winning customer orders [26]. However, short lead time induces higher operating costs. In addition, tardiness may cause penalty cost, and negative impact on the company’s reputation. Indeed, there is a trade-off between the length of lead time quoted to the customers and the achieved reliability [29]. Many research works have been published in the area of due date assignment and scheduling, which are summarized by Gordon et al. [15]. These include minimizing the mean absolute deviation (MAD) of completion time about a common completion due date, or mean absolute lateness to minimize the penalty cost in a problem of scheduling a job on a single machine or parallel machines. However, most of these research works are only studied at the level of job–shop scheduling. There is lack of research work focusing on demand due date factor at the higher decision level of the distribution network.

Improvement of a particular factor may be based on the sacrifice of the other factors; for instance, cost and customer service are conflicting in nature. These complex relationships increase the difficulty level in design of the distribution network, consequently influencing its performance. Such trade-offs between factors may vary from one network structure to the other. Therefore, addition of weightings into each criterion for the consideration of optimal solutions makes the optimization methodology more realistic and practical.

Many researchers have studied optimization of distribution networks. With a set of demands (known or estimated from historical data), the interrelationship, the demand allocation, inventory management, location of facilities, determination of transportation policy have been studied. Some of them adopted linear programming, mixed integer programming, fractional programming, and multiobjective linear fractional programming [2,7,20,31]. These optimization approaches can generate optimal solutions. However, they are usually time consuming in computation and complicated in model construction [2]. In the nonlinear situation, such as the delivery cost changes along with the delivery quantity/batch size, nonlinear programming is required, which makes the modeling and computation even more complex. Near-optimal solutions determined by heuristic approach (sometime optimal) are more preferable and acceptable because they can be obtained relatively more efficiently; hence, genetic algorithms (GAs) are widely adopted [6].

Abdinnour-Helm [2] testified the reliability and robustness of GA by deploying five different distribution networks with the geographical layouts of Continental USA, Regional USA, Canada, and Western Europe. The optimization results obtained by GAs were compared with the one obtained by mixed integer programming for the objective of minimization of the overall transportation cost. The results proved that the technique of GA is reliable and robust. Vignaux and Michalewica [30] adopted GAs to minimize the cost factor for a linear transportation problem. GAs heuristic is widely preferred because GAs do not restrict on analytical properties of the function to be optimized. In addition, GAs can be combined with other heuristic methods, such as when Abdinnour-Helm [1,2] adopted GA with Tabu search to enhance the optimization results [12,13]. Some researchers combined GAs with fuzzy to overcome uncertainties present in supply chain, such as demand fluctuation [14,22]. GAs can achieve good optimization results even in job – shop scheduling problems [9,10]. Sakawa [25] deployed GAs to maximize the fulfillment reliability of job’s due date in a job – shop scheduling problem, in which the uncertainties of production lead time and the due date are represented by fuzzy sets.

This paper develops an optimization algorithm to solve the problem of demand allocation, transportation, and production-scheduling in a demand-driven multiechelon distribution network, especially with the consideration of demand due date. This proposed optimization algorithm is further developed from the optimization methodology of GA + AHP, which adopts the optimization concept of GAs, and decision-making technique of analytic hierarchy process (AHP) [8]. The proposed algorithm is capable of considering several factors with different weightings in determining an optimal solution. The proposed algorithm divides the problem into two parts. The first part utilizes GA to determine the demand allocation and transportation policy. The second part applies GA to determine the production scheduling of demands in each manufacturing plant.

The remaining part of this paper is organized as follows. Section 2 characterizes the model of a distribution network problem, explains the difficulties, and describes the objective functions. Section 3 presents the proposed optimization methodology, and Section 4 analyzes the computation results. Section 5 will be the conclusions and directions for future research.

## 2. The problem structure

In this section, we discuss an example of a three tiers distribution network model which consists of four manufacturing plants M<sub>i</sub> (i = 1, 2, 3, 4), four warehouses $W _ { j } \ ( j = 1 , 2 , 3 , 4 )$ , and 10 customers, in which each customer will release one order demand with a total of 10 order demands, ${ D _ { k } } \left( { k = 1 , 2 , . . . , 1 0 } \right)$ Two different types of delivery modes (m = 1, 2) are available between each manufacturing plant and each warehouse, and between each warehouse and each customer, as shown in Fig. 1. It is assumed that the delivery lead time in delivery mode 1 are shorter than that in delivery mode 2 for the same delivery arcs, while the delivery cost is higher.

## 2.1. Problem background

Consider a demand-driven distribution network with no storage stock in the system. Demands can only be satisfied from the manufacturing plants, through the warehouses. The production of a demand in manufacturing plants begins to be produced only after the preceding demands have been produced. Once a demand is produced, it may be stored in the manufacturing plant or immediately delivered to warehouses for storage. Similarly, this demand may be immediately delivered to customer. Delivery unit cost ratio is independent of delivery quantity. Each demand has a given due date assigned by the customers, and the product will only be delivered to customer on the due date. Penalty cost will be incurred for tardiness. Each manufacturing plant and warehouse has different operating costs, involves different lead time, and has different capacity constraints.

![](/api/attachments/D9XE29VA/fulltext/images/57c6afc69992fd9ec175ca49378c739f76bb50c1b8a6b7a5373748430dcea8f9.jpg)  
Fig. 1. A sample of distribution network model. M<sub>i</sub>—manufacturing plant i. $W _ { j }$ —warehouse j.

The problem here is to determine which demands should be allocated to which warehouses, and which should be produced in which manufacturing plant. The optimization methodology should also determine the type of transportation to adopt in each delivery, and the production scheduling of demands in the manufacturing plants. These decision variables are indeed closely related because they cumulate up for the total system cost and lead time of demand delivery.

With the demand due date assigned, it is necessary to take a trade-off between earliness and tardiness. If finished products are delivered earlier than the date required, customers may not utilize the products. They may have to have free extra space for storage, or even refuse to receive the early products. For this reason, this paper assumes that the finished products will be stored in suppliers’ warehouses. Similarly, if the finished products are delivered later than the due date required, customers may have shortage of material supply problem. In this connection, early completion may induce storage costs, while tardy completion may induce penalty costs. The optimization methodology should determine to use which manufacturing plant, warehouse, and transportation mode from manufacturing plant to warehouse, and from warehouse to customer, so that, an optimal trade-off between the penalty cost and operating costs can be obtained.

Tardy demand is caused by lead time relatively taken longer than the due date. Intelligent control of the required lead time of demand is crucial, among which, the production scheduling of demands in manufacturing plants influences lead time significantly. Because production capability is limited, a demand can be produced only after the completion of its preceding demands, and this defines the completion time of that demand. In this connection, during the allocation of demand to manufacturing plant, the optimization methodology should also determine the production priority of each demand allocated.

In this paper, one of the objective functions is to minimize the total system cost. Other objective functions are to minimize the total lead time of demands, the total number of tardy demands, total duration of tardiness time, and the mean absolute deviation of tardy demands. Indeed, these objective functions may conflict in nature. Therefore, the optimization methodology should take into account the weighting for each objective function.

The following notation is used in the distribution network model:

## 2.2. Optimization functions

<table><tr><td> $\text{MCA}_i$ </td><td>Maximum production capacity of manufacturing plant  $i$ </td></tr><tr><td> $\text{MLT}_i$ </td><td>Production lead time per unit product of manufacturing plant  $i$ </td></tr><tr><td> $\text{MPC}_i$ </td><td>Production unit cost of manufacturing plant  $i$ </td></tr><tr><td> $\text{MSC}_i$ </td><td>Storage unit cost per unit time of manufacturing plant  $i$ </td></tr><tr><td> $\text{WCA}_j$ </td><td>Maximum inventory storage capacity of warehouse  $j$ </td></tr><tr><td> $\text{WLT}_j$ </td><td>Order-processing lead time per order of warehouse  $j$ </td></tr><tr><td> $\text{WHC}_j$ </td><td>Inventory handling unit cost rate of warehouse  $j$ </td></tr><tr><td> $\text{WSC}_j$ </td><td>Storage unit cost per unit time of warehouse  $j$ </td></tr><tr><td> $\text{DC}_k$ </td><td>Demand quantity from customer  $k$ </td></tr><tr><td> $\text{DW}_j$ </td><td>Demand quantity from warehouse  $j$ </td></tr><tr><td> $\text{DCR}_m$ </td><td>Delivery unit cost rate per unit time for each unit of product transported for delivery mode  $m$ </td></tr><tr><td> $\text{CWD}_{jk}$ </td><td>Delivery unit cost for each unit of product transported from warehouse  $j$  to customer  $k$ </td></tr><tr><td> $\text{CMD}_{ij}$ </td><td>Delivery unit cost for each unit of product transported from manufacturing plant  $i$  to warehouse  $j$ </td></tr><tr><td> $\text{LW}_{mjk}$ </td><td>Delivery lead time for each unit of product delivered from warehouse  $j$  to customer  $k$  for delivery mode  $m$ </td></tr><tr><td> $\text{LM}_{mij}$ </td><td>Delivery lead time for each unit of product transported from manufacturing plant  $i$  to warehouse  $j$  for delivery mode  $m$ </td></tr><tr><td>PC</td><td>Penalty cost per unit of product incurred from tardiness</td></tr><tr><td> $T_k$ </td><td>Time of tardiness for demand  $k$ </td></tr><tr><td> $\text{DU}_k$ </td><td>Due date of demand  $k$ </td></tr><tr><td> $\text{AT}_k$ </td><td>Arrival time (total lead time) of demand  $k$ </td></tr><tr><td> $\text{MT}_{ki}$ </td><td>Production lead time of demand  $k$  in manufacturing plant  $i$ </td></tr></table>

The decision variables for this model are:

<table><tr><td> $DC_{kj}$ </td><td>A share of  $DC_k$  allocated to warehouse  $j$ </td></tr><tr><td> $DW_{ji}$ </td><td>A share of  $DW_j$  allocated to manufacturing plant  $i$ </td></tr><tr><td> $DWM_{mjk}$ </td><td>Transportation mode adapted to delivery product from warehouse  $j$  to customer  $k$ </td></tr><tr><td> $DMM_{mij}$ </td><td>Transportation mode adapted to delivery product from manufacturing plant  $i$  to warehouse  $j$ </td></tr><tr><td> $WS_{kj}$ </td><td>Storage unit time of demand  $k$  spent in warehouse  $j$ </td></tr><tr><td> $MS_{ki}$ </td><td>Storage unit time of demand  $k$  spent in manufacturing plant  $i$ </td></tr><tr><td> $SCH_{ki}$ </td><td>Ranking number of demand  $k$  in production scheduling in manufacturing plant  $i$ </td></tr></table>

## 2.2.1. Total system cost

In this problem, the total system cost can be expressed as follows: total system cost (TC) = total production cost in manufacturing plants + total inventory handling cost in warehouses + delivery cost from manufacturing plants to warehouses + delivery cost from warehouses to customers + total storage cost + total penalty cost.

MIN

$$
\begin{array}{l} \mathrm{TC} = \sum_ {i} \sum_ {j} \mathrm{DW} _ {j i} \mathrm{MPC} _ {i} + \sum_ {i} \sum_ {j} [ (\mathrm{MPC} _ {i} \\ + \mathrm{CMD} _ {i j}) \mathrm{WHC} _ {j} \mathrm{DW} _ {j i} ] + \sum_ {i} \sum_ {j} \mathrm{DW} _ {j i} \mathrm{CMD} _ {i j} \\ + \sum_ {j} \sum_ {k} \mathrm{DC} _ {k j} \mathrm{CWD} _ {j k} \\ + \sum_ {i} \sum_ {j} \sum_ {k} (\mathrm{WSC} _ {j} \mathrm{WS} _ {k j} + \mathrm{MSC} _ {i} \mathrm{MS} _ {k i}) \mathrm{DC} _ {k} \\ + \sum_ {k} T _ {k} \mathrm{DC} _ {k} \mathrm{PC} \end{array}\tag{1}
$$

where

$$
\begin{array}{l} \mathrm{CMD} _ {i j} = \sum_ {m} (\mathrm{MPC} _ {i} \mathrm{DCR} _ {m} \mathrm{LM} _ {m i j} \mathrm{DMM} _ {m i j}) \\ \mathrm{CWD} _ {j k} = \sum_ {i} \sum_ {m} ([ (\mathrm{MPC} _ {i} \\ + \mathrm{CMD} _ {i j}) \mathrm{WHC} _ {j} ] \mathrm{DCR} _ {m} \mathrm{LW} _ {m j k} \mathrm{DWM} _ {m j k}) \end{array}
$$

$$
T _ {k} = \mathrm{AT} _ {k} - \mathrm{DU} _ {k}, \text {   if   } \mathrm{AT} _ {k} > \mathrm{DU} _ {k} = 0, \text {   if   } \mathrm{AT} _ {k} \leq \mathrm{DU} _ {k}
$$

## 2.2.2. Total lead time for demands

This function can be represented as part of the customer service level. A small value implies that the demands can be delivered to customer earlier.

Total lead time required for demand k $( D _ { k } ) = { \mathfrak { p r o } } -$ roduction lead time in manufacturing plant + storage time spent in manufacturing plant + delivery lead time from manufacturing plant to warehouse + inventory handling lead time + storage time spent in warehouse + delivery lead time from warehouse to customer.

$$
\begin{array}{r l} \mathrm{AT} _ {k} & = \sum_ {i} \sum_ {j} \sum_ {m} (\mathrm{MT} _ {k i} + \mathrm{MS} _ {k i} + \mathrm{DMM} _ {m i j} \mathrm{LM} _ {m i j} \\ & \quad + \mathrm{WLT} _ {j} + \mathrm{WS} _ {k j} + \mathrm{DWM} _ {m j k} \mathrm{LW} _ {m j k}) \end{array}\tag{2}
$$

MIN

$$
\text { Total   lead   time } = \sum_ {k} \mathrm{AT} _ {k}
$$

2.2.2.1. Production lead time. In practical situations, a manufacturing plant’s production capacity is limited. The production sequence of demands scheduled determines the completion time of each demand. A demand scheduled earlier can be delivered earlier. On the other hand, it will take a longer time if it is scheduled at the end of the queue. The production lead time can be expressed as follows:

For production lead time of demand $n \left( 1 { \leq } n { \leq } k \right)$ in manufacturing plant i,

$$
\begin{array}{l} \mathrm{MT} _ {n i} = \text { Production   lead   time   required   to   produce } \\ \text { its   preceding   demands } + \text { Production   lead } \\ \text { time   required   to   produce   itself } \\ = \sum_ {j} \sum_ {k} \mathrm{DW} _ {j i} \mathrm{MLT} _ {i} X _ {k}, \text { if } \mathrm{SCH} _ {k i} \leq \mathrm{SCH} _ {n i}, \\ \text { then } X _ {k} = 1, \text { else } = 0 \end{array}\tag{3}
$$

## 2.2.3. Total number of tardy demands (TD)

This represents the total number of tardy demands caused from the optimization result, e.g., a total of 3 tardy demands. This function is independent of quantity of demands and duration of tardiness time of the demands. The purpose of this function is to minimize the number of tardy demands.

MIN

TD ¼ Number of tardy demands:

## 2.2.4. Total duration of tardiness time (TT)

This represents the total duration of tardiness time caused from the optimization result, e.g., a total of 10 tardy days, and which may have total 1 tardy demand. Similarly, it can result of a total 9 tardy days for only 3 tardy demands. The purpose of this function is to minimize the duration of tardiness time. In this case, the smallest value will be the optimal.

MIN

TT ¼ Duration of tardiness time:

## 2.2.5. Total deviation of tardy demands (TD)

This represents the equality of tardiness time between demands. A larger value indicates that the difference between the tardiness time for the demands is large, e.g., 1 and 10 tardy days for demands A and B, respectively. The purpose of this is to minimize this difference. TD is represented by mean square error (MSE).

MIN

$$
\mathrm{TD} = \left\{\sum_ {j} (T _ {k} - \text { avg. } T) ^ {2} / k \right\} ^ {1 / 2}\tag{4}
$$

where

Average number of tardiness $( \mathrm { a v g . ~ } T ) { = } \sum _ { k } T _ { k } / k$

## 2.3. Constraints

The model is subject to constraints as follows: Manufacturing plant production capacity constraints

$$
\sum_ {j} \mathrm{DW} _ {j i} \leq \mathrm{MCA} _ {i}, \quad \text { for   every } i
$$

Warehouse handling capacity constraints

$$
\sum_ {k} \mathrm{DC} _ {k j} \leq \mathrm{WCA} _ {i}, \quad \text { for   every } j
$$

Demand allocation constraints

Total demand allocated to all the warehouses = total demand

$$
\sum_ {j} \sum_ {k} \mathrm{DC} _ {k j} = \sum_ {k} \mathrm{DC} _ {k}
$$

Total demand allocated to all the manufacturing plants = total demand allocated to all the warehouses

$$
\sum_ {i} \sum_ {j} \mathrm{DW} _ {j i} = \sum_ {j} \sum_ {k} \mathrm{DC} _ {k j}
$$

Quantity of demand k allocated to all warehouses = quantity of demand k

$$
\sum_ {j} \mathrm{DC} _ {k j} = \mathrm{DC} _ {k}, \text {   for   every   } k
$$

Quantity of demand from warehouse j allocated to all manufacturing plant i = quantity of demand from warehouse j

$$
\sum_ {i} \mathrm{DW} _ {j i} = \mathrm{DW} _ {j}, \quad \text { for   every } j
$$

Delivery mode

$\begin{array} { r } { \mathrm { D W M } _ { m j k } = 1 , } \\ { \mathrm { D W M } _ { m j k } = 0 . } \end{array}$ ; if the delivery mode is adopted; else;

$\mathrm { D M M } _ { m i j } = 1$ ; if the delivery mode is adopted; else; $\mathrm { D M } \mathbf { M } _ { m i j } = 0 .$

## 2.4. Structure parameters

The input values of the mode is expressed as follows:

Demand is generated between (250 – 500) units Production capacity (2000 – 2200) units Production lead time (0.01–0.025) unit time/unit

Production unit cost (1.0 –1.5)/unit

Manufacturing storage cost (0.2 – 0.4)/unit per unit time

Warehouse capacity (2000 – 2500) units

Warehouse handling lead time (1.0 –2.0) unit time/ order

Warehouse handling cost (0.1–0.2)/unit of product value

Warehouse storage cost (0.1–0.15)/unit

Penalty cost (0.5)/unit per unit time

Delivery cost of mode 1 (0.2) of product value Delivery cost of mode 2 (0.8) of product value Delivery lead time of mode 1=(0.3 – 0.5) of delivery lead time of mode 2 per unit time for the same delivery arc.

## 3. Proposed optimization algorithm GA+AHP

A better collaboration between manufacturing plants, warehouses, and transportations may obtain a better optimization result. In this connection, the proposed optimization methodology will holistically optimize the allocation of demands, the adoption of transportation mode, and the production scheduling. It is perceivable that the number of combination simply for demands allocation to manufacturing plants and warehouses is already a large number. This complexity would increase exponentially with the addition of different choices in transportation mode. More importantly, different production scheduling causes different production lead time and completion time of demand. Consequently, it creates different result in terms of total costs and due date reliability, although the same set of demand allocation and transportation mode selected is used. In this connection, this paper divides the optimization into two parts, as shown in Fig. 2. Deploying the optimization of GAs, Part I is designed to optimize the demand allocation and the adoption of transportation mode, while Part II optimizes the production schedule of demands in manufacturing plants.

The idea of this optimization approach utilizes Part I as a core, and Part II works as auxiliary. In detail, a certain number of potential solutions will be generated in Part I. Each potential solution provides an initial framework of a distribution network, in which the demands have been allocated to warehouses and manufacturing plants, and the transportation mode have been decided in each delivery arc for each demand. The next phase will bring in the Part II for the optimization of the production scheduling for each potential solution. With the initial framework of Part I, the optimality of different production scheduling solutions are calculated by AHP. After an optimal production, scheduling is determined, the potential solution for Part I is completed in this phase. After each potential solution in Part I has been optimized by Part II, these potential solutions will be passed to calculate their fitness values and to other genetic operators. The next generation of these potential solutions will require the Part II again to optimize their production scheduling, and the iteration of these process will carry on until the evolution completed. Because optimization of multiobjective functions are involved in this distribution problem, the fitness values are evaluated by AHP [25].

![](/api/attachments/D9XE29VA/fulltext/images/385c9a267b05e40f42f79e80fde35808d3be88ff441110e5099be2580815cdd9.jpg)  
Fig. 2. An outline of the proposed optimization methodology.

## 3.1. Genetic algorithms

GAs are one of the modern heuristic optimization technique, which has been widely adopted by many researchers in solving various problems. GAs was developed by John Holland in 1960. Its heuristic optimization algorithms mimic the mechanism of genetic evolution in biological nature. A chromosome (string) is composed of genes, which represent a number of values called alleles. Each chromosome represents one potential solution. Initially, a number of chromosomes forms an initial pool of solutions. The process of crossover and mutation will be carried out in the pool; after that, an evolution is completed, new chromosomes (offspring) will be generated. A new chromosome is expected to be stronger than the parents, but this may not always be true.

GAs does not rely on analytical properties of the function to be optimized. In short, GAs have two major processes. Firstly, GAs are reiteratively and randomly generating new solutions. Secondly, these solutions are checked for the optimality according to predefined fitness functions. This becomes the most powerful principle of GAs. It makes them widely suitable for finding optimal solution in many complex problems such as traveling salesman problem and any forms of scheduling problems.

## 3.1.1. Representation of chromosome

Each chromosome represents a potential optimal solution of a problem being optimized. According to the problem structure, two different types of chromosomes are designed. Chromosome type A is designed for Part I. This chromosome is represented by a 2- dimensional matrix, as shown in Table 1a. In the supplier row, region 1, the value of gene represents the warehouse number, and the location of the gene represents the customer number. This implies the corresponding demand will be supplied through the corresponding warehouse assigned. In region 2, the value of gene represents the manufacturing plant number, and the location of the gene represents the customer number. This implies that the corresponding demand will be produced in the corresponding manufacturing plant allocated. With a similar interpretation, the transportation row shows the transportation mode to adopt. In region 1, it indicates the transportation mode between the warehouse and customer for a particular demand. In region 2, it indicates the transportation mode between manufacturing plant and warehouse for a particular demand.

A sample of chromosome structure—a five demands, three warehouses, and three manufacturing plants allocation and transportation solution

<table><tr><td></td><td colspan="10">Chromosome type A</td></tr><tr><td>Customer order</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Gene location</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Supplier</td><td> $W_1$ </td><td> $W_3$ </td><td> $W_2$ </td><td> $W_3$ </td><td> $W_1$ </td><td> $M_1$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_1$ </td></tr><tr><td>Transportation mode</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td></td><td colspan="5">Region 1</td><td colspan="5">Region 2</td></tr></table>

Decision variables—supplier and transportation mode.

A sample of chromosome structure—a five demands production scheduling solution

<table><tr><td rowspan="2"></td><td colspan="5">Chromosome type B</td></tr><tr><td> $M_1$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_1$ </td></tr><tr><td>Production scheduling</td><td>2</td><td>2</td><td>1</td><td>3</td><td>1</td></tr></table>

Decision variable—production scheduling pattern.

Chromosome type B is designed for Part II, as shown in Table 1b. The production-scheduling row indicates the ranking number of demand in the production scheduling in its manufacturing plant assigned.

## 3.1.2. Extended segment of chromosome

In the case when a single demand is larger than the maximum capacity of supply from warehouse or manufacturing plant, this order will be divided into two individual orders. One order will be in the quantity of the largest maximum absolute capacity of supply. Another order will be in the value of the remaining quantity and allocated to any other potential supplier. If the remaining quantity is still larger than the next largest maximum capacity of supply, it will be further spilt until the order can be totally allocated. The advantage of this quantity distribution is that it can fully utilize the capacity of one supplier. Moreover, in reality, the delivery cost can also be reduced due to the large delivery quantity, but this will not be considered in this model. A chromosome consists of two segments— (i) basic segment and ii) extended segment. The basic segment is mentioned previously, as shown in Table 1a and b. The representation of the splitting process is defined in the extended segment of the chromosome.

This can be exemplified by a demand order that is larger than the largest absolute capacity of the available manufacturing plants, as shown in Table 2a and b. This demand order will then be split. Number of genes in the extended segment is set equal to the number of available manufacturing plants. The location of gene represents the manufacturing plant number, such as the first gene (gene location 11) represents manufacturing plant 1 $( M _ { 1 } )$ . If the customer 1 $( D _ { 1 } )$ with an order of 1000 units, which is greater than the largest maximum capacity of any individual manufacturing plant, say $M _ { 1 }$ with 800 units, $D _ { 1 }$ will be split into two parts—800 units and 200 units. The first part will be allocated to $M _ { 1 } ,$ , and the second part will be randomly allocated to other, for example $M _ { 3 }$ in gene location 13. The chromosome type B should also be extended with corresponds to the chromosome type A for production scheduling, as shown in Table 2c.

Similar to the approach of dealing with manufacturing plant, if the demand order is larger than the largest absolute capacity of the warehouses, the extended segment will be set equal to the warehouse number. However, no change is required for the chromosome type B. In case of more than one order in excess of the largest maximum capacity of supply, each excess order will be split as previously mentioned. However, the priority of allocation among those excess orders are equally and totally arbitrary.

An example of splitting demand—the sample of chromosome with the customer order 1 greater than the largest production capacity of manufacturing plant 1

<table><tr><td></td><td colspan="10">Basic segment</td><td colspan="3">Extended segment</td></tr><tr><td>Supplier</td><td> $W_1$ </td><td> $W_3$ </td><td> $W_2$ </td><td> $W_3$ </td><td> $W_2$ </td><td> $>M_1$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_3$ </td><td>F</td><td>E</td><td>*R</td></tr><tr><td>Transportation mode</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td></tr><tr><td rowspan="3">Gene location</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>1</td><td>2</td><td>3</td></tr><tr><td colspan="5">Customer number</td><td colspan="5">Customer number</td><td colspan="3">Manufacturing plant Number</td></tr></table>

E—empty gene; \*R—remaining quantity; F—fully utilized.

Table 2b  
An example of splitting demand—the allocation representation interpreted from the sample of chromosome as presented in Table 2a

<table><tr><td colspan="6">Customer demand</td><td colspan="4">Warehouse demand</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td colspan="6">Warehouse</td><td colspan="4">Manufacturer</td></tr><tr><td>1</td><td>1000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>800</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>0</td><td>200</td><td>0</td><td>300</td><td>2</td><td>0</td><td>500</td><td>200</td></tr><tr><td>3</td><td>0</td><td>300</td><td>0</td><td>200</td><td>0</td><td>3</td><td>0</td><td>300</td><td>200</td></tr></table>

## 3.1.3. Fitness value

Fitness value is a positive value that represents the strength/desirability of a chromosome. A strong chromosome will be assigned with a large value. For example, in a problem of minimizing the cost function, if two solutions are found with A is \$300, and B is \$700, the fitness value of A and B obtained may be $( 1 - 3 0 0 / 1 0 0 0 = 0 . 7 )$ , and $( 1 - 7 0 0 / 1 0 0 0 = 0 . 3 )$ . In supply chain management, optimization of multiobjective problems may usually be encountered. In this paper, we have selected the objective functions regarding total system cost, total lead time of demands, total tardiness variations, and total number of tardy demands to focus on. In this connection, we deploy AHP to calculate the fitness values.

## 3.2. Analytic hierarchy process

AHP is developed by Thomas L. Saaty [23]. It is a well-proven multiobjective decision-making methodology, especially powerful for those complex problems with a set of highly interrelated decision factors [24]. With a pool of potential solutions, AHP helps to determine which one is the most desirable according to the decision-maker’s preference. AHP can also rank them from the most desirable to the most undesirable, with a corresponding AHP value for each solution that indicates its suitability. It is similar to the representation of fitness value. This ranking function provides the main purpose and contribution for the adoption of AHP in GAs.

Another useful feature of AHP is the assignment of attribute weightings. This allows decision makers to directly input their knowledge and experiences into the system. In addition, by adjusting the weightings, decision makers could obtain better insight about their particular scenarios by comparing different possible solutions. Different from simply giving weightings to each criterion, weightings in AHP are in pair-wise comparison. That is, decision makers can specifically compare attribute A to attribute B and attribute C, and then specifically compare the attribute of B to C, or simply make changes in subcriterion level without changing the weightings of major criterion. This approach allows a much more detailed, convenient, and flexible weightings for the decision makers.

The example problem in this paper can be modeled into four hierarchy levels, as shown in Fig. 3. Level 1 represents the objective, which is to determine the best chromosome among the solution pool. Level 2 is the major attributes (objective functions in Section 2), and level 3 is the subcriterion under the tardiness attribute. Lastly, level 4 contains the potential solutions in the solution pool. For each chromosome, the values of the optimization functions will be represented as a relative value, such as the total system cost value as shown in Eq. (5).

For total system cost objective function:

Relative cost

$$
= 1 - \frac {\text { Total   system   cost   of   the   chromosome }}{\text { Highest   total   system   cost   of   chromosome   in   the   pool }}\tag{5}
$$

A larger relative value implies that the chromosome behavior would be better in that attribute. The fitness value of that chromosome in the pool is equal to the summation of the relative value multiplied by the normalized importance weightings from the AHP for each factor.

Table 2c  
An example of splitting demand—the sample of an extended segment for chromosome type B with respect to chromosome type A shown in Table 2a

<table><tr><td rowspan="2"></td><td colspan="5">Basic segment</td><td colspan="3">Extended segment</td></tr><tr><td> $M_1$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_2$ </td><td> $M_3$ </td><td> $M_1$ </td><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td>Production scheduling</td><td>0</td><td>3</td><td>1</td><td>4</td><td>2</td><td>1</td><td>2</td><td>1</td></tr></table>

![](/api/attachments/D9XE29VA/fulltext/images/a11a559dc4f7a19b91f86236c21d84c23d8356fbd893747a28904591b58cb046.jpg)  
Fig. 3. The hierarchy structure of the proposed algorithm.

## 4. Computation results and analysis

In this paper, three experiments have been established with the same model structure and demands discussed in Section 2. These experiments focus on different purposes and have adopted different optimization approaches and different weighting in objective functions. In the Experiment 1, the optimization approach is to optimize the demand allocation, and the adoption of transportation mode, regardless of the production scheduling and penalty cost due to tardiness. That is, the Part I optimization without the auxiliary of Part II optimization. After attaining the optimal solution of demand allocation and adoption of transportation mode, the production scheduling of demand in manufacturing plant will be ranked by Part II optimization in order to minimize the penalty cost. The weighting of the total system cost will be emphasized among the level-2 attribute matrix, as shown in Fig. 4a. In this setting, there is lack of collaboration between manufacturing plants. Experiments 2 and 3 will adopt the proposed optimization methodology discussed in Section 3, involving Part I and Part II optimization. That means the entities among the network can fully collaborate. In Experiment 2, the weighting of the total system cost will be emphasized in the level-2 attribute matrix, while Experiment 3 will emphasize on the weighting of tardiness in level-2 attribute matrix, and the number of tardy demands in level-3 subattribute matrix, as shown in Fig. 4a and b, respectively.

The purpose of experiments is to testify the effect of demand due date factor in the optimization of a distribution network and the ability of the proposed optimization methodology to determine the trade-off between earliness and tardiness.

The optimization results of Experiments 1, 2, and 3 are shown in Table 3a. The results show that total system cost of Experiment 1 (41,893.30) is the highest among the three experiments, mostly due to the huge penalty cost (28,100.00). The total

![](/api/attachments/D9XE29VA/fulltext/images/86ea8653e7580e92980b530e89c736f3fb5992da3048a362f20f71b554f26268.jpg)  
Fig. 4. Weighting of attributes for various experiments. (a) Experiments 1 and 2. (b) Experiment 3.

Table 3a  
Optimization result for Experiments 1, 2, and 3

<table><tr><td>Objective functions</td><td>Exp. 1</td><td>Exp. 2</td><td>Exp. 3</td></tr><tr><td>Total system cost</td><td>41,893.30</td><td>16,923.59</td><td>17,338.83</td></tr><tr><td>Penalty cost</td><td>28,100.00</td><td>725.00</td><td>0</td></tr><tr><td>Other costs</td><td>13,793.30</td><td>16,198.59</td><td>17,338.83</td></tr><tr><td>Total lead Time</td><td>384</td><td>215</td><td>211</td></tr><tr><td>Total tardiness variations</td><td>14.60</td><td>0.64</td><td>0.00</td></tr><tr><td>Total number of tardy demands</td><td>7</td><td>2</td><td>0</td></tr></table>

system cost is the summation of the penalty cost and other costs. Penalty cost accounts the cost induced by tardiness. Other costs consist of production cost, warehouse handling cost, storage cost, and delivery cost, etc. as mentioned in Section 2. As expected, without the due date constraint, Experiment 1 obtains the lowest value in the other costs area because the system selects the cheapest transportation mode, the manufacturing plants with the lowest production unit cost, and the warehouses with the lowest handling cost. However, Experiment 1 has the highest value in penalty cost. It also bears the highest total number of tardy demands, total tardiness time and total tardiness variation, and the longest total lead time. This is because the cheapest transportation mode takes relatively longer delivery lead time. Moreover, inadequately allocating demands to single manufacturing plants induces the problem of long production lead time, as shown in Table 3b. The capacity of manufacturing plant 1 is fully utilized whereas we have low utilization ratio in other manufacturing plants. The results shows that $D _ { 3 }$ ranked with the first priority of production still cannot meet the due date. This can be explained by the inadequate adoption of transportation mode. For those demands ranked behind it, the tardiness time increases along the queue because the completion time of the preceding demands cause the long waiting time.

In Experiment 2, the optimization objective is again focused on minimization of the total system cost. Although relatively higher values for other costs are obtained, the penalty cost and the total system cost are much lesser than that in Experiment 1. This can be explained by the consideration of the due date factor during the optimization and indicates the importance of due date considering. It forces the system to adopt other different choices of manufacturing plants, warehouses, and transportation mode to reduce the high penalty cost induced by tardiness. Table 3b shows that the demands have been allocated more equally into different manufacturing plants. This relieves the problem of long production lead time. The number of tardy demands, and the tardiness time are also reduced but not totally eliminated. The reason is that the penalty cost induced by tardiness is lower than the costs involved to make changes and force the tardy demands to be satisfied on time. This shows the ability of the proposed optimization algorithm to take trade-off between earliness and tardi ness. This can be further explained by Experiment 3, which has been deliberately designed to minimize the total number of tardy demands, which is equal to minimizing the total number of tardiness time in this case. The purpose is to maximize the on time delivery of demands. The results report that all demands can satisfy as the given due date assigned. However, the total system cost increases by 2.45% to 17,338.83 compared to Experiment 2. Comparison of Experiments 2 and 3 illustrates two different possible solutions according to two different sets of attribute weightings. Indeed, more insight could be obtained by inputting more sets of attribute weightings before a decision is made.

Table 3b  
Optimization result capacity utilization and production scheduling results of Experiments 1, 2, and 3

<table><tr><td>Manufacturing plant</td><td>Exp. 1</td><td>Capacity utilization (%)</td><td colspan="7">Production scheduling</td></tr><tr><td rowspan="4"></td><td>1</td><td>100</td><td> $D_{10}$  [21] T(7)</td><td> $D_4$  [24] T(11)</td><td> $D_3$  [19] T(23)</td><td> $D_5$  [24] T(32)</td><td> $D_8$  [23] T(31)</td><td> $D_1$  [21] T(41)</td><td> $D_7$  [20] T(51)</td></tr><tr><td>2</td><td>0</td><td colspan="7"></td></tr><tr><td>3</td><td>32</td><td> $D_9$  [19] T(0)</td><td> $D_2$  [22] T(0)</td><td colspan="5"></td></tr><tr><td>4</td><td>14</td><td> $D_6$  [18] T(0)</td><td colspan="6"></td></tr><tr><td>Manufacturing plant</td><td>Exp. 2</td><td>Capacity utilization (%)</td><td colspan="7">Production scheduling</td></tr><tr><td rowspan="4"></td><td>1</td><td>30</td><td> $D_{10}$  [21] T(3)</td><td> $D_5$  [24] T(1)</td><td rowspan="2" colspan="5"></td></tr><tr><td>2</td><td>27</td><td> $D_3$  [19] T(0)</td><td> $D_6$  [18] T(0)</td></tr><tr><td>3</td><td>41</td><td> $D_9$  [19] T(0)</td><td> $D_1$  [21] T(0)</td><td colspan="5"> $D_2$  [22] T(0)</td></tr><tr><td>4</td><td>48</td><td> $D_7$  [20] T(0)</td><td> $D_8$  [23] T(0)</td><td colspan="5"> $D_4$  [24] T(0)</td></tr><tr><td>Manufacturing plant</td><td>Exp. 3</td><td>Capacity utilization (%)</td><td colspan="7">Production scheduling</td></tr><tr><td rowspan="4"></td><td>1</td><td>9</td><td> $D_1$  [21] T(0)</td><td colspan="6"></td></tr><tr><td>2</td><td>32</td><td> $D_6$  [18] T(0)</td><td> $D_{10}$  [21] T(0)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>43</td><td> $D_9$  [19] T(0)</td><td> $D_2$  [22] T(0)</td><td colspan="5"> $D_5$  [24] T(0)</td></tr><tr><td>4</td><td>61</td><td> $D_3$  [19] T(0)</td><td> $D_7$  [20] T(0)</td><td> $D_8$  [23] T(0)</td><td colspan="4"> $D_4$  [24] T(0)</td></tr></table>

[\*] – denote due date.  
T(\*) – denote tardiness time.  
[D [] T()] drawn in scale of time horizon length.

## 5. Conclusions and future research

Short and reliable demand due date is crucial in achieving high customer service level and winning of customer orders. Due date is an importance factor not only existing in decision level of job – shop scheduling but all levels throughout the supply chain. This paper studies its importance in a multiechelon distribution network problem. Tardiness induces penalty cost and negative impact on company reputation, while earliness requires higher operating costs and storage cost. Trade-off between earliness and tardiness should be determined. In addition, minimizing total system cost and achieving high service level in demand due date are conflicting in practice. A flexible and reliable optimization algorithm should be capable to allow decision makers to input weightings to determine an optimal solution, which can in fact reflecting their needs in their situations. In this connection, this paper further develop the optimization methodology of GA + AHP, which deploys the well-known decision-making technique of AHP to calculate the fitness value and allow decision makers to assign weighting in each criterion efficiently and flexibly. The proposed algorithm iteratively optimizes the demand allocation, the adoption of transportation mode, and the production scheduling by separately applying GAs in two stages. The computation results shows the importance of due date in the distribution network. It also indicates that the proposed algorithm can reduce the penalty cost incurred from tardiness by determination of the trade-off between earliness.

## 5.1. Further research

Partition of demands is a common practice in real application. This reason may be due to the factor of demand due date fulfillment and better capacity utilization. In addition, the distribution network mode discussed in this paper is a deterministic one. In practice, there are many uncertainties existing in supply chain environment, such as the production lead time, delivery reliability, and demand due date. These uncertainties influence the completion time of demands and increase the difficulties for the determination of trade-off between earliness and tardiness. Further research will be studied on the optimization of partition of demands and supply chain uncertainties.

## References

[1] S. Abdinnour-Helm, A hybrid heuristic for the uncapacitated hub location problem, European Journal of Operational Research 106 (2 – 3) (1998) 489 – 499.

[2] S. Abdinnour-Helm, Network design in supply chain management, International Journal of Agile Management Systems 1 (2) (1999) 99– 106.

[3] S. Alshawi, Logistics in the Internet age: towards a holistic information and processes picture, Logistics Information Management 18 (8) (2001) 235– 281.

[4] R.H. Ballou, Business Logistics Management, 8th edition, Prentice-Hall, Upper Saddle River, N.J., 1999.

[5] B.M. Beamon, Supply chain design and analysis: models and methods, International Journal of Production Economics 55 (3) (1998) 281–294.

[6] L.M. Berry, B.A. Murtagh, G.B. McMahon, S.J. Sugden, L.D. Welling, Genetic algorithms in the design of complex distribution networks, International Journal of Physical Distribution and Logistics Management 28 (5) (1998) 377 – 381.

[7] M. Chakraborty, S. Gupta, Fuzzy mathematical programming for multi objective linear fractional programming problem, Fuzzy Sets and Systems 125 (3) (2002) 335 – 382.

[8] F.T.S. Chan, S.H. Chung, Multi-criterion genetic optimization for distribution network problems, International Journal of Advanced Manufacturing Technology (2004) (In press).

[9] R. Cheung, M. Gen, Y. Tsujimura, A tutorial survey of job – shop scheduling problems using genetic algorithms—I, Computers & Industrial Engineering 30 (4) (1996) 983 – 997.

[10] R. Cheung, M. Gen, Y. Tsujimura, A tutorial survey of job – shop scheduling problems using genetic algorithms—part II, Computers & Industrial Engineering 37 (1) (1999) 51 – 55.

[11] M.A. Cohen, H.L. Lee, Strategic analysis of integrated production – distribution systems: models and methods, Operations Research 36 (2) (1988) 216 – 228.

[12] F. Glover, Future paths for integer programming links to artificial intelligence, Computers & Operations Research 13 (5) (1986) 533– 589.

[13] F. Glover, Tabu search part I, ORSA Journal on Computing 1 (3) (1989) 190– 206.

[14] E.L. Gonza´lez, M.A. Ferna´ndez, Genetic optimization of a fuzzy distribution model, International Journal of Physical Distribution and Logistics Management 30 (7/8) (2000) 681–696.

[15] V. Gordon, J.M. Proth, C. Chu, A survey of the state-of-the-art of common due date assignment and scheduling research, European Journal of Operational Research 139 (1) (2002) 1 – 25.

[16] R.I.V. Hoek, I. Chong, Epilogue: UPS logistics—practical approaches to the e-supply chain, International Journal of Physical Distribution and Logistics Management 31 (6) (2001) 863 – 868.

[17] Y.H. Lee, S.H. Kim, C. Moon, Production–distribution planning in supply chain using a hybrid approach, Production Planning and Control 13 (1) (2002) 35 – 46.

[18] K. Lumsden, F. Dallari, R. Ruggeri, Improving the efficiency of the hub and spoke system for the SKF European distribution network, International Journal of Physical Distribution and Logistics Management 29 (1) (1999) 60– 64.

[19] M. Marcel, J.J.M. Evers, Distribution network design: an integrated planning support framework, Logistics Information Management 9 (1) (1996) 58 – 85.

[20] A.M. Ma´rmol, J. Puerto, F.R. Ferna´ndez, Sequential incorporation of imprecise information in multiple criterion decision process, European Journal of Operational Research 137 (1) (2002) 123– 133.

[21] M. Milgate, Supply chain complexity and delivery performance: an international exploratory study, Supply Chain Management: An International Journal 6 (3) (2001) 106– 118.

[22] H. Miznuma, J. Watada, Fuzzy mixed integer programming

based on genetic algorithm and its application to resource distribution, Japanese Journal of Fuzzy Theory and Systems 7 (1) (1995) 97 – 116.

[23] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[24] T.L. Saaty, Fundamentals of decision making and priority theory with the analytic hierarchy process, in: The Analytic Hierarchy Process Series, vol. 6, RWS Publications, 1994.

[25] M. Sakawa, Genetic Algorithms and Fuzzy Multi-objective Optimization, Kluwer Academic Publishing, Boston, 2002.

[26] D.P. Song, C. Hicks, C.F. Earl, Product due date assignment for complex assemblies, International Journal of Production Economics 76 (1) (2002) 243– 256.

[27] T.P. Stank, T.F. Goldsby, A framework for transportation decision making in an integrated supply chain, Logistics Information Management 5 (2) (2000) 71–77.

[28] D.J. Thomas, P.M. Griffin, Coordinated supply chain management, European Journal of Operational Research 94 (1) (1996) 1 – 15.

[29] H.P.G. van Ooijen, J.W.M. Bertrand, Economic due-date setting in job – shops based on routing and workload dependent flow time distribution functions, International Journal of Production Economics 74 (1) (2001) 261 – 268.

[30] G.A. Vignaux, Z. Michalewica, A genetic algorithm for the linear transportation problem, IEEE Transactions on Systems, Man, and Cybernetics 21 (2) (1991) 445 – 452.

[31] I. Wilson, Distribution control systems within the supply chain, Logistics Information Management 8 (3) (1995) 80 – 82.

[32] S.H. Wu, S.H. Fuh, J.Y.H. Nee, Concurrent process planning and scheduling in distributed virtual manufacturing, IIE Transactions 34 (1) (2002) 77– 89.

[33] H. Yrjo¨la¨, Physical distribution considerations for electronic grocery shopping, International Journal of Physical Distribution and Logistics Management 31 (10) (2001) 761– 786.

![](/api/attachments/D9XE29VA/fulltext/images/6a8af2d0ba68699fa3717c887eae672406251362241ad1937e8be056eed0fe3c.jpg)

Dr. Felix Chan received his BSc in Mechanical Engineering with First Class Honour at Brighton Polytechnic (now University) in 1981. He was then obtained his MSc in Advanced Applied Mechanics and PhD at Imperial College of Science and Technology, University of London in 1982 and 1986, respectively. He was a research fellow for 2 years in the Department of Design, Manufacture and Engineering Management, University of Strathclyde.

Prior to joining The University of Hong Kong in 1996, Dr. Chan was a senior lecturer at the School of Manufacturing and Mechanical Engineering, University of South Australia. Dr Chan is now an Associate Professor at the Department of Industrial and Manufacturing Systems Engineering, The University of Hong Kong. He is also one of the admission tutors in the IMSE department. His research areas cover modeling and simulation in advanced manufacturing systems and supply chain networks, supply chain performance measurement systems, intelligent distribution methodology with multicriterion decision-making approach for logistics, and supply chain management.

![](/api/attachments/D9XE29VA/fulltext/images/5f59cf0b200d49c8879f2ec62be18723e72f84da356d7a1b6af8f982bb1efe37.jpg)  
Mr. S.H. Chung received his BSc in Industrial Management and Manufacturing Systems Engineering with First Class Honour at The University of Hong Kong in 1998. He was then obtained his M.Phil. at the same University in 2003. He is now a PhD student. His research areas include supply chain networks and intelligent distribution methodology with multicriterion decision-making approach for logistics and supply chain management.
