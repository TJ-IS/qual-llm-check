---
otero_id: 7360
otero_key: "DV55SV4A"
title: "SocoTraveler : Travel-package recommendations leveraging social influence of different relationship types"
authors: "Jiangning He; Hongyan Liu; Hui Xiong"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.04.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: SocoTraveler: Travel-package Recommendations Leveraging Social Influence of Different Relationship Types

Author: Jiangning He Hongyan Liu Hui Xiong

![](/api/attachments/DV55SV4A/fulltext/images/4967116b2730876d4dc32f766501f5404198d772a010c5f8964b974619461370.jpg)

PII: S0378-7206(16)30036-2

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.04.003

Reference: INFMAN 2901

To appear in: INFMAN

Received date: 10-7-2015

Revised date: 8-1-2016

Accepted date: 10-4-2016

Please cite this article as: Jiangning He, Hongyan Liu, Hui Xiong, SocoTraveler: Travelpackage Recommendations Leveraging Social Influence of Different Relationship Types, Information and Management http://dx.doi.org/10.1016/j.im.2016.04.003

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# SocoTraveler: Travel-package Recommendations Leveraging Social Influence of Different Relationship Types

Jiangning He<sup>a,b</sup>, Hongyan Liu<sup>a,b\*</sup>, Hui Xiong<sup>c</sup>

<sup>a</sup>Research Center for Contemporary Management, Tsinghua University, Beijing, China

<sup>b</sup>School of Economics and Management, Tsinghua University, Beijing, China

<sup>c</sup>Management Science and Information Systems Department, Rutgers, the State University of New Jersey

Corresponding author: hyliu@tsinghua.edu.cn

## Highlights

C The role of relationship type is exploited to enhance social recommendation.

 A novel topic model integrating multiple kinds of information is proposed.

Interesting findings and practical implications are obtained from real travel dataset.

## Abstract

The immense amount of data generated and collected on e-commerce platforms provides opportunities and challenges for big data analytics to create business value. E-tourism platforms collect not only users’ travel information but also users’ social connection information and need effective personalized recommendation systems for target marketing. In this paper, we aim to study how different types of social relationships such as colleague, schoolmate, and relative between co-travelers influence a user’s travel behavior and how to use this influence to enhance recommendation quality. To this end, we develop a probabilistic topic model leveraging individual travel history and social influence of co-travelers to capture personal interests and propose a recommendation method to utilize the proposed model. Experiments on a real travel dataset show that the proposed approach significantly outperforms benchmarks. The result highlights useful findings for travel agencies.

Keywords: travel-package recommendation, social relationship, topic models, social influence, collaborative filtering, generative probabilistic models

## 1 Introduction

With the development of Web 2.0 platforms and applications, an immense amount of company, product, and customer information is generated and gathered on the web at an exponential speed. The unprecedented data generation and collection speed brings about opportunities and challenges for big data analytics [1-3]. E-tourism, as a fast-growing field in e-commerce, collects rich user behavioral data and serves as an attractive field for big data analytics to facilitate operational management and foster customer relationships [4, 5]. The core product in a travel agency, travel package, refers to an integrated travel product designed by the travel agency with attributes such as category, cost, number of days, content describing travel route and activities, and related services, such as transportation and accommodation [6, 7]. Facing the overload of travel packages, travel agencies find it a great challenge to match the correct packages with the correct customers because each customer is endowed with a unique blend of experiences, motivations, and desires [8]. In addition, it is difficult for tourists to find travel packages that exactly match their preferences. The problem of information overload poses a great challenge for the development of intelligent travel-package recommenders.

Compared with traditional items, such as movies and books, travel-package recommendations have their uniqueness characterized by extreme sparseness, rapid depreciation over time, relatively higher financial and time costs, and lack of user ratings [9]. Existing studies on travel-package recommendations focused on one or two of such characteristics to improve recommendation quality. For example, Liu, Ge, Li, Chen and Xiong [9] consider temporal-spatial correlations of travel data, and Ge, Liu, Xiong, Tuzhilin and Chen [10] capture the sensitivity of time and financial cost in travel decision. However, to the best of our knowledge, little work on travel-package recommendations has considered social influence, leaving an open field worthy of research.

Social influence, through which individuals’ opinions, feelings and behaviors are affected[11], attracts wide attention in the field of social recommendations and has been proved to enhance recommendation quality significantly [12-14]. To exploit the advantage of social influence, many e-travel agencies construct social networking platforms with the intention of building and maintaining customer relationships. The mode of socialized travel provides online travel agencies with a competitive advantage over their offline counterparts. It becomes more attractive for travelers to be able to make new friends on online social networks, introduce their familiar offline friends to the social networks, travel together with friends, and share feelings of travel online. Examined by previous empirical studies on user behavior and decision theory, social influence shapes travel behavior in two channels. The first channel represents the direct influence of replicated experience; in other words, people tend to engage in a vacation enjoyed by their friends or peers. Because the mode of independent decision-making involves a high risk of wrong decisions, travelers place great emphasis on the advice and opinions of others. The second channel is the indirect influence of shared goals, meaning that friends would like to travel together to destinations that they both prefer [15]. Thus, given that social influence plays an important role in the process of travel decision-making, the consideration of this effect is expected to improve the recommendation quality.

Existing works on social recommendations fail to consider the heterogeneity and diversity of social relationship types, which might have different effects on travel-package recommendations.

People prefer to join different travel activities with different types of friends. For example, we would like to spend a romantic island holiday with lovers, start longer deep travel with close friends, and experience short nearby trips with online friends. Existing research also suggests that the information sources of distinct relationship types might lead to differing patterns of travel behavior. For example, travelers who receive advice from friends and relatives tend to visit families and friends during travel, whereas travelers who seek information from other travelers prefer to experience various types of activities [16]. Thus, the factor of relationship type exerts a discriminant effect on travel behavior.

In this paper, we focus on analyzing the social influence effects of different social relationships on users’ behavior and aim to leverage the diversity of social influence to enhance travel-package recommendations. Figure 1 depicts a heterogeneous graph to illustrate the scenario. The figure consists of a labeled social network and a bipartite graph. The labeled social network is composed of nodes of circles and edges of solid lines with labels, denoting users and social connections labeled with corresponding relationship types, separately. The labels of social connections indicate social relationship types between users, such as online friend (OF), schoolmate (S), colleague (C), relative (R) and so on. The bipartite graph consists of users (circle nodes) and travel packages (square nodes); the dashed arrows from users to packages represent individual travel history. Text in the rounded rectangle on the right of the graph displays an example of a travel package, described with various attributes such as title, category, cost, time, number of days and content. Here, the attribute time means the active duration of a travel package, during which there might be one or several batches of travel groups, and each batch of travel lasts for 7 days. The goals of this paper are twofold. One is to validate the discriminant correlation of social relationship types and selection behavior of travel packages, and the other is to incorporate both individual travel history and social influence to develop an effective model for accurate travel-package recommendations.

To reach the goals, we must solve the following issues. The first one comes from the serious sparseness of the travel dataset, making it difficult to find similar users solely from a user-package matrix. Moreover, a question remains whether it is beneficial to incorporate the information of selection behavior of friends to tackle the sparseness problem. The second issue lies in how social influence affects users’ travel decisions. Will the possibility of a user selecting a travel package increase as the number of friends selecting the package increases? The final issue is how to model the behavior of co-travel. Co-travel, the phenomenon of two users selecting same package, indicates that they share similar travel interests to some degree. How, then, does a co-travel occur—due to the attraction of travel topics, the social connection or both? Do users of different social relationship types tend to select packages of different travel topics?

To address the above issues, we propose a generative probabilistic model called socoLDA, jointly leveraging individual travel history and social influence of different relationship types to infer personal interests. Similar to LDA, socoLDA is topic-aware because it represents user interests with a user-specific probability distribution over the space of topics. Then, following the idea of user-based collaborative filtering, we introduce a recommendation framework named socoTraveler based on the user interests learned from socoLDA [9, 17]. The proposed recommendation approach finds similar users through computing similarities of user-specific topic distributions and then recommends travel packages selected by similar users. Finding similar users in a topic space is also beneficial for solving the data sparseness problem, given that it is inaccurate to find similar users by computing similarity based on the co-occurrence of user-item pairs when users have very limited numbers of travel records [6, 9].

In summary, this research makes the following contributions.

First, to the best of our knowledge, this work is the first to consider social influence to improve the performance of travel-package recommendations. In addition, we attempted to discriminate social influence of different relationship types on travel behavior, which remains an open field even in all item recommendation domains.

Second, we proposed a novel generative probabilistic model named socoLDA with heterogeneous social influence to better capture users’ travel interests. Moreover, a deep analysis of the proposed model highlights many useful insights about product design and marketing strategy of travel agencies.

Third, we developed a sound recommendation framework called socoTraveler combining the proposed model with user-based collaborative filtering. Experiments conducted on a real travel dataset demonstrate the advantages of our proposed method in comparison with the state-of-art recommendation approaches.

In the rest of the paper, we first review the literature in Section 2, then provide a definition of the travel-package recommendation problem in Section 3. Based on a description and analysis of the dataset in Section 4, we introduce our socoLDA model in Section 5 and present the recommendation framework in Section 6. Experimental evaluation is given in Section 7, and further discussions are listed in Section 8. Finally, we conclude the paper and list possible directions for future work in Section 9.

#

## 2 Literature Review

This paper is related to three branches of research: travel-package recommendations, social recommendations, and topic models.

## 2.1 Travel-package recommendations

Travel-package recommendations aim to recommend products or services provided by e-travel companies to users. To this end, personalized travel-package recommenders must capture or infer users’ travel interests from users’ consumption behavior on travel packages. Early studies focused on developing and presenting prototypes of personalization travel agents, but the recommendation methods employed are relatively simple and experiments are conducted on very small datasets. For example, Srivihok and Sukonmanee [18] developed a personalization travel agent using reinforcement learning to explore personal interests by maximizing a reward to the item that interests the user and awarding a penalty to the items that do not interest the user. Schiaffino and Amandi [19] proposed a hybrid expert-software agent named Traveller, combining collaborative filtering with content-based recommendation methods to recommend travel tours. These early works largely aimed at developing the prototypes of recommendation systems, rather than employing big data analytics to discover unique patterns. Recently, benefiting from the accessibility of rich user-generated data collected by the website of e-travel agencies, researchers started to analyze large real travel datasets and developed more-sophisticated models to improve the recommendation quality. Liu, Ge, Li, Chen and Xiong [9] developed a Tourist-Area-Season topic model to capture temporal-spatial correlation in the process of designing a travel package, which is based on the assumption that users have different travel interests in different seasons and the landscapes incorporated in a travel package are caused by travel topics and areas. Considering the relatively higher financial and time cost of travel products, Ge, Liu, Xiong, Tuzhilin and Chen [10] developed a cost-aware latent factor approach for travel-package recommendations by considering both the travel cost and tourists’ interests. Subsequently, Tan, Liu, Chen, Xiong and Wu [7] proposed an open Object-oriented recommendation framework through representing multiple types of additional context information as feature-value pairs and modeling users’ travel interests as topic distributions over the feature-value pairs. Despite various recommendation approaches, there remains an open field in considering and analyzing social influence in the behavior of co-travelers. As examined in previous studies [4, 15, 16], people like to travel with friends and are more willing to trust travel suggestions from their peers, rather than from marketing messages. Thus, it is potentially effective to consider social influence in co-travel behavior for travel-package recommendations.

## 2.2 Social recommendations

Social recommendations refer to incorporating social influence to enhance the performance of recommendations as a successful means of utilizing additional information sources to handle the data sparseness problem [13, 20, 21]. Leveraging the information of social connection has been widely proved valuable because users are more likely to behave similarly to their friends or are more likely to trust their friends through a word-of-mouth influence. In terms of methods in social recommendations, the most popular approach is latent factor models such as low-rank matrix factorization methods with social regularization, assuming that similarity between users is quantified with a numerical value representing the level of trust. Each user’s rating profile should be as similar as possible to the weighted average of friends’ rating profiles [13, 22-24]. The value of trust can be defined in different ways, such as the count of common friends, the count of co-selection behaviors and so on. Moreover, another method of inferring domain-specific trust circles proposed by Yang et al. (2012) is based on the assumption that users trust different circles of friends for different categories of products, which helps to achieve higher recommendation performance compared with methods considering no category difference. In addition, other methods for social recommendations include graph-based collaborative filtering [25], a Bayesian approach (Yang et al. 2013), and a diffusion-based method [26] These methods all construct a network by leveraging the social connection between users to generate better rankings of recommended items, possibly achieving better recommendation accuracy with a higher expense of computational cost.

