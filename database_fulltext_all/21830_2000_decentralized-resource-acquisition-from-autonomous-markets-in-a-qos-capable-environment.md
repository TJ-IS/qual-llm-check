---
otero_id: 21830
otero_key: "A7F7DUA4"
title: "Decentralized resource acquisition from autonomous markets in a QoS-capable environment"
authors: "Spyros Lalis; Dimitris Papadakis; Manolis Marazakis"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00077-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decentralized resource acquisition from autonomous markets in a QoS-capable environment

Spyros Lalis <sup>a,b,)</sup>, Dimitris Papadakis <sup>a,b</sup>, Manolis Marazakis <sup>a,b</sup>

<sup>a</sup> Computer Science Department, UniÕersity of Crete, P.O. Box 2208, Heraklion, Crete, GR-71409, Greece Institute of Computer Science, Foundation for Research and Technology-Hellas, P.O. Box 1385, Heraklion GR-7110, Greece

## Abstract

We present a protocol for acquiring multiple resources that are traded through autonomous markets. Further, we describe the protocol’s application to and implementation in a prototype system that supports prioritized end-to-end QoS for applications invoking services over an ATM switch. The corresponding network and server resources are allocated to applications via auctions that are performed independently of each other. Finally, we investigate the effects of market autonomy and protocol design in the performance of the system by discussing results of experiments for alternative system configurations and workloads. q 2000 Elsevier Science B.V. All rights reserved

Keywords: Multi-resource allocation; Electronic trading; Auctions; Negotiation protocols; Distributed systems; End-to-end service provision; Workload dynamics

## 1. Introduction

With the growing standardization and increasing processing capacity of the electronic infrastructure, allocating resources at run time becomes practically feasible at a global scale. For instance, network providers could offer a variety of connectivity services that computer agents select and invoke dynamically. Similarly, a large number of institutions could export a multitude of electronic information and data processing services, to be used by a worldwide community of electronic clients. This could significantly promote the development of advanced applications in the areas of telemedicine, multimedia digital libraries, global distributed computing, electronic commerce, remote laboratories, and virtual enterprises.

On the other hand, the inherent openness of the Internet also leads to a highly inhomogeneous environment with numerous applications and a large number of authorities providing widely diversified services. This, in turn, makes automated service negotiation difficult, giving rise to two major technical challenges.

First of all, end-user requirements must be mapped and compared to what is actually being offered. This task can be simplified via appropriate information infrastructures supporting registration and searching of ‘‘electronic goods’’, as well as efficient translation of application requirements to combinations ofŽ . the properties of primitive services. Work on information ontologies 9 , metadata translation mecha-<sup>w</sup> <sup>x</sup> nisms 12 , knowledge exchange protocols 7 , goods<sup>w</sup> <sup>x</sup> <sup>w x</sup> description languages 32 , and QoS specification<sup>w</sup> <sup>x</sup> methods 11 contributes significantly in this direc-<sup>w</sup> <sup>x</sup> tion.

Secondly, efficient mechanisms are needed for contacting the underlying electronic services and performing allocation in a coordinated way. It must be noted that since resources are de facto distributed, these mechanisms cannot do better than centralized control. Moreover, in an open environment where there is little or no knowledge about future load, static assignment of resources to task classes is not an option so that allocation decisions have to be taken dynamically as application requests arrive. The market paradigm receives considerable attention in distributed systems aiming for flexible and efficient resource allocation 2,10,30 . Resources and services <sup>w</sup> <sup>x</sup> are valued according to the rules of supply vs. demand, and allocation of goods is typically achieved using automated trading mechanisms, most notably auctions 16,28 .<sup>w</sup> <sup>x</sup>

In this paper, we present a protocol for acquiring multiple resources that are traded in autonomous markets. Our key assumption is that in a global electronic ecosystem, no central authority is responsible or capable of coordinating all trading activities. Instead, trading is performed via different markets that exist and operate independently of each other. Furthermore, we show how this protocol is applied in the context of a prototype system to provide prioritized end-to-end QoS for applications requiring simultaneous allocation of two resources — server and network capacity. Through a series of experiments, we study the performance of the protocol under conditions of resource scarcity. It is shown how internal market tie-breaking policy can lead to increased communication overhead and non-optimal allocation. An equally important finding is that protocol performance depends on the relative occurrence of application classes, at a constant aggregate load. These phenomena are of particular interest for mechanism designers who wish to build robust distributed systems. This work is being further pursued in the context of a facility supporting flexible service composition in an open environment 15 .<sup>w</sup> <sup>x</sup>

The rest of the paper is organized as follows. Section 2 describes the resource acquisition protocol.

The prototype system employing this protocol is presented in Section 3. The experiments that have been conducted using this system are discussed in Section 4. In Section 5, an overview of related work is given, identifying parallels and differences with our approach. Finally, Section 6 concludes the paper and gives future directions.

## 2. Marketplace model and acquisition protocol

As the backbone of a distributed marketplace, we postulate a global directory for locating markets. When a market for trading an electronic service is created, it is registered in the directory, and conversely, it is removed from the directory when it is no longer needed. Via the directory, provider-agents Ž . Ž . sellers and application-agents buyers locate markets for placing service offers and requests, respectively.

