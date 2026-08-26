---
otero_id: 1286
otero_key: "6CYAETP8"
title: "Composite quality of service and decision making perspectives in wireless networks"
authors: "Punit Ahluwalia; Upkar Varshney"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.10.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Composite quality of service and decision making perspectives in wireless networks

Punit Ahluwalia <sup>a,</sup>⁎, Upkar Varshney

<sup>a</sup> CIS and QM Department, The University of Texas — Pan American, Edinburg, TX-78541, United States

<sup>b</sup> Department of Computer Information Systems, Georgia State University, Atlanta, Georgia 30302-4015, United States

## a r t i c l e i n f o

Article history: Received 19 August 2007 Received in revised form 15 July 2008 Accepted 2 October 2008 Available online 5 November 2008

Keywords: Quality of service Composite quality of service Decisions

## a b s t r a c t

Supporting quality of service (QoS) in wireless networks has been a very rich and interesting area of research. Many signi<sup>fi</sup>cant advances have been made in supporting QoS in single wireless networks. However, the support for the QoS across multiple heterogeneous wireless networks will be required in the future wireless networks. In connections spanning multiple wireless networks, the end-to-end QoS will depend on several factors such as mobility and connection patterns of users, and the QoS policies in each of the wireless networks. The end-to-end QoS is also affected by multiple decisions that must be made by several different network entities for resource allocation. The paper has two objectives: one is to demonstrate the decision making process for resource allocation in multiple heterogeneous wireless networks and the second is to present a novel concept of composite QoS in such wireless environment. More speci<sup>fi</sup>cally, we present an architecture for multiple heterogeneous wireless networks, decision making process for resource request and allocation, a simulation model to study composite QoS, and several interesting results. We also present potential implications of composite QoS on users and network service providers. We also show how the QoS ideas presented in this paper can be used by wireless carriers for improved QoS support and management. The paper can form the basis for a signi<sup>fi</sup>cant further research in DSS for emerging 3G/4G wireless networks supporting QoS for a range of sophisticated and resource intensive mobile applications.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

“Quality of Service” in wireless networks has been a very widely researched topic [29,32,13,1]. This paper proposes a new paradigm in “Quality of Service” in wireless networks. We call this new paradigm — “Composite Quality of Service (CQoS)”. Additionally, this paper investigates and presents the decisions made by various entities in providing or requesting “Quality of Service” in wireless networks.

The “Quality of Service” in wireless networks can be broadly de<sup>fi</sup>ned as the guarantees of support provided by the networks based on the applications agreeing to conform to certain conditions of requirements. Conditions of requirements may mean resources requested or traf<sup>fi</sup>c characteristics. In this de<sup>fi</sup>nition, resources denote the bandwidth requested by applications and traffic characteristics denote the number, arrival and duration characteristics, and mobility characteristics.

The applications that are supported by wireless networks are especially attractive to users because of their anytime–anywhere characteristics. Therefore numerous mobile applications are being developed. The challenges in supporting voice, data, and multimedia traf<sup>fi</sup>c by wireless networks have been studied by the research community and a wide range of solutions to improve the QoS received by these applications have been proposed. In this paper, we present a novel yet simple measure of quality of service in wireless networks which includes both user centric vs network centric QoS measures.

## 1.1. Focus of the paper and research contributions

The main focus of this paper is on presenting a new paradigm of representing “Quality of Service” in wireless networks viz. Composite Quality of Service (CQoS). Further, we contend that the quality of service requested by users or applications or that provisioned by the wireless networks can be studied from the perspective of decisions made by various actors in the network. The paper also presents decision making by various entities in wireless networks in the context of QoS support.

## 1.1.1. Composite quality of service

Until now, the research community has identi<sup>fi</sup>ed different elements of Quality of Service (QoS) in wireless networks. The QoS in wireless networks has been examined in terms of supporting “new incoming” as well as “existing” connections by proposing different methods of allocating <sup>fi</sup>xed amounts of bandwidth. The QoS in wireless has been de<sup>fi</sup>ned to include connection blocking probability and connection dropping probability [29]. Because the bandwidth available to wireless networks is limited, its ef<sup>fi</sup>cient utilization has also been considered an important goal. Most research in QoS considers these three parameters, but has analyzed them separately.

These contributions have resulted in a much better understanding of “Quality of Service” in wireless networks by the research and practitioner community. However, much of this research has been “network centric” — that is, the research has focused on the challenges and opportunities available to the networks in effectively providing QoS to various applications. However, there is a need to examine the “user-centric” context of QoS in wireless networks. For example, an important research question is — “What do the different elements of QoS mean to a user as a single metric of quality of service?” In this paper we endeavor to answer this research question. We present a new paradigm of CQoS as a single, homogeneous metric of QoS that uni<sup>fi</sup>es different QoS metrics. An important contribution of CQoS will be to balance user-centric considerations such as connection dropping and connection blocking with network-centric considerations such as bandwidth utilization.

## 1.1.2. Decision making in wireless networks

The topic of quality of service in wireless has been traditionally dealt with as primarily a resource management issue. This treatment is quite appropriate because wireless networks have limited resources and the overall quality of service depends on how effectively and ef<sup>fi</sup>ciently the available resources are provisioned to the applications seeking them. Several entities in a wireless network are involved in the resource allocation process. These entities need to consider several factors such as network parameters, available resources, QoS demands of the applications, and QoS policies etc. in order to make decisions that affect how the resource allocation is made. The decisions by the entities may be made individually or through interaction with other entities. Therefore, an insight into the decision making of these entities is likely to lead to a better understanding of the potentials and the challenges in improving the “Quality of Service in wireless networks”. In this paper, we investigate the decision making in the resource allocation process in wireless networks.

In this paper we use scenario based simulation modeling approach to present the paradigm of CQoS in wireless networks. We also consider heterogeneous wireless network architecture in view of the emerging 3G and 4G networks [41]. In these networks a user might be able to access multiple networks during a session which may result in setting up of connections across heterogeneous wireless networks. For example, a user traveling during a single session with another mobile user may be connected to a cellular network, and then to a satellitebased networks where the cellular network may be unable to support the connection. The user at the other end of the connection may also be located in another wireless network. Therefore, such a connection may traverse through multiple wireless networks. In a heterogeneous wireless network environment, the QoS received by a particular application will not only depend upon the network in which the users are located, but also the network conditions at the other end of the connection as well as the intermediate networks [1]. We analyzed the end-to-end QoS performance by simulating various traf<sup>fi</sup>c and mobility scenarios. Details of the scenarios considered, simulation methodology and the evaluation results are provided in the paper.

Moreover, the performance of various QoS metrics needs to be considered in context of resource utilization. Since the wireless networks have bounded resources, and because resource allocation impacts the QoS at the connection level, resource utilization in the networks needs to be taken into account while analyzing the QoS performance. The network utilization can be de<sup>fi</sup>ned as the ratio of the bandwidth utilized to the total bandwidth available in a network over a given period of time. In a fully loaded network, providing incremental QoS is likely to incur costs in terms of the overall resource utilization in the network. The trade-off between QoS performance and resource utilization is likely to signi<sup>fi</sup>cantly impact the network management policies. As a result, from the context of network providers, “utilization” is an important metric in the study of QoS provisioning in wireless. Therefore, we also analyze the resource utilization performance and include it as a component in overall QoS.

If $Q _ { \mathrm { b } }$ is the call blocking probability, $Q _ { \mathrm { d } }$ is the call dropping probability, and U is the utilization, then overall QoS, denoted by Q, can be expressed as:

$$
Q = f (Q _ {\mathrm{b}}, Q _ {\mathrm{d}}, U)\tag{1}
$$

The individual QoS metrics $( Q _ { \mathrm { b } } , Q _ { \mathrm { d } } ,$ and U) are a function of frequency of connection arrivals, average longevity of connections, bandwidths available, and mobility of users in the individual networks [1].

