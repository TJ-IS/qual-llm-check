---
otero_id: 6932
otero_key: "42WMWUX9"
title: "Network reliability based decision of Internet with multiple sources and multiple sinks"
authors: "Yi-Kuei Lin; Louis Cheng-Lu Yeng"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.018"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Network reliability based decision of Internet with multiple sources and multiple sinks

Yi-Kuei Lin ⁎, Louis Cheng-Lu Yeng

Department of Industrial Management, National Taiwan University of Science & Technology, Taipei 10607, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 23 April 2012 Received in revised form 12 December 2012 Accepted 14 December 2012 Available online 23 December 2012

Keywords: Light path (LP) Submarine cable Network reliability Multiple sources Multiple sinks Stochastic-<sup>fl</sup>ow network (SFN)

## a b s t r a c t

In a network system, decision makers always require appropriate tools for arranging the placement and timing of resources, whether in the construction or maintenance stage. The reliability evaluation is a fundamental issue that supports decisions made by the managers concerning enhancements to the system infrastructure. This paper proposes a modi<sup>fi</sup>ed stochastic-<sup>fl</sup>ow network model to evaluate the network reliability of the Internet where data is transmitted through several light paths. Network reliability is de<sup>fi</sup>ned as the probability that the maximal <sup>fl</sup>ow is not less than a speci<sup>fi</sup>ed threshold. It is regarded as a performance index for measuring the service level of a communication network from the perspective of quality of service (QoS). This study focuses on the network reliability of a practical system, Taiwan Advance Research and Education Network (TWAREN), which is Taiwan's academic research network that provides mainly network communication services for Taiwan's research and academic society. An algorithm based on a new technique, minimal light path (MLP), is proposed to evaluate the network reliability of TWAREN's international scope. The supervisor can subsequently use the analysis results to improve the reliability of the entire system and make better decisions.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In computer networks, operations research, business, and other <sup>fi</sup>elds, decision makers always require appropriate tools or organized knowledge to arrange the placement and timing of acquired resources. For network systems, in particular international connections, the resources are limited and cost-oriented, and its infrastructure relies heavily on the decision making support tools whether in the construction or maintenance stage. Decisions may concern the selection of interconnections for Internet service providers (ISP), locations of routers or routing decisions for the entire network system, or the assignment of a variety of other resources. It is important that the manager identi<sup>fi</sup>es useable tools that are required to make suitable decisions for the network infrastructure. The quality of service (QoS) is a critical task when seeking to realize the performance of an actual network system, and is a good tool to help the decision makers to improve the system. The subject of the QoS [4,8,25] of systems has been extensively studied for the past few decades. The QoS indicates the ability of the network to provide a consistent and predictable data transfer service that satis<sup>fi</sup>es customers applications, and a network reliability analysis is essential to maximize the use of network resources. In this area, the most classical network reliability research is known as the source-sink network reliability issue [1,3,9,12,14,17–19,21–23,26,34], which some literatures name two-terminal network reliability (TTNR) [9,26]. A TTNR analysis is capable of calculating the network reliability in terms of the linking paths between two speci<sup>fi</sup>c nodes, commonly known as the source-sink. Other researchers extend the research of TTNR to problems that contain at least one path from the source node to other k nodes, also named the k-terminal network reliability (KTNR) issue [15,33]. Apart from the TTNR and KTNR, there is a problem of calculating the probability that every node in the network is connected to each other [20,27], which is called all-terminal network reliability (ATNR) problem (also named uniform or overall network reliability).

In a realistic system, the edges (or arcs) should have different capacities or states, and this kind of network is called a stochastic <sup>fl</sup>ow network (SFN) or multi-state <sup>fl</sup>ow network [1,3,12,14,17–21,23,30,31,34]. In particular, when the capacity of each edge has two levels (0 and a positive integer), it is called a binary-state <sup>fl</sup>ow network. However, TTNR, KTNR, and ATNR problems are discussed for binary-state <sup>fl</sup>ow networks, and this paper will focus on the network reliability for a revised SFN with multiple sources and multiple sinks.

The major function of Taiwan's academic research network, which is called the Taiwan Advanced Research and Education Network (TWAREN) [28], is to provide a communication service for Taiwan's academic and research community. TWAREN's international segment provides a channel to connect Taiwan to the United States via the Asia-Paci<sup>fi</sup>c region's land surface and submarine cable, as shown on the international logic map in Fig. 1. Since TWAREN has limited resources (or bandwidth), it is important to identify a technique that optimizes its utilization and performance. The major aim of Taiwan's National High Performance Computing Center (NCHC) is to enhance its infrastructure and network management skills, and one of the methods to achieve this goal is the adoption of ef<sup>fi</sup>cient evaluation and supporting techniques to realize TWAREN's performance. Network reliability analysis, which can be used to support managers to make decisions, is a technique that is useful for the assessment of TWAREN's performance. Practical transmission media, such as <sup>fi</sup>ber optics or coaxial cables, which are wired into the communication system, may be regarded as edges, and transmission facilities, such as switches or routers, may be deemed to be nodes (or vertices). To avoid the possibility of system failure, partial disablement or maintenance, the capacity of each edge should be stochastic. Therefore, a network system with such edges also has stochastic capacities is a typical SFN. This has been studied as a performance index to evaluate the network reliability of a SFN in the past couple of decades, and most of these studies examined network reliability from a source node to a sink node by means of minimal paths (MP), where an MP is a path with proper subsets which are no longer paths [17,18,21,23,34]. This means that, from the perspective of the network topology, an MP is a set of edges and nodes that links a source-sink pair, here not limited to one source-sink pair, without any surplus edges.

![](/api/attachments/42WMWUX9/fulltext/images/659ec586e5a9a8359d672deec8edacef508021b4198103b442ab15445cca3822.jpg)  
Fig. 1. TWAREN international logic map between Taiwan and U.S.<sup>a,b</sup>. <sup>a</sup>The Pwave, STARLight, ManLAN, Telehouse and Equinix are the ISP in U.S. that integrated by CHT. <sup>b</sup>ONS devic is Cisco network equipments.

Previous literatures suppose that data can be delivered through all MP from a source to a sink in accordance with the network infrastructure, where each MP is organized by some physical lines (PL). In fact, in a realistic system, data could simply be delivered in terms of some light paths (LP) and tunnel between two speci<sup>fi</sup>c nodes, in which an LP is a virtual tunnel between two end-to-end nodes which is composed of some segments (i.e. edges) and nodes. An LP is a link between any two nodes (not limited to a source-sink pair), but an MP is a path that only connects two speci<sup>fi</sup>c source and sink pairs. In other words, data can be transmitted from a source node to a sink node through at least one LP. That is, any segment that the LP goes through cannot be divided during transmission through any of its edges or nodes. Therefore, previous literatures [17,18,21,23,34] based on MP to deliver data are not suitable for TWAREN. Each LP in TWAREN is composed of a set of light path segments (LPS) linking two nodes. Particularly, each PL of a realistic network can be divided into several LPS, and each LPS belongs to only one LP. This characteristic of LP is indivisible through any part of its nodes or edges during transmission in TWAREN, so this kind of network pattern is different with the MP described in [17,18,21,23,34]. Therefore, in order to evaluate TWAREN's network reliability, a minimal light path (MLP) concept is developed to <sup>fi</sup>nd all LP. An MLP is de<sup>fi</sup>ned as a series of nodes and LPSs from a source node to a sink node that includes no cycle.

A revised SFN with multiple sources and multiple sinks is constructed herein to demonstrate the TWAREN in terms of LP. First, this paper addresses a two-source and two-sink case for convenience. A general case with multiple sources and multiple sinks can be extended easily by the proposed algorithm. Subsequently, the network reliability of the international scope of TWAREN can be assessed, the tunnel of which is mainly linked to the worldwide academic research society, especially the Internet2 Network [13] in the United States. TWAREN's international infrastructure is provided by Taiwan's largest ISP, Chunghwa Telecom (CHT) [6]. CHT integrates those ISP that the cables pass through to organize the whole international portion of TWAREN in two areas: on the land surface of both Taiwan and the United States, and in the under-sea areas of the Asia Paci<sup>fi</sup>c, including the Japan-US submarine cable that was disconnected when it was hit by the earthquake and tsunami in Japan on March 11, 2011. Nakagawa [24] mentioned the in<sup>fl</sup>uence of the earthquake regarding reliability, so the affect of this disaster is studied here as well. As a matter of fact, when a line break occurs, the ISP of these pass-through cables will offer serviceable lines as backups to achieve the service level; therefore they provide some degree of network reliability. This study only concentrates on the regular lines to determine the factors that in<sup>fl</sup>uence TWAREN's network reliability, which is the main task of NCHC. Apart from improving TWAREN's overall performance, the major factors which could fail the regular lines are anticipated. However, the problem of the network reliability of the backup cables [2,5,10,11,30] has not been considered yet. Only after analysis of the regular lines' performance, then we can make further decision to construct better backup lines' structure.

