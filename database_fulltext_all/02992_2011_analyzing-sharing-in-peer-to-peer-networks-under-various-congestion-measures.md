---
otero_id: 2992
otero_key: "8E84VMS2"
title: "Analyzing Sharing in Peer-to-Peer Networks Under Various Congestion Measures"
authors: "Monica Johar; Syam Menon; Vijay Mookerjee"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0258"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/8E84VMS2/fulltext/images/07dd2f9a73bc51c39e2053fcfc665496eb843aa2c44868c425ad068723264622.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Analyzing Sharing in Peer-to-Peer Networks Under Various Congestion Measures

Monica Johar, Syam Menon, Vijay Mookerjee,

## To cite this article:

Monica Johar, Syam Menon, Vijay Mookerjee, (2011) Analyzing Sharing in Peer-to-Peer Networks Under Various Congestion Measures. Information Systems Research 22(2):325-345. http://dx.doi.org/10.1287/isre.1090.0258

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/8E84VMS2/fulltext/images/cae1e55863b7e14de1fc877348cd53b23d9524c0f2fb33a9c1999fc3bfa25835.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Analyzing Sharing in Peer-to-Peer Networks Under Various Congestion Measures

Monica Johar

The Belk College of Business, University of North Carolina at Charlotte, North Carolina 28223, msjohar@uncc.edu,

Syam Menon, Vijay Mookerjee School of Management, The University of Texas at Dallas, Richardson, Texas 75080 {syam@utdallas.edu, vijaym@utdallas.edu}

istorically, the use of peer-to-peer (P2P) networks has been limited primarily to user-initiated exchanges of (mostly music) files over the Internet. This traditional view of P2P networks is changing, however, and the use of P2P networks has been suggested for delivering general-purpose content over the Web (or corporate intranets), even in real time. We analyze sharing in a P2P community in this new context under three different congestion measures: delay, jitter, and packet loss. Sharing is important to study in the presence of congestion because most existing research on P2P networks views congestion in the network as a relatively insignificant criterion. However, when delivering general-purpose content, congestion and its relationship to sharing is a critical factor that influences end-user performance. This paper looks at P2P networks from this new perspective by explicitly considering the effects of congestion on user incentives for sharing. We also propose a simple incentive mechanism that induces socially optimal sharing.

Key words: peer-to-peer networks; congestion; sharing; socially optimal sharing; free-riders

History: Paulo Goes, Senior Editor; H. Raghav Rao, Associate Editor. This paper was received on

March 27, 2008, and was with the authors 4 months for 2 revisions. Published online in Articles in Advance December 15, 2009.

## 1. Introduction

The explosive growth of the Internet over the last decade or so has made it a necessary part of everyday life. Over this period, various technologies have evolved to facilitate the efficient delivery of content over the Internet, with content delivery networks (CDNs) and peer-to-peer (P2P) networks being two of the more popular ones among them. Both CDNs and P2P networks essentially use a distributed solution for content delivery. Content delivery networks rely on replicating and caching content at appropriate nodes that are closer to demand centers, thereby reducing network congestion and server overload. Content delivery networks have been successfully used by large corporations like Motorola (Carr 2003), and by content delivery companies such as Akamai. P2P networks, as the name suggests, are often social networks designed to bring together groups of people with similar interests. Although these have also found wide application, they have been recognized primarily for use in situations where congestion is not particularly critical, like distributed computing (e.g., distributed.net, SETI@home) and file sharing (e.g., Gnutella, Kazaa).

In this paper, we consider newer, congestionsensitive applications of P2P networks and study the effects of congestion on sharing. Our focus is to understand how the goal of reducing congestion can influence peering participants to share content with one another. To isolate the impact of congestion, we do not consider factors that can directly lead to sharing, such as altruism. We first analyze the effect of congestion on the sharing decisions of rational, self-interested individuals to see if they may have an incentive to share in the absence of externally imposed rewards or punishments. Because we find that participants naturally share less than the socially optimum level, we propose and analyze a simple incentive mechanism that leads to optimal sharing.

The specific context in which we study sharing is one of a congested P2P network that delivers timesensitive, general-purpose content (e.g., news stories, streamed movies, etc.). The term general purpose is used to convey that we are interested in P2P applications where the content is of general interest to a user community, such as a weather report or a popular movie that is being streamed to a group of consumers. On the other hand, P2P applications designed for the point-to-point delivery of content of local interest (such as a phone conversation in a VOIP application) are not the focus of this study. The presence of congestion in the network is important in our study because its presence can degrade the quality of service received by users. The question of interest is whether congestion could lead to sharing. Here we find that unless common (or shared) resources are congested, sharing is not likely to occur. Although content delivery networks often explicitly consider congestion in the design of the network (Huang and Abdelzaher 2005), congestion is seldom considered important in conventional applications of P2P networks. This has changed recently, however, with various P2P applications for distributing general-purpose content, often with relatively tight delay constraints, e.g., news stories, streamed content (Xu et al. 2006), and multicasting (Pouwelse et al. 2004, Parameswaran et al. 2001).

