---
otero_id: 8896
otero_key: "66R5P5S3"
title: "Towards generating scalable personalized recommendations: Integrating social trust, social bias, and geo-spatial clustering"
authors: "Divyaa L.R.; Nargis Pervin"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards generating scalable personalized recommendations: Integrating social trust, social bias, and geo-spatial clustering

![](/api/attachments/66R5P5S3/fulltext/images/cf9092570821c090d6f785693d4a6779da143ae7bc15d398a6329767bb56555b.jpg)

Divyaa L.R., Nargis Pervin 大

Department of Management Studies, Indian Institute of Technology Madras, India

## A R T I C L E I N F O

Keywords: Probabilistic Matrix Factorization Two-stage clustering Social network Preference network Location based social recommendation

## A B S T R A C T

With the advent of Web 2.0, recommender systems have become a viable means to harness relevant information online. In the past decades, extensive research have been conducted in the field of recommendations — model based collaborative techniques being the most favored ones. Recently, a new paradigm of trust-based recommendation approach has emerged wherein structural features from social network resulted in an improved eficacy of the algorithms. However, majority of these approaches assume that users' ratings are impacted by all his social connections in friendship network and completely ignore their preferential similarity, which is essential for personalized recommendations. Herein, we address this pivotal issue and propose a two-stage clustering based matrix-factorization algorithm, ‘Cluster REfinement on Preference Embedded MF (CREPE MF)’ using a subgraph of social network that integrates preferential similarity score. Also, an immense surge in mobile device usage has been observed in recent times, thereby paving the way for tracking users' locations en-route to physical entity recommendations. As users' locations are geo-spatially co-located, we extend CREPE MF to Geographical CREPE MF (gCREPE MF) by incorporating geo-spatial influence. These two proposed algorithms have been systematically evaluated with state-of-the-art algorithms in terms of prediction accuracy and runtime complexity using two real-world data sets, namely Yelp and Gowalla. Gratifyingly, our approach CREPE MF outperforms the state-of-the-art algorithms; depending on the underlying data sets it achieves an improvement of 6.50% to 17.93% in accuracy and 11.67% to 74.23% in runtime. Extended model gCREPE MF further achieves 18.06% to 83.44% reduction in runtime without compromising on accuracy.

## 1. Introduction

Recommendation technology is a continuous enterprise in the area of machine learning with diverse applications in sociology, healthcare, and physicist communities [1-3]. It has become a core component of various e-Marketplaces such as Amazon, eBay, Epinion, etc. and also been judiciously incorporated in the domain of books [4], movies [5], tourist spots [6], Point-of-Interests (POI) [7], etc.

A Recommender System (RS) in general, analyzes relationships between users and interdependencies among items to predict new items or the missing preferences for the users [8]. In this context, Collaborative Filtering (CF) is the most popular technique owing to its operational simplicity. The CF approach can be classified into modelbased and memory-based technique where memory-based methods use entire user-item rating matrix in the memory to recommend items from users with similar taste and model-based CF techniques learn the parameters of a generative model using machine learning or data mining technique. The CF techniques sufer from well-known data sparsity and cold-start problems [9] which can be addressed by incorporating trust information or social factors into the user-item rating matrix. It has paved the way to trust-aware recommender systems which gained immense popularity with the emergence of online social network [10, 11]. However, in general, trust-based CF methods do not scale well as the number of users and items grow exponentially and users' huge social network adds to the complexity, restricting its swift adaptability in real-world applications [12].

To address the scalability issue, model-based techniques [13], particularly Matrix Factorization (MF) [14] has gained significant attention, where the rating matrix $R _ { m , n }$ is approximated by product of lower dimensional matrices which capture the latent or unobserved attributes of the users and items with improved prediction accuracy and scalability. Apart from these model-based approaches, another popular approach is the clustering based CF technique [15, 16], which segregates the user-item rating space into smaller clusters and the recommendations are generated using CF method in individual clusters. It is worthy to mention that clustering has primarily been applied to memory-based CF techniques to reduce the runtime complexity, while it compromises on the recommendation quality (accuracy). To the best of our knowledge implementation of clustering on model-based tech nique is scarce and demands a systematic investigation.

Improving the scalability of recommender systems along with accuracy [11, 17] is in the focus of general interest. In a recent survey paper, Bao et al. [18] demonstrated that scalability and accuracy are the two critical metrics to measure the performance of a recommender system. We envisage a scenario that amalgamates a model-based trustaware CF approach with clustering would drastically improve these two metrics to a great extent. As the approach considers trust-network in modeling, it would inherently as well address the data-sparsity issue. However, materialization of this concept is not straight-forward as the poor clustering due to sub-optimal choice of number of clusters may result in reduction of recommendation accuracy. It has been observed that the users' opinions are afected by the Social Bias [19, 20] — higher rated items get higher ratings and thus items are trapped in so called ‘Rating Bubbles'. Similarly, the social bias traps the users into users' rating bubbles. Utilization of this distinct phenomenon to cluster useritem space would be a transformative alternate.

Further, most of the studies on trust-aware recommender systems utilize all the connections from the social network for recommending items [21, 22]. However, among the myriad of online connections on social platform only a few exhibit similar taste [1, 23] with varied level of significance in the active user's decision making. This leaves it unclear whether a user trust recommendations by all his friends. Thus, extending Theory of Homophily and Triadic Closure, we alter the social network and introduce Preference Network (PN), where an edge exists between a pair of users if they have similar preference on a set of items and the Social Trust among users is propagated through PN. We propose a clustering based probabilistic matrix factorization technique, by incorporating user's Preference Network (PN) connections into PMF model and refer that as “Cluster REfinement on Preference Embedded MF (CREPE MF)”. Here, Preference Network (PN) has been defined as a graph where an edge exists between a pair of users if they have similar preference on a set of items. It is worth noting that PN is a subgraph of actual social network and does not include all the social connections of a user as generally considered in social recommender systems [21, 22].

While scalability and accuracy play pivotal roles in determining the eficacy of a RS, consideration of the location is significant for recommending physical entities such as restaurants, tourist spots, etc. In fact this is the prime factor when real-time location specific recommendations are in concern and in today's scenario it is gaining increasing attention with the rapid proliferation of smart mobile devices with wireless network connections. Thus, generating recommendations by considering location based social networks (LBSNs) is highly desirable. However, prior literature [7, 24] on LBSNs relies on user check-in data to model user preferences which is either not available in many applications or extremely sparse. In such a scenario, modeling geographical influence using available rating data turns out to be a convenient route. Thus, we present our second algorithm, modifying CREPE MF to include the geographical influence and refer it as Geographical CREPE MF or gCREPE MF.

Experiments have been conducted on two real-world data set col lected from Yelp<sup>1</sup> and Gowalla<sup>2</sup> and compared with four state-of-the-art algorithms as presented in Refs. [14, 21, 22, 25]. The experimental results demonstrate the eficacy of our approaches (CREPE MF and gCREPE MF) compared to the baseline algorithms with a significant improvement of 6.50% to 17.93% in accuracy and 11.67% to 74.23% in runtime for CREPE MF, depending on the underlying data sets. Grati fyingly, when compared with gCREPE MF runtime complexity improved significantly up to an additional 18.06% to 83.44% (compared to CREPE MF) without compromising on accuracy.

This paper provides several important contributions. First, our findings extend the trust-based recommendation literature [21, 22, 25] by incorporating the ‘Preference Network’ in the model constructed using theories of Social Trust (Theory of Homophily and Triadic Closure). Secondly, it demonstrates the importance of clustering user-item space to discover ‘Rating Bubbles' derived from Theory of Social Bias. Third, the incorporation of geographical influence in the model ensures the real-time location based recommendations of items. Moreover, this study empirically revealed the eficacy of our approaches, CREPE MF and gCREPE MF, compared to four state-of-the-art baseline algorithms with two unrelated big real-world data sets. The proposed approaches are derived by drawing inspiration from social science theories. They are quite general with broad application prospects in various domains. The proposed algorithms are directly applicable to firms like Yelp and Gowalla and can also be considered to many other e-Marketplaces having social networking option. Along with the empirical validation of the approaches with real big data sets, the algorithmic steps can be well-understood from a social theory perspective.

This article is organized as follows. At the outset, we discuss the related literature in the field of trust-based recommender system and then explicate the significance of similarity based Preference Network followed by literature on clustering and location-aware recommendations. We also discuss the relevant social science theories in connection with our approach. Thereafter, we present our two proposed approaches CREPE MF and gCREPE MF detailing the mathematical formulations for each step and the illustration of the computational complexity. Subsequently, using two real-world data sets collected from Yelp and Gowalla, we experimentally validated the eficacy of our approaches. Lastly, we conclude our findings with future research directions.

## 2. Literature review

Based on the relevance to our approaches, we have segregated the existing RSs into the following areas: trust-based collaborative filtering, clustering based RSs, and location-aware RSs. Subsequently, we present social network theories in connection with trust-based recommender systems.

## 2.1. Trust-based collaborative filtering

Collaborative Filtering (CF), which essentially automates the pro cess of electronic word-of-mouth are broadly classified into two categories [13]: memory-based [26, 27] and model-based [14, 21]. While memory-based approaches boost the prediction accuracy model-based approaches are scalable and hence are eficient for real-time recommender systems. The Probabilistic Matrix Factorization (PMF) technique [14] is the state-of-the-art latent factor model which factorizes the rating matrix into product of two lower-dimensional matrices to improve accuracy and scales linearly with the number of users.

The recent growth of online social networks have made social information easily accessible, providing a way for emergence of trustbased recommender systems. In trust-based recommender systems, the user's latent features are generally assumed to be similar to friend's latent features [21]. In this context, Ma et al. [22] introduced a social regularization to the Matrix Factorization approach, where the influ ence of users' friends on the users' latent feature is weighted diferently based on the rating similarity between the users and their friends. Yang et al. [25] further extended this model to incorporate the item-item similarity network based on item attributes. This approach facilitates the propagation of influence through the social network of users and the network of similar items. The underlying assumption in such methods is that all of the online friends in social network circle influence the active users' preference for items. However, in reality majority of the social network friends do not share similar interests [1] and hence they probably have very little impact on active users' decision making. Therefore, computing similarity among the social connections based on their true item preference is crucial and thus a novel metho dology that exploits preference-similarity network to capture common preferences between the target user and other social connections is highly desirable.

## 2.2. Clustering based recommender systems

Grouping users/items into homogeneous clusters is an intriguing strategy in the field of recommender systems. While a plethora of works have been done to study the efect of clustering on memory-based methods [15, 16], far too little attention has been paid to study the efect of clustering on model-based techniques. Nima and Charles [28] have applied clustering on rating patterns to find communities of users and items, and reconstructed the rating matrix accordingly. Matrix factorization is applied on new rating matrix to identify the community efect. The final predictions are the fusion of predictions obtained from original rating matrix and the reconstructed one. This method could improve both scalability and accuracy compared to traditional CF, however it requires training of two matrices: user-item rating matrix and rating matrix for the clusters separately. Nevertheless, clustering users and items into homogeneous groups is a crucial step for scaling the model in real-time. Therefore, we argue that fusion of clustering and matrix factorization would improve both scalability and accuracy of the system to a great extent.

## 2.3. Location-aware recommendation

Apart from giving importance to accuracy and scalability, the location of physical entities such as restaurants, tourist spots etc. plays an important role in determining the users' visits. This has led to the popularity of location-aware or point of interest (POI) recommendation using check-in services on social-media through mobile-devices in multiple disciplines [7, 24]. However, majority of these applications do not consider the geographical influence i.e., the distance among the neighboring items or POIs. In an early work by Kang et al. [6] user profiles have been modeled to capture the similarity between user preference attributes and POI attributes to recommend POIs. Geographical distance of user check-in activities follows power-law distribution which can be used to model check-in probability of nearby POIs. Inspired by the geographical clustering phenomenon of check-in activities Mao et al. [7] have proposed a power-law probabilistic model. Further, to improve the quality of predictions social influence of friends in a specific location has been incorporated [7]. Apart from these memory-based techniques, several model-based approaches have been introduced lately, which inherently improves the scalability of the model [24, 29]. Cheng et al. [24] introduced a multi-center gaussian model for capturing geographical influence. In Hu et al.’s work [29] geographical influence of top k neighboring items within a given distance has been incorporated in matrix factorization technique where the influence has been captured using their latent features. However, these preceding works overlooked item similarity in the recommendation process. In this work, along with geographical distance, we have considered social influence and item similarity influence mined from item attributes, enabling to locate items that are not only closer but also similar to the focal item

Our proposed approach CREPE MF incorporates the clustering and social influence in the basic PMF model and gCREPE MF extends CREPE MF to include geographical influence of the items. The theories and the methods applied in these two models have been described in Section 2.4.

## 2.4. Applied theories and method

2.4.1. Theories on social trust, social bias, and geo-spatial clustering

In this section, we study theories on Social Trust, Social Bias, and Geo-spatial clustering which describe the users' behavior while making a purchase decision. Notably, utilization of these theories in social recommender system is trending [30]. We also show how these theorie are used judiciously to propose a framework that aids in personalizing recommendations for users.

2.4.1.1. Social trust. According to Sztompka [31] “Trust is a bet about the future contingent actions of others” which means trust occurs when a person believe the trusted person's actions and commits to it. Existing literature states that if a person trusts another person, then he will make decisions similar to the other person [32]. Though reliable trust values can be collected from users, the process turns out to be cumbersome [33]. However, according to Theory of Homophily proposed by McPherson et al. [34], ‘Similarity breeds connection’ which implies that users form ties with others who have similar preferences. In addition, Ziegler and Golbeck in Ref. [35] showed that there exists a strong and significant correlation between trust and similarity. Therefore, we argue that users' who share very strong preferences, trust each other while making decisions. On the contrary, researchers in the area of social recommender systems proclaim trust also arose from people who are directly connected in social networks (like friends, followers, experts etc.) [21]. The usefulness of friends' recommendations was studied in Ref. [36] and the results revealed that recommendations from friends were perceived to be useful and trustworthy. Few other studies showed that in addition to direct neighbors, trust can also be propagated from indirect neighbors [32]. The term Triadic Closure coined by M.Granovetter [37] postulates that two individuals with common friends are likely to become friends in the future. Inspired by this theory, we argue that trust can arise not only from people who are directly connected (friends), but also from indirect connections (mutual friends) if they share strong common preferences [30]. Therefore, using Triadic Closure, we extend the friends' network to include second hop connections as well and using Theory of Homophily, we retain only those connections which have high preferential similarity scores. This newly constructed network is termed as Preference Network, PN where PN for a focal user is defined as a subgraph of his direct and two-hop connections having high preference similarity score with the focal user. We model the propagation of social trust through this Preference Network and argue that this can potentially improve the accuracy of the predictions.

