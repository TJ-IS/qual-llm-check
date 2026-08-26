---
otero_id: 10206
otero_key: "4NQWW8HZ"
title: "An adaptive coordination framework for fast atomic multi-business transactions using web services"
authors: "Jonghun Park; Ki-Seok Choi"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.05.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An adaptive coordination framework for fast atomic multi-business transactions using web services

Jonghun Park <sup>a,⁎</sup>, Ki-Seok Choi <sup>b</sup>

<sup>a</sup> Department of Industrial Engineering, Seoul National University, San 56-1, Silim-Dong, Kwanak-Gu, Seoul 151-742, South Korea <sup>b</sup> Hankuk University of Foreign Studies, South Korea

Received 26 March 2005; received in revised form 9 May 2006; accepted 14 May 2006 Available online 21 June 2006

## Abstract

Web services are emerging as an effective means for carrying out automated transactions between multiple business parties. While there are several specific protocols that have been discussed to address the problem of coordinating web services-enabled business transactions, we consider the tentative hold protocol (THP) that allows the placement of tentative holds on business resources prior to actual transactions in order to provide increased flexibility in coordination. In this paper, we present a formal coordination framework for applying THP in conjunction with two phase commit protocol to the problem in which service providers independently manage resources and clients seek to acquire the resources from multiple providers as a single atomic transaction. The proposed framework facilitates the performance optimization of THP through effective parameterization with the notion of overhold size and hold duration. Subsequently, a detailed analysis is carried out to obtain an efficient method that can optimize the performance by adaptively determining the hold duration. The simulation results show that the proposed adaptive approach yields a significant improvement over other non-adaptive policies © 2006 Elsevier B.V. All rights reserved.

Keywords: Web services; Business transactions; Tentative hold protocol; Two phase commit protocol; Distributed coordination

## 1. Introduction

Currently significant efforts are being invested in application integration, enabling business processes of different companies to interact and form complex multiparty processes. In particular, as web services are becoming the predominant technology for facilitating business-to-business (B2B) collaboration, there are increasing needs for the enhanced transaction models that can effectively support complex, multi-party business interactions based on web services. Although efficient and reliable, the traditional transaction models that require fine-grained control of locking and close trust are not directly applicable for open, loosely coupled computing environments consisting of autonomous and heterogenous services [21]. In a web service based B2B environment, transactions are often complex, involve multiple autonomous parties, span many independent organizations, and may have long duration [17].

There are a number of emerging specifications that seek to address the requirements of such web service based collaborative business transactions. These specifications define a flexible and extensible framework for the coordination of loosely-coupled web services by use of a predefined set of transaction semantics, and they also suggest new notions of transactions that relax some of the ACID properties [1] of conventional transaction processing [6].

Business Transaction Protocol (BTP) [15], a committee specification of the Organization for the Advancement of Structured Information Standards (OASIS), is proposed to support interactions that cross application and administrative boundaries, requiring extended transactional support beyond the ACID properties. It is based on two phase commit (2PC) [1] for short duration interactions called atoms, which can be further aggregated into larger non-ACID transactions called cohesions [12]. More recently, Web Services Transaction (WS-Transaction) proposed by IBM and Microsoft [4] provides specifications for atomic transactions in a trusted domain that uses 2PC, and for business activities using compensating transactions. It also defines an XML-based protocol for multiple transaction processing platforms to interoperate.

Taking a slightly different approach to the problem, Tentative Hold Protocol (THP) [19], published as a W3C (World Wide Web Consortium) note, attempts to define a building block that can work with other technologies in order to facilitate the automated coordination of multi-business interactions as well as the creation of new opportunities to leverage the web services to improve business efficiencies. THP is an open, loosely coupled, messaging-based framework for the exchange of tentative commitments between businesses prior to actual transaction [19]. It addresses more semantic issues than low-level transactional mechanisms by providing a standard means for trading partners to place tentative holds for business resources.

In this protocol, it is possible that multiple clients can place tentative holds on the same item prior to sale, and whenever one client completes the purchase of the item, the other clients may receive notifications that their holds are not valid any more. Hence, the clients have the ability to request tentative holds on the resources they want to acquire as a single coordinated purchase, verifying availability before completing the transaction. On the other hand, the resource providers may grant non-blocking reservations on their products, retaining control of their resources, while allowing the clients greater flexibility in coordinating their acquisitions.

When combined with existing multi-business transaction coordination methods such as custom applications, compensating transactions, and 2PC, THP can provide several significant benefits. In particular, as claimed in [22], introducing a tentative hold phase to long-running collaborative business applications that employ 2PC protocol for ensuring atomicity of multitransactions can overcome the limitations of the pure 2PC. THP allows clients to tentatively obtain resources for long time periods before entering the prepare phase of a 2PC transaction, enabling the possibility that the clients make tentative commitments to the terms of a contract and make all decisions without actually requiring the resource provider to lock such resources for the duration. Accordingly, it can shorten the required 2PC lock duration by reducing the time spent on the prepare phase while at the same time it will also facilitate minimizing the time required for business applications to successfully complete their multitransactions. The result of a simulation study that shows the performance improvement achieved by adding THP to 2PC in a generalized resource allocation environment that allows co-allocation of arbitrary number of resources as well as alternative resource coallocation schemes can be found in our earlier work [18].

In this paper, we consider the problem in which businesses independently manage and expose their resources through web services and client applications seek to acquire resources from them as a single atomic web service transaction [11]. In such circumstances, the clients are competing for finitely available resources, and it is not guaranteed that the required resources are always available. Moreover, the client should be able to achieve all-or-nothing semantics for the entire end-toend transaction: if some of the transactions for resource acquisition are not successful, the entire transaction must be canceled. This problem is getting increasing attention in many real-world application contexts [5,9,3], including an e-commerce application that seeks to identify the best combination of many small orders from several businesses for making a purchase [22], a travel web service that interacts with flight, hotel, and car rental services [16], and a supply chain management application that carries out conversational transactions via the web services of suppliers and shippers [7].

Coordination of this kind of multi-business transactions could be carried out through the human intervention or the creation of a custom application that is aware of the inter-dependencies among the transactions. However, the increasing complexity of multi-business interactions driven by the technologies for automated discovery and integration of web services makes it necessary to flexibly automate the coordination in order to increase the business efficiency and agility [20]. Indeed the THP's key contribution is the flexibility it provides with the notion of tentative holds whose life expectancy can be explicitly defined. It can enhance the flexibility by providing targeted customer service in the granting of holds, specifying greater or less hold expiration periods for a given hold request, and allowing notification to clients when another client reserves some resource [22]. Yet, presently the problem of determining whether or not a particular tentative hold requested by a client should be granted and for how long still remains unexplored.

Motivated by this, the objective of this paper is to address the issue of optimizing the performance of THP to realize its full potential when it is used in conjunction with 2PC for the problem outlined above. The starting point for our discussion is the observation that THP can be effectively characterized in terms of two parameters, namely overhold size and hold duration, each of which respectively represents the number of holds that can be placed on a single available resource, and the time period during which a granted hold is valid. As will be detailed in the next section, these parameters represent the resource provider's commitment to the service level, and may vary according to the specific provider. Furthermore, the proposed parameterization provides a basis for constructing Petri net-based [23,24] formal behavioral models of clients and resource providers that are participating in the multi-transactions spanning organizational boundaries.

The proposed THP characterization also provides a framework where one can seek to minimize the time required for clients to successfully complete their multitransactions. Specifically, two different cases depending on the value of the overhold size are taken into consideration. In the first case, we examine the case in which the overhold size is finite, and propose computational methods to adaptively determine the hold duration that can lead to overall reduced transaction completion time. In the second case in which the overhold size is infinite, we show the result that the performance is indifferent to the individual resource provider's decision on the hold duration. The proposed method assumes that each provider is autonomous and fully decentralized, and does not require any single party controlling all the resources needed for a transaction. Therefore, it is anticipated that the proposed framework will facilitate more efficient multi-party business transactions, resulting in faster transaction, higher resource utilization, and better customer satisfaction in e-business.

