---
otero_id: 19758
otero_key: "JUWDD98N"
title: "A personalized paper recommendation method considering diverse user preferences"
authors: "Yi Li; Ronghui Wang; Guofang Nan; Dahui Li; Minqiang Li"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113546"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A personalized paper recommendation method considering diverse user preferences

![](/api/attachments/JUWDD98N/fulltext/images/875a79c89aaae9212b532d086adf8fa8ff955dbd05236cec9d0d11a4ec362185.jpg)

Yi Li <sup>a</sup>, Ronghui Wang <sup>a</sup>, Guofang Nan <sup>a,\*</sup>, Dahui Li <sup>b</sup>, Minqiang Li <sup>a</sup>

<sup>a</sup> College of Management and Economics, Tianjin University, Tianjin 300072, China

<sup>b</sup> Labovitz School of Business and Economics, University of Minnesota Duluth, Duluth, MN 55812, USA

## A R T I C L E I N F O

Keywords: Paper recommendation Heterogeneous network Meta-paths Personalized recommendation

## A B S T R A C T

Prior studies of paper recommendation methods that consider historical user preferences rarely adequately address the complexity of user preferences and interests. We propose a method to recommend personalized papers based on a heterogeneous network that includes papers, venues, authors, terms, and users as well as the relations among these entities. We investigate meta-paths in the network to capture user preferences and apply random walks on these meta-paths to measure recommendation scores of candidate papers to target users. We employ a personalized weight learning process to discover a user's personalized weights on different meta-paths using Bayesian Personalized Ranking as the objective function. A global recommendation score is calculated by combining recommendation scores on different meta-paths with personalized weights. We conducted experi ments using two different datasets and the results showed that the proposed method performed better than other baseline methods.

## 1. Introduction

Academic papers are generated, gathered, stored, and disseminated on the web at an unprecedented speed, which results in information overload on users who need to find academic papers of interest [1]. Scientific digital libraries and literature search engines employ search tools to retrieve a list of relevant papers using keyword-based queries. However, these search tools will return the same results to different users who search the same keyword because these tools have no knowledge of users’ historical preferences. In addition, search tools are not sufficient to fulfill a user’s implicit needs when the user is not clear of what to search. Therefore, how to effectively find relevant and helpful papers based on user preferences is a crucial factor for paper recom mendation research [2], which has developed various recommender systems in the areas of movie [3,4], news [5,6], music [7,8] and service [9,10]. Such recommender systems are more effective than search en gines because these systems consider the user’s unique preferences and interests in the design of recommendation methods.

Previous studies have focused on several categories of paper recommendation methods: content-based filtering methods, collabora tive filtering methods, and network-based methods [11]. Content-based filtering methods build user profiles based on prior user preferences and recommend papers that match user profiles. The main drawback of content-based filtering methods is the lack of diversity and novelty in recommendations because the method only recommends papers with the same research topics [26]. Collaborative filtering methods provide recommendations based on similar preferences of peer users. However, there exist such limitations as data sparsity and cold start problem, which makes it difficult to reach ideal results using these methods [26].

Network-based methods, which consider recommendations as a link prediction task in a network, have received attention from the research community [12,13]. However, some network-based methods, which assume a homogeneous network that contains objects and relations that are of the same types, such as the citation network and the co-author network [29–31], fail to consider the heterogeneous nature of the ob jects and relations in the network. For example, novice users who are not familiar with a research field would prefer papers that are focused on similar research topics, whereas expert users tend to choose papers written by their co-authors. Thus, recommendations based on the ho mogeneous network are only appropriate for one kind of users and the overall performance of the recommendation may be poor. Moreover, user preferences are often vague, diverse, and complex. For example, users may prefer to have papers that share the same authors, venues, and research topics rather than papers that only share similar research topics. A heterogeneous network can include much more information and richer semantics, which is able to model complex user preferences.

![](/api/attachments/JUWDD98N/fulltext/images/c368690c1dcb63d1a0f630552e2fc32ebadb3d8dfd2e43b12fa4553d1f5d420a.jpg)  
Fig. 1. A heterogeneous network of academia papers.

An academic web which contains multiple types of interacting components can be modeled as a heterogeneous network with different objects and relations. Fig. 1 depicts such a network used in our paper recommendation method, which consists of different types of nodes and links. Nodes indicate object types, including papers, authors, venues, terms, and users. Links indicate relation types between these objects, including cite or cited-by, written or written-by, publish or published-in, include or included-in, and like or liked-by. This heterogeneous network can effectively integrate multiple categories of useful information to improve recommendation quality [12].

Prior network-based methods apply random walk with restart on the heterogeneous network to calculate node proximity between users and papers. However, pattern discovery of user preferences is commonly ignored in these studies. The main task of our work is to discover user preference patterns to provide the foundation for paper recommenda tions. We explore the semantic information of meta-path that consists of a series of relations between objects in the heterogeneous network to represent user preference for personalized recommendations, where different meta-paths represent diverse user preferences [14]. After generating a set of meta-paths, we apply random walk on each metapath that directly connects users and papers, so that we are able to predict the recommendation scores between users and papers of different preference patterns.

Considering that users may have different preferences on each metapath, we design a learning process to derive personalized weights on each meta-path and build a recommendation model for each individual user based on the user’s historical preferences. Xu et al. [42] minimized the square of the difference between recommendation scores given by the model and a user’s real preferences for papers to learn the user’s personalized weights on each meta-path. In other word, the authors minimized the scores of papers that were not recommended and maxi mized the scores of papers that were recommended. Therefore, they emphasized using the accurate recommendation score of each paper, which is not necessary for personalized weight learning and may lead to poor recommendation. To overcome this problem, we apply Bayesian Personalized Ranking (BPR) to build the objective function in order to ensure that recommendation scores of recommended papers are greater than those of papers that are not recommended.

Overall, we propose a paper recommendation method based on the heterogeneous network (named as PRHN) by leveraging a user’s history record and different meta-paths to infer personal interests for paper recommendations. The main contributions of this paper are as follows. First, we construct a heterogeneous network to integrate papers, venues, authors, terms, users and their relations into a unified framework. Sec ond, we apply random walk on different meta-paths that connect papers and users to calculate the recommendation scores of candidate papers to target users. Third, we employ Bayesian Personalized Ranking (BPR) as the objective function to learn personalized weights on different metapaths. We conducted experiments on the Aminer [15] dataset and the DBLP dataset to demonstrate the effectiveness of our proposed method in comparison with other baseline paper recommendation methods.

The rest of the paper is organized as follows. Section 2 reviews previous studies on paper recommendations. Section 3 introduces the details of our proposed method. Section 4 describes the experiment design and reports experiment results. Section 5 concludes the paper and presents future directions.

