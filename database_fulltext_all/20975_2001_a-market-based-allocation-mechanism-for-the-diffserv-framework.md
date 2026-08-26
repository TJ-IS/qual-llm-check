---
otero_id: 20975
otero_key: "MNMK9XFV"
title: "A market-based allocation mechanism for the DiffServ framework"
authors: "Manoj Parameswaran; Jan Stallaert; Andrew B. Whinston"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00143-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A market-based allocation mechanism for the DiffServ framework

Manoj Parameswaran <sup>a,)</sup>, Jan Stallaert <sup>b</sup>, Andrew B. Whinston <sup>c</sup>

<sup>a</sup> DIT, VMH 4350, Smith School of Business, UniÕersity of Maryland, College Park, MD 20742, USA 1 IOM, Marshall School of Business, UniÕersity of Southern California, Los Angeles, CA, USA MSIS, Red McCombs School of Business, The UniÕersity of Texas, Austin, TX, USA

## Abstract

Public networks currently offer only one service model, the best-effort. Increased commercial usage and convergence of networks have led to demand for guaranteed quality of service for a class of premium applications. While such traffic may constitute only a fraction of the network usage, the economic impact would be significant. Current engineering efforts to provide a multi-tier service model center on the DiffServ architecture. The contention of this paper is that a differentiated service model needs to be complemented by economic resource allocation mechanisms which include some form of pricing that provides the right incentives for users and network providers to sustain the model. The paper briefly reviews the DiffServ model, describes a proposed instantiation of it and outlines a market-based allocation mechanism designed to complement such an architecture. The objective is to provide a conceptual framework that shows it is possible to bridge economics and network engineering in deriving a feasible economic model for multi-tier service architecture. The allocation mechanism is initially described for a single domain and later on, extended to multiple domains with individual bandwidth brokers. The paper addresses the issue of bilateral agreements among domains to facilitate interconnection from an economic perspective. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Quality of service; Differentiated service; Internet resource allocation

## 1. Introduction

Traditionally, public data networks have offered a single service model, where all applications are treated equally to best-effort service. In particular, this implies that there are no service level guarantees offered to applications. With the expansion of the scope of the usage from academic and federal purposes, to private and commercial usage, the need for differentiating applications based on their valuation of the usage arose. The associated increase in congestion levels led to the research efforts toward network resource allocation 3 . The Resource Reser-<sup>w</sup> <sup>x</sup> vation Protocol, Integrated Services and Differentiated Services frameworks, are all different directions that successively emerged in the effort towards providing an architecture that supports multiple service classes. Premium applications such as video-conferencing, remote education, interactive multimedia entertainment and virtual leased lines, now hold immense potential for academic and commercial exploitation 1 . While high bandwidth networks and<sup>w</sup> <sup>x</sup> enabling technologies have brought such applications to the realm of the possible, ultimately, they will not be feasible without a multi-tier service model that can offer guarantees about service levels. The abovementioned efforts propose architectural frameworks that define multiple service classes. However, sustaining actual traffic along multiple service levels would require corresponding resource allocation policies.

The public network infrastructure is composed of interconnected, privately owned networks. Further, usage of the network is an economic activity where valuations differ over a wide range. Thus, allocation of resources to individual users, as well as toward interconnection among networks, hold economic impacts. While the need for economic allocation policies and pricing has been recognized, the complexity of the environment has meant that by and large, the business rules governing allocations are simple, feasible rules. In particular, individual users or interconnections among networks are typically not charged with respect to actual usage of resources. Subscription schemes and interconnection agreements which do not necessarily relate to usage dominate the currently practiced allocation policies 7 .

However, the advent of a multiple level service model would be critically dependent on economically justified allocation schemes. Such a service model would typically imply that individual network elements dedicate some resources for higher service classes, and interconnections among networks provide support for inter-domain service guarantees at such higher classes. Providing differential treatment through dedicated resources and service level guarantees would incur costs, further amplified by the overhead in storing, signaling and processing associated information. In the absence of economic incentives, network vendors may not be expected to support such a model. Thus, the provision of multiple service classes should be viewed as an economic problem, as well as a network engineering issue. Network engineering proposals usually leave the allocation policies to be determined extraneously, possibly by individual vendors. Since cooperation among vendors for interconnections become critical, research into what could be sustainable economic allocation policies becomes important. Whereas economists and the engineering community have recognized these issues, the consequent research usually does not represent a blend of the engineering design and economic principles. The idiosyncrasies of the network architecture constrain the resource allocation environment and often, abstract economic models fail to recognize these constraints. Further, any allocation mechanism is required to be computationally feasible in real-time and have minimum overhead, essential requirements for deployment over the Internet. Thus, feasibility and compatibility with the decentralized, connectionless architecture, may override the merits of providing an optimal allocation based on an abstract model 4 .<sup>w</sup> <sup>x</sup>

