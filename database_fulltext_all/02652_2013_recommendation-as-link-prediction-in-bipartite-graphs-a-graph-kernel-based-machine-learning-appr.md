---
otero_id: 2652
otero_key: "VNCWJJJM"
title: "Recommendation as link prediction in bipartite graphs: A graph kernel-based machine learning approach"
authors: "Xin Li; Hsinchun Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.019"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Recommendation as link prediction in bipartite graphs: A graph kernel-based machine learning approach

Xin Li <sup>a,</sup>⁎, Hsinchun Chen <sup>b</sup>

<sup>a</sup> Department of Information Systems, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong

<sup>b</sup> Department of MIS, University of Arizona, 1130 East Helen St., Rm. 430, Tucson, AZ, USA

## a r t i c l e i n f o

Article history: Received 23 August 2011 Received in revised form 21 June 2012 Accepted 18 September 2012 Available online 4 October 2012

Keywords: Recommender systems Kernel-based methods Link prediction Bipartite graph Collaborative <sup>fi</sup>ltering

## a b s t r a c t

Recommender systems have been widely adopted in online applications to suggest products, services, and contents to potential users. Collaborative <sup>fi</sup>ltering (CF) is a successful recommendation paradigm that employs transaction information to enrich user and item features for recommendation. By mapping transactions to a bipartite user– item interaction graph, a recommendation problem is converted into a link prediction problem, where the graph structure captures subtle information on relations between users and items. To take advantage of the structure of this graph, we propose a kernel-based recommendation approach and design a novel graph kernel that inspects customers and items (indirectly) related to the focal user–item pair as its context to predict whether there may be a link. In the graph kernel, we generate random walk paths starting from a focal user–item pair and de<sup>fi</sup>ne similarities between user–item pairs based on the random walk paths. We prove the validity of the kernel and apply it in a one-class classi<sup>fi</sup>cation framework for recommendation. We evaluate the proposed approach with three real-world datasets. Our proposed method outperforms state-of-the-art benchmark algorithms, particularly when recommending a large number of items. The experiments show the necessity of capturing user–item graph structure in recommendation.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Consumers nowadays have an increasing amount of experience with online recommender systems, such as when buying books from Amazon, borrowing movies from Net<sup>fl</sup>ix, or setting up friend circles on Facebook. Compared with search engines, recommender systems apply information <sup>fi</sup>ltering mechanisms that may lead users to items they are not aware of or cannot access using a keyword search. Well-designed recommender systems save users' time, improve customer satisfaction [29], and promote sales [12]. To better capture users' interests and make effective recommendations, it is necessary to combine multiple models [35] and make effective use of different types of data, such as user information, item information, and transaction information (business transactions, browsing activities, review activities, etc.) [32,49]. The collaborative <sup>fi</sup>ltering (CF) recommendation paradigm models users' collaborative behaviors re<sup>fl</sup>ected in transactions and cross-recommends products to users.There are generally two types of recommendation tasks, predicting purchase vs. predicting rating. Transaction/purchase is essentially an implicit and coarse rating on preferring an item [22]. Furthermore, it does not differentiate the statuses of “unknown” vs. “unlike.” Thus, the two tasks are quite different from each other according to their computational nature. In real-world e-commerce applications, there generally exists more transaction information than explicit rating information. In this research, we focus on the modeling and prediction of transactions.

Given a set of users U and a set of objects/items O, we represent transactions T between them as a user-object interaction graph G= (V, E), where $V = U \cup O { \mathrm { ~ a n d ~ } } E = \{ ( u , o ) \colon u \in U , o \in O , u \to o \in T \}$ . This is a bipartite graph since user nodes can connect only to item nodes and vice versa. Under this representation, recommendation is equivalent to link prediction between users and items based on the existing graph (of previous transactions). The graph representation reveals subtle relations between indirectly connected users and items. Several collaborative <sup>fi</sup>ltering heuristic algorithms have explored the structure of user–item interaction graphs to improve recommendation performance [27,70]. However, few learning-based methods explicitly utilize the graph in constructing effective personalized recommendation models. Existing learning-based recommendation algorithms usually rely on explicit feature extraction, which is dif<sup>fi</sup>cult to apply onto graph-structured data due to the requirements of superior computational capacity and extensive domain knowledge (to design features).

In this research, we propose a generic kernel-based machine learning approach of link prediction in bipartite graphs and apply it in recommender systems. We inspect nodes and links that are close to a focal user–item pair as its context to predict the possibility for the pair to interact, i.e., the possibility that the user may use/buy the item. We propose a novel graph kernel to capture the structure and user/item features in the context of focal user–item pairs and feed it into the one-class SVM algorithm to build the prediction model. We examine the validity and computational ef<sup>fi</sup>ciency of the graph kernel. We demonstrate the performance of this recommendation approach using three real-world datasets.

The paper is organized as follows. The second section reviews related studies on recommendation algorithms. The third section introduces the proposed graph kernel-based recommendation framework. The fourth section describes experiments on three real-world datasets and discusses the experimental results. The last section summarizes the <sup>fi</sup>ndings and proposes directions for future research.

## 2. Literature review

## 2.1. Recommendation algorithms

There have been several survey papers on recommender system studies [3,24]. In this research, we focus on the utilization of graph structure in the design of recommendation algorithms and review previous studies according to the feature types and computational techniques.

First, previous studies generally use two types of features in designing the recommendation algorithms: collective local features and graphrelated features.