We provide two real examples of the new breed of P2P networks that are the focus of this study. Kontiki (recently acquired by Verisign) provides a P2P environment that will be used in AOL’s In2TV effort to make available for download thousands of old television shows free of charge. The JXTA technology from Sun Microsystems provides a set of open, generalized peer-to-peer protocols that facilitate the development of distributed, cooperative applications; an application developed for the National Association of Realtors using this technology allows users to “query local or remote listings for the most accurate, up-to-the minute information, without requiring the member databases to forfeit their autonomy or be forced to fund a centrally managed database” (http:// www.sun.com/software/jxta/).

## 1.1. Congestion Measures

We consider three distinct, but related, measures of congestion: delay, jitter, and packet loss in the delivery of general-purpose content via a congested P2P network. We discuss these measures next.

Similar to the case of content delivery networks, delay remains a significant measure of quality in the new P2P environments considered in this paper. For example, high delays can considerably degrade the value of the content reaching the end user, e.g., financial news (Vogells et al. 2002). In more real-time environments such as streaming, P2P implementations are subject to even more stringent timing constraints (Yeh and Pui 2005). Pouwelse et al. (2004) describe the importance of delays in developing a real-time video delivery system using peer-to-peer networks. Additional examples of delay-sensitive applications include multicast streaming applications (Pucha et al. 2007) such as NICE (Banerjee et al. 2002) and Split-Sream (Castro et al. 2003). Indeed, delay is particularly important in many of these applications because the content being distributed is free and the objective of participants is usually to consume such freely available content at minimum delay. On the other hand, prior research on P2P networks has focused primarily on technical aspects such as network topology or distribution protocols (Asvanund et al. 2003), as well as economic issues not directly related to delay (Golle et al. 2001).

Jitter (the variance of delay) in a P2P network is particularly relevant for real-time content delivery. This is because video encoders capture and send video at a certain rate, and the receivers need to decode and display frames at the same rate. Each frame has a specific deadline by which it must be received and displayed, and a frame arriving after its deadline is not useful. In addition, it is often the case that subsequent frames depend on the frame that has arrived late, and therefore the damaging effects of a delayed frame can escalate.

Finally, we consider packet loss as a congestion measure. This measure is designed to capture the fact that the content distribution application may not wait indefinitely for a packet to be delivered; when the delivery delay exceeds a threshold, an alternative needs to be found for the requested packet. We consider a packet that has exceeded a delivery delay threshold to be lost.

## 1.2. Congestion Driven Sharing

As mentioned earlier, the main focus of this study is to examine sharing in a congested P2P network. Specifically, we are interested in examining sharing decisions that are made voluntarily, rather than those that are implicitly imposed on the end user by the manner in which the P2P application functions.

Although several P2P media-streaming solutions have been proposed by researchers, the highscalability potential of P2P networks often relies heavily on the individual peers contributing their resources voluntarily. However, such collaboration does not always occur; for example, many believe free-riding to be a major challenge that threatens the existence and usefulness of P2P networks (Habib and Chuang 2004). Moreover, the challenges posed by high-bandwidth live-media streaming differ from those encountered in traditional P2P file sharing. In P2P streaming, bandwidth becomes the bottleneck resource, and the peer’s perceived quality of service (QoS) requires the stream to start flowing within a few seconds of the request and have very low delay, jitter, packet loss, and failure probability (Kant et al. 2002). Thus, sharing in such P2P applications is a real issue. Our analysis helps by deriving sharing results concerning the extent of sharing that occurs in equilibrium in a variety of P2P networking scenarios.

A related issue we study is how incentive schemes can be designed to induce sharing that is optimal from the perspective of a central planner or network designer. Although prior research has considered incentive schemes, it is in the context of traditional P2P networks, such as file-sharing networks. In this context, Pai and Mohr (2006) observe that incentive schemes designed for file-sharing protocols perform very poorly when applied to streaming systems, because of the strict time and bandwidth constraints and intolerance to long delays. To this end, a variety of incentive schemes have been proposed for delivering time-sensitive content in a P2P network. These schemes often rely on a penalty that discourages low sharing. Pai and Mohr (2006) propose an incentive scheme wherein the probability of suffering packet loss is inversely proportional to the upload bandwidth contributed. Chu et al. (2004) derive a mechanism in which resource-rich peers contribute more bandwidth to the system, thereby subsidizing resource-poor peers. Habib and Chuang (2004) use a score-based incentive mechanism that provides an indirect mapping between contribution and benefit. Tan and Jarvis (2006) also propose a similar incentive mechanism for P2P streaming using an internal currency called “points” to represent a peer’s contribution level.

Although the above incentive schemes have all been developed for time-sensitive P2P applications of the kind we consider, the approach in these studies is experimental: A scheme is proposed (but not analyzed) and its properties studied via simulation experiments. In contrast, we propose and analyze an incentive scheme that is guaranteed to coordinate, i.e., produce the same solution as the one arrived at by the social planner.

The rest of this paper is organized as follows. Section 2 describes the basic problem setting, presents the underlying assumptions, and describes the parameters used. In §3 we analyze the sharing of participants in an m-participant, peer-to-peer network. Section 4 numerically investigates the impact of various problem parameters on the sharing level. In §5 we study some extended scenarios, including the impact of a central planner. Section 6 summarizes and concludes the paper.

## 2. Modeling Congestion in a P2P Network

This section introduces a simple structured model of a peer-to-peer network used for general-purpose content delivery (such as weather, news, etc.). We consider rational, nonaltruistic participants and investigate whether (and under what circumstances) the objective of reducing congestion induces sharing among the participants. To this end, we propose three measures of congestion that could be of interest to participants in different peer-to-peer network applications.

Figure 1 Simple Model of a Peer-to-Peer Network  
![](/api/attachments/8E84VMS2/fulltext/images/65a83efbb235d1a3a165f69f8aa217e9966252f966ade41829ba87d34a8ba7af.jpg)

Figure 1 depicts the setting of our model. The peering community consists of m participants, and there are a total of n items (Web pages, documents, multimedia files, etc.) that are of interest to the community, and each participant has a cache that can store an average of R items. When a participant requests an item that is already present in the cache, the request is satisfied with zero delay. In the event of a cache miss, items are requested from other participants using a flooded-request model (Milojicic et al. 2002). This approach is common for peer-to-peer streaming applications such as GnuStream (Jiang et al. 2003) and LimeWire (http://www.limewire.com). It has the advantage of being fully decentralized and scalable. Researchers have also studied iterated forms of flooded request (gossiplike) protocols for peer-topeer streaming (Kempe et al. 2003, Rejaie and Stafford 2004). In a flooded-request model, requests are broadcast to all other participants, and no directory information is tracked by any participant. A request can be satisfied by one or more sharing participants that can supply the item. Alternatively, if no sharing participant can supply the requested item, the request is satisfied via the external link E that connects the peering community with the rest of the Internet. In either case, the participant’s internal link must be used to finally deliver the content.

We assume that the participants are homogenous in the average traffic they generate, $P _ { m } H _ { 0 } f$ . Here, $P _ { m }$ is the probability that a requested item is not available in the participant’s own cache, $H _ { 0 }$ is the average access rate in terms of items per second, and f is the average number of packets generated in a request. The notation relevant to our analysis is summarized in Table 1.

Table 1 Notation

<table><tr><td>Variable</td><td>Description</td><td>Units</td></tr><tr><td> $M$ </td><td>Number of participants</td><td>—</td></tr><tr><td> $P_{m}$ </td><td>Cache-miss probability</td><td>—</td></tr><tr><td> $N$ </td><td>Total number of items</td><td>—</td></tr><tr><td> $H_{0}$ </td><td>Average request rate</td><td>Item requests per unit time</td></tr><tr><td> $F$ </td><td>Number of packets per item</td><td>—</td></tr><tr><td> $\mu_{z}$ </td><td>External link capacity</td><td>Packets per unit time</td></tr><tr><td> $\mu_{i}$ </td><td>Internal link capacity for  $i$ </td><td>Packets per unit time</td></tr><tr><td> $R$ </td><td>Cache capacity in number of items</td><td>—</td></tr><tr><td> $\lambda_{i}$ </td><td>Average traffic generated by participant  $i$ </td><td>Packets per unit time</td></tr><tr><td> $\lambda_{z}$ </td><td>Average traffic on external link</td><td>Packets per unit time</td></tr><tr><td> $q_{i}$ </td><td>Level of sharing for participant  $i (0 \leq q_{i} \leq 1)$ </td><td>Decision variable</td></tr></table>

## 2.1. Congestion Measures

Because the congestion in the system is negatively correlated to the quality of service received, each participant minimizes congestion by choosing a sharing level $q _ { i } , 0 \leq q _ { i } \leq 1$ , where $q _ { i }$ is the proportion of the cache that participant i shares with the rest of the peering community. We consider the following three measures of congestion.

2.1.1. Total Delay. One reasonable measure of congestion in the network is the expected time taken to satisfy a participant’s request. The random time to satisfy a request made by participant l is given by

$$
\tilde{\tau}_{l} = \sum_{\substack{i = 1\\ i\neq l}}^{m}\tilde{X}_{il}(\tilde{\tau}_{l}^{l} + \tilde{\tau}_{l}^{i}) + \tilde{X}_{iz}(\tilde{\tau}_{l}^{l} + \tilde{\tau}_{l}^{z}).
$$

Here, $\tilde { \tau } _ { i } ^ { i }$ represents the time spent by peer $l { ' } s$ request on $l ^ { \prime } \mathrm { s }$ internal (or self) link, $\tilde { \tau } _ { l } ^ { i }$ represents the time spent on a peer link, and $\tilde { \tau } _ { l } ^ { z }$ represents the time spent on the external link. $\tilde { X } _ { i l } \in \dot { \{ 0 , 1 \} }$ is a discrete random variable such that $\tilde { X } _ { i l } = 1 \mathrm { i f } l ^ { \prime } { \mathrm { s } }$ request is satisfied by peer $i ,$ and 0 otherwise. Similarly, $\tilde { X } _ { i z } = 1$ if participant l’s request is satisfied by the external link, and 0 otherwise. Note that $\tilde { X } _ { i l } + \tilde { X } _ { i z } ^ { ' } = 1$

The expected time for a packet to be received over a link is calculated using an $\mathrm { M } / \mathrm { G } / 1 / \mathrm { P S }$ queuing model. This model assumes an exponentially distributed arrival of packets, but the service time distribution can follow any general distribution. A link is modeled as a processor-sharing queue because multiple requests share the transmission capacity of the link. This queuing model is consistent with a wide body of work in the area (Roberts and Massoulie 2000, Fredj et al. 2001, Kherani and Kumar 2000). With the M/G/1/PS assumptions, the average time spent by a packet on the internal link for participant l is $\dot { E [ \tilde { \tau } _ { l } ^ { l } ] } \dot { = } \delta _ { l } = ( \mu _ { l } - \lambda _ { l } ) ^ { - 1 }$ , whereas that in the external link is $E [ \tilde { \tau } _ { l } ^ { z } ] = \delta _ { z } = ( \mu _ { z } - \lambda _ { z } ) ^ { - 1 }$ and the time spent on a neighboring participant $i ^ { \prime } \mathrm { s }$ link is $E [ \tilde { \tau } _ { l } ^ { i } ] = \hat { \delta } _ { i } =$ $( \mu _ { i } - \lambda _ { i } ) ^ { - 1 }$ . The total delay for a packet experienced by participant l has two components: (i) the delay experienced when content is supplied by a neighboring peer, $\begin{array} { r } { \sum _ { i = 1 , i \neq l } ^ { m } p _ { i } ( \delta _ { i } + \delta _ { l } ) } \end{array}$ , and (ii) the delay associated with receiving content from the external link, $p _ { z } ( \delta _ { z } + \delta _ { l } )$ Here, $p _ { z }$ is the probability that the request is satisfied by using the external link, and $p _ { i }$ is the probability that the request is satisfied by using peer $i ^ { \prime } \bar { \bf s }$ link.

The objective of each participant in the system is to minimize total expected delay per packet, $W _ { l } ^ { \mathrm { D e l a y } } ,$ by choosing an appropriate sharing level $q _ { l }$ that could affect the delay terms $\delta _ { z } , \delta _ { i } ,$ and $\delta _ { l }$ .

$$
\begin{array}{c}\underset {q_{l}}{\text{Min}}  W_{l}^{\text{Delay}} = \bigg(p_{z}(\delta_{z} + \delta_{l}) + \sum \limits_{\substack{i = 1\\ i\neq l}}^{m}p_{i}(\delta_{i} + \delta_{l})\bigg),\\ \text{where}\delta_{z}\geq 0, \delta_{i}\geq 0 \forall i\in \{1,\ldots ,m\} \end{array}
$$

2.1.2. Jitter. Jitter measures the variability in the time taken for packet arrival. Many Internet environments, such as streaming real-time applications, are vulnerable to the variation of the end-to-end delays (or jitter) (Trajkovic and Golestani 1992, Venkatasubramanian and Nahrstedt 1997). In such cases, jitter (rather than total delay) is a more appropriate measure of congestion to be minimized (Mansour and Patt-Shamir 1998, Galenbe et al. 2002). The expression for jitter is given by $g ( \tilde { \tau } _ { l } ) = E ( \tilde { \tau } _ { l } ^ { 2 } ) \ -$ $[ \hat { E ( \tau _ { l } ) } ] ^ { 2 }$ . Assuming an exponential service time distribution, the variance in the delay on internal link l is given by, $\zeta _ { l } = E [ g ( \tilde { \tau } _ { l } ^ { l } ) ] = \dot { \lambda } _ { l } / \mu _ { l } ^ { 2 } ( \mu _ { l } - \lambda _ { l } ) .$ whereas that on the external link $\zeta _ { z } = E [ g ( \tilde { \tau } _ { l } ^ { z } ) ] =$ $\lambda _ { z } / \mu _ { z } ^ { 2 } ( \mu _ { z } - \lambda _ { z } )$ (Coffman et al. 1970).

The jitter experienced by peer l has three components: (i) the jitter experienced on the self link, $\zeta _ { l } ;$ (ii) the jitter experienced when a request satisfied by a neighboring peer $i , \ \Sigma _ { i = 1 , \ i \neq l } ^ { m } \zeta _ { i } p _ { i } ^ { 2 } ;$ and (iii) the jitter experienced when the request is satisfied by the external link, $p _ { z } ^ { 2 } \zeta _ { z }$

The objective of each participant in the system is to minimize its variation in delay per packet, $W _ { l } ^ { \mathrm { J i t t e r } } .$ by choosing an appropriate sharing level $q _ { l }$ that could affect the jitter terms $\bar { \zeta } _ { z } , \bar { \zeta } _ { i } , \bar { \zeta } _ { l }$

$$
\begin{array}{c} \underset {q _ {l}} {\text {Min}}   W _ {l} ^ {\text {Jitter}} = \left(\zeta_ {l} + \sum_ {i = 1,   i \neq l} ^ {m} \zeta_ {i} p _ {i} ^ {2} + p _ {z} ^ {2} \zeta_ {z}\right) \quad \text {where}, \\ \zeta_ {z} \geq 0,   \zeta_ {i} \geq 0   \forall   i \in \{1, \ldots , m \}. \end{array}
$$

2.1.3. Proportion of Packets Lost in the System. Another congestion metric used to measure the quality of service over the Internet is packet loss (Paxson 1997, Jiang and Sehulzrinne 2000). For multimedia applications, packet loss typically results from congestion in the network that causes the play-out deadline of a request to be missed (Sanneck and Carle 2000). The “loss” of a packet is defined as the event that a requested packet has not arrived before a delivery constraint that is influenced by the end-user’s preference for quality. Because the preference for quality could vary across users and across sessions for the same user, we allow for some randomness in the delivery constraint rather than considering it as deterministic. For the $\mathrm { M } / \mathrm { G } / 1 / { \infty } / \mathrm { P S }$ queue, we can calculate the probability that a packet is lost on link l as $h _ { l } = \nu ( \bar { \mu _ { l } } - \lambda _ { l } + \nu ) ^ { - 1 }$ (refer to the appendix). Here $1 / \nu$ is the mean exponential delay tolerance for a packet, beyond which it is considered to have been lost. Furthermore, when peer i satisfies peer $l ^ { \prime } s$ request, the probability that the packet is lost is given by $h _ { l } + h _ { i } -$ $\bar { h } _ { l } h _ { i }$ (refer to the appendix). Note that the packet loss experienced by peer l has two components: (i) probability that the packet is lost when consuming content from another peer, $\begin{array} { r } { \sum _ { i = 1 , i \neq l } ^ { m } p _ { i } ( h _ { l } + h _ { i } - h _ { l } h _ { i } ) } \end{array}$ and (ii) probability of packet loss when consuming content from the external link, $p _ { z } ( h _ { l } + h _ { z } - h _ { l } h _ { z } )$ . The objective of each participant in the system is to minimize the probability that a packet is lost, $W _ { l } ^ { \mathrm { P a c k e t \ L o s s } } ,$ , by choosing an appropriate sharing level $q _ { l }$ that could affect the loss terms $h _ { z } , h _ { l } , h _ { i }$

$$
\begin{array}{l} \underset {q _ {l}} {\text {Min}} W _ {l} ^ {\text {Packet Loss}} = p _ {z} (h _ {l} + h _ {z} - h _ {z} h _ {l}) \\ \qquad \qquad \qquad + \sum_ {i = 1,   i \neq l} ^ {m} p _ {i} (h _ {l} + h _ {i} - h _ {i} h _ {l}) \quad \text {where}, \\ \qquad \qquad \qquad \qquad h _ {z} \geq 0,   h _ {i} \geq 0   \forall   i \in \{1, \ldots , m \}. \end{array}
$$

## 2.2. Model Trade-Offs: Positive and Negative Effects of Sharing

In the next section, we consider two scenarios that differ in terms of how the congestion on the external link is perceived by the participants in the P2P system. In the first case, the congestion on the external link is viewed as constant. This is representative of a situation where the common external resource shared by the participants is insensitive to the sharing level chosen by the participants in the network. This may be a reasonable approximation when the external link has abundant excess capacity. On the other hand, this may also represent a situation in which the participants are simply not alert to the fact that their sharing decisions impact the congestion on the external link. As a result, the participants do not take into account the congestion on the external link while choosing their sharing levels. In the second case, we consider a congestible external resource. Here the congestion on the external link is a function of the sharing of the participants, and participants take this congestion into account while choosing their sharing levels.

The key trade-off in our model is between the negative and positive effects of sharing. The negative effect of sharing manifests itself as the higher congestion experienced by a sharing participant as a result of uploading by participants. The positive effect has two components. The first is an internal one: By diverting traffic to one’s internal link, a sharing participant can reduce congestion on the internal links of other participants. This effect results entirely from self-interest, because less-congested participant links provide faster response when a peer is used to satisfy a request. The second positive effect is external: A sharing participant can reduce congestion on the external link, thus providing benefits when this link is used for self-traffic. Of course, the second positive effect gets nullified (i.e., it cannot drive sharing) in the case where the participants do not consider the external link to be congestible.

Note that the negative effect of sharing arises from our assumption that the congestion on a participant’s internal link increases with the level of sharing chosen by this participant. Although traditional TCP/IP networks are designed to have separate upload and download capacities, there is ample evidence that upload traffic and link delays are not independent of each other. Balakrishnan et al. (1997) have shown that network performance depends on the traffic and link characteristics in both directions of data transfer. This is attributed largely to the imperfection and variability of the acknowledgment feedback from the sender to receiver and is found in both wired and wireless TCP/IP networks (Leith et al. 2005, Pilosof et al. 2003). These effects are further exacerbated by the asymmetry in TCP/IP networks where available capacities for uploads are typically much lower than those for downloads (Balakrishnan and Padmanabhan 2001).

Habib and Chuang (2004) provide direct evidence of the negative effect of sharing. Using packet-level simulation and Internet experiments, they study the impact of peer noncooperation on the performance of a P2P media-streaming system (PROMISE). They investigate whether there is a significant cost of sharing resources, especially bandwidth. Their experiments clearly demonstrate that there is a cost (or drop in performance) associated with uploading: Too much uploading hurts a peer. Similar results are reported by Feldman et al. (2003), who propose that the basic rationale for not sharing is that downloading becomes slower. They verify this phenomenon using a simulator, where the use on a peer’s incoming link is observed in relation to the number of outgoing flows. As a peer begins to upload, use on the incoming link drops for both Ethernet and DSL nodes. Along the same lines, Golle et al. (2001) and Cunningham et al. (2004) associate a bandwidth cost of sharing in P2P networks. The cost arises because download bandwidth is sacrificed while uploading files to other participants. For the mathematical analysis in the next section, we will assume that upload and download traffic affect congestion in the same manner.

This assumption is relaxed in $\ S 5 ,$ where we numerically investigate nonuniform impacts of upload traffic on download delay and download traffic on upload delay.

## 3. Analysis of Sharing Under Congestion

In this section, we further develop the model and analyze it to derive several results concerning the level of sharing in a P2P community that is faced with congestion. We first derive the expressions for the traffic on the external and internal links. Let $\lambda _ { i }$ be the arrival rate of traffic on the link connecting participant i to the network. This traffic is composed of self-generated traffic and traffic generated as a result of supplying requests for items to other participants. The self-generated traffic is not a function of the sharing decision and is simply $P _ { m } H _ { 0 } f$ . The peer-generated traffic can result from a request by any of $( m { - } 1 )$ peers and will exist only when participant i is sharing and has the requested item in cache, which can happen with a probability of $q _ { i } \times ( R / n )$ . It is convenient to introduce $\rho _ { j i }$ as the conditional probability that participant j receives the item from participant $i ,$ given that participant i is sharing. The arrival rate of traffic for participant i can then be written as

$$
\lambda_ {i} = P _ {m} H _ {0} f \left(1 + q _ {i} \frac {R}{n} \sum_ {j \neq i} \rho_ {j i}\right), \quad \text { where }
$$

$$
\begin{array}{l}\rho_{ji} = 1 + \sum_{\substack{a = 1\\ a\neq j,i}}^{m}\bigg\{-\frac{1}{2} q_{a}\frac{R}{n} +\sum_{\substack{b = a + 1\\ b\neq j,i}}^{m}\bigg\{\frac{1}{3} q_{a}\frac{R}{n} q_{b}\frac{R}{n}\\ \\ \qquad \qquad +\sum_{\substack{c = b + 1\\ c\neq j,i}}^{m}\bigg\{-\frac{1}{4} q_{a}\frac{R}{n} q_{b}\frac{R}{n} q_{c}\frac{R}{n} +\dots \bigg\} \bigg\} \bigg\} \bigg\} . \end{array}
$$

Hence, the probability that the requested packet is obtained using peer $i ^ { \prime } \mathrm { s }$ link is given by

$$
p _ {i} = q _ {i} \frac {R}{n} \rho_ {i j}.
$$

Similarly, $\lambda _ { z } ,$ the arrival rate of traffic on the external link, is the sum of the traffic generated by each participant on the external link. The traffic generated by participant i on the external link is simply the participant’s self-traffic $P _ { m } H _ { 0 } f$ multiplied by the probability that participant i’s request is not satisfied by any other participant in the community, given by

$$
p_{z} = \prod_{\substack{j = 1\\ j\neq i}}^{m}\biggl (1 - q_{j}\frac{R}{n}\biggr).
$$

Thus, the arrival rate of traffic on the external link can be written as

$$
\lambda_{z} = \sum_{i = 1}^{m}\bigg(P_{m}H_{0}f\prod_{\substack{j = 1\\ j\neq i}}^{m}\bigg(1 - q_{j}\frac{R}{n}\bigg)\bigg).
$$

## 3.1. Heterogeneous Participants with a Noncongestible External Link

In this section we consider a peer-to-peer community of m participants with a noncongestible external link. In other words, delay, jitter, and packet loss in the link that connects this peer-to-peer community to the rest of the Internet are either insensitive to the sharing of the participants in the network or are (incorrectly) perceived by them as such. Consequently, the participants do not believe that their sharing decision impacts the delay, jitter, or packet loss on the external link, and treat it as being constant when making their sharing decisions. To make our analysis more general, we allow the participants to be heterogeneous in their internal link capacities, i.e., $\mu _ { i }$ can be different for each participant i.

Consequently, the three congestion measures for participant l can be rewritten as

(i) Total delay<sup>1</sup>:

$$
W _ {l} ^ {\text { Delay }} = \left(p _ {z} (D _ {z} + \delta_ {l}) + \sum_ {i = 1, i \neq l} ^ {m} p _ {i} (\delta_ {i} + \delta_ {l})\right),
$$

where $D _ { z }$ is the constant external link delay, which is independent of the sharing decisions of the participants.

(ii) Jitter:

$$
W _ {l} ^ {\text {Jitter}} = \left(\zeta_ {l} + \sum_ {i = 1, i \neq l} ^ {m} \zeta_ {i} p _ {i} ^ {2}\right).
$$

Note that for a noncongestible external link the total jitter experienced by the participants is assumed to be independent of the jitter on the external link.

(iii) Packet Loss:

$$
W _ {j} ^ {\text { Packet   Loss }} = p _ {z} (h _ {j} + H _ {z} - h _ {j} H _ {z}) + \sum_ {r \neq j} p _ {r} (h _ {j} + h _ {r} - h _ {j} h _ {r}),
$$

where $H _ { z }$ is the constant packet loss rate on the external link, independent of the sharing decisions of the participants.

<sup>Proposition</sup> <sup>1.</sup> Only a nonsharing equilibrium $q _ { i } ^ { * } = 0 ;$ $\forall i \in ( 1 , \ldots , m )$ can exist in a system of m participants heterogeneous in their internal link capacities, when the external link delay, jitter, or packet loss is constant.

<sup>Proof.</sup> Refer to the appendix.

Proposition 1 states that when the participants in the network do not perceive a common congested external resource, there is no sharing. Note that the above result holds even though the participants may perceive internal resources to be congestible. This implies that the internal positive effect of sharing that results when a sharing participant relieves some traffic on the internal links of all other participants in the community is not enough to overcome the negative effect of sharing, namely, the increased congestion in the internal link. Cooperation to relieve internal congestion is therefore predicated on the fact that the participants share. When other members do not share, even a wellintentioned participant will not share, because relieving internal congestion on the links of nonsharing participants could hurt this participant. This result holds despite the fact that a participant may have a much higher internal link capacity than others—to benefit from relieving congestion on other participants’ links by sharing, it is necessary for those participants to share. Hence, an equilibrium outcome is one of nonsharing.

The statement of the proposition is, of course, much stronger: No equilibrium outcome other than a nonsharing one is possible under these conditions. Although the proof is tedious, the intuition behind the proof is easy to understand. Consider any level of sharing q for all participants, except a particular participant i. It is easy to see that if the sharing level of all other participants is fixed at q, it may be optimal for participant i to share. Hence, one might be led to believe that a sharing equilibrium may be possible under these conditions. However, the above situation cannot arise in equilibrium for a link congestion measure that is convex in the traffic. Assuming that we begin with a condition where equal traffic is flowing on all links, it never pays (for a congestion measure function that is convex in the traffic) for a participant to divert some traffic to oneself, because this participant’s congestion would increase more than the congestion reduction it would cause on the link of the participant from whom the traffic is diverted.

Thus, in the absence of a common congestible resource (whose availability does not depend on sharing), we observe a prisoner’s dilemma where no participant shares. This nonsharing result can be interpreted as a tragedy of the commons; because all participants assume that the external link is abundant, they do not see the need to share to reduce the congestion on an already abundant resource.

## 3.2. Homogeneous Participants with a Congestible External Link

In this section we consider the same structured model of a P2P community, but with a congestible external link. The external link delay, jitter, or packet loss therefore is not constant and depends on the amount of traffic, which in turn depends on the sharing decisions of the participants. In addition, we assume the m participants to be homogeneous in their internal link capacities ${ \mathrm { ( i . e . , ~ } \mu _ { i } = \mu }$ for each participant i) for tractability and to offer useful insights.

We conduct the analysis for one participant $B _ { 1 } ,$ and then invoke symmetry. Let $q _ { 1 }$ be the sharing level for this participant. Define $q _ { i } = q ~ \forall i \neq 1$ . Let $\lambda _ { 1 }$ be the arrival rate of traffic on the link connecting $B _ { 1 }$ to the network, and let $\delta _ { 1 }$ be the delay experienced by $B _ { 1 }$ as a result of the traffic $\lambda _ { 1 }$ . The traffic is composed of self-generated traffic, and traffic generated as a result of requests for items from peers. The self-generated traffic is not a function of the sharing decision, and is simply $P _ { m } H _ { 0 } f$ . The peer-generated traffic can result from any of $( m - 1 )$ peers and will exist only when $B _ { 1 }$ is sharing and has the item, which happens with probability $q _ { 1 } \times ( R / n )$ . A request from a peer is satisfied by $B _ { 1 }$ with a probability $( q R / n ) ^ { s } ( 1 - \mathbf { \bar { q } } R / n ) ^ { ( m - 2 - s ) }$ $1 / ( s + \bar { 1 ) }$ , where s is the number of peers of $B _ { 1 }$ who also have the item. The value of s can be any integer between 0 and $( m - 2 )$ . Therefore, over all possible values of $s ,$ this probability is $\textstyle \{ \sum _ { s = 0 } ^ { m - 2 } { \binom { m - 2 } { s } } ( q \dot { R } / n ) ^ { s }$ $( 1 - q R / n ) ^ { ( m - 2 - s ) } 1 / ( \hat { s + 1 } ) \}$ . Consequently,

$$
\begin{array}{l} \lambda_ {1} = P _ {m} H _ {0} f \bigg [ 1 + \frac {q _ {1} R}{n} (m - 1) \\ \qquad \cdot \left\{\sum_ {s = 0} ^ {m - 2} \binom {m - 2} {s} \left(\frac {q R}{n}\right) ^ {s} \left(1 - \frac {q R}{n}\right) ^ {(m - 2 - s)} \frac {1}{s + 1} \right\} \bigg ]. \end{array}
$$

Similarly, , the traffic on the internal links of participants $2 , \ldots , m - 1$ , m, and $\lambda _ { z } ,$ respectively, can be obtained as

$$
\begin{array}{r l} \lambda = P _ {m} H _ {0} f & \left[ 1 + \frac {q R (m - 2)}{n} \right. \\ & \cdot \left\{\frac {q _ {1} R}{n} \sum_ {s = 0} ^ {m - 3} \binom {m - 3} {s} \left(\frac {q R}{n}\right) ^ {s} \left(1 - \frac {q R}{n}\right) ^ {(m - 3 - s)} \right. \\ & \cdot \frac {1}{s + 2} + \left(1 - \frac {q _ {1} R}{n}\right) \sum_ {s = 0} ^ {m - 3} \binom {m - 3} {s} \left(\frac {q R}{n}\right) ^ {s} \\ & \cdot \left(1 - \frac {q R}{n}\right) ^ {(m - 3 - s)} \frac {1}{s + 1} \Bigg \} \\ & + \frac {q R}{n} \sum_ {s = 0} ^ {m - 2} \binom {m - 2} {s} \left(\frac {q R}{n}\right) ^ {s} \left(1 - \frac {q R}{n}\right) ^ {(m - 2 - s)} \frac {1}{s + 1} \Bigg ] \end{array}
$$

and

$$
\begin{array}{c} \lambda_ {z} = P _ {m} H _ {0} f \bigg [ \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 1)} \\ + (m - 1) \bigg (1 - \frac {q _ {1} R}{n} \bigg) \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 2)} \bigg ]. \end{array}
$$

