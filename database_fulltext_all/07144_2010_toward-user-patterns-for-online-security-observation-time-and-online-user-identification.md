---
otero_id: 7144
otero_key: "98K8EEHP"
title: "Toward user patterns for online security: Observation time and online user identification"
authors: "Yinghui (Catherine) Yang; Balaji Padmanabhan"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.11.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Toward user patterns for online security: Observation time and online user identi<sup>fi</sup>cation

Yinghui (Catherine) Yang <sup>a,</sup>⁎<sup>,1</sup>, Balaji Padmanabhan

<sup>a</sup> Graduate School of Management, University of California, Davis, AOB IV, One Shields Ave., Davis, CA 95616, USA

<sup>b</sup> College of Business, University of South Florida, 4202 East Fowler Ave., Tampa, FL 33620, USA

## a r t i c l e i n f o

Article history: Received 24 December 2008 Received in revised form 21 October 2009 Accepted 6 November 2009 Available online 14 November 2009

Keywords: Web usage mining Behavioral signatures Online security User identi<sup>fi</sup>cation Biometrics Electronic commerce

## a b s t r a c t

Research in biometrics suggests that the time period a speci<sup>fi</sup>c trait is monitored over (i.e. observing speech or handwriting “long enough”) is useful for identi<sup>fi</sup>cation. Focusing on this aspect, this paper presents a data mining analysis of the effect of observation time period on user identi<sup>fi</sup>cation based on online user behavior. We show that online identi<sup>fi</sup>cation accuracies improve with pooling user data over sessions and present results that quantify the number of sessions needed to identify users at desired accuracy thresholds. We discuss potential applications of this for veri<sup>fi</sup>cation of online user identity, particularly as part of multi-factor authentication methods.

© 2009 Elsevier B.V. All rights reserved

## 1. Motivation

Humans are believed to have many unique characteristics such as <sup>fi</sup>ngerprints and handwriting styles. We use the term “signatures” here to refer to distinguishing characteristics that are behavioral (e.g. writing styles), as opposed to characteristics that are physiological (e.g. <sup>fi</sup>ngerprints). The applications of methods for unique identi<sup>fi</sup>cation are signi<sup>fi</sup>cant, ranging from forensics and law enforcement to novel biometrics-based access to personal information that protects user privacy and mitigates fraud. The development and perfection of such unique distinguishing characteristics continues to be an important area of research.

Given the vast impact technology has in everyday life, there has naturally been interest in recent years on whether there might be unique signatures in technology mediated applications. Ref. [24] shows that users have distinct ways in which they use computer keyboards and that users have unique keystroke dynamics. Ref. [7] extends this work to the use of mouse movements in addition to keystroke dynamics and note that the combination can often be used to uniquely identify humans. Ref. [20] shows that authors have unique writing styles that enable identifying them from text. In a similar vein, Ref. [19] shows that users have unique writing patterns when they author content for online message boards. A recent article [10] published in Nature that studied user mobility patterns with cell phone GPS data showed that, perhaps not surprisingly, most users tend to have quite predictable daily mobility patterns.

In the same spirit, are there unique “clickprints” based on how users browse, or consume content online? This is an open question, the answer to which can have signi<sup>fi</sup>cant implications for applications such as online fraud detection and product recommendations.

If individuals can be identi<sup>fi</sup>ed based on online patterns, even to a reasonable extent, then there are important server-side and clientside applications. As an example of a server-side application, if a <sup>fi</sup>rm can identify a user who is not explicitly signed in there may be opportunities for targeted recommendations. Of course in this case the <sup>fi</sup>rm will have to consider online privacy needs of their customers and the <sup>fi</sup>rm's own privacy policy before any such action.

On the client-side there may be important practical applications of such technology that may mitigate online fraud and identity theft, issues that are known to be important to consumers [15]. For instance, users may opt-in to download client-side software from a trusted third party<sup>2</sup> that will track client-side activities to build user identi<sup>fi</sup>cation models. Such models may be used to provide behavioral authentication services on behalf of the user. For instance, when this user makes a large online brokerage transaction, the <sup>fi</sup>nancial institution may, in real time, query the client-side software for a “user score”. If the returned score suggests that the user is unlikely to be who they claim to be, the <sup>fi</sup>rm may then proceed to seek additional information. Such an application may offer users real bene<sup>fi</sup>ts such as fraud and online identity theft mitigation, while being sensitive to privacy concerns due to its opt-in nature and limited data (a user score) that it reveals, with consent, to third parties. In this research we do take such a “user-centric” perspective — the data we analyze is user-centric browsing data and the results in this research are relevant to client-side applications such as the one noted here.

Related to the client-side security application, a key US federal agency, the Federal Financial Institutions Examination Council (FFIEC) recently issued guidance entitled Authentication in an Internet Banking Environment<sup>3</sup>. This document notes that: “existing authentication methodologies involve three basic “factors”:

• something the user knows (e.g., password, PIN);

• something the user has (e.g., ATM card, smart card); and

• something the user is (e.g., biometric characteristic such as a <sup>fi</sup>ngerprint).”

The guidance notes that fraud and identity theft are often the result of exploiting single factor authentication systems and suggests that multi-factor authentication methods are stronger fraud deterrents. Indeed deterrence as a mechanism to improve IT security has been stressed in the IS literature. It is known that just the use of security software by <sup>fi</sup>rms can deter computer abuse from a network intrusion perspective [28]. While the accuracy of such systems matters, it is often the deterrence that comes from accuracy that actually contributes to better security [4]. The hypothetical client-side application discussed previously, if designed appropriately, may provide one such additional factor in a multi-factor approach to fraud deterrence. Designing such a system will require developing accurate user identi<sup>fi</sup>cation models. This in turn requires a deeper understanding of the factors that can result in better or worse identi<sup>fi</sup>cation accuracies. Our research in this paper focuses on one such factor as we note below in Section 2.

It should also be noted that there are efforts on the part of Internet service providers to improve security for all users. In this context recent research [35] has proposed certi<sup>fi</sup>cation mechanisms as a manner in which incentive alignment can be achieved. Indeed such efforts are complementary to better client-side approaches for security. Further, user and computer security within organizational settings has naturally attracted speci<sup>fi</sup>c attention in research. Ref. [12] takes such a broader view of security in organizations and note that organizations should study employee “security behavior” in detail and discusses organizational mechanisms for this purpose. Related is the work of Ref. [11], where a genetic algorithm is used to determine an organization's optimal security pro<sup>fi</sup>le to balance cost as well as risk.

## 2. Focus of this research

There are online user behavior theories, most notably the research in Web usage mining [1,26,32] which suggest that user behavior is not random and there is often a purpose that translates into revealed online behavior. However they do not provide speci<sup>fi</sup>c answers on how unique the revealed behavior is. On the other hand there has been substantial work in biometrics over the last few decades that has speci<sup>fi</sup>cally studied user identi<sup>fi</sup>cation from various characteristics such as <sup>fi</sup>ngerprints, handwriting or speech. Much of the biometrics work focusing on user identi<sup>fi</sup>cation has been experimental, and has collectively highlighted two intuitive aspects:

1. The quality of user data impacts identi<sup>fi</sup>cation accuracy. In the handwriting and <sup>fi</sup>ngerprinting literature, quality refers to image quality as measured by the resolution or number of pixels. There is evidence in this literature [16] that higher quality improves identi<sup>fi</sup>cation accuracies. For user identi<sup>fi</sup>cation from online behavior, quality of data can be measured by the features created from behavior. A large number of features can be generated from every click or page viewed online. The associated intuitive hypothesis here will be that better features result in better user identi<sup>fi</sup>cation models.

2. The quantity of user data impacts identi<sup>fi</sup>cation accuracy. In the speech recognition and handwriting literatures, quantity refers to how long this behavior is observed or monitored. The results show that if speech and handwriting can be observed “long enough”, fairly accurate models can be built [14]. For user identi<sup>fi</sup>cation from online behavior, quantity is a measure of how much user data is observed. Intuitively we expect this result to hold as well. For instance from just one session of browsing data a user may not look suf<sup>fi</sup>ciently different from others, but over time there might be enough data to highlight differences.

In this paper we focus on studying the quantity aspect in online user identi<sup>fi</sup>cation. By doing so we hope this research can provide light on how much user data is needed before accurate user identi<sup>fi</sup>cation models can be obtained.<sup>4</sup> Insights into this issue are signi<sup>fi</sup>cant for client-side applications such as the one noted above. To our knowledge this is the <sup>fi</sup>rst research paper that addresses this question. Further the methodology developed here can be used to study this aspect for any given quality of features used for identi<sup>fi</sup>cation.

