---
otero_id: 13062
otero_key: "7VYAN2DQ"
title: "COUSIN: A network-based regression model for personalized recommendations"
authors: "Mingxin Gan"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.12.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# COUSIN: A network-based regression model for personalized recommendations

Mingxin Gan ⁎

Department of Management Science and Engineering, Donlinks School of Economics and Management, University of Science and Technology Beijing, China Department of Statistics, University of California, Berkeley, USA

## a r t i c l e i n f o

Article history: Received 17 November 2014 Received in revised form 9 November 2015 Accepted 1 December 2015 Available online 11 December 2015

Keywords: Recommender systems Network-based regression Accuracy Diversity

## a b s t r a c t

Recently, such state-of-the-art methods as collaborative filtering, content-based, model-based and graph-based approaches have achieved remarkable success in recommendations. However, most of them make recommendations based on either information from users or objects, or bipartite relationships between them, without explicitly exploring object, user and object-user relationships simultaneously. Meanwhile, recent discoveries in sociology and behavior science have demonstrated that similar users tend to select similar objects, usually referred to the n-degree of influence. However, such understandings have not been systematically incorporated into recommendations yet. With these understandings, we propose a novel method named COUSIN (Correlating Object and User SImilarity profiles to personalized recommendatioN), adopting a regression model to incorporate object, user and object-user associations simultaneously in a global way for personalized recommendation. We also construct a power-law adjusted heterogeneous network for COUSIN to prevent adversely influence of popular nodes. We demonstrate the effectiveness of our method through comprehensive cross-validation experiments across two data sets (MovieLens and Netflix). Results show that our method outperforms the state-of-the-art methods in both accuracy and diversity performance, indicating its promising future for recommendation

© 2015 Elsevier B.V. All rights reserved

## 1. Introduction

Over the past few years, information overload accompanying the explosion of the world-wide-web has been recognized as a serious problem in not only business areas but also our daily life. As one of the promising solutions, recommender systems have been proposed to help people filtering out irrelevant information efficiently and identifying their personalized preferences effectively [1], resulting in successful applications in a variety of fields such as the online recommendation books [2], movies [3], news [4,5], TV programs [6], microblogs [7], friends [8,9], tourism [10], taxi [11], and many others [12,13].

A recommendation method is typically designed based on the collaborative filtering principle, grounded on the understanding that users who agreed on preferred objects in the past will tend to agree in the future [14–18]. With this assumption, a user-based filtering approach calculates discriminant scores for candidate objects relying on user similarities that are derived from historical data and then ranks candidates accordingly [19]. An object-based filtering design, as a counterpart of the user-based formulation, relies on object similarities that are also derived from historical data [20]. In contrast, information such as descriptions, annotations and properties of objects can also be utilized to characterize similarities between objects, resulting in a class of content-based approaches [21–23]. To promote respective advantages of these two categories, hybrid methods have also been proposed [19]. The recent advancement has also suggested that sophisticated mathematical modeling of latent relationships between users or objects could greatly benefit recommendation performance, resulting in such stateof-the-art model-based methods as the probabilistic latent semantic analysis [21,24], non-negative matrix factorization [25] and singular value decomposition [26]. Another branch of actively studied graphbased approaches tries to construct a network of users and/or objects and then makes recommendations via simulating random walk [8,27], diffusion [28,29] and heat conduction [30] processes in the network.

A hallmark of the classical collaborative filtering or content-based approaches is that they make recommendations based on the information of either users or objects alone in a local way. For example, a typical object-based collaborative filtering method relies on only object similarities and overlooks potential relationships between users. In such an approach, the prediction score of a candidate object for a query user is calculated by considering only objects that have been selected by the user in history, coinciding with a local manner. Therefore, in the scenario that similarities can only be reliable inferred between the candidate object and a small set of other objects, and it happens that these objects are not frequently selected by the query user, such an item-based method can hardly be effective due to its intrinsic local characteristic. In such a situation, simultaneous consideration of both object similarity and user similarity is desired. A toy example for the scenario is illustrated in the supplementary material (section 1). Furthermore, model-based methods such as the probabilistic latent semantic analysis, and graph-based approaches such as the random walk with restart model, have demonstrated that the use of object or user relationships in a global way will benefit the recommendation performance [31,32]. Nevertheless, none of these existing methods has explicitly explored object relationships and user relationships simultaneously in a global way. Recent discoveries in sociology and behavior science have demonstrated that similar users tend to select similar objects, in studying statistical properties of bipartite graphs of actors and movies [33,34] as well as scientists and papers they co-authored [35]. These findings, usually referred to the n-degree of influence [36–38], suggest that not only direct associations but also indirect relationships between users and objects could contribute to a recommendation process. However, such discoveries have not been systematically incorporated into a recommendation method yet.

With the above considerations, we propose in this paper a novel method called COUSIN (Correlating Object and User SImilarity profiles for personalized recommendatioN), adopting a regression model to simultaneously incorporate both of object relationships and user relationships in a global way into personalized recommendation. Specifically, our method treats the user similarity as the response variable, derive the predictor variable from the object similarity, and adopt a regression through the origin model to explain the user similarity using the object similarity. Furthermore, the computation involved in our method can be further simplified to the calculation of the cosine value between a user similarity vector and an object similarity vector, thereby greatly reduce the computational burden. We demonstrate the effectiveness of our method through comprehensive crossvalidation experiments across two data sets. Results show that our method outperforms the state-of-the-art methods in both accuracy and diversity of recommendation.

## 2. Methods

## 2.1. Overview of COUSIN

The basic premise of our method is that two users with high similarity in preference often rate similar objects, and thus the concordance between two users on preference coincides with the relatedness of objects they preferred. As illustrated in Fig. 1, our approach includes four main components. First, in the similarity calculation procedure, we calculate object similarities and user similarities based on the historical data, obtaining two matrices representing pairwise similarities. Note that in principle, object similarities can also be calculated using a content-based approach [39] or based on annotations, such as tags [40]. Second, in the network construction procedure, we apply a power-law adjustment strategy [41] to both of the object and user similarity matrices, obtaining sparse similarity networks for objects and users, respectively. Third, in the extraction process of concordance vectors, we construct two concordance vectors for the target user and a candidate object, respectively. Particularly, the vector for the target user is composed of similarities between the user and all other users, which is represented as the “user similarity profile”, and thus is of the same length as the number of users. The vector for the candidate object is derived from object similarities in the following way. For each of the other user, we collect all objects that have been selected by the user in history and sum over similarities between such objects and the candidate object to obtain a score, represented as the “associated object similarity”. Repeating this procedure for all the users, we obtain the “associated object similarity profile” between users and the object, which is represented as a vector whose length is the same as the number of users and whose elements contain scores calculated in the above way. Forth, in the concordance score calculation procedure, we establish a regression through the origin model using the two vectors, known as the user similarity profile of the user and the associated object similarity of the object, and adopt the goodness of fit of this model to measure the concordance between the target user and the candidate object. Specifically, this procedure can be simplified to the calculation of a concordance score (the same as the cosine of the angle) between the two vectors (the user similarity profile of the user and the associated object similarity profile of the object), which is defined as the “global matching degree”. Repeating the above four procedures for each pair of a target user and a candidate object, we generate their corresponding “global matching degree”. Finally, we prioritize candidate objects according to their “global matching degrees” (the concordance scores) for each target user and obtain the ranking list to make recommendations. A toy example for COUSIN is illustrated in the supplementary material (section 1).

## 2.2. Similarity calculation

We adopt two definitions of similarities: the cosine similarity (CS) and the Jaccard index (JC). Let matrix $\mathbf { X } { = } ( x _ { o u } ) _ { m \times n }$ be preferences of n users on m objects, where $x _ { o u } = 1$ if object o is preferred by user u and $x _ { o u } = 0$ otherwise. We calculate the cosine similarity between users u and v (1≤u≤n,1≤v≤n) and denote it as,