Therefore, the three congestion measures for participant $B _ { 1 }$ can be rewritten as follows.

3.2.1. Total Delay. The total delay for participant $B _ { 1 }$ has three components—(i) the self-delay, $\delta _ { 1 } \bar { ; } \ ( \mathrm { i i } )$ the delay associated with a peer, $( 1 - ( 1 - q \dot { R _ { / } } n ) ^ { m - 1 } ) \delta ;$ and (iii) the delay associated with the external link, $( 1 - q R / n ) ^ { m - 1 } \delta _ { Z }$ . Therefore, the total delay for $B _ { 1 }$ is

$$
\begin{array}{c} W _ {1} ^ {\text {Delay}} (q _ {1} \mid q, \ldots , q) = \bigg (\delta_ {1} + \bigg (1 - \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 1)} \bigg) \delta \\ + \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 1)} \delta_ {z} \bigg). \end{array}
$$

3.2.2. Jitter. The jitter experienced by peer $B _ { 1 }$ has three components: (i) jitter experienced on the selflink, $\zeta _ { 1 } ; ( \mathrm { i i } \bar { ) }$ jitter experienced when a request is satisfied by a neighboring peer, $( 1 - ( 1 - q R / \bar { n } ) ^ { ( m - 1 ) } ) ^ { 2 } \zeta ;$ and (iii) jitter experienced when the request is satisfied by the external link, $( ( 1 - q R / n ) ^ { ( m - 1 ) } ) ^ { 2 } \dot { \zeta } _ { z }$

