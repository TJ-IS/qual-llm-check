---
otero_id: 14704
otero_key: "SM3UG42T"
title: "<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" altimg=\"si1.gif\" overflow=\"scroll\"><mml:mrow><mml:mi>β</mml:mi><mml:mi mathvariant=\"script\">P</mml:mi></mml:mrow></mml:math>: A novel approach to filter out malicious rating profiles from recommender systems"
authors: "Chen-Yao Chung; Ping-Yu Hsu; Shih-Hsiang Huang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.020"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# β : A novel approach to <sup>fi</sup>lter out malicious rating pro<sup>fi</sup>les from recommender systems

Chen-Yao Chung, Ping-Yu Hsu ⁎, Shih-Hsiang Huang

Department of Business Administration, National Central University, No. 300, Jhongda Rd., Jhongli City, Taoyuan County, Taiwan

## a r t i c l e i n f o

Article history: Received 25 June 2012 Received in revised form 11 November 2012 Accepted 24 January 2013 Available online 4 February 2013

Keywords: Shilling attacks detection Collaborative <sup>fi</sup>ltering Recommender systems

## a b s t r a c t

Recommender systems are widely deployed to provide user purchasing suggestion on eCommerce websites. The technology that has been adopted by most recommender systems is collaborative <sup>fi</sup>ltering. However, with the open nature of collaborative <sup>fi</sup>ltering recommender systems, they suffer signi<sup>fi</sup>cant vulnerabilities from being attacked by malicious raters, who inject pro<sup>fi</sup>les consisting of biased ratings. In recent years, several attack detection algorithms have been proposed to handle the issue. Unfortunately, their applications are restricted by various constraints. PCA-based methods while having good performance on paper, still suffer from missing values that plague most user–item matrixes. Classi<sup>fi</sup>cation-based methods require balanced numbers of attacks and normal pro<sup>fi</sup>les to train the classi<sup>fi</sup>ers. The detector based on SPC (Statistical Process Control) assumes that the rating probability distribution for each item is known in advance. In this research, Beta-Protection ( β ) is proposed to alleviate the problem without <sup>P</sup>the abovementioned constraints. β grounds its theoretical foundation on Beta distribution for easy compu-<sup>P</sup>tation and has stable performance when experimenting with data derived from the public websites of MovieLens.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

To overcome the phenomenon of information overload, many academic researches and practical applications related to recommender systems have been proposed. Recommender systems can extract patterns to generate recommendations and provide useful information to users for decision making. Recommender systems typically apply content-based <sup>fi</sup>ltering, collaborative <sup>fi</sup>ltering, or hybrid approaches to suggest products that users may <sup>fi</sup>nd “interesting” in many internet commerce settings [14,38,44]. Among them, collaborative <sup>fi</sup>ltering is the most popular personalized recommendation method in recommender systems. Examples of collaborative <sup>fi</sup>ltering recommender systems include GroupLens, Ringo [20,34] and Amazon [23].

Most collaborative <sup>fi</sup>ltering methods rely on a user–item matrix (also called user–product matrix) which comprises user pro<sup>fi</sup>les offered by users to record their preference ratings toward each product [2,9,38]. If the quality of the matrix data is in doubt, the accuracy of the recommendations can be questionable. Therefore, maintaining the integrity of the matrix is an essential task for making meaningful recommendations. Issues related to the integrity of the matrix can be classi<sup>fi</sup>ed into three categories: slow start of the new items or new users, sparse ratings and abnormal ratings from malicious raters. The <sup>fi</sup>rst two problems are widely known as “cold start” and “data sparseness”, respectively [19,24,32]. The third problem is often called “shilling attacks” [8,22,30,37] or the problem of “pro<sup>fi</sup>le injection attacks” [5].

These so-called shilling attacks or pro<sup>fi</sup>le injection attacks [5,8,22,30,37] can be done by introducing attacking pro<sup>fi</sup>les which consist of biased ratings under spurious identities. The ratings within questionable pro<sup>fi</sup>les targeting a particular item can be rated extremely high (called push attacks) or low (called nuke attacks) [28,30,31]. Essentially, the aim of shilling attacks is to shift the predicted ratings of a particular item to affect the recommendations for genuine users. At least two known attacks on Amazon.com have been published in the past. The <sup>fi</sup>rst event is that of a well-known company injecting fake quotes into systems to promote its <sup>fi</sup>lms [35]. The second one involved malicious authors with <sup>fi</sup>ctitious identities inserting biased ratings into the systems to promote their books [29]. If the attackers get their way often, users trust toward the recommender systems will diminish.

To <sup>fi</sup>ght back against shilling attacks, both user-based and item-based detection algorithms have been proposed to identify the attack pro<sup>fi</sup>les and weed them out from the dataset before generating recommendations. Pro<sup>fi</sup>le-based algorithm is developed to identify the abnormal pro<sup>fi</sup>les, by screening the rating vectors of each user in the user–item matrix, while the item-based detection algorithm is devised to <sup>fi</sup>nd the items under attack with item vectors within the user–item matrix. Pro<sup>fi</sup>le-based detection algorithms can be further divided into two categories, namely, classi<sup>fi</sup>cation-based detection and outlier detection. The classi<sup>fi</sup>cation-based approach exploits a classi<sup>fi</sup>cation model built in advance to predict whether a new pro<sup>fi</sup>le is an attacker [5,6,8,13,28]. PCA (Principal Component Analysis) based method transforms the entire user–item matrix to a hyper-plane and represents each pro<sup>fi</sup>le with three principal components. Pro<sup>fi</sup>les that are closed to the origin of the hyper-plane are identi<sup>fi</sup>ed as attackers [13,25–27].

The classi<sup>fi</sup>cation-based method requires balanced numbers of positive and negative cases, which in the real world are not easy to collect since negative cases may go unnoticed and do not happen as often as normal cases anyway. Even though there are known methods to treat imbalanced cases, the result is mixed [3,21,40]. The PCA-based method on the other hand cannot handle missing values in the user–item matrix. All missing values have to be transferred to estimated values, which are computed from values residing on cells around the missing values. However, as it is well known that most user–item matrixes are sparse due to users possibly not having known or having bought all the items on offer, the quality of the estimated values is itself questionable. Besides, with the principal component transformation, it is dif<sup>fi</sup>cult to explain the clustering result with the original data.

The item-based approaches identify items under attack by picking up items whose preference scores are beyond boundaries [4]. The approach is based on the SPC (Statistical Process Control) technique to detect anomaly ratings for each individual item. The boundary is composed of two horizontal lines called upper and lower control limits, which are estimated with historical ratings. Unfortunately, the approach can only alert managers that an item is under attack but lacks the ability to exactly pinpoint which raters are the culprits.

In summarizing prior work, an ideal detection algorithm should have the following characteristics: (1) high detection rate and low false alarm rate (2) ability to identify attack pro<sup>fi</sup>les without an abundant number of negative cases, (3) immunity to missing values, and (4) the results should be easy to explain so that users can decide if any parameters need to be <sup>fi</sup>ne tuned. In this research, an unsupervised algorithm based on Beta probability distribution is proposed to detect attackers with all the desired features. The proposed approach strives to identify as many attackers as possible while keeping as many normal users intact as possible. The formula employed is easy to understand and is immune to missing values.

The data used in the experiments come from the MovieLens database offered by GroupLens Research Lab [1]. The effectiveness of the approach is evaluated with the measure of detection rate and false alarm rate. Detection rates can be achieved at or close to 100% under two quantiles 0.00142 and 8E-14 respectively when attackers mount average push or nuke attacks. And false alarm rates are very stable under all kinds of attacks. Besides, in the experiments, we introduce a new attack concept with multiple-targets in each single pro<sup>fi</sup>le, while all prior published works assume raters attack one target in each pro<sup>fi</sup>le. The results have shown that the proposed approach has similar effectiveness when facing both single and multiple-target attacks. Finally, the experimental results also show that our proposed approach outperforms the PCA-based method.

