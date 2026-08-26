---
otero_id: 164
otero_key: "BPFUXKQT"
title: "An upper approximation based community detection algorithm for complex networks"
authors: "Pradeep Kumar; Samrat Gupta; Bharat Bhasker"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.02.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

An upper approximation based community detection algorithm for complex networks

Pradeep Kumar, Samrat Gupta, Bharat Bhasker

![](/api/attachments/BPFUXKQT/fulltext/images/4271d331d31e536f4d8e1e5a20bc4f955439e75ed120c27404b3f6eb4372f0ce.jpg)

PII: S0167-9236(17)30026-X

DOI: doi: 10.1016/j.dss.2017.02.010

Reference: DECSUP 12810

To appear in: Decision Support Systems

Received date: 9 October 2016

Revised date: 5 February 2017

Accepted date: 19 February 2017

Please cite this article as: Pradeep Kumar, Samrat Gupta, Bharat Bhasker , An upper approximation based community detection algorithm for complex networks. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2016), doi: 10.1016/j.dss.2017.02.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# An Upper Approximation based Community Detection Algorithm for Complex Networks

Pradeep Kumar, Samrat Gupta , Bharat Bhasker

IT and Systems Department, Indian Institute of Management Lucknow, India

(pradeepkumar,samratgupta,bhasker)@iiml.ac.in

Abstract. The emergence of multifarious complex networks has attracted researchers and practitioners from various disciplines. Discovering cohesive subgroups or communities in complex networks is essential to understand the dynamics of real-world systems. Researchers have made persistent efforts to investigate and infer community patterns in complex networks. However, real-world networks exhibit various characteristics wherein existing communities are not only disjoint but are also overlapping and nested. The existing literature on community detection consists of limited methods to discover co-occurring disjoint, overlapping and nested communities.

In this work, we propose a novel rough set based algorithm capable of uncovering true community structure in networks, be it disjoint, overlapping or nested. Initial sets of granules are constructed using neighborhood connectivity around the nodes and represented as rough sets. Subsequently, we iteratively obtain the constrained connectedness upper approximation of these sets. To constrain the sets and merge them during each iteration, we utilize the concept of relative connectedness among the nodes. We illustrate the proposed algorithm on a toy network and evaluate it on fourteen real-world benchmark networks. Experimental results show that the proposed algorithm reveals more accurate communities and significantly outperforms state-ofthe-art techniques.

Keywords: Community Structure; Complex Networks; Community Detection Algorithms; Overlapping Communities; Neighborhood Model; Rough Sets

# ACCEPTED MANUSCRIPT

## 1 Introduction

The modern view of data manifests varied interactions taking place in different areas ranging from social sciences to biology [1]. These interactions can be modeled through graphs or networks consisting of nodes and edges. In the contemporary world, Web 2.0 has also led to enormous growth in online networks [2]. Online social networks such as, MySpace, LinkedIn, Facebook and Twitter, have changed the way internet users interact, transact, search and share data. Amidst the advanced data-intensive techniques for investigating complex networks, community detection holds value as it helps in intelligent decision making [2]. Community detection techniques have witnessed a variety of practical applications ranging from photo clustering [3] to tag disambiguation [4] of online content generated on applications such as, Flickr, Delicious and Twitter. Antiterrorism agencies have also used community detection to identify suspicious individuals or groups in a network [5].

Though researchers and practitioners have been addressing the community identification problem for a long time, several issues remain unexplored [1]. The majority of existent community identification algorithms aim at exposing disjoint communities, assigning each node to one community. Moreover, some algorithms need pre-specified parameters like number of communities, some algorithms become intractable for large networks, others work only for a specific domain and some algorithms are insensitive to communities of varying sizes.

In today‟s increasingly interconnected world, traditional silo based approaches may not be able to reveal the true community structure in a network. There could be overlapping and nested communities in a network where an entity has multiple memberships due to diverse roles and relationships. For instance, participation of human beings in the real world is not restricted to one group since they interact with multiple societal groupings such as grade, college, family, nation, profession, ethnic groups etc. Overlapping and nested communities arising due to such shared affiliations are important characteristics of real-world complex networks. Furthermore, an entity in a network may not belong to any community. As shown in Fig. 1, communities B and C are nested within community A, thus forming a nested community structure. Communities A and D are overlapping communities. Similarly E and D are also overlapping communities. Communities A and E are disjoint with respect to each other, and community F is disjoint with respect to all other communities. A few nodes like G and H, which do not belong to any community, may also be present in a network.

![](/api/attachments/BPFUXKQT/fulltext/images/6195115995590fd389c95f38be59159d0a76928be8d6dcdadf10a4b02fa95a72.jpg)  
Fig. 1. Representation of Community Structure within a Network

A community detection scheme must be sensitive to the peculiarities of the network. It must be able to detect disjoint, overlapping and nested subgroups, and should not exhaustively associate each node with a subgroup. The community structure thus detected can help us in exploring the factors defining communities and confronting many real life challenges. For example, if a company wants to perform targeted marketing of products having different characteristics, the characteristics may be mapped to different communities and thus can be recommended to the customer. If characteristics of the products are interrelated, mapping them particularly to overlapping/nested communities might be helpful.

Another application of detecting communities can be seen from online social media where diffusion of information takes place. Firstly, number of communities detected can help in deciding the speed of information diffusion. The content will spread slowly if there are more communities within a network. Disjoint communities will further exacerbate the speed of spread of information as compared to overlapping communities. Secondly, it can be used to understand the behaviour of each group, and the appropriate communication strategy for that group. For instance, a group using a specific language or following a specific account might benefit more from a particular piece of content than another group.

In this work, we have designed a new community detection algorithm and named it ROugh CONnectedness Algorithm (abbreviated as ROCONA). The proposed algorithm, ROCONA is based on an unexplored theoretical cornerstone of rough sets and granular computing in the context of complex networks. The main contributions of this paper are as follows:

1. We propose a parameter-free community detection algorithm for complex networks. ROCONA effectively reveals co - occurring disjoint, overlapping and nested communities without necessarily assigning each node to a community.

2. We introduce the concept of relative connectedness and a measure based on set theory to derive the relative connectedness between nodes of a network. Relative connectedness is used for constraining community components in the course of each iteration of ROCONA.

3. By integrating the strengths of rough clustering and conductance [6], ROCONA overcomes problems that conventional algorithms suffer from. Experiments and comparative analysis on fourteen realworld networks from diverse domains establish the usefulness of ROCONA.

In Section 2, we discuss the state-of-the-art in community detection and rough sets. In Section 3, we present ides the illustration of ROCONA on a toy network. The results of experiments and comparison of ROCONA with relevant state-of-the-art algorithms is presented in presented in Section 5. Section 6 discusses the practical implications of this work. Finally, conclusion and potential future directions are discussed in Section 7.

## 2 Related Work

The notion of cohesive subgroups of humans (also known as communities) has been studied by sociologists since the second half of 20<sup>th</sup> century [7]. With networks attaining increased utility and adoption in the representation of many real-world complex systems, the concept of grouped structures or communities places, proteins, events, topics, web pages, words, photos, videos, tags or any activity. Consequently, a wide range of community detection methods have been proposed and elaborate surveys in the field of community detection have been published by Fortunato [8], Xie et al. [9] and Papadopoulos et al. [3]. Based on these surveys, community detection approaches can be broadly divided into five categories viz., approaches based on quality optimization, clique based approaches, similarity based graph clustering approaches, model based approaches and soft computing approaches. We describe these approaches in the following subsections and list the notations used frequently in this paper in Table 1.

Table 1. Description of Notations

<table><tr><td>Symbol</td><td>Description</td></tr><tr><td> $C(G)$ </td><td>A set of detected communities in  $G$ </td></tr><tr><td> $G = (V, E)$ </td><td>A complex network with  $V$ , a set of vertices and  $E$ , a set of edges</td></tr><tr><td> $D$ </td><td>Domain of discourse</td></tr><tr><td> $N$ </td><td>Neighborhood Relation</td></tr><tr><td> $S(v_i)$ </td><td>Neighborhood Connectedness Subset of vertex  $v_i$ </td></tr><tr><td> $deg(v_i)$ </td><td>Degree of vertex  $v_i$ </td></tr><tr><td> $deg(C_i)$ </td><td>Sum of degrees of vertices in  $C_i$ </td></tr><tr><td> $\overline{S}(v_i)$ </td><td>First Connectedness Upper Approximation of vertex  $v_i$ </td></tr><tr><td> $RelCon(v_i, v_j)$ </td><td>Relative Connectedness between vertices  $v_i$  and  $v_j$ </td></tr><tr><td> $S_c(v_i)$ </td><td>Constrained Connectedness Upper Approximation</td></tr><tr><td> $\phi(C_i)$ </td><td>Conductance of community  $C_i$ </td></tr><tr><td> $|S(v_i)|$ </td><td>Cardinality of subset  $S(v_i)$ </td></tr><tr><td> $Q$ </td><td>Modularity</td></tr><tr><td> $e_{ii}$ </td><td>Percentage of edges in community  $i$ </td></tr><tr><td> $a_i$ </td><td>Percentage of edges with atleast one end in community  $i$ </td></tr><tr><td> $w_{in}^{c_i}$ </td><td>Total internal weight of edges in community  $C_i$ </td></tr><tr><td> $w_{out}^{c_i}$ </td><td>Total external weight of edges in community  $C_i$ </td></tr><tr><td> $r$ </td><td>Resolution Parameter</td></tr><tr><td> $k$ </td><td>Number of communities detected in  $G$ </td></tr></table>

## 2.1 Quality Optimization based Approaches for Community Detection

Several community detection methods operate on the strategy of optimizing a sort of graph-based quality metric as shown in Table 2. For instance, the “modularity” metric [10] has been utilized extensively for developing community detection algorithms. Modularity measures the quality of division of a network into communities by taking the difference between fraction of links that fall within these communities, and the expected fraction if edges were randomly distributed. The value of modularity can be negative or positive, with higher and positive values indicating dense linkages between the nodes of a community, but sparse linkages between nodes in different communities [10]. Modularity was first proposed and used in “edge betweenness” algorithm for detection of disjoint communities [10]. Edge betweenness refers to the number of instances of an edge falling on the shortest paths in a network. Edge betweenness algorithm first computes the betweenness of all network edges and then removes the edge with the highest betweenness. This process is repeated iteratively until the modularity score is maximized. Subsequently, modularity based algorithms