The paper is organized as follows: the next section presents a characterization of THP based on the overhold size and hold duration, and then introduces

Petri net-based models to define formal models of the participants' behavior considered in the paper. Subsequently, Section 3 describes the methods that compute the hold duration for two different cases: Section 1 for finite overhold case and Section 2 for infinite overhold. In Section 4, we demonstrate the efficacy of the proposed approach through the simulation experimentation. Finally, Section 5 concludes the paper by pointing out some future research work.

## 2. Proposed protocol for atomic multi-business transactions

## 2.1. Characterization of tentative hold protocol

In web services computing, services are platform and network independent operations that clients or other services invoke [14]. The distributed system model considered in this paper consists of a set of service provider processes $S { = } \left\{ s _ { 1 } , { \bf \phi } . . . , s _ { m } \right\}$ that expose their resources as web services, and a set of client processes $C { = } \{ c _ { 1 } , . . . , c _ { n } \}$ , each of which seeks to acquire a set of resources from the providers, denoted by $\bar { R } _ { j } { \in } 2 ^ { S }$ , such that $R _ { j } \neq \emptyset , j { = } 1 , . . . , n$ . Service provider $s _ { i } , i { = } 1 , . . . , m$ manages resources of the same type, and we denote the number of resources available at time t by $r _ { i } ( t )$ . It is assumed that client $c _ { j }$ needs to acquire the resources defined in $R _ { j }$ as a single atomic transaction. That is, it makes no sense for a client to allocate only a subset of its required resources, and a whole transaction can be completed only if all the required resources are successfully allocated as a bundle.

We use 2PC protocol to achieve the atomicity. Each service provider implements interfaces for a <sup>prepare</sup> method, an <sup>abort</sup> method, and a <sup>commit</sup> method. In the 2PC protocol considered in this paper, a transaction is initiated by a client which invokes the <sup>prepare</sup> methods of its service providers to determine if all the required resources are available for <sup>commit</sup>. When a service provider receives a request for prepare, it first locks the resources requested if they are available, and replies with <sup>yes</sup>. Otherwise, the service provider replies with <sup>no</sup>. Subsequently the client will either invoke the <sup>commit</sup> method to complete the transaction if all service providers associated with the transaction replied with yes or invoke the <sup>abort</sup> method if some of the replies were <sup>no</sup>.

As discussed in [13,6,18], however, a simple application of 2PC protocol outlined above to coordinate long-running collaborative business applications may end up with undesirable long lock duration, resulting in lower resource utilization and less number of successful transaction completions. To overcome this problem, we add a tentative hold phase to 2PC by requiring the clients to obtain tentative holds from their respective resource providers before they initiate a 2PC transaction. This augmented protocol will be referred to as THP +2PC in this paper.

A set of interfaces defined for the service providers is used to facilitate the interactions based on THP. We define a <sup>hold</sup> method for the clients to request a tentative hold on some resource, and a <sup>cancel</sup> method to request removal of a current active hold. The result of the hold invocation is either <sup>yes</sup> or <sup>no</sup> indicating the success or failure of a hold request. A hold request made by a client when the service provider has no available resource will be immediately rejected, and the client will be replied with $\mathrm { n o }$ . On the contrary, when there is more than one resource available, the decision on the acceptance or rejection of a requested hold from a client may vary according to the service provider. One extreme policy the service provider can take is to approve only one hold request for each available resource, whereas the other extreme policy is to grant as many hold requests as it wants provided that there is at least one available resource. Generalizing these two extremes, we introduce the notion of overhold size that can characterize the service provider's commitment to a certain service level.

Specifically, the overhold size represents the number of holds that can be placed on one unit of available resource, and it will be denoted by a positive real number $k _ { i } ,$ such that $k _ { i } { \ge } 1 , i { = } 1 , . . . , m$ . That is, at time $0 ,$ service provider $s _ { i }$ will be able to grant holds to the first $k _ { i } r _ { i } ( 0 )$ hold requests, but afterwards it will reject all further hold requests unless a new resource becomes available. We let $h _ { i } ( t )$ be the number of valid holds issued by $s _ { i }$ at time t. Under $\mathrm { T H P } + 2 \mathrm { P C }$ protocol, a client that has a hold is entitled to enter a 2PC phase. Hence, when there is more than one client possessing holds for one resource, any of them may initiate 2PC phase by invoking a <sup>prepare</sup> method, claiming one resource to be locked. In this case, one unit of the resource will become unavailable, and the number of active holds will be immediately decreased by one. Furthermore, the service provider will need to expire $e _ { i } ( t )$ additional holds, where $e _ { i } ( t )$ is the number of holds to be expired at time t which is computed as follows.

$$
e _ {i} (t) = \max \{0, h _ {i} (t) - k _ {i} r _ {i} (t) \}, i = 1, \dots , m\tag{1}
$$

For example, let $k _ { i } = 2$ and $r _ { i } ( t _ { 1 } ) = 3$ . Assuming that $h _ { i }$ $( t _ { 1 } ) \ d s = 6 ,$ , the number of holds to be expired, when a <sup>prepare</sup> request is approved for a client having a hold at $t _ { 2 } \ ( t _ { 2 } { > } t _ { 1 } )$ , is $e _ { i } ( t _ { 2 } ) = \operatorname* { m a x } \{ 0 , 5 - 2 \cdot 2 \} = 1$ . On the other hand, if we assumed $h _ { i } ( t _ { 1 } ) { = } 2 , e _ { i } ( t _ { 2 } )$ would be max $\{ 0 , 5 - 2 \cdot 2 \} = 0 .$

As it is clear from the above discussion of the overhold size, the higher value of $k _ { i }$ will allow more tentative holds to be placed on available resources, potentially decreasing the time spent on the tentative hold phase. At the same time, however, it will also lead to the increased number of expirations of active holds, and clients will experience more frequent unexpected expiration of their holds. For instance, in the extreme case in which $k _ { i } = \infty ,$ , the service provider will grant a hold as long as there is one resource available, and will expire all the current holds when there is no resource available. That is, the overhold size can be understood as a parameter that reflects the service provider's policy on the quality of service for its clients in terms of the frequency of unexpected expirations, and it should be determined in such a way that the quality of service agreed with the clients can be guaranteed.

Another method defined for the service provider when a hold placed on a resource needs to be invalidated, is an <sup>expire</sup> that notifies an expiration of an active hold to the corresponding clients. An expiration of a hold occurs when (i) the service provider has no available resource any more, (ii) the number of current active holds exceeds the maximum number of holds allowed under the specified overhold size, or (iii) the timeout associated with a hold expires. In particular, having a timeout for each active hold introduces the problem of determining the hold duration which can significantly affect the performance of the system. The hold duration represents a contract granting tentative rights over a shared resource for a limited period of time. It specifies the time period during which a granted hold is valid, and it is determined independently by individual service provider whenever a new hold is approved. When the lifetime of an active hold reaches this preset time period, the service provider will immediately invalidate the hold, and notify an expiration to the corresponding client. Therefore, it is not allowed for the clients to maintain a hold indefinitely during their resource acquisition process, and consequently, with the finite hold duration, THP+2PC can effectively eliminate deadlock and avoid unnecessary long blocking.

Different methods for computing hold duration can be defined based on different characteristics, resulting in a different objective to be optimized. One of our objectives is to find the hold duration that can minimize the average waiting time incurred to clients before they successfully complete their atomic multitransactions. The actual formulation used in THP + 2PC to adaptively compute the hold duration is presented in Section 3. Two parameters proposed in this paper, namely the overhold size and the hold duration, provides a framework in which the performance of THP +2PC can be optimized. Finally, we assume that a reliable transport protocol such as TCP/ IP is used for message communication so that the <sup>cancel</sup> and <sup>expire</sup> methods can be defined as asynchronous calls that do not require the result of a request to be delivered.