The remainder of the paper is structured as follows. Section 2 provides a brief overview of related research. Section 3 presents the proposed algorithm. The experimental results are shown and discussed in Section 4. Section 5 highlights the conclusions and future work of the research.

## 2. Related work

With the popularity of rating and recommender systems, some have started to exploit avenues to populate the user–item matrix with biased data to gain unfair bene<sup>fi</sup>t [29,35]. In order to secure the collaborative <sup>fi</sup>ltering recommender systems against these attacks, several researches have been proposed to detect and remove malicious attacks [4–6,8,25–28]. User pro<sup>fi</sup>les generated by attackers are segmented into four partitions for more detailed examinations. These are target-item, <sup>fi</sup>ller-item, selected-item and unrated-item partitions. Ratings in target-item partitions are aimed at promoting or demoting these items. Ratings in <sup>fi</sup>ller-item partition are used to neutrally <sup>fi</sup>ll up pro<sup>fi</sup>les to make it look like a normal user pro<sup>fi</sup>le. Ratings in selected-item partition are particularly high or low to associate the pro<sup>fi</sup>les with users who like or distaste some products. Unrated-item partitions are the vacant rating areas. As a result, several indicators are de<sup>fi</sup>ned to identify abnormal patterns of <sup>fi</sup>ller-item partitions, and selected-item partitions issued by attackers.

Based on detected objects, the works can be divided into user-based or item-based anomaly detection algorithms. The userbased algorithms detect anomaly within user pro<sup>fi</sup>les in the user– item matrix. Each user pro<sup>fi</sup>le is a vector of scores ranked by a user to all items. The item-based algorithm treats ratings of each item as a vector. There are basically two approaches to detect anomaly users. One is by classifying user pro<sup>fi</sup>les into two types, namely, normal and abnormal [5,6,8,28]. This type of method requires training pro<sup>fi</sup>les of both normal and attackers. The other is by treating attackers as outliers [25–27]. This type of method takes only normal pro<sup>fi</sup>les as training data and treats abnormal pro<sup>fi</sup>les as attacks.

To measure the malicious degrees of a given set of user pro<sup>fi</sup>les, <sup>fi</sup>ve indexes have been proposed and employed by several classi<sup>fi</sup>cationbased methods [8]. The indexes are Number of Prediction-Differences (NPD), Standard Deviation in User's Ratings (SDUR), Degree of Agreement with Other Users (DAOU), Degree of Similarity with Top Neighbors (DSTN), and Rating Deviation from Mean Agreement (RDMA). NPD is the change of an item's rating, if the pro<sup>fi</sup>les in question are removed. The more signi<sup>fi</sup>cant the change, the more suspicious the user is. The name of SDUR is self-explanatory. The author claims that users with close to 0 SDUR are attackers. DAOU is the rating differences given by a suspected user and average users to each item. The sharper the difference, the likelier the suspect is an attacker. DSTN measures the similarity of ratings given by a user and his/her nearest neighbors. Since attackers have to generate a large number of user pro<sup>fi</sup>les to affect ratings, the attacking pro<sup>fi</sup>les should be very similar to each other. Therefore, user pro<sup>fi</sup>les with high DSTN are likely to be generated by the same attacker. RDMA is DAOU divided by number of users who actually rated the items.

Equipped with the abovementioned indicators, several classi<sup>fi</sup>cation models are proposed to separate attackers from genuine users based on user pro<sup>fi</sup>les [5,6,28]. Two types of indicators are employed in the classi<sup>fi</sup>cation models, namely, generic and model speci<sup>fi</sup>c. Adopted versions of the abovementioned indicators are deployed as generic indicators. Model speci<sup>fi</sup>c indicators are designed for known attack models, each of which has tailor made indicators. All classi<sup>fi</sup>cation-based methods have to face the issue of a scarcity of negative cases. Comparing to normal user pro<sup>fi</sup>les, negative pro<sup>fi</sup>les are very dif<sup>fi</sup>cult to collect since attacks do not happen every day and when they do happen, the corresponding pro<sup>fi</sup>les may not be that easy to capture. Therefore, the demon of data skew that threatens all classi<sup>fi</sup>ers with uneven data has to be tamed before the classi<sup>fi</sup>ers can identify human attackers [3,21,40]. Another approach based on the Neyman–Pearson theory is proposed to classify users with the assumption that the statistical models of genuine users and attackers can be known in advance [13].

In [25–27], a PCA-based approach is proposed to treat attack pro-<sup>fi</sup>les as outliers. In essence, the PCA method is one of the multivariate analysis techniques that can be applied to detect outlier variables. In these approaches, the ratings in the user pro<sup>fi</sup>les are interpreted as variables. The values in the variables are projected to a space composed by three principal components, which have the highest correlations with the ratings in user pro<sup>fi</sup>les. As a result, each user pro<sup>fi</sup>le is translated to a three-element vector in the space constructed by the principal components. Outliers of user pro<sup>fi</sup>les are supposed to be very close to the origin of the space since they share little commonality with normal pro<sup>fi</sup>le and should have zero correlation with the three principal components. The approach can only be applied to a dense user–item matrix since PCA cannot tolerate null values, which have to be replaced by estimated values. However, in reality, very few users have the experience to purchase all items or care to rate all items. Therefore, sparse user–item matrix is very common among recommender systems.

Instead of detecting attackers, item-based approaches identify items under attack without knowing who are attacking the items [4]. Item-based approaches employ the SPC technique, which monitors the trend of the observation values and reports exceptions when the observed value deviates outside three standard deviations of the average. The method can only alarm managers which items are under attack but cannot remove the malicious pro<sup>fi</sup>les.

Another approach to fend off an attack on the user–item matrix is to discard the user–item matrix altogether and design a recommender algorithm with alternative approaches, such as association rules [37]. However, to make sensible recommendation and yet be immune to user attacks, all items have to be purchased frequently in the transaction data bank. This will add more aggravation to the already severe cold start problems of recommender systems.

Another area of related research is in identifying biased product reviews composed by texts and evaluating the impact of biased review on sales ranking [7,10–12,18,33,39,45]. The research is based on observations that consumer opinions can be manipulated by biased review comments. Therefore, biased review comments should be viewed as a form of attack on review feedback systems. Methods based on sentiments of review comments, sequences of review comments and readability have been proposed to identify biased review comments. Even though this is a very important research area, biased review comment identi<sup>fi</sup>cation is not the subject of this study, which focuses on identifying malicious users who give biased scores.

The research proposes a novel yet easy to implement method to identify and remove biased and malicious user pro<sup>fi</sup>les. The proposed algorithm is immune to the issue of null values and does not need negative training data and is therefore immune from the problem of data skew. Besides, none of the abovementioned algorithms try to detect multiple-target attacks launched at the same time. They all assume that only one item is under attack in each pro<sup>fi</sup>le. The proposed method, on the other hand, is also effective in detecting multiple-target attacks launched at the same time.

## 3. The proposed methodology

The method is termed as Beta-Protection (β ) which is based on <sup>P</sup>Beta distribution to detect and remove user pro<sup>fi</sup>les. Beta distribution is known for its capability to model various shapes of data distribution via tuning two parameters, namely α and β. The distribution is a continuous Probability Density Function (PDF) on (0, 1) indexed by two parameters, namely α and $\beta .$ The Beta PDF denoted by f(x|α, β) can be expressed with Gamma function Γ as the following:

$$
f (x | \alpha , \beta) = \frac {\Gamma (\alpha + \beta)}{\Gamma (\alpha) \Gamma (\beta)} p (x) ^ {\alpha - 1} (1 - p (x)) ^ {\beta - 1}, 0 <   p <   1, \alpha > 0, \beta > 0\tag{1}
$$