This paper attempts to address the need for a feasible economic allocation mechanism that can serve to guide allocation of resources for premium usage. Specifically, the premium usage addressed here requires end-to-end service guarantees, with constant latency and minimum, or negligible jitter. In the interest of relating the research to the engineering architecture, the allocation model is framed in the context of the DiffServ framework, where a simple model with two classes of service, best-effort and Premium, is considered. Premium service, as proposed by Van Jacobson, offers a model for constant bit rate service, that we feel, forms an ideal candidate for a preliminary economic model, due to its simplicity. The essential purpose of the allocation model is to determine the economic part of the admission control decision making; that is, to resolve which of the contending applications get allocations for premium service, subject to the bandwidth available at network elements to support such service and the individual valuations of such usage by applications.

Whereas admission control will involve several other aspects, such as security and authentication, the purpose here is merely to suggest how the economic aspects may be addressed and to propose a set of admission control policies. These may, at best, form part of a suite of such policies, and the associated signaling may form part of the messaging infrastructure for the DiffServ architecture. The following sections review DiffServ architecture, briefly address economic issues, review the premium service model and describe the market mechanism. First in the context of a single domain, and later, extended to multiple domains.

## 1.1. ReÕiew of DiffSerÕ architecture

The DiffServ architecture framework is intended to address the issue of providing QoS guarantees, or differential QoS service, to independent flows in a scalable and efficient manner across an inter-network spanning multiple domains that may vary in adminis trative policies, ownership and underlying technolo gies. Essentially, it decentralizes QoS provision to the level of independent domains, each of which has a bandwidth broker. Applications submit requests for ‘calls’ to the BB broker , which makes an admis-Ž . sion decision based on local allocation policies and communicates it to a leaf router in charge of packet classification. The router then accepts the flow from the application, refers to the allocation policy as communicated by the BB and marks each packet in the flow as belonging to one of a few classes, according to the QoS it was granted. These classes are few in number, and the expected treatment of each class is simple enough to be implemented by any individual network element. Thereafter, all pack ets marked as belonging to any one class are treated similarly, resulting in an aggregation, and negating the need for tracking flow level information inside the network. Thus, information processing load is pushed towards the periphery of the network, for scalability with number of flows. In case of inter-do main flows, the BB initiates a call request with all BB’s in the proposed path for this flow. Domains form bilateral contracts with adjacent domains to service aggregate flows, and the other BB’s respond to the call request granting service based on these contracts. For the actual aggregate flows, these con tracts are enforced by edge routers, which bridge the two adjacent networks. Thus, there are two types of contracts, flow level and aggregate. Effective imple mentation of end-to-end allocations would depend on how each of these are designed, and how the aggregates can be unraveled into flow level contracts, orŽ how the flow level contracts may be aggregated into inter-domain contracts . Allocation policies, as well. as design of contracts, are left to individual imple mentations of DiffServ. In general, proposed imple mentations address these as engineering issues. Ac cordingly, QoS request is most often specified as a peak rate in terms of token bucket rate, and policing of QoS involves shaping of flows in accordance with granted rates, dropping and delaying packets. Allocation policies are often guided by the philosophy that flows already in the network must continue to receive the QoS guaranteed to them, without their service being degraded by the incremental allocations. For example, in the Two-Bit architecture 6 ,<sup>w</sup> <sup>x</sup> flows are granted admission only if unallocated bandwidth is available to satisfy their requests; and if they are inter-domain flows, there must be a share of the inter-domain contracted bandwidth available for allocation as well.

## 1.2. Economic issues of allocation

From an engineering point of view, these guidelines seem feasible for achieving end-to-end allocations. In particular, an architecture such as the Two-Bit, which includes a Premium Service, can offer end-to-end QoS with constant latency and minimum jitter or in other words, close to connection-oriented service. However, the environment is not merely an engineering system. It exhibits the characteristics of an economy where scarce resources are to be allocated. For instance, consider the differentiation of services. While such differentiation addresses the problem caused by equal treatment of all applications, the question remains as to how a particular application is classified as belonging to a higher or lower service class. While the engineering design would simply expect each call request to identify itself as requesting a particular level of service, and treat it accordingly, there is an economic issue of providing users incentive to represent their need for service correctly. Otherwise, every user can request higher levels of service and there will be no true differentiation based on valuations. Since providing different classes of service incurs a cost to the provider network, the provider will have no incentive to support the system unless the service classes were correctly priced. Further, when multiple applications request the same resources, a mechanism that allocates resources simply based on availability will not be able to resolve conflicts. An economic mechanism, on the other hand, can do so by differentiating based on user valuations for the same resources.