Unlike existing works about social recommendations, we focus on investigating the effect of different social relationship types on travel behavior. People like to travel to different places and join different activities with different types of friends. For example, you will not invite a normal colleague for romantic island travel when your girlfriend or boyfriend is the first choice. Concerning adventurous activities such as camping and rock climbing, online friends with common interests in most cases might be a better choice than are family members. Therefore, in this paper, we model the joint effect of relationship type and travel preference in affecting people’s choices of travel packages.

#

## 2.3 Topic models

Topic models have received much attention in recent years. The models originate from document analysis and are then applied to many areas. Topic models usually assume that documents or other textual contents are a mixture of latent topics, which are described by a mixture of a bag of words [27]. Originally, Latent Dirichlet Allocation (LDA), as the most classical topic model, is used to model the generation process of a document which is seen as a bag of words [28]. In recent years, researchers began considering the citation relationships between documents to capture better the topical influence in citation networks. Nallapati, Ahmed, Xing and Cohen [29] proposed two models, Pairwise-Link-LDA and Link-PLAS-LDA, to jointly model text and citations in a framework of topic modeling. Then, the model of Citation-LDA [30] was advanced, which facilitates the discovery of individual research topics and theme evolution from multiple related topics. In our work, co-travel behavior is similar to a citation relationship except that studies in citation analysis assume that citations are purely caused by topical relevance; however, in our case, co-travel behavior among friends is jointly determined by the attraction of travel topics and social relationship types.

Recently, topic models have been successfully applied to the field of recommendations [6, 31]. To address the complexity of Point-of-interest recommendations, a topic and location aware recommender system was developed by exploiting associated textual and context information [31]. Additionally, Wang and Blei [32] combined topic modeling with collaborative filtering to recommend scientific articles. Moreover, researchers extended topic models to leverage social influence in social networks [33-35]. However, a lack of research exists on discriminating the social influence of differing relationship types from topic models, a topic addressed in this paper.

## 3 Problem Definition

In this section, we initially introduce several necessary concepts and then formulate the problem of travel-package recommendations with a labeled social network.

Let U denote the set of users, P denote the set of travel packages, and $T { = } \{ ( u , p ) \}$ be a set of observed travel records in which each record $\textstyle ( u , \ p )$ represents a trip of user $u \in U$ on travel-package $p \in P$ . For each record $( u , p ) \in T$ , we define a rating score, score $( u , p ) { = } 1$ . From the observed travel records, we can extract each user’s traveled packages, called individual travel history,

as defined in Definition 1.

Definition 1 (individual travel history): A user’s individual travel history refers to the set of travel packages selected by the user in a period. We denote individual travel history of user u as $P _ { u }$ , in which for any $p \in P _ { u } ,$ , there exists a record $( u , p ) \in T$

As is often true, users usually travel with various types of friends or relatives. The behavior that two users have both selected a package is called a co-travel. Noting that the existence of a co-travel between a pair of users does not guarantee that the two users travel together at the same time because some packages contain several travel groups during a period and these two users might travel in different groups. Likewise, we define co-travelers for a user in Definition 2. To discriminate the social relationship types between pairs of co-travelers, a labeled social network is defined in Definition 3.

Definition 2 (co-travelers): For a user u, the travelers who have at least one co-travel behavior with u are defined as its co-travelers. We denote a list of co-travelers of user u as $C _ { u }$ , in which for any user $v \in C _ { u }$ , there exists at least one package p such that $( u , p ) \in T$ and $( v , p ) \in T$ . Note that if user u co-traveled more than once with user v, then user v will repeatedly occur in the co-traveler list of user u and the occurrences of user v equal the count of co-travels between them.

Definition 3 (A Labeled Social Network): A labeled social network is a social network with a label of social relationship type on each edge, denoted as G (U, E, R), where E is a set of social connections between users in U and R is a set of social relationship types for social connections in E. Social relationship types include, for example, colleague, schoolmate, online friend, real friend (offline friend), and relative.

Given a labeled social network, we can define the relationship type of a co-travel. For user u and a co-traveler of user u, v, the relationship type of their co-travel is defined as the social relationship type between user u and v if they are socially connected in a social network, and the type is defined as non-social co-traveler if they are not. Therefore, the relationship types of co-travelers are varied from social relationships such as colleague, schoolmate, lover, and online friend to non-social co-traveler.

Based on the above definitions, we define the task of travel-package recommendations with a labeled social network as follows.

Travel-package recommendation task with a labeled social network. Given observed travel records of $T ^ { t r a i n } = \{ ( u , p ) \}$ and a labeled social network G (U, E, R), the goal of this paper is to predict score $( u , ~ p )$ for each unobserved user and package pair $( u , ~ p )$ and generate a top-K recommendation list for each user u, described as follows.

$$
\begin{array}{c} f \colon \left(u, T ^ {t r a i n}, G (U, E, R)\right) \to \quad \text {recommendation} \quad \text {list} \quad P \colon \quad s c o r e (p _ {i}) \geq \dots s c o r e (p _ {j}) \geq \\ s c o r e (p _ {k}) \geq \dots \end{array}
$$

where ?????????? ${ \bf \langle } p _ { j } ) \geq s c o r e ( p _ { k } )$ indicates that user u shows a higher preference toward package $p _ { j }$ than toward package $p _ { k }$

## 4 Dataset Analysis

In this section, we provide a description of a real travel dataset and highlight findings through basic statistical analysis, which yields hints for later model construction.

The travel dataset comes from a newly developed China tourism company set up in 2009, which operates through an e-commerce platform embedded with a social network of travelers. Its mode of social networking and traveling largely promotes its popularity among travelers, reaching a level of over one million registered users and an average of two thousand travel activities per week. In this paper, we extract a five-year dataset from 2010 to 2014 consisting of 10,812 travelers, 2,369 packages and 68,786 travel records, ensuring that each user has at least two travel records with one travel record for testing and at least one for training. In this travel dataset, the packages are classified into 7 categories including deep travel, outdoor activity, leisure travel, photography, sightseeing, party, and salon. Table 1 lists the number of packages, percentage of packages in each category over the total number of packages, average cost, and average participants for each category of packages. These figures suggest that packages in the category of deep travel are the most expensive on average, whereas packages of party or salon are the cheapest but have the highest number of participants on average. Strictly speaking, packages in the categories of party or salon do not refer to travel or trips outside but rather to parties between travelers or speeches and lectures about experiences and knowledge of travel. However, we incorporate them into the recommendation system because these packages are very important to increase registered users of the social networking platforms and increase interactions among users.

The social network of travelers is formed by adding social connection between friends and labeling friends into groups according to social relationship types. On average, each user has approximately 24 friends, and the friends are grouped into eight categories in this dataset, namely online friend (OF), real friend (RF), travel acquaintance (TA), schoolmate (S), colleague (C), fellow townsman (FT), relative (R) and other (O), as listed in Table 2. Here, real friend (RF) means friend known in real life, travel acquaintance (TA) refers to a type of social connection between users who know one another through participating in travel activities of the travel agency, and fellow townsman (FT) means a type of social connection between users who have the same hometown.

With a statistical analysis of the dataset, we discovered some unique characteristics as shown below:

1) Extreme sparseness. Each user has only selected an average of approximately 6 travel packages and merely 0.27% entries of the user-package matrix are non-zero. Over 60% of users have only 2 or 3 travel records, and only 4% of users have more than 20 travel records. Such sparseness makes it difficult to find similar users if we only utilize the user-package matrix with traditional collaborative filtering methods [9]. However, social information is much more plentiful. As shown in Table 3, both the average number of friends and that of co-travelers are much higher than the number of travel records for each group of users. For example, users with only 2 or 3 travel records have approximately 11 friends and 93 co-travelers on average. Thus, it is promising to develop algorithms effectively leveraging social information to tackle the sparseness problem.

2) Effect of social influence. Social influence occurs when one’s options, emotions and behaviors are affected by others in forms such as compliance and conformity [11]. To quantify the effect of social influence, we test whether a user will be more likely to select a package as more and more of the user’s friends select the package. To be more specific, let $P _ { u }$ denote the set of packages traveled by user u and $P _ { F _ { u } } ^ { n }$ denotes the set of packages, each of which is selected by n friends of user u. Then, we define proportion $\begin{array} { r } { \mathsf { p } ( u , n ) = \frac { | P _ { u } \cap P _ { F _ { u } } ^ { n } | } { | P _ { F _ { u } } ^ { n } | } , } \end{array}$ , which is the likelihood that user u selects a package among those selected by n friends of u. Furthermore, to consider the social relationship type specifically, we denote $P _ { F _ { u } ^ { R } } ^ { n }$ as the set of packages, each of which is selected by user u’s n friends of relationship type R. Thus, the selection proportion of user u in terms of relationship R is defined as $\begin{array} { r } { \mathsf { p } ( u , R , n ) = } \end{array}$ $\frac { | P _ { u } \cap P _ { F _ { u } ^ { R } } ^ { n } | } { | P _ { F _ { u } ^ { R } } ^ { n } | }$ . After averaging the selection proportion across all users, we plot a graph in Figure 2, which demonstrates that users’ selection likelihood of a package is positively correlated to the number of friends selecting the package, as shown by the line labeled with social connection increases with the number of friends. Thus, it seems promising to leverage social influence to enhance travel-package recommendations because users tend to select packages selected by their friends and such occurrence of co-travel behavior indicates similarity of their travel interests. Moreover, the positive effect of relationship types such as colleague, schoolmate and travel acquaintance are much stronger than that of online friend, indicating the necessity of discriminating the influence of different relationship types.

3) Inter-relationship of travel topic and co-travel relationship type. In daily life, we tend to engage in different activities with different types of friends. For example, we prefer to watch movies with lovers and discuss studies with our schoolmates. Similarly, we assume that travelers of different social relationship types tend to select packages of different travel topics. To demonstrate this selection pattern, we use categories of travel packages in the travel dataset as a measure of travel topics and describe each relationship type as a bag of package categories selected by pairs of co-travelers of this relationship type. Then, we employ TF-IDF to measure the importance of package category in representing each relationship type of co-travels. TF-IDF is a measure used in information retrieval to measure the importance of a term in representing the content of a document, defined as the multiplication of each term’s frequency (TF) with the inverse document frequency (IDF) to penalize common terms [36]. In this paper, we consider each relationship type of co-travelers a document, and package categories terms. Thus, the higher the TF-IDF value of a package category specific to a relationship type, the stronger preference this relationship type of travelers has. As shown in Figure 3, the TF-IDF values of package categories vary with social relationship types. For example, colleagues show a strong preference for parties, whereas online friends are keen on outdoor photography, thus suggesting that the travel topics and social relationship types are both important and that they should be considered simultaneously in modeling co-travel behavior.

## 5 SocoLDA

In this section, we propose a probabilistic topic model called socoLDA for describing user’ travel interests. We choose a topic model because it can represent users’ travel interests in a topic space. Then, the similarity between users can be computed, making it possible to generate recommendation lists in the framework of user-based collaborative filtering [7, 17]. Based on the findings provided in Section 4, we exploit social influence in co-travels to augment the information used for mining users travel interests instead of only using the individual historical travel record as was done in previous works [7, 9]. In the following, we will first introduce the modeling of socoLDA, then give the model inference by Gibbs sampling, and finally present the methods of topic analysis.

## 5.1 Modeling