This paper mainly evaluates the network reliability with which the network can deliver speci<sup>fi</sup>ed units of data from multiple sources (Taipei city and Hsinchu city) to multiple sinks (New York and Chicago) through TWAREN's LP. The remainder of this paper is organized as follows: The TWAREN is introduced in Section 2. The research scope, problem formulation, concept of the MLP and the evaluation technique, recursive sum of disjoint products, (RSDP [34]) are all described in Section 3. The network reliability of TWAREN is evaluated in Section 4, and a conclusion and discussion are presented in Section 5.

## 2. TWAREN network

## 2.1. Introduction to TWAREN

TWAREN has been funded by the National Science Council of Taiwan since 1998 and was built and organized by the NCHC. Construction was completed at the end of 2003 and service and operation started in 2004. Today, more than 100 academic and research institutions connect with TWAREN in Taiwan and this number is increasing continuously. As well, since 2005, over 1000 elementary schools and junior and senior high schools have been using TWAREN's internal backbone. TWAREN provides network infrastructure for general use but is also an integrated platform for network research. For instance, TWAREN was instrumental in developing applications and network technology such as IPv6, MPLS, VoIP, e-learning, multicast, multimedia and performance measurement, and has supported GRID and cloud computing applications such as e-Learning Grid, Medical Grid, and EcoGrid. As promoting Taiwan to be an international R&D center is one of NCHC's objectives, a stable and reliable TWAREN is the foundation to achieve this goal.

Many countries fund national research and education network (NREN) infrastructure. TWAREN, Taiwan's NREN, connects to the international research community through global advanced networks, specifically the Internet2 Network [13] of the United States, the major NREN in the world. Therefore, network reliability analyses of TWAREN will help to continuously improve its infrastructure so it can continue to cooperate and connect globally.

## 2.2. Light path of TWAREN

The Internet portion of TWAREN is a network that connects to the world-wide research network through LP. Any segment that the LP goes through cannot be split during transmission through any of its edges or nodes. Each LP consists of a set of LPS linking two nodes. Each PL of a realistic network can be divided into many LPS, and each LPS belongs to only one LP. TWAREN's physical topology is an optical infrastructure and its virtual topology is constructed by connecting LP and routers which are organized by CHT. An LP is a tunnel between two sites connected by various cables and is an end-to-end, pre-allocated optical network resource, according to users' needs. It allows signals to be delivered sequentially without jitters and congestion. Each LP is generally a

155-Mb–10-Gb dedicated channel that transports various applications and needs. These LP are pre-assigned by CHT for achieving better economic effect in the optical infrastructure instead of designing by NCHC. That is, the validation of LP depends on the disconnection rate of optical cable that it locates.

Fig. 2 is the LP international infrastructure that TWAREN leases from CHT, including major sites located at Taipei and Hsinchu in Taiwan, as well as Los Angeles, Chicago, and New York in the United States. This infrastructure contains the land surface and submarine cable within these cities which leased and designed by CHT. Each LP is denoted by $L P _ { i }$ where $i = 1 , 2 , . . . ,$ l with l being the number of LP. Most of these city sites connect to each other with 2.5 Gb PL connections, which divided into four LP channels at 622 Mb bandwidths. The research scope of this paper is to study the network reliability of the transmission from multiple sources (Taipei city and Hsinchu city) to multiple sinks (New York and Chicago) by means of the LP tunnel.

## 3. Problem description and model formulation

## 3.1. Problem description

This paper describes how the probability that a speci<sup>fi</sup>ed amount of data, here called demand level, can be sent from Taipei city and

![](/api/attachments/42WMWUX9/fulltext/images/c2532e0edde08632b740dd14c450cb05c710ce034496bf482da48872e4e0408e.jpg)  
Fig. 2. TWAREN's light path between Taiwan and the U.S.

Hsinchu city to New York and Chicago via TWAREN, is measured. This is referred to as network reliability. Also, Fig. 2 is transformed into Fig. 3 which is constructed by the LPS and nodes.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Notations
$s_1; s_2$ source 1; source 2
$t_1; t_2$ sink 1; sink 2
$p$ number of nodes
$v_k$ kth node, $k=1,2,...,p$ $l$ number of light paths
$LP_i$ ith light path, $i=1,2,...,l$ $c$ number of PL
$P_i$ ith PL, $i=1,2,...,c$ $r_i$ number of LPS in $LP_i$ $l_{i,j}$ jth LPS in $LP_i$, $j=1,2,...,r_i$ $n$ total number of LPS
$e_i$ alternate expression of $l_{i,j}$, relabel all LPS as $e_1$, $e_2$, ..., $e_n$ $E$ $\{e_i| 1 \leq i \leq n\}$: the set of LPS
$V$ set of nodes
$M^i$ (an integer) the maximum capacity of LPS $e_i$, $i=1,2,...,n$ $M$ ($M^1$, $M^2$, ..., $M^n$)
$G$ ($E$, $V$, $M$): a stochastic flow network
$ml_j$ all MLP from $\{s_1, s_2\}$ to $\{t_1, t_2\}$, $j=1,2,...,r+q$ $x_i$ the current capacity of $e_i$ $X$ ($x_1$, $x_2,...,x_n$): capacity vector
$f_j$ the current flow on $ml_j$, $j=1,2,...,r+q$ $F$ ($f_1$, $f_2,...,f_{r+q}$): flow vector
$d_1; d_2$ demand at $t_1$; demand at $t_2$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$F_{(d_1,d_2)}$ $\{F|F$ satisfies $(d_1,d_2)\}$ $\Omega_{(d_1,d_2)}$ those $X$ generated from $F\in F_{(d_1,d_2)}$ $\Omega_{(d_1,d_2),\min}$ $\{X|X$ is $\leq$ w.r.t. in $\Omega_{(d_1,d_2)}\}$ $U_j$ the maximum capacity of $ml_j$, $j = 1,2,\dots,r + q$ $o_j$ the minimum of remaining total demand and $U_j$, $j = 1,2,\dots,r + q$ $R_{(d_1,d_2)}$ network reliability to meet $d_1$ and $d_2$
</div>

## 3.2. Some definitions

As Fig. 3 shows, those cities or site devices de<sup>fi</sup>ned as nodes are denoted by $\nu _ { k } ,$ where $k = 1 , 2 , . . . , p$ with p being the number of nodes. For example, Taipei City is $\nu _ { 1 }$ and site TP-1 is $\nu _ { 2 }$ . We denote each LPS as $l _ { i , j }$ where $l _ { i , j } \in L P _ { i }$ means the jth segment $l _ { i , j }$ in $L P _ { i } ( j { = } 1 , 2 , . . . , r _ { i }$ with $r _ { i }$ being the number of LPS in $L P _ { i } )$ . For example, in Fig. 3, $L P _ { 1 }$ is a tunnel from Taipei $\left( \nu _ { 1 } \right)$ to Chicago $\left( \nu _ { 8 } \right)$ , which is combined with three LPS $l _ { 1 , 1 } ,$ $l _ { 1 , 2 } , \mathrm { a n d } l _ { 1 , 3 } ,$ and goes through two nodes v (TP-1) and $\nu _ { 6 }$ (San Francisco). Its connection sequence is: $\nu _ { 1 }  l _ { 1 , 1 }  \nu _ { 2 }  l _ { 1 , 2 }  \nu _ { 6 }  l _ { 1 , 3 }  \nu _ { 8 } .$ The capacity of each LP is 622 Mb, and each LP is combined by four 155-Mb channels. As each channel is regarded as one unit, there are 4 units for each LP.