Collective local features capture the collective characteristics of individual user/item information, such as a user's demographic characteristics, content of interest [32], item's speci<sup>fi</sup>cations, transaction contexts (environment, time, etc.), and temporal usage patterns (which re<sup>fl</sup>ect user's characteristics). Collective local features directly show differences between people and the products they bought. Thus, researchers design similarity measures to cross-recommend similar products among similar users [5]. Researchers also proposed several probabilistic latent variable models on users' usage/purchase histories that group users/items to (hidden) classes to estimate the probabilities of user–item interactions [21].

Graph-related features highlight interactions between related users/ items. By representing transactions using a user–item interaction graph, the subtle relations between indirectly connected users and items can be modeled by the graph structure. In light of the graph theory, topological characteristics of nodes on the graph were considered an indication of items' attractiveness and importance in the network, which can be used in recommendation [18]. Graph structure can be used to design similarity measures for cross-recommendation. The bipartite user–item graph can also be projected onto a unipartite user/item graph [70] to simplify the graph structure. Furthermore, some researchers construct graphs based on user/item similarities. Such arti<sup>fi</sup>cial graphs can help alleviate the data sparsity problem [8]. In Webpage recommendation applications, a Webpage browsing graph has been employed to capture user behaviors and interest in certain contents [62].

Second, previous recommendation algorithms generally include two types of computational techniques: heuristic (i.e., memory-based) algorithms and learning-based (model-based) algorithms.

Heuristic algorithms are designed based on rules/measures provided by domain experts. A widely adopted heuristic is to recommend the most popular items (according to number of sales) to users. User/item similarity-based cross-recommendation is also a type of heuristic, which relies on designing appropriate similarity measures. In previous research, several similarity measures have been proposed based on user/item features [32]and transactional characteristics [5]. The most popular measures were the Pearson correlation coef<sup>fi</sup>cient [52] and cosine-based similarity [55].

User/item similarities have been combined with the interaction graph structure to capture information in connected nodes for link prediction [36]. Liben-Nowell and Kleinberg [43] explored the algorithms that iteratively compare nodes and update node similarities to a global node similarity measure. Taking a graph view of transactions, several previous studies proposed using eigenvector-based node ranking algorithms to rank items for recommendation. These algorithms are in general similar to PageRank [18,19,23] and HITS [27], which model in<sup>fl</sup>uence of users and attractiveness of products based on the connectivity of the graph. Furthermore, Fouss et al. proposed that closer users and items on the interaction graph (as measured by conducting random walks between them) may have a higher probability of interacting [14,15]. Huang et al. [26] also conjectured that possible links should lead to some topological changes on the graph, such as on clustering coef<sup>fi</sup>cients.

Compared to heuristic algorithms, learning-based methods build models based on existing data instances. Several probabilistic models, such as probabilistic latent semantic analysis (PLSA) [21], have been proposed to learn from business transactions [50,67,68] to predict future purchases. It is a common practice for such models to design and capture hidden user classes according to purchase histories and use the classes to aid recommendation. Temporal information of user purchase histories can be captured with a maximum entropy model to better tackle the recommendation problem [28,48]. Other research has explored <sup>fi</sup>nding the most effective features in business transactions that can be fed into mature machine learning models to do recommendation. For example, the probabilistic relational model (PRM) [17,45] was utilized to make predictions based on product features [10]. The regression model has been used with product features [60] and user rating features [2] to make recommendations. The SVM algorithm was applied on product features [64] and transaction context features, such as time, weather, etc., [4,46] to examine the probability that a product will be selected by users.

Due to its success in a recent Net<sup>fl</sup>ix contest, the matrix factorization method has attracted signi<sup>fi</sup>cant interest. Matrix factorization assumes that each item and user can be characterized by a set of factors whose inner product is the user's rating of the item [35], which are essentially hidden groups of users and items. These factors can be learned by minimizing the estimation error using the stochastic gradient descent or alternating least squares methods. Variations of matrix factorization techniques have been explored for computational ef<sup>fi</sup>ciency and data characteristic concerns [16,34,47,53]. Notably, Hu et al. [22] have developed a method for matrix factorization on binary matrices, which better suits the purchase recommendation problem.

It is also possible to use graph-related features in the learning-based paradigm. Huang et al. [25] extended the PRM framework and de<sup>fi</sup>ned rules to extract features on connected nodes in the user–item interaction graph to construct recommendation models. Yajima [65] used a Laplacian kernel to capture the positional relations among nodes on the graph and built one-class SVM models for each user to recommend items that are positionally closer to their previously bought items. Under an unsupervised learning paradigm, Reddy et al. [51] proposed to use a graph-based clustering algorithm to group similar users on the user–item graphs. The user groups help recommendation. Table 1 summarizes major research on recommendation algorithms. In general, a signi<sup>fi</sup>cant amount of effort focused on learning-based models using collective local features. Several studies explored the use of graph features in heuristics. There are limited studies using learning-based models on explicit graph data representations.

## 2.2. Link prediction in graphs

Using graph representations, a recommendation problem can be converted to a link prediction problem, which is an active research area in computer science. To our best knowledge, most link prediction research focused on unipartite networks, such as social networks, Webpages, and email networks. However, the recommendation problem is on bipartite networks.

In link prediction research, several heuristics have been proposed. For example, sociologists identi<sup>fi</sup>ed a strong homophily phenomenon in friendships [44]. This rationale led to a heuristic that uses actor similarity to infer social links. Liben-Nowell and Kleinberg [43] adopted and proposed several graph-based similarity measures for social network link prediction. Acar et al. [1] applied matrix factorization on one such measure, the Katz measure, to improve link prediction performance. In graph theory, the preferential attachment model for network evolution [6] can be used for link prediction, which predicts that high degree nodes will have higher probability to initiate new links.

Table 1  
A summary of previous recommendation algorithm studies.

<table><tr><td>Study</td><td>Featurea</td><td>Techniqueb</td><td>Notes</td></tr><tr><td>Resnick et al. 1994 [52]</td><td>L</td><td>H</td><td>Similarity-based</td></tr><tr><td>Sarwar et al. 2001 [55]</td><td>L</td><td>H</td><td></td></tr><tr><td>Ahn 2008 [5]</td><td>L</td><td>H</td><td></td></tr><tr><td>Kim et al. 2011 [32]</td><td>L</td><td>H</td><td></td></tr><tr><td>Huang et al. 2004 [23]</td><td>G</td><td>H</td><td>Eigenvector-based node ranking</td></tr><tr><td>Griffith et al. 2006 [19]</td><td>G</td><td>H</td><td></td></tr><tr><td>Gori and Pucci 2007 [18]</td><td>G</td><td>H</td><td></td></tr><tr><td>Huang et al. 2007 [27]</td><td>G</td><td>H</td><td></td></tr><tr><td>Zhou et al. 2007 [70]</td><td>G</td><td>H</td><td></td></tr><tr><td>Fouss et al. 2007 [15]</td><td>G</td><td>H</td><td>Node position-based</td></tr><tr><td>Fouss et al. 2012 [14]</td><td>G</td><td>H</td><td></td></tr><tr><td>Huang et al. 2007 [26]</td><td>G</td><td>H</td><td>Clustering coefficient-based</td></tr><tr><td>Hofmann 2004 [21]</td><td>L</td><td>L</td><td>Probabilistic model</td></tr><tr><td>Yu et al. 2004 [67]</td><td>L</td><td>L</td><td></td></tr><tr><td>Zeng et al. 2004 [68]</td><td>L</td><td>L</td><td></td></tr><tr><td>Polcicova and Tino 2004 [50]</td><td>L</td><td>L</td><td></td></tr><tr><td>Iwata et al. 2008 [28]</td><td>L</td><td>L</td><td></td></tr><tr><td>Getoor and Sahami 1999 [17]</td><td>L</td><td>L</td><td>Machine learning model + local features</td></tr><tr><td>Newton and Greiner 2004 [45]</td><td>L</td><td>L</td><td></td></tr><tr><td>Vucetic and Obradovic 2005 [60]</td><td>L</td><td>L</td><td></td></tr><tr><td>Adomavicius and Tuzhilin 2005 [3]</td><td>L</td><td>L</td><td></td></tr><tr><td>Xu and Araki 2006 [64]</td><td>L</td><td>L</td><td></td></tr><tr><td>Adomavicius and Tuzhilin 2011 [4]</td><td>L</td><td>L</td><td></td></tr><tr><td>Funk 2006 [16]</td><td>L</td><td>L</td><td>Matrix factorization</td></tr><tr><td>Paterek 2007 [47]</td><td>L</td><td>L</td><td></td></tr><tr><td>Salakhutdinov and Mnih 2008 [53]</td><td>L</td><td>L</td><td></td></tr><tr><td>Koren 2008 [34]</td><td>L</td><td>L</td><td></td></tr><tr><td>Hu et al. 2008 [22]</td><td>L</td><td>L</td><td></td></tr><tr><td>Koren et al. 2009 [35]</td><td>L</td><td>L</td><td></td></tr><tr><td>Huang et al. 2004 [25]</td><td>G</td><td>L</td><td>PRM + aggregative features</td></tr><tr><td>Yajima 2006 [65]</td><td>G</td><td>L</td><td>One-class SVM + Laplacian kernel</td></tr><tr><td>Reddy et al. 2002 [51]</td><td>G</td><td>L</td><td>Graph-based clustering</td></tr></table>

<sup>a</sup> L — collective local features; G — graph-related features.  
<sup>b</sup> H — heuristic methods; L — learning-based methods

Model-based methods have also been used in link prediction. The Markov chain model has been used to explore user navigation history for Webpage link prediction [54,71]. Cohn et al. [13] applied the PLSA algorithm on Webpage contents and hyperlinks for hyperlink prediction. As an extension of the PRM model, Taskar et al. [59] proposed the use of the Relational Markov Network (RMN) on link prediction. Hasan et al. [20] proposed a supervised learning framework that considers node proximity features, aggregated linkage features, and topological features for link prediction, which is also applied in [7]. Such a method can also be utilized in the recommendation problem. Wang et al. [61] adopted a logistic regression model and used topological and content-based similarity measures to predict co-authorship relations. Yu and Chu [66] adopted the Gaussian process approach and decompose link similarities to node-wise linear kernels to build a link prediction model. Kashima et al. [31] and Scripps et al. [57] took an optimization approach to assign same-link labels to links with similar node characteristics.

## 2.3. Kernel-based machine learning methods and graph kernels

In general, it is dif<sup>fi</sup>cult to de<sup>fi</sup>ne features on the complicated structure of graphs. As an alternative machine learning framework, kernel-based machine learning provides a systematic way to deal with this problem. Compared to traditional feature-based methods, kernel-based methods do not require explicit feature generation. A kernel-based method relies on a kernel function that de<sup>fi</sup>nes a similarity measure between data instances, $k { : } \chi \times \chi \to R .$ The kernel function maps data from the input space χ to a feature space H (named reproducing kernel Hilbert space, RKHS), $\phi ( x ) { : } \chi \to H ,$ where the mapping function Φ(x) is not explicitly de<sup>fi</sup>ned and meets the condition $k ( x , x ^ { \prime } ) { = } { < } \phi ( x )$ Φ(x′)>. A kernel-based method also need a kernel machine, which is an algorithm that needs only kernel function values to learn patterns of the data instances in the feature space H. There are only limited kernel machines, such as Support Vector Machines (SVM), one-class SVM, kernel Fisher discriminant (KFD), and Support Vector Data Description (SVDD). However, given the different characteristics of applications, the performance of kernel-based methods is highly dependent on the selection and design of kernel functions [58].

In graph-structured data, graph kernels, including the Laplacian kernel [65], diffusion kernels [33], commute time kernel [14], and marginalized kernel [30], are designed to capture features of graphs. They have been widely used in bioinformatics studies on gene interaction networks or protein interaction networks. Previously, graph kernels have been applied on graph classi<sup>fi</sup>cation (to classify protein functions according to their molecular structures) [9,39]. In these models, graphs are generally decomposed into their sub-structures, such as nodes, links, and random walk paths. Graph similarities are thus de<sup>fi</sup>ned by aggregating the sub-structures' similarities. By representing nodes on the graph with sub-graphs close to them, graph kernels have also been generalized to node classi<sup>fi</sup>cation (to classify patents according to citation networks) [40].

There are studies that simply use kernels as node similarity values in a heuristic paradigm to cross-recommend products to users. For example, Kunegis built graph kernels as linear, polynomial, and exponential combinations of a graph adjacency matrix and Laplacian matrix [37,38] and then employed the kernel values to indicate the possibilities of a link between node pairs. However, studies on graph kernels in a machine learning scheme for link prediction are still limited.

## 2.4. Highlights

The three streams of literature together shed light on the potential directions to improve product recommendation models. First, learningbased methods are one active approach in this area. As compared with heuristics, this approach generally has more stable performances across different datasets (and requires more computational power). As a link prediction problem, recommendation deals with (the matching of) node pairs on a network. Thus, a straightforward approach is to compile local features from pairs of nodes and employ mature machine learning algorithms to classify whether they may interact. In co-authorship link prediction, authors' publication status, their common keywords, and distances between authors in a network have been used as user features [20]. In a recommendation task, product features, such as textual features on product descriptions, have been employed [64].

While the use of local features currently dominates learning-based recommendation algorithms, the explorations of graph features in heuristics show the potential of using graph features in a learning-based framework. Kernel-based methods and graph kernels enabled such a direction. Yajima [65] provides a basic example of this approach, which uses a Laplacian kernel to capture node similarities that are related to distances between nodes. Under a one-class SVM algorithm, positionally closer users and items are more likely to be predicted to interact. In recommendation, several graph kernels have also been used under a rule-based framework (where the model is not trained from data) [15]. Many of these kernels take a similar idea of node closeness. They usually estimate distances between nodes through commute time or transition probabilities of random walks. One obvious limitation of such a kernel design is that it can only work with nodes that are (indirectly) connected. For more effective use of the kernel-based machine learning paradigm, it is necessary to carefully design and select appropriate kernels for recommendation.

Previous studies have provided many successful examples of the design of graph kernels. One effective approach is to inspect structural commonality of different parts of a network with the help of previous graph comparison kernels. For example, in patent classi<sup>fi</sup>cation [40], a node (patent) was accompanied by its two-level neighbors as a sub-graph and classi<sup>fi</sup>ed together into different categories. To compare such neighborhoods, the study decomposed sub-graphs into random walk paths and conducted pairwise comparisons of random walks paths. In this design, random walks are not used as a distance measure but simply to represent sub-structures of graphs. Such a design highlights the interdependency between nodes in a graph. However, to use similar design principles in recommendation, signi<sup>fi</sup>cant effort must be put into re-designing the kernel.

In short, to <sup>fi</sup>ll the research gap of limited learning-based methods on graph-related features in recommendation, we take a kernel-based approach [65] and develop graph kernels for modeling. Different from the designs based on node distance [15], we explore structural commonality between different parts of a network [40] in the kernel design. We aim to contribute to the design of an effective graph kernel that suits the requirement of the recommendation task.

## 3. Methodology

In recommendation, the task is to estimate the probability that user u and item o will interact. Here, we inspect the users and items close to u and o on the graph and consider these as the context to judge the relationship between u and o. We conjecture that user– item pairs with a topologically similar context may have a similar probability to have (or not have) an interaction. Based on their context characteristics, we can classify user–item pairs into two groups (positive and negative). The major task in this process is to design a graph kernel comparing contexts of user–item pairs.

## 3.1. A graph kernel-based recommendation framework

Fig. 1 shows the four steps in our graph kernel-based framework. 1) In the graph and feature extraction step, we construct the user–item graph from transaction histories. We also extract features describing nodes (users and items) from the data. 2) In the graph kernel construction step, we design a kernel k() on user–item pairs based on their context structure and features. In kernel-based methods, the kernel design is the most essential module for prediction. 3) In the model building step, a classi<sup>fi</sup>er is built to separate potential links from impossible links. In the recommendation task we investigate, all known data instances are the transactions or interactions that have happened. We cannot differentiate whether unhappened transactions are negative data instances or transactions that will happen in the future. Thus, we take a one-class SVM algorithm [56] which looks for a hyper-plane to separate positive data instances from the origin of RKHS to deal with this task. As shown in Fig. 1, the points represent data instances and the line represents the hyper-plane. In this model, the data instances on the same side of origin as the hyper-plane are predicted to be negative (i.e., impossible to exist), and those on the opposite side of origin from the hyper-plane are predicted to be positive. In previous research, two-class classi<sup>fi</sup>cation was also applied [25], where unhappened transactions are sampled and considered as negative instances. However, the sampling process in this practical approach lacks sound theoretical justi<sup>fi</sup>cation. Thus, we choose the one-class classi<sup>fi</sup>cation method in this study. 4) In the prediction step, we rank items for each user according to predicted con<sup>fi</sup>dences of user–item interactions (so that we can provide top N recommendations). To make such a ranking, we use the Euclidean distance from data instances (i.e., user–item pairs) to the classi<sup>fi</sup>cation hyper-plane as the estimated con<sup>fi</sup>dence, where data instances farther from the hyperplane (on the side opposite of the origin) have higher probability to occur. Given all support vectors $\left\{ { \overline { { u _ { 1 } o _ { 1 } } } } ^ { \prime } { \overline { { , u _ { 2 } o _ { 2 } } } } , \ldots \right\}$ identi<sup>fi</sup>ed by the <sup>f g</sup>one-class SVM classi<sup>fi</sup>er, the con<sup>fi</sup>dence score of an instance uo is calculated as: $\begin{array} { r } { f ( \overline { { u o } } ) = \sum _ { i } a _ { i } k ( \overline { { u o } } , \overline { { u _ { i } o _ { i } } } ) + b , } \end{array}$ where a and b are estimated by the SVM algorithm. Such a measure is proportional to several classi<sup>fi</sup>cation con<sup>fi</sup>dence probability estimation measures for SVM [63]. Since we only care about ranks of items in recommendation, the measure is suf<sup>fi</sup>- cient for this research.

