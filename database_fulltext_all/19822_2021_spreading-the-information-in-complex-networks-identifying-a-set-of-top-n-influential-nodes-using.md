---
otero_id: 19822
otero_key: "6RT7WBHZ"
title: "Spreading the information in complex networks: Identifying a set of top-N influential nodes using network structure"
authors: "Mukul Gupta; Rajhans Mishra"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113608"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spreading the information in complex networks: Identifying a set of top-N influential nodes using network structure

Mukul Gupta , Rajhans Mishra

Indian Institute of Management Indore, Information Systems Area, Indore, India

## A R T I C L E I N F O

Keywords: Complex networks Information propagation Network structure Top-N influential nodes Node ranking

## A B S T R A C T

The real world contains many complex networks, including research networks, social networks, biological net works, and transport networks. Real-world complex networks are unconstrained and can be characterized as undirected and unweighted. Understanding and controlling the process of information propagation in such networks is significant for decision-making activities and has many uses, such as disease control, market advertising, rumor control, and innovation propagation. Identifying the influencers in complex networks is an important activity, as influencers play a key role in spreading information to aid the decision-making process. In this study. we consider the problem of identifving a set of top-N influential nodes for spreading the information in undirected and unweighted networks using the network structure in the absence of domain-specific knowledge. In this study, we propose a novel method that computes the ranking scores of the nodes in the network and considers the influence of other nodes simultaneously when forming the set of top-N influential nodes. The proposed method is different from other methods of identification of influential nodes in the network, in that it takes into consideration the position of the nodes in the network while computing the ranking score, thereby preventing the clustering of important nodes, which hampers the information flow. Experiments are performed using several real-world complex networks to demonstrate the effectiveness of the proposed method.

## 1. Introduction

The decision-making process in a network structure depends on the information flow in the network. In real-world complex networks, influencers moderate the flow of information, and identifying the influencers is a critical task for decision support activities [8,20]. Most real-world phenomena, including friendship, biological interaction, transport infrastructure, and research collaboration, can be represented easily and naturally using complex network structures [4,5,21]. The objects in these real-world phenomena are represented as nodes and their interactions as links between those nodes [4,21]. Most of the time, these interactions are bidirectional and have no weightage as such, leading to undirected and unweighted networks like Facebook friend ship networks, gene–gene interaction networks, co-authorship net works, and many more [8,9,11]. In these real-world complex networks, understanding and controlling information propagation is significant for many real-world applications, such as disease control, market adver tising, rumor control, and innovation propagation [12,16,18].

To control and understand the information propagation behavior of nodes in real-world complex networks, we need to identify influential/ important nodes in the network [13,14]. The spread of information is important for decision-making in a complex network. A faster and greater information flow will lead to more accuracy in decision-making in the network [12,15]. Identifying the right set of influencers can support faster information flow, which in turn supports the decisionmaking process. Different networks have domain-specific properties that result in domain-specific influencer identification processes [17]. However, having a domain-independent method of influencer identifi cation provides versatility; the availability of domain-specific informa tion for various real-world complex networks, like gene–gene interaction networks and behavioral interaction networks, may not be present or may be difficult to obtain, thus limiting the applicability of methods that require domain-specific information to find the influential nodes [11,16].

In this study, the proposed method considers only the network structure for identifying the top-N influential nodes in the network and does not require the domain-specific knowledge of the network for the identification of influential nodes. Collection of domain-specific knowledge of a network is cumbersome and may limit the applicability of the domain-specific methods. The primary research aim is to find the influential nodes in a real-world complex network using a method that is domain-independent and therefore can easily be used in real-world complex networks. Identifying the top-N influential nodes is an impor tant activity for controlling and analyzing the information flow in the network.

![](/api/attachments/6RT7WBHZ/fulltext/images/a976812f80ceb79756e89eac5bd0f2506fd2ad2b2b0420fbbd1652071588e7de.jpg)  
Fig. 1. Finding the top two (N = 2) influential nodes in a toy network.

Most previous studies on finding the top-N influential nodes have computed the ranking scores of nodes in isolation, meaning that the ranking of a node is performed independently of other nodes [18,21]. However, in reality, this is not the case. If high-ranked nodes are in proximity (i.e., clustered in the network and not scattered over the whole network), then the selection of top-N nodes may not be effective, as the coverage from those nodes for information propagation in the network will not be high. However, if the method selects the influential nodes in such a way that the nodes are scattered over the whole network, then the information propagation may be faster [9].

For example, consider the network shown in Fig. 1(a). In the network, there are thirteen nodes and twenty edges. If we find a set of the top two (N = 2) influential nodes, then it may be possible that many algorithms would suggest nodes $\nu _ { 4 }$ and $\nu _ { 5 }$ due to the network structure and structural properties of these two nodes. However, it is obvious that information propagation in the network using these two nodes would not be faster, as the nodes are clustered, and therefore the coverage may not be high. In another case, shown in Fig. 1(b), the two nodes that are selected for information propagation are $\nu _ { 4 }$ and $\nu _ { 1 1 }$ . Since these two nodes are important from the point of view of network structure and location in the network, the information propagation from these two nodes will be faster than in the previous case. It follows that the selection of the nodes for information propagation in a set should not be carried out in isolation, but that each node should be considered in the set.

We propose a novel method for finding the set of top-N influential nodes in complex real-world undirected and unweighted networks. To find the influential nodes, the proposed method requires only the network structure and thus has wide applicability in different domains without the need for domain-specific knowledge. It performs the k-core decomposition [10] of the network and then computes the normalized iteration multiplier (NIM) to compute the iteration number at which the k-core decomposition is performed for all the nodes in the networks. This gives the global importance of the nodes in the network and how they are surrounded by the other nodes in the network. After computing the NIM, the proposed method computes the normalized global impor tance (NGD). which considers the degree of the nodes. k-core decom: position values, and NIM to compute the NGI of the nodes. It also computes the relative local–global importance (RLGI) of nodes by considering the immediate neighborhood. Finally, the normalized ranking scores of nodes are computed.

The expected contribution of this study is a novel method for finding a set of top-N influential nodes in real-world complex networks. The proposed method is domain-independent and does not require node- or network-specific information. It uses only the network structure and a parameter-free technique, efficiently handling both local and global information for the network to compute the ranking scores of the nodes and form a set of top-N influential node nodes. The proposed method is novel in the way it uses the immediate neighborhood of nodes to compute their local importance, thereby preventing the clustering of influential nodes in the network. This will enhance the information propagation speed in the network from the set of top-N influential nodes.

The rest of the paper has the following sections. In Section 2, relevant work from the literature is reviewed. In Section 3, the proposed method is presented. The experimental setup is presented in Section 4. Section 5 gives the results of the experiments, which are then discussed in Section 6. Finally, the paper concludes in Section 7 with recommendations for future research directions.

## 2. Related work

Finding the important/influential nodes in real-world complex net works is an important data mining task, as it has various real-world applications in different domains ranging from social networks to bio logical networks [9,10,13,20]. Various real-world applications, such as disease control, market advertising, rumor control, and innovation propagation, require the identification of a set of influential nodes in the network so that the information can be propagated quickly and cover the maximum number of nodes in the network [14,16]. In this study, we address the problem of finding a set of top-N influential nodes in undi rected and unweighted networks

Various approaches have been used to find the influential nodes in networks according to their assumptions, and different measures of centrality have been proposed to find the influential nodes in the network according to various criteria. Measures such as degree cen trality (DC) [1], closeness centrality (CC) [3], betweenness centrality (BC) [15], and eigenvector centrality (EC) [2] can be used to find the influential nodes. Some of these measures are local and some are global. The local measures use the neighborhood of the node to compute the ranking score, while in the case of global measures the whole network structure is considered for the purposes of computing the ranking score. To apply these measures, knowledge of domain-specific assumptions is required. For example, if a node is considered influential when it is connected to many other nodes in the network, then we can apply the DC measure to rank the nodes [1,19]. However, if a node is considered influential when it is connected to other important nodes, then EC can be applied [2,19]. Thus, these measures are applied effectively if domainspecific information for the network is available.

However, for many real-world networks, domain-specific informa tion is not available or is difficult to acquire, making it difficult to choose the appropriate conventional centrality measures to find the influential nodes [5,19]. Various approaches have been proposed to find the influential nodes in real-world complex networks considering only the network structure. Lü et al. [13] developed a method called LeaderRank

Important notations.  
Table 1 Summary of related work.