# ACCEPTED MANUSCRIPT

such as, Louvain [11] and Fast modularity (FastQ) [12], were proposed. Louvain first identifies small communities by optimizing modularity locally. Then it aggregates nodes of the same community and builds a new network whose nodes are the communities identified in the first step. This process is repeated iteratively until no increase in modularity is possible. FastQ performs hierarchical agglomeration in a greedy manner. First, each node is assigned to its own community. Then communities (or nodes) connected by an edge are repeatedly merged into a single community such that modularity is maximized. However, modularity based algorithms are exposed to the problem of resolution limit [13] and thus do not ensure correct division of a network. To avoid the drawbacks of modularity, methods based on optimization of other objective functions, as seen in Table 2, have been proposed. Iterative Scan (IS) [14] first ranks the nodes of a network and then prunes the nodes with high rank until compact cluster cores are obtained. In the second step of IS, the cores formed in the first step are expanded iteratively until a density function, shown in Table 2, is maximized. Local Fitness Method (LFM) [15] optimizes a fitness function (Table 2) for expanding locally from a random seed node. Another algorithm operates by unfolding and extracting overlapping communities (UEOC) [16]. UEOC integrates random walk with constrained-optimization based on annealed network [17] to reveal overlapping communities. An algorithm named Order Statistics Local Optimization Method (OSLOM) [18] works by measuring significance of communities with respect to a null model having no community structure [19]. First, it identifies statistically significant communities by agglomerating neighborhood nodes. Then several iterations of adjustments (addition/deletion of nodes) are performed so as to increase the significance of communities identified in the first step. However, all these methods have their own shortcoming(s). IS depends on the quality of cores and in some cases, it also produces disconnected components [9]; LFM identifies one community at a time; both LFM and UEOC are parameter dependent [9,16]; OSLOM is prone to detection of several outliers [9].

Table 2. Quality Functions for Optimization based Community Detection Algorithms

<table><tr><td>Function</td><td>Formula</td><td>Algorithms</td></tr><tr><td>Modularity</td><td> $Q = \sum_{i=1}^{k}(e_{ii} - a_i^2)$ </td><td>Edge Betweenness, Louvain, Fast Modularity(FastQ)</td></tr><tr><td>Density function</td><td> $d(c) = \frac{w_{in}^{c}}{w_{in}^{c} + w_{out}^{c}}$ </td><td>Iterative Scan (IS)</td></tr><tr><td>Fitness function</td><td> $f(c) = \frac{deg(C_{i})}{(deg(C_{i}) + cut(C_{i}))^{r}}$ </td><td>Local Fitness Method (LFM), Greedy Clique Expansion (GCE)</td></tr></table>

## 2.2 Clique based Approaches for Community Detection

Another class of community detection methods is based on the strategy of clique identification. A clique is a subgraph that contains all the possible ties within its nodes [8]. One of the earliest attempts to uncover overlapping community structure was Clique Percolation Method (CPM) [20]. CPM first identifies all cliques of size . Then a new network is formed with each of its nodes representing a clique and an edge existing between two nodes (cliques) if they share clique members. The connected components of the network thus formed represent communities. Though CPM performs well for networks having densely connected modules, it fails for many large social networks [9]. An algorithm named EAGLE [21] performs agglomerative hierarchical clustering based on maximal cliques. First, all the maximal cliques are identified as seed communities and then these seed communities are expanded through similarity based pairwise merging. Another algorithm named Greedy Clique Expansion (GCE) also works on the principle of identifying maximal cliques [22]. GCE first identifies maximal cliques as seeds and then expands these seeds by optimizing an objective function in a greedy manner. However, both EAGLE and GCE are computationally expensive [9].

## 2.3 Similarity based Graph Clustering Approaches for Community Detection

Similarity based graph clustering algorithms have also been developed for community detection in complex networks. These algorithms first compute similarity, either between the nodes or edges of a network, and then utilize hierarchical agglomerative clustering for detecting communities. For instance, Walktrap algorithm [23] derives similarity based on random-walks between nodes and then performs hierarchical agglomeration to detect communities. However, Walktrap utilizes modularity as a stopping criteria for agglomerative hierarchical process and thus is suitable only for detecting disjoint communities [13]. Ahn et al. [24] posited that communities should be viewed as groups of links rather than nodes since this notion is

# ACCEPTED MANUSCRIPT

more suitable for identification of overlapping communities. Consequently, authors proposed a new algorithm (ABL) in which Jaccard similarity coefficient between pairs of links sharing a node is computed in the first step. Then link communities are detected through single-linkage hierarchical clustering and link communities are converted to node communities based on node-edge incidence. However, ABL tends to find small communities which may not represent meaningful community structure in a network [25].

## 2.4 Model based Approaches for Community Detection

In addition, several model-based techniques have been proposed for community detection in complex networks. For instance, an information theoretic method, InfoMap [26] encodes the information represented through full adjacency matrix and takes advantage of lesser information to detect communities. InfoMap uses Huffman coding [27] to distinguish nodes in a community from communities in a network. First, a greedy search algorithm is used to assign long code words to occasionally visited nodes and short code words to frequently visited nodes. Minimum Description Length (MDL) [28] is used as a quality function to evaluate random walk based two-level information in a network. In the second step, simulated annealing is used for fine-tuning the results of the first step [26]. Another method in this category is Label Propagation Algorithm information diffusion in a network. Initially each node is assigned a unique label and the neighborhood of each node is inspected. Then relabeling is performed iteratively until each node has the same label as the majority of its neighborhood nodes. However, InfoMap and LPA are not capable of detecting overlapping communities. Therefore, several model-based algorithms for overlapping community detection have been proposed. Community Overlap Propagation Algorithm (COPRA) [30] is an adaptation of LPA for overlapping community detection as it allows a node to have more than one label at a time. In COPRA, the membership coefficient of each node is updated iteratively by taking the mean of the coefficients of neighborhood nodes. Another algorithm called Speaker-listener Label Propagation Algorithm (SLPA) [31] starts with each node as a memory to store labels. For each node (listener), its neighborhood nodes (speakers) indicate a community membership (label) for the listener, based on their interactions. This process is repeated multiple times and finally the probability of observing a community membership in a node's memory is taken as its belongingness to that community. However, both COPRA and SLPA require a parameter to limit the number of communities to which a node can belong [9].

In some model-based methods, a network is considered to be generated from a statistical generative model [32]. One such method called OSBM [33] utilizes a stochastic block model (SBM) [34] for modelling a network and detecting overlapping communities. However, OSBM is not scalable to large networks [35]. Another algorithm, Model-based Overlapping Seed Expansion (MOSES) [35] integrates local optimization with OSBM to detect overlapping communities. Both OSBM and MOSES require several input parameters for modelling a network [9]. A machine learning technique called Non-Negative Matrix Factorization has also been adapted to complex networks to develop algorithms namely, Bayesian Non-Negative Matrix Factorization (BNMF) [36] and Symmetric Binary Matrix Factorization (SBMF) [37], for detecting overlapping communities. However, NMF based techniques are rendered inefficient due to memory and time constraints required for matrix multiplication.

## 2.5 Soft Computing Approaches for Community Detection