2.4.1.2. Social bias. In the current era of digitalization, many online sites such as Amazon, eBay, Yelp, etc. let users post ratings and reviews about a particular product. This abundant amount of information indirectly influences the users' opinion to follow the herd instinct [19, 20] i.e., a high rated item is susceptible to get a high rating and conversely, a user who consistently rates items higher (lower) is very likely to give a high (low) rating to a new item. This distinct behavior can be understood from theory of information cascading which occurs when an individual follows the choice of preceding individuals without regard to his own information [38]. Researchers have called this phenomenon as ‘Herding’, in which the behavior of individuals converge to a uniform social behavior [39]. Few other studies also proved that observational learning inferred from other users' ratings can trigger herding behavior [40] which traps the users and items in their respective Rating Bubbles [19, 20]. Inspired by this phenomenon, we suggest that clustering users and items based on their rating behavior can significantly improve the quality of recommendations. Therefore, in this study, we propose a novel two stage clustering approach, namely “Cluster REfinement on Preference Embedded MF (CREPE MF)” where users and items are clustered based on their rating behavior.

2.4.1.3. Geo-spatial clustering. It is also instructive that geographical influence becomes very important when physical entities like restaurants, tourist spots need to be recommended. According to Tobler's First Law of Geography “everything is related to everything else, but near things are more related than distant things” [41]. In addition, human mobility is constrained geographically by the distance one can travel within a day. Also, a study on 100,000 cellphone users' trajectories has shown that the travel patterns exerted by humans follow a simple reproducible pattern [42]. For instance, in case of restaurant search, it is intuitive that a user tends to look for restaurants that are nearby his home or ofice more often than restaurants that are far away from his place. This pattern has been found in Ref. [43] where the authors observed 20% of user's check-in occur within 1 km distance, 60% occur between 1 and 10 km, 20% occur between 10 and 100 km, and a very small percentage of user's check-in extend beyond 100 km in Foursquare data. Therefore, we argue that the users' visits are geospatially clustered and the businesses located near other businesses visited by the users are more relevant to the user. Thus, we extended CREPE MF to include geographical influence and refer it as gCREPE MF.

## 2.4.2. Probabilistic Matrix Factorization

Probabilistic Matrix Factorization (PMF), proposed by Ruslan and Andriy [14] is a popularly used model-based collaborative filtering technique for predicting the missing ratings. In PMF, the rating matrix $R _ { m \times n }$ is factorized into two matrices of lower dimensions, $U _ { m \times l }$ and $V _ { n \times l } ^ { T }$ which are user-latent matrix and item-latent matrix, respectively. The rating matrix is approximated as ${ R } _ { m \times n } \approx { U } _ { m \times l } \times { V } _ { n \times l } ^ { T } ,$ where l represents the dimension of the latent space. The rating matrix R is usually sparse and only observed ratings are considered while factorizing R. The conditional probability distribution of the observed ratings is given as follows:

$$
\begin{array}{l} p (R | U, V, \sigma_ {R} ^ {2}) \\ = \prod_ {u = 1} ^ {m} \prod_ {i = 1} ^ {n} [ \mathcal {N} (R _ {u, i} | U _ {u} \times V _ {i} ^ {T}, \sigma_ {R} ^ {2}) ] ^ {I _ {u, i}} \\ \text {where} \quad \mathbf {I} _ {u, i} = 1 \text {if user u has rated item i} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad = 0 \text {otherwise} \end{array}\tag{1}
$$

$N ( x | \mu , \sigma ^ { 2 } )$ is the normal distribution with mean μ and variance $\sigma ^ { 2 } .$ The Gaussian priors for user and item latent features are assumed as follows:

$$
p (U | \sigma_ {U} ^ {2}) = \prod_ {u = 1} ^ {m} \mathcal {N} (U _ {u} | 0, \sigma_ {U} ^ {2} I)\tag{2}
$$

$$
p (V | \sigma_ {V} ^ {2}) = \prod_ {i = 1} ^ {n} \mathcal {N} (V _ {i} | 0, \sigma_ {V} ^ {2} I)\tag{3}
$$

Based on Bayesian inference, the posterior probability distribution of U and V are given as:

$$
p (U, V | R, \sigma_ {R} ^ {2}, \sigma_ {U} ^ {2}, \sigma_ {V} ^ {2}) \propto p (R | U, V, \sigma_ {R} ^ {2}) p (U | \sigma_ {U} ^ {2}) p (V | \sigma_ {V} ^ {2})\tag{4}
$$

From Eq. (4), U and V can be learned for predicting missing ratings.

## 3. Solution details

In this section, we propose two models CREPE MF and gCREPE MF that extends the basic Probabilistic Matrix Factorization (PMF) technique discussed in Section 2.4.2.

## 3.1. CREPE MF

## 3.1.1. Two-stage clustering

Considering the concept of ‘Rating Bubbles' discussed in Section 2.4.1.2, we propose that users and items should be grouped into homogeneous clusters. In this context, choosing the number of user and item clusters is extremely crucial. While very low number of clusters will fail to capture the rating bubbles, very high number of clusters will reduce the density of social network and inter-item similarity graph, resulting in lower prediction accuracy. To define the distance metric in clustering, we capture the mean and standard deviation of the ratings in a 2-dimensional rating vector. $\mathcal { U } _ { u }$ is the rating vector for user u and <sub>i</sub> is the rating vector for item i. The mathematical expression for user rating vector $\mathcal { U } _ { u }$ and item rating vector $\mathcal { T } _ { i }$ are given as follows:

$$
\mathcal {U} _ {u} = \left[ \begin{array}{l l} - & - \\ R _ {u}, & \sqrt {\frac {\sum_ {i = 1} ^ {n} \boldsymbol {I} _ {u , i} (R _ {u , i} - R _ {u}) ^ {2}}{\sum_ {i = 1} ^ {n} \boldsymbol {I} _ {u , i} - 1}} \end{array} \right]\tag{5}
$$

$$
\mathcal {I} _ {i} = \left[ \begin{array}{l l} - & \sqrt {\frac {\sum_ {u = 1} ^ {m} \boldsymbol {I} _ {u , i} (R _ {u , i} - \bar {R _ {i}}) ^ {2}}{\sum_ {u = 1} ^ {m} \boldsymbol {I} _ {u , i} - 1}} \\ R _ {i}, & \end{array} \right]\tag{6}
$$

Here, $R _ { u }$ and $R _ { i }$ are the $u ^ { t h }$ user's and $i ^ { t h }$ item's mean ratings, respectively. The rating matrix is clustered in two-stages — in the first stage, we get $n _ { u }$ user clusters, where users with similar rating pattern will be grouped together using K-Means algorithm [44]. The optimal number of user clusters $( n _ { u } )$ and item clusters (n ) are chosen to optimize the accuracy and time complexity, keeping the average number of similar users and items in each cluster comparable to global average values. First, we varied the number of user clusters and chose the optimal cluster number based on accuracy, runtime, and average number of similar users and items. Next, we repeated the same process for determining the number of item clusters. However, to ensure that the final clusters are not too sparse because of over clustering, the second level of item clustering is done only for those user clusters for which the average number of interactions per user is comparable to global average interactions per user. Choosing the optimal number of user cluster and item cluster is explained in Section 6.2.1.

3.1.2. Computation of preference network and inter-item similarity network 3.1.2.1. Preference network computation. User-user similarity is generally computed by considering a vector of common ratings. However, this approach fails to consider the users' preference for a particular item category. Consider an example where a user visited ten American and two Asian restaurants but liked only one of the Asian restaurants. In this case, the user likes exploring American cuisine more often and therefore recommending American restaurants to this user is preferable. Cuisine specific preferences will not be captured in traditional way of user similarity computation.

Therefore, we construct a Preference Network which considers users implicit preferential attributes in the similarity computation stage. For each user $u ,$ the implicit Preference Vector $( P _ { u } )$ is defined as in Eq. (7) where $A _ { i }$ is the d-dimensional item attribute vector for $i ^ { t h }$ item. For example, if restaurant 1 serves American and Alcohol, restaurant 2 serves American, Alcohol, and Chinese, then $A _ { 1 } = [ 1 , 1 , 0 ] , A _ { 2 } = [ 1 , 1$ , 1] where $A _ { i 1 } \mathbf { , } A _ { i 2 } \mathbf { , } A _ { i 3 }$ correspond to American, Alcohol, and Chinese, respectively. The dimension of the attribute vectors $( d = 3$ in this example) depends on the total number of categories available among all the restaurants. We compute an average rating given by user u for all the items as shown in Eq. (8).

$$
P _ {u} = \frac {\sum_ {i = 1} ^ {n} A _ {i} \pmb {I} _ {u , i}}{\sum_ {i = 1} ^ {n} \pmb {I} _ {u , i}}\tag{7}
$$

$$
\stackrel {-} {R _ {u}} = \frac {\sum_ {i = 1} ^ {n} R _ {u , i} \pmb {I} _ {u , i}}{\sum_ {i = 1} ^ {n} \pmb {I} _ {u , i}}\tag{8}
$$

The $( d + 1 )$ dimensional User Preference Vector $( \mathcal { P } _ { u } )$ is updated by concatenating Eqs. (7) and (8) to reflect the user's implicit and explicit item preferences as $\mathcal { \hat { P } } _ { u } = P _ { u } \vert \vert _ { } R _ { u }$ . Preference vector is then standardized such that the range of attribute values are bounded in [0,1] and is denoted by $\hat { \mathcal { P } } _ { u }$ .

We compute the user preference similarity between users u and v using the cosine similarity as:

$$
P r e f S i m (u, v) = \frac {\hat {\mathcal {P}} _ {u} ^ {T} \hat {\mathcal {P}} _ {v}}{\| \hat {\mathcal {P}} _ {u} \| \| \hat {\mathcal {P}} _ {v} \|}\tag{9}
$$

We denote the Preference Network (PN) as $S _ { u , \mathcal { V } } ( \widehat { \theta } _ { U } )$ for the user u based on the preferences and define the corresponding vertex sets and edge sets as:

$$
\begin{array}{r l} & V (S _ {u, \mathcal {V}} (\theta_ {U})) = \{v \in \mathcal {V} | P r e f S i m (u, v) \geq \theta_ {U} \}, \\ & E (S _ {u, \mathcal {V}} (\theta_ {U})) = \{(u, v) \forall v \in V (S _ {u, \mathcal {V}} (\theta_ {U})) \} \end{array}\tag{10}
$$

where $\theta _ { U }$ is the threshold on PrefSim so that two users are connected by an edge in the PN and denotes the set of direct and second-hop nodes connected to user u.

3.1.2.2. Item network computation. The item-item similarity $( S i m ( i , j ) )$ between two items i and j is computed using the d-dimensional item attribute vectors using cosine similarity as shown in Eq. (9). We then denote the Item similarity network (IN) as $S _ { i , \mathcal { T } } ( \theta _ { I } )$ for item i and define the corresponding vertex sets and edge sets analogous to PN as:

$$
\begin{array}{r l} & V (S _ {i, \mathcal {I}} (\theta_ {I})) = \{j \in \mathcal {J} | S i m (i, j) \geq \theta_ {I} \}, E (S _ {i, \mathcal {I}} (\theta_ {I})) \\ & \qquad = \{(i, j) \forall j \in V (S _ {i, \mathcal {I}} (\theta_ {I})) \} \end{array}\tag{11}
$$

where denotes the set of items. Hereafter, we simplified the notations of $S _ { u , \mathcal { V } } ( \widehat { \theta } _ { U } )$ and $S _ { i , \mathcal { T } } ( \theta _ { I } )$ as $S _ { u }$ and $S _ { i } ,$ for user u and item i, respectively. The Preference Network for user set and the item similarity network for item set $\boldsymbol { \mathcal { I } }$ can be defined as $\boldsymbol { S _ { U } } = \cup _ { u \in \boldsymbol { U } } \ S _ { u }$ and $S _ { I } = \cup _ { i \in I } \ S _ { i }$ respectively.

## 3.1.3. Modeling user and item profiles (cluster-wise)

A user's (item's) latent vector is assumed to be Gaussian distributed with the mean being the average of the other similar users' (items') latent features. Thus, extending Eqs. (2) and (3), we get the following:

$$
\begin{array}{l} p (U | S _ {\mathbf {U}}, \sigma_ {U} ^ {2}, \sigma_ {S _ {\mathbf {U}}} ^ {2}) \\ = \prod_ {u = 1} ^ {m} \mathcal {N} (U _ {u} | 0, \sigma_ {U} ^ {2} I) \times \prod_ {u = 1} ^ {m} \mathcal {N} \left(U _ {u} | \frac {\sum_ {s \in S _ {u}} P r e f S i m (u , s) U _ {s}}{\sum_ {s \in S _ {u}} P r e f S i m (u , s)}, \sigma_ {S _ {\mathbf {U}}} ^ {2} I\right) \end{array}\tag{12}
$$

$$
p (V | S _ {\mathbf {I}}, \sigma_ {V} ^ {2}, \sigma_ {S _ {\mathbf {I}}} ^ {2}) = \prod_ {i = 1} ^ {n} \mathcal {N} (V _ {i} | 0, \sigma_ {V} ^ {2} \boldsymbol {I}) \times \prod_ {i = 1} ^ {n} \mathcal {N} \left(V _ {i} | \frac {\sum_ {z \in S _ {i}} S i m (i , z) V _ {z}}{\sum_ {z \in S _ {i}} S i m (i , z)}, \sigma_ {S _ {\mathbf {I}}} ^ {2} \boldsymbol {I}\right)\tag{13}
$$

From Eqs. (4), (12), and(13) and using Bayesian inference, the posterior probability of the latent features can be computed as:

$$
\begin{array}{l} p (U, V | R, S _ {\mathbf {U}}, S _ {\mathbf {I}}, \sigma_ {R} ^ {2}, \sigma_ {U} ^ {2}, \sigma_ {V} ^ {2}, \sigma_ {S _ {\mathbf {U}}} ^ {2}, \sigma_ {S _ {\mathbf {I}}} ^ {2}) \\ = \prod_ {u = 1} ^ {m} \prod_ {i = 1} ^ {n} [ \mathcal {N} (R _ {u, i} | g (U _ {u} V _ {i} ^ {T}), \sigma_ {R} ^ {2}) ] ^ {I _ {u, i}} \times \prod_ {u = 1} ^ {m} \mathcal {N} (U _ {u} | 0, \sigma_ {U} ^ {2} \boldsymbol {I}) \\ \times \prod_ {u = 1} ^ {m} \mathcal {N} \left(U _ {u} | \frac {\sum_ {s \in S _ {u}} P r e f S i m (u , s) U _ {s}}{\sum_ {s \in S _ {u}} P r e f S i m (u , s)}, \sigma_ {S _ {\mathbf {U}}} ^ {2} \boldsymbol {I}\right) \times \prod_ {i = 1} ^ {n} \mathcal {N} (V _ {i} | 0, \sigma_ {V} ^ {2} \boldsymbol {I}) \times \\ \prod_ {i = 1} ^ {n} \mathcal {N} \left(V _ {i} | \frac {\sum_ {z \in S _ {i}} S i m (i , z) V _ {z}}{\sum_ {z \in S _ {i}} S i m (i , z)}, \sigma_ {S _ {\mathbf {I}}} ^ {2} \boldsymbol {I}\right) \end{array}\tag{14}
$$

where $g ( x )$ is the modified logistic function used for bounding the predictions in range [1, 5] and is defined as:

$$
g (x) = \min _ {u \in {\bf U}, i \in {\bf I}} R _ {u, i} + \frac {\max _ {u \in {\bf U} , i \in {\bf I}} R _ {u , i} - \min _ {u \in {\bf U} , i \in {\bf I}} R _ {u , i}}{1 + e ^ {- x}}\tag{15}
$$

The log posterior probability can be obtained by taking the natural logarithm of Eq. (14).

$$
\begin{array}{r l} & {\ln (p (U, V | R, S _ {\mathbf {U}}, S _ {\mathbf {I}}, \sigma_ {R} ^ {2}, \sigma_ {\mathbf {U}} ^ {2}, \sigma_ {V} ^ {2}, \sigma_ {S _ {\mathbf {U}}} ^ {2}, \sigma_ {S _ {\mathbf {I}}} ^ {2})} \\ & {\quad = - \frac {1}{\sigma_ {R} ^ {2}} \bigg (\frac {1}{2} \sum_ {u = 1} ^ {m} \sum_ {i = 1} ^ {n} I _ {u, i} (R _ {u, i} - g (U _ {u} V _ {i} ^ {T})) ^ {2} + \frac {\sigma_ {R} ^ {2}}{\sigma_ {\mathbf {U}} ^ {2}} \frac {1}{2} \sum_ {u = 1} ^ {m} \| U _ {u} \| ^ {2} + \frac {\sigma_ {R} ^ {2}}{\sigma_ {V} ^ {2}} \frac {1}{2} \sum_ {i = 1} ^ {n} \| V _ {i} \| ^ {2}} \end{array}
$$

$$
\begin{array}{r l} & + \frac {\sigma_ {R} ^ {2}}{\sigma_ {S \mathbf {U}} ^ {2}} \frac {1}{2} \sum_ {u = 1} ^ {m} \left\| U _ {u} - \sum_ {s \in S u} \frac {P r e f S i m (u , s) U _ {s}}{\sum_ {s \in S u} P r e f S i m (u , s)} \right\| ^ {2} + \frac {\sigma_ {R} ^ {2}}{\sigma_ {S \mathbf {I}} ^ {2}} \frac {1}{2} \sum_ {i = 1} ^ {n} \left\| V _ {i} - \sum_ {z \in S _ {i}} \frac {S i m (i , z) V _ {z}}{\sum_ {z \in S _ {i}} S i m (i , z)} \right\| ^ {2}) + C ^ {\prime} \end{array}\tag{16}
$$

Assume C is the number of clusters. Hence, for each cluster $c \in \{ 1 , 2 ,$ $\cdots , C \}$ , our objective becomes minimizing the following equation (after minor re-arrangement of Eq. (16)):

$$
\begin{array}{r l} & Z ^ {c} (R ^ {c}, S _ {\mathbf {U}} ^ {c}, S _ {\mathbf {I}} ^ {c}, U ^ {c}, V ^ {c}) \\ & \quad = \frac {1}{2} \sum_ {u \in M ^ {c}} \sum_ {i \in N ^ {c}} I _ {u, i} (R _ {u, i} ^ {c} - g (U _ {u} ^ {c} V _ {i} ^ {c T})) ^ {2} + \frac {\gamma_ {U} ^ {c}}{2} \sum_ {u \in M ^ {c}} \| U _ {u} ^ {c} \| ^ {2} + \frac {\gamma_ {V} ^ {c}}{2} \sum_ {i \in N ^ {c}} \| V _ {i} ^ {c} \| ^ {2} \\ & \quad + \frac {k _ {U} ^ {c}}{2} \sum_ {u \in M ^ {c}} \left\| U _ {u} ^ {c} - \sum_ {s \in S _ {u} ^ {c}} \frac {\text {PrefSim} (u , s) U _ {s} ^ {c}}{\sum_ {s \in S _ {u} ^ {c}} \text {PrefSim} (u , s)} \right\| ^ {2} + \frac {k _ {V} ^ {c}}{2} \sum_ {i \in N ^ {c}} \left\| V _ {i} ^ {c} - \sum_ {\substack {z \in S _ {i} ^ {c}}} \frac {\text {Sim} (i , z) V _ {z} ^ {c}}{\sum_ {z \in S _ {i} ^ {c}} \text {Sim} (i , z)} \right\| ^ {2} \\ & \quad + \frac {\gamma_ {U} ^ {c}}{2} \sum_ {\substack {\mathcal {O} (u, s) = 0 \\ \mathcal {O} (u, s) = 0}} \frac {\text {PrefSim} (u , s) U _ {s} ^ {c}}{\sum_ {\mathcal {O} (u , s)} \text {PrefSim} (u , s)} \Bigg \| ^ {2}. \end{array}\tag{17}
$$

where $( \lVert \cdot \rVert )$ denotes the Frobenius norm<sup>3</sup>. $S _ { u } ^ { c }$ and $S _ { i } ^ { c }$ denote the set of similar users and items for user u and item i in cluster $c ,$ respectively. The hyper-parameters related to the Bayesian variances are as follows:

![](/api/attachments/66R5P5S3/fulltext/images/c5181837df684afb9d3c49fb3bb17204fcc0830b8e1531c47ab62086146ab688.jpg)  
Fig. 1. Graphical representation of CREPE MF.

$\begin{array} { r } { \gamma _ { U } ^ { c } = \frac { \sigma _ { R } ^ { c 2 } } { \sigma _ { U } ^ { c 2 } } , \gamma _ { V } ^ { c } = \frac { \sigma _ { R } ^ { c 2 } } { \sigma _ { V } ^ { c 2 } } , k _ { U } ^ { c } = \frac { \sigma _ { R } ^ { c 2 } } { \sigma _ { S _ { \mathrm { U } } } ^ { c } 2 } , k _ { V } ^ { c } = \frac { \sigma _ { R } ^ { c 2 } } { \sigma _ { S _ { \mathrm { I } } } ^ { c 2 } } } \end{array}$ . Here $R ^ { c } , U ^ { c } , V ^ { c }$ are the useritem ratings matrix, user, and item latent features in cluster c. $\gamma _ { U } ^ { c } , \gamma _ { V } ^ { c } , k _ { U } ^ { c } ,$ k<sup>c</sup> are the hyper-parameters and $M ^ { c } , N ^ { c }$ are the sets of user and items with respect to the cluster c. Also, $S _ { U } ^ { c }$ is a subgraph of $s _ { U }$ containing all the nodes present in $M ^ { c } . S _ { I } ^ { c }$ is defined analogous to $S _ { U } ^ { c }$ Algorithm 1. Two-stage Rating Pattern Clustering

interactions per user for proceeding to second-stage item clustering. This step helps to avoid over-fitting for small user clusters. The outputs of this algorithm are a set of user clusters, a set of item clusters, and the corresponding rating matrix (line 21, Algorithm 1).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input:  $R, n_{u}, n_{i}, \delta$ 
2: Return: M, N, R
3: Use K-Means to cluster M users into  $\{UC_{1}, UC_{2}, ..., UC_{n_{u}}\}$  clusters in U space
4: Initialize:  $c \leftarrow 1$ ,  $M \leftarrow \emptyset$ ,  $N \leftarrow \emptyset$ ,  $R \leftarrow \emptyset$ 
5: for  $x \in \{1, ..., n_{u}\}$  do
6:    $Temp \leftarrow \{j | R_{v,j} \neq 0 \quad \forall v \in UC_{x}\}$ 
7:    if  $|UC_{x}| \leq \delta$  then
8:    $M^{c} \leftarrow UC_{x}$ 
9:    $N^{c} \leftarrow Temp$ 
10:    $R^{c} \leftarrow [R_{m,n}]_{|M^{c}| \times |N^{c}|}$  s.t.  $I_{m,n} \neq 0$ 
11:    $c \leftarrow c + 1$ 
12:    else
13:    Use K-Means to cluster Temp items into  $\{IC_{1}, IC_{2}, ..., IC_{n_{i}}\}$  clusters in I space
14:    for  $y \in \{1, ..., n_{i}\}$  do
15:    $M^{c} \leftarrow UC_{x}$ 
16:    $N^{c} \leftarrow IC_{y}$ 
17:    $R^{c} \leftarrow [R_{m,n}]_{|M^{c}| \times |N^{c}|}$  s.t.  $I_{m,n} \neq 0$ 
18:    $c \leftarrow c + 1$ 
19:  $c \leftarrow c - 1$ 
20:  $M \leftarrow \{M^{1}, M^{2}, ..., M^{c}\}$ ,  $N \leftarrow \{N^{1}, N^{2}, ..., N^{c}\}$ ,  $R \leftarrow \{R^{1}, R^{1}, ..., R^{c}\}$ 
21: return(M, N, R)
</div>

The details of the Two-stage Rating Pattern Clustering Algorithm have been presented in Algorithm 1. The algorithm explains the process of clustering m users, n items into $n _ { u }$ user-clusters and $n _ { i }$ item-clusters, respectively, based on the rating patterns (Eqs. (5), (6)). Initially, the users are clustered into $n _ { u }$ user-clusters based on their rating history using K-Means clustering algorithm (line $^ { 3 , }$ Algorithm 1). Each of the user clusters will have a set of items rated by the users. These items are then clustered into $n _ { i }$ item-clusters using K-Means clustering algorithm (Eq. (6)). However, to ensure that there are suficient number of interactions in each user cluster, we fix a predefined threshold (line $^ { 7 , }$ Algorithm 1). This threshold reflects the number of interactions per user and for each cluster it should be comparable to global average

3.1.3.1. Gradient optimization. Eqs. (18) and (19) represent the partial derivatives of the objective function (Eq. (17)) with respect to the latent features.

$$
\begin{array}{r l} \frac {\partial Z ^ {c}}{\partial U _ {u} ^ {c}} = & \sum_ {i \in N ^ {c}} I _ {u, i} V _ {i} ^ {c} g ^ {\prime} (U _ {u} ^ {c} V _ {i} ^ {c T}) (g (U _ {u} ^ {c} V _ {i} ^ {c T}) - R _ {u, i} ^ {c}) + \gamma_ {U} ^ {c} U _ {u} ^ {c} + k _ {U} ^ {c} \\ & \left(U _ {u} ^ {c} - \frac {\sum_ {s \in S _ {u} ^ {c}} P r e f S i m (u , s) U _ {s} ^ {c}}{\sum_ {s \in S _ {u} ^ {c}} P r e f S i m (u , s)}\right) \\ & - k _ {U} ^ {c} \frac {\sum_ {\{s | u \in S _ {s} ^ {c} \}} P r e f S i m (s , u) \left(U _ {s} ^ {c} - \frac {\sum_ {p \in S _ {s} ^ {c}} P r e f S i m (s , p) U _ {p} ^ {c}}{\sum_ {p \in S _ {s} ^ {c}} P r e f S i m (s , p)}\right)}{\sum_ {\{s | u \in S _ {s} ^ {c} \}} P r e f S i m (s , u)} \end{array}\tag{18}
$$

![](/api/attachments/66R5P5S3/fulltext/images/b396410859cb328baf02622340617ae77e0cfe74b9455057e96f60b04a32fae3.jpg)  
Fig. 2. Illustration of geographical filtering for one arbitrary item.

$$
\begin{array}{l} \frac {\partial Z ^ {c}}{\partial V _ {i} ^ {c}} = \sum_ {u \in M ^ {c}} I _ {u, i} U _ {u} ^ {c} g ^ {\prime} (U _ {u} ^ {c} V _ {i} ^ {c T}) (g (U _ {u} ^ {c} V _ {i} ^ {c T}) - R _ {u, i} ^ {c}) + \gamma_ {V} ^ {c} V _ {i} ^ {c} + k _ {V} ^ {c} \\ \qquad \qquad \qquad \left(V _ {i} ^ {c} - \frac {\sum_ {z \in S _ {i} ^ {c}} S i m (i , z) V _ {z} ^ {c}}{\sum_ {z \in S _ {i} ^ {c}} S i m (i , z)}\right) \\ - k _ {V} ^ {c} \frac {\sum_ {\{z | i \in S _ {z} ^ {c} \}} S i m (z , i) \biggl (V _ {z} ^ {c} - \frac {\sum_ {r \in S _ {\xi} ^ {c}} S i m (z , r) V _ {r} ^ {c}}{\sum_ {r \in S _ {\xi} ^ {c}} S i m (z , r)} \biggr)}{\sum_ {\{z | i \in S _ {z} ^ {c} \}} S i m (z , i)} \end{array}\tag{19}
$$

where $\begin{array} { r } { g ^ { \prime } ( x ) = \frac { ( \operatorname* { m a x } _ { u \in { \mathbf { U } } , i \in { \mathbf { I } } } R _ { u , i } - \operatorname* { m i n } _ { u \in { \mathbf { U } } , i \in { \mathbf { I } } } R _ { u , i } ) e ^ { - x } } { ( 1 + e ^ { - x } ) ^ { 2 } } } \end{array}$ , is the derivative of the lo gistic function.

$U _ { u } ^ { c }$ and $V _ { i } ^ { c }$ can be updated iteratively in the Gradient Optimization approach (e.g.: Gradient Descent, Stochastic Gradient Descent, etc.) using Eqs. (18) and (19). Fig. 1, the graphical representation for CREPE MF, shows an arbitrary cluster c incorporating preference and item network in the basic PMF model, thereby propagating trust through similar users and items.

## 3.2. Incorporating geographical influence in CREPE MF

Item network in the proposed CREPE MF model consists of similar items where similarity between two items should be above a predefined threshold $( \theta _ { I } , \ \mathrm { E q } . \ ( 1 1 ) )$ . However, the item network size here solely depends on the value of $\theta _ { I } - \mathbf { a }$ low threshold value can increase the size drastically. Moreover, in such a process the geographical proximity of the items is overlooked, particularly, in case of venue recommendations which is highly undesirable. Also, as discussed in Section 2.4.1.3 users' mobility is constrained geographically by the distance they travel within a day and their check-ins can be Geo-spatially clustered. Therefore, we propose a new model, gCREPE MF (Geographical CREPE MF), which incorporates geographical influence of similar items. Herein, we redefine the item similarity network (IN) for item i, (defined in Eq. (11)). In the modified item-similarity network (IN<sup>′</sup>), each item i is connected with top k similar items situated within r radius from i. Hence. the modified IN' for item i is denoted as $S _ { g _ { i , \mathcal { T } } } ( r , k )$ and the vertex set is defined as:

$$
V (S _ {g _ {i, \mathcal {J}}} (r, k)) = \{j \in \mathcal {J} | g (i, j) \leq r \quad \text { and } \quad p o s (j, S i m _ {i \mathcal {J}}) \leq k) \}\tag{20}
$$

