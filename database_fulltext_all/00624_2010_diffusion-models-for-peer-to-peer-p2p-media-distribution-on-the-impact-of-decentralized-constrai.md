---
otero_id: 624
otero_key: "XBFY4PCY"
title: "Diffusion Models for Peer-to-Peer (P2P) Media Distribution: On the Impact of Decentralized, Constrained Supply"
authors: "Kartik Hosanagar; Peng Han; Yong Tan"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0221"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [186.233.152.15] On: 05 May 2014, At: 01:03 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## 6SR

![](/api/attachments/XBFY4PCY/fulltext/images/e016c37273c05ec5bfdb4adc066ad603068d4e5475907985ccf207f56fa8578a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Diffusion Models for Peer-to-Peer (P2P) Media Distribution: On the Impact of Decentralized, Constrained Supply

Kartik Hosanagar, Peng Han, Yong Tan,

To cite this article:

Kartik Hosanagar, Peng Han, Yong Tan, (2010) Diffusion Models for Peer-to-Peer (P2P) Media Distribution: On the Impact of Decentralized, Constrained Supply. Information Systems Research 21(2):271-287. http://dx.doi.org/10.1287/isre.1080.0221

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XBFY4PCY/fulltext/images/4142232b1ab7fef7e6d02d7b44c27192ee44bd62c6843ed008a5333719f0b747.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Diffusion Models for Peer-to-Peer (P2P) Media Distribution: On the Impact of Decentralized, Constrained Supply

Kartik Hosanagar

Operations and Information Management, The Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104, kartikh@wharton.upenn.edu

Peng Han aQuantive, Inc. (Microsoft), Seattle, Washington 98104, realbug@gmail.com

Yong Tan Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195, ytan@u.washington.edu

n peer-to-peer (P2P) media distribution, users obtain content from other users who already have it. This form Iof decentralized product distribution demonstrates several unique features. Only a small fraction of users in the network are queried when a potential adopter seeks a file, and many of these users might even free-ride, i.e., not distribute the content to others. As a result, generated demand might not always be fulfilled immediately. We present mixing models for product diffusion in P2P networks that capture decentralized product distribution by current adopters, incomplete demand fulfillment and other unique aspects of P2P product diffusion. The models serve to demonstrate the important role that P2P search process and distribution referrals—payments made to users that distribute files—play in efficient P2P media distribution. We demonstrate the ability of our diffusion models to derive normative insights for P2P media distributors by studying the effectiveness of distribution referrals in speeding product diffusion and determining optimal referral policies for fully decentralized and hierarchical P2P networks.

Key words: peer-to-peer file diffusion; P2P; supply-constrained diffusion; free-riding; mixing model of diffusion; distributed systems

History: Sumit Sarkar, Senior Editor; Giri Kumar Tayi, Associate Editor. This paper was received on September 30, 2006, and was with the authors 12 months for 3 revisions. Published online in Articles in Advance August 31, 2009.

## 1. Introduction

Peer-to-Peer (P2P) networks are distributed networks in which the participants share their own resources in addition to consuming them from others. In P2P-based media distribution, users download content from other users who have the content and in turn redistribute it to future adopters. P2P allows a content provider to efficiently distribute content at a relatively low cost and is also effective in handling flash crowds in content distribution (Padmanabhan and Sripanidkulchai 2002). A number of encryption technologies have also emerged to prevent piracy in P2P networks. Thus, although the early use of the technology was for illegal file sharing, P2P is increasingly being adopted for legitimate media distribution on the Internet. P2P is being used for online radio (e.g., Social.fm), Internet TV (e.g., Joost), and software distribution (e.g., distribution of the RedHat Linux OS on BitTorrent). Recently, NBC Universal and AOL announced Internet TV initiatives based on P2P technologies. In addition, Altnet, iMesh, Grooveshark, rVibe, We7, and several other firms use a P2P distribution platform to sell music and other digital media licensed from the music labels. In 2004, there were over 50 million legal downloads per month on Kazaa for over 10,000 titles in Altnet’s library (Currah 2004).

In 2007, over 9.5 M music files were uploaded by 10,000 beta users of Grooveshark’s P2P music download service.<sup>1</sup>

Nodes in a P2P network are potential consumers of a digital product and, by virtue of the design of P2P networks, can redistribute the product upon buying it. P2P distribution is unique relative to centralized media distribution in that decentralized supply often imposes a constraint on demand fulfillment. In most P2P architectures, only a fraction of the nodes in the network are queried in response to a request to prevent flooding the network with queries. Thus, even if a file exists in a network, nodes containing the file might not always be queried. Furthermore, even if a node containing the requested file is queried, the node might not distribute the file. Free riders—users that consume content from the network, without sharing or redistributing it to other users— are known to be pervasive in P2P networks (Adar and Huberman 2000). As a result of these two factors, generated demand might not always be satisfied. Thus, “supply-side” factors related to incomplete search of the network and the redistribution incentives have a crucial impact on file diffusion within the network.

Commonly used redistribution incentives include penalties to users who free-ride and rewards to users who contribute. Penalties include intentionally slowing the download of free riders as in the BitTorrent protocol. Penalties are used sparingly in commercial P2P systems where users pay to obtain content. Commercial P2P networks often provide payments, known as distribution referrals, to users who distribute content to others in the network. Distribution referrals have been advocated in various studies (e.g., Golle et al. 2001, Arora et al. 2003) and are used in several commercial P2P networks. For example, Altnet pays users on the Kazaa network who agree to join Altnet as distribution points (New York Times 2003). Grooveshark and rVibe also compensate users for distributing content. In these networks, whenever a new user purchases a track, a small payment is made to the user that distributes the content to the buyer. rVibe currently pays the distributing user \$0.05 on a \$0.99 sale, and Grooveshark pays the user \$0.25 per sale (Techcrunch 2007). Hereafter, we refer to these payments as referrals.<sup>2</sup>

In this paper, we propose a model for diffusion of digital products in P2P networks that explicitly captures the supply-side factors—file search and redistribution incentives—described above and demonstrates the applicability of our model by studying optimal payments to users who distribute content. Modeling product diffusion is of considerable interest to managers. Diffusion models can be used for demand forecasting and for planning a variety of prelaunch and postlaunch strategic decisions such as optimal level of product sampling, optimal pricing, and optimal timing of successive generations of a product (Mahajan et al. 2000). As a result, product diffusion models have been actively studied in marketing for more than forty years. These models focus primarily on the demand generation process. They generally assume that the generated demand is always fulfilled and do not model the important supply-side constraint in P2P networks. The few papers in the product diffusion literature that have modeled supply constraints have done so in centralized settings where supply does not depend on the number of current adopters or actions taken by them. In contrast, current adopters generate the supply in P2P diffusion. These supply-side factors, tied to the file search process and free-riding in the network, significantly influence product diffusion in P2P networks and are in fact of most interest to P2P network managers. It is thus important to incorporate these into diffusion models.

Our study of product diffusion in P2P networks makes three main contributions. First, we develop a diffusion model that incorporates supply-side constraints unique to P2P networks, and we derive analytical results about the sales dynamics. Specifically, we develop a mixing model of file diffusion that incorporates both incomplete search and free-riding in P2P networks. Second, we present an application on optimal referrals that endogenizes the impact of distribution referrals on file availability and overall profits. We derive expressions for the optimal referral and show that a referral policy that accounts for diffusion dynamics is far more profitable than a myopic policy that ignores these dynamics. Finally, we demonstrate that the file search architecture exerts a strong influence on diffusion. We find that a hierarchical architecture with a few groups demonstrates faster diffusion than flat P2P networks. However, there are diminishing returns from increased centralization.

The rest of this paper is organized as follows. In §2, we review related literature. In §3, starting with existing epidemiological models, we develop analytical models to capture the dynamics of diffusion in P2P networks. Section 3.1 introduces the notation. Section 3.2 develops diffusion models for flat P2P networks and includes a study of the optimal referral policy. Section 3.3 focuses on product diffusion and optimal referrals in hierarchical P2P networks and examines the impact of the search architecture on the rate of diffusion. In §3.4 we use simulations to test the robustness of the models under more general demand processes. Section 4 concludes this study and discusses future work.

## 2. Literature Review

There are three streams of work highly relevant to our study of P2P content diffusion. The first two relate to the literature on new product diffusion and epidemiological diffusion, respectively. The third relates to studies of free-riding in P2P networks and the use of referral payments to address the same.

## 2.1. Product Diffusion

Direct work on P2P content diffusion is limited. A notable exception is the work by Izal et al. (2004) on an empirical study of file diffusion in the BitTorrent network. Developing an analytical model of file diffusion within networks is not the focal point of the paper. However, there is a vast body of work on new product diffusion models, dating back to 1960s. Fourt and Woodlock (1960) propose a product diffusion model in which a fixed fraction of the consumers who have not yet bought the product do so every period. Bass (1969) proposed an extension that additionally incorporates word of mouth (WOM) communication between current adopters and potential adopters. Building on this model, work has also been done to incorporate effects of advertising and promotion (Horsky and Simon 1983), competition (Krishnan et al. 2000) and pricing (Bass 1980).

These diffusion models focus on demand generation and assume that demand is always fulfilled. In P2P networks, a potential adopter can conduct only an incomplete search of the network, and even the queried nodes may free-ride. As a result, demand is often not fulfilled immediately. In this sense, the supply-constrained diffusion models of Ho et al. (2002), Kumar and Swaminathan (2003), and Jain et al. (1991) are more relevant to our diffusion model. These papers study situations where demand is not met because of production capacity constraints. However, they focus on centralized settings wherein the managerial intervention is tied to capacity sizing. In contrast, the distribution infrastructure in P2P networks is decentralized, and the product supply involves a social process. The more the number of current adopters and higher their willingness to distribute a product, the greater is the file availability in the network. Thus, product adoption directly increases product supply. Furthermore, the relevant managerial interventions relate to the design of the search process and incentives to encourage nodes to distribute content rather than an increase in the centralized capacity. Our diffusion model uniquely captures these variables and the dependence between product diffusion and social supply.

## 2.2. Epidemiological Diffusion

Infectious diseases spread from infected nodes to susceptible nodes and are examples of decentralized diffusion processes. Epidemic diffusion models have been used in computer networking research, including in studies of information diffusion in mobile ad hoc networks (Khelil et al. 2002) and spread of computer viruses (Kephart and White 1991). The diffusion mechanism in P2P networks is in many ways similar to the spread of diseases. Broadly speaking, when a node seeks content in a P2P network, a request is sent out to other nodes in the network. File transfer is completed once a node is found that shares the desired resource. Similarly, in the spread of diseases, an infected individual makes contact with people around her and disease transmission occurs once a susceptible individual is contacted. Thus, the susceptible in epidemic diffusion is analogous to the node seeking content in P2P and the infected is analogous to the node that distributes content.

Despite these similarities, diffusion in a P2P network is unique in several ways. One major difference is that the susceptible agent typically receives a disease passively, whereas the node seeking content initiates the contact in P2P diffusion. This implies that epidemic contact occurs in a semi-random manner, while the search process in P2P network is not. P2P search can be architected and the design choices have a notable impact on diffusion. For example, although the content in P2P networks is always distributed, the search process can be completely centralized, completely decentralized/flat, or hierarchical (Asvanund et al. 2004). Networks like Napster maintained a single central catalog and search requests were forwarded to the central server. Gnutella version 0.4 is completely decentralized, with each node maintaining its own catalog and responding to search queries. Gnutella version 0.6 and Kazaa use a hierarchical architecture wherein nodes connect to supernodes, which are in turn connected to each other. The supernodes index the content for their nodes and respond to search requests. An additional difference is that the reproductive capacity of a virus usually grows proportionately with the diffusion of a disease. In contrast, file availability and free-riding impose a constraint on product diffusion in P2P networks. Finally, epidemiologists are interested in slowing the diffusion through vaccinations or by quarantining the infected. P2P managers are interested in speeding the diffusion by appropriately architecting P2P search process or using referrals and other incentives to encourage users to distribute content.

## 2.3. Free-Riding in P2P and Payment-Based Incentives

Free-riding, which has been widely documented in P2P networks (Adar and Huberman 2000, Asvanund et al. 2004), can slow the diffusion of products within the network. Several approaches have been proposed to alleviate this problem, for example, offering higher quality of service (QoS) to users that share their resources (Kamvar et al. 2003). In commercial P2P networks, where users pay for content, content providers can use payments to encourage users to distribute content to others in the network (Arora et al. 2003, Lang and Vragov 2005). Golle et al. (2001) discuss the use of micropayments to reward peers for distributing content. A number of commercial P2P systems such as Grooveshark and rVibe use payment-based incentives to encourage users to share and distribute content.

## 3. P2P Diffusion Model

The diffusion models we develop are homogeneous mixing models. In homogeneous mixing models, there is no spatial structure, i.e., specific neighbors of a node are not modeled, and all nodes within a compartment (i.e., of the same type) run the same risk of being infected. One can use the equivalent of mean field analysis for large populations N →  to develop differential equations that capture the dynamics.<sup>3</sup> Popular examples of homogeneous mixing models include the SIR/SIS models in epidemiology (Diekmann and Heesterbeek 2000), Bass model in marketing (Bass 1969) and the Lotka-Volterra model in population ecology (Brauer and Castillo-Chavez 2000). The implication of the homogeneous mixing setup is that we do not model the specific topological connections in the P2P network. The diffusion dynamics depend only on the number of nodes seeking or distributing content rather than which particular nodes seek or distribute content. We model the search process in P2P networks within the framework of the homogeneous mixing model. Specifically, groups in hierarchical networks are modeled as additional compartments in the diffusion model.

We begin by introducing our notation in §3.1. In §§3.2 and 3.3, we focus on diffusion in completely decentralized (flat) networks and hierarchical networks, respectively.

## 3.1. Notation, Definitions, and Assumptions

Consider a digital product such as a music file being distributed in a P2P network. Nodes in the network are potential consumers of the product and can obtain it from nodes that already have the product. Whenever a node distributes a copy of the digital product to another node, it gets a referral payment from the firm. In the discussion below, we assume that the firm paying the referral fee is the copyright holder.<sup>4</sup>

Let N denote the total number of nodes in the network. We assume that there is no intermediary—i.e., a node that buys and sells the product while not seeking it—and that a node is used by one individual only, so no node consumes a file more than once. Thus N is also the market potential or the total number of nodes that might eventually buy the product. The nodes that have the product already are called satisfied nodes. The number of satisfied nodes in the network at time t is denoted by Qt, and the fraction of nodes that are satisfied is $q ( t ) = Q ( t ) / N$ . The nodes that do not yet have the product are called seeking nodes. The number of seeking nodes at t is $N - Q ( t )$ , and the fraction of seeking nodes in the network is $( 1 - q ( t ) )$ . $\beta$ denotes the rate at which seeking nodes attempt to seek the product. Seeking nodes can obtain the product from satisfied nodes. Note, however, that not all satisfied nodes distribute the product. Satisfied nodes that are willing to distribute the product are called seeds. The number of seeds and fraction of nodes that are seeds are denoted by $S ( t )$ and $s ( t ) = S ( t ) / N$ , respectively. In the rest of the model development, we simplify notation by denoting the number of seeking nodes, satisfied nodes and seeds by $( N - Q ) , Q ,$ , and $S ,$ respectively (and the corresponding fractions by $( 1 - q ) , q ,$ and s). It is implied that these are dynamic variables. Note that a satisfied node does not have to be a seed, but a seed must be a satisfied node first. Thus, $S \le Q$

We assume that the network contains some altruistic nodes that are always willing to be seeds even if there is no compensation for doing so and that the remaining nodes are “strategic,” i.e., they will not be a seed unless the distribution referral is greater than their cost of being a seed. The fraction of nodes that are altruistic is denoted by  and the number of altruistic seeds is $\alpha Q .$ The assumption of altruistic nodes is without loss of generality as  might be set equal to zero. However, some users are known to distribute content in $\mathrm { P } 2 \mathrm { P }$ networks in which no distribution referral is offered. This willingness to share might be fueled by a sense of community, reciprocity, or other such factors. Let c denote a node’s cost of distributing a file and r denote the referral payment made to the seed that distributes the file. A strategic satisfied node will be a seed if and only if $c \leq r .$ . Assuming that c is Uniformly distributed in $[ 0 , C ]$ across the strategic nodes, the number of strategic satisfied nodes that act as seeds is $( 1 - \alpha ) Q ( r / C )$ . Therefore,

$$
S = \left\{ \begin{array}{l l} \bigg (\alpha + \frac {r}{C} (1 - \alpha) \bigg) Q, & \text { if } r \leq C; \\ Q, & \text { otherwise }. \end{array} \right.\tag{1}
$$

When $r = 0 ,$ , file distribution relies solely on the goodwill of the altruistic nodes. We also assume that the firm is unable to price discriminate, i.e., altruistic nodes also get the referral even though they would share regardless.

Finally, we describe the search process in the network and associated notation. We consider both a completely decentralized as well as a hierarchical network in this paper. In a completely decentralized or flat network, whenever a seeking node seeks a file, i neighbors of the seeking node are randomly selected and queried. Each of the queried nodes again forwards the request to another i unique nodes. This process continues until the maximum number of hops, denoted by $j ,$ is reached. Thus, the request will be sent to a total of $k = i + i ^ { 2 } + \cdots + i ^ { j } = i ( \bar { i } ^ { j } - 1 ) / ( i - 1 )$ nodes. The search fails if none of these k nodes are seeds.<sup>5</sup> In Gnutella 0.4, a seeking node will query 7 of its neighbors. If these nodes do not have the file, they each contact 7 of their neighbors, and so on until the maximum hop count of 10 is reached (Ross and Rubenstein 2003).

Figure 1 Hierarchical P2P Network  
![](/api/attachments/XBFY4PCY/fulltext/images/a6d2210dc619ab9cbb31e6c5d73074342b680f4ed2b0eca19ed619a8fb68068c.jpg)

Now consider a 2 level hierarchical P2P network in which N nodes are organized into M groups. We assume that all the groups are homogenous, except that one of them labeled Group-I has the initial satisfied node. Because the assignment of nodes to groups in current P2P networks is independent of both the request rate of the nodes and the content supplied by them (Garces-Erice et al. 2003), the assumption of homogeneity across groups is reasonable. The number of nodes in any group is given by $n = N / M .$ The number of satisfied nodes and fraction of nodes that are satisfied in Group-I are denoted $Q _ { I }$ and $q _ { I }$ respectively. Similarly, Q and $q$ denote the corresponding variables for the other groups. Each group in the network has a supernode that provides indexing services to all the nodes within its group, as shown in Figure 1. Any request from a seeking node will be satisfied if there is a seed within the group, because the supernode indexes all nodes in the group and can forward the request to the seed directly. If there is no seed in the group, the supernode forwards the request to $( l - 1 )$ randomly selected groups.<sup>6</sup> Thus, a total of l groups in the network are queried. The probability that a randomly queried satisfied node distributes the file is given by $\phi = \alpha + ( 1 - \alpha ) r / C$ . Thus, given nq satisfied nodes in a group, the probability that there is no seed in the group is $p = ( 1 - \phi ) ^ { n q }$ . Similarly, the probability that there is no seed in Group-I is $p _ { I } = ( 1 - \phi ) ^ { n q _ { I } }$

Table 1 Glossary of Terms

<table><tr><td>t</td><td>Time</td></tr><tr><td>N</td><td>Total number of nodes in the network (also the market potential)</td></tr><tr><td>Q(t)</td><td>Number of satisfied nodes at time t, Q(0) &gt; 0; q = Q/N</td></tr><tr><td>S(t)</td><td>Number of seeds at time t, S(0) &gt; 0; s = S/N</td></tr><tr><td>α</td><td>Fraction of nodes that are altruistic</td></tr><tr><td>β</td><td>Average rate at which a seeking node seeks content</td></tr><tr><td>r</td><td>Referral per download offered to a node that distributes content</td></tr><tr><td>c</td><td>The cost per unit time of being a seed, c ∈ U[0, C]</td></tr><tr><td colspan="2">Notation for a flat P2P network</td></tr><tr><td>i</td><td>Number of requests generated by seeking nodes in a flat network</td></tr><tr><td>j</td><td>Maximum number of hops for requests in a flat network</td></tr><tr><td>k</td><td>Maximum number of nodes queried, k = i(i^j - 1)/(i - 1)</td></tr><tr><td colspan="2">Notation for a hierarchical P2P network</td></tr><tr><td>M</td><td>Total number of groups in a hierarchical network</td></tr><tr><td>n</td><td>Number of nodes in a single group (n = N/M)</td></tr><tr><td>I</td><td>Number of groups queried in a hierarchical network</td></tr><tr><td>Q_i, q_i</td><td>Number and fraction of satisfied nodes in Group-I</td></tr><tr><td>Q, q</td><td>Number and fraction of satisfied nodes in a group other than Group-I</td></tr><tr><td>φ</td><td>Probability that a randomly queried satisfied node distributes the file</td></tr><tr><td>p = (1 - φ)^nq</td><td>Probability that there is no seed in a group other than Group-I</td></tr><tr><td>p_I = (1 - φ)^nq_I</td><td>Probability that there is no seed in Group-I</td></tr></table>

Table 1 summarizes the notation that will be used in the rest of this paper.

## 3.2. Diffusion Model for Flat Networks

We begin by considering a completely decentralized P2P network. Whenever a seeking node seeks content, requests are sent to other nodes and forwarded within the network. A maximum of k nodes are queried as described in §3.1. If a request reaches a seed, the file is transferred to the seeking node, which then becomes a satisfied node. Otherwise, the request fails and the status of the seeking node remains unchanged. The node can return in a later period to seek the content. Because $\beta$ is the rate at which a seeking node seeks content, $\beta ( N - Q )$ is the total number of seeking nodes seeking content at an instant when there are Q satisfied nodes. If each of these nodes sends out k requests, $( 1 - ( 1 - ( S / N ) ) ^ { k } )$ is the fraction of the nodes that reach at least one seed.<sup>7</sup> Thus, the mean field diffusion equation for $Q { \mathrm { - i . e . , } }$ , the average rate at which seeking nodes become satisfied nodes—is

$$
\begin{array}{c} \frac {d Q}{d t} = \beta (N - Q) \bigg (1 - \bigg (1 - \frac {S}{N} \bigg) ^ {k} \bigg), \quad \mathrm{or} \\ \frac {d q}{d t} = \beta (1 - q) (1 - (1 - s) ^ {k}). \end{array}\tag{2}
$$

We can substitute the expression for S from (1). A referral equal to C ensures that every satisfied node is a seed. Thus a referral greater than C is unnecessary. Substituting (1) into (2) and assuming $r \leq C ,$

$$
\frac {d q}{d t} = \beta (1 - q) (1 - (1 - \phi q) ^ {k}),\tag{3}
$$

where $\phi = ( \alpha + ( 1 - \alpha ) r / C )$ . Solving the above differential equation with the initial condition of $Q ( 0 ) = 1$ $( \mathrm { o r } , q ( 0 ) = q _ { 0 } = 1 / N )$ , we obtain the following solution $\cdot ^ { 8 }$

$$
\begin{array}{l} \frac {1}{a ^ {k} - 1} \ln (x - a) - \frac {1}{k (a - 1)} \ln (x - 1) \\ - \frac {1}{k} \sum_ {j = 1} ^ {k - 1} \frac {x _ {j}}{a - x _ {j}} \ln (x - x _ {j}) = \beta t + C _ {1}, \end{array}\tag{4}
$$

where $a = ( 1 - \alpha ) ( 1 - r / C ) , x = 1 - \phi q , C _ { I }$ is a constant of integration computed in the online supplement, and $x _ { j } = e ^ { i 2 \pi j / k }$ is the jth root of $x ^ { k } = 1$ , not including $x = 1$ . In the supplement, we show that (4) has no imaginary parts and that the solution is unique. We also show that sales $( d q / d t )$ is unimodal.

Proposition 1. The product penetration $q ( t _ { c } )$ at a given time instant $t _ { c }$ increases with k in a convex fashion early in the file’s diffusion (small $q )$ and in a concave fashion late in the diffusion (large q. The time $t ( q _ { c } )$ to achieve a given level of product penetration $q _ { c }$ decreases with k in a convex fashion.

The proof is in the appendix. Figure 2 illustrates Proposition 1 for sample parameter values $( N = 1 0 , 0 0 0 , \ Q ( 0 ) = 1 , \ C = 1 , \ \alpha = 0 . 1 , \ \beta = 0 . 5 ,$ , and $r = 0 . 2 )$ . The time to achieve 50% network penetration decreases with k in a convex manner, and product penetration after 8 time units (q(8)) is S-shaped in k. Proposition 1 indicates that the marginal benefit of querying more nodes can be increasing early in the diffusion, but once there are sufficient satisfied nodes, querying more nodes no longer provides the significant returns that it did before. Considering the negative effects of request flooding, there should be a threshold beyond which any further increase in k is not desirable. One potential impact of request flooding is that nodes have to respond to many more requests, which in turn might reduce their likelihood of serving as seeds. Our model does not explicitly incorporate these costs of request flooding. However, additional analysis reveals that if the number of seeds decreases with k in a concave manner, there could be a threshold value of k beyond which the gains identified in Proposition 1 are offset by the reduction in the seeds. The analysis is omitted from this paper but is available on request from the authors.

Figure 2 Impact of Querying More Nodes on Diffusion Speed  
![](/api/attachments/XBFY4PCY/fulltext/images/094453b42332cfb86fb0521864dc0a3b47aec7e37b0e6eeaf65933139aab165f.jpg)

Proposition 2. The product penetration $q ( t _ { c } )$ at a given time instant $t _ { c }$ increases with the referral r. Simultaneously, the time $t ( q _ { c } )$ to achieve a given level of product penetration $q _ { c }$ decreases with r in a convex fashion.

The proof is in the appendix. An increase in the referral increases the willingness of satisfied nodes to serve as seeds. This, in turn, increases file availability and helps speed product diffusion. There is a tradeoff between offering a high referral to speed diffusion and reducing the referral to increase margins. We evaluate this trade-off in §3.2.1 to compute the optimal referral $r ^ { * }$

Consider a special case in which $k = 1 .$ , i.e., only one node in the network is queried whenever a seeking node attempts to obtain the content. Equation (3) can now be solved to obtain the following closed-form expressions:

$$
q (t, r) = \frac {1}{1 + (N - 1) e ^ {- A (r) t}},\tag{5}
$$

and

$$
t (q, r) = \frac {1}{A (r)} \left(\ln \frac {q}{1 - q} + \ln (N - 1)\right),\tag{6}
$$

where $A ( r ) = \beta ( \alpha + r ( 1 - \alpha ) / C )$ . Equations (5) and (6) specify an S-shaped P2P diffusion curve. These equations can be used to derive the optimal referral that the firm should offer. We turn to that question now.

3.2.1. Optimal Referral. We demonstrate the applicability of the diffusion model by studying optimal referral strategies in P2P networks. Diffusion modeling can be particularly useful here relative to myopic policies that determine referrals based on the immediate impact on sales without accounting for the impact on future sales.

Denote the length of the planning horizon by T . Assume the referral r is constant throughout the planning horizon, and the unit price of the product is constant and normalized to 1. The firm’s profit from each sale is $( 1 - r )$ . Thus, the referral optimization problem is

$$
\max _ {r} \left(\int_ {0} ^ {T} (1 - r) \frac {d q}{d t} d t\right) \approx (1 - r) q (T).\tag{7}
$$

In the equation above,<sup>9</sup> we do not discount future sales for analytical tractability. The referral optimization problem for arbitrary values of k is relatively easy to solve numerically, but closed-form results are hard to come by. In the following analysis, we focus on the case in which k 1 due to the tractability it affords. Numerical analysis suggests that although the magnitude of the referrals changes with $k ,$ the results are qualitatively similar to the ones highlighted below.

Substituting qt from (5) into (7) and computing the first-order condition with respect to r gives

$$
\begin{array}{l} (N - 1) \exp \left(- \beta T \bigg (\alpha + (1 - \alpha) \frac {r}{C} \bigg)\right) \\ \cdot \left(\beta T (1 - \alpha) \frac {1 - r}{C} - 1\right) - 1 = 0. \end{array}\tag{8}
$$

Solving (8) and imposing the bounds on $r ,$ the result follows (proof in the appendix).

Proposition 3. The optimal referral for the flat P2P network with diffusion specified by (5) is

$$
r ^ {*} = \max \left[ 0, \min \left[ C, 1 - \frac {C}{\beta T (1 - \alpha)} \left(1 + W \left(\frac {1}{N - 1} \right. \right. \right. \right.
$$

$$
\left. \left. \cdot \exp \left(\beta T \left(\alpha + \frac {1 - \alpha}{C}\right) - 1\right)\right)\right) \biggr ] \biggr ],\tag{9}
$$

where W x is the Lambert W -function (solution of $W ( x ) \exp ( W ( x ) ) = x )$

Using the properties of the Lambert W -function, the following properties of the optimal referral are derived in the appendix.

Proposition 4. The optimal referral is (a) nonincreasing with the fraction of nodes in the network that are altruistic , (b) nondecreasing with the P2P network’s size N , and (c) nondecreasing with request rate $\beta$ for $\beta < \beta _ { t h }$ and nonincreasing with $\beta$ for $\beta > \beta _ { t h } ,$ where

$$
\begin{array}{l} \beta_ {t h} = \frac {1}{T} \bigg (2 + W ((N - 1) e ^ {- 1}) + \frac {e}{N - 1} \\ \qquad \cdot \exp (W ((N - 1) e ^ {- 1})) \bigg) \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) ^ {- 1}. \end{array}\tag{10}
$$

As expected, an increase in the number of altruistic nodes reduces the need for a high referral. Similarly, product penetration occurs at a slower rate in a large network (see (5)). As a result, a higher referral is needed to speed the diffusion in a large network.

Figure 3 illustrates the impact of $\beta$ for sample parameters $( N = 1 0 , 0 0 0 , \ Q ( 0 ) = 1 , \ C = 1 , \ \alpha = 0 . 1 )$ When $\beta$ is extremely small, i.e., request rate among seeking nodes is low, the best strategy for the firm is to offer no referral. This is because the bottleneck is not free-riding but the low rate of demand generation. Once $\beta$ reaches a certain threshold value, the referral starts having an impact and thus increases. Finally, a very high request rate helps speed up diffusion considerably. This helps generate altruistic satisfied nodes at a faster rate, which in turn reduces the need for a very high referral. As a result, we observe the switch from a nondecreasing relationship to a nonincreasing relationship between $r ^ { * }$ and $\beta .$

Now consider a myopic referral policy that does not account for the impact of referrals on future sales. The myopic referral maximizes the instantaneous profit given by

Figure 3 Optimal Referral vs. Request Rate  
![](/api/attachments/XBFY4PCY/fulltext/images/69702adc2f7596dfb3b90d05a4ff98f8f00de78b9546cd8dadc17f32cd46f5bf.jpg)

$$
\pi (t) = (1 - r) \frac {d q}{d t} = (1 - r) \beta \left(\alpha + \frac {r (1 - \alpha)}{C}\right) (1 - q) q.\tag{11}
$$

Setting d! $/ d r = 0 .$ , the optimal myopic referral is

$$
r _ {M} ^ {*} = \frac {1}{2} - \frac {C \alpha}{2 (1 - \alpha)}.\tag{12}
$$

Proposition 5. The myopic referral is nonincreasing with the fraction of nodes that are altruistic  and independent of both the request arrival rate $\beta$ and the network size N .

The proof follows from (12) and imposing the bounds on the referral. Interestingly, the myopic referral, unlike the optimal referral, is independent of both the request arrival rate $\beta$ and the network size N . This is because the instantaneous profit depends on the instantaneous demand, the fraction that is fulfilled, and the margin per sale. The referral impacts only the fraction of demand that is fulfilled and the margin per sale, but not the instantaneous demand, which is fixed for the purpose of computing the instantaneous sales. As a result, factors such as $\beta$ and $N ,$ that influence only the instantaneous demand but not demand fulfillment or margins, are irrelevant to the computation of the myopic referral. In contrast, the optimal policy accounts for the fact that the referral impacts the demand generated in future periods, and thus the optimal referral interacts with the demand terms.

Figure 4 Profit Differential Between Optimal and Myopic Referral  
![](/api/attachments/XBFY4PCY/fulltext/images/30c4d92a818e1fac04c4040ea00088f002a8228ec430ae670950aa17fd3feef2.jpg)

In Figure 4, we plot the percentage increase in profit achieved by the optimal referral relative to the myopic referral against the fraction of altruistic nodes in the network () and the request rate (). The remaining parameters are $N = 1 0 , 0 0 0 , T = 2 0$ , and $C = 1$ . When is high or $\beta$ is too low or too high, the need to offer referrals diminishes (see Propositions 4 and 5). Hence, it does not matter whether a myopic or optimal referral is offered. However for intermediate request rates and low levels of altruism, as observed in reality (Izal et al. 2004, Adar and Huberman 2000), the optimal referral significantly outperforms the myopic referral.

## 3.3. Diffusion in Hierarchical P2P Networks

A number of P2P networks are hierarchical, rather than completely decentralized to reduce query flooding. Kazaa, a popular P2P network, has a two level structure where leaf nodes are organized into groups. A rough estimate from 2003 indicates that there were 10,000 groups in the Kazaa network with the supernode in each group handling 200 to 500 nodes (Ross and Rubenstein 2003).

Consider a 2 level hierarchical P2P network with M groups. As described in §3.1, the supernode of the seeking node’s group will query all nodes within the group and also forward the request to (l−1) neighboring groups. Let us first consider diffusion in Group-I:

$$
\begin{array}{r l} \frac {d q _ {I}}{d t} & = \beta (1 - q _ {I}) (1 - p _ {I} p ^ {l - 1}) \\ & = \beta (1 - q _ {I}) (1 - (1 - \phi) ^ {n (q _ {I} + (l - 1) q)}). \end{array}
$$

(13)

In (13), $\beta ( 1 - q _ { I } )$ is the generated demand and $( 1 - p _ { I } p ^ { l - 1 } )$ is the fraction of this demand that is fulfilled $( p _ { I }$ and $p$ represent the probability that there is no seed in Group-I and another group, respectively).

Now consider diffusion in the remaining $( M - 1 )$ groups. The generated demand in any group is $\beta ( 1 - q )$ . The probability that there is a seed within a group is $( 1 - p )$ . When there is no seed within the group, two cases arise. The first case is one in which all $( l - 1 )$ requests are forwarded to groups other than Group-I. The probability of this case (i.e., of not querying Group-I) is

$$
\binom {M - 2} {l - 1} \cdot \binom {M - 1} {l - 1} ^ {- 1} = \frac {M - l}{M - 1}.\tag{14}
$$

The probability that one of these $( l - 1 )$ groups contains a seed is $( 1 - p ^ { l - 1 } )$ . The second case is one in which one of the $( l - 1 )$ requests goes to Group-I, and the remaining $( l - 2 )$ requests are sent to other groups. The probability of querying Group-I is $1 - ( M - l ) /$ $( M - 1 ) = ( l - 1 ) / ( M - 1 )$ . The probability that one of the groups contains a seed is $\bar { ( 1 - p _ { I } p ^ { l - 2 } ) }$ . Hence, the probability that generated demand is fulfilled is

$$
(1 - p) + p \left(\frac {M - l}{M - 1} (1 - p ^ {l - 1}) + \frac {l - 1}{M - 1} (1 - p _ {I} p ^ {l - 2})\right).\tag{15}
$$

Substituting the expression for $p$ and $p _ { I } ,$ we get the diffusion equation

$$
\begin{array}{l} \frac {d q}{d t} = \beta (1 - q) \bigg (1 - (1 - \phi) ^ {n (l - 1) q} \\ \qquad \cdot \left(\frac {M - l}{M - 1} (1 - \phi) ^ {n q} + \frac {l - 1}{M - 1} (1 - \phi) ^ {n q _ {l}}\right) \bigg). \end{array}\tag{16}
$$

We can jointly solve (16) and (13) to obtain the diffusion trajectory in each of the groups. The diffusion curve for the network as a whole is then obtained by aggregating the diffusion curves across all $\mathrm { g r o u p s . } ^ { 1 0 }$ While (13) and (16) can be solved numerically, there is no closed-form solution to these differential equations. The numerical solutions are discussed below.

Figure 5 plots the diffusion curves based on (13) and (16) for different values of M. The remaining parameters are $N = 1 0 , 0 0 0 , \ C = 1 , \ \alpha = 0 . 1 , \ \beta = 0 . 5 ,$ $l = 2 ,$ and $r = 0 . 2$ . When the number of groups M

Figure 5 Diffusion Process Under Varying Levels of Network Centralization  
![](/api/attachments/XBFY4PCY/fulltext/images/d7e4baa1ea5c163015475c47eb20e6b96f1188052be1437940742e65f8046859.jpg)  
is large, the P2P network is similar to the decentralized network of §3.2. As M decreases, the fraction of requests reaching a seed increases significantly relative to a completely flat network and product diffusion occurs faster. Figure 6 plots the time to achieve

Figure 6 Impact of Network Centralization on Time to Achieve 50% Network Penetration  
![](/api/attachments/XBFY4PCY/fulltext/images/57d3bb488ab03fd1ada2d8ff2d41e34b4b557faaa073c9c61502fa9cb12682bf.jpg)

Figure 7 Impact of Incomplete Search and Free-Riding on Diffusion Speed  
![](/api/attachments/XBFY4PCY/fulltext/images/7f3660ea130f85e4b55eb08141cc230f213c71332769165aa4746741f3dcca06.jpg)  
50% network penetration for the same parameters as in Figure 5. Initially, as we move from a flat structure to hierarchical structure, a small decrease in M will result in a significant reduction in diffusion time. However, as M reaches a sufficiently small value, further centralization will not necessarily help speed up the diffusion noticeably. The bottleneck is no longer the incomplete search of the network; rather, the bottlenecks are the rate of demand generation and the willingness of satisfied nodes to distribute the file. Given that the primary motivation for reducing the number of groups is to speed diffusion, there is little reason to prefer a completely (or nearly) centralized P2P architecture given other drawbacks of centralized structure, such as the increased load on supernodes. For example, Figures 5 and 6 suggest that there is little to gain by reducing groups below 50 for the given network configuration.

To illustrate the joint impact of incomplete search and free-riding, Figure 7 plots the time to achieve 50% network penetration against the number of groups in the network M and the distribution referral r. Other parameters are the same as in Figure 5. When both aspects of supply are active constraints, there is much to gain by increasing the referral, reducing the number of groups in the network, or both. However, if the referral is very high, then almost all nodes distribute the file, and the gains from reducing M are somewhat modest. Similarly, if the network is highly centralized, the referral might not be as crucial. This,

Figure 8 Impact of Search Process on Optimal Referral  
![](/api/attachments/XBFY4PCY/fulltext/images/4bc6d2038652144b6e44c5e0e5cd0c5aa1aa01ae73616ebed04e0a71c62547af.jpg)  
of course, assumes that there are sufficient altruistic nodes in the network $( \alpha = 0 . 1$ in Figure 7). If most nodes in the network are not altruistic, then a referral will still be needed even with considerable centralization of the network. In summary, there are a number of interesting design parameters $\left( M , r , l \right)$ available to managers and network designers that can be carefully tuned based on the diffusion model.

3.3.1. Optimal Referral in Hierarchical Networks. In this section, we investigate the optimal referral in the hierarchical network. Because of the complexity of the diffusion equation for a hierarchical network, we cannot derive a closed-form analytic expression for the optimal referral. We evaluate it numerically using $( 7 )$ as the objective function and (13) and (16) as the diffusion equations. Figure 8 plots the optimal referral $r ^ { * }$ against the number of groups in the network (M) and the number of requests forwarded (l). The other parameters are $N = 1 0 , 0 0 0 _ { \cdot }$ $C = 1$ $\alpha = 0 . 1$ $\beta = 0 . 5 .$ . Increasing the number of requests helps reduce the magnitude of the referral. Furthermore, increasing the degree of centralization of the P2P network (i.e., reducing M) reduces the need to offer high referrals (provided there are a reasonable number of altruistic nodes). At the same time, if there are very few altruistic nodes in the network, then increasing the degree of centralization cannot entirely replace the need for referrals (Figure 9).

## 3.4. Simulations

Our diffusion models focus on supply-side factors and model a simple demand process based on mean field analysis. We now use simulations to study the robustness of the models under more general demand processes. Specifically, the simulations incorporate heterogeneity by allowing  to vary across nodes. Furthermore, given the mean request rate $\beta$ for any node, the simulation models a Poisson request generation process for each node (recollect that the model assumed a deterministic process). Thus, the timing of requests varies across simulation runs. We then compare the average outcome over these runs with the predictions from the models.

Figure 9 Impact of Altruism and Network Centralization on Optimal Referral  
![](/api/attachments/XBFY4PCY/fulltext/images/ea680379b57620acf96e2a4bc37dc79ae68a4ad17c13c93784e32184570e25aa.jpg)

The input to a simulation is the parameter set $\{ N , \alpha , \beta , C , r \}$ . Further {k} or {l, M } are additionally specified based on the type of network. First, N nodes are generated. A fraction () of nodes are randomly selected to be altruistic nodes. For the remaining nodes, the cost of being a seed (c) is drawn from a Uniform distribution in 0 C. Before the diffusion begins, one of the nodes is randomly chosen as the initial satisfied node. To allow heterogeneity, the content seeking rate is uniformly distributed from 0.5 to 1.5 across the nodes. Given the mean seeking rate of a node, the request process is modeled as a Poisson distribution. That is, the time between successive attempts by a specific seeking node to locate content is drawn from an exponential distribution. Hierarchical networks are simulated by randomly forming M groups before the diffusion begins. Each group has a randomly selected supernode.

The diffusion process is simulated through a series of discrete steps. In the first step, the time until the first request is drawn for each node from the respective exponential distributions. The node with the lowest value is chosen as the first seeking node. The node is assigned several random neighbors at the time it is ready to request content. Requests are then forwarded to k randomly selected neighbors. If k exceeds the number of neighbors then these neighbors forward the request to their randomly assigned neighbors until k unique nodes are queried. If none of the requests reach a seed, the status of the seeking node is unchanged and the time before the node’s next attempt to locate the content is drawn. If the queried node is a seed, the status of the querying node is changed to a satisfied node. This newly satisfied node will be a seed if it is altruistic or if its cost of distributing content is less than the referral. Next, the node with the lowest time to a request is selected. The process repeats until all nodes are satisfied or the time reaches an upper threshold. The simulation is repeated 100 times with the same parameters, and the average value of $q$ is recorded as the simulation result. The simulation for the hierarchical network is similar except that nodes are organized into groups and requests are always handled by supernodes.

The predicted diffusion curve and the curve observed in the simulations (averaged over 100 runs) for a flat P2P network are plotted in Figure 10. The parameter configuration is $N = 1 0 , 0 0 0 , Q ( 0 ) = 1$ C = 1,  = 01,  = 05, k = 8, and $r = 0 . 2$ . The mean field model reasonably approximates the mean diffusion curve. Figure 11 indicates that the model fits the simulations for a hierarchical P2P network as

Figure 10 Simulation Result for Flat P2P with Multiple Requests  
![](/api/attachments/XBFY4PCY/fulltext/images/2d78443d172175cc809f167a1f6b8e6482480f2e28af60ac9304e18098c16653.jpg)

Figure 11 Simulation Result for Hierarchical P2P Network  
![](/api/attachments/XBFY4PCY/fulltext/images/f9a9a335a88514e911ea658ccfe7f49d87c70228566be27709cbb8c055352a96.jpg)  
well. The parameter settings are $N = 1 0 , 0 0 0 , M = 1 0 0 ,$ C 1,  01,  1, and $r = 0 . 0 0 1$

4. Conclusions and Future Directions With the increasing use of P2P networks for distribution of digital products, modeling P2P product diffusion is of considerable interest. However, P2P diffusion demonstrates several unique characteristics not captured by traditional models. For example, generated demand is often not fulfilled immediately because of the decentralized distribution in P2P coupled with the incomplete search and free-riding by nodes. P2P media distributors are often most interested in understanding and designing these P2Pspecific attributes such as P2P search architecture or use of distribution referrals to encourage file sharing. We developed models to capture the influence of the decentralized supply on product diffusion in P2P networks and demonstrated its application in determining optimal distribution referrals. Simulations suggest that the models are robust to heterogeneity across nodes and stochasticity in the request process.

There exist a number of interesting avenues for future work. On the modeling front, we develop a mixing model and do not model detailed spatial structure in a P2P network. An interesting direction to pursue is that of modeling network topology and the entry and exit of nodes in the network. The network models of Andersson (1998), Durrett (1999), Eubank et al. (2004), and Ganesh et al. (2005) are highly applicable in this regard. Models that incorporate network structure can sometimes generate novel insights on the diffusion process (e.g., see Durrett 1999). Given the spatial structure, it is interesting to ask what types of network topologies and search strategies are effective in locating seeds in the network. In this context, recent work on decentralized search in complex networks is relevant (Kleinberg 2006, Liben-Nowell et al. 2005). Vega-Redondo (2007) provides an excellent overview of the topic.

We assumed a monopoly setup in which unfulfilled demand returns in a future period. In reality, unfulfilled demand might be permanently lost to a competitor, especially in the presence of a centralized media distributor such as iTunes. In addition, we assumed that the referral does not impact the demand process itself whereas it can impact the timing of purchases when participants are forward-looking. Modeling the loss of sales to competitors and the impact of distribution referrals on the demand process are likely to be particularly relevant to practice.

An interesting direction for future study would be in applying the models to address managerial questions tied to P2P media distribution. For example, how do prior results on optimal dynamic pricing, promotion, timing of product release, etc., change under decentralized product supply in P2P? How should a firm “seed” a new product, i.e., use free samples to support the distribution of a product whose availability is limited early in its diffusion? Similarly, a more detailed investigation of dynamic referral policies can be particularly useful for P2P managers. We are currently investigating this issue in ongoing work (Hosanagar et al. 2008). It would also be interesting to incorporate congestion costs to determine the optimal number of nodes to query in a decentralized network. Finally, a highly valuable extension would be the estimation of diffusion parameters using data from real P2P networks. Although it is ideal to estimate diffusion parameters from the closed-form solutions of diffusion equations, it might be necessary in our case to estimate parameters using discrete-time difference equations because of the complexity of the P2P diffusion models. Mahajan et al. (2000) provide an excellent overview of maximum likelihood estimation (MLE) and nonlinear least squares (NLS) based estimation techniques for diffusion models.

All of the above comments suggest that there are a number of open problems and further study on P2P product diffusion modeling can prove useful. Our research is only a first step in this direction.

## Acknowledgments

The authors thank Sumit Sarkar, an associate editor, and two anonymous referees for their valuable feedback. All errors remain our own.

## Appendix A. Diffusion in Flat P2P Network

Proposition 1. The product penetration qt  at a given time instant $t _ { c }$ increases with k in a convex fashion early in the file’s diffusion (small q) and in a concave fashion late in the diffusion (large q). The time $t ( q _ { c } )$ to achieve a given level of product penetration $q _ { c }$ decreases with k in a convex fashion.

<sup>Proof.</sup> Suppose we fix $t = t _ { c } .$ Given the number of requests forwarded (k), let the value of q at this instant be denoted $q = q ( k )$ . The diffusion equation can be rewritten as $\begin{array} { r } { \int _ { q _ { 0 } } ^ { q ( k ) } \bigl ( \dot { d x } / ( ( \dot { 1 } - x ) ( 1 - ( 1 - \phi x ) ^ { k } ) ) \bigr ) \dot { = } \beta t _ { c } } \end{array}$ . Now suppose we instead had k 1 requests forwarded, then

$$
\int_ {q _ {0}} ^ {q (k + 1)} \left(\frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1})}\right) = \beta t _ {c}.
$$

