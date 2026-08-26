---
otero_id: 1602
otero_key: "QBVU2K47"
title: "A decision support system of vehicle routing and refueling for motor carriers with time-sensitive demands"
authors: "Yoshinori Suzuki"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system of vehicle routing and refueling for motor carriers with time-sensitive demands

Yoshinori Suzuki ⁎

Department of Supply Chain and Information Systems, College of Business, Iowa State University, 2340 Gerdin Business Building, Ames, IA 50011‐1350, USA

## a r t i c l e i n f o

Article history: Received 10 August 2011 Received in revised form 6 June 2012 Accepted 5 September 2012 Available online 12 September 2012

Keywords: Decision support system Fuel cost Motor carriers Vehicle routing Optimization

## a b s t r a c t

Given the recent trend of raising fuel cost and the increased time-sensitiveness of shippers, an extensive pressure is placed on the motor-carrier industry to meet the time-constrained customer demands at minimum fuel cost. We propose a decision support system that allows motor carriers to route each vehicle such that the vehicle not only visits all the customers in time (without violating time windows), but also utilizes the “cheapest” gas stations (cheapest truck stops in the region) as refueling points during the tour. While this approach does not necessarily minimize a vehicle's fuel consumption, as it often suggests using non-shortest routes with cheap gas stations (truck stops), it allows the vehicle to reduce the unit cost of buying fuel. Computational testing shows that the proposed approach may attain up to 4.29% savings in fuel cost for motor carriers.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

U.S. motor carriers, including the asset-based third-party logistics companies (3PLs) and the shippers with private <sup>fl</sup>eets, are currently facing a challenging business environment for two reasons. The <sup>fi</sup>rst is the raising fuel cost. It is well known that, during the last few years, fuel prices have increased dramatically by more than 100%, and that thousands of U.S. motor carriers went bankrupt because of such price hikes (Transport Topics [13]). The second is the increased time-sensitiveness of customers. Because of the growing use of lean and just-in-time operations in the manufacturing sector (a major customer segment for motor carriers), many shippers are now imposing time-window constraints on their demands (Ohlmann and Thomas [9]). Hence, an extensive pressure is placed on motor carriers to dispatch their pickup and delivery vehicles in such a way that they can meet the time-sensitive customer demands at minimum fuel costs.

Many carriers are using the following two strategies to cope with these challenges. The <sup>fi</sup>rst is to reduce the fuel consumption of each vehicle by scheduling the customer visits such that the total travel distance during a tour can be minimized without violating time windows. This can be accomplished by using the techniques (and the software products) that solve the time-constrained vehicle routing problems (Bell and Grif<sup>fi</sup>s [1]). The second is to reduce the unit-cost of buying fuel (cost per gallon). This is usually accomplished by using the “purchase contract” strategy, in which a carrier makes a commitment to buy certain amounts of fuel from a speci<sup>fi</sup>c truck stop (typically located near the company depot) to obtain price discounts. Many carriers believe that the joint use of these two strategies would minimize their fuel costs in the long run.

In theory, however, the use of these two strategies may not necessarily minimize the fuel cost of carriers. The reason is that, while the price discounts the motor carriers obtain by using purchase contracts typically range from ¢3 to ¢5 per gallon, the difference (variance) of fuel price among truck stops in the same region often goes beyond ¢10 per gallon (see, e.g., Transport Topics [14], or any publicly available fuel-price data). This pattern implies that carriers may attain larger discounts in fuel price by refueling their vehicles at “cheap” truck stops along the route (during the tour) than by using the conventional purchasecontract strategy, which limits the choice of truck stops. From the <sup>fl</sup>eet managers' standpoint, therefore, it may be more logical to use an alternative refueling strategy in which each vehicle is routed such that: (i) the vehicle not only visits all customers in time (without violating time windows) but also <sup>fi</sup>nds cheap truck stops along the route, so that (ii) the vehicle can be asked to refuel at these “cheap” truck stops.

This paper describes the work being carried out to develop a decision support system for motor carriers that is designed to address the following two questions jointly: (i) “Which route should a truck use to minimize fuel consumption”, and (ii) “Where (at which fuel station) should a truck buy fuel to minimize the fuel-procurement cost”. We develop a technique that seeks to minimize the fuel cost of operating a vehicle by jointly making the routing and refueling decisions, while enforcing the time-window constraints. This method allows carriers to consider the trade-off between using the shortest route (which can minimize the fuel consumption) and using non-shortest routes with cheap truck stops (which can minimize the unit cost of buying fuel). To the best of our knowledge, no study has considered this type of problem in the past.

The contribution of this paper is threefold. First, we present a problem (model) that jointly addresses the time-constrained single-vehicle routing problem, known as the traveling salesman problem with time windows (TSPTW), and the vehicle-refueling problem. This model, which is denoted hereafter as the traveling-salesman problem with time windows and refueling (TSPTWR), was developed by working closely with motor carriers to maximize its workability in the <sup>fi</sup>eld. Second, we propose a metaheuristic method for the TSPTWR. Our method seeks both the route and the sequence of truck stops, which (in combination) minimize the fuel cost of operating a vehicle. Third, we apply our method to both the actual and hypothetical instances, and test its effectiveness. We show that our method provides considerably lower fuel costs than the conventional method, which combines the “shortest-route” and “purchase contract” strategies.

## 2. Literature review

Since the vehicle-routing studies are reviewed extensively elsewhere (see, e.g., Figliozzi [3]), this section reviews only the studies that considered the vehicle-refueling problem, or those that jointly considered the vehicle-routing and vehicle-refueling problems, for motor carriers. Studies which proposed the vehicle-refueling methods for other modes of transportation, or those which proposed the methods of <sup>fi</sup>nding the best locations of fuel stations, are not reviewed. We refer the readers who are interested in these “other” refueling studies to Besbes and Savin [2], Suzuki [12], Wang and Lin [15], Huang et al. [4], and Nourbakhsh and Ouyang [8].

The simplest, and the earliest, form of the vehicle-refueling problem is the fixed-route vehicle refueling problem (FRVRP). The FRVRP seeks the optimal refueling policy which indicates the best sequence of truck stops to use, along with the best refueling quantities at the chosen truck stops, for a given (<sup>fi</sup>xed) origin–destination route. The FRVRP and its solution techniques were pioneered by practitioners (consulting <sup>fi</sup>rms) in the mid-1990s. The idea was to develop software products for motor carriers that allow them to buy more gallons at cheap truck stops and buy fewer gallons at expensive truck stops. Today, several software products exist that can solve the FRVRP to near-optimality, which are often called fuel optimizers by <sup>fl</sup>eet managers. These products (fuel optimizers) typically work in conjunction with truck-routing software products, so that carriers can <sup>fi</sup>rst compute the shortest route for a given origin–destination, and then <sup>fi</sup>nd a refueling policy for this route. Fuel optimizers also work in conjunction with fuel-price databases (which are updated daily), so that carriers can always utilize the latest fuel price.

Recently, several scholarly works have been conducted that proposed the exact (optimal) solution techniques for the FRVRP. Lin et al. [7] proposed a linear-time greedy (but an exact) algorithm for the FRVRP by modifying the technique widely used in the inventory-capacitated lot-sizing literature. Khuller et al. [5] also proposed a relatively simple algorithm that solves the FRVRP to optimality by employing a dynamic programming technique. Suzuki [11] proposed a mixed-integer linear programming approach to the FRVRP, and empirically showed that, for relatively small problems, the optimal refueling policies can be obtained in a straight-forward fashion by using the simplex algorithm, in conjunction with the branch-and-bound technique.

Some scholarly works have considered more complex forms of refueling problems that jointly address the shortest-route problem and the FRVRP. The motivation behind these studies is that, if the routing and refueling problems are solved sequentially (independently), we will ignore the impact of routing decisions on refueling performances, so that the resulting solutions may not be optimal (near optimal). Both

Lin [6] and Khuller et al. [5] proposed exact algorithms that jointly solve the shortest-route problem and the FRVRP. These two methods <sup>fi</sup>nd the route and the refueling policy which, in combination, minimize the fuel cost of operating a vehicle from origin to destination. It is to be noted, however, that these methods both assume that the origin and the destination represent two distinct points in a graph. This implies that they may not be applied directly to the TSP (traveling salesman problem) type instances. (Note that the TSP, which is NP-hard, and the shortest route problem with distinct origin and destination, which is not NP-hard, are intrinsically different problems that cannot be solved by the same technique).

Perhaps the work that is most relevant to this study is Khuller et al. [5]. They considered the problem that jointly addresses the TSP and the FRVRP, and proposed a heuristic method. In our view, however, their study (method) seems to suffer from limited practical values for the following two reasons. First, it does not consider some “real-world” issues and constraints that are considered by all commercial fuel optimizers. These constraints include: (i) the minimum purchase quantity per fuel stop (which prohibits “small-purchase” fuel stops and/or too many fuel stops), and (ii) the maximum distance a vehicle is allowed to travel “off the route” to reach a fuel station (which forbids a vehicle to divert excessively from the route). Second, it does not consider the customer time windows (delivery or pickup). As we had discussed previously, this constraint is increasingly recognized as an important customer-service element by motor carriers.

