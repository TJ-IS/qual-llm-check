---
otero_id: 1572
otero_key: "CWUTPRA9"
title: "A framework for exploring organizational structure in dynamic social networks"
authors: "Jiangtao Qiu; Zhangxi Lin"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for exploring organizational structure in dynamic social networks

Jiangtao Qiu <sup>a,</sup>⁎, Zhangxi Lin <sup>b</sup>

<sup>a</sup> School of Information, Southwestern University of Finance and Economics, Chengdu, China

<sup>b</sup> Center for Advanced Analytics and Business Intelligence, Texas Tech University, Lubbock, TX, USA

a r t i c l e i n f o

Available online 1 February 2011

Keywords: Social network analysis Organizational structure Dynamic social network Community discovery Evolution analysis

## a b s t r a c t

Recent research has provided promising results relating to discovering communities within a social network. We <sup>fi</sup>nd that further representing the organizational structure of a social network is an interesting issue that helps gain better understandings of the social network. In this paper, we de<sup>fi</sup>ne a data structure, named Community Tree, to depict the organizational structure and provide a framework for exploring the organizational structure in a social network. In this framework, an algorithm, which combines a modi<sup>fi</sup>ed PageRank and Random Walk on graph, is developed to derive the community tree from the social network. In the real world, a social network is constantly evolving. In order to explore the organizational structure in a dynamic social network, we develop a tree learning algorithm, which employs tree edit distance as the scoring function, to derive an evolving community tree that enables a smooth transition between two community trees. We also propose an approach to threading communities in community trees to obtain an evolution graph of the organizational structure, by which we can reach new insights from the dynamic social network. The experiments conducted on synthetic and real dataset demonstrate the feasibility and applicability of the framework. Based on the theoretical outcomes, we further apply the proposed framework to explore the evolution of organizational structure with the 2001 Enron dataset, and obtain several interesting <sup>fi</sup>ndings that match the context of Enron.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Community discovery is an important problem in social network analysis (SNA), where the goal is to identify related groups of members such that intra-community associations are denser than inter-communities associations [6,10,14,17,22,23,26,30,33,35]. Generally, a social network (SN) is composed of one to multiple communities, each of which is a collection of members sharing some common properties, such as hobbies, social functions, discussion topics, concerned issues, or on-going tasks. Recently, community discovery, a promising research topic, has attracted broad attention from researchers in both computer science and information systems. Researchers have developed various approaches to detect and extract communities from an SN. Speci<sup>fi</sup>cally, discovering the organizational structure of communities in an SN has been identi<sup>fi</sup>ed as an interesting but challenging problem [11,32]. Examples of important applications include identifying potential key candidates for viral marketing or discovering core members of criminal group in monitoring criminal network. Research on <sup>fi</sup>nding in<sup>fl</sup>uential members in an SN [4,11,19,31,32] is one effort in this direction, but outcomes to date have limited power to provide a complete view of the organizational structure. In our view, a uni<sup>fi</sup>ed framework for the comprehensive understanding of the organizational structure of an SN is needed. In this paper, we pursue such a framework. The basic research problem we address is how to formalize the description of the organizational structure in an SN and design algorithms necessary for structure determination.

Social networks are changing and evolving in the real world. New members may join the network, existing members may quit from the network, and associations among members constantly change over time. For example, users in web forums may change their interest in topics over time. In an academic network, scholars often change their research interests and research collaborators. Therefore, our proposed framework should be capable of supporting the exploration of organizational structure in a dynamic setting. Some earlier research has presented approaches to discovering communities from a dynamic social network [15,29,36]. These approaches detect changes of communities in an SN, but do not address questions related to the changing organizational structure, such as who is becoming more powerful or members power scope is shifting.

Earlier research efforts [7,12,16] have also addressed determining the hierarchy in an SN, where hierarchy has a similarity to an organizational structure. Different from this earlier work, our framework uses a community tree data structure to represent organizational structure. This provides a quantitative depiction of characteristics of organizational structure and can present an evolution of organizational structure of a dynamic SN. Our contributions include:

(1) De<sup>fi</sup>ning a community tree to depict the organizational structure for an SN;

(2) Developing an algorithm to derive the community tree from the SN.

(3) Developing a tree learning algorithm to generate the evolving community trees.

(4) Proposing an approach for representing the evolution of the organizational structure based on the evolving community trees; and,

(5) De<sup>fi</sup>ning new metrics for studying the properties of a dynamic SN.

The remainder of this paper is organized as follows. Section 2 reviews the related research on community discovery and organizational structure. Section 3 introduces the concept of community tree and proposes an approach for deriving the community tree from a static social network. Section 4 presents the methods for analyzing the evolution of organizational structure in a dynamic SN. Section 5 provides the experimental results. Section 6 reports the application of the framework to Enron e-mail corpus and details several key <sup>fi</sup>ndings. Section 7 offers concluding remarks.

## 2. Related work

## 2.1. Community discovery

Community discovery is one of the most important problems in SNA. There are two threads of research on community discovery, static community discovery and dynamic community discovery. The methods on static community discovery include hierarchical clustering [22,25,30], graph partitioning [6,10,14,26] and others [23,35]. Hierarchical clustering methods aim at <sup>fi</sup>nding natural grouping divisions of a social network based on various metrics of similarity or connection strength among vertices in a graph. Hierarchical clustering methods further fall into two broad classes, agglomerative and divisive, depending on whether the method's focus is on the addition or removal of edges to or from the network

The graph partitioning approach treats an SN as a graph. Community discovery involves dividing the graph into a set of subgraphs. The fundamental issue is how to divide a graph into two subgraphs. MINcut [6] is the simplest algorithm for the purpose, which partitions a connected graph (network) into two sub-graphs with the cut size minimized. However, it tends to result in a very small subgraph cut away. Other improved algorithms include the normalized cut [26], ratio cut [14], and min–max cut [10]. In exploratory graph partitioning for community discovery, typically a top–down technique is applied to recursively cut a graph into a given number of subgraphs. Exploratory graph partitioning utilizes binary cutting algorithms as the elementary component and adopts a cost function criteria to determine the optimal solution from multiple choices at different branches of the division.

A few other methods have been introduced to tackle the SN community discovery task. Zhou et al. [35] propose two generative Bayesian models, combining probabilistic modeling with community detection, for semantic SN community discovery. Newman and Girvan [23] present an algorithm for discovering community structure from networks with only a single type of vertex and a single type of undirected, unweighted edge. The algorithm identi<sup>fi</sup>es a set of edges with high betweenness and removes these edges one by one in a descending order of betweenness to split the network into communities. A measure, called modularity, is used to indicate the strength of the communities discovered.

In analyzing a dynamic social network, most studies [28,29,35] to date have sought either to obtain a snapshot of a single point in time in the dynamic social network or to aggregate changes of dynamic social network over a time window. However, both approaches may miss important tendencies of dynamic networks. Tantipathananandh [29] proposed a framework to identify communities in a social network that changes over time, and proved that searching for the most explanatory community structure is NP-hard and APX-hard. Tang et al. [28] used a spectral clustering framework to identify community evolution based on snapshots from a dynamic multimode network. In this approach, the effect of temporal social network changes is used as a regularization term when performing the clustering. Zhou et al. [36] present a new constrained partitioning algorithm to investigate the community discovery problem with the communication documents produced over time, threading the statically derived communities in different time periods.

## 2.2. Organizational structure

Organizational structure discovery of SN can provide better understanding of an SN. Some existing work explores the organizational structure using an SN hierarchy. Li et al. [16] proposed a hierarchical community model to distinguish community cores from the af<sup>fi</sup>liated members. Aaron et al. [7] presented a general technique for inferring the hierarchical structure from a network, explicitly including the organizations in all scales in an SN. Marko et al. [12] employed an approach to semi-automatically construct ontology from an SN, in which the hierarchy of the ontology presents the organizational structure in the SN. However, hierarchies can only divide members of an SN into groups in different scales. It cannot reveal important information about the organizations in the SN such as what individual is the immediate leader of another member, or what is the importance level of an individual member.

In the work<sup>fl</sup>ow area, organization mining has also been the focus of past research [1,21,27]. Different from our approach, the work<sup>fl</sup>ow area research has emphasized the exploration of organizational structure in the unit from event logs of information systems.

CrimeNet Explore [32] is a system for criminal network knowledge discovery that incorporates several techniques including the concept space approach, hierarchical clustering, social network analysis, and multidimensional scaling. CrimeNet can obtain the organizational information about a criminal network, such as who is the core of the network, what subgroups exist in the network, and so on. However, CrimeNet does not consider dynamic characteristics of criminal networks.

