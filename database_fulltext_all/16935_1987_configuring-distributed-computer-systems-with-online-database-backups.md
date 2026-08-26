---
otero_id: 16935
otero_key: "EMR9EUCJ"
title: "Configuring distributed computer systems with online database backups"
authors: "Hasan Pirkul"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90034-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Configuring Distributed Computer Systems with Online Database Backups

Hasan PIRKUL
The Ohio State University, Columbus, OH 43210, USA

Designers of distributed computer systems face many complex decisions in determining the system configuration. These decisions involve location of computing resources, determination of databases and allocation of one or more copies of these databases among computing facilities. This paper deals with the configuration problem for a class of organizations that are critically dependent on the availability of their computer systems, and have widely dispersed operations with localized information needs. These organizations require online back-up copies of their databases in order to continue their operations in case of failure of a computer installation or a communication channel. An integer programming formulation of the problem is presented and an effective solution procedure is developed. Computational experience with this procedure is reported.

Keywords: Designing distributed computer systems, Database allocation, Computer location, File allocation, Integer programming, Heuristics.

![](/api/attachments/EMR9EUCJ/fulltext/images/e6b404b4463d654a280b4fe323e7a90e3e855cf6b46aa39e508fb65de727f5a5.jpg)

Hasan Pirkul received the B.S. degree in Industrial Engineering from Bosphorous University, Istanbul, Turkey in 1977, the M.S. degree in Management Science and Ph.D. degree in Computers and Information Systems from the Graduate School of Management, University of Rochester in 1980 and 1983, respectively. Currently, he is an Assistant Professor of Management Information Systems at The Ohio State University. His research interests are distributed computer systems, data bases, computer networks and applications of mathematical programming. He has published articles in several journals including IIE Transactions, IEEE Transactions on Computers, Mathematical Programming, European Journal of Operational Research, Decision Sciences and Naval Research Logistics Quarterly. Dr. Pirkul is a member of TIMS, IEEE Computer Society and ACM

## 1. Introduction

Determination of system configuration is one of the problems faced by designers of distributed computer systems early in the design process. Solution of this problem involves decisions regarding the size and number of computer installations and their locations, contents of databases and allocation of these databases among computer installations. This problem is especially important for those organizations that have operations dispersed over large geographic regions and have information demand patterns that dictate the use of a particular data item mainly in and around the point where it is captured. In these organizations, distributed computer systems present significant potential telecommunication cost savings over centralized systems. Since the system configuration is one of the important factors determining the efficiency of operations, a satisfactory solution for the configuration problem is doubly important for organization where information systems represent an area of strategic importance. Many service firms like banks and insurance companies are typical examples of such organizations (Cash et al. [3]).

To date there have been only a few formal studies dealing with the configuration problem (Chen and Akoka [4], Gavish and Pirkul [14], Gavish [13], Pirkul [24]). All but one of these studies do not consider multiple database copies. The study in which multiple copies of databases are considered results in a complex mathematical programming model which can be solved only for small problem instances [4]. Most of the past research has concentrated on the related problem of allocating files and databases among the nodes of a distributed computer system (Chu [5], Casey [2], Morgan and Levin [21], Fisher and Hochbaum [11], Ramamoorthy and Wah [25], Coffman et al. [6], Lanning and Leonard [20], Pirkul [22]).

A version of the configuration problem which does not consider multiple copies of databases was addressed in a recent study [24]. In that study, the problem was formulated as a simple uncapacitated facility location problem for which a very efficient solution procedure exists [7]. In this paper we extend the results of that study to handle online backups of databases which are kept in different computer installations to provide uninterrupted service in case of failure of an installation or a communication channel. This extension represents a significant improvement in the configuration method since in the types of organizations considered here operations are critically dependent on the computer system and availability of the system is extremely important. The resulting problem no longer has the structure of the simple uncapacitated facility location problem and requires development of new solution procedures.

In section 2, we will discuss the information system structure for the class of firms under study and provide a general configuration approach. Section 3 presents an integer programming formulation of the configuration problem. The solution of the model and its use as a design tool will be discussed in section 4.

## 2. System Description and Configuration Approach

In this study, we consider organizations for which transaction processing represents a significant portion of the information system activities. Moreover, these organizations require information system support at many different locations dispersed over large geographic regions. The scope of the investigation is further limited to those organizations where data elements captured in a location are generally used to support requests from that location or locations which are geographically close to it (strong locality of reference).

We propose the following configuration approach. Service points contain special purpose and/or dump terminals along with a cluster controller with limited processing and storage capabilities. Customers are identified with the service point that they use most often. The data records associated with accounts of customers belonging to a service point form a database partition. Each database partition will be assigned to a primary and a secondary computer installation. The copy that is assigned to the installation designated as secondary will be kept current and will be used whenever the primary computer installation is not available. The long distance data communication support will be provided by a value added network (Guilbert [17], TYMNET [26]). Data communications within a metropolitan area will be supported through point to point leased lines. Therefore those bank branches located in the same metropolitan area with a computer installation will be connected to the computer with leased lines. These branches can then use the value added network port of the computer and do not need separate ports into the network.

The proposed system works in the following manner. A transaction triggered by a customer in a service node will be directed to the appropriate computer site by the cluster controller. The message will be transmitted to the computer installation and the response will be transmitted back to the cluster controller via the value added network. If the primary computer installation is down then this condition will be detected by the cluster controller and the transaction will be directed to the secondary installation. Transactions requiring updates are sent to both copies of the database simultaneously. If one of the systems is down the updates will be kept in a journal by the cluster controller and retransmitted when the system becomes available. Transactions involving more than one account, e.g., funds transfer, may result in two different computer installations being accessed. Such a transaction can effectively be treated as two transactions each accessing a single database. The cluster controller coordinates the execution of these transactions.

