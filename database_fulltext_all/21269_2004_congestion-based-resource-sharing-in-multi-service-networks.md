---
otero_id: 21269
otero_key: "2P5UXTBJ"
title: "Congestion based resource sharing in multi-service networks"
authors: "Boris Jukic; Robert Simon; Woan Sun Chang"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00046-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Congestion based resource sharing in multi-service networks

Boris Jukic<sup>a,</sup>\*, Robert Simon<sup>b</sup>, Woan Sun Chang<sup>b</sup>

<sup>a</sup> School of Management, George Mason University, Fairfax, VA 22030, USA <sup>b</sup> Department of Computer Science, George Mason University, Fairfax, VA 22030, USA

Received 1 March 2001; accepted 1 December 2002

Available online 11 April 2003

## Abstract

The internet traffic is increasingly composed of streams of packets with very diverse quality of service (QoS) requirements: from those containing standard, best-effort traffic, such as e-mail or http sessions, to internet telephony and high-quality video streaming demanding dedicated allocation of network capacity. However, while methods based on externality pricing exist to offer socially optimal prices to the groups of users demanding different grades of the best-effort service class, less attention has been devoted to the implementation of such pricing models to the improvement of network resources allocation in a multi-service setting (i.e., a network offering various grades of both guaranteed and best-effort level of service). This paper addresses the problem through an end-to-end approach that combines a congestion-based pricing model for resource sharing with a QoS network model, based on admission rules. We describe a measurement-based approach for QoS path pricing that results in improved resource allocation policies between QoS and best-effort traffic. We also present the results of a large-scale simulation study that shows how this pricing scheme increases both end user value and system throughput with low computational overhead. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Networks; Resource sharing; Pricing; Quality of service

## 1. Introduction

Pricing for access, usage and quality of service on both public and private networks is one of the dominant issues affecting the diffusion of the next generation of bandwidth-intensive applications for Electronic Commerce. The simplest (and currently widely used) way to guarantee that all the performance requirements for all types of traffic are satisfied is over-provisioning of network capacity typically combined with at price periodical rate. Indeed, the aggressive expansion of fiber optic capacity combined with ongoing advances in high-speed technology make the notion of virtually unlimited availability of bandwidth at a very low price for everyone intuitively appealing, and it has been suggested that the future of providing for, pricing and managing of the internet capacity will be very similar to its past and present state [17]. However, while in the short run certain non-bottleneck parts of internet infrastructure may be in a temporary over-supply stage, as witnessed by the current decrease in prices for wholesale spot market for bandwidth [19], increased usage, driven by new applications, is most likely to catch up with the excess bandwidth. While it is always difficult to predict future with any degree of certainty, there does not seem to be shortage of proposed high-bandwidth consuming applications in areas of entertainment (interactive virtual reality gaming for example) or high-quality videoconferencing for variety of purposes such as business meetings, customer service, distance education, telemedicine and many others. These emerging types of distributed applications exhibit a wide range of communication needs and quality of service (QoS) performance requirements.

To meet these needs, most proposals for the next generation of networks and the internet offer a wide variety of service and QoS choices [1,2]. Although various proposals for QoS-enabled networking differ in many specifics, most assume that both best-effort traffic and traffic that receives some form of QoS support need to share resources at the level of individual routers or gateways. Since QoS traffic must be supported on an end-to-end basis, one of the challenges facing network architects is determining how QoS and best-effort traffic will share network resources. While current flat-rate charging mechanisms provide great degree of simplicity and flexibility in operation and management of internet infrastructure, need to provide for variety of QoS types is fueling the demands for a change in pricing mechanisms [4]. It is becoming increasingly obvious that the simple model on which the internet has operated so successfully, with all packets being treated equally is going to face possibility of drastic revisions in order to provide for more efficient way for providing sufficient bandwidth according to the needs of various user and application types.

Academic research community and networking and telecommunications industry is actively looking beyond over-provisioning and at rate pricing, and a variety of traffic management proposals, combining engineering and economic approaches, have been proposed. Several pricing proposals assessing charges on individual packets of best-effort transmission submission reflecting current state of the network have appeared in the literature [5,8,13,20]. (For a short overview of some of those schemes see Ref. [12].) Additionally, there has been much recent interest in pricing performance-sensitive networks. Courcoubetis et. al. [3] present an agent-based approach for charging users for ATM ABR connections. This approach is formulated as an optimization problem where bandwidth is allocated to each user proportionally to the amount of money the user is willing to pay per unit time. Other researchers have concentrated on the role of service-class sensitive pricing, [13], focused on a single node [21] or have suggested service-class insensitive pricing models [4]. In Ref. [16], the idea of ‘‘Paris Metro Pricing’’ (PMP) is introduced. Here, the network is partitioned into logically separate channels, and these channels are then priced by the network. Work described in this paper differs from these earlier approaches because we focus on both guaranteed, end-to-end QoS environment along with a node-by-node best-effort environment. The problem of optimal allocation of network resources between different applications with different performance objectives, including the guaranteed services, has been addressed in Ref. [25], but under the assumptions of a single profit-maximizing monopolist operating the point-to-point single link network.

The mechanism we choose to manage allocation of resources in this mixed environment is based on one of the general approaches to regulation of the use of network and other computing resources, based on the notion that the monetary cost of the submission should reflect the cost of inconvenience (delay) imposed on other submissions [9,14,15,22,24]. The so-called congestion-based pricing approach has also faced a lot of criticisms regarding its practicality. Issues raised range from the large computational overhead the pricing scheme may impose on the system, incentive compatibility, need to address the heterogonous nature of the internet traffic and its scalability over the large number of networks. However, it is important to notice that some of the listed criticisms are not limited to the congestion based pricing and indeed, academic and industrial community is still struggling to propose a widely accepted workable approach to improve the pricing management and performance of internet infrastructure beyond the policies of at rate and bandwidth over-provisioning. For example, some studies [6] bring the viability of any kind of differentiated pricing in doubt showing that carrier offering differentiated pricing (PMP in this case) would lose to a competitor offering undifferentiated services. On the other hand, a game theoretic simulation study by Stahl et. al. [23] showed that congestion-based pricing outperforms flat-rate pricing in ability to generate profits and delivery of user value. While admitting that problems of introducing differentiated pricing in the competitive setting such as today’s public internet are large and potentially insurmountable, current research on its viability is at best inconclusive. Work presented in this paper contributes to this ongoing discussion by explicitly addressing the issue of heterogeneity of internet traffic, while taking into account many of the above-mentioned practical considerations.

In the past, the congestion-based pricing approach has primarily been investigated in the context of priority classes for jobs/submissions roughly corresponding to the best-effort (elastic) applications, although the question of the role of pricing in facilitating different QoS requirements has been raised in Refs. [10,25]. The work presented here addresses that exact question by implementing the incentive-compatible multi-class priority pricing scheme and combining it with the admission rules for QoS constrained traffic, guaranteeing availability of network resources necessary to satisfy predetermined quality parameters. The general framework used corresponds closely to the one introduced in Ref. [8], where network nodes are represented as decentralized queuing systems producing estimates of waiting times and computing admission prices locally.

The paper proceeds as follows. Section 2 outlines the basics of the combined pricing and admission rulebased approach. Section 3 provides a discussion of the node and path-pricing model, along with the description of the network architecture on which the model and subsequent simulation experiments are based. Section 4 discusses implementation details, including the measurement algorithm. Section 5 details the results of an extensive simulation study that examined how well our approach works under a variety of Poisson and heavytailed traffic and connection patterns. Section 6 presents some conclusions and observations as well as the discussion of pricing implementation issues in the context of a global public network.