p in Eq. (1) denotes the prior probability of observing the events indeed happens. With the tuning of the values of α and $\beta ,$ Beta distribution exhibits various shapes of distribution plots. The expected value (μ) of a Beta distribution random variable p with parameters α and β is shown as:

$$
E (p) = \alpha / (\alpha + \beta)\tag{2}
$$

In case observing the events are binary independent, and r and s denote the number of success and failure trials, respectively, then $\alpha { = } r { + } 1$ and $\beta = s + 1$ . As a result, Eq. (2) is equivalent to

$$
E (p) = (r + 1) / (r + s + 2)\tag{3}
$$

For details of the inference, please refer to [15,42].

The <sup>fl</sup>exibility and the value of p being within 0 and 1 make the Beta distribution ideal for modeling user feedback in online stores since feedback is skewed toward the positive with certain probability. Therefore, the Beta distribution has been adapted to model user feedback given to online sellers [15–17,42]. Each rating to a seller is modeled as an event of Beta distribution with a prior probability of the seller being awarded with positive comments. User feedback is restricted to positive and negative only in the abovementioned work.

On the other hand, the research will apply the Beta distribution to model user feedback on ordinal data of Likert Scale to identify attackers. Several transformations of user feedback are in order. The transformations along with anomaly detection algorithms will be presented in the following subsections.

## 3.1. The problem definition

User feedback is stored in a user–item matrix in most collaborative <sup>fi</sup>ltering recommender systems. Given m raters and n items, let $U { = } \{ u _ { 1 } , u _ { 2 } , . . . , u _ { \mathrm { m } } \}$ and $I = \{ i _ { 1 } , i _ { 2 } , . . . , i _ { \mathrm { n } } \}$ . The user–item matrix $R _ { U \times I }$ is a m×n matrix. Each entry $r _ { k , j }$ in $R _ { U \times I }$ expresses the preference rating of user $u _ { k }$ on item $i _ { j } ,$ and $r _ { k , j }$ is a value on the Likert Scale denoting the raters' preference. $\mathrm { I f } \ A = \{ a _ { 1 } , a _ { 2 } , . . . , a _ { z } \}$ is a set of attackers, then a user–item matrix $R _ { ( U + A ) \times I }$ is ${ \textsf { a } } \left( m + z \right) \times n$ matrix with the addition of the attackers. $\beta \mathcal { P }$ is to remove as many users from $R _ { ( U + A ) \times I }$ and <sup>P</sup>keep as many users in U solely with the data in $R _ { ( U + A ) \times I } .$

Shilling attack detections are basically binary classi<sup>fi</sup>cations with imbalanced dataset [13,41]. The most classes are called “genuine pro-<sup>fi</sup>les”, while the rare classes are called “attack pro<sup>fi</sup>les”. There are two primary measures to evaluate the effectiveness of the proposed algorithms, namely detection rate and false alarm rate. The detection rate is de<sup>fi</sup>ned as the number of attack pro<sup>fi</sup>les being correctly detected di vided by the total number of malicious pro<sup>fi</sup>les. The measure can be formally stated by the following formula:

$$
\text { detection   rate } = | D \cap A | / | A |\tag{4}
$$

where D is the set of the detected user pro<sup>fi</sup>les by the proposed algorithm. The false alarm rate is de<sup>fi</sup>ned as the number of genuine pro<sup>fi</sup>les that are identi<sup>fi</sup>ed as attacks divided by the number of genuine pro<sup>fi</sup>les. This measure can be formally stated by the following formula:

$$
\text { false   alarm   rate } = | D \cap U | / | U |\tag{5}
$$

β is aimed to have high detection rate and low false alarm rate even when more than one item is attacked in a user pro<sup>fi</sup>le.

In β , a three-phase screening approach is deployed to weed out <sup>P</sup>attacker pro<sup>fi</sup>les. In the <sup>fi</sup>rst phase, users who rate extremely low numbers of items are singled out as abnormal since attackers have to deliberately give scores to <sup>fi</sup>ller items, which therefore can be very few in some attacking pro<sup>fi</sup>les. In the second and third phases, raters who give extreme scores when giving positive and negative feedback are identi<sup>fi</sup>ed, respectively. Raters who are judged as abnormal in at least two phases are viewed as attackers. All three screening detections are based on the same theory, namely, the characteristics of Beta distribution, to identify attackers. In the <sup>fi</sup>rst phase, the characteristic applied is on the distribution of items being rated. In the second and third phases, the characteristic is applied on the scores given by raters.

## 3.2. Counting the probability of items being rated

De<sup>fi</sup>nition 1. Given a set of users, U, a set of items, I, and a user–item matrix, $R _ { U \times 1 }$ I

a. A <sup>fi</sup>lled user rating set, $S _ { u } { ^ + }$ for user, u, based on $R _ { U \times I }$ is de<sup>fi</sup>ned as

$$
S _ {u} ^ {+} (R) = \{x | \forall i \in I, x = R (u, i), x \text {   is   not   null } \}
$$

b. Similarly, a null user rating set, ${ S _ { u } } ^ { - }$ for user, u, based on $R _ { U \times I }$ is de<sup>fi</sup>ned as

$$
S _ {u} ^ {-} (R) = \left\{x \mid \forall i \in I, x = R (u, i), x \notin S _ {u} ^ {+} (R) \right\}
$$

c. The <sup>fi</sup>lled and null rating sets for the entire population of U, are denoted as $S ^ { + }$ and S<sup>−</sup>, where

$$
\begin{array}{l} S ^ {+} (R) = \cup_ {u \in U} S _ {u} ^ {+} (R) \\ S ^ {-} (R) = \cup_ {u \in U} S _ {u} ^ {-} (R) \end{array}
$$

Theorem 1. Given a set of user U, a set of item I and a user–item matrix ${ \cal R } _ { U \times I } , { \cal I f p r i }$ s the probability of a user giving a rating to an item then the expected value of pr based on the prior knowledge is

$$
E (p r) = \frac {\left| S ^ {+} (R) \right| + 1}{\left| U \right| \times \left| I \right| + 2}
$$

Proof.

$$
\begin{array}{l} E (p r) = \frac {\left| S ^ {+} (R) \right| + 1}{\left| S ^ {+} (R) \right| + \left| S ^ {-} (R) \right| + 2}, \quad a c c o r d i n g t o f o r m u l a (3) \\ = \frac {\left| S ^ {+} (R) \right| + 1}{\left| U \right| \times \left| I \right| + 2} \end{array}
$$

#

If a user u is a normal rater in U, then the expected value of he/she giving a rating to an item should be closed to $E ( p r )$ . In another word, if the expected value is in the extreme quantile of a rater's distribution, then the rater is very likely to be an outlier.

Example 1. Considering the user–item matrix R listed in Table $1 , U =$ $\{ u _ { 1 } , u _ { 2 } , u _ { 3 } , u _ { 4 } \}$ and $I = \{ i _ { 1 } , i _ { 2 } , i _ { 3 } , i _ { 4 } \}$ . The <sup>fi</sup>lled rating set of u is

Table 1 A sample of a user–item matrix, R.

<table><tr><td></td><td> $i_{1}$ </td><td> $i_{2}$ </td><td> $i_{3}$ </td><td> $i_{4}$ </td></tr><tr><td> $u_{1}$ </td><td>1</td><td>5</td><td></td><td>2</td></tr><tr><td> $u_{2}$ </td><td>4</td><td></td><td>3</td><td>5</td></tr><tr><td> $u_{3}$ </td><td></td><td>4</td><td>3</td><td>2</td></tr><tr><td> $u_{4}$ </td><td>2</td><td></td><td>5</td><td></td></tr></table>

