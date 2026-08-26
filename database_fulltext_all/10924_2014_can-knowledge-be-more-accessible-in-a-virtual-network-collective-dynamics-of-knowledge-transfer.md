---
otero_id: 10924
otero_key: "YANVHG9M"
title: "Can knowledge be more accessible in a virtual network?: Collective dynamics of knowledge transfer in a virtual knowledge organization network"
authors: "Seung Kyoon Shin; Woong Kook"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.11.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can knowledge be more accessible in a virtual network?: Collective dynamics of knowledge transfer in a virtual knowledge organization network

![](/api/attachments/YANVHG9M/fulltext/images/6f8ddda5e3e37e4c9fbc3c2a1f3072308d9fe5f0c275a5d658b4b925c1adec6b.jpg)

Seung Kyoon Shin <sup>a,1</sup>, Woong Kook <sup>b,</sup>⁎

<sup>a</sup> College of Business Administration, University of Rhode Island, 7 Lippitt Road, Kingston, RI 02881-0802, United States

<sup>b</sup> Department of Mathematical Sciences, Seoul National University, Seoul 151-747, Korea

## a r t i c l e i n f o

Article history: Received 26 December 2012 Received in revised form 14 November 2013 Accepted 18 November 2013 Available online 11 December 2013

Keywords: Virtual community Knowledge network Knowledge transfer Network complexity Centrality

## a b s t r a c t

Virtual knowledge organizations (VKOs) produce and embrace priceless, and often, unique knowledge assets within the boundary of each virtual community. An important question is how do we maximize the bene<sup>fi</sup>ts from these valuable assets at the entire VKO network level? Relying on the graph theory, this study is to investigate how the structure of virtual knowledge networks formed by knowledge agents and knowledge pro<sup>fi</sup>le of each VKO in<sup>fl</sup>uence the dynamics of knowledge transfer in a virtual knowledge organization network (VKON). We develop a network model through which knowledge will be ef<sup>fi</sup>ciently disseminated when knowledge agents are uniformly distributed across the network. Using this model's intrinsic capability to assess global effects of local transformations in a network, we found that VKON complexity, a measure for ef<sup>fi</sup>ciency of knowledge transfer, is optimized when a new knowledge agent is placed between two communities with the minimum knowledge transfer capacity. The results of this study will help understand the inter-community knowledge transfer dynamics in virtual knowledge community networks.

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

As business becomes knowledge dependent, organizational productivity often relies upon in-depth knowledge of business processes, technologies, and transfer knowledge across the organizational boundary [68]. Because organizations may not always have all necessary knowledge within their organizational boundaries, many have implemented inter-organizational knowledge networks as a mechanism to obtain knowledge [35,46]. Virtual knowledge organizations (VKOs) provide an ef<sup>fi</sup>cient mechanism to search for and access knowledge in needs and facilitate the knowledge transfer process [33,43].

A VKO can be viewed as a virtual organization in which knowledge users co-create and share knowledge [39,44]. An important feature of VKOs is to bring knowledge seekers and providers into one virtual space that is equipped with knowledge databases over networks. Being free from the constraints of hierarchy and rules of real-world organizations, people bene<sup>fi</sup>t from this virtual organization by gaining access to new knowledge, expertise, and ideas, all of which may not be available within the organizational boundary [77]. Our notion of VKO focuses on a knowledge-centric virtual community where a group of knowledge workers with common topics, interests, problems, experiences and practices co-create and share valuable knowledge. A unique characteristic of VKOs, which differentiates them from real-world organizations, is that knowledge processed through VKOs becomes explicit in the way of knowledge digitalization, and turns into common assets bene<sup>fi</sup>ting all participating groups [40].

This paper develops on the network and organizational perspective, which de<sup>fi</sup>nes VKO network (VKON) as networked organizations transmitting knowledge through the network. A VKON can be viewed as a market mechanism that provides knowledge resources to problems and solutions in a decentralized manner [31]. An example of VKON is “Network of Networks (N2)” (http://n2canada.ca/), a Canadian national initiative that integrates 29 existing virtual organizations to enhance Canada's disease research capability and capacity.<sup>2</sup> The Network of Networks (N2) was initiated because researchers from diverse knowledge domains confront challenges in carrying out a joint research project that requires integrating knowledge from foreign domain. They need a networked system establishing a common knowledge base and integrating knowledge from various <sup>fi</sup>elds. In N2, a number of members who join multiple VKOs play the role of knowledge agents transferring and distributing knowledge across domains. Similarly, in an effort to facilitate knowledge creation process between academia and industry, European academic and business organizations from nine nations designed a VKON, European Corporate Academies Transnational Best Practice Network (ECUANET).

During the last two decades, many of research and development organizations that engaged in innovative tasks have begun a rapid transformation toward using virtual organization networks [39]. They, however, have learned that acquiring knowledge from external sources is not a simple task, and that there are challenges in making newly acquired knowledge useful. While the evolution of individual VKOs leads to knowledge specialization by developing local knowledge and coding schemes, it also hinders the acquisition and interpretation of knowledge transferred from other VKOs [20]. In addition, developing an effective channel to transmit knowledge kept in one VKO to another is not an easy task. Then, how can we create a VKO network that would effectively facilitate the knowledge transfer process among VKOs?

We suggest two ef<sup>fi</sup>cient mechanisms to cope with the challenges of cross-VKO knowledge transfer; acquiring inter-VKO common knowledge, and forming the network based on knowledge transfer agents (knowledge agents hereafter). The current study addresses two important questions; how do we ef<sup>fi</sup>ciently distribute and acquire necessary knowledge across the network? and how do we maximize the collateral bene<sup>fi</sup>ts from the valuable knowledge through the entire VKON? Using a mathematical modeling approach, this study attempts to answer these questions based upon the theories of common knowledge and knowledge agent. We posit that the common knowledge between VKOs and the topological properties of a VKON characterized by distribution of knowledge agents are associated with superior knowledge transfer capacity.

The capacity of knowledge network is measured by network complexity, which is a generalization of the number of spanning trees in a graph. This notion of network ef<sup>fi</sup>ciency has been well addressed in the quanti<sup>fi</sup>cation of <sup>fl</sup>ow of information by Stephenson and Zelen [65]. We view a VKON as an organic social network consisting of two outstanding entities: 1) a group of VKOs in which private and common knowledge are created and 2) cross-VKO knowledge agents connecting two VKOs by involving in and transferring knowledge between the two.<sup>3</sup> We argue that the distribution of the agents is an imperative determinant of knowledge transfer capacity and accessibility of knowledge in a VKON. We investigate how a network structure formed by knowledge agents connecting multiple VKOs along with the knowledge pro<sup>fi</sup>le of each VKO in<sup>fl</sup>uences the dynamics of knowledge transfer in a VKON. Our objective is to assess the effects of a knowledge network structure formed by the distribution of knowledge agents and common knowledge on knowledge transfer.

The strategy of this paper is to examine interactions between two VKOs, and to illustrate how they affect knowledge diffusion, cohesion of knowledge network, and structural issues of the entire knowledge network. Our VKON model seeks to advance an understanding of knowledge transfer in virtual organization networks in two ways. First, while extant research on knowledge transfers tends to focus on sharing activities within the boundary of a VKO, we consider the dynamics of knowledge transfer at a network level. Second, one common assumption of the studies in this area is knowledge transfer based on direct communication. This study further considered knowledge transfer through indirect communication which is a common practice in VKON.

The knowledge transfer capacity of a VKON is measured by network complexity and common knowledge accumulated in each VKO. The mathematical approach in this study has been adopted in various areas including electrical engineering and biomedical sciences where the original motivation was to address the issues of non-social networks.

We next review relevant literature, focusing on the theory of common knowledge and the knowledge agent. We, then, develop a mathematical model of VKON using information centrality in Section 3.

Section 4 shows an optimal condition for knowledge dissemination in a VKON and Section 5 discusses the effect of merging two VKOs on knowledge transfer in the VKON. Section 6 suggests a way to maximize knowledge transfer capacity in a VKON and Section 7 assesses the amount of knowledge transfer between two VKOs through direct and indirect communication channels. Section 8 examines the effects of common knowledge on the dynamics of knowledge transfer in a VKON. Finally, we summarize and discuss the results and conclude with contributions, implications and limitations of this research in Section 9. Detailed mathematical proofs and leads are provided in the Appendix A.

## 2. The role of common knowledge and knowledge agent

A VKON can be viewed as a network that consists of multiple VKOs. Thanks to the frictionless nature of VKOs [9], they pro<sup>fi</sup>ciently operate on relational structures or networks [46]. Recently, researchers have paid attention to various phenomena of VKOs due to their tremendous potential for knowledge creation and transfer [2,3,28,39,77]. Given the importance and potential of knowledge transfer, researchers have investigated various phenomena within the boundary of a VKO. Particularly in research and development organizations, the importance of inter-organizational knowledge transfer has been highlighted due to the emerging need of cross-disciplinary research.

