---
otero_id: 19143
otero_key: "Y64B8WWP"
title: "Allocating data files over a wide area network: Goal setting and compromise design"
authors: "Heeseok Lee; Yong Shi; Justin Stolen"
year: "1994"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)90056-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Allocating data files over a wide area network: Goal setting and compromise design

Heeseok Lee, Yong Shi and Justin Stolen

University of Nebraska at Omaha, Omaha, NE, USA

The problem of allocating data files over geographically dispersed sites connected by data communication networks has been extensively studied in the literature. Determining file locations in a distributed information system typically requires trade-offs among multiple design objectives, some in conflict. This paper proposes a method to determine a compromise design for file allocation via a wide area telecommunication network. This compromise approach is likely to be better at representing the systems designers' goal setting behavior under a multiple design criteria situation.

Keywords: File allocation; Wide area networks; Distributed information systems; Goal setting; Compromise design; Multiple criteria

![](/api/attachments/Y64B8WWP/fulltext/images/e3b2667398571f6a9829daa13cdf5d6a2e3a32d0c1c8c40bfaff46870148e4b7.jpg)

Heeseok Lee is Assistant Professor of Information Systems and Quantitative Analysis at the College of Business Administration, the University of Nebraska at Omaha. Starting from 1994, Dr. Lee will teach at the Korea Advanced Institute of Science and Technology. He received his bachelor's degree in industrial engineering from Seoul National University, Seoul, Korea, his master's degree in industrial engineering from the Korea Advanced Institute of Science and

Technology, and his doctorate in management information systems from the University of Arizona. He taught information systems courses at the University of Arizona and the State University of Minnesota. Dr. Lee's research interests include systems analysis, database design, distributed databases, and telecommunication systems. He has his research papers published or forthcoming in Information and Management, Computers and Industrial Engineering, Journal of Systems and Software, Computers and Operations Research, European Journal of Operational Research, Systems Science, and Annals of Operations Research.

## Introduction

Distributed information technology is one of the most important computing developments. Many organizations from industry, academia, and government have used distributed databases to support their information needs. Their use has been accelerated by two driving forces: (i) technological advances in telecommunication systems and (ii) difficulties in satisfying organizational need for geographically dispersed information. A telecommunication infrastructure has great po-

![](/api/attachments/Y64B8WWP/fulltext/images/1fb82739f0d2b1c6d10888bdd0e61b115a7a9828c09e6057b80c0db889208130.jpg)  
tems, and telecommunication management. He has published in various journals including Management Science, Operations Research Letters, Computers and Operations Research, Mathematical and Computer Modeling, Decision Support Systems, and Asia-Pacific Journal of Operational Research. He is a member of DSI, ORSA, and TIMS.

![](/api/attachments/Y64B8WWP/fulltext/images/3ba2866c2c098acade747c8958804132145e8d0b43c21c7e21a177050a1b23d4.jpg)

tion in curriculum development. He has published in various journals including Decision Sciences, Omega, Review of Economics and Statistics, and Journal of Economic Inquiry.

Correspondence to: Dr. H. Lee, Department of Information Systems and Quantitative Analysis, International Center for Telecommunications Management, College of Business Administration, University of Nebraska, Omaha, Nebraska 68182-0048. e-mail: hlee@cwis.unomaha.edu.

tential for reducing the cost of information systems. Indeed, most database systems are being distributed [30,44].

A distributed database is a collection of data that logically belongs to the same organization or system but is physically spread over the sites of a data communication network. The two important aspects in the design of distributed databases are fragmentation and allocation $[5,32]$ . Fragmentation is the partitioning of an entire database into a set of different databases. Allocation concentrates on the (possibly replicated) distribution of these local fragments across geographically dispersed sites. An integration of both designs is referred to as distribution design (or data allocation design). A general method for designing centralized databases includes four phases: requirements collection and analysis, conceptual design, data model mapping, and physical design $[11]$ . The design of distributed databases adds to the above phases an additional one, distribution design.

Solving these two designs simultaneously is not a trivial task because of its complexity. Each design problem has been shown to be NP-complete $[1,12]$ . Therefore, a common approach is to solve one design in isolation, assuming that the other is determined a priori. This paper concentrates on allocation decisions, i.e., it studies how to allocate database fragments, that were previously computed according to any fragmentation method, to dispersed database locations. These database fragments are referred to as (data) files.

Data communications is of particular importance in distribution design. Broadly speaking, telecommunication networks can be categorized into local and wide area networks (LANs and WANs, respectively). Sheng and Lee [41] demonstrated how the distribution design depends upon the supporting data communication network: the primary incentive for distributed database implementations in LANs is load balancing, while the development of distributed databases via WANs is motivated by locality of reference. Today, LANs typically use cable, whereas WANs use telephone lines or satellites. Several approaches to file allocation on LANs include [27,29,45,47]. However, most file allocation research has been based on WANs. The operation of distributed databases on WANs has been considered important; e.g., [31].