$$
s _ {u v} ^ {(\text { cosine })} = \left\{ \begin{array}{l} \frac {\sum_ {1 \leq o \leq m} x _ {o u} x _ {o v}}{\sqrt {\sum_ {1 \leq o \leq m} x _ {o u} ^ {2}} \sqrt {\sum_ {1 \leq o \leq m} x _ {o v} ^ {2}}}, u \neq v; \\ 0, u = v. \end{array} \right.
$$

That is the cosine of the angle between the two column vectors corresponding to the users. We denote similarities between all users as matrix $\pmb { S } ^ { ( \mathrm { c o s i n e } ) } = \{ S _ { u \nu } ^ { ( \mathrm { c o s i n e } ) } \} _ { n \times n } .$ . In a similar way, we calculate cosine similarities between all objects as matrix $\mathbf { T } ^ { ( \mathrm { c o s i n e } ) } = \{ t _ { o w } ^ { ( \mathrm { c o s i n e } ) } \} _ { m \times m }$

Furthermore, treating preferences of users u and v as two sets, $\mathbf { x } _ { u } =$ $\{ 0 : x _ { o u } = 1 , 1 \leq 0 \leq m \}$ . and $\mathbf { x } _ { v } = \{ o : x _ { o v } = 1$ ,1≤o≤m}, respectively, we calculate the Jaccard index between the two users as

$$
s _ {u v} ^ {\text {(Jaccard)}} = \left\{ \begin{array}{l} \frac {| \mathbf {x} _ {u} \cap \mathbf {x} _ {v} |}{| \mathbf {x} _ {u} \cup \mathbf {x} _ {v} |}, u \neq v; \\ 0, u = v. \end{array} \right.
$$

That is, the number of elements in the intersection of the two sets over that in the union. We denote similarities between all users as matrix $\pmb { S } ^ { ( \mathrm { J a c c a r d } ) } = \{ S _ { u \nu } ^ { ( \mathrm { J a c c a r d } ) } \} _ { n \times n } .$ Similarly, we calculate similarity matrix between all objects using the Jaccard index and denote it as

$$
\mathbf {T} ^ {\text {(Jaccard)}} = \left\{t _ {o w} ^ {\text {(Jaccard)}} \right\} _ {m \times m}
$$

## 2.3. Network construction

Although the above similarity calculation have been widely used in the existing collaborative filtering approaches, the existence of unreliable relationships may result in small similarity scores and hence adversely influence the downstream inference [42]. Recent studies have shown that the application of a power-law transformation to user similarities can greatly benefit recommendation performance by effectively magnifying the difference between strong similarities resulting from the share of a large fraction of objects and weak similarities due to the share of a small number of popular objects [41]. We therefore adopt such a power-law transformation strategy in our model. Specifically, given the original similarity $s _ { u v }$ between two users u and $\nu ,$ we raise it by the exponent $\beta ,$ obtaining the adjusted similarity $s _ { u v } ^ { \beta } .$ Repeating this procedure for all pairwise similarities between users, we obtain the power law adjusted user similarity matrix $\begin{array} { r } { \pmb { S } = ( s _ { u v } ^ { \beta } ) _ { n \times n } . } \end{array}$ We further treat users as vertices and user relationships with non-zero similarities in this matrix as edges to obtain a user network. Similarly, we obtain power law adjusted object similarity matrix $\mathbf { T } = ( t _ { o w } ^ { \alpha } ) _ { m \times m }$ and further construct an object network.

![](/api/attachments/7VYAN2DQ/fulltext/images/457f480fcd2d4538ae49138205e86d539612f1c04f63b4e283d09228390e8d9f.jpg)  
Fig. 1. Workflow of COUSIN. (A) The user and object similarity matrix. (B) The user and object similarity networks are constructed using power-law adjustment strategy. (C) To score a particular user-object pair (u, o), the user similarity profile for u and the object similarity profile for o are extracted. (D) The linear regression of two profiles is calculated and assigned as the ranking score for u to o.

## 2.4. Regression through the origin

With power-law adjusted similarities for object and users obtained, we construct two concordance vectors for a query user and a candidate object, respectively. The vector for the query user is composed of adjusted similarities between the user and all other users, represented as the “user similarity profile”, and thus is of the same length as the number of users. Formally, for user u, the vector is $\mathbf { y } _ { u } = ( y _ { u 1 } , y _ { u 2 } , \ldots , y _ { u n } ) ,$ where $y _ { u \nu } = s _ { u \nu } ^ { \beta }$ with $s _ { u v }$ the similarity between users u and v. The vector for the candidate object is derived from object similarities as follows. For a user, we collect all objects that have been selected by the user in history and sum over adjusted similarities between such objects and the candidate object to obtain a score, represented as the “associated object similarity”. Repeating this procedure for all users, we obtain a vector representing the “associated object similarity profile”, whose length is the same as the number of users and whose elements contain scores calculated in the above way. Formally, for object o, the vector is $\mathbf { x } _ { o } = ( x _ { o 1 } , x _ { o 2 } , \dots , x _ { o n } )$ , where $x _ { o v } =$ $\sum _ { w \in \mathcal { Q } ( v ) } t _ { o w } ^ { \alpha }$ for 1≤v≤n, where Ω(v) is the collection of objects that have been selected by user v in history, and $t _ { o w }$ the similarity between objects o and w.

We then fit a regression through the origin model using these two vectors as

$$
\mathbf {y} = \theta \mathbf {x} + \epsilon ,
$$

where θ is the regression slope, y = y the concordance vector for user u, $\mathbf { x } = \mathbf { x } _ { o }$ the concordance vector for candidate object o, and $\epsilon = ( \varepsilon _ { 1 } , \dots , \varepsilon _ { n } ) ^ { T } , \varepsilon _ { i } { \sim } N ( 0 , \sigma ^ { 2 } ) ( i { =                1 } , \dots , n )$ , independent and identically distributed.

With this regression model, we quantify the strength of association between user u and object o using the statistical significance of the hypothesis testing problem.

$$
H _ {0}: \theta = 0 \text { versus } H _ {1}: \theta \neq 0.
$$

Apparently, the maximum likelihood estimator of the parameters are

$$
\hat {\theta} = \frac {\sum_ {v = 1} ^ {n} x _ {o v} y _ {u v}}{\sum_ {v = 1} ^ {n} x _ {o v} ^ {2}} \text {   and   } \hat {\sigma} ^ {2} = \frac {1}{n} \sum_ {v = 1} ^ {n} \left(y _ {u v} - \hat {\theta} x _ {o v}\right) ^ {2} = \frac {n - 1}{n} S ^ {2},
$$

with sampling distributions

$$
\frac {\hat {\theta} - \theta}{\sqrt {S ^ {2} / \sum_ {v = 1} ^ {n} x _ {o v} ^ {2}}} \sim T _ {n - 1} \text { and } S ^ {2} = \frac {1}{n - 1} \sum_ {v = 1} ^ {n} \left(y _ {u v} - \hat {\theta} x _ {o v}\right) ^ {2} \sim \chi_ {n - 1} ^ {2},
$$

Define a test statistic F as.

$$
F = \frac {\hat {\theta} ^ {2}}{S ^ {2} / \sum_ {v = 1} ^ {n} x _ {o v} ^ {2}}
$$

It is evident that this statistic has an F distribution with 1 and n-1 degrees of freedom $\left( F _ { 1 , ~ n - 1 } \right)$ when the null hypothesis holds. The p-value of the proposed test can then be calculated as $P ( F _ { n - 1 } { \ge } f )$ with f the realized value of statistic F.

In the recommendation process, the goal is to rank candidate objects, and this can be done by using realized values of F statistics corresponding to the objects directly without calculating the p-values, given the one-to-one corresponding relationship between these two statistics (F and p-value) and the fixed number of degrees of freedom (n-1). Furthermore, since the sample variance can be calculated as.

$$
(n - 1) S ^ {2} = \sum_ {v = 1} ^ {n} y _ {u v} ^ {2} - \left(\sum_ {v = 1} ^ {n} x _ {o v} y _ {u v}\right) ^ {2} / \left(\sum_ {v = 1} ^ {n} x _ {o v} ^ {2}\right),
$$

statistic F can be calculated as

$$
\begin{array}{l} F = \frac {\hat {\theta} ^ {2}}{S ^ {2} / \sum_ {v = 1} ^ {n} x _ {o v} ^ {2}} = \frac {\left(\sum_ {v = 1} ^ {n} x _ {o v} y _ {u v}\right) ^ {2}}{\sum_ {v = 1} ^ {n} x _ {o v} ^ {2}} \frac {1}{S ^ {2}} \\ = \frac {n - 1}{\left(\sum_ {v = 1} ^ {n} x _ {o v} ^ {2}\right) \left(\sum_ {v = 1} ^ {n} y _ {u v} ^ {2}\right) / \left(\sum_ {v = 1} ^ {n} x _ {o v} y _ {u v}\right) ^ {2} - 1}. \end{array}
$$

Hence, given the fact that all $x _ { o v }$ and $y _ { u v }$ are non-negative, ranking candidate objects according to the realized values of F is equivalent to rank them according to the cosine value between the two concordance vectors, as.

$$
\mathrm{con} = \frac {\sum_ {v = 1} ^ {n} x _ {o v} y _ {u v}}{\sqrt {\sum_ {v = 1} ^ {n} x _ {o v} ^ {2}} \sqrt {\sum_ {v = 1} ^ {n} y _ {u v} ^ {2}}}
$$

We call this cosine value the concordance score between a target user and a candidate object, representing the “global matching degree”, since this value measures the degree that the user similarities coincide with the object similarities in a global point of view. With such a global matching degree calculated for every candidate object, the recommendation can then be done by ranking them according to their scores.

From the point of view of implementation, we present the matrix form of our method as follows. Given the preference matrix ${ \bf X } = ( x _ { o u } ) _ { m \times n }$ , the power law adjusted object similarity matrix T = $( t _ { o w } ^ { \alpha } ) _ { m \times m }$ and the power law adjusted user similarity matrix $\mathbf { S } = \left( S _ { \perp \nu } \right.$ $^ { \beta } ) _ { n \times n } ,$ we first calculate a matrix $\mathbf { R } { = } \mathbf { T } \mathbf { X } { = } ( r _ { o u } ) _ { m \times n } .$ Columns of this matrix therefore correspond to concordance vectors for objects. We then calculate row-normalized matrix $\tilde { \mathbf { R } } = ( \tilde { r } _ { o u } ) _ { m \times n }$ with $\tilde { r } _ { o u } = r _ { o u } /$ $\sqrt { \Sigma _ { \nu = 1 } ^ { n } r _ { o \nu } ^ { 2 } }$ and column-normalized matrix $\pmb { \mathsf { S } } = ( \mathsf { \pmb { S } } _ { u v } ) _ { n \times n } ,$ , where $s _ { u v } =$ $s _ { u \nu } ^ { \beta } / \sqrt { \Sigma _ { w = 1 } ^ { n } \big ( s _ { w \nu } ^ { \beta } \big ) ^ { 2 } }$ . Finally, we calculate a ranking score matrix for all object-user pairs as $\mathbf { P } = \tilde { \mathbf { R } } \mathbf { S }$ . Particularly, the u-th column of matrix

P contains ranking scores for a certain user u. In some applications, it might be necessary to perform column-wise normalization for matrix P and use $\textstyle p _ { o u } = p _ { o u } / \sum _ { w = 1 } ^ { m } p _ { w u }$ as the ranking score of object o for query user u, in order to guarantee that all ranking scores for a user sum up to 1.

## 2.5. Methods for comparison

We compare the proposed approach with five other methods. First, we replace the cosine measure with the Pearson's correlation coefficient (PCC) in the calculation of the concordance score, resulting in a method named COUSIN-PCC. Analogous to the aforementioned derivation, this method can be derived from a simple linear regression model with both intercept and slope present. Hence, the difference between the cosine and PCC versions of COUSIN is whether the concordance vectors are centered in the calculation of the score.

Second, we implement a collaborative filtering approach based on object similarity with power law adjustment (OSpl) by calculating the prediction score of a candidate object o for a query user u as $p _ { o u } =$ $\scriptstyle \sum _ { w = 1 } ^ { m } t _ { o w } ^ { \alpha } x _ { w u } .$ In matrix form, $\mathbf { P } = \mathbf { T } \mathbf { X } .$ . In a similar way, we implement a collaborative filtering approach based on user similarity with power law adjustment (USpl) by calculating the prediction score of a candidate object o for a query user u as $\begin{array} { r } { p _ { o u } = \sum _ { \nu = 1 } ^ { n } \chi _ { o \nu } s _ { u \nu } ^ { \beta } } \end{array}$ . In matrix form, $\mathbf { P } { = } \mathbf { X } \mathbf { S } .$

Third, implement two typical matrix factorization methods, i.e. non-negative matrix factorization (NMF) [25,43] and singular value decomposition (SVD) [26]. For NMF, we first calculate two nonnegative matrices $\pmb { W } = ( w _ { i j } ) _ { m \times q }$ and $\begin{array} { r } { \mathbf { H } = ( h _ { i j } ) _ { q \times n } , } \end{array}$ where q is typically much smaller than $n ,$ with the objective of minimizing the Frobenius norm of the difference between the original matrix X and the product WH under the constraint that W and H should be non-negative, i.e.,

$$
\min \| \mathbf {X} - \mathbf {W H} \| _ {F}, \text {   s.t.,   } \mathbf {W} \geq 0, \mathbf {H} \geq 0
$$

To prevent over-fitting, regularization terms $\| \mathbf { W } \| _ { F }$ and $\| \mathbf { H } \| _ { F }$ are further added to the objective function as

$$
\min \left\| \mathbf {X} - \mathbf {W} \mathbf {H} ^ {\mathrm{T}} \right\| _ {F} + \| \mathbf {W} \| _ {F} + \| \mathbf {H} \| _ {F}, \text { s.t., } \mathbf {W} \geq 0, \mathbf {H} \geq 0
$$

$$
\mathbf {P} = \mathbf {W H}
$$

For SVD, we calculate three matrices $\mathbf { U } = ( u _ { i j } ) _ { m \times m } , \Sigma = ( \delta _ { i j } ) _ { m \times n }$ and $\pmb { V } ^ { T } = ( \nu _ { i j } ^ { T } ) _ { n \times n }$ corresponding to the singular value decomposition of X, $\mathrm { i } . \mathrm { e } . , \mathbf { U } \pm \mathbf { V } ^ { T }$ , where U is a unitary matrix over $R ^ { m \times m } , \pmb { \Sigma }$ a diagonal matrix with non-negative real numbers on the diagonal, and $\mathbf { V } ^ { T }$ the conjugate transpose of a unitary matrix V over $R ^ { n \times n }$ . Then, we calculate the prediction score matrix P as the product of the three, i.e., $\mathbf { p } { = } \mathbf { U } \pmb { \Sigma } \mathbf { V } ^ { T }$

Finally, we implement a probabilistic spreading method (ProbS), which works by simulating the process of reallocating resources between objects and users [44]. Formally, we first calculate a weight matrix $\mathbf { E } = ( e _ { o t } ) _ { m \times m } \mathsf { a s }$

$$
e _ {o t} = \frac {1}{d _ {t}} \sum_ {\nu = 1} ^ {n} \frac {x _ {o \nu} x _ {t \nu}}{d _ {\nu}},
$$

where $\begin{array} { r } { d _ { t } = \sum _ { u = 1 } ^ { n } x _ { u t } } \end{array}$ and $\begin{array} { r } { d _ { v } = \sum _ { o = 1 } ^ { m } x _ { o \nu } } \end{array}$ are degrees of the object t and user v, respectively. Then, we calculate the prediction score matrix as $\mathbf { P } { = } \mathbf { E } \mathbf { X }$

## 2.6. Validation methods and evaluation criteria

We perform 10-fold cross-validation experiments to validate the proposed approach. For this purpose, we partition known links between users and objects at random into 10 subsets of almost equal size. In each validation run, we use 9 subsets as training data to generate similarity matrices and use the remaining one as test data to assess the effectiveness of our method. For a certain user, we collect a set of test objects as those that connect to the user in the test data, and a set of control objects as those that neither connect to the user in the training data nor in the test data. Then, we calculate concordance scores for both the test and the control objects, and rank each test object against all control objects in non-ascending order according to their scores. Repeating the above ranking procedure for all users, we obtain a set of ranking lists and further calculate two criteria for measuring accuracy and two criteria for assessing diversity, as defined below.

A good recommendation method tends to rank objects known as preferred by a query user ahead of irrelevant objects. In other words, a test object should receive a small rank value. Considering that the number of objects in the corresponding control set varies across different tests, we derive an accuracy criterion called mean rank ratio (MRR). Given a test object and a number of control objects, we sort the test object in a non-ascending order according to their concordance scores. In the situation that multiple objects have equal scores, we break the tie by putting these objects in a random order. We further divide the rank by the total number of test and control objects to obtain the rank ratio. Then, we average rank ratios for all objects in the test set and obtain the criterion of mean rank ratio. Obviously, mean rank ratio measures the accuracy of a method in recommending user preferred objects, and a method with high accuracy tends to have a lower mean rank ratio.

Since a good recommendation method should rank objects known as preferred by a query user ahead of irrelevant objects, the known preferred objects should be enriched among top positions. We therefore derive a criterion called recall enhancement (RE). Given a pre-defined threshold L, we claim a test object as successfully recommended if it is ranked among top L in the ranking list. For a user u who has collected a number of $D _ { u }$ objects in the test data, we count the number of successful recommendations among these objects as $R _ { u }$ and calculate the fraction of successfully recommended objects to obtain the recall for the user as $p _ { u } = R _ { u } / D _ { u }$ . Averaging over recalls for all users who have collected at least one object in the test data, we obtain the recall under the threshold L, denoted by $R ( L )$ . To take into account intrinsic properties of the data, we further compare a recommender method with the random guess approach. By random guess, the expected number of successful recommendations is $R _ { u } ^ { ( \mathrm { r a n d } ) } { = } D _ { u } { \times } L / ( O { - } D _ { u } { + } 1 )$ for user u, corresponding to a recall of $\mathrm { R } _ { u } ^ { ( \mathrm { r a n d ) } } / D _ { u } = L / ( O - D _ { u } + 1 )$ ≈L/O, since in general total number of objects $O < < D _ { u } .$ We then define the recall enhancement as the fold enhancement of the recall over the random guess approach as

$$
R E (L) = \frac {R (L)}{R ^ {\text {(rand)}} (L)} \approx \frac {O}{L} \times R (L).
$$

In this paper, we use $L = 1 0$ in the calculation of this criterion. It is also obvious that a method of higher recommendation accuracy will have a larger recall enhancement.

A good recommendation method should produce a ranking list with certain divergence across different users. In other words, when looking at objects ranked among top L, the ranking list of two users should be significant different from each other. With this consideration, we derive a criterion for diversity evaluation and name it mean personality (MP). Given prediction scores calculated for a list of objects, we obtain a subset of objects, $\varDelta ( L )$ , that are ranked among top L in the ranking list. For two users u and v, we count the number of objects shared by their corresponding top-ranking sets, $\varDelta _ { u } ( L )$ and $\Delta _ { \nu } ( L )$ , and normalize this number by the threshold value L to obtain the degree of overlap between the two ranking lists. Finally, we define the mean personality as one minus the average degree of overlap between every two users, as [30]

$$
M P (L) = 1 - \frac {1}{L} \times \frac {2}{L (L - 1)} \times \sum_ {1 \leq u <   v \leq n} | \Delta_ {u} (L) \cap \Delta_ {v} (L) |.
$$

A good recommendation method should not always recommend common objects that are already preferred by a query user. Instead, a method should also recommend some novel objects. In other words, when looking at objects ranked among top L, there should be some of such novel objects. We take this into consideration and derive a criterion named mean novelty (MN) for diversity evaluation. For each object, we calculate the fraction of users that have collected the object and obtain the information content of the object as the negative logarithm of the fraction. Then, given the top-ranking subset of objects for a u-th user as $\varDelta _ { u } ( L )$ , we average over the information content of the objects in the set to obtain the novelty of recommendation for the user. Finally, we define mean novelty as the average novelty over all the n users, as.

$$
M N (L) = - \frac {1}{n} \times \sum_ {1 \leq u \leq n} \frac {1}{| \Delta_ {u} (L) |} \sum_ {o \in \Delta_ {u} (L)} \log_ {2} f _ {o},
$$

where $f _ { o }$ is the fraction of users that have collected the o-th object [30].

## 3. Results

## 3.1. Data sets

We used two large-scale data sources to validate the proposed approach. The first dataset, named MovieLens, was obtained from the GroupLens lab (http://www.grouplens.org). The original data set included more than 10 million ratings given by 69,878 users for 10,677 movies. Each rating had 10 values, ranging from 0.5 (worst) to 5.0 (best) with step 0.5. We followed the literature [30] to convert the ratings to binary links by assigning 1 as “relevant” to ratings no less than 3.0 and 0 as “not-relevant” to all other cases. Then, we repeatedly removed movies and users with less than five links and obtained a data set that included 8,240,192 links between 69,814 users and 9888 movies. We further calculated that on average each user rated 118.03 movies, and each movie was rated by 833.35 users in this dataset.

The second data set, called Netflix, was obtained from the Netflix Prize (http://www.netflixprize.com). This data set contained about 100 million ratings given by 480,189 users for 17,770 movies. Each rating had 5 possible values, ranging from 1 (worst) to 5 (best) with step 1. We performed a similar sampling process by down-sampling at random 50,000 users and retaining 16,560 movies rated by at least 5 of such users. Treating ratings below 3.0 as “not-relevant” and those no less than 3.0 as “relevant”, we obtained a data set that includes 9,087,865 links between the sampled users and movies. We further calculated that on average each user rated 181.76 movies, and each movie was rated by 548.78 users in this dataset.

## 3.2. Object similarity implies user similarity

We first validated the basic assumption of our method by checking whether the derived user similarity can be explained using object similarity according to annotated associations between users and objects. For this purpose, we derived a user similarity matrix and an object similarity matrix using the cosine measure. Then, we derived a quantity named mean object similarity by calculating for each pair of users the mean pairwise similarity between their associated objects. Next, we analyzed the relationship between the user similarity and the mean object similarity by partitioning mean object similarities into 100 bins of equal size, averaging over both mean object similarity values and corresponding user similarity values in each bin, and plotting the resulting relationships in Fig. 2.

From the figure, we clearly see strong positive correlation between the user similarity and the mean object similarity. For example, for user pairs with weak mean object similarities $( \mathbf { e . g . , } \leq 0 . 1 0 )$ , the corresponding user similarities are also low $( \mathrm { i } . \mathsf { e } . , \leq 0 . 0 5 )$ . For user pairs with relatively strong mean object similarities $( \mathrm { e . g . , } \sim 0 . 5 )$ , the corresponding user similarities are also relatively strong $\left( \mathrm { i } . \mathrm { e } . , \sim 0 . 3 \right)$ . For user pairs with mean object similarities in between $( \mathbf { e . g . } , \sim 0 . 3 )$ , the mean object similarity is also in between $( \mathbf { e . g . , } \sim 0 . 1 5 )$ . Furthermore, it is obvious that with the increase of the mean object similarity, the user similarity also increases, suggesting that users having selected similar object also tend to be similar.

![](/api/attachments/7VYAN2DQ/fulltext/images/347b952ca71c8d9a3177ab88a3263bc8c8733494da4b7c8af592aa698ddbf39d.jpg)  
Fig. 2. Object similarity implies user similarity. A quantity named mean object similarity is calculated for each pair of users as the mean pairwise similarity between their associated objects, and is partitioned into 100 bins of equal size (MovieLens dataset, cosine similarity measure). Averaging over both mean object similarity values and corresponding user similarity values in each bin, we obtain the relationship between the user similarities and object similarities.

To quantitatively measure the correlation between user similarity and the mean object similarity, we further derived two vectors, one composed of mean similarities of user pairs in the bins and the other consisting of corresponding mean object similarities. We then calculated correlation coefficient of these two vectors. Results show that the Person's correlation coefficient is 0.9765 (p-value ${ < 2 . 2 2 \times 1 0 ^ { - 1 6 } } )$ and the Spearman's correlation coefficient is 0.9756 (p-value b2.22 × 10<sup>−16</sup>), both revealing that the user similarity indeed positively correlates with the mean object similarity with strong statistical significance.

We further performed a regression analysis using the user similarity as the response and the mean object similarity as the predictor. Results show that the resulting model is well fitted $( r ^ { 2 } = 0 . 9 5 2 7 )$ . The slope coefficient is statistically significant (p-value $< 2 . 2 \times 1 0 ^ { - 1 6 }$ by one-side t test), while the intercept coefficient is near to zero (−0.0069) and is not statistically significant (p-value =0.247 by one-sided t test). We therefore discarded the intercept and fitted a regression through the origin model. Results show that the resulting model is well fitted $( r ^ { 2 } = 0 . 9 8 6 7 )$ , and the slope coefficient is statistically significant $( p \mathrm { - } \mathrm { v a l u e } < 2 . 2 \times 1 0 ^ { - 1 6 }$ by one-side t test). These results further confirm that the mean object similarity indeed implies user similarity, and thus the basic assumption of our method is valid.

## 3.3. Improvement in recommendation performance

We conducted 10-fold cross-validation experiments to access the performance of our method (with parameters $\alpha = 1 0 \mathrm { a n d } \beta = 5 )$ and compared it with existing state-of-the-art methods. We first performed an object-wise comparison of different methods by testing whether rank positions of the test objects produced by a method is significantly higher than another via a one-sided Wilcoxon rank sum test. Results suggest that our method outperforms all the other methods in comparison (p-values $< 2 . 2 \times 1 0 ^ { - \bar { 1 } 6 } )$ , and the order of the other methods according to their performance from the best to the worst is NMF,

USpl (with parameter $\beta = 5 )$ , SVD, OSpl (with parameter $\alpha = 1 )$ , and ProbS.

We further performed a user-wise comparison of ranking performance via a binomial exact test. For a certain user, we claim that method A outperforms method B if rank positions of more than half test objects generated by the former are ahead of those provided by the later (equal rank cases are discarded in the comparison). Then, we count the number of users for whom method A outperforms B and test whether the relative frequency of such users is greater than 0.5 using a onesided binomial exact test. Results also suggest that our method in general performs significantly higher than all the other methods in comparison (p-values $< 2 . 2 \ \times \ 1 0 ^ { - 1 6 } )$ , consistent with the results obtained from the object-wise comparison, as illustrated in Table 1.

We then assessed the performance of each method using the criteria defined in the method section and summarized the results in Table 2 and Fig. 3. We observe that our approach in general outperforms all the other methods. As for the recommendation accuracy, our method achieves a mean rank ratio (MRR) of 4.20% in 10 independent runs of the cross-validation experiment, suggesting that on average a test object can be ranked at about 4 out of 100. In comparison, NMF, as the method with the second highest performance, only achieves an MRR of 5.09%. SVD, ProbS, OSpl and USpl achieve MRRs of 6.11%, 5.84%, 5.69% and 5.08%, respectively. A one-sided Wilcoxon rank sum test based on 10 independent repeats of the validation experiments suggests that the MRR of our method is significantly smaller than that of NMF $( p \mathrm { - v a l u e } = 9 . 1 3 \times 1 0 ^ { - 5 } )$ , which in turn significantly smaller than those of the other methods. In terms of the recall enhancement (RE), our method also outperforms all the others ones with the highest value of 168.22, and one-sided Wilcoxon rank sum tests support the statistical significance of this superiority (p-values $< 9 . 1 3 \times 1 0 ^ { - 5 } )$ NMF, SVD, ProbS, OSpl and USpl achieve REs of 165.25, 143.33, 124.85, 145.58 and 155.72, respectively.

As for recommendation diversity, COUSIN achieves a mean personalization (MP) of 94.86% (at the rank cut-off value of L = 10), suggesting that ranking lists of every two users are quite different. NMF, SVD, ProbS, OSpl and USpl achieve MPs of 91.42%, 86.91%, 70.52%, 85.79% and 83.12% respectively. Statistical analysis supports the superiority of our method over the others (one-sided Wilcoxon rank sum tests show p-values $< 9 . 1 3 \times 1 0 ^ { - 5 } )$ . In terms of the mean novelty (MN), our method achieves the highest value of 2.98 (at the rank cut-off value of $L = 1 0 )$ among all methods. NMF, SVD, ProbS, OSpl and USpl achieve MNs of 2.30, 2.07, 1.74, 2.24 and 2.01, respectively. One-sided Wilcoxon rank sum tests also support the statistical significance of this superiority (p-values $< 9 . 1 3 \times 1 0 ^ { - 5 } )$

The above experimental results are all based on the cutoff value of 3.0. We also analyzed the influence of different cutoff values (0.5, 1.0, 2.0, 3.0, 4.0 and 5.0) for converting the MovieLens data. We find that the selection of the cutoff values does not affect our conclusion. Particularly, although the values of the criteria are different when selecting different cutoff values to convert the dataset, our method, COUSIN, uniformly outperforms all the other methods at all cutoff

## Table 1

User-wise comparison of different methods. Results are obtained by 10-fold crossvalidation experiments on MovieLens (69,814 users and 9888 objects) with the cosine similarity measure. \*\*\* denotes the method in the corresponding row is better than that in the corresponding column at the statistical signi cance level of $1 0 ^ { - 8 }$ after the Bonferroni correction. + denotes the pull-hypothesis cannot be reiected at the signi cance level of $1 0 ^ { - 1 }$ after the Bonferroni correction

<table><tr><td>Method</td><td>COUSIN</td><td>NMF</td><td>SVD</td><td>ProbS</td><td>OSpl</td><td>USpl</td></tr><tr><td>COUSIN</td><td></td><td>***</td><td>***</td><td>***</td><td>***</td><td>***</td></tr><tr><td>NMF</td><td>+</td><td></td><td>***</td><td>***</td><td>***</td><td>***</td></tr><tr><td>SVD</td><td>+</td><td>+</td><td></td><td>***</td><td>***</td><td>+</td></tr><tr><td>ProbS</td><td>+</td><td>+</td><td>+</td><td></td><td>+</td><td>+</td></tr><tr><td>OSpl</td><td>+</td><td>+</td><td>+</td><td>***</td><td></td><td>+</td></tr><tr><td>USpl</td><td>+</td><td>+</td><td>***</td><td>***</td><td>***</td><td></td></tr></table>

Performance of different methods on MovieLens (69,814 users and 9888 objects) with cosine similarity measure. Abbreviations for criteria: MRR (mean rank ratio), RE (recall enhancement), MP (mean personality), MN (mean novelty). Results are mean (standard deviation) obtained by 10-fold cross-validation experiments. Note: The bold values mean the highest performance among all methods.

<table><tr><td>Method</td><td>MRR (STD) (%)</td><td>RE (STD)</td><td>MP (STD) (%)</td><td>MN (STD)</td></tr><tr><td>COUSIN</td><td>4.20 (0.01)</td><td>168.22 (0.60)</td><td>94.86 (0.03)</td><td> $2.98 (8 \times 10^{-4})$ </td></tr><tr><td>NMF</td><td>5.09 (0.06)</td><td>165.25 (1.75)</td><td>91.42 (0.41)</td><td> $2.30 (2 \times 10^{-2})$ </td></tr><tr><td>SVD</td><td>6.11 (0.02)</td><td>143.33 (0.43)</td><td>86.91 (0.06)</td><td> $2.07 (7 \times 10^{-4})$ </td></tr><tr><td>ProbS</td><td>5.84 (0.01)</td><td>124.85 (0.32)</td><td>70.52 (0.07)</td><td> $1.74 (5 \times 10^{-4})$ </td></tr><tr><td>OSpl</td><td>5.69 (0.01)</td><td>145.58 (0.45)</td><td>85.79 (0.13)</td><td> $2.24 (2 \times 10^{-3})$ </td></tr><tr><td>USpl</td><td>5.08 (0.01)</td><td>155.72 (0.37)</td><td>83.12 (0.04)</td><td> $2.01 (7 \times 10^{-4})$ </td></tr></table>

values, making the selection of the cutoff values not an important issue in the comparison of different methods. Results are summarized in details in the supplementary material (Section 2).

In addition, instead of performing a coarse-graining mapping of the rating to the binary form, we also conducted validation experiments based on the original ordinal scores, for methods in comparison. Although the values of the criteria on the ordinal data are a little different on contrast with those on the binary data, the proposed method COUSIN, uniformly outperforms all the other methods. Results are summarized in the supplementary material (Section 3).

Furthermore, to show the relationships between the ranks and the original ordinal scores of objects, we group objects according to their original preference rating scores (10-levels) and further partition objects into two groups, six groups and ten groups, respectively. Using the binary data as input, we present the mean rank ratio of each group and summarize the results in the supplementary material (Section 4). Using the original ordinal preference scores as input, we present the mean rank ratio of each group and summarize the results in the supplementary material (Section 5).

## 3.4. Contributions of different associations

Our method relies on three different associations as object relationships, user relationships and known connections between users and objects to make recommendation. It is therefore necessary to assess the contribution of different associations to the final performance of our method. Therefore, we first assessed the contribution of relationships between objects by permuting the object similarity matrix. Results show that after the permutation, our method achieves a mean rank ratio of 49.97%, a recall enhancement of 0.98, a mean personalization of 97.79%, and a mean novelty of 9.16. All these criteria is near to those of a random guess procedure, suggesting the indispensability of the object relationships to the performance of our final method. We further ran OSpl using the same parameter $( \alpha = 1 0 )$ as our method. Results show this method achieves a mean rank ratio of 6.01%, a recall enhancement of 123.51, a mean personalization of 79.39%, and a mean novelty of 2.00, as shown in Fig. 4. Since all these criteria are clearly inferior to those of COUSIN (Table 2), we conclude that the object similarity has positive contribution to the performance of our method.

![](/api/attachments/7VYAN2DQ/fulltext/images/462bce878240a29e8b28fe51e9e6d9e2e721c497df770822449ca4c7ff29e1ed.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/f4ecbe75f64061af74f8f78869db5fe53b28967fdee111e2bbf88a0b08b79b61.jpg)

We then assessed the contribution of relationships between users by permuting the user similarity matrix. Results show that after the permutation, our method achieves a mean rank ratio of 48.92%, a recall enhancement of 0.99, a mean personalization of 99.90%, and a mean novelty of 9.23. All these criteria is also near to those of a random guess procedure and thus support the indispensability of the user relationships to the performance of our final method. We further ran USpl using the same parameter (β = 5) as our method. Results show this method achieves a mean rank ratio of 5.08%, a recall enhancement of 155.72, a mean personalization of 83.12%, and a mean novelty of 2.01, as shown in Fig. 4. Since all these criteria are also inferior to those of COUSIN (Table 2), we conclude that the user similarity also has positive contribution to the performance of our method.

We then permuted the associations between users and objects in the regression model to assess the contribution of known links between users and objects. Results show that after the permutation, our method achieves a mean rank ratio of 47.22%, a recall enhancement of 1.18, a mean personalization of 99.65%, and a mean novelty of 9.21. All these criteria are obviously inferior to those of COUSIN (Table 2), suggesting the indispensability of the known links between users and objects to the performance of our final method.

Our method adopts a regression through the origin model to explain the similarity between two users using similarities between objects that the users have selected in history. It is therefore natural to ask how an ordinary regression model with both the intercept and the slope coefficients performs. To answer this question, we implemented a method called COUSIN-PCC that calculate the concordance score as the Pearson's correlation coefficient between a user similarity vector and an object similarity vector and optimized its performance by a grid search on the two parameters, α and β. Results suggest that the best performance of this method with $\alpha = 1 0$ and $\beta = 5$ is not as good as COUSIN, as shown in Fig. 4. For example, COUSIN-PCC achieves a mean rank ratio of 5.39%, a recall enhancement of 150.01, a mean personalization of 91.72% and a mean novelty of 2.51, and all the criteria are inferior to COUSIN (see Table 2). We therefore conjecture that the reason behind this observation is due to the fact that the regression through the origin model and the corresponding method for calculating the concordance score via the cosine measure are both more suitable in this situation.

![](/api/attachments/7VYAN2DQ/fulltext/images/a42a7f78d120e5021f1eb0b09c59fb596ab10f4411c2248d0f632e353b03c9fc.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/cc3c5f4b4bcc0c598ee66a7e5a979853ce2aac367c7bea352cae280213293f59.jpg)  
Fig. 3. Comparison of recommendation performance of different methods. Results are obtained by 10 independent runs of the 10-fold cross-validation experiments on the MovieLens dataset with cosine similarity measure. COUSIN clearly outperforms the others in recommendation accuracy and diversity performance. Method index: C (COUSIN), N (NMF), S (SVD), P (ProbS), O (Ospl), U (Uspl).

![](/api/attachments/7VYAN2DQ/fulltext/images/2e957b38723f36bee4d747a399f9bdc7e81e4fc60ce36327e0e6b8ed9092dd73.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/f4c3a736328859c09688ff21b0660f20686c459d29d84dbf97f2a6386ff0c609.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/3aa18a0cf05e5b6f0b30a9a63c9eebed4fc7618e401aad7bf1c196decf8e8f97.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/44c84644d97ac29c66b7f04745791b707bf39dd99c38c913e02991d132eb3750.jpg)  
Fig. 4. Contributions of individual components. The three information sources are object similarity, user similarity and known associations between objects and users. Method index: C (COUSIN), O (OSim with power law adjustment, using the same value of α = 5 as COUSIN), U (USim with power law adjustment, using the same value of β = 10 as COUSIN), P (COUSIN-PCC).

## 3.5. Influence of parameters

There are two parameters in our method: the power-law adjustment parameter for object similarities (α) and that for user similarities (β). By default, these parameters are set to $\alpha = 1 0$ and $\beta = 5 ,$ . It is therefore necessary to assess how these parameters influence the performance of in our method. We first performed a grid search by varying both parameters from 1 to 15 with step 1, and evaluated the performance of our method in the 10-fold cross-validation experiment on the MovieLens data set at each possible combination of the parameters values. The resulting landscape of the performance on evaluation criteria, as shown in Fig. 5, suggests that both parameters impact the accuracy and the diversity of our method significantly. Taking mean rank ratio as an example, at the optimal combination of the parameters $( \alpha = 1 0 \mathrm { a n d } \beta = 5 )$ , the value of this criterion is as good as 4.20%. However, with the parameters $\alpha = 1$ and $\beta = 1$ , the value of this criterion is as poor as 8.41%. This observation suggests that the selection of a reasonable combination of the parameters is indispensable to our method. Nonetheless, we also observe from Fig. 5 that around the optimal combination of the two parameters $( \alpha = 1 0$ and $\beta = 5 )$ , our method exhibits excellent performance in a wide range of these parameter values, suggesting the robustness of our method around this region.

We then studied in detail the influence of individual parameters around the optimal region. We first vary the power-law adjustment parameter for object similarities, α, from 5 to 15, while fixing the other parameter $\beta = 5$ as its default value. The performance of our method at different values of the parameter $\alpha _ { \ast }$ as shown in Fig. 6 (left), clearly suggests the robustness of our method to parameter α in a wide range. Taking the mean rank ratio as an example, with the increase of the parameter values, MRR improves slowly from 4.62% at $\alpha = 5$ to 4.20% at $\alpha = 1 0$ and then stabilizes around this value afterwards. As for the recall enhancement, we observe a similar improving and then stable patterns. Moreover, the performance on two diversity measures exhibits very stable patterns. These observations suggest that one can simply select the parameter of α in a wide range around the default value (α = 10) without losing the high performance of our method.

We then vary the power-law adjustment parameter for the user similarity, β, from 1 to 10, while fixing parameter α to its default value $( \alpha = 1 0 )$ . The performance of our method at different values of this parameter, as shown in Fig. 6 (right), suggests that one should take this parameter around its default value $( \beta = 5 )$ ). Taking the mean rank ratio as an example, at the default value $\beta = 5 ,$ , the MRR is 4.20%. When $\beta$ decreases, the MRR increases to 6.10% at $\beta = 1$ , suggesting small values of $\dot { \boldsymbol { \beta } }$ is not preferred. On the other hand, when $\beta$ increases towards large values, the MRR decreases to 4.08% at $\beta = 7$ and then increases to 4.20% when $\beta = 1 0 ,$ , suggesting a wide range around the default value of $\beta$ is preferred. The other accuracy measure, recall enhancement, and the two diversity measures, mean personalization and mean novelty, all demonstrate unimodal patterns, also suggesting the preference of neither small nor large values of ${ \bf \nabla } \cdot \beta .$ In detail, when $\beta$ increases from 1 to 10, the mean personalization increases from 79.11% to 95.18% (at $\beta = 6 )$ , and then decreases to 89.73% and the mean novelty increases from 1.90 to 3.12 $( \mathsf { a t } \beta = 6 )$ and then decreases to 2.71. Taking all these criteria into consideration, we conclude that a value around the default $( \beta = 5 )$ should be selected for the powerlaw adjustment parameter for user similarities.

3.6. Consistence of performance on different similarity measures and different data sets

We asked the question of whether the superior performance achieved by our method is consistent for different similarity measures. To answer this question, we replaced cosine similarity measure with

![](/api/attachments/7VYAN2DQ/fulltext/images/17fbb0c4768b6e951b229834604dac0573415ba94597a5c80a00f88d5d4fbea0.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/a06acddd6054238c35c342c2db98f0421adf38fe53c2c9b3424cbe394a5200d0.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/ae0089102e89d0bf2082f09c9930ec6e973a92e0e16acd29c158edb1f7350efe.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/37b41c52cf0b1fe76dfa94758fe2258ea5974ab385deb0d8626d10b911becdaf.jpg)  
Fig. 5. Performance Landscape of COUSIN on evaluation criteria with the combination of two parameters. Results are obtained by the 10-fold cross-validation experiments on MovieLens using cosine similarity measure through performing a grid search varying both power-law adjustment parameter for object similarities (α), and that for user similarities (β), from 1 to 15 with step 1. Results suggest that both parameters impact the accuracy and the diversity of COUSIN significantly.

Jaccard index and repeated the validation experiments. Not surprisingly, with Jaccard index and at the default parameter setting $( \alpha = 1 0$ and $\beta = 5 )$ , our method achieves a mean rank ratio of 4.26%, a recall enhancement of 158.21, a mean personalization of 95.81% and a mean novelty of 3.21. All these criteria are superior to those of NMF, the state-of-the-art method (see Table 2 for the criteria for NMF). We therefore conclude that the superiority of our method is consistent across different similarity measures instead of due to the selection of a certain similarity measure for characterizing relationships between objects and between users.

![](/api/attachments/7VYAN2DQ/fulltext/images/eea542f23c5f1aff252b4617dee1e1f7acb67f326e8b1c3a50fe5d6fef3b29a2.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/b001c08e34eb2bdccafddb2bf539fe796c1c89914ca7bc96df986ce76a53d7d2.jpg)  
Fig. 6. In uence of parameters. Left, performance of COUSIN on different values of the object similarity adjustment parameter ( ) with a xed value of = 5. Right, performance of COUSIN on different values of the user similarity adjustment parameter ( ) with a xed value of = 10.

Performance of different methods on Netflix (50,000 users and 16,560 objects) using cosine similarity measure. Abbreviations for criteria: MRR (mean rank ratio), RE (recall enhancement), MP (mean personality), MN (mean novelty). Results are mean (standard deviation) obtained by 10-fold cross-validation experiments. Note: The bold values mean the highest performance among all methods

<table><tr><td>Method</td><td>MRR (STD) (%)</td><td>RE (STD)</td><td>MP (STD) (%)</td><td>MN (STD)</td></tr><tr><td>COUSIN</td><td>4.34 (0.01)</td><td>197.68 (0.59)</td><td>94.87 (0.07)</td><td> $2.68 (2.2 \times 10^{-3})$ </td></tr><tr><td>NMF</td><td>5.03 (0.05)</td><td>187.25 (2.36)</td><td>91.40 (0.84)</td><td> $2.16 (2.5 \times 10^{-2})$ </td></tr><tr><td>SVD</td><td>5.62 (0.01)</td><td>178.40 (0.62)</td><td>90.25 (0.08)</td><td> $2.10 (4.0 \times 10^{-4})$ </td></tr><tr><td>ProbS</td><td>5.08 (0.01)</td><td>128.44 (0.44)</td><td>68.98 (0.07)</td><td> $1.79 (6.0 \times 10^{-4})$ </td></tr><tr><td>OSpl</td><td>4.93 (0.09)</td><td>140.21 (0.65)</td><td>81.98 (0.17)</td><td> $2.34 (1.1 \times 10^{-3})$ </td></tr><tr><td>USpl</td><td>5.03 (0.01)</td><td>168.18 (0.56)</td><td>86.08 (0.09)</td><td> $1.98 (1.2 \times 10^{-3})$ </td></tr></table>

We finally asked the question of whether the improvement achieved by our method are consistent between different data sets. To answer this question, we replaced the MovieLens dataset (69,814 users and 9888 objects) with the Netflix one (50,000 users and 16,560 objects) and repeated the validation experiments with the default parameter setting (α = 10 and $\beta = 5 )$ . Results, as shown in Table 3 and Fig. 7, suggest that the improvement in recommendation performance achieved by our method on the Netflix dataset is also consistent with that exhibited on the MovieLens one.

When compared with the existing state-of-the-art methods, we observe that our method shows the highest performance across all the evaluation criteria. For example, in terms of recommendation accuracy, our method achieves an MRR of 4.34% and a recall enhancement of 197.68, while NMF, as the best existing method, achieves an MRR of 5.03% and a recall enhancement of 187.25, both significantly worse than our method. In terms of the diversity measures, our method achieves a mean personalization of 94.87% and a mean novelty of 2.68, while NMF achieves a mean personalization of 91.40% and a mean novelty of 2.16, again significantly worse than our method. All these results suggest the superiority of our method over existing state-ofthe-art methods.

In this paper, we have considered both object relationships and user relationships in a recommendation procedure and proposed a regression through the origin model to explain similarities between users using similarities between objects that are associated with the users. We have analyzed the performance of this approach via 10-fold crossvalidation experiments. Results show the superior performance of our method over existing state-of-the-art methods across two independent datasets in different size in not only the accuracy but also the diversity of recommendations.

## 3.7. Conclusions and discussion

![](/api/attachments/7VYAN2DQ/fulltext/images/2e00a0c545ec8f7938c66a428025e53f5e854e7d94eed941069a1ecd388d1a2a.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/d24478a8fb450bb28131c9acd5d8dcd4884f574967841a134efca9e53c777668.jpg)

The success of our method can be attributed to a combination of several aspects. First, the power-law adjustment strategy effectively removes weak relationships that may adversely affect the calculation of similarities. Second, the combined use of not only user relationships but also object relationships in a single regression model improves the performance over methods that rely on one type of relationships alone. As a result, our method achieves significant improvements in the accuracy and diversity of personalized recommendations. Our method is therefore ready to be used in recommender systems that are based on the ordinary historical data to achieve easy yet reasonable improvements in performance.

Certainly, our approach can be further investigated from the following aspects. First, a natural question is how to determine the parameters in our model. Following a general cross-validation frame, we propose to sample a small set of data from the full dataset, perform cross-validations using the sampled data across different parameters, and select the parameter that gives us the desired performance. Considering that the cross-validation procedure could be computationally expensive, a method that can infer parameters by using statistical properties of the historical data is desired, and this will be one of the goals of our future studies. Second, the integrated use of both object relationships and user relationships, as we have demonstrated, is an effective way towards a high performance personalized recommender system. Although we have shown the feasibility of a regression model in this paper, there are certainly other statistical models such as diffusion and random walk process and graph algorithms such as the maximum flow that can be used. How to design an effective algorithm from these aspects with careful consideration of both types of relationships is one of our future work. Third, many information sources besides the historical data can be utilized to characterize objects, with examples include but not limited to contents, properties, tag annotations, etc. Each of these information sources can be finally converted to a type of object relationship. Similarly, there are also many information sources can be used to characterize relationships between users, with examples include but not limited to user social contacts with timestamp, social networks, trust networks, etc. Each of these information sources can also be converted to a type of user relationship. With such information, the scientific question will then be how to integrate multiple information sources towards to a recommendation system of even higher performance. Our method, build upon the regression model, can be extended from the viewpoint of multivariate regression, and thus provide a feasible solution to this data integration problem. Forth, theoretical analysis can be performed to further demonstrate the effectiveness of COUSIN.

![](/api/attachments/7VYAN2DQ/fulltext/images/0e98a50ee4f62eee8227d9a2df719a47e9b56b6669601ab0bda8dd5ae0d402d5.jpg)

![](/api/attachments/7VYAN2DQ/fulltext/images/4d5df8a159ffccc917f7418502de7b625d75af20afef3aa97354e2904d69796e.jpg)  
Fig. 7. Comparison of recommendation performance of different methods. Results are obtained by 10 independent runs of the 10-fold cross-validation experiments on the Netflix dataset with cosine similarity measure. COUSIN clearly outperforms the others in recommendation accuracy and diversity performance. Method index: C (COUSIN), N (NMF), S (SVD), P (ProbS), O (Ospl), U (Uspl).

## Appendix A. Supplementary material

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2015.12.001.

## References

[1] B. Jeong, J. Lee, H. Cho, Improving memory-based collaborative filtering via similarity updating and prediction modulation, Information Sciences 180 (2010) 602–612.

[2] G. Linden, B. Smith, J. York, Amazon. com recommendations: item-to-item collaborative filtering, Internet Computing, IEEE 7 (2003) 76–80.

[3] G. Nie, H. Xia, X. Li, An Ontology-based Approach on Intelligent Recommendation in Movie Field, in: A. DeHovos (Ed.) Proceedings of the 6th International Conference on Innovation and Management 2009, pp. 1489–1494.

[4] D. Wei, T. Zhou, G. Cimini, P. Wu, W.P. Liu, Y.C. Zhang, Effective mechanism for social recommendation of news, Physica A-Statistical Mechanics and Its Applications 390 (2011) 2117–2126.

[5] S. Prawesh, B. Padmanabhan, Probabilistic news recommender systems with feedback, Proceedings of the Sixth ACM Conference on Recommender Systems, ACM 2012, pp. 257–260.

[6] A.B. Barragáns-Martínez, E. Costa-Montenegro, J.C. Burguillo, M. Rey-López, F.A. Mikic-Fonte, A. Peleteiro, A hybrid content-based and item-based collaborative ltering approach to recommend TV programs enhanced with singular value decomposition, Information Sciences 180 (2010) 4290–4311.

[7] A.R. Sun, J. Cheng, D.D. Zeng, A novel recommendation framework for microblogging based on information diffusion, Proceedings of the 19th Workshop on In formation Technologies and Systems 2009, pp. 112–121.

[8] L. Backstrom, J. Leskovec, Supervised random walks: predicting and recommending links in social networks, Proceedings of the fourth ACM international conference on Web search and data mining, ACM 2011, pp. 635–644.

[9] M. Jamali, M. Ester, A matrix factorization technique with trust propagation for recommendation in social networks, Proceedings of the fourth ACM conference on Recommender systems, ACM 2010, pp. 135–142.

[10] D. Gavalas, C. Konstantopoulos, K. Mastakas, G. Pantziou, Mobile recommender systems in tourism Journal of Network and Computer Applications 39 (2014) 319–333

[12] T. Bogers, A. Van Den Bosch, Fusing recommendations for social bookmarking web sites International Journal of Electronic Commerce 15 (2011) 31–72

[13] R. Farzan, P. Brusilovsky, Social navigation support in a course recommendation system, Adaptive hypermedia and adaptive web-based systems, Springer 2006, pp. 91–100.

[14] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-Based Collaborative Filtering Recommendation Algorithms, in: Proceedings of the 10th International Conference on World Wide Web, ACM, Hong Kong, Hong Kong, 2001 285–295.

[15] F. Cacheda, V. Carneiro, D. Fernandez, V. Formoso, Comparison of collaborative filtering algorithms: limitations of current techniques and proposals for scalable, High-Performance Recommender Systems, ACM Transactions on the Web 5 (2011) 1–33.

[16] G. Biau, B. Cadre, L. Rouvière, Statistical analysis of k-nearest neighbor collaborative recommendation The Annals of Statistics 38 (2010) 1568-1592

[17] A. Moreno, C. Ariza-Porras, P. Lago, C.L. Jiménez-Guarín, H. Castro, M. Riveill, Hybrid model rating prediction with linked open data for recommender systems, Semantic Web Evaluation Challenge, Springer 2014, pp. 193–198.

[18] Y. Shi, M. Larson, A. Hanjalic, Collaborative filtering beyond the user-item matrix: a survey of the state of the art and future challenges, ACM Computing Surveys (CSUR) 47 (2014) 3.

[19] R. Burke, Hybrid recommender systems: survey and experiments, User Modeling and User-Adapted Interaction 12 (2002) 331–370

[20] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommendation algorithms, Proceedings of the 10th International Conference on World Wide Web, ACM 2001, pp. 285–295.

[21] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (2005) 734–749.

[22] M. Balabanović, Y. Shoham, Fab: content-based, collaborative recommendation, Communications of the ACM 40 (1997) 66–72.

[23] H.-N. Kim, I. Ha, K.-S. Lee, G.-S. Jo, A. El-Saddik, Collaborative user modeling for enhanced content filtering in recommender systems, Decision Support Systems 51 (2011) 772–781.

[24] T. Hofmann, Latent semantic models for collaborative filtering, ACM Transactions on Information Systems 22 (2004) 89–115.

[25] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (2009) 30 37.

[26] A. Paterek, Improving regularized singular value decomposition for collaborative filtering, Proceedings of KDD cup and workshop 2007, pp. 5–8.

[27] M. Gan, Walking on a user similarity network towards personalized recommendations, PLoS ONE 9 (2014) e114662, http://dx.doi.org/10.1371/journal.pone. 0114662.

[28] M.-S. Shang, Z.-K. Zhang, T. Zhou, Y.-C. Zhang, Collaborative filtering with diffusionbased similarity on tripartite graphs, Physica A: Statistical Mechanics and its Applications 389 (2010) 1259–1264.

[29] M.-S. Shang, Z.-K. Zhang, Diffusion-based recommendation in collaborative tagging systems, Chinese Physics Letters 26 (2009) 118903.

[30] T. Zhou, Z. Kuscsik, J.G. Liu, M. Medo, J.R. Wakeling, Y.C. Zhang, Solving the apparent diversity-accuracy dilemma of recommender systems, Proceedings of the National Academy of Sciences of the United States of America 107 (2010) 4511–4515.

[31] M. Gan and R. Jiang, ROUND: Walking on an object-user heterogeneous network for personalized recommendations, Expert Systems With Applications 42, 8791–8804. http://dx.doi.org/10.1016/j.eswa.2015.07.032.

[32] M. Jamali, M. Ester, TrustWalker: a random walk model for combining trust-based and item-based recommendation, Proceedings of the 15th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM 2009, pp. 397–406.

[33] D.J. Watts, S.H. Strogatz, Collective dynamics of ‘small-world'networks, Nature 393 (1998) 440-442

[34] A.-L. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[35] M. Girvan, M.E. Newman, Community structure in social and biological networks Proceedings of the National Academy of Sciences 99 (2002) 7821–7826

[36] A. Anagnostopoulos, R. Kumar, M. Mahdian, Influence and correlation in social networks, Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2008, pp. 7–15.

[37] J.H. Fowler, N.A. Christakis, The dynamic spread of happiness in a large social network, BMJ 337 (2008) a2338.

[38] J. Whitfield, The Secret of Happiness: Grinning on the Internet, Nature, 2008.

[39] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions JEEE Transactions op Knowledge and Data Engineering 17 (2005) 734–749.

[40] A.K. Milicevic, A. Nanopoulos, M. Ivanovic, Social tagging in recommender systems: a survey of the state-of-the-art and possible extensions. Artificial Intelligence Review 33 (2010) 187–209.

[41] M. Gan, R. Jiang, Improving accuracy and diversity of personalized recommendation through power law adjustments of user similarities, Decision Support Systems 55 (2013) 811–821.

[42] M. Gan, R. Jiang, Constructing a user similarity network to remove adverse influence of popular objects for personalized recommendation, Expert Systems with Applications 40 (2013) 4044-4053

[43] S. Kabbur, G. Karypis, NLMF: NonLinear Matrix Factorization Methods for Top-N Recommender Systems, Data Mining Workshop (ICDMW), 2014 IEEE international conference on, IEEE 2014, pp. 167–174.

[44] T. Zhou, J. Ren, M. Medo, Y.-C. Zhang, Bipartite network projection and personal rec ommendation, Physical Review E 76 (2007) 046115.

Mingxin Gan received her BS in Automation from Tsinghua University in Beijing, China, in 2001, and PhD in Management Science and Engineering from Beijing Institute of Technology in 2006. She is currently an Associate Professor in the Department of Management Science and Engineering, Donlinks School of Economics and Management, University of Science and Technology Beijing. Her current research interests include recommender systems, information retrieval, complex networks analysis, text mining and knowledge management. She can be reached at Donlinks School of Economics and Management, University of Science and Technology Beijing, Beijing 100083, China; ganmx@ustb.edu.cn.