To extend the above literature, in our research, we propose a community tree data structure to depict SN organizational structure and provide metrics for depicting the characteristics of organizational structure, thereby providing enriched information about a dynamic SN.

## 3. Discovering the organizational structure in a static social network

## 3.1. Organization structure of a social network

Song and Van [27] presented a de<sup>fi</sup>nition of organizational model for organizational structure, where an organizational model consists of organizational units (e.g. functional units), roles (e.g. duty), originators, and relationships (e.g., hierarchy). In this paper, we de<sup>fi</sup>ne the organizational structure of an SN as a hierarchy which represents communities (or units) and subordinations of members in the SN. Subordination describes the relationship between two members where the leader is the most likely destination of information <sup>fl</sup>ow starting from the subordinate.

SN can be constructed using associations among members, such as communications in a communication network, paper references in an academic network, or blogger-to-blogger comment in the blogosphere. The derived organizational structure of an SN does not necessarily map well a real-world organization. For example, there does not exist a real organization in an academic network or in a blogosphere. Even for a communication network constructed from e-mails in a real-world organization, we may not be able to tell exactly to what extent the relationships can be mapped to the real-world organizational structure. The organizational structure derived from an SN can depict units (or community) and subordinations of members in the SN, thus helping gain better understandings of the real-world organization. For example, in an organizational structure derived from a communication network, a unit indicates that there are more frequent communications among the members in the unit. When a member is designated as a leader in a unit this generally implies that the member is either a leader in real-world organization or an active agent (e.g., a secretary of leaders) for some real-world leader. In an organizational structure derived from a blogoshpere, a unit indicates a circle of friends. A leader in the unit is a member who draws most attention in the circle of friends. The subordination relationship here indicates the closest contact of a subordinate is his/her immediate leader.

To depict importance of members in the SN, we <sup>fi</sup>rst provide a score, named m-Score. The higher the score is, the more important the member is. A data structure, named community tree, is de<sup>fi</sup>ned to represent the SN organizational structure.

De<sup>fi</sup>nition 1. (Community Tree): Let $P = \{ p _ { 1 } , . . . , p _ { \mathrm { k } } \}$ be a collection of members in an SN, CT be a tree, and NULL be the root of the tree, and every member in P be referred to as a node in the tree. Each member $p _ { \mathrm { i } }$ in CT it has a unique parent node $p _ { \mathrm { j } }$ where m-Score $( p _ { \mathrm { { j } } } ) > = m { - } S c o r e$ $\left( p _ { \mathrm { i } } \right)$ . If the parent node of ${ \dot { p } } _ { \mathrm { i } }$ is the root node NULL, $p _ { \mathrm { i } }$ is called a core of the tree. A core and its descendents compose a community.

To derive an SN's organizational structure, we calculate the m-Score for every member and then attempt to <sup>fi</sup>nd the immediate leader of every member in a network. Further, we draw the community tree using m-Score and subordinations.

After having constructed the SN community tree, we can discover communities and obtain the SN organizational structure. An example of a community tree is illustrated in Fig. 1 where node 1 and node 5 are cores of community 1 and community 2, respectively. The edges depict the subordination of two nodes, for example, node 1 is the immediate leader of node 2. Community 1 contains four nodes: 1, 2, 3 and 4.

To calculate the m-Score for every node, we need to investigate each node's importance in a network. Those nodes that link many important nodes are also themselves important. Such a process is very similar to PageRank algorithm [3]. PageRank is a link analysis algorithm that can produce a global “'importance”' ranking for every web page by analyzing links among web pages.

Unlike applying PageRank in an unweighted directed graph, we need to calculate the m-Score in a weighted undirected graph. We propose a modi<sup>fi</sup>ed PageRank algorithm to calculate the m-Score for every member in an SN.

![](/api/attachments/CWUTPRA9/fulltext/images/ef8bea8a629c80955fa49304791d0e3c906020feb7fd89fcf662211f3cb06257.jpg)  
Fig. 1. An example of a community tree.

SN is also regarded as a graph indicating information <sup>fl</sup>ows among members. The relationship of SN members can be obtained by analyzing information <sup>fl</sup>ows [13]. The process of determining SN information <sup>fl</sup>ow is similar to a random walk on a graph [8,18]. Given a graph and a starting point, the starting point's neighbor is selected at random, and the next start point is moved to this neighbor then a neighbor of this new start point is selected again at random and so on. The random sequence of points generated in this process is a random walk on the graph. Combining random walks with m-Score of every node, we can <sup>fi</sup>nd an immediate leader for every member in an SN. Then an SN community tree can be derived in this way. Our framework includes the following steps to derive the community tree:

(1) employ the modi<sup>fi</sup>ed PageRank to calculate m-Score for every node in an SN; and,

(2) combine random walk with m-Score of every node to derive a community tree.

## 3.2. Calculating m-Score

An algorithm for calculating the m-Score of members in a social network is described as follows.

Algorithm 1. Calculating m-Score for members: calcScore Input: social network G

Out: vector of m-Score for all members R

1. $R _ { 0 } {  } S$

2. Loop:

3. For each node $p _ { \mathrm { i } }$

$$
\mathrm{R} _ {\mathrm{k} + 1} [ \mathrm{i} ] = \frac {1 - d}{N} + d \sum_ {p _ {\mathrm{i}} \in M (p _ {\mathrm{i}})} W (p _ {\mathrm{ij}}) \frac {R _ {\mathrm{k}} [ j ]}{L (p _ {\mathrm{j}})}
$$

5. End

6. $e  \| R _ { \mathbf { k } } \| _ { 1 } - \| R _ { \mathbf { k } + 1 } \| _ { 1 }$

7. $R _ { { \bf k } + 1 }  R _ { { \bf k } + 1 } + e ^ { * } S$

8. $\delta \gets | | R _ { \mathrm { k } + 1 } - R _ { \mathrm { k } } | | _ { 1 }$

9. While $\left( \epsilon < \delta \right)$

10. normalize $\left( R _ { \mathrm { k + 1 } } \right)$

11. return $R _ { \mathrm { k + 1 } }$

In the calcScore, S is a start vector. Vector $R _ { \mathrm { k } }$ stores the m-Score of every member calculated in the kth iteration. $R _ { \mathrm { k } } [ \mathrm { i } ]$ is the m-Score of member $p _ { \mathrm { i } } ,$ , d denotes the damping factor, and N denotes the number of members. $M ( p _ { \mathrm { i } } )$ denotes the collection where members are associated with $p _ { \mathrm { i } } . L ( p _ { \mathrm { i } } )$ denotes the sum of weights for all edges associated with $p _ { \mathrm { j } } . W ( p _ { \mathrm { i j } } )$ is the weight of the edge linking $p _ { \mathrm { i } }$ and $p _ { \mathrm { j } } .$ Let $| | R _ { \mathrm { k } } | | _ { 1 }$ be the $L _ { 1 }$ norm of R. We can calculate the error of $| | R _ { \mathrm { k } } | | _ { 1 }$ and $| | R _ { \mathbf { k } + 1 } | | _ { 1 }$ , denoted as e, then calculate $R _ { \mathrm { k + 1 } }$ again using e. The iteration terminates when the $L _ { 1 }$ norm of $R _ { \mathrm { k + 1 } } - R _ { \mathrm { k } }$ is less than a preset threshold ε. After the values of $R _ { \mathrm { k + 1 } }$ is normalized to range [0, 1], the values indicate the <sup>fi</sup>nal m-Scores of members in the social network.

## 3.3. Deriving the community tree

A t-steps random walk on a graph sums the probabilities of all paths of length t between two nodes. It gives a measure of the volume of paths between the two nodes. The more paths between the two nodes, the higher will be the transition probability between the two nodes. A random walk can be one of two types, a forward random walk or a backward random walk. The forward random walk <sup>fi</sup>nds the probability of ending at node j when a t-step random walk starts at node k, denoted $P _ { \mathrm { t } | 0 } ( k | j )$ ). The backward random walk <sup>fi</sup>nds the probability of starting at node k when a t-step walk ended at node j, denoted $P _ { 0 | \mathrm { t } } ( k | j )$ . There exists a rule that ${ P _ { 0 | \mathrm { t } } ( k | j ) \propto P _ { \mathrm { t } | 0 } ( j | k ) P _ { 0 } ( k ) . P _ { 0 } ( k ) }$ is probability of choosing k as starting node.

