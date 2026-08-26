---
otero_id: 15678
otero_key: "SP4AWKN9"
title: "Capacity Provision Networks: Foundations of Markets for Sharable Resources in Distributed Computational Economies"
authors: "Anna Ye Du; Xianjun Geng; Ram Gopal; R. Ramesh; Andrew B. Whinston"
year: "2008"
journal: "Information Systems Research"
doi: "10.1287/isre.1070.0145"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/SP4AWKN9/fulltext/images/d172fbbdafb11b4022c612ca615a4b293614e01894f0ed7813454373220a574a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Capacity Provision Networks: Foundations of Markets for Sharable Resources in Distributed Computational Economies

Anna Ye Du, Xianjun Geng, Ram Gopal, R. Ramesh, Andrew B. Whinston,

To cite this article:

Anna Ye Du, Xianjun Geng, Ram Gopal, R. Ramesh, Andrew B. Whinston, (2008) Capacity Provision Networks: Foundations of Markets for Sharable Resources in Distributed Computational Economies. Information Systems Research 19(2):144-160. http:// dx.doi.org/10.1287/isre.1070.0145

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2008, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/SP4AWKN9/fulltext/images/8623534a1499c49a6e09437eea1eab167f0ed99ce82e2b71072ffe45ce2c7319.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Capacity Provision Networks: Foundations of Markets for Sharable Resources in Distributed Computational Economies

Anna Ye Du

Department of Management Science and Systems, SUNY at Buffalo, Buffalo, New York 14260, yedu@buffalo.edu

Xianjun Geng

Department of Information Systems and Operations Management, University of Washington, Seattle, Washington 98195, gengxj@u.washington.edu

Ram Gopal

Department of Operations and Information Management, University of Connecticut, Storrs, Connecticut 06269, ram.gopal@business.uconn.edu

R. Ramesh

Department of Management Science and Systems, SUNY at Buffalo, Buffalo, New York 14260, rramesh@buffalo.edu

Andrew B. Whinston

Department of Management Science and Information Risk, and Operations Management, University of Texas at Austin, Austin, Texas 78712, abw@uts.cc.utexas.edu

W<sup>ith</sup> <sup>the</sup> <sup>rapid</sup> <sup>growth</sup> <sup>of</sup> <sup>rich-media</sup> <sup>content</sup> <sup>over</sup> <sup>the</sup> <sup>Internet,</sup> <sup>content</sup> <sup>and</sup> <sup>service</sup> <sup>providers</sup> <sup>(SP)</sup> <sup>are</sup> increasingly facing the problem of managing their service resources cost-effectively while ensuring a high quality of service (QoS) delivery at the same time. In this research we conceptualize and model an Internetbased storage provisioning network for rich-media content delivery. This is modeled as a capacity provision network (CPN) where participants possess service infrastructures and leverage their topographies to effectively serve specific customer segments. A CPN is a network of SPs coordinated through an allocation hub. We first develop the notion of discounted QoS capabilities of storage resources. We then investigate the stability of the discount factors over time and the network topography using a test-bed on the Internet through a longitudinal empirical study. Finally, we develop a market maker mechanism for optimal multilateral allocation and surplus sharing in a network. The proposed CPN is closely tied to two fundamental properties of Internet service technology: positive network externality among cooperating SPs and the property of effective multiplication o capacity allocation among several distributed service sites. We show that there exist significant incentives for SPs to engage in cooperative allocation and surplus sharing. We further demonstrate that intermediation can enhance the allocation effectiveness and that the opportunity to allocation and surplus sharing can play an important role in infrastructure planning. In conclusion, this study demonstrates the practical business viability of a cooperative CPN market.

Key words: capacity provision networks; resource sharing; online market; distributed computation; quality of service

History: Sumit Sarkar, Senior Editor; Giri Kumar Tayi, Associate Editor. This paper was received on February 10, 2006, and was with the authors 7 months for 3 revisions.

## 1. Context and Motivation

Computational environments such as grids (Foster and Kesselman 1997), peer-to-peer systems (Oram 2001), and a host of service networks such as content delivery networks (Rabinovich and Spatschek 2002)

and internet storage infrastructures (HTRC 2005) have emerged as flexible computing infrastructures that adaptively share distributed resources. The objective of flexible infrastructures is to leverage the topography of distributed resources to attain desired levels of performance within resource and cost constraints (Foster et al. 2000). This leads to the notion of distributed computational economies (Waldspurger et al. 1992) built on such flexible infrastructures where resources can be traded, cooperatively shared, and accessed through coordination mechanisms (Buyya 2002). This is an evolution from high-end computing to decentralized service architectures where economic market mechanisms drive the trading of resources and services among globally distributed service providers (SP) in collectively servicing underlying market needs (Ferguson et al. 1996). A detailed survey of related works in this area is provided in Online Supplement I at the Information Systems Research website at http://isr.pubs.informs.org/ecompanion.html.

In this research we conceptualize and model a network of Internet storage infrastructures such as storage area networks (SAN) and network attached storage (NAS) (Preston 2002) as a distributed computational economy and term it capacity provision networks (CPN). Corporations are increasingly outsourcing their storage services to extend the reach and scalability of their operations and to ensure cost-effective levels of quality of service (QoS). A storage infrastructure provider essentially provides warehousing services for their clients, besides a global file system, geographical mirroring, and global load balancing, so that its services are more aligned with the Internet with Internet-level scalability. Furthermore, corporate spending on storage infrastructure is expected to rapidly grow and soon exceed \$3.5 billion (HTRC 2005). The proposed CPN model is motivated by the growing market externalities for storage services, increasing vertical integration among Internet storage infrastructure (ISI) consumers, and the consequential horizontal alignments among the service providers.

## 2. Capacity Provision Networks

Although the concept of a CPN is broad-based (Geng et al. 2003), we define a CPN in our current context as follows: a CPN is a network of nodes representing storage services that are interconnected via the Internet. A storage service comprises a data warehouse with the associated set of servers. Each CPN node is owned and operated by a service provider that services its clients from its CPN node. Although the types of services could be numerous, we focus on a specific type as follows. Consider a CPN comprising four nodes as shown in Figure 1.

Figure 1 CPN Structure  
![](/api/attachments/SP4AWKN9/fulltext/images/a7761cc0881d9339761e92b8f09773a0e65833cb417d7f41b0e8e7b7fcf2dd6b.jpg)

Consider SP-A, whose CPN node is located at Austin. Let SP-A contract with a client headquartered at Seattle with regional offices in the Midwest and Northeast to service the regional offices through its Austin node. The service entails the storage of some of the corporate data at the Austin node, providing analyses and answering queries from the regional client offices. This could involve both partitioning and replication of corporate data (Rabinovich and Spatschek 2002) between the Seattle and Austin nodes. The analyses and queries could require the use of local Austin data, collection of additional data from Seattle, consolidation, and reporting. This contract would require SP-A to set aside a certain portion of its storage and computing resources at its CPN node exclusively for this client. However, note that the capacity at the Austin node is limited and SP-A could have other clients for whom capacity needs to be allocated as well. Furthermore, the demand for services could vary over time. As a result, capacity allocation and utilization should be dynamically adjusted to make the best use of the available resources.

Now consider another service provider, SP-B, operating from Buffalo who is also faced with a similar situation. The two service providers could agree to a resource pooling strategy to protect them respectively against demand surges as follows. Assume that the two providers contract over a given period of time under the following terms. Let the demand over the period at each node be observable at its beginning. Therefore, the nature of demand variations would determine the length of each period. Given the initial capacity allocations at each node, if one of them has an excess over its demand and the other has a shortfall, then the excess node would provide its surplus capacity to the other for a certain cost. If both have surpluses or shortfalls, then no trade is needed. For example, in a scenario where SP-A has a shortfall and SP-B has a surplus in a given period, SP-A would avail the services of SP-B by partitioning some of its data and services to be stored at SP-B. The keys to such cooperative resource pooling are flexible resources, topographical leverage, and market enablers.