## 2. Related work

## 2.1. Content-based filtering and collaborative filtering methods

Content-based filtering methods recommend a user papers that are similar to the papers preferred by the user in the past [16]. Liang et al. [17] applied a semantic network and the spreading activation model to create user profiles and made recommendations accordingly. Weng and Chang [18] employed ontology and the spreading activation model to find topics of interest for users and then recommended papers that were related to these users’ research topics. Tang and Zeng [19] applied keyword clustering and generated user profiles based on the extended subject ontology. Zhao et al. [20] introduced a method based on the knowledge gap between background knowledge and research target, both of which were extracted from a user’s history and a new proposal of the user. Pera and Ng [21] integrated content similarity and social connections to recommend papers on a social bookmarking site. Chen et al. [22] suggested a hybrid reranking approach by utilizing both paper content and user behavior. These methods emphasize feature extraction from papers and user profiles so that there exists a lack of diversity and novelty in recommendations.

Collaborative filtering methods assume that users who are interested in the same papers usually have similar preferences for other papers [16]. Such methods have issues such as data sparsity and cold-start problem caused by few ratings on papers to be recommended [26]. To resolve such problems, Sun et al. [23] used implicit and explicit social relationships to find similar users, including social connection, behavior connection, and profile similarity. Sugiyama and Kan [24] presented an imputation-based collaborative filtering approach with adaptive neighborhood selection strategies to identify potential citation papers. Lai et al. [25] incorporated user and group trust into filtering techniques in order to improve recommendation quality. Wang et al. [26] inte grated friend relations and preferences into a standard collaborative filtering model to address data sparsity. The drawback of these methods is that they can recommend papers to researchers with the same pref erence patterns but cannot fulfill different users’ diverse preferences.

## 2.2. Network-based methods

Network-based methods transform paper recommendation into a link prediction task in a network, where a user’s historical preferences are considered as known links to predict possible links that exist between the user and papers. The network can be either homogeneous or heterogeneous given the types of entities and relations [12]. A homo geneous network includes only one type of entity and relation, such as a citation network. Kessler [27] presented a bibliographic coupling algo rithm to measure the similarity between two papers by the number of shared citations. Small [28] used the frequency of two papers being cited together as a measure of similarity in a co-citation analysis. West et al. [29] applied hierarchical clustering on a citation network to make expert, traditional, and random recommendations for different users based on multiple scales of relevance. Son and Kim [30] combined citation analysis and network analysis on a multilevel citation network and used co-citation and bibliographic coupling to select candidate pa pers and recommend papers based on a combination of four centrality measures. Huang et al. [31] proposed a neural probabilistic model that jointly learned the semantic representation of citation contexts and cited articles and then estimated the probability of citing an article by training the neural network.

![](/api/attachments/JUWDD98N/fulltext/images/b3f250261f4d75883b4d4b9ee96da37b23c8cd37d007293923889b558870eec1.jpg)  
Fig. 2. The process of PRHN.

To improve recommendation performance, recent paper recom mendation methods considered the heterogeneous network. Hwang et al. [32] integrated topic information in a co-authorship network and developed a task-focused technique. Liu et al. [33] applied random walk on a heterogeneous network which combined citation relations between articles and researchers’ historical preferences. Xia et al. [34] developed a heterogeneous network with common author relations and re searchers’ historical preferences. Tian and Jing [35] established a birelational graph of the heterogeneous information of scientific articles by considering content similarity, user interest correlation, and userpaper readership. Cai et al. [36] incorporated different information such as content similarity between two papers, relationship between papers and authors, and relationship between papers and venues into a three-layered mutually reinforced model. However, these methods could not provide diverse recommendations to users with different preference patterns which were unable to be discovered in the hetero geneous network.

## 2.3. Diverse user preferences in recommendations

User preferences are heterogeneous, complex and diverse. Therefore, modeling user preferences is a crucial task in recommendation methods. Many recent studies were focused on exploring heterogeneous user preferences in different domains to improve recommendation quality. Danaf et al. [37] applied the Hierarchical Bayes procedure to estimate user preferences at the population-level, the individual-level, and the menu-specific level before providing personalized menu recommenda tions. Gao et al. [38] extracted three major factors that influenced user interests in the microblog system. which were personal interest. interest in authors, and microblog quality. The authors then constructed a feature vector based on these factors as the input of a deep learning network model to rank candidate microblogs. Wang et al. [39] con structed three bipartite graphs related to a user’s interests in music topics, which were song-playlist network, song-singer network, and song-album network. Final recommendations were made by integrating the ranks calculated by applying Personalized PageRank model on the three bipartite graphs. Qiao et al. [40] established a joint model of various contextual factors that included geographical influence, social relationship, and temporal information to recommend point of interests in a location-based social network. Zhou et al. [41] captured user preferences in the group facet, the individual facet, and the action facet, and then integrated these multi-facet user preferences into a matrix factorization recommendation model.

The heterogeneous user preference parameters in these studies were specifically designed for specific domains of interest such as sharing music data in a social network [39] or location-based service that allows users to share geographical information [40], and, therefore, could not be applied to our domain of paper recommendation. In contrary, our method is different in that we construct a heterogeneous network with the meta-data of a general domain so that we can automatically model diverse user preferences by discovering the meta-paths in a network.

Xu et al. [42] examined online academic community recommenda tion by combining the recommendation scores on different meta-paths with personalized weights learned from users’ historical preferences. This work is closely related to our research. In order to learn personal ized weights on meta-paths, Xu et al. [42] minimized the square of the difference between recommendation scores given by the model and a user’s real preference for each paper. However, it is unnecessary to pursuit accurate recommendation scores of papers, which may lead to poor recommendation results. Different from Xu et al. [42], we apply the Bayesian Personalized Ranking optimization framework to build our objective function to ensure that recommendation scores of recom mended papers are greater than those of papers that are not recommended.

## 3. Paper recommendation based on the heterogeneous network

We name our proposed method as Paper Recommendation based on the Heterogeneous Network (PRHN). The process for the proposed method comprises five steps, as shown in Fig. 2. First, we construct a heterogeneous network containing multiple type of extracted objects and relations. Second, we develop a meta-path set to explore the abundant connections between target users and candidate papers. Third, we calculate recommendation scores of candidate papers to target users in each meta-path. Fourth, we apply historical user preferences to learn personalized weights on all the meta-paths. Finally, we generate a Top-N recommendation list by selecting N papers with the highest global recommendation scores. The global score is the sum of the product of the personalized weight and the recommendation score between the user and the paper on each meta-path.

## 3.1. Heterogeneous network construction

A heterogeneous network contains rich information and fuses mul tiple semantic meanings into a unified framework [12]. In this subsec tion, we define a heterogeneous network and then apply it to paper recommendation.