Markets are autonomous, opaque objects that may reside anywhere in the network. Each market is responsible for a single type of resource, and operates in isolation, i.e., its does not communicate with other markets to coordinate activities. Trading is assumed to occur in a closed, persistent, single-shot fashion, without any communication and thus, ‘‘real’’ price negotiation between sellers and buyers. Agents may place, at most, one bid in each market, which remains valid unless it is either accepted or explicitly recalled. In the former case, the market notifies agents via a contract message, which they either acknowledge or cancel. Agents may also cancel a bid anytime, without waiting to receive a contract. An efficient implementation of such a matchmaking mechanism is the continuous double auction, which allows buyers to make offers and sellers to accept offers at any particular time. Each auction is cleared according to Ž . M<sup>q</sup>1 st price rules 24 , which is a<sup>w</sup> <sup>x</sup> generalization of the second price Vickrey 29 auc-<sup>w</sup> <sup>x</sup> tion for the sale and purchase of multiple units of a good. It must be underlined, however, that Vickrey auctions have limitations 20 , most notably when <sup>w</sup> <sup>x</sup> agents have reason to lie about their true valuations of a good. In this paper, we assume that this is not the case.

Thus, to acquire a resource of interest, agents have to locate the markets trading this resource, place their bid, and wait for the market to respond. An agent wishing to acquire multiple resources submits bids to several markets. Since these may not be matched simultaneously, agents have to employ a protocol to achieve the desired bundling of resources.

Assuming that R is the set of resources to be acquired, and that agents maintain a contract set $C ,$ the following protocol is proposed.

Ž . 1 For each resource r in R, create a bid $b _ { r }$ and place it in market m where resource r is being traded.

Ž . 2 Initialize C to empty, record the current time t, set a timer to expire at $t + T _ { w }$ , and suspend hence,Ž the agent remains suspended for, at most, $T _ { w } )$

Ž . 3 Upon receipt of contract message $c _ { r } .$ , add $c _ { r }$ in C. Then, check whether for each $r$ in R, there is a corresponding contract $c _ { r }$ in C. If this is indeed the case, acknowledge all contracts, return C to the application, and deactivate the timer. Else, suspend.

Ž . 4 If the timer expires, then, for each contract $c _ { r }$ in $C ,$ send a message to market $m _ { r }$ , canceling the contract and requesting that bid $b _ { r }$ be reconsidered in the next market clearing this is equivalent toŽ re-placing $b _ { r }$ with a new identical bid $b _ { r } ^ { \prime } )$ . Then, wait for markets to clear again, i.e., go to step 2 .Ž .

This protocol works well when there are plenty of resources available in the system. Each agent immediately succeeds in allocating the complete resource bundle, because it can acquire all requested resources from each individual market. Moreover, the protocol overhead is low in terms of blocking and number of messages exchanged. Establishing a bundle requires exactly $3 * | R |$ messages, because three messages are needed for each transaction bid placement, contractŽ notification, and contract acknowledgement . Since. markets are contacted simultaneously and trading occurs in parallel, agents are blocked at most for max $( T _ { m } ) _ { \ l }$ , assuming that each market m has a clearing period of $T _ { m }$ Žand ignoring message propagation delay . For the same reason, the maximum time that. elapses between the arrival, the acknowledgement, and the activation of a contract is $\operatorname* { m a x } ( T _ { m } )$

On the other hand, increased communication and non-optimal allocation may occur when resources are scarce. Due to the fact that it is impossible to match all bids, an agent may succeed in acquiring only a strict subset R of R. Although it is guaranteed that each r in R will be released, this happens at the cost of sending $\left| R ^ { \prime } \right|$ cancellation messages. As a more important consequence, each resource r in R remains unavailable for trade in market $m _ { ( r ) }$ during $n + 1$ clearing periods, where $0 \leq n \leq T _ { w } / \dot { T } _ { m r }$ . This resource unavailability, though temporary, may result in lost opportunities for other agents. Moreover, agents bidding in the same markets may be granted resources in such a way that neither establishes its bundle, even though this would be feasible for some of them.

It can be argued that this protocol is appropriate only for lightly loaded systems. Nevertheless, we are interested in investigating its performance for occasional traffic bursts that cause increased competition for system resources, for short periods of time. This is important for open systems where application traffic is not known a priori and may vary unpredictably. In a first attempt to study the protocol’s performance, we restrict ourselves to the ideal case where agents and markets execute in perfect synchrony with each other. In other words, when cancellations occur, only a single market clearing is lost, namely the one that returned the contract being canceled, and the corresponding resources become available for trade during the next clearing period.

## 3. System architecture and application structure

The described protocol has been implemented in a working prototype system. Fig. 1 shows the overall system architecture. The system comprises underlying services providing guaranteed quality of service. It also features a marketplace for trading resources and a brokerage mechanism for bundling together resources according to application requirements. The main motivation for employing the market paradigm is to guarantee differentiated QoS for a dynamically evolving society of users where it is difficult to assign priorities statically.

