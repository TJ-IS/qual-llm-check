---
otero_id: 6176
otero_key: "C9KFWJWS"
title: "A new temporal and social PMF-based method to predict users' interests in micro-blogging"
authors: "Hongyun Bao; Qiudan Li; Stephen Shaoyi Liao; Shuangyong Song; Heng Gao"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.02.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new temporal and social PMF-based method to predict users' interests in micro-blogging

Hongyun Bao <sup>a,1</sup>, Qiudan Li <sup>a,</sup>⁎, Stephen Shaoyi Liao <sup>b,c,2</sup>, Shuangyong Song <sup>a,1</sup>, Heng Gao <sup>a,1</sup>

<sup>a</sup> State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China

<sup>b</sup> Department of Information Systems and Advanced Transportation Information Systems Research Center, City University of Hong Kong, Hong Kong

<sup>c</sup> Department of Electronic Commerce and Information Management, School of Economics and Management, Southwest Jiaotong University, Chengdu 610031, China

## a r t i c l e i n f o

Article history: Received 15 May 2012 Received in revised form 20 November 2012 Accepted 4 February 2013 Available online 24 February 2013

Keywords: Micro-blogging User interest prediction Temporal and social probabilistic matrix factorization model Interest variation

## a b s t r a c t

Micro-blogging is becoming an increasingly popular social media platform where users can discover interesting information about the real world and especially corporations are able to understand customers' demands. The fast diffusion of information and the convenience of micro-blogging have resulted in large audiences sharing their daily activities, exchanging opinions and establishing friendships with others. By analyzing the user-generated contents, one can explore users' potential interests, which helps micro-blogging provide users with better personalized information services. Users' behaviors are affected by opinions of their friends and changes in their interests over time. Based on these intuitions, in this paper we propose a temporal and social probabilistic matrix factorization model to predict users' potential interests in micro-blogging. By exploiting the matrix factorization technique to learn latent features of users and topics, our model analyzes the impacts of time information and users' activities, including posting of tweets and establishing friendships with others, on the latent feature space of users and topics of their interests. The proposed model provides a uni<sup>fi</sup>ed way to fuse the time information and the social network structure to predict users' future interests accurately. The experimental results on Sina-weibo, one of the most popular micro-blogging sites in China, demonstrate the ef<sup>fi</sup>ciency and effectiveness of our proposed model.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

With the rapid development of the Internet, social media has played an increasingly signi<sup>fi</sup>cant role in our everyday lives, providing reports on world events, improving enterprise in<sup>fl</sup>uence through social media marketing and so on. Micro-blogging is becoming one of the most popular social media platforms where users can share their daily activities, exchange opinions, publish posts on some trending topics and follow others to get relevant information about their interested topics. If A is following B, B is called A's friend, and A is called B's follower. Thus friendships can either be reciprocated or one-way [10]. The convenience and high frequency of updates of information in micro-blogging have attracted a large number of users to actively participate. For example, Sina-weibo, one of the most popular micro-blogging services in China, has had over 300 M unique visitors since December 31, 2011 and around 100 M tweets per day.<sup>3</sup> Nowadays, more and more corporations are registering user accounts on Sina-weibo for marketing. For example, Nokia successfully held a product release conference for N8 on August 25, 2010.

Corporations utilize micro-blogging not only to introduce their products but also to formulate customer-driven marketing plans by obtaining rich information such as which features customers consider important in their products, new market dynamics and so on. Microblogging has become an important e-commerce marketing channel, and the promotion of merchandise is accessible to micro-blogging users around every corner of this platform. Users' interest plays a vital role in the process of micro-blogging's development [7], which in<sup>fl</sup>uences the effect of micro-blogging marketing soon afterwards. The research <sup>fi</sup>ndings in [5] point out that the accurate prediction of users' interest will improve their satisfaction and promote their buying decisions, which will increase the e-commerce business bene<sup>fi</sup>ts undoubtedly. Decision makers will also bene<sup>fi</sup>t from the interest prediction work; Chen and Cheng and Zhao and Lu [4,28] proposed that decision makers need to grasp users' interest for raising up their satisfaction and providing reasonable results. Asur and Huberman [2] tell us that the box-of<sup>fi</sup>ce revenues of movies can be successfully forecasted in advance of their release by analyzing users' interest in micro-blogging. If the forecasted box-of<sup>fi</sup>ce revenues are below expectations, decision makers can provide ways of <sup>fi</sup>lm promotion with some incentives in time, or some other methods for coming up to their expectations. All in all, it's valuable and meaningful to predict users' interest in social media, whether for e-commerce business or decision makers. On one hand, it can help micro-blogging systems provide users with better personalized information and advertising services to motivate users to be more active. On the other hand, corporations can easily capture users' future interest and make marketing decisions.

In micro-blogging, trending topics are popular topics, which may be related to emerging events and breaking news or topics under the discussion by a large fraction of micro-blogging users [19]. In Sina-weibo, trending topics are edited and complemented, and users are available to enter into the trending topics and take part in the discussion by publishing posts on them. Trending topics often have a clear meaning [11], mainly relating to entertainment, sports, current events and so on. If the user is interested in a trending topic, he/she may publish posts on it. In other words, if a user has published posts on a trending topic, it shows that the user has interest in this topic. Posts published on some trending topics can well re<sup>fl</sup>ect users' interests. Thus, in this paper, we use trending topics to represent users' interests.

Despite the importance of user interest prediction in micro-blogging, existing works on micro-blogging mainly focus on mining users' current interests; little work has been done on prediction of users' potential interests. Nori et al. [20] focused on computing the similarity between a user and a set of resources to predict the user's interests. However, this method ignores the in<sup>fl</sup>uence of the user's friends on his/her interests. Besides, it doesn't take the evolution of interests into account.

Some researchers have suggested that users are more affected by opinions of their peers than in<sup>fl</sup>uentials [21,24,25]. By comparing quality of recommendations made by recommender systems to recommendations made by users' friends, Sinha et al. [23] showed that users' friends consistently provided better recommendations than recommender systems. In social recommendation, making use of the information in a social graph has recently been receiving increasing research attention. The experimental results [6,9,15–17] show that fusing the social network structure of users with the user–item rating matrix can help make more accurate and personalized recommendations in a social rating network. From this viewpoint, a user's social network affects users' behaviors on the Web.

Additionally, interests of Web users change over time. For timeaware recommendation, it is important to capture users' temporal preferences to make more accurate recommendations. Xiang et al. [12] stated that users' dynamic preferences are affected by both their long-term and short-term preferences. That means their interests may vary over time. In this case, to capture users' temporal preferences, it is necessary to follow the evolution of users' preferences. Generally, recent preferences may play a more important role in predicting current preferences while earlier preferences have relatively smaller contribution to <sup>fi</sup>nal recommendation. Especially in micro-blogging, the rich information and frequent updates make users' interests more extensive and changeable over time. Therefore, to improve the accuracy of prediction of users' interests in micro-blogging, both the social network structure and time information should be taken into consideration.

SocialMF [9] is an effective method for detecting users' interests by exploiting the matrix factorization techniques and analyzing the in<sup>fl</sup>uence of users' friendships on their interests. Based on this model, we propose a temporal and social probabilistic matrix factorization model (TS-PMF) which fuses on social in<sup>fl</sup>uence and the time information to predict users' interests in micro-blogging. Following the evolution of users' interests, to import time information in our model, we make the latent features of users and topics associated with their previous latent features by adopting an exponential time decay function. Using this idea, our approach accurately describes the change of the distribution of the latent feature space of users' interests. The proposed model can re<sup>fl</sup>ect the impacts of users' interest evolution and users' friendships on their future interests, thus realizing the prediction of users' interests. The experimental results on Sina-weibo demonstrate that our model can improve the quality of prediction.

The remainder of this paper is organized as follows. In Section 2, some related work is discussed. Section 3 introduces the proposed model. Results of the detailed experimental analysis are presented in Section 4. Finally, we conclude the paper and present some directions for future work in Section 5.

## 2. Related work

In this work we propose a novel model to predict users' interests in micro-blogging. Our work is related to prediction of user interest in micro-blogging, trust-aware recommendation and time-aware recommendation. In this section we review the related works.

## 2.1. User interest analysis and prediction

Banerjee et al. [3] gathered tweets data from Twitter across ten (worldwide) cities over a period of four weeks to generate an exhaustive list of keywords and then applied statistical and mining techniques to discover the distribution of users' interest on categories such as “movie”, “food”, “game”, “dinner” and so on. Xu et al. [30] proposed a modi<sup>fi</sup>ed author-topic model to discover users' topics of interest on Twitter by <sup>fi</sup>ltering out interest-unrelated tweets (noisy posts) from the aggregated user pro<sup>fi</sup>les. These studies concentrated on the text level analysis of user interests. Yan et al. [27] established a human dynamic model co-driven by interest and social identity and showed that users' interest in sending posts is positively correlated with the number of comments on their previous posts.