The use of soft computing techniques such as, fuzzy logic and genetic search, for community detection has gained popularity in recent years. Fuzzy community detection algorithms quantify the extent of membership of each node and the corresponding community(s). For example, an algorithm by Nepusz et al. [38] utilizes by Zhang et al. [39] uses a spectral clustering based framework to detect communities. In this algorithm, first a network is projected into Euclidean space with dimensions and then fuzzy c-means (FCM) clustering is used to detect overlapping commu ties. However, fuzzy community detection methods require the number of communities ( to be pre-specified [9]. Some community detection methods such as, GA-Net+ [40] and GaoCD [25], are based on genetic algorithm. GA-Net+ first converts a network to a line graph [41] and then utilizes the line graph as an input to genetic algorithm. In each iteration, the line graph is converted to node graph for evaluation of fitness. However, conversion from node graph to line graph is less effective and computationally expensive [42]. Genetic Algorithm for overlapping Community Detection (GaoCD) utilizes genetic representation for finding link communities, followed by conversion of link communities to node communities. A major drawback of genetic search based algorithms is that setting of multiple parameters is required to achieve meaningful results [25]. Rough set theory [43] is another soft computing approach that holds great potential for community detection in complex networks. In the past, fundamental concepts of rough set theory such as, approximations, equivalence relations and reducts, have been used to find obscure patterns in data [44]. Rough set theory has also been used for developing web recommendation systems [45]. Recently, rough set theory has been used in conjunction with other techniques for community detection. For instance, rough spectral clustering (RSC) algorithm is based on rough set theory and spectral theory [46]. Wang et al. proposed a density based rough set model (DBRSM) by fusing density based shrinkage with tolerance based rough set model [47]. Another study has integrated rough sets with fuzzy sets to detect communities [48]. However, the richness of the rough set theory has not been explored to its fullest potential and it is relatively under-researched for community detection.

The classical rough set theory is based on the premise that there is some additional information (data, knowledge) associated with the elements of the universe of discourse [43]. To model uncertainty and vagueness, this information can be expressed by an indiscernibility or equivalence relation, and used to form elementary granules of knowledge called equivalence classes. Ho equivalence relations restrict many applications of rough set theory. Apart from equivalence relations, rough sets have been generalized from different viewpoints like binary tolerance relations, coverings and neighborhood relations [44]. Lin was the first to apply the idea neighborhood rough set to formulate the notion of qualitative fuzzy sets [49].

The proposed algorithm, ROCONA, first models a network in the configuration of rough sets and generates classes of neighborhood granules (subsets of neighborhood nodes). Then, a topological operation named „connectedness upper approximation‟ and an altered equivalence relation named neighborhood relation are used to expand the granules. Further, the concept of constrained relative connectedness is used during each iteration for merging community components. This work proposes an algorithm that is, to the best of our knowledge, the first community detection algorithm based on the concept of constrained relative connectedness and connectedness upper approximation in complex networks.

## 3 ROCONA - Community Detection Algorithm for Complex Networks

From a network theoretic point of view, a complex network is a graph with topological properties such as, power-law distribution of degree centrality [8], high betweenness centrality scaling as the number of nodes [50], average clustering coefficient significantly higher than that of the corresponding random graph [51],

# ACCEPTED MANUSCRIPT

approximately the same average path length as its corresponding random graph [52]. Most real networks like, social, technological and biological, have these non-trivial structural properties because connection patterns between nodes are not purely random [8]. As can be seen in Table 10 (Appendix A), average clustering coefficients of complex networks used in this study are considerably higher than the expected value for corresponding random networks, thus indicating that there are significant number of triangles (loops of 3 nodes) in the network [51]. Betweenness centrality increases as the number of nodes increases, thus indicating that most of the nodes are just a few edges away and can be reached by others nodes through short paths [50]. Power law exponent for all the networks is greater than two, indicating that there are a few nodes with degree higher than average degree (hubs) and many nodes with degree lower than average degree [8]. Also, average path length for all the networks, excluding one network (power grid) is approximately the same as the corresponding value for random graph. The presence of community structure is another important property of complex networks. Communities are defined as cohesive or tightly knit subgroups of example, friendship in social networks, biological interactions in PPI networks, transmission and distribution in power grid networks [8].

The problem of community detection in a complex network consists of four phases: data transformation, data mining, evaluation and visualization [54]. In this work, our contribution pertains to the second phase i.e., data mining. We propose a new algorithm based on rough set theory for identifying community structure in complex networks and establish its effectiveness through comparison with state-of-the-art methods.

The community detection problem can be mathematically expressed in the following way: Let $G = ( V , E )$ be a network with set of vertices $V ( G ) = \{ v _ { 1 } , v _ { 2 } , v _ { 3 } , \ldots , v _ { n } \}$ and set of edges $E ( G ) \subseteq V \times V$ where the edge connecting a vertex pair $v _ { i } , v _ { j } \in V$ is denoted by $e _ { i , j }$ . The objective of the community detection problem is to find a set of communities such that vertices of each of these communities (subgroups) have more connections between them than the outside vertices and represent the real community structure existing in a

# ACCEPTED MANUSCRIPT

network. Hence, if k communities are identified in a network, $C _ { 1 } , C _ { 2 } , C _ { 3 } , \dots C _ { k } \in C ( G )$ represents the set of communities existing in the network<sup>†</sup>.

The proposed algorithm, ROCONA for solving the community detection problem is based on the concept of information granularity that exists in a variety of fields and provides the basis for different theories including rough set theory [55]. An information granule is regarded as a clump of objects in the domain of discourse , coming together due to some form of equivalence or indiscernibility [43]. This indiscernibility can be because of functionality, similarity or proximity [43]. An indiscernibility relation on the domain of discourse, $N \subseteq D \times D$ can generally be considered as an equivalence relation [43]. Thus, an equivalence class or a granule consists of indistinguishable elements. In a graph, an indiscernibility relation can be defined through an edge of a vertex $v _ { i }$ such that neighborhood connectedness around it is used to form a basic granule of knowledge. Definitions and equations used in the proposed algorithm are presented below.

Definition 1. Let define a neighborhood relation on a network $G ( V , E )$ . For any vertex $v _ { i }$ of $G ( V , E )$ , its $v _ { i }$ and all the adjacent vertices to vertex $v _ { i }$ [56]. Mathematically, it can be expressed as:

$$
S (v _ {i}) = \{v _ {i} \} \cup \{v _ {j} \in V (G): e _ {i, j} \in E (G) \}\tag{1}
$$

Thus constitutes a subset family of $G ( V , E )$ induced by such that $\cup _ { i = 1 } ^ { n } S ( v _ { i } ) \ : = \ : V ( G )$ for the vertices in a network. The number of links of $i ^ { t h }$ vertex in a network can be represented by $| S ( v _ { i } ) | = d e g ( v _ { i } ) + 1$ where $d e g ( v _ { i } )$ is the degree of vertex $v _ { i }$ [57]. To understand Definition 1, consider a toy network made of 20 vertices and 40 edges as shown in Fig.2. NCS corresponding to vertex $v _ { 6 }$ and $v _ { 7 }$ are $S ( v _ { 6 } ) =$ $\{ v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 4 } , v _ { 5 } , v _ { 6 } , v _ { 7 } \}$ and $S ( v _ { 7 } ) = \{ v _ { 1 } , v _ { 4 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 2 } , v _ { 1 7 } , v _ { 1 9 } \}$ respectively. Similarly, for a network with vertices there are such subsets, $S = \{ S ( v _ { 1 } ) , S ( v _ { 2 } ) , S ( v _ { 3 } ) , \ldots , S ( v _ { n } ) \}$ for all $v _ { i } \in { \mathsf { V } } ( G )$

![](/api/attachments/BPFUXKQT/fulltext/images/1783de3c8747c14c915f872bcbb61c8b6a931039b2303f54c67bd2ced2c015a1.jpg)  
Fig. 2. A Toy Network

Definition 2. For a network $G ( V , E )$ , the first-Connectedness Upper Approximation (f-CUA) of a subset corresponding to any node $v _ { i } \in V ( G )$ is the union of neighborhood connectedness subsets of all vertices in $S ( v _ { i } )$ . Mathematically it is defined as:

$$
\overline {{S}} (v _ {i}) = \bigcup \{S (v _ {j}): v _ {j} \in S (v _ {i}) \}\tag{2}
$$

Therefore, f-CUA of vertex $v _ { i }$ consists of all the vertices connected to it by a path whose length is at most two. For instance, in the toy network shown in Fig. 1, the f-CUA of vertex $v _ { 6 }$ and $v _ { 7 }$ are $\overline { { \cal S } } \left( v _ { 6 } \right) =$ $\{ v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 4 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 2 } , v _ { 1 7 } , v _ { 1 9 } \}$ and

$\bar { S } \left( v _ { 7 } \right) = \left. v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 4 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 3 } , v _ { 1 4 } , v _ { 1 5 } , v _ { 1 6 } , v _ { 1 8 } , v _ { 2 0 } \right.$ respectively. To compute the second connectedness upper approximation, the sets formed by f-CUA are used as NCS in Definition 2. The higher CUAs can be computed in the same way.

In this work, we have computed the first connectedness upper approximation and constrained it by utilizing the concept of relative connectedness as defined in Definition 3. The resultant subsets of f-CUA may have some vertices in common (termed as boundary elements in rough set terminology). The association strength of a vertex to f-CUA is calculated using relative connectedness measure.

Definition 3. For any two vertices $v _ { i } , v _ { j } \in G ( V , E )$ , the relative connectedness between $v _ { i }$ and $v _ { j }$ is defined as the ratio of number of their common connections to the number of different connections. Mathematically it is expressed as follows:

$$
R e l C o n \big (v _ {i}, v _ {j} \big) = \frac {\left| \Big (S (v _ {i}) \cap S (v _ {j}) \Big) \right|}{m a x \left(\left| \Big (S (v _ {i}) \cap S (v _ {j}) \Big) \right| , m i n \left(\left| \Big (S (v _ {i}) - S (v _ {j}) \Big) \right| , \left| \Big (S (v _ {j}) - S (v _ {i}) \Big) \right|\right)\right)}\tag{3}
$$

where $S ( v _ { i } ) - S \big ( v _ { j } \big )$ consists of nodes that are connected to $v _ { i }$ but not to i.e. $S ( v _ { i } ) - S \bigl ( v _ { j } \bigr ) = \{ x \ \in \qquad $ $S ( v _ { i } ) : x \notin S \big ( v _ { j } \big ) \}$ . The formulation for the expression of relative connectedness is based on the intuition that connectedness within a pair of objects in real-world is determined by the number of exclusive links between them, in addition to the number of their common links. Two objects are considered to be associated with each other if their exclusive links are less than their common links. From a set theoretic perspective, the expression of computes the ratio of area of intersection between two subsets and the minimum of the area of difference between them. Since, for a pair of objects, relative connectedness between them should get a symmetric treatment, the set difference with minimum cardinality is taken in the denominator of relative $0 \leq R e l C o n \big ( v _ { i } , v _ { j } \big ) \leq 1$ We use after each iteration of ROCONA to compute the magnitude of pair-wise node connectedness.

Definition 4. For a subset $S ( v _ { i } ) \in G ( V , E )$ , its Constrained Connectedness Upper Approximation (CCUA) is the union of all elements in its f-CUA with relative connectedness value equal to one [56] . Mathematically it is defined as:

$$
S _ {c} (v _ {i}) = \bigcup \{S (v _ {j}): v _ {j} \in S (v _ {i}) | R e l C o n (v _ {i}, v _ {j}) = 1 \}\tag{4}
$$

An f-CUA is constrained at a level where the number of common connections exceeds the number of exclusive connections. Thus, a CCUA can be viewed as a tightened version of the corresponding f-CUA. This is a repetitive process and CCUAs are successively computed for each f-CUA until CCUAs formed at iteration are found to be identical with CCUAs formed at iteration . When two consecutive CCUAs are found to be similar, they are taken as stable and no further computation is carried on these CCUAs. The algorithm converges once all the CCUAs become stable. The CCUAs thus rendered represent several clusters wherein a vertex may have more than one memberships. Moreover, some clusters may be exact copy of each other and some clusters may have superfluous overlaps referred as redundant and non-distinct clusters respectively [56]. Conductance based fine tuning is performed to filter out these ambiguous clusters and retain all the unique and meaningful clusters. The number of iterations required for convergence of ROCONA depends on the size of a network. It can also be observed from Table 10 that ROCONA converges faster on networks with higher average clustering coefficient as compared to the networks with smaller average clustering coefficient.

Since graphs are analogous to resistor networks, the concept of conductance in graphs has been derived from electrical conductivity [8]. Conductance of a subgraph can be formally defined as the proportion of outbound edges in the total edges of a community [6]. Since a community is considered as a densely connected subset of nodes with better interior linkage than exterior linkage, sets of nodes forming com unities have lower conductance. Mathematically, conductance of community $C _ { i }$ expressed by $\mathfrak { g } ( C _ { i } )$ , is defined as:

$$
\phi (C _ {i}) = \frac {c u t (C _ {i})}{m i n \{d e g (C _ {i}) , d e g (\overline {{C}} _ {i}) \}}.\tag{5}
$$