<table><tr><td rowspan="2">Method name</td><td colspan="4">Network type</td><td rowspan="2">Summary of method</td><td rowspan="2">Time complexity (m = number of edges, n = number of nodes in the network)</td><td rowspan="2">Limitation(s)</td></tr><tr><td>Directed</td><td>Undirected</td><td>Weighted</td><td>Unweighted</td></tr><tr><td>LeaderRank (LR), Lü et al. [13]</td><td>√</td><td></td><td></td><td>√</td><td>Based on the random walker and utilizes the stochastic matrix to determine the importance of a node</td><td> $O((m + 2n) \cdot T)$ , where  $T$  is the number of iterations</td><td>This method is a variant of the PageRank algorithm, and it emphasizes the incoming links to the node only. It does not consider the outgoing links of a node while computing its importance.</td></tr><tr><td>Extended Gravity Centrality (EGC), Ma et al. [14]</td><td></td><td>√</td><td></td><td>√</td><td>Based on the gravity formula, where it uses k-shell values and the shortest distance between nodes</td><td> $O(n^2)$ </td><td>This method requires the calculation of the shortest distance between nodes, which is time-consuming for large graphs.</td></tr><tr><td>Local Gravity Model (LGM), Li et al. [9]</td><td></td><td>√</td><td></td><td>√</td><td>Based on the gravity formula, where it uses degree values and the shortest distance between nodes</td><td> $O(n^2)$ </td><td>This method requires calculation of the shortest distance between nodes, which is time-consuming for large graphs. The free parameter may impact performance.</td></tr><tr><td>ProfitLeader (PL), Yu et al. [18]</td><td></td><td>√</td><td></td><td>√</td><td>Based on the profit capacity of nodes, where the profit capacity is computed using sharing probability and available resources</td><td> $O(n \cdot \langle k \rangle)$ , where  $\langle k\rangle$  is the average degree of nodes</td><td>The accuracy of the method is not adequate for finding the influential nodes in the network.</td></tr><tr><td>Global Importance of Node (GIN), Zhao et al. [21]</td><td></td><td>√</td><td></td><td>√</td><td>Considers self-importance and global importance in computing the node&#x27;s influence</td><td> $O(n^2)$ </td><td>This method is significantly influenced by closeness centrality, which may affect its accuracy, and it is not applicable to directed and weighted networks.</td></tr><tr><td>Global and Local Structure (GLS), Sheng et al. [16]</td><td></td><td>√</td><td></td><td>√</td><td>Considers local and global influence of the nodes in computing their importance</td><td> $O(n^2)$ </td><td>The accuracy of the method is not adequate for finding the influential nodes in the network.</td></tr><tr><td>Generalized Mechanics Model (GMM), Liu et al. [11]</td><td></td><td>√</td><td></td><td>√</td><td>Uses local and global information of the node in the network to compute its importance</td><td> $O(n_k \cdot (2n^2 + m))$ </td><td>This method requires the computation of eigenvectors and the shortest distance between nodes, which is time-consuming.</td></tr></table>

## Table 2

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $G = (V,E)$ </td><td>Undirected and unweighted graph</td></tr><tr><td> $V, E$ </td><td>Set of nodes and set of edges in  $G$ </td></tr><tr><td> $n (=|V|), m (=|E|)$ </td><td>Number of nodes and number of edges in  $G$ </td></tr><tr><td> $A \in \{0,1\}^{n \times n}$ </td><td>Adjacency matrix</td></tr><tr><td> $A_{ij} \in \{0,1\}$ </td><td>Relationship between nodes  $v_i$  and  $v_j$ </td></tr><tr><td> $v_i \in V$ </td><td> $i^{th}$  node in the network</td></tr><tr><td> $m_k$ </td><td>Total number of iterations to remove the k-degree nodes in the network</td></tr><tr><td> $n^k$ </td><td>Number of iterations to remove the  $k^{th}$  degree node in the network</td></tr><tr><td> $\delta_i$ </td><td>Normalized iteration multiplier for node  $v_i$ </td></tr><tr><td> $\Gamma(v_i)$ </td><td>Neighborhood of node  $v_i$ </td></tr></table>

(LR), which is based on the random walker and uses the stochastic matrix to decide the importance of a node in the network. It is a global measure that utilizes the whole network structure for node ranking. This method is a variant of the PageRank algorithm, and it emphasizes only the incoming links to the node. It does not consider the outgoing links of a node while computing its importance and is applicable also to weighted networks.

Another approach, Extended Gravity Centrality (EGC), proposed by Ma et al. [14]. is based on the gravity formula and uses k-shell values and the shortest distance between nodes. This approach is based on the global network structure and can be extended to weighted networks [14]. It requires the calculation of the shortest distance between nodes, which is time-consuming for large graphs. Li et al. [9] proposed a method called the Local Gravity Model (LGM), which is based on the gravity formula and uses degree values and the shortest distance between nodes. LGM also requires the calculation of the shortest dis tance between nodes, which again is time-consuming for large graphs. Moreover, it has a free parameter that may impact its performance.

The approach proposed by Yu et al. [18], called ProfitLeader (PL), finds the influential nodes in real-world complex networks considering only the network structure. This method is based on the profit capacity of nodes, where the profit capacity is computed using sharing proba bility and available resources. Although this approach is efficient, the accuracy of the method in finding the influential nodes in the network is not adequate. Zhao et al. [21] proposed an approach based on the global network structure, the so-called Global Importance of Node (GIN). This method considers self-importance and global importance when computing the node influence. It is significantly influenced by the closeness centrality, which may affect its accuracy.

A method based on the local and global structure of the network was then proposed by Sheng et al. [16]: Global and Local Structure (GLS) which considers the local and global influence of the nodes to calculate their importance. However, the accuracy of the method is not adequate; it is also inefficient and time-consuming for large graphs. Liu et al. [11] proposed the Generalized Mechanics Model (GMM) model, which uses both local and global information in the network to compute the node’s importance and can be applied to weighted networks. This method in volves computing the shortest distance between nodes and requires ei genvectors to be computed, which is time-consuming. Table 1 summarizes these earlier attempts to find the influential nodes in realworld complex networks.

The present study offers a novel method for finding the set of top-N influential nodes in real-world complex networks that takes into account the limitations of earlier attempts. The proposed method uses both local and global information for the nodes in the network to compute their ranking score. It does not require domain-specific information related to nodes and edges in the network to do this, and it is parameter-free.

Therefore, the proposed method is generalizable and can be applied to real-world complex networks; it is efficient and can be applied to large graphs; and it is novel in the way it uses the immediate neighborhood of nodes to compute their local importance, thereby preventing the clus tering of influential nodes and enhancing the information propagation speed and coverage in the network.

## 3. The proposed method

We first present the background of the study to understand the proposed method for finding the top-N influential nodes in real-world complex networks.

## 3.1. Background and preliminaries

The background, mathematical notations, and important definitions are presented in this section. Some important and frequent notation used in this paper are listed in Table 2.

Definition 1 [19] concerns unweighted and undirected networks:

Definition 1 (Unweighted and Undirected Network). An un weighted and undirected real-world complex network is depicted as a graph $G = ( V , E )$ and the adjacency matrix $A \in \{ 0 , 1 \} ^ { n \times n }$ representing relationships between nodes as follows:

$$
A _ {i j} = \left\{ \begin{array}{c} 1, i f v _ {i} a n d v _ {j} h a v e r e l a t i o n s h i p \\ 0, i f v _ {i} a n d v _ {j} h a v e n o r e l a t i o n s h i p \end{array} \right.
$$

Many real-world networks are undirected and unweighted [4,19]. These networks can be represented using the adjacency matrix. In the adjacency matrix, a value of 1 is used to represent the presence of a relationship between a pair of nodes, and a value of 0 is used to represent the absence of a relationship. Since the relationship has no weightage, only 1 is used to represent its presence. In the case of undirected and unweighted networks, the adjacency matrix is symmetric and binary [19].

In this study, the problem of finding a set of top-N influential nodes in an unweighted and undirected real-world complex network is defined as follows [11,16]:

Definition 2 (Influential nodes). For an unweighted and undi rected network, $G = ( V , E ) ,$ , the problem of identification of a set of top-N influential nodes for information propagation is to determine the ranking scores of all nodes in the network and select the top-N nodes.

In the real world, networks represent the relationships between ob jects, and the task is to find the set of top-N influential nodes (i.e., to find the top-N nodes according to ranking scores that would propagate the information in the network very quickly).

## 3.2. Proposed method

This section discusses the proposed method for finding a set of top-N influential nodes in real-world complex networks. An illustration is provided to clarify how the method works.

![](/api/attachments/6RT7WBHZ/fulltext/images/95f4b67749376345063d80dda97d5e779252edd47ae09930d27978142e838829.jpg)  
Fig. 2. Toy network for illustration.

The method is novel in terms of using the network structure. Local and global information for nodes is used simultaneously to determine the ranking scores, and the nodes are ranked in such a way that there is no clustering of influential nodes. This improves performance in terms of faster information propagation. The proposed method performs the kcore decomposition [10] of the nodes in the network as follows. First, remove all the nodes with degree 1 (1-core decomposition) and keep removing nodes until all the nodes have degree greater than 1. Repeat the process for the rest of the nodes to form different k-core values of the network. Then compute the NIM to determine the iteration number at which the node is removed from the network while performing the kcore decomposition. This is defined as follows:

Definition 3. Given a complex network $\mathbf { G } = ( \mathsf { V } , \mathbf { E } ) ;$ , during the pro cess of k-core decomposition for the k-degree iteration, the total number of iterations is $m _ { k } ,$ and node $\mathbf { v _ { i } } \in \mathbf { V }$ is removed in iteration number $n ^ { k } .$ Then $1 \leq  { \mathbf { n } } ^ { \mathrm { k } } \leq  { \mathbf { m } } _ { \mathrm { k } }$ and the normalized iteration multiplier (NIM) is defined as

$$
\delta_ {i} = \left(1 + \frac {n ^ {k}}{\max (m _ {k})}\right)\tag{1}
$$

where max(m ) is the maximum number of total iterations for any k.

The NIM computes the normalized iteration number at which a node is removed from the network while performing k-core decomposition. By computing the NIM, we determine how important a node is and what its normalized k-core value in the network is. A node with a higher NIM is important in the network from a global perspective, as the NIM computes the global significance/importance of the node.

The proposed approach uses the NIM alongside the degree of node and the k-core decomposition value to compute the normalized global importance (NGI) as follows:

$$
N G I (v _ {i}) = \frac {\deg (v _ {i}) ^ {*} K D (v _ {i}) ^ {*} \delta_ {i}}{| V |}\tag{2}
$$

The NGI computes the global importance by normalizing the NIM using the size of the network. The NGI combines the local and the global significance of the nodes to compute their global importance in the network. From the NGI, the proposed approach then computes the relative local–global importance (RLGI), taking into account the im mediate neighborhood of the nodes to prevent clustering of the influ ential nodes. The RLGI is computed as follows:

$$
R L G I (v _ {i}) = \frac {N G I (v _ {i}) ^ {*} d e g (v _ {i})}{\sum_ {\forall j \in \Gamma (v _ {i})} N G I (v _ {i})}\tag{3}
$$

Using the RLGI, the clustering of important nodes is prevented by discounting the NGI of a node using the total NGI of its neighborhood. If a node a surrounded by other important nodes according to NGI, then its importance is discounted. From this, normalized ranking scores for the nodes are computed, allowing the selection of the top-N influential nodes in the network.

The proposed method is effective in finding the set of top-N nodes by combining the local and global network structure for the nodes. It is also scalable, as the time complexity is O(n). The computation of the NIM is performed in O(n); since the degree computation of nodes in networks is linear and takes time in the order of O(n) and the k-core decomposition takes O(n) time, the computation of NGI will be linear in time complexity and will be O(n). The RLGI requires consideration of the immediate neighborhood of nodes, which takes O(n) time. Hence, the proposed method effectively takes linear time, and the time complexity is O(n). This makes the method effective, and it is faster than many previously proposed methods. The algorithm for the proposed method is given below:

```txt
Algorithm
Input:
G = (V, E): undirected and unweighted network
N: number of influential spreaders in the network
Output:
RS_N: top-N influential spreaders in the network
Begin
1. For ∀v_i ∈ V, compute
    KD(v_i) ← K - core decomposition(v_i)
2. For ∀v_i ∈ V, compute δ_i using Eq. (1)
3. Compute normalized global importance (NGI) for ∀v_i ∈ V as follows:
    NGI(v_i) = \frac{deg(v_i) * KD(v_i) * δ_i}{|V|}
4. Compute relative local–global importance (RLGI) for ∀v_i ∈ V as follows:
    RLGII(v_i) = \frac{NGI(v_i) * deg(v_i)}{\sum_{j∈Γ(v_i)} NGI(v_i)}
5. Compute ranking score (RS) for ∀v_i ∈ V as follows:
    RS(v_i) = \frac{RLGI(v_i)}{max(RLGI)}
6. Return top-N influential nodes RS_N according to the ranking scores.
End
```

## 3.3. Illustration

The toy network shown in Fig. 2 clarifies the functioning of the proposed method. The network has fourteen nodes and eighteen edges. We have to find the influential nodes, or, in other words, we have to determine the ranking scores so that we can find the top-N influential nodes from the network.

For the network shown in Fig. 2, we apply the proposed algorithm in a stepwise manner as follows.

Step 1 and Step 2. On the given network, compute the k-core decomposition (KD) and NIM for all the nodes. The values are given below:

<table><tr><td>Node</td><td> $v_1$ </td><td> $v_2$ </td><td> $v_3$ </td><td> $v_4$ </td><td> $v_5$ </td><td> $v_6$ </td><td> $v_7$ </td><td> $v_8$ </td><td> $v_9$ </td><td> $v_{10}$ </td><td> $v_{11}$ </td><td> $v_{12}$ </td><td> $v_{13}$ </td><td> $v_{14}$ </td></tr><tr><td> $deg(v_i)$ </td><td>1</td><td>2</td><td>3</td><td>5</td><td>4</td><td>3</td><td>6</td><td>2</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $KD(v_i)$ </td><td>1</td><td>1</td><td>2</td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\delta_i$ </td><td>1.5</td><td>2</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>2</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td></tr></table>

Step 3. Compute the NGI for each node in the network:

<table><tr><td>Node</td><td> $NGI(v_i) = \frac{deg(v_i)*KD(v_i)*\delta_i}{|V|}$ </td><td>Node</td><td> $NGI(v_i) = \frac{deg(v_i)*KD(v_i)*\delta_i}{|V|}$ </td></tr><tr><td> $v_1$ </td><td> $\frac{1*1*1.5}{14} = 0.107$ </td><td> $v_8$ </td><td> $\frac{2*2*1.5}{14} = 0.429$ </td></tr><tr><td> $v_2$ </td><td> $\frac{2*1*2}{14} = 0.286$ </td><td> $v_9$ </td><td> $\frac{3*1*2}{14} = 0.429$ </td></tr><tr><td> $v_3$ </td><td> $\frac{3*2*1.5}{14} = 0.643$ </td><td> $v_{10}$ </td><td> $\frac{3*2*1.5}{14} = 0.643$ </td></tr><tr><td> $v_4$ </td><td> $\frac{5*3*1.5}{14} = 1.607$ </td><td> $v_{11}$ </td><td> $\frac{1*1*1.5}{14} = 0.107$ </td></tr><tr><td> $v_5$ </td><td> $\frac{4*3*1.5}{14} = 1.286$ </td><td> $v_{12}$ </td><td> $\frac{1*1*1.5}{14} = 0.107$ </td></tr><tr><td> $v_6$ </td><td> $\frac{3*3*1.5}{14} = 0.964$ </td><td> $v_{13}$ </td><td> $\frac{1*1*1.5}{14} = 0.107$ </td></tr><tr><td> $v_7$ </td><td> $\frac{6*3*1.5}{14} = 1.929$ </td><td> $v_{14}$ </td><td> $\frac{1*1*1.5}{14} = 0.107$ </td></tr></table>

Step 4. Compute the RLGI:

<table><tr><td>Node</td><td> $RLGI(v_i) = \frac{NGI(v_i)*deg(v_i)}{\sum_{\forall j \in \Gamma(v_i)} NGI(v_i)}$ </td><td>Node</td><td> $RLGI(v_i) = \frac{NGI(v_i)*deg(v_i)}{\sum_{\forall j \in \Gamma(v_i)} NGI(v_i)}$ </td></tr><tr><td> $v_1$ </td><td> $\frac{0.107*1}{0.286} = 0.375$ </td><td> $v_8$ </td><td> $\frac{0.429*2}{2.571} = 0.333$ </td></tr><tr><td> $v_2$ </td><td> $\frac{0.286*2}{0.75} = 0.762$ </td><td> $v_9$ </td><td> $\frac{0.429*3}{2.143} = 0.6$ </td></tr><tr><td> $v_3$ </td><td> $\frac{0.643*3}{3.179} = 0.607$ </td><td> $v_{10}$ </td><td> $\frac{0.643*3}{2.464} = 0.783$ </td></tr><tr><td> $v_4$ </td><td> $\frac{1.607*5}{4.929} = 1.63$ </td><td> $v_{11}$ </td><td> $\frac{0.107*1}{0.643} = 0.167$ </td></tr><tr><td> $v_5$ </td><td> $\frac{1.286*4}{5.143} = 1$ </td><td> $v_{12}$ </td><td> $\frac{0.107*1}{0.429} = 0.25$ </td></tr><tr><td> $v_6$ </td><td> $\frac{0.964*3}{4.821} = 0.6$ </td><td> $v_{13}$ </td><td> $\frac{0.107*1}{0.429} = 0.25$ </td></tr><tr><td> $v_7$ </td><td> $\frac{1.929*6}{5.357} = 2.16$ </td><td> $v_{14}$ </td><td> $\frac{0.107*1}{1.607} = 0.067$ </td></tr></table>

Step 5. From the RLGI, compute the RS of the nodes:

<table><tr><td>Node</td><td> $RS(v_i) = \frac{RLGI(v_i)}{max(RLGI)}$ </td><td>Node</td><td> $RS(v_i) = \frac{RLGI(v_i)}{max(RLGI)}$ </td></tr><tr><td> $v_1$ </td><td> $\frac{0.375}{2.16} = 0.174$ </td><td> $v_8$ </td><td> $\frac{0.333}{2.16} = 0.154$ </td></tr><tr><td> $v_2$ </td><td> $\frac{0.762}{2.16} = 0.353$ </td><td> $v_9$ </td><td> $\frac{0.6}{2.16} = 0.278$ </td></tr><tr><td> $v_3$ </td><td> $\frac{0.607}{2.16} = 0.281$ </td><td> $v_{10}$ </td><td> $\frac{0.783}{2.16} = 0.363$ </td></tr><tr><td> $v_4$ </td><td> $\frac{1.63}{2.16} = 0.755$ </td><td> $v_{11}$ </td><td> $\frac{0.167}{2.16} = 0.077$ </td></tr><tr><td> $v_5$ </td><td> $\frac{1}{2.16} = 0.463$ </td><td> $v_{12}$ </td><td> $\frac{0.25}{2.16} = 0.116$ </td></tr><tr><td> $v_6$ </td><td> $\frac{0.6}{2.16} = 0.278$ </td><td> $v_{13}$ </td><td> $\frac{0.25}{2.16} = 0.116$ </td></tr><tr><td> $v_7$ </td><td> $\frac{2.16}{2.16} = 1$ </td><td> $v_{14}$ </td><td> $\frac{0.067}{2.16} = 0.031$ </td></tr></table>

Step 6. From the RS of the nodes, find the top-N influential nodes in

Table 3  
Real-world networks used for experiments.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Description</td><td rowspan="2"> $n(|V|)$ </td><td rowspan="2"> $m(|E|)$ </td><td rowspan="2"> $\langle k\rangle$ </td><td rowspan="2"> $k_{max}$ </td><td rowspan="2">CC</td><td colspan="2">Size of LCC</td></tr><tr><td> $n(|V|)$ </td><td> $m(|E|)$ </td></tr><tr><td>Zachary-Karate-Club $^{a}$ </td><td>Karate club network of a university collected by Zachary</td><td>34</td><td>78</td><td>4.5882</td><td>17</td><td>0.2556</td><td>34</td><td>78</td></tr><tr><td>Jazz $^{a}$ </td><td>Collaboration network between jazz musicians</td><td>198</td><td>2742</td><td>27.697</td><td>100</td><td>0.5202</td><td>198</td><td>2742</td></tr><tr><td>USAir97 $^{b}$ </td><td>US Air Flights infrastructure network</td><td>332</td><td>2126</td><td>12.8072</td><td>139</td><td>0.3963</td><td>332</td><td>2126</td></tr><tr><td>Network-Science $^{a}$ </td><td>Network of co-authorships in network science</td><td>1461</td><td>2742</td><td>3.7536</td><td>34</td><td>0.6934</td><td>379</td><td>914</td></tr><tr><td>Wikipedia-Chameleon $^{c}$ </td><td>Wikipedia page–page network on the topic Chameleon</td><td>2277</td><td>31,371</td><td>27.5547</td><td>732</td><td>0.3136</td><td>2277</td><td>31,371</td></tr><tr><td>Hamsterster-full $^{a}$ </td><td>Links between users of the hamsterster.com</td><td>2426</td><td>16,631</td><td>13.7106</td><td>273</td><td>0.2314</td><td>2000</td><td>16,098</td></tr><tr><td>Oregon-1 $^{c}$ </td><td>Autonomous systems peering information inferred from Oregon route-views from May 26, 2001</td><td>11,174</td><td>23,409</td><td>4.1899</td><td>2389</td><td>0.0096</td><td>11,174</td><td>23,409</td></tr><tr><td>Bio-CE-CX $^{b}$ </td><td>Gene functional associations network</td><td>15,229</td><td>2,45,952</td><td>32.6445</td><td>375</td><td>0.2874</td><td>15,063</td><td>2,45,862</td></tr></table>

http://konect.cc/networks/  
Note: The table gives the number of nodes n(=|V|), edges m(=|E|), average degree $\langle k \rangle _ { ; }$ , maximum degree $k _ { m a x } ,$ clustering coefficient (CC), and size (number of nodes and edges) of the largest connected component (LCC).  
<sup>b</sup> http://networkrepository.com/  
<sup>c</sup> https://snap.stanford.edu/data/

the network by sorting the nodes according to the RS:

<table><tr><td>Node</td><td> $RS(v_i)$ </td><td>Rank</td><td>Node</td><td> $RS(v_i)$ </td><td>Rank</td></tr><tr><td> $v_7$ </td><td>1</td><td>1</td><td> $v_6, v_9$ </td><td>0.278</td><td>7</td></tr><tr><td> $v_4$ </td><td>0.755</td><td>2</td><td> $v_1$ </td><td>0.174</td><td>8</td></tr><tr><td> $v_5$ </td><td>0.463</td><td>3</td><td> $v_8$ </td><td>0.154</td><td>9</td></tr><tr><td> $v_{10}$ </td><td>0.363</td><td>4</td><td> $v_{12}, v_{13}$ </td><td>0.116</td><td>10</td></tr><tr><td> $v_2$ </td><td>0.353</td><td>5</td><td> $v_{11}$ </td><td>0.077</td><td>11</td></tr><tr><td> $v_3$ </td><td>0.281</td><td>6</td><td> $v_{14}$ </td><td>0.031</td><td>12</td></tr></table>

From the above table, we see that $\nu _ { 7 }$ is the most influential node in the network. The spreading ability of v is the highest in the network as per the structural information. Nodes $\nu _ { 6 }$ and v and nodes $\nu _ { 1 2 }$ and $\nu _ { 1 3 }$ are ranked as having equal importance according to the structure of the network.

## 4. Experimental setup

In this section, we discuss the experimental setup applied to eight real-world complex network datasets from various domains ranging from social networks to biological networks. All the experiments in this study to find the influential nodes in the networks were performed on a system using R version 4.0.2.

## 4.1. Datasets

The experiments use real-world datasets that are undirected and unweighted networks from different domains. For these networks, the number of nodes, number of edges, average degree, maximum degree of nodes, and clustering coefficients are listed in Table 3. In this study, we consider the largest connected components of the networks, as the problem under study is how to find the influential nodes for information propagation. The size of the largest connected component (i.e., the number of edges and the number of nodes) is given in Table 3. The log–log degree distribution of the eight datasets is shown in Fig. 3.

The Zachary-Karate-Club is a very famous and highly utilized dataset for various mining tasks. That contains the Karate club network of a university collected by Zachary. In this network. the 34 nodes represent the club members, and the 78 edges represent their interactions outside the club. The Jazz network is a collaboration network between Jazz musicians that represents the musicians as nodes and the collaborations between them as edges. A collaboration occurs if two musicians play together in a band. This network has 198 nodes representing the musi cians and 2742 edges representing the collaborations between them.

USAir97 is an airport transport network dataset with 332 nodes and 2126 edges representing the paths between the source and destination. The Network-Science dataset is a network of co-authorships in the network science domain with 1461 nodes representing researchers and 2742 edges representing co-authorship.

The Wikipedia-Chameleon dataset has 2277 and 31,371 edges. The nodes in the network represent Wikipedia pages and the edges represent links between pages. The Hamsterster-full network dataset has 2426 nodes representing users of the Hamsterster.com website, with 16,631 edges representing the links between them. The Oregon-1 network dataset is a network of Autonomous Systems peering information inferred from Oregon route-views from May 26. 2001. This dataset has 11,174 nodes and 23,409 edges. From the domain of biology, the Bio-CE-CX has 15,229 nodes and 2,45,952 edges; the nodes represent genes, and the edges represent the associations of genes in the network.

In the present study, to find the set of top-N influential nodes in each network, the connected graphs were utilized. Of the eight datasets, the Network-Science, Hamsterster-full, and Bio-CE-CX datasets are not connected. Accordingly, we pre-processed these datasets for experi ments, taking the largest connected component (listed in Table 3), and performing a comparison of the proposed method with other algorithms.

## 4.2. Performance evaluation

The performance of the proposed method was then compared with that of several existing techniques for finding the set of top-N influential nodes in a network. These techniques are applicable to unweighted and undirected complex networks and therefore highly relevant to the problem under study. They are also domain-independent and do not require any domain-specific information/assumption for nodes and edges.

• Leader Rank (LR): The leader rank technique is based on a random walk model for finding the influential nodes in real-world complex networks. It is parameter-free and utilizes the stochastic matrix to decide the importance of a node in the network [13].

• Extended Gravity Centrality (EGC): This method is based on the gravity formula where it uses k-shell values and the shortest distance between nodes [14]. The k-shell values are taken as the mass of the nodes, and the distances of the shortest paths are taken as the dis tance between the nodes when computing the gravity.

• Local Gravity Model (LGM): This is based on the gravity formula, using degree values and the shortest distance between nodes [9]. The

![](/api/attachments/6RT7WBHZ/fulltext/images/7879808b572e7f9ed286cf94509b540576e329bd88f5a15fdef24ff19ae8b132.jpg)  
(a) Zachary-Karate-Club

![](/api/attachments/6RT7WBHZ/fulltext/images/0632eaef7e9a6481c215faf62d95259b8384c9fdb07f3043d57d2d33644ac3af.jpg)  
(b) Jazz

![](/api/attachments/6RT7WBHZ/fulltext/images/f9fd283e34d894e34820d3dfa047cfd218d9a62ed1eaed43634d34eafefe4fcd.jpg)  
(c) USAir97

![](/api/attachments/6RT7WBHZ/fulltext/images/2590d60077880181159b9ac483f331b786252f2b1d9521be7c57b0d829abee44.jpg)  
(d) Network-Science

![](/api/attachments/6RT7WBHZ/fulltext/images/bfbb961c1e7b133f0738f72c8703318d9a5b7e67573d542dad952ee480bc3d37.jpg)

![](/api/attachments/6RT7WBHZ/fulltext/images/4788c9f6729369e493fb7867803cf557deee076d60a57f11ee485325cca95c96.jpg)  
(f) Hamsterster-full

(e) Wikipedia-Chameleon  
![](/api/attachments/6RT7WBHZ/fulltext/images/a63cf169dbe7aed460e7c45727693dd4910b616e6b9abde0914f4b64544b434d.jpg)  
(g) Oregon-1

![](/api/attachments/6RT7WBHZ/fulltext/images/91a4d7c92624ac4e43540aad4baa470bf06a5cff2f81fd624b0e8e4d61dd92ed.jpg)  
(h) Bio-CE-CX  
Fig. 3. Log–log degree distribution of the datasets.

LGM uses both neighborhood and path information to measure the importance of nodes in the network.

• ProfitLeader (PL): This method is based on the profit capacity of nodes, where profit capacity is computed using sharing probability and available resources. [18]. This approach is based on the concept of profit given by a node to other nodes in the network. The more profit a node offers to other nodes in the network, the more impor tant it is in the network.

• Global Importance of Node (GIN): This method considers selfimportance and global importance while computing the node influ ence. It is significantly influenced by closeness centrality [21] and can identify the seemingly unimportant nodes that are influential in the network.

• Global and Local Structure (GLS): This method considers the local as well as the global structure of the network. The closeness of nodes to all other nodes in the network is used as a measure of global influ ence, while closeness to nearest neighbors is used as a measure of local influence [16].

• Generalized Mechanics Model (GMM): The proposed model uses both local and global information for the node in the network to compute its importance in the network. It requires eigenvectors and the shortest distance between nodes to be computed [11].

In addition to the above-mentioned methods, we also considered degree centrality (DC) [1], EC [2], and k-shell centrality (KSC) [7] as the baseline methods for the comparison with the proposed approach.

To evaluate the different algorithms, we used the monotonicity index M(X) for a ranking list X of nodes in the network [14], as given below:

$$
M (X) = \left[ 1 - \frac {\sum_ {c \in V} N _ {c} (N _ {c} - 1)}{N (N - 1)} \right] ^ {2}\tag{4}
$$

where the size of the network is N and the number of nodes with the same rank c is $N _ { c } . \operatorname { I f } M ( X ) = 1$ , the ranking algorithm has given a distinct rank to all the nodes in the network (high resolution of the algorithm); if $M ( X ) = 0 ,$ , the ranking algorithm has given the same rank to all the nodes in the network (zero resolution).

In addition to monotonicity, the complementary cumulative distri bution function (CCDF) was utilized for better evaluation of the differ entiation of the ranking list of nodes in the network [6]. The CCDF function captures the distribution of the nodes in the network to different ranks. Methods that rank fewer nodes in the same rank are considered good from the point of view of differentiating the nodes. This is helpful for selecting the top-N nodes from a network based on their rank; if a larger number of nodes have the same rank, then it will not be possible to select a node for that rank value. If more nodes are cumulated in the same rank, then the CCDF function will approach zero quickly, and the slope will be steep [6]. In contrast. uniformly distributed nodes for different ranks will cause the CCDF to have a gradual slope [6].

Differentiation of nodes based on their rank is not sufficient to show the success of a ranking algorithm. Therefore, in addition to mono tonicity and the CCDF, we evaluated the methods based on their ability to spread the information in the networks. A node located at an important position in the complex network has a strong infectious ability and is considered influential [21]. In this study, to evaluate the

Table 4  
Monotonicity values for eight real-world datasets.

<table><tr><td rowspan="2">Method</td><td colspan="8">Dataset</td></tr><tr><td>Zachary-Karate-Club</td><td>Jzz</td><td>USAir97</td><td>Network-Science</td><td>Wikipedia-Chameleon</td><td>Hamsterster-full</td><td>Oregon-1</td><td>Bio-CE-CX</td></tr><tr><td>Proposed</td><td>0.976961</td><td>0.999282</td><td>0.998363</td><td>0.997112</td><td>0.999465</td><td>0.999673</td><td>0.999877</td><td>0.999988</td></tr><tr><td>LR</td><td>0.950712</td><td>0.990537</td><td>0.994439</td><td>0.994799</td><td>0.999639</td><td>0.999186</td><td>0.999822</td><td>0.999868</td></tr><tr><td>EGC</td><td>0.948975</td><td>0.999641</td><td>0.99789</td><td>0.998437</td><td>0.999532</td><td>0.999909</td><td>0.999878</td><td>0.999994</td></tr><tr><td>LGM</td><td>1</td><td>0.999179</td><td>0.998417</td><td>0.997405</td><td>0.999472</td><td>0.999656</td><td>0.999894</td><td>0.999998</td></tr><tr><td>PL</td><td>0.980488</td><td>0.999282</td><td>0.998308</td><td>0.997042</td><td>0.999466</td><td>0.999622</td><td>0.999871</td><td>0.999982</td></tr><tr><td>GIN</td><td>1</td><td>0.999282</td><td>0.998381</td><td>0.997405</td><td>0.999471</td><td>0.999656</td><td>0.999893</td><td>0.999998</td></tr><tr><td>GLS</td><td>0.980488</td><td>0.999282</td><td>0.998417</td><td>0.997419</td><td>0.999472</td><td>0.999652</td><td>0.999894</td><td>0.999995</td></tr><tr><td>GMM</td><td>1</td><td>0.999282</td><td>0.998690</td><td>0.997488</td><td>0.999551</td><td>0.999795</td><td>0.999896</td><td>0.999998</td></tr><tr><td>KSC</td><td>0.942041</td><td>0.989924</td><td>0.994003</td><td>0.994716</td><td>0.999125</td><td>0.998999</td><td>0.999821</td><td>0.999867</td></tr><tr><td>EVC</td><td>0.980488</td><td>0.999384</td><td>0.998817</td><td>0.999037</td><td>0.999815</td><td>0.999792</td><td>0.999904</td><td>0.999999</td></tr><tr><td>DC</td><td>0.950711</td><td>0.990536</td><td>0.994438</td><td>0.994799</td><td>0.99914</td><td>0.999013</td><td>0.999821</td><td>0.999867</td></tr></table>

![](/api/attachments/6RT7WBHZ/fulltext/images/a10098319b1c975db1c36361ab4768c0662e58a5c344af2fdf8f5f0e5e45b653.jpg)  
(a) Zachary-Karate-Club

![](/api/attachments/6RT7WBHZ/fulltext/images/e3f5417532355c14472301c671a4ae4f28c443eab3431ae308e9109c176d98c3.jpg)  
(b) Jazz

![](/api/attachments/6RT7WBHZ/fulltext/images/86baab4930592d49d4db72ba85eb56305e91ea5635e57876ce1d0917c0d8c1e5.jpg)

![](/api/attachments/6RT7WBHZ/fulltext/images/776ff74af74b85597e172b315067bf9e7a81e109080f06649718519efbf20d93.jpg)  
(d) Network-Science

(c) USAir97  
![](/api/attachments/6RT7WBHZ/fulltext/images/61524ff7b63906eee6e44a55806f151fa9db76eff1385c2e46c5421acda1ef92.jpg)

![](/api/attachments/6RT7WBHZ/fulltext/images/36e8af7943955293ce900919054dcb262ebfae7a65b17a47cf1fc6a8eac0caa5.jpg)  
(f) Hamsterster-full

(e) Wikipedia-Chameleon  
![](/api/attachments/6RT7WBHZ/fulltext/images/4ae1338606e1dcde7bfc4f13c39535d9d3d1b095469964033b2410fa1a3a16dc.jpg)  
(g) Oregon-1

![](/api/attachments/6RT7WBHZ/fulltext/images/badc637c171df7eb26ca51328fa0939d9bf3f090e5b09c00eb0a1baac91e969c.jpg)  
(h) Bio-CE-CX  
Fig. 4. Complementary cumulative distribution function (CCDF) plots for eight real-world datasets.

infectious ability of the set of top-N nodes in the complex networks, the SI (susceptible–infectious) model was adopted [11,21]. There is a pos itive correlation between the infectious ability of a node in the network and its importance in the network [11]. This means that if a node is important, its ability to spread the infection in the network is high [11,21].

Accordingly, to evaluate the methods, the average infection ability of top-N nodes was considered. The top-10 nodes (N = 10) were selected as initially infected nodes, and the remaining nodes were considered as susceptible nodes in the SI model. At each step, the infectious nodes spread infection to their neighbors according to the spreading proba bility (β) value. As we used the top-N nodes for information dissemi. nation in the network, the focus was on the top-N nodes in the network, where the value of N depends on the application and domain. The value of N is usually not very large, as in real-world scenarios the section and utilization of these influential nodes for information dissemination is

Table 5  
Spread of infection, Zachary-Karate-Club dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>43.16</td><td>54.21</td><td>63.02</td><td>69.96</td><td>75.73</td><td>80.43</td><td>84.19</td><td>87.22</td><td>89.36</td><td>91.28</td></tr><tr><td>LR</td><td>40.81</td><td>50.46</td><td>58.45</td><td>65.22</td><td>71.08</td><td>75.83</td><td>79.95</td><td>83.41</td><td>86.15</td><td>88.63</td></tr><tr><td>EGC</td><td>41.3</td><td>51.37</td><td>59.74</td><td>66.66</td><td>72.75</td><td>77.75</td><td>81.67</td><td>85.04</td><td>87.78</td><td>90.04</td></tr><tr><td>LGM</td><td>40.56</td><td>50.14</td><td>58.08</td><td>64.97</td><td>70.85</td><td>75.66</td><td>79.8</td><td>83.26</td><td>86.21</td><td>88.65</td></tr><tr><td>PL</td><td>40.81</td><td>50.46</td><td>58.45</td><td>65.22</td><td>71.08</td><td>75.83</td><td>79.95</td><td>83.41</td><td>86.15</td><td>88.63</td></tr><tr><td>GIN</td><td>40.56</td><td>50.19</td><td>58.33</td><td>65.26</td><td>71.21</td><td>76.24</td><td>80.29</td><td>83.82</td><td>86.41</td><td>88.68</td></tr><tr><td>GLS</td><td>40.81</td><td>50.46</td><td>58.45</td><td>65.22</td><td>71.08</td><td>75.83</td><td>79.95</td><td>83.41</td><td>86.15</td><td>88.63</td></tr><tr><td>GMM</td><td>39.97</td><td>49.13</td><td>57.12</td><td>63.91</td><td>69.8</td><td>74.95</td><td>79.24</td><td>82.86</td><td>85.74</td><td>88.21</td></tr><tr><td>KSC</td><td>38.96</td><td>47.6</td><td>55.22</td><td>62.06</td><td>68.07</td><td>73.39</td><td>77.99</td><td>81.74</td><td>84.61</td><td>87.26</td></tr><tr><td>EVC</td><td>39.81</td><td>48.89</td><td>56.86</td><td>63.7</td><td>69.78</td><td>74.91</td><td>79.26</td><td>82.84</td><td>85.75</td><td>88.03</td></tr><tr><td>DC</td><td>40.81</td><td>50.46</td><td>58.45</td><td>65.22</td><td>71.08</td><td>75.83</td><td>79.95</td><td>83.41</td><td>86.15</td><td>88.63</td></tr></table>

Table 6  
Spread of infection, Wikipedia-Chameleon dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>24.48</td><td>49.19</td><td>64.24</td><td>71.98</td><td>76.77</td><td>80.4</td><td>83.19</td><td>85.56</td><td>87.56</td><td>89.17</td></tr><tr><td>LR</td><td>32.77</td><td>54.44</td><td>64.68</td><td>70.87</td><td>75.33</td><td>78.81</td><td>81.76</td><td>83.94</td><td>85.99</td><td>87.55</td></tr><tr><td>EGC</td><td>14.12</td><td>25.4</td><td>38.27</td><td>50.78</td><td>60.36</td><td>67.1</td><td>71.93</td><td>75.59</td><td>78.44</td><td>80.66</td></tr><tr><td>LGM</td><td>32.67</td><td>54.65</td><td>64.5</td><td>70.76</td><td>75.35</td><td>78.9</td><td>81.79</td><td>84.02</td><td>86.02</td><td>87.71</td></tr><tr><td>PL</td><td>14.76</td><td>26.09</td><td>39.47</td><td>52.26</td><td>61.71</td><td>67.72</td><td>72.44</td><td>75.99</td><td>78.77</td><td>80.95</td></tr><tr><td>GIN</td><td>31.78</td><td>54.17</td><td>64.23</td><td>70.6</td><td>75.26</td><td>78.88</td><td>81.63</td><td>83.98</td><td>85.83</td><td>87.54</td></tr><tr><td>GLS</td><td>32.95</td><td>54.57</td><td>64.5</td><td>70.73</td><td>75.19</td><td>78.76</td><td>81.72</td><td>83.86</td><td>85.77</td><td>87.36</td></tr><tr><td>GMM</td><td>15.04</td><td>26.35</td><td>39.38</td><td>52.9</td><td>61.73</td><td>68.08</td><td>72.87</td><td>76.3</td><td>79.12</td><td>81.33</td></tr><tr><td>KSC</td><td>12.46</td><td>22.14</td><td>33.31</td><td>45.46</td><td>55.79</td><td>63.43</td><td>68.68</td><td>72.83</td><td>76.13</td><td>78.69</td></tr><tr><td>EVC</td><td>14.79</td><td>26.41</td><td>39.77</td><td>52.42</td><td>61.56</td><td>67.87</td><td>72.45</td><td>76.05</td><td>78.81</td><td>81.11</td></tr><tr><td>DC</td><td>32.77</td><td>54.44</td><td>64.68</td><td>70.87</td><td>75.33</td><td>78.81</td><td>81.76</td><td>83.94</td><td>85.99</td><td>87.55</td></tr></table>

Table 7  
Spread of infection, USAir97 dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>28.73</td><td>45.27</td><td>55.69</td><td>63.26</td><td>69.12</td><td>73.68</td><td>77.39</td><td>80.44</td><td>83.08</td><td>85.21</td></tr><tr><td>LR</td><td>28.85</td><td>44.91</td><td>54.89</td><td>62.14</td><td>67.71</td><td>72.17</td><td>75.78</td><td>78.74</td><td>81.31</td><td>83.44</td></tr><tr><td>EGC</td><td>25.76</td><td>41.96</td><td>52.19</td><td>59.74</td><td>65.63</td><td>70.24</td><td>74.06</td><td>77.27</td><td>79.8</td><td>82.11</td></tr><tr><td>LGM</td><td>28.64</td><td>44.55</td><td>54.47</td><td>61.69</td><td>67.36</td><td>71.69</td><td>75.31</td><td>78.39</td><td>80.96</td><td>83.13</td></tr><tr><td>PL</td><td>28.64</td><td>44.55</td><td>54.47</td><td>61.69</td><td>67.36</td><td>71.69</td><td>75.31</td><td>78.39</td><td>80.96</td><td>83.13</td></tr><tr><td>GIN</td><td>28.64</td><td>44.55</td><td>54.47</td><td>61.69</td><td>67.36</td><td>71.69</td><td>75.31</td><td>78.39</td><td>80.96</td><td>83.13</td></tr><tr><td>GLS</td><td>28.64</td><td>44.55</td><td>54.47</td><td>61.69</td><td>67.36</td><td>71.69</td><td>75.31</td><td>78.39</td><td>80.96</td><td>83.13</td></tr><tr><td>GMM</td><td>28.64</td><td>44.55</td><td>54.47</td><td>61.69</td><td>67.36</td><td>71.69</td><td>75.31</td><td>78.39</td><td>80.96</td><td>83.13</td></tr><tr><td>KSC</td><td>25.56</td><td>41.9</td><td>52.28</td><td>59.93</td><td>65.66</td><td>70.29</td><td>74.07</td><td>77.28</td><td>79.86</td><td>82.19</td></tr><tr><td>EVC</td><td>28.64</td><td>44.55</td><td>54.47</td><td>61.69</td><td>67.36</td><td>71.69</td><td>75.31</td><td>78.39</td><td>80.96</td><td>83.13</td></tr><tr><td>DC</td><td>28.85</td><td>44.91</td><td>54.89</td><td>62.14</td><td>67.71</td><td>72.17</td><td>75.78</td><td>78.74</td><td>81.31</td><td>83.44</td></tr></table>

Table 8  
Spread of infection, Hamsterster-full dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>16.89</td><td>39.49</td><td>54.63</td><td>64.58</td><td>71.27</td><td>76.16</td><td>79.81</td><td>82.71</td><td>85.07</td><td>86.98</td></tr><tr><td>LR</td><td>17.36</td><td>38.84</td><td>53.78</td><td>63.89</td><td>70.75</td><td>75.72</td><td>79.52</td><td>82.46</td><td>84.87</td><td>86.8</td></tr><tr><td>EGC</td><td>13.6</td><td>34.11</td><td>49.69</td><td>60.58</td><td>68.14</td><td>73.69</td><td>77.84</td><td>80.99</td><td>83.63</td><td>85.76</td></tr><tr><td>LGM</td><td>17.36</td><td>38.84</td><td>53.78</td><td>63.89</td><td>70.75</td><td>75.72</td><td>79.52</td><td>82.46</td><td>84.87</td><td>86.8</td></tr><tr><td>PL</td><td>16.47</td><td>37.26</td><td>52.38</td><td>62.7</td><td>69.92</td><td>75.09</td><td>78.94</td><td>82.05</td><td>84.47</td><td>86.48</td></tr><tr><td>GIN</td><td>16.84</td><td>37.99</td><td>52.9</td><td>63.11</td><td>70.21</td><td>75.3</td><td>79.16</td><td>82.16</td><td>84.64</td><td>86.6</td></tr><tr><td>GLS</td><td>16.31</td><td>36.9</td><td>51.93</td><td>62.26</td><td>69.55</td><td>74.74</td><td>78.69</td><td>81.79</td><td>84.3</td><td>86.28</td></tr><tr><td>GMM</td><td>0.55</td><td>0.61</td><td>0.69</td><td>0.8</td><td>1.01</td><td>1.29</td><td>1.86</td><td>2.47</td><td>3.52</td><td>5.24</td></tr><tr><td>KSC</td><td>3.84</td><td>15.56</td><td>33.69</td><td>48.46</td><td>58.82</td><td>66.18</td><td>71.73</td><td>75.9</td><td>79.22</td><td>81.94</td></tr><tr><td>EVC</td><td>16</td><td>36.5</td><td>51.57</td><td>62.02</td><td>69.31</td><td>74.58</td><td>78.59</td><td>81.7</td><td>84.19</td><td>86.24</td></tr><tr><td>DC</td><td>17.36</td><td>38.84</td><td>53.78</td><td>63.89</td><td>70.75</td><td>75.72</td><td>79.52</td><td>82.46</td><td>84.87</td><td>86.8</td></tr></table>

## Table 9

Spread of infection, Oregon-1 dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>8.53</td><td>17.91</td><td>26.69</td><td>34.69</td><td>41.89</td><td>48.32</td><td>54.05</td><td>59.13</td><td>63.63</td><td>67.63</td></tr><tr><td>LR</td><td>8.49</td><td>17.81</td><td>26.61</td><td>34.58</td><td>41.77</td><td>48.2</td><td>53.91</td><td>59</td><td>63.48</td><td>67.5</td></tr><tr><td>EGC</td><td>6.85</td><td>15.95</td><td>24.54</td><td>32.46</td><td>39.65</td><td>46.08</td><td>51.85</td><td>57.04</td><td>61.65</td><td>65.77</td></tr><tr><td>LGM</td><td>8.49</td><td>17.81</td><td>26.61</td><td>34.58</td><td>41.77</td><td>48.2</td><td>53.91</td><td>59</td><td>63.48</td><td>67.5</td></tr><tr><td>PL</td><td>7.95</td><td>17.23</td><td>25.96</td><td>33.9</td><td>41.09</td><td>47.5</td><td>53.23</td><td>58.33</td><td>62.86</td><td>66.91</td></tr><tr><td>GIN</td><td>8.49</td><td>17.81</td><td>26.61</td><td>34.58</td><td>41.77</td><td>48.2</td><td>53.91</td><td>59</td><td>63.48</td><td>67.5</td></tr><tr><td>GLS</td><td>8.43</td><td>17.79</td><td>26.55</td><td>34.53</td><td>41.72</td><td>48.14</td><td>53.86</td><td>58.92</td><td>63.43</td><td>67.45</td></tr><tr><td>GMM</td><td>8.49</td><td>17.81</td><td>26.61</td><td>34.58</td><td>41.77</td><td>48.2</td><td>53.91</td><td>59</td><td>63.48</td><td>67.5</td></tr><tr><td>KSC</td><td>7.27</td><td>16.28</td><td>24.9</td><td>32.81</td><td>39.97</td><td>46.42</td><td>52.12</td><td>57.3</td><td>61.9</td><td>66</td></tr><tr><td>EVC</td><td>8.49</td><td>17.81</td><td>26.61</td><td>34.58</td><td>41.77</td><td>48.2</td><td>53.91</td><td>59</td><td>63.48</td><td>67.5</td></tr><tr><td>DC</td><td>8.49</td><td>17.81</td><td>26.61</td><td>34.58</td><td>41.77</td><td>48.2</td><td>53.91</td><td>59</td><td>63.48</td><td>67.5</td></tr></table>

Table 10  
Spread of infection, Network-Science dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>7.75</td><td>13.48</td><td>19.5</td><td>25.6</td><td>31.48</td><td>37.15</td><td>42.53</td><td>47.58</td><td>52.11</td><td>56.36</td></tr><tr><td>LR</td><td>7.49</td><td>12.89</td><td>18.48</td><td>24.12</td><td>29.77</td><td>35.27</td><td>40.4</td><td>45.41</td><td>50.08</td><td>54.22</td></tr><tr><td>EGC</td><td>3.77</td><td>5.09</td><td>6.51</td><td>8.02</td><td>9.53</td><td>11.15</td><td>12.82</td><td>14.55</td><td>16.14</td><td>17.85</td></tr><tr><td>LGM</td><td>7.33</td><td>12.47</td><td>17.78</td><td>23.13</td><td>28.38</td><td>33.59</td><td>38.52</td><td>43.3</td><td>47.85</td><td>52</td></tr><tr><td>PL</td><td>7.33</td><td>12.47</td><td>17.78</td><td>23.13</td><td>28.38</td><td>33.59</td><td>38.52</td><td>43.3</td><td>47.85</td><td>52</td></tr><tr><td>GIN</td><td>6.83</td><td>11.28</td><td>15.96</td><td>20.62</td><td>25.33</td><td>30.03</td><td>34.74</td><td>39.08</td><td>43.21</td><td>47.29</td></tr><tr><td>GLS</td><td>7.33</td><td>12.47</td><td>17.78</td><td>23.13</td><td>28.38</td><td>33.59</td><td>38.52</td><td>43.3</td><td>47.85</td><td>52</td></tr><tr><td>GMM</td><td>4.4</td><td>6.24</td><td>8.16</td><td>10.11</td><td>12.12</td><td>14.19</td><td>16.22</td><td>18.19</td><td>20.13</td><td>22.04</td></tr><tr><td>KSC</td><td>4.84</td><td>7.25</td><td>9.88</td><td>12.62</td><td>15.36</td><td>18.21</td><td>21.11</td><td>23.81</td><td>26.63</td><td>29.29</td></tr><tr><td>EVC</td><td>4.28</td><td>6</td><td>7.76</td><td>9.54</td><td>11.4</td><td>13.26</td><td>15.19</td><td>16.93</td><td>18.79</td><td>20.71</td></tr><tr><td>DC</td><td>7.49</td><td>12.89</td><td>18.48</td><td>24.12</td><td>29.77</td><td>35.27</td><td>40.4</td><td>45.41</td><td>50.08</td><td>54.22</td></tr></table>

Table 11  
Spread of infection, Jazz dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>50.83</td><td>79.85</td><td>88.67</td><td>92.02</td><td>93.77</td><td>94.84</td><td>95.68</td><td>96.33</td><td>96.8</td><td>97.26</td></tr><tr><td>LR</td><td>48.12</td><td>76.14</td><td>86.53</td><td>90.74</td><td>92.83</td><td>94.12</td><td>95.01</td><td>95.73</td><td>96.33</td><td>96.77</td></tr><tr><td>EGC</td><td>39.18</td><td>70.04</td><td>83.68</td><td>89.4</td><td>91.92</td><td>93.48</td><td>94.49</td><td>95.25</td><td>95.96</td><td>96.45</td></tr><tr><td>LGM</td><td>48.13</td><td>76.31</td><td>86.72</td><td>90.84</td><td>92.91</td><td>94.15</td><td>95.08</td><td>95.83</td><td>96.36</td><td>96.78</td></tr><tr><td>PL</td><td>47.75</td><td>75.86</td><td>86.49</td><td>90.76</td><td>92.8</td><td>94.07</td><td>95.01</td><td>95.72</td><td>96.33</td><td>96.74</td></tr><tr><td>GIN</td><td>48.13</td><td>76.31</td><td>86.72</td><td>90.84</td><td>92.91</td><td>94.15</td><td>95.08</td><td>95.83</td><td>96.36</td><td>96.78</td></tr><tr><td>GLS</td><td>47.58</td><td>76.04</td><td>86.52</td><td>90.7</td><td>92.81</td><td>94.1</td><td>95.02</td><td>95.75</td><td>96.38</td><td>96.79</td></tr><tr><td>GMM</td><td>6.38</td><td>11.96</td><td>24.54</td><td>41.53</td><td>58.61</td><td>72.69</td><td>82.62</td><td>89.82</td><td>93.73</td><td>96.26</td></tr><tr><td>KSC</td><td>40.94</td><td>70.26</td><td>83.37</td><td>89.13</td><td>91.83</td><td>93.28</td><td>94.39</td><td>95.19</td><td>95.8</td><td>96.29</td></tr><tr><td>EVC</td><td>47.78</td><td>76.1</td><td>86.62</td><td>90.76</td><td>92.85</td><td>94.11</td><td>95.07</td><td>95.78</td><td>96.33</td><td>96.82</td></tr><tr><td>DC</td><td>48.12</td><td>76.14</td><td>86.53</td><td>90.74</td><td>92.83</td><td>94.12</td><td>95.01</td><td>95.73</td><td>96.33</td><td>96.77</td></tr></table>

Table 12  
Spread of infection, Bio-CE-CX dataset.

<table><tr><td rowspan="2">Method</td><td colspan="10">Probability of spreading (β)</td></tr><tr><td>0.01 (%)</td><td>0.02 (%)</td><td>0.03 (%)</td><td>0.04 (%)</td><td>0.05 (%)</td><td>0.06 (%)</td><td>0.07 (%)</td><td>0.08 (%)</td><td>0.09 (%)</td><td>0.1 (%)</td></tr><tr><td>Proposed</td><td>22.64</td><td>47.84</td><td>59.86</td><td>67.21</td><td>72.42</td><td>76.35</td><td>79.46</td><td>81.98</td><td>84.09</td><td>85.84</td></tr><tr><td>LR</td><td>22.04</td><td>47.41</td><td>59.62</td><td>67.04</td><td>72.26</td><td>76.22</td><td>79.36</td><td>81.9</td><td>84</td><td>85.76</td></tr><tr><td>EGC</td><td>18.24</td><td>44.41</td><td>57.6</td><td>65.47</td><td>70.94</td><td>75.07</td><td>78.32</td><td>80.96</td><td>83.14</td><td>84.99</td></tr><tr><td>LGM</td><td>22.07</td><td>47.43</td><td>59.61</td><td>67.05</td><td>72.28</td><td>76.23</td><td>79.35</td><td>81.9</td><td>84.01</td><td>85.76</td></tr><tr><td>PL</td><td>19.76</td><td>45.61</td><td>58.43</td><td>66.16</td><td>71.54</td><td>75.6</td><td>78.79</td><td>81.4</td><td>83.56</td><td>85.36</td></tr><tr><td>GIN</td><td>21.91</td><td>47.32</td><td>59.53</td><td>66.98</td><td>72.2</td><td>76.16</td><td>79.3</td><td>81.84</td><td>83.95</td><td>85.71</td></tr><tr><td>GLS</td><td>19.3</td><td>45.27</td><td>58.2</td><td>65.96</td><td>71.38</td><td>75.47</td><td>78.68</td><td>81.29</td><td>83.46</td><td>85.29</td></tr><tr><td>GMM</td><td>19.73</td><td>45.72</td><td>58.48</td><td>66.17</td><td>71.56</td><td>75.63</td><td>78.83</td><td>81.42</td><td>83.58</td><td>85.39</td></tr><tr><td>KSC</td><td>8.03</td><td>34.7</td><td>51.2</td><td>60.69</td><td>67.06</td><td>71.77</td><td>75.45</td><td>78.4</td><td>80.85</td><td>82.92</td></tr><tr><td>EVC</td><td>19.12</td><td>45.1</td><td>58.05</td><td>65.83</td><td>71.26</td><td>75.35</td><td>78.57</td><td>81.18</td><td>83.36</td><td>85.19</td></tr><tr><td>DC</td><td>22.04</td><td>47.41</td><td>59.62</td><td>67.04</td><td>72.26</td><td>76.22</td><td>79.36</td><td>81.9</td><td>84</td><td>85.76</td></tr></table>

costly in terms of time and effort required) [16,18].