## 3.2. Graph kernel design

Our designed kernel measures similarities of user–item pairs based on their related nodes/links, which utilizes the structure of the user– item graph. To capture the structural features, we generate random walk paths on the user–item graph as a simpli<sup>fi</sup>ed representation of the focal user–item pair's context. Since we work on a link prediction task, we use only the random walk paths starting from the focal user– item pair to other parts of the graph, which is a major difference between our design and previous research [9,40]. Fig. 2a shows an example context of a user–item pairuo. In Fig. 2b, we present a transformed representation to show how to generate random walks from u and o. (Some nodes are presented more than once for explanation.) Examples of the random walk paths are shown in Fig. 2c.

![](/api/attachments/VNCWJJJM/fulltext/images/78c0d0309a4e219dd9368036135275d0f6f58c3ad5aeedec6ee4f019c4a673c4.jpg)  
Fig. 1. A graph kernel-based recommendation framework.

![](/api/attachments/VNCWJJJM/fulltext/images/777b4e57c83897bedd50605e4bcb1e928c7c8b8acf2a02043c5143e9c482ce68.jpg)  
a) The context of user u and item o  
b) A transformed representation of the context  
Fig. 2. Context of a user–item pair.  
c) Example random walks

Given a focal user–item pair uo, a generated random walk path h on the pair can be represented as a sequence: $h { = } n _ { x } ^ { u } {  } { \cdots } n _ { 2 } ^ { u } {  } n _ { 1 } ^ { u } {  } u -$ $o \to n _ { 1 } ^ { o } \to n _ { 2 } ^ { o } \dots \to n _ { y } ^ { o }$ , where $n _ { i } ^ { u } ( i { = } 1 \ \mathrm { t o } x )$ and $n _ { i } ^ { o } ( i { = } 1 \mathrm { t o } y )$ are the mixture of user and item nodes on the u and o side of the path, respectively. (u and o can also be represented as n<sup>u</sup> and n<sup>o</sup>). The random walks connect the focal user–item pair to related users/items. In this research, we utilize only the random walk paths within a certain length to focus on the most relevant nodes. Features from such nodes are accumulated for the focal user–item pair's prediction. The generated random walks are associated with a probability of occurrence. Assuming the random walks jump from one node to its neighbors (or stop) with a transit probability $p _ { t }$ (or stop probability $p _ { s } )$ , the path h has a probability of occurrence:

$$
\begin{array}{c} P (h | G) = p _ {s} \big (n _ {x} ^ {u} \big) p _ {t} \big (n _ {x} ^ {u} | n _ {x - 1} ^ {u} \big) \dots p _ {t} \big (n _ {2} ^ {u} | n _ {1} ^ {u} \big) p _ {t} \big (n _ {1} ^ {u} | u \big) p _ {t} \big (n _ {1} ^ {o} | o \big) p _ {t} \big (n _ {2} ^ {o} | n _ {1} ^ {o} \big) \\ \dots p _ {t} \Big (n _ {y} ^ {o} \Big | n _ {y - 1} ^ {o} \Big) p _ {s} \Big (n _ {y} ^ {o} \Big). \end{array}
$$

Based on all generated random walk paths, we de<sup>fi</sup>ne the graph kernel, i.e., similarities of user–item pairs, as the sum of pairwise similarities between their related random walk paths weighted by the paths' probability of occurrence: $k _ { g } ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) = \sum _ { \overline { { u o } } \subset h \overline { { u ^ { \prime } o ^ { \prime } } } \subset h ^ { \prime } }$ $\left[ k _ { p a t h } \left( h , h ^ { \prime } \right) P ( h | G ) P ( h ^ { \prime } | G ) \right]$ , where $k _ { p a t h } ( h , h ^ { \prime } )$ is the similarity between random walk paths. Generally speaking, the probability of occurrence re<sup>fl</sup>ects the strength of connections between the focal user–item pair and other users and items on the path. The nodes farther from focal user–item pairs will be involved with fewer and longer random walk paths and have smaller weight and impact on the focal user– item's link prediction.

To assess $k _ { p a t h } ( h , h ^ { \prime } )$ , we decompose the paths and compare their matching nodes and links according to their sequence. In this process, we always match focal user–item pairs between random walk paths. If two random walk paths do not have a one-to-one mapping after matching their focal user–item pairs (for example, without an equal length), we simply deem their similarity as 0. Otherwise, we de<sup>fi</sup>ne

$$
\begin{array}{c} k _ {p a t h} (h, h ^ {\prime}) = k _ {n o d e} (n _ {x} ^ {u}, n _ {x} ^ {u}) \times k _ {n o d e} (n _ {x - 1} ^ {u}, n _ {x - 1} ^ {u}) \times \ldots \times k _ {n o d e} (u, u ^ {\prime}) \\ \times k _ {n o d e} (o, o ^ {\prime}) \times \ldots \times k _ {n o d e} (n _ {y - 1} ^ {o}, n _ {y - 1} ^ {o}) \times k _ {n o d e} (n _ {y} ^ {o}, n _ {y} ^ {o}), \end{array}
$$

where $k _ { n o d e } ( )$ is the similarity (kernel) between nodes. (Link features can also be used to assess random walk path similarities. However, most applications have limited features on interactions. Thus, we focus on node features in this research.)

Node similarity, $k _ { n o d e } ( )$ , should be de<sup>fi</sup>ned based on user/item features according to application and domain knowledge. It should be noted that the appropriate node features may vary across applications and interfere with graph structure. We leave the systematic exploration of effective node features to future research. In general, the selection of such features should highlight the factors that re<sup>fl</sup>ect/affect users' decisions, such as user age, education level, product category, etc. The representation of such features in a kernel form depends on characteristics of data; for example, a linear kernel can be applied on categorical data or textual data, and a Radial Basis Function (RBF) kernel can be applied on numerical data.

Finally, we normalize the graph kernel, which in general leads to a better prediction performance: $k ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) = k _ { g } ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) /$ $\sqrt { k _ { g } ( \overline { { u o } } , \overline { { u o } } ) } k _ { g } ( \overline { { u ^ { \prime } o ^ { \prime } } } , \overline { { u ^ { \prime } o ^ { \prime } } } )$