where $c u t ( C _ { i } )$ is the number of outward edges of $C _ { i }$ and $d e g ( C _ { i } )$ is the sum of degrees of vertices in $C _ { i }$ $\overline { { C } } _ { \imath }$ denotes the complement or remaining part of the network such that ${ \mathfrak { g } } ( C _ { i } ) = { \mathfrak { g } } ( { \overline { { C } } } _ { \imath } )$ [6].

Fine-tuning coalesces non-distinct or superfluous clusters into a meaningful cluster. From a particular group of non-distinct clusters, cluster with minimum conductance is selected and its conductance is tested after including each additional node in that group. The node which leads to a decrease in the conductance of cluster is retained in the cluster. The fine-tuning process is represented by the following expression:

$$
\min \left\{\sum_ {i = 1} ^ {k} \varnothing (C _ {i}) \colon C _ {i} \in C (G) \right\}\tag{6}
$$

The group of clusters thus originating after the fine-tuning operation gives the true community structure of the input network. The resultant communities might be concurrently disjoint, overlapping or nested as shown in Fig. 3 (one disjoint and two overlapping communities occurring concurrently). In Fig. 3 we present the process of community detection diagrammatically with our contribution in the second phase. We designed a rough set based node clustering technique to detect meaningful communities in complex networks and named it ROCONA (Rough Connectedness Algorithm). In essence, ROCONA works in a manner as if each node is selected to diffuse some information to the whole network. Since information can be directly diffused to only the neighborhood nodes, first the information is diffused to all the neighbors of a node and then they

# ACCEPTED MANUSCRIPT

diffuse this information to their neighbors not having the information yet. This process goes on iteratively to ensure that a node is the member of the subgroup with which it has most connections. The pseudo-code of ROCONA is presented in Algorithm 1.

## 3.1 Complexity Analysis of ROCONA

To calculate time complexity of ROCONA, each of its key components has been considered. These components include f-CUA computation, computation, iterative procedure and fine-tuning operation. Suppose ROCONA is applied to a network consisting of nodes and edges such that an average of CCUAs become stable after each iteration. Since $\vert G / N \vert$ complexity of f-CUA computation is in the order of [58]. The complexity of computation is $O ( n ^ { 2 } l o g _ { 2 } l )$ [56] where $l = 2 m / n$ is the average degree of nodes in network . Given that an average of $p$ CCUAs become stable after each iteration, the algorithm will converge in $n / p$ iterations. The complexity of iterative routine is , since the complexity of each iteration is [59]. The fine tuning operation has the complexity of $O ( n + d n )$ where is a small variable [25]. Finally, after removing and summing up, the total complexity of ROCONA is in the order of $O ( n ^ { 2 } l o g _ { 2 } l ) + O ( n l o g p ) + O ( n )$ Table 10 (Appendix A) shows the total number of iterations and execution time required for convergence of ROCONA on different networks used in this study. The execution times per iteration of ROCONA for each network are depicted in Fig. 10 (Appendix A) through a grouped bar plot.

![](/api/attachments/BPFUXKQT/fulltext/images/7ca58a99084b34bad7a24914dffb7e1aa32ed461d9e5751e6324180b699c9bcf.jpg)  
Fig. 3. Community Detection Process

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: ROCONA: Algorithm for Community Detection in Complex Networks

Input: A network G(V, E)

Output: Detected Communities C = {C₁, C₂, C₃, C₄, ..., Cₖ} //disjoint, nested and overlapping communities

Begin

Initialization:

1: for each vertex vᵢ in G do

2: NCS ← Neighborhood Connectedness Subset S(vᵢ) using Definition 1

3: end for

4: Iter ← 0

5: CCUAᵢₑᵣ ← NCS

Update:

6: do

7: Iter ← Iter + 1

8: TempC ← ∅

9: for each NCS do

10: Compute first Connectedness Upper Approximation  $\overline{S}(v_i)$  using Definition 2

11: Compute Relative Connectedness using Definition 3

12: CCUAᵢₑᵣ ← Constrained Connectedness Upper Approximation S_c(vᵢ) using Definition 4

13: if CCUAᵢₑᵣ == CCUAᵢₑᵣ₋₁ then

14: TempC ← TempC ∪ S_c(v_j)    // Freeze calculations for corresponding CCUAs

15: end if

16: end for

17: while Constrained Connectedness Upper Approximation S_c(vᵢ) is not stable

18: Fine Tuning using Equation (6)

19: return C

End
</div>

## 4 Illustration

To illustrate the working of ROCONA, we demonstrate it on a toy network consisting of 20 nodes and 40 edges as shown in Fig. 2. This toy network consists of four densely connected groups of nodes which are quite observable and form four communities. There is also a highly connected node, namely the node 7 which acts as a bridge between the four observable communities. As evident from the topology of this bridge node, it should be assigned to more than one community. Disjoint and hierarchical communities can also be observed in this toy network.

The Neighborhood Connectedness Subsets (NCS) of nodes are constructed as explained in Definition 1. Hence, NCS of each node is formed by grouping a node with all other nodes directly connected to it, as shown in Table 3. Now, Definition 2 is used to compute the first-Connectedness Upper Approximation (f-CUA) of each node and relative connectedness ( ) between a node and each element of its f-CUA is calculated using Definition 3. These f-CUAs are constrained at a value of one, such that nodes for which is less than one are dropped and remaining nodes constitute the CCUAs after first iteration.

The CCUAs computed after first iteration are shown in Table 3 (third column). Now, the same process is repeated and second iteration is performed on the CCUAs after first iteration. The f-CUAs in third iteration needs to be computed only for CCUAs which are not similar to respective CCUAs after first iteration. After third iteration, f-CUAs needs to be computed only for CCUAs which differ in their third and second CCUAs and so on. Thus some CCUAs will become stable with each iteration. In case of toy network, CCUAs of all nodes become stable after the third iteration, hence algorithm converges in three iterations. Now using Equation 6, we fine-tune the clusters and detect five communities in the toy network as shown in Fig. 4. Thus, the community structure of toy network consists of five communities including of one disjoint community {12,13,14,15}, three overlapping communities {(1,2,3,4,5,6,7),(7,8,9,10,11) & (7,16,17,18,19,20)}, and one nested community {17,19,20}.

Fig. 5. shows the relative connectedness matrices in each of the three iterations and graphical representation of the community component corresponding to Node 1. The CCUAs after the first, second and third iteration of the toy network are shown in Table 3. The CCUAs obtained after third iteration consist of distinct, redundant and non-distinct clusters. For better understanding, we explain this through an example in Table 4. As marked

Table 3. Computations on Toy Network

<table><tr><td> $v_i$ </td><td>NCS</td><td>CCUA after  $1^{st}$  iteration</td><td>CCUA after  $2^{nd}$  iteration</td><td>CCUA after  $3^{rd}$  iteration</td></tr><tr><td>1</td><td>1,2,5,6,7</td><td>1,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td></tr><tr><td>2</td><td>1,2,3,6</td><td>2,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td></tr><tr><td>3</td><td>2,3,4,6</td><td>1,3,5,6,7</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td></tr><tr><td>4</td><td>3,4,5,6,7</td><td>1,2,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td></tr><tr><td>5</td><td>1,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td rowspan="3">Converged in  $2^{nd}$  Iteration</td></tr><tr><td>6</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td></tr><tr><td>7</td><td>1,4,5,6,7,8,9,10,12,17,19</td><td>1,2,3,4,5,6,7,8,9,10,11,16,18,20</td><td>1,2,3,4,5,6,7,8,9,10,11,16,18,20</td></tr><tr><td>8</td><td>7,8,9,10,11</td><td>7,8,9,10,11</td><td rowspan="3" colspan="2">Converged in  $1^{st}$  Iteration</td></tr><tr><td>9</td><td>7,8,9,10,11</td><td>7,8,9,10,11</td></tr><tr><td>10</td><td>7,8,9,10,11</td><td>7,8,9,10,11</td></tr><tr><td>11</td><td>8,9,10,11</td><td>7,8,9,10,11</td><td>7,8,9,10,11</td><td rowspan="2">Converged in  $2^{nd}$  Iteration</td></tr><tr><td>12</td><td>7,12,13,14,15</td><td>12,13,14,15</td><td>12,13,14,15</td></tr><tr><td>13</td><td>12,13,14,15</td><td>12,13,14,15</td><td rowspan="3" colspan="2">Converged in  $1^{st}$  Iteration</td></tr><tr><td>14</td><td>12,13,14,15</td><td>12,13,14,15</td></tr><tr><td>15</td><td>12,13,14,15</td><td>12,13,14,15</td></tr><tr><td>16</td><td>16,17,19,20</td><td>7,16,18,20</td><td>7,16,18,20</td><td rowspan="5">Converged in  $2^{nd}$  Iteration</td></tr><tr><td>17</td><td>7,16,17,18,20</td><td>17,19,20</td><td>17,19,20</td></tr><tr><td>18</td><td>17,18,19,20</td><td>7,16,18,20</td><td>7,16,18,20</td></tr><tr><td>19</td><td>7,16,18,19,20</td><td>17,19,20</td><td>17,19,20</td></tr><tr><td>20</td><td>16,17,18,19,20</td><td>7,16,17,18,19,20</td><td>7,16,17,18,19,20</td></tr></table>

Table 4. Types of Clusters after third iteration on Toy Network

<table><tr><td>Distinct Clusters</td><td>Redundant clusters</td><td>Non-Distinct Clusters</td></tr><tr><td>1,2,3,4,5,6,7</td><td>1,2,3,4,5,6,7</td><td>7, 16, 18, 20</td></tr><tr><td>7,8,9,10,11</td><td>1,2,3,4,5,6,7</td><td>7, 16, 17, 18, 19, 20</td></tr></table>

![](/api/attachments/BPFUXKQT/fulltext/images/353fedaa459e2810584c8ed83b015c0b395d2047cc96373efbccac3c9e5d4413.jpg)

Fig. 4. Community Structure Identified in Toy Network  
![](/api/attachments/BPFUXKQT/fulltext/images/22c7105d95112b13d80e166b57145fd809ae8de0b90dc0f3e08654015108066d.jpg)

## Fig. 5. Community Component of Node 1 in Toy Network

