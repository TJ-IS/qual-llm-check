---
otero_id: 2968
otero_key: "M3UAHBSB"
title: "Collaborative error-reflected models for cold-start recommender systems"
authors: "Heung-Nam Kim; Abdulmotaleb El-Saddik; Geun-Sik Jo"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Collaborative error-re<sup>fl</sup>ected models for cold-start recommender systems

Heung-Nam Kim <sup>a,</sup>⁎, Abdulmotaleb El-Saddik <sup>a,c</sup>, Geun-Sik Jo <sup>b</sup>

<sup>a</sup> School of Information Technology and Engineering, University of Ottawa, Canada

<sup>b</sup> Department of Information Engineering, Inha University, Korea

<sup>c</sup> Faculty of Engineering, New York University Abu Dhabi, UAE

## a r t i c l e i n f o

Article history: Received 16 April 2010 Received in revised form 8 December 2010 Accepted 27 February 2011 Available online 4 March 2011

Keywords: Collaborative <sup>fi</sup>ltering Cold start problems Recommender systems

## a b s t r a c t

Collaborative Filtering (CF), one of the most successful technologies among recommender systems, is a system assisting users to easily <sup>fi</sup>nd useful information. One notable challenge in practical CF is the cold start problem, which can be divided into cold start items and cold start users. Traditional CF systems are typically unable to make good quality recommendations in the situation where users and items have few opinions. To address these issues, in this paper, we propose a unique method of building models derived from explicit ratings and we apply the models to CF recommender systems. The proposed method <sup>fi</sup>rst predicts actual ratings and subsequently identi<sup>fi</sup>es prediction errors for each user. From this error information, pre-computed models, collectively called the error-re<sup>fl</sup>ected model, are built. We then apply the models to new predictions. Experimental results show that our approach obtains signi<sup>fi</sup>cant improvement in dealing with cold start problems, compared to existing work.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The prevalence of digital devices and the development of Web 2.0 technologies and services enable end-users to be producers as well as consumers of media content. Even in a single day, an enormous amount of content including digital video, blogging, photography and wikis is generated on the Web. It is getting more dif<sup>fi</sup>cult to make a recommendation to a user about what he/she will prefer among those items automatically, not only because of the huge amount of data, but also because of the dif<sup>fi</sup>culty of automatically grasping the meanings of such data. Recommender systems that have emerged in response to the above challenges provide users with recommendations of items that are likely to <sup>fi</sup>t their needs [2].

One of the most successful technologies among recommender systems is Collaborative Filtering (CF). Numerous on-line companies (e.g., Amazon.com, Net<sup>fl</sup>ix.com, and Last.fm) apply CF to provide recommendations to their customers. CF has an advantage over content-based <sup>fi</sup>ltering, which is the ability to <sup>fi</sup>lter any type of items, such as text, music, videos and photos [11]. Because the <sup>fi</sup>ltering process is only based on historical information of whether or not a given target user has preferred an item before, analysis of the actual content itself is not necessarily required. However, despite its success and popularity, CF encounters serious limitations with quality evaluation, namely the cold start problems.

The cold start problems that can be divided into cold start items and cold start users occur when available data is insuf<sup>fi</sup>cient to enable the user to grasp such data [2]. A cold start item is cause by a new item. In a CF-based recommender system, an item cannot be recommended until a number of users have previously rated it. This is known as the cold start item problem [27]. This item is hardly ever recommended to users due to insuf<sup>fi</sup>cient user opinions. Another notable challenge in recommender systems is the cold start user problem [1,30,31]. A cold start user describes a new user who has joined a CF-based recommender system and has presented few opinions. With this situation, it is often the case that there is no intersection at all between two users, and hence the similarity is not computable. Even when the computation of similarity is possible, it may not be very reliable because of the insuf<sup>fi</sup>cient processed information. Accordingly, the system is generally unable to make high quality recommendations [2]. These problems, particularly for the cold start items, can be partially alleviated by content-based technologies because they provide recommendations by comparing properties or content contained in an item to those of a user's interest items. Therefore, a number of studies have attempted to incorporate content-based techniques into collaborative <sup>fi</sup>ltering [15,20,27]. Although such systems give promise of overcoming the problems, the main drawback to the systems is that <sup>fi</sup>ltering processes generally depend on a type of items (e.g., articles, images, music, and videos); consequently, a system working a particular application domain could not be directly applied to different domains without any modi<sup>fi</sup>cations. Moreover, for some domains it is hard to automatically analyze the underlying content, as well as a user's interest cannot always be characterized by content properties contained in an item [6,7].

In this paper, we address the above issues by introducing a unique method of building models that can be applied to CF recommender systems. Our aim is to build a recommender system derived from explicit ratings so that it can be <sup>fl</sup>exible for any type of items. The proposed method is divided into two phases, an of<sup>fl</sup>ine phase and an online phase. The of<sup>fl</sup>ine phase is a pre-computed model building phase in which most tasks can be conducted. The online phase is either a prediction or recommendation phase in which the models are used. In the model building phase, we <sup>fi</sup>rst determine pre-predicted ratings and subsequently identify the pre-prediction errors for each user. From the error information, error-re<sup>fl</sup>ected models are built. The error-re<sup>fl</sup>ected models that re<sup>fl</sup>ect the average pre-prediction errors of user neighbors and of item neighbors can make accurate predictions in the situation where users or items have few opinions. In addition, in order to reduce the re-building tasks, the errorre<sup>fl</sup>ected models are designed such that the models are effectively updated and users' new opinions are incrementally re<sup>fl</sup>ected, even when users present a new rating feedback.

The subsequent sections are organized as follows: Section 2 brie<sup>fl</sup>y discusses previous studies related to collaborative <sup>fi</sup>ltering. In Section 3, we describe a detailed method of building models. In Section 4, we then provide a description of how the system uses the models for item predictions. In Section 5, an experimental evaluation is presented comparing our approach with existing work. Finally, we present the conclusions and future work.

## 2. Background and preliminaries

In this section, we brie<sup>fl</sup>y explain the concepts used in our research on recommender systems, especially those related to a user-based CF and an item-based CF. CF is based on the fact that “word of mouth” opinions of other people have considerable in<sup>fl</sup>uence on the buyers' decision making [14,28]. If advisors have similar preferences to the buyer, the buyer is much more likely to be affected by their opinions. The most common ways to obtain users' opinions is to use rating information given explicitly or observed implicitly [6,12]. In the case of explicit ratings indicating how relevant or interesting a speci<sup>fi</sup>c item is to a user, users are required to explicitly evaluate an item using like/dislike, thumbs up/down (a binary scale), or numerical values (e.g., a scale of 1–5 points). On the other hand, in the case of implicit ratings, information observed implicitly from users' behaviors is treated as preference indicators, e.g., a user viewed, accessed, listened to, or bought an item [21]. The best use of implicit ratings has been seen in Amazon.com where a user's past purchased items are used to make product recommendations [18].

Although the <sup>fi</sup>eld of CF research has a large number of information <sup>fi</sup>ltering problems, in this paper, we focus on explicit numerical ratings that can be represented as an m×n user–item rating matrix R [26].

## De<sup>fi</sup>nition 1. User–item rating matrix, R.

If there is a list of m users $U { = } \{ u _ { 1 } , u _ { 2 } { , \ldots } , u _ { m } \}$ and a list of n items I = $\{ i _ { 1 } , i _ { 2 } , . . . , i _ { n } \}$ mapping between the user–item pairs and the explicit ratings, then m×n user–item data can be represented as a rating matrix. This matrix is called a user–item rating matrix, R. The matrix rows represent users, the columns represent items and $R _ { u , j }$ represents the rating of user u of item j. Some of the entries are not <sup>fi</sup>lled, as there are items not rated by some users.

In matrix R, an element $R _ { u , j }$ either exists as numerical ordinal scale between $R _ { m i n }$ and $R _ { m a x } ,$ or is empty. If user u rates item j with $R _ { m i n } ,$ it implies he/she does not have any preference for the item j. On the contrary, if user u rates item j with $R _ { m a x }$ it means the item is suited to his/ her preference. If user u has not previously rated item j (i.e., a blank element), we assign ∅ to the value of $R _ { u , j } \ : ( \mathrm { i } . \mathrm { e } . , R _ { u , j } = \emptyset )$ , and ultimately those items $( \mathrm { i } . \mathbf { e } . , R _ { u , ^ { * } } = \emptyset )$ which have not yet been rated by the target user can be considered for recommendation to the target user.

In CF-based recommendation schemes, two approaches have mainly been developed: memory-based CF (also known as userbased CF) and model-based CF [5]. Following the proposal of GroupLens [24], the <sup>fi</sup>rst system generates automated recommendations, user-based CF approaches have seen the widest use in recommender systems. User-based CF uses a similarity measurement between neighbors and a target user to learn and predict preferences toward new items or unrated products by the target user. However, despite the popularity of user-based CF algorithms, they have some serious problems relating to the increasing computation complexity of recommendations as the number of users and items increases. In addition, problems of sparsity due to the insuf<sup>fi</sup>ciency of users' historical information should be seriously considered [25]. In order to improve the scalability and real-time performance of large applications, a variety of model-based recommendation techniques have been developed. Model-based approaches, such as our algorithm, provide item recommendations by <sup>fi</sup>rst developing a pre-computed model [13]. In comparison to user-based approaches, model-based approaches are typically faster in terms of recommendation time, though the method may have an expensive learning or model building process. A new class of modelbased CF, called an item-based CF, has been proposed [9,25] and applied to commercial recommender systems such as Amazon.com [18]. Instead of computing the similarities between users, an itembased CF reviews a set of items that the target user has rated and selects the most similar items based on the similarities between the items.