The investigation of the file allocation problem on WANs dates to a pioneering work by Chu [6]. Since then, the file allocation design problem via wide area networks has been extensively studied in the literature (for example, see [4,8,16,33,35]). A common objective of these models is to minimize telecommunication costs. However, in a distributed information system, further economy can be achieved: the cost of allocating data files over geographically dispersed sites may be lower than the cost of frequently accessing a remote file over the network.

Furthermore, planning for distributed information systems involves other multiple design criteria, such as system response time and data availability. Solving for file allocation under multiple criteria in conflict is an open research area, even though a number of studies have been reported (e.g., [21,22]). In a conflicting situation, designers typically set their goals or targets, and iteratively modify them to find more effective designs under given constraints until satisfied. Therefore, it is of particular interest to address the goal setting behavior of designers of distributed information systems.

An analytical technique known as a compromise solutions approach supports a policy maker's goal setting process when multiple goals are in conflict. This paper applies a compromise modeling technique to file allocation design. Because this involves zero-one decision variables, the resulting model is termed a zero-one compromise model. This fits the designers' interactive decision making process very well, since target values are adjusted until a compromise design is finally reached. For example, Lee et al [25] recently applied this to the design of rural telecommunication systems.

## File allocation via wide area networks

A WAN typically has a point-to-point topology, with any two points connected by one or more communication channels. Let the total number of channels be m. A typical principle for data communications over WANs is that the data to be transmitted should be divided into smaller units termed packets. These traverse and queue for channels.

User requests for data in distributed information systems include queries and updates. A query requests data, whereas updates require modification of current data content in addition to retrieval. Each site is assumed to have its own central processor and its own software. A data file may have to be allocated to a local site because remote user access to it would be too slow.

We define a zero-one integer variable $x_{ik}^{f}$ , to be 1 when a copy of file i is allocated to site k; otherwise, 0. Denote a file allocation decision vector by $\mathbf{x}^{\mathbf{f}} = (x_{11}^{f}, \ldots, x_{ln}^{f})$ , where l is the total number of files and n is the total number of sites.

For multiple file copies, a query must be transmitted to the site that allows the most economical data retrieval. In order to describe query routing decisions, we define a zero-one integer variable $x_{ijk}^{q}$ that is 1 when a site j requests file i to be routed through site k; otherwise, 0. \* Denoting this query routing decision vector by $\mathbf{x}^{\mathbf{q}} = (x_{111}^{q}, \ldots, x_{lnn}^{q})$ , the decision variable becomes the vector $\mathbf{x} = (\mathbf{x}^{\mathbf{f}}, \mathbf{x}^{\mathbf{q}})$ .

The following system parameters are used to represent the file allocation design problem.

$\lambda =$ total rate of data requests entering the system

$\gamma =$ total data request rate within the system

$\alpha =$ total query request rate entering the system

$\beta =$ total update request rate entering the system

$\alpha_{ik} =$ the query request rate at site $k$ for file $i$

$\beta_{ik} =$ the update request rate at site $k$ for file $i$

$q_{ijk} =$ the telecommunication cost of the query for file $i$ between site $j$ and site $k$

$u_{ijk} =$ the telecommunication cost of the update for file $i$ between site $j$ and site $k$

$s_{ik} =$ the storage cost of file $i$ at site $k$

$p_{jk} =$ the set of channels that are contained in the path taken by data request (from site $j$ to site $k$ )

$r_{jk}$ = the probability that site j can communicate with site k

$r_k$ = the reliability of site $k$

$\tau =$ the average site delay of processing a packet

$1 / \mu =$ the average length of a packet

$\sigma_{i} =$ the size of file $i$

$\theta_{k} =$ the processing capacity of channel $k$

$\phi_{k} =$ the storage capacity of site $k$ .

The goal of building a distributed information system is a statement of the degree to which the managerial purpose must be realized. For example, if the purpose of building a distributed system is to minimize the telecommunication costs, a goal can be “Build the system while spending less than fifty thousand dollars per month”. Goal setting is an important aspect of human management practice and is a critical phase in the human decision making process.

In the design of distributed information systems, the following three goals are important.

1. Minimization of operating costs ( $y_{c}$ ): Operating costs include both telecommunication and site storage costs. Telecommunication costs occur due to data transfers for queries and updates. Storage costs occur because of file storage.

2. Minimization of system response time ( $y_{t}$ ): System response time is the expected time that either a query or an update spends in the system. It is estimated as the delays experienced in site processing and channel transfers. If data files are appropriately allocated, data can be accessed more effectively, i.e., the system response time can be reduced.

3. Maximization of data availability ( $y_{d}$ ): Data availability is defined as the fraction of data requests that are successfully executed (with respect to requests submitted to the system) over a given time interval [26]. Certain data requests may be lost due to site and/or channel failures, from these the source–destination reliabilities $r_{jk}$ are computed [2]. However, if the system supports multiple file copies, a data request can still be satisfied, i.e., the system can improve data availability.

