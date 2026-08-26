---
otero_id: 10016
otero_key: "H7MFFSMS"
title: "Who should you follow? Combining learning to rank with social influence for informative friend recommendation"
authors: "Chien Chin Chen; Shun-Yuan Shih; Meng Lee"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.06.017"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Who should you follow? Combining learning to rank with social influence for informative friend recommendation

Chien Chin Chen ⁎, Shun-Yuan Shih, Meng Lee

Department of Information Management, National Taiwan University, Taiwan

a r t i c l e i n f o

Article history: Received 30 July 2015 Received in revised form 21 June 2016 Accepted 22 June 2016 Available online xxxx

Keywords: Recommendation systems Learning to rank Social influence Matrix factorization

## a b s t r a c t

Social network sites have gradually taken the place of traditional media for people to receive the latest information. To receive novel information, users of social network sites are encouraged to establish social relations. The updates shared by friends form social update streams that provide people with up-to-date information. However, having too many friends can lead to an information overload problem causing users to be overwhelmed by the huge number of updates shared continuously by numerous friends. This information overload problem may affect user intentions to join social network sites and thereby possibly reduce the sites' advertising earnings, which are based on the number of users. In this paper, we propose a learning-based recommendation method which suggests informative friends to users, where an informative friend is a friend whose posted updates are liked by the user. Techniques of learning to rank are designed to analyze user behavior and to model the latent preferences of users and updates. At the same time, the learning model is incorporated with social influence to enhance the learned preferences. Informative friends are recommended if the preferences of the updates that they share are highly associated with the preferences of a target user.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

The prevalence of social media has advanced the way people exchange information. Nowadays, users can gather various kinds of information from social media that allow the creation and exchange of user-generated content for a variety of purposes ranging from entertainment to learning and shopping. Among all social media, social network sites such as Facebook have become increasingly popular, with estimates of over 60% of adults in the US<sup>1</sup> having more than one social network site account. The most popular social network site worldwide is Facebook, which as of 2014 had 1393 million active users.<sup>2</sup> There is a great deal of evidence showing that social network sites are ubiquitous and have become a part of our daily life.

Users on social network sites exchange information by sharing updates using posts, photos, or videos. These updates form social update streams, which are sets of chronologically ordered updates shared by users' friends [15]. When users share an update, the update will instantaneously appear in their friends' social update streams, which enable users to get the latest information. It has been asserted that Internet users heavily rely on social update streams to seek information and thus are willing to notify and be notified by their friends of important information [33]. As a result, social update streams accelerate the spread of information among social circles. By taking advantage of efficient information delivery, social update streams have successfully played a role in word-of-mouth marketing and event detection. For example, Twitter is regarded as an ideal place to provide a highly interactive one-to-many information channel, which is why organizations like Microsoft US, Coca-Cola, etc., use a combination of retweets, hashtags, and hyperlinks to promote marketing messages, and even to respond to customers' complaints either made directly to organizations or discovered by monitoring the social update streams [12]. Li et al. [24], who conducted a real-time analysis of the updates on Twitter, demonstrated that temporal and spatial patterns on social update streams generally coincide with emergent accidents (e.g., earthquake or tsunami); in this way, social update streams can be an important source information for national surveillance. Due to their varied functionalities and efficient delivery, social update streams have gradually taken the place of traditional media and are becoming an important mechanism of information dissemination [4,22].

Social network site users need to establish friendships to receive updates. However, when the quantity of friends reaches a fairly high level, users can be overwhelmed by the amount of fresh social updates. The thousands of social updates from hundreds of friends per day may be seen as a kind of spam in the social update streams. This so-called information overload problem [21] may subsequently lead to a degraded user experience which in turn may affect user intention to join or remain a member of social network sites. Since a major source of income for social network sites comes from advertising based on the number of site users [11], the information overload problem may affect the revenues of the sites.

From a decision support perspective, recommendation systems are supporting tools that analyze users' behavior to suggest items relevant to their preferences [17]. The personalized recommendation is essential to substantially reduce information overload and has been shown effective to increase users' satisfaction and loyalty to e-services [25]. Therefore, in order to resolve the information overload problem of social update streams and to create a win–win proposition for both social network site users and owners, effective friend recommendation methods which suggest informative friends to users are critical [50], where an informative friend is a friend whose posted updates are relevant to the preferences of the user. Recommending informative friends not only enriches the content of social update streams but also helps social network sites retain users to increase potential advertising revenues.

In recent years, more and more studies have started to investigate friend recommendation for social network sites. A great proportion of friend recommendation methods are comparable to the link prediction of social networks [16], which analyzes the structures of social networks (e.g., friends of friends) to predict potential links (i.e., friendships) between users. Other methods adopt recommendation system techniques to compute the similarity between users in terms of user-generated content and friend lists. Preference-similar users are recommended to a target user [44]. Although the two approaches enable expansion of users' social circles, they could intensify the information overload problem because the informativeness of the suggested friends is neglected. In this paper, we thus study the informative friend recommendation problem. We design a model-based friend recommendation method which employs learning to rank [29] to recommend informative friends to users. Recent recommendation studies [9,44] advocate learning to rank to incorporate users' implicit feedback with the recommendation algorithms. Instead of measuring the preference degree (e.g., rating) of an item, learning to rank utilizes the implicit feedback to train a ranking model which discriminates preferences between items. In the proposed method, we consider social updates as items and integrate techniques of matrix factorization with learning to rank in order to learn the latent preferences of users and updates. At the same time, as users are more likely to receive and respond to updates their friends are interested in, social influence (the association of friends and their preferences) is incorporated to derive representative latent preferences. Thereafter, informative friends are recommended if the preferences of the updates they share are highly associated with the preferences of a target user. To examine the proposed method, we adopted a real-world dataset consisting of thousands of updates and users. The experiment results based on this large dataset demonstrate the effectiveness of the proposed method in recommending informative friends; further, the updates shared by the recommended friends were highly associated with user preferences. The proposed method thus outperforms many well-known friend recommendation methods and learning to rank recommendation methods.

The remainder of this paper is organized as follows. The next section contains a review of related works on recommendation systems and friend recommendation. We introduce the proposed friend recommendation method in Section 3, and then evaluate it in Section 4. Section 5 provides discussions and implications, and some concluding remarks and future avenues of research are given in Section 6.

## 2. Related works

In this section, we first review a number of recommendation systems and their applications on learning to rank. Next, we consider social influence and introduce their techniques used in friend recommendation.

## 2.1. Collaborative filtering on recommendation systems

The goal of recommendation systems is to suggest items relevant to user preferences. The most widely used recommendation approach is collaborative filtering [6,40] which assumes that like-minded people prefer similar items and thus analyzes user behavior (e.g., ratings) on items to identify reference users whose preferences are similar to those of a target user. Items that interest the reference users then are recommended to the target user. Methods of collaborative filtering can be classified as either memory-based or model-based. Normally, memory-based methods record all the ratings made by users. The ratings are regarded as explicit user preferences and are analyzed by a similarity metric to find out reference users. For instance, Resnick et al. [40] employed the Pearson correlation coefficient to select positively correlated users as the reference users; and Linden et al. [28] utilized cosine similarity, which is the normalized inner product of users' rating vectors, to measure the similarity between users. How ever, a major concern with the memory-based methods is the sparsity of ratings [7] in that users generally rate few items. Consequently, the explicit preferences are too sparse to infer effective reference users. To remedy the sparsity problem, model-based methods analyze users ratings to model users' latent (implicit) preferences. One of the most popular model-based methods is matrix factorization whose goal is to represent the latent preferences of users and items as Z dimensional preference vectors that approximate the user–item rating matrix. Matrix factorization maps both users and items to a joint latent factor space such that user–item behavior can be represented as inner prod ucts in the space. It is worth mentioning that model-based collaborative filtering has become a major recommendation methodology due to its superior performance in several recommendation contests, such as the Netflix Prize competition and KDDCUP [5,20]. Sarwar et al. [42] applied the singular value decomposition (SVD) [47] to the user–item rating matrix. The authors demonstrated that the decomposed singular vectors successfully represent the latent preferences of users and are capable of discovering reliable reference users for effective item recom mendations. Paterek [36] developed an effective model-based recom mendation method, which achieved a remarkable performance in the Netflix prize competition, by enhancing the SVD recommendation method with a memory-based technique; he also introduced bias variables to decrease the root mean square error of the predicted rating and to increase the accuracy of item recommendations. Koren [19] merged the ratings predicted by an SVD-based method and a memory-based method, and thus formulated a neighborhood model which optimizes a cost function that integrates the latent preferences of users and their neighborhoods. As the SVD-based method and the memory-based method addressed item recommendation from different perspectives, their combination complemented each other and thus significantly improved recommendation accuracy. Recently, Koren et al. [20] conducted a thorough analysis of matrix factorization techniques and formulated matrix factorization as an optimization problem, thereby introducing a gradient descent-based learning algorithm to rapidly approximate adequate preference vectors by minimizing the root mean square error between the actual item ratings and the ratings predicted by the preference vectors. This method achieved remarkable performances on many recommendation datasets and is currently the state-of-the-art matrix factorization method.

## 2.2. Learning to rank on recommendation systems