Usually, user-based and item-based CF systems involve two steps: <sup>fi</sup>rst, the neighbor group, which are users who have a similar preference to the target user (for user-based CF) or the set of items that is similar to the item rated by the target user (for an item-based CF), should be determined by using a variety of similarity computing methods. Based on the group of neighbors, we obtain the prediction values of particular items, estimating how much the target user is likely to prefer the items, and then the top-N items with the highest predicted values of interest to the target user are identi<sup>fi</sup>ed.

## 2.1. Neighborhood formation

The important task in CF-based recommendations is neighborhood formation, because different neighbor users or items lead to different recommendations. Here, neighbors simply mean a group of likeminded users similar to a target user or a set of items similar to those that were previously identi<sup>fi</sup>ed as being preferred by the target user. The number of neighbors may be varied depending on the characteristics of the domains and the application. Since the number also has signi<sup>fi</sup>cant impact on the quality of results from the CF, the recommender systems should determine the size of the neighborhood in order to compute the prediction results effectively [26].

## 2.1.1. User neighborhood

The main goal of neighborhood formation for a user-based CF is to identify the set of user neighbors which is de<sup>fi</sup>ned as the group of users exhibiting preferred items similar to those of the target user. For <sup>fi</sup>nding the nearest neighbors, a variety of similarity methods have been researched, such as the Pearson correlation [24], which is widely used, cosine similarity, weight ampli<sup>fi</sup>cation, inverse user frequency, and default rating [5], including probability-based approaches. According to the results of the selected similarity measure, particular k users with highest similarity are identi<sup>fi</sup>ed as neighbors. Fig. 1 shows examples of calculating the similarity of two users, u and v from a user–item rating matrix R. Finally, for m users, the similarity of users can be represented as an m×m user–user similarity matrix A, where both rows and columns represent users. In matrix $\mathsf { A } , A _ { u , v } ,$ , which represents the u-th user for the v-th user, is set to the similarity value between a pair of users u and v if the corresponding similarity value is greater than the k highest similarity value in the u-th row of A, and 0 otherwise. Non-zero entries of each row, often called k nearest neighbors (KNN), are used to recommend items for each user of the row.

![](/api/attachments/M3UAHBSB/fulltext/images/aa588766ab4714a1e31c78bccfcd2352e0d91072bd71766730871215b2d6d931.jpg)  
Fig. 2. An item–item similarity matrix D used in item-based CF.

![](/api/attachments/M3UAHBSB/fulltext/images/430a25ab155fe62f760e02c0b0d650a20066d0fec513e930427fd5070bd8e8a2.jpg)

![](/api/attachments/M3UAHBSB/fulltext/images/021326841ceb20428a0550f49131983a17b18171275812e34a317858961e28ee.jpg)  
Fig. 1. A user–user similarity matrix A used in user-based CF

## 2.1.2. Item neighborhood

Instead of computing similarities between users, an item neighborhood for an item-based CF is generated by computing similarities between items. The main use of the neighborhood is to identify, for each item, the set of items that is most likely to be preferred by users. For capturing the similarity relationships between pairs of items, Sarwar et al. [25] proposed several similarity measures between pairs of items such as cosine-based similarity, correlation-based similarity and adjusted cosine similarity. The basic idea of computing similarity between two items is to <sup>fi</sup>rst look into users who have rated both of these two items and then to apply one of the similarity measures to calculate a similarity value between the two items [25].

Fig. 2 illustrates computation of the similarity for a pair of items i and j corresponding to the i-th and j-th columns of the rating matrix R. Similar to the user–user similarity matrix A, for n items, the similarity of items can be represented as an n×n item–item similarity matrix D, where the i-th row stores the k′ most similar items to item i. In matrix $D _ { i , j }$ is set to the similarity value between two items i and j if the corresponding similarity value is greater than the k′ highest similarity value in the i-th row of D, and 0 otherwise. Non-zero entries per each row, often called k′ most similar items (MSI), are used to recommend items for the target user [9].

## 2.2. Predictions and recommendations

Once the neighborhood is generated, various methods can be used to combine the ratings of neighbors to compute a prediction value on unrated items for the target user. The preference rating of each neighbor is usually weighted by the similarity value, which is computed when the neighbors are determined. The more a neighbor is similar to a target user or item, the more in<sup>fl</sup>uence he/she has for calculating a prediction value. After predicting how much a target user will like particular items not previously rated by him/her, the top-N item set, the set of ordered items with the highest predicted values is identi<sup>fi</sup>ed and recommended. The target user can present feedback on whether he/she actually likes the recommend top-N items or how much he/she prefers those items as scaled ratings.

## 2.2.1. User-based prediction

In a user-based CF, we can predict the target user's interest in the target item based on its ratings from other similar users. The main idea is that ratings by more similar users contribute more to predicting the target item rating [11]. Formally, the measurement of how much target user u prefers item j is given by:

$$
\stackrel {\vee} {R} _ {u, j} = \overline {{R _ {u}}} + \frac {\sum_ {v \in K N N} \left(R _ {v , j} - \overline {{R _ {v}}}\right) \cdot s i m (u , v)}{\sum_ {v \in K N N} | s i m (u , v) |}\tag{1}
$$

where KNN is a set of k nearest neighbors of user $u ,$ and $R _ { \nu , j }$ is the rating of user v on item j. In addition, $\overline { { R _ { u } } }$ and $\overline { { R _ { \nu } } }$ refer to the average rating of users u and v, and sim(u,v) represents the similarity between users u and v, which can be calculated by a number of different methods, as discussed in Section 2.1.1.

## 2.2.2. Item-based prediction

Essentially, item-based prediction tries to capture how the target user has rated similar items [25]. For predicting a particular item in an item-based CF, we can calculate a weighted average of the user's ratings $R _ { u , j }$ using the similarity between two items as the weight. Formally, we can calculate the predicted rating of target user u for target item j using the following formula:

$$
\stackrel {\vee} {R} _ {u, j} = \frac {\sum_ {i \in M S I} s i m (i , j) \cdot R _ {u , i}}{\sum_ {i \in M S I} | s i m (i , j) |}\tag{2}
$$

where MSI is the set of $k ^ { \prime }$ most similar items to item $j .$ sim(i, j) represents the similarity between items i and j, which can be calculated in the manner mentioned in Section 2.1.2. The main idea behind this prediction is that the weighted rating of items that are similar to the target item is a good estimate of the rating for that item.

## 3. Building collaborative models using pre-prediction errors

In this section, we describe our method of building models, collectively called an error-reflected model, in detail. According to a type of neighbors used in building the model, the error-re<sup>fl</sup>ected model is divided into three classes: a user-based model, an itembased model, and a hybrid model.

In this paper, prior to generating a rating prediction of the items that users have not yet rated, we predict values of the items that the users have previously rated. That is, we validate how accurately the rating of a given user for an item is predicted, compared to an actual rating given by him/her for that item. In this sense, a prediction can be divided into two cases: a prediction of a target user on items that have already been rated by the target user and a prediction of a target user on items that have not yet been rated by the target user. To differentiate the former from the latter, we label the former case a pre-prediction.

## 3.1. Computing pre-predictions

Prior to generating a pre-prediction, we <sup>fi</sup>rst identify k nearest neighbors of each user by using cosine similarity with the inverse user frequency [5] and $k ^ { \prime }$ most similar items of each item by using cosine similarity with the inverse item frequency. For the pre-prediction of the items, we withhold a single selected item for a target user within the entire selection of items he/she rated, and then try to predict its value. In order to compute the pre-prediction value of target user u for item j, we consider not only the rating propensity of users who have similar tastes with user u but also the past rating propensity of user u for items similar to item j. Formally, the measurement of the preprediction is given by:

$$
P _ {u, j} = R _ {k n n (u)} ^ {j} + \frac {\sum_ {i \in M S I _ {u} (j)} \left(R _ {u , i} - R _ {k n n (u)} ^ {i}\right) \times s i m (i , j)}{\sum_ {i \in M S I _ {u} (j)} s i m (i , j)}\tag{3}
$$

where $P _ { u , j }$ is a pre-predicted value of user u on item j and $M S I _ { \mathrm { u } } ( j )$ is a set of most similar items of item $j . ~ R _ { k n n ( u ) } ^ { i }$ and $R _ { k n n ( u ) } ^ { j } ,$ respectively, refer to the average rating of the nearest neighbors of user u for items i and j. Note that if the average rating of the user neighborhood for a certain item is unavailable, we always use the average rating of item j rated by all users instead. sim(i, j) represents the similarity between items i and j, which can be calculated using diverse similarity algorithms such as cosine-based similarity, correlation-based similarity and adjusted cosine similarity [25]. However, we also consider the number of users' ratings of items in generating item-to-item similarities, namely the inverse item frequency. When the inverse item frequency is applied to the cosine similarity technique, the similarity between two items, i and j is measured by Eq. (4):

$$
\operatorname{sim} (i, j) = \frac {\sum_ {u \in \left(U _ {i} \cap U _ {j}\right)} \left(R _ {u , i} \times \log \left(n / f _ {u}\right)\right) \times \left(R _ {u , j} \times \log \left(n / f _ {u}\right)\right)}{\sqrt {\sum_ {u \in U _ {i}} \left(R _ {u , i} \times \log \left(n / f _ {u}\right)\right) ^ {2}} \sqrt {\sum_ {u \in U _ {j}} \left(R _ {u , j} \times \log \left(n / f _ {u}\right)\right) ^ {2}}}\tag{4}
$$