in bold, distinct clusters have only one element in common, redundant clusters are exactly similar and nondistinct clusters have four common elements. Fine-Tuning operation is performed on CCUAs computed after last iteration to obtain the actual communities. The community structure detected by ROCONA in the toy network is consistent with our observations. Since real networks comprise basic structures similar to those in affirmed.

## 5 Experiments and Comparative Analysis

To gauge the performance of ROCONA, it was examined on complex networks emerging from various domains. We considered fourteen benchmark networks for our experiments having disjoint, overlapping or nested community structures. All these network datasets have most of the non-trivial structural properties of complex networks as shown in Table 10 (Appendix A) and they have been used extensively in the literature related to community detection in complex networks. The initial experiments were performed on High School Friendship network [60] and Les Miserables [61] network.

High School Friendship network consists of 69 nodes representing students of a high school and 220 selfreported friendships (links) within them. The ground-truth of this network is known and roughly consists of six different groups which represent grade seven to grade twelve. The community structure of the high school friendship network is quite interesting as it consists of two nested communities within grade nine corresponding to black and white ethnic groups. The challenge with the high school friendship network is to detect both the nested communities as well as other existing communities.

Les Miserables is a network formed by co-appearance of characters in Victor Hugo's famous novel with the same name. An edge exists between two characters if they appear together in a scene of the novel. This network consists of 77 nodes (characters) and 254 links. The number of communities is not predefined and it consists of overlapping community structure [60]. The main objective of community detection in this network is to identify the nodes which belong to overlapping communities.

# ACCEPTED MANUSCRIPT

Apart from High School Friendship and Les Miserables networks, we tested ROCONA on twelve other realworld benchmark network datasets. Out of these twelve datasets, ground-truth was available for seven datasets, whereas for the remaining five, ground-truth was not available. Networks such as, Karate club network [7], Risk network [13], Dolphin‟s association network [62], American political books network [63], American football team network [64], SFI collaboration network [64] and citation network of political blogs [65], have pre-defined ground truth. For networks such as, Jazz [66], Email [67], Roget‟s Thesaurus [61], Krogan‟s PPI network [68] and Power Grid<sup>†</sup> [69], ground-truth is unknown. Table 5 gives a detailed overview of the networks used in this study and the nature of communities existing within them. All the experiments described in this paper were carried out in R programming language. We used version 3.3.1 of R running on a system with 8.00 GB RAM and Intel Core i5 processor. For visualization of the networks, we used Gephi open source software.

Table 5. Overview of Experimental Datasets

<table><tr><td></td><td>Network Dataset</td><td># of Nodes</td><td># of Edges</td><td># of Groups</td><td>Nature</td><td>Description</td></tr><tr><td>1</td><td>Karate (N1)</td><td>34</td><td>78</td><td>2</td><td>Disjoint</td><td>A friendship network of club members</td></tr><tr><td>2</td><td>Risk (N2)</td><td>42</td><td>83</td><td>6</td><td>Disjoint</td><td>A network of countries on political map of earth</td></tr><tr><td>3</td><td>Dolphin (N3)</td><td>62</td><td>159</td><td>2</td><td>Nested</td><td>An association network of bottlenose dolphins</td></tr><tr><td>4</td><td>High School (N4)</td><td>69</td><td>220</td><td>6</td><td>Nested</td><td>A high school friendship network</td></tr><tr><td>5</td><td>Les Miserables (N5)</td><td>77</td><td>254</td><td>Unknown</td><td>Overlapping</td><td>A co-appearance network of characters in novel</td></tr><tr><td>6</td><td>Polbooks (N6)</td><td>105</td><td>441</td><td>3</td><td>Disjoint</td><td>A co-purchasing network of political books</td></tr><tr><td>7</td><td>Football (N7)</td><td>115</td><td>613</td><td>12</td><td>Disjoint</td><td>A game-scheduling network of teams</td></tr><tr><td>8</td><td>Jazz (N8)</td><td>198</td><td>2742</td><td>Unknown</td><td>Unknown</td><td>A collaboration network of Jazz musicians</td></tr><tr><td>9</td><td>SFI (N9)</td><td>271</td><td>676</td><td>6</td><td>Disjoint</td><td>A collaboration network of scientists</td></tr><tr><td>10</td><td>Roget&#x27;s Thesaurus (N10)</td><td>1022</td><td>5075</td><td>Unknown</td><td>Unknown</td><td>A lexical network of English words and phrases</td></tr><tr><td>11</td><td>Email (N11)</td><td>1133</td><td>5451</td><td>Unknown</td><td>Unknown</td><td>A communication network of emails</td></tr><tr><td>12</td><td>Polblog (N12)</td><td>1490</td><td>19025</td><td>2</td><td>Disjoint</td><td>A citation network of political blogs</td></tr><tr><td>13</td><td>Krogan&#x27;s PPI (N13)</td><td>2708</td><td>7123</td><td>Unknown</td><td>Unknown</td><td>A protein-protein interaction network of yeast</td></tr><tr><td>14</td><td>Power Grid (N14)</td><td>4941</td><td>6594</td><td>Unknown</td><td>Unknown</td><td>A topological network of an electrical grid</td></tr></table>

## 5.1 Pilot Experiments

On the High School Friendship network, ROCONA identifies two nested communities {13,14,17,18,19,20,60} & {15,16,44,45,46,47,54,55,56,57,60,62,63}, within grade-nine of this network. Node {43} is not assigned to any community since it acts as a bridge between three different groups and does not have allegiance to any particular group [9]. Two nodes {46 and 47} were detected as overlapping nodes

# ACCEPTED MANUSCRIPT

similar to other popular algorithms of overlapping community detection such as GCE, ABL and OSLOM [9]. All other nodes were detected according to the ground-truth, except four misclassified nodes {1, 32, 59 and 64} as shown in Fig. 6. The colored nodes represent the ground-truth and dashed lines represent the communities detected by ROCONA. The results substantiate that ROCONA can effectively uncover disjoint, nested and overlapping community structures within a network.

<sup>†</sup> Though average path length in case of Power Grid network is not equal to its corresponding random graph, it has high clustering coefficient and has been used widely in literature related to complex networks [75] and community detection methods [1][25].

![](/api/attachments/BPFUXKQT/fulltext/images/b8e696b6b496d910fd3765d611edf2e92d6c2bae1e05a0562eafc8c840143d22.jpg)  
Fig. 6. Two Nested Communities Detected in High School Friendship Network

We compare the performance of ROCONA on the High School Friendship network with other widely used state-of the-art methods of overlapping community detection: CPM [20], ABL [24], BNMF [36] and OSLOM [18]. For comparison we considered an information theoretic metric called Normalized Mutual Information (NMI) [70]. NMI measures the extent of concordance between the true partition (ground truth) and detected partition (detected communities). NMI was first introduced for partitions (disjoint communities) and later it was extended for covers (overlapping communities) [15]. Here we have used an advanced version of NMI proposed by Esquivel et al. [71], which is sensitive to nested and overlapping communities, and gives the same results as the standard measure when no overlapping or nested communities are present. From Table 6 it is clear that ROCONA outperforms other relevant methods of community detection.

Table 6. Comparative Analysis of ROCONA on High School Network

<table><tr><td>Algorithms</td><td>Normalized Mutual Information</td></tr><tr><td>CPM</td><td>.1679</td></tr><tr><td>ABL</td><td>.3155</td></tr><tr><td>BNMF</td><td>.6430</td></tr><tr><td>OSLOM</td><td>.4315</td></tr><tr><td>ROCONA</td><td>.8714</td></tr></table>

On Les Miserables network, ROCONA reveals the overlapping community structure quite effectively and identifies four overlapping communities represented by A, B, C and D in Fig. 7. The characters Enjolras, Marius, Gavroche and Jondrette are concurrently detected as members of two communities A and B. Perpetue, Fantine and Marguerite are detected as members of both communities B and C. The characters Valjean, MmeMagloire and MlleBaptistine are also detected as members of two social groupings B and D. To be part of multiple communities, a minimum threshold level of relationship should exist with the members of each community. The concept of connectedness upper approximation used in ROCONA takes care of this minimum required threshold. Since characters Thenardier and Bossuet are active with central characters like Valjean, Gavroche, Marius and Fantine, their detection becomes critical for any algorithm. ROCONA also identified the community memberships of both these nodes correctly.

![](/api/attachments/BPFUXKQT/fulltext/images/a95b5a4ed5e05ac42f251f725067992c569e6ef88da8c7057d3cc331375e820a.jpg)  
Fig. 7. Overlapping Community Structure Identified in Les Miserables

ROCONA detects similar community structure in Les Miserables as detected by a method proposed by He et al. [60]. However, three small communities detected by their method have become part of a single community B and other two small communities are detected as a single community C. These results are further supported by research published by Shi et al.[25], according to which small communities are usually meaningless and do not reflect the true community structure of a real-world network.

The algorithms CPM, ABL, BNMF and OSLOM were again used for comparison on Les Miserables network. Since the ground truth of Les Miserables is unknown, NMI cannot be used for comparative purpose. Therefore, we used another metric called partition density as an evaluation criteria [24]. Partition density, has become a widely accepted measure for overlapping community structure. It is mathematically defined as:

$$
D = \frac {2}{| E |} \sum_ {i} \frac {l _ {i} \{l _ {i} - (n _ {i} - 1) \}}{(n _ {i} - 2) (n _ {i} - 1)}\tag{7}
$$

where $l _ { i }$ is the number of links within $C _ { i }$ , $n _ { i }$ is the number of nodes within $C _ { i }$ and varies from 1 to (total N number of detected communities). denotes the total number of links within a network. From Table 7 it can be seen that partition density value of community structure detected by ROCONA is better than that of communities which may not represent the meaningful community structure of a network [25].

Table 7. Comparative Analysis of ROCONA on Les Miserables Network

<table><tr><td>Algorithms</td><td>Partition Density</td></tr><tr><td>CPM</td><td>.2426</td></tr><tr><td>ABL</td><td>.5821</td></tr><tr><td>BNMF</td><td>.0496</td></tr><tr><td>OSLOM</td><td>.3082</td></tr><tr><td>ROCONA</td><td>.2660</td></tr></table>

## 5.2 Experiments on networks with known ground-truth