$$
S i m _ {i, \mathcal {J}} = (s _ {j} | s _ {j} = s i m (i, j) \quad \forall j \in \mathcal {J}) \quad \forall i \in \mathbf {I}\tag{21}
$$

where $\mathcal { T }$ denotes the set of items, $g ( i , j )$ denotes the geographical distance between items i and $j . S i m _ { i , \mathcal { I } }$ is the ordered set of similarity values of item i with all other items ( ). The illustration of gCREPE MF with respect to one arbitrary item is depicted in Fig. 2. In Stage 1, all the items are clustered into their respective homogeneous clusters using K-Means for identifying rating bubbles. In Stage 2, all the items that belong to “Item Cluster 1” are filtered. Subsequently, in the next stage for each item, $\cdot _ { r }$ radius distance is drawn and the neighboring items are identified. Finally, in the last stage, top ‘k’ items that are highly similar to focal items are selected based on item similarity.

Hereafter, we simplified the notations of $S _ { g _ { i } , \mathcal { T } } ( r , k )$ as $S _ { g _ { i } }$ for item i. Hence, IN<sup>′</sup> for item set I becomes $S _ { g _ { I } } = \cup _ { i \in I } S _ { g _ { i } } \forall i \in I .$ . Construction of IN<sup>′</sup> ensures that size of the network is deterministic (depends on the fixed value of k) and almost all items are included in the network.

Let ${ S _ { g } } _ { i } ^ { c }$ be the modified item-network for item i belonging to cluster c. Our objective now becomes minimizing the following equation (derived from Eq. (17)):

$$
\begin{array}{l} Z ^ {c} (R ^ {c}, S _ {\mathrm{U}} ^ {c}, S _ {g \mathrm{I}} ^ {c}, U ^ {c}, V ^ {c}) \\ = \frac {1}{2} \sum_ {u \in M ^ {c}} \sum_ {i \in N ^ {c}} I _ {u}, i (R _ {u, i} ^ {c} - g (U _ {u} ^ {c} V _ {i} ^ {c T})) ^ {2} + \frac {\gamma_ {U} ^ {c}}{2} \sum_ {u \in M ^ {c}} \| U _ {u} ^ {c} \\ \| ^ {2} + \frac {\gamma_ {V} ^ {c}}{2} \sum_ {i \in N ^ {c}} \| V _ {i} ^ {c} \| ^ {2} \\ + \frac {k _ {U} ^ {c}}{2} \sum_ {u \in M ^ {c}} \| U _ {u} ^ {c} - \sum_ {s \in S _ {u} ^ {c}} \frac {\text {PrefSim} (u , s) U _ {s} ^ {c}}{\sum_ {s \in S _ {u} ^ {c}} \text {PrefSim} (u , s)} \| ^ {2} + \frac {k _ {V} ^ {c}}{2} \sum_ {i \in N ^ {c}} \| V _ {i} ^ {c} - \\ \sum_ {z \in S _ {g _ {i} ^ {c}}} \frac {\text {Sim} (i , z) V _ {z} ^ {c}}{\sum_ {z \in S _ {g _ {i} ^ {c}}} \text {Sim} (i , z)} \| ^ {2} \end{array}\tag{22}
$$

Partial derivatives of the objective function as shown in Eq. (22) with respective to item latent features are derived as follows:

$$
\begin{array}{l} \frac {\partial Z ^ {c}}{\partial V _ {i} ^ {c}} = \sum_ {u \in M ^ {c}} I _ {u, i} U _ {u} ^ {c} g ^ {\prime} (U _ {u} ^ {c} V _ {i} ^ {c T}) (g (U _ {u} ^ {c} V _ {i} ^ {c T}) - R _ {u, i} ^ {c}) \\ + \gamma_ {V} ^ {c} V _ {i} ^ {c} + k _ {V} ^ {c} \left(V _ {i} ^ {c} - \frac {\sum_ {z \in S _ {g _ {i}} ^ {c}} S i m (i , z) V _ {z} ^ {c}}{\sum_ {z \in S _ {g _ {i}} ^ {c}} S i m (i , z)}\right) \\ - k _ {V} ^ {c} \frac {\sum_ {\{z | i \in S _ {g _ {z}} ^ {c} \}} S i m (z , i) \left(V _ {z} ^ {c} - \frac {\sum_ {r \in S _ {g _ {z}} ^ {c}} S i m (z , r) V _ {r} ^ {c}}{\sum_ {r \in S _ {g _ {z}} ^ {c}} S i m (z , r)}\right)}{\sum_ {\{z | i \in S _ {g _ {z}} ^ {c} \}} S i m (z , i)} \end{array}\tag{23}
$$

The partial derivatives of the objective function with respective to user latent features will remain the same as in Eq. (18).

## 4. Complexity computation

Let there be M users, $S _ { u }$ similar users, N items, and $S _ { i }$ similar items spread across $n _ { u }$ user clusters and $n _ { i }$ item clusters. Both the user clusters and item clusters are mutually exclusive. Then we have,

$$
M = \sum_ {x = 1} ^ {n _ {u}} M ^ {x}; \quad S _ {u} = \sum_ {x = 1} ^ {n _ {u}} S _ {u} ^ {x}; \quad N = \sum_ {y = 1} ^ {n _ {i}} N ^ {y}; \quad S _ {i} = \sum_ {y = 1} ^ {n _ {i}} S _ {i} ^ {y}\tag{24}
$$

Time complexity of our algorithm is mainly contributed by the gradient update step. The computational complexity of the user feature update step (Eq. (18)) is $O ( M l + M S _ { u } ^ { 2 } )$ . Our approach is closely similar to Social MF [21] where the computational complexity is derived as $O ( M l r + M S _ { u } ^ { 2 } l )$ , l being the dimension of latent features and r being average number of ratings per user. Since rating matrix is sparse, r is relatively small. Also ( )l is constant and practically taken as a small number, the complexity for updating user features can be approximated as $O ( M + M S _ { u } ^ { 2 } )$ . Similarly, the complexity for updating item features can be expressed as $O ( N + N S _ { i } ^ { 2 } )$ . Hence, for a single iteration the gradient update costs:

$$
O (M + N + M S _ {u} ^ {2} + N S _ {i} ^ {2}) \approx O (M S _ {u} ^ {2} + N S _ {i} ^ {2})\tag{25}
$$

Hence, in terms of the cluster number we have the complexity as

$$
O (M S _ {u} ^ {2} + N S _ {i} ^ {2}) = O \left(\sum_ {x = 1} ^ {n _ {u}} M ^ {x} \left(\sum_ {x = 1} ^ {n _ {u}} S _ {u} ^ {x}\right) ^ {2} + \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \left(\sum_ {y = 1} ^ {n _ {i}} S _ {i} ^ {y}\right) ^ {2}\right)\tag{26}
$$

It can be shown that

$$
\begin{array}{l} \sum_ {x = 1} ^ {n _ {u}} M ^ {x} \left(\sum_ {x = 1} ^ {n _ {u}} S _ {u} ^ {x}\right) ^ {2} \\ \qquad = \sum_ {x = 1} ^ {n _ {u}} M ^ {x} (S _ {u} ^ {x}) ^ {2} + \sum_ {x = 1} ^ {n _ {u}} M ^ {x} \sum_ {\nu \neq x = 1} ^ {n _ {u}} (S _ {u} ^ {\nu}) ^ {2} + \sum_ {x = 1} ^ {n _ {u}} M ^ {x} \sum_ {x = 1} ^ {n _ {u}} S _ {u} ^ {x} \sum_ {\nu > x} ^ {n _ {u}} S _ {u} ^ {\nu} \\ \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \left(\sum_ {y = 1} ^ {n _ {i}} S _ {i} ^ {y}\right) ^ {2} \\ \qquad = \sum_ {y = 1} ^ {n _ {i}} N ^ {y} (S _ {i} ^ {y}) ^ {2} + \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \sum_ {j \neq y = 1} ^ {n _ {i}} (S _ {i} ^ {j}) ^ {2} + \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \sum_ {y = 1} ^ {n _ {i}} S _ {i} ^ {y} \sum_ {j > y} ^ {n _ {i}} S _ {i} ^ {j} \end{array}\tag{27}
$$

(28)

From Eqs. (27) and (28), the computational complexity of the un clustered algorithm is:

$$
\begin{array}{l} O \Bigg (\sum_ {x = 1} ^ {n _ {u}} M ^ {x} (S _ {u} ^ {x}) ^ {2} + \sum_ {x = 1} ^ {n _ {u}} M ^ {x} \sum_ {v \neq x = 1} ^ {n _ {u}} (S _ {u} ^ {v}) ^ {2} + \sum_ {x = 1} ^ {n _ {u}} M ^ {x} \sum_ {x = 1} ^ {n _ {u}} S _ {u} ^ {x} \sum_ {v > x} ^ {n _ {v}} S _ {u} ^ {v} + \\ \sum_ {y = 1} ^ {n _ {i}} N ^ {y} (S _ {i} ^ {y}) ^ {2} \\ + \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \sum_ {j \neq y = 1} ^ {n _ {i}} (S _ {i} ^ {j}) ^ {2} + \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \sum_ {y = 1} ^ {n _ {i}} S _ {i} ^ {y} \sum_ {j > y} ^ {n _ {i}} S _ {i} ^ {j} \Bigg) \end{array}\tag{29}
$$

## 4.1. Complexity computation for CREPE MF

Let us investigate the complexity of our first clustered algorithm, $\mathrm { i . e . , }$ CREPE MF. The derivation of the complexity for CREPE MF is explained using a simple example. The entire user space M is clustered into three user clusters and the entire item space N is clustered into two item clusters. For simplicity, we assume that each user cluster has same set of item clusters. In practice, some of these item clusters will be null or in other words, some of these user clusters will not be clustered further. The complexity of the model for the first user cluster $M ^ { 1 }$ is expressed as:

$$
O (M ^ {1} (S _ {u} ^ {1}) ^ {2} + N ^ {1} (S _ {i} ^ {1}) ^ {2} + M ^ {1} (S _ {u} ^ {1}) ^ {2} + N ^ {2} (S _ {i} ^ {2}) ^ {2})\tag{30}
$$

Hence, we can express the complexity of the entire model as follows:

$$
O (2 (M ^ {1} (S _ {u} ^ {1}) ^ {2} + M ^ {2} (S _ {u} ^ {2}) ^ {2} + M ^ {3} (S _ {u} ^ {3}) ^ {2}) + 3 (N ^ {1} (S _ {i} ^ {1}) ^ {2} + N ^ {2} (S _ {i} ^ {2}) ^ {2}))\tag{31}
$$

Therefore, the complexity of a two-level cluster algorithm with $n _ { u }$ user clusters and $n _ { i }$ item clusters is derived as follows:

$$
O \left(n _ {i} \sum_ {x = 1} ^ {n _ {u}} M ^ {x} (S _ {u} ^ {x}) ^ {2} + n _ {u} \sum_ {y = 1} ^ {n _ {i}} N ^ {y} (S _ {i} ^ {y}) ^ {2}\right)\tag{32}
$$

Without loss of generalizability, let us assume that number of users (items) in all user (item) clusters are same, number of similar users (items) in all user (item) clusters are same to mitigate the mathematical complexity, i.e.,

$$
| M ^ {1} | = | M ^ {2} | = \ldots = | M ^ {x} | = m; \quad | S _ {u} ^ {1} | = | S _ {u} ^ {2} | = \ldots = | S _ {u} ^ {x} | = s _ {u}\tag{33}
$$

$$
| N ^ {1} | = | N ^ {2} | = \ldots = | N ^ {y} | = n; \quad | S _ {i} ^ {1} | = | S _ {i} ^ {2} | = \ldots = | S _ {i} ^ {y} | = s _ {i}\tag{34}
$$

Using Eq. (33) and $^ { 3 4 , }$ , we re-arrange Eq. (29) as follows:

$$
\begin{array}{r l} & n _ {u} \cdot m (s _ {u}) ^ {2} + n _ {u} \cdot (n _ {u} - 1) \cdot m (s _ {u}) ^ {2} + \frac {n _ {u} ^ {2} \cdot (n _ {u} - 1) \cdot m (s _ {u}) ^ {2}}{2} + n _ {i} \cdot n (s _ {i}) ^ {2} \\ & + n _ {i} \cdot (n _ {i} - 1) \cdot n (s _ {i}) ^ {2} + \frac {n _ {i} ^ {2} \cdot (n _ {i} - 1) \cdot n (s _ {i}) ^ {2}}{2} \end{array}\tag{35}
$$

Similarly, the complexity for a two-level cluster algorithm (see Eq. (32)) can be re-written as:

$$
n _ {u} \cdot n _ {i} \cdot m (s _ {u}) ^ {2} + n _ {u} \cdot n _ {i} \cdot n (s _ {i}) ^ {2}\tag{36}
$$

Hence, reduction in complexity due to clustering is as follows:

$$
\begin{array}{r l} & {(n _ {u} - n _ {i}) \cdot n _ {u} \cdot m (s _ {u}) ^ {2} + \frac {n _ {u} ^ {2} \cdot (n _ {u} - 1) \cdot m (s _ {u}) ^ {2}}{2} + (n _ {i} - n _ {u}) \cdot n _ {i} \cdot n (s _ {i}) ^ {2}} \\ & {+ \frac {n _ {i} ^ {2} \cdot (n _ {i} - 1) \cdot n (s _ {i}) ^ {2}}{2}} \end{array}\tag{37}
$$

generalizes to