In heterogeneous wireless networks, the end-to-end connections between any two users may span multiple wireless networks. These connections are setup and maintained with the co-operation of source and destination as well as intermediate networks, each of which may have different amounts of resources, and QoS support. In such connections, the characteristics and traf<sup>fi</sup>c pattern in each of the networks are likely to impact the overall QoS.

In this paper, we evaluated CQoS by using a heterogeneous wireless network as a case study. We use simulation modeling to conduct the analysis. Furthermore, a decision making perspective of various entities which in<sup>fl</sup>uences QoS in wireless networks is also presented.

## 1.1.3. Our approach and contributions

To the best of our knowledge, this is the <sup>fi</sup>rst paper which has synthesized various separate metrics QoS to propose a single, unifying QoS metric. The main contributions of this paper are as follows:

1. We introduce a single unifying metric of QoS, namely “CQoS”

2. We investigate QoS provisioning in wireless networks in terms of decision making by various entities

3. We present insights into the implications of CQoS on users and network service providers through qualitative discussion of simulation results.

The rest of the paper is organized as follows. Related work in QoS for wireless networks is discussed in Section 2. The proposed CQoS metric is discussed in Section 3. The decision support provided by various network entities in supporting QoS is discussed in Section 4. The simulation model, results of performance evaluation and qualitative analysis of the results are presented in Section 5. In Section 6, we discuss implications of CQoS on users and network providers. The concluding remarks and opportunities for future research are discussed in Section 7.

## 2. Related work

In this section, we summarize the existing research in QoS for wireless networks. In particular, we focus on the various metrics of QoS proposed by the research community.

The focus of most research in QoS for wireless networks has been on allocating resources to mobile users on a call or connection level. Probabilities of new call blocking and existing call dropping have been posited as important basic QoS metrics in wireless networks [31,27]. The call admission algorithm determines whether an incoming call can be admitted or not, based on ef<sup>fi</sup>cient allocation of the limited bandwidth to guarantee users' QoS requirements. A call is forced to terminate when attempting a handoff, if the target cell does not have enough bandwidth to support the connection. In the existing research, it is posited that termination of existing connections would cause greater level of annoyance to users than if the new connections are denied access. Therefore, handoff calls have been given a higher priority in accessing the available bandwidth, in order to provide a seamless connection to users. Because of bounded availability of bandwidth, there is a trade-off between the levels of connection dropping and connection blocking that can be supported under conditions of total demand exceeding the supply of resources. A network that provides some buffer bandwidth for expected handoffs is likely to result in lower connection dropping probability, at some cost of higher connection blocking probability, hence better overall QoS [31]. However the relative importance of each individual metric depends on the context of the application. For example, a certain establishment of connection in a disaster recovery scenario, even if for a short duration is very important lending greater signi<sup>fi</sup>cance to QoS of connection blocking relative to QoS of connection dropping. A data connection such as an email or a “text messaging” application lends almost equal signi<sup>fi</sup>cance to QoS of connection blocking and connection dropping because a slight delay in transfer of data is of little consequence to users in most cases. On the other hand, a data connection comprising of a <sup>fi</sup>nancial transaction lends great importance to connection dropping probability because an incomplete <sup>fi</sup>nancial transaction may have to be started all over again and may cause anxiousness to users.

Bandwidth reservation has been proposed in order to maximize the ef<sup>fi</sup>cient use of available bandwidth while giving higher priority to handoff calls. Some bandwidth is reserved for the exclusive use of handoff calls, while the rest is shared by both new calls and handoff calls. The amount of reserved bandwidth affects the QoS performance as well as the resource utilization. Reserving greater resources leads to reduced probability of call dropping during handoff, but may result in higher connection blocking probability and lower utilization ef<sup>fi</sup>ciency.

Several bandwidth reservation schemes have been proposed to maximize resource utilization while minimizing call dropping probabilities [14,12]. Bandwidth can be reserved based on the knowledge of the traf<sup>fi</sup>c pattern of the area, and the estimation of channel occupancy time distribution [19]. However these parameters may also vary over time due to user-mobility. For example, to provide adequate QoS to the existing connections in micro-cellular networks, distinction is made between users with different mobility levels and bandwidth requirements to adjust bandwidth allocated to slow moving users with high bandwidth allocations [18]. To overcome these limitations, dynamic reservation schemes have been proposed where resource reservation is adaptive to the changes in network traf<sup>fi</sup>c conditions [30,34]. For example, the shadow cluster approach uses the user dynamics to pre-warn base stations of approaching users [27]. Knowledge about user mobility and user characteristics can be utilized in ef<sup>fi</sup>ciently allocating resources [44].

While the focus of most research in QoS for wireless networks has remained on resource utilization and managing call dropping probability, several related issues such as adaptation at the application level have also been addressed [28,17]. As the predictability in wireless network support cannot be completely ensured, mobile applications should be able to adapt to changing QoS support. Many schemes for bandwidth estimation have been suggested [5]. The effect of system degradation in wireless networks has been studied with respect to QoS, and two new user-perceived QoS metrics, degradation ratio and upgrade/degrade frequency have been proposed [10]. The algorithms for updating web pages in mobile devices during dis-connections from the web-server have been proposed in [21]. A model for <sup>fl</sup>exible QoS management suggests mobility predictive advanced bandwidth reservation, and bandwidth recon<sup>fi</sup>guration strategy [22].

Many other aspects of QoS in wireless have been studied. The QoS and resource allocation for multimedia traf<sup>fi</sup>c have been considered by [7,2]. To achieve scalability in providing QoS, a cluster approach is suggested rather than per-user call management [36]. The potential of seamless roaming in 3G/4G networks has led to the study of QoS in and across multiple heterogeneous wireless networks [39,3]. Robustness of components used in wireless architecture determine faulttolerance or dependability levels of networks for QoS support [40,42]. It has been shown that optimization of power control and base station assignment also affects resource management and QoS [35,43]. Application recovery when faced with frequent disconnections has been studied in the context of database operations [16]. Comparisons of various QoS schemes employed in wireless networks are also available [6,9,23].

A decision support system for wireless broadband network is presented in [37]. A design of reliable wireless network under capacity constraints by minimizing the connection cost is presented in [4]. A comprehensive discussion on decision support technology can be found in [38]. This also includes use of wireless in decision making. The use of quality of data is suggested in [11] for enhancing the mobile decision making. The authors propose a QoD model by considering mobile decision and a prototype for measuring the usefulness of the model. The use of QoS for selecting data networks for a company is proposed in [25] where the requirements are studied along with cost minimizing problem. The use of QoS in the Internet along with congestion-based pricing is addressed in [24]. An application driven approach to resource management in networks is presented in [26]. This is differentiated from the existing lower level resource reservation schemes. Several network con<sup>fi</sup>gurations are considered in studying QoS based pricing for the Internet in [15]. The authors concluded that a single network architecture with common higher QoS for all traf<sup>fi</sup>c was most desirable although at a higher cost. Several applications of emerging wireless networks are presented in [33], where QoS will affect how the applications are designed, adopted and utilized.

Seamless connections involving multiple wireless and wired networks have become possible because of the 3G networks. Therefore, it is important to have an overall mechanism to manage QoS for connections which involve different networks. A distributed QoS reference model has been proposed to reconcile the existing notion of quality of service at different system levels and among different network architectures in the wired Internet [20].

The research community has made extensive contributions in proposing individual QoS measures in wireless networks and on improving QoS support for various applications. This paper underscores the need for a unifying measure of QoS that would encompass various individual QoS metrics. We propose CQoS to be such a measure.

## 3. Composite quality of service (CQoS)

We propose that CQoS will include the three elements namely connection blocking probability, connection dropping probability, and utilization. Previous research has shown that there needs to be an effective trade-off between the utilization level and the connection blocking and connection dropping probabilities. The three QoS metrics can individually improve or deteriorate at the expense or bene<sup>fi</sup>t of the other competing metrics. Therefore, a composite measure of the Quality of Service must include these three elements. In this paper, we present a uni<sup>fi</sup>ed QoS metric which takes into account the elements of connection blocking probability, connection dropping probability and resource utilization. We call this metric CQoS.

