---
otero_id: 12518
otero_key: "QZJHV7WZ"
title: "A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship"
authors: "Yung-Ming Li; Chun-Te Wu; Cheng-Yang Lai"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.02.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship

Yung-Ming Li ⁎, Chun-Te Wu, Cheng-Yang Lai

Institute of Information Management, National Chiao Tung University, Hsinchu 300, Taiwan

## a r t i c l e i n f o

Article history: Received 6 December 2011 Received in revised form 26 December 2012 Accepted 25 February 2013 Available online xxxx

Keywords: E-commerce Social recommender systems Preference similarity Trust Social relation Analytic hierarchy process

## a b s t r a c t

Online business transactions and the success of e-commerce depend greatly on the effective design of a product recommender mechanism. This study proposes a social recommender system that can generate personalized product recommendations based on preference similarity, recommendation trust, and social relations. Compared with traditional collaborative <sup>fi</sup>ltering approaches, the advantage of the proposed mechanism is its comprehensive consideration of recommendation sources. Accordingly, our experimental results show that the proposed model outperforms other benchmark methodologies in terms of recommendation accuracy. The proposed framework can also be effectively applied to e-commerce retailers to promote their products and services.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

“Social is not just about sharing connections, it's about providing different ways for people to interact…. Social commerce excites me — we already know how powerful recommendations from friends can be and the group shopping experience can easily be replicated through social commerce.”

[Sophy Silver, Facebook's UK & Ireland Public Relations Chief]

With booming social networking technologies and platforms, most e-commerce companies are creating social network pro<sup>fi</sup>les of their own. J.P. Morgan anticipates that global e-commerce revenue will reach \$963 billion by 2013 [28]. The report forecasts that e-commerce revenue will grow to \$680 billion worldwide, up 18.9% from 2010 revenue, and online retail commerce in the U.S. alone will grow 13.2% to \$187 billion.

For many people, shopping is a social experience, and they often want to get their friends' opinions before buying. Social commerce is helping people buy where they connect. It integrates social media into e-retail sites and adds e-commerce functionality to social networks. For online storeowners, social commerce is becoming a way of thinking about transacting business online. Some e-commerce sites use your friends' preferences to help you make better purchasing decisions.

Amazon, for example, helps you <sup>fi</sup>nd records and books by the artists and authors your friends have listed in their Facebook pro<sup>fi</sup>les.

Recommender systems assist users in making choices from various alternatives; the goal of these systems is to estimate user preferences and provide predictions of appropriate information. Social recommender systems aim to relieve information and interaction overload by applying various techniques that ultimately present the most relevant and attractive information to users. These personalized recommendations based on social interactions or preferences are viewed as a huge opportunity for vendors. Indeed, a survey of online retailers in 2010 found that over half planned on implementing recommendation features on their sites [20].

To date, a variety of recommendation techniques has been developed. To our best knowledge, collaborative <sup>fi</sup>ltering, content-based, and hybrid approaches are three popular approaches that have been used to generate recommendations [23]. An approach that has received less attention is using the social relations on individuals as an additional source of information. The principle of homophily from the social network <sup>fi</sup>eld suggests that “similarity breeds connection.” In other words, users share many attributes with the people close to them. This suggests that if we have information about the connections in a person's network, we can infer some of that person's attributes. Most commercial recommender systems are strongly supported by the demographic information of users. Since some of the similarities within a network are caused by the in<sup>fl</sup>uence and interactions of its members, it would be reasonable and feasible to develop a social recommendation based on the connections of individual users. In reality, people tend to be affected by the opinions of and suggestions by people with similar interests, shopping experts, and close friends.

However, most of current social networking platform, such as Facebook and twitter, and electronic commerce platform, such as Amazon and Yahoo! Shopping, are independently operated. The supporting recommender systems are also independently deployed on the two kinds of platforms based on social factors and purchase history respectively. As a result, the electronic commerce (retailing) platforms generally do not consider social factors such as relationships and trust etc. among the users and the power of social in<sup>fl</sup>uence is not exploited. Contrarily, social networking platforms generally do not consider online shopping related factors such as purchase history and product rating etc.

To address these issues, in this research, we synthesize the features of social networking and electronic commerce platforms to design a social recommender mechanism that considers the factors of preference similarity, recommendation trust, and social relationship in order to increase the prediction accuracy of product recommendations in e-commerce. The factors of human interactions and relations (e.g. trusts [30,61], reputations [40,64], and social relationship [34,68]) have been applied separately in different application contexts. In this research, by building several new social metric formulas, we exploit and consolidate various types of consulting information source to generate product recommendations.

The proposed mechanism allows us to identify suitable products for individual customers by utilizing the collective intelligence from social networks and to balance the consulted sources based on these personalized preferences. Our experimental results based on users' evaluations in Yahoo! Shopping show that the proposed model could enhance recommendation accuracy. The proposed model could be practically applied to new emerging social commerce platforms.

The remainder of this paper is organized as follows. In Section 2, we discuss the existing literature related to our research topics. In Section 3, we discuss the factors that contribute to the proposed social recommendation framework. Section 4 describes the experimental data source, settings, and procedures. The experimental results and evaluations are discussed in Section 5. Section 6 concludes our research contributions and presents future research directions.

## 2. Related works

## 2.1. Recommender systems

Recommender systems can help users identify the items that suit their needs or preferences in an effective way. They are usually used to solve information overload problems and to grow sales in e-commerce [55].

For providing personalized recommendations, there are two ways to receive users' preferences [21]: implicit and explicit. First, the implicit method collects users' behavior to infer their preferences. When detecting changes, these user preference data change simultaneously [2]. Choi et al. [10] derive implicit rating information from transaction history to identify preference of users. Nunez-Valdez et al. [48] investigate the behavior of electronic book readers to capture, measure, and classify implicit information for discovering user interests. Koren et al. [32] construct matrix factorization models that use implicit feedback. Second, the explicit method <sup>fi</sup>lters and analyzes interactions and feedback to infer users' speci<sup>fi</sup>cations [5]. Schafer et al. [58] collect feedback from customers about books they have read to construct recommendations. Based on the user de<sup>fi</sup>ned reading preferences, Wen et al. [67] build a personalized news recommender system on the Web.

A variety of common recommendation techniques has been developed: collaborative <sup>fi</sup>ltering, content-based, and hybrid recommender systems [23]. Content-based systems use items' characteristics and the ratings that users have given to generate recommendations. Lee et al. [37] propose a content-based online product recommendation using Amazon's book rating and review data to support business-toconsumer e-commerce. Mooney and Roy [46] construct recommender systems by using text content. Phelan et al. [52] analyze Twitter to recommend news; however, this approach has a critical problem: when collecting or providing insuf<sup>fi</sup>cient information, recommender systems tend to fail [3]. Collaborative systems identify similar users and analyze their preferences to generate recommendations. In the work of Choi et al. [10], the users' purchase patterns (e.g. ratings and items) are derived by sequential pattern analysis to collaboratively recommend items to users. Based on the music rating information, Lee et al. [35] identify the taste-liked users for users and provide the collaborative-based recommendation in the mobile environment. Amazon.com analyzes customers' interests to recommend books [42]. There are many studies of the combination of content- and collaborative-based systems [44,67]. Wen et al. [67] develop a hybrid news recommender system in which recommendation is made based on analyzed users' preferences and computed news similarities. Liu et al. [44] combine user-based and item-based methods to build a hybrid recommendation of movies in P2P networks. When the content of the description is not obvious, a collaborative approach increases the system's precision [53]. By contrast, when users are not sensitive, a content-based approach increases precision [51].

In the current paper, we develop a social recommender system by merging and extending content- and collaborative-based recommender systems.

## 2.2. Trust and reputation systems

Online communities allow users to easily express their personal preferences, such as the users they trust and the products/services they are interested in [18]. In the online services environment, users have insuf<sup>fi</sup>cient information about other users, service providers, and the services offered. This phenomenon forces consumers to face some risks during transactions [26].

The basic idea of the trust and reputation system is to derive a score for users. According to these scores, users can decide whether or not to transact with a user. Trust means a subjective expectation that an agent has about another's future behavior based on the interaction history of their encounters [47]. Gambetta [17] de<sup>fi</sup>nes trust as the subjective probability by which an individual expects that another individual performs a given action on which its welfare depends. This de<sup>fi</sup>nition shows the concept of dependence and reliability between trusted and trusting parties. Furthermore, Josang et al. [26] de<sup>fi</sup>ne trust as the extent to which one party is willing to depend on something or somebody in a given situation with a feeling of relative security, even though negative consequences are possible. Furthermore, trust is a <sup>fi</sup>rm's belief in the competence of an entity to act dependably, securely, and reliably within a speci<sup>fi</sup>ed context [18]. These de<sup>fi</sup>nitions explain that the situational risks that result from previous experience are accepted by the trusting party.

Reputation can be considered to be a collective measure of trustworthiness (in the sense of reliability) based on the referrals or ratings of members in a community [26]. This indicates that a combination of received referrals and personal experience could derive the measurable subjective trust of an individual. According to Bromley [6], reputation can be separated from the person it belongs to. This will lead to the effect that people take action to enhance and protect their reputations, because they have value to them [6]. In other words, the trust of a person can be built or enhanced from his or her reputation. Van Baalen et al. [60] note that trust is a construct that has a signi<sup>fi</sup>- cant impact on users' online purchasing behavior. Doing business with people we have never met before requires a great deal of trust, especially when the transaction is executed online without any physical interaction [16]. Therefore, trust plays a critical role in e-commerce behavior.

## 2.3. Social networks and relationship

Social networks have become an important web service with broad ranges of applications such as collaborative work, collaborative service rating, resource sharing, and searching for new friends [13]. The de<sup>fi</sup>nition of a social network is enriched. The concept of social networks does not just stay merely in the conceptual aspect but also moves into implemental <sup>fi</sup>elds. As long as the relationships of users can be described and analyzed, a social network of applications and online services can be found and de<sup>fi</sup>ned. Network theory concerns the study of the representation of relations between nodes [31]. A social network is a network formed by a set of speci<sup>fi</sup>c ties that connect actors. Social network theory suggests that the positions of actors in a web of relationships in<sup>fl</sup>uence their access to resources, friends, and information [60]. Many works on the applications of social network analysis have been developed. For example, DeMeo et al. [12] develop a framework to recommend similar users and resources based on social network analysis. Zhen et al. [69] apply this social network concept to develop a recommender system for peer-to-peer knowledge sharing.

Recently, e-commerce companies examine how to leverage social relationships to improve customers' purchase decision making so as to increase sales [29]. The users with closer social relationships to others are much worth to be believed [8] and are much powerful in in<sup>fl</sup>uencing others [36]. Social in<sup>fl</sup>uence might create shopping intention for people to consume a product [29] so that the social relationship is one of the important factors for predicting the potential purchasing intention of a customer [36].

Closeness centrality measures the average geodesic distance to all other nodes in the network and has been applied to the study of social in<sup>fl</sup>uence. Carchiolo et al. [7] indicate that the relationships of friends and friends of friends within a social network are crucial when referencing trustworthy and reliable information. Albert and Barabasi [4] note that social networks are a type of complex networks that have social entities as nodes and links show the relationships. The nature of a social network focuses more on the relationships of components that form the network than on its own structure. Evaluating the closeness of social relation, the rankings or scores of social nodes in a social network could be derived to represent the strength of in<sup>fl</sup>uential power or trust [59]. Regarding the applications, Wang and Chiu [62] combine social closeness and social reputations to discover the trusted online auction sellers. In a study of targeted advertisements, Kempe et al. [27] indicate that information spread by the people with higher closeness relationship would be more in<sup>fl</sup>uential to other nodes in the network.

In this research, by analyzing the relationships among users, we also measure the in<sup>fl</sup>uence of a recommender on product recommendations.

## 2.4. Multi-Criteria Decision Making (MCDM) methods

MCDM methods can be considered to be complex and dynamic processes including generating and evaluating alternatives [14]. They need to de<sup>fi</sup>ne the quantitative weights for criteria while aggregating in order to assess the relative importance of different criteria for ranking alternatives to support users' decision making [49]. Chen et al. [9] apply an MCDM method to support consumers to select a suitable mobile phone and propose a web-based personalized recommender system. Li and Kao [39] utilize the fuzzy inference system and fuzzy MCDM method to support decisions about service choice. Consumers make purchasing decisions based on their own private criteria — even for the same items. Generally, objective weighting and subjective weighting are the two kinds of weighting methods [24]. Subjective weighting is based on the preferences of a decision maker's subjective judgments (e.g. the analytic hierarchy process (AHP) [24,57,58] and Delphi method [56]), while objective weighting derives from observed values (e.g. the Principal Component Analysis method [11,25]) and entropy method [24,66]).