Flexible storage and computing resources yield improved quality of distributed content services through partitioning and replication. In this regard, a CPN implementation follows the same principles underlying the content delivery networks. By positioning content partitions and replicas optimally over the edges of the Internet, many latencies in content delivery can be avoided (Rabinovich and Spatschek 2002). Examples of such configurations are Akamai (Dilley et al. 2002), Kontiki (Junginger and Lee 2002), Radar (Rabinovich and Aggarwal 1999), SPREAD (Rodriguez and Sibal 2000), and Globule (Pierre and Steen 2001, 2003). Rabinovich and Spatschek (2002) described a set of approaches for designing content delivery networks by structuring them into components. The components are dynamically assembled and delivered from multiple servers when they are requested through technologies like Edge Side Includes (http://www.esi.org/index.html). The issue of component placement among multiple server farms is well studied under replica server placement (Li et al. 1999, Qiu et al. 2001, Radoslavov et al. 2001) and replica content placement (Gao et al. 2005; Rabinovich and Aggarwal 1999; Rodriguez and Sibal 2000; Chen et al. 2002a, b, 2003; Kangasharju et al. 2001). The dynamic distribution and updates of the components and their timing are commonly known as adaptation triggering. Adaptation triggers can be classified based on time and source of adaptation. On the time dimension, they are known as periodic, aperiodic, and hybrid triggers (Rabinovich and Aggarwal 1999, Pierre and Steen 2001). On the source dimension, they can be classified into servertriggered (Rabinovich and Aggarwal 1999, Pierre and Steen 2001), client-triggered (Sayal et al. 2003), and router-triggered (Rodriguez and Sibal 2000) adaptation.

Topographical leverage is obtained from the strategic positioning of an SP in an information supply chain; resource trades with others arise as a consequence. An SP derives this leverage from (a) a geographic advantage in service operations that others may not have, leading to enhanced QoS levels, and (b) the possession of necessary infrastructural/ architectural capabilities to provide the service. We illustrate this concept using a multimedia streaming example as follows. Audio/video online streaming with low latencies and jitters is a major challenge for service providers. This requires significant server bandwidth and storage capacities. Variability in customer demand and the returns on investments render these investments risky. Therefore, topographical leveraging through cooperative multimedia caching is a viable option for many service providers. In a typical application, streaming starts from the origin server, followed by compression and encryption at a streaming server and final delivery to the client through a front-end edge server. The client media player performs the decompression, decryption, and synchronization of audio and video components. Ramanna et al. (2006) provide a comprehensive survey of such streaming techniques. Now, consider the following scenario. If SPs A and B have a resource sharing contract with a peering connection between their respective front-end servers, then, some of the customers of A would be routed to front end server of B if (a) the streaming server of A is overloaded and cannot accept any further persistent connections or (b) the streaming content that a customer requests is not available at A but is available at B. This provides a better quality of service to the customer because the content is streamed through the peering connection, greater scale because more customers could simultaneously avail the streaming services, better load balancing, and increased customer reach. Consequently, a scenario where a customer of A is serviced by the streaming server of B while at the same time a customer of B is serviced by A is clearly possible from the resource sharing agreement. In both content distribution and multimedia streaming applications, it is important that a service provider knows the quantity and type of content to be shared with a trading partner. The above discussion on these applications shows how this can be accomplished.

A CPN represents a market economy with decentralized ownership of resources. Consequently, a market enabler in the form of a trading hub is central to its initial realization. In this regard, the CPN hub is similar to the notion of registries in web services. A CPN hub can be viewed as a market enabler where all capacity trades are initially carried out prior to their implementation. The hub is both a marketplace and a registry of participating service providers. A participant could either buy or sell capacity or even serve as an intermediary in a trade. An intermediary could be one who sells some of its own resources while also buying from others to meet its own demands. The topographical leverage would be principal to such trades.

In the CPN market, each unit of storage capacity is a two-attribute good: its value is determined by its price and its location on the Internet. The value of a CPN comes from the fact that Internet storage, as a technology, is characterized by positive network externality among storage sites: given the uncertainty in content demand, storage sites can better fulfill the demand collectively rather than separately. A CPN provides service providers not only a marketplace to trade, but also an incentive system for them to cooperate. While issues considered in classical mechanism design research in economics are not industry specific, the ones involved in CPN design are different: our proposed design of the CPN market is closely tied to the characteristics of Internet storage technologies, namely, positive network externality and sharability among geographically separated storage sites.

In this paper we first model the CPN as a financial market with a hub that provides both market coordination and operational support needed for the trades. We expect several innovative business models for Internet markets to originate from this concept. Second, we develop the service level leverages that drive the potential trades. Third, we study the characteristics of the leverage factors using a test-bed on the Internet through a longitudinal empirical study. The

CPN illustrated in Figure 1 has been implemented as a data distribution network and used in this study. Fourth, we develop the economic foundations of the CPN and a market maker mechanism for trade coordination and surplus generation using a cooperative capacity sharing principle. Fifth, we develop a surplus sharing strategy using Shapley values. We develop the structural properties of the surplus sharing strategy and a sequential permutation sharing algorithm that asymptotically converges to the Shapley values. Finally, we present detailed simulations with the CPN architecture.

The organization of this paper is as follows. Section 3 develops a topographical framework for service provisioning and the foundations of the capacity discounting concept. Section 4 develops the concepts of topographical leverage and arbitrage in a CPN and presents the longitudinal study with discount factors and the significant empirical conclusions. Section 5 presents the cooperative capacity sharing principle, and §6 develops the surplus sharing strategy. Section 7 presents the simulation experiments with results, and the conclusions are provided in §8.

## 3. A Topographical Framework for Service Provisioning

In this section we develop a framework of analysis of the CPN. We first consider the topography of the service resources of SPs and determine the areas where the topography can be effectively leveraged to deliver a required QoS to customers. Second, we model the service-level agreements (SLA) between an SP and its customers and capacity-trading agreements among SPs in a CPN in a given time horizon. Using these models, we derive results on the efficiency of the CPN market and the incentives among CPN participants to cooperate. A detailed illustrative example is provided in Online Supplement II at the Information Systems Research website at http://isr. pubs.informs.org/ecompanion.html.

## 3.1. Service Topography

We consider a set of SPs whose service infrastructures are networked, either through peering lines or via a public network like the Internet. Each SP represents the first point of access to capacity services for local clientele in its respective market and is represented by a CPN node. A client receives all the content from the network through the local service provider. Each SP establishes an SLA with a corporation or any content provider. In the case of an SLA with a business, the SP provides a remote capacity service within the environment of a distributed data warehouse maintained by the business. Such service is common among application service providers (ASP) such as Citrix Systems, USi, and Storage Alliance where the master data set is held at the business headquarters and replications/ partitions of the data sets are stored at the SP sites for faster access at remote sites. In the case of an SLA with content providers, a CDN-type arrangement usually exists, where copies of original content are stored in edge server farms maintained by the SP. In either case, when a user requests some data, it is served from a local edge server if it is available; otherwise, the data are retrieved from the master set at the origin server. If some of the requested data is locally available, then only the missing data are retrieved from the origin server. We assume that the Internet is the medium for all of these transactions and that all of the necessary applications are hosted at an edge server farm denoted by the corresponding CPN node.

We measure the QoS from an SP site by average delay, t, that users experience. This delay includes the network delay for the $\mathrm { S P }$ to acquire content from the source node, the $\mathrm { S P ^ { \prime } s }$ local processing time, and the time to deliver the content to the user through the local network. Local networks typically have high bandwidth and do not face congestion problems. Consequently the delays over the local network are minimal and are independent of the user location within the local network. To illustrate service topology, suppose that users need access to a total amount - of content. Furthermore, suppose that the SP services an amount $\Omega _ { c } \leq \Omega$ of the requested content locally, which can be accessed at average delay of $t _ { c }$ that consists only of local processing and delivery time. The remaining content needs to be accessed from the origin via the Internet, and let the average access delay be $t _ { 0 } .$ . By definition, $t _ { 0 } > t _ { c } ,$ because $t _ { 0 }$ must also include the additional network delay. For simplicity, assume that the content is organized into a collection of data units where each unit is individually serviced and managed and that each unit has the same probability of access by the users. Then, the users will experience an average delay of $t _ { 1 } =$ $( \Omega _ { c } / \Omega ) t _ { c } + ( ( \Omega - \Omega _ { c } ) / \Omega ) t _ { 0 }$ where $\Omega _ { c } \leq \Omega$ . Therefore, the average end-user delay, $t _ { 1 } ,$ is a nonincreasing function of $\Omega _ { c } .$ . To lower the access delay experienced by the users when $\Omega _ { c } < \Omega$ the SP has two options: (a) to provide additional service capacity locally or (b) to obtain the needed additional service capacity from another nearby SP. The viability of the second option depends on the cooperation agreement between the SPs and their relative proximity. The proximity between the SPs dictates the benefits of mutual trade as it results in the reduced performance problem: given a certain amount of local service capacity and same amount of remote service capacity, an SP would always prefer the local capacity because the performance of any remote capacity can be negatively affected by the delay between the two SPs. The farther the remote service, the more likely that retrieving data from it could be delayed. This leads to the notion of discounted remote capacity, which is developed below.

## 3.2. Inter-SP Trades and Discounted Remote Capacity

Consider a different SP who can provide $\Omega _ { r }$ units of content with an average access delay of $t _ { r }$ to the SP discussed above. Call this new provider the remote SP. Then, by definition, $t _ { r } > t _ { c } ,$ because $t _ { r }$ covers the network delay from the remote SP. In this context, “local” and “remote” refer to the topographical rather than geographical distance. Furthermore, it should also be true that $t _ { r } < t _ { 0 } ;$ otherwise, this remote service is of no value. By employing the services of the remote SP, the average delay time is $( \Omega _ { c } / \Omega ) t _ { c } + ( \Omega _ { r } / \Omega ) t _ { r }$ + $( ( \boldsymbol { \Omega } - \boldsymbol { \Omega } _ { c } - \boldsymbol { \Omega } _ { r } ) / \boldsymbol { \Omega } ) t _ { 0 } .$ , which is lower than $t _ { 1 } .$ . Although an SP can lower the access delays for its consumers by availing of content services from another SP, the remote capacity is discounted as follows. Consider $t _ { 1 }$ as before and set $t _ { 1 } = ( ( \Omega _ { c } - S _ { c } ) / \Omega ) t _ { c } + ( S _ { r } / \Omega ) t _ { r } +$ $( ( \Omega - ( \Omega _ { c } - S _ { c } ) - S _ { r } ) / \Omega ) t _ { 0 }$ to denote the same average delay experienced when both local and remote contents are used. In the latter expression, the local SP compensates for allocation of $S _ { c }$ unit of local capacity to service content from its own site with allocation of $S _ { r }$ units of servicing capacity from the remote SP. From the two expressions, we have $S _ { c } = ( ( t _ { 0 } - t _ { r } ) /$ $( t _ { 0 } - t _ { c } ) ) S _ { r }$ . Because $( t _ { 0 } - t _ { r } ) / ( t _ { 0 } - t _ { c } ) < 1$ , it follows that remote service is not as effective as local service, which justifies the reduced performance problem. A unit of remote service equals only $( t _ { 0 } - t _ { r } ) / ( t _ { 0 } - t _ { c } )$ units of local service, which implies that remote service is discounted by a factor of $( t _ { 0 } - t _ { r } ) / ( t _ { 0 } - t _ { c } )$

The reduced performance can be more conveniently modeled by using a discount factor. We define a discount factor $\delta _ { i j }$ between $\operatorname { S P s } \ i$ and $j \ \mathrm { i f } ,$ from $\mathrm { S P } \ j ^ { \prime } \mathbf { s }$ perspective, one unit of service capacity from SP i is equivalent to $\delta _ { i j }$ units of $\mathrm { S P } j ^ { \prime } { \bf s }$ local capacity. If the average delay to retrieve content from SP i (the remote SP) and to deliver it to the end users of SP j (the local SP) is $t _ { i j } ,$ and the average delay to retrieve content from the origin is $t _ { 0 j } ,$ we immediately have $\delta _ { i j } = ( t _ { 0 j } - t _ { i j } ) / ( t _ { 0 j } - t _ { c } )$ . Note that in this case $t _ { c }$ can also be denoted as $t _ { j j } .$ . The discount factors satisfy the following properties: $\delta _ { i j } \in ( 0 , 1 ]$ and $\delta _ { j j } = 1$ . The definition of $\delta _ { i j }$ leads to an important property that we call effective multiplication.

Property of Effective Multiplication. Consider SPs $i , j ,$ and l such that

$$
\frac {t _ {i l} - t _ {c}}{t _ {0 l} - t _ {c}} \geq \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}} + \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}}.
$$

