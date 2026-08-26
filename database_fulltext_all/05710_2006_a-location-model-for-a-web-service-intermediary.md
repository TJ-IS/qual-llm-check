---
otero_id: 5710
otero_key: "QMKDAPEV"
title: "A location model for a web service intermediary"
authors: "Yi Sun; Gary J. Koehler"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.016"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A location model for a web service intermediary

Yi Sun <sup>a,\*</sup>, Gary J. Koehler <sup>b</sup>

<sup>a</sup> College of Business Administration, California State University San Marcos, CA 92069, USA

<sup>b</sup> The Warrington College of Business Administration, University of Florida, Gainesville, FL 32611, USA

Available online 13 January 2005

## Abstract

Recently, Web services have entered the competition for a new type of distributed e-commerce platform. This paper studies the placement of servers of a Web service intermediary. The intermediary serves as a common interface to its clients while obtaining Web services from independent providers. The intermediary locates its servers by minimizing costs where a major component is network latency. We propose and study an integer programming formulation to determine the locations and usage rates of the servers of an intermediary. A greedy heuristic method is used to obtain good solutions to the problem. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Web services; Web services intermediary; Facility location; Network latency; Heuristic algorithm

## 1. Introduction

Web services now compete with other middle-tier technologies as a possible alternate distributed ecommerce platform. They promise to deliver an unprecedented level of interoperation between programs written in different languages and running on different platforms by exploiting existing open standards, such as the extensible markup language (XML) and the ubiquitous hypertext transfer protocol (HTTP). Because of modularization and open interfaces, Web services facilitate the development of highly customizable and adaptable applications to meet business demand. In addition, Web services offer a convenient registration, search and discovery system. This system potentially breeds a market of Web services intermediaries (WSIs) who, on behalf of their clients, search, assemble and customize various Web services from Web services providers (WSPs), either statically or dynamically at run time to meet additional conditions that may vary such as quality, speed, etc. This paper focuses on the problems faced by a Web services intermediary in locating its servers.

Web services are independent programmable application components that offer services to other applications through commonly defined interfaces and standard Web protocols across the Internet. Transactions over the Internet currently rely mainly on Web browsers and traditional distributed component technologies (such as Microsoft’s Component Object Model, COM+, and Sun’s Enterprise Java Beans).

Web services surpass the browser-based approaches by allowing services to be programmatically manipulated and making service accessible to any device which implements HTTP protocols. They exceed traditional distributed component technologies with interoperability and platform-and-language-independence.

Web services also have the potential to transform business conducted on the Internet. For end users, they are more accessible over the Internet than previous technologies. In addition, they may lower entry cost for end users by offering differential pricing through extensive service customization that accommodates businesses with different budgets. They also promise to alleviate organizations’ concerns for interoperability in areas such as Enterprise Application Integration and Business-to-Business Integration. Industry analysts (e.g. [1,8]) suggest that Web services provided competitive advantages in business relationships and product development. They also indicate that more businesses than ever were adopting the platform for their core activities.<sup>Q</sup>

There are three major players in Web services architectures: WSPs, WSIs, and service requesters. WSPs offer Web services and maintain a registry to make them exposed and accessible. Service requestors use Web services by invoking those services themselves or through WSIs. WSIs act as matchmakers between WSPs and service requestors. They add synergistic value to the services and offer other value-added activities such as additional processing of information, collation, quality control, etc. Part of the motivation for clients to go through a WSI instead of contacting WSPs directly is to take advantage of unified interfaces and added services offered by the WSI.

Web services can be used by any business that conducts transactions using Web-based applications. For example, a Web services application can be written for a travel agent who helps its clients with travel arrangements. Its clients submit itineraries through client applications to the agent application. The agent then decomposes the request into multiple sub-requests and contacts appropriate Web services, such as hotel reservations, airplane reservations, weather reports and credit card transactions, etc., offered by various businesses to answer these subrequests. After all sub-requests are served, the agent then confirms the itinerary and sends all relevant information back to its clients. In this case, the travel agent application serves as a WSI and businesses that offer Web services WSPs.

One of the major benefits of using Web services for this application is that all services involved are only loosely coupled programmatically. The agent does not need to have prearrangement with any service providers. It can secure the appropriate services at run time and switch to others when necessary.

The performance of a distributed service is often judged by its response time. Service response time is of paramount concern for some time-sensitive applications, such as financial ones. Response time includes local processing time and network response time. Network response time consists of transmit time (the time to load data on to the network), queuing delays, and network latency. Network latency refers to the amount of time that a packet of data takes to travel from one location to another on a network [13].

Until recently, studies of service response time [18,20] focused on increasing local processing speed and reducing transmission time and queuing delays. Network latency was often justifiably ignored. Compared with other factors, especially on a slow, local network, network latency accounted only for a small percentage of service response time.

However, because of recent changes, such as the move to high-speed Internet communication with broadband connections and tremendous increases in computing power, recent studies [12,13] suggest that network latency has begun to play a more important role in determining total service response time. Recent literature on efficiently redirecting clients<sup>T</sup> requests to the appropriate server [15,21] or on optimally placing servers [3,4,9,16,17] focused on reducing network latency.

Potentially, network latency is even more important in the study of Web services location problems. Web services are implemented on a loosely coupled network. An application may need the collaborations of many remotely located Web services and may generate many messages to discover, negotiate, and invoke these services. These messages greatly increase the overall network latency. In addition, Web services often create short messages to discover and arrange services, and to pass parameters. According to [13], network latency has a bigger impact on total service response times when messages are short.

Minimizing service response time consequently requires decreasing the network latencies between servers and clients. For problems of locating Web services, network latency is closely related to the proximity between Web services and their clients. The placement of Web services on a network therefore becomes critical in improving network latency and service response time.

The main purpose of this research is to provide a framework that guides a WSI to locate its servers. A WSI serves as an interface to both its clients and WSPs. The WSI contacts various service providers at run time and compiles multiple Web services into a coherent presentation to its clients. The research problem studied here is to formulate and solve a model to determine the placement of WSI servers. We structure costs based on network latency and other local operating costs. The objective is to minimize a WSI’s overall expected operating cost. To balance the loads between its clients and WSPs, the WSI needs to determine where and how many servers to deploy and to choose appropriate WSPs who often offer similar Web services at different prices and with different performance and capacities. To capture the levels of customization that Web services offer, the model requires the WSI to map each client request to a vector of needed Web services. A single client request is a bundle of these Web services, represented as a vector. A client will request a multiple number of such bundles, but each bundle is identical.

The formulation of this problem results in a capacitated, fixed cost, mixed-integer mathematical programming model. As expected, this model becomes computationally intractable as the number of participants increases. We therefore turn our attention to heuristics that can be employed to solve the problem. Furthermore, since a WSI can find and assemble Web services at run time, matching its client requests with needed Web services is often done dynamically while minimizing latencies. This requires efficient algorithms to solve the problem.