## 3.3. Graph kernel characteristics

Computing the graph kernel by enumerating all random walk paths is computationally expensive. We therefore introduce a matrix formulation of the graph kernel calculation. For ease of discussion, we assume the adjacency matrix of the user–item interaction graph is $A = \{ A _ { i , j } \}$ . The transition probability matrix is $M = \{ M _ { i , j } \} = \{ p _ { t } ( j | i ) \}$ and the stopping probability matrix is $Q = \{ Q _ { i , j } \} = \{ p _ { s } ( j ) \}$

Proposition 1. The graph kernel K can be decomposed to the product of two random walk kernels starting from the user and item of focal user–item pairs.

Proof: Before normalization

$$
\begin{aligned} & k_{g}(\overline{uo},\overline{u^{\prime}o^{\prime}}) = \sum_{uo\subset h}\sum_{u^{\prime}o^{\prime}\subset h^{\prime}}\Bigl [k_{path}(h,h^{\prime})P(h|G)P(h^{\prime}|G)\Bigr ]\\ & = \sum_{\substack{\overline{uo}\subset h,u^{\prime}o^{\prime}\subset h^{\prime}:\\ h\text{matches} h^{\prime}}}\Biggl [\prod_{i = 1}^{x}k_{node}(n_{i}^{u},n_{i}^{u})\times k_{node}(u,u^{\prime})\times k_{node}(o,o^{\prime})\\ & \quad \times \prod_{i = 1}^{y}k_{node}(n_{i}^{o},n_{i}^{o})\times p_{s}(n_{x}^{u})\times \left(\prod_{i = 1}^{x}p_{t}(n_{i}^{u}|n_{i - 1}^{u})\right)\times \left(\prod_{i = 1}^{y}p_{t}(n_{i}^{o}|n_{i - 1}^{o})\right)\times p_{s}(n_{y}^{o})\\ & \quad \times p_{s}(n_{y}^{u^{\prime}})\times \left(\prod_{i = 1}^{x}p_{t}(n_{i}^{u}|n_{i - 1}^{u})\right)\times \left(\prod_{i = 1}^{y}p_{t}(n_{i}^{o}|n_{i - 1}^{o})\right)\times p_{s}(n_{y}^{o^{\prime}})\Biggr ]\\ & = \sum_{\substack{\overline{uo}\subset h,u^{\prime}o^{\prime}\subset h^{\prime}:\\ h\text{matches} h^{\prime}}} \Biggl [\prod_{i = 1}^{x}k_{node}(n_{i}^{u},n_{i}^{u})\times k_{node}(u,u^{\prime})\times p_{s}(n_{x}^{u})\times \prod_{i = 1}^{x}p_{t}(n_{i}^{u}|n_{i - 1}^{u})\times p_{s}(n_{x^{\prime}}^{u^{\prime}})\\ & \quad \times \prod_{i = 1}^{x}p_{t}(n_{i^{\prime}}^{u^{\prime}}|n_{i - 1^{\prime}}^{u})\times k_{node}(o,o^{\prime})\times \prod_{i = 1}^{y}k_{node}(n_{i}^{o},n_{i^{\prime}}^{o^{\prime}})\times \prod_{i = 1}^{y}p_{t}(n_{i}^{o}|n_{i - 1}^{o}).\\ & \quad \times p_{s}(n_{y}^{o})\times \prod_{i = 1}^{y}p_{t}(n_{i^{\prime}}^{o^{\prime}}|n_{i - 1^{\prime}}^{o})\times p_{s}(n_{y^{\prime}}^{o^{\prime}})\Biggr ]. \end{aligned}
$$

We de<sup>fi</sup>ne $h _ { u } = u \to n _ { 1 } ^ { u } \to n _ { 2 } ^ { u } \dots \to n _ { x } ^ { u }$ and $h _ { o } = o \to n _ { 1 } ^ { o } \to n _ { 2 } ^ { o } \dots \to n _ { y } ^ { o }$ which are the random walk paths starting from u and o, respectively. $k _ { g } ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } )$

$$
= \sum_ {h _ {u}, h _ {u} ^ {\prime}, h _ {o}, h _ {o} ^ {\prime}} \left[ k _ {p a t h} (h _ {u}, h _ {u} ^ {\prime}) P (h _ {u} | G) P (h _ {u} ^ {\prime} | G) \times k _ {p a t h} (h _ {o}, h _ {o} ^ {\prime}) P (h _ {o} | G) P (h _ {o} ^ {\prime} | G) \right]
$$

$$
= \sum_ {h _ {u}; h _ {u} ^ {\prime}} \left[ k _ {p a t h} (h _ {u}, h _ {u} ^ {\prime}) P (h _ {u} | G) P (h _ {u} ^ {\prime} | G) \right] \times \sum_ {h _ {o}; h _ {o} ^ {\prime}} \left[ k _ {p a t h} (h _ {o}, h _ {o} ^ {\prime}) P (h _ {o} | G) P (h _ {o} ^ {\prime} | G) \right].
$$

We de<sup>fi</sup>n $\mathsf { \Omega } _ { \ast } ^ { \ast } k _ { h a l f } ( u , u ^ { \prime } ) = \sum _ { h _ { u } ; h _ { u } ^ { \prime } . } \big [ k _ { p a t h } \big ( h _ { u } , h _ { u } ^ { \prime } \big ) P \big ( h _ { u } | G \big ) P \big ( h _ { u } ^ { \prime } | G \big ) \big ]$ 0u

We can then get $k _ { g } ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) = k _ { h a l f } ( u , u ^ { \prime } ) k _ { h a l f } ( o , o ^ { \prime } ) .$

<sup>ð Þ ¼ ð Þ ð Þ</sup>It can be easily shown that the normalized graph kernel k() can be represented as the product of normalized $k _ { h a l f } ( )$ , which can be represented as $k _ { h a l f \_ n o r m } ( ) . \varTheta$

$k _ { h a l f }$ is identical to the context graph kernel in [41] that was used in a node classi<sup>fi</sup>cation problem. The kernel matrix $K _ { h a l f } = \{ k _ { h a l f } ( \mathbf { \theta } ) \}$ can be represented as:

$$
K _ {h a l f} = \sum_ {i = 1} ^ {l} K _ {i}, \quad K _ {1} = (M ^ {*} Q) K _ {n o d e} (M ^ {*} Q) ^ {\mathrm{T}}, \quad K _ {i + 1} = M (K _ {n o d e} ^ {*} K _ {i}) M ^ {\mathrm{T}},
$$

where $K _ { n o d e } = \{ k _ { n o d e } ( ) \} ,$ l is the maximum length of random walk paths considered, and operation \* is the Hadamard product (i.e., entrywise product). In this formulation, each matrix $K _ { i }$ covers the random walk paths of length=i and the features from nodes that are i step(s) away from the starting user (or item). It was proved that this matrix formula converges when n goes to ∞ given a uniform stopping probability $p _ { s }$ or a $p _ { s }$ larger than 0.5 [41].

Proposition 2. The calculation of graph kernel K can be finished in O(l| $U | ^ { 2 } | O | )$ or O(l|U||O|<sup>2</sup>) time, whichever is in a larger scale, where |U| is the number of users and |O| is the number of items.

Proof: Since the user–item interaction graph is a bipartite graph, the adjacency matrix A and the transition probability matrix M take the form of $\left( \begin{array} { c c } { { 0 } } & { { X ^ { \prime } } } \\ { { X } } & { { 0 } } \end{array} \right)$ , where X and X′ indicate non-zero elements (without loss of generality, we assume user nodes are put in front of item nodes in these matrices). The kernel matrices, such as $K _ { n o d e } ,$ $K _ { i } ,$ take the form of $\left( \begin{array} { c c } { { Y } } & { { 0 } } \\ { { 0 } } & { { Y ^ { \prime } } } \end{array} \right)$ , where Y and Y′ indicate non-zero elements, since a user and an item do not have matched random walk paths or features and are not directly comparable. In the decomposed form of $K _ { h a l f } ,$ the matrix multiplication operation in calculating $K _ { i }$ can be simpli<sup>fi</sup>ed to the multiplication of non-zero sub-matrices. In a naive algorithm, it takes $0 ( \bar { 2 } | U | ^ { 2 } | O | + 2 | U | | O | ^ { 2 } )$ time to <sup>fi</sup>nish. Furthermore, calculating $K _ { i }$ also needs O(2|U||O|) or $0 ( | U | ^ { 2 } + | O | ^ { 2 } )$ time for the Hadamard product operation. Thus, to calculate $K _ { h a l f }$ takes at most $0 ( l | U | ^ { 2 } | O | )$ or $0 ( l | U | | O | ^ { 2 } )$ time, whichever is in a larger scale. Calculating K from $K _ { h a l f }$ takes another Hadamard product for $0 ( [ | U | + | O | ] ^ { 2 } )$ time. Overall, the calculation of K can be <sup>fi</sup>nished in $0 ( l | U | ^ { 2 } | O | )$ or O(l|U||O|<sup>2</sup>) time. If appropriate numerical techniques are applied, the exponent may be further reduced. □

It should be noted that according to previous network analysis studies, l can be a small number to cover a large network. Thus, it can be considered as a constant scale in real applications.

Proposition 3. The graph kernel K is positive semi-de<sup>fi</sup>nite and thus a valid kernel.