## 2. Combined pricing and admission control approach

In this section, we will introduce the idea of combining congestion pricing mechanism with the admission algorithm in the environment characterized by diversity of applications and user quality of service environments. Dynamic congestion-based pricing satisfies many stated characteristics necessary for viable pricing mechanism in multi-service data communication networks [10]. It encourages end user network management by shifting demands to the time of lower congestion. It reflects the load status of network nodes and it can be implemented in a decentralized manner, reflecting the decentralized nature of internet architecture and minimizing computational and transmission overhead. It also facilitates incentive compatible multi-priority pricing. Prices for admission in each of the priority levels reflect the cost of congestion imposed on all the affected traffic. As such, this mechanism is well suited for managing the various forms of traffic which does not have absolute performance limitations such as maximum delay suffered by packets in a data stream and guaranteed transfer rate. On the other hand, traffic streams resulting from applications that are sensitive to delay or decrease in other performance parameters need to have a mechanism in place guaranteeing that their requirements will be satisfied at the time of submission. For example, a telephone call or an interactive video-conferencing session over the internet will be of intolerable quality or may completely fail if a per-packet delay or packet loss percentage falls below certain minimum values. One possible approach to guaranteeing performance in a packet switched environment that does not allow for permanent and exclusive end-to-end reservation of network resources is through a variety of admission mechanisms that have been proposed (and implemented in certain environments such as ATM networks) guaranteeing minimum satisfaction of variety of performance measures for the streams that have constrained quality of service requirements. The main idea behind these methods is to monitor the current state of the network and all the streams currently owing through and allow (or prevent) submission of a new request based on the current availability of network capacity to satisfy its desired performance parameters without causing any minimum performance thresholds to be crossed for current traffic streams. The main goal of most of these proposed methods is to guarantee quality of service parameters among various priority classes of traffic in a packetswitched environment, and user value of a submis sion is not considered as an admission criterion. In order to maximize the total value of submitted requests in a capacity constrained environment, an additional admission criterion, based on the tradeoff between the value of new submission and the cost of delay imposed to other user request in the system needs to be introduced. With this in mind we investigate the possibility of extending the potential of congestion based pricing to serve this purpose and improve the efficiency of use of network resources shared by two fundamentally different types of traffic streams. The centerpiece of our approach consists of combining a known congestion-pricing model with admission rules mechanism for the traffic constrained by quality of service parameters. We will refer to this type of traffic as real-time traffic to contrast it with the best-effort network traffic without minimum performance requirements. We will outline our integrated model and show its potential to improved allocation of network resources among the diverse types of network traffic.

The two-step process of admission of traffic stream submissions will be described and its properties will be discussed using an analytical model. In the subsequent section, we will describe the multinode simulation study undertaken to show the benefits of this combined approach by comparing the performance of this approach with the one in which network resource are allocated between the besteffort traffic and constrained QoS traffic in fixed proportions.

## 3. A model for pricing-based resource sharing in multi-service networks

The following section describes our pricing and admission control model, as well as the network architecture on which it is based. The developed network resource-pricing model explicitly combines multiple service classes in an integrated framework.

In our model, nodes serve two different types of traffic. The first type will consist of multiple classes of real-time traffic that demands guaranteed bandwidth and per-node delay. The second type will be presented as a single class of best-effort traffic receiving no specific guarantees regarding any performance parameters.

Multi-service network architectures capable of providing QoS support typically require that new connections undergo an admission control test before they are admitted into service. The purpose of the admission control test is to verify that sufficient resources exist to support the QoS requirements of the new connection. In multi-service networks admission control for QoS traffic is generally done on a per node or a per domain basis. We assume that these nodes or domains can have an arbitrary interconnection pattern. Domains have internal and external behaviors. A domain’s external behavior is characterized by the QoS requirements it can offer to traffic that enters or exits (or both) and conceptually corresponds to the QoS requirement offerings of an individual node. In this paper, we focus our model on the node level, whereby each node supports two classes of service. The first is the QoS class. Traffic in this class receives network performance guarantees for both bandwidth and per node delay. The second class is the best-effort class. Traffic in this class does not receive any performance guarantees.

Each network node gives QoS traffic a higher priority than best-effort traffic. We assume that packet transmission is non-preemptive, that is, when a packet starts to be transmitted by the node that transmission is never interrupted, even when the node receives a higher priority packet. Logically each node maintains two levels of transmission queues. The top level consists of two transmission queues, one for QoS traffic and one for best-effort traffic. The node makes a scheduling decision whenever it is not currently transmitting a packet and whenever there are packets on at least one of the queues. If at scheduling decision time there are packets present on both the QoS and the best-effort queue then the node always picks for transmission a packet from the QoS queue. The second level of queues is a per-connection queue for QoS traffic that is logically within the higher level QoS queue.

We assume that each network node manages its per connection QoS Queues via a Fair Queueing packet scheduling algorithm in order to provide QoS bounds. Fair queueing algorithms are scheduling and multiplexing disciplines capable of providing end-toend delay and bandwidth guarantees on a per connection basis. A realizable and widely known Fair

Queueing packet algorithm is Weighted Fair Queueing (WFQ). In Ref. [18], Parekh and Gallagher showed that with an appropriate admission control and resource reservation policy WFQ provides a firm per packet end-to-end delay bound and ensures that all transmitted packets will be able to meet this bound. The value of the end-to-end delay guarantee is a function of the reserved rate for the connection, the connection’s short-term burst rate and the number of network hops in the route.

QoS requirements are put into the form of a source-destination pair and an end-to-end guaranteed rate. An application also specifies the economic value of the connection. This is the price that the user is willing to pay to obtain the service. Each QoS request $M _ { i }$ is formally specified as follows:

$$
M _ {i} \equiv \langle s, d, r _ {i}, V _ {i} \rangle
$$

where s is the source node, d is the destination node, $r _ { i }$ is the maximum channel rate in packets per second and $V _ { i }$ is the economic value of the request. The interpretation of this request is as follows. The values of $s ,$ d, $r _ { i }$ are used by the network to provide end-to-end QoS support. In a WFQ environment, the network takes this request and verifies that the network path can support the requested value of $r _ { i } .$ The value function $V _ { i }$ specifies the gross value per time unit gained by the user. Once a connection is accepted at a node, a separate queue is maintained for that connection at the node, and all packets arriving on that connection are placed on the appropriate queue. The WFQ policy specifies which packet to transmit next.

Each network path is priced by the network. This price reflects both the level of QoS provided by the network and the level of resource sharing between QoS and best-effort traffic.

## 3.1. QoS path prices

Each network node y advertises a vector $\pmb { p } _ { y }$ of prices. Prices are based upon the value and QoS requirements of the submitted job and the current level of utilization and resource sharing at the node. Assume that there are currently K QoS request types supported by a particular node. Each type of QoS request is of the form shown in Section 2. Then the price vector $\pmb { p } _ { y }$ has the form $\pmb { p } _ { y } = \langle p _ { y , M _ { 1 } } , p _ { y , M _ { 2 } } , \cdot \cdot \cdot , p _ { y , M _ { K } } ,$ $p _ { y , \mathbf { b } } \rangle$ , where $p _ { M _ { i } }$ is the price of admission for a new QoS request $M _ { i } ,$ and $p _ { \mathrm { b } }$ is the current price for besteffort traffic.