where $U _ { i }$ and $U _ { j }$ refer to a set of users who rated items i and $j ,$ respectively. $R _ { u , i }$ is the rating of user u on item i whereas $R _ { u , j }$ is the rating of user u on item j. The inverse item frequency of user u is de<sup>fi</sup>ned as log(n/f ), where $f _ { u }$ is the number of items rated by user u and n is the total number of items in the system. If user u rated all items, then the value of the inverse item frequency is 0. Likewise, in the inverse user frequency [5], the main concept of the inverse item frequency dictates that users rating numerous items present less contribution with regard to similarity than users rating a smaller number of items [9].

To illustrate a simple example for computing a pre-prediction, consider the following user–item rating matrix R as shown in Table 1. Alice has already rated the movies “Seven,” “JFK,” “Shrek” and “Godzilla,” but she has not yet seen “Titanic” and “AI”. For Alice, the movies for the pre-prediction are those movies that have already been rated by her, $\mathrm { I } _ { \mathrm { A l i c e } } = \{ \mathrm { S e v e n } , \mathrm { J F K } ,$ Shrek, Godzilla}.

Assume that we calculate the prediction value for “JFK” by using Eq. (3). And suppose KNN(Alice), the similar user neighborhood of Alice, and MSI(JFK), the similar item neighborhood of “JFK,” are as follows:

$$
\begin{array}{l} - \text { KNN(Alice) = \{John, Bob\}} \\ - \text { MSI(JFK) = \{(Seven, 0.95), (Godzilla, 0.88), (Titanic, 0.71)\}.} \end{array}
$$

Analyzing the rating for “JFK” of the neighbors of Alice, John rated it with 5 points and Bob rated it with 4 points. Hence, the average rating of the neighborhood $R _ { k n n ( A l i c e ) } ^ { J F K }$ becomes 4.5. In addition, analyzing the rating of Alice for items that are similar to “JFK,” the value is calculated as follows:

$$
\frac {(3 - 3) \times 0 . 9 5 + (5 - 4) \times 0 . 8 8}{0 . 9 5 + 0 . 8 8} = 0. 4 8.
$$

In this calculation, “Titanic” is excluded because Alice has not yet rated it. Finally, we can calculate the pre-predicted value of Alice for “JFK” as follows:

$$
P _ {A l i c e, J F K} = 4. 5 + 0. 4 8 = 4. 9 8.
$$

This implies that the movie $\ " \mathrm { J F K } ^ { \prime \prime }$ is pre-predicted as 4.98 even though the actual rating of Alice on it is 5.

An example of a user–item rating matrix, R.

<table><tr><td></td><td>Seven</td><td>JFK</td><td>Titanic</td><td>Shrek</td><td>AI</td><td>Godzilla</td></tr><tr><td>Alice</td><td>3</td><td>5</td><td></td><td>1</td><td></td><td>5</td></tr><tr><td>Bob</td><td>4</td><td>4</td><td>5</td><td>4</td><td>3</td><td></td></tr><tr><td>John</td><td>2</td><td>5</td><td>4</td><td></td><td></td><td>4</td></tr><tr><td>Dannis</td><td></td><td>1</td><td>2</td><td></td><td>5</td><td>4</td></tr></table>

## De<sup>fi</sup>nition 2. User–item pre-prediction matrix, P.

For an m ×n user–item rating matrix, R, the pre-predictions can be represented as an m×n user–item pre-prediction matrix, P. The matrix rows represent users, the columns represent items, and $P _ { u , j } ,$ $R _ { m i n } { \le } P _ { u , j } { \le } R _ { m a x } ,$ , represents the pre-predicted rating of user u on item j.

Analogous to the rating matrix R, the value $P _ { u , j }$ may be assigned to ∅, indicating user u has not previously rated item j. Occasionally, we cannot compute the pre-prediction due to the following cases: i) the user neighborhood of user u does not exist and ii) the item neighborhood of item j does not exist. If the cases happen, the average rating value of user u is used as $P _ { u , j } .$

## 3.2. Computing pre-prediction errors

Once the predictions for users on items are represented on the preprediction matrix, error of each prediction can be computed by subtracting the pre-predicted value from the actual rating. Given the set of actual and pre-predicted rating pairs $< R _ { u , j } , P _ { u , j } >$ for all actual rating value in the rating matrix R and the corresponding prepredicted value in the pre-prediction matrix P, a prediction error is calculated as:

$$
E _ {u, j} = R _ {u, j} - P _ {u, j}.\tag{5}
$$

Fig. 3 illustrates the process of computing the pre-prediction error. For example, the error of the pre-predicted value of Alice for “JFK,” $E _ { A l i c e J F K } ,$ as mentioned in the previous section, becomes 0.02.

Formally, from matrices R and P, the prediction errors can be represented by a user–item error matrix.

## De<sup>fi</sup>nition 3. User–item error matrix, E.

From the given set of actual rating and pre-predicted value pairs $< R _ { u , j } , \ : P _ { u , j } >$ for all the data in matrices R and P, a user–item error matrix, E, can be <sup>fi</sup>lled with error entries. Each entry, $E _ { u , j } ,$ in E represents the pre-prediction error of the uth user of the jth item. $E _ { u , j }$ is in the range of $\left( R _ { m i n }  – R _ { m a x } \right)$ ) and $\left( R _ { m a x } – R _ { m i n } \right)$ . Some of the entries are not <sup>fi</sup>lled, as there are items that are not rated by some users.

In the case that the pre-prediction was overestimated, the preprediction error value $E _ { u , j }$ becomes negative; on the contrary, in the case that the value was underestimated, $E _ { u , j }$ becomes positive (Fig. 4). If $E _ { u , j } = 0 ,$ it means that the algorithm exactly estimated the actual rating. The closer to 0 the value approaches, the higher the accuracy of a pre-prediction value. A pre-prediction error can be analyzed as follows:

$- \ R _ { u , j } { < } P _ { u , j }$ (overestimation): In the case of the overestimation, the pre-predicted value is estimated as being higher than the actual rating value of the user. This is the result of the prediction based on the rating tendency of similar users with target user u and the past rating tendency of target user u for items that are similar to item j. Considering this point, with respect to a new prediction of item j for a certain user similar to the target user u, it may be necessary to slightly decrease the value predicted. In addition, in the case of a new prediction of the target user u for items similar to item j, it may also be necessary to slightly decrease the value predicted.

$R _ { u , j } { > } P _ { u , j }$ (underestimation): Contrary to the overestimation, it may be necessary to slightly increase the predicted value with respect to a new prediction for the case of the underestimation.

## 3.3. Building error-reflected models

As mentioned in the previous section, the pre-prediction error of a target user is the result that re<sup>fl</sup>ects the opinion of like-minded users and the target user's own rating tastes. Therefore, pre-prediction errors of users similar to a target user on a certain item may contain valuable information to make a prediction of the target user for that item. Likewise, pre-prediction errors of a target user for items that are similar to a certain item may be helpful to estimate the rating of the target user for that item. In fact, there are recent studies [4,10,16,22] that have made attempts to utilize pre-predictions to CF recommender systems. Similar to their motivation, the fundamental assumption of our study is that there are systematic and thus exploitable preprediction errors for predicting items that have not yet been rated by the target user.

Theoretically, the error matrix E itself can be used for a new prediction. Intuitively, however, if a pre-prediction value is accurate, it implies that the pre-prediction process accurately re<sup>fl</sup>ects the tendency of the user's past ratings on similar items and the tendency of similar other users' ratings on the same items. On the contrary, if a pre-prediction value appears to be of a high deviation from a corresponding actual rating, there may be noise information used in making the prediction. Therefore, to avoid in not only increasing unnecessary computation cost but also including unnecessary noise information, the model is built by the only data within a predetermined threshold (θ). Note that the prediction error value becomes negative in the case of overestimation whereas it becomes positive in the case of underestimation.

![](/api/attachments/M3UAHBSB/fulltext/images/880478aa65945b5dba45e147526f34e3ac92dfa7aea9dbdadca7158be5adf5a2.jpg)  
Fig. 3. The process of computing a pre-prediction error. The pre-prediction error can be calculated by subtracting the pre-prediction value from the actual rating.

Table 3  
![](/api/attachments/M3UAHBSB/fulltext/images/249e1ea2f2d0069110e4499e11094d3039d006e50394e52b4424df2f1347e034.jpg)  
Fig. 4. Overestimation and underestimation of a pre-prediction value.

Therefore, we select the elements of the error matrix E that satisfy the following conditions:

$$
\left| \mathrm{E} _ {\mathrm{u}, \mathrm{j}} \right| <   \theta , \text { for } \mathrm{R} _ {\mathrm{u}, \mathrm{j}} \neq \varnothing .\tag{6}
$$

The method of building models that are re<sup>fl</sup>ected by the prediction errors can be divided into three approaches: a user-based approach, an item-based approach, and a hybrid approach.

## 3.3.1. The user-based error-reflected model

The user-based error-re<sup>fl</sup>ected model is built by utilizing the preprediction errors of similar user neighbors with the target user u for a certain item. The built model can be represented as an m×n user– item matrix $\widehat { \mathbf { E } } ^ { ( 6 ) }$ . The matrix rows represent users, the columns represent items and jth column of uth row implies the average error of the pre-prediction on similar users' rating of the target user u for item j, as de<sup>fi</sup>ned in Eq. (7)