## 2.2. Protocol specification

This section presents Petri net (PN) based formal definitions of the behaviors of clients and service providers that follow the THP+2PC protocol. For the purpose of the subsequent discussion, we only explicitly model the THP and 2PC phases, not the detailed business logic that may be different according to the application domain. Although we use PN as a specification tool, we remark that it can also be implemented as a program logic for controlling the behaviors of clients and service providers. For details of implementing PNs as controllers, the interested readers are referred to [24].

The behavior of a service provider, $s _ { i } , i { = } 1 , . . . , m ,$ implementing the THP + 2PC protocol is formally defined as a PN in Fig. 1 where each transition is annotated with its meaning. Whenever a new resource becomes available, transition $t _ { i , 1 }$ fires, and $k _ { i }$ tokens are deposited to place $p _ { i , 1 }$ that represents the available holds that can be issued by service provider $s _ { i } .$

Transition $t _ { i , 2 }$ models the receipt of a hold request from a client, and the corresponding response of the service provider. As indicated in Fig. 1, a new hold can be granted only if there is a token in place $p _ { i , 1 }$ . On the approval of a new hold, a hold duration is dynamically computed afresh, and the yes reply is delivered to the client. If it is not possible to grant a hold, the service provider will reply with no. We remark that the firing of $t _ { i , 2 }$ does not need to be immediate. Depending on the application context, the service provider may need to have some time to make a final decision on the approval of a hold.

Place $p _ { i , 2 }$ represents the holds already granted by $s _ { i } .$ Therefore, from the definition of overhold size, it follows that the total number of tokens contained collectively in places $p _ { i , 1 }$ and $p _ { i , 2 }$ should always be equal to $k _ { i } r _ { i } ( t )$ . The receipt of a <sup>prepare</sup> request from a client is modeled by $t _ { i , 3 }$ that also generates the reply to the client and notifies hold expirations to other affected clients if necessary. Transitions $t _ { i , 4 }$ and $t _ { i , 5 }$ respectively represent the arrival of a <sup>cancel</sup> request from a client and the event that a hold duration reaches its prespecified timeout.

Place $p _ { i , 3 }$ denotes the resources in <sup>prepare</sup> state, waiting to be committed or aborted. On <sup>commit</sup> request $\left( \mathrm { i . e . , ~ } t _ { i , 7 } \right)$ , one token will be simply removed from $p _ { i , 3 ; }$ , indicating that one resource becomes committed and unavailable. On the other hand, an <sup>abort</sup> request $\left( \mathrm { i . e . , ~ } t _ { i , 6 } \right)$ will remove one token from $p _ { i , 3 }$ , and put $k _ { i }$ tokens back to place $p _ { i , 1 }$ , indicating that $k _ { i }$ more holds can now be issued owing to the availability of a single resource.

![](/api/attachments/4NQWW8HZ/fulltext/images/353dc26ee4c39a08085fcb691614ba54783531a262661124a350489bfb721e58.jpg)  
Fig. 1. Petri net representation of the behavior of a service provider.

In order to be consistent with the overhold management scheme described in Section 1, firing of $t _ { i , 3 }$ requires to remove x and $y$ tokens from both places $p _ { i , 1 }$ and $p _ { i , 2 }$ , where x and y are nonnegative integers whose sum should be always equal to $k _ { i } .$ The actual valuation of x and y will be determined by assigning higher priority to the arc between $p _ { i , 1 }$ and $t _ { i , 3 }$ . That is, as long as there are tokens in $p _ { i , 1 } ,$ , they will be removed first. For instance, suppose that $k _ { i , - 3 , m } ( p _ { i , 1 } ) { = } 1$ , and m $( p _ { i , 2 } ) \mathop { = } 5$ , where $m ( )$ represents the marking (i.e., the number of tokens in a place). When $t _ { i , 3 }$ fires, x + y = 3 tokens need to be removed from the places $p _ { i , 1 }$ and $p _ { i , 2 }$ By firing the arc $\left( p _ { i , 1 } , \ t _ { i , 3 } \right)$ first, we get $x = 1$ , and therefore $y = 2$

Invocation of a <sup>hold</sup> method is idempotent: when a service provider receives a hold request from a client that already has an active hold, such request is replied with <sup>yes</sup>. However, the hold duration will not be renewed in this case. In addition, as indicated in the weight of arc $( t _ { i , 6 } , ~ p _ { i , 1 } )$ , the hold of the client that requests an abort will not be renewed. Finally, we remark that although we assume consumable resources in Fig. 1, a PN model for reusable resources can also be obtained by merging the transitions $t _ { i , 7 }$ and $t _ { i , 1 }$

Fig. 2 shows a PN specification of the client's behavior following the proposed THP + 2PC protocol. Upon creation $( \mathrm { i } . \mathrm { e } . , t _ { j , 1 } )$ , client $c _ { j } , j { = } 1$ , …, n requests holds to all the service providers defined in $R _ { j } .$ . This event is modeled as transition $t _ { j , 2 }$ . Since the <sup>hold</sup> is a blocking method that must result in either yes or no, place $p _ { j , 2 }$ represents that the client is waiting until all the replies are received. Depending on the results of the hold requests, the client can make a transition to either state $p _ { j , 3 }$ or $p _ { j , 7 }$ . When all the replies are yes $( \mathrm { i . e . , } t _ { j , 3 } )$ the client's state is changed to $p _ { j , 3 }$ where it is entitled to start a <sup>prepare</sup> phase of 2PC.

For some applications, the client staying at state $p _ { j , 3 }$ may need some more time to further negotiate with service providers or cancel its current active hold, which may result in expiration or cancellation of holds that are already placed. Such contingencies are modeled through the use of transitions $t _ { j , 6 }$ and $t _ { j , 7 }$ that respectively models the invocation of a <sup>cancel</sup> method and the occurrence of an expiration event.

Place $p _ { j , 4 }$ models the client waiting for the results of invoking <sup>prepare</sup> methods. When all service providers in $R _ { j }$ agree to <sup>prepare</sup>, transition $t _ { j , 8 }$ will fire to request <sup>commits</sup>, and subsequently the client will simply wait until all the acknowledgments from the service providers are received. Otherwise, the client needs to undo the entire transaction following the 2PC semantics by firing $t _ { j , 9 } ,$ which requires the invocation of <sup>abort</sup> methods of the client's service providers that have agreed to <sup>prepare</sup>. The results of abort requests will also be acknowledged as modeled by $t _ { j , 1 1 }$

![](/api/attachments/4NQWW8HZ/fulltext/images/bcb1b2dbd284edccbdecf648e8ba0f5120acb0cdb9fbbd621991d0bbd0c1d0ab.jpg)  
Fig. 2. Petri net representation of the behavior of a client.

Finally, place $p _ { j , 7 }$ represents the state where the client is waiting for the next retrial which is made when the client wakes up after some randomly generated backoff time. This wake-up event is represented by $t _ { j , 1 3 }$ . Basic purposes of introducing a backoff time between the client's two successive trials are two-folds: first, the service providers may not want to receive too frequent requests for <sup>hold</sup> when there is no available resource, and may set some lower bound on the acceptable inter-trial times for the clients. Second, under the reliable transport protocol assumed in this paper, the possibility of receiving a stale expiration message from a service provider (i.e., the expiration pertaining to the previous round) can be minimized by having the backoff time much bigger than the usual message delivery time (this event is modeled as $t _ { j , 1 2 }$ in Fig. 2).

## 3. Analytical models for computing hold duration

In this section, formal analysis for computing the hold duration is carried out in detail. In Section 3.1, we first consider the finite overhold case and propose a novel method to adaptively compute the hold duration based on the local information available to individual service provider. Then, Section 3.2 considers the infinite overhold case, and shows that the average time for clients to complete their atomic multi-transactions is indifferent to the length of hold duration.

## 3.1. Hold duration for finite overhold case