‘Correct’ pricing in public networks is difficult to obtain, due to the complex, dynamic and stochastic nature of the environment. Research, in general, has focused on deriving approximately correct pricing that is computationally feasible to implement.

## 1.3. Dynamic allocations

DiffServ literature proposes support of a wide spectrum of allocation mechanisms ranging from static allocations based on subscriptions, to fully dynamic, on-demand allocations where each call is priced based on current cost of resources and actual usage. Static allocations may be useful for users that expect a consistent profile of premium usage. However, the bulk of premium QoS applications to be supported by a DiffServ model would be constituted by video-conferencing, multimedia on-demand and similar applications, which are more dynamic in nature. Further, a subscription-only system could lead to inefficient usage, as a limited number of users could subscribe to the available premium capacity, while not using it continuously. Whereas RED-like algorithms at network elements could facilitate usage of idle premium capacity by best-effort traffic, this would still mean that providers forego revenues in premium traffic not serviced, and that potential users lose utility while the capacity is available. The mechanism we propose is essentially dynamic in nature but actual implementations could, if necessary, derive subscription rates from such a mechanism.

The existence of economically justified prices would provide incentives for users to choose the service class that best matches their valuation of usage, and for providers to support the model of multiple service classes. The most important criterion in DiffServ and related proposals has been expedient deployment for both experimental purposes and actual usage. Since the ‘public’ networks are actually a collection of privately owned networks, an incentive compatible economic allocation mechanism is essential to facilitate such deployment. Nichols et al. 6 use the airline service class analogy <sup>w</sup> <sup>x</sup> to argue that the small number of passengers in premium classes form a crucial part of the economic model for airline industry and the differentiation serves to provide a ‘healthy’ economic environment. If such economic rationale form the motivation to provide a differentiated service model, it is essential that the allocation mechanisms used make sense from an economic point of view. We describe the allocation mechanism in the context of the Premium service model 5 , a particular proposed instantiation <sup>w</sup> <sup>x</sup> of the DiffServ conceptual framework, which was later incorporated into the two-bit architecture 6<sup>w</sup> <sup>x</sup> which included a provision for Assured services 2 .<sup>w</sup> <sup>x</sup> In this paper, we limit our focus to premium services, to illustrate the allocation mechanism. In the following section, the premium service model is briefly reviewed.

## 1.4. Premium serÕice model

Premium service is guaranteed, as with a telephone call, in that the user expects to find the capacity when initiating a call. The contracted parameter is a peak-rate for the flow. At the start of the flow, packets are shaped to conform to the contracted peak-rate and at intermediate elements, premium-tagged flows are serviced by a higher priority queue. The size of the queue at each element determines the total allocations it can support, and the model is designed so that with reasonable sizes, the flows can proceed with negligible queuing delay. Thus, premium service practically constitutes a virtual network which is providing close-to-connection-oriented service. The contract also specifies allowed burst size, which is also enforced at the entry point. Premium traffic model has a strict no-oversubscription rule, as the network contracts to provide the specified rate deterministically. This also means that pricing is crucial to control subscription and there is no need for complex queue management policies.

## 1.5. Market-based allocation mechanism

## 1.5.1. Assumptions

The market-based model described below, uses double actions where applications submit bids specifying source, destination, peak rate and a bid price, which is a per-period price they are willing to pay

for the flow, and network elements specify bids stating the available capacity and the asking price for unit capacity per period. A ‘Market Process’ located at the bandwidth broker in each domain conducts double auctions which compute the allocations based on these bids. It is assumed that the forwarding paths for given source destination pairs are known to this process, that is, path computation is not part of the market-based allocation. The BB constructs bundles based on these paths, by assembling capacities at individual nodes that constitute the path for each requested flow. Thus, the ‘commodity’ sold is an artificial bundle constructed from capacities at individual nodes. This bundling ensures that the buyer gets the allocation for the entire path and does not have to incrementally build an allocation as in the case of RSVP. The peak rate is a token bucket rate enforced at entry point and at each node, the ‘capacity’ refers to the total number of premium packets the queue can service in that period. Thus, if a node specifies x as available capacity, it denotes the aggregate of peak-rates for premium traffic that can be serviced at that node in the following period. Burst rate is not factored into the market allocation model and is assumed to be pre-determined as an engineering decision. Possibly, the lowest of allow able burst rates among constituent elements in the path for a flow could be quoted as allowable burst rate to the bidder, and the application may choose to submit a bid based on whether that is acceptable. An application is assumed not to have any value in obtaining allocation for less than the requested peak rate, as in obtaining allocations that are not available over the entire path. In the following discussion, market process refers to Bandwidth Broker, users refer to applications, and capacity refers to the contracted rate for applications, and the available capac ity on the higher priority queue for network nodes. The auctions are assumed to be performed indepen dently of other components of the admission control, such as rules for enforcing security. These may be used to filter out bids prior to the auctions. The allocations referred to here are ONLY for the premium service class applications, and the resources being allocated are only the available capacity to support the premium class of applications. The decisions on the rate of premium traffic that can be supported at individual nodes, as well as the proportion of net traffic that is constituted by premium traffic are assumed exogenous and may be made based on traffic profiles and available queues at individual network elements. That is, this model does not seek to optimally allocate network resources for all service classes; rather, it seeks a feasible allocation scheme that facilitates deployment of a differentiated service model where premium resources are priced and allocated in a nearly optimal manner.

