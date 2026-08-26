---
otero_id: 4136
otero_key: "QRURKKX4"
title: "Network projection-based edge classification framework for signed networks"
authors: "Mukul Gupta; Rajhans Mishra"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113321"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Network projection-based edge classification framework for signed networks

Mukul Gupta, Rajhans Mishra

Indian Institute of Management Indore, Information Systems Area, Indore, India

A R T I C L E I N F O

Keywords: Signed network Edge classification Spanning subgraph projection

## A B S T R A C T

Many real-world networks have signed relationships between the nodes. Identification of these relationships is an important aspect of decision making, The existing signed relationships in a network may impact the relationships between the other nodes, hence learning from the existing signed relationships in a network can be used for decision making in various mining tasks. These signed networks are getting attention in recent vears due to their relevance to many applications such as categorization, recommendation, and relationship discovery in various domains for decision support such as biological, social network analysis, communication and making knowledge graphs. In this work, we focus on edge classification (sign/label prediction for edges) in unweighted and undirected signed networks where the task is to predict the label of the unlabeled edges. Edge classification is a challenging problem as in real-world signed networks, edges are scarcely labeled. In our work, we are using labeled edges to predict the sign of unlabeled edges (classification) with the help of structural information. In this work, we have proposed a novel framework named NPECF for the classification of unlabeled edges. The proposed framework is novel in its way of utilizing the existing information in the signed network to predict the label of unlabeled edges. The utilization of the unlabeled edges in NPECF using three spanning subgraph projections of the given network minimizes the information loss. The experiments have been performed on four realworld datasets from diferent domains to demonstrate the efectiveness of the proposed framework.

## 1. Introduction

With the existence of many signed real-world networks, the prediction of signs of edges has become a very important and valuable decision-making problem as it can help to unfold the potential of real world networks. Signed real-world networks in diferent domains exist, such as biology, social network, and communication where the users/ objects have a positive or negative relationship with each other. Many times, network structures are not very rich in terms of existing re lationship information, still, prediction of sign of unlabeled relationships is required to support the decision-making process in various applications like categorization, recommendation, and relationship discovery [7,19] and knowledge graphs [16]. Besides that, the knowledge graph is being used as a tool for the development of the semantic web. The knowledge graph primarily explores the node and edge network for identifying the relationship between the entities.

Classification of relationships in signed networks has significant managerial implications [1,14]. A positive-labeled edge in signed networks represents the friendship, trust, love or support while a negative labeled edge represents the enmity, distrust, hate or oppose [1,14]. These signed networks are prevalent and exist in many real-world domains and classification of relationships between users/nodes can add a great value to decision making. For example, Epinions,<sup>1</sup> a review website, can be used by users to like or dislike reviews of other users [14]. The network of US senators and their positive and negative relationships inferred from co-sponsorship data [3] is another example of a signed network in the social network domain. In the biology domain, Bornholdt [5] used a signed network to give the simplified representation of the yeast regulatory network where interactions are classified into the two types i.e. activated (positive relationship) or repressed (negative relationship).

Diferent mining tasks can be performed on signed networks to get rich insights. In this work, our focus is on the problem of edge classification (sign/label prediction for edges) for signed networks. In the edge classification problem, the task is to classify unlabeled edges as either a positive-labeled edge or negative-labeled edge in the network [15,18]. The problem of node classification is a well-known and wellexplored problem [1,20]. However, the edge classification problem in a signed network is very challenging and it is relatively less explored as compared to node classification problem [1]. For real-world signed networks, manually labeling of the edges could be a daunting task due to the high cost involved in terms of time and efort. Therefore, we can utilize the information of the labeled edges to perform the edge classification of the unlabeled edges. However, the existing techniques may not be able to accurately classify the edges because real-world networks are highly sparse and very few of the edges are labeled due to the cost involved in it. Due to the scarcity of the labeled edges and high sparsity of the networks, the existing machine learning-based techniques would not be efective for edge classification.

Earlier work on edge classification has utilized the structural balance theory for undirected signed networks for perception and attitude of individuals [6,10]. Yang et al. [24] and Leskovec et al. [15] are examples of the work where structural balance theory was utilized along with their proposed methodology for edge classification in signed networks. However, these works leveraged the domain-specific characteristics of graph-structured data and their efectiveness depend on the domain-specific assumptions [1]. These domain-specific assump tions are not valid across the domains and that would limit the applicability of these methods [1,12]. Considering this, in this work, we have proposed a novel framework named NPECF for the classification of edges in an unweighted and undirected signed network. This framework is domain-independent and applicable to the arbitrary domain for edge classification in signed networks. The proposed framework NPECF uses the structural information of the network and predicts the sign of the unlabeled edges in the network.

The expected contribution of this study is a novel framework named NPECF for edge classification in a signed network. This framework generates three spanning subgraph projections of the given signed network in such a way that each projection utilizes unlabeled edges to reduce the information loss while predicting the labels. Using these projections, the NPECF framework computes the pairwise similarities of nodes in the network. The similarity scores of two projections that contain only positive edges and negative edges separately along with the unlabeled edges are compared with the third projection which is the given network but without label information. By these two comparisons, the information loss in terms of node similarity is found. The projection which has lower information loss in terms of node similarity for an unlabeled edge is utilized to predict the label of that edge. The proposed framework is domain-independent as it works considering network structure and edge label information present in the network without specific assumptions about the problem domain or characteristics of graphs.

The remaining of the paper is as follows. In Section 2, the related work is presented. In Section 3, the background and problem definition for the edge classification is presented. The proposed framework NPECF for edge classification is presented in Section 4. Experimental setup and results are discussed in Section 5 and Section 6 respectively. Finally, we conclude the paper with future research directions in Section 7.

## 2. Related work

Many data mining tasks can be performed on signed networks, such as node ranking, edge prediction, information difusion, edge classification (sign/label prediction for edges), negative sign prediction for edges [18,25]. Among these tasks, in the present study, our focus is on the task of edge classification in signed networks which is a link-oriented task. Various approaches based on the behavior-relation interplay (BRI) model have been proposed for edge classification in signed networks [2,4,15,24]. Domain-specific assumptions and behavioral evidence for learning are utilized to predict the label of the relationships in signed networks using these approaches [1]. These approaches are based on domain-specific assumptions for a signed network to perform the edge classification. Also, the methods mentioned earlier require specialized domain-specific assumptions. Utilization of the domain-specific assumptions for edge classification makes these method not suitable for the problem considered in this work as in many realworld situations we would not be able to get the domain-specific as sumptions or in many instances on the networks those domain-specific assumptions would not be followed [1,12]

Kunegis et al. [13] proposed a spectral method for diferent mining tasks on the signed network. They studied the signed graph Laplacian for signed network and performed clustering, rating prediction in recommendation network, visualization. Aggarwal et al. [1] proposed a neighborhood-based method for predicting the label of unlabeled edges in the signed network. Their proposed approach is not domain-specific and utilizes the network structure and edge label information present in the network to perform the edge classification of unlabeled edges. Ag garwal et al. [1] proposed to utilize the unlabeled edges along with the labeled edges to predict the label of the unlabeled edges. However, the performance of their proposed method is adversely afected when the network has a high number of unlabeled edges and the sparsity of the network is high [1]. Zhou et al. [26] proposed a random walk on the signed network for the clustering of nodes in the network. But in their proposed random walk they had the assumption that the randomwalker would have less probability to traverse on the negative labeled edge as compared to the positive labeled edge which restricts its application to the arbitrary domain. Of late, Jung et al. [12] proposed a random walk-based method for ranking of nodes in signed networks and applied their methodology for sign prediction for edges. They proposed Signed Random Walk with Restart (SRWR) for signed networks and utilized that for label prediction for edges. In their approach for label prediction, they basically removed all the unlabeled edges from the network and utilized only the labeled edges for a random walk. In their work, they have shown that the proposed SRWR approach is highly accurate as compared to earlier techniques, such as Guha et al. [8], Leskovec et al. [15], Wu et al. [23] for label prediction in signed networks. However, SRWR is afected when a large number of edges are unlabeled. In that case, since SRWR removes all unlabeled edges, due to high information loss the accuracy of edge classification would not be high.