Existing works on micro-blogging mainly focus on mining users' current interests; little work has been done on prediction of users' potential interests. Nori et al. [20] proposed ActionGraph, a new graphic representation for modeling users' multinomial, time-evolving actions, to compute the similarity between a user and a set of resources to predict the user's interest. ActionGraph is a bipartite graph whose edge connects an action node at some point in time and the object nodes representing users and resources. It preserves the time information for each user by representing the same action in different times as different action nodes. However, it ignores the in<sup>fl</sup>uence of the user's friendships on his/her interest. Besides, it doesn't take the evolution of interest into account.

## 2.2. Trust-aware recommendation

In social networks, users can follow others whom they are interested in, and then they may have social interactions or connections instead of being independent and identically distributed. Many researchers have recently focused on trust-aware recommender systems. Ziegler and Golbeck [29] established two frameworks for investigating and analyzing the correlation between interpersonal trust and interest similarity, and empirical results showed that the mean similarity of trusting and trusted peers exceeded the arbitrary user similarity. Massa and Avesani [18] show that the idea of Trust-aware Recommender System is not to search for similar users as CF (Collaborative Filtering) does but to search for trustable users by exploiting trust propagation over the trust network. The items appreciated by these users are then recommended to the active user. They present a complete evaluation of Trust-aware Recommender System, by comparing different algorithms, ranging from traditional CF ones to algorithms that utilize only trust information with different trust metrics and algorithms that combine both trust and similarity to baseline algorithms. Those methods are all memory-based methods not scalable to very large datasets.

Ma et al. [6,15,16] studied the relationship between the trust network and the user–item matrix systematically and proposed the methods integrating social network structure and the user–item rating matrix, which were based on probabilistic factor analysis. Jamali and Ester [9] stated that the real world recommendation processes are not re<sup>fl</sup>ected in the model [6,15,16]. Due to social in<sup>fl</sup>uence, related people in a social network in<sup>fl</sup>uence each other to become more similar. They proposed a SocialMF model by incorporating trust propagation into a matrix factorization for recommendation in social network. Their experimental results demonstrate that SocialMF outperforms existing methods for social network based recommendation.

In the advertising recommendation system of micro-blogging, some researchers are taking advantage of friendships of users [14].

## 2.3. Time-aware recommendation

Ding and Li [26] presented a new time weight collaborative <sup>fi</sup>ltering algorithm using an exponential time decay function to compute time weights for different items according to each user and each cluster of items. Xiang et al. [12] argued that user preferences often exhibit long-term and short-term factors and proposed a STG model to capture users' dynamic preferences by considering all items viewed by a user as his long-term preferences and items viewed by him at a given time as his short-term preferences. Xiong et al. [13] presented a Bayesian Probabilistic Tensor Factorization algorithm for modeling evolving relational data by organizing the ratings into a three-dimensional tensor whose three dimensions correspond to user, item and time slices, assuming each time feature vector depends only on its immediate predecessor. Ahmed et al. [1] argued user pro<sup>fi</sup>les were temporal and changed user activity patterns, thus presenting a comprehensive statistical framework for user pro<sup>fi</sup>ling based on topic models. Their method modeled topical interests of a user dynamically where both the user association with the topics and the topics themselves were allowed to vary over time, ensuring that the pro<sup>fi</sup>les remain current.

Thus, in extant literature, little work has been done on prediction of users' potential interests in micro-blogging; works on trust- and time-aware recommendation show that both the social network structure and the time information are important for recommendation in social network. In this paper, we propose a TS-PMF model to predict users' interests in micro-blogging, which provides a uni<sup>fi</sup>ed way to integrate the social network structure and the time information. Speci<sup>fi</sup>cally, we express users' interests as a series of temporal matrices and use the probabilistic matrix factorization technique to learn the users' latent feature space and topics' latent feature space by employing users' social network and temporal matrices.

## 3. The proposed user interest prediction model

In this section, <sup>fi</sup>rst we introduce the theoretical background for our proposed model. Second, we illustrate how to fuse social network structure and time information in our TS-PMF model to predict users' interests in micro-blogging.

## 3.1. Theoretical background

We introduce some notations <sup>fi</sup>rst. We have a set of users $U = \{ u _ { 1 } , . . . , u _ { m } \}$ and a set of topics $Z = \{ z _ { 1 } , . . . , z _ { n } \}$ in a micro-blogging dataset. We construct a user–topic matrix $R \in { R ^ { m \times n } }$ to represent users' interests, where we set $R _ { i j } = 1 { \mathrm { ~ i f ~ } } u _ { i }$ has published posts on $z _ { j } .$ In micro-blogging, each user can follow others whom he is interested in. Then users' friendships can be described as a user–user matrix $C \in R ^ { m \times m }$ , where $C _ { i j } = 1$ that denotes u has followed $u _ { j } .$ Furthermore, we record the set of $u _ { i } ^ { \prime } s$ friends as $N ( i )$

The task of predicting users' interests is to predict the relational scores for a given user u on topic $Z = \{ z _ { 1 } , . . . , z _ { n } \}$ in the future using R and C. Salakhutdinov and Mnih [22] have shown that it is very effective to employ matrix factorization techniques to learn the latent characteristics of users and topics and predict the scores using these latent characteristics. Let $U \in {  R } ^ { d \times m }$ and $V \in R ^ { d \times n }$ be the latent user and topic feature matrices, with column vectors $U _ { i }$ and $V _ { j }$ representing d-dimensional user- and topic-latent feature vectors of $u _ { i }$ and $z _ { j } ,$ respectively. The goal of matrix factorization is to model each score as the production of user- and topic-latent feature vectors, i.e. $R _ { i j } \approx U _ { i } ^ { T } V _ { j } ,$ where $\Breve { U } _ { i } ^ { T }$ is the transpose of $U _ { i \cdot }$ As is shown in the SocialMF model, the conditional probability of the known scores is de<sup>fi</sup>ned as:

$$
p (R | U, V, \sigma_ {R} ^ {2}) = \prod_ {i = 1} ^ {m} \prod_ {j = 1} ^ {n} \left[ N \Big (R _ {i j} \Big | g \Big (U _ {i} ^ {T} V \Big), \sigma_ {R} ^ {2} \Big) \right] ^ {I _ {i j} ^ {R}}\tag{1}
$$

where $N ( x | \mu , \sigma ^ { 2 } )$ is the Gaussian distribution with mean $\mu$ and variance $\sigma ^ { 2 }$ , and $I _ { i j } ^ { R }$ is the indicator function that is equal to 1 if $R _ { i j } = 1$ and equal to 0 otherwise. The function $g ( x )$ is the logistic function $g ( x ) = 1 / \left( 1 + \exp ( - x ) \right)$ ), which makes it possible to bound x within the range [0,1].

Social network researchers have pointed out that the social network structure plays an important role in users' behavior [21,23,25] Speci<sup>fi</sup>cally, a user is more and more similar to his/her friends. From this perspective, SocialMF incorporates social in<sup>fl</sup>uence into the matrix factorization for recommendation in social network [9].

Because the behavior of a user $u _ { i }$ is affected by his/her friends $N ( i ) ,$ , the latent feature vector of $u _ { i }$ is dependent on latent feature vectors of all his/her friends $u _ { \nu } \in N ( i )$ ). For user latent features, there are two factors: the zero-mean Gaussian prior and the latent features of his/her friends. Therefore,

$$
\begin{array}{l} p \left(U | C, \sigma_ {U} ^ {2}, \sigma_ {C} ^ {2}\right) \propto p \left(U \sigma_ {U} ^ {2} |\right) \times p \left(\sigma_ {C} ^ {2}\right) \\ = \prod_ {i = 1} ^ {m} N \left(U _ {i} | 0, \sigma_ {U} ^ {2} I\right) \times \prod_ {i = 1} ^ {m} N \left(U _ {i} N | \sum_ {v \in N (i)} C _ {i v} U _ {v}, \sigma_ {C} ^ {2} I\right) \end{array}\tag{2}
$$

where each row of C is normalized, through $C _ { i \nu } = 1 / | N ( i ) |$ with $\nu \in N ( i )$

![](/api/attachments/C9KFWJWS/fulltext/images/1fc735899035db720f1354d7804dbc406d824578e01e4111b2830c7062ede054.jpg)  
Fig. 1. Graphical model of the baseline SocialMF considering the social network in the matrix factorization.

Now, the posterior probability of latent variables U and V can be obtained through a Bayesian inference. Maximizing the log of the posterior distribution is equivalent to minimizing the following sum-of-squared-errors objective function with quadratic regularization terms:

$$
\begin{array}{l} E (R, C, U, V) = \frac {1}{2} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} I _ {i j} ^ {R} \left(R _ {i j} - g \left(U _ {i} ^ {T} V _ {j}\right)\right) ^ {2} \\ \qquad + \frac {\lambda_ {U}}{2} \sum_ {i = 1} ^ {m} U _ {i} ^ {T} U _ {i} + \frac {\lambda_ {V}}{2} \sum_ {j = 1} ^ {n} V _ {j} ^ {T} V _ {j} \\ \qquad + \frac {\lambda_ {C}}{2} \sum_ {i = 1} ^ {m} \left(\left(U _ {i} - \sum_ {v \in N (i)} C _ {i v} U _ {i}\right) ^ {T} \left(U _ {i} - \sum_ {v \in N (i)} C _ {i v} U _ {i}\right)\right). \end{array}\tag{3}
$$

The above optimization can be done ef<sup>fi</sup>ciently using gradient descent. The graphical model for SocialMF is presented in Fig. 1.

## 3.2. Proposed user interest prediction model

In the near future, micro-blogging users may focus on new topics, and they may also show different concerns to the topics which they have been interested in for a period of time. The above users' dynamic interests are mainly affected by their friends and their historical favorites Based on these intuitions, the primary motivation of our model is to provide a uni<sup>fi</sup>ed way to fuse the social network structure and the evolution of users' interests for predicting users' interests accurately. In this section, we extend SocialMF to predict users' future interests in micro-blogging by taking time information into account.

## 3.2.1. Toy example

We use a simple toy example to demonstrate the proposed model for predicting users' interests in micro-blogging. There are 6 users $U = \{ u _ { 1 } , . . . , u _ { 6 } \}$ and 8 topics $Z = \{ z _ { 1 } , . . . , z _ { 8 } \}$ in total. The relationships among users (nodes) are illustrated in Fig. 2(a), and the edge from u to $u _ { j }$ denotes that $u _ { i }$ has followed $u _ { j } .$ We have segmented users' historical data into 3 time points $\left( T _ { 1 } , T _ { 2 } , T _ { 3 } \right)$ . As shown in Fig. 2(b, c, d), each user has published posts on some topics in $T _ { t } ( t = 1 , 2 , 3 )$ to express interest in those topics. Our main goal is to predict users' interests in the future time $T _ { 4 } .$ As elaborated in Section 1, a user's social friendships make his/her interest similar to his/her friends and the current interest is also affected by historical interest. Therefore, we minimize the sum-squared distance to the target matrix $R _ { t }$ by $U _ { t } ^ { T } V _ { t }$ to factorize the current user–topic matrix $R _ { t }$ fusing the social network structure and the evolution of users' interest, where $U _ { t }$ denotes the user laten feature space and $V _ { t }$ represents the topic feature space in time t. If we use 5 dimensions to perform the matrix factorization, we obtain $U _ { t }$ and $V _ { t } \left( t = 1 , 2 , 3 \right)$ and then compute the mean matrices $\mathtt { M } _ { U _ { 4 } }$ and $\mathtt { M } _ { V _ { 4 } }$ of $U _ { 4 }$ and $V _ { 4 }$ for predicting the user-matrix $R _ { 4 }$ in $T _ { 4 } \mathrm { : }$

![](/api/attachments/C9KFWJWS/fulltext/images/b064751a2763417dda58ec5854fffd56a0fa0c1e4e1b3f2fcba95b3d48d27774.jpg)  
(a) Social network (b) $R _ { I } \colon$ user-topic matrix in $T _ { I }$ (c) $R _ { 2 } { \mathrm { : } }$ user-topic matrix in $T _ { 2 }$ (d) $R _ { 3 } { \mathrm { : } }$ user-topic matrix in $T _ { 3 }$ (e) $R _ { 4 } \mathrm { : }$ user-topic matrix in $T _ { 4 }$  
Fig. 2. Data of the toy example.

![](/api/attachments/C9KFWJWS/fulltext/images/9592d63f9fceb5520d5ae8ea33047a42c5f46f6fb032d800bfd303829509ce28.jpg)  
Fig. 3. The framework of predicting users' interest.

$$
M _ {U _ {4}} \left[ \begin{array}{c c c c c c} - 0. 3 2 4 1 & - 0. 2 2 8 8 & - 0. 8 0 3 3 & - 0. 3 3 5 3 & - 0. 4 1 0 4 & - 0. 6 7 4 3 \\ - 0. 8 1 2 0 & - 0. 2 7 7 2 & - 1. 1 1 9 8 & - 0. 4 9 2 8 & - 0. 8 0 9 8 & - 0. 6 0 4 4 \\ - 0. 8 7 0 9 & 0. 2 1 9 0 & - 0. 0 8 0 6 & - 0. 0 9 7 9 & - 0. 4 8 6 3 & 0. 2 6 4 3 \\ - 0. 3 3 0 9 & - 1. 1 1 8 1 & 0. 8 5 6 9 & - 0. 6 0 1 2 & - 0. 1 0 0 0 & 0. 3 6 7 7 \\ - 0. 5 2 4 6 & - 0. 6 8 2 9 & 0. 3 1 0 0 & 0. 2 8 2 3 & - 0. 9 4 6 4 & 0. 5 7 3 4 \end{array} \right]
$$

$$
M _ {V _ {4}} \left[ \begin{array}{c c c c c c c c} - 0. 5 5 9 4 & - 0. 4 7 5 8 & - 0. 5 5 5 9 & 0. 2 0 3 1 & - 0. 2 3 1 5 & - 1. 0 5 7 2 & - 0. 2 7 4 1 & - 0. 2 5 9 0 \\ - 0. 6 0 3 8 & - 0. 6 7 4 0 & - 0. 6 8 1 6 & - 0. 0 4 7 7 & - 0. 3 5 4 0 & - 0. 8 8 4 6 & - 0. 8 7 6 5 & - 0. 7 6 2 7 \\ 0. 0 1 2 9 & - 0. 1 0 6 9 & - 0. 0 1 5 7 & - 0. 4 8 4 4 & - 1 9 8 8 & - 0. 0 4 7 8 & - 0. 5 0 8 7 & - 0. 0 6 9 1 \\ 0. 7 6 6 0 & - 0. 6 8 1 8 & 0. 8 9 7 1 & - 0. 5 5 4 4 & - 0. 6 9 1 8 & 0. 5 1 4 8 & 0. 1 2 6 5 & - 0. 8 1 6 4 \\ 0. 2 4 2 4 & - 0. 9 6 8 9 & 0. 3 8 0 5 & - 0. 4 7 8 8 & - 0. 0 6 5 6 & 0. 6 5 0 3 & - 0. 0 5 6 3 & - \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \text {   } \end{array} \right]
$$

where $M _ { U _ { 4 } , \ L }$ and $M _ { V _ { 4 } j }$ are the column vectors and denote the latent feature vector of u and topic $z _ { j } ,$ respectively, in $T _ { 4 } .$ . Then we use $R _ { 4 } { \approx } M _ { U _ { 4 } } ^ { T } M _ { \nu _ { 4 } }$ to predict all the values in $R _ { 4 } ,$ , where we need to transfer the value of $M _ { U _ { 4 } , i } ^ { T } M _ { v _ { 4 } , j }$ using the function $g ( x )$ introduced in Section 3.1. And then according to the values in $R _ { 4 }$ as shown in Fig. $2 ( \mathsf e )$ , each user is provided a topic list he/she is likely to prefer in the future.

We take $u _ { 4 }$ as an example to explain the reasoning behind the prediction by our model. As shown in Fig. 2(a), $u _ { 4 }$ has followed $u _ { 1 }$ and $u _ { 2 } .$ u has focused on $z _ { 8 }$ in $T _ { 2 }$ and $u _ { 2 }$ has also focused on $z _ { 8 }$ in $T _ { 2 }$ and $T _ { 3 }$ as well as $u _ { 1 }$ does in $T _ { 3 } .$ Considering the impacts of his/her friends and the evolution of interest, our model predicts $u _ { 4 }$ will be interested in $z _ { 8 }$ in $T _ { 4 }$ with the maximum probability of $0 . 6 7$ . Since $u _ { 4 }$ is interested in $z _ { 6 }$ in $T _ { 3 } ,$ and only $u _ { 1 }$ has paid attention to $z _ { 6 }$ in $T _ { 1 }$ , our model provides $z _ { 6 }$ for $u _ { 4 }$ in the second place in the prediction list. While both $u _ { 1 }$ and $u _ { 2 }$ are interested in $z _ { 2 }$ in $T _ { 3 } ,$ and $u _ { 4 }$ has never published posts on $z _ { 2 } ,$ our model places $z _ { 2 }$ in the third place.

