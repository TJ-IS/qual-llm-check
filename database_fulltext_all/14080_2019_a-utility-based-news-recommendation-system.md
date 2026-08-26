---
otero_id: 14080
otero_key: "JGQG988Z"
title: "A utility-based news recommendation system"
authors: "Morteza Zihayat; Anteneh Ayanso; Xing Zhao; Heidar Davoudi; Aijun An"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.12.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Decision Support Systems

## A utility-based news recommendation system

Morteza Zihayat, Anteneh Ayanso, Xing Zhao, Heidar Davoudi, Aijun An

![](/api/attachments/JGQG988Z/fulltext/images/5a53d07e95a2b7bab3761a075bb6c14332655a16583bc6ef902a75b0ef30da38.jpg)

PII: S0167-9236(18)30197-0

DOI: https://doi.org/10.1016/j.dss.2018.12.001

Reference: DECSUP 13014

To appear in: Decision Support Systems

Received date: 20 July 2018

Revised date: 5 December 2018

Accepted date: 5 December 2018

Please cite this article as: Morteza Zihayat, Anteneh Ayanso, Xing Zhao, Heidar Davoudi, Aijun An , A utility-based news recommendation system . Decsup (2018), https://doi.org 10.1016/j.dss.2018.12.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A Utility-based News Recommendation System

Morteza Zihayat<sup>∗</sup>, Anteneh Ayanso<sup>\$</sup>, Xing Zhao<sup>+</sup>, Heidar Davoudi<sup>+</sup>, Aijun An<sup>+</sup>

<sup>∗</sup>Ted Rogers School of IT Management, Ryerson University, Canada <sup>\$</sup>Goodman School of Business, Brock University, Canada <sup>+</sup>School of Computer Science and Engineering, York University, Canada

## Abstract

News platforms exhibit both the challenges as well as opportunities for enhancing the functionalities of recommendation systems in today’s big data environment. Novel use of big data storage and programming models can improve news recommendation systems through eficient handling and analysis of clickstream data and a better understanding of users’ interests. Most existing approaches to news recommendation consider users’ clicks as the implicit feedback to understand user behaviors. However, “clicks” may not be an efective indicator of real user interests. We address this problem by developing a novel news recommendation system based on a news utility model. Given the new utility model, we propose a two stage news recommendation framework. The framework first generates article-level recommendation rules based on the utility model, then integrates the notion of utility and probabilistic topic models and generates topic-level recommendation rules. We argue that the proposed utility-based news recommendation system also addresses the news cold start problem which is one of the most challenging obstacles for news agencies. We evaluate the framework on a massive real dataset (two billion records) obtained from a major newspaper (i.e., The Globe and Mail) in Canada and show that it outperforms the existing methods.

Keywords: News Recommendation Systems, News Utility Model, Big Clickstream Data, MapReduce, Rule Mining.

## 1. Introduction

Recent advancements in Internet-based technologies and the production of digital contents have shifted news consumption models from reading physical newspapers to visiting online news websites. Understanding and modeling users’ interests is a critical task for the value proposition and prosperity of any online service provider. Moreover, in the digital age, value creation has become value co-creation between companies and customers [1]. Thus, many companies focus on their big historical data to model users’ behaviors and boost profits. Similarly, online newspaper agencies aim to provide personalized contents to improve visit experiences. This does not only increase the frequency of visits, which boosts the revenue through the advertisements, but also improves user engagement, leading to more subscriptions [2]. In fact, from an online news provider’s business perspective, increasing the revenue through advertisements and subscriptions is a major objective. Therefore, for most online newspapers, developing efective recommendation systems to help users find interesting articles and keep them engaged is of paramount importance.

Building an efective and eficient recommendation system for the news domain is much more challenging than other domains:

1. Business Objectives Trade-of. As the business model evolves, many online news publishers are struggling to balance the availability of high value advertising inventory with the need for content that maximizes opportunities for subscriber acquisition and retention. Thus, in many cases, a recommendation system is needed in which recommended articles satisfy more than one business objective, even if those objectives are in contention with one another.

2. Beyond Click-Through Rates. Conventional news recommendation systems only consider a click as an implicit feedback. This is quite problematic because a user might click on an article but may not be interested in reading it (e.g., the title may be appealing to her while the content may not meet her expectations). Therefore, the number of clicks may not be helpful to address an intended domain specific objective. For example, it is very likely that user engagement increases the number of subscriptions, therefore a news agency might be interested in a type of recommendation which increases the engagement (e.g., dwell time of visited articles) thus the subscription rate. However, click analysis does not necessarily maximize this objective.

3. Big Data of Unknown Visitors. Newspapers are rich repositories of visitors’ historical data. In 2016, the number of average monthly unique visitors for top 50

# ACCEPTED MANUSCRIPT

U.S. newspapers was more than 11 billion<sup>1</sup>. The user interaction data of The Globe and Mail<sup>2</sup>, Canada’s foremost news media company, is about 30 million sessions in one month. Building a recommendation system that can handle big data requires applying scalable techniques and platforms[3]. Moreover, despite the availability of such huge volume of historical data, most interactions belong to un-subscribed users (i.e., unknown visitors). Therefore, user profiling and collaborative filtering techniques such as Matrix factorization [4] are not efective recommendation approaches in the news domain. This is due to the fact that such approaches need to identify users and collect their reading histories to discover their interests and the similarity among them.

4. News/Users Cold Start Problems. Articles are generated continuously and unboundedly at a high speed. This makes recommending new articles much harder than recommending new items (e.g., new products, new travel packages [5]) in other ecommerce domains. Thus, the ability to handle the cold start problem is essential for newspapers. There are two types of cold start problems: user cold start (when a new or unknown user visits the portal) and item cold start (when a new article is published). Despite diferent solutions [6, 7] to this major issue, this problem is still challenging, particularly in the news domain.

To address the aforementioned challenges, this paper presents a Utility-based News Recommendation SYStem, called URecSYS, which works based on a news utility model. The idea of the news utility model is inspired by the concept of utility in intelligent agents. In intelligent agents and machine learning, goal-based agents and utility-based agents are two common classes of agents [8]. A goal-based agent can only diferentiate between goal and non-goal states in the environment. However, it is important to measure how desirable a particular state is. To do so, a utility function is defined such that it measures how satisfied the agent (e.g., a visitor) will be if it moves to a particular state (e.g., article). This helps agents to move toward a goal state (e.g., increase user engagement) with the highest satisfaction. It is important to note that the concept of utility in our model is very similar to its common usage in economics. In economics, the term utility is used to describe the measurement of usefulness and satisfaction that a consumer obtains from any good [9]. The utility is not a characteristic of a particular good (e.g., article), but rather of each consumer’s reactions (e.g., user’s engagement) to that good. In this paper, we argue that the utility can be defined in the context of recommendation. We model the utility to represent a desirable domain specific objective and recommend article with respect to this specific objective. In other words, we design a utility model to recommend those articles that persuade the user to move toward a higher value of the objective. For example, if the objective is to increase user engagement, a utility model can be designed such that a recommender suggests articles that lead to a highly engaged visit.

The news utility model is designed based on two broad types of attributes: article and user-article interaction attributes. Importantly, the model can be engineered to address one or more objectives even if those objectives are in conflict with one another. URecSYS recommends news articles by discovering article-level rules based on the news utility model. Moreover, by leveraging topic modeling and a probabilistic framework, it generalizes rules from the article-level to the topic-level. This addresses the news cold-start problem properly as newly-published articles can be recommended to a user by matching them to the topiclevel rules. Moreover, as the news utility model is built based on reading sessions of all users, the recommendation rules (at either the article-level or the topic-level) can be used for new users, thus also resolves the user cold start problem.

To the best of our knowledge, this study is the first step towards exploring the impact of both article and user-article interaction attributes in a unified framework. Our contributions are summarized as follows:

1. We define a novel model, called News Utility Model, to simultaneously consider both article attributes (e.g., the recency of the article) and user-article interaction attributes (e.g., DwellTime). We argue that it is more beneficial to recommend news articles based on the utility of articles rather than the browsing frequency of articles.

2. We propose a novel and scalable rule engine to discover article-level recommendation rules based on the news utility model. At its heart, the rule engine uses multiple

MapReduce-like steps to discover article-level recommendation rules in parallel.

3. We propose a novel probabilistic approach on top of topic-based models to generalize article-level news recommendation rules. The output is a topic-level recommendation rule engine that links topics of articles based on the news utility model, thus the domain specific objective. Such rules recommend newly-published articles based on topics of interests to users.

4. We apply the proposed framework to a dataset of two billion records collected from a major Canadian news agency (The Globe and Mail <sup>3</sup>) and demonstrate the efectiveness of the recommended articles by comparing the proposed framework to other state-ofthe-art recommendation systems in practice.

The rest of the paper is organized as follows. In Section 2 we provide a review of prior work relevant to news recommenders. In Section 3 we introduce terms and concepts used in this paper. In Section 4 we present the proposed framework. In Section 5 we outline the experimental settings and discuss the results. Finally, in Section 6 we provide conclusions and point out limitations and future research directions.

## 2. Literature Review

The underlying techniques used in recommender systems can be categorized into three broad classes: content-based [10, 11], collaborative filtering [4, 12, 13, 14, 15] and hybrid [7, 16, 17] approaches. Several studies have been conducted on content-based news recommendation systems[10]. For example, Liang et al. [18] propose a time-aware content recommendation system. In another work, Agrawal et al [19] take activity freshness into account and significantly outperform click-through rate (CTR). Even though content-based recommendation systems are easy to implement, they only look at a user’s profile as a bag of words which is not good enough to keep track of the exact reading interest of the user.

On the other hand, collaborative filtering approaches are built based on the users’ past rating behaviors to predict news ratings, or modeling users’ behaviors in a probabilistic way [12]. Matrix factorization [4] is a popular collaborative filtering approach that has

# ACCEPTED MANUSCRIPT

