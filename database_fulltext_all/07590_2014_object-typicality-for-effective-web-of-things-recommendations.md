---
otero_id: 7590
otero_key: "9A4FG392"
title: "Object typicality for effective Web of Things recommendations"
authors: "Yi Cai; Raymond Y.K. Lau; Stephen S.Y. Liao; Chunping Li; Ho-Fung Leung; Louis C.K. Ma"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Object typicality for effective Web of Things recommendations

Yi Cai <sup>a</sup>, Raymond Y.K. Lau <sup>b,</sup>⁎, Stephen S.Y. Liao <sup>b</sup>, Chunping Li <sup>c</sup>, Ho-Fung Leung <sup>d</sup>, Louis C.K. Ma <sup>e</sup>

<sup>a</sup> School of Software Engineering, South China University of Technology, China

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Hong Kong Special Administrative Region

<sup>c</sup> School of Software, Tsinghua University, 100084 Beijing, China

<sup>d</sup> Department of Computer Science and Engineering, The Chinese University of Hong Kong, China

<sup>e</sup> SCOPE, City University of Hong Kong, Hong Kong Special Administrative Region

## a r t i c l e i n f o

Available online xxxx

Keywords: Object typicality Recommender systems Situation awareness Web of Things

## a b s t r a c t

With the rapid growth of “Web of Things” (WoT), there is a pressing need to develop effective mechanisms for the intelligent discovery and selection of these things (items). Recommender systems are viable solutions to address the issue of WoT discovery and selection. However, classical recommender systems are weak in handling sparse recommendation spaces which characterize most WoT recommendations. Moreover, classical recommender systems may not be able to scale up to ef<sup>fi</sup>ciently process a large number of things on the Web, and yet these systems may produce big-error recommendations that diminish users' trusts on utilizing WoT. The main contribution of our research is the design and development of a novel recommendation method which is underpinned by the principle of object typicality veri<sup>fi</sup>ed in the <sup>fi</sup>eld of cognitive psychology to address the aforementioned issues related to WoT recommendations. Based on the MovieLens benchmark data set, our experimental results show that the proposed recommendation method is effective and produces the least big-errors. Since the proposed method exploits data generalization by operating at item group and user group level during recommendation time, it is more effective and ef<sup>fi</sup>cient than other baseline methods given sparse training data. Based on the Net<sup>fl</sup>ix benchmark data set that simulates a large WoT recommendation space, the proposed method also signi<sup>fi</sup>cantly outperforms state-of-the-art recommendation methods in terms of Mean Absolute Error (MAE). The business implication of our research is that the proposed recommendation method can enhance the situation awareness of WoT applications which facilitate the reuse of enterprise resources and the interoperability among enterprises.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The transition from the Social Web to the Semantic Web has triggered increasingly more physical devices (i.e., smart things) such as RFID chips, wireless sensors, actuators, and mobile phones to be connected to the digital world for the development of useful realworld applications on the Internet (i.e., the “Internet of Things”) [12]. More recently, the vision of “Web of Things” (WoT) leads to the design of more sophisticated applications or services by interconnecting any objects through the Web layer (e.g., interconnecting via the HTTP protocol) [8,12]. For example, a movie recommendation service (i.e., a smart thing) is connected to a sensor installed at a cinema; a new WoT application is then composed to timely inform users once tickets of the recommended movies are nearly sold out at that cinema.

However, it has been pointed out that the emerge of a large number of smart things on the Web causes great dif<sup>fi</sup>culties to computers as well as humans to <sup>fi</sup>nd, select, and utilize smart things in an effective way [11,25]. Due to the problem of information overload [19,38,47], it is extremely dif<sup>fi</sup>cult for Web users to develop the situation awareness about the huge number of things initiated on the Web everyday. Accordingly, there is a pressing need to examine the issue of smart things discovery and selection on the Web. Since recommender systems have been shown to be viable solutions for the discovery and selection of services on the Web [49], this paper focuses on the design and development of a novel recommendation method that can facilitate users (humans or machines) to discover and select relevant smart things. For example, the proposed WoT recommendation service can autonomously suggest some useful things to users based on their previous usage experience and the preferences of other like-minded users.

A large body of research about recommender systems has been performed in the past two decades. Existing recommender systems are usually classi<sup>fi</sup>ed under one of the three broad categories, namely collaborative <sup>fi</sup>ltering (CF) [17,36], content-based recommendation (CB) [28,33], and hybrid recommendation [2,24,27]. Content-based recommendation methods suggest items to a user based on similar items s/he having consumed before. On the other hand, collaborative <sup>fi</sup>ltering methods recommend items to a user based on the preferences of similar users. Hybrid recommendation methods represent a modelbased or heuristic-based combination of the aforementioned recommendation methods. Although these recommendation methods have been widely used in electronic commerce, they are faced with the following challenges for WoT recommendations:

• First, data sparsity is a big challenge given few ratings for a large number of items on the Web.

• Second, computational ef<sup>fi</sup>ciency is another concern given the sheer volume of information about user preferences and items on the Web. Nevertheless, it is desirable for recommender systems to generate recommendations in real-time to facilitate the timely compositions of WoT applications.

• Third, existing recommender systems may generate big-error predictions. In other words, some items suggested by a recommender system are very different from the actual preferences of a user. These big-error predictions diminish users' trusts on WoT applications.

The main contribution of the research work presented in this paper is that we exploit the principle of “object typicality” extensively studied in the <sup>fi</sup>eld of cognitive psychology [9] to develop a novel, cognitively motivated recommendation method called Recommendation based On Typicality (ROT) to address the aforementioned issues arising in WoT recommendations, and hence to improve the situation awareness of WoT applications. Since recommender systems deal with human perceptions about objects, there is a distinct advantage of designing recommender systems grounded in the principle of human cognition. To the best of our knowledge, this is the <sup>fi</sup>rst successful design of a cognitively motivated recommender system to enhance WoT recommendations. In particular, ROT exploits high-level item- and user-based similarities to facilitate WoT recommendations. The basic intuition of the proposed method is that a “typical” user of a speci<sup>fi</sup>c user interest group should be recommended “typical” items that the group is most interested in. For example, a typical user of the “war movies” interest group tends to prefer the typical movies (e.g., “The Longest Day”) characterizing the interests of the group.

More speci<sup>fi</sup>cally, the proposed ROT method <sup>fi</sup>rst exploits the natural partitions of items of a given recommendation space to establish item groups. Then, the user interest group pertaining to each item group is identi<sup>fi</sup>ed. Finally, items are recommended to a user according to a novel typicality-based computational mechanism that exploits the user's fuzzy memberships pertaining to various user interest groups and the typical items characterizing each of these groups. Pragmatically, items are recommended according to the match between user groups and item groups at execution time. In other words, the ROT method operates at a high level of data granularity (data generalization) [47]. This is a novel way on how ROT addresses the issues of data sparsity and computational complexity arising in WoT recommendations.

The remainder of the paper is organized as follows. Section 2 discusses related research of recommender systems and compares existing work with our proposed approach. The computational details about the proposed object typicality based recommendation method are illustrated in Section 3. In Section 4, we discuss the results of our empirical experiments based on the MovieLens data set<sup>1</sup> and the Net<sup>fl</sup>ix data set.<sup>2</sup> We then summarize the main characteristics of the proposed ROT method in Section 5. Finally, we offer concluding remarks and describe future directions of our research work.

## 2. Related work

## 2.1. Research on object typicality

Psychologists have found that people are more interested in typical objects than atypical ones when a concept (i.e., a category of objects)

is referred to [29]. According to the prototypical view of concepts, each concept is represented by the best prototype capturing the salient properties of objects belonging to that category [26]. Vanpaemel et al. [42] extended the prototypical view of concepts by developing methods to identify the prototypes of a concept based on typical objects. In particular, an object is considered to be an instantiation from the most similar abstraction (prototype). Barsalou [3] proposed two quantitative measures, namely central tendency and frequency of instantiation to estimate the typicality of an object with respect to a given concept. Central tendency refers to the degree of an object's “family resemblance”. An object is considered to have a high central tendency if it is similar to other members of the same category and it is different from the members of other categories. On the other hand, frequency of instantiation refers to the frequency of an object being referred to by people when a speci<sup>fi</sup>c concept is examined. If an object is often used as an exemplar for a concept, it has a high frequency of instantiation, and therefore it is considered a typical one with respect to that concept.

Rifqi [34] proposed a computational method to estimate object typicality in large databases. In particular, the typicality of an object is estimated according to its resemblance to other members of the same category and its dissimilarities to the members of other categories. Lesot et al. [21] developed a similar computational method in the context of fuzzy systems. Desclés and Pascu [6] applied the notion of object typicality to construct new quanti<sup>fi</sup>ers for natural language processing and common sense reasoning. Cai and Leung [5] formalized object typicality with reference to an ontology. Hua et al. [14] applied the principle of object typicality to develop a typicality-based query operator that enhances the effectiveness of query processing in databases.

## 2.2. Recommender systems

The assumption of content-based recommender systems is that people prefer items similar to those that they positively evaluate before. For content-based recommender systems, the central issue is to examine computational methods for learning user pro<sup>fi</sup>les and measuring item similarity. For example, Pazzani and Billsus [33] applied the naive Bayes classi<sup>fi</sup>er to construct a user pro<sup>fi</sup>le that captured “relevant” and “nonrelevant” Web pages for the user. Mooney and Roy [28] developed the LIBRA system for the recommendations of books. A detailed account of content-based recommender systems is provided by Pazzani and Billsus [32].

On the other hand, collaborative <sup>fi</sup>ltering-based recommender systems suggest items to a user based on the preferences of other likeminded users. Since the collaborative <sup>fi</sup>ltering approach does not require well-structured item descriptions, it has been widely used to recommend a variety of items including images, videos, and music [1]. For example, GroupLens [17] and PHOAKS [40] were developed based on the collaborative <sup>fi</sup>ltering approach. The user-based CF approach <sup>fi</sup>rst identi<sup>fi</sup>es the nearest “neighbors” of a user by exploiting the user similarity relations. Then, the system predicts the rating of an unrated item based on the ratings given by these nearest “neighbors” [13]. Moreover, Zheng et al. [49] developed a user-based CF approach for the discovery and selection of Web services. In contrast, item-based CF approach recommends items to a user based on other users' ratings of similar items. More speci<sup>fi</sup>cally, an item-based CF system <sup>fi</sup>rst identi<sup>fi</sup>es the nearest “neighbors” of an unrated item by examining the item similarity relations. Then, the system predicts the rating of the unrated item based on other users' ratings assigned to these nearest “neighbors” of items [7,36].