## 1.6. Market model

First, the market for the special case where the network consists of one administrative domain in-Ž tranet, or Atrusted regionB. is described, which is suitable for a small autonomous network. Later, the model is extended to larger networks and the coordination among multiple domains is introduced. Individual call requests specify the source, destination and required capacity for the flow along with a bid price. Nodes submit offers specifying the capacity available for allocation, and an ask price. The bandwidth broker identifies the nodes constituting the path for each request and constructs bundles.

The market M1 operates as a sealed bid periodicŽ . <sup>1</sup> double auction call market . The call requests areŽ . indexed by $j ,$ the nodes within a domain by i and $j = 1 , \ldots , n$ and $i = 1 , \ldots , m$ . The rate requested by the offer $j$ is $q _ { j }$ , the total capacity available at node i is $c _ { i } .$ We assume that the maximum price the user j is willing to pay for allocation per unit isŽ . $- v _ { j }$ $( v _ { i } < 0 )$ and the minimum price node i requests for selling its capacity $c _ { i }$ is $v _ { i } \ ( v _ { i } \geq 0 )$ . Let $z ^ { j } \in \Re ^ { m }$ be the vector of capacities requested by request j, i.e. $z _ { i } ^ { j } = q _ { j }$ if capacity of $q _ { j }$ is requested on node $i ,$ and $z _ { i } ^ { j } = \dot { 0 }$ otherwise. Of course, the $z _ { i } ^ { j } > 0$ represent a connected path within the domain. Denote the matrix Z as $\mathbf { Z } = \left[ \begin{array} { l } { z ^ { j } } \end{array} \right| - c _ { i } \pmb { e } ^ { i } \big ]$ where $e ^ { i }$ is a unit vector having 1 for the $j ^ { \mathrm { t h } }$ element. Specify the vector $z _ { o } \ \mathrm { a s }$

$$
\mathbf {z} _ {o} ^ {j} = v _ {j} q _ {j} \qquad j = 1, \ldots n
$$

$$
\boldsymbol {z} _ {o} ^ {n + i} = v _ {i} c _ {i} \qquad i = 1, \ldots , m
$$

The market problem then becomes:

$$
\min \boldsymbol {z} _ {o} \cdot \boldsymbol {x}\tag{M1}
$$

$$
\text { subject   to: } \mathbf {Z} \cdot \mathbf {x} \leq 0
$$

$$
\boldsymbol {x} \in \{0, 1 \} ^ {n} \times [ 0, 1 ] ^ {m}
$$

The objective function represents the surplus value in the system, which is the sum of differences between the valuations of flows and the valuations for specified capacity for the flow at the nodes making up the corresponding bundles. Note that Ž $v _ { j } < 0 ;$ hence the minimization ..

Each row of the Z matrix corresponds to a node. The Z matrix has the first n columns corresponding to the call requests, with non-zero values on the rows corresponding to nodes forming part of the bundle for each flow. The last m columns correspond to the nodes, with the capacity of the node represented on the row corresponding to that node $( - c _ { i } e ^ { i } )$

The first n elements of the column vector x are constrained to be either 0 or 1 and indicate whether the corresponding request is allocated or not. Since the users gain utility only if they obtain allocations for the amount of capacity they requested a video-Ž stream requiring, say, 1 Mbps to provide a consistent frame rate, has no use of getting half of it , bundles. can either be allocated fully or not at all. Hence, the  4 0,1 restriction, which captures the combinatorial nature of the auctions. The next m elements indicate the fraction of available capacity at each of the m nodes that is allocated in the aggregate and are hence constrained to be in the interval 0,1 .<sup>w</sup> <sup>x</sup>

The constraint, $\mathbf { Z } \cdot \mathbf { { x } } \leq 0$ ensures that the capacity constraint at each node is satisfied. The combinatorial nature of auctions rules out direct solutions and we need to use heuristic methods to find an allocation. We solve the model with algorithms designed to be feasible in real time. Since the model yields a mixed-integer programming problem, an allocation does not necessarily directly yield transaction prices; which are usually determined as dual prices. The simplest solution would be to set transaction prices at the values that requests specified in their bids.<sup>2</sup>