been applied to news recommendation. This approach needs users’ reading histories to find users’ interests and the similarity between users. However, in the news domain, most of the readers are not subscribed users. Moreover, it is very hard to identify users to collect their browsing histories. Some approaches consider news article co-visitations, which does not need to identify users, but only consider articles read by users in a session. For example, one main component of Google news recommender [13] is built on a network which represents co-visited articles. Alternatively, since the nature of news reading behavior is sequential, the intuitive approach to model news reading behavior is to use k-order Markov model. In this model, the next article is predicted based on the last k visited articles [14]. Nonetheless, it is not clear how to select the order k. Approaches like context-tree [15] try to alleviate the problem by introducing a variable-order Markov model. However, they treat all articles equally important which may not be suitable in practice. Collaborative filtering systems are eficient in cases where historical consumption across users and the content universe is almost static. However, in the news domain, the contents (i.e., items) change over time drastically. Moreover, we usually have news and user cold start problems. These issues make collaborative filtering inefective in news recommendation environments. In [16], the authors investigate how dwell time is computed from a large scale web log. Later, for collaborative filtering, they use dwell time as a form of implicit feedback from users and demonstrate how it can be incorporated into a state-of-the-art matrix factorization model. Moreover, the authors in [7] propose to apply the WWW as an external database to calculate the correlations between items. Then, such correlations are converted to estimate the similarity between the items. The authors show that the estimated similarities improve the performance of conventional item-based collaborative filtering systems. In [17], the authors address the cold start problem by proposing a unique method of building models derived from explicit ratings. The method first predicts actual ratings and subsequently identifies prediction errors for each user.

In practice, both content-based and collaborative filtering systems have their own advantages. To build a news recommendation system with more efective recommendations, extensive studies have been conducted on combining these methods [6, 20, 21, 22, 23]. In [23], the authors argue that a truly successful recommendation system not only considers what

# ACCEPTED MANUSCRIPT

the customer needs but also maximizes the customers’ after-sale satisfaction. To do so, they diferentiate between the customer purchase and the customer endorsement and proposed a rating classification model based on the customer’s profile and feedback. In [6] the authors focus on sequential information provided by a user’s click to predict a user’s next page visit. They show that the sequential information can improve the prediction performance. Moreover, they argue that the next page visit of a user can give useful information about their likes and tastes. They apply similarity upper approximation and singular valued decomposition for developing the recommendation system. In [20], the authors design a recommendation system that generates personalized recommendations based on preference similarity, recommendation trust, and social relations. The advantage of the proposed system, compared to traditional collaborative filtering systems, is its comprehensive consideration of recommendation sources.

Recently, some approaches consider the concept of utility in their proposed recommendation systems. For example, the authors in [24] propose a utility-based link recommendation system. They argue that existing approaches overlook the benefit a recommended link could bring to an operator. Therefore, they formulate the problem of utility-based link recommendation problem. The proposed method recommends links based on the value, cost, and linkage likelihood of a link, while existing methods focus solely on linkage likelihood. However, the concept of utility in this paper is limited to the cost and profit analysis. In [25], the authors leverage recommendation systems to predict consumers’ willingness to pay and estimate non-linear utility functions to provide a better approximation of consumers’ preference structures. They show that exponential utility functions are better suited for predicting optimal recommendation ranks for products than linear functions. The utility function proposed by [25] is more of a cost function for the proposed optimization problem than a function that represents users’ interests. Moreover, none of these approaches are applicable to the news domain directly.

Our work is essentially a hybrid recommendation approach. What diferentiates our proposed system from prior methods is that it takes a utility model into account and can handle huge volume of data as the underlying method is designed based on the MapReduce framework. Moreover, our utility model is broadly defined to be flexible and fine-tuned as

# ACCEPTED MANUSCRIPT

desired depending on the specific business objective. That is, it can consider diferent factors all together for the recommendation.

## 3. Notations and Definitions

For convenience, Table 1 summarizes the concepts and notations we define in this paper.

Table 1: Summary of Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>nw</td><td>News article</td></tr><tr><td> $S_i$ </td><td>Session i</td></tr><tr><td>D</td><td>Clickstream dataset</td></tr><tr><td> $\Psi (nw)$ </td><td>Article-driven measure of news article nw calculated based on attributes of nw</td></tr><tr><td> $\Upsilon (nw,S_r)$ </td><td>User-driven measure of article nw in session  $S_r$ </td></tr><tr><td> $\varphi (nw,S_r)$ </td><td>Utility of news article nw in session  $S_r$ </td></tr><tr><td> $\sigma (nw,P)$ </td><td>Local utility of news article nw in news reading pattern P</td></tr><tr><td> $\varphi (P,D)$ </td><td>Utility of news reading pattern P in clickstream dataset D</td></tr><tr><td> $R:X\to Y$ </td><td>An article-level rule R (news reading pattern X implies news reading pattern Y)</td></tr><tr><td> $uconf(R)$ </td><td>The utility confidence of article-level rule R</td></tr><tr><td> $min\_uconf(R)$ </td><td>The minimum utility confidence of article-level rule R</td></tr><tr><td> $R:t_i\to t_j$ </td><td>The topic-level rule R (topic  $t_i$  implies topic  $t_j$ )</td></tr><tr><td> $tconf(R)$ </td><td>The utility confidence of topic-level rule R</td></tr><tr><td> $min\_tconf(R)$ </td><td>The minimum topic confidence of topic-level rule R</td></tr></table>

Let $\mathcal { N } = \{ n w _ { 1 } , n w _ { 2 } , . . . , n w _ { n } \}$ be a set of distinct articles. A clickstream dataset consists of several user sessions. A user session S (or session in short) is defined as an ordered list of viewed articles $\langle n w _ { 1 } , n w _ { 2 } , . . . , n w _ { z } \rangle$ within a visit. Each article is represented by diferent attributes such as popularity, topics, published date. These attributes are called article attributes. Once an article is visited by a user, diferent attributes (e.g., dwell time, timestamp) are initialized based on interactions of the user with the article. These attributes are called user-article interaction attributes and present the quality of a visit. The article and user-article interaction attributes are selected with respect to an objective. There are two common approaches to select objective-oriented attributes: 1) Attributes/metrics presented by prior literature related to the objective, 2) Feature selection approaches [26] that can be used to discover data-driven attributes with respect to the objective. Later, we present an example of the first approach when the objective is to increase user engagement.

We consider these categories of attributes to design the news utility model. Our goal is to propose a general mapping from the attributes in a clickstream dataset to a news utility model with respect to a domain specific objective. In the next section, we present a framework to utilize this model for article recommendation.

Definition 1. (Article-driven measure) Given news article nw, Article-driven measure is denoted and defined as:

$$
\Psi (n w) = F _ {\Psi} (f _ {1}, f _ {2}, \dots , f _ {k})\tag{1}
$$

where $\left\{ f _ { 1 } , f _ { 2 } , . . . , f _ { k } \right\}$ are article attributes and $F _ { \Psi }$ is an aggregation function.

Definition 2. (User-driven measure) Given a session $S _ { r }$ and a set of user-article interaction attributes $f _ { 1 } ^ { \prime } , f _ { 2 } ^ { \prime } , . . . , f _ { k } ^ { \prime }$ , the user-driven measure is defined as:

$$
\Upsilon (n w, S _ {r}) = F _ {\Upsilon} (f _ {1} ^ {\prime}, f _ {2} ^ {\prime}, \dots , f _ {k} ^ {\prime})\tag{2}
$$

where $F _ { \Upsilon }$ is an aggregation function.

Definition 3. (News Utility Model) Given an article nw and a session $S _ { r }$ , the news utility model is defined and denoted as follows:

$$
\varphi (n w, S _ {r}) = F _ {\varphi} (\Psi (n w), \Upsilon (n w, S _ {r}))\tag{3}
$$

where $F _ { \varphi }$ is the function for aggregating the article-driven and the user-driven measures.

In the above definitions, we do not limit the aggregation functions $F _ { \Psi } , \ F _ { \Upsilon }$ and $F _ { \varphi }$ to any specific form. In general, the aggregation functions can be formulated with respect to the given business objective(s). Without loss of generality, we formulate some aggregation functions as examples and illustrate them in our experiments. However, we reiterate that any other aggregation function can be formulated and utilized as desired depending on the specific business objective.

Figure 1 (a) shows a clickstream dataset consisting of five sessions $\{ S _ { 1 } , S _ { 2 } , S _ { 3 } , S _ { 4 } , S _ { 5 } \}$

<table><tr><td>Session ID</td><td>&lt;news ID, {SocialAct, DwellTime}</td></tr><tr><td>S1</td><td>&lt;nw1, {2,14} &lt;nw3, {1,3} &lt;nw5, {2,22} &lt;nw6, {2,7}</td></tr><tr><td>S2</td><td>&lt;nw4, {0.2,4} &lt;nw5, {2,15} &lt;nw6, {2,18}</td></tr><tr><td>S3</td><td>&lt;nw2, {2,14} &lt;nw4, {0.1,4} &lt;nw5, {1,19} &lt;nw6, {1,3}</td></tr><tr><td>S4</td><td>&lt;nw1, {1,4} &lt;nw3, {1,8} &lt;nw5, {0.6,13}</td></tr><tr><td>S5</td><td>&lt;nw4, {1,9} &lt;nw5, {1,2}</td></tr></table>

Figure 1: (a) Clickstream dataset with article and user-article interaction attributes, (b) Utility-oriented dataset with article-driven and user-driven measures