Therefore,

$$
\begin{array}{l} \int_ {q _ {0}} ^ {q (k)} \bigg (\frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})} \bigg) \\ \qquad - \int_ {q _ {0}} ^ {q (k + 1)} \bigg (\frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1})} = 0. \end{array}
$$

Rewriting it,

$$
\begin{array}{l} \int_ {q (k)} ^ {q (k + 1)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})} \\ = \int_ {q _ {0}} ^ {q (k + 1)} \frac {(1 - \phi x) ^ {k} \phi x d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1}) (1 - (1 - \phi x) ^ {k})}. \end{array}\tag{A1}
$$

Because the second term is greater than zero, we can conclude that $q ( k + 1 ) > q ( k )$ . Thus, an increase in the number of nodes queried serves to increase the product penetration.

Now let us evaluate the nature of the increasing relationship. Just as with (A1), we can derive

$$
\begin{array}{l} \int_ {q (k - 1)} ^ {q (k)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})} \\ = \int_ {q _ {0}} ^ {q (k - 1)} \frac {(1 - \phi x) ^ {k - 1} \phi x d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) (1 - (1 - \phi x) ^ {k - 1})}. \end{array}\tag{A2}
$$

Taking the difference between (A1) and (A2), we have

$$
\begin{array}{l} \int_ {q (k)} ^ {q (k + 1)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})} - \int_ {q (k - 1)} ^ {q (k)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})} \\ = \int_ {q (k - 1)} ^ {q (k + 1)} \frac {(1 - \phi x) ^ {k} \phi x d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1}) (1 - (1 - \phi x) ^ {k})} \\ + \int_ {q _ {0}} ^ {q (k - 1)} \frac {(1 - \phi x) ^ {k - 1} (\phi x) ^ {2} d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1}) (1 - (1 - \phi x) ^ {k - 1})} > 0. \end{array}
$$