## 3.2.2. The proposed model

It's noticeable that users' interests are changing over time; users show their concerns to different topics at different times. For example, a user was fond of some electronic products in early days, but lately, he took a great interest in the topic of ‘new iPad’ for a few days. Two in<sup>fl</sup>uencing factors may prompt him to perform like this: maybe he was informed of the message that the new iPad has been released, or he was likely affected by his friends who had focused on this topic for a while. The users' dynamically changing interests can be expressed as the collection of users' sequential interest matrix at different times, each of which is constructed as a temporal user–topic matrix $R _ { t } \in R ^ { m \times n } ,$ , where t $( t = 1 , 2 , . . . , N )$ is the time label of the data section. In the user–topic matrix, the value of element $R _ { t , i j }$ equals 1 means that the user $u _ { i }$ is interested in the topic $z _ { j }$ at time point t. Meanwhile, users' friendships can be expressed as a user–user matrix C. Our proposed model is designed to utilize users' sequential interest matrices $\{ R _ { 1 } , . . . , R _ { N } \}$ at the existing time points $( t = 1 , 2 , . . . , N )$ and the users' friendships matrix C, to predict users' interest in the near future.

The framework of our proposed model is shown in Fig. 3. At each time point, our model will <sup>fi</sup>nd the matrix $R _ { t } \approx U _ { t } ^ { T } V _ { t } \left( t = 1 , . . . , N \right)$ which minimizes the sum-squared distance to the target matrix $R _ { t }$ under the constraints of the temporal and social impacts, where $U _ { t } ^ { T }$ and $V _ { t } ^ { T }$ represent the users' and topics' latent feature spaces in time t.

In time t, the conditional distribution probability of the observed items in $R _ { t }$ is similar to that in Eq. (1):

$$
p \Big (R _ {t} | U _ {t}, V _ {t}, \sigma_ {R _ {t}} ^ {2} \Big) = \prod_ {i = 1} ^ {m} \prod_ {j = 1} ^ {n} \left[ N \Big (R _ {t, i j} \Big | g \Big (U _ {t, i} ^ {T} V _ {t, j} \Big), \sigma_ {R _ {t}} ^ {2} \Big) \right] ^ {I _ {i j} ^ {R _ {t}}}.\tag{4}
$$

$U _ { t , i } ^ { T }$ represents the latent feature vector of user $u _ { i }$ in time t. The user's latent feature vector follows Gaussian distribution [6,9,15,16], which is decided by the mean value of Gaussian distribution. Changes in mean values always re<sup>fl</sup>ect changes in users' interests. Normally, users' current interests will be affected by his historical favorites; the in<sup>fl</sup>uence will be greater with the closer interest to the current time. Amazingly, the exponential decay function can describe the in<sup>fl</sup>uence process effectively [26], with the following mathematical expression:

$$
f (k) = \exp \left(- \frac {t - k}{\beta}\right) (k \in \{1, 2, 3,..., t - 1 \}   \beta > 0).\tag{5}
$$

In Eq. (5), the value o $\mathbf { \dot { \boldsymbol { \beta } } }$ presents the kernel parameter, and the value of t − k shows us the time interval between the k-th time point and the current time t. The higher value $t - k$ presents the earlier time k from current time t, accompanied with the smaller in<sup>fl</sup>uencing value f(k). It's evident that the exponential decay function can vividly illustrate the in<sup>fl</sup>uence that the historical favorites have on the current interests

Based on the above analyses, we utilize exponential decay function with kernel parameter $\boldsymbol { \beta }$ to compute the mean value matrix of user-latent feature and the mean value matrix of topic-latent feature in time t. The computing formulation is listed below:

$$
M _ {U _ {t}} = \theta \sum_ {k = 1} ^ {t - 1} \exp \left(- \frac {t - k}{\beta}\right) U _ {k}, M _ {V _ {t}} = \theta \sum_ {k = 1} ^ {t - 1} \exp \left(- \frac {t - k}{\beta}\right) V _ {k}\tag{6}
$$

where $\mathbf { M } _ { U t } , \mathbf { M } _ { V t }$ are the mean matrices of $U _ { t }$ and $V _ { t }$ with spherical Gaussian priors, and θ is a weight parameter that indicates how important the whole previous time points are to the current one.

In summary, the user's latent feature vector is affected by two factors, of which are the latent feature vectors of his historical interests and his friends' interests. Therefore, the conditional distribution probability of users' latent features can be expressed like this:

$$
\begin{array}{l} p \Big (U _ {t} | \{R _ {1}, R _ {2},..., R _ {t - 1} \}, C, \sigma_ {C} ^ {2}, \sigma_ {U _ {t}} ^ {2} \Big) \propto \\ p \Big (U _ {t} | \{R _ {1}, R _ {2},..., R _ {t - 1} \}, \sigma_ {U _ {t}} ^ {2} \Big) \times p \Big (U _ {t} | C, \sigma_ {C} ^ {2} \Big) \\ = \prod_ {i = 1} ^ {m} N \Big (U _ {t, i} | M _ {U _ {t, i}}, \sigma_ {U _ {t}} ^ {2} I \Big) \times \prod_ {i = 1} ^ {m} N \Bigg (U _ {t, i} | \sum_ {\nu \in N (i)} C _ {i \nu} U _ {t, \nu}, \sigma_ {C} ^ {2} I \Bigg). \end{array}\tag{7}
$$

The above normal distribution consists of two parts. The <sup>fi</sup>rst part, that is $\prod _ { i = 1 } ^ { m } N \Big ( U _ { t , i } \Big | M _ { U _ { t , i } } , \sigma _ { U _ { t } } ^ { 2 } \mathrm { I } \Big )$ , informs us of the fact that the distribution vectors of users' latent feature space are close to their historical distribution vectors. The second part, which is $\prod _ { i = 1 } ^ { m } N \left( U _ { t , i } \middle | \sum _ { \nu \in N ( i ) } C _ { i \nu } U _ { t , \nu } , \sigma _ { C } ^ { 2 } \mathrm { I } \right)$ tells us that the distribution vectors of users' latent feature space are also close to their friends' distribution vectors.

<table><tr><td> $R_t$ </td><td>The user-topic matrix in time t</td></tr><tr><td>C</td><td>The user-user matrix</td></tr><tr><td> $U_t^T$ </td><td>The users&#x27; latent feature space in time t</td></tr><tr><td> $V_t^T$ </td><td>The topics&#x27; latent feature space in time t</td></tr><tr><td> $M_{Ut}$ </td><td>The mean matrix of  $U_t$  with spherical Gaussian priors in time t</td></tr><tr><td> $M_{Vt}$ </td><td>The mean matrix of  $V_t$  with spherical Gaussian priors in time t</td></tr><tr><td>θ</td><td>A weight that indicates how important the whole previous time points are to the current one</td></tr><tr><td>β</td><td>The kernel parameter</td></tr><tr><td>d</td><td>The dimension of latent feature space</td></tr><tr><td> $λ_C$ </td><td>The impact of the social network on users&#x27; interest</td></tr><tr><td> $λ_U$ </td><td>The impact of the users&#x27; latent feature vectors on users&#x27; interest</td></tr><tr><td> $λ_V$ </td><td>The impact of the topics&#x27; latent feature vectors on users&#x27; interest</td></tr><tr><td>T</td><td>The days for partitioning the data set</td></tr></table>

![](/api/attachments/C9KFWJWS/fulltext/images/4c2b517843b1b2d690f69735a221c1768f62d2fc78cad62205c72cfe0f663542.jpg)  
Fig. 4. Accumulated error value of different dimensionality d with iterations.

After that, through a Bayesian inference, we have the following equation for the posterior probability over latent features of users and topics,

$$
\begin{array}{l} p \Big (U _ {t}, V _ {t} | \{R _ {1}, R _ {2}, \ldots , R _ {t - 1}, R _ {t} \}, C, \sigma_ {C} ^ {2}, \sigma_ {U _ {t}} ^ {2}, \sigma_ {V _ {t}} ^ {2}, \sigma_ {R _ {t}} ^ {2} \Big) \propto \\ p \Big (R _ {t} | U _ {t}, V _ {t}, \sigma_ {R _ {t}} ^ {2} \Big) p \Big (U _ {t} | C, \sigma_ {C} ^ {2} \Big) p \Big (U _ {t} | \{R _ {1}, R _ {2}, \ldots , R _ {t - 1} \}, \sigma_ {U _ {t}} ^ {2} \Big) p \Big (V _ {t} | \{R _ {1}, R _ {2}, \ldots , R _ {t - 1} \}, \sigma_ {V _ {t}} ^ {2} \Big). \end{array}\tag{8}
$$

The log of the posterior distribution for our proposed model at time point t is given by