Assume that our domain specific objective is to recommend articles that increase user engagement. It has been shown that the recency of an article, its popularity and also social media activity (i.e., social media activity score of the user regarding an article) are indicators/triggers of the user engagement [27, 28]. Moreover, according to [16], Dwell-Time (i.e., the time that the user spends on the clicked article) is one of the efective attributes to measure engagement. Therefore, two attributes are captured per article: popularity (how popular an article is) and recency (how recent an article is). For example nw has the popularity score of 3 based on the clicks and the recency of 1 (lower value means more recent the article is) $( n w , S _ { r } ) \ =$ log(DwellT ime(usr, nw)) × SocialAct(usr, nw). We use log(DwellT ime(usr, nw)) since after a certain amount of time, DwellTime does not necessarily represent the user engagement. In addition, the article-driven measure of nw is calculated as follows: $\begin{array} { r } { \Psi ( n w ) = \frac { p o p u l a r i t y ( n w ) } { r e c e n c y ( n w ) + 1 } . } \end{array}$ In this example, two user-article interaction attributes SocialAct, and DwellTime are also captured per visited article. Higher value of SocialAct means more social activities (e.g., share the article, like the article, etc.), thus higher engagement. The item hnw<sub>1</sub>, {2, 14}i in $S _ { 1 }$ means that a user visited the news article nw<sub>1</sub>, spent 14 minutes on $n w _ { 1 }$ and had a relatively high social activity score on the article (e.g., clicked on the like button and shared it on social media). The tables in Figure 1 (b) show the results of applying the aggregation functions. The result dataset, Figure 1 (b), is called utility oriented dataset. Later, we define $F _ { \varphi }$ as a multiply function. That is, $\varphi ( n w , S _ { r } ) = \Psi ( n w ) \times \Upsilon ( n w , S _ { r } )$

# ACCEPTED MANUSCRIPT

Note that, the above example presents only one potential option for the news utility model. In practice, any other utility model can be plugged in as desired. For further illustration, Figure 2 shows examples of news utility models with respect to diferent objectives.

![](/api/attachments/JGQG988Z/fulltext/images/a19026731a97dbd8d95da98f3f3fd4d5bacc4759dd0b960041894ce6ab1fea2c.jpg)  
Figure 2: Examples of the news utility model for diferent objectives in recommendation

To take this model into account, we first define news reading pattern and then, we show how we calculate the utility of a pattern.

Definition 4. (News Reading Pattern) a news reading pattern P is a set of news articles $\{ n w _ { 1 } , n w _ { 2 } , . . . , n w _ { L } \}$ where L is the length of the pattern.

Definition 5. (Local Utility of a News Article) Given a news reading pattern P , the $\sigma ( n w _ { i } , P ) = \sum _ { P \in S _ { j } , S _ { j } \in D } \varphi ( n w _ { i } , S _ { j } )$ , where D is the clickstream dataset.

Definition 6. (High Utility News Reading Pattern) Given clickstream dataset D, a news reading pattern P is a high utility news reading pattern $i f f \varphi ( P , D )$ is not less than a given user specified threshold, where $\varphi ( P , D ) = \sum _ { S _ { r } \in D } \sum _ { n w \in P , P \subseteq S _ { r } } \varphi ( n w , S _ { r } )$

## 4. URecSYS: A Utility-based News Recommendation System

Given the proposed news utility model to present a domain specific objective, the most important challenge is how to incorporate it into the recommendation process. To address this challenge, we design a Utility-based news Recommendation SYStem (URecSYS). URec-SYS is a rule-based recommendation system which is designed and developed using Apache

Spark and MapReduce framework. URecSYS first finds recommendation rules from the clickstream dataset and then applies the discovered rules to recommend articles with respect to the current session of a user. Figure 3 shows our proposed framework. There are two main stages to discover recommendation rules: 1) article-level recommendation rule discovery, and 2) topic-level recommendation rule discovery. In Subsection 4.1, we describe Stage 1 and in Subsection 4.2, we describe Stage 2. In Subsection 4.3, we discuss how URecSYS recommends articles based on the discovered rules.

![](/api/attachments/JGQG988Z/fulltext/images/c4cbc78553e7cd4d92c1fb1174bcd73c05089bd34ccaff23e04f294a6662a921.jpg)  
Figure 3: URecSYS, the proposed framework

## 4.1. Stage 1: Article-level Recommendation Rule Discovery

Most rule-based recommendation systems generate association rules from data. That is, they first discover all the news reading patterns whose frequency (e.g., occurrences of the pattern in the data) is no less than a minimum support threshold [29]. Then, given a frequent news reading pattern P , all the rules in the form of R : A → B are generated from P if the confidence of R is no less than a confidence threshold. The confidence is the percentage of sessions containing the pattern B among the set of sessions containing the pattern A. However, this approach is not able to tell how satisfactory articles in B are by knowing that the articles in A were satisfactory with respect to a domain specific objective.

We propose a novel rule discovery framework to find all article-level rules R : A → B based on the proposed news utility model. We argue that recommendations are satisfactory if they meet two conditions: 1) A reading session, including visited articles and the recommended ones, should form a high utility news reading pattern, 2) The recommended articles should increase the utility to some extent by providing more satisfactory information. To meet these conditions, we define an article-level news recommendation rule as follows. Given two news reading patterns X and Y , a rule $R : X \to Y$ (X implies Y) is an article-level news recommendation rule if:

1. $X \neq \emptyset , Y \neq \emptyset$ and $X \cap Y = \emptyset$

2. Y and $X \cup Y$ are high utility news reading patterns.

3. Its utility confidence $( u c o n f ( R ) )$ is no less than a user-defined minimum threshold $( m i n \_ u c o n f )$ , where

$$
u c o n f (R) = \frac {\sigma (Y , X \cup Y)}{\sigma (X \cup Y , X \cup Y)}\tag{4}
$$

Rationale: The utility-confidence of the rule $R : X \to Y$ reflects the utility contribution of Y to the utility of news reading pattern $X \cup Y . \mathrm { ~ T h a t }$ is, it recommends Y , associated to X, where $X \cup Y$ forms a high utility news reading pattern. A higher confidence indicates a higher total utility value of the recommended news articles.

Our proposed framework to discover such rules consists of two parts: (1) high utility news reading pattern discovery (to meet condition 1 ), and (2) identifying article-level news recommendation rules (to meet condition 2 ). Mining high utility news reading patterns from a big clickstream dataset is not an easy task. To mine such patterns, the method should deal with the critical combinatorial explosion of search space caused by sequencing among articles in sessions. Moreover, pruning the search space is more dificult than that in traditional frequent pattern mining as the news utility model is not necessarily monotonic, and thus downward closure property does not hold for mining high utility news reading patterns. That is, the utility of a pattern may be higher than, equal to, or lower than its super-patterns and sub-patterns [30]. In addition, with a considerably large number of sessions whose information may not be entirely loaded into memory, developing a distributed method is the only solution to identify article-level recommendation rules.

Figure 4 shows an overview of the proposed framework to discover article-level recommendation rules using several MapReduce jobs. In this work, we use an extended version of a recently proposed approach called $B i g H U S P$ [30] to discover article-level news recommendation rules. In the first MapReduce, we apply Definition 1 and Definition 2 to build the utility-oriented dataset (See Figure 1 (b)). Given the utility-oriented dataset, using one Mapper and one MapReduce, the framework discovers high utility news reading patterns. Lastly, article-level recommendation rules are discovered using the last MapReduce.

![](/api/attachments/JGQG988Z/fulltext/images/954fd12fff9193d5434e54d0a5a1887114f55c5361360912547226ced8084d15.jpg)  
Figure 4: The Conceptual Big Data Framework for Article-level Rule discovery

Algorithm 1 shows the proposed method to discover high utility news reading patterns. In lines 1-8, we first distribute the data among nodes in a cluster of computers, and then convert the input dataset based on the given news utility model. In line 9, the algorithm runs a procedure [30] to discover high utility news reading patterns in each mapper. A high utility news reading pattern in a mapper is called local high utility news reading pattern and the set of local high utility news reading patterns in the mapper i is denoted as $\chi _ { i }$ . Then, using a MapReduce job, we discover high utility news reading patterns by aggregating patterns in

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 High Utility News Reading Pattern Discovery
Input: A utility-oriented dataset D, News utility model  $F_{\varphi}$ , Minimum utility threshold  $\delta$ 
Output: High Utility News Reading Patterns  $\Re$ 
1: Distribute D among m nodes in the cluster  $\{D_{1}, D_{2}, \ldots, D_{m}\}$ 
2: for  $\forall S_{i} \in each D_{j} do$ 
3: for  $\forall nw \in S_{i} do$ 
4:  $\varphi(nw, S_{i}) \leftarrow F_{\varphi}(\Psi(nw), \Upsilon(nw, S_{i}))$ 
5: Add  $\langle nw, \varphi(nw, S_{i}) \rangle$  to session  $S_{i}'$ 
6: end for
7: Add  $S_{i}'$  to  $D_{j}'$ 
8: end for
9:  $\chi_{i} \leftarrow$  Find high utility news reading patterns in node i using  $\delta$  and  $D_{i}'$ 
10:  $X \leftarrow$  Aggregate  $\chi_{i}$ s to find high utility news reading patterns over  $D'$ 
11: Return X
</div>

Given a set of high utility news reading patterns, a naive solution to discover articlelevel rules is to generate all the rules using an exhaustive search. However, this approach produces all the possible subsets of a high utility news reading pattern P with k articles,

# ACCEPTED MANUSCRIPT

that is $2 ^ { k }$ subsets which grows exponentially. As we are dealing with a huge volume of data, we are more interested in finding possible antecedents for a consequent eficiently (e.g., in a linear time) without missing rules with highest confidence among all rules mined from the same pattern. Our goal is to design a greedy algorithm to discover article-level news recommendation rules in a linear time.

Theorem 1. Given a news reading pattern $P = \{ n w _ { 1 } , n w _ { 2 } , . . . , n w _ { n } \}$ where $\sigma ( n w _ { 1 } , P ) <$ $\sigma ( n w _ { 2 } , P ) < . . . < \sigma ( n w _ { n } , P ) , X = \{ n w _ { 1 } , n w _ { 2 } , . . . , n w _ { k } \} \subseteq P$ $k \leq n$ and any article nw<sub>i</sub> from P where $\sigma ( n w _ { i } , P )$

$$
u c o n f (\langle \{X - n w _ {k} \} \rightarrow n w _ {i} \rangle) > u c o n f (\langle \{X - n w _ {k - 1} \} \rightarrow n w _ {i} \rangle)\tag{5}
$$