Proof: Since $K _ { n o d e }$ is a selected valid kernel, for any vector $\alpha \in R ^ { | U | + | O | } ,$ $\alpha K _ { n o d e } \alpha ^ { T } 2 0$ . For any vector $\alpha \in R ^ { | U | + | O | }$ , αK $\scriptstyle 1 \alpha ^ { T } =$ $\alpha ( M * Q ) K _ { n o d e } [ \alpha \ ( M * Q ) ] ^ { \mathrm { T } }$ . Considering $\alpha ( M * Q )$ is a vector∈ $R ^ { \left| U \right| + \left| O \right| } ,$ αK ${ \mathrm { \Omega } } _ { l } \alpha ^ { T } { \ge } 0 .$ . Thus, $K _ { 1 }$ is a valid kernel. Since the Hadamard product is entrywise multiplication, according to the closure properties of kernel functions, $K _ { n o d e ^ { * } } K _ { 1 }$ is a valid kernel. By applying these two rules iteratively, it is easy to prove $K _ { i + 1 } = M ( K _ { n o d e ^ { * } } K _ { i } ) M ^ { \mathrm { I } }$ is a series of valid kernels. The sum of these kernels, $K _ { h a l f } ,$ is also a valid kernel. $K _ { g }$ is the tensor product of two valid $K _ { h a l f }$ kernels and is positive semi-de<sup>fi</sup>nite. Last, normalization on $K _ { g }$ does not change the validity of the kernel function. Thus, K is positive semi-de<sup>fi</sup>nite and a valid kernel. □

In our proposed framework, the Euclidean distance between a data instance (i.e., user–item pair) and the classi<sup>fi</sup>cation hyperplane built by one-class SVM is used as the con<sup>fi</sup>dence score to predict the probability of the user–item's interaction. Given support vectors u o ; u o ; … identi<sup>fi</sup>ed by the one-class SVM, this con<sup>fi</sup>dence score is: $\begin{array} { r } { f ( \overline { { u o } } ) = \sum _ { i } a _ { i } k ( \overline { { u o } } , \overline { { u _ { i } o _ { i } } } ) + b , } \end{array}$ where $a _ { i }$ and b are parameters estimated by SVM. Since $k ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) = k _ { h a l f _ { n } o r m } ( u , u ^ { \prime } )$ $\begin{array} { r } { k _ { h a l f _ { n } o r m } ( o , o ^ { \prime } ) , \ f ( \overline { { u o } } ) = \sum _ { \ast } a _ { i } k _ { h a l f _ { n } o r m } ( u , u _ { i } ) k _ { h a l f _ { n } o r m } ( o , o _ { j } ) + b . } \end{array}$ . In recommendation, we always compare different products for individual customers. Thus $a _ { i } k _ { h a l f \_ n o r m } ( u , u _ { i } )$ does not change for each user in each recommendation. The rank of items depends on their similarities with items in the support vectors $k _ { h a l f \_ n o r m } ( o , \boldsymbol { o } _ { i } )$ . The difference between users is captured by $a _ { i } k _ { h a l f \_ n o r m } ( u , u _ { i } )$ , in which the importance of each support vector is moderated by their similarity to the focal user $k _ { h a l f \_ n o r m } ( u , u _ { i } )$ . Since $k _ { h a l f \_ n o r m } ( )$ depends on both node (local) features and graph structure, our proposed recommendation model <sup>fi</sup>nds representative reference users with similar contexts to the focal user and makes recommendations according to reference users' previous purchases.

## 4. Experimental study

## 4.1. Datasets

In order to show the algorithms' performance on different data characteristics, we use three datasets from quite different application settings to evaluate the proposed framework.

An online book retail dataset obtained from a major Chinese online bookstore in Taiwan [26]. The dataset includes 5 years of transactions of 2000 randomly selected users, involving 9695 books and 18,771 transactions.

An online clothing retail dataset provided by a leading U.S. online clothing merchant [27]. The dataset includes 16 million online transactions from a 3-month period, involving 4 million households and 128,000 items.

A book rating dataset collected from the Book-Crossing community [72]. The dataset reports 278,858 users' 1,149,780 ratings on 271,379 books. Since this research focuses on exploiting transaction information, we treat each rating as a transaction by assuming that a user buys a book before reading and rating it.

For meaningful testing, we include only users with 5 to 100 transactions. This constraint results in 851 users for the book retail dataset. For comparison purposes, we sample 1000 users with 5 to 100 items from the other two datasets. Table 2 reports the descriptive statistics of the reduced datasets. The two sampled book datasets show closer average purchases per user while the sampled clothing dataset and the book rating dataset have closer numbers of sales per item. Overall, the sampled book retail dataset is much denser than the other two. The reduced datasets were split into 80% training data and 20% testing data according to transaction time. Items that appeared only in the testing data, which cannot be predicted by any algorithm, are removed from the study.

## 4.2. Evaluation metrics

In the task of predicting transactions/purchases, the RMSE measure for rating prediction evaluation cannot be applied. To evaluate recommendation performance, we have each algorithm generate a ranked list of items for each user and compare the recommendations with actual transactions in the testing data using three types of measures.

Table 2 Dataset statistics.

<table><tr><td>Dataset</td><td># of users</td><td># of items</td><td># of transactions</td><td>Avg. purchases/user</td><td>Avg. sales/ item</td></tr><tr><td>Book retail</td><td>851 (~2000)</td><td>8566 (~9700)</td><td>13,902 (~18,000)</td><td>16.34 (~9)</td><td>1.62 (~1.86)</td></tr><tr><td>Clothing retail</td><td>1000 (~4 million)</td><td>7328 (~128,000)</td><td>9332 (~16 million)</td><td>9.33 (~4)</td><td>1.27 (~125)</td></tr><tr><td>Book rating</td><td>1000 (~280,000)</td><td>15,578 (~270,000)</td><td>19,329 (~1 15 million)</td><td>19.33 (~4.12)</td><td>1.24 (~4.24)</td></tr></table>

The numbers in parentheses are the statistics on the original dataset.

• We use precision, recall, and F-measure to measure the algorithms performance in top 10 recommendations [49].

Number of recommended products that match with the future purchases Precision Total number of recommendedproducts

Number of recommended products that match with the future purchases Recall Total number of products with future purchases

F−measure 2 Precision Recall= Precision Recall

• We use the rank score to measure top recommendations from the algorithms [49].

Rank score $R S = 1 0 0 \frac { \sum _ { i } R S _ { i } } { \sum _ { i } R S _ { i } ^ { \operatorname* { m a x } } } ,$ , where $R S _ { i } = \sum _ { j } \frac { w i l l \_ b u y ( i , j ) } { 2 ^ { ( j - 1 ) / ( h a l f l i f e - 1 ) } }$ and

1; ifthe jthrecommendedproductisincustomer i sfuturepurchaselist will buy i; j 0; otherwise:

where the parameter halflife is the rank of the item that has a 50% likelihood of being read by users, which was set at 2 following previous research [27]. Under this parameter setting, the rank score is affected mainly by the <sup>fi</sup>rst couple of items on the list.

• We inspect the ROC curve of the algorithm, which visualizes the recommendation performance for a large number of recommendations. Due to the unique requirement of recommendation, we have slightly revised the ROC curve. Speci<sup>fi</sup>cally, we replace the X axis from false positive rate to the number of recommendations. Since these two variables are highly correlated, this change does not change the shape of the curve much. However, the <sup>fi</sup>gure is more straightforward for understanding the performance for different numbers of recommendations.

## 4.3. Experimental procedure

Our proposed algorithm is a graph kernel-based machine learning approach. In the evaluation, we compare our proposed approach with state-of-the-art benchmark algorithms and the kernel-based machine learning algorithms that do not effectively use graph information.

For the <sup>fi</sup>rst set of experiments, we select seven state-of-the-art benchmark algorithms:

1) A user-based algorithm that cross-recommends items to similar users (user similarity is based on the items they bought before) [49]. The algorithm <sup>fi</sup>rst computes a user similarity score based on their purchased items. A higher similarity score indicates users have purchased a larger set of common products. Then, the occurrences of items in previous purchases are aggregated while weighted by their similarity to the focal user. Items with a larger score are recommended to the focal user.

2) An item-based algorithm that recommends items that are similar to users' previously purchased items (item similarity is based on the users who bought the item) [49]. The algorithm <sup>fi</sup>rst computes an item similarity score based on users who purchased them. A higher similarity score indicates items share a larger set of common users. Then, for each user, the items that are similar to all his/her previous purchases are aggregated while weighted by the similarity score. Items that are most similar to previous purchases of the focal user are recommended.

3) An item popularity algorithm that recommends items according to their sales/access volumes. Items with higher previous sales volume are recommended to all users.

4) A spreading activation algorithm [23], which is a PageRank-like node ranking algorithm. In this approach, consumers and products are represented as nodes in a graph, each with an activation leve $\mu _ { \mathrm { j } } .$ To generate recommendations for user u, the node is <sup>fi</sup>rst activated and then the effect is propagated to other parts of the graph with given probability. When the process converges, the <sup>fi</sup>nal activation level (on items) indicates their probability of being selected by focal user u.

5) A link analysis algorithm [27], which is a HITS-like node ranking algorithm. This algorithm considers a link between a user u and an item o indicates that o represents part of u's interest and u partially represents o's user base. Thus, an item representativeness score (with respect to each user) and a user representativeness score (with respect to each item) can be calculated in the same fashion as the authority and hub scores in the HITS algorithm, where the sum of the item representativeness scores of the products linked to a user gives the user representativeness score and vice versa. The item representativeness score is used to generate recommendations for the focal user.

6) A matrix factorization algorithm considering user and item bias [35,47]. This algorithm decomposes the user–item adjacency matrix (a matrix of size |U|×|O|) to the multiplication of two sets of vectors, which maps both users and items to a joint latent factor space. It is closely related to the singular value decomposition (SVD) in that it decomposes the user–item matrix. To address practical concerns, previous research has developed the stochastic gradient descent algorithm and also considers that bias may exist on individual users and items. This basic implementation is adopted in our experiments.

7) A binary matrix factorization algorithm [22]. This algorithm considers the fact that unhappened transactions may be due to “unknown” instead of “unlike.” It gives different weights on positive and negative elements in binary matrices when conducting optimization to conduct SVD. We implement the paper's iterative optimization algorithm as a benchmark.