Combined with the m-Score of every member, a random walk on the graph is applied to derive the community tree from an SN. In experiments, we <sup>fi</sup>nd the forward random walk to have a better performance than the backward random walk. Thus, we employ the forward random walk in our algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2. Deriving Community Tree: CT_Deriving
Input: Social network G
Output: Community Tree CT

1.  $CT \leftarrow [null, \ldots, null]$ 
2.  $A \leftarrow getOneStepTransMatrix(G)$ 
3.  $Z \leftarrow a$  diagonal matrix satisfied  $Z_{jj} = \sum_{i}[A^{t}]_{ij}$ 
4.  $M^{t} \leftarrow A^{t} * Z^{-1}$ 
5.  $R \leftarrow calcScore(G)$ ;
6. For each member  $p_{i}$  in R
7.  $k \leftarrow arg_{j} max \quad M^{t}[i][j]$ 
8. if  $R[k] &gt; R[i]$ 
9.  $CT[i] \leftarrow k$ 
10. End
11. Return CT
</div>

Function getOneStepTransMatrix(G) in step 2 calculates the onestep transition probability for each pair of nodes in an SN and then organizes the one-step transition probability as a matrix A, which is a row stochastic matrix satisfying $\textstyle \sum _ { \mathrm { j } } A _ { \mathrm { i j } } = 1 \ . \ A [ j ,$ k] is the one-step transition probability from node j to k.

$$
P _ {t + 1 | t} (k | j) = \left\{ \begin{array}{c} (1 - s) C _ {j k} / \sum_ {\mathrm{ij}} C _ {\mathrm{ji}} \forall k \neq j \\ s \quad k = j \end{array} \right.
$$

where s denotes the self-transition probability, and $C _ { \mathrm { j i } }$ denotes the weight of edge between node j and i. We derive a t-step transition probability matrix $M ^ { \mathrm { t } } { = } A ( A { \ldots } ( A ) )$ and normalize M<sup>t</sup> according to $\overset { \cdot } { M } { } ^ { \mathrm { t } } = A ^ { \mathrm { t } * } Z ^ { - 1 }$ , where Z is a diagonal matrix. With M<sup>t</sup>, we can <sup>fi</sup>nd the most likely ending node j by starting a t-step forward random walks at node i. If the m-Score of node j is much greater than that of node i, we regard j as the parent node of node i. After all the operations end, we obtain a community tree CT represented in an array where CT[i] indicates the parent node of node i. A null value of CT[i] indicates that there is no the immediate leader of node i. Hence node i is the core of community.

Node i and its descendents compose a community. The m-Score of each member shows the member's importance in the community. Descendents of a node present its power scope. The parent node of each node is its immediate leader.

## 4. Exploring evolution of the organizational structure in a dynamic social network

In Section 3, we develop the algorithms to derive a community tree from a static SN, which is called the static community tree. However, the static community tree does not do a good job in presenting the evolution of the organizational structure in the dynamic SN. Consider the following simplistic scenario in Fig. 2: We derive three static community trees A, B and C in three successive time periods $t _ { 1 } , t _ { 2 }$ and $t _ { 3 } ,$ respectively. During these periods, member n emerges in community trees A and C, but disappears from B. When we present the evolution of organizational structure with the three static community trees, it indicates that member n has exited from the organizational structure in time period $t _ { 2 } .$ However, it seems reasonable to expect n to remain a member of B, just as we cannot reliably assume that a user has exited from a web forum when the user did not access the forum in one time period. Hence, we need an evolving community tree that enables a smooth change between the two community trees. The evolving community tree is also a community tree that complies with De<sup>fi</sup>nition 1.

![](/api/attachments/CWUTPRA9/fulltext/images/07986d092a1ca3a14febfdb9d17c58b9e1b25a7a575f48adb1e13ff376f1f086.jpg)  
Fig. 2. Organizational structure evolution in a static community tree.

To present the evolution of organizational structure in a dynamic SN, we aggregate the change of an SN during different time periods, and then derive community trees. We further construct the evolving community tree from the two closest community trees. Hence, the evolving community tree can accurately present evolution of organizational structure over time.

The Best-<sup>fi</sup>rst search is a search algorithm which explores a graph by expanding the most promising node chosen according to a speci<sup>fi</sup>ed rule. Judea Pearl [24] described the Best-<sup>fi</sup>rst search as “estimating the promise of node n by a heuristic evaluation function f (n), which, in general, may depend on the description of n, the description of the goal, the information gathered by the search up to that point, and, most important, on any extra knowledge about the problem domain”.

Motivated by the idea of the Best-<sup>fi</sup>rst search, we propose a tree learning algorithm for our framework to derive the evolving community tree. The algorithm may generate a number of candidates in the process of deriving an evolving community tree. To select the vbest candidate, an evaluation function is needed. In Section 4.1, we de<sup>fi</sup>ne a scoring function to evaluate the candidate evolving community tree.

## 4.1. Scoring function

Let $D ( C T _ { \mathrm { i } } , { \cal C T } _ { \mathrm { j } } )$ denote the distance between the two community trees i and j. We use a function ES, in Eq. (1), as a scoring function, which measures distance errors among evolving community tree $C T _ { \mathrm { e } } ,$ previous period community tree $C T _ { \mathfrak { p } }$ and current period community tree $C T _ { \mathrm { { c } } }$ An optimal evolving community tree should satisfy minimum value in ES.

$$
E S = \sqrt {D (C T _ {\mathrm{c}} , C T _ {\mathrm{e}}) ^ {2} + D \left(C T _ {\mathrm{p}} , C T _ {\mathrm{e}}\right) ^ {2}}\tag{1}
$$

Tree edit distance [2] provides a measure of distance (similarity) between the two trees, de<sup>fi</sup>ned as the least cost of edit operation to change a tree to another tree. It can be employed to calculate $D ( C T _ { \mathrm { i } } ,$ CT ). Appendix provides a classical method for calculating the tree edit distance between two trees.

## 4.2. Tree learning algorithm

In our framework, we propose a tree learning algorithm to derive an evolving community tree from two static community trees. Deriving an evolving community tree is a process in which a community tree is reconstructed according to a scoring function, ES. It is uncertain that such an evolving community tree obtained from this process is a globally optimal solution, but in every step of the reconstruction, we can derive a locally optimal one. The reconstructing process is as follows:

(1) obtain a collection of members in the evolving community tree $P _ { \mathrm { c e } } { = } P _ { \mathrm { p r e } } { \cup } P _ { \mathrm { c s } }$ where $P _ { \mathrm { p r e } }$ and $P _ { { \mathrm { c } } s }$ are collections of members in the previous time period static community tree and current time periods one respectively;

(2) compute the m-Score for every member in the evolving community tree, $m { \cdot } S c o r e ( p _ { \mathrm { i } } ) = ( 1 - \alpha ) { \cdot } m { - } S c o r e ( p _ { \mathrm { i | p r e } } ) + \alpha { \cdot } m { - } S c o r e ( p _ { \mathrm { i | c s } } )$ where α is a smoothing factor. For those members that appear in the evolving community tree but not in the current community tree, if their m-Scores are less than a threshold ε, we regard them as retired members and remove them from the evolving community tree;

(3) according to the de<sup>fi</sup>nition of community tree, the m-Score of one node should not be larger than the m-Score of its parent node. Therefore, when reconstructing the evolving community tree, we <sup>fi</sup>rstly generate a root node NULL for the tree and then pick up members in a descending order of m-Score. In each iteration, we put one member under every node of the current evolving community tree respectively. Such a method can generate a collection of candidate evolving community trees. We choose the candidate having the minimum ES score as a solution in each iteration. After all the members are examined, an evolving community tree is derived.

## Algorithm 3. Learning evolving community tree: ECT\_Learning Input: Community Tree $C T _ { \mathrm { p r e } } , C T _ { \mathrm { c s } }$ Output: Evolving community tree $C T _ { \mathrm { e } }$

1. $P _ { \mathrm { c e } } {  } P _ { \mathrm { p r e } } { \cup } P _ { \mathrm { c s } }$

2. For each $p _ { \mathrm { i } }$ in $P _ { \mathrm { c e } }$

3. $m { \cdot } S c o r e ( p _ { \mathrm { i } } ) = ( 1 { - } \alpha ) { \cdot } m { \cdot } S c o r e ( p _ { \mathrm { i | p r e } } ) + \alpha { \cdot } m { \cdot } S c o r e ( p _ { \mathrm { i | c s } } )$

4. End

$$
P _ {\mathrm{ce}} \leftarrow P _ {\mathrm{ce}} - \left\{p _ {\mathrm{i}} \in P _ {\mathrm{ce}} - P _ {\mathrm{cs}} \mid m - S c o r e (p _ {\mathrm{i}}) <   \epsilon \right\}
$$

6. $C T _ { \mathrm { e } }$ ←build a community tree with only a root node

7. For each $p _ { \mathrm { i } }$ in $P _ { \mathrm { c e } }$ in m-Score descending order

8. CS←put $p _ { \mathrm { i } }$ under every node in $C T _ { \mathrm { e } }$ to generate a candidates collection

9. $\begin{array} { r l } { C T _ { \mathrm { t } }  \ a r g m i n } & { { } E S ( C T _ { \mathrm { i } } ) } \end{array}$

10. $\mathrm { | f \ E S ( } C T _ { \mathrm { t } } ) { > } \mathrm { E S ( } C T _ { \mathrm { e } } )$

11. $C T _ { \mathrm { e } } {  } C T _ { \mathrm { t } }$

12. End

13. Return $C T _ { \mathrm { e } }$

## 4.3. Exploring dynamic social network

After deriving a series of evolving community trees, we exploit these trees to discover the evolution path of the organizational structure and to study the properties of the dynamic SN.

We <sup>fi</sup>rstly de<sup>fi</sup>ne four types of relationships among communities to generate an evolution graph that represent evolution of the organizational structure:

De<sup>fi</sup>nition 2. (Relationships among communities and evolution graph):

Let $c _ { 1 } , c _ { 2 }$ be two communities in t-1 time period, and $c _ { 3 }$ and $c _ { 4 }$ be another two communities in time period $t ; n _ { 1 } , n _ { 2 } , n _ { 3 }$ and $n _ { 4 }$ be core of communities $c _ { 1 } , c _ { 2 } , c _ { 3 }$ and $c _ { 4 } ,$ respectively. There are four types of relationships among communities:

(1) splitting: If $n _ { 3 }$ and $n _ { 4 }$ are also members of $\dot { c } _ { 1 } ,$ we say that $c _ { 1 }$ split into $c _ { 3 }$ and $c _ { 4 } . c _ { 3 }$ and $c _ { 4 }$ are called the splitting entity of $c _ { 1 } ;$

(2) merging: $\operatorname { I f } n _ { 1 }$ and $n _ { 2 }$ are also members of $c _ { 3 } .$ , we say that $c _ { 1 }$ and $c _ { 2 }$ merged into $c _ { 3 } , c _ { 3 }$ is called the merging entity of $c _ { 1 }$ and c ;

(3) evolving: If $n _ { 1 }$ is a member of $c _ { 3 }$ and $n _ { 3 }$ is also a member of $c _ { 1 } ,$ we say that $c _ { 1 }$ evolved to $c _ { 3 } . c _ { 3 }$ is called the evolving entity of c ; and,

(4) emerging: If there is no core in time period t-1 appearing in $c _ { 3 } ,$ we say $c _ { 3 }$ is the emerging entity.

When using the four types of relationships to thread communities among the evolving community trees, we generate a graph which is called the evolution graph.

Fig. 3 provides examples to illustrate the relationships among communities. In Fig. 3(a), $c _ { 3 }$ and $c _ { 4 }$ are the splitting entities of $c _ { 1 } ,$ while $c _ { 3 }$ is also the emerging entity and $c _ { 4 } ~ .$ is the evolving entity of $c _ { 1 } .$ In Fig. $3 ( \mathsf { b } ) , c _ { 3 }$ is the merging entity of $c _ { 1 }$ and $c _ { 2 } . c _ { 3 }$ is also the evolving entity of c . In Fig. 3(c), c is the evolving entity of $c _ { 1 }$ because the core $\mathsf { o f c } _ { 3 } , n _ { 3 } ,$ is a member of $c _ { 1 }$ and the core of $c _ { 1 } , n _ { 1 }$ , is also member of $c _ { 3 } .$ . In Fig. 3(d), there is no any core of the community tree in t-1 appearing in $c _ { 3 } .$ Hence $c _ { 3 }$ is the emerging entity. The four types of relationships can well represent the evolution of communities over time. Fig. 6 is an example of evolution graph.

Combing evolution graph and dynamic SN properties, we can obtain insights into the dynamic SN. De<sup>fi</sup>nitions 3–5 de<sup>fi</sup>ne key properties of the dynamic SN.

De<sup>fi</sup>nition 3. (life-line): Let $C { = } \{ c _ { 1 } , . . . , c _ { \mathrm { n } } \}$ be a collection of communities. For each community $c _ { \mathrm { i } } \in C$ with i b $\Pi , C _ { \mathrm { i } + 1 }$ is the evolving entity of $c _ { \mathrm { i } } .$ . We say $\{ c _ { 1 } , . . . , c _ { \mathrm { n } } \}$ is a life-line of the community $c _ { 1 } .$ . Community $c _ { \mathrm { k } } \in C$ is called the entity of the life-line.

A life-line depicts an evolving process of one community in the dynamic SN.

De<sup>fi</sup>nition 4. (supporter): Given a life-line $C L { = } \{ c _ { 1 } , c _ { 2 } { , } . . . , c _ { \mathrm { n } } \}$ , we call the members as supporters of CL if they appear in CL not less than δ times with $\delta < = \mathtt { n }$

In De<sup>fi</sup>nition 4, δ is a parameter set by the user. If there is a life-line $C L { = } \{ c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } \}$ and $\delta = 3 ,$ that means only members appearing in the life-line not less than 3 times are supporters of CL. Exploring life-lines in the evolution graph and their supporters helps to better understand dynamic social networks. For example, we can discover the backbone of criminal group or detect loyal members in a forum over time.