$$
\stackrel {\wedge} {E _ {u, j} ^ {(\theta)}} = \frac {\sum_ {v \in K N N _ {j} ^ {\theta} (u)} E _ {v , j}}{\operatorname{card} \left(K N N _ {j} ^ {\theta} (u)\right)}\tag{7}
$$

where $K N N _ { j } ^ { \theta } ( u )$ denotes the set of users whose absolute value of the pre-prediction error for item j is less than θ among the similar neighbors of the target user u. In addition, card(KNN<sup>θ</sup>(u)) refers to the cardinality of the set KNN<sup>θ</sup>(u) (i.e., the number of elements in the set).

For example, assume that the pre-prediction errors for Table 1 are shown in Table 2. If an error threshold value θ is 0.8 (θ=0.8), and the size of the user neighborhood is $2 \ : ( k = 2 )$ , then the average of the preprediction errors of Alice's neighbors for $" \mathrm { T i t a n i c } "$ can be calculated from the given values $E _ { B o b , T i t a n i c } = 0 . 7$ and $E _ { J o h n , T i t a n i c } = - 0 . 4$

$$
\hat {E} _ {A l i c e, T i t a n i c} ^ {(0. 8)} = (0. 7 - 0. 4) / 2 = 0. 1 5
$$

In an analogous fashion, $\hat { E } ^ { ( 0 . 8 ) } { } _ { A l i c e , A I }$ of Alice for “AI” is calculated as $- 0 . 0 2$ . In the case of Bob, it is possible to compute that $\hat { E } _ { B o b , G o d z i l l a } ^ { ( 0 . 8 ) }$ for “Godzilla” from KNN(Bob)={Alice, Dannis}. However, the prediction error value of Alice for “Godzilla” is 0.9, which is greater than the prediction error value of Dannis is selected. Finally, the user-based error-re<sup>fl</sup>ected model of Table 2 can be built as shown in Table 3.

## 3.3.2. The item-based error-reflected model

The item-based error-re<sup>fl</sup>ected model is built using the preprediction errors of the target user u for the items that are similar to the target item. This method is similar to the method of building the user-based error-re<sup>fl</sup>ected model. The difference is merely that the similar item neighborhood is used instead of the user neighborhood. The item-based error-re<sup>fl</sup>ected model can also be represented as an m×n user–item matrix $\check { \mathbf { E } } ^ { ( 6 ) }$ . The matrix rows represent users, the columns represent items and jth column of uth row implies the average of the pre-prediction errors of user u for items similar to item j, as de<sup>fi</sup>ned in Eq. (8).

An example of a user–item prediction error.

<table><tr><td></td><td>Seven</td><td>JFK</td><td>Titanic</td><td>Shrek</td><td>AI</td><td>Godzilla</td></tr><tr><td>Alice</td><td>-0.3</td><td>0.02</td><td></td><td>-0.4</td><td></td><td>0.9</td></tr><tr><td>Bob</td><td>0.1</td><td>-2</td><td>0.7</td><td>2</td><td>-0.02</td><td></td></tr><tr><td>John</td><td>-0.15</td><td>0.2</td><td>-0.4</td><td></td><td></td><td>-0.3</td></tr><tr><td>Dannis</td><td></td><td>-2</td><td>0.5</td><td></td><td>-0.03</td><td>0.6</td></tr></table>

$$
\stackrel {\vee} {E _ {u, j} ^ {(\theta)}} = \frac {\sum_ {i \in M S I _ {u} ^ {\theta} (j)} E _ {u , i}}{c a r d (M S I _ {u} ^ {\theta} (j))}\tag{8}
$$

where $M S I _ { u } ^ { \theta } ( j )$ denotes the set of items whose absolute value of the pre-prediction errors for user u is less than θ among the similar items of the target item i. And card(MSI<sup>θ</sup>(j)) is the number of elements in the set.

Let us calculate the average of the prediction errors of Alice for similar items to “Titanic” in Table 2. The prediction error of Alice for “Seven” and “JFK” that are similar to “Titanic” is $E _ { A l i c e , S e v e n } = - 0 . 3$ and $E _ { A l i c e , J F K } = 0 . 0 2$ , respectively. Therefore, $\check { E } ^ { ( 0 . 8 ) } { } _ { A l i c e , T i t a n i c }$ can be calculated as follows:

$$
\check {\mathrm{E}} _ {A l i c e, T i t a n i c} ^ {(0. 8)} = (- 0. 3 + 0. 0 2) / 2 = - 0. 1 4.
$$

If the case of MSI(AI)={Titanic, Shrek, Godzilla}, then $\check { \mathrm { E } } _ { A l i c e , A I } ^ { ( 0 . 8 ) }$ of Alice for $" A ^ { \prime \prime }$ is calculated as 0.4. Since the prediction error of Alice for “Godzilla” is $0 . 9 , E _ { A l i c e , G o d z i l l a } = 0 . 9$ , it is not re<sup>fl</sup>ected from calculation. In the case of John for ${ } ^ { \mathfrak { u } } \mathrm { A l } , { } ^ { \mathfrak { v } } \check { E } _ { J o h n , A I } ^ { ( 0 . 8 ) }$ is calculated as $\check { E } _ { J o h n , A I } ^ { ( 0 . 8 ) } = - 0 . 3 5$ from $E _ { J o h n , T i t a n i c } = - 0 . 4$ and $E _ { J o h n , G o d z i l l a } = - 0 . 3$ . Finally, the item-based errorre<sup>fl</sup>ected model of Table 2 can be built as Table 4.

## 3.3.3. The hybrid error-reflected model

The hybrid error-re<sup>fl</sup>ected model, which is represented as m×n user–item matrix $\hat { \mathbf { H } } ^ { ( 6 ) }$ , is built by unifying the user-based model and the item-based model. The entry in $\mathbf { \hat { H } } ^ { ( \theta ) }$ is <sup>fi</sup>lled as the value that is close to 0, but is not 0 among the values of jth column of uth row in $\widehat { \mathbf { E } } ^ { ( 6 ) }$ and $\check { \mathbf { E } } ^ { ( 6 ) } .$ Formally, $\hat { H } _ { u , j }$ is de<sup>fi</sup>ned as in Eq. (9).