The PL is the actual optical cable where the LP is located and used for data transmission, denoted by $P _ { i _ { 1 } }$ , where $i = 1 , 2 , . . . , c$ with c being the number of PL. For example, LPS $l _ { 1 , 3 } , l _ { 4 , 4 } , l _ { 1 1 , 1 }$ is combined in one PL from San Francisco to Chicago, as shown as the PL $P _ { 1 0 }$ in Fig. 4. The capacity of each PL is 2.5 Gb and is divided into four 622-Mb LP. The capacity state of an LPS is the same as a PL either when connected or disconnected. Each LPS has two capacity states: 0 units (0 Gb) and 4 units (622 Mb with four 155-Mb LP), respectively. That is, once the PL fails, all the LPS that are located in this PL also fail. Those LPS located in the same PL have the same disconnection probability (or conversely, the same connection probability). For example, LPS $l _ { 1 , 3 } ,$ l<sub>4,4</sub>, $l _ { 1 1 , 1 }$ located in one PL $P _ { 1 0 }$ have the same disconnection probability.

![](/api/attachments/42WMWUX9/fulltext/images/cca5e311ae4947c298b3c55e2f6f8bb3799117c749a1ddc99a22348414db4541.jpg)  
Fig. 3. Revised network using LPS.

![](/api/attachments/42WMWUX9/fulltext/images/ce01820600a59641341610578b1f8b1d9a27615291255dae41f7c21e24411360.jpg)  
Fig. 4. Physical line connection.

## 3.3. Revised stochastic-flow network model

The SFN evaluation technology developed in [17] is a method that is not suitable to be applied to TWAREN. There are some differences in this problem. In particular, each LP is combined with LPS $l _ { i , j } ,$ which cannot be divided through any nodes. To create an easier expression, we relabel all $\mathrm { L P S } \operatorname { a s } e _ { 1 } , e _ { 2 } , . . . , e _ { n } ,$ where n is the number of LPS, instead o $\cdot _ { l _ { i , j } . }$ Let $G =$ (E, V, M) be a SFN where E={e<sub>i</sub>| 1≤i≤n} is the set of LPS, V is the set of nodes, and $M { = } ( M ^ { 1 } , M ^ { 2 } , { \ldots } , M ^ { n } )$ with M<sup>i</sup> (an integer) being the maximum capacity of each LPS $e _ { i \cdot }$ Such a G further satis<sup>fi</sup>es the following assumptions:

## 1. Each node is perfectly reliable.

2. The capacity of each LPS is stochastic with a given probability distribution according to historical data.

3. The capacities of different LPS are statistically independent.

Let Taipei city be the <sup>fi</sup>rst source denoted by $s _ { 1 } ,$ Hsinchu city be the second source denoted by $s _ { 2 } ,$ New York be the <sup>fi</sup>rst sink denoted by $t _ { 1 } ,$ and Chicago be the second sink denoted by $t _ { 2 } .$ An MLP is a series of LPS from a source to a sink, which contains no cycle. In particular, any segment used by $L P _ { i }$ cannot be divided during transmission in $L P _ { i \cdot }$ That is, each LPS belongs to only one LP. Different from the MP, the MLP is a series of LPS. For example, as Fig. 3 shows, since $L P _ { 1 }$ and $L P _ { 4 }$ is divided, the connection $l _ { 1 , 1 }  l _ { 1 , 2 }  l _ { 4 , 4 }  l _ { 1 0 , 1 }$ is an MP but not an MLP. The connection $l _ { 1 , 1 }  l _ { 1 , 2 }  l _ { 1 , 3 }  l _ { 1 0 , 1 }$ is a MLP, as the whole LPS of $L P _ { 1 }$ and $L P _ { 1 0 }$ are all in the connection.

Suppose ml , ml , …, ml are all MLP from s and s to $t _ { 1 } ,$ , and $m l _ { r + 1 } ,$ $m l _ { r + 2 } , . . . , m l _ { r + q }$ are all MLP from $s _ { 1 }$ and $s _ { 2 }$ to $t _ { 2 } .$ . Then, the SFN can be described by the capacity vector $X = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ ) and the <sup>fl</sup>ow vector $F { = } ( f _ { 1 } , f _ { 2 } , . . . , f _ { r + q } )$ where $x _ { i }$ denotes the current capacity of $e _ { i } ,$ and $f _ { j }$ denotes the current <sup>fl</sup>ow on $m l _ { j } .$ The following constraint shows that the <sup>fl</sup>ow through e cannot exceed the maximum capacity of $e _ { i } ,$

$$
\sum_ {j = 1} ^ {r + q} \left\{f _ {j} \mid e _ {i} \in m l _ {j} \right\} \leq M ^ {i}, i = 1, 2, \dots , n.\tag{1}
$$

The network equipment in the headquarters of TWAREN can automatically compute and make decision to transfer data from different sources in Taiwan to the sinks in the U.S., depending on the loading and various status of each LP in order to achieve the best performance and better load balance of the whole of TWAREN's network topology. The LP is indivisible through any part of its nodes or edges during transmission, so we develop the MLP technique instead of traditional MP concept [17,18,21,23,34]. As there are multiple MLP to transfer data between Taiwan and U.S., different paths from various sources may go to the same destination and impact each other simultaneously. Therefore the demand level is based on the data delivered to the different sink nodes which is quite different than the classical source-sink problem [1,3,9,12,14,17–19,21–23,26,34]. Let $d _ { 1 }$ and $d _ { 2 }$ be the demand at New York and Chicago, respectively. To meet the demand $( d _ { 1 } , d _ { 2 } )$ , the <sup>fl</sup>ow vector $F { = } ( f _ { 1 } , f _ { 2 } , . . . , f _ { r + q } )$ has to satisfy

$$
\sum_ {j = 1} ^ {r} f _ {j} = d _ {1}, \text { and }\tag{2}
$$

$$
\sum_ {j = r + 1} ^ {r + q} f _ {j} = d _ {2}.\tag{3}
$$

For convenience, let $F _ { ( d _ { 1 } , d _ { 2 } ) } = \{ F | F$ satis<sup>fi</sup>es constraints $( 1 ) , ( 2 )$ and (3)} be the set of F meeting $( d _ { 1 } , d _ { 2 } )$ . For each $F { \in } F _ { ( d _ { 1 } , d _ { 2 } ) } $ , the corresponding capacity vector $X _ { F } { = } ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ is generated via

$$
x _ {i} = \sum_ {j = 1} ^ {r + q} \left\{f _ {j} \mid e _ {i} \in m l _ {j} \right\}, i = 1, 2, \dots , n.\tag{4}
$$

For convenience, let $\Omega _ { ( d _ { 1 } , d _ { 2 } ) } = \{ X _ { F } | F { \in } F _ { ( d _ { 1 } , d _ { 2 } ) } \}$ and $\Omega _ { ( d _ { 1 } , d _ { 2 } ) , \operatorname* { m i n } } = \{ X | X \quad$ is w.r.t. in $\Omega _ { ( d _ { 1 } , d _ { 2 } ) } \}$ (where Y≤X if and only if y ≤x for each $i { = } 1 , 2 , . . . , n$ and YbX if and only i $\operatorname { f } Y \leq X$ and y bx for at least one i). For short, each $\pmb { X } { \in } \Omega _ { ( d _ { 1 } , d _ { 2 } ) , \operatorname* { m i n } }$ is named $\textsf { a } ( d _ { 1 } , d _ { 2 } ) – \mathsf { M L P }$ in this paper. All $( d _ { 1 } , d _ { 2 } ) – \mathrm { M L P }$ can be derived by the following steps:

$$
F = (f _ {1}, f _ {2}, \dots , f _ {r + q})
$$

Step 2 Transform each F into $X _ { F } { = } \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right)$ via Eq. (4) to get $\Omega _ { ( d _ { 1 } , d _ { 2 } ) } .$ Step 3 Remove those non-minimal ones in $\varOmega _ { ( d _ { 1 } , d _ { 2 } ) }$ to obtain $\varOmega _ { ( d _ { 1 } , d _ { 2 } ) }$ <sub>; min</sub> , i.e. $( d _ { 1 } , d _ { 2 } ) – \mathrm { M L P } .$

