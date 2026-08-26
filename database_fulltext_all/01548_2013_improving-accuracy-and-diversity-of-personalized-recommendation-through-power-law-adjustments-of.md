---
otero_id: 1548
otero_key: "WX6PYZFS"
title: "Improving accuracy and diversity of personalized recommendation through power law adjustments of user similarities"
authors: "Mingxin Gan; Rui Jiang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving accuracy and diversity of personalized recommendation through power law adjustments of user similarities

Mingxin Gan <sup>a</sup>, Rui Jiang <sup>b,</sup>⁎

<sup>a</sup> Dongling School of Economics and Management, University of Science and Technology Beijing, Beijing, 100083, China <sup>b</sup> Department of Automation, Tsinghua University, Beijing, 100084, China

## a r t i c l e i n f o

Article history: Received 27 May 2012 Received in revised form 26 January 2013 Accepted 28 March 2013 Available online 6 April 2013

Keywords: Recommender systems Collaborative <sup>fi</sup>ltering Power law adjustment Accuracy Diversity

## a b s t r a c t

Recommender systems have become more and more indispensable in both commercial and research communities, due to the increasingly serious problem of information overload accompanying the rapid development of the internet technology in the recent years. As one of the dominant branches, collaborative <sup>fi</sup>ltering approaches base on similarities of user preferences in historical data have achieved remarkable successes in producing personalized recommendations. Nevertheless, the existence of popular objects may adversely in<sup>fl</sup>uence the correct scoring of candidate objects and further yield unreasonable recommendation results. Meanwhile, it has been increasingly recognized that the gains of the recommendation accuracy are often accompanied by the losses of the diversity, yielding the accuracy-diversity dilemma for a personalized recommender system. In order to overcome these limitations while keeping a reasonable tradeoff between the accuracy and the diversity, we propose in this paper a method called PLUS (Power Law adjustments of User Similarities) to achieve personalized recommendations via the introduction of a power function to adjust user similarity scores, for the purpose of reducing adverse effects of popular objects in the user-based collaborative <sup>fi</sup>ltering framework. We perform a series of large scale validation experiments on two real data sets (MovieLens and Net<sup>fl</sup>ix) and compare the performance of our approach against that of an ordinary collaborative filtering method. Results show that our method outperforms the existing method not only in recommendation accuracy measured by the mean rank ratio and the recall enhancement, but also in recommendation diversity quanti<sup>fi</sup>ed by the mean personality and the mean novelty.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Over the past few years, recommender systems have been more and more effective in helping people to identify their preferred resources from a large set of candidate objects [12], with successful stories pervasive in a variety of applications such as the online recommendation of books [5], CDs [15], movies [15,18], news [26], and many others [2]. With the recognition of its potential value in commerce, studies on recommender systems have been drawing more and more attentions in such research communities as machine learning [20,22], data mining [8,14], information retrieval [3,17], and statistical physics [29].

Although there have been different ways in the design of a recommender system, most practical approaches are considered as belonging to either the collaborative <sup>fi</sup>ltering category or the content-based class [1]. A collaborative <sup>fi</sup>ltering method resorts to historical relationships between users and objects to infer future preferences of users on objects [7]. Such an approach can be designed based on either user similarities or object similarities that are derived from historical data. A user-based collaborative <sup>fi</sup>ltering approach assumes that users who agreed on preferred objects in the past will tend to agree in the future [4]. With this assumption, the recommendation of a set of candidate objects for a target user is done by calculating similarity scores between all pairs of users from historical data, computing discriminant scores for the candidate objects according to preferences of individual users and pairwise similarity between users, and then sorting the objects according to their scores [9]. Hence, the effectiveness of such an approach depends largely on the calculation of similarity scores between the users. Similarly, an objectbased collaborative <sup>fi</sup>ltering approach is mathematically equivalent to a user-based one by simply interchanging the roles of user and object [23]. In contrast, a content-based recommender system uses contents and properties of objects to characterize their similarities and then recommends to the target user new objects that are similar in some aspects to objects already preferred by the user [19]. Therefore, the derivation of similarities between objects from contents of the objects is crucial to such an approach. In order to promote respective advantages of these two categories of methods, a class of hybrid approaches has also been proposed [6].

The basic assumption of a user-based collaborative <sup>fi</sup>ltering approach is that users having similar preferences in history would also have similar preferences in the future. However, this principle, through having been successfully applied to a number of situations [10,11], may fail in cases that some popular objects are present. For example, suppose there exist two groups of users. The <sup>fi</sup>rst group includes people who prefer epic science <sup>fi</sup>ction <sup>fi</sup>lms (e.g., Avatar), and thus these people have strong similarities because in history they have seen quite a few <sup>fi</sup>lms in common. The second group includes much more people who prefer comedy <sup>fi</sup>lms (e.g., Forrest Gump), and thus these people also have strong similarities. In addition, suppose that all people in both groups have seen some popular Oscar-winning <sup>fi</sup>lms, and thus two users from different groups have weak similarities, simply because they only share a small number of such popular <sup>fi</sup>lms in history. Now, consider the recommendation of two <sup>fi</sup>lms, Avatar and Forrest Gump, to a target user in the epic group. It is desired that Avatar appears in front of Forrest Gump in the ranking list, because people in the epic group prefer such an epic science <sup>fi</sup>ction <sup>fi</sup>lm as Avatar. However, in real cases, it could happen that Forrest Gump occupies a higher ranking position. Since the comedy group has much more people than the epic group, it is quite possible that the number of people who prefer the comedy genre and have seen Forrest Gump is much larger than the number of people who prefer the epic genre and have seen Avatar. In this case, the discriminant score assigned to Forrest Gump could be larger than that of Avatar, because the summation of a large number of weak similarities between the target user and those prefer comedy <sup>fi</sup>lms could be higher than the summation of a much smaller number of strong similarities between the target user and those prefer epic <sup>fi</sup>lms. As a result, Forrest Gump will be ranked higher than Avatar in the recommendation list for the target user. This example shows that the presence of popular objects may adversely in<sup>fl</sup>uence the correct calculation of discriminant scores and further yield unreasonable recommendation results.

Meanwhile, although the effectiveness of a recommender system has been traditionally evaluated by accuracy metrics such as the degrees of agreement [8], the average relative rank of deleted links [28], and the mean rank ratio [13], it has been increasingly recognized that diversity measures are also indispensable in order to achieve a comprehensive understanding on the performance of a recommender system [28]. Nevertheless, the gains of the accuracy are often accompanied by the losses of the diversity, yielding the accuracy-diversity dilemma [16,28]. Therefore, how to obtain a reasonable tradeoff between the accuracy and the diversity is still a topic worth exploring [28].

To overcome these limitations while keeping a reasonable tradeoff between the accuracy and the diversity, in this paper, we propose a method called PLUS (Power Law adjustments of User Similarities) to achieve personalized recommendations by reducing the adverse effects of popular objects in the user-based collaborative <sup>fi</sup>ltering framework. Our method resorts to a power function to adjust user similarities derived from historical data using either the cosine similarity or the Jaccard index before the calculation of discriminant scores for candidate objects. We demonstrate the superior performance of our approach by performing large scale validation experiments on two real data sets (MovieLens [17] and Net<sup>fl</sup>ix [3]). Results show that our approach can raise the recommendation accuracy by more than 25% and improve the recommendation diversity by more than 26% when compared with an ordinary collaborative <sup>fi</sup>ltering method. We further perform a cluster analysis to show that the power adjustment function, with a suitable exponent parameter, effectively emphasizes opinions of users sharing similar preferences, and thus largely reduces the adverse in<sup>fl</sup>uence of popular objects with little increment in the computational burden.

## 2. Related works

## 2.1. Existing user-based collaborative filtering methods

Given a user and a set of candidate objects, we like to rank the objects according to the preference of the user such that objects ranked higher are more preferred by the user. This can be done by assigning a discriminant score to each candidate and then sorting the objects in descending order according to their scores. In this procedure, historical data about preferences of a set of users to the set of candidate objects are typically the only information we could resort to. In general, such type of historical data is represented as a matrix ${ \bf X } = ( x _ { i j } ) _ { O \times U } ,$ where O and U are the total numbers of candidate objects and users respectively, and $x _ { i j }$ represents whether the i-th object is preferred by the j-th user $( x _ { i j } = 1 )$ or not $( x _ { i j } = 0 )$

With the assumption that users tend to select popular objects, a “global ranking” method has been proposed to rank candidate objects according to their overall popularity [1]. More speci<sup>fi</sup>cally, by assigning a discriminant score $\begin{array} { r } { \boldsymbol { \nu } _ { i j } = \sum _ { 1 } \mathop { \leq } j \mathop { \leq } \boldsymbol { \nu } \boldsymbol { \mathcal { X } } _ { i j } } \end{array}$ to the i-th object $( 1 \leq i \leq 0 )$ we are able to rank the objects in descending order according to their scores. This method is simple in computation but lacks the consideration of the personality of the given user. We will refer to this method as “GlobalRank” in the rest of this paper.