The proposed model is designed to capture users’ travel interests by leveraging information from two aspects. The first is from individual travel behavior, which means that if a user often travels on packages of certain travel topics such as mountain climbing, then it is reasonable to predict that the user has an interest in climbing mountains. The second is from social co-travel behavior, which means that if a user always travels with a certain circle of friends who have strong interests in deep travel, the user might have an underlying interest of deep travel because similar friends tend to flock together or gradually develop similar interests due to the effect of social influence [11]. Thus, this user is likely to travel on packages of deep travel some day in the future, although no such travel records occurred previously. In addition, the model attempts to capture the joint effect of travel topics and relationship types on co-travel behaviors because people prefer to participate in different types of activities with different types of friends. For instance, people like to go on a deep travel far away with real friends whereas they tend to travel together with online friends for nearby activities such as hiking and camping. Therefore, the co-travel behavior is determined based on both the attraction of travel topics and the influence of relationship types in the proposed model.

To fulfill the purposes above, socoLDA jointly models the generation process of users’ individual travel history and co-travelers to enhance the representation of travel interests by leveraging social influence of co-travel behaviors. Analogous to the traditional LDA considering each article as a document with words as tokens, socoLDA models each user as a document with packages and co-travelers as two types of tokens. The graphical representation of socoLDA is displayed in Figure 4 and its corresponding descriptions of notations are shown in Table 4.

A basic analysis of Figure 4 uncovers that user-topic distribution ??, as a representation of users’ travel interests, is correlated with both z and x, namely the topic assignments of packages in an individual travel history, and the topic assignments of co-travelers, separately. More specifically, a user will be predicted to have strong interests in topic K if the user has traveled many packages on topic K or if the user’s co-travelers have strong interests in topic K. This prediction demonstrates that the proposed model is able to capture the social influence of co-travelers iteratively by considering a user’s travel interests affected by the user’s co-travelers’ travel interests.

Next, we introduce the detailed generation process of socoLDA as represented in Figure 5. For the generation of individual travel history, each user is viewed as a mixture of latent topics from which packages are drawn, similar to LDA [28]. As shown in the left part of Figure 4, for the $m ^ { t h }$ user, first a multinomial topic distribution $\theta _ { m }$ is drawn from its Dirichlet prior ??. Then, for the $n ^ { t h }$ package selected by the $m ^ { t h }$ user, a travel topic $z _ { m , n }$ is generated from $\theta _ { m }$ . According to the generated topic $z _ { m , n }$ , a package $p _ { m , n } .$ , is drawn from multinomial topic-package distribution $\varphi _ { z _ { m , n } }$

For the generation of co-travelers, the generation process is more complex. Different users have a different mixture relationship type of co-travelers, including friends with social connections depicted by the travelers’ social network and a part of non-social co-travelers. For example, some people are more likely to travel with family members whereas some others prefer to travel with online friends. Therefore, for each user, we use a multinomial distribution ?? to model different mixtures of relationship types. The type of non-social co-traveler is included as a type of implicit social influence in co-travel behaviors. The generation of a co-traveler is jointly determined by the attraction of a travel topic and a relationship type of social influence. To be more specific, for the $m ^ { t h }$ user, a multinomial relationship type distribution $\sigma _ { m }$ is drawn from its Dirichlet prior $\gamma .$ . Then, for the $l ^ { \mathrm { t h } }$ co-traveler of the $m ^ { t h }$ user, a type of social influence $r _ { m , l }$ is drawn from multinomial $\sigma _ { m }$ and an attractive topic $x _ { m , l }$ is drawn from the user’s topic distribution $\theta _ { m }$ . Finally, based on the attractive topic $x _ { m , l }$ and the social relationship type $r _ { m , l }$ , a co-traveler $f _ { m , l }$ is drawn from user distribution $\pi _ { x _ { m , l } , r _ { m , l } } .$

## 5.2 Inference of socoLDA

For parameter estimation of socoLDA, we apply collapsed Gibbs Sampling for approximate inference, given that closed forms of exact inference is intractable [28, 37]. The variables we must sample are $z _ { m , p }$ and $x _ { m , l }$ . We conclude the sampling equations as shown in Equations (1) and (2) and the process of derivations can be seen in Appendix. Here, $c _ { z , m , p }$ means the count of package ?? assigned to topic z in the individual travel history of the $m ^ { t h }$ user. $d _ { x , m , r , f }$ means the count of co-traveler f assigned to topic x and relationship type r among the co-travelers of the $m ^ { t h }$ user. $c _ { z , m , p } ^ { - ( m , n ) }$ denotes the count of package ?? assigned to topic $z$ in the individual travel history of the $m ^ { t h }$ user excluding the $n ^ { t h }$ package, and $d _ { x , m , r , f } ^ { - ( m , l ) }$ has the same meaning as $d _ { x , m , r , f }$ except for the exclusion of the $l ^ { t h }$ co-traveler of the $m ^ { t h }$ user.

$$
\mathrm{p} (z _ {m, n} | z _ {- (m, n)}, p, x, r, f, \alpha , \beta , \gamma , \varepsilon) \propto \frac {(c _ {z _ {m , n} , m , *} ^ {- (m , n)} + d _ {z _ {m , n} , m , * , *} + \alpha_ {z _ {m , n}}) (c _ {z _ {m , n} , *} ^ {- (m , n)} p _ {m , n} + \beta_ {p _ {m , n}})}{c _ {z _ {m , n} , * , *} ^ {- (m , n)} + \sum_ {i = 1} ^ {V} \beta_ {i}}\tag{1}
$$

$$
\mathsf {p} (x _ {m, l} | x _ {- (m, l)}, p, z, r, f, \alpha , \beta , \gamma , \varepsilon) \propto \frac {(c _ {x _ {m , l} , m , *} + d _ {x _ {m , l} , m , * , *} ^ {- (m , l)} + \alpha_ {x _ {m , l}}) (d _ {* , m , r _ {m , l} , *} ^ {- (m , l)} + \gamma_ {r _ {m , l}}) (d _ {x _ {m , l} , *} ^ {- (m , l)} , f _ {m , l} + \varepsilon_ {f _ {m , l}})}{d _ {x _ {m , l} , *} ^ {- (m , l)} , r _ {m , l} , *} + \sum_ {l = 1} ^ {M} \varepsilon_ {l}\tag{2}
$$

Collecting samples after the burn-in time, we can obtain expectation estimations of parameters as follows.

$$
\theta_ {\mathrm{z|m}} = \frac {c _ {\mathrm{z,m,*}} + d _ {\mathrm{z,m,*,*}} + \alpha_ {\mathrm{z}}}{c _ {* , \mathrm{m,*}} + d _ {* , \mathrm{m,*,*}} + \sum_ {\mathrm{k=1}} ^ {\mathrm{K}} \alpha_ {\mathrm{k}}}\tag{3}
$$

$$
\sigma_ {\mathrm{r|m}} = \frac {d _ {* , \mathrm{m,r,*}} + \gamma_ {\mathrm{r}}}{d _ {* , \mathrm{m,*,*}} + \sum_ {\mathrm{i=1}} ^ {\mathrm{R}} \gamma_ {\mathrm{i}}}\tag{4}
$$

$$
\varphi_ {\mathrm{p} | \mathrm{z}} = \frac {c _ {\mathrm{z} , * , \mathrm{p}} + \beta_ {\mathrm{p}}}{c _ {\mathrm{z} , * , *} + \sum_ {\mathrm{n} = 1} ^ {\mathrm{V}} \beta_ {\mathrm{n}}}\tag{5}
$$

$$
\pi_ {\mathrm{f|x,r}} = \frac {d _ {\mathrm{x,*,r,f}} + \varepsilon_ {\mathrm{f}}}{d _ {\mathrm{x,*,r,*}} + \sum_ {\mathrm{l=1}} ^ {\mathrm{M}} \varepsilon_ {\mathrm{l}}}\tag{6}
$$

A glimpse of parameter estimations in Equations from (3) to (6) highlights the ability of our proposed socoLDA in incorporating findings and purposes in model designing. For example, the estimated user-topic distribution $\theta _ { z | m }$ integrates the count of topics assigned for packages in individual travel history and that for co-travelers, namely the sum of $c _ { z , m , \ l }$ <sub>∗</sub> and $d _ { z , m , * , * }$ separately, indicating that socoLDA surely incorporates information in two aspects of individual travel behavior and co-travel behavior to model a user’s travel interests. The topic-package distribution $\varphi _ { p | z }$ yields a mathematical representation of travel topics. In addition, the topic and relationship type-co-traveler distribution $\pi _ { f | x , r }$ illustrates how travel topics and relationship types jointly affect co-travel behavior.

## 5.3 Complexity analysis

Time complexity. The main time cost of socoLDA lies in the collapsed Gibbs Sampling of model inference, including the inference of latent variables x, topics of travel packages, and z, topics of a co-travelers. The time complexity of inferring x in Equation (1) is $\mathcal { O } ( M \bar { N } K )$ , where M is the number of users, $\bar { N }$ is the average number of travel packages selected by the users, and K is the number of topics. Because the travel dataset is very sparse and each user selected only a small part of travel packages, ??<sup>̅</sup> is very small compared with M. Similarly, the time complexity of inferring z in Equation (2) is $\mathcal { O } ( M \bar { L } K )$ , where ??<sup>̅</sup> is the average number of co-travelers of users. ??<sup>̅</sup> also does not scale with

M. Therefore, the time complexity of inferring x and z in each iteration is $\mathcal { O } ( M ( \overline { { { N } } } + \overline { { { L } } } ) K )$ , which is linearly correlated with number of users M.

Space complexity. The memory cost of socoLDA primarily comes from the storage of input information and count matrices needed in inference. The space complexity for input information, including user individual history, co-travelers and relationship types, is $\mathcal { O } ( M ( \overline { { N } } + 2 \overline { { L } } ) K )$ . Moreover, according to Equations (1) and (2), the count matrices include $c _ { z , m , * } , \ c _ { z , * , p } , \ d _ { x , m , * , * } , \ d _ { * , m , r , * }$ <sub>∗</sub> and $d _ { x , * , r , f }$ , and the space complexity for the count matrices is $\mathcal { O } ( ( 2 K + R + K R ) M + V K )$ . Thus, the memory cost is also linearly correlated with the number of users M. This complexity analysis shows that the proposed model is both time and space efficient and can scale to a very large dataset.

## 5.4 Topic analysis and description

The topic-package distribution $\{ \varphi _ { p | z } \}$ , as computed in Equation (5), yields the probability distribution of each topic over packages. To obtain a clearer understanding of what a topic is semantically, we combine the topic-package distribution $\varphi$ with some package-level descriptive information, such as cost, days, and title, to provide a profound topic analysis from the following three aspects, namely finding representative packages, giving a descriptive summarization, and displaying the pattern of topic evolution.

## Topic representative packages

The estimated topic-package distribution $\{ \varphi _ { p | z } \}$ indicates how well a single package ?? represents a topic ??. The ranking of packages based on $\{ \varphi _ { p | z } \}$ essentially provides topic-aware importance of packages in representing a topic. In this sense, the most simple but effective means to catch the basic semantics of a topic is to list topic representative packages (i.e., the packages ranking top for a topic according to $\varphi _ { p | z } )$ combined with their package-level descriptive information to show the topic-level information such as cost, number of days and keywords of travel activities.

## Topic descriptive summarization

To better summarize the topic-level information with a few attributes, we compute the expectations of package-level attributes over the estimated topic-package distribution $\{ \varphi _ { p | z } \}$ . For numerical attributes such as cost and days of travel packages, the corresponding topic-level attribute is computed as Equations (7) and (8). Here, ????????(??) and $d a y s ( p )$ denote the cost and the number of days of package p, separately, and ????????(??) and ????????(??) denote the expected cost and the expected

number of days of topic z, separately.

$$
E [ c o s t (z) ] = \sum_ {p \in P} c o s t (p) \varphi_ {p | z}\tag{7}
$$

$$
E [ d a y s (z) ] = \sum_ {p \in P} d a y s (p) \varphi_ {p | z}\tag{8}
$$

Moreover, we extract topic-level keywords from package titles and summarize the topic by those words with a high expected-frequency of occurrence. Specifically, the word occurrence of word w for topic z over $\{ \varphi _ { p | z } \}$ is computed as Equation 9, where $\# ( w , p )$ is the count of occurrences of word w in the title of package p.

$$
E [ \text { frequency } (z, w) ] = \sum_ {p \in P} \# (w, p) \varphi_ {p | z}\tag{9}
$$