Therefore,

$$
\begin{array}{l} \int_ {q (k)} ^ {q (k + 1)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})} \\ > \int_ {q (k - 1)} ^ {q (k)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k})}. \end{array}\tag{A3}
$$

The relationship between $q ( k + 1 ) , \ q ( k )$ , and $q ( k - 1 )$ depends on the function $\psi _ { k } ( q ) ~ = ~ \int _ { a } ( d x / ( ( 1 ~ - ~ x ) ( 1 ~ -$ $( 1 - \phi x ) ^ { k } ) )$ , which is increasing in $q . \mathrm { ~ I f ~ } \psi _ { k } ( q )$ is concave, then for inequality (A3) to hold, we require that $q ( k + 1 ) +$ $q ( k - 1 ) - 2 \bar { q ( k ) } > \bar { 0 }$ . That is, we require $q ( k )$ to be convex. The second derivative of $\psi _ { k } ( q )$ is negative when q is small. Thus, qk is convex with k for small q.

To prove that $q ( k )$ is concave for large q, we rewrite (A1) and (A2) as

$$
\begin{array}{l} \int_ {q (k)} ^ {q (k + 1)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1})} \\ = \int_ {q _ {0}} ^ {q (k)} \frac {(1 - \phi x) ^ {k} \phi x d x}{(1 - x) (1 - (1 - \phi x) ^ {k + 1}) (1 - (1 - \phi x) ^ {k})}; \\ \int_ {q (k - 1)} ^ {q (k)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k - 1})} \\ = \int_ {q _ {0}} ^ {q (k)} \frac {(1 - \phi x) ^ {k - 1} \phi x d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) (1 - (1 - \phi x) ^ {k - 1})}. \end{array}
$$