Two types of primitive services are considered: servers and a network connecting servers to applications. Each service is represented via a QoS manager that is responsible for controlling its resources. To invoke a service, applications must send a request along with a description of the desired performance characteristics to the corresponding QoS manager. In the current implementation of the system, servers are stream transmitters that continuously send data, at a rate specified by the application. The network is an ATM switch connecting the server machines to the workstations where the application resides. For simplicity, QoS is specified in integer quantities while providers and consumers may offer and request for, respectively, several units thereof.

![](/api/attachments/A7F7DUA4/fulltext/images/dd45ad79c50039b9d453543a2ff670267d1879a6f4482da95a588342fdeca8f5.jpg)  
Fig. 1. System architecture.

Applications running on top of the system request data to be generated by a server and transferred over the network, at a given rate. Once an application manages to acquire both the corresponding network and server resources from the marketplace, a connection is opened between the application and the server, and data transmission is initiated with calls to the respective QoS managers. After a random period of time, transmission is stopped and the connection is closed, thereby releasing the corresponding resources. Applications have a budget for acquiring resources, which reflects their precedence over other applications. It is presumed that users on whose behalf applications execute are endowed this budget through an external mechanism, e.g., an authentication procedure.

The marketplace is a virtual space where markets responsible for trading services reside. Each market executes its matchmaking process independently of other markets. The default trading mechanism is continuous double auction. QoS managers register with the marketplace via a sell order, describing the service being offered. If a market for trading this type of service already exists, the order is placed in that market; else, a new market is created for this service. When it is no longer desirable to trade a service through the marketplace, the QoS manager sends a cancel request, thereby invalidating the respective sell orders that were issued earlier.

The broker is an agent acting as a mediator between applications services and the marketplace. It receives from applications a list of resource descriptions, allocates a corresponding resource bundle, and sends back the respective contracts. In the current implementation, there is a single broker agent to which all applications send their allocation requests. However, application requests are handled asynchronously to each other within the broker so that, in principle, each application is assumed to spawn its own agent. Coordinated resource acquisition is implemented using the protocol described in Section 2.

## 4. Experimental observations

Initial experiments that discuss the properties of the protocol for application classes with different priorities can be found in Ref. 14 . For reasons of<sup>w</sup> <sup>x</sup> completeness, an analogous set of experiments illustrating the performance of two application classes with different budget is also presented here. As it becomes evident, resource scarcity is a ‘‘local’’ class phenomenon. For this reason and since we wish to study the performance of the protocol under contention, subsequent observations are made based on application traffic with the same priority. More specifically, the second series of experiments investigates the behavior of the system in the presence of a homogeneous load, i.e., requests of a single application class. A third series of experiments is performed for the case of two applications with overlapping resource requirements.

Protocol performance is studied as a function of the method used within markets to select a single bid among two or more equal bids when it is impossible to match all of them. Two different methods are compared to each other: random selection and selection based on timestamps. For obvious reasons, we refer to them as random and timestamp tie-break, respectively. The latter is implemented by assigning timestamps to applications and including these timestamps in bids.

The workload used in the presented experiments is a heavy load traffic pattern with bursts, thereby driving the system through phases of contention. It is shown, however, that the degree of performance degradation depends on the tie-breaking method used. The traffic pattern of the workload was generated using an exponential distribution for the arrival process and a uniform distribution for request duration. The amount of resources requested by each application is constant, and equal to a single QoS unit, both for the servers and the network.

![](/api/attachments/A7F7DUA4/fulltext/images/19b91e6433df37657c2d02ed56238d9e617af3608492c8d4553be2eaafa21335.jpg)  
Fig. 2. $\mathrm { C } _ { 1 }$ backlog for random and timestamp tie-break.

![](/api/attachments/A7F7DUA4/fulltext/images/7b507d58af53360717970ea742c51ffef9b9124d2898f9cbd6a298270f400c76.jpg)  
Fig. 3. $\mathrm { C } _ { 1 }$ cancellations for random and timestamp tie-break.

System performance is expressed in terms of the number of application blocked requests waiting for a resource bundle, referred to as the backlog, and the number of contract cancellations. Measurements are displayed as time series for successive market clearings. Thus, in all subsequent figures, the horizontal axis represents successive points in time, and the vertical axis represents the number of cancellations and blocked application requests, respectively.

## 4.1. Competition between applications with different priority

A first series of experiments is conducted to observe the differentiated handling of requests with different priority. Two application classes, $\mathrm { C } _ { 1 }$ and $\mathbf { C } _ { 2 }$ , with different budgets are used. Class $\mathrm { C } _ { 1 }$ has a lower budget than $\mathbf { C } _ { 2 }$ , and both compete for the same resources network and server . Each applica- Ž . tion class accounts approximately for half of the total traffic load.