As validated later by experiments, the topic descriptive summarization provides a multi-aspect description for topics with minimal information, making it easy to understand the semantics of topics for managers and decision makers in travel agencies.

## Topic temporal evolution

Travel packages are easily depreciative over time and their popularity is usually correlated with seasonal factors. For travel agencies, it is important to grasp the temporal evolution of topics, thus designing and promoting travel packages of appropriate and popular topics at the right time. We compute the topic temporal distribution (TTD) to illustrate the information [30]. Discrete time case TTD, as shown in Equation (10), is computed as the proportion of accumulated probability of travel packages for a topic z in a period of time t, for example a month. Here, a package’s active duration of time is denoted as ????????(??), and ????????(??) $\cap t \neq \emptyset$ if the period of travel-package p overlaps time period t.

$$
\operatorname * {P r} (t i m e = t | z) = \sum_ {p \in P, t i m e (p) \cap t \neq \emptyset} \varphi_ {p | z}\tag{10}
$$

The topic temporal distribution displays how a topic evolves temporally, indicating whether the topic is popular throughout the year or has seasonal fluctuations and yields essential insights on how travel agencies should market the right travel topics at the right time.

## 6 Recommendation Framework

In this section, we introduce the framework of travel-package recommendation named socoTraveler, which employs socoLDA to represent a user’s travel interests in topic space and to find similar users to generate recommendations with user-based collaborative filtering. SocoTraveler attempts to recommend travel packages intelligently according to travelers’ preference and helps travel agencies increase the efficiency of target marketing and precision marketing. In general, the working process of socoTraveler contains the following three steps:

1) Extract individual travel history and co-travelers for each user and represent user’s travel interests with user-topic distribution $\{ \theta _ { z | m } \}$ estimated by the proposed socoLDA model;

2) Calculate similarity between users based on the estimated user-topic distribution, and generate initial recommendation list according to user-based collaborative filtering;

3) Refine the initial recommendation list by adding new packages that are similar to candidates generated previously by comparing descriptive information of packages.

Because step 1 has been introduced in detail in the previous section, we will only explain the details of steps 2 and 3 in the following.

## 6.1 Generating the initial recommendation list

To find similar users in terms of travel interests, we employ a simple but effective similarity metric, correlation coefficient [6], according to the estimated user-topic distribution $\theta _ { z | m }$ as shown in Equation (3). For user $u _ { a }$ and $u _ { b }$ , their similarity of correlation coefficient is computed by Equation (11), where $\overline { { \theta _ { z } } }$ is the average probability for topic z across all users, and $\theta _ { z | a }$ and $\theta _ { z | b }$ are user-topic distribution for user a and b, separately.

$$
s i m (u _ {a}, u _ {b}) = \frac {\sum_ {z = 1} ^ {K} (\theta_ {z | a} - \overline {{\theta_ {z}}}) (\theta_ {z | b} - \overline {{\theta_ {z}}})}{\sqrt {\sum_ {z = 1} ^ {K} (\theta_ {z | a} - \overline {{\theta_ {z}}}) ^ {2}} \sqrt {\sum_ {z = 1} ^ {K} (\theta_ {z | b} - \overline {{\theta_ {z}}}) ^ {2}}}\tag{11}
$$

Then, based on the idea of user-based collaborative filtering, the rating score user u would assign to package $p$ is computed as the summarization of top-ranked S similar users’ selections of package $p$ weighted by their similarities, as shown in Equation (12), where $s c o r e ( u _ { s } , p )$ is 1 if user $u _ { s }$ has selected package ?? and otherwise 0.

$$
s c o r e (u, p) = \frac {\sum_ {s = 1} ^ {S} s c o r e (u _ {s} , p) \times s i m (u _ {s} , u)}{\sum_ {s = 1} ^ {S} s i m (u _ {s} , u)}\tag{12}
$$

## 6.2 Refining the initial recommendation list

To solve the cold-start problem of new packages, we refine the initial recommendation list by adding new packages similar to the package in the initial recommendation list generated previously.

We employ the package-level textual information, such as package title, to compute similarity between pairs of packages [7]. For a pair of packages $p _ { i }$ and $p _ { j }$ , we denote the set of words occurred in the textual information of packages $p _ { i }$ and $p _ { j }$ as $W _ { p _ { i } }$ and $W _ { p _ { j } } ,$ respectively. Then, the similarity between $p _ { i }$ and $p _ { j }$ is computed based on the Jaccard Coefficient as shown in Equation (13).

$$
s i m (p _ {i}, p _ {j}) = \frac {| W _ {p _ {i}} \cap W _ {p _ {j}} |}{| W _ {p _ {i}} \cup W _ {p _ {j}} |}\tag{13}
$$

Next, based on the top $\mathrm { Q } ,$ most similar packages in the initial recommendation list compute the rating score that user u would assign to a new package $p _ { n e w }$ in Equation (14), where ?????????? $( u , p _ { i } )$ is the score computed by Equation (12) and ?????? $( p _ { i } , p _ { n e w } )$ is the package similarity based on textual descriptions computed by Equation (13).

$$
s c o r e (u, p _ {n e w}) = \frac {\sum_ {i = 1} ^ {Q} s c o r e (u , p _ {i}) \times s i m (p _ {i} , p _ {n e w})}{\sum_ {i = 1} ^ {Q} s i m (p _ {i} , p _ {n e w})}\tag{14}
$$

Ultimately, we add new packages into the initial recommendation list according to the descending order of the score. In addition, we remove packages that are not active and obtain the final recommendation list for each user.

We can see that socoTraveler effectively handles the problem of extreme data sparseness by leveraging social influence of co-travelers, and solves the cold-start problem of new packages. Thus, socoTraveler provides a new approach to recommend travel packages intelligently by combining a topic-aware model with social influence and collaborative filtering.

## 7 Experimental Evaluation

In this section, we conduct experiments to demonstrate the performance of the proposed approach on a real travel dataset. Specifically, we intend to exhibit the following aspects: 1) recommendation performance of the proposed model compared with benchmark methods; 2) topic analysis in terms of representative packages, keyword summarization and temporal evolution; and 3) the co-occurrence analysis of topic and relationship type in affecting co-travel behavior.

## 7.1 Experimental setup

The travel dataset was divided into a training set and a testing set. Each user’s last travel record was added into the testing set and other travel records were used for training. A detailed description of

the training and testing data is listed in

, with 10,812 users in total and 23 new packages traveled by 165 tourists in the testing set.

Benchmark Methods. Given that existing recommendation methods are countless, we choose representative methods as benchmarks for different purposes. First, our model is proposed to consider various social influences. Therefore, social recommendation methods such as SocialMF [28] and Citation-LDA [29] are chosen to compare the effect of different social relationship types. Second, we study the travel-package recommendation problem. Hence, a recommendation method OTM-ORS [7] that has been shown to outperform other travel-package recommendation methods is chosen as benchmark. Third, because our proposed model is a modification of the LDA model, we compare the two. Finally, recommendation methods such as UCF and ICF are selected because they are the most typical methods and our method is an extension based on them. A short description of the benchmark methods follows.

SocialMF: This method is proposed by Jamali and Ester [38]. It is a probabilistic latent factor model with a social regularization incorporating social network information to improve recommendation quality, assuming that users’ latent factors are similar to the weighted average of his friends’ latent factors.

Citation-LDA: This method was proposed by Nallapati, Ahmed, Xing and Cohen [29] to model the writing and citation relationships of research networks. It is based on the assumption that citation is only caused by topical relatedness, a reasonable assumption in citation networks. We modify this model by replacing a paper’s citations with a user’s co-travelers, who are generated because of topical attraction. Thus, compared with socoTraveler, Citation-LDA does not consider specific relationship types.

OTM-ORS: This is a probabilistic topic model developed in the scenario of travel-package recommendations, which considers users and packages objects of feature-value pairs and utilizes the correlation of feature-value pairs for travel recommendations [7]. In addition to the original seven features used in Tan, Liu, Chen, Xiong and Wu [7], we add the features of package category, user location, and user hometown to enhance the recommendation quality of OTM-ORS on our dataset.

LDA-related methods: Both LDA-P and LDA-W are LDA models with different token settings.

Specifically, LDA-P uses package IDs as tokens, whereas LDA-W uses words extracted from package descriptions as tokens. Then, we represent user interests as user-topic distributions learned from LDA methods. For all of the above topic models, we use correlation coefficient to calculate user similarity and generate a recommendation list as is done in the recommendation framework of socoTraveler.

UCF: This method is the baseline of user-based collaborative filtering [17], which employs a user-item matrix to find similar users and recommend items preferred by similar users. We employ the Jaccard Coefficient [39] to compute similarity between users for the binary user-item matrix..

ICF: this method is the baseline of item-based collaborative filtering [40]. The method assumes that users will prefer items similar to those they selected previously. We also employ the Jaccard coefficient [39] to calculate similarity between items based on the user-item selection matrix.

In addition to these benchmark methods, we also compare SocoTraveler with its different variants as described below.

SocoTraveler-related methods: These methods are developed in the framework of socoTraveler with a few variations. They are ST-New without adding new packages, ST-W using words of package descriptions as tokens, ST-S with only socially connected co-travelers and excluding non-social co-travelers, and ST-W-S using words of package descriptions as tokens and excluding non-social co-travelers. Except for the specified differences, all other aspects are kept the same as socoTraveler.

Parameter Setting. For topic models, we set the number of topics as K=100, hyper-parameter $\begin{array} { r } { \alpha = \frac { 5 0 } { K } } \end{array}$ and other hyperparameters as 0.01 [37]. We run Gibbs sampling for 1500 iterations and then estimate the model parameters. For models using words as tokens such as ST-W, ST-W-S and LDA-W, we use a popular word segmentation tool for Chinese words named Ansj<sup>1</sup> to segment the contents of packages into words and then remove stop words and top popular words as done by Zhao, Jiang, Weng, He, Lim, Yan and Li [41]. For user-based collaborative filtering methods, we fix the number of similar users at 1000. For item-based collaborative filtering methods, the number of similar packages is set as 500. Such parameters are selected by experiments to achieve good performance and fixed for a fair comparison.

Evaluation Metrics. We adopt Degree of Agreement (DOA) and Recall@K as evaluation

metrics.

DOA measures the percentage of pairs of packages ranked in the correct order [7, 42]. To measure user-specific $D O A _ { u }$ for user u, we define $N _ { u }$ as the set of packages neither in the training set nor in the testing set of user u, i.e., for any $p \in N _ { u }$ , (u, p) is not in $( T ^ { t r a i n } \cup T ^ { t e s t } )$ , and $Y _ { u }$ as the set of packages in the testing set of user u, i.e., for any $p \in Y _ { u } , ( \mathfrak { u } , \mathfrak { p } )$ is in $T ^ { t e s t }$ . For each pair of package $p _ { i }$ in $Y _ { u }$ and package $p _ { j }$ in $N _ { u } .$ , function ??ℎ?????? $\_ o r d e r _ { u } ( p _ { i } , p _ { j } )$ is 1 if the predicted rank of $p _ { i }$ is greater than $p _ { j }$ , and 0 otherwise. Therefore, $D O A _ { u }$ as defined in Equation (15), measures the degree to which a recommendation list satisfies the preference of an individual user u. In this paper, we employ DOA, the average of $D O A _ { u }$ across all users, to measure the goodness of overall ranking. An ideal ranking list reaches 100% DOA; the higher the value of DOA, the better an algorithm’s ability in ranking items.

$$
D O A _ {u} = \frac {\sum_ {i \in Y _ {u} , j \in N _ {u}} c h e c k \_ o r d e r _ {u} (p _ {i} , p _ {j})}{| Y _ {u} | \times | N _ {u} |}\tag{15}
$$

Recall@K evaluates the ability of recalling packages in a testing set when the size of the recommendation list is K [43]. We first define the measure for user u as ???????? $l l @ K _ { u }$ in Equation (16), where $Y _ { u }$ is defined as the set of packages in the testing set of user u, and $R _ { u } ^ { K }$ is the set of packages recalled in the top-K position of the recommendation list. Here, $R _ { u } ^ { K } \cap Y _ { u }$ means the intersection set of $R _ { u } ^ { K }$ and $Y _ { u }$ . Then, recall@K can be calculated by an average of ????????????@ $K _ { u }$ across all users. The higher the value of recall@K, the better the recommendation algorithm is.