De<sup>fi</sup>nition 5. (Activeness of community): Let node p be the core of community c, we use the m-Score of p to indicate the activeness of community c.

Activeness of community is a metric for the extent to which associations occur among members of the community over one period of time. We can use Activeness of community to reveal hot communities, which may re<sup>fl</sup>ect on-going hot topics in the forum or new activities in a criminal group.

## 5. Experiments

In this section, our framework is evaluated using both synthetic and real datasets. The performance of the proposed approach to discover communities is compared with the shortest-path betweenness method [23]. We also evaluate the capability of the approach on discovering organizational structure. The algorithms in our framework are implemented in Java. The experiments were conducted on a 1.8 GHz PC with Dual-Core Pentium 4 processor and 1 GB of RAM.

Shortest-path betweenness algorithm is intended to reveal edges with the highest betweenness, where betweenness is a measure that favors edges between communities and disfavors inside communities. The algorithm can <sup>fi</sup>nd the shortest paths between all pairs of vertices and count how many runs along each edge. The count will be referred to as the shortest-path betweenness. Thus the general form of using the shortest-path betweenness algorithm to <sup>fi</sup>nd communities is as follows:

(1) calculate betweenness scores for all edges in the network;

(2) <sup>fi</sup>nd the edge with the highest score and remove it from the network;

![](/api/attachments/CWUTPRA9/fulltext/images/580b0511f2dade8b6c3d8402e822993fe3dc8cb2b34a1d13bffd8458771608dc.jpg)  
Fig. 3. Relationships between communities.

(3) recalculate betweenness for all remaining edges; and,

(4) repeat from step 2.

## 5.1. Dataset

We evaluate the proposed framework on two datasets: a synthetic dataset and a karate club dataset [34]. To evaluate algorithm performance on discovering communities, we employ synthetic networks, which contain known communities, to conduct experiments, and compare the found communities to the known communities. We use the method proposed in [23] to generate the synthetic networks.

The karate club dataset represents a relationship network at a university karate club which consisted of 34 members. We use the karate dataset to evaluate the performance of our framework on <sup>fi</sup>nding organizational structure in static social networks. In Section $^ { 6 , }$ we will employ the proposed framework to explore the dynamic social network.

## 5.2. Experiments for finding communities

We have presented a framework for deriving the organizational structure from a social network. The framework can also be used for <sup>fi</sup>nding communities. We use a synthetic dataset to evaluate the performance of the CT\_Deriving algorithm for <sup>fi</sup>nding communities. Modularity proposed in [23] can evaluate the discovered communities from the SN. The greater the value of the modularity, the better the result. Hence our experiments employed the following modularity measure as a metric:

$$
Q = \sum_ {i} \left(e _ {\mathrm{ii}} - a _ {\mathrm{i}} ^ {2}\right) = T r e - \left\| e ^ {2} \right\|.\tag{2}
$$