$$
\begin{array}{l} \ln p \Big (U _ {t}, V _ {t} | \{R _ {1}, R _ {2}, \dots , R _ {t} \}, C, \sigma_ {C} ^ {2}, \sigma_ {U _ {t}} ^ {2}, \sigma_ {V _ {t}} ^ {2}, \sigma_ {R _ {t}} ^ {2} \Big) = \\ - \frac {1}{2 \sigma_ {R _ {t}} ^ {2}} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} I _ {i j} ^ {R _ {t}} \left(R _ {t, i j} - g \left(U _ {t, i} ^ {T} V _ {t, j}\right)\right) ^ {2} - \frac {1}{2} \left(\sum_ {i = 1} ^ {m} \sum_ {j} ^ {n} I _ {i j} ^ {R _ {t}}\right) \ln \sigma_ {R _ {t}} ^ {2} \\ - \frac {1}{2 \sigma_ {U _ {t}} ^ {2}} \sum_ {i = 1} ^ {m} \left(U _ {t, i} - M _ {U _ {t, i}}\right) ^ {T} \left(U _ {t, i} - M _ {U _ {t, i}}\right) - \frac {1}{2 \sigma_ {V _ {t}} ^ {2}} \sum_ {j = 1} ^ {n} \left(V _ {t, j} - M _ {V _ {t, j}}\right) ^ {T} \left(V _ {t, j} - M _ {V _ {t, j}}\right) \\ - \frac {1}{2 \sigma_ {C} ^ {2}} \sum_ {i = 1} ^ {m} \left(\left(U _ {i} - \sum_ {\nu \in N (i)} C _ {\mathrm{i} \nu} U _ {i}\right) ^ {T} \left(U _ {i} - \sum_ {\nu \in N (i)} C _ {\mathrm{i} \nu} U _ {i}\right)\right) \\ - \frac {1}{2} \left(m d \ln \sigma_ {U _ {t}} ^ {2} + n d \ln \sigma_ {V _ {t}} ^ {2} + m d \ln \sigma_ {C} ^ {2}\right) + W. \end{array}\tag{9}
$$

In this equation, W is a constant. Once the parameters $\sigma _ { R _ { t } } , \sigma _ { U _ { t } } , \sigma _ { V _ { t } } , \sigma _ { C }$ are <sup>fi</sup>xed, maximizing the log of the posterior distribution with regard to $U _ { t }$ and $V _ { t }$ is equivalent to minimizing the following sum-of-squared-errors objective function:

$$
\begin{array}{l} E (U _ {t}, V _ {t}, \{R _ {1}, R _ {2},..., R _ {t} \}, C) = \frac {1}{2} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} I _ {i j} ^ {R _ {t}} \left(R _ {t, i j} - g \left(U _ {t, i} ^ {T} V _ {t, j}\right)\right) ^ {2} + \frac {\lambda_ {U _ {t}}}{2} \left\| U _ {t} - M _ {U _ {t}} \right\| _ {F} ^ {2} \\ + \frac {\lambda_ {V _ {t}}}{2} \left\| V _ {t} - M _ {V _ {t}} \right\| _ {F} ^ {2} + \frac {\lambda_ {C}}{2} \sum_ {i = 1} ^ {m} \left(U _ {t, i} - \sum_ {v \in N (i)} C _ {i v} U _ {t, v}\right) ^ {T} \left(U _ {t, i} - \sum_ {v \in N (i)} C _ {i v} U _ {t, v}\right). \end{array}\tag{10}
$$

In Eq. (10), $\lambda _ { C } = \delta _ { R _ { t } } ^ { 2 } / \delta _ { C } ^ { 2 } , \ \lambda _ { U _ { t } } = \delta _ { R _ { t } } ^ { 2 } / \delta _ { U _ { t } } ^ { 2 } , \ \lambda _ { V _ { t } } = \delta _ { R _ { t } } ^ { 2 } / \delta _ { V _ { t } } ^ { 2 }$ , and $| | \cdot | | _ { F } ^ { 2 }$ are the Frobenius norm. The <sup>fi</sup>rst sum item in Eq. (10) represents the sum-squared error between $R _ { t }$ and $U _ { t } ^ { T } V _ { t } ,$ while the second term and the third term denote the sum-squared distance from the users' and the topics' latent feature space to the prior ones, we utilize the forth sum to represent the sum-squared deviation between the user's latent feature

## Table 2

Precison at top-N results of the <sup>fi</sup>ve models.

<table><tr><td rowspan="2"></td><td colspan="4">Dimensionality d = 10</td><td colspan="4">Dimensionality d = 45</td><td colspan="4">Dimensionality d = 50</td><td rowspan="2">MT1</td></tr><tr><td>PMF</td><td>SocialMF</td><td>T-PMF</td><td>TS-PMF</td><td>PMF</td><td>SocialMF</td><td>T-PMF</td><td>TS-PMF</td><td>PMF</td><td>SocialMF</td><td>T-PMF</td><td>TS-PMF</td></tr><tr><td>Pr1</td><td>0.2612</td><td>0.2673</td><td>0.2816</td><td>0.3571</td><td>0.3388</td><td>0.3508</td><td>0.4878</td><td>0.4939</td><td>0.3408</td><td>0.3408</td><td>0.4510</td><td>0.4776</td><td>0.0571</td></tr><tr><td>Pr3</td><td>0.2449</td><td>0.2524</td><td>0.2265</td><td>0.2782</td><td>0.2959</td><td>0.3041</td><td>0.3313</td><td>0.3531</td><td>0.3197</td><td>0.3224</td><td>0.3156</td><td>0.3463</td><td>0.0408</td></tr><tr><td>Pr5</td><td>0.2241</td><td>0.2294</td><td>0.1955</td><td>0.2318</td><td>0.2637</td><td>0.2629</td><td>0.2661</td><td>0.2714</td><td>0.2722</td><td>0.2731</td><td>0.2600</td><td>0.2845</td><td>0.0322</td></tr><tr><td>Pr10</td><td>0.1733</td><td>0.1749</td><td>0.1500</td><td>0.1645</td><td>0.1898</td><td>0.1916</td><td>0.1845</td><td>0.1859</td><td>0.1947</td><td>0.1973</td><td>0.1876</td><td>0.1865</td><td>0.0216</td></tr></table>

space and his friends' latent feature space. We can <sup>fi</sup>nd a local optimal value of the objective function in Eq. (10) by performing gradient descent in $U _ { t , i }$ and $V _ { t , j } ,$ that is

$$
\begin{array}{l} \frac {\partial E}{\partial U _ {t , i}} = \sum_ {j = 1} ^ {n} I _ {i j} ^ {R _ {t}} g ^ {'} \left(U _ {t, i} ^ {T} V _ {t, j}\right) \left(g \left(U _ {t, i} ^ {T} V _ {t, j}\right) - R _ {t, i j}\right) V _ {t, j} + \lambda_ {U} \left(U _ {t, i} - M _ {U _ {t, i}}\right) \\ \qquad + \lambda_ {C} \left(U _ {t, i} - \sum_ {\nu \in N (i)} C _ {i v} U _ {t, \nu}\right) - \lambda_ {C} \sum_ {\{\nu | i \in N (\nu) \}} C _ {i v} \left(U _ {t, \nu} - \sum_ {\omega \in N (i)} C _ {\nu \omega} U _ {t, \omega}\right) \\ \frac {\partial E}{\partial V _ {t , j}} = \sum_ {i = 1} ^ {m} I _ {i j} ^ {R _ {t}} g ^ {'} \left(U _ {t, i} ^ {T} V _ {t, j}\right) \left(g \left(U _ {t, i} ^ {T} V _ {t, j}\right) - R _ {t, i j}\right) U _ {t, i} + \lambda_ {V} \left(V _ {t, j} - M _ {V _ {t, j}}\right) \end{array}\tag{11}
$$

12

where $g ^ { \prime } ( x ) = \exp ( - x ) / ( 1 + \exp ( - x ) ) ^ { 2 }$ is the derivative of logistic function g(x). In order to reduce the model complexity, in all experiments we set $\lambda _ { U _ { t } } = \lambda _ { V _ { t } } = \lambda _ { U } = \lambda _ { V } .$

Our proposed model provides an effective method to predict users' interests by integrating users' friendships and users' historical interests. Our model can effectively take various factors that will have in<sup>fl</sup>uence on users' interests change into account, thus achieving accurate forecasts of users' future interests. The process of predicting users' interests with our model is described in Algorithm 1. And the notations used throughout the paper are summarized in Table 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. The process of predicting users' interests

Input:
    dataset:  $\{R_{1}, \ldots, R_{N}\}$ , C;
    the dimension of the latent feature: d;
    parameters:  $\lambda_{U}$ ,  $\lambda_{V}$ ,  $\lambda_{C}$ ,  $\theta$ ,  $\beta$ ;
    an updating parameter:  $\partial$ ;
    convergence parameter:  $\varepsilon$ ;
    the maximum number of iterations: K.