In our experiments, the parameters of all algorithms are optimized for their best performance. Since all these benchmark algorithms use only transaction information, for a fair comparison we only use transaction information for our proposed graph-based approach in this experiment.

For the second set of experiments, we employ the same kernelbased machine learning framework on different features. The purpose is to show the ability of our proposed approach in making use of graph structure and aggregating node information. The <sup>fi</sup>rst benchmark is based solely on user's and item's local features: $k _ { l o c a l } ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) = k _ { n o d e } ( u , u ^ { \prime } ) k _ { n o d e } ( o , o ^ { \prime } )$ [20]. This model directly judg-<sup>ð Þ ¼ ð Þ ð Þ</sup>es probabilities of linkage based on user–item pair characteristics. The second benchmark considers nodes in the context equally as a set: $k _ { s e t } ( \overline { { u o } } , \overline { { u ^ { \prime } o ^ { \prime } } } ) = \sum _ { \substack { i \mathrm { i s w i t h i n } k } \atop \mathrm { s t e p s f r o m } \overline { { u i } } } \sum _ { \substack { i ^ { \prime } \mathrm { i s w i t h i n } k } } k _ { n o d e } ( i , i ^ { \prime } )$ . This kernel con-

ducts pairwise comparison on two sets of nodes and sums node similarity as the overall similarity. In these two algorithms, node features are critical for inferences. Thus, we use such features for all algorithms in this set of experiments. Table 3 shows the local features we selected in the three datasets and the kernels we choose to represent such features. As we have explained, the selection of node features and kernel representation is not a trivial task. In our experiments, we choose the features and kernels that lead to a better performance on local feature models, so that our model is compared with the best scenario of baseline methods. We also optimize the size of the neighborhood for the set kernel, which is two steps from the focal user–item pair. We separate the experiments on user information and item information. While it is possible to include both of them in a model, node feature selection is also (then) required. We leave the optimization of appropriate node features (considering the interference of graph structure) to future research.

Table 3 User and item features.

<table><tr><td>Dataset</td><td>Category</td><td>Feature</td><td>Type</td><td>Kernel</td></tr><tr><td rowspan="5">Book retail</td><td rowspan="2">User</td><td>Age</td><td>Numerical</td><td>RBF</td></tr><tr><td>Education level</td><td>Numerical</td><td>RBF</td></tr><tr><td rowspan="3">Item</td><td>Book title</td><td>Textual</td><td>Linear</td></tr><tr><td>Keywords</td><td>Textual</td><td>Linear</td></tr><tr><td>Introduction</td><td>Textual</td><td>Linear</td></tr><tr><td rowspan="2">Clothing retail</td><td rowspan="2">Item</td><td>Product category</td><td>Categorical</td><td>Linear</td></tr><tr><td>Description</td><td>Textual</td><td>Linear</td></tr><tr><td rowspan="3">Book rating</td><td rowspan="2">User</td><td>Location</td><td>Categorical</td><td>Linear</td></tr><tr><td>Age</td><td>Numerical</td><td>RBF</td></tr><tr><td>Item</td><td>Book author</td><td>Categorical</td><td>Linear</td></tr></table>

When implementing the graph kernel, we conduct 10 iterations (l=10), which means 10 steps of random walks from the focal user– item pair in both directions. According to our observation, the kernel matrix has converged after such number of iterations. In fact, in our testbed, the prediction performance becomes stable after about 3 steps of random walks. It is not sensitive to steps of random walks after that. We specify a uniform stopping probability, p<sub>s</sub>()=1−λ (0bλb1), to generate random walks on the user–item graph. We assume equal probability of jumping from one node to any of its neighbors, i.e., $p _ { t } ( j | i ) = \lambda / d ( i )$ , where d(i) is the number of i's neighbors. We roughly optimize parameter λ (from 0.1 to 0.9) using the training dataset (using 80% training data to build the model and 20% training data to test performance), which leads us to set λ at 0.9.

For all three kernel-based algorithms, we use a popular SVM package, libSVM [11], to build prediction models. The parameters for SVM are selected using the grid search tool provided by libSVM based on experiments on the training data.

In both experiments, the unconnected user–item pairs in the training dataset are examined and ranked. The most possible N links (according to each algorithm) are recommended for each user. The ranked list is compared with the actual transactions in the testing dataset for evaluation.

## 4.4. Results and discussion

Table 4 reports the performance<sup>1</sup> of the top 10 recommendations as compared with the models that do not take a kernel-based framework. The algorithms with the best performance according to pairwise t-tests are highlighted. In general, for top 10 recommendations, the proposed graph kernel is always in the group of best algorithms according to precision, recall, and F-measure. The link analysis algorithm, spreading activation algorithm, and user-based algorithm are also among the best algorithms in different datasets. In general, the algorithms' relative performances are different across datasets, especially for heuristic algorithms, which are not tuned for the dataset. This is common in machine learning research. Since it is almost impossible for one algorithm to succeed in all applications, we generally prefer algorithms that are consistently good across datasets (while searching for the best ones for each particular application). Obviously, our proposed graph kernel is a good algorithm on data with different distributions in terms of precision, recall, and F-measure. According to the rank score measure, which values the <sup>fi</sup>rst couple of recommendations more than later recommendations, our proposed algorithm is slightly lower (statistically signi<sup>fi</sup>cant) than the top ones in different datasets, although the performance difference is minor. The matrix factorization, item popularity, and link analysis algorithms in general achieve a good performance on rank score.

Table 4  
Performance comparison between graph-based algorithms.

<table><tr><td>Dataset</td><td>Algorithms</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>RS</td></tr><tr><td rowspan="8">Book retail</td><td>User-based</td><td>0.0242</td><td>0.1165</td><td>0.0377</td><td>8.2882</td></tr><tr><td>Item-based</td><td>0.0076</td><td>0.0396</td><td>0.0121</td><td>2.4338</td></tr><tr><td>Item popularity</td><td>0.0258</td><td>0.1317</td><td>0.0405</td><td>12.4843</td></tr><tr><td>Link analysis</td><td>0.0280</td><td>0.1408</td><td>0.0439</td><td>11.8745</td></tr><tr><td>Spreading activation</td><td>0.0224</td><td>0.1110</td><td>0.0349</td><td>9.3618</td></tr><tr><td>Matrix factorization</td><td>0.0255</td><td>0.1286</td><td>0.0399</td><td>12.4843</td></tr><tr><td>Binary Matrix factorization</td><td>0.0110</td><td>0.0593</td><td>0.0177</td><td>3.0812</td></tr><tr><td>Graph kernel</td><td>0.0286</td><td>0.1461</td><td>0.0449</td><td>11.2838</td></tr><tr><td rowspan="8">Clothing retail</td><td>User-based</td><td>0.0114</td><td>0.0778</td><td>0.0193</td><td>4.5900</td></tr><tr><td>Item-based</td><td>0.0078</td><td>0.0597</td><td>0.0136</td><td>3.0354</td></tr><tr><td>Item popularity</td><td>0.0062</td><td>0.0326</td><td>0.0100</td><td>1.4173</td></tr><tr><td>Link analysis</td><td>0.0124</td><td>0.0818</td><td>0.0209</td><td>4.7752</td></tr><tr><td>Spreading activation</td><td>0.0076</td><td>0.0513</td><td>0.0129</td><td>3.1005</td></tr><tr><td>Matrix factorization</td><td>0.0058</td><td>0.0309</td><td>0.0094</td><td>1.3935</td></tr><tr><td>Binary matrix factorization</td><td>0.0088</td><td>0.0649</td><td>0.0153</td><td>3.9898</td></tr><tr><td>Graph kernel</td><td>0.0131</td><td>0.0855</td><td>0.0219</td><td>4.1307</td></tr><tr><td rowspan="8">Book rating</td><td>User-based</td><td>0.0082</td><td>0.0269</td><td>0.0119</td><td>1.8260</td></tr><tr><td>Item-based</td><td>0.0052</td><td>0.0203</td><td>0.0079</td><td>1.3080</td></tr><tr><td>Item popularity</td><td>0.0058</td><td>0.0224</td><td>0.0089</td><td>1.9283</td></tr><tr><td>Link analysis</td><td>0.0065</td><td>0.0225</td><td>0.0096</td><td>1.6260</td></tr><tr><td>Spreading activation</td><td>0.0071</td><td>0.0264</td><td>0.0106</td><td>1.7307</td></tr><tr><td>Matrix factorization</td><td>0.0054</td><td>0.0203</td><td>0.0082</td><td>1.9307</td></tr><tr><td>Binary matrix factorization</td><td>0.0061</td><td>0.0245</td><td>0.0093</td><td>1.4029</td></tr><tr><td>Graph kernel</td><td>0.0077</td><td>0.0295</td><td>0.0118</td><td>1.6251</td></tr></table>

Bold values are not signi<sup>fi</sup>cantly different from the largest ones at 90% con<sup>fi</sup>dence interval.

Fig. 3 reports the ROC curves for the top 1000 recommendations made by the different models. It con<sup>fi</sup>rms that the graph kernel was among one of the best algorithms for a smaller number of recommendations (about 50 recommendations for the two book datasets and about 20 recommendations for the clothing dataset). Moreover, when a large number of predictions are needed, the graph kernel signi<sup>fi</sup>cantly outperforms all other methods on the ROC curve. Its performance is about twice that of the item-based algorithm and 20% to 50% better than other algorithms. The matrix factorization algorithm also has a better performance than other benchmarks on a large number of predictions.

Table 4 and Fig. 3 together show the advantage of different algorithms. In general, our proposed graph kernel shows absolute advantage on a larger number of recommendations. Its performance is always among the best on top 10 recommendations. Its performance is slightly lower than the best ones on the <sup>fi</sup>rst couple of recommendations. Matrix factorization and item popularity methods are good at recommending items at the very top of the list. With appropriate parameters, the binary matrix factorization algorithm can outperform standard matrix factorization on top 10 recommendations. Other than the graph kernel, link analysis methods also perform well on predictions of the top 10 to 50 items.