While <sup>fi</sup>rms acquire valuable knowledge assets through network, there are substantial barriers to knowledge transfer between organizations [30,76]. The identi<sup>fi</sup>ed barriers include 1) lack of absorptive capacity of the recipient entities, 2) lack of credibility on the part of the source of knowledge, 3) disconcerted relationships between the sourcing and recipient entities, and 4) causal ambiguity caused by the complexity of knowledge [66,75]. The barriers can be overcome by increasing common knowledge between the source and recipient organizations [12,17] and by acquiring capable knowledge agents [71,78].

## 3. Common knowledge

Knowledge is socially embedded and highly context-speci<sup>fi</sup>c, and these characteristics make it dif<sup>fi</sup>cult to transfer knowledge [8,51]. von Hippel [75] argued that knowledge transfer becomes costly particularly when the recipient organizations need to obtain pre-required knowledge and skills to be able to use the newly acquired knowledge. As a more concrete example, a group of web designers who launch a web development project using web development software will not be aided to a great extent simply by adopting the software program unless they have already obtained the pre-required knowledge related to the web server and the fundamental operating systems. Similarly, the cost of knowledge transfer would be lowered when the software vendor provides training and technical support to the web designers who have common fundamental knowledge. In other words, when both knowledge sourcing and seeking entities share a set of necessary common knowledge, transferring knowledge would be less costly and the transfer process would be more ef<sup>fi</sup>cient. The cost of transfer can be substantially lowered by common knowledge particularly when knowledge transfer takes place in an “explicit” form [50].

Social scientists have been emphasizing the important roles of common knowledge in knowledge transfer [17,28,45,51,70]. It is because common knowledge 1) facilitates the knowledge transfer processes by increasing similarity of knowledge pro<sup>fi</sup>les of the two VKOs, and 2) allows knowledge sourcing and seeking parties to share rules in the form of practices. Zhao and Anand [84] further suggest that the similarity of structural and cultural attributes of the knowledge between the two entities, which becomes an important component of common knowledge, is the vehicle acquiring and assimilating newly transferred knowledge. The depth and breadth of common knowledge, therefore, may indicate the functional and technical expertise integrated across organizational boundaries. This notion of common knowledge has been viewed as a key component of absorptive capacity of knowledge recipients [42,83].

On the contrary, a lack of knowledge commonality can be conceptualized as the impedance of knowledge transfer. The greater the mismatch in knowledge pro<sup>fi</sup>le and cognitive orientations of the two VKOs, the greater the dif<sup>fi</sup>culties of transferring [81]. Transferring knowledge involves high costs and often creates greater ambiguity, particularly when knowledge is being transferred across multiple VKOs that lack common knowledge [27]. An increasing amount of common knowledge facilitates knowledge transfer between VKOs, lends itself to knowledge development, and brings forth a VKON that is more accessible to all VKOs.

Inkpen [34] further emphasized the importance of a common language protocol for knowledge transfer between knowledge sourcing and seeking VKOs. For those who share common communication protocols, terms, and awareness, communication is remarkably ef<sup>fi</sup>cient. Furthermore, a positive effect of network externalities takes place when VKOs in the network increase communality in their views and behaviors to the extent that they <sup>fi</sup>nd proximity to other VKOs in the network [54].

From the perspective of inter-community knowledge transfer, knowledge owned by a VKO can be classi<sup>fi</sup>ed into two types: 1) private knowledge that is exclusively owned by a knowledge sourcing VKO and can be transferred to other VKOs, and 2) common knowledge that is commonly owned by the two interacting communities (Fig. 1). By de<sup>fi</sup>nition, once knowledge is transferred from one VKO to another, transferred knowledge becomes common for the two, and in turn the amount of common knowledge increases. Our goal is to understand the dynamic effects of common knowledge and its facilitating mechanism for knowledge transfer (c.f. Section 8).

## 4. The roles of inter-VKO knowledge agents

Researchers suggest that one way to ef<sup>fi</sup>ciently deal with the costly knowledge transfer process is through knowledge agents who are capable of understanding and translating contrasting knowledge of both knowledge sourcing and seeking VKOs [71,78]. We de<sup>fi</sup>ne Inter-VKO knowledge agents (knowledge agents afterwards) as those who actively engage multiple VKOs and connect them by transferring knowledge. Knowledge agents communicate with knowledge seeking VKO to identify the need of external knowledge, coordinate and align an access to a knowledge source, understand the knowledge from a knowledge sourcing VKO, and localize and disseminate it to a knowledge seeking VKO.

According to Katz and Lazarsfeld's model of “two-step <sup>fl</sup>ow” of communication [37], a small group of knowledge agents act as useful intermediary channels between the source of information and information users. Inkpen [34] emphasized the important role of business managers as the knowledge agents transferring between organizations. Tushman and Katz's early work in R&D identi<sup>fi</sup>ed the organizational bene<sup>fi</sup>ts of having gatekeepers as knowledge agents who gather relevant knowledge from the external environment and enable the <sup>fl</sup>ow of knowledge into the group [71]. Hargadon and Sutton [32] highlighted the role of these knowledge brokers and translators who coordinate the transfer of knowledge through external network. Social researchers called these key individuals stars, de<sup>fi</sup>ned them as the most important actors in a social network [62], and attempted to quantify the effects of their existence in the network by “centrality” [78]. In a similar vein, Cohen and Levinthal [13] viewed the aggregation of the prior relevant knowledge or experiences of the key individuals as an important source of absorptive capacity.

![](/api/attachments/YANVHG9M/fulltext/images/5c2f1c54f7be30a27e212be8f2fe3dc95f1b308134d94248eab9f9319bd2fb9b.jpg)  
Fig. 1. Decomposition of knowledge pro<sup>fi</sup>les: private vs. common knowledge

Knowledge agents in a VKON are important in that they are the links and play the role of transfer channels between VKOs they are associated with, and they are the ones who understand common knowledge of both VKOs. With these knowledge agents, external knowledge can be transferred into a knowledge seeking VKO from a knowledge sourcing one by means of two-step process as shown in Fig. 2: gathering and internalizing knowledge from a knowledge sourcing VKO, and translating and externalizing it in local language of the knowledge seeking VKO [35,49]. Because transferring knowledge requires an understanding of the fundamental knowledge of business processes, culture, or norms of both VKOs, it is critical to have knowledge agents who understand the fundamental common knowledge of both VKOs. Inter-community knowledge transfer without a knowledge agent may lead to misperceptions and an incomplete understanding of the transferred knowledge.

Another important role of these key individuals is formation of knowledge transfer network. In a social network theory, a network structure can be viewed as an arrangement of the network elements that patternize the <sup>fl</sup>ow of communication in a network [47]. Knowledge agents formulate the network structure of a VKON by continuously engaging, acquiring and communicating with multiple VKOs. Because knowledge agents are important channels of knowledge <sup>fl</sup>ow among VKOs, the capacity of knowledge transfer in a network created by knowledge agents becomes a meaningful determinant of knowledge transfer channel between VKOs.

## 5. Modeling virtual knowledge organization network (VKON)

## 5.1. Graph theory

One useful method in analyzing and representing a network is the graph theory. The graph theory has been considered a useful tool in various areas including computer network research (i.e. [25,67]), electrical engineering (i.e. [82]) and medical sciences (i.e. [36]). This connection topology has been adopted in social network analysis for many reasons [23]. One, graph theory offers practical terms and labels representing various properties of a social network structure. For example, we consider a VKON a network that is formed with a group of VKOs connected by agents transferring knowledge among them. In this study, VKOs and knowledge agents are represented by nodes and arcs, respectively. These terms provide us with a set of fundamental tools for analyzing the dynamics created by various network properties. Two, graph theory

![](/api/attachments/YANVHG9M/fulltext/images/d803d4d9dcb14740975e5ea8a998139b889efd493e7902303e66138f6ae6a223.jpg)  
Fig. 2. Decomposition of knowledge transfer.

$C _ { N } .$ : Virtual Knowledge Community N $w _ { i j } .$ Number of Knowledge Agent between $\mathrm { C _ { i } }$ and $\mathrm { C _ { j } }$ offers useful mathematical operations and notions with which social network properties and their effects can be quanti<sup>fi</sup>ed. Finally, the theory allows us to prove theorems regarding network and representations of a social structure. In addition to its mathematical utility, the graph theory offers a vehicle reconceptualizing a VKON as a model of a knowledge transfer system. This model can be viewed as a simpli<sup>fi</sup>ed representation of a VKON characterized by distribution of knowledge agents and common knowledge.

## 5.2. Measuring social network capacity: information centrality

We use Information Centrality in Social Network [78] as the method of analysis of a virtual knowledge organization network (VKON). The term “Centrality” as applied to the entire network relates the compactness of the network as well [22]. A network can be regarded compact when the average length of knowledge transfer paths (in terms of the number of necessary connections) between any two VKOs is short. It is reasonable to assume that knowledge can be transferred more accurately and rapidly, when there are fewer connections involved between two parties.

The score of centrality is determined by the distribution of nodes (or VKOs) and arcs (or knowledge agents). Since the idea of network centrality applied to human communication was originally introduced by Bavelas [5], the concept has been used to examine various phenomena of social networks such as political integration [14], design of organization [6], diffusion of technology innovation [1,16], inter-organization relationships [59], group stability [11], network structure in virtual organizations [2], and individual centrality in virtual groups [3].