## 3. The Model Formulation

Configuring the system described in the previous section requires modelling decisions regarding the number of computer installations, their locations, sizes, and the allocation of database partitions of service nodes among these installations as primary and secondary sites. In real life, designers seldom have the freedom of choosing all the sites which will contain the processors to support the system. In many cases a number of installations are already present and the problem becomes one of adding one or more installations to the existing ones. This dimension of the problem is taken into account in developing the model. The following notation is be used in the presentation of the model:

I = index set of service nodes,

$K =$ index set of computer installation sites (existing and potential),

$p_{i}(\bar{p}_{i}) = \text{processing requirements, in instructions/time period, for transactions directed to primary (secondary) computer installation of service node } i,$

$b_{i}$ = secondary storage requirements, in bytes, for database partition of service node i,

$s_{ij}(\bar{s}_{ij})$ = average communication load, in bytes/time period, for query transactions from service node i to primary (secondary) database partition of service node j,

$q_{ij}$ = average communication load, in bytes/ time period, for update transactions from service node i to database partitions of service node j.

$c_{ij}$ = cost of communication via the value added network between nodes i and j (\$/byte), (equal to zero if i and j are in the same metropolitan area),

$c_{ij}''$ = cost of a point to point line from node i to computer installation j if they are in the same metropolitan area, otherwise it stands for the cost of a point to point line from node i to the nearest value added port plus the port charge (\$/time period),

$\tilde{c}_{i}$ =cost of a unit of processing power at computer installation located in node i (\$/instruction),

$$
\bar {c} _ {i}
$$

=cost of a unit of secondary storage capacity at computer installation located in node i (\$/byte),

$$
c _ {i} ^ {\prime}
$$

=cost of a unit of telecommunication capacity at computer installation located in node i (\$/byte),

$v_{j} =$ set up costs associated with opening a new computer installation,

$$
x _ {i j}
$$