Further, we evaluated the performance of ROCONA on well-known empirical networks for which groundtruth community structure is known a priori. On Karate club, a network of friendships among 34 members of a club at an American university, ROCONA correctly identifies the two groups with no misclassification. However, seven nodes were detected as members of both the communities, as shown in Fig. 8(a). These

# ACCEPTED MANUSCRIPT

seven nodes are connected to the most influential nodes of both the communities {1, 34}, either directly or within two-hops. The propinquity of these dichotomous nodes to the most influential nodes of the network indicates that they act as bridges between the two communities. In his study, Zachary himself observed that some of the individuals in the network have dual roles, thus enabling the flow of information between two groups [7].

Dolphin network consists of 62 dolphins (nodes) and 159 links representing frequent associations between them. The experiment on Dolphin network partitions it into four disjoint communities as shown in Fig. 8 (b). Out of these four communities, vertices in blue are detected as one community, while three detected subcommunities belong to another community. This result is similar to the „edge-betweenness‟ based algorithm of Girvan & Newman [72].

![](/api/attachments/BPFUXKQT/fulltext/images/4deee505744a095359d85cc8e4aeea90748f737df781d2f81619823edff3649e.jpg)  
Fig. 8. Detected Communities vs. Ground-Truth in Karate Club and Dolphin Network

Risk is a board game consisting of 42 countries roughly organized into six continents. On Risk network, seven communities. These communities consist of two overlapping, two nested and three disjoint communities. All the countries have been classified correctly except one country (Middle East). This misclassification is probably due to a dubious connection between East Africa and Middle East [13].

Polbooks represent a network of 105 American political books (nodes) where two books are connected if they were bought together from Amazon.com. The community structure detected by ROCONA in Polbooks consists of three communities. Though, books were mainly clustered into two groups (conservatives and liberals), some of the books (centrist) dispersed across three detected communities. Fewer nodes were misclassified nodes, as compared to eigenvector based and modularity maximization based methods [73]. PolBlog network is based on links among political blogs, around the time of the 2004 US presidential elections. The undirected version of PolBlog consists of 1490 nodes and 19025 links. On PolBlog network, ROCONA correctly identified two communities wherein 51 nodes were misclassified.

A collaboration network of 271 scientists (nodes) at an interdisciplinary research centre, Santa Fe Institute (SFI), was also used for the experiment. On the largest connected component of the SFI collaboration network consisting of 118 nodes, ROCONA produces four communities corresponding to four different disciplines: statistical physics, structure of RNA, mathematical ecology and agent based models [64]. However, one node has been detected as overlapping node of both mathematical ecology and statistical physics disciplines.

The test of ROCONA on football team network classifies 102 teams out of 115 into 10 conferences (communities) with only one misclassification. The team “Connecticut” actually belongs to IA Independents, but has been classified with Mid-American, because it has four out of seven connections with the teams in Mid-American conference and none with the teams in IA Independents. 7 out of 13 teams which were not classified into any conference belong to a single conference called Sunbelt as shown in Appendix B. It can be observed from the Football network that Sunbelt teams played lesser games against the teams in their own conference as compared to the teams in other conferences. In such situations, when the community structure is not in coherence with the network structure, ROCONA is unable to detect communities. However, this outcome is congruent with our observations and expectations.

Results on networks used in this section are visualized in Fig. 8 and Appendix B. To evaluate the performance of ROCONA on these networks, we compared it with four popular algorithms for disjoint community detection viz. FastQ [12], Walktrap [23], INFOMAP [26] and LPA [29]. Since ground-truth is known, we have used NMI for evaluation. As shown in Table 8, NMI of community structure identified by ROCONA is highest for all the networks excluding PolBlog network where it is the second highest. In case of PolBlog network NMI of LPA is higher than ROCONA however LPA is not a robust method, as it detects unstable communities [3].

Table 8. Comparison of NMI on Networks with Known Ground-Truth

<table><tr><td>Algorithms</td><td>Karate</td><td>Risk</td><td>Dolphin</td><td>Polbooks</td><td>PolBlog</td><td>SFI</td><td>Football</td></tr><tr><td>FastQ</td><td>.1102</td><td>.8878</td><td>.5571</td><td>.5308</td><td>.7632</td><td>.8453</td><td>.7099</td></tr><tr><td>Walktrap</td><td>.0907</td><td>.8015</td><td>.5816</td><td>.5427</td><td>.7356</td><td>.4845</td><td>.8986</td></tr><tr><td>INFOMAP</td><td>.1157</td><td>.8934</td><td>.5373</td><td>.4934</td><td>.7445</td><td>.5627</td><td>.9351</td></tr><tr><td>LPA</td><td>.2077</td><td>.8404</td><td>.5607</td><td>.5650</td><td>.8289</td><td>.5361</td><td>.8526</td></tr><tr><td>ROCONA</td><td>.5176</td><td>.9596</td><td>.6526</td><td>.5860</td><td>.7826</td><td>.9850</td><td>.9566</td></tr></table>

## 5.3 Experiments on networks with unknown ground-truth

Finally, ROCONA was tested on five networks for which ground-truth is not known. These networks include collaboration network of musicians (Jazz), communication network of emails (Email), protein-protein interaction network of the yeast Sacchromyces Cerevisiae (PPI), association network of English words and phrases (Roget‟s Thesaurus) and a network representing the topology of electrical grid in United States (Power Grid). On Roget‟s Thesaurus, the community structure detected by ROCONA was similar to that of a bibliometric method of community detection [74]. The complexes identified by ROCONA on PPI network, were consistent with that of Markov Clustering procedure [68].

![](/api/attachments/BPFUXKQT/fulltext/images/79c3c869a5005a471428303e8b7bb218adee5bb9dfe2a58a29cdb3efcdee3b37.jpg)  
Fig. 9. Detected Communities in Jazz Network

For Jazz, Email and Power Grid networks, we again compared the results of ROCONA with those of FastQ, Walktrap, INFOMAP and LPA. Here modularity measure has been used for evaluation, since it is considered a de facto metric for comparison and validation of community structures. It can be observed from Table 9 that modularity values are highest for Jazz and Email networks, but second highest for Power Grid network. Fig. 9 shows the detected community structure of Jazz network. For Email, Roget‟s Thesaurus, Krogan‟s PPI and Power Grid networks only a part of community structure has been visualized in Appendix C.

Table 9. Comparison on Networks with Unknown Ground-Truth

<table><tr><td rowspan="2">Algorithms</td><td colspan="2">Jazz</td><td colspan="2">Email</td><td colspan="2">Power Grid</td></tr><tr><td># of communities</td><td>Modularity</td><td># of communities</td><td>Modularity</td><td># of communities</td><td>Modularity</td></tr><tr><td>FastQ</td><td>4</td><td>.4389</td><td>12</td><td>.5070</td><td>41</td><td>.9335</td></tr><tr><td>Walktrap</td><td>11</td><td>.4384</td><td>49</td><td>.5265</td><td>364</td><td>.8310</td></tr><tr><td>INFOMAP</td><td>7</td><td>.2800</td><td>69</td><td>.5294</td><td>487</td><td>.8182</td></tr><tr><td>LPA</td><td>3</td><td>.4295</td><td>5</td><td>.2749</td><td>495</td><td>.8043</td></tr><tr><td>ROCONA</td><td>4</td><td>.4398</td><td>42</td><td>.5387</td><td>463</td><td>.8649</td></tr></table>

## 6 Implications for Practice

The nature and society consist of highly connected and complex systems where entities are organized into functional groups. Moreover, a variety of devices, social networks and software applications have emerged due to advancements in technology. As a result customers, products and services are getting increasingly connected at different levels in every walk of life. Therefore, businesses are looking to monetize plethora of interactions taking place in an interconnected world. In networks, these interactions are represented through connections. Networked community detection enables exploration of customers‟ subtle preferences so that products and services could be designed accordingly.

ROCONA not only can help to predict the speed and relevance of a particular piece of information on social media, it can also be used for improved customer valuation in various industries. For example, a wireless vendor may have a low value customer who has subscribed to a cheap calling plan. Despite being barely profitable to the company this customer may be highly connected within a community of heavy users. Allowing such a customer to leave, can lead to contagion effect and corresponding community members may also drop the vendor. Thus community detection enables the identification of influencers, and provides a new context where it is possible to determine and act based on the total revenue influenced by a customer, rather than individual revenue. Even outside the real life marketing challenges, ROCONA has the potential to throw up unforeseen and extremely interesting observations. A lot of phenomena earlier thought of as being unrelated might actually have a good amount of overlap with each other. Community based approach can also help in explaining a number of world events and predict the general direction of the mood within a city, nation or any other community.

## 7 Conclusion and Future Work

In this paper, we have proposed a previously unexplored rough set based community detection algorithm for complex networks. The proposed algorithm is conceptually simple, easy to implement and has broad applicability. At each stage, the algorithm allows a community component to grow uniformly and then constrains its growth such that loosely connected nodes are dropped from the component. Experiments on networks from diverse domains show that the proposed algorithm is an effective community detection algorithm. A systematic evaluation of our algorithm establishes its superiority over other currently used algorithms. The community structure identified through the proposed algorithm, ROCONA, can aid in decision making in various domains such as, social media marketing and telecommunications.

We believe that this work will guide future research and add rigor to the field of network analysis and community detection. Since we have only considered first upper approximation in this work, the use of higher upper approximations is an important future direction of this work. Another avenue of future research is to generalize the proposed algorithm to weighted networks, directed networks and heterogeneous networks, using the concept of vector based relative connectedness measure. The proposed algorithm can also be used in designing a recommender system to forecast the connections among products and customers. For this, semantic information such as product reviews and transaction details can be mined to derive the connectedness among products and customers.

## Appendix A

Table 10. Properties, No. of Iterations and Execution Time for Convergence of ROCONA on Experimental Networks