The request backlog and cancellations per tiebreaking method and for each application class are depicted in Figs. 2–5. The aggregate backlog and cancellations per tie-breaking method are shown in Figs. 6 and 7. By observing the class backlogs, it can be concluded that class $\mathbf { C } _ { 2 }$ consistently enjoys better service than class $\mathrm { C } _ { 1 }$ . Moreover, traffic bursts result in significant performance degradation for class $\mathrm { C } _ { 1 }$ but hardly affect class $\mathrm { C } _ { 2 } .$ . This is because resources are allocated to the high-bidding class first. In other words, the $\mathbf { C } _ { 2 }$ class experiences performance degradation only when it is already occupying all system resources. The $\mathbf { C } _ { 2 }$ backlog depicted in Fig. 4 indicates, however, that some traffic bursts lead even the $\mathbf { C } _ { 2 }$ class in overload. The price of prioritized allocation in favor of class $\mathbf { C } _ { 2 }$ is an increased resource scarcity for class $\mathrm { { C } } _ { 1 } .$ . Since only a fraction of the system resources remains available for $\mathrm { C } _ { 1 }$ after the $\mathbf { C } _ { 2 }$ requests have been matched, $\mathrm { C } _ { 1 }$ is particularly vulnerable to traffic bursts; hence, the significant $\mathrm { C } _ { 1 }$ backlog shown in Fig. 2.

![](/api/attachments/A7F7DUA4/fulltext/images/49fa327d329e9d7fe27404df0b701e90b64a18f7028fbc085156882c29a4ef56.jpg)  
Fig. 4. C backlog for random and timestamp tie-break. <sub>2</sub>

It is important to note that the choice of the tie-breaking method does not gravely affect the performance of class $\mathbf { C } _ { 2 }$ . But it does have an impact on class $\mathrm { C } _ { 1 : }$ , in which case timestamp tie-break performs better than random tie-break. As it can be inferred from Figs. 3 and 5, random tie-break also results in contract cancellations, considerably more for class $\mathrm { C } _ { 1 }$ than for $\mathrm { C } _ { 2 }$ . This is due to the fact that tie-breaking comes into play for the class experiencing resource scarcity. The subsequent sections discuss this effect in greater detail. Notably, the difference between the two tie-breaking methods is also reflected on the overall performance, as illustrated in Figs. 6 and 7.

![](/api/attachments/A7F7DUA4/fulltext/images/69eb0d7cc8848e484cee07226c196d453fd96e525f9ddb4ffe9a68a81a9fc3ee.jpg)  
Fig. 5. $\mathrm { C } _ { 2 }$ cancellations for random and timestamp tie-break.

![](/api/attachments/A7F7DUA4/fulltext/images/371dc809a9cd20563429b6ad6780d8aaa2ea9aed62fe947d3ec649bacbd68dca.jpg)  
Fig. 6. Total backlog for random and timestamp tie-break.

## 4.2. Contention effects for homogeneous traffic

To expose the behavior of the protocol under situations of contention, in isolation from the differentiation between application classes with different priorities, we present a series of experiments for homogeneous traffic. In other words, requests of a single application class, C, are submitted to the system, requesting both network and server capacity. Apart from this difference, the workload has the same aggregate characteristics as the one used in the previous experiments.

![](/api/attachments/A7F7DUA4/fulltext/images/d27c87f987c76ab72c76aa1b49cddf56455bd4b3ce75c0fe951d6e88ce3eaf03.jpg)  
Fig. 7. Total cancellations for random and timestamp tie-break.

![](/api/attachments/A7F7DUA4/fulltext/images/57b85cf923d4b718b08ad8e98ac1eb55505158b023dc0a58d13d4b435e0b9bef.jpg)  
Fig. 8. C backlog for random and timestamp tie-break.

The request backlog for each of the two tie-breaking methods is depicted in Fig. 8 while Fig. 9 shows the respective cancellations. In accordance to the previous observations, random tie-break leads to numerous contract cancellations, while no cancellations occur when timestamp tie-breaking is used. By comparing the respective backlogs, it also becomes clear that cancellations are not merely an internal overhead, but do lead to a noticeable backlog increase.

The reason is that with random tie-break, there is no predefined sequence according to which equal bids are matched. This can be viewed as a special case of uncoordinated trading under resource scarcity, which was stressed in Section 2. For the simple scenario where two applications compete for a single bundled QoS unit, this means that one of them can acquire the free network slot while the other acquires the free server slot. As a consequence, an allocation opportunity is lost; both cancel their contracts and remain blocked. It is important to note that the probability of having allocation conflicts, and thus cancellations, increases with growing resource scarcity. This also explains why random tie-break leads to worse performance for homogeneous traffic than for a blend of applications with the same resource requirements but different priorities, as it can be verified by comparing the respective backlogs in Figs. 6 and 8. Indeed, in the former case, the number of requests that have equal priority and compete for the same resources is less than in the latter case.

![](/api/attachments/A7F7DUA4/fulltext/images/3854c967bfc9407619e51d67e6d8a8ddd4270f571983bd238f8892fdcc69b44e.jpg)  
Fig. 9. C cancellations for random and timestamp tie-break.

![](/api/attachments/A7F7DUA4/fulltext/images/6fde3ea86b9a347c9a5faf99bb15cdb54c03cbae174741d653f18af3bf6caa0b.jpg)  
Fig. 10. $\mathrm { C } _ { 1 }$ backlog for random and timestamp tie-break.