Taking the difference between the above two expressions, just as we did with (A1) and (A2) to get (A3),

$$
\begin{array}{l} \int_ {q (k)} ^ {q (k + 1)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k - 1})} \\ <   \int_ {q (k - 1)} ^ {q (k)} \frac {d x}{(1 - x) (1 - (1 - \phi x) ^ {k - 1})}. \end{array}\tag{A4}
$$

Similarly, $\begin{array} { r } { \psi _ { k - 1 } ( q ) = \int _ { a } { ( d x / ( ( 1 - x ) ( 1 - ( 1 - \phi x ) ^ { k - 1 } ) ) ) } } \end{array}$ is increasing in q. If $\psi _ { k - 1 } ( q )$ is convex, we require $q ( k + 1 ) +$ $q ( k - 1 ) - 2 q ( k ) < 0$ to make inequality (A4) hold. That is, we require qk to be concave. The second derivative of $\psi _ { k - 1 } ( q )$ is positive for large q. It thus follows that $q ( k )$ is concave with k for large q.

Now, let us evaluate the impact of k on the time to achieve a given level of product penetration. Suppose we fix $q = q _ { c }$ . Denote the time taken to achieve this level of product penetration by tk. Then,

$$
\begin{array}{l} t (k + 1) - t (k) \\ = - \frac {1}{\beta} \int_ {q _ {0}} ^ {q _ {c}} \frac {\phi x (1 - \phi x) ^ {k} d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) (1 - (1 - \phi x) ^ {k + 1})} <   0. \end{array}
$$