To execute step 1, we may apply the branch-and-bound approach [16], which is always denoted by a search tree composed of vertices and branches. For example, choose $f _ { 1 }$ as the starting variable, and treat Eq. (2) as the constraint of the search tree (see Fig. 5). Let U denote the maximum capacity of $m l _ { j } ,$ , and $o _ { j } = \left\{ \operatorname* { m i n } \left\{ \left( w - \sum _ { i = 1 } ^ { j - 1 } f _ { i } \right) , U _ { j } \right\} \right.$ where $j = 2 , 3 , . . . , r .$ By repeating the search tree procedure in $\mathrm { F i g . } \stackrel { \cdot } { 5 } ,$ we can identify all of the feasible solutions for $d _ { 1 } .$ . Similarly we can use branch-and-bound approach to get the feasible solution for $d _ { 2 } .$ Step 2 is a regular computation used to obtain $\varOmega _ { ( d _ { 1 } , d _ { 2 } ) }$ . Step 3 can apply the approach of Quicksort in [7], which uses the Divide-and-Conquer theory, except that we remove the non-minimal ones in the exchange step of the partition algorithm.

## 3.4. Network reliability evaluation

In previous literatures [1,3,9,12,14,17–19,21–23,26,34], the network reliability is the probability of the maximum <sup>fl</sup>ow not less than speci<sup>fi</sup>c demand d between some nodes, which can be represented as $R _ { d } = \operatorname* { P r } \{ Y |$ Y≥X for a d-MP X}, where d-MP [23] are the lower boundary points for d. Similarly, we can calculate the network reliability of LP system based on the same concept. Since $( d _ { 1 } , d _ { 2 } ) { \mathrm { - M L P } }$ are the lower boundary points for $( d _ { 1 } , d _ { 2 } )$ , we de<sup>fi</sup>ne the network reliability $R _ { ( d _ { 1 } , d _ { 2 } ) }$ as the probability that the system can transmit $d _ { 1 }$ units of data to the <sup>fi</sup>rst sink $t _ { 1 }$ and $d _ { 2 }$ units of data to the second sink $t _ { 2 } .$ The network reliability is to calculate the probability for those vectors not less than $( d _ { 1 } , d _ { 2 } ) – \mathrm { M L P } , \mathrm { i . e . , } R _ { ( d _ { 1 } , d _ { 2 } ) } =$ $\operatorname* { P r } \{ Y | Y { \geq } X$ for a $( d _ { 1 } , d _ { 2 } )$ -MLP X}. If $\{ X _ { 1 } , X _ { 2 } , . . . , X _ { h } \}$ is the set of $( d _ { 1 } ,$ $d _ { 2 } ) \mathrm { - M L P }$ , then network reliability $R _ { ( d _ { 1 } , d _ { 2 } ) }$ is

$$
R _ {(d _ {1}, d _ {2})} = \operatorname * {P r} \left\{\bigcup_ {v = 1} ^ {h} Q _ {v} \right\},\tag{5}
$$

where $Q _ { \nu } = \{ X | X { \geq } X _ { \nu } \} , \nu { = } 1 , 2 , . . . , h$ . Several methods such as the RSDP algorithm [34], the inclusion-exclusion method [12,31], the disjointevent method [32], and state-space decomposition [1,3] may be applied to compute $R _ { ( d _ { 1 } , d _ { 2 } ) } .$ . The RSDP algorithm has a better computational ef<sup>fi</sup>- ciency to compute the network reliability here. It calculates the probability of a union with r vectors in terms of the probabilities unions with $( r - 1 )$ vectors or less by using a special maximum operator [34] $" \oplus " ,$ , which is de<sup>fi</sup>ned as

$$
X _ {1, 2} = X _ {1} \oplus X _ {2} \equiv (\max (x _ {1 i}, x _ {2 i})), \text { for } i = 1, 2, \dots n.\tag{6}
$$

For example, if $X _ { 1 } = ( 2 , 2 , 1 , 1 , 0 )$ and $X _ { 2 } = ( 3 , 0 , 1 , 0 , 1 ) , X _ { 1 , 2 } =$ $X _ { 1 } \oplus X _ { 2 } = ( \operatorname* { m a x } ( 2 , 3 )$ , max(2, 0), max(1, 1), max(1, 0), max(0, 1))=(3, 2, 1, 1, 1). The RSDP algorithm is presented as follows.

RSDP algorithm//calculate the network reliability $R _ { ( d _ { 1 } , d _ { 2 } ) }$ for all Ω  <sub>d1;d2 ;</sub> <sub>min</sub> function $R _ { ( d _ { 1 } , d _ { 2 } ) } = \tt R S D P ( X _ { 1 } , X _ { 2 } , . . . , X _ { h } )$ //Input h vectors $( X _ { 1 } , X _ { 2 } , . . . ,$ $X _ { h } )$ and connection probability of each LPS

$$
\begin{array}{l} \text { for } i = 1: h \\ \text { if } i = = 1 \\ R _ {(d _ {1}, d _ {2})} = \operatorname * {P r} (X \geq X _ {i}); \\ \text { else } \\ \text { Temp\_R\_1 } = \operatorname * {P r} (X \geq X _ {i}); \\ \text { If } i = = 2 \\ \text { Temp\_R\_2 } = \operatorname * {P r} (X \geq \max (X _ {1}, X _ {i})); / / \max (X _ {1}, X _ {i}) = (X _ {1} \oplus X _ {i}) \end{array}
$$

![](/api/attachments/42WMWUX9/fulltext/images/a7f708c77597d6f71f8aeb0a876a378ba3dae6216bf178236dbb91380fac4dff.jpg)  
Fig. 5. Branch-and-Bound approach to get solution for $d _ { 1 } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
else
    for j = 1 : i - 1
 $X_{j} = \max(X_{j}, X_{i})$ ; //  $\max(X_{j}, X_{i}) = (X_{j} \oplus X_{i})$ 
    end
    Temp_R_2 = RSDP( $X_{1}, X_{2}, ..., X_{i-1}$ );
    end
end
 $R_{(d_{1}, d_{2})} = R_{(d_{1}, d_{2})} + (\text{Temp\_R\_1}) - (\text{Temp\_R\_2})$ ;
</div>

## 4. Network reliability of TWAREN international scope

## 4.1. Demand level and MLP

In this paper, we calculate the network reliability of multiple sources (Taipei and Hsinchu) that transmit $d _ { 1 }$ units of data to the <sup>fi</sup>rst sink in New York, and $d _ { 2 }$ units of data to the second sink in Chicago. First we have to de<sup>fi</sup>ne a LP unit to calculate the network reliability. Since the smallest bandwidth of the LP system is 155 Mb, we regard each 155 Mb as one unit. Therefore, there are four units in each 622 Mb LP channel.

We try to evaluate $R _ { ( 2 0 , 8 ) } = \operatorname* { P r } \{ Y | Y \geq X$ for a (20, 8)-MLP X} for the case that $( d _ { 1 } , d _ { 2 } ) = ( 2 0 , \dot { 8 } )$ . In Fig. 3, there are 10 MLP from $\nu _ { 1 }$ (Taipei) to $\nu _ { 9 }$ (New York) as shown in Table 1(a), 10 MLP from $\nu _ { 1 3 }$ (Hsinchu) to $\nu _ { 9 }$ (New York) as shown in Table 1(b), 7 MLP from $\nu _ { 1 }$ (Taipei) to $\nu _ { 8 }$ (Chicago) as shown in Table 1(c), and 9 MLP from $\nu _ { 1 3 }$ (Hsinchu) to v (Chicago) as shown in Table 1(d).

Table 2 shows all LPS connection probability after screening all PL's disconnection records and selecting the longest broken time for each in [29]. These breaks include disabled card devices, circuit failures, and breaks from the March 11, 2011 Japanese earthquake and tsunami that caused the physical submarine line $P _ { 8 }$ to break. This line uses a submarine cable connection between TP-3 and Los Angeles. Arti<sup>fi</sup>cial devices, short circuits, and natural disasters simultaneously in<sup>fl</sup>uence TWAREN's network reliability. Since each failure of a node device has been included and recorded in the PL's disconnection record, each node is supposed to be perfect with a reliability of 1 (the reason to

To compute the connection probability of each PL, we use the disconnection data from 2008 through 2011 of the circuit down report in [29]. The longest duration of every break for each PL during the 168 h of every week is used to determine the disconnection probability of each line. For example, as the PL $P _ { 1 0 }$ from San Francisco to Chicago broke for 403 minutes on 2010/5/25, its connection probability is $( 1 6 8 \times 6 0 - 4 0 3 ) / ( 1 6 8 \times 6 0 ) = 0 . 9 0 .$ Therefore, its disconnection probability is $( 1 - 0 . 9 ) = 0 . 1 $ . All the LPS $l _ { 1 , 3 } , l _ { 4 , 4 } ,$ and $l _ { 1 1 , 1 }$ located in this PL ${ \bf \nabla } _ { { \bf { 1 0 } } }$ have the same disconnection probability of 0.1.

## 4.2. Probability of LPS breaking

Table 1  
All MLP from multi-sources to multi-sinks.  
```txt
MLP # Light paths combination Nodes & LPS combination
(a) From Taipei (v1) to New York (v9).
ml1 Taipei → LP1 → Chicago → LP10 → New York v1 → l1,1 → v2 → l1,2 → v6 → l1,3 → v8 → l10,1 → v9
ml2 Taipei → LP1 → Chicago → LP13 → New York v1 → l1,1 → v2 → l1,2 → v6 → l1,3 → v8 → l13,1 → v9
ml3 Taipei → LP4 → Chicago → LP10 → New York v1 → l4,1 → v2 → l4,2 → v5 → l4,3 → v6 → l4,4 → v8 → l10,1 → v9
ml4 Taipei → LP4 → Chicago → LP13 → New York v1 → l4,1 → v2 → l4,2 → v5 → l4,3 → v6 → l4,4 → v8 → l13,1 → v9
ml5 Taipei → LP3 → New York v1 → l3,1 → v2 → l3,2 → v3 → l3,3 → v7 → l3,4 → v9
ml6 Taipei → LP2 → Los Angeles → LP12 → New York v1 → l2,1 → v2 → l2,2 → v3 → l2,3 → v4 → l2,4 → v7 → l12,1 → v9
ml7 Taipei → LP2 → Los Angeles → LP11 → Chicago → LP10 → New York v1 → l2,1 → v2 → l2,2 → v3 → l2,3 → v4 → l2,4 → v7 → l11,2 → v6 → l11,1 → v8 → l10,1 → v9
ml8 Taipei → LP2 → Los Angeles → LP11 → Chicago → LP13 → New York v1 → l2,1 → v2 → l2,2 → v3 → l2,3 → v4 → l2,4 → v7 → l11,2 → v6 → l11,1 → v8 → l13,1 → v9
ml9 Taipei → LP1 → Chicago → LP11 → Los Angeles → LP12 → New York v1 → l1,1 → v2 → l1,2 → v6 → l1,3 → v8 → l11,1 → v6 → l11,2 → v7 → l12,1 → v9
ml10 Taipei → LP4 → Chicago → LP11 → Los Angeles → LP12 → New York v1 → l4,1 → v2 → l4,2 → v5 → l4,3 → v6 → l4,4 → v8 → l11,1 → v6 → l11,2 → v7 → l12,1 → v9
(b) From Hsinchu (v13) to New York (v9).
ml11 Hsinchu → LP5 → Chicago → LP10 → New York v10 → l5,1 → v3 → l5,2 → v2 → l5,3 → v5 → l5,4 → v6 → l5,5 → v8 → l10,1 → v9
ml12 Hsinchu → LP5 → Chicago → LP13 → New York v10→l5,1→v3→l5,2→v2→l5,3→v5→l5,4→v6→l5,5→v8→l13,1→v9
ml13 Hsinchu→LP7→New York v10→l7,1→v3→l7,2→v4→l7,3→v7→l7,4→v9
ml14 Hsinchu→LP6→Los Angeles→LP12→New York v10→l6,1→v3→l6,2→v7→l12,1→v9
ml15 Hsinchu→LP6→Los Angeles→LP11→Chicago→LP10→New York v10→l6,1→v3→l6,2→v7→l11,2→v6→l11,1→v8→l10,1→v9
ml16 Hsinchu→LP6→Los Angeles→LP11→Chicago→LP13→New York v10→l6,1→v3→l6,2→v7→l11,2→v6→l11,1→v8→l13,1→v9
ml17 Hsinchu→LP8→Los Angeles→LP12→New York v10→l8,1→v3→l8,2→v7→l12,1→v9
ml18 Hsinchu→LP8→Los Angeles→LP11→Chicago→LP10→New York v10→l8,1→v3→l8,2→v7→l11,2→v6→l11,1→v8→l10,1→v9
ml19 Hsinchu→LP8→Los Angeles→LP11→Chicago→LP13→New York v10→l8,1→v3→l8,2→v7→l11,2→v6→l11,1→v8→l13,1→v9
ml20 Hsinchu→LP5→Chicago→LP11→Los Angeles→LP12→New York v10→l5,1→v3→l5,2→v2→l5,3→v5→l5,4→v6→l5,5→v8→l11,1→v6→l11,2→v7→l12,1→v9
(c) From Taipei (v₁) to Chicago(v₈).
ml21 Taipei→LP₁→Chicago v₁→l₁,₁→v₂→l₁,₂→v6→l₁,₃→v8
ml22 Taipei→LP4→Chicago v₁→l4,₁→v₂→l4,₂→v5→l4,3→v6→l4,4→v8
ml23 Taipei→LP2→Los Angeles→LP₁2→New York→LP₁0→Chicago v₁→l2,₁→v₂→l2,2→v3→l2,3→v4→l2,4→v7→l12,1→v9→l₁0,₁→v8
ml24 Taipei→LP2→Los Angeles→LP₁2→New York→LP₁3→Chicago v₁→l2,₁→v₂→l2,2→v3→l2,3→v4→l2,4→v7→l  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5
ml25 Taipei→LP2<fcel>Hsinchu \rightarrow LP5 \rightarrow Chicago \rightarrow HP_4 \rightarrow Chicago \rightarrow HP_4 \rightarrow Chicago \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_4 \rightarrow HP_<nl>
ml26 Taipei \( \rightarrow\) LP3 \( \rightarrow\) New York \( \rightarrow\) LP_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{s}}_{\text{p}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{s}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\text{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}}_{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}} _{\mathrm{p}}
(d) From Hsinchu (v\( _{i} \) ) to Chicago(v\( _{8} \)).
ml\( _{28} \) Hsinchu \( \rightarrow\) LP\( _{5} \) \( \rightarrow \) Chicago \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*} W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}W^{*}\)
ml\( _{29} \) Hsinchu \( \rightarrow\) LP\( _{6} \) \( \rightarrow \) Los Angeles \( \rightarrow\) LP\( _{i} \) \( \rightarrow \) Chicago \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \)
ml\( _{30} \) Hsinchu \( \rightarrow\) LP\( _{6} \) \( \rightarrow \) Los Angeles \( \rightarrow\) LP\( _{i} \) \( \rightarrow \) New York \( \rightarrow\) LP\( _{i} \) \( \rightarrow \) Chicago \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \)
ml\( _{30} \) Hsinchu \( \rightarrow\) LP\( _{6} \) \( \rightarrow \) Los Angeles \( \rightarrow\) LP( p ) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \) \( V_{i} \)\( V_{i0}\to L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.7V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V - L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.8V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V- L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=V -L7.9V=
```

Table 2  
Connection probability of all physical lines and LPS

<table><tr><td>PL#</td><td>LPS in this PL</td><td>Disconnection starting time</td><td>Disconnection ending time</td><td>Disconnection duration</td><td>Connection probability (t=a week=4032 min)</td><td>Root cause</td></tr><tr><td> $P_1$ </td><td> $l_{1,1}; l_{2,1}; l_{3,1}; l_{4,1}$ </td><td>2011/4/21 10:17:00 AM</td><td>2011/4/21 11:56:00 AM</td><td>99 min</td><td>1-99/t=0.98</td><td>Circuit broken</td></tr><tr><td> $P_2$ </td><td> $l_{2,2}; l_{3,2}; l_{5,2}$ </td><td>N/A</td><td>N/A</td><td>N/A</td><td>1</td><td>No</td></tr><tr><td> $P_3$ </td><td> $l_{2,3}; l_{7,2}$ </td><td>N/A</td><td>N/A</td><td>N/A</td><td>1</td><td>No</td></tr><tr><td> $P_4$ </td><td> $l_{1,2}$ </td><td>2010/9/28 10:08:00 AM</td><td>2010/9/28 02:07:00 PM</td><td>239 min</td><td>1-239/t=0.94</td><td>Card broken</td></tr><tr><td> $P_5$ </td><td> $l_{4,2}; l_{5,3}$ </td><td>2011/4/21 22:01 PM</td><td>2011/4/22 04:29:00 AM</td><td>388 min</td><td>1-388/t=0.90</td><td>Circuit broken</td></tr><tr><td> $P_6$ </td><td> $l_{4,3}; l_{5,4}$ </td><td>2009/5/29 05:16 AM</td><td>2009/5/29 08:27:00 AM</td><td>191 min</td><td>1-191/t=0.95</td><td>Circuit broken</td></tr><tr><td> $P_7$ </td><td> $l_{3,3}; l_{6,2}; l_{8,2}$ </td><td>2009/9/16 04:40:00 PM</td><td>2009/9/16 05:01:00 PM</td><td>211 min</td><td>1-211/t=0.99</td><td>Circuit broken</td></tr><tr><td> $P_8$ </td><td> $l_{2,4}; l_{7,3}$ </td><td>2011/3/11 01:53:00 PM</td><td>2011/3/12 01:37:00 AM</td><td>704 min</td><td>1-704/t=0.83</td><td>Japan earthquake</td></tr><tr><td> $P_9$ </td><td> $l_{11,2}$ </td><td>2011/2/17 01:19:00 AM</td><td>2011/2/17 03:33:00 AM</td><td>134 min</td><td>1-134/t=0.97</td><td>Card disable</td></tr><tr><td> $P_{10}$ </td><td> $l_{1,3}; l_{4,4}; l_{11,1}; l_{5,5}$ </td><td>2010/5/25 04:28:00 AM</td><td>2010/5/25 11:11:00 AM</td><td>403 min</td><td>1-403/t=0.90</td><td>Circuit broken</td></tr><tr><td> $P_{11}$ </td><td> $l_{3,4}; l_{12,1}; l_{7,4}$ </td><td>2009/3/21 08:58:00 PM</td><td>2009/3/22 03:23:00 AM</td><td>385 min</td><td>1-385/t=0.90</td><td>Card disable</td></tr><tr><td> $P_{12}$ </td><td> $l_{10,1}; l_{13,1}$ </td><td>2011/2/8 01:17:00 AM</td><td>2011/2/8 11:07:00 AM</td><td>590 min</td><td>1-590/t=0.85</td><td>Card disable</td></tr><tr><td> $P_{13}$ </td><td> $l_{5,1}; l_{6,1}; l_{7,1}; l_{8,1}$ </td><td>N/A</td><td>N/A</td><td>N/A</td><td>1</td><td>No</td></tr></table>

have assumption 1). For computational convenience, as described in Section 3.3, we converted LPS $l _ { i , j }$ by using e and the probability of e , as shown in Table 3.