Many studies of server placement on a network [2,12] have borrowed analytical tools and algorithms from well-developed literature of facility location models [6]. Our model derives but differs from these models in several respects. First, as a three-tiered model, it studies interactions between clients, an intermediary and service providers, and, distinctly, the sharing relationship between servers of the intermediary. Many facility location models are twotiered. In the case of three-tiered models, the relationship between intermediaries is not often explored. Second, it is assumed here that a client does not assemble services himself (or then the client acts as a type of intermediary) but gets each bundled request, in whole, from a single intermediary server. Since the client may request multiple such bundles, he may request and get his bundles from possibly more than one intermediary server. Hence, a WSI serves as a unified interface and synthesizes a number of services from potentially many WSPs to offer its client an integrated answer, while facility location models either impose a pre-selected single-source constraint for all items or allow clients to obtain services needed for its total needs from all facilities without the requirement that a facility deliver goods in integer multiples of the basic bundle request. Lastly, the model studies the latency of delivering bundled information goods. The latency cost of such delivery is usually not a function of the size of the parts. Facility location models seldom synthesize or integrate physical products and even when they do, the cost of shipping the integrated product is often a function of the total weight and size and therefore the transportation cost structures between facilities and their clients are different from ours.

In Section 2 we provide a formulation for our model. Section 3 develops heuristics that are studied in Section 4. We use these to study a number of hypotheses on the placement of WSIs. These solutions are compared to optimal solutions obtained from CPLEX 8 [11] where possible. The experiments and their results are discussed in Section 5. We end with a discussion of our results and possible future research directions in Section 6.

## 2. Model formulation

In this section we define the WSI’s server location problem. The model captures the characteristics of the WSI and its interactions with its clients and WSPs. The problem objective is to minimize the operating costs of the WSI while satisfying all constraints imposed by the location infrastructures, client demand and WSPs characteristics. The costs include commu-

Table 1 Summary of notation

nication cost, which is a function of the network latency between a server and a client, and the servers<sup>T</sup> service times. The WSI may set up multiple servers at different locations to reduce service delays. We assume that all overhead database information shared between WSI servers is kept synchronized in this study. Upon receiving service requests from its clients or other WSI servers, a WSI server will contact one or more remotely located WSPs and possibly other WSI servers to process these requests. The WSI server will then return the requested information to its clients or pass information to other requesting WSI servers.

The planning horizon of this WSI location problem consists of several consecutive periods. Initially, the WSI makes decisions to minimize cost. After the first period and at the beginning of each successive period, it reviews and rebalances previous decisions when encountering changes in the customer base and demand, the number of and offerings by WSPs and the properties of WSI server locations. We focus on the WSI’s initial decision in this study.

Table 1 summarizes the parameters and variables used in our model. We assume all data are deterministic and leave variable or stochastic considerations for future research. Consider a network $G { = } ( V , E )$ with vertices $\nu \in V ,$ and undirected arcs, e<sup>a</sup>E. We use to represent the number of the vertices $( \nu \equiv \mid V \mid )$ , an index of a location and, later, a decision variable letting context keep the particular meaning clear. These servers have the same interface, functionality and accessibility to all clients and WSPs. They differ from one another only by their physical locations, fixed setup cost, and service capacities.

If a WSI locates a server on vertex i, we refer to this server as server i. Different locations, (i.e., vertex i) may incur different fixed costs, $f _ { i } ,$ to host a WSI server, i. In practice, a location may also charge the WSI a variable cost based on that server’s usage of the facility and bandwidth. This cost is subsumed in the variable communication cost between WSI servers and their clients. Each location posts a capacity limit, $s _ { i } ,$ on the number of requests a WSI server, i, can process per period. The WSI knows the number of its clients, their locations, $c \in C \subseteq V ,$ and their expected requests and service requirement, $r _ { c }$

We assume that the variety of applications supported by our model have well-defined Web service requirements so reasonably accurate estimates of types and volumes of requests are known in advance. The WSI knows that there are z distinct Web services offered in the market by WSPs and knows how to use these Web services to process its client requests. It maps client $c \mathbf { \hat { s } }$ request to a z-dimensional vector of Web services, denoted by bundle $h _ { c }$ . Any particular client request may not need all z Web services, in which case the unused Web services will have a zero value in the appropriate row of $\ h _ { c } .$ . A WSI server must satisfy client requests as integer multiples of the bundle, although the client can submit requests to multiple WSI servers at the same time. The actual serving WSI locations are determined by a solution to the model and each delivers integer multiples of the required bundle. The total number of deliveries to client c is $r _ { c }$

<table><tr><td colspan="2">Summary of notation</td></tr><tr><td> $G=N(V,E)$ </td><td>Undirected graph  $G$  with node (vertex) set  $V$  and undirected arc (edge) set  $E$ </td></tr><tr><td> $v=|V|$ </td><td>Positive integer indicating the number of vertices and the index of their locations in the network  $G$ </td></tr><tr><td> $e\in E$ </td><td>An undirected arc in the network  $G$ </td></tr><tr><td> $l_{i,j}$ </td><td>Nonnegative variable communication cost from vertex  $v_i$  to  $v_j$  (see text for more details)</td></tr><tr><td> $u_{i,j}$ </td><td>Nonnegative integer decision variable representing the number of transfers of Web services vector from vertex  $i$  to  $j$ ; this may be from a client to a WSI server or from a WSI server to a WSP</td></tr><tr><td> $z$ </td><td>Number of different types of Web services available</td></tr><tr><td> $v_i\in\{0,1\}$ </td><td>Binary variable that takes value 1 if vertex  $i$  is used as a WSI server location and 0 otherwise</td></tr><tr><td> $\alpha_{i,j}$ </td><td>Nonnegative integer decision vector valued variable representing the slack of Web services usage given from WSI server  $i$  to server  $j$ , a vector of  $z$  dimensions; each dimension represents a unique Web service</td></tr><tr><td> $p$ </td><td>The number of Web services sent at a time between WSI servers</td></tr><tr><td> $f_i$ </td><td>Nonnegative fixed cost per period to establish a WSI server at location  $i$ </td></tr><tr><td> $s_i$ </td><td>WSI server  $i$ &#x27;s capacity per period. It refers to the number of requests a WSI server can process per period</td></tr><tr><td> $o$ </td><td>A  $z$ -dimensional sum vector with all elements equal to 1</td></tr><tr><td> $c\in C\subseteq V$ </td><td>Index of client locations in the network  $G$ </td></tr><tr><td> $r_c$ </td><td>Nonnegative integer representing the service level requirement for client  $c$  per period; it refers to the number of requests a client submits per period</td></tr><tr><td> $h_c$ </td><td>A  $z$ -dimensional, nonnegative integer vector of Web services that client  $c$  uses per service; each dimension represents a unique Web service; the full vector is called a bundle and deliver to the client is in bundles</td></tr><tr><td> $w\in W\subseteq V$ </td><td>Index of WSP locations in the network  $G$ </td></tr><tr><td> $q_w$ </td><td>A  $z$ -dimensional, nonnegative integer vector of Web services that WSP  $w$  provides; each dimension represents a unique Web service</td></tr><tr><td> $t_w$ </td><td>WSP  $w$ &#x27;s capacity per period. It refers to the number of requests a WSP can process per period</td></tr><tr><td> $x_w\in\{0,1\}$ </td><td>Binary variable that takes value 1 if a WSI uses service provided by WSP  $w$ , and 0 otherwise</td></tr><tr><td> $g_w$ </td><td>Nonnegative fixed fee that WSP  $w$  charges a WSI per period for accessing the WSP&#x27;s service</td></tr></table>