The second difference is:

$$
\begin{array}{l} t (k + 1) + t (k - 1) - 2 t (k) \\ = \frac {1}{\beta} \int_ {q _ {0}} ^ {q _ {c}} \frac {(\phi x) ^ {2} (1 - \phi x) ^ {k - 1} (1 + (1 - \phi x) ^ {k}) d x}{(1 - x) (1 - (1 - \phi x) ^ {k - 1}) (1 - (1 - \phi x) ^ {k}) (1 - (1 - \phi x) ^ {k + 1})} > 0. \end{array}
$$

Proposition 2. The product penetration $q ( t _ { c } )$ at a given time instant $t _ { c }$ increases with the referral r. Simultaneously, the time $t ( q _ { c } )$ to achieve a given level of product penetration $q _ { c }$ decreases with r in a convex fashion.

<sup>Proof.</sup> Recollect that $\begin{array} { r } { \int _ { q _ { 0 } } ^ { q } \big ( d x / ( ( 1 - x ) ( 1 - ( 1 - \phi x ) ^ { k } ) ) \big ) = \beta t } \end{array}$ Suppose we fix $t = t _ { c }$ <sup>0</sup> . We examine how $q$ varies with respect to $r ,$ we have

or

$$
\begin{array}{l} \frac {d q}{d r} \frac {1}{(1 - q) (1 - (1 - \phi q) ^ {k})} - \frac {k (1 - \alpha)}{C} \\ \cdot \int_ {q _ {0}} ^ {q} \frac {x (1 - \phi x) ^ {k - 1} d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) ^ {2}} = 0, \end{array}
$$