Methods of matrix factorization-based collaborative filtering have normally formulated the preference approximation as an optimization problem whose goal is to predict item ratings as accurately as possible. However, it would be more appropriate to model the approximation task as a ranking problem because the essential of recommendation is to rank items according to user preferences [37]. Recently, a novel machine learning technique called learning to rank [29], which has demonstrated impressive performance in many research fields such as in information retrieval, has attracted considerable attention from recommendation system researchers. Technically, methods that employ machine learning techniques to solve ranking problems are referred to as learning to rank. With regard to recommendation systems, learning to rank analyzes users' feedback on items to discriminate preferences between items. For instance, Rendle et al. [39] formulated a Bayesian optimization criterion which approximates the likelihood (probability) that a user prefers an item i over an item j. Then, a stochastic gradient descent algorithm was developed to optimize the ranking likelihood. This ranking criterion successfully improved the recommendation performance of various matrix factorization and memory-based methods. Shi et al. [45] developed an efficient learning to rank method for effective collaborative filtering. Instead of measuring the precedence of items in a pair, the authors designed a matrix factorization method which optimizes the precedence of items in a list. Chen et al. [9] assumed that the tweets retweeted by users have a high precedence and developed a pairwised learning model to learn the precedence of tweets over users. The experiment results demonstrated that the model was effective in recommending useful tweets for users.

## 2.3. Social influence on recommendation systems

Social influence is another useful recommendation technique since the decisions of users are generally influenced by friends or trusted people [10,32,53,54,56]. In terms of recommendation systems, social influence aims to leverage the social relationships between users as well as their past behavior for improving preference learning. Many recommendation methods aggregate the preferences of friends to recommend interesting items to users. For instance, Ma et al. [31] presented a probabilistic matrix factorization method which incorporates social (trust) networks of users into the user–item rating matrix. They developed a weighted average scheme which adjusts the preferences of a user according to the preferences of the trusted users. The authors validated that the social information is effective in item recommendation especially when the rating matrix is sparse, i.e., when few item ratings are given. Shen and Jin [43] argued that although users might have few common interests, most social recommendation systems measure the overall preference similarity between users and their friends. The authors therefore developed a mixture membership stochastic model to discover the partial preferences of users, which further characterize users' distinct social interests and enhance social recommendations. Yang et al. [53] thoroughly examined the effect of social influence on recommendation systems, and obtained experiment results that demonstrate that trust and social information siginificantly improved the performace of recommendation systems. Furthermore, matrix factorization models perform better when combining feedback data with social information.

## 2.4. Friend recommendation using link prediction

The existing friend recommendation methods are mainly classified into two categories. One is based on link prediction which analyzes social network structures to suggest friends to users; and the other employs recommendation system techniques, like collaborative filtering and matrix factorization, to make friend recommendations. Basically, link prediction examines a network to predict the presence of links or connections between entities (nodes) [41]. It is applicable to many real-world domains to enhance various information systems. Taking citation analysis as an example, methods of link prediction analyze a citation graph where nodes represent research articles and links depict their citation relations to recommend meaningful citations to an article [38]. Friend recommendation is often formulated as an instance of link prediction that was first introduced by Liben-Nowell and Kleinberg [27]. Given a social network in which nodes represent people (or entities) and edges depict friendships, link prediction examines structural aspects to infer social ties. Liben-Nowell and Kleinberg, for example, examined node neighborhoods, the ensemble of all paths in a network, and unsupervised clustering approaches for link prediction. The prediction task, however, is so difficult that the best prediction accuracy reported in their study was merely 16%. Leskovec et al. [23], assuming that social networks involve positive (friendly) and negative (opposing) relationships, employed a logistic regression model to predict positive and negative links in online social networks. The authors incorporated balance theories from social psychology into their prediction model and showed that negative links are useful in predicting positive relationships. Hopcroft et al. [16] investigated the formation of reciprocal relationships on Twitter. They examined factors of geographic distances, homophily of users, implicit networks, and social balance theories to predict the “follow backs” among Twitter users. Their experiments revealed the effects of the aforementioned factors, and they concluded that users usually make follow back decisions within 10 days. Zhang et al. [55] studied the multi-network link prediction problem which focuses on the formation of social links across differnt aligned networks, such as friendship networks and location checkin networks. The authors explored the social meta path, which is the weighted path that connects two nodes in different networks, and their experiment results demonstrate that heterogeneous features extracted from both intra- and inter-social meta paths significantly enhance the link prediction.

## 2.5. Friend recommendation using recommendation system techniques

Recently, a number of studies have started to employ recommendation system techniques to suggest friends to social network site users. For instance, Hannon et al. [14] represented users by the updates they posted. The authors supposed that friends have similar preferences and as a result recommended friends whose posts are similar to those posted by the target user. Moreover, Shi et al. [44] transformed the mean reciprocal rank, a well-known metric used to evaluate the ranking quality of the recommended items, into a continuous objective function. A learning model which combines matrix factorization and learning to rank was developed to maximize the objective function and to recommend friends to users. The proposed CLiMF method treats a friend as an item and models user-friend relationships by means of a user–item matrix. Then, a pairwise learning to rank algorithm is employed to extract the preferences of users from the matrix. Again, users whose preferences are similar to that of a target user are recommended. Liao et al. [26] developed a classification-based friend recommendation method for virtual worlds, and found that, in general, users in virtual worlds join different activities and friendships exist if users tend to join similar types of activities (e.g., chatting, joining bidding, or playing games). The friend recommendation method thus characterizes users' contact activities into features and constructs a classification model based on the features to predict friendships.

While the friend recommendations using link prediction or recommendation system techniques are applicable to expand users' social circles, the methods could exacerbate the information overload of social update streams. This is because the methods simply recommend realworld friends or friends with similar preferences that overlook the friends' informativeness. It has been asserted that the information overload of social update streams is becoming so severe that social network site users are increasingly becoming annoyed by the huge amount of informationless social update streams. Also, given that users' perceived utility affects their loyalty to e-services [30], the information overload caused by friend recommendations could reduce a social network site's popularity and advertising earnings. It is therefore worth investigating informative friend recommendation.

To fill the research gap of limited friend recommendation methods in light of the information overload of social update streams, we

investigated the informative friend recommendation problem. Informative friend recommendation is a new research paradigm that has not yet been well addressed in prior research. To the best of our knowledge, only Wan et al. [50] studied this research topic. While the research work explored matrix factorization techniques to recommend friends informative to a target user, the method does not take into account social influence, which is a key element of social recommendation [10, 32,53,54,56]. In this paper, we employ techniques of matrix factorization and learning to rank to extract preferences of updates that are refined by an adaptive social influence mechanism. Users whose updates are useful (informative) to a target user are deemed as informative friends and are recommended.

## 3. Informative friend recommendation using social update streams

Fig. 1 depicts our model-based friend recommendation method consisting of two major components: preference learning and informative friendship computation. In the preference learning stage, implicit user feedback, such as replies or likes, on social updates is collected. The feedback are fed into a pairwise learning to rank model to learn two types of preferences that affect the precedence of an update in a pair. One relates to users reading preferences and the other to the updates' sharing preferences. Furthermore, the social influence between users is incorporated into the learning model to enhance the learned preferences. In the informative friendship computation stage, informative friends are recommended. Thi is achieved by first constructing a user's sharing preferences by aggregating the preferences of the updates shared by the user. After this, the similar ities between users' reading and sharing preferences are computed and users are classified as informative friends if their sharing preferences are highly associated (similar) with the reading preferences of a target user. We discuss each component in detail in the following sub-sections

## 3.1. Preference learning

Our preference learning incorporates techniques of learning to rank and social influence into the latent factor model which has been shown to be effective in many recommendation scenarios [15]. The latent factor model, also known as matrix factorization, decomposes a user–item matrix to discover the preferences (latent factors) of users and items. In our method, let $U = \{ u _ { 1 } , u _ { 2 } , . . . , u _ { M } \}$ be a set of users on a social network site and let items $V = \{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { N } \}$ be the updates shared by U. The user–item matrix R is an $M \times N$ matrix where the entry $r _ { i j }$ is 1 if user u has provided a feedback (e.g., like or reply) on update v ; otherwise, it is 0. The goal of matrix factorization is to search for matrices P and Q such that

$$
r _ {i j} \approx \hat {r} _ {i j} = c _ {i} + b _ {j} + \underline {{p}} _ {i} ^ {T} \underline {{q}} _ {j},\tag{1}
$$

where $\hat { r } _ { i j }$ represents the estimation of $r _ { i j } ,$ p and $g _ { j }$ are the ith and jth columns of P and $Q _ { ☉ }$ respectively. The matrix P is a $Z \times M$ matrix where each column p $\in \mathbb { R } ^ { Z }$ represents u 's reading preference vector and the dimension of the preferences is Z. Similarly, Q is $1 Z \times N$ matrix where each column $q _ { j } \in \mathbb { R } ^ { Z }$ is v 's sharing preference vector; c and $b _ { j }$ are bias variables in that c is the average $r _ { i j }$ made by $u _ { i }$ subtracted by the average $r _ { i j }$ made by all users

![](/api/attachments/H7MFFSMS/fulltext/images/e4de9846a2009bbbf644e567fb895885aa86b75931fcc3afb01534bc14303f98.jpg)  
Fig. 1. The system structure.