Consider a particular division of a network into k communities. For a k\*k symmetric matrix $e ,$ let element $e _ { \mathrm { i j } }$ be the fraction of all edges in the network that link vertices in community i to vertices in community j. The row (or column) sums $a _ { i } = \textstyle \sum _ { j } e _ { i j }$ represent the fraction of edges that connect to the vertices in community i.

When we randomly generate a synthetic network using the method proposed in [23], some parameters must be chosen such as the number of vertices v, the number of communities $c ,$ the average number of edges for each vertex z, and the average number of edges linking one vertex outside communities zout.

We <sup>fi</sup>rst analyze how self-transition probability and the steps of a random walk impact performance of CT\_Deriving in <sup>fi</sup>nding communities. We set the parameters for this experiment as $\nu = 1 2 8 , c = 4 , z = 1 6 ,$ zout=4, with 32 members in every community. We randomly generated 100 networks. The random walk steps (steps in short) and self-transition probabilities (p in short) in the CT\_Deriving algorithm are set steps={10, 20…, 100}, p={0.8, 0.85, 0.87, 0.9, 0.92}. With each p value, we run CT\_Deriving on the 100 networks using each steps value. Then we calculate the average modularity score for the communities identi<sup>fi</sup>ed in the 100 networks. The results are illustrated in Fig. 4(a). It can be seen that under each p, the modularity increases while steps increase from 10, but the modularity decreases after attaining a peak. For p={0.8, 0.85, 0.87, 0.9, 0.92}, CT\_Deriving yields the greatest modularity on corresponding steps= {30, 40, 50, 70, 90} respectively.

We can conclude that increasing self-transition probability and random walk steps simultaneously can almost maintain algorithm performance unchanged. In Fig. 4(a), it can be seen that the modularity values are less than 0 at some points. This means that CT\_Deriving failed to <sup>fi</sup>nd signi<sup>fi</sup>cant communities at these points.

We continually analyze the performance of CT\_Deriving in <sup>fi</sup>nding communities. The parameters on generating synthetic networks are given as $\nu = 1 2 8 , c = 4 , z = 1 6 , z o u t = \{ 0 , . . . , 8 \}$ , there are 32 vertices on average in every community. We generate 100 networks under each zout. The experiment with parameter settings z=16, and zout=8 indicates that there are an average of 16 edges at every vertex in the generated network with eight of them linked to vertices in other communities, implying that the generated network does not contains a community structure. The experiment with parameter settings z=16, and zout=0 indicates that there do not exist edges among communities. Therefore, as the value of zout decreases, the generated networks will present a strong community structure. In another dimension, the parameters of CT\_Deriving are set as follows. The p values are p={0.8, 0.85, 0.87, 0.9, 0.92}, and the steps value corresponding to each p value are steps={30, 40, 50, 70, 90}. Under each p value with its corresponding steps value, we run CT\_Deriving on 100 networks generated on each zout value respectively. Then we calculate the average modularity score. The results are illustrated in Fig. 4(b). It can be seen that when zout is set between 0 and 4, we can get almost the same modularity on each p value. When zout is 5, the greater the p value is, the worse the performance is. When zout is 6, CT\_Deriving fails to <sup>fi</sup>nd any signi<sup>fi</sup>cant community with any p value. We do not illustrate modularity value when zout are 7 and 8 in Fig. 4 (b) and (c), because they are far less than 0.

The synthetic networks are generated by presetting parameters and labeling every vertex in the network with its community.

![](/api/attachments/CWUTPRA9/fulltext/images/81394747591b5f8a8e13f330ebf279a8c222675b6440e26f4dfa64cb8ef706f1.jpg)

(b)  
![](/api/attachments/CWUTPRA9/fulltext/images/5ef94ba36a576bce274467cf517255dd7cd9e2a83b087ffe937be7b35c39b858.jpg)

(c)  
![](/api/attachments/CWUTPRA9/fulltext/images/5732781db7d5d521b7c875f5a67a0e6cc02315d60a4819d005c52eaa6660bb30.jpg)  
Fig. 4. Experiments for <sup>fi</sup>nding communities. (a) Evaluating parameter p and steps of CT\_Deriving. (b) Performance of CT\_Deriving in looking for communities. (c) Comparison of CT\_Deriving, shortest-path betweenness and best value.

Therefore, we can calculate the modularity for communities on the synthetic network and identify the highest modularity. The curve best in Fig. 4(b) and (c) illustrates the highest modularity. We pick up the highest modularity under <sup>fi</sup>ve p values in Fig. 4(b) to represent the performance of CT\_Deriving. Fig. 4(c) illustrates the performance of CT\_Deriving and shortest-path betweenness [23]. We observe that when zoutb=5, CT\_Deriving demonstrates almost the best performance where the standard error between CT\_Deriving and best is 0.034. CT\_Deriving gets better performance than shortest-path betweenness except at the point that zout=6.

From the discussion above, we conclude that CT\_Deriving performs well in identifying communities from networks having a community structure. In this paper, we focus on how the con<sup>fi</sup>gurable parameters affect community <sup>fi</sup>nding. The details in optimizing the parameters are beyond the scope of this paper and remain for the future research.

## 5.3. Experiments for finding organizational structure

We employ the karate dataset, shown in Fig. 5(a), to evaluate the performance of CT\_Deriving. The karate dataset was collected by Zachary [34] from a university-based karate club, where there was an on-going con<sup>fl</sup>ict between the club president, John A., and Mr. Hi, a part-time karate instructor, over the price of karate lessons. Mr. Hi, who wished to raise prices, claimed his authority to set his own lesson fees, since he was the instructor. John A., who wished to stabilize prices, claimed the authority to set the lesson fees since he was the club's chief administrator. As time passed the entire club became divided over this issue, and the con<sup>fl</sup>ict was translated into ideological terms by most club members. A factional division led to a formal separation of the club into two organizations.

The karate dataset, illustrated in Fig. 5(a), contains 34 members in the karate club. An edge is drawn if two individuals were consistently observed to interact outside the normal activities of the club (karate classes and club meetings). Node 1 and 34 denote Mr. Hi and John A. respectively. Nodes denoted using circles belong to the faction of John A. and nodes denoted using squares belong to the faction of Mr. Hi.

We employ CT\_Deriving algorithm to explore the organizational structure in the karate club dataset. The derived organizational structure is illustrated in Fig. 5(b)–(d) when parameter step is 50, and p is 0.85, 0.87 and 0.92 respectively. It can be seen that only one community is found when p is 0.85 where node 1 is the immediate leader of the other <sup>fi</sup>fteen nodes, but node 1 is under the leadership of node 34. When p increases to 0.87, two communities are identi<sup>fi</sup>ed that are the same as the results in [23]. The organizational structure of communities is formed in a <sup>fl</sup>at structure where node 1 and node 34 are leaders, respectively. When p increases to 0.92, the two communities are further expanded toward a hierarchical structure where node 25 and 26 are under the leadership of node 32, and node 17 is under the leadership of node 7. The organizational structure remains unchanged when p is greater than 0.92.

Fig. 5(d) shows that the proposed approach discovered two organizations from the dataset. We observe that the obtained organizational structure well maps the real-world organizational structure. The leaders of the derived organizations node 1 and 34 are the real-world leaders of the two factions, Mr. Hi and John A. Members in the derived organizations also completely come into line with the two real-world factions. Zachary did not provide more information about organization structure in the karate club dataset. However, Fig. 5(d) indicates that the immediate leader of node 17 is node 7 and the immediate leader of nodes 25 and 26 is node 32.

Although the experiments demonstrate that the derived organi zational structure does a good job of mapping to the real-world one when p is 0.92, this does not mean that 0.92 is the best value of selftransition probability. Another value certainly might be superior in a different context. In this experiment, we analyzed how parameters affect the exploration of organizational structure. We cannot determine which parameter value helps in obtaining the optimal solution because different parameters provide different views of the organizational structure.

## 6. Exploring evolution of the organizational structure in Enron in 2001

Several researchers [5,9,20] have analyzed the Enron e-mail data set to provide insights into the Enron Corporation (Enron) since the case of Enron caught the public attention. Diesner et al. [9] and

![](/api/attachments/CWUTPRA9/fulltext/images/bf25415c3ab11dadf86c61f05f9514c10093b3769ecabb5787ebd522e93481d8.jpg)  
Fig. 5. Illustrated Karate dataset (a) and organizational structure in Karate when p = 0.85 (b), p = 0.87 (c), and p = 0.92 (d).

