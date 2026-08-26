---
otero_id: 16010
otero_key: "5QZ34VQY"
title: "Collaborative user modeling for enhanced content filtering in recommender systems"
authors: "Heung-Nam Kim; Inay Ha; Kee-Sung Lee; Geun-Sik Jo; Abdulmotaleb El-Saddik"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Collaborative user modeling for enhanced content <sup>fi</sup>ltering in recommender systems

Heung-Nam Kim <sup>a,</sup>⁎, Inay Ha <sup>b</sup>, Kee-Sung Lee <sup>b</sup>, Geun-Sik Jo <sup>b</sup>, Abdulmotaleb El-Saddik <sup>a</sup>

<sup>a</sup> School of Information Technology and Engineering, University of Ottawa, 800 King Edward, Ottawa, Ontario, K1N 6N5, Canada

<sup>b</sup> School of Computer and Information Engineering, Inha University, 253 Younghyun-dong, Nam-gu, Incheon (402–751), Korea

a r t i c l e i n f o

Available online 31 January 2011

Keywords: Collaborative user modeling Recommender system Personalization Content-based user model

## a b s t r a c t

Recommender systems, which have emerged in response to the problem of information overload, provide users with recommendations of content suited to their needs. To provide proper recommendations to users, personalized recommender systems require accurate user models of characteristics, preferences and needs. In this study, we propose a collaborative approach to user modeling for enhancing personalized recommendations to users. Our approach <sup>fi</sup>rst discovers useful and meaningful user patterns, and then enriches the personal model with collaboration from other similar users. In order to evaluate the performance of our approach, we compare experimental results with those of a probabilistic learning model, a user model based on collaborative <sup>fi</sup>ltering approaches, and a vector space model. We present experimental results that show how our model performs better than existing alternatives.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The prevalence of Web 2.0 technologies and services enables endusers to be producers as well as consumers of content. Even on a daily basis, an enormous amount of textual content, such as online news, research papers, blog articles, and wikis is generated on the Web. It is getting more dif<sup>fi</sup>cult to make automatic recommendations to a user related to his/her preferences, not only because of the huge amount of information but also because of the dif<sup>fi</sup>culty of automatically grasping his/her interests [7]. Recommender systems, which have emerged in response to the above challenges, provide users with recommendations of content suited to their needs. There are two widely used approaches among recommender systems, content-based <sup>fi</sup>ltering and collaborative <sup>fi</sup>ltering. The traditional task in collaborative <sup>fi</sup>ltering is to predict the utility of a certain item for the target user from the opinions of other similar users, and thereby make appropriate recommendations [21]. On the other hand, content-based <sup>fi</sup>ltering provides recommendations by comparing representations of content contained in an item to those of a user's interest content, ignoring opinions of other similar users [17]. Collaborative <sup>fi</sup>ltering has an advantage over content-based <sup>fi</sup>ltering in situations where it is hard to analyze the underlying content, e.g., music, videos, and photos. Because collaborative <sup>fi</sup>ltering process is only based on historical information about whether or not a given target user has previously preferred an item, analysis of the actual content, itself, is not necessarily required.

Nevertheless, collaborative <sup>fi</sup>ltering suffers from a fundamental problem, namely the cold start problem, which can be divided into cold start items and cold start users [25]. Several researchers have offered proposals dealing with the challenge of addressing this problem [10,17,22,25]. In a collaborative <sup>fi</sup>ltering-based recommender system, an item cannot be recommended until a large number of users have previously rated it. This is known as a cold start item. This problem applies to new items generated every few minutes and can be partially alleviated by content-based technology. In the case of domains such as textual documents, content-based <sup>fi</sup>ltering has proven to be effective in locating textual content relevant to a speci<sup>fi</sup>c content information need [6,10]. However, content-based <sup>fi</sup>ltering also encounters limitations for a cold start user, similar to collaborative <sup>fi</sup>ltering. A cold start user describes a new user that joins a recommender system and has presented few opinions (i.e., the user has insuf<sup>fi</sup>cient preference history). With these situations, the system is generally unable to make high quality recommendations.

We address these issues by introducing a collaborative approach to user modeling for enhancing content <sup>fi</sup>ltering. Our goal is to build a robust user model that can be applied to personalized recommender systems. By capturing a user's content of interest, we can discover the preference patterns and terms existing in the user's content of interest. In addition to partially overcome the cold start user problem, we propose an enrichment method of the personal model in collaboration with other similar users.

This paper presents three speci<sup>fi</sup>c contributions toward user modeling in recommender systems. First, we propose a new method of building a user model, allowing understanding and <sup>fi</sup>ltering of the user's interests. We then present a method of a collaborative enrichment of user interests in dealing with the cold start problem. Second, we propose how the individual model can be applied to personalized recommendations relevant to the user's needs. We incorporate collaborative characteristics into a content-based approach. Third, we provide detailed experimental evaluations with real datasets and investigate how collaborative user models work in terms of improving the recommendation performance.

The subsequent sections are organized as follows: Section 2 summarizes previous studies related to user modeling and personalized recommendations. In Section 3, we describe the notations and method to build the initial user model. We then describe a collaborative approach for modeling user interests and recommending content in Section 4. Next, Section 5 describes the implemented system and interface. In Section 6, we present the effectiveness of our approach in terms of its performance. Finally, conclusions are presented and future work is discussed in Section 7.

## 2. Related work

In personalized recommender systems, two main approaches have been developed: a content-based <sup>fi</sup>ltering approach and a collaborative <sup>fi</sup>ltering approach. Following the proposal of GroupLens [21], the <sup>fi</sup>rst system to generate automated recommendations, collaborative <sup>fi</sup>ltering approaches have seen the widest use in a large number of information <sup>fi</sup>ltering problems relating to such things as movies, books, music, online news, TV programs, and research papers. Despite success and popularity, collaborative <sup>fi</sup>ltering encounters several limitations, including the sparsity of the data, scalability, the cold start problem, and untrustworthy users. A number of researchers have addressed these problems using content-based <sup>fi</sup>ltering [4].

Content-based <sup>fi</sup>ltering methods, which are another well-known technique in recommender systems, have been developed using learning procedures. These procedures require training data to identify personal preferences (user model) from information objects and their content. Webmate tracked documents of interest to the user and exploited the vector space model using the TF-IDF (Term Frequency– Inverse Document Frequency) method [6]. Schwab et al. [26] explored the use of a classi<sup>fi</sup>cation approach to recommend articles relevant to the user pro<sup>fi</sup>le, such as NewsDude. In NewsDude, two types of user interests are used: short-term and long-term interests. To avoid recommendations of very similar documents, a short-term pro<sup>fi</sup>le is used. For the long-term interests of a user, the probabilities of a document are calculated using Naïve Bayes approach to classify a document as interesting or not. Instead of learning from users' explicit information, PVA [5] learned a user pro<sup>fi</sup>le implicitly without user intervention. The user pro<sup>fi</sup>le is represented as a keyword vector in the form of a hierarchical category structure. In Newsjunkie [11], a noveltyanalysis algorithm is employed to present novel information for users by identifying the novelty of articles in the contexts of articles they previously reviewed. Lihua et al. [14] proposed a method of modeling multiple user interests by using a self-organizing map neural network with a changeable network structure. SiteIF [15] proposed using word sense-based document representation to build a model of the user's interests. A <sup>fi</sup>ltering procedure was employed to dynamically predict new documents based on a semantic network.

After mining user u's content of interest, <sup>fi</sup>ve personalized term patterns are found.