Please cite this article as: C.C. Chen, et al., Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.017

and b<sub>j</sub> is the average r<sub>ij</sub> received by v<sub>j</sub> subtracted by the average r<sub>ij</sub> received by all updates. These variables denote the user and item biases associated with u and v against the global average and they account for the user and item effects [20]; including these variables allows the learned P and Q to deviate from the biases and thus makes P and Q focused on user and update preferences.

Since the preferences of users will be affected by those of their friends [32,43,53,54], we therefore modify the definition of $\hat { r } _ { i j }$ by incorporating the social influence as follows:

$$
\hat {r} _ {i j} = c _ {i} + b _ {j} + (1 - \alpha_ {i}) \underline {{p}} _ {i} ^ {T} \underline {{q}} _ {j} + \alpha_ {i} \sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{p}} _ {g} ^ {T} \underline {{q}} _ {j},\tag{2}
$$

where $F ( u _ { i } )$ denotes the set of $u _ { i } ^ { \prime } s$ friends and $s _ { i \mathrm { g } }$ stands for $u _ { g } ^ { \prime } s$ influence degree for $u _ { i } .$ We adopted Ma et al.'s social measure [31] which computes the association of users in a social network as follows:

$$
S _ {i g} = \sqrt {\left. ^ {d _ {g} ^ {-}} \right/ _ {(d _ {g} ^ {-} + d _ {i} ^ {+})}} \Bigg / \sum_ {u _ {l} \in F (u _ {i})} \sqrt {\left. ^ {d _ {l} ^ {-}} \right/ _ {(d _ {l} ^ {-} + d _ {i} ^ {+})}},\tag{3}
$$

where $d _ { i } ^ { + }$ indicates the out-degree $( \mathrm { i . e . } ,$ , the number of friends) of $u _ { i }$ and $d _ { \mathrm { g } } ^ { - }$ is the in-degree of $u _ { g }$ in the social network; the denominator is a normalization factor that makes $s _ { i \mathrm { g } }$ range from 0 to 1. Specifically, the influence value $s _ { i \mathrm { g } }$ decreases if $u _ { i }$ makes a lot of friends; however, $s _ { i \mathrm { g } }$ increases if $u _ { g }$ is followed by a lot of users, i.e., if $u _ { g }$ is a popular and influential user; as such, $u _ { g } ^ { \prime } s$ opinions are likely to affect $u _ { i } .$ The last term of Eq. (2) denotes the social in uence weighted by $\alpha _ { i } .$ Here, we present two strategies to determine the value of $\alpha _ { i } .$ One is the xed social in uence strategy which sets $\alpha _ { i }$ as a fixed value. The other is the adaptive social influence strategy in which α is adaptive to the social degree of $u _ { i } .$

$$
\alpha_ {i} = 1 - ^ {1} \big / _ {(d _ {i} ^ {+} / s r) + 1},\tag{4}
$$

where sr is a social regularization parameter. Fig. 2 shows the curve of α against the size of $d _ { i } ^ { + }$ . Basically, the curve approximates the sigmoid function [13] ranging from 0 to 1. An important property of α is that it grows as the number of u 's friends increases. The property is based on [48] in that users are prone to be subjected to friends' opinions if they have a lot of friends. Also note that the growth curve eases up once the number of friends reaches a fairly high level. In the experiment section, we will examine the social regularization parameter and the effect of the social influence strategies.

Given the user–item matrix R, methods of the latent factor model are used to search for P and Q that minimize the root mean square between $r _ { i j }$ and $\hat { r } _ { i j } .$ More recently, recommendation research has started to advocate learning to rank, which strives to identify the P and Q that characterize the precedence $( \mathrm { i . e . } ,$ , relative ordering) of items, instead of minimizing the root mean square error. As the goal of recommendation systems is to rank items according to user preferences, learning to rank closely corresponds with this goal and has been investigated in many recommendation studies [15,44]. We adopted the pairwise learning to rank [29] that models the precedence of updates in terms of update pairs. In general, items with user feedback have a higher precedence (preference) than those with no feedback [9]. Here, we assume that updates liked or replied to by users have a high precedence. Based on this, we constructed a set of training update pairs $D _ { i } = \{ < \nu _ { x } , \nu _ { y } > | \nu _ { x } \in V , \nu _ { y } \in V , r _ { i x } > r _ { i y } \}$ for a user $u _ { i }$ and computed the sum of the logistic loss, which is the core of our preference learning, as follows:

$$
\sum_ {i = 1} ^ {M} \sum_ {<   v _ {x}, v _ {y} > \in D _ {i}} \ln \left(1 + e ^ {- \left(\hat {r} _ {i x} - \hat {r} _ {i y}\right)}\right),\tag{5}
$$

where the variables $\hat { r } _ { i x }$ and $\hat { r } _ { i y }$ are derived from the preference matrices P and Q (see Eq. (2)), and they stand for the estimation of $r _ { i x }$ and $r _ { i y } ,$ respectively. The term ln $( 1 + e ^ { - ( \hat { r } _ { i x } - \hat { r } _ { i y } ) } )$ computes the logistic loss of P and Q on a training update pair $< \nu _ { x } , \nu _ { \mathrm { y } } >$ in $D _ { i } .$ As mentioned above, the goal of our preference learning is to find P and O that preserve the precedence of updates. To reach this goal, when constructing training data $D _ { i }$ we require $r _ { i x } > r _ { i y }$ . In other words, each training update pair ${ < } v _ { x } , v _ { y } { > }$ conveys a high precedence of item $\nu _ { x }$ over item $\nu _ { y } .$ . As shown in Fig. 3, when $\hat { r } _ { i x } = \hat { r } _ { i y } ,$ the logistic loss will be larger than that of $\hat { r } _ { i x } > \hat { r } _ { i y }$ , and it will also be the case that $\hat { r } _ { i x } < \hat { r } _ { i y }$ . However, the two cases $( \mathrm { i } . \mathrm { e } . , \hat { r } _ { i x } = \hat { r } _ { i y }$ and $\hat { r } _ { i x } { < } \hat { r } _ { i y } )$ imply the learned P and Q cannot differentiate the precedence in the training update pair (i.e., the $\hat { r } _ { i x }$ and $\hat { r } _ { i y }$ estimated by P and Q cannot

![](/api/attachments/H7MFFSMS/fulltext/images/ade09cec530ce5cfff2f713daadd0bca8e9c09a4949f12c8d06eb95f4607ac2b.jpg)  
Fig. 2. The growth of against the number of friends.

Please cite this article as: C.C. Chen, et al., Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.017

C.C. Chen et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/H7MFFSMS/fulltext/images/603a6244800e693b38c94ff4b43e773841d99c64da88b978eb3b6ca2c98204c9.jpg)  
Fig. 3. The curve of logistic loss.

reflect the fact that $r _ { i x } > r _ { i y } )$ . We therefore penalize the cases by assigning them a large logistic loss value. By minimizing the sum of the logistic loss on all training update pairs over all users, the appropriate P and Q can be acquired.

By substituting $\hat { r } _ { i x }$ and $\hat { r } _ { i y }$ with Eq. (2), the goal of our preference learning is to find the P and Q that minimize the following loss function F.

$$
\begin{array}{l} F (P, Q) = \sum_ {i = 1} ^ {M} \sum_ {<   v _ {x}, v _ {y} > \in D _ {i}} \ln \left(1 + e ^ {- \left(\hat {r} _ {i x} - \hat {r} _ {i y}\right)}\right) + \lambda \Big (\| P \| ^ {2} + \| Q \| ^ {2} \Big) \\ = \sum_ {i = 1} ^ {M} \sum_ {<   v _ {x}, v _ {y} > \in D _ {i}} \ln \left(1 + e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(p _ {i} ^ {T} \underline {{q}} _ {x} - p _ {i} ^ {T} q _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (u _ {i})} s _ {\mathrm{ig}} \underline {{p}} _ {g} ^ {T} q _ {x} - \sum_ {u _ {g} \in F (u _ {i})} s _ {\mathrm{ig}} \underline {{p}} _ {g} ^ {T} q _ {y}\right)\right)}\right) + \lambda \Big (\| P \| ^ {2} + \| Q \| ^ {2} \Big), \end{array}\tag{6}
$$

where the first term is the sum of the logistic loss over all users; $\| P \| ^ { 2 }$ and $\| Q \| ^ { 2 }$ are regularization terms that prevent the overfitting of the learned P and Q, and λ is the corresponding regularization coefficient. We adopted the stochastic gradient descent [34] to search for adequate preference vectors. Speci cally, the stochastic gradient descent rst randomly initiates P and Q. Then, ${ \underline { { p } } } _ { i } , q _ { x } ,$ and $g _ { y }$ are iteratively re ned by using their derivatives upon F defined below until F reaches a local minimum. Fig. 4 illustrates the stochastic gradient descent algorithm.