$$
r e c a l l @ K _ {u} = \frac {| R _ {u} ^ {K} \cap Y _ {u} |}{| Y _ {u} |}\tag{16}
$$

## 7.2 Recommendation performance

DOA. The average ranking performances of socoTraveler and related benchmark methods are listed in Table 6, which reveals the following findings.

1) The improvement of socoTraveler over ST-New suggests that considering new packages does enhance recommendation quality and provides an effective solution to the item cold-start problem in the domain of travel-package recommendation.

2) The comparison of ST-S with SocoTraveler tells us that the augmentation of non-social co-travelers significantly enhances recommendation performance by raising DOA from 76.53% to 80.10%, demonstrating that the behavior of non-social co-travel, as a sort of implicit social influence, is an effective indicator of similar travel interests.

3) Surprisingly, using packages as tokens is better than using textual words as tokens, possibly because package descriptions are long, tedious, and noisy with some common words not related to travel interests, whereas packages more accurately capture users’ travel interests overall. The same finding can be concluded from the enhancement of socoTraveler over ST-W and the advantage of LDA-P over LDA-W. The advantage of package tokens is also validated by the fact that compared with UCF, LDA-P performs better, but LDA-W is inferior.

4) The consideration of relationship types is important in modeling co-travel behavior, given that socoTraveler is superior to Citation-LDA, which only considers the attraction of travel topics but ignores the influence of different relationship types.

5) Considering social influence definitely benefits the travel-package recommendations, which can be seen because socoTraveler performs better than do benchmark methods that ignore social influence, such as OTM-ORS, LDA-related methods, UCF, and ICF.

6) SocialMF has not achieved satisfactory performance even considering social connections, possibly because SocialMF considers all social connections, but in fact not all friends share similar travel interests, particularly when a friend list is long. In contrast, socoTraveler utilizes social influence of at least one co-travel, benefiting from the fact that co-travel guarantees similarity of travel interests to some degree.

Recall@K. As shown Figure 6, the comparison of performances measured by recall@K metric is almost the same as that of DOA, suggesting that socoTraveler significantly outperforms all benchmark methods as K increases from 5 to 30. As shown in Figure 6(c), SocialMF performs extremely poorly when K is less than 10 and is superior to collaborative filtering methods such as UCF and ICF when K is greater than 25, but still much lower than the proposed socoTraveler. Varying the size of the training set. To test the effects of varying the size of the training dataset on recommendation performances of socoTraveler, we randomly select 50%, 60%, 70%, 80%, and 90% of travel records as training sets and leave the rest as a testing set. The recommendation performances of socoTraveler compared with existing methods in terms of DOA are listed in Figure 7. The recommendations show that socoTraveler outperforms all existing methods in any size of training sets varying from 50% to 90% and that the advantages of socoTraveler are particularly prominent when the size of a training set becomes small at 50%, demonstrating the ability of the proposed model to address a sparse dataset when users’ travel records are extremely limited. In addition, the recommendation performances of UCF and ICF are extremely poor when the percentage of training set is small at 50%. Figure 8 provides comparison results among different methods in terms of recall@K when the percentage of training set is at 50%. The recall@K comparison for other sizes of training sets has tendencies similar to those shown in Figure 8.

Computational performance. To compare the computational performances of different methods, we run all methods on the same platform and show the time and memory costs (including costs for building models and generating recommendation lists) of different methods in Figure 9. Among the variants of SocoTraveler algorithms, ST-S is the most efficient because it uses the least amount of information; it has comparable running time with ICF and LDA-P. ICF runs fast because it computes the similarity between items instead of users and because the number of items is much smaller than is that of users. LDA-P only uses package ID. ST-W is the most time-consuming algorithm because it uses all of the words of each package description instead of package ID. ST-W-S runs faster than ST-W because ST-W uses information of all co-travelers, but ST-W-S uses only socially connected co-travelers. SocoTraveler has comparable running time with SocialMF and Citation-LDA, which is reasonable because they use similar information and they are all topic models. OTM-ORS runs faster because it only utilizes feature-value information of packages without considering social information, but its running time remains of the same magnitude as SocoTraveler’s. For the memory costs, there is not a large difference among all of the algorithms. SocoTraveler has a bit higher memory cost primarily due to the utilization of social information. Overall, running time and memory cost of socoTraveler are comparable with benchmarks, suggesting the proposed approach is efficient and effective for practical use. Furthermore, because user interests are relatively stable in a period, we need only regularly update the distribution of user-interests offline, for example, every month, and generate recommendation lists online based on similar users’ travel history. Thus, socoTraveler is practical to use in a real personalized recommendation system.

## 7.3 Topic analysis

In this subsection, we present the results of topic analysis based on socoLDA. Given a topic, we list its top representative packages according to the estimated topic-package distribution, provide an overall descriptive summarization of the topic, and plot its temporal evolution in several years to understand better both the semantics of a topic and how it changes over time.

## Topic representative packages

In Table 7, we list top 3 representative packages for topics 3, 13, and 48, including package title, cost, and the number of travel days. The top effect packages for topic 3 were all centered on a prairie tour to the northwest of China with relatively high cost and a long travel period. Topic 13 primarily focuses on hydrophilic travel packages for waterscape scenery, river rafting, and some sort of water activities, whereas topic 48 concentrated on climbing famous mountains, such as Mount Qiyun, Wuyi and so on.

## Topic descriptive summarization

Using the estimated topic-package distribution φ̂ and package information, we obtain a descriptive summarization of topics including top-ranked keywords extracted from package titles, the expectation of cost, the expectation of the number of days, and manually labeled topic name, as listed in Table 8. Among the five topics, topic 3 of the northwest prairie tour has the highest cost and longest travel days, with approximately 7 days of travel at the cost of over 3000. However, topic 11 of suburb night-walk is nearly free, with only one day, approximately. Some topics are designed for a specific season, for example topic 90 of autumn hiking, and some topics are for specific regions and terrains, for example northwest grassland in topic 3, mountains in topic 48 and rivers in topic 11. This pattern demonstrates that topic is very effective in clustering similar packages to better capture users’ travel interests.

## Topic temporal evolution

Figure 10 plots temporal evolution for the five topics in Table 8 from 2012 to 2014, suggesting that some topics, such as topics 11 and 90, are only popular in several months within a year, whereas other topics such as topics 3 and 48 are attractive over several years. Additionally, some topics are seasonal, for example topic 13 (hydrophilic tour) is largely for summer and topic 90 (autumn hiking) for autumn, whereas mountain climbing topics are popular throughout the year.

#

## 7.4 Travel topic and co-travel relationship type

In this subsection, we uncover what relationship type of co-travelers prefers to travel what type of travel topics. Based on the model of socoLDA, each user can be described by a collection of co-travelers with specified relationship types and travel topics. We exploit Pointwise Mutual Information (PMI) [44] to uncover the co-occurrence pattern of travel topics and relationship types in co-travel behavior. Given a pair of travel topic x and relationship type r, PMI (x, r) quantifies the discrepancy between the probability of their joint coincidence and their individual distributions assuming independence, as defined in Equation (17). For comparison, we employ normalized Pairwise Mutual Information (nPMI), as defined in Equation (18). The nPMI is normalized between [−1, +1], resulting in −1 for never occurring together, 0 for mutual independence, and +1 for complete co-occurrence.

$$
\mathrm{PMI} (\mathbf {x}, \mathbf {r}) = \log \frac {P (x , r)}{P (x) P (r)}\tag{17}
$$

$$
\mathrm{nPMI} (\mathrm{x}, \mathrm{r}) = \frac {\mathrm{PMI} (\mathrm{x} , \mathrm{r})}{- \log (P (x , r))}\tag{18}
$$

In summary, we list in Table 9 the top 3 travel topics for each relationship type measured by nPMI. From the value of nPMI and descriptive summarization of travel topics, we highlight some interesting points below:

1) The nPMI value for real friend is very high compared with other relationship types, whereas the nPMI for non-social co-traveler is the lowest, with only approximately 0.01, indicating that travelers with a social connection, particularly friends in real life, have a higher chance of traveling together.

2) Online friends prefer outdoor activities nearby with relatively low cost and a short number of days. The type of adventurous activities such as camping, night-walk, and mountain traversing wins popularity over online friends.

3) Real friends tend to travel to places in more distant provinces and enjoy diversified sceneries such as sea and prairie. Moreover, the travel cost is much higher and the number of days is greater. These differences are possibly caused by the fact that people prefer to travel far away with friends they know in real life rather than with online friends.

4) Travel acquaintances are keen on activities such as hiking on an ancient road, day or night, which often takes approximately one day, indicating that the short trip is a good approach to making new friends.

5) The travel topics for schoolmates, colleagues, fellow-townsmen, and relatives are varied, including deep travel to distant places and leisure travels nearby. Moreover, colleagues prefer salons and parties to gaining knowledge from travel and sharing travel experiences.

## 8 Discussion

In this section, we present further discussion on the following three points. The first point lies in the generalizability of the proposed approach, namely whether it can be applied to other recommendation scenarios such as product recommendations. We then discuss the contribution of our research to big data analytics. Finally, we discuss a multiplicity of real-world relationship types and how our model can address this issue.

## Generalizability of the proposed approach

This paper proposed a recommendation framework, namely socoTraveler, based on a topic model, socoLDA, leveraging the social influence of co-travelers to mitigate the sparseness problem of a travel dataset. Although socoTraveler is only evaluated on a travel dataset, the proposed approach can be applied to various scenarios of item recommendations with implicit feedback in which social relationships between users are available. Item recommendations with implicit feedback [45] is a crucial area of research in recommendations because explicit feedback is not always available and numerous cases in the real world have only implicit feedback, such as clicking a web page, downloading mobile apps, consumption of products, and so on. The characteristic that implicit feedback contains only positive feedback but no negative feedback poses a great challenge to personalized recommendations [14, 45]. The proposed model socoLDA is capable of handling datasets with implicit feedback, benefiting from the fact that only positive tokens are needed in the topic model. To adapt to different scenarios of item recommendations with implicit feedback, we must replace packages with items and reset the document of co-travelers according to a specific recommended scenario. Specifically, if co-selection behavior is a potential means of social influence, corresponding to co-travel behavior in travel-package recommendations, we can set the document of co-travelers as co-selectors, users selecting same items. However, if co-selection behavior is easy and prevalent, such as co-buying behavior of the same product, it might be wiser to employ users’ friends as tokens. Therefore, the proposed model can be broadly applied to scenarios of item recommendations with implicit feedback through minor adjustment of settings, demonstrating prominent generalizability of the proposed model for personalized item recommendations.

## Contribution to big data analytics

Personalized recommendation systems, as an active and important field in big data analytics, have been adopted by leading e-commerce vendors such as Amazon and eBay on their innovative and highly scalable e-commerce platforms. Successful recommendation systems are able to create business value and generate huge effects [3]. To enhance further the recommendation quality in e-tourism, we collect a rich travel dataset containing both individual travel history and information on social relationships between users. Data can be “big” in different dimensions such as volume, velocity and variety [1]. E-tourism platforms collect a rich and large volume of user-generated data every day. The variety lies in the combination not only of user and travel-package information, user behavioral and social network information but also of information of different relationship types, providing us an advantage to analyze distinct co-travel behavior of specific relationship types and develop innovative social recommenders leveraging heterogeneous social influence for better recommendations. Furthermore, time complexity analysis shows that the proposed model is time-efficient and can scale to a large dataset. Therefore, our research does contribute to big data analytics in proposing a unified recommendation model integrating various types of information including user behavior, social links, and relationship types to generate a personalized recommendation list.

## Multiplicity of relationship types

Unlike existing studies on social recommendations, our research focuses on analyzing the role of relationship types in shaping human behavior. Due to the limitation of the collected dataset, we only consider a single relationship type for a link in the experimental evaluation. However, the relationship types for a link can be multiple. For example, two classmates can also be lovers in the real world. Actually, our model is capable of handling a multiplicity of relationship types with minor adjustments. There are two possible ways to accomplish that. One approach is to maintain the multiplicity of relationship types and repeatedly add the tokens of co-travelers for each possible relationship type. The other approach is to rank the importance of the relationship types and choose relationship type at a high level to represent the relationship type between users. For instance, the type of lover should rank higher than the type of classmate, thus lover is selected as the representative type for the link. In this sense, the proposed model can be easily used to address a multiplicity of relationship types.