<table><tr><td>Pattern-id</td><td>PTP</td><td>PS</td><td>Length</td></tr><tr><td> $p_1$ </td><td> $\{t_1, t_2, t_3\}$ </td><td>0.56</td><td>3</td></tr><tr><td> $p_2$ </td><td> $\{t_1, t_2, t_3, t_4\}$ </td><td>0.51</td><td>4</td></tr><tr><td> $p_3$ </td><td> $\{t_1, t_2, t_5\}$ </td><td>0.47</td><td>3</td></tr><tr><td> $p_4$ </td><td> $\{t_4, t_5\}$ </td><td>0.41</td><td>2</td></tr><tr><td> $p_5$ </td><td> $\{t_2, t_3, t_4\}$ </td><td>0.32</td><td>3</td></tr></table>

Collaborative and content-based <sup>fi</sup>ltering methods have unique advantages and disadvantages. Therefore, some studies combine these techniques in developing hybrid recommender systems [4]. Berkovsky et al. [22] presented a method of user modeling data integration for the purposes of a speci<sup>fi</sup>c recommendation task, referred to as the mediation of a user model. By importing and integrating data collected from other recommender systems, four types of user model mediation are presented: cross-user, cross-item, cross-context, and cross-representation. In [3], the same authors presented mediated user models that are transformed from collaborative <sup>fi</sup>ltering to content-based recommender systems. In [8], a content-collaborative hybrid recommender system is proposed that exploits WordNet-based user pro<sup>fi</sup>les to capture the semantics of user interests. Similar to our approach, the authors generated the neighborhood of a user through content-based methods. Melville et al. [17] followed a two-stage approach. First they applied a naive Bayesian classi<sup>fi</sup>er as content-based predictor to complete the rating matrix, and then they re-estimated ratings from this full rating matrix by collaborative <sup>fi</sup>ltering. CinemaScreen [22] reversed the stages. It executed content-based <sup>fi</sup>ltering on a result set generated through collaborative <sup>fi</sup>ltering.

Although the above-mentioned studies combine collaborative and content-based <sup>fi</sup>ltering approaches to exploit the bene<sup>fi</sup>ts of each and lessen the disadvantages, our approach takes a different stance. Differing from earlier work, we automatically identify meaningful or useful patterns in building a user model. In addition, rather than utilizing explicit user feedback such as numeric ratings assigned to content, our aim is to build a robust user model implicitly inferred by the system from observing user behavior. Through the identi<sup>fi</sup>cation of useful patterns of a user in collaboration with other similar users, we discover content relevant to the user's needs.

## 3. Building a personal user model

The capability to learn users' preferences is at the heart of a personalized recommender system. In order to provide proper recommendations to users, personalized recommender systems require user models of characteristics, preferences, and needs. This information is typically referred to in the literature as a User Model (UM) [3]. Additionally, since every user can have different interests, feature selection for representing users' interests should be personalized and performed individually for each user [16]. In this section, we describe our approach to building a personal user model that is driven by the user's content of interest.

Before going into further detail, the notation and de<sup>fi</sup>nitions required for understanding our approach are introduced. Let C = $\{ c _ { 1 } , c _ { 2 } , . . . , c _ { n } \}$ be the set of all content, $T = \{ t _ { 1 } , t _ { 2 } , . . . , t _ { m } \}$ be the set of all index terms, and $U { = } \{ u _ { 1 } , u _ { 2 } , . . . , u _ { l } \}$ be the set of distinct users. The content $c _ { j }$ is a set of terms, each of which may appear in multiple content with different weights that quantify the importance of the term for describing the content. In our study, a weight $w _ { i , j }$ associated with a pair $( t _ { i } , c _ { j } )$ (i.e., a term t of a content c ) is computed by a fairly common type of TF-IDF weighting scheme [23]. To build a personal user model, potentially representative of user interests, we initially need some information given by the user, called user feedback. The most common ways to obtain the feedback is to use information given explicitly or to get information observed implicitly from the user's interaction [19]. Explicit feedback requires a user to evaluate content and indicate how relevant or interesting speci<sup>fi</sup>c content is to him/her using like/dislike (a binary scale) or numerical ratings. Even though explicit feedback helps us to capture user preferences accurately, there is a serious drawback in that users do not tend to provide enough feedback. Users are generally not motivated to provide their feedback if they do not receive immediate bene<sup>fi</sup>ts, even when they would pro<sup>fi</sup>t in the long-term [19]. Therefore, in our study, we take implicit feedback into consideration in the sense that the system automatically infers the user's preferences from the user's behaviors [2,7,19]. In general, the preference indicator of implicit feedback can be represented as a form of a co-occurrence pair $( u _ { h } , c _ { j } )$ where $u _ { h } { \in } U$ is a user and $c _ { j } \in C$ is speci<sup>fi</sup>c content. The co-occurrence pair implies that user $u _ { h }$ viewed, clicked, collected, or bookmarked content $c _ { j } .$ While implicit feedback on speci<sup>fi</sup>c content by a user does not necessarily mean that he/she likes the content, we assume that the co-occurrence pairs of the user are his/her interest content, implicitly.

## 3.1. Modeling user interests by text mining

Our approach to modeling user interests mainly consists of three steps: extracting terms, mining frequent patterns, and pruning patterns. In this section, we present the steps to initially build a personal user model in detail.

The <sup>fi</sup>rst step in user modeling is the extraction of the terms from interest content that have been preprocessed by removing stop words and stemming words [20]. After extracting terms, each interest content $c _ { j }$ is represented as a vector of attribute-value pairs as follows:

$$
c _ {j} = \left\{\left(t _ {1, j}, w _ {1, j}\right), \left(t _ {2, j}, w _ {2, j}\right),..., \left(t _ {m, j}, w _ {m, j}\right) \right\}\tag{1}
$$

where $t _ { i , j }$ is the extracted term in c and $w _ { i , j }$ is the weight of t in $c _ { j } . w _ { i , j }$ is computed by the static TF-IDF term-weighting scheme [23] and de<sup>fi</sup>ned as follows:

$$
w _ {i, j} = \frac {f _ {i , j}}{m a x _ {l} f _ {l , j}} \times l o g \frac {n}{n _ {i}}\tag{2}
$$

where $f _ { i , j }$ is the frequency of occurrence of term t in content $c _ { j } ,$ n is the total number of content pieces in the collections, and $n _ { i }$ is the number of content pieces in which term t occurs. The weight indicates the importance of a term in representing the content.

The second step is to mine frequent term patterns from the interest content of each user. Since every user has different interests, content used for the mining process must be selected individually for each user. Frequent patterns are a set of terms that appear frequently together in a set of a user's interest content. For example, if a set of terms {recommendation, collaborative, personalization, <sup>fi</sup>ltering} appear frequently together in a user's set of interest content, the set of those terms is a frequent pattern for the user. In the data mining research literature, frequent patterns are typically de<sup>fi</sup>ned as patterns that occur at least as frequently as a predetermined minimum support (min\_sup) [12]. In our study, we apply the mining process based on the following assumption: each transaction corresponds to an interest content of a user, items in a transaction are terms extracted from the content, and a transaction database corresponds to a user's set of interest content. Therefore, if the pattern support of pattern $p _ { k }$ (De<sup>fi</sup>nition 1) that is composed of at least $l \left( l { \geq } 2 \right)$ different terms, is above min\_sup, i.e., $P S _ { u }$ $( p _ { k } ) \ d s$ Nmin\_sup, then pattern $p _ { k }$ is referred to as a frequent term pattern. We denote a set of frequent term patterns for user u as $\mathbf { { } } F _ { u } .$

## Definition 1 (Pattern Support, PS)