For convenience we will use the term “aggregation” to describe the process of observing and collecting data over longer time periods. While time is a useful notion to intuitively measure “how much” data is needed, we will focus our analysis in this research to aggregation over multiple Web sessions as opposed to time periods. We note that the analysis methodology presented here can be directly applied to time if desired. However a user session is a commonly used unit of analysis when describing online behavior, and “long enough” in this context refers to observing a user over an adequate number of sessions.

In this paper we answer the following questions:

(Q1a). Does aggregation result in improved user identification based on online behavior?

While prior research in biometrics has shown the value of aggregation for other problems, to our knowledge this work is the <sup>fi</sup>rst to present such analysis for online user identi<sup>fi</sup>cation.

Rather than treating this as a single hypothesis to test, we break this down into a series of tests as described below. Intuitively we expect that as the number of users in the population grows, user identi<sup>fi</sup>cation will be more dif<sup>fi</sup>cult. Hence the signi<sup>fi</sup>cance of aggregation can be expected to depend on the number of users considered in a dataset. Further we restrict our consideration to a range of different aggregation levels and test if accuracies at a speci<sup>fi</sup>c level of aggregation are lower than the accuracies at the immediate higher level of aggregation. Hence we answer Q1a in a table where the rows correspond to varying number of users (speci<sup>fi</sup>cally M=2, 3, 5, 10, 25, 50 and 100) and the columns represent pairs of adjacent aggregations (2 over 1, 3 over $^ { 2 , \ldots , }$ 10 over 9). Each cell represents a hypothesis that the accuracies corresponding to the higher level of aggregation are greater than the accuracies corresponding to the lower aggregation.

(Q1b). What are the accuracy gains from aggregation for online user identification?

Testing speci<sup>fi</sup>c hypotheses related to Q1a will answer whether aggregation is useful. The empirical analyses needed for this will also provide data to compute speci<sup>fi</sup>c magnitude gains. These gains will provide an understanding of how much the predictive accuracies improve.

Our results show that aggregation is indeed useful and that the value and amount of aggregation depend on problem dif<sup>fi</sup>culty, as measured by the number of users to distinguish among. Speci<sup>fi</sup>cally, the more the number of users the greater the value from pooling data across sessions. This <sup>fi</sup>nding leads us to an important empirical question (Q2) which we study next.

(Q2). What is the minimum aggregation needed to attain a specific threshold accuracy for online user identification?

As noted above as the number of users in the population grows, user identi<sup>fi</sup>cation is more dif<sup>fi</sup>cult, and hence more aggregation is needed to attain a desired accuracy. Hence here we seek to answer how much aggregation is needed to achieve a desired accuracy level for a speci<sup>fi</sup>c number of users. This is an empirical question and we seek here to develop a table where the rows correspond to different number of users, the columns correspond to different accuracy thresholds, and the cells are the aggregation levels needed on average to achieve the desired accuracy threshold.

This is an important empirical contribution since it will provide insight into how much user-centric (client-side) information may be needed before users can be identi<sup>fi</sup>ed based on their online behavior. To our knowledge there has been no prior work that has provided such an analysis.

## 3. Theoretical bases and literature review

Studying the impact of aggregation on online identi<sup>fi</sup>cation accuracies is new and there is no prior research that has addressed this speci<sup>fi</sup>cally. However our research questions here are built on several important ideas that have been well developed in the literature, particularly prior to work in the areas of Web usage mining, methods for biometric identi<sup>fi</sup>cation and behavioral signatures. Collectively they support our research in the following manner:

• The Web usage mining literatures provide ample evidence that suggest that online user behavior is not random and that user patterns do exist.

• Research in biometrics and behavioral signatures suggests that users may have unique behavioral traits in some areas and that aggregation can be important for identi<sup>fi</sup>cation.

However, as noted earlier, the link between aggregation and online user identi<sup>fi</sup>cation has not yet been studied. We discuss the major related results in these areas below.

## 3.1. Web usage mining

An early technique developed in Ref. [2] shows how association rules could be generated from online data to build pro<sup>fi</sup>les. Ref. [1] describes a system for learning pro<sup>fi</sup>les that capture both facts about users as well as behavioral rules learned from transaction data. Instead of just individual user pro<sup>fi</sup>les, there has also been work on learning aggregate pro<sup>fi</sup>les, such as Ref. [23], which builds pro<sup>fi</sup>les that can apply across groups of users who may have similar interests. Rather than learning pro<sup>fi</sup>les from clickstream data, Ref. [9] describes an approach that unobtrusively monitors user activities on pages, such as how much they scroll, to build pro<sup>fi</sup>les that capture user interest in speci<sup>fi</sup>c pages or content. Reviews of work in this area are presented in Ref. [27] and Ref. [17].

The main reason for learning pro<sup>fi</sup>les has been to use these for personalization and product recommendations. However these applications do not require that users have unique pro<sup>fi</sup>les. On the contrary it is recognized that these may be similar since it is possible that many users share the same interests or buy similar products. While the observation that users may be similar in certain respects is intuitive, and has direct marketing applications, it does not preclude the notion that there may be systematic differences as well. Differences are important given potential applications to online fraud, but these have not been studied as extensively.

However this literature does make the key point that users have behavioral signatures (not assumed to be unique) that manifest themselves in clickstream data. Motivated speci<sup>fi</sup>cally by the signature learning problem, Ref. [32] shows how a pattern-based clustering approach can be used to group Web transactions such that individual user sessions could be accurately separated. This approach is based on choosing a representation for user signatures and still used only single sessions (with no aggregation considered) as the unit of analysis to learn patterns.

On a broader note, this literature provides substantial empirical evidence of patterns in online behavior. However the questions that have not been addressed are whether such patterns may sometimes enable user identi<sup>fi</sup>cation and what effect aggregation may have in this process.

Finally, research in information foraging [26] also suggests that individual browsing behavior is not random and may be explained by a combination of rules and information scent-based heuristics. In this paper we focus more on understanding the extent and conditions under which any underlying patterns lend themselves to online user identi<sup>fi</sup>cation than we do on the basis for any non-randomness in information seeking behavior online.

## 3.2. Biometrics and behavioral signatures

Converting physiological characteristics of users into techniques for biometric identi<sup>fi</sup>cation has been an active area of research for several years, and Ref. [22] presents a review of many such approaches. With the widespread use of technology, recently there has been substantial interest in identifying unique behavioral characteristics that can possibly serve as identi<sup>fi</sup>ers. Ref. [24] shows that users have distinct ways in which they use computer keyboards and that users have unique keystroke dynamics. They show that depending on the classi<sup>fi</sup>er used, between 80 and 90% of users can be automatically recognized using features such as the latency between keystrokes and the length of time different keys are pressed. Ref. [7] extends this work to the use of mouse movements in addition to keystroke dynamics and note that the combination can often be used to uniquely identify humans. Ref. [20] shows that authors have unique writing styles that enable identifying them from text. In a similar vein, Ref. [19] studies online message board postings and show that users may have online “writeprints” — unique ways in which they write messages on online bulletin boards. A post on a message board is converted to a large number of features (such as number of sentences and frequency of speci<sup>fi</sup>c characters), and Ref. [19] applies a genetic algorithm based feature selection method to extract a set of subfeatures that are then used to identify users. Experiments involving 10 users in two different message boards suggest that “writeprints” could well exist since the accuracies obtained were between 92 and 99%.

Research has also shown that humans may have distinct patterns even in everyday activities like walking and driving. Ref. [13] shows how driving behavior, such as the extent of braking, often can be used to identify the driver of a vehicle. Ref. [21] shows that users may also have unique gait patterns relating to how they walk when they talk on mobile phones. Such gait patterns are then used to provide an extra layer of security for personal information in mobile devices.

Related to the concept of aggregation, in the <sup>fi</sup>eld of automatic speaker recognition, Ref. [3] states that there is generally a tradeoff between accuracy and the duration of the speech used in the training and testing period. It has also been well accepted in the human speaker identi<sup>fi</sup>cation <sup>fi</sup>eld that the longer the duration of the speech observed, the higher the probability of correct identi<sup>fi</sup>cation [14].

Ref. [6] states that exposure duration seems to affect identi<sup>fi</sup>cation accuracy positively. Ref. [18] shows a signi<sup>fi</sup>cant performance improvement when exposure duration increases. Ref. [33,34] also conclude that longer exposure duration increases the probability of correct identi<sup>fi</sup>cation but they also <sup>fi</sup>nd an increase in the number of false alarms. Ref. [8] states that the performance improvement with longer test sample duration for standard speaker recognition system eventually levels off. It is also generally accepted in the <sup>fi</sup>eld of handwriting identi<sup>fi</sup>cation that the use of several words can provide better information than a single signature [36].

Also related is work on learning user signatures fraud detection. From a database of fraudulent and normal transactions, user signatures may be built from machine learning techniques that can then be used to predict if any transaction is fraudulent. Ref. [5] shows how user call records can be used to learn caller signatures. These signatures can then be tested against a current call to determine if fraud occurred. While this is a different application, building statistical measures across calls and generating feature distributions across multiple Web sessions are similar in spirit and lend further support to our hypothesis relating aggregation and identi<sup>fi</sup>cation accuracies.