$= \left\{ \begin{array}{ll}1 & \text{if computer installation at site } j \text{ is}\\ & \text{designated as the primary installation for the database partition of}\\ & \text{service node } i,\\ 0 & \text{otherwise.} \end{array} \right.$

$z_{ij}$ $= \left\{ \begin{array}{ll}1 & \text{if computer installation at site } j \text{ is}\\ & \text{designated as the secondary in}\\ & \text{stallation for the database parti}\\ & \text{tion of service node } i,\\ 0 & \text{otherwise.} \end{array} \right.$

$$
y _ {j} \quad = \left\{ \begin{array}{l l} 1 & \text { if   a   computer   installation   is } \\ & \text { established   in   node } j, \\ 0 & \text { otherwise. } \end{array} \right.
$$

The model is built on the assumption that we are dealing with totally modular computers and that computing, telecommunication and secondary storage capacities can be purchased in units. This approximation is not very far from reality. Many vendors provide computers with a wide range of CPU power. Furthermore it is possible to configure systems with different levels of secondary storage capacities. Therefore various computer configurations resulting from the use of the model could indeed be implemented. It is also assumed that existing equipment can be transported to a new location if it would be underutilized in the new configuration. The model is stated as:

## Problem-IP

$$
\begin{array}{l l} \min & \sum_ {i \in I} \sum_ {j \in K} x _ {i j} \left(c _ {i j} ^ {\prime \prime} + \sum_ {l \in I} \left(s _ {l i} + q _ {l i}\right) c _ {l j}\right) \\ & + \sum_ {i \in I} \sum_ {j \in K} z _ {i j} \left(c _ {i j} ^ {\prime \prime} + \sum_ {l \in I} \left(\bar {s} _ {l i} + q _ {l i}\right) c _ {l j}\right) \\ & + \sum_ {i \in I} \sum_ {j \in K} x _ {i j} \left(b _ {i} \bar {c} _ {j} + p _ {i} \tilde {c} _ {j} + \sum_ {l \in I} \left(s _ {l i} + q _ {l i}\right) c _ {j} ^ {\prime}\right) \\ & + \sum_ {i \in I} \sum_ {j \in K} z _ {i j} \left(b _ {i} \bar {c} _ {j} + \bar {p} _ {i} \tilde {c} _ {j} + \sum_ {l \in I} \left(\bar {s} _ {l i} + q _ {l i}\right) c _ {j} ^ {\prime}\right) + \sum_ {j \in K} v _ {j} y _ {j} \end{array} \tag {1}
$$

subject to

$$
\sum_ {j \in K} x _ {i j} = 1 \quad \forall i \in I,\tag{2}
$$

$$
\sum_ {j \in K} z _ {i j} = 1 \quad \forall i \in I,\tag{3}
$$

$$
x _ {i j} + z _ {i j} \leq y _ {j} \quad \forall i \in I, j \in K,\tag{4}
$$

$$
x _ {i j}, z _ {i j} \in (0, 1), \quad \forall i \in I, j \in K,
$$

$$
y _ {j} \in (0, 1) \quad \forall j \in K.\tag{5}
$$

The first two terms in the objective function capture the telecommunication costs. These costs include point to point leased line costs, network port costs and volume dependent communication costs charged by the value added network [26]. It is assumed that if a service node is within the same metropolitan area with a computer: installation a local leased line is used to connect the branch to the computer installation. In this case the node can use the value added network port of the installation and does not need a dedicated port. Those service nodes which are not in the same metropolitan area use dedicated ports. In this case the model captures the port cost and the cost of a local leased line into the port. The third and fourth terms represent cost of hardware. The fifth term represents set up costs associated with new installations. The existing installations are handled by setting the associated set up costs equal to zero. Set up costs might include software, site preparation and other costs in the form of either rents and/or discounted capital costs. The objective function value of the model has to be adjusted to account for the existing equipment. Since the existing equipment is assumed to be transportable, this can easily be accomplished by deducting value of the existing equipment from the objective function value. The objective function components can be rearranged in the following form to better illustrate the structure of the problem:

$$
\begin{array}{l l} \min & \sum_ {i \in I} \sum_ {j \in J} \hat {c} _ {i j} x _ {i j} + \sum_ {i \in I} \sum_ {j \in J} \bar {\overline {{c}}} _ {i j} z _ {i j} \\ & + \sum_ {j \in J} v _ {j} y _ {j}, \quad \text { where } \end{array}\tag{6}
$$

$$
\begin{array}{r l} \hat {c} _ {i j} & = \sum_ {l \in I} (s _ {l i} + q _ {l i}) c _ {l j} + c _ {i j} ^ {\prime \prime} + b _ {i} \bar {c} _ {j} \\ & \quad + p _ {i} \tilde {c} _ {j} + \sum_ {l \in I} (s _ {l i} + q _ {l i}) c _ {j} ^ {\prime}, \\ \bar {\bar {c}} _ {i j} & = \sum_ {l \in I} (\bar {s} _ {l i} + q _ {l i}) c _ {l j} + c _ {i j} ^ {\prime \prime} \\ & \quad + b _ {i} \bar {c} _ {j} + \bar {p} _ {i} \tilde {c} _ {j} + \sum_ {l \in I} (\bar {s} _ {l i} + q _ {l i}) c _ {j} ^ {\prime}. \end{array}
$$

Constraint set (2) and (3) ensure that the database partition of each service node gets assigned to two different computer installations designated as primary and secondary installations. Constraint set (4) states that there should be a computer installation at every node to which one or more database partitions are assigned. It also ensures that a computer installation is not designated as both primary and secondary for the same service node. Integrality conditions are enforced with constraint set (5).

Note that the problem could have been formulated with various capacity constraints as in [14]. One advantage of problem-IP over a formulation that uses capacity constraints is that, in such a formulation the size and configuration of the computer installations are predetermined. As a result some computers end up being underutilized or worse yet within an installation one or more of the resources are underutilized due to another resource creating a bottle neck. The present formulation not only avoids these problems but also has the added advantage of simplicity. On the other hand, it captures only rough approximations of computer installation costs. This is mainly due to the assumption about linear capacity expansion costs. We know that in real life these costs are nonlinear, e.g., CPU power or secondary storage capacity is purchased in certain integral sizes not in units. Furthermore, the model is only applicable when long distance communication does not involve fixed charges on the links. Today the tariffs of value added network companies satisfy this condition. But if these tariffs were to change or if we wanted to use dedicated long distance lines the model has to be modified to address additional questions like, which long distance links to select and how the required internode traffic should be routed on this selected network.

## 4. Solution Procedures

The model presented in the previous section constitutes a considerable size zero-one integer programming problem. An instance of the model with 100 service points and 20 existing and potential installations will have over 4000 integer variables and 2200 constraints. Furthermore problem-IP is NP-Complete. This can be seen by dropping secondary computer installation assignment variables from the model ( $z_{ij}$ ). The remaining problem is an uncapacitated facility location problem which is known to be NP-complete [12]. Despite its size and computational complexity the model displays a special structure which can be exploited to develop efficient solution procedures. In section 4.1 we present a Lagrangian relaxation of problem-IP. In section 4.2 a heuristic solution method is developed using the information provided by the Lagrangian relaxation. Computational results are presented in section 4.3.

## 4.1. A Lagrangian Relaxation of Problem-IP

The Lagrangian relaxation scheme has been successfully applied to many combinatorial optimization problems during the last decade. The use of generalized Lagrange multipliers was first suggested by Everett [8]. The successful application of this relaxation to the travelling salesman problem by Held and Karp [18], led to its use in a variety of other problems. Capacitated facility location problem [16]; distributed computer system design problems [13], [14], [22] and multiple item inventory replenishment problem [23] are only a few of the problems to which this relaxation was applied. We consider the following Lagrangian relaxation of problem-IP.

Problem-L

$$
\begin{array}{r l} Z _ {L} (\lambda , \mu) = & \min \left\{\sum_ {i \in I} \sum_ {j \in K} \hat {c} _ {i j} x _ {i j} + \sum_ {i \in I} \sum_ {j \in K} \bar {\bar {c}} _ {i j} z _ {i j} \right. \\ & \left. + \sum_ {j \in K} v _ {j} y _ {j} + \sum_ {i \in I} \lambda_ {i} \left(\sum_ {j \in K} x _ {i j} - 1\right) \right. \\ & \left. + \sum_ {i \in I} \mu_ {i} \left(\sum_ {j \in K} z _ {i j} - 1\right) \right\} \end{array} \tag {7}
$$

subject to constraint sets (4) and (5).

Problem-L can be decomposed into the following subproblems: For every computer site $j \in K$ ,

$$
\min \left\{\sum_ {i \in I} x _ {i j} \left(\hat {c} _ {i j} + \lambda_ {i}\right) + \sum_ {i \in I} z _ {i j} \left(\bar {\bar {c}} _ {i j} + \mu_ {i}\right) + v _ {j} y _ {j} \right\}\tag{8}
$$

subject to

$$
x _ {i j} + z _ {i j} - y _ {j} \leq 0 \quad \forall i \in I,\tag{9}
$$

$$
x _ {i j}, z _ {i j} \in \{0, 1 \} \quad \forall i \in I, y _ {j} \in (0, 1).\tag{10}
$$

In each subproblem $y_j$ is equal to either 0 or 1. If $y_j$ is equal to 0 then all $x_{ij}$ and $z_{ij}$ are also equal to 0 due to constraint set (10). If $y_j$ is equal to 1 then for every service node $i'$ , either $x_{i'j}$ or $z_{i'j}$ can be set equal to 1. If $\hat{c}_{i'j} + \lambda_{i'} \leq \bar{\bar{c}}_{i'j} + \mu_{i'}$ and $\hat{c}_{i'j} + \lambda_{i'}$ is negative $x_{i'j}$ is set equal to 1 and $z_{i'j}$ is set equal to 0, if $\bar{\bar{c}}_{i'j} + \mu_{i'} < c_{i'j} + \lambda_{i'}$ and $\bar{\bar{c}}_{i'j} + \mu_{i'}$ is negative $z_{i'j}$ is set equal to 1 and $x_{i'j}$ is set equal to 0, otherwise both variables are set equal to 0. If the solution value for this problem is negative and its absolute value is greater than $v_j$ then $y_{j}$ is set equal to 1 and the corresponding solution is kept. Otherwise the solution of the subproblem is taken to be the zero vector.

Other Lagrangian relaxations of the problem may also be considered. In an alternative relaxation we can dualize constraint set (4). The resulting Lagrangian problem is decomposable over index set I and results in $|I|+1$ subproblems. Each of the first $|I|$ subproblems are solved by searching two vectors of size $|K|$ for their minimum valued elements. The solution of the last subproblem involves $|K|$ comparisons. Therefore the relaxed problem can be solved in polynomial time. Both this relaxation and problem-L possess the integrality property [15], indicating that the lower bounds derived from these relaxations can be at best equal to the linear programming bound. Despite this point, there are two advantages to using a Lagrangian relaxation approach. First, a very good lower bound can be identified fairly quickly. Secondly, a feasible solution is generated in every iteration of the subgradient optimization procedure that is used in solving the Lagrangian problem. As a result, very good feasible solution values are generated simultaneously with the calculation of a lower bound.

The best lower bound using problem-L is obtained by calculating,

$$
Z _ {L} (\lambda^ {*}, \mu^ {*}) = \max _ {\lambda , \mu} \left\{Z _ {L} (\lambda , \mu) \right\}.
$$

Excluding a few special cases, finding optimal multipliers is known to be a very difficult task. In practice, a good but not necessarily optimal set of multipliers can be found by using either a sub-gradient optimization method or various multiplier adjustment methods known as ascent (descent) methods [1].

In this study we employ the subgradient optimization algorithm. The subgradient method is an adaptation of the gradient method in which subgradients replace gradients. Given an initial multiplier vector $(\lambda,\mu)^{0}$ a sequence of multipliers are generated using the following rule:

$$
(\lambda , \mu) ^ {k + 1} = (\lambda , \mu) ^ {k} + t _ {k} (A (x, z, y) ^ {k} - b),
$$

where $(x^{k}, z^{k}, y^{k})$ is the solution vector corresponding to $Z_{L}((\lambda, \mu)^{k})$ , $t_{k}$ is a positive scalar step size, A is the matrix defined by constraint sets (2) and (3) and b is the corresponding right hand side vector. We use the following step size that has been frequently used in the past [10]:

$$
t _ {k} = d _ {k} \left(\bar {Z} - Z _ {L} \left(\left(\lambda , \mu\right) ^ {k}\right)\right) / \| A (x, z, y) ^ {k} - b \| ^ {2},
$$

where $\overline{Z}$ is the best known feasible solution value and $d_{k}$ is a scalar satisfying $0 \leq d_{k} \leq 2$ . This scalar is set equal to 2 at the beginning of the algorithm and is halved whenever the bound does not improve in 15 consecutive iterations. It should be pointed out that this is only a heuristic and that it is not guaranteed to give the optimal Lagrangian dual solution. The algorithm is terminated after 500 iterations unless the gap between the best feasible solution and the lower bound becomes smaller than .01 percent of the lower bound before this cut off point is reached. For all practical purposes when this condition is met the solution can be considered optimal since the gap between the optimal solution and the feasible solution at hand will be guaranteed to be less than .01 percent of the optimal solution.

## 4.2. Solution Procedure

In this section a heuristic solution procedure is developed in conjunction with the Lagrangian relaxation presented in the previous section. This procedure generates a feasible solution at every iteration of the subgradient optimization algorithm. Note that in the solution to problem-L there may be service points for which no computer installation is designated as primary (secondary) installation. It is also possible that multiple installations are designated as primary (secondary) installation for a single service node. If we define $(\tilde{x}, \tilde{z}, \tilde{y})$ as a solution to problem-L and $(\bar{x}, \bar{z}, \bar{y})$ as the current best incumbent solution, then the solution procedure can be stated as

## Procedure-Heur

I Initialize sets S and $S_{t}$ to contain all sites selected by the solution to problem-L as determined by $\tilde{y}$ . Let $y = \tilde{y}$ .

II Initialize $(x, z)$ as the zero vector. For every service point i determine

(1) the best $(k_{1})$ and second best $(k_{2})$ primary computer installation as $\hat{c}_{ik_1} = \min_{j\in S}\{\hat{c}_{ij}\}$ , $\hat{c}_{ik_2} = \min_{j\in S - \{k_1\}}\{\hat{c}_{ij}\}$ , (2) the best $(l_{1})$ and second best $(l_{2})$ secondary computer installation as $\overline{\bar{c}}_{il_1} = \min_{j\in S}\{\overline{\bar{c}}_{ij}\}, \overline{\bar{c}}_{il_2} = \min_{j\in S - \{l_1\}}\{\overline{\bar{c}}_{ij}\}$ . If $k_{1}\neq l_{1}$ then let $x_{ik_1} = 1$ and $z_{il_1} = 1$ , other wise calculate $\delta_{1}$ and $\delta_{2}$ as $\delta_{1} = \hat{c}_{ik_{2}} - \hat{c}_{ik_{1}}$ , $\delta_{2} = \overline{\bar{c}}_{il_{2}} - \overline{\bar{c}}_{ll_{1}}$ . If $\delta_{2} \leq \delta_{1}$ let $x_{ik_{1}} = 1$ and $z_{il_{2}} = 1$ , otherwise let $x_{ik_{2}} = 1$ and $z_{il_{1}} = 1$ . If there are computer installations that are in set $S$ and are not assigned a service node in the current feasible solution $(x, z, y)$ , modify the current solution by setting location variables $(y_{j})$ corresponding to these installations equal to zero. If the current solution $(x, z, y)$ is better than the incumbent solution $(\bar{x}, \bar{z}, \bar{y})$ , update the incumbent.

III For every site $j \in S_t$ repeat the following steps: (i) Let set $S = S_t \cup \{j\}$ .

(ii) Define vector $y$ by letting $y_j = 1$ for all $j \in S$ and setting all other variables equal to zero.

(iii) Use the process outlined in step II to create a new feasible solution and update the incumbent if necessary.

IV Redefine set $S_{t}$ to contain those installations selected in $\bar{y}$ . For every site $j \in S_{t}$ repeat the following steps:

(i) Let set $S = S_{t} - \{j\}$ .

(ii) Define vector $y$ by letting $y_j = 1$ for all $j \in S$ and setting all other variables equal to zero.

(iii) Use the process outlined in step II to create a new feasible solution and update the incumbent if necessary.

This procedure generates a feasible solution by allocating service points among the computer installations selected in the solution to the Lagrangian problem (captured in set $S_t$ ). Later, in step III a site $j$ which was not selected (not in $S_t$ ) is added to those sites that were selected (forming set $S$ ), and a new feasible solution is generated by allocating the service points among these sites. This process is repeated for all sites that were not selected. Step III results in $|J| - |S_t|$ new feasible solutions. In step IV set $S_t$ is redefined to contain those sites that are selected in the incumbent feasible solution. This time we consider deleting a member of the set $S_t$ and generating a new feasible solution. Then that particular member is restored and a new one is deleted. This process is repeated until all members of $S_t$ are considered. At this step a total of $|S_t|$ feasible solutions are obtained. Steps III and IV resemble the celebrated ADD [19] and DROP [9] algorithms. The major difference between this algorithm and the classical ADD/DROP algorithms is that this one starts out with a number of selected sites and considers adding and/or dropping a single site as opposed to starting with no sites selected or all sites selected and adding or dropping multiple sites as done in the ADD and DROP algorithms respectively. Since Procedure-Heur does not modify the starting solution significantly, its success is strongly dependent on the ability of the Lagrangian relaxation to predict the sites that should receive the computing facilities. Computational experiments show that the relaxation is indeed very successful in this role.

## 4.3. Computational Results

A set of computational experiments were designed to test the performance of procedure-Heur. The subgradient optimization algorithm incorporating Procedure-Heur was coded in FORTRAN IV and experiments were performed using a PRIME 9955 minicomputer. Computing times reported throughout the paper are in CPU seconds of this computer. The problem data used in these experiments were randomly generated. Data points representing service nodes and computer installation sites were drawn from a uniform distribution over a rectangle with sides 50 and 100. Cost coefficients $\hat{c}_{ij}$ were determined by multiplying euclidean distances between service nodes and computer installation sites with a random number from a uniform distribution between 10 and 25. This cost coefficient captures communication costs resulting from queries and updates to the database partition of service node $i$ assigned to computer installation at site $j$ . Due to locality of reference most of the load is from locations geographically close to node $i$ . Therefore it is reasonable to expect this cost to be correlated to the distance between node $i$ and site $j$ . Cost coefficients $\bar{\bar{c}}_{ij}$ were determined in a similar fashion using a uniform distribution between 2 and 4. The fixed set up costs $(v_j)$ were drawn from a uniform distribution between $l$ and $u$ .

In the first experiment, a total of 300 problems were solved using Procedure-Heur. These problems were arranged into 30 groups where each group had 10 problems. The results of these experiments are reported in table 1. As mentioned before, a cut off rule of terminating the algorithm whenever the gap between the lower bound and the feasible solution value becomes less than 0.01 percent of the lower bound was used in the procedure. In all but 18 of the problems the procedure was terminated by this cut off rule. The problems with gaps larger than 0.01 percent of the lower bound are indicated in the table and the corresponding gaps are reported. Even in these problems the gaps are insignificant. For each problem group the maximum, minimum and mean computation times are reported. These times are reasonable for the problem sizes solved (up to 12020 variables and 6600 constraints). This is especially true if we keep in mind that these times are reported in CPU seconds of a minicomputer.

Problem structure is strongly effected by the relative levels of fixed set up costs and assignment costs. We captured a range of problems by using different levels of fixed set up costs. This is illustrated by the average (over all $(i, j)$ pairs) fixed to variable cost ratios $(RI)$ reported for each problem structure. In problems where set up costs are low, a relatively high number of installations are opened. On the other hand, as fixed set up costs are increased fewer installations are opened. This can be clearly seen in table 1 where the average number of installations that are opened is reported for each group. It is interesting to note that the ratios $(R2)$ of fixed costs to variable costs in problem solutions do not change as dramatically as the average fixed to variable cost ratios $(RI)$ used in generating the problems. This is due to the fact that when fixed set up costs associated with opening new computer installations become high, the model opens fewer installations and compensates by making them larger. Since the computer purchase costs are mainly captured in variable costs, the result is only a modest increase in the overall fixed to variable cost ratio. The solution procedure was found to be effective in solving problems with all five set up cost levels.

Problems reported in table 1 were generated by setting assignment costs equal to a multiple of the euclidian distances between service points and computer installations. In reality assignment costs contain a component which is not related to the location of the service point with respect to the computer installation but to the size of the bank branch (cost of acquiring computer capacity). Furthermore, in these problems the load placed on the backup computer by a service point was insignificant compared to the load placed on the primary computer. If updates are a significant part of the transaction load the backup installations will also be utilized heavily. A second experiment was designed to capture these points. As before data points representing service nodes and computer installation sites were drawn from a uniform distribution over a rectangle with sides 50 and 100. Cost coefficients were calculated using the follow-

Table 1
Performance of the solution procedure.

<table><tr><td colspan="4">Problem Id.</td><td colspan="3">Solution Time (CPU sec.)</td><td rowspan="2"># of Cases  $Gap^b$ &gt;0.01%</td><td rowspan="2">Max. Gap as % of L. Bound</td><td rowspan="2"> $R2^c$ </td><td rowspan="2">Number of Facilities</td></tr><tr><td>(l,u)</td><td> $RI^a$ </td><td>M</td><td>N</td><td>Min.</td><td>Mean</td><td>Max.</td></tr><tr><td rowspan="6">(1000, 1500)</td><td rowspan="6">3.2</td><td rowspan="3">10</td><td>100</td><td>2.92</td><td>7.04</td><td>10.10</td><td></td><td></td><td>0.33</td><td>6.7</td></tr><tr><td>200</td><td>8.35</td><td>28.36</td><td>60.38</td><td></td><td></td><td>0.22</td><td>8.2</td></tr><tr><td>300</td><td>8.39</td><td>10.78</td><td>12.16</td><td></td><td></td><td>0.15</td><td>9.0</td></tr><tr><td rowspan="3">20</td><td>100</td><td>9.84</td><td>17.82</td><td>29.57</td><td></td><td></td><td>0.43</td><td>7.7</td></tr><tr><td>200</td><td>14.21</td><td>67.45</td><td>132.28</td><td>3</td><td>0.14</td><td>0.33</td><td>9.9</td></tr><tr><td>300</td><td>40.75</td><td>66.85</td><td>202.65</td><td>1</td><td>0.01</td><td>0.28</td><td>12.1</td></tr><tr><td rowspan="6">(2000, 3000)</td><td rowspan="6">6.3</td><td rowspan="3">10</td><td>100</td><td>4.88</td><td>10.65</td><td>16.20</td><td></td><td></td><td>0.41</td><td>4.9</td></tr><tr><td>200</td><td>27.40</td><td>50.74</td><td>70.71</td><td>1</td><td>0.02</td><td>0.37</td><td>6.0</td></tr><tr><td>300</td><td>9.85</td><td>16.25</td><td>27.81</td><td></td><td></td><td>0.28</td><td>6.4</td></tr><tr><td rowspan="3">20</td><td>100</td><td>19.44</td><td>27.56</td><td>41.06</td><td></td><td></td><td>0.49</td><td>4.0</td></tr><tr><td>200</td><td>18.79</td><td>43.40</td><td>57.06</td><td></td><td></td><td>0.43</td><td>6.0</td></tr><tr><td>300</td><td>36.12</td><td>78.71</td><td>201.24</td><td>1</td><td>0.09</td><td>0.45</td><td>8.0</td></tr><tr><td rowspan="6">(3000, 4000)</td><td rowspan="6">8.8</td><td rowspan="3">10</td><td>100</td><td>4.69</td><td>7.14</td><td>10.85</td><td></td><td></td><td>0.45</td><td>2.8</td></tr><tr><td>200</td><td>18.71</td><td>27.23</td><td>54.83</td><td></td><td></td><td>0.43</td><td>3.3</td></tr><tr><td>300</td><td>17.56</td><td>25.03</td><td>38.21</td><td></td><td></td><td>0.37</td><td>4.0</td></tr><tr><td rowspan="3">20</td><td>100</td><td>4.04</td><td>25.67</td><td>69.51</td><td>1</td><td>0.26</td><td>0.45</td><td>2.7</td></tr><tr><td>200</td><td>36.60</td><td>46.31</td><td>55.51</td><td></td><td></td><td>0.49</td><td>3.6</td></tr><tr><td>300</td><td>64.43</td><td>109.58</td><td>203.10</td><td>2</td><td>0.44</td><td>0.52</td><td>4.8</td></tr><tr><td rowspan="6">(10000, 15000)</td><td rowspan="6">31.5</td><td rowspan="2">10</td><td>100</td><td>8.36</td><td>17.34</td><td>24.56</td><td></td><td></td><td>0.59</td><td>2.8</td></tr><tr><td>200</td><td>30.11</td><td>48.55</td><td>68.49</td><td></td><td></td><td>0.61</td><td>4.0</td></tr><tr><td>-</td><td>300</td><td>61.96</td><td>89.27</td><td>101.72</td><td>1</td><td>0.02</td><td>0.43</td><td>4.0</td></tr><tr><td rowspan="3">20</td><td>100</td><td>10.79</td><td>19.36</td><td>40.84</td><td>2</td><td>0.05</td><td>0.67</td><td>2.8</td></tr><tr><td>200</td><td>38.94</td><td>94.18</td><td>175.65</td><td>3</td><td>0.57</td><td>0.49</td><td>3.7</td></tr><tr><td>300</td><td>81.15</td><td>162.37</td><td>275.53</td><td>3</td><td>0.37</td><td>0.52</td><td>4.3</td></tr><tr><td rowspan="6">(50000, 60000)</td><td rowspan="6">138.5</td><td rowspan="3">10</td><td>100</td><td>3.83</td><td>5.21</td><td>13.86</td><td></td><td></td><td>1.78</td><td>2.0</td></tr><tr><td>200</td><td>4.63</td><td>8.14</td><td>16.32</td><td></td><td></td><td>1.04</td><td>2.0</td></tr><tr><td>300</td><td>14.76</td><td>23.77</td><td>65.61</td><td></td><td></td><td>0.70</td><td>2.0</td></tr><tr><td rowspan="3">20</td><td>100</td><td>7.30</td><td>13.84</td><td>19.77</td><td></td><td></td><td>1.94</td><td>2.0</td></tr><tr><td>200</td><td>10.65</td><td>16.43</td><td>24.83</td><td></td><td></td><td>1.08</td><td>2.0</td></tr><tr><td>300</td><td>32.73</td><td>53.26</td><td>84.11</td><td></td><td></td><td>0.72</td><td>2.0</td></tr></table>

$^{a}$ R1 = average (over all $(i, j)$ pairs) fixed to variable cost ratio.  
$^{b}$ Number of problems where the gap between the feasible solution value and the lower bound is greater than 0.01 percent of the lower bound.  
$^{c}$ R2 = the ratio of total fixed cost to total variable cost in problem solution (average over all problems).  
ing formulas:

$$
\hat {c} _ {i j} = d _ {i j} * 1 0 + (1 0 0 + r _ {i} * 1 0 0),
$$

$$
\bar {\bar {c}} _ {i j} = 1 / 2 * \hat {c} _ {i j},
$$

where $d_{ij}$ was the euclidian distance between i and j and $r_{i}$ is a random number from a uniform distribution between 0 and 1 that is used to capture the size of service point i. In these formulas the load on the backup computer is set equal to

half the load on the primary computer. Also the assignments costs are set up so that operationally half of the cost is related to the distance and the other half is related to the size of the service point. As before fixed set up costs $(v_{j})$ were drawn from a uniform distribution between l and u and these parameters were varied to generate problems with different degrees of trade-off between fixed set up costs and cost related to assignment of service points to computer installations. A total of 90 problems arranged in 9 groups of 10 problems each were solved. The results are reported in table 2. These results are similar to the results reported for the previous experiment. Solutions times are somewhat lower than times reported for comparable size problems in table 1. This is mainly due to the fact that the results reported in table 2 are for a cut off rule of 0.1% of the feasible solution value rather than 0.01% used in the previous experiment. This new cut off rule was used to illustrate the fact that we can cut down the computation time significantly and not affect the solution quality. It was observed that beyond a certain point in the subgradient optimization procedure the feasible solution did not improve. The gap was reduced only because of improvements in the lower bound. To illustrate this point problems were solved using both cut off rules and it was observed that there was indeed no difference in the feasible solution values but the time is cut nearly in half with the new rule. Furthermore when the procedure was used with .01% rule in all but 3 cases the gap between the bound and the feasible solution was less than 0.01% of the feasible solution value. In those three cases the gaps were 0.04%, 0.07% and 0.09% respectively. Fixed set up costs upto 10000 were considered. The solution quality does not seem to be related to the set up cost level within the range considered in this experiment. On the other hand the solution structure is affected. As before with increasing fixed costs number of computer installations declines reflecting the domination of fixed set up costs over assignment costs.

The model presented in this paper can be used as a tool for designing distributed systems. Computational results indicate that the proposed solution procedure is adequate for solving problems having the structures tested in the experiments reported in this section. One should keep in mind that this is a high level model. Therefore it is likely that the final design will not be provided by the model but will be decided upon by the designer considering the information provided by the model along with other aspects of the problem that are not captured by the model. System designers can rely on this model to provide them with initial configurations which can be used as starting points in the detailed design process. They can also use this model to evaluate the implications of various design decisions; the model can be solved repeatedly with different parameters and the sensitivity of the solution to changes in these parameters can be investigated, e.g., if management strongly favors a city to establish a computer installation and if that city is not picked by the optimal solution, then we can solve the model as if we already have a computer installation there to find out the cost increase over the optimal solution. If the cost increase is low then that location can be used without further consideration. If the cost increase is high it does not eliminate the location automatically, the management should be made aware of the extra cost and might still decide to have a computer installation there.

Performance of the solution procedure with 0.1% cut off rule.

<table><tr><td colspan="4">Problem Id.</td><td colspan="3">Solution Time (CPU Sec.)</td><td rowspan="2"># of Cases  $Gap^b$  &gt;0.01%</td><td rowspan="2">Max. Gap as % of L. Bound</td><td rowspan="2"> $R2^c$ </td><td rowspan="2">Number of Facilities</td></tr><tr><td>(l,u)</td><td> $RI^a$ </td><td>M</td><td>N</td><td>Min.</td><td>Mean</td><td>Max.</td></tr><tr><td rowspan="3">(2000,3000)</td><td rowspan="3">6.1</td><td rowspan="3">20</td><td>100</td><td>11.21</td><td>18.37</td><td>32.08</td><td></td><td></td><td>0.29</td><td>4.3</td></tr><tr><td>200</td><td>36.27</td><td>28.36</td><td>63.42</td><td>1</td><td>0.09</td><td>0.25</td><td>6.2</td></tr><tr><td>300</td><td>60.21</td><td>74.85</td><td>96.59</td><td></td><td></td><td>0.24</td><td>8.2</td></tr><tr><td rowspan="3">(5000,6000)</td><td rowspan="3">13.4</td><td rowspan="3">20</td><td>100</td><td>14.62</td><td>17.38</td><td>21.61</td><td>1</td><td>0.04</td><td>0.32</td><td>2.8</td></tr><tr><td>200</td><td>31.13</td><td>52.63</td><td>80.62</td><td></td><td></td><td>0.28</td><td>4.0</td></tr><tr><td>300</td><td>49.54</td><td>82.76</td><td>101.11</td><td></td><td></td><td>0.28</td><td>5.3</td></tr><tr><td rowspan="3">(9000,10000)</td><td rowspan="3">23.2</td><td rowspan="3">20</td><td>100</td><td>7.35</td><td>11.48</td><td>17.82</td><td></td><td></td><td>0.36</td><td>2.0</td></tr><tr><td>200</td><td>23.28</td><td>31.84</td><td>42.69</td><td></td><td></td><td>0.32</td><td>3.0</td></tr><tr><td>300</td><td>63.37</td><td>72.43</td><td>84.12</td><td>1</td><td>0.07</td><td>0.29</td><td>3.8</td></tr></table>

a $RI = \text{average (over all } (i, j) \text{ pairs)}$ fixed to variable cost ratio.

## 5. Summary

In this paper we have studied the problem of configuring distributed computer systems with online database backups. This problem is faced by most of the service organizations operating over large geographical areas. An integer programming formulation of the problem was presented and an efficient solution procedure was developed. This procedure was tested on a large number of problems and shown to be capable of solving realistic size problems. Potential uses of the model were discussed. Copies of the solution procedure reported in this paper can be obtained from the author.

## References

[1] Bazaara, M.S. and J.J. Goode, A. Survey of Various Tactics for Generating Lagrangian Multipliers in the Context of Lagrangian Duality, European Journal of Operational Research 3 (1979) 322–338.

[2] Casey, R.G., Allocation of Copies of a File in an Information Network, AFIPS Conference Proceedings 40 (1972) SJCC, 617–625.

[3] Cash, J.I.Jr., F.W. McFarlan and J.L. McKenney, Corporate Information Systems Management: Text and Cases, Irwin, Homewood, IL (1983).

[4] Chen, P. and J. Akoka, Optimal Design of Distributed Information Systems, IEEE Trans. Comput. C-29, No. 12 (1980) 1068–1080.

[5] Chu, W.W. Optimal File Allocation in Multiple Computer System, IEEE Trans. Comput. C-18 (1969) 885–889.

[6] Coffman, E.G.Jr., E. Gelenbe, and B. Plateau, Optimization of the Number of Copies in a Distributed Database, IEEE Trans. Software Eng. SE-7, No. 1 (1981) 78–84.

[7] Erlenkotter, D., A Dual Based Procedure for Uncapacitated Facility Location, Operations Research 26, No. 1 (1978) 992–1009.

[8] Everett, H., Generalized Lagrange Multipliers Method for Solving Problems of Optimum Allocation of Resources, Operations Research 11 (1963) 399–417.

[9] Feldman, E., F.A. Lehrer and T.L. Ray, Warehouse Location Under Continuous Economies of Scale, Management Science 12 (1966) 670–684.

[10] Fisher, M.L., Lagrangian Relaxation Method for Solving Integer Programming Problems, Management Science 27, No. 1 (1981) 1–18.

[11] Fisher, M.L. and D.S. Hochbaum, Database Location in Computer Networks, J. Ass. Comput. Mach. 27, No. 4 (1980) 718–735.

[12] Garey, M.R., and D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, Freeman, San Francisco, CA (1979).

[13] Gavish, B., Models for Configuring Large Scale Distributed Computing Systems, Bell Systems Technical Journal 64, No. 2 (1985) 491–532.

[14] Gavish, B. and H. Pirkul, Computer and Database Location in Distributed Computer Systems, IEEE Trans. Comput. C-35, No. 7 (1986) 583–590.

[15] Geoffrion, A.M., Lagrangian Relaxation and its Uses in Integer Programming, Mathematical Programming Study 2 (1974) 82–114.

[16] Geoffrion, A.M. and R. McBride, Lagrangian Relaxation Applied to Capacitated Facility Location Problems, AIIE Transactions 10 (1978) 40–47.

[17] Guilbert, J.F., TRANSPAC: The Impact of a Value Added Network, Teleinformatics 79, Boutmy/Danthine, eds., IFIP, North Holland Publishing Company, Amsterdam (1979).

[18] Held, M. and R.M. Karp, The Travelling Salesman Problem and Minimum Spanning Trees, Operations Research 18 (1970) 1138–162.

[19] Kuehn, A.A. and M.J. Hamburger, A. Heuristic Program for Locating Warehouses, Management Science 9 (1963) 643–666.

[20] Lanning, L.J. and M.S. Leonard, File Allocation in a Distributed Computer Communication Network, IEEE Trans. Comput. C-32, No. 3 (1983) 232–244.

[21] Morgan, H.L. and K.D. Levin, Optimal Program and Data Locations in Computer Networks, Commun. Ass. Comput. Mach. 20, No. 5 (1977) 315–321.

[22] Pirkul, H., An Integer Programming Model For the Allocation of Databases in a Distributed Computer System, European Journal of Operational Research 26 (1986) 401–411.

[23], Pirkul, H. and O.A. Aras, Capacitated Multiple Item: Ordering Problem with Quantity Discounts, IIE Transactions 17 (1985) 206–211.

[24] Pirkul, H., Configuring Distributed Computer Systems, International Journal on Policy and Information 10, No. 1 (1986).

[25] Ramamoorthy, C.V. and B.W. Wah, The Isomorphism of Simple File Allocation, IEEE Trans. Comput. C-32 (1983) 221–231.

[26] TYMNET The Intelligent Network People, Tymnet, Inc., Great Lakes District, Pittsburgh, PA.