$$
\begin{array}{l} \frac {d q}{d r} = (1 - q) (1 - (1 - \phi q) ^ {k}) \frac {k (1 - \alpha)}{C} \\ \cdot \int_ {q _ {0}} ^ {q} \frac {x (1 - \phi x) ^ {k - 1} d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) ^ {2}} > 0. \end{array}
$$

Now, let us evaluate the impact of r on the time to achieve a given level of product penetration. Suppose we fix $q = q _ { c }$ . Taking the derivative of t with respect to $r ,$ we get

$$
\frac {d t}{d r} = - \frac {k (1 - \alpha)}{\beta C} \int_ {q _ {0}} ^ {q _ {c}} \frac {x (1 - \phi x) ^ {k - 1} d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) ^ {2}} <   0, \quad \text { and }
$$

$$
\begin{array}{l} \frac {d ^ {2} t}{d r ^ {2}} = \frac {k (1 - \alpha) ^ {2}}{\beta C ^ {2}} \\ \cdot \int_ {q _ {0}} ^ {q _ {c}} \frac {x ^ {2} (1 - \phi x) ^ {k - 2} (k - 1 + (k + 1) (1 - \phi x) ^ {k}) d x}{(1 - x) (1 - (1 - \phi x) ^ {k}) ^ {3}} > 0. \end{array}
$$