The main goal of this section is to discuss the details of the proposed hold duration computation scheme, inspired by the reliability theory for a multi-component parallel system. As defined in Fig. 2, a client is not allowed to enter the <sup>prepare</sup> phase until it obtains holds for all the required resources. Unless the overhold size is infinite, any outstanding holds granted to clients will necessarily decrease the chance of granting further holds to future clients' hold requests. Hence, from the service provider's point of view, maintaining a large number of holds for a long period without having actual transactions is not desirable since it will result in lower resource utilization, reducing the likelihood of successful transaction completion.

Motivated by this, in Section 2.1 we introduced the notion of hold duration that sets the time limit on the validity of an approved hold. With this finite hold duration, the service providers can control the number of outstanding holds to increase the chance of successful transactions while eliminating the possibility of long blocking and deadlock. However, from the client's viewpoint, spending a certain amount of time at <sup>hold</sup> state before initiating a <sup>prepare</sup> phase is unavoidable when multiple resources need to be acquired together. Consequently, there is a fundamental tradeoff in determining the hold duration: With a short hold duration, it is less likely that a client obtains holds of required resources before one of its active holds is expired. On the other hand, granting a long hold will negatively affect the service provider's resource utilization. Therefore, the proposed method for computing hold duration takes into account this trade-off, and seeks to adaptively determine the hold duration based on the local information available to individual service provider.

For the purpose of subsequent analysis, we consider a single service provider, $s _ { i } , \ i \in \{ 1 , \ . . . , \ m \}$ . In what follows, we will use the subscript i to denote the fact that the variable is defined for $s _ { i } .$ . We let the hold-to-prepare time $T _ { i } ^ { \mathrm { H P } }$ of $s _ { i }$ be the time between the approval of a hold for a client and the receipt of the <sup>prepare</sup> request from the same client. The starting point for the result proposed herein is the observation that $T _ { i } ^ { \mathrm { H P } }$ can be effectively modeled by use of a failure model in reliability theory [2]. We consider the multi-component parallel system model that consists of multiple identical components working in parallel in order to enhance the system reliability in spite of a component failure. In this model, the system is operational as long as one component is live, and the entire system fails only when all components have failed. That is, the time to failure of a multi-component parallel system is equal to the time taken until all the components in the system have failed.

Considering that the services providers in THP + 2PC manage the resources independently and their behaviors are identical, we see that the process of the entire system failure in the multi-component parallel model is the same as that of the successful acquisition of all the required holds from the corresponding service providers in THP +2PC. Accordingly, if we model the time taken to obtain a hold of one unit of resource as a lifetime of a single component of the multi-component parallel system, the total time required for a client to obtain all the necessary holds to be able to invoke the <sup>prepare</sup> method can then be represented as the time to failure of the entire multi-component parallel system. Under this interpretation, $T _ { i } ^ { \mathrm { H P } }$ can be understood as a random variable representing how much time is left until the entire system failure (i.e., the completion of acquisition of all necessary holds and the request for <sup>prepare</sup>), given that a component has just failed (i.e., a hold request has been just approved).

Time to failure is a well-studied subject that has been investigated extensively over the years in reliability community. In this paper, we adopt the Weibull distribution that has been widely used in literature. It is well known that it provides a nice flexibility to model various types of failure behaviors [2,8]. Specifically, we use the Weibull distribution for $\bar { T } _ { i } ^ { \mathrm { H P } }$ whose cumulative distribution function is given by

$$
F _ {i} (x) = \mathsf {P} \{T _ {i} ^ {\mathrm{HP}} \leq x \} = 1 - \exp (- \beta_ {i} x ^ {\alpha_ {i}})\tag{2}
$$

where $\alpha _ { i } \ ( > 0 )$ and $\beta _ { i } \ ( > 0 )$ are the parameters of the distribution.

A hold for a client can be either expired before the event that the request for <sup>prepare</sup> from the same client is received, or continued until that event, depending on the length of hold duration. In order to explain the basic idea, we assume that time is divided into discrete time epochs at which the service provider makes a decision on the hold duration. Under this assumption, the service provider has two alternatives on an active hold at every time period: to expire it now or continue it until the next epoch. For both cases, we compute the probability that the hold-to-prepare transition takes place within a certain length of time interval. Then, the hold duration will be the time point when the computed probability becomes higher by expiring the current active hold. We remark that this method is heuristical since it attempts to increase the chance of successful transactions near the decision point.

More specifically, suppose that a new hold has been granted at time 0 and it is not expired until time x. If the hold is expired at time x, this will increase the number of holds that can be issued by the service provider. However, this will not improve the chance of a successful transaction significantly if there are enough resources available to serve most of the future hold requests. In fact, comparing with the other option of extending the hold, expiring the hold at time x will be beneficial if the service provider becomes able to grant another new hold that would otherwise be rejected.

Fig. 3 shows one possible sequence of state transitions when an active hold is expired at time x. In order to compare this scenario with the other alternative choice that can be made by $s _ { i }$ at time x $( \mathrm { i . e . , }$ to continue the current active hold in consideration), we compute the criterion probability that a new hold-to-prepare transition takes place owing to the expiration of the current active hold. The total amount of time required for a client's resource acquisition to make a successful transition to the <sup>prepare</sup> state consists of two parts: the time required for a requested hold to be accepted, and the time for the same hold to enter the prepare state, $T _ { i } ^ { \mathrm { H P } }$ . Hence, the computation of the criterion probability mentioned above necessarily involves a convolution of the two distributions of time, which, however, is not amenable to exact analysis due to the distribution function, $F _ { i } ( x )$ in (2). As a result, we approximate the criterion probability with its lower bound, and denote it as $P _ { i } ^ { \mathrm { E } }$ which represents the probability that a new hold approved before time x + 1 makes a hold-to-prepare transition within the next time unit $( \mathrm { i } . \mathrm { e } . , x ^ { + } 2 )$ , given that one of the existing hold is expired at time x.

![](/api/attachments/4NQWW8HZ/fulltext/images/4119cec84bca95f19a30790ef8dad629df1914ef89b1d1a2f52dc0957561e410.jpg)  
Fig. 3. An example state transition of an active hold.

The probability that the expiration of an existing hold at x allows the provider to accept another hold request before $x + 1$ that would otherwise be rejected is equivalent to the probability that there exists at least one hold request rejected from $x \ \mathrm { t o } \ x { + 1 }$ . This rejection probability for $s _ { i } ,$ denoted by $\gamma _ { i } ,$ depends on how many hold requests are received and how many of them can be approved during the time period. It should be noted that service provider $s _ { i }$ can only approve $k _ { i } r _ { i } ( t ) - h _ { i } ( t )$ new hold requests at time t.

We further assume that clients' hold requests arrive to a service provider according to a Poisson process. The use of Poisson process is justified by the Palm-Khintchine theorem which states that the superposition of many independent renewal process forms, in limit, a Poisson process [10]. With this assumption, $\gamma _ { i }$ can be approximated by $\textstyle \sum _ { j = k _ { i } r _ { i } ( t ) - h _ { i } ( t ) + 1 } ^ { \infty } \mathrm { e } ^ { - \lambda _ { i } } \lambda _ { i } ^ { j } / j !$ where $\lambda _ { i }$ is <sup>¼ ð Þ- ð Þþ</sup>the average occurrence rate of hold requests for $s _ { i \cdot }$ Since the probability that a hold-to-prepare transition occurs within one time unit equal to $F _ { i } ( 1 )$ , the approximated criterion probability $P _ { i } ^ { \mathrm { E } }$ is given by

$$
P _ {i} ^ {\mathrm{E}} := \gamma_ {i} \rho_ {i}\tag{3}
$$

where $\rho _ { i } : = F _ { i } ( 1 ) { = } 1 - \mathrm { e } ^ { - \beta i }$ . We note that a high hold request rejection rate (i.e., large $\gamma _ { i } )$ and short hold-toprepare transition time (i.e., large $\rho _ { i } )$ will increase the probability $P _ { i } ^ { \mathrm { E } }$ , leading to a decision in favor of expiring the hold.