## 1.7. The market clearing heuristic

Since our objective is to maximize the net economic value of the system, we base our heuristic on making the allocations in descending order of surplus per unit capacity per node, subject to the capacity constraints. For call request $j ,$ surplus per unit capacity $S _ { j }$ is given by

$$
S _ {j} = \sum_ {i = 1} ^ {m} v _ {i} I _ {i} ^ {j} + v _ {j} \quad j = 1, \dots , n
$$

where $I _ { i } ^ { j }$ is 0 if $z _ { i } ^ { j } = 0$ , 1 otherwise. The surplus for request j per node, $s _ { j }$ is then given by,

$$
s _ {j} = S _ {j} / \sum_ {i = 1} ^ {m} I _ {i} ^ {j}
$$

The call requests are sorted on $s _ { j } ,$ in ascending order. Recall thatŽ $v _ { i } < 0 )$ . Starting with the lowest, requests are allocated if $( 1 ) \ s _ { i } < 0$ Ž . and 2 $q _ { j } \leq c _ { j }$ , ; $I _ { i } ^ { j } = 1$ . As each request is allocated, each $c _ { i }$ where $I _ { i } ^ { j } = 1$ is decremented by $q _ { j }$

The entire heuristic involves only lightweight computation and is executed only in the market process, not at every node. Thus, each and every participating element is not burdened with processing and storage of local, proprietary policies.

## 1.8. Inter-domain flows

## 1.8.1. Inter-domain flows in premium serÕice model

The Premium service model envisages bilateral agreements among bordering domains to ensure interconnection and support of inter-domain premium flows. These agreements simply specify the aggregate rate of premium traffic that one domain is allowed to forward to the second through a given egress point. It is enforced by an egress router, which shapes the aggregate traffic to conform to the contracted peak rate and an ingress router, which polices the traffic to verify compliance, and may drop packets exceeding the rate. At the allocation level, the Bandwidth Broker does a call-setup by communicating with BBs in domains along the path, and each domain-to-domain allocation for an individual flow is made only if sufficient bandwidth is available at the egress point. The key engineering issue here is that the local allocations and border allocations should be related to each other. The actual availability of resources at various nodes in second domain are not known to the first BB and unless there is a link between contracting and pernode allocations, individual flows may suffer in that even if egress is allocated, the forwarding path within the next domain may not be fully supported.

## 1.8.2. Economic issues: incentiÕe compatibility

Even if a BB–BB call set-up process were to ensure verification of available capacity along the forwarding path in downstream domains for a call, the autonomous nature and private ownership of domains could raise potential economic issues. The bilateral agreement should involve some form of transfer payment among vendors, to motivate supporting inter-domain flows, which incur opportunity cost of local traffic not serviced and revenues forgone thereby. Unless this payment were linked to the opportunity cost, the vendors would have no incentive to support the inter-domain flows. Further, even in the presence of such contracts, it is possible for a vendor to contract for a rate higher than that available and later default on it, unless sufficient economic mechanisms were in place to ensure compliance. This is the familiar problem of incentive compatibility in economics, and we address this issue by introducing a penalty in the contracts for traffic not serviced according to contract. In the revised model, the net revenues for an individual domain would be net of the penalty paid out to neighboring domains. We frame the new optimization problem for the domain which accounts for inter-domain contracts, by adding dummy nodes with capacity equal to the contracted rate in the bilateral agreement. The dummy nodes occur in place of egress and ingress points, and local paths terminate or start from these dummy nodes, in case of inter-domain flows. With this modification, the allocation problem is seen as a local problem by the market process. We first describe the inter-domain market and later explain the penalties and design of contracts that form the basis for bilateral agreements.

## 1.8.3. Inter-domain market

On the inter-domain market, only simple assets are traded: aggregate capacities within a certain domain.<sup>3</sup> The market node here has a role similar to the NYSE specialist. The node takes a position by selling short aggregated capacity in the domain, which Ž . will later be bought from the intra-domain nodes. Essentially these trades result in domains buying futures contracts for aggregate capacity in other domains. Traders in the inter-domain market are market nodes from other domains. Domains guarantee that with probability S, the future capacity sold will get allocated for forwarded premium traffic. Note, that we would like S to be 1, but because of node failures and the unknown composition of the requested bundle, S<sup>s</sup>1 cannot be guaranteed. Assume that other domains submit bids $( \mathcal { Q } _ { j } , \ v _ { j } )$ for an aggregated capacity of $\mathcal { Q } _ { j }$ and a maximum price of $- { v _ { j } } ^ { 4 }$ Also, assume that the market node computes ${ \mathcal { Q } } ,$ , Õ where:

Q: maximum sum of aggregated capacity to be sold,

Õ: minimum price for one unit of aggregated capacity.

We allow requests for aggregated capacity to be partially fulfilled. Assume that the pairs $( \mathcal { Q } _ { j } , v _ { j } )$ are ordered such that $v _ { j } \leq v _ { j + 1 }$ . Under our rule, the first k orders are traded, where k is the biggest integer such that:

$$
\Sigma_ {(j = 1 \dots k)} q _ {j} \leq Q
$$

and

$$
v _ {k} \leq v
$$

The transaction prices would then be min $[ v _ { \mathrm { k + 1 } } ,$ 4 Õ and the $( k + 1 ) ^ { \mathrm { { \bar { t } } h } }$ order will be partially filled if $\Sigma _ { ( j = 1 \dots k ) } \ q _ { j } < Q .$

One domain may submit more than one bid. For example, it may submit a Ahigh priorityB bid for a small chunk of capacity for a high price, and submit lower-priced bids to acquire some extra capacity that could be used for lower priority traffic. In that case, we denote the total capacity reserved by domain D by $\mathcal { Q } _ { D }$

## 1.8.4. UnraÕeling futures contracts intra-domain( market)

There are two aspects to restating the intra-domain market model to account for inter-domain flows and futures contracts. Dummy nodes are introduced to intra-domain markets, where each node has the capacity equal to aggregate capacity bought from a neighboring domain through a futures contract. The dummy node essentially becomes the gateway to the neighboring domain and all inter-domain requests will have the path bundles terminating at the dummy nodes corresponding to the neighboring domain they connect to. The second aspect is the introduction of inter-domain requests forwarded by neighboring domains, to contend with local requests for allocations Žwhen a locally originating inter-domain request clears with the path including a dummy node, effectively, the request has the local portion of the bundle cleared and is forwarded to the next domain for dis-aggregation and clearance of the rest of the bundle. ..

Since only the aggregated capacity is specified when the inter-domain requests are handled, the dis-aggregated bundle with requests for specific nodes may contain anywhere from 1 up to m nodes.

There is no additional income from granting requests that have already been sold in the futures market. However, there is a penalty, $\gamma _ { j }$ for not granting a request $j$ to domain D if $\begin{array} { r } { \sum _ { j \in R ( D ) } q _ { j } \le \mathcal { Q } _ { D } } \end{array}$ where R D( ) are the outside requests from domain D for a path with destination $d _ { j }$ and capacity on theŽ path of . $q _ { j } ,$ and $\mathcal { Q } _ { D }$ is the total aggregated capacity reserved by domain D. So, after request $j \in R ( D )$ has been dis-aggregated into specific node requests $z _ { i } ^ { j } ,$ intra-domain market becomes:

$$
\min \gamma \cdot \left(\mathbf {1} - \boldsymbol {x} ^ {0}\right) + z _ {0} \cdot \boldsymbol {x}
$$

$$
\text { subject   to: } - \mathbf {Z} ^ {0} \cdot \left(\mathbf {1} - x ^ {0}\right) + \mathbf {Z} \cdot x \leq - \mathbf {Z} ^ {0} \cdot \mathbf {1}
$$

$$
\boldsymbol {x} ^ {0} \in \{0, 1 \} ^ {n ^ {0}}, \boldsymbol {x} \in \{0, 1 \} ^ {n} \times [ 0, 1 ] ^ {m}
$$

With $\boldsymbol { x } ^ { 0 }$ the Boolean vector of outside requests granted when $x _ { i } ^ { 0 } = 1$ , and $n ^ { 0 }$ the number of outside requests that need to be dis-aggregated because of their reservation in a prior period. The sum vector, 1, is a column vector of 1s.

## 1.9. Contract enforcement

The penalties are used to prohibit the market node from selling capacity to neighboring domains and later not granting the requests. The calibration of $\gamma$ will ensure that the reserved capacity $Q$ sold in the inter-domain market will neither be undersold, nor oversold. In the first case, this leads to a non-optimal utilization of the resources, in the second case, the system will behave in a non-predictable manner since even though capacities have been reserved capacity will only rarely be obtained. Setting  too high would result in underselling, implying underutilization of capacity and loss of revenues; setting too low leads to overselling, which will imply networks not being able to meet the commitment, leading to unpredictable scenarios. It can be shown that setting $\gamma _ { j } = S / ( 1 - S ) \mathrm { m i n } \{ v _ { k + 1 } , v \}$ will prevent under- and over-selling. Or, in other words, in order to ensure that a pre-purchased chunk of capacity will be dis-aggregated successfully with probability S, it suffices to set $\gamma _ { j }$ as stated.

## 2. Results

We are running a series of simulations of simple network scenarios to assess the market performance and computational load. The results for a typical domain in our experimental framework, in terms of the net surplus over 60 periods, are plotted below for two different scenarios Figs. 1 and 2 ; it can be seenŽ . that the system converges quickly. It was observed that congested nodes restrict allocation to higher surplus requests and that the surplus achieved reasonably approximates the optimum. Investigating alternate allocations in periods where throughput was lower due to congestion, did not yield a higher surplus in most cases. The slight fluctuation in the surplus curve after it has converged is due to recurrence of congestion, which is relieved as earlier flows terminate and allocations are restricted. The system responded to congestion quickly. Some of the performance measures we are studying include utilization of capacity, throughput and computation time. These results will be compared against a benchmark model that simulates the premium service model without any economic resource allocation mechanism.

![](/api/attachments/MNMK9XFV/fulltext/images/c354cfe4381c484b6e602b895e2067c5591df5b1cfa6fe50d92a00c087bb70d7.jpg)  
Fig. 1. Net Surplus in a single domain network.

## 3. Ongoing research

Currently, transaction prices are set the same as the bid prices for successful call requests. This works fine as all the nodes within an AS are owned by the same vendor, and for inter-domain flows, the payments are decided by the forward contracts, not by individual transaction prices. However, transaction prices can signal information to the bidders as to resource availability and hence, are important. Bidders can use these prices to update their bids in subsequent periods, vendors can use this information in deciding on the capacity sold to neighboring domains. Since the optimization problem involves a mixed integer-programming model, dual prices cannot be derived, as is normal practice.

The other purpose of deriving transaction prices is to determine how the surplus will be distributed among the agents. For instance, if the prices are set at the reservation values specified by buyers’ bids, the entire surplus goes to the sellers. Logically, the transaction price should fall somewhere between the bid and ask prices; indeed, when dual prices can be derived, this is what occurs. In combinatorial auctions where dual prices cannot be derived, different criteria are used to choose prices in the interval between bid and ask prices, the simplest being to set it midway in the interval. However, in our case, the commodities that the sellers specify prices for are node capacities, and the commodities bought are bundles of node capacities. Hence, we cannot directly relate the two sets of reservation values. A possible approach is to divide the total surplus from a request into half, with one half going to the buyers and the other half to the sellers. The second half may be apportioned among the sellers equally. However, setting prices using such a rule may not signal congestion at nodes efficiently. A useful criterion may be to determine the marginal value of adding a unit of capacity to a given node; if the node is congested, the value will be significant, if the node has slack, there will be no value in adding capacity. However, the bundled markets and the combinatorial nature of auctions render it complex to come up with a method of determining the marginal value. Hence, we are testing different methods of deriving prices, to test their effectiveness in signaling congestion and in distributing surplus.

![](/api/attachments/MNMK9XFV/fulltext/images/94e61cbdbf945f6769292536abec4d06a9c3dca8d082ad0cd37b0b41e0a7e815.jpg)  
Fig. 2. Net Surplus in a two domain network with inter-domain flows.

We are also working on different smoothing algorithms to derive values of $\mathcal { Q }$ and Õ, used in contracting. These take the information from previous periods to refine the values and we investigate whether a steady state is attained with maximum surplus. In turn, this work is expected to yield guidelines on designing incentive compatible contracts.

## 4. Conclusions

We have described a resource allocation mechanism consisting of markets and bilateral agreements to complement the Premium Service DiffServ model by providing sustainable economic functionality. Markets induce users to reveal their valuations of resources so as to facilitate allocation, bilateral agreements are designed to provide the vendors sufficient incentive to support inter-domain allocations. The essential objectives are to improve allocation efficiency, to facilitate inter-domain Premium flows in the presence of multiple owners of the network infrastructure and to be computationally feasible. Initial results of simulation experiments have been encouraging.

While resource allocation is a serious issue for network traffic in general, the network environment as a whole is not easily amenable to economic modeling. While there have been significant efforts to introduce economic mechanisms of resource allocation, all of them stumble when it comes to the engineering details of feasibility and accounting for the varied and complex nature of traffic. In this respect, Premium traffic poses a better-defined problem. While we focus on this problem, we recognize the fact that resource allocations for different types of traffic are interdependent. In allowing for nodes to specify their reservation values for the capacity, we seek to capture the existence of an opportunity cost. It is quite possible that these valuations may depend on some form of usage-based pricing mechanism for network traffic that vendors may deploy or in the absence of such mechanisms, vendors may use their own cost estimates.

## Acknowledgements

This research was funded in part by a grant from Intel.

## References

<sup>w</sup> <sup>x</sup>1 S-Y. Choi, D.O. Stahl, A.B. Whinston, Economics of Electronic Commerce, Macmillan, 1997.

<sup>w</sup> <sup>x</sup> 2 D. Clark and J. Wroclawski, An Approach to Service Allocation in the Internet, Internet Draft,<sup>-</sup>draft-clark-diff-svc-alloc 00.txt<sup>)</sup>, August 1997 .Ž .