We propose “CQoS” as a single unitary measure of “Quality of Service”. We de<sup>fi</sup>ne this QoS measure as a function of QoS of connection blocking, QoS of connection dropping, and bandwidth utilization. That is

$$
\mathrm{CQoS} = f \left(Q _ {\mathrm{b}}, Q _ {\mathrm{d}}, Q _ {\mathrm{u}}\right)\tag{2}
$$

The “CQoS” is de<sup>fi</sup>ned as a weighted average of the three separate QoS measures. Introducing respective proportionality constants $w _ { \mathrm { b } } ,$ $w _ { \mathrm { d } }$ and $w _ { \mathrm { u } }$ for $Q _ { \mathrm { b } } , Q _ { \mathrm { d } }$ and $Q _ { \mathrm { u } }$ respectively:

$$
C Q o S = w _ {b} \cdot Q _ {b} + w _ {d} \cdot Q _ {d} + w _ {u} \cdot Q _ {u}\tag{3}
$$

The values of weighted factors $w _ { \mathrm { b } } , w _ { \mathrm { d } } ,$ and $w _ { \mathrm { u } }$ can be based on the desired performance of the wireless network under given conditions of network traf<sup>fi</sup>c, user preferences etc. The <sup>fi</sup>rst case represents equal weight factors leading to the “CQoS ”. Because the weights of the three individual QoS measures are equal, this may be considered a “fair” measure of CQoS. Eq. (4) represents this case.

$$
W _ {\mathrm{b}} = W _ {\mathrm{d}} = W _ {\mathrm{u}}\tag{4}
$$

The second case is based on weighted factors biased in favor of call blocking probability leading to the “CQoS ”. This condition is appropriate where network would prefer higher quality of service with respect to call blocking. This situation is more suited for emergency scenarios such as disaster recovery scenarios where setting up of connection is a critical attribute even if the connection has to be dropped later. Eq. (5) represents this case.

$$
W _ {\mathrm{b}} > W _ {\mathrm{d}}, W _ {\mathrm{u}}\tag{5}
$$

The third case is based on weighted factors biased in favor of call dropping leading to the “CQoS ”. This condition is appropriate for typical mobile users and applications which would prefer better call dropping quality than call blocking probability. This scenario is very critical for applications that must be completed in one session such as <sup>fi</sup>nancial transactions. Eq. (6) represents this case.

$$
W _ {\mathrm{d}} > W _ {\mathrm{b}}, W _ {\mathrm{u}}\tag{6}
$$