In contrast, when the service provider $s _ { i }$ decides to continue the hold at time $x ,$ another criterion probability, $P _ { i } ^ { \mathrm { C } }$ that the active hold at time x makes a transition to the <sup>prepare</sup> state by time $x + 2 ,$ can be represented by the conditional probability of $T _ { i } ^ { \mathrm { H P } }$ as follows.

$$
P _ {i} ^ {\mathrm{C}} (x) := \mathsf {P} \left\{T _ {i} ^ {\mathrm{HP}} \leq x + 2 \mid T _ {i} ^ {\mathrm{HP}} > x \right\}
$$

$$
= \frac {\mathsf {P} \{x <   T _ {i} ^ {\mathrm{HP}} \leq x + 2 \}}{\mathsf {P} \{T _ {i} ^ {\mathrm{HP}} > x \}} = \frac {F _ {i} (x + 2) - F _ {i} (x)}{1 - F _ {i} (x)}
$$

$$
= \frac {\exp \left(- \beta_ {i} x ^ {\alpha_ {i}}\right) - \exp \left(- \beta_ {i} (x + 2) ^ {\alpha_ {i}}\right)}{\exp \left(- \beta_ {i} x ^ {\alpha_ {i}}\right)}
$$

$$
= 1 - \exp (- \beta_ {i} [ (x + 2) ^ {\alpha_ {i}} - x ^ {\alpha_ {i}} ]).\tag{4}
$$

Two probability metrics, $P _ { i } ^ { \mathrm { E } }$ and $P _ { i } ^ { \mathrm { C } }$ , that respectively characterize the likelihood of the consequences of two alternative decisions (i.e., either expire or continue a current active hold) provide a basis for formulating a policy to adaptively compute the hold duration. From the definitions of $P _ { i } ^ { \mathrm { E } }$ and $P _ { i } ^ { \mathrm { C } }$ , it follows that expiring an existing hold makes a sense only if $P _ { i } ^ { \mathrm { E } }$ is greater than $P _ { i } ^ { \mathrm { C } }$ . In other words, as long as $\bar { P } _ { i } ^ { \mathrm { C } } ( x )$ is greater than or equal to $P _ { i } ^ { \mathrm { E } }$ at time $x ,$ it is more likely that an existing active hold rather than a new hold makes a transition to the <sup>prepare</sup> state, and accordingly it will not be worth expiring the existing active hold. Therefore, an optimal hold duration, denoted by $x ^ { * }$ , will be the largest x such that $P _ { i } ^ { \mathrm { C } } ( x )$ is greater than or equal to $P _ { i } ^ { \mathrm { E } }$ , and it will maximize the probability of the hold-to-prepare transitions to occur.

More specifically, let $x ^ { * }$ denote the time when $P _ { i } ^ { \mathrm { E } }$ and $P _ { i } ^ { \mathrm { C } } ( x )$ become equal. That is, $x ^ { * }$ is formally defined as

$$
x ^ {*} := \inf \left\{x \geq 0: P _ {i} ^ {\mathrm{C}} (x) \leq P _ {i} ^ {\mathrm{E}} \right\}.
$$

To compute $x ^ { * }$ , we consider two different cases depending on the value range of $\mathsf { \Omega } \mathsf { \Omega } \ast _ { i } .$ . From (4), it can be shown that $P _ { i } ^ { \mathrm { C } } ( x )$ is decreasing if and only if $\alpha _ { i } < 1$ . The left plot of Fig. 4 depicts the graphs of $\mathbf { \Theta } _ { { P } _ { i } ^ { \mathrm { { E } } } } ^ { \ }$ and $P _ { i } ^ { \mathrm { C } }$ with respect to $x ,$ which shows that $P _ { i } ^ { \mathrm { C } } ( x )$ decreases as x increases when $\alpha _ { i } < 1$ . This graph also suggests that the probability of one of the existing holds to make a holdto-prepare transition becomes smaller than that of a new hold request accepted by the service provider to make a transition to the <sup>prepare</sup> state, once the time exceeds the value $x ^ { * }$ . Consequently, in order to find $x ^ { * }$ that makes $P _ { i } ^ { \mathrm { E } }$ and $P _ { i } ^ { \mathrm { C } } ( x )$ equal, we need to solve the following equation:

$$
\gamma_ {i} \rho_ {i} = 1 - \exp (- \beta_ {i} [ (x + 2) ^ {\alpha_ {i}} - x ^ {\alpha_ {i}} ])
$$

which reduces to

$$
z _ {i} = (x + 2) ^ {\alpha_ {i}} - x ^ {\alpha_ {i}}\tag{5}
$$

where $z _ { i } : = \log ( 1 - \gamma _ { i } / \rho _ { i } ) / \log ( 1 - \rho _ { i } )$ . It follows that $0 \leq z _ { i } < 1$ , since $0 \leq \gamma _ { i } < 1$ and $0 \leq \rho _ { i } < 1$ . Furthermore, from the right plot of Fig. 4 which shows the curves of $( x + 2 ) ^ { \alpha i } - x ^ { \alpha i }$ and $z _ { i }$ when $\alpha _ { i } < 1$ , it can be seen that there is a unique solution $x ^ { * }$ to (5) in this case.

![](/api/attachments/4NQWW8HZ/fulltext/images/7d3e67596944b5a0672e167e066b80c6d85c2251887c42dbeb1c7e886c885ed1.jpg)  
Fig. 4. Computation of hold duration when $\alpha _ { i } < 1$

When $\alpha _ { i } \geq 1$ , however, the right-hand side of (5) is non-decreasing and the equation yields no solution. In this case, $P _ { i } ^ { \mathrm { E } }$ is smaller than $P _ { i } ^ { \bf C } ( x )$ for all $x \ge 0$ , and therefore it will be desirable to continue the current hold as long as possible. Thus, the hold duration is set to its maximum, denoted by $M _ { i } ,$ if $\alpha _ { i } \geq 1$ , where $M _ { i }$ is a predefined upper limit set by $s _ { i }$ on the allowable hold duration.

For the purpose of implementation, it is required to use the estimates for the parameters defined in (5). While there exist straightforward statistics that can be used as estimates for $\rho _ { i }$ and $\gamma _ { i }$ in (5), there is no corresponding statistic available to estimate $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega }$ directly from observed data. Hence, we use the squared coefficient of variation of $T _ { i } ^ { \mathrm { H P } } , c _ { i } ,$ that has one-to-one map with $T _ { i } ^ { \mathrm { H P } }$ as follows:

$$
c _ {i} := \frac {\operatorname{Var} \left[ T _ {i} ^ {\mathrm{HP}} \right]}{E \left[ T _ {i} ^ {\mathrm{HP}} \right] ^ {2}} = \frac {\Gamma (1 + 2 / \alpha_ {i})}{\Gamma (1 + 1 / \alpha_ {i}) ^ {2}} - 1
$$

where Γ denotes the gamma function [10]. From the definition, it follows that $\alpha _ { i } < 1$ if and only if $c _ { i } > 1$

Furthermore, based on the observation that (5) does not have a closed form solution, we use a numerical approximation to obtain an explicit expression for $x ^ { * }$ that satisfies (5). By solving Eq. (5) numerically for a variety of values of $c _ { i } > 1$ and $0 < z _ { i } < 1$ , and fitting the nonlinear relationship between the solutions and the parameters, we get the following regression equation:

$$
x ^ {*} \cong \frac {3 . 2 3}{(c _ {i} - 1) ^ {0 . 7 9} \cdot z _ {i} ^ {2 . 0 1}}.
$$

Based on the above results, we now present the computational method to determine hold duration in the THP+2PC protocol. Suppose that service provider, $s _ { i } ,$ $i { = } 1 , { \ldots } , m$ , has received a hold request from a client at time $t . \mathrm { I f } s _ { i }$ has an available hold to grant, it will accept the hold request, and assign the duration to the granted hold by use of the following statistics that are observed up to time t independently by $s _ { i } .$