<sup>w</sup> <sup>x</sup> 3 A. Gupta, D.O. Stahl, A.B. Whinston, A stochastic equilibrium model of internet pricing, Journal of Economic Dynamics and Control 21 1997 .Ž .

<sup>w</sup> <sup>x</sup> 4 A. Gupta, B. Jukic, M. Parameswaran, D.O. Stahl, A.B. Whinston, Streamlining the digital economy: how to avert a tragedy of the commons, IEEE Internet Computing 1 6Ž . Ž . 1997 November<sup>r</sup>December.

<sup>w</sup> <sup>x</sup> 5 K.Nichols, Using Premium Service to Provide Internet2 QoS, Internet2 Technical Paper May 1998 .Ž .

<sup>w</sup> <sup>x</sup> 6 K. Nichols, V. Jacobson and L. Zhang, A Two-Bit Differentiated Services Architecture for the Internet, Internet Draft, <sup>-</sup> draft-nichols-diff-svc <sup>)</sup> http:<sup>rr</sup>www-nrg.ee.lbl.gov<sup>r</sup> papers<sup>r</sup>2bitarch.pdf November 1997 .Ž .

<sup>w</sup> <sup>x</sup> 7 P. Sriganesh, Internet cost structures and interconnection agreements, in: L.W. McKnight, J.P. Bailey Eds. , InternetŽ . Economics, MIT Press, Cambridge, 1997.