Output:
    the user–topic matrix in time segment  $N+1:R_{N+1}$ .

Learning:
    set  $M_{V_{t}} = zeros(d,n)$ ,  $M_{U_{t}} = zeros(d,m)$ .
    For t = 1, ..., N
    Step 1: initialize  $U_{t}, V_{t}, U_{t,0} = U_{t}, V_{t,0} = V_{t}, E_{0} = inf$ .
    If t &gt; 1
    compute the mean matrices  $M_{U_{t}}$  and  $M_{V_{t}}$  in Eq. (6).
    End If

    For l = 1, ..., K
    Step 2: compute the gradient descent in Eq. (11) and (12).
    Step 3: updating:
    $U_{t} = U_{t} + \frac{\partial E}{\partial U_{t}}, V_{t} = V_{t} + \frac{\partial E}{\partial V_{t}}$  (13)
    Step 4: compute  $E_{1}$  in Eq. (10)
    If  $|E_{0}-E_{1}| &lt; \varepsilon$ , then break out of the loop
    Else get  $E_{0} = \min\{E_{0}, E_{1}\}$ . if  $E_{0} = E_{1}$ , then set  $U_{t,0} = U_{t}, U_{t,0} = V_{t}$ .
    End If

    End For

    Step 5:  $U_{t} = U_{t,0}, U_{t} = V_{t,0}$ .
    End For

    Step 6: compute  $M_{V_{N+1}}$  and  $M_{U_{N+1}}$  in Eq. (6).
    Step 7: predict  $R_{N+1}$  using  $R_{N+1} \approx M_{U_{N+1}}^{T} M_{V_{N+1}}$ .
</div>

## 3.3. Complexity analysis

The main computation of learning parameters involves evaluating the object function E in Eq. (10) and its gradients against variables $U _ { t }$ and $V _ { t } ( t \in [ 1 , { N } ] )$ in Eqs. (11) and (12), including computing the mean matrices $\mathtt { M } _ { U _ { t } }$ and $\mathtt { M } _ { V _ { t } }$ in Eq. (6). In each time segment t, the complexity of evaluation E is $o ( \rho _ { R _ { t } } + \rho _ { c } d )$ , where $\rho _ { R _ { t } }$ and $\rho _ { c }$ are the numbers of nonzero entries in matrices $R _ { t }$ and C, respectively. The cost of computing the

## Table 3

Performance on different users of our proposed model TS-PMF $( d = 4 5 )$

<table><tr><td rowspan="2"></td><td colspan="4">1-10</td><td colspan="4">11-20</td><td colspan="4">&gt;20</td></tr><tr><td>PMF</td><td>SocialMF</td><td>T-PMF</td><td>TS-PMF</td><td>PMF</td><td>SocialMF</td><td>T-PMF</td><td>TS-PMF</td><td>PMF</td><td>SocialMF</td><td>T-PMF</td><td>TS-PMF</td></tr><tr><td>Pr1</td><td>0.2684</td><td>0.2711</td><td>0.3919</td><td>0.3730</td><td>0.4878</td><td>0.4878</td><td>0.7439</td><td>0.8415</td><td>0.6316</td><td>0.6316</td><td>0.8684</td><td>0.9211</td></tr><tr><td>Pr3</td><td>0.2026</td><td>0.2079</td><td>0.2261</td><td>0.2207</td><td>0.5000</td><td>0.5163</td><td>0.5813</td><td>0.6870</td><td>0.7105</td><td>0.7281</td><td>0.8158</td><td>0.8947</td></tr><tr><td>Pr5</td><td>0.1642</td><td>0.1621</td><td>0.1627</td><td>0.1681</td><td>0.4854</td><td>0.4927</td><td>0.4780</td><td>0.5220</td><td>0.7105</td><td>0.7053</td><td>0.7632</td><td>0.7895</td></tr><tr><td>Pr10</td><td>0.1039</td><td>0.1068</td><td>0.1027</td><td>0.1051</td><td>0.3659</td><td>0.3683</td><td>0.3439</td><td>0.3598</td><td>0.6184</td><td>0.6079</td><td>0.6132</td><td>0.6211</td></tr></table>

![](/api/attachments/C9KFWJWS/fulltext/images/aaac8a19994e5498c986b0b9637855d55966cb52d162ce29def15ac46e46497d.jpg)  
Fig. 5. Impact of different values of $\negmedspace \lambda _ { c }$ on the performance of user interest prediction with $d = 4 5$

gradients is $o \left( \rho _ { R _ { t } } d + \rho _ { c } ^ { 2 } d / m \right)$ . Then all cost in one iteration is $o \big ( \rho _ { R _ { t } } d + \rho _ { c } d + \rho _ { c } ^ { 2 } d / m + ( N - 1 ) / 2 \big ) \big )$ . Thus, our model is effective for handling large datasets when $R _ { t }$ <sup>þ</sup>and C are sparse.

## 4. Experimental analysis

In this section, comprehensive and systematic analyses are conducted to evaluate the proposed user interest prediction model. The process of collection of the dataset used in the empirical work and the evaluation metrics are presented <sup>fi</sup>rst. Next, we explain the purpose of our experiments in detail. Finally, the performance of our model is compared with results of the other four models; results of the comparison verify the ef<sup>fi</sup>cacy of the proposed model.

## 4.1. Description of the Sina-weibo dataset

In this paper, we use Sina-weibo API to gather users' following links and data of topics of their interest from Oct 29, 2011 to Nov 13, 2011. In this data set, a timestamp is available for each user. After removing users with less than 16 posts, we had 1170 users and 2788 topics. In this dataset, each user has on average 1.57 expressed topics per day and 2.04 following links. We can observe that both the user–user matrix and the user–topic matrix are very sparse.

In this paper, the <sup>fi</sup>rst 15 days' data is used for training and the last day's data for testing. Because the average time of duration of each topic is 2.72 days in our data set, we set $T = 3$ days, and accordingly get $N = 5$

## 4.2. Evaluation metric

Prediction results are evaluated by ranking the topics for all users according to the scores in $R _ { N + 1 }$ . Since users are concerned about the top ranking topics, the metrics of precision in top-n [8] is, therefore, adopted to measure the prediction quality of our proposed approach in comparison with other methods, de<sup>fi</sup>ned as:

$$
\operatorname * {P r} n = \frac {N _ {\text { corr }} (n)}{N _ {u} \times n}\tag{14}
$$

where Pr n is the precision in top-n, and $N _ { u }$ is the number of users in the testing data set. We consider the correct topics of a user as those which appear in users' future posts in the testing data set. $N _ { c o r r } ( n )$ is the number of correct topics in top-n prediction list for users who are in the testing data set.

## 4.3. Purpose of our experiments

Our model is based on the intuition that both the social network structure and the evolution of users' interest affect users' future interest. Our experiments are intended to address the following questions:

1 Do the social network structure and the evolution of users' interest have impact on users' interest in micro-blogging in the future?

2 How do model parameters λ and θ affect the accuracy of prediction?

3 How does our model select an appropriate dimension of latent feature space d?

4 Does the division of temporal sections T affect the resulting performance?

5 Is our model effective for active users, who help improve the social in<sup>fl</sup>uence of micro-blogging?

To answer these questions, we proceed in the following fashion. For the <sup>fi</sup>rst question, we conduct a set of experiments to separately take the social network structure and the evolution of users' interest into account for proving the effectiveness of these factors in shaping future interest of users in micro-blogging. For the second question, we illustrate the impacts of parameters with different values. For the third question, we will perform some further experiments to select the appropriate dimensionality of our proposed model by minimizing the accumulated error. For the fourth question, we will take further experiments to analyze the impact of division of temporal sections on the resulting performance.

The social in<sup>fl</sup>uence of micro-blogging is dependent upon fast fusion of information and the rich user-generated content. Therefore, active users who are keen on publishing posts on trending topics are important for micro-blogging. For the <sup>fi</sup>fth question, it intuitively shows that the performance of active users plays an important role in prediction.

## 4.4. Experimental results

In this sub-section, to demonstrate the usefulness and effectiveness of our proposed model TS-PMF, we compare it with four other models:

1 Probabilistic matrix factorization (PMF): This is the baseline matrix factorization approach proposed in [22], which only uses the user– topic matrix without temporal information.

2 SocialMF: This is the model proposed in [9], which takes the social network into account and uses the user–user matrix and user–topic matrix without temporal information. We set $\lambda _ { C } = 0 . 0 0 1$ for SocialMF in our experiments, which is the optimum value according to the best performance on our data.