$c _ { i } ( t ) \colon$ the squared coefficient of variation of $\tilde { T } _ { i } ^ { \mathrm { H P } }$ $\rho _ { i } ( t ) \colon$ the rate of occurrence that $\tilde { T } _ { i } ^ { \mathrm { H P } }$ is smaller than or equal to one time unit

$\lambda _ { i } ( t ) \colon$ the arrival rate of hold requests

$\gamma _ { i } ( t ) \colon$ the approximated probability that one or more hold requests are rejected during one time unit; that is, $\begin{array} { r } { \gamma _ { i } ( t ) \stackrel { - } { = } \sum _ { j = k _ { i } r _ { i } ( t ) - h _ { i } ( t ) + 1 } ^ { \infty } \mathrm { e } ^ { - \lambda _ { i } } \lambda _ { i } ^ { \bar { j } } / j ! } \end{array}$

$\theta _ { i } ( t ) \colon$ the rate of occurrence that an active hold makes transition to prepare state before it is expired.

We remark that we have used $\tilde { T } _ { i } ^ { \mathrm { H P } }$ instead of $T _ { i } ^ { \mathrm { H P } }$ in the above definitions to address the effect of $M _ { i \cdot } ~ \tilde { T } _ { i } ^ { \mathrm { H P } }$ represents a conditional random variable that considers only the hold-to-prepare transition instances that take less time than $M _ { i } .$ . With $\tilde { T } _ { i } ^ { \mathrm { H P } }$ , the probability of a hold-toprepare transition in (3) should now be estimated by

$$
\gamma_ {i} (t) \theta_ {i} (t) \rho_ {i} (t)
$$

Consequently, when $c _ { i } ( t ) > 1 ( \mathrm { i . e . , } \alpha _ { i } < 1 )$ the hold duration assigned by $s _ { i }$ at time t is computed as follows:

$$
d _ {i} (t) := \min \left\{\max \left\{1, \left\lfloor \frac {3 . 2 3}{[ c _ {i} (t) - 1 ] ^ {0 . 7 9} \times [ \tilde {z} _ {i} (t) ] ^ {2 . 0 1}} \right\rfloor \right\}, M _ {i} \right\}\tag{6}
$$

where $\tilde { z } _ { i } ( t ) : = \log ( 1 - \gamma _ { i } ( t ) \theta _ { i } ( t ) \rho _ { i } ( t ) ) / \log ( 1 - \rho _ { i } ( t ) ) .$

Finally, as noted above, when $c _ { i } ( t ) \leq 1 ~ ( \mathrm { i . e . , } ~ \alpha _ { i } \geq 1 ) .$

$$
d _ {i} (t) := M _ {i}\tag{7}
$$

Example. We illustrate how the proposed hold duration computation method works through a simple e-commerce scenario in which service providers expose their items to sell in the form of web services. Suppose that service provider $s _ { i }$ receives a hold request at time t and $\mathrm { T H P } + 2 \mathrm { P C }$ allows it to accept the request $( \mathrm { i . e . , } h _ { i } ( t ) { < } k _ { i } r _ { i }$ (t)). First, the service provider computes $c _ { i } ( t )$ . This statistic estimates the variance of hold-to-prepare state transition times based on the observations made up to time t. If $c _ { i } ( t ) \leq 1$ the maximum allowable hold duration, $M _ { i } ,$ is assigned to $d _ { i } ( t )$ . Note, however, that at the beginning the service provider receives a hold request before it observes the first hold-to-prepare state transition. For this reason, we propose that the service provider sets $d _ { i } ( t )$ to $M _ { i }$ when there are not enough observations to compute $c _ { i } ( t )$

On the other hand, when $c _ { i } ( t )$ is greater than one (say $c _ { i } ( t ) { = } 2 . 5$ for this example), the service provider computes the hold duration according to Eq. (6). The equation requires valuation of three statistics, $\gamma _ { i } ( t ) , \theta _ { i } ( t )$ and $\rho _ { i } ( t )$ , which can be computed as follows. First, suppose that the service provider has received hold request messages according to the rate of 4.5 messages per unit time $( \mathrm { i . e . , } \lambda _ { i } ( t ) { = } 4 . 5 )$ and the overhold size is 2 $( \mathrm { i } . \mathrm { e } . , k _ { i } { = } 2 )$ . Assuming that the service provider has four available items in stock at time $t \left( \mathrm { i . e . , } r _ { i } ( t ) \mathrm { = } 4 \right)$ and there are five active holds $( \mathrm { i . e . , } h _ { i } ( t ) { = } 5 )$ , γ (t) can be computed by $\begin{array} { r } { \gamma _ { i } ( t ) = \sum _ { j = k _ { i } r _ { i } ( t ) - h _ { i } ( t ) + 1 } ^ { \infty } \mathrm { e } ^ { - \lambda _ { i } ( t ) } \lambda _ { i } ( t ) ^ { j } / j ! = } \end{array}$ $\begin{array} { r } { \sum _ { j = 2 \times 4 - 5 + 1 } ^ { \infty } \mathrm { e } ^ { - 4 . 5 } ( 4 . 5 ) ^ { j } / j ! \approx 0 . 6 5 8 . \mathrm { S e c o n d } , \theta _ { i } ( t ) } \end{array}$ <sup>Þ ¼</sup>can be <sup>¼  - þ ð Þ</sup>obtained by taking the ratio of the number of hold-toprepare transitions to the number of hold requests received by time t. That is, if 500 out of 1000 hold requests granted by time t have made transitions to the <sup>prepare</sup> state before expiration, $\theta _ { i } ( t )$ becomes $5 0 0 / 1 0 0 0 { = } 0 . 5 .$ . Third, since $\rho _ { i } ( t )$ counts the number of hold-to-prepare state transitions that took place in less than one unit time, it follows that $\rho _ { i } ( t ) = 1 0 / 5 0 0 { = } 0 . 1 2$ , if there have been 60 such cases out of all 500 transitions observed by time t. Combining the above results, we obtain:

$$
\begin{array}{r l} \tilde {z} _ {i} (t) & = \frac {\log (1 - \gamma_ {i} (t) \theta_ {i} (t) \rho_ {i} (t))}{\log (1 - \rho_ {i} (t))} \\ & = \frac {\log (1 - 0 . 5 6 8 \times 0 . 5 \times 0 . 1 2)}{\log (1 - 0 . 1 2)} \approx 0. 2 7 3 \end{array}
$$

Finally, the service provider assigns the hold duration to the hold request according to Eq. (6) which evaluates to what follows, assuming that $M _ { i }$ is sufficiently large.

$$
d _ {i} (t) = \left\lfloor \frac {3 . 2 3}{(2 . 5 - 1) ^ {0 . 7 9} \times 0 . 2 7 3 ^ {2 . 0 1}} \right\rfloor = 2 5 \text {   time   units }
$$

We remark that $\tilde { z } _ { i } ( t )$ becomes 0 when $\scriptstyle \theta _ { i } ( t ) = 0 \mathrm { o r } \rho _ { i } ( t ) = 1$ In this case, additional attention is needed to avoid a division by zero error, and it is natural to set $d _ { i } ( t )$ to $M _ { i \cdot }$

## 3.2. Hold duration for infinite overhold case

The fundamental intuition underlying the derivation of the result in Section 1 is that unnecessarily long hold duration granted for a client will decrease the chance of other clients to successfully obtain holds. However, this is no longer true for the infinite overhold case in which a hold can be issued as long as there is an available resource unit. Indeed, the performance is rather independent of the length of hold duration in this case, and we prove this property formally in the following proposition.