The price of a QoS path is given by combining the price at each intermediate node to form the overall QoS path price. For a route L and a QoS type $M _ { i } ,$ the QoS path price $P _ { M _ { i } , L }$ is given by

$$
P _ {M _ {i}, L} = \sum_ {y \in L} p _ {y, M _ {i}}.
$$

## 3.2. Node level pricing

Since admitted QoS traffic is given higher priority than best-effort traffic, QoS traffic is charged the price equaling the marginal cost of delay its submission caused to the best-effort traffic. If the utility of the admitted QoS traffic is not high enough to warrant the price of submission, the user submitting this QoS request will decide not to submit the request, despite the fact that the admission tests may have been passed. This is the optimal decision from the standpoint of the overall system (e.g., from the node’s point of view), since the utility of this request was not sufficient to offset increased delay cost of the best-effort class. Similarly, best-effort traffic will also be charged the price corresponding to the increase in delay cost caused to other besteffort requests. If the utility of the request is too low for the rational user to submit the request at the given price, then its decision not to submit is optimal for the entire network. In other words, the prices for the guaranteed quality of service are based on delay caused to best-effort traffic, while, consistently with framework proposed in Ref. [8], the best-effort traffic is charged the price corresponding to the marginal delay caused to subsequent best-effort requests.

## 3.2.1. Assumptions

The pricing model assumes that each request submission is motivated strictly by the individual shortterm net benefit maximization. Consequently, as in Ref. [8], we assume that users make decision to submit a request to the network based on current expected waiting times and expected monetary cost of their submission, without being concerned how serving of their request might affect future waiting times and posted admission prices. The model also makes the following assumptions:

1. Arrival processes: we assume that best-effort traffic arrives according to an average rate of ${ \hat { r } } _ { \mathrm { b } } .$ Requests for each class $M _ { i }$ of QoS traffic arrives with an average rate of $\lambda _ { M _ { i } } , i = 1 , \ldots . . , K .$ . We also assume that each class $M _ { i }$ has an average holding rate of $\mu _ { M _ { i } }$

2. Value functions: the value function of packet streams for both types of user classes can be expressed as $V _ { M _ { i } } ( \lambda _ { M _ { i } } )$ and $V _ { \mathrm { b } } ( \hat { r } _ { \mathrm { b } } )$ , which specifies the aggregate gross value per unit of time gained by users when arrival rates of submitted jobs are $\lambda _ { M _ { i } }$ and ${ \hat { r } } _ { \mathrm { b } } .$ By assumption $V _ { M _ { i } } ( \lambda _ { M _ { i } } )$ and $V _ { \mathrm { b } } ( \hat { r } _ { \mathrm { b } } )$ are differentiable, concave and nondecreasing functions. The total value of packet streams owing through the network link y can be expressed as sum of their value functions, or

$$
\sum_ {M _ {i} \in y} V _ {M _ {i}} (\lambda_ {M _ {i}}) + V _ {\mathrm{b}} (\hat {r} _ {\mathrm{b}}).
$$

3. Delay cost structure: best-effort user requests are characterized by the linear delay cost, with the parameter $\nu _ { \mathrm { b } }$ per unit of time. User requests for all the classes of QoS jobs have a delay cost $\nu _ { M _ { i } } { = } 0$ since their admission parameters have already been satisfied.

## 3.2.2. Optimal node pricing structure

Let $L _ { \mathrm { b } } ( \cdot )$ be a function that specifies the expected queue length for best-effort traffic at a node. When there is no chance for confusion, for simplicity we drop the node subscript y in all subsequent notation. The problem of maximizing net benefits to the system as a whole can be formulated in the following way:

Value function

$$
\max _ {\hat {r} _ {\mathrm{b}}, \lambda_ {M _ {i}}} \left(\sum_ {M _ {i}} V _ {M _ {i}} \left(\lambda_ {M _ {i}}\right) + V _ {\mathrm{b}} \left(\hat {r} _ {\mathrm{b}}\right) - v _ {\mathrm{b}} L _ {\mathrm{b}} (\cdot)\right).\tag{1}
$$

This expression is a slight variation of the standard approach to maximizing net user value, as shown in Refs. [8,15,22] and only includes nonmonetary cost of submission. Price charged for packet stream submissions is transfer payment from one part of the system to another and is not included in the objective function. Our model differs from the ones cited above in added assumption that QoS transmissions that have passed the admission rule do not incur any explicit delay costs. We now present the following pricing result as a joint theorem:

Theorem. Let $W _ { \mathrm { b } }$ be the expected waiting time for best-effort traffic. The following pricing results in the optimal allocation of the link between the QoS and best-effort traffic.

$$
p _ {M _ {i}} = v _ {\mathrm{b}} \hat {r} _ {\mathrm{b}} \frac {\partial W _ {\mathrm{b}}}{\partial \lambda_ {M _ {i}}}\tag{2}
$$

$$
p _ {\mathrm{b}} = v _ {\mathrm{b}} \hat {r} _ {\mathrm{b}} \frac {\partial W _ {\mathrm{b}}}{\partial \hat {r} _ {\mathrm{b}}}.\tag{3}
$$

Proof. This proof is again a slight modification of a proof of multi-class case of generalized net value maximizing pricing scheme, as shown in Ref. [15]. It reflects the additional assumption of zero value for delay cost for QoS classes of traffic. We will first prove Eq. (2) and then Eq. (3). First, define the vector ${ \pmb { \psi } } _ { M _ { i } }$ as

$$
\boldsymbol {\Psi} _ {M _ {i}} = \left\langle \lambda_ {M _ {1}} \hat {r} _ {M _ {1}}, \lambda_ {2} \hat {r} _ {M _ {2}}, \dots , \lambda_ {M _ {K}} \hat {r} _ {M _ {K}} \right\rangle
$$

where $\hat { r } _ { M _ { i } }$ is the average packet arrival rate for a QoS channel of type $M _ { i } .$ Notice that, especially for bursty QoS traffic, this value will be less than the peak rate $r _ { i }$ for all the $M _ { i } \mathbf { s }$ . The average waiting time for a besteffort packet is a function of the vector ${ \pmb { { \varPsi } } } _ { M _ { i } }$ and the arrival rate for best-effort traffic, ${ \hat { r } } _ { \mathrm { b } } .$ We write this average waiting time as $W _ { \mathrm { b } } ( \pmb { \Psi } _ { M _ { i } } , \hat { r } _ { \mathrm { b } } )$ . By Little’s Law the average number of best-effort packets $L _ { \mathrm { b } } ( \Psi _ { M _ { i } } , \hat { r } _ { \mathrm { b } } )$ is given by

$$
L _ {\mathrm{b}} \left(\boldsymbol {\Psi} _ {M _ {i}}, \hat {r} _ {\mathrm{b}}\right) = \hat {r} _ {\mathrm{b}} W _ {\mathrm{b}} \left(\boldsymbol {\Psi} _ {M _ {i}}, \hat {r} _ {\mathrm{b}}\right).
$$

First order conditions for maximizing our objective function (social optimality) are given by:

$$
V _ {M _ {i}} ^ {\prime} (\lambda_ {M _ {i}}) = v _ {\mathrm{b}} \frac {\partial L _ {\mathrm{b}} (\Psi_ {M _ {i}} , \hat {r} _ {\mathrm{b}})}{\partial \lambda_ {M _ {i}}}\tag{4}
$$