## 4. Methodology for Q1a

In this section we describe the methodology used to address Q1a (Does aggregation result in improved user identi<sup>fi</sup>cation based on online behavior?). Computing magnitude gains to answer Q1b can be done directly from this process.

For a given number, M, of users, determining signi<sup>fi</sup>cance of one aggregation level over the immediate next level can be done using the following procedure:

1. Randomly sample M users' user-centric Web sessions.

2. Partition the session-level data into training and testing datasets.

3. Preprocess the training and testing datasets corresponding to different aggregation levels.

4. Corresponding to each aggregation level, build a classi<sup>fi</sup>er and record its holdout accuracy.

5. Repeat the analysis above for a large number of runs.

The output of the process above is a column of accuracy values for each aggregation level. From these columns signi<sup>fi</sup>cance tests across aggregation levels are performed and magnitude gains are recorded.

Below we describe in detail how each of these steps is done.

## 4.1. Sampling

The data provided to us was the anonymized client-side (usercentric) browsing behavior of a random sample of 50,000 users over one year. There are two criteria that we used when selecting the users to sample from this population.

First, each panelist in the sample represents a household that is tracked. For our analyses it is important for the clickstream data to represent a single user's data, as opposed to a household. Hence we restrict our random selection of users to those corresponding to a household size of one in the household demographic <sup>fi</sup>le provided.

Second, we require users with enough browsing activity such that we have enough training and holdout data on which the models can be trained and tested. Fig. 1 shows the histogram of total number of sessions across all users corresponding to a household size of one (the <sup>fi</sup>rst bar corresponds to the number of users with b100 sessions, the second bar indicates the number of users with 100–300 sessions, and so on).

The larger the (minimum) number of sessions per user the greater the training as well as the testing datasets available. However using a higher value may bias the sample towards users who are more active online. In the analysis here we used 300 sessions as the minimum cutoff to ensure that we would have suf<sup>fi</sup>cient data. Hence we randomly sampled users from those who had at least 300 sessions in the data. Given that the time period was one year this would suggest that our analysis would not generalize to users who are online for more limited times (less than a session a day on average). This is a limitation of our study which we recognize in Section 8.

![](/api/attachments/98K8EEHP/fulltext/images/50374ccf56fe8963e6874604c08ed115ce125dbdc4b4caea58f34f99b13dc0dc.jpg)  
Fig. 1. Histogram of the number of sessions across users.

## 4.2. Creating training and testing datasets

When a given number of users are selected, the priors in the data may be unequal to start with. For instance, when constructing a dataset of three users, the number of sessions for each user may be 300, 600 and 2100 (resulting in class priors of 0.1, 0.2 and 0.7 respectively). A naïve classi<sup>fi</sup>er predicting the most frequent class will start with an accuracy of 70%. To avoid this from providing any accuracy gains we pick the same number of sessions for all users selected in any given sub-dataset (in the example just mentioned this would mean selecting the <sup>fi</sup>rst 300 sessions for each user). This guarantees exactly equal class priors (a 20 user dataset would therefore have exactly 5% class priors for all the classes). Note that this would mean ignoring the later sessions of some of the users selected. However, this guarantees that any dataset of M users used in our study, at any level of aggregation, will always provide random guessing accuracies of 1/M. This uniform baseline will permit easy comparison across datasets, enhance interpretability of the results and ensure that any improved accuracy observed is due to behavioral patterns as opposed to an artifact of class distributions. A limitation of this though is that the actual accuracy numbers will not re<sup>fl</sup>ect the distribution on real data where the priors will be different for different users.

For each user, we then keep the <sup>fi</sup>rst 2/3 of their sessions in a master training dataset and the last 1/3 of the sessions in a master testing dataset. For any level of aggregation, the training dataset will only be based on the master training dataset and the testing will be done only from this master testing dataset. We do this to ensure that even with aggregations (i.e. pooling sessions together) there is no overlap whatsoever between any testing and training dataset.

## 4.3. Constructing datasets for different aggregation levels

There are two important issues here — how features are computed from aggregation and then the actual choice of features for this study. In Section 4.3.1, we will describe how features are computed from aggregation. In Section 4.3.2, we will then present the speci<sup>fi</sup>c features used in this study.

## 4.3.1. Aggregation and feature creation

The feature creation procedure is used to generate features that can be used in classi<sup>fi</sup>cation models for different aggregation levels. Clearly in the experiments we can use any given method for creating single session and multi-session features. A statistical approach to doing so is to <sup>fi</sup>rst determine the core set of variables that can be created for a single session, and then use groups of sessions to learn the distributions of these variables. As sessions are aggregated, we obtain better estimates of the distribution of the core variables for each user.

For instance, for a single session the core set of features may be session time, number of pages viewed and advertisements seen. Now given a set of sessions, the procedure may be de<sup>fi</sup>ned to return: bavg. session time=5.3 min, variance of session time=1.3, avg. number of pages=4, variance of number of pages=1.1, avg. number of $a d s = 7 ,$ variance of number of adds=2.2, userid=4N.

Consider the speci<sup>fi</sup>c example in Fig. 2 where, for simplicity, we just use the averages of the variables to represent the distributions. The term $D _ { \nu } ^ { a g g }$ refers to the derived dataset at aggregation level agg. F is the chosen feature creation method. There are two observations that we wish to draw attention to from this example:

1. A sliding window approach is used to generate the derived datasets at a given level of aggregation. Hence if the number of sessions for a user is m, then the number of records in the dataset for that user at level agg is m−(agg−1).

2. Since the prior probabilities of the M different users are the same in the initial dataset (as noted in Section 4.2 above), the priors in any derived dataset are also exactly 1/M. Hence aggregation by itself will not arti<sup>fi</sup>cially impact accuracy.

## 4.3.2. Specific features used in this study

The raw data provided to us in the user-centric dataset contains information about basic page/time statistics during a session and the speci<sup>fi</sup>c list of domain names (Web sites) visited in the user's session. Hence for each user session we construct four continuous measures: (i) the duration of the session (ii) number of pages viewed (iii) the starting time (in seconds after 12:00 am) and (iv) the number of sites visited. Since the speci<sup>fi</sup>c sites visited are important features, for each user session we also construct a set of binary indicators for speci<sup>fi</sup>c Web sites indicating whether there was access to a speci<sup>fi</sup>c site in a session. Given the very large number of domains, it is impossible to construct a binary indicator for every domain in the data. Instead we construct this set of features in the following manner. Assume that for a three user dataset, there are 900 total user sessions. Recall that 2/3 of this (600 sessions) is used as the training data. From this training data (the 600 sessions) we extract the top k sites for each of the three users (we report results for k=5 and 10 in the results) and take the union of these sites to create speci<sup>fi</sup>c binary variables. Since there can be common Web sites across different users, this results in a $p { < } 3 ^ { * } k$ binary indicators. Note that, as expected, the binary features created here are done only from the training data and do not use any information from the sessions in the hold out data. During aggregation, the value of these p binary variables will be decided depending on whether the p sites appear in the sessions grouped together. For example, let {site1, site2, site3} represent the $p \ ( = 3 )$ sites used as the binary variables (note: these p sites are derived from the entire training set, and do not change as aggregation level changes). When the aggregation is two sessions, each data record is corresponding to two sessions, and the values of the p variables will be 0 or 1 depending on whether these two sessions have these three sites in them. The same logic applies for other aggregation levels.

Hence for a single user session we construct four continuous variables and p binary variables. For any aggregation we compute the mean, median, variance, maximum and minimum values for the four continuous measures giving us 5⁎4= 20 speci<sup>fi</sup>c variables. Based on the p binary variables in each single session, for any group of sessions we construct p integer variables that represent the counts of the binary variables in this group. Hence on any aggregation we construct a total of 20+p variables plus the categorical dependent variable (userid.)

## 4.4. Build classifiers and record accuracies

We chose weka's J4.8 [29] as the classi<sup>fi</sup>er since classi<sup>fi</sup>cation trees in general have been shown to be highly accurate classi<sup>fi</sup>ers. The speci<sup>fi</sup>c choice of J4.8 was also for convenience since weka is an open source data mining platform that also lends itself easily to automation within scripts. We also ran experiments using neural networks and the general conclusions do not change.