Then, we have $\delta _ { i l } < \delta _ { i j } \delta _ { j l }$

Proof. Rewrite the definition of $\delta _ { i j } = ( t _ { 0 j } - t _ { i j } ) /$ $( t _ { 0 j } - t _ { c } )$ as

$$
\delta_ {i j} = \frac {(t _ {0 j} - t _ {c}) - (t _ {i j} - t _ {c})}{t _ {0 j} - t _ {c}} = 1 - \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}}.
$$

To get $\delta _ { i l } < \delta _ { i j } \delta _ { j l } ,$ we need to show

$$
1 - \frac {t _ {i l} - t _ {c}}{t _ {0 l} - t _ {c}} <   \left(1 - \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}}\right) \left(1 - \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}}\right)
$$

i.e.,

$$
\frac {t _ {i l} - t _ {c}}{t _ {0 l} - t _ {c}} > \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}} + \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}} - \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}} \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}}.\tag{1}
$$

Because

$$
\frac {t _ {i l} - t _ {c}}{t _ {0 l} - t _ {c}} \geq \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}} + \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}} \quad (\text { by   the   given   condition }),
$$

and

$$
\frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}} > 0, \quad \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}} > 0
$$

(by that $t _ { c }$ is the time for last mile delivery) then (1) must be true. Q.E.D.

The property of effective multiplication establishes the condition under which capacity provision via intermediation services is beneficial. The condition in the property,

$$
\frac {t _ {i l} - t _ {c}}{t _ {0 l} - t _ {c}} \geq \frac {t _ {i j} - t _ {c}}{t _ {0 j} - t _ {c}} + \frac {t _ {j l} - t _ {c}}{t _ {0 l} - t _ {c}},
$$

is not very restrictive—it is true, for instance, whenever SP j sits on the traffic route from SP i to SP l, i.e., $( t _ { i l } - t _ { c } ) = ( t _ { i j } - t _ { c } ) + ( t _ { j l } - t _ { c } )$ , and if $t _ { 0 l } \le t _ { 0 j }$ . This last condition of $t _ { 0 l } \le t _ { 0 j }$ can be satisfied, for example, if there is a high-speed connection from SP i through $\operatorname { S P } j$ to SP l, a middle-speed connection from the origin to SP $l ,$ and a low-speed connection from the origin to SP j .

## 3.3. Structure of the SLA with Clients

Consider an SLA between an SP and its client. Let - denote the maximum possible volume of content that the client wants the $\mathrm { S P }$ to support during a specified contract period. Let the client also specify that content should be accessible at an average delay of no more than $t _ { 1 }$ during this period. Assume that, when the SLA is made, the actual demand for content during the contract period is unknown and stochastic. Let the continuous random variable - denote the content demand with a density function $g ( \Omega )$ on [0 - ]. The long-term content demand patterns are uncertain and cannot be precisely specified at the contract time. These fluctuations can create mismatches between available capacity and available demand at various points in the contract duration. On the other hand, the short-term demand (immediate or near future) for the content can be more accurately determined. As a result, the whole contract-servicing span can be envisioned as comprising a number of servicing periods. At each servicing period, let the SP be provided with the demand for content for that servicing period. The proposed CPN trading mechanism enables the SPs to maintain the QoS through cooperative trading in each servicing period. Clearly, the length of a servicing period is dictated by the accuracy of demand estimation and the time needed to complete and implement the trade agreement between the service providers. In most online trade scenarios, a service period that lasts only a day or even an hour is practically viable if content duplication among SPs can be accomplished in a timely manner at the beginning of the service period. Note that recent technological advancements, such as traffic prioritization and improvements to the TCP/IP protocol stack, have dramatically improved the content duplication process among SPs.

Now, consider the relationship between the demand for content and the required service capacity at any period of the whole contracting span. Given a demand for - content, the locally serviced content $\Omega _ { c }$ required by the $\mathrm { S P }$ such that the content is delivered with an average access delay of $t _ { 1 }$ (specified in the contract) is given by $\Omega _ { c } = \Omega ( t _ { 0 } - t _ { 1 } ) / ( t _ { 0 } - t _ { c } )$ Because $( t _ { 0 } - t _ { 1 } ) / ( t _ { 0 } - t _ { c } )$ is fixed, $\Omega _ { c }$ is a linear function of - and follows the rescaled distribution of $\Omega .$ Let $h ( \Omega _ { c } )$ and $H ( \Omega _ { c } )$ denote the probability density function and cumulative distribution function of $\Omega _ { c } ,$ where $h ( \Omega _ { c } )$ can be obtained directly from $g ( \Omega )$ Finally, let $\Omega _ { c }$ denote the maximum content requirement locally serviced at any period of the whole contracting span, and thus $\bar { \Omega } _ { c } = \bar { \Omega } ( t _ { 0 } - t _ { 1 } ) / ( t _ { 0 } - t _ { c } )$

Central to the structure of the SLA is the risk that arises from demand uncertainty. At one end of the risk sharing spectrum is a contract where none of the risk is borne by the SP. In such a case, the SP simply agrees to provide a specified amount of capacity to service the content regardless of the average access delays for the duration of the contract at a fixed price. Consequences of any under-utilized capacity or lack of adequate capacity are borne completely by the client. In the case where the SP and the client share the risk, the contract specifies a service capacity amount y $( y \le \bar { \Omega } _ { c } )$ and a corresponding penalty clause. In such a contract, the SP is committed to satisfying the demand of up to a service capacity of y in each of the servicing periods and would pay the client a unit penalty b if for some reason this agreed capacity is not provided during any period of the contract span. The contract specifies a price $p$ that is paid to the SP for this service. The aggregated total penalty is computed at the end of the whole contract span. Note that the risk borne by the SP is increasing in $y ,$ and when $y = \hat { \Omega } _ { c }$ all the risk arising from the uncertainty of content demand is transferred to the SP. It follows then that $p$ is strictly increasing in y. For ease of analysis and exposition we will consider the case of $y = \hat { \Omega } _ { c }$ in the following discussion. The results of this analysis can easily be extended to cases where the SP bears only some of the risk. Note that when the SP bears no risk, the problem faced by the $\mathrm { S P }$ is straightforward: either to provide the capacity at the agreed-upon contract terms or to reject the contract.