$$
\left. \partial_ {F} / _ {\partial \underline {{{p}}} _ {i}} = - \frac {e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(\underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {x} - \underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{{p}}} _ {g} ^ {T} \underline {{{q}}} _ {x} - \sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{{p}}} _ {g} ^ {T} \underline {{{q}}} _ {y}\right)\right)} \times (1 - \alpha_ {i}) \times \left(\underline {{{q}}} _ {x} - \underline {{{q}}} _ {y}\right)}{\left(1 + e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(\underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {x} - \underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (\mathrm{u} _ {i})} s _ {i g} \underline {{{p}}} _ {g} ^ {T} \underline {{{q}}} _ {x} - \sum_ {u _ {g} \in F (\mathrm{u} _ {i})} s _ {i g} \underline {{{p}}} _ {g} ^ {T} \underline {{{q}}} _ {y}\right)\right)}\right)}\right) + 2 \lambda p _ {i}\tag{7}
$$

$$
\left. \right. \partial_ {F} / _ {\partial \underline {{q}} _ {x}} = - \frac {e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(\underline {{p}} _ {i} ^ {T} \underline {{q}} _ {x} - \underline {{p}} _ {i} ^ {T} \underline {{q}} _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{p}} _ {g} ^ {T} q _ {x} - \sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{p}} _ {g} ^ {T} q _ {y}\right)\right)} \times \left((1 - \alpha_ {i}) \underline {{p}} _ {i} + \alpha_ {i} \sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{p}} _ {g}\right)}{\left(1 + e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(\underline {{p}} _ {i} ^ {T} \underline {{q}} _ {x} - \underline {{p}} _ {i} ^ {T} \underline {{q}} _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (\mathrm{u} _ {i})} s _ {i g} \underline {{p}} _ {g} ^ {T} q _ {x} - \sum_ {u _ {g} \in F (\mathrm{u} _ {i})} s _ {i g} \underline {{p}} _ {g} ^ {T} q _ {y}\right)\right)}\right)} + 2 \lambda \underline {{q}} _ {x}\tag{8}
$$

$$
\left. \right. \partial_ {F} / _ {\partial \underline {{{q}}} _ {y}} = - \frac {e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(\underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {x} - \underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{{p}}} _ {g} ^ {T} \underline {{{q}}} _ {x} - \sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{{p}}} _ {g} ^ {T} \underline {{{q}}} _ {y}\right)\right)} \times \left(- (1 - \alpha_ {i}) \underline {{{p}}} _ {i} - \alpha_ {i} \sum_ {u _ {g} \in F (u _ {i})} s _ {i g} \underline {{{p}}} _ {g}\right)}{\left(1 + e ^ {- \left(b _ {x} - b _ {y} + (1 - \alpha_ {i}) \times \left(\underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {x} - \underline {{{p}}} _ {i} ^ {T} \underline {{{q}}} _ {y}\right) + \alpha_ {i} \times \left(\sum_ {u _ {g} \in F (\bar {u} _ {i})} s _ {i g} \underline {{{p}}} _ {\bar {g}} ^ {T} \underline {{{q}}} _ {x} - \sum_ {u _ {g} \in F (\bar {u} _ {i})} s _ {i g} \underline {{{p}}} _ {\bar {g}} ^ {T} \underline {{{q}}} _ {y}\right)\right)}\right)} + 2 \lambda \underline {{{q}}} _ {y}\tag{9}
$$

Please cite this article as: C.C. Chen, et al., Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.017

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Preference Learning
Input: The user-item matrix R with M users and N items (updates), learning rate  $\gamma$ , dimension of preferences Z.
Output: The learned preference vectors P, Q.
t = 0 // t is the iteration count
Initialize  $P^{t}$  and  $Q^{t}$  with random values.
while  $(P^{t} \neq P^{t-1} \&amp;\&amp; Q^{t} \neq Q^{t-1})$  do
    for i = 1, 2, ..., M do
    construct a set of precedence update pairs  $D_{i} = \{&lt;v_{x}, v_{y}&gt; | v_{x} \in V, v_{y} \in V, r_{ix}&gt; r_{iy}\}$  for a user  $u_{i}$ 
    for  $&lt;v_{x}, v_{y}&gt; \in D_{i}$  do
    $\triangle p_{i}^{t} = \delta F / \delta p_{i}^{t}$  based on Eq. (7)
    $\triangle q_{x}^{t} = \delta F / \delta q_{x}^{t}$  based on Eq. (8)
    $\triangle q_{y}^{t} = \delta F / \delta q_{y}^{t}$  based on Eq. (9)
    for z = 1, 2, ..., Z do
    $p_{i}^{t+1}_{z} = p_{i}^{t}_{z} - \gamma * \triangle p_{i}^{t}_{z};$ $q_{x}^{t+1}_{z} = q_{x}^{t}_{z} - \gamma * \triangle q_{x}^{t}_{z};$ $q_{y}^{t+1}_{z} = q_{y}^{t}_{z} - \gamma * \triangle q_{x}^{t}_{z};$ 
    end
    end
    end
    end
    end
    end
return  $P = P^{t}, Q = Q^{t}$
</div>

Fig. 4. The stochastic gradient descent for preference learning.

Here, we analyze the time complexity of our preference learning. The core of the algorithm is the set of the derivatives (i.e., Eqs. (7), (8), and (9)) which compute the inner products of the preference vectors against users and updates. As the dimension of the vectors is Z, the time complexity of the inner product is O(Z). Also, the derivatives aggregate the friends' inner products against an update pair, Their complexity is thus O(MZ) where M is the number of users. The time complexity of the preference refinement for each training update pair $< \nu _ { x } , \nu _ { y } > \mathrm { i } s 0 ( M Z )$ and the complexity of constructing the set of training update pairs $D _ { i }$ is $\mathsf { O } ( N ^ { 2 } )$ where N denotes the number of updates. Let T denote the iteration number of stochastic gradient descent, and the time complexity of the preference learning algorithm is $0 ( T M ^ { 2 } N ^ { 2 } Z )$

## 3.2. Informative friendship computation

Once matrices P and $Q$ are converged, we constructed the sharing preference vector $\underline { { h } } _ { j }$ of user $u _ { j }$ by aggregating all the sharing preference vectors of the updates shared by $u _ { j } .$

$$
\underline {{{h}}} _ {j} = \frac {\sum_ {v _ {n} \in s (u _ {j})} \underline {{{q}}} _ {n}}{\left| \sum_ {v _ {n} \in s (u _ {j})} \underline {{{q}}} _ {n} \right|},\tag{10}
$$

where $S ( u _ { j } )$ denotes the set of updates shared by $u _ { j } ,$ and ${ \underline { { q _ { n } } } }$ is the sharing preference vector of update $\nu _ { n } .$ The denominator of $\operatorname { E q . }$ (10) is a normalization factor, which makes the sharing preference vector $\underline { { h _ { j } } }$ a length-normalized vector. For a target user $u _ { i } , i$ a user $u _ { j }$ is deemed an informative friend if $\boldsymbol { u } _ { j } ^ { \prime } \boldsymbol { s }$ sharing preferences are highly similar to the reading preferences of $u _ { i } .$ We adopted the cosine metric to measure the preference similarity between u and $u _ { j }$ as follows:

$$
\operatorname{sim} \left(u _ {i}, u _ {j}\right) = \operatorname{cosine} \left(\underline {{{p}}} _ {i}, \underline {{{h}}} _ {j}\right) = \frac {\underline {{{p}}} _ {i} \cdot \underline {{{h}}} _ {j}}{| \underline {{{p}}} _ {i} | | \underline {{{h}}} _ {j} |}.\tag{11}
$$

The range of $s i m ( u _ { i } , u _ { j } )$ is within [0,1], with a higher value indicating a greater similarity of the preferences of $u _ { i }$ and $u _ { j } .$ Finally, we ranked users according to their cosine values and the top-ranked users are suggested as the informative friends.

Please cite this article as: C.C. Chen, et al., Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.017

Table 1 Statistics of the evaluation datasets.

<table><tr><td></td><td>Data200</td><td>Data300</td></tr><tr><td>Number of users</td><td>5145</td><td>1565</td></tr><tr><td>Number of weibos</td><td>150,117</td><td>50,003</td></tr><tr><td>Number of social links</td><td>106,023</td><td>25.424</td></tr><tr><td>Number of user feedback (replied or liked records)</td><td>60,670</td><td>22.708</td></tr><tr><td>Average feedback per user</td><td>11.79</td><td>14.51</td></tr></table>

## 4. Experiment

## 4.1. Datasets and evaluation metrics

To evaluate the proposed method, we conducted experiments using the Weibo dataset from the WISE 2012 Challenge.<sup>3</sup> Weibo<sup>4</sup> is the most popular social network site in China and its users share their updates by posting weibos, i.e., short messages. There are also follower–followee friendships between users that form a directed social network. Since the functions of Weibo are similar to those provided by Twitter, it has been labeled the Chinese Twitter in East Asian social circles. The Weibo dataset consists of 58,655,849 users and 366,946,149 updates, and is so big that it has been frequently used as a benchmark for big data analytics [2,3,35]. However, we noticed that the dataset consists of a lot of inactive users who have few social relationships and social interactions. Insofar as Pan et al. [35] regard inactive users as noisy users, to reduce their influence on system performance and to simulate the scenario of information overload, we evaluated the recommendation performance on two subsets of the data. One (denoted as Data200) filters out the users with fewer than 200 followees and the other (denoted as Data300) excludes the users with fewer than 300 followees. Table 1 summarizes the experiment data. Obviously, the experiment users in Data300 have more social relationships and interactions (i.e., average feedback per user) than those in Data200. Comparing system performance under Data200 and Data300 thus enables us to examine the robustness of our method.