where term $X - n w _ { k }$ excludes the article nw<sub>k</sub> from its residing set X.

Given Theorem 1, Algorithm 2 shows the overview of our proposed greedy algorithm to discover article-level recommendation rules. The algorithm takes a high utility news reading pattern and min uconf as inputs and returns the article-level news recommendation rules. In line 2, we first sort articles in pattern P in an ascending order based on the local utility of articles in the session. Given each article nw, Algorithm 2 generates all article-level recommendation rules whose antecedent is nw.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Article-level Rule Engine

Input: A set of high utility news reading patterns PSet, min_uconf

Output: A set of article-level recommendation rules R

1:  $R \leftarrow \emptyset$ 

2:  $PSet' \leftarrow$  sort articles  $nw \in P$  in ascending order based on  $\sigma(nw, P)$  where  $P \in PSet$ 

3: for each  $P = \{nw_{1}, nw_{2}, ..., nw_{n}\} \in PSet'$  do

4:    for  $i \leftarrow n : 1$  do

5:    if  $nw_{i} \in PSet'$  then

6:    $X \leftarrow \{(nw_{1}, nw_{2}, ..., nw_{i-1})\}$ 

7:    $Y \leftarrow nw_{i}$ 

8:    $R \leftarrow Algorithm 3$  with X, Y, R, min_uconf, PSet

9:    else

10:    Return

11:    end if

12:    end for

13: end for

14: Return R
</div>

Algorithm 2 calls Algorithm 3 to check the validity of each generated rule using the conditions presented in Section 4.1. Theorem 1 is applied to Algorithm 3 in the step of the article-level rule evaluation and it ensures the algorithm has a linear running time complexity. Algorithm 3 is a recursive algorithm where lines 1 and 2 set the base case to guarantee that it terminates. In Line 10, the algorithm recursively calls itself to look for a possible antecedent but with size decremented by one. The time complexity of this algorithm is O(k) compared to the exhaustive search which is $O ( 2 ^ { k } )$ (check all the subsets), where k is the length of the input high utility news reading pattern.

```txt
Algorithm 3 Backwards Analysis
Input: Antecedent (antec), Consequent (cons), current R, min_uconf, Pset
Output: updated R
1: if (X = ∅ or antec ∪ cons∉ PSet) then
2:    return
3: end if
4: uconf ← σ(Y,X∪Y)/σ(X∪Y,X∪Y)
5: if uconf ≥ min_uconf then
6:    R ← ⟨X → Y, uconf, σ(Y, X ∪ Y)⟩
7:    Add R to R
8: end if
9: for ∀nw ∈ X, X' ← X - nw do
10:    Call Algorithm 3 (X', Y,R, min_uconf, Pset)
11: end for
```

Example 1. Given a high utility news reading pattern $\langle n w _ { 6 } , n w _ { 2 } , n w _ { 4 } , n w _ { 5 } \rangle$ , all potential rules of recommending the article nw<sub>5</sub> are: r<sub>1</sub> : {nw<sub>6</sub>, nw<sub>2</sub>, nw<sub>4</sub>} → nw<sub>5</sub>; r<sub>2</sub> : $\{ n w _ { 6 } , n w _ { 2 } \} $ nw<sub>5</sub>; $r _ { 3 } : \{ n w _ { 6 } \}  n w _ { 5 }$ . Then, each rule is evaluated. Suppose the utility confidences are $f = 0 . 6$ . Therefore, only rule $r _ { 3 }$ is chosen as an article-level

## 4.2. Stage 2: Topic-based News Recommendation Rule Discovery

Article-level news recommendation rules represent the utility-based connection among articles efectively. However, they may not recommend newly published articles. A straightforward solution is to apply a content-based approach (e.g., based on topics’ similarity) to recommend newly-published articles with similar content to visited articles by a user. However, such approaches have two main drawbacks: (1) Repellent recommendations. Since recommended articles are only based on content similarity and they do not consider news reading patterns, recommended articles may not be interesting to the user, and (2) Lack of diversity. It is very common that a user reads articles with a wide variety of topics ranging from politics to sports. For example, a user may visit a news website to read some articles about presidential election and to get some updates on a basketball league. Recommending

# ACCEPTED MANUSCRIPT

articles without considering the user-based relationships among topics might not satisfy the diversity of users’ information needs. Therefore,we identify topic-level recommendation rules based on the news utility model such that the rules represent the relationships among topics.

A probabilistic topic model infers latent topics from a text corpus. For example, LDA represents a topic as a distribution over words. In particular, given a news article corpus N with a vocabulary V, a topic t is a multinomial distribution over words $w _ { i } \in \mathcal V$ , where $p ( w _ { i } | t )$ is the probability of word $w _ { i }$ in topic t. Moreover, each document is a mixture of topics. As such, given a news article nw (i.e., document) and a set of topics $T = \{ t _ { 1 } , t _ { 2 } , \cdot \cdot \cdot , t _ { i } , \cdot \cdot \cdot , t _ { m } \}$ $p ( t _ { i } | n w )$ is a probability of topic $t _ { i }$ in the article nw. In the second stage of URecSYS, we apply LDA to detect latent topics and represent each article as a distribution over topics. Then, we generate topic-level rules using our news utility model. Note that, our proposed approach works based on a probabilistic topic model, therefore any other topic modeling technique that infers a distribution for a document can be applied here as an alternative.

Given news articles represented by topics, the goal is to define relationships among topics based on article-level news recommendation rules. A naive approach is to map each article of a rule to the top-1 topic of the article (i.e., the topic with highest probability). However, this approach assumes that each article has only one topic; moreover, it generates a large number of rules which are not necessarily attractive.

Intuitively, a topic-level rule $t _ { j } ~  ~ t _ { i }$ is satisfactory if $p ( t _ { i } | t _ { j } )$ is high. We estimate this probability using the news utility model. Given an article, assuming that topics are conditionally independent, we can estimate $p ( t _ { i } | t _ { j } )$ as follows:

$$
\begin{array}{l} p (t _ {i} | t _ {j}) = \frac {\sum_ {n w \in \mathcal {N}} p (t _ {i} , n w) p (t _ {j} | t _ {i} , n w)}{p (t _ {j})} \\ = \frac {\sum_ {n w \in \mathcal {N}} p (n w) p (t _ {i} | n w) p (t _ {j} | n w)}{p (t _ {j})} = \frac {\sum_ {n w \in \mathcal {N}} p (n w) p (t _ {i} | n w) p (t _ {j} | n w)}{\sum_ {n w \in \mathcal {N}} p (n w) p (t _ {j} | n w)} \end{array}\tag{6}
$$

We can estimate the $p ( n w )$ using our news utility model as:

$$
p (n w) = \frac {\sum_ {S _ {r} \in D} \varphi (n w , S _ {r})}{\sum_ {n w _ {i} \in \mathcal {N}} \sum_ {S _ {r} \in D} \varphi (n w _ {i} , S _ {r})}\tag{7}
$$

where D is the given clickstream dataset and $S _ { r }$ is a session in D. Note that in Equation (6) we obtain the probability of $p ( t _ { i } | n w )$ from the probabilistic topic model. We define topic utility confidence of a topic-level rule $R : t _ { j }  t _ { i }$ (i.e., tconf (R)) as $p ( t _ { i } | t _ { j } )$ . Formally, given a topic-level utility confidence and a minimum topic confidence threshold min tconf , Algorithm 4 finds topic-level recommendation rules. It first draws two topics, then computes the conditional probabilities $p ( t _ { j } | t _ { i } )$ and $p ( t _ { i } | t _ { j } ) . \mathrm { ~ H ~ } p ( t _ { j } | t _ { i } )$ or $p ( t _ { i } | t _ { j } )$ is no less than a specified threshold, a new topic rule $R : \{ t _ { i } \to t _ { j } \}$ or $R : \{ t _ { j } \to t _ { i } \} )$ is discovered respectively.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4 Topic-level Rule Engine

Input: A clickstream dataset D, topic distributions on news articles corpus T, minimum topic confidence min_tconf
Output: A set of topic-level news recommendation rules  $R_{T}$ 

1: for each  $t_{i}, t_{j} \in T$  do
2: Calculate  $p(t_{i}|t_{j})$  and  $p(t_{j}|t_{i})$  using Equation 1
3: if  $p(t_{i}|t_{j}) \geq min\_tconf$  then
4: Add  $R : \langle t_{j} \to t_{i}, p(t_{i}|t_{j}) \rangle$  to  $R_{T}$ 
5: end if
6: if  $p(t_{j}|t_{i}) \geq min\_tconf$  then
7: Add  $R : \langle t_{i} \to t_{j}, p(t_{j}|t_{i}) \rangle$  to  $R_{T}$ 
8: end if
9: end for
10: return  $R_{T}$
</div>

## 4.3. Personalized News Recommendation

URecSYS calculates three scores to rank articles for recommendations:

• Article-level News Recommendation Score: Given an active user session $S _ { r }$ , the recommendation score of an article nw regarding the current reading pattern P in the session $S _ { r }$ is denoted and calculated as: $A L ( n w ) = \varphi ( P , S _ { r } ) \times u c o n f ( P  n w )$ , where $\varphi ( P , S _ { r } )$ is the utility value of the current reading pattern P in the user session $S _ { r }$ . As a subset of $P _ { \mathrm { : } }$ , it may have higher recommendation score with respect to nw, we choose the highest recommendation score from all the subsets of P as the recommendation score of $n w$ . For a reading pattern P with k articles, we use all the $2 ^ { k }$ subsets of $P$ to generate the candidate recommendations. The same size candidate (subset of P) with the highest score is considered for recommendation.

# ACCEPTED MANUSCRIPT