$$
\begin{array}{l} W _ {1} ^ {\text { Jitter }} (q _ {1} | q, \dots , q) \\ = \zeta_ {1} + \left(1 - \left(1 - \frac {q R}{n}\right) ^ {(m - 1)}\right) ^ {2} \zeta + \left(\left(1 - \frac {q R}{n}\right) ^ {(m - 1)}\right) ^ {2} \zeta_ {z}. \end{array}
$$

3.2.3. Packet Loss. Note that the packet loss experienced by peer l has two components: (i) packet loss when consuming content from a neighboring peer,

$$
\big (1 - (1 - q R / n) ^ {(m - 1)} \big) (h _ {1} + h - h _ {1} h) \quad \text { and }
$$

(ii) proportion of packets lost when consuming content from the external link, $( 1 \mathrm { ~ - ~ } q R / n ) ^ { ( m - 1 ) } ( h _ { 1 } \mathrm { ~ + ~ }$ $h _ { z } - h _ { 1 } h _ { z } )$

$$
\begin{array}{l} W _ {1} ^ {\text { Packet   Loss }} (q _ {1} \mid q, \ldots , q) \\ = \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 1)} (h _ {1} + h _ {z} - h _ {1} h _ {z}) \\ \quad + \bigg (1 - \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 1)} \bigg) (h _ {1} + h - h _ {1} h). \end{array}
$$

<sup>Proposition</sup> <sup>2.</sup> In a P2P community with m homogeneous participants,

(a) a symmetric sharing equilibrium $( q _ { i } = q ^ { * } , \forall i = 1$ $\cdots , m )$ occurs when

$$
) D e l a y: \frac {1}{(\mu - P _ {m} H _ {0} f)} <   \frac {1}{(\mu_ {z} - m P _ {m} H _ {0} f)};
$$

$$
\text {(ii)} J i t t e r: \frac {1}{\mu (\mu - P _ {m} H _ {0} f) ^ {2}} <   \frac {1}{\mu_ {z} (\mu_ {z} - m P _ {m} H _ {0} f) ^ {2}};
$$

4iii5 Packet Loss: $\frac { h _ { 1 } ^ { 2 } } { 1 - h _ { 1 } } \Big | _ { q  0 } < \frac { h _ { z } ^ { 2 } } { 1 - h _ { z } } \Big | _ { q  0 } .$

Otherwise, $q _ { i } = 0 , \forall i = 1 , 2 , \ldots , m .$

(b) When sharing occurs, the level of sharing $q ^ { * }$ is given by the solution of the mth degree equation:

(i) Delay:

$$
\begin{array}{c} \left(\frac {\partial \delta_ {1}}{\partial q _ {1}} + \left(1 - \left(1 - \frac {q R}{n}\right) ^ {(m - 1)}\right) \frac {\partial \delta}{\partial q _ {1}} \right. \\ \left. + \left(1 - \frac {q R}{n}\right) ^ {(m - 1)} \frac {\partial \delta_ {z}}{\partial q _ {1}}\right) = 0. \end{array}\tag{ii}
$$

$$
\begin{array}{c} J i t t e r: \left(\frac {\partial \zeta_ {1}}{\partial q _ {1}} + \left(1 - \left(1 - \frac {q R}{n}\right) ^ {2 (m - 1)}\right) \frac {\partial \zeta}{\partial q _ {1}} \right. \\ \left. + \left(1 - \frac {q R}{n}\right) ^ {2 (m - 1)} \frac {\partial \zeta_ {z}}{\partial q _ {1}}\right) = 0. \end{array}
$$

$$
\begin{array}{l} \text {(iii) Packet Loss:} \left(1 - \frac {q R}{n}\right) ^ {(m - 1)} \bigg (\frac {\partial h _ {1}}{\partial q _ {1}} (1 - h _ {z}) \\ \qquad \qquad \qquad + \frac {\partial h _ {z}}{\partial q _ {1}} (1 - h _ {1}) \bigg) \\ \qquad + (m - 1) \bigg (1 - \bigg (1 - \frac {q R}{n} \bigg) ^ {(m - 1)} \bigg) \\ \qquad \cdot \left(\frac {\partial h _ {1}}{\partial q _ {1}} (1 - h) + \frac {\partial h}{\partial q _ {1}} (1 - h _ {1})\right) = 0. \end{array}
$$

<sup>Proof.</sup> Refer to the appendix.

Proposition 2 identifies conditions under which various sharing equilibria will exist for m homogeneous participants. The conditions in Proposition $2 ( \mathsf { a } )$ have a nice interpretation. The left side of the inequalities represents the congestion (delay, jitter, or packet loss) on the internal link at nonsharing $( q = 0 )$ , whereas the right side represents the congestion (delay, jitter, or packet loss) on the common external link at $q = 0$ Therefore, this condition implies that there is an incentive to share only if the congestion on the internal link is less than that in the external link. Note that because the objective function is convex, we can characterize a unique symmetric equilibrium. However, there may be asymmetric equilibria that we have not characterized.

In contrast to Proposition 1, where we found that nonsharing is the only equilibrium in the absence of a common congested resource, Proposition 2 asserts that sharing can be a natural outcome for nonaltruistic, congestion-minimizing participants who are faced with a common congestible external resource. Therefore, the presence of an external link, the congestion on which is a function of the sharing of the participants, is necessary to induce sharing in a P2P community (in the absence of external factors). In this case, in addition to the internal positive effect of sharing, a participant enjoys an additional external positive effect from sharing, i.e., a reduction in the congestion on the external link. Also, unlike the internal positive effect, the external positive effect is not contingent on the sharing decision of other participants. Thus, the presence of the common congested resource can eliminate the prisoner’s dilemma because it increases a participant’s payoff from sharing (external and internal positive effect of sharing).

<sup>Corollary</sup> <sup>1.</sup> A system of m homogeneous participants with a congestible external link in a nonsharing equilibrium moves to a sharing equilibrium as the number of participants increases.

<sup>Proof.</sup> Refer to the appendix.

The intuition here is that in a nonsharing P2P community the external link capacity is seen as abundant. However, as the number of participants increases, and they continue not to share, the traffic on the external link, increases. Eventually, the use of the congested link will become high enough for the participants to feel the effects of the congestion. At this point, the participants have an incentive to share and reduce the congestion on the external link to reduce their overall expected delay, jitter, or packet loss.

## 3.3. Understanding the Internal Positive Effect of Sharing