Upon receiving requests from a client, the WSI will use the corresponding Web services vector to obtain Web services from appropriate WSPs. A WSP publishes its $w { \in } W { \subseteq } V$ location in the graph G. It also publishes its services as Web services vector $q _ { w }$ (also z dimensional with zero-valued entries as needed). If a WSP offers different vectors, we break the WSP into multiple sub-WSPs on duplicates of the same vertex so each WSP vertex offers just one vector. We assume that each request from a WSI server is for all the elements of a WSP’s Web services offering. This assumption is justified by WSP’s desire for bundling and/or for resource pooling. In addition, compared with proprietary technologies that are fine tuned for specific task, Web services often generate higher overhead per transaction. Therefore requesting multiple Web services at a time helps the WSI to cut down communication cost by lowering the number of requests for WSP’s services.

$\mathrm { W S P } _ { w }$ is subjected to a service capacity constraint, $t _ { w } ,$ limiting the number of requests it can process. In addition, $\mathrm { W S P } _ { w }$ charges the WSI a fixed fee, $g _ { w } ,$ per period. The WSP may also charge a variable fee based on the usage of its service. This cost is subsumed in the variable communication cost between WSI servers and WSPs. Since a service request to a WSP activates its entire Web services vector, there are times when some Web services are not utilized by the original requesting WSI server but are nevertheless available. We allow a WSI server to share such excess Web services with other WSI servers. We assume the timevalue of the requests holds for the problem’s planning period. We use $\boldsymbol { \alpha } _ { j , i }$ as a decision vector to denote the Web services that are shared by WSI server $j$ with WSI server i. Each element of this vector can be shared in discrete amounts but $p$ each units shared incurs a communication charge and reduces service capacity by one unit. Unless stated otherwise, $p$ is normally one. By enabling sharing, we trade-off communication costs and the variable fees (imbedded in communication costs) to access remote WSPs with the communication costs between WSI servers to obtain a possibly lower overall cost.

Let $u _ { i , j }$ be a decision variable representing the frequency of communication between vertex i and j per period. It is a multiplier used with Web services vectors $h _ { c }$ and $q _ { w }$ to calculate the amount of Web services needed per period. For example, $h _ { c } u _ { c i }$ vector stands for the entire Web services delivered to client c from WSI server i per period. Similarly, vector $q _ { w } u _ { i , w }$ stands for all the Web services that WSI server i obtains from WSP per period.

Communication between vertices $\nu _ { i }$ and $\nu _ { j }$ incurs a variable communication cost $l _ { i , j }$ . This cost is primarily a result of service delay and can be considered as an opportunity cost expressed in the form of reimbursement from a WSI to its clients. For information goods, communication costs are less determined by the quantity of the information goods delivered per transaction than the network latencies they incur. As discussed earlier, network bandwidth and congestions are constantly improving while network latency remains the same-largely limited by the constant speed of light through fiber optic media. In addition, although we decompose a service request into multiple Web services, the communication costs of the request may be independent of the number of Web services. This is because, although a WSI server may obtain multiple responses from these services, it often uses them to construct just one coherent answer to the service request and therefore incurs only one unit of communication cost when sending the result back to the client. We assume that the total communication cost on an arc may include possible different costs of sending and receiving messages. In the following, we treat as a linear cost based on the number of service requests.

## 2.1. Model description

In this model, we seek to determine the number and locations of WSI servers and the WSPs that the WSI contacts for services to minimize the overall operating costs for the WSI. There are four sets of decision variables: the locations of WSI servers, $\nu ,$ the frequencies of communications between participants, $u ,$ the selections of WSPs as service providers, x, and the amount of Web services shared between WSI servers, a.

A WSI solves the following discrete optimization problem (1) with the following objective function and constraints (2)–(5). The objective function is

$$
\begin{array}{l} \min _ {v, u, x, \alpha} \sum_ {c \in C} \sum_ {i \in V} l _ {c, i} u _ {c, i} + \sum_ {i \in V} \sum_ {w \in W} l _ {i, w} u _ {i, w} \\ + \frac {1}{p} \sum_ {i \in V} \sum_ {i, j \in V _ {j \neq i}} l _ {i, j} o ^ {\prime} \alpha_ {i, j} + \sum_ {i \in V} f _ {i} v _ {i} + \sum_ {w \in W} g _ {w} x _ {w} \end{array}\tag{1}
$$

The first term is the communication costs between WSI servers and their clients. The second term is the communication costs between WSI servers and WSPs. The third term is the communication costs between WSI servers, where o is a z-dimensional sum vector with all elements equal to 1 and $( 1 / p ) o ^ { \prime } \alpha _ { i , j }$ and is the communication frequency between WSI servers i and j. The fourth term gives the fixed costs to setup all WSI servers. The last term refers to the fixed fees that WSPs charge the WSI.

## 2.2. Web services usage constraint

We model a market in which all clients of the WSI are fully served. Each WSI server should process all the incoming requests from its clients. Since we break down the client requests to Web services, each WSI server should obtain enough Web services from WSPs and other WSI servers who enjoy excess Web services minus those it shares with other WSI servers. This requirement is captured by

$$
\sum_ {c \in C} h _ {c} u _ {c, i} \leq \sum_ {w \in W} q _ {w} u _ {i, w} + \sum_ {j \in V} \alpha_ {j, i} - \sum_ {j \in V} \alpha_ {i, j} \quad \forall i \in V\tag{2}
$$

Here the first term is the total client requests in terms of Web services to WSI server i. The second term is the amount of Web services that WSI server obtains from WSPs. The third term is amount of the Web services that WSI server i obtains from other WSI servers. The fourth term is amount of the Web services that WSI server i shares with other WSI servers.

## 2.3. WSI server’s capacity and client assignment constraint

Each WSI server location has a service capacity constraint limiting the amount of requests the server can process per period. This constraint is often a result of service contracts, company policy, and/or technical limitations posed on the server by its location’s infrastructure. This constraint requires that no WSI server can provide more services to its clients and provide and receive more services from other WSI servers than its capacity allows. In addition, this constraint insures that if a location is not selected as a WSI server location, no clients or WSI servers will request services from or send services to this location.

$$
\sum_ {c \in C} u _ {c, i} + \frac {1}{p} \sum_ {j \in V} o ^ {\prime} \alpha_ {i, j} + \frac {1}{p} \sum_ {j \in V} o ^ {\prime} \alpha_ {j, i} \leq s _ {i} v _ {i} \quad \forall i \in V\tag{3}
$$