These goals and the constraints are represented in terms of decision variables and system parameters (for further details, see a multicriteria file allocation model proposed by Lee and Sheng [24]). Operating costs consist of query telecommunication, update telecommunication, and data storage costs:

$$
\begin{array}{r}y_{c} = \sum_{i = 1}^{l}\sum_{k = 1}^{n}\left[ \sum_{\substack{j\neq k\\ j = 1}}^{n}\alpha_{ij}q_{ijk}x_{ijk}^{q} \right.\\ \left. + \left(\sum_{\substack{j\neq k\\ j = 1}}^{n}\beta_{ij}u_{ijk} + s_{ik}\right)x_{ik}^{f}\right]. \end{array}
$$

Representing each channel as an M/M/1 queue, the average time that a data request spends within the system is:

$$
\begin{array}{l}y_{t} = \tau +\frac{1}{\gamma}\sum_{c = 1}^{m}\sum_{\substack{j,k\\ c\in p_{jk}}}\sum_{i = 1}^{l}\left[\tau +\frac{1}{\mu\theta_{c}}\right]\\ \times \left(\alpha_{ij}x_{ijk}^{q} + \beta_{ij}x_{ik}^{f}\right). \end{array}
$$

For query-intensive distributed information systems, $\gamma$ is approximated by $\lambda (\gamma \approx \lambda)$ . In this case, $y_{t}$ is a linear function of decision variables. In contrast, system-wide data availability is:

$$
\begin{array}{c}y_{d} = \sum_{i = 1}^{l}\sum_{j = 1}^{n}\left[\sum_{\substack{k\neq j\\ k = 1}}^{n}w_{\alpha}\frac{\alpha_{ij}}{\alpha}\Big(r_{jk}x_{ijk}^{q} + r_{j}x_{ij}^{f}\Big) \right.\\ \left. + \prod_{\substack{k = 1\\ x_{ik}^{f} = 1}}^{n}w_{\beta}\frac{\beta_{ij}}{\beta} r_{jk}\right]. \end{array}
$$

The designer assigns relative importance $w_{\alpha}$ and $w_{\beta}$ , respectively, so that $w_{\alpha} + w_{\beta} = 1$ . For convenience, the set of system constraints is denoted by $S_{c}$ . First, because a data file must be allocated to at least one site,

$$
\sum_ {j = 1} ^ {n} x _ {i j} ^ {f} \geqslant 1, \forall i = 1, \dots , l.
$$

The site j request of file i must be transferred to one of the remote sites if file i is not placed at site j. Therefore,

$$
\sum_{\substack{k\neq j\\ k = 1}}^{n}x_{ijk}^{q} + x_{ij}^{f} = 1, \forall i = 1,\ldots ,l, j = 1,\ldots ,n.
$$

Because the site j request of file i is routed to site k only if file i is placed at site k,

$$
\begin{array}{c} x _ {i j k} ^ {q} \leqslant x _ {i k} ^ {f}, \forall i = 1, \ldots , l, j = 1, \ldots , n, \\ k = 1, \ldots , n, j \neq k. \end{array}
$$

Because updates are transmitted to all of the sites containing the data to be updated, the total request rate within the system depends on file allocation:

$$
\sum_{i = 1}^{l}\sum_{j = 1}^{n}\sum_{\substack{k\neq j\\ k = 1}}^{n}\beta_{ij}x_{ik}^{f} = \gamma -\alpha .
$$

In order for the communication network to remain stable,

$$
\sum_{i = 1}^{l}\sum_{\substack{j,k\\ c\in p_{jk}}}\left(\alpha_{ij}x_{ijk}^{q} + \beta_{ij}x_{ik}^{f}\right)\leqslant \mu \theta_{c},  \forall c = 1,\ldots ,m.
$$

For the storage requirements of each site,

$$
\sum_ {i = 1} ^ {l} \sigma_ {i} x _ {i k} ^ {f} \leqslant \phi_ {k}, \forall k = 1, \ldots , n.
$$

## Zero-one compromise model

This file allocation formulation is incorporated into the framework of a compromise model that was recently proposed by Shi and Yu [42]. One of its advantages is its applicability in the representation of human goal setting behavior. Furthermore, a compromise model is comprehensive: it includes goal programming models [18,20,28,36], which have been widely applied in multiple criteria environments.

In practice, target values for goals are set several times until the best design is reached. The flexibility of the compromise solutions accommodates a creeping commitment approach to goal setting. The trade-off among the three goals for file allocation requires zero-one integer decision variables. These variables have not been explored in past linear compromise models (see, for example, [48,49]).