As outlined in Proposition 1, the internal positive effect alone can never induce sharing. However, an important question to ask is the following: When sharing does occur, how do the internal resources influence the level of sharing? To answer this question, we consider a situation where the internal positive effect is ignored, but the external positive effect is perceptible. Suppose that all the participants in the P2P network are naïve, a term we use to convey the fact that every participant thinks that although their link is congestible, the links of all other participants are not. In other words, a naïve participant expects to suffer a constant delay, which is independent of his/her sharing decision, when receiving content from another participant. In contrast, we use the term informed to describe participants who are aware of congestion in the internal links of all participants, including their own. Our analysis of a naïve peering community leads to the following result.

<sup>Proposition</sup> <sup>3.</sup> In a community of homogeneous naïve participants, the symmetric sharing equilibrium level is always lower than that for a community of informed participants.

<sup>Proof.</sup> Refer to the appendix.

In Proposition 3, we find that the absence of the internal positive effect has the impact of reducing the symmetric sharing level chosen by the participants. Thus, we conclude that although the perception of internal congestion is not sufficient by itself to induce sharing (as shown in Proposition 1), this effect does impact the sharing level chosen by a sharing community. The intuition is that the internal links of participants may also be viewed as a common congested resource. Reducing the congestion on this shared internal resource is an additional incentive to share, and in the absence of this incentive, naïve participants choose a lower sharing level than informed participants.

## 4. Numerical Simulations

As seen in Proposition 2, for all three congestion measures, the equilibrium sharing level for the m-homogeneous participant model is the solution to an mth order equation. Given this solution form, deriving a closed-form expression for the decision variable is difficult. We therefore conduct numerical experiments to depict the effect of model parameters on the equilibrium sharing level and to derive additional insights.