$$
V _ {\mathrm{b}} ^ {\prime} \left(\hat {r} _ {\mathrm{b}}\right) = v _ {b} \frac {\partial L _ {\mathrm{b}} \left(\Psi_ {M _ {i}} , \hat {r} _ {\mathrm{b}}\right)}{\partial \hat {r} _ {\mathrm{b}}}.\tag{5}
$$

Individually rational submission rates resulting in an equilibrium are expressed in the following demand relationship:

$$
V _ {M _ {i}} ^ {\prime} (\lambda_ {M _ {i}}) = p _ {M _ {i}}\tag{6}
$$

$$
V _ {\mathrm{b}} ^ {\prime} \left(\hat {r} _ {\mathrm{b}}\right) = p _ {\mathrm{b}} + v _ {\mathrm{b}} W _ {\mathrm{b}} (\boldsymbol {\Psi}, \hat {r} _ {\mathrm{b}}).\tag{7}
$$

The interpretation of these relationships is that the marginal individual job is the one whose submitter is indifferent between submitting and refusing to submit because individual benefit realized from this job equals total expected cost of submission.. By using Eqs. (4) and (6) we can prove Eq. (2).

$$
\begin{array}{l} p _ {M _ {i}} = v _ {b} \frac {\partial L _ {\mathrm{b}} (\boldsymbol {\Psi} _ {M _ {i}} , \hat {\boldsymbol {r}} _ {b})}{\partial \lambda_ {M _ {i}}} \\ \qquad = v _ {b} \frac {\partial \hat {\boldsymbol {r}} _ {b} W _ {b} (\boldsymbol {\Psi} _ {M _ {i}} , \hat {\boldsymbol {r}} _ {\mathrm{b}})}{\partial \lambda_ {M _ {i}}} \\ \qquad = v _ {\mathrm{b}} \bigg (W _ {\mathrm{b}} (\boldsymbol {\Psi} _ {M _ {i}}, \hat {\boldsymbol {r}} _ {\mathrm{b}}) \frac {\partial \hat {\boldsymbol {r}} _ {\mathrm{b}}}{\partial \lambda_ {M _ {i}}} + \hat {\boldsymbol {r}} _ {\mathrm{b}} \frac {\partial W _ {\mathrm{b}} (\boldsymbol {\Psi} _ {M _ {i}} , \hat {\boldsymbol {r}} _ {\mathrm{b}})}{\partial \lambda_ {M _ {i}}} \bigg) \end{array}\tag{8}
$$

$$
= v _ {\mathrm{b}} \hat {r} _ {\mathrm{b}} \frac {\partial W _ {\mathrm{b}}}{\partial \lambda_ {M _ {i}}}.\tag{9}
$$

Eq. (9) follows from Eq. (8) because of the independence of $\mathrm { \hat { r } _ { b } }$ and $\lambda _ { M _ { i } } .$ By using Eqs. (5) and (7), we likewise prove Eq. (3):

$$
\begin{array}{l} p _ {\mathrm{b}} = v _ {\mathrm{b}} \frac {\partial L _ {b} (\Psi_ {M _ {i}} , \hat {r} _ {b})}{\partial \hat {r} _ {b}} - v _ {b} W _ {b} (\Psi_ {M _ {i}}, \hat {r} _ {b}) \\ = v _ {b} W _ {b} (\Psi_ {M _ {i}}, \hat {r} _ {b}) + v _ {b} \hat {r} _ {b} \frac {\partial W _ {b} (\Psi_ {M _ {i}} , \hat {r} _ {\mathrm{b}})}{\partial \hat {r} _ {\mathrm{b}}} \\ - v _ {\mathrm{b}} W _ {\mathrm{b}} (\Psi_ {M _ {i}}, \hat {r} _ {\mathrm{b}}) \end{array}
$$

## 4. Implementation

The purpose of the QoS path pricing scheme is to maximize user value via resource sharing. We use best-effort prices as a way of regulating the level and utilization of best-effort connections. The level of resource sharing between QoS and best-effort traffic can be determined by the objective of maximizing user value or by a network policy decision. Either way, the fully distributed nature of our proposed resource sharing and pricing mechanisms depend first on the feasibility of each node actually producing the correct QoS and best-effort prices. This section first describes the node-based approach for actually setting the prices, and then explains the combined admission control rules.

## 4.1. Node price measurements

Implementation of this pricing scheme depends on the feasibility of retrieving all the needed input parameters. Once again, when there is no chance for confusion, for simplicity we drop the node subscript y in all subsequent notation. The values of $\partial W _ { \mathrm { b } } / \partial \lambda _ { M _ { i } }$ and $) W _ { \mathrm { b } } / \partial \hat { r } _ { \mathrm { b } }$ will have to be obtained. There are several approaches to this problem. For instance, in a network with relatively static workload it is possible to obtain these values analytically. However, an analytical approach is often not feasible in a network undergoing frequent shifts in traffic patterns. Another alternative is to determine the exact functional relationship between the arrival rates and waiting times through an estimation method using previously observed values, but computational overhead may render this approach impractical. For the purpose of conducting our experiments, we use a reduced bandwidth measurement-based approach using the standard M/G/1 queuing model with no priorities for estimating the waiting time incurred by admitting new jobs. This particular approach to estimating waiting times has also been suggested and used in the best-effort network model in Refs. [8,9]. As will be seen, all of the parameters required by our model are obtainable from existing on-line router measurements. We have found that this technique produces excellent results for setting prices, even under circumstances of non-Poisson traffic arrival patterns.

The reduced bandwidth approach is as follows: let $\hat { r } _ { \mathrm { b } }$ be the average packet arrival rate for best-effort traffic, and $S _ { \mathrm { b } }$ be the average size of best-effort traffic. Let C be the total bandwidth of the node, and define $C _ { \mathrm { b } }$ as the amount of (reduced) bandwidth available to best-effort traffic. Let $\rho _ { \mathrm { b } }$ be the measured utilization rate for best-effort traffic. $W _ { \mathrm { b } }$ is given by [11]:

$$
W _ {\mathrm{b}} = \frac {\hat {r} _ {\mathrm{b}} S _ {\mathrm{b}} ^ {2}}{2 C _ {\mathrm{b}} ^ {2} (1 - \rho_ {\mathrm{b}})}.\tag{10}
$$

Recalling that $\mu _ { M _ { i } }$ is the average holding rate for $M _ { i } ,$ the reduced bandwidth $C _ { \mathrm { b } }$ is given by:

$$
C _ {\mathrm{b}} = C - \sum_ {i} \frac {\lambda_ {M _ {i}}}{\mu_ {M _ {i}}} \hat {r} _ {M _ {i}}.\tag{11}
$$

$\rho _ { \mathrm { b } }$ is given by

$$
\begin{array}{c} \rho_ {\mathrm{b}} = \frac {\hat {r} _ {\mathrm{b}} S _ {\mathrm{b}}}{C _ {\mathrm{b}}} \\ = \frac {\hat {r} _ {\mathrm{b}} S _ {\mathrm{b}}}{C - \sum_ {M _ {i}} \frac {\lambda_ {M _ {i}}}{\mu_ {M _ {i}}} \hat {r} _ {M _ {i}}}. \end{array}\tag{12}
$$