## 4.3. Network reliability evaluation

When a cable breaks, the suppliers of this pass-through PL provide all serviceable lines as backup lines, therefore increasing the network reliability, and the backup lines' infrastructure is base on the analysis result of the regular lines. In this study, we do not discuss the backup lines, and concentrate only on the regular lines to determine those factors that affect their network reliability. First, we focus on the demand pair (20, 8), given all MLP in Table 1(a) to (d) and by using the algorithm in Section 3.3 as follows to obtain $\varOmega _ { ( d _ { 1 } , d _ { 2 } ) }$ <sub>; min</sub> .

Step 1 Find all feasible solutions F that satisfy constraints (7), (8) and (9).

$$
\begin{array}{l} f _ {1} + f _ {2} + f _ {9} + f _ {2 1} \leq 4, \\ \vdots \\ f _ {1} + f _ {2} + f _ {9} + f _ {2 1} \leq 4, \end{array}\tag{7}
$$

$$
\begin{array}{r} f _ {1 7} + f _ {1 8} + f _ {1 9} + f _ {3 4} + f _ {3 5} + f _ {3 6} \leq 4, \\ f _ {1 7} + f _ {1 8} + f _ {1 9} + f _ {3 4} + f _ {3 5} + f _ {3 6} \leq 4, \end{array}
$$

