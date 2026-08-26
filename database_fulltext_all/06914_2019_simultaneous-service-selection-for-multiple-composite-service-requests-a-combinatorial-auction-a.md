---
otero_id: 6914
otero_key: "QZHEPN4W"
title: "Simultaneous service selection for multiple composite service requests: A combinatorial auction approach"
authors: "Mahboobeh Moghaddam; Joseph G. Davis"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.03.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Simultaneous service selection for multiple composite service requests: A combinatorial auction approach

![](/api/attachments/QZHEPN4W/fulltext/images/978fa8e62198893115131447e7e51586fdb66d72bbe120952d962ec33df8a622.jpg)

Mahboobeh Moghaddam<sup>a,⁎</sup>, Joseph G. Davis<sup>b</sup>

<sup>a</sup> Australian Institute for Business and Economics (AIBE), The University of Queensland, Brisbane, QLD 4102, Australia <sup>b</sup> School of Computer Science, The University of Sydney, Sydney, NSW 2006, Australia

## A R T I C L E I N F O

Keywords: Web services Combinatorial auctions Service selection Service markets Service composition

## A B S T R A C T

Emerging developments in service-based systems have contributed to a range of proposals for the rapid development of complex applications by composing existing web services through standards-based interfaces. With the availability of a large number of such services offering identical functionality at varving levels of price and other Quality-of-Service (QoS) parameters, selecting the best web services for composition is critical– the problem referred to as composite service selection (CSS). Extant CSS approaches have tended to offer solutions to the problem for a single composite service. We extend CSS to address the setting involving multiple, simultaneous composite service requests. We propose a service selection mechanism based on combinatorial auctions to solve this problem by simultaneously matching the web service ofers and requests and performing extensive evaluations in four market sectors with varving economic sizes and complexity of requests. The results indicate that the proposed simultaneous mechanism achieves a higher success rate in allocating services to requesters compared to sequential matching mechanisms. While the average cost diference in procuring composite services under the two mechanisms is not statistically significant, the simultaneous mechanism achieves more stable and homogenous costs over time.

## 1. Introduction

Web services are self-contained, modular business applications with open, Internet-oriented, standard-based interfaces [1]. Service-oriented architecture and web services technology ofer efective means to achieve interoperability among heterogeneous entities over the In ternet. As a result, web services have been proposed as the technology of choice to implement the service concept in cloud computing [2], Internet of Things (IoT) [3], mobile applications [4], Data Services [5], among others.

However, a single web service can rarely satisfy the user's needs fully [6]. Service composition techniques facilitate the creation of complex functionalities by composing already existing web services based on a composition plan. The composition plan (e.g. a business process or workflow specification) defines the set of tasks required to achieve the complex functionality along with the control and data flows among them. In order to create an executable composite service, one web service should be selected for each task.

There is a growing number of web services over the Internet<sup>1</sup>; many of these services provide similar functionality at diferent levels of quality of service (QoS) parameter values and price. Selecting an optimal set of web services from all the available candidates while considering the impact of the individual service's QoS levels on the end-toend quality of the composite service constitutes an important problem referred to as ‘quality-aware Composite Service Selection’ (CSS) [7–10].

Web services researchers have addressed the composition problem in a range of domains including cloud computing [2,11], IoT [12,13], mobile applications [4,6], and open data [14]. In IoT, for example, service composition is often seen as presenting the opportunity to create potentially complex yet flexible applications relying on an ecosystem of simple and well-defined components [12]. In cloud computing, typical working composite services are described to demonstrate the practicality of service composition for cloud services. Ye et al. [15], for instance, presented a scenario in which a composite application was needed to generate videos from 3D scene files. This was created by compositing three existing services in the cloud: a 3D scene model transforming service, a rendering service, and a video creation and output service.

However, in practice, it is rarely a “single” requester who requires composite service selection. With increases in scale, many composite service (CS) requesters simultaneously request web services to execute their compositions. While each requester can be serviced separately, a logical extension would be to address service selection in the presence of many CS requesters and web service providers who seek matches. Such settings introduce competition among the service requesters for the service providers' limited resources. While the increased number of web service providers gives the service requesters' greater choice, it also creates greater competition among those providers to ofer more services to avoid under-utilization of their resources and increase revenues [16].

Existing CSS research has addressed a variety of related concerns [17–20]. However, little is known about how existing CSS approaches can be efectively extended to the setting with multiple CS requests. To address this problem, we propose a mechanism based on combinatorial auctions to match multiple CS requests (from one to many service requesters) with the existing web service ofers (of one to many service providers) simultaneously; i.e. the “simultaneous auction” mechanism. The combinatorial auction model allows service providers to ofer their services in bundles [21]. This enables them to exploit inter-service complementarities and improve the QoS or price of their ofered services [10]. We also investigate the tradeofs involved in performing service selection for the case of each request independent of other re quests and for the case when CSS is performed simultaneously for all the requests. The requests may originate from the same or diferent requesters and could be for similar CSs or diferent ones. No relationship or dependency between CS requests is assumed. The main contributions of this paper include:

i) We developed mechanisms for service selection in the presence of multiple, simultaneous composite service requests. This problem has significant resonance in areas such as cloud computing and IoT in which there is an emerging need to develop complex applications by composing web service components $[ 2 , 4 , 6 , 1 1 - 1 4 ]$

ii) We designed two variations of the simultaneous auction mechanism, “full-matching” and “partial-matching”, and developed Integer Linear Programming (ILP) formulations for them. In the fullmatching case, a match is sought for all requests while partialmatching relaxes this assumption and aims to find matches for the largest feasible subset of requests.

iii) We carried out comprehensive experimental evaluation and analyzed the tradeofs in various settings and in comparison with two baseline mechanisms. Our results show that the key benefit from the combinatorial auction model may not be the price diferences as much as the stable and predictable outcomes over time which is highly valued by many of the players.

The rest of this paper is organized as follows: Section 2 presents background information on auction models. Related work is discussed in Section 3. Section 4 presents our approach based on combinatorial auction models to simultaneously solve service selection for multiple CS requests and the two variations of the solution. Section 5 describes the evaluation process. The results of the experimental evaluation are discussed in Section 6. Section 7 provides a discussion of the results and implications of our research. Section 8 concludes the paper and outlines future work and limitations.

## 2. Background information: Auctions

We adopt a combinatorial model to manage the complexity of service selection for multiple CS requests and web service offers. The auction model enables dynamic pricing and the combinatorial auction model allows for taking into account the dependencies between atomic services that attend a composition. We present below the concept of dynamic pricing and combinatorial auctions.

Auctions have been used as a key trading mechanism in markets for centuries, typically when there is no standard valuation for the item to be traded and there is a need for price discovery. Setting the right price for a product or service goes beyond the estimation of the cost and minimum profit; rather, it is governed by a complex set of variables which include supply and demand, competitor pricing, and the lifecycle of the product, among others.