Let $I _ { u }$ be user u's set of interest content and pattern $p _ { k } { = } \{ t _ { 1 } , t _ { 2 } , . . . , t _ { n } \}$ be a set of terms such that $p _ { k }$ T and $n { \ge } 2 . \mathsf { A }$ content piece $c _ { j }$ is said to contain pattern $p _ { k }$ if and only if p $c _ { j } .$ Pattern support for pattern ${ \boldsymbol { \cdot } } { p _ { k } }$ in $I _ { u } ,$ written as $P S _ { u } ( p _ { k } )$ , is the ratio of content in $I _ { u }$ that contains pattern $p _ { k } .$ That is, $P S _ { u } ( p _ { k } ) { = } f _ { u } ( p _ { k } ) / \vert ~ I _ { u }$ |, where $f _ { \mathrm { u } } ( \boldsymbol { p } _ { k } )$ indicates the occurrence frequency of pattern p in $I _ { u } .$

Once the frequent patterns are mined, in the third step we remove the patterns containing unnecessary terms from the set of frequent term patterns. To this end, we de<sup>fi</sup>ne the importance of each term in representing a certain pattern, called the pattern weight. Formally, for a given pattern $p _ { k } \in \pmb { F } _ { u } ,$ , the pattern weight of $p _ { k }$ for user $u ,$ denoted as $P W _ { u } ( p _ { k } )$ , is computed by:

$$
P W _ {u} (p _ {k}) = \frac {1}{| p _ {k} |} \cdot \sum_ {i \in p _ {k}} \mu_ {i, u}\tag{3}
$$

where $\mu _ { i , u }$ is the mean weight for term $t _ { i }$ in $I _ { u }$ and is computed as follows:

$$
\mu_ {i, u} = \frac {1}{| I _ {u} (i) |} \times \sum_ {j \in I _ {u} (i)} w _ {i, j}\tag{4}
$$

where $I _ { u } ( i )$ is the set of interest content for user u containing term t and $w _ { i , j }$ is the weight of term t<sub>i</sub> in content $c _ { j } .$ For any pattern $p _ { k }$ in $\mathbf { } F _ { u } ,$ we determine the patterns for which the pattern weight is greater than the minimum pattern weight, min\_pw, and model user preferences based on the identi<sup>fi</sup>ed patterns, collectively called a Personalized Term Pattern. In addition, terms that appear within personalized term patterns are called Personalized Terms.

## Definition 2 (Personalized Term Pattern, PTP)

A personalized term pattern is de<sup>fi</sup>ned as a frequent term pattern for which the pattern weight is greater than the minimum pattern weight min\_pw, i.e., $p _ { k } \in F _ { u }$ and $P W _ { u } ( p _ { k } )$ Nmin\_pw. A set of personalized term patterns for user u is denoted as $P T P _ { u }$ such that $P T P _ { u } { = } \{ ( p _ { k } , P S _ { u } ( p _ { k } ) ) |$ $P W _ { u } ( p _ { k } )$ Nmin\_pw ∧ $p _ { k } \in F _ { u } \}$

## Definition 3 (Personalized Term, PT)

A personalized term is a term that occurs within personalized term patterns. The set of personalized terms for user u is denoted as $P T _ { u } .$ . In addition, the vector for $P T _ { u }$ is represented by $\vec { P T } _ { u } = ( \mu _ { 1 , u } , \mu _ { 2 , u } , . . . , \mu _ { t , u } )$ where t is the total number of personalized terms and $\mu _ { i , u }$ is the mean weight for term $t _ { i } ,$ which is computed by Eq. (4).

The formal description of the model for user u, $M _ { u } ,$ is as follows: $\pmb { M _ { u } } = \langle P T P _ { u } , P T _ { u } \rangle$ , where $P T P _ { u }$ models the interest patterns (De<sup>fi</sup>nition 2) and $P T _ { u }$ models the interest terms (De<sup>fi</sup>nition 3). And the model is stored in a pre<sup>fi</sup>x tree structure, which is inspired by a frequent-pattern tree (FP-tree) [12], to save memory space, explore relationships of terms, and retrieve PTPs having some PTs ef<sup>fi</sup>ciently.

For example, if <sup>fi</sup>ve personalized term patterns are found, as shown in Table 1, after mining the content of interest for user u, the tree structure of the model for user u is then constructed as follows. All $P T _ { \mathrm { u } }$ are stored in the header table and sorted in order of descending frequency of terms since there are better chances that more pre<sup>fi</sup>x terms can be shared [12].

First, we create the root of the tree, labeled with “null”. For the <sup>fi</sup>rst term pattern, $\{ t _ { 1 } , t _ { 2 } , t _ { 3 } \}$ is inserted into the tree as a path from the root node, where $t _ { 2 }$ is linked as the child of the root, $t _ { 1 }$ is linked to $t _ { 2 } ,$ and $t _ { 3 }$ is linked to $t _ { 1 } . P S$ and length of the pattern $( P S ( p _ { 1 } ) = 0 . 5 6 ,$ , length=3) are then attached to the last node $t _ { 3 } .$ The nodes linked together in the path imply that the nodes (terms) contained in the pattern co-occur frequently in the user's interest content. For the second pattern, since its term pattern, $\{ t _ { 1 } , t _ { 2 } , t _ { 3 } ,$ and $t _ { 4 } \}$ , shares a common pre<sup>fi</sup>x $\{ t _ { 2 } , t _ { 1 } ,$ and $t _ { 3 } \}$ with the existing path for the <sup>fi</sup>rst term pattern, a new node $t _ { 4 }$ is created and linked as a child of node $t _ { 3 } .$ Thereafter. $P S ( p _ { 2 } )$ and length(p₂) are attached to the last node $t _ { 4 } .$ The third, fourth, and <sup>fi</sup>fth patterns are inserted in a manner similar to the <sup>fi</sup>rst and second patterns. To facilitate tree traversal, a header table is built, in which each term points to its occurrence in the tree via a node-link. Nodes with the same term-name are linked in sequence via such node-links. Finally, the model for user u is constructed as shown in Fig. 1. Note that the built tree is a compact data structure for representing the whole interest patterns and terms of user u by sharing personalized terms in the personalized patterns.

![](/api/attachments/5QZ34VQY/fulltext/images/c56d6a791bf7a6290c80b5fcd7b9e6c0420076d485d43c8e67b5b044fd0dfd25.jpg)  
Fig. 1. A tree structure of $M _ { u }$ for personalized term patterns in Table 1.

## 4. Collaborative user modeling for content <sup>fi</sup>ltering

In this section we describe how to enrich the model for a speci<sup>fi</sup>c user. The model $M _ { u }$ described in Section 3 is referred to the initial user model for user u. This model can be applied immediately to generate content recommendations. However, diverse patterns for user u cannot be discovered via the mining process in the case where the user has a small number of interest content. This is known as a cold start user. With this situation, initial personalized term patterns may not be suf<sup>fi</sup>cient to represent user preferences, and thus our approach is generally unable to make high quality recommendations. In addition, when we only use the initial model for recommendations, it is hard to recommend to the user novel content of value aside from the usual set. For the above reasons, we propose an enrichment method of the user model via personalized term patterns of like-minded users.

## 4.1. Content-based neighborhood formation