• Topic-level News Recommendation Score: Given the current user session $S _ { r } =$ $\{ n w _ { i } , n w _ { i + 1 } , . . . , n w _ { k } \}$ , we first discover top-k important topics from the visited articles. They are obtained by calculating the average probability of topics in the visited articles and selecting k topics with the highest probability. Then, all the topic-level rules whose antecedents are one of the top-k topics are discovered (i.e., T Rule). Given a set of rules T Rule, the recommendation score for a newly-published article $( \mathrm { e . g . , } n w )$ is calculated as: $T L ( n w ) = \sum _ { ( t _ { i }  t _ { j } ) \in T R u l e } p ( t _ { j } | n w ) \times t c o n f ( t _ { i }  t _ { j } )$ . In our experiments, for simplicity and computing eficiency, the number of topics considered for each article is limited to 5.

• Combined News Recommendation Score: The two scores are combined in ranking the candidates for news recommendation: $C o m ( n w ) = A L ( n w ) \times T L ( n w )$ . Combining the article-level score and the topic-level score ofers the advantages of both approaches and shows an improved news recommendation performance over the one using either the article-level news recommendation rules or the topic-level news recommendation rules alone.

## 5. Experimental Results and Discussions

The experimental environment consists of one master node and six worker nodes. Each node is equipped with Intel Xeon 2.6 Ghz (each 12 cores) and 128 GB main memory. The framework is implemented on Spark 2.3.0.

## 5.1. Data Collection and Data Preparation

The data used in this paper are collected from a major Canadian news agency (The Globe and Mail<sup>4</sup>). Every time a user reads an article, watches a video or generally takes an action, it is tracked on the website, and then is recorded as a hit. In data collection frameworks (e.g., Omniture by Adobe), a hit simply shows a row (record) in the data warehouse. It contains rich information about the visitors and their actions. Typically, a hit contains information like date, time, user id, user environment variables (e.g., browser type), id of article and special events of interest such as cursor movement, social activities, sign in and etc. Figure 5 illustrates the collection procedure for The Globe and Mail dataset. The sequence of interactions is as follows: (1) the user browser requests an article from The Globe and Mail news portal (i.e., G&M portal), (2) The Globe and Mail Web server responds by sending the requested article including a small Javascript code, (3) Each user-article interaction will be sent by the Javascript code to a third party server (i.e., Omniture data server), (4) The data collection server sends the collected data periodically to The Globe and Mail to be used in the data analytics pipeline.

![](/api/attachments/JGQG988Z/fulltext/images/be17468b11997d5d7cd97f71170a2fa2aa4b99dbc0c5c8e3f07502e55177bfb4.jpg)  
Figure 5: Data Collection Platform

The Globe and Mail clickstream dataset is composed of 2 billion hits. It contains 246 attributes which capture diferent aspects of interactions with users. Table 2 describes the various types of attributes in The globe and Mail clickstream dataset.

Table 2: Categories of attributes in The Globe and Mail Dataset.

<table><tr><td>Attributes</td><td>Description</td></tr><tr><td>Traffic Variables</td><td>Count the instances of specific events on a web page (e.g., Number of clicks on advertisements).Group the pages (logically) based on variable set in hits (e.g., User logged in/not logged in).</td></tr><tr><td>Conversion Variables</td><td>Conversion variables are persistent and hold the values for a longer period time (e.g., Number of viewed articles).</td></tr><tr><td>Events</td><td>A point on the portal in which a successful event occurs (e.g., share an article in social media).</td></tr></table>

Although clickstream data collection can provide a lot of insights into users’ behaviors, it is usually noisy, and contains a lot of unrelated information. As such, we need careful data preprocessing and cleaning steps before exploring, extracting and summarizing any useful pattern. For example, since dwell time is one of the factors which indicates user’s engagement, we are supposed to focus on articles whose time spent is high. However, a long time does not necessarily imply that a user spends more time on reading clicked articles. It is possible that a user is using a multi-tab browser and (s)he is engaging in other activities.

Table 3: Preprocessing steps on The Globe and Mail dataset.

<table><tr><td>Step</td><td>Description</td></tr><tr><td>Filtering out irrelevant hits</td><td>We only keep the hits related to articles and important events such as social activities.</td></tr><tr><td>Extracting events of interest</td><td>We extract events such as like, share, comments.</td></tr><tr><td>Computing Dwell time</td><td>Dwell time is calculated using two consecutive viewed article timestamps.</td></tr><tr><td>Roll-up from hits to a visit and a user</td><td>The aggregation is done using the user unique id, visit and page id.</td></tr><tr><td>Converting to expressive format</td><td>Each user activity record is stored as a json format to facilitate the analysis in later stages.</td></tr></table>

Therefore, we use both data aggregation and data cleaning to solve the problem in the data preprocessing phase. We first aggregate the data to user session levels. Each session represents a visit which is a set of viewed articles in the ascending order by time. Then, we filter out sessions whose time spent is longer than 30 minutes. Table 3 shows the general preprocessing steps which are done on The Globe and Mail clickstream dataset.

To calculate the dwell time per article, we use timestamps captured by the data collection platform. That is, the diference between any two consecutive page click timestamps is used to calculate the time that a user spent on an article. Similar to other studies, the last visited article in a session is ignored as we cannot estimate its dwell time. Moreover, attributes which are not required in the calculation of the proposed news utility model are filtered out. Lastly, we remove outlier visits whose time spent value deviates more than three times of the standard deviation from the average time spent for a specific article. This removes unreasonable values from the measures.

## 5.2. News Utility Model

We use a utility model to increase user engagement. However, other utility models can be plugged in as desired (e.g., See Figure 2). Given a news article nw and a user usr, since the engagement of nw is dynamic and varying from time to time, the article-driven measure of nw is calculated using recency and popularity as follows:

$$
\Psi (n w) = \frac {p o p u l a r i t y (n w)}{a c c e s s D a t e (n w) - r e l e a s e d D a t e (n w) + 1}\tag{8}
$$

where accessDate is the date that usr clicked on nw and releasedDate is the published date of nw. Note that 1 in the denominator is added to avoid zero division.

In addition, the user-driven measure $( \mathrm { e . g . } , \Upsilon ( n w , S _ { r } ) )$ of nw to usr is calculated using two user-interaction attributes: 1) DwellTime (in seconds): the time that usr spent on nw, and 2) social media activity (SocialAct): this measure represents if usr shares the article in social media and it was engaging (e.g., number of likes). The aggregation function is defined as follows:

$$
\Upsilon (n w, S _ {r}) = \log (D w e l l T i m e (u s r, n w)) \times S o c i a l A c t (u s r, n w)\tag{9}
$$

In this formula, we use log(DwellT ime(usr, nw)) since after a certain amount of time, dwell time does not necessarily represent user engagement. Lastly, the utility model is defined and calculated as follows:

$$
\varphi (n w, u s r) = \frac {\text {popularity} (n w) \times \log (\text {DwellTime} (u s r , n w)) \times \text {SocialAct} (u s r , n w)}{\text {accessDate} (n w) - \text {releasedDate} (n w) + 1}\tag{10}
$$

Note that, the only criteria on the model is that it should return positive value as the utility values. The distribution of utility values is not tied to a specific type of distribution and it depends on the design of the news utility model. Figure 6 shows the distribution of utility value of articles for the dataset used in our experiment. As the figure shows, all the values are positive and the majority are within 0 and 560. As the system is looking for maximizing the utility, the higher utility value implies that the article is more satisfactory with respect to the objective defined.

![](/api/attachments/JGQG988Z/fulltext/images/ec2ff9531a254042e6c2235784bc8fa470ed1e7206a049c9554bba1df977cc3d.jpg)  
Figure 6: The utility of articles in the dataset (shown in logarithmic scale)

## 5.3. Baseline Methods

We compare the performance of URecSYS against the following baseline systems:

• News Popularity (Pop): in this method, news articles are ranked by the DwellTime as a popularity measure. In fact, the results based on the popularity are used as a

baseline in many studies [31].

• News-to-News Collaborative Filtering (NewsKNN): this method is similar to the popular collaborative filtering method which has been commercially used by Amazon [32]. In this approach, each article is represented by a vector of users on which they have spent time. Cosine measure is utilized to measure the similarity between articles. After several test, we found 50 as the best number of number of neighbors.

• Non-negative Matrix factorization (NMF): one of the common methods in news recommendation is based on Non-negative Matrix factorization [4] where the userarticle matrix is factorized into two matrices with the property that all matrices have no negative value. Inspired by [16], we considered DwellTime to build the matrix than only clicks. Compared to traditional matrix factorization, the results of this method is interpretable and more proper for the ranking tasks in recommendation. We set the number of factors to 30 as higher values had no significant efects on the results.

• Association Rule Mining (AR-SYS): this method recommends articles using the proposed method in [33]. It considers association rules whose support and confidence are no less than some thresholds (e.g., 0.6). It recommends articles based on current visited articles by the user.

• LDA: this method is a content-based recommendation approach which uses topic modeling (e.g., LDA) for recommendation. In the method, users are considered as documents and news articles are treated as words. We use the default setting proposed by [34] to run the recommendation system.

• URecSYS<sub>B</sub>: this method is our proposed recommendation system with combined score. The main diference is that we consider only Dwelltime as the news utility model. Our purpose is to show how efective the recommendations are even when the news utility model is as simple as a single measure (e.g., DwellTime).

Lastly, we evaluate three versions of URecSYS: a) Article-level URecSYS, denoted as URecS $\mathbf { \nabla } _ { \mathbf { Y } \mathbf { S } _ { A L } }$ , recommends articles according to the article-level news recommendation score. b) Topic-level URecSYS, denoted as URecSYS<sub>T</sub> <sub>L</sub>, recommends articles based on the proposed topic-level news recommendation score, and c) Combined URecSYS, denoted URecSYS , recommends articles using the proposed combined news recommendation score.

## 5.4. Performance Metrics

In our experiments, we perform 5-fold cross validation. That is, the dataset is split randomly into five folds. In each iteration, we use four folds as the training set and the remaining fold as the test set. Eventually, all folds are tested and the average results are reported as final performance results. To measure the efectiveness of recommended articles, we use Mean Average Precision at $k \ ( i . e . , \ M A P @ K )$ , where precision is defined as the number of relevant articles divided by the total number of articles in the dataset. We set K to 1, 5, 10 respectively in our experiments. We use a validation set taken from the training set to find the optimal values for the parameters of our methods. Moreover, to evaluate how diverse the recommendation results are, URecSYS is compared to the baselines in terms of news set diversity described in [35]. The diversity is defined as the average dissimilarity of all pairs of news articles in the recommendation list. Given a set of news articles N , the average dissimilarity of N is defined as follows:

$$
A v g D i s (N) \quad = \quad \frac {2}{p (p - 1)} \sum_ {n w _ {i} \in N} \sum_ {n w _ {j} \in N \& n w _ {i} \neq n w _ {j}} (1 - S i m (n w _ {i}, n w _ {j}))\tag{11}
$$

In this formula, p is the number of news articles and the dissimilarity is defined as $1 - S i m ( n w _ { i } , n _ { j } )$ $S i m ( n w _ { i } , n w _ { j } )$ denotes the similarity of two news articles $n w _ { i }$ and $n w _ { j }$ and is calculated by cosine similarity.

We also set the utility threshold $( \mathrm { e . g . , } m i n _ { - } u t i l )$ such that the method discovers 100, 000 high utility news reading patterns, the min uconf to 0.6 and min tconf to 0.45. Later, we show the sensitivity of results to the diferent values of these parameters.

## 5.5. News Recommendation Rules in Practice

Table 4 presents top-5 article-level rules discovered by our approach and top-5 frequencybased recommendation rules (i.e., AR-SYS), which are sorted by the utility confidence and support confidence respectively.

## ACCEPTED MANUSCRIPT

Table 4: Top-5 Recommendation Rules generated by $U R e c S Y S _ { A L }$ and AR-SYS

<table><tr><td>Approach</td><td>ID.</td><td>Rule (Title of the news in the rule)</td><td>Dwell Time (mins.)</td><td>Conf.</td></tr><tr><td rowspan="5"> $URecSYS_{AL}$ </td><td> $UR_1$ </td><td>Police charge Garland with murder...→ Meet the sobriety coach hired ...</td><td>12</td><td>0.888</td></tr><tr><td> $UR_2$ </td><td>In pictures: Scenes from crash ... → MH17:Disaster ratchets up...</td><td>11.6</td><td>0.880</td></tr><tr><td> $UR_3$ </td><td>La Prairie, Quebec mayor dies ...→ MH17:Separatists hand over black...</td><td>9.9</td><td>0.839</td></tr><tr><td> $UR_4$ </td><td>MH17 Disaster ratchets up Russia-Ukraine ...→ I refused to play the Conservatives...</td><td>8.2</td><td>0.812</td></tr><tr><td> $UR_5$ </td><td>Liberals take two Toronto ridings ...→ Full by election results from Trinity-Spadina...</td><td>9.4</td><td>0.812</td></tr><tr><td rowspan="5">AR-SYS</td><td> $AR_1$ </td><td>Harper alleges Supreme Court Chief Justice ...→ Chief Justice hits back at Prime Minister...</td><td>&lt; 1</td><td>0.953</td></tr><tr><td> $AR_2$ </td><td>Body of missing Canadian Dave Walker ...→ Rob Ford takes leave as recent drug video emerge...</td><td>2</td><td>0.924</td></tr><tr><td> $AR_3$ </td><td>Our Rob Ford problem: We forgive him ...→ Assembly of First Nations national chief Shawn...</td><td>&lt; 1</td><td>0.897</td></tr><tr><td> $AR_4$ </td><td>Toronto&#x27;s scandal mayor: World media ...→ The end of the line for Toronto&#x27;s rogue mayor...</td><td>3</td><td>0.891</td></tr><tr><td> $AR_5$ </td><td>Ontario election expected to be close race between Grits ...→ Ontario&#x27;s deficit includes the politicians...</td><td>&lt; 1</td><td>0.882</td></tr></table>

Table 4 suggests that the rules with high support do not necessarily recommend articles that increases user engagement when we use dwell time as the measure of engagement. This is due to the fact that there are rules discovered from news reading patterns whose frequency is low $( \mathrm { e . g . , } U R _ { 1 }$ and $U R _ { 2 } )$

Figure 7 shows sum of the browsing time of two groups of recommendation rules. In this figure, the $\ " _ { \mathrm { X } } \ " $ axis refers to the top-k rules $( \mathrm { e . g . }$ , article-level rules and frequency-based rules) and the $^ { \mathfrak { n } } \mathbf { y } ^ { \mathfrak { n } }$ axis shows sum of the time spent based on the top-k recommendation rules. The results reveal that the rules discovered by $U R e c S Y S _ { A L }$ may lead users to spend more time as the recommended articles are of the user’s interests.

![](/api/attachments/JGQG988Z/fulltext/images/7e5beef30f224210d5b04e179b154a3fa2e227265b770f02ca7d183fef3fbdca.jpg)  
Figure 7: Average browsing time using diferent sets of recommendation rules  
Figure 8 illustrates the top-5 topic-level recommendation rules obtained from the dataset.

# ACCEPTED MANUSCRIPT

In this figure, each topic is represented by its top-4 words. The percentage on each relationship arrow shows the rule confidence. To validate the rules, we check if the top-5 rules discovered by our framework were truly associated in real life scenarios. We examine the association among topics by searching for the news articles using top-4 words from the topics as search keywords on the news portal. Since we use the data from 2014 to 2015 in the above experiments, we only consider news articles published within this time period. From the top-5 topic-level rules, we found that most of the times the rules found by our framework have very close associations in reality during the same period of time. For example, given topic $t _ { 1 } = \{ F i r e$ , P eople, Area, Emergency}, $t _ { 2 } = \{ R u s s i a . $ , U kraine, P utin, Moscow}, according to the rule in Figure 8, 67% of users who read news articles on $t _ { 1 }$ also read news articles on $t _ { 2 }$ . We found that in late 2014, two of the most associated topics were based on the conflicts between Russia and Ukraine in one hand, and Russia helping Syria government against ISIS on the other hand. The other rules revealed real world news stories in 2014 as well.

![](/api/attachments/JGQG988Z/fulltext/images/a2374667af866f69c2b5925ba4b67b4d02f6714cc0e5ea17e4f560a55ec38040.jpg)  
Figure 8: Top-5 Topic-level Recommendation Rules discovered by $U R e c S Y S _ { T L }$

We conducted a user study to evaluate the interestingness of the top-5 article-level recommendation rules. We gave these rules to 10 undergraduate and graduate students, along with top-4 ranked keywords per topic. We asked them to judge the quality of the top-5 rules by first searching the top-4 ranked keywords in the newspaper and then giving a score between zero and one to rate each rule based on how strong they think the topics (in antecedent and consequent) in a rule are related and interesting. Table 5 shows the average results in percentage. The results show that the proposed framework for topic-level rule discovery ranks the rules very close to the ranking obtained from the survey participants.

Table 5: The average precision of top-5 topic-level recommendation rules

<table><tr><td>Topic-level rules</td><td>Possible Response Range</td><td>Actual Response Range</td><td>User Judge Mean(SD)</td><td>tconf(%)</td></tr><tr><td>Fire, People, Area, Emergency → Russia, Ukraine, Moscow, Putin</td><td>0 - 100</td><td>60 - 100</td><td>78 (15)</td><td>67</td></tr><tr><td>Air, Airport, Flight, Aircraft → Russia, Ukraine, Moscow, Putin</td><td>0 - 100</td><td>50 - 100</td><td>64 (11)</td><td>66</td></tr><tr><td>Info., Data, Security, Privacy → Russia, Ukraine, Moscow, Putin</td><td>0 - 100</td><td>40 - 100</td><td>73 (21)</td><td>55</td></tr><tr><td>Board, Executive, Chief, President → Court, Legal, Law, Judge</td><td>0 - 100</td><td>40 - 100</td><td>67 (18)</td><td>52</td></tr><tr><td>Drug, People, Health, Disease → City, Ford, Mayor, Toronto</td><td>0 - 100</td><td>50 - 100</td><td>71 (21)</td><td>49</td></tr></table>

## 5.6. Experimental Results on Recommendations

Figure 9 shows the results of MAP@K for diferent recommendation systems. In this figure, ”x” axis stands for diferent values of K and ”y” axis stands for the MAP@K value obtained by each recommendation system. As the figure shows, $U R e c S Y S _ { A L }$ outperforms all the methods on diferent values of K. The results provide the following observations: 1) Although $U R e c S Y S _ { B }$ does not consider all the measures, it still works better than the baselines as it considers both topics-level and article-level rules and associations among articles based on the utility model. 2) $U R e c S Y S _ { A L }$ and $U R e c S Y S _ { C }$ outperform other approaches, which demonstrates the superiority of our news utility model for news recommendation. 3) The performance gap between $U R e c S Y S _ { T L }$ and the AR-SYS is significant, which reveals that topic-level recommendation rules are more suitable for recommendations.

![](/api/attachments/JGQG988Z/fulltext/images/a3cfa4b827a5aac976257d8ae0cac6208c2cdaa0adae60ac4fd17e4c6ce3c66a.jpg)  
Figure 9: Mean Average Precision @K for the diferent recommender systems

Table 6 shows the average diversity results for diferent methods. It can be observed that, the diversity decreases as the number of recommended articles increases. This is due to the fact that when more articles are selected, the recommendation articles are getting closer to the user’s interest and the recommended articles become more similar. URecSYS outperforms the other methods significantly and the diversity of its results decreases smoothly when the number of the recommended articles increases.

Table 6: Diversity evaluation on the result list

<table><tr><td>Methods</td><td>Top@5</td><td>Top@10</td><td>Top@15</td></tr><tr><td>Pop</td><td>0.541</td><td>0.438</td><td>0.360</td></tr><tr><td>NewsKNN</td><td>0.417</td><td>0.382</td><td>0.324</td></tr><tr><td>NMF</td><td>0.571</td><td>0.512</td><td>0.460</td></tr><tr><td>AR-SYS</td><td>0.381</td><td>0.319</td><td>0.284</td></tr><tr><td>LDA</td><td>0.507</td><td>0.472</td><td>0.312</td></tr><tr><td> $URecSYS_C$ </td><td>0.712</td><td>0.683</td><td>0.6552</td></tr></table>