$$
\begin{array}{l} (n _ {u} - n _ {i}) \sum_ {x = 1} ^ {n _ {u}} M ^ {x} (S _ {u} ^ {x}) ^ {2} + \sum_ {x = 1} ^ {n _ {u}} M ^ {x} \sum_ {x = 1} ^ {n _ {u}} S _ {u} ^ {x} \sum_ {v > x} ^ {n _ {u}} S _ {u} ^ {v} + (n _ {i} - n _ {u}) \sum_ {y = 1} ^ {n _ {i}} N ^ {y} (S _ {i} ^ {y}) ^ {2} \\ + \sum_ {y = 1} ^ {n _ {i}} N ^ {y} \sum_ {y = 1} ^ {n _ {i}} S _ {i} ^ {y} \sum_ {v > y} ^ {n _ {i}} S _ {i} ^ {j} > 0 \forall n _ {u}, n _ {i} > 0 \end{array}\tag{38}
$$

From Eq. (38), it is evident that the number of user clusters $( n _ { u } )$ and item clusters (n ) play an important role in determining the reduction in complexity (along with accuracy) and hence have to be chosen carefully. If clustering is stopped at stage 1, the complexity of CREPE MF may increase compared to unclustered model, depending on the number of users and items in the system. Here, we assume that a focal user and all his similar users are clustered together. In practice this assumption holds good due to the fact that the preference network for a focal user is computed using both rating patterns as well as the business attributes. However, terminating at stage 1 might prove eficient when the focal user and some of his similar connections fall in different clusters. This is evident from Eq. (32) as the number of similar users $( S _ { u } ^ { x } )$ has a quadratic efect. In our experiments, we varied $n _ { u }$ and n to see the efect of cluster numbers. The reduction in time complexity has been shown experimentally in Section 5.2.3.3. We argue that a further reduction in complexity can be achieved by executing the algorithm for each cluster in parallel as the clusters are mutually exclusive. Hence, the time complexity of CREPE MF reduces to time taken to execute the biggest cluster. Therefore, Eq. (32) can be reduced to:

$$
\mathcal {O} \max _ {x \in \{1, 2, \dots , n _ {u} \}, y \in \{1, 2, \dots , n _ {i} \}} (M ^ {x} (S _ {u} ^ {x}) ^ {2} + N ^ {y} (S _ {i} ^ {y}) ^ {2})\tag{39}
$$

## 4.2. Computational complexity for gCREPE MF

For CREPE MF, we considered $S _ { i }$ as set of similar items of item i located in the entire geography under consideration. In gCREPE MF, $S _ { g i }$ is considered as set of top k similar items within radius r around item i. From Eq. (32), the runtime complexity for gCREPE MF can then be derived as $\begin{array} { r } { O \Big ( n _ { i } \sum _ { x = 1 } ^ { n _ { u } } M ^ { x } ( S _ { u } ^ { x } ) ^ { 2 } + n _ { u } \sum _ { y = 1 } ^ { n _ { i } } N ^ { y } ( S _ { g _ { i } } { } ^ { y } ) ^ { 2 } \Big ) } \end{array}$ . It is evident that $S _ { g i }$ ≪ $S _ { i } .$ Therefore, we have,

$$
\begin{array}{l} O \left(n _ {i} \sum_ {x = 1} ^ {n _ {u}} M ^ {x} (S _ {u} ^ {x}) ^ {2} + n _ {u} \sum_ {y = 1} ^ {n _ {i}} N ^ {y} (S _ {g _ {i}} ^ {y}) ^ {2}\right) \\ <   O \left(n _ {i} \sum_ {x = 1} ^ {n _ {u}} M ^ {x} (S _ {u} ^ {x}) ^ {2} + n _ {u} \sum_ {y = 1} ^ {n _ {i}} N ^ {y} (S _ {i} ^ {y}) ^ {2}\right) \end{array}\tag{40}
$$

The reduction in runtime for gCREPE MF greatly depends on the number of k nearest neighbors as k determines the size of $S _ { g _ { i } } .$ The reduction in runtime has been reported in Section 5.2.3.3 by varying the value of k.

Table 1 Dataset description.

<table><tr><td>Description</td><td>Phoenix — Restaurants (Yelp)</td><td>Toronto — Restaurants (Yelp)</td><td>Phoenix — Other Businesses (Yelp)</td><td>Chicago — All Businesses (Gowalla)</td></tr><tr><td># Users</td><td>14,198</td><td>8082</td><td>13,942</td><td>11,587</td></tr><tr><td># Businesses</td><td>3233</td><td>6193</td><td>9752</td><td>10,901</td></tr><tr><td># Friends</td><td>99,464</td><td>38,923</td><td>90,144</td><td>27,826</td></tr><tr><td># Nodes in Preference-Network</td><td>197,564</td><td>153,887</td><td>334,710</td><td>87,812</td></tr><tr><td>%Friends who are similar</td><td>9.5%</td><td>14.3%</td><td>11.1%</td><td>4.7%</td></tr><tr><td># Nodes in Item-Similarity Network</td><td>171,510</td><td>517,118</td><td>523,990</td><td>796,499</td></tr><tr><td>% of Items in Item-Similarity Network</td><td>98.48%</td><td>99.68%</td><td>82.27%</td><td>79.09%</td></tr><tr><td># Ratings</td><td>130,881</td><td>143,673</td><td>120,080</td><td>147,832</td></tr><tr><td>Standard Deviation of Ratings</td><td>1.1853</td><td>1.1184</td><td>1.2955</td><td>0.8416</td></tr><tr><td>Ratings Sparsity</td><td>99.72%</td><td>99.71%</td><td>99.91%</td><td>99.89%</td></tr><tr><td>% Visits less than 15 km</td><td>81.39%</td><td>93.07%</td><td>76.74%</td><td>86.11%</td></tr><tr><td>% Visits less than 10 km</td><td>68.07%</td><td>84.04%</td><td>61.19%</td><td>75.14%</td></tr></table>

![](/api/attachments/66R5P5S3/fulltext/images/fb9c61e28c34fe31b584e230082bdde136a15eb30eda5452055e27cdc5085483.jpg)  
Fig. 3. Rating distribution.

## 5. Experimental results

## 5.1. Data set description

We have evaluated our proposed method using two publicly avail able data sets commonly used in the literature [29, 45], one from Yelp data set challenge 2017, Round 9<sup>4</sup> and the other from Gowalla [46], a location based social networking site. Both data sets contain users' social connections and location details of the physical entities which are essential for construction of user-preference network and location-enhanced item-similarity network in the proposed two models, CREPE MF and gCREPE MF. While user-business interactions in Yelp data set is in the form of ratings and reviews, Gowalla provides users' check-in in formation. The statistics of the data sets are given in Table 1. In both the data sets, several business categories such as restaurants, shopping, local services, etc. are present and the businesses are spread across multiple states in diferent countries like the United States of America (USA), Canada, Germany, and United Kingdom (UK). For this study, we have considered four subsets of the data; two sets from Yelp on restaurants from two big cities Phoenix (Arizona, USA) and Toronto (Ontario, Canada) which are geographically diverse. The third data set (Yelp) contains all business categories except restaurants located in Phoenix (Arizona, USA) and the fourth one contains all business from Gowalla located in Chicago (Illinois, USA). The third subset which contains all categories except restaurants was again chosen from Phoenix because this city is bigger (higher number of user-item interactions) compared to Toronto and also Phoenix data set is more frequently used in the literature [29, 47]. The fourth subset considered is Chicago (Gowalla) which has comparable number of user-item interactions and users with respect to the other three subsets from Yelp.

Notably, higher number of interactions will ensure adequate data for both training and test sets and therefore will reflect appropriate performance of the models in terms of accuracy. Subsets having comparable number of users/items is also necessary to ensure fair comparison of runtime (since the size of user-preference/item-similarity network is dependent on number of users/items). However, since it is dificult to find subsets which have all three numbers (number of user, items, and interactions) comparable, we chose number of users and number of interactions, which are broadly comparable for all four subsets, as selecting criteria and relaxed on number of items. The third and fourth data sets contain a diverse set of business categories like Arts & Entertainment, Health & Medical, Religious Organizations, etc. which are very diferent from restaurants. This is to ensure that our proposed model can be applicable to other business categories and also to validate that our findings are not data set dependent.

Yelp provides a detailed list of business attributes either tagged by business or the users themselves. However, many of these attributes are closely associated. To reduce this redundancy we manually grouped the closely related attributes into ten broad categories for restaurants and twenty broad categories for other businesses. For example: American New, American Traditional, Bagels, Burger, etc. are grouped into ‘American’ category for restaurants and Automotive, Auto Repair, Tires, etc. are grouped into ‘Automotive’ category. For this task, we employed two experts to independently categorize the attributes into bins. The experts were then asked to exchange the category mapping with each other. Final mapping was derived after the experts mutually agreed with the final categorization. Preference network and the item-item similarity network have been constructed as discussed in Sections 3.1.2.1 and 3.1.2.2 using the mapped categories. The data set also includes the users' social network connections (c.f: Table 1).

The fourth subset was taken from Gowalla, a popular LBSN tracking more than 600,000 users' check-in activities since November 2010 [46]. The data set comprises of user profiles, user's friendship network business location information, and users' check-in history before June 01, 2011. The businesses are categorized into seven broad categories, namely Community, Entertainment, Food, Nightlife, Outdoors, Shopping, and Travel. For obtaining user-item preference matrix based on number of check-ins, an approach similar to Yang et al. in Ref. [25] has been followed where one check-in corresponds to 1 star rating, two check-ins to 2 star rating, three check-ins to 3 star rating, four check-ins to 4 star rating, five or more check-ins to 5 star rating. In addition, Yang et al. enhanced the preference matrix using the sentiments extracted from tip data [25]. However, due to the unavailability of tip data, we skipped the step. For this study, we have considered all the businesses that are located in Chicago City. The data set description can be found in Table 1.

![](/api/attachments/66R5P5S3/fulltext/images/aba6125b7988ec2d7ff6167dbd81a17d07eb1ec024655bdb19c16172f57f1e9c.jpg)  
Fig. 4. Cumulative distribution of pairwise distance: Phoenix — Restaurants (Yelp).

## 5.1.1. Observations

A careful investigation on both the data sets reveal that on an average only a small percentage (c.f.: Table 1) of users' social network friends have similar preferences. This as well indicates that consideration of preference similarity among users might improve the accuracy of predictions. The experimental validation for this finding has been reported in Section 6.1.

Next, we analyzed the distribution of ratings for both the data sets. As seen from Fig. 3, the rating distribution is very diferent for Yelp and Gowalla. In Yelp data set, we can see most of the users are high raters (users tend to rate above 3). In Gowalla data set, most of the users have made 1 check-in and ratings (derived from check-ins) follow a unimodal distribution peaking at 1 with low standard deviation (0.8416) (cf: Table 1). Choosing Gowalla data set can potentially reduce the validity of the results as the data is skewed towards left. However, finding another alternative data set was dificult for the reasons mentioned earlier in Section 5.1. Nevertheless, achieving good improvement in accuracy compared to benchmark models becomes challenging because even simply predicting all 1 will yield a good accuracy here. We have experimentally verified the robustness of our algorithm in terms of accuracy in Section 5.2.3.2.

Finally, the impact of distance on a user's visits to venues has been investigated. To measure this, we calculated the distance between all pairs of venues a user has visited and analyzed the results. In Phoenix-Restaurants (Yelp) data set, it has been observed that on average, 81.39% of user-visits are located within 15 km radius and 68.07% of user-visits fall within 10 km radius. From Fig. 4, it can be observed that majority of users visit restaurants which are closer to each other. In other words, the restaurants visited by a user are geographically colocated (Fig. 5). Similar pattern has been observed in the other three data sets as well, (c.f: Table 1). Therefore, we consider venues situated within k km radius for locating similar neighbors. The newly con structed inter-item similarity network will ensure the items are similar to focal item both in terms of venue attributes as well as the distance between them. Further, it will reduce the time taken as the task is now reduced to finding similar items within k km radius and not the entire geography in concern. We have experimentally validated the impact of distance in Section 6.3.

![](/api/attachments/66R5P5S3/fulltext/images/f8e8e9a0b02eb86404d9bd617bdcb493297c431a2f8ae6a614ba759671c6d2a1.jpg)  
Fig. 5. Geographical clustering pattern seen in user visits: Phoenix — Restaurants (Yelp).

Table 2  
Specification of parameters (α is the learning rate of Gradient Descent method).

<table><tr><td>Dataset</td><td>Model</td><td> $\alpha$ </td><td> ${\gamma }_{U}$ </td><td> ${\gamma }_{V}$ </td><td> ${k}_{U}$ </td><td> ${k}_{V}$ </td><td># iterations</td></tr><tr><td rowspan="6">Phoenix — Restaurants (Yelp)</td><td>PMF</td><td>0.006</td><td>0.01</td><td>0.01</td><td>NA</td><td>NA</td><td>300</td></tr><tr><td>SocialMF</td><td>0.0012</td><td>0.01</td><td>0.01</td><td>5</td><td>NA</td><td>300</td></tr><tr><td>SocReg</td><td>0.001</td><td>0.01</td><td>0.01</td><td>0.000001</td><td>NA</td><td>300</td></tr><tr><td>LBSMF</td><td>0.0013</td><td>0.01</td><td>0.01</td><td>1.3</td><td>10</td><td>300</td></tr><tr><td>CREPE MF</td><td>0.0028</td><td>0.01</td><td>0.01</td><td>28</td><td>10</td><td>300</td></tr><tr><td>gCREPE MF</td><td>0.0028</td><td>0.01</td><td>0.01</td><td>28</td><td>10</td><td>300</td></tr><tr><td rowspan="6">Toronto — Restaurants (Yelp)</td><td>PMF</td><td>0.005</td><td>0.01</td><td>0.01</td><td>NA</td><td>NA</td><td>300</td></tr><tr><td>SocialMF</td><td>0.0013</td><td>0.01</td><td>0.01</td><td>1</td><td>NA</td><td>300</td></tr><tr><td>SocReg</td><td>0.0013</td><td>0.01</td><td>0.01</td><td>0.000001</td><td>NA</td><td>300</td></tr><tr><td>LBSMF</td><td>0.0016</td><td>0.01</td><td>0.01</td><td>0.5</td><td>5</td><td>300</td></tr><tr><td>CREPE MF</td><td>0.0018</td><td>0.01</td><td>0.01</td><td>20</td><td>4</td><td>300</td></tr><tr><td>gCREPE MF</td><td>0.0018</td><td>0.01</td><td>0.01</td><td>20</td><td>4</td><td>300</td></tr><tr><td rowspan="6">Phoenix — Other Businesses (Yelp)</td><td>PMF</td><td>0.011</td><td>0.01</td><td>0.01</td><td>NA</td><td>NA</td><td>300</td></tr><tr><td>SocialMF</td><td>0.0014</td><td>0.01</td><td>0.01</td><td>15</td><td>NA</td><td>300</td></tr><tr><td>SocReg</td><td>0.0009</td><td>0.01</td><td>0.01</td><td>0.000001</td><td>NA</td><td>300</td></tr><tr><td>LBSMF</td><td>0.001</td><td>0.01</td><td>0.01</td><td>0.001</td><td>0.00001</td><td>300</td></tr><tr><td>CREPE MF</td><td>0.0016</td><td>0.01</td><td>0.01</td><td>10</td><td>0.00001</td><td>300</td></tr><tr><td>gCREPE MF</td><td>0.0016</td><td>0.01</td><td>0.01</td><td>10</td><td>0.00001</td><td>300</td></tr><tr><td rowspan="6">Chicago — All Businesses (Gowalla)</td><td>PMF</td><td>0.0023</td><td>0.01</td><td>0.01</td><td>NA</td><td>NA</td><td>300</td></tr><tr><td>SocialMF</td><td>0.0019</td><td>0.01</td><td>0.01</td><td>1</td><td>NA</td><td>300</td></tr><tr><td>SocReg</td><td>0.001</td><td>0.01</td><td>0.01</td><td>0.00001</td><td>NA</td><td>500</td></tr><tr><td>LBSMF</td><td>0.0022</td><td>0.01</td><td>0.01</td><td>6.4</td><td>20</td><td>300</td></tr><tr><td>CREPE MF</td><td>0.0018</td><td>0.01</td><td>0.01</td><td>22</td><td>22</td><td>300</td></tr><tr><td>gCREPE MF</td><td>0.0018</td><td>0.01</td><td>0.01</td><td>22</td><td>22</td><td>300</td></tr></table>