<sup>w</sup> <sup>x</sup> 8 R. Wilson, Incentive efficiency of double auctions, Econometrica 53 5 September 1985 .Ž . Ž .

![](/api/attachments/MNMK9XFV/fulltext/images/f55f26ad524769fe6f795fbfdbaa2befbb06173c377d7895b40a6b0b4f7ffd69.jpg)

Jan Stallaert is an Assistant Professor at the Marshall School of Business at the University of Southern California, Los Angeles. Dr. Stallaert’s research focuses on the interplay between Economics, Information Systems and Organizational Theory. His past research has focused on developing new types of Decision Support Systems and their organizational impact. More recently, he has directed his attention to the new opportunities created by Electronic Commerce.

He has designed and developed a patented method for trading assets in bundles, a method that has a wide variety of applications, from Financial Portfolio Theory, Financial Derivatives Trading to Creating Internal Markets for Knowledge and Supply Chain Coordination.

![](/api/attachments/MNMK9XFV/fulltext/images/f1c5913d2cb044cfd6413fe0a779b78a4e26248b37a487629b49ed4212e9e2ec.jpg)

Manoj Parameswaran is Assistant Professor at Decision and Information Technologies Department at the Robert H. Smith School of Business, University of Maryland. He holds a joint appointment with the Institute for Systems Research and is a research associate at the Center for Research in Electronic Commerce at the University of Texas, Austin. His research and teaching interests include logistics of digital products, electronic markets, telecommunications and

industrial organization in the digital economy. He has worked on network resource allocation for unicast and multicast distribution of multimedia products. His article on economic issues of electronic commerce was featured in The Financial Times.

![](/api/attachments/MNMK9XFV/fulltext/images/f427604d61b22aea1762f91e12804d9dd1bd881f2d17bea0d48309daa71baa3e.jpg)

Prof. Andrew Whinston is the Hugh Roy Cullen Centennial Chair Professor in Information Systems at the McCombs School of Business in the University of Texas at Austin. He is a Professor in the departments of Economics and Computer Science as well. Prof. Whinston is a Fellow of the $\mathrm { I C } ^ { 2 }$ Institute, Austin and is the Director of the Center for Research in Electronic Commerce at the McCombs School of Business in the University of Texas at Austin. His re-

search areas include Artificial Intelligence, E-Commerce, Information Systems and The New Economy. His recent books include Frontiers of Electronic Commerce, Readings in Electronic Commerce, Electronic Commerce: A Manager’s Guide, The Economics of Electronic Commerce, The Internet Economy: Technology and Practice SmartEcom.com , Handbook on Electronic Com- . merce, and Electronic Commerce and Revolution in Financial Markets forthcoming . He has also published over 250 papers in Ž . leading academic journals in Economics, Business and Computer Science. Prof. Whinston received his PhD in management from Carnegie Mellon University in 1962.