Here the first term is the number of service requests from all clients to WSI server i. The second term is the frequency that WSI server i sends Web services to the other WSI servers. The third term is the frequency that WSI server i receives Web services from other WSI servers. The fourth term is the product of the capacity of WSI server i and the binary decision variable of the selection of WSI server location $\nu _ { i } .$

## 2.4. WSP’s capacity and WSI assignment constraint

Often, multiple WSPs compete to provide Web services to a WSI. In the absence of considerations to the contrary, the WSI will choose those WSPs with low communication costs and fees to help minimize its operating costs. The following selection constraint insures the WSI does not contact any WSP that is not chosen for usage. In addition, a WSP also has a capacity constraint that limits its ability to process the WSI’s demand. This limit may be the result of a contract between the WSI and the WSP as well as the maximum physical server capacity of the WSP. This constraint therefore requires that no WSP can provide services more than its capacity permits.

$$
\sum_ {i \in V} u _ {i, w} \leq x _ {w} t _ {w} \quad \forall w \in W\tag{4}
$$

Here the term on the left is the number of service requests from all WSI servers to WSP w. The term on the right is the product of the capacity of WSP w and the binary decision variable of the selection of WSP w.

## 2.5. Client service constraint

This constraint insures the summation of all requests from a client should be equal to its service requirement.

$$
\sum_ {i \in V} u _ {c, i} = r _ {c} \quad \forall c \in C\tag{5}
$$

Here the term on the left is the number of service requests from client c to all WSI servers. The term on the right is the service level requirement of client c.

Tests using CPLEX show that the WSI location problem is unlikely to be solvable directly for large instances. Hence we turn to heuristics that we develop in the next section.

## 3. Heuristics development

The WSI location problem is a multi-service, capacitated, three-tiered server location problem with added constraints on bundling and sharing. Facility location problems are generally NP-Hard [7] and are therefore prohibitively difficult to solve when the problem size is big. Many exact algorithms have been developed for small versions of these problems. None of them, however, can be readily adapted to solve our problem because of its size and additional complicating constraints.

Much research has been devoted to develop efficient heuristic algorithms as a bridge between solution speed and solution optimality. Two of the predominant greedy construction heuristics are the ADD [14] and DROP [5] methods, which build solutions from scratch. An important greedy improvement heuristic is the Alternate Location-Allocation (ALA) [19] method which builds on an existing solution. The ADD procedure starts with all facilities closed and locates a facility that gives the greatest savings at each step and iterates through all potential locations until no further savings can be made. In contrast, DROP opens all facilities and removes a location that gives the greatest savings at each step and tries to find optimal or near optimum solutions at the end of the iterative procedure. ALA closes a facility from a feasible solution set at each step and uses one ADD step to optimize the problem. It stops when no improvement can be made. These heuristics are often used together and, in practice, they perform well. We propose an iterative heuristic method to locate WSI servers and WSPs. This method, which we call DAL, incorporates adapted versions of DROP, ALA, and LP relaxations of Integer Transportation (IT) problems. Fig. 1 outlines this procedure. As is typical when using heuristics, one can develop lower bounds to bound estimates on the performance of the heuristic, perhaps using duality methods. This may prove useful for large problems, although the quality of such lower bounds introduces additional uncertainty on these estimates.

When applying DROP and ALA to our problem, both treat the locations of WSI servers and WSPs equivalently when choosing one to drop or add. The only selection criterion is the saving that dropping or adding a location brings. This equal treatment is viable because both types of locations incur fixed costs or fees. If we limit our heuristic selections only to potential WSI server locations, we will need to solve, at each step, a multi-product transportation problem with the selection of WSPs as a decision variable. This is a difficult problem by itself, with integer constraints on both the selection of WSPs and the communication frequencies.

![](/api/attachments/QMKDAPEV/fulltext/images/bf220afa4579c7cfdd3f964a049a65ae7b2106976372be3f73d7cabd005985d7.jpg)  
Fig. 1. DAL heuristic flowchart.