## 5.2. Experimental detail

## 5.2.1. Experimental setup

Herein, we discuss about the experiments conducted to evaluate the performance of our algorithm “CREPE MF ”. All the algorithms are implemented in Java 1.8 and the experiments are run on a Windows system with 3.4 GHz Intel i3 processor and 4 GB RAM. One of the main focus of this paper is to measure the scalability of the proposed algorithms. Obviously a low end computer system will better justify the eficacy of the proposed algorithms and thus, purposely chosen a low configured computer system. The four data sets chosen are diverse in terms of venue category as well as geography. This is to ensure that the findings are not data set dependent. The parameters are tuned as follows: the values of $\gamma _ { U }$ and $\gamma _ { V }$ are fixed as 0.01 for all the experiments conducted in this study. The other parameters are tuned and based on lowest RMSE the corresponding parameters were chosen. The order of tuning is α, $k _ { U } , k _ { V } ,$ and the number of iterations. The parameters are optimized for each algorithm and reported in Table 2.

## 5.2.2. Evaluation metrics

While eficacy of a recommender system is in general evaluated using accuracy, scalability, diversity, cold-start issue, data sparsity, etc., the recent survey paper by Bao et al. [18] demonstrated that accuracy and scalability are two critical measures and becomes particularly very significant in case of location based recommendations due to faster growth of location based social network. Thus, in this context we have considered accuracy and the scalability as the metrics to validate the performance of the recommender systems.

5.2.2.1. Accuracy. Two popular metrics are used for evaluating the accuracy of the algorithms, namely, Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) defined as:

$$
R M S E = \sqrt {\frac {1}{| T |} \sum_ {R _ {u , i} \in T} (R _ {u , i} - \hat {R} _ {u , i}) ^ {2}}\tag{41}
$$

$$
M A E = \frac {1}{| T |} \sum_ {R _ {u, i} \in T} | (R _ {u, i} - \hat {R} _ {u, i}) |\tag{42}
$$

|T| is the number of observations in the test data set T. $R _ { u , i }$ and $\hat { R } _ { u , i }$ are the actual and the predicted ratings issued by user u for item i, respectively. Lower RMSE and MAE values imply better accuracy.

5.2.2.2. Scalability. Scalability of a model is generally assessed [11, 17] using average runtime where runtime refers to time taken to train a model. Obviously, a scalable model is expected to have lower runtime.

## 5.2.3. Experimental findings

5.2.3.1. Benchmark models. The proposed models CREPE MF and gCREPE MF are systematically evaluated with following state-of-theart algorithms to validate its eficacy in terms of prediction accuracy and runtime.

1. Probabilistic Matrix Factorization (PMF) [14]: This algorithm predicts the missing ratings by approximating the user-item rating matrix as a product of two matrices of lower dimensions.

2. Social Matrix Factorization (SocialMF) [21]: This algorithm propagates trust by exploiting users' social network in the Probabilistic Matrix Factorization framework.

3. Social Regularization (SocReg) [22]: This algorithm quantifies the similarity among users and their friends and accordingly incorporates a weighted social network trust propagation.

4. Location-based Social Matrix Factorization (LBSMF) [25]: This algorithm extends SocReg algorithm by incorporating an item-item similarity network in addition to social influence in the recommender system.

The dimension of latent space (l) is set to two standard values, 5 and 10 for all the experiments as in SocialMF [21], SoReg [22], and LBSMF [25]. Increasing the dimension of latent space to more than 10 increases the complexity of the model which is not desirable. The data sets have been randomly divided into 80% as training set and 20% as test set. The experiments are also repeated with 90% as training set and 10% as test set. The random partition was carried out five times independently and the average results are reported, thus, ensuring the robustness of our findings. The summary of the results is provided in Table 3.

Accuracy comparison with benchmark models. Table 3

<table><tr><td rowspan="2">Data set</td><td rowspan="2">Training</td><td rowspan="2">Metric</td><td colspan="7">l=5</td><td colspan="7">l=10</td></tr><tr><td>PMF</td><td>SocialMF</td><td>SocReg</td><td>LBSMF</td><td>CREPE MF</td><td>gCREPE MF (k=5)</td><td>gCREPE MF (k=10)</td><td>PMF</td><td>SocialMF</td><td>SocReg</td><td>LBSMF</td><td>CREPE MF</td><td>gCREPE MF (k=5)</td><td>gCREPE MF (k=10)</td></tr><tr><td rowspan="8">Phoenix — Restaurants (Yelp)</td><td rowspan="4">80%</td><td>RMSE</td><td>1.423</td><td>1.173</td><td>1.178</td><td>1.168</td><td>1.017</td><td>1.016</td><td>1.016</td><td>1.364</td><td>1.172</td><td>1.177</td><td>1.167</td><td>1.017</td><td>1.016</td><td>1.016</td></tr><tr><td>Improve</td><td>28.54%</td><td>13.31%</td><td>13.68%</td><td>12.97%</td><td></td><td></td><td></td><td>25.44%</td><td>13.23%</td><td>13.59%</td><td>12.85%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.952</td><td>0.932</td><td>0.941</td><td>0.928</td><td>0.804</td><td>0.804</td><td>0.804</td><td>0.982</td><td>0.934</td><td>0.941</td><td>0.927</td><td>0.804</td><td>0.804</td><td>0.804</td></tr><tr><td>Improve</td><td>15.55%</td><td>13.73%</td><td>14.56%</td><td>13.34%</td><td></td><td></td><td></td><td>18.13%</td><td>13.92%</td><td>14.56%</td><td>13.31%</td><td></td><td></td><td></td></tr><tr><td rowspan="4">90%</td><td>RMSE</td><td>1.312</td><td>1.176</td><td>1.181</td><td>1.170</td><td>1.019</td><td>1.018</td><td>1.018</td><td>1.291</td><td>1.176</td><td>1.182</td><td>1.168</td><td>1.019</td><td>1.018</td><td>1.018</td></tr><tr><td>Improve</td><td>22.34%</td><td>13.36%</td><td>13.73%</td><td>12.94%</td><td></td><td></td><td></td><td>21.07%</td><td>13.35%</td><td>13.79%</td><td>12.76%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.955</td><td>0.929</td><td>0.938</td><td>0.924</td><td>0.806</td><td>0.806</td><td>0.806</td><td>0.950</td><td>0.933</td><td>0.942</td><td>0.925</td><td>0.806</td><td>0.806</td><td>0.806</td></tr><tr><td>Improve</td><td>15.59%</td><td>13.23%</td><td>14.06%</td><td>12.78%</td><td></td><td></td><td></td><td>15.13%</td><td>13.59%</td><td>14.41%</td><td>12.85%</td><td></td><td></td><td></td></tr><tr><td rowspan="8">Toronto — Restaurants (Yelp)</td><td rowspan="4">80%</td><td>RMSE</td><td>1.186</td><td>1.086</td><td>1.090</td><td>1.073</td><td>0.991</td><td>0.991</td><td>0.991</td><td>1.189</td><td>1.092</td><td>1.099</td><td>1.077</td><td>0.990</td><td>0.990</td><td>0.990</td></tr><tr><td>Improve</td><td>16.46%</td><td>8.77%</td><td>9.10%</td><td>7.66%</td><td></td><td></td><td></td><td>16.74%</td><td>9.34%</td><td>9.92%</td><td>8.08%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.901</td><td>0.883</td><td>0.885</td><td>0.868</td><td>0.787</td><td>0.787</td><td>0.787</td><td>0.906</td><td>0.887</td><td>0.891</td><td>0.871</td><td>0.787</td><td>0.787</td><td>0.787</td></tr><tr><td>Improve</td><td>12.61%</td><td>10.83%</td><td>11.03%</td><td>9.29%</td><td></td><td></td><td></td><td>13.13%</td><td>11.27%</td><td>11.67%</td><td>9.64%</td><td></td><td></td><td></td></tr><tr><td rowspan="4">90%</td><td>RMSE</td><td>1.147</td><td>1.074</td><td>1.079</td><td>1.060</td><td>0.988</td><td>0.989</td><td>0.989</td><td>1.166</td><td>1.082</td><td>1.091</td><td>1.067</td><td>0.988</td><td>0.988</td><td>0.988</td></tr><tr><td>Improve</td><td>13.86%</td><td>8.01%</td><td>8.43%</td><td>6.79%</td><td></td><td></td><td></td><td>15.27%</td><td>8.69%</td><td>9.44%</td><td>7.40%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.879</td><td>0.866</td><td>0.869</td><td>0.852</td><td>0.784</td><td>0.784</td><td>0.784</td><td>0.895</td><td>0.872</td><td>0.878</td><td>0.857</td><td>0.784</td><td>0.783</td><td>0.783</td></tr><tr><td>Improve</td><td>10.81%</td><td>9.47%</td><td>9.78%</td><td>7.98%</td><td></td><td></td><td></td><td>12.40%</td><td>10.09%</td><td>10.71%</td><td>8.52%</td><td></td><td></td><td></td></tr><tr><td rowspan="8">Phoenix — Other Businesses (Yelp)</td><td rowspan="4">80%</td><td>RMSE</td><td>1.418</td><td>1.287</td><td>1.294</td><td>1.294</td><td>1.062</td><td>1.062</td><td>1.062</td><td>1.417</td><td>1.282</td><td>1.293</td><td>1.291</td><td>1.062</td><td>1.062</td><td>1.062</td></tr><tr><td>Improve</td><td>25.11%</td><td>17.48%</td><td>17.93%</td><td>17.93%</td><td></td><td></td><td></td><td>25.05%</td><td>17.16%</td><td>17.87%</td><td>17.74%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.984</td><td>1.032</td><td>1.040</td><td>1.040</td><td>0.821</td><td>0.821</td><td>0.821</td><td>0.991</td><td>1.025</td><td>1.036</td><td>1.034</td><td>0.821</td><td>0.821</td><td>0.821</td></tr><tr><td>Improve</td><td>16.57%</td><td>20.45%</td><td>21.06%</td><td>21.06%</td><td></td><td></td><td></td><td>17.15%</td><td>19.90%</td><td>20.75%</td><td>20.60%</td><td></td><td></td><td></td></tr><tr><td rowspan="4">90%</td><td>RMSE</td><td>1.405</td><td>1.278</td><td>1.292</td><td>1.292</td><td>1.063</td><td>1.063</td><td>1.063</td><td>1.408</td><td>1.272</td><td>1.289</td><td>1.288</td><td>1.063</td><td>1.063</td><td>1.063</td></tr><tr><td>Improve</td><td>24.34%</td><td>16.82%</td><td>17.72%</td><td>17.72%</td><td></td><td></td><td></td><td>24.50%</td><td>16.43%</td><td>17.53%</td><td>17.47%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.981</td><td>1.024</td><td>1.037</td><td>1.037</td><td>0.822</td><td>0.822</td><td>0.822</td><td>0.989</td><td>1.015</td><td>1.032</td><td>1.03</td><td>0.821</td><td>0.821</td><td>0.821</td></tr><tr><td>Improve</td><td>16.21%</td><td>19.73%</td><td>20.73%</td><td>20.73%</td><td></td><td></td><td></td><td>16.99%</td><td>19.11%</td><td>20.45%</td><td>20.29%</td><td></td><td></td><td></td></tr><tr><td rowspan="8">Chicago — All Businesses (Gowalla)</td><td rowspan="4">80%</td><td>RMSE</td><td>1.089</td><td>0.831</td><td>0.831</td><td>0.823</td><td>0.770</td><td>0.758</td><td>0.758</td><td>1.086</td><td>0.827</td><td>0.829</td><td>0.820</td><td>0.768</td><td>0.758</td><td>0.757</td></tr><tr><td>Improve</td><td>29.33%</td><td>7.39%</td><td>7.39%</td><td>6.50%</td><td></td><td></td><td></td><td>29.27%</td><td>7.15%</td><td>7.36%</td><td>6.42%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.650</td><td>0.528</td><td>0.526</td><td>0.523</td><td>0.428</td><td>0.425</td><td>0.425</td><td>0.655</td><td>0.527</td><td>0.526</td><td>0.523</td><td>0.427</td><td>0.425</td><td>0.425</td></tr><tr><td>Improve</td><td>34.18%</td><td>18.98%</td><td>18.68%</td><td>18.22%</td><td></td><td></td><td></td><td>34.77%</td><td>18.95%</td><td>18.84%</td><td>18.29%</td><td></td><td></td><td></td></tr><tr><td rowspan="4">90%</td><td>RMSE</td><td>1.056</td><td>0.833</td><td>0.834</td><td>0.823</td><td>0.778</td><td>0.762</td><td>0.762</td><td>1.057</td><td>0.830</td><td>0.832</td><td>0.820</td><td>0.775</td><td>0.761</td><td>0.761</td></tr><tr><td>Improve</td><td>26.29%</td><td>6.54%</td><td>6.63%</td><td>5.40%</td><td></td><td></td><td></td><td>26.70%</td><td>6.67%</td><td>6.84%</td><td>5.49%</td><td></td><td></td><td></td></tr><tr><td>MAE</td><td>0.627</td><td>0.530</td><td>0.529</td><td>0.525</td><td>0.431</td><td>0.426</td><td>0.426</td><td>0.634</td><td>0.530</td><td>0.529</td><td>0.524</td><td>0.429</td><td>0.426</td><td>0.426</td></tr><tr><td>Improve</td><td>31.27%</td><td>18.80%</td><td>18.57%</td><td>17.91%</td><td></td><td></td><td></td><td>32.31%</td><td>19.12%</td><td>18.97%</td><td>18.15%</td><td></td><td></td><td></td></tr></table>