Proposition 3. The optimal referral for the flat P2P network with diffusion specified by (5) is

$$
\begin{array}{c} r ^ {*} = \max \bigg [ 0, \min \bigg [ C, 1 - \frac {C}{\beta T (1 - \alpha)} \bigg (1 + W \bigg (\frac {1}{N - 1} \\ \cdot \exp \left(\beta T \Big (\alpha + \frac {1 - \alpha}{C} \Big) - 1\right) \bigg) \bigg) \bigg ] \bigg ], \end{array}
$$

where $W ( x )$ is the Lambert W -function (solution of $W ( x )$ exp $( W ( x ) ) = x )$

<sup>Proof.</sup> Setting the first-order condition specified in (8) equal to zero, we get $( N - 1 ) \exp ( - \beta T ( \alpha + ( 1 - \alpha ) ( r / C ) ) )$ $( \bar { \beta } T ( 1 - \alpha ) ( ( 1 - r ) / \bar { C } ) - 1 ) = 1$ . Rearranging this condition, we have

$$
\begin{array}{l} \left(\frac {(1 - r) \beta T (1 - \alpha)}{C} - 1\right) \exp \left(\frac {(1 - r) \beta T (1 - \alpha)}{C} - 1\right) \\ = \frac {1}{N - 1} \exp \left(\beta T \left(\alpha + \frac {1 - \alpha}{C}\right) - 1\right). \end{array}
$$

This equation is of the form $W ( x ) \exp ( W ( x ) ) = x ,$ where

$$
\begin{array}{l} W \bigg (\frac {1}{N - 1} \exp \bigg (\beta T \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) - 1 \bigg) \bigg) \\ = \frac {(1 - r) \beta T (1 - \alpha)}{C} - 1. \end{array}\tag{A5}
$$

Given the Lambert W -function $W ( ) .$ , the solution to (21) is

$$
r ^ {*} = 1 - \frac {C}{\beta T (1 - \alpha)} \left(1 + W \left(\frac {1}{N - 1} \exp \left(\beta T \left(\alpha + \frac {1 - \alpha}{C}\right) - 1\right)\right)\right).
$$

The second derivative at $r = r ^ { * }$ is

$$
\begin{array}{l} - (N - 1) \exp \left(- \beta T \left(\alpha + \frac {1 - \alpha}{C} r ^ {*}\right)\right) (1 - r ^ {*}) \\ \cdot \left(\beta T \frac {1 - \alpha}{C}\right) ^ {2} \Bigg / \left(1 + (N - 1) \exp \left(- \beta T \left(\alpha + \frac {1 - \alpha}{C} r ^ {*}\right)\right)\right) ^ {2} <   0, \end{array}
$$

because $r ^ { * } < 1 ,$ . Therefore, the function is locally concave and $r ^ { * }$ is a local maximum. However, the objective function is convex for small r and concave for large r. We can nonetheless show that the objective function is unimodal, hence, $r = r ^ { * }$ is a global maximum. To see this, consider the first derivative with respect to $r .$ The denominator is positive, so the sign is determined by the numerator:

$$
\begin{array}{l} Z (r) = - 1 + (N - 1) \\ \qquad \cdot \exp \bigg (- \beta T \bigg (\alpha + \frac {1 - \alpha}{C} r \bigg) \bigg) \bigg ((1 - r) \beta T \frac {1 - \alpha}{C} - 1 \bigg). \end{array}
$$

Suppose that $Z ( 0 ) > 0 .$ . This is the condition under which a nonzero optimal r exists. Then

$$
\begin{array}{l} Z ^ {\prime} (r) = - (N - 1) \\ \qquad \cdot \exp \bigg (- \beta T \bigg (\alpha + \frac {1 - \alpha}{C} r \bigg) \bigg) (1 - r) \bigg (\beta T \frac {1 - \alpha}{C} \bigg) ^ {2}, \end{array}
$$

which is negative if $r < 1$ and positive if $r > 1 .$ . Therefore $Z ( r )$ , starting from a positive value at $r = 0 ,$ , decreases with $r ,$ crosses 0 at $r = r ^ { * } < 1 .$ , and eventually increases with r for $r > 1$ . However, for $r > 1 , Z ( r ) < 0 . 5 0 , Z ( r ) \geq 0 { \mathrm { ~ i f } }$ $r \leq r ^ { * }$ , and $Z ( r ) < 0 { \mathrm { ~ i f ~ } } r > r ^ { * }$ . This shows that the objective function is unimodal

Proposition 4. The optimal referral is (a) nonincreasing with the fraction of nodes in the network that are altruistic (), (b) nondecreasing with the P2P network’s size $( N ) ,$ , and (c) nondecreasing with request rate $\beta$ for $\beta < \beta _ { t h } ,$ , and nonincreasing with $\beta$ for $\beta > \beta _ { t h } ,$ where

$$
\begin{array}{l} \beta_ {t h} = \frac {1}{T} \bigg (2 + W ((N - 1) e ^ {- 1}) + \frac {e}{N - 1} \\ \qquad \cdot \exp (W ((N - 1) e ^ {- 1})) \bigg) \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) ^ {- 1}. \end{array}
$$

Proof.

$$
\begin{array}{l} \text {(a) From (8), we have \beta T(1 - \alpha)((1- r)/C)- 1 = 1/} \\ ((N - 1) \exp (- \beta T (\alpha + (1 - \alpha) r / C))) > 0. \text { Thus, \beta T(1 - \alpha) .} \end{array}
$$

$( 1 - r ^ { * } ) / C > 1$ . It then follows that $1 - r ^ { * } > 0$ . We will use this result below.

$$
\begin{array}{l} \frac {\partial r ^ {*}}{\partial \alpha} = - \frac {C}{\beta T (1 - \alpha) ^ {2}} \bigg (1 + W \bigg (\frac {1}{N - 1} \exp \bigg (\beta T \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) - 1 \bigg) \bigg) \bigg) \\ \qquad - \frac {C}{\beta T (1 - \alpha)} W ^ {\prime} \bigg (\frac {1}{N - 1} \exp \bigg (\beta T \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) - 1 \bigg) \bigg) \\ \qquad \cdot \frac {\beta T (1 - 1 / C)}{N - 1} \exp \bigg (\beta T \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) - 1 \bigg). \end{array}
$$

Using (8) and the equation $W ^ { \prime } ( x ) = W ( x ) / ( ( 1 + W ( x ) ) x )$ , we can rewrite the above expression:

$$
\begin{array}{l} \frac {\partial r ^ {*}}{\partial \alpha} = - \frac {C}{1 - \alpha} \bigg (\frac {1 - r ^ {*}}{C} + 1 - \frac {1}{C} - \frac {C (1 - 1 / C)}{\beta T (1 - r ^ {*}) (1 - \alpha)} \bigg) \\ <   - \frac {C}{1 - \alpha} \bigg (\frac {1 - r ^ {*}}{C} + 1 - \frac {1}{C} - 1 + \frac {1}{C} \bigg) = - \frac {1 - r ^ {*}}{1 - \alpha} <   0. \end{array}
$$

(b) W is an increasing function of N . Because $r ^ { * }$ is increasing in $W ,$ it follows that $r ^ { * }$ increases with N .

(c) We have