## 9 Conclusions and Future Work

In this paper, we study a new problem of travel-package recommendation leveraging social influence of different types of co-travel behaviors. Unlike existing studies in social recommendations, our work focuses on discriminating the social influence of different social relationship types of co-travelers. To fulfill the task of travel-package recommendations with a labeled social network, we first develop a model of socoLDA jointly incorporating individual travel history and co-travelers to represent users’ travel interests in a topic space. Then, based on the proposed model, a recommendation framework named socoTraveler is developed to generate a recommendation list for each user. With an in-depth analysis of the dataset and experimental results, we highlight interesting findings and practical implications as follows.

First, the consideration of social influence is useful in enhancing the quality of travel-package recommendations. Experimental results on a real travel dataset validate that socoTraveler significantly outperforms other existing methods, benefiting from socoLDA’s ability to represent users’ travel interests by jointly exploiting the effect of travel topic and relationship type in affecting co-travel behavior. Practically speaking, this finding also suggests that it is wise for travel agencies to develop a social networking platform for customers to take advantage of social influence and electronic “word of mouth” in business marketing.

Second, we identify a positive correlation between the likelihood that a user selects a package and the number of friends who select the package. Moreover, the strength of the positive correlation varies by type of friend. For example, colleagues and schoolmates have a stronger effect than do online friends.

Third, discriminating social influence of different types of co-travelers is necessary and effective because different types of travelers show different preferences in travel topics. For example, online friends prefer leisure travels nearby with short days, whereas real friends prefer to travel far away for longer days.

Finally, this paper presents some methods of topic analysis, including representative packages, descriptive summarization and temporal evolution, which provides an effective and convenient means for decision makers of travel agencies to understand the sematic meanings of travel topics, target important packages, and promote the right packages at the right time.

In summary, this paper presents a new angle of leveraging social influence into recommendations. By discriminating social influence of different social relationship types, we demonstrate important findings that different types of friends tend to prefer packages of different travel topics. From a broader perspective, our work enriches big data analytic methods and recommendation methods b proposing a model incorporating various types of information and integrating it into a recommendation framework.

In our future research, we attempt to apply the findings to other domains of recommendations, such as movie recommendations, location recommendations, and so on. Using movie recommendations as an example, it is probable that different types of friends have differing preferences in categories of movies. For example, people prefer to watch romantic movies with lovers and action movies with male friends. Furthermore, another direction of future research is to design methods capable of simultaneously identifying relationship types and recommending items according to preferences, which is important for social networks that still lack explicit labels for relationship types.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China under Grant No. 71272029, 71490724, 71110107027 and 71432004, the Beijing Municipal Natural Science Foundation under No. 4152026, and the Major Program of National Social Science Foundation of China under Grant No. 13&ZD184.

## Appendix

To illustrate, we derive the sampling equation of $x _ { m , l }$ as an example. The sampling equation of $z _ { m , n }$ can be derived similarly.

$$
\begin{array}{r l} & p \big (x _ {m, l} | x _ {- (m, l)}, p, z, r, f, \alpha , \beta , \gamma , \varepsilon \big) \\ & \propto p (p, f, r, z, x | \alpha , \beta , \gamma , \varepsilon) = \int \int \int \int p (p, f, r, z, x, \theta , \varphi , \sigma , \pi | \alpha , \beta , \gamma , \varepsilon) d \vartheta d \varphi d \sigma d \pi \\ & = \int p (\theta | \alpha) p (z | \vartheta) p (x | \theta) d \theta \int p (\varphi | \beta) p (p | \varphi , z) d \varphi \int p (\sigma | \gamma) p (r | \sigma) d \sigma \int p (\pi | \varepsilon) p (\varepsilon | \pi , x, r) d \pi \end{array}
$$

Then, because the second and third integrals do not contain ?? , we eliminate them and obtain $x _ { m , l }$

the following formulas.

$$
\begin{array}{r l} & {\propto \int p (\theta | \alpha) p (z | \vartheta) p (x | \theta) d \theta \int p (\pi | \varepsilon) p (\varepsilon | \pi , x, r) d \pi} \\ & {= \int \prod_ {m = 1} ^ {M} \frac {\Gamma (\sum_ {k = 1} ^ {K} \alpha_ {k})}{\prod_ {k = 1} ^ {K} \Gamma (\alpha_ {k})} \prod_ {k = 1} ^ {K} \theta_ {m, k} ^ {\alpha_ {k} - 1} \prod_ {m = 1} ^ {M} \prod_ {n = 1} ^ {N _ {m}} \theta_ {z _ {m, n}} \prod_ {m = 1} ^ {M} \prod_ {l = 1} ^ {L _ {m}} \theta_ {x _ {m, l}} d \theta} \\ & {\times \int \prod_ {k = 1} ^ {K} \prod_ {r = 1} ^ {R} \frac {\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f})}{\prod_ {f = 1} ^ {M} \Gamma (\varepsilon_ {f})} \pi_ {k, r, f} ^ {\varepsilon_ {f} - 1} \prod_ {m = 1} ^ {M} \prod_ {l = 1} ^ {L _ {m}} \pi_ {x _ {m, l}, r _ {m, l}, f _ {m, l}} d \pi} \\ & {= \prod_ {m = 1} ^ {M} \int \frac {\Gamma (\sum_ {k = 1} ^ {K} \alpha_ {k})}{\prod_ {k = 1} ^ {K} \Gamma (\alpha_ {k})} \prod_ {k = 1} ^ {K} \theta_ {m, k} ^ {\alpha_ {k} - 1 + c _ {k, m, *} + d _ {k, m, *, *}} d \theta_ {m} \prod_ {k = 1} ^ {K} \prod_ {r = 1} ^ {R} \int \frac {\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f})}{\prod_ {f = 1} ^ {M} \Gamma (\varepsilon_ {f})} \pi_ {k, r, f} ^ {\varepsilon_ {f} - 1 + d _ {k, *, r, f}} d \pi_ {k, r}} \\ & {= \prod_ {m = 1} ^ {M} \frac {\Gamma (\sum_ {k = 1} ^ {K} \alpha_ {k})}{\prod_ {k = 1} ^ {K} \Gamma (\alpha_ {k})} \frac {\prod_ {k = 1} ^ {K} \Gamma (\alpha_ {k} + c _ {k , m , *} + d _ {k , m , , * , *})}{\Gamma (\sum_ {k = 1} ^ {K} \alpha_ {k} + c _ {k , m , *} + d _ {k , m , , * , *})} \prod_ {k = 1} ^ {K} \prod_ {r = 1} ^ {R} \frac {\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f})}{\prod_ {f = 1} ^ {M} \Gamma (\varepsilon_ {f})} \frac {\prod_ {f = 1} ^ {M} \Gamma (\varepsilon_ {f} + d _ {k , , * , r , f})}{\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f} + d _ {k , , * , r , f})}.} \end{array}
$$

Next, we eliminate constant terms that do not depend upon the position (m,l),

$$
\begin{array}{r l} & {\propto \frac {\prod_ {k = 1} ^ {K} \Gamma (\alpha_ {k} + c _ {k , m , *} + d _ {k , m , * , *})}{\Gamma (\sum_ {k = 1} ^ {K} \alpha_ {k} + c _ {k , m , *} + d _ {k , m , * , *})} \prod_ {k = 1} ^ {K} \frac {\Gamma (\varepsilon_ {f _ {m , l}} + d _ {k , * , r _ {m , l} , f _ {m , l}})}{\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f} + d _ {k , * , r _ {m , l} , f})}} \\ & {= \frac {\prod_ {k \neq x _ {m , l}} \Gamma (\alpha_ {k} + c _ {k , m , *} + d _ {k , m , * , *} ^ {- (m , l)})}{\Gamma (1 + \sum_ {k = 1} ^ {K} \alpha_ {k} + c _ {k , m , *} + d _ {k , m , * , *} ^ {- (m , l)})} \times \Gamma (\alpha_ {x _ {m, l}} + c _ {x _ {m, l}, m, *} + d _ {x _ {m, l}, m, *, *} ^ {- (m, l)} + 1)} \\ & \times \prod_ {k \neq x _ {m, l}} \frac {\Gamma (\varepsilon_ {f _ {m , l}} + d _ {k , * , r _ {m , l} , f _ {m , l}} ^ {- (m , l)})}{\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f} + d _ {k , * , r _ {m , l} , f} ^ {- (m , l)})} \times \frac {\Gamma (\varepsilon_ {f _ {m , l}} + d _ {x _ {m , l} , * , r _ {m , l} , f _ {m , l}} ^ {- (m , l)})}{\Gamma (\sum_ {f = 1} ^ {M} \varepsilon_ {f} + d _ {x _ {m , l} , * , r _ {m , l} , f} ^ {- (m , l)})} \times \frac {\varepsilon_ {f _ {m , l}} + d _ {x _ {m , l} , * , r _ {m , l} , f _ {m , l}} ^ {- (m , l)}}{\sum_ {f = 1} ^ {M} \varepsilon_ {f} + d _ {x _ {m , l} , * , r _ {m , l} , f} ^ {- (m , l)}} \\ & {\propto \frac {(c _ {x _ {m , l} , m , *} + d _ {x _ {m , l} , m , * , *} ^ {- (m , l)} + \alpha_ {x _ {m , l}}) (d _ {x _ {m , l} , * , r _ {m , l} , f _ {m , l}} ^ {- (m , l)} + \varepsilon_ {f _ {m , l}})}{d _ {x _ {m , l} , * , r _ {m , l} , *} ^ {- (m , l)} + \sum_ {l = 1} ^ {M} \varepsilon_ {l}}} \end{array}
$$

## References

[1] J.L. Zhao, S.F. Hu, Daning, Business challenges and research directions of management analytics in the big data era, Journal of Management Analytics, 1 (2014) 169-174.

[2] E.P. Lim, H. Chen, G. Chen, Business Intelligence and Analytics: Research Directions, Acm Transactions on Management Information Systems, 3 (2013).

[3] H. Chen, R.H. Chiang, V.C. Storey, Business Intelligence and Analytics: From Big Data to Big Impact, MIS quarterly, 36 (2012) 1165-1188.

[4] D. Buhalis, R. Law, Progress in information technology and tourism management: 20 years

on and 10 years after the Internet—The state of eTourism research, Tourism management, 29 (2008) 609-623.

[5] H. Werthner, F. Ricci, E-commerce and tourism, Communications of the ACM, 47 (2004) 101-105.

[6] Q. Liu, E. Chen, H. Xiong, Y. Ge, Z. Li, X. Wu, A cocktail approach for travel package recommendation, Knowledge and Data Engineering, IEEE Transactions on, 26 (2014) 278-293.

[7] C. Tan, Q. Liu, E. Chen, H. Xiong, X. Wu, Object-oriented Travel Package Recommendation, ACM Transactions on Intelligent Systems and Technology (TIST), 5 (2014) 43.

[8] H. Werthner, Intelligent systems in travel and tourism, in, IJCAI 2003: 18th International Joint Conference on Artificial Intelligence, 2002.

[9] Q. Liu, Y. Ge, Z. Li, E. Chen, H. Xiong, Personalized travel package recommendation, in: Data Mining (ICDM), 2011 IEEE 11th International Conference on, IEEE, 2011, pp. 407-416.

[10] Y. Ge, Q. Liu, H. Xiong, A. Tuzhilin, J. Chen, Cost-aware travel tour recommendation, in: Proceedings of the 17th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2011, pp. 983-991.

[11] R.B. Cialdini, N.J. Goldstein, Social influence: Compliance and conformity, Annu. Rev. Psychol., 55 (2004) 591-621.

[12] H. Ma, D. Zhou, C. Liu, M.R. Lyu, I. King, Recommender systems with social regularization, in: Proceedings of the fourth ACM international conference on Web search and data mining, ACM, 2011, pp. 287-296.