<table><tr><td>Network Dataset</td><td colspan="2">Average Centrality Scores</td><td colspan="2">Average Path Length</td><td colspan="2">Average Clustering Coefficient</td><td>Power law Exponent</td><td># of Iterations</td><td>Execution Times (secs)</td></tr><tr><td></td><td>Degree</td><td>Betweenness</td><td>Complex</td><td>Random</td><td>Complex</td><td>Random</td><td></td><td></td><td></td></tr><tr><td>Karate</td><td>4.588</td><td>23.235</td><td>2.408</td><td>2.314</td><td>.588</td><td>.135</td><td>2.125</td><td>5</td><td>.566</td></tr><tr><td>Risk</td><td>3.952</td><td>63.380</td><td>4.091</td><td>2.719</td><td>.516</td><td>.094</td><td>4.622</td><td>5</td><td>.413</td></tr><tr><td>Dolphin</td><td>5.120</td><td>71.887</td><td>3.356</td><td>2.527</td><td>.303</td><td>.082</td><td>7.708</td><td>7</td><td>.816</td></tr><tr><td>High School</td><td>6.377</td><td>66.811</td><td>2.965</td><td>2.285</td><td>.467</td><td>.092</td><td>7.430</td><td>7</td><td>.845</td></tr><tr><td>Les Miserables</td><td>6.597</td><td>82.722</td><td>2.641</td><td>2.302</td><td>.736</td><td>.085</td><td>4.124</td><td>5</td><td>1.440</td></tr><tr><td>Polbooks</td><td>8.400</td><td>108.095</td><td>3.078</td><td>2.186</td><td>.488</td><td>.080</td><td>2.621</td><td>6</td><td>1.735</td></tr><tr><td>Football</td><td>10.661</td><td>85.965</td><td>2.508</td><td>2.004</td><td>.403</td><td>.092</td><td>9.091</td><td>6</td><td>.969</td></tr><tr><td>Jazz</td><td>27.697</td><td>121.651</td><td>2.235</td><td>1.592</td><td>.633</td><td>.139</td><td>5.273</td><td>6</td><td>11.131</td></tr><tr><td>SFI</td><td>4.989</td><td>105.628</td><td>4.485</td><td>3.456</td><td>.863</td><td>.018</td><td>2.102</td><td>6</td><td>2.932</td></tr><tr><td>Roget&#x27;s Thesaurus</td><td>9.931</td><td>3426.649</td><td>4.075</td><td>3.525</td><td>.162</td><td>.007</td><td>3.877</td><td>10</td><td>6.518</td></tr><tr><td>Email</td><td>9.622</td><td>1475.014</td><td>3.606</td><td>3.106</td><td>.254</td><td>.008</td><td>6.775</td><td>11</td><td>40.912</td></tr><tr><td>Polblog</td><td>25.536</td><td>1574.389</td><td>2.737</td><td>2.348</td><td>.361</td><td>.015</td><td>3.912</td><td>7</td><td>236.160</td></tr></table>

![](/api/attachments/BPFUXKQT/fulltext/images/2e666a9b47768c9f6db853b9d916dc1382aece21ec4fd16644d9b4ad1d85f3b5.jpg)

## ACCEPTED MANUSCRIPT

<table><tr><td>Krogan’s PPI</td><td>5.261</td><td>4526.026</td><td>4.744</td><td>4.760</td><td>.277</td><td>.002</td><td>3.607</td><td>11</td><td>275.640</td></tr><tr><td>Power Grid</td><td>2.669</td><td>44433.290</td><td>18.989</td><td>8.663</td><td>.107</td><td>.0005</td><td>7.629</td><td>8</td><td>41.053</td></tr></table>

![](/api/attachments/BPFUXKQT/fulltext/images/457ba4f0b6b67853987bfd2d97db1dc4a6238f2d9d885b9e7d374a33800c59a8.jpg)

![](/api/attachments/BPFUXKQT/fulltext/images/3ec0bb35dc5b5ba631c2fcec010e7f36dbe27d6b14fb5fff74f767d2a3e489b2.jpg)

![](/api/attachments/BPFUXKQT/fulltext/images/0bf75200e2a3aa8e1a4418f68fa138dd1f0fb17ce34c58d8fc06eb2784f19794.jpg)

![](/api/attachments/BPFUXKQT/fulltext/images/47e2a03793c28f6b062302e6bd9c2cf499e5c6d87b48da542d645ef2c898f3f5.jpg)  
Fig. 10. Execution Time (secs) per Iteration on Different Networks

![](/api/attachments/BPFUXKQT/fulltext/images/fbcacce927f35719e92117cd29669f793826084a308a9b736bb4a1f37f7d507f.jpg)

![](/api/attachments/BPFUXKQT/fulltext/images/fee3cd601b7197e0226687389c146ba8a4b3b8ab5489edd75102b325611eb5fa.jpg)

![](/api/attachments/BPFUXKQT/fulltext/images/c2d44780767ac386499dfabe72ce201aa5ca1a33744f3c4ce25a297274107dbc.jpg)  
Experimental Results on SFI Collaboration Network

West Athletic SunBelt Independents Mid American Big10 Mountain West Big 12 Southeastern Conference USA Atlantic Coast Big East

![](/api/attachments/BPFUXKQT/fulltext/images/5dac9b6e02d29c5acafb08cb5fc9c51068e3598912a186eca57a6c960c4dd6a4.jpg)

## ACCEPTED MANUSCRIPT

## References

[1] W. Liu, M. Pellegrini, X. Wang, Detecting communities based on network topology, Scientific Reports 4 (2014).

[2] D. Ganley, C. Lampe, The ties that bind: Social network principles in online communities, Decision Support Systems 47 (2009) 266–274.

[3] S. Papadopoulos, Y. Kompatsiaris, A. Vakali, P. Spyridonos, Community detection in Social Media: Performance and application considerations, Data Mining and Knowledge Discovery 24 (2012) 515– 554.

[4] Z. Zhang, Q. Li, D. Zeng, H. Gao, User community discovery from multi-relational networks, Decision Support Systems 54 (2013) 870–879.

[5] U.K. Wiil, N. Memon, P. Karampelas, Detecting New Trends in Terrorist Networks, International Conference on Advances in Social Network Analysis and Mining, IEEE 2010, pp. 435–440.

[6] J. Leskovec, K.J. Lang, M. Mahoney, Empirical comparison of algorithms for network community detection, Proceedings of the $1 9 ^ { \mathrm { t h } }$ International Conference on World Wide Web, ACM, 2010, pp. 631– 640.

[7] W.W. Zachary, An information flow model for conflict and fission in small groups, Journal of Anthropological Research (1977) 452–473.

[8] S. Fortunato, Community detection in graphs, Physics Reports 486 (3) (2010) pp. 75–174.

[9] J. Xie, S. Kelley, B.K. Szymanski, Overlapping community detection in networks: The state-of-the-art and comparative study, ACM Computing Surveys 45 (2013) 1–35.

[10] M.E. Newman, M. Girvan, Finding and evaluating community structure in networks, Physical Review E. 69 (2004) 026113.

[11] V.D. Blondel, J.-L. Guillaume, R. Lambiotte, E. Lefebvre, Fast unfolding of communities in large networks, Journal of Statistical Mechanics: Theory and Experiment (2008) P10008.

Review E. 70 (2004) 66111.

[13] K. Steinhaeuser, N.V. Chawla, Identifying and evaluating community structure in complex networks, Pattern Recognition Letters 31 (2010) 413–421.

[14] J. Baumes, M.K. Goldberg, M.S. Krishnamoorthy, M. Magdon-Ismail, N. Preston, Finding communities by clustering a graph into overlapping subgraphs., IADIS AC. 5 (2005) 97–104.

[15] A. Lancichinetti, S. Fortunato, J. Kertész, Detecting the overlapping and hierarchical community structure in complex networks, New Journal of Physics 11(3) (2009) 33015.

[16] D. Jin, B. Yang, C. Baquero, D. Liu, D. He, J. Liu, A Markov random walk under constraint for discovering overlapping communities in complex networks, Journal of Statistical Mechanics: Theory and Experiment (2011) P05031.

[17] M.E. Newman, S.H. Strogatz, D.J. Watts, Random graphs with arbitrary degree distributions and their applications, Physical Review E. 64 (2001) 26118.

[18] A. Lancichinetti, F. Radicchi, J.J. Ramasco, S. Fortunato, Finding statistically significant communities in networks, PloS One. 6 (2011) e18961.

[19] M. Molloy, B. Reed, A critical point for random graphs with a given degree sequence, Random Structures and Algorithms 6 (1995) 161–180.

[20] G. Palla, I. Derényi, I. Farkas, T. Vicsek, Uncovering the overlapping community structure of complex networks in nature and society, Nature. 435 (2005) 814–818.

[21] H. Shen, X. Cheng, K. Cai, M.-B. Hu, Detect overlapping and hierarchical community structure in networks, Physica A: Statistical Mechanics and its Applications 388 (2009) 1706–1712.

[22] C. Lee, F. Reid, A. McDaid, N. Hurley, Detecting highly overlapping community structure by greedy clique expansion, Proceedings of the $4 ^ { \mathrm { t h } }$ Workshop on Social Network Mining and Analysis (SNA/KDD‟10) 2010, pp. 33-42

[23] P. Pons, M. Latapy, Computing communities in large networks using random walks, International Symposium on Computer and Information Sciences, Springer (2005), pp. 284–293.

[24] Y.-Y. Ahn, J.P. Bagrow, S. Lehmann, Link communities reveal multiscale complexity in networks, Nature. 466 (2010) 761–764.

## ACCEPTED MANUSCRIPT

[25] C. Shi, Y. Cai, D. Fu, Y. Dong, B. Wu, A link clustering based overlapping community detection algorithm, Data and Knowledge Engineering 87 (2013) 394–404.

[26] M. Rosvall, C.T. Bergstrom, Multilevel compression of random walks on networks reveals hierarchical organization in large integrated systems, PloS One. 6 (2011) e18209.

[27] D.A. Huffman, A method for the construction of minimum-redundancy codes, Proceedings of the IRE. 40(9) 1952, pp. 1098–1101.

[28] P.D. Grünwald, I.J. Myung, M.A. Pitt, Advances in minimum description length: Theory and applications, MIT press, (2005).

[29] U.N. Raghavan, R. Albert, S. Kumara, Near linear time algorithm to detect community structures in large-scale networks, Physical Review E. 76 (2007) 36106.

[30] S. Gregory, Finding overlapping communities in networks by label propagation, New Journal of Physics 12 (2010) 103018.

