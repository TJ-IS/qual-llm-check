---
otero_id: 2818
otero_key: "Q3TM2KBS"
title: "Detect potential relations by link prediction in multi-relational social networks"
authors: "Ling Chen; Man Gao; Bin Li; Wei Liu; Bolun Chen"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.09.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Detect potential relations by link prediction in multi-relational social networks

![](/api/attachments/Q3TM2KBS/fulltext/images/86b1673667b76bdcdd8f732a9ef96ee47e3c64127ba034534e68d25d7b08cca6.jpg)

Ling Chen, Man Gao, Bin Li, Wei Liu, Bolun Chen

<table><tr><td>PII:</td><td>S0167-9236(18)30157-X</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.09.006</td></tr><tr><td>Reference:</td><td>DECSUP 12992</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>9 February 2018</td></tr><tr><td>Revised date:</td><td>17 September 2018</td></tr><tr><td>Accepted date:</td><td>24 September 2018</td></tr></table>

Please cite this article as: Ling Chen, Man Gao, Bin Li, Wei Liu, Bolun Chen , Detect potential relations by link prediction in multi-relational social networks. Decsup (2018), doi:10.1016/j.dss.2018.09.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Detect Potential Relations by Link Prediction in Multi-Relational Social Networks

Ling Chen<sup>1,2,a</sup> Man Gao<sup>1,b</sup> Bin Li<sup>1</sup>, Wei Liu<sup>1</sup>, Bolun Chen<sup>3</sup>

<sup>1</sup>Department of Computer Science, Yangzhou University, Yangzhou, 225127, China

<sup>2</sup>State Key Lab of Novel Software Tech, Nanjing University, Nanjing, 210093, China Department of Computer Science, Huaiyin Institute of Technology, Huaiyin,223001, China

<sup>a</sup> lchen@yzu.edu.cn <sup>b</sup>15396768192@163.com

Abstract Potential relation detecting on social network has become more important for decision making in many business disciplines, such as marketing, business strategy, human resources development, finance planning, business transformation, insurance policy design, and tourism management. People are used to seeking useful information from the relationships among social members to support their decisions on investment, partner seeking and marketing. Corporations are seeking opportunities to leverage them for “word of mouth” advertising based on the relations between the customers. When we collect and observe relationships between people, missing or redundant relations unavoidably occur since the time and cost restrictions in market or social investigation prevent us to discover all the relations. Moreover, since the social relations are changing constantly, current social relations may disappear, and new relations will be established. Many trade and social networks consist of multiple types of relations between the individuals. This paper presents an efficient method to detect the potential and future social relations between individuals in multi-relational social networks using link prediction. First, we calculate the belief of each individual by belief propagation on each type of relations. Based on the belief vectors, the similarities between various types of relations are computed to measure their mutual influence. Based on the similarities between various types of relations, we model link prediction as the problem of matrix completion by optimizing its max-norm constrained formulation. We propose a projected gradient descent optimization algorithm which is scalable to large size networks. Empirical results on real multi-relational social networks demonstrate that the predicting results of our algorithm have higher quality compared with other similar algorithms.

Keywords multi-relational social networks, potential relations, link prediction, similarity, matrix completion

## 1. Introduction

Detecting potential social relations between individuals is important for decision making in virus marketing [1], merchandise recommendation [2,3], social trust prediction [4, 5], social influence maximization [6], retail transaction prediction [7], and community detecting. Detecting potential relation on social network has attracted more attention of the decision makers from many business disciplines, such as marketing [8, 9], business strategy [10], human resources development [11], finance plaining [12], business transformation [13], insurance policy design [14], and the tourism management [15]. Identification or recognition of potential relations between members in a trade and social network has become a crucial issue in various areas or platforms. With the emergence and growing popularity of online social networks, people are becoming used to seeking friends and partners from the websites. Meanwhile, corporations are also seeking opportunities to leverage potential customers for “word of mouth” advertising and marketing strategy design. Predicting potential social relations between individuals is helpful for discovering potential customers or members of organizations, which will then help both people and corporations to secure their long-term interests.

On websites in social networks, members perform various social interactions with each other, such as contacting, commenting and marking favorites. Based on social network theory, these interactions performed can build social relations among members and can be recorded in social networks [16], such as trade networks [1], collaboration networks [17], customer-commodity networks and service-user networks. In such networks, nodes represent the entities such as customers or goods, and the links represent the relations between the entities. Those relations may be explicit or implicit. The explicit relations straightly demonstrate the different interactions, and the implicit relations indicate the closeness of the relationship which can be deduced from a given dataset. For instance, relations in social networks are usually explicit, where relations are directly reflected by information expansion such as emails and telecommunications. Examples of implicit relations include on-line social networks like Twitter or Facebook [18], where two users can be indirectly linked by their common topics or favorite photos. In the trade network, implicit relations between the customers can be found if they frequently buy the same merchandise.

When we collect and observe relationships between people, missing or redundant relations may unavoidably occur since the time and cost restrictions in market investigation prevent us to discover all the relations. Moreover, since the relations in the market are changing constantly [19], some potential relations may appear in the future. Thus，it is necessary to discover such hidden relations or the future connections from the current topological structure of the trade or social networks.

Link prediction is an effective approach to detect such potential relations between the individuals in trade and social networks. Using link prediction, we can discover potential interpersonal contacts [19, 20] by analyzing the customers’ shopping behavior and social relationships. Link prediction can reveal the potential friendship of users in social networks [21 22] and can recommend the possible merchandise or services to the users [2, 23]. In e-commerce, merchants usually use link-prediction to recommend a commodity to the customers [1, 7]. Link prediction is often employed in analyzing the author networks of scientific publication and predict the potential co-authors [24]. Link prediction also can be used to analyze the e-mail communication and detect anomalous e-mails [25]. In the fight against terrorism, link prediction has been exploited in monitoring terrorist networks to detect disguised connections and relations between the members of the terrorism organizations and to stop their malefaction.

Many trade and social networks consist of multiple types of relations between the individuals. We call them multi-relational network or heterogeneous networks. In such networks, there may exist multiple types of relations between the users or customers, such as partners, friends, relatives, and colleagues [26]. Between each pair of different types of relations, there exist mutual influences. This influence may deviate for different pairs of relations. For example, it is more probable that a student will build a friendship with a friend of his classmate than with a friend of his relative. The relation “classmate” has a higher influence on the relation “friend” than “relative” does. For predicting the potential links in such multi-relational social network, the relevancy and impact between different relations should be considered synthetically. Most existing relation prediction algorithms are not suitable to multi-relational networks since they just observe one relation and disregard the entire structure along with the influence between various relations. An intuitive way for predicting the hidden or future relations in multi-relational networks is to merge the multiple relations in the network into a single one and conduct potential relation prediction based on this merged one. But we may miss too much topological information in such simple and easy approach and cannot achieve accurate prediction results. Therefore, we should design an effective method that exploits multi-relational information in the social network to increase the precision of the prediction results.

In this paper, we present a link prediction-based algorithm for detecting the relations in multi-relational network. We treat the adjacent matrix of the network as a sparse matrix destroyed by noise or interference and use matrix completion to recover the original “true” adjacent matrix which reveal the potential relations in the network. Since there exist various types of relations in the multi-relational networks and each type of relation has its own adjacent matrix, we must tackle the problem of recovering multiple adjacent matrixes for predicting the target relation. However, it is challenging to find an optimal recovered matrix from the multiple adjacent matrixes of the various types of links. In this work, we first model the link prediction for multi-relational networks as multiple matrixes completion, and then solve the matrix completion problem with a max-norm constrained formulation. Since max-norm is not easy to optimize, we utilize a reformulation of max-norm, and present a projected gradient descent optimization approach to obtain the recovered low-rank matrix.

The rest of this paper is organized as follows. In Section 2, we review the related works on relation and link prediction in social networks. Section 3 defines some fundamental concepts about multi-relational social network link prediction and matrix completion. Section 4 presents a matrix completion method called MCLP for link prediction in multi-relational networks. Section 5 shows and analyzes the empirical results. Section 6 concludes our paper and gives our future work.

## 2. Related Works

## 2.1 Works on Relation Prediction

With the development of social network analysis, there have been many relation prediction methods reported recently. The interaction-based method [27] is an efficient and widely used relation detection approach due to its low time complexity. The method identifies potential but unlinked relations between users by their interactions with other users. Another widely used relation prediction approach is the path-based method [28]. This method uses contact information by implementing the concept of the well-known PageRank algorithm from Google. Jeh and Widom [29] propose SimRank to measure the similarity of elements using the information of their relations. SimRank combines the features of interaction-based method and the PageRank algorithm. Due to its high computational cost, this type of algorithm is seldom used in large scale trade and social networks.

Some relation detection methods predict the relations using users' attributes such as race, gender, age, location, and education [30]. Yin [31] proposes a relation detection method named LINKREC. Based on the random walk with the restart algorithm, the method uses the information of network structure and users' attributes. Many research works have been made to estimate the influence of the users’ attributes on their relations. For instance, Eder and Hallinan [32] find that the youths prefer to delete a cross-sex friend than to add a cross-sex friend, which leads to gender segregation in social media. On the other hand, the networks of adults are more sex-integrated. Marsden [33] explains that when people “discuss important matters with” the confidants, 70% of them are sex heterogeneous. However, Huckfeldt and Sprague [34] showed that when the topic is limited to politics, 84% of men choose other men to discuss it.

Some methods for detecting potential relations use the machine learning technique. Vedula et al. [35] proposed an unsupervised learning method for relation detecting. The method integrates the implicit factors of social influence exerted by each user in the network, the underlying network structural topology and the opinions expressed by the users in the textual content they communicate. Shi et al. [36] presented a method to predict the potential positive and negative relations between the users in social media networks. Their method employs matrix factorization and hybrid particle swarm optimization to estimate the similarity between the users and gets high quality results.

Recommendation techniques such as collaborative filtering is an important approach in social relation prediction. Research has shown that a quality friend recommendation can detect the potential connections between users, as well as the user loyalty to a social media [37]. Zhang et al. [38] presented a friend recommendation system using a user's attributes information. Based on the law of total probability, their method can be easily extended for friend recommendation in networks with large number of user's attributes at low computation cost. Fang et al. [39] proposed a recommendation-based method for trust and distrust prediction in multi-faceted social networks. The method considers both interpersonal and impersonal factors of trust and distrust. Two logistic regression models are developed and trained by accommodating these factors and applied to predict continuous values of users' trust and distrust.