Among various measures of centrality, Information Centrality [78] measures the importance of a node (as a hub) in a network. The measure focuses on the <sup>fl</sup>ow of knowledge originating from a VKO, and reveals its in<sup>fl</sup>uence on the whole VKON.

## 5.3. Virtual knowledge organization network (VKON)

A VKON can be viewed as a collection of VKOs which are connected by knowledge agents. Members in each VKO create and share knowledge within the community boundary, developing their own set of knowledge focusing on a domain-speci<sup>fi</sup>c knowledge space. Among members, there are those who acquire and transfer knowledge between two VKOs. A model of a VKON consists of nodes and a set of arcs connecting pairs of nodes, where each node and arc represent a VKO and a knowledge agent connecting two related VKOs respectively. The central idea of VKON is that a VKO takes advantage of autonomy among nodes, but uses arcs (agents) to transmit valuable knowledge between them. Clearly, this form of network precludes the idea of global interaction in the sense that a VKO can interact with selective other [15]. Indeed, VKOs tend to interact only with a relatively circumscribed subset of the entire VKON.

Fig. 3 depicts a simpli<sup>fi</sup>ed example of a VKON. Knowledge can be transferred between two VKOs when there is at least one knowledge agent. The distribution of knowledge agents, therefore, forms the network structure of a VKON. An intuitive notion of the knowledge agent in the context of inter-community knowledge transfer is that the distribution of knowledge agents affects the probability that knowledge can be transferred from one VKO to another. Knowledge transfer wouldn't be enabled without knowledge agents. We investigate the effects of knowledge agents on the dynamics of knowledge transfer in a VKON. The weight<sup>4</sup> assigned to each arc indicates the number of agents assigned to the VKOs. Knowledge agents involve knowledge sourcing and seeking VKOs, and transfer knowledge in two ways. We, therefore, assume that a VKON N is non-directed.

![](/api/attachments/YANVHG9M/fulltext/images/9240d4f3091a326b3eb76498902b4d9ab950fdf20d8b4aab5089e2dba1991f9e.jpg)  
Fig. 3. Simple virtual knowledge organization network (VKON)

## 5.4. Complexity of network

Knowledge becomes more valuable when it is swiftly distributed to and consumed by more knowledge users [26]. The network complexity is a key measurement computing the probability of knowledge <sup>fl</sup>ows from a sourcing VKO to a recipient VKO in a network [19]. From this perspective, network complexity that assesses the degree of knowledge dissemination in a network is a meaningful indicator of knowledge transfer capacity of a network [10,65]. The complexity, c(N), of a VKON N quanti<sup>fi</sup>es the number of possible ways connecting all VKOs without a recursive loop. It is a generalization of the number of spanning trees in a graph and general indicator of cohesiveness of a network, measuring how evenly knowledge agents are dispersed in a network [65]. The implication of network complexity is that the greater c(N) of a VKON is, the more likely knowledge is disseminated throughout the network. When the weights of all arcs in N are constant, c(N) counts the number of possible loop-free spanning trees each of which forms a set of arcs connecting all nodes in the graph (c.f. West [80] for details). That is, we can develop a more ef<sup>fi</sup>cient network using the same number of knowledge agents.

Consider a simple VKON N formed by three VKOs $C _ { 1 } , C _ { 2 } ,$ and $C _ { 3 }$ with knowledge agents connecting them. The connection created by knowledge agents between $C _ { i }$ and $C _ { j }$ will be represented by an arc $\mathbf { e _ { i j } } .$ Let $\boldsymbol { \mathbf { w } } _ { i j }$ denote a weight assigned to ${ \bf e _ { i j } }$ indicating the number of knowledge agents between $C _ { i }$ and $C _ { j } .$ . Then, the complexity of N is de<sup>fi</sup>ned as

$$
c (N) = w _ {1 2} \cdot w _ {2 3} + w _ {2 3} \cdot w _ {3 1} + w _ {3 1} \cdot w _ {1 2}\tag{3.1}
$$

where $\mathbf { w } _ { i j } = \mathbf { w } _ { j i }$ because N is non-directed. $\mathbf { w } _ { i j } = 0$ when there is no agent placed between $C _ { i }$ and $C _ { j } .$ Each term counts different ways connecting all VKOs without looping. For example, the <sup>fi</sup>rst term, $\begin{array} { r } { \mathbf { w } _ { 1 2 } \bullet \mathbf { w } _ { 2 3 } , } \end{array}$ computes the number of possible knowledge transfer paths between $C _ { 1 }$ and $C _ { 3 }$ via $C _ { 2 } ,$ and thus c(N) counts the total number of paths from each and all VKOs to the rest of VKON.<sup>5</sup> If N has n VKOs, there are possible $n ( n - 1 ) / 2$ connections in N. We measure the dynamics of knowledge transfer in a VKON using the Laplacian matrix (also called Kirchhoff matrix) which is a widely adopted mathematical tool for examining various properties of a graph. We de<sup>fi</sup>ne the Laplacian matrix L(N) of the VKON N as a n × n matrix, whose $n ^ { 2 }$ entries are denoted by $L _ { i j } \left( 1 \le i , j \le n \right)$ such that each diagonal entry L equals the sum of the weights of all arcs that are connected to the node $C _ { i }$ and each $L _ { i j } \left( i \neq j \right)$ equals $- \mathbf { w } _ { i j } .$ . Now, let $L _ { 0 } ( N )$ be the $( n - 1 ) \times ( n - 1 )$ matrix obtained by deleting one arbitrary row and one arbitrary column of $L ( N )$ . Then we de<sup>fi</sup>ne c(N) to be the absolute value of the determinant of $L _ { 0 } ( N ) . ^ { 6 }$ When the weights of the arcs in N are non-negative integers and represent the multiplicities of the arcs, c(N) is the number of span ning trees in N [72].

Alternately, c(N) for a weighted VKON can be described as follows. Let T be a spanning tree in N. The complexity c(T) of T is de<sup>fi</sup>ned as the product of all weights in T. Note that c(T) is a square-free monomial of degree $( n - 1 )$ in ${ \bf { w } } _ { i j } { ' } S$ as variables. Then, c(N) is the sum of $c ( T )$ over all spanning trees T:

$$
c (N) = S _ {T \hat {I} \beta (N)} c (T)\tag{3.2}
$$

where β(N) denotes the set of all spanning trees in N. Clearly, c(N) is a square-free homogeneous symmetric polynomial of degree $( n - 1 )$ in $\mathbf { { w } } _ { i j } \mathbf { { s } } . { c } ( N )$ is symmetric in the sense that it remains the same after permutations of nodes.

## 6. Optimizing knowledge transfer capacity of VKON

Communication network literature suggests that short length of communication path leads to an ef<sup>fi</sup>cient information transfer [73,78]. Knowledge dissemination in a VKON mainly depends on the distribution of knowledge agents in the network, which plays a role of communication path. Then, how do we create an ef<sup>fi</sup>cient knowledge transferring network with a certain number of knowledge agents? In this section, we discuss a general guiding principle to optimize c(N) with varying distribution of knowledge agents in a VKON. We obtain the total number of knowledge agents by summing all weights of the arcs.

Theorem 1. If the total weight of N is bounded, network complexity $c ( N )$ will be maximized when the weights are uniformly distributed among all arcs in N. That is, with the constant number of knowledge agents, the degree of knowledge dissemination throughout an entire VKON is maximized when knowledge agents are uniformly dispersed across the network.

Proof. This theorem is a weighted version of the fact that a complete graph has more spanning trees than any other graph of the same size [38]. □

The implication of Theorem 1 is that, assuming that the number of knowledge agents in a VKON remains constant, the network complexity that indicates the degree of knowledge dissemination in a VKON can be maximized by placing knowledge agents evenly throughout the network. This is consistent with the implications of the diffusion literatures that evenly generated networks tend to be more effective [73,79]

## 7. Improving knowledge transfer capacity of VKON(c(N)) by merging two VKOs

Based on Theorem 1, two natural questions are 1) what is the most ef<sup>fi</sup>cient way to achieve uniform distribution of agents (discussed in Section 6)? and 2) among those, which agent would be more important than others in enhancing the degree of knowledge dissemination (discussed in Section $7 ) ?$ In this section, we deploy a two-step approach as a preliminary work leading to answers for the questions. First, we use a measure to assess the capacity of knowledge transfer between two VKOs (C and $C _ { j } ) , I _ { i j } ,$ from the notion of knowledge centrality suggested by the seminal work of Stephenson and Zelen $[ 6 5 ] . ^ { 7 }$ Knowledge centrality is mathematically de<sup>fi</sup>ned as

$$
I _ {i j} = \left(c _ {i i} + c _ {j j} - 2 \cdot c _ {i j}\right) ^ {- 1}\tag{5.1}
$$

where $c _ { i j }$ denotes ij entry in $( J + L ( N ) ) ^ { - 1 }$ and J is an n × n matrix with all entries equal to $1 . I _ { i j }$ indicates the degree of ease of knowledge <sup>fl</sup>ow between two VKOs in a network. An analogous application of $I _ { i j }$ is found in the area of the electrical engineering in which $I _ { i j }$ is known as effective conductance (a measurement of how easily electrical current <sup>fl</sup>ows between nodes in a network) [19,82]. In addition, according to the theory of random walks, $I _ { i j }$ is an expected value of escape probability [19]. That is, $I _ { i j }$ can be viewed as a probabilistic capacity that the network transfers knowledge from one place to another.