With the timestamp tie-break, despite the fact that markets perform matching independently from each other, selection between equal bids is done according to a global order. The result is that either all or none of the application’s bids are matched, thereby eliminating conflicts within an application class. When employing the timestamp tie-break method, the performance for homogeneous traffic thus has to be comparable to the performance obtained for the aggregated load of the previous experiments. This can be seen clearly in Figs. 6 and 8.

## 4.3. Contention effects for inhomogeneous traffic

Timestamp tie-break is a better choice for homogeneous traffic, but this is not necessarily the case in the presence of several application classes with overlapping resource requirements. To demonstrate this, we present a third series of experiments, for a balanced traffic mixture of two application classes, $\mathrm { C } _ { 1 }$ and $\mathrm { C } _ { 2 }$ . Both classes compete for the same networkŽ . but request for two different types of server resources, say $\mathbf { S } _ { 1 }$ and $\mathbf { S } _ { 2 }$ , which are traded in different markets. The aggregated capacity of $\mathbf { S } _ { 1 }$ and $\mathbf { S } _ { 2 }$ equals the total server capacity available in the previous experiments.

![](/api/attachments/A7F7DUA4/fulltext/images/0670ae2beeae41295b3dda775993d4e6614384468c5bac416a3576aeac909950.jpg)  
Fig. 11. $\mathrm { C } _ { 1 }$ cancellations for random and timestamp tie-break.

![](/api/attachments/A7F7DUA4/fulltext/images/3e56bd99b24d9d611b10bdc7929ea995730858b381f8696d370a3cd568401985.jpg)  
Fig. 12. $\mathrm { C } _ { 2 }$ backlog for random and timestamp tie-break.

Figs. 10–13 show the request backlog and cancellations per tie-break method and for each class. The aggregated values are given in Figs. 14 and 15. As it can be seen, the overall difference between the two tie-breaking methods is strikingly small. Furthermore, it is important to note that the timestamp tie-break method results in cancellations, too, to an amount that is comparable to the number of cancellations produced with random tie-break.

This is because, while preventing cancellations within each class, timestamp tie-break causes cascading cancellations at a global level. To give an example, suppose that a burst of $\mathrm { C } _ { 1 }$ requests leads class $\mathrm { C } _ { 1 }$ to overload i.e., there are not enoughŽ $\mathbf { S } _ { 1 }$ resources while only a few. $\mathbf { C } _ { 2 }$ requests follow. Let us also assume that the aggregate $\mathrm { C } _ { 1 }$ and $\mathrm { C } _ { 2 }$ load cannot be sustained by the commonly used resource, namely the network. In this case, $\mathrm { C } _ { 2 }$ requests cannot acquire the network resource because it is allocated to $\mathrm { C } _ { 1 }$ requests, in timestamp order. But $\mathrm { C } _ { 2 }$ requests do acquire the server resource $\mathbf { S } _ { 2 }$ and are forced to cancel the corresponding contracts. In turn, several $\mathrm { C } _ { 1 }$ requests that were granted the network resource fail to acquire the server resource $\mathrm { \bf S } _ { 1 }$ , which is a resource bottleneck for class $\mathrm { C } _ { 1 }$ , and thus cancel, too. This process is repeated until the $\mathrm { C } _ { 1 }$ requests holding back the $\mathbf { C } _ { 2 }$ requests finally succeed to acquire the server resource. In the meantime, the backlog of $\mathbf { C } _ { 2 }$ requests may build up to a critical level, thereby perpetuating this phenomenon, with the roles of class $\mathrm { C } _ { 1 }$ and class $\mathbf { C } _ { 2 }$ being reversed. A more detailed discussion is given in Ref. 13 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/A7F7DUA4/fulltext/images/93df0503cde2d3c6b2e707b9a5b4ff093f65a9052b63292a8b2a65f1dbbfa775.jpg)  
Fig. 13. $\mathrm { C } _ { 2 }$ cancellations for random and timestamp tie-break.

![](/api/attachments/A7F7DUA4/fulltext/images/e240624024edd5abf65afbdfd6e97697ec790ba5fb7e00983ecd5edb679b6cd8.jpg)  
Fig. 14. Total backlog for random and timestamp tie-break.

With random tie-break, cancellations occur due to the reasons stated earlier. However, given the relative occurrence of $\mathrm { C } _ { 1 }$ and $\mathbf { C } _ { 2 }$ , this method statistically avoids almost as many conflicts at a global level, i.e., between the two classes, as it introduces at a local level, i.e., within each class. This compensation effect leads to an overall performance, in terms of backlog and cancellations, similar to the one measured for timestamp tie-break, a fact that is illustrated in Figs. 14 and 15.

![](/api/attachments/A7F7DUA4/fulltext/images/fb9e723b7ca3e09b7ae1c5fc6e77217d900a3c1aa6e916ae28dd9be4e6c0f4c4.jpg)  
Fig. 15. Total cancellations for random and timestamp tie-break.