## 2.2 Works on Link Prediction

Link prediction is an important approach for relation detection in social networks. The methods for link prediction in social networks fall into three main classes: similarity based, probabilistic model based, and machine learning based methods.

The similarity-based method [40] is the easiest and most widely used link prediction method. It assumes that nodes with similar topological structures are probably connected with each other. In this method, a similarity index is computed for each node pair according to the main topological features of the network. If a pair of nodes have correlated topological structures or more common features, they should be assigned a higher similarity score, which means they are more likely to be connected by a potential link. Probabilistic model-based method [41] first constructs a probabilistic model, and then the model is optimized to predict the hidden links. In machine learning based methods, supervised learning techniques, such as supervised rank aggregation [42], principal component analysis [43] and ensemble [44] are employed for network link prediction. To reduce the time cost for optimization, heuristic optimization approaches, such as evolutionary algorithm [45] and ant colony optimization [46] are also employed for network link prediction. B. Chen et al. [47] presented a sampling-based algorithm to predict the links involving a given node. The method constructs a sub-graph centered at the given node. By choosing a proper size of such sub-graph, the method can make the error of the estimated similarities be less than a given threshold. In [48], a matrix factorization-based method is proposed for link prediction in dynamic networks. The method first gets a lower rank matrix by nonnegative matrix factorization on the similarity matrix, and then get the predicting results from the latent space represented by the lower rank matrix. Since the lower rank matrix carries important features of the network, the method can get high quality predicting results.

# ACCEPTED MANUSCRIPT

## 2.3 Works on Relation and Link Prediction in Multi-relational Social Networks

In recent years, some relation and link prediction methods in multi-relational networks were proposed. Some approaches for multi-relational network link prediction are based on matrix or tensor operations. C.Y. Dai et al. [49] present a matrix factorization-based method to detect the possible links of a given type in a multi-relational network. The method considers the similarity and influence between different types of relations. Using the similarity and influence between different types of relations, the method can predict links of the target type by nonnegative matrix factorization. V. Stroele et al. [50] proposed a clustering-based link prediction method for multi-relational social networks. The approach uses topological features of network structures by employing tensor decomposition. On the other hand, some link prediction methods are based on feature selection and machine learning. Wang et al. [17] presented a social feature-based method for predicting the potential links in multi-relational networks. The algorithm weights the sub-network consisting of different types of links using a similarity function based on their topological features. M. Berlingerio et al. [51] presented a multi-graph model for predicting multiple relations. The method treats the multi-relational network as a multi-graph which consists of many subgraphs corresponding to the different types of links. It defines topological measurements for the graph to characterize the global and local properties of the networks and exploits machine learning technique to obtain the predicting results.

To predict the potential link of a given type in the multi-relational network, it is important to consider the impacts between different types of links. Cao et al. [52] introduce the linkage homophily principle for collective prediction of multiple types of links in heterogeneous information networks. Based on such principle, they defined an index named RM to estimate the relatedness between various types of links in the networks. Based on RM index, they presented an iterative algorithm to collectively detect different types of links. Jeong et al. [53] introduce the Local Relatedness Measure (LRM) that indicates occurrence possibility of a link between different types of nodes. Also, they proposed a measurement called TypeCorr to quantitatively capture the correlation between a link type and path type. The method performs the link prediction based on a supervised learning method, by using features obtained by combining TypeCorr with other relevant properties. Some methods use the concept of meta-path to estimate the similarity between nodes and predict potential links. Zhang et al. [54] define seven "intra-network social meta paths"

and four categories of "inter-network social meta paths" to categorize these diverse connections among users. These "social meta paths" can cover a wide variety of connection information in the network, which can be helpful for solving the multi-relational network link prediction problem. They advanced an approach to choose a subset of the most descriptive social meta paths for predicting links in the multi-relational social network.

Although many methods for relation and link prediction in multi-relational network have been proposed, their high time complexity prevents their application on large scale matrixes. In addition, most of those multi-relational network link prediction methods are based on the methods for the uni-relational networks and cannot achieve high quality link prediction results for the multi-relational ones. Moreover, these methods only consider the relationship between each pair of different types of relations, and there is no overall consideration of the interaction and collective impact of all the types of links. Since there exist multiple types of links in the multi-relational networks and every type of link has its own adjacent matrix, an efficient algorithm is needed to integrate the multiple adjacent matrixes for link prediction on the target relation.

In this work, we formulate the problem of link prediction for multi-relational social networks as the multiple matrixes completion. Because the data in multi-relational social network is usually sampled non-uniformly, a max-norm based model is more suitable for predicting the potential links. We present an efficient projected gradient decent algorithm to optimize the max-norm. This algorithm can considerably decrease the computational time and can be used for large scale social networks. Computation time of the algorithm reaches the lower bound of the time complexity for a similarity-based link prediction method.

## 3. Link Prediction in Multi-Relational Networks and Matrix Completion

In this section, we first define the problem of link prediction in multi-relational networks, and then model the problem based on matrix completion. Main notations used in this paper are listed in Table 1.

Table 1 Main notations used in the paper.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>G=(V,E)</td><td>A network with node set V and edge set E</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>n</td><td>Number of nodes in G</td></tr><tr><td>d</td><td>Number of different edge types in G</td></tr><tr><td>Er</td><td>Set of the r-th type edges</td></tr><tr><td>Gr</td><td>Sub-graph consists of the r-th type of edges</td></tr><tr><td>A(r)</td><td>The adjacent matrix of Gr</td></tr><tr><td>Ωr</td><td>Set of indexes of the non-zero elements in A(r)</td></tr><tr><td>PΩr(X)</td><td>A projection operator on matrix X</td></tr><tr><td>ψr(vi,vj)</td><td>Transformation function for edge (vi,vj) in Gr</td></tr><tr><td>Nr(i)</td><td>The set of nodes linked with vi in Gr</td></tr><tr><td>dr(vi)</td><td>Degree of vi in Gr</td></tr><tr><td>mr(j,i)</td><td>The message node vjsends to vi in Gr</td></tr><tr><td>bri</td><td>The belief of node vi in Gr</td></tr><tr><td>βr</td><td>Similarity between the r-th and the target relation</td></tr><tr><td>X(i)</td><td>The similarity score matrix of Gi</td></tr><tr><td>U, V</td><td>n*m matrixes, factorization of X</td></tr><tr><td>Γ(A)</td><td>Shrinkage operator for scaling the rows matrix A</td></tr></table>

## 3.1 Link Prediction in Multi-Relational Social Networks

A multi-relational social network can be formulated as a graph $G = ( V , E )$ , where $E { = } E _ { 1 }$ ∪ $E _ { 2 } \cup \ldots \cup E _ { d }$ denotes the set of different types of edges, and $E _ { i } \left( i { = } 1 , 2 , . . . , d \right)$ denotes the set of the i-th type edges. Different types of edges represent different relations between individuals. The sub-graph of G consisting of the r-th type of edges is denoted as $G _ { r } { = } ( V , E _ { r } )$ , and the adjacency matrix of sub-graph $G _ { r }$ is denoted as $A ^ { ( r ) } = \left[ a _ { i j } ^ { ( r ) } \right] _ { n \times n }$ , where $a _ { i j } ^ { ( r ) } = 1$ if an edge of the r-th type exists between nodes $\nu _ { i }$ and $\nu _ { j } ,$ and $a _ { i j } ^ { ( r ) } = 0$ otherwise. It is worth mentioning that a sub-graph $G _ { r }$ is not necessarily connected, even though the whole network $G$ is connected. This is because the nodes in $G$ are connected by all types of edges, while the nodes in $G _ { r }$ are connected only by the r-th type of edges. But different subgraphs may connect with each other since they have identical node set.

Given an integer $t ( 1 \leq t \leq d )$ , the purpose of link prediction is to detect the t-th type of links based on the topological structures of all types of links in the network, which are represented by adjacent matrixes $\boldsymbol { A } ^ { ( i ) } \ ( i { = } 1 , 2 , . . . , d )$ . We call the t-th type link the target relation or target dimension. The final result of link prediction is to output a similarity matrix $X ^ { ( t ) } = \left[ x _ { i j } ^ { ( t ) } \right] _ { n \times n }$ for the target relation, where $\chi _ { i j } ^ { ( t ) }$ is the occurrence probability of the t-th type link connecting nodes $\nu _ { i }$ and $\nu _ { j } .$ Therefore, probability matrix $X ^ { ( t ) }$ can intuitively reflect the presence of the t-th type relation between the nodes. Without losing generality, we assume $\scriptstyle t = 1$ in this paper, namely, we treat the $1 ^ { \mathrm { s t } }$ type of links as the target dimension. Instead of using ${ A } ^ { ( 1 ) }$ and $X ^ { ( 1 ) }$ , we use A and X to denote the adjacent matrix and the similarity score matrix on the target dimension.

## 3.2 Matrix Completion for Link Prediction

To predict the hidden or absent links in the network, matrix completion can be used to obtain the latent space that reflects the essential features of network topology structure, and the potential link can be revealed through the latent space. We treat the adjacent matrix A of the network as the sparse matrix destroyed by noise or interference and use matrix completion to recover the original adjacent matrix as the final probability matrix X which reveals the potential links in the network. Our method uses a low-rank matrix $X$ to approximate the adjacent matrix A according to the known observed link set. For the observed link set in matrix $A = \left[ a _ { i j } \right]$ <sub>,</sub> we define the index set $\Omega = \left\{ \left( i , j \right) | a _ { i j } = 1 \right\}$ as the set of indexes of the non-zero elements in matrix A. Since X is the similarity score matrix including all the observed data in set $\varOmega ,$ we define $P _ { \Omega } ( X )$ as a projection operator on matrix X such that $P _ { \Omega } ( X )$ is a matrix satisfying:

