---
otero_id: 1634
otero_key: "NVXBFQE2"
title: "A trust-semantic fusion-based recommendation approach for e-business applications"
authors: "Qusai Shambour; Jie Lu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A trust-semantic fusion-based recommendation approach for e-business applications

Qusai Shambour, Jie Lu ⁎

Lab of Decision Systems and e-Service Intelligence Centre for Quantum Computation and Intelligent Systems School of Software, Faculty of Engineering and Information Technology University of Technology Sydney, PO Box 123, Broadway, NSW 2007, Australi

## a r t i c l e i n f o

Article history: Received 16 March 2012 Received in revised form 19 June 2012 Accepted 5 September 2012 Available online 14 September 2012

Keywords: Recommender systems Collaborative <sup>fi</sup>ltering Trust <sup>fi</sup>ltering Semantic <sup>fi</sup>ltering Information fusion Cold-start Data sparsity

## a b s t r a c t

Collaborative Filtering (CF) is the most popular recommendation technique but still suffers from data sparsity, user and item cold-start problems, resulting in poor recommendation accuracy and reduced coverage. This study incorporates additional information from the users' social trust network and the items' semantic domain knowledge to alleviate these problems. It proposes an innovative Trust–Semantic Fusion (TSF)-based recommendation approach within the CF framework. Experiments demonstrate that the TSF approach significantly outperforms existing recommendation algorithms in terms of recommendation accuracy and coverage when dealing with the above problems. A business-to-business recommender system case study validates the applicability of the TSF approach.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Recommender systems are considered the most popular forms of web personalization and have become a promising and important research topic in information sciences and decision support systems [9,10,17,19,20,24,46,49]. Recommender systems are used to either predict whether a particular user will like a particular item or to identify a set of k items that will be of interest to a certain user, and have been used in different web-based applications including e-business, e-learning and e-tourism [8,22,31]. Currently, Collaborative Filtering (CF) is probably the most known and commonly used recommendation approach in recommender systems. CF works by collecting user ratings for items in a given domain and computing similarities between users or between items in order to produce recommendations [1,31]. CF can be further divided into user-based and item-based CF approaches. In user-based CF approach, a user will receive recommendations of items that similar users liked. In item-based CF approach, a user will receive recommendations of items that are similar to the ones that the user liked in the past [1]. Despite their popularity and success, the CF-based approaches still suffer from some major limitations; these include data sparsity, cold-start user and cold-start item problems [1,3,36,37]. The data sparsity problem occurs when the number of available items increases and the number of ratings in the rating matrix is insuf<sup>fi</sup>cient for generating accurate predictions. When the ratings obtained are very small compared to the number of ratings that are needed to be predicted, a recommender system becomes unable to locate similar neighbors and produces poor recommendations. The cold-start (CS) user problem, which is also known as the new user problem, affects users who have none, or a small number of ratings. When the number of rated items is small for the CS user, the CF-based approaches cannot properly <sup>fi</sup>nd the user neighbors using rating similarity, so it fails to generate accurate recommendations. The CS item problem, which is also known as the new item problem, affects items that have none, or only a small number of ratings. With few ratings for CS items, CF-based approaches cannot appropriately locate similar neighbors using rating similarity and would be unlikely to recommend them [1,33,36,37].

In view of these limitations, researchers have commonly decided to opt for trust-based [11,16,26,27,44] and semantic-based [2,15,22, 35,45] recommender systems to tackle such limitations. These systems can deal with the trust relations between users and semantic features of items, which cannot be well handled in traditional CF-based recommendation approaches, to support the recommendation process. These systems have proved to be successful in solving some limitations of CF-based approaches by allowing the recommender systems to make inferences based on an additional source of knowledge. We believe that, by considering information extracted from the users' trust network and the items' semantic domain knowledge, a fusion-based recommendation approach that takes into account both trust and semantic information should provide more effective recommendations.

Based on this notion and following our previous work [22,23, 38–41] where we addressed some limitations of CF-based recommendation approaches, this paper proposes a fusion-based recommendation approach that fuses the trust and semantic information of users and items within the CF framework to achieve yet more effective results in terms of recommendation accuracy and coverage, especially when dealing with data sparsity, CS user and CS item problems. The proposed approach, called TSF (Trust Semantic Fusion), fuses two hybrid recommendation approaches; the user-based trust-enhanced CF, and the item-based semantic-enhanced CF. The user-based trust-enhanced CF approach utilizes the intuitive properties of trust and trust propagation to address the data sparsity and CS user problems. The item-based semantic-enhanced CF approach employs the underlying semantic relationships between items to help reduce the effect of data sparsity and CS item problems. We also de<sup>fi</sup>ne and introduce the notion of an item's reputation weight into the item-based semantic-enhanced CF to further improve the quality of predictions. This paper is organized as follows. In Section $^ { 2 , }$ research background and related work are described. Section 3 presents the components of the TSF approach. A case-based mathematical example for illustrating the procedure of the TSF is given in Section 4. Section 5 demonstrates the experimental evaluation and results using MovieLens and Yahoo! Webscope datasets. Section 6 describes a case study to validate the feasibility of applying the TSF approach into real e-business applications. Finally, the contributions of this study are summarized, and future research is presented in Section 7.

## 2. Background and related work

## 2.1. CF-based recommender systems

The CF approach is the most popular recommendation approach in current recommender systems. Typically, CF can be further divided into user-based and item-based CF approaches. The user-based CF approach produces recommendations for interesting items based on evaluations of users who have similar tastes. First, it analyzes the user–item matrix and creates a vector containing the user's ratings for each rated item. Then, it computes the similarity between the target user's vector and the vectors of the remaining users, using similarity measures such as the Pearson correlation and Cosine vector. These similarity measures compute the similarity between two users based only on the overlap items de<sup>fi</sup>ned in their respective vectors. Next, the most similar users (Top-n) to the target user are selected as the user's nearest neighbors. Finally, predictions are generated using a weighted average of the neighbors' ratings of items that are contained in their pro<sup>fi</sup>les [1,37]. The item-based CF approach is the transpose of the user-based one. While the user-based CF approach produces predictions based on users' similarity, item-based CF approach produces predictions based on items' similarity [1,36,37]

## 2.2. Trust-based recommender systems

Trust-based recommender systems utilize a social network augmented with trust ratings, known as a trust network, to generate recommendations for users based on people they trust. A trust network is a directed graph where the nodes are users and the edges are weighted according to the degree of trust assigned by one user to another. By utilizing trust information, trust-based recommender systems allow users to be aware that the sources of recommendation were formed from people who are either directly trusted by the current user, or indirectly trusted by another trusted user through the trust propagation method. Trust propagation is often employed to infer the trust, and establish new relations between users who have no direct trust links between them [11,26]. In practice, trust-based recommender systems that exploit trust information can provide better recommendation effectiveness than conventional CF-based techniques, in particular, by alleviating issues concerning data sparsity or CS user problems [11,16,26,40,47]. Two main trust <sup>fi</sup>ltering methods have been adopted in the current literature: Explicit trust and Implicit trust <sup>fi</sup>ltering approaches.

Explicit trust <sup>fi</sup>ltering approaches obtain trust values from pre-existing social links between users [11,26]. Nevertheless, the use of explicit trust <sup>fi</sup>ltering approaches has exposed two major limitations: (1) they require additional manual labor and user effort from the end user (i.e. time consuming and expensive to get the explicit trust); (2) they suffer from the CS user problem because new users have to <sup>fi</sup>rst build up their web of trust before the <sup>fi</sup>ltering is effective [16,47]. These limitations have limited the applicability of explicit trust <sup>fi</sup>ltering approaches in recommender systems, and makes the implicit trust <sup>fi</sup>ltering approaches more feasible to use [44,47]. Implicit trust <sup>fi</sup>ltering approaches derive trust values between users based on item ratings [16,27,47]. For example, O'Donovan and Smyth [27] acknowledged that user reliability in delivering accurate recommendations in the past is an important factor for in<sup>fl</sup>uencing recommendation and prediction in the future. In particular, the more accurate predictions a given user has produced in the past, the more trustworthy he/she is. Hwang and Chen [16] developed an implicit trust <sup>fi</sup>ltering method where the trust values are directly derived from the user ratings data. Yuan et al. [47] proposed a novel implicit trust aware recommendation model (iTARS) based on the small-worldness of the implicit trust network, in which the implicit trust is generated from the user similarities. To sum up, most of the implicit trust <sup>fi</sup>ltering techniques we have explored share common features: (1) they use ratings or prediction errors between users' pro-<sup>fi</sup>les as an indication of trust; (2) they operate on the intersection of users' pro<sup>fi</sup>les; as a result, they do not consider what has not been rated when computing trust.

## 2.3. Semantic-based recommender systems

Semantic-based recommender systems exploit the underlying semantic properties and attributes associated with users and items to generate recommendations. For instance, semantic information about items consists of the attributes of the items, the relationship between items, and the relationship between items and metainformation [30]. Taxonomies and ontologies as the major source of semantic information can be taken advantage of in recommender systems, since they provide a means of discovering and classifying new information about the items to recommend, about user pro<sup>fi</sup>les and even about their context [35]. For example, product taxonomies and ontologies have been presented in several recommender systems to utilize the relevant semantic information in order to help improve the recommendation quality [2,7,15,22,35]. In summary, most of the presented research provides two primary advantages. First, the semantic attributes for items provide additional explanations about why particular items have been recommended or not. Secondly, the additional source of semantic knowledge provides better recommendation effectiveness than current CF-based techniques, particularly in cases where little or no rating information is available.

## 3. Trust–semantic fusion-based recommendation approach

This section <sup>fi</sup>rst describes the structure and each component of the TSF approach. Then, the TSF's recommendation computation process is demonstrated.

## 3.1. The structure of the TSF recommendation approach

The TSF approach (Fig. 1) obtains as inputs a raw user-item rating matrix $R _ { m * n }$ and item taxonomy, and produces as an output a user– item prediction matrix. $R _ { m * n }$ contains the rating values of m users and n items. The item taxonomy is represented in a tree hierarchy structure with two levels of nodes: the <sup>fi</sup>rst level contains the item categories that items belong to; the second contains the items as leaf nodes.

![](/api/attachments/NVXBFQE2/fulltext/images/f707f4aba70db3fb192febb7becb94e6627843fa469fe2b8db8a8ed3b74664b7.jpg)  
Fig. 1. A TSF recommendation approach structure diagram.

The detailed recommendation process of the TSF approach is described in the following subsections.