## 5. Results

In this section, the results of experiments performed on eight datasets (Zachary-Karate-Club, Jazz, USAir97, Network-Science, Wikipedia-Chameleon, Hamsterster-full, Oregon-1, and Bio-CE-CX) are presented for monotonicity, CCDF, and SI infectious model.

## 5.1. Monotonicity

From Table 4, we see the monotonicity values of various methods for different datasets. The monotonicity index values are very close to 1 (higher the value of M better it is in terms of resolution), which indicates that all the methods were able to give distinct ranks to a significant number of nodes in the network.

From these results, it is clear that the proposed method is effective for resolution of a significant number of nodes in these networks; therefore, using the proposed method, we can select top-N nodes without any problem for even a large value of N. However, it is not possible to compare the methods using the monotonicity index alone, as the dif ferences between the monotonicity values are not significant. We therefore include CCDF and SI model in the comparison.

## 5.2. CCDF

Fig. 4 shows the CCDF plots for the eight datasets. It is clear that the proposed method is able to differentiate the nodes on the basis of the network structure, and that the ranking scores given to nodes in the network will be different in a large number of cases. Profit Leader (PL) was able to give different ranking scores to a larger number of nodes in the network than the other methods. From this point of view, degree centrality (DC) and k-shell centrality (KSC) were the worst-performing methods.