To simulate the news cold-start scenario, similar to [36], we divide the articles into two training and testing subsets. Since the number of articles published per day is large, we use 40% of the articles for training and 40% of articles for testing and 20% of articles in both training and testing. We compare our framework to the alternative recommendation methods on the dataset. In the scenarios of news cold-start, since there is no visits on news articles, most of the approaches do not work. Figure 10 shows the average performance of each method across the dataset to the news cold-start scenario. In terms of MAP@K, $U R e c S Y S _ { T L }$ outperforms all other approaches. The main reason is that this approach not only contains the relations among the topics based on user’s interests, it can also recommend newly-published articles. In Figure 10, URecSY S<sub>C</sub> outperforms $U R e c S Y S _ { A L }$ since its score is leveraged by the score obtained by $U R e c S Y S _ { T L }$

![](/api/attachments/JGQG988Z/fulltext/images/d3cf0f57a73ef5fc4a0fe631439213da4c4b62d9e383d48891f4fc7be152baff.jpg)  
Figure 10: MAP@K for the diferent systems on the dataset with the news cold-start problem

We also evaluate the performance of $U R e c S Y S _ { A L }$ and $U R e c S Y S _ { T L }$ by varying min uconf and min tconf. Figures 11 (a), (b) show the sensitivity of the results with respect to diferent values min uconf and min tconf. The lower value of the min uconf and min tconf leads to a larger number of recommendation rules. Such added rules are not necessarily better rules as their confidence is lower. In general, lower values of the parameters decrease the performance of the recommendation systems in terms of the precision. This change is less significant for $U R e c S Y S _ { T L }$ as the rules are generalized to topic level.

![](/api/attachments/JGQG988Z/fulltext/images/758ff369bf62f9092aef346140971c94af60b263bf2590c77d6a93acf6035a5b.jpg)  
(a)

![](/api/attachments/JGQG988Z/fulltext/images/bf2cf5c302d79b2afd5ac11aebef30373786c2c10011bdc38a47fb6451dd8b46.jpg)  
(b)  
Figure 11: (a) $U R e c S Y S _ { A L }$ performance on diferent values of min uconf, (b) $U R e c S Y S _ { T L }$ performance on diferent values of min tconf

## 5.7. Discussions and Implications

The literature in news recommendation systems indicates that having a model (e.g., the proposed news utility model) that can represent a domain specific objective is essential for recommendation. Given the model, the main challenge is how to efectively incorporate it during the recommendation process. Our experiments verify that our proposed utility model and its incorporation into the recommendation process improved the performance of the recommendation with respect to the objective defined.

The first implication in our experiment was the fact that applying the news utility model during article-level rule discovery, results in finding domain specific rules and therefore, recommended articles increase user experience quality with respect to the objective. The comparison against rules discovered by other methods verified that the results were promising and satisfactory. Moreover, in the topic-level, we observe that efective semantic connections among topics are built by using the utility model and the article-level rules. Therefore, we addressed the cold start problems efectively as we use the domain specific objective as well as the semantic connections during recommendations. Our experiments show that the article-level rules have better performance in the absent of cold start problem. This is due to the level of details that such rules represent. However, when there is news cold start (which is very common), the topic-level rules are of importance for having an efective recommendation system.

Analyzing two billion records in experiments verified the scalability of the proposed framework. We noticed that with the current dataset size, some baselines could not even finish

# ACCEPTED MANUSCRIPT

the learning process due to the exponential growth of search space and we needed to adjust the parameters to get results. However, taking advantage of the Apache Spark technology and the MapReduce framework improved the performance of the system significantly.

## 6. Conclusions, Limitations and Future Work

In the news recommendation context, the most challenging problem for any online news publisher is to make a balance between diferent business objectives (e.g., increasing user engagement through free content delivery in one hand and revenue maximization through subscription on the other hand). Such objectives are usually in contention with one another. Moreover, most existing news recommendation systems only consider the click (e.g., CTR) as an implicit feedback, which is quite problematic as a user might click on an article in which she/he is not interested in. To address these challenges, we designed a news utility model that represents business objectives by simultaneously considering both article-related and user-article interaction attributes. We showed that this model is more beneficial to recommend news articles compared to existing approaches. In addition, we argued that building a news recommendation system that can handle big data requires applying scalable techniques and platforms [3]. Moreover, despite the availability of such huge volume of historical data, most interactions belong to un-subscribed users (i.e., unknown visitors). Therefore, we proposed a novel and scalable rule engine to discover article-level recommendation rules based on the news utility model. At its heart, the rule engine uses multiple MapReduce-like steps to discover article-level recommendation rules in parallel. We also proposed a novel probabilistic approach on top of a well-known topic model (i.e., Latent Dirichlet Allocation) [37] to generalize article-level news recommendation rules. The output is a topic-level recommendation rule engine that links topics of articles based on the news utility model, thus business objectives. Such rules recommend newly-published articles based on topics of interests to a user, thus addressed the news cold start problem efectively. Lastly, we conducted extensive experiments on a dataset of two billion records collected from a major Canadian news agency (The Globe and Mail ) and showed the efectiveness of the proposed recommendation system by comparing to state-of-the-art recommendation systems in practice.

In the future, we plan to study how to further improve the recommendation quality through the use of more rigorous utility models to better measure a business objective.

# ACCEPTED MANUSCRIPT

Moreover, our proposed utility model presents an efective mapping from attributes to a model with respect to a domain specific objective, however, there are objectives that all the mapping details (e.g., aggregation functions) are not available. Particularly, when the objective is not as popular as user engagement. For such objectives, experts are required to design the model. This can be addressed by data driven modeling approaches and build an end-to-end solution to design the model automatically. In future, we investigate how data driven approaches can be applied to address this limitation.

This research sheds new light on the usage of the utility model in the user modeling, which can be consumed in more application scenarios. Note that the proposed utility model provides a general platform so that diferent utility models can be plugged in as desired. We plan to investigate the applicability of the proposed framework to other similar domain such as recommending research papers published in open access portals to users. The number of research paper published is exponentially growing $( \mathrm { e . g . }$ , cold start problems) and a user (e.g., researcher) cannot keep the pace to find the most recent but essential work to his/her research interests and he/she needs to choose papers from the huge quantity of potential candidates. Our aim is to show the efectiveness of the proposed utility model and the recommendation system to efectively address challenges in this domain.

## Acknowledgment

We would like to thank The Globe and Mail for providing the dataset used in this work and for their collaboration and suggestions in our joint project.

## References

[1] K. Xie, Y. Wu, J. Xiao, Q. Hu, Value co-creation between firms and customers: The role of big data-based cooperative assets, Information and Management 53 (2016) 1034 – 1048.

[2] H. Davoudi, M. Zihayat, A. An, Time-aware subscription prediction model for user acquisition in digital news media, in: Proceedings of the SDM’2017, 2017, pp. 135–143.

[3] R. Agarwal, V. Dhar, Big data, data science, and analytics: The opportunity and challenge for is research, 2014.

[4] D. D. Lee, H. S. Seung, Algorithms for non-negative matrix factorization, in: Advances in neural information processing systems, 2001, pp. 556–562.

[5] J. He, H. Liu, H. Xiong, Socotraveler: Travel-package recommendations leveraging social influence of diferent relationship types, Information and Management 53 (2016) 934 – 950.

[6] R. Mishra, P. Kumar, B. Bhasker, A web recommendation system considering sequential information, Decision Support Systems 75 (2015) 1–10.

[7] T. C.-K. Huang, Y.-L. Chen, M.-C. Chen, A novel recommendation model with google similarity, Decision Support Systems 89 (2016) 17–27.

[8] S. J. Russell, P. Norvig, Artificial intelligence: a modern approach, Malaysia; Pearson Education Limited,, 2016.

[9] F. W. Taussig, Principles of economics, volume 2, Cosimo, Inc., 2013.

[10] P. Lops, M. De Gemmis, G. Semeraro, Content-based recommender systems: State of the art and trends, in: Recommender systems handbook, Springer, 2011, pp. 73–105.

[11] J. Liu, C. Wu, W. Liu, Bayesian probabilistic matrix factorization with social relations and item contents for recommendation, Decision Support Systems 55 (2013) 838–850.

[12] X. Su, T. M. Khoshgoftaar, A survey of collaborative filtering techniques, Advances in artificial intelligence 2009 (2009) 4.

S. Rajaram, Google news personalization: scalable online

[14] G. Shani, D. Heckerman, R. I. Brafman, An mdp-based recommender system, Journal of Machine Learning Research 6 (2005) 1265–1295.

[15] F. Garcin, B. Faltings, O. Donatsch, A. Alazzawi, C. Bruttin, A. Huber, Ofline and online evaluation of news recommender systems at swissinfo. ch, in: Proceedings of the 8th ACM RecSYS, ACM, 2014, pp. 169–176.

[16] X. Yi, L. Hong, E. Zhong, N. N. Liu, S. Rajan, Beyond clicks: Dwell time for personalization, in: Proceedings of RecSys ’14, ACM, 2014, pp. 113–120.

[17] H.-N. Kim, A. El-Saddik, G.-S. Jo, Collaborative error-reflected models for cold-start recommender systems, Decision Support Systems 51 (2011) 519–531.

[18] H. Liang, Y. Xu, D. Tjondronegoro, P. Christen, Time-aware topic recommendation based on micro-blogs, in: Proceedings of the 21st ACM international conference on Information and knowledge management, ACM, 2012, pp. 1657–1661.

[19] D. Agarwal, B.-C. Chen, R. Gupta, J. Hartman, Q. He, A. Iyer, S. Kolar, Y. Ma, P. Shivaswamy, A. Singh, L. Zhang, Activity ranking in linkedin feed, in: Proceedings of the 20th ACM SIGKDD, ACM, 2014, pp. 1603–1612.