$$
P _ {\Omega} (X) _ {i j} = \left\{ \begin{array}{l l} X _ {i j}, & (i, j) \in \Omega \\ 0, & \text { otherwise } \end{array} \right..\tag{1}
$$

Using the projection operator, we transfer the matrix completion problem for link prediction into the following low-rank matrix optimization:

$$
\begin{array}{l} \min _ {x} r a n k (X) \\ \text { s.t. } A = P _ {\Omega} (X) \end{array}\tag{2}
$$

Here, rank(X) is the rank of matrix X. Minimizing rank(X) means finding a latent space with the lowest dimension, keeping the non-zero elements of A in the latent space. In such latent space, the essential topological features of the original network are preserved. Since minimizing rank(X) is non-convex, we transform the optimization problem into a convex one as follows:

$$
\min _ {X} \left\| P _ {\Omega} (A - X) \right\| _ {F} ^ {2}\tag{3}
$$

$$
\text { s.t. } \quad \| X \| _ {*} ^ {2} \leq \lambda^ {2}
$$

Here, || $\boldsymbol { X } \parallel _ { * }$ is the nuclear norm of matrix $X . \parallel X \parallel _ { * }$ can be obtained by computing the summation of matrix $X \gamma$ singular values. Since problem (3) corresponds to a convex optimization, it has a unique solution. In (3), λ is a constant related to the expected rank of X, $\left\| A \right\| _ { F }$ is the Frobenius norm of matrix A.

## 4. Matrix Completion based Algorithm for Multi-Relational Link Prediction

## 4.1 Transforming Multi-Relational Link Prediction into Matrix Completion

In our multi-relational link prediction algorithm, probability matrix X should not only approximate the adjacent matrix of the target dimension, but also should approximate the adjacent matrixes of all the other types of links. For the adjacent matrix $A ^ { ( k ) } = \left[ a _ { i j } ^ { ( k ) } \right]$ of the k-th type links, we define the index set $\Omega _ { \boldsymbol { k } } = \left\{ ( i , j ) | a _ { i j } ^ { ( k ) } = 1 \right\}$ as the set of indexes of the non-zero elements in matrix ${ A } ^ { ( k ) }$ . Similar to the definition of $P _ { \it 2 } ( X )$ in (1), we define $P _ { \Omega _ { k } } \left( X \right)$ as a projection operator of X to all the observed data in set $\itOmega _ { k } .$ Then the optimization of (3) can be extended as

$$
\max _ {X} \frac {1}{2} \left\| P _ {\Omega_ {1}} (A ^ {(1)} - X) \right\| _ {F} ^ {2} + \sum_ {i = 2} ^ {d} \frac {\beta_ {i}}{2} \left\| P _ {\Omega_ {i}} (A ^ {(i)} - X) \right\| _ {F} ^ {2}\tag{4}
$$

$$
\text { s.t. } \quad \| X \| _ {*} ^ {2} \leq \lambda^ {2}
$$

Here, $\beta _ { i }$ is the similarity between the i-th type of link and the target one. Larger value of $\beta _ { i }$ indicates that links of the i-th type have greater influence on link prediction in the target dimension.

## 4.2 Optimization Problem for Matrix Completion

As a replacement of rank(X), nuclear norm is employed in (4) to construct a convex optimization. But nuclear norm cannot get satisfied results on the datasets which are not uniformly distributed. Hence, in our method, max-norm is exploited to replace the nuclear norm.

Let a factorization form of matrix A be $A = U L ^ { T }$ , where U and L are two n\*m nonnegative matrixes. Here m (m<n) is a constant. We define max-norm of A as follows:

$$
\left\| A \right\| _ {\max} = \min _ {U, L, A = U L ^ {T}} \frac {1}{2} \left[ \left\| U \right\| _ {2, \infty} ^ {2} + \left\| L \right\| _ {2, \infty} ^ {2} \right]\tag{5}
$$

Here, $\left\| A \right\| _ { 2 , \alpha }$ is defined as

$$
\left\| A \right\| _ {2, \infty} = \max _ {i = 1, 2, \dots , m} \left\| a _ {i} \right\| _ {2}\tag{6}
$$

where $a _ { i }$ is the i-th row vector in $A$ .

Using the max norm defined in (5) and (6), we can reform the problem (4) into the following optimization:

$$
\max _ {X} \frac {1}{2} \left\| P _ {\Omega_ {1}} \left(A ^ {(1)} - X\right) \right\| _ {F} ^ {2} + \sum_ {i = 2} ^ {d} \frac {\beta_ {i}}{2} \left\| P _ {\Omega_ {i}} \left(A ^ {(i)} - X\right) \right\| _ {F} ^ {2}\tag{7}
$$

$$
\mathrm{s.t.} \quad \left\| X \right\| _ {\mathrm{max}} ^ {2} \leq \lambda^ {2}
$$

Here, λ is a tunable parameter related to the expected rank of X.

An SDP (Semi-Definite Programming) solver can optimize $\left\| X \right\| _ { \operatorname* { m a x } }$ since it is convex. However, since SDP solvers are not scalable to large scale matrices, we propose a projected gradient method to solve optimization problem (7). We first reformulate the constrain in (7). Suppose matrix X can be factorized into $X { = } U L ^ { \mathrm { { T } } }$ , with $U { \in } R ^ { n \times m }$ and $L \in { \cal R } ^ { n \times m }$ . Based on this factorization, we can get the equivalent optimization:

$$
\min _ {U, L} \frac {1}{2} \left\| P _ {\Omega_ {1}} \left(A ^ {(1)} - U L ^ {T}\right) \right\| _ {F} ^ {2} + \sum_ {i = 2} ^ {d} \frac {\beta_ {i}}{2} \left\| P _ {\Omega_ {i}} \left(A ^ {(i)} - U L ^ {T}\right) \right\| _ {F} ^ {2}\tag{8}
$$

$$
\text { s.t. } \left\| U \right\| _ {2, \infty} \leq \lambda ; \quad \left\| L \right\| _ {2, \infty} \leq \lambda
$$

Since element $a _ { i j } ^ { k }$ in adjacent matrix ${ A ^ { ( k ) } }$ satisfies $\left| a _ { i j } ^ { k } \right| \leq 1$ and $U _ { _ { i } } . L _ { _ { j } } ^ { T }$ is supposed to approximate $a _ { i j } ^ { k }$ , we set $\lambda \ge 1$ . Since a larger value of λ could make the value of $| X _ { i j } |$ deviant away from 1, the value of λ should be a little bit larger than 1.

There are two advantages of using the factorization in (8). First, it requires only $O ( d . n )$ memory space which is much less than $O ( n ^ { 2 } )$ )of SDP. The second advantage is that a projected gradient descendent algorithm can be designed to make the method computationally scalable to large matrices. Although optimization of (8) is non-convex, any local minimum of (8) can approximate the global one if the value of d is set sufficiently large.

## 4.3 Estimating the Similarity between Types of Links

In the optimization problem (8), $\beta _ { i }$ is the similarity between the i-th type of link and the target one. There are several approaches to estimate the similarity between two types of links. This problem is to compute the similarity between two graphs. The detection of potential relations requires the information of the indirect relations between the users, that is to say, the global topology information is needed, rather than the local information. Therefore, using only the Pearson correlation coefficient of the columns in the adjacency matrix is not sufficient for detecting the potential relations. Here, we use the belief propagation method to obtain the information of global path between the users, and then use Pearson correlation coefficient of the global paths to measure the similarity between different types of relations.

First, for an edge $( \nu _ { i } , \nu _ { j } )$ in sub-graph $G _ { r } ,$ a transformation function $\psi _ { r } ( \nu _ { i } , \nu _ { j } )$ is computed as:

$$
\psi_ {r} \left(v _ {i}, v _ {j}\right) = \frac {a _ {i j} ^ {(r)}}{\sum_ {k \in N r (i)} a _ {i k} ^ {(r)}}\tag{9}
$$

Here, $N _ { r } ( i ) { = } \left\{ \nu \mid \nu \in V , ( \nu _ { i } , \nu ) \in E _ { r } \right\}$ is the set of nodes linked with $\nu _ { i } .$

To perform belief propagation in sub-graph $G _ { r }$ nodes send messages through the links iteratively. Denote the message node $\nu _ { i }$ sends to $\nu _ { j }$ in sub-graph $G _ { r }$ as $m _ { r } ( i , j )$ . The value of $m _ { r } ( i , j )$ is initially set as $\frac { 1 } { | V | + 1 }$ , and is recursively modified as:

$$
m _ {r} (j, i) = \psi_ {r} \left(v _ {j}, v _ {i}\right) \prod_ {k \in N r (j) \backslash i} m _ {r} (k, j)\tag{10}
$$

After convergence, the belief of a node $\nu _ { i }$ in sub-graph $G _ { r }$ is defined as:

$$
b _ {r i} = \frac {\sum_ {j \in N r (i)} m _ {r} (j , i)}{d _ {r} \left(v _ {i}\right)}\tag{11}
$$

Here, $d _ { r } ( \nu _ { i } )$ is the degree of $\nu _ { i }$ in sub-graph $G _ { r }$ .

A belief vector $b _ { r } { = } ( b _ { r 1 } , \ b _ { r 2 } { , } . . . , \ b _ { r n } )$ is used to denote the beliefs in sub-graph $G _ { r }$ . The similarity between sub-graph $G _ { r }$ and the target one $G _ { 1 }$ can be computed based on Pearson’s

coefficient of vectors $b _ { r }$ and $b _ { 1 } , ( r { = } 2 , . . . , d )$

$$
\beta_ {r} = \frac {n \sum_ {k = 1} ^ {n} \left(b _ {r k} - \bar {b} _ {r}\right) \left(b _ {1 k} - \bar {b} _ {1}\right)}{\sum_ {k = 1} ^ {n} \left(b _ {r k} - \bar {b} _ {r}\right) ^ {2} \sum_ {k = 1} ^ {N} \left(b _ {1 k} - \bar {b} _ {1}\right) ^ {2}}\tag{12}
$$

Here, $\overline { { b } } _ { r } = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } b _ { r k } \ : , \beta _ { r }$ is the similarity between the r-th and the target relation.

## 4.4 Solving the Optimization Problem

We present a projected gradient descendent algorithm to optimize (8). Let

$$
J (U, L) = \frac {1}{2} \left\| P _ {\Omega_ {1}} \left(A ^ {(1)} - U L ^ {T}\right) \right\| _ {F} ^ {2} + \sum_ {i = 2} ^ {d} \frac {\beta_ {i}}{2} \left\| P _ {\Omega_ {i}} \left(A ^ {(i)} - U L ^ {T}\right) \right\| _ {F} ^ {2}
$$