[13] H. Ma, H. Yang, M.R. Lyu, I. King, Sorec: social recommendation using probabilistic matrix factorization, in: Proceedings of the 17th ACM conference on Information and knowledge management, ACM, 2008, pp. 931-940.

[14] T. Zhao, J. McAuley, I. King, Leveraging Social Connections to Improve Personalized Ranking for Collaborative Filtering, in: Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management, ACM, 2014, pp. 261-270.

[15] R.R. Currie, F. Wesley, P. Sutherland, Going where the Joneses go: Understanding how others influence travel decision-making, International Journal of Culture, Tourism and Hospitality Research, 2 (2008) 12-24.

[16] L. Murphy, G. Mascardo, P. Benckendorff, Exploring word‐ of‐ mouth influences on travel decisions: friends and relatives vs. other travellers, International Journal of Consumer Studies, 31

(2007) 517-527.

[17] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative filtering, in: Proceedings of the Fourteenth conference on Uncertainty in artificial intelligence, Morgan Kaufmann Publishers Inc., 1998, pp. 43-52.

[18] A. Srivihok, P. Sukonmanee, E-commerce intelligent agent: personalization travel support agent using Q Learning, in: Proceedings of the 7th international conference on Electronic commerce, 2005, pp. 287-292.

[19] S. Schiaffino, A. Amandi, Building an expert travel agent as a software agent, Expert Systems with Applications, 36 (2009) 1291-1299.

[20] I. King, M.R. Lyu, H. Ma, Introduction to social recommendation, in: Proceedings of the 19th international conference on World wide web, ACM, 2010, pp. 1355-1356.

[21] M. Ye, X. Liu, W.-C. Lee, Exploring social influence for recommendation: a generative model approach, in: Proceedings of the 35th international ACM SIGIR conference on Research and development in information retrieval, ACM, 2012, pp. 671-680.

[22] Q. Yuan, L. Chen, S. Zhao, Factorization vs. regularization: fusing heterogeneous social relationships in top-n recommendation, in: Proceedings of the fifth ACM conference on Recommender systems, ACM, 2011, pp. 245-252.

[23] X. Yang, H. Steck, Y. Liu, Circle-based recommendation in online social networks, in: Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2012, pp. 1267-1275.

[24] M. Jiang, P. Cui, R. Liu, Q. Yang, F. Wang, W. Zhu, S. Yang, Social contextual recommendation, in: Proceedings of the 21st ACM international conference on Information and knowledge management, ACM, 2012, pp. 45-54.

[25] F. Fouss, A. Pirotte, J.-M. Renders, M. Saerens, Random-walk computation of similarities between nodes of a graph with application to collaborative recommendation, Knowledge and data engineering, ieee transactions on, 19 (2007) 355-369.

[26] Y. Pan, F. Cong, K. Chen, Y. Yu, Diffusion-aware personalized social update recommendation, in: Proceedings of the 7th ACM conference on Recommender systems, ACM, 2013, pp. 69-76.

[27] M. Steyvers, T. Griffiths, Probabilistic topic models, Handbook of latent semantic analysis, 427 (2007) 424-440.

[28] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, the Journal of machine Learning research, 3 (2003) 993-1022.

[29] R.M. Nallapati, A. Ahmed, E.P. Xing, W.W. Cohen, Joint latent topic models for text and citations, in: Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2008, pp. 542-550.

[30] X. Wang, C. Zhai, D. Roth, Understanding evolution of research themes: a probabilistic generative model for citations, in: Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2013, pp. 1115-1123.

[31] B. Liu, H. Xiong, Point-of-Interest Recommendation in Location Based Social Networks with Topic and Location Awareness, in: SDM, 2013, pp. 396-404.

[32] C. Wang, D.M. Blei, Collaborative topic modeling for recommending scientific articles, in: Proceedings of the 17th ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, 2011, pp. 448-456.

[33] L. Liu, J. Tang, J. Han, M. Jiang, S. Yang, Mining topic-level influence in heterogeneous networks, in: Proceedings of the 19th ACM international conference on Information and knowledge management, ACM, 2010, pp. 199-208.

[34] N. Barbieri, F. Bonchi, G. Manco, Topic-aware social influence propagation models, Knowledge and information systems, 37 (2013) 555-584.

[35] B. Bi, Y. Tian, Y. Sismanis, A. Balmin, J. Cho, Scalable topic-specific influence analysis on microblogs, in: Proceedings of the 7th ACM international conference on Web search and data mining, ACM, 2014, pp. 513-522.

[36] H.C. Wu, R.W.P. Luk, K.F. Wong, K.L. Kwok, Interpreting tf-idf term weights as making relevance decisions, ACM Transactions on Information Systems (TOIS), 26 (2008) 13.

[37] G. Heinrich, Parameter estimation for text analysis, in, Technical report, 2005.

[38] M. Jamali, M. Ester, A matrix factorization technique with trust propagation for recommendation in social networks, in: Proceedings of the fourth ACM conference on Recommender systems, ACM, 2010, pp. 135-142.

[39] A.H. Cheetham, J.E. Hazel, Binary (presence-absence) similarity coefficients, Journal of Paleontology, (1969) 1130-1136.

[40] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommendation algorithms, in: Proceedings of the 10th international conference on World Wide

Web, ACM, 2001, pp. 285-295.

[41] W.X. Zhao, J. Jiang, J. Weng, J. He, E.-P. Lim, H. Yan, X. Li, Comparing twitter and traditional media using topic models, in: Advances in Information Retrieval, Springer, 2011, pp. 338-349.

[42] Q. Liu, E. Chen, H. Xiong, C.H. Ding, J. Chen, Enhancing collaborative filtering by user interest expansion via personalized ranking, Systems, Man, and Cybernetics, Part B: Cybernetics, IEEE Transactions on, 42 (2012) 218-233.

[43] P. Cremonesi, Y. Koren, R. Turrin, Performance of recommender algorithms on top-n recommendation tasks, in: Proceedings of the fourth ACM conference on Recommender systems, ACM, 2010, pp. 39-46.

[44] G. Bouma, Normalized (pointwise) mutual information in collocation extraction, Proceedings of GSCL, (2009) 31-40.

[45] Y. Hu, Y. Koren, C. Volinsky, Collaborative filtering for implicit feedback datasets, in: Data Mining, 2008. ICDM'08. Eighth IEEE International Conference on, IEEE, 2008, pp. 263-272.

## 10 Biography

Jiangning He is a PhD candidate in the Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, China. Her research interests involve Data Mining and Recommendation. She received her BA in Information System from Renmin University of China.

Hongyan Liu is a full professor of Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, China. Dr. Liu received her PhD in Management Science from Tsinghua University. Her research interests include Business Intelligence, Data Mining, Recommendation, and Social Computing. Dr. Liu is member of ACM, IEEE, SIAM and AIS and has published many papers in top journals such as ACM Transactions on Information Systems (TOIS), INFORMS Journal on Computing, ACM Transactions on Database Systems (TODS), and IEEE Transactions on Knowledge and Data Engineering (TKDE), and in many top international conferences such as International Conference on Very Large Data Bases (VLDB), IEEE International Conference on Date Engineering (ICDE), International Conference on Knowledge Discovery and Data Mining (SIGKDD), IEEE International Conference on Data Mining (ICDM), SIAM International Conference on Data Mining (SDM), and ACM International Conference on

Information and Knowledge Management (CIKM).

Hui Xiong is a Professor and Vice Chair in the Management Science and Information Systems Department. Dr. Xiong's general area of research is data and knowledge engineering, with a focus on developing effective and efficient data analysis techniques for emerging data intensive applications. He has published prolifically in refereed journals and conference proceedings, such as IEEE Transactions on Knowledge and Data Engineering, the VLDB Journal, INFORMS Journal on Computing, Machine Learning, the Data Mining and Knowledge Discovery Journal, ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), SIAM International Conference on Data Mining (SDM), IEEE International Conference on Data Mining (ICDM), and ACM International Symposium on Advances in Geographic Information Systems (ACM GIS). He is an ACM Distinguished Scientist and a senior member of the IEEE.

![](/api/attachments/DV55SV4A/fulltext/images/610fe26e3305f02a90052771de6495aff432573f69da23e6e3d784db549de277.jpg)  
Figure 1 An illustrating graph of a labeled social network and a bipartite graph with a description of a travel package

![](/api/attachments/DV55SV4A/fulltext/images/222d171d00165572dbcb3e5af93d26eab0c3552c5fd630c6b5f479e0ea434717.jpg)  
Figure 2 The influence of friends' selections on users’ selection likelihood shows that users are more likely to select a travel package as more of their friends select it and that the increasing ratio varies with relationship types.

![](/api/attachments/DV55SV4A/fulltext/images/8f5ba168c92beddfadfb177d39251fd5e735cfb55577cc0759907f0f5dd26497.jpg)  
Figure 3 The TF-IDF value of package category in different relationship types of co-travels shows that users prefer to travel on packages of different categories with different relationship types of friends.

![](/api/attachments/DV55SV4A/fulltext/images/69ddcff3f2e85a26e404e3f7de5b97ce964c38eba1d413f01318825420043e09.jpg)  
Figure 4 Graphical representation of socoLDA. The Observed variables $p , f ,$ and r denote travel packages, co-travelers, and relationship types between users and co-travelers, separately. The hidden variables x and z denote topics assigned for travel packages and topics assigned for co-travelers, separately.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For each topic $k=1,\ldots,K$
Choose $\varphi_{k}\sim Dirichlet(\beta)$
For each topic $k=1,\ldots,K$
For each relationship type $r=1,\ldots,R$
Choose $\pi_{k,r}\sim Dirichlet(\varepsilon)$
For each user $m=1,\ldots,M$
Choose $\theta_{m}\sim Dirichlet(\alpha)$
Choose $\sigma_{m}\sim Dirichlet(\gamma)$
For the $n^{th}$ package of the $m^{th}$ user, where $n\in\{1,\ldots,N_{m}\}$
Choose a topic $z_{m,n}\sim Multi(\theta_{m})$, where $z_{m,n}\in\{1,\ldots,K\}$
Choose a package $p_{m,n}\sim Multi(\varphi_{z_{m,n}})$, where $p_{m,n}\in\{1,\ldots,V\}$
For the $l^{th}$ co-traveler of the $m^{th}$ user, where $l\in\{1,\ldots,L_{m}\}$
Choose a relationship type $r_{m,l}\sim Multi(\sigma_{m})$, where $r_{m,l}\in\{1,\ldots,R\}$
Choose a topic $x_{m,l}\sim Multi(\theta_{m})$, where $x_{m,l}\in\{1,\ldots,K\}$
Choose a co-traveler $f_{m,l}\sim Multi(\pi_{x_{m,l},r_{m,l}})$, where $f_{m,l}\in\{1,\ldots,M\}$
</div>

## Figure 5 A generative process of socoLDA

![](/api/attachments/DV55SV4A/fulltext/images/a8e11d5ebea86b7b2311b1656c0a34d84da869a211207ef7ac976b4ac965c051.jpg)

![](/api/attachments/DV55SV4A/fulltext/images/d45eb39a516b091d5160e118ef1a299629b2ebfacfa596d9885c2b9bd1b4de32.jpg)  
Figure 6 Recall@K comparison of different methods

![](/api/attachments/DV55SV4A/fulltext/images/c3fcf2eec22188e1a40bac88b3142001aa1bc38fd8905d90d36fa6a8d345d20c.jpg)

![](/api/attachments/DV55SV4A/fulltext/images/43839cfc5ef60f9086cf0031b071390c8f59e03cd2cc78e29295a0cd96d9adcf.jpg)  
Figure 7 DOA comparison by varying the size of training set from 50% to 90%

![](/api/attachments/DV55SV4A/fulltext/images/5c91156b8dfd1f0d1b59ea8c1e24eee492002201a02f63602ef0a9e0d6998b39.jpg)  
Figure 8 Recall@K comparison when the percentage of training set is 50%

![](/api/attachments/DV55SV4A/fulltext/images/bcbc9f8b3c9de14b4e68c5c00434ab71c23f396cdfffaedd6120341cdf7800b0.jpg)  
Figure 9 Time and memory cost of different methods

![](/api/attachments/DV55SV4A/fulltext/images/5e334379222c22be155eade5dae2294282bdbe969ba4596a7ede899ebecda487.jpg)