The <sup>fi</sup>nal case is based on weighted factors biased in favor of network utilization leading to the $^ { \mathrm { 4 } } \mathrm { C Q } 0 0 \mathrm { S } _ { \mathrm { u } } ^ { \mathrm { ~ \tiny ~ " ~ } }$ . This condition is suitable for network providers who would prefer to ef<sup>fi</sup>ciently utilize the available bandwidth. Eq. (7) represents this case.

$$
W _ {\mathrm{u}} > W _ {\mathrm{b}}, W _ {\mathrm{d}}\tag{7}
$$

The four scenarios represented by Eqs. (4)–(7) were analyzed by <sup>fi</sup>rst simulating a case study network scenario under different conditions and then deriving measures of CQoS. The methodology is discussed in Section 5.

## 4. Decision support for quality of service

In this section, we show how various decisions must be made at different levels in wireless networks. These decisions are required to support the desired quality of service for different users.

More speci<sup>fi</sup>cally, decisions are made at user level, device level, connection level, base station level, network level and multi-network level (Fig. 1). At user level, this includes selecting an application and attempting to establish a connection. The selection of an application is made by the user and the quality of service required may vary from application to application. In general, the selection of an application will eventually result in some resources that network must allocate and in some cases the quality of service of the application may require substantial resources, thus affecting how many users the network may be able to support (scalability). The connection attempt will be made by a user/application and network will try to establish the connection involving two (unicast) or more than two (multicast) users in potentially multiple locations. If not successful, the user/application could request connection setup at a later instant at the same location or at another location if user has moved away in the wireless network. It is possible that a later connection attempt will be successful as (a) if the particular user remains at the same location, other users may have moved to another location or many existing connections may have been completed and (b) if the user moves to another location, the new location may have a fewer on-going connections.

![](/api/attachments/6CYAETP8/fulltext/images/89f07300d3a9e2df97bb3ccef2f68301c011f56b6997096866919639fdee41b1.jpg)  
Fig. 1. Decision framework of QoS in wireless networks

```txt
Decision level 1: decision making at user level
Selecting an application
Attempting to establish a connection, if not possible, trying later (in the same or another location due to mobility)
Attempting an adaptable application
```

The decision making at the device level involves selection of one of several wireless networks, such as cellular/PCS/GSM/3G, wireless LANs, satellites, or <sup>fi</sup>xed wireless networks, based on resources available in a wireless network and the required quality of service for application/user.

```txt
Decision level 2: decision making at device/connection level
Choosing a network for some QoS
Decide internal or external connection (or may be the network will decide this)
```

The decision making at base station level deals with how much bandwidth has been requested by an application/user, how much total bandwidth is assigned for new connections, and how much of that has already been allocated to the existing connections. Similarly, for continuing connections (users hand-of<sup>fi</sup>ng to the coverage of base station), the decisions involve how much bandwidth has been requested, how much total bandwidth is assigned for handoffs and new connections, and how much of the bandwidth has already been allocated to the new and continuing connections. Essentially, handoffs (or continuing connections) are prioritized over the new connections as a networklevel quality of service measure where the goal is to support all continuing connections (zero connection dropping) and minimize the blocking for new connections (minimal new connection blocking).

```txt
Decision level 3: decision making at base station level
A major decision on how much bandwidth to allocate to new connections and how much to handoff connections-could be based on desired QoS
for New connections do
    if BW-requested ≤(Total-New-Conn-BW-Allocated-BW-New-Conn) then
    Allocate BW-Requested
    Update Allocated-BW-New-Conn
    Update QoS Metrics
    Compute Utilization
    else
    Block the connection
    Update call blocking
end if
end for
for Handoffed connections do
    if BW-requested ≤((Total-Handoff-BW+Total-New-Conn-BW)-(Allocated-BW-New-Conn+Allocated-BW-Handoff-Conn) then
    Allocate BW-Requested
    Update Allocated-BW-Handoff-Conn
    Update QoS Metrics
    Compute Utilization
    else
    Block the handoff
    Update call dropping
end if
end for
for Connection termination do
    Update Allocated-BW-New-Connection or Allocated-BW-Handoff-Connection (depending on if the connection originated in the same cell or a different cell)
end for
```

<table><tr><td>Decision level 5: decision making at multi network level</td></tr><tr><td>Use Eq. (3) and decide on the values of different weightsDecide on how manage QoS (resources, QoS, pricing etc.)</td></tr></table>

![](/api/attachments/6CYAETP8/fulltext/images/25559b6c1165a0129455f4f5496df9a9c1e82f8e18fdd99aca9b6c6f596a5f65.jpg)  
Fig. 2. The case study heterogeneous wireless network model.

The decision making at the network level includes allocation of bandwidth for internal (all ends of a connection are in the same wireless network) as well as external connections (all ends of a connection are in different wireless networks).

Decision level 4: decision making at network leve

<table><tr><td>Allocation of bandwidth for internal and external connections</td></tr><tr><td>Computing network utilization (resources for both ends for internal and only one end for the external connections)</td></tr></table>

Decision making at multi-network level involves managing QoS across multiple networks and creating pricing/billing for the requested/achieved quality of service for both unicast and multicast connections.

## 5. Methodology, results, and analysis

We have used simulation modeling as the methodology to compute, evaluate and validate the proposed CQoS metric in wireless networks. We provide qualitative analysis of the results obtained from the simulations. Furthermore, we also present qualitative discussion of the implications of CQoS for users, network providers etc.

Numerous architectures are possible for simulating heterogeneous wireless networks. We have used a case study approach whereby a heterogeneous wireless network comprising of two cellular networks was simulated. The case study network model is shown in Fig. 2.

A simulation model developed for QoS research was extended to compute CQoS in this paper [1]. The discrete event model has been developed using C++ programming language and is capable of dynamically allocating resources to connections during connection admission and connection handoff events in multiple heterogeneous wireless networks. The model is <sup>fl</sup>exible and scalable in terms of varying type and number of networks, number of users, internal and external connections, and various traf<sup>fi</sup>c parameters.

The model supports bandwidth allocation to users with internal connections, and/or external connections involving one or more networks. The type of connections is classi<sup>fi</sup>ed as internal connections and external connections. An internal connection is de<sup>fi</sup>ned as the connection in which both ends are located within the same network. An external connection is de<sup>fi</sup>ned as one where two users are located in separate networks. Multi-level and continuous mobility is also supported in the model. A derivation of “random walk mobility model” was used [8]. The multi-network simulation can be done to evaluate QoS under varying traf<sup>fi</sup>c conditions, mobility, and number of users. Although this study assumes unicast connections with symmetric bandwidth requests and allocation, the model can be extended to include multicast connections and asymmetric bandwidth allocation. A simple step-by-step illustration of the simulation model is provided in Table 1.

## 5.1. Performance evaluation

We used simulations to obtain QoS metrics in the heterogeneous wireless network described in the case study scenario. The results so obtained were then used to derive CQoS. We now discuss the simulation modeling setup.

Traf<sup>fi</sup>c levels were manipulated by varying mean time between two simultaneous connections, mean duration of connections, and mean number of users in a location. The users were assumed to be mobile and moving at variable speeds. That ${ \mathrm { i } } s ,$ mobility of a user is characterized by couplet variables (speed, direction). The mobility was controlled for every individual user in the network. The resources in each of the wireless networks could be varied independently and exclusively. That is, the bandwidths available in the networks and the bandwidths requested by the connections could be controlled independently.

## Table 1

Treatment of simulation data for desirability semantics

<table><tr><td>Events</td><td>Events details/steps</td></tr><tr><td>Simulation parameters</td><td>Number of users, inter-arrival interval and holding times of calls, average time to cross-over (mobility), number and types of wireless networks and their resources, network traffic characteristics (local vs external)</td></tr><tr><td>QoS metrics</td><td>Connection blocking and drop rate system utilization, efficiency of resource allocation</td></tr><tr><td>Event: getting inputs</td><td>Assign network parameters and constantsSelect distributions for calls, and handoffs, and continuous mobility</td></tr><tr><td>Event: generating traffic</td><td>Initialize networks, cells, and users in different locations and schedule first connections, handoffs and mobility levels.Initialize location registers and store users&#x27; locations.</td></tr><tr><td>Event: call arrival</td><td>For an internal connection, check if the resources are available in the cells where users are located.If yes, set up the connection and allocate requested resources according to RA scheme used. Schedule the connection termination event. Update the available resources in the affected locations.For external connections, check if all involved networks have required amount of resourcesIf yes, set up the connection and allocate requested resources according to RA scheme used.</td></tr><tr><td>RA scheme 1 connection level event: handoff</td><td>Process handoffIf the user involved in a transaction, use prioritized allocation of resources</td></tr><tr><td>Event: call termination</td><td>Release resources at all the locations used in the connection Update QoS metrics</td></tr><tr><td>Event: post processing</td><td>Process and output QoS metrics</td></tr></table>

In heterogeneous wireless networks, internal connections are those which involve users that are located in the same network. External connections are those in which the users are located in different networks. The nature of network traf<sup>fi</sup>c characterized by ratio of internal to external connections was controlled through the parameter “probability of internal connections”.

The nominal values of various user, cell, and network parameters used in conducting the performance evaluation are shown in Table 2. The results shown in the paper are obtained by modeling unicast connections having symmetrical bandwidth requirements. Connection blocking and connection drop probabilities were measured as individual metrics of QoS. Network utilization was measured as the ratio of sum of average bandwidths allocated to the users in all cells by the total bandwidth available to the network. In this section, we present three sets of results which show the effect of connection interarrivals, connection durations, and number of users on individual QoS metrics and on CQoS.

Individual QoS metrics of connection blocking $( Q _ { \mathrm { b } } ) ,$ connection dropping $( Q _ { \mathrm { d } } ) ,$ , and utilization $\left( Q _ { \mathrm { u } } \right)$ were obtained directly from the simulation results (see Eq. (3)). Then, CQoS measures were computed using Eq. (3). CQoS measures were derived for the four scenarios represented by $\mathsf { C Q o S } _ { \mathrm { f } } , \mathsf { C Q o S } _ { \mathrm { b } } , \mathsf { C Q o S } _ { \mathrm { d } } ,$ and $\mathsf { C Q o o S } _ { \mathrm { u } }$ discussed in Section 3. For illustration purposes, the arbitrary values of weights $( w _ { \mathrm { b } } , w _ { \mathrm { d } } ,$ and $w _ { \mathrm { u } } )$ were used to represent the four scenarios as shown below. CQoS for fair scenario was computed using Eq. (8).

$$
C Q o S _ {f} = \frac {1}{3} \cdot Q _ {b} + \frac {1}{3} \cdot Q _ {d} + \frac {1}{3} \cdot Q _ {u}\tag{8}
$$

Where $\begin{array} { r } {  { w _ { \mathrm { b } } } =  { w _ { \mathrm { d } } } =  { w _ { \mathrm { u } } } = \frac { 1 } { 3 } . } \end{array}$ CQoS for the scenario where QoS of connection blocking is preferred is computed using Eq. (9).

$$
C Q o S _ {b} = \frac {1}{2} \cdot Q _ {b} + \frac {1}{4} \cdot Q _ {d} + \frac {1}{4} \cdot Q _ {u}\tag{9}
$$

Where $\begin{array} { r } { W _ { \mathrm { b } } = \frac { 1 } { 2 } , W _ { \mathrm { d } } = W _ { \mathrm { u } } = \frac { 1 } { 4 } . } \end{array}$ CQoS for the scenario where QoS of connection dropping is preferred is computed using Eq. (10).

$$
C Q o S _ {d} = \frac {1}{4} \cdot Q _ {b} + \frac {1}{2} \cdot Q _ {d} + \frac {1}{4} \cdot Q _ {u}\tag{10}
$$

Where $\begin{array} { r } { { w _ { \mathrm { d } } } = \frac { 1 } { 2 } , { w _ { \mathrm { b } } } = { w _ { \mathrm { u } } } = \frac { 1 } { 4 } . } \end{array}$ . CQoS for the scenario where QoS of utilization is preferred is computed using Eq. (11).

$$
C Q o S _ {u} = \frac {1}{4} \cdot Q _ {b} + \frac {1}{4} \cdot Q _ {d} + \frac {1}{2} \cdot Q _ {u}\tag{11}
$$

Where $\begin{array} { r } {  { w _ { \mathrm { u } } } = \frac { 1 } { 2 } ,  { w _ { \mathrm { b } } } =  { w _ { \mathrm { d } } } = \frac { 1 } { 4 } . } \end{array}$ . The terms $ { Q _ { \mathrm { b } } } ,  { Q _ { \mathrm { d } } }$ and $Q _ { \mathrm { u } }$ in the above equations refer to QoS components for connection blocking, connection dropping, and utilization respectively. The simulation model provides corresponding variables of connection blocking probability, connection dropping probability, and utilization. In order to use these observed variables in Eqs. (8)–(11), two step treatment was required. In the <sup>fi</sup>rst step, the values were adjusted so that they have similar directional semantics in terms of QoS or simply the quality. For example, an increase in value should mean increased QoS for all the three QoS components. In the second step, the three components were normalized. This was necessary because simulation measures yield absolute values of the individual QoS components. Absolute values can be used as-is if the QoS components are to be analyzed individually. But because they are to be included in one single expression, they should have a common level of reference. To achieve a common reference level, normalization of the three QoS components was necessary. This two-step data manipulation is explained next for one set of values.

Typical values of parameters used in the simulation model

<table><tr><td>Parameter</td><td>Typical value</td></tr><tr><td>Probability of internal call in Network A</td><td>0.5</td></tr><tr><td>Probability of internal call in Network B</td><td>0.5</td></tr><tr><td>Mobility (average time to handoff)</td><td>60 s</td></tr><tr><td>Average duration of connection</td><td>60 s</td></tr><tr><td>Number of users in each cell</td><td>70</td></tr><tr><td>Bandwidth of cells in Networks A and C</td><td>10</td></tr></table>

Treatment of simulation data for desirability semantics

<table><tr><td> $C_{ia}$ </td><td> $Q_b'$ </td><td> $Q_d'$ </td><td> $Q_u$ </td><td> $Q_b$ </td><td> $Q_d$ </td></tr><tr><td>300</td><td>0.5831</td><td>0.2613</td><td>0.6882</td><td>0.4169</td><td>0.7387</td></tr><tr><td>600</td><td>0.3906</td><td>0.1353</td><td>0.5917</td><td>0.6094</td><td>0.8647</td></tr><tr><td>900</td><td>0.2457</td><td>0.0858</td><td>0.5235</td><td>0.7543</td><td>0.9142</td></tr><tr><td>1200</td><td>0.1431</td><td>0.0562</td><td>0.4703</td><td>0.8569</td><td>0.9438</td></tr><tr><td>1500</td><td>0.0794</td><td>0.0339</td><td>0.4280</td><td>0.9206</td><td>0.9661</td></tr><tr><td>1800</td><td>0.0501</td><td>0.0220</td><td>0.3830</td><td>0.9499</td><td>0.9780</td></tr></table>

The <sup>fi</sup>rst step involves making the values of three individual QoS metrics consistent in terms of their directional semantics. We also de<sup>fi</sup>ne a term “Desirability Semantics” which refers to marginal improvement in quality with marginal increase in the absolute value of the metric. Simply stating, all three metrics should be consistent in their meaning of quality, if they are to be included in one expression. That is, an increase in value should represent increased QoS for all the three QoS components. In literature, connection blocking and connection dropping probabilities have been generally referred as QoS metrics but these are indirect representations of QoS. This is so because increased probabilities of call blocking and call dropping do not enhance the QoS but diminish it. In contrast, an increase in utilization $\left( Q _ { \mathrm { u } } \right)$ enhances the QoS. To be consistent with the existing literature, the simulation model provides call blocking (Q′) and call dropping Q<sub>d</sub>′ probabilities in response to changes in network conditions. Utilization $\left( Q _ { \mathrm { u } } \right)$ is modeled to measure the ratio of the bandwidth used to the bandwidth available. Because the CQoS expressions include the three QoS components, they have to be mathematically treated so that the derived variables are consistent with each other in their directional semantics. Given the discordance in directional semantics of the three variables, we derive “QoS of connection blocking” $( Q _ { \mathrm { b } } )$ as $Q _ { \mathrm { b } } { = } ( 1 { - } Q _ { \mathrm { b } } ^ { \prime } )$ and “Quality of connection dropping” $( Q _ { \mathrm { d } } )$ as $Q _ { \mathrm { d } } { = } \big ( 1 { - } Q _ { \mathrm { d } } ^ { \prime } \big )$ Table 3 shows the results of the mathematical treatment. Variable $C _ { \mathrm { i a } }$ represents average inter-arrival periods between connections, in seconds.

In the second step, values of QoS component metrics were normalized to make them suitable for inclusion in Eqs. (8)–(11). Normalization was necessary because the simulations provided absolute values of each QoS component without any common reference level. Because we are interested in analyzing relative effects of the three QoS components on CQoS, it is necessary that these variables have a common reference. The normalization was done based on the following heuristics. For each of the three components $( Q _ { \mathrm { u } } , \ Q _ { \mathrm { b } } ,$ and $Q _ { \mathrm { d } } ) ,$ their maximum values were considered as the respective base values and converted to unity (maximum QoS).

Normalization of QoS data

<table><tr><td> $C_{ia}$ </td><td> $Q_{bn}$ </td><td> $Q_{dn}$ </td><td> $Q_{un}$ </td></tr><tr><td>300</td><td>0.4388</td><td>0.7553</td><td>1.0000</td></tr><tr><td>600</td><td>0.6415</td><td>0.8841</td><td>0.8596</td></tr><tr><td>900</td><td>0.7940</td><td>0.9347</td><td>0.7606</td></tr><tr><td>1200</td><td>0.9020</td><td>0.9650</td><td>0.6832</td></tr><tr><td>1500</td><td>0.9691</td><td>0.9878</td><td>0.6218</td></tr><tr><td>1800</td><td>1.0000</td><td>1.0000</td><td>0.5564</td></tr></table>

Table 5 QoS Values

<table><tr><td> $C_{ia}$ </td><td> $CQoS_f$ </td><td> $CQoS_b$ </td><td> $CQoS_d$ </td><td> $CQoS_u$ </td></tr><tr><td>300</td><td>0.7240</td><td>0.6583</td><td>0.7374</td><td>0.7985</td></tr><tr><td>600</td><td>0.7872</td><td>0.7567</td><td>0.8174</td><td>0.8112</td></tr><tr><td>900</td><td>0.8215</td><td>0.8209</td><td>0.8561</td><td>0.8125</td></tr><tr><td>1200</td><td>0.8416</td><td>0.8631</td><td>0.8788</td><td>0.8084</td></tr><tr><td>1500</td><td>0.8510</td><td>0.8869</td><td>0.8917</td><td>0.8002</td></tr><tr><td>1800</td><td>0.8436</td><td>0.8891</td><td>0.8891</td><td>0.7782</td></tr></table>

The normalized values were obtained by dividing every observed value of a particular adjusted QoS metric by its base value. The base values are shown in bold in Table 3. The normalized values are presented in Table 4. Subscript $" \mathrm { n } "$ was added to the symbols of QoS metrics to denote normalized variables. Therefore $Q _ { \mathrm { u n } } , Q _ { \mathrm { b n } } ,$ and $Q _ { \mathrm { d n } }$ represent QoS of utilization, connection blocking, and connection dropping respectively.

Finally, using Eqs. (8)–(11), CQoS for various weighted factors were computed. These values are presented in Table 5. CQoS , CQoS , CQoS and $\mathsf { C Q o o S } _ { \mathrm { u } }$ represent CQoS for fair weighted, call blocking biased weighted, call dropping biased weighted, and utilization biased weighted respectively.

The normalized values of QoS metric components were then plotted to evaluate and analyze their individual sensitivities to the varying network conditions. This is because for a given set conditions, the three metrics have been converted to enable direct comparison with each other. Figs. 3 and 4 show the plots of individual QoS metrics and CQoS with respect to variations in connection inter-arrival times. These plots are based on Tables 4 and 5.

We now present the results under different network conditions, i.e. behavior of individual QoS components and CQoS with respect to connection inter-arrival times, connection durations, and number of users in the networks. The methodology discussed in the foregoing paragraphs was used in these scenarios. Unless otherwise speci<sup>fi</sup>cally mentioned, typical values shown in Table 2 were used in the simulation.

## 5.2. Variable inter-arrival

The performances of CQoS and individual QoS measures for varying call inter-arrivals are shown in Figs. 3 and 4. Call inter-arrivals are a function of the number of applications generated by users and represents average time duration between two adjacent calls. Consequently, increased inter-arrival represents a lower level of traf<sup>fi</sup>c in the network and therefore results is a fewer requests for resource allocation. Fig. 3 shows that QoS of call blocking $( Q _ { \mathrm { b n } } )$ and QoS of call dropping probabilities $\left( Q _ { \mathrm { d n } } \right)$ improve in response to increase in inter-arrivals between connections. Further, QoS of utilization $( Q _ { \mathrm { u n } } )$ deteriorates with increase in inter-arrival times between connections. This behavior is expected because lower traf<sup>fi</sup>c results in lower number of blocked and dropped connections but also lower level of utilization. The performance of CQoS is shown in Fig. 4. The CQoS biased in favor of QoS of call blocking and QoS of call dropping, i.e. $\mathsf { C Q o s S } _ { \mathsf { b } }$ and $\mathrm { C Q o S _ { d } }$ represented by Eqs. (9) and (10) respectively exhibit increased level of QoS with increasing inter-arrival times. In contrast, QoS of utilization represented by Eq. (11) exhibits a slight decrease in QoS levels with increased connection interarrivals. The fair CQoS scenario, i.e. CQoS represented by Eq. (8) also exhibits improved CQoS with increased values of connection interarrivals although the response is not as strong as exhibited by CQoS and $\mathrm { C Q o S } _ { \mathrm { u } } .$ This is because combined effect of $Q _ { \mathrm { b n } }$ and $Q _ { \mathrm { d n } }$ is greater than the effect of $Q _ { \mathrm { u n } }$ on the overall CQoS. Finally, by comparing Figs. 3 and 4 one can say that in general, the sensitivity of CQoS to changes in connection inter-arrivals is more moderate than in the case of individual QoS elements $( Q _ { \mathrm { b n } } , Q _ { \mathrm { d n } } ,$ and $Q _ { \mathrm { u n } } )$

![](/api/attachments/6CYAETP8/fulltext/images/b3ebd391970680b443c06fef5a11280cb259fea9fb48111bf1ae79d8b6057cf9.jpg)  
Fig. 3. QoS components as a function of connection arrivals.

![](/api/attachments/6CYAETP8/fulltext/images/441179dcaeb9cf492c0e05be50e4fc859134c23e6ae15d9bfc84f0d76207e99a.jpg)  
Fig. 4. CQoS as a function of connection arrivals.

## 5.3. Variable connection duration

The second set of results show the impact of connection duration on individual QoS components as well as on the CQoS (Figs. 5 and 6). Connection duration measures the average time applications stay in the network. Fig. 5 shows the effect of average connection duration on QoS of connection blocking, QoS of connection dropping and QoS of utilization components $( Q _ { \mathrm { b n } } , Q _ { \mathrm { d n } } ,$ and $Q _ { \mathrm { u n } } ) .$ . The connection blocking and connection dropping performances are best at applications with least connection durations and deteriorate as connections stay longer in the network. The utilization performance improves with increasing connection durations but the rate of improvement decreases for higher connection duration values. These results are as expected. Fig. 6 shows the effect of variation in connection durations on the CQoS. In general, the CQoS improves with increase in values of connection durations up to a certain level (about 100 s). Beyond this value of connection durations, the CQoS plots are generally <sup>fl</sup>at. This is explained by smaller dispersion between $Q _ { \mathrm { b n } } , Q _ { \mathrm { d n } } ,$ and $Q _ { \mathrm { u n } }$ (Fig. 5). Furthermore, the distribution of weights determine the best and the worst performing CQoS at any given value of connection duration, all other factors remaining the same. Therefore, this behavior can be taken into consideration by the decision module at the user/application level or at the base station level to regulate the overall QoS delivered by the system.

![](/api/attachments/6CYAETP8/fulltext/images/06da72b5630bb04b1f2667638aae3204e71cf83b43bb64ffecd31efc2133254d.jpg)  
Fig. 5. QoS components as a function of connection duration.

![](/api/attachments/6CYAETP8/fulltext/images/b9d313ed030f9dcaabca7b44624d32efc5f1acf97d82bb5be3a23f8a5838a4d9.jpg)  
Fig. 6. CQoS as a function of connection duration

## 5.4. Variable number of users

The base stations can determine the connection admission policies with respect to the number of users in their respective cells. The number of users admitted to the network will in<sup>fl</sup>uence the connection admission and connection dropping probabilities and the resource utilization. The impact of varying number of users in a cell on each of the three individual QoS components and on the CQoS are shown in Figs. 7 and 8 respectively. Fig. 7 shows relative performance of QoS of connection blocking, QoS of connection dropping and QoS of resource utilization as a function of average numbers of users in a cell. Fig. 7 shows a general pattern of a drop in levels of QoS associated with connection blocking and connection dropping and increase in QoS of resource utilization with increase in presence of higher number of users in a cell location. These results were expected. Fig. 7 shows the performance of CQoS as a function of number of users. For the four scenarios represented by Eqs. (9)–(11), Fig. 8 exhibits increased CQoS as the base station allows access to greater number of users. Fig. 7 shows that the slope of QoS of utilization plot $( Q _ { \mathrm { u n } } )$ is signi<sup>fi</sup>cantly greater than the plots of QoS of call blocking $( Q _ { \mathrm { b n } } )$ and QoS of call dropping $( Q _ { \mathrm { d n } } ) .$ . The in<sup>fl</sup>uence of $Q _ { \mathrm { u n } }$ on all CQoS plots in seen in Fig. 8.

![](/api/attachments/6CYAETP8/fulltext/images/405a677a41565b807726e2ea7ee9d31987a85c2461c6f7177967fbe57b9a2754.jpg)  
Fig. 7. QoS components as a function of users per cell.

![](/api/attachments/6CYAETP8/fulltext/images/c98d48bdb5f5c9980967049912c1b9cf1ea9ffbc2a9071e18a8ad63e351a2f84.jpg)  
Fig. 8. CQoS as a function of users per cell.

## 6. Implications of CQoS

In general, CQoS includes both user-centric QoS and networkcentric QoS and has the potential to result in a fair and optimal quality of service for both users and network service providers. As CQoS is implemented, it is likely to impact users, individual network providers and multi-network providers. The users have the incentive of paying less when the network is lightly loaded, while network service providers have the incentive of carrying more traf<sup>fi</sup>c using an improved traf<sup>fi</sup>c management during a high-load condition.

## 6.1. Implications for decision support model

The decision support models presented in Section 4 are based on allocation of available resources to the seeking mobile applications. For example, the decision making at the “base-station” level allocates bandwidth on “<sup>fi</sup>rst-come <sup>fi</sup>rst-serve” bases to the new and existing connections (Decision level 1). The CQoS paradigm suggests that various entities in the network can take into account the CQoS attributes in their decision models (Fig. 9).

![](/api/attachments/6CYAETP8/fulltext/images/dde1899c903069f2dd03d45b15f20f8b7d9da3a3ab48aacead25350296d78d7d.jpg)  
Fig. 9. Decision framework including CQoS.

We refer to Figs. 4, 6, and 8 in discussing implications of CQoS on decision support for various entities. Furthermore, we refer to the plots of $\mathrm { C Q o S _ { d } }$ and $\mathrm { C Q o S } _ { \mathrm { u } }$ in underscoring the usefulness of the CQoS paradigm. We do this because QoS of connection dropping and QoS of bandwidth utilization have been considered most signi<sup>fi</sup>cant from the context of users and networks respectively. In Fig. 4, for the given set of conditions, the plots of $\mathrm { C Q o S _ { d } }$ and $\mathrm { C Q o S } _ { \mathrm { u } }$ intersect close to connection inter-arrival times of about 600 s. Therefore, at this point of intersection or close to this point, the marginal rate of change of CQoS is least because the two plots diverge signi<sup>fi</sup>cantly on the either side. It follows, that the network seeking to balance the QoS elements of call dropping and utilization would prefer to operate close to this point of intersection between the two plots. If this were to be the objective of a network provider, the decision model at the network level could consider controlling inter-arrivals between connections either by permitting appropriate number of users or by offering a right mix of incentives or deterrence to users. A scheme of incentives/deterrence used by a network provider could in<sup>fl</sup>uence decision level at the user level.

Next, we consider the $\mathrm { C Q o S _ { d } }$ and $\mathsf { C Q o o S } _ { \mathrm { u } }$ plots in Fig. 6. In the given scenario, there is very little divergence between the CQoS biased in favor of connection dropping and bandwidth utilization. Therefore, a network seeking to balance the two CQoS metrics would want to operate in the region where call durations are greater than about 85 s. A decision level at the base station level could take this trade-off into consideration while assigning bandwidths when the demand for bandwidth exceeds its availability. If base stations have information about user pro<sup>fi</sup>les and their calling patterns, preference could be given to users who are more likely to establish connections greater than the established threshold value.

Finally we consider the CQoS plots in Fig. 8. In this scenario, there is signi<sup>fi</sup>cant divergence between the $\mathrm { C Q o S _ { d } }$ and $\mathrm { C Q o S } _ { \mathrm { u } }$ plots when the average number of active users per cell is low. The divergence shrinks as the number of users grow. The decision level at the network level can consider this behavior of CQoS to regulate the number of active users.

## 6.2. Implications for users

The QoS-based pricing could be part of future service level agreement and service level guarantee between wireless carriers and users. Such arrangements on pricing, network availability, charges for additional traf<sup>fi</sup>c, and credits if network cannot support the agreed level of performance are made between network carriers and companies, and could be extended to individual and group wireless users. No data is available to suggest that QoS based pricing models have been offered by operators. The pricing for mobile services, if dependent on CQoS, will also re<sup>fl</sup>ect the wireless network utilization. Thus users may pay different charges based on both QoS received and network load. This may give users incentive to use the services provided by the network and receive QoS when network is lightly loaded. The pricing also re<sup>fl</sup>ects more closely the dif<sup>fi</sup>culty for the wireless network under overload to provide the desired QoS for a user. This could lead to an unprecedented level of user-control of their traf<sup>fi</sup>c as users could prioritize their traf<sup>fi</sup>c based on its criticality and time-sensitiveness with the current charges. For implementation, we envision that mobile devices with intelligent features and software will be employed to assist users in such decision making by showing the current prices for desired levels of QoS, which will be updated with changes in location (accessing another wireless network), time (changes in network load), and resource requirement of mobile applications.

## 6.3. Implication for network service providers

CQoS leads to more complexity of decision making as network utilization will affect the level of processing required. However this would also result in an increased revenue for individual network providers. A CQoS based revenue generation and sharing among multiple providers will also re<sup>fl</sup>ect the “true” cost of providing QoS to users. This would lead to a higher probability that many emerging and sophisticated services, including resource-intensive mobile commerce, will be offered and supported by several network providers as their new set of revenues will re<sup>fl</sup>ect their actual cost in service provisioning.

In future many more factors must be considered and included in decision making for resource allocation to support CQoS. These will include how resources are allocated in individual wireless networks (connectionless vs connection-oriented), granularity of resource allocation (packet, transactions or connection level), QoS and traf<sup>fi</sup>c control policies of individual wireless networks, the ability of mobile applications to adapt to changing level of resources in different locations at different time, and, the interaction of an individual network policy with other networks in the end-to-end CQoS.

## 7. Conclusion

QoS support across multiple heterogeneous wireless networks is an important area as the future wireless networks are likely to support roaming across multiple wireless networks. Many of these networks will be heterogeneous in their resource availabilities and allocation. Most QoS research in the past has focused on various metrics of service quality. In this paper, we present the new concept of Composite QoS as a uni<sup>fi</sup>ed metric of quality-of-service. Furthermore, the end-to-end QoS is also affected by multiple decisions that are made by several different network entities for allocating resources and enforcing the network policies. This paper presents the decision making perspective for resource allocation in multiple heterogeneous wireless networks. The results show that composite QoS is very useful as it considers both user-centric QoS as well as network-centric resource utilization. We also presented a qualitative analysis of implications of Composite QoS on users and network service providers. We also show how the QoS ideas presented here can be used by wireless carriers for improved QoS support and management.

In this paper, we have used a case-study approach to simulate three scenarios to illustrate the CQoS paradigm. Furthermore, the weights assigned to re<sup>fl</sup>ect the CQoS bias in favor of the individual QoS components were also chosen to present the concept. Further research is possible in this area to establish a rigorous model of CQoS. Finally, we used a deductive approach in demonstrating the usefulness of CQoS in the decision models of various network entities. Future research could include the CQoS variables in considering bandwidth allocations at various levels. Next, the simulation model uses “random walk mobility model” with no feedback from the performance of the networks. The mobility model could be extended so that the user mobility could be informed by the network performance especially in a heterogeneous wireless scenario.

The future research can include designing “Decision Support Systems” for the current and future wireless networks, deriving changes in the revenues for individual and multi-network providers, studying user empowerment with composite QoS, designing novel business models for mobile services in heterogeneous wireless networks, and testing of composite QoS in real wireless networks. In this respect, the ideas presented in this paper should provide opportunities for future research to extend and/or re<sup>fi</sup>ne the CQoS model by including more variables for a more narrow range of applications and making it more rigorous. It is our hope that the paper can form the basis for a signi<sup>fi</sup>cant further research in DSS for emerging 3G/4G wireless networks supporting QoSfor a range of sophisticated user-centric mobile applications.

## References

[1] P. Ahluwalia, U. Varshney, Managing end-to-end quality of service in multiple heterogeneous wireless networks, International Journal of Network Management 17 (3) (2007) 243–260.

[2] N. Bartolini, Handoff and optimal channel assignment in wireless networks Mobile Networks and Applications 6 (6) (2001) 511–524.

[3] G. Bianchi, N. Blefari-Melazzi, P. Chan, M. Holzbock, Y. Hu, A. Jahn, R. Sheriff, Design and validation of QoS aware mobile internet access procedures for heterogeneous networks, Mobile Networks and Applications 8 (2003) 11-25

[4] I. Bose, E. Eryarsoy, L. He, Multi period design of survivable wireless access networks under capacity constraints, Decision Support Systems 38 (4) (Jan. 2005) 529–538.

[5] A. Capone, L. Fratta, F. Martignon, Bandwidth estimation schemes for TCP over wireless networks, IEEE Transactions on Mobile Computing 3 (2) (Apr. 2004) 129–143.

[6] D. Chalmers, M. Sloman, A survey of quality of service in mobile computing environments, IEEE Communication Survey 2 (2) (1999).

[7] H. Chen, Q.-A. Zeng, D.P. Agrawal, A novel analytical model for optimal channel partitioning in the next generation integrated wireless and mobile networks, Proceedings of the 5th ACM International Workshop on Modeling Analysis and Simulation of Wireless and Mobile Systems, 2002, pp. 120–127.

[8] K.-H. Chiang, N. Shenoy, A random walk mobility model for location management in wireless networks, 12th IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, vol. 2, Sept. 2001, pp. E–43.

[9] S. Choi, K. Shin, A comparative study of bandwidth reservation and admission control schemes in QoS-sensitive cellular networks, Mobile Networks and Applications 6 (2000) 289–305.

[10] C. Chun-Ting, K. Shin, Analysis of adaptive bandwidth allocation in wireless networks with multilevel degradable quality of service, IEEE Transactions on Mobile Computing 3 (1) (Jan. 2004) 5–17.

[11] J. Cowie, F. Burstein, Quality of data model for supporting decision making Decision Support Systems 43 (4) (2006) 1625–1683.

[12] S.K. Das, S.K. Sen, R. Jayaram, A dynamic load balancing strategy for channel assignment using selective borrowing in cellular mobile environment, Wireless Networks 3 (5) (1997) 333–347.

[13] S.K. Das, R. Jayaram, S.K. Sen, A call admission and control scheme for quality-ofservice (QoS) provisioning in next generation wireless networks, Wireless Networks 6 (2000) 17–30.

[14] S.O.M. El-Kadi, H. Abdel-Wahab, A rate-based borrowing scheme for QoS provisioning in multimedia wireless networks, IEEE Transactions of Parallel and Distributed Systems 13 (2) (Feb. 2002).

[15] P.C. Fishburn, A. Odlyzko, Dynamic behaviour of differential pricing and quality of service options for the Internet, Decision Support Systems 28 (1–2) (Mar. 2000) 123–136.

[16] S. Gadiraju, V. Kumar, Recovery in the mobile wireless environment using mobile agents, IEEE Transactions on Mobile Computing 3 (2) (Apr. 2004) 180–191.

[17] J. Gomez, A.T. Campbell, HAVANA: supporting application and channel dependent OoS in wireless packet networks Wireless Networks 9 (1) (2003) 21–35

[18] A. HaC, A. Armstrong, Resource allocation scheme for QoS provisioning in microcellular networks carrying multimedia traf<sup>fi</sup>c, International Journal of Network Management 11 (5) (2001) 277–307.

[19] D. Hong, S. Rappaport, Traf<sup>fi</sup>c model and performance analysis for cellular mobile radio telephone systems with prioritized and non-prioritized handoff procedures, IEEE Transaction on Vehicular Technology 35 (Aug. 1986) 77–92.

[20] D.W.-K. Hong, C.S. Hong, A QoS management framework for distributed multimedia systems, International Journal of Network Management 13 (2) (2003) 115–127.

[21] C. Ing-Ray, A.P. Ngoc, Y. I-Ling, Algorithms for supporting disconnected write operations for wireless web access in mobile client–server environments, IEEE Transactions on Mobile Computing 1 (1) (Jan, 2002) 46–58

[22] Y. Jian, H. Jiongkuan, S. Papavassiliou, A comprehensive resource management framework for next generation wireless networks. IEEE Transactions on Mobile Computing 1 (4) (Oct. 2002) 249–264.

[23] W. Jingao, Z. Qing-An, D. Agrawal, Performance analysis of a preemptive and priority reservation handoff scheme for integrated service-based wireless mobile networks, IEEE Transactions on Mobile Computing 2 (1) (Jan. 2003) 65-65.

[24] B. Jukie, R. Simon, W.S. Chang, Congestion based resource sharing in multi-service networks, Decision Support Systems 37 (3) (Jun. 2004) 397–413.

[25] N. Kasapa, H. Aytug, S. Selcuk Erenguc, Provider selection and task allocation issues in networks with different Qos levels and all you can send pricing, Decision Support Systems 43 (2) (2007) 375–389.

[26] M.J. Katchabaw, H.L. Lut<sup>fi</sup>yya, M.A. Bauer, Driving resource management with application-level quality of service speci<sup>fi</sup>cations, Decision Support Systems 28 (1–2) (Mar. 2000) 71–87.

[27] D.A. Levine, I.F. Akyildiz, M. Naghshineh, A resource estimation and call admission algorithm for wireless multimedia networks using the shadow cluster concept, IEEE/ACM Transactions on Networking 5 (1) (Feb. 1997).

[28] R.R.-F. Liao, A.T. Campbell, A utility-based approach for quantitative adaptation in wireless packet networks, Wireless Networks 7 (5) (2001) 541–557.

[29] M. Naghshineh, A.S. Acampora, QoS provisioning in micro-cellular networks supporting multiple classes of traf<sup>fi</sup>c, Wireless Networks 2 (3) (1996) 195–203.

[30] M. Naghshineh, M. Schwartz, Distributed call admission control in mobile/wireless networks, IEEE Journal on Selected Areas in Communications 14 (4) (May 1996).

[31] A. Nagshineh, M. Acampora, QoS provisioning in micro-cellular networks supporting multiple classes of traf<sup>fi</sup>c, Mobile Networks and Applications 2 (3) (Aug. 1996) 195–203.

[32] M. Naghshineh, M. Willebeek-LeMair, End to end QoS provisioning multimedia wireless/mobile networks using an adaptive framework, IEEE Communications Magazine 35 (11) (Nov. 1997) 72–81

[33] E. Ngai, A. Gunasekaran, A review of mobile commerce research and applications, Decision Support Systems 43 (2) (Feb. 2007) 3–15.

[34] C. Oliveira, J. Kim, T. Suda, An adaptive bandwidth reservation scheme for high speed multimedia wireless network, IEEE Journal on Selected Areas in Communications 16 (6) (Aug. 1998) 858–874.

[35] L. Papavassiliou, L. Tassiulas, Joint optimal channel, base station and power assignment for wireless access, IEEE/ACM Transactions on Networking 4 (6) (Dec. 1996) 857–872.

[36] B. Sadeghi, E. Knightly, Architecture and algorithms for scalable mobile QoS, Mobile Networks and Applications 9 (2003) 7–20

[37] K.P. Scheibe, L.W. Cartensen, T.R. Rakes, L.P. Rees, Going the last mile: a spatial decision support system for wireless broadband communications, Decision Support Systems 42 (2) (2006) 557–570.

[38] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsaon, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (Jun. 2002) 111–126.

[39] M. Stemm, R.H. Katz, Vertical handoffs in wireless overlay networks, Mobile Network Applications 3 (4) (1999) 335–350.

[40] D. Tipper, T. Dahlberg, H. Shin, C. Charnsripinyo, Providing fault tolerance in wireless access systems, IEEE Communications Magazine 40 (1) (Jan. 2002) 58–64.

[41] U. Varshney, R. Vetter, Emerging mobile and wireless networks, Communication of the ACM 43 (6) (Aug. 2000) 73–81.

[42] U. Varshney, A. Malloy, Introducing multi-level fault-tolerance for highly dependable wireless networks, Hawaii International Conference on System Sciences, IEEE Computer Society Press, Jan. 2003.

[43] R. Yates, C. Huang, Integrated power control and base station assignment, IEEE Journal on Vehicular Technology 44 (3) (Aug. 1995) 1–7.

[44] J. Ye, J. Hou, S. Papavassiliou, Comprehensive resource management framework for next generation wireless networks, IEEE Transactions on Mobile Computing 1 (4) (2002) 249–264.

Punit Ahluwalia is currently an assistant professor in the department of Computer Information Systems and Quantitative Methods at the University of Texas — Pan American. Punit Ahluwalia received his PhD degree in Computer Information Systems from Georgia State University, Atlanta in 2006. He also has graduate degrees in Computer Information Systems and Management and Systems from Georgia State University and IIT Delhi respectively. He received his undergraduate degree in Electrical Engineering from Regional Engineering College, Kurukshetra, India (now National Institute of Technology, Kurukshetra). His research interests include wireless networks, mobile transactions, QoS, and mobile commerce. He is also interested in behavioral and social issues arising out of implementation of wireless networks. He has authored several journal and conference papers and is a winner of the college teaching award. He is a member of IEEE, ACM, and Association of Information Systems (AIS).

Upkar Varshney received BE in Electrical Engineering from University of Roorkee (now IIT-Roorkee) in 1988, MS in Computer Science and PhD in Telecommunications and Networking in 1992 and 1995, respectively, from University of Missouri-Kansas City. Since 1998 Upkar Varshney is on the faculty of CIS at Georgia State University and is currently Associate Professor. His research interests include wireless networks, pervasive healthcare, and mobile commerce. He is the author of 110 journal and conference papers and among the most cited author in wireless and mobile commerce. He has also received several grants and numerous teaching awards at GSU. He is the cofounder and chair of International Pervasive Health Conference. He has been an editor/ guest editor for ACM/Kluwer MONET, IEEE Computer, Communications of the AIS (CAIS), International Journal on Network Management (IJNM), and Int. Journal on Mobile Communications (IJMC). He is a member of IEEE, ACM, and Association of Information Systems (AIS)