By substituting Eqs. (11) and (12) into Eq. (10) we get

$$
\begin{array}{c} W _ {\mathrm{b}} = \frac {\hat {r} _ {\mathrm{b}} S _ {\mathrm{b}} ^ {2}}{2 \left(C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}}\right) ^ {2} \left(1 - \frac {\hat {r} _ {\mathrm{b}} S _ {\mathrm{b}}}{C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}}}\right)} \\ = \frac {\hat {r} _ {\mathrm{b}} S _ {\mathrm{b}} ^ {2}}{2 \left(C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}}\right) ^ {2} - 2 \hat {r} _ {\mathrm{b}} S _ {\mathrm{b}} \left(C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}}\right)}. \end{array}
$$

We can now show expressions for $\partial W _ { \mathrm { b } } / \partial \hat { r } _ { \mathrm { b } }$ and $\partial W _ { \mathfrak { b } } / \partial \lambda _ { M _ { i } }$

$$
\begin{array}{l} \frac {\partial W _ {\mathrm{b}}}{\partial \hat {r} _ {\mathrm{b}}} = \frac {S _ {\mathrm{b}} ^ {2}}{2 \left(C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}}\right) \left(C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}} - \hat {r} _ {\mathrm{b}} S _ {\mathrm{b}}\right)} \\ + \frac {W _ {\mathrm{b}} S _ {\mathrm{b}}}{\left(C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}} - \hat {r} _ {\mathrm{b}} S _ {\mathrm{b}}\right)} \end{array} \tag {1}\tag{13}
$$

and

$$
\begin{array}{l} \frac {\partial W _ {\mathrm{b}}}{\partial \lambda_ {M _ {i}}} = W _ {\mathrm{b}} \frac {\hat {r} _ {i}}{\mu_ {M _ {i}}} \left[ \left(\frac {1}{C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}} - \hat {r} _ {\mathrm{b}} S _ {\mathrm{b}}}\right) + \left(\frac {1}{C - \sum_ {i} \frac {\lambda_ {M _ {i}} \hat {r} _ {i}}{\mu_ {M _ {i}}}}\right) \right] \end{array}\tag{14}
$$

The derivations of these expressions is algebraically straightforward but rather laborious. The details are presented in Ref. [21] and will not be repeated here. Notice that the parameters in Eqs. (13) and (14) are obtainable from online router measurements. This approach takes into account the amount of bandwidth allocated to QoS traffic relative to the average size of best-effort packets and guarantees that the congestion charge for QoS traffic reflects the full cost of reserved bandwidth. Therefore, the incentive-compatibility issue is addressed by guaranteeing that QoS charge does not invite possibility of multitude of best-effort traffic packets masking themselves as a single QoS submission in order to get lower per-packet price at higher priority. The implementation is not ‘‘forward looking’’ though, so problem of locking in a relatively low price for a significantly large period of holding time for QoS traffic does exist and it needs to acknowledged as a potential implementation issue.

## 4.2. Connection establishment and resource sharing

QoS connections require a connection two-step establishment phase. Consider a new channel request of type $M _ { i } \equiv \langle s , d , r _ { i } , V _ { i } \rangle$ , where, as explained in Section $^ { 3 , }$ s is the source, d is the destination, $r _ { i }$ is the maximum packet rate and $V _ { i }$ is the value of the request.

The network first selects a path from s to d upon which to route the QoS connection request. The network then determines the path price, as specified in Section 3. If the value of the connection is greater than or equal to the price then the second phase is run. If the value is less then either a different path is selected or the connection is rejected.

The second phase is a QoS verification step. For WFQ, the admission control step is performed at each node in the routing path from s to d. This test verifies that the aggregate bandwidth of existing QoS connections, along with the new request, is not greater than the bandwidth allocated to QoS traffic. The test can be explained as follows. Assume that the maximum size of a packet in the network is given by $S _ { \mathrm { m a x } }$ bits. Define the required bandwidth $b _ { i }$ of the new request $M _ { i }$ as

$$
b _ {i} = \lceil r _ {i} S _ {\mathrm{max}} \rceil\tag{15}
$$

Next, without loss of generality, assume that the capacity allocated to serving QoS traffic at a particular node is C bits per second. Further, assume that there are currently K QoS connections that are in service at the node. Each of these QoS connections has a bandwidth requirement of $b _ { j } , \forall M _ { j } { \in } K .$ . Then, the new request M is admitted if and only if the following relationship is verified:

$$
b _ {i} + \sum_ {j = 1} ^ {K} b _ {j} \leq C\tag{16}
$$

Best-effort users also assign values to their connections and flows. Assigning of explicit values to the best-effort flows can be specific to an individual system implanting this scheme, and can be done on a user basis, an application basis (such as ftp vs. web traffic) or by an ISP that classifies value of traffic according to their customer’s willingness to pay. The best-effort price is determined from Eq. (3). Notice that our approach easily extends to multiple classes of best-effort traffic. If the value of the best-effort traffic is greater than or equal to the price plus the expected waiting cost then best-effort packets use the node, else the best-effort packet will not use that particular node. Since it is not feasible to determine this price on every packet, in practice the best-effort pricing mechanism is periodically posted by the node. Best-effort routing decisions could then be made using this posted price.

## 5. Simulation study

In this section, we describe the results of a simulation study designed to test the effectiveness of the path pricing model. We tested network throughput and utilization for the path-pricing scheme, but the main performance measure of our interest is the aggregate value of real-time and best-effort requests served by the network over a period of time. Three sets of experiments were conducted.

The first study involved logical separation of bandwidth between guaranteed QoS traffic and besteffort traffic by implementing fixed allocation of links between those two types of traffic. This study is conducted for the purpose of setting a performance benchmark against which we will measure the results of dynamic bandwidth allocation experiments.

The second simulation study implements dynamic allocation of network capacity, using congestionbased pricing in concert with admission rules implementation.

Finally, the third study illustrates the ability of dynamic pricing to contribute to increased throughput of user value, even if fixed allocation of bandwidth is mandated by the system. For example, a network may be required to offer a percentage of its capacity for best-effort traffic at any time. This requirement is implemented in the third set of experiments which still implements dynamic pricing to allocate bandwidth but the caps are set on the percentage of bandwidth that can be consumed by the QoS traffic, with the remainder always being available to the besteffort traffic. For both QoS and best-effort traffic the admission control procedures described in Section 4.2 were used.

## 5.1. Traffic characteristics

In order to simulate both QoS and best-effort connections, we used a mixture of Poisson and non-Poisson for QoS connection request arrivals, QoS connection holding time patterns, and traffic arrival patterns for best-effort flows. The experiments were developed using the CSIM simulation package. Per node packet scheduling was done with WFQ scheduling routines using the analysis contained in Ref. [18]. We simulated a linear network consisting of five nodes connected with four links as shown in Fig. 1.

![](/api/attachments/2P5UXTBJ/fulltext/images/e341abc009d52d1acba01539d786dcddb45911e74430af199709525a0e50fb5b.jpg)  
Fig. 1. Simulated network. There are 20 best-effort flows and three network path routes.

Each link has a bandwidth of 45 Mbps. All links are simplex, e.g., all traffic flows from lower numbered nodes to higher numbered nodes.