Hybrid recommender systems combine CB- and CF-based approaches to address the limitations of individual recommendation method [2,27,37]. Melville et al. [27] applied a content-based approach to augment a user-item rating matrix, and then used a collaborative <sup>fi</sup>ltering ap proach to generate the <sup>fi</sup>nal recommendations. Xue et al. [46] developed a cluster-based Pearson Correlation Coef<sup>fi</sup>cient method (SCBPCC) that exploited both item similarity and user similarity in collaborative <sup>fi</sup>ltering. Wang et al. [43] proposed the similarity fusion method to unify user- and item-based CF methods. Ma et al. [24] proposed an effective missing data prediction (EMDP) method that leveraged the advantages of both item- and user-based CF approaches. Recently, Li et al. [22] developed a transfer learning-based recommendation method by means of the extraction of cross-domain contextual information. Kim et al. [16] proposed a collaborative <sup>fi</sup>ltering approach to enrich user modeling for more personalized recommendations. Xu et al. [45] combined social network analysis and semantic concept analysis to facilitate personalized researcher recommendations.

## 2.3. Differences between the proposed ROT method and existing method

The proposed ROT method is grounded in the sound principle of object typicality which has been veri<sup>fi</sup>ed based on numerous empirical tests in the <sup>fi</sup>eld of cognitive psychology [26,29,42]. In addition, the principle of object typicality has been successfully applied to enhance user query processing in database systems [14]. The basic intuition of the proposed ROT method is that a typical user of a speci<sup>fi</sup>c user interest group should be recommended typical items that the user group is most interested in. The proposed ROT method differs from existing contentbased recommendation approach in that it does not directly recommend new items to a user based on the items s/he positively rated before. Moreover, it differs from CF-based recommendation approach in that it does not need to compute the “nearest neighbors” of an individual user when a recommendation for that user is generated. In contrast, the ROT method represents each user by a typicality vector which captures the user's typicality degrees with respect to various user interest groups. The user typicality vectors and user groups are constructed by means of an off-line system training process.

The ROT method is different from economic choice models in that it generates recommendations based on the typicality of a user with respect to various user interest groups and the typical items that these groups prefer instead of the joint statistical distributions of item properties and user preferences. Pragmatically, ROT operates at item group and user group level rather than individual user and item levels during recommendation time. This is a unique way on how the proposed ROT method addresses the issues of data sparsity and computational ef<sup>fi</sup>ciency for WoT recommendations. Moreover, there is a good potential for the ROT method to address the problem of big-error predictions due to the sound principle of object typicality. It should be noted that the proposed ROT method differs from clustering-based CF methods such as SCBPCC [46] in that ROT applies data clustering to identify item groups and user groups, whereas SCBPCC invokes clustering processes to predict missing ratings. Though the proposed ROT method utilizes item descriptions to construct item groups, it does not involve extra data processing when compared to existing CB and hybrid methods which also leverage item descriptions to generate recommendations.

## 3. The computational model for typicality-based recommendations

In this section, we illustrate the computational details of the proposed typicality-based recommendation model which predicts users' ratings on items based on both user typicality and item typicality. The concept of typicality provides a sound mechanism to rank items in a way that is close to human perception [9,29]. Since the main functionality of recommender systems is to predict users' preferences about items, it is desirable to design recommender systems that can imitate the way how people evaluate real-world items.

## 3.1. The computational apparatus of object typicality

To illustrate the computational apparatus of the proposed typicalitybased recommendation method, we <sup>fi</sup>rst formally de<sup>fi</sup>ne items, item groups, users, and user groups, respectively. Let U and O denote a set of users and a set of items (objects). Each item is represented by some properties. For example, a movie is represented by directors, actors, and country of production, whereas a Web service is represented by the service provider, service quality, expected response time, and so on. It should be noted that an item can be represented by any properties rather than restricting to keywords. Formally, each item is represented by an item vector as follows.

## De<sup>fi</sup>nition 1. Item vector

An item $O _ { i }$ is represented by a vector of property–value pair such as $\vec { p } _ { 0 _ { i } } = \left. \left( p _ { 0 _ { i } , 1 } : l _ { 0 _ { i } , 1 } \right) , \left( p _ { 0 _ { i } , 2 } : l _ { 0 _ { i } , 2 } \right) , \cdots , \left( p _ { 0 _ { i } , n } : l _ { 0 _ { i } , n } \right) \right.$ where $l _ { O _ { i } , j } { \in } [ 0 , 1 ]$ indicates the fuzzy degree of $\mathbf { \bar { \rho } } _ { O _ { i } }$ possessing the property $p _ { 0 _ { i } , j } . \operatorname { I f } l _ { 0 _ { i } , j } = 0$ is established, it indicates that item $O _ { i }$ does not possess propert $\tt V P o  _ { i } , \it j$ at all, whereas $l _ { O _ { i } , j } = 1$ suggests that $O _ { i }$ de<sup>fi</sup>nitely possesses property $p _ { O _ { i } , j } .$

For example, a computer $O _ { i }$ is represented by an item vector ${ \vec { p } } _ { 0 _ { i } } =$ b (‘has intelCPU’: 1), …, (‘has wideScreen’: 0.8) N. For the proposed computational method, a set of fuzzy clusters is <sup>fi</sup>rst constructed based on all the items under consideration. Each fuzzy cluster is called an item group which consists of similar items. An item belongs to some fuzzy clusters with various degrees. For example, ${ \vec { p } } _ { 0 _ { i } } = <$ (‘has intelCPU’: 1), …, (‘has wideScreen’: 0.8) N may belong to the item group “desktop computer” and the item group “netbook” with various degrees. From a cognitive perspective, each item group represents a concept of a speci<sup>fi</sup>c domain. Formally, an item group is represented by a fuzzy cluster which is underpinned by the theory of fuzzy sets [48]. Essentially, each cluster is represented by the same set of properties (e.g., keywords). However, each cluster owns these properties with various degrees (i.e., fuzzy memberships). An item group is de<sup>fi</sup>ned as follows.

## De<sup>fi</sup>nition 2. Item group

An item group $k _ { j }$ is a fuzzy cluster of similar objects represented by: $k _ { j } = \left\{ O _ { 1 } ^ { w _ { j , 1 } } , O _ { 2 } ^ { w _ { j , 2 } } , \cdots , O _ { m } ^ { w _ { j , m } } \right\}$ where m represents the number of items; $O _ { i }$ is an item, and $w _ { j , i }$ is the typicality degree of item $O _ { i }$ for the cluster $k _ { j } .$

Formally, the construction of fuzzy clusters is represented by a mapping function $( \mathrm { i . e . }$ , a fuzzy membership function): $m : { \cal O } \times { \cal K } \mapsto [ 0 , 1 ] ,$ where O is a set of items and $K = \{ k _ { 1 } , k _ { 2 } , \cdots , k _ { n } \}$ is a set of clusters. The term n denotes the number of clusters induced based on the natural patterns of the set of items O. The term $w _ { j , i }$ denotes the typicality degree (i.e., fuzzy membership) of an item $O _ { i }$ for the item group $k _ { j } .$ For the proposed ROT method, different clustering methods can be applied to construct the fuzzy clusters (i.e., item groups) [23,44]. However, the search for the most effective clustering method given a speci<sup>fi</sup>c domain will be left as part of our future work. If a clustering method is effective, the semantic distances among different fuzzy clusters tend to be large (i.e., the overlapping among item groups is small).

According to the prototypical view of concepts [5,29], each item group can also be represented by a single prototype induced based on the set of object instances described by the corresponding concept. For a computer-based implementation of concept prototype, previous research work has proposed using a prototype vector to represent a concept prototype which is an abstraction of a group of similar objects [5,29,42]. A prototype vector is induced based on the set of similar objects described by the concept. For example, a prototype vector can be composed based on the mean, median, or mode vector derived from the set of object (item) vectors of a specific category (concept) [21,29]. Formally, a prototype vector is de<sup>fi</sup>ned as follows.

## De<sup>fi</sup>nition 3. Prototype vector

A prototype vector $\vec { t } _ { k _ { j } } = \left. \left( p _ { k _ { j } , 1 } : r _ { k _ { j } , 1 } \right) , \left( p _ { k _ { j } , 2 } : r _ { k _ { j } , 2 } \right) , \cdots , \left( p _ { k _ { j } , m } : r _ { k _ { j } , m } \right) \right.$ is a vector of property–value pairs which represent the prototype of an item group $k _ { j } .$ The term m denotes the number of properties of the

Y. Cai et al. / Decision Support Systems xxx (2013) xxx–xxx

prototype $k _ { j } ,$ and $r _ { k _ { j } , i } \in [ 0 , 1 ]$ represents the fuzzy degree of k possessing the property $p _ { k _ { j } , i } .$

For the special case, if $r _ { k _ { i } , i } = 0$ holds, it means that the item group $k _ { j }$ does not possess the property $p _ { k _ { i } , i }$ at all. In contrast, if $r _ { k _ { j } , i } = 1$ holds, it suggests that $k _ { j }$ de<sup>fi</sup>nitely possesses the property $p _ { k _ { i } , i }$ . For the set of users U, each individual user may have speci<sup>fi</sup>c favorites or preferences for some kinds of items (i.e., item groups). For instance, a user Bob may be interested in “Horror” movies, while his wife Amy may prefer “Adventure” movies, and yet their son Tom likes “Thrillers” movies. For each induced item group $k _ { i } ,$ the proposed recommendation method constructs a fuzzy set [48] of users who like the corresponding item group. Within a user interest group $g _ { i } \subset U ,$ , each user $U _ { x } \in g _ { i }$ is interested in the group of items to various degrees. For example, Bob likes “Horror” movies to a higher degree than Tom does. The set of users pertaining to an item group $k _ { i }$ is called a user group $g _ { i } ,$ and it is represented by a fuzzy set. The semantics of g is that it describes the set of users who like the particular item group $k _ { i } .$ The membership of each member $U _ { x } \in g _ { i }$ indicates the typicality degree of $U _ { x }$ with respect to g . The fuzzy membership of $U _ { x }$ for g is called the user typicality. The rationale of using fuzzy sets to represent item groups and user groups is that an item may belong to multiple item groups and a user may also have multiple interests pertaining to different user interest groups in the real-world.

## De<sup>fi</sup>nition 4. User group