Chapanond et al. [5] investigated the structure and properties of the network constructed from the Enron corpus, and then mapped the changes of the structure and properties of the network to the events within Enron. McCallum et al. [20] applied the Author-Recipient-Topic (ART) model to the Enron e-mail corpus and derived key topics from the corpus. They then studied the roles of users in accordance with speci<sup>fi</sup>c topics. Because the Enron e-mail corpus only contains e-mails among a portion of the employees at Enron, it is clear that any analysis on the corpus cannot present all perspectives of Enron. In this section, we apply our framework to explore the evolution of organizational structure in the Enron corpus in seeking a clear understanding of the incidents in Enron during a speci<sup>fi</sup>c time period.

The Enron e-mail corpus was made public by the Federal Energy Regulatory Commission during its investigations and subsequently made it available. The Enron e-mail corpus can be converted into an SN, in which a vertex represents a user, an edge stands for the communications between two users, and a weight on the edge indicates the number of communications. The original Enron dataset contains 517,432 e-mail documents collected from 150 employees in the Enron company. After preprocessing, 148 unique users are identi<sup>fi</sup>ed. We assign every user an ID. When only picking up e-mail documents communicated among the 148 users, 58,875 e-mail records are included.

We derived twelve social networks from the preprocessed Enron dataset by aggregating communications among users in each month in 2001 and then obtained twelve static community trees. We employed ECT\_Learning to generate eleven evolving community trees (see Fig. 8) with the smoothing parameter α=0.5 and the threshold parameter ε=0.01.

Employing relationships among communities in De<sup>fi</sup>nition 2, we threaded communities in the evolving community trees. This yielded an evolution graph (see Fig. 6), which presents the evolution of the organizational structure in Enron in 2001. Each node denotes a community. We used the ID of core as the ID of the community.

Communities in Fig. 6 and organizational structures in Fig. 8 present the discovered communities and the organizational structure. We know that they do not always re<sup>fl</sup>ect the true situation because we obtain the organizational structure by relying only on Enron e-mails over a speci<sup>fi</sup>c period of time. Communications among members also may <sup>fl</sup>uctuate in different time periods and the dataset may contain noises. Hence, if we explore the organizational structure over a long time period, we may obtain more accurate and precise pictures of the context in Enron.

In Section 6.1, we use life-line, supporter and hot community (see De<sup>fi</sup>nitions 3–5) to obtain a clearer and more accurate view of Enron.

## 6.1. Long life-line and supporters

In general, we can obtain many life-lines from the evolution graph of a dynamic SN. However, exploring long life-line nodes and their supporters can help to better understand the dynamic SN.

By analyzing Fig. 6, we obtain the four longest life-lines and their supporters in the Enron dataset from 2001, shown in Table 1. Community c<sup>m</sup> in Table 1 denotes community n in mth month. Parameter δ in De<sup>fi</sup>nition 4 (supporter) is set at δ = length of life-lines− 1. We list the average number of members (size) in each community in life-lines. The values, calculated in ratio of the number of supporters and the size, named stability, are listed as well. The stability indicates the extent to which members change in a life-line of community. High stability means that members have a small change.

Table 1 shows that the top ranked life-line (Community c<sup>1</sup> ) has a 12 months life. This suggests that its supporters have a greater loyalty than supporters of other life-lines. However, Community 20 is a loose group in its evolution since its stability is the lowest. Community $c _ { 1 4 4 } ^ { 6 }$ has the second longest life-line (seven months), but far higher stability than Community $c _ { 2 0 } ^ { 1 } .$ We say that $c _ { 1 4 4 } ^ { 6 }$ has a much more solid structure than $c _ { 2 0 } ^ { 1 }$ in its evolution. We infer that Community $c _ { 1 4 4 } ^ { 6 }$ probably maps a real organization and $c _ { 2 0 } ^ { 1 }$ is a virtual organization formed because of a single target owned by members. Our guess could be validated (or invalidated) by analyzing contents of e-mails. $c _ { 2 0 } ^ { 1 }$ is a virtual organization formed in processing the California Electricity Crisis. $c _ { 1 4 4 } ^ { 6 }$ is a sale team of Enron in Portland during 2001.

![](/api/attachments/CWUTPRA9/fulltext/images/e26de8e07c44043fe2f667bf45f0c33f8c6ae61d7e0496c2c67c9dec09954be4.jpg)  
Fig. 6. Evolution of communities in Enron in 2001.

Table 1 The longest life-line.

<table><tr><td>Rank</td><td>Life-line</td><td>Supporters</td><td>Size</td><td>Stability</td></tr><tr><td>1</td><td>Community  $c_{20}^{1}$   $\{c_{20}^{1}, c_{20}^{2}, c_{20}^{3}, c_{20}^{4}, c_{20}^{5}, c_{20}^{6}, c_{20}^{7}, c_{20}^{8}, c_{8}^{9}, c_{8}^{10}, c_{41}^{11}, c_{61}^{12}\}$ </td><td>12,20,24,57,64,108,116</td><td>73.4</td><td>0.095</td></tr><tr><td>2</td><td>Community  $c_{144}^{6}$   $\{c_{144}^{6}, c_{144}^{7}, c_{144}^{8}, c_{144}^{9}, c_{144}^{10}, c_{144}^{11}, c_{144}^{12}\}$ </td><td>18,34,42,67,82,106,109,113,119,121,131,144</td><td>14.8</td><td>0.81</td></tr><tr><td>3</td><td>Community  $c_{55}^{1}$   $\{c_{55}^{1}, c_{55}^{2}, c_{55}^{3}, c_{124}^{4}, c_{114}^{5}, c_{114}^{6}\}$ </td><td>5,25,47,55,87,114,124,132,143</td><td>14.3</td><td>0.63</td></tr><tr><td>4</td><td>Community  $c_{7}^{1}$   $\{c_{7}^{1}, c_{13}^{2}, c_{13}^{3}, c_{4}^{4}\}$ </td><td>7,13,49,126</td><td>4.75</td><td>0.84</td></tr></table>

From Section 6.1, we can assert that those communities with long life-line and great stability are corresponding to a real organization.

## 6.2. Hot communities

An analyst might be interested in investigating “hot communities in an SN”, communities that might be related to important events. For example, if a hot community is a criminal group, it is perhaps likely that the group is plotting a new criminal plan. According to Activeness of community (see De<sup>fi</sup>nition 5), hot communities generally have more activities. We plot a chart in Fig. 7 to examine the Activeness of Communities in Enron during 2001, in which each circle represents a community contained in Fig. 6. Its position in the y-axis in the chart corresponds to the community's activeness level.