The measure allows us to observe the marginal impact on the entire network complexity caused by changing a relationship between any two VKOs. Second, we consider merging VKOs under certain conditions as a way to increase the degree of knowledge dissemination of the entire VKON. The structure of virtual organization networks is to be a more amorphous web of connections and to continuously evolve in response to the need of knowledge [2]. Researchers argue that merge and split of virtual organizations may cause only a marginal cost, while offering substantial bene<sup>fi</sup>ts [55,57]. Due to the frictionless nature of virtual organization [9], merging VKOs would be bene<sup>fi</sup>cial to the process of improving knowledge transfer. In this section, we devise a measure of knowledge transfer capacity between two $\mathsf { V K O s } ,$ , and then use it to determine when to merge the two. Let N $\textit { \textbf { / } } e _ { i j }$ denote a new VKON with n − 1 VKOs after merging $C _ { i }$ and $C _ { j } .$ After merging two VKOs, the knowledge agents between the two, $e _ { i j } ,$ are no longer present. Let $I _ { i j }$ be the knowledge transfer capacity between two VKOs, $C _ { i }$ and $C _ { j } ,$ then we can derive Theorem 2 as follows.

Theorem 2. The knowledge transfer capacity $I _ { i j }$ between $C _ { i }$ and $C _ { j }$ is the ratio of the complexity of N and that of $\mathrm { ~ \bf ~ N ~ } / \mathrm { ~ } e _ { i j } ,$ That is,

$$
I _ {i j} = c (N) / c \left(N / e _ {i j}\right).\tag{5.2}
$$

Proof. See the $\mathsf { A } \mathrm { \Sigma }$ pendix A.

By reformulating Eq. (5.2), we can obtain an optimal point at which it is better for two VKOs to merge, providing bene<sup>fi</sup>ts to the entire net work.

$$
c \left(N / e _ {i j}\right) = \left(1 / I _ {i j}\right) \cdot c (N)\tag{5.3}
$$

As such, merging two VKOs reduces the network complexity when $I _ { i j } > 1$ , but escalates when $I _ { i j } < 1$ . Theorem 2 implies that merging two VKOs with a high degree of knowledge transfer capacity (a high score of $I _ { i j } )$ reduces the complexity of the resulting VKON, while merging two with a low degree of knowledge transfer capacity (a low score of $I _ { i j } )$ raises the complexity. In other words, when there are relatively a small number of knowledge transfer activities taking place between two VKOs (that is, the two have a low degree of knowledge transfer capacity $\left( I _ { i j } \right) )$ , merging the two lowers the cost of knowledge transfer by avoiding unnecessary detours in a network.

## 8. Improving knowledge transfer in VKON

We learn from Theorem 1 that the degree of knowledge dissemination through a VKON is maximized when knowledge agents are uniformly distributed across the network. Then, if there are knowledge agents newly joining a network, what is the most ef<sup>fi</sup>cient way to achieve a uniform distribution of agents?, and where should the agents be placed in order to optimize the network complexity? Note that researchers in a joint project between two separate knowledge domains are good examples of a knowledge agent. Then, those are often questions of of<sup>fi</sup>cers in such organizations as National Science Foundation (NSF) and National Institutes of Health (NIH), who seek for an opportunity of a cross-disciplinary project linking two research domains. By extending Theorem $^ { 2 , }$ we offer a new theorem providing an answer to the question. The proof is based on a new interpretation of $I _ { i j }$ as the inverse of the relative growth rate of c(N) with respect to $\mathbf { w } _ { i j } .$

Theorem 3. A marginal increase of VKON complexity is maximized when a new knowledge agent is placed between two VKOs with the minimum knowledge transfer capacity $\left( I _ { i j } \right)$

## Proof. See the Appendix A.

Via numerical simulation (Fig. 4), we attempt to <sup>fi</sup>nd the optimal positioning of a new knowledge agent in a VKON, and to show how the appearance of this new agent is conducive to the network complexity c(N) and knowledge transfer capacity I between the $C _ { i }$ and $C _ { j } .$ Suppose there is a VKON of <sup>fi</sup>ve VKOs. Among these <sup>fi</sup>ve VKOs, one knowledge agent can connect to any two between which the number of knowledge agents are $w _ { 1 2 } = 3 , w _ { 2 3 } = 2 , w _ { 2 5 } = 1 , w _ { 1 5 } = 1$ , and $w _ { 4 5 } = 3$ while others 0 (c.f. VKON (i) in Fig. 4). Information <sup>fl</sup>ows, $I _ { i j } ,$ are calculated by using Eq. (A.5) in the Appendix A. Note that an increase in network complexity is largest $( c ( N ) = 1 0 1 )$ ) when an additional agent is positioned between $C _ { 3 }$ and $C _ { 4 }$ (VKON (ii) in Fig. 4) where information <sup>fl</sup>ow is minimal $( I _ { 3 4 } = 0 . 7 1 )$ . In general, the smaller the information <sup>fl</sup>ow between two VKOs, the greater the marginal increase in network complexity by adding a new agent. It is worthwhile to note that the mean of ${ \dot { I } } _ { i j }$ which indicates the knowledge transfer capacity of the network is greatest $( \mathsf { M e a n } ( I _ { i j } ) = 2 . 2 2 )$ and the asymmetry of knowledge transfer capacity in the network is lowest $( \mathrm { S t d } ( I _ { i j } ) = 0 . 7 6 )$ , when the network complexity is the greatest (VKON (ii) in Fig. 4).

Theorem 3 suggests that optimal positioning of a knowledge agent can improve the capacity of knowledge transfer of a VKON. Among numerous innovations, the costs are lowered and bene<sup>fi</sup>ts increase as they are more widely accepted. A VKON, like other information technologies, can generate positive network-based economies through optimal distribution of knowledge agents which, in turn, results in enhanced accessibility of knowledge [24,58]. This can be achieved by knowledge agents who grab a better understanding of culture, norms, and common knowledge of the two VKOs, which eventually leads to improved knowledge transfer activities. The cost of placing a new knowledge agent between two VKOs will be also lowered as the number of agents between the two increases thanks to the externalities among the agents and related communities [4,52].

## 9. Direct vs. indirect transfer

The knowledge transfer capacity $I _ { i j }$ between two $\mathrm { V K O } s , C _ { i }$ and $C _ { j } ,$ relates direct and indirect communication. Indirect transfer is when there are intermediating VKOs between $C _ { i }$ and $C _ { j } ,$ while there is none in direct transfer. For example, the path $C _ { 1 }  C _ { 2 }$ in Fig. 3 is a direct transfer while $C _ { 1 }  C _ { 3 }  C _ { 2 }$ is an indirect transfer. The information transfer capacity through direct transfer between $C _ { i }$ and $C _ { j }$ is represented by the weight $w _ { i j }$ of the arc $e _ { i j } .$ We can represent the indirect knowledge transfer by

$$
\widetilde {w} _ {i j} = I _ {i j} - w _ {i j}.\tag{7.1}
$$

The signi<sup>fi</sup>cance of the indirect transfer is that it represents the effect of externality on knowledge transfer at a network level. Thus, it is reasonable to expect that $\widetilde { w } _ { i j }$ should be computable without any reference to the direct <sup>fl</sup>ow $w _ { i j } .$ The following proposition gives an expression of $\widetilde { w } _ { i j }$ that is independent of $I _ { i j }$ or $w _ { i j } .$ . Now, we de<sup>fi</sup>ne a new network $\grave { N \mu }$ e which is created by deleting $e _ { i j }$ from N.

Proposition 4. The knowledge transfer capacity of indirect transfer between $C _ { i }$ and $C _ { j }$ in a VKON can be calculated by the ratio of the complexity $o f N \mid e _ { i j }$ and that of $\mathrm { ~ \bf ~ N ~ } / \mathrm { ~ \bf ~ } e _ { i j } ,$ That $i s ,$

$$
\widetilde {w} _ {i j} = \frac {c (N \backslash e _ {i j})}{c (N / e _ {i j})}.\tag{7.2}
$$