Considering the limitations of the earlier techniques, in the present study, we have proposed a novel framework named NPECF (Network Projection-based Edge Classification Framework) for edge classification in signed networks. The proposed framework utilizes the structural information and edge label information present in the given network for edge classification. NPECF is not based on social balance theory and does not depend on the domain-specific assumptions for edge classification. Hence, it is applicable to any signed network from an arbitrary domain. NPECF addresses the problem of information loss due to the removal of unlabeled edges in the signed network by projecting the given network into three spanning subgraph projections where one of the projections contains all the edges but does not have label information. The rest of the two projections contains only positive edges and negative edges with unlabeled edges. Using these three projections the NPECF computes the pairwise similarities of nodes and determines the appropriate label for the unlabeled in the network by comparing the scores with the scores of the projection that has all the edges. The proposed framework does not remove unlabeled edges in the network for reducing the information loss but utilizes them in a novel way to determine the label of the unlabeled edges.

## 3. Background and preliminaries

To understand the methodology of the proposed framework NPECF, we first need to understand the mathematical notations used. For that, in this section, the background, preliminaries and important definitions are presented. Some important and frequently utilized notations are listed in Table 1.

To have the understanding of a signed network, they are formally defined in Definition 1.

## 3.1. Definition 1 (signed network)

A signed network is represented as a graph $G = ( V , E ^ { + } \cup E ^ { - } )$ with the adjacency matrix $A \in \{ - 1 , 0 , 1 \} ^ { n \times n }$ , which denotes relationships between nodes as follows:

Table 1 Important notations.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $G = (V, E^{+} \cup E^{-})$ </td><td>Signed graph with positive and negative labeled edges</td></tr><tr><td> $V, E = E^{+} \cup E^{-}$ </td><td>Set of nodes and set of edges (positive and negative labeled) in  $G$ </td></tr><tr><td> $E_{b}, E_{u}$ </td><td>Set of labeled and unlabeled edges in the network</td></tr><tr><td> $G^{pl} = (V, E_{l} \cup E_{u})$ </td><td>Partially labeled signed graph</td></tr><tr><td> $l_{ij} \in \{+, -\}$ </td><td>Label of edge ( $v_{i}, v_{j}$ )</td></tr><tr><td> $n (=|V|), m (=|E|)$ </td><td>Number of nodes and edges in  $G$ </td></tr><tr><td> $A \in \{-1, 0, 1\}^{n \times n}$ </td><td>Signed adjacency matrix</td></tr><tr><td> $A^{pl} \in \{-1, 0, 1, x\}^{n \times n}$ </td><td>Signed adjacency matrix of a partially labeled graph where  $x$  is the unknown label of the unlabeled edges and  $x \in \{1, -1\}$ </td></tr><tr><td> $A^{PU} \in \{0, 1\}^{n \times n}$ </td><td>Adjacency matrix for positive and unlabeled spanning subgraph projection of the graph</td></tr><tr><td> $A^{NU} \in \{0, 1\}^{n \times n}$ </td><td>Adjacency matrix for negative and unlabeled spanning subgraph projection of the graph</td></tr><tr><td> $A^{T} \in \{0, 1\}^{n \times n}$ </td><td>Adjacency matrix for total spanning subgraph projection of the graph</td></tr><tr><td> $SM^{PU} \in \mathbb{R}^{n \times n}$ </td><td>Pairwise node similarity matrix for  $A^{PU}$ </td></tr><tr><td> $SM^{NU} \in \mathbb{R}^{n \times n}$ </td><td>Pairwise node similarity matrix for  $A^{NU}$ </td></tr><tr><td> $SM^{T} \in \mathbb{R}^{n \times n}$ </td><td>Pairwise node similarity matrix for  $A^{T}$ </td></tr><tr><td> $DSM^{PUT} \in \mathbb{R}^{n \times n}$ </td><td>Difference score matrix for  $SM^{PU}$  and  $SM^{T}$ </td></tr><tr><td> $DSM^{NUT} \in \mathbb{R}^{n \times n}$ </td><td>Difference score matrix for  $SM^{NU}$  and  $SM^{T}$ </td></tr></table>