$$
f _ {1} + f _ {2} + \dots + f _ {1 0} = d _ {1} = 2 0, \text { and }\tag{8}
$$

$$
f _ {1 1} + f _ {1 2} + \dots + f _ {2 0} = d _ {2} = 8.\tag{9}
$$

In this step, each f has two values, say 0 and 4, standing for the two capacity states of failure or success. From this, we obtain 72 <sup>fl</sup>ow vectors as shown in column 1 of Table 4.

$$
\begin{array}{l} \text {Step 2 Transform each F into LPS X to get \Omega_ {(20,8)} by Eq. (10).} \\ \text {For F_{1} = (0,0,0,0,4,0,0,0,0,0,0,4,4,0,4,0,4,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,} \end{array}
$$

Table 3  
The connection probability of LPS $l _ { i , j }$ re-denoted by $e _ { i \cdot }$

<table><tr><td>Edge</td><td> $e_{1}$ </td><td> $e_{2}$ </td><td> $e_{3}$ </td><td> $e_{4}$ </td><td> $e_{5}$ </td><td> $e_{6}$ </td><td> $e_{7}$ </td><td> $e_{8}$ </td><td> $e_{9}$ </td><td> $e_{10}$ </td><td> $e_{11}$ </td></tr><tr><td>LPS</td><td> $l_{1,1}$ </td><td> $l_{1,2}$ </td><td> $l_{1,3}$ </td><td> $l_{2,1}$ </td><td> $l_{2,2}$ </td><td> $l_{2,3}$ </td><td> $l_{2,4}$ </td><td> $l_{3,1}$ </td><td> $l_{3,2}$ </td><td> $l_{3,3}$ </td><td> $l_{3,4}$ </td></tr><tr><td>Prob.</td><td>0.98</td><td>0.94</td><td>0.90</td><td>0.98</td><td>1.00</td><td>1.00</td><td>0.83</td><td>0.98</td><td>1.00</td><td>0.99</td><td>0.90</td></tr><tr><td>Edge</td><td> $e_{12}$ </td><td> $e_{13}$ </td><td> $e_{14}$ </td><td> $e_{15}$ </td><td> $e_{16}$ </td><td> $e_{17}$ </td><td> $e_{18}$ </td><td> $e_{19}$ </td><td> $e_{20}$ </td><td> $e_{21}$ </td><td> $e_{22}$ </td></tr><tr><td>LPS</td><td> $l_{4,1}$ </td><td> $l_{4,2}$ </td><td> $l_{4,3}$ </td><td> $l_{4,4}$ </td><td> $l_{10,1}$ </td><td> $l_{11,1}$ </td><td> $l_{11,2}$ </td><td> $l_{12,1}$ </td><td> $l_{13,1}$ </td><td> $l_{5,1}$ </td><td> $l_{5,2}$ </td></tr><tr><td>Prob.</td><td>0.98</td><td>0.90</td><td>0.95</td><td>0.90</td><td>0.85</td><td>0.90</td><td>0.97</td><td>0.90</td><td>0.85</td><td>1.00</td><td>1.00</td></tr><tr><td>Edge</td><td> $e_{23}$ </td><td> $e_{24}$ </td><td> $e_{25}$ </td><td> $e_{26}$ </td><td> $e_{27}$ </td><td> $e_{28}$ </td><td> $e_{29}$ </td><td> $e_{30}$ </td><td> $e_{31}$ </td><td> $e_{32}$ </td><td> $e_{33}$ </td></tr><tr><td>LPS</td><td> $l_{5,3}$ </td><td> $l_{5,4}$ </td><td> $l_{5,5}$ </td><td> $l_{6,1}$ </td><td> $l_{6,2}$ </td><td> $l_{7,1}$ </td><td> $l_{7,2}$ </td><td> $l_{7,3}$ </td><td> $l_{7,4}$ </td><td> $l_{8,1}$ </td><td> $l_{8,2}$ </td></tr><tr><td>Prob.</td><td>0.90</td><td>0.95</td><td>0.90</td><td>1.00</td><td>0.99</td><td>1.00</td><td>1.00</td><td>0.83</td><td>0.90</td><td>1.00</td><td>0.99</td></tr></table>

0,0,0,0), the capacity vector $X _ { 1 }$ is transformed by