The main goal of neighborhood formation is to identify a set of user neighbors, k nearest neighbors, which is de<sup>fi</sup>ned as a group of users exhibiting interest terms similar to those of the target user. A typical collaborative <sup>fi</sup>ltering recommender system encounters serious limitations for <sup>fi</sup>nding a set of users, namely the sparsity problem [8,17]. The sparsity problem occurs when available data is insuf<sup>fi</sup>cient to identify similar users (neighbors) due to the immense amount of content. In practice, even when users are very active, the result of rated content is only a small proportion of the total number of content. Accordingly, it is often the case that a pair of users has nothing in common, and hence the similarity cannot be computed. Even when the computation of similarity is possible, it may not be very reliable, because insuf<sup>fi</sup>cient information is processed. To this end, in our study, we select the best neighbors by using the personalized terms, PT, of each user. In order to <sup>fi</sup>nd k nearest neighbors, the cosine similarity, which quanti<sup>fi</sup>es the similarity of a pair of vectors according to their angle, is employed to measure the similarity values between a target user and every other user. As noted in De<sup>fi</sup>nition $^ { 3 , }$ the personalized terms of a pair of users, u and $\nu ,$ are represented as t-dimensional vectors, $\vec { P T } _ { u }$ and $\vec { P T } _ { \nu }$ respectively. Therefore, the similarity between a pair of users, u and v is measured by Eq. (5).

$$
\operatorname{sim} (u, v) = \cos \left(\vec {P T _ {u}}, \vec {P T _ {v}}\right) = \frac {\sum_ {k = 1} ^ {t} \mu_ {k , u} \times \mu_ {k , v}}{\sqrt {\sum_ {k = 1} ^ {t} \mu_ {k , u} ^ {2}} \times \sqrt {\sum_ {k = 1} ^ {t} \mu_ {k , v} ^ {2}}}.\tag{5}
$$

The similarity score between a pair of users is in the range [0, 1] and the higher a user's score, the more similar he/she is to the target user. After computing the all-to-all similarity between users, we de<sup>fi</sup>ne the set of nearest neighbors of each user u as an ordered list of k users $N ( u ) = \{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { k } \}$ such that u∉ $N ( u )$ , and $s i m ( u , v _ { 1 } )$ is the maximum, sim $\scriptstyle { \ l ( u , v _ { 2 } ) }$ is the next maximum etc. [24].

## 4.2. Collaborative enrichment of user interests

Once we have identi<sup>fi</sup>ed the set of the nearest neighbors for a certain user u, his/her initial model $\pmb { M _ { u } } = \langle P T P _ { u } , \ P T _ { u } \rangle$ is enriched from the neighbors. The basic idea of enriching the model of the user u starts from assuming that the user is likely to prefer similar patterns that have been discovered from the neighbors with similar tastes. The patterns discovered from more similar users contribute more to enriching the model of the target user. For example, if the pattern, such as {personalization, recommender}, frequently appears in interest content of a user, he/she might also be interested in the pattern, such as {personalization, recommender, collaborative, <sup>fi</sup>ltering}, that frequently appears in interest content of users similar to him/her. This enrichment process is particularly effective to some users who do not contain interest terms and patterns in their user model, such as the cold start users.

We elaborate on the general idea of the enrichment process in the following. Let $N ( u ) = \{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { k } \}$ be a sorted neighbor list of target user $u , P T P _ { u }$ be a set of personalized term patterns for user u, and $P T P _ { v } ,$ $\nu \in N ( u )$ , be a set of personalized term patterns for neighbor user v of user u. Firstly, we choose neighbor user v in descending order of similarity between target user u and neighbors.

For each pattern $p _ { i }$ in $P T P _ { u } ,$ specific patterns o $\dot { \cdot } p _ { i }$ in $P T P _ { \nu }$ are identi<sup>fi</sup>ed. Given two patterns $p _ { i }$ and $p _ { j } , p _ { i }$ is said to be a general pattern of $p _ { j }$ if and only if $p _ { i }$ is a subset of $p _ { j } ,$ i.e., $p _ { i } \subset p _ { j } .$ On the contrary, $p _ { j }$ is said to be a specific pattern of $p _ { i } .$ For example, let $p _ { 1 } = \{ t _ { 4 } ,$ , and $t _ { 5 } \}$ be the personalized terms pattern for user u such that $p _ { 1 } { \in } P T P _ { u } ,$ , and $P T P _ { \nu } { = } \{ p _ { 2 } , p _ { 3 } , p _ { 4 } ,$ and $p _ { 5 } \}$ be the set of PTPs for user v such that $p _ { 2 } = \{ t _ { 2 } , t _ { 4 } ,$ and t<sub>5</sub>}, $p _ { 3 } = \{ t _ { 4 } , t _ { 5 } ,$ and t<sub>8</sub>}, $p _ { 4 } = \{ t _ { 2 } , t _ { 4 } , t _ { 5 }$ , and t }, and $p _ { 5 } = \{ t _ { 7 } ,$ , and $t _ { 8 } \}$ as shown in Fig. 2.

Since pattern $p _ { 2 } , p _ { 3 } ,$ and $p _ { 4 }$ contain the entire terms of pattern $p _ { 1 }$ they are said to be a speci<sup>fi</sup>c pattern. Several speci<sup>fi</sup>c patterns that occur in the PTPs of neighbor v, $P T P _ { v } ,$ may be found. For ef<sup>fi</sup>cient enrichment, we only consider speci<sup>fi</sup>c patterns which have higher pattern support than that of the general pattern. Assume that the pattern support for $p _ { 1 } ,$ $p _ { 2 } , p _ { 3 } ,$ and $p _ { 4 } \mathrm { i } s 0 . 4 1 , 0 . 5 , 0 . 4 7$ , and $0 . 3 5$ , respectively $( \mathrm { i . e . , } P S _ { u } ( p _ { 1 } ) = 0 . 4 1 ,$ $P S _ { \nu } ( p _ { 2 } ) = 0 . 5 , \ P S _ { \nu } ( p _ { 3 } ) = 0 . 4 7$ , and $P S _ { \nu } ( p _ { 4 } ) = 0 . 3 5 )$ ). In this case, only pattern p and $p _ { 3 }$ is used for enriching the model of user u if they are not PTPs for user u, as can be seen in Fig. 3. Patterns such as $p _ { 2 }$ and $p _ { 3 }$ are called Collaborative Term Patterns (CTPs) for target user u. An enriched model for user u by neighbor user v is built, as shown in Fig. 4.

Finally, a set of collaborative patterns is identi<sup>fi</sup>ed from k nearest neighbors, with respect to target user u. Note that the collaborative term pattern for the target user is not allowed to be redundant. That is, if the same patterns that were previously enriched by neighbor v are also discovered from another neighbor h such that sim $( u , v ) { \geq } s i m ( u , h )$ for v≠h, those patterns are pruned.

The enriched model for user u is de<sup>fi</sup>ned as a triple $M ^ { + } { } _ { u } = \langle P T P _ { u } , C T P _ { u } ,$ $P T ^ { + } { } _ { u } )$ where $P T P _ { u }$ is the set of personalized term patterns for user u, $C T P _ { u }$ is the set of collaborative term patterns for user u, and $P T _ { \ u } ^ { + }$ is the set of interest terms that occur within either the personalized patterns or the collaborative patterns, respectively. In the enriched model $M ^ { + } { } _ { u } , P T P _ { u }$ models the interest patterns of user u whereas $C T P _ { u }$ models the enriched interest patterns by the neighbors of user u.

![](/api/attachments/5QZ34VQY/fulltext/images/f44e5677c0c6bb342fe7456e08e3e2348cf81e3c7e80decbe5e11d3536a80467.jpg)  
Fig. 2. Initial model for user v who is a neighbor of target user u.

![](/api/attachments/5QZ34VQY/fulltext/images/f857ac8148a2d0906537561b113175f0935c0bf33d73c0c1183ff0edf01e913d.jpg)  
Fig. 3. Speci<sup>fi</sup>c patterns, general pattern, and enriched patterns.

## Definition 4 (Collaborative Term Pattern, CTP)