We considered three QoS request types, $M _ { 1 } , M _ { 2 }$ and M<sub>3</sub>, and 20 UDP best-effort flows. Each best-effort flow fell into one of two different traffic classes, either highly bursty or Poisson. For all three QoS request types the source node was node 0 and the destination node was node 4. Users were divided into three different populations corresponding to the three different QoS request types. Users only requested QoS request types for their assigned types.

The arrival patterns for the pricing experiment were picked to on average produce roughly over 70% occupancy of our total capacity for all types of QoS traffic. Therefore, we expect admission control to be a factor, for both QoS and best-effort traffic, in all experiments. We proceeded as follows: all runs had the following QoS traffic arrival patterns. $M _ { 1 }$ requests had an interarrival rate of 0.3 min and a lognormal holding time of 3 min average. $M _ { 2 }$ requests had an interarrival rate of 4.2 min and a fixed holding time of 30 min. $M _ { 3 }$ had an interarrival rate of 8.3 min and a holding time taken from a normal distribution with a 60 min average.

$M _ { 1 }$ represents a QoS request type designed to support a QoS audio connection, specifically an 8 kHz 8-bit mu-law PCM audio application. It is effectively represented by an on–off source model. During an ‘‘on’’ phase, the source transmits 200 byte packets at a rate of 80 kbps. During an ‘‘off’’ phase, the source is completely silent. Both the on and the off times are taken from an exponential distribution with a 500 ms average.

M represents a QoS request type designed to support moderately bursty video-on-demand application of fixed duration, such as a TV show. $M _ { 3 }$ represents QoS request types designed to support highly bursty video-on-demand application of longer duration, such as a pay-per-view sporting event. In this way, both $M _ { 2 }$ and $M _ { 3 }$ represent bursty higher bandwidth applications. These processes are represented as two state Markovmodulated Poisson process. We refer to these two states as the ‘‘average’’ state and the ‘‘peak’’ state. In the average state, $M _ { 2 }$ sends data according to an exponential distribution with an average rate of 1.25 Mbps. In the peak state, $M _ { 2 }$ sends data according to an exponential distribution with an average rate of 1.5 Mbps.

In the average state, QoS request type $M _ { 3 }$ sends at a rate of 392 kbps. $M _ { 3 }$ sends at the peak rate of 1.5 Mbps during the peak state. The average times are taken from an exponential distribution with a 1300 ms average, and the peak times are taken from an exponential distribution with a 250 ms average.

We ran simulation experiments with two different classes of best-effort traffic flows. One best-effort flow class produced traffic according to an exponential traffic model, while the other class produced traffic according to an on–off source model. For each exponential flow, the average rate of best-effort traffic is 2 Mbps. During ‘‘on’’ phase of on –off source model, packets arrive at a rate of 4 Mbps. During ‘‘off’’ phase, no packets arrive. Both the on and off times are taken from an exponential distribution with a 500 ms average. For the network under consideration, we simulated 20 best-effort flows, 10 of type exponential and 10 of type on– off. These 20 flows are shown in Table 1.

For best-effort packets, admission control, using either the pricing mechanism or the threshold mechanism, was done on a per node level, e.g., not a flow basis. Best-effort packet sizes were drawn from a uniform distribution between 40 and 1500 bytes.

## 5.2. User values of traffic flows

In determining the levels of user values used in our experiments, we approximated the average levels of transmission values for various classes of traffic with the current prices for commercially available services most closely resembling each request type. This approach is based on the notion that user’s average value for particular service is comparable to its current market price. The approximations are fairly crude, since real utility of any individual submission of a job of any class is determined by a variety of additional factors. However, additional complexity in determining the true user valuation of each request, through smart agents or otherwise, may render the implementation of the pricing scheme infeasible, by imposing too large computational overhead on user submission process requiring a complex decision making process for each submission. On the other hand by approximating the value of each individual request by the average price users are willing to pay for the corresponding class of service, we have an easily implementable method of allocating value to each flow in our simulation experiment. Average value approximations for three classes of real time services were determined in the following way. Since QoS request type $M _ { 1 }$ represents an internet telephony application, we assume that the average price of a long distance phone call is about \$US0.10/min, and that the average length of a phone call is approximately 3 min long. We use that assumption to allocate average value to the user of $M _ { 1 }$ equaling \$US0.30, or \$US0.00167/s of connection. There exists significant empirical evidence that call holding time distributions for twoway phone conversations, fax transmissions and voice messaging systems are actually better modeled by heavy tailed distributions. For this reason, we model the call holding time by a lognormal long-tailed distribution.

<table><tr><td colspan="2">Table 1Best-effort flows</td></tr><tr><td>Source node</td><td>Destination nodes</td></tr><tr><td>0</td><td>1, 2, 3, 4</td></tr><tr><td>1</td><td>2, 3, 4</td></tr><tr><td>2</td><td>3, 4</td></tr><tr><td>3</td><td>4</td></tr></table>

Each source-destination pair has two flows, one of traffic type exponential and one of type on – off, for a total of 20 flows.

For $M _ { 2 } .$ , based on an estimated price of a flat fee of US\$200 a month for media-on-demand services and usage of 40 h a month, we arrive at a rate of US\$5 an hour for usage value. The average usage value of 30- min $M _ { 2 }$ connection is US\$2.5. For the longer $M _ { 3 }$ connection, the average usage value is US\$10.

For each best-effort packet, we assume that the average value to the user is US\$0.000001. We used the following reasoning to derive this figure: currently many users pay approximately US\$20 a month for unlimited access to the internet. Assume that average user is online approximately 20 h a month. Further, assume that the network connection is active on the order of taking place 20 min in every hour of active usage at the speed of 50 kbps, we arrive at the average packet value above. Average packet size of 6000 bits is assumed. The delay cost is set to correspond to a certain percentage of user value per unit of time meaning that the value of each packet is assumed to deteriorate at a linear scale. For each packet, the delay cost for best-effort traffic is drawn from a normal distribution. We simultaneously created flows with a variety of means for the delay distribution, ranging form several milliseconds (representing best-effort flows resulting form delay intolerant applications) to tens of seconds (representing less time sensitive besteffort flows).

As arbitrary as our choice of user values for all classes of jobs may seem, our primary concern was to reflect higher relative users’ valuation of real-time streams compared to the average valuation of besteffort requests. The guiding principle we used is that, in most cases, higher quality of transmission corresponds to the higher utility for the user and vice versa. For example, a user may conduct a telephone call as an $M _ { 1 }$ flow or as a best-effort transmission. If a chosen transmission is a real-time flow, it probably has a higher value to the user than a best-effort session of similar length would have.

## 5.3. Experiment setup and results

We are interested in judging how the dynamic QoS price routing strategy affects user value, compared to the fixed partition model. While we would expect adaptive pricing to produce higher overall user values than the fixed strategy, one advantage of the fixed partition model is its simple implementation. We therefore want to assess whether the expected performance improvement through adaptive pricing is significant enough to justify its increased complexity.

In the first experiment, based on the fixed threshold model, the admission control mechanisms for QoS and best-effort do not use pricing. Instead, a fixed bandwidth threshold is set to statically partition available capacity between QoS and best-effort traffic. A new QoS channel request will be admitted as long as there is sufficient bandwidth for QoS traffic from its source node to its destination node to meet its peak rate. On a weighted averaging basis the node measures the arrival rate of best-effort traffic. If the arrival rate of the best-effort packets does not exceed the allocated bandwidth, a new best-effort packet will be admitted. If the threshold is reached then new besteffort traffic is rejected for a fixed time interval. The set of experiments is conducted gradually increasing the percentage of available threshold bandwidth to the real time traffic. The first threshold experiment was