Combining Figs. 6 and 7, we can easily identify life-line and hot communities. Community c<sup>1</sup> and the entities in its life-line maintain a high level of activeness. We wonder what are behind the phenomenon. By analyzing the contents of the e-mails in the 2001 Enron dataset, we learn that the community $c _ { 2 0 } ^ { 1 }$ and the entities in its lifeline are very closely related to the California Electricity Crisis (CEC). Because of the high activeness value of the life-line of $c _ { 2 0 } ^ { 1 } ,$ we can infer that Enron had a high involvement in the crisis in 2001, which matches the context of the company during the period. One book “The California Electricity Crisis: Causes and Policy Options” (http://www. ppic.org/content/pubs/report/R\_103CWR.pdf) gives a detailed introduction to the CEC that lasted from 2000 to 2002, verifying that Enron played an important role in the crisis.

In Fig. 7, we see that the hottest communities in January, February and March do not have a 1.0 activeness level because, in the three months, the communities with a 1.0 activeness level only had one member. Therefore, we treat these communities as outliers.

Adibi (University of Southern California) provided a document that contains the status of Enron employee in 2001 (dataset used to be available in http://www.isi.edu/\~adibi/Enron/Enron\_Employee\_Status. xls). In the document, Member 20, dasovich-j, was a Government Relation Executive, and member 8, beck-s, was Chief Operating Of<sup>fi</sup>cer. In the organizational structure derived by our framework (Fig. 8), dasovich-j was the core of his/her community and beck-s was under the leadership of dasovich-j for a large part of the dataset period. Obviously, the derived organizational structure would not seem to line up with the real one. However, we suggest that dasovich-j was serving as an agent, whom the real leader had authorized to perform certain tasks. This has been veri<sup>fi</sup>ed by analyzing the contents of Enron e-mail corpus. Therefore, our framework can obtain new insights regarding an organization.

Community $c _ { 1 4 4 } ^ { 6 }$ and the entities in its life-line are also a hot community. By analyzing the contents of e-mails, we learn that it was a sale team of Enron in Portland during 2001. The core of the community, member 144 (Williams-w3), was a real leader of the team. Its high activeness for a long time may indicate that the team was working hard for the business.

From Sections 6.1 and 6.2, we can draw a conclusion that the cores in an organizational structure, in general, are either the leaders of the real organization or the agents of the leaders.

By using the proposed framework to analyze the Enron corpus, we discovered both real and virtual organizations in Enron. Community $c _ { 2 0 } ^ { 1 }$ (and its entities) in Table 1 is a virtual organization which was formed for dealing with California Energy Crisis. Community $c _ { 1 4 4 } ^ { 6 }$ (and the entities) is a real organization in Enron with signi<sup>fi</sup>cant business activity. We also derived the backbone of the two organizations. We found that dasovich-j plays a role of agent in the virtual organization.

![](/api/attachments/CWUTPRA9/fulltext/images/312acc65b8e41424b829700cd5b47f963d9bb009afc05a591175cf99453ce2ad.jpg)  
Fig. 7. Activeness levels of Enron communities during 2001.

![](/api/attachments/CWUTPRA9/fulltext/images/d8d51a4e3d75b5c537e88c21f15be48cd8207d908d1636b3ce40acc1b621e3e8.jpg)  
Fi<sub>g.</sub> 8<sub>.</sub> The evolvin<sub>g</sub> communit<sub>y</sub> trees derived from the Enron e-mails cor<sub>p</sub>us

## 7. Conclusion

Exploring organizational structure in a dynamic SN has a broad range of applications, such as monitoring the dark web and improving performance of viral marketing. In this paper, we present our research effort in applying the concept of organizational structure in social network analysis to obtain a better understanding of dynamic SN. We formalized a community tree data structure for the purpose of presenting the SN organizational structure, and proposed a framework for exploring the SN organizational structure in a dynamic setting. The framework is composed of three main parts: (1) an approach to combining PageRank and Random Walks on a graph representation for deriving a community tree from an SN; (2) a tree learning algorithm, which employs the tree edit distance as a scoring function, to generate the evolving community tree; and, (3) an approach for presentation of the evolution of the organizational structure and investigation of characteristics of a dynamic SN.

In the <sup>fi</sup>rst stage, we conducted experiments on the synthetic dataset and real dataset. This demonstrated that the proposed framework performs better than the shortest-path betweenness in the community structure discovery of social networks. The experiments also show that the framework can well present the organizational structure of an SN. As an open research issue, presently, we do not analyze which parameter can yield optimal solutions. This effort is beyond the scope of this paper.

In the second stage, we applied the framework to the study of the 2001 Enron dataset. We obtained the following interesting <sup>fi</sup>ndings: (1) those communities with long life-line and great stability likely correspond to a real organization; and (2) the cores in an organizational structure, in general, are either the top leaders of real organizations or the agents of these leaders. Although it is possible that the organizational structure discovered from an SN do not perfectly come in line with a real organization, the framework may help reach new understandings of the organization.

In learning an evolving community tree, we employ tree edit distance as the scoring function. However, the high complexity of the tree edit distance algorithm results in heavy time overhead in exploring the evolution of organizational structure. In the future, we plan to improve ef<sup>fi</sup>ciency of our framework and the algorithms as well. In addition, we will employ topic analysis techniques using the textual data available in an SN. The textual information and the new technical ingredients are expected to reinforce automatic content analysis of e-mail corpus.

## Acknowledgements

The authors gratefully acknowledge the constructive comments and suggestions of three anonymous referees as well as those from Dr. James R. Marsden.

This work was supported by the Humanities and Social Science Foundation for the Youth Scholars of Ministry of Education of China (No. 09YJCZH101) and the Scienti<sup>fi</sup>c Research Fund of Southwestern University of Finance and Economics, China (No. 09XG058).

Appendix A. A classical method for calculating the tree edit distance between two trees

Let v $( a _ { 1 } , . . . , a _ { \mathrm { T } } )$ be a tree, v be a root node, and $a _ { 1 } , . . . , a _ { \mathrm { T } }$ be subtrees. Every node of a tree is labeled a symbol. We denote by L the set of labels and by $\lambda \not \in L$ the empty label. A labeled tree v $( a _ { 1 } , . . . , a _ { \mathrm { T } } )$ is denoted by $l \ ( a _ { 1 } , . . . , \ a _ { \mathrm { T } } )$ . There are three main edit operations on the trees: 1)substitution of the label l of a tree (or subtree) root by l′ (denoted as $( l , l ^ { \prime } ) ) , 2 )$ deletion of a subtree a (denoted as $\left( a _ { \mathrm { i } } , \lambda \right) )$ and 3) insertion of a subtree $a _ { \mathrm { j } }$ (denoted as $\left( \lambda , a _ { \mathrm { j } } \right) )$

Let $\delta _ { \mathrm { t } }$ denote a cost function over edit operations, and δ a cost function over one step edit operation $\delta = ( L \cup \{ \lambda \} ) \times ( L \cup \{ \lambda \} ) ^ { 2 } \backslash \{ ( \lambda , \lambda ) \}$ Hence the cost of deletion operation of a tree is

$$
\delta_ {t} (l (a _ {1}, \dots , a _ {T}), \lambda) = \delta (l, \lambda) + \sum_ {i = 1} ^ {T} \delta_ {t} (a _ {i}, \lambda).
$$

Similarly, the cost of a tree insertion is

$$
\delta_ {t} \left(\lambda , l ^ {\prime} \left(b _ {1}, \dots , b _ {V}\right)\right) = \delta \left(\lambda , l ^ {\prime}\right) + \sum_ {j = 1} ^ {V} \delta_ {t} \left(\lambda , b _ {j}\right).
$$

The substitution of two labels is de<sup>fi</sup>ned as $\delta _ { t } ( l , l ^ { \prime } ) = \delta ( l , l ^ { \prime } )$

Let $x , y$ be two trees. Edit script $e = \{ e _ { 1 } , . . . , e _ { \mathrm { n } } \mid e _ { \mathrm { i } } = \delta = ( L \cup \{ \lambda \} ) \times$ $( L \cup \{ \lambda \} ) ^ { 2 } | \{ ( \lambda , \lambda ) \} \}$ is a sequence of edit operations that change x to y. A cost of edit script is the sum of all costs of edit operations. Since several scripts may exist when changing x to $y ,$ tree edit distance between two trees can be de<sup>fi</sup>ned as the cost of minimum cost edit script, which can be recursively computed as follows.

$$
\begin{array}{l} D (\lambda , \lambda) = 0 \\ D (l (a _ {\mathrm{i}},..., a _ {\mathrm{T}}), \lambda) = \delta_ {\mathrm{t}} (l (a _ {\mathrm{i}},..., a _ {\mathrm{T}}), \lambda) \\ D (\lambda , l ^ {\prime} (b _ {\mathrm{i}},..., b _ {\mathrm{V}})) = \delta \mathrm{t} (\lambda , l (b _ {\mathrm{i}},... b _ {\mathrm{V}})) \\ D (l (a _ {\mathrm{i}},..., a _ {\mathrm{T}}), l ^ {\prime} (b _ {\mathrm{i}},... b _ {\mathrm{V}})) = \delta (l, l ^ {\prime}) + D ^ {\prime} (a _ {1},..., a _ {\mathrm{T}}: b _ {1},..., b _ {\mathrm{V}}) \end{array}
$$

$$
\begin{array}{l} D ^ {\prime} (\lambda : \lambda) = 0 \\ D ^ {\prime} (a _ {1},..., a _ {T}: \lambda) = D ^ {\prime} (a _ {1},..., a _ {T - 1}: \lambda) + \delta_ {t} (a _ {T}, \lambda) \\ D ^ {\prime} (\lambda : b _ {1},..., b _ {V}) = D ^ {\prime} (\lambda : b _ {1},..., b _ {V - 1}) + \delta_ {t} (\lambda , b _ {V}) \end{array}
$$