A user group ${ { g } _ { i } } = \left\{ U _ { 1 } ^ { { { V } _ { i , 1 } } } , U _ { 2 } ^ { { { V } _ { i , 2 } } } , \cdots , U _ { m } ^ { { { V } _ { i , m } } } \right\}$ is a fuzzy set of users who like the corresponding item group $k _ { i \cdot }$ The term m denotes the number of users of the group $g _ { i } ,$ and $U _ { x }$ represents a user. The term $\nu _ { i , x } \in [ 0 , 1 ]$ (i.e., fuzzy membership) is the typicality degree of the user $U _ { x }$ for the user group g .

There are four important components of the proposed recommender system, namely items, users, item groups, and user groups. Fig. 1 shows the relationships between these four components. For each item, it has different typicality degrees with respect to the item groups. Similarly, each user has different typicality degrees with respect to different user groups. It should be noted that item groups are <sup>fi</sup>rst constructed via a chosen clustering method, and then the user group pertaining to each item group is composed. An item $O _ { i }$ may have a fuzzy membership $w _ { j , i } > 0$ for multiple item groups, whereas a user $U _ { x }$ may also have a fuzzy membership $\begin{array} { r } { \boldsymbol { v } _ { i , \ast } } \end{array}$ $_ x > 0$ for multiple user groups.

According to the principle of “object typicality”, a “typical” user of a speci<sup>fi</sup>c user interest group should be recommended “typical”

![](/api/attachments/9A4FG392/fulltext/images/2e36d3e9cb86d106799d779ccc62baef1d367de8b2929c5a24ff3aa68994c06c.jpg)

$$
U _ {i} - \text { User } i \quad g _ {i} - \text { User   Groups } i \quad k _ {i} - \text { Item   Group } i \quad O _ {i} - \text { Item } i
$$

$\tau _ { g _ { i } } ( U _ { y } )$ – typicality of user $U _ { y }$ in the user group gi

$\tau _ { k _ { j } } ( O _ { x } )$ – typicality of item Ox in the item group kj

Fig. 1. The relationships among items, item groups, users, and user groups of the ROT model.

items that the user group is most interested in. Therefore, the recommendation strategy of the proposed ROT method is that if an item $O _ { i }$ is a typical (atypical) item of the item group $k _ { j } ,$ and a user $U _ { j }$ is a typical (atypical) user of the user group $g _ { j }$ that corresponds to the item group $k _ { j } ,$ item $O _ { i }$ should be recommended to the user $U _ { j }$ with a high (low) recommendation score. In this case, the pair $( k _ { j } , g _ { j } )$ (i.e., the matching item group and user group) represents a speci<sup>fi</sup>c “recommendation context” discovered via un-supervised item clustering and user clustering. Formally, the recommendation score of $O _ { i }$ for $U _ { j }$ is estimated via the typicality-based recommendation function RS $\big ( \dot { \vec { o } } _ { i } , \vec { U } _ { j } \big ) : { \cal O } { \times } U { \mapsto } [ 0 , 1 ]$ , where O is a set of items represented by the corresponding item group vectors, and U is a set of users represented by the corresponding user group vectors. More speci<sup>fi</sup>cally, the proposed recommendation function RS should observe the following axioms.

Axiom 1. For a user $U _ { j }$ and an item $O _ { i } ,$ if ∀ x, $\begin{array} { r } { \nu _ { x , j } = 0 , } \end{array}$ then $R S ( \vec { o } _ { i } , \vec { U } _ { j } ) = 0 .$

Axiom 2. For a user $U _ { j }$ and an item $O _ { i } ,$ if ∃ x, $\nu _ { x , j } = 1$ and $w _ { x , i } = 1$ , then $R S ( \vec { o } _ { i } , \vec { U } _ { j } ) = 1$

Axiom 3. For a user $U _ { j }$ and two items $O _ { x }$ and $O _ { y } , \mathrm { i f } \exists k _ { i } : w _ { i , x } > w _ { i , y } ,$ , and $\forall h \neq i : w _ { h , x } = w _ { i , y } ,$ then $R S \big ( \vec { o } _ { x } , \vec { U } _ { j } \big ) { > } R S \big ( \vec { o } _ { y } , \vec { U } _ { j } \big )$

Axiom 4. For two users $U _ { x }$ and $U _ { y }$ and one item $O _ { i } , \operatorname { i f } \exists g _ { j } : \nu _ { j , x } > \nu _ { j , y }$ , and $\forall h \neq j : \nu _ { h , x } = \nu _ { h , y } ,$ then $R S ( \vec { o } _ { i } , \mathbf { \vec { U } } _ { x } ) { > } R S ( \vec { o } _ { i } , \vec { U } _ { y } )$

Axioms 1 and 2 specify the boundary cases of generating the recommendation scores. If a user does not like any item groups at all $( \mathrm { i . e . }$ , the user is not typical in any user group), it means that the user does not like any items for all item groups, and so the recommendation score of any item for the user should be zero. For a user $U _ { j }$ and an item $O _ { i } , \det U _ { j }$ likes an item group $k _ { x }$ with the highest degree $( \mathrm { i } . \mathsf { e } . , U _ { j }$ is the most typical user of the user group $g _ { x } )$ , and $O _ { i }$ is the most typical item of the item group $k _ { x } ,$ the ROT system should recommend $O _ { i }$ to $U _ { j }$ with the highest recommendation score. On the other hand, Axioms 3 and 4 specify the in<sup>fl</sup>uence of user typicality degrees from user groups and item typicality degrees from item groups, respectively. If an item is more typical for some item groups, and a user is more typical for the corresponding user groups, the ROT system should recommend the item to the user with a relatively high recommendation score. Accordingly, we propose a novel typicality-based recommendation function RS that observes all the aforementioned axioms.

$$
R S \left(\vec {o} _ {i}, \vec {u} _ {j}\right) = \frac {\sum_ {x = 1} ^ {n} w _ {x , i} \cdot v _ {x , j}}{n}\tag{1}
$$

The term n represents the number of item groups (also the number of user groups). Moreover, $w _ { x , i }$ is the typicality degree of the item $O _ { i }$ for the item group $k _ { x } ,$ , and $\nu _ { x , j }$ is the typicality degree of the user $U _ { j }$ for the user group $g _ { x }$ that corresponds to the item group $k _ { x } .$ As can be seen, the proposed RS function is underpinned by the typicality degrees of items and the typicality degrees of users. The computational details of deriving these typical degrees will be illustrated in Sections 3.2 and 3.3, respectively. It should be noted that Eq. (1) does not rate an item based on the average rating (i.e., simply recommending popular items to a user). In contrast, it takes a user's speci<sup>fi</sup>c interests into account by evaluating their typicality with respect to various user interest groups. Even though Eq. (1) produces a recommendation score that falls in the unit interval, the proposed ROT system can simply invoke a linear conversion function ϑ : [0,1] ↦ [Min, Max] that maps the unit interval to any desirable range [Min, Max] of recommendation scores for a variety of WoT recommendation applications.

## 3.2. Estimating typicality degrees of items in item groups