To incorporate the personality of the given user into the recommendation procedure, a “user similarity” method has been proposed to weight preferences of other users according to their similarities with the given user and then mix the preferences to obtain discriminant scores for candidate objects [1]. In detail, this method <sup>fi</sup>rst calculates the pairwise similarity between every two users using the historical data, and then computes the discriminant score as follows:

$$
v _ {i j} = \frac {\sum_ {1 \leq k \leq U} s _ {k j} x _ {i k}}{\sum_ {1 \leq k \leq U} s _ {k j}},
$$

where $s _ { k j }$ is the similarity score between the k-th and j-th users. We will refer to this method as “UserSim” in the rest of this paper.

Apparently, the effectiveness of the UserSim method depends on the calculation of pairwise similarity scores between users, and so far there have been quite a few methods for such calculation, with examples including the Pearson correlation coef<sup>fi</sup>cient, the mutual information, the cosine similarity, the Jaccard index, and many others. Among these methods, the cosine similarity might be one of the most popular measures. By treating each user as a vector in a high dimensional space, this method calculates the similarity score between two users as the cosine value of the angle between the two corresponding vectors. In detail, let $\mathbf { x } _ { u } = ( x _ { k u } ) _ { O \times 1 }$ and ${ \bf x } _ { v } = ( x _ { k v } ) _ { O \times 1 }$ be the vectors corresponding to the u-th and the v-th users, the similarity between them is calculated as

$$
S _ {u v} = \frac {\mathbf {x} _ {u} ^ {T} \mathbf {x} _ {v}}{\| \mathbf {x} _ {u} \| \| \mathbf {x} _ {v} \|} = \frac {\sum_ {1 \leq k \leq 0} x _ {k u} x _ {k v}}{\sqrt {\sum_ {1 \leq k \leq 0} x _ {k u} ^ {2}} \sqrt {\sum_ {1 \leq k \leq 0} x _ {k v} ^ {2}}}.
$$

Another method for computing user similarity is the Jaccard index. By treating each user as a set that contains objects preferred by the user (i.e., the set corresponds to the u-th user is $\mathbf { u } = \{ k : x _ { k u } = 1$ $1 \leq k \leq O \} )$ , this method calculates the similarity score between two users as the number of elements in the intersection of the two sets corresponding to the two users divided by the number of elements in the union of the two sets, as

$$
S _ {u v} = \frac {| \mathbf {u} \cap \mathbf {v} |}{| \mathbf {u} \cup \mathbf {v} |},
$$

where u and v are the sets corresponding to users u and v, respectively.

## 2.2. Limitation analysis

The basic assumption of the UserSim method is that users having similar preferences in history would also have similar preferences in the future. Therefore, discriminant scores for candidate objects can be calculated as the weighted average of preferences of other users, with the weights being estimated using the historical data. Nevertheless, this formulation, though having been successfully applied to a number of situations, may fail in some special cases as illustrated in the following examples.

It is obvious that the similarity score between two users calculated as either the cosine value or the Jaccard index is proportional to the number of objects shared by the users. Therefore, a weak similarity score will be calculated for two users that share only a small number of objects. In the extreme case, a popular object must have been preferred by a large number of users, and thus the chance that two users both prefer this object will be high. As a result, it is likely that a weak similarity score will be assigned for two users simply because the two users share a popular object by chance. Such weak similarity scores will not be dominant in the downstream calculation of discriminant scores for candidate objects in most circumstances. However, in some cases, these weak similarity scores can adversely affect the calculation of discriminant scores and even lead to apparently wrong recommendations.

For example, in Fig. 1(A), a strong similarity score (0.7) has been calculated for two users u and $u _ { 1 } ,$ because they share a large fraction of common objects in historical data. Meanwhile, seven weak similarity scores (0.1) have been calculated for users u and u<sub>i</sub> $( i = 2 , . . . , 8 )$ , because u and u<sub>i</sub> $( i = 2 , . . . , 8 )$ share only a small fraction of common objects in historical data. Now, for a candidate objects $o _ { 1 }$ that is preferred only by $u _ { 1 } ,$ a discriminant score of 0.5 is calculated according to the UserSim method. On the other hand, for another candidate objects $o _ { 2 }$ that is preferred by u<sub>i</sub> $( i = 2 , . . . , 8 )$ , a discriminant score of 0.5 is also calculated. Consequently, the rank of $o _ { 1 }$ will be equal to that of $o _ { 2 }$ in the recommendation list. However, by intuition, $u _ { 1 }$ should be considered more in the recommendation process, owing to the fact that $u _ { 1 }$ share a large fraction of objects with u in history, and thus these two users could be very likely to have similar preferences. In contrast, the other users $u _ { i } ( i = 2 , . . . , 8 )$ should be less considered, in the sense that the weak similarity scores between u and these users are likely to be obtained due to the share of some popular objects. Consequently, as a more reasonable recommendation, o should be quali<sup>fi</sup>ed to occupy a place in front of $o _ { 2 }$ in the ranking list.

We further show in Fig. 1(B) a more comprehensive example that illustrates an obvious mistake introduced by a large number of weak similarity scores. Suppose that a strong similarity scores (0.7) have been calculated for users u and $u _ { 1 }$ because they share a large fraction of common objects in historical data. Similarly, a strong similarity scores (0.5) have also been calculated for users u and $u _ { 2 } .$ Meanwhile, 130 weak similarity scores (0.01) have been calculated for users u and $u _ { i } ( i = 3 , . . . ,$ 132), simply because u and u $( i = 3 , . . . , 1 3 2 )$ ) share only a small fraction of common objects in historical data. Now, for a candidate objects $o _ { 1 }$ that is preferred only by $u _ { 1 }$ and $u _ { 2 } , \mathsf { a }$ discriminant score of 0.48 is calculated according to UserSim. On the other hand, for another candidate objects $o _ { 2 }$ that is preferred by u $( i = 3 , . . . , 1 3 2 )$ , a discriminant score of 0.52 is calculated. Consequently, the rank of $o _ { 2 }$ will be higher than that of $o _ { 1 }$ in the recommendation list. However, by intuition, $u _ { 1 }$ and $u _ { 2 }$ are more important in the process of recommending objects for $u ,$ because each of them share a large fraction of objects with u in history and thus should have similar preference with u. In contrast, the other users $u _ { i } ( i = 3 ,$ …,132) are less important when recommending objects for $u ,$ because the weak similarity scores between u and these users are likely to be obtained due to the share of some popular objects. Therefore, in a more reasonable recommendation, $o _ { 1 }$ should be quali<sup>fi</sup>ed to rank in front of $_ { 0 _ { 2 } . }$

## 3. Methods

## 3.1. Overview of the proposed method

The objective of a personalized recommender system is to rank a set of candidate objects for a given user such that higher ranked objects are more preferred by the user. To achieve this goal, we propose a four-step method called PLUS (Power Law adjustment of User Similarity) that targets on reducing the adverse in<sup>fl</sup>uence of popular objects as demonstrated in the previous section.

Given the historical data $\mathbf { X } = ( x _ { i j } ) _ { O \times U }$ that describe preferences of a set of U users to the set of O candidate objects, with x representing whether the i-th object is preferred by the j-th user $( x _ { i j } = 1 )$ or not $( x _ { i j } = 0 )$ . We <sup>fi</sup>rst calculate pairwise similarity scores between users with the use of either the cosine similarity or the Jaccard index, yielding a user similarity matrix $\pmb { S } = ( s _ { i j } ) _ { U \times U } .$ . Note that in theory any other method for computing user similarity scores can be used in this step, as long as the resulting similarity scores are in the range of [0, 1].

In the second step, we apply a power function $f ( x ) = \alpha x ^ { \beta }$ to similarity scores calculated above, yielding an adjusted user similarity pro<sup>fi</sup>le, $\mathbf { T } = ( t _ { j k } ) _ { U \times U } ,$ where $t _ { i j } = \alpha s _ { i j } ^ { \beta } \mathrm { f o r } 1 \leq j , k \leq U .$ . Obviously, the scaling factor α will be cancelled in the calculation of discriminant scores for objects if a method such as UserSim is used. Hence, we focus on the in-<sup>fl</sup>uence of the exponent parameter $_ { \mathrm { ~ \it ~ \ / ~ B ~ } }$ on the performance of the proposed method, as will be described in the next section.

B  
![](/api/attachments/WX6PYZFS/fulltext/images/9ce32c50147a64a00f9a46c1b3777070f2a3b2e2739bd1197ecd651ddc84c782.jpg)

![](/api/attachments/WX6PYZFS/fulltext/images/e75b1954c302b44b154b9304ae4853100363d01bea5cc857bf886481fb4b23ff.jpg)

![](/api/attachments/WX6PYZFS/fulltext/images/8fd0f5aedfccaa145000cf632b68ec1ad83e00edeb432a4d0d0100118a54f7fc.jpg)