[20] Y.-M. Li, C.-T. Wu, C.-Y. Lai, A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems 55 (2013) 740–752.

[21] L. Li, T. Li, News recommendation via hypergraph learning: encapsulation of user behavior and news content, in: Proceedings of the sixth ACM WSDM, ACM, 2013, pp. 305–314.

[22] E. Zhong, N. Liu, Y. Shi, S. Rajan, Building discriminative user profiles for large-scale content recommendation, in: Proceedings of the 21th ACM SIGKDD, ACM, 2015, pp. 2277–2286.

[23] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online recommendation system: A novel associative classification model, Decision Support Systems 48 (2010) 470–479.

[24] Z. Li, X. Fang, X. Bai, O. R. L. Sheng, Utility-based link recommendation for online social networks, Management Science 63 (2016) 1938–1952.

[25] M. Scholz, V. Dorner, M. Franz, O. Hinz, Measuring consumers’ willingness to pay with utility-based recommendation systems, Decision Support Systems 72 (2015) 60–71.

[26] G. Chandrashekar, F. Sahin, A survey on feature selection methods, Computers & Electrical Engineering 40 (2014) 16–28.

[27] M. Tavakolifard, J. A. Gulla, K. C. Almeroth, J. E. Ingvaldesn, G. Nygreen, E. Berg, Tailored news in the palm of your hand: A multi-perspective transparent approach to news recommendation, in: Proceedings of WWW ’13, 2013, pp. 305–308.

[28] V. Karnowski, A. S. Kmpel, L. Leonhard, D. J. Leiner, From incidental news exposure to news engagement. how perceptions of the news post and news usage patterns influence engagement with news articles encountered on facebook, Computers in Behavior 76 (2017) 42 – 50.

[29] D.-R. Liu, C.-H. Lai, W.-J. Lee, A hybrid of sequential rules and collaborative filtering for product recommendation, Information Sciences 179 (2009) 3505 – 3519.

[30] M. Zihayat, Z. Z. Hu, A. An, Y. Hu, Distributed and parallel high utility sequential pattern mining, in: IEEE International Conference on Big Data, 2016, pp. 853–862.

[31] X. He, T. Chen, M.-Y. Kan, , X. Chen, Trirank: Reviewaware explainable recommendation by modeling aspects, in: Proceedings of CIKM, ACM, New York, NY, USA, 2015, pp. 1661–1670.

[32] B. N. Miller, I. Albert, S. K. Lam, J. A. Konstan, J. Riedl, Movielens unplugged: experiences with an occasionally connected recommender system, in: Proceedings of ACM IUI, ACM, 2003, pp. 263–266.

[33] C. Kim, J. Kim, A recommendation algorithm using multi-level association rules, in: Proceeding of WI 2003, 2003, pp. 524–527.

[34] G. Guo, J. Zhang, Z. Sun, N. Yorke-Smith, Librec: A java library for recommender systems., in: UMAP Workshops, 2015.

[35] M. Zhang, N. Hurley, Avoiding monotony: improving the diversity of recommendation lists, in: Proceedings of the 2008 ACM conference on Recommender systems, ACM, 2008, pp. 123–130.

[36] I. Barjasteh, R. Forsati, F. Masrour, A.-H. Esfahanian, H. Radha, Cold-start item and user recommendation with decoupled completion and transduction, in: Proceedings of RecSYS, ACM, 2015, pp. 91–98.

[37] D. M. Blei, A. Y. Ng, M. I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022.

## Appendix

Theorem 1 proof. Let set $X _ { t } = X - n w _ { k - t }$ that is $X _ { t }$ has all articles from X excludes article $n w _ { k - t }$ . For example, $X _ { 1 } = \{ n w _ { 1 } , n w _ { 2 } , \dots , n w _ { k - 2 } , n w _ { k } \}$ . Since $1 \leq t < k$ , we know that $\sigma ( n w _ { k - t } , P ) < \sigma ( n w _ { k } , P )$ , thus: $\sum _ { j = 1 } ^ { \kappa - 1 } \sigma ( n w _ { j } , P ) + \sigma ( n w _ { k - t } , P ) < \sum _ { j = 1 } ^ { \kappa - 1 } \sigma ( n w _ { j } , P ) + \sigma ( n w _ { k } , P )$ Then, $, \sum _ { j = 1 } ^ { k - 1 } \sigma ( n w _ { j } , P ) < \sum _ { j = 1 } ^ { k - 1 } \sigma ( n w _ { j } , P ) - \sigma ( n w _ { k - t } , P ) + \sigma ( n w _ { k } , P )$ . In the above inequality, the left side is $X _ { 0 }$ and the right side is $X _ { 1 }$ , so we have $\sigma ( X _ { 0 } , P ) < \sigma ( X _ { 1 } , P )$ . Given $\sigma ( n w _ { i } , P )$ 2 we have $\begin{array} { r } { \frac { \sigma ( n w _ { i } , P ) } { \sigma ( X _ { 0 } , P ) } > \frac { \sigma ( n w _ { i } , P ) } { \sigma ( X _ { 1 } , P ) } } \end{array}$ . Since $\frac { \sigma ( n w _ { i } , P ) } { \sigma ( X _ { 0 } , P ) }$ yields the uconf of a rule $ \{ X - n w _ { k } \}  n w _ { i } $ , the proof is complete.

# ACCEPTED MANUSCRIPT

## Highlights

 The news utility model goes beyond click through rate analysis for recommendations

 The system is designed based on MapReduce to analyze huge volume of data in parallel

 News Cold Start Problem has been addressed by a novel probabilistic approach

 Experiments on 2 billion records demonstrate the effectiveness of the system

<table><tr><td>Session ID</td><td> $\langle news, ID, \{SocialAct, DwellTime\}$ </td></tr><tr><td>S1</td><td> $\langle nw_1, \{2,14\}\rangle\langle nw_3, \{1,3\}\rangle\langle nw_5, \{2,22\}\rangle\langle nw_6, \{2,7\}\rangle$ </td></tr><tr><td>S2</td><td> $\langle nw_4, \{0.2,4\}\rangle\langle nw_5, \{2,15\}\rangle\langle nw_6, \{2,18\}\rangle$ </td></tr><tr><td>S3</td><td> $\langle nw_2, \{2,14\}\rangle\langle nw_4, \{0.1,4\}\rangle\langle nw_5, \{1,19\}\rangle\langle nw_6, \{1,3\}\rangle$ </td></tr><tr><td>S4</td><td> $\langle nw_1, \{1,4\}\rangle\langle nw_3, \{1,8\}\rangle\langle nw_5, \{0.6,13\}\rangle$ </td></tr><tr><td>S5</td><td> $\langle nw_4, \{1,9\}\rangle\langle nw_5, \{1,2\}\rangle$ </td></tr><tr><td colspan="2"> $Y(nw_i, S_r) = \log(DwellTime (nw_i, S_r) \times SocialAct (nw_i, S_r))$ </td></tr><tr><td>Session ID</td><td> $\langle news, Y(news)\rangle$ </td></tr><tr><td>S1</td><td> $\langle nw_1, 2.3\rangle\langle nw_3, 0.5\rangle\langle nw_5, 2.7\rangle\langle nw_6, 1.7\rangle$ </td></tr><tr><td>S2</td><td> $\langle nw_4, 0.12\rangle\langle nw_5, 2.3\rangle\langle nw_6, 2.5\rangle$ </td></tr><tr><td>S3</td><td> $\langle nw_2, 2.3\rangle\langle nw_4, 0.06\rangle\langle nw_5, 1.3\rangle\langle nw_6, 0.5\rangle$ </td></tr><tr><td>S4</td><td> $\langle nw_1, 0.6\rangle\langle nw_3, 0.9\rangle\langle nw_5, 0.7\rangle$ </td></tr><tr><td>S5</td><td> $\langle nw_4, 0.9\rangle\langle nw_5, 0.3\rangle$ </td></tr></table>

![](/api/attachments/JGQG988Z/fulltext/images/d9cbb8951464129163a11a4f939087ad251cba5679d2b9f6a28538eedfc4b7b4.jpg)  
Figure 2

![](/api/attachments/JGQG988Z/fulltext/images/0694a03e2ab1878d420214afa9e852f1dac9dfbc8dd93ebea118e35ecd317f15.jpg)  
Figure 3

![](/api/attachments/JGQG988Z/fulltext/images/7cf1b001da00cf8f5994d7ab8bed5b6c9da4f7e55ea0582a19989bad757e9de3.jpg)  
Figure 4

![](/api/attachments/JGQG988Z/fulltext/images/de17fa01b0d062095d1822699edced45f066ac25d73ef996f372e44465bc67ab.jpg)  
Figure 5

![](/api/attachments/JGQG988Z/fulltext/images/b28776bc9cb2b9055f793164300105b1a1e49402eb4ef2b19ef1549a370e7b75.jpg)  
Figure 6

![](/api/attachments/JGQG988Z/fulltext/images/19ec2a2b3ecf55e569cb0cc81bbdf15e1be71f5b9395e8d2804bee48cb1ce9e9.jpg)  
Figure 7

![](/api/attachments/JGQG988Z/fulltext/images/9c421dfb862f8b7aad73a00695ec8e121529d6ce899d5f71d1b8d1a2821e11e2.jpg)

![](/api/attachments/JGQG988Z/fulltext/images/d63a1c67ae9f56f6c9e17acc8ca47f435f96cddb6026c73353da357f5617efd0.jpg)  
Figure 9

![](/api/attachments/JGQG988Z/fulltext/images/8d6f766a9d2dc31e45c4568019c248bfa05c86cccac4ace978bd51e6488e91f2.jpg)  
Figure 10

![](/api/attachments/JGQG988Z/fulltext/images/06b619e927bf56ead79d4738a8549615c99de381214dc796258897355b18e968.jpg)  
(a)

![](/api/attachments/JGQG988Z/fulltext/images/2dc1e0e07ea5f6a3afb74f0deb474b3e3e6cb8920e23c179e4a9097110392b2a.jpg)  
(b)  
Figure 11