![](/api/attachments/VNCWJJJM/fulltext/images/6856da97558ac7e55cb6d6ab18ddc7898993ce7cb89c2a31aa1866909670e43a.jpg)

![](/api/attachments/VNCWJJJM/fulltext/images/5f47a17cb9528795417a0a6b763d288449a79a7198c7bc1088821663d956e241.jpg)

![](/api/attachments/VNCWJJJM/fulltext/images/5470a28a85e996968c590f473cb7d284546b02874c9cbd9fb1ed2274c21f2801.jpg)  
Fig. 3. ROC curves of top 1000 recommendations of graph-based algorithms.

In our proposed approach, the model is optimized to link prediction performance on the entire graph, i.e., differentiating overall positive vs. negative instances. It may provide more “high con<sup>fi</sup>dence” predictions to some users than others. When limited to a small number of recommendations, many of such predictions may be excluded, which limits its recommendation performance on rank score (as re<sup>fl</sup>ected in a couple of top predictions). On a larger number of predictions, its advantages can be fully exhibited. In real applications, a large number of predictions are always needed if e-commerce Websites want to update the recommendation list when users refresh the Webpages. Furthermore, repeat customers, who bring a large portion of pro<sup>fi</sup>ts, also require a larger number of recommendations. Our proposed graph kernel meets these requirements very well. The customers may be better served by the follow-up recommendations from our proposed approach. In practice, it is also bene<sup>fi</sup>cial to combine graph kernels with other algorithms to improve performance on a small number of recommendations.