Average Net User Value

set to 50% best-effort and 50% QoS. The subsequent experiments were conducted, whereby the capacity given to the QoS traffic at expense of best-effort traffic was increased in increments of 10%.

Fig. 2 shows that, given our parameters, the highest net user value in the fixed threshold setting is achieved when 90% of capacity is permanently allocated to the QoS traffic. This may seem unexpected given that aggregate average arrival rate is set to 0.7 of the total path capacity. However, given the burstiness of traffic patterns allocation of 90% provided for maximum acceptance rate for QoS traffic, which was more than enough to offset value losses in best-effort traffic. Notice that giving 100% of capacity to QoS traffic resulted in dramatic loss of net user value since no additional net user value is generated on the QoS side while all best-effort traffic was eliminated.

In the second set of the simulation experiments, we employ congestion-based pricing to allocate bandwidth among real-time and best-effort traffic by charging for the externalities imposed to all the submissions at lower priority, and in the case of best-effort traffic, also for the externalities incurred by the submissions of the same priority. No amount of bandwidth is pre-allocated to the QoS traffic, and each submission request may use any portion of unused capacity, as long as it passes the two-step admission process as described in Section 4.2.

The following figures compare the results of the second experiment using dynamic link allocation and the first experiment using fixed threshold allocation across three different performance measures. As mentioned above, the primary performance measure of our interest is aggregate net user value.

Fig. 3 compares the highest level of net user value realized by fixed threshold approach with the net user value generated when dynamic allocation of link is implemented through our adaptive pricing scheme. The results show that, by not restricting the usage of network capacity to either traffic type, significantly higher amount of net user value was generated under dynamic allocation scheme than under the most successful fixed threshold allocation.

As mentioned in the introduction part of this section, a third set of experiments is conducted, which also implements dynamic pricing to allocate bandwidth but this time with caps being set on the percentage of bandwidth that can be consumed by the QoS traffic, with the remainder always being available to the best-effort traffic. We conducted this set of simulation experiments using the pricing and admission control model with different maximum link bandwidth allocations for QoS traffic. These maxi-

![](/api/attachments/2P5UXTBJ/fulltext/images/951af096a2d193ebdd617d63278be3b6d619cb9c48de64840d0dcf6aa90f4883.jpg)  
Fig. 2. Average net user value: fixed threshold allocation.

Average Net User Value

![](/api/attachments/2P5UXTBJ/fulltext/images/80a47614de28d3e89151ed40ef045226c683c369a025eeab5406d05c78548e0b.jpg)  
Fig. 3. Average net user value: best-fixed threshold vs. dynamic allocation.

mum QoS allocations were 70%, 60% and 50% of bandwidth.

Fig. 4 expands the net-value based comparison by including the performances from the third set of experiments limiting maximum allowed bandwidth for the QoS traffic and comparing them with the results of the first, fixed capacity allocation experiment. These results show that, even with mandated bandwidth percentage caps, dynamic link allocation outperforms static link allocation across the whole range of percentages allowed for QoS traffic.

Now, we turn our attention to other two chosen performance parameters, link utilization and number of packets transmitted. Fig. 5 shows the average link utilization for dynamic pricing model (experiment set 2) and the fixed threshold run (experiment set 1) with the highest utilization (50 allocation to QoS resulted in highest link utilization among all fixed threshold runs). Again, the run with the pricing model has a higher link utilization than the best one with the threshold model.

![](/api/attachments/2P5UXTBJ/fulltext/images/4be6a63b64e10077f048fe0cad49d85298d18e7bf6aba202ff98f6b671c6ad4d.jpg)  
Fig. 4. Average net user value: fixed threshold vs. dynamic allocation with maximum threshold.

![](/api/attachments/2P5UXTBJ/fulltext/images/facf51d971e25e247cc2107b2c6f3f1ddb7a9a77a4a4c5eb8b888baea01e8e11.jpg)  
Fig. 5. Average utilization: best-fixed threshold vs. dynamic allocation.

Fig. 6 contains the expanded results with respect to the link utilization, including the results of the third set of experiments. It again shows that the highest average link utilization (72%) was achieved when the entire link is apportioned using dynamic pricing, without maximum restrictions on QoS allocation. However, even in the set of experiments that limits the bandwidth allocation to QoS traffic while using the adaptive scheme average link utilizations were kept relatively high, compared to the fixed threshold allocation. For instance, at 50% maximum allocation to QoS under adaptive pricing the average link utilization was still 66%. Further, in each case adaptive pricing achieved higher network utilization than the fixed resource allocation strategy. For instance, at 60% allocation the utilization for adaptive pricing was 68.9%, while the fixed strategy only achieved 52.8%. This result clearly shows that the adaptive pricing approach makes good use of all available resources and in fact far outperforms static partitioning for average utilization.

![](/api/attachments/2P5UXTBJ/fulltext/images/f228f6046c3227ae07dcc8f26a81af544ea47d8cdc783b64e1a90eaf368c2dab.jpg)  
Fig. 6. Average utilization: fixed threshold vs. dynamic allocation with maximum threshold.

Finally, Fig. 7 shows the performance with respect to the actual number of packets transmitted throughout the entire network. Notice that, as would be expected, as the allowable bandwidth for QoS traffic decreases the number of transmitted best-effort packets increase. When all of the bandwidth is potentially reserved for QoS traffic the number of best-effort packets is around 63.2 million. When only 50% of the bandwidth is reserved for QoS traffic the number of best-effort packets is around 66 million, an increase of around 6%. This shows that the pricing scheme does an excellent job in supporting best-effort flows. Further, the static threshold scheme is far worse. For instance, with the 70% static threshold policy only about 35 million best-effort packets are transmitted, as opposed to over 64 million with the adaptive scheme.

In short, our experimental results show that, with an appropriate pricing structure, the various measures of network performance for best-effort traffic can be improved without affecting the overall level of performance for QoS traffic.

## 6. Conclusions and directions for future research

This paper has presented a fully distributed adaptive pricing scheme for combined QoS and best-effort resource sharing. We presented a per node measurement-based approach for QoS path pricing that results in near-optimal resource allocation policies between QoS and best-effort prices. The node-based pricing approach was used as the basis for setting a QoS-path price. We also presented the results of a large scale simulation study, using a mixture of connection types, holding times and packet arrival patterns, that shows how this pricing scheme increases both end user value and system throughput with minimal computational overhead.

![](/api/attachments/2P5UXTBJ/fulltext/images/1fb179eece9462ec64f89cbc57f94254bedfc2ebb56a14b993000dea9224fdb4.jpg)  
Fig. 7. Packets transmitted: dynamic allocation, fixed threshold and dynamic allocation with maximum threshold.