<table><tr><td colspan="7"><img src="/api/attachments/YANVHG9M/fulltext/images/2cf72eb57848eb65c384ad35361dc41a6d8c4282a6abbb4463f3ece3a5e7ece4.jpg"/></td></tr><tr><td>Information Flow</td><td>(i)</td><td>(ii)</td><td>(iii)</td><td>(iv)</td><td>(v)</td><td>(vi)</td></tr><tr><td> $I_{12}$ </td><td>3.50</td><td>3.61</td><td>3.63</td><td>3.64</td><td>4.17</td><td>3.64</td></tr><tr><td> $I_{13}$ </td><td>1.27</td><td>1.63</td><td>1.71</td><td>1.29</td><td>2.27</td><td>1.29</td></tr><tr><td> $I_{14}$ </td><td>1.11</td><td>1.51</td><td>1.23</td><td>1.67</td><td>1.12</td><td>2.11</td></tr><tr><td> $I_{15}$ </td><td>1.75</td><td>2.02</td><td>2.07</td><td>2.11</td><td>1.79</td><td>2.50</td></tr><tr><td> $I_{23}$ </td><td>2.00</td><td>2.53</td><td>2.64</td><td>2.00</td><td>2.78</td><td>2.00</td></tr><tr><td> $I_{24}$ </td><td>1.11</td><td>1.77</td><td>1.34</td><td>2.11</td><td>1.12</td><td>1.67</td></tr><tr><td> $I_{25}$ </td><td>1.75</td><td>2.30</td><td>2.42</td><td>2.50</td><td>1.79</td><td>2.11</td></tr><tr><td> $I_{34}$ </td><td>0.71</td><td>1.71</td><td>1.18</td><td>1.03</td><td>0.85</td><td>0.91</td></tr><tr><td> $I_{35}$ </td><td>0.93</td><td>1.68</td><td>1.93</td><td>1.11</td><td>1.19</td><td>1.03</td></tr><tr><td> $I_{45}$ </td><td>3.00</td><td>3.48</td><td>3.00</td><td>3.64</td><td>3.00</td><td>3.64</td></tr><tr><td>Mean( $I_{ij}$ )</td><td>1.71</td><td>2.22</td><td>2.11</td><td>2.11</td><td>2.01</td><td>2.09</td></tr><tr><td>(Std( $I_{ij}$ ))</td><td>(0.91)</td><td>(0.76)</td><td>(0.81)</td><td>(0.93)</td><td>(1.05)</td><td>(0.96)</td></tr><tr><td>Complexity c(N)</td><td>42</td><td>101</td><td>87</td><td>80</td><td>75</td><td>80</td></tr></table>

Fig. 4. Optimal positioning of a new knowledge agent in VKON

Proof. The following equation (Eq. (7.3)) is called the Deletion– Contraction Recursion<sup>8</sup> [53] for c(N).

$$
c (N) = w _ {i j} \bullet c \left(N / e _ {i j}\right) + c \left(N \backslash e _ {i j}\right)\tag{7.3}
$$

Applying Eqs. (5.2) to (7.3), we obtain

$$
I _ {i j} = w _ {i j} + c \left(N \backslash e _ {i j}\right) / c \left(N / e _ {i j}\right).\tag{7.4}
$$

Now the result follows from $\widetilde { w } _ { i j } = I _ { i j } - w _ { i j } .$

Note that if all VKOs in N are reachable, then $c ( N / e _ { i j } ) \neq 0 ,$ because $\textit { N } / \textit { e } _ { i j }$ remains connected and the complexity of a connected network is positive. Proposition 4 implies that $\widetilde { w } _ { i j }$ will be zero iff $c ( N \mid e _ { i j } ) = 0 ,$ which happens only when $\boldsymbol { N } \backslash \boldsymbol { e } _ { i j }$ is no longer a connected network. That is, knowledge agents between two VKOs will be called essential to VKON if their disappearance severs the network into two. As such, disappearance of essential knowledge agents will result in two disconnected networks (a technical term for an essential arc representing the essential agent is an isthmus).

## 10. Common knowledge and network complexity

The literature on social capital emphasizes the importance of collective production of network-based capital [56]. Knowledge transfer, however, becomes costly when it takes place between two with little common knowledge [3,44]. For example, transferring knowledge regarding software installation will be costly when knowledge seeking and sourcing VKOs do not have basic common knowledge such as knowledge of the operating systems [12,61]. In contrast, if the two have too much common knowledge (that is, the knowledge pro<sup>fi</sup>les of the two VKOs are almost identical), there would be little knowledge to be transferred. What is necessary, therefore, is to identify the optimal amount of common knowledge between two VKOs, which becomes a complementary requirement for ef<sup>fi</sup>cient knowledge transfer. In this section, we measure the commonness of knowledge (knowledge similarity) and its effects on knowledge agents.

Consider a VKO with a knowledge pro<sup>fi</sup>le noted by a vector $P _ { i } = [ k _ { i 1 } ,$ $k _ { i 2 } , . . . , k _ { i T } ]$ . where $k _ { i t } ( \geq 0 )$ is the amount of knowledge on topic t, while T is the total number of topics. The magnitude of a knowledge pro<sup>fi</sup>le is denoted by $p _ { i } = | | P _ { i } | |$ , which assesses the quantity of knowledge in $C _ { i } .$ Assume that $p _ { i } > 0$ as each VKO maintains a certain amount of knowledge in at least one topic. Let $S _ { i j }$ and $D _ { i j }$ denote knowledge similarity, the normalized degree of knowledge commonness between by $C _ { i }$ and $C _ { j } ,$ and knowledge distance, the degree of difference of knowledge (transferable knowledge) between $P _ { i }$ and $P _ { j } ,$ respectively. $S _ { i j }$ and $D _ { i j }$ between the knowledge pro<sup>fi</sup>les $P _ { i }$ and $P _ { j }$ can be de<sup>fi</sup>ned as follows [74];

$$
S _ {i j} = \operatorname{Cos} \left(\Theta_ {i j}\right) = P _ {i} \cdot P _ {j} / p _ {i} p _ {j}\tag{8.1}
$$

$$
D _ {i j} = \left| \left| P _ {i} - P _ {j} \right| \right| ^ {1 / 2} = \left(p _ {i} ^ {2} + p _ {j} ^ {2} - 2 S _ {i j} p _ {i} p _ {j}\right) ^ {1 / 2}\tag{8.2}
$$

where $S _ { i j }$ ranges from 0 to 1. If any two VKOs have common knowledge, there must be at least one common topic (t N 0) and both $k _ { i t }$ and $k _ { j t }$ are positive. $S _ { i j } = 0$ , iff there is no common knowledge, and $S _ { i j } = 1$ when $P _ { i } = \lambda P _ { j }$ . There should be transferable knowledge, if $P _ { i } \neq P _ { j } .$ . In other words, if knowledge of two VKOs is of high similarity but no distance, it indicates that there is no knowledge to be transferred. Similarly, if it is of high distance but no similarity, it indicates that the two VKOs may not need knowledge of each other. Knowledge similarity is a qualitative measure of likelihood of knowledge transfer, while knowledge distance is a quantitative one. $S _ { i j }$ in conjunction with $D _ { i j } ,$ therefore, can be meaningful proxies of the amount of transferable knowledge between $C _ { i }$ and $C _ { j } .$

![](/api/attachments/YANVHG9M/fulltext/images/89724ef7b30bdb267432df80c14b3cf7dabd89da83d09b5b322232f0d673f6eb.jpg)  
Fig. 5. The curvilinear relationship among the number of participating knowledge agents $( w _ { i j } ) ,$ , knowledge similarity $( S _ { i j } )$ and knowledge magnitudes $( p _ { i } , p _ { j } )$

Furthermore, it is reasonable to conjecture that the more similar the knowledge pro<sup>fi</sup>les of two VKOs and the more transferable knowledge between the two, the more knowledge agents who would engage in knowledge transfer activities between them [29]. Studies showed that a VKO tends to <sup>fi</sup>nd and connect to another one with which the knowledge transfer cost can be optimized [74], and this cost declines as knowledge similarity between them is escalated. The rationale behind this argument is rather simple: Common knowledge lowers the knowledge transfer costs and lower transfer cost attracts knowledge consumers. A study of knowledge transfer in a multi-organizational network suggests that effective inter-organizational knowledge transfer requires relatedness in knowledge content among business units and the network of lateral relations that facilitates task units to acquire related knowledge [31]. Studies in sociology also showed that people tend to feel more comfortable with engaging in community activities when they <sup>fi</sup>nd communality [64].

Since the degree of commonness and distance of knowledge pro<sup>fi</sup>les are important factors in<sup>fl</sup>uencing the number of knowledge agents $( w _ { i j } )$ between $C _ { i }$ and $C _ { j } ,$ we obtain the following equation:

$$
n w _ {i j} = \ln c + \alpha \ln S _ {i j} + \beta \ln D _ {i j}\tag{8.3}
$$

where α, $\beta ,$ and c are positive constants. Applying the exponential function to both sides of Eq. (8.3), we obtain

$$
w _ {i j} = c S _ {i j} ^ {\alpha} D _ {i j} ^ {\beta} = c S _ {i j} ^ {\alpha} \left(p _ {i} ^ {2} + p _ {j} ^ {2} - 2 S _ {i j} p _ {i} p _ {j}\right) ^ {\beta / 2}.\tag{8.4}
$$

The number of expected knowledge agents $w = w _ { i j }$ is a function of knowledge similarity $S = S _ { i j }$ and distance ${ D _ { i j } } ^ { 9 }$ which is a function of $p _ { i }$ and $p _ { j } .$ Based on $\operatorname { E q . } \left( 8 . 4 \right)$ , Fig. 5 depicts the increasing number of knowledge agents between two VKOs in relation to changing $S _ { i j }$ and $p _ { i } .$