![](/api/attachments/WX6PYZFS/fulltext/images/78f15ec9f352fcfda85c665b60d95a4b5782a0142ffe95c8d61821815e578d82.jpg)  
Fig. 1. Limitation analysis of the UserSim method and effects of power law adjustments to user similarity scores. A: Two objects o and o are assigned equal scores by UserSim. B: Object o is assigned a smaller score than o by UserSim. C: In contrast to $( \mathsf { A } ) ,$ , object o is assigned a larger score than o after applying power law adjustments to user similarity scores. D: In contrast to (B), obiect $o _ { 1 }$ is assigned a larger score than $o _ { 2 }$ after applving power law adiustments to user similarity scores.

In the third step, we calculate discriminant scores for candidate objects using the weighted average method as in UserSim, as

$$
v _ {i j} = \frac {\sum_ {1 \leq k \leq U} t _ {k j} x _ {i k}}{\sum_ {1 \leq k \leq U} t _ {k j}}.
$$

Note that the denominator serves as a normalization factor to ensure the resulting discriminant score in the range of [0, 1]. Such a normalization procedure, however, will not affect the ranking list of the candidates for a query user, because all discriminant scores are normalized by the same number for a given user.

In the fourth step, we sort candidate objects for the given user in descending order and obtain a ranking list of the objects. It is possible that a tie occurs when two or more candidate objects are assigned equal discriminant scores. In such a situation, we break the tie by putting objects with equal scores in random order. Alternatively, we can average over ranks of objects in the tie and assign the average rank to the objects. According to our experiences, the difference between these two strategies for breaking ties is negligible.

Finally, we adopt a repeated random sub-sampling strategy to validate the above approach with the use of two large-scale data sets (MovieLens and Net<sup>fl</sup>ix), and we evaluate the performance of this approach using two criteria for measuring the recommendation accuracy (mean rank ratio and recall enhancement) and two criteria for assessing the recommendation diversity (mean personality and mean novelty). Details of the validation strategy and the evaluation criteria will be presented below.

## 3.2. Adjustment of user similarity scores

We propose to adjust user similarity scores calculated using cosine similarity, Jaccard index, or some other methods that can produce similarity scores in the range of [0, 1]. More speci<sup>fi</sup>cally, given a user similarity pro<sup>fi</sup>le, denoted by ${ \textsf { a } } U \times U$ matrix $\begin{array} { r } { \pmb { S } = ( s _ { j k } ) _ { U \times U } , } \end{array}$ the adjustment is done by applying a power function to every element in the matrix, say, introducing a new user similarity matrix $\mathbf { T } = ( t _ { j k } ) _ { U \times U }$ and calculating its elements as $t _ { j k } = \alpha s _ { j k } ^ { \beta }$ for $1 \leq j ,$ $k \leq U ,$ where α and $\mathcal { B }$ are the scaling factor and the exponent of the power function, respectively.

It is evident that the scaling factor α will be cancelled when using the UserSim method for the downstream calculation of discriminant scores for objects. Therefore, we omit this parameter in the power function and simply adjust user similarity scores as $t _ { j k } = s _ { j k } ^ { \beta }$ for $1 \leq j , k \leq U .$ This is equivalent to setting the scaling factor α to 1.

The exponent parameter ${ \mathcal { B } } ,$ however, plays a critical role in the adjustment of user similarity scores. This parameter can take values from 0 to positive in<sup>fi</sup>nity. At one end of the spectrum, setting ß to 0 is equivalent to assign an identical similarity score of 1 to every pair of users (we de<sup>fi</sup>ne $0 ^ { \circ }$ as 1). In this situation, the proposed method degenerates to the GlobalRank method since the discriminant score for every object is proportional to the number of users that have collected the object in history. At the other end of the spectrum, setting ß to positive in-<sup>fi</sup>nity is equivalent to assign an identical similarity score of 0 to every pair of users. In this situation, the proposed method degenerates to a random guess approach that assigns a discriminant score generated at random to every candidate object. At the middle of the spectrum, setting $\mathcal { B }$ to 1 is equivalent to keep similarity scores unchanged. In this situation, the proposed method degenerates to the ordinary UserSim approach.

Note that although in theory the similarity score between two users could be 1, such a rare case only occurs when the two users have collected identical objects in history. Therefore, we can simply ignore such kinds of rare special cases in our analysis without affecting conclusions. Alternatively, we can replace such maximal similarity scores with a fraction that is close to one (e.g., 0.99) to avoid the occurrence of such rare cases in a simple way. According to our experiences, these two strategies yield almost identical results in all analysis.

The in<sup>fl</sup>uence of the parameter $\mathcal { B }$ on the proposed method is illustrated in Fig. 1(C) and (D). Recall that in the previous example 1, the similarity score for u and $u _ { 1 } \mathrm { i s } 0 . 7 ,$ , and those for u and $u _ { i } ( i = 2 , . . . , 8 )$ are all 0.1. As shown in Fig. $1 ( { \mathsf { C } } ) ,$ however, when the power function with exponent ${ \boldsymbol { \beta } } = 2$ is applied, the user similarity score for u and $u _ { 1 }$ becomes 0.49, and those for u and u $( i = 2 , . . . , 8 )$ all become 0.01. As a result, the discriminant scores become 0.875 for $o _ { 1 }$ and 0.125 for $_ { 0 _ { 2 } , }$ and thus $o _ { 1 }$ ranks higher than $_ { O _ { 2 } . }$ . Similarly, in the previous example 2, the similarity scores are 0.7 for u and $u _ { 1 } , 0 . 5$ for u and $u _ { 2 } ,$ and 0.01 for u and u $( i = 3 , . . . , 1 3 2 )$ . As shown in Fig. 1(D), however, when the power function with exponent ${ \boldsymbol { \beta } } = 2$ is applied, the similarity scores become 0.49 for u and $u _ { 2 } , 0 . 2 5$ for $u _ { 1 }$ and $u _ { 3 } ,$ , and 0.0001 for $u _ { 1 }$ and u $( i = 3 , . . . , 1 3 2 )$ . Consequently, the discriminant scores become 0.983 for $o _ { 1 }$ and 0.017 for $^ { O _ { 2 } , }$ and thus $o _ { 1 }$ ranks higher than $O _ { 2 }$

## 3.3. Validation methods and evaluation criteria

Both the repeated random sub-sampling strategy and the multi-fold cross-validation method are widely used in the assessment of a recommendation method. Following the literature [28], we adopt a repeated random sub-sampling strategy to validate the proposed approach. In each validation run, we split at random known links between users and objects into a training set that contains 90% links and a test set that contains the rest 10% links, calculate a user similarity matrix using the training data, and then assess the effectiveness of the proposed method in recovering the links in the test set using the following method. For a <sup>fi</sup>xed user, we collect a set of test objects as those that connect to the user in the test data, and we collect a set of control objects as those that neither link to the user in the training data nor in the test data. Then, we calculate discriminant scores for both test and control objects, and we rank each test object against all control objects in descending order according to the discriminant scores. Repeating the above ranking procedure for all users, we obtain a set of ranking lists and further calculate four criteria to evaluate the performance of the proposed method. To account for uncertainties in the data splitting process, we further repeat the above validation run 20 times and average over all runs to obtain two criteria for measuring the recommendation accuracy and two criteria for assessing the recommendation diversity, as de<sup>fi</sup>ned below.

The <sup>fi</sup>rst accuracy criterion for evaluating the accuracy is called the mean rank ratio (MR). Given a test object and a number of control objects, we obtain the rank of the test object by sorting these objects in descending order according to their discriminant scores, with ties broken by putting objects with equal scores in random order. We further divide the rank by the total number of test and control objects to obtain the rank ratio. Then, we calculate the mean rank ratio by averaging rank ratios for all objects in the test set. Obviously, the mean rank ratio measures the accuracy of a method in recommending user preferred objects, and a method with high accuracy tends to have a lower mean rank ratio.

The second criterion for evaluating the accuracy is called the recall en hancement (RE). Given a pre-de<sup>fi</sup>ned threshold L, we claim a test object as successfully recommended if the object has been ranked among top L in the ranking list. For a user $u _ { j }$ who has collected a number of $D _ { j }$ objects in the test data, we count the number of successful recommendations among these objects as $R _ { j }$ and calculate the fraction of successfully recommended objects to obtain the recall for the user, as $p _ { j } = R _ { j } / D _ { j } $ . Finally, averaging over recalls for all users who have collected at least one object in the test data, we obtain the recall under the threshold L, denoted by $R ( L )$ . To take into account intrinsic properties of the data, we further compare a recommender method with the random guess approach. By random guess, the probability that a test object ranks among top L for user u<sub>j</sub> is $L / ( O - D _ { j } + 1 )$ , and the expected number of successful recommendations is $R _ { j } ^ { ( \mathrm { r a n d } ) } = D _ { j } \times L / ( O - D _ { j } + 1 )$ , resulting in a recall of $\mathbb { R } _ { j } ^ { ( \mathrm { r a n d } ) } /$