We showed that the congestion based pricing approach for both real-time and best-effort traffic, combined with an admission method for real-time traffic guaranteeing that all admitted real-time jobs will be served properly, will lead to improved allocation of the link between real-time traffic and besteffort traffic when compared to the noncongestion based approach of fixed allocation of bandwidth between real-time traffic and best-effort traffic. This conclusion depends on certain assumptions, such as differentiable, concave and nondecreasing value functions of the arrival rates for both types of jobs. Additionally, we used approximations of functional dependencies between the expected waiting time for each class of jobs and the arrival rates for all job classes. We used these approximation in order to create analytical expressions for computing of prices in real time at each node using only the locally collected information, without the need to coordinate the process from a central location. Acknowledging that the analytical approximations of queuing behavior do not reflect the exact nature of internet traffic, we tested our pricing and bandwidth allocation in a simulated link environment subjected to the bursty arrival patterns. Main set of experiments was designed to compare the link allocation based on congestion based pricing (using analytical approximation of waiting times for jobs in the system) with the static allocation of the link where the proportions of the link capacity given to real-time traffic and best-effort traffic are fixed. The simulation results were encouraging, not only increasing the increase in ability to generate significantly higher net user value but also showing a significant improvement in all relevant network performance measures such as number of packets transmitted, link utilization etc. Also, our experimental results have shown that the prices computed on the basis of analytical approximations, although not reflecting fully the real nature of traffic arrival patterns, can still lead to an improved network performance.

However, a host of other implementation issues still need to be resolved and we consider the work presented in this paper only the first step in addressing the implementation of congestion-based pricing in the regulation of mixed traffic on the public networks. One of the first issues we plan to address in our future work is accounting for future externalities imposed by current submissions of real-time requests. We plan to investigate several different methods of taking future externalities into account, ranging form use of dynamic traffic forecasting methods to implementation of two part tariffs in which fixed component includes average future externalities over the period of subscription time. In conclusion, we recognize of one of the main challenges facing implementation of this or any other differentiated pricing scheme in the context of public networks and open the issue of potential remedies. As pointed out in series of paper and position statements [17], even though the logic of quality and price differentiation is impeccable it unfortunately runs up against very strong preferences for simplicity and especially for at rates. Therefore, it is instrumental that any solution striving to be perceived as practicable incorporates differentiated prices in the context of a simple and stale pricing scheme. One interesting approach to incorporating congestion based pricing with stable and unchanged pricing from the customer’s point of view has been developed by Gibbens and Kelly [5] and is based on the idea of marginal cost pricing implemented by tagging all packets of data appearing in the link during the congestion and setting the price proportionate to the number of tagged packets during the transmission. Packet flow rate would then adjust from period to period through recursive process intended to stabilize the rate around the value matching the predetermined expected charge user is willing to pay. Our pricing approach may be implemented in a similar fashion, allowing users to announce the periodical charge and expected usage and allocating packet values and expected delay costs according to those predetermined parameters. In such setting, our pricing mechanism will serve the same purpose adjusting individual flow rates according to the user’s willingness to pay, as opposed to changing end user prices to reflect changes in network environment. One difference between our approach and above-mentioned method is in definition and measurement of marginal cost used for price setting. In Ref. [5], marginal cost and corresponding price matches the current sate of congestion as expressed by the number of dropped packets. Our approach mandates that along with the number of packets in each flow, associated value of each flow on per packet basis should also be taken into account. In our future research, we plan to devote more attention to this issue, further investigating the tradeoff between optimality of network resource allocation methods and simplicity of their implementations.

## References

[1] S. Blake, D. Black, M. Carlson, E. Davies, Z. Wang, W. Weiss, An Architecture for Differentiated Services, draftietf-diffserv-arch-02.txt (in preparation).

[2] R. Braden, D. Clark, S. Shenker, Integrated services in the internet: an overview, RFC 1633, June, 1994.

[3] C. Courcoubetis, G.D. Stamoulis, C. Manolakis, F.P. Kelly, An intelligent agent for optimizing QoS-for-money in priced ABR connections, Telecommunications Systems, Special Issue on Network Economics.

[4] P.C. Fishburn, A.M. Odlyzko, Dynamic behavior of differential pricing and quality of service options for the internet, Decision Support Systems 28 (2000, March).

[5] R.J. Gibbens, F.P. Kelly, Resource pricing and the evolution of congestion control, Automatica (1999) 35.

[6] R.J. Gibbens, R. Mason, R. Steinberg, Multiproduct Competition between Congestible Networks, University of Southampton Discussion Paper in Economics and Econometrics, No. 9816, 1998, Sept.

[7] A. Gupta, M. Parameswaran, B. Jukic, D. Stahl, A. Whinston, Streamlining the digital economy: can we avert a tragedy of the commons? IEEE Internet Computing, 1997 (Nov. – Dec.) 38–46.

[8] A. Gupta, D.O. Stahl, A.B. Whinston, A stochastic equilibrium model of internet pricing, Journal of Economic Dynamics and Control (1997) 21.

[9] A. Gupta, D.O. Stahl, A.B. Whinston, Priority pricing of integrated services networks, in: J.P. Bailey, L.W. McKnight (Eds.), Internet Economics, MIT Press, Cambridge, MA, 1997, pp. 323 – 352.

[10] A. Gupta, D.O. Stahl, A.B. Whinston, The economics of network management, Communications of the ACM (1999, Sept.) 57– 63.

[11] C. Harris, D. Gross, Fundamentals of Queueing Theory, Wiley, New York, 1998.

[12] R. Johari, Mathematical modeling and control of internet congestion, SIAM News (2000, March) 33.

[13] J. MacKie-Mason, H. Varian, Pricing congestible network resources, IEEE JSAC 13 (7) 1141 – 1149.

[14] H. Mendelson, Pricing computer services: queueing effects, Communications of the ACM 28 (1985) 312– 321.

[15] H. Mendelson, S. Whang, Optimal incentive-compatible priority pricing for the M/M/1 queue, Operations Research 38 (1990) 870 – 883.

[16] A. Odlyzko, Paris metro pricing for the internet, Proceedings of the ACM Conference on Electronic Commerce, 1999.

[17] A. Odlyzko, Should at-rate Internet pricing continue? IT Professional 2 (5) (2000, Sept. – Oct.) 48 – 51.

[18] A. Parekh, R. Gallagher, A generalized processor sharing approach to flow control—the multiple node case, IEEE Transactions on Networking 2 (2) (1994) 137– 150.

[19] D. Passmore, A bandwidth glut, Business Telecommunications Review (1999, Sept.) 18 – 20.

[20] S. Shenker, D. Clark, D. Estrin, S. Herzog, Pricing in computer networks: reshaping the research agenda, Journal of Telecommunications Policy 20 (3) (1996) 183–201.

[21] R. Simon, B. Jukic, W. Chang, Optimal resource allocation for multi-service networks, IEEE/SCS 33rd Annual Simulation Symposium, Washington, DC, 2000, April.

[22] D. Stahl, A. Whinston, An economic approach to client-server computing with priority classes, in: W.W. Cooper, A.B. Whinston (Eds.), New Directions in Computational Economics, Kluwer Academic Publishing, Boston, MA, 1994, pp. 71– 95.

[23] D.O. Stahl, A.B. Whinston, K. Zhang, A simulation study of competitive Internet pricing: AOL at rates versus GSW usage prices, Proceedings of the First International Conference on Information and Computation Economies, Oct. 25–28, ACM Press, NY, 1998, pp. 68 – 76, Available at http://www.acm.org/ pubs/citations/proceedings/dl/288994/p68-stahl/.

[24] S. Stidham, Optimal control of admission to a queuing system, IEEE Transactions on Automatic Control (1985, Aug.) 705– 713.

[25] Q. Wang, J.M. Peha, M.A. Sirbu, Optimal pricing for integrated services networks, in: J.P. Bailey, L.W. McKnight (Eds.), Internet Economics, The MIT Press, Cambridge, MA, 1997, pp. 353– 376.