Previous research in the <sup>fi</sup>eld of cognitive psychology shows that central tendency (i.e., an object's similarity to a concept prototype) is

Please cite this article as: Y. Cai, et al., Object typicality for effective Web of Things recommendations, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.008

one of the main factors that largely in<sup>fl</sup>uences an object's typicality with respect to a concept [4,5]. When the principle of object typicality is applied to design the proposed recommender system for WoT recommendations, the central tendency of an item (i.e., an object) with respect to an item group $( \mathrm { i . e . } ,$ a concept) is estimated based on the similarity between the corresponding item vector and prototype vector of the item group. More speci<sup>fi</sup>cally, the central tendency of an item is estimated based on its internal similarity and external dissimilarity [3,5]. Internal similarity refers to the similarity between an object and the prototype of the corresponding concept, whereas external dissimilarity is the distance between the object and the prototypes of other concepts. As discussed in Section 3.1, objects and prototypes of concepts are represented by the corresponding item vectors and prototype vectors of item groups. Conceptually, a similarity function sim is applied to map the product of the set of items and the set of prototypes of item groups to the unit interval: sim : $P \times T \mapsto [ 0 , 1 ]$ , where T is a set of prototype vectors of item groups, and P is a set of property vectors of items. For each pair of item vector ${ \vec { p } } _ { O _ { i } } { \in } P$ and prototype vector $\vec { t _ { c } } { \in } T$ , if sim $\left( \vec { t } _ { C } , \vec { p } _ { O _ { i } } \right) = 1$ is established, it means that the item $O _ { i }$ is certainly typical with respect to the prototype c of the item group $k _ { j } .$ On the other hand, if sim $\left( \vec { t } _ { c } , \vec { p } _ { 0 _ { i } } \right) = 0$ is true, it suggests that item $O _ { i }$ is totally atypical with re-<sup>¼</sup>spect to the prototype c of the item group $k _ { j } .$

For the proposed ROT method, any standard similarity functions discussed in the literature can be used [35]. For the implementation of our current prototype system, we employ the following similarity function:

$$
s i m \Big (\overrightarrow {p} _ {O _ {i}}, \overrightarrow {t} _ {c} \Big) = \left\{ \begin{array}{l l} 0 & \forall k, \exists l _ {O _ {i}, k} = 0 \\ \kappa & \text { otherwise } \end{array} \right.\tag{2}
$$

$$
\kappa = e x p \left(- \left(\sqrt {\sum_ {k = 1} ^ {n} \left| r _ {c , k} - l _ {O _ {i} , k} \right| ^ {2}}\right) ^ {\theta}\right)\tag{3}
$$

where n represents the number of properties of the universe of discourse. The term $l _ { 0 _ { i } , k }$ represents the degree to which item $O _ { i }$ possesses the property $p _ { { 0 _ { i } } , \mathrm { i } }$ , while $r _ { c , k }$ indicates the degree to which prototype c possesses the property $p _ { c , k }$ . The parameter $\theta \in R ^ { + }$ is a positive real number which is applied to tune the rate of decay of the exponential function so that the proposed similarity function is effective for different recom-

mendation applications. The Euclidean distance $\sqrt { \sum _ { k = 1 } ^ { n } \left| r _ { c , k } - l _ { O _ { i } , k } \right| ^ { 2 } }$ is applied to estimate the similarity between an item vector $\overrightarrow { p } _ { O _ { i } }$ and a prototype vector $\overrightarrow { t } _ { c }$ . The proposed exponential function produces a high typicality degree if an item is extremely close to a prototype. On the other hand, the resulting typicality degree substantially decreases if the item is only moderately similar to the prototype [29].

The internal similarity of an item O with respect to the prototype c of an item group is computed according tosim<sub>in</sub> $\left( \vec { p } _ { 0 _ { i } } , \vec { t } _ { c } \right) = s i m \left( \vec { p } _ { 0 _ { i } } , \vec { t } _ { c } \right)$ . In addition, the external dissimilarity dissim $e x t \left( \overrightarrow { p } _ { O _ { i } } , \overrightarrow { t } _ { c } \right)$ <sup>¼</sup>is taken as the average of dissimilarities between the item and other prototypes excluding the current one. More speci<sup>fi</sup>cally, the external dissimilarity between an item $O _ { i }$ and the prototype c of an item group is de<sup>fi</sup>ned as follows:

$$
\operatorname{dissim} _ {\text { ext }} \left(\vec {p} _ {O _ {i}}, \vec {t} _ {c}\right) = \frac {\sum_ {x \in C / \{c \}} \operatorname{dissim} \left(\vec {p} _ {O _ {i}} , \vec {t} _ {x}\right)}{| C | - 1}\tag{4}
$$

where C is the set of prototypes of the item groups for a given recommendation domain. For the dissimilarity function dissim, it is de-<sup>fi</sup>ned by dissim $\left( \vec { p } _ { 0 _ { i } } , \vec { t } _ { c } \right) = 1 - s i m \Big ( \vec { p } _ { 0 _ { i } } , \vec { t } _ { c } \Big )$ . Finally, the central tendency of an item with respect to an item group is estimated based on an aggregation function that combines the internal similarity and external dissimilarity [21]. More speci<sup>fi</sup>cally, we propose the following aggregation function to estimate central tendency ct of an item $O _ { i }$

$$
\tau_ {k _ {j}} (O _ {i}) \approx c t \left(\vec {p} _ {O _ {i}}, \vec {t} _ {c}\right) = s i m _ {i n t} \left(\vec {p} _ {O _ {i}}, \vec {t} _ {c}\right) \cdot d i s s i m _ {e x t} \left(\vec {p} _ {O _ {i}}, \vec {t} _ {c}\right)\tag{5}
$$

For the proposed ROT method, each item has a typicality degree against each item group. Accordingly, an item typicality matrix is needed to characterize item typicality. Formally, an item typicality matrix is de<sup>fi</sup>ned as follows:

## De<sup>fi</sup>nition 5. Item typicality matrix

An item typicality matrix $M _ { I K }$ captures the typicality degree for each item $O _ { i }$ against each item group k<sub>j</sub> of a recommendation domain, and it has the form:

$$
M _ {I K} = \left\{ \begin{array}{c} \left(k _ {1}: w _ {1, 1}\right), \left(k _ {2}: w _ {2, 1}\right), \dots , \left(k _ {n}: w _ {n, 1}\right) \\ \dots \\ \left(k _ {1}: w _ {1, m}\right), \left(k _ {2}: w _ {2, m}\right), \dots , \left(k _ {n}: w _ {n, m}\right) \end{array} \right\}
$$

where $\nu _ { j , i } = \tau _ { k _ { i } } ( O _ { i } )$ is the typicality degree of item $O _ { i }$ for the item group $k _ { j } .$

## 3.3. Estimating typicality degrees of users in user groups

For the proposed ROT method, estimating the typicality degrees of users with respect to various user groups is also an important procedure. Similar to the item typicality matrix, a user typicality matrix captures the typicality degrees of a user against various user groups.

## De<sup>fi</sup>nition 6. User typicality matrix

A user typicality matrix $M _ { I G }$ captures the typicality degree for each user U against each user group g of a recommendation domain, and it has the form:

$$
M _ {I G} = \left\{ \begin{array}{c} \left(g _ {1}: v _ {1, 1}\right), \left(g _ {2}: v _ {2, 1}\right), \dots , \left(g _ {n}: v _ {n, 1}\right) \\ \dots \\ \left(g _ {1}: v _ {1, m}\right), \left(g _ {2}: v _ {2, m}\right), \dots , \left(g _ {n}: v _ {n, m}\right) \end{array} \right\}
$$

where $\nu _ { j , i } = \tau _ { g _ { j } } ( U _ { i } )$ is the typicality degree of user $U _ { i }$ for the user group $g _ { j } .$

In order to estimate the typicality degree of a user for each user group, we need to interpret the principle of central tendency in the context of typical user group formation. In particular, a user interest group $g _ { j }$ is constructed with respect to a speci<sup>fi</sup>c item group $k _ { j }$ (i.e., the items generally preferred by the group of users). Under such a circumstance, if a user $U _ { i }$ often rates the items of $k _ { j } ,$ s/he has the tendency to prefer these items. Consequently, s/he is likely to be the typical member of the corresponding user interest group $g _ { j } .$ In fact, it reveals $U _ { i } " s$ central tendency in $g _ { j } .$ . Moreover, if the user $U _ { i }$ highly rates the items of $k _ { j } ,$ it also shows their tendency of preferring those items. As a result, $U _ { i }$ has a high central tendency in $g _ { j } .$ Accordingly, we estimate the central tendency, and hence the typicality degree of a user $U _ { i }$ with respect to a user group $g _ { j }$ based on the frequency of U rating each item $O _ { i } \in k _ { j }$ and the rating that U speci<sup>fi</sup>es for $O _ { i } \in k _ { j }$ . Formally, these two factors are expressed by ${ s _ { g } ^ { i } } _ { j } , f$ and $s _ { g _ { j } , r } ^ { i } ,$ , respectively:

$$
s _ {g _ {j}, f} ^ {i} = \frac {N _ {j , i}}{\sum_ {y = 1} ^ {n} N _ {y , i}}\tag{6}
$$

$$
s _ {g _ {j}, r} ^ {i} = \frac {\sum_ {y = 1} ^ {N _ {j , i}} w _ {j , y} \cdot R _ {i , y}}{N _ {j , i} \cdot R ^ {\max}}\tag{7}
$$

Please cite this article as: Y. Cai, et al., Object typicality for effective Web of Things recommendations, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.008

where n is the total number of item groups. The term $N _ { j , i }$ represents the number of items that user $U _ { i }$ has rated for an item group $k _ { j } . R _ { i , y }$ is the rating that $U _ { i }$ assigns to the item $O _ { y } \in k _ { j } .$ The term $w _ { j , y }$ represents the typicality degree of $O _ { y }$ for the item group $k _ { j } ,$ and $R _ { \mathrm { m a x } }$ is the maximal rating value for any items.

Finally, the typicality degree $\nu _ { j , i } = \tau _ { g _ { i } } ( U _ { i } )$ of a user $U _ { i }$ for a user group $g _ { j }$ <sup>¼ ð Þ</sup>is approximated by the aggregation of the above two measures through a standard convex function. The weight factor $\alpha = 0 . 5$ is speci<sup>fi</sup>ed to assign equal weight for $S _ { g _ { i } , f } ^ { i }$ and $s _ { g _ { i } , r } ^ { i } ,$ , respectively. The proposed user typicality function has the property that if the user $U _ { i }$ often assign high rating values for the items $O _ { i } \in k _ { j } ,$ U<sub>i</sub>'s typicality degree for the user group $g _ { j }$ that corresponds to $k _ { j }$ will be high.

$$
\tau_ {g _ {j}} (U _ {i}) \approx \alpha \cdot s _ {g _ {j}, f} ^ {i} + (1 - \alpha) \cdot s _ {g _ {j}, r} ^ {i}\tag{8}
$$

## 4. System evaluation

In this section, we discuss the experiments that evaluate the performance of the proposed typicality-based recommendation method when compared to that of state-of-the-art recommendation methods. In particular, we try to answer the following research questions by running two series of experiments:

1. How does item clustering affect the recommendation quality of the proposed ROT method?

2. Does the proposed ROT method produce less big-error predictions when compared to existing recommendation methods?

3. Does the proposed ROT method achieve good performance given sparse training data?

4. Is the proposed ROT method more ef<sup>fi</sup>cient than some classical recommendation methods?

5. Is the proposed ROT method effective when compared to state-ofthe-art recommendation methods?

## 4.1. Evaluation data sets

Since a benchmark data set speci<sup>fi</sup>cally constructed for the evaluation of WoT recommender systems is not available, we applied the common MovieLens [24,36] and Net<sup>fl</sup>ix [18] data sets to evaluate the effectiveness of the proposed ROT prototype system. The MovieLens data set we used contains 100,000 ratings generated by 943 users for 1682 movies. Each user has rated at least 20 movies, and the ratings are in the range between 1 (bad) and 5 (excellent). The sparsity level of this data set is $\begin{array} { r } { 1 - \frac { 1 0 0 , 0 0 0 } { 9 4 3 \times 1 , 6 8 2 } = 0 . 9 3 6 9 . } \end{array}$ . We downloaded the descriptions of movies from the IMpB movie site.³ Then, the properties of the movies (items) were identi<sup>fi</sup>ed by extracting the corresponding keywords from these descriptions. Since only the descriptions of 1334 movies were available, we used this subset of movies in our experiments. In addition, we also evaluated the ROT system based on a subset of the Net<sup>fl</sup>ix data set which contained 100,480,507 ratings offered by 480,189 users for 17,770 movies. The sparsity level of our Net<sup>fl</sup>ix data set is $\begin{array} { r } { 1 - \frac { 1 0 0 , 4 8 0 , 5 0 7 } { 4 8 0 , 1 8 9 \times 1 7 , 7 7 0 } = 0 . 9 8 8 2 . } \end{array}$

## 4.1. Performance metrics

To measure the accuracy of the experimental system, we adopted the Mean Absolute Error (MAE) which is de<sup>fi</sup>ned as the average absolute difference between the system predicted ratings and the actual user ratings [1]. MAE is commonly used by researchers to evaluate the effectiveness of recommender systems, and so it is easy to compare our experimental results with published results. Formally, MAE is de<sup>fi</sup>ned by:

$$
\mathrm{MAE} = \frac {\sum_ {i = 1} ^ {n} | f _ {i} - h _ {i} |}{n}
$$

where n is the number of recommendations. $f _ { i }$ is the user-speci<sup>fi</sup>ed rating, and $h _ { i }$ is the prediction provided by a recommender system. If the MAE score is low, it suggests that the recommender system can predict users' ratings with a high accuracy.

Another common metric for the evaluation of recommender systems is root mean square error (RMSE). Since the errors are squared before they are averaged, the RMSE measure is more sensitive to big-error predictions when compared to the MAE measure. In general, the RMSE score achieved by a recommender system is always greater than or equal to its MAE score. The greater difference between the MAE score and the RMSE score achieved by a system, the larger variance of the individual errors produced by the system will be. Formally, the RMSE measure is de<sup>fi</sup>ned as follows.

$$
\mathrm{RMSE} = \sqrt {\frac {\sum_ {i = 1} ^ {n} \left| f _ {i} - h _ {i} \right| ^ {2}}{n}}
$$

## 4.2. The experimental procedures

For all the experiments reported in this paper, we applied the topic modeling based clustering method to generate item groups [39]. After the clustering process, a prototype vector was extracted for each cluster (i.e., item group). In particular, the top k most probable (typical) keywords were applied to construct each prototype vector after the probabilistic topic modeling process was invoked. For our experiments, the parameter k = 20 was empirically established. Table 1 shows the sample prototype vector for the “crime movie” item group generated by means of a topic modeling process [39]. According to our empirical observation, relevant keywords often appear in movie descriptions. As a result, topic modeling processes tend to extract useful topics that characterize different types of movies. However, we do not make a claim that topic modeling is the best clustering method. Searching for the most effective clustering method for a given domain will be left as part of our future work. After the construction of item groups, the user group corresponding to each item group was constructed according to the computational method illustrated in Section 3.3. To answer the aforementioned research questions, we performed two series of experiments.

The objective of the <sup>fi</sup>rst series of experiments was to examine the impact of the number of item groups and the sparsity of training data on the recommendation quality of the proposed ROT prototype system. In addition, the computational ef<sup>fi</sup>ciency of the ROT system was evaluated when compared to several classical recommender systems. The classical recommender systems involved in our experiments included a content-based recommender system (CB) that used the cosine similarity function to compute item similarity, a user-based collaborative <sup>fi</sup>ltering system (UBCF) that employed the Pearson Correlation Coef<sup>fi</sup>cient to compute user similarity, an item-based collaborative <sup>fi</sup>ltering system (IBCF) that used Pearson Correlation Coef<sup>fi</sup>cient to compute item similarity, a naive hybrid recommender system, and a collaborative <sup>fi</sup>ltering system that supported missing data prediction (EMDP) [24]. For these experiments, we divided the whole data set into two parts namely, a training set and a test set. Each system under testing was <sup>fi</sup>rst trained using the training set, and then its performance was evaluated based on the test set. We applied 5-fold cross-validation to compute the average MAE and RMSE scores for each system. To assess ROT's performance under the condition of sparse training data, various divisions of the training and the test sets were tried [36]. For instance, a splitting ratio $x = 0 . 8$ indicates that 80% of the evaluation data are randomly selected to build the training set and the remaining 20% of data are used to create the test set.

The Prototype of the Item Group “Crime Movies”.

<table><tr><td>Properties</td><td>Membership</td><td>Properties</td><td>Membership</td></tr><tr><td>Murder</td><td>0.9830</td><td>Police</td><td>0.8216</td></tr><tr><td>Prison</td><td>0.3689</td><td>Suicide</td><td>0.3662</td></tr><tr><td>Revenge</td><td>0.3642</td><td>Serial-killer</td><td>0.3628</td></tr><tr><td>Courtroom</td><td>0.3612</td><td>Obsession</td><td>0.3030</td></tr><tr><td>Investigation</td><td>0.2564</td><td>Lawyer</td><td>0.2404</td></tr><tr><td>Robbery</td><td>0.1830</td><td>Police-officer</td><td>0.1216</td></tr><tr><td>Fugitive</td><td>0.1089</td><td>Judge</td><td>0.1066</td></tr><tr><td>Chase</td><td>0.1042</td><td>Confession</td><td>0.0982</td></tr><tr><td>Deception</td><td>0.0961</td><td>Smoking</td><td>0.0933</td></tr><tr><td>Gunfight</td><td>0.0864</td><td>Escape</td><td>0.0840</td></tr></table>

For the second series of experiments, we compared the performance of ROT with that of state-of-the-art recommender systems based on both the MovieLens [24,36] and the Net<sup>fl</sup>ix [18] benchmark data sets. The state-of-the-art recommender systems included cluster-based Pearson Correlation Coef<sup>fi</sup>cient (SCBPCC) [46], Weighted Low-rank $\mathsf { A p - }$ proximation (WLR) [30], and Transfer Learning-based Collaborative Filtering (CBT) [22]. Similar to previous research [22,24], we extracted a subset of 500 users from the MovieLens data set. For instance, we randomly selected the <sup>fi</sup>rst 100, 200 and 300 users from the benchmark data set to build different training sets such as ML100, ML200, and ML300, respectively. The remaining 200 users were then applied to build the test set. Moreover, similar to previous research, three different sizes of the observed ratings such as 5 ratings (Given5), 10 ratings (Given10), and 15 ratings (Given15) were applied to compute user similarity for each user [22,24]. To better simulate a WoT recommendation environment, the larger and more sparse Net<sup>fl</sup>ix data set was applied to further evaluate the performance of the ROT system. Based on this larger benchmark data set, we compared the performance of ROT with that of other state-of-the-art recommender systems such as SVD [31], ${ \mathrm { S V D } } + + [ 1 8 ] ,$ , and socialMF [15] which were made available via the publicly accessible MyMediaLite library [10].

## 4.3. Experimental results

For the proposed ROT system, determining the number of item groups (clusters of items) is an important design issue. For topic modeling based conceptual clustering, perplexity is a common measure applied to estimate a reasonable number of clusters with respect to the natural partitions of a given data set [41]. Accordingly, we empirically established an appropriate number of item groups K based on the movie descriptions pertaining to the MovieLens data set. In general, a small perplexity value implies that the learned model (e.g., the derived

![](/api/attachments/9A4FG392/fulltext/images/d858d1c75a87f8fbd813c4ac087aad1d91279e002122e33907442e44c9a3b306.jpg)  
Fig. 2. Perplexity vs. number of item groups

## Table 2

Sensitivity of MAE w.r.t. K and training/test ratios.

<table><tr><td></td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>K=10</td><td>0.8291</td><td>0.7804</td><td>0.7722</td><td>0.7664</td><td>0.7624</td></tr><tr><td>K=15</td><td>0.8176</td><td>0.7774</td><td>0.7611</td><td>0.7587</td><td>0.7529</td></tr><tr><td>K=20</td><td>0.8231</td><td>0.7806</td><td>0.7689</td><td>0.7645</td><td>0.7582</td></tr><tr><td>K=25</td><td>0.8262</td><td>0.7843</td><td>0.7688</td><td>0.7654</td><td>0.7607</td></tr><tr><td>K=30</td><td>0.8308</td><td>0.7850</td><td>0.7686</td><td>0.7657</td><td>0.7624</td></tr><tr><td>K=35</td><td>0.8414</td><td>0.7887</td><td>0.7754</td><td>0.7675</td><td>0.7645</td></tr></table>

clusters) has a high predictive power [41]. We tried different numbers of topics and computed the corresponding perplexities. Fig. 2 shows our experimental results; it seems that $K \in [ 1 5 , 2 8 ]$ leads to lower perplexity values. We then adopted the range of $K \in [ 1 0 , 3 5 ]$ to establish the number of item groups for the proposed ROT system. For each chosen K value, we applied a different training/test splitting ratio $x \in [ 0 . 1 , 0 . 9 ]$ to simulate different data sparsity conditions. Finally, 5- fold cross-validation was applied to compute the MAE and the RMSE scores achieved by the ROT system. Tables 2 and 3 report the MAE and the RMSE scores achieved by the ROT system with respect to various numbers of item groups and training/test splitting ratios.

Our experimental results show that both the number of item groups K and the training/test splitting ratio have an impact on the system's recommendation performance. For example, both the MAE and the RMSE scores are the lowest when $K = 1 5$ is applied. The MAE and the RMSE scores slightly increase when K is deviated from 15 (e.g., $K = 1 0$ and $K = 2 0 )$ However, the absolute differences of the MAE and the RMSE scores are small after a reasonable range of K values are established. Accordingly, we applied the empirically established parameter value (e.g., $K = 1 5 )$ to the remaining experiments. On the other hand, more training data (e.g., $x = 0 . 9 )$ lead to better recommendation performance, that is, a lower MAE or RMSE score. Although the proposed empirical method may not be able to identify the optimal number of item groups, applying more sophisticated methods such as genetic algorithms [20] for parameter tuning will only further improve the performance of the proposed ROT system reported in this paper. However, more sophisticated parameter tuning will be left as part of our future work.

## 4.3.2. Recommendation quality

We performed a comparative evaluation of the performance of ROT when compared to that of classical recommender systems under different training/test splitting ratios. Figs. 3 and 4 show the comparative MAE and RMSE performance of the experimental and the baseline systems. It is obvious that the proposed ROT system outperforms all the baseline systems for both MAE and RMSE under various training/test splitting ratios. For example, ROT achieves 0.7529 and 1.0327 for MAE and RMSE, respectively for a training/test splitting ratio $x = 0 . 9 ,$ while EMDP (the best baseline system) achieves 0.8040 and 1.0826, respectively. Under a testing/test splitting ratio of $x = 0 . 3$ , ROT achieves 0.7774 and 1.0705 for MAE and RMSE, while the best performing baseline system IBCF achieves 0.8803 and 1.1544, respectively. This experimental result indicates that the recommendation quality of the ROT system is higher than that of classical recommender systems.

Tables 4 and 5 depict the details of MAE and RMSE improvements achieved by the proposed ROT system. When compared to the EMDP baseline system, the performance improvement achieved by ROT

Sensitivity of RMSE w.r.t. K and training/test ratios.

<table><tr><td></td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>K=10</td><td>1.1290</td><td>1.0703</td><td>1.0592</td><td>1.0526</td><td>1.0442</td></tr><tr><td>K=15</td><td>1.1161</td><td>1.0705</td><td>1.0434</td><td>1.0451</td><td>1.0327</td></tr><tr><td>K=20</td><td>1.1234</td><td>1.0705</td><td>1.0524</td><td>1.0463</td><td>1.0365</td></tr><tr><td>K=25</td><td>1.1203</td><td>1.0719</td><td>1.0523</td><td>1.0503</td><td>1.0454</td></tr><tr><td>K=30</td><td>1.1272</td><td>1.0781</td><td>1.0563</td><td>1.0491</td><td>1.0425</td></tr><tr><td>K=35</td><td>1.1440</td><td>1.08174</td><td>1.0636</td><td>1.0528</td><td>1.0487</td></tr></table>

Please cite this article as: Y. Cai, et al., Object typicality for effective Web of Things recommendations, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.008

Table 4

![](/api/attachments/9A4FG392/fulltext/images/b9d6b001beaa6561c0d391f2a9aa075cced373724355cb4ef1cff8f018857a76.jpg)  
Fig. 3. Comparative MAE performance of ROT.

reduces with the increment of the training/test splitting ratio. However, when compared to the IBCF and the CB baseline systems, ROT achieves a larger performance improvement with the increment of the training/ test splitting ratio. For the training/test splitting ratio x N = 0.4, ROT outperforms the best baseline system EMDP by at least 6.35% in terms of MAE, and at least 4.6% in terms of RMSE. On the other hand, for training/test splitting ratio x b 0.4, IBCF is the best performing baseline system. ROT outperforms IBCF by at least 9.89% in terms of MAE and at least 5.67% in terms of RMSE. According to paired one-tail t -tests, all the performance improvements achieved by the ROT system are statistically signi<sup>fi</sup>cant.

## 4.3.3. The impact of sparse training data

Figs. 3 and 4 also highlight an interesting property of the ROT system in that it achieves the best MAE and RMSE scores when compared to other baseline systems even with a low training/test splitting ratio (i.e., sparse training data). For instance, ROT achieves a MAE score of 0.8176 and a RMSE score of 1.1161 for the lowest training/test splitting ratio x = 0.1. The EMDP baseline system achieves similar results only when suf<sup>fi</sup>cient training data is available (e.g., a training/test splitting ratio x = 0.7). Such a characteristic of ROT is desirable for a WoT recommendation environment where little user ratings (i.e., training data) are available given a huge user-item recommendation space.

The reason of such a signi<sup>fi</sup>cant performance improvement of ROT over other baseline systems is that it is dif<sup>fi</sup>cult for collaborative <sup>fi</sup>ltering based systems to accurately identify the nearest “neighbors” for each user given sparse training data (e.g., commonly rated items). As a result, the recommendation accuracy of these systems is generally low. In contrast, the ROT system relies on the item typicality of item groups and the user typicality of user groups to generate a recommendation. The construction of item groups does not rely on any rated training data at all. Consequently, the proposed ROT system is less susceptible to sparse training data. From a cognitive perspective, the proposed typicalitybased recommendation method operates based on the sound object typicality principle in that the typical user of a speci<sup>fi</sup>c user interest group should be recommended the typical items that the user group is most interested in. From a computational perspective, the proposed typicality-based recommendation method mainly operates at the group level rather than individual item or user level. More speci<sup>fi</sup>cally, item groups are matched with user groups in order to generate recommendations during the recommendation time. This can be seen as a kind of “generalization” approach to address the data sparsity issue of WoT recommendations.

![](/api/attachments/9A4FG392/fulltext/images/eff9ebb37b0e86fbdea72c4bd789919acbaad730674a49e64c7ff5009f47be0c.jpg)  
Fig. 4. Comparative RMSE performance of ROT.

Comparative MAE improvements of ROT under different training/test ratios.

<table><tr><td></td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>EMDP</td><td>17.56%</td><td>14.92%</td><td>9.64%</td><td>8%</td><td>6.35%</td></tr><tr><td>CB</td><td>14.17%</td><td>17.09%</td><td>18.54%</td><td>18.78%</td><td>19.34%</td></tr><tr><td>IBCF</td><td>9.89%</td><td>11.69%</td><td>12.08%</td><td>12.1%</td><td>12.03%</td></tr><tr><td>UBCF</td><td>11.77%</td><td>12.27%</td><td>11.55%</td><td>10.53%</td><td>9.63%</td></tr><tr><td>Naive hybrid</td><td>19.08%</td><td>20.62%</td><td>14.97%</td><td>12.91%</td><td>11.39%</td></tr></table>

## 4.3.4. Big-error predictions

As mentioned before, big-error predictions produced by recommender systems can seriously harm users' trusts on recommender systems. For this experiment, we evaluated the big-errors produced by the ROT and other baseline systems. For the MovieLens data set, a rating value between 1 and 5 is assigned to an item. So, the biggest prediction error is 4. Fig. 5 shows the comparison of the prediction errors (PE) committed by the ROT and other baseline systems. Our experimental result was obtained with 15 item groups (K = 15) and a training/test splitting ratio of x = 0.9. The legend PE = 0 means that there is no prediction error, and PE = 4 implies that the difference between a system predicted rating and the actual user rating is 4 (the big-error). As shown in Fig. 5, the proposed ROT system produces the most correct predictions (e.g., 38.58% predictions with PE = 0) and the most small errors (48.92% predictions with PE = 1) among all the systems. Besides, the ROT system only generates 0.05% predictions with PE = 4 (the bigerrors). As a whole, ROT generates 12.5% prediction errors for PE 2, while the EMDP and the CB baseline systems produce 16% and 29% prediction errors at the same level. The IBCF, UBCF and Naive Hybrid baseline systems all produce 17% or above prediction errors at the same level. It is obvious that the proposed ROT system produces the least big-error predictions when compared to other baseline systems. For other training/test splitting ratios (i.e., x b 0.9), similar results were observed. For the reason of brevity, we only report the typical result $( \mathbf { e . g . } , x = 0 . 9 )$ in this paper.

## 4.3.5. Evaluation of computational efficiency

Since a WoT recommendation environment involves a large number of items and users, computational ef<sup>fi</sup>ciency is a major concern. Fig. 6 shows the recommendation time consumed by all systems under the training/test splitting ratio of $x = 0 . 9 .$ . For the proposed ROT system, item groups and user groups are computed in advance during the system training time. During the recommendation time, the ROT system only needs to aggregate the typicality degrees of items and users in order to generate the <sup>fi</sup>nal recommendation scores. As a result, the ROT system can ef<sup>fi</sup>ciently generate the recommendation scores on the <sup>fl</sup>y. The CB baseline system is the second best system in terms of recommendation time because it only needs to compute the similarities between a target item and all the items rated by the current user. Both the UBCF and the IBCF baseline systems need to identify the “nearest neighbors” of an item or a user in the entire recommendation space. As a result, they are not as ef<sup>fi</sup>cient as the ROT system and the CB system. The EMDP baseline is the least ef<sup>fi</sup>cient system since it needs to predict the missing data <sup>fi</sup>rst, and then it combines the ratings obtained through a user-based CF method and an item-based CF method. For other training/test splitting ratios, we obtained similar experimental results. For the reason of brevity, we only report the result under the condition x = 0.9.

Table 5  
Comparative RMSE improvements of ROT under different training/test ratios

<table><tr><td></td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>EMDP</td><td>10.1%</td><td>9.32%</td><td>7.12%</td><td>5.26%</td><td>4.6%</td></tr><tr><td>CB</td><td>8.91%</td><td>11.08%</td><td>12.72%</td><td>12.53%</td><td>13.5%</td></tr><tr><td>IBCF</td><td>5.67%</td><td>7.26%</td><td>8.29%</td><td>8.13%</td><td>8.84%</td></tr><tr><td>UBCF</td><td>7.33%</td><td>8.02%</td><td>7.89%</td><td>6.94%</td><td>7.07%</td></tr><tr><td>Naive hybrid</td><td>11.97%</td><td>13.34%</td><td>10.06%</td><td>8.09%</td><td>7.39%</td></tr></table>

Please cite this article as: Y. Cai, et al., Object typicality for effective Web of Things recommendations, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.008

![](/api/attachments/9A4FG392/fulltext/images/91f68ac8c613671efdb9b3c086a304625ce9d80991323a92dfab048a6e1a93b0.jpg)  
Fig. 5. Comparative performance of big-error predictions.

## 4.3.6. Comparison with the state-of-the-art methods

To further evaluate the performance of the proposed ROT system, we adopted a similar experimentation procedure and data set as reported in the literature [22]. Table 6 shows the comparative performance of ROT and other state-of-the-art recommender systems reported in the literature [22]. For the reason of limited space, we only show the experimental result based on MAE. According to Table 6, ROT outperforms all state-of-the-art systems under different con<sup>fi</sup>gurations. In particular, given both sparse training data (e.g., ML100 and Given5) and relatively rich training data (e.g., ML300 and Given15), ROT achieves the lowest MAE scores when compared to state-of-the-art systems such as SCBPCC, WLR, and CBT.

![](/api/attachments/9A4FG392/fulltext/images/f5e3b1cfd7e80bf0569f9d937893724c9e6963e57e4218e84a36f7802a58747f.jpg)  
Fig. 6. Comparison of recommendation time.

Table 6  
Comparison with state-of-the-art methods on MAE.

<table><tr><td>Training set</td><td>Methods</td><td>Given5</td><td>Given10</td><td>Given15</td></tr><tr><td rowspan="4">ML100</td><td>SCBPCC</td><td>0.874</td><td>0.845</td><td>0.839</td></tr><tr><td>WLR</td><td>0.915</td><td>0.875</td><td>0.890</td></tr><tr><td>CBT</td><td>0.840</td><td>0.802</td><td>0.786</td></tr><tr><td>ROT</td><td>0.807</td><td>0.797</td><td>0.781</td></tr><tr><td rowspan="4">ML200</td><td>SCBPCC</td><td>0.871</td><td>0.833</td><td>0.828</td></tr><tr><td>WLR</td><td>0.941</td><td>0.903</td><td>0.883</td></tr><tr><td>CBT</td><td>0.839</td><td>0.800</td><td>0.784</td></tr><tr><td>ROT</td><td>0.813</td><td>0.771</td><td>0.764</td></tr><tr><td rowspan="4">ML300</td><td>SCBPCC</td><td>0.870</td><td>0.834</td><td>0.819</td></tr><tr><td>WLR</td><td>1.018</td><td>0.962</td><td>0.938</td></tr><tr><td>CBT</td><td>0.840</td><td>0.801</td><td>0.785</td></tr><tr><td>ROT</td><td>0.785</td><td>0.755</td><td>0.753</td></tr></table>

We also compared the performance of ROT with that of three stateof-the-art recommender systems, SVD, SVD++, and SocialMF because these systems achieved very good performance under the larger Net<sup>fl</sup>ix benchmark data set [18]. For this experiment, we utilized the Net<sup>fl</sup>ix benchmark data set and adopted a training/test splitting ratio of x = 0.8. The experimental results that were generated based on 5-fold cross-validation are plotted in Figs. 7 and 8, respectively. According to Fig. 7, the proposed ROT system signi<sup>fi</sup>cantly outperforms SVD, SocialMF, and SVD++ by 5.27% $( t ( 4 ) = 3 0 . 0 , p < . 0 1 )$ ), 4.45% (t(4) = 73.4, $p < . 0 1 )$ , and $3 . 1 6 \% ~ ( t ( 4 ) = 6 1 . 6 , p < . 0 1 )$ in terms of MAE, respectively. Moreover, the ROT system achieves a comparable RMSE performance with that of state-of-the-art systems. Our post-experimental analysis found that some users were not assigned to any user groups. Accordingly, the ROT system only generated a default rating for an item (i.e., the average rating of that item) with respect to these users. Nevertheless, these recommendations may lead to big-error predictions. Since the metric of RMSE is sensitive to big-error predictions, the RMSE score achieved by the ROT system is not as good as those achieved by other state-of-the-art systems. We will explore other methods (e.g., default user pro<sup>fi</sup>ling) to speci<sup>fi</sup>cally deal with the coldstart problem so that new users can also be classi<sup>fi</sup>ed to some user interest groups. However, this line of research will be conducted as part of our future work. As a whole, we compare the performance of the proposed ROT system with quite a number of state-of-the-art recommender systems based on two different benchmark data sets. The ROT system signi<sup>fi</sup>cantly outperforms state-of-the-art systems based on the MovieLens data set. As for the Net<sup>fl</sup>ix data set, the results are mixed. The ROT system outperforms state-of-the-art systems in terms of

![](/api/attachments/9A4FG392/fulltext/images/5ee43b0097cb300e0f64fd273b80a1cfa6137c33cdb5ec0d03397e06b609cc44.jpg)  
Fig. 7. Comparative MAE performance of ROT based on the Net<sup>fl</sup>ix data set.  
Please cite this article as: Y. Cai, et al., Object typicality for effective Web of Things recommendations, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.008

Y. Cai et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/9A4FG392/fulltext/images/0f20199e8e5d4bd4ea9f95399ef61da2efdb9ab5dd08793af5fdd00f57e6685b.jpg)  
Fig. 8. Comparative RMSE performance of ROT based on the Net<sup>fl</sup>ix data set.