The AHP is one of the common approaches to dealing with the uncertain weighting problem of parameter combination [33]. It is an effective method to solve MCDM problems by determining the relative importance or weight of criteria using mathematical pair-wise comparison [22,63]. The AHP has been extensively applied in many research <sup>fi</sup>elds, such as location selection [33], social network analysis [41], and recommender systems [22,43]. In this research, we use AHP to deal with the personalized factors weighting allocation for consolidating various types of information sources.

## 3. The model

In product purchasing, people tend to ask for advice or suggestions from people with similar interests or professional expertise, or from close friends. However, close friends may not have the expertise or interest in certain products. Furthermore, we may not always believe the suggestions of product experts with whom we have no acquaintance. Consulted sources also differ when product types vary. Therefore, an effective product recommendation should appropriately incorporate these factors. In this study, we propose a social recommender system that comprehensively employs preference analysis, recommendation trust analysis, and social relation analysis modules, as well as a personalized decision module, in order to construct a more comprehensive and personalized framework for product recommendation in e-commerce. Fig. 1 depicts the architecture of the proposed recommendation mechanism.

Four analysis modules have been developed to analyze the information from the constructed form network. The objectives of the analysis modules included in the system are described as follows:

(1) The preference similarity analysis module measures the preference similarity between two customers based on the product rating records of each customer.

(2) The recommendation trust analysis module computes the reputation quality (success rate) of the product recommendations of a customer according to his/her product rating records.

(3) The social relation analysis module analyzes the relation closeness degree between two customers according to implicit interaction records or explicit closeness ratings between them in a social network.

(4) The personalized product recommendation module computes the personalized factor weights for product evaluation and recommendation based on individual factor ratings with respect to different product categories.

For each customer visiting an e-commerce website, the system can provide a list of recommended products, which is individually determined based on the combined product recommendation scores of preference similarity degree, recommendation trust degree, and social relation degree. The whole process of the recommendation mechanism is detailed in the following subsections.

## 3.1. Preference similarity analysis module

People with similar preferences or behavior tend to be interested in the same products, even though they may not know each other [1,12]. Based on the activities of users in a speci<sup>fi</sup>ed social context, a group of users with the same similarity level can be identi<sup>fi</sup>ed. The preference of a targeted customer towards a speci<sup>fi</sup>c product can be predicted by a group of other customers with the same preference similarity. The preference similarity degree of two customers can be estimated according to their product purchases or rating records.

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

![](/api/attachments/QZJHV7WZ/fulltext/images/f49f178ec144c06a871aa85a911f7c26bf9ba39fee2085a857c6fe2f99e03b3e.jpg)  
Fig. 1. Main components in the social recommender framework.

Denote $I _ { p }$ as the set of products customer p has rated. $R _ { p , j }$ represents the evaluation (rating) of product j by customer p. The average product rating of a typical customer p can be formulated as:

$$
\overline {{{R}}} _ {p} = \frac {1}{I _ {p}} \sum_ {j \in I _ {p}} R _ {p, j}, \forall p \in S N,\tag{1}
$$

where SN is the set of all customers in a social network of customers with similar interests. The preference similarity of two customers c and p can be estimated by comparing their records of product purchases or ratings with the Pearson correlation rule [55]. This is formulated as:

$$
\text { Similarity } (c, p) = \frac {\sum_ {j \in I _ {p} \cap I _ {c}} \left(R _ {c , j} - \overline {{R}} _ {c}\right) \left(R _ {p , j} - \overline {{R}} _ {p}\right)}{\sqrt {\sum_ {j \in I _ {p} \cap I _ {c}} \left(R _ {c , j} - \overline {{R}} _ {c}\right) ^ {2}} \sqrt {\sum_ {j \in I _ {p} \cap I _ {c}} \left(R _ {p , j} - \overline {{R}} _ {p}\right) ^ {2}}}.\tag{2}
$$

A higher value for Eq. (2) indicates a higher similarity in the preferences of two customers. It is important to note that the value of similarity could be negative and the magnitude of negativeness standards for the dissimilarity degree. Using the preference similarity between customer c and other customers in the social network, we can predict the rating of customer c on product j as:

$$
\mathrm{PS} (c, j) = \overline {{R}} _ {c} + \frac {\sum_ {p \in S N} \text { Similarity } (c , p) \left(R _ {p , j} - \overline {{R}} _ {p}\right)}{\sum_ {p \in S N} | \text { Similarity } (c , p) |}.\tag{3}
$$

Eq. (3) predicts the level to which customer c likes product j based on how other customers feel about product j weighted by the similarity between customer c and them. The prediction is performed with the support of pair-wise similarity and collective ratings.

## 3.2. Recommendation trust analysis module

When faced with problems that have high information complexity, people may seek help from friends/experts [69,70]. It is likely that recommenders with high expertise make more plausible product recommendations. In other words, the recommendation predication accuracy is positively associated with the recommendation trust (expertise reputation) of recommenders. In this research, the recommendation trust of a recommender is evaluated by his/her success rate of product recommendations and this is measured as follows.

Denote I as the set of all products offered by the e-retailer and the set of product recommendations made by user $p$ to all other customers in the social network as:

$$
\operatorname{RecSet} (p) = \left\{(c, i) \mid c \neq p \in S N, i \in I _ {0}, R _ {p, i} \neq 0, R _ {c, i} \neq 0 \right\}.\tag{4}
$$

A product recommendation is successful only if the rating of the recommender is very close to the rating of the target customer. Therefore, we de<sup>fi</sup>ne the set of successful recommendations made by user p as:

$$
\operatorname{CorrectSet} (p) = \left\{(c, i) \in \operatorname{RecSet} (p), | \mathrm{PS} (c, i) - R _ {c, i} | <   \varepsilon \right\},\tag{5}
$$

where ε is the threshold represented by a small real number. The recommendation trust of user p for a product is de<sup>fi</sup>ned as the successful recommendation rate of the speci<sup>fi</sup>ed product and is formulated as:

$$
\operatorname{Trust} (p, j) = \frac {| \{(c , i) \in \operatorname{CorrectSet} (p) , i = j \} |}{| \{(c , i) \in \operatorname{RecSet} (p) , i = j \} |}.\tag{6}
$$

After we obtain the recommendation trust values from all recommenders in the social network, we can predict the rating of customer c for product j as:

$$
\operatorname{RT} (c, j) = \overline {{R}} _ {c} + \frac {\sum_ {p \in S N} \operatorname{Trust} (p , j) \left(R _ {p , j} - \overline {{R}} _ {p}\right)}{\sum_ {p \in S N} | \operatorname{Trust} (p , j) |}.\tag{7}
$$

The prediction of whether product j is suitable to customer c is performed based on the weighted authorities and ratings of the recommenders' recommendations for this speci<sup>fi</sup>ed product.

## 3.3. Social relation analysis module

It is common that people gather product information by consulting their friends and thus their purchasing decisions can be signi<sup>fi</sup>cantly in<sup>fl</sup>uenced by close friends [50]. Therefore, recommendations by close friends should be more accurate because of the effect of social in<sup>fl</sup>uence. The closeness value of a relation path between two users is measured by the weakest tie strength (closeness) at the edge of the path. When there are multiple relation paths between two users, the path with the strongest closeness value is used to represent the social relation strength between the two users.

Denote $\theta _ { c , p }$ as the set of all available relation paths from customer c to recommender p and $\delta ( e )$ as the tie strength of a direct relation connection between two users e in a relation path L. Note that the tie strength of a relation between two nodes is asymmetric, namely the tie strength of a direct relation from customer A to customer B (evaluated by customer $A ) , e _ { A B } ,$ could be different from that from customer B to customer A (evaluated by customer $B ) , e _ { B A }$ . The social relation closeness between customer c and recommender p is formulated as:

$$
\text { Relation } (c, p) = \max _ {L \in \Theta_ {c, p}} \{\min _ {e \in L} \{\delta (e) \} \}\tag{8}
$$

$\delta ( e )$ in Eq. (8) is a tie strength estimation function, which could be formulated by structural and interactional closeness. In practice, the structural dimension (e.g. possessing friend networks [19]) and the behavioral dimension (e.g. interaction frequency [38]) are two common measurements of tie strength. Granovetter [19] de<sup>fi</sup>nes the tie strength as the overlap of friends of two nodes in a social network. Li and Du [38] use the frequency of the interactions to represent the tie strength between blog readers and authors. In our experiments, because current electronic commerce services do not provide social networking service with online shopping, the social relations could not directly be captured from the website. Thus, the values of δ(e) are explicitly evaluated and provided by participants.

After we <sup>fi</sup>nd the social relation closeness between customer c and all other users in the group, we can predict the rating of customer c for product j as:

$$
\operatorname{SR} (c, j) = \overline {{R}} _ {c} + \frac {\sum_ {p \in S N} \text { Relation } (c , p) \left(R _ {p , j} - \overline {{R}} _ {p}\right)}{\sum_ {p \in S N} | \text { Relation } (c , p) |}.\tag{9}
$$

Eq. (9) shows that the prediction accuracy of recommending a product to customer c is positively associated with the weighted relation closeness and the ratings of recommenders' for this speci<sup>fi</sup>ed product.

## 3.4. AHP personalized recommendation module

Even when facing the same product/category, consumers will still have their own purchase criteria. These criteria are signi<sup>fi</sup>cantly affected by the impact of personality traits, such as gender, age, and economic status. In the present research, we use the AHP [15,33], one of the best-known methods for solving MCDM problems, to analyze the relative weights of the factors (preference similarity, recommendation trust, social relation) included in the proposed framework. The AHP uses mathematical pair-wise comparison to determine the relative importance or weight of criteria so as to support people in making decisions. It has been applied in many research <sup>fi</sup>elds, such as product recommendations [43] and tourism recommendations [22].

In order to achieve the personalized recommendation criteria, users are invited to evaluate the relative importance of preference similarity, recommendation trust, and relationship closeness. Let $A _ { s t r }$ be the relative preference weight matrix of customer c in which element $a _ { i j }$ denotes the relative preference weight of i criterion, in terms of j criterion. This is formulated as:

$$
A _ {s t r} = \left[ \begin{array}{c c c} 1 & a _ {s t} & a _ {s r} \\ 1 / a _ {s t} & 1 & a _ {t r} \\ 1 / a _ {s r} & 1 / a _ {t r} & 1 \end{array} \right],\tag{10}
$$

where $a _ { s t }$ is the relative weight of preference similarity to recommendation trust, $a _ { s r }$ is the relative weight of preference similarity to social relation, and $a _ { t r }$ is the relative weight of recommendation trust to social relation. To derive the relative weight of the criteria from the comparison matrix $A _ { s t r } ,$ an arithmetic mean method is used as follows:

$$
w _ {i} = \frac {1}{3} \sum_ {j = 1} ^ {3} \left(a _ {i j} / \sum_ {i = 1} ^ {3} a _ {i j}\right),\tag{11}
$$

where $w _ { i }$ is the relative weight value for criteria i.

Then, we can obtain the decision weight matrix of customer c on the three factors (preference similarity, recommendation trust, and social relation):

$$
W _ {\mathrm{STR}} (c) = \left[ W _ {S} (c), W _ {T} (c), W _ {R} (c) \right] = \left[ w _ {1}, w _ {2}, w _ {3} \right].\tag{12}
$$

Finally, the personalized recommendation score for product j with respect to customer c can be calculated by the formula:

$$
\mathrm{P} (c, j) = W _ {S} (c) \cdot \mathrm{SR} (c, j) + W _ {\mathrm{T}} (c) \cdot \mathrm{RT} (c, j) + W _ {\mathrm{R}} (c) \cdot \mathrm{PS} (c, j).\tag{13}
$$

Notice that if a customer cannot complete the questionnaires, we can predict his/her preference according to the proposed preference similarity analysis module. The information source preference of a targeted customer can be predicted by a group of other customers who have revealed their weight preferences on the questionnaires. Alternatively, we can use the weights generated from the group consensus of AHP weight on speci<sup>fi</sup>c attributes, such as the product category, gender, and age range.

## 4. Experiments

In the following section, we conduct an empirical study based on the proposed social recommender framework. According to the evaluation results from the recommendation ratings of users participating in e-commerce, we compare the performance of the proposed framework with those of other traditional collaborative product recommendation approaches.

## 4.1. Data source

We conducted our experiments with customers using Yahoo! Shopping, which is the largest online shopping site in Taiwan. We used the product categories and corresponding products provided on the website, and invited users who had experience in purchasing products there to participate in our experiment. In the experiment, four product categories (consumer electronics, entertainment & living, boutique, health & beauty) were selected. In total, 25 different products belonging to these categories were chosen to collect decision weight preferences and product recommendation ratings from participating customers. To establish the social network of customers, we initially invited a few customers as the starting nodes and then expanded the social network by inviting friends of these starting nodes. Note that in the experiments, the relationships between users were explicitly evaluated and provided by participants because currently Yahoo! Shopping does not provide a social networking service with online shopping/auctions and thus the relationships between users could not be captured directly from the website. Speci<sup>fi</sup>cally, online questionnaires were <sup>fi</sup>rst randomly disseminated to users who had purchasing experience on Yahoo! Shopping (at least twice within the past six months). Then, the selected users further disseminated the questionnaires to their friends who met the same shopping experience criteria. This process continued until the friends of a visited user had a satisfactory shopping experience or a user was revisited. Finally, the social network was constructed by all the invited users who agree to participate in the experiments.

The survey questions in the online questionnaires for collecting social relation closeness and product rating information are included in Appendix A. In this research, Likert scales were used for social relation closeness, product preference, and importance of recommendation factors rating evaluation. The social relation closeness levels between two social nodes (direct linked users) are ranged from 1 (lowest) to 10 (highest). The product preference rating levels are ranged from 1 to 5 (very bad: 1; bad: 2; moderate: 3; good: 4; very good: 5) and the relative importance of recommendation factors was evaluated by <sup>fi</sup>ve levels: the values of 1, 3, 5, 7, and 9 respectively represent equal importance, weak importance, essential importance, demonstrated importance, and extreme importance.

Table 1  
Statistics of the experimental dataset.

<table><tr><td>Number of users invited</td><td>1075</td></tr><tr><td>Number of participants</td><td>424</td></tr><tr><td>Average connection degree of a user</td><td>2.654</td></tr><tr><td>Number of recommendation ratings collected</td><td>7199</td></tr><tr><td>Average preference similarity</td><td>0.229</td></tr><tr><td>Average recommendation trust</td><td>0.637</td></tr><tr><td>Average tie strength</td><td>4.926</td></tr></table>

In total, 1075 users were included in the social network construction stage and 424 users (174 males, 250 females) aged between 20 and 50 (47 users below 25, 341 users between 25 and 40, and 36 users above 40) participated in our experiment (successfully <sup>fi</sup>lled and returned questionnaires in product information collection stage). Table 1 shows the statistics of the dataset collected in the experiment. Figs. 2–4 depict the distributions of preference similarity between two users, recommendation trust of a user on a product, and the relation closeness (tie strength) of two directly linked users. These all show bell-shaped normal distributions.

Using the AHP, we obtained the relative importance of the factors with respect to product category, gender, and age. The distribution of these derived factor weights was used as the default factor weight setting if a customer did not reveal his/her preferred factor weight distribution or when only partial individual information was available. Table 2 shows that the importance rankings of decision factors with respect to products in different categories signi<sup>fi</sup>cantly diverge. When people purchase products of “consumer electronics,” recommendations from experts had the highest importance; however, the opinions from friends were lowest. For products of “entertainment & living,” recommendations from friends and individual preferences had the same high importance; however, the opinions from experts were lowest. For “boutique” products, the consideration of individual preference had the highest importance; however, the opinions from experts were lowest. For products of “health & beauty,” recommendations from experts had the highest importance; however, individual preferences were lowest.

Table 3 shows that the importance rankings of decision factors with respect to different genders signi<sup>fi</sup>cantly diverge. Recommendation from experts had the highest importance for male customers. However, opinions from friends were lowest. For female consumers, the consideration of individual preferences had the highest importance, but opinions from experts were lowest.

Table 4 shows that the importance rankings of decision factors with respect to different age ranges signi<sup>fi</sup>cantly diverge. The ranking of factor importance for younger customers (aged 25 or under) was identical to that of older customers (over 40). The consideration of individual preference had the highest importance. For consumers aged between 26 and 40, the relative importance levels of different factors were approximately the same, whereas the opinions from experts were less weighted.

## 4.2. Recommendation strategies

In this research, we compare our recommendation approach with <sup>fi</sup>ve benchmark approaches to evaluate the performance of the proposed system design. The six different approaches used in the experiments are described as follows.

1. Resnick model [54]: A traditional collaborative <sup>fi</sup>ltering approach that mainly uses preference similarity analysis among a customer and other recommenders.

2. Average model: A <sup>fi</sup>ltering approach that considers all three factors (preference similarity, recommendation trust, and social relation), but without exploiting the AHP criteria weighting technique. The recommendation prediction of the average model is formulated as:

$$
\operatorname{AVG} (c, j) = \overline {{R}} _ {c} + \frac {\sum_ {p \in G} \operatorname{Weight} (c , p , j) \left(R _ {p , j} - \overline {{R}} _ {p}\right)}{\sum_ {p \in G} | \operatorname{Weight} (c , p , j) |},\tag{14}
$$

$$
\text { where   Weight } = \frac {3 \cdot \text { Similarity } (c , p) \cdot \text { Trust } (p , j) \cdot \text { Relation } (c , p)}{\text { Similarity } (c , p) + \text { Trust } (p , j) + \text { Relation } (c , p)}\tag{15}
$$

3. SR model: A product <sup>fi</sup>ltering approach that exploits only preference similarity and social relation factors.

4. TR model: A product <sup>fi</sup>ltering approach that exploits only recommendation trust and social relation factors.

5. ST model: A product <sup>fi</sup>ltering approach that exploits only prefer ence similarity and recommendation trust factors.

6. STR model (our approach): A <sup>fi</sup>ltering approach that considers all three factors (preference similarity, recommendation trust, and social relation) and exploits the AHP personalized criteria weighting.

![](/api/attachments/QZJHV7WZ/fulltext/images/0150b914280817ab6fbbfb11aa8ad5d135b82123398a655dbe42ec635293ab21.jpg)  
Fig. 2. Preference similarity distribution.

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

Y.-M. Li et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/QZJHV7WZ/fulltext/images/bfc0cd3e6e9cfc2e3a84450eda3e223c7c64056fbc64e06264765e31677da121.jpg)  
Fig. 3. Recommendation trust distribution.

## 5. Results and evaluations

In order to evaluate and compare the performances of different product recommendation strategies, we randomly separated the collected 7199 product rating records into a training dataset (95%, 6839 records) and an evaluation dataset (5%, 360 records).

## 5.1. Prediction precision rate

For customer $c ,$ the recommendation level of product j predicted by the recommender system is denoted as $\Gamma _ { c , j }$ and the rating of product j evaluated by customer c is denoted as $R _ { c , j \cdot } \mathtt { A }$ recommendation prediction of product j to customer c is successful if $| { \cal { T } } _ { c , j } - { \cal { R } } _ { c , j } | < \varepsilon .$ Let $N _ { T }$ be the total recommendation predictions and $N _ { S }$ be the successful recommendation predictions. The recommendation prediction precision rate is de<sup>fi</sup>ned as:

Prediction precision rate $= N _ { S } / N _ { T } .$

16

Fig. 5 depicts the frequency distribution of the absolute value of prediction error $\mathfrak { E } = | \varGamma _ { c , j } - \varR _ { c , j } |$ . We can observe that the success frequency distribution is similar to a bell-shaped normal distribution with the highest success frequency when ε = 0.6. We can also observe that the proposed STR model has higher success frequencies than do the Resnick and average models when ε is small (smaller than 0.6) and has lower success frequencies than do the Resnick and average models when ε is large (larger than 1.5). The statistics from the distribution implies that the STR model has the best prediction accuracy and the traditional Resnick model the worst. Furthermore, we also compared the performance of the proposed approach with those of the SR, ST, and TR models. We observed that the proposed STR model has higher success frequencies than so the SR, ST, and TR models when ε is small (smaller than 0.6) and has lower success frequencies than so the SR, ST, and TR models when ε is large (larger than 1.2). The statistics from the distribution implies that the STR model has the best prediction accuracy and the TR model the worst.

Fig. 6 compares the performance of the proposed approach with those of the other models. Under the precision threshold $\varepsilon = 0 . 6 ,$ the STR model has a precision rate of 0.62, the Resnick model has a precision rate of 0.36, the average model has a precision rate of 0.44, the ST model has a precision rate of 0.47, the SR model has a precision rate of 0.50, and the TR model has a precision rate of 0.41. The results verify that a social recommender including all three factors and using the AHP personalized recommendation weighting approach has better recommendation accuracy compared with the other approaches.

Fig. 7 depicts the performance comparisons on root mean squared error (RMSE) and mean absolute error (MAE).The following <sup>fi</sup>gure depicts the RMSEs and MAEs generated from different recommendation approaches (under the precision threshold ε = 0.6). The results verify that a social recommender including all three factors and using the AHP personalized recommendation weighting approach has a

![](/api/attachments/QZJHV7WZ/fulltext/images/331a682547b22f5ad6d11d7057a70724a68872faa252ac02add021e71e07e961.jpg)  
Fig. 4. Relation closeness distribution.

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

Table 2  
Factor importance of different product categories.

<table><tr><td></td><td>Preference</td><td>Expert</td><td>Friend</td></tr><tr><td>Consumer electronics</td><td>0.318</td><td>0.385</td><td>0.297</td></tr><tr><td>Entertainment &amp; living</td><td>0.388</td><td>0.211</td><td>0.401</td></tr><tr><td>Boutique</td><td>0.375</td><td>0.306</td><td>0.319</td></tr><tr><td>Health &amp; beauty</td><td>0.316</td><td>0.358</td><td>0.326</td></tr></table>

Table 3  
Factor importance of different genders.

<table><tr><td></td><td>Preference</td><td>Expert</td><td>Friend</td></tr><tr><td>Male</td><td>0.332</td><td>0.351</td><td>0.317</td></tr><tr><td>Female</td><td>0.372</td><td>0.297</td><td>0.331</td></tr></table>

Table 4  
Factor importance of different age ranges.

<table><tr><td></td><td>Preference</td><td>Expert</td><td>Friend</td></tr><tr><td>≤25</td><td>0.467</td><td>0.337</td><td>0.196</td></tr><tr><td>26-40</td><td>0.333</td><td>0.317</td><td>0.350</td></tr><tr><td>&gt;40</td><td>0.421</td><td>0.325</td><td>0.254</td></tr></table>

signi<sup>fi</sup>cantly lower rate of recommendation error, compared with the other approaches.

To further verify the statistical signi<sup>fi</sup>cance of our comparison results, we use paired sample t-tests to con<sup>fi</sup>rm the signi<sup>fi</sup>cant difference of the prediction results with respect to various recommendation approaches and weighting models. Table 5 shows that at 95% signi<sup>fi</sup>cant level, all the test results show that the proposed STR model is signi<sup>fi</sup>- cantly different from other benchmark approaches. Therefore, it veri<sup>fi</sup>es that our proposed approach has the best performance, compared to other benchmark approaches.

Table 6 shows the results of a paired sample t-test on the results generated based on different weighting approaches. It can be veri<sup>fi</sup>ed that the personalized weighting approach has the best performance with statistical signi<sup>fi</sup>cance.

## 5.2. Recommendation precision rate

A product recommendation is made only when the recommendation level of a product predicted by the recommender system is equal to or greater than a speci<sup>fi</sup>ed value. Speci<sup>fi</sup>cally, product j is recommended to customer c when the predicted recommendation level $\begin{array} { r } { \Gamma _ { c j } > \delta , } \end{array}$ where δ is a prede<sup>fi</sup>ned recommendation threshold. The accuracy performance of a recommendation approach can be evaluated by two indexes: recommendation hit rate and recommendation loss rate. These two measures are formulated as:

$$
\begin{array}{l} \text {(1) Recommendation hit rate} = \left| \frac {\{(c , j) | \Gamma_ {c , j} \geq \delta , R _ {c , j} \geq \delta \} |}{| \{(c , j) | \Gamma_ {c , j} \geq \delta \} |} \right. \\ \text {(2) Recommendation loss rate} = \left| \frac {\{(c , j) | \Gamma_ {c , j} <   \delta , R _ {c , j} \geq \delta \} |}{| \{(c , j) | \Gamma_ {c , j} <   \delta \} |}. \right. \end{array}
$$

The <sup>fi</sup>rst measure (hit rate) calculates the probability that the products recommended by the system are also highly rated by the targeted customers. The second measure (loss rate) calculates the probability that the products not recommended by the system are highly rated by the targeted customers.

In Figs. 8 and 9, we observe that even under strict conditions (recommendation threshold $\delta = 5 )$ , the proposed STR model still has a 60% hit rate and only a 3% loss rate. The average model has a 30% hit rate and 5% loss rate. The Resnick model is unable to make any successful recommendations under this threshold level $\left( \delta = 5 \right)$ . The loss rates of the average and Resnick models are all higher than are those of the proposed STR model. This implies that the proposed model will miss fewer potential business opportunities. The experimental results verify that the proposed STR model has the highest recommendation effectiveness.

Notice that the experimental results also show that these three factors (preference similarity, recommendation trust, and social relation) should be appropriately balanced to <sup>fi</sup>t the weight preference of the target user. Otherwise, the effectiveness will deteriorate. For example, the effectiveness of the AVG model, which considers all three factors without considering the weighting preference of the target user, is worse than those of the personalized two-factor models (SR, TR, and ST models).

To further evaluate the effectiveness of the role of personalized factor importance weights in the proposed recommender system, we compared the personalized AHP weighting method with various group AHP weighting methods (product category, gender, and age) in the STR model. Figs. 10 and 11 show that the recommendation hit rate of the proposed STR model with personalized factor importance weight is higher compared with any other group relative importance weights but the loss rate is lower. These experimental results verify that the personalized factor importance method effectively improves recommendation performance. In addition, among these three group relative importance factors, we observe that although the recommendation effectiveness (higher hit rate and lower loss rate) of the importance derived from product category is lower than is personalized importance, it has a better performance compared with the others. Although personal information (e.g. gender and age) may not

![](/api/attachments/QZJHV7WZ/fulltext/images/8eb303b26be5f188adac6781b0b73407c73c220af4faa7c616d260f4ed1aecce.jpg)  
Fig. 5. The distribution of successful recommendation prediction

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

Table 5  
Y.-M. Li et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/QZJHV7WZ/fulltext/images/12c543ec7828bd214ec93b7d61e0b6f4d9768947f917ade8319a5ee8c00e7be0.jpg)  
Fig. 6. The precision rate of successful recommendation prediction.

![](/api/attachments/QZJHV7WZ/fulltext/images/f2955a4101fb3679906daf28c8c58a57a3870a52b480f9be6b67fd79dcd88765.jpg)  
Fig. 7. The RMSEs and MAEs of different recommendation approaches.

be obtainable, the recommender system could be implemented according to the default factor important weights extracted from each product category.

## 6. Conclusion