Let there be a set of potential WSI servers and WSP locations $k { \in } K$ and a set of clients $c { \in } C$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$P_{k}=\left\{\begin{array}{ll}1 &amp; \text{if a location is selected at } k,\\ 0 &amp; \text{otherwise}\end{array}\right.$ 

K1 subset of K for which $P_{k}=1$

K0 subset of K for which $P_{k}=0$ $C^{*}(K,I)$ the optimal solution to an IT problem with source set K and sink set C

$C(K,I)$ the lower bound of an IT problem with LP relaxation of the integer constraints
</div>

on communication frequencies with source set and sink set.

## 3.1. DROP procedure

At the beginning of the DROP procedure, we include all WSPs and WSI server locations as an initial solution. This means all locations are in the set. The DROP procedure adapted from [22] as follows:

1. For each $k { \in } K 1$ compute $\sigma _ { k } { = } f _ { k } { + } C ( K 1 , I ) { - }$ $C ( K 1 \backslash \{ k \} , I )$ or $\sigma _ { k } { = } g _ { k } { + } C ( K 1 , I ) { - } C ( K 1 \backslash \{ k \} , I )$ depending whether location k is a WSI server or a WSP.

2. Find the location $k ^ { * }$ that maximizes $\sigma _ { k }$ from $\sigma _ { k } ^ { * } { = } \operatorname* { m a x } _ { k \in K 1 } \{ \sigma _ { k } \}$

3. If $\sigma _ { k } ^ { * } { > } 0 ,$ move $k ^ { * }$ from K1 to K2 and go to Step 1. Otherwise, terminate the procedure.

At step 1, there are |K1| IT problems to be solved. To reduce computer time, we approximate an optimal solution by relaxing the integer constraints on the communication frequencies and simplify the original IT problem to one with fixed selections of WSI server and WSPs locations and without integer constraints. The resulting LP relaxed problems are solved for lower bounds, which are then used to select locations to drop.

At the end of the DROP procedure, we solve an IT problem to obtain $C ^ { * } ( K , I )$ . If an integer solution is not available, the procedure will backtrack to previous location decisions iteratively until we find a feasible integer solution. If we returned to the initial solution to the problem and there is still no integer solution, then the problem does not have a feasible integer solution.

## 3.2. ALA procedure

Once a feasible integer solution is found, the solution set K1 will be passed to the ALA procedure to serve as an initial solution for further improvement. The ALA procedure is also adapted from [22] as follows:

1. Drop a $k ^ { \prime } { \in } K 1$ that has not been dropped before. Terminate when every location has been dropped once.

2. For each $k { \in } K 0$ compute, $\sigma _ { k } { = } C ( K 1 , I ) { - } C ( K 1 \cup$ $\{ k \} , I ) - f _ { k }$ or $\sigma _ { k } { = } C ( K 1 , I ) { - } C ( K 1 \cup \{ k \} , I ) { - } g _ { k } ,$ depending whether location k is a WSI server or a WSP.

3. Find the location $k ^ { * }$ that maximizes $\sigma _ { k }$ from $\sigma _ { k } ^ { * } { = } \operatorname* { m a x } _ { k \in K 0 } { \{ \sigma _ { k } \} }$

4. Solve $\overleftrightarrow { C } ^ { * } ( K 1 \cup \{ k ^ { * } \} , I )$ . If not feasible, add $k ^ { \prime }$ to K1 and go to Step 1.

5. If $\sigma _ { k } { = } C ^ { * } ( K 1 , I ) { - } C ^ { * } ( K 1 \cup \{ k ^ { * } \} , \operatorname { I } ) { - } f _ { k } ^ { * } { > } 0$ or $\sigma _ { k } { = } C ^ { * } ( K 1 , I ) { - } C ^ { * } ( K 1 \cup \{ k ^ { * } \} , I ) { - } g _ { k ^ { * } } { > } 0 $ , depending whether location k is a WSI server or a WSP, add $k ^ { * }$ to K1 and go to Step 1. Otherwise, add $k ^ { \prime }$ to K1 and go to Step 1.

There are |K0| IT problems to be solved at Step 2. To reduce computer time, we again relax the integer constraints on the communication frequencies. At Step 4, we verify that replacing $k ^ { \prime }$ with $k ^ { * }$ gives an integer solution by solving an IT problem.

## 4. Data collection and experiments

We design two representative test beds of problems, one for testing the performance of the DAL heuristics in terms of solution quality and computer time and one for testing a number of design hypotheses. Our experiments consist of the solutions to location problems using simulated data. Details related to the construction of these tests and various costs can be found in [23].

Some Web services applications may involve many participants spread over large areas. Problems of this type are challenging for any solution method. Hence an aggregation of individual locations to a city level is necessary. Forty cities on the US Internet backbone networks were selected as the potential locations for the participants (Fig. 2).

Communication/opportunity costs were derived from network latencies which were approximated by geographical proximity between locations on the network. Using geographical proximity in this study is justified. First, the selected cities are on Internet backbone networks with high bandwidths and there is a correlation between network latency and geographical distance [10]. Second, physical distance is not subjected to many external influences and provides a lower bound on network latency. Eventually physical distance will dominate as a measurement of network latency as other factors become progressively less relevant. We convert physical distance to communication cost in dollars by dividing distance by an appropriate factor.

To facilitate the generation of the two sets of problems, we assigned base values to the control parameters and varied these base values to simulate different scenarios and applications. The first test bed was used to study the solution performance of DAL. We benchmarked DAL against CPLEX 8 [11] which is a general-purpose commercial integer programming package that provides exact solutions. Because of its efficiency in solving IP/LP problems, CPLEX 8 was also used to solve the LP and IP sub-problems of DAL heuristics. All tests were conducted on a 933 MHZ and Windows 2000 computer. Different test scenarios were set up by varying the size of problems and the values of various control parameters. We considered eight classes (a to h) of problems defined by the number of clients, WSPs and the potential WSI server locations ranging from 5 to 40 (Table 2). In each class, there were eight instances defined by the combinations of the fixed costs of WSI server locations and WSP fixed fees, communication costs and dimensions of the Web services vectors (Table 3). Table 4 lists the base values for the efficacy tests. For every instance, the values of each parameter were randomly varied within a 40% range of the parameter’s base value as the medium.

![](/api/attachments/QMKDAPEV/fulltext/images/faa7a257f892647ec047d6dfd9a48809c4cbdcf9b719a49482756ec89d64c7a5.jpg)  
Fig. 2. US internet backbone networks with 40 city locations and connections.

Table 2  
Performance test classes

<table><tr><td>Class</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td><td>h</td></tr><tr><td>Number of WSPs, WSI Servers and Clients</td><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td><td>30</td><td>35</td><td>40</td></tr></table>

We were also interested in knowing how various factors would affect the optimal solutions in terms of the number of WSI servers and WSPs, and the number of Web services being shared between WSI servers. The factors under study included communication costs, the fixed costs of WSPs and WSI server locations, the number of client demands per period and the number of Web services sent at a time between WSI servers. We proposed five hypotheses to study the resulting design of the model.

Since network latency is considered as an opportunity cost, a WSI has an incentive to minimize it to reduce its overall operating costs. Facing clients who are sensitive to service delays, the WSI may alleviate the impact of the increased network latency costs by setting up more servers to be nearer to its clients and by contacting more WSPs near to its servers. This leads to:

H1. High latency costs and a large number of timesensitive clients will increase the number of WSI servers and WSPs required.

Modifying the values of WSI and WSP fixed costs may also influence the number of WSI servers and WSPs. Reduced fixed cost may make latency cost account for a larger portion of WSI operating cost. A WSI will have a bigger incentive to setup more servers and contact more WSPs to reduce the overall network latency. This gives:

Table 3  
Test instances for each class

<table><tr><td>Instance</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>WSI ( $f_i$ ), WSP ( $g_w$ ) fixed cost/fee</td><td>1500</td><td>1500</td><td>1500</td><td>1500</td><td>6000</td><td>6000</td><td>6000</td><td>6000</td></tr><tr><td>Factor to convert distance to communication cost</td><td>50</td><td>50</td><td>200</td><td>200</td><td>50</td><td>50</td><td>200</td><td>200</td></tr><tr><td>Dimensions of web services vectors (z)</td><td>2</td><td>8</td><td>2</td><td>8</td><td>2</td><td>8</td><td>2</td><td>8</td></tr></table>

Table 4  
Base values for performance test

<table><tr><td>Parameters</td><td>Base Value</td></tr><tr><td>WSP capacity ( $t_w$ )</td><td>5000</td></tr><tr><td>Value of each WSP service vector element</td><td>2</td></tr><tr><td>Number of web services incurring a full costs and capacity usage ( $p$ )</td><td>1</td></tr><tr><td>WSI capacity ( $s_i$ )</td><td>5000</td></tr><tr><td>Client demand ( $r_c$ )</td><td>1000</td></tr><tr><td>Value of each client service vector element</td><td>1</td></tr></table>

H2. Low WSI and WSP fixed costs will increase the number of WSI servers and WSPs required.

An increase in client demand may increase the overall communication costs and render the fixed costs less consequential. The WSI may take advantage of these <sup>b</sup>decreased<sup>Q</sup> fixed costs and expand its server locations and their contacts with WSPs. This gives:

H3. High client demand will increase the number of WSI servers and WSPs required.

Total sharing costs in Equation (P1) and capacity constraint (2) were computed assuming each Web service component incurred a single communication cost charge and utilized a single capacity unit (i.e., that p=1). This might not be realistic for many applications since often more than one service could be sent at a time. Given that sharing cost is a function of network latency rather than the number of Web services being sent at a time, sending multiple Web services at a time will lower the overall costs. That is, as p increases overall costs should decrease. The WSI servers may increase the number of Web services transferred to other servers giving:

Table 5  
Common base values for hypothesis test

<table><tr><td>Parameters</td><td>Base value</td></tr><tr><td>WSP fixed fee ( $g_w$ )</td><td>1000</td></tr><tr><td>WSI fixed cost ( $f_i$ )</td><td>1000</td></tr><tr><td>Factor to convert distance to communication cost</td><td>100</td></tr><tr><td>Dimension of web services vectors ( $z$ )</td><td>2</td></tr><tr><td>Client demand ( $r_c$ )</td><td>1000</td></tr><tr><td>WSP capacity ( $t_w$ )</td><td>5000000</td></tr><tr><td>WSI capacity ( $s_i$ )</td><td>5000000</td></tr><tr><td>Value of each element in WSP web services vector</td><td>2</td></tr><tr><td>Value of each element in client web services vector</td><td>3</td></tr><tr><td>Number of web services incurring a full costs and capacity usage ( $p$ )</td><td>5</td></tr></table>

Table 6  
Table 7  
Values of experiment parameters for hypothesis test

<table><tr><td>Tests</td><td>Factor to convert distance to communication cost</td><td>WSI ( $f_i$ ), WSP ( $g_w$ ) fixed cost</td><td>Client demand ( $r_c$ )</td><td>Number of web services sent at a time between WSI servers ( $p$ )</td></tr><tr><td>1</td><td>1</td><td>100</td><td>100</td><td>1</td></tr><tr><td>2</td><td>2</td><td>200</td><td>200</td><td>2</td></tr><tr><td>3</td><td>4</td><td>400</td><td>400</td><td>3</td></tr><tr><td>4</td><td>8</td><td>800</td><td>800</td><td>4</td></tr><tr><td>5</td><td>16</td><td>1600</td><td>1600</td><td>5</td></tr><tr><td>6</td><td>32</td><td>3200</td><td>3200</td><td>6</td></tr><tr><td>7</td><td>64</td><td>6400</td><td>6400</td><td>7</td></tr><tr><td>8</td><td>128</td><td>12,800</td><td>12,800</td><td>8</td></tr><tr><td>9</td><td>256</td><td>25,600</td><td>25,600</td><td>9</td></tr><tr><td>10</td><td>512</td><td>N/A</td><td>N/A</td><td>10</td></tr></table>

H4. The higher the number of Web services sent at a time between WSI servers the greater the number of WSI servers required.

H5. The higher the number of Web services sent at a time between WSI servers the greater the amount of sharing between WSI servers.

A second test bed of problems was used to study Hypotheses 1–5. For Hypothesis 1, 4 and 5 we conducted 5 sets of 10 tests. For Hypothesis 2 and 3 we conducted 5 sets of 9 tests. Within each set, the value of the parameters under investigation (i.e., communication costs, fixed costs, number of client demands per period, and factor p) were modified while others were held constant. Five sets of 17 potential locations for WSPs, WSI servers, and clients were randomly generated to be used for the tests.

Table 5 shows the common base values for these tests. We artificially increased the capacities of WSP and WSI to a large number to void their influences on the test results. For every problem, the values of each parameter were randomly varied within a 4% range with the parameter’s base value as the medium. Table 6 summarizes the modifications of the values of four experimental parameters. Up to 10 different values were assigned to each of them.

## 5. Experimental results

## 5.1. Efficacy test

A summary of the comparative study of the performance result, including solution quality and computer time, is presented in Table 7. For problems with 25 or more location choices (i.e., for classes e, f, g and h tests), CPLEX 8, with its default searching technique, often ran out of memory before finding optimal solutions or took excessive amounts of time to converge. We therefore only tested problems from class a to class e with CPLEX. The solutions of the DAL heuristics averaged a gap of about 0.38% of the optimum values for 34 problems. The maximum gap of these tests was about 2.88%.

We compared the <sup>b</sup>anytime<sup>Q</sup> performance of the DAL heuristics and CPLEX for problems where CPLEX did not find optimal solutions (6 problems in class e). For every one of these problems, CPLEX did not produce better solutions at the time when DAL terminated. CPLEX ran out of memory when solving two problems and its best solutions were worse than those of the DAL heuristics. We terminated CPLEX when solving four other problems after CPLEX ran for no less than 10 times the time that DAL used for the same problems. CPLEX gave two worse solutions and two better solutions compared with those of DAL heuristics.

Objective function value gap between DAL and CPLEX

<table><tr><td>Problem classes/number of locations</td><td>Average percentage gap between DAL and CPLEX (%)</td><td>Maximum percentage gap between DAL and CPLEX (%)</td><td>DAL average time (s)</td><td>DAL relative standard deviation (%)</td><td>CPLEX average time (s)</td><td>CPLEX relative standard deviation (%)</td></tr><tr><td>a/5</td><td>0</td><td>0</td><td>2</td><td>0</td><td>1</td><td>0</td></tr><tr><td>b/10</td><td>0.179</td><td>0.878</td><td>7</td><td>34.992</td><td>1.25</td><td>37.032</td></tr><tr><td>c/15</td><td>0.249</td><td>1.000</td><td>32.625</td><td>52.221</td><td>28.25</td><td>106.627</td></tr><tr><td>d/20</td><td>1.112</td><td>2.886</td><td>116.625</td><td>58.995</td><td>1358.875</td><td>140.469</td></tr><tr><td> $e/25^a$ </td><td>0.307</td><td>0.615</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Weighted Average</td><td>0.380</td><td>N/A</td><td>N/A</td><td>36.552</td><td>N/A</td><td>71.032</td></tr></table>

Only 2 problems instances are included.

Table 7 and Fig. 3 show that for problems with fewer than 15 location choices, CPLEX 8 was faster than DAL. However, for problems with 15 location choices or more, the computer times of CPLEX surpassed those of DAL. The computer times of CPLEX increased dramatically as the number of location choices continued to increase while DAL increased at more modest rate.

The results also demonstrate that on average the computer times of DAL varied much less across problems of similar size than CPLEX. We see in Table 7 the average relative standard deviation of DAL for the problems studied was about 36.55% while the one of CPLEX was 71.03%. Moreover, this table shows the relative standard deviations of DAL computer times increased at a lower rate than those of CPLEX. This suggests the computer times of DAL were more predictable than CPLEX.

## 5.1.1. Computer times by the dimensions of web services vectors

Table 8 and Fig. 4 present a summary of 64 tests of DAL computer times decomposed into two categories by the dimensions of the Web services vectors. They show that the DAL heuristics were sensitive to the dimensions, that is, to the size of the Web service vector. In general, higher dimensions made it more difficult to solve. Table 8 also illustrates the relative standard deviations of DAL computer times for problems of both dimensions were low. The average relative standard deviation was about 7.46% for two dimensions and 5.69% for eight dimensions.

![](/api/attachments/QMKDAPEV/fulltext/images/0b70e6d9ec1437449fddb50c70d24dff198addaebb6f0570bf5294b9d656f291.jpg)  
Fig. 3. Log of average computer times in seconds of DAL and CPLEX.

Computer times with two and eight dimensions of Web services vectors

<table><tr><td rowspan="2">Problem classes/number of locations</td><td colspan="2">Two dimensions</td><td colspan="2">Eight dimensions</td></tr><tr><td>DAL average time (s)</td><td>DAL relative standard deviation (%)</td><td>DAL average time (s)</td><td>DAL relative standard deviation (%)</td></tr><tr><td>a/5</td><td>20</td><td>0</td><td>2.00</td><td>0</td></tr><tr><td>b/10</td><td>4.75</td><td>10.52</td><td>9.25</td><td>5.40</td></tr><tr><td>c/15</td><td>16.75</td><td>5.71</td><td>48.50</td><td>4.29</td></tr><tr><td>d/20</td><td>52.50</td><td>10.37</td><td>180.75</td><td>3.94</td></tr><tr><td>e/25</td><td>141.50</td><td>9.41</td><td>536.75</td><td>6.72</td></tr><tr><td>f/30</td><td>292.25</td><td>6.62</td><td>1329.50</td><td>7.29</td></tr><tr><td>g/35</td><td>588.50</td><td>6.10</td><td>2846.00</td><td>13.67</td></tr><tr><td>h/40</td><td>1164.25</td><td>10.91</td><td>5520.50</td><td>4.24</td></tr><tr><td>Average</td><td>N/A</td><td>7.46</td><td>N/A</td><td>5.69</td></tr></table>

## 5.1.2. ALA performance

The DAL heuristics consist of DROP and ALA procedures. The DROP procedure finds a good feasible solution quickly and the ALA procedure attempts to improve it. It is important to know the performance of ALA since it solves a series of transportation problems and is time consuming. Table 9 summarizes the results of the comparative performance tests of the ALA and DROP procedures. It shows the average solution quality improvement of ALA over DROP was about 0.51%. For one instance, the improvement was over 5%. The overall improvement was not insignificant considering the average gap between DAL solutions and optimal solutions was only about 0.38%. Table 9 shows that the average computer times of the ALA procedure was about 48.63% of those of the DROP procedure. Considering the improvement of solution quality it made, ALA was a justified part of the DAL heuristics.

Log of Average DAL Computer Times with Different Dimentions of Web Services Vectors  
![](/api/attachments/QMKDAPEV/fulltext/images/05b47ac1182035239dd0cb90848ce162ca71699619c41e7857aa961578b1d247.jpg)  
Fig. 4. Log of average DAL computer times by dimensions of web services vectors.

Table 9  
Solution quality improvement of ALA over DROP

<table><tr><td rowspan="2">Problem classes/number of locations</td><td rowspan="2">Average percentage improvement of ALA over DROP (%)</td><td colspan="2">Solution quality improvement of ALA over DROP</td><td colspan="2">Average DROP and ALA computer times</td></tr><tr><td>Maximum percentage improvement of ALA over DROP (%)</td><td>DROP computer time (s)</td><td>ALA computer time (s)</td><td>Average percentage computer time of ALA over DROP (%)</td></tr><tr><td>a/5</td><td>0.661</td><td>5.288</td><td>1</td><td>1</td><td>100</td></tr><tr><td>b/10</td><td>0.001</td><td>0.012</td><td>4.875</td><td>2.125</td><td>43.589</td></tr><tr><td>c/15</td><td>0.455</td><td>2.225</td><td>23.000</td><td>9.625</td><td>41.847</td></tr><tr><td>d/20</td><td>0.166</td><td>1.331</td><td>84.500</td><td>32.125</td><td>38.017</td></tr><tr><td>e/25</td><td>0.219</td><td>1.107</td><td>242.625</td><td>96.500</td><td>39.773</td></tr><tr><td>f/30</td><td>0.523</td><td>3.003</td><td>569.375</td><td>241.500</td><td>42.414</td></tr><tr><td>g/35</td><td>0.841</td><td>2.294</td><td>1200.000</td><td>517.250</td><td>43.104</td></tr><tr><td>h/40</td><td>1.209</td><td>4.234</td><td>2383.000</td><td>959.375</td><td>40.259</td></tr><tr><td>Average</td><td>0.509</td><td>N/A</td><td>N/A</td><td>N/A</td><td>48.625</td></tr></table>

## 5.2. Hypotheses testing

Test results, in general, supported the hypotheses.

![](/api/attachments/QMKDAPEV/fulltext/images/cacf09b98ba85c676c906ccd171cecb69575a22ef989919e73a991ad6119c26f.jpg)  
Fig. 5. The number of WSI servers and WSPs for each latency costs decrement (higher values of the factor mean lower latency costs).

Fig. 5 shows that network latency costs were positively related to the number of WSI servers and WSPs and therefore supports H1. The correlations between the factor to transform latency to communication costs and the number of WSI servers and WSPs were -0.823 and -0.657, respectively, and were significant at the 0.01 level. This finding suggests that, facing clients who were sensitive to service delays, a WSI would set up more servers and contact more WSPs to better serve its clients.

Fig. 6 supports H2 by showing a negative relationship between the WSI and WSP fixed costs and the number of WSI servers and WSPs. The correlations were -0.784 and -0.693, respectively, and were significant at the 0.01 level.

![](/api/attachments/QMKDAPEV/fulltext/images/b21754dc1337d42faf3eb92852525c2013004751b1b4051e3425b0ff1c657901.jpg)  
Fig. 6. The number of WSI servers and WSPs for each WSP and WSI fixed costs increment.

![](/api/attachments/QMKDAPEV/fulltext/images/10a9b216772476a631196b599f6bd2ac313573f07ee2f0e3a16105e70041ab14.jpg)  
Fig. 7. The number of WSI servers and WSPs for each client demand increment.

Fig. 7 supports H3 by showing a positive relationship between client demand and the number of WSI servers and WSPs. The correlations between client demand and the number of WSI servers and WSPs were -0.546 and -0.779, respectively, and were significant at the 0.01 level.

Fig. 8 supports H4 by showing that the number of WSI servers increased gradually with an increase in the number of Web services sent at a time between WSI servers. The correlation between these two variables was 0.525 and was significant at the 0.01 level. We suspected that the WSI set up more servers to take advantage this lowered sharing costs. Fig. 9 supports H4 by showing that sharing between WSI servers increased dramatically as the number of Web services sent at a time between WSI servers increased. The correlation was 0.569 and was significant at the 0.01 level.

Number of WSI Servers and WSPs vs. Number of Shared Web Services Incurring a Full Cost and Capacity Charge  
![](/api/attachments/QMKDAPEV/fulltext/images/9aebcccaedc73936808bdcaf90a96fe6e9e82dffd14e0ef90413c16586c23824.jpg)  
Number of Shared Web Services Incurring a Full Cost and Capacity Charge  
Number of WSPs Number of WSI Servers  
Fig. 8. The number of WSI servers and WSPs for each increment in the number of shared Web Services incurring a full cost and capacity charge ( p).

![](/api/attachments/QMKDAPEV/fulltext/images/db48e53e4c38dd91141ead911b1b737a639dc9f260d9feaeaf5b0809d4694731.jpg)  
Fig. 9. Sharing between WSI Servers for each increment in the number of shared Web Services incurring a full cost and capacity charge ( p).

## 6. Conclusion, limitations and future research

In this research, we defined a Web services intermediary location problem and presented a mathematical model to describe it. We expect the model to be applied with modifications to many business applications that take advantage of the capability and versatility that Web services offer. We also developed an efficient heuristic method to find good solutions in reasonable execution times. For the problems tested, the DAL heuristics provided near optimal solutions in short computer times and with limited computer memory. We expect the heuristics to be used for similar location problems.

This model assumes a design-time location decision problem. Each decision is valid until there are changes in the customer base and demand, the number of and offerings by WSPs and the properties of WSI server locations. Nevertheless, one advantage of using DAL is evident when a previously solved problem has changes to the constraints on the locations of WSI servers and WSP and needs to be revolved. For example, if a WSI needs to set up an additional server, or a selected WSP no longer provides services, DAL can build on the solution to the original problem and compute the best location to drop or to add. This is particularly advantageous in rebalancing or finetuning decisions when needed. Another advantage of practical importance is that the DAL heuristics use less computer memory when compared with CPLEX 8 using <sup>b</sup>Best-bound search<sup>Q</sup> technique [11]. This allows DAL to be implemented on limited capacity computers where CPLEX may run out of memory for the same problems.

A series of simulated tests were conducted to discover the characteristics of the WSI location model. From the experiment, we were able to extract patterns that are instrumental in learning a WSI’s planning to minimize operating costs. We found that latency costs, client demand and number of shared Web services incurring a full cost and capacity charge ( p) were positively related the number of WSI servers and WSPs required. WSI and WSP fixed costs were negatively related with the number of WSI servers and WSPs. As expected, we also found that the higher the value p the greater the amount of sharing between WSI servers.

This was a preliminary study of WSI location problems and there were important limitations in our investigation. First, to study the efficacy of the DAL heuristics and the characteristics of the model, we used simulated data. Despite our best effort to generate reasonable and representative data, we acknowledge the study might benefit from using real life data. Second, to make the model manageable, we made certain assumptions that might or might not be generally true. For example, we assumed that clients chose not to contact WSPs directly for services. We also assumed all data were deterministic, including demands and the timing of demands. In future research, these assumptions may be relaxed and revisited.

Web services as a technology and WSI location problems are still in their infancy and, thus, a great deal remains for further development and refinement of their modeling and solution methodologies. Our model minimized the operating costs of a WSI. It assumed the buyers’ market was fully covered and all client demands were met. A natural extension to this model is one that studies a monopoly market in which a WSI seeks profit maximization by deciding which client to serve and how much to serve. In addition, the current model was designed for one-period planning of a WSI with the assumption that the values of all parameters would stay constant in future periods. However, this assumption can be easily violated by the dynamics of a customer base, the number of and offerings by WSPs and the properties of WSI server locations. New models are needed to assist the WSI to review and rebalance previous decisions to reflect changes.

## References

[1] W. Andrews, Predicts 2004: Web Services, Gartner Research (2003).

[2] P. Barford, J.-Y. Cai, J. Gast, Cache Placement Methods Based on Client Demand Clustering, Technical Report TR1437, University of Wisconsin at Madison, Madison, WI (2001).

[3] R. L. Carter, M. E. Crovella, Dynamic Server Selection Using Bandwidth Probing in Wide-Area Networks, Technical Report BU-CS-96-007, Boston University, Boston, MA (1996).

[4] Z. Fei, S. Bhattacharjee, E.W. Zegura, M.H. Ammar, A novel server selection technique for improving the response time of a replicated service, Proceedings of IEEE INFOCOM, San Francisco, CA, 1998.

[5] E. Feldman, F.A. Lehrer, T.L. Ray, Warehouse location under continuous economies of scale, Management Science 12 (1966) 670– 684.

[6] R.L. Francis, L.F. McGinnis, J.A. White, Facilities Layout and Location: An Analytical Approach, Prentice-Hall, Englewood Cliffs, NJ, 1992.

[7] M.R. Garey, D.S. Johnson, Computers and Antractability: a Guide to the Theory of NP-Completeness, W.H. Freeman and Company, New York, NY, 1979.

[8] M. Gilpin, Who has how many Web services? Forrester Research, 2004.

[9] J.D. Guyton, M.F. Schwartz, Locating Nearby Copies of Replicated Internet Servers, Technical Report CU-CS-762-95, University of Colorado, Boulder, CO (1995).

[10] J. Gwertzman, M. Seltzer, An analysis of geographical pushcaching, Proceedings of 5th IEEE Workshop on Hot Topics in Operating Systems, Orcas Island, WA, 1995.

[11] ILOG, CPLEX Division, Incline Village, NV, USA, ILOG CPLEX 8 User’s Manual, 2003.

[12] S. Jamin, C. Jin, A.R. Kurc, D. Raz, Y. Shavitt, Constrained mirror placement on the internet, Proceedings of IEEE INFOCOM, Anchorage, AK, 2001.

[13] J.M. Johansson, On the impact of network latency on distributed systems design, Information Technology Management 1 (2000) 183–194.

[14] A.A. Kuehn, M.J. Hamburger, A heuristic program for locating warehouses, Management Science 9 (1963) 643– 666.

[15] B.N. Levine, J.J. Garcia-Luna-Aceves, Improving Internet multicast with routing labels, Proceedings of International Conference on Network Protocols, Atlanta, GA, 1997.

[16] B. Li, M.J. Golin, G.F. Italiano, X. Deng, On the Optimal placement of Web proxies in the Internet, Proceedings of IEEE INFOCOM, New York, NY, 1999.

[17] L. Qiu, V.N. Padmanabhan, G.M. Voelker, On the placement of Web server replicasProceedings of IEEE INFOCOM, Anchorage, AK, 2001.

[18] S. Ram, S. Narasimhan, Database allocation in a distributed environment: incorporating a concurrency control mechanism and queuing costs, Management Science 40 (1994) 969–983.

[19] Y. Rapp, Planning of exchange locations and boundaries, Ericson Technics 2 (1962) 1– 22.

[20] S. Rho, S.T. March, Designing distributed database systems for efficient operationProceedings of Sixteenth Internationa Conference on Information Systems, Amsterdam, The Nether lands, 1995.

[21] A. Shaikh, R. Tewari, M. Agrawal, On the effectiveness of DNS-based server selectionProceedings of IEEE INFOCOM, Anchorage, AK, 2001.

[22] R. Sridharan, The capacitated plant location problem, European Journal of Operation Research 87 (1995) 203–213.

[23] Y. Sun, A Location Model for Web Services Intermediaries. Doctoral Dissertation, Warrington College of Business Admin istration, University of Florida, 2003.

![](/api/attachments/QMKDAPEV/fulltext/images/0cfd9c0cd7fade8b49a915412ebe6c40705775b9acead43a59b4d52c25a7961b.jpg)

![](/api/attachments/QMKDAPEV/fulltext/images/0288c0c604bea76c28199ce7c85a07256b62bb13f3ec5cdba5be62a61287586a.jpg)

Yi Sun is an Assistant Professor of Information Systems at the School of Business, California State University San Marcos. His degrees include BA degree from Foreign Affairs College in Beijing, China and PhD (Management Information Systems) from University of Florida. He has research interests in telecommunications, data mining and artificial intelligence, electronic commerce, applied operations research.

Gary J. Koehler is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida.