In [50], the users whose shared updates had been previously responded to (replied to or liked) by a target user were considered to be informative users. An informative friend recommendation method was deemed effective if it was able to rank the informative users more highly in the generated friend recommendation list. Based on this, we adopted the conventional leave-one-out procedure [7] to evaluate our informative friend recommendation method. Specifically, for each user $u _ { i }$ in the evaluation datasets, we evaluated the recommendation performance over multiple runs. Each run selected an informative user $u _ { j }$ of $u _ { i }$ for testing. Then, the preferences of users and updates were learned in an unbiased manner by deleting all feedback made between u and u . Finally, a friend recommendation list was generated by running the informative friendship computation. The results of all the evaluation runs were evaluated to examine whether our method was able to recommend informative friends to $u _ { i } .$ . The evaluation metrics include the conventional coverage rate at K (denoted as C@K) [7] and the mean reciprocal rank (denoted as MRR) [49]. The coverage rate at K was defined as follows:

$$
C @ K = \frac {| h i t |}{| T |},\tag{12}
$$

where |hit| represents the number of evaluation runs in which the top-K recommendation covers the removed informative user, and |T| denotes the total number of evaluation runs. The mean reciprocal rank is a wellknown ranking quality metric and is defined as follows:

$$
M R R _ {i} = \max _ {u _ {j} \in \text { the   informative   users   of } u _ {i}} \left(1 / r a n k _ {i j}\right),\tag{13}
$$

The effect of Z on preference learning  
![](/api/attachments/H7MFFSMS/fulltext/images/36900282f2c807a77ade52adcc28adc24b89673e136768f660aac0edc9cea522.jpg)  
Fig. 5. The effect of Z on the normalized learning loss.

where $r a n k _ { i j }$ is the position of the removed informative user $u _ { j }$ in the friend recommendation list. Basically, the two metrics respectively measure how many and how early the informative friends are suggested, but they hardly reflect the quality of the recommendation list. Therefore, we designed a new evaluation metric called the discounted cumulative ranking performance (denoted as DCRP) that calibrates the quality of the recommended friends and their ranking positions in the generated recommendation list. The discounted cumulative ranking performance is defined as follows:

$$
D C R P _ {i} = \sum_ {u _ {j} \in \text { the   informative   users   of } u _ {i}} \left(2 ^ {I F _ {i j} - 1} / \log_ {2} \left(\operatorname{rank} _ {i j} + 1\right)\right),\tag{14}
$$

where $I F _ { i j }$ denotes the frequency of feedback made by u to $u _ { j } .$ Basically, DCRP is a variant of discounted cumulative gain (DCG) [52], a common ranking quality metric. A large DCRP implies that the recommendation method is able to assign a high ranking position to the users that the target user frequently interacts with. In other words, the method is effective. The DCRPs and MRRs of all the evaluation users were averaged to obtain the overall performance.

It should be noted that Apache Mahout,<sup>5</sup> a Java-based machine learning library, was adopted to implement our stochastic gradient descent algorithm. The learning rate γ and regularized coefficient λ of the stochastic gradient descent was set at 1 and 0.01, respectively, as suggested by the library authors.

## 4.2. Effects of parameter settings on preference learning

Before evaluating the recommendation performance, we first investigated the effect of system parameters on preference learning. We also conducted tests to calculate the execution time of our preference learning on an Intel I7-4790K PC with a 32 GB main memory. There were two system parameters in our recommendation method, namely, Z and sr. Fig. 5 shows the effect of Z which designates the dimension of the latent preferences. Here, sr is set at 250. Later, we examine its effect. In Fig. 5, the x-coordinate is Z and the y-coordinate designates the learning loss (i.e., Eq. (5)) normalized by Z. We normalized the learning loss by $Z$ in order to diminish the influence of the regularization terms when Z is large. The trend in the figure shows that a large $Z$ generally produces a low loss. This is because a large Z is able to differentiate latent preferences. However, a large Z will also increase the length of preference learning as shown in Fig. 6. For instance, by setting $Z = 1 0 0 0$ , our method takes 652,554 ms to complete a 50-iteration learning, and the execution time is about twice that of $Z = 6 0 0$ . Note that the data we used to evaluate the execution time is only a small portion of Weibo, and because of this, to deploy the proposed method to a real-world social network site it is critical to

C.C. Chen et al. / Decision Support Systems xxx (2016) xxx–xxx

The effect of Z on learning time  
![](/api/attachments/H7MFFSMS/fulltext/images/22e6a2417c78b8a38825574d45a05db9bb368badc0650b9a5102e268d62130f6.jpg)  
Fig. 6. The effect of Z on the execution time of preference learning.

select a moderate Z that balances the tradeoff between learning loss and learning computation cost. As can been seen in Fig. 5, the improvement of Z over the loss is not significant when Z is larger than 600. For these reasons, we set Z at 600 in the following experiments.

As mentioned in Section 3.1, parameter sr calibrates the number of friends on social influence and a large sr decreases the social influence in preference learning. Fig. 7, illustrates the effect of sr on preference learning, shows that the learning loss decreases as sr increases. Because we observed that the decrease of learning loss becomes minor when sr is larger than 250, we set the parameter at 250 in the following experiments. It is interesting to note that the setting makes the most of the α 's in our datasets at around 0.1. This finding thus implies that social network site users are generally self-centered when reading social update streams.

Lastly, we examined the impact of the above settings on the convergence of our stochastic gradient descent. Although Fig. 8 shows that our preference learning quickly converges within a few iterations, the 50-iteration learning still takes approximately 385,432 ms.

## 4.3. Comparisons and results

We compare our method with nine friend recommendation methods: Pop [1], FdFd [50], FlFd [50], KNN [51], MF [20], SVD++ [50], MF + LTR [9], CLiMF [44], and SR [32]. For our method, we examine the fixed and adaptive social influence strategies, respectively denoted as OurMetho $\mathsf { I } _ { \mathrm { f i x } }$ and $\mathrm { O u r M e t h o d } _ { \mathrm { a d a p t i v e } } ,$ that we introduced in Section 3.1. For OurMethod , the α is set at 0.1 as suggested in our previous work [46]. Comparing the two strategies helps us comprehend the effect of the adaptive social influence on recommendation performance. To ensure the comparisons are fair, all the compared methods were evaluated by means of the leave-one-out evaluation procedure.

The effect of sr on preference learning  
![](/api/attachments/H7MFFSMS/fulltext/images/3841615ce5cecfc38b121bc7c83c8673e7380e94f76ba64d098d74f457262dd2.jpg)  
Fig. 7. The effect of sr on the normalized learning loss.

The convergence of preference learning  
![](/api/attachments/H7MFFSMS/fulltext/images/8c579b425a397f0ad12a36f2752406a2c76e3e89eb5321fcd31f39eb26a69d92.jpg)  
Fig. 8. The convergence of preference learning.

• Pop (Popularity): This method and the FdFd and FlFd methods analyzed social network structures to recommend friends to users. This method assumes that popular users are worth recommending, and thus recommends users with many friends (followers) in the given training dataset.

• FdFd (Friend-of-Friend): FdFd recommends the followees of followees, normalized by their in-degrees in the social network to a target user.

• FlFd (Follower-of-Friend): The method analyzes the co-neighboring degree between users. It recommends the users whose followees are highly overlapped with those of a target user.

• KNN (K-Nearest Neighborhood): The method is a user-based collaborative filtering method. It utilizes the following Jaccard coefficient to measure the similarity between users:

$$
J a c c a r d S i m (u _ {i}, u _ {j}) = \frac {\left| U R _ {i} \cap U R _ {j} \right|}{\left| U R _ {i} \cup U R _ {j} \right|},\tag{15}
$$

where UR stands for the set of updates that were replied to or liked by $u _ { i } ,$ i.e., $U R _ { i } = \{ \nu _ { x } | \nu _ { x } \in V , r _ { i x } = 1 \}$ . The method treats similar users as friends and recommends the users to a target user.

• MF (Matrix Factorization): MF is the most common realization of the latent factor model. In its basic form, the method trains user and item preferences by minimizing the root mean square error of the approximated user–item matrix.

• SVD++: In [50], SVD++ [19] is employed to recommend informative friends to users. The method is also a matrix factorization and it extracts the preferences of users and updates from a user-update relation matrix. The learned preferences are used to predict an update's rating. The users whose updates received high predicted ratings will be deemed informative and are recommended.

• MF + LTR (Matrix Factorization with Learning to Rank): Both this method, CLiMF, and our method incorporate pairwised learning to rank into matrix factorization for preference learning. Nevertheless, MF + LTR and CLiMF do not examine the influence of social ties (i.e., social influence), but a comparison with these methods helps us comprehend the effect of social influence. It is noteworthy that MF + LTR has been considered the state-of-the-art recommendation method due to its superior recommendation performance [9].

• CLiMF: The method models user relationships by means of a friendship matrix. It combines pairwised learning to rank and matrix factorization to extract preferences of users from the matrix, which are used to recommend preference-similar friends to users.