## 3.1.1. The user-based trust-enhanced CF module

This module produces user-based trust-enhanced CF recommendations. The module integrates the enhanced user-based CF and the user-based trust <sup>fi</sup>ltering approaches in order to exploit their advantages and to eliminate the known limitations of the current user-based CF approaches.

3.1.1.1. U-Step 1: calculate user-based CF similarity and implicit trust. This process is divided into two steps: <sup>fi</sup>rst, the enhanced userbased CF similarity computation, and second the user-based implicit trust computation.

3.1.1.1.1. U-Step 1.1: enhanced user-based CF similarity computation. This step uses the combination of the user-based Constrained Pearson Correlation (CPC) [42] and the user-based Jaccard similarity [6] measures to calculate the enhanced user-based CF similarity value between any pair of users. The CPC metric, as given by Eq. (1), measures the similarity based on the rating variation between two users' co-rated items only. This is a key drawback since two users can be totally similar if they only share one item with the same rating. In contrast to the user-based CPC similarity measure, the user-based Jaccard metric, as given by Eq. (2), does not have this limitation because it measures the similarity based on the overlap items that the two users have rated in common to the number of items that both users have rated in total. For example, according to the user-based Jaccard metric, two users can be very similar, if they commonly rated 8 items taking into account that each user has rated 10 items in total, regardless of their ratings [6]. Thereby, by combining the user-based CPC with the Jaccard, we can ensure that users who share many items are preferred to others that only share a few items.

$$
U C P C _ {a, b} = \frac {\sum_ {i = 1} ^ {I _ {a , b}} \left(r _ {a , i} - \bar {r} _ {a}\right) \times \left(r _ {b , i} - \bar {r} _ {b}\right)}{\sqrt {\sum_ {i = 1} ^ {I _ {a , b}} \left(r _ {a , i} - \bar {r} _ {a}\right) ^ {2}} \times \sqrt {\sum_ {i = 1} ^ {I _ {a , b}} \left(r _ {b , i} - \bar {r} _ {b}\right) ^ {2}}},\tag{1}
$$

$$
U J a c c a r d _ {a, b} = \frac {\left| I _ {a , b} \right|}{\left| I _ {a} \right| + \left| I _ {b} \right| - \left| I _ {a , b} \right|},\tag{2}
$$

where $r _ { a , i }$ and $r _ { b , i } \in [ 1 , 5 ]$ represent the ratings of users a and b on item i respectively, $\bar { r } _ { a }$ and $\bar { r } _ { b } { \in } [ 1 , 5 ]$ represent the average rating values of users a and b on all items that are rated by each user separately. $I _ { a , b }$ is the set of co-rated items by both users a and b. $| I _ { a , b } |$ is the number of items that have been commonly rated by active user a and potential neighbor user b. |I | is the number of items that have been rated by active user a. |I | is the number of items that have been rated by neighbor user $b .$ Formally, for any $a , b \in U ,$ the enhanced user-based CF between active user a and potential neighbor user b, $e U C F _ { a , b } { \mathrm { : } }$ $U \times U {  } [ - 1 , 1 ]$ , is given by:

$$
e U C F _ {a, b} = U C P C _ {a, b} \times U J a c c a r d _ {a, b}.\tag{3}
$$

3.1.1.1.2. U-Step 1.2: user-based implicit trust computation. This step divided into two main connected sub-steps, trust derivation and trust propagation. Trust derivation takes as input the rating matrix and calculates the direct implicit trust scores of every pair of users. After computing the direct implicit trust scores, trust propagation exploits the indirect trust relationships to calculate the trust scores between users who are not directly connected.

3.1.1.1.2.1. Trust derivation. This study measures the trustworthiness of a given user by measuring the prediction accuracy of that user, as a recommender, in the past to the active user. For example, if user b has delivered high accurate recommendations to active user a in the past, then user b should acquire a high trust score from active user a [16]. For trust derivation, we <sup>fi</sup>rst use the Resnick's prediction method [29] to compute the predicted rating. For any a, $b \in U , i \in I ,$ the predicted rating of item i for the user a by the only neighborhood user b, $P _ { a , i } \colon U \times I \to [ 0 , 5 ]$ , is given as follows:

$$
P _ {a, i} = \bar {r} _ {a} + \left(r _ {b, i} - \bar {r} _ {b}\right),\tag{4}
$$

where $r _ { b , i } \in [ 1 , 5 ]$ denotes the rating of item i by user $b ,$ and $\bar { r } _ { a }$ and $\bar { r } _ { b } { \in } [ 1 , 5 ]$ are the mean ratings of users a and b, respectively. Bearing in mind that the prediction accuracy of a user in the past is used to measure his/her trustworthiness, we use the Mean Squared

Differences (MSD) method [1,42] to measure the degree of similarity of user a with respect to user b from the prediction error of co-rated items between them, as shown by Eq. (5). To ensure that the value of $M S D _ { a , b } \in [ 0 , 1 ]$ , we have <sup>fi</sup>rst to normalize the rating $r _ { a , i }$ and the predicted rating $P _ { a , i }$ values within the range [0,1] using the Max–Min Normalization method [13]. For any $a , b \in U$ , the degree of similarity of user a with respect to user $b , M S D _ { a , b } { \in } [ 0 , 1 ]$ , based on the prediction error of co-rated items between them ${ \cal I } _ { a , b } ,$ , is given by:

$$
M S D _ {a, b} = \left(1 - \frac {\sum_ {i = 1} ^ {I _ {a , b}} \left(P _ {a , i} - r _ {a , i}\right) ^ {2}}{I _ {a , b}}\right),\tag{5}
$$

where $P _ { a , t }$ refers to the normalized predicted rating of item i for user $a , r _ { a , i }$ denotes the normalized rating value of item i with respect to user a, $I _ { a , b }$ is the number of co-rated items between users a and b.

However, the $M S D _ { a , b }$ metric still has a major drawback, as demonstrated in a previous research work in implicit trust <sup>fi</sup>ltering approaches [16,27,47], since it does not consider what has not been rated between users a and b when computing the implicit trust between them. The impact of this issue can be seen when users who have rated a very small number of items express a high level of trust with almost all other users. For example, an implicit trust value of 0.85 calculated between two users with only 15 common items is not as trustworthy and reliable as an implicit trust value of 0.75 calculated with 170 common items. The proportion between the common ratings and the total rated items should be taken into consideration when computing the derived implicit trust. One way to solve this issue is to use the user-based Jaccard similarity metric [6] (refer to Eq. (2)). We therefore use the user-based Jaccard metric as a weighting scheme to consider the proportion between the common ratings and the total rated items when computing the derived implicit trust, as given by Eq. (6). For any $a , b \in U ,$ , the implicit trust derivation metric between user a and user $b , D T r u s r _ { a , b } \colon U \times U \to [ 0 , 1 ]$ , is given as:

$$
D T r u s t _ {a \rightarrow b} = M S D _ {a, b} \times U J a c c a r d _ {a, b}.\tag{6}
$$

3.1.1.1.2.2. Trust propagation. Trust derivation computes the direct implicit trust values between users in the trust social network. Trust propagation (also known as trust inference) is needed when there are no direct trust relations between users. Thus, from the direct trust network, it is possible to infer the trust and establish new relations among users who have no direct trust link between them. For example, assuming that user $a \in U$ (source user) trusts user $b \in U$ (intermediate user) and user b trusts user $c \in U$ (target user), it can be inferred by using trust propagation matrices that user a can trust user c at some level. In case there is more than one intermediate user (bs), a trust aggregation method is needed to combine the different trust beliefs that target user a has received from bs about c to infer a unique trust belief about c. Richardson et al. [32] clari<sup>fi</sup>ed three different types of trust path aggregation: maximum value, minimum value and average. The maximum value method takes the path with the highest trust and neglects all other paths. The minimum value method takes the trust path with the lowest trust value and neglects all other paths. The average approach <sup>fi</sup>nally calculates an average using the trust values of all available paths. Taking into consideration that those weak paths (with lowest trust value) can convey valuable information like strong paths (with highest trust value), the Weighted Mean Aggregation Method is used because previous research has shown its robust performance in the trust path aggregation [11,24,28]. The mean aggregation method ensures that the inferred trust value is most signi<sup>fi</sup>cantly weighted by the most trusted users. For any $a , b , c \in U ,$ , the propagated implicit trust value that indicates what extent user a implicitly trusts user $c , P T r u s t _ { a  c } \colon U \times U \{ 0 ,$ 1], is computed as follows:

$$
P T r u s t _ {a, c} = \frac {\sum_ {b \in a d j (a)} D T r u s t _ {a , b} \times \left(D T r u s t _ {b , c} \times \beta_ {d}\right)}{\sum_ {b \in a d j (a)} D T r u s t _ {a , b}}, \quad \text { where } D T r u s t _ {a, b} \geq \lambda\tag{7}
$$

$$
\beta_ {d} = (M P D i s t - d + 1) / M P D i s t, \quad d \in [ 2, M P D i s t ]\tag{8}
$$

where user a has b direct trusted adjacent neighbors that trust user c, $D T r u s t _ { a , b } \in [ \lambda , 1 ]$ is the implicit trust value between user a and user b. The parameter $\lambda { \in } ( 0 . . 1 ]$ is a tunable trust <sup>fi</sup>lter threshold applied to ensure that non-trustworthy users, as de<sup>fi</sup>ned by the trust <sup>fi</sup>lter, are not allowed to participate in the trust propagation process. Thus, users who have a trust value below the threshold are considered as untrustworthy users, and cannot in<sup>fl</sup>uence the trust propagation process. We can select a proper value of λ by performing sensitivity analysis on a particular dataset (see Section 5.4 for more detail). Massa and Avesani [26] acknowledged that the trustworthiness of the propagated trust decreases along with every new trust propagation step. Therefore, to ensure that trust decreases along the propagation, we use the trust metric MoleTrust [26] as shown in Eq. (8) as a weighting scheme $\beta _ { d } \in ( 0 . . 1 ]$ in the proposed trust propagation metric. MPDist is a tunable trust propagation limit that is used to control the maximum distance from the source user to where the trust is propagated. For instance, if the MPDist is set to 3, trust is only propagated up to users at distance 3. We can select a proper value of MPDist by performing sensitivity analysis on a particular dataset (see Section 5.4 for more details). Parameter d is the trust propagation distance from the source user to other users (i.e., refers to the number of propagation hops in the trust propagation path from the trustor to the trustee). For trust propagation, two hops are required as a minimum (i.e., at least two hops are required to propagate trust between users a and c. The <sup>fi</sup>rst hop is from user a to user b and the second is from user b to user c). For example, assume MPDist=3, then for $d = 2 \ ( \beta _ { 2 } = ( 3 -$ $2 + 1 ) / 3 = 0 . 6 6 7 )$ and for $d = 3 ( \beta _ { 3 } = ( 3 - 3 + 1 ) / 3 = 0 . 3 3 4 )$ . The weighting parameter $\beta _ { d }$ will ensure that trust scores from the directly trusted neighbors (or at a close propagation distance) will have more weights, and therefore, more in<sup>fl</sup>uence on the trust propagation process.