In the compromise model, the objective is to minimize a regret function. For given $\kappa$ goals, define a vector $\mathbf{y}=(y_{1},y_{2},\ldots,y_{\kappa})$ as a set of goal functions. Let $y^{*}$ be a target vector that is initially set by designers. The regret of achieving y instead of achieving the target $y^{*}$ is represented by the distance between y and $y^{*}$ . Thus the regret function is defined by

$$
r (\mathbf {y}) = \left\| \mathbf {y} - \mathbf {y} ^ {*} \right\|.
$$

Typically, the $l_{p}$ norm is used to denote the distance. Therefore, for $p \geqslant 1$ ,

$$
r (\mathbf {y} \mid p) = \left[ \sum_ {i = 1} ^ {\kappa} \left| y _ {i} - y _ {i} ^ {*} \right| ^ {p} \right] ^ {1 / p}.
$$

Because the goals have different degrees of importance, the weighting vector w is applied. Applying weighting factors,

$$
r (\mathbf {y} \mid p, \mathbf {w}) = \| \mathbf {y} - \mathbf {y} ^ {*} \| _ {p, \mathbf {w}}.
$$

The expression can be rewritten as

$$
r (\mathbf {y} \mid p, \mathbf {w}) = \left[ \sum_ {i = 1} ^ {\kappa} w _ {i} ^ {p} \mid y _ {i} - y _ {i} ^ {*} \mid^ {p} \right] ^ {1 / p}.
$$

For convenience, further define $d_{i}^{+}$ , the value of $y_{i}$ exceeding $y_{i}^{*}$ , and $d_{i}^{-}$ , the value of $y_{i}$ below $y_{i}^{*}$ , respectively, for $i = 1, \ldots, \kappa$ , so that