Proposition 1. Consider the set of service providers, $s _ { l } ,$ $\ldots , s _ { m } ,$ that grant finite length holds according to $T H P +$ $2 P C$ protocol. Assuming that clients interact with the providers via THP+2PC, and that there is no message delay between them, the length of hold duration does not affect the waiting time of clients if ${ \mathrm {  ~ \bar { \kappa } ~ } } _ { i } = \infty , \ \forall i = I , \ . . . , m .$

Proof. Let $c _ { j }$ be a client that has valid holds at time t from the set of service providers $Q _ { j }$ such that $Q _ { j } \subset R _ { j }$ and $Q _ { j } \neq R _ { j }$ . Without loss of generality, we assume that $c _ { j }$ has obtained a hold from a service provider $s _ { i } \in R _ { j }$ at time $t ^ { \prime } ( < t ) ,$ , and further suppose that $c _ { j }$ requests holds to the service providers defined by $R _ { j } \backslash$ $Q _ { j }$ at t. We consider two different hold duration policies of $s _ { i } \dot { . }$ the first policy has expired the hold for $c _ { j }$ before t, and the second policy will not expire the hold until t. Hence, under the first policy, $s _ { i } \notin { Q _ { j } }$ while $s _ { i } { \in } Q _ { j }$ in the second policy.

Since there is no message delay, the fact that $s _ { i } { \in } Q _ { j }$ under the second policy implies that $s _ { i }$ has an available resource at t. As a result, even with the first policy, $c _ { i }$ is able to obtain a hold from $s _ { i }$ at t due to the definition of $\mathrm { T H P } + 2 \mathrm { P C }$ protocol with infinite overhold size. Therefore, the length of hold duration does not change the chance that $c _ { j }$ can obtain a hold from $s _ { i } .$ □

Therefore, for the business applications whose running time is long enough compared to message delay, Proposition 1 provides a background to effectively establish the optimal policy for computing hold duration when all service providers implement the infinite overhold strategy.

## 4. Experimental results

Simulation analysis results are given in this section to demonstrate the performance of the THP + 2PC protocol with the proposed adaptive policy for computing hold durations. We consider an experimentation scenario in which e-tailers sell the commodity products through the web services. Clients purchase the products from multiple e-tailers to make assembled products, and seek to purchase these items as a single atomic transaction. E-tailers, on the other hand, are assumed to start their business with some initial stock, and replenish the products whenever sale is made. We also consider a time delay required for the product replenishment. Since each e-tailer wants to maximize its inventory turnover rate, we consider the objective to minimize the time required for clients to complete their entire transactions (i.e. successful acquisition of all the required products as a bundle). Both clients and service providers follow the THP+ 2PC protocol.

The simulation results for three different cases are presented in this section, and in each case, we compare the proposed method for computing hold duration with the fixed-term policies that assign the same length of hold duration to all the holds granted. Each case considers the different configuration in terms of the number of independent providers, the initial stock size, and the replenishment times. For the experimentation, we use minute as a basic time unit, and the uniform distribution with two parameters is used to randomly generate the replenishment time for each provider.

Clients are dynamically created during the simulation run, and the exponential distribution with mean 10 min is used to simulate the inter-arrival times of clients throughout the three cases. Upon creation, each client is assigned with a random value that represents the number of products it needs to purchase as a bundle. For this purpose, we use the binomial distribution defined by m identical trials with some pre-specified success probability π, where m denotes the number of independent providers. For example, using the binomial distribution with parameters $m = 2 0$ and $\pi { = } 0 . 1$ will lead to the bundle of size 2 for the clients on the average.

From the definition of Fig. 2, each client needs to perform backoff whenever an attempt for obtaining holds or entering to prepare phase is not successful. In this experimentation, we have used a simple constant backoff policy in which a client makes retrials on every time unit (i.e. minute). Finally, the simulation was performed for 3000 client arrivals for each case, and the message delivery delay is simulated by use of the uniform distribution of 10 and 200 ms.

For each case, we first consider the situations when the overhold size is finite, and experimentally compare the performance of the proposed hold duration computation method (to be called as adaptive policy) with the fixed-term policies by examining the effect of varying π which indicates the level of resource contention of the simulated system. The fixed-term policies considered in the experimentation are denoted by 1-delta, 10-delta, and 100-delta which assign the hold duration of lengths, 1, 10, and 100 time units, respectively. We use the average number of retrials made by clients as a performance measure, which, in this considered scenario, is directly proportional to the average waiting time incurred to the clients. For instance, if the number of retrials of a client is 20, it is fair to say that the client has waited approximately for 20 min, considering that the message delivery delays are relatively very small.

![](/api/attachments/4NQWW8HZ/fulltext/images/fbef9b9f4e62caf9b4fd4dcabb6d44a96df4a965143497439dc30994ce0651c0.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/e259c37f9f88cb2c2b97da552bf24afb1cd60a66ca999bbbbb3b91bf542c70ac.jpg)

The plots in Figs. 5–7 show the average performance comparison results when the overhold size varies under the different configurations. The overhold size employed by each service provider, $k _ { i } , i { = } 1 , . . . , m .$ , for each simulation run was set to be equal across the providers, and it is denoted as k in Figs. 5–7. There are four plots in one figure, and each plot contains the performance results of THP + 2PC under the same overhold size when four different hold duration computation methods are used by the service providers.

![](/api/attachments/4NQWW8HZ/fulltext/images/73ef977980450519e47f4c735ef4c3241ac676e83d775ad545f4498e0ffb351b.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/a1c47a4430a78eb8938c67a1b1eb5d21140be875d6e5474be3dda3049164a822.jpg)  
Fig. 5. Performance comparison results when the number of independent providers is 20, the initial stock size is 5, and the replenishment time distribution parameters are 50 and 250.

![](/api/attachments/4NQWW8HZ/fulltext/images/5475f32390eceb656080bf1a3d59f682439d74fc7a7f4c55da80daed28742270.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/77b7e59e69a8a4bc92ed0f73509ab1d567ca51542d1247401365d54e89f76346.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/8b16ffa80968be67ee4516d701380bba2d1e17330d56d1c585d0b1c4bc39b6c2.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/8f6190e8ca0e214d18f18f36be46c1c5f2048c63a4759a4c1996df025f85376c.jpg)  
Fig. 6. Performance comparison results when the number of independent providers is 5, the initial stock size is 7, and the replenishment time distribution parameters are 100 and 250.

![](/api/attachments/4NQWW8HZ/fulltext/images/cb3c9a2c53cda4b81a1cee31cdaf64d58591e083f335e93f03927b2b7287f86b.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/7235684d0dcaa5f17cc7d18ba5fabb7f3aa12ac5cee0f9311806e243d5789b83.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/4860a1e467e646a680969a0671eca68f1aca25d618f3717ff31cc647e3672342.jpg)

![](/api/attachments/4NQWW8HZ/fulltext/images/425df81c15bbffac479ae2b0ff05014f63fc51ad9ecdfb86deff26828012d080.jpg)  
Fig. 7. Performance comparison results when the number of independent providers is 20, the initial stock size is 20, and the replenishment time distribution parameters are 350 and 500.

For instance, the top left plot of Fig. 5 represents the case in which (i) the overhold size is equal to 1 for all service providers, (ii) the number of independent providers (i.e., m) is 20, (iii) the initial stock size is 5, (iv) the replenishment time follows the uniform distribution with parameters of 50 and 250, and finally (v) four methods, namely 1-delta, 10-delta, 100-delta, and the proposed adaptive policy are employed by the service providers.

The comparison of the plots when the overhold size is finite indicates that performance differences are significant across the different hold duration computing methods. In particular, the proposed adaptive policy achieves a significant improvement over the other fixed-term policies as the probability π becomes larger, which indicates the increased competition for the resources. For example, from the top left plot of Fig. 6, we see that the clients need to make almost 400 retrials on the average under π = 0.15 in order to acquire necessary resources as a single atomic transaction when the service providers employ the 100-delta policy. However, when the proposed adaptive policy is used, only about 100 retrials are required for the clients on the average for the same case. As a result, it can be observed that, through the adaptive computation of hold durations, the service providers are able to manage their resources more efficiently, resulting in the reduced number of retrials for the clients to perform successful transactions.