In the context of a CPN, the risk arises fundamentally from the fluctuation of demand, which can create either excess capacity or a lack of capacity to meet the realized demand. Whereas the long-term strategy involves effective capacity planning, CPN provides capacity management tools when the available capacity is static and cannot be altered in the short term. The complexities involved in the design of market mechanisms arise from the discounting of quality and the property of effective multiplication exhibited by the capacity resources. In the next section we consider a network of multiple service providers. Such a scenario raises the possibility of topography-based intermediary services, which result in complex capacity allocation and routing strategies among the SPs. We also present results from a longitudinal experimental analysis that provide strong support both for the viability of the discount factors for practical trade scenarios and for the presence of intermediation opportunities for capacity trading on the Internet.

## 4. Network of SPs: Arbitrage and Empirical Evidence

A network of more than two SPs can result in a more efficient allocation of capacity because each SP can provide and realize capacity to and from multiple SPs. The allocation patterns that emerge, however, could be potentially more complex because they provide opportunities for intermediation. We demonstrate this in the following.

## 4.1. Topographical Leverage and Arbitrage

We define an intermediary as an SP who could both provide and realize capacity in the servicing period. An intermediary node is topographically (and not necessarily geographically) situated between the supply and demand nodes. It purchases capacity from the supply node not to meet its own capacity needs, but for the purpose of selling it to the demand node. Such an intermediary could serve as a bridge for capacity allocation among other SPs. Consider SPs 1 and 2 that wish to engage in a capacity trading. In the absence of an intermediary, the SPs would engage in allocation behavior as described in §3. Now assume that a third SP (SP 3) is strategically positioned so that

$$
\frac {t _ {1 3} - t _ {c}}{t _ {0 3} - t _ {c}} + \frac {t _ {3 2} - t _ {c}}{t _ {0 2} - t _ {c}} \leq \frac {t _ {1 2} - t _ {c}}{t _ {0 2} - t _ {c}}.
$$

From the property of effective multiplication it follows that $\delta _ { 1 3 } \delta _ { 3 2 } > \delta _ { 1 2 }$ . By virtue of its strategic topographic location, SP 3 could facilitate a more effective capacity transfer without actually changing its local demand fulfillment in the allocation. Consider a situation where $\mathrm { S P ~ 1 }$ provides 1 unit of capacity to SP 2. If a direct allocation occurs between the two, SP 2 realizes an effective capacity of $\delta _ { 1 2 }$ to service its clients. Now consider an alternate allocation strategy as follows: SP 1 provides capacity of 1 unit to SP 3; this is equivalent to $\delta _ { 1 3 }$ units of capacity for SP 3 at SP 3’s local site. Then SP 3 can allocate $\delta _ { 1 3 }$ units of its own local capacity for use by SP 2. Note that the capacity available for SP 3 is identical to the capacity available prior to the trade, and hence SP 3 is no worse off. However, the amount of capacity available for SP 2 is $\delta _ { 1 3 } \delta _ { 3 2 } ,$ which is larger than when SP 3 is a nonparticipant in the capacity allocation. As a result, SP 3 realizes intermediary surplus sharing as long as it receives positive returns for providing the intermediary services. Such intermediation also enhances the overall effectiveness of the available capacity to provide services to the clients.