To capture the typical situation where a participant’s cache is much smaller than the number of items the participant may be interested in, we chose a cache size (R) of 10 while the total number of items of interest (n) was set to 100,000. The number of participants (m) was set to 10,000 to represent the reasonably large peering communities that exist. Finally, the units for link traffic and capacities in the model are derived from the product of access rate (items requested per sec) and the item size in bytes. We used an access rate of $H _ { 0 } = 1$ request/sec, which generates a traffic of 40 packets per second $( f = 4 0 )$ . Assuming a packet size of approximately 50 bits, the external and internal link capacities ( and ) were set to 160 Kpps (or 8 Mbps) and 300 Kpps (or 15 Mbps), respectively, i.e., the external link capacity is much higher. The mean exponential delay tolerance for a packet (1/5 beyond which the packet is assumed to be lost is assumed to be 1 microsec. Below we present various results from the numerical experiments.

## 4.1. Impact of Internal Link Capacity

Figure 2 illustrates the impact of the internal link capacity (). First, we see that the sharing level in equilibrium increases with internal link capacity for all the three congestion measures, namely, delay, jitter, and packet loss (Figure 2(a)). The intuition is that increasing internal link capacity reduces internal link congestion, thus reducing the negative effect or the “cost” of sharing. This increases the incentive for participants to share. The reduction in the external link congestion is also interesting—as participants share more, they are able to reduce the congestion on the external link. Figure 2(b) demonstrates the external positive effect of sharing. This reduction in external link congestion occurs because the probability of satisfying a participant’s request from within the P2P community increases with the internal link capacity (Figure 2(c)). Also, the total congestion experienced by a participant (in terms of delay, jitter, or packet

## Figure 2 Impact of Internal Link Capacity

(a) Impact of internal link capacity on sharing level  
![](/api/attachments/8E84VMS2/fulltext/images/1bfc708c5a777326ee1b208cc34acbc353d9bc9585966008a2abb4db93955e26.jpg)

(b) Impact of internal link capacity on external link delay, jitter, and packet loss  
![](/api/attachments/8E84VMS2/fulltext/images/4de058d6532c53d7ce3a58b5868bf0fe566a13a4c86857d5e363c30c8e06781b.jpg)

(c) Impact of internal link capacity on probability of satisfying a request within the P2P community  
![](/api/attachments/8E84VMS2/fulltext/images/ae1beaa58082b19acd41375509223955400cbb28f25a0d7887094a9a976816d2.jpg)

(d) Impact of internal link capacity on total expected delay, jitter, and packet loss  
![](/api/attachments/8E84VMS2/fulltext/images/e7979c931874700c855d6685250c9975e43949ba591824572ee61f46029057d7.jpg)

(e) Impact of internal link capacity on internal link delay, jitter, and packet loss  
![](/api/attachments/8E84VMS2/fulltext/images/2668c9898ec2cf2b8a1e9d42559b3e6523562d1105fd504a00d8936ea3ae700d.jpg)

loss) decreases as the internal link capacity increases (Figure 2(d)). Interestingly, the total congestion tends to stabilize as the internal link capacity is increased beyond a point. The intuition here is that the increase in sharing level is prompted by the participant’s need to lower congestion on the external link. However, the use of the external link decreases as sharing levels increase because more requests are satisfied internally.

As a result, there are decreasing returns from sharing. Note that despite increased sharing it is possible for the internal link delay to decrease (Figure 2(e)). This can be seen as the manifestation of the internal positive effect—increased sharing relieves congestion on the neighboring peer’s internal link, which is beneficial when using that peer’s link for satisfying a request. In addition, the higher internal link capacity allows the peer to better handle the increased traffic from sharing.

## 4.2. Impact of External Link Capacity

The impact of external link capacity is illustrated in Figure 3. Figure 3(a) shows that increasing the external link capacity decreases the sharing level. The intuition is that as the external link capacity increases, the congestion on the external link decreases. This reduces the external positive effect from sharing, and thus participants have a lower incentive to share. One way to interpret this result is that as the external link capacity increases, we move towards a truly abundant external resource, and as outlined in Propositions 1 and 2, it is the presence of the common congested resource that induces sharing. In its absence, participants have less incentive to share and, consequently, the sharing levels decrease. In Figure 3(b) we see that external link delays decrease as the external link capacity increases, even though the equilibrium sharing levels decrease. The intuition is that participants reduce sharing level such that the increase in the external link capacity can overcome the additional traffic and still reduce external link delay.

## 4.3. Impact of Number of Participants

Figure 4 demonstrates the impact of the number of participants in the P2P community. As illustrated in Figure 4(a), as the number of participants in the network increases, the sharing level increases. The intuition behind this result is closely related to our finding that a common congested resource is needed to induce participants to share. As the number of participants in the community increases, the common resource gets more congested. In response, the participants share more to alleviate the congestion on the external link, but the sharing levels tend to stabilize as the number of participants is increased beyond a point. The intuition here is that the increase in sharing level is prompted by the goal to lower congestion on the external link. However, the use of the external link decreases as sharing levels increase because more requests are satisfied internally (Figure 4(b)). As a result, there are decreasing returns from sharing.

The expected congestion (delay, jitter, or packet loss) of a participant is plotted in Figure 4(c) for various sizes of the P2P community. As the size of the community increases, with no change in the capacity of the external link, the congestion experienced by the participant increases even though the participants share more. The intuition here is that the participants share only to the extent that they relieve the congestion on the external link without overburdening their internal links. More interestingly, we find that the increase in the congestion experienced by the participants increases less than linearly with the size of the P2P community (although the increase in the sharing levels is concave). This suggests that the P2P community scales well. This effect arises from the fact that the probability of satisfying a request from within the community increases as the size of the community increases. Thus, the increased congestion on the external link is offset by the higher likelihood that the participant will not have to use the external link. Another observation is that increasing the number of participants can cause a nonsharing community to start sharing (Figure 4(a)). However, as the number of participants continues to increase, so does expected congestion. This suggests that, eventually, for a high

Figure 3 Impact of External Link Capacity  
![](/api/attachments/8E84VMS2/fulltext/images/f61396949b81c55cfdb7d5672f6c0775328e11506c9b1391cd2d5d7fe152f1b9.jpg)

(b) Impact of external link capacity on external link  
![](/api/attachments/8E84VMS2/fulltext/images/4ea585a89f81c25afe8a1c57bb33aad2a33a071b401d60b73f6df942c9d82d2d.jpg)

## Figure 4 Impact of Number of Participants

(a) Impact of number of participants on sharing level  
![](/api/attachments/8E84VMS2/fulltext/images/11903662e4e0597b36973e1b6e2a8c47f072caea3007a45d7e5336b3561db0c7.jpg)

(b) Impact of number of participants on probability of satisfying a request within the P2P community  
![](/api/attachments/8E84VMS2/fulltext/images/64e4dcb4e9b4d6b01378c2ef83453853b7fcb88684a4db684bfe5caa0c1f43c5.jpg)

(c) Impact of number of participants on total expected delay, jitter, and packet loss  
![](/api/attachments/8E84VMS2/fulltext/images/f4180c91bca1e5adf84f1a483f5ada75579cddfa9e05b10e5e7c57a5671c595f.jpg)

![](/api/attachments/8E84VMS2/fulltext/images/fc024053afb90eb8accfd00ead00fd244caa53a71545130797183d0a487bab62.jpg)

enough value of the number of participants, the network will be severely underprovided and the congestion will be too high for the P2P community to exist.

Figure 5 Minimum Number of Participants to Induce Sharing  
Figure 6 Impact of the Internal Positive Effect  
![](/api/attachments/8E84VMS2/fulltext/images/eaa6424c75e4600b3195fba1c9af0e3851930cd7b32ce4c81e122e53a174cafc.jpg)

The above analysis suggest that for given internal and external link capacities there exists a critical value m, below which no sharing takes place. The intuition is that below m, the external link traffic is sufficiently low so that the external resource seems truly abundant, and therefore the participants have no incentive to share. On the other hand, there exists another critical value of the number of participants, m° , beyond which nonsharing is again the equilibrium solution. This represents a region in which the size of the P2P community is simply too large, and a small increase in the sharing level (above zero) leads to a relatively large increase in internal delay without an offsetting decrease in external delay. Consequently, in this region (m > m5 ° the participants simply choose not to share.

In Figure 5 we illustrate the impact of increasing the external link capacity on m. We demonstrate that increasing the external link capacity has the impact of increasing the minimum number of participants needed in the P2P community to induce sharing. This is because increasing the external link capacity reduces congestion and thus reduces the external positive effect of sharing. Thus, a participant’s incentive to share is reduced because it would take a greater number of participants to cause sufficient congestion in the common external resource.

## 4.4. Impact of Internal Positive Effect

Figure 6 demonstrates the impact of the internal positive effect. As outlined in Proposition 3, we identified the optimal sharing level for a community of naïve participants: those who do not perceive the internal links of other participants as congestible resources. We contrast this with the equilibrium sharing level chosen by a community of informed participants who are aware that their sharing decision affects the internal link delays of the other participants. In Figure $^ { 6 , }$ we plot the difference between the sharing levels chosen by informed and naïve participants. We find that the sharing level chosen is always lower when the internal link congestion is ignored. As the internal link capacity increases, both naïve and informed participants increase their sharing levels. However, informed participants who understand the importance of the internal positive effect increase their sharing levels at a faster rate relative to the naive participants.

At a conceptual level, Figure 6 shows that the internal link of a peer and the external link are both common resources from the perspective of a user in the P2P community. While congestion in the external link is a precondition for sharing, congestion in the internal link is neither necessary nor sufficient for sharing. The role played by the internal link is to increase the level of sharing when sharing occurs.

A common theme that emerges from Figures 1 through 6 is that the equilibrium level of sharing is the lowest when jitter is used as the congestion metric, i.e., jitter suffers most from the tragedy of the commons. This issue is considered again in §5.3, where we discuss the socially optimal level of sharing for each of the congestion metrics studied here. There, we will observe that jitter is also the congestion metric with the smallest level of sharing relative to the social optimum.

## 4.5. Impact of Different Interest Groups

To examine the effects of different interests in a P2P community, we divide the community into two groups with different, but overlapping, interests. We consider two groups in the community: Each group is homogeneous with respect to the content they consume. There are k 4≤m5 participants in group 1, and the remaining 4m − k5 participants are in group 2. Furthermore, we denote $\hat { \boldsymbol { \beta } } \ ( \leq 1 \hat { ) }$ to be a measure of the

Figure 7 Impact of Different Interest Groups 4m = 505

(a) Impact of different interest groups on sharing level when minimizing delay

![](/api/attachments/8E84VMS2/fulltext/images/2528195232f903bea91621315503bef8af5f5e5cb8ee24dad0c9aea928211294.jpg)

(b) Impact of different interest groups on sharing level when minimizing jitter  
![](/api/attachments/8E84VMS2/fulltext/images/4eec9e682ce90347d84d1e409b0bd7c93c1ad356d2a505b9e10d45e50985d114.jpg)

(c) Impact of different interest groups on sharing leve when minimizing packet loss  
![](/api/attachments/8E84VMS2/fulltext/images/804bb8ff018b5f4f95ce7706d2fc92157cf44d7afec0b5b2b6f85f349c7197ff.jpg)

degree of commonality between the interests of the two groups. The probability of finding a requested item from a peer i in the same group is $q _ { i } \times ( R / n )$ . In contrast, the probability of finding a requested item in the other group is lower, given by $\beta \times q _ { i } \times ( R / n )$ . We invoke symmetry for sharing levels within a group, and consider $q _ { g } ^ { 1 ^ { * } }$ and $q _ { g } ^ { 2 ^ { * } }$ to be the equilibrium sharing levels for all peers within groups 1 and 2, respectively (refer to the appendix for details of the model setup).

In Figure 7, we illustrate how the sharing levels of the two groups vary with the relative size of the two groups (for $\bar { \beta } = 0 . \dot { 2 } 5 )$ . Note that both groups experience the same external link congestion when the request is not satisfied within the P2P community. Therefore, the external positive effect of sharing is identical, irrespective of the group to which the participant belongs. In contrast, the cost of sharing is quite sensitive to the size of the group to which the participants belongs. This is because the number of requests served by a sharing participant increases with the group size. As a result, we find that participants in the smaller group (Group 1 in Figure 7) share more than those in the larger group (Group 2 in Figure 7). This also explains why peers in Group 1(2) decrease (increase) their sharing levels as the size of Group 1 increases. Eventually, when the groups are of equal size, the sharing levels converge to the same value.

## 5. Model Extensions

In this section, we revisit our analysis under some extended situations: free-riding, interference of uploading on download performance, and socially optimal sharing levels induced by a central planner. First, we consider free-riding. The analysis here is different because we consider a free-rider as one who, by type, does not share. Under interference, we examine sharing decisions when the upload and download traffic have different effects on the congestion measure of interest. Finally, we make some observations concerning the optimal level of sharing from the perspective of a central planner and an incentive scheme that induces the community to operate at the socially optimum level.

## 5.1. Free Riding

Free-riding is a common phenomenon observed in P2P networks. Free-riders are participants who use the system resources without contributing to the system. Empirical studies have shown free-riding to be prevalent in traditional P2P file-sharing networks (Adar and Huberman 2000, Saroiu et al. 2003). In these file-sharing networks, the free-riding phenomenon has been likened to the tragedy of the commons—as users do not benefit from serving files to others, many users decline to perform this altruistic act (Ramaswamy and Liu 2003). In fact, many believe free–riding to be a major challenge that threatens the existence and usefulness of P2P networks (Habib and Chuang 2004). In this section, we analyze free-riding in the context of congestion-sensitive participants in a P2P network. In our context, a free-rider is a participant who by type chooses not to share. For example, a peer may choose not to share (but consume content from others) if the peer believes that the external link has ample capacity. Clearly, such a peer would perceive no benefit from sharing. We study the optimal (symmetric) sharing of the other congestion-minimizing participants in the network in the presence of such free-riders. Based on numerical experiments, we show that the sharing participants find it optimal to continue sharing, even in the presence of free-riders. In fact, they try to compensate for the presence of free-riders by increasing their optimal sharing level. This suggests that the congestionminimizing peering community is scalable and to an extent resilient to the effects of free-riding. Interestingly, we also observe that the entry of a free-rider into a P2P network in nonsharing equilibrium could induce sharing, even though the free-rider does not share. Next, we present the details of our analysis.

We consider a system of m homogeneous (in their internal link bandwidths) participants. Within such a network, we allow g (≤m5 free-riders, and the remaining $( m - g )$ participants are rational and congestionminimizing. In this setup, we vary the proportion of free-riders in the community $( g \dot { / } m )$ and evaluate the optimal symmetric sharing level for the remaining participants. As before, we consider three metrics for congestion: delay, jitter, and packet loss. Because free-riders are participants who exploit the system resources (internal links of the sharing participants and the external link) without contributing, an increase in the number of free-riders increases the system congestion. In addition, increasing the proportion of free-riders increases the likelihood of using the external link to satisfy a request, further increasing the congestion on the external link. To compensate for this increase in congestion, the sharing participants actually increase their optimal sharing level as the proportion of free-riders in the system increases (refer to Figure 8). This illustrates that in the presence of free-riders, peers who are willing to share not only continue to share but also, in fact, increase their sharing levels. In Figure 9, we plot the extent of congestion (delay, jitter, and packet loss respectively) experienced by sharing peers as the proportion of free-riders in the system is increased. Interestingly, we find that the congestion experienced by the sharing peers does not change much with an increase in the proportion of free-riders, implying that the peering community can tolerate fairly high levels of freeriding within the community. However, there seems to be a knee in the curve beyond which the congestion experienced by the peers increases sharply with the proportion of free-riders (>50% in this setup).

Figure 8 Free-Rider Impact on Sharing  
![](/api/attachments/8E84VMS2/fulltext/images/ad66340d00d412117f54d229b158965bf8c7f9d7074d392dec6a404f14e88796.jpg)

Thus, we would expect that for networks with a large proportion of free-riders, the community will eventually break down with a nonsharing outcome.

Next, we investigate whether the introduction of a free-rider can induce sharing in a previously nonsharing community. For this experiment, we begin with a homogeneous community that is in a nonsharing equilibrium. In this community we introduce additional peers who are all free-riders by type. In Figure 10, we plot the optimal symmetric sharing level chosen by the other peers in the network as the number of free-riders introduced in the network is increased. The introduction of free-riders in the system causes previously nonsharing participants to begin sharing and to further increase their sharing levels as the number of free-riders increases. Intuitively, as the number of free riders increases, so does the congestion on the external link (simply because more members in the community are using

Figure 9 Free-Rider Impact on Congestion  
![](/api/attachments/8E84VMS2/fulltext/images/ebf472261b8f87525e3beb8d22151191e32b5f664e93d94e39cc9979c1b9f2ba.jpg)

Figure 10 Free-Riders Induce Sharing in a Previously Nonsharing Community  
![](/api/attachments/8E84VMS2/fulltext/images/cbbd4381e933d9d8626cf93c20ac85206a8fc10c793bbbfc43ab40ec9442aa67.jpg)  
the external link). Eventually, the rational congestionminimizing peers find it optimal to compensate for this by sharing their resources.

## 5.2. Interference of Uploading on Download Performance

As outlined in §2, although traditional TCP/IP networks are designed to have separate upload and download capacities, there is ample evidence that upload traffic and download delays are not independent of each other. For the mathematical analysis in this paper, we have assumed that upload and download traffic affect congestion in the same manner. In this section, we allow the impact of upload traffic on download congestion to be nonuniform, and numerically we study the sensitivity of our results to this assumption. For this experiment we define an interference parameter  $( 0 < \alpha < 1 )$ , such that $\alpha = 1$ represents the case when the upload and download traffic affect congestion in the same manner. On the other hand, $\alpha = 0$ represents the scenario where the upload traffic has no effect on download congestion. Here we wanted to ask the following questions: (a) What is the minimum value of the interference parameter beyond which the nonsharing result in Proposition 1 holds? (b) What is the impact of the interference parameter  on the level of sharing chosen by participants in the presence of a congestible external link (see Proposition 2)?

Recall (from Proposition 1) that under the symmetric assumption $( \alpha = 1 )$ , we show that nonsharing is the only equilibrium in the absence of a congestible external link. We numerically revisit this result for different values of  in a system of heterogeneous (in internal link bandwidth) congestion-minimizing participants. The minimum level of the interference parameter (5, beyond which the nonsharing holds is defined as alpha critical, $\alpha _ { c } .$ That is, for $\alpha \geq \alpha _ { c }$ only a nonsharing equilibrium exists. The results from this analysis are illustrated in Figure 11. We find that our nonsharing result holds for most of the feasible range of interference parameter  (because $\alpha _ { c }$ was typically < 0014). Moreover, the value of $\alpha _ { c }$ is decreasing in the number of participants. The intuition is that as the number of participants increases the likelihood of a request being satisfied by an internal link increases, and so does the upload traffic on the internal links of the sharing participants. This implies that for relatively small values of alpha, the negative effect of sharing is significant, and this increases a participant’s resistance to share (reflected in lower values of $\alpha _ { c }$ as m increases). This trend suggests that for medium-to-large peering communities our results (for $\alpha = 1 )$ should hold for a wide range of the interference parameter (). Also, as illustrated in Figure 11, $\alpha _ { c }$ decreases as the conditional probability that a peer satisfies a request $( R / n )$ decreases. This result is a direct consequence of the reduction in the internal positive effect of sharing as the probability that a sharing participant can satisfy a request $( R / n )$ reduces. Thus, peers are willing to share only if upload traffic has negligible impact on the download congestion $( \alpha _ { c }$ decreases).

Recall that in Proposition 2 we derive the symmetric sharing level chosen by participants in the presence of a congestible external link under the assumption that $\alpha = 1$ . When  is less than 1, the negative impact of upload traffic on download congestion reduces. In other words, the cost of sharing reduces as  decreases, with no impact on the benefit of sharing. Hence, participants share more. In Figure 12, we study how sharing levels change for different values of the interference parameter (5. As expected, we find that the participants share more as the interference between upload and download traffic reduces. Interestingly, in Figure 12 we find that beyond a point, the increase in the sharing is not very sensitive to the interference parameter. This is because for a reasonably large P2P community a small increase in the sharing level leads to a considerable increase in upload traffic, thus compensating for the reduction in the cost of sharing (arising from a lower value of $\alpha )$ . Of course, when upload traffic has no impact on download congestion $( \alpha = 0 )$ the participants move to full sharing $( q ^ { * } = 1 )$

Figure 11 Impact of Number of Participants on Alpha Critical 4<sub>c</sub> 5 in the Presence of a Noncongestible External Link  
![](/api/attachments/8E84VMS2/fulltext/images/c367423b6891fe827e6fd18084ceaeb84fcd8745a6638bcefcfe01a8ae6d6b08.jpg)

## 5.3. A Social Perspective

So far in this paper, we have focused on each participant making self-interested, independent sharing decisions. These decisions, although optimal from an equilibrium perspective, need not be optimal from the standpoint of the community as a whole. From a social perspective, one can imagine a different version of the problem where a central planner chooses the sharing levels of the participants with the objective of minimizing total network congestion. It is plausible for the planner to implement an incentive scheme that induces participants to move from the equilibrium sharing level to the socially optimal one.

From a social perspective, it is possible for sharing to be optimal even in the absence of congestion in the external link. This is because the socially optimal sharing levels should result in a more balanced trade-off between the delays on the internal and external links. Although individual congestion-minimizing participants have no incentive to share in the absence of a congestible external link, a central planner might induce sharing in this situation by exploiting the internal positive effect of sharing. Clearly, therefore, in the presence of a congestible external link, we would expect the socially optimal sharing levels to be consistently higher than the equilibrium sharing levels. It is also clear that the total network congestion will always be lower (never higher) at the socially optimal level of sharing.

Figure 12 Impact of Interference Parameter 45 on Sharing Level in the Presence of a Congestible External Link  
![](/api/attachments/8E84VMS2/fulltext/images/6d36b2957ab0df7c2a2b7ee93ecc4268a26a915404905acc11546e462d7a7f7d.jpg)

A social planner can view the decision to be made from two perspectives: one where the sharing level is imposed on the participants and another where the sharing level is induced via incentives. The former, when applicable, essentially requires the identification of the socially optimal sharing levels, and would correspond to an engineering solution to the sharing problem, implemented directly in the way the P2P application works. To find the optimal sharing level, one would need to minimize the appropriate measure of interest (total network delay, total network jitter, or total network packet loss) with respect to the sharing level. For example, the total network delay can be written as $\begin{array} { r } { W _ { \mathrm { T O T } } ^ { \mathrm { D e l a y } } = \sum _ { i = 1 } ^ { m } W _ { i } ^ { \mathrm { D e l a y } } ( q , q , \dots , q ) \stackrel { \_ } { = } } \end{array}$ $m W _ { 1 } ^ { \mathrm { D e l a y } } ( q , q , \dots , q )$ in the symmetric case. The socially optimal sharing level $q _ { \mathrm { C P ( D e l a y ) } } ^ { * }$ is obtained by minimizing total network delay, i.e., $q _ { \mathrm { C P ( D e l a y ) } } ^ { * }$ is such that $( \partial W _ { \mathrm { T O T } } ^ { \mathrm { D e l a y } } ( q , q \dots q ) ) / ( \partial q ) | _ { q = q _ { \mathrm { C P ( D e l a v ) } } ^ { * } } = 0 .$ . The socially optimal sharing level for the other congestion measures can be identified in a similar fashion.

When individual users make sharing decisions, the social planner would attempt to guide the participants to the socially optimal levels by implementing appropriately designed incentive schemes. The challenge here is to develop incentives that can be implemented even when the sharing actions of the participants are difficult to observe. Simpler schemes are preferable in general, and it would be beneficial to have a scheme where the social planner can charge the participants based on easily observable network parameters. In the rest of this section, we show how a social planner can impact the sharing levels using such an incentive scheme. The proposed incentive scheme places a participation fee of $\beta _ { 1 }$ per unit of traffic on the external link. This scheme is simple to implement because total traffic on the external link is much easier to observe than actual sharing levels.

We illustrate the idea using delay; the analysis is similar for each of the other congestion measures (interested readers are referred to the Online Supplement<sup>2</sup> for details). Given the proposed participation fees, the objective for participant 1 is to select a sharing level that minimizes her cost. That is, participant 1 will need to solve

$$
\begin{array}{c} \operatorname{Min} _ {q _ {1}} C _ {1} ^ {\text {Delay}} (q _ {1} \mid q, \ldots q) = \beta_ {1} \lambda_ {z} (q _ {1} \mid q, \ldots q) \\ + \beta_ {2} W _ {1} ^ {\text {Delay}} (q _ {1} \mid q, \ldots q), \end{array}
$$

where $\beta _ { 1 }$ is the fee per unit of external link traffic. The constant $\beta _ { 2 }$ is the cost per unit of the relevant congestion measure (delay, jitter, packet loss) incurred by participants. The value of $\beta _ { 2 }$ can be normalized to 1 without loss of generality, because it only has a scaling effect on the participation fee $\beta _ { 1 } .$

The first component of the above objective function is the participation fee, whereas the second is the total cost associated with delay. It is straightforward to show that this cost function is convex in $q _ { 1 } .$ . The social planner can induce the socially optimal sharing level $q _ { \mathrm { C P ( D e l a y ) } } ^ { * }$ by identifying the value of $\beta _ { 1 }$ that solves

$$
\begin{array}{c} \frac {\partial C _ {1} ^ {\text {Delay}}}{\partial q _ {1}} \Big | _ {q _ {1} = q = q _ {\text {CP(Delay)}} ^ {*}} = \beta_ {1} \frac {\partial \lambda_ {z}}{\partial q _ {1}} \Big | _ {q _ {1} = q = q _ {\text {CP(Delay)}} ^ {*}} \\ + \beta_ {2} \frac {\partial W _ {1} ^ {\text {Delay}}}{\partial q _ {1}} \Big | _ {q _ {1} = q = q _ {\text {CP(Delay)}} ^ {*}} = 0 \end{array}
$$

for any given value of $\beta _ { 2 } .$ .

Next, we analyze the impact of the key problem parameters on the levels of sharing and the participation fees needed to induce socially optimal sharing levels. Figure 13 shows that the sharing levels without a social planner tend to be a very small fraction of the socially optimal levels. This effect is most pronounced for jitter, suggesting that online streaming situations are the ones most likely to require intervention, rather than situations that involving simple downloading of files (i.e., delay-driven situations). However, it can be observed from Figure 13 that even for the other measures, sharing levels are far below what is socially optimal. As the internal link capacity increases, the ratio of the equilibrium sharing level to the socially optimal one increases; this can be attributed to the fact that the participants are less affected by internal congestion and are willing to share more.

Figure 14 corroborates the finding in Figure 13; the participation fees needed to induce socially optimal levels of sharing drop off significantly as the internal link capacity increases. Note that the values of the fee are scaled for convenient depiction in the same figure. Interestingly, the participation fee needed to induce socially optimal sharing levels is much lower in the case of jitter than in the other two measures. Thus, although jitter is the measure that benefits most from intervention, it is also the measure that responds the quickest to incentives.

Figure 13 Impact of Internal Link Capacity on Game Sharing Level Relative to the Social Planner’s Sharing Level  
![](/api/attachments/8E84VMS2/fulltext/images/0a175d48c84b170b59a21a6e08e19b5c3772837d924a775d5ba4f33c9a3713d2.jpg)

Figure 14 Impact of Internal Link Capacity on the Participation Fee  
![](/api/attachments/8E84VMS2/fulltext/images/181ea01ebbcc4bfe1ff1f0e501add2e74ecebfac7f1af0448b8da38745e06f12.jpg)

Figures 15 and 16 present the impact of external link capacity. As would be expected, the ratio of the equilibrium sharing levels to the socially optimal levels drops off as the external link capacity increases. When this happens, the participants start to perceive it as an increasingly abundant resource and move closer to the “tragedy of the commons” outcome. Consequently, the participation fees are observed to increase with external link capacity. This increase however, is not substantial, implying that the participants move to the socially optimal levels with only a small nudge.

Figure 15 Impact of External Link Capacity on Relative Sharing Levels  
![](/api/attachments/8E84VMS2/fulltext/images/3b14425694bf86b6bc1c8f5e9859a5338cc632e6334d3735942df94990a7eefb.jpg)

Figure 16 Impact of External Link Capacity on the Participation Fee  
![](/api/attachments/8E84VMS2/fulltext/images/a959826c5edbc6f2f9886f3d2b09f494624ce927dc796719a59c4f26b0306b29.jpg)

Figures 17 and 18 depict the impact of the size of the P2P community on sharing levels and the participation fee. Increasing the number of participants increases congestion in the network and causes the participants to naturally move closer to optimal sharing levels. With more participants, the overall traffic in the network increases. Thus, the participation fee that needs to be charged does not need to increase much, because the increased congestion naturally makes the community share more.

The general observation from the incentive-related experiments is that the level of intervention needed decreases as more resource constraints are imposed on the participants. As the participants feel the effect of these constraints, they naturally move closer to the socially optimal sharing levels (and away from the “tragedy of the commons” scenario). Conversely, our results show that if the network is running over capacity, it is more important to consider incentives that induce the participants to share.

Figure 17 Game vs. Social Planner Sharing  
![](/api/attachments/8E84VMS2/fulltext/images/ef8201b23d3287747affa17799a7051de534023cfde238c910de8382eb38f0da.jpg)

Figure 18 Participation Fee vs. Size  
![](/api/attachments/8E84VMS2/fulltext/images/92c6724f7cf983b868e1d296811b77d5de3b4f66f691a080c91a0cb4308ab2ae.jpg)

## 6. Summary and Conclusions

In this paper, we analyzed the sharing of participants in a P2P network used for delivering congestion-sensitive content. We considered rational, nonaltruistic, congestion-minimizing participants. We considered three commonly used metrics for congestion, namely, delay, jitter, and packet loss. We studied the situation where the participants of the P2P network share a common resource, such as an external network link that members need to use when it is not possible to obtain a requested item from within the community (either because of lack of availability or because participants with the content refuse to share).

First, we considered the case where the common resource (the external link) shared by the participants is insensitive to their sharing decision. This could happen if the common resource is abundant or if the participants are oblivious to the fact that their sharing level impacts the availability of the common resource. Next, we consider the case where the external link is congestible and the participants are aware that they can relieve the congestion on the external link by sharing.

Through sharing, the participants relieve congestion on the common external link (external positive effect) and the internal links of other participants in the network (internal positive effect). This provides benefits of lower congestion when the external link or the internal links of one of the other sharing participants is used to satisfy a participant’s request. However, this benefit of sharing comes at the cost of increased internal link congestion because sharing increases the traffic on the internal link.

Our first key finding is that nonsharing is the only equilibrium possible when the external link delay is insensitive to the sharing decision of the participants. This is in line with the tragedy of commons (Hardin 1968), where the nonsharing result occurs because a common resource (the external link in our case) is assumed to be plentiful or abundant. The second key result from our analysis is that when the participants are all affected by the performance of a common resource (a congestible external link), sharing can indeed be an outcome of rational, self-interested participants. We show that the internal positive effect of sharing, which is contingent on the sharing decision of the other participants, cannot, by itself, induce sharing. However, we find that the realization of the internal positive effect influences the level of sharing chosen by participants. In fact, the levels of sharing chosen by a community of naïve participants who do not perceive that the internal positive effect is always lower than those chosen by informed participants who are aware of the internal positive effect.

We find that a P2P network initially in a nonsharing equilibrium moves towards a sharing equilibrium as the number of participants in the network increases. This result is a direct outcome of the increased congestion on the external link as the size of the community increases. If the common resource is abundant and no cost is imposed to use it, the participants do not share. However, as the congestion on the external link increases or the participants are charged a fee to use it, participants begin to share to reduce the congestion on the external link. This finding has policy implications: Incentives to share are needed in precisely those situations in which there appear to be no obvious congestion problems facing the P2P community.

Most of the mathematical analysis in the paper assumes that the upload and the download traffic affect congestion in the same manner. However, numerical experiments indicate that our results are quite robust to allowing the impacts of upload traffic and download traffic to be different. For mediumto-large peering communities, only a modest impact of the upload traffic (a small value of c) is needed to maintain the nonsharing equilibrium result in Proposition 1.

Our numerical experiments suggest that a congestion-minimizing P2P community can, to an extent, withstand the effects of free-riding. In fact, rational congestion-minimizing participants might find it optimal to increase their sharing level in response to an increase in the number of free-riders in the network. Another result from our analysis is that a certain amount of free-riding can actually induce sharing among previously nonsharing members of the community. That is, some free-riding could “wake up a self-centered community” and make them share.

Finally, we considered the situation in which a social planner can put incentive schemes in place to induce socially optimal levels of sharing. We show that socially optimal sharing levels can be achieved by using a simple incentive scheme whereby a participation fee is imposed for using the common external resource.

There are several limitations of this analysis that could form the basis for future studies on the subject of sharing in P2P communities. Our emphasis in this paper was to examine sharing as a response to congestion in the P2P network. Clearly, however, there could be other reasons for sharing, the most obvious being one that is altruistically motivated. It would be useful to study (perhaps using an experimental economics approach) whether participants become altruistic when they do not perceive common resources to be congested and thus naturally find a way out of the tragedy of commons.

Whereas altruism is a positive force, we also ignored forces such as security concerns that could inhibit sharing. When security is a concern, it is conceivable that even in the presence of congestion the participants will not share. Although in theory charging a higher fee to use common resources may work, engineering solutions that make sharing more secure will probably need to be simultaneously pursued. Otherwise, it may happen that the participants simply begin to leave the network and the community fails.

As a final direction for future research, it would be useful to combine the power of P2P networks with other commercially managed distribution methods, such as those offered by caching and replication (e.g., content delivery solutions). We are currently pursuing research that investigates the role of centrally managed content delivery solutions in the presence of organically provisioned P2P networks.

## 7. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## References

Adar, E., B. Huberman. 2000. Free riding on Gnutella. First Monday 5(10) 1–22.

Asvanund, A., M. Smith, R. Telang. 2003. Interest-based selforganization of peer-to-peer networks: A club economics approach. The 13th Workshop Inform. Technologies and Systems 4WITS 035, Seattle, WA.

Balakrishnan, H., V. Padmanabhan. 2001. How network asymmetry affects TCP. IEEE Comm. Magazine 39(April) 60–67.

Balakrishnan, H., V. Padmanabhan, R. H. Katz. 1997. The effects of asymmetry on TCP performance. Proc. 3rd ACM/IEEE Internat. Conf. Mobile Comput. Networking, ACM, New York, 77–89.

Banerjee, S., B. Bhattacharjee, C. Kommareddy. 2002. Scalable application layer multicast. Proc. ACM SIGCOMM.

Carr, J. 2003. Motorola plugs into content delivery network. Network Magazine (October 6). http://journals.iranscience .net:800/www.networkmagazine.com/www.networkmagazine .com/shared/article/showArticle.jhtml@articleId=15201422.

Castro, M., P. Druschel, A. Kermarrec, A. Nandi, A. Rowstron, A. Singh. 2003. SplitStream: High-bandwidth multicast in cooperative environments. Proc. Nineteenth ACM Sympos. Operating Systems Principles, ACM, New York, 298–313.

Chu, Y., J. Chuang, H. Zhang. 2004. A case for taxation in peerto-peer streaming broadcast. Proc. ACM SIGCOMM Workshop Practice and Theory Incentives and Game Theory Networked Systems, ACM, New York, 205–212.

Coffman, E. G., R. R. Muntz, H. Trotter. 1970. Waiting time distributions for processor-sharing systems. J. ACM 17(1) 123–130.

Cunningham, B. M., P. J. Alexander, N. Adilov. 2004. Peer-to-peer file sharing communities. Inform. Econom. Policy 16(2) 197–213.

Feldman, M., K. Lai, J. Chuang, I. Stoica. 2003. Quantifying disincentives in peer-to-peer networks. Proc. 1st Workshop Econom. Peer-to-Peer Systems, Berkeley, CA.

Fredj, S. B., T. Bonald, A. Proutiere, G. Régnié, J. W. Roberts. 2001. Statistical bandwidth sharing: A study of congestion at flow level. ACM SIGCOMM Comput. Comm. Rev. 31(4) 111–122.

Galenbe, E., R. Lent, A. Montouri, Z. Xu. 2002. Cognitive packet networks: QoS and performance. Proc. 10th IEEE Internat. Sympos. Modeling, Anal. Simulation Comput. Telecomm. Systems, Fort Worth, TX, 3–9.

Golle, P., K. Leyton-Brown, I. Mironov, M. Lillibridge. 2001. Incentives for sharing in peer-to-peer networks. Proc. 2nd Internat. Workshop Electronic Commerce, Springer-Verlag, London, 75–87.

Habib, A., J. Chuang. 2004. Incentive mechanism for peer-to-peer media streaming. Proc. 12th Internat. Workshop Quality Service 4IWQOS’045, Montreal, 171–180.

Hardin, G. 1968. The tragedy of the commons. Science 162 1243–1248.

Huang, C., T. Abdelzaher. 2005. Bounded-latency content distribution: Feasibility and evaluation. IEEE Trans. Comput. 54(11) 1422–1437.

Jiang, W., H. Schulzrinne. 2000. Modeling of packet loss and delay and their effect on real-time multimedia service quality. Proc. 10th Internat. Workshop Network and Operating Systems Support for Digital Audio and Video (NOSSDAV), Chapel Hill, NC.

Jiang, X., Y. Dong, D. Xu, B. Bhargava. 2003. GnuStream: A P2P media streaming system prototype. Proc. IEEE Internat. Conf. Multimedia and Expo 4ICME5, Baltimore, 325–328.

Kant, K., R. Iyer, V. Tewari. 2002. A framework for classifying peer-to-peer technologies. Proc. 2nd IEEE/ACM Internat. Sympos. Cluster Comput. Grid (CCGRID ’02), IEEE Computer Society, Washington, DC.

Kempe, D., A. Dobra, J. Gehrke. 2003. Gossip-based computation of aggregate information. Proc. 44th Annual IEEE Sympos. Foundations Comput. Sci. 4FOCS’035, IEEE Computer Society, Washington, DC, 482–491.

Kherani, A. A., A. Kumar. 2000. Performance analysis of TCP with nonpersistent sessions. Workshop on Modeling of Flow and Congestion Control. INRIA, Ecole Normale Supérieure, Paris.

Leith, D. J., P. Clifford, B. Malone, G. Ng. 2005. TCP fairness in 802.11E WLANs. IEEE Comm. Lett. 9(12) 964–966.

Mansour, Y., B. Patt-Shamir. 1998. Jitter control in QoS networks. Proc. 39th Annual Sympos. Foundations Comput. Sci., IEEE Computer Society, Washington, DC, 50–59.

Milojicic, D., V. Kalogeraki, R. Lukose, K. Nagaraja, J. Pruyne, B. Richard, S. Rollins, Z. Xu. 2002. Peer-to-peer computing. Technical report HPL-2002-57, Hewlett-Packard, Palo Alto, CA.

Pai, V., A. E. Mohr. 2006. Improving robustness of peer-to-peer streaming with incentives. Proc. First Workshop Econom. Networked Systems, Ann Arbor, MI.

Parameswaran, M., A. Susarla, A. Whinston. 2001. P2P Networking: An information sharing alternative. IEEE Comput. 34(7) 31–38.

Paxon, V. 1997. End-to-end Internet packet dynamics. Proc. ACM SIGCOMM Conf. Appl., Technologies, Architectures, Protocols Comput. Comm., ACM, New York, 139–152.

Pilosof, S., R. Ramjee, Y. Shavitt, P. Sinha. 2003. Understanding TCP fairness over wireless LAN. Proc. 22nd Annual Joint Conf.

IEEE Comput. Comm. Societies (INFOCOM 2003), San Francisco, 863–872.

Pouwelse, J., J. Taal, R. Lagendijk, D. Epema, H. Sips. 2004. Realtime video delivery using peer-to-peer bartering networks and multiple description coding. Proc. IEEE Internat. Conf. Systems, Man Cybernetics, The Hague, The Netherlands, 4599–4605.

Pucha, H., Y. Zhang, Z. M. Mao, Y. C. Hu. 2007. Understanding network delay changes caused by routing events. Proc. ACM SIGMETRICS Intl. Conf. Measurement Modeling Comput. Systems, ACM, New York, 73–84.

Ramaswamy, L., L. Liu. 2003. Free riding: A new challenge to peerto-peer file sharing systems. Proc. 36th Hawaii Internat. Conf. System Sci. (HICSS), Big Island, Hawaii.

Rejaie, R., S. Stafford. 2004. A framework for architecting peer-topeer receiver-driven overlays. Proc. 14th Internat. Workshop Network Operating Systems Support Digital Audio and Video, ACM, New York, 42–47.

Roberts, J. W., L. Massoulié. 2000. Bandwidth sharing and admission control for elastic traffic. Telecomm. Systems 15 185–210.

Sanneck, H., G. Carle. 2000. A framework model for packet loss metrics based on loss runlengths. Proc. SPIE/ACM SIGCOMM Multimedia Comput. Networking Cong. (MMCN), San Jose, CA.

Saroiu, S., K. P. Gummadi, S. D. Gribble. 2003. Measuring and analyzing the characteristics of Napster and Gnutella hosts. Multimedia System 39(2) 170–184.

Tan, G., S. A. Jarvis. 2006. A payment-based incentive and service differentiation mechanism for peer-to-peer streaming broadcast. Proc. 14th IEEE Internat. Workshop Quality Service 4IWQoS5, New Haven, CT, 41–50.

Trajkovic, L., S. J. Golestani. 1992. Congestion control for multimedia services. IEEE Network 6(5) 20–26.

Venkatasubramanian, N., K. Nahrstedt. 1997. An integrated metric for video QoS. Proc. 5th ACM Internat. Conf. Multimedia, ACM, New York, 371–380.

Vogells, W., C. Re, R. Renesse, K. Birman. 2002. A collaborative infrastructure for scalable and robust news delivery. Proc. 22nd Internat. Conf. Distributed Comput. Systems Workshops 4ICDCSW’025, IEEE Computer Society, Washington, DC, 655–659.

Xu, D., S. Kulkarni, C. Rosenberg, H. Chai. 2006. Analysis of a CDN–P2P hybrid architecture for cost-effective streaming media distribution. Multimedia Systems 11(4) 383–399.

Yeh, C. C., L. S. Pui. 2005. On the frame forwarding in peer-to-peer multimedia streaming. Proc. ACM Workshop Adv. Peer-to-Peer Multimedia Streaming, ACM, New York, 1–10.