$D _ { j } = L / ( O - D _ { j } + 1 ) \approx L / O ,$ since in general total number of objects $O < < D _ { j }$ . We then de<sup>fi</sup>ne the recall enhancement as the fold enhancement of the recall over the random guess approach, as

$$
R E (L) = \frac {R (L)}{R ^ {\text {(rand)}} (L)} \approx \frac {O}{L} \times R (L).
$$

The <sup>fi</sup>rst criterion for evaluating the diversity is called the mean personality (MP). Given the discriminant scores calculated for a list of objects, we sort the objects in descending order according to their scores and obtain a subset of objects, $\Delta ( L )$ , that are ranked among top L in the ranking list. For two users j and k, we count the number of objects shared by their corresponding top-ranking sets, $\varDelta _ { j } ( L )$ and $\Delta _ { k } ( L )$ , and further normalize this number by the threshold value L to obtain the degree of overlap between the two ranking lists. Finally, we de<sup>fi</sup>ne the mean personality as one minus the average degree of overlap between every two users, as

$$
M P (L) = 1 - \frac {1}{L} \times \frac {2}{L (L - 1)} \times \sum_ {1 \leq j <   k \leq U} | \Delta_ {j} (L) \cap \Delta_ {k} (L) |.
$$

The second criterion for evaluating the diversity is called the mean novelty (MN). For each object, we calculate the fraction of users that have collected the object and obtain the information content of the object as the negative logarithm of the fraction. Then, given the top-ranking subset of objects for a j-th user as $\varDelta _ { j } ( L )$ , we average over the information content of the objects in the set to obtain the novelty of recommendation for the user. Finally, we de<sup>fi</sup>ne the mean novelty as the average novelty over all users, as

$$
M N (L) = - \frac {1}{U} \times \sum_ {1 \leq j \leq U} 1 | \Delta_ {j} (L) | \sum_ {i \in \Delta_ {j} (L)} \log f _ {i},
$$

where $f _ { i }$ is the fraction of users that have collected the i-th object.

A  
![](/api/attachments/WX6PYZFS/fulltext/images/1b1d1797511728368be4b1e0c31884f9787ca2fa9817f1692bd14719677e5388.jpg)  
B

## 4. Results

C

## 4.1. Data sources

D  
![](/api/attachments/WX6PYZFS/fulltext/images/7fca34c368e3be1cdd0955a504b80a4e4f21b30f11aebc05f2ab2295196d1798.jpg)