be the objective function, since U and L are variables in (8), we fix one of the variables at each iteration in the algorithm, and update the other one to minimize $J ( U , L )$ . After matrices U and L being initialized, they are modified by a gradient descendent method. In the method, the following two steps are performed iteratively until convergence:

(a) Fix matrix L，modify U to minimize $J ( U , L ) ;$

(b) Fix matrix U，modify L to minimize $J ( U , L )$ .

Rules for updating matrixes U and L in the iterations are as follows:

## (a) Updating matrix U

Fixing matrix L，the partial derivative of $J ( U , L )$ w.r.t. $U$ is,

$$
\frac {\partial J (U , L)}{\partial U} = P _ {\Omega_ {1}} \left[ \left(U L ^ {T} - A _ {1}\right) L \right] + \sum_ {i = 2} ^ {d} \beta_ {i} P _ {\Omega_ {k}} \left[ \left(U L ^ {T} - A _ {k}\right) L \right]\tag{13}
$$

Then we can get the following formula for updating $U { : }$

$$
U ^ {(t + 1)} = U ^ {(t)} - \mu_ {t} \frac {\partial J (U ^ {(t)} , L)}{\partial U}\tag{14}
$$

Here, $\mu _ { t }$ is the step size of the t-th iteration.

## (b) Updating matrix L

Fixing matrix U，the partial derivative of $J ( U , L )$ w.r.t. L is

$$
\frac {\partial J (U , L)}{\partial L} = P _ {\Omega_ {1}} \left[ \left(L U ^ {T} - A _ {1}\right) U \right] + \sum_ {i = 2} ^ {d} \beta_ {i} P _ {\Omega_ {k}} \left[ \left(L U ^ {T} - A _ {k}\right) U \right]\tag{15}
$$

Then we can get the following formula for updating L：

$$
L ^ {(t + 1)} = L ^ {(t)} - \mu_ {t} \frac {\partial J (U , L ^ {(t)})}{\partial L}\tag{16}
$$

In (14) and (16), $\mu _ { t }$ is the step size and can be set using the Armijo rule [55].

The inequality constraints in (8) can be addressed by a projection step. That is, when we have a new solution $( \boldsymbol { U } ^ { ( t ) } , \boldsymbol { L } ^ { ( t ) } )$ , we can check whether they violate the constraints. If not, we can proceed to the next iteration. Otherwise, we can scale the rows of matrixes U and L using coefficients $\frac { \lambda } { \left\| U \right\| _ { 2 , \infty } }$ , and $\frac { \lambda } { \left\| L \right\| _ { 2 , \infty } }$ respectively. Therefore, a shrinkage operator is defined as follows:

$$
\Gamma (A) = \left\{ \begin{array}{c c} \frac {\lambda}{\| A \| _ {2 , \infty}} A & \text { if } \| A \| _ {2, \infty} > \lambda \\ A & \text { otherwise } \end{array} \right.
$$

Using projection operator Γ, the formula for updating U and L in (14) and (16) can be replaced by the following formulas：

$$
U ^ {(t + 1)} = \Gamma \left(U ^ {(t)} - \mu_ {t} \frac {\partial J (U ^ {(t)} , L)}{\partial U}\right)\tag{17}
$$

$$
L ^ {(t + 1)} = \Gamma \left(L ^ {(t)} - \mu_ {t} \frac {\partial J (U , L ^ {(t)})}{\partial L}\right)\tag{18}
$$

## 4.4 The Algorithm

According to the above analysis, we present a matrix completion-based algorithm MCLP (Matrix Completion based Link Prediction) for multi-relational link prediction. The flowchart of our algorithm is illustrated in Figure 1 where we can see that the algorithm consists of three main steps:

Step 1: Compute similarity $\beta _ { r } \left( r \mathrm { = } 1 , 2 , . . . , d \right)$ between the r-th type relation and the target one;

Step 2: Get matrixes L and U by matrix completion on the adjacent matrixes;

Step 3: Compute and output similarity matrix X using L and U.

![](/api/attachments/Q3TM2KBS/fulltext/images/d1d04271ec6645ad0a398340d070483a807ba81676f84582fe291d1a5354c417.jpg)  
Figure 1 The flowchart of algorithm MCLP

Let the positive integer $N _ { m a x }$ be the maximum number of iteration steps, algorithm MCLP is described as follows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm MCLP
input:
 $A^{(1)}, A^{(2)}, ..., A^{(d)}$ : adjacent matrices of different types of links;
d: number of different types of links;
Nmax: positive integer, maximum number of iterations;

output:
X: similarity score matrix for link prediction;

Begin
1. For r=1 to d do
2. For each edge ( $v_i, v_j$ ) in  $G_r$ , compute transformation probability  $\psi_r(v_i, v_j)$  according to (9);
3. For every edge ( $v_i, v_j$ ) in  $G_r$ , recursively compute the message  $m_r(i,j)$  according to (10);
4. For every node  $v_i$  in  $G_r$ , compute its belief  $b_{ri}$  according to (11);
5. If r&gt;1 then compute  $\beta_r$  according to (12);
6. /*  $\beta_r$  is the similarity between the r-th and the target relation*/
7. Endfor r;
8. Set initial solutions of  $U^{(0)}$  and  $L^{(0)}$ ;
9. for t=0 to N max do
9.1 Compute  $d_U^{(t)} = \frac{\partial J(U^{(t)}, L)}{\partial U}$  according to (13);
9.2  $U^{(t+1)} = \Gamma(U^{(t)} - \mu_t d_U^{(t)})$ ;
9.3 Compute  $d_L^{(t)} = \frac{\partial J(U, L^{(t)})}{\partial L}$  according to (15);
9.4  $L^{(t+1)} = \Gamma(L^{(t)} - \mu_t d_L^{(t)})$ ;
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
End for t;
10. Compute probability matrix for link prediction:
 $X = U^{(N\max)}(L^{(N\max)})^{T}$ ;
Output(X);
End
</div>

In the algorithm, lines 1 to 7 compute the transformation probability between the nodes and the similarity between the relations. Line 2 computes the transformation probabilities according to (9) in $O ( m )$ time. Line 3 computes the messages $m _ { r }$ according to (10) in $O ( n ^ { 2 } )$ time，and line 4 computes the belief of the nodes according to (11) in O(n) time. Similarity between the target relation and the other ones are computed by line 5 according to (12) in O(d.n) time. Line 8 sets the initial values of ${ \cal U } ^ { ( 0 ) }$ and ${ \boldsymbol { V } } ^ { ( 0 ) }$ in ${ \mathrm { O } } ( n ^ { * } m )$ time. Lines 9.1 and 9.3 compute the partial derivatives according to (13) and (15) respectively. From (13) and (15), we can see that lines 9.1 and 9.3 require $ { \mathrm { O } } ( d . m . n ^ { 2 } )$ time. Lines 9.2 and 9.4 update U and V by performing the shrinkage operator, which requires O(m.n) time. Line 10 computes and outputs the similarities between the nodes in the network in $O ( m . n ^ { 2 } )$ time. Since m and d can be considered as constants, time complexity of MCLP is $O ( n ^ { 2 } )$ . Since there are $\frac { n ( n - 1 ) } { 2 }$ node pairs in the network, similarity-based link prediction methods require at least ${ \mathrm { O } } ( n ^ { 2 } )$ time. Therefore, algorithm MCLP reaches the lower bound of the time complexity for a similarity-based link prediction method.

## 5. Experimental Results and Analyses

## 5.1. Experimental Environment

We test the algorithm MCLP on some real networks and compare the results with those of four methods based on indexes CN, JC, PA, and AA. The performance of MCLP is also compared with that of the nonnegative matrix factorization based multi-relational link prediction method LPMR [48]. All the tests are conducted on Pentium IV processor with 1.7G memory, under Windows XP operating system. The algorithms are coded in VC++ 6. 0. We set $\lambda = 1 . 2$ in our experiments.

## 5.2. Evaluation Data Sets

In our experiments, four multi-relational networks are used to test the presented method. The four datasets are YouTube, disease-gene network, climate network, and DBLP .

## A. YouTube Network

YouTube dataset [56] consists of users and the videos they are interested. The network has 5,088 nodes representing the users, which are linked by five types of relations including: the links of contacts among those users (CNU); the links between the users who both link to the same user beyond YouTube (FR); the links between the users who subscribe to the same user (SBN); the links between the users who are both subscribed by the same user (SBR); the links between the users which share favorite videos (VID). The main topological features of these types of relations in YouTube data are shown in Table 2.

Table 2 Numbers of nodes and edges in YouTube data tested

<table><tr><td>Nodes</td><td colspan="5">Edges in different types of relations</td></tr><tr><td>Users</td><td>CNU</td><td>FR</td><td>SBN</td><td>SBR</td><td>VID</td></tr><tr><td>15,088</td><td>76,765</td><td>1,940,806</td><td>2,239,440</td><td>5,574,249</td><td>3,797,635</td></tr></table>

## B. Disease-gene Network

The disease-gene (DG) [57] dataset represents a bipartite network consisting of two parts of nodes. One part contains nodes of genes and the other contains nodes of diseases. There are four types of relations in the network: genetic association(G), phenotypic (P), protein-protein interaction (PPI) and phosphor motif finder (F). The main topological features of the Disease-Gene Network are shown in Table 3.

Table 3 Numbers of nodes and edges in the Disease-Gene Network tested

<table><tr><td colspan="2">Nodes</td><td colspan="4">Edges in different types of relations</td></tr><tr><td>Diseases</td><td>Genes</td><td>G</td><td>P</td><td>PPI</td><td>F</td></tr><tr><td>703</td><td>1,132</td><td>10,483</td><td>74,523</td><td>2,450</td><td>3,279</td></tr></table>

## C. Climate Network

The climate network [58] we tested in the experiment consists of 1701 nodes representing different geographical locations. The edges between nodes indicate the climate relations between the locations they connected. There are six types of climate relations, which are: geopotential height (GH), relative humidity (RH), precipitable water (PW), vertical wind speed (VWS), horizontal wind speed (HWS), sea level pressure (SLP), temperature (SST). In the experiment, loose connected links are deleted according to the nodes similarity. An edge with one type can overlap with links of some other types, and a single node pair may linked by relations of up to seven different types. The main topological features of the Climate Network are shown in Table 4.

Table 4 Numbers of nodes and edges in the Climate Network tested

<table><tr><td>Nodes</td><td colspan="7">Edges in different types of relations</td></tr><tr><td>Locations</td><td>GH</td><td>VWS</td><td>PW</td><td>RH</td><td>SST</td><td>SLP</td><td>HWS</td></tr><tr><td>1,701</td><td>249,322</td><td>71,458</td><td>50,835</td><td>25,375</td><td>132,469</td><td>175,786</td><td>31,615</td></tr></table>

## D. DBLP network

DBLP [59] is a dataset consisting of publications in the areas in information technology and computational science. Each node in the network symbolizes an author. In the experiment, we select 2041 authors from DBLP which are represented by the nodes connected by three types of relations. These three types of relations represent different interactions, which are the common conference (CC): two authors show up in the same conference in the same year; co-author (CA): two authors collaborate on at least one paper; common terms (CT): two authors have publications with similar terms of topic. Table 5 shows the main topological features of DBLP data .

Table 5 Numbers of nodes and edges in the DBLP Network tested

<table><tr><td>Nodes</td><td colspan="3">Edges in different types of relations</td></tr><tr><td>Authors</td><td>CC</td><td>CA</td><td>CT</td></tr><tr><td>1,701</td><td>249,322</td><td>71,458</td><td>50,835</td></tr></table>

## 5.3. Compared Methods

In our experiments, we compare the results by MCLP with those of four similarity-based methods, and the nonnegative matrix factorization based multi-relational network link prediction

method LPMR [48].

In the test of the four similarity-based algorithms, the multiple relations are integrated as a single relational one. These four index-based methods are commonly used in relation prediction and are also used as a benchmark method to compare the quality of the prediction results. The methods are based on the following 4 indexes:

1) Common Neighbors (CN). For a node x, let $\Gamma ( x )$ denote the set of neighbors of x. In common sense, two nodes x and y are more likely to have a link if they have many common neighbors. The common neighbors index is defined as:

$$
S _ {x y} ^ {C N} = | \Gamma (x) I \Gamma (y) |,\tag{19}
$$

where $\left| \Gamma ( x ) \right|$ is the cardinality of the set $\Gamma ( x )$

2) Jaccard Index (JC). This index was proposed by Jaccard and is defined as:

$$
S _ {x y} ^ {J C} = \frac {\left| \Gamma (x) I \Gamma (y) \right|}{\left| \Gamma (x) Y \Gamma (y) \right|}.\tag{20}
$$

3) Preferential Attachment Index (PA). The basic idea of preferential attachment index is that the probability that a new link is connected to the node x is proportional to its degree $k _ { x }$ . The probability that a new link will connect x and y is proportional to $k _ { x } \times k _ { y }$ . Therefore, the corresponding similarity index can be defined as:

$$
S _ {x y} ^ {P A} = k _ {x} \times k _ {y},\tag{21}
$$

4) Adamic-Adar Index (AA). This index refines the simple counting of common neighbors by assigning the less-connected neighbors more weight, and is defined as:

$$
S _ {x y} ^ {A A} = \sum_ {z \in \Gamma (x) I \Gamma (y)} \frac {1}{\log k _ {z}}.\tag{22}
$$

The performance of MCLP is also compared with that of the nonnegative matrix factorization (NMF) based multi-relational network link prediction method LPMR [48]. LPMR first gets a lower rank matrix by nonnegative matrix factorization on the similarity matrix, and then obtains the predicting results from the latent space represented by the lower rank matrix. Since both our method MCLP and LPMR perform link prediction by getting a lower rank matrix which carries important features of the network, we test LPMR and compare its performance with MCLP.

## 5.4 Quality Measurements for the Prediction Results

In the experiments, we use AUC score, precision, recall and F-measure to measure the quality of the prediction results.

## (1) AUC score

AUC (Area Under Curve) was originally a measurement to evaluate the model of binary classification. AUC is defined as the area under the ROC (receiver operating characteristic) curve. An ROC curve is built by plotting the true positive rate against the false positive rate at different threshold values. Therefore, AUC is just the probability that a randomly chosen positive object is ranked higher than a randomly chosen negative one.

AUC score also can be applied to estimate the quality of link prediction results. In this case, AUC is equal to the probability that the similarity index of a randomly selected existing link is higher than that of a randomly selected non-existing one. To compute the AUC score, we rank the similarity indexes of the existing and non-existing edges. Then we compare the similarity indexes of n pairs of existing and non-existing edges. If among these n pairs of edges, the score of existing edge is larger than the non-existing one in n’ comparisons, and the score of existing edge is equal to the non-existing one in n’’ comparisons, then the AUC is

$$
A U C = \frac {n ^ {\prime} + 0 . 5 n ^ {\prime \prime}}{n}\tag{23}
$$

A higher AUC score commonly represents better quality of predicting results. From (23) we can see that the highest AUC is 1 which indicates an absolutely correct result. The AUC score of a completely random prediction is 0.5.

## (2) Precision

If in the L node pairs with the highest similarity scores, only m node pairs represent existing edges, then the precision is：

$$
p r e c i s i o n = \frac {m}{L}\tag{24}
$$

## (3) Recall

If an algorithm predicts m existing edges in E , then the recall of the predicting result is

defined by:

$$
r e c a l l = \frac {m}{| E |}\tag{25}
$$

## (4) F-measure

Based on the precision and recall of a link prediction result, the F-measure can be defined as:

$$
F = \frac {2 \times p r e c i s i o n \times r e c a l l}{p r e c i s i o n + r e c a l l}\tag{26}
$$

Because F-measure combines precision and recall collectively, it is a comprehensive measurement for the quality of the link prediction results.

From the definitions, we can see that larger AUC value means the higher probability that a randomly chosen existing relation is ranked higher than a randomly chosen non-existing one. High precision means that an algorithm returned substantially more relevant relations than irrelevant ones, while high recall means that an algorithm returned most of the relevant relations. But in fact there is a contradiction between the measurements of precision and recall. For example, in extreme cases, if we detected only one relation out of many existing ones, the precision is 100%, but recall is low. If we return all the existing and non-existing relations, the recall is 100%, but precision is low. Therefore, it is necessary to judge which measurement is more important according to the cost of its error in the specific application. For instance, when we detect the hidden interactions and relations between the terrorists, our goal is to predict all their possible interactions and relations. If we fail to detect a terrorist, the cost of this error is very high. Thus the measurement of recall is more important. On the other hand, when we predict the relationship between customers for the sake of marketing, we hope that all the predicted relationships are true, so as to reduce the cost of advertising promotion. If we put an unrelated person as customer, this error will increase the unnecessary cost of sales. In this case, the measurement of precision is more important. In some situations, we want to find an optimal blend of precision and recall, we can combine the two metrics into the index F-measure as a collective measurement for the quality of the link prediction results.

To carry out the performance evaluation precisely and reduce the evaluation error，we apply the random 10-fold CV (cross validation). In the test, edges in the network are partitioned into 10 subsets randomly. From the 10 subsets, one subset is chosen as the test set, and the other 9 subsets are the training data. Such 10-fold CV procedure is performed 10 times on different training data sets. The average values of AUC scores, precisions, recalls and F-measures in the 10 tests on are treated as the final results.

## 5.5 Comparison of the AUC Scores

AUC scores of MCLP and the other methods on four datasets are shown in Tables 6 to 9. In the tables, each row lists the AUCs in the experiment using one type of link as the target relation. On each target relation, the largest AUC by the six methods is highlighted in bold numbers, while the second-largest is underlined.

Table 6 Comparison of AUC scores by MCLP with other methods for YouTube

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>CNU</td><td>0.783</td><td>0.781</td><td>0.865</td><td>0.784</td><td>0.947</td><td>0.955</td></tr><tr><td>FR</td><td>0.984</td><td>0.988</td><td>0.934</td><td>0.986</td><td>0.985</td><td>0.989</td></tr><tr><td>SBN</td><td>0.98</td><td>0.982</td><td>0.944</td><td>0.981</td><td>0.983</td><td>0.986</td></tr><tr><td>SBR</td><td>0.988</td><td>0.987</td><td>0.946</td><td>0.985</td><td>0.989</td><td>0.988</td></tr><tr><td>VID</td><td>0.971</td><td>0.968</td><td>0.957</td><td>0.973</td><td>0.975</td><td>0.981</td></tr></table>

Table 6 lists the AUCs of MCLP and the other methods on YouTube dataset. It can be seen from Table 6 that MCLP obtains the largest AUCs on four relations. For example, on the relation CNU, Algorithm MCLP achieves the largest AUC score 0.955, which is much higher than the second-largest AUC 0.947. For the relation SBR, MCLP obtains the second-largest AUC, which is slightly lower than the highest score 0.989.

Table 7 Comparison of AUC scores by MCLP with other methods for Disease-Gene Network

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>G</td><td>0.951</td><td>0.957</td><td>0.903</td><td>0.956</td><td> $\underline{0.972}$ </td><td>0.979</td></tr><tr><td>P</td><td>0.909</td><td>0.771</td><td> $\underline{0.943}$ </td><td>0.911</td><td>0.938</td><td>0.952</td></tr><tr><td>PPI</td><td>0.788</td><td>0.786</td><td>0.827</td><td>0.789</td><td> $\underline{0.831}$ </td><td>0.847</td></tr></table>

The AUC scores of MCLP and the other algorithms on Disease-Gene Network dataset are listed in Table 7, which shows that MCLP achieves the largest AUCs on all the relations. For instance, AUC score of MCLP is 0.952 on relation P, which is much larger than the second-largest score 0.943.

Table 8 Comparison of the AUC scores by MCLP with other methods on the Climate Network

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>GH</td><td>0.985</td><td>0.987</td><td>0.783</td><td>0.986</td><td>0.992</td><td>0.991</td></tr><tr><td>VWS</td><td>0.935</td><td>0.954</td><td>0.802</td><td>0.942</td><td>0.949</td><td>0.957</td></tr><tr><td>PW</td><td>0.990</td><td>0.995</td><td>0.717</td><td>0.992</td><td>0.995</td><td>0.994</td></tr><tr><td>RH</td><td>0.992</td><td>0.995</td><td>0.681</td><td>0.993</td><td>0.994</td><td>0.996</td></tr><tr><td>SST</td><td>0.956</td><td>0.973</td><td>0.776</td><td>0.962</td><td>0.975</td><td>0.981</td></tr><tr><td>SLP</td><td>0.979</td><td>0.985</td><td>0.698</td><td>0.981</td><td>0.988</td><td>0.989</td></tr><tr><td>HWS</td><td>0.990</td><td>0.973</td><td>0.731</td><td>0.992</td><td>0.995</td><td>0.997</td></tr></table>