$$
\begin{array}{l} x _ {1} = f _ {1} + f _ {2} + f _ {9} + f _ {2 1} = 0 + 0 + 0 + 4 = 4, \\ x _ {2} = f _ {1} + f _ {2} + f _ {9} + f _ {2 1} = 0 + 0 + 0 + 4 = 4, \\ \vdots \\ x _ {3 2} = f _ {1 7} + f _ {1 8} + f _ {1 9} + f _ {3 4} + f _ {3 5} + f _ {3 6} = 4 + 0 + 0 + 0 + 0 + 0 = 4, \text { and } \\ x _ {3 3} = f _ {1 7} + f _ {1 8} + f _ {1 9} + f _ {3 4} + f _ {3 5} + f _ {3 6} = 4 + 0 + 0 + 0 + 0 + 0 = 4. \end{array}\tag{10}
$$

Thus, X =(4,4,4,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 4,4,4). Similarly, we obtain 72 capacity vectors as shown in column 2 of Table 4.

Step 3 The non-minimal ones in $\Omega _ { ( 2 0 , 8 ) }$ are removed to obtain $\Omega _ { ( 2 0 , 8 ) }$ <sub>,min</sub>, i.e. (20,8)-MLP as shown in column 3 of Table 4.

In terms of RSDP [34], we calculate the network reliability $R _ { ( 2 0 , 8 ) } = \operatorname* { P r } \{ Y | Y \geq X { \mathrm { ~ f o r ~ a ~ } } ( 2 0 , 8 ) { \mathrm { - M L P ~ } } X \} = 0 . 1 7 7 5$ . Similarly, $R _ { ( 2 0 , 4 ) } =$ $0 . 3 5 1 7 , R _ { ( 2 0 , 0 ) } = 0 . 4 1 4 0 ,$ , can be evaluated respectively. The network reliability can be observed to decrease as the total demand increases, as shown in Table 5 and Fig. 6.

Usually QoS only need to be concerned as there are limited networks resources or bandwidth. In case of $d _ { 1 } = 4 ,$ when there are enough resources and demand $d _ { 2 }$ is low, for instance as above with (4, 0), there are still plenty of resources to handle other transmission requests, so the network reliability is quite high. On the other hand, if demand $d _ { 2 }$ is high, say above set (4, 24), the network reliability will be low, since there are insuf<sup>fi</sup>cient resources to handle other data transmissions. To maintain the network reliability, it is important to avoid full transmission loads or to increase line capacity in lower cost expense. Depending on the results of our analysis, we may decide to allocate more economic resources to TWAREN to maximize future network utilities.

## 5. Conclusion and discussion

In many <sup>fi</sup>elds, decision makers of various organizations always require appropriate tools to manage the resources available to them and lower cost. TWAREN's resources are limited and cost-oriented, and its infrastructure relies heavily on the supporting decision making tools, whether in the construction or maintenance stage. It is critical that a network manager identi<sup>fi</sup>es an appropriate tool that can assist with making proper decisions for the network infrastructure. The QoS is an essential parameter when seeking to realize the performance of a real network system. The reliability evaluation technique is a fundamental issue required to support the decisions made by managers for the improvement of the entire infrastructure. This paper evaluates the network reliability of a revised SFN with multiple sources and multiple sinks, instead of a traditional TTNR, KTNR, and ATNR analysis in a binary-state <sup>fl</sup>ow network. We also adopt an MLP-based network reliability evaluation technique for the international LP portion of TWAREN which is organized by CHT. This segment contains the Asia-Paci<sup>fi</sup>c domestic land surface and submarine cables, which are connected to the worldwide academic research network, especially the Internet2 Network [13] in the United States.

Table 4 Results of example for Ω<sub>(20,8),min</sub>.