![](/api/attachments/DV55SV4A/fulltext/images/bd63614f0ae54bf0a1909d2bb797c7ebe39b15f82a4d88215bbcb9cbcebad4d9.jpg)  
Figure 10 Topic temporal evolution. The X-axis denotes time points of each month in three years from 2012 to 2014, and the Y-axis denotes the temporal strength of topics, denoting how the popularity of travel topics changes over time.

Table 1 Basic statistics for each category of packages

<table><tr><td>Package Category</td><td>Percentage of Packages (%)</td><td>Average Cost (¥)</td><td>Average Participants</td></tr><tr><td>Deep travel</td><td>11.44</td><td>3360.92</td><td>26.83</td></tr><tr><td>Outdoor activity</td><td>64.96</td><td>193.47</td><td>29.44</td></tr><tr><td>Leisure travel</td><td>5.87</td><td>533.42</td><td>19.93</td></tr><tr><td>Photography</td><td>14.35</td><td>902.10</td><td>29.84</td></tr><tr><td>Sightseeing</td><td>0.63</td><td>398.67</td><td>17.8</td></tr><tr><td>Party</td><td>1.86</td><td>15.80</td><td>40.61</td></tr><tr><td>Salon</td><td>0.89</td><td>3.33</td><td>66.67</td></tr></table>

Table 2 Number of social connections for each social relationship type

<table><tr><td>Relationship Type</td><td>Count</td><td>Relationship Type</td><td>Count</td></tr><tr><td>Online friend</td><td>111,976</td><td>Schoolmate</td><td>6,631</td></tr><tr><td>Real friend</td><td>70,817</td><td>Colleague</td><td>2,891</td></tr><tr><td>Travel acquaintance</td><td>55,380</td><td>Fellow townsman</td><td>1,682</td></tr><tr><td>Other</td><td>10,416</td><td>Relative</td><td>205</td></tr></table>

Table 3 Sparse travel records vs. plentiful social information

<table><tr><td>Range of travel records</td><td>Percentage of Users (%)</td><td>Average Friends</td><td>Average Co-travelers</td></tr><tr><td>[2, 3]</td><td>60.13</td><td>11.01</td><td>92.84</td></tr><tr><td>[4, 5]</td><td>14.45</td><td>14.28</td><td>221.31</td></tr><tr><td>[6, 7]</td><td>7.78</td><td>23.91</td><td>309.29</td></tr><tr><td>[8, 10]</td><td>6.37</td><td>27.60</td><td>431.64</td></tr><tr><td>[11, 20]</td><td>7.27</td><td>41.33</td><td>674.09</td></tr><tr><td>[21, 50]</td><td>3.29</td><td>131.92</td><td>1346.79</td></tr><tr><td>[51, 230]</td><td>0.71</td><td>609.31</td><td>3353.45</td></tr></table>

Table 4 Notations and descriptions of parameters of socoLDA model

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>M</td><td>Number of unique users, M=|U|</td></tr><tr><td>V</td><td>Number of unique packages in travel records, V=|P|</td></tr><tr><td>K</td><td>Number of topics</td></tr><tr><td>R</td><td>Number of relationship types, including a type of non-social co-traveler</td></tr><tr><td>Nm</td><td>Number of packages selected by the  $m^{th}$  user</td></tr><tr><td>Lm</td><td>Number of co-travelers for the  $m^{th}$  user</td></tr><tr><td>α,β,γ,ε</td><td>Hyper-parameters of Dirichlet priors for multinomial distributions</td></tr><tr><td>θ</td><td>User-specific topic multinomial distribution</td></tr><tr><td>φ</td><td>Topic-specific package multinomial distribution</td></tr><tr><td>σ</td><td>User-specific relationship type multinomial distribution</td></tr><tr><td>π</td><td>Topic &amp; relationship type-specific co-traveler multinomial distribution</td></tr><tr><td>z</td><td>Topic of a package</td></tr><tr><td>x</td><td>Topic of a co-traveler</td></tr><tr><td>r</td><td>Relationship type of a co-traveler</td></tr><tr><td>p</td><td>A package token of a user</td></tr><tr><td>f</td><td>A co-traveler token of a user</td></tr></table>

Table 5 Description of training and testing data

<table><tr><td></td><td># users</td><td># packages</td><td># records</td></tr><tr><td>Training Set:  $T^{train}$ </td><td>10,812</td><td>2,346</td><td>57,974</td></tr><tr><td>Testing Set:  $T^{test}$ </td><td>10,812</td><td>1,824</td><td>10,812</td></tr></table>

Table 6 DOA comparison of different methods

<table><tr><td>Method</td><td>DOA (%)</td><td>Method</td><td>DOA (%)</td><td>Method</td><td>DOA (%)</td></tr><tr><td>SocoTraveler</td><td>80.10</td><td>ST-W-S</td><td>70.74</td><td>LDA-W</td><td>68.60</td></tr><tr><td>ST-New</td><td>79.07</td><td>Citation-LDA</td><td>75.37</td><td>SocialMF</td><td>70.02</td></tr><tr><td>ST-S</td><td>76.53</td><td>OTM-ORS</td><td>72.21</td><td>UCF</td><td>69.30</td></tr><tr><td>ST-W</td><td>75.33</td><td>LDA-P</td><td>74.08</td><td>ICF</td><td>66.90</td></tr></table>

Table 7 Top 3 representative packages for selected topics

<table><tr><td colspan="4">Topic 3 “Northwest Prairie Tour”</td></tr><tr><td>Rank</td><td>Title</td><td>Cost</td><td>Days</td></tr><tr><td>1</td><td>A 9-day deep travel to northern Xinjiang</td><td>3950</td><td>9</td></tr><tr><td>2</td><td>A 6-day cool travel to Bashang grassland</td><td>2350</td><td>6</td></tr><tr><td>3</td><td>A 9-day autumn travel to Hulunbeir prairie and greater Hinggan mountains</td><td>3580</td><td>9</td></tr><tr><td colspan="4">Topic 13 “Hydrophilic Tour”</td></tr><tr><td>Rank</td><td>Title</td><td>Cost</td><td>Days</td></tr><tr><td>1</td><td>A full view of Guilin, rafting in Lijiang river</td><td>1190</td><td>5</td></tr><tr><td>2</td><td>A rafting and orange picking in Mid-Autumn festival</td><td>120</td><td>1</td></tr><tr><td>3</td><td>A cool travel for Wuxi river rafting and terrace photography</td><td>420</td><td>2</td></tr><tr><td colspan="4">Topic 48 “Mountain Climbing”</td></tr><tr><td>Rank</td><td>Title</td><td>Cost</td><td>Days</td></tr><tr><td>1</td><td>Climbing through Wugong mountains in the eastern of China</td><td>550</td><td>4</td></tr><tr><td>2</td><td>Loop climbing to famous Taoism mountain—Mount Qiyun</td><td>300</td><td>2</td></tr><tr><td>3</td><td>A personalized travel to Mount Wuyi for beautiful scenery</td><td>600</td><td>3</td></tr></table>

Table 8 Results of descriptive summarization for selected topics

<table><tr><td>Topic</td><td>Topic label</td><td>Keywords</td><td>E(cost)</td><td>E(days)</td></tr><tr><td>3</td><td>Northwest Prairie Tour</td><td>Prairie, grassland, horse, cool, kite</td><td>3,070.05</td><td>6.77</td></tr><tr><td>11</td><td>Suburb Night-walk</td><td>Outdoor, night-walk, loop, Thursday, evening</td><td>25.08</td><td>1.04</td></tr><tr><td>13</td><td>Hydrophilic Tour</td><td>River, water, sea, leisure, rafting, boat</td><td>512.88</td><td>2.29</td></tr><tr><td>48</td><td>Mountain Climbing</td><td>Famous mountains, mount, camping, climbing</td><td>448.87</td><td>2.74</td></tr><tr><td>90</td><td>Autumn hiking</td><td>Outdoor, hiking, autumn, ancient road</td><td>139.68</td><td>1.16</td></tr></table>

Table 9 Co-occurrence analysis of travel topic and relationship type by nPMI

<table><tr><td colspan="5">Online Friend</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>91</td><td>0.141</td><td>Photography, outdoors, portrait, Shanghai, Tianzi lane</td><td>234.98</td><td>1.68</td></tr><tr><td>7</td><td>0.113</td><td>Outdoor activity, traversing, camping, night-walk</td><td>292.23</td><td>1.76</td></tr><tr><td>62</td><td>0.109</td><td>Party, ladies, salon, conductor training, treasure hunt</td><td>51.50</td><td>1.12</td></tr><tr><td colspan="5">Real Friend</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>18</td><td>0.316</td><td>Deep travel, autumn scenery, beautiful, leisure</td><td>275.39</td><td>1.42</td></tr><tr><td>8</td><td>0.227</td><td>Photography, deep, sea, stream, waterfall, island</td><td>580.30</td><td>2.35</td></tr><tr><td>3</td><td>0.227</td><td>Prairie, grassland, horse, cool, kite</td><td>3,070.05</td><td>6.77</td></tr><tr><td colspan="5">Travel Acquaintance</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>4</td><td>0.168</td><td>Ancient road, legend, village, photography, outdoor</td><td>58.78</td><td>1.10</td></tr><tr><td>41</td><td>0.163</td><td>Ancient road, autumn, beautiful, mountain, scenery</td><td>85.08</td><td>1.16</td></tr><tr><td>7</td><td>0.135</td><td>Outdoor, ancient road, camping, leisure, night-walk</td><td>292.23</td><td>1.76</td></tr><tr><td colspan="5">Schoolmate</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>18</td><td>0.140</td><td>Deep travel, autumn scenery, beautiful, leisure</td><td>275.39</td><td>1.42</td></tr><tr><td>97</td><td>0.130</td><td>Mountain, outdoors, night-walk, traversing, hiking</td><td>17.74</td><td>1.03</td></tr><tr><td>4</td><td>0.128</td><td>Ancient road, legend, village, photography, outdoor</td><td>58.78</td><td>1.10</td></tr><tr><td colspan="5">Colleague</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>62</td><td>0.270</td><td>Party, ladies, salon, conductor training, treasure hunt</td><td>51.50</td><td>1.12</td></tr><tr><td>7</td><td>0.104</td><td>Outdoor, ancient road, camping, leisure, night-walk</td><td>292.23</td><td>1.76</td></tr><tr><td>69</td><td>0.103</td><td>Salon, photography, grand party, award</td><td>363.18</td><td>1.47</td></tr></table>

##

<table><tr><td colspan="5">Fellow Townsman</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>91</td><td>0.197</td><td>Photography, outdoors, portrait, Shanghai, Tianzi lane</td><td>234.98</td><td>1.68</td></tr><tr><td>72</td><td>0.105</td><td>Photography, deep, terrace, Yunnan, red land, rape flower</td><td>2,716.80</td><td>7.03</td></tr><tr><td>7</td><td>0.104</td><td>Outdoor, ancient road, camping, leisure, night-walk</td><td>292.23</td><td>1.76</td></tr><tr><td colspan="5">Relative</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>60</td><td>0.139</td><td>Outdoors, climb, loop, city, night-walk, Linyin mountain</td><td>10.28</td><td>1.02</td></tr><tr><td>18</td><td>0.139</td><td>Deep travel, autumn scenery, beautiful, leisure</td><td>275.39</td><td>1.42</td></tr><tr><td>90</td><td>0.136</td><td>Outdoors, hiking, autumn, ancient road</td><td>139.68</td><td>1.16</td></tr><tr><td colspan="5">Non-social Co-traveler</td></tr><tr><td>Topic</td><td>nPMI</td><td>Keywords</td><td>E (cost)</td><td>E (days)</td></tr><tr><td>24</td><td>0.010</td><td>Huihang ancient road, outdoors, leisure, traveling light</td><td>292.91</td><td>1.32</td></tr><tr><td>27</td><td>0.009</td><td>Deep, prairie, Qinghai lake, Lhasa, Mogao caves</td><td>3,212.79</td><td>7.735</td></tr><tr><td>34</td><td>0.008</td><td>Photography, snow village, soft rime, snowy mountains</td><td>3,469.17</td><td>6.95</td></tr></table>