We see that the proposed method was largely able to differentiate the nodes in the network by giving different ranking scores to a large number of nodes. In the real world, for top-N influential nodes selection, the value of N is typically taken as between 10 and 200, depending on the size of the network and the associated cost of selecting the nodes as initial spreaders [11,21]. Considering the practical aspects of the influential node selection problem, we can conclude that the proposed method has performed satisfactorily.

## 5.3. SI infectious model

The results for spreading ability using the SI infectious model are shown in Table 5, 6, 7, 8, 9, 10, 11 and 12. The percentage coverage of each network for different values of spreading probability (β) is given in the tables. Higher coverage (spread) values indicate that the method propagates the information in the network efficiently. For the experi ments, the value of β was varied from 0.01 to 0.1 for different spreading phenomena. A higher value of β indicates that the neighboring nodes have a higher chance of being infected from the currently infected nodes in the network. For SI infectious model, we considered time steps t from 1 to 10, and each experiment for a given value of β was repeated 100 times. The average values are reported in the results [11,21]. To simu late the information-spreading abilities of the nodes and determine which method best finds the influential nodes in the network, ten time steps were taken, as in previous work [11]. By taking an appropriate value for the number of iterations, we were able to compare the results of using each method.

It is clear that the proposed method outperformed all the comparison methods. For the Zachary-Karate-Club, Oregon-1, Network-Science, Jazz, and Bio-CE-CX datasets, for all values of spreading probabilities, the spread percentage from the top 10 nodes from the proposed method was higher than for all the other methods. For the USAir97 and