The above result can easily be extended to the general case of multiple intermediaries. Let $G = ( V , A )$ denote a network of N SPs, where each node $i \in V$ represents an SP and each edge $( i , j ) \in A$ represents the segment connecting SPs i and j. Let $\delta _ { i j }$ denote the discount factor associated with the edge (i j. We define a compound discount factor for each pair of SPs along each path connecting them in the network as follows. Consider any two SPs i and j. Let $( i , i _ { 1 } , i _ { 2 } , \ldots , i _ { l } , j )$ denote a path between i and j. Then, $\delta ( i , i _ { 1 } , i _ { 2 } , \dots , i _ { l } , j )$ is defined to be the compound discount factor for the path $( i , i _ { 1 } , i _ { 2 } , \ldots , i _ { l } , j )$ and is the product of all the discount factors along this path. Let ${ { \delta } _ { i j } ^ { * } }$ denote the maximum compound discount factor among all paths between i and j. We model the length of the paths with topological distance measured by discount factors and term the path corresponding to the maximum factor $\delta _ { i j } ^ { * }$ as the maximal discount path between the two nodes. All nodes along the maximal discount path have intermediary opportunities in improving the allocation between SPs i and j. The problem of determining the maximal compound discount factors between a pair of SPs is fairly straightforward. Using the inverse of discount factor $1 / \delta _ { i j }$ along each edge (i j of G we solve a product-form of the shortest-path problem.

The standard shortest-path algorithm with a small modification will solve the problem. Instead of using the additive function in the shortest-path recursion, the multiplicative function is used. Note that $0 < \delta _ { i j } \leq 1$ , and, hence, $1 / \delta _ { i j } \geq 1 \forall i , j$ . Therefore, the multiplicative recursion is positive and increasing with each computation of algorithm. As a result, the product-form of the shortest-path algorithm will yield the optimal solution to the problem (Cormen et al. 2001). Finally, it can easily be seen that the same path that solves the problem also yields the maximum compound discount factor.

Successive allocation through intermediaries has strong implications for capacity allocation between SPs who are topographically far remote from each other. Typically, a consortium of intermediaries could generate such networks that are otherwise either too expensive to operate or even impossible. The behavior of the discount factors determines the intermediary options. Intermediary opportunities that arise because of topographical positioning have been observed in the related area of bandwidth trading in the telecom industry (Chiu and Crametz 2000).

## 4.2. Longitudinal Study of Discount Factors in a CPN

We have carried out a longitudinal experimental study of discount factors to assess their spatio-temporal stability and other properties in comparison with the direct measures of delay among the service nodes in a CPN. Large-scale computer networks are often volatile, and any measure, if it is also volatile, poses significant implementation and monitoring problems. Such network delays arise because of the dynamic routing of data packets and other network-based phenomena and cannot be controlled by a service provider. A logical question that follows is whether discount factors are more stable measures than actual time delays. More specifically, we address whether (a) discount factors are less volatile than network delays and (b) discount factors are spatio-temporally stable. Issue (b) implies whether the discount factors are statistically stable over the time-of-the-day and day-of-the-week parameters. Furthermore, as addressed earlier, the property of effective multiplication is an important theoretical foundation of a CPN because it underscores the importance of intermediation to achieve optimal capacity allocation and sharing plans. In the empirical study we were also motivated to seek out cases that exhibited strong effective multiplication. This leads to the following: (c) whether effective multiplication of discount factors holds true for some Internet-based trading paths.

The design of the computational experiments entailed four sites, termed A (Austin, Texas), B (Buffalo, New York), C (Storrs, Connecticut), and S (Seattle, Washington). Note that the computation of a discount factor is based on the triplet (local site, origin site, remote site) with the constraint that the delay time from the remote site is lower than the delay time from the origin site. Thus, the four experimental sites used in the study translated to 12 discount factor computations. The delay times required for the discount factor computation were obtained from the transfer of a data file with a random size of up to 10 MB between site pairs utilizing the file transfer protocol (ftp). File transfers were conducted from every pair of sites on an hourly time interval for a period of 5 months in the year 2004. This computational design yielded a total of 17,622 usable discount factors for analysis. Additional details are provided in Online Supplement II at the Information Systems Research website at http://isr.pubs.informs.org/ecompanion.html.

Table 1 reports the comparative volatility values (measured as the ratio of standard deviation over the mean) for delay times and discount factors. Except for the discount factor with index 5, the results indicate that the discount factors are significantly more stable than network delays. Note that the higher volatility measure of the discount factor for index 5 results primarily from the low mean value (0.0487). For practical purposes, such low discount factors make capacity sharing unviable, further strengthening the case for the use of discount factors for effective capacity sharing contracts.

Table 1 Comparative Volatility Measures

<table><tr><td>Discount factor index</td><td>Volatility of network delay time</td><td>Volatility of discount factor</td><td>Mean discount factor</td></tr><tr><td>1</td><td>0.694</td><td>0.091</td><td>0.8882</td></tr><tr><td>2</td><td>0.694</td><td>0.193</td><td>0.2774</td></tr><tr><td>3</td><td>0.694</td><td>0.068</td><td>0.9187</td></tr><tr><td>4</td><td>0.612</td><td>0.070</td><td>0.7220</td></tr><tr><td>5</td><td>0.612</td><td>0.787</td><td>0.0487</td></tr><tr><td>6</td><td>0.612</td><td>0.091</td><td>0.7068</td></tr><tr><td>7</td><td>0.689</td><td>0.063</td><td>0.9715</td></tr><tr><td>8</td><td>0.689</td><td>0.157</td><td>0.2660</td></tr><tr><td>9</td><td>0.689</td><td>0.048</td><td>0.9780</td></tr><tr><td>10</td><td>0.677</td><td>0.098</td><td>0.5852</td></tr><tr><td>11</td><td>0.677</td><td>0.305</td><td>0.2563</td></tr><tr><td>12</td><td>0.677</td><td>0.055</td><td>0.6940</td></tr></table>

The temporal stability of the discount factors was evaluated by the following empirical model:

$$
\delta_ {i w} = \alpha_ {i} + \sum_ {k = 1} ^ {2 3} \beta_ {k} \text { Hour } + \sum_ {j = 1} ^ {6} \gamma_ {j} \text { Day } + \varepsilon_ {i w}
$$

where i indices the 12 distinct discount factors, j the day-of-week, k the time-of-day, and $w = 1 , \dots , W$ the index of observations. The results, provided in Table 2, indicate that the discount factors are independent of hour of the day or days in a work week (Monday to Friday). An adjusted R<sup>2</sup> value of 0.978 and an F value of 18,819 indicate an excellent fit with the overall model. Finally, Figure 2 illustrates the evidence of effective multiplication when the origin site is located in Seattle, the local site in Austin, and the remote site in Buffalo. A capacity sharing agreement between the remote and the local sites that are intermediated via Connecticut can significantly enhance the overall sharing efficiency. Together the results strongly underscore the viability of discount factors as the appropriate measure for developing capacity sharing strategies.

The empirical finding that the discount factors are more stable than the response time can be explained as follows. As expected, we find that $t _ { c } \approx 0$ . Therefore, we can write $\delta _ { i j } = ( t _ { 0 j } - t _ { i j } ) / t _ { 0 j }$ . In this expression, $t _ { 0 j } - t _ { i j }$ and $t _ { 0 j }$ are random variables and $\delta _ { i j }$ is a ratio of these two random variables. Because the two random variables are highly correlated (<sub>≥</sub>0874 in the experimental analysis for all panels except No. 5), it follows naturally that the ratio of two highly correlated random variables is more stable.

Table 2 Time Stability of Discount Factors

<table><tr><td>Hour of the day</td><td>Estimate (x 0.001)</td><td>p-value</td></tr><tr><td>1</td><td>0.5</td><td>0.83</td></tr><tr><td>2</td><td>1.3</td><td>0.61</td></tr><tr><td>3</td><td>-0.6</td><td>0.81</td></tr><tr><td>4</td><td>0.6</td><td>0.8</td></tr><tr><td>5</td><td>0.5</td><td>0.85</td></tr><tr><td>6</td><td>2</td><td>0.41</td></tr><tr><td>7</td><td>1.1</td><td>0.66</td></tr><tr><td>8</td><td>3.4</td><td>0.16</td></tr><tr><td>9</td><td>0.2</td><td>0.93</td></tr><tr><td>10</td><td>2.3</td><td>0.34</td></tr><tr><td>11</td><td>1.3</td><td>0.58</td></tr><tr><td>12</td><td>1</td><td>0.69</td></tr><tr><td>13</td><td>1.8</td><td>0.47</td></tr><tr><td>14</td><td>-2.5</td><td>0.29</td></tr><tr><td>15</td><td>2.7</td><td>0.26</td></tr><tr><td>16</td><td>-2.9</td><td>0.23</td></tr><tr><td>17</td><td>2.4</td><td>0.32</td></tr><tr><td>18</td><td>-0.1</td><td>0.98</td></tr><tr><td>19</td><td>4.5</td><td>0.06</td></tr><tr><td>20</td><td>1</td><td>0.67</td></tr><tr><td>21</td><td>3.2</td><td>0.19</td></tr><tr><td>22</td><td>-4</td><td>0.11</td></tr><tr><td>23</td><td>-1.1</td><td>0.66</td></tr><tr><td colspan="3">Day of the week</td></tr><tr><td>Tue</td><td>-0.9</td><td>0.53</td></tr><tr><td>Wed</td><td>0.2</td><td>0.86</td></tr><tr><td>Thu</td><td>-2.2</td><td>0.09</td></tr><tr><td>Fri</td><td>-1.2</td><td>0.37</td></tr><tr><td>Sat</td><td>3.8</td><td>&lt;0.01</td></tr><tr><td>Sun</td><td>1.4</td><td>0.3</td></tr></table>

## 5. Cooperative Capacity Sharing: Market Maker Mechanism

Although allocation according to maximal discount paths appears intuitive, it raises a considerable amount of complexity in executing the allocations because of the capacity constraint that each SP faces and in setting priorities when an intermediary is present in two or more maximal discount paths. In the following discussion we present a market maker (MM) mechanism for optimal capacity allocation that is arbitrage-free. This mechanism provides socially optimal allocation plans and is applicable when all the service facilities are under the control of a single owner or when the CPN hub generates allocation plans. In the latter case, the MM is a centralized mechanism that operates in a decentralized market. Each service provider operates independent of the others and chooses to voluntarily participate with the CPN hub that facilitates and coordinates the buying/selling of the capacity resources. Each service provider communicates its proprietary capacity needs or capacity availability information to the hub, which then creates a socially optimal capacity trading agreement. Such centralized mechanisms that operate in decentralized market settings are common in a number of online and financial markets. In cases where there is no integrated planner, the following discussion provides an upper bound on the potential gains from capacity allocation.

Figure 2 Effective Multiplication in the Experimental Sites  
![](/api/attachments/SP4AWKN9/fulltext/images/d5b389bb077edc5dac5d9513f0eebb522b52a1ef295a57af26d640941c62ae9e.jpg)

In the centralized mechanism, the SPs provide full information to the market maker and allocation decisions by the market maker are binding. The market maker’s objectives, illustrated in Figure 3, are twofold: (a) to develop allocation plans that are globally optimal and (b) to develop surplus sharing plans that are fair to the participating SPs. The first objective is developed in the following discussion, and the subsequent objective of developing fair sharing plans is discussed below.

Consider a network $G = ( V , A )$ of SPs. Let $s _ { i }$ be the service capacity of SP i and $y _ { i }$ be the end-user demand at the contract servicing period. In terms of making its own capacity available for others, an SP would simply identify a portion of its own capacity for use by the other SPs. Let $S _ { i j }$ denote the capacity made available by SP i for use by SP j. To simplify notation, let $S _ { i i }$ denote the capacity allocated by $\operatorname { S P } i$ for its own use, and let $\delta _ { i i } = 1$ . Therefore, it follows that $\textstyle \sum _ { j = 1 } ^ { N } S _ { i j } = s _ { i }$ $\forall i \in N$ . Similarly, the total capacity available for SP i is given by $\textstyle \sum _ { j = 1 } ^ { N } \delta _ { j i } S _ { j i }$ . Let E denote the set of nodes with excess capacity (all i where $s _ { i } \geq y _ { i } )$ , and let $F$ denote the set of nodes with excess demand (all i where $s _ { i } < y _ { i } )$ . Note that all the SPs in E should never face a shortfall. Therefore, $\textstyle \sum _ { j = 1 } ^ { N } \delta _ { j i } S _ { j i } \geq y _ { i } , \forall i \in E$ . Similarly, for each node in $F ,$ effective capacity that is provided should not exceed what is required. Therefore, $\begin{array} { r } { \sum _ { j = 1 } ^ { N } \delta _ { j i } S _ { j i } \le y _ { i } , \forall i \in F . } \end{array}$ . The objective of the market maker is to minimize the total penalty incurred by the SPs. Suppose that $b _ { i }$ is the unit penalty at $\mathrm { { S P } } i .$ The market maker solves the following formulation to generate the socially optimal allocation plan.

Figure 3 Market Maker Mechanism  
![](/api/attachments/SP4AWKN9/fulltext/images/82570123bb214d69b472a0c9c73b106aa05fb499d0d83b18b84e86f50898b0bf.jpg)

$$
\begin{array}{l l} \text {(MM)} & \text {Minimize} \sum_ {i \in F} b _ {i} \left(y _ {i} - \sum_ {j = 1} ^ {N} \delta_ {j i} S _ {j i}\right) \\ & \text {s.t.} \sum_ {j = 1} ^ {N} S _ {i j} = s _ {i} \quad \forall   i \\ & \sum_ {j = 1} ^ {N} \delta_ {j i} S _ {j i} \leq y _ {i}, \quad \forall   i \in F \\ & \sum_ {j = 1} ^ {N} \delta_ {j i} S _ {j i} \geq y _ {i}, \quad \forall   i \in E \\ & S _ {i j} \geq 0, \quad \forall i. \end{array}
$$

The above allocation capacity formulation can be solved as a linear programming (LP) problem and hence is computationally efficient. It can easily be verified that the solution to problem MM is arbitragefree. We now turn to the issue of surplus sharing.

## 6. Surplus Sharing

In a CPN, surplus is created from the reduction in the total penalty incurred, and the monetary savings that result from the penalty reduction provide the source of payments for capacity provisioning. In the context of a cooperative game, surplus allocation according to Shapley values is widely regarded as fair. Although it exhibits the property of fairness, this mechanism does not have a core. That is, there would remain incentives for a subset of the players to form a coalition and exclude certain other members from this coalition. For example, existing buyers are always better off by excluding any new buyers from joining the CPN. However, this issue is significantly mitigated in a CPN for the following reasons: (1) members need not share proprietary private information with each other, but only with the trusted third party; (2) significant demand fluctuations make the formation of stable coalitions less attractive—a buyer under certain demand conditions may switch to become a seller under other conditions; and (3) we demonstrate empirically the existence of positive network externalities, where each member, on average, benefits from other members participating with the CPN.

The Shapley values in the context of a CPN can be defined as follows. Let N denote the set of players in this game. Let K be a subset of N and $S _ { j i } ^ { K } , i , j \in K ,$ , be the optimal choices for the MM model computed on the subset K only. We define the characteristic function of Shapley values as

$$
v (K) = \sum_ {l \in F \cap K} b _ {l} (y _ {l} - s _ {l}) - \sum_ {l \in F \cap K} b _ {l} \bigg (y _ {l} - \sum_ {j \in K} \delta_ {j l} S _ {j l} ^ {K} \bigg).
$$

This subset surplus is the maximal subset surplus that can be generated by this subset K only. Consider $i ,$ $i \not \in K .$ . SP i’s marginal contribution to this subset $K$ is $\varphi _ { i } ( K ) = v ( K \cup \{ i \} ) - v ( K )$ . The probability that i joins $K , i \notin K , \mathrm { i s } | K | ! ( | N | - | K | - 1 ) ! / | N | !$ . The Shapley value of i in this cooperative game is the expected marginal contribution that i can make by joining a subset $K ,$ $i \not \in K$ . Now formally define v, $N \to R ^ { 1 }$ as a side payment game where the set surplus is given by $v ( K )$ $\forall K \subseteq N$ . Let $\boldsymbol { \phi } = \{ \phi _ { 1 } , \ldots , \phi _ { N } \}$ define how $v ( N )$ is shared among $i = 1 , \ldots , N$ according to Shapley values. We have

$$
\phi_ {i} (v) = \sum_ {K \subseteq N \backslash \{i \}} \frac {| K | ! (| N | - | K | - 1) !}{| N | !} [ v (K \cup \{i \}) - v (K) ].
$$

It can be seen that $\begin{array} { r } { \sum _ { i \in N } \phi _ { i } ( v ) = v ( N ) } \end{array}$ , which is the surplus of the global set to be shared among the N members. The order of number of subsets $K \subseteq N \backslash \{ i \}$ that i can join is $O ( 2 ^ { N - 1 } )$ . Each surplus computation vK involves solving an LP problem. For each subset K we need $v ( K \cup \{ i \} )$ and $v ( K )$ , which requires two LPs for each computation of the marginal contribution $\varphi _ { i } ( K )$ . Online Supplement III at the Information Systems Research website at http://isr.pubs. informs.org/ecompanion.html. presents a number of useful structural properties of the Shapley values. Because the direct computation of Shapley values is of exponential order and is not feasible in practical systems, we develop a heuristic approach in the following discussion.

## 6.1. Surplus Sharing Algorithm

The computational burden in obtaining the Shapley values arises from the exponential number of permutations of the set of N SPs that need to be considered. In the following discussion we develop a heuristic methodology that is based on sequential sampling from the exponential number of possible permutations. This heuristic strategy offers important advantages in developing properties of the estimated Shapley values and deriving stochastic bounds on the Shapley value estimates. The algorithm is formally developed below.

Algorithm: Sequential Permutation Sampling Inputs: $\delta _ { i j } , b _ { i } , y _ { i } , s _ { i } ,$ , for all $i , j \in N$

Step 1 (Initialization). Select initial sample size m. Generate m random permutations $\pi _ { 1 } , \ldots , \pi _ { m }$ of the set N with replacement. For each permutation $\boldsymbol { \pi } _ { q }$ compute SP i’s marginal contribution $\varphi _ { i } ( K ( \pi _ { q } , i ) ) =$ $v ( K ( \pi _ { q } , i ) \cup \{ i \} ) - v ( K ( \pi _ { q } , i ) )$ where $K ( \pi _ { q } , i )$ is the set of SPs that precede SP i in the permutation $\pi _ { q } .$ Compute the estimated Shapley value $\hat { \phi } _ { i , m } ( v ) \stackrel { \cdot } { = }$ $\textstyle \sum _ { q = 1 } ^ { m } \varphi _ { i } ( K ( \pi _ { q } , i ) ) / m$ and the estimated variance of marginal contributions

$$
\hat {\sigma} _ {i, m} ^ {2} = \frac {1}{m - 1} \cdot \sum_ {q = 1} ^ {m} (\varphi_ {i} (K (\pi_ {q}, i)) - \hat {\phi} _ {i, m} (v)) ^ {2}.
$$

Step 2 (Generate Permutation). Generate an additional random permutation. Set $m  m + 1$ and compute $\hat { \phi } _ { i , m + 1 } ( v )$ and $\hat { \sigma } _ { i , m + 1 } ^ { 2 }$

Step 3 (Stopping Criterion). If

$$
\max \left\{\frac {| \hat {\phi} _ {i , m + 1} (v) - \hat {\phi} _ {i , m} (v) |}{\hat {\phi} _ {i , m} (v)}, \frac {| \hat {\sigma} _ {i , m + 1} ^ {2} - \hat {\sigma} _ {i , m} ^ {2} |}{\hat {\sigma} _ {i , m} ^ {2}} \right\} > \varepsilon ,
$$

where $\varepsilon > 0$ is a prespecified small positive number, then go to Step 2.

Step 4 (Compute Shapley Values and Determine Bounds). Set $m  \overline { { m } }$ . Use the normal distribution ${ \cal N } ( \hat { \phi } _ { i , m + 1 } ( v ) , \hat { \sigma } _ { i , m + 1 } ^ { 2 } / \overline { { { m } } } )$ to estimate the Shapley values and the confidence intervals. STOP.

Note that the above sequential permutation sampling algorithm requires solutions to OmN  <sub></sub> LP problems. The estimated Shapley values thus obtained exhibit the properties of being unbiased, consistent, sufficient, asymptotically normally distributed, and asymptotically efficient. These properties are developed in the following analysis.

Let 1 denote a permutation of the nodes. The <sub></sub>N <sub>!</sub> permutations form a population $\Pi = \{ \pi ^ { 1 } , \ldots , \pi ^ { | N | ! } \}$ Pick an arbitrary permutation $\pi ^ { q } .$ . Here a superscript denotes that the permutation is a member of the population set 4, and a subscript denotes that the permutation is a member of a sample set, denoted as 5. Then i joins subset of $N \backslash \{ i \}$ in $\pi ^ { q }$ . Denote the subset as $K ( \pi ^ { q } , i ) . \ \varphi _ { i } ( K ( \pi ^ { q } , i ) )$ is the marginal contribution of i to $K ( \pi ^ { q } , i )$ in 1 <sup>q</sup> . $\varphi _ { i } ( K ( \pi ^ { q } , i ) ) = v ( K ( \pi ^ { q } , i ) \cup \{ i \} ) -$ $v ( K ( \pi ^ { q } , i ) )$ . Then $\varphi _ { i } ( K ( \pi ^ { 1 } , i ) ) , \dots , \varphi _ { i } ( K ( \pi ^ { | N | ! } , i ) )$ forms a population ${ \Pi } _ { i } = \{ \varphi _ { i } ( K ( { \pi } ^ { 1 } , i ) ) , \ldots , \varphi _ { i } ( K ( { \pi } ^ { | N | ! } , i ) ) \}$ $\forall i = 1 , \ldots , N$

The sampling algorithm works as follows. First, select a random subset, 5, of permutations with replacement from $\Pi = \{ \pi ^ { 1 } , \ldots , \pi ^ { | N | ! } \}$ , i.e., $\Theta =$ $\{ \pi _ { 1 } , \ldots , \pi _ { m } \}$ . Then, for each observation in 5, compute i’s marginal contribution, $\varphi _ { i } ( K ( \pi _ { 1 } , i ) ) , \ldots ,$ $\varphi _ { i } ( K ( \pi _ { m } , i ) ) , \forall i = 1 , \dots , N$ . This set of $\varphi _ { i }$ is a sample of size m. Obtain the sample mean,

$$
\hat {\phi} _ {i, m} (v) = \frac {1}{m} \cdot \sum_ {q = 1} ^ {m} \varphi_ {i} (K (\pi_ {q}, i)), \quad \forall   i = 1, \ldots , N.
$$

$\hat { \phi } _ { i , m } ( v )$ is a sample mean. $\phi _ { i } ( v )$ is the population mean. The sample mean is an unbiased, sufficient, consistent, asymptotically efficient estimator of the population mean (Green 2003). Let $\sigma _ { i } ^ { 2 }$ be the variance for population $P _ { i } = \{ \varphi _ { i } ( K ( \pi ^ { 1 } , i ) ) , \dots , \varphi _ { i } ( K ( \pi ^ { | N | ! } , i ) ) \}$ Then sample mean has the asymptotic distribution $\sqrt { m } ( \hat { \phi } _ { i , m } ( v ) - \phi _ { i } ( v ) ) \stackrel { d } { \longrightarrow } N ( 0 , \sigma _ { i } ^ { 2 } )$ . The sample variance $\textstyle \hat { \sigma } _ { i , m } ^ { 2 } = \sum _ { q = 1 } ^ { m } ( \varphi _ { i } ( K ( \pi _ { q } , i ) ) - \hat { \phi } _ { i , m } ( v ) ) ^ { 2 } / ( m - 1 )$ is an unbiased and asymptotically efficient estimator for the population variance $\sigma _ { i } ^ { 2 }$ . The sample variance has the asymptotic distribution of $\chi _ { m } ^ { 2 } .$ . Therefore, when m is large, we can use the sample mean $\hat { \phi } _ { i , m } ( v )$ to estimate the Shapley value $\phi _ { i } ( v )$

Because the asymptotic distribution of both $\hat { \phi } _ { i , m } ( v )$ and $\hat { \sigma } _ { i , m } ^ { 2 }$ depends on a large sample $m ,$ we need to determine whether $\hat { \phi } _ { i , m } ( v )$ and $\hat { \sigma } _ { i , m } ^ { 2 }$ converge before using them to estimate the Shapley values. The stopping rule in the sequential sampling algorithm is used for this purpose. If

$$
\max \left\{\frac {| \hat {\phi} _ {i , m + 1} (v) - \hat {\phi} _ {i , m} (v) |}{\hat {\phi} _ {i , m} (v)}, \frac {| \hat {\sigma} _ {i , m + 1} ^ {2} - \hat {\sigma} _ {i , m} ^ {2} |}{\hat {\sigma} _ {i , m} ^ {2}} \right\} \leq \varepsilon ,
$$

where $\varepsilon > 0$ is a prespecified small positive number, then we conclude that the estimated mean and variance converge. The value of the resulting m provides the requisite sample size. The asymptotic property is useful because the size of the population, although finite, can quickly grow. For example, with ten SPs the population size is 3,628,800, and the corresponding value of m<sub></sub> is 30.

## 7. Computational Analysis

We have conducted an extensive simulation analysis of capacity trading with the market maker mechanism. The key objective of the simulation analysis is to provide critical insights on the surplus generation from capacity trading via CPN and the performance of the sequential permutation sampling heuristic strategy for surplus allocation.

The design of the simulation analysis is as follows. The CPN comprises 100 SPs, each with a capacity of 0.5. The penalty for each of the SPs is generated from a uniform distribution on 05 1. The discount factor between each pair of SPs, $\delta _ { i j } ,$ is generated from the uniform distribution on 0 1. One hundred trading periods denoted as $\tau = 1 , \dots$  100 are simulated. In each trading period, the demand at each SP is drawn from a uniform distribution on 0 1. Note that the capacity at each SP is set at the expected value of the demand.

The first set of experiments focuses on the total surplus generated from the market maker capacity allocation strategy. This surplus is generated from savings in the penalty payments by the SPs who face a shortfall in demand. We consider the impact of the number of SPs participating in the CPN on the total surplus generated. Initially, one SP is selected randomly. At each iteration, one additional SP from the list of remaining unselected SPs is chosen randomly and added to the network, and the total surplus is recomputed with the additional SP. Figure 4 depicts the total surplus and the average surplus per SP, averaged over 100 trading periods, over the size of the network. As expected, the total surplus generated is nondecreasing in the size of the network. Interestingly, the average surplus per SP also exhibited a strong upward trend.

Figure 4 Total and Average Surplus  
![](/api/attachments/SP4AWKN9/fulltext/images/828b6fee4b6e010a3445c2191c09f1a888be99248e7b82b4140407a5ff6f5ec4.jpg)

![](/api/attachments/SP4AWKN9/fulltext/images/249b0c2e725005bfb1f2ad6426a0c230c8914324cf909dcd40b472fda62122ef.jpg)

To further explore the impact by an SP as additional members join the network, we conducted the following experiments. A group of five SPs was selected as the control set. Additional members were iteratively added to the control set, and in each instance the actual and estimated Shapley values for each of five SPs is computed. Given the computational complexity inherent in the calculation of the exact Shapley values, these were computed only while the size of the network is no more than 10. The estimated Shapley values, however, were computed until all the SPs in the design set were included in the network. The sequential permutation sampling algorithm was used to estimate the Shapley values. This methodology resulted in two sets of data for each of the five SPs in the control set—one based on the true Shapley values and the other based on the estimated Shapley values. We then performed regression analysis on each of the 10 data sets, with the number of participating SPs in the network as the independent variable, and the Shapley values as the dependent variable. The estimated coefficients of the network size are all positive and significant at the 0.05 level. Figure 5 presents a histogram of the estimated coefficients. These results underscore the presence of strong positive network externality effects, whereby each of the SPs is benefited as new members join the network.

We now provide an analysis of the performance of our sequential permutation sampling algorithm. Note that the computational effort incurred in this algorithm depends on the sample size required to satisfy the stopping criteria. As described earlier, we consider trading networks of various sizes. For each trading network considered, the sampling strategy is repeated five times, for each of 100 trading periods. Figure 6 depicts the average values of the minimum, mean, and maximum sample sizes required as a function of the network size. The figure reveals that the proposed sampling algorithm converges rapidly. The sample sizes required, even for large networks, is fairly small (all of the sample sizes in the experimental analysis were under 500). This highlights the computational efficiency of the proposed algorithm for practical applications.

Figure 5 Network Size  
![](/api/attachments/SP4AWKN9/fulltext/images/be5bae23ed8a0080c21b40cef6a5daebf1dfd29c84df0707d84b2e171ca7afd0.jpg)

Figure 6 Sample Size  
![](/api/attachments/SP4AWKN9/fulltext/images/0ab15791d0f44c07191c978d81104e357f4a3e65ee814e8376e5c3420e64e258.jpg)

An important evaluation metric of the heuristic is the quality of the estimated Shapley values in relation to the true Shapley values. We provide this comparative analysis for networks ranging in size from five to ten SPs, repeated over 100 trading periods. We compute the metric “coefficient variances,” which is defined as the ratio of the standard deviation of the estimated Shapley values to the true Shapley values. A histogram of the “coefficient variances” is shown in Figure 7. The vast majority of the estimated Shapley values are within 20% of the true Shapley values and were obtained with very small sample sizes. For example, with ten SPs, the sample size is under 100 (see Figure 6) for a population of size 3,628,800.

For larger networks, the computational burden involved in obtaining the true Shapley values precludes a direct comparison between the exact and estimated values. For a large network of eighty-five SPs, we compute the ratio of the standard deviation to the mean for each SP, based on five samples. A histogram of the computed ratio is shown in Figure 8, and it suggests that the estimated Shapley values are relatively impervious to the sample that is drawn.

Figure 7 Coefficient Variances for Smaller Networks  
![](/api/attachments/SP4AWKN9/fulltext/images/76bc0f28bb2111fd340a35970428c8431ef07b7571b81a4939a754aa95ed0854.jpg)

While the estimated Shapley values may deviate from the true Shapley value for an SP in a given trade scenario, we are motivated to consider this deviation from a cumulative perspective. In other words, capacity trading is expected to occur repeatedly over time, and a well designed surplus sharing mechanism would ensure convergence in cumulative surplus allocations. Let $\phi _ { i } ^ { \tau } - \hat { \phi } _ { i } ^ { \tau }$ denote the difference between the actual and estimated Shapley values for SP i in a trade that occurs in period 9. The cumulative percentage deviation of the estimated Shapley values is given by $( \textstyle \sum _ { i = 1 } ^ { N } | \sum _ { \tau = 1 } ^ { \Gamma } ( \phi _ { i } ^ { \tau } - \hat { \phi } _ { i } ^ { \tau } ) | ) / ( \textstyle \sum _ { i = 1 } ^ { N } \hat { \textstyle \sum _ { \tau = 1 } ^ { \Gamma } } \hat { \phi } _ { i } ^ { \tau } )$ , where : is the number of trade periods and N is the size of the network. Figure 9 illustrates the convergence of the cumulative deviation between the true and estimated Shapley values for a network of size five over a period of 100 trades. The gross absolute cumulative differences drop rapidly (from approximately 20% in one period to under 2% in 30 periods), underscoring the practicality of the proposed algorithm in practical trade scenarios.

Figure 8 Standard  
![](/api/attachments/SP4AWKN9/fulltext/images/c594d1d9df28010c8741c7dc6db66878ad7d34ef93e1a1fff569aa3319181092.jpg)

Figure 9 Convergence of Cumulative Shapley Values  
![](/api/attachments/SP4AWKN9/fulltext/images/f366f499a330a1fb47fcf4f15591272eedba0353786becb91f272b14b4aa68ed.jpg)

## 8. Concluding Remarks

In this paper we first model the business-level CPN as a financial market for ISI services with a central market coordinator. We expect several innovative business models for Internet markets to originate from this concept. Second, we develop the service level leverages that drive the potential trades at the business level. Using standardized QoS as a basis, the topographical leverage of storage services is modeled as discounted QoS capabilities of storage resources.

The discounted capacities characterize the efficiency gains that result from storage capacity trading among remote servers and provide a stable basis for the trades. Third, we investigate the spatio-temporal stability of the discount factors using a test-bed on the Internet through a longitudinal empirical study. This study has established the discount factors to be very stable, highly resilient to indeterminate traffic behaviors over the Internet, and in possession of the useful property of effective multiplication that can be effectively used to evaluate resources in potential trades. Furthermore, the traditional metrics for QoS are much more volatile and highly sensitive to Internet traffic pattern changes. In this regard, the proposed discount factors offer a stable and robust alternative. Fourth, we develop the economic foundations of the CPN and a market maker mechanism for trade coordination and surplus generation using a cooperative capacity sharing principle. Fifth, we develop a surplus sharing strategy using Shapley values. We develop the structural properties of the surplus sharing strategy and a sequential permutation sharing algorithm that asymptotically converges to the Shapley values. Finally, we present detailed simulations with the CPN architecture.

We develop the foundations of the market mechanisms that would enable SPs to meet volatile demands for their services through bilateral and multilateral capacity trading. We show using a CPN trading model that each SP would gain by agreeing to buy/sell the additionally needed/excess capacities as market conditions dictate. Such trading is particularly advantageous when the resources are relatively expensive to build and when their nonavailability could lead to higher customer churn rates. This study demonstrates the practical business viability of a cooperative CPN market. Consequently, we can see a rapid emergence of the CPN market with several innovative business models. The centralized approach utilized in the current study can be fruitfully extended to consider a decentralized approach where the transactions could be modeled as a network of auctions.

## Acknowledgments

A preliminary version of the paper was presented at the Workshop on Information Technologies and Systems (WITS), 2005, and was nominated for the best paper award. The authors gratefully acknowledge the senior editor, associate editor, and three reviewers for many constructive suggestions that have significantly enhanced the manuscript.

## References

Buyya, R. 2002. Economic-based distributed resource management and scheduling for grid computing. Ph.D. thesis, Monash University, Melbourne, Australia.

Chen, Y., R. Katz, J. Kubiatowicz. 2002a. Dynamic replica placement for scalable content delivery. 1st Internat. Workshop Peer-to-Peer Systems, Cambridge, MA.

Chen, Y., L. Qiu, W. Chen, L. Nguyen, R. H. Katz. 2002b. Clustering web content for efficient replication. Proc. 10th IEEE Internat. Conf. Network Protocols ICNP’02, Los Alamitos, CA.

Chen, Y., L. Qiu, W. Chen, L. Nguyen, R. H. Katz. 2003. Efficient and adaptive web replication using content clustering. IEEE J. Selected Areas Comm. 21.

Chiu, S., J. P. Crametz. 2000. Surprising pricing relationships. Bandwidth Special Rep. 12–14, http://www.riskwaters.com/ bandwidth/images/pricing.pdf

Cormen, T. H., R. L. Rivest, C. E. Leiserson, C. Stein. 2001. Introduction to Algorithms, 2nd ed. The MIT Press, Cambridge, MA.

Dilley, J., B. Maggs, J. Parikh, H. Prokop, R. Sitaraman, B. Weihl. 2002. Globally distributed content delivery. IEEE Internet Comput. 6 50–85.

Edge Side Includes. http://www.esi.org/index.html, Oracle Corporation and Akamai Technologies, Inc., Cambridge, MA.

Ferguson, D., C. Nikolaou, J. Sairamesh, Y. Yemini. 1996. Economic models for allocating resources in computer systems. Market-Based Control: A Paradigm for Distributed Resource Allocation. World Scientific Press, Singapore.

Foster, I., C. Kesselman. 1997. Globus: A metacomputing infrastructure toolkit. Internat. J. Supercomputer Appl. 11(2) 115–128.

Foster, I., A. Roy, V. Sander. 2000. A quality of service architecture that combines resource reservation and application adaptation. Proc. IEEE/IFIP 8th Internat. Workshop on Quality of Service IWQOS 2000, Pittsburgh, 181–188.

Gao, L., M. Dahlin, A. Nayate, J. Zheng, A. Iyengar. 2005. Improving availability and performance with application-specific data replication. IEEE Trans. Knowledge Data Engrg. 17(1) 106–120.

Geng, X., R. Gopal, R. Ramesh, A. B. Whinston. 2003. Capacity provision networks: A scalable web services architecture for web cache trading hubs. IEEE Comput. 36(11) 64–72.

Green, W. H. 2003. Econometric Analysis, 5th ed. Pearson Education, Upper Saddle River, NJ.

HTRC Group, LLC. 2005. The emerging internet storage infrastructure market. Research report, The HTRC Group, San Andreas, CA.

Junginger, M., Y. Lee. 2002. The multi-ring topology-high-networks. Proc. Second Internat. Conf. Peer-to-Peer Comput. P2P 2002, Linköping University, Linköping, Sweden, 49–56.

Kangasharju, J., J. Roberts, K. Ross. 2001. Object replication strategies in content distribution networks. 6th Web Caching Workshop, Boston.

Li, B., M. J. Golin, G. F. Italiano, X. Anddeng. 1999. On the optimal placement of web proxies in the internet. 18th INFOCOM Conf., New York.

Oram, A., ed. 2001. Peer-to-Peer: Harnessing the Power of Disruptive Technologies. O’Reilly Press, Cambridge, MA.

Pierre, G., M. V. Steen. 2001. Globule: A platform for self-replicating web documents. 6th Internat. Conf. Protocols for Multimedia Systems, Springer, New York.

Pierre, G., M. V. Steen. 2003. Design and implementation of a usercentered content delivery network. 3rd IEEE Workshop on Internet Appl., San Jose, CA.

Preston, W. C. 2002. Using SANs and NAS. O’Reilly & Associates, Cambridge, MA.

Qiu, L., V. Padmanabhan, G. Voelker. 2001. On the placement of web server replicas. 20th INFOCOM Conf., Anchorage, AK.

Rabinovich, M., A. Aggarwal. 1999. Radar: A scalable architecture for a global web hosting service. Comput. Networks 31 1545–1561.

Rabinovich, M., O. Spatschek. 2002. Web Caching and Replication. Pearson Education, Upper Saddle River, NJ.

Radoslavov, P., R. Govindan, D. Estrin. 2001. Topology-informed internet replica placement. 6th Web Caching Workshop, Boston, MA.

Ramanna, S. S., R. Sharman, R. Ramesh, R. D. Gopal. 2006. Cache architecture for on-demand streaming on the web. Working paper.

Rodriguez, P., S. Sibal. 2000. SPREAD: Scalable platform for reliable and efficient automated distribution. Comput. Networks 33 33–49.

Sayal, M., P. Sheuermann, R. Vingralek. 2003. Content replication in Web<sub>++</sub>. 2nd Internat. Sympos. Network Comput. Appl., Cambridge, MA.

Sharman, R., S. S. Ramanna, R. Ramesh, R. Gopal. 2007. Cache architecture for on-demand streaming on the Web. ACM Transact. Web (TWEB) 1(3).

Waldspurger, C., T. Hogg, B. Huberman, J. Kephart, W. Stornetta. 1992. Spawn: A distributed computational economy. IEEE Trans. Software Engrg. 18(2) 103–117.