Le $p _ { i }$ be a personalized term pattern for target user u, $p _ { i } { \in } P T P _ { u }$ , and p be a personalized term pattern for neighbor v such that $p _ { j } { \in } P T P _ { \nu } ,$ , and $\nu \in N ( u )$ . We de<sup>fi</sup>ne the set of collaborative term patterns for user u, denoted as $C T P _ { u } ,$ as the set of neighbor patterns $p _ { j }$ such that $p _ { i } \subset p _ { j }$ p<sub>j</sub>∉ $P T P _ { u } ,$ and $P S _ { u } ( p _ { i } ) { \leq } P S _ { v } ( p _ { j } )$ .

## 4.3. Personalized content recommendation

After the model is enriched, we are ready to provide recommendations for new content that a user has not previously read. Based on the enriched model for each user, we recommend to the user the top-N ranked content that he/she might be interested in reading. To this end, the most important task in personalized recommendation is to generate a prediction, that is, speculation about how much a certain user would prefer unseen content. In our study, we consider matched patterns, that ${ \mathrm { i } } s ,$ how many interest patterns in a user model are contained in the new content. Formally, the numeric score of the target user u for the content $c _ { n } ,$ denoted as $P _ { u , n } ,$ is obtained as follows:

$$
P _ {u, n} = \frac {\sum_ {p _ {k} \in (P T P _ {u} \cup C T P _ {u})} B _ {n} ^ {p _ {k}}}{N _ {u}}. \frac {\sum_ {p _ {k} \in (P T P _ {u} \cup C T P _ {u})} | p _ {k} | \times \omega_ {u} ^ {p _ {k}} \times B _ {n} ^ {p _ {k}}}{\sum_ {P _ {k} \in (P T P _ {u} \cup C T P _ {u})} \omega_ {u} ^ {p _ {k}}}\tag{6}
$$

where $N _ { u }$ is the total number of patterns in both $P T P _ { u }$ and $C T P _ { u } ,$ and B<sup>pk</sup> is binary variable for determining whether or not pattern $p _ { k }$ occurs in content $c _ { n \cdot }$ . That is, $B _ { n } ^ { p _ { k } }$ is 1 if pattern $p _ { k }$ appears in content $c _ { n }$ and 0 otherwise, and $\omega _ { u } ^ { p _ { k } }$ represents the weighted pattern support of $p _ { k }$ for user u, which is given by:

$$
\omega_ {u} ^ {p _ {k}} = \left\{ \begin{array}{l l} P S _ {u} (p _ {k}) & \text { if } p _ {k} \in \mathrm{PTP} _ {u} \\ P S _ {v} (p _ {k}) \times s i m (u, v) & \text { if } p _ {k} \in \mathrm{CTP} _ {u}, p _ {k} \in \mathrm{PTP} _ {v} \end{array} \right.\tag{7}
$$

The main concept of prediction dictates that interest patterns in the model of the target user are a good estimate of the preference for the selected content. The more the content contains the patterns in the model, the higher rank the content obtains. This scheme can also make recommendations for new content added regularly to the system, known as the new item problem in collaborative <sup>fi</sup>ltering [1], as well as support serendipitous recommendations [13]. Recommender systems relying exclusively on a user's interest content can only recommend content highly related to that which the user has previously selected. It is hard to recommend novel content that are different from anything the user has previously read before. This is known as the problem with overspecialization [1,22]. In our approach, by utilizing the enriched patterns from neighbors with similar tastes, we can make content to be a higher rank in the recommended set that the content contains the collaborative (enriched) patterns valuable to the target user, even though the patterns are not directly discovered from the user's interest content.

Once the content predictions about the target user, which the user has not previously read, are computed, the content are sorted in order of descending predicted value $P _ { u , n } .$ . Finally, the set of N ordered content elements with the highest values are identi<sup>fi</sup>ed for user u. This is the set of content recommended to user u (top-N recommendation).

Definition 5 (Top-N recommendation)

Let C be the set of all content, $X _ { u }$ be the content list that user u has previously collected or added to his preference list (interest content), and $Y _ { u }$ be the content list not previously read by user u, $Y _ { u } = C - X _ { u }$ and $X _ { u } \cap Y _ { u } = \emptyset$ . Given a pair of content elements c and $c _ { j } , c _ { i } \in Y _ { u }$ and $c _ { j } \in Y _ { u } ,$ content $c _ { i }$ will be of more interest to user u than content $c _ { j }$ if and only if the prediction score $P _ { u , i }$ of the target user u for the content c is higher than that of content $c _ { j } , \ P _ { u , i } { > } P _ { u , j } . \ T o p { - } N$ recommendations for user u identi<sup>fi</sup>es an ordered set of N content, TopN , that will be of interest to user u such that $\vert T o p N _ { u } \vert \le N , T o p N _ { u } \cap X _ { u } = \emptyset$ , and $T o p N _ { u }$ Y<sub>u</sub>.

![](/api/attachments/5QZ34VQY/fulltext/images/fb7e3155a150f494c1a461d2a739c7fd60768a899021035723e6ac242820d27c.jpg)  
Fig. 4. Enriched user u model, $M ^ { + } { } _ { u } ,$ , by neighbor user v.

## 5. System implementation

Based on the requirements de<sup>fi</sup>ned in Sections 3 and 4, we developed a prototype system to support personalized content recommendations, named PRCUM (Personalized Recommendations via Collaborative User Model). The PRCUM system is divided into four main types of tasks: (a) Observing relevance feedback of a given user, (b) Modeling user interests from observed content, (c) Enriching user interests from nearest neighbors, and (d) Generating content recommendations for a given user. An overall system process for personalized content recommendations is shown in Fig. 5.

PRCUM <sup>fi</sup>rst requires the user to sign in with his/her username and password, and then it allows the user to add content to a preference list and monitors the user's browsing inside the system. Because PRCUM cannot make recommendations to the user before building the individual model, it delays recommendations until the model is of a suf<sup>fi</sup>cient size and has been successfully built. The user can adjust the desired model parameters, such as the minimum support (min\_sup), the minimum pattern weight (min\_pw) and the number of nearest neighbors (k). Once the model has been built, PRCUM allows the user to enter his/her personalized pages and proposes to him/her a list of recommended content. The GUI of PRCUM is implemented using C# and the server side is implemented using MySQL 5.0 and PHP 5.2 in an Apache 2.2 environment.

The GUI mainly consists of four frames: a menu frame, a favorite frame, a recommendation frame and a main frame. By interacting with the menu frame, users can choose the functions of PRCUM rendered by the main frame. As one of the principal functions in PRCUM, the recommendation frame provides a list of recommended content, a list of nearest neighbors, and recently added interest content. And the favorite frame is used for jumping to content in favorites previously registered in PRCUM. Users can maximize (display) or minimize (hide) the recommendation frame and the favorite frame according to their preference. Fig. 6 shows a snapshot of the user interface for the PRCUM system.

## 6. Experimental evaluation

In this section, we empirically evaluate the proposed approach and compare its performance against that of the benchmark algorithms. All experiments were performed on a Dual Xeon 3.0 GHz, 2.5 GB RAM computer running the MS-Window 2003 server.

## 6.1. Datasets

We use two test datasets for our comparative experiments. The <sup>fi</sup>rst dataset is taken from NSF (National Science Foundation) research award abstracts [20]. The original dataset is too large to be used in practice and thus we selected award abstracts with topics highly related to computer science. The selected dataset contains 974 unique abstracts (i.e., content) and 9823 unique terms were obtained from the abstracts. In addition, we collected 9845 preference histories (i.e., interest content of users) from 78 users. We refer to this dataset as NSF.

Table 2  
Datasets used in experimental evaluation.

<table><tr><td></td><td>Number of users</td><td>Number of items</td><td>Number of interest items</td></tr><tr><td>NSF</td><td>78</td><td>974</td><td>9845</td></tr><tr><td>MLens</td><td>658</td><td>1682</td><td>50,318</td></tr></table>

The second dataset comes from MovieLens, which is a web-based research recommendation system (www.movielens.org). The original dataset does not contain any information about movie content, and thus we extracted the textual descriptions (i.e., genres, keywords, summary) for each movie from the IMDb database (www.imdb.com). Though the dataset contains numerical ratings, we ignored these and binarized them as follows: if a certain user's movie rating is larger than his/her average rating we set the rating to 1 (i.e., the interest movie of the user), or 0 otherwise. Thereafter, we removed users who had less than 20 ratings. The binarized dataset consists of 50,318 ratings on 1682 movies from 658 users. We refer to this dataset as MLens. Table 2 brie<sup>fl</sup>y describes our datasets.

## 6.2. Evaluation design and metrics

To evaluate the performance of the recommendations, we randomly divided the dataset into a training set and a test set. The users' interest items were split into a test set with 10 items per user (i.e., 780 items for NSF and 6580 items for MLens) and a training set with the remaining content (i.e., 9065 items for NSF and 43,738 items for MLens) that was to used to learn and build a model of each user.

In order to evaluate the performance of our approach, we implemented the following: i) a user-based collaborative <sup>fi</sup>ltering method UCF [24], ii) an item-based collaborative <sup>fi</sup>ltering method, which employs cosine-based similarity ICF [9], iii) a probabilistic learning algorithm termed NB that applies the multinomial event model of a naïve Bayes assumption [16], and iv) a TF-IDF vector-based algorithm VT [6]. For the content recommendation process, in the case of NB, content were ranked using the calculated probability values, whereas they were ranked using the calculated cosine similarity for VT. For UCF and ICF, the proximity between users or items was measured by cosine-based similarity and items were ranked using the weighted sum using the similarity as the weight. Our top-N recommendation strategy $( M ^ { + } )$ was then compared with the benchmark algorithms. We adopted two evaluation measures that are de<sup>fi</sup>ned as follows:

![](/api/attachments/5QZ34VQY/fulltext/images/07f2209c7b8fcd7a2cb098824fcf0146bf02ce528322180b98aef6928a65307c.jpg)  
Fig. 5. An overview of PRCUM for content recommendations.

![](/api/attachments/5QZ34VQY/fulltext/images/56a15ae20acf2e12142d5ac743bb898ffb3d78d9455c10d5ff9457c2381d0f30.jpg)  
Fig. 6. A snapshot of the user interface for PRCUM.

## 6.2.1. Hit Rate (HR)

In the context of top-N recommendations, the hit-rate, a measure of how often a list of recommendations contains items that the user is actually interested in, was used for the evaluation metric [9]. The hit-rate for user u is de<sup>fi</sup>ned as:

$$
H R (u) = \frac {\mid T e s t _ {u} \cap T o p N _ {u} \mid}{\mid T e s t _ {u} \mid}\tag{8}
$$

where $T e s t _ { u }$ is the item list of user u in the test data and $T o p N _ { u }$ is the top-N recommended item list for user u. Finally, the overall HR of top-N recommendation for all users is computed by averaging the personal HR(u) in the test data.

## 6.2.2. Reciprocal Hit Rank (RHR)

One limitation of the hit-rate measure is that it treats all hits equally regardless of the ranking of recommended content. In other words, a content item that is recommended with top ranking is treated equally with an item that is recommended with Nth ranking. To address this limitation, we adopted the reciprocal hit-rank metric described in [9].

Table 3  
HR and RHR with respect to increasing neighborhood size (NSF).

<table><tr><td>Neighbors:</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td></tr><tr><td>HR</td><td>0.1584</td><td>0.1636</td><td>0.1640</td><td>0.1651</td><td>0.1655</td><td>0.1643</td></tr><tr><td>RHR</td><td>0.4238</td><td>0.4891</td><td>0.4889</td><td>0.4745</td><td>0.4732</td><td>0.4732</td></tr></table>

The reciprocal hit-rank for user u is de<sup>fi</sup>ned as:

$$
R H R (u) = \sum_ {i _ {n} \in \left(\text { Test } _ {u} \cap {} ^ {u} \text { TopN } _ {u}\right)} \frac {1}{\operatorname{rank} \left(i _ {n}\right)}\tag{9}
$$

where rank(i ) refers to the recommended ranking of item i within the hit set of user u. That is, hit content that appear earlier in the top-N list are given more weight than later ones. Finally, the overall RHR for all users is computed by averaging the personal RHR(u) in the test data. The higher the RHR, the more accurately the algorithm recommends items.

## 6.3. Experimental results

In this section, we present detailed experimental results. The performance evaluation is divided into three dimensions. The effect of the neighbor size on the performance of model enrichment is <sup>fi</sup>rst evaluated, and then the effectiveness of model enrichment is evaluated in comparison with the initial user model. Finally, the accuracy of content recommendations is evaluated in comparison with the benchmark methods. In the experiments, min\_sup and min\_pw was set to 0.1 (10%) and 0.5, respectively.

Table 4  
HR and RHR with respect to increasing neighborhood size nMLens).

<table><tr><td>Neighbors:</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td></tr><tr><td>HR</td><td>0.2043</td><td>0.2136</td><td>0.2255</td><td>0.2262</td><td>0.2262</td><td>0.2288</td></tr><tr><td>RHR</td><td>0.2822</td><td>0.3666</td><td>0.3881</td><td>0.3881</td><td>0.3876</td><td>0.3732</td></tr></table>

![](/api/attachments/5QZ34VQY/fulltext/images/5f6a311cc636d06842a105126cb446f6cbdfd1e32a9475cd9331da5902ab3430.jpg)

![](/api/attachments/5QZ34VQY/fulltext/images/754deaae35eeb2014491789a34b4748fd8d005804e8f1ca41840d689cca14f49.jpg)

![](/api/attachments/5QZ34VQY/fulltext/images/5e126cec516efe750ac153bf67396f51142d38ae5be67e433a49bf03d3fee29b.jpg)

![](/api/attachments/5QZ34VQY/fulltext/images/7287140ad56866646df13ec7fcf2d16aef89aeb04753943a5d86405ce4162171.jpg)  
Fig. 7. Comparison of HR and RHR obtained by the initial model and the enriched model.

## 6.3.1. Experiments with neighborhood size

The following experiment investigates the effect of the enriched model through the neighborhood. And the number of recommended items N was set to 10 for each user in the test set. As noted in a number of previous studies, the size of the neighborhood in<sup>fl</sup>uences the recommendation quality of neighborhood-based algorithms. Therefore, different numbers of user neighbors were used for model enrichment: 10, 20, 30, 40, 50, and 60.

Table 3 summarizes the results of RHR and HR for the NSF dataset. With respect to HR, we observe that HR tends to improve slightly as the neighborhood size increases from 10 to 20; beyond this point, any further increase of the model size did not affect the performance. Interestingly, RHR was poorer for a neighborhood size of 30, 40, 50, and 60 than for a size of 20.

We further examined the performance of the MLens dataset. Similar results to NSF were obtained for MLens, as can be seen in Table 4. For example, when the neighborhood size is 30, this provides a reasonably good performance for both HR and RHR.