3 Temporal probabilistic matrix factorization (T-PMF): This is the model using a series of temporal matrices, in which we just import temporal impact on users' interest into the PMF model.

4 MT1: This is the model presented in [18], using only the users explicitly followed by the target user.

In all the experiments, some parameters setting of our approach are $\beta = 3 , ~ \lambda _ { U } = \lambda _ { V } = 0 . 0 0 0 1$ . And we take the users who have published posts at least on one topic on the 16th day for testing. Other parameters are set as $\lambda _ { c } = 0 . 0 0 1$ and $\theta = 0 . 2$ , which are explained in Sections 4.6 and 4.7.

We perform some further experiments to select the appropriate dimensionality of our proposed model by minimizing the accumulated error value, as shown in Fig. 4. In those experiments, we range the dimension of latent feature space d from 5 to 100 by an interval of $5 ,$ and <sup>fi</sup>nd the best performance at $d = 4 5 ,$ eventually. And we show the experimental results with the dimensionality $d = 1 0 , d = 4 5$ and $d = 5 0$ in Table 2, where we indicate the best performance of those models in bold type, with the same dimensionality d. From Table 2, we can observe that with different dimensionalities, both SocialMF and T-PMF improve the accuracy of prediction in comparison with PMF. That ${ \mathrm { i } } s ,$ friendships and temporal factor are both useful for user interest prediction in micro-blogging. And T-PMF can also improve the precision in comparison with SocialMF, i.e. it is necessary to take the evolution of users' interest into consideration to predict users' interest. More signi<sup>fi</sup>cantly, our proposed model TS-PMF outperforms the other methods except for the precision in top-10 (Pr10). With the dimensionality $d = 4 5$ , our model outperforms them in terms of accuracy by 15.51%, 15.31%, 0.61% and 43.68% relative to PMF, SocialMF, T-PMF and MT1 at top-1, respectively.

Intuitively, increasing d should add more <sup>fl</sup>exibility to the models and improve the results. However, comparing results in Table 2, with the dimensionality increasing more than 45, neither T-PMF nor TS-PMF makes the accuracy increase in comparison with the results of $d = 4 5$ , although they still outperform PMF and SocialMF. That means only increasing d in a certain range can improve the accuracy of prediction results by our proposed model.

## 4.5. Performance on different users

Users are grouped into 3 classes: $\ " 1 - 1 0 \ " , \ \ " 1 1 - 2 0 \ "$ and $" > 2 0 "$ denoting on how many topics they have published posts on the 16th day. The experimental results for different users with dimensionality $d = 4 5$ are shown in Table 3, where we indicate the highest accuracy of those models in bold type, with the same user class; T-PMF outperforms other models on users with the label $" 1 - 1 0 "$ , and TS-PMF has better performance than PMF and SocialMF. TS-PMF greatly improves the accuracy of users with labels $" 1 1 - 2 0 "$ and $" > 2 0 '$ relative to other models, especially improving the precision in top-1 more than 25% in comparison with SocialMF and PMF. Although the performance of TS-PMF for users with different labels is not always the best among all algorithms, our model still generates better predictions than PMF and SocialMF. Furthermore, our model is more effective for predicting interest of active users with a large number of tweets.

## 4.6. Impact of $\lambda _ { c }$ on the results

Parameter $\lambda _ { c }$ controls the impact of the social network on users' interest. Larger values of $\lambda _ { c }$ in Eq. (10) show relatively more in<sup>fl</sup>uence of the social network structure on users' interest in comparison with the user–topic matrix. Fig. 5 compares the precision of our model for different values of $\lambda _ { c }$ for users publishing posts at least on one topic on the 16th day when $d = 4 5 .$ . As shown in Fig. 5, TS-PMF obtains the best performance for $\lambda _ { c } = 0 . 0 0 1$

![](/api/attachments/C9KFWJWS/fulltext/images/03ea2eed4c08a69950b0d238974965589865adbd2e2a7ec43477f3fadd6106d4.jpg)  
Fig. 6. Impact of different values of θ on the performance of user interest prediction with $d = 4 5$

## 4.7. Impact of θ on the results

Parameter θ in Eq. (6) is a weight that indicates how important the previous time points are to the current one, for user-latent feature matrix and topic-latent feature matrix. If $\theta = 0 ,$ our model is the same as T-PMF, which takes only time information into account, and if $\theta = 1$ , we consider that the evolution of users' interest plays a decisive role in the current users' latent feature space and topics latent feature space. $\mathrm { F i g . }$ 6 shows the in<sup>fl</sup>uence of θ for users publishing posts at least on one topic on the 16th day when $d = 4 5$ . We observe that values of θ affect the accuracy of predicting users' interests. From Fig. 6, we can see TS-PMF has its best result for $\theta = 0 . 2$

## 4.8. Impact of T on the results

Parameter T denotes the days for partitioning the data set. In this paper, we set $T = 3$ because of the average time of duration of each topic in our dataset. In addition, we take further experiments to analyze the impact of T on the resulting performance. As is shown in Fig. 7, the X-axis represents the days for partitioning our data set, including 2, 3, 4 and 5 days respectively, and the Y-axis represents the precision of predicting users' interest in the test data. And we can observe that when we set T = 3 days for partitioning data sets, our proposed model achieve the best performance when d = 45.

![](/api/attachments/C9KFWJWS/fulltext/images/75073d819bdecb1fa6a74565ec324cee0ebe25e3174cd47844bdf941d937fe78.jpg)  
Fig. 7. Impact different values of T on the performance of user interest prediction with $d = 4 5$

## 4.9. Prototype system

Fig. 8 shows our prototype system interfaces, which allow users to see not only a list of topics on which a given user has published posts in the past and the ones he will prefer in the future, but also the related posts on the given topic, which appears in the user's topic list.

The upper graph of Fig. 8 gives an example of searching a given user “The vagrant 1885838067”. His interests include costume drama, comic, movie, daily life, Korean current star and so on. Since he focused on costume drama “Introduction of the Princess” and “Each step Escape” for a long time, our model predicts he may continue to prefer them as well as other models. Meanwhile, some of his interests have changed over time. For example, he only paid attention to Korean Current star such as “Girls' Generation” and “U-know” at <sup>fi</sup>rst, and then he showed his interests in TV series of stars such as “Poseidon”. Therefore, our model provides him a TV series “Skip beat” of Korean Current star. Furthermore, he has published posts on “Nokia N9”, “BYD G3”, “Gas station”, “Air quality”, “Highway”, a sightseeing spot named “Zhang jiajie” and “Good trip”. This shows he is interested in some topics about travelling by car. Additionally, some of his friends have been paying attention to a topic named “Posting tweets with mobile on trips”. Our model offers “Posting tweets with mobile on trips” to him. From the above example, we can see that our proposed method can effectively detect users' future interests by considering the social network structure and the evolution of users' interest.

![](/api/attachments/C9KFWJWS/fulltext/images/abdec646805740aee60703dafadbcd9949d69ddbb1fdd98b56f9bb6301f9a6a8.jpg)  
Fig. 8. Search results of our prototype system.

The bottom graph in Fig. 8 gives an example of querying the topic “Epson”, where we can observe some information on the topic, including posters, release time and post content.

As we have mentioned in the paper body, our model accurately forecasts users' liking score for certain programs. With this valuable information, we can recommend these movies to the people whose liking score exceeds a certain threshold, which will increase the programs' viewership and help businesses make better screening policies. For example, based on the users' interest predicted by our model stated above, we can provide a TV series “Skip beat” to some target users, such as “The vagrant 1885838067”. The accurate recommendation not only improves users' satisfaction, but also increases the viewership of “Skip beat”, meanwhile, it helps merchants get more bene<sup>fi</sup>ts. Besides, it is useful for corporations to make effective marketing decisions, for example, proper advertisements may be shown to a given user and businesses can enhance their services to satisfy customers.

## 5. Conclusions and future work

Micro-blogging is one of the most popular social media platforms where the convenience, high update frequency and rich information have attracted millions of active users to join in. Users can publish posts on their daily lives and some trending topics. Trending topics are featured prominently to provide users with an up-to-date glimpse of what is happening in the real world and clearly re<sup>fl</sup>ect users' interests. Users enthusiastically follow other users they are interested in to get relevant information of their interest.

In this paper, we propose a novel model to predict users' interests in micro-blogging to help micro-blogging systems provide users better personalized information and advertising services. Our model is a probabilistic matrix factorization based approach. We present a user interest prediction framework fusing the social network structure and the evolution of users' interest. In microblogging, the rich information and frequent updates make users' interests more extensive and changeable over time, and then make users' latent feature space and topics' latent feature space change over time. Therefore, our model uses exponential decay function to obtain the mean matrix of user-latent feature matrix and the mean matrix of topic-latent feature matrix. The experimental results on Sina-weibo, one of the most popular micro-blogging sites in China, demonstrate that our model can improve the accuracy of predictions of users' interest.