Table 8 demonstrates the AUCs of algorithm MCLP and the other algorithms on Climate dataset. It can be seen from Table 8 that MCLP gets the largest AUCs on 5 relations. For example, on the relation SST, AUC score of algorithm MCLP is 0.981, which is much larger than the second-largest AUC 0.975. For the relations PW and GH, MCLP obtains the second-highest AUC scores, which are 0.001 lower than the highest one. The slight lower AUC score of MCLP in a few relations is due to the sparseness of those types of relations, which may reduce the precision of the matrix completion.

Table 9 Comparison of MCLP AUC scores with other methods on DBLP Network

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>CC</td><td>0.8328</td><td>0.6653</td><td>0.7365</td><td>0.8417</td><td>0.8425</td><td>0.8519</td></tr><tr><td>CA</td><td>0.9805</td><td>0.5274</td><td>0.5533</td><td>0.9112</td><td>0.9818</td><td>0.9827</td></tr><tr><td>CT</td><td>0.9632</td><td>0.7023</td><td>0.7359</td><td>0.9278</td><td>0.9381</td><td>0.9701</td></tr></table>

Table 9 compares the AUC scores of MCLP with other methods on DBLP Network. It can be observed from Table 9 that MCLP can achieve the largest AUCs on all the relations. For instance, AUC score of algorithm MCLP is 0.9701 on the relation CT, which is much larger than the second-largest one 0.9632.

The high AUC score MCLP obtained is due to the multiple matrix completion, which can recover a proper latent space to reflect the hidden topological structure of the target relation. Moreover, MCLP uses the influence from the other types of relations on the target one to integrate the topological structures of different types of relations.

## 5.6 Precisions of the Test Results

The precision of algorithm MCLP is also tested and compared with those of the other algorithms on four datasets. Figures 2 to 5 demonstrate the test results.

![](/api/attachments/Q3TM2KBS/fulltext/images/874e64a4eb70a21f22fc4f5fe63064555a323e1a65d52091b1c2c7374c15635a.jpg)  
Figure 2 Precisions of the six algorithms on YouTube dataset

Figure 2 depicts the precisions of MCLP and the other algorithms on YouTube dataset. It can be observed from Figure 2 that MCLP can obtain the largest precision in predicting most of the relations in YouTube. For relation SBR, the MCLP’s precision is the second largest, a little bit less than that of LPMR.

![](/api/attachments/Q3TM2KBS/fulltext/images/1fee0361bd293fd872a40f1debe24f230a6a225aed5dfc6aaa53c088b43ed702.jpg)  
Figure 3 Precisions of the six algorithms on Disease-Gene Dataset

Figure 3 shows the precisions of algorithm MCLP and the other algorithms on Disease-Gene dataset. From Figure 3, we can see that MCLP can obtain the highest precision among the six methods on all the relations in the Disease-Gene Network.

![](/api/attachments/Q3TM2KBS/fulltext/images/c789d1b6f315a1db3ec740acf2ca143fc26efb59260647ee6f8b0f183e0ab7e1.jpg)  
Figure 4 Precisions of the six algorithms on Climate dataset

The precisions of MCLP and the other algorithms on Climate Network dataset are depicted in Figure 4, where we can see that MCLP can get the highest precisions among the six methods in predicting the 6 relations in the Climate Network. For relation PW, MCLP’s precision is the second highest, a little bit less than that of LPMR.

For the relation SBR in YouTube and the relation PW in Climate Network, the precisions of MCLP are slightly lower than the highest one. This is because that connections in those types of relations are denser or sparser than the other ones. The topological information of other types of relations has very little contribution on predicting those types of relations.

![](/api/attachments/Q3TM2KBS/fulltext/images/d70e9ac33075a2b618fb29dd210bb2aa1594d72d955f8656abe8f0abf90c6782.jpg)  
Figure 5 Precisions of the six algorithms on DBLP Network dataset

Figure 5 demonstrates the precisions by MCLP and compares with the other algorithms on

DBLP Network dataset. From Figure 5, we can see that among the six algorithms, MCLP has the highest precision on all the relations.

It can be seen from Figures 2 to 5 that on most of the relations in all networks tested, MCLP’s precisions are the highest among the six algorithms. Therefore, we can see that MCLP can always assign higher scores to the existing edges, and obtains more accurate prediction results.

Our method maps the different types of links to the same latent space, which can reveal the essential topological characteristics of the various types of links. In addition, since the latent space takes into consideration the relationship between the different types of links, it can improve the quality of prediction results. Other methods simply analyze the topological structures within each type of links, and ignore its interactions with the links of other types. At the same time, they only consider the local relations between users, but fail to consider the global relations. Therefore, our method can achieve higher quality results than other methods.

## 5.7 Recalls of the Test Results

The recalls of the predicting results by algorithm MCLP are also tested and compared with those of the other methods. Figures 6 to 9 demonstrate the test results.

Figure 6 shows recalls of the six algorithms on YouTube dataset, where we can see that the recalls of MCLP are higher than those of all the other methods in the relations FR, SBR and SBN. For the relation CNU, recall of MCLP is the second highest, being a little bit less than that of JC. This is because the measurement of recall only considers the percentage of detected relations among the existing ones. For the sparsely connected relation types, our algorithm may produce slightly lower recalls.

![](/api/attachments/Q3TM2KBS/fulltext/images/f5413f44711319f7c39343f67311cc28689a157abda929e7756acbf345ac1377.jpg)  
Figure 6 Recalls of the six algorithms on YouTube dataset

Recalls of the six methods on the Disease-Gene dataset are shown in Figure 7, where we can see that recalls of MCLP are the highest among the six methods in all types of the relations. For example, MCLP’s recall in relation G type is 85.1%, while that of CN is 76.8%.

![](/api/attachments/Q3TM2KBS/fulltext/images/7c0ba3cf48504fb1619d2c1e6af74cb72ec76bea4daecd00eb5d92bb831e1e1d.jpg)  
Figure 7 Recalls of the six algorithms on Disease-Gene Network dataset

![](/api/attachments/Q3TM2KBS/fulltext/images/0dffda5036d718470241fab6fe27299f80d42df5ed80c93605c88ce5386e82b9.jpg)  
Figure 8 Recalls of the six algorithms on Climate

Figure 8 shows recalls of the six algorithms on Climate dataset. From Figure 8 we can see that MCLP’s recalls are the highest among the six methods in all types of relations except HWS. For the relation of HWS, the recall of MCLP is the second highest, being a little bit less than that of JC. This is because the relation HWS is a sparsely connected relation type, our algorithm may produce slightly lower recall.

![](/api/attachments/Q3TM2KBS/fulltext/images/e80a9443672a962dcc93a0400bc31d8e05668940f466ce770f13e672304c12fc.jpg)  
Figure 9 Recalls of the six algorithms on DBLP dataset

Recalls of the six algorithms on DBLP dataset are demonstrated in Figure 9, where we can observe that recalls of MCLP are the highest among the six methods in all types of relations. For instance, MCLP’s recall in relation CT is 83.8%, while the second highest one is 81.4% by LPMR, and the lowest one is 71.9% by JC.

From Figures 6 to 9, we can see that in the experiments on the most types of relations in the networks tested, recalls of MCLP are the highest among the six methods. This means that more existing links can be detected by MCLP than the other methods. Therefore, algorithm MCLP can achieve more accurate results than the other methods.

## 5.8 F-measures of the Test Results

F-measure can be used to estimate the overall quality of the prediction results. In Tables 10 to 13, we compare the F-measures of the predicting results by MCLP and the other algorithms. In the figures, the largest F-measures of each type of relation by the six algorithms is highlighted in bold numbers, and the second-largest F-measure is underlined.

Table 10 F-measures of the six methods on YouTube

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>CNU</td><td>72.59</td><td>80.79</td><td>75.3</td><td>71.76</td><td>83.11</td><td>84.81</td></tr><tr><td>FR</td><td>79.78</td><td>79.74</td><td>76.27</td><td>75.21</td><td>84.11</td><td>86.61</td></tr><tr><td>SBN</td><td>78.55</td><td>81.64</td><td>73.34</td><td>75.51</td><td>85.50</td><td>87.84</td></tr><tr><td>SBR</td><td>80.00</td><td>78.47</td><td>74.19</td><td>73.87</td><td>83.51</td><td>83.71</td></tr><tr><td>VID</td><td>77.38</td><td>75.93</td><td>77.53</td><td>71.79</td><td>80.97</td><td>86.42</td></tr></table>

Table 11 F-measures of the six methods on the Disease-Gene Network

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>G</td><td>81.63</td><td>77.29</td><td>84.51</td><td>85.47</td><td> $\underline{87.58}$ </td><td>89.10</td></tr><tr><td>P</td><td>80.92</td><td>74.66</td><td>82.43</td><td>76.59</td><td> $\underline{87.59}$ </td><td>88.29</td></tr><tr><td>PPI</td><td>78.10</td><td>72.02</td><td>77.68</td><td>73.08</td><td> $\underline{79.22}$ </td><td>82.34</td></tr></table>

Table 12 F-measures of the six methods on Climate

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>GH</td><td>74.92</td><td>76.69</td><td>79.41</td><td>83.37</td><td>85.77</td><td>85.97</td></tr><tr><td>VWS</td><td>79.67</td><td>77.34</td><td>76.2</td><td>83.48</td><td>85.90</td><td>86.74</td></tr><tr><td>PW</td><td>79.92</td><td>84.92</td><td>76.96</td><td>83.69</td><td>85.44</td><td>85.75</td></tr><tr><td>RH</td><td>80.05</td><td>75.62</td><td>78.27</td><td>77.25</td><td>80.94</td><td>84.29</td></tr><tr><td>SST</td><td>79.13</td><td>79.41</td><td>77.94</td><td>76.34</td><td>85.21</td><td>85.83</td></tr><tr><td>SLP</td><td>72.79</td><td>80.71</td><td>78.49</td><td>76.65</td><td>80.96</td><td>83.99</td></tr><tr><td>HWS</td><td>79.43</td><td>83.16</td><td>81.64</td><td>79.39</td><td>83.68</td><td>85.39</td></tr></table>