MAE, but it only achieves a comparable performance with state-of-the art systems in terms of RMSE.

## 5. Discussions

The proposed typicality-based recommendation method is novel since it can take into account the way how people evaluate objects with reference to a concept (e.g., a user's speci<sup>fi</sup>c interest). More specifically, the proposed recommendation method is underpinned by the principle of object typicality empirically evaluated in the <sup>fi</sup>eld of cognitive psychology. The proposed method estimates the speci<sup>fi</sup>c interest of a user in terms of the typicality of the user within a particular user interest group and the typicality of items that the user group is most interested in. It addresses the issues of data sparsity and computational ef<sup>fi</sup>ciency pertaining to the WoT recommendation environment by recommending things at the level of item groups and user groups instead of directly evaluating individual items and users on the <sup>fl</sup>y. These are the reasons why the proposed ROT system outperforms (e.g., in terms of MAE and computational time) all the baseline systems that directly operate at individual item and user level under the condition of sparse training data.

For example, for the MovieLens-based experiments, the ROT system predicted a rating of 5 for the movie “Usual Suspects, The (1995)” (movie id 12) and the movie “Pulp Fiction (1994)” (movie id 56) with respect to the user 99 (a user with benchmark id 99). The user 99 is very typical (with a typicality degree of 0.9) for the user interest group “Crime Movies”. Besides, the typicality degrees of “Usual Suspects, The (1995)” and “Pulp Fiction (1994)” for the item group “Crime Movies” are 1.0 and 0.9517, respectively. Since the user 99 is typical for the user interest group “crime movie”, and the two movies are the typical items that the user group likes, the ROT system generates high ratings for these movies according to the principle of object typicality. In fact, the predictions provided by the ROT system are exactly the same as user 99's actual ratings for the respective movies.

Basically, all the research questions have been answered through the two series of benchmark experiments. The number of item groups K has an impact on the performance of the ROT prototype system. The empirical parameter tuning method that we adopted can identify a reasonable range of K values for the ROT system. Our experiments also show that the ROT system is more effective (e.g., producing the least big-errors) than other baseline systems given sparse training data. Moreover, it is more ef<sup>fi</sup>cient than other baseline systems because it mainly operates at the item group and user group level during the recommendation time. Finally, the ROT system signi<sup>fi</sup>cantly outperforms other state-ofthe-art recommender systems in terms of MAE based on both the MovieLens and the Net<sup>fl</sup>ix benchmark data sets.

## 6. Conclusions

With the rapid growth of “Web of Things” applications, there is a pressing need to develop an effective and ef<sup>fi</sup>cient method for the discovery and selection of smart things on the Web. This paper proposes a recommender system-based solution to address WoT discovery and selection, and hence to improve the situation awareness of WoT applications. Since the recommendation space of WoT is typically sparse, and computational ef<sup>fi</sup>ciency as well as users' trusts on recommendations are also the primary concerns, the main contribution of our research work is the design of a novel typicality-based recommendation method that addresses the aforementioned critical issues for WoT recommendations. As the proposed recommendation method is underpinned by the “object typicality” principle empirically veri<sup>fi</sup>ed in the <sup>fi</sup>eld of cognitive psychology, it tends to produce less big-error recommendations, and hence it promotes users' trusts on WoT applications. In addition, since the proposed method exploits data generalization by operating at the item group and the user group level during recommendation time, it alleviates the problems of data sparsity and computational ef<sup>fi</sup>ciency for large-scale WoT recommendations.

Based on the benchmark MovieLens data set, our experimental results con<sup>fi</sup>rm that the proposed ROT prototype system signi<sup>fi</sup>cantly outperforms all the baseline recommender systems even under the condition of sparse training data. Moreover, the ROT system is more ef-<sup>fi</sup>cient than other baseline recommender systems and it produces the least big-error recommendations. Based on the Net<sup>fl</sup>ix data set that simulates a large WoT recommendation space, the ROT system signi<sup>fi</sup>cantly outperforms state-of-the-art recommender systems in terms of MAE, and it achieves comparable performance with that of state-of-the-art recommender systems in terms of RMSE. As a whole, our experimental results reveal that the proposed ROT prototype system has great potential to support large-scale WoT discovery and recommendation. To the best of our knowledge, it is the <sup>fi</sup>rst successful research work which involves the design and development of a cognitively motivated recommender system for WoT recommendations. The business implication of our research work is that the proposed recommendation method can enhance the situation awareness of WoT applications which facilitate the reuse of enterprise resources and the interoperability among enterprises.

For our current experiments, only keyword-based properties (e.g., the textual descriptions of movies) have been explored to construct item groups. Future work will explore a richer model of item properties to enhance the effectiveness of the proposed ROT system. Another limitation of our current work is that the number of item groups identi<sup>fi</sup>ed by the ROT system may not be optimal. More sophisticated methods such as genetic algorithms will be explored to identify optimal or near optimal clusters of items. In addition, alternative clustering algorithms and similarity functions will be applied to bootstrap the performance of item group and user group construction. A hybrid method will be examined to tackle the cold-start problem such that new users of the system can also be assigned to some user groups. A comparative study about the recommendation performance of ROT and that of economic choice models will be performed. Finally, we will explore Big Data Analytics (e.g., MapReduce) to support parallel incremental clustering of item groups and user groups to further improve the computational ef<sup>fi</sup>ciency of the ROT system for real-time WoT recommendations.

## Acknowledgments

The work described in this paper was supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (project no. CityU 115910), City University of Hong Kong (project no. 7008138), the Shenzhen Municipal Science and Technology R&D Funding — Basic Research Program (project no. JCYJ20130401145617281), the Shenzhen Research Institute, City University of Hong Kong, National Natural Science Foundation of China (project no.

61300137), the Guangdong Natural Science Foundation of China (project no. S2011040002222 and S2013010013836), the Fundamental Research Funds for the Central Universities, SCUT (project no. 2012ZM0077).

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[2] Marko Balabanović, Yoav Shoham, Fab: content-based, collaborative recommendation, Communications of the ACM 40 (3) (1997) 66–72.

[3] Lawrence W. Barsalou, Ideals, central tendency, and frequency of instantiation as determinants of graded structure in categories, Journal of Experimental Psychology: Learning, Memory, and Cognition 11 (4) (October 1985) 629–654.

[4] Lawrence W. Barsalou, Cognitive Psychology: An Overview for Cognitive Scientists Lawrence Erlbaum As. Pu. 1992

[5] Yi Cai, H.F. Leung, Multi-prototype concept and object typicality in ontology, Proceedings of the 21st International Florida Arti<sup>fi</sup>cial Intelligence Research Society Conference, AAAI Press, 2008, pp. 470–475.

[6] Jean-Pierre Desclés, Anca Pascu, Logic of determination of objects: the meaning of variable in quanti<sup>fi</sup>cation, International Journal of Arti<sup>fi</sup>cial Intelligence Tools 15 (6) (2006) 1041–1052.

[7] Mukund Deshpande, George Karypis, Item-based top-n recommendation algorithms, ACM Transactions on Information Systems 22 (1) (2004) 143–177

[8] Carolina Fortuna, Matevz Vucnik, Blaz Fortuna, Klemen Kenda, Alexandra Moraru, Dunja Mladenic, Towards building a global oracle: a physical mashup using arti<sup>fi</sup>cial intelligence technology, in: Simon Mayer, Dominique Guinard, Erik Wilde (Eds.) Third International Workshop on the Web of Things, WoT'12, Newcastle, United Kingdom, June 19, 2012, ACM, 2012.

[9] K.M. Galotti, K.M. Galotti, Cognitive Psychology In and Out of the Laboratory, third edition, Wadsworth, Belmont, CA, 2004.

[10] Zeno Gantner, Steffen Rendle, Christoph Freudenthaler, Lars Schmidt-Thieme, Mymedialite: a free recommender system library Proceedings of the Fifth ACM Conference on Recommender Systems, 2011, pp. 305–308.

[11] Dominique Guinard, Mathias Fischer, Vlad Trifa, Sharing using social networks in a composable Web of Things, Proceedings of the 8th IEEE International Conference on Pervasive Computing and Communications, IEEE, 2010, pp. 702–707.

[12] Jing He, Yanchun Zhang, Guangyan Huang, Jinli Cao, A smart Web service based on the context of things, ACM Transactions on Internet Technology (TOIT) 11 (3) (January 2012)(Article 13).

[13] Jonathan L. Herlocker, Joseph A. Konstan, Al Borchers, John Riedl, An algorithmic framework for performing collaborative <sup>fi</sup>ltering, Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval ACM Press New York NY USA 1999 pp. 230–237.

[14] Ming Hua, Jian Pei, Ada W. Fu, Xuemin Lin, Ho-Fung Leung, Top-k typicality queries and ef<sup>fi</sup>cient query answering methods on large databases, The VLDB Journal 18 (3) (2009) 809–835.

[15] Mohsen Jamali, Martin Ester, A matrix factorization technique with trust propagation for recommendation in social networks, Proceedings of the Fourth ACM Conference on Recommender Systems, RecSys'10, ACM, New York, NY, USA, 2010, pp. 135–142.

[16] Heung-Nam Kim, Inay Ha, Kee-Sung Lee, GeunSik Jo, Abdulmotaleb El-Saddik, Collaborative user modeling for enhanced content <sup>fi</sup>ltering in recommender systems, Decision Support Systems 51 (4) (2011) 772–781.

[17] Joseph A. Konstan, Bradley N. Miller, David Maltz, Jonathan L. Herlocker, Lee R. Gordon, John Riedl, GroupLens: applying collaborative <sup>fi</sup>ltering to Usenet news, Communications of the ACM 40 (3) (1997) 77–87.

[18] Yehuda Koren, Robert M. Bell, Chris Volinsky, Matrix factorization technigues for recommender systems, IEEE Computer 42 (8) (2009) 30–37

[19] Raymond Y.K. Lau, Peter D. Bruza, Dawei Song, Towards a belief-revision-based adaptive and context-sensitive information retrieval system, ACM Transactions on Information Systems 26 (2) (2008)(Article 8).

[20] Raymond Y.K. Lau, M. Tang, O. Wong, S. Milliner, Y. Chen, An evolutionary learning approach for adaptive negotiation agents, International Journal of Intelligent Systems 21 (1) (2006) 41–72.

[21] Marie-Jeanne Lesot, Laure Mouillet, Bernadette Bouchon-Meunier, Fuzzy prototypes based on typicality degrees, Proceedings of the 8th Fuzzy Days'04, volume 33, Springer, 2004, pp. 125–138.

[22] Bin Li, Qiang Yang, Xiangyang Xue, Can movies and books collaborate? Cross-domain collaborative <sup>fi</sup>ltering for sparsity reduction, in: Craig Boutilier (Ed.), Proceedings of the Twenty-<sup>fi</sup>rst International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 2009, pp. 2052–2057.

[23] Cen Li, Gautam Biswas, Unsupervised learning with mixed numeric and nominal data, IEEE Transactions on Knowledge and Data Engineering 14 (2002) 673–690.

[24] Hao Ma, Irwin King, Michael R. Lyu, Effective missing data prediction for collaborative <sup>fi</sup>ltering, Proceedings of the 30th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, New York, NY, USA, 2007, pp. 39–46.

[25] Simon Mayer, Dominique Guinard, An extensible discovery service for smart things, in: Dominigue Guinard, Vlad Trifa, Erik Wilde (Eds.). Second International Workshop on the Web of Things (WoT 2011). San Francisco California June 2011.

[26] D.L. Medin, E.E. Smith, Concepts and concept formation, Annual Review of Psychol-0gv 35 (1984).113-138

[27] Prem Melville, Raymod J. Mooney, Ramadass Nagarajan, Content-boosted collaborative <sup>fi</sup>ltering for improved recommendations, Proceedings of the Eighteenth National Conference on Arti<sup>fi</sup>cial Intelligence, American Association for Arti<sup>fi</sup>cial Intelligence, Menlo Park, CA, USA, 2002, pp. 187–192.

[28] Raymond J. Mooney, Loriene Roy, Content-based book recommending using learning for text categorization, DL'00: Proceedings of the Fifth ACM Conference on Dig ital Libraries, ACM, New York, NY, USA, 2000, pp. 195–204.

[29] Gregory L. Murphy, Gregory L. Murphy, The Big Book of Concepts, MIT Press, 2002.

[30] Nathan Srebro Nati, Tommi Jaakkola, Weighted low-rank approximations, In 20th International Conference on Machine Learning, AAAI Press, 2003, pp. 720–727.

[31] A. Paterek, Improving regularized singular value decomposition for collaborative <sup>fi</sup>ltering, Proceedings of the ACM SIGKDD Cup and Workshop, ACM, 2007, pp. 39–42.

[32] M.J. Pazzani, D. Billsus, Content-based recommendation systems, The Adaptive Web: Methods and Strategies of Web Personalization, 2007. 325–341.

[33] Michael Pazzani, Daniel Billsus, Learning and revising user pro<sup>fi</sup>les: the identi<sup>fi</sup>cation of interesting web sites, Machine Learning 27 (3) (1997) 313–331.

[34] M. Rifqi, Constructing prototypes from large databases, Proceedings of the Information Processing and Management of Uncertainty Conference. 1996. pp. 301–306.

[35] Simone Santini, Ramesh Jain, Similarity matching, Proceedings of the Second Asian Conference on Computer Vision, 1995, pp. 571–580.

[36] Badrul Sarwar, George Karypis, Joseph Konstan, John Reidl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, Proceedings of the 10th International World Wide Web Conference, ACM, New York, NY, USA, 2001, pp. 285–295.

[37] Ian M. Soboroff, Charles K. Nicholas, Combining content and collaboration in text <sup>fi</sup>ltering, In Proceedings of the IJCAI'99 Workshop on Machine Learning for Information Filtering, 1999, pp. 86–91.

[38] D. Song, R.Y.K. Lau, P.D. Bruza, K.F. Wong, D.Y. Chen, An adaptive information agent for document title classi<sup>fi</sup>cation and <sup>fi</sup>ltering in document-intensive domains, Decision Support Systems 44 (1) (2008) 251–265.

[39] Jie Tang, Jing Zhang, Limin Yao, Juanzi Li, Li Zhang, Zhong Su, Arnetminer: extraction and mining of academic social networks, Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, New York, NY, USA, 2008, pp. 990–998.

[40] Loren Terveen, Will Hill, Brian Amento, David McDonald, Josh Creter, Phoaks: a system for sharing recommendations, Communications of the ACM 40 (3) (1997) 59–62.

[41] J.P. Ueberla, An extended clustering algorithm for statistical language models, IEEE Transactions on Speech and Audio Processing 4 (4) (1996) 313–316.

[42] W. Vanpaemel, G. Storms, B. Ons, A varying abstraction model for categorization, Proceedings of the 27th Annual Cognitive Science Conference, Lawrence Erlbaum, Mahwah, NJ, 2005, pp. 2277–2282.

[43] Jun Wang, Arjen P. de Vries, Marcel J.T. Reinders, Unifying user-based and item-based collaborative filtering approaches by similarity fusion. Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval ACM New York NY USA 2006 pp. 501–508.

[44] Rui Xu, D. Wunsch, Survey of clustering algorithms, IEEE Transactions on Neural Networks 16 (3)(2005) 645–678

[45] Xu. Yunhong, Xitong Guo, Jinxing Hao, Jian Ma, Raymond Y.K. Lau, Wei Xu, Combining social network and semantic concept analysis for personalized academic researcher recommendation, Decision Support Systems 54 (1) (2012) 564–573.

[46] Gui-Rong Xue, Chenxi Lin, Qiang Yang, WenSi Xi, Hua-Jun Zeng, Yong Yu, Zheng Chen, Scalable collaborative filtering using cluster-based smoothing, Proceedings of the 28th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, New York, NY, USA, 2005, pp. 114–121.

[47] Xin Yan, Raymond Y.K. Lau, Dawei Song, Xue Li, Jian Ma, Toward a semantic granularity model for domain-speci<sup>fi</sup>c information retrieval, ACM Transactions on Information Systems 29 (3) (2011)(Article 15).

[48] L.A. Zadeh, Fuzzy sets, Journal of Information and Control 8 (1965) 338–353.

[49] Zibin Zheng, Hao Ma, Michael R. Lyu, Irwin King, WSRec: a collaborative <sup>fi</sup>ltering based web service recommender system, Proceedings of the 2009 IEEE International Conference on Web Services, IEEE, 2009, pp. 437–444.

Yi Cai received his Ph.D. degree in computer science from the Chinese University of Hong Kong. He is currently an associate professor of the School of Software Engineering at the South China University of Technology, Guangzhou, China. His research interests are recommendation system personalized search semantic web and data mining.

Raymond Y. K. Lau is an associate professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. degree from the Queensland University of Technology in 2003. He is the author of over 100 refereed international journals and conference papers. His research work has been published in renowned journals such as the MIS Quarterly, ACM Transactions on Information Systems. IEEE Transactions on Knowledge and Data Engineering, INFORMS Journal on Computing, Journal of MIS, etc. His research interests include information retrieval, WoT, and social media analytics. He is a senior member of IEEE and ACM, respectively.

Y. Cai et al. / Decision Support Systems xxx (2013) xxx–xxx

Stephen S.Y. Liao is a professor and the director of the Advanced Transportation Information Systems (ATIS) Research Center at the City University of Hong Kong. He received a bachelor's degree from Beijing University and a Ph.D. from the University of Aix-Marseille III and Institute of France Telecom. His research work has been published in journals including the MIS Quarterly, Decision Support Systems, Communications of the ACM, Information Science, etc. His current research interests include the use of information technology in mobile commerce applications and intelligent business systems, especially intelligent transportation systems.

Chunping Li received his Ph.D. degree from Darmstadt University of Technology, Germany in 1999. He is currently an associate professor in Tsinghua University, China. His research interests include machine learning, data mining, text classi<sup>fi</sup>cation and topic modeling. He has published more than eighty research papers in related <sup>fi</sup>elds.

Ho-fung Leung is currently a professor and the chairman of the Department of Computer Science and Engineering, at the Chinese University of Hong Kong, China. He has been active in research on intelligent agents, multi-agent systems, game theory, and semantic web

Louis C. K. Ma is the acting director of the School of Continuing and Professional Education at the City University of Hong Kong. He obtained his MBA from the University of Technology, Sydney, and his Ph.D. from the University of Warwick, UK. His areas of research interest are in IS policy and strategy, project management, and e-markets. His publications have appeared in major IS journals such as the Journal of MIS, Information & Management, and Decision Support Systems.