Table 4 Runtime comparison (in sec).

<table><tr><td></td><td>Phoenix — Restaurants (Yelp)</td><td>Toronto — Restaurants (Yelp)</td><td>Phoenix — Other Businesses (Yelp)</td><td>Chicago — All Businesses (Gowalla)</td></tr><tr><td>PMF</td><td>8.20</td><td>9.40</td><td>8.00</td><td>9.00</td></tr><tr><td>SocialMF</td><td>753.20</td><td>252.60</td><td>630.00</td><td>53.00</td></tr><tr><td>SocReg</td><td>933.20</td><td>433.60</td><td>2011.20</td><td>266.80</td></tr><tr><td>LBSMF</td><td>1984.20</td><td>7007.80</td><td>7318.75</td><td>13,051.80</td></tr><tr><td>CREPE MF</td><td>1752.60</td><td>4933.40</td><td>3649.80</td><td>3362.80</td></tr><tr><td>gCREPE MF (k = 5)</td><td>1436.00</td><td>2755.00</td><td>2340.20</td><td>556.80</td></tr><tr><td>gCREPE MF (k = 10)</td><td>1509.60</td><td>2958.40</td><td>2475.60</td><td>739.40</td></tr></table>

## 5.2.3.2. Evaluation of accuracy

Accuracy evaluation of CREPE MF. From Table 3, it is evident that PMF has the highest RMSE, which is because it assumes the users and items are i.i.d. (independent and identically distributed). Since SocialMF and SocReg incorporate the efect of social network trust propagation, they have lower RMSE and MAE compared to PMF. The accuracy is further improved in LBSMF model as it additionally incorporates the efect of inter-item influence. Notably, CREPE MF outperforms all other baseline algorithms (see Table 3). For latent space dimension of 5 and 80%–20 % division of the data set, CREPE MF achieves 28.54%, 16.46%, 25.11%, and 29.33% RMSE improvement compared to PMF and 12.97%, 7.66%, 17.93%, and 6.50% RMSE improvement compared to LBSMF for Phoenix — Restaurants(Yelp), Toronto — Restaurants(Yelp), Phoenix — Other Businesses (Yelp), and Chicago — All Businesses (Gowalla), respectively. Similar results have been observed for all other experimental settings. Further improvement in accuracy can be expected through cluster-specific hyper-parameter tuning. The statistical significance of performance of CREPE MF is tested by conducting t-test for diferent dimensions of latent space (k = 5 and k = 10) and training-test split sets (80%–20 % and 90%–10 %). The results suggest that CREPE MF outperforms all other benchmark models at 1% significance level (p = 0.01).

Accuracy evaluation of gCREPE MF. From Table 1, it can be seen that majority of the users tend to visit nearby locations. On an average, around 75%–95 % of visits made by users fall within 15 km radius in all the data sets. Therefore, radius r is fixed as 15 km for locating k nearest neighbors. Also, we have considered two settings for gCREPE MF, namely gCREPE MF (k = 5 nearest neighbors) and gCREPE MF (k = 10 nearest neighbors) (Table 3). While for three data sets, the accuracy of gCREPE MF is almost the same compared to CREPE MF, in Gowalla data set the accuracy of gCREPE MF is much higher compared to CREPE MF for both 5 and 10 nearest neighbors (k). This is because in CREPE MF few item clusters had very sparse item-similarity network. However, gCREPE MF ensures all the items have similar items if they have neighbors in the vicinity.

5.2.3.3. Evaluation of runtime. A careful investigation of the runtime observations reveals that PMF has the lowest runtime, followed by SocialMF, SocReg, gCREPE MF, CREPE MF, and LBSMF (Table 4). This order is in agreement with the increasing level of model complexity and it is maximum in case of LBSMF, CREPE MF, and gCREPE MF where both social and item similarity networks are included.

Runtime evaluation of CREPE MF. From Table 4, it can be seen that CREPE MF in general achieves higher reduction in runtime compared to LBSMF and the efect is maximum (up to 74.23%) for Chicago — All Businesses (Gowalla) data set. This reduction in runtime is mainly attributed to the efect of clustering the users and items into homogeneous groups (same rating behavior) and is expected to increase with the increasing size of user-preference and itemsimilarity networks. In a scenario where the sizes of both userpreference and item-similarity network are less (as in Phoenix — Restaurants (Yelp)) then the runtime for LBSMF will be less (c.f. Table 4) and subsequently the reduction in runtime for CREPE MF, where clustering is employed, will be less. Smaller size of itemsimilarity network in Phoenix-Restaurants (Yelp) compared to Chicago (c.f. Table 1) results in lesser runtime for LBSMF and hence the reduction in runtime for CREPE MF is also less (11.67%). On the other hand, the item-similarity network for Chicago is huge compared to other data sets and also the runtime for LBSMF is higher and hence the reduction in runtime (74.23%) is drastic. While clustering in general has very positive impact on runtime, one must also note that the number of the clusters as well as the size of the individual cluster, which is a very specific and inherent characteristic of a data set, will also have critical influence in determining the runtime and results may vary when a diferent data set is experimented. It is worth noting that these results were obtained by running the CREPE MF clusters in series. However, a considerable reduction in runtime can be achieved by executing the clusters in parallel. For example, the runtime for the biggest cluster in Phoenix — Restaurants (Yelp) data set (among 20 clusters) is 271.2 s which is much lower than SocialMF, SocReg, and LBSMF (with 63.99%, 70.94% and 86.33% improvement, respectively).

Runtime evaluation of gCREPE MF. Herein, we compare the runtime of gCREPE MF (for both 5 and 10 nearest neighbors) with all other models. As seen from Table 4, the runtime of gCREPE MF is much lower compared to CREPE MF for all the data sets. For 10 nearest neighbors (k), there is a reduction in runtime by 78.01% and for 5 nearest neighbors, there is 83.44% reduction in runtime for Chicago — All Businesses (Gowalla) data set. Also, for other three data sets there is a significant reduction in runtime for gCREPE MF model compared to other models. The diferences in reduction in runtime among these four data sets can be rationalized by the nearly uniform size of reconstructed location-enhanced item-similarity network in gCREPE MF model. From Table 1, it is apparent that 79.09% of total items are present in itemsimilarity network for Chicago data set; however, the item-network size is still significantly large in comparison to other data sets, indicating the presence of large neighborhood for many items. The newly constructed location-enhanced item-similarity network in gCREPE MF ensures almost all the items have at least one similar item (if they fall within the geographic vicinity) and only top k similar items are considered for each item thereby reducing the size of the network drastically. We should note that although Phoenix — Other Businesses (Yelp) data set has huge item-similarity network the reduction is not comparable to Chicago data set as the user-preference network is very large. Overall, in scenario where size of item-similarity network is huge and size of user-preference network is moderate, then a good reduction in runtime can be expected as gCREPE MF utilizes only top k similar neighbor for each item. Thus, comparing Tables 3 and 4, we can conclude that we are able to preserve the accuracy of the recommendations by significantly reducing the runtime. Also, one should note that the runtime mentioned here is time taken to train the model which does not include the item similarity computation. For CREPE MF $\frac { N ^ { c } \cdot ( N ^ { c } - 1 ) } { 2 }$ pairs of item similarities are calculated, where $N ^ { c }$ is the number of items within an item cluster c. On the contrary, gCREPE MF looks for n<sup>c</sup> items within its item cluster and geographical vicinity and computes $\frac { n ^ { c } \cdot ( n ^ { c } - 1 ) } { - }$ 2 (where N<sup>c</sup>≫ n<sup>c</sup>) similarities. Hence, the overall runtime is expected to be much lower than as shown in Table 4.

<table><tr><td>Training</td><td>Metric</td><td></td><td>Phoenix — Restaurants (Yelp)</td><td>Toronto — Restaurants (Yelp)</td><td>Phoenix — Other Businesses (Yelp)</td><td>Chicago — All Businesses (Gowalla)</td></tr><tr><td rowspan="10">80%</td><td rowspan="5">RMSE</td><td>LBSMF</td><td>1.168</td><td>1.073</td><td>1.294</td><td>0.823</td></tr><tr><td>UPMF</td><td>1.138</td><td>1.061</td><td>1.280</td><td>0.827</td></tr><tr><td>% Improved over LBSMF</td><td>2.60%</td><td>1.15%</td><td>1.12%</td><td>- 0.49%</td></tr><tr><td>CREPE MF</td><td>1.017</td><td>0.991</td><td>1.062</td><td>0.770</td></tr><tr><td>% Improved over LBSMF</td><td>12.97%</td><td>7.66%</td><td>17.93%</td><td>6.50%</td></tr><tr><td rowspan="5">MAE</td><td>LBSMF</td><td>0.928</td><td>0.868</td><td>1.040</td><td>0.523</td></tr><tr><td>UPMF</td><td>0.892</td><td>0.855</td><td>1.025</td><td>0.523</td></tr><tr><td>% Improved over LBSMF</td><td>3.83%</td><td>1.51%</td><td>1.44%</td><td>0.00%</td></tr><tr><td>CREPE MF</td><td>0.804</td><td>0.787</td><td>0.821</td><td>0.428</td></tr><tr><td>% Improved over LBSMF</td><td>13.34%</td><td>9.29%</td><td>21.06%</td><td>18.22%</td></tr><tr><td rowspan="10">90%</td><td rowspan="5">RMSE</td><td>LBSMF</td><td>1.170</td><td>1.060</td><td>1.292</td><td>0.823</td></tr><tr><td>UPMF</td><td>1.137</td><td>1.046</td><td>1.269</td><td>0.830</td></tr><tr><td>% Improved over LBSMF</td><td>2.88%</td><td>1.31%</td><td>1.78%</td><td>- 0.85%</td></tr><tr><td>CREPE MF</td><td>1.019</td><td>0.986</td><td>1.063</td><td>0.778</td></tr><tr><td>% Improved over LBSMF</td><td>12.94%</td><td>6.98%</td><td>17.72%</td><td>5.40%</td></tr><tr><td rowspan="5">MAE</td><td>LBSMF</td><td>0.924</td><td>0.852</td><td>1.037</td><td>0.525</td></tr><tr><td>UPMF</td><td>0.891</td><td>0.838</td><td>1.014</td><td>0.526</td></tr><tr><td>% Improved over LBSMF</td><td>3.59%</td><td>1.69%</td><td>2.22%</td><td>- 0.19%</td></tr><tr><td>CREPE MF</td><td>0.806</td><td>0.781</td><td>0.822</td><td>0.431</td></tr><tr><td>% Improved over LBSMF</td><td>12.78%</td><td>8.33%</td><td>20.73%</td><td>17.91%</td></tr></table>

User preference similarity impact (
l =5). Table 5

## 6. Discussion

Improvement in accuracy and runtime in CREPE MF can be attributed to two important features: a) creation of user preference network — for propagating social trust, b) clustering the users and items based on rating pattern — for capturing social bias. On the other hand, performance of gCREPE MF is further dependent on the radius considered for geo-spatial clustering. We discuss the independent impact of each of these factors on CREPE MF and gCREPE MF performances.

## 6.1. Impact of user preference networks on CREPE MF

The impact of User Preference Network on recommendation accuracy is validated by incorporating the preference enhanced social network and item-similarity network in the PMF model which we term it as ‘UPMF’. The parameters used for CREPE MF are used in this case and the accuracy is compared with LBSMF which considers the entire social network without preference similarity along with the item-similarity network. Table 5 demonstrates the superiority of UPMF compared to LBSMF (with up to 2.88% improvement in accuracy) for all experi mental settings for Yelp data set. This highlights the importance of preference enhanced social networks as posited in earlier section. However, the performance of UPMF in Gowalla data set has not improved compared to LBSMF. This outcome can be realized from by inspecting the preference network and item-similarity network. It can be observed from Table 1 that the number of connections in friends network and preference network is less, however item-similarity network is huge. Hence, efect of preference network is minimal and RMSE values are comparable for all the models.

## 6.2. Impact of clustering on CREPE MF

From Table $^ { 5 , }$ we can infer that UPMF has up to 2.88% improvement in accuracy compared to LBSMF and a significant improvement in accuracy (up to 17.93%) was observed for CREPE MF for all the experimental settings (Table 5). This accuracy improvement is attributed to clustering users and businesses into homogeneous rating clusters. Further, CREPE MF achieves up to 74.23% lower runtime compared to LBSMF (Table 4). As the network densities are comparable for both LBSMF and CREPE MF. this reduction in runtime has been realized due to user and business clustering.

## 6.2.1. Impact of number of user clusters and item clusters

The eficiency of a RS can be greatly afected by number of user clusters and item clusters. A very few clusters may not improve accuracy or runtime, whereas too many clusters may decrease the number of connections in preference network and item-similarity network in each cluster. Ensuring clusters with adequate number of users, items, and connections in similarity networks is therefore essential to attain optimal accuracy and runtime. We varied the number of user clusters and item clusters and recorded accuracy (RMSE) and runtime (seconds). Initially, users are clustered into $n _ { u }$ user clusters. For those user clusters whose number of interactions per user is comparable or greater than the global average number of interactions per user, we proceeded for second stage item-clustering $( n _ { i }$ item clusters) ensuring the cluster density is high enough. Fig. 6 depicts the performance of CREPE MF, for Phoenix — Restaurants (Yelp), in terms of accuracy and runtime for diferent values of $n _ { u }$ and $n _ { i } .$ After analyzing Fig. $^ { 6 , }$ we fixed $n _ { u }$ as 10 and n as 3, as they gave considerable reduction in runtime without much loss of accuracy. The same procedure has been repeated for the other three sets of data, and the results indicate similar trends.

![](/api/attachments/66R5P5S3/fulltext/images/806c1375a7297970ce085504cf54e5622488240c2e256960ec19721a8590bb15.jpg)