## 3. The decision support system

The proposed decision support system is composed of three parts; i.e., inputs, decision model, and outputs (see Fig. 1). The inputs include: (i) the set of customers to service (along with their time windows), (ii) the geographical data of the covered area, and (iii) the data on truck-stop attributes. The geographical data are readily available from many truck-routing software products (e.g., PC Miler), and the truck-stop attributes (of nearly all the truck stops in the U.S.) can be obtained from several fuel-price database products such as the OPIS (Oil Price Information Service) database. The outputs consist of the routing and refueling instructions for truck drivers. The former identi<sup>fi</sup>es the sequence (order) of customer visits, while the latter identi<sup>fi</sup>es the set of truck stops to use, along with the refueling quantity at each chosen truck stop.

The main focus of this paper is the formulation of the decision model (problem) and the development of the solution technique for the problem. In the paragraphs that follow we discuss: (i) the de<sup>fi</sup>nition and the formulation of the problem, (ii) the computational complexity of the problem, (iii) the proposed solution approach to the problem, and (iv) the set of strategies that can be used to improve the CPU time of solving the problem when using the proposed technique.

## 4. Problem formulation

## 4.1. The TSPTWR instance

Consider a TSPTW delivery instance for day t. Let $G = ( N , L )$ be a directed graph, where $N { = } \{ 0 , 1 , 2 , { \ldots } , n , n { + } 1 \}$ is the <sup>fi</sup>nite set customers (nodes) that must be visited on day t, and L is the set of arcs connecting nodes (see Fig. 2 for a sample network). The depot is represented by two nodes; 0 (starting node) and n+1 (ending node). We assume that there exists an arc $( i , j ) \in L$ for every i ∈ N \{n+1}, j ∈ N \{0}, $i \neq j .$ . The distance (miles) and travel time (minutes) of each arc (i, j) are denoted by $d _ { i j }$ and $t _ { i j } ,$ respectively. Each customer i has a speci<sup>fi</sup>c time window $\left[ S _ { i } , S _ { i } + D _ { i } \right]$ during which the customer must be served, where $S _ { i }$ and D denote the starting time and the duration, respectively, of the time window. The unloading time (duration) at each customer i is denoted by $U _ { i \cdot }$ A visit to customer i must be scheduled such that both the time to begin unloading (B ) and the time to <sup>fi</sup>nish unloading $( B _ { i } + U _ { i } )$ are within the range $[ S _ { i } , S _ { i } + D _ { i } ]$ . Like other TSPTW studies, we assume that waiting at customer sites is permitted; i.e., a truck's arrival time to customer i (A ) can be earlier than $S _ { i } ,$ but the truck cannot start unloading before $S _ { i \cdot }$

![](/api/attachments/QBVU2K47/fulltext/images/c53b1acc23a9ced48dd0be2ebdc2a0401cdb2f1ff2380c1e8c6b31ce4867b25f.jpg)  
Fig. 1. Overview of decision support system.

The truck to be used for this TSPTW has a <sup>fi</sup>xed fuel tank capacity of Q gallons and an average fuel consumption rate of $c _ { 1 }$ (gallons per mile). The vehicle is allowed to make at most z refueling stops during the tour to maintain the minimum fuel level μ in the tank at all times. Each arc $( i , j ) \in L$ has a <sup>fi</sup>nite set of refueling points $R _ { i j } = \{ 1 , 2 , . . . , k , . . . ,$ $K _ { i j } \}$ , where $K _ { i j } 2 0 \ \forall \ i \in N \ \backslash \{ n + 1 \} , j \in N \ \backslash \{ 0 \} , i \neq j$ . We denote the kth refueling point in arc (i, j) as the refueling point, or truck stop, ijk. (We also say that ijk is the $k ^ { \mathrm { { t h } } }$ truck stop connected to arc (i, j).)

Characteristics of each truck stop ijk are given by: $( i ) \ p _ { i j k }$ (fuel price per gallon on day $t ) , ( i i ) e _ { i j k }$ (out-of-route miles, or extra miles a vehicle must travel beyond d while moving along the arc (i, j), if refueling at truck stop ijk; see Fig. 2), and (iii) d<sub>ij</sub><sup>k</sup> (miles from customer i to ijk excluding $e _ { i j k } )$ . The vehicle is allowed to choose only the truck stops whose out-of-route miles (one-way) do not exceed e^ ≥0. When refueling at a truck stop, the vehicle must purchase at least $\rho { \ge } 0$ gallons, and stay at the truck stop for α≥ 0 minutes (like many commercial fuel optimizers, we assume that the refueling duration (α) is <sup>fi</sup>xed). The total route time must not exceed θb minutes.

Given the initial fuel level $\beta { \geq } \mu$ and the required minimum fuel level ε≥μ at the end of the tour, we want to determine an operational policy specifying a tour visiting each customer exactly once without violating time window, the waiting time at each customer, the truck stops to use, and the refueling quantities at the truck stops. We consider two types of fuel consumption; i.e., the fuel consumed (per mile) while the vehicle is in motion $\left( c _ { 1 } \right)$ , and the fuel consumed (per minute) while the vehicle is waiting (idling) at customer sites (c ) (when a vehicle is waiting, its engine is typically idling for various reasons; e.g., for heating or cooling the driver compartment).

![](/api/attachments/QBVU2K47/fulltext/images/d29d93269396dfb2433b76071cd968e85e5c9e29e133ed147c89ac4c41cc2fe6.jpg)  
Fig. 2. A sample network (n=3).

## 4.2. Model formulation

Our objective is to minimize the refueling cost during the tour. Since the refueling cost is given by the product of refueling quantity (gallons) and the average price of purchased fuel (cost per gallon), minimization of the refueling cost allows us to consider the trade-off between choosing the route that minimizes fuel consumption (shortest route) and choosing the route that has the most attractive truck stops. We express TSPTWR as a mixed-integer non-linear program with four types of decision variables, which are: (i) the binary variable $X _ { i j }$ indicating the tour (1 if customer j is visited right after customer i, 0 otherwise), (ii), the non-negative variable $\omega _ { i }$ indicating the waiting time at each customer i, (iii) the binary variable $\delta _ { i j k }$ indicating the refueling location (1 if refueling at truck stop ijk, 0 otherwise), and (iv) the non-negative variable $\phi _ { i j k }$ indicating the refueling quantity at truck stop ijk (see Appendix A for the complete formulation).