Table 13 F-measures of the six methods on the DBLP Network

<table><tr><td>Methods Relations</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td><td>MCLP</td></tr><tr><td>CC</td><td>81.20</td><td>68.14</td><td>74.17</td><td>82.59</td><td>83.66</td><td>84.50</td></tr><tr><td>CA</td><td>85.25</td><td>61.85</td><td>64.92</td><td>82.91</td><td>86.46</td><td>88.28</td></tr><tr><td>CT</td><td>85.49</td><td>71.94</td><td>72.85</td><td>82.72</td><td>84.48</td><td>86.88</td></tr></table>

From the tables, we can observe that MCLP’s F-measures are the highest among these methods in predicting all the relations in all the datasets. For instance, MCLP’s F-measure values on all the relations in YouTube are roughly 10% to 15% higher than those of AA. For dataset Disease-Gene, MCLP’s F-measure values on all the relations are approximately 10% to 12% higher than those of JC. For the Climate Network dataset, the F-measure values of MCLP on the relations are 5% to 11% higher than those of CN. For dataset DBLP, MCLP’s F-measure values on all the relations are approximately 15% higher than those of JC.

## 5.9 T-test on the Results

We also use paired t-test to show that the F-measures and AUC scores on different relations in all the datasets by MCLP are significantly different from that of the other algorithms.

We first conducted paired t-test on the F-measures and AUC scores of all the relations in all the datasets listed in Tables 6 to 13. Table 14 shows the results of t-values of the F-measures and AUC scores by MCLP with other algorithms.

Table 14 t-values of F-measures and AUCs by MCLP with other methods

<table><tr><td>Algorithm</td><td>CN</td><td>JC</td><td>PA</td><td>AA</td><td>LPMR</td></tr><tr><td>t-values of F-measures with MCLP</td><td>7.3080</td><td>6.6805</td><td>8.3265</td><td>6.4991</td><td>2.5813</td></tr><tr><td>t-values of AUC scores with MCLP</td><td>1.3268</td><td>2.2100</td><td>5.4374</td><td>1.4308</td><td>0.4103</td></tr></table>

Because each group of data has 18 samples, the degree of freedom in the t-test is（18-1） \*2=34. From t-distribution table, we can know that $t _ { 0 . 9 9 9 } ( 3 4 ) = 3 . 6 0 1 , t _ { 0 . 9 8 } ( 3 4 ) = 2 . 4 4 1$ $t _ { 0 . 9 5 } ( 3 4 ) \substack { = } 2 . 0 3 2 , t _ { 0 . 8 0 } ( 3 4 ) \substack { = } 1 . 3 0 7$ . From Table 14, we can see that there is significant difference between the F-measures by MCLP and the algorithms CN, JC, PA and AA at the significance level $\scriptstyle \alpha = 0 . 0 0 1 \ \ ( p = 0 . 9 9 9 )$ . If we set the significance level $\scriptstyle a = 0 . 0 2 \ ( p = 0 . 9 8 )$ , then there is significant difference between the F-measures by MCLP and the algorithm LPMR. As for the AUC scores, if we set the significance level α=0.001 (p=0.999) then there is significant difference between the AUCs by MCLP and the algorithm PA. There is also significant difference between the AUCs by MCLP and the algorithm JC at the significance level $\scriptstyle \alpha = 0 . 0 5 \ ( p = 0 . 9 5 )$ . At the significance level $\scriptstyle { a = 0 . 2 } \ ( p = 0 . 8 )$ , there is significant difference between the AUCs by MCLP and the algorithms CN and AA. Although the average AUC score of MCLP is higher than that of LPMR, there is no significant difference between the AUCs by MCLP and the algorithm LPMR. This is because different types of relations in the networks are unevenly distributed. In highly skewed datasets, F-measure can more effectively measure the quality of prediction results than AUC score. Since there is significant difference between the F-measures by MCLP and LPMR at significance level $\scriptstyle \alpha = 0 . 0 2 \ ( { \mathrm { p } } { = } 0 . 9 8 )$ , the overall quality of MCLP is obviously better than the algorithm LPMR.

Since F-measure effectively combines recall and precision, it can accurately evaluate the overall quality of the predicting results. From the table we can see that there is significant difference between the F-measures by MCLP and all the other methods at significance levels α=0.001 and 0.02. This shows that MCLP has strong ability to improve the quality of the relation prediction on the multi-relational networks.

Then we conducted paired t-tests on the 10 AUC scores and the F-measurements in each 10-fold CV test on the all relations in all the data sets. The test results also show that there is significant difference between the F-measures and AUC scores by MCLP and the other methods at different significance levels.

We can see from the experiments that MCLP has significantly improved the quality of the multi-relation prediction results. The reason for MCLP obtain high quality predicting results is that it uses the influence from the relations of other types on the target one to integrate the topological structures of different types of relations. In addition, MCLP employs matrix completion to recover a proper latent space reflecting the hidden topological structures of the target relations.

## 6. Conclusions and Future Works

Detecting potential social relations between individuals has great importance for decision making in marketing, business strategy, human resources development, finance planning, business transformation, insurance policy design. Relation prediction on social network has attracted more attention of the decision makers from many business disciplines, such as virus marketing, merchandise recommendation, social trust prediction, social influence maximization, retail transaction prediction, community detecting, and tourism management. People are used to consulting the relations between members for useful information and corporations are seeking opportunities to leverage them for “word of mouth” advertising. The prediction of potential social relations between individuals is helpful for discovering potential customers or members of organizations, which will then help both people and corporations to secure their long-term interests. In the real society, there are many types of relationships between people, such as friends, colleagues, relatives, classmates, partners, etc. When we detect on type of relation, information about other types of relationships also plays an important role.

Link prediction is an important tool in detecting relations in trade and social networks. To predict the potential relations in multi-relational networks, we should take into account the relevance and impact between various types of relations. A matrix completion based algorithm MCLP is proposed for predicting multiple relations in social networks. First, the belief of each node is calculated to build a belief vector for each type of relations by belief propagation. Based on the belief vectors, the similarities between different types of relations are computed to measure

# ACCEPTED MANUSCRIPT

their mutual influence. Based on the similarities between various types of relations, we model the link prediction as the matrix completion by optimization on its max-norm constrained formulation. Since max-norm is not easy to optimize, we utilize a reformulation of max-norm, and propose a projected gradient optimization algorithm which is scalable to large scale social networks. We test our algorithm by abundant experiments on real networks and compare the results with other recent link prediction methods. Experimental results show that algorithm MCLP outperforms other similar algorithms, and can achieve more accurate results on multi-relational networks. We also show the time complexity of algorithm MCLP reaches the lower bound for a similarity based link prediction method.

In many real social networks, the users may have attributes, such as their age, gender, occupation, income, habit, hobby etc. which are very valuable for their relationship prediction. In our current study, we ignore such useful information of users’ attributes. In addition, our study is focusing on static networks, where the latent relations between the users are fixed. However, the relations between the users in a social network are changing with time. Therefore, it is our future work to study on the efficient method to predict the potential relations in dynamic social networks with users’ attributes.

## Acknowledgements

This research was supported in part by the Chinese National Natural Science Foundation under grant Nos. 61379066, 61702441, 61379064，61472344, 61402395 and 61602202; Natural Science Foundation of Jiangsu Province under contracts BK20130452, BK2012672 ， BK2012128, BK20140492 and Natural Science Foundation of Education Department of Jiangsu Province under contract 12KJB520019, 13KJB520026, 09KJB20013. Six talent peaks project in Jiangsu Province(Grant No. 2011-DZXX-032).

## References

[1] Rajarshi Chakraborty, Jaeung Lee, Sharmistha Bagchi-Sen, Shambhu Upadhyaya, H. Raghav Rao, Online shopping intention in the context of data breach in online retail stores: An examination of older and younger adults, Decision Support Systems, 83 (2016) 47-56.

[2] Bo Xiao, Izak Benbasat, An empirical examination of the influence of biased personalized product recommendations on consumers' decision making outcomes, Decision Support Systems, 110 (2018) 46-57

[3] F. Xie, Z. Chen, J. X. Shang, X. P. Feng, J. Li, A link prediction approach for item recommendation with complex number, Knowledge- based Systems. 81(2015) 148-158.

[4] Shankhadeep Banerjee, Samadrita Bhattacharyya, Indranil Bose, Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business, Decision Support Systems, 96 (2017) 17-26.

[5] Hui Fang, Guibing Guo, Jie Zhang, Multi-faceted trust and distrust prediction for recommender systems, Decision Support Systems, 71 (2015) 37-47

[6] Michael Siering, Amit V.Deokar, Christian Janze, Disentangling consumer recommendations: Explaining and predicting airline recommendations based on online reviews, Decision Support Systems, 107 (2018) 52-63

[7] J. Li, L. L. Zhang, F. Meng, F. H. Li, Recommendation Algorithm based on Link Prediction and Domain Knowledge in Retail Transactions, Procedia Computer Science. 31(2014) 875-881.

[8] V. Kumar, V. Bhaskaran, R. Mirchandani, M. Shah, Practice prize winner—creating a measurable social media marketing strategy: increasing the value and ROI of intangibles and tangibles for hokey pokey, Marketing Science 32 (2) (2013) 194–212.

[9] I. Roelens, P. Baecke, D. F. Benoit, Identifying influencers in a social network: The value of real referral data, Decision Support Systems, 91 (2016) 25-36

[10] A. Bharadwaj, O. El Sawy, P. Pavlou, N. Venkatraman, Digital business strategy: toward a next generation of insights, MIS Quarterly 37 (2) (2013) 471–482.

[11] E. Urban Jr., R. Boscolo, Using scientific meetings to enhance the development of early career scientists, Oceanography 26 (2) (2013) 164–170.

[12] T. Røssvoll, L. Fritsch, Trustworthy and Inclusive Identity Management for Applications in Social Media, Proceedings of Human-Computer Interaction, Users and Contexts of Use 15th International Conference, HCI International 2013, Lecture Notes in Computer Science Volume 8006 (2013) 68–77.

[13] S. Aral, C. Dellarocas, D. Godes, Introduction to the special issue-social media and business transformation: a framework for research, Information Systems Research 24 (1) (2013) 3–13.

[14] A. Coustasse, S. Chelsea, Potential benefits of using Facebook in the healthcare industry: a literature review, Insights to a Changing World Journal 2013 (1) (2013) 41–52.