As the magnitudes of two knowledge pro<sup>fi</sup>les $P _ { i }$ and $P _ { j }$ converge, the curve of w tends to decrease after an optimal point of S. Otherwise, w increases monotonically as S increases. That is, when the magnitudes of knowledge pro<sup>fi</sup>les are the same, increasing their similarity S will eventually lead to identical knowledge pro<sup>fi</sup>les and there would be no knowledge to be transferred, whereas a certain degree of asymmetry between knowledge pro<sup>fi</sup>les may cause monotonic increase in the activities of knowledge agents as the similarity S increases. Based on this rationale, the following proposition, therefore, can be obtained.

Proposition 5. The number of knowledge agents between two VKOs is increasing and concave with respect to the knowledge similarity S initially. However, as the knowledge profiles of the two VKOs converge (that is, the difference of magnitudes of the two knowledge profiles decreases as shown in Fig. 5 (1) → (4)), it turns to a decreasing function after a certain optimal point of S.

## 11. Discussion

Knowledge is considered one of the most valuable resources for the growth and sustained competitive advantage of the modern organizations [49,55]. Because organizations do not have all knowledge necessary within their organizational boundary, they need to somehow search for external knowledge sources beyond the boundary. One ef<sup>fi</sup>- cient way of acquiring knowledge from external sources is to utilize virtual knowledge networks [7,29].

The importance of VKON cannot be overstated. When well structured, it would play as one of the most ef<sup>fi</sup>cient mechanisms for locating and transferring knowledge. An indispensable bene<sup>fi</sup>t of a VKON is that it creates an opportunity for knowledge workers to go beyond interaction with content and people. Even more dramatic is the availability and amount of knowledge offered. Combining content management with cross-organizational online collaboration at all levels of the business can help unite organizations and give them greater insight and perspective, which, in turn, exponentially increases the value of intellectual capital [60]. It is important to note that a majority of innovations have taken place across disciplines or organizational boundaries [41]. Researchers have agreed that collaboration across organizational boundaries is a true driving force of competitive advantage [12]. To address this urgent issue, National Science Foundation (NSF) has called for proposals for discovering advanced ways to facilitate cross-disciplinary intellectual collaboration using virtual organizational network.<sup>10</sup> We believe that successful formation of knowledge networks will signi<sup>fi</sup>cantly increase the bene<sup>fi</sup>ts and decrease the costs to knowledge organizations.

The result of this study provides a set of important implications regarding cross-organizational knowledge transfer using VKON. Theorem 1 can be used as a general guiding principle for maximizing the capacity of knowledge transfer, which eventually offers the most bene<sup>fi</sup>ts to VKON. This, however, may not be suf<sup>fi</sup>cient to warrant the optimal status of the network. Theorem 3 suggests that the <sup>fl</sup>ow of knowledge in a VKON can be even further improved by placing a new knowledge agent between two VKOs where information transfer capacity is at minimum. Theorem 2 offers an alternative measure assessing the knowledge transfer capacity between two VKOs. It is worth noting that while the measures of knowledge <sup>fl</sup>ow capacity from the prior studies merely rely on endogenous variables of the two related VKOs [65], Eq. (5.2) enables us to assess the knowledge transfer capacity between two VKOs using network complexity. VKOs may need to be merged at times in order to enhance the capacity of knowledge transfer in the entire network. An important question to a VKON manager is when two VKOs should be merged. Theorem 2 provides a set of criteria for merging VKOs. A general guideline is that merging two VKOs with a high degree of knowledge transfer capacity will decrease the complexity of the entire VKON, while merging two with a low degree of knowledge transfer capacity will improve it. Using Proposition 4, we can identify essential knowledge agents who play a critical role in knowledge transfer of the whole VKON. The <sup>fi</sup>ndings of this paper will provide a set of useful guidelines for managing a VKON.

The notion of centrality is derived from local information around a given node and does not provide suf<sup>fi</sup>cient information regarding global properties of the network. Unlike other centrality measures, information centrality adopted in this paper begins with global invariants of the network and extracts local information. Hence, one may speculate the possibility of retrieving global properties of the network upon the underlying meaning of this centrality. This study reveals this hidden mystery (Theorem 2) and provides how this intriguing property can be concretely implemented (Theorem 3) for the purpose of ef<sup>fi</sup>cient global stabilization by strategically distributing knowledge agents. Therefore, we claim that the main contributions of this paper relate global organizational strategy rather than micro management of a network.

Our macro perspectives on virtual knowledge network are differentiated by three points from the ones of the prior studies investigating within-organization knowledge transfer. One, the prior studies mainly focused on the interaction at an individual level within a single community boundary, and thus supplied limited information in relation to VKON. This study examined the relationships between/among VKOs by constraining knowledge agents, and illustrated the dynamics of inter-community knowledge transfer.

Two, despite the enormous bene<sup>fi</sup>ts of VKON, the success and failure of an implementation depend primarily on the social context in which they are used [3]. We have taken into account the role of common knowledge in the virtual knowledge transfer process. Common knowledge accumulated in an organizational boundary has been regarded as the organizational memory or learning capacity [48]. While the prior studies of virtual communities have emphasized merely on the quantity of knowledge transferred through a network structure, it is a pioneering attempt to consider the role of common knowledge of virtual communities as a determinant of knowledge transfer capacity.

Three, one unique phenomenon in the evolution process of a VKO is that they evolve by merging two VKOs to improve the capacity of the knowledge <sup>fl</sup>ow. We investigated the impacts of merging VKOs on knowledge transfer of the entire network.

Finally, network complexity and knowledge transfer capacity are crucial indicators of the knowledge transfer ef<sup>fi</sup>cacy in a VKON. There are conventional complexity and centrality measures devised from the perspective of of<sup>fl</sup>ine individual networks (c.f. [23]). The applications of these measures, however, are limited to the context of an of<sup>fl</sup>ine individual network. We reinterpreted those measures by re<sup>fl</sup>ecting unique characteristics of virtual knowledge organizations; the mergeability [63] of VKOs. The other aspect of VKOs, the splitability of a VKO, should be further investigated in the future research.

We attempted to develop new VKO-level knowledge transfer capacity assessment methods using network complexity. In addition, the effects of network complexity on the capacity of knowledge transfer in VKON were examined. The validity of developed measures needs to be empirical tested in future research.

## 12. Concluding remarks

During the last two decades, many research and development organizations involving innovative tasks began an obvious and swift transformation toward using VKOs [39]. Recently, the speed of organizational transformation has been considerably improved due to environmental and cultural transformation using virtual knowledge networks. To our knowledge, this is the <sup>fi</sup>rst study employing the notion of the network theory in the context of a virtual knowledge organization network.

This new perspective on knowledge creation and transfer across virtual communities is important not only because it offers a macroscopic view of knowledge economics, but also because it provides a new opportunity for modern society to speed up the process of interdisciplinary knowledge creation. We attempted to further extend the theory of virtual knowledge communities and intercommunity knowledge transfer from a macroscopic perspective. While the founding of this study presents the dynamics of global level of VKON, further research should be conducted with variables re<sup>fl</sup>ecting VKO's local characteristics. For example, a method of sequence data classi<sup>fi</sup>cation [18,21] would be a useful tool to conduct an extended examination with VKO's local properties.

The implications of studies in the area of VKOs, in general, are bounded as most studies merely focus on the knowledge sharing process at nodal (focusing on the behavior of a single community) or dyadic (focusing on the relational behavior of a pair) levels. It is important to note that knowledge creation and transfer activities are no longer bounded within a VKO, but have evolved into further sophisticated forms of transfer through a cross-VKO network. As cross-community knowledge <sup>fl</sup>ows become more complex with increasing number of VKOs, it is imperative to understand the dynamics of VKO networks from a macro perspective. While the analysis in this study is essentially mathematical, both the future research based on quantitative and qualitative methods will recognize the potential for models.

## Acknowledgments

This work was <sup>fi</sup>nancially supported by the National R&D project of "Development of Technology for support to deep seawater industry" supported by the Korean Ministry of Oceans and Fisheries, and conducted by Seung Kyoon Shin. This work was also partially supported by a grant from the Simons Foundation #245994 to Woong Kook while he was at the University of Rhode Island.

## Appendix A

Proof of Theorem 2. Consider a case that $i = 1 \mathrm { a n d } j = 2 ,$ , since the complexity of network does not depend on how the nodes are ordered, the proofs for other cases are the same after relabeling the nodes as necessary. As preliminary facts, we note that if J is an n × n matrix with all entries equal to 1, then it follows from Temperley's formula [69] that the determinant of $B = J + L ( N )$ equals ${ \operatorname* { d e t } ( B ) = n ^ { 2 } \cdot c ( N ) }$ . The Laplacian matrix $L ( N / e _ { 1 2 } )$ is obtained from L(N) by replacing Row 2 by Row 1 + Row 2 and Column 2 by Column 1 + Column 2 and then by deleting Row 1 and Column 1. $\mathsf { A s C } = B ^ { - 1 } = ( \mathsf { c } _ { i j } )$ is the inverse matrix of B and B(i|j) is obtained from B by deleting row j and column i, we have

$$
c _ {i j} = (- 1) ^ {i + j} \det (B (i | j)) / \det (B)\tag{A.1}
$$

for each i and j. Then,