Hamsterster-full datasets, the proposed method outperformed all the other methods when the value of spreading probability was greater than 0.01. For the Wikipedia-Chameleon dataset, the proposed method out performed all the other methods when the value of the spreading probability was greater than 0.03. For all the datasets, if the spreading condition was appropriate, the proposed method outperformed all the other methods. It is also clear that the proposed method can spread in formation in a real-world complex network for a wide range of spreading conditions simulated through the different values of spreading probabilities.

## 6. Discussion

In this section, we discuss the results of the experiments. As we see from the monotonicity index values and the CCDF plots, the proposed method is able to differentiate the nodes in the network by giving them distinct ranking scores. If a method gives distinct ranking scores to the nodes in a network, then it is possible to select the top-N influential nodes in that network; otherwise, it is not possible to select the top-N nodes, as there will be many nodes for any particular position. From the plots, we see that although the proposed method is not the best of all the methods, it is able to select distinct nodes for a sufficiently large value of N respective to a network. This demonstrates the usability of the pro posed method in real-world applications.

However, the monotonicity index and CCDF are not enough to establish the effectiveness of a given method of information propaga tion, hence we have also used the SI infectious model. The experimental results show that the proposed method outperforms all the other methods. It is effective for a wide range of probabilities, which dem onstrates its effectiveness for the selection of top-N nodes in the network for information propagation.