When shopping online, people tend to seek the suggestions and help of similar people, shopping experts, and close friends. However, most of current social networking platform, such as Facebook and twitter, and electronic commerce platform, such as Amazon and Yahoo! Shopping, are independently operated. The recommender systems deployed by famous electronic commerce websites, such as Amazon.com and eBay, are based on personal purchase history, aggregated rating of members, and feedbacks [58]. They generally do not consider relationships among the users and the power of social in<sup>fl</sup>uence is not exploited. To consider and balance these consulting factors, this paper proposes a social recommender system that incorporates the preference similarity, recommendation trust, and social relation analyses in order to offer product recommendations in e-commerce. Our experimental results show that the performance of the proposed social recommendation mechanism outperforms those of other benchmark approaches. The proposed framework can thus be effectively applied to electronic retailers in promoting their products and services.

Statistical veri<sup>fi</sup>cation of different recommendation models

<table><tr><td colspan="2">Paired Group</td><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>T</td><td>Sig. (2-tailed)</td></tr><tr><td>STR model</td><td>Average</td><td>-0.328</td><td>0.513</td><td>0.028</td><td>-11.550</td><td>.000</td></tr><tr><td>V.S.</td><td>Resnick</td><td>-0.453</td><td>0.647</td><td>0.036</td><td>-12.637</td><td>.000</td></tr><tr><td></td><td>ST</td><td>-0.289</td><td>0.608</td><td>0.034</td><td>-8.613</td><td>.000</td></tr><tr><td></td><td>SR</td><td>-0.249</td><td>0.559</td><td>0.031</td><td>-8.076</td><td>.000</td></tr><tr><td></td><td>TR</td><td>-0.304</td><td>0.567</td><td>0.031</td><td>-9.707</td><td>.000</td></tr></table>

## 6.1. Research contributions

The contributions and managerial implications of this paper are summarized as follows. First, from the perspective of system innovation,

Table 6  
Statistical veri<sup>fi</sup>cation of different weighting models.

<table><tr><td>Paired Group</td><td></td><td>Mean</td><td>Std. Deviation</td><td>Std. Error Mean</td><td>T</td><td>Sig. (2-tailed)</td></tr><tr><td rowspan="3">STR model personalize weighting V.S.</td><td>Age weighting</td><td>-0.151</td><td>0.373</td><td>0.021</td><td>-7.318</td><td>.000</td></tr><tr><td>Gender weighting</td><td>-0.171</td><td>0.360</td><td>0.020</td><td>-8.580</td><td>.000</td></tr><tr><td>Product weighting</td><td>-0.078</td><td>0.286</td><td>0.016</td><td>-4.927</td><td>.000</td></tr></table>

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

Y.-M. Li et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/QZJHV7WZ/fulltext/images/426d85bc6ad3d5731d9b5fd0eb18f057c30e120af7619145d0a18bcc0f7eb51b.jpg)  
Fig. 8. The recommendation hit rates of different approaches.

![](/api/attachments/QZJHV7WZ/fulltext/images/8d574559ceb4c976571bdc622ad672439822dfa376f9e63536ded5ed99ba9085.jpg)  
Fig. 9. The recommendation loss rates of different approaches.

as product recommendations in e-commerce have become increasingly popular, the designs of social recommender systems remain an emerging issue. Second, from the perspective of methodology, we not only consider the consulted sources of the group with similar interests (preference similarity) and people with expertise (recommendation trust) but also close friends (social relation) and personalized multi-criteria decision factors in the evaluation of product recommendation. Third, from the perspective of performance, better recommendation accuracy implies that our mechanism can improve the relevance of product information. Lastly, from the perspective of practice, our empirical survey shows that the importance rankings of decision factors with respect to products in different categories signi<sup>fi</sup>cantly diverge. For example, recommendations from experts have the highest importance when people purchase “consumer electronics” and “health & beauty” products. However, for

![](/api/attachments/QZJHV7WZ/fulltext/images/e36029046bfc206b033a72289461fe6c4d6148d9dbbb79ce3155685e4735c477.jpg)  
Fig. 10. The recommendation hit rates of different weighting approaches

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

Y.-M. Li et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/QZJHV7WZ/fulltext/images/ba5ec3198041fb8d0228748b1a53acc121767cc5f86ab006a7f34f7a06afc907.jpg)  
Fig. 11. The recommendation loss rates of different weighting approaches.

“entertainment & living” and “boutique” products, the consideration of individual preferences and friends' opinions becomes more important. Furthermore, the social recommender system – according to the factor weights extracted by product category – has higher effectiveness than it does for gender and age. The proposed product recommendation mechanism provides e-commerce retailers with a powerful vehicle to improve service quality, enhance customer relationships, and promote products successfully.

## 6.2. Limitations

There are several limitations to this research. First, although the social networking service is increasingly promising, the offered features of social commerce are still limited to prestigious e-commerce sites, such as Amazon and Yahoo! Shopping. Owing to platform constraints and data privacy, in the experiment we collected experimental data, such as product rating and relation closeness degree, via online questionnaires. Without these constraints, the data should be appropriately gathered from online user activities, such as product browsing and purchasing as well as information sharing and social interactions. Second, in this research product recommendation and performance evaluation were based on the level of interest in the recommended products. Although interest rating may re<sup>fl</sup>ect how much a customer likes a recommended gift, his or her purchase intention may be different. Third, owing to the constraints of the experiment, only 424 users and four product categories (25 varieties of product) were studied. Although the number of participants and varieties of products are representative and statistically explainable, an experiment on a larger scale would be helpful if more business transaction and social relation dataset are obtainable in the social commerce platform.

## 6.3. Future studies

There are some directions for future studies. First, the proposed social recommender mechanism includes three important decision factors. Other factors may be included to further enhance recommendation effectiveness. However, balancing prediction effectiveness and computational ef<sup>fi</sup>ciency should remain a concern. Second, incorporating implicit data on online user activities into the mechanism may be a desirable direction to improve the quality of the system. Speci<sup>fi</sup>cally, it would be interesting to analyze user preference, expertise reputation, and relation tie strength by mining user activities. Third, the computing methodologies for similarity, trust, relation, and MCDM techniques can be further advanced by exploiting other techniques such as arti<sup>fi</sup>cial intelligence and machine learning. Fourth, some computational issues in the design of social recommender system can be further studied. For example, the data sparsity problem [45,65] in the collaborative <sup>fi</sup>ltering environment may also occur in the social recommendation as the proposed mechanism includes the component of preference similarity which is evaluated based on the customers' product purchases and rating records. Finally, the targets of recommendations can be further extended, such as promoting a bundle of highly correlated products and social networking-driven products (e.g. group purchasing products).

## Acknowledgment

This research was supported by the National Science Council of Taiwan (Republic of China) under grant NSC 99-2410-H-009-035-MY2.

## Appendix A

In the social network construction stage, the questionnaire shown in Table 7 was used to record the information of friend list and social relation closeness. In the product information collection stage, the questionnaire shown in Table 8 was used to collect the personal product

Table 7 Social network construction questionnaire.

<table><tr><td colspan="2">Part I: Social relation closeness scale and definitions.</td></tr><tr><td>Scale</td><td>Description</td></tr><tr><td>1</td><td>I do not believe his/her suggestion.</td></tr><tr><td>2</td><td>I am dubious about his/her suggestion.</td></tr><tr><td>3</td><td>I am just listening to his/her suggestion but don&#x27;t consider it.</td></tr><tr><td>4</td><td>I will simply consider his/her suggestion.</td></tr><tr><td>5</td><td>I will carefully consider his/her suggestion.</td></tr><tr><td>6</td><td>I will seriously consider his/her suggestion.</td></tr><tr><td>7</td><td>I will keep his/her suggestion in my mind.</td></tr><tr><td>8</td><td>I will agree with his/her suggestion.</td></tr><tr><td>9</td><td>I will absolutely believe his/her suggestion.</td></tr><tr><td>10</td><td>I will make my purchase by following his/her suggestion.</td></tr><tr><td colspan="2">1. Please record name/nick-name/ID and relationship of your friends who you disseminated to according to above definitions.</td></tr><tr><td colspan="2">Name: Relationship:</td></tr><tr><td colspan="2">Name: Relationship:</td></tr><tr><td colspan="2">Name: Relationship:</td></tr></table>