$S _ { u _ { 1 } } ^ { + } ( R ) = \{ 1 , 5 , 2 \}$ , and the null rating set of u is $S _ { u _ { 1 } } ^ { - } ( R ) = \{ n u l l \}$ <sup>ð Þ ¼ f g</sup>With the same argument, $S _ { u _ { 2 } } ^ { + } ( R ) = \{ \bar { 4 } , 3 , 5 \} , S _ { u _ { 2 } } ^ { - } ( R ) = \{ \stackrel {  } { n } u l l \} , S _ { u _ { 3 } } ^ { + } ( R ) =$ $\{ 4 , 3 , 2 \} , S _ { u _ { 3 } } ^ { - } ( R ) = \{ n u l l \} , S _ { u _ { 4 } } ^ { + } ( \bar { R } ) = \{ 2 , 5 \} , S _ { u _ { 4 } } ^ { - } ( \bar { R } ) ^ { - } = \{ n u l l$ <sup>g ð Þ ¼</sup>; null . As a re-<sup>f</sup>sult, $\begin{array} { r } { S ^ { + } ( \vec { R } ) = \{ 1 , 5 , 2 , 4 , 3 , 5 , 4 , 3 , 2 , 2 , 5 \} . ~ S ^ { - } ( \vec { R } ) = } \end{array}$ <sup>Þ ¼ f g</sup>{null,null,null,null,null}. $\begin{array} { r } { E ( p r ) = \frac { \left| S ^ { + } ( R _ { 4 \times 4 } ) \right| + 1 } { \left| S ^ { + } ( R _ { 4 \times 4 } ) \right| + \left| S ^ { - } ( R _ { 4 \times 4 } ) \right| + 2 } = \frac { 1 1 + 1 } { 1 1 + 5 + 2 } = 0 . 6 7 . } \end{array}$

Property I. According to [36], given the PDF, f, of a beta distribution, pr, and a quantile, $q _ { \mathcal { F } } ,$ there exist unique threshold $b _ { n } ,$ bound for number of <sup>F</sup>rated items, such that:

$$
q _ {\mathcal {F}} = \int_ {b _ {n}} ^ {1} f (p r)
$$

With the property, the boundary value, $b _ { n } ,$ can be calculated for each rater given the $q _ { \mathcal { F } } . \mathsf { A s } :$ a result, if the expected value of the entire <sup>F</sup>population falls into the range $\left( b _ { n } , \ 1 \right)$ of a rater, then the rater is judged as abnormal.

## 3.3. Converting Likert ratings to Tri-Value ratings

In general, the preference ratings in recommender systems are represented by <sup>fi</sup>ve or seven degree of Likert Scale (i.e. a scale from 1 to 5 or from 1 to 7), whereas the binary Beta distribution takes only binary ratings as input. Several conversions based on the same rules have to be performed to convert the ratings into binary values to be used in phases two and three of $\beta \mathcal { P }$

De<sup>fi</sup>nition 2. Given a user set U, an item set I, a user item matrix of $R _ { U \times I } ,$ a left delimiter LD, a neutral value NV, and a right delimiter RD, a transformed matrix, $T ^ { L D , N V , R D }$ is de<sup>fi</sup>ned as

$$
T ^ {L D, N V, R D} (u, i) = \left\{ \begin{array}{l l} v ^ {+} & \text { if } R D \geq R _ {U \times I} (u, i) > N V \\ v & \text { if } R _ {U \times I} (u, i) = N V \\ v ^ {-} & \text { if } L D \leq R _ {U \times I} (u, i) <   N V \end{array} \right.
$$

Besides expediting computation, the conversion rules also can protect the systems against obfuscating attacks [39]. In obfuscating, attack pro<sup>fi</sup>les are disguised as genuine pro<sup>fi</sup>les and deviate from known attack pro<sup>fi</sup>les. The obfuscating attacks are mounted with two avenues, noise injection and target shifting. Noise injection is that each rating within a subset of the union of <sup>fi</sup>ller-item and selected-item partitions is multiplied by a random number generated from a Gaussian distribution. Target shifting is that the vote on a target item has to be shifted to one step lower than maximal rating for push attacks while shifted to one step above the minimal rating for nuke attacks. The conversion rules can foil the plot since a range of high (low) scores is converted to the same value.

Example 2. Given the left delimiter $L D = 3 ,$ the neutral value $N V { = } 4$ and the right delimiter $R D = 5 ,$ the value of $T ^ { 3 , 4 , 5 }$ are listed in Table 2.

## 3.4. Creating rating sets from Transformed matrix

Rating sets based on the transformed matrix $T ^ { L D , N V , R D }$ are created to describe user preferences. Each user is associated with a rating set and the entire user set is associated with an aggregated rating set.

A sample transformed matrix, $T ^ { 3 , 4 , 5 } .$

<table><tr><td></td><td> $i_1$ </td><td> $i_2$ </td><td> $i_3$ </td><td> $i_4$ </td></tr><tr><td> $u_1$ </td><td></td><td> $v^+$ </td><td></td><td></td></tr><tr><td> $u_2$ </td><td>v</td><td></td><td> $v^-$ </td><td> $v^+$ </td></tr><tr><td> $u_3$ </td><td></td><td>v</td><td> $v^-$ </td><td></td></tr><tr><td> $u_4$ </td><td></td><td></td><td> $v^+$ </td><td></td></tr></table>

When creating the rating sets, each $\nu ^ { + }$ and v<sup>−</sup> in the matrix generates the same element in the set; while a v in the matrix generates both $v ^ { + }$ and v<sup>−</sup> in the set and a null value generates no entries in the set.

A neutral rating is generated from two ratings simultaneously to distinguish neutral opinions from null opinion. There can be up to 90% of null values in the matrix. Besides reasonably representing ratings, increasing both ratings also has the bene<sup>fi</sup>t of stabilizing the estimated expected value of the corresponding distribution to fending off malicious attacks.

De<sup>fi</sup>nition 3. Given a set of users, U, a set of I, and a transformed matrix, $T ^ { L D , N V , R D }$

a. A high user rating set, $Q _ { u } { ^ + }$ for user, u, based on $T ^ { L D , N V , R D }$ is de<sup>fi</sup>ned as

$$
Q _ {u} ^ {+} \left(T ^ {L D, N V, R D}\right) = \left\{x \mid \forall i \in I, t = T ^ {L D, N V, R D} (u, i), t = v ^ {+} \vee t = v \rightarrow x = v ^ {+} \right\}
$$

b. Similarly, a low user rating set, $\boldsymbol { Q _ { u } }$ <sup>−</sup> for user, u, based on $T ^ { L D , N V , R D } \mathrm { i }$ is de<sup>fi</sup>ned as

$$
Q _ {u} ^ {-} \left(T ^ {L D, N V, R D}\right) = \left\{x \mid \forall i \in I, t = T ^ {L D, N V, R D} (u, i), t = v ^ {-} \vee t = v \rightarrow x = v ^ {-} \right\}
$$

c. A user rating set, $Q _ { u }$ for user, u, based on $T ^ { L D , N V , R D }$ is de<sup>fi</sup>ned as

$$
Q _ {u} \left(T ^ {L D, N V, R D}\right) = Q _ {u} ^ {+} \left(T ^ {L D, N V, R D}\right) \cup Q _ {u} ^ {-} \left(T ^ {L D, N V, R D}\right)
$$

d. The high, low and combined rating set, $Q ^ { + } , Q ^ { - } , Q ,$ , for all users in U based on $T ^ { L D , N V , R D }$ is de<sup>fi</sup>ned as

$$
Q ^ {+} \left(T ^ {L D, N V, R D}\right) = \cup_ {u \in U} Q _ {u} ^ {+} \left(T ^ {L D, N V, R D}\right),
$$

$$
Q ^ {-} \left(T ^ {L D, N V, R D}\right) = \cup_ {u \in U} Q _ {u} ^ {-} \left(T ^ {L D, N V, R D}\right),
$$

$$
Q \left(T ^ {L D, N V, R D}\right) = \cup_ {u \in U} Q _ {u} \left(T ^ {L D, N V, R D}\right).
$$

Theorem 2. Given a set of user U, a set of item I and a $T ^ { L D , N V , R D }$ , the expected value of a user giving a high rating based on the prior knowledge of $Q ( T ^ { L D , N V , \mathbf { \bar { R } } D } )$ is

$$
\frac {\left| Q ^ {+} \left(T ^ {L D , N V , R D}\right) \right| + 1}{\left| Q ^ {+} \left(T ^ {L D , N V , R D}\right) \right| + \left| Q ^ {-} \left(T ^ {L D , N V , R D}\right) \right| + 2}
$$

Proof. The formula can be derived from formula (3).

If a user u is a normal user in U, the two expected values should be closed to each other. In other words, if the expected values are too far away from each other then the user probably is an outlier.

Example 3. Given $T ^ { 3 , 4 , 5 }$ shown in Table 2, $Q _ { u _ { 1 } } ^ { + } \Big ( T ^ { 3 , 4 , 5 } \Big ) = \{ \nu ^ { + } \}$ $\begin{array} { r l r } { { \bf \Pi } _ { Q } ^ { u _ { 1 } - } \left( T ^ { 3 , 4 , 5 } \right) = } & { { } \mathcal { O } , Q _ { u _ { 1 } } \left( T ^ { 3 , 4 , 5 } \right) = \{ \boldsymbol { v } ^ { + } \} , } & { { Q } _ { u _ { 2 } } ^ { + } \left( T ^ { 3 , 4 , 5 } \right) = { \bf \Pi } ^ { \{ \nu ^ { + } , \nu ^ { + } \} , } Q _ { u _ { 2 } } ^ { - } } \end{array}$ $\left( T ^ { 3 , 4 , 5 } \right) = \{ \pmb { \nu } ^ { - } , , \pmb { \nu } ^ { - } \} , Q _ { u _ { 2 } } \left( T ^ { 3 , 4 , 5 } \right) = \{ \pmb { \nu } ^ { + } , \pmb { \nu } ^ { - } , \pmb { \nu } ^ { - } , \pmb { \nu } ^ { + } \} , Q _ { u _ { 3 } } ^ { + } \left( T ^ { 3 , 4 , 5 } \right) =$ $\begin{array} { r l } { \{ \nu ^ { + } \} , Q _ { u _ { 3 } } ^ { - } \Big ( T ^ { 3 , 4 , 5 } \Big ) = \{ \nu ^ { - } , , \nu ^ { - } \} , Q _ { u _ { 3 } } \Big ( T ^ { 3 , 4 , 5 } \Big ) } & { { } = \{ \nu ^ { + } , \nu ^ { - } , \nu ^ { - } \} } \end{array}$ Q<sub>þu</sub> $\left( T ^ { 3 , 4 , 5 } \right) \ = \ \{ v ^ { + } \} , Q _ { u _ { 4 } } ^ { - } \left( T ^ { 3 , 4 , 5 } \right) \ = \ \mathcal { O } , Q _ { u _ { 4 } } \left( T ^ { 3 , 4 , 5 } \right) \ = \ \{ v ^ { + } \} . Q ^ { + } \left( T ^ { 3 , 4 , 5 } \right) \ =$ $\{ v ^ { + } , v ^ { + } , v ^ { + } , v ^ { + } , v ^ { + } , v ^ { + } \} , \ Q ^ { - } ( T ^ { 3 , 4 , 5 } ) = \{ v ^ { - } , v ^ { - } , v ^ { - } , v ^ { - } \} \ , \ Q ( T ^ { 3 , 4 , 5 } ) = \{ v ^ { + } , v ^ { + } , v ^ { - } , v ^ { - } \}$ $\nu ^ { - } , \nu ^ { + } , \nu ^ { + } , \nu ^ { - } , \nu ^ { - } , \nu ^ { + } )$

Property II. According to [36], given the PDF, f, of a Beta distribution, p, and a quantile, $q _ { s } ,$ there exist $b _ { r } { } ^ { u p p e r }$ and $b _ { r } ^ { l o w e r }$ , bounds for rated scores such that:

$$
\begin{array}{l} \mathbf {a}. q _ {\mathcal {S}} = \int_ {0} ^ {b _ {r} ^ {l o w e r}} f (p) \\ \mathbf {b}. q _ {\mathcal {S}} = \int_ {b _ {r}} ^ {1} u p p e r f (p) \end{array}
$$

With the property, given $q _ { s } ,$ the boundary values, $b _ { r } ^ { l o w e r }$ and $b _ { r } ^ { { \boldsymbol { u p p e r } } }$ <sup>S</sup>, can be calculated for each rater's Beta probability distribution. As a result, if the expected value based on the entire population falls outside the bounds of a rater, then the rater is judged as abnormal. In Property I, the screening method examines only one quantile because attackers tend to rate few <sup>fi</sup>ller items while in Property II, two quantiles are examined since attackers may give too many or too few high (low) scores.

## 3.5. The Algorithm of β

In order to protect recommender systems against attacks, we adopt a three-phase approach to <sup>fi</sup>lter out attacker pro<sup>fi</sup>les. In the <sup>fi</sup>rst phase, raters rating an extremely low number of items are marked as possible attackers. Raters giving extreme scores when providing positive feedback and negative feedback is also identi<sup>fi</sup>ed as possible attackers in phase two, and three, respectively. A user deemed as possible attackers if he/she is labeled as an attacker in at least two phases. In the <sup>fi</sup>rst phase, the quantile for <sup>fi</sup>ller size, $q _ { \mathcal { F } } ,$ , is <sup>F</sup>given as parameter, whereas, in the last two phases, the quantile for rated scores, $q _ { s } ,$ , is provided as parameter.

<sup>S</sup>β is composed by one main program and two procedures. The procedure utilized in the <sup>fi</sup>rst phase is named as rating\_ extremely\_few\_items, which besides taking $q _ { \mathcal { F } }$ as parameters, also <sup>F</sup>taking U,I,R and returns the raters who score extremely few items when compared to other raters. The pseudo code of the procedure is shown in Fig. 1. The other procedure, rating\_extreme\_scores, is used in both phases two and three. The difference is that the transformed matrix is fed into the procedure. Transformed matrixes of positive and negative ratings are provided to the procedure in phases two and three, respectively. The code of rating\_extreme\_ scores is listed in Fig. 2. The positive and negative transformed matrixes are computed in the main algorithm, in which, neutral ratings are included in both matrixes. Readers can <sup>fi</sup>nd that the score partitioning method can correctly identify middle values given the scoring system utilizing odd number of scales. Fig. 3 shows the main algorithm of $\beta \mathcal { P }$

## 4. Evaluation of βP

## 4.1. Simulation dataset

To measure the performance of the proposed algorithm β , the <sup>P</sup>MovieLens dataset, published by GroupLens Research Lab is utilized [1]. This dataset consists of 100,000 ratings on 1682 movies by 943 raters and each rater had to rate at least 20 movies. All ratings are in the form of integral values between minimum value 1 and maximum value 5. The minimum score means the rater distastes the movie, while the maximum score means the rater enjoyed the movie. According to the information derived from MovieLens website, the sparse ratio of the rating data approximates to 93.7% and the overall mean rating of all users is nearly 3.53. Besides, the Average Number of Items Rated (ANIR) by each user is approximately 7% [1].

<table><tr><td>Procedure:</td><td>rating_extremely_few_items</td></tr><tr><td rowspan="2">Input:</td><td> $U,I,{R}_{U \times I}$  //  $U$ , a set of users,  $I$ , a set of items,  ${R}_{U \times I}$ , a user-item matrix</td></tr><tr><td> ${q}_{F}$  //  ${q}_{F}$  a quantile used in the first phase</td></tr><tr><td>Output:</td><td>Possible_attackers //users who rated extremely few number of items</td></tr><tr><td></td><td>compute the expected value,  $E\left( pr\right)$  ,of the Beta distribution with the prior distribution of  $S^{ + }\left( R\right) \cup S^{-}\left( R\right)$ </td></tr><tr><td></td><td>PossibleAttackers  $= \varnothing$ </td></tr><tr><td></td><td>For each user  $u \in U$  do</td></tr><tr><td></td><td>With quantile  ${q}_{F}$  ,compute the corresponding bound of numbers of rated items,  ${b}_{n}\left( u\right)$  ,of the distribution of  ${S}_{u}{}^{ + }\left( R\right) \cup {S}_{u}{}^{-}\left( R\right)$ </td></tr><tr><td></td><td>IF  $E\left( pr\right) >{b}_{n}\left( u\right)$  Then</td></tr><tr><td></td><td>PossibleAttackers  $\mathrm{U} = \{ u\}$ </td></tr><tr><td></td><td>Return PossibleAttackers</td></tr></table>

Fig. 1. Identifying raters scoring extremely low number of items.

## 4.2. Types of attacks

The shilling attacker's intent is to pour bias into the recommender systems by introducing a number of rating pro<sup>fi</sup>les to affect recommendations of attacked items. The affect is increasing the popularity of the attacked items in push attacks and reducing the popularity in nuke attacks. The experiments will show the resilience of $\beta \mathcal { P }$ under <sup>P</sup>various shilling attacks. When a number of attack pro<sup>fi</sup>les with various attack size and <sup>fi</sup>ller size are inserted into the original MovieLens a dataset will be generated. Furthermore, we introduce a new type of attack pro<sup>fi</sup>les, which attack more than one item in the attack-item partition. In prior work [22,28], attack-item partition contained only one item.

Prior work [22,28] showed that an attack can be very effective if items in <sup>fi</sup>ller-item partition are rated with average rating of the items. Besides, the research also showed the most effective attacks as having zero items in the selected-item partition. As a result, such a scheme will be utilized to generate attack pro<sup>fi</sup>les.

The experiments are composed in three steps. In the <sup>fi</sup>rst step, the experiment dataset is used to <sup>fi</sup>nd appropriate quantile of $q _ { \mathcal { F } }$ and $q _ { s } .$ <sup>F S</sup>The details are stated in Subsection 4.3. In the second step, shilling attacks with various <sup>fi</sup>ller sizes and attack sizes are performed. The results are shown in Figs. 5–8. The details are shown in Subsection 4.4. In the <sup>fi</sup>nal step, we <sup>fi</sup>nd the performance contrast of $: \beta \mathcal { P }$ and a PCA-based <sup>P</sup>method. The results show that β consistently outperforms PCA-based <sup>P</sup>methods under various attack and <sup>fi</sup>ller sizes. The details are shown in Figs. 9–10 in the Subsection 4.5.

## 4.3. Adjusting quantiles

To decide suitable quantiles of $q _ { \mathcal { F } }$ and $q _ { s } ,$ the research examines <sup>F S</sup>various combinations of the two values to <sup>fi</sup>nd a good balance that

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure rating_extreme_scores   
Input: $U,T$ // $U$ ,a set of users, T.transformed matrix   
$q_{\delta}$ // $q_{\delta}$ two quantile used in the second phase and the third phase   
Output: PossibleAttackers //a set of users given extreme ratings   
compute the expected value, $E(p)$ ,of the Beta distribution with the prior distribution of $Q(T)$   
PossibleAttackers $\cup = \emptyset$   
For each user $u\in U$ do With quintile $q_{\delta}$ ,compute $b_{r}(u)^{upper}$ and $b_{r}(u)^{lower}$ of the binary Beta distribution with $Q_u(T)$ as the prior distribution IF $b_{r}(u)^{upper} &lt; E(p)$ OR $E(p) &lt; b_r(u)^{lower}$ Then PossibleAttacker $\cup = \{u\}$   
Return PossibleAttackers
</div>

Fig. 2. Identifying raters given extreme scores.

$$
\beta \mathcal {P}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm: p5

Input: U, I, $R_{U \times I}$ // U, a set of users, I, a set of Items, $R_{U \times I}$, a user-item matrix
$q_{\overline{F}}$ // $q_{\overline{F}}$ a quantile used in the first phase
$q_{\delta}$ // $q_{\delta}$ a quantile used in the second and third phase
max, min // the highest and lowest scores in the recommendation scale system
Output: U - A // a set of authentic raters

//Calculate the middle values used in phase two and three
$\delta = (min + max)/2 \quad \omega = (\delta + max)/2 \quad \lambda = (min + \delta)/2$ $PA_1 = rating\_extremely\_few\_items(U,I,R_{U \times I},q_{\overline{F}})$ $PA_2 = rating\_extreme\_scores(U,T^{\delta,\lambda,max},q_{\delta})$ $PA_3 = rating\_extreme\_scores(U,T^{min,\omega,\delta},q_{\delta})$
A = 0

For each user u ∈ U do
    If u ∈ $(PA_1 \cap PA_2) \cup (PA_2 \cap PA_3) \cup (PA_1 \cap PA_3)$ then
    A ∪ = {u}

Return U - A
</div>

Fig. 3. Filtering out attackers.

can derive both high detection and low false alarm rates. From Fig. 4, readers can <sup>fi</sup>nd that the combination of $q _ { \mathcal { F } } = 8 E { - 1 4 }$ and $q _ { S } =$ <sup>F S</sup>0:00142 gives the most balanced result under an attack size of 5%. Therefore, the two quantiles are selected for the rest of the experiment. The reason for experimenting with the attack size is because in most known published work [5,13,22,25–27,30,43], attack sizes ranged from 1 to 10%. A middle size is picked in the hope that the value can represent most cases.

## 4.4. The protection provided by β under various attacks

The research conducts four types of attacks in the experiment. They attack single targets with the push method, attack a single target with the nuke method, attack multiple-targets with the push method and attack multiple-targets with the nuke method.

Since the original dataset has 1682 movies, every percentage of <sup>fi</sup>ller size increases the number of items rated by 16 in the attacking pro<sup>fi</sup>les. In the <sup>fi</sup>ller partition, items are chosen randomly with each one being <sup>fi</sup>lled with the item's average rating. At the same time, the dataset contains ratings from 943 users, every percentage of attack size increases 9 users to attacking pro<sup>fi</sup>les. In the experiment, all attacking pro<sup>fi</sup>les attack the same items, as have been done in previous work [22,28].

Fig. 5 shows the detection and false alarm rates of β while facing <sup>P</sup>Single-Target Push attacks. Readers can <sup>fi</sup>nd that the detection rates increase very fast along with the increase of <sup>fi</sup>ller size. The detection rates reach 90% when <sup>fi</sup>ller size reaches 6%. Except for the attacks with attack sizes of 7% and 9%, the detection rates even reach 100% at the <sup>fi</sup>ller size of 6%. The false alarm rates, on the other hand, consistently stay around 13% and 14%, regardless of <sup>fi</sup>ller size and attack size.

![](/api/attachments/SM3UG42T/fulltext/images/7340c0573ca861d833326780d7699e44c719a70ef3ae3c99a3a400fcd86dcbbb.jpg)  
Fig. 4. The detection and false alarm rates with various quantiles and <sup>fi</sup>ller sizes under an attack size of 5%.

![](/api/attachments/SM3UG42T/fulltext/images/d1d0fbc4bbf8c1b2cebd76a6ded517d5a4d5bec7b339034b68ce94715691a61b.jpg)  
Fig. 5. Performance under Single-Target Push attacks.

Fig. 6 shows the detection and false alarm rates of β while facing <sup>P</sup>Single-Target Nuke attacks. Readers can <sup>fi</sup>nd that the detection rates also increase very fast along with the increase of <sup>fi</sup>ller size. The detection rates reach 100% at the <sup>fi</sup>ller size of 6% for all attack sizes. The false alarm rates, again, consistently stay at around 13%.

Figs. 5 and 6 show that the detection and false alarm rates are very stable when attack pro<sup>fi</sup>les are equipped with 7% of <sup>fi</sup>ller items which, is also the ANIR value of the dataset and is frequently adapted as the <sup>fi</sup>ller size of attack pro<sup>fi</sup>les in other research. Therefore, in multiple-target attacks all attacks are assumed to have 7% of the <sup>fi</sup>ller size.

Fig. 7 shows the performance of β under Multiple-Target Push attacks. When attack size is around 1%, the detection rate remains around 100%, regardless of number of targets. For other attacking sizes, increasing the number of targets attacked in one pro<sup>fi</sup>le in general decreases the detection rate. The false alarm rates are again very stable, regardless of the attack size, and number of targets.

Fig. 8 shows the performance of β under Multiple-Target Nuke at-<sup>P</sup>tacks. The results show that the detection rate of nuke attacks constantly stays around 100%, regardless of the attack size and number of targets. False alarm rates still consistently stay around 13% and 14%.

![](/api/attachments/SM3UG42T/fulltext/images/f5457fd2f5da4dd42957966ac8735be7919e18074ce880f2dbe79c578d3e8854.jpg)  
Fig. 6. Performance under Single-Target Nuke attacks.

![](/api/attachments/SM3UG42T/fulltext/images/78ea0c34300feef2768ca3e2d6ad71dce8ae8aed34b09cd2de6e627cd24f8118.jpg)  
Fig. 7. Performance under Multiple-Target Push attacks.

## 4.5. Compare and contrast to the performance of PCA methods

PCA methods are also used to identify attackers in recommender systems. As a contrast, PCA methods are used to identify attackers from pro<sup>fi</sup>les that have been used in this experiment. The main limitation of the PCA methods is that PCA cannot take any missing value. In this study, a missing value in the user–item matrix is interpreted as the corresponding user having not watched or having no impression of watching the corresponding movie. Therefore, a missing value is viewed as no opinion, which is neither favorable nor unfavorable of the corresponding movie. As a result, missing value is replaced with “3” since the opinion is expressed in 5 level Likert Scale in MovieLens.

Fig. 9 shows the performance under Single-Target Push attacks. The detection rates eventually fall to zero when <sup>fi</sup>ller size is at 1 and 5% and the detection rates decrease dramatically with the increase of <sup>fi</sup>ller size. Fig. 10 shows the performance under Single-Target Nuke attacks. Readers can <sup>fi</sup>nd that the detection rates of attack size 1% and 5% once again fall into zero. The detection rates again decrease signi<sup>fi</sup>cantly with the increase of <sup>fi</sup>ller size. Since the number of attackers has to be given in PCA methods, there is no fair way to com pare and contrast the false alarm rates of both approaches.

![](/api/attachments/SM3UG42T/fulltext/images/e7ec8e5e2dcfc9c90b4da7e4a24b46b184793e362fdd8f390dc571561c4c0326.jpg)  
Fig. 8. Performance under Multiple-Target Nuke attacks

![](/api/attachments/SM3UG42T/fulltext/images/fda0eb4cca9157c22af1686847dbe45a1568140650cac04468e59813074802a4.jpg)  
Fig. 9. PCA Methods under Single-Target Push attacks.

## 5. Conclusion

With the open nature of collaborative <sup>fi</sup>ltering recommender systems, they suffer signi<sup>fi</sup>cant vulnerabilities of being attacked from malicious raters, who inject pro<sup>fi</sup>les consisting of biased ratings. In order to <sup>fi</sup>ght back against the attacks, in this research, a novel approach β is proposed to detect and exclude attackers.

<sup>P</sup>In recent years, several attack detection algorithms have been proposed to handle the issue [5–9,31,32,39]. Unfortunately, their applications are restricted by various constraints. PCA-based methods that even have good performance on paper, suffer from missing values that plague most user–item matrixes. Classi<sup>fi</sup>cation-based methods require balanced numbers of attack and normal pro<sup>fi</sup>les to train the classi<sup>fi</sup>ers. However, attack pro<sup>fi</sup>les that can even be successfully identi<sup>fi</sup>ed, are scarce compared to normal pro<sup>fi</sup>les. The statistical detector based on the Neyman–Pearson theory assumes that the rating probability distribution for each item is known in advance.

The algorithm of β detects attackers without all the abovementioned constraints. β does not need attacking pro<sup>fi</sup>les as the <sup>P</sup>training data, is immune to missing values, and does not need prior knowledge of rating distribution on each item.

β derives stable result under various attacks. The detection rates under single-target attacks with <sup>fi</sup>ller and attack size larger than 6% are better than 90%. The same detection rate is maintained when the target size is less than 5 in multi-target attacks. The false alarm rate however, is also very stable in all cases.

![](/api/attachments/SM3UG42T/fulltext/images/11cffc0168874829dcefb87acdac4407ffc028c4739bccc3ba3e8e9020416a88.jpg)  
Fig. 10. PCA Methods under Single-Target Nuke attacks.

One of the limitations of the proposed method comes directly from the de<sup>fi</sup>nition of Beta distribution. The method assumes that a single prior distribution can be used to describe the possible values being observed in each cell of the user–item matrix for normal users. If the normal users have signi<sup>fi</sup>cantly different grading behavior, then the method will yield a low detection rate and a high false alarm rate. Another limitation comes from the attack size. Large attack size can distort prior distribution and render the method with poor result.

β serves as a pioneer in a new research direction of attacker de-<sup>P</sup>tection. Yet, it is by no means complete. The basic concept of collaborative <sup>fi</sup>ltering recommender systems is that the users are recommended items that people with similar tastes and preferences like. The ratings given to user–item matrix are not updated frequently with the assumption that users' preferences are static, namely users' purchasing interest and preference are always the same. Unfortunately, this assumption may not always be valid. For inexpensive and low involvement items, the product awareness, users' purchasing interests and preferences can vary with environment changes, such as new promotions, new pricing strategy and the introduction of new items. Hence, future study can incorporate the property of the temporal dynamics into the attacks detector to provide timely detection of attacks.

## Acknowledgments

The authors would like to express the gratitude to referees for their suggestions that helped to substantially improve the manuscript. This research was supported in part by the National Science Council of the Taiwan (Republic of China) under the Grant NSC 99-2410-H-008-032 and by the Ministry of Education (MOE) Program for Aiming for the Top Universities under Grant No. 101G904-4.

## References

[1] GroupLens Lab, MovieLens Data Set, http://www.grouplens.org/node/12 2010

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[3] R. Barandela, J.S. Sánchez, V. García, E. Rangel, Strategies for learning in class imbalance problems, Pattern Recognition 36 (3) (2003) 849–851.

[4] R. Bhaumik, C. Williams, B. Mobasher, R. Burke, Securing collaborative <sup>fi</sup>ltering against malicious attacks through anomaly detection, ITWP'06 Proceedings of the 4th Workshop on Intelligent Techniques for Web Personalization, at AAAI'06, Boston, 2006.

[5] B. Burke, B. Mobasher, C. Williams, R. Bhaumik, Classi<sup>fi</sup>cation features for attack detection in collaborative recommender systems, KDD '06 Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM Press, 2006.

[6] R. Burke, B. Mobasher, C. Williams, R. Bhaumik, Detecting pro<sup>fi</sup>le injection attacks in collaborative recommender systems, CEC-EEE '06 Proceedings of the 8th IEEE International Conference on E-Commerce Technology and the 3rd IEEE International Conference on Enterprise Computing, E-Commerce, and E-Services, 2006.

[7] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[8] P.A. Chirita, W. Nejdl, C. Zam<sup>fi</sup>r, Preventing shilling attacks in online recommender systems, WIDM '05 Proceedings of the 7th Annual ACM International Workshop on Web Information and Data Management, ACM Press, 2005.

[9] M. Deshpande, G. Karypis, Item-based top-N recommendation algorithms, ACM Transactions on Information Systems 22 (1) (2004) 143–177.

[10] N. Hu, I. Bose, Y. Gao, L. Liu, Manipulation in digital word-of-mouth: a reality check for book reviews, Decision Support Systems 53 (3) (2011) 627–635.

[11] N. Hu, L. Liu, V. Sambamurthy, Fraud detection in online consumer reviews, Decision Support Systems 50 (3) (2011) 614–626.

[12] N. Hu, I. Bose, N.S. Koh, L. Liu, Manipulation of online reviews: an analysis of ratings, readability, and sentiments, Decision Support Systems 52 (3) (2012) 674–684.

[13] N.J. Hurley, Z. Cheng, M. Zhang, Statistical attack detection, RecSys '09 Proceedings of the third ACM conference on Recommender systems, ACM Press, 2009.

[14] R. Jin, J.Y. Chai, L. Si, An automatic weighting scheme for collaborative <sup>fi</sup>ltering, SIGIR '04 Proceedings of the 27th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval 2004

[15] A. Jøsang, R. Ismail, The Beta reputation system, Proceedings of the 15th Bled Conference on Electronic Commerce Conference 2002

[16] A. Jøsang, S. Hird, E. Faccer, Simulating the effect of reputation systems on e-markets, Proceedings of the First International Conference on Trust Management, 2003.

[17] A. Jøsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[18] F. Karakaya, N.G. Barnes, Impact of online reviews of customer care experience on brand or company selection, Journal of Consumer Marketing 27 (5) (2010) 447–457.

[19] H.N. Kim, A.T. Ji, H.J. Kim, G.S. Jo, Error-based collaborative <sup>fi</sup>ltering algorithm for top-N recommendation, Lecture Notes in Computer Science 4505 (2007) 594–605.

[20] J. Konstan, B. Miller, D. Maltz, J. Herlocker, L. Gordon, J. Riedl, GroupLens: applying collaborative <sup>fi</sup>ltering to usenet news, Communications of the ACM 40 (3) (1997) 77–87.

[21] S. Kotsiantis, D. Kanellopoulos, P. Pintelas, Handling Imbalanced Datasets: a Review, GESTS International Transactions on Computer Science and Engineering, 2006.

[22] S.K. Lam, J. Riedl, Shilling recommender systems for fun and pro<sup>fi</sup>t, WWW '04 Proceedings of the 13th International Conference on World Wide Web, ACM press, 2004.

[23] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative <sup>fi</sup>ltering, IEEE Internet Computing 7 (1) (2003) 76–80.

[24] P. Massa, B. Bhattacharjee, Using trust in recommender systems: an experimental analysis, Lecture Notes in Computer Science 2995 (2004) 221–235.

[25] B. Mehta, Unsupervised shilling detection for collaborative <sup>fi</sup>ltering, AAAI '07 Proceedings of the 22nd National Conference on Arti<sup>fi</sup>cial Intelligence, 2007.

[26] B. Mehta, W. Nejdl, Unsupervised strategies for shilling detection and robust collaborative <sup>fi</sup>ltering, User Modeling and User-Adapted Interaction 19 (1–2) (2009) 65–97.

[27] B. Mehta, T. Hofmann, P. Fankhauser, Lies and propaganda: detecting spam users in collaborative <sup>fi</sup>ltering, IUI '07 Proceedings of the 12th International Conference on Intelligent User Interfaces, 2007.

[28] B. Mobasher, R. Burke, B. Bhaumil, C. Williams, Towards trustworthy recommender systems: an analysis of attack models and algorithm robustness, ACM Transactions on Internet Technology 7 (4) (2007) 23–38.

[29] S. Olsen, Amazon blushes over sex link gaffe, http://news.cnet.com/2100-1023- 976435.html 2002

[30] M.P. O'Mahony, N.J. Hurley, G.C.M. Silvestre, Promoting recommendations: an attack on collaborative <sup>fi</sup>ltering, Lecture Notes in Computer Science 2453 (2002) 494–503.

[31] M. O'Mahony, N.J. Hurley, N. Kushmerick, G.C.M. Silvestre, Collaborative recommendation: a robustness analysis, ACM Transactions on Internet Technology 4 (4) (2004) 344–377.

[32] M. Papagelis, D. Plexousakis, T. Kutsuras, Alleviating the sparsity problem collaborative <sup>fi</sup>ltering using trust inferences, Lecture Notes in Computer Science 3477 (2005) 224–239.

[33] S. Piramuthu, G. Kapoor, W. Zhou, S. Mauw, Input online review data and related bias in recommender systems, Decision Support Systems 53 (3) (2012) 418–424.

[34] P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative <sup>fi</sup>ltering of netnews, CSCW ‘94 Proceedings of Computer Supported Cooperative Work, 1994

[35] Joe Roth, BBC News, Sony admits using fake reviewer, http://news.bbc.co.uk/1/hi/ entertainment/film/1368666.stm 2001.

[36] J. Rutledge, B. Warner, Using the Beta distribution on con<sup>fi</sup>dence intervals for proportions, Proceedings of the Quality and Productivity Research Conference, 1999.

[37] J.J. Sandvig, B. Mobasher, R. Burke, Robustness of collaborative recommendation based on association rule mining, RecSys '07 Proceedings of the 2007 ACM Conference on Recommender Systems, ACM press, 2007.

[38] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative <sup>fi</sup>ltering recommendation algorithms, Proceedings of the 10th International World Wide Web Conference, ACM Press, 2001.

[39] P.J. Sher, S.H. Lee, Consumer skepticism and online reviews: an elaboration likelihood model perspective, Social Behavior and Personality 37 (1) (2009) 137–144.

[40] C.T. Su, L.S. Chen, Y. Yih, Knowledge acquisition through information granulation for imbalanced data, Expert Systems with Applications 31 (3) (2006) 531–541.

[41] P.N. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Addison Wesley, 2006.

[42] A. Whitby, A. Jøsang, J. Indulska, Filtering out unfair ratings in bayesian reputation systems, The Icfain Journal of Management Research 4 (2) (2005) 48–64.

[43] C. Williams, B. Mobasher, R. Burke, R. Bhaumik, J. Sandvig, Detection of obfuscated attacks in collaborative recommender systems, ECAI'06 Proceedings of the 17th European Conference on Artificial Intelligence, 2006

[44] L. Yu, L. Liu, X.F. Li, A hybrid collaborative <sup>fi</sup>ltering method for multiple-interests and multiple-content recommendation in E-commerce, Expert Systems with Applications 28 (1) (2005) 67–77.

[45] Z. Zhang, Q. Ye, R. Law, Y. Li, The impact of e-word-of-mouth on the online popularity of restaurants: a comparison of consumer reviews and editor reviews, International Journal of Hospitality Management 29 (4) (2010) 694–700.

Chen-Yao Chung is a Ph.D. candidate at the department of business administration at National Central University in Taiwan, and majors in ERP and Business Intelligence. He was a computer system engineer at Industrial Technology Research Institute (ITRI) in Taiwan, He was a certified instructor of ERP and has trained innumerable certified engineers at Chinese ERP Society. His current research interests include recommenda tions, ERP, business intelligence and cloud computing.

Dr. Ping-Yu Hsu graduated from the CSIE department of National Taiwan University in 1987, got his Masters degree from the Computer Science Department of New York University in 1991, and Ph.D. degree from the Computer Science Department of UCLA in 1995. He is a professor in the Business Administration department of National Central University in Taiwan and the secretary-in-chief of the Chinese ERP association. He has been actively participating in the application of ERP in Taiwan. His research interest focuses in the business data related applications, including Data mining, Business Intelligence, Data Warehousing, and Enterprise System implementation. He has published more than 100 Journal and conference articles. His papers have been published in IEEE Transactions, Information Systems, Information Sciences, and various other journals.

Shih-Hsiang Huang is a Ph.D. student at the National Central University of Taiwan. His research interests include the development and applications of data mining techniques to a variety of business problems.