We also see that the proposed method is effective in finding the influential nodes in the networks. It computes the local as well as the global importance, and on that basis, assigns ranking scores to nodes and thus this work adds to the existing body of literature.

It is parameter-free and independent of domain-specific assump tions, which makes it useful in practical terms for different real-world complex networks, making it very useful for the implementation pur pose. The proposed method is also efficient, can be applied to large graphs, and is novel in the way it uses the immediate neighborhood of nodes to compute their local importance, thereby preventing the clus tering of influential nodes in the network.

## 7. Conclusions and future research

This study develops a novel method for finding the top-N influential nodes in unweighted and undirected real-world complex networks. The proposed method uses only the network structure and does not require domain-specific information related to nodes or networks. It is effective in finding the influential nodes and can propagate information in the network rapidly. It is also scalable, as it has linear time complexity and can be applied to large real-world complex networks. It uses the local and global network structure to find the ranking score of nodes and thereby identify the set of top-N influential nodes in the network. This avoids clustering of the influential nodes in the network and is therefore more effective for information propagation than the other comparison methods. The experiments confirm the effectiveness of the method using several real-world complex networks.

A limitation of the proposed method is that it is applicable only to unweighted and undirected real-world networks; real-world networks may be weighted or directed, or both weighted and directed. Therefore, future research could develop the model by applying it to weighted and directed networks to find the top-N influential nodes. Another inter esting extension of the proposed approach would be to find the seed nodes in social networks for discovering polarized communities.