Please cite this article as: Y.-M. Li, et al., A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.02.009

Product information collection questionnaire.

The purpose of this part is to understand your product preference, and importance of recommendation factors of category products, please fill in according to your personal evaluation.

<table><tr><td colspan="3">Impact assessment in accordance with the assessment scale.</td></tr><tr><td>Assessment scale</td><td>Definition</td><td>Description</td></tr><tr><td>1</td><td>Equal importance</td><td>The impact of the two reference sources are equal importance</td></tr><tr><td>3</td><td>Weak importance</td><td>Weakly in clined to the preferences of a party&#x27;s proposal</td></tr><tr><td>5</td><td>Essential importance</td><td>Essentially inclined to the preferences of a party&#x27;s proposal</td></tr><tr><td>7</td><td>demonstrated importance</td><td>Demonstrate inclined to the preferences of a party&#x27;s proposal</td></tr><tr><td>9</td><td>Extreme importance</td><td>Extremely inclined to the preferences of a party&#x27;s proposal</td></tr></table>

4. When you are looking for Category products, three different consultations will impact your final decision. Which one will impact greater? Please give it a grade.

<table><tr><td></td><td>9</td><td>7</td><td>5</td><td>3</td><td>1</td><td>3</td><td>5</td><td>7</td><td>9</td><td></td></tr><tr><td>Personal preferences</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>The advice of experts</td></tr><tr><td>Personal preferences</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>The advice of friends</td></tr><tr><td>The advice of experts</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>The advice of friends</td></tr></table>

5. How do you like the following Category products?

Please click the link to preview the product.(Source Yahoo Shopping Center)

Product 01 product page link of Yahoo!Shopping

Product 02 product page link of Yahoo!Shopping

Product 03 product page link of Yahoo!Shopping

<table><tr><td></td><td>Very Bad</td><td>Bad</td><td>Moderate</td><td>Good</td><td>Very good</td></tr><tr><td>1. Product 01</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>2. Product 02</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>3. Product 03</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr></table>

preference, and the importance of recommendation factors rating evaluation of each product category.

## References

[1] A. Abdul-Rahman, S. Hailes, Supporting trust in virtual communities, Proceedings of the Hawaii International Conference on System Sciences, Maui, Hawaji, 4–7 January, 2000.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[3] H.J. Ahn, A new similarity measure for collaborative <sup>fi</sup>ltering to alleviate the new user cold-starting problem, Information Sciences 178 (1) (2008) 37–51.

[4] R. Albert, A. Barabasi, Statistical mechanics of complex networks, Reviews of Modern Physics 74 (47) (2002) 47–97.

[5] R. Alton-Scheidl, R. Schumutzer, P.P. Sint, G. Tscherteu, Voting and Rating in Web4Groups, Oldenbourg, Vienna, Austria, 1997. 13–103.

[6] D.B. Bromley, Reputation, Image and Impression Management, Wiley-Blackwell, 1993.

[7] V. Carchiolo, A. Longheu, M. Malgeri, Reliable peers and useful resources: searching for the best personalised learning path in a trust- and recommendation-aware environment, Information Sciences 180 (10) (2010) 1893–1907.

[8] M. Chau, J. Xu, Mining communities and their relationships in blogs: a study of online hate groups, International Journal of Human Computer Studies 65 (1) (2005) 57–70.

[9] D.N. Chen, P.J.H. Hu, Y.R. Kuo, T.P. Liang, A Web-based personalized recommendation system for mobile phone selection: design, implementation, and evaluation, Expert Systems with Applications 37 (12) (2010) 8201–8210.

[10] K. Choi, D. Yoo, G. Kim, Y. Suh, A hybrid online-product recommendation system: combining implicit rating-based collaborative <sup>fi</sup>ltering and sequential pattern analysis Flectronic Commerce Research and Applications 11 (4) (2012) 309–317

[11] C. Croux, G. Haesbroeck, Principal components analysis based on robust estimators of the covariance or correlation matrix: influence functions and efficiencies Biometrika 87 (3) (2000) 603–618.

[12] P. DeMeo, A. Nocera, G. Terracina, D. Ursino, Recommendation of similar users, resources and social networks in a social internetworking scenario, Information Sciences 181 (7) (2011) 1285–1305

[13] J. Domingo-Ferrer, A. Viejo, F. Sebe, U. Gonzalez-Nicolas, Privacy homomorphisms for social networks with private relationships, Computer Networks 52 (2008) 3007–3016.

[14] L. Duckstein, S. Opricovic, Multiobjective optimization in river basin development, Water Resources Research 16 (1) (1980) 14–20

[15] R.F. Dyer, E.H. Forman, Group decision support with the analytic hierarchy process Decision Support Systems 8 (2) (1992) 99–124.

[16] A. Enders, H. Hungenberg, H. Denker, S. Mauch, The long tail of social networking, Revenue models of social networking sites. European Management Journal 26 (3) (2008) 199–211.

[17] D. Gambetta, Can we trust? in: D. Gambetta (Ed.), Trust: Making and Breaking Cooperative Relations, Basil Blackwell, Oxford, New York, 1990, pp. 213–238.

[18] T. Grandison, M. Sloman, A survey of trust in internet applications, IEEE Communications Surveys & Tutorials 3 (4) (2000) 2–16.

[19] M.S. Granovetter, The strength of weak ties, The American Journal of Sociology 78 (6) (1973) 1360–1380.

[20] J. Grau, Social commerce: personalized and collaborative shopping experiences, eMarketer, http://www.eMarketer.com2010.

[21] U. Hanani, B. Shapira, P. Shoval, Information <sup>fi</sup>ltering: overview of issues, research and systems, User Modeling and User-Adapted Interaction 11 (3) (2001) 203–259.

[22] Y. Huang, L.A. Bian, Bayesian network and analytic hierarchy process based personalized recommendations for tourist attractions over the Internet, Expert Systems with Applications 36 (1) (2009) 933–943.

[23] Z. Huang, W. Chung, H. Chen, A graph model for E commerce recommender systems, Journal of the American Society for Information Science and Technology 55 (3) (2004) 259–274.

[24] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making: Methods and Applications, Springer, Berlin, 1981.

[25] I.T. Jolliffe, Principal Component Analysis, Springer-Verlag978-0-387-95442-4, 1986. 487, http://dx.doi.org/10.1007/b98835.

[26] A. Josang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[27] D. Kempe, J. Kleinberg, E. Tardos, Maximizing the spread of in<sup>fl</sup>uence through a social network, Proceedings of ACM SIGKDD'03, 2003, pp. 137–146.

[28] I. Khan, 2011 Internet Sector Outlook — Nothing but Net, J.P. Morgan Securities LLC, 2011.

[29] Y.A. Kim, J. Srivastava, Impact of social in<sup>fl</sup>uence in e-commerce decision making, Proceedings of the ninth international conference on Electronic commerce, ACM New York, NY, USA, 2007, pp. 293–302.

[30] D.J. Kim, D.L. Ferrin, H.R. Rao, A trust-based consumer decision-making model in electronic commerce: the role of trust, perceived risk, and their antecedents, Decision Support Systems 44 (2) (2008) 544–564.

[31] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[32] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (8) (2009) 30–37.

[33] R.J. Kuo, S.C. Chi, S.S. Kao, A decision support system for selecting convenience store location through integration of fuzzy AHP and arti<sup>fi</sup>cial neural network, Computers in Industry 47 (2) (2002) 199–214.

[34] S. Lee, Analysis of relationships e-commerce on consumer decision making motivation for buying goods online. Available at SSRN: http://ssrn.com/ abstract=1918328 2010, http://dx.doi.org/10.2139/ssrn.1918328, (or).

[35] S.K. Lee, Y.H. Cho, S.H. Kim, Collaborative <sup>fi</sup>ltering with ordinal scale-based implicit ratings for mobile music recommendations, Information Sciences 180 (11) (2010) 2142–2155.