These results were affected by the fact that a neighborhood with a small size provides enough collaborative term patterns for each user. Recall that patterns are selected for enriching collaborative term patterns according to the nearest-order of neighbors, and thus redundant patterns generated by farthest neighbors are pruned. Another reason might be that we were only looking for a small number of recommended content (i.e., N=10). That is, once the number of nearest neighbors is relatively large, the rank of recommended content for each user is barely changed by any further increases in the number of nearest neighbors. In practice, recommender systems make a trade-off between recommendation accuracy and real-time performance ef<sup>fi</sup>ciency by pre-selecting a number of nearest neighbors. In consideration of both accuracy and computation cost, we selected 20 and 30 as the neighborhood size for NSF and MLens model enrichment, respectively, in subsequent experiments.

![](/api/attachments/5QZ34VQY/fulltext/images/e56ae6ac45de8875c33fcbbe1f855da108906e8a23a10d9895bddaa334a8f2d5.jpg)

![](/api/attachments/5QZ34VQY/fulltext/images/606ae6b290c506ff657eeea44e4a5afeff60d57f54e88fb6f035e0600a75e84b.jpg)

![](/api/attachments/5QZ34VQY/fulltext/images/6f987f130714fccb1a92a2eb2046328bc8ae73a0fb1909026911dce74dedb11f.jpg)

![](/api/attachments/5QZ34VQY/fulltext/images/860970090ee122956dccb35555d97c611d8d3fe584751d3223ab20a382497263.jpg)  
Fig. 8. Comparisons of HR and RHR with respect to increasing N.

## 6.3.2. Effect of model enrichment

This section investigates the effect of the enriched model $M ^ { + }$ of each user in more detail, by comparing the results obtained by the initial model M of each user. We performed an experiment with N values of 10, 20, and 30 and examined the average number of collaborative term patterns of users. In the case of NSF, we found that 192 patterns had been enriched for each user, whereas the average number was 234 for MLens.

Fig. 7 presents the results of the experiment. The results demonstrate that the enriched model provides considerably improved HR values on all occasions, compared to the initial model. For example, the enriched model $M ^ { + }$ achieves 8.7% and 11.4% average improvement for NSF and MLens, respectively, in terms of HR, compared to the initial model M. Similar conclusions are implied by the RHR results as well. More importantly, we found that the enriched model outperforms the initial model in all cases that the number of recommended content is small. When N is 10, the enriched model obtains an RHR value of 0.489 and 0.388 for NSF and MLens, respectively, whereas the initial model demonstrates an RHR value of 0.358 and 0.281, respectively. This is particularly important, since users tend to click on content with higher ranks. We conclude that the collaborative model has signi<sup>fi</sup>cant advantages in terms of improving both the recommendation accuracy and the recommendation ranking.

## 6.3.3. Comparisons with other methods

To experimentally evaluate the performance of top-N recommendation, we calculated the hit rate (HR) and the reciprocal hit rank (RHR) obtained by NB, VT, UCF, ICF and $M ^ { + }$ . We selectively varied the number of returned items N from 10 to 30 with an increment of 10. According to previous studies for collaborative <sup>fi</sup>ltering, the neighborhood size of UCF and ICF was set to 50.

Fig. 8 shows the results of RHR and HR for the NSF and MLens dataset, showing how $M ^ { + }$ outperforms the benchmark methods. As the number of recommended items N increases, the HR and RHR values tend to increase. Comparing the results achieved by $M ^ { + }$ and the benchmark algorithms, for both test sets, the HR value of the former was found to be superior to that of the benchmark methods in all cases. In the NSF dataset, on average, on all occasions, $M ^ { + }$ outperforms VT, NB, UCF and ICF by 6.7%, 16.7%, 7% and 8.5%, respectively. And for the MLens dataset, $M ^ { + }$ obtains 11.1%, 12.7%, 4.2%, and 4.2% improvement compared to VT, NB, UCF, and ICF, respectively. With respect to RHR, similar results are demonstrated. More interestingly, $M ^ { + }$ signi<sup>fi</sup>cantly outperforms the other methods when a relatively small number of content items were recommended. For the MLens dataset, in the case of N=10, our method outperforms all of the other methods, whereas for the NSF dataset, only VT achieves comparable results. That is, $M ^ { + }$ provides more suitable content with a higher rank in the recommended content set, and thus can provide better quality of content for the target user than the other methods.

Ideally, recommender systems should provide a wide range of desirable content for users. Therefore, we continued to analyze the number of content items for which the methods, except for NB, could not provide any predictions for a user (i.e., the prediction value of the target user for the content was zero). Recall that NB and VT is a class of content-based <sup>fi</sup>ltering, whereas UCF and ICF is a class of collaborative <sup>fi</sup>ltering. Strictly speaking, our approach is closely connected with content-based <sup>fi</sup>ltering due to the dependence of content characteristics $( \mathrm { i . e . }$ , content-based user models, content-based neighbors, contentbased enrichments, and content-based recommendations). The results of the NSF dataset were that 2.6%, 7.1%, 7.1% and 2.9% of items for VT, UCF, ICF and $M ^ { + }$ could not be predicted, respectively. For the MLens dataset, 0.12%, 0.29%, 0.68% and 0.13% of items for VT, UCF, ICF and $M ^ { + }$ could not be predicted, respectively. As noted previously, such results are due to the fact that the collaborative <sup>fi</sup>ltering approaches, UCF and $I C F ,$ can only make predictions for items that at least a few users have rated. On the other hand, VT and $M ^ { + }$ can only make predictions for items that contain terms in the target user model, although they never suffer from cold start items.

These comparison experiments show that our collaborative model effectively and consistently improves the recommendation quality.

## 7. Conclusions and future work

Automated recommender systems are becoming widely used as a solution for reducing information overload of diverse domains. In this paper we presented a new and unique method for modeling user interests via a collaborative approach of users. It also provides enhanced recommendation accuracy. The major advantage of the proposed modeling method is that it supports not only identi<sup>fi</sup>cation of each user's useful patterns but also enrichment of valuable neighbors' patterns. As noted in our experimental results, our model obtained better recommendation accuracy compared to the benchmark methods. Moreover, we also observed that our method can provide more suitable content for user preferences, even when the number of recommended items is small. There are common issues that have been mentioned in keyword-based analysis: homonymy and synonymy. We expect to improve our user model further by considering word semantics such as WordNet [18] or ontologies. Therefore, we plan to do further study on semantic user models in recommender systems.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[2] S. Berkovsky, T. Ku<sup>fl</sup>ik, F. Ricci, Mediation of user models for enhanced personalization in recommender systems, User Modeling and User-Adapted Interaction 18 (3) (2008) 245–286.

[3] S. Berkovsky, T. Ku<sup>fl</sup>ik, F. Ricci, Cross-representation mediation of user models User Modeling and User-Adapted Interaction 19 (2009) 35–63.

[4] R. Burke, Hybrid recommender systems: survey and experiments, User Modeling and User-Adapted Interaction 12 (2002) 331–370.

[5] C.C. Chen, M.C. Chen, Y. Sun, PVA: a self-adaptive personal view agent, Journal of Intelligent Information Systems 18 (2002) 173-194

[6] L. Chen, K. Sycara, WebMate: personal agent for browsing and searching, Proceedings of the 2nd international conference on autonomous agents and multi agent systems, 1998, pp. 132–139.

[7] A. Das, M. Datar, A. Garg, Google news personalization: scalable online collaborative <sup>fi</sup>ltering, Proceedings of the 16th international conference on World Wide Web, 2007, pp. 271–280.

[8] M. Degemmis, P. Lops, G. Semeraro, A content-collaborative recommender that exploits WordNet-based user pro<sup>fi</sup>les for neighborhood formation, User Modeling and User-Adapted Interaction 17 (2007) 217–255.

[9] M. Deshpande, G. Karypis, Item-based top-n recommendation algorithms, ACM Transactions on Information Systems 22 (1) (2004) 143–177.