$$
\begin{array}{c} c _ {1 1} + c _ {2 2} - 2 \cdot c _ {1 2} = [ \det (B (1 | 1)) + \det (B (2 | 2)) + 2 \cdot \det (B (1 | 2)) ] \\ / \Big [ n ^ {2} \cdot c (N) \Big ]. \end{array}\tag{A.2}
$$

Now, from the multi-linearity of the determinant function and the construction of $L ( N / e _ { 1 2 } )$ from L(N), we get

$$
[ \det (B (1 | 1)) + \det (B (2 | 2)) + 2 \cdot \det (B (1 | 2)) ] = \det (K + L (N / e _ {1 2})),\tag{A.3}
$$

where K is an $( n - 1 ) \times ( n - 1 )$ matrix with the <sup>fi</sup>rst row equal to $( 4 , 2 , 2 , . . . , 2 )$ and all of the remaining rows equal to $( 2 , 1 , 1 , . . . , 1 )$ Hence, it follows by a similar argument for det(B) that

$$
\det (K + L \left(N / e _ {1 2}\right)) = \left(4 + 2 \cdot (2 n - 4) + (n - 2) ^ {2}\right) \cdot c \left(N / e _ {1 2}\right) = n ^ {2} \cdot c \left(N / e _ {1 2}\right).\tag{A.4}
$$

Finally, we have

$$
\begin{array}{l} I _ {1 2} = (c _ {1 1} + c _ {2 2} - 2 \cdot c _ {1 2}) ^ {- 1} = \left[ n ^ {2} \cdot c (N) \right] / \left[ n ^ {2} \cdot c (N / e _ {1 2}) \right] \\ = c (N) / c (N / e _ {1 2}). \end{array}\tag{A.5}
$$

□

Proof of Theorem 3. By replacing N with $\textit { N } / \textit { e } _ { i j }$ in Eq. (3.2), we obtain

$$
c \left(N / e _ {i j}\right) = \sum_ {T ^ {\prime} \in \beta \left(N / e _ {i j}\right)} c \left(T ^ {\prime}\right)\tag{A.6}
$$

where the sum is over all spanning trees T′ in $\textit { N } / \ e _ { i j } .$ Note that w is not included in any c(T′). There is a bijective matching between $\beta ( N , e _ { i j } )$ , the set of all spanning trees T containing the arc $e _ { i j } ,$ , and $\beta ( N / e _ { i j } ) ;$ the matching is given by $T \to T / e _ { i j } .$ Hence, we have,

$$
c \left(N / e _ {i j}\right) = \sum_ {T \in \beta (N, e _ {i j})} c \left(T / e _ {i j}\right).\tag{A.7}
$$

Since $c ( T ) = \mathbf { w } _ { i j } \cdot c ( T / e _ { i j } )$ for each $T \in \beta ( N , e _ { i j } )$ , we have

$$
\partial_ {w _ {i j}} c (T) = c \left(T / e _ {i j}\right).\tag{A.8}
$$

Furthermore, it is clear that $\partial _ { w _ { i i } } c ( T ) = 0 \mathrm { i f } T \not \in \beta ( N , e _ { i j } )$ because such T will not contain $\mathbf { w } _ { i j } .$ Therefore,

$$
\partial_ {w _ {i j}} c (N) = \partial_ {w _ {i j}} \sum_ {T \in \beta (N)} c (T)\tag{A.9}
$$

$$
= \partial_ {w _ {i j}} \sum_ {T \in \beta (N, e _ {i j})} c (T) + \partial_ {w _ {i j}} \sum_ {T \notin \beta (N, e _ {i j})} c (T)\tag{A.10}
$$

$$
= \sum_ {T \in \beta (N, e _ {i j})} \partial_ {w _ {i j}} c (T)\tag{A.11}
$$

$$
= \sum_ {T \in \beta (N, e _ {i j})} c (T / e _ {i j}) = c (N / e _ {i j})\tag{A.12}
$$

From Theorem 2 and the fact $c ( N ⁄ e _ { i j } ) = \partial _ { w _ { i i } } c ( N )$ , we conclude that $I _ { i j }$ is minimal (among all dyadic knowledge transfer capacity), if and only $\mathrm { i } \mathrm { \bar { f } } \partial _ { w _ { i j } } c ( N )$ is maximum among all partial derivatives of $c ( N )$ . This implies that a marginal increase of $c ( N )$ is maximized when an additional knowledge agent is placed between $C _ { i }$ and $C _ { j }$ with minimum $I _ { i j } . \quad \square$

## References

[1] E. Abrahamson, L. Rosenkopf, Social network effects on the extent of innovation diffusion: a computer simulation, Organization Science 8 (3) (1997) 289–309.

[2] M.K. Ahuja, K.M. Carley, Network structure in virtual organizations, Organization Science 10 (6) (1999) 741–757

[3] M.K. Ahuja, D.F. Galletta, K.M. Carley, Individual centrality and performance in virtual R&D groups: an empirical study, Management Science 49 (1) (2003) 21–38.

[4] K.J. Arrow, Methodological individualism and social knowledge, American Economic Review 84 (2) (1994) 1–9

[5] A. Bavelas, A mathematical model for group structures, Human Organization 7 (3) (1947) 16–30.

[6] M. Beauchamp, An improved index of centrality, Behavioral Science 10 (1965) 161-163

[7] M. Bieber, D. Engelbart, R. Furuta, S.R. Hiltz, Toward virtual community knowledge evolution, Journal of Management Information Systems 18 (4) (2002) 11–35.

[8] J.S. Brown, P. Duguid, Organizing knowledge, California Management Review 40 (3) (1998) 90–111.

[9] E. Brynjolfsson, M.D. Smith, Frictionless commerce? A comparison of Internet and conventional retailers, Management Science 46 (4) (2000) 563–585.

[10] C.T. Butts, The complexity of social networks: theoretical and empirical <sup>fi</sup>ndings, Social Networks 23 (1) (2001) 31–72.

[11] K. Carley, A theory of group stability, American Sociological Review 56 (3) (1991) 331–354.

[12] P.R. Carlile, Transferring, translating, and transforming: an integrative framework for managing knowledge across boundaries Organization Science 15 (5) (2004) 555–568

[13] W.M. Cohen, D.A. Levinthal, Absorptive capacity: a new perspective on learning and innovation, Administrative Science Ouarterly 35 (1) (1990) 128–152

[14] B.S. Cohn, M. Marriott, Networks and centres of integration in Indian civilization, Journal of Social Research 1 (1958) 1–9.

[15] R. Cowan, Network models of Innovation and knowledge diffusion, in: S. Breschi, F. Malerba (Eds.), Clusters, Networks, and Innovation, Oxford University Press, New York, 2006, pp. 29–53.

[16] J.A. Czepiel, Word-of-mouth processes in the diffusion of a major technological innovation, Journal of Marketing Research 11 (2) (1974) 172–180.

[17] N.M. Dixon, Common Knowledge: How Companies Thrive by Sharing What They Know Harvard Business School Press Boston Mass 2oo0

[18] G. Dong, J. Pei, Classi<sup>fi</sup>cation, clustering, features and distances of sequence data, Advances in Database Systems 33 (1) (2007) 47–65.

[19] P.G. Doyle, J.L. Snell, Random Walks and Electric Networks, 2006.

[20] J.H. Dyer, N.W. Hatch, Relation-speci<sup>fi</sup>c capabilities and barriers to knowledge transfers: creating advantage through network relationships, Strategic Management Journal 27 (4) (2006) 701–719.

[21] U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, Advances in Knowledge Discovery and Data Mining, MIT Press, Cambridge, 1996.

[22] L.C. Freeman, Centrality in social networks: conceptual clari<sup>fi</sup>cation, Social Networks 1 (1978) 215–239.

[23] L.C. Freeman, Turning a pro<sup>fi</sup>t from mathematics: the case of social networks, Journal of Mathematical Sociology 10 (1984) 343–360.

[24] J.M. Gallaugher, Y.-M. Wang, Understanding network effects in software markets: evidence from web server pricing, MIS Quarterly 26 (4) (2002) 303–327.

[25] M.C. Golumbic, I.B.-A. Hartman, Graph Theory, Combinatorics and Algorithms: Interdisciplinary Applications, Springer, 2005.

[26] N.F. Granados, A. Gupta, R.J. Kauffman, The impact of IT on market information and transparency: a uni<sup>fi</sup>ed theoretical framework, Journal of the Association for Information Systems 7 (3) (2006) 148–177.

[27] R.M. Grant, Toward a knowledge-based theory of the <sup>fi</sup>rm, Strategic Management Journal 17 (1996) 109–122(Winter).

[28] T.L. Grif<sup>fi</sup>th, J.E. Sawyer, M.A. Neale, Virtualness and knowledge in teams: managing the love triangle of organizations, individuals, and information technology, MIS Quarterly 27 (2) (2003) 265–287.

[29] B. Gu, P. Konana, B. Rajagopalan, H.-W.M. Chen, Competition among virtual communities and user valuation: the case of investing-related communities, Information Systems Research 18 (1)(2007) 68–87.

[30] R. Gulati, N. Nohria, A. Zaheer, Strategic networks, Strategic Management Journal 21 (3) (2000) 203–215.

[31] M.T. Hansen, Knowledge networks: explaining effective knowledge sharing in multiunit companies, Organization Science 13 (3) (2002) 232–248.