$$
A _ {i j} = \left\{ \begin{array}{c} 1, i f v _ {i} a n d v _ {j} h a v e p o s t i v e r e l a t i o n s h i p \\ - 1, i f v _ {i} a n d v _ {j} h a v e n e g a t i v e r e l a t i o n s h i p \\ 0, o t h e r w i s e \end{array} \right.
$$

Many real-world networks are signed. Using the signed adjacency matrix, we can represent these networks. In the signed adjacency matrix, zero represents the absence of a relationship between nodes [18].

In this work, our focus is on the problem of the prediction of labels for unlabeled edges in the network. This is also known as edge classification [1] and is defined in Definition 2.

## 3.2. Definition 2 (binary edge classification)

Given an unweighted and undirected partially labeled signed net work, $G ^ { p l } = ( V , E _ { l } \cup E _ { u } )$ and a set of labeled edges $E _ { l } \subseteq E ,$ where each edge $( \nu _ { i } , \nu _ { j } ) \in E _ { l }$ has a binary label $l _ { i j } \in \{ + , - \}$ , the edge classification problem is to determine the labels for the unlabeled edges in $E _ { u } = E \backslash E _ { l } .$

In this work, we are considering signed networks which are partially labeled i.e. $G ^ { p l } = ( V , E ^ { + } \cup E ^ { - } \cup E _ { u } )$ i.e. some edges do not have the label information (the label information of these edges are represented as $x \in \{ - 1 , + 1 \} )$ then the adjacency matrix would be as follows:

$$
A _ {i j} ^ {p l} = \left\{ \begin{array}{l} 1, \text {positive relationship} \\ \quad - 1, \text {negative relationship} \\ x, \text {label of relationship is not known} \\ \quad 0, \text {no relationship} \end{array} \right.
$$

In the real-world, the networks are very sparse and the relationships represented by edges are scarcely labeled and the task is to predict the label of unlabeled edges in the network i.e. we have to predict the label information x of the unlabeled edges.

## 4. NPECF: framework for edge classification

In this section, we discuss the proposed framework for binary classification of unlabeled edges in the network. We also give an il lustration to understand the working of the proposed framework.

## 4.1. Description of the framework

The proposed framework NPECF is novel in terms of using three spanning subgraph projections of the given signed network. NPECF works in two phases as shown in Fig. 1.

In the first phase, two steps are performed namely projection and similarity computation. In the projection step, the first projection termed as positive-unlabeled projection keeps all the nodes of the given network with positive and unlabeled edges. The second projection, termed as negative-unlabeled projection has negative and unlabeled edges. The third projection, called total projection keeps all the edges but disregards their label information and also has unlabeled edges. The next step in this phase is to compute the pairwise similarity between nodes of each projection. We can utilize any suitable algorithm to compute the pairwise similarity between nodes for each projection, however, if the utilized algorithm is efective in computing the pairwise similarity between nodes then it would lead to the better performance of the NPECF. After computing the pairwise similarity between nodes, we get three similarity matrices called the similarity matrix for the positive-unlabeled projection $( S M ^ { P U } )$ , similarity matrix for the negative-unlabeled projection $( S M ^ { N U } )$ and the similarity matrix for the total projection (SM<sup>T</sup>) for positive-unlabeled projection, negative-unlabeled projection, and total projection respectively.

The adjacency matrices for the positive-unlabeled projection $( A ^ { P U } ) ,$ negative-unlabeled projection $( A ^ { \hat { N } U } )$ and total projection $( A ^ { T } )$ are computed as follows:

$$
A ^ {P U} = \frac {| A ^ {p l} | _ {x = 1} + A _ {x = 1} ^ {p l}}{2}\tag{1}
$$

$$
A ^ {N U} = \frac {| A ^ {p l} | _ {x = 1} - A _ {x = 1} ^ {p l}}{2}\tag{2}
$$

$$
A ^ {T} = | A ^ {p l} | _ {x = 1}\tag{3}
$$

Here, $\big | \boldsymbol A ^ { p l } \big | _ { \boldsymbol x = 1 }$ is the absolute adjacency matrix when we assume a positive label of unlabeled edges. However, $A ^ { p l } { } _ { x = 1 }$ is the adjacency matrix when we assume a positive label for unlabeled edges. From these adjacency matrices, we compute the similarity matrices as follows:

$$
S M ^ {P U} = f _ {s i m} (A ^ {P U})\tag{4}
$$

$$
S M ^ {N U} = f _ {s i m} (A ^ {N U})\tag{5}
$$

$$
S M ^ {T} = f _ {s i m} (A ^ {T})\tag{6}
$$

Here, $f _ { s i m } ( \cdot )$ is the function which corresponds to the algorithm that computes the pairwise similarities between nodes in the network.

In the second phase of NPECF, we have two steps called score difference computation and edge labeling. In the score diference computation step, we compute the absolute diferences between $S M ^ { P U }$ and SMT and also $S M ^ { N U }$ and ${ \boldsymbol { S } } { \boldsymbol { M } } ^ { T }$ to get diference score matrices called $D S M ^ { P U T }$ and $D S M ^ { N U T }$ respectively. These diference score matrices correspond to the information loss of positive-unlabeled projection and negative-unlabeled projection with respect to total projection. For pairwise similarity computation, the total projection uses the complete information present in the network after disregarding the sign of edges. However, $\mathbf { \widehat { \mathbf { \xi } } } _ { S M } \mathbf { \widehat { \mathbf { \xi } } } ^ { P U }$ and ${ \cal { S } } M ^ { N U }$ has pairwise similarities considering only positive and negative edges along with the unlabeled edges respectively. So the diference between $S M ^ { T }$ and $S M ^ { P U }$ , and ${ \boldsymbol { S } } { \boldsymbol { M } } ^ { T }$ and $S M ^ { \overset { \underset { \star } { } } { N U } }$ would give the information regarding which projection corresponding to the edge for which absolute diference is being computed is closer to the total projection and thus the sign of that unlabeled edge can be decided accordingly. In the second step of this phase, we do the edge labeling for unlabeled edges according to the comparison of $D S M ^ { P U { \bar { T } } }$ and $D S M ^ { N U T }$ Whichever score is lower, we assign the sign of that projection (positive for SM<sup>PU</sup> and negative for $S M ^ { N U } )$ to the unlabeled edge. We compute DSM<sup>PUT</sup> and $D S M ^ { N U T }$ using the following equations:

![](/api/attachments/QRURKKX4/fulltext/images/ea8ca1059301eb5dee292c47182daa34877891e14b483fedaa144e04e1203f1d.jpg)  
Phase - 2  
Fig. 1. NPECF for edge classification in signed networks

$$
D S M ^ {P U T} = | S M ^ {P U} - S M ^ {T} | \odot \left(\frac {A _ {x = 1} ^ {p l} - A _ {x = - 1} ^ {p l}}{2}\right)\tag{7}
$$

$$
D S M ^ {N U T} = | S M ^ {N U} - S M ^ {T} | \odot \left(\frac {A _ {x = 1} ^ {p l} - A _ {x = - 1} ^ {p l}}{2}\right)\tag{8}
$$

Here, ⨀ is the operator for the elementwise product of two matrices. For an unlabeled edge $( \nu _ { i } , \nu _ { j } ) \in E ^ { u }$ , the predicted label $\widehat { l } _ { i j }$ would be as follows:

$$
\widehat {l} _ {i j} = \left\{ \begin{array}{l} -  ,   D S M _ {i j} ^ {P U T} - D S M _ {i j} ^ {N U T} > 0 \\ +  ,   D S M _ {i j} ^ {P U T} - D S M _ {i j} ^ {N U T} \leq 0 \end{array} \right.\tag{9}
$$

The algorithm for NPECF is written below:

## 4.2. Illustration

## 5. Experimental setup

In this section, we discuss the experimental setup to perform a set of experiments on four real-world datasets from diferent domains. All experiments were performed on a system using R version 3.6.0.

## 5.1. Datasets

For experiments, we have utilized Epinions,<sup>2</sup> Slashdot ${ \mathsf { Z o o } } , { } ^ { 3 }$ Wikipedia Requests for Adminship $( \mathrm { R f A } ) ^ { 4 }$ and Yeast Genetic Interaction Network (GIN)<sup>5</sup> datasets. The diferent statistics of these datasets are given in Table 2.

The Epinions dataset is a who-trust-whom online social network<sup>6</sup> of consumer reviews. Using Epinions, a review given by a consumer can be either trusted or distrusted by other consumers. In the network of the Epinions dataset, these records of trust or distrust relationships are kept

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm NPECF

Input:
$G^{pl} = (V, E^{+} \cup E^{-} \cup E_{u})$: partially labeled undirected and unweighted signed network
$A^{pl} \in \{-1, 0, 1, x\}^{n \times n}$: adjacency matrix for $G$ where $x \in \{-1, +1\}$ $f_{sim}(\cdot)$: function corresponding to the algorithm for computing pairwise similarities of nodes
Output:
$\hat{l}_{ij}$: predicted labels for all unlabeled edges $(v_{i}, v_{j}) \in E_{u}$ in the network
Begin
1. Compute $A^{PU}$, $A^{NU}$ and $A^{T}$ as follows:
$A^{PU} = \frac{|A^{pl}|_{x=1} + A^{pl}_{x=1}}{2}$ $A^{NU} = \frac{|A^{pl}|_{x=1} - A^{pl}_{x=1}}{2}$ $A^{T} = |A^{pl}|_{x=1}$
2. Compute the pairwise node similarity matrices for $A^{PU}$, $A^{NU}$ and $A^{T}$ as follows:
$SM^{PU} = f_{sim}(A^{PU})$ $SM^{NU} = f_{sim}(A^{NU})$ $SM^{T} = f_{sim}(A^{T})$
3. Compute the difference score matrices $DSM^{PUT}$ and $DSM^{NUT}$ as follows:
$DSM^{PUT} = |SM^{PU} - SM^{T}| \odot \left( \frac{A^{pl}_{x=1} - A^{pl}_{x=-1}}{2} \right)$ $DSM^{NUT} = |SM^{NU} - SM^{T}| \odot \left( \frac{A^{pl}_{x=1} - A^{pl}_{x=-1}}{2} \right)$
4. For all $(v_{i}, v_{j}) \in E_{u}$, predict the label as follows:
$\hat{l}_{ij} = \begin{cases}-, &amp; DSM_{ij}^{PUT} - DSM_{ij}^{NUT} &gt; 0 \\+, &amp; DSM_{ij}^{PUT} - DSM_{ij}^{NUT} \leq 0\end{cases}$
End
</div>

To understand the working of the proposed framework NPECF, we consider a toy signed network shown in $\mathrm { F i g . ~ } 2 ( \mathbf { a } )$ . This network has six nodes and nine edges. Three of the edges have negative labels, five edges have positive labels and one edge $( \nu _ { 1 } , \nu _ { 6 } )$ is unlabeled for which we have to predict the label. The adjacency matrix $A ^ { p l }$ of this network and three adjacency matrices $( A ^ { P U } , \dot { A ^ { T } }$ and $\overset { \cdot } { A } { } ^ { N U } )$ for its three projections are shown in Fig. 2(b).

For these three adjacency matrics i.e. $A ^ { P U } , A ^ { T }$ and $A ^ { N U }$ , we perform the pairwise node similarity computation using SimRank [11]. After applying SimRank, we get three similarity matrices called ${ \mathit { s M } } ^ { P U } ,$ T and $S M ^ { N U }$ as shown in Fig. 2(c). Using these similarity matrices, we compute the diference score matrices $D S M ^ { P U T }$ and $D S M ^ { N U T }$ using Eq. (7) and Eq. (8). After that, we can do the prediction of the unlabeled edge using Eq. (9). In this particular example, there is only one edge $( \nu _ { 1 } ,$ $\nu _ { 6 } )$ which is unlabeled. For this edge, we compare the score of $D S M ^ { P U T }$ and $D S M ^ { N U T }$ and according to Eq. (9), the appropriate label is assigned to this edge. In this example, since $\Delta S M _ { 1 6 } ^ { \mathrm { \Delta \hat { \it P } \hat { U } T } } \mathrm { \Sigma } _ { - } ^ { - } \mathrm { \Delta } D S M _ { 1 6 } ^ { \mathrm { \Delta \it N U T } } \mathrm { \Sigma } < \mathrm { \Sigma } \stackrel { \sim } { 0 } \mathrm { i . e . }$ $( 0 . 0 0 2 0 - 0 . 0 1 2 7 \ < \ 0 )$ therefore, this edge is assigned the positive label.

as signed edges. A trust relationship is represented by a positive edge and a distrust relationship is represented as a negative edge in the network. Slashdot<sup>7</sup> is a technology-related news website and it is known for its specific user community. The users of Slashdot can tag each other as friends or foes after the introduction of the Slashdot Zoo feature in 2002. Slashdot records these friends or foe relationships between the users of Slashdot.

Wikipedia is an open collaboration-based free online encyclopedia. A Wikipedia editor can become an administrator and for that, a request

$$
\begin{array}{r l} & \text {Positive edge} \\ & \text {Negative edge} \\ & \text {Unlabeled edge} \\ & v _ {1} \\ & v _ {2} \\ & v _ {3} \\ & v _ {4} \\ & v _ {5} \\ & v _ {6} \\ & A ^ {v i} = \left[ \begin{array}{c c c c c c} 0 & 1 & 0 & 0 & 0 & x \\ 1 & 0 & 1 & - 1 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & 0 & 0 \\ 0 & - 1 & - 1 & 0 & 1 & 1 \\ 0 & - 1 & 0 & 1 & 0 & 1 \\ x & 0 & 0 & 1 & 1 & 0 \end{array} \right] \\ & A ^ {P U} = \left[ \begin{array}{c c c c c c} 0 & 1 & 0 & 0 & 0 & 1 \\ 1 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 & 0 & 1 \\ 1 & 0 & 0 & 1 & 1 & 0 \end{array} \right] \\ & A ^ {T} = \left[ \begin{array}{c c c c c c} 0 & 1 & 0 & 0 & 0 & 1 \\ 1 & 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 1 \\ 0 & 1 & 0 & 1 & 0 & 1 \\ 1 & 0 & 0 & 1 & 1 & 0 \end{array} \right] \\ & A ^ {N U} = \left[ \begin{array}{c c c c c c} 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 & 0 \end{array} \right] \end{array}
$$

(a)

(b)

$$
\begin{array}{r l} & S M ^ {P U} = \left[ \begin{array}{c c c c c c} 1 & 0. 0 0 4 2 & 0. 0 2 8 2 & 0. 0 1 6 5 & 0. 0 1 6 5 & 0. 0 1 0 7 \\ 0. 0 0 4 2 & 1 & 0. 0 0 1 8 & 0. 0 0 9 1 & 0. 0 0 9 1 & 0. 0 1 4 5 \\ 0. 0 2 8 2 & 0. 0 0 1 8 & 1 & 0. 0 1 5 1 & 0. 0 1 5 1 & 0. 0 0 7 8 \\ 0. 0 1 6 5 & 0. 0 0 9 1 & 0. 0 1 5 1 & 1 & 0. 0 1 7 1 & 0. 0 1 4 7 \\ 0. 0 1 6 5 & 0. 0 0 9 1 & 0. 0 1 5 1 & 0. 0 1 7 1 & 1 & 0. 0 1 4 7 \\ 0. 0 1 0 7 & 0. 0 1 4 5 & 0. 0 0 7 8 & 0. 0 1 4 7 & 0. 0 1 4 7 & 1 \end{array} \right] \\ & S M ^ {T} = \left[ \begin{array}{c c c c c c} 1 & 0. 0 1 2 8 & 0. 0 1 5 5 & 0. 0 1 4 9 & 0. 0 1 6 0 & 0. 0 1 2 7 \\ \text {SM} ^ {T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {P U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} - \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left\lbrack \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DMS} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}{c c c c c c} \text {DSM} ^ {N U T} = \left[ \begin{array}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{b}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \begin{array}{c}\right) \\ \text {DSM} ^ {N U T} = \left[ \mathrm{d.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c}. \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ .) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ). \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ) \\ (\\ ). \\ (\\ ) \\ (\\ ) \\ (\\ ). \\ (\\ ) \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ .) \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\ ). \\ (\\). \\ (\mathsf {S M} ^ {\mathsf {N U}} = [ {\mathsf {S M}} ^ {\mathsf {N U}} ] = [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^{\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [{\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathsf {N U}} ] + [ {\mathsf {S M}} ^ {\mathbf N u t}) ] + [ {\mathsf {S M}} ^ {\mathbf N u t}) ] + [ {\mathsf {S M}} ^ {\mathbf N u t}) ] + [ {\mathsf {S M}} ^ {\mathbf N u t}) ] + [ {\mathsf {S M}} ^ {\mathbf N u t}) ] + [ {\mathsf {S M}} ^ {\mathbf N u t}) ] + [ {\mathsf {S M}}, [ {\mathsf {S M}} ] ] + [ {\mathsf {S M}}, [ {\mathsf {S M}} ] ] + [ {\mathsf {S M}}, [ {\mathsf {S M}} ] ] + [ {\mathsf {S M}}, [ {\mathsf {S M}} ] ] + [ {\mathsf {S M}}, [ {\mathsf {S M}} ] ] + [ {\mathsf {S M}}, [ {\mathsf {S M}} ] ] + [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _[[ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ [ {\bar {\mathsf {S}}} _ {[ {\bar {\mathsf {S}}} _ {[ {\bar {\mathsf {S}}} , [{\bar {\mathsf {{H}}} }_{-})},\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,\bar{\mathbb{{C}}} ,,}\right) ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---|
| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---|
| :--| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---|
| :--| :---| :---| :---| :---| :---| :---| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--| :--|
| :--| :---| :---| :---| :---| :---| :---| :--| :--| :--| :--| :--| :--| :--|:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\: |\:)\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\:|\: |\:)\:+\:(\texttta,b,c,d,e,f,g,h,i,j,k,l,m,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,l,l,l,l,l,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,K,L,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,J,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,H,i,j,k,l,m,\texttta,b,c,d,e,f,g,h,i,j,k,l,m,\texttta,b,c,d,e,f,g,H,i,j,k,l,m,\texttta,b,c,d,e,f,g,H,i,j,k,l,m,\texttta,b,c,d,e,f,g,H,i,j,k,l,m,\texttta,b,c,d,e,f,g,H,i,j,k,l,m,\texttta,b,c,d,e,f,G,H,i,j,k,l,m,\texttta,b,c,d,e,f,G,H,i,j,k,l,m,\texttta,b,c,d,e,f,G,H,i,j,k,l,m,\texttta,b,c,d,e,f,G,H,i,j,k,l,m,\texttta,b,c,d,e,f,G,H,i,j,k,l,m,\texttta,b,c,d,e,f,G,H,i,j,k,l,m,\texttta,b,c,d,E,F,G,H,i,j,k(l),\texttta,b,c,D,E,F,G,H,i,j,k(l),\texttta,b,C,D,E,F,G,H,i,j,k(l),\texttta,B,C,D,E,F,G,H,i,j,k(l),\texttta,B,C,D,E,F,G,H,i,j,k(l),\texttta,B,C,D,E,F,G,H,i,j,k(l),\texttta,B,C,D,E,F,G,H,i,j,k(l),\texttta,B,C,D,E,F,G,H,i,j,k(l),\texttta,B,C,D,E,F,G,H,i,j,k(l),\texttt{s.t.,}\\x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,x,y,v,w,x,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w,v,w v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v ,v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv, Vv]
$$

(c)  
Fig. 2. A toy network, adjacency matrices of its projections and the computation of diference score matrices.  
Table 2  
Description of datasets.

<table><tr><td></td><td>Epinions</td><td>Slashdot Zoo</td><td>Wikipedia RfA</td><td>Yeast GIN</td></tr><tr><td>Domain</td><td>Online consumer review</td><td>Technology related news</td><td>Wikipedia election</td><td>Biology</td></tr><tr><td>Directed</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>#Nodes</td><td>131,828</td><td>77,357</td><td>11,278</td><td>5361</td></tr><tr><td>#Edges</td><td>841,372</td><td>516,575</td><td>185,627</td><td>92,136</td></tr><tr><td>#Positive Edges</td><td>717,667</td><td>396,378</td><td>144,451</td><td>16,998</td></tr><tr><td>#Negative Edges</td><td>123,705</td><td>120,197</td><td>41,176</td><td>75,138</td></tr></table>

for adminship (RfA) is submitted. In response to RfA, supporting, neutral, or opposing votes may be casted by Wikipedia members. In the Wikipedia-RfA dataset, these supporting or opposing relationships are recorded. The supporting relationship is considered as a positive edge in the network and an opposing relationship is considered as a negative edge in the network. Genetic interactions are important for the determination of the function of diferent genes and the analysis of their properties. The Yeast Genetic Interactions (GIs) were downloaded from BioGRID [17]. We retrieved «positive genetic» relationships between genes as positive GIs, and «negative genetic» ones as negative GIs.

In their original form, the Epinions, Slashdot Zoo and Wikipedia RfA datasets are directed, and the number of positive edges is very high as compared to negative edges. The Yeast GIN dataset is undirected, but the number of negative edges is very high as compared to positive edges. So, before utilizing them for experiments we perform data preprocessing. Since NPECF is for undirected graphs, so in order to make Epinion, Slashdot Zoo and Wikipedia RfA datasets undirected, we consider only those node pairs which have the same sign edges in both directions [22]. While converting the directed network into undirected one, we have not simply ignored the direction of links because that would not be applicable to networks from domains like communication, biology, and online social networks like the Twitter network.

![](/api/attachments/QRURKKX4/fulltext/images/f3d02ec906eaf61f235bbb13b316e38383a1e9e32c998caa6f083d753557ce03.jpg)  
(a) Epinions network

![](/api/attachments/QRURKKX4/fulltext/images/bb4e7b663765d0dca3016ad26d0d080caf52a59506752e33d4b3e6d9ed8b3992.jpg)  
(b) Degree distribution in Epinions network

![](/api/attachments/QRURKKX4/fulltext/images/14db52a7228f0d76f54970953f5e62cc687367575f88cc19a6eaa36e5383aa1b.jpg)  
(c)Slashdot Zoo network

![](/api/attachments/QRURKKX4/fulltext/images/79a7124d8825d6b4999b5984e277b8abbd6e7eb8a9e8e3a704de9975a554b15d.jpg)  
(d) Degree distribution in Slashdot Zoo network

![](/api/attachments/QRURKKX4/fulltext/images/0422ed5bcd7e2eb2760defa3f7983942f90e3f92baec59a819c4d07fa10cc452.jpg)  
(e) Yeast GIN network

![](/api/attachments/QRURKKX4/fulltext/images/058f7b42176d1b580e2271534cfabb61b76b14746ba43659ee59737b13d03220.jpg)  
(f) Degree distribution in Yeast GIN network

![](/api/attachments/QRURKKX4/fulltext/images/fd9f0e281de34a015771443911a3b1b66b83c0e0a3a187a9ff35c15b51ede1bf.jpg)  
(g) Wikipedia RfA network

![](/api/attachments/QRURKKX4/fulltext/images/2c06069880492fbcfef4cfffa88cce182d82aead81a76cbb9bde9c95631f34df.jpg)  
(h) Degree distribution in Wikipedia RfA network  
Fig. 3. Diferent signed networks used in experiments. In these networks, the green edges show the positive relationships and the red edges show the negative relationships. In degree distribution plots, we have probability values on the vertical axis and degrees on the horizontal axis. As shown in the figures, degree distribution plots for all datasets used for experiments follow the long tail. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Conversion to the undirected network will make these networks disconnected. So, we take a connected component in such a way that the number of positive and negative labeled edges are going to be balanced. After pre-processing, we get pre-processed datasets as shown in Fig. 3 and their statistics are given below in Table 3. For Yeast GIN, which is an undirected network, we take only a connected component in such a way that the positive and negative edges are balanced in that. The preprocessed Yeast GIN dataset is shown in Fig. 3 and the statistics of this dataset are also given in Table 3. From Table 3, we can see that the number of positive edges and the negative edges in these datasets is balanced after pre-processing, so the experiments performed on these datasets would lead to meaningful conclusions.

Table 3  
Description of balanced datasets after pre-processing.

<table><tr><td></td><td>Epinions</td><td>Slashdot Zoo</td><td>Wikipedia RfA</td><td>Yeast GIN</td></tr><tr><td>Domain</td><td>Online consumer review</td><td>Technology related news</td><td>Wikipedia election</td><td>Biology</td></tr><tr><td>#Nodes</td><td>2952</td><td>2559</td><td>1738</td><td>3451</td></tr><tr><td>#Edges</td><td>5923</td><td>3162</td><td>2968</td><td>8982</td></tr><tr><td>#Positive Edges</td><td>2960</td><td>1580</td><td>1482</td><td>4493</td></tr><tr><td>#Negative Edges</td><td>2963</td><td>1582</td><td>1486</td><td>4489</td></tr></table>

To show the applicability of the proposed NPECF method, we also consider the undirected connected datasets used for experiments in which the ratio of positive to negative edges are going to be similar as in the original datasets. These four datasets are shown in Fig. 4 and the statistics of these four datasets are given in Table 4.

## 5.2. Algorithms for comparison and performance evaluation

To show the efectiveness, the performance of NPECF is compared with the following sign prediction techniques applicable to unweighted and undirected signed networks. These techniques do not assume any domain-specific assumptions for edge classification and suitable for the problem discussed in this paper.

Signed Random Walk with Restart (SRWR): This is a method that is utilized for personalized ranking of nodes in the signed networks and can be utilized for sign prediction of unlabeled edges in the signed networks [12].

Neighborhood-based Algorithm (NbA): In this method, the neigh borhood of the nodes on which unlabeled edges are incident are considered while predicting the sign of the unlabeled edges [1].

For evaluation of the performance of the methods, we use the accuracy (Acc) of classification of unlabeled edges in the network which is defined as given below:

$$
A c c = \frac {\# c o r r e c t l y l a b e l e d e d g e s}{\# u n l a b e l e d e d g e s}\tag{10}
$$

If we consider the contingency table, then the accuracy can be computed as:

$$
A c c = \frac {T P + T N}{T P + F P + T N + F N}\tag{11}
$$

where TP is True Positive, TN is True Negative, FP is False Positive and FN is False Negative [9].

The higher value of accuracy means the method is efective for the classification of unlabeled edges in the network. The Acc ∈ [0,1] where 0 indicates that no unlabeled edge in the network has been classified correctly by the method being evaluated and a value 1 indicates that all unlabeled edges in the network have been classified correctly by the method being evaluated.

For evaluation, we also use Geometric Mean [21] as accuracy alone is not enough to assess the algorithms for sign prediction. Since in this work, both the positive and negative edges are of the same importance, therefore, the measures which consider both true positive and true negative predictions would be suitable. Geometric Mean aggregates both sensitivity (True positive rate, TPR) and specificity (True negative rate, TNR) as given below:

$$
G M = \sqrt {T P R \times T N R} = \sqrt {\frac {T P}{T P + F N} \times \frac {T N}{T N + F P}}\tag{12}
$$

Geometric Mean $G M \in [ 0 , 1 ]$ where 0 indicates that no unlabeled edge in the network has been classified correctly by the method being evaluated and a value 1 indicates that all unlabeled edges in the network have been classified correctly by the method being evaluated.

To evaluate the performance of the algorithms, we also employed another measure called Diagnostic Odds Ratio (DOR) [21] that is defined as given below:

$$
D O R = \frac {T P R}{1 - T N R} \times \frac {T N R}{1 - T P R} = \frac {T P \times T N}{F P \times F N}\tag{13}
$$

where TPR is True positive rate and TNR is True negative rate defined as given below:

$$
T P R = \frac {T P}{T P + F N}\tag{14}
$$

$$
T N R = \frac {T N}{T N + F P}\tag{15}
$$

Diagnostic Odds Ratio measures how well the two classes (positive and negative) are classified/predicted by the algorithms. High values of the Diagnostic Odds Ratio indicate high accuracy of the classification and well-balanced class accuracies.

For performance evaluation of diferent methods on each dataset, x % (where x = 60, 65, 70, 75 and 80) of the labeled edges are selected. We use the label information of those edges as prior knowledge. The classification of the unlabeled edges is performed using that prior knowledge and we compute the accuracy of diferent algorithms.

For SRWR, we take the optimal values of parameters according to Jung et al. [12]. The values of parameters β and γ are taken as 0.5 and 0.8 respectively for Epinions and Slashdot Zoo datasets as described in Jung et al. [12]. For the Wikipedia-RfA dataset, the values of parameters β and γ are taken as 0.3 and 0.5 respectively. For NbA, we take the value of parameters μ as 0.5 and neighborhood size as 100 for all four datasets following Aggarwal et al. [1]. For NPECF, we have used SimRank [11] in phase-1 to measure the pairwise similarities between nodes in the network. However, our framework could use any other more efective algorithm to compute the pairwise similarities which would improve the overall performance of NPECF. In our experiments, for SimRank, we take the value of decay factor as 0.6 and the number of iterations is taken as 5 [11] for all four datasets.

## 6. Experimental results and discussion

In this section, we present the experimental results of the four datasets i.e. Epinions, Slashdot Zoo, Wikipedia RfA, and Yeast GIN for both the balanced and imbalanced cases.

## 6.1. Results for balanced case

Fig. 5.1 and Fig. 5.2 shows the Accuracy, Geometric Mean and Diagnostic Odds Ratio charts for all four datasets i.e. Epinions, Slashdot Zoo, Wikipedia RfA, and Yeast GIN datasets. In Fig. 5.1(a), for the Epinions dataset, we can see that the accuracy of NPECF is higher as compared to SRWR and NbA. For NbA, we can see that the accuracy is low due to many unlabeled edges in the network. Also, NbA could classify only 96%, 96%, 97%, 97% and 97% of the unlabeled edges in the network when the labeled edges were 60%, 65%, 70%, 75% and

![](/api/attachments/QRURKKX4/fulltext/images/d1152055a32a079790e8cd0d61cc3e412bb566203f84d4817d1537c763f3b438.jpg)  
(a) Epinions network

![](/api/attachments/QRURKKX4/fulltext/images/d6e3bbc4a3012a9a50061af6635ae1597d5fe349063027e95c0522973690c80e.jpg)  
(b) Degree distribution in Epinions network

![](/api/attachments/QRURKKX4/fulltext/images/526279bc6833989f670b90f28f9301319e2f0d6f973b0ab7ca421a010041f676.jpg)  
(c) Slashdot Zoo network

![](/api/attachments/QRURKKX4/fulltext/images/19af707663cc2f437ce7cc37066120083ab28124193691f815bc5750e2ea19f9.jpg)  
(d) Degree distribution in Slashdot Zoo network

![](/api/attachments/QRURKKX4/fulltext/images/ddf2a74dbf0cc8a57f29d732edbf047bb2ce0f210ab6c6182c4e1231b137dfc5.jpg)  
(e) Yeast GIN network

![](/api/attachments/QRURKKX4/fulltext/images/6db9acb55069b3ddae5cf4542f1034982d82e9195516c25b5f8508b17644b1f0.jpg)  
(f) Degree distribution in Yeast GIN network

![](/api/attachments/QRURKKX4/fulltext/images/28c932320be69ab4ef69885baad81b5a1c6397618cd00b78d8f5a08e07a07ce2.jpg)  
(g) Wikipedia RfA network

![](/api/attachments/QRURKKX4/fulltext/images/e5698885685c240f5cf48b5b2f9664e83e3cc84944f622b7303d972ff81e500f.jpg)  
(h) Degree distribution in Wikipedia RfA network  
Fig. 4. Diferent signed networks used in experiments. In these networks, the green edges show the positive relationships and the red edges show the negative relationships. In degree distribution plots, we have probability values on the vertical axis and degrees on the horizontal axis. As shown in the figures, degree distribution plots for all datasets used for experiments follow the long tail. (a) Epinions network. (b) Degree distribution in Epinions network. (c) Slashdot Zoo network. (d) Degree distribution in Slashdot Zoo network. (e) Yeast GIN network. (f) Degree distribution in Yeast GIN network. (g) Wikipedia RfA network. (h) Degree distribution in Wikipedia RfA network.

80% respectively. However, NPECF and SRWR were able to classify all unlabeled edges.

Since NbA was not able to classify all the unlabeled edges, therefore, we compare only NPECF and SRWR using Geometric Mean and Diagnostic Odds Ratio as these measures require all unlabeled edges to be classified by a method. In Fig. 5.1(b) and Fig. 5.1(c), the performance of NPECF and SRWR has been plotted along with the percentage improvement of NPECF over SRWR. We can see that the performance of NPECF is significantly better as compared to SRWR in terms of Accuracy, Geometric Mean and Diagnostic Odds Ratio. The NPECF method is better in terms of classifying both the positive and negative edges.

Table 4  
Description of imbalanced datasets after pre-processing.

<table><tr><td></td><td>Epinions</td><td>Slashdot Zoo</td><td>Wikipedia RfA</td><td>Yeast GIN</td></tr><tr><td>Domain</td><td>Online consumer review</td><td>Technology related news</td><td>Wikipedia election</td><td>Biology</td></tr><tr><td>#Nodes</td><td>3490</td><td>3225</td><td>1708</td><td>3453</td></tr><tr><td>#Edges</td><td>9958</td><td>4907</td><td>2973</td><td>8976</td></tr><tr><td>#Positive Edges</td><td>8468</td><td>3961</td><td>2356</td><td>1546</td></tr><tr><td>#Negative Edges</td><td>1490</td><td>946</td><td>617</td><td>7430</td></tr></table>

![](/api/attachments/QRURKKX4/fulltext/images/c9038066c0e1424af750d663a04d1b6eae4049be28d78702dd5941f1bf389bd0.jpg)  
(a) Accuracy values for Epinions dataset

![](/api/attachments/QRURKKX4/fulltext/images/f37e431bde608cb4665550e202bb8e48d866d1a5ccb5f5950e63db8ef37b53f1.jpg)  
(b) Geometric mean values for Epinions dataset

![](/api/attachments/QRURKKX4/fulltext/images/0a0b4e34b53d7ee3f4e35cf854b3d4ce834d8608f398708c4a09b2eaad38b0da.jpg)  
(c) Diagnostic odds ratio values for Epinions dataset

![](/api/attachments/QRURKKX4/fulltext/images/c932712a909863abf638f746810d48abc9b5894e1871ec9c0e3169968c0d5f49.jpg)  
(d) Accuracy values for Slashdot Zoo dataset

![](/api/attachments/QRURKKX4/fulltext/images/128f11bbe2439a82215f5dc6c590871a13dbbec272aad989eab28318dc1e9db4.jpg)  
(e) Geometric mean values for Slashdot Zoo dataset

![](/api/attachments/QRURKKX4/fulltext/images/898391497d3483e8273ebef89344a7956a2fe2713f28804bd3b85b56949963af.jpg)  
(f) Diagnostic odds ratio values for Slashdot Zoo dataset

Fig. 5. 1. Accuracy, Geometric mean and Diagnostic odds ratio values of diferent algorithms for Epinions and Slashdot Zoo datasets. For NbA algorithm, we have only accuracy values as NbA could not predict the sign of all unsigned edges in the experiments. 2. Accuracy, Geometric mean and Diagnostic odds ratio values of diferent algorithms for Wikipedia RfA and Yeast GIN datasets. For NbA algorithm, we have only accuracy values as NbA could not predict the sign of all unsigned edges in the experiments.  
![](/api/attachments/QRURKKX4/fulltext/images/c0a224a6b27bab4c21e33452431930384f44b3d355be848ceb0da5ba96ec65a0.jpg)  
(a) Accuracy values for Wikipedia RfA dataset

![](/api/attachments/QRURKKX4/fulltext/images/5586215c38ffe46e36193efb8db3756ce60e17250518de22c671cb2cde52863e.jpg)  
(b) Geometric mean values for Wikipedia RfA dataset

![](/api/attachments/QRURKKX4/fulltext/images/be5bcbd9ef4118aa09526243c9305208e46dc2c4b7e0f318836df1cfad545248.jpg)  
(c) Diagnostic odds ratio values for Wikipedia RfA dataset

![](/api/attachments/QRURKKX4/fulltext/images/5ec86e8c05e580b21a058a8d521f1a0f09de0f5cc40715009253ccc902361f88.jpg)  
(d) Accuracy values for Yeast GIN dataset

![](/api/attachments/QRURKKX4/fulltext/images/fa79e4839edd7ba4a0325f11d63a14d23908804b4a50b33a5a82490ac7b9d84d.jpg)  
(e) Geometric mean values for Yeast GIN dataset  
Fig. 5. (continued)

![](/api/attachments/QRURKKX4/fulltext/images/5cbcdb3f4c0e50c91ff0362598d419219c9bfe73c1e7306fbecb1f5ae877cd7f.jpg)  
(f) Diagnostic odds ratio values for Yeast GIN dataset

![](/api/attachments/QRURKKX4/fulltext/images/f5e4f72ba0bcdda353ed85d26f8d8b3264b73879b97c72989447b21f8b55fc8f.jpg)  
(a) Accuracy values for Epinions dataset

![](/api/attachments/QRURKKX4/fulltext/images/ecbf4435618f929e93233abbd73d51219d58d3c2c55327a265f9632fc81179fb.jpg)  
(b) Geometric mean values for Epinions dataset

![](/api/attachments/QRURKKX4/fulltext/images/06fd59403c81c0e56f07cea2c3fcdc8bdb3fdfe292150587efbdcd541e41befa.jpg)  
(c) Diagnostic odds ratio values for Epinions dataset

![](/api/attachments/QRURKKX4/fulltext/images/d2165b420903c621c09da1ebfe91a7229a1e237a382d933759d68817200c6da3.jpg)  
(d) Accuracy values for Slashdot Zoo dataset

![](/api/attachments/QRURKKX4/fulltext/images/d85b9e00cccf9251002e066df357065f6abe3e490e1bd19fbd5e70637db32e62.jpg)  
(e) Geometric mean values for Slashdot Zoo dataset

![](/api/attachments/QRURKKX4/fulltext/images/6dbdaab21b257417f62e6ab4d0444569da23b8e044ee4a84fc3d78a90e2176f4.jpg)  
(f) Diagnostic odds ratio values for Slashdot Zoo dataset

Fig. 6. 1. Accuracy, Geometric mean and Diagnostic odds ratio values of diferent algorithms for Epinions and Slashdot Zoo datasets. For NbA algorithm, we have only accuracy values as NbA could not predict the sign of all unsigned edges in the experiments. 2. Accuracy, Geometric mean and Diagnostic odds ratio values of diferent algorithms for Wikipedia RfA and Yeast GIN datasets. For NbA algorithm, we have only accuracy values as NbA could not predict the sign of all unsigned edges in the experiments.  
![](/api/attachments/QRURKKX4/fulltext/images/6be2dadc3d80b6dd5c69db9808031f1ef4ee7df662b35fecd0b920b0318b6336.jpg)  
(a) Accuracy values for Wikipedia RfA dataset

![](/api/attachments/QRURKKX4/fulltext/images/88ea2427404198d8c4f0a0609cc441886738fd7bd448e3d77ddd1ac56439fb04.jpg)  
(b) Geometric mean values for Wikipedia RfA dataset

![](/api/attachments/QRURKKX4/fulltext/images/96921c166139febf7eb8d5c05c14aac2c6e8e5e6271660b0d8d79d4e46ca0506.jpg)

![](/api/attachments/QRURKKX4/fulltext/images/1605a43910b2138b43db3106461509f98f85c33b3533724441efd073a02e3d03.jpg)  
(c) Diagnostic odds ratio values for Wikipedia RfA dataset

(d) Accuracy values for Yeast GIN dataset  
![](/api/attachments/QRURKKX4/fulltext/images/4784af3063a594d0376801dadc5b6ed7f42398cefc78c8083b90f7f9fda1da58.jpg)  
(e) Geometric mean values for Yeast GIN dataset

![](/api/attachments/QRURKKX4/fulltext/images/143b96014262d39edc3e5645f81e59fb59eec0d4187669de10ddcd58aeb8fadf.jpg)  
(f) Diagnostic odds ratio values for Yeast GIN dataset  
Fig. 6. (continued)

Similarly, Fig. 5.1(d) to (f) show the performance of diferent algorithms for the Slashdot Zoo dataset. From the results, we can see that the performance of the NPECF is better as compared to NbA and SRWR. Fig. 5.2 shows the performance of the algorithms for the Wikipedia RfA and Yeast GIN datasets. From the results, we can see that the performance of NPECF is better as compared to other algorithms.

## 6.2. Results for imbalanced case

Fig. 6.1 and Fig. 6.2 shows the Accuracy, Geometric Mean and

Diagnostic Odds Ratio charts for all four datasets used in the experiments. From the results, we can see that the performance of NPECF is significantly better than SRWR and NbA. Since NbA was not able to classify all the unlabeled edges in the network, therefore, we could compare only NPECF and SRWR using Geometric Mean and Diagnostic Odds Ratio.

## 6.3. Discussion

As we can see from the charts that when many edges are unlabeled then the accuracy of the NbA approach would be low and Aggarwal et al. [1] have already mentioned that in their paper. The approach proposed by Aggarwal et al. [1] is primarily based on the information of the labeled edges on the same node on which unlabeled edges are incident. However, in their approach, the labeled information is not being difused in the network, so this limits the accuracy of their approach and performance is get afected when many edges are unlabeled. Also, from the accuracy charts for all datasets, we can see that all unlabeled edges were not classified by NbA in both balanced and unbalanced cases, and therefore the Geometric Mean and Diagnostic Odds Ratio could not be applied to evaluate the performance of NbA.

From the charts, we can see that the performance of SRWR [12] is better than the approach proposed by Aggarwal et al. [1] except for the Wikipedia RfA dataset for the imbalanced case. However, the Accuracy, Geometric Mean and Diagnostic Odds Ratio values of SRWR for clas sification of unlabeled edges would be less than the NPECF. The SRWR utilizes only labeled edges for the prediction of edges in the network along with their sign. Since in their work, all unlabeled edges are removed for the edge classification task, therefore, it results in informa tion loss and when in the network many edges are unlabeled then the accuracy of SRWR would be adversely afected.

The accuracy of the proposed NPECF is better than other methods considered for comparison for all four datasets in both balanced and imbalanced cases. Since NPECF utilizes in a novel way the information of the unlabeled edges to determine the sign, therefore, the information loss in NPECF would be less as compared to SRWR and the approach proposed by Aggarwal et al. [1]. Also, from the Geometric Mean and Diagnostic Odds Ratio it clear that the performance of NPECF is balanced in terms of classifying positive and negative edges in the network.

## 7. Conclusion and future research directions

In this work, we have proposed a network projection-based framework named NPECF for binary classification of edges in unweighted and undirected signed networks. The proposed framework is efective in the prediction of signs of unlabeled edges. This framework utilizes three projections of the given network with very few edges signed to predict the sign of the unlabeled edges in the network. The proposed framework can utilize the information of the unlabeled edges in the network along with the positive and negative labeled edges to predict the sign of the unlabeled edges. This framework is novel in its way to utilize the information of the unlabeled edges to reduce the information loss to improve the accuracy of the classification of edges. The performance of the proposed framework is compared with other contemporary methods for edge classification using four real-world datasets. The accuracy of the proposed framework is higher as compared to the other methods that show the efectiveness of the proposed frame work.

The proposed NPECF framework is for unweighted and undirected signed networks. In the future, we would like to extend the proposed framework to be applicable for the weighted and directed network for sign prediction. Another interesting future research direction could be the extension of the framework for the prediction of weights along with the signs for unlabeled edges in the weighed signed networks.

## References

[1] C. Aggarwal, G. He, P. Zhao, Edge classification in networks, 2016 IEEE 32nd International Conference on Data Engineering (ICDE), IEEE, 2016, pp. 1038–1049.

[2] P. Agrawal, V.K. Garg, R. Narayanam, Link label prediction in signed socia

networks, Proceedings of the Twenty-Third International Joint Conference on Artificial Intelligence, 2013, pp. 2591–2597.

[3] S. Aref, M.C. Wilson, Measuring partial balance in signed networks, J. Complex Netw. 6 (4) (2017) 566–595.

[4] G. Bachi, M. Coscia, A. Monreale, F. Giannotti, Classifying trust/distrust relationships in online social networks, Proceedings of 2012 International Conference on Privacy, Security, Risk and Trust and 2012 International Conference on Socia Computing, IEEE, 2012, pp. 552–557.

[5] S. Bornholdt, Boolean network models of cellular regulation: prospects and lim itations, J. R. Soc. Interface 5 (suppl\_1) (2008) S85–S94.

[6] D. Cartwright, F. Harary, Structural balance: a generalization of Heider’s theory, Psychol. Rev. 63 (5) (1956) 277

[7] H. Fang, G. Guo, J. Zhang, Multi-faceted trust and distrust prediction for recommender systems, Decis. Support. Syst. 71 (2015) 37–47.

[8] R. Guha, R. Kumar, P. Raghavan, A. Tomkins, Propagation of trust and distrust, Proceedings of the 13th International Conference on World Wide Web, ACM, 2004, pp. 403–412.

[9] J. Han, M. Kamber, J. Pei, Classification: basic concepts, Data Mining Concepts and Techniques. Elsevier. 2011. pp. 327–391

[10] F. Heider, Attitudes and cognitive organization, J. Psychol. 21 (1) (1946) 107–112.

[11] G. Jeh, J. Widom, SimRank: a measure of structural-context similarity, Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2002, pp. 538–543.

[12] J. Jung, W. Jin, U. Kang, Random walk-based ranking in signed social networks: model and algorithms, Knowledge and Information Systems, 2019, pp. 1–40.

[13] J. Kunegis, S. Schmidt, A. Lommatzsch, J. Lerner, E.W. De Luca, S. Albayrak Spectral analysis of signed graphs for clustering, prediction and visualization, Proceedings of the 2010 SIAM International Conference on Data Mining, Society for Industrial and Applied Mathematics, 2010, pp. 559–570.

[14] J. Leskovec, D. Huttenlocher, J. Kleinberg, Signed networks in social media, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2010, pp. 1361–1370

[15] J. Leskovec, D. Huttenlocher, J. Kleinberg, Predicting positive and negative links in online social networks, Proceedings of the 19th international conference on World Wide Web, ACM, 2010, pp. 641–650.

[16] M. Nickel, K. Murphy, V. Tresp, E. Gabrilovich, A review of relational machine learning for knowledge graphs, Proc. IEEE 104 (1) (2015) 11–33

[17] C. Stark, B.J. Breitkreutz, T. Reguly, L. Boucher, A. Breitkreutz, M. Tyers, BioGRID: a general repository for interaction datasets, Nucleic Acids Research 34 (suppl 1) (2006) D535–D539.

[18] J. Tang, Y. Chang, C. Aggarwal, H. Liu, A survey of signed network mining in social media, ACM Comput. Surv. 49 (3) (2016) 42.

[19] J. Tang, C. Aggarwal, H. Liu, Recommendations in signed social networks, Proceedings of the 25th International Conference on World Wide Web. ACM. 2016 pp. 31–40.

[20] J. Tang, C. Aggarwal, H. Liu, Node classification in signed social networks, Proceedings of the 2016 SIAM International Conference on Data Mining, Society for Industrial and Applied Mathematics, 2016, pp. 54–62.

[21] A. Tharwat, Classification assessment methods, Applied Computing and Informatics. 2018

[22] P.J. Tremblay. G.A. Cheston. Graphs. Data Structures and Software Development ir an Obiect-Oriented Domain. Pearson Education India, 2003, pp. 825–920.

[23] Z. Wu, C.C. Aggarwal, J. Sun, The troll-trust model for ranking in signed networks, Proceedings of the Ninth ACM International Conference on Web Search and Data Mining, ACM. 2016, pp. 447–456.

[24] S.H. Yang, A.J. Smola, B. Long, H. Zha, Y. Chang, Friend or frenemy? Predicting signed ties in social networks, Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2012, pp. 555–564.

[25] W. Yuan, C. Li, G. Han, D. Guan, L. Zhou, K. He, Negative sign prediction for signed social networks, Futur, Gener, Comput, Syst. 93 (2019) 962–970.

[26] J. Zhou, L. Li. A. Zeng, Y. Fan, Z. Di, Random walk on signed networks, Physica A 508 (2018) 558–566.

Mukul Gupta is currently working as an Assistant Professor in Information Systems area at Indian Institute of Management Indore, India. He received his Ph.D. in Information Technology and Systems area from Indian Institute of Management Lucknow, India, He did his M.Tech from Davalbagh Educational Institute, India in Computer Science and B.Tech in Computer Science and Engineering, His current research interest includes e-Commerce, Recommendation Systems, Information Networks, Machine Learning, Social Media Analytics, Web and Data Mining.

Raihans Mishra is an Associate Professor in Information Systems Area at Indian Institute of Management Indore (India). He has also served as a visiting faculty at Indian Institute of Management Ahmedabad and Indian Institute of Management Lucknow. His research interest includes recommendation systems, web mining, data mining, text mining, e-Governance and business analytics.