[10] S. Flesca, S. Greco, A. Tagarelli, E. Zumpano, Mining user preferences, page content and usage to personalize website navigation, World Wide Web: Internet and Web Information System 8 (3) (2005) 317–345.

[11] E. Gabrilovich, S. Dumais, E. Horvitz, Newsjunkie: providing personalized news-feeds via analysis of information novelty, Proceedings of the 13th international conference on World Wide Web, 2004, pp. 482–490.

[12] J. Han, J. Pei, Y. Yin, Mining frequent patterns without candidate generation: a frequent-pattern tree approach, Data Mining and Knowledge Discovery 8 (2004) 53–87.

[13] J.L. Herlocker, J.A. Konstan, J. Riedl, Explaining collaborative <sup>fi</sup>ltering recommendations, Proceedings of the 2000 ACM conference on computer supported cooperative work, 2000, pp. 241–250.

[14] W. Lihua, L. Lu, L. Jing, Zongyong Li, Modeling user multiple interests by an improved GCS approach, Expert Systems with Applications 29 (2005) 757–767.

[15] B. Magnini, C. Strapparava, User modelling for news web sites with word sense based techniques, User Modeling and User-Adapted Interaction 14 (2004) 239–257.

[16] A. McCallum, K. Nigam, A comparison of event models for naïve Bayes text classi<sup>fi</sup>cation, Proceedings of AAAI-98 workshop on learning for text categorization, 1998, pp. 41–48.

[17] P. Melville, R.J. Mooney, R. Nagarajan, Content-boosted collaborative <sup>fi</sup>ltering for improved recommendations Proceedings of the 18th national conference or arti<sup>fi</sup>cial intelligence, 2002, pp. 187–192.

[18] G.A. Miller, WordNet: a lexical database for English, Communications of the ACM 38 (11) (1995) 39–41.

[19] M. Montaner, B. Lopez, J.L. de la Rosa, A taxonomy of recommender agents on the internet, Arti<sup>fi</sup>cial Intelligence Review 19 (4) (2003) 285–330.

[20] M.J. Pazzani, A. Meyers, NSF research awards abstracts 1990–2003, http://kdd.ics. uci.edu/databases/nsfabs/nsfawards.html 2003.

[21] P. Resnick, N. Iacovou, M. Suchak, P. Bergstorm, J. Riedl, GroupLens: an open architecture for collaborative <sup>fi</sup>ltering of netnews, Proceedings of 1994 ACM conference on computer supported cooperative work, 1994, pp. 175–186.

[22] J. Salter, N. Antonopoulos, CinemaScreen recommender agent: combining collaborative and content-based <sup>fi</sup>ltering, IEEE Intelligent Systems 21 (2006) 35–41.

[23] G. Salton, C. Buckley, Term weighting approaches in automatic text retrieval, Information Processing and Management 24 (1988) 513–523.

[24] B.M. Sarwar, G. Karypis, J.A. Konstan, J.T. Riedl, Analysis of recommendation algorithms for e-commerce, Proceedings of the 2nd ACM conference on electronic commerce, 2000, pp. 158–167.

[25] A.I. Schein, A. Popescul, L.H. Ungar, D.M. Pennock, Methods and metrics for cold-start recommendations, Proceedings of the 25th annual international ACM SIGIR conference on research and development in information retrieval, 2002, pp. 253–260.

[26] I. Schwab, W. Pohl, I. Koychev, Learning to recommend from positive evidence, Proceedings of the 5th international conference on intelligent user interfaces, 2000 pp. 241–247.

![](/api/attachments/5QZ34VQY/fulltext/images/bbec7afa019e27a36f3848b480364b1f26337d5b73935fd5e73fd921cc04c9a8.jpg)  
Heung-Nam Kim is a postdoctoral fellow in the Multimedia Communications Research Laboratory (MCRLab) at University of Ottawa, Canada. His research interests include collaborative <sup>fi</sup>ltering, recommender systems, semantic Web, data mining, user modeling, and social networking applications. He obtained his Ph.D. in Computer and Information Engineering from Inha University, Korea.

![](/api/attachments/5QZ34VQY/fulltext/images/01fa4a2caf47af0ddc54a3f6d74241fdb88df9bca981a1d491ef8e26d2a84b15.jpg)  
Inay Ha received the B.S. degree in Computer Science from University of Suwon and the M.Eng. degree in Computer and Information Engineering from Inha University, Korea, in 2007. She is currently working toward the Ph.D. with Intelligent E-Commerce Systems Laboratory (IESL), Inha University. Her research interests include Web mining, social networks, recommender systems, and intelligent e-Learning systems.

![](/api/attachments/5QZ34VQY/fulltext/images/1c0c0a287bd70064b0eae279f342c53c76cb2ef41cfb4d117313eb71d4859345.jpg)

Kee-Sung Lee received the B.S. degree in Computer Science from Cheon-An University and the M.Eng. degree in Computer and Information Engineering from Inha Uni versity, Korea, in 2005. He is working as the Ph.D. student in Intelligent E-Commerce Systems Laboratory (IESL), Inha University. His research interests include semantic Web, image annotation and retrieval, information visualization and user interface design.

![](/api/attachments/5QZ34VQY/fulltext/images/8ec07a092dc05295161e21b4a8174d5d9b15f63edf9d8a584de704f6ff337c1e.jpg)

Geun-Sik Jo is a Professor in Computer and Information Engineering, Inha University, Korea. He is the chairman of the school of Computer and Information Engineering at Inha University. He received the B.S. degree in Computer Science from Inha University in 1982. He received the M.S. and the Ph.D. degrees in Computer Science from City University of New York in 1985 and 1991, respectively. He has been the General Chair and/or Technical Program Chair of more than 20 international conferences and workshops on arti<sup>fi</sup>cial intelligence, knowledge management, and semantic applications. His research interests include knowledge-based scheduling, ontology, semantic Web, intelligent E-Commerce, constraint-directed scheduling, knowledge-based systems, decision support systems, and intelligent agents. He has authored and coauthored <sup>fi</sup>ve books and more than 200 publications.

![](/api/attachments/5QZ34VQY/fulltext/images/2de1b56927d6dab0b513ca7e57ae34e4a13a5457a319236524e528d428f1f8cb.jpg)

Abdulmotaleb El-Saddik University Research Chair and Professor, SITE, University of Ottawa and recipient of the Friedrich Wilhelm-Bessel Research Award from Germany's Alexander von Humboldt Foundation (2007) the Premier's Research Excellence Award (PREA 2004), and the National Capital Institute of Telecommunications (NCIT) New Professorship Incentive Award (2004). He is the director of the Multimedia Communications Research Laboratory (MCRLab). He is Associate Editor of the ACM Transactions on Multimedia Computing, Communications and Applications (ACM TOMCCAP), IEEE Transactions on Multimedia (IEEE TMM) and IEEE Transactions on Computational Intelligence and AI in Games (IEEE TCIAIG) and Guest

Editor for several IEEE Transactions and Journals. Dr. El Saddik has been serving on several technical program committees of numerous IEEE and ACM events. He was the general co-chair of ACM MM 2008. He is leading researcher in haptics, service-oriented architectures, collaborative environments and ambient interactive media and communications. He has authored and coauthored two books and more than 200 publications. His research has been selected for the BEST Paper Award at the “Virtual Concepts 2006” and “IEEE COPS 2007”. Dr. El Saddik is a Senior Member of ACM, an IEEE Distinguished Lecturer and a Fellow of the IEEE (FIEEE), the Canadian Academy of Engineers (FCAE) and the Engineering Institute of Canada (FEIC).