[36] K.O. Lee, N. Shi, M.K. Cheung, H. Lim, C.L. Sia, Consumer's decision to shop online: the moderating role of positive informational social in<sup>fl</sup>uence, Information Management 48 (6) (2011) 185–191.

[37] Y.H. Lee, J.H. Hu, T.H. Cheng, Y.F. Hsieh, A cost-sensitive technique for positive-example learning supporting content-based product recommendations in B-to-C e-commerce, Decision Support Systems 53 (1) (2012) 245–256.

[38] F. Li, T.C. Du, Who is talking? An ontology-based opinion leader identi<sup>fi</sup>cation framework for word-of-mouth marketing in online social blogs, Decision Support Systems 51 (1) (2011) 190–197.

[39] Y.M. Li, C.P. Kao, TREPPS: a Trust-based Recommender System for Peer Production Services, Expert Systems with Applications 36 (2) (2009) 3263–3277.

[40] X. Li, L. Liu, PeerTrust: supporting reputation-based trust for peer-to-peer electronic communities, IEEE Transactions on Knowledge and Data Engineering 16 (7) (2004) 843–857.

[41] J. Liebowitz, Linking social network analysis with the analytic hierarchy process for knowledge mapping in organizations, Journal of Knowledge Management 9 (1) (2005) 76–86.

[42] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative <sup>fi</sup>ltering, IEEE Internet Computing 7 (1) (2003) 76–80.

[43] D.R. Liu, Y.Y. Shih, Integrating AHP and data mining for product recommendation based on customer lifetime value, Information Management 42 (3) (2005) 387–400.

[44] Z.B. Liu, W.Y. Qu, H.T. Li, C.S. Xie, A hybrid collaborative <sup>fi</sup>ltering recommendation mechanism for P2P networks, Future Generation Computer Systems 26 (8) (2010) 1409–1417.

[45] Q. Liu, Y. Gao, Z.M. Peng, A novel collaborative <sup>fi</sup>ltering algorithm based on social network, Advances in Swarm Intelligence 7332 (2012) 164–174.

[46] R.J. Mooney, L. Roy, Content-based book recommending using learning for text categorization, Proceedings of the 5th ACM Conference on Digital Libraries, San Antonio TX June 2000 2000.

[47] L. Mui, M. Mohtashemi, A. Halberstadt, A computational model of trust and reputation, Proceedings of the 35th International Conference on System Science 2002 pp. 280–287.

[48] E.R. Nunez-Valdez, J.M. Cueva Lovelle, O. Sanjuan Martinez, V. Garcia-Diaz, P. Ordonez de Pablos, C.E. Montenegro Marin, Implicit feedback techniques on recommender systems applied to electronic books, Computers in Human Behavior 28 (4) (2012) 1186–1193

[49] S. Opricovic, G.H. Tzeng, Compromise solution by MCDM methods: a comparative analysis of VIKOR and TOPSIS, European Journal of Operational Research 156 (2) (2004) 445–455.

[50] P.A. Pavlou, Consumer acceptance of electronic commerce-integrating trust and risk with the technology acceptance model, International Journal of Electronic Commerce 7 (3) (2003) 69–103.

[51] M. Pazzani, A framework for collaborative, content-based, and demographic <sup>fi</sup>ltering, Arti<sup>fi</sup>cial Intelligence Review 13 (5–6) (1999) 393–408

[52] O. Phelan, K. McCarthy, B. Smyth, Using twitter to recommend real-time topical news, Proceedings of the Third ACM Conference on Recommender Systems, 2009, pp. 385–388.

[53] A. Popescul, L. Ungar, D. Pennock, S. Lawrence, Probabilistic models for uni<sup>fi</sup>ed collab orative and content-based recommendation in sparse-data environments, Proceedings of the Conference in Uncertainty in Arti<sup>fi</sup>cial Intelligence, 2001, pp. 437–444; P. Reisnick, H.R. Varian, Recommender systems, Special Issue of Communications of the ACM 40.3. 1997. 56-59

[54] P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative <sup>fi</sup>ltering of netnews, Proceedings of ACM 1994 Conference on Computer Supported Cooperative Work, New York, NY, USA, 1994, pp. 175–186.

[55] G. Rowe, G. Wright, Expert opinions in forecasting: the role of the Delphi technique, in: J.S. Armstrong (Ed.), Principles of Forecasting, Kluwer Academic Publishers, Boston, 2001, pp. 125–144.

[56] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[57] T.L. Saaty, The Analytic Network Process: Decision Making With Dependence and Feedback, Rws Publication, 2001.

[58] J.B. Schafer, J.A. Konstan, J. Riedl, E-commerce recommendation applications, Data Mining and Knowledge Discovery 5 (1–2) (2001) 115–153.

[59] J. Srivastava, N. Pathak, S. Mane, M.A. Ahmad, Data mining for social network analysis, IEEE International Conference on Data Mining, Hong Kong, 2006, pp. 18–22.

[60] P. Van Baalen, J. Bloemhof-Ruwaard, E. van Heck, Knowledge sharing in an emerging network of practice, European Management Journal 23 (2005) 300–314.

[61] W. Wang, I. Benbasat, Attributions of trust in decision support technologies: a study of recommendation agents for e-commerce, Journal of Management Information Systems 24 (4) (2008) 249–273.

[62] J.C. Wang, C.C. Chiu, Recommending trusted online auction sellers using social network analysis, Expert Systems with Applications 34 (3) (2008) 1666–1679.

[63] T.C. Wang, H.D. Lee, Developing a fuzzy TOPSIS approach based on subjective weights and objective weights, Expert Systems with Applications 36 (5) (2009) 8980–8985.

[64] Y. Wang, K.J. Lin, Reputation-oriented trustworthy computing in e-commerce environments, IEEE Internet Computing 55–59 (2008)

[65] Z.Q. Wang, M. Zhang, Y.W. Tan, W.Q. Wang, Y.X. Zhang, L. Chen, Recommendation algorithm based on graph-model considering user background information, Ninth International Conference on Creating, Connecting and Collaborating Through Computing, 2011, pp. 32–39.

[66] M. Wasko, S. Faraj, Why should I share? Examining social capital and knowledge contribution in electronic networks of practice, MIS Quarterly 29 (1) (2005) 35–58.

[67] H. Wen, L. Fang, L. Guan, A hybrid approach for personalized recommendation of news on the Web Expert Systems with Applications 39 (5) (2012) 5806–5814

[68] Y. Zhang, Y. Fang, K.K. Wei, E. Ramsey, P. McCole, H. Chen, Repurchase intention in B2C e-commerce — a relationship quality perspective, Information Management 48 (6) (2011) 192–200.

[69] L. Zhen, Z. Jiang, H. Song, Distributed recommender for peer-to-peer knowledge sharing, Information Sciences 180 (18) (2010) 3546–3561.

[70] C.N. Ziegler, J. Golbeck, Investigating interactions of trust and interest similarity, Decision Support Systems 43 (2) (2007) 460–475.

![](/api/attachments/QZJHV7WZ/fulltext/images/dcc495083bdf64041da6c58599e5bcb83f0ea146330584ee96c67827511baec5.jpg)

![](/api/attachments/QZJHV7WZ/fulltext/images/09018d25da0ed7822ec0d5959f434a0c9b1a53c5e47b2b7d3434af66af217f54.jpg)

![](/api/attachments/QZJHV7WZ/fulltext/images/ddd2d0f8684c987f33b9cda63068e5d00120029b16f25ad9c3b31fb9a735c66e.jpg)

Yung-Ming Li is a Professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, INFORMS Journal on Computing, European Journal of Operational Research, Decision Support Systems, International Journal of Electronic Commerce, Electronic Commerce Research and Applications, ICIS, WTIS, among others.

Chun-Te Wu is an information technology manager at NeoEnergy Microelectronics Inc. in Taiwan. He received his M.S. degree from the Institute of Information Management, National Chiao Tung University in Taiwan. His research interests focus on electronic commerce and mobile computing.

Cheng-Yang Lai is a Ph.D. student at the Institute of Information Management, National Chiao Tung University in Taiwan. His research interests include electronic commerce and business intelligence. His research has appeared in Electronic Commerce Research and Applications and Information Sciences.