It is also interesting to observe that each tie-break method favors a different class. More specifically, random tie-break works better for class $\mathbf { C } _ { 2 }$ , whereas timestamp tie-break gives better results for class $\mathbf { C } _ { 1 } .$ Besides statistical deviations, the main reason is that the workloads used in these experiments have a few more $\mathrm { C } _ { 1 }$ than $\mathrm { C } _ { 2 }$ requests. This introduces more contention in class $\mathrm { C } _ { 1 : }$ , which is a situation where timestamp tie-break performs better than random tie-break. Conversely, given a $\mathrm { C } _ { 1 }$ overload, random tie-break results in better performance for class $\mathrm { C } _ { 2 } .$

It can be concluded that the relative occurrence of application classes affects performance considerably, making it possible for random tie-break to outperform timestamp tie-break, and vice versa.

## 5. Related work

The problem of distributed resource allocation has been widely studied in the context of meeting protocols and agent coalitions 23,25,26 . This work deals<sup>w</sup> <sup>x</sup> with the problem of a ‘‘homogeneous’’ group of nodes, each managing a set of resources of the same type. Nodes negotiate with each other to coordinate resource allocation and scheduling of tasks. Instead, we focus on the case where the authorities, through which resources are acquired, do not communicate with one another other to coordinate trading. Coordination must therefore be achieved by a separate software component, employing an appropriate protocol.

Another coordination metaphor is proposed in Ref. 19 . Individual resources use a calendar for <sup>w</sup> <sup>x</sup> arranging their schedule while external clients may lock a time slot when they commit to using the associated resource during that period. A two-phase commit protocol 8 is used to atomically reserve<sup>w</sup> <sup>x</sup> slots for all resources. However, although calendars do not communicate with each other, their entire state is available for anyone to access. This clearly creates many optimization opportunities. In our implementation, the broker agent has no knowledge of the internal market states, and coordination is achieved using a simpler protocol.

Our prototype uses auctions for allocating individual resources to applications. Auctions of various types have been applied to a wide range of resource allocation problems arising in distributed systems. However, most of these works have been concerned with allocation of a single item, such as processing time 30 , communication bandwidth 5 , access to<sup>w</sup> <sup>x</sup> <sup>w x</sup> data 6 or network information services 17 . Our work is concerned with allocating multiple resources in a single bundle, when each resource has to be acquired from a different market. Notably, auction mechanisms for allocating multiple items 4,28 do <sup>w</sup> <sup>x</sup> not address this problem. In this case, it is assumed that offers regarding all goods are forwarded to a central authority, which can take optimal allocation decisions since all relevant state information of the global market are available locally.

Work has also been done in developing software components that can be used to build an electronic economy. For instance, the Michigan AuctionBot <sup>w</sup> <sup>x</sup> 34 is a configurable trading environment capable of supporting various types of auctions, such as double auction which is being used in our prototype. The Auction Manager 18 , developed in the context of<sup>w</sup> <sup>x</sup> the University of Michigan Digital Library project, is designed to support creation of auctions, matching of agents to auctions, and notification of agents upon creation of new auctions that match their interests. A distributed version of this service could be used to implement the directory of a global marketplace. In our system, we rely on a much simpler marketplace structure to locate market objects, since the only items of trade are integer QoS values.

Further, Ref. 3 presents an architecture to sup-<sup>w</sup> <sup>x</sup> port a variety of commerce transaction types, from simple direct buying and selling to complex multiagent contract negotiations. In this case, markets for specific commodities are hosted in ‘‘exchanges’’, which are network-accessible resources that support a set of markets and provide common services. Market services are delivered to a participating agent through a ‘‘market session’’ that encapsulates the state of all interactions in the process of contracting with other agents. This functionality corresponds to the broker component of our architecture, which handles the details of establishing resource bundles on behalf of applications.

Negotiation and bidding policies have been investigated extensively in the framework of automated contracting among agents 21,27 . An important ob- <sup>w</sup> <sup>x</sup> servation is that protocols allowing agents to decommit may lead to desirable states that cannot be achieved without this option 22 . Our work presents <sup>w</sup> <sup>x</sup> a simple routine with no adjustment possibility, rather than a strategy for self-interested agents. However, although in a much simpler context, the presented protocol employs de-commitment to release resources in case of a failed attempt to acquire a resource bundle.

Our results indicate that uncoordinated operation of multiple independent markets poses non-trivial problems in achieving efficient allocation of resource bundles in the presence of contention. In this respect, the concept of market-oriented programming 33 in<sup>w</sup> <sup>x</sup> combination with simulation environments for computational economies 1 can be valuable for deter-<sup>w</sup> <sup>x</sup> mining the properties of resource allocation interactions. In particular, Ref. 31 discusses convergence <sup>w</sup> <sup>x</sup> of bidding policies for auctions in a setting involving bundling of multiple items under resource scarcity. It is shown that economies with certain properties eventually reach quiescence at a desirable state, but this may require multiple negotiation rounds. There are also economies that apparently do not converge.

## 6. Conclusions and future work

We have presented a protocol for acquiring distinct resources from autonomous markets, indicating important performance issues. We have shown how this protocol is employed to achieve market-based end-to-end resource in a working prototype system, and discussed the results of experiments, further elaborating on its performance under overload. It has been shown that the tie-breaking method used by individual markets to select among equal bids, along with the relative occurrence of application classes with the same budget, affects performance significantly.