Dynamic pricing is an important concept at the heart of auction theory. Dynamic pricing is defined in contrast with the traditional static (fixed) pricing in which the seller fixes the price and the buyer has to take the ofer or leave it. In a fixed pricing approach, the prices might change only in the relatively medium to long term, based on market fluctuations [22,30]. For many products and services, fluctuations occur constantly, making it costly for producers to frequently adjust the prices. In dynamic pricing, the price of a product or service is determined by a market mechanism, such as an auction. For web services which are characterized by dynamic execution environments (in terms of the provider's available resources) and users with diferent and changing demands, dynamic pricing presents a good fit.

Auctions can be categorized based on a range of attributes. Two of the types most relevant to our problem are discussed below. A more comprehensive review of auction types and attributes is presented in [23].

## 2.1. Direct/reverse auctions [24]

Traditionally, auctions have been used for selling products; i.e. di rect auctions. However, the same theory applies when the auctioneer aims to buy products or services; i.e. reverse or procurement auctions. Procurement auctions are popular mechanisms for supply chain management.

## 2.2. Single-item/multi-item (combinatorial) auctions [21,25]

In an auction setting where multiple items are auctioned simulta neously, bidders might be allowed to bid for single items (a non-combinatorial auction) or bid for a combination or bundle of items; i.e. combinatorial auctions. Bundling is particularly important when bidders have preferences not just for specific items but for bundles due to the complementarity or substitutability efects among the items [21]. Bundling is proven to increase economic eficiency due to the allowance for the bidders to more fully express their preferences for combinations of items [21].

## 2.3. Single-sided/double-sided auctions [26]

In a single-sided auction, only one side (either seller or buyer) submits their bids and the auctioneer decides the winners of the auction. In a double-sided (exchange) auction, both buyers and sellers submit their bids and the auctioneer matches the buyers and sellers.

## 3. Related work

We present our review of related work under three categories: service selection (i) for a single task, (ii) for a composite service, and (iii) for multiple composite services. In each category, the web service's QoS profile, the provider's ofered values for service QoS attributes, plays a central role [17]. The service selection process takes the QoS attribute values as inputs and selects the best service(s) based on the user's preferences and constraints.

## 3.1. Single service selection

This deals with service selection performed to choose the best service for a single task. Single service selection research tends to focus on service recommendation and ranking, where the aim is to highlight/ recommend the best service for the service user/requester. Recommendation is mainly based on QoS attributes, but researchers try to improve the recommendation accuracy by incorporating other factors such as the temporal dynamics of QoS attributes [27], user location [28], customer satisfaction with web services [29], user's personalized factors [30], etc. The output of a service recommendation system can be fed to a CSS process to ‘warm-start’ service selection with a more relevant set of services rather than the pool of all the available web services.

## 3.2. Composite service selection

The objective of composite service selection is to select an optimal set of web services that can collectively achieve a specific complex functionality from the pool of available services. The most natural approach to solve the CSS problem is to map it to an optimization problem. Optimization can be performed at two levels: local optimization for an individual task [31], and global optimization for the whole composite service [32–34]. Local approaches may not lead to global optimality for the end-to-end QoS of the composition. Besides, it may not be possible to set global quality constraints for the CS. As for global approaches, optimization is carried out for the composition, and the requester can define end-to-end requirements and constraints. It is still possible to have local constraints for individual services. Optimization approaches have adopted a variety of techniques, including integer linear programming [32,34], linear programming [35], genetic algorithm [8,36], and particle swarm combined with simulated annealing [37].

Composite service selection has also been studied from a game theoretic perspective focusing on extracting the cost function of selfinterested service providers [38] or by generating a Nash equilibrium for service providers' pricing strategy, without forcing them to disclose their private information [39].

Double auction models are also employed for CSS, especially in the cloud [40,41]. In these studies, the assumption is that all the services in the composition can be provided by the same provider. This assumption is not unrealistic in cloud environments which ofer Infrastructure as a Service (IaaS), with limited variety in the ofered/requested resources, and is useful to limit the complexity of the service selection problem. However, in a Software as a Service (SaaS) cloud environment, it is unlikely that all required services are ofered by the same provider. For example, a complex CS requester might need to find diferent providers for data cleaning and fusion services, machine learning services, and secure data transfer and encryption services. Moreover, the requester may be reluctant to procure all the services from the same provider.

The research papers discussed above tend not to consider the possibility of bundling web services. Even when a provider ofers multiple services, the ofers are considered to be independent of one another. Such an approach does not consider the dependencies between the web services attending a composition. These web services are dependent on each other based on factors such as chronological sequence, execution time, and data [42], or constraints such as technical [43,44] and business constraints [45].

These inter-service dependencies are the drivers for service provi ders to ofer their web services in bundles. For example, bundling can help the service provider internalize some of the costs related to interface compatibility required for data exchange between the ofered web services. This can lead to reduced cost of provisioning the services, and enables the service provider to ofer discounts over bundled ser vices, similar to the Microsoft sale promotions when two or more services are included in the same plan [46]. Bundling may also allow service providers to improve the quality of bundled services along with competitive prices [10]. For instance, when bundled services are executed on the same machine, the provider can guarantee a lower execution time for the bundle of ofered services.

A useful approach to address the inter-service dependencies is to model composite service selection based on combinatorial auctions which allows services to be ofered in bundles. Depending on the auction being direct or reverse, the service requester or the providers bid to buy or sell the bundled web services. A direct auction model is proposed in [47] which is discussed in Section 3.3 as it considers multiple simultaneous CS requests. In the CSS approaches based on procurement combinatorial auctions [10,44,48–50], the service requester asks the service providers to bid for provisioning one or more of the required services. In both approaches, the set of winning bids, i.e. the concrete web service for each task, is determined based on the defined objective for the auction, e.g. minimize the cost [44] or maximize the quality [10] for the service requester.

## 3.3. Service selection for multiple CS requests

The research on service selection for multiple CS requests is relatively sparse. Papazoglou [51] was one of the first to discuss multiple simultaneous CS requests in the context of web service marketplaces. The purpose of these markets is to create the opportunity for service requesters and providers to meet and conduct business. Tang [52] investigated the providers' optimal strategies for ofering functionally complementary web services in the presence of multiple CS requests. However, no specific model was proposed for the service selection.

Lamparter [47] studied automated contracting in a web service market through semantic technologies. A service selection mechanism is also proposed based on combinatorial direct auctions in which service providers ofer their web services in bundles and CS requesters bid for these bundles. However, the service requester can only have “one” winning bid, which means that the bid should include all the services required for the composition. This leads to similar limitations as the double auction models which assume that all the services should be provided by the same provider, as discussed in Section 3.2. Moreover, the model solves CSS for “all" the requests simultaneously. This means that with even one unsuccessful/infeasible request, the “whole” auction fails. Thus, the proposed model is likely to have a low success rate. As no evaluation was performed, it is dificult to estimate the performance of the proposed model, including its success rate.

Javed et al. [16] proposed a mechanism for dynamic pricing and service selection of cloud services, through a platform where cloud providers ofer their unused resources. For each service provider, a direct auction is set up and consumers bid to acquire the auctioned resource. As a result, a consumer may need to attend multiple auctions to acquire a required resource. For a composite service requester, this process might even take longer. Moreover, the CS requester might end up acquiring only some of the required services; i.e. there is no guarantee for the simultaneous allocation of the required services for a CS.

Hwang and Lee [53] investigated service selection for multiple composite services in a choreography-based model where multiple CSs execute and interact in a distributed set-up. In this decentralized service selection mechanism, each web service autonomously searches for the right operation in the right web service that maximizes the possibility of completing the entire choreography (a choreography consists of the set of interacting composite services). The mechanism only supports service selection for interactive composite services, no discussion is provided on how to define the end-to-end quality requirements, neither is service bundling considered. In contrast, our approach follows the orchestration model [54] in which a central mechanism is in charge of service selection with no assumptions about the composite services' runtime interactions.

A closely related problem is studied in [55], in the context of service provider organizations who expose their services in the form of web service workflows for consumption by their peer organizations. Both service providers and consumers require the use of Service Level Agreements (SLAs) to ensure of the quality of the services. For a provider organization with existing operational workflows, the challenge is to predict the impact of adding a new web service workflow on the SLAs of existing workflows. It proposed a model to aggregate the SLA terms of the underlying services which can be performed before service se lection to prevent the entry of new services that invalidate existing SLAs.

Table 1  
A summary of service selection mechanisms and the main gaps in the literature.

<table><tr><td>Level of service selection</td><td>Study</td><td>Main gap</td></tr><tr><td>Single service selection</td><td>[27-30]</td><td>Does not address service selection for a composition; end-to-end QoS constraints not supported.</td></tr><tr><td rowspan="2">Composite service selection (CSS)</td><td>[8,31-39]</td><td>No possibility for bundling of service offers; the presence of multiple simultaneous CS requests not addressed.</td></tr><tr><td>[10,44,48-50]</td><td>The presence of multiple simultaneous CS requests not addressed.</td></tr><tr><td rowspan="6">Service selection for multiple CS requests</td><td>[51,56]</td><td>A conceptual model; no actual mechanism for service selection.</td></tr><tr><td>[52]</td><td>Game theoretic study of providers&#x27; strategies; no actual mechanism for service selection.</td></tr><tr><td>[47]</td><td>Possibly low success rate; no performance evaluation.</td></tr><tr><td>[53]</td><td>No support for service selection of multiple, independent CS requests; service bundling not supported; end-to-end QoS constraints not supported.</td></tr><tr><td>[16]</td><td>No direct support for composite service requests. As a result, no guarantee for simultaneous allocation of resources to all the tasks in a composition.</td></tr><tr><td>[55]</td><td>A pre-processing step before multiple CSS; not a service selection mechanism.</td></tr></table>

The simultaneous auction model presented in this paper difers from other research in service selection for multiple CSs in two ways. First, it supports modeling the inter-service dependencies by allowing service providers to ofer their services in bundles. Second, it improves the service allocation for both service requesters and providers by considering all the requests at the same time and adopting a long-term horizon for service selection. A summary of the relevant literature and the gaps identified is presented in Table 1.

## 4. A simultaneous combinatorial auction mechanism

## 4.1. Web service market setting

A service selection mechanism based on procurement combinatorial auctions is performed in a setting where multiple CS requesters and web service providers are seeking trade partners, such as in a market for cloud services or IoT applications. The market is created and maintained by an independent entity (e.g. a consortium of organizations), called the market maker who is responsible for market administration, maintenance, and management of the activities required for the market to stay open for business [51]. Some of the activities include creating and maintaining the task directory and execution of the service selection mechanism.

The task directory describes the functionalities of the web services exchanged in the market. Service providers register the functionality of their web services and service requesters consult the directory to check whether the services they require are ofered in this market.

Service requesters enter the market and register the required composite (or single) services, i.e. the requests. We have assumed that a request is defined at a high level as an abstract business process (BP). The specification of each request includes all the tasks in the BP, the sequence of the tasks, and the local (for individual services) and the end-to-end (for the CS) QoS constraints, such as the execution time or the budget constraints of the CS. For simplicity, we assume that the BP only includes sequential structures. The existence of other structures (parallel, loop and conditional) only afects our model in terms of the aggregation functions for the quality attributes. The problem of mapping the BP's complex structure to a sequential execution path has already been resolved in the literature [32–34]. Service providers also register their ofered services in the market, i.e., the bids or ofers. They can register single services as well as bundles. Similar to the requests, the ofers are multi-dimensional, including information about the quality and the price of the ofered services. If the ofer includes a bundle, the QoS profile of each service is presented separately while the price is specified for the bundle.

When new providers or requesters enter the market, they need to consult the directory to decide whether to attend that market. For example, if a service requester finds no commonality between the services in the task directory and the tasks in their BP, they might not find it useful to attend that market. However, requesters can register new tasks in the directory. Many requests for specific new tasks act as signals to the service providers of the market's need for new services.

The ofers and requests are submitted to the service selection me chanism which performs the matching at specific intervals, e.g. based on time limits and/or the number of active participants in the market. After each matching round, the successful providers and requesters are notified and charged a fee based on the business model, e.g. based on the number of transactions, or the price of the composite service. The results are also announced to all the participants to improve their future decision making. The market maker can use the procurement combinatorial auction model as the basis for the matching. As the matching mechanism considers multiple composite service requests at the same time, we refer to it as the “simultaneous auction”. The relationship of the market maker, service requesters and providers is illustrated in Fig. 1.

The simultaneous auction mechanism matches the offers and requests based on the defined objective function. Currently, two alternative objectives of procurement auctions for web services have been considered in the literature: (1) maximizing the overall utility for the service requester in terms of quality and price of the composite service as in [10], and (2) minimizing the cost of service procurement subject to quality constraints as in [47]. The market maker decides what objective to implement based on the requirements of that market's participants. If the requesters have a clear understanding of the trade-of between diferent quality attributes and it is important for them to maximize the achieved quality, maximizing the utility can attract more participants to the market. In other cases, the objective to minimize the cost may engage more requesters as it requires less complex specification of the service request (e.g. there is no need to define weights for the quality attributes). Moreover, in a market with this objective, it is still possible to define tight quality constraints to achieve the desired level of quality. The formulation presented below deals with the cost-minimizing objective function where we have mapped the proposed auction-based mechanism to an ILP optimization problem.

## 4.2. Specification of ofers and requests

Let T denote the set of all the tasks registered in the task directory, and M is the total number of tasks. Let B denote the set of all received ofers (bids) from all web service providers, and N is the total number of all received bids. Each bid b ∈ B is defined as $\boldsymbol { b } = ( T _ { b } , Q _ { b } , c _ { b } )$ , where $( \mathrm { T } _ { \mathrm { i } } \subseteq \mathrm { T a s k } )$ is the set of tasks that this bid is ofering web services to execute, $Q _ { b }$ is the set of QoS profiles of the relevant web services and $c _ { b }$ is the provider's requested price to execute the services. While $c _ { b }$ is the price requested for the whole bundle, $Q _ { b }$ is a set including the QoS profiles of all the services ofered in $^ { b , }$ that is, $Q _ { b } = \{ P _ { b t } \mid t \in T _ { b } \}$ where $P _ { b t }$ is the QoS profile of one service. Let L denote the set of quality of service attributes in a QoS profile of a typical service in this market. Then, $P _ { b t }$ is defined as $P _ { b t } = \{ q _ { l b t } | l \in L \}$ } where $q _ { l b t }$ is the ofered value for the quality attribute l of the service in $^ { b , }$ executing t.

![](/api/attachments/QZHEPN4W/fulltext/images/55619aa38703b5c0a44535dcb4a6bda5d1e9eaefd207c82d9b77f8ff02db83da.jpg)  
Fig. 1. Relationship of market maker, service requesters, and web service providers

As an example, consider the bid b illustrated in Fig. 2. This bid includes services for three tasks. The QoS profile includes two quality attributes, $L = \{ \nu , x \}$ , where v represents the availability and x represents the response time. The price requested for this bundle is \$5. The three tasks are indexed in the directory as $t _ { 1 } , t _ { 2 }$ and $t _ { 1 0 } .$ Then we have:

$$
\begin{array}{l} b = (T _ {b} = \{t _ {1}, t _ {2}, t _ {1 0} \}, Q _ {b} = \{P _ {b t _ {1}}, P _ {b t _ {2}}, P _ {b t _ {1 0}} \}, c _ {b} = 5), P _ {b t _ {1}} \\ \qquad = \{q _ {x b t _ {1}} \leq 2 \text {m sec}, q _ {v b t _ {1}} \geq 99 \% \}, \\ P _ {b t _ {2}} = \{q _ {x b t _ {2}} \leq 1 0 \text {m sec}, q _ {v b t _ {2}} \geq 95 \% \}, P _ {b t _ {1 0}} = \{q _ {x b t _ {1 0}} \leq 1 0 m s e c, q _ {v b t _ {1 0}} \\ \qquad \geq 99 \% \}. \end{array}
$$

Let R be the set of all received requests for composite services from service requesters, and W is the total number of all received requests. Each request r ∈ R is defined as $\boldsymbol { r } = ( T _ { r } , P _ { r } , B _ { r } )$ , where T ⊆ T is the set of tasks requested in $r , P _ { r }$ is the QoS profile required for the end-to-end quality of the requested composite service, and B is the budget con straint to procure services for r. The QoS profile P is a tuple including the quality attributes' values requested for $r ,$ that is, $P _ { r } = \{ \ q _ { t r } \ | \ l \in L \}$ , where $q _ { l r }$ is the minimum or maximum (depending on the type of quality attribute) acceptable value for the end-to-end quality attribute l of the CS request r.

As an example, consider the composite service request r as illu strated in Fig. 3. This request needs services to execute five tasks. The end-to-end QoS requirements of this request specify that the service availability should be over 90% and the response time should not ex ceed 25 msec. The budget available to procure all the required web services is \$15. The required tasks are indexed based on the task directory to be $t _ { 1 } , \quad t _ { 2 } , \quad t _ { 8 } , \quad t _ { 9 }$ and $t _ { 1 0 } .$ Then we have: $r = ( T _ { r } = \{ t _ { 1 } , t _ { 2 } , t _ { 8 } , t _ { 9 } , t _ { 1 0 } \} , P _ { r } = \{ q _ { x r } \leq 2 5 ~ m s e c , q _ { v r } \geq 9 0 ^ { 9 } 0 \} , B _ { r } = \mathfrak { F } 1 5 )$

## 4.3. Matching algorithm

The matching algorithm specifies which bidders have won and how the items are allocated to them. The auction designer needs to consider two main components: the auction objective and the set of allocation constraints. We define the objective function to be minimizing the cost of procuring CSs for the requesters. The allocation constraints are defined based on the QoS requirements of the CSs. Service requesters can also incorporate any other preferences about the provisioning of the CS by defining appropriate allocation constraints, such as the ones proposed in [10,44]. We have developed two matching algorithms as follows:

![](/api/attachments/QZHEPN4W/fulltext/images/414bd7a2596372a687726ddf3a09d177ec70671f20c302e80b4a37d7bcd7f399.jpg)  
Fig. 2. Example of a bid, ofering a bundle of services.

![](/api/attachments/QZHEPN4W/fulltext/images/12f2581467778345bab53327d0de61cfe0cbe1e9269fa31fc31b0fd9452ca6ad.jpg)  
Fig. 3. Example of a request for a composite service.

## 4.3.1. Full matching of requests and ofers

The full-matching mechanism targets all the CS requests and tries to find their best matching ofers. The objective is to minimize the cost for all requests collectively, defined in function (1). The decision variable is denoted by ${ z _ { b r } } \left( b \in B , r \in R \right)$ to be 1 if ofer b is selected for request r and 0 otherwise. Constraint (2) ensures that for each task in each request, there is exactly one winning bid. In this constraint, $a _ { b t }$ is an arbitrary member of the matrix $A _ { N \times M } ,$ that specifies the mapping of the bids to the tasks in the market; i.e. $a _ { b t }$ is 1 if $T _ { b }$ includes task t and 0 otherwise. The budget constraint is specified in constraint (3).

The constraints over other quality attributes are presented in (4) and (5), depending on the type of quality attribute. We define a quality attribute to be a “positive” attribute if higher values are more desirable for it, such as availability and reputation. Similarly, a “negative” quality attribute is one for which lower values are more desirable, such as response time and recovery from failure time. Constraint (4) ensures the minimum desirable values for positive quality attributes, and constraint (5) sets maximum acceptable values for negative quality attributes. In these constraints, each quality attribute l has a specific aggregation function, G<sup>l</sup>. The function $G ^ { l }$ takes the quality attribute values of the services in a CS and calculates the end-to-end value of that quality attribute. The aggregation functions can be similar to the ones presented in the literature, such as in [44].

<table><tr><td>Minimize</td><td></td><td> $\sum_{r\in R}\sum_{b\in B}c_b*z_br$ </td><td>(1)</td></tr><tr><td colspan="4">Subject to:</td></tr><tr><td>Full allocation constraint</td><td> $\forall r\in R,\forall t\in T_r$ </td><td> $\sum_{b\in B}a_{bt}*z_br=1$ </td><td>(2)</td></tr><tr><td>Budget constraint</td><td> $\forall r\in R$ </td><td> $\sum_{b\in B}c_b*z_br\leq Br$ </td><td>(3)</td></tr><tr><td rowspan="2">Quality constraints</td><td> $\forall r\in R, \forall l$  which is a positive quality attribute</td><td> $G^{l}_{t\in Tr}(\sum_{b\in B}q_{lb t}*a_{bt}*z_br)\geq q_{lr}$ </td><td>(4)</td></tr><tr><td> $\forall r\in R, \forall l$  which is a negative quality attribute</td><td> $G^{l}_{t\in Tr}(\sum_{b\in B}q_{lb t}*a_{bt}*z_br)\leq q_{lr}$ </td><td>(5)</td></tr></table>

## 4.3.2. Partial matching of requests and ofers

The main limitation of the full-matching is that even if a single request is not feasible due to budget or quality constraints, the whole auction fails. To address this limitation, we propose the partialmatching mechanism, which relaxes the requirement to find providers for all the requests. The partial-matching mechanism aims to find the optimal set of providers for as many requests as possible.

We define a new objective function, Eq. (6), to minimize the cost for all the requests, and maximize the number of “feasible” requests, i.e. requests that get all their required web services. Feasibility is indicated by the decision variable, $y _ { r }$ which is equal to 1 if r is feasible and 0 otherwise. To construct one linear objective function from the two parts, the Big-M method is used [57, p.54].

The relaxation of the allocation constraint (2) is achieved by de fining a set of constraints, (7) to (9), and a decision variable, $x _ { t r }$ , which is equal to 1 if task t in request r is feasible and 0 otherwise. A request's task is called “feasible” if a bid is selected to provision it. Constraints (7) to (9) state the relationship of a feasible request, a feasible request's task and a winning bid. They enforce: (a) if a request r does not contain a task $t ,$ then $x _ { t r }$ is zero, (b) if a request is feasible, then “all” of its task are feasible, (c) if a request is not feasible, “none” of its tasks are feasible, (d) no bids should be assigned to an infeasible request, and (e) there is one winning bid that contains a feasible task. Constraints (10), (11) and (12) present the budget constraint and the quality requirements for positive and negative quality attributes for the feasible requests. A provider's resource limitation is presented in constraint (13), where we simply assume that each service can be assigned to one request. If a provider is willing to ofer a bid more than once, we need to either replicate the bid, or define diferent resource limitation constraints for diferent providers. The notations are summarized Table 2.

Notation used for the formulation of full-matching and partial-matching mechanisms.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>T</td><td>set of all tasks registered in the market&#x27;s task directory</td></tr><tr><td>M</td><td>total number of tasks in the market</td></tr><tr><td>t</td><td>an element of the set T</td></tr><tr><td>L</td><td>set of quality attributes in a QoS profile</td></tr><tr><td>l</td><td>an element of the set L</td></tr><tr><td>B</td><td>set of all received offers (bids)</td></tr><tr><td>N</td><td>total number of all received bids</td></tr><tr><td>b</td><td>an element of the set B</td></tr><tr><td> $T_b$ </td><td>set of tasks that b offers web services to execute ( $T_b \subseteq T$ )</td></tr><tr><td> $c_b$ </td><td>cost of providing service(s) for the task(s) in  $T_b$ </td></tr><tr><td> $Q_b$ </td><td>set of the offered QoS profiles for the services executing  $T_b$ </td></tr><tr><td> $P_{bt}$ </td><td>QoS profile of the service executing task t in b  $b_i = (T_i, c_i, Q_i)$ </td></tr><tr><td> $q_{lbt}$ </td><td>value of l-th quality attribute function offered for task t in bid b</td></tr><tr><td>R</td><td>set of all received requests from service requesters</td></tr><tr><td>W</td><td>total number of all received requests</td></tr><tr><td>r</td><td>an element of the set R</td></tr><tr><td> $T_r$ </td><td>set of tasks requested in r ( $T_r \subseteq T$ )</td></tr><tr><td> $B_r$ </td><td>budget constraint to procure  $T_r$ </td></tr><tr><td> $P_r$ </td><td>QoS profile requested for the end-to-end quality of request r</td></tr><tr><td> $q_{lr}$ </td><td>value of the l-th quality attribute, requested for r</td></tr><tr><td> $z_{br}$ </td><td>decision variable to be 1 if offer b is selected for request r</td></tr><tr><td> $A_{N \times M}$ </td><td>matrix mapping the bids to the tasks in the market</td></tr><tr><td> $a_{bt}$ </td><td>an element of the matrix  $A_{N \times M}$ </td></tr><tr><td>BigM</td><td>a sufficiently large number</td></tr><tr><td> $y_r$ </td><td>decision variable to be 1 if the request r is feasible, 0 otherwise</td></tr><tr><td> $x_{tr}$ </td><td>decision variable to be 1 if t in r finds a provider, 0 otherwise</td></tr><tr><td> $G^l$ </td><td>the aggregation function of quality attribute l</td></tr></table>

$$
\text { Minimize }
$$

$$
\sum_ {r \in R} \sum_ {b \in B} c _ {b} * z _ {b r} - B i g M * \sum_ {r \in R} y _ {r}\tag{6}
$$

$$
\forall r \in R, \forall t \in T _ {r}
$$

$$
x _ {t r} = y _ {r}\tag{7}
$$

$$
\forall r \in R, \forall b \in B
$$

$$
z _ {b r} \leq y _ {r}\tag{8}
$$

$$
\forall r \in R, \forall t \in T _ {r}
$$

$$
\sum_ {b \in B} a _ {b t} * z _ {b r} = x _ {t r}\tag{9}
$$

$$
\forall r \in R,
$$

$$
B _ {r} - \sum_ {b \in B} c _ {b} * z _ {b r} \geq y _ {r} - 1\tag{10}
$$

$$
\forall r \in R,\tag{11}
$$

l: a positive quality attribute ∀r ∈ R,

$$
G _ {t \in T r} ^ {l} (\sum_ {b \in B} q _ {l b t} * a _ {b t} * z _ {b r}) \geq q _ {l r} * y _ {r}\tag{12}
$$

$$
\forall b \in B
$$

$$
G _ {t \in T r} ^ {l} (\sum_ {b \in B} q _ {l b t} * a _ {b t} * z _ {b r}) \leq q _ {l r} * y _ {r}
$$

$$
\sum_ {r \in R} z _ {b r} \leq 1\tag{13}
$$

## 5. Evaluation process

This section presents the data generation model, the developed baselines, and the experimental setup.

## 5.1. Data

The current trend in evaluation of CSS approaches is to generate CS requests with a fixed of number of tasks [9,10]. For the web service ofers, the quality of service attributes are either generated randomly [46,58] or based on existing public data sets of web services QoS pro files such as WS-Dream [59] and QWS [60]. Although these data sets ofer a variety of QoS attributes, they do not provide information on actual pricing or bundling practices if any.

To address this problem, we studied a number of web service communities on the Internet to understand the settings in which service requesters need composite services, including biodiversity research, GIS-related web services, life science, astronomy and eLearning web services. We found that these communities vary significantly in size depending on the maturity level of the community. The services ofered in these communities can be composed together to create CSs ranging from simple (less than five services in the composition) to complex (including over 20 single services).

Based on these observations, we conducted our experiment in fou settings, as depicted in Table 3. These settings are called market sectors and are designed based on two factors: (i) the complexity of the CS requests, borrowed from [61], and (ii) the size of the economy, adopted from [52]. The complexity includes two categories of CSs: small and large. Small CSs are composed of 3 to 5 tasks, while large CSs include 15 to 20 tasks. The size of the economy indicates the number of participants (service providers and requesters) and is categorized as: small economy, including 50 or 100 service ofers, and 4 or 12 CS requests; and large economy, including 300 or 500 service ofers, and 20 or 28 CS requests.

Initially, a fixed number of tasks are generated which represents the tasks in the task directory. A fixed number of providers are also generated, and bids are randomly assigned to them. Bid generation involves deciding the number of the services in the bid, the services to include, and the bundle price. A well-known distribution from the combinatorial auction experiments is applied to choose the number and the items in a bid, known as the decay distribution [62]. As per this distribution, a bid starts with one random item. Subsequently, a new random item is repeatedly added to the bid with probability α until a new item is not added to the bid or the bid size reaches the maximum number of auctioned items. Changing the distribution of the combinatorial bids should not afect the behavior of the auction model in finding the optimal allocation. However, diferent distributions, as listed in [63], generate diferent combinatorial instances in terms of the dificulty to be solved. The decay distribution is known to generate some of the hardest instances of combinatorial bids [64]. We experimented with a variety of values for ${ \mathfrak { a } } ,$ and fixed it at 75% to generate the diferent bid sizes [44].

Table 3  
The four market sectors in the experiments.

<table><tr><td>CS complexity</td><td>Simple# tasks in a CSrequest: [3-5]</td><td>Complex#tasks in a CS requests:[15-20]</td></tr><tr><td>Economy size</td><td></td><td></td></tr><tr><td>Small</td><td>Small-Simple</td><td>Small-Complex</td></tr><tr><td>#offers: 50,100, #CSrequests: 4,12</td><td></td><td></td></tr><tr><td>Large</td><td>Large-Simple</td><td>Large-Complex</td></tr><tr><td>#offers: 300,500, #CSrequests: 20,28</td><td></td><td></td></tr></table>

Table 4  
Experiment setup.

<table><tr><td>Parameter</td><td>Values of the parameter</td></tr><tr><td>Tasks_Number (in the directory)</td><td>[25,50]</td></tr><tr><td>Providers_Number</td><td>[5,50]</td></tr><tr><td>Offers_Number (Bids_Number)</td><td>[50,100, 300, 500]</td></tr><tr><td>Requests_Number</td><td>[4,12,20,28]</td></tr><tr><td>α in the market</td><td>75%</td></tr><tr><td>Max_Discount</td><td>25%</td></tr><tr><td>Requests_Size</td><td>Small request: [3-5]Large request: [15,16,...,20]</td></tr></table>

The prices of web services are generated randomly between 1 and 100, following the assumption of providers with an Independent Private Valuation (IPV) model [26], which is similar to other research in composite service selection [10]. The price requested for a bundle is calculated as the sum of the provider's prices for the bundled services, minus the provider's discount (a random number between 0 and 25%).

The number of tasks in a request is a random number from 3 to 5 for simple requests, and from 15 to 20 for complex requests, which are randomly chosen from the task directory. The requester's budget is the sum of the requester's valuations for the tasks in the request, where the value of each task is a random number between 1 and 100, following the IPV model. The experiment setup is summarized in Table 4. There are 128 problem sets to be evaluated. For each problem set, 30 instances are generated. More details on data generation are presented in [65,p.152].

## 5.2. Baseline

The proposed simultaneous mechanism solves the CSS by considering all the existing requests at the same time. We compare this mechanism with two other mechanisms which solve the CSS for multiple requests, one at a time: (1) the single auction mechanism [44], and (2) the fixed-price mechanism [66].

The single (combinatorial) auction mechanism is proposed and evaluated in [44]. It performs CSS for a single CS request, similar to other existing proposals. To extend its functionality to a setting with multiple requests, it performs CSS one by one for the CS requests based on the first come (in the market), first served policy. For each request, the auction aims to find the lowest procurement cost while satisfying all other allocation constraints. If the auction is successful, the winning bids are removed from the pool of ofers and the auction starts over for the next request with the remaining available ofers.

We are also interested in understanding the impact of dynamic pricing of the auction mechanism on service selection outcomes. Therefore, we designed a second baseline with fixed pricing, which is the accepted baseline for comparison with the dynamic pricing of auctions in the literature [66].

In a fixed price mechanism, the trader sets a predefined price, and the trade occurs with the first business partner who agrees to the predetermined price. Fixed pricing can be implemented either by the buyer or the seller, depending on who is setting up the trade. In a procurement setting, the buyer ofers to buy a product or service at a fixed price, and the seller can take the ofer or leave it. In our context, the fixed-price baseline is defined as: the service requester (buyer) sets a fixed price (budget) for the CS. The fixed-price mechanism selects the first set of service ofers for which the total price is below the specified budget, and satisfies all the other allocation constraints. After finding such a set, the allocated services are removed from the pool of available ofers, and the mechanism continues the search for the next request. The requests and ofers are considered based on the first-come, first-served policy.

## 5.3. Experimental setup

The objective of the evaluation is to compare the performance of the simultaneous auction with the two baseline mechanisms. The evaluation is performed on the partial-matching simultaneous combinatorial procurement auction mechanism, referred to hereafter as “the simultaneous auction”.

The performance metrics are measured at the end of each simulation round. A simulation round starts with a fixed number of requests and ofers. The simultaneous auction performs CSS simultaneously for all the requests. The baseline mechanisms perform the matching of the requests one at a time.

In our experiments, we relaxed the constraint of exactly one winning service for each task in a request, i.e. constraint (9). The relaxation allows each task to have “at least” one winning bid, rather than “exactly” one. We argue that as the objective function is set to minimize the cost, there is no problem if more than one service is selected for a task (for example two bundles with a common service win the auction) if such an allocation leads to a less expensive provisioning of the CS. The requester needs to decide which of the winners will ultimately execute the task, either randomly or based on some criteria, such as choosing the one that is already providing more (or fewer) services for other tasks in the composition.

All three mechanisms are implemented in AMPL [67], and solved by IBM ILOG CPLEX 12.6, using a server computer with 64 AMD Opteron processors, each 1400 MHz and 132 GB memory. In the simultaneou auction model, a 60-second time limit is set for the solver (CPLEX), due to the complexity of the mechanism. To maintain consistency, a similar time-out is set for the other two mechanisms.

## 6. Results

This section presents the experiment's results, focusing on comparison with exiting optimization approaches in terms of the success rate in allocating web services to CS requests, the procurement cost of the CSs, and the time taken to find the optimal allocation.

## 6.1. Success rate

Success rate (SR) is defined as the ratio of the successful composite service requests (in procuring web services) to the total number of requests. This is similar to the success rate defined in the literature [53]. Following the notations presented in Table $\begin{array} { r } { { 2 } , S R = \sum _ { r \in R } y _ { r } / W } \end{array}$

The SRs of the three mechanisms are plotted for the four market sectors in Fig. 4.<sup>3</sup> The results show that, among the three mechanisms, the simultaneous auction achieves the highest SR in all four market sectors. This could be the result of its longer-term horizon of the simultaneous auction versus the shorter horizon of the other two mechanisms. In a short-term allocation horizon, requests that arrive later and have tighter budget constraints might not find the required set of services in the remaining pool of web services' ofers. In the long-term horizon, the simultaneous mechanism considers all requests and their needs simultaneously. Therefore, it has the possibility to match the requests and ofers more efectively and increase the number of successful requests. The results also show that the SRs of the single auction and the fixed-price mechanisms are not significantly diferent which is likely to be due to their similar short-term allocation horizon.

Fig. 4 also shows that the diference between the SR of the simultaneous auction and that of the two other mechanisms is most substantial in the large-complex market sector (simultaneous auction's SR is 16% higher than the two other mechanisms). This trend is followed by the large-simple sector (SR 15% higher), the small-complex sector (SR 10% higher), and the small-simple sector (SR 3% higher). This trend suggests that the simultaneous auction's lead in achieving a better SR is more notable in more complicated settings. In simpler settings, the long-term and short-term horizons might not lead to very diferent outcomes.

Studying each mechanism's SR in the four market sectors shows that all three achieve a higher SR with complex requests compared to simple ones, in both economy sizes. This might be because we used a fixed number of tasks (registered in the directory) to generate both simple and complex requests. As a result, it is likely that the smaller CS requests have less overlap with the ofered services compared to the larger ones.

To verify this proposition, we plotted the SR of the simultaneous auction separately for the number of tasks at 25 and 50, in Fig. 5. This shows that with 25 tasks in the market, the SR is higher than with 50 tasks, which supports the speculation that a lower number of tasks in the directory leads to more overlap among service ofers and requests, and consequently, a higher SR. This is consistent with the general understanding that participants are more likely to find a match if they attend a narrower limited domain market, rather than a more general purpose market with many tasks.

We also studied the infeasible problem instances in which service could not be allocated to the requests within the specified budget; i.e. SR = 0. As depicted in Table 5, the findings are: (1) none of the instances with 300 or 500 bids were infeasible, (2) 94% of the instances had 50 tasks in the market directory, and (3) in all cases, the problem instance remained infeasible regardless of the applied service selection mechanism. We conclude that the high variety in the number of items (tasks) in the market (50 versus 25 tasks) leads to less overlap between ofered (bundled) services and requests, which in turn, makes service composition more expensive than the budget when the number of bids is small (50 or 100 bids).

## 6.2. Statistical analysis of SR

To estimate the statistical significance of the results, the Kruskal Wallis test [68] is performed on the success rate of the three mechanisms as the SRs' residuals did not follow a normal distribution. Also known as the “one-way ANOVA on ranks”, the Kruskal-Wallis test is the nonparametric alternative to the one-way ANOVA. Unlike ANOVA, it does not assume a normal distribution of the residuals of the dependent variable. The Conover-Iman method [69] is used as the post-hoc analysis. This method is a common procedure used with the Kruskal-Wallis test and is a distribution-free rank transformation method that replaces data by its rank.

Firstly, we consider only one independent variable, the type of service selection mechanism with three values: the simultaneous auction. the single auction and the fixed-price. The Kruskal-Wallis test shows that the SRs of at least two mechanisms are significantly dif ferent, K (df = 2) =153.730, p < 0.001. The Conover-Iman procedure reveals that the SR of the simultaneous auction is significantly diferent from the SR of the other two mechanisms, and the SR of the single auction and fixed-price do not difer significantly.

We also estimate the statistical significance of the impact of the economy size and the request complexity at the same time as the impact of the service selection mechanism on the SR, that is, we consider three independent variables simultaneously. To do so, we defined a dummy independent variable that represents the combination of the three actual independent variables forming 12 groups.

![](/api/attachments/QZHEPN4W/fulltext/images/b7bf891c9621bd0a7cb285e415224d6f79ddc9195a3175022d5725cbbf2a4915.jpg)  
Fig. 4. SR achieved by the three mechanisms in the four market sectors.

![](/api/attachments/QZHEPN4W/fulltext/images/1aa55f21a95c6a9868dc8002b35954e2892814641f32511fbebdae1a9be247f7.jpg)

![](/api/attachments/QZHEPN4W/fulltext/images/573055e9616ab78b6065539de2cd6712430c875153e460023eda6561a499d086.jpg)  
Fig. 5. Impact of the number of tasks registered in the market's task directory on the SR of the simultaneous auction, for (a) simple and (b) complex requests

Number of infeasible instances based on the number of bids and the number of tasks in the directory.

<table><tr><td>#bids</td><td>50</td><td>100</td><td>Total</td></tr><tr><td>#tasks</td><td></td><td></td><td></td></tr><tr><td>25</td><td>66</td><td>12</td><td>78</td></tr><tr><td>50</td><td>1026</td><td>162</td><td>1188 (94%)</td></tr><tr><td>Total</td><td>1092</td><td>174</td><td> $1266^a$ </td></tr></table>

<sup>⁎</sup> Simultaneous auction: 422 instances, single auction: 422 instances, fixed price: 422 instances.

The Kruskal-Wallis test shows that the SR of at least two groups is statistically diferent, $\begin{array} { r l } { \mathrm { K } _ { \mathrm { o b s e r v e d } } } & { ( \mathrm { d f } = 1 1 ) } \end{array} = 3 0 3 4 . 5 6 2 , \ p \ < \ 0 . 0 0 1 .$ Performing the Conover-Iman procedure shows that the SR of the simultaneous auction is statistically significantly diferent to that of the single auction and the fixed-price mechanisms in all market sectors, except for the (small-simple) sector. This means that with small market and simple CS requests, the choice of the service selection mechanism does not significantly afect the success rate. Moreover, the SRs of the fixed-price and the single auction mechanisms are not statistically different in any of the market sectors.

## 6.3. Cost per composite service

Another interesting aspect to study is the cost of procuring web services for the CS requests. This is similar to the evaluation of the execution price (in dollars) performed in [32]. Two units of measurement are defined:

• Cost per composite service (CPC): the average cost of procuring a single composite service (mechanism's total procurement cost di vided by the number of feasible requests),

![](/api/attachments/QZHEPN4W/fulltext/images/ee23813f63da9707bd6d00796ff14182471ce824da1474af17b543984d2ade27.jpg)  
Fig. 6. CPC achieved by the three mechanisms in the four market sectors.

Cost per task (CPT): the average cost of procuring a task (CPC di vided by the average number of tasks in a request, depending on the request's complexity).

Following the notations presented in Table 2, CPC and CPT are defined as:

$$
C P C = \frac {\sum_ {r \in R} \sum_ {b \in B} c _ {b} * z _ {b r}}{\sum_ {r \in R} y _ {r}} \quad C P T = \frac {C P C}{\sum_ {r \in R} | T _ {r} | / W}
$$

We removed the instances whose SR is equal to zero from the cost analysis since it suggests that the mechanism failed to assign any service to any of the requests, and the CPC would be zero. Including the zero cost values would lead to inaccurate final average cost computation.

The CPC of each mechanism is depicted in Fig. 6 based on the market sectors. The results show that firstly, the cost of procuring a composite service is much higher if the requester attends the fixed-price mechanism, compared to the single auction or the simultaneous mechanisms. This confirms our expectations from dynamic pricing in auctions: the price discovery of auction mechanisms can lead to considerably lower prices compared to the requesters' predetermined prices (budgets).

Secondly, the CPC of the simultaneous mechanism is not significantly diferent from that of the single auction. This may not seem intuitive as the single auction aims to find the best providers for each request regardless of the other existing requests, whereas the simultaneous auction aims to find the best providers for the collective set of requests. The very close CPC of these two mechanisms is likely to be the result of averaging the cost across all successful requests in a simulation round regardless of their order of arrival in the market. While in the simultaneous auction, the arrival order should not afect the procurement cost, it is likely to afect the cost in the single auction. In each simulation round, the single auction might be able to find very good deals for the early requests. However, with more service ofers being matched with the requests, the remaining available services would be the more expensive ones, leading to higher costs for the late arriving requests.

To investigate this proposition, the impact of a request's order of arrival in the market on its procurement cost is studied next. For the two auction mechanisms, the cost of the first and the last successful CSs are measured separately in each simulation round and then averaged across all simulation rounds. The results are presented in Fig. 7, for (a) simple and (b) complex requests. The results indicate that the first request attending the single auction mechanism has the lowest procurement cost, and the last request attending this auction has the highest cost. However, the first and the last requests that attended the simultaneous mechanism are procured at very close costs. The costs achieved by the simultaneous auction are positioned between the lowest and highest costs obtained by the single auction mechanism. These results apply to both simple and complex requests.

Moreover, the cost of procuring the first request through the single auction mechanism does not change substantially by having more requests, while the cost of the last request dramatically increases with more requests. This can be explained based on the single auction strategy which aims to find the best deal for each request, where the first request benefits from having the most ofers available, while the last request is afected by the number of requests that need to be served before it

To summarize, although the single auction and the simultaneous auction achieve close outcomes in terms of the average cost for the requests, the simultaneous auction attains more “homogenous” costs for the requests compared to the single auction. The single auction finds the best deals for the requests that are first to arrive, while the last requests will be procured at a higher cost compared to the requests that have already been served. The impact of order of arrival on the procurement cost can significantly afect service requesters' decisions regarding which service selection mechanism to attend.

To isolate the impact of request size on average cost, we also study the average cost per task (CPT). Fig. 8 highlights several interesting results for the CPT achieved by each mechanism. Firstly, the CPT in a large economy is considerably lower than in a small economy. This is not a surprise as in larger economies the variety of ofers is expected to lower cost of procurement for consumers, regardless of the allocation mechanism.

Secondly, in each economy size, the CPT of complex requests is lower than that of simple requests. This might not be very intuitive as generally it is expected that a product with higher complexity in it lifecycle imposes a higher procurement cost on its consumers. This result is related to our formulation of the composite service selection problem. In this formulation, a bid can win the execution of a request's task as far as it ofers a web service for that task and it is part of the minimum cost allocation, even if the bid includes services that are ir relevant to that request. Therefore, some of the selected bids for a request may include service ofers which are not required by the requester at all, that is, “redundant” services. When the request is complex and thus includes many tasks, the number of redundant services in the winning bids is likely to be lower than in a simple request. Ultimately, a higher number of redundant services increases the average CPT in simple requests.

![](/api/attachments/QZHEPN4W/fulltext/images/0a6743f90813b3e836ede52918f55791488b091f6f58df02bd4ee1f256b6e596.jpg)  
(a) Simple Requests

![](/api/attachments/QZHEPN4W/fulltext/images/18f00b33311cfc9f3ae5fe87120c6cb7d3eefe21f878bdbe842fa09f18ebd8b0.jpg)  
(b) Complex Requests  
Fig. 7. Cost of procuring the first and the last arriving requests in the simultaneous and single auction mechanisms, for (a) simple and (b) complex requests

However, it is worth mentioning that restricting the ofers on their number of redundant services to allow them to be part of the winning allocation for a request will not necessarily reduce the cost. On the contrary, adding any restriction to the current formulation of the CSS problem, including restrictions on the winning ofers' configuration, is expected to increase the average cost of procurement. Moreover, there is no reason to believe that the number of redundant services difer significantly across the three mechanisms.

The results presented in Figs. 6 and 8 also show that in small economies, a fixed-price mechanism attains a procurement cost marginally worse than that achievable through the single or simultaneous auctions. However, in large economies, allocation strategies based on auction models (either single or simultaneous) significantly decrease the procurement cost for the composite service requesters, compared to the fixed-price mechanism.

## 6.4. Statistical analysis of cost

The Kruskal-Wallis test is performed on the CPC of the three mechanisms in which residuals did not follow a normal distribution. We first consider the type of service selection mechanism as the independent variable. The Kruskal-Wallis test shows that the CPCs of at least two mechanisms are statistically significantly diferent K $( \mathrm { d f } = 2 ) \ = 5 5 0 . 4 1 0 , \ p \ < \ 0 . 0 0 1$ 1. The Conover-Iman procedure shows that the CPC of the fixed-price is significantly diferent from the CPC of the two auction mechanisms, and the CPC of the single auction and the simultaneous auction do not difer significantly, which confirms our previous observations.

![](/api/attachments/QZHEPN4W/fulltext/images/39667f5709032895b8908d04d47e40aee434dffb560f21809a343fb3210bda5d.jpg)  
Fig. 8. CPT achieved by the three mechanisms in the four market sectors.

We also estimate the statistical significance of the impact of the economy size and the request complexity at the same time as the impact of the service selection mechanism on the CPC. We performed the Kruskal-Wallis test again with three independent variables. Based on the results, the CPC of at least two groups are significantly diferent from each other, $\mathrm { K _ { o b s e r v e d } } \quad ( \mathrm { d f } = 1 1 ) = 4 2 5 2 . 8 9 4 , \quad \mathrm { p } < 0 . 0 0 1 .$ Performing the Conover-Iman procedure shows that firstly, the CPC of the fixed-price mechanism is significantly diferent to those of the auction-based mechanisms. In other words, the dynamic pricing in auction-based mechanisms achieves lower costs for composite services regardless of the size of the market or the complexity of the requests. Secondly, the CPC of the simultaneous auction is not statistically significantly diferent to that of the single auction in any of the market sectors, except in the (small-complex) sector. As discussed earlier, the reason for the close costs achieved by the simultaneous auction and the single auction is that the cost is averaged over all the successful requests in one simulation round regardless of the order of arrival.

However, the statistical analysis indicates that in small markets with complex requests in demand, the short-term horizon of the single auction achieves lower costs for CSs compared to the simultaneous auction. This means that in this market sector, the small number of requests prevents the simultaneous auction demonstrating its eficiency in terms of the cost.

## 6.5. Solve time

The solve time of the mechanism is the time taken by the solver to match web service ofers and CS requests. A 60-s time limit is set for the solver. Initially. the number of instances in which the solver reached the time limit is studied. This study shows that the fixed-price and single auction mechanisms do not reach the time limit in any of the problem instances. The simultaneous mechanism does not reach the time limit with simple requests regardless of the economy size. With complex requests, it reaches the time limit in 28% of instances in the large economy and 4% of instances in the small economy.

Next, the average solve time of the three mechanisms in each market sector is plotted using logarithmic scale in Fig. 9. The results show that the fixed-price mechanism has the shortest solve time in all market sectors except the small-simple sector. It is then followed by the single auction, again in all market sectors except the small-simple sector where the simultaneous auction is the fastest. These results could be anticipated as the fixed-price mechanism follows a constraint satisfaction approach by searching for the first set of ofers which are below the requester's budget, rather than searching the whole solution space to find an optimal allocation. Simultaneous auction is the slowest due to the complexity of the problem to be solved.

The small-simple sector is an exception to this trend. The reason is that the single auction and fixed-price mechanisms allocate ofers to the requests one by one, while the simultaneous auction solves the allocation problem in one go. Therefore, when the complexity of the problem instance is not high, the simultaneous auction achieves a better solve time than the other two mechanisms.

Despite having the longest solve time in three out of four market sectors, the solve time of the simultaneous auction can be considered reasonable considering the market sectors: the solve time is around 33 s in the large-complex sector, 5 s in the small-complex sector, 1 s in the large-simple sector and 70 ms in the small-simple sector.

## 7. Discussion

The evaluation results show that the longer-term horizon of the simultaneous auction allows for more eficient matching of service ofers and requests (higher success rate), compared to the shorter horizon of the two baseline mechanisms. The single auction and the fixed-price mechanisms achieve similar outcomes in terms of the success rate. A low SR might discourage service requesters and providers from attending a service selection mechanism with a business model based on subscription fees. However, for a business model that only charges the successful participants, it might not be as discouraging, and other factors such as the cost of service provisioning might become more important.

The average cost of procuring CSs achieved by the single auction is not significantly diferent from the cost achieved by the simultaneous auction. However, the simultaneous auction procures the composite services at more homogenous costs, and the requests' order of arrival in the market does not impact their procurement cost. In comparison, in the single auction early requests get the better deals as compared to later requests. This means that in the simultaneous auction model, the service requesters do not have to time their moves for when to enter the market. They can access the service selection mechanism whenever they require web services without being disadvantaged.

The results also demonstrate that dynamic pricing in the auction mechanism benefits service requesters with reduced procurement cost compared to a fixed pricing strategy. Moreover, despite the complexity of simultaneous matching of many requests and ofers, the solve time of the simultaneous auction can be considered reasonable for all market sectors.

![](/api/attachments/QZHEPN4W/fulltext/images/a22fa1690f08471ca26d5afb4a360e537e57ddac33f5efcca5b24742b09bb68e.jpg)  
Fig. 9. Solve time of the three mechanisms to find the best allocation in the four market sectors.

## 8. Conclusions and future work

In this paper, we introduce and analyze CSS in the presence of multiple CS requests and web service ofers. We propose a service selection mechanism based on combinatorial auctions to allocate web service ofers to all the requests simultaneously. We allow service providers to ofer services in bundles, taking into account the interdependencies between services of a composition.

All the requests are treated as equivalent in our model in the sense that factors such as the size or the cost of the requested composition does not afect the service allocation, neither potential relationships between distinct CS requests, such as message passing. Considering such factors and relationships will potentially bring interesting challenges to the mechanism. For example, if the service requesters were to pay a fee based on the cost of the requested composition, the mechanism may benefit from prioritizing more expensive requests. Moreover, the complexity of the proposed ILP model could pose scal ability challenges. Further research is required to develop suitable heuristics or exact methods to improve the solve time and scalability. Lack of public data sets that include information on web services pricing or bundling remains as a limitation for this line of research. Finally, the experiments are conducted while allowing for redundant services in the winning bundles. Further investigation is required to study the performance of the mechanism without such services.

## Acknowledgements

The research in this study was supported in part by DATA61/ NICTA.

## References

[1] UDDI Consortium. UDDI Executive White Paper, [Online]. Available: www,uddi org/pubs/UDDI\_Executive\_White\_Paper.pdf.

[2] A. Jula. E. Sundararajan, Z. Othman, Cloud computing service composition: a

systematic literature review, Expert Systems with Applications 41 (8) (Jun. 2014) 3809–3824.

[3] D. D. Guinard and V. Trifa, Building the web of things: with examples in Node.js and Raspberry Pi. Manning Publications, 2016.

[4] J. Lee, S.-J. Lee, P.-F. Wang, A framework for composing SOAP, non-SOAP and non web services, IEEE Transactions on Services Computing 8 (2) (Mar. 2015) 240–250

[5] M.J. Carey, N. Onose, M. Petropoulos, Data services, Communications of the ACM vol. 55, (6) (Jun. 2012) 86.

[6] S. Deng, L. Huang, D. Hu, J.L. Zhao, Z. Wu, Mobility-enabled service selection for composite services, IEEE Transactions on Services Computing 9 (3) (May 2016) 394–407.

[7] L. Zeng, B. Benatallah, M. Dumas, J. Kalagnanam, Q.Z. Sheng, Quality driven web services composition. The 12th International Conference on World Wide Web. ACM Budapest, Hungary, 2003, pp. 411–421.

[8] G. Canfora, M. Di Penta, R. Esposito, M.L. Villani, An Approach for QoS-Aware Service Composition Based on Genetic Algorithms, Proceedings of the 2005 Conference on Genetic and Evolutionary Computation, ACM, Washington DC, USA, 2005, pp. 1069–1075.

[9] A. Michlmayr, F. Rosenberg, P. Leitner, S. Dustdar, End-to-end support for QoSaware service selection. binding, and mediation in VRESCo. JEEE Transactions or Services Computing 3 (3) (2010) 193–205.

[10] Q. He, J. Yan, H. Jin, Y. Yang, Quality-aware service selection for service-based systems based on iterative multi-attribute combinatorial auction, IEEE Transactions on Software Engineering 40 (2) (Feb. 2014) 192–215.

[11] Z. Ye, S. Mistry, A. Bouguettaya, H. Dong, Long-term QoS-aware cloud service composition using multivariate time series analysis. JEEE Transactions on Services Computing 9 (3) (May 2016) 382–393.

[12] L. Atzori, A. Iera, G. Morabito, The internet of things: a survey, Computer Networks 54 (15) (Oct, 2010) 2787–2805

[13] L, Da Xu. W. He. S. Li. Internet of things in industries: a survey, JEEE Transactions on Industrial Informatics 10 (4) (Nov. 2014) 2233–2243.

[14] A. Malki, M. Barhamgi, S.-M. Benslimane, D. Benslimane, M. Malki, Composing data services with uncertain semantics. JEEE Transactions on Knowledge and Data Engineering 27 (4) (Apr. 2015) 936–949.

[15] K. Cho, et al., Render Verse: Hybrid Render Farm for Cluster and Cloud Environments, 2014 7th International Conference on Control and Automation.

[16] B. Javed, P. Bloodsworth. R.U. Rasool, K. Munir, O. Rana, Cloud market maker: An automated dynamic pricing marketplace for cloud users, Future Generation

[17] M. Moghaddam and J. Davis, “Service Selection in Web Service Composition: A Comparative Review of Existing Approaches,” in Web Services Foundations, 1, A. Bouguettaya, Q. Z. Sheng, and F. Daniel, (Eds.) Springer New York, 2014, pp. 321-346.

[18] Q.Z. Sheng, X. Qiao, A.V. Vasilakos, C. Szabo, S. Bourne, X. Xu, Web services composition: a decade's overview, Information Sciences 280 (Oct. 2014) 218–238.

[19] C. Jatoth, G.R. Gangadharan, R. Buyya, Computational intelligence based QoS aware web service composition: a systematic literature review, IEEE Transactions on Services Computing 10 (3) (May 2017) 475–492

[20] A.L. Lemos, F. Daniel, B. Benatallah, Web service composition, ACM Computing Surveys 48 (3) (Dec. 2015) 1–41.

[21] S. de Vries, R.V. Vohra, Combinatorial auctions: a survey, INFORMS Journal on

[22] M. Schwind, Dynamic Pricing and Automated Resource Allocation for Complex Information Services, Springer, 2007.

[23] M. Moghaddam, J.G. Davis, Amin Beheshti, Mustafa Hashmi, Hai DongWei, Emma Zhang (Eds.), Auction-Based Models for Composite Service Selection: A Design Framework, Springer, Cham, 2018, pp. 101–115.

[24] M. Bichler, A. Davenport, G. Hohner, J. Kalagnanam, Industrial procurement auctions, in: P.C. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, Cambridge, Mass.; London, 2006, pp. 593–612.

[25] L. Blumrosen, N. Nisan, Combinatorial auctions, Algorithmic Game Theory, Cambridge University Press, 2007, pp. 267–299.

[26] S. Parsons, J.A. Rodriguez-Aguilar, M. Klein, Auctions and bidding: a guide fo computer scientists, ACM Computing Surveys 43 (2) (2011) 1–59.

[27] S. Ding, Y. Li, D. Wu, Y. Zhang, S. Yang, Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model, Decision Support Systems 107 (Mar. 2018) 103–115.

[28] X. Chen, Z. Zheng, Q. Yu, M.R. Lyu, Web service recommendation via exploiting location and OoS information. JEEE Transactions on Parallel and Distributed Systems 25 (7) (Jul. 2014) 1913–1924.

[29] S. Ding, Z. Wang, D. Wu, D.L. Olson, Utilizing customer satisfaction in ranking prediction for personalized cloud service selection, Decision Support Systems 93 (Jan. 2017) 1–10.

[30] Y. Hu, Q. Peng, X. Hu, R. Yang, Web Service Recommendation Based on Time Series Forecasting and Collaborative Filtering. 2015 IEEE International Conference on Web Services, 2015, pp. 233–240.

[31] J. El Haddad, M. Manouyrier, M. Rukoz, TOoS: transactional and OoS-aware selection algorithm for automatic web service composition, IEEE Transactions on Services Computing 3 (1) (2010) 73–85.

[32] L. Zeng, B. Benatallah, A.H.H. Ngu, M. Dumas, J. Kalagnanam, H. Chang, QoSaware middleware for web services composition, IEEE Transactions on Software Engineering 30 (5) (2004) 311–327.

[33] T. Yu, Y. Zhang, K.J. Lin, Eficient algorithms for Web services selection with end to-end QoS constraints, ACM Transactions on the Web (TWEB) 1 (1) (2007) 6:1–6:26.

[34] D. Ardagna, B. Pernici, Adaptive service composition in flexible processes, IEEE Transactions on Software Engineering 33 (6) (2007) 369–384.

[35] V. Cardellini, E. Casalicchio, V. Grassi, S. Iannucci, F. Lo Presti, R. Mirandola, MOSES: a framework for QoS driven runtime adaptation of service-oriented systems, IEEE Transactions on Software Engineering 38 (5) (Sep. 2012) 1138–1159.

[36] Y. Ma, C. Zhang, Quick convergence of genetic algorithm for QoS-driven web ser vice selection, Computer Networks 52 (5) (2008) 1093–1104.

[37] X.-Q. Fan, X.-W. Fang, C.-J. Jiang, Research on Web service selection based on cooperative evolution, Expert Systems with Applications 38 (8) (Aug. 2011) 9736–9743.

[38] P. Wang, X. Du, QoS-aware service selection using an incentive mechanism, IEEE Transactions on Services Computing (2016) 1.

[39] L. Pan, B. An, S. Liu, L. Cui, Nash Equilibrium and Decentralized Pricing for QoS Aware Service Composition in Cloud Computing Environments, 2017 IEEE International Conference on Web Services (ICWS), 2017, pp. 154–163.

[40] P. Samimi, Y. Teimouri, M. Mukhtar, A combinatorial double auction resource allocation model in cloud computing, Information Sciences 357 (Aug. 2016)

[41] Z. Sun, Z. Zhu, L. Chen, H. Xu, L. Huang, A Combinatorial Double Auction Mechanism for Cloud Resource Group-Buving. 2014 JEEE 33rd International Performance Computing and Communications Conference (IPCCC). 2014. pp. 1–8

[42] A.M. Omer, A. Schill, Web Service Composition Using Input/Output Dependency Matrix, Proceedings of the 3rd workshop on Agent-oriented Software Engineering Challenges for Ubiquitous and Pervasive Computing, 2009, pp. 21–26.

[43] R. Aggarwal, V. Kunal, J. Miller, W. Milnor, Constraint driven Web service composition in METEOR-S, IEEE International Conference on Services Computing (SCC 2004), 2004, pp. 23–30.

[44] M. Moghaddam, J. Davis, T. Viglas, A Combinatorial Auction Model for Composite Service Selection Based on Preferences and Constraints, 10th IEEE Internationa Conference on Services Computing (SCC 2013), IEEE, Santa Clara, CA, USA, 2013.

[45] L. Ai, M. Tang, OoS-Based Web Service Composition Accommodating Inter-service Dependencies Using Minimal-Conflict Hill-Climbing Repair Genetic Algorithm, IEEE Fourth International Conference on eScience (eScience ‘08), 2008, pp. 119–126.

[46] S. Deng, H. Wu, D. Hu, J. Leon Zhao, Service selection for composition with OoS correlations. JEEE Transactions on Services Computing 9 (2) (Mar, 2016) 291–303

[47] S. Lamparter, Policy-Based Contracting in Semantic Web Service Markets, PhD Dissertation, Karlsruhe Institute of Technology, 2007.

[48] M. Mohabey, Y. Narahari, S. Mallick, P. Suresh, S.V. Subrahmanya, A Combinatorial Procurement Auction for QoS-Aware Web Services Composition, IEEE Internationa Conference on Automation Science and Engineering (CASE 2007), 2007, pp. 716–721.

[49] B. Prashanth. Y. Narahari. Efficient Algorithms for Combinatorial Auctions With Volume Discounts Arising in Web Service Composition. JEEE International Conference on Automation Science and Engineering, 2008, pp. 995–1000.

[50] Q. Wu, M. Zhou, Q. Zhu, Y. Xia, VCG auction-based dynamic pricing for multi granularity service composition, IEEE Transactions on Automation Science and Engineering (2017) 1–10.

[51] M.P. Papazoglou, Service-Oriented Computing: Concepts, Characteristics and Directions, Fourth International Conference on Web Information Systems Engineering (WISE 2003), 2003, pp. 3–12.

[52] Q. Tang, Economics of Web Service Provisioning: Optimal Market Structure and Intermediary Strategies, Doctoral Dissertation University of Florida, 2004.

[53] S.-Y. Hwang, C.-H. Lee, Reliable web service selection in choreographed environ ments, Decision Support Systems 54 (3) (Feb. 2013) 1463–1476.

[54] C. Peltz, Web services orchestration and choreography, IEEE Computer Society 36 (10) (2003) 46–52.

[55] M.B. Blake, D.J. Cummings, A. Bansal, S. Kona Bansal, Workflow composition of service level agreements for web services, Decision Support Systems 53 (1) (Apr. 2012) 234–244.

[56] S. Zimmermann, M. Müller, B. Heinrich, Exposing and selling the use of web ser vices—an option to be considered in make-or-buy decision-making, Decision Support Systems 89 (Sep. 2016) 28–40.

[57] M.W. Padberg, Linear Optimization and Extensions, Springer, 1999

[58] M.C. Jaeger, G. Mühl, S. Golze, QoS-aware composition of web services: an evaluation of selection algorithms, in: R. Meersman, Z. Tari (Eds.), On the Move to Meaningful Internet Systems 2005: CoopIS, DOA, and ODBASE, 3760 Springer Berlin, Heidelberg, 2005, pp. 646–661.

[59] Z. Zheng, Y. Zhang, M.R. Lyu, Investigating QoS of real-world web services, IEEE Transactions on Services Computing 7 (1) (Jan. 2014) 32–39.

[60] E. Al-Masri, Q.H. Mahmoud, QoS-Based Discovery and Ranking of Web Services, Proceedings of 16th International Conference on Computer Communications and Networks (ICCCN 2007), 2007, pp. 529–534.

[61] C. Weinhardt, B. Blau, T. Conte, L. Filipova-Neumann, T. Meinl, W. Michalk, The Vision of Web Service Markets, Business Aspects of Web Services, Springer, 2011, pp. 191–194.

[62] T. Sandholm, Algorithm for optimal winner determination in combinatorial auc tions, Artificial Intelligence 135 (1) (2002) 1–54.

[63] K. Leyton-Brown, M. Pearson, Y. Shoham, Towards a Universal Test Suite for Combinatorial Auction Algorithms. The 2nd ACM Conference on Flectronic com merce, 2000, pp. 66–76.

[64] T. Sandholm, S. Suri, A. Gilpin, D. Levine, CABOB: a fast optimal algorithm for winner determination in combinatorial auctions, Management Science 51 (3) (2005) 374–390.

[65] M. Moghaddam, “Combinatorial Auction-based Mechanisms for Composite Web Service Selection,” Sydney, NSW: University of Sydney. Available: http://hdl. handle.net/2123/13512, 2015.

[66] J. Chen, X. Chen, X. Song, Comparison of the group-buying auction and the fixed pricing mechanism, Decision Support Systems 43 (2) (Mar. 2007) 445–459

[67] AMPL Optimization Inc., AMPL Streamlined Modeling For Real Optimization, [Online]. Available: https://ampl.com/. (2018) [Accessed: 31-Mav-2018]

[68] W.H. Kruskal, W.A. Wallis, Use of ranks in one-criterion variance analysis, Journa of the American Statistical Association 47 (260) (1952) 583–621.

[69] W.J. Conover, R.L. Iman, Rank transformations as a bridge between parametric and nonparametric statistics. The American Statistician 35 (3) (1981) 124–129.

[70] Wendell Santos, Which API Types and Architectural Styles are Most Used? ProgrammableWeb, 2017 [Online]. Available: https://www.programmableweb. com/news/which-api-types-and-architectural-styles-are-most-used/research/2017/ 11/26 [Accessed: 15-Feb-2018].

![](/api/attachments/QZHEPN4W/fulltext/images/f302c28c2543e87ae82b8636c1916d192f3d6eeec0b369f0ad79dac4781f1e53.jpg)

Mahboobeh Moghaddam is a postdoctoral research fellow at the Australian Institute of Business and Economics, th University of Oueensland in Brisbane Australia She re ceived her PhD in Information Technology from the University of Sydney in 2015. She has a B.Sc. and a M.Sc. in Software Engineering from Amirkabir University of Technology and Sharif University of Technology, Iran, respectively. She is a recipient of multiple research and innovation scholarships and awards. including Advanced Queensland, UsydIS, NRPA (NICTA Research Project Award). and NASSCOM IT. Her research interests include web services, optimization models, mechanism design, and auction models

![](/api/attachments/QZHEPN4W/fulltext/images/fe01c6931f91e506936afcea29a32fb058f1479ea1e41db03553526d80d8e7cf.jpg)

Joseph G. Davis is the Professor of Information Systems and Services at the School of Computer Science, the University of Sydney. Australia. He has been active researcher in the information systems field. with a focus or research questions at the intersection between information systems and computer science, namely on semantic information processing, crowdsourcing, decision support, and service computing, In particular. he has contributed extensively to understanding the creation. sharing and utili. zation of information and knowledge in organizations and the links to decision making. He is a recipient of the IBM Faculty Research award for IT services-related research. His research has been funded by the Australian Research Council, Carnegie Bosch Institute, and IBM Research Labs

among others. He is a Charter Member of the Association for Information Systems, a Senior Member of the Association for Computing Machinery (ACM) and a Member of the IEEE.