![](/api/attachments/66R5P5S3/fulltext/images/7f0aec9ab7e54e63a4d86fa52c46de74808ea1a12892f7af63bb70e20171dd3a.jpg)  
Fig. 6. Performance comparison with number of clusters: Phoenix — Restaurants (Yelp).

## 6.3. Impact of distance on gCREPE MF

We measure the impact of geographical neighborhood influence (distance) on recommendation accuracy. To study this, we varied the geographical distance (radius, r) and re-constructed the inter-item similarity network. Phoenix — Restaurants (Yelp) and Toronto — Restaurants (Yelp) data sets show similar trends for nearest neighbors $k = 5 ;$ the prediction accuracy improves if r is reduced. However, when k is increased to 10, the prediction accuracy decreases with reduced value of r. This could be attributed to reducing r: locating k nearest neighbors can be dificult as k becomes large. It is easy to note that, however, the optimal value of k for the two data sets is diferent. For Phoenix — Other Businesses (Yelp), there is no diference in accuracy when r is altered. This may be as the business categories for this data set comprises of diferent domain like Health & Medical, Education, etc. which may require traveling to a far place to locate a specialized business and henceforth distance has the least impact on prediction accuracy. For Chicago — All Businesses (Gowalla), the RMSE is the least for 15 km distance for both 5 and 10 nearest neighbors. Hence, there is a trade-of between neighborhood distance r and number of nearest neighbors k. Therefore, we need to carefully choose the distance r such that we have substantial k nearest neighbors for the items (Fig. 7).

## 7. Conclusion and future work

In the era of Web 2.0, while users are confronted with abundance of online information, a recommender system does the formidable task by filtering content pertinent to user's query in the form of personalized recommendation. In this context, eficacy of the system is primarily governed by accuracy and scalability metrics. To handle the datasparsity issue and inherently improve accuracy, social recommender systems have been proven fruitful with the advent of online social network where only the direct connections are considered. In this paper, drawing inspiration from social science theories, we posited that direct and mutual connections in the social network with high preference similarity should be included in the model-based recommender systems along with ratings. Further, we envision that clustering on useritem rating space can be applied using the theory of Social Bias to improve the scalability. A systematic evaluation has been carried out on two large real data sets collected from Yelp and Gowalla. Our analysis reveals that inclusion of mutual connections as well as clustering using Rating Bubbles are beneficial and our proposed approaches, CREPE MF and gCREPE MF both outperform the state-of-the-art baseline techni ques in terms of accuracy and runtime. In this section, we build on the results to discuss the implications of application of social science theories on recommender system and anticipate the applicability in practical scenario.

## 7.1. Implications for research

In this study, we introduced the concept of ‘Preference Network’ and emphasized the impact of ‘Rating Bubbles' to the emerging area of Trust-based recommender systems. A key implication that unfolds from the findings of this study is that all connections are not equally important and hence preference similarity must be considered to propagate trust in social recommender system. Although prior literature has mostly focused only on the direct connections (friends) in social network to propagate trust, findings of this study experimentally validate the impact of using two-hop connections in model-based social recommender system. This notion has been applied in the construction of the ‘Preference Network’ inspired by Theory of Social Trust; using the concept of Triadic Closure, we expand the friends network to include second hop mutual connections and using Theory of Homophily, we retain only similar connections. Further, investigation reveals that rating bubbles are present in real online rating patterns due to social influence bias [19, 20] and can be utilized to cluster users in homogeneous groups. This is the key to improve the accuracy as well as the scalability of the system.

![](/api/attachments/66R5P5S3/fulltext/images/b6b86096e8a736278fa921a76e3661e2cf754bf49084031358a1a7a21eef676e.jpg)  
Fig. 7. Impact of distance on accuracy.

## 7.2. Implication for practice

To increase the adaptability of any recommender system it is important to reduce the response time and improve the accuracy. Moreover, in real life users trust suggestions from their friends. In re cent times social recommender system which has gained popularity can be utilized to provide trust-worthy personalized recommendations. By incorporating these three important aspects the proposed approach, CREPE MF, builds a trust-based social recommender system with 6.50% to 17.93% improvement in accuracy (RMSE) and 11.67% to 74.23% reduction in runtime, depending on the underlying data sets. A further reduction in runtime of 18.06% to 83.44% has been achieved by modified approach gCREPE MF by incorporating geographical-filtering which can be used in real-time venue recommendations. Considering the scale of real user-base and item-base, this improvement is remarkable indicating its applicability in firms like Yelp, Gowalla, Foursquare, etc. with social networking option.

## 7.3. Limitations and future work

In this study, we considered the social network connections of the users, however, few online e-commerce websites provide networking option on the platform itself. So gathering the social network information for such users otherwise is limited. However, for such cases instead of considering the friend's network, interaction based network can be formulated from the review/rating itself. Also, in this work, we have presented the experimental findings of clusters run in series. This can be further implemented with a distributed algorithm to improve the computational complexity. For performance evaluation, two key metrics, namely accuracy and scalability, have been chosen. It will be interesting to evaluate against other metrics like data-sparsity, diversity, cold-start users/items, etc. which are not considered in this study. In this study, we have compared the performance of the recommender system using two data sets having diferent rating distribution with one (Gowalla) being left-skewed which can reduce the validity of the results. However, the experimental findings indicate that the suggested approaches work better even for these left-skewed data sets. A detailed investigation on understanding the diference in performance of the recommender system with two data sets having different distribution is left open to the research community. Finally, we have not considered the review text which can better predict the user preference for diferent attributes of the businesses and their associated sentiments, which is currently undergoing.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## References

[1] R.I. Dunbar. Do online social media cut through the constraints that limit the size of ofline social networks? Open Science 3 (1) (2016) 150292.

[2] L. Duan, W.N. Street. E. Xu, Healthcare information systems: data mining methods in the creation of a clinical recommender system. Enterprise Information Systems 5 (2) (2011) 169–181,

[3] Y.-C. Zhang, M. Blattner, Y.-K. Yu, Heat conduction process on community networks as a recommendation model, Physical Review Letters 99 (15) (2007) 154301

[4] G. Linden, B. Smith. J. York, Amazon,com recommendations: item-to-item collaborative filtering, IEEE Internet Computing 7 (1) (2003) 76–80.

[5] G. Lekakos, P. Caravelas, A hybrid approach for movie recommendation, Multimedia Tools and Applications 36 (1-2) (2008) 55–70.

[6] E.-y. Kang, H. Kim, J. Cho, Personalization method for tourist point of interest (POI) recommendation, International Conference on Knowledge-Based and Intelligent Information and Engineering Systems, Springer, 2006, pp. 392–400.

[7] M. Ye. P. Yin. W.-C. Lee, D.-L. Lee, Exploiting geographical influence for collaborative point-of-interest recommendation, Proceedings of the 34th International

ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2011, pp. 325–334.

[8] J. Bobadilla, F. Ortega, A. Hernando, A. Gutiérrez, Recommender systems survey, Knowledge-Based Systems 46 (2013) 109–132.

[9] H.-N. Kim, A. El-Saddik, G.-S. Jo, Collaborative error-reflected models for cold-start recommender systems, Decision Support Systems 51 (3) (2011) 519–531

[10] M.M. Azadjalal, P. Moradi, A. Abdollahpouri, M. Jalili, A trust-aware recommendation method based on Pareto dominance and confidence concepts, Knowledge-Based Systems 116 (2017) 130–143

[11] H. Parvin, P. Moradi, S. Esmaeili, N.N. Qader, A scalable and robust trust-based nonnegative matrix factorization recommender using the alternating direction method, Knowledge-Based Systems 166 (2019) 92–107.

[12] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Analysis of recommendation algorithms for e-commerce, Proceedings of the 2nd ACM Conference on Electronic Commerce, ACM. 2000, pp. 158–167

[13] L. Lü, M. Medo, C.H. Yeung, Y.-C. Zhang, Z.-K. Zhang, T. Zhou, Recommender systems, Physics Reports 519 (1) (2012) 1–49.

[14] A. Mnih, R.R. Salakhutdinov, Probabilistic matrix factorization, Advances in Neural Information Processing Systems, 2008, pp. 1257–1264.

[15] M.C. Pham, Y. Cao, R. Klamma, M. Jarke, A clustering approach for collaborative filtering recommendation using social network analysis, J. UCS 17 (4) (2011) 583–604.

[16] G.-R. Xue, C. Lin, Q. Yang, W. Xi, H.-J. Zeng, Y. Yu, Z. Chen, Scalable collaborative filtering using cluster-based smoothing, Proceedings of the 28th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM. 2005, pp. 114–121.

[17] H. Langseth. T.D. Nielsen. Scalable learning of probabilistic latent models for col laborative filtering, Decision Support Systems 74 (2015) 1–11.

[18] J. Bao, Y. Zheng, D. Wilkie, M. Mokbel, Recommendations in location-based social networks: a survey, GeoInformatica 19 (3) (2015) 525–565.

[19] S. Aral, The problem with online ratings, MIT Sloan Management Review 55 (2) (2014) 47.

[20] L. Muchnik, S. Aral, S.J. Taylor, Social influence bias: a randomized experiment, Science 341 (6146) (2013) 647–651.

[21] M. Jamali, M. Ester, A matrix factorization technique with trust propagation for recommendation in social networks, Proceedings of the Fourth ACM Conference on Recommender Systems, ACM, 2010, pp. 135–142.

[22] H. Ma, D. Zhou, C. Liu, M.R. Lyu, I. King, Recommender systems with social reg ularization. Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, ACM, 2011, pp. 287–296.

[23] M.J. Brzozowski, T. Hogg, G. Szabo, Friends and foes: ideological social networking, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2008, pp. 817–820.

[24] C. Cheng, H. Yang, I. King, M.R. Lyu, Fused Matrix Factorization with Geographical and Social Influence in Location-based Social Networks. AAAI, vol. 12, 2012, pp. 17–23.

[25] D. Yang, D. Zhang, Z. Yu, Z. Wang, A sentiment-enhanced personalized location recommendation system, Proceedings of the 24th ACM Conference on Hypertext and Social Media, ACM, 2013, pp. 119–128.

[26] P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative filtering of netnews. Proceedings of the 1994 ACM Conference on Computer Supported Cooperative Work. ACM. 1994. pp. 175–186

[27] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommendation algorithms. Proceedings of the 10th International Conference on World Wide Web. ACM. 2001, pp. 285–295

[28] N. Mirbakhsh, C.X. Ling, Clustering-based matrix factorization, arXiv preprint, 2013arXiv:1301.6659

[29] L. Hu, A. Sun, Y. Liu, Your neighbors afect your ratings: on geographical neigh borhood influence to rating prediction, Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval. ACM 2014, pp. 345–354.

[30] G. Carullo, A. Castiglione, A. De Santis, F. Palmieri, A triadic closure and homophily-based recommendation system for online social networks. World Wide Web 18 (6) (2015).1579–1601

[31] P. Sztompka, Trust: A Sociological Theory, Cambridge University Press, 1999.

[32] J. Golbeck, Trust and nuanced profile similarity in online social networks, ACM Transactions on the Web (TWFB) 3 (4) (2009) 12

[33] X. Li. M. Wang, T.-P. Liang, A multi-theoretical kernel-based approach to socia network-based recommendation, Decision Support Systems 65 (2014) 95–104.

[34] M. McPherson, L. Smith-Lovin, J.M. Cook, Birds of a feather: homophily in socia networks, Annual Review Of Sociology 27 (1) (2001) 415–444.

[35] C.-N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decision Support Systems 43 (2) (2007) 460–475.

[36] R.R. Sinha, K. Swearingen, Comparing recommendations made by online systems and friends. DELOS Workshop: Personalisation and Recommender Systems in Digital Libraries, vol, 106, 2001

[37] M.S. Granovetter, The strength of weak ties, American Journal of Sociology 78 (6) (1973).1360–1380.

[38] S. Bikhchandani, D. Hirshleifer, I. Welch, A theory of fads, fashion, custom, and cultural change as informational cascades, Journal of Political Economy 100 (5) (1992) 992-1026

[39] A.V. Baneriee. A simple model of herd behavior, The Ouarterly Journal of Economics 107 (3) (1992) 797–817.

[40] Y.-J. Lee, K. Hosanagar, Y. Tan, Do I follow my friends or the crowd? Information cascades in online movie ratings, Management Science 61 (9) (2015) 2241–2258.

[41] W.R. Tobler, A computer movie simulating urban growth in the Detroit region,

Economic Geography 46 (sup1) (1970) 234–240

[42] M.C. Gonzalez, C.A. Hidalgo, A.-L. Barabasi, Understanding individual human mobility patterns, Nature 453 (7196) (2008) 779.

[43] A. Noulas, S. Scellato, C. Mascolo, M. Pontil, An empirical study of geographic user activity patterns in foursquare. ICwSM 11 (70-573) (2011) 2.

[44] J.A. Hartigan, M.A. Wong, Algorithm AS 136: a k-means clustering algorithm, Journal of the Royal Statistical Society. Series C (Applied Statistics) 28 (1) (1979) 100–108.

[45] Y. Si, F. Zhang, W. Liu, An adaptive point-of-interest recommendation method for location-based social networks based on user activity and spatial features, Knowledge-Based Systems 163 (2019) 267–282.

[46] Y. Liu, W. Wei, A. Sun, C. Miao, Exploiting geographical neighborhood characteristics for location recommendation. Proceedings of the 23rd ACM International Conference on Information and Knowledge Management. ACM. 2014, pp. 739–748

[47] F.M.F. Wong, Z. Liu, M. Chiang, F. Ming Fai Wong, Z. Liu, M. Chiang, On the efficiency of social recommender networks, IEEE/ACM Transactions on Networking (TON) 24 (4) (2016) 2512–2524.

![](/api/attachments/66R5P5S3/fulltext/images/b02c60ecf67f06a74c8bd8d3a107994a22edb32532ef92b1ae677a39fc0a595b.jpg)  
Nargis Pervin is an Assistant Professor in Department of Management Studies in Indian Institute of Technology, Madras. She received her Ph.D. from National University of Singapore, Singapore in the area of Information Systems. Her research interests include recommendation systems, social network analytics, econometric modeling, etc. Her papers have appeared in ACM Transactions on Management Information Systems, ACM Mobile Networks and Applications (MONET), ICIS, AMCIS, PACIS, WITS, DESRIST, among others.

![](/api/attachments/66R5P5S3/fulltext/images/df591d9010f1f59dc2f8a686d90d140c2636d643ab76b1ddb6672aba6eb0b02a.jpg)

Divyaa L.R. is a M.S. student in Department of Management Studies in Indian Institute of Technology, Madras. Her research interests include recommendation systems, text mining, and data mining. Her research ha appeared in AMCIS and HCII.