$$
\hat {H} _ {u, j} = \left\{ \begin{array}{l} \stackrel {{\wedge}} {{E}} _ {u, j} \text {if} (| \stackrel {{\vee}} {{E}} _ {u, j} | \geq | \stackrel {{\wedge}} {{E}} _ {u, j} | \text {and} \stackrel {{\wedge}} {{E}} _ {u, j} \neq 0) \text {or} (\stackrel {{\vee}} {{E}} _ {u, j} = 0) \\ \stackrel {{\vee}} {{E}} _ {u, j} \text {if} (| \stackrel {{\vee}} {{E}} _ {u, j} | <   | \stackrel {{\wedge}} {{E}} _ {u, j} | \text {and} \stackrel {{\vee}} {{E}} _ {u, j} \neq 0) \text {or} (\stackrel {{\wedge}} {{E}} _ {u, j} = 0) \\ 0 \quad \text {otherwise} \end{array} \right..\tag{9}
$$

From two examples in Tables 3 and 4, the hybrid model uni<sup>fi</sup>ed two models can be built as Table 5.

An example of the user-based error-re<sup>fl</sup>ected model.

<table><tr><td></td><td>Seven</td><td>JFK</td><td>Titanic</td><td>Shrek</td><td>AI</td><td>Godzilla</td></tr><tr><td>Alice</td><td>0</td><td>0</td><td>0.15</td><td>0</td><td>-0.02</td><td>0</td></tr><tr><td>Bob</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.6</td></tr><tr><td>John</td><td>0</td><td>0</td><td>0</td><td>-0.4</td><td>-0.02</td><td>0</td></tr><tr><td>Dannis</td><td>-0.05</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td></tr></table>

An example of the item-based error-re<sup>fl</sup>ected model

<table><tr><td></td><td>Seven</td><td>JFK</td><td>Titanic</td><td>Shrek</td><td>AI</td><td>Godzilla</td></tr><tr><td>Alice</td><td>0</td><td>0</td><td>-0.14</td><td>0</td><td>-0.4</td><td>0</td></tr><tr><td>Bob</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.4</td></tr><tr><td>John</td><td>0</td><td>0</td><td>0</td><td>-0.12</td><td>-0.35</td><td>0</td></tr><tr><td>Dannis</td><td>0.6</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td></tr></table>

## 3.3.4. Error-reflected models for cold start problems

As clearly discussed in [27], for cold start users and cold start items, recommender systems are generally unable to provide high quality recommendations. With respect to the cold start users, they should be encouraged to continuously provide their opinions because they do not have enough rating information. However, inaccurate predictions from the insuf<sup>fi</sup>ciency of the users' historical information lead them to undermine the credibility of the system, and thus, cause their deviation from the system. Likewise, the cold start items can hardly be recommended compared to items which have suf<sup>fi</sup>cient users ratings. Considering these points, a differentiated strategy is necessary to generate the prediction for both of the cold start users and items.

Since a cold start item has a few ratings given by users, we take into consideration all users who rated the cold start item when building the user-based model for such item. Analogously, with respect to a cold start user, because he/she has rated insuf<sup>fi</sup>cient items, most of items similar to a target item may not be rated by him/ her. Rather than similar items, therefore, we consider all items rated by the cold start user when building the item-based model for that user. Formally, the error-re<sup>fl</sup>ected models of cold start users and items are built by revising Eqs. (7) and (8). That is, the user-based model and item-based model respectively use Eqs. (10) and (11), respectively.

$$
\stackrel {\wedge} {E _ {u, j} ^ {(\theta)}} = \frac {\sum_ {v \in U _ {j}} E _ {v , j}}{\operatorname{card} (U _ {j})} \text {   if   } j \in C S I\tag{10}
$$

$$
E _ {u, j} ^ {\vee} = \frac {\sum_ {i \in I _ {u}} E _ {u , i}}{c a r d (I _ {u})} \text {   if   } u \in C S U\tag{11}
$$

where CSU and CSI are sets of cold start users and cold start items, respectively. In addition, U is a set of users who has rated item j and $I _ { u }$ is a set of items that has been rated by user u; thus, card(U ) and card $\left( I _ { u } \right)$ are the numbers of elements of the sets $U _ { j }$ and $I _ { u } ,$ respectively.

## 4. Applying collaborative models to recommender systems

Fig. 5 illustrates our method with two phases: an of<sup>fl</sup>ine phase and an online phase. The of<sup>fl</sup>ine phase is a building model phase as explained in Section 3 and the online phase is a prediction phase using the error-re<sup>fl</sup>ected models.

## 4.1. Generating a prediction

The <sup>fi</sup>nal step in a collaborative <sup>fi</sup>ltering is the process of generating the prediction by attempting to guess the rating that a user would provide for an item. In collaborative recommender

## Table 5

An example of the hybrid error-re<sup>fl</sup>ected model.

<table><tr><td></td><td>Seven</td><td>JFK</td><td>Titanic</td><td>Shrek</td><td>AI</td><td>Godzilla</td></tr><tr><td>Alice</td><td>0</td><td>0</td><td>-0.14</td><td>0</td><td>-0.02</td><td>0</td></tr><tr><td>Bob</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.4</td></tr><tr><td>John</td><td>0</td><td>0</td><td>0</td><td>-0.12</td><td>-0.02</td><td>0</td></tr><tr><td>Dannis</td><td>-0.05</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td></tr></table>

systems, it is crucial to accurately predict how much a certain user prefers a certain item based on historical information as this directly in<sup>fl</sup>uences the decision making of the users for purchasing, selecting or watching. In addition, processing time required to generate prediction is also an important issue. As noted previously, the proposed CF approach constructs the error-re<sup>fl</sup>ected models which can be accomplished of<sup>fl</sup>ine, prior to online prediction or recommendation. Since most tasks can be conducted in the of<sup>fl</sup>ine phase, the system can result in fast online performance. The salient concept behind our prediction scheme is that prediction errors derived from similar users and similar items can help in predicting a user similar to the users on an item similar to the items. The online prediction applied for each constructed model can be divided into three methods.

The <sup>fi</sup>rst approach is a method of applying the user-based error re<sup>fl</sup>ected model to the prediction. The basic concept of this method is to re<sup>fl</sup>ect whether the pre-predictions of similar neighbors for the target item are overestimated or underestimated. Formally, the value of target user u for item j, ${ \check { R } } _ { u , j } ^ { } ,$ is computed by:

$$
\stackrel {\vee} {R} _ {u, j} = R _ {k n n (u)} ^ {j} + \stackrel {\wedge} {E} _ {u, j}\tag{12}
$$

where $\hat { E } _ { u , j }$ is the value of the uth row of the jth column in the userbased error-re<sup>fl</sup>ected model, Ê and $R _ { k n n ( u ) } ^ { j }$ refers to the average rating of neighborhood of user u for item j. If the average rating of the neighborhood for item j is unavailable, the average rating value of item j rated by all users is used instead. For example, the rating value of Alice for “Titanic,” ${ \check { R } } _ { A l i c e , T i t a n i c } ,$ , in Table 1 is predicted as 4.65 from the average rating of similar users $R _ { k n n ( A l i c e ) } ^ { \mathrm { T i t a n i c } } = 4 . 5$ and the value in the user-based error-re<sup>fl</sup>ected mode $\hat { E } _ { A l i c e , T i t a n i c } ^ { ( 0 . 8 ) } = 0 . 1 5$ as described in Table 3.

For the second approach, we apply the item-based error re<sup>fl</sup>ected model to the online prediction. This approach re<sup>fl</sup>ects whether prepredictions of the target user of items similar to the target item are overestimated or underestimated. Formally, the measurement of how much the target user u prefers item j is given by:

$$
\stackrel {\vee} {R} _ {u, j} = R _ {k n n (u)} ^ {j} + \stackrel {\vee} {E} _ {u, j}\tag{13}
$$

where $\check { E } _ { u , j }$ is the value of the uth row for the jth column in the itembased error-re<sup>fl</sup>ected model, Ě. Applying this way, the predicted value of Alice for “Titanic”, ${ \check { R } } _ { A l i c e , T i t a n i c } ,$ is calculated as 4.36 from the average rating of similar users, $R _ { k n n ( A l i c e ) } ^ { \mathrm { T i t a n i c } } = 4 . 5$ , and the value in the item-based error-re<sup>fl</sup>ected model $\check { E } _ { A l i c e , T i t a n i c } ^ { ( 0 . 8 ) } = - 0 . 1 4$ as described in Table 4.

Finally, the measurement using the hybrid error-re<sup>fl</sup>ected model is de<sup>fi</sup>ned as:

$$
\stackrel {\vee} {R} _ {u, j} = R _ {k n n (u)} ^ {j} + \stackrel {\wedge} {H} _ {u, j}\tag{14}
$$

where the value of the uth row for the jth column in the hybrid model, Ĥ. Since $| \hat { E } _ { A l i c e , T i t a n i c } ^ { ( 0 . 8 ) } | > - \check { E } _ { A l i c e , T i t a n i c } ^ { ( 0 . 8 ) } |$ in the previous example, in this case, Ř can be predicted as 4.36.

## 4.2. Model incremental updates

Model-based CF is generally faster in recommendation time compared to memory-based CF due to the advantageous aspect of prior use of the pre-computed model [13]. However, this approach tends to require expensive learning time for building a model. Moreover, once the model is built, it is dif<sup>fi</sup>cult to immediately re<sup>fl</sup>ect users' feedback despite its signi<sup>fi</sup>cance in the recommender system [7]. In other words, the new information of user preference for the items is dif<sup>fi</sup>cult to re<sup>fl</sup>ect until the model is re-built. Generally, building, renewing or rebuilding the model is not frequently considered due to the time consuming process. Accordingly, the ef<sup>fi</sup>cient method of rebuilding the model is required.

![](/api/attachments/M3UAHBSB/fulltext/images/6fdb3be1db570075e35013d5c1bf45ecda4a10b5d329869248aaa348e7a926c5.jpg)  
Fig. 5. An overview of the proposed approach for item recommendations.

In order to alleviate the weak points of model-based CF, the proposed approach is designed such so that the model is updated effectively as illustrated in Fig. 6. In addition, users' new opinions are re<sup>fl</sup>ected incrementally, even when users present explicit feedback. For example, we assume that the system predicted the rating of Alice for movie “Titanic” as 4.36 and recommended it to Alice. If Alice provided 4.0 as explicit feedback of her actual rating after watching the movie, then the new prediction error can be calculated from the actual rating and the predicted value as follows:

$$
R _ {\text { Alice }, \text { Titanic }} - \check {R} _ {\text { Alice }, \text { Titanic }} = 4. 0 - 4. 3 6 = - 0. 3 6.
$$

The basic concept of measuring the new prediction error is the same as that of measuring the pre-prediction error. In the case where users present explicit feedback about the prediction, the models can easily update the error value which is computed by subtracting the predicted value from feedback rating. Therefore, the proposed method can use the updated information in the process of any further new predictions as well as enhance the quality of recommendations regarding user preferences. We believe our incremental update of the models is much more attractive and particularly ef<sup>fi</sup>cient for cold start users before rebuilding process of the models.

## 5. Experimental evaluations

In this section, we empirically evaluate the proposed prediction methods using the error-re<sup>fl</sup>ected models and compare those performances against the performances of the benchmark algorithms. To this end, we implemented a user-based CF algorithm, wherein the similarity is computed by the well-known Pearson correlation coef<sup>fi</sup>cient (denoted as UserCF) [5], and the item-based CF approach which employs cosine-based similarity (denoted as ItemCF) [25]. The performance applied the user-based model (denoted as UErrorCF), the item-based model (denoted as IErrorCF), and the hybrid model (denoted as HErrorCF) were evaluated in comparison with the benchmark algorithms.

## 5.1. The dataset and evaluation metric

Experimental data comes from MovieLens, a web-based research recommender system (www.movielens.org). The dataset used in this paper is 100 k ratings dataset in MovieLens containing 100,000 ratings of 1682 movies rated by 943 users in the system (943 rows and 1682 columns of a user–item matrix R). This dataset is publicly available. We used two different training data: full training dataset and cold start training dataset. First, for the full dataset that includes all available ratings of users, the entire data was divided into two groups; 80% of the data (80,000 ratings) was used as a training set and 20% of the data (20,000 ratings) was used as a test set. A <sup>fi</sup>ve-fold cross validation scheme was used. This dataset is used to examine the quality of the prediction no matter whether users or items have suf<sup>fi</sup>cient ratings or not. Second, for the cold start dataset, we arti<sup>fi</sup>cially generated two groups that satisfy cold starting conditions because the original dataset contains a minimum of 10 ratings per user. The <sup>fi</sup>rst group contains 100 users who have three ratings per user (the number of items rated by each user) and the second group contains 100 users who have <sup>fi</sup>ve ratings per user.

In order to measure the accuracy of the predictions, we adopted the mean absolute error (MAE) that was widely used for the statistical accuracy measurements in the diverse algorithms [12]. The mean absolute error of user u for N items in the test data is de<sup>fi</sup>ned as:

$$
M A U E (u) = \frac {\sum_ {j = 1} ^ {N} | R _ {u , j} - \overset {\vee} {R} _ {u , j} |}{N}\tag{15}
$$

where $< R _ { u , j } , \check { R } _ { u , j } >$ is the actual/predicted rating pairs of user u in the test data. Finally, the MAE of all M users in the test set is computed as:

$$
M A E = \frac {\sum_ {u = 1} ^ {M} M A U E (u)}{M}.\tag{16}
$$

![](/api/attachments/M3UAHBSB/fulltext/images/cbcacb3dc79d5ad99128125bdf73343a40d6c42a21f816f729376ad8de9f1782.jpg)  
Fig. 6. Updating the error models incrementally by using user feedback.

## 5.2. Parameter tuning experiments

In this section, we present detailed experimental results according to three parameters: the size of user neighborhood k, the size of item neighborhood k′ and the error threshold θ.

## 5.2.1. Accuracy of the pre-prediction according to neighborhood size

The pre-prediction is in<sup>fl</sup>uenced by the size of the user neighborhood, KNN, and the size of the item neighborhood, MSI. Accordingly, for building accurate prediction error models, we should <sup>fi</sup>rst determine a proper size of the user neighborhood k and the item neighborhood k′, respectively. Hence, in this section, we examined the accuracy of the pre-prediction in order to choose optimal values for the number of nearest neighbors and most similar items.

First, we measured MAE of the pre-prediction according to the variation of the item neighborhood k′. According to previous studies, we set the size of the user neighborhood k to 50 (k=50). The experimental result is depicted in Fig. 7 (left graph). It can be observed from the graph that the size of the item neighborhood affects the prediction quality. The quality of the pre-prediction improved as k′ value was increased from 10 and 60, and after this value, the curve tends to become <sup>fl</sup>at. We also observed that the MAE value increases after the item neighborhood size of 80. These results indicate that when the item neighborhood size is too small, the accuracy of the pre-prediction is remarkably decreased. In addition, too large of a size can also negatively impact the accuracy.

In the subsequent experiment, we continued to examine the accuracy by changing the number of user neighbors k. During this experiment, k′ was set to 60 according to the previous result. As shown in Fig. 7 (right graph), the number of the neighbor users also affected the pre-prediction. However, unlike the size of the item neighborhood, the curve of the graph tends to be <sup>fl</sup>at at the relatively small size of the user neighborhood. For example, MAE considerably decreases as the size of the user neighborhood increases from 10 to 20; beyond this point, any further increase of the neighborhood size did not affect the accuracy even though the slight variation of MAE values appeared. When the neighborhood size was 10, we found many cases that nearest users of a target user have not rated a target item yet while the pre-prediction of the target user on the target item was generated. This fact might affect the result that the accuracy of the pre-prediction becomes worse when the size of the user neighborhood is small.

## 5.2.2. Experiments with the error threshold

In this section, we investigate the effect of an error threshold on the performance of the prediction. As described in Section 3.3, we expected that the threshold θ could be a signi<sup>fi</sup>cant factor affecting the quality of the prediction in our study because different error-re<sup>fl</sup>ected models (i.e., Ê<sup>(θ)</sup> and Ě<sup>(θ)</sup>) are built depending on the threshold. So, we measured MAE of the prediction according to the θ value variation from 0.2 to 2.0. Based on the previous experiment, the size of the user neighbors and the item neighbors are set to 50 and 60, respectively (k=50, k′=60).

Fig. 8 illustrates the variation of MAE for UErrorCF, IErrorCF and HerrorCF. It can be observed from the graph that the three methods demonstrate similar types of charts. In the case of UErrorCF, the downward curve appeared until θ value became 1.2, in the case of IErrorCF, the curve appeared until θ value bacame 1.6 and in the case of HerrorCF, the curve appeared until θ value became 1.4, respectively. After those values, the upward curves gradually appeared in the graph. That is, a low threshold value discarded more pre-prediction errors, and thus, the three methods obtained the poor prediction quality because remaining pre-prediction errors were not suf<sup>fi</sup>cient to build the error-re<sup>fl</sup>ected models. Contrarily, a high threshold value included unnecessary noise information that could give negative in<sup>fl</sup>uence on accuracy. When the threshold is 1.4, the models can be built by eliminating approximately 10,000 pieces of super<sup>fl</sup>uous information; consequently, UErrorCF, IErrorCF and HErrorCF can provide the enhanced prediction quality.

![](/api/attachments/M3UAHBSB/fulltext/images/02ec03e7747c91b2954e9ceb097b12ecb9ec7a819bef2d906ea81af8b3ab1b73.jpg)

![](/api/attachments/M3UAHBSB/fulltext/images/546fb10f939b583c5ea0a09cced55ae7d51aac34585e71c35016353a8199a7a8.jpg)  
Fig. 7. MAE according to variation of user neighbor size and item neighbor size used in generating a pre-prediction

![](/api/attachments/M3UAHBSB/fulltext/images/ff593ff544a25341d935f769fb7513fe529f6783cfd4609d511bbcee6deb3311.jpg)  
Fig. 8. MAE according to variation of the error threshold.

Examining the best prediction quality of the three methods, UerrorCF, IErrorCF and HerrorCF obtains an MAE of 0.7584 (θ=1.2), 0.7556 $( \theta = 1 . 6 )$ , and 0.7543 (θ=1.4), respectively. Based on this experiment result, in the subsequent experiments we selected 1.2, 1.6, and 1.4 as the error threshold of UErrorCF, IErrorCF and HerrorCF, respectively. That is, for UErrorCF, model $\hat { \mathbf { E } } ^ { ( 1 . 2 ) }$ was used whereas model $\check { \mathbf { E } } ^ { ( 1 . 6 \bar { ) } }$ was used for IErrorCF. In the case of HErrorCF, we used the model uni<sup>fi</sup>ed $\widehat { \mathbf { E } } ^ { ( 1 . 4 ) }$ and $\check { \mathbf { E } } ^ { ( 1 . 4 ) }$

## 5.3. Comparison with other methods

In this section, we present detailed experimental results in comparison with the benchmark methods. The performance comparison is divided into three dimensions. The accuracy of the prediction is <sup>fi</sup>rst evaluated, and then, the accuracy of the prediction to the cold start problems is evaluated. Finally, we compare computational complexity with related studies.

## 5.3.1. Comparison of the prediction accuracy

As noted in a number of previous studies, the number of neighbors has signi<sup>fi</sup>cant impact on the prediction accuracy of neighborhood-based algorithms [25,26]. Therefore, different numbers of user or item neighbors from 10 to 100 were used for the prediction generation.

a  
![](/api/attachments/M3UAHBSB/fulltext/images/7690ab8c15b9c9cca7598b4c1c8b1571c8407b1d4946b9fe46a201a9c111be46.jpg)  
b

Fig. 9(a) illustrates MAE of UserCF and UErrorCF with respect to the variation in the user neighborhood size. In UErrorCF, the user neighborhood size denotes the number of nearest neighbors k that is exploited for building $\widehat { \mathbf { E } } ^ { ( 6 ) }$ in Eq. (7). In the experimental results, at most neighborhood size, the overall prediction accuracy of UserCF appears to be better than that of UErrorCF. However, we found that the prediction accuracy of UErrorCF is superior to that of UserCF when the neighborhood size is small $( \mathbf { e } . \mathbf { g } . , k = 1 0 )$ . This result can imply that UErrorCF can provide a more accurate prediction performance than UserCF when the information data is sparse or available data for users is relatively insuf<sup>fi</sup>cient.

We continued to examine the prediction accuracy of ItemCF and IErrorCF. In IErrorCF, the item neighborhood size denotes the number of most similar items k′ that is exploited for building $\check { \mathbf { E } } ^ { ( 6 ) }$ in Eq. (8). In the rating prediction for IErrorCF, we set the user neighborhood to 50 in order to calculate the average rating of the user neighborhood for a certain item in Eq. (13). Fig. 9(b) shows MAE obtained by ItemCF and IErrorCF with respect to the variation of the item neighborhood size. The result demonstrates that, at all neighborhood size levels, IErrorCF provides more accurate predictions than ItemCF.

ItemCF elevates the prediction accuracy as the neighborhood size increases from 10 to 50; after this value, the accuracy decreased slightly. On the contrary, in the case of IErrorCF, after the size passed a certain level $( k ^ { \prime } = 4 0 – 5 0 )$ , the variation of the accuracy almost never occurs. Comparing MAE obtained by the user-based approaches and the item-based approaches in a neighborhood size of 10, the accuracy of IErrorCF and ItemCF is remarkably worse than UserCF and UErrorCF. These results may be affected by the fact that the item-based approaches essentially attempt to capture how the target user has rated the similar items. In the case of a too-small size of the item neighborhood, the items similar to a certain item were not rated by the target user, and thus, it was more dif<sup>fi</sup>cult to predict the rating of the item for him/her.

Table 6 summarizes the comparison of the best results achieved by the <sup>fi</sup>ve methods. The comparison results of MAE show that the methods based on the proposed models (such as UErrorCF, IErrorCF, and HErrorCF) provide slightly worse accuracy than UserCF; however, the difference appears insigni<sup>fi</sup>cant in a comparative fashion. Our methods obtain nearly 7% improvements of the prediction accuracy compared to ItemCF. To analyze statistical signi<sup>fi</sup>cance, we also conducted two-tailed paired t-tests (per user) on MAUE results of HErrorCF and those of the benchmark algorithms [8]. As a result, we observed that the p-value obtained from the t-test on HErrorCF and UserCF was 0.5074 (t[942]=0.66) indicating there was no signi<sup>fi</sup>cant difference. However, the difference between HErrorCF and ItemCF is statistically signi<sup>fi</sup>cant $( \mathrm { t } [ 9 4 2 ] = - 8 . 3 4 , p < 0 . 0 0 1 )$ .

![](/api/attachments/M3UAHBSB/fulltext/images/6e0ccf353037a6cbfa1141d910781b256e7d153fb5660fa7b0665d96231befb1.jpg)  
Fig. 9. (a) A comparison of MAE achieved by UserCF and UErrorCF as the user neighborhood size (k) grows; (b) a comparison of MAE achieved by ItemCF and IErrorCF as the item neighborhood size (k′) grows.

Table 7  
Table 6  
A comparison of the best results achieved by the <sup>fi</sup>ve methods.

<table><tr><td rowspan="2">Method:</td><td rowspan="2">UserCF (k=60)</td><td rowspan="2">ItemCF (k&#x27;=50)</td><td colspan="3">Error-reflected models</td></tr><tr><td>UErrorCF (k=60)</td><td>IErrorCF (k=50, k&#x27;=60)</td><td>HErrorCF (k=50, k&#x27;=60)</td></tr><tr><td>MAE</td><td>0.7534</td><td>0.8230</td><td>0.7572</td><td>0.7556</td><td>0.7543</td></tr></table>

## 5.3.2. Comparison of cold start users and items

In this section, we investigate the prediction accuracy of the proposed models for cold start problems in comparison with the benchmark methods. First, in order to analyze the prediction accuracy of cold start items, we analyzed MAE of the previous prediction results according to the number of users' ratings that items contained in the training set.

Table 7 summarized the results of this analysis, showing how our methods outperformed the other methods. As can be seen from the results, for all methods, the more the users' ratings contained, the higher the prediction accuracy obtained. Comparing MAE of cold start items (less than <sup>fi</sup>ve ratings) obtained by each method, on the whole, CF applied error-re<sup>fl</sup>ected models provide accurate prediction. Particularly, HErrorCF provides more accurate prediction performance than the other methods. HErrorCF achieves 3% and 13% improvements compared to UserCF and ItemCF, respectively. Two-tailed paired t-tests (per item) were also performed to determine if there are signi<sup>fi</sup>cant differences. With respect to HErrorCF and UserCF, there is a small difference at a level of $1 0 \% ( \mathrm { t } [ 3 3 2 ] = - 1 . 8 6 4 , p < 0 . 1 )$ . Comparing the t-test obtained in HErrorCF and ItemCF, the difference appears to be statistically signi<sup>fi</sup>cant $( \mathrm { t } [ 3 3 2 ] = - 2 . 8 3 4 , p < 0 . 0 1 )$ .

We carried out a further experiment with the cold start dataset to examine prediction accuracy for cold start users. For the experiment, we considered different subsets of users who had few ratings in the training dataset (e.g., users who have three ratings and <sup>fi</sup>ve ratings).

Table 8 summarizes MAE of the cold start users. As expected, we observed that the quality of prediction for the cold start users is considerably lower than that of prediction when we used the original dataset. Such results were caused by the fact that it was hard to analyze the users' propensity to rate items. Nevertheless, CF based on the error-re<sup>fl</sup>ected models signi<sup>fi</sup>cantly outperforms the benchmark methods. Comparing MAE achieved by UErrorCF, IErrorCF, and HErrorCF, interesting results were observed. A higher accuracy prediction is achieved by the independent models like UErrorCF and IErrorCF over the hybrid model HErrorCF, particularly when the users have only three ratings. We identi<sup>fi</sup>ed that, on average, IErrorCF provides improved prediction performance by 17.5% more than UserCF and by 15.1% more than ItemCF, respectively. In addition, UErrorCF obtains 14.1% and 11.6% improvements for MAE compared to UserCF and ItemCF, respectively. We continued to compute two-tailed paired t-tests (per user). First, for the cold start users who have three ratings, we observed that there were signi<sup>fi</sup>cant differences between IErrorCF and UserCF (t[99]=−3.74, pb0.01), and between IErrorCF and ItemCF (t[99]= 3.56, pb0.01). Second, for the cold start users that have <sup>fi</sup>ve ratings, the obtained p-values were also less than 0.01 (pb0.01) between IErrorCF and the other two methods. The results indicate that the differences in MAE are signi<sup>fi</sup>cantly different from zero. We conclude from these experiments that the proposed CF utilizing the error-re<sup>fl</sup>ected models can improve the prediction quality of the cold start items and the cold start users.

A comparison of MAE for cold start items.

<table><tr><td>Test item</td><td>Cold start items (&lt;5)</td><td>&lt;10</td><td>&lt;15</td><td>&lt;20</td></tr><tr><td># of items</td><td>333</td><td>530</td><td>650</td><td>743</td></tr><tr><td>UserCF</td><td>0.9661</td><td>0.9199</td><td>0.8734</td><td>0.8412</td></tr><tr><td>ItemCF</td><td>1.067</td><td>1.011</td><td>0.9976</td><td>0.9912</td></tr><tr><td>UErrorCF</td><td>0.9405</td><td>0.8878</td><td>0.87714</td><td>0.8632</td></tr><tr><td>IErrorCF</td><td>0.9542</td><td>0.9015</td><td>0.8908</td><td>0.8870</td></tr><tr><td>HErrorCF</td><td>0.9352</td><td>0.8864</td><td>0.8528</td><td>0.8465</td></tr></table>

Table 8  
A comparison of MAE for cold start users.

<table><tr><td>Test user</td><td colspan="3">Cold start users</td><td rowspan="2">Original</td></tr><tr><td># of ratings for each user:</td><td>3</td><td>5</td><td>Average</td></tr><tr><td>UserCF</td><td>1.2360</td><td>1.0730</td><td>1.1545</td><td>0.7942</td></tr><tr><td>ItemCF</td><td>1.2234</td><td>1.0365</td><td>1.1299</td><td>0.832</td></tr><tr><td>UErrorCF</td><td>0.9907</td><td>1.0374</td><td>1.0140</td><td>0.7915</td></tr><tr><td>IErrorCF</td><td>0.9846</td><td>0.9726</td><td>0.9786</td><td>0.8052</td></tr><tr><td>HErrorCF</td><td>1.1312</td><td>1.0395</td><td>1.0853</td><td>0.7897</td></tr></table>

## 5.4. Discussion of computational complexities

In this section, we discuss computational complexity of previous studies in comparison with our complexity. High computational complexity is often demanded to enhance the quality of predictions and recommendations. The scalability of CF is a critical challenge in practical recommender systems with a huge number of users and items.

We <sup>fi</sup>rst analyzed the computational complexities of our methods according to the number of users m, the number of items n, the number of rating values v, the number of similar users k and the number of similar items k′. In the model-based point of view, the computational complexity can be distinguished between an of<sup>fl</sup>ine phase and an online phase. The former can be accomplished of<sup>fl</sup>ine, prior to actual recommendations for a given user, whereas the latter has to be done online and often in real time [13]. The of<sup>fl</sup>ine computation is closely connected with time required to build the error-re<sup>fl</sup>ected model based on pre-prediction errors. For calculating a pre-predicted value, the set of user neighbors and the set of item neighbors should be determined. The upper bound on the complexity of this step is $O ( m ^ { 2 } n )$ and $O ( m n ^ { 2 } )$ respectively. Additionally, the time of O(kmn) and O(k′mn) is spent for building the user-based model and for building the item-based model, respectively. Therefore, the total computational complexity in the of<sup>fl</sup>ine phase becomes approximately $O ( m ^ { 2 } n + m n ^ { 2 } + k m n ) \cong O ( m ^ { 2 } n + m n ^ { 2 } )$ for the user-based model, $O ( m ^ { 2 } n + m n ^ { 2 } + k ^ { \prime } m n ) \cong O ( m ^ { 2 } n + m n ^ { 2 } )$ for the item-based model and $O ( m ^ { 2 } n + m n ^ { 2 } + k m n + k ^ { \prime } m n ) \cong O ( m ^ { 2 } n + m n ^ { 2 } )$ for the hybrid model. However, in practice, since user–item rating matrix is very sparse, the actual computational complexity for the pre-prediction errors of users can be approximately reduced to O(mv+nv). In the online phase, the complexity required to predict a certain item j of a target user u, is given as O(k) because we need to compute the average rating of k number of users similar to the user u. Accordingly, the computational complexity of predicting all the items becomes approximately O(kn)≅O(n). In fact, when we measured the server response time on an Apache Web server environment, on average, the responding time required to predict an item was 0.0042 s. In addition, it took, on average, 2.79 s to generate predictions of all items for each user.

As for the complexity of previous studies, a memory-based CF such as UserCF provides an advantage to easily take new data into account. This is because it utilizes entire data in real-time when generating recommendations in an online phase. However, as both the number of users m and the number of items n grow, computation cost also rapidly grows as well. In the case of UserCF [5], for a target user, O(mn) is required to determine k nearest neighbors. And O(kn) is additionally required to predict all items; therefore the computational complexity becomes O(mn+kn) during the online phase. However, for most recommender systems, the online complexity in which the rating prediction of items that the users have not yet rated is more important compared to those of the of<sup>fl</sup>ine case [13]. Similar to our models, to reduce the online complexity, diverse models such as an item–item similarity model [9,25], Aspect model [13], User Rating Pro<sup>fi</sup>le (URP) model [19], Uni<sup>fi</sup>ed Relevance (UR) model [30], and Weighted Low Rank Approximations (WLRA) model [29], were proposed. The aim of such models is to support fast recommendations online by <sup>fi</sup>rst developing a pre-computed model which most timeconsuming tasks can be conducted in the of<sup>fl</sup>ine. If a user–user similarity model for UserCF is previously built in the of<sup>fl</sup>ine [17], the online cost can be rapidly diminished as O(kn) whereas the time required to build the model becomes $O ( m ^ { 2 } n )$ . Similarly, with respect to an item–item similarity model for ItemCF, $O ( m n ^ { 2 } )$ time complexity is needed in the of<sup>fl</sup>ine; for the online prediction the complexity is O (kn). Therefore, in the cases that the number of users is relatively larger than the number of items (mNNn) or the number of users that change is more dynamic than those of items that change, the item– item similarity pre-computed is practically more ef<sup>fi</sup>cient than the user–user similarity pre-computed [25].

In probabilistic approaches for building models such as WLRA, URP, UR and Aspect, Expectation Maximization (EM) algorithm is generally used to estimate the models for CF. Hence, the complexity in the of<sup>fl</sup>ine is divided into E-step and M-step; thus, the number of iterations that affect the complexity is required to estimate stable parameters. For each iteration, WLRA using Singular Value Decomposition (SVD) is needed O $( m n ^ { 2 } + m ^ { 3 } )$ for building the model. In the case of URP and Aspect, both complexities in building the model are $O ( k m n \nu )$ ; in the worst case they become $O ( k m ^ { 2 } n ^ { 2 } )$ because the number of total ratings v becomes mn at the worst $( \nu = m n )$ . With respect to UR model, the complexity is $O ( m ^ { 2 } n + m n ^ { 2 } + k ^ { 2 } m n )$ though the iteration process is not required to build the model.

Table 9 summarizes the comparisons of the computation complexity in terms of the of<sup>fl</sup>ine and the online. Although the complexity of the item–item model and the user–user model is much lower than that of our models, in the experiments we observed that UserCF and ItemCF performed worse for cold start users and items. That is, our approach provides advantages both in terms of improving the quality and in dealing with fast recommendation time. In comparison with the probabilistic models (WLRA, URP, UR, and Aspect), our approach does not include iterative building processes required in the probabilistic approaches. In addition, we support incremental updates of the models as presented in Section 4.2.

## 6. Conclusions and future work

In this paper, we have proposed a unique method of building models derived from explicit ratings. The proposed method <sup>fi</sup>rst determines a pre-predicted rating, and subsequently, identi<sup>fi</sup>es prediction errors for each user. Pre-computed models, namely the error-reflected model, are built by re<sup>fl</sup>ecting the prediction errors. The major advantage of the proposed models is that it supports incremental updating of the model by using explicit user feedback. We also presented a new method of applying the proposed models to

## Table 9

Comparison of computational complexities.

<table><tr><td colspan="2">Collaborative filtering algorithms</td><td>OfflineModel building</td><td>OnlinePrediction</td></tr><tr><td>Memory-based</td><td>UserCF</td><td>-</td><td>O(mn + kn)</td></tr><tr><td rowspan="6">Model-based</td><td>User-user model</td><td>O( $m^{2}$ n)</td><td>O(kn)</td></tr><tr><td>Item-item model</td><td>O( $mn^{2}$ )</td><td>O(kn)</td></tr><tr><td>WLRA model</td><td>O( $mn^{2}$  +  $m^{3}$ )</td><td>O(kn)</td></tr><tr><td>URP model</td><td>O(kmnv)</td><td>O(knv)</td></tr><tr><td>UR model</td><td>O( $mn^{2}$  +  $m^{2}$ n +  $mnk^{2}$ )</td><td>O( $k^{2}$ n)</td></tr><tr><td>Aspect model</td><td>O(kmnv)</td><td>O(knv)</td></tr><tr><td rowspan="3">Proposed models (model-based)</td><td>UErrorCF</td><td>O( $mn^{2}$  +  $m^{2}$ n + kmn)</td><td>O(kn)</td></tr><tr><td>IErrorCF</td><td>O( $mn^{2}$  +  $m^{2}$ n + kmn)</td><td>O(kn)</td></tr><tr><td>HErrorCF</td><td>O( $mn^{2}$  +  $m^{2}$ n + 2kmn)</td><td>O(kn)</td></tr></table>

m: # of total users, n: # of total items, v: # of ratings, k: model size.

CF recommender systems that can enhance the accuracy of the prediction with respect to the cold start problem. As noted in the experimental results, our models obtained signi<sup>fi</sup>cantly better prediction accuracy in dealing with both cold start users and cold start items, compared to the benchmark methods.

In future work, we plan to exploit social networks to build our model and generate item predictions, which is an emerging research area in recommender systems. We expect that the model incorporated with reliable social friends may offer more trustworthy items relevant to users' needs. Another interesting direction to address is the problem of manipulated ratings by unreliable users, often called shilling attacks [23]. We intend to detect unreliable user ratings by analyzing diverse types of attack model. We will investigate the possible usages of pre-prediction errors for robust recommender systems against shilling attacks. Finally, we plan to examine stability of how the proposed models provide consistent predictions over a period of time even when ratings are newly added to a system before rebuilding the models [3].

## Acknowledgments

The authors would like to acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC) and Universidad Carlos III de Madrid and Banco Santander through a Catedra de Excelencia.

## References

[1] H.J. Ahn, A new similarity measure for collaborative <sup>fi</sup>ltering to alleviate the new user cold-starting problem, Information Sciences 178 (1) (2008) 37–51.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transac tions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[3] G. Adomavicius, J. Zhang, On the stability of recommendation algorithms, Proceedings of the 4th ACM Conference on Recommender Systems, 2010, pp. 47–54.

[4] G. Bogdanova, T. Georgieva, Using error-correcting dependencies for collaborative <sup>fi</sup>ltering, Data & Knowledge Engineering 66 (3) (2008) 402–413.

[5] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative <sup>fi</sup>ltering, Proceedings of the 14th Annual Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, 1998, pp. 43–52.

[6] K.-W. Cheung, J.T. Kwok, M.H. Law, K.-C. Tsui, Mining customer product ratings for personalized marketing, Decision Support Systems 35 (2003) 231–243.

[7] A. Das, M. Datar, A. Garg, S. Rajaram, Google news personalization: scalable online collaborative <sup>fi</sup>ltering, Proceedings of the 16th International World Wide Web Conference, 2007, pp. 271–280

[8] J. Demsar, Statistical comparisons of classi<sup>fi</sup>ers over multiple data sets, Journal of Machine Learning Research 7 (2006) 1–30

[9] M. Deshpande, G. Karypis, Item-based top-n recommendation algorithms, ACM Transactions on Information Systems 22 (1) (2004) 143–177.

[10] S. Ding, S. Zhao, Q. Yuan, X. Zhang, R. Fu, L. Bergman, Boosting collaborative <sup>fi</sup>ltering based on statistical prediction errors, Proceedings of the 2nd ACM Conference on Recommender Systems, 2008, pp. 3–10.

[11] J.L. Herlocker, J.A. Konstan, A. Borchers, J. Riedl, An algorithmic framework for performing collaborative <sup>fi</sup>ltering, Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 1999, pp. 230–237.

[12] J.L. Herlocker, J.A. Konstan, L.G. Terveen, J.T. Riedl, Evaluating collaborative <sup>fi</sup>ltering recommender systems, ACM Transactions on Information Systems 22 (1) (2004) 5–53.

[13] T. Hofmann, Latent semantic models for collaborative <sup>fi</sup>ltering, ACM Transactions on Information Systems 22 (1) (2004) 89–115.

[14] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (2010) 470–479

[15] C.Y. Kim, J.K. Lee, Y.H. Cho, D.H. Kim, VISCORS: a visual-content recommender for the mobile Web, IEEE Intelligent Systems 19 (6) (2004) 32–39.

[16] H.-N. Kim, A.-T. Ji, H.-J. Kim, G.-S. Jo, Error-based collaborative <sup>fi</sup>ltering algorithm for top-n recommendation, Proceedings of the Joint 9th Asia-Paci<sup>fi</sup>c Web and 8th International Conference on Web-Age Information Management Conference on Advances in Data and Web Management, 2007, pp. 594–605.

[17] J.A. Konstan, B.N. Miller, D. Maltz, J.L. Herlocker, L.R. Gordon, J. Riedl, GroupLens: applying collaborative <sup>fi</sup>ltering to Usenet news, Communications of the ACM 40 (1997) 77–87.

[18] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative filtering JEEE Internet Computing 7 (1) (2003) 210–217

[19] B. Marlin, Modeling user rating pro<sup>fi</sup>les for collaborative <sup>fi</sup>ltering, Proceedings of the 7th Annual Conference on Neural Information Processing Systems. 2003