A heterogeneous network is defined as a direct graph $G = ( V , E )$ with an object type mapping function $\phi : V  O$ and a relation type mapping function $\psi : E  R ,$ where the type of objects $| O | > 1$ or the type of relations $| R | > 1$ . Each vertex v ∈ V belongs to one particular object type in the object type set $O : \phi ( \nu ) \in O _ { : }$ , and each edge e ∈ E belongs to one particular relation type in the relation type set $R : \psi ( e ) \in R$

Based on the definition, we extract multiply objects and relations from the academic dataset to build an academic heterogeneous network for paper recommendation as shown in Fig. 3. The figure includes five types of objects, which are paper(P), venue(V), author(A), term(T), and user(U), and ten types of relations, which are cite, cited-by, publish, published-in, write, written-by, include, included-in, like, and liked-by. The link weight between two types of objects represents the relevance degree between the objects. In most cases, the weight is set to 1 if there exists a link, otherwise 0. Because a paper contains multiple terms of relevance, we use Term Frequency–Inverse Document Frequency (TF-IDF) scores to represent link weights between papers and terms.

![](/api/attachments/JUWDD98N/fulltext/images/d5f5cace133b2947e2243ba2fbb0d124993f2b14fdf693f90c47d18b8660d8b5.jpg)  
Fig. 3. An academic heterogeneous network.

The relations between object type set M and N can be represented as an adjacency matrix $A _ { M N } = [ a _ { i j } ] _ { m \times n } ,$ which is defined as:

$$
a _ {i j} = \left\{ \begin{array}{c c} w _ {i j} & \text { if } M _ {i} \text { has   a   link   with } N _ {j} \\ 0 & \text { otherwise } \end{array} \right.\tag{1}
$$

where m is the index of object type M, n is the index of object type N, w is the link weight between M and $N _ { j } ,$ and $0 \leq w _ { i j } \leq 1$ . Our heterogeneous network contains multiple adjacency matrices and each matrix corre sponds to a relation type from one to another type of objects. It is noteworthy that there are different relation types between papers, we use $A _ { P P ^ { \prime } }$ to represent the adjacency matrix of cite relation between them, and $A _ { P ^ { \prime } P }$ to represent the adjacency matrix of cited-by relation between them.

## 3.2. Generation of meta-path set

A heterogeneous network connects two types of objects through in direct relations called meta-paths that include multiple types of objects and relations [12]. Meta-path is an effective tool to model user prefer ences in a heterogeneous network

A meta-path $M P = O _ { 0 } { \stackrel { R _ { 0 } } {  } } O _ { 1 } { \stackrel { R _ { 1 } } {  } } \cdots { \stackrel { R _ { l - 1 } } {  } } O _ { l }$ is a composite relation $R =$ $R _ { 0 } R _ { 1 } . . . R _ { l - 1 }$ between objects $O _ { 0 } , O _ { 1 } , . . . , O _ { l } ,$ where $O _ { 0 }$ denotes the source type of the meta-path, O denotes the target type of the meta-path, and l is the length.

A path instance is a specific path that follows the object and relation requirement of a meta-path. Since the purpose of this research is to recommend papers to users, we only focus on meta-paths with authors as the source and papers as the target. In an academic heterogeneous network, papers and authors can be connected through different metapaths with different semantic meanings, where user preferences of pa pers are embedded in these meta-paths. For example, a paper that is a reference of a user’s preferred paper can be represented using the metapath $U s e r { \stackrel { l i k e } { \to } } P a p e r { \stackrel { c i t e } { \to } }$ Paper. A paper that has the same author with a user’s preferred paper can be represented as $U s e r { \stackrel { l i k e } { \to } } P a p e r { \xrightarrow { w r i t t e n - b y } } A u t h o r { \stackrel { w r i t e } { \to } }$ Paper. Some other examples are shown in Table 1.

Table 1  
List of meta-paths and semantic meanings

<table><tr><td>Path instance</td><td>Meta-path</td><td>Semantic meaning</td></tr><tr><td> $U_0 \xrightarrow{like} P_0 \xrightarrow{cite} P_2$ </td><td> $User \xrightarrow{like} Paper \xrightarrow{cite} Paper$ </td><td>A paper is a reference of user’s preferred paper</td></tr><tr><td> $U_0 \xrightarrow{like} P_0 \xrightarrow{written-by} A_1 \xrightarrow{write} P_1$ </td><td> $User \xrightarrow{like} Paper \xrightarrow{written-by} Author \xrightarrow{write} Paper$ </td><td>A paper has a same author with user’s preferred paper</td></tr><tr><td> $U_0 \xrightarrow{like} P_0 \xrightarrow{published-in} V_0 \xrightarrow{publish} P_2$ </td><td> $User \xrightarrow{like} Paper \xrightarrow{published-in} Venue \xrightarrow{publish} Paper$ </td><td>A paper published in a same venue with user’s preferred paper</td></tr></table>

A meta-path set is a group of meta-paths, each of which describes a target user’s preferences for a candidate paper. Theoretically, all possible meta-paths between papers and users could be used to make recommendations. However, a longer meta-path may introduce noise to the recommendation model and cause higher computational costs [42]. Therefore, we determine the maximum length L of the meta-path and any meta-path with length l that is less than L is added to the meta-path set.

## 3.3. Recommendation score calculation based on meta-paths

Random walk on meta-path is used to calculate node proximity between start nodes and target nodes through the path. Therefore, we apply random walk on all meta-paths that connect users and papers to calculate recommendation scores.

Because random walk on a constraint meta-path starts from a target user, given user $u ,$ we define user query vector $q _ { u }$ as follows

$$
q _ {u} (i) = \left\{ \begin{array}{l l} 1 & \text { if } i = u \\ 0 & \text { otherwise } \end{array} \right.\tag{2}
$$

where $q _ { u } ( i )$ is the ith item of user query vector $q _ { u } .$ In this vector, user u is set to an initial value 1, while the others are set to 0.

After assigning an initial value to the target user, the target user will transfer the value to its neighbor nodes that follow the next object type on the meta-path. The transition matrix $T _ { M N } = [ t _ { i j } ] _ { m \times n }$ is defined to represent the transition probability from nodes of type M to nodes of type N. A transition matrix can be obtained by normalizing adjacency matrix $A _ { M N } = [ a _ { i j } ] _ { m \times n }$ by columns as follows:

$$
t _ {i j} = \frac {a _ {i j}}{\sum_ {k = 0} ^ {m} a _ {k j}}\tag{3}
$$

where $\scriptstyle \sum _ { k = 0 } ^ { m } a _ { k j }$ is the sum of elements in the column j of the adjacency matrix.

Given the transition matrix and user query vector, we simulate random walk on the constraint meta-path $M P _ { k } ~ =$ $U s e r \overset { R _ { 0 } } { \to } O _ { 1 } \overset { R _ { 1 } } { \to } \cdots \overset { R _ { l - 1 } } { \to }$ Paper. Recommendation vector $r _ { u } ^ { k }$ that consists each paper’s recommendation score to user u on the meta-path k is defined as:

$$
r _ {u} ^ {k} = T _ {P O _ {l - 1}} \cdot \dots \cdot T _ {O _ {1} U} \cdot q _ {u}\tag{4}
$$

where $T _ { P O l - 1 }$ is the transition matrix of papers to node type $O _ { l - 1 }$ , T is the transition matrix of node type $O _ { 1 }$ to users. For any pair of papers $( i , j ) ,$ paper i is more likely to be recommended to user u than paper j $\mathrm { i f } r _ { u } ^ { k } ( i ) >$ $r _ { u } ^ { k } ( j )$ , where $r _ { u } ^ { k } ( i )$ and $r _ { u } ^ { k } ( j )$ are the recommendation scores of paper i and paper j to user u on meta-path k.

## 3.4. Personalized weight learning of meta-paths

A user tends to have different preferences for different meta-paths, which are embedded in the user’s historical preference records. For example, users who prefer papers that have the same research topics to papers they have preferred will find the meta-path $U s e r \stackrel { l i k e d } {  } P a p e r \stackrel { i n c l u d e } {  }$ $T e r m \xrightarrow { i n c l u d e d - b y }$ Paper important. Other users may be interested in the citation of a paper they have preferred and, therefore, the meta-path $U s e r \stackrel { l i k e d } {  } P a p e r \stackrel { c i t e d } {  }$ Paper is more important. For every user, we build a linear function to integrate the recommendation scores between the target user and candidate papers on all meta-paths and the result of the function becomes a global recommendation score. The linear function embodies the principle that users are interested in the papers that have multiple connections with these users and that are connected through important meta-paths emphasized by users. The global recommendation score of each paper to user u is represented in a global score vector $g _ { u }$ as follows:

$$
g _ {u} = \sum_ {k} \alpha_ {u} ^ {k} \cdot r _ {u} ^ {k}\tag{5}
$$

where $\alpha _ { u } ^ { k }$ denotes personalized weight of user u on path $k , r _ { u } ^ { k }$ denotes the recommendation score vector of user u on path k. We then learn a user’s personalized weight for each meta-path $\alpha _ { u } ^ { k }$ by mining the user’s histor ical preferences.

## 3.4.1. Objective function

Different from Xu et al. [42], we apply the Bayesian Personalized Ranking (BPR) optimization framework to construct our objective function [43], which is commonly used in many classification problems.

We consider papers liked by a user as a positive set, denoted as PS, and papers disliked by the user as a negative set, denoted as NS [13]. BPR posits that the scores of the positive papers are higher than those of the negative papers with the best parameters setting. Therefore, we design the objective function for target user u as follows:

$$
\operatorname{maxobj} _ {u} (\alpha) = \frac {\sum_ {i \in P S _ {u}} \sum_ {j \in N S _ {u}} I \left(g _ {u} (i) - g _ {u} (j)\right)}{\left| P S _ {u} \right| \left| N S _ {u} \right|}\tag{6}
$$

where $P S _ { u }$ denotes the positive set of user $u , N S _ { u }$ denotes the negative set of user $u , \vert P S _ { u } \vert$ denotes the size of $P S _ { w } \left| N S _ { u } \right|$ denotes the size of $N S _ { u } , g _ { u } ( i )$ is the global recommendation score of paper i to user u, $g _ { u } ( j )$ is the global recommendation score of paper j to user $u ,$ and I(⋅) is an indicator function that equals to 1 $\mathrm { i f } g _ { u } ( i ) > g _ { u } ( j )$ , and 0 otherwise. As the indicator function is not differentiable, we replace it with a sigmoid function as follows:

$$
\sigma (x) = \frac {1}{1 + e ^ {- x}}\tag{7}
$$

Replacing I(⋅) with $\sigma ( \cdot ) _ { i }$ , we obtain a new objective function as follows:

$$
\operatorname{maxobj} _ {u} (\alpha) = \frac {\sum_ {i \in P S _ {u}} \sum_ {j \in N S _ {u}} \sigma \left(g _ {u} (i) - g _ {u} (j)\right)}{\left| P S _ {u} \right| \left| N S _ {u} \right|}\tag{8}
$$

For each user, few papers are in the positive set while millions of papers are in the negative set. It is time consuming to use all papers in the negative set for parameter learning. Therefore, we select a small number of papers in the negative set, which can reduce the running time without affecting the learning result.

## 3.4.2. Solving the objective function

To find parameter $\alpha _ { u }$ that maximizes the objective function for user u, we adopt the gradient ascent (GA) algorithm for parameter learning. For each user, we update the parameter by following the ascending di rection of the gradient as follows:

$$
\alpha_ {u} ^ {(t + 1)} = \alpha_ {u} ^ {(t)} + \eta \frac {\partial O b j _ {u} (\alpha)}{\partial \alpha}\tag{9}
$$

where η denotes learning rate, $\alpha _ { u } ^ { ( t ) }$ and $\alpha _ { u } ^ { ( t + 1 ) }$ are the parameters of user u at time t and $t + 1$ . The gradient of $O b j _ { u } ( \alpha )$ to parameter α is calculated as:

$$
\frac {\partial o b j _ {u} (\alpha)}{\partial \alpha} = \frac {\sum_ {i \in P S _ {u}} \sum_ {j \in N S _ {u}} \frac {\partial \sigma (\delta_ {i j})}{\partial \delta_ {i j}} \left(\frac {\partial g _ {u} (i)}{\partial \alpha} - \frac {\partial g _ {u} (j)}{\partial \alpha}\right)}{| P S _ {u} | | N S _ {u} |}\tag{10}
$$

where $\begin{array} { r } { \delta _ { i j } = g _ { u } ( i ) - g _ { u } ( j ) } \end{array}$ . We can have $\begin{array} { r } { \sigma ( \delta _ { i j } ) / \partial \delta _ { i j } = e ^ { - ( \delta _ { i j } ) } / ( 1 + e ^ { - ( \delta _ { i j } ) } ) ^ { 2 } } \end{array}$ by deriving the sigmoid function. The derivative $\partial { \dot { g } } _ { u } / \partial \alpha _ { u } ^ { k }$ of each parameter $\alpha _ { u } ^ { k }$ is calculated as:

$$
\frac {\partial g _ {u}}{\partial \alpha_ {u} ^ {k}} = r _ {u} ^ {k}\tag{11}
$$

Note that parameter α must be positive, we set parameter $\alpha _ { u } ^ { k }$ to 0 when it is smaller than 0 during the iteration process. Moreover, when the sum of all parameters $\alpha _ { u } { \mathrm o f }$ user u is not 1, these parameters are normalized so that the sum equals to 1. The learning process stops when the change of parameters $\alpha _ { u }$ of user u between the last two iterations is less than a tolerance rate $\xi .$ After the learning process converges, an optimal parameter $\alpha _ { u }$ can be reached for user u. The procedure is described in Algorithm 1.

Algorithm 1. Personalized weight learning for meta-paths.

```matlab
Algorithm 1. Personalized weight learning for meta-paths
Input: user u, learning rate η, threshold ξ
Output: personalized weight αu
1: t=0;
2: Initialize αu(0);
3: Do until αu(t+1) - αu(t) < ξ;
4 Compute the global ranking score gu(p) of each candidate paper p;
5: Compute ∂gu/∂αu;
6: Update α: αu(t+1) = αu(t) + η ∂Obju(αu(t)/∂α);
7: t=t+1;
8: End
```

## 3.5. Personalized recommendation based on meta-paths

Our recommendation method is based on the principle that users are interested in the papers that both have multiple connections with these users and are connected through important meta-paths emphasized by users. We use a global recommendation score to integrate recommen dation scores between the target user and candidate papers through different meta-paths. Papers are recommended to the target user based on the global recommendation score. Papers that are already preferred by a target user are taken as known preferences and therefore excluded from the list of candidate papers. We calculate the global recommen dation score between a target user and a candidate paper as the sum of all the products of the recommendation score of the candidate paper and the target user’s personalized weight in each meta-path. The global recommendation score of user u and paper p is defined as follows:

$$
g _ {u} (p) = \sum_ {k} \alpha_ {u} ^ {k} \cdot r _ {u} ^ {k} (p)\tag{12}
$$

where k denotes the meta-path, $\alpha _ { u } ^ { k }$ denotes the weight of meta-path k given by user u, r<sup>k</sup>(p) denotes the recommendation score between user u and paper p on meta-path k. All candidate papers for each target user are ranked based on the global recommendation score and a recommenda tion list is generated using a Top-N strategy.

## 4. Experiment

## 4.1. Datasets

We conducted experiments to demonstrate the performance of our proposed paper recommendation method on the Aminer and DBLP datasets. The Aminer dataset contained 2,070,699 papers published from 1950 to 2013, while the DBLP dataset included 2,126,627 papers published from 1936 to 2012. We extracted venues and authors directly from the original datasets that included 263,250 venues and 1,557,147 authors in Aminer and 8686 venues and 1,221,259 authors in DBLP, respectively. We selected ten terms with the highest TF-IDF score from the title and abstract of each paper, which included 735,059 terms in Aminer and 256,214 terms in DBLP. Papers published in the latest year (2014 for Aminer dataset and 2013 for DBLP dataset) were selected as users. The reference list of each user was used for training and testing because the list represented the latest preference record set of re searchers who wrote the papers. After removing users with less than five references, we collected 9398 users in Aminer and 3765 users in DBLP. The statistics of Aminer and DBLP are shown in Table 2.

Data Set Statistics.

<table><tr><td>Datasets</td><td>Aminer</td><td>DBLP</td></tr><tr><td>Nodes</td><td></td><td></td></tr><tr><td>Number of papers</td><td>2,070,699</td><td>2,126,267</td></tr><tr><td>Number of venues</td><td>263,250</td><td>8686</td></tr><tr><td>Number of authors</td><td>1,557,147</td><td>1,221,259</td></tr><tr><td>Number of terms</td><td>735,059</td><td>256,214</td></tr><tr><td>Number of users</td><td>9398</td><td>3765</td></tr><tr><td>Links</td><td></td><td></td></tr><tr><td>Number of paper-papers</td><td>7,858,912</td><td>4,028,245</td></tr><tr><td>Number of paper-venues</td><td>2,070,562</td><td>2,126,267</td></tr><tr><td>Number of paper-authors</td><td>5,171,807</td><td>5,772,357</td></tr><tr><td>Number of paper-terms</td><td>18,742,963</td><td>17,578,799</td></tr><tr><td>Number of paper-users</td><td>158,609</td><td>56,235</td></tr></table>

Table 3  
Weights of meta-paths for the three individual users.

<table><tr><td>User</td><td>Meta-path</td><td>User1</td></tr><tr><td>1</td><td> $User \xrightarrow{like} Paper \xrightarrow{published-in} Venue \xrightarrow{publish} Paper \xrightarrow{cite} Paper$ </td><td>0.984</td></tr><tr><td rowspan="2">2</td><td> $User \xrightarrow{like} Paper \xrightarrow{cite} Paper$ </td><td>0.398</td></tr><tr><td> $User \xrightarrow{like} Paper \xrightarrow{written-by} Author \xrightarrow{write} Paper \xrightarrow{cite} Paper$ </td><td>0.366</td></tr><tr><td rowspan="4">3</td><td> $User \xrightarrow{like} Paper \xrightarrow{cite} Paper$ </td><td>0.445</td></tr><tr><td> $User \xrightarrow{like} Paper \xrightarrow{cited-by} Paper \xrightarrow{cite} Paper \xrightarrow{cite} Paper$ </td><td>0.174</td></tr><tr><td> $User \xrightarrow{like} Paper \xrightarrow{cite} Paper \xrightarrow{liked-by} User \xrightarrow{like} Paper$ </td><td>0.138</td></tr><tr><td> $User \xrightarrow{like} Paper \xrightarrow{cite} Paper \xrightarrow{cite} Paper \xrightarrow{cited-by} Paper$ </td><td>0.114</td></tr></table>

For each user, we randomly divided references into five partitions and conducted experiments following a 5-fold cross validation strategy. In each experiment, we used four partitions for training and the remaining partition for testing. In the personalized weight learning process, the training data of each user was split into two subsets. We used the first half as known preferences and the other half for weight learning.

## 4.2. Evaluation measures

In order to evaluate the performance of our proposed PRHN, we first defined recommendations liked by users as True Positive (TP), and others as False Positive (FP). We also defined papers that were not recommended but liked by users as False Negative (FN), and others as True Negative (TN). Then, we adopted the Top-N recommendation strategy and used two common evaluation metrics, namely, Precision and Recall. The definitions of the evaluation metrics are as follows:

⋅Precision: represents the probability that relevant papers appear in the recommendation list, calculated as:

$$
\text { Precision } = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {T P _ {i}}{T P _ {i} + F P _ {i}}\tag{13}
$$

where n denotes the number of users. TP denotes the number of relevant recommendations that appear in the recommendation list of user i, FP denotes the number of irrelevant recommendations that appear in the recommendation list of user i, and $T P _ { i } + F P _ { i }$ denotes the length of the recommendation list of user i.

⋅Recall: represents the probability that recommended papers appear in the user’s reference list, calculated as:

![](/api/attachments/JUWDD98N/fulltext/images/1356bb91811e81ce3a284e5738aa15781f48722c823a0a43946425b148a73552.jpg)

$$
\text { Recall } = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {T P _ {i}}{T P _ {i} + F N _ {i}}\tag{14}
$$

where $F N _ { i }$ denotes the number of relevant recommendations that do not appear in the recommendation list of user i, and $T P _ { i } + F N _ { i }$ denotes the length of the list of user i.

## 4.3. Baseline methods

We compared PRHN with the following baseline methods:

⋅BC (Bibliographic coupling) [27]: This method measures the simi larity of the reference list of two papers. It is based on the assumption that the more similar two papers’ reference lists, the more similar the papers. Similarity is calculated by calculating the number of the same references between the two papers.

⋅CC(Co-citation) [28]: This method measures how frequently two papers are cited together by other papers. It is based on the assumption that the more two papers are preferred together by others, the more similar they are. It is calculated by counting the number of papers that co-cited the two papers.

⋅MSCN [30]: This method combines citation analysis and network analysis on a multilevel citation network. We first use co-citation and bibliographic coupling to select candidate papers. We then recommend papers according to the sum of degree centrality, closeness centrality, betweenness centrality and Eigenvector centrality of each paper.

⋅CAR [33]: This method incorporates citation relations and re searchers’ historical preferences into a heterogeneous network and ap plies random walk with restart model on the network.

⋅Metapath [42]: This method minimizes the square of the difference between recommendation scores given by the model and a user’s real preference for each paper to learning user’s personalized weights on meta-paths. The object function is shown as follows:

$$
\operatorname{minobj} = \sqrt {\sum_ {i} \sum_ {v} \left(Y _ {i , v} - \sum_ {k} \alpha_ {i} ^ {k} \widehat {Y} _ {i , v} ^ {k}\right) ^ {2}}\tag{15}
$$

where $Y _ { i , \astrosun }$ is 1 if user i likes paper v before, $\alpha _ { i } ^ { k }$ is the personalized weight on meta-path k of user i, $\widehat { \boldsymbol { Y } } _ { i , \nu } ^ { k }$ is the recommendation score of user i and paper v on meta-path k.

## 4.4. Parameter settings

In the parameter learning process, the size of negative set $\begin{array} { r } { | N S _ { u } | , } \end{array}$ threshold ξ, and learning rate η influence parameter learning result and converge speed. We set |NS | to 1000, ξ to 0.001 and η to 1 empirically. For each target user, we observed that the parameters learning process became stable after 20–40 iterations.

![](/api/attachments/JUWDD98N/fulltext/images/6434aca709a6728fb1dfc8da36942903f3a40445aad724ac44b9b782966557cb.jpg)  
Fig. 4. Precision and Recall of PRHN on Aminer with different maximum length L.

![](/api/attachments/JUWDD98N/fulltext/images/2b800031358f25f34acde3d589ed6ca1dc6571d9127246cddf7d0344f9309fe9.jpg)

![](/api/attachments/JUWDD98N/fulltext/images/7817df0b0b5afd644e72bd77ff8c9fa369f24c3a8aaf654855e110923dc05c25.jpg)  
Fig. 5. Precision and Recall of PRHN on DBLP with different maximum length L.

![](/api/attachments/JUWDD98N/fulltext/images/2b5bc2137558d25bf9573cf4a7fb041230aaa9bcb14c032ceb50b778696fe831.jpg)

![](/api/attachments/JUWDD98N/fulltext/images/aafc7b2e9b952e60c79e2cd7c4ec57967b3ba0fe9faa89df328d59fbf3c7eafe.jpg)  
Fig. 6. Precision and Recall of PRHN and baseline methods on Aminer.

![](/api/attachments/JUWDD98N/fulltext/images/a60b2b81a94c29e0c51016759ef21e2e7b42811f03ed977596e8023cd283d3a0.jpg)

![](/api/attachments/JUWDD98N/fulltext/images/026d40963e149377a42ce5c0413f8ce15dc935ae247aeeb2fb8cb256405468bb.jpg)  
Fig. 7. Precision and Recall of PRHN and baseline methods on DBLP.

After learning users’ personalized weights, we observed that users preferences for meta-paths were different, which indicated diverse user preference patterns. Table 3 shows the most influential meta-paths for three users. The first user assigned almost a full percentage on $U s e r \overset { l i k e } {  } P a p e r \overset { p u b l i s h e d - i n } { \longrightarrow } V e n u e \overset { p u b l i s h } {  } P a p e r \overset { c i t e } {  } P a p e r ,$ which meant that this meta-path played a key role when this user selected papers of interest. The second user assigned almost the same weight on $U s e r { \stackrel { l i k e } { \to } } P a p e r { \stackrel { c i t e } { \to } }$ Paper and $U s e r \overset { l i k e } {  } P a p e r \overset { w r i t t e n - b y } {  } A u t h o r \overset { w r i t e } {  } P a p e r \overset { c i t e } {  } P a p e r ,$ which meant that this user was likely to select papers of interest based on these two meta-paths. Differently, the third user assigned a high value on $U s e r \overset { l i k e } {  } P a p e r \overset { c i t e } {  } P a p e r ,$ and lower values on three meta-paths.

## 4.5. Impact of maximum meta-path length

As stated in Section 3.2, the maximum meta-path length L influences method performance by constraining the meta-paths used for recom mendations. A small L will lead to poor performance because many important meta-paths are excluded from the model. However, a large L will lead to a high computational cost, which will affect the efficiency of recommendations. We first conducted experiments using different values of L(i.e., 2, 3 and 4) to find the best value of Lfor the two datasets. Fig. 4 and Fig. 5 show the results using different maximum length L on Aminer and DBLP. Fig. 4 shows that PRHN achieved better precision and recall when L was 4 on Aminer. Fig. 5 shows that PRHN achieved better precision and recall when L was 3 on DBLP. Therefore, to achieve better recommendation performance without compromising efficiency, we set L to 4 on Aminer and 3 on DBLP for the rest of the experiments.

## 4.6. Recommendation performance

Fig. 6 shows the Top-N recommendation performance of PRHN and other baseline methods on Aminer. The results indicated that PRHN was better than other baseline methods in terms of precision and recall. Fig. 6(a) shows that the highest precision of PRHN reached 16.4% when N was 1, which was 1.2% higher than the second best method CAR. Fig. 6(b) shows that the recall of PRHN was approximately similar to CAR but was much higher than other baseline methods.

Fig. 7 shows the Top-N recommendation performance based on DBLP. The results were almost the same as those on Aminer. Fig. 7(a) shows that the highest precision of PRHN reached 17.9% when N was 1, which was 3.8% higher than the second best method CAR. Fig. 7(b) shows that the highest recall of PRHN was 25.5% when N was 10, which was 1.2% higher than the second best method CAR.

In summary, PRHN significantly outperformed other methods in terms of precision and recall on both datasets. Compared with CAR, which was based on random walk with the restart model, PRHN discovered personalized preference patterns on the heterogeneous network for each individual user. Metapath preformed worse than PRHN because it used the accurate recommendation score of each paper for personalized weight learning, which was not necessary and would lead to poor recommendation. CC and BC performed worse than PRHN because they were based on a single perspective (meta-path). MSCN had a worse performance because it was based on popularity other than similarity.

## 5. Conclusion

In this paper, we propose PRHN, a paper recommendation method that is based on the heterogeneous network and can effectively recom mend papers based on a user’s historical preferences. Unlike prior studies [29,30], our method integrates multiple types of objects and relations to construct a heterogeneous network. To explore user pref erences, we generate a meta-path set and use random walk on a metapath to calculate the recommendation score between the target user and candidate papers on each meta-path. Then, we develop a person alized weight learning process based on Bayesian Personalized Ranking to learn user preferences of meta-paths. Finally, we recommend paper to each user by combining the similarity between the target user and candidate papers and user’s personalized weights on each meta-path. Experiments were conducted on Aminer and DBLP to compare PRHN with several baseline methods. The experimental results showed that PRHN outperformed other baseline methods in terms of precision and recall.

There are some limitations in our research. First, our research relies heavily on a user’s historical preferences in order to discover user preference patterns and provide new recommendations. Recommenda tion performance may suffer when analyzing data from new users or those with few activities on the web. Second, a user’s recent preferences and previous preferences are considered to have the same impacts on their current interests in our model. However, previous preferences should have less impact than recent ones, because researchers may change their research directions as they continuously read papers. Third, our research only uses offline evaluations with implicit feedback to evaluate recommendation performance. It is worth incorporating the proposed method into real applications to understand a user’s explicit response to recommended papers.

There might be three directions for future research. First, future research can integrate more objects and relations into the heterogeneous network for user preference mining, such as research topics, author af filiations, and their relations with other objects in the network. Second, the rich semantic information in the heterogeneous network has not been fully explored, such as popularity finding and expert finding. Third, as researchers continuously read papers and change their research di rections as time evolves, future research can work on how to have a continuous learning dimension on the personalized weight and make adaptive recommendations based on time.

## Acknowledgments

This research is supported by research grant from the Key Program of National Natural Science Foundation of China (No.71631003).

## References

[11 J. Lu. D.S. Wu. M.S. Mao. W. Wang. G.O. Zhang. Recommender system application developments: a survey, Decis. Support. Syst. 74 (2015) 12–32.

[2] M. Gorgoglione, U. Panniello, A. Tuzhilin, Recommendation strategies in personalization applications, Inf. Manag. 56 (2019) 103143.

[3] S. Yang, M. Korayem, K. Aljadda, T. Grainger, S. Natarajan, Combining contentbased and collaborative filtering for job recommendation system: a cost-sensitive statistical relational learning approach, Knowl.-Based Syst. 136 (2017) 37–45.

[4] M. Reusens, W. Lemahieu, B. Baesens, L. Sels, A note on explicit versus implicit information for job recommendation, Decis. Support. Syst. 98 (2017) 26–35

[5] J.T. Ren, J.W. Long, Z.K. Xu, Financial news recommendation based on graph embeddings, Decis. Support. Syst. 125 (2019) 113115.

[6] C. Lin, R.Q. Xie, X.J. Guan, L. Li, T. Li, Personalized news recommendation via implicit social experts, Inf. Sci. 254 (1) (2014) 1–18.

[7] S.K. Lee, Y.H. Cho, S.H. Kim, Collaborative filtering with ordinal scale-based implicit ratings for mobile music recommendations, Inf. Sci. 180 (11) (2010) 2142–2155.

[8] W.P. Lee, C.T. Chen, J.Y. Huang, J.Y. Liang, A smartphone-based activity-aware system for music streaming recommendation, Knowl.-Based Syst. 131 (2017) 70–82.

[9] W.L. Chang, C.F. Jung, A hybrid approach for personalized service staff recommendation, Inf. Syst. Front. 19 (2017) 149–163.

[10] G. Tian, J. Wang, K.Q. He, D.G. Sun, Y. Tian, Integrating implicit feedbacks for time-aware web service recommendations, Inf. Syst. Front. 19 (2017) 75–89.

[11] J. Beel, B. Gipp, S. Langer, C. Breitinger, Research-paper recommender systems: a

[12] C. Shi, Y.T. Li, J.W. Zhang, Y.Z. Sun, P.S. Yu, A survey of heterogeneous information network analysis, IEEE Trans. Knowl. Data Eng. 29 (1) (2015) 17–37.

[13] T.A.N. Pham, X.T. Li, G. Cong, Z.J. Zhang, A general recommendation model for heterogeneous networks. JEEE Trans. Knowl. Data Eng, 28 (12) (2016) 3140–3153

[14] Y. Xiong, Y. Zhu, P.S. Yu, Top-k similarity join in heterogeneous information networks, JEEE Trans, Knowl. Data Eng, 27 (6) (2015) 1710–1723

[15] J. Tang, J. Zhang, L. Yao, J. Li, L. Zhang, Z. Su, ArnetMiner: extraction and mining of academic social networks, in: Proceedings of the Fourteenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2008, pp. 990–998.

[16] G. Adomavicius, A. Tuzhilin. Toward the next generation of recommender systems a survey of the state-of-the-art and possible extensions. JEEE Trans. Knowl. Data Eng, 17 (6) (2005) 734–749.

[17] T.P. Liang, Y.F. Yang, D.N. Chen, Y.C. Ku. A semantic-expansion approach to personalized knowledge recommendation, Decis. Support. Syst. 45 (3) (2008) 401-412.

[18] S.S. Weng, H.L. Chang, Using ontology network analysis for research document recommendation, Expert Syst. Appl. 34 (3) (2008) 1857–1869.

[19] X.Y. Tang, Q.T. Zeng, Keyword clustering for user interest profiling refinemen within paper recommender systems, J. Syst. Softw. 85 (1) (2012) 87–101.

[20] W.D. Zhao, R. Wu, H. Liu, Paper recommendation based on the knowledge gap between a researcher’s background knowledge and research target, Inf. Process. Manag. 52 (5) (2016) 976–988.

[21] M.S. Pera, Y.K. Ng, Exploiting the wisdom of social connections to make personalized recommendations on scholarly articles, J. Intell. Inf. Syst. 42 (3) (2014) 371–391.

[22] X.Y. Li, T.F. Chen, B. Pettit, M.D. Rijke, Personalised reranking of paper recommendations using paper content and user behavior, ACM Trans. Inf. Syst. 37 (3) (2019) 1–23.

[23] J.S. Sun, J. Ma, Z.Y. Liu, Y.J. Miao, Leveraging content and connections for scientific article recommendation in social computing contexts, Comput. J. 57 (9) (2014) 1331–1342.

[24] K. Sugiyama, M.Y. Kan, A comprehensive evaluation of scholarly paper 91–109.

[25] C.H. Lai, D.R. Liu, C.S. Lin, Novel personal and group-based trust models in

[26] G. Wang. X.R. He. C.I. Ishuga. HAR-SI: a novel hybrid article recommendatior approach integrating with social information in scientific social network. Knowl.- Based Svst 148 (2018) 85–99

[27] M.M. Kessler, Bibliographic coupling between scientific papers, Am. Doc. 14 (1) (1963) 10–25.

[28] H.G. Small, Co-citation in the scientific literature: a new measure of the

[29] J.D. West, I. Wesley-Smith, C.T. Bergstrom, A recommendation system based on hierarchical clustering of an article-level citation network, IEEE Trans. Big Data 2 (2) (2016) 113–123.

[30] J. Son, S.B. Kim, Academic paper recommender system using multileve simultaneous citation networks, Decis. Support. Syst. 105 (2018) 24–33.

[31] W. Huang, Z. Wu, C. Liang, P. Mitra, C.L. Giles, A neural probabilistic model for context based citation recommendation, in: Proceedings of the Twenty-ninth Aaai Conference on Artificial Intelligence, 2015, pp. 2404–2410.

[32] S.Y. Hwang, C.P. Wei, C.H. Lee, Y.S. Chen, Coauthorship network-based literature recommendation with topic model, Online Inf, Rev, 41 (3) (2017) 318–336.

[33] H.F. Liu, Z. Yang, I. Lee, Z.Z. Xu, S. Yu, F. X, CAR: Incorporating filtered citation relations for scientific article recommendation. in: 2015 IEEE International Conference on Smart City/SocialCom/SustainCom (SmartCity). 2015. 513-518S

[34] F. Xia, H.F. Liu, I. Lee, L.B. Cao, Scientific article recommendation: exploiting common author relations and historical preferences, IEEE Trans. Big Data 2 (2) (2016) 101–112.

[35] G. Tian, L. Jing, Recommending scientific articles using bi-relational graph-based iterative RWR, in: Proceedings of the Seventh ACM Conference on Recommender Systems, 2013, pp. 399–402.

[36] X.Y. Cai, J.W. Han, W.J. Li, R.X. Zhang, S.R. Pan, L.B. Yang, A three-layered mutually reinforced model for personalized citation recommendation, IEEE Trans. Neural Netw. Learn. Syst. (2018) 1–12.

[37] M. Danaf, F. Becker, X. Song, B. Atasoy, M. Ben-Akiva, Online discrete choice models: applications in personalized recommendations, Decis. Support. Syst. 119 (2019) 35–45.

[38] J.M. Gao, C.X. Zhang, Y.Y. Xu, M.Q. Luo, Z.D. Niu, Hybrid microblog recommendation with heterogeneous features using deep neural network, Expert Syst. Appl. (2020), https://doi.org/10.1016/j.eswa.2020.114191 forthcoming.

[39] R.R. Wang, X. Ma, C. Jiang, Y. Ye, Y. Zhang, Heterogeneous information networkbased music recommendation system in mobile networks, Comput. Commun. 150 (2020) 429–437.

[40] Y.Q. Qiao, X.Y. Luo, C.L. Li, H.C. Tian, J.T. Ma, Heterogeneous graph-based join representation learning for users and POIs in location-based social network, Inf. Process. Manag. 57 (2) (2020), https://doi.org/10.1016/j.ipm.2019.102151 forthcoming.

[41] X. Zhou, G.B. Guo, Z. Sun, Y. Liu, Multi-facet user preference learning for finegrained item recommendation, Neurocomputing 385 (2020) 258–268.

[42] Y.H. Xu, D.N. Zhou, J. Ma, Scholar-friend recommendation in online academic communities: an approach based on heterogeneous network, Decis. Support. Syst. 119 (2019) 1–13.

[43] S. Rendle, C. Freudenthaler, Z. Gantner, BPR: Bayesian personalized ranking from implicit feedback. in: Proceedings of the Twenty-fifth Conference on Uncertainty Artificial Intelligence. 2009, pp. 452–461.

Yi Li received the B.Sc. degree in information management and information system from Tianjin University, Tianjin, China, in 2018. She is currently working toward the M.S. degree in management science and engineering from the College of Management and Economics, Tianjin University, Tianjin, China. Her current research interests include personalized recommendation and data mining

Ronghui Wang received the B.Sc. degree in information management and information system from Hebei University of technology, Tianjin, China, in 2017. She is currently pursuing the Ph.D. degree in management science and engineering from the College of Management and Economics, Tianjin University, Tianjin, China. Her current research in terests include platform business models and ominichannel retailing. Her paper has appeared in IEEE Transactions on Engineering Management. She has also presented her work at the Pre-ICIS Workshop on e-Business and the China Summer Workshop on In formation Management (CSWIM).

Guofang Nan (gfnan@tju.edu.cn) is a professor of information systems at the College of Management and Economics, Tianjin University, China. He received his Ph.D. from Tianjin University. Dr. Nan’s current research interests include diverse areas of information sys tems, decision support systems, and information economics. He has published more than 50 papers in such journals as Information Systems Research, Journal of Management In formation Systems, Journal of the Association for Information Systems, and Decision Support Systems.

Dahui Li is a professor of MIS at the University of Minnesota Duluth. He received his Ph.D in MIS from Texas Tech University. His current research focuses on business-to-consumer relationships, online communities, and technology innovation. He has had papers pub lished in the Communications of the ACM, Decision Sciences, Decision Support Systems, Information & Management, Journal of the Association for Information Systems, Journal of Product Innovation Management. and elsewhere

Minqiang Li is a professor of information systems at the College of Management and Economics, Tianjin University. He received the Ph.D. from the College of Management and Economics, Tianjin University in 2000. His research interests include management science and decision support, IT strategy, electronic commerce, data mining, and intelligent sys tems. His papers have appeared in MIS Quarterly, Journal of Management Information Systems, European Journal of Operational Research, IEEE Transactions on Engineering Management, and Information Sciences