Fig. 4 reports the ROC curves for the top 1000 recommendations made by the learning-based algorithms. (We omit the performance tables on top 10 recommendations due to space limitations. The three algorithms' performances on top 10 recommendations are generally distinguishable in the <sup>fi</sup>gure.) While the graph kernel performance may be improved with carefully selected node features, in the current setting the graph kernel signi<sup>fi</sup>cantly outperformed the set kernel and local features in most cases. The results clearly show the necessity of capturing the structure of the user–item graph in addressing the recommendation task. In the graph kernel, the features of individual nodes are accumulated to the focal user–item pairs following the links. The effective use of the user–item graph may cause its better performances. The set kernel ignores the graph structure, while the local feature-based kernel ignores all related nodes. These design de<sup>fi</sup>ciencies may have limited their prediction abilities.

When using item information on the book rating dataset, the local feature method initially achieved the best performance and then was outperformed by the graph kernel. In this dataset, the item information was author name. In the book rating application, the author of a book has a strong in<sup>fl</sup>uence on users' ratings. A reader may choose a book purely because of the author. In comparison, different books rated by a reader may have much less topic/style similarities. Thus, co-rated books may have less prediction power than just local features on authors in these experiments.

## 5. Conclusions and future directions

In this paper, we present a graph kernel-based approach for recommendation. Considering the recommendation task as a link prediction problem in user–item interaction graphs, we de<sup>fi</sup>ne a graph kernel on the user–item pair's context and use its graph structure to infer whether a user may have a link with an item. We analyzed the graph kernel's characteristics including validity and computational ef<sup>fi</sup>ciency. On three real-world datasets, our graph kernel-based approach shows improved recommendation performances over benchmark algorithms and kernel-based machine learning algorithms that make limited use of graph structure. Our proposed approach performed even better for recommending a large number of items.

We will explore how to extend this graph kernel-based approach to other link prediction and recommendation applications, such as information recommendation within mixed contents (i.e., related textual, image, and multimedia contents) and patent prior art search where patent examiners suggest additional references for patent applications. Such knowledge recommendation problems are critical to modern organizations [42,69]. We also plan to extend our work by combining multiple types of graphs into a model. For example, apart from the graph of user–item interactions, we will include social networks (between users) and/or citation networks (between items/ contents) to address the link prediction and recommendation problem. We also plan to identify a systematic approach that will combine graph kernels with appropriate node information to fully exploit the ability of graph kernels in recommendation, which is not fully addressed in the scope of this paper.

![](/api/attachments/VNCWJJJM/fulltext/images/a303289b39749e5c144797400cc2953f56af876583c612714a61de47b07a1b8b.jpg)  
Fig. 4. ROC curves of top 1000 recommendations of learning-based algorithms.

## Acknowledgments

This work was supported in part by: the City University of Hong Kong SRG-7002518, SRG-7002625, StUp-7200170, and the United States NSF IIS-0114011. All opinions in this article are those of the authors and do not necessarily re<sup>fl</sup>ect the views of the funding agencies.

## References

[1] E. Acar, D.M. Dunlavy, T.G. Kolda, Link prediction on evolving data using matrix and tensor factorizations, in: International Conference on Data Mining, 2009.

[2] G. Adomavicius, Y. Kwon, New recommendation techniques for multicriteria rating systems, IEEE Intelligent Systems (2007) 48–55

[3] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowl edge and Data Engineering 17 (2005) 734–749.

[4] G. Adomavicius, A. Tuzhilin, Context-aware recommender systems, in: F. Ricci, L. Rokach, B. Shapira, P.B.. Kantor (Eds.), Recommender Systems Handbook, Springer Science & Business Media 2011

[5] H.J. Ahn, A new similarity measure for collaborative <sup>fi</sup>ltering to alleviate the new user cold-starting problem, Information Sciences 178 (2008) 37–51.

[6] A.L. Barabasi, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[7] N. Benchettara, R. Kanawati, C. Rouveirol, Supervised machine learning applied to link prediction in social networks in: International Conference on Advances in Social Networks Analysis and Mining, 2010, pp. 326–330.

[8] J. Bollen, M.L. Nelson, G. Geisler, R. Araujo, Usage derived recommendations for a video digital library, Journal of Network and Computer Applications 30 (2007) 1059–1083.

[9] K.M. Borgwardt, C.S. Ong, S. Schonauer, S.V.N. Vishwanathan, A.J. Smola, H.P. Kriegel, Protein function prediction via graph kernels, Bioinformatics 21 (2005) I47–I56.

[10] S. Boutemedjet, D. Ziou, A graphical model for context-aware visual content recommendation, IEEE Transactions on Multimedia 10 (2008) 52–62.

[11] C.-C. Chang, C.-J. Lin, LIBSVM: a library for support vector machines, http://www. csie ntuedu.tw/\~cilin/libsym 2001

[12] K.W. Cheung, J.T. Kwok, M.H. Law, K.C. Tsui, Mining customer product rating for personalized marketing Decision Support Systems 35 (2003) 231-243.

[13] D. Cohn, T. Hofmann, The missing link: a probabilistic model of document content and hypertext connectivity, Advances in Neural Information Processing Systems, 2001.

[14] F. Fouss, A. Pirotte, J.M. Renders, M. Saerens, Random-walk computation of similarities between nodes of a graph with application to collaborative recommendation, IEEE Transactions on Knowledge and Data Engineering 19 (2007) 355–369.

[15] F. Fouss, K. Francoisse, L. Yen, A. Pirotte, M. Saerens, An experimental investigation of kernels on graphs for collaborative recommendation and semisupervised classification, Neural Networks 31 (2012) 53–72.

[16] S. Funk, Net<sup>fl</sup>ix update: try this at home. Available from http://sifter.org/\~simon/ journal/20061211.html 2006

[17] L. Getoor, M. Sahami, Using probabilistic relational models for collaborative <sup>fi</sup>ltering, in: International WebKDD Workshop, 1999.

[18] M. Gori, A. Pucci, ItemRank: a random-walk based scoring algorithm for recommender engines, in: International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 2007.

[19] J. Grif<sup>fi</sup>th, C. O'Riordan, H. Sorensen, A constrained spreading activation approach to collaborative <sup>fi</sup>ltering, in: The International Conference on Knowledge-Based Intelligent Information and Engineering Systems, 2006, pp. 766–773.

[20] M.A. Hasan, V. Chaoji, S. Salem, M. Zaki, Link prediction using supervised learning, in: Workshop on Link Analysis, Counter-terrorism and Security, 2006.

[21] T. Hofmann, Latent semantic models for collaborative <sup>fi</sup>ltering, ACM Transactions on Information Systems 22 (2004) 89–115.

[22] Y. Hu, Y. Koren, C. Volinsky, Collaborative <sup>fi</sup>ltering for implicit feedback datasets, in: IEEE International Conference on Data Mining, 2008.

[23] Z. Huang, H. Chen, D. Zeng, Applying associative retrieval techniques to alleviate the sparsity problem in collaborative <sup>fi</sup>ltering, ACM Transactions on Information Systems 22 (2004) 116–142.

[24] Z. Huang, W.Y. Chung, H.C. Chen, A graph model for e-commerce recommender systems, Journal of the American Society for Information Science and Technology 55 (2004) 259–274.

[25] Z. Huang, D. Zeng, H. Chen, A uni<sup>fi</sup>ed recommendation framework based on probabilistic relational models, in: 4th Annual Workshop on Information Technologies and Systems, 2004.

[26] Z. Huang, D. Zeng, H. Chen, Analyzing consumer-product graphs: empirical <sup>fi</sup>ndings and applications in recommender systems, Management Science 53 (2007) 1146–1164.

[27] Z. Huang, D. Zeng, H. Chen, A comparative study of recommendation algorithms in e-commerce applications, IEEE Intelligent Systems 22 (2007) 68–78.

[28] T. Iwata, K. Saito, T. Yamada, Recommendation method for improving customer lifetime value, IEEE Transactions on Knowledge and Data Engineering 20 (2008) 1254–1263.

[29] Y.C. Jiang, J. Shang, Y.Z. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (2010) 470–479.

[30] H. Kashima, K. Tsuda, A. Inokuchi, Marginalized kernels between labeled graphs, in: The 20th International Conference on Machine Learning, 2003.

[31] H. Kashima, T. Kato, Y. Yamanishi, M. Sugiyama, K. Tsuda, Link propagation: a fast semi-supervised learning algorithm for link prediction, in: SIAM Data Mining Conference, 2009.

[32] H.-N. Kim, I. Ha, K.-S. Lee, G.-S. Jo, A. El-Saddik, Collaborative user modeling for enhanced content <sup>fi</sup>ltering in recommender systems, Decision Support Systems 51 (2011) 772–781.

[33] R.I. Kondor, J. Lafferty, Diffusion kernels on graphs and other discrete structures, in: The 19th International Conference on Machine Learning, 2002, pp. 315–322.

[34] Y. Koren, Factorization meets the neighborhood: a multifaceted collaborative <sup>fi</sup>ltering method, in: International Conference on Knowledge Discovery and Data Mining, 2008, pp. 426–434.

[35] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (2009) 30–37.

[36] J. Kubica, A. Goldenberg, P. Komarek, A. Moore, J. Schneider, A comparison of statistical and machine learning algorithms on the task of link completion, in: KDD Workshop on Link Analysis for Detecting Complex Behavior, 2003, p. 8.

[37] J. Kunegis, A. Lommatzsch, Learning spectral graph transformation for link prediction, in: International Conference on Machine Learning, 2009.

[38] J. Kunegis, E.W.D. Luca, S. Albayrak, The link prediction problem in bipartite networks, in: International Conference on Information Processing and Management of Uncertainty in Knowledge-based Systems, 2010.

[39] S.Q. Le, T.B. Ho, T.T.H. Phan, A novel graph-based similarity measure for 2D chemical structures, Genome Informatics 14 (2004) 82–91.

[40] X. Li, H.C. Chen, Z. Zhang, J.X. Li, J.F. Nunamaker, Managing knowledge in light of its evolution process: an empirical study on citation network-based patent classification, Journal of Management Information Systems 26 (2009) 129–153

[41] X. Li, H.C. Chen, J.X. Li, Z. Zhang, Gene function prediction with gene interaction networks: a context graph kernel approach, IEEE Transactions on Information Technology in Biomedicine 14 (2010) 119–128.

[42] T.P. Liang, Y.F. Yang, D.N. Chen, Y.C. Ku, A semantic-expansion approach to personalized knowledge recommendation, Decision Support Systems 45 (2008) 401–412.

[43] D. Liben-Nowell, J. Kleinberg, The link-prediction problem for social networks, Journal of the American Society for Information Science and Technology 58 (2007) 1019–1031.

[44] M. McPherson, L. Smith-Lovin, J.M. Cook, Birds of a feather: homophily in social networks, Annual Review of Sociology 27 (2001) 415–444.

[45] J. Newton, R. Greiner, Hierarchical probabilistic relational models for collaborative <sup>fi</sup>ltering, in: Workshop on Statistical Relational Learning, 21st International Conference on Machine Learning, 2004.

[46] K. Oku, S. Nakajima, J. Miyazaki, S. Uemura, Context-aware SVM for context-dependent information recommendation, in: 7th International Conference on Mobile Data Management, Washington, DC, USA, 2006, p. 109.

[47] A. Paterek, Improving regularized singular value decomposition for collaborative <sup>fi</sup>ltering, in: KDD Cup and Workshop, 2007, pp. 39–42

[48] D. Pavlov, E. Manavoglu, C.L. Giles, D.M. Pennock, Collaborative <sup>fi</sup>ltering with maximum entropy, IEEE Intelligent Systems 19 (2004) 40–48.

[49] M.J. Pazzani, A framework for collaborative, content-based and demographic <sup>fi</sup>ltering, Arti<sup>fi</sup>cial Intelligence Review 13 (1999) 393–408.

[50] G. Polcicova, P. Tino, Making sense of sparse rating data in collaborative <sup>fi</sup>ltering via topographic organization of user preference patterns, Neural Networks 17 (2004) 1183–1199.

[51] P.K. Reddy, M. Kitsuregawa, P. Sreekanth, S.S. Rao, A graph based approach to extract a neighborhood customer community for collaborative <sup>fi</sup>ltering, Lecture Notes in Computer Science 2544 (2002) 188–200

[52] P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative <sup>fi</sup>ltering of netnews, in: The ACM 1994 Conference on Computer Supported Cooperative Work, 1994, pp. 175–186.

[53] R. Salakhutdinov, A. Mnih, Probabilistic matrix factorization, in: Neural Information Processing Systems, 2008, pp. 1257–1264.

[54] R.R. Sarukkai, Link prediction and path analysis using Markov chains, Computer Networks 33 (2000) 377–386.

[55] B.M. Sarwar, G. Karypis, J.A. Konstan, J. Reidl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, in: The International Conference on the World Wide Web, 2001, pp. 285–295

[56] B. Scholkopf, J.C. Platt, J. Shawe-Taylor, A.J. Smola, R.C. Williamson, Estimating the support of a high-dimensional distribution, in: MSR-TR-99-87, Microsoft Research, 1999.

[57] J. Scripps, P.-N. Tan, F. Chen, A.-H. Esfahanian, A matrix alignment approach for link prediction, in: International Conference on Pattern Recognition, 2008.

[58] Y. Tan, J. Wang, A support vector machine with a hybrid kernel and minimal Vapnik–Chervonenkis dimension, IEEE Transactions on Knowledge and Data Engineering 16 (2004) 385–395.

[59] B. Taskar, P. Abbeel, D. Koller, Label and link prediction in relational data, in: IJCAI Workshop on Learning Statistical Models from Relational Data 2003

[60] S. Vucetic, Z. Obradovic, Collaborative <sup>fi</sup>ltering using a regression-based approach, Knowledge and Information Systems 7 (2005) 1–22.

[62] Y.W. Wang, W.H. Dai, Y.F. Yuan, Website browsing aid: a navigation graph-based recommendation system, Decision Support Systems 45 (2008) 387–400.

[64] J.A. Xu, K. Araki, A SVM-based personal recommendation system for TV programs, in: The 12th International Multi-Media Modelling Conference, 2006.

[65] Y. Yajima, One-class support vector machines for recommendation tasks, in: The Paci<sup>fi</sup>c-Asia Conference on Advances in Knowledge Discovery and Data Mining, 3918, 2006, pp. 230–239.

[66] K. Yu, W. Chu, Gaussian process models for link analysis and transfer learning, Neural Information Processing Systems, 2007.

[67] K. Yu, A. Schwaighofer, V. Tresp, X.W. Xu, H.P. Kriegel, Probabilistic memorybased collaborative <sup>fi</sup>ltering, IEEE Transactions on Knowledge and Data Engineering 16 (2004) 56–69.

[68] C. Zeng, C.X. Xing, L.Z. Zhou, X.H. Zheng, Similarity measure and instance selection for collaborative <sup>fi</sup>ltering, International Journal of Electronics Commerce 8 (2004) 115–129.

[69] L. Zhen, G.Q. Huang, Z.H. Jiang, Recommender system based on work<sup>fl</sup>ow, Decision Support Systems 48 (2009) 237–245.

[70] T. Zhou, J. Ren, M. Medo, Y.C. Zhang, Bipartite network projection and personal recommendation, Physical Review E 76 (2007).

[71] J. Zhu, J. Hong, J.G. Hughes, Using Markov chains for link prediction in adaptive Web sites, in: ACM SIGWEB Hypertext, 2002.

[72] C.-N. Ziegler, S.M. McNee, J.A. Konstan, G. Lausen, Improving recommendation lists through topic diversi<sup>fi</sup>cation, in: The International Conference on the World Wide Web, 2005, pp. 22–32.

Xin Li received the B. Eng. degree in automation and the M. Eng. degree in control theory and control engineering from Tsinghua University, Beijing, China, in 2000 and 2003, respectively, and the Ph.D. degree in management information systems from the University of Arizona, Tucson, in 2009. He is currently an Assistant Professor in the Department of Information Systems at the City University of Hong Kong, Hong Kong. His work has appeared in the Journal of Management Information Systems, Journal of Biomedical Informatics, Bioinformatics, Nature Nanotechnology, and Journal of the American Societ for Information Science and Technology, among others. His current research interests include business intelligence & knowledge discovery, social network analysis, social media and scientometric analysis. Dr. Li is a member of IEEE ACM and AIS

Hsinchun Chen received the B.S. degree in management science from the National Chiao-Tung University in Taiwan in 1981, the MBA degree from the State University of New York at Buffalo in 1985, and the Ph.D. degree in Information Systems from the New York University in 1989. He is currently the McClelland Professor of Management Information Systems at the University of Arizona, Tucson, where he is also the Director of the Arti<sup>fi</sup>- cial Intelligence Laboratory. He is author/editor of 20 books, 25 book chapters, 230 SCI journal articles, and 140 refereed conference articles. His current interests include Web computing, search engines, digital library, intelligence analysis, biomedical informatics, data/text/web mining, and knowledge management Dr. Chen is a fellow of IEEE and AAAS and a member of the ACM, INFORMS, AIS, AAAI, AMIA, and ASIS. Dr. Chen has served as a Scienti<sup>fi</sup>c Counselor/Advisor of the National Library of Medicine (USA), Academia Sinica (Taiwan), and National Library of China (China). Dr. Chen is the Editor-in-Chief of the ACM Transactions on Management Information Systems and Springer Security Informatics Journal, and Associate Editor-in-Chief of the IEEE Intelligent Systems and serves on ten editorial boards including JEEE Transactions on Systems Man and Cybernetics ACM Transactions on Information Systems, Journal of the American Society for Information Science and Technology, Decision Support Systems, and International Journal on Digital Library. Dr. Chen received the IEEE Computer Society Technical Achievement Award in 2006 and the INFORMS De sign Science Award in 2008.