<table><tr><td>F</td><td>X</td><td>(20,8)-MLP or not?</td></tr><tr><td> $F_1 = (0,0,0,0,4,0,0,0,0,0,0,4,4,0,4,0,4,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0)$ </td><td> $X_1 = (4,4,4,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559</td><td>\( X_1 \geqslant X_2$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$  $X_2 \geqslant X_3$ </td></tr><tr><td> $F_2 = (0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)$ </td><td>\( X_2 = (4.4,4.0,0.0,0.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4. 4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4 4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4.4. 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0. 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0 0 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0. 0 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.</td><td></td></tr><tr><td colspan="3">\( F_3 = (0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.</td></tr><tr><td>\( F_4 = (0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0 0.0.0.0.0.0.0.0.0 0 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0 1 0 0.0.0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0 0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0.0 1 0 0.0.0.0 1 0 0.0.0.0 1 0 0.0.0.0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 8 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 6 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 67 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X68 X</td><td></td><td></td></tr></table>

Table 5  
Network reliability for various demand $( d _ { 1 } , d _ { 2 } ) .$

<table><tr><td></td><td> $d_1=0$ </td><td> $d_1=4$ </td><td> $d_1=8$ </td><td> $d_1=12$ </td><td> $d_1=16$ </td><td> $d_1=20$ </td><td> $d_1=24$ </td></tr><tr><td> $d_2=0$ </td><td>1</td><td>0.9999</td><td>0.9976</td><td>0.9707</td><td>0.8195</td><td>0.4140</td><td>0</td></tr><tr><td> $d_2=4$ </td><td>1</td><td>0.9998</td><td>0.9955</td><td>0.9558</td><td>0.7694</td><td>0.3517</td><td>0</td></tr><tr><td> $d_2=8$ </td><td>0.9990</td><td>0.9969</td><td>0.9770</td><td>0.8745</td><td>0.5814</td><td>0.1775</td><td>0</td></tr><tr><td> $d_2=12$ </td><td>0.9878</td><td>0.9721</td><td>0.8856</td><td>0.6297</td><td>0.2401</td><td>0</td><td>0</td></tr><tr><td> $d_2=16$ </td><td>0.6866</td><td>0.8557</td><td>0.6276</td><td>0.2456</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $d_2=20$ </td><td>0.2838</td><td>0.5575</td><td>0.2401</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $d_2=24$ </td><td>0</td><td>0.1775</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Since the LP cannot be divided via any part of its nodes or LPS during data delivery, the MLP proposed in this paper is a totally new concept to evaluate the network reliability in an LP environment, which is different from that used in previous studies to discuss the <sup>fl</sup>ow assignment and evaluate the network reliability. The contribution of this study is that it is the <sup>fi</sup>rst to develop a revised SFN with multiple sources and multiple sinks based on LP, and then to make practical TWAREN data available for analysis. In terms of the MLP analysis technique, this will indicate how to continuously adjust TWAREN's infrastructure to achieve higher network reliability and enhance the NCHC's network management skills, which help the decision-maker to build up reliable and economic system. However, before deciding to construct the backup lines' infrastructure, the administrators have to know the performance of the regular lines. This study focuses on the portion of the network of regular lines which do not contain backup cables yet, which will help to determine the factors that affect the reliability of the dedicated regular lines' network, which may further help the managers to make better construction of the backup lines. This paper also considers the in<sup>fl</sup>uence of the earthquake that hit Japan on March 11, 2011. That is, it studies all the factors that can affect network reliability, including arti<sup>fi</sup>cial, machine, and cable failures and natural disasters that simultaneously in<sup>fl</sup>uence the reliability of the TWAREN network. In addition, the MLP network reliability technique used in the multiple sources and multiple sinks case will improve the ef<sup>fi</sup>ciency of TWAREN and assist us to learn how to improve its network infrastructure and performance in the near future.

This study implements the MLP technique. First, it lists all MLP (ml , $m l _ { 2 } . . . , m l _ { 3 6 } )$ from multiple sources to multiple sinks, and by means of this method, the <sup>fl</sup>ow from the source $s _ { 1 }$ (Taipei) to the sink t (New York) can be easily calculated. Similarly, other <sup>fl</sup>ows can also be computed in terms of the combination of else source and sink (e.g. s (Hsinchu) and $t _ { 2 }$ (Chicago)) based on the MLP. This technique enables practical and ef<sup>fi</sup>cient network system analysis to achieve a desired level of performance. That is, both theoretical and practical issues are discussed in this paper to make network reliability evaluation more ef<sup>fi</sup>cient. Subsequent study may be undertaken on the issue of the network reliability of TWARENs multiple sources to multiple sinks with backup lines, and further we may study the in<sup>fl</sup>uence of nodes failure.

## Acknowledgments

This work was supported in part by the National Science Council, Taiwan, Republic of China, under Grant No. NSC 98-2221-E-011-051-MY3.

## Appendix A

Acronyms QoS Quality of Service TWAREN Taiwan Advanced Research and Education Network TTNR Two-terminal network reliability KTNR k-terminal network reliability ATNR all-terminal network reliability SFN stochastic <sup>fl</sup>ow network NCHC Taiwan's National High Performance Computing Center MP minimal path LP light path LPS light path segment MLP minimal light path ISP Internet service provider CHT Chunghwa Telecom (the biggest ISP in Taiwan) RSDP recursive sum of disjoint products NREN national research and education network PL physical line

## References

[1] C. Alexopoulos, A note on state-space decomposition methods for analyzing stochastic flow networks JEEE Transactions on Reliability 44 (1995) 354–357

[2] W. Al-Khateeb, S. Al-Irhayim, Reliability Enhancement of Complex Networks Through Redundancy Scaling, in: International Conference on Computer and Communication Engineering, Kuala Lumpur, Malaysia, 2010, pp. 11–13.

[3] T. Aven, Reliability evaluation of multistate systems with multistate components, IEEE Transactions on Reliability 34 (1985) 473–479.

[4] I. Bose, E. Eryarsoy, L. He, Modeling and analysis of the effects of QoS and reliability on pricing, pro<sup>fi</sup>tability, and risk management in multiperiod grid-computing networks, Decision Support Systems 38 (2005) 529–538.

[5] I. Chen, M.R. Ito, A Study of Unreserved Backup Paths for Reliable QoS Under Single Link Failure, in: Computer Communications and Networks, ICCCN, Proceedings of 17th International Conference, St. Thomas, U.S. Virgin Islands, 2008 pp. 459–464.

![](/api/attachments/42WMWUX9/fulltext/images/e3b2fea57372aaaec1f82d06b5462e30d66805100a67bdc64f61f25579f819d0.jpg)  
Fig. 6. (demand, network reliability) for various demand $( d _ { 1 } , d _ { 2 } ) .$

[18] Y.K. Lin, Reliability of a stochastic-<sup>fl</sup>ow network with unreliable branches & nodes under budget constraints, IEEE Transactions on Reliability 53 (2004) 381–387.

[19] Y.K. Lin, A stochastic model to study the system capacity for supply chains in terms of minimal cuts, International Journal of Production Economics 124 (2010) 181–187.

[6] Chunghua Telecommunication(CHT) International, http://www.twgate.net2012.

[7] T. Cormen, C. Leiserson, R. Rivest, C. Stein, in: Introduction to algorithms, second edition, MIT Press, 2001, pp. 145–146.

[8] J.M. Cruz, Z. Liu, Modeling and analysis of the effects of QoS and reliability on pricing, pro<sup>fi</sup>tability, and risk management in multiperiod grid-computing networks Decision Support Systems 52 (2012) 562–576.

[9] B.A. Gebre, J.E. Ramirez-Marquez, Element substitution algorithm for general two-terminal network reliability analyses, IEEE Transactions on Reliability 39 (2007) 265–275.

[10] A. Haque, A study on the design of survivable optical virtual private networks (O-VPN), IEEE Transactions on Reliability 55 (2006) 516–524.

[11] P.H. Ho, Spare capacity reprovisioning for shared backup path protection in dynamic generalized multi-protocol label switched networks, IEEE Transactions on Reliability 57 (2008) 551–563.

[12] J.C. Hudson, K.C. Kapur, Reliability bounds for multistate systems with multistate components, Operations Research 33 (1985) 153–160.

[13] Internet2 Network, http://www.internet2.edu2012.

[14] C.C. Jane, J.S. Lin, J. Yuan, Reliability evaluation of a limited-<sup>fl</sup>ow network in terms of minimal cutsets, IEEE Transactions on Reliability 42 (1993) 354–361.

[15] T. Koide, S. Shinmori, H. Ishii, Ef<sup>fi</sup>cient computation of network reliability importance on k-terminal reliability, International Journal of Reliability, Quality and Safety Engineering 39 (2007) 213–226.

[16] R.C.T. Lee, S.S. Tseng, R.C. Chang, Y.T. Tsai, Introduction to the Design and Analysis of Algorithms, in: McGraw-Hill Education (Asia), 2005, pp. 167–170.

[17] Y.K. Lin, A simple algorithm for reliability evaluation of a stochastic-<sup>fl</sup>ow network with node failure, Computers and Operations Research 28 (2001) 1277–1285.

[20] Y.K. Lin, Reliability evaluation for overall-terminal multistate <sup>fl</sup>ow networks with bi-directed arcs, Expert Systems with Applications 37 (2010) 6669–6674.

[21] Y.K. Lin, C.T. Yeh, Maximizing network reliability for stochastic transportation networks under a budget constraint by using a genetic algorithm, International Journal of Innovative Computing, Information and Control 7 (2011) 7033–7050.

[22] Y.K. Lin, C.T. Yeh, Using minimal cuts to optimize network reliability for a stochastic computer network subject to assignment budget, Computers and Operations Research 38 (8) (2011) 1175–1187.

[23] J.S. Lin, C.C. Jane, J. Yuan, On reliability evaluation of a capacitated-<sup>fl</sup>ow network in terms of minimal pathsets, Networks 25 (1995).131-138

[24] T. Nakagawa, Maintenance Theory of Reliability, Springer, London, 2005.

[25] K.I. Park, QOS in Packet Networks, The MITRE Corporation USA: Springer, 2005.

[26] J.E. Ramirez-marquez, D.W. Coit, M. Tortorella, A generalized multistate-based path vector approach to multistate two-terminal reliability, IEEE Transactions on Reliability 38 (2006) 477–488.

[27] A.R. Sharafat, O.R. Ma'rouzi, All-terminal network reliability using recursive truncation algorithm, IEEE Transactions on Reliability 58 (2009) 338–347.

[28] Taiwan Advanced Research and Education Networks (TWAREN), http://www.twaren net2012.

[29] Taiwan Advanced Research and Education Networks (TWAREN), circuit down report, http://noc.twaren.net/nmrs/events/noc\_web/index\_assemble.php2012.

[30] S. Wang, J. Watada, Reliability optimization of a series-parallel system with fuzzy random lifetimes, International Journal of Innovative Computing, Information and Control 5 (2009) 1547–1558.

[31] J. Xue, On Multistate System Analysis, IEEE Transactions on Reliability 34 (1985) 329–337.

[32] R. Yarlagadda, J. Hershey, Fast algorithm for computing the reliability of communication network, International Journal of Electronics 70 (1991) 549–564.

[33] F.M. Yeh, S.K. Lu, S.Y. Kuo, OBDD-Based Evaluation of k-terminal network reliabil ity, IEEE Transactions on Reliability 51 (2002) 443–451

[34] M.J. Zuo, Z. Tian, H.Z. Huang, An ef<sup>fi</sup>cient method for reliability evaluation of multistate networks given all minimal path vectors, IIE Transactions 39 (2007) 811–817.

Yi-Kuei Lin is currently a Chair Professor and the Chairman of Industrial Management Department, National Taiwan University of Science and Technology, Taiwan, Republic of China. He received a Bachelor degree in Applied Mathematics Department from National Chiao Tung University, Taiwan. He obtained his Master degree and Ph.D. degree in the Department of Industrial Engineering and Engineering Management at National Tsing Hua University, Taiwan, Republic of China. He has the honor to get the Outstanding Research Awards from National Science Council of Taiwan in 2008 and 2010, respectively. His research interest includes performance evaluation, stochastic network reliability, operations research and telecommunication management. He has published over 130 papers in refereed journals including European Journal of Operational Research; Computers and Operations Research; Reliability Engineering & System Safety; IEEE Transactions on Reliability; IEEE Transactions on Systems, Man, and Cybernetics–Part A: Systems and Humans; Information Sciences; International Journal of Production Economics; and Applied Mathematics and Computation.

Louis Cheng-Lu Yeng obtained his Ph.D. degree in Graduate Institute of Management at National Taiwan University of Science and Technology. He previously was CIO of listed company in Taiwan for over 10 years. Before that he was system analyst of Texas Instrument for manufacturing related system. Currently he has partnership of a company in U.S. He graduated from the Feng-Chia University with a BA degree of Applied Mathematic in Taiwan in 1988 and studied the Decision Support System since then, and received his MS degree in Computer Science at the University of Massachusetts in U.S. in 1994. His research interests include the stochastic network reliability, decision support system and business administration.