• SR (Social Regularization): In [32], the authors considered users and their friends having similar preferences, and incorporated the social influence as a regularization term into the matrix factorization process to minimize their preference differences. The authors developed two regularization models. Here, we compare the individual-based regularization model due to its superior performance [32]. Also, the vector space similarity is used to measure the similarity between users. The learned preferences are used to recommended friends to a target user.

As can be seen in Tables 2 and 3, the coverage rates of the methods are all low. This is because the methods need to predict (recommend) the removed informative friend among thousands of experiment users in each evaluation run, and the prediction task is not trivial. Both FdFd and FlFd are link-prediction-based recommendation methods. While the friend-of-friend and social co-neighboring patterns they used were useful in identifying real-world friends of users in a social site [23], the identified friends may not be informative. As a result, these recommendation methods had poor coverage rates. Pop's coverage rates were also poor. This is because the method simply recommended famous people on social network sites and did not consider the preferences of users. As a result of this, the suggested celebrities may be irrelevant to user interests, which will decrease Pop's coverage rates.

Contrary to expectations, the performances of the MF and SVD++ methods were inferior especially when under Data200. Both the methods learned user and update preferences by minimizing the root mean square error of the approximated R. We observed that R's entries are of a binary scale, rather than a numerical score. Moreover, the user– item matrix R was so sparse that learned preferences would be obscured [20]. For these reasons, the methods were unable to recommend informative friends. Nonetheless, the coverage rates of KNN were normally superior to those of MF and SVD++, even though it also measured user similarity in terms of sparse user feedback. We speculate that the joint feedback among users may not be fortuitous, especially when feedback are so sparse. The Jaccard coefficient was thus able to identify users with similar preferences and recommend informative friends.