$$
d _ {i} ^ {+} = \left\{ \begin{array}{l l} y _ {i} - y _ {i} ^ {*} & \text { if } y _ {i} > y _ {i} ^ {*} \\ 0 & \text { otherwise }; \end{array} \right.
$$

$$
d _ {i} ^ {-} = \left\{ \begin{array}{l l} y _ {i} ^ {*} - y _ {i} & \text { if } y _ {i} <   y _ {i} ^ {*} \\ 0 & \text { otherwise }. \end{array} \right.
$$

According to the above definition, it can be seen that

$$
y _ {i} ^ {*} - y _ {i} = d _ {i} ^ {-} - d _ {i} ^ {+}, \forall i = 1, \dots , \kappa ; \text { and }
$$

$$
d _ {i} ^ {+} \times d _ {i} ^ {-} = 0, \forall i = 1, \dots , \kappa .
$$

Applying these results removes the absolute value sign of regret function and yields

$$
r (\mathbf {y} \mid p, \mathbf {w}) = \left[ \sum_ {i = 1} ^ {\kappa} w _ {i} ^ {p} \left(d _ {i} ^ {-} + d _ {i} ^ {+}\right) ^ {p} \right] ^ {1 / p}.
$$

Minimization of this is equivalent to minimization of

$$
r ^ {\prime} (\mathbf {y} \mid p, \mathbf {w}) = \sum_ {i = 1} ^ {\kappa} w _ {i} ^ {p} \left(d _ {i} ^ {-} + d _ {i} ^ {+}\right) ^ {p}.
$$

Without loss of generality, we will use the above function $r'$ for the regret function.

The goal function $y_{i}$ is a function of x such that $y_{i}=f_{i}(\mathbf{x})$ for $i=1,\ldots,\kappa$ . In consequence, the file allocation design problem can be presented in the form of a compromise model as

Minimize $r(\mathbf{y} \mid p, \mathbf{w}) = \sum_{i=1}^{\kappa} w_i^p (d_i^- + d_i^+)^p$

Subject to $y_{i}^{*} - f_{i}(\mathbf{x}) = d_{i}^{-} - d_{i}^{+}, \forall i = 1, \ldots, \kappa$

$$
\mathbf {x} \in S _ {c}
$$

$$
\mathbf {x} \in \{0, 1 \}.
$$

The constraint, $d_{i}^{+} \times d_{i}^{-} = 0$ , is redundant and thus not incorporated into the formulation. In the case of one-sided goals, where $y_{i} \geqslant y_{i}^{*}$ (a lower bound goal) or $y_{i} \leqslant y_{i}^{*}$ (an upper bound goal), r does not need both $d_{i}^{-}$ and $d_{i}^{+}$ . For example, in the case of a lower bound goal, $d_{i}^{+}$ would be deleted from r because only a $d_{i}^{-}$ deviation may be penalized. In other words, the goal is to maximize $y_{i}$ only when $y_{i}$ is less than $y_{i}^{*}$ , i.e., it is not necessary to consider $d_{i}^{+}$ . In the same sense, $d_{i}^{-}$ would be deleted from r in the case of an upper bound goal.

To solve the resulting zero-one integer programming problem, we use the ZOOM system as developed by Singhal et al [43]. The total number of zero-one variables in the model is $l \times n \times (n + 1)$ . For example, allocating five files over ten sites requires 550 binary variables. This size is consistent with real-life file allocation designs that can be solved by the ZOOM. For example, Ram and Marsten [34] adopted the ZOOM to solve file allocations that require 6500 binary variables.

The weighting vector w must be estimated once the goals are identified. Either the MAUT (Multiple Attribute Utility Technique) [13,23] or the AHP (Analytic Hierarchy Process) [37,38] may be adopted on the basis of the designers' preference with respect to each goal. Historically, researchers have maintained both methods as separate areas of application. For a current debate between exponents and critics of these methods, see [9,10,15,17,39,40].

In this project, we illustrate the weighting process by using the AHP for its simplicity. The method starts by pairwise comparisons. A computer software package called Expert Choice [7,14] may be used for this estimation. A pairwise comparison is likely to generate the best estimation for simplicity and convenience. The basic premise is that two goals are compared at a time until all combinations of comparison have been considered. Thus, the total number of pairwise comparisons for given $\kappa$ goals is:

$$
\binom {\kappa} {2} = \frac {\kappa (\kappa - 1)}{2}.
$$

For our file allocation model, the total number is three because $\kappa = 3$ .

An example of a possible question during pairwise comparison is “In the file allocation, what is the relative importance of goal 1 (e.g., minimization of operating costs) versus goal 2 (e.g., minimization of system response time)?” The result from all of the pairwise comparisons is stored in a matrix $A = [a_{ij}]$ , a $\kappa \times \kappa$ matrix. Typically, the goals are sorted in descending order of importance. The element $a_{ij}$ gives the relative importance of goal i to goal j. Matrix A is arranged so that all diagonal elements are one. Its lower triangle is the reciprocal of the upper one. The relative weight of each goal may be calculated by an eigenvalue method and then stored in the form of a vector $\mathbf{w} = (w_{1}, \ldots, w_{\kappa})$ . Another measuring method, based on shadow prices instead of pairwise comparisons, can be found in [3].

Designers often update target values several times throughout the file allocation design process. This iterative process is often used by systems designers [46]. The target value that is feasible at one stage of database systems design may become less feasible or even infeasible later. At the same time, the compromise design may provide a better opportunity to assess model parameters (i.e., target values, weighing factors, etc.) for the designers; i.e., they may review the resulting file allocation design and value of the target function, and then interactively adjust parameters.

Within the framework of the creeping commitment, an iterative generation of compromise solutions is inevitable. The process continues until the best design is identified. This process is summarized in Figure 1.

## A sample distributed information system

Consider a credit card transaction company that maintains a distributed information system over six sites $n = 6$ . To process transaction requests, the company needs to operate databases over these geographically dispersed sites. The sites are connected by eight channels $m = 8$ via a wide area network as depicted in Figure 2. The company uses a single logical data file $l = 1$ . This prototype illustrates the applicability of the zero-one compromise model in file allocation design.

Table 1 shows the transaction request rates, data storage costs, and site reliabilities. The average packet size is 256 bytes ( $1/\mu = 256$ ). Table 2 shows query communication costs and capacities for communication channels. For example, $C_{12}$ is the channel between Seattle (Site 1) and Los Angeles (Site 2). The communication costs between these sites are the summation of costs for channels traversed by data requests. An expansion factor for updates is 20%, i.e., $u_{1jk} = 1.2 \times q_{1jk}$ , for $j = k = 1, \ldots, n$ , $j \neq k$ .

![](/api/attachments/Y64B8WWP/fulltext/images/75247ce02b98e1d2d6e6b66d365ff4e46fa4480f38bf86934e2cf79f2ea2bb77.jpg)  
Fig. 1. Creeping commitment design process in compromise model.

![](/api/attachments/Y64B8WWP/fulltext/images/aef5df72eae822ec2da346c885edad040a1408e1070f0072203499cfe51e8562.jpg)  
Fig. 2. A network topology for sample distributed system.

Site related data for a distributed information system

<table><tr><td>System parameter</td><td>Specification</td></tr><tr><td>Query request rate, sites 1..6 ( $\alpha_{1k}$ )</td><td>6.0 9.0 3.0 6.0 3.0 8.0 (request/sec)</td></tr><tr><td>Update request rate, sites 1..6 ( $\beta_{1k}$ )</td><td>2.0 2.0 1.5 2.0 1.0 2.0 (request/sec)</td></tr><tr><td>Storage cost, sites 1..6 ( $s_{1k}$ )</td><td>16.67 3.33 20.00 30.00 6.67 3.33 ($/day)</td></tr><tr><td>Site reliability, sites 1..6 ( $r_k$ )</td><td>98.5 95.5 98.0 99.0 97.5 99.0 (%)</td></tr></table>

Table 2  
Query communication costs and channel capacities

<table><tr><td>Communication channel</td><td>Query cost (0.01 cent/second)</td><td>Capacity (kilobits/sec)</td></tr><tr><td> $C_{12}$ </td><td>1.8</td><td>76.8</td></tr><tr><td> $C_{13}$ </td><td>2.7</td><td>76.8</td></tr><tr><td> $C_{24}$ </td><td>0.5</td><td>200.0</td></tr><tr><td> $C_{34}$ </td><td>1.1</td><td>76.8</td></tr><tr><td> $C_{35}$ </td><td>2.5</td><td>19.2</td></tr><tr><td> $C_{45}$ </td><td>1.5</td><td>76.8</td></tr><tr><td> $C_{36}$ </td><td>3.1</td><td>38.4</td></tr><tr><td> $C_{56}$ </td><td>1.3</td><td>76.8</td></tr></table>

Table 3 shows source-destination reliabilities $r_{jk}$ . The system operates 100 hours per week and 4.2 weeks per month. Sufficient storage capacity is assumed at each site. In this system, the nodal delay is dominated by the telecommunication delay and thus ignored, i.e., $\tau = 0$ . The emphasis is on query transactions so that $\gamma \approx \lambda = 45.5$ , $w_{\alpha} = 1$ , and $w_{\beta} = 0$ .

The designer first has to determine the relative importance of goals by pairwise comparison. For this purpose, the designer must define one unit of each goal. This must be determined so that the designer can make comparison in a consistent fashion. The units used are \$1,000/month for operating costs, 1 second for system response time, and 1% for data availability. With respect to these units, goals are compared. For instance, a question is asked to systems users: What is more important, and by how much, a \$1,000/ month decrease of operating costs or a 1 second decrease of system response time? If the answer is that the first is five times more important than the second, then $a_{12}=5$ . The result of all such pairwise comparisons is then represented in matrix A:

Table 3  
Source-destination reliability ( $r_{jk}$ ) of the communication network (unit: %)

<table><tr><td rowspan="2">Source</td><td colspan="6">Destination</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>-</td><td>97.0</td><td>95.5</td><td>92.1</td><td>92.6</td><td>91.5</td></tr><tr><td>2</td><td>97.0</td><td>-</td><td>92.0</td><td>94.3</td><td>93.1</td><td>91.5</td></tr><tr><td>3</td><td>95.5</td><td>92.0</td><td>-</td><td>96.3</td><td>96.5</td><td>95.1</td></tr><tr><td>4</td><td>92.1</td><td>94.3</td><td>96.3</td><td>-</td><td>94.6</td><td>93.6</td></tr><tr><td>5</td><td>92.6</td><td>93.1</td><td>96.5</td><td>94.6</td><td>-</td><td>96.5</td></tr><tr><td>6</td><td>91.5</td><td>91.5</td><td>95.1</td><td>93.6</td><td>96.5</td><td>-</td></tr></table>

$$
A = \left( \begin{array}{c c c} 1 & 5 & 7 \\ \frac {1}{5} & 1 & 3 \\ \frac {1}{7} & \frac {1}{3} & 1 \end{array} \right).
$$

The eigenvalues that represent the estimated normalized weights are then:

$$
\mathbf {w} = (0. 7 3 1, 0. 1 8 8, 0. 0 8 1)
$$

The inconsistency ratio is 0.130, which is accepted by the designer. Cost and response time goals are upper bounded, whereas the availability goal is lower bounded. The designer feels that his regret is linearly proportional to the distance between the target point and goal achievement, i.e., p = 1. Hence, the objective function for the zero-one compromise model is:

Minimize $r(\mathbf{y}) = 0.731d_c^+ + 0.188d_t^+ + 0.081d_d^-$ .

The total number of zero-one variables for the compromise model is 30. The designer sets an initial target value as:

$$
\mathbf {y} _ {1} ^ {*} = (10, 000, 45.0 \text { sec }, 99.0\%).
$$

To meet this target value, a compromise design is obtained by recommending that a file be allocated to Dallas in isolation ( $x_{4}^{f}=1$ ). Therefore, only Dallas can serve query services, i.e., $x_{14}^{q}=x_{24}^{q}=x_{34}^{q}=x_{54}^{q}=x_{64}^{q}=1$ . Each goal function is then achieved at the level of $\mathbf{y}_{1}=(\$10,840, 46.5\ sec, 96.0\%)$

The designer is not satisfied with such low achievements of system response time and data availability and is willing to pay up to \$12,000 in exchange for reducing the system response time to 45 seconds while increasing data availability to 97.5%. Therefore, the second target is: $y_{2}^{*} = ($12,000, 45.0 \ sec, 97.5\%)$ .

Another compromise design for this target is obtained by recommending that file copies be allocated to both Los Angeles and New York, i.e., $x_{2}^{f} = x_{6}^{f} = 1$ . Query requests from Seattle, Omaha, and Dallas are routed to Los Angeles, whereas query requests from Atlanta are routed to New York, i.e., $x_{12}^{q} = x_{32}^{q} = x_{42}^{q} = x_{56}^{q} = 1$ . Goal functions are then: $\mathbf{y}_{2} = (\$12,150, 46.2 \ sec, 96.7\%)$ .

Actually, the response time and data availability are improved by 0.65% ( $=\{46.5-46.2\}/\{46.5\}\times100$ ) and 0.73% ( $=\{96.7-96.0\}/\{96.0\}\times100$ ), respectively, with the detriment of 12.1% ( $=\{12,150-10,840\}/\{10,840\}\times100$ ) of operating costs. The designer still attempts to explore the possibility of improving response time and data availability by allowing \$12,500 of operating costs (this is the maximum allowable costs). Therefore, a new target is set as

$y_{3}^{*} = (\$12,500, 45.0 \ sec, 97.0\%).$

Even under this target, the compromise design remains unchanged. Therefore, the designer accepts this as the best one and quits the iterative process, i.e., file copies are allocated to Los Angeles and New York. The monthly operating cost is \$12,150, the system response time is 46.2 seconds, and data availability is 96.7%.

## Conclusions

This paper presents a methodology for incorporating human goal seeking behavior into file allocation decisions in a distributed information system using WANs. The applicability of a zero-one compromise modeling in file allocation was demonstrated with a sample distributed system. The iterative target setting process is likely to better represent designers' compromising behavior while trading off multiple goals.

From a practical perspective, the design of distributed information systems involves processor location, program location, and network topology as well as file allocation. Modeling and optimization of this comprehensive model under multiple goals is not a trivial task. One promising approach would be to find a method that can be applied in real-life projects by incorporating some major system parameters into the model. Incorporating an exchange heuristic $[19]$ into the proposed design procedure may be a good candidate.

## Acknowledgment

The authors wish to thank Dr. E.H. Sibley for detailed comments to improve the presentation of this paper.

## References

[1] P.M.G. Apers, “Data allocation in distributed database systems,” ACM Trans. Database Systems, vol. 13, 1988, pp. 236–304.

[2] M.O. Ball, “Computing network reliabilities,” Operations Research, vol. 27, 1979, pp. 823–838.

[3] E. Ballestero and C. Romero, “Weighing in compromise programming: a theorem on shadow prices,” Operations Research Letters (forthcoming).

[4] R.G. Casey, "Allocation of copies of a file in an information network," Proc. AFIPS Spring Joint Computer Conf., AFIPS Press, 1972, pp. 617-625.

[5] S. Ceri and G. Pelagatti, Distributed Databases: Principles and Systems, McGraw-Hill, 1984.

[6] W.W. Chu, "Optimal file allocation in a computer network," IEEE Trans. Computers, vol. 18, 1969, pp. 885-888.

[7] D.M. Buede, “Superior design features of decision analytic software,” Computers and Operations Research, 19, 1992, pp. 43–57.

[8] L.W. Dowdy and D.V. Foster, “Comparative models of the file assignment problem,” ACM Computing Survey, vol. 14, 1982, pp. 287–313.

[9] J.S. Dyer, “Remarks on the Analytic Hierarchy Process,” Management Science, vol. 36, 1990, pp. 249–258.

[10] J.S. Dyer, “A clarification of remarks on the Analytic Hierarchy Process,” Management Science, vol. 36, 1990, pp. 274–275.

[11] R. Elmasri and S.B. Navathe, Fundamentals of Database Systems, Benjamin/Cummings, 1989.

[12] K.P. Eswaran, “Placement of records in a file and file allocation in a computer network,” Proc. IFIP Congress, 1974, pp. 304–307.

[13] P. Fishburn, The Foundations of Expected Utility, Reidel, Dordrecht, 1982.

[14] E.H. Forman, T.L. Saaty, M.A. Selly and R. Waldron, Expert Choice, Pittsburgh: Decision Support Software Inc., 1985.

[15] E.H. Forman, “AHP is intended for more than expected value calculations,” Decision Sciences, vol. 21, 1990, pp. 670–672.

[16] B. Gavish and H. Pirkul, “Computer and database location in distributed computer systems,” IEEE Trans. Comput., vol. 35, 1986, pp. 583–590.

[17] P.T. Harker and L.G. Vargas, “Reply to remarks on the Analytic Hierarchy Process by J.S. Dyer,” Management Science, vol. 36, 1990, pp. 269–273.

[18] F.S. Hillier and G.J. Lieberman, Introduction to Operations Research, Holden-Day, 1986.

[19] J.P. Ignizio, “Solving large-scale problems: a venture into a new dimension,” J. Opl. Res. Soc., vol. 31, 1980, pp. 217–225.

[20] J.P. Ignizio, Linear programming in single and multiple objective systems, Prentice-Hall, 1982.

[21] H.K. Jain and A. Dutta, “Distributed computer system design: a multicriteria decision making methodology,” Decision Sciences, vol. 4, 1986, pp. 437–453.

[22] H.K. Jain, “A comprehensive model for the design of distributed computer systems,” IEEE Trans. Software Eng., vol. 13, 1987, pp. 1092–1104.

[23] R. Keeney and H. Raiffa, Decisions with Multiple Objectives, John Wiley and Sons, New York, 1976.

[24] Heeseok Lee and O.R. Liu Sheng, “A multiple criteria model for the allocation of data files in a distributed information system,” Computers Ops Res., vol. 21, 1992, pp. 21–33.

[25] Heeseok Lee, Y. Shi, and S. Nazem, “Supporting rural telecommunication networks via hub cities: a compromise solutions approach,” International Center for Telecommunications Management Research Paper #20, University of Nebraska at Omaha, 1992.

[26] Heeseok Lee, “An evaluation method for the availability of a distributed database management system,” Inform. and Management, vol. 24, 1993, pp. 203–208.

[27] Heeseok Lee, “Modelling and optimization of data assignment in a distributed information system,” Systems Science, vol. 24, 1993, pp. 173–181.

[28] S.M. Lee, Goal Programming for Decision Analysis, Pennsylvania: Auerbach, 1972.

[29] Y.N. Lien, Y.L. Chang, and B.W. Wah, "File allocation problems on homogeneous two-level local broadcast networks," Proc. Fourth Int'l Conf. on Data Engineering, 1988, pp. 92–99.

[30] R. Nolan, “Managing the advanced stages of computer technology; key research issues,” In E.W. McFarlan, ed., The Information Systems Research Challenge, Boston, Mass.: Harvard Business School Press, 1984.

[31] M.T. Ozsu and P. Valdureiz, “Distributed database systems: where are we now?,” Computer, vol. 24, 1991, pp. 68–78.

[32] M.T. Ozsu and P. Valdureiz, Principles of Distributed Database Systems, Prentice-Hall, 1991.

[33] S. Ram, “A model for designing distributed database systems,” Inform. and Management, vol. 17, 1989, pp. 169–180.

[34] S. Ram and R.E. Marsten, "A model for database allocation incorporating a concurrency control mechanism," IEEE Trans. Knowledge and Data Engineering, vol. 3, 1991, pp. 389-395.

[35] R. Ramesh and B. Ryan, "Optimal file allocation and report assignment in distributed information networks," Naval Research Logistics, vol. 37, 1990, pp. 165-181.

[36] C. Romero, Handbook of Critical Issues in Goal Programming, Oxford: Pergamon Press, 1991.

[37] T.L. Saaty, “A scaling method for priorities in hierarchical structures,” J. Math. Psychology, vol. 15, 1977, pp. 234–281.

[38] T.L. Saaty, The Analytic Hierarchy Process, New York: McGraw-Hill, 1980.

[39] T.L. Saaty, “An exposition of the AHP in reply to the paper, Remarks on the Analytic Hierarchy Process,” Management Science, vol. 36, 1990, pp. 259–268.

[40] B. Schoner, W.C. Wedley and E.U. Choo, “A rejoinder to Forman on AHP, with emphasis on the requirements of composite ratio scales,” Decision Sciences, vol. 23, 1992, pp. 509–517.

[41] O.R. Liu Sheng and Heeseok Lee, “Data allocation design in computer networks: LAN versus MAN versus WAN,” Annals of Operations Research, vol. 36, 1992, pp. 125–150.

[42] Yong Shi and P.L. Yu, "Goal setting and compromise solutions," In B. Karpak and S. Zionts (Eds.), Multiple criteria decision making and risk analysis using microcomputers. Berlin: Springer-Verlag, 1989.

[43] J. Singhal, R.E. Marsten and T.L. Morin, “Fixed order branch-and-bound methods for mixed-integer programming: the ZOOM system,” ORSA Journal on Computing, vol. 1, 1989, pp. 44–51.

[44] M. Stonebraker, “Future trends in database systems,” IEEE Trans. Knowledge and Data Engineering, vol. 1, 1989, pp. 33–44.

[45] B.W. Wah and Y.N. Lien, “Design of distributed databases on local computer systems,” IEEE Trans. Software Eng., vol. 11, 1985, pp. 606–619.

[46] J.L. Whitten, L.D. Bentley and V.M. Barlow, Systems Analysis and Design Methods. Irwin, 1989.

[47] C.T. Yu, M. Siu, K. Lam and C.H. Chen, "Adaptive file allocation in star computer network," IEEE Trans. Software Eng., vol. 11, 1985, pp. 959-965.

[48] P.L. Yu, Multiple-Criteria Decision Making: Concepts, Techniques and Extensions, New York: Plenum Press, 1985.

[49] M. Zeleny, “A concept of compromise solutions and the method of the displaced ideal,” Computers and Operations Research, vol. 1, 1974, pp. 479–496.