[15] R. Davies, G. Cairncross, Student tourism and destination choice: exploring the influence of traditional, new, and social media: an Australian case study, Tourism Culture & Communication 13 (1) (2013) 29-42(14).

[16] N. M. Ahmed, L. Chen, An efficient algorithm for link prediction in temporal uncertain social networks, Information Science. 331, (2016) 120-136.

[17] Wang, Xi, and Gita Sukthankar. Link prediction in multi-relational collaboration networks. Proceedings of the 2013 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining. ACM, (2013).

[18] Matthias Bogaert, Michel Ballings, Dirk Van den Poel, The added value of Facebook friends data in event attendance prediction, Decision Support Systems, 82 (2016) 26-34

[19] N. M. A. Ibrahim，L. Chen, Link prediction in dynamic social networks by integrating different types of information, Applied Intelligence，42(4) ( 2015) 738-750.

[20] Buccafurri, G. Lax, A. Nocera, and D. Ursino. Discovering Missing Me Edges across Social Networks. Information Sciences. 319 (2015) 18-37.

[21] Chien Chin Chen, Shun-Yuan Shih, Meng Lee, Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems, 90 (2016) 33-45

[22] Hsiu-Yu Liao, Kuan-Yu Chen, Duen-Ren Liu, Virtual friend recommendations in virtual worlds, Decision Support Systems, 69 (2015) 59-69

[23] Qian Zhang, Dianshuang Wu, Jie Lu, Feng Liu, Guangquan Zhang, A cross-domain recommender system with consistent information transfer, Decision Support Systems, 104 (2017) 49-63

[24] Y. Sun, R. Barbery, M. Gupta, C. C. Aggarwal, J. Han, Co-Author Relationship Prediction in multi-relational Bibliographic Networks, Proceedings of 2011 International Conference on Advances in Social Networks Analysis and Mining, (ASONAM 2011). (2011) 121-128.

[25] Zan Huang, Daniel D. Zeng, A Link Prediction Approach to Anomalous Email Detection, 2006 IEEE International Conference on Systems, Man and Cybernetics, (2006) DOI: 10.1109/ICSMC.2006.384552

[26] D. Darcy, L. Ryan, Chawla N. V, multi-Relational Link Prediction in multi-relational Information Networks. Proceedings of 2011 International Conference on Advances in Socia Networks Analysis and Mining. (2011) 281-288.

[27] J. Chen, W. Geyer, C. Dugan, M. Muller, I. Guy, Make New Friends, But Keep the Old: Recommending People on Social Networking Sites, Proceedings of the 27th International Conference on Human Factors in Computing Systems (2009), pp. 201–210.

[28] Z. Huang, X. Li, H. Chen, Link Prediction Approach to Collaborative Filtering, Proceedings of the 5th ACM/IEEE-CS Joint Conference on Digital Libraries (2005), pp. 141–142.

[29] G. Jeh, J. Widom, SimRank: A Measure of Structural-Context Similarity, Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (2002), pp. 538–543.

[30] M.S. Granovetter, The strength of weak ties, American Journal of Sociology 1360–1380 (1973).

[31] Z. Yin, M. Gupta, T. Weninger, J. Han, A Unified Framework for Link Recommendation Using RandomWalks, International ConferenceonAdvancesinSocial Networks, Analysis and Mining (ASONAM), (2010), pp. 152–159.

[32] D. Eder, M.T. Hallinan, Sex differences in children's friendships, American Sociological Review 237–250 (1978).

[33] P.V. Marsden,Corediscussion networks of Americans, American Sociological Review 122–131 (1987).

[34] R.R. Huckfeldt, Citizens, Politics and Social Communication: Information and Influence in an Election Campaign, Cambridge University Press, (1995).

[35] Nikhita Vedula, Srinivasan Parthasarathy, Valerie L. Shalin, Predicting Trust Relations Within a Social Network: A Case Study on Emergency Response, WebSci '17: Proceedings of the 2017 ACM on Web Science Conference, (2017)

[36] Zhenkun Shi, Wanli Zuo, Weitong Chen, Lin Yue, Jiayu Han, Lizhou Feng, User Relation Prediction Based on Matrix Factorization and Hybrid Particle Swarm Optimization, WWW '17 Companion: Proceedings of the 26th International Conference on World Wide Web Companion, (2017 )1335-1341

[37] S. Lo, C. Lin, WMR–A Graph-Based Algorithm for Friend Recommendation, Proceedings of the 2006 IEEE/WIC/ACM International Conference on Web Intelligence, (2006).

[38] Zhou Zhang , Yuewen Liu, Wei Ding, Wei Huang, Qin Su, Ping Chen, Proposing a new friend recommendation method, FRUTAI, to enhance social media providers' performance, Decision Support Systems 79 (2015) 46–54

[39] Hui Fang, Guibing Guo, Jie Zhang, Multi-faceted trust and distrust prediction for recommender systems, Decision Support Systems, 71, (2015) 37-47

[40] W. Ahn, W. S. Jung, Accuracy test for link prediction in terms of similarity index: The case of WS and BA models, Physica A: Statistical Mechanics and its Applications. 429(1) (2015) 177-183.

[41] N. Barbieri, F. Bonchi, G. Manco, Who to follow and why: link prediction with explanations, Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining. (2014) 1266-1275.

[42] M. Pujari, R. Kanawati, Supervised Rank Aggregation Approach for Link Prediction in Complex Networks, WWW 2012 Companion. (2012) 1189-1196.

[43] Z. F. Bao, Y. Zeng, Y. C. Tay, sonL: social network link prediction by principal component regression, Proceedings of the 2013 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining. ( 2013).

[44] Y. L. He, James N.K. Liu, Yan-xing Hu, Xi-zhao Wang, OWA operator based link prediction ensemble for social network, Expert Systems with Applications. 42(1) (2015) 21-50.

[45] C. A. Bliss, M. R. Frank, C. M. Danforth, P. S. Dodds, An evolutionary algorithm approach to link prediction in dynamic social networks, Journal of Computational Science. 5(5) (2014) 750-764.

[46] E. Sherkat, M. Rahgozar，M. Asadpour，Structural link prediction based on ant colony approach in social networks. Physica A: Statistical Mechanics and its Applications，419(1) (2015) 80-94.

[47] B. L. Chen, L. Chen, B. Li, A fast algorithm for predicting links to nodes of interest. Information Science. 329 (2016) 552-567.

[48] Nahla Mohamed Ahmed, Ling Chen, Yulong Wang; Bin Li, Yun Li, and Wei Liu, DeepEye:Link prediction in dynamic networks based on non-negative matrix factorization, Big Data Mining and Analytics, 1(1)(2018) pp19– 33

[49] C.Y. Dai , L. Chen , B. Li , Y. Li , Link Prediction in multi-relational networks based on Relational Similarity, Information Sciences, 394–395 (2017) 198–216

[50] V. Stroele, G. Zimbrao, J. M. Souza, Group and link analysis of multi-relational scientific social networks, The Journal of Systems and Software. 86 (2013) 1819-1830.

[51] M. Berlingerio, M. Coscia, F. Giannotti, A. Monreale, D. Pedreschi, Foundations of Multidimensional Network Analysis. ASONAM (2011) 485-489.

[52] Cao, Bokai, Xiangnan Kong, and S. Yu Philip. Collective prediction of multiple types of links in heterogeneous information networks. Data Mining (ICDM), 2014 IEEE International Conference on. IEEE,(2014).

[53] Jeong, Hyun Ji, Kim Taeyeon, and Myoung Ho Kim. Link Prediction by Utilizing Correlations Between Link Types and Path Types in Heterogeneous Information Networks. International Conference on Data Mining and Big Data. Springer International Publishing, (2016)

[54] Zhang, Jiawei, Philip S. Yu, and Zhi-Hua Zhou. Meta-path based multi-network collective link prediction. Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, (2014)

[55] L. Armijo et al. Minimization of functions having Lipschitz continuous first partial derivatives. Pacific Journal of mathematics, (1966)16(1):1–3,

[56] Link Prediction Group, Social Networks, http://www.linkprediction.org/index.php/link/resource/data . Accessed in 12.09.2017

[57] Icahn School of Madicine at Mount Sinai, OMIN Gene-Disease Associations, http://amp.pharm.mssm.edu/Harmonizome/dataset/OMIM+Gene-Disease+Associations, Accessed in 10.10.2017

[58] NCAR, CGD’s Climate Section, http://www.cgd.ucar.edu/cas/catalog/climind/, Accessed in 11.10.2017

[59] L. Tang, H. Liu, J. P. Zhang, and Z. Nazeri. Community Evolution in Dynamic multi-Mode Networks, in Proceedings of the 14<sup>th</sup> ACM SIGKDD International Conference on Discovery and Data Mining (KDD’08), pp 677-685, August 24-27, (2008). Las Vegas, Neveda.

## Biographical Note for the Authors

Ling Chen, He is currently a professor in the Computer Science Department, Yangzhou University, China. His research interests include decision support system, data mining and computational intelligence.

Man Gao, She got her M.S. degree in computer science in Yangzhou University, China in 2016. Her research interests include decision support system, data mining and computational intelligence.

Bin Li, he got his Ph.D. degree in Computer Science in Nanjing University of Aeronautics and Astronautics, China in 2001. He is currently a professor in the Computer Science Department, Yangzhou University, China. His research interests include computational intelligence, decision support system and service computing.

Wei Liu, she got her Ph.D. degree in Computer Science in Nanjing University of Aeronautics and Astronautics, China in 2010. She is currently an associate professor in the Computer Science Department, Yangzhou University, China. Her research interests include decision support system and computational intelligence.

Bolun Chen, he got his Ph.D. degree in Computer Science in Nanjing University of Aeronautics and Astronautics, China in 2016. He is currently a lecturer in the Computer Science Department, Huaiyin Institute of Technology, Huaiyin, China. His research interests include decision support system and computational intelligence.

## Highlights

1. Present a link prediction based algorithm for detecting the potential relations in multi-relational social networks.

2. Propose a matrix completion based method to solve the link prediction in multi-relational networks.

3. Propose a method to solve the matrix completion by a reformulated max-norm constrained optimization.

4. Present a projected gradient optimization algorithm which is scalable to large scale datasets.

5. Experimental results show that the method presented can obtain higher quality results than other methods.