$$
D ^ {\prime} (a _ {1},..., a _ {T}: b _ {1},..., b _ {V}) =   m i n \left\{ \begin{array}{l} D ^ {\prime} (a _ {1},..., a _ {T - 1}: b _ {1},..., b _ {V}) + \delta_ {t} (a _ {T}, \lambda) \\ D ^ {\prime} (a _ {1},..., a _ {T}: b _ {1},..., b _ {V - 1}) + \delta_ {t} (\lambda , b _ {V}) \\ D ^ {\prime} (a _ {1},..., a _ {T - 1}: b _ {1},..., b _ {V - 1}) + \delta_ {t} (a _ {T}, b _ {V}) \end{array} \right.
$$

## References

[1] E. Bertino, E. Ferrari, V. Alturi, The speci<sup>fi</sup>cation and enforcement of authorization constraints in WFMS, ACM Transactions on Information and System Security 2 (1) (1999) 65–104.

[2] P. Bille, A survey on tree edit distance and related problems, Theoretical Computer Science 337 (1–3) (2003) 217–239.

[3] S. Brin, L. Page, The anatomy of a large-scale hypertextual web search engine Computer Networks and ISDN Systems 30 (1–7) (1998) 107–117

[4] Kathleen M. Carley, Jana Diesner, Jeffrey Reminga, Maksim Tsvetovat, Toward an interoperable dynamic network analysis toolkit, Decision Support Systems 43 (2007) 1324–1347.

[5] Anurat Chapanond, Mukkai S. Krishnamoorthy, Bulent Yener, Graph theoretic and spectral analysis of Enron e-mail data, Computational & Mathematical Organiza: tion Theory 11 (2005) 261–281.

[6] C. Chekuri, A. Goldberg, D. Karger, M. Levin, C. Stein, Experimental study of minimum cut algorithms, The Proceedings of the 8th SAIM Symposium on Discreet Algorithm, 1997, pp. 324–333.

[7] Aaron Clauset, Cristopher Moore, M.E.J. Newman, Hierarchical structure and the prediction of missing links in networks, Nature 453 (2008) 98–101.

[8] Nick Craswell, Martin Szummer, Random walks on the click graph, The Proceedings of the 30th Annual International ACM SIGIR Conference, 2007, pp. 239–246.

[9] Jana Diesner, Terrill L. Frantz, Kathleen M. Carley, Communication network from the Enron e-mail corpus “It's always about the people. Enron is no different”, Computational & Mathematical Organization Theory 11 (2005) 201–228.

[10] C. Ding, X. He, H. Zha, M. Gu, H. Simon, A min–max cut algorithm for graph partitioning and data clustering, The Proceedings of the 2001 IEEE International Conference on Data Mining, 2001, pp. 107–114.

[11] Amit Goyal, Francesco Bonchi, Laks V.S. Lakshmanan, Discovering leaders from community actions, The proceedings of 17th ACM conference on Information and knowledge management, 2008, pp. 499–508.

[12] Marko Grobelnik, Dunja Mladenic, Blaz Fortuna, Semantic technology for capturing communication inside an organization, Semantic Technologies (JULY/AUGUST 2009) 59–67.

[13] D. Gruhl, R. Guha, D. Liben-Nowell, A. Tomkins, Information diffusion through blogspace, The Proceedings of the 13th international conference on World Wide Web 2004 pp.491-501

[14] L. Hagen, A.B. Kahng, New spectral methods for ratio cut partitioning and clustering JEEE Transactions on Computed Aided Design 11 (9) (1992) 1074–1085.

[15] Ravi Kumar, Jasmine Novak, Andrew Tomkins, Structure and evolution of online social networks, The Proceedings of the 12th ACM SIGKDD Internationa Conference on Knowledge Discovery and Data Mining, 2006, pp. 611–617.

[16] Huajing Li, Zaiqing Nie, Wang-Chien Lee, C. Lee Giles, Ji-Rong Wen, Scalable community discovery on textual data with relations, The Proceedings of 17th ACM conference on Information and knowledge management, 2008, pp. 1203–1212.

[17] Bo Long, Xiaoyun Wu, Zhongfei (Mark) Zhang, Community learning by graph approximation, The proceedings of 7th IEEE International Conference on Data Mining, 2007, pp. 232–241.

[18] L. Lovasz, Random walks on graphs: a survey, Bolyai Society Mathematical studies 2 (1993) 1–46.

[19] Hao Ma, Haixuan Yang, Michael R. Lyu, Irwin King, Mining social networks using heat diffusion processes for marketing candidates selection, The proceedings of 17th ACM conference on Information and knowledge management, 2008, pp. 233–242.

[20] Andrew McCallum, Xuerui Wang, Topic and role discovery in social networks with experiments on Enron and academic e-mail, Journal of Arti<sup>fi</sup>cial Intelligence Research 30 (2007) 249–272.

[21] M. zur Muhlen, Organizational management in work<sup>fl</sup>ow applications issues and perspectives, Information Technology and Management 5 (3) (2004) 271–291.

[22] M.E.J. Newman, Fast algorithm for detecting community structure in networks, Physical Review E 69 (2004) 066133.

[23] M.E.J. Newman, M. Girvan, Finding and evaluating community structure in networks, Physical Review E 69 (2) (2004) 1–15.

[24] J.J. Pearl, Heuristics: Intelligent Search Strategies for Computer Problem Solving Addison-Wesley, 1984, pp. 48–59.

[25] J.P. Scott, Social Network Analysis: a Handbook, SAGE Publications, 2000.

[26] J. Shi, J. Malik, Normalized cuts and image segmentation, IEEE Transactions on Pattern Analysis and Machine Intelligence 22 (8) (2000) 888–905.

[27] Minseok Song, Wil M.P. van der Aalst, Towards comprehensive support for organizational mining, Decision Support Systems 46 (2008) 300–317.

[28] Lei Tang, Huan Liu, Jianping Zhang, Zohreh Nazeri, Community evolution in dynamic multi-mode networks, The Proceedings of 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2008, pp. 677–685.

[29] C. Tantipathananandh, Tanya Berger-Wolf, David Kempe, A framework for community identi<sup>fi</sup>cation in dynamic social networks, The Proceedings of 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2007, pp. 717–726.

[30] Andrew Y. Wu, et al., Mining scale-free networks using geodesic clustering, The Proceedings of 10th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2004, pp. 719–724.

[31] Jennifer J. Xu, Hsinchun Chen, Fighting organized crimes: using shortest-path algorithms to identify associations in criminal networks, Decision Support Svstems.38 (2004).473-487.

[32] J. Jennifer Xu, Hsinchun Chen, CrimeNet explorer: a framework for criminal network knowledge discovery, ACM Transactions on Information Systems 23 (2) (2005) 201–226.

[33] Xiaowei Xu, Nurcan Yuruk, Zhidan Feng, Thomas A.J. Schweiger, SCAN: a structural clustering algorithm for networks, The Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2007, pp. 824–833.

[34] W.W. Zachary, An information <sup>fl</sup>ow model for con<sup>fl</sup>ict and <sup>fi</sup>ssion in small groups, Journal of Anthropological Research 33 (1977) 452–473.

[35] Ding Zhou, Eren Manavoglu1, Jia Li, C. Lee Giles, Zha Hongyuan, Probabilistic models for discovering e-communities, The Proceedings of the 15th international conference on World Wide Web, 2006, pp. 173–182.

[36] Ding Zhou, Isaac Councill, Hongyuan Zha, C. Lee Giles, Discovering temporal communities from social network documents, The Proceedings of 7th IEEE International Conference on Data Mining, 2007, pp. 745–750.

![](/api/attachments/CWUTPRA9/fulltext/images/25a042c43d0c51e8d333f410000656ddc6c29ee55630611512b9fda3f0b4212b.jpg)

Dr. Jiangtao Qiu is an associate professor in the School of Information at the Southwestern University of Finance and Economics, China. He received his Ph.D degree in Computer Science from Sichuan University, China in 2008. His research interest include data mining, social network analysis and business intelligence

![](/api/attachments/CWUTPRA9/fulltext/images/d75bf224fa234a053540e3beb07ede4192c21b211dc6092ea9881141a423a321.jpg)

Dr. Zhangxi Lin is an associate professor at the Rawls College of Business Administration, and a codirector of Center for Advanced Analytics and Business Intelligence, at Texas Tech University. He received his <sup>fi</sup>rst master's degree in computer science in 1982 from Tsinghua University, and another master's degree in economics in 1996 from the University of Texas at Austin. He earned his Ph.D. degree in information systems in 1999 from the University of Texas at Austin. Zhangxi Lin’s research interests include data communications, business intelligence, electronic commerce, and knowledge-based system. In the last ten years, he has published more than a hundred papers in internationally refereed journals and conferences. Zhangxi

Lin is a member of IEEE Computer Society, Association of Information Systems, and INFORMS.

Contact information: Phone: +1-806-742-1926, Fax: +1-806-742-3193

E-mail: zhangxi.lin@ttu.edu