A TSPTWR solution is given by the set of matrices $( \Im , \Phi , \Omega ) ,$ , where 3 is the $( n + 2 ) \times ( n + 2 )$ matrix of $X _ { i j }$ variables de<sup>fi</sup>ning a TSPTW route, Φ is the h×1 vector of $\phi _ { i j k }$ variables de<sup>fi</sup>ning a refueling policy, and Ω is the h×1 vector of ω variables de<sup>fi</sup>ning a waiting policy $\begin{array} { r } { ( h = \sum _ { i \in N \backslash \{ n + 1 \} } \sum _ { j \in N \backslash \{ 0 \} } K _ { i j } ) } \end{array}$ ). Notice that $\delta _ { i j k }$ plays no role in de<sup>fi</sup>ning a TSPTWR solution. This is because the information given by $\delta _ { i j k }$ variables (refueling locations) is also included in $\phi _ { i j k }$ variables (given $\phi _ { i j k }$ values, we can easily identify the refueling locations by pooling truck stops with positive $\phi _ { i j k } ( s )$ . It is to be noted that, in our model, $\delta _ { i j k }$ variables are used mainly to impose the lower-bound and the upperbound constraints on the refueling quantity at each truck stop.

## 4.3. Problem complexity

The TSPTWR is dif<sup>fi</sup>cult to solve. It is well known that the TSPTW is a combination of the routing and scheduling problems. Hence, the TSPTWR is a combination of the routing, scheduling, and refueling problems, all of which must be solved simultaneously. Solving each of these problems is already a challenging task (TSP itself is NP-hard, and <sup>fi</sup>nding even a feasible TSPTW solution is NP-hard — see Savelsbergh, [10]), so that the problem that encompasses all of these three areas is clearly complex, even when the problem size is small. While in theory we can <sup>fi</sup>nd an optimal TSPTWR solution by using an enumeration method (where we <sup>fi</sup>rst identify all the feasible TSPTW tours and then determine, for each tour, the optimal refueling policy by solving a mixed-integer linear program similar to the FRVRP), this is extremely time-consuming.

Given this condition, we propose a heuristic method for the TSPTWR. Our approach is to decompose the TSPTWR into a routing problem (TSPTW) and a refueling problem (FRVRP), and solve these sub-problems by using existing techniques while considering their mutual impacts (i.e., we consider the impact of routing decisions on refueling performances). Our method is essentially the same as solving the original problem (before decomposition) by using (a variant of) the simulated annealing method, except that it produces solutions at a substantially faster speed. In the next section we discuss: (i) how we decompose the TSPTWR into TSPTW and FRVRP, (ii) which solution techniques we use to solve these two sub-problems, and (iii) how we integrate the solutions of these two sub-problems to derive a quality TSPTWR solution.

## 5. Proposed solution technique

## 5.1. Problem decomposition

Let $P _ { 1 }$ and $P _ { 2 }$ be the TSPTW and FRVRP sub-problems, respectively, that constitute the TSPTWR. These two sub-problems must be speci<sup>fi</sup>ed such that if we solve $P _ { 1 }$ and $P _ { 2 }$ sequentially (i.e., in two steps, where we <sup>fi</sup>rst <sup>fi</sup>nd the TSPTW route and then <sup>fi</sup>nd the refueling policy for this route), we can <sup>fi</sup>nd a feasible TSPTWR solution in most situations. This means that by solving $P _ { 1 }$ we should <sup>fi</sup>nd a feasible TSPTW tour ℑ, and by solving $P _ { 2 }$ we should <sup>fi</sup>nd a feasible set of refueling and waiting policies Φ and Ω for the tour ℑ derived in the <sup>fi</sup>rst step.

We specify $P _ { 1 }$ as a standard TSPTW where the objective is to <sup>fi</sup>nd the feasible tour that minimizes the expected fuel consumption of a vehicle. The complete formulation of $P _ { 1 }$ is given in Appendix B. We specify $P _ { 2 }$ as a mixed-integer program similar to the original TSPTWR formulation (Appendix $\mathsf { A } ) ,$ , except that $X _ { i j }$ variables are <sup>fi</sup>xed to some feasible values (with respect to $P _ { 1 }$ constraints). The complete formulation of $P _ { 2 }$ is also given in Appendix B. Notice that the $P _ { 2 }$ formulation can be viewed as an “enhanced” version of the standard FRVRP which also takes into account the time-sensitiveness (time-window constraints) of customer demands.

## 5.2. Solution techniques for sub-problems

We solve $P _ { 1 }$ by using a metaheuristic method called “compressedannealing” (Ohlmann and Thomas [9]), a variant of the standard simulated annealing technique, for its performance in producing quality solutions. This method adjusts two parameters during an annealing run; i.e., the “temperature”, which controls the probability of accepting more costly solutions (the higher the temperature the higher the probability of accepting costly solutions), and the “pressure”, which controls the probability of accepting infeasible solutions with respect to time windows (the higher the pressure the lower the probability of accepting infeasible solutions). The method starts by adopting high temperature and low pressure values, so that the probability of accepting costly and/or infeasible solutions is close to 1 at the initial phase of the annealing run (which allows us to explore the solution space extensively). The method then gradually reduces the temperature and increases the pressure over the annealing run so as to decrease the probability of accepting costly and/or infeasible solutions to 0 toward the end (which ensures the quality and feasibility of the <sup>fi</sup>nal solution). Ohlmann and Thomas [9] empirically showed that the quality of solutions given by their method either matches or outperforms those of other TSPTW techniques.

We solve P by using the simplex algorithm, in conjunction with the standard branch-and-bound technique. It can be easily shown that, unlike the original TSPTWR, $P _ { 2 }$ formulation shown in Appendix B is a linear mixed-integer program, so that it can be solved to optimality in a straightforward fashion (in one step) by using the standard integer linear programming method.

## 5.3. Limitations of sequential procedure

One way to derive a TSPTWR solution, given the above problem decomposition, is to solve $P _ { 1 }$ and $P _ { 2 }$ sequentially. This approach has an important advantage; i.e., it cuts the number of $\delta _ { i j k }$ and $\phi _ { i j k }$ variables substantially. Notice that, when solving the TSPTWR by this two-step approach, we can ignore, in the second step $( P _ { 2 } )$ , the $\delta _ { i j k }$ and $\phi _ { i j k }$ variables of those truck stops that are not located along the route ℑ found in the <sup>fi</sup>rst step $\left( P _ { 1 } \right)$ . The approach, however, has limitations too. First, it may not always generate feasible TSPTWR solutions. It can be shown that, if we solve $P _ { 1 }$ and $P _ { 2 }$ independently, the resulting solution does not necessarily satisfy all the model constraints (proof is given in the online supplement). Second, as discussed previously, simply solving $P _ { 1 }$ and $P _ { 2 }$ sequentially, in two steps, does not necessarily give quality TSPTWR solutions. These conditions suggest that, perhaps, we need a better way (system) of solving $P _ { 1 }$ and $P _ { 2 } .$ In this study we use the following procedure to <sup>fi</sup>nd feasible, quality TSPTWR solutions.

## 5.4. The solution algorithm

Our algorithm starts by solving $P _ { 1 }$ in a standard way by using the compressed annealing. However, unlike the standard compressed annealing procedure (which keeps track of only the best feasible TSPTW tour), we store in memory the M best feasible tours found during an annealing run, where $M { < } \infty$ is an arbitrary large integer. We do so by dynamically updating the vector of best M feasible tours $H _ { \mathrm { b e s t } } =$ $\{ \mathfrak { I } _ { 1 } , \mathfrak { I } _ { 2 } , . . . , \mathfrak { I } _ { m } , . . . , \mathfrak { I } _ { M } \}$ over an annealing run, where $f ( \Im _ { m } )$ is the $P _ { 1 }$ objective function of the tour $\Im _ { m } ,$ and $f ( \mathfrak { I } _ { 1 } ) { \le } f ( \mathfrak { I } _ { 2 } ) { \le } . . . { \le } f ( \mathfrak { I } _ { m } ) { \le } . . . { \le } f ( \mathfrak { I } _ { M } )$ Since the compressed annealing can revisit the same solution, we include a new tour ℑ into $H _ { \mathrm { b e s t } }$ only $\mathrm { i f } \ \Im \not \in H _ { \mathrm { b e s t } }$ . Once the annealing run is completed and $H _ { \mathrm { b e s t } }$ is <sup>fi</sup>nalized, we formulate and solve $P _ { 2 }$ for each tour in $H _ { \mathrm { b e s t } }$ (iteratively from ${ \mathfrak { I } } _ { 1 }$ to $\Im _ { M } )$ to <sup>fi</sup>nd the best policies $\Phi _ { m }$ and $\Omega _ { m }$ for each ${ \mathfrak { I } } _ { m } \in H _ { \mathrm { b e s t } }$ (hereafter this iterative process is referred to as refueling iterations). We keep track of the set of solution vectors $( \Im _ { m } , \Phi _ { m } , \Omega _ { m } )$ which, in combination, provides the best feasible $P _ { 2 }$ objective function value (i.e., best TSPTWR solution) during the refueling iterations.

It can be shown that if $M = T = \infty$ (where T denotes the annealing time) our method will produce an optimal TSPTWR solution, because in this case the method will formulate and solve $P _ { 2 }$ for all the feasible TSPTW tours; i.e., it is essentially the same as solving the TSPTWR by the enumeration method. If, on the other hand, M is small our method is unlikely to produce quality solutions (even when $T = \infty )$ , as it solves $P _ { 2 }$ for only a limited number of feasible TSPTW tours (notice that when $M = 1$ our algorithm reduces to the sequential solving of $P _ { 1 }$ and $P _ { 2 } ) .$ . This implies that, in general, the larger the M the better the solution quality, so that we should use a large value of M. In practice, however, the use of large M values may be dif<sup>fi</sup>cult, as it requires very long solution time (we must solve millions of mixed-integer programs). To get around this issue, we use the following two strategies to reduce the required time to perform the cumbersome refueling iterations without using small M values (i.e., without sacri<sup>fi</sup>cing the quality of solution).

## 5.5. Strategies for Improving Solution Time

The <sup>fi</sup>rst strategy is to reduce the number of refueling iterations by cutting those TSPTW tours which are guaranteed not to improve the solution. We <sup>fi</sup>rst perform the refueling iterations in a standard way (as described above) until we <sup>fi</sup>nd the <sup>fi</sup>rst feasible TSPTWR solution. Next, using the data of this <sup>fi</sup>rst feasible solution, we calculate the fuel consumption σ which re<sup>fl</sup>ects the threshold value (upper bound) of f(ℑ) such that any TSPTW tour for which $f ( \Im ) > \sigma$ cannot give a better TSPTWR solution than the <sup>fi</sup>rst feasible solution. We then use σ as the termination criterion such that we stop the refueling iterations at the smallest integer m where $f ( \mathfrak { I } _ { m } ) > \sigma$ is satis<sup>fi</sup>ed. We update σ every time a new “best feasible” TSPTWR solution is found, so that this stopping criterion is tightened throughout the procedure. We compute σ by solving a mixed-integer linear program (denoted $P _ { 3 } )$ . The complete $P _ { 3 }$ formulation can be found in Appendix C. Notice that this <sup>fi</sup>rst strategy cuts only that part of the computational effort which is guaranteed not to improve the solution, so that it reduces the solution time without affecting solution quality.

The second strategy is to cut the computational time per refueling iteration. We <sup>fi</sup>rst perform the refueling iterations in a standard way until we <sup>fi</sup>nd the <sup>fi</sup>rst feasible TSPTWR solution. We then use the objective value of this <sup>fi</sup>rst solution as the cut-off value to judge, in the remaining iterations $( P _ { 2 }$ solving tasks), whether to perform the branch-and-bound (B&B) enumeration. Speci<sup>fi</sup>cally, in each iteration performed after <sup>fi</sup>nding the <sup>fi</sup>rst feasible solution, we <sup>fi</sup>rst solve the relaxed version of $P _ { 2 }$ (with respect to integer constraints), and then decide whether we should proceed to the B&B by comparing the objective value of the relaxed $P _ { 2 }$ with that of the <sup>fi</sup>rst feasible solution (cut-off value). We proceed to the B&B only if the former is lower than the latter. We also use this cut-off value to reduce the $P _ { 2 }$ solution time in situations where we must proceed to the B&B. Speci<sup>fi</sup>cally, we use this cut-off value as the “incumbent” in the B&B tree search, so that any node (branch) that has an objective value above this threshold is cut off during the search. We update this cut-off value each time a new best-feasible TSPTWR solution is found. This second strategy should do a nice job of cutting the CPU time in situations where a large number of refueling iterations is inevitable (if the <sup>fi</sup>rst strategy does not work well).

It should be noted that, while the above two strategies allow us to use large M values, we may still want to avoid using extremely large M values, as they tend to reduce the compressed-annealing speeds by requiring a huge memory space (to store and update $H _ { \mathrm { b e s t } } )$ . Our experience indicates that M values between 200 and 500 are small enough to have only trivial impacts on the solution speeds but are suf<sup>fi</sup>ciently large to terminate the refueling iterations before reaching $\Im _ { M } .$ This means that by using M ∈ [200, 500] we obtain the same quality solution as that expected from the use of an extremely large value of M, but with a substantially faster speed (CPU time).

## 5.6. Termination criteria

In our algorithm, two types of termination criteria must be speci<sup>fi</sup>ed. The <sup>fi</sup>rst indicates when to stop the compressed annealing. Following Ohlmann and Thomas [9], we terminate the compressed annealing run when the best tour found has not been updated in the last 75 temperature/pressure changes, while requiring a minimum of 100 temperature/pressure changes.

The second indicates when to stop the refueling iterations. We have already mentioned this criterion above; i.e., stop at iteration m where m is the smallest integer value for which $f ( \mathfrak { I } _ { m } ) { > } \sigma$ is satis<sup>fi</sup>ed. This stopping rule, however, may not be suitable for every user (as some users may want quick solutions at the expense of reduced quality). To accommodate for this type of user heterogeneity, we introduce an additional parameter $\hat { \boldsymbol { \gamma } } \in [ 0 , 1 ]$ , which is denoted hereafter as the refueling tolerance. This parameter allows us to control the length of refueling iterations by forcing the algorithm to stop when $\gamma \le \hat { \gamma }$ is satis<sup>fi</sup>ed, where γ is given by the formula below:

$$
\gamma = \frac {O _ {\mathrm{min}}}{O _ {\mathrm{f1}}};
$$

where $O _ { \mathrm { m i n } }$ is the (P ) objective function of the best TSPTWR solution found thus far, and $O _ { \mathrm { f 1 } }$ is that of the <sup>fi</sup>rst feasible TSPTWR solution. This formula indicates that: (i) for quality solutions we should let $\hat { \gamma } = 0$ so that the algorithm will not stop until $f ( \Im _ { m } )$ >σ is satis<sup>fi</sup>ed, but (ii) for quick solutions we should let $\hat { \gamma } = 1$ so that the algorithm will stop when it <sup>fi</sup>nds the <sup>fi</sup>rst feasible solution. The complete description (outline) of our solution algorithm is shown in Fig. 3.

## 6. Application

This section applies the proposed method to both real-world and hypothetical instances to test its performance. We <sup>fi</sup>rst apply the method to three real-world instances to verify that it can actually be used in practice. We then apply the method to randomly-generated instances and conduct six simulation experiments to obtain robust estimates of its cost-saving potentials. We report two computational results for the proposed method; i.e., one with $\hat { \gamma } = 1$ and the other with $\hat { \gamma } = 0 .$ We use the Visual Basic .NET (2008), along with the CPLEX optimizer (version 11.2), to implement the algorithm, and run the codes on a 2.93 GHz quad-core PC with 6 GB of DDR3 memories. For space limitations we omit the details on how the compressed-annealing parameters are speci<sup>fi</sup>ed in this study (details are available to the interested readers upon request).

## 6.1. Design of testing

Our computational testing is designed to mimic the actual business environment of a medium-sized trucking company based in Portland, U.S.A. This (anonymous) motor carrier, which collaborated with us for conducting this TSPTWR study, is denoted hereafter as Carrier X.

The <sup>fi</sup>rst part of the testing is performed by solving three actual instances obtained from Carrier X. Characteristics of these actual instances are shown in Table 1. The second part of the testing is performed by generating and solving numerous hypothetical instances. These hypothetical instances are generated by randomly choosing n customers from the list of existing customers obtained from Carrier X. Characteristics of the hypothetical instances are also shown in Table 1. To gain insights into the conditions under which our method works most effectively, we perform six simulation experiments in the second part of our testing by adopting a two-factor, 2×3 experimental design with $n \in \{ 1 0 , 2 0 \}$ and $D _ { i }$ (in minutes ∀ i) ∈ {360, 300, 240}. This design allows us to test the impact of problem size (n) and time-window duration (D ) on the effectiveness of our method. In each experiment we create and solve 1,000 TSPTWR instances.

We obtained the necessary inputs for our numerical testing (e.g., network characteristics such as $d _ { i j }$ and $t _ { i j } ,$ and truck stop attributes such as $p _ { i j k }$ and $e _ { i j k } )$ from PC Miler and ProMiles (the former is a well-known truck-routing software product and the latter is a widely-used fuel optimizer in the <sup>fi</sup>eld, which contains the OPIS database). Selected parameters are shown in Table 2. These parameters are determined mainly by consulting with <sup>fl</sup>eet managers of Carrier X. Notice that we use relatively small n values in our testing (10 or 20). This is because, according to Carrier X, their pickup-and-delivery vehicles seldom visit more than 15 customers per tour.

We compare the cost of our method with those of three benchmark methods. The <sup>fi</sup>rst (benchmark method I) gives the cost expected under the actual routing and refueling practices used by Carrier X. This cost is determined by <sup>fi</sup>rst calculating the expected fuel consumption of a vehicle when following the actual route used by Carrier X, and then

## 6.2. Benchmark methods

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Set M, the size of  $H_{best}$ 

Initialize  $H_{best}$  such that  $f(\mathfrak{I}_{m}) = \infty \forall m = 1, 2, \ldots, M$ 

Generate initial tour I

Let g = 0

Set initial temperature and pressure,  $\tau_{0}, \lambda_{0}$ 

Set t, the number of iterations at each temperature/pressure

Repeat:

Let counter = 0

Repeat:

Randomly generate  $\chi$ , a neighbor tour of I

With the probability given by Ohlmann and Thomas (2007) $^{a}$ , let I =  $\chi$ 

If I is feasible,  $f(\mathfrak{I}) &lt; f(\mathfrak{I}_{M})$ , and  $I \notin H_{best}$ , let  $I_{M} = I$ 

Sort  $H_{best}$  in ascending order such that  $f(\mathfrak{I}_{1}) \leq f(\mathfrak{I}_{2}) \leq \ldots \leq f(\mathfrak{I}_{M})$ 

Increment counter by 1

Until counter is equal to t

Increment g by 1

Update  $\tau_{g}$  and  $\lambda_{g}$  according to cooling/compression schedules

Until compressed-annealing termination criterion is satisfied

Initialize the best TSPTWR solution ( $I_{best}, \Phi_{best}, \Omega_{best}$ ) such that its cost  $\eta(\mathfrak{I}_{\text{best}}, \Phi_{\text{best}}, \Omega_{\text{best}}) = \infty$ 

Set refueling tolerance  $\hat{\gamma}$ 

Let termination criterion  $\sigma = \infty$ 

Let m = 1

Repeat:

Retrieve  $I_{m}$  from the set  $H_{best}$  ( $m^{th}$  element of  $H_{best}$ )

If  $f(\mathfrak{I}_{m}) &gt; \sigma$ , terminate algorithm

Formulate and solve relaxed version of  $P_{2}$  for  $I_{m}$  (with respect to integer constraints)

If solution is feasible and objective value &lt;  $\eta(\mathfrak{I}_{\text{best}}, \Phi_{\text{best}}, \Omega_{\text{best}})$ :

Solve  $P_{2}$  via B&amp;B (let  $\eta(\mathfrak{I}_{\text{best}}, \Phi_{\text{best}}, \Omega_{\text{best}}) = \text{incumbent}$ )

If integer solution ( $\Phi_{m}, \Omega_{m}$ ) is feasible and objective value &lt;  $\eta(\mathfrak{I}_{\text{best}}, \Phi_{\text{best}}, \Omega_{\text{best}})$ :

Let  $I_{best} = I_{m}, \Phi_{best} = \Phi_{m}, \Omega_{best} = \Omega_{m}$ 

Let  $\eta(\mathfrak{I}_{\text{best}}, \Phi_{\text{best}}, \Omega_{\text{best}}) = \text{objective function of } P_{2} \text{ evaluated at } (\Phi_{m}, \Omega_{m})$ 

Calculate  $\gamma$ ; and terminate algorithm if  $\gamma \leq \hat{\gamma}$ 

Solve  $P_{3}$ , and let  $\sigma = P_{3}$  objective value

Increment m by 1

Until m is equal to M
</div>

Table 1 Problem characteristics.

<table><tr><td rowspan="2"></td><td colspan="3">Actual instances</td><td colspan="3">Hypothetical instances</td></tr><tr><td>Prob. 1</td><td>Prob. 2</td><td>Prob. 3</td><td>Avg.</td><td>Min.</td><td>Max.</td></tr><tr><td>Number of customers (n)a</td><td>10</td><td>10</td><td>10</td><td>-</td><td>10</td><td>20</td></tr><tr><td>Time window width (min.)a</td><td>360</td><td>360</td><td>360</td><td>-</td><td>240</td><td>360</td></tr><tr><td>Avg. num. of truck stops per arcb</td><td>2.318</td><td>1.264</td><td>2.145</td><td>5.007</td><td>0</td><td>14</td></tr><tr><td>Avg. fuel price per gallon ($)b</td><td>2.025</td><td>2.006</td><td>2.025</td><td>2.072</td><td>1.919</td><td>2.440</td></tr><tr><td>Avg. OOR miles of truck stopsb</td><td>0.479</td><td>0.888</td><td>0.615</td><td>0.262</td><td>0.000</td><td>2.900</td></tr><tr><td>Avg. arc distance (miles)b</td><td>61.99</td><td>35.54</td><td>52.78</td><td>143.48</td><td>4.60</td><td>418.70</td></tr><tr><td>Avg. arc traversal time (min.)b</td><td>70.64</td><td>43.14</td><td>61.50</td><td>143.81</td><td>3.60</td><td>443.40</td></tr></table>

<sup>a</sup> These represent experimental factors in simulation experiments (hypothetical instances).  
<sup>b</sup> For hypothetical instances these re<sup>fl</sup>ect the characteristics of the graph from which instances are drawn.

multiplying the resulting <sup>fi</sup>gure by the expected fuel price per gallon under the “purchase contract” strategy. The expected fuel price is determined by <sup>fi</sup>rst calculating the average fuel price of all the truck stops located within 10-mile radius from the carrier's depot, and then subtracting ¢5 from the resulting <sup>fi</sup>gure (recall that the purchasecontract strategy typically gives price discounts of ¢3 to ¢5 per gallon).

The second (benchmark method II) calculates the cost under the assumption that a vehicle: (i) follows the best TSPTW tour found by the compressed-annealing, and (ii) refuels only at the truck stop with purchase contract. This cost is obtained by using the same procedure as benchmark method I, except that the expected fuel consumption during the tour is calculated by using the best TSPTW tour found via the compressed annealing, instead of the actual route used by Carrier X. Note that this method is similar to the conventional cost-saving approach discussed earlier, where the shortest-route and the purchasecontract strategies are used jointly.

The third (benchmark method III) gives the optimal TSPTWR cost. This third cost is computed by using the enumeration technique discussed earlier (“problem complexity” section), which <sup>fi</sup>rst identi<sup>fi</sup>es all the feasible TSPTW tours (that do not violate time windows), and then solves the mixed-integer linear program (P<sub>2</sub>) for each of them. Since this is an extremely time-consuming technique, we calculate the cost of benchmark method III only for “actual” (n=10) instances (it is practically impossible to solve problems with n>10 by this enumeration method).

It is to be noted that our benchmark methods do not include the “sequential” or “two-step” solution procedure discussed earlier, which <sup>fi</sup>rst computes the (near) optimal TSPTW route via the compressed annealing and then <sup>fi</sup>nds the best refueling policy for this route by solving the $P _ { 2 }$ linear integer program via the simplex algorithm. This is because the TSPTWR solutions produced by this sequential procedure, if they are feasible, will always be identical to those given by the proposed algorithm (γ^ =1). Thus, while a seemingly attractive benchmark, this two-step procedure is excluded from our benchmark methods to avoid redundancy in reporting our results.

<table><tr><td>Parameters</td><td>Value</td><td>Unit</td><td>Source</td></tr><tr><td>Fuel consump. per mile while in motion ( $c_1$ )</td><td>0.167</td><td>gallons</td><td>Carrier X</td></tr><tr><td>Fuel consump. per minute while waiting ( $c_2$ )</td><td>0.012</td><td>gallons</td><td>Carrier X</td></tr><tr><td>Starting fuel ( $\beta$ )</td><td>120</td><td>gallons</td><td>—</td></tr><tr><td>Ending fuel ( $\varepsilon$ )</td><td>120</td><td>gallons</td><td>—</td></tr><tr><td>Tank capacity ( $Q$ )</td><td>200</td><td>gallons</td><td>Carrier X</td></tr><tr><td>Refueling duration ( $\alpha$ )</td><td>30</td><td>minutes</td><td>Carrier X,ProMiles</td></tr><tr><td>Minimum refueling quantity ( $\rho$ )</td><td>50</td><td>gallons</td><td>Carrier X,ProMiles</td></tr><tr><td>Lower-bound fuel level ( $\mu$ )</td><td>40</td><td>gallons</td><td>Carrier X</td></tr><tr><td>Maximum refueling stops ( $z$ )</td><td>3</td><td>times</td><td>Carrier X</td></tr><tr><td>Maximum out-of-route miles ( $\hat{e}$ )</td><td>3</td><td>miles</td><td>Carrier X,ProMiles</td></tr><tr><td>Maximum route time ( $\theta$ )a</td><td>14/24</td><td>hours</td><td>Carrier X</td></tr><tr><td>Maximum refueling iteration ( $M$ )</td><td>200</td><td>times</td><td>—</td></tr></table>

<sup>a</sup> 14 hr for n=10, and 24 hr for n=20 (we assume team driving for the latter instances).

## 6.3. Computational results

Results are reported in Tables 3 to 5. Table 3 shows the results of solving the three actual instances, while Tables 4 to 5 show the results of simulation experiments. In Table 3 the results of our method (and those of benchmark method II) are obtained by performing ten optimization runs per instance and calculating averages. In Tables 4 and 5 the results of our method are obtained by performing one optimization run per instance. The most important <sup>fi</sup>ndings follow.

First, our method seems to perform well in actual instances. Table 3 indicates that our method outperforms both benchmark methods I and II in terms of fuel cost in all of the three actual instances. The table shows that the fuel cost of our method (γ^ =0 or 1) is 8.3% to 14.4% lower than that of benchmark method I, and 1.2% to 1.7% lower than that of benchmark method II. This pattern implies that Carrier X may save up to 14.4% in fuel cost by utilizing our method in lieu of their current routing method. This also implies that our method may outperform the conventional approach (benchmark method II) by 1.2% to 1.7% in fuel cost. As expected, our method suggests using the route which requires more fuel consumption than the minimum-fuel route, but this extra fuel consumption (0.26% to 0.38%) is compensated by using the “cheap” truck stops as refueling points. It is to be noted that our method <sup>fi</sup>nds the optimal solutions (benchmark method III) in all of the actual instances when γ^ =0, and <sup>fi</sup>nds either the optimal solutions (problems 1 and 3) or a near-optimal solution (problem 2) when $\hat { \gamma } = 1 .$ . This condition suggests that our method consistently converges to the optimal or quality TSPTWR solutions.

Second, the cost-saving advantage of the proposed method over the conventional method (benchmark method II) is quite robust. Simulation results (Tables 4 and 5) show that, on average, our method attains cost savings of 1.62% ( γ^ =1) and 1.65% ( γ^ =0) over the conventional method when n=10, and 3.95% (γ^ =1) and 4.29% (γ^ =0) when n=20. This implies that our method outperforms the conventional approach not only in a limited number of actual instances (Table 3), but also in a series of experiments performed over a large number of instances. Statistical tests (paired t–tests) showed that the cost of our method (γ^ =1 or 0) and that of the conventional method are signi<sup>fi</sup>cantly different at the 99.9% con<sup>fi</sup>dence level in all of the experiments (n=10 or 20). These results suggest that our method may be used as a viable alternative to the conventional approach. It is worth noting that statistical tests also showed that the cost of our method when γ^ =1 and that when γ^ =0 are signi<sup>fi</sup>cantly different at the 99.9% con<sup>fi</sup>dence level in all the experiments (n=10 or 20). This <sup>fi</sup>nding suggests that carriers may attain signi<sup>fi</sup>cantly lower fuel cost by setting γ^ =0 than by setting γ^ =1 when using our method.

Third, the effectiveness of our method seems to be affected by the values of experimental factors (n and D ). Two notable <sup>fi</sup>ndings follow. First, the bene<sup>fi</sup>t of using our method seems to improve with the problem size (n). Tables 4 and 5 indicate that the cost saving achieved by our method over the conventional method is larger when $n = 2 0$ (3.95% for γ^ =1 and 4.29% for γ^ =0) than when n=10 (1.62% for γ^ =1 and 1.65% for γ^ =0). This pattern implies that the effectiveness of our method may be an increasing function of n. Second, the performance of our method relative to that of the conventional method seems to improve as the time-window length (duration) diminishes. Tables 4 and 5 show that, as the time-window length decreases from 360 to 240 minutes, the cost saving attained by our method over the conventional method increases considerably (from \$2.057 to \$ 2.247 whenγ^ =1 and $n = 1 0 ;$ from \$14.864 to \$ 16.432 when γ^ =1 and n=20; from \$2.090 to \$ 2.286 when γ^ =0 and n=10; from \$15.936 to \$ 18.003 when γ^ =0 and n=20). This pattern suggests that our method may generate higher cost savings to the carriers with tight (narrow) time windows than to those with weak (loose or no) time windows.

Table 3 Computational results (actual).

<table><tr><td rowspan="2"></td><td rowspan="2">Benchmark method I</td><td rowspan="2">Benchmark method II</td><td rowspan="2">Benchmark method III</td><td colspan="2">Proposed method</td></tr><tr><td> $\hat{\gamma}=1$ </td><td> $\hat{\gamma}=0$ </td></tr><tr><td colspan="6">Problem 1 (n=10)</td></tr><tr><td>CPU time (sec.)a</td><td>-</td><td>1.474</td><td>234.6</td><td>2.106</td><td>2.203</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>-</td><td>-</td><td>1</td><td>7</td></tr><tr><td>Fuel consumed (gallons)</td><td>87.929</td><td>78.968</td><td>79.222</td><td>79.222</td><td>79.222</td></tr><tr><td>Number of refueling stops made</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>1.964</td><td>1.964</td><td>1.930</td><td>1.930</td><td>1.930</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>172.702</td><td>155.102</td><td>152.923</td><td>152.923</td><td>152.923</td></tr><tr><td colspan="6">Problem 2 (n=10)</td></tr><tr><td>CPU time (sec.)a</td><td>-</td><td>1.500</td><td>1,430.8</td><td>2.077</td><td>2.263</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>-</td><td>-</td><td>1</td><td>49</td></tr><tr><td>Fuel consumed (gallons)</td><td>62.607</td><td>54.219</td><td>54.358</td><td>54.358</td><td>54.358</td></tr><tr><td>Number of refueling stops made</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>1.964</td><td>1.964</td><td>1.935</td><td>1.935</td><td>1.935</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>122.955</td><td>106.481</td><td>105.207</td><td>105.208</td><td>105.207</td></tr><tr><td colspan="6">Problem 3 (n=10)</td></tr><tr><td>CPU time (sec.)a</td><td>-</td><td>1.468</td><td>375.3</td><td>2.264</td><td>2.293</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>-</td><td>-</td><td>1</td><td>5</td></tr><tr><td>Fuel consumed (gallons)</td><td>68.518</td><td>63.903</td><td>64.146</td><td>64.146</td><td>64.146</td></tr><tr><td>Number of refueling stops made</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>1.960</td><td>1.960</td><td>1.919</td><td>1.919</td><td>1.919</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>134.276</td><td>125.231</td><td>123.079</td><td>123.079</td><td>123.079</td></tr></table>

<sup>a</sup> For benchmark method II the CPU time re<sup>fl</sup>ects that of performing the compressed annealing run.

Fourth, it seems that our algorithm can <sup>fi</sup>nd a feasible TSPTWR solution within a reasonable CPU time. Table 4 shows that, when n=10, the average run time of our algorithm ranges between 2.026 seconds ( γ^ =1) and 2.619 seconds ( γ^ =0). These <sup>fi</sup>gures compare favorably with the CPU times of the enumeration (exact) method, which range roughly from 4 to 23 minutes (see Table 3). Table 5 shows that, even after n is increased to 20, the average run time of our algorithm still remains to be reasonable, ranging between 1.851 seconds ( γ^ =1) and 4.592 seconds ( γ^ =0). Although the run time of an algorithm can vary depending on several factors (e.g., processor speed, memory size, bus speed, and language implementation), it seems that our algorithm can solve the TSPTWR within <sup>fi</sup>ve seconds under many realistic settings.

## 6.4. Cost-saving potential

The analyses indicate that our method may attain up to 4.29% savings in fuel cost over the conventional approach. This cost-saving <sup>fi</sup>gure, while seemingly trivial on an instance-by-instance basis (saves \$2.06 to \$18.00 per instance), converts to a large cost saving for the U.S. trucking industry as a whole. Assuming, for example, the total fuel burns of 36.4 billion gallons per year for the U.S. trucking industry (Transport Topics [14]), the above <sup>fi</sup>gure suggests that our method, if properly implemented, may save over \$3 billion of fuel cost for the industry per year.

It is worth noting that this study was conducted by using the fuel-price data of 2010, the average diesel fuel price of which was only about \$2. This condition suggests that the results reported in this paper may somewhat underestimate the cost-saving potential of the proposed method. Our estimates indicate that, if applied under the current pricing condition (diesel price of roughly \$3 per gallon), the proposed method should produce the cost saving of roughly \$4.7 billion per year. The cost-saving <sup>fi</sup>gure becomes even larger if the fuel price continues to increase in the future. Our estimates show that, if the diesel fuel price goes beyond \$6 per gallon (which re<sup>fl</sup>ects the current pricing condition of many non-U.S. countries), the cost-saving potential of the proposed method may exceed \$9 billion per year for the U.S. trucking industry.

Computational results (hypothetical instances with $n = 1 0 ) . { \overset { \underset { \mathrm { a , b , c } } { } } { } }$

<table><tr><td rowspan="2"></td><td rowspan="2">Benchmark method II</td><td colspan="2">Proposed method</td></tr><tr><td> $\hat{\gamma}=1$ </td><td> $\hat{\gamma}=0$ </td></tr><tr><td colspan="4">Experiment 1 (6 hr time-window width)</td></tr><tr><td>CPU time (sec.)</td><td>1.506</td><td>2.026</td><td>2.619</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>1.000</td><td>44.656</td></tr><tr><td>Fuel consumed (gallons)</td><td>65.977</td><td>65.977</td><td>65.996</td></tr><tr><td>Number of refueling stops made</td><td>1.000</td><td>1.000</td><td>1.000</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>1.971</td><td>1.939</td><td>1.938</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>130.016</td><td>127.959</td><td>127.926</td></tr><tr><td colspan="4">Experiment 2 (5 hr time-window width)</td></tr><tr><td>CPU time (sec.)</td><td>1.540</td><td>2.073</td><td>2.548</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>1.000</td><td>34.590</td></tr><tr><td>Fuel consumed (gallons)</td><td>67.340</td><td>67.340</td><td>67.353</td></tr><tr><td>Number of refueling stops made</td><td>1.000</td><td>1.000</td><td>1.000</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>1.963</td><td>1.939</td><td>1.938</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>132.718</td><td>130.556</td><td>130.530</td></tr><tr><td colspan="4">Experiment 3 (4 hr time-window width)</td></tr><tr><td>CPU time (sec.)</td><td>1.557</td><td>2.095</td><td>2.520</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>1.001</td><td>30.923</td></tr><tr><td>Fuel consumed (gallons)</td><td>68.690</td><td>68.690</td><td>68.704</td></tr><tr><td>Number of refueling stops made</td><td>1.000</td><td>1.001</td><td>1.000</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>1.963</td><td>1.939</td><td>1.938</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>135.414</td><td>133.167</td><td>133.128</td></tr></table>

<sup>a</sup> Sample size is 1,000 for each experiment (<sup>fi</sup>gures shown in the table are averages).  
<sup>b</sup> Costs of benchmark method I are not calculated, as the data of actual routes are not available.  
<sup>c</sup> Costs of benchmark method III are not calculated, as this method is too time-consuming.

Computational results (hypothetical instances with $n = 2 0 ) . \overset { \mathrm { a , b , c } } { \cdot }$

<table><tr><td rowspan="2"></td><td rowspan="2">Benchmark method II</td><td colspan="2">Proposed method</td></tr><tr><td> $\hat{\gamma}=1$ </td><td> $\hat{\gamma}=0$ </td></tr><tr><td colspan="4">Experiment 1 (6 hr time-window width)</td></tr><tr><td>CPU time (sec.)</td><td>2.171</td><td>2.193</td><td>4.001</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>1.0578</td><td>45.041</td></tr><tr><td>Fuel consumed (gallons)</td><td>175.333</td><td>175.343</td><td>175.546</td></tr><tr><td>Number of refueling stops  $made^d$ </td><td>2.000</td><td>1.998</td><td>1.993</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>2.043</td><td>1.958</td><td>1.949</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>358.150</td><td>343.286</td><td>342.215</td></tr><tr><td colspan="4">Experiment 2 (5 hr time-window width)</td></tr><tr><td>CPU time (sec.)</td><td>2.036</td><td>2.073</td><td>4.255</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>1.5439</td><td>54.825</td></tr><tr><td>Fuel consumed (gallons)</td><td>194.860</td><td>194.905</td><td>195.166</td></tr><tr><td>Number of refueling stops  $made^d$ </td><td>2.030</td><td>1.999</td><td>1.998</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>2.048</td><td>1.965</td><td>1.956</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>399.023</td><td>383.074</td><td>381.668</td></tr><tr><td colspan="4">Experiment 3 (4 hr time-window width)</td></tr><tr><td>CPU time (sec.)</td><td>1.787</td><td>1.851</td><td>4.592</td></tr><tr><td>Total refueling iterations performed</td><td>-</td><td>2.0767</td><td>54.021</td></tr><tr><td>Fuel consumed (gallons)</td><td>215.978</td><td>216.107</td><td>216.345</td></tr><tr><td>Number of refueling stops  $made^d$ </td><td>2.172</td><td>2.012</td><td>2.003</td></tr><tr><td>Avg. refueling price ($ per gallon)</td><td>2.052</td><td>1.975</td><td>1.965</td></tr><tr><td>Total refueling cost of the tour ($)</td><td>443.225</td><td>426.793</td><td>425.222</td></tr></table>

<sup>a</sup> Sample size is 1,000 for each experiment (<sup>fi</sup>gures shown in the table are averages). b Costs of benchmark method I are not calculated, as the data of actual routes are not available.  
<sup>c</sup> Costs of benchmark method III are not calculated, as this method is too time-consuming. c Costs of benchmark method III are not calculated, as this method is too time-consuming.  
<sup>d</sup> When it is necessary to refuel on the road under benchmark method II, a vehicle is assumed to buy, at a randomly selected truck stop, the minimum fuel to reach the truck stop with purchase contract near the depot.

## 7. Conclusions and limitations

This study provides two types of implications to practitioners. First, motor carriers, asset-based 3PLs, and shippers with private <sup>fl</sup>eet may wish to re-consider their routing/refueling strategies. Our computational results suggest that the fuel cost (refueling cost) of vehicles can become noticeably lower by using the proposed “refuel over the road” strategy, in lieu of using the conventional approach. Thus, rather than negotiating price discounts with a limited number of truck stops near their depots, motor carriers may want to start looking at much wider geographic regions in search for the truck stops that offer signi<sup>fi</sup>cantly lower fuel prices. Second, consulting <sup>fi</sup>rms, fuel-optimizer vendors, and other software companies may wish to develop vehicle-routing software products that can solve the TSPTWR (perhaps by using the technique proposed in this paper). Our computational testing shows promising results for using this type of software products in the <sup>fi</sup>eld. Given that the trucking industry can possibly save billions of dollars in fuel cost by using the approach proposed in this paper, it is possible (even likely) that motor carriers show strong interests in using such software products once they are developed.

One limitation of this study is that our TSPTWR model may underestimate the costs associated with travel miles. Appendix A shows that, in our model, the only cost associated with travel miles is the fuel cost. In reality, however, there are other costs that can increase with trip miles. These include, but are not limited to, vehicle maintenance costs and driver wages (truck drivers are typically paid by miles or hours). This implies that, if these other “distance-related” costs are considered, the cost-saving potential of our method (which often suggests using non-shortest routes) may become lower than that reported in this paper. Although we believe that our approach (fuel-cost minimization) properly re<sup>fl</sup>ects the goal of many carriers, future research may wish to develop an alternative TSPTWR form that also considers other (i.e., non-fuel) costs.

## Appendix A. TSPTWR formulation

Let $r _ { i }$ be the vehicle's fuel level when arriving at customer i (before waiting), $r _ { i j k }$ be the vehicle's fuel level either at truck stop ijk before buying fuel $( \mathrm { i f } \ \delta _ { i j k } = 1 )$ or at the diversion point to ijk $( \mathrm { i f } \delta _ { i j k } = 0 ;$ see Fig. $2 ) ,$ , and $\nu _ { i j k }$ be the vehicle's travel speed (miles per minute) when diverting from arc $( i , j )$ to reach truck stop ijk (we assume that $\nu _ { i j k } = d _ { i j } / t _ { i j } \forall i \in N \ \lvert \{ n + 1 \} , j \in N \ \lvert \{ 0 \} , k \in R _ { i j } , i \neq j ,$ , but other $\nu _ { i j k }$ values may also be used). The TSPTWR can be expressed as:

$$
\underset {X _ {i j}, \omega_ {i}, \delta_ {i j k}, \phi_ {i j k}} {\text { minimize }} \sum_ {i \in N} \sum_ {\{n + 1 \}   j \in N} \sum_ {\{0, i \}} \sum_ {k \in R _ {i j}} p _ {i j k} \phi_ {i j k}\tag{1}
$$

$$
\text { subject   to }: X _ {i j} \in \{0, 1 \} \forall i \in N \setminus \{n + 1 \}, j \in N \setminus \{0 \}, i \neq j;\tag{2}
$$

$$
\delta_ {i j k} \in \{0, 1 \} \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{3}
$$

$$
\sum_ {j \in N \{0, i \}} X _ {i j} = 1 \quad \forall i \in N \backslash \left\{n + 1 \right\};\tag{4}
$$

$$
\sum_ {i \in N \{j, n + 1 \}} X _ {i j} = 1 \quad \forall j \in N \backslash \left\{0 \right\};\tag{5}
$$

$$
\left[ A _ {j} - B _ {i} - U _ {i} - t _ {i j} - \sum_ {k \in R _ {i j}} \delta_ {i j k} \left(\alpha + \frac {2 e _ {i j k}}{v _ {i j k}}\right) \right] X _ {i j} = 0 \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, i \neq j;\tag{6}
$$

$$
B _ {i} = A _ {i} + \omega_ {i} \geq S _ {i} \quad \forall i \in N \backslash \{0 \};\tag{7}
$$

$$
B _ {i} + U _ {i} \leq S _ {i} + D _ {i} \quad \forall i \in N \backslash \{0 \}.\tag{8}
$$

$$
B _ {0} = U _ {0} = S _ {n + 1} = U _ {n + 1} = 0, \quad D _ {n + 1} = \theta ;\tag{9}
$$

$$
\delta_ {i j k} \leq X _ {i j} \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{10}
$$

$$
\delta_ {i j k} e _ {i j k} \leq \hat {e} \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{11}
$$

$$
\phi_ {i j k} \geq \delta_ {i j k} \rho \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{12}
$$

$$
\phi_ {i j k} \leq \delta_ {i j k} Q \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{13}
$$

$$
r _ {i j k} + \phi_ {i j k} \leq Q \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{14}
$$

$$
\sum_ {i \in N \{n + 1 \}} \sum_ {j \in N \{0, i \}} \sum_ {k \in R _ {i j}} \delta_ {i j k} \leq z;\tag{15}
$$

$$
r _ {0} = \beta ;\tag{16}
$$

$$
r _ {n + 1} \geq \varepsilon ;\tag{17}
$$

$$
r _ {i} \geq \mu \quad \forall i \in N \backslash \{0, n + 1 \};\tag{18}
$$

$$
\left(r _ {i j k} - \mu\right) X _ {i j} \geq 0 \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{19}
$$

$$
\left. \right.\left[ r _ {j} - \left(r _ {i} + \sum_ {k \in R _ {i j}} \phi_ {i j k} - c _ {1} \left(d _ {i j} + \sum_ {k \in R _ {i j}} 2 \delta_ {i j k} e _ {i j k}\right) - c _ {2} \omega_ {i}\right)\right]
$$

$$
X _ {i j} = 0 \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, i \neq j;\tag{20}
$$

$$
\begin{array}{l} r _ {i j k} = \left\{ \begin{array}{l} r _ {i} - c _ {1} \Big (d _ {i j} ^ {k} + \delta_ {i j k} e _ {i j k} \Big) - c _ {2} \omega_ {i} \text {   if   } k = 1 \\ r _ {i j k - 1} + \phi_ {i j k - 1} - c _ {1} \Big (d _ {i j} ^ {k} - d _ {i j} ^ {k - 1} + \delta_ {i j k - 1} e _ {i j k - 1} + \delta_ {i j k} e _ {i j k} \Big) \text {   if   } k \neq 1 \end{array} \right. \\ \forall i \in N \setminus \{n + 1 \}, j \in N \setminus \{0 \}, i \neq j. \end{array} \tag {21}
$$

Interpretations of the constraints are as follows. Constraints (4) and (5) require that the vehicle visit each customer exactly once. Constraints (6) enforce the temporal relationship of consecutively served customers. Constraints (7) and (8) specify the customer time windows, while constraint (9) ensures that the total route time does not exceed θ minutes. Constraints (10) and (11) mandate that only the truck stops that are located along the tour and whose out-of-route miles do not exceed e^ be chosen. Constraints (12) to (14) specify the minimum and maximum refueling quantities, while constraint (15) limits the number of refueling stops per tour. Constraints (16) and (17) impose the beginning and ending fuel levels. Constrains (18) through (21) jointly ensure that the vehicle's fuel level does not fall below μ at any point during the tour.

## Appendix B. TSPTWR sub-problems

$P _ { 1 } ,$ the TSPTW which seeks to minimize a vehicle's fuel consumption, can be written as:

$$
\underset {X _ {i j}} {\text { minimize }} \sum_ {i \in N \setminus \{n + 1 \}} \sum_ {j \in N \setminus \{0, i \}} c _ {1} d _ {i j} X _ {i j} + \sum_ {i \in N \setminus \{0, n + 1 \}} c _ {2} \omega_ {i}\tag{22}
$$

subject to: (2), (4), (5), (6), (7), (8), (9);

$$
\delta_ {i j k} = 0 \quad \forall i \in N \backslash \{n + 1 \}, j \in N \backslash \{0 \}, k \in R _ {i j}, i \neq j;\tag{23}
$$

$$
\omega_ {i} = \max \left\{A _ {i}, S _ {i} \right\} - A _ {i} \quad \forall i \in N \backslash \{0 \}.\tag{24}
$$

The above formulation is essentially the same as that used by Ohlmann and Thomas [9], except the addition of the fuel cost (consumption) associated with the waiting time. $P _ { 2 }$ can be expressed as a mixed-integer linear program similar to the original TSPTWR problem (1)–(21), except that $X _ { i j }$ variables are <sup>fi</sup>xed to some feasible values (with respect to $P _ { 1 }$ constraints); i.e.,

$$
\underset {\omega_ {i}, \delta_ {i j k}, \phi_ {i j k}} {\text { minimize }} \sum_ {i \in N \setminus \{n + 1 \}} \sum_ {j \in N \setminus \{0, i \}} \sum_ {k \in R _ {i j}} p _ {i j k} \phi_ {i j k}
$$

subject to: (3), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21);

$$
\Im = H;\tag{25}
$$

where H is an $( n + 2 ) \times ( n + 2 )$ matrix of constants $( X _ { i j }$ values) representing a feasible tour for P .

## Appendix C. Calculating σ

We compute σ by solving a mixed-integer linear program $( P _ { 3 } ) _ { }$ . Let $O _ { \mathrm { m i n } }$ be the objective-function value of the best TSPTWR solution available at the time of solving $P _ { 3 } . \ P _ { 3 }$ is written as:

maximize σ

$$
\text { subject   to }: \delta_ {y} \in \{0, 1 \} \quad \forall y \in R _ {\min};\tag{26}
$$

$$
\phi_ {y} \geq \delta_ {y} \rho \quad \forall y \in R _ {\min};\tag{27}
$$

$$
\phi_ {y} \leq \delta_ {y} (Q - \mu) \quad \forall y \in R _ {\min};\tag{28}
$$

29

$$
\delta_ {y} + \delta_ {l} \leq 2 - E _ {\mathrm{yl}} \quad \forall y \in R _ {\min}, l \in R _ {\min}, y \neq l;\tag{30}
$$

$$
\sum_ {y \in R _ {\min}} p _ {y} \phi_ {y} \leq O _ {\min};\tag{31}
$$

$$
\sum_ {y \in R _ {\min}} \phi_ {y} \geq \sigma - \beta + \varepsilon ;\tag{32}
$$

where $R _ { \operatorname* { m i n } } { = } \{ 1 , 2 , . . . , y , . . . , z \}$ is the set of z cheapest truck stops in the entire graph, $p _ { y }$ is the fuel price of truck stop $y \in R _ { \operatorname* { m i n } } ,$ σ≥0 is the fuel-consumption decision variable, and $\delta _ { y }$ and $\phi _ { y }$ are (as before) decision variables indicating the refueling location and refueling quantity. $E _ { y l }$ is a binary constant such that $E _ { y l } = 1$ if truck stops y and l are mutually exclusive, $E _ { y l } = 0$ otherwise. (We say that y and l are mutually exclusive if they cannot be used jointly because of the in-degree, out-degree, or sub-tour elimination constraints — e.g., if y is connected to arc (1, 2) and l is connected to arc (3, 2), they are mutually exclusive because of the in-degree constraint (5) for node 2.)

Notice that $P _ { 3 }$ calculates σ by assuming that a vehicle: (i) uses only the cheapest truck stop(s) that are not mutually exclusive (constraints (27) to (30)), (ii) buys as much fuel within the budget $O _ { \mathrm { m i n } }$ as possible (constraint (31)), and (iii) consumes as much fuel as possible without violating the ending fuel requirement (constraint (32)). Since these conditions jointly represent the best scenario for maximizing σ, given $O _ { \mathrm { m i n } } ,$ it follows that any TSPTW tour ℑ for which f(ℑ)>σ cannot possibly give a better (lower) refueling cost than $O _ { \mathrm { m i n } } ,$ and thus can be ignored.

## Appendix D. Supplementary data

Supplementary data to this article can be found online at http:// dx.doi.org/10.1016/j.dss.2012.09.004.

## References

[1] J.E. Bell, S.E. Grif<sup>fi</sup>s, Swarm intelligence: application of the ant colony optimization to logistics vehicle routing problems, Journal of Business Logistics 31 (2010) 157–175.

[2] O. Besbes, S. Savin, Going bunkers: the joint route selection and refueling problem, Manufacturing & Service Operations Management 11 (2009) 694–711.

[3] M.A. Figliozzi, An iterative route construction and improvement algorithm for the vehicle routing problem with soft time windows, Transportation Research Part C 18 (2010) 668–679.

[4] Y. Huang, C. Chen, Y. Fan, Multistage optimization of the supply chains of biofuels, Transportation Research Part E 46 (2010) 820–830.

[5] S. Khuller, A. Malekian, J. Mestre, To Fill or Not to Fill: The Gas Station Problem, in: Proceedings of the 15th European Symposium on Algorithms, 4698, 2008, pp. 534–545.

[6] S.H. Lin, Finding Optimal Refueling Policies in Transportation Networks, in: Proceedings of the 4th International Conference on Algorithmic Aspects in Information and Management, 5034, 2008, pp. 280–291.

[7] S.H. Lin, R. Gertsch, J.R. Russell, A linear-time algorithm for <sup>fi</sup>nding optimal vehicle refueling policies, Operations Research Letters 35 (2007) 290–296.

[8] S.M. Nourbakhsh, Y. Ouyang, Optimal fueling strategies for locomotive <sup>fl</sup>eets in railroad networks, Transportation Research Part B 44 (2010) 1104–1114.

[9] J.W. Ohlmann, B.W. Thomas, A compressed-annealing heuristic for the traveling sales man problem with time window, INFORMS Journal on Computing 19 (2007) 80–90.

[10] M.W. Savelsbergh, Local search in routing problems with time windows, Annals of Operations Research 4 (1984) 285–305.

[11] Y. Suzuki, A generic model of motor-carrier fuel optimization, Naval Research Logistics 55 (2008) 737-746

[12] Y. Suzuki, A decision support system of dynamic vehicle refueling, Decision Support Systems 46 (2009) 522–532

[13] Transport Topics, in: 405 Fleets Fail in 3rd Qtr., December 14 2009, pp. 1–27

[14] Transport Topics, in: Last Year's Diesel-Price Nightmare Teaches Fleets to Diversify Options in Buying Strategies to Cut Costs, July 27 2009, pp. 1–2.

[15] Y. Wang, C. Lin, Locating road-vehicle refueling stations, Transportation Research Part E 45 (2009) 821–829.

Yoshinori Suzuki is an Associate Professor of Supply Chain Management and Jacobson Company Fellow in Transportation and Logistics at the College of Business, Iowa State University. He holds a Bachelor of Science in Business and Economics from Sophia University (Tokyo Japan), a Master of Business Administration in Marketing from New York University, and a Doctor of Philosophy in Business Logistics from The Pennsylvania State University, He has participated in many publicly and privately funded research projects, and has published over 25 research papers in such journals as Decision Support Systems, Journal of Business Logistics, Journal of Transportation Engineering, Naval Research Logistics, and Transportation Research (A, D, E). His research interest centers on freight logistics and motor-carrier management issues