We consider building adaptive systems as a promising direction for future work. Regarding the problem of multiple resource allocation, flexibility can be introduced at various levels. Markets can be operated via intelligent agents that record trading history. This information can be used to enhance the market tie-breaking mechanism, giving ‘‘reliable’’ agents precedence over ‘‘unreliable’’ agents that frequently cancel their contracts. Further, the protocol itself can be extended, e.g., to back off when conflicts are detected, much like this is done to avoid collisions is common carrier networks. A more detailed performance analysis is also in place, with focus on the asynchrony that can be introduced by variations in market clearing frequency and message propagation delay.

Finally, for the case where trading is performed within a controlled domain, e.g., a portal, or a network of portals, it is imaginable to implement mechanisms for the dynamic generation of mediator agents. Their role would be to acquire quantities of primitive resources from existing markets and then, themselves using a market mechanism, offer bundles thereof to the clients of the system. Determining the proper threshold for triggering the creation and destruction of such intermediaries, and devising strategies for a dynamic selection of resource palettes that might bring profit in the future, are challenging issues.

## References

<sup>w</sup> <sup>x</sup> 1 J.Q. Cheng, M.P. Wellman, The WALRAS algorithm: a convergent distributed implementation of general equilibrium outcomes, Computational Economics 1997 to appear; avail- Ž . able via URL http:<sup>rr</sup>auction.eecs.umich.edu.

<sup>w</sup> <sup>x</sup> 2 S.H. Clearwater Ed. , Market-Based Control: A ParadigmŽ . for Distributed Resource Allocation, World Scientific, 1995.

<sup>w</sup> <sup>x</sup> 3 J. Collins, S. Jamison, B. Mobasher, M. Gini, A market architecture for multi-agent contracting, Technical Report 97-15, University of Minessota, 1997.

<sup>w</sup> <sup>x</sup> 4 R. Demange, D. Gale, M. Sotomayor, Multi-item auctions, Journal of Political Economy 94 4 1986 863–872.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 D.F. Ferguson, C. Nikolaou, Y. Yemini, An economy for flow control in computer networks, in: Proc. IEEE Infocom ’89, IEEE Computer Society Press, Washington, DC, 1989, pp. 110–118.

<sup>w</sup> <sup>x</sup> 6 D.F. Ferguson, C. Nikolaou, Y. Yemini, An economy for managing replicated data in autonomous decentralized systems, in: Proc. ISADS’93, International Symposium in Autonomous Decentralized Systems, IEEE Computer Society Press, Los Alamitos, CA, 1993, pp. 367–375.

<sup>w</sup> <sup>x</sup> 7 T. Finnin, R. Fritzson, D. McKay, A language and protocol to support intelligent agent interoperability, in: Proc. CE& CALS Washington ’92 Conference, 1992.

<sup>w</sup> <sup>x</sup> 8 J. Gray, Notes on database operating systems,Operating Systems: An Advanced Course, Springer-Verlag, 1978.

<sup>w</sup> <sup>x</sup> 9 N. Guarino, Formal Ontology and Information Systems, in: N. Guarino Ed. , Formal ontology in information systems,Ž . Proc. of the 1st International Conference, IOS Press, Trento, Italy, 1998, June.

<sup>w</sup> <sup>x</sup> 10 B.A. Huberman, The Ecology of Computation, North-Holland, 1988.

<sup>w</sup> <sup>x</sup> 11 V. Issarny, C. Bidan, F. Leleu, T. Saridakis, Towards specifying QoS-enabling software architectures, in: Proc. IWQOS ’97, Fifth International Workshop on Quality of Service, New York, 1997.

<sup>w</sup> <sup>x</sup> 12 C. Lagose, C.A. Lynch, R. Daniel Jr., The Warwick framework: a container architecture for aggregating sets of metadata, Technical Report TR96-1593, Cornell Computer Science Department, 1996.

<sup>w</sup> <sup>x</sup> 13 S. Lalis, M. Marazakis, D. Papadakis, Effects of resource autonomy on end-to-end service provision, in: Proc. ISADS ’99, Fourth International Symposium on Autonomous Decentralized Systems, Tokyo, Japan, tentative.

<sup>w</sup> <sup>x</sup> 14 S. Lalis, C. Nikolaou, D. Papadakis, M. Marazakis, Marketdriven resource allocation in a QoS-capable environment, in: Proc. ICE’98, International Conference on Computationa Economics, ACM Press, 1998.

<sup>w</sup> <sup>x</sup> 15 M. Marazakis, D. Papadakis, C. Nikolaou, The Aurora architecture for developing network-centric applications by dynamic composition of services, Technical Report TR 213, FORTH<sup>r</sup>ICS, 1997.

<sup>w</sup> <sup>x</sup> 16 R.P. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 1987 699–738.Ž .

<sup>w</sup> <sup>x</sup> 17 T. Mullen, M.P. Wellman, A simple computational market for network information services, in: Proc. of the International Conference on Multiagent Systems, San Francisco, CA, 1995.