[32] A. Hargadon, R.I. Sutton, Technology brokering and innovation in a product development <sup>fi</sup>rm, Administrative Science Quarterly 42 (4) (1997) 716–749.

[33] M. Hoegl, K.P. Parboteeah, C.L. Munson, Team-level antecedents of individuals' knowledge network, Decision Sciences 34 (4) (2003) 741–770.

[34] A.C. Inkpen, Knowledge transfer and international joint ventures: the case of NUMMI and General Motors, Strategic Management Journal 29 (4) (2007) 447–453

[35] A.C. Inkpen, A. Dinur, Knowledge management processes and international joint ventures, Organization Science 9 (4) (1998) 454–468.

[36] H. Jeong, S.P. Mason, A.-L. Barabási, Z.N. Oltvai, Lethality and centrality in protein networks Nature 411 (3) (2001) 41–42

[37] E. Katz, P.F. Lazarsfeld, Personal In<sup>fl</sup>uence: The Part Played by People in the Flow of Mass Communications Free Press Glencoe Ill 1955

[38] A.K. Kelmans, On graphs with the maximum number of spanning trees, Random Structures and Algorithms 9 (1/2) (1996).

[39] G. Kuk, Strategic interaction and knowledge sharing in the KDE developer mailing list, Management Science 52 (7) (2006) 1031–1042

[40] G.K. Lee, R.E. Cole, From a <sup>fi</sup>rm-based to a community-based model of knowledge creation: the case of the Linux kernel development, Organization Science 14 (6) (2003).

[41] D. Leonard-Barton, Wellsprings of Knowledge, Harvard Business School Press, Boston, MA, 1995.

[42] N.S. Levinson, M. Asahi, Cross-national alliances and interorganizational learning, Organizational Dynamics 24 (2) (1995) 50–63.

[43] I. Lin. X. Geng, A.B. Whinston, A sender-receiver framework for knowledge transfer. MIS Ouarterly 29 (2) (2005) 197–219.

[44] W.S. Lovejoy, A. Sinha, Ef<sup>fi</sup>cient structures for innovative social networks, Management Science 56 (7) (2010) 1127–1145

[45] M.L. Markus, Toward a theory of knowledge reuse: types of knowledge reuse situations and factors in reuse success, Journal of Management Information Systems 18 (1) (2001) 57–93.

[46] L.F. Mesquita, J. Anand, T.H. Brush, Comparing the resource-based and relational views: knowledge transfer and spillover in vertical alliances, Strategic Management Journal 29 (9) (2008) 913–941.

[47] P.R. Monge, N. Contractor, Theories of Communication Networks, Oxford University Press, New York, 2003.

[48] C. Moorman, A.S. Miner, Organizational improvisation and organizational memory, Academy of Management Review 23 (4) (1998) 698–723.

[49] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1) (1994) 14–37.

[50] I. Nonaka, N. Konno, The concept of “Ba”: building a foundation for knowledge creation, California Management Review 40 (3) (1998) 40–54.

[51] I. Nonaka, T. Nishiguchi, Knowledge Emergence: Social, Technical, and Evolutionary Dimensions of Knowledge Creation, Oxford University Press, New York, 2001.

[52] E. Ofek, M. Sarvary, Leveraging the customer base: creating competitive advantage through knowledge management, Management Science 47 (11) (2001) 1441–1456.

[53] J.G. Oxley, Matroid Theory, Oxford University Press, New York, 2006.

[54] J.-C. Pastor, J.R. Meindl, M.C. Mayo, A network effects model of charisma attributions, Academy of Management Journal 45 (2) (2002) 410–420

[55] L. Poppo, T. Zenger, Testing alternative theories of the <sup>fi</sup>rm: transaction cost, knowledge-based and measurement explanations for make-or-buy decisions in in: formation services, Strategic Management Journal 19 (9) (1998) 853–877.

[56] R.D. Putnam, Bowling alone: the collapse and revival of American community, 2001.

[57] J.J. Reuer, M.P. Koza, Asymmetric information and joint venture performance: theory and evidence for domestic and international joint ventures, Strategic Management Journal 21 (1) (2000) 81–88.

[58] F.J. Riggins, C.H. Kriebel, T. Mukhopadhyay, The growth of interorganizational systems in the presence of network externalities, Management Science 40 (8) (1994) 984–998.

[59] D.L. Rogers, Sociometric analysis of interorganizational relations: application of theory and measurement, Rural Sociology 39 (4) (1974) 487–503.

[60] M.J. Rosenberg, E-Learning: Strategies for Delivering Knowledge in the Digital Age, McGraw-Hill, 2001.

[61] R. Sabherwal, I. Becerra-Fernandez, Integrating speci<sup>fi</sup>c knowledge: insights from the Kennedy Space Center, IEEE Transactions on Engineering Management 52 (3) (2005) 301–315.

[62] S. Sarker, S. Sarker, S. Kirkeby, S. Chakraborty, Path to “stardom” in globally distributed hybrid teams: an examination of a knowledge-centered perspective using social network analysis, Decision Sciences 42 (2) (2011) 339.

[63] K.C. Sia, S. Chebotariov, J. Cho, Theory of Mergeability: Safely Merging Two Versions of a Document, ACM, VLDB Endowment, Vienna, Austria, 2007.

[64] E.R. Smith, D.M. Mackie, Social Psychology, 2nd ed. Psychology Press, Philadelphia, PA, 2000.

[65] K. Stephenson, M. Zelen, Rethinking centrality: methods and examples, Social Networks 11 (1) (1989) 1–37.

[66] G. Szulanski, The process of knowledge transfer: a diachronic analysis of stickiness, Organizational Behavior and Human Decision Processes 82 (1) (2000) 9–27.

[67] A.S. Tanenbaum, Computer Networks, Prentice Hall, 2002

[68] D.J. Teece, Technology transfer by multinational <sup>fi</sup>rms: the resource cost of transferring technological know-how, Economic Journal 87 (346) (1977) 242–261.

[69] H.N.V. Temperley, On the mutual cancellation of cluster integrals in Mayer's fugacity series, Proceedings of the Physical Society 83 (1964) 3–16.

[70] R. Tissen, D. Andriessen, F.R. Lopez, The Knowledge Dividend: Creating Highperformance Companies, Prentice Hall, London, 2000.

[71] M.L. Tushman, R. Katz, External communication and project performance: an investigation into the role of gatekeepers, Management Science 26 (11) (1980) 1071–1085.

[72] W.T. Tutte, The dissection of equilateral triangles into equilateral triangles, Mathematical Proceedings of the Cambridge Philosophical Society 44 (4) (1948) 463–482.

[73] T.W. Valente, Network Models of the Diffusion of Innovations, Hampton Press, NJ, 1995.

[74] M. Van Alstyne, E. Brynjolfsson, Global village or cyber-Balkans? Modeling and measuring the integration of electronic communities, Management Science 51 (6) (2005) 851–868.

[75] E.A. von Hippel, “Sticky information” and the locus of problem solving: Implications for innovation, Management Science 40 (4) (1994) 429–440.

[76] J. Walter, C. Lechner, F.W. Kellermanns, Knowledge transfer between and within alliance partners: private versus collective bene<sup>fi</sup>ts of social capital, Journal of Business Research 60 (7) (2007) 698.

[77] M.M. Wasko, S. Faraj, Why should I share? Examining social capital and knowledge contribution in electronic networks of practice, MIS Quarterly 29 (1) (2005) 35–56.

[78] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, Cambridge, 1994

[79] D.I. Watts, Small Worlds: The Dynamics of Networks between Order and Randomness, Princeton University Press, 2003.

[80] D.B. West, Introduction to Graph Theory, Prentice Hall, 1996.

[81] C. Williams, Transfer in context: replication and adaptation in knowledge transfer relationships, Strategic Management Journal 28 (9) (2007) 867–889

[82] F.Y. Wu, Theory of resistor networks: the two-point resistance, Journal of Physics A: Mathematical and General 37 (2004) 6653–6673.

[83] S.A. Zahra, G. George, Absorptive capacity: a review, reconceptualization, and extension, Academy of Management Review 27 (2) (2002) 180–203.

[84] Z.J. Zhao, J. Anand, A multilevel perspective on knowledge transfer: evidence from the Chinese automotive industry, Strategic Management Journal 30 (9) (2009) 959-983.

Seung Kyoon Shin is an Associate Professor of Information Systems in the College of Business Administration at the University of Rhode Island. Prior to joining academia, he worked in IT industry as a software specialist, IS project manager, and system integration consultant. His research has appeared in journals such as Information and Management, Communications of the ACM, Information Systems Research, IEEE Transactions on Engineering Management, Decision Support Systems, and International Journal of Production and Operation Management among others.

Woong Kook is an Associate Professor in the Department of Mathematical Sciences at the Seoul National University, Seoul, Korea. His current research interests include spectral methods for simplicial complexes, topological combinatorics, topological data analysis, neural networks, random walks, centrality, and spanning tree entropy. His research has appeared in journals such as Journal of the American Mathematical Society, Journal of Combinatorial Theory B, European Journal of Combinatorics, Advances in Applied mathematics, and Applied Mathematics Letters