From the plots for the finite overhold cases, it is also interesting to note that the performance of the fixed-term policies blows up more quickly than the proposed adaptive policy as π increases. This suggests that the adaptive policy is more robust to the increases in the resource contention as well as in the number of clients. Furthermore, it can be seen that better performance can be achieved by increasing the size of overhold. For instance, in Fig. 7, the average number of retrials required for clients under the adaptive policy when k = 1 is about 100 at π = 0.340 whereas it is decreased to less than 60 when k=1.5.

This performance improvement can be attributed to the result of reduced blocking and livelock during the hold acquisition process when the service providers increase the overhold size. Nevertheless, the higher value of overhold size will incur more frequent unexpected hold expirations to clients, leading to less satisfactory quality of services. Therefore, the actual determination of the overhold size should not be solely based on the performance concern. Finally, Figs. 5–7 confirm that the performance difference between policies becomes negligible when the service providers adopt the infinite overhold policy as shown in Proposition 1.

## 5. Conclusion

The recent advent of web services has opened up the possibility of automating multi-business transactions that span across the organizational boundaries. While there are several specific protocols that have been discussed to address the problem of coordinating web service enabled business transactions, this paper considered the tentative hold protocol that allows the placement of tentative holds on business resources prior to actual transactions in an attempt to provide increased flexibility in coordination.

We proposed a framework for efficiently applying the THP in conjunction with 2PC (named THP+2PC) to the problem in which service providers independently manage and expose their resources through web services and clients seek to acquire the resources from multiple providers as a single atomic transaction. In particular, by refining THP through the notion of overhold size and hold duration, our approach provides an effective framework to facilitate optimizing the performance of THP+2PC when it is used for automated coordination of multi-business transactions.

Furthermore, the problem of determining hold duration for the cases of finite and infinite overhold size was considered separately, and detailed analysis to obtain efficient hold duration was carried out. More specifically, with the objective of minimizing the average waiting time until clients complete their atomic multi-transactions, an adaptive scheme to compute the hold duration was proposed for the finite overhold case. For the infinite overhold case, we showed that the performance is indifferent to specific hold duration decision. Finally, simulation results confirmed that the proposed approach performs significantly better than the other possible nonadaptive schemes considered.

Future research work will concentrate on examining the effects of other various resource usage patterns on the performance of the proposed framework. In addition, we plan to extend the proposed scheme to more complex situations in which clients as well as service providers are subject to failure. Addressing these issues promises to be an interesting area for future research.

## Acknowledgements

This work was supported by the Korea Research Foundation Grant (KRF-2004-003-D00482).

## References

[1] P.A. Bernstein, E. Newcomer, Principles of Transaction Processing, Morgan Kaufmann, 1997.

[2] R. Billinton, R.N. Allan, Reliability Evaluation of Engineering Systems: Concepts and Techniques, 2nd edition, Plenum Press, 1992.

[3] M.B. Blake, H. Gomaa, Agent-oriented compositional approaches to services-based cross-organizational workflow, Decision Support Systems 40 (2005) 31–50.

[4] F. Cabrera, G. Copeland, B. Cox, T. Freund, J. Klein, T. Storey, S. Thatte. Web services transaction (WS-transaction). http://www. ibm.com/developerworks/library/ws-transpec/, August 2002.

[5] F. Casati, M.-C. Shan, Dynamic and adaptive composition of eservices, Information Systems 26 (2001) 143–163.

[6] S. Dalal, S. Temel, M. Little, M. Potts, J. Webber, Coordinating business transactions on the web, IEEE Internet Computing (2003 (January/February)) 30–39.

[7] S. Frølund, K. Govindarajan, Transactional Conversations. W3C Workshop on Web Services, 2001.

[8] B. Gertsbakh, Statistical Reliability Theory, Marcel Dekker Inc., 1989.

[9] M. Hansen, S. Madnick, M. Siegel, Process aggregation using web services, in: Proceedings of the Workshop on Web Services, e-Business, and the Semantic Web (WES), 2002.

[10] D.P. Heyman, J. Sobel, Stochastic Models in Operations Research, McGraw-Hill, 1982.

[11] J.B. Kim, A. Segev, A web services-enabled marketplace architecture for negotiation process management, Decision Support Systems 40 (2005) 71–87.

[12] B. Limthanmaphon, Y. Zhang, Web service composition transaction management, in: Proceedings of the 15th Australasian Database Conference (ADC), 2004.

[13] M. Littlel, Transactions and web services, Communications of the ACM 46 (10) (2003 (October)) 49–54.

[14] N. Milanovic, M. Malek, Current solutions for web service composition, IEEE Internet Computing 8 (6) (2004) 51–59.

[15] OASIS (Organization for the Advancement of Structured Information Systems). Business transaction protocol primer, version 1.0. http://www.oasis-open.org/, June 2002.

[16] OASIS (Organization for the Advancement of Structured Information Systems). Business transaction protocol: An OASIS committee specification, version 1.0. http://www.oasisopen.org/, June 2002.

[17] M.P. Papazoglou, Web services and business transactions, World Wide Web: Internet and Web Information Systems 6 (1) (2003) 49–91.

[18] J. Park, T. Yang. A protocol for fast co-allocation of shared web services, in: Proceedings of the 4th International Workshop on

Technologies for E-Services, volume 2819 of Lecture Notes in Computer Science, pp. 191–202, 2003.

[19] J. Roberts, K. Srinivasan. Tentative hold protocol part 1: White paper. http://www.w3.org/TR/tenthold-1/, 2001.

[20] J.Y. Sayah, L.-J. Zhang, On-demand business collaboration enablement with web services, Decision Support Systems 40 (2005) 107–127.

[21] M.P. Singh, M.N. Huhns, Service-Oriented Computing: Semantics, Processes, Agents, John Wiley & Sons, 2005.

[22] K. Srinivasan, P.G. Malu, G. Moakley, Automatic multibusiness transactions, IEEE Internet Computing 7 (3) (2003) 66–73.

[23] J. Wang, Timed Petri Nets, Kluwer Academic Publishers, 1998.

[24] M.C. Zhou, K. Venkatesh, Modeling, Simulation, and Control of Flexible Manufacturing Systems: A Petri Net Approach, World Scientific, 1999.

![](/api/attachments/4NQWW8HZ/fulltext/images/2b22c6105b514b8579523a84623d117a8cb0d94c6a963c63a6ca1c17f366e23a.jpg)

Jonghun Park received B.S. and M.S. degrees in industrial engineering from Seoul National University (SNU), Seoul, Korea, in 1990 and 1992, respectively, and Ph.D. degree in industrial and systems engineering with a minor in computer science from Georgia Institute of Technology, Atlanta, GA, in 2000. He is currently an Assistant Professor at Department of Industrial Engineering of SNU. Before joining SNU, he was with School of Information Sciences and

Technology at Pennsylvania State University, University Park, PA, and with Department of Industrial Engineering at KAIST, Daejeon, Korea, both as an Assistant Professor. His research interests include Internet services, entertainment computing, and mobile services.

![](/api/attachments/4NQWW8HZ/fulltext/images/538b8b3554b09e75d804d59d19999ca663514de9306bd8ac77c96e2974e95cb1.jpg)

Ki-Seok Choi received B.S. and M.S. degrees in industrial engineering, respectively from Seoul National University, Seoul, Korea, in 1991, and from KAIST, Daejeon, Korea, in 1993, and Ph.D. degree in industrial and systems engineering from Georgia Institute of Technology, Atlanta, GA, in 2003. He is currently an Assistant Professor at Department of Industrial Information and Systems Engineering, Hankuk University of

Foreign Studies, Korea. Previously he worked at Electronics and Telecommunication Research Institute and Samsung Data Systems. His research interests are in telecommunication networks and quality of services.