<sup>w</sup> <sup>x</sup> 18 T. Mullen, M.P. Wellman, The Auction Manager: market middleware for large-scale electronic commerce, in: Proc. Workshop on Agent-Mediated Electronic Trading in Conjunction with the 2nd International Conference on Autonomous Agents, 1998.

<sup>w</sup> <sup>x</sup> 19 R. Ramamoorthi, A. Rifkin, B. Dimitrov, K.M. Chandy, A general resource reservation framework for scientific computing, in: Proc. 1st International Scientific Computing in Object-Oriented Parallel Environments ISCOPE Confer-Ž . ence, 1997.

<sup>w</sup> <sup>x</sup> 20 T. Sandholm, Limitations of the Vickrey auction in computational multiagent systems, in: Proc. ICMAS ’96, Second International Conference on Multiagent Systems, Kyoto, Japan, 1996.

<sup>w</sup> <sup>x</sup> 21 T. Sandholm, V. Lesser, Issues in automated negotiation and electronic commerce: extending the contract net framework, in: Proc. ICMAS ’95, San Francisco, CA, 1995.

<sup>w</sup> <sup>x</sup> 22 T. Sandholm, V. Lesser, Advantages of a leveled commitment contracting protocol, in: Proc. AAAI ’96, Thirteenth National Conference on Artificial Intelligence, Portland, OR, 1996.

<sup>w</sup> <sup>x</sup> 23 T. Sandholm, V. Lesser, Coalitions among computationally bounded agents, Artificial Intelligence, Special Issue on Economic Principles of Multiagent Systems 94 1 1997 99–Ž . Ž . 137.

<sup>w</sup> <sup>x</sup> 24 M.A. Satterhwaite, S.R. Williams, Bilateral trade with the sealed bid k-double auction: existence and efficiency, Journal of Economic Theory 48 1989 107–133.Ž .

<sup>w</sup> <sup>x</sup> 25 S. Sen, Reciprocity: a foundational principle for promoting cooperative behavior among self-interested agents, in: Proc. Second International Conference on Multiagent Systems, AAAI Press, Menlo Park, CA, 1996.

<sup>w</sup> <sup>x</sup> 26 S. Sen, E.H. Durfee, A contracting model for flexible distributed scheduling, Annals of Operations Research 65 1996Ž . 195–222.

<sup>w</sup> <sup>x</sup>27 R.G. Smith, The contract net protocol: high-level communication and control in a distributed problem solver, IEEE Transactions on Computers 29 12 1980 1104–1113.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 H.R. Varian, J.K. MacKie-Mason, Generalized Vickrey auctions, Technical Report, Department of Economics, University of Michigan, 1994.

<sup>w</sup> <sup>x</sup> 29 W. Vickrey, Counterspeculation, auctions and competitive sealed tenders, Journal of Finance 16 1961 8–37.Ž .

<sup>w</sup> <sup>x</sup> 30 C.A. Waldspruger, T. Hogg, B.A. Huberman, J. Kephart, S. Stornetta, Spawn: a distributed computational ecology, IEEE Transactions on Software Engineering 18 2 1992 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 W.E. Walsh, M.P. Wellman, A market protocol for distributed task allocation, in: Proc. International Conference on Multiagent Systems, 1998.

<sup>w</sup> <sup>x</sup> 32 P. Weinstein, W.P. Birbingham, Service classification in a proto-organic society of agents, in: Proc. IJCAI-97 Workshop on Artificial Intelligence in Digital Libraries, 1997.

<sup>w</sup> <sup>x</sup> 33 M.P. Wellman, Market-oriented programming: some early lessons, in: S.H. Clearwater Ed. , Market-Based Control: A Ž . Paradigm for Distributed Resource Allocation, World Scientific, 1995, pp. 74–95, Chap. 4.

<sup>w</sup> <sup>x</sup> 34 P.R. Wurman, M.P. Wellman, W.E. Walsh, The Michigan Internet AuctionBot: a configurable auction server for human and software agents, in: Proc. International Conference on Autonomous Agents, 1998.

Spyros Lalis received a Doctoral Degree in Technical Sciences and a Diploma in Informatics Engineering from the Swiss Federal Institute of Technology, Zurich, Switzerland, in 1989 and 1994, respectively. Since 1997, he has been serving as adjunct assistant professor of Computer Science at the University of Crete and research associate at the Institute of Computer Science-FORTH. His research interests include software technologies, distributed protocols, operating systems, communication architectures, information economies, and market mechanisms for electronic goods.

Dimitris Papadakis is a PhD candidate at the Computer Science Department of the University of Crete, Greece and a research assistant at ICS-FORTH. He received a MSc in Computer Science and a Diploma in Computer Science from the Computer Science Department of the University of Crete, in 1993 and 1995. His research interests include object technologies and architectures, and, market models for resource allocation in distributed systems.

Manolis Marazakis is a PhD candidate at the Computer Science Department of the University of Crete, Greece and a research assistant at ICS-FORTH. He received a MSc in Computer Science and a Diploma in Computer Science from the Computer Science Department of the University of Crete, in 1993 and 1995. His research interests include object technologies and architectures, and service-level management of distributed systems.