3.1.1.2. U-Step 2: select neighbors. Two sets of neighbors that are the most similar and trusted users to the active user in terms of enhanced user-based CF $( N ^ { e U C F } \in U )$ similarity and trustworthiness $( N ^ { T r u s t } { \in } U )$ are selected. For the neighbors' selection process, two methods have been employed in the recommender systems [14]: the Top-n method (e.g., a prede<sup>fi</sup>ned number of users with greatest correlation are selected), and the correlation weight threshold (e.g., all users with similarity correlation exceeding a certain threshold are selected). We use the Top-n method as recommended by Herlocker, Konstan and Riedl [14].

3.1.1.3. U-Step 3: calculate Weighted Predictions. Computing the rating predictions is the <sup>fi</sup>nal important step in the recommendation process. The deviation-from-mean approach [14,29] is used in the weighted predictor module to calculate the predicted rating value the active user a∈U on item $x { \in } I , P _ { a , x T e C F } \colon U { \times } I {  } [ 0 , 5 ]$ , as given by

$$
P _ {a, x} ^ {T e C F} = \bar {r} _ {a} + \frac {\sum_ {b = 1} ^ {N ^ {e C F}} \left(e U C F _ {a , b} \times \left(r _ {b , x} - \bar {r} _ {b}\right)\right) + \sum_ {b = 1} ^ {N ^ {T r u s t}} \left(T r u s t _ {a , b} \times \left(r _ {b , x} - \bar {r} _ {b}\right)\right)}{\sum_ {b = 1} ^ {N ^ {e C F}} e U C F _ {a , b} + \sum_ {b = 1} ^ {N ^ {T r u s t}} T r u s t _ {a , b}}\tag{9}
$$

where, ${ \bar { r } } _ { a } { \in } [ 1 , 5 ]$ and $\bar { r } _ { b } { \in } [ 1 , 5 ]$ represent the average rating values of the active user a and potential neighbor user b on all items that are rated by each user separately, $r _ { b , x } \in [ 1 , 5 ]$ denotes the rating value of the potential neighbor user b for target item x. $e U C F _ { a , b } { \in } [ - 1 , 1 ]$ represents the enhanced user-based similarity value between the active user a and potential neighbor user b, and is obtained from the user– user CF similarity matrix. $T r u s t _ { a , b } { \in } [ 0 , 1 ]$ represents the implicit trust value between the active user a and potential neighbor user b, and is obtained from the user–user implicit trust matrix. $N ^ { e U C F }$ and $N ^ { T r u s t }$ are two sets of the nearest neighbors of active user a.

## 3.1.2. The item-based semantic-enhanced CF module

This module produces item-based semantic-enhanced CF recommendations. It integrates the enhanced item-based CF with the item-based semantic <sup>fi</sup>ltering approaches to exploit their advantages and to eliminate the known limitations of the current item-based CF approaches. Also, the notion of the item's reputation weight is de<sup>fi</sup>ned and introduced into the prediction computation process.

3.1.2.1. I-Step 1: calculate item-based CF and semantic similarity. This process is divided into three steps: <sup>fi</sup>rst is the enhanced item-based CF similarity computation, the second is item-based semantic similarity computation, and <sup>fi</sup>nally the item reputation computation.

3.1.2.1.1. I-Step 1.1: enhanced item-based CF similarity computation. The combination of the Adjusted Cosine similarity measure [36] and the item-based Jaccard [6] similarity measures is used to calculate the enhanced item-based CF similarity value between any pair of items. By combining the item-based Adjusted Cosine with the item-based Jaccard, we can ensure that items that have been rated by many users are preferred to others that are only rated by a few users:

$$
I A d j C o s _ {x, y} = \frac {\sum_ {u = 1} ^ {U _ {x , y}} \left(r _ {u , x} - \bar {r} _ {u}\right) \times \left(r _ {u , y} - \bar {r} _ {u}\right)}{\sqrt {\sum_ {u = 1} ^ {U _ {x , y}} \left(r _ {u , x} - \bar {r} _ {u}\right) ^ {2}} \times \sqrt {\sum_ {u = 1} ^ {U _ {x , y}} \left(r _ {u , y} - \bar {r} _ {u}\right) ^ {2}}},\tag{10}
$$

$$
I J a c c a r d _ {x, y} = \frac {\left| U _ {x , y} \right|}{\left| U _ {x} \right| + \left| U _ {Y} \right| - \left| U _ {x , y} \right|},\tag{11}
$$

where $r _ { u , x }$ and $r _ { u , y } { \in } [ 1 , 5 ]$ represent the ratings of the active user u on items x and y respectively. $\bar { r } _ { u } \in [ 1 , 5 ]$ is the mean rating value of user u on all items, and $U _ { x , y }$ is the set of users who rated both items x and y. $| U _ { x , y } |$ is the number of users who have rated both target item x and potential neighbor item y. |U | is the number of users who have rated a target item x. |U | is the number of users who have rated a potential neighbor item y. Speci<sup>fi</sup>cally, for any $x , y \in I ,$ the enhanced item-based CF similarity between target item x and potential neighbor item $y , e I C F _ { x , y } \colon I \times I \to [ - 1 , 1 ]$ , is given by:

$$
e I C F _ {x, y} = I A d j C o s _ {x, y} \times I J a c c a r d _ {x, y}.\tag{12}
$$

3.1.2.1.2. I-Step 1.2: item-based semantic similarity computation. In order to utilize the semantic information of items, we <sup>fi</sup>rst have to create the item taxonomy in a tree hierarchy structure, with the items located in the leaves. A taxonomy T is de<sup>fi</sup>ned by three elements: a <sup>fi</sup>nite set of nodes G; a root; and a parent function to represent the parent–child relationship between two nodes. To build such a taxonomy in a given domain, we have to (1) identify the total number of main categories that every item may belong to; (2) create the main item categories; (3) assign each item to the appropriate main category (one item can be assigned to more than one category). The item taxonomy has two levels of nodes. The <sup>fi</sup>rst level contains the categories of main items, and the second level contains the items as leaf nodes, where each item belongs to one or more categories. Let T be an item taxonomy given by experts that contains a set of g categories that items may fall into. Each item is represented as a binary vector, as shown by:

$$
\vec {V} _ {\chi , g} = \Big (v _ {\chi , 1}, v _ {\chi , 2}, \dots .., v _ {\chi , g} \Big),\tag{13}
$$

where $\widehat { V } _ { x , g }$ is an item vector that represents the item category vector for item x. We de<sup>fi</sup>ne $\nu _ { x , j } ~ ( j = 1 , . . . , g )$ as a binary variable, as follows:

$$
v _ {x, j} = \left\{ \begin{array}{l l} 1 & \text { If   Item   } x \text {   belong   to   category   } j \\ 0 & \text { If   Item   } x \text {   does   not   belong   to   category   } j \end{array} \right..\tag{14}
$$

The similarity between the two items is computed based on their semantic descriptions, as given in the item taxonomy. For this purpose, we use the binary Jaccard similarity coef<sup>fi</sup>cient [43] to compute the degree of overlap of categories between any pair of items. For any x, $y \in I ,$ the item-based semantic similarity between target item x and potential neighbor item y, $S S i m _ { x , y } \colon I \times I \to [ 0 , \ 1 ] ,$ , is based on the ratio of the common categories to their total categories, as shown by:

$$
\begin{array}{l} S S i m _ {x, y} = \frac {C _ {1 1}}{C _ {0 1} + C _ {1 0} + C _ {1 1}}, \\ \left\{ \begin{array}{l} C _ {1 1} = \text { Total   number   of   occurrences   where } v _ {x, j} \text { is } 1 \text { and } v _ {y, j} 1 \\ C _ {0 1} = \text { Total   number   of   occurrences   where } v _ {x, j} \text { is } 0 \text { and } v _ {y, j} 1 \\ C _ {1 0} = \text { Total   number   of   occurrences   where } v _ {x, j} \text { is } 1 \text { and } v _ {y, j} 0 \end{array} \right\}. \end{array}\tag{15}
$$

3.1.2.1.3. I-Step 1.3: item reputation computation. The percentage of users who have rated an item can re<sup>fl</sup>ect weather it is popular or not. The more ratings an item has, the more popular the item is. Also, the mean rating value of an item is a reasonable indication of the item likeability. Henceforth, in this paper, we consider the product of the item popularity with the item likeability to refer to the item reputation, as follows:

$$
I R _ {y} = \left(\frac {\left| U _ {y} \right|}{\left| U \right|}\right) \times \bar {r} _ {y}\tag{16}
$$

where $U _ { y }$ represents the number of users who rated the item y, U is the total number of users in the recommender system, and $\bar { r } _ { y }$ is the mean rating value of the item y.

3.1.2.2. I-Step 2: select neighbors. The Top-n method is used to select two sets of neighbors that are the most similar items to the target item, in terms of item-based semantic similarity $( N ^ { s e m } \in I )$ and enhanced item-based CF $( N ^ { e I C F } { \in } I )$ similarity, from the item–item semantic and CF similarity matrices.

3.1.2.3. I-Step 3: calculate weighted predictions. This step computes the rating predictions of all unseen items that an active user has not yet rated. The predicted rating of active user a∈U on a target item x∈I, $P _ { a , x S e C F } \colon U { \times } I \to [ 0 , 5 ]$ is calculated using the weighted sum of deviations from the mean item rating approach [6,14,29] as given by Eq. (17):

$$
P _ {a, x} ^ {S e C F} = \bar {r} _ {x} + \frac {\sum_ {y = 1} ^ {N ^ {e l C F}} \left(e I C F _ {x , y} \times \left(r _ {a , y} - \bar {r} _ {y}\right) \times I R _ {y}\right) + \sum_ {y = 1} ^ {N ^ {S e m}} \left(S S i m _ {x , y} \times \left(r _ {a , y} - \bar {r} _ {y}\right) \times I R _ {y}\right)}{\sum_ {y = 1} ^ {N ^ {e l C F}} \left(e I C F _ {x , y} + I R _ {y}\right) + \sum_ {y = 1} ^ {N ^ {S e m}} \left(S S i m _ {x , y} + I R _ {y}\right)},\tag{17}
$$

where, $\bar { r } _ { x }$ and $\bar { r } _ { y } { \in } [ 1 , 5 ]$ are the mean rating values of the target item x and potential neighbor item y, respectively. $e I C F _ { x , y } { \in } [ - 1 , 1 ]$ represents the enhanced item-based CF similarity value between the target item x and neighbor item y, and is obtained from the item–item CF similarity matrix. $S S i m _ { x , y } { \in } [ 0 , 1 ]$ represents the item-based semantic similarity value between the target item x and neighbor item y, and is obtained from the item–item semantic similarity matrix. $N ^ { e I C \bar { F } }$ and $N ^ { s e m }$ are the two sets of nearest neighbors of the target item x in terms of enhanced item-based CF and item-based semantic similarities respectively, obtained by the neighbors' selection module. $r _ { a , y } \in [ 1 , 5 ]$ refers to the rating value of the neighbor item y with respect to the active user a. $I R _ { y }$ is the item reputation score of neighbor item y. The incorporation of the reputation scores of the neighbor items ensures that the neighbor items with a high reputation contribute more to the <sup>fi</sup>nal prediction value of the target item than do neighbor items with a low reputation.

## 3.1.3. The prediction fusion module

The fusion prediction value $( F P _ { a , x } { \in } [ 0 , 5 ] )$ is calculated by Eq. (18) where all possible ways to obtain a rating prediction value for an active user a who has not rated the target item x are taken into account.

$$
F P _ {a, x} = \left\{ \begin{array}{l l} 0 & \text {if} P _ {a, x} ^ {T e C F} = 0 \text {and} P _ {a, x} ^ {S e C F} = 0 \\ P _ {a, x} ^ {T e C F} & \text {if} P _ {a, x} ^ {T e C F} \neq 0 \text {and} P _ {a, x} ^ {S e C F} = 0 \\ P _ {a, x} ^ {S e C F} & \text {if} P _ {a, x} ^ {T e C F} = 0 \text {and} P _ {a, x} ^ {S e C F} \neq 0 \\ \frac {2 \times P _ {a , x} ^ {T e C F} \times P _ {a , x} ^ {S e C F}}{P _ {a , x} ^ {T e C F} + P _ {a , x} ^ {S e C F}} & \text {if} P _ {a, x} ^ {T e C F} \neq 0 \text {and} P _ {a, x} ^ {S e C F} \neq 0 \end{array} . \right.\tag{18}
$$

## 3.2. Computational complexity analysis

In most recommendation algorithms, the computation cost rapidly grows as both the number of m users and the number of n items grow. The classical item-based CF computational complexity is ${ \mathsf { O } } ( m \times n ^ { 2 } )$ in the worst case. The classical user-based CF computational complexity is O(m×n) in the worst case [18,21]. In the TSF approach, we <sup>fi</sup>rst have to analyze the computational complexities of its main components, which are the user-based trust-enhanced CF and item-based semantic-enhanced CF approaches. The computational complexity of the user-based trust-enhanced CF recommendation approach depends on the amount of time required for each active user to identify the most trusted and similar users and the amount of time required computing the predictions for unrated target items. The upper bound complexity of this step is divided into three sup-steps: <sup>fi</sup>rst, $0 ( m \times \bar { k ^ { M a x P r o D i s t } } )$ is required to build the implicit trust network and <sup>fi</sup>nd the most trusted neighbors. Where k is the maximum number of edges per node in the implicit trust network, and MaxProDist is the maximum distance from the source user node to where implicit trust between users is propagated. This process can be accomplished of<sup>fl</sup>ine. Then, for an active user, O(m×n) is the upper bound on the complexity required to determine the nearest neighbors in terms of enhanced user-based CF similarities. Finally, O(n) is required to predict all unrated items; therefore the overall computational complexity becomes $0 ( m \times k ^ { M a x P r o D i s t } + m + m \times$ $n + n ) { \approx } 0 ( m { \times } k ^ { M a x P r o D i s t } )$ .

The computational complexity of the item-based semanticenhanced CF recommendation approach depends on the amount of time required for each target item to identify the most similar items and the amount of time required to compute the predictions. Let g be the number of item categories for n items, to generate recommendations for m users: $0 ( m \times n ^ { 3 } \times g )$ and $0 ( m \times n ^ { 2 } )$ are the upper bounds on the complexity required to determine the nearest neighbors for target items in terms of item-based semantic similarity and enhanced item-based CF similarity, respectively. This process can be accomplished of<sup>fl</sup>ine. Also, O(n) is required to predict all unrated items; hence the overall computational complexity becomes $0 ( m \times n ^ { 3 } \times g +$ $m \times n ^ { 2 } + n ) \approx 0 ( m \times n ^ { 3 } \times g )$

The computational complexity of the TSF recommendation approach is the combination of the computational complexities of both the above approaches, which is $0 ( m \times k ^ { M a x P r o D i s t } ) + 0 ( m \times n ^ { 3 } \times g )$ in addition to the prediction fusion process that is O(n). Although our proposed TSF recommendation approach is computationally more expensive than the classical CF-based recommendation approaches, high computational complexity is often required to enhance the quality of recommendations. In addition, most of the required calculations of the TSF recommendation approach, including the time required to build the implicit trust network $0 ( m \times k ^ { M a x P r o \overline { { { D } } } i s t } )$ and the time required to determine the nearest neighbors for target items in terms of item-based semantic similarity and enhanced item-based CF similarity $0 ( m \times n ^ { 3 } \times g ) + { \cal O } ( m \times n ^ { 2 } )$ , can be completed of<sup>fl</sup>ine.

Table 1 Raw supplier–buyer rating matrix.

<table><tr><td colspan="7">Suppliers</td></tr><tr><td>Buyers</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td> $B_1$ </td><td>Null</td><td>Null</td><td>3</td><td>Null</td><td>Null</td><td>Null</td></tr><tr><td> $B_2$ </td><td>4</td><td>3</td><td>4</td><td>2</td><td>Null</td><td>Null</td></tr><tr><td> $B_3$ </td><td>4</td><td>2</td><td>Null</td><td>4</td><td>Null</td><td>4</td></tr><tr><td> $B_4$ </td><td>Null</td><td>1</td><td>Null</td><td>Null</td><td>4</td><td>5</td></tr></table>

## 4. Case-based example

Assume that there are six ‘Food and Beverage’ Australian supplier businesses $\left( S _ { 1 } \mathrm { t } 0 S _ { 6 } \right)$ listed in an online suppliers' directory. Also, suppose that there are four overseas buyers $( \mathtt { B } _ { 1 }$ to $\mathsf { B } _ { 4 } )$ who have conducted business with some of the listed suppliers and have rated them on a numeric <sup>fi</sup>ve-point scale from 1 (Poor) to 5 (Excellent). Accordingly, a raw supplier–buyer rating matrix can be created as depicted in Table 1. In the following rating matrix, we consider the buyer $\mathtt { B } _ { 1 }$ to be an extreme CS user, and suppliers $S _ { 4 }$ and $S _ { 5 }$ to be extreme CS items, since both have only one rating. We also assume that the supplier taxonomy has eight categories; each supplier belongs to one or more categories as shown in Table 2.

Now, assume that the overseas buyer B is looking for ‘Food and Beverage’ Australian supplier businesses. A numerical recommendation example is given to illustrate how the TSF recommendation approach is used to generate recommendations.

## 4.1. The user-based trust-enhanced CF module

## 4.1.1. U-Step 1: calculate user-based CF similarity and implicit trust

4.1.1.1. U-Step 1.1: enhanced user-based CF similarity computation. Based on Table 1, we compute the enhanced user-based CF similarities between the four buyers as given in Table 3.

## 4.1.1.2. U-Step 1.2: user-based implicit trust computation

4.1.1.2.1. Trust derivation. The direct implicit trust values of each pair of buyers are calculated using Eq. (6), and we obtain the buyer–buyer direct trust implicit values, as shown in Table 4.

4.1.1.2.2. Trust propagation. In Table 4, we observe that for buyer $\mathsf { B } _ { 1 } ,$ the only trusted neighbor is buyer ${ \tt B } _ { 2 }$ (Trust $B _ { 1 }  B _ { 2 } = 0 . 2 5 )$

Table 2 Supplier–supplier category matrix.

<table><tr><td colspan="9">Suppliers</td></tr><tr><td>Category</td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td><td> $g_4$ </td><td> $g_5$ </td><td> $g_6$ </td><td> $g_7$ </td><td> $g_8$ </td></tr><tr><td> $S_1$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td> $S_2$ </td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $S_3$ </td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $S_4$ </td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $S_5$ </td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $S_6$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr></table>

Table 3  
Buyer–buyer enhanced user-based CF similarity matrix.

<table><tr><td> $eUCF_{B',B'}$ </td><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td></tr><tr><td> $B_1$ </td><td></td><td>0.00</td><td>N/A</td><td>N/A</td></tr><tr><td> $B_2$ </td><td></td><td></td><td>0.03</td><td>0.17</td></tr><tr><td> $B_3$ </td><td></td><td></td><td></td><td>0.38</td></tr><tr><td> $B_4$ </td><td></td><td></td><td></td><td></td></tr></table>

Table 4  
Buyer–buyer direct implicit trust matrix.

<table><tr><td> $DTrust_{B',B'}$ </td><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td></tr><tr><td> $B_1$ </td><td></td><td>0.25</td><td>N/A</td><td>N/A</td></tr><tr><td> $B_2$ </td><td>0.25</td><td></td><td>0.35</td><td>0.17</td></tr><tr><td> $B_3$ </td><td>N/A</td><td>0.35</td><td></td><td>0.40</td></tr><tr><td> $B_4$ </td><td>N/A</td><td>0.17</td><td>0.40</td><td></td></tr></table>

There are no direct implicit trust connections between buyer $\mathtt { B } _ { 1 }$ and buyers ${ \sf B } _ { 3 }$ and ${ \tt B } _ { 4 }$ as they do not co-rate any similar suppliers, thus implicit trust propagation is needed in this situation to infer the indirect implicit trust values between them. Let $\lambda { = } 0 . 1 5$ and $M P D i s t = 2 \ ( { \mathrm { i . e . } }$ $\beta _ { d } = 0 . 5 0 ) ;$ ; we calculate the propagated implicit trust values between buyers $B _ { 1 } \to B _ { 3 }$ and $B _ { 1 } \to B _ { 4 }$ as shown in Fig. 2.

Table 5 shows the user–user implicit trust matrix of the four buyers after the trust propagation process.

## 4.1.2. U-Step 2: select neighbors

Let the number of nearest neighbors $N ^ { T r u s t } = 3$ and $N ^ { e U C F } { = } 3$ ; then based on Tables 3 and 5, we identify the nearest neighbors to any given buyer in terms of enhanced user-based CF similarities and trustworthiness, as shown in Table $6 .$

As shown in Table 6, buyer $\mathtt { B } _ { 1 } ,$ who is considered to be a CS user, has no neighbors, in terms of the enhanced user-based CF approach, who can be used to produce recommendations. However, buyer $\mathtt { B } _ { 1 }$ (by exploiting the advantage of trust propagation) has three trusted neighbors (buyers $\mathsf { B } _ { 2 } , \mathsf { B } _ { 3 } ,$ and $\mathsf { B } _ { 4 } )$ who can be used to produce recommendations. Accordingly, trust propagation can, indeed, be utilized to increase the recommendation accuracy and coverage in cases of data sparsity and CS users.

## 4.1.3. U-Step 3: calculate weighted predictions

On the basis of Tables 3, 5 and 6, we can use Eq. (9) to calculate the user-based trust enhanced CF (TeCF) predicted rating values on each un-rated supplier for all buyers, as shown in Table 7.

Table 5  
Buyer–buyer propagated implicit trust matrix.

<table><tr><td> $PTrust_{B',B'}$ </td><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td></tr><tr><td> $B_1$ </td><td></td><td>0.25</td><td>0.175</td><td>0.131</td></tr><tr><td> $B_2$ </td><td>0.25</td><td></td><td>0.35</td><td>0.17</td></tr><tr><td> $B_3$ </td><td>0.125</td><td>0.35</td><td></td><td>0.40</td></tr><tr><td> $B_4$ </td><td>0.081</td><td>0.17</td><td>0.40</td><td></td></tr></table>

Values of bold data emphasize the implicit trust values between buyers B $\cdot { \cal B } _ { 3 } , { \cal B } _ { 1 } {  } { \cal B } _ { 4 } ,$ $B _ { 3 } {  } B _ { 1 }$ and $B _ { 4 } {  } B _ { 1 }$ after the trust propagation process.

## 4.2. The item-based semantic-enhanced CF module

## 4.2.1. I-Step 1: calculate item-based CF and semantic similarity

4.2.1.1. I-Step 1.1: enhanced item-based CF similarity computation. Based on Table 1, we compute the enhanced item-based CF similarities between the six suppliers, as given in Table 8.

4.2.1.2. I-Step 1.2: item-based semantic similarity computation. Based on Table 1, we use Eq. (15) to calculate the item-based semantic similarity between the six suppliers, as given in Table 9.

4.2.1.3. I-Step 1.3: item reputation computation. In this step, based on Table 2, we use Eq. (16) to calculate the item reputation scores for the six suppliers as given in Table 10.

## 4.2.2. I-Step 2: select neighbors

Let the number of nearest neighbors $N ^ { s e m } = 4$ and $N ^ { e I C F } { = } 4 ;$ based on Tables 8 and $^ { 9 , }$ we identify the nearest neighbors to any given buyer in terms of enhanced item-based CF and semantic similarities, as shown in Table 11.

Table 11 shows that semantic information can indeed be utilized to increase the recommendation accuracy and coverage in cases of data sparsity and CS items.

## 4.2.3. I-Step 3: calculate weighted predictions

On the basis of Tables 8, 9, 10 and 11, we use Eq. (17) to calculate the item-based semantic-enhanced CF (SeCF) predicted rating values on each un-rated supplier for all buyers (Table 12).

## 4.3. The prediction fusion module

On the basis of Tables 7 and 12, we use Eq. (18) to calculate the <sup>fi</sup>nal TSF predicted rating values on each un-rated supplier for all buyers, as shown in Table 13.

Finally, let Top-k $( k = 3 )$ ; hence, the most interested three suppliers for an active buyer are recommended. According to the <sup>fi</sup>nal

![](/api/attachments/NVXBFQE2/fulltext/images/b2ecfe734c28b094db3d4a063ca4d7b02d7132f4f32f3455f67104ae3b878d72.jpg)  
Fig. 2. An example of the trust propagation process.

Table 10  
Table 6 Neighbors' selection.

<table><tr><td rowspan="2">Neighbors&#x27; order</td><td colspan="2"> $B_1$ </td><td colspan="2"> $B_2$ </td><td colspan="2"> $B_3$ </td><td colspan="2"> $B_4$ </td></tr><tr><td>CF</td><td>Trust</td><td>CF</td><td>Trust</td><td>CF</td><td>Trust</td><td>CF</td><td>Trust</td></tr><tr><td>1</td><td>N/A</td><td> $B_2$ </td><td> $B_4$ </td><td> $B_3$ </td><td> $B_4$ </td><td> $B_4$ </td><td> $B_3$ </td><td> $B_3$ </td></tr><tr><td>2</td><td>N/A</td><td> $B_3$ </td><td> $B_3$ </td><td> $B_1$ </td><td> $B_2$ </td><td> $B_2$ </td><td> $B_2$ </td><td> $B_2$ </td></tr><tr><td>3</td><td>N/A</td><td> $B_4$ </td><td>N/A</td><td> $B_4$ </td><td>N/A</td><td> $B_1$ </td><td>N/A</td><td> $B_1$ </td></tr></table>

TSF predicted supplier–buyer rating matrix, as shown in Table 13, the top three recommended suppliers for active buyer $\mathtt { B } _ { 1 }$ are $\mathsf { S } _ { 6 } \ ( P V _ { B 1 } , \mathsf { \Lambda } _ { S 6 } = 4 . 0 0 )$ , S<sub>5</sub> $( P V _ { B 1 } , \varsigma 5 = 3 . 5 8 )$ and S<sub>1</sub> $( P V _ { B 1 } , \varsigma _ { 1 } = 3 . 5 7 )$

## 5. Experiments and results

This section demonstrates the effectiveness of the proposed TSF recommendation approach. It includes the datasets, evaluation measures, benchmark algorithms, and evaluation results.

## 5.1. Datasets

We use two datasets to validate the performance of the proposed TSF recommendation approach.

(1) The MovieLens dataset. This dataset contains 100,000 ratings of 1682 movies from 943 users (http://www.movieLens.org). The ratings scale is from 1 to 5. Movies in the dataset are categorized in a two-level taxonomy hierarchical structure. The <sup>fi</sup>rst level contains the main item categories (i.e., Movie genres) that every item belongs to, and the second level contains the items as leaf nodes (i.e., Movies). The genre has 18 attributes including Action, Adventure, Children's… etc. The sparsity level of the MovieLens dataset is 93.7% (sparsity level=1− densit $\mathsf { y } = 1 - ( 1 0 0 , 0 0 0 / ( 9 4 3 \times 1 6 8 2 ) ) = 0 . 9 3 7 )$

(2) The Yahoo! Webscope R4 dataset. This dataset is provided as part of the Yahoo! Research Alliance Webscope program (http://webscope.sandbox.yahoo.com), to be used for approved non-commercial research purposes. The Yahoo! Webscope dataset consists of two <sup>fi</sup>les, a training dataset and a test dataset, where ratings in both sets are discrete values from 1 to 5 on a single criterion (i.e., each user can only make one rating for a speci<sup>fi</sup>c movie). The training data contains 7642 users, 11,915 movies and 211,231 ratings. The test data contains 2309 users, 2380 movies and 10,136 ratings. Movies in the dataset are categorized into a two-level taxonomy hierarchical structure. The <sup>fi</sup>rst level contains the main item categories (i.e., Movie genres) that every item belongs to, and the second level contains the items as leaf nodes (i.e., Movies). The genre has 32 attributes including Action/Adventure; Adaptation; Animation… etc. The sparsity level of the Yahoo! R4 training dataset is 99.8% (sparsity level=1−density=1− $( 2 1 1 , 2 3 1 / ( 7 6 4 2 \times 1 1 , 9 1 5 ) ) = 0 . 9 9 7 6 )$

Table 7  
TeCF predicted supplier–buyer matrix.

<table><tr><td colspan="7">Suppliers</td></tr><tr><td>Buyers</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td> $B_1$ </td><td>3.65</td><td>1.86</td><td></td><td>2.47</td><td>3.67</td><td>4.00</td></tr><tr><td> $B_2$ </td><td></td><td></td><td></td><td></td><td>3.92</td><td>4.29</td></tr><tr><td> $B_3$ </td><td></td><td></td><td>4.06</td><td></td><td>4.17</td><td></td></tr><tr><td> $B_4$ </td><td>3.91</td><td></td><td>3.94</td><td>3.31</td><td></td><td></td></tr></table>

Table 8  
Supplier–supplier enhanced item-based CF similarity matrix.

<table><tr><td> $eICF_{S',S'}$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td> $S_1$ </td><td>-0.46</td><td>0.33</td><td>-0.57</td><td>N/A</td><td>0.33</td></tr><tr><td> $S_2$ </td><td></td><td>-0.25</td><td>-0.14</td><td>-0.33</td><td>-0.64</td></tr><tr><td> $S_3$ </td><td></td><td></td><td>-0.33</td><td>N/A</td><td>N/A</td></tr><tr><td> $S_4$ </td><td></td><td></td><td></td><td>N/A</td><td>0.33</td></tr><tr><td> $S_5$ </td><td></td><td></td><td></td><td></td><td>0.50</td></tr></table>

Table 9  
Supplier–supplier semantic similarity matrix

<table><tr><td> $SSim_{S',S'}$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td> $S_1$ </td><td>0.20</td><td>0.00</td><td>0.17</td><td>0.20</td><td>0.25</td></tr><tr><td> $S_2$ </td><td></td><td>0.33</td><td>0.29</td><td>0.33</td><td>0.40</td></tr><tr><td> $S_3$ </td><td></td><td></td><td>0.50</td><td>0.14</td><td>0.40</td></tr><tr><td> $S_4$ </td><td></td><td></td><td></td><td>0.50</td><td>0.60</td></tr><tr><td> $S_5$ </td><td></td><td></td><td></td><td></td><td>0.17</td></tr></table>

To verify the validity of the experimental results, a hold-out cross-validation method is applied. Through cross-validation all datasets are divided into a training set and a test set, with the training set consisting of 80% of the data and the test set consisting of 20%.

## 5.2. Evaluation metrics

A number of evaluation measures have been used to evaluate the quality of recommendations in current recommender systems. We use the most broadly popular measurement metrics: the standard Mean Absolute Error (MAE) and the Coverage metrics. The MAE is the most widely used metric in recommendation research [14,29] to measure the accuracy of recommendations. MAE measures the accuracy by computing the average absolute deviation between the system's predicted rating against the actual rating assigned by the user. Note that a lower MAE value represents a higher recommendation accuracy. Given the set of actual/predicted rating pair for all the n items available in the test set, the measurement for MAE can be given by:

$$
M A E = \frac {\sum_ {i = 1} ^ {n} \left| r _ {a i} - r _ {p _ {i}} \right|}{n}.\tag{19}
$$

The coverage measure evaluates the ability of a given recommender system to provide recommendations. The coverage is computed as the percentage of items for which a prediction is requested and for which the recommender system is able to make a prediction [14]. If we use n to denote the number of available items and $I _ { p }$ to denote the number of items for which a prediction can be made, the coverage can be given ${ \tt b y : } r _ { a , i }$

$$
C o v e r a g e = \frac {I _ {p}}{n}.\tag{20}
$$

## 5.3. Benchmark algorithms

Bearing in mind that the TSF approach is a combination of user-based and item-based recommendation algorithms, all obtained results of the TSF approach are compared with the performance of four benchmark user-based and item-based recommendation algorithms. Accordingly, we implement Resnick's user-based CF where the similarity is computed using the Pearson correlation (denoted as Resnick-UCF) [29], and the Sarwar item-based CF, which employs the vector cosine similarity (denoted as Sarwar-ICF) [36]. The algorithms have been widely exploited as benchmarks to evaluate recently proposed recommendation approaches [5,6,12,19,34,45]. To further validate the performance of the TSF recommendation approach, taking into account that the TSF approach is a combination of implicit trust and semantic <sup>fi</sup>ltering recommendation algorithms, we compare its results with the benchmark user-based implicit trust (i.e. combined trust-based <sup>fi</sup>ltering and weighting using pro<sup>fi</sup>le-level trust) (denoted as O'Donovan-Trust) [27], and item-based semantic <sup>fi</sup>ltering (denoted as Ruiz-Semantic) [35] recommendation approaches.

Supplier reputation matrix.

<table><tr><td> $IR_{S'}$ </td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td>Reputation score</td><td>2.00</td><td>1.50</td><td>1.75</td><td>1.50</td><td>1.00</td><td>2.25</td></tr></table>

Table 11  
Neighbors' selection.

<table><tr><td rowspan="2">Neigh. order</td><td colspan="2"> $S_1$ </td><td colspan="2"> $S_2$ </td><td colspan="2"> $S_3$ </td><td colspan="2"> $S_4$ </td><td colspan="2"> $S_5$ </td><td colspan="2"> $S_6$ </td></tr><tr><td>CF</td><td>Semantic</td><td>CF</td><td>Semantic</td><td>CF</td><td>Semantic</td><td>CF</td><td>Semantic</td><td>CF</td><td>Semantic</td><td>CF</td><td>Semantic</td></tr><tr><td>1</td><td> $S_3$ </td><td> $S_6$ </td><td> $S_4$ </td><td> $S_6$ </td><td> $S_1$ </td><td> $S_4$ </td><td> $S_6$ </td><td> $S_6$ </td><td> $S_6$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_4$ </td></tr><tr><td>2</td><td> $S_6$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_5$ </td><td> $S_2$ </td><td> $S_6$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_2$ </td><td> $S_2$ </td><td> $S_1$ </td><td> $S_2$ </td></tr><tr><td>3</td><td> $S_2$ </td><td> $S_5$ </td><td> $S_5$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_5$ </td><td>N/A</td><td> $S_1$ </td><td> $S_4$ </td><td> $S_3$ </td></tr><tr><td>4</td><td> $S_4$ </td><td> $S_4$ </td><td> $S_1$ </td><td> $S_4$ </td><td>N/A</td><td> $S_5$ </td><td> $S_1$ </td><td> $S_2$ </td><td>N/A</td><td> $S_6$ </td><td> $S_2$ </td><td> $S_1$ </td></tr></table>

## 5.4. Parameter setup

Based on our preliminary optimization tests on both datasets, a set of parameters is <sup>fi</sup>xed to achieve the best results in terms of prediction accuracy and coverage throughout the following experiments in Section 5.5. For the MovieLens dataset, the parameter λ=0.15 was chosen as an optimal threshold to achieve the best prediction accuracy. The maximum trust propagation distance MPDist=3 was chosen as an optimal value to reach the best performance in terms of prediction accuracy and coverage. Accordingly, β =(3−2+1)/ 3=0.667 when d=2 and $\beta _ { 3 } = ( 3 - 3 + 1 ) / 3 = 0 . 3 3 4$ when d=3. For the Yahoo! Webscope dataset, the parameter λ=0.05 was chosen as an optimal threshold to achieve the best prediction accuracy. The maximum trust propagation distance MPDist=5 was selected as an optimal value to reach the best prediction accuracy and coverage performance. Accordingly, β =(5−2+1)/5=0.80 when d=2, β = (5−3+1)/5=0.60 when d=3, β =(5−4+1)/5=0.40 when d=4 and $\beta _ { 5 } = ( 5 - 5 + 1 ) / 5 = 0 . 2 0$ when d=5 (these values are reasonable considering the sparsity level and the number of users in each dataset).

Table 12  
SeCF predicted rating matrix.

<table><tr><td colspan="7">Suppliers</td></tr><tr><td>Buyers</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td> $B_1$ </td><td>3.92</td><td>1.98</td><td></td><td>2.96</td><td>3.97</td><td>4.41</td></tr><tr><td> $B_2$ </td><td></td><td></td><td></td><td></td><td>3.96</td><td>4.41</td></tr><tr><td> $B_3$ </td><td></td><td></td><td>3.49</td><td></td><td>4.16</td><td></td></tr><tr><td> $B_4$ </td><td>4.10</td><td></td><td>3.52</td><td>3.08</td><td></td><td></td></tr></table>

Table 13  
Final TSF predicted rating matrix.

<table><tr><td colspan="7">Suppliers</td></tr><tr><td>Buyers</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td><td> $S_6$ </td></tr><tr><td> $B_1$ </td><td>3.78</td><td>1.92</td><td></td><td>2.69</td><td>3.81</td><td>4.20</td></tr><tr><td> $B_2$ </td><td></td><td></td><td></td><td></td><td>3.94</td><td>4.35</td></tr><tr><td> $B_3$ </td><td></td><td></td><td>3.75</td><td></td><td>4.17</td><td></td></tr><tr><td> $B_4$ </td><td>4.00</td><td></td><td>3.72</td><td>3.19</td><td></td><td></td></tr></table>

## 5.5. Evaluation results

A number of experiments to examine the effectiveness and verify the enhancement of the proposed TSF recommendation approach against the benchmark algorithms were conducted, in terms of improving accuracy and resolving data sparsity, CS user and CS item problems.

5.6. Comparing the recommendation accuracy of the TSF with other algorithms

The recommendation accuracy performance of the TSF approach is compared, in this experiment, with all benchmark algorithms. For this purpose, we use the MovieLens and Yahoo! Webscope datasets to validate the performance of the TSF approach. In both experiments, we varied the number of neighbors and computed the corresponding MAE for all recommendation approaches. Results in Figs. 3 and 4 demonstrate that the TSF recommendation approach achieves the best recommendation accuracy in all neighborhood sizes in all datasets, compared to other benchmark recommendation approaches. It can be concluded that the TSF recommendation approach, which takes advantage of users' trust, items' semantic and user–item rating information, is a signi<sup>fi</sup>cant improvement on the recommendation accuracy, compared to benchmark recommendation approaches.

![](/api/attachments/NVXBFQE2/fulltext/images/a7d37bbfb4451d200ce58f53186c6678fbda030dd97dc8b6a7f03bfa685a4d75.jpg)  
Fig. 3. Recommendation accuracy (MAE) comparison between the TSF approach with other benchmark algorithms on different numbers of neighbors (MovieLens dataset).

MAE comparison between the TSF with benchmark algorthms  
![](/api/attachments/NVXBFQE2/fulltext/images/14aaf8b3da6e30c1592ec0cb70b7cfcfc44e5fa159f2aa4b2380c8d1637bf1a9.jpg)  
Fig. 4. Recommendation accuracy (MAE) comparison between the TSF approach with other benchmark algorithms on different numbers of neighbors (Yahoo Webscope dataset).

![](/api/attachments/NVXBFQE2/fulltext/images/17a337f48293b23f6f3fae88dda520d7ab28e84b621d988b94196f1a38cfe483.jpg)  
Fig. 5. Recommendation accuracy (MAE) improvement on different data sparsity levels.

## 5.7. Impact of the TSF on the data sparsity problem

This section examines the effectiveness of the TSF approach to easing the data sparsity problem. The sparsity level of any dataset is de-<sup>fi</sup>ned as 1 — density. Density (Dataset)=no. of nonzero entries/total no. of entries, where the number of total entries is calculated by multiplying the number of users by the number of items; the number of nonzero entries is the total number of overall ratings in the dataset. As shown in Section 5.1, the MovieLens dataset is denser than the Yahoo! Webscope sparsity dataset because it has a lower sparsity level. Accordingly, to manipulate different levels of sparsity, we used the sparsity metric to extract and create six sparse datasets from the MovieLens dataset. In these sparse datasets, sparsity levels decrease from the highest level of 99.5% to the lowest level of 97.0% (i.e., 99.5%, 99.0%, 98.5%, 98.0%, 97.5%, and 97.0%).

Two experiments were conducted to measure the recommendation accuracy and coverage of the TSF approach against the benchmark algorithms on different data sparsity levels. Fig. 5 indicates that the TSF approach has the highest recommendation accuracy at all levels of data sparsity, compared to the benchmark algorithms. Fig. 6 validates the TSF approach as having the highest coverage for all levels of data sparsity, compared to the benchmark algorithms. We can conclude from the recommendation accuracy and coverage results that the TSF approach signi<sup>fi</sup>cantly alleviates the data sparsity problem, compared to the benchmark recommendation algorithms.

## 5.8. Impact of the TSF on the CS user problem

This section presents the results of two experiments conducted to demonstrate the effectiveness of the TSF approach in addressing the CS user problem. The two experiments, as depicted by Figs. 7 and 8, measure the recommendation accuracy and coverage of the TSF approach compared to the user-based benchmark algorithms on a different number of ratings for CS users. Fig. 7 proves that the TSF approach has the highest recommendation accuracy at any given number of ratings of CS users, compared to the user-based benchmark algorithms. Fig. 8 con<sup>fi</sup>rms that the TSF approach has the highest coverage at any given number of ratings of CS users, compared to the user-based benchmark algorithms. Accordingly, it can be concluded that the TSF approach signi<sup>fi</sup>cantly alleviates the CS user problem, compared to the user-based benchmark algorithms.

![](/api/attachments/NVXBFQE2/fulltext/images/266da96feaa703dc7312e921ab0934d265f2d896eeee048e86b2ed69e705c7f6.jpg)  
Fig. 6. Recommendation coverage improvement on different sparsity levels.

MAE comparison at different number of ratings for CS Users  
![](/api/attachments/NVXBFQE2/fulltext/images/d84072ac2b9a5d16f89c2c42fa4ed3c3e9c7f7c9c282659a4ebfa9c32a094baa.jpg)  
Fig. 7. Recommendation accuracy improvement on different numbers of ratings for CS users.

## 5.9. Impact of the TSF on the CS item problem

In this section, we report the results of two experiments to show the effectiveness of the TSF approach in alleviating the CS item problem. The two experiments, as shown by Figs. 9 and 10, demonstrate the improvement of the recommendation accuracy and coverage of the TSF approach compared to the item-based benchmark algorithms on different numbers of ratings for the CS items. Fig. 9 indicates that the TSF approach has the highest recommendation accuracy for any given number of ratings for the CS items compared to the itembased benchmark algorithms. However, using the TSF approach, the CS items that have very few ratings (two ratings) do not present signi<sup>fi</sup>cant improvements in the MAE due to the lack of ratings available for these items. Fig. 10 shows that the TSF approach has the highest coverage of any given number of ratings for the CS items in comparison with the item-based benchmark algorithms. Thereby, it can be concluded that the TSF approach signi<sup>fi</sup>cantly alleviates the CS item problem when compared to the item-based benchmark algorithms.

## 6. A case study: business-to-business recommender system

Nowadays, the business environment is increasingly changing as a result of business integration; thus, a business entity can gain a competitive advantage and increase its market share by searching, selecting and integrating with quali<sup>fi</sup>ed business partners. Business integration is the coordination, between the discrete business activities conducted by different individuals, work groups, or organizations, to form a uni<sup>fi</sup>ed business process. Business integration is essential for successful e-commerce for both B2B and the B2C [25]. Business partner selection is a very necessary prerequisite and challenge for any successful business integration. It involves a multistage decision making process consisting of several tasks, including searching for partners, negotiating and signing a contract [4]. The problem of searching for business partners is probably the least explored stage of the business partner selection process in the relevant literature [4]. Because of the information overload and the evolving number of businesses, searching for a quali<sup>fi</sup>ed business partner is a daunting and costly task. For example, for business partner searching purpose, a number of public online business directories and portals, such as Kompass.com and Masterseek.com, employ general purpose keyword search engines to support the process of retrieving potential business partners. Due to its simplicity, low recall and poor precision, the keyword query is not ef<sup>fi</sup>cient and does not satisfy users' needs [48]. In addition, as the amount of information available in business directories is overwhelming, the task of searching and locating appropriate business partners becomes too costly, inconsistent, and unreliable. These tasks can, however, be ef<sup>fi</sup>ciently supported by personalized recommender systems that facilitate the decision process of a business user (e.g., buyer) in selecting quali<sup>fi</sup>ed business partners (e.g., sellers) based on their preferences.

Coverage comparison at different number of ratings of CS Users  
![](/api/attachments/NVXBFQE2/fulltext/images/cd0ca8c64b1b72564e1131a343d69fe186b2807ecf56ad8aa0807538672ded38.jpg)  
Fig. 8. Recommendation coverage improvement on different numbers of ratings for CS users.

![](/api/attachments/NVXBFQE2/fulltext/images/810446df7c76fdb3643c68e84e5a274e89c94778102c7f6b89fa2de670bebd26.jpg)  
Fig. 9. Improvement of recommendation accuracy on different numbers of CS item ratings.

Another example is the Australian Suppliers Directory (ASD, http://www.austrade.gov.au/ASD/) that promotes Australian goods and services to overseas buyers, as well as assists overseas buyers to search suppliers all over Australia. The ASD is full of information that increases drastically day by day, about Australian businesses that have export-ready products or services (suppliers). The ASD has a search facility that employs a simple keyword search engine to help overseas companies to retrieve potential Australian business partners. The problem, as mentioned before, is that the keyword query as a search facility is neither reliable, nor ef<sup>fi</sup>cient and cannot satisfy users' particular needs. To solve this problem, a recommender system called BizSeeker [22] is implemented to provide business partner recommendation e-services for Small to Medium Businesses (SMBs).

We use a dataset extracted from the ‘BizSeeker’ system, which is related to the domain of business partner recommendations, as a case study to further validate the feasibility of applying the proposed TSF approach into real e-business applications such as B2B. The BizSeeker dataset contains 1602 ratings of 332 businesses from 100 users. The businesses are selected from the Australian Suppliers Directory which is provided by the Australian Trade Commission government trade agency (http://www.austrade.gov.au). Businesses in the dataset are categorized into a two-level taxonomy hierarchical structure. The <sup>fi</sup>rst level contains the main item categories (i.e., Business types/classes) that every item belongs to, and the second level contains the items as leaf nodes (i.e., Businesses). Businesses are categorized based on the Austrade classi<sup>fi</sup>cation of industry classes and includes 17 categories: Agribusiness; Building and construction; Business and other services; Consumer goods; Defense, security and safety; Education and training; Environment and energy; Finance and insurance; Food and beverage; Government; Health, biotechnology and wellbeing; ICT; Manufacturing; Mining; Transport; Tourism and hospitality. The sparsity level of the BizSeeker dataset is 95.2% (sparsity $\mathrm { l e v e l } = 1 - \mathrm { d e n s i t y } = 1 - ( 1 6 0 2 / ( 1 0 0 \times 3 3 2 ) ) = 0 . 9 5 2 )$

![](/api/attachments/NVXBFQE2/fulltext/images/c55f7fea81798c3d43f7c5698ca7ae781019671c9c15a9d32872b2cff293905c.jpg)  
Fig. 10. Improvement of recommendation coverage on different numbers of CS item ratings.

![](/api/attachments/NVXBFQE2/fulltext/images/de3fa2cf35045344a2c998a3a145aba0ac5b4e0d524b4f849b577b1faed29c1d.jpg)  
Fig. 11. Improvement of recommendation accuracy on different numbers of neighbors

Two experiments have been carried out to: (1) validate the applicability of the proposed TSF approach into real B2B application; and (2) evaluate the effectiveness of the proposed TSF approach compared to the benchmark algorithms on a B2B related dataset. In the <sup>fi</sup>rst experiment, we measure the recommendation accuracy as shown in Fig. 11. The experiment shows that the TSF approach achieves the highest recommendation accuracy of any given neighborhood size. The second experiment, as shown in Fig. 12, measures the recommendation coverage. Fig. 12 con<sup>fi</sup>rms that the TSF approach has the highest coverage of any given neighborhood size. It can be concluded that, by using the BizSeeker dataset, the TSF approach is a signi<sup>fi</sup>cant improvement on the recommendation accuracy and coverage, in comparison to the benchmark algorithms.

## 7. Conclusions and future work

This paper proposes the TSF recommendation approach, which provides a far higher quality of recommendations in terms of recommendation accuracy and coverage, compared to the benchmark trust, semantic and CF-based recommendation algorithms. The TSF approach fuses the user-based trust-enhanced CF and the item-based semantic-enhanced CF approaches. The user-based trust-enhanced CF approach utilizes the intuitive properties of trust and trust propagation to address the sparsity and CS user problems. The item-based semantic-enhanced CF approach employs the underlying semantic relationships between items to reduce the effect of sparsity and CS item problems. The experimental results verify the effectiveness of the TSF approach, by signi<sup>fi</sup>cantly achieving better recommendation accuracy and more coverage when dealing with data sparsity, CS users and CS items compared to the benchmark recommendation algorithms. Also, the results of the validation performed, using as a case study a B2B recommender system, allows us to conclude that the proposed TSF approach is a feasible and effective method for building recommender systems in real e-business applications.

![](/api/attachments/NVXBFQE2/fulltext/images/d831b211de5e7f765e84e9f044ab764b8a7c036ab9be5dc0102d59616607cd5f.jpg)  
Fig. 12. Improvement of recommendation coverage on different numbers of neighbors.

In future work, we plan to: (1) study and evaluate the impact of using different Uninorm functions to aggregate trust on the recommendation quality of the user-based trust-enhanced CF recommendation approach; (2) study and evaluate the impact of different fusion strategies on the recommendation quality of the fusion-based recommendation approach; (3) design and develop an ef<sup>fi</sup>cient method for updating and rebuilding the implicit trust social network. Once the implicit trust social network has been built, it will be dif<sup>fi</sup>cult to instantly re<sup>fl</sup>ect new information for user preferences. Updating the implicit trust social network has not regularly been considered because of the expensive computational time required for this process. Accordingly, an ef<sup>fi</sup>cient method of updating and rebuilding the implicit trust social network is required; and, (4) further extend our ‘BizSeeker’ system to incorporate the use of the proposed fusion-based recommendation approach in real-world practice for e-business applications.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transac tions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[2] A. Albadvi, M. Shahbazi, A hybrid recommendation technique based on product category attributes, Expert Systems with Applications 36 (9) (2009) 11480–11488

[3] S.S. Anand, B. Mobasher, Intelligent techniques for web personalization, in: B. Mobasher, S.S. Anand (Eds.), Intelligent Techniques for Web Personalization, Springer, Heidelberg, 2005, pp. 1–36.

[4] J. Bivainis, Development of business partner selection, Economics 73 (1) (2006) 7–18.

[5] J. Bobadilla, F. Ortega, A. Hernando, J. Alcala, Improving collaborative <sup>fi</sup>ltering rec ommender system results and performance using genetic algorithms, Knowledge Based Systems 24 (8) (2011) 1310–1316.

[6] L. Candillier, F. Meyer, F. Fessant, Designing speci<sup>fi</sup>c weighted similarity measures to improve collaborative <sup>fi</sup>ltering systems, in: P. Perner (Ed.), Advances in Data Mining. Medical Applications, E-Commerce, Marketing, and Theoretical Aspects Springer, Heidelberg, 2008, pp. 242–255.

[7] Y. Cho, J. Kim, Application of web usage mining and product taxonomy to collaborative recommendations in e-commerce, Expert Systems with Applications 26 (2) (2004) 233–246.

[8] O. Daramola, M. Adigun, C. Ayo, Building an ontology-based framework for tourism recommendation services, in: W. Höpken, U. Gretzel, R. Law (Eds.), Information and Communication Technologies in Tourism 2009, Springer-Verlag, Vienna, 2009, pp. 135–147.

[9] R. Gar<sup>fi</sup>nkel, R. Gopal, A. Tripathi, F. Yin, Design of a shopbot and recommender system for bundle purchases, Decision Support Systems 42 (3) (2006) 1974–1986.

[10] R. Gar<sup>fi</sup>nkel, R. Gopal, B. Pathak, F. Yin, Shopbot 2.0: integrating recommendations and promotions with comparison shopping, Decision Support Systems 46 (1) (2008) 61–69.

[11] J. Golbeck, Generating predictive movie recommendations from trust in social networks, in: K. Stølen, W. Winsborough, F. Martinelli, F. Massacci (Eds.), Trust Management, Springer, Heidelberg, 2006, pp. 93–104.

[12] X Guo. LLu Intelligent e-government services with personalized recommendation techniques, International Journal of Intelligent Systems 22 (5) (2007) 401–417.

[13] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Second Edition Morgan Kaufmann, San Francisco, 2006.

[14] J. Herlocker, J.A. Konstan, J. Riedl, An empirical analysis of design choices in neighborhood-based collaborative <sup>fi</sup>ltering algorithms, Information Retrieval 5 (4) (2002) 287–310.

[15] L. Hung, A personalized recommendation system based on product taxonomy for one-to-one marketing online, Expert Systems with Applications 29 (2) (2005) 383–392.

[16] C.-S. Hwang, Y.-P. Chen, Using trust in collaborative <sup>fi</sup>ltering recommendation, in: H. Okuno, M. Ali (Eds.), New Trends in Applied Arti<sup>fi</sup>cial Intelligence, Springer, Heidelberg, 2007, pp. 1052–1060.

[17] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (3) (2009) 470–479.

[18] D.-H. Kim, V. Atluri, M. Bieber, N. Adam, Y. Yesha, A clickstream-based collaborative <sup>fi</sup>ltering personalization model: towards a better performance, in: Proceedings of the 6th Annual ACM International Workshop on Web Information and Data Management, 2004, pp. 88–95.

[19] H.-N. Kim, A. El-Saddik, G.-S. Jo, Collaborative error-re<sup>fl</sup>ected models for cold-start recommender systems, Decision Support Systems 51 (3) (2011) 519–531.

[20] T.-P. Liang, Y.-F. Yang, D.-N. Chen, Y.-C. Ku, A semantic-expansion approach to personalized knowledge recommendation, Decision Support Systems 45 (3) (2008) 401–412.

[21] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative <sup>fi</sup>ltering, IEEE Internet Computing 7 (1) (2003) 76–80.

[22] J. Lu, Q. Shambour, Y. Xu, Q. Lin, G. Zhang, BizSeeker: a hybrid semantic recommendation system for personalized government-to-business e-services, Internet Research 20 (3) (2010) 342–365.

[23] J. Lu, Q. Shambour, Y. Xu, Q. Lin, G. Zhang, A web-based personalized business partner recommendation system using fuzzy semantic techniques, Computational Intelligence (in press), http://dx.doi.org/10.1111/j.1467-8640.2012.00427.x.

[24] J. Malinowski, T. Weitzel, T. Keim, Decision support for team staf<sup>fi</sup>ng: an automated relational recommendation approach, Decision Support Systems 45 (3) (2008) 429–447.

[25] M.L. Markus, Paradigm shifts — e-business and business/systems integration, Communications of the Association for Information Systems 4 (1) (2000) 1–45.

[26] P. Massa, P. Avesani, Trust-aware recommender systems, in: Proceedings of th 2007 ACM Conference on Recommender Systems, 2007, pp. 17–24.

[27] J. O'Donovan, B. Smyth, Trust in recommender systems, in: Proceedings of the 10th International Conference on Intelligent User Interfaces, 2005, pp. 167–174.

[28] M. Papagelis, D. Plexousakis, T. Kutsuras, Alleviating the sparsity problem of collaborative <sup>fi</sup>ltering using trust inferences, in: P. Herrmann, V. Issarny, S. Shiu (Eds.), Trust Management, Springer, Heidelberg, 2005, pp. 224–239.

[29] P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative <sup>fi</sup>ltering of netnews, in: Proceedings of the 1994 ACM Conference on Computer Supported Cooperative Work, 1994, pp. 175–186.

[30] P. Resnik, Using information content to evaluate semantic similarity in a taxonomy, in: Proceedings of the 14th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 1995, pp. 448–453.

[31] F. Ricci, L. Rokach, B. Shapira, P.B. Kantor, Recommender Systems Handbook, 1st ed. Springer, US, 2011.

[32] M. Richardson, R. Agrawal, P. Domingos, Trust management for the semantic web, in: D. Fensel, K. Sycara, J. Mylopoulos (Eds.), The Semantic Web, Springer, Heidel berg, 2003, pp. 351–368.

[33] R.M. Rodriguez, M. Espinilla, P.J. Sanchez, L. Martinez, Using linguistic incomplete preference relations to cold start recommendations, Internet Research 20 (3) (2010) 296–315.

[34] W. Rui-Qin, K. Fan-Sheng, Semantic-enhanced personalized recommender system, in: Proceedings of the International Conference on Machine Learning and Cybernetics, 2007, pp. 4069–4074.

[35] M. Ruiz-Montiel, J. Aldana-Montes, Semantically enhanced recommender systems, in: R. Meersman. P. Herrero. T. Dillon (Eds.). On the Move to Meaningful Internet Systems: OTM 2009 Workshops, Springer, Heidelberg, 2009, pp. 604–609.

[36] B. Sarwar, G. Karypis, J. Konstan, J. Reidl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, in: Proceedings of the 10th International Conference on WWW, 2001, pp. 285–295.

[37] J.B. Schafer, D. Frankowski, J. Herlocker, S. Sen, Collaborative <sup>fi</sup>ltering recommender systems, in: B. Peter, K. Alfred, N. Wolfgang (Eds.), The Adaptive Web: Methods and Strategies of Web Personalization, Springer, Heidelberg, 2007, pp. 291–324.

[38] Q. Shambour, J. Lu, Government-to-business personalized e-services using semantic-enhanced recommender system, in: K. Andersen, E. Francesconi, Å. Grönlund, T. van Engers (Eds.), EGOVIS 2011, LNCS, Springer, Heidelberg, 2011, pp. 197–211.

[39] Q. Shambour, J. Lu, A hybrid multi-criteria semantic-enhanced collaborative <sup>fi</sup>ltering approach for personalized recommendations, in: Proceedings of the 2011 IEEE/WIC/ACM International Conference on Web Intelligence (WI'11), 2011, pp. 71–78.

[40] Q. Shambour, J. Lu, A hybrid trust-enhanced collaborative <sup>fi</sup>ltering recommendation approach for personalized government-to-business e-services, International Journal of Intelligent Systems 26 (9) (2011) 814–843.

[41] Q. Shambour, J. Lu, Integrating multi-criteria collaborative <sup>fi</sup>ltering and trust <sup>fi</sup>ltering for personalized recommender systems, in: Proceedings of the 2011 IEEE Symposium on Computational Intelligence in Multicriteria Decision-Making (SSCL2011-MCDM 2011).2011, pp. 44–51

[42] U. Shardanand, P. Maes, Social information <sup>fi</sup>ltering: algorithms for automating 'word of mouth' in: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, 1995, pp. 210–217.

[43] P. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Pearson Inc., Boston, 2006.

[44] P. Victor, M. Cock, C. Cornelis, Trust and recommendations, in: F. Ricci, L. Rokach, B. Shapira, P.B. Kantor (Eds.), Recommender Systems Handbook, Springer, US, 2010, pp. 645–675.

[45] R.-Q. Wang, F.-S. Kong, Semantic-enhanced personalized recommender system, in: Proceedings of the International Conference on Machine Learning and Cybernetics, 2007, pp. 4069–4074.

[46] Y. Wang, W. Dai, Y. Yuan, Website browsing aid: a navigation graph-based rec ommendation system, Decision Support Systems 45 (3) (2008) 387–400.

[47] W. Yuan, L. Shu, H.C. Chao, D. Guan, Y.K. Lee, S. Lee, ITARS: trust-aware recommender system using implicit trust networks, IET Communications 4 (14) (2010) 1709–1721.

[48] L. Zhang, M. Zhu, W. Huang, A framework for an ontology-based e-commerce product information retrieval system, Journal of Computers 4 (6) (2009) 436–443.

[49] L. Zhen, G.Q. Huang, Z. Jiang, Recommender system based on work<sup>fl</sup>ow, Decision Support Systems 48 (1) (2009) 237–245.

Qusai Shambour has completed his Ph.D. in the School of Software, Faculty of Engineering and Information Technology, at the University of Technology Sydney (UTS)/Australia. He is a member of the Decision Systems and e-Service Intelligence Research Lab. His research interests include web personalization, recommender systems, collaborative <sup>fi</sup>ltering, e-service intelligence, and government-to-business personalized e-services

Professor Jie Lu is the Head of School of Software in the Faculty of Engineering and Information Technology, and the Director of the Decision Systems and e-Service Intelligence Research Laboratory in the Centre for Quantum Computation & Intelligent Systems at the University of Technology, Sydney (UTS). She received her PhD from the Curtin University of Technology in 2000. Her main research interests lie in the area of decision making modeling, decision support system tools, uncertain information processing, recommender systems and e-Government and e-Service intelligence. She has published <sup>fi</sup>ve research books and 270 papers in refereed journals and conference proceedings. She has won <sup>fi</sup>ve Australian Research Council (ARC) discovery grants. She received the <sup>fi</sup>rst UTS Research Excellent Medal for Teaching and Research Integration in 2010. She serves as Editor-In-Chief for Knowledge-Based Systems (Elsevier), and editor for book series on Intelligent Information Systems (World Scienti<sup>fi</sup>c).