As noted previously we use time-based hold out testing where the <sup>fi</sup>rst 2/3 of data is used for model building, while the last 1/3 is used as the hold out set where the accuracies are measured. Hence if 300 sessions are selected for each of the three users, the first 200 sessions of each user is used in the training set, while the last 100 sessions of each user is in the hold out test. When a model corresponding to agg = 10 is built, this will therefore use 191 (=200 − 10 + 1) points from the training data, and will use 91 (100−10+1) points from the hold out set. This guarantees that there is no overlap between the training and testing sets at any point in the process. Note that this process ensures that the hold out set also always has exactly equal class priors, making it dif<sup>fi</sup>cult to improve on the baseline accuracy of 1/(# of users) by chance.

Assume six user sessions such that:

<table><tr><td>Avg. num pages per sess.</td><td>Avg. time spent per sess.</td><td>User</td></tr><tr><td>10</td><td>30</td><td>1</td></tr><tr><td>6</td><td>20</td><td>1</td></tr><tr><td>12</td><td>15</td><td>1</td></tr><tr><td>5</td><td>40</td><td>2</td></tr><tr><td>3</td><td>10</td><td>2</td></tr><tr><td>7</td><td>15</td><td>2</td></tr></table>

![](/api/attachments/98K8EEHP/fulltext/images/f400b01415b94b68eb9985f6e128cc6c6ec2ce716bc65f94d4b4e55e7984bcbb.jpg)

<table><tr><td>Avg. num pages per sess.</td><td>Avg. time spent per sess.</td><td>User</td><td>Comment</td></tr><tr><td>8</td><td>25</td><td>1</td><td>From sessions 1 and 2 of user 1</td></tr><tr><td>9</td><td>17.5</td><td>1</td><td>From sessions 2 and 3 of user 1</td></tr><tr><td>4</td><td>25</td><td>2</td><td>From sessions 1 and 2 of user 2</td></tr><tr><td>5</td><td>12.5</td><td>2</td><td>From sessions 2 and 3 of user 2</td></tr></table>

<table><tr><td>Avg. num pages per sess.</td><td>Avg. time spent per sess.</td><td>User</td><td>Comment</td></tr><tr><td>9.33</td><td>21.67</td><td>1</td><td>From sessions 1, 2 and 3 of user 1</td></tr><tr><td>5</td><td>21.67</td><td>2</td><td>From sessions 1, 2 and 3 of user 2</td></tr></table>

Fig. 2. An example of creating datasets at different levels of aggregation.

Accuracy gains (and p-values) across number of users and aggregation levels

<table><tr><td colspan="11">increase in aggregation</td></tr><tr><td></td><td></td><td>2/1</td><td>3/2</td><td>4/3</td><td>5/4</td><td>6/5</td><td>7/6</td><td>8/7</td><td>9/8</td><td>10/9</td></tr><tr><td rowspan="9"># of users</td><td>2</td><td>0.85(0.18)</td><td>0.95(0.06)</td><td>-0.23(0.6)</td><td>0.04(0.49)</td><td>-0.64(0.79)</td><td>-1.35(0.92)</td><td>2.3(0.05)</td><td>-0.7(0.75)</td><td>0.7(0.27)</td></tr><tr><td>3</td><td>1.34(0.05)</td><td>0.25(0.37)</td><td>0.77(0.16)</td><td>0.15(0.39)</td><td>0.19(0.3)</td><td>-0.41(0.62)</td><td>0.2(0.41)</td><td>0.37(0.14)</td><td>0.56(0.11)</td></tr><tr><td>4</td><td>3.36(0)</td><td>-0.16(0.59)</td><td>1.44(0.01)</td><td>-0.85(0.92)</td><td>0.64(0.11)</td><td>-0.18(0.67)</td><td>-0.3(0.83)</td><td>1.34(0.04)</td><td>-0.31(0.71)</td></tr><tr><td>5</td><td>3.88(0)</td><td>1.28(0)</td><td>0.28(0.21)</td><td>-0.25(0.72)</td><td>-0.05(0.53)</td><td>1.09(0.04)</td><td>-0.24(0.74)</td><td>0.34(0.21)</td><td>-0.79(0.89)</td></tr><tr><td>10</td><td>5.25(0)</td><td>1.2(0)</td><td>0.76(0.11)</td><td>-0.02(0.51)</td><td>0.61(0.09)</td><td>-0.83(0.94)</td><td>0.43(0.12)</td><td>0.05(0.46)</td><td>-0.84(0.92)</td></tr><tr><td>15</td><td>6.47(0)</td><td>2.33(0)</td><td>0.96(0.11)</td><td>0.87(0.01)</td><td>-0.56(0.94)</td><td>-0.09(0.59)</td><td>0.24(0.3)</td><td>-0.01(0.51)</td><td>-0.56(0.91)</td></tr><tr><td>20</td><td>6.92(0)</td><td>2.05(0)</td><td>0.83(0.02)</td><td>0.7(0.02)</td><td>0.66(0.02)</td><td>-0.13(0.67)</td><td>-0.52(0.92)</td><td>0.08(0.41)</td><td>0.51(0.08)</td></tr><tr><td>50</td><td>8.86(0)</td><td>3.19(0)</td><td>1.59(0)</td><td>0.34(0.07)</td><td>0.03(0.46)</td><td>-0.06(0.59)</td><td>0.32(0.11)</td><td>0.03(0.46)</td><td>-0.09(0.62)</td></tr><tr><td>100</td><td>10.13(0)</td><td>3.9(0)</td><td>1.49(0)</td><td>0.75(0)</td><td>0.33(0.04)</td><td>0.13(0.27)</td><td>0.36(0.06)</td><td>-0.4(0.98)</td><td>-0.11(0.7)</td></tr></table>

## 5. Results for Q1a and Q1b: Effect of aggregation

Table 1 summarizes the results of eighty-one tests examining the value of aggregation. Note that as evident from the methodology, each of these tests is on a different dataset. Hence we do not face the problem of multiple hypotheses testing on a single dataset.

Each cell in the table has an accuracy gain and a p-value computed from 50 different runs. For example, the values in the lower left cell (100, 2/1) are computed as follows. In each of 50 runs, 100 different users are randomly chosen, and the classi<sup>fi</sup>er is built for agg=1 and agg=2, thereby resulting in two columns of 50 accuracy values. From these two columns, the average accuracy gain due to the higher aggregation is computed, and a directional test of signi<sup>fi</sup>cance (testing whether the accuracy gain is signi<sup>fi</sup>cantly greater than zero) is used to compute the p-value. The average accuracy gains reported in this table are all absolute, and not relative <sup>fi</sup>gures. For example, in this particular cell (lower left), the average absolute accuracy improvement for agg=2 over agg=1 is 10.13%, and the test indicates signi<sup>fi</sup>cant value of aggregation with p-value=0.

Does aggregation result in improved user identi<sup>fi</sup>cation online? At the face of it, the results seem mixed to negative, with only 26 out of 81 tests showing signi<sup>fi</sup>cant positive differences due to aggregation, almost suggesting a lack of value.

However, the effect is not evenly distributed. There is a strong pattern where the lower left quadrant is almost entirely signi<sup>fi</sup>cant with high absolute gains. Speci<sup>fi</sup>cally, 17 of 20 cells in this quadrant here show highly signi<sup>fi</sup>cant gains, suggesting that the main value from aggregation is in this range. These results hence show two effects:

1. The value of aggregation increases with problem complexity (# of users/classes). For the <sup>fi</sup>rst few columns, the absolute accuracy gains on average increase with increasing complexity (i.e. going down the columns).

2. For more complex problems the gains from aggregation seem to hold for a greater range of aggregations. For instance, for the 100 user datasets signi<sup>fi</sup>cant gains from aggregation exist all the way until agg=6, while for the less complex problems the bene<sup>fi</sup>ts seem to stop earlier. This suggests that for a <sup>fi</sup>xed complexity (i.e. # of users in the dataset) there may be a (different) minimum level of aggregation. This is what we investigate in Q2 where we seek to empirically determine this minimum value for different complexity levels.

For illustration purpose, we graphed the average accuracy gains for 4 levels (number of users=2, 5, 20, 100) in Fig. 3. As we can see, the improvement levels off as the level of aggregation increases.

Table 2 examines speci<sup>fi</sup>cally the value of going from no aggregation to agg=2 as a function of the difference in problem complexity. While these values can be directly computed from those in Table 1, the results here focus on how much the accuracy gains increase when going from no aggregation to the <sup>fi</sup>rst level of aggregation (agg=2). The cell corresponding to the bottom left value with coordinates (100,2) should be interpreted as follows. If the average increase in accuracy from going from no aggregation to agg=2 for 100 user datasets is x, and if the same value for 2 user datasets is y, then x−y=9.28 (the value in the cell). The signi<sup>fi</sup>cance tests whether the accuracy gain for the higher number of users is signi<sup>fi</sup>cantly greater than that of the lower number of users. All numbers are positive and mostly signi<sup>fi</sup>cant, showing that as the relative problem complexity increases there is clear evidence of increased value with some aggregation.

![](/api/attachments/98K8EEHP/fulltext/images/4c27a8179d0596831e8c7ece3ab54803bea121a094080e76d5d5f563be680725.jpg)  
Fig. 3. Average accuracy gains across 4 different number of users.

Table 2  
Accuracy gains going from no aggregation to agg=2.

<table><tr><td colspan="9"># of users</td><td></td></tr><tr><td></td><td></td><td>2</td><td>3</td><td>4</td><td>5</td><td>10</td><td>15</td><td>20</td><td>50</td></tr><tr><td rowspan="8"># of users</td><td>3</td><td>0.49(0.347)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>2.51(0.015)</td><td>2.03(0.016)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>3.03(0.005)</td><td>2.54(0.003)</td><td>0.52(0.245)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>4.4(0)</td><td>3.91(0)</td><td>1.89(0.007)</td><td>1.37(0.033)</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>5.62(0)</td><td>5.13(0)</td><td>3.1(0)</td><td>2.59(0)</td><td>1.22(0.035)</td><td></td><td></td><td></td></tr><tr><td>20</td><td>6.07(0)</td><td>5.58(0)</td><td>3.56(0)</td><td>3.04(0)</td><td>1.67(0.01)</td><td>0.45(0.22)</td><td></td><td></td></tr><tr><td>50</td><td>8(0)</td><td>7.52(0)</td><td>5.49(0)</td><td>4.97(0)</td><td>3.6(0)</td><td>2.39(0)</td><td>1.93(0)</td><td></td></tr><tr><td>100</td><td>9.28(0)</td><td>8.79(0)</td><td>6.77(0)</td><td>6.25(0)</td><td>4.88(0)</td><td>3.66(0)</td><td>3.21(0)</td><td>1.28(0)</td></tr></table>

## 6. Methodology for Q2

Conditional on aggregation helping identi<sup>fi</sup>cation accuracy, in Q2 we seek to determine the minimum aggregation needed to attain a speci<sup>fi</sup>c threshold accuracy for online user identi<sup>fi</sup>cation. This can clearly be done by exhaustive search, which may be preferred when the expected levels are likely to be fairly small. In Section 6.1 we present this formally, thereby clearly delineating the inputs which will affect the results. In Section 6.2 we present a heuristic that can apply in some cases when dealing with much larger problems.

## 6.1. Determining the minimum aggregation

Let $D = \{ S _ { 1 } , S _ { 2 } , . . . , S _ { N } \}$ be a Web browsing dataset representing a total of N Web sessions. Assume that in this dataset the number of unique users is M and users are identi<sup>fi</sup>ed by a userid∈ $\{ 1 , 2 , . . . , M \}$ Next de<sup>fi</sup>ne F to be a feature creation procedure that takes a set of sessions belonging to the same user and returns a vector of attribute values $< \nu _ { 1 } , \nu _ { 2 } , . . . . , \nu _ { q } ,$ useridN. For any given level of aggregation (of sessions), agg, when F is repeatedly applied to sets of agg consecutive sessions – and in such a manner for all users – we derive a dataset $D _ { \nu } ,$ on which a classi<sup>fi</sup>er, C, is built. As done in Section 4.3, when we need to make explicit the speci<sup>fi</sup>c level of aggregation, agg, used in the process of creating $D _ { v }$ we will denote the dataset as $D _ { \nu } ^ { a g g } .$

Here C is any classi<sup>fi</sup>cation algorithm that can be applied to data to learn the classi<sup>fi</sup>cation function g: $V  U$ that maps any feature vector v∈V to a user ${ \mathrm { I D } } \in U ,$ where $U { \in } \{ 1 , 2 , . . . , M \}$ . Hence we write $g = C ( D )$ to refer to the trained classi<sup>fi</sup>er built on the dataset D by applying algorithm C.

Fig. 4 formally presents the procedure for determining the smallest level of aggregation. Here we start with a set of sessions and <sup>fi</sup>rst group all sessions belonging to the same user. For each user, we then sort all sessions chronologically, and then apply a sliding window of size agg to pick out all groups of consecutive sessions of size agg. The feature creation procedure is then applied to every such window to create feature vectors. On all the feature vectors constructed in this manner a classi<sup>fi</sup>er is built. If the goodness of this classi<sup>fi</sup>er is better than some threshold goodness then we say that users can be identi<sup>fi</sup>ed at this (agg) level of aggregation. If not, the process repeats after incrementing agg by one and terminates based on a user-speci<sup>fi</sup>ed stopping condition (we use a maximum agg of 30 for these experiments).

```txt
Inputs: Dataset D = { S1, S2, ..., SN } of N sessions.
Feature creation function F(s) returning a vector of features
    <v1, v2, ..., vq, userid>, where s is a set of sessions.
Classification algorithm C and related model goodness criterion, goodness.
Threshold goodness, A, at which the learned classifier is deemed to adequately classify users.(A can be < 1 if some misclassification can be tolerated).
A procedure, TEST_STOP, to test if some other stopping condition is met.

Output: The minimum level of aggregation, agg

model_acc = 0; agg = 0; other_stopping_condition = FALSE
Compute M as the number of unique userIDs in D
for u = 1 to M do
    Select all sessions belonging to user u in D: X1(u), X2(u), ..., Xku(u)
    // Xj(u) represents the j-th session of user u.
    // ku represents the total number of sessions from user u.
    Sort X1(u), X2(u), ..., Xku(u) chronologically such that the time that session Xi(u) starts < time that session Xj(u) starts whenever i < j

end for
num_sessions = min(k1, k2, ..., kM) // use same number of sessions for all users
Create master training dataset by selecting first 2/3 of num_sessions for all users
Create master testing dataset by selecting the last 1/3 of num_sessions for all users
while ((model_acc < A) AND not(other_stopping_condition)) do
    agg = agg + 1
    Dv = {}
    for u = 1 to M do
    Let Sagg = {RXagg | RXagg is a set of agg consecutive sessions of user u in master training dataset}
    // i.e. all sliding windows of size agg are created and stored in Sagg
    For all s ∈ Sagg
    Dv = Dv ∪ F(s)

end for
Following the same procedure, aggregate sessions in the master testing dataset to create TDv
g = C(Dv) // i.e. g is the trained classifier
model_acc = goodness(g) // as evaluated on the aggregated testing dataset TDv
other_stopping_condition = TEST_STOP( ). 
end while
If (model_acc < A) // the "other stopping condition" terminated the iterations
    agg = -1
return agg
```  
Fig. 4. Determining the minimum level of aggregation needed.

Note that the goodness of the classi<sup>fi</sup>er is also considered an input since it can be based on different criteria. Without loss of generality we assume that goodness is de<sup>fi</sup>ned such that a larger value corresponds to a better model. As done in Section 4 in our experiments we de<sup>fi</sup>ne goodness as accuracy on a separate test dataset created from the last 1/3 of all user sessions (before any aggregation).

The procedure to determine the minimum agg in Fig. 4 was for a given set of users. We iterate this over a large number of runs to derive empirical estimates for Q2.

## 6.2. A heuristic for large problems

In practice we may wish to limit the search to a small number of possibilities and hence the procedure suggested in Section 6.1 may suf<sup>fi</sup>ce and is the methodology used for the experiments in this paper. However for generality in this section we consider cases where the different levels of aggregation to be considered are perhaps unknown at the outset (worst case=the total number of sessions a user has) or are too large to permit exhaustive search across different levels of aggregation. For such cases (as we note below) we present a heuristic here that can reduce the complexity of the process, bringing it to O (log |D|).

Let $g ^ { \prime } { = } C ( D _ { \nu } ^ { i } )$ , denoting the classi<sup>fi</sup>cation function learned from applying the feature creation procedure F on the original dataset D at a level of aggregation i. Similarly let $g ^ { \prime \prime } { = } C ( D _ { \nu } ^ { j } )$ . Also assume a given goodness measure T. If T can be guaranteed to be monotonic in the levels of aggregation considered then binary search can be used to determine minimum aggregation levels. The monotonicity assumption speci<sup>fi</sup>cally is the following.

Given C, D, F and T, then $T ( g ^ { \prime } ) { \geq } T ( g ^ { \prime \prime } )$ whenever iNj, where as noted earlier:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- $g' = C(D_v^i), g'' = C(D_v^j)$ and
</div>

• D<sub>v</sub><sup>i</sup> refers to the aggregated dataset created by applying F to D at level of aggregation i.

This states that the goodness of the model when applied to more aggregated data is never worse than the goodness of the model applied to less aggregated data.

It is dif<sup>fi</sup>cult to prove that this holds for arbitrary C, D, F and T, but it may be possible to empirically test if this is true within the range of aggregations that may be considered. When this is assumed to hold – which can be tested empirically – then the procedure described below can be used to answer Q2 in a more ef<sup>fi</sup>cient manner.

Since the monotonicity assumption implies that the model goodness at increasing levels of aggregation is sorted in ascending order, binary search can be used in such cases reducing complexity to O(log<sub>2</sub>|D|). Using the notation in Section 6.1 we present the algorithm for this case (see Fig. 5).

When the sequence is not exactly in ascending order (i.e. when the assumption does not hold) the binary search can converge to higher levels of aggregation when perhaps smaller aggregations are adequate. In such cases it may be possible to modify the technique such that it does not consider each point per se, but uses neighborhoods around each point to compute an average goodness in the neighborhood around a speci<sup>fi</sup>c point considered. This may make it feasible to deal with sequences that are mostly sorted, but not exactly so. This is not the focus of this paper but is an interesting possibility to consider in future work.

```txt
Inputs: Dataset D = { S1, S2, ..., SN } of N sessions.
Feature creation function F(s)
Classification algorithm C and related model goodness criterion, goodness
Threshold goodness, A

Output: The minimum level of aggregation, agg

model_acc = 0
Compute M as the number of unique userIDs in D
for u = 1 to M do
    Select all sessions belonging to user u in D: X1(u), X2(u), ..., Xku(u)
    Sort X1(u), X2(u), ..., Xku(u) chronologically such that the time that
    session Xi(u) starts < time that session Xj(u) starts whenever i < j
end for
num_sessions = min(k1, k2, ..., kM) // use same number of sessions for all users
Create master training dataset by selecting first 2/3 of num_sessions for all users
Create master testing dataset by selecting the last 1/3 of num_sessions for all users

start = 1, end = (1/3)*num_sessions // max aggregation that can be tested
while (end ≥ start) do
    agg = int (start + end) / 2
    Dv = {}
    for u = 1 to M do
    Let Sagg = {Xagg | Xagg is a set of agg consecutive sessions of user u in
    master training dataset}
    For all s ∈ Sagg
    Dv = Dv ∪ F(s)
    end for
    Following the same procedure, aggregate sessions in the master testing dataset
    to create TDv
    g = C(Dv) // g is the trained classifier
    model_acc = goodness(g) // as evaluated on the aggregated testing dataset TDv
    if (model_acc ≥ A)
    // current model is very good, so search again in the first half
    end = min (agg, end-1)
    else
    // the current agg is inadequate, so search in the second half
    start = agg+1
    endif
end while
If (model_acc < A)
    agg = -1
return agg

Fig. 5. Binary search for determining the minimum level of aggregation.
```

## 7. Results for Q2: determining the minimum level of aggregation

The results in Table 1 show that while there are bene<sup>fi</sup>ts from aggregation, they do not consistently increase as the aggregation level continuously increases, suggesting that monotonicity does not hold for a larger range of aggregation values. Hence we use the approach in Section 6.1 to determine the minimum level of aggregation in a range of agg=1 to agg=30.

Recall that one feature creation parameter was the number of top (k) sites to use as binary indicators as discussed in Section 4.3. Table 3a–d and 4a–d present a summary of the results for different accuracy thresholds for k=5, 10 respectively.

While the median (the second column) in all the above tables is computed based on all the 20 runs, the mean is computed just based on the terminated runs, since in the other runs, an agg does not exist or may be greater than 30 (the stopping criterion used). The last column shows the % of terminated runs — i.e. % of runs where the threshold was reached before agg=30. For instance, in the <sup>fi</sup>rst row of Table 3a, the value in the last column (100%) indicates that in this case however, all runs resulted in <sup>fi</sup>nding small agg values, and hence the stopping criterion (agg=30) never came into effect.

Table 3  
agg values across users for k=5.

<table><tr><td>Num of users</td><td>Median</td><td>Mean</td><td>% runs with agg&lt;30</td></tr><tr><td colspan="4">a (Accuracy threshold 75%)</td></tr><tr><td>2</td><td>1</td><td>1.45</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1.15</td><td>100</td></tr><tr><td>4</td><td>1</td><td>1.1</td><td>100</td></tr><tr><td>5</td><td>1</td><td>1.61</td><td>90</td></tr><tr><td>10</td><td>1</td><td>1.3</td><td>100</td></tr><tr><td>15</td><td>1</td><td>1.5</td><td>100</td></tr><tr><td>20</td><td>1</td><td>1.45</td><td>100</td></tr><tr><td>50</td><td>2</td><td>2.43</td><td>100</td></tr><tr><td>100</td><td>3</td><td>3.71</td><td>100</td></tr><tr><td colspan="4">b (Accuracy threshold 80%)</td></tr><tr><td>2</td><td>1</td><td>1.7</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1.3</td><td>100</td></tr><tr><td>4</td><td>1</td><td>1.25</td><td>100</td></tr><tr><td>5</td><td>1</td><td>1.72</td><td>90</td></tr><tr><td>10</td><td>1</td><td>1.9</td><td>100</td></tr><tr><td>15</td><td>2</td><td>3</td><td>100</td></tr><tr><td>20</td><td>2</td><td>2.2</td><td>100</td></tr><tr><td>50</td><td>4</td><td>3.75</td><td>95</td></tr><tr><td>100</td><td>6.5</td><td>7.03</td><td>70</td></tr><tr><td colspan="4">c (Accuracy threshold 85%)</td></tr><tr><td>2</td><td>1</td><td>1.85</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1.7</td><td>100</td></tr><tr><td>4</td><td>1</td><td>1.82</td><td>85</td></tr><tr><td>5</td><td>1</td><td>1.82</td><td>85</td></tr><tr><td>10</td><td>2</td><td>3.55</td><td>100</td></tr><tr><td>15</td><td>3</td><td>5.41</td><td>85</td></tr><tr><td>20</td><td>3</td><td>3.68</td><td>95</td></tr><tr><td>50</td><td>6</td><td>6.91</td><td>55</td></tr><tr><td>100</td><td>N/A</td><td>N/A</td><td>0</td></tr><tr><td colspan="4">d (Accuracy threshold 90%)</td></tr><tr><td>2</td><td>1</td><td>2.05</td><td>100</td></tr><tr><td>3</td><td>1</td><td>2</td><td>100</td></tr><tr><td>4</td><td>2</td><td>4.29</td><td>85</td></tr><tr><td>5</td><td>1.5</td><td>2.38</td><td>80</td></tr><tr><td>10</td><td>4.5</td><td>5.17</td><td>90</td></tr><tr><td>15</td><td>5</td><td>7.17</td><td>60</td></tr><tr><td>20</td><td>7</td><td>6.94</td><td>85</td></tr><tr><td>50</td><td>N/A</td><td>N/A</td><td>0</td></tr><tr><td>100</td><td>N/A</td><td>N/A</td><td>0</td></tr></table>

Table 4  
agg values across users for k=10.

<table><tr><td>Num of users</td><td>Median</td><td>Mean</td><td>% runs with agg&lt;30</td></tr><tr><td colspan="4">a (Accuracy threshold 75%)</td></tr><tr><td>2</td><td>1</td><td>1</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1</td><td>95</td></tr><tr><td>4</td><td>1</td><td>1</td><td>100</td></tr><tr><td>5</td><td>1</td><td>1</td><td>100</td></tr><tr><td>10</td><td>1</td><td>1.05</td><td>100</td></tr><tr><td>15</td><td>1</td><td>1.2</td><td>100</td></tr><tr><td>20</td><td>1</td><td>1.45</td><td>100</td></tr><tr><td>50</td><td>2</td><td>2.14</td><td>100</td></tr><tr><td>100</td><td>2</td><td>2.48</td><td>100</td></tr><tr><td colspan="4">b (Accuracy threshold 80%)</td></tr><tr><td>2</td><td>1</td><td>1</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1</td><td>95</td></tr><tr><td>4</td><td>1</td><td>2.25</td><td>100</td></tr><tr><td>5</td><td>1</td><td>1.1</td><td>100</td></tr><tr><td>10</td><td>1</td><td>1.65</td><td>100</td></tr><tr><td>15</td><td>2</td><td>2</td><td>100</td></tr><tr><td>20</td><td>2</td><td>2.5</td><td>100</td></tr><tr><td>50</td><td>3</td><td>2.95</td><td>95</td></tr><tr><td>100</td><td>4</td><td>4.8</td><td>95</td></tr><tr><td colspan="4">c (Accuracy threshold 85%)</td></tr><tr><td>2</td><td>1</td><td>1</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1</td><td>95</td></tr><tr><td>4</td><td>1</td><td>1.16</td><td>95</td></tr><tr><td>5</td><td>1</td><td>1.16</td><td>95</td></tr><tr><td>10</td><td>2</td><td>2.21</td><td>95</td></tr><tr><td>15</td><td>2</td><td>2.84</td><td>95</td></tr><tr><td>20</td><td>3</td><td>3.78</td><td>90</td></tr><tr><td>50</td><td>4</td><td>6.18</td><td>80</td></tr><tr><td>100</td><td>11.5</td><td>12.5</td><td>40</td></tr><tr><td colspan="4">d (Accuracy threshold 90%)</td></tr><tr><td>2</td><td>1</td><td>1.05</td><td>100</td></tr><tr><td>3</td><td>1</td><td>1.26</td><td>95</td></tr><tr><td>4</td><td>2</td><td>1.78</td><td>90</td></tr><tr><td>5</td><td>2</td><td>2.16</td><td>95</td></tr><tr><td>10</td><td>3</td><td>4.24</td><td>85</td></tr><tr><td>15</td><td>5</td><td>5.2</td><td>75</td></tr><tr><td>20</td><td>6</td><td>8.9</td><td>50</td></tr><tr><td>50</td><td>13</td><td>13</td><td>10</td></tr><tr><td>100</td><td>N/A</td><td>N/A</td><td>0</td></tr></table>

As noted in detail in Section 4, all the accuracies here are computed on hold out datasets (last 1/3 of sessions selected for each user) created before any aggregation.

The distribution of the agg values (beyond the mean/median values reported) can be seen from speci<sup>fi</sup>c histograms. Fig. 6 plots the histogram of the values corresponding to threshold accuracy of 90% for k=5. The right tails of the histograms show the number of runs that were terminated due to the stopping condition.

As noted before, terminating at agg=30 without reaching threshold accuracies could mean (a) that there is a higher agg value or (b) there is no agg for which the threshold accuracy can be reached. In these runs we did not test higher values since we have limited data on which it may be dif<sup>fi</sup>cult to accurately test high values. Assuming that termination implies that there is no agg for which users can be accurately identi<sup>fi</sup>ed, we plot the percentage of successful terminations (aggb30) across datasets with different number of users.

The results in Table 3a–d and 4a–da–d show that in most cases the models accurately predict user IDs for the range of users considered here, often with very few sessions. In the range of users considered here these empirical results speci<sup>fi</sup>cally indicate that:

(1) the minimum level of aggregation needed increases with problem complexity and

(2) the minimum level of aggregation increases with threshold accuracy levels.

![](/api/attachments/98K8EEHP/fulltext/images/6d84e0803f8e91ebe3a4c5a68ad2254dae834e577f21e33d2400e75ea77d065a.jpg)

![](/api/attachments/98K8EEHP/fulltext/images/25a74538fa732b03fa04e7b31b2688aae07761f405341f436e72b93ffb831a45.jpg)  
Fig. 6. Histograms of agg values across the 20 runs (accuracy threshold 90%, k=5).

Qualitatively it is worth noting that the experiments demonstrated high levels of accuracy, often with low aggregations. For instance attaining 75% accuracy levels in 100 user datasets from agg=3 on average is remarkable given that, as described in Section 4, the class priors of these datasets were exactly 1%. The high accuracies obtained come from two simple factors that the biometrics literature had shown (as noted in Section 2 of this paper) — quality of data, speci<sup>fi</sup>cally the features available to describe a single session, and the quantity of data, namely the number of sessions to be aggregated. Related to the quality factor, the set of sites visited is a strong predictor as these experiments have shown. Across all the runs the hold out accuracies with no aggregation (i.e. for $a g g = 1 )$ ranged from 56% to 98%, suggesting that the initial set of features is very informative for the classi<sup>fi</sup>er even at the single session level. Recall that the priors in the hold out datasets are exactly at 1/M, and hence even 56% for a 20 user dataset suggests substantial structure (from these features) in the data at the single session level alone. Aggregations did increase the accuracies as the results show but the gains are not always dramatic and are typically more useful for the more dif<sup>fi</sup>cult datasets as discussed. Further in these runs, the gains are highest for the <sup>fi</sup>rst few sessions aggregated (also perhaps due to the high initial accuracies), suggesting perhaps a diminishing returns effect.

## 8. Discussion

To our knowledge this is the <sup>fi</sup>rst study that has systematically studied user identi<sup>fi</sup>cation from online behavior, particularly investigating the value of aggregation. At the highest level the results in this paper may have implications for online fraud detection as well as online privacy as we note below.

These results do suggest that at the user-centric level we may be able to build reasonably accurate models identifying the user by observing “enough” data, at least for some users. This does suggest that client-side software, perhaps provided by a trusted third party or an authentication <sup>fi</sup>rm, may be developed that can monitor user behavior and provide identi<sup>fi</sup>cation scores to third parties if the user chooses to do so. Online brokerages and banks today struggle with identi<sup>fi</sup>cation mechanisms, often requiring users to register computers and remember answers to secret questions as veri<sup>fi</sup>cation mechanisms. Client-centric user scores may be complementary to such existing methods, providing yet another layer of deterrence in a multi-factor approach to fraud deterrence recommended by the US federal agency FFIEC for online <sup>fi</sup>nancial institutions. Such an application may also be deployed in a privacy-preserving manner, whereby users may voluntarily choose to use such authentication software and which works such that none of the client data is revealed, providing instead solely a user score.

As noted in Section 1, our goal in this paper is not to build the best user identi<sup>fi</sup>cation model. Rather it is to study one factor that in<sup>fl</sup>uences user identi<sup>fi</sup>cation accuracies. The design of accurate user identi<sup>fi</sup>cation models will remain a question for future research and may be one that requires the understanding of other factors that contribute to improved accuracies as well, and may also require having user-centric data on a much larger scale than we have access to.

On the <sup>fl</sup>ip side, the results also suggest that in some cases enough user data may be used to reveal identities, possibly in an unintended manner. However the range of users considered here is limited and the results do suggest an indirect value from “crowds”, where we see the need for higher aggregations as the problem complexity rises. Nevertheless the high accuracies obtained in the experiments leave open the possibility that at least some users may be identi<sup>fi</sup>able in this manner. While not the focus of this paper in future research we might investigate this question speci<sup>fi</sup>cally, seeking to determine how many – and possibly what type of – users may actually be identi<sup>fi</sup>ed based on user-centric data. For instance, it may be possible that users with low levels of general activity do not leave enough or detailed trails to permit identi<sup>fi</sup>cation, but more active and possible ‘niche’ users may be more prone to such identi<sup>fi</sup>cation. These however remain conjectures and need to be separately investigated.

As with any empirical study we developed a careful methodology but had to make speci<sup>fi</sup>c choices in this process. Hence there are important limitations and challenges that limit the scope of our results. Here we discuss the signi<sup>fi</sup>cant issues that limit generalizability and which may need to be further studied.

First, we need to study how these results will change as the number of users considered increases to higher levels. We would expect the accuracies to diminish for large number of users, but it is not clear by how much and what the improvements with aggregation may then be. However exploring scale in this manner would still mean addressing another dif<sup>fi</sup>cult problem. Building accurate classi-<sup>fi</sup>ers when the class label takes on a large set of values is known to be hard. In such cases the class priors will be very small and the heuristics used to build these classi<sup>fi</sup>ers may no longer work well. One possibility is to modify the approach here in the following manner. Speci<sup>fi</sup>cally, rather than working on a dataset where the label takes several values, the approach can be used to build a classi<sup>fi</sup>er for each user. Here for each user we can construct a dataset where the class label is now binary (this user or “anyone else”) and traditional classi<sup>fi</sup>ers can be built. The output of our approach then will be a level of aggregation that is required for each user to distinguish this user from anyone else. In this case though, a large number of classi<sup>fi</sup>ers need to be built and the data can be extremely unbalanced. This is a direction that we will pursue in future work. There are indeed other approaches that may be investigated for this too, such as reducing the size of the problem by clustering the original set of users into a more manageable number of segments before applying this procedure to distinguish between segments instead of users. In such cases we might even iteratively break segments down in this manner to ultimately predict individual users. This is similar in spirit to the idea of multi-stage classi<sup>fi</sup>cation.

The second challenge is determining the features to use. Our approach for determining minimum levels of aggregation and the accuracy results are for a speci<sup>fi</sup>c choice of these. In this paper we presented some guidelines on how to do this. Speci<sup>fi</sup>cally suggesting that session-level features can <sup>fi</sup>rst be identi<sup>fi</sup>ed, and then aggregations can be used to estimate various statistical measures of these features. However identifying good session-level features is important and may be critical to determine whether such identi<sup>fi</sup>cation can scale to higher levels. The basic set of features used in this study was constrained by the session-level data provided and does miss potentially important information such as the content of pages and/or the nature of user activity at any of the sites (i.e. does the user spend most of the time at a site on business news or online games?). Such missing features can be expected to have signi<sup>fi</sup>cant impact on identi<sup>fi</sup>cation models and aggregations. We have also conducted sensitivity analysis, which shows that the binary variables for the top sites visited are more effective at identifying users than the continuous variables (and the models with all the variables are naturally more accurate).

The third challenge is to have adequate data at the user-level. As noted in Section 4 we have one year's worth of data for each user in a random panel and had to select users for which adequate data was available. This limits the generalizability of our results. We hope this research triggers follow-on studies that may have access to larger datasets. Finally, we acknowledge generalization limitations implied by the “No Free Lunch” theorems [30,31]. Our results in this paper are derived from speci<sup>fi</sup>c data sets and learning methods and we cannot show that it will generalize to other learning methods or data.

## Acknowledgements

The authors thank the seminar participants at Microsoft Research, University of Minnesota, University of Washington, Tsinghua University and the Winter Conference on Business Intelligence at University of Utah for their useful comments.

## References

[1] G. Adomavicius, A. Tuzhilin, Using data mining methods to build customer pro<sup>fi</sup>les, IEEE Computer 34 (2) (2001) 74–82.

[2] C. Aggarwal, Z. Sun, P.S. Yu, Fast algorithms for online generation of pro<sup>fi</sup>le association rules, IEEE Transactions on Knowledge and Data Engineering 14 (5) (2002) 1017–1028.

[3] J.P. Campbell Jr, Speaker recognition: a tutorial, Proceedings of the IEEE 85 (9) (1997) 1437–1462.

[4] H. Cavusoglu, B. Mishra, S. Raghunathan, The value of intrusion detection systems in information technology security architecture, Information Systems Research 16 (1) (2005) 28–46.

[5] C. Cortes, D. Pregibon, Signature-based methods for data streams, Data Mining and Knowledge Discovery 5 (3) (2001) 167–182.

[6] K.A. Deffenbacher, J.F. Cross, R.E. Handkins, J.E. Chance, A.G. Goldstein, R.H. Hammersley, J.D. Read, Relevance of voice identi<sup>fi</sup>cation research to criteria for evaluating reliability of an identi<sup>fi</sup>cation, Journal of Psychology 123 (2) (1989) 109–119.

[7] R.A. Everitt, P.W. McOwan, Java-based Internet biometric authentication system, IEEE Transactions on Pattern Analysis Machine Intelligence 25 (9) (2003) 1166–1172.

[8] L. Ferrer, H. Bratt, V. Gadde, S. Kajarekar, E. Shriberg, K. Sonmez, A. Stolcke, A. Venkataraman, Modeling duration patterns for speaker recognition, Proc EUROSPEECH 2017-2003, 2003.

[9] J. Goecks, J. Shavlik, Learning users' interests by unobtrusively observing their normal behavior. Proc, 5th Int'l Conf. Intelligent User Interfaces, 2000, pp. 129–132

[10] M.C. González, C.A. Hidalgo, A. Barabási, Understanding individual human mobility patterns, Nature 453 (2008) 779–782.

[11] M. Gupta, J. Rees, A. Chaturvedi, J. Chi, Matching information security vulnerabilities to organizational security pro<sup>fi</sup>les: a genetic algorithm approach, Decision Support Systems 41 (3) (2006) 592–603.

[12] T. Herath, H.R. Rao, Encouraging information security behaviors in organizations: role of penalties, Pressures and Perceived Effectiveness, Decision Support Systems 47 (2) (2009) 154–165.

[13] K. Igarashi, C. Miyajima, C.K. Itou, K. Takeda, F. Itakura, H. Abut, Biometric identi<sup>fi</sup>cation using driving behavioral signals, Proc. Int'l Conf. Multimedia and Expo, 2004, pp. 65–68.

[14] J. Kerstholt, N. Jansen, A. Van Amelsvoort, A. Broeders, Earwitnesses: effects of speech duration, retention interval and acoustic environment, Applied Cognitive Psychology 18 (3) (2004) 327–336.

[15] D.J. Kim, D.L. Ferrin, H.R. Rao, A trust-based consumer decision-making model in electronic commerce: the role of trust perceived risk and their antecedents Decision Support Systems 44 (2) (2008) 544–564

[16] T. Ko, R. Krishnan, Monitoring and reporting of <sup>fi</sup>ngerprint image quality and match accuracy for a large user application, Proc. 33rd Applied Imagery Pattern Recognition Workshop, 2004, pp. 159–164.

[17] R. Kosala, H. Blockeel, Web mining research: a survey, SIGKDD Explorations 2 (1) (2000) 1–15.

[18] G.E. Legge, C. Grosmann, C.M. Pieper, Learning unfamiliar voices, Journal of Experimental Psychology. Learning, Memory, and Cognition 10 (2) (1984) 298–303.

[19] J. Li, R. Zheng, H. Chen, From <sup>fi</sup>ngerprint to writeprint, Communications of the ACM 49 (4) (2006) 76–82.

[20] D. Madigan, A. Genkin, D.D. Lewis, S. Argamon, D. Fradkin, L. Ye, Author identi<sup>fi</sup>cation on the large scale, Proc. Interface and the Classi<sup>fi</sup>cation Society of North America, 2005.

[21] J. Mäntyjärvi, M. Lindholm, E. Vildjiounaite, S. Mäkelä, H. Ailisto, Identifying users of portable devices from gait pattern with accelerometers, Proc. IEEE International Conference on Acoustics, Speech, and Signal Processing, 2005.

[22] B. Miller, Vital signs of identity, IEEE Spectrum 31 (2) (1994) 22–30.

[23] B. Mobasher, H. Dai, T. Luo, M. Nakagawa, Discovery and evaluation of aggregate usage pro<sup>fi</sup>les for web personalization, Data Mining and Knowledge Discovery 6 (1) (2002) 61–82.

[24] F. Monrose, A. Rubin, Authentication via keystroke dynamics, Proc. 4th ACM Conference on Computer and Communications Security, 1997, pp. 48–56.

[25] B.K. Natarajan, Machine Learning: a Theoretical Approach, Morgan Kaufmann, 1991.

[26] P.L. Pirolli, Information Foraging Theory: Adaptive Interaction with Information Oxford University Press, Cambridge, UK, 2007.

[27] J. Srivastava, R. Cooley, M. Deshpande, P-T. Tan, Web usage mining: discovery and applications of usage patterns from web data, SIGKDD Explorations 1 (2) (2000) 12–23.

[28] D. Straub, Effective is security: an empirical study, Information Systems Research 1 (3) (1990) 255–276.

[29] H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques. 2nd ed, Morgan Kaufmann, San Francisco, 2005.

[30] D.H. Wolpert, The lack of a priori distinctions between learning algorithms, Neural Computation 8 (7) (1996) 1341–1390.

[31] D.H. Wolpert, W.G. Macready, No Free Lunch theorems for optimization, IEEE Transactions on Evolutionary Computation 1 (1) (1997) 67–82.

[32] Y. Yang, B. Padmanabhan, GHIC: a hierarchical pattern based clustering algorithm for grouping web transactions JEEETransactions on Knowledge and Data Engineering 17 (9) (2005) 1300–1304.

[33] A.D. Yarmey, Voice identi<sup>fi</sup>cation over the telephone, Journal of Applied Social Psychology 21 (22) (1991) 1868–1876.

[34] A.D. Yarmey, E. Matthys, Voice identi<sup>fi</sup>cation of an abductor, Applied Cognitive Psychology 6 (5) (1992) 367–377.

[35] X. Zhao, F. Fang, A.B. Whinston, An economic mechanism for better internet security, Decision Support Systems 45 (4) (2008) 811–821.

[36] E.N. Zois, V. Anastassopoulos, Methods for writer identi<sup>fi</sup>cation, Proc. IEEE International Conference on Electronics, Circuits and Systems, 1996.

![](/api/attachments/98K8EEHP/fulltext/images/afcd2a8a003b3601bc987004d38ec86956b65289495666e770ba627f2baefce8.jpg)  
Yinghui (Catherine) Yang is an assistant professor of the Graduate School of Management at University of California. Davis, She received her Ph.D. in Operations and Information Management from The Wharton School at the University of Pennsylvania, and B.E. in Management Information Systems from The School of Economics and Management at Tsinghua University. Her research is interdisciplinary between data mining and marketing. Her research has been published in top data mining journals (e.g. IEEE Transactions on Knowledge and Data Engineering) and Marketing journals (e.g. Marketing Science).

![](/api/attachments/98K8EEHP/fulltext/images/547de62846d8e6e53ec01cdd624938f2f93ba651e846e0c70456bf793cb53eed.jpg)

Balaji Padmanabhan is the Anderson Professor of Global Management and Associate Professor of Information Systems and Decision Sciences at the University of South Florida. He received a B.Tech in Computer Science from the Indian Institute of Technology (IIT), Madras and a Ph.D. in Information Systems from New York University. His work has been published in leading conferences and journals including Management Science, Decision Support Systems, MIS Quarterly, INFORMS Journal on Computing, IEEE Transactions on Knowledge and Data Engineering and Proceedings of ACM KDD JEEE ICDM WITS and AIS, He has served on the program committees of several ACM, IEEE, SIAM and WITS conferences and has editorial appointments at Information

Systems Research and INFORMS Journal on Computing.