We use two large-scale data sources to validate the proposed approach. The <sup>fi</sup>rst data set is obtained from the MovieLens movie rating system (data <sup>fi</sup>le available at http://www.grouplens.org/). The original data set includes more than 10 million ratings given by 69,878 users for 10,677 movies. Each rating has 10 values, ranging from 0.5 (worst) to 5.0 (best) with step 0.5. We <sup>fi</sup>rst down-sample at random 5000 users and 5000 objects from the original data, and then follow the literature [28] to convert the ratings to binary links by assigning 1 to ratings no less than 3.0 and 0 to all other cases. Finally, we obtain a data set that includes 265,481 links between 5000 users and 5000 objects. We refer to this data set as “MovieLens” in the rest of this paper.

The second data set is obtained from Net<sup>fl</sup>ix Prize (data <sup>fi</sup>le available at http://net<sup>fl</sup>ixprize.com/). The original data contains more than 100 million ratings given by 480,189 users for $1 7 { , } 7 7 0$ movies. Each rating has 5 possible values, ranging from 1 (worst) to 5 (best) with step 1. We also use the down-sampling strategy to sample 5000 users and 5000 objects, and then convert the ratings to binary links by only keeping ratings no less than 3.0. Finally, we obtain a data set that includes 255,612 relevant links between 5000 users and 5000 objects. We refer to this data set as “Net<sup>fl</sup>ix” in the rest of this paper.

## 4.2. Improvement of the recommendation accuracy

We <sup>fi</sup>rst focus on the cosine similarity measure and the MovieLens data set to study how the parameter $\mathcal { B }$ in<sup>fl</sup>uence the recommendation accuracy of the proposed method. For this purpose, we perform a grid search on $\mathcal { B }$ by varying its value from 1.0 to 20.0 with step 1.0 and also from 0.0 to 1.0 with step 0.1, and we look at the performance of the proposed method at each such ß. In detail, for a certain $. { \mathcal { B } } ,$ we repeat the random sub-sampling strategy 20 times, evaluate the validation results in terms of the mean rank ratio (MR) and recall enhancement (RE), and summarize the results in Fig. 2.

![](/api/attachments/WX6PYZFS/fulltext/images/0ff71b2e73fbeb38ac622b4c43b9060c19a27278d80137ddab0b4ee0bf277d3d.jpg)

![](/api/attachments/WX6PYZFS/fulltext/images/66785886a3a45127ced54b02329356fd7d97db33b8291c16610ab2b8bee82bdd.jpg)  
Fig. 2. Effects of ß on the recommendation accuracy. A: The mean rank ratio on various ß. B: The recall enhancement $( L = 2 0 )$ on various ß. C: The recall enhancemen $( L = 1 0 )$ on various ß. D: The recall enhancement $( L = 5 0 )$ on various β

From Fig. 2(A), we can clearly see the positive in<sup>fl</sup>uence of a relative large ß on the recommendation accuracy of the proposed method. When $\mathcal { B }$ is equal to 1, the proposed method is the same as the ordinary UserSim approach. In this situation, we obtain a mean rank ratio of 6.58% with the standard error 0.07% (estimated from 20 repeats). When $\mathcal { B }$ increases towards 9, we observe obvious improvements in mean rank ratios. For example, the mean rank ratio decreases to 5.98% (±0.07%) when $\mathcal { B }$ increases to 2, further decreases to $5 . 3 1 \% ( \pm 0 . 0 6 \% )$ when ß increases to $^ { 4 , }$ and reaches the lowest value of 4.92% (±0.07%) when $\mathcal { B }$ is equal to 9. When ß further increases beyond 9, however, we observe a slow increase of mean rank ratios. For example, the mean rank ratio increases to 5.12% (±0.06%) when $\mathcal { B }$ increases to 15 and further increases to 5.32% (±0.06%) when $\mathcal { B }$ increases to 20. From these results, we make the conjecture that a suitable $\mathcal { B }$ value that is greater than 1 will greatly improve the recommendation accuracy of the proposed method. In our experiments, the enhancement of the mean rank ratio from $\beta = 1 \mathrm { t o } \beta = 9$ is as large as 25.23%.

We can also see from the zoomed-in plot of Fig. 2(A) the negative in-<sup>fl</sup>uence of a fractiona $\mathcal { B }$ on the recommendation accuracy of the proposed method. We observe a clear decline in mean rank ratios when $\mathcal { B }$ decreases from 1 towards 0. For example, the mean rank ratio decreases to 7.02% (±0.08%) when $\mathcal { B }$ decreases to 0.5 and further decreases to 7.45% (±0.08%) when $\mathcal { B }$ decreases to 0.1. At the low end of the spectrum, the proposed method degenerates to the ordinary GlobalRank approach when $\mathcal { B }$ decreases to $0 ,$ and we observe a relative large mean rank ratio of 7.82% (±0.08%). From these results, we make the conclusion that recommendation accuracy of the proposed method suffers from fractional $\mathcal { B }$ values. In our experiments, the decline of the mean rank ratio from $\beta = 1 \mathrm { t o } \beta = 0$ is as large as 20.36%.

The mean rank ratio indicates the expected rank position of a user preferred object in the ranking list of a recommendation. Nevertheless, in real applications a user may only pay attention to objects that appear in the <sup>fi</sup>rst recommended page (typically containing 20 objects, sometimes 10 or 50 objects). We therefore introduce the criterion of recall enhancement to study the effectiveness of the proposed method in this situation and summarize the results in Fig. 2(B), in which the cutoff value L is set to 20. Brie<sup>fl</sup>y speaking, the in<sup>fl</sup>uence of the parameter $\mathcal { B }$ on the recall enhancement is consistent with that on the mean rank ratio. When $\mathcal { B }$ is equal to 1, we observe the recall enhancement as 70.50 (±1.17). When $\mathcal { B }$ increases from 1 to 20, the recall enhancement increases with the increase of $\mathcal { B }$ and reaches the peak value of 92.81 (±1.13) when $\mathcal { B }$ is equal to $^ { 7 , }$ and then drop down slowly. When $\mathcal { B }$ decreases from 1 to $0 ,$ the recall enhancement declines with the decrease of $\mathcal { B }$ in a nearly linear fashion and <sup>fi</sup>nally jump down to the lowest value of 46.61 $( \pm 0 . 8 9 )$ when $\mathcal { B }$ is equal to $0 .$ To study the in<sup>fl</sup>uence of $\boldsymbol { \beta }$ on the recall enhancement on other values of the threshold L, we further show how this criteria changes with $1 \beta$ in Fig. 2(C and D) with L setting to 10 and 50, respectively. We observe very similar patterns in Fig. 2(C and D) as that in Fig. 2(B), though the values of the recall enhancement vary for different cutoff values. From these results, we conclude that a suitable $\mathcal { B }$ value that is greater than 1 will greatly improve the recall enhancement of the proposed method. According to our experiments, the improvement of the recall enhancement (L = 20) from $\beta = 1 \mathrm { t o } \beta = 7$ is as large as 31.65%.

We then explore the reason why a properly selected $\mathcal { B }$ could bene<sup>fi</sup>t the recommendation performance. Through literature search, we <sup>fi</sup>nd that the power adjustment strategy has been used in such research <sup>fi</sup>elds as cluster analysis of graphs [25] and gene co-expression network analysis [27]. Nevertheless, in most successful applications [24], the effectiveness of the power function and the determination of the optimal exponent parameter are conducted by empirical analysis instead of theoretical studies. Considering the fact that a recommendation process is based on the assumption that users share similar opinions in history are likely to have similar taste in the future, we hypothesize that opinions from users sharing common preferences could be ampli<sup>fi</sup>ed by the power adjustment function, and we perform the following statistical analysis to validate this hypothesis. Focusing on the MovieLens data, we conduct a cluster analysis on the user similarity pro<sup>fi</sup>le obtained by using the cosine measure to determine the optimal number of groups that share similar preferences. By applying the k-medoids algorithm to the user similarity pro<sup>fi</sup>le with k varying from 2 to 40 and adopting a criterion called the mean Silhouette width [21] to quantify the goodness of a clustering result, we <sup>fi</sup>nd that the Silhouette value exhibits a unimodal pattern with the increase of $k ,$ and the optimal clustering result is achieved at $k = 9 .$ . We hence select 9 as the optimal number of groups in the following analysis. We then evaluate whether users in the same group shared similar opinions. Given a user and a group that the user belongs to, we average over the Jaccard index between the user and every other user in the group to obtain the mean within-group Jaccard index, average over the Jaccard index between the user and every user not in the group to obtain the mean outside-group Jaccard index, and divide the mean within-group Jaccard index by the outside-group one to obtain the ratio of mean Jaccard index. We <sup>fi</sup>nd that the distribution of this criterion demonstrates a strong positive skew pattern, and most ratios (>98%) are greater than 1, indicating that users in the same group indeed share similar opinions.

We then assess effects of ß on the contribution of within-group users in a recommendation process. In each run of the validation experiment, we apply the k-medoids algorithm $( k = 9 )$ to partition users into groups, identify for each user j a set $W _ { j }$ of within-group users that belong to the same group as the user, and calculate for each object i the contribution of within-group users, as

$$
\rho_ {i j} (\beta) = \frac {\sum_ {k \in W _ {j}} s _ {k j} ^ {\beta} x _ {i k}}{\sum_ {1 \leq k \leq U} s _ {k j} ^ {\beta} x _ {i k}},
$$

where $s _ { k j } ^ { \beta }$ is the adjusted similarity between users k and $j ,$ and $x _ { i k }$ represents whether object i is preferred by user k. We further average over all test objects to obtain the mean contribution of within-group users for test objects $( \rho _ { t } )$ , average over all control objects to obtain the mean contribution of within-group users for control objects $( \rho _ { c } )$ , and calculate the relative change of $\dot { \rho } _ { t }$ over $\rho _ { c }$ as $r _ { t c } = \rho _ { t } / \rho _ { c } - 1$ to obtain the relative change of contributions.

By varying ß from 1 to 20 and repeating the validation run 20 times for each ${ } . { \mathcal { B } } ,$ we plot the above three criteria against $_ { \mathrm { ~ \it ~ \ / ~ B ~ } }$ in Fig. 3(A and B). We observe that the contribution of within-group users for test objects $( \rho _ { t } ,$ Fig. $3 ( \mathsf { A } ) ,$ upper line) exhibits a monotone increasing behavior with the increase of ${ \mathcal { B } } .$ For example, when $\mathcal { B }$ increases from 1 to 10, the median value in the 20 validation runs increases rapidly from 0.5652 to 0.7507. When $\mathcal { B }$ keeps increasing towards $^ { 2 0 , }$ however, the increase of $\rho _ { t }$ tends to slow down. In contrast, although such a monotone increasing pattern is also observed for the contribution of within-group users for control objects $( \rho _ { c } ,$ Fig. $3 ( \mathsf { A } ) ,$ , lower line), the speed of increasing is much slower. As a result, the relative change of $\rho _ { t }$ over $\rho _ { c }$ (r , Fig. 3(B)) also exhibit a monotone increasing pattern, suggesting that the increase of $\rho _ { t }$ is much faster than $\rho _ { c }$ with the increase of ${ \mathrm { ; } } { \boldsymbol { \beta } } .$

From these observations, we make the conjecture that the power adjustment function with $\it { \Delta } \beta$ > 1 can give more weight to opinions from the group that a user belongs to. Since we have shown that users in the same group share similar preferences, more weight on opinions of withingroup users often means more accurate discriminant scores. Second, although the contributions of within-group users for test and control objects both increase with the increase of ${ \mathcal { B } } ,$ the former increases much faster. Consequently, the discriminant scores for test objects tend to be more accurate than those for control objects with the increase of ${ \bf \dot { \boldsymbol { \beta } } } ,$ and thus the recommendation accuracy is likely to be improved.

We further analyze why the recommendation accuracy as illustrated in Fig. 2 exhibits an increasing and then decreasing pattern. For each test object, we divide its discriminant score by the maximal discriminant score of corresponding control objects to obtain the score ratio, and we identify the median of all such score ratios to obtain an index called the median score ratio. By varying $\mathcal { B }$ from 1 to 20 and repeating the validation run 20 times for each ß, we plot the median score ratio in Fig. 3(C). We observe from the <sup>fi</sup>gure that the median score ratio increases drastically as ß increases at the beginning, reaches the maximum at $g = 9$ , and then drops gradually $\tt a s \itbeta$ keeps increasing. Compared with the value at $\beta = 1$ , the improvement of the ratio at the optimal point ${ \boldsymbol { \beta } } = 9$ is about 55%. This observation is consistent with our previous results regarding the improvement of the recommendation accuracy and can be explained as follows.

A  
![](/api/attachments/WX6PYZFS/fulltext/images/7d868ed026ea67178ab84aa1f0cc9bdbd85f955fbd3ed7b71945bf3c4977b881.jpg)

B  
![](/api/attachments/WX6PYZFS/fulltext/images/979f0dea0533580e42b4e3d004579af732bdbc1ec6a4db6390ce3cf87b9d68d8.jpg)

C  
![](/api/attachments/WX6PYZFS/fulltext/images/0711dc14a6897295346c1bdbc98e6309394ef2062042c644059d080b578f9f31.jpg)  
Fig. 3. Effects of ß on the contribution of within-group users and the median score ratio. A: The contribution of within-group users on various ß. B: The relative change of contributions on various ß. C: The median score ratio on various ${ \mathcal { B } } .$

In the recommendation process, the rank of a test object is determined by comparing its discriminant score with those of control objects. Hence, a large score ratio indicates that the test object is likely to be ranked high. Considering all test objects as a whole, the median score ratio re<sup>fl</sup>ects how likely test objects receive high ranks. More precisely, a large median score ratio indicates that the test objects are likely to be ranked $\mathrm { \ h i g h { \it \Psi } }$ , and thus the recommendation accuracy is likely to be high. From Fig. $3 ( \mathsf C )$ , we clearly see that the trend of the median score ratio against $\mathcal { B }$ demonstrates the increasing and then decreasing pattern, with the optimal value achieving around $\beta = 9 .$ . Consequently, the recommendation accuracy as illustrated in Fig. 2 also shows such an increasing and then decreasing pattern.

## 4.3. Improvement of the recommendation diversity

We then study the in<sup>fl</sup>uence of the parameter $\mathcal { B }$ on the recommendation diversity of the proposed method, also focusing on the cosine similarity measure and the MovieLens data set. We perform the above grid search on ${ \mathcal { B } } ,$ repeat the random sub-sampling strategy 20 times for each value of ${ \mathcal { B } } ,$ evaluate the validation results in terms of the mean personality (MP) and mean novelty (MN) with the threshold value L setting to 20, and summarize the results in Fig. 4.

From Fig. 4(A), we can clearly see the positive in<sup>fl</sup>uence of a large $\mathcal { B }$ $( > 1 )$ and the negative in<sup>fl</sup>uence of a fractional $\beta ( < 1 )$ on the mean personality. When $\mathcal { B }$ is equal to 1, the proposed method, as the ordinary UserSim approach, achieves a mean personality of 54.12% (±0.51%). On the one hand, when ß increases towards positive in<sup>fi</sup>nity, we observe consistent improvement of this criterion. For example, the mean personality increases to $7 1 . 9 1 \% ( \pm 0 . 4 7 \% )$ when $\mathcal { B }$ increases to 4, further increases to $8 1 . 1 2 \% ( \pm 0 . 3 5 \% )$ when $\mathcal { B }$ increases to $^ { 8 , }$ and reaches the highest value of 87.52% (±0.36%) when $\mathcal { B }$ is equal to 20. On the other hand, when $\mathcal { B }$ decreases towards $0 ,$ we observe obvious decline of the mean personality. For example, this criterion decreases to 47.64% $( \pm 0 . 7 1 \% )$ when $\mathcal { B }$ decreases to 0.5, further decreases to 40.60% $( \pm 0 . 8 1 \% )$ ) when $\mathcal { B }$ is equal to 0.1, and jump down to 24.36% (±0.78%) when ß is equal to 0.

It is not hard to understand why setting ß to 0 results in a poor mean personality. When ß is equal to 0, all elements in the user similarity matrix become one (we de<sup>fi</sup>ne $0 ^ { 0 }$ as 1). In this situation, the proposed method degenerates to the GlobalRank approach, which is not a personalized recommendation method at all and theoretically has a mean personality of zero because an identical list of objects are recommended to all users. We also notice that in Fig. 4(A) the value of this criterion is not strictly equal to zero in our experiments. This is because users have collected different objects in the original data set. As a result, objects need to be recommended are different for different users, and thus objects ranked among top positions are not strictly identical. At the other end of the spectrum, when ß tends to positive in<sup>fi</sup>nity, all elements in the user similarity matrix become zero except for those in the main diagonal (recall that a similarity score is in the range of [0,1] and is strictly equal to 1 only when two users prefer identical objects in history). In this situation, the proposed method gives the same discriminant score (zero) to all objects and thus is equivalent to the random guess approach (recall that ties are broken by putting objects with equal scores in random order), which theoretically has the highest possible mean personality of almost one.

![](/api/attachments/WX6PYZFS/fulltext/images/2e040f8d3e0f041fea273352ff0f5ca91899f800301996a978775c06cc85e5ba.jpg)

![](/api/attachments/WX6PYZFS/fulltext/images/ca66005e27d12595b40219fbf00245e2e0f9b2b00cd86f4595e68121008d3426.jpg)  
Fig. 4. Effects of ß on the recommendation diversity. A: The mean personality $( L = 2 0 )$ on various ß. B: The mean novelty $( L = 2 0 )$ on various ß.

A  
![](/api/attachments/WX6PYZFS/fulltext/images/8235b559053be141de8df6870b14d8b062349f140756a4b329044b27253702d8.jpg)

B  
![](/api/attachments/WX6PYZFS/fulltext/images/33d838b143824cd747d11d1e5a4f3645b481ebc1f696a8ec16a57ed4276ac4a4.jpg)

C  
![](/api/attachments/WX6PYZFS/fulltext/images/214e5583e76b5359dc3815b8c7c44c2394596996b083283b191069ea59c786bb.jpg)

D  
![](/api/attachments/WX6PYZFS/fulltext/images/d13dbba9e0fad284378728823e4ecb0b9a8e1d3e98ef263e3f68afbb3a79fd03.jpg)  
Fig. 5. Effects of ß on the recommendation diversity with different threshold values (L). A: The mean personality (L = 10) on various ß. B: The mean personality $( L = 5 0 )$ on various ß. C: The mean novelty (L = 10) on various ß. D: The mean novelty (L = 50) on various ß.

The mean novelty exhibits a very similar pattern as the mean personality in responding to the change of the parameter ß, as illustrated in Fig. 4(B). When ß is equal to 1, the proposed method achieves a mean novelty of 1.97 (±0.01). When ß increases towards positive in<sup>fi</sup>nity, the mean novelty increases to 2.21 (±0.01) when ß increases to 4, further increases to 2.45 (±0.01) when ß increases to 8, and reaches the highest value of 2.71 (±0.01) when ß is equal to 20. When ß decreases towards

0, the mean personality decreases to 1.93 (±0.01) when ß decreases to 0.5, further decreases to 1.91 (±0.01) when ß is equal to 0.1, and jump down to 1.87 (±0.01) when ß is equal to 0. It is also evident that setting ß to 0 results in the GlobalRank approach that has the lowest possible mean novelty, and setting ß to positive in<sup>fi</sup>nity results in the random guess approach that has the highest possible mean novelty.

To study the in<sup>fl</sup>uence of ß on the recommendation diversity with other values of the threshold L, we further show how the mean personality and the mean novelty change with ß in Fig. 5 with L setting to 10 (Fig. 5A and B) and 50 (Fig. 5C and D). We observe very similar patterns in Fig. 5 as that in Fig. 4, though the values of the criteria vary for different cutoff values. With these results, we make the conjecture that a suitable ß value that is greater than 1 will greatly bene<sup>fi</sup>t the recommendation diversity of the proposed method. In our experiments, the enhancement of the mean personality from ß = 1 to ${ \boldsymbol { \beta } } = 9$ (for maximizing the mean rank ratio) is as large as 51.71%, and the enhancement of the mean novelty from $\mathcal { B } = 1 \mathrm { t o } \beta = 9$ is as large as 26.40%.

Furthermore, to provide a comprehensive comparison between the original UserSim and the proposed PLUS (with ß setting to the optimal value 7), we summarize the performance of these two methods in Table 1. We observe from this table that the incorporation of the power adjustment function signi<sup>fi</sup>cantly improve the performance of the collaborative <sup>fi</sup>ltering approach in terms of not only recommendation accuracy measured by the mean rank ratio and the recall enhancement, but also recommendation diversity measured by the mean personality and the mean novelty.

Table 1  
Improvements of PLUS (with ß setting to the optimal value) over UserSim in both recommendation accuracy and diversity.

<table><tr><td rowspan="2">Criterion</td><td colspan="2"> $L = 10$ </td><td colspan="2"> $L = 20$ </td><td colspan="2"> $L = 50$ </td></tr><tr><td>UserSim</td><td>PLUS</td><td>UserSim</td><td>PLUS</td><td>UserSim</td><td>PLUS</td></tr><tr><td>Mean rank ratio</td><td>0.0654 (0.0007)</td><td>0.0491 (0.0005)</td><td>0.0654 (0.0007)</td><td>0.0491 (0.0005)</td><td>0.0654 (0.0007)</td><td>0.0491 (0.0005)</td></tr><tr><td>Recall enhancement</td><td>106.68 (1.8172)</td><td>142.04 (1.4339)</td><td>70.50 (1.167)</td><td>92.81 (1.132)</td><td>39.17 (0.3675)</td><td>50.05 (0.3305)</td></tr><tr><td>Mean personality</td><td>0.5429 (0.0063)</td><td>0.9077 (0.0023)</td><td>0.5412 (0.0051)</td><td>0.8752 (0.0036)</td><td>0.4784 (0.0066)</td><td>0.8270 (0.0032)</td></tr><tr><td>Mean novelty</td><td>1.7503 (0.0048)</td><td>2.5212 (0.0100)</td><td>1.9745 (0.0052)</td><td>2.7138 (0.0092)</td><td>2.2861 (0.0059)</td><td>3.0763 (0.0113)</td></tr></table>

4.4. Consistency between different methods for calculating user similarity scores

Although the cosine similarity measure has been widely used in the calculation of user similarity scores, there also exist several other methods for the same purpose. We therefore ask the question of whether the observed improvements in both the accuracy and the diversity criteria are consistent between different methods for calculating user similarity scores. To answer this question, we replace the cosine similarity with the Jaccard index, repeat all the above experiments, and summarize the results in Fig. 6.

With the use of the Jaccard index, we observe from the <sup>fi</sup>gure a rapid decrease of the mean rank ratio when ß increases from 0 to about 7, and a slow increase of the same criterion when $\mathcal { B }$ further increases towards positive in<sup>fi</sup>nity. On the contrary, we observe a rapid increase of the recall enhancement when $\mathcal { B }$ increases from 0 to about $6 ,$ and a slow decrease of the same criterion when $\mathcal { B }$ further increases towards positive in<sup>fi</sup>nity. When comparing the above patterns with those exhibited in the results for the cosine similarity, we clearly see their consistency. We therefore make the conjecture that the in<sup>fl</sup>uence of $\mathrm { \Delta } \cdot \mathrm { \Delta } \mathcal { B }$ on the performance of the proposed method is not occasionally observed for some individual method for calculating user similarity. Moreover, we notice that the optimal performance achieved using the cosine similarity (mean rank ratio = 4.92%, recall enhancement = 92.81) is slightly better than that of the Jaccard index (mean rank ratio = 5.02%, recall enhancement = 91.41), albeit without any adjustment the Jaccard index achieves slightly higher performance than the cosine similarity. These results suggest that the cosine similarity is preferred if the recommendation accuracy is the major concern.

The trend of the mean personality with the exponent parameter $\mathcal { B }$ increasing from 0 to 20 exhibits different characteristics from that of either the mean rank ratio or the recall enhancement. When using the

A

B

Jaccard index, we observe a rapid increase of the mean personality when ß increases from 0 to 3, and then a slow increase when ß increases towards positive in<sup>fi</sup>nity. When using the cosine similarity, we observe a more smooth increase of the mean personality when $\it { \Delta } \mathcal { B }$ increases from 0 to positive in<sup>fi</sup>nity. Moreover, the mean personality obtained using the Jaccard index is higher than that of the cosine similarity for every ${ \mathcal { B } } ,$ suggesting the superior performance of the Jaccard index in providing diverse recommendations for different users. We also notice that the trend of the mean novelty is similar to that of the mean personality for both similarity measures, and again the mean novelty for the Jaccard index is higher than that of the cosine similarity for every ${ \mathrm { ~ . ~ } } \beta .$ These results suggest the superior performance of the Jaccard index in providing novel recommendations.

![](/api/attachments/WX6PYZFS/fulltext/images/aaed29dcdf948512d250db47083cc8873d01c87e713750d60cdcc19d7b180ce8.jpg)  
C

## 4.5. Consistency between different data sets

So far we have demonstrated the signi<sup>fi</sup>cant improvements of the proposed approach in making accurate and diverse recommendations using the MovieLens data set. It is therefore natural to ask the question of whether such improvements are consistent between different data sets. To answer this question, we replace the MovieLens data with the Net<sup>fl</sup>ix data, repeat all the validation experiments with the use of the cosine similarity measure, and summarize the results in Fig. 7.

Similar to the patterns exhibited in the results for the MovieLens data (Figs. 2 and 4), when using the Net<sup>fl</sup>ix data (Fig. 7), we observe a rapid decrease of the mean rank ratio when $\mathcal { B }$ increases from 0 to about 8, and a slow increase of this criterion when $\mathcal { B }$ further increases towards positive in<sup>fi</sup>nity. We also observe a rapid increase of the recall enhancement when $\mathcal { B }$ increases from 0 to about $^ { 7 , }$ , and a slow decrease of this criterion when $\mathcal { B }$ further increases towards positive in<sup>fi</sup>nity. By comparison, we see that the change of both diversity measures with the increase of $\mathcal { B }$ exhibit a different pattern from that of the accuracy measures in that both the mean personality and the mean novelty increase persistently with the increase of ${ \mathcal { B } } .$ We further perform the validation experiments based on the Jaccard index and observe similar patterns as those based on the cosine similarity (data not shown).

![](/api/attachments/WX6PYZFS/fulltext/images/de99efa4065b6523d0561179ebeaea3ce1fa118659413ce210725946926fc42f.jpg)

![](/api/attachments/WX6PYZFS/fulltext/images/945a2fb6075157428174d0af5e8cc7d35af7893a838624dbd6ca625c6f47899b.jpg)

D  
![](/api/attachments/WX6PYZFS/fulltext/images/dc7b790cf4c694098b2345accd834c4b90791005789b99028d1ad3cefdcd83ec.jpg)  
Fig. 6. Performance of the proposed approach when using different methods for calculating user similarity scores.

A  
![](/api/attachments/WX6PYZFS/fulltext/images/120e685700521e401d49a97abbea279d014fcf1057c87de7aa138a8607e102c6.jpg)

B  
![](/api/attachments/WX6PYZFS/fulltext/images/b6c5a06e7aaac95b145d785b36d6b4b784cd22e9191d8d68dd8914e9387f8a1d.jpg)

C  
![](/api/attachments/WX6PYZFS/fulltext/images/63e017d602bc825d9cafc58f1dc5e92a8150f544f5b8bbad0461237c15b82c1b.jpg)

D  
![](/api/attachments/WX6PYZFS/fulltext/images/153213cf5e34559b32142bf1874f02d5c11133f7c9ba085a27ecaf8eccf9d96e.jpg)  
Fig. 7. Performance of the proposed approach on different data sets.

We then summarize the performance of the proposed PLUS method, together with a comprehensive comparison to the UserSim approach, in Table 2. We observe from this table the clear improvement of PLUS over UserSim in terms of not only recommendation accuracy measured by the mean rank ratio and recall enhancement but also recommendation diversity quanti<sup>fi</sup>ed by the mean personality and mean novelty. Moreover, we observe that such improvement is consistent not only across different user similarity measures but also between different data sets. Therefore, we conclude from these results that the proposed PLUS method, with an appropriate exponent parameter to tune the similarity scores between users, will greatly improve the performance of the underlying collaborative <sup>fi</sup>ltering approach.

Finally, the above results are obtained based on two relative small data sets (5000 users and 5000 objects) down-sampled from the real MovieLens and Net<sup>fl</sup>ix data. It is therefore natural to ask the question of whether the above observations are still valid for relatively large data sets. To answer this question, we increase the number of both sampled users and objects to 10,000, and we repeat the validation experiments. Not surprisingly, we observe similar patterns for both accuracy and diversity criteria on the large data sets (data not shown), suggesting that the previous conclusions are independent of the number of users and objects sampled.

## 5. Conclusions and discussion

In this paper, we have proposed a method called PLUS (Power Law adjustments of User Similarities) to achieve personalized recommendation by reducing the adverse effects of popular objects in the user-based collaborative <sup>fi</sup>ltering framework. We have demonstrated the superior performance of this approach over existing methods by large-scale validation experiments and summarized the improvements of this approach in not only the accuracy but also the diversity of recommendation results. We have also shown that the performance of the proposed method is consistent between different methods for calculating user similarities and different data sets.

The success of the proposed method mainly lies in the introduction of the power function in the adjustment of user similarities. With a suitable value that is greater than 1 for the exponent parameter, our method effectively reduce the adverse in<sup>fl</sup>uence of popular objects by magnifying the difference between strong similarities that mainly result from the share of a large fraction of objects between users and weak similarities that are mainly due to the share of a small number of popular objects between users. Consequently, our method achieves signi<sup>fi</sup>cant improvements in both the accuracy and the diversity of the resulting recommendations, while only adding very few computational burdens (calculation of the power function). Therefore, our method is ready to be used in recommendation systems that are based on the collaborative <sup>fi</sup>ltering framework.

Table 2  
Performance of UserSim and PLUS on different data sets. The threshold L is set to 20.

<table><tr><td rowspan="2">Criterion</td><td rowspan="2">Similarity</td><td colspan="2">MovieLens</td><td colspan="2">Netflix</td></tr><tr><td>UserSim</td><td>PLUS</td><td>UserSim</td><td>PLUS</td></tr><tr><td rowspan="2">Mean rank ratio</td><td>Cosine</td><td>0.0658 (0.0007)</td><td>0.0492 (0.0007)</td><td>0.0616 (0.0007)</td><td>0.0511 (0.0005)</td></tr><tr><td>Jaccard</td><td>0.0646 (0.0007)</td><td>0.0502 (0.0008)</td><td>0.0608 (0.0007)</td><td>0.0516 (0.0006)</td></tr><tr><td rowspan="2">Recall enhancement</td><td>Cosine</td><td>70.50 (1.167)</td><td>92.81 (1.132)</td><td>51.77 (0.879)</td><td>63.73 (0.942)</td></tr><tr><td>Jaccard</td><td>72.48 (1.077)</td><td>92.41 (0.977)</td><td>53.92 (0.903)</td><td>63.19 (1.140)</td></tr><tr><td rowspan="2">Mean personality</td><td>Cosine</td><td>0.5412 (0.0051)</td><td>0.8752 (0.0036)</td><td>0.5554 (0.0075)</td><td>0.8838 (0.0022)</td></tr><tr><td>Jaccard</td><td>0.5629 (0.0047)</td><td>0.9107 (0.0023)</td><td>0.5852 (0.0070)</td><td>0.9532 (0.0012)</td></tr><tr><td rowspan="2">Mean novelty</td><td>Cosine</td><td>1.9745 (0.0052)</td><td>2.7138 (0.0092)</td><td>1.8658 (0.0064)</td><td>2.4306 (0.0133)</td></tr><tr><td>Jaccard</td><td>1.9978 (0.0057)</td><td>3.1732 (0.0110)</td><td>1.9358 (0.0137)</td><td>3.4253 (0.0143)</td></tr></table>

Certainly, the proposed method can be further investigated from the following aspects. First, although our method is proposed to target on user-based collaborative <sup>fi</sup>ltering framework, it is straightforward to incorporate the idea of our method into item-based collaborative <sup>fi</sup>ltering approaches by simply applying the power function to object similarities derived from historical data. It is also not hard to incorporate our idea into content-based methods by using the power function to adjust object similarities calculated based on the analysis of contents of objects.

Second, we have provided comprehensive simulation experiments and numerical analysis about the in<sup>fl</sup>uence of the exponent parameter ß on the performance of the proposed method. However, theoretical analysis about the optimal value of this parameter is still an open question. A possible treatment is to convert the adjusted user similarity matrix into a complex network and then look at how global properties of the network (e.g., the degree distribution, the scale free property, etc.) change with the exponent parameter ß. Nevertheless, the main dif<sup>fi</sup>culty in this treatment is that the conversion of the user similarity matrix into a network may itself require some threshold values that are possibly controversial.

Finally, although currently most collaborative <sup>fi</sup>ltering approaches focus on historical data to calculate user similarity scores, it has become more and more feasible to incorporate social networks of users and social tagging systems into the collaborative <sup>fi</sup>ltering framework to enhance the derivation of user similarities. Intuitively, information such as preferences of social friends and correlation of social tags between social friends will bene<sup>fi</sup>t a recommender system to overcome known issues such as the data sparsity and the cold-start problems. How to integrate these types of valuable information into the proposed method is one of our future research directions.

## Acknowledgments

This work was partly supported by the National Natural Science Foundation of China under Grants No. 71101010 and 61175002, and the Fundamental Research Funds for the Central Universities under Grant No. FRF-BR-11-019A.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (2005) 734–749.

[2] A.B. Barragans-Martinez, E. Costa-Montenegro, J.C. Burguillo, M. Rey-Lopez, F.A. Mikic-Fonte, A. Peleteiro, A hybrid content-based and item-based collaborative <sup>fi</sup>ltering approach to recommend TV programs enhanced with singular value decomposition, Information Sciences 180 (2010) 4290–4311.

[3] J. Bennett, C. Elkan, B. Liu, P. Smyth, D. Tikk, KDD Cup and workshop 2007, ACM SIGKDD Explorations Newsletter 9 (2007) 51–52.

[4] G. Biau, B. Cadre, L. Rouvière, Statistical analysis of k-nearest neighbor collaborative recommendation The Annals of Statistics 38 (2010) 1568–1592

[5] T. Bogers, A. van den Bosch, Fusing recommendations for social bookmarking web sites, International Journal of Electronic Commerce 15 (2011) 31–72.

[6] R. Burke, Hybrid recommender systems: survey and experiments, User Modeling and User-Adapted Interaction 12 (2002) 331–370.

[7] F. Cacheda, V. Carneiro, D. Fernandez, V. Formoso, Comparison of collaborative <sup>fi</sup>ltering algorithms: limitations of current techniques and proposals for scalable. high-performance recommender systems, ACM Transactions on the Web 5 (2011) 1–33.

[8] F. Fouss, A. Pirotte, J.-M. Renders, M. Saerens, Random-walk computation of similaritie between nodes of a graph with application to collaborative recommendation, IEEE Transactions on Knowledge and Data Engineering 19 (2007) 355–369.

[9] O. Georgiou, N. Tsapatsoulis, The Importance of Similarity Metrics for Representative Users Identi<sup>fi</sup>cation in Recommender Systems, 2010.

[10] J.L. Herlocker, J.A. Konstan, K. Terveen, J.T. Riedl, Evaluating collaborative <sup>fi</sup>ltering recommender systems, ACM Transactions on Information Systems 22 (2004) 5–53.

[11] Z. Huang, H. Chen, D. Zeng, Applying associative retrieval techniques to alleviate the sparsity problem in collaborative <sup>fi</sup>ltering, ACM Transactions on Information Systems 22 (2004) 116–142

[12] B. Jeong, J. Lee, H. Cho, Improving memory-based collaborative <sup>fi</sup>ltering via similarity updating and prediction modulation, Information Sciences 180 (2010) 602–612.

[13] R. Jiang, H. Yang, L.Q. Zhou, C.C.J. Kuo, F.Z. Sun, T. Chen, Sequence-based prioritization of nonsynonymous single-nucleotide polymorphisms for the study of disease mutations, American Journal of Human Genetics 81 (2007) 346–360.

[14] Y. Koren, Factorization meets the neighborhood: a multifaceted collaborative <sup>fi</sup>ltering model, Proceedings of the Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (Las Vegas, Nevada, USA, 2008), 2008, pp. 426–434

[15] G. Linden, B. Smith, J. York, Amazon.com recommendation: Item-to-item collaborative <sup>fi</sup>ltering, IEEE Internet Computing 7 (2003) 76–80.

[16] J.G. Liu, K.R. Shi, Q. Guo, Solving the accuracy-diversity dilemma via directed random walks, Physical Review E 8 (5) (2012) 016118.

[17] B.N. Miller, I. Albert, S.K. Lam, J.A. Konstan, J. Riedl, MovieLens unplugged: experiences with an occasionally connected recommender system, Proceedings of the Proceedings of the 8th International Conference on Intelligent User Interfaces (Miami, Florida, USA, 2003), 2003, pp. 263–266

[18] G. Nie, H. Xia, X. Li, An Ontology-based Approach on Intelligent Recommendation in Movie Field, Proceedings of the Proceedings of the 6th International Conference on Innovation and Management, vols. I and Ii, 2009, pp. 1489–1494.

[19] I.J. Perez, F.J. Cabrerizo, E. Herrera-Viedma, Group decision making problems in a linguistic and dynamic context, Expert Systems with Applications 38 (2011) 1675–1688.

[20] J.D.M. Rennie, N. Srebro, Fast maximum margin matrix factorization for collaborative prediction, Proceedings of the Proceedings of the 22nd International Conference on Machine Learning (Bonn, Germany, 2005), 2005, pp. 713–719.

[21] P.J. Rousseeuw, Silhouettes: a graphical aid to the interpretation and validation of cluster analysis, Journal of Computational and Applied Mathematics 20 (1987) 53–65

[22] R. Salakhutdinov, A. Mnih, Bayesian probabilistic matrix factorization using Markov chain Monte Carlo, Proceedings of the Proceedings of the 25th International Conference on Machine Learning (Helsinki, Finland, 2008), 2008, pp. 880–887.

[23] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, Proceedings of the Proceedings of the 10th International Conference on World Wide Web (Hong Kong, Hong Kong, 2001), 2001, pp. 285–295.

[24] E.E. Schadt, M.D. Linderman, J. Sorenson, L. Lee, G.P. Nolan, Computational solutions to large-scale data management and analysis, Nature Reviews Genetics 11 (2010) 647–657.

[25] S.M. van Dongen, Graph Clustering by Flow Simulation, Centrum voor Wiskunde en Informatica, Amsterdam, 2000.

[26] D. Wei, T. Zhou, G. Cimini, P. Wu, W.P. Liu, Y.C. Zhang, Effective mechanism for social recommendation of news, Physica A: Statistical Mechanics and its Applications 390 (2011) 2117–2126.

[27] B. Zhang, S. Horvath, A general framework for weighted gene co-expression network analysis, Statistical Applications in Genetics and Molecular Biology 4 (2005)(Article17)

[28] T. Zhou, Z. Kuscsik, J.G. Liu, M. Medo, J.R. Wakeling, Y.C. Zhang, Solving the apparent diversity-accuracy dilemma of recommender systems, Proceedings of the National Academy of Sciences of the United States of America 107 (2010) 4511–4515

[29] T. Zhou, M. Medo, G. Cimini, Z.K. Zhang, Y.C. Zhang, Emergence of Scale-free leadership structure in social recommender systems, PLoS One 6 (2011) e20648.

Mingxin Gan received her BS in Automation from Tsinghua University in Beijing, China, in 2001 and PhD in Management Science and Engineering from Beijing Institute of Technology in 2006. She is currently an Associate Professor in the Department of Management Science and Engineering, School of Economics and Management, University of Science and Technology Beijing. Her current research interests include recommender systems, information retrieval and text mining, information systems modeling, and knowledge management based on ontology. She can be reached at School of Economics and Management, University of Science and Technology Beijing, Beijing 100083, China; ganmx@ustb.edu.cn.

Rui Jiang received his BS in Control Science and Engineering from Tsinghua University, Beijing, China in 1997 and PhD in Control Science and Engineering from Tsinghua University in 2002. After graduation, he worked as a postdoctoral research associate in Hong Kong University of Science and Technology from 2002 to 2003 and then in the University of Southern California, USA from 2004 to 2007. He is currently an associate professor in the Department of Automation, Tsinghua University, Beijing, China. He works in the <sup>fi</sup>elds of intelligent information processing, knowledge discovery and data mining, information retrieval and text mining, and bioinformatics. His papers have appeared in the Proceedings of the National Academy of Sciences of the United States of America (PNAS), American Journal of Human Genetics, Na ture Biotechnology, IEEE-ACM Transactions on Computational Biology and Bioinformatics, Bioinformatics, Statistics and Its Interface, Communications in Information and Systems, International Journal of Information Engineering and Flectronic Business, etc He can be reached at FIT 1-107, Tsinghua University, Beijing 100084, China; ruijiang@tsinghua.edu.cn