There are several directions future research can take. Firstly, there are some parameters in our proposed model, and different values of those parameters should affect the performance. Therefore, we would like to provide an ef<sup>fi</sup>cient procedure for tuning the parameters automatically, such as Markov Chain Monte Carlo (MCMC) algorithm [13]. Secondly, we may unearth other effective factors to enhance the performance of the proposed model; for example, the retweeting relationships and discussions among users.

## Acknowledgments

This research is supported by the NNSFC grants (no. 61172106, no. 71090402, no. 71002064) and the BJNSF grant (no. 4112062).

## References

[1] A. Ahmed, Y. Low, M. Aly, V. Josifovski, Scalable distributed inference of dynamic user interests for behavioral targeting, in: KDD'11: Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 114–122.

[2] S. Asur, B.A. Huberman, Predicting the future with social media, WI-IAT'10: The 2010 IEEE WIC ACM International Conferences on Web Intelligence and Intelligent Agent Technology, 2010, pp. 492–499.

[3] N. Banerjee, D. Chakraborty, K. Dasgupta, A. Joshi, S. Mittal, S. Nagar, A. Rai, S. Madan, User interests in social media sites: an exploration with micro-blogs, CIKM'09: Proceedings of the 2009 ACM Conference on Information and Knowledge Management, 2009, pp. 1823–1826.

[4] Y. Chen, L. Cheng, An approach to group ranking decisions in a dynamic environment Decision Support Systems 48 (2010) 622–634.

[5] C. Chiu, M. Hsu, H. Lai, C. Chang, Re-examining the in<sup>fl</sup>uence of trust on online repeat purchase intention: the moderating role of habit and its antecedents Decision Support Systems 53 (2012) 835–845.

[6] H. Ma, M.R. Lyu, I. King, Learning to recommend with trust and distrust relationships in: RecSys'09: Proceedings of the 2009 ACM Conference on Recommender Systems, 2009, pp. 189–196.

[7] O. Hinz, M. Spann, Managing information diffusion in Name-Your-Own-Price auctions, Decision Support Systems 49 (4) (2010) 474–485.

[8] J.L. Herlocker, J.A. Konstan, L.G. Terveen, J. Riedl, Evaluating collaborative <sup>fi</sup>ltering recommender systems, ACM Transactions on information systems 22 (1) (2004) 5–53.

[9] M. Jamali, M. Ester, A matrix factorization technique with trust propagation for recommendation in social networks. RecSys'10: Proceedings of the 2010 ACM Conference on Recommender Systems, 2010, pp. 135–142.

[10] A. Java, X. Song, T. Finin, B. Tseng, Why we twitter: understanding microblogging usage and communities, WebKDD/SNA-KDD 2007: Proceedings of the 9th WebKDD and 1st SNA-KDD 2007 Workshop on Web Mining and Social Network Analysis, 2007, pp. 56–65.

[11] H. Kwak, C. Lee, H. Park, S. Moon, What is Twitter, a social network or a news media? WWW'10: Proceedings of the 2010 ACM Conference on the World Wide Web, 2010, pp. 591–600.

[12] L. Xiang, Q. Yuan, S. Zhao, L. Chen, X. Zhang, Q. Yang, J. Sun, Temporal recommendation on graphs via long- and short-term preference fusion, in: KDD'10: Proceedings of the 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2010, pp. 723–731.

[13] L. Xiong, X. Chen, T. Huang, J. Schneider, J.G. Carbonell, Temporal collaborative <sup>fi</sup>ltering with Bayesian probabilistic tensor factorization, in: SAM'10: 10th SIAM International Conference on Data Mining, 2010, pp. 211–222.

[14] Y. Li, Y. Shiu, A diffusion mechanism for social advertising over microblogs, DSS: Decision Support Systems 54 (2) (2012) 9–22

[15] H. Ma, H. Yang, M.R. Lyu, I. King, SoRec: social recommendation using probabilistic matrix factorization, CIKM'08: Proceedings of the 2008 ACM Conference on Information and Knowledge Management, 2008, pp. 931–940.

[16] H. Ma, M.R. Lyu, I. King, Learning to recommend with trust and distrust relationships, RecSys'09: Proceedings of the 2009 ACM Conference on Recommender Systems, 2009, pp. 189–196.

[17] H. Ma, T. Zhou, M.R. Lyu, I. King, Improving recommender systems by incorporating social contextual information, ACM Transactions on Information Systems 29 (2) (2011), (Article 9).

[18] P. Massa, P. Avesani, Trust-aware recommender systems, RecSys'07: Proceedings of the 2007 ACM Conference on Recommender Systems, 2007, pp. 17–24.

[19] Michael Mathioudakis, Nick Koudas, TwitterMonitor: trend detection over the Twitter stream. Proceedings of the 2010 ACM SIGMOD International Conference on Management of Data, 2010, pp. 1155–1158.

[20] N. Nori, D. Bollegala, M. Ishizuka, Interest prediction on multinomial, time-evolving social graphs, IJCAI'11: The Twentieth International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 2011, pp. 2507–2512.

[21] P. Domingos, M. Richardson, Mining the network value of customers, in: KDD'01: Proc. of the 7th ACM SIGKDD Int. Conf. on Knowledge Discovery and Data, 2001, pp. 57–66.

[22] R. Salakhutdinov, A. Mnih, Probabilistic matrix factorization, in: NIPS'07: the 20th Annual Conference on Neural Information Processing Systems, 2007, pp. 1257–1264

[23] R.R. Sinha, K. Swearingen, Comparing recommendations made by online systems and friends, DELOS Workshop: Personalisation and Recommender Systems in Digital Libraries, 2001.

[24] S. Staab, P. Domingos, P. Mika, J. Golbeck, L. Ding, T.W. Finin, A. Joshi, A. Nowak, R.R. Vallacher, Social networks applied, IEEE Intelligent Systems 20(1) (2005) 80–93.

[25] D. Watts, Challenging the in<sup>fl</sup>uentials hypothesis, WOMMA Measuring Word of Mouth 3 (2007) 201–211.

[26] Y. Ding, X. Li, Time weight collaborative <sup>fi</sup>ltering, in: CIKM'05: 14th Conference on Information and Knowledge Management, 2005, pp. 485–492.

[27] Q. Yan, L. Yi, L. Wu, Human dynamic model co-driven by interest and social identity in the microblog community, Physica A: Statistical Mechanics and its Applications 391 (2012) 1540–1545.

[28] L. Zhao, Y. Lu, Enhancing perceived interactivity through network externalities: an empirical study on micro-blogging service satisfaction and continuance intention, Decision Support Systems 53 (2012) 825–834.

[29] C. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, DSS: Decision Support Systems 43 (2007) 460–475.

[30] Z. Xu, R. Lu, L. Xiang, Q. Yang, Discovering user interest on twitter with a modi<sup>fi</sup>ed author-topic model, WI-IAT'11: the 2011 IEEE WIC ACM International Conferences on Web Intelligence and Intelligent Agent Technology, 2010, pp. 422–429.

Hongyun Bao is a Ph.D. candidate in the State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences. She received her B.S. degree in School of Mathematical Sciences from Capital Normal University, China, in 2008. Her research interests include information retrieval and web/text mining.

Qiudan Li (corresponding author) is an Associate Professor in the State Key Laboratory of Management and Control for Complex Systems Institute of Automation Chinese Academy of Sciences. She received a Ph.D. in Computer Science from Da Lian University of Technology, China, in 2004. Her research interests include web mining and mobile commerce applications. Her articles are published in Communications of the AIS, Decision Support Systems, Journal of the American Society for Information Science and Technology, IEEE Transactions on SMC, and Expert Systems with Applications.

Stephen Shaoyi Liao is a Professor at the Department of Information Systems and director of Advanced Transportation Information Systems Research Center, City University of Hong Kong. He is also a Visiting Professor and a Ph.D. Supervisor in USTC and Southwest Jiaotong University. He received a bachelor's degree from Beijing University and a Ph.D. from the University of Aix-Marseille III and Institute of France Telecom. His research focuses on use of IT in e-business systems and transportation systems. His articles have been published in MISO. Decision Support Systems, IEEE Transactions. Communications of the ACM. Information Science. Computer Software and other SCI journals.

Shuangyong Song is a Ph.D. candidate in the State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences. He received his B.S. degree in Biomedical Engineering from Beijing Jiaotong University, China, in 2007. His research interests include information retrieval and web/text mining.

Heng Gao is a Master Candidate in the State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences. He received his B.E. degree in Computer Science from China University of Mining and Technology, China, in 2010. His research interests include information retrieval, web/text mining and community question answering.