[31] J. Xie, B.K. Szymanski, X. Liu, SLPA: Uncovering overlapping communities in social networks via a speaker-listener interaction dynamic process, Proceedings of the $1 1 ^ { \mathrm { t h } }$ IEEE International Conference on Data Mining Workshops (ICDMW'11) 2011, pp. 344–349.

[32] A. Goldenberg, A. X. Zheng, S. E. Fienberg, & E. M. Airoldi, A Survey of Statistical Network Models, Foundations and Trends® in Machine Learning 2(2) (2009) 129–233.

[33] P. Latouche, E. Birmelé, C. Ambroise, Overlapping stochastic block models with application to the french political blogosphere, The Annals of Applied Statistics (2011) 309–336.

[34] K. Nowicki, T.A.B. Snijders, Estimation and prediction for stochastic blockstructures, Journal of the American Statistical Association 96 (2001) 1077–1087.

[35] A. McDaid, N. Hurley, Detecting highly overlapping communities with model-based overlapping seed expansion, International Conference on Advances in Social Networks Analysis and Mining (ASONAM) IEEE, 2010, pp. 112–119.

[36] I. Psorakis, S. Roberts, M. Ebden, B. Sheldon, Overlapping community detection using bayesian nonnegative matrix factorization, Physical Review E. 83 (2011) 66114.

[37] Z.-Y. Zhang, Y. Wang, Y.-Y. Ahn, Overlapping community detection in complex networks using symmetric binary matrix factorization, Physical Review E. 87 (2013) 62803.

[38] T. Nepusz, A. Petróczi, L. Négyessy, F. Bazsó, Fuzzy communities and the concept of bridgeness in complex networks, Physical Review E. 77 (2008) 16107.

[39] S. Zhang, R.-S. Wang, X.-S. Zhang, Identification of overlapping community structure in complex networks using fuzzy c-means clustering, Physica A: Statistical Mechanics and its Applications 374 (2007) 483–490.

[40] C. Pizzuti, Overlapped community detection in complex networks, Proceedings of the $1 1 ^ { \mathrm { t h } }$ Annual Conference on Genetic and Evolutionary Computation, ACM, 2009, pp. 859–866.

[41] T.S. Evans, R. Lambiotte, Line graphs, link partitions, and overlapping communities, Physical Review E. 80 (2009) 16105.

[42] U. Kang, S. Papadimitriou, J. Sun, H. Tong, Centralities in Large Networks: Algorithms and Observations, Proceedings of the SIAM International Conference on Data Mining, 2011, pp. 119–130.

[43] Z. Pawlak, Rough sets, International Journal of Computer and Information Sciences 11(5) (1982) 341– 356.

[44] P. Kumar, P.R. Krishna, R.S. Bapi, S.K. De, Rough clustering of sequential data, Data & Knowledge Engineering 63(2) (2007) 183–199.

[45] R. Mishra, P. Kumar, B. Bhasker, A web recommendation system considering sequential information, Decision Support Systems 75 (2015) 1–10.

[46] F.-L. Huang, N.-F. Xiao, Rough spectral clustering algorithm applied to overlapping network communities discovery, Journal of Chinese Computer Systems 33(2) (2012) 263–266.

[47] J. Wang, J. Peng, O. Liu, An Approach for hesitant Node Classification in Overlapping Community Detection., PACIS, 2014, p. 47.

[48] S. Kundu, S.K. Pal, Fuzzy-rough community in social networks, Pattern Recognition Letters 67 (2015) 145–152.

[49] T.Y.T. Lin, Neighborhood systems: mathematical models of information granulations, Proceedings of the IEEE International Conference on Systems, Man and Cybernetics, IEEE, 2003, pp. 3188–3193.

## ACCEPTED MANUSCRIPT

[50] M. Barthelemy, Betweenness centrality in large complex networks, European Physical Journal B-Condensed Matter and Complex Systems 38 (2004) 163–168.

[51] N. Przulj, Graph theory analysis of protein-protein interactions, Knowledge Discovery in Proteomics. 8 (2005) 73–128.

[52] R. Albert, A.-L. Barabási, Statistical mechanics of complex networks, Reviews of Modern Physics 74 (2002), p. 47.

[53] T. Chesney, Networked individuals predict a community wide outcome from their local information, Decision Support Systems 57 (2014) 11–21.

[54] M. Wang, C. Wang, J.X. Yu, J. Zhang, Community detection in social networks: an in-depth benchmarking study with a procedure-oriented framework, Proceedings of the VLDB Endowment 8 (10) (2015) 998–1009.

[55] L.A. Zadeh, Toward a theory of fuzzy information granulation and its centrality in human reasoning and fuzzy logic, Fuzzy Sets and Systems 90 (1997) 111–127.

[56] S. Gupta, P. Kumar, B. Bhasker, A Rough Connectedness Algorithm for Mining Communities in Complex Networks, Proceedings of International Conference on Big Data Analytics and Knowledge Discovery, Springer, 2016, pp. 34–48.

[57] T.H. Cormen, C.E. Leiserson, R.L. Rivest, C. Stein, Introduction to algorithms, Volume 6, MIT press, Cambridge, 2001.

[58] J.W. Grzymala-Busse, LERS-a system for learning from examples based on rough sets, Intelligent Decision Support, Springer, 1992, pp. 3–18.

[59] M. Dash, H. Liu, P. Scheuermann, K.L. Tan, Fast hierarchical clustering and its validation, Data and Knowledge Engineering 44(1) (2003) 109–138.

[60] D. He, D. Jin, Z. Chen, W. Zhang, Identification of hybrid node and link communities in complex networks, Scientific Reports 5 (2015) 8638.

[61] D.E. Knuth, The Stanford GraphBase: a platform for combinatorial computing, Addison-Wesley Reading, 1993.

[62] D. Lusseau, K. Schneider, O.J. Boisseau, P. Haase, E. Slooten, S.M. Dawson, The bottlenose dolphin community of Doubtful Sound features a large proportion of long-lasting associations, Behavioral Ecology Sociobiology 54 (2003) 396–405.

[63] V. Krebs, Books about us politics, Unpublished http://www.orgnet.com. (2004).

[64] M. Girvan, M.E. Newman, Community structure in social and biological networks, Proceedings of the National Academy of Sciences 99(12) (2002) 7821–7826.

[65] L.A. Adamic, N. Glance, The political blogosphere and the 2004 US election: divided they blog, Proceedings of the $3 ^ { \mathrm { r d } }$ International Workshop on Link Discovery, ACM, 2005, pp. 36–43.

[66] P.M. Gleiser, L. Danon, Community structure in jazz, Advances in Complex Systems 6 (2003) 565– 573.

[67] R. Guimera, L. Danon, A. Diaz-Guilera, F. Giralt, A. Arenas, Self-similar community structure in a network of human interactions, Physical Review E. 68 (2003) 65103.

[68] N.J. Krogan, G. Cagney, H. Yu, G. Zhong, X. Guo, A. Ignatchenko, J. Li, S. Pu, N. Datta, others, Global landscape of protein complexes in the yeast Saccharomyces cerevisiae, Nature. 440 (2006) 637– 643.

[69] D.J. Watts, S.H. Strogatz, Collective dynamics of “small-world” networks, Nature. 393 (1998) 440– 442.

[70] A. Arenas, Leon Danon, Albert Dıaz-Guilera, Jordi Duch, Comparing community structure identification, Journal of Statistical Mechanics: Theory and Experiment (2005) P09008.

[71] A.V. Esquivel, M. Rosvall, Comparing network covers using mutual information, ArXiv Prepr. ArXiv12020425. (2012).

[72] D. Lusseau, M.E. Newman, Identifying the role that animals play in their social networks, Proceedings of the Royal Society of London B: Biological Sciences 271 (2004) S477–S481.

[73] G. Agarwal, D. Kempe, Modularity-maximizing graph communities via mathematical programming, The European Physical Journal B 66 (2008) 409–418.

[74] H. Balakrishnan, N. Deo, Discovering communities in complex networks, Proceedings of the $4 4 ^ { \mathrm { t h } }$ Annual Southeast Regional Conference, ACM, 2006, pp. 280–285.

[75] G.A. Pagani, M. Aiello, The power grid as a complex network: a survey, Physica A: Statistical Mechanics and its Applications 392(11) (2013) 2688–2700.

Dr. Pradeep Kumar is currently an Associate Professor in IT and Systems area at Indian Institute of Management Lucknow, India. Prior to joining IIM, he was associated with SET Labs, Infosys Technologies Ltd. as a researcher. He served Institute for development and research in Banking Technology (IDRBT), established by Reserve Bank of India (RBI), as a Research Fellow. He received his Ph.D. from Department of Computer and Information Sciences, Hyderabad University, India. He holds M.Tech. and B.Sc.(Engg.) in Computer Science. His area of interest includes Data Warehousing, Data Mining, Web Mining, Text Mining and Big Data analytics. In his credit he has more than 30 authored research papers in international journals and conferences of repute.

Samrat Gupta did his B.E. from PEC University of Technology, Chandigarh in Information Technology. He is currently a Doctoral Student in IT and Systems Department at Indian Institute of Management Lucknow, India. Prior to joining IIM Lucknow, he was working as Software Engineer with Computer Sciences Corporation (CSC), India. His current research interests include Data Mining, Analysis of Complex Networks and Predictive Analytics.

Dr. Bharat Bhasker is a Professor in the area of IT and Systems, at Indian Institute of Management Lucknow, India. He holds a Bachelor's degree in Electronics and Communications Engineering from University of Roorkee, India; Master's degree and Doctorate in Computer Science from Virginia Polytechnic Institute and State University, USA. Prior to joining IIM Lucknow, he was with MDL Information Systems and Sybase Inc., California, USA and was the architect of the massively parallel DBMS, Sybase MPP. He also served as a Visiting Professor of Information Systems, Business Management School, University of Maryland, University of California, and University of Texas, USA. His research interests include Distributed Database Management, Data Mining, Personal Recommendation Systems, and Agent based Electronic Shopping. He has also authored two books on Electronic Commerce.

# ACCEPTED MANUSCRIPT

## Highlights

 A Rough Set Based Community Detection Algorithm for Complex Networks has been proposed

 Experiments have been performed on fourteen benchmark networks from diverse domains

 Comparative analysis of the proposed algorithm has been performed with the relevant stateof-the-art methods

 The performance of proposed algorithm is superior to state-of-the-art methods