MF + LTR outperformed the MF method, indicating that learning to rank was capable of resisting the sparsity problem when learning user and update preferences. It is worth pointing out that CLiMF's cover rates were low, even though the method is also based on learning to rank. The inferior performance was due to the method's design that suggests preference-similar friends, which means that the method cannot recommend informative friends to users. Note that the coverage rates of the MF + LTR method were further improved by incorporating social influence into $\mathrm { M F } \ + \ \mathrm { \Delta \ L T R }$ (i.e., our method) and both OurMethod and OurMethod significantly outperformed the compared methods. Furthermore, although SR, MF, and SVD++ adopted similar matrix factorization approaches to learn latent preferences, SR performed better than MF and SVD++ did in terms of coverage rate, MRR, and DCRP because MF and SVD++ neglected social influence in their preference learning process. These comparisons correspond with the findings in [10,32,53,54,56] that social information is effective in item recommendation. While OurMetho $\mathsf { I } _ { \mathsf { a d a p t i v e } }$ normally had better coverage rates than OurMethod <sub>x</sub>, its improvement over $0 \mathrm { u r M e t h o d } _ { \mathrm { f i x } }$ was insignificant given that most of OurMethod $_ \mathrm { a d a p t i v e } ^ { \prime } S$ α s are around 0.1 and they are very close to $0 \mathrm { u r M e t h o d } _ { \mathrm { f i x } } \mathrm { ' } s$ fixed $\alpha _ { i }$ $( \mathrm { i } . \mathsf { e } . , \alpha _ { i } = 1 )$ ). Nevertheless, the adaptive social influence removes the need for tuning $\alpha _ { i } ,$ which makes it adaptable to different recommendation scenarios. Our method was superior to SR because SR's matrix factorization aims at minimizing the error of the approximated user– item matrix, and the sparsity of user–item matrix affects the learned preferences. Our method, on the other hand, is based on learning to rank which is effective in resisting the sparsity problem of preference learning [39].

With regard to the MRR of the compared methods, our method again outperformed the other methods insofar as it was able to place informative friends at the top of the recommendation list. This is important because users generally focus on only a few top items in a recommendation list [8]. Similar to the last experiment, the MRR performances of MF, FdFd, FlFd, and Pop were poor because they recommended hardly any informative users, and did not put them at the top of a recommendation list. While Pop's coverage rates were sometimes inferior to those of FdFd and FlFd, its MRR scores were superior to those of FdFd and FlFd. We concluded that a great number of users' informative friends were not celebrities, but users still intensively followed a few of them relevant to their preferences. The MRRs of SR, $\mathrm { M F } + \mathrm { L T R }$ , OurMethod , and OurMethodad were far better than those of the MF and SVD++. The combined results once again show that learning to rank and social influence are effective in informative friend recommendation.

Finally, we examined the DCRP of the compared methods. The inferior performance of FdFd indicates that users were not intimate with indirect friends (i.e., friends of friends), and thus recommending the friends of friends to users would exacerbate the information overload of social update streams. It is worth pointing out that FlFd's DCRP scores were superior to those of FdFd and Pop. Since the recommendation of FlFd is based on the co-neighboring degree between users, the recommended friends are likely to be of the same community. The result of FlFd reveals that the updates shared among social communities are informative. Under Data200, the sparsity problem of matrix factorization was so severe that the DCRP scores of MF and SVD++ were even inferior to that of the naive Pop method. Interestingly, MF and SVD++ performed better than Pop did under Data300. The reason for this is that the experiment users under Data300 were active, which lessened the sparsity of the matrix R and therefore improved the DCRP performance of MF and SVD++. Note that MF and SVD++ were inferior to MF + LTR again. This is because these methods aim to approximate the user–item matrix but the approximation ignores the precedence of items. The learned preferences are thus incapable of ranking frequently interacting friends in a top position. The learning-to-rankbased methods generally outperformed the other methods and our method achieved the best DCRP score. The results again validate the

Table 2  
The performance of the compared methods under Data200.

<table><tr><td rowspan="2"></td><td colspan="4">C@K</td><td rowspan="2">MRR</td><td rowspan="2">DCRP</td></tr><tr><td>K=5</td><td>K=10</td><td>K=20</td><td>K=50</td></tr><tr><td>Pop</td><td>0.0075***</td><td>0.0109***</td><td>0.0157***</td><td>0.0554***</td><td>0.1795^^^</td><td>0.0017^^^</td></tr><tr><td>FdFd</td><td>0.0075***</td><td>0.0102***</td><td>0.0150***</td><td>0.0424***</td><td>0.1082^^^</td><td>0.0015^^^</td></tr><tr><td>FlFd</td><td>0.0041***</td><td>0.0088***</td><td>0.0170***</td><td>0.0396***</td><td>0.1302^^^</td><td>0.0018^^^</td></tr><tr><td>KNN</td><td>0.0184***</td><td>0.0266***</td><td>0.0506**</td><td>0.0943***</td><td>0.2244^^^</td><td>0.0020^^^</td></tr><tr><td>MF</td><td>0.0088***</td><td>0.0109***</td><td>0.0170***</td><td>0.0369***</td><td>0.1116^^^</td><td>0.0017^^^</td></tr><tr><td>SVD++</td><td>0.0020***</td><td>0.0034***</td><td>0.0061***</td><td>0.0109***</td><td>0.0339^^^</td><td>0.0015^^^</td></tr><tr><td>MF+LTR</td><td>0.0150***</td><td>0.0246***</td><td>0.0485***</td><td>0.0896***</td><td>0.2227^^^</td><td>0.0021^^</td></tr><tr><td>CLiMF</td><td>0.0054***</td><td>0.0095***</td><td>0.0198***</td><td>0.0348***</td><td>0.0723^^^</td><td>0.0016^^^</td></tr><tr><td>SR</td><td>0.0212**</td><td>0.0307***</td><td>0.0519**</td><td>0.1101**</td><td>0.2013^^^</td><td>0.0022</td></tr><tr><td>OurMethodfix</td><td>0.0314</td><td>0.0465</td><td>0.0691</td><td>0.1326</td><td>0.4363^</td><td>0.0024</td></tr><tr><td>OurMethodadaptive</td><td>0.0341</td><td>0.0492</td><td>0.0691</td><td>0.1361</td><td>0.4879</td><td>0.0024</td></tr></table>

The results marked with \*, \*\*, and \*\*\* show, respectively, the improvements achieved by OurMethod over the compared methods with 90%, 95% and 99% confidence levels based on the Z-statistic for two proportions, and the symbol ^, ^^, and ^^^ indicate the improvements based on the one-tailed paired t test [18].

Please cite this article as: C.C. Chen, et al., Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.017

Table 3  
The performance of the compared methods under Data300.

<table><tr><td rowspan="2"></td><td colspan="4">C@K</td><td rowspan="2">MRR</td><td rowspan="2">DCRP</td></tr><tr><td>K=5</td><td>K=10</td><td>K=20</td><td>K=50</td></tr><tr><td>Pop</td><td>0.0076***</td><td>0.0138***</td><td>0.0209***</td><td>0.0657***</td><td>0.0737^^^</td><td>0.0062^^^</td></tr><tr><td>FdFd</td><td>0.0114***</td><td>0.0204***</td><td>0.0347***</td><td>0.0781***</td><td>0.0630^^^</td><td>0.0058^^^</td></tr><tr><td>FlFd</td><td>0.0080***</td><td>0.0200***</td><td>0.0390***</td><td>0.0814***</td><td>0.0490^^^</td><td>0.0063^^^</td></tr><tr><td>KNN</td><td>0.0219***</td><td>0.0376***</td><td>0.0681***</td><td>0.1405***</td><td>0.1182^^^</td><td>0.0065^^^</td></tr><tr><td>MF</td><td>0.0204***</td><td>0.0319***</td><td>0.0624***</td><td>0.1252***</td><td>0.1191^^^</td><td>0.0069^^^</td></tr><tr><td>SVD++</td><td>0.0080***</td><td>0.0200***</td><td>0.0390***</td><td>0.0814***</td><td>0.0490^^^</td><td>0.0063^^^</td></tr><tr><td>MF+LTR</td><td>0.0414***</td><td>0.0700***</td><td>0.1152***</td><td>0.2000***</td><td>0.1999^^^</td><td>0.0079^^^</td></tr><tr><td>CLiMF</td><td>0.0242***</td><td>0.0395***</td><td>0.0690***</td><td>0.1291***</td><td>0.1344^^^</td><td>0.0068^^^</td></tr><tr><td>SR</td><td>0.0333***</td><td>0.0662***</td><td>0.1090***</td><td>0.2053***</td><td>0.1805^^^</td><td>0.0079^^^</td></tr><tr><td>OurMethodfix</td><td>0.0662</td><td>0.0976</td><td>0.1386</td><td>0.2310</td><td>0.3134</td><td>0.0087^</td></tr><tr><td>OurMethodadaptive</td><td>0.0714</td><td>0.1048</td><td>0.1500</td><td>0.2286</td><td>0.3287</td><td>0.0090</td></tr></table>

The results marked with \*, \*\*, and \*\*\* show, respectively, the improvements achieved by OurMetho $\mathsf { I } _ { \mathsf { a d a p t i v e } }$ over the compared methods with 90%, 95% and 99% confidence levels based on the Z-statistic for two proportions, and the symbol $\hat { \cdot } ^ { \wedge \wedge } ,$ and ^^^ indicate the improvements based on the one-tailed paired t test [18].

value of learning to rank. As mentioned above, the updates shared among social communities are informative, and for this reason, social influence is effective in improving DCRP because it represents the influence of social ties. It is worth mentioning that the DCRP scores of our method under Data300 are much higher than those under Data200. The results indicate that our method is efficient when the target users are actively involved in social connections.

In summary, our method achieved the best coverage rate, MRR, and DCRP. In other words, our method was able to recommend not only intimate friends but also those whose updates are informative to users. Since users prefer the updates shared by the recommended users, the proposed methods are likely to alleviate the information overload of social update streams.

## 5. Discussions and implications

To summarize, the contributions of this research are as follows. First, we made a distinction between the current friend recommendation research and our informative friend recommendation. The current literature on friend recommendation normally focuses on identifying real-world friends or friends with similar preferences, whereas we advocate suggesting informative friends whose updates are useful to social network site users. Second, we have proposed an effective informative friend recommendation method which integrates learning to rank and matrix factorization in order to learn the preferences of users and updates. In addition, social influence is incorporated into the proposed method to suggest informative friends to users. The experiments based on a huge real-world dataset demonstrate that the proposed method is capable of overcoming the data sparsity of preference learning and the social influence is useful in the recommendation task. Finally, the proposed DCRP contributes a new evaluation metric that can be generalized to evaluate different recommendation tasks. In contrast to the current recommendation evaluation metrics (e.g., coverage) that are normally based on the percentage of successful recommendations, the proposed DCRP further calibrates the quality of the recommended items and their ranking positions. It thus provides a comprehensive evaluation of recommendation systems.

Several interesting findings from the experiment results can benefit researchers and practitioners in different ways. First, the methods based on network structure analysis (e.g., FdFd, FlFd, and Pop) and user preference similarity (e.g., CLiMF and KNN) were found to be inferior. This result suggests that the current friend recommendation methods are inappropriate for recommending informative friends because they normally focus on identifving real-world friends or friends with similar preferences. The result also reveals that research on informative friend recommendation has not been well-addressed in prior studies. Our research thus contributes to this new research topic. Second, learning to rank enhanced the recommendation of matrix factorization, which suggests that learning to rank is capable of resisting the sparsity problem that matrix factorization suffered when learning user and update preferences. This result also corresponds with the findings in [39] validating that learning to rank is useful for resolving the sparsity problem of preference learning. Third, our method achieved its remarkable performance by incorporating social influence into learning to rank. Social influence has been confirmed in many e-commerce recommendation scenarios in which consumers are generally influenced by friends or trusted people when they make purchasing decisions [10,32,54,56]. By regarding updates as social network site products, our research further generalizes social in uence to include the preferences of users on updates that are influenced by social ties. As a result of this, users that are informative to the friends of a target user can also be informative to the user. Finally, the comparison between Data300 and Data200 indicates that users actively involved in social connections would benefit more from the proposed method. Consequently, our research makes a practical contribution to the social network business because a great portion of the business income comes from advertising based on the number of active users. By offering active users satisfactory friend recommendations, our method is able to improve the information quality of their social update streams so as to increase their loyalty to social network sites.

## 6. Limitations and future works

Nowadays, social update streams have become a major medium for users to receive valuable information. Since social update streams are basically constituted by the updates shared by friends, the quality of the friends thus affects the value of social update streams. It has been observed that social network site users generally suffer from the information overload of social update streams because of having too many friends. The thousands of social updates every day from hundreds of friends can decrease the users' intentions to visit social network sites, and by extension, decrease the sites' advertising revenues. To resolve the information overload problem and to create a win–win proposition for both users and site owners, recommending informative friends to users is critical.

Our research is subject to the following limitations. First, our preference learning method considers that updates without user feedback (e.g., likes or replies) have a low precedence. However, some of the updates may interest users but the users just do not give feedback for some reason. Future studies can analyze indirect user feedback (e.g., the time a user spends on an update) to acquire more representative training updates for preference learning. Second, the meaning of the learned user preferences is unexplainable. Like other matrix factorization models, the preferences we learned are represented by a set of high-dimensional vectors and the dimension definition is unknown. Because of this, the learned user preferences are specific to the task of informative friend recommendations and cannot contribute toward other domains. The length of learning is definitely a computational challenge when deploying our method. Fortunately, parallel machine learning (e.g., the parallelized stochastic gradient descent [57]) is becoming increasingly popular and many advanced learning mechanisms can help distribute our preference learning and make our method practicable in extremely big social networks. Finally, the dataset we used for performance evaluation was collected from Weibo which is an East Asian social network site, so future research can conduct experiments on Western social networks to examine culture influence. In the future, we will deploy the proposed method on a social network site, and user feedback (e.g., acceptance or rejection) on the suggested friends will be collected to examine the satisfaction of online users. The feedback will further be analyzed to enhance the recommendation method. While this paper focused on informative friend recommendations, the proposed method can be applied to various social recommendation tasks, such as recommending useful groups to social network users by considering social groups as items. We also plan to extend our method to different social recommendation domains and evaluate their recommendation performances.

## Acknowledgments

This research was supported in part by MOST 103-2221-E-002-106- MY2 from the Ministry of Science and Technology, Republic of China.

## References

[1] M.G. Armentano, D. Godoy, A. Amandi, Topology-based recommendation of users in micro-blogging communities, Journal of Computer Science and Technology 27 (2012) 624–634.

[2] Y. Bae, P.-M. Ryu, H. Kim, Predicting the lifespan and retweet times of tweets based on multiple feature analysis ETRI Journal 36 (2014) 418–428

[3] P. Bao, H.-W. Shen, W. Chen, X.-Q. Cheng, Cumulative effect in information diffusion: empirical study on a microblogging network, PloS One 8 (2013), e76027.

[4] F. Benevenuto, T. Rodrigues, M. Cha, V. Almeida, Characterizing user behavior in online social networks. IMC '09 Proceedings of the 9th ACM SIGCOMM Conference on Internet Measurement Conference, ACM 2009, pp, 49–62.

[5] J. Bennett, S. Lanning, The Netflix Prize, Proceedings of the KDD Cup and Workshop, ACM 2007, pp. 3–6.

[6] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative filtering, Proceedings of the Fourteenth Conference on Uncertainty in Artificial Intelligence, Morgan Kaufmann Publishers Inc. 1998, pp. 43–52

[7] C.C. Chen, Y.-H. Wan, M.-C. Chung, Y.-C. Sun, An effective recommendation method for cold start new users using trust and distrust networks, Information Sciences 224 (2013) 19-36

[8] H. Chen, D.R. Karger, Less is more: probabilistic models for retrieving fewer relevant documents, Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 2006, pp. 429–436.

[9] K. Chen, T. Chen, G. Zheng, O. Jin, E. Yao, Y. Yu, Collaborative personalized tweet recommendation, SIGIR '12 Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 2012, pp. 661–670.

[10] C.M.K. Cheung, D.R. Thadani, The impact of electronic word-of-mouth communication: a literature analysis and integrative model, Decision Support Systems 54 (2012) 461–470.

[11] A. Enders, H. Hungenberg, H.-P. Denker, S. Mauch, The long tail of social networking: revenue models of social networking sites, European Management Journal 26 (2008) 199–211

[12] D. Fortin, M. Uncles, S. Burton, A. Soboleva, Interactive or reactive? Marketing with Twitter, Journal of Consumer Marketing 28 (2011) 491–499.

[13] J. Han, C. Moraga, The influence of the sigmoid function parameters on the speed of backpropagation learning, From Natural to Artificial Neural Computation, Springer 1995, pp. 195–201.

[14] J. Hannon, M. Bennett, B. Smyth, Recommending Twitter users to follow using content and collaborative filtering approaches Proceedings of the Fourth ACM Conference on Recommender Systems, ACM, Barcelona, Spain 2010, pp. 199–206.

[15] L. Hong, R. Bekkerman, J. Adler, B.D. Davison, Learning to rank social update streams, SIGIR '12 Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval ACM 2012 pp. 651–660.

[16] J. Hopcroft, T. Lou, J. Tang, Who will follow you back? Reciprocal relationship prediction, CIKM '11 Proceeding of the 20th ACM Conference on Information and Knowledge Management, ACM 2011, pp. 1137–1146.

[17] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classification model, Decision Support Systems 48 (2010) 470-479

[18] G. Keller, Statistics for Management and Economics, Cengage Learning, 2015.

[19] Y. Koren, Factorization meets the neighborhood: a multifaceted collaborative filtering model, Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2008, pp. 426–434.

[20] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (2009) 30–37.

[21] K. Koroleva, H. Krasnova, O. Günther, ‘STOP SPAMMING ME!’—exploring information overload on Facebook, Proceedings of the 16th Americas Conference on Information Systems (AMCIS) 2010, p. 447.

[22] H. Kwak, C. Lee, H. Park, S. Moon, What is Twitter, a social network or a news media? WWW '10 Proceedings of the 19th International Conference on World Wide Web, ACM 2010, pp. 591–600.

[23] J. Leskovec, D. Huttenlocher, J. Kleinberg, Predicting positive and negative links in online social networks, WWW '10 Proceedings of the 19th International Conference on World Wide Web, ACM 2010, pp. 641–650.

[24] R. Li, K.H. Lei, R. Khadiwala, K.-C. Chang, TEDAS: a Twitter-based event detection and analysis system, data engineering (ICDE), 2012 IEEE 28th International Conference on, IEEE 2012, pp. 1273–1276.

[25] T.-P. Liang, H.-J. Lai, Y.-C. Ku, Personalized content recommendation and user satisfaction: theoretical synthesis and empirical findings, Journal of Management Information Systems 23 (2006) 45–70.

[26] H.-Y. Liao, K.-Y. Chen, D.-R. Liu, Virtual friend recommendations in virtual worlds, Decision Support Systems 69 (2015) 59–69.

[27] D. Liben-Nowell, J. Kleinberg, The link-prediction problem for social networks Journal of the American Society for Information Science and Technology 58 (2007) 1019–1031.

[28] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative ltering, Internet Computing, IEEE 7 (2003) 76–80.

[29] T.-Y. Liu, Learning to rank for information retrieval, Foundations and Trends in Information Retrieval 3 (2009) 225–331.

[30] P. Luarn, H.H. Lin, A customer loyalty model for E-service context, Journal of Electronic Commerce Research 4 (2003) 156–167.

[31] H. Ma, H. Yang, M.R. Lyu, I. King, SoRec: social recommendation using probabilistic matrix factorization, CIKM '08 Proceedings of the 17th ACM Conference on Information and Knowledge Management, ACM 2008, pp. 931–940.

[32] H. Ma, D. Zhou, C. Liu, M.R. Lyu, I. King, Recommender systems with social regularization, WSDM '11 Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, ACM 2011, pp. 287–296.

[33] S.E. Miller, L.A. Jensen, Connecting and communicating with students on Facebook, Computers in Libraries 27 (2007) 18–22.

[34] T.M. Mitchell, Machine learning and data mining, Communications of the ACM 42 (1999) 30–36.

[35] Y. Pan, F. Cong, K. Chen, Y. Yu, Diffusion-aware personalized social update recommendation, RecSys '13 Proceedings of the 7th ACM Conference on Recommender Systems, ACM 2013, pp. 69–76.

[36] A. Paterek, Improving regularized singular value decomposition for collaborative filtering, Proceedings of KDD Cup and Workshop 2007, pp. 5–8.

[37] J.-F. Pessiot, T.-V. Truong, N. Usunier, M.-R. Amini, P. Gallinari, Learning to rank for collaborative filtering, Proceedings of the 9th International Conference on Enterprise Information Systems 2007, pp. 145–151.

[38] A. Popescul, L.H. Ungar, Statistical relational learning for link prediction, IJCAI03 Workshop on Learning Statistical Models from Relational Data, 2003

[39] S. Rendle, C. Freudenthaler, Z. Gantner, L. Schmidt-Thieme, BPR: Bayesian personalized ranking from implicit feedback, UAI '09 Proceedings of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence, ACM 2009 pp. 452-461.

[40] P. Resnick. N. Jacovou. M. Suchak. P. Bergstrom. I. Riedl. GroupLens: an open architecture for collaborative filtering of netnews, Proceedings of the 1994 ACM Conference on Computer Supported Cooperative Work, ACM 1994, pp. 175-186.

[41] R.R. Sarukkai, Link prediction and path analysis using Markov chains, Computer Networks 33 (2000) 377 386

[42] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Application of dimensionality reduction in recommender system—a case study, ACM WebKDD 2000 Workshop, 2000.

[43] Y. Shen, R. Jin, Learning personal + social latent factor model for social recommendation, KDD '12 Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2012, pp. 1303–1311.

[44] Y. Shi, A. Karatzoglou, L. Baltrunas, M. Larson, N. Oliver, A. Hanjalic, CLiMF: learning to maximize reciprocal rank with collaborative less-is-more filtering, RecSys '12 Proceedings of the Sixth ACM Conference on Recommender Systems, ACM 2012, pp. 139–146.

[45] Y. Shi, M. Larson, A. Hanjalic, List-wise learning to rank with matrix factorization for collaborative filtering, Proceedings of the Fourth ACM Conference on Recommender Systems, ACM 2010, pp. 269–272.

[46] S.-Y. Shih, M. Lee, C.C. Chen, An effective friend recommendation method using learning to rank and social influence, PACIS 2015 Proceedings, Paper, 242, 2015 (pp. Paper 242).

[47] G. Strang, Linear Algebra and Its Applications, Thomson, Brooks/Cole, Belmont, CA, 2006.

[48] S.T. Tong, B. Van Der Heide, L. Langwell, J.B. Walther, Too much of a good thing? The relationship between number of friends and interpersonal impressions on Facebook Journal of Computer-Mediated Communication 13 (2008). 531–549

[49] E.M. Voorhees, The TREC-8 Question Answering Track Report, TREC, 1999 77–82.

[50] S. Wan, Y. Lan, J. Guo, C. Fan, X. Cheng, Informational friend recommendation in social media, SIGIR '13 Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 2013, pp. 1045–1048.

[51] J. Wang, A.P. De Vries, M.J. Reinders, Unifying user-based and item-based collaborative filtering approaches by similarity fusion, Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 2006, pp. 501–508.

[52] Y. Wang, L. Wang, Y. Li, D. He, W. Chen, T.-Y. Liu, A theoretical analysis of NDCG ranking measures, Proceedings of the 26th Annual Conference on Learning Theory (COLT 2013), 2013.

[53] X. Yang, H. Steck, Y. Guo, Y. Liu, On top K recommendation using social networks, RecSys' 12 Proceedings of the Sixth ACM Conference on Recommender Systems, ACM 2012, pp. 67–74.

[54] M. Ye, X. Liu, W.-C. Lee, Exploring social influence for recommendation—a generative model approach, SIGIR '12 Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval 2012, pp. 671–680.

[55] J. Zhang, P.S. Yu, Z.-H. Zhou, Meta-path based multi-network collective link prediction, KDD '14 Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2014, pp. 1286–1295.

[56] L. Zhu, I. Benbasat, Z. Jiang, Let's shop online together: an empirical investigation of collaborative online shopping support, Information Systems Research 21 (2010) 872–891.

[57] Y. Zhuang, W.-S. Chin, Y.-C. Juan, C.-J. Lin, A fast parallel SGD for matrix factorization in shared memory systems, Proceedings of the 7th ACM Conference on Recommender Systems, ACM, Hong Kong, China 2013, pp. 249–256.

Chien Chin Chen received his B.S. and M.S. degrees in Computer Science and Information Engineering from National Central University, Taiwan, in 1997 and 1999, respectively. Then he joined the Institute of Information Science at Academia Sinica, Taiwan, as a research assistant and participated in several research projects in the area of text mining. In August 2003, he began his Ph.D. program and received his Ph.D. degree in Electrical Engineering from National Taiwan University, Taiwan, in 2007. He is currently an associate professor of the Department of Information Management at National Taiwan University. His papers have ap peared in Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, ACM Transactions on Information Systems (TOIS), Information Sciences, Knowledge-Based Systems, ACM SIGIR, ACM SIGKDD, ECIR, AIRS, PACIS, etc. His current research interests include text mining, business intelligence, data mining, and recommendation systems.

Shun-Yuan Shih received his M.S. degree in Information Management from National Taiwan University, Taiwan, in 2015. His current research interests include recommendation system, learning to rank, and business intelligence.

Meng Lee received his M.S. degree in Information Management from National Taiwan University, Taiwan, in 2015. His current research interests include learning to rank, statistical sampling, and business intelligence.