## References

[1] P. Bonacich, Factoring and weighting approaches to status scores and clique identification, J. Math. Sociol. 2 (1) (1972) 113–120.

[2] P. Bonacich, P. Lloyd, Eigenvector-like measures of centrality for asymmetric relations, Soc. Networks 23 (3) (2001) 191–201.

[3] L.C. Freeman, Centrality in social networks conceptual clarification, Soc. Networks 1 (3) (1978) 215–239.

[4] M. Gupta, P. Kumar, Recommendation generation using personalized weight of meta-paths in heterogeneous information networks, Eur. J. Oper. Res. 284 (2) (2020) 660–674

[5] M. Gupta, R. Mishra, Network projection-based edge classification framework for signed networks. Decis, Support, Syst, (2020) 113321

[6] J.C. Helton, Probability, conditional probability and complementary cumulative distribution functions in performance assessment for radioactive waste disposal, Reliab. Eng. Syst. Saf. 54 (2–3) (1996) 145–163.

[7] M. Kitsak, L.K. Gallos, S. Havlin, F. Liljeros, L. Muchnik, H.E. Stanley, H.A. Makse, Identification of influential spreaders in complex networks, Nat. Phys. 6 (11) (2010) 888–893.

[8] P. Kumar, S. Gupta, B. Bhasker, An upper approximation based community detection algorithm for complex networks, Decis. Support. Syst. 96 (2017) 103–118.

[9] Z. Li, T. Ren, X. Ma, S. Liu, Y. Zhang, T. Zhou, Identifying influential spreaders by gravity model, Sci. Rep. 9 (1) (2019) 1–7.

[10] J.H. Lin, Q. Guo, W.Z. Dong, L.Y. Tang, J.G. Liu, Identifying the node spreading influence with largest k-core values, Phys. Lett, A 378 (45) (2014) 3279–3284.

[11] F. Liu, Z. Wang, Y. Deng, GMM: a generalized mechanics model for identifying the importance of nodes in complex networks, Knowl.-Based Syst. 193 (2020) 105464.

[12] D. Lu, Q. Li, S.S. Liao, A graph-based action network framework to identify prestigious members through member’s prestige evolution, Decis. Support. Syst. 53 (1) (2012) 44–54.

[13] L. Lü, Y.C. Zhang, C.H. Yeung, T. Zhou, Leaders in social networks, the delicious case, PLoS One 6 (6) (2011), e21202.

[14] L.L. Ma, C. Ma, H.F. Zhang, B.H. Wang, Identifying influential spreaders in complex networks based on gravity formula, Physica A: Statistical Mechanics and its Applications 451 (2016) 205–212.

[15] M.E. Newman, A measure of betweenness centrality based on random walks, Soc. Networks 27 (1) (2005) 39–54

[16] J. Sheng, J. Dai, B. Wang, G. Duan, J. Long, J. Zhang, K. Guan, S. Hu, L. Chen, W. Guan, Identifying influential nodes in complex networks based on global and local structure. Physica A: Statistical Mechanics and its Applications 541 (2020 123262.

[17] P. Wang, J. Lü, X. Yu, Identification of important nodes in directed biological networks: a network motif approach, PLoS One 9 (8) (2014), e106132

[18] Z. Yu, J. Shao, Q. Yang, Z. Sun, ProfitLeader: identifying leaders in networks with profit capacity, World Wide Web 22 (2) (2019) 533–553.

[19] R. Zafarani, M.A. Abbasi, H. Liu, Social Media Mining: An Introduction, Cambridge University Press, 2014.

[20] A. Zareie, A. Sheikhahmadi, K. Khamforoosh, Influence maximization in socia networks based on TOPSIS, Expert Syst. Appl. 108 (2018) 96–107

[21] J. Zhao, Y. Wang, Y. Deng, Identifying influential nodes in complex networks from global perspective, Chaos, Solitons Fractals 133 (2020) 109637.

Mukul Gupta is currently working as an Assistant Professor in the Information Systems area at the Indian Institute of Management Indore, India. He received his Ph.D. in Infor mation Technology and Systems area from the Indian Institute of Management Lucknow, India. He did his M.Tech from Dayalbagh Educational Institute, India, in Computer Science and B.Tech in Computer Science and Engineering. His current research interest includes e-Commerce, Recommendation Systems, Information Networks, Machine Learning, Socia Media Analytics, Web and Data Mining.

Rajhans Mishra is an Associate Professor in the Information Systems Area at the Indian Institute of Management Indore (India). He has also served as a visiting faculty at the Indian Institute of Management Ahmedabad and Indian Institute of Management Luck now. His research interest includes recommendation systems, web mining, data mining, text mining, e-Governance and business analytics.