$$
\begin{array}{c} \frac {\partial r ^ {*}}{\partial (\beta T)} = \frac {C}{(\beta T) ^ {2} (1 - \alpha)} (1 + w) - \frac {C}{\beta T (1 - \alpha)} w ^ {\prime} \frac {1}{N - 1} \\ \cdot \exp \left(\beta T \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) - 1\right) \bigg (\alpha + \frac {1 - \alpha}{C} \bigg), \end{array}
$$

where $w = W ( ( 1 / ( N - 1 ) ) \exp ( \beta T ( \alpha + ( 1 - \alpha ) / C ) - 1 ) )$ and $w ^ { \prime } = d W ( x ) / d x$ . We apply the following two properties of the Lambert-W function:

$$
w e ^ {w} = \frac {1}{N - 1} \exp \left(\beta T \left(\alpha + \frac {1 - \alpha}{C}\right) - 1\right),\tag{A6}
$$

and $( 1 + w ) e ^ { w } w ^ { \prime } = 1$ . Using these properties, the derivative can be rewritten as follows:

$$
\frac {\partial r ^ {*}}{\partial (\beta T)} = \frac {C}{(\beta T) ^ {2} (1 - \alpha)} (1 + w) - \frac {C}{\beta T (1 - \alpha)} \frac {w}{1 + w} \left(\alpha + \frac {1 - \alpha}{C}\right).
$$

Hence, the sign of the above expression is determined by the expression

$$
(1 + w) ^ {2} - w \left(\beta T \left(\alpha + \frac {1 - \alpha}{C}\right)\right).\tag{A7}
$$

Using (A6), (A7) can be rewritten as $1 + w - w \ln ( ( N - 1 ) w ) .$ which is positive for small w and negative for $w > w _ { t h } ,$ where $\tilde { w _ { t h } } \bar { = } ( e / ( N - 1 ) ) \exp ( W ( ( N - 1 ) e ^ { - 1 } ) )$ . It follows that $r ^ { * }$ increases when $\beta < \beta _ { t h }$ and decreases for $\beta > \beta _ { t h } ,$ where

$$
\begin{array}{l} \beta_ {t h} = \frac {1}{T} \bigg (2 + W ((N - 1) e ^ {- 1}) + \frac {e}{N - 1} \\ \qquad \cdot \exp (W ((N - 1) e ^ {- 1})) \bigg) \bigg (\alpha + \frac {1 - \alpha}{C} \bigg) ^ {- 1}. \end{array}
$$

Imposing $r \in [ 0 , C ] ,$ , it follows that $r ^ { * }$ is nondecreasing for $\beta < \beta _ { t h }$ and nonincreasing for $\beta > \beta _ { t h }$

## References

Adar, E., B. A. Huberman. 2000. Free riding on Gnutella. First Monday: Peer-Reviewed J. Internet 5–10. http://www. firstmonday.dk/issues/issue5\_10/adar/index. html.

Andersson, H. 1998. Limit theorems for a random graph epidemic model. Ann. Appl. Probab. 8(4) 1331–1349.

Andersson, H., T. Britton. 2000. Lecture Notes in Statistics: Stochastic Epidemic Models and Their Statistical Analysis. Springer-Verlag, New York.

Arora, G., M. Hanneghan, M. Merabti. 2005. P2P commercial digital content exchange. Electronic Commerce Res. Appl. 4(3) 250–263.

Asvanund, A., K. Clay, R. Krishnan, M. Smith. 2004. An empirical analysis of network externalities in peer-to-peer music sharing networks. Inform. System Res. 15(2) 155–174.

Bass, F. 1969. A new product growth model for consumer durables. Management Sci. 15(5) 215–227.

Bass, F. 1980. The relationship between diffusion rates, experience curves, and demand elasticities for consumer durable technological innovations. J. Bus. 53(July) 551–567.

Brauer, F., Castillo-Chavez. 2001. Mathematical Models in Population Biology and Epidemiology. Springer, New York.

Currah, A. 2004. The digital storm: The strategic challenge of Internet distribution to the Hollywood studio system. Executive Report, University of Oxford, Oxford, UK.

Diekmann, O., J. A. P. Heesterbeek. 2000. Mathematical Epidemiology of Infectious Diseases: Model Building, Analysis and Interpretation. Mathematical and Computational Biology. Wiley, New York.

Durrett, R. 1999. Stochastic spatial models. SIAM Rev. 41(4) 677–718.

Eubank, S., H. Guclu, V. S. Anil Kumar, M. Marathe, A. Srinivasan, Z. Toroczkai, N. Wang. 2004. Modeling disease outbreaks in realistic urban social networks. Nature 429(6988) 180–184.

Fourt, L. A., J. W. Woodlock. 1960. Early prediction of market success for grocery products. J. Marketing 25 31–38.

Ganesh, A., L. Massoulie, D. Towsley. 2005. The effect of network topology on the spread of epidemics. Proc. 2005 Infocom, Institute of Electrical and Electronics Engineers, Miami, 1455–1466.

Garces-Erice, L., E. Biersack, K. Ross, P. Felber, G. Urvoy-Keller. 2003. Hierarchical peer-to-peer systems. Parallel Processing Lett. 13(4) 643–657.

Golle, P., K. Leyton-Brown, I. Mironov, M. Lillibridge. 2001. Incentives for sharing in peer-to-peer networks. Proc. 3rd ACM Conf. Electronic Commerce, ACM, Tampa, FL.

Ho, T., S. Savin, C. Terwiesch. 2002. Managing demand and sales dynamics in constrained new product diffusion under supply constraint. Management Sci. 48(2) 187–206.

Hosanagar, K., P. Han, Y. Tan. 2008. Optimal dynamic referrals in P2P networks. Working paper, University of Pennsylvania, Philadelphia.

Horsky, D., L. S. Simon. 1983. Advertising and the diffusion of new products. Marketing Sci. 2(1) 1–17.

Iamnitchi, A., M. Ripeanu, I. Foster. 2004. Small-world filesharing communities. Proc. 23rd Annual Joint Conf. IEEE Comput. Comm. Soc., Hong Kong, 7–11.

Izal, M., G. Urvoy-Keller, E. W. Biersack, P. A. Felber, A. Al Hamra, L. Garc’es-Erice. 2004. Dissecting BitTorrent: Five months in a torrent’s lifetime. Proc. Passive Active Measurement Workshop, Antibes Juan-les-Pins, France

Jain, D., V. Mahajan, E. Muller. 1991. Innovation diffusion in presence of supply restrictions. Marketing Sci. 10(1) 100–113.

Kamvar, S. D., M. T. Schlosser, H. Garcia-Molina. 2003. Incentives for combatting freeriding on P2P networks. Lecture Notes Comput. Sci., Vol. 2790, Euro-Par 2003 Parallel Processing. Springer, Berlin/Heidelberg.

Kephart, J. O., S. R. White. 1991. Directed-graph epidemiological models of computer viruses. IEEE Comput. Soc. Sympos. Res. Security Privacy, Oakland, CA, 343–359.

Khelil, A., C. Becker, J. Tian, K. Rothermel. 2002. An epidemic model for information diffusion in MANETs. Proc. Fifth ACM Internat. Workshop Model., Anal. Simulation Wireless Mobile Systems, ACM, New York, 54–60.

Kleinberg, J. 2006. Complex networks and decentralized search algorithms. Proc. Internat. Congress of Mathematicians, Association of the International Congress of Mathematicians, Madrid, Spain.

Krishnan, T. V., F. M. Bass, V. Kumar. 2000. Impact of a late entrant on the diffusion of a new product/service. J. Marketing Res. 37(May) 269–278.

Kumar, S., J. Swaminathan. 2003. Diffusion of innovations under supply constraints. Oper. Res. 51(6) 866–879.

Lang, K., R. Vragov. 2005. A pricing mechanism for digital content distribution over peer-to-peer networks. J. Management Inform. Systems 22(2) 121–139.

Liben-Nowell, D., J. Novak, R. Kumar, P. Raghavan, A. Tomkins. 2005. Geographic routing in social networks. Proc. National Acad. Sci. USA 102(33) 11623–11628.

Mahajan, V., E. Muller, Y. Wind. 2000. New-Product Diffusion Models. IEEE, Springer-Science and Business Media, New York.

Newman, M. E. J., C. Moore, D. J. Watts. 2000. Mean-field solution of the small-world network model. Physical Rev. Lett. 84(14) 3201–3204.

New York Times. 2003. E-Commerce Report: Incentive marketing spreads on the Internet, with offers of discounts or credit toward gifts. (June 9).

Opper, M., D. Saad. 2001. Advanced Mean Field Methods—Theory and Practice. MIT Press, Cambridge.

Padmanabhan, V. N., K. Sripanidkulchai. 2002. The case for cooperative networking. P. Druschel, M. F. Kaashoek, A. I. T. Rowstron, eds. Proc. First Internat. Workshop on Peer-to-Peer Systems, Springer, Cambridge, MA, 178–190.

Ross, K. W., D. Rubenstein. 2003. Tutorial on P2P systems. Proc. 22nd Ann. Joint Conf. Comput. Comm. Societies, IEEE, Washington, DC.

TECHCRUNCH. 2007. P2P music sharing service Grooveshark ups compensation.

Vega-Redondo, F. 2007. Complex Social Networks. Cambridge University Press, Cambridge, UK.
