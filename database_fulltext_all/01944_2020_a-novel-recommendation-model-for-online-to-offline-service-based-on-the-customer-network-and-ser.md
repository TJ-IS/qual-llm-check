---
otero_id: 1944
otero_key: "2SKKUAB4"
title: "A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location"
authors: "Yuchen Pan; Desheng Wu"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2020.1759927"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location

Yuchen Pan & Desheng Wu

To cite this article: Yuchen Pan & Desheng Wu (2020) A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location, Journal of Management Information Systems, 37:2, 563-593, DOI: 10.1080/07421222.2020.1759927

To link to this article: https://doi.org/10.1080/07421222.2020.1759927

![](/api/attachments/2SKKUAB4/fulltext/images/4ce41f34d67e5fc5eb2f2880b19c1f8ae37fe61a0944965a06cf21d7fa8b1062.jpg)

View supplementary material

![](/api/attachments/2SKKUAB4/fulltext/images/7557ed67afd319c83998af2d1e576c07da7835c3f995696932904b87cce2e171.jpg)

Published online: 16 Jun 2020.

![](/api/attachments/2SKKUAB4/fulltext/images/59d8a821d6dfafcf3d84a03bdeab96b468eb3fc89ec01a3ddc2648fc0f83f17e.jpg)

Submit your article to this journal

![](/api/attachments/2SKKUAB4/fulltext/images/e585e135e277daf4eff7bf4ee7af84836fc14386fb8d9557819652fc0e6e866f.jpg)

View related articles

![](/api/attachments/2SKKUAB4/fulltext/images/9e9015e76f05596d00e46bb1239b6fa09c885d5c4162fe23072f7f48f4e20aa3.jpg)

View Crossmark data

Check for updates

# A Novel Recommendation Model for Online-to-Ofline Service Based on the Customer Network and Service Location

Yuchen Pan<sup>a</sup> and Desheng Wu<sup>a,b</sup>

<sup>a</sup>Economics and Management School, University of Chinese Academy of Sciences, Beijing, China; <sup>b</sup>Stockholm Business School, Stockholm University, Stockholm, Sweden

## ABSTRACT

We propose a new online-to-o<sup>fl</sup>ine (O2O) service recommendation method based on a novel customer network and service location (CNLRec) in order to help customer to choose the “ideal” O2O services from a large set of alternatives. Our customer network, based on the “co-used” behaviors obtained from the online rating matrix, captures customers’ online behaviors while service location re<sup>fl</sup>ects o<sup>fl</sup>ine behavior characteristic of the customer. For a target customer, a ranking of candidate services based on their locations and this network is generated, in which customer scale usage bias is eliminated. Our experimental results show that: First, even though the rating matrix is sparse, most customers are connected to our proposed customer network, which largely addresses the problem of sparse data. Second, CNLRec outperforms widely-used and state-of-the-art recommendation methods. In addition, e-commerce recommendations that use CNLRec without including item location information (CNRec) has better performance than existing methods. Third, all attributes in CNLRec, including network attributes (relationship degree and customer attribute) and location attributes, play a signi<sup>fi</sup>cant role in recommendations. Specially, O2O service location plays an important role in O2O service selection. In our research, we <sup>fi</sup>nd the optimal combinations of these attributes.

## KEYWORDS

Online-to-o<sup>fl</sup>ine model; O2O service recommendation; customer network; service location; rating matrix; sparse data

## Introduction

The emerging O2O business model, which directs customers acquired online to o<sup>fl</sup>ine stores, is becoming increasingly popular in the world. In contrast to electronic commerce (e-commerce) platforms such as Tmall and Amazon which focus on shifting customer shopping behaviors from the o<sup>fl</sup>ine to the online environment, O2O platforms, such as Dianping, are closely tied to brick-and-mortar stores. They serve as digital intermediaries that bring together costumers and merchants through group buying [28]. Customers purchase coupons from the platforms online <sup>fi</sup>rst, and then use them in o<sup>fl</sup>ine transactions. Meanwhile, the coupons are redeemed by o<sup>fl</sup>ine stores which o<sup>f</sup>er the deals. After that, customers can share their feelings on O2O platforms, including ratings and comments, of services they have experienced [15]. Studies have found that location is an important issue for businesses that bring online customers to o<sup>fl</sup>ine stores, and customers selections are location-sensitive [13]. Speci<sup>fi</sup>cally, the cost of traveling to o<sup>fl</sup>ine stores would impact the choice of service, and low transportation cost would make services more accessible. Sometimes, customers may not purchase a service despite its appeal because of its location (too far from home or o<sup>fi</sup>ce) [28]. Comparing with customers of O2O businesses, customers usually are not concerned with the locations of merchants and services in other e-commerce businesses such as Amazon and Net<sup>fl</sup>ix. Thanks to rapid delivery, customers can shop on Amazon without considering its location. This di<sup>f</sup>erence makes location an important and unique characteristic in O2O business.

According to our data, in Beijing there are 12,000 restaurants providing coupons for customers on the Dianping platform. Generally, it is di<sup>fi</sup>cult for customers to <sup>fi</sup>nd their “ideal” coupons among the vast number of coupons sold on Dianping, which results in the serious problem of information overload. Recommender systems are widely used for addressing this problem in numerous emerging e-commerce models, including Business to Business (B2B) models, Business to Customer models (B2C) and Customers to Customer models (C2C). B2B, as one of the earliest e-commerce models, provides an electronic platform for companies’ business [29]. The following two e-commerce models, B2C and C2C, such as Net<sup>fl</sup>ix and Amazon, have dramatically changed consumers’ buying habits from o<sup>fl</sup>ine shopping to online shopping. In these business models, recommender systems have already represented their e<sup>f</sup>ectiveness. For instance, Over 35% of sales on Amazon and more than 60% of Net<sup>fl</sup>ix’s income is attributed to their recommender systems [17].

Recommender systems aim to provide customers with item recommendations based on a customer’s criteria such as their preferences, shopping histories, and selections made by other customers with similar pro<sup>fi</sup>les [44]. Two types of recommender systems are typically used: content-based recommendations [9] and rating-based recommendations [7]. Content-based recommendations use items’ characteristics extracted from items’ descriptions by employing text-mining techniques to recommend items which are similar to those items that a target customer previously bought or liked [9]. This type of recommendations usually su<sup>f</sup>ers from a high calculation and time cost on text processing. In comparison, rating-based recommendations, represented by collaborative <sup>fi</sup>ltering techniques (CF), are mainly based on the rating matrix from customers’ historical behaviors [7]. CF uses this matrix to <sup>fi</sup>nd customers similar to the target customer, and recommends items to him based on what these similar customers have liked. Although rating-based recommendations avoid analyzing the content, they require a matrix consisting of a su<sup>fi</sup>cient number of initial ratings. Otherwise, they cannot generate accurate recommendations [8]. Recently, hybrid recommendation systems, which combine the advantages of rating-based and content-based methods, have outperformed many traditional systems. This improvement in performance stems not only from combining di<sup>f</sup>erent types of classical recommendation methods but also from integrating state-of-the-art techniques, such as deep learning and neural network, into recommendation models [19].

In spite of these advances in hybrid recommendation systems, rating-based recommendations are still more widely used in practice because of the ease of access to data [61]. Data for rating-based models can be acquired without engaging in the collection and cleaning of text data that is necessary in content related methods. While rating-based models are convenient, they may su<sup>f</sup>er from the data sparsity problem which results in bad recommendations, as the key process of CF is the preference similarity estimation that is based on co-used items. When data is sparse, co-used items between pairs of customers become rare, leading to inaccurate preference similarity estimations [1]. This problem is exacerbated by methods not using all of the information they could. While these methods rely exclusively on ratings to determine preference similarity between customers, there are other methods for establishing connections. In particular, customers’ service selections can also re<sup>fl</sup>ect their purchase preferences [41], and make predictions of customers’ future selections.

While having a su<sup>fi</sup>cient amount of clean data is central to recommendations, the submission of reviews for items is voluntary and self-driven in all e-commerce platforms including O2O. In other words, customers can freely decide whether to give ratings and what ratings to give. This feature of reviews raises two problems. First, customers may not give ratings after their experiences, which raises a missing data problem. Second, even if ratings exist, there is no guarantee that these ratings re<sup>fl</sup>ect customers’ true evaluations, which raises a data quality problem. Ho et al. has made substantial contributions to this issue. They <sup>fi</sup>nd customer’s decision on whether to give a rating and what rating to give are both in<sup>fl</sup>uenced by the discon<sup>fi</sup>rmation that is the discrepancy between his pre-purchase expectation and post-purchase evaluation of the same purchased product [20]. In detail, they <sup>fi</sup>nd that a customer may not give ratings when the discon<sup>fi</sup>rmation is low. Even though customers give ratings, positive discon<sup>fi</sup>rmation will in<sup>fl</sup>uence what ratings they give. Furthermore, those infrequent raters are more susceptible to discon<sup>fi</sup>rmation and therefore are more likely to give uninformative ratings. We must acknowledge data limitations due to this discon<sup>fi</sup>rmation e<sup>f</sup>ect in our research. Within the observational data that we are leveraging, we are not able to control for discon<sup>fi</sup>rmation e<sup>f</sup>ects on the customer decision of whether to give rating and what rating to give.

While e-commerce businesses mainly provide services online, the O2O business model is a combination of online and o<sup>fl</sup>ine channels. For this reason, O2O service customers comprehensively consider subjective online information (such as online reviews) and objective o<sup>fl</sup>ine characteristics (such as o<sup>fl</sup>ine locations) of candidate services in their selections. For example, in addition to the online ratings of candidate services, customers consider the o<sup>fl</sup>ine transportation costs of using them. Therefore, O2O service selection is the decision-making process which integrates online and o<sup>fl</sup>ine information of candidate services, both of which should be considered in the recommender system design. In this paper, we introduce customer network and service location into O2O service recommendation. While our proposed customer network is based on ratings of O2O services, provided online by those customers who have used them, service location is used to re<sup>fl</sup>ect o<sup>fl</sup>ine characteristics of these services. In addition, this network can also be used to address data sparsity, a common problem in recommendations. First, we present the customer network construction processes. We further explain how nodes and ties of the network are de<sup>fi</sup>ned and estimate node attributes and tie weights. Second, the ranking of candidate services based on customer network is generated in which estimation of indirect customer relationships and elimination of customers’ scale usage biases are considered. Third, we give another ranking of candidate services based on the physical distance estimation between customer central preference locations and candidate service locations. The central preference location is estimated by the center of locations of customer’s used services. Finally, a service recommendation list is created for each customer by combining these two rankings. The key contributions of this work are as follows:

First, we build a novel customer network for O2O service recommendations based on the customer-service rating matrix. In this network, nodes represent customers. If two customers have used the same services, they are connected by a tie.

Second, we explore new ways of estimating tie strength that re<sup>fl</sup>ects the degree of customer relationship. We propose to mainly use the number of co-used services to estimate tie strength, and Pearson Correlation Coe<sup>fi</sup>cient (PCC) similarity estimation is as an enhancement in this process. In addition, estimations of indirectly connected customers are considered.

Third, beside relationships, we propose a new way to estimate customer attributes from two di<sup>f</sup>erent perspectives: behavior activity and preference diversity. These two sources of information are used to re<sup>fl</sup>ect the customer experience originating from service number and service diversity, respectively. While behavior activity is an essential attribute that is not in<sup>fl</sup>uenced by other customers, preference diversity is a network attribute which we measure using degree centrality.

Fourth, we propose methods for integrating location data into the recommendation process. The physical distance between customer central preference location and candidate service location is considered in CNLRec, which is calculated by Haversine formula. Customer central preference location is estimated by the central location of used services. In addition, CNRec can be used in general e-commerce recommendations without consideration of location, which is simpli<sup>fi</sup>ed from CNLRec.

Fifth, in our models, we leverage a novel data set of O2O data acquired from Dianping, which has 636,072,722 ratings of 12,923 services generated by 502,247 customers. In addition, we mapped the locations of all services in this data set using Google Maps. Such an O2O data set with location information has not appeared in previous research.

The remainder of this paper is organized as follows. The second section brie<sup>fl</sup>y reviews the literatures on O2O business model and recommender systems. The third section describes the customer network construction processes and provides the de<sup>fi</sup>nitions and related calculations of nodes and ties within it. The fourth section presents the process of generating recommendations based on the customer network and service location. The <sup>fi</sup>fth section reports experiment results followed by the conclusions and future works in the sixth section.

## Literature Review

## O2O Business Model

The O2O business model brings together local merchants and local consumers through coupons. [28]. The unique feature of this model is the interaction between online (virtual) and o<sup>fl</sup>ine (reality). In details, service providers post service information on virtual platforms, while customers make selections of o<sup>fl</sup>ine services based on the provided information. After the experience o<sup>fl</sup>ine, customers give reviews which supplements existing service information, including spontaneous information provided by merchants and feedback from other customers, and provide more multi-dimensional decision support for other customers [15]. In addition to helping potential customers, O2O recommender systems can help suppliers to make e<sup>fi</sup>cient inventory decisions by making customer demand more predictable [42].

Much past research has been devoted to the study of online-o<sup>fl</sup>ine integration. Some researchers <sup>fi</sup>nd that customers’ perceptions of online channels are a<sup>f</sup>ected by their experiences in o<sup>fl</sup>ine channels [10, 60]. Yang proposes that perceived o<sup>fl</sup>ine service quality in<sup>fl</sup>uences perceived online service quality [60]. Moreover, customers’ trust from o<sup>fl</sup>ine channels can be transferred to online channels [10]. In addition, Tibert Verhagen <sup>fi</sup>nds that o<sup>fl</sup>ine store perceptions directly in<sup>fl</sup>uenced online purchase intention by drawing on a sample of 630 customers of a large music retail store in the Netherlands [57]. In terms of service quality, Customer purchase experiences online, in turn, a<sup>f</sup>ect o<sup>fl</sup>ine decision-making [15, 45]. Gallino and Moreno, through analysis of the BOPS project, reports that customers’ shopping intentions at brick-and-mortar stores are in<sup>fl</sup>uenced by their inventory information in online store [15]. Phang et al. <sup>fi</sup>nds that o<sup>fl</sup>ine sales are a<sup>f</sup>ected by the product promotion on social media websites [45].

In addition, location, which is a unique characteristic of O2O business that di<sup>f</sup>erentiates it from other e-commerce businesses, is an issue that has drawn the attention of scholars [5, 12]. Li et al. studied the in<sup>fl</sup>uences of transportation cost on O2O commerce with an empirical analysis of Groupon and <sup>fi</sup>nds that it a<sup>f</sup>ects the cost of deal redemption o<sup>fl</sup>ine and has signi<sup>fi</sup>cant impact on customer deal choice behavior [28]. Dickinger and Kleijnen investigate customer intentions to redeem mobile coupons, and proposes that customers usually make location-based service selections [12]. Indeed, Ardizzone and Mortara <sup>fi</sup>nd customers sometimes are not willing to buy coupons even though they have attractive prices because these services are located too far from their homes or o<sup>fi</sup>ces [5].

## Recommender Systems

Due to the overwhelming amount of information and choice available online, customers are often required to choose their preferred item from a large set of possible alternatives [29]. Driven by this phenomenon, recommendation techniques have been developed to predict personal preferences, expressed by means such as ratings, of an individual customer for items which they have not yet experienced [16]. Recommender systems have been successful in e-commerce businesses such as Amazon and Net<sup>fl</sup>ix [17]. For example, Amazon has reported that 35% of its product sales result from recommendations, and about 75% of the content chosen by subscribers on Net<sup>fl</sup>ix are the result of recommendations from the site [17].

In the recommender systems related research, recommendation algorithms can be divided into three categories: rating-based [1], content-based [9], and hybrid-based recommendations [8]. Rating-based recommendations, which generally adopt CF techniques like item-based [41] and user-based CF [64], are the most widely used due to the ease of acquiring ratings used as inputs and their low computational complexity. As the core of CF is preference similarity estimation based on a user-item rating matrix [1], it tends to su<sup>f</sup>er when the fraction of existing ratings in the matrix is too small. In this case, contentbased recommendations are e<sup>f</sup>ective because they make recommendations based on items’ descriptions and customers’ information obtained by text-mining techniques [29]. However, the data needed for content-based recommendations can be di<sup>fi</sup>cult to access and they can be prohibitively computationally complex to implement. In response to the di<sup>fi</sup>culties associated with content and rating-based recommendations, some have proposed hybrid-based methods that combine the advantages of both. For instance, Barragans-Martínez et al. describes the design, development, and startup of a TV program recommender system combining content-<sup>fi</sup>ltering and CF techniques [8].

In addition, there has been a stream of studies relating to the combination of social networking and CF [22, 30, 38, 51, 62]. In social networking, this combination is often used to recommend new people to connect to. For example, Mao et al. represents di<sup>f</sup>erent user relationships in a multigraph and develops a multigraph ranking model to identify and recommend the nearest neighbors of particular users in high-order environments [38]. Based on a CF model, Li proposes that the maximum intersection method be used to extract the optimal neighbor candidate set and presents a weighted adjusted cosine similarity method to estimate user similarity in social networks [30]. While using this combination is most popular for recommending new connections, it can also be used to recommend services [62], items [22], and activities [51].

In recent years, due to the widespread adoption of GPS devices, location information has become ubiquitous [49]. Compared with traditional e-commerce businesses, recommendations built on location-based social network (LBSN) have received more attention. These social networks use location data to help customers with decision-making by providing a list of locations that are likely to be relevant to their needs and interests [54]. Among LBSN recommendations, Point-of-interest (POI) recommendations are most commonly used in helping customers e<sup>f</sup>ectively explore their preferences [33, 37, 52]. In response to their popularity, several researchers have proposed systems for improving POI recommendations. Si proposes an adaptive POI recommendation method that combines user activity and spatial feature [52]. Lyu et al. proposes a novel POI recommendation framework, integrating user preferences with geographical, category and attribute criteria with personalized weights [37]. Liu et al. proposes a general geographical probabilistic factor model framework which strategically takes various factors into consideration [33].

In summary, there are many related studies that focus on O2O services and recommendations. Our research is inspired by social network recommendations based on locations. Unlike past research, though, our proposed customer network is based on coused behaviors instead of social relationships. In addition, the in<sup>fl</sup>uence of candidate service location on the customer decision-making process of O2O service selection has not been researched. These are the aims of this paper

## Customer Network Based on Service Selections

First, due to the voluntary and self-driven nature of service rating submissions, customers can freely decide whether to give ratings and what ratings to give. Their rating behaviors are in<sup>fl</sup>uenced by the discon<sup>fi</sup>rmation e<sup>f</sup>ect, which has been studied by Ho et al. [20]. Therefore, we acknowledge that our proposed model is based on the observed ratings. The limitations of the data we use in this study mean that we do not consider the missing ratings that should have been given by customers and the degree to which observed ratings re<sup>fl</sup>ect customers’ objective evaluations. In this section, the process of customer network generation is presented <sup>fi</sup>rst, and then the de<sup>fi</sup>nitions of nodes and ties in this network are provided. Finally, we explain the calculation of the node attributes and the tie strengths.

## Customer Network Generation

Assume $\mathbf { C } { = } \{ c _ { i } \ | \ i { \in } \{ 1 , \ . . . , \ m \} \}$ and $\mathbf { O S } { = } \{ o s _ { j } \ | \ j { \in } \{ 1 ,  . . . , n \} \}$ are the sets of m customers and n O2O services, respectively. Then, $\mathbf { R } { = } \{ r _ { i , j } | i { \in } \{ 1 ,  . . . , m \} , j { \in } \{ 1 ,  , . . . , n \} \}$ is the rating matrix of OS and $\mathbf { C } ,$ and the rating of os<sub>j</sub> given by $c _ { i }$ is represented by $r _ { i , j } .$ . Based on R, a customercustomer matrix $\mathbf { C M } = \{ c m _ { p , q } \ | \ p , q { \in } \{  1 , \ . . . , \ m \} \}$ can be generated, where $c m _ { p , q }$ is the number of co-used O2O services of $c _ { p }$ and $c _ { q } .$ . It can be calculated as follows:

$$
c m _ {p, q} = \left\{ \begin{array}{l l} \left| \mathbf {S} _ {p} \cap \mathbf {S} _ {q} \right| & p \neq q \\ \left| \mathbf {S} _ {p} \right| = \left| \mathbf {S} _ {q} \right| & p = q \end{array} \right.\tag{1}
$$

where ${ \bf S } _ { p }$ and ${ \mathsf { S } } _ { q }$ are the used service sets of $c _ { p }$ and $c _ { q } ,$ respectively, and $| \mathbf { A } |$ represents the number of elements of the set A. Obviously, customer-customer matrix is a symmetric matrix, and the diagonal element represents the number of used services by this customer.

In customer-customer matrix, when $p \neq q , c m _ { p , q }$ and $c m _ { q , p }$ are the same, which represent that there are $c m _ { p , q }$ (or $c m _ { q , p } )$ services co-used by $c _ { p }$ and $c _ { q } . $ It also represents the number of services which have nonzero ratings from both $c _ { p }$ and $c _ { q }$ in the rating matrix. When $\begin{array} { r } { \dot { p } = q , c m _ { p , p } } \end{array}$ and $c m _ { q , q }$ represent the numbers of services rated by $c _ { p }$ and $c _ { q } ,$ respectively. They also represent the numbers of nonzero elements in row c and $c _ { p }$ $c _ { q }$ of the rating matrix, respectively.

Once the customer-customer matrix has been generated, a customer network can be generated based on service selections. If $c m _ { p , q } ~ ( p \neq q )$ is not equal to $0 , \ c _ { p }$ and $c _ { q }$ are connected by a tie, indicating these two customers co-used at least one service. Formally we have the following de<sup>fi</sup>nition:

De<sup>fi</sup>nition 1: Given $G = ( \bf N , \omega T )$ , an undirected graph generated from a customer-customer matrix, we de<sup>fi</sup>ne that N and T represent a node set and tie set, respectively. On the condition that both $c _ { p }$ and $c _ { q }$ are in N, if $\left( p , ~ q \right)$ is in $\mathbf { T } , \ c _ { p }$ and $c _ { q }$ are connected in this network.

Notably, not all the customers are in N. Because the number of services used by a customer is very small, it is possible that the services a customer has used have not been used by anyone else. In this case, this customer is not in N. Therefore, the relationship between C and N can be described as following theorem:

Theorem 1:

$$
\begin{array}{l l} c _ {i} \in \mathbf {N} = > c _ {i} \in \mathbf {C} & i \in (1, m) \\ c _ {i} \in \mathbf {C} \neq > c _ {i} \in \mathbf {N} \end{array}
$$

An example of customer network generation based on real date is described in detail in online supplemental Appendix A.1. In O2O service recommendation, the number of services used by any customer is very small relative to the total number of services. According to our abstracted data, the total numbers of services and customers are 12,923 and 502,247, respectively. However, the maximum number of services used by one user $( u _ { 9 8 2 } )$ is only 42. Since customers use relatively few services in comparison with the total number available, we rely on co-used services in our models. If there are services (even one service) co-used by two customers, they are connected in the customer network, as their customer purchasing behaviors and service selection preferences are similar. In comparison, CF usually utilizes the PCC to estimate the accurate numerical distance between two items [29]. However, because of the sparse rating matrix (generally around 3% [42]), the co-used services only account for a small portion of total used services for all pairs of customers. In a sparse matrix, PCC cannot provide satisfactory estimates of the relationships between pairs of customers. Even if two customers co-use several services but give them opposite ratings, they are likely to be much more similar to each other than another pair of customers who co-used only one service and gave the same rating. This preference similarity is revealed by their using so many of the same services.

If a customer is connected to a customer network, all of the services used by the other customers in this network can be recommended to him through direct and indirect relationships. Therefore, the problem of recommendation di<sup>fi</sup>culty due to sparse data can be addressed to some extent.

## Tie Strength Estimation

In our proposed customer network, ties connect customers based on their service selection records. If two customers have co-used services, they are connected by a tie. Furthermore, tie strength is used to re<sup>fl</sup>ect the relationship of two customers who are connected. Since tie strength plays a central role in our network, deciding how to de<sup>fi</sup>ne and calculate it is important. It is important to note that our de<sup>fi</sup>nition of tie strength has important limitations. We would like to acknowledge that posting selection bias due to the discon-<sup>fi</sup>rmation e<sup>f</sup>ect exists in most e-commerce platforms [20], including O2O platforms like Dianping. The current research cannot take such e<sup>f</sup>ects into account. Nonetheless, our objective is to leveraging our observational data to develop new models.

## Service Selections versus Numerical Ratings

Customer relationship estimation based on ratings, such as PCC and Cosine, are commonly used in recommender systems [7, 29]. However, online ratings sometimes cannot re<sup>fl</sup>ect true evaluations. For example, fake reviews have been acknowledged as a critical challenge by the e-commerce industry [25]. According to research, nearly 16% of restaurant reviews that are more extreme than other reviews are marked as fake on Yelp, a popular online review platform similar to Dianping except that it does not provide coupons [36]. In many cases, reviews are likely to have been tampered with by unscrupulous businesses who attempt to manipulate the available information by posting either fake positive reviews about themselves or fake negative reviews about their competitors [11]. For example, the New York Times reported on businesses hiring workers to post fake 5-star Yelp reviews on their behalf for as little as 25 cents per review [50]. Besides fake ratings, some other factors, such as social in<sup>fl</sup>uence bias [4], discon<sup>fi</sup>rmation e<sup>f</sup>ect [20], and even free product sampling [32], may in<sup>fl</sup>uence customer ratings. All of these factors combined indicate that some ratings cannot re<sup>fl</sup>ect the objective and true evaluations of customers.

In order to ensure review quality, most O2O service platforms, such as Dianping, require customers to have experienced the services for which they are posting ratings. Therefore, a rating, regardless of its value, can only occur if the customer has purchased and used the service corresponding to his rating. In other words, a customer can only post a rating of a service whose coupon he not only purchased but also redeemed. Thus, a rating signals a service selection, which implies a purchase behavior. While review submissions encourage frivolity by require little commitment on the part of the customer, purchases encourage prudence by requiring customers to spend their own money [27]. Psychologists and economists have revealed that people usually spend money carefully as their utilities are determined by how and where to spend their money [55]. In comparison, posting a rating exerts little in<sup>fl</sup>uence on customer utility. Instead, ratings of a service mainly in<sup>fl</sup>uence the decision-making of customers who have not purchased it [31]. While a rating means an objective purchase behavior implying a prudent decision-making, its value only re<sup>fl</sup>ects a subjective evaluation that can be a<sup>f</sup>ected by many factors.

In addition, most of online platforms motivate customers to post ratings. Despite many reviews not re<sup>fl</sup>ecting customers’ true evaluations, platforms encourage ratings in the hope that these ratings can help customers make more informed purchases while increasing their dependence on the platform. In fact, customer reviews are such a central part of Dianping that the name of the site literally means “posting reviews” in Chinese. This O2O service platform encourages customers to post reviews after using services. A real example of the incentive mechanism of Dianping is described in online supplemental Appendix A.2.

While Dianping takes steps to ensure review quality, it cannot identify whether ratings truly re<sup>fl</sup>ect customers’ objective evaluations. According to descriptive statistics of our data set, 21.56% customers give 5-star ratings for all services they have used without leaving any other types of comments. It is possible that these users are simply posting reviews in order to accrue more bene<sup>fi</sup>ts that come with being at a higher level. While these users’ ratings may not re<sup>fl</sup>ect their objective evaluations, their service selections really exist as they can only give ratings for the services that they have purchased and used. Since customers are usually prudent in spending their money, their using a service implies that they had a good reason to do so [27].

## Number of Co-Used Services in Tie Strength Estimation

The generation of our proposed customer network is mainly based on co-used behaviors. To be more speci<sup>fi</sup>c, two customers are connected by a tie if they have used same services. In addition, the rating matrix is usually too sparse in recommendation research. For example, the matrix densities of our O2O data and widely-used MovieLens 100K are 9.81% and 6.03% [61], respectively. Therefore, data sparsity is a serious problem in recommendations. Studies have suggested addressing this problem by estimating the preference similarity of two customers based on the number of their co-rated items instead of their ratings [6, 56], which has also shown its e<sup>f</sup>ectiveness in our previous work [41]. In that research, we <sup>fi</sup>nd that O2O service recommendations based on the number of co-used services outperform those based on PCC. And in network related research, the number of “co-items” is a popular way to estimate tie strength, such as the number of co-occurrences in social network [47], the number of co-authorized papers in collaboration network [40], and the number of co-investments in <sup>fi</sup>rm network [21].

Based on these reasons, tie strength is de<sup>fi</sup>ned to re<sup>fl</sup>ect relationship of two customers who are connected in our proposed customer network. And it is mainly estimated by the number of co-used services (i.e., cm).

## PCC in Tie Strength Estimation

While PCC has limitations, it should not be abandoned. It can still be used to accurately estimate the relationship of two customers based on their ratings of co-used services [1, 2, 29]. Today, PCC is widely used for preference similarity estimation in many original and classical recommendation models, like CF-based models, that have satisfactory performances [3]. In addition, our previous work shows that the performance of recommendation models without PCC is clearly worse than that of models which use it, despite PCC accounting for a much smaller proportion of the preference similarity estimation compared with the number of coused services [41]. The calculation of PCC is in the following:

$$
P C C _ {p, q} = \frac {\sum_ {o s _ {i} \in \mathbf {s} _ {p} \cap \mathbf {s} _ {q}} \left(r _ {i , p} - \bar {r} _ {p}\right) \left(r _ {i , q} - \bar {r} _ {q}\right)}{\sqrt {\sum_ {o s _ {i} \in \mathbf {s} _ {p} \cap \mathbf {s} _ {q}} \left(r _ {i , p} - \bar {r} _ {p}\right) ^ {2}} \sqrt {\sum_ {o s _ {i} \in \mathbf {s} _ {p} \cap \mathbf {s} _ {q}} \left(r _ {i , q} - \bar {r} _ {q}\right) ^ {2}}}.\tag{2}
$$

where $\bar { r } _ { p }$ and $\bar { r } _ { q }$ are average ratings of used services of $c _ { p }$ and $c _ { q } ,$ respectively. Notably, the interval of PCC is [-1, 1]. As with many other models, our de<sup>fi</sup>nition of preference similarity states that a pair of customers with a negative PCC value have no correlation rather than opposite preferences [1]. Thus, only positive PCC values are used in our estimation of preference similarity as shown in the following:

$$
s i m _ {p, q} = \left\{ \begin{array}{c c} P C C _ {p, q} & P C C _ {p, q} > 0 \\ 0 & P C C _ {p, q} \leq 0 \end{array} \right.\tag{3}
$$

Intuitively, two customers who have used the same group of services will be seen as more similar if they give similar ratings for those services than if they simply co-use the services. In the case that two customers give opposite ratings to co-used services, estimation of their relationship should not be signi<sup>fi</sup>cantly in<sup>fl</sup>uenced as it is mainly determined by the co-used behaviors instead of ratings, as previously discussed. Therefore, we adopt the number of co-used services as the “main factor” and PCC as the “enhancement factor” in the tie strength estimation as follows:

$$
t s _ {p, q} = c m _ {p, q} * \left(1 + s i m _ {p, q}\right)\tag{4}
$$

where $t s _ { p , q }$ is the strength of the tie which connect $u _ { p }$ and $u _ { q }$ in the customer network. $c m _ { p , q }$ is the number of co-used service of $u _ { p }$ and $u _ { q } ,$ which is a positive integer greater than 0. In comparison, the interval of $s i m _ { p , q } ,$ as the “enhancement factor,” is [0, 1]. When two customers give opposite ratings of their co-used services, sim is equal to 0, which means that tie strength is equal to the number of co-used services (i.e., ts = sim). When sim is larger than 0, preference similarity originating from ratings on co-used services closes the “distance” (i.e. relationship) between them to some extent. However, while rating similarity plays a role, the relationship is still mainly determined by their coused behaviors according to this equation. In our de<sup>fi</sup>nition of tie strength, a high value of sim enhances the strength of the relationships that are based on the number of co-used services. To justify the use of Equation 4 in CNLRec and CNRec, we conduct comparative experiments of these two methods with four di<sup>f</sup>erent tie strength estimations in online supplemental Appendix C.2.

## Customer (Node) Attribute Estimation

In our proposed customer network, a tie describes a customer relationship and tie strength re<sup>fl</sup>ects the degree of this relationship. In addition, customers, as nodes in this network, have their own attributes due to their di<sup>f</sup>erent experiences. Customer experience can be described as a proxy for customer knowledge of a service that is gained through involvement in or exposure to it [46]. This knowledge is accrued as a customer uses a greater number and diversity of products [14]. Experienced customers tend to have richer knowledge bases regarding products [39], and also tend to post more reliable and credible product reviews [24]. Therefore, services with high evaluations from experienced customers tend to have high quality which makes them worth selecting [23]. As customer experience can be improved by accumulation of both the number and the diversity of used services, we estimate customer experience stemming from these two perspectives, represented by behavior activity and preference diversity, respectively.

A customer becomes more experienced with the increase number of products he has used [14]. In line with this perspective, we use behavior activity, estimated by the number of services a customer used, to represent customer experience. Obviously, behavior activity is an essential attribute of a customer, which cannot be in<sup>fl</sup>uenced by other customers in our proposed network. For further combinations of customer attribute, behavior activity of a customer is normalized in the following:

$$
b a _ {p} = \frac {c m _ {p , p} - c m _ {m i n}}{c m _ {m a x} - c m _ {m i n}}\tag{5}
$$

where $b a _ { \mathnormal { p } }$ is the behavior activity of $c _ { p } ,$ and has an interval of [0, 1]. The $c m _ { p , p }$ is the number of services that $c _ { p }$ has used. $c m _ { m a x }$ is the maximum number of services used by all customers on the platform. And $c m _ { m i n }$ is opposite to $c m _ { m a x } ,$ which is always equal to 1.

Besides behavior activity, a greater diversity of used products can also help customers become more experienced [43]. Indeed, sometimes quantity does not imply diversity, as a large number of services used by one customer may belong to a small number of service categories. To account for this possibility, we separately estimate customer experience originating from service diversity, represented by preference diversity, from customer experience based on behavior activity. Preference diversity of a customer is usually calculated by the number of categories that the services he has used fall into [53]. In contrast, in our proposed model we base preference diversity on the rating matrix which does not contain the information of service speci<sup>fi</sup>c categories. As customers have di<sup>f</sup>erent personalized preferences, the service categories they prefer are likely to be di<sup>f</sup>erent [58]. These di<sup>f</sup>erent preferences imply that services used by each of these customers may occur in di<sup>f</sup>erent categories. Therefore, when a customer co-used services with many other customers, these services are likely to be in di<sup>f</sup>erent categories. In other words, these services are likely to be diversi<sup>fi</sup>ed. This relationship between co-using behavior and service diversity further implies that the number of customers a customer has co-used with can re<sup>fl</sup>ect diversity of his used services to some extent. In our proposed network, this number is just the number of customers a customer is connected to. As degree centrality measures the centrality of an item based on the number of items that a given item is linked to in a network [35], we introduce it to estimate preference diversity as follows:

$$
p d _ {\mathrm{p}} = \frac {\sum_ {i = 1 , i \neq p} ^ {m} \operatorname{sgn} \bigl (\bigl | \mathbf {S} _ {i} \cap \mathbf {S} _ {p} \bigr | \bigr)}{m - 1}\tag{6}
$$

$$
\operatorname{sgn} (x) = \left\{ \begin{array}{l l} 1 & x \neq 0 \\ 0 & x = 0 \end{array} \right.\tag{7}
$$

where $p d _ { p }$ is the preference diversity of $c _ { p } ,$ and its interval is [0, 1]. The sgn (x) is the sign function. $\mathbf { S } _ { i }$ and $\mathsf { \pmb { S } } _ { P }$ represent sets of services used by $c _ { i }$ and $c _ { p } ,$ respectively. Therefore, $\left| \pmb { S } _ { i } \cap \pmb { S } _ { p } \right|$ is the number co-used services of them. A real example comparing behavior activity and preference diversity is described in online supplemental Appendix A.3. For estimating the attribute of a customer from his comprehensive experience, we combine behavior activity (i.e., ba) and preference diversity (i.e., pd) using the Cobb-Douglas function in the following way:

$$
c a _ {p} = \left(b a _ {p}\right) ^ {1 - \alpha} \cdot \left(p d _ {p}\right) ^ {\alpha}\tag{8}
$$

where $c a _ { p }$ is the estimation of $\vec { c _ { p } s }$ customer attribute. The α is the weight parameter for adjusting the in<sup>fl</sup>uence degree of ba and pd in the combination of ca, and its interval is [0,1].

## O2O Service Recommendation

In this section, we <sup>fi</sup>rst introduce the recommendation process of CNRec, including customer ranking, scale usage bias elimination, and candidate service ranking. Second, we describe a location-based O2O service recommendation (LRec), which is mainly based on the geographical distance between locations of used services and candidate services. Finally, we generate a comprehensive recommendation list of O2O candidate services based on customer network and service location.

## Service Recommendation (Ranking) Based on Customer Network (CNRec)

## Customer Ranking of Target Customer

For a target customer $c _ { p } ,$ we <sup>fi</sup>rst consider the degrees of relationships between him and other customers in the customer network, including direct relationships (i.e., the customers who connect the target customer directly) and indirect relationships (i.e., the customers who do not connect the target customer). In order to estimate the indirect relationships, we <sup>fi</sup>rst normalize the tie strength in to [0,1] as following:

$$
\begin{array}{l l} c _ {i} \in \mathbf {N} = > c _ {i} \in \mathbf {C} & i \in (1, m) \\ c _ {i} \in \mathbf {C} \neq > c _ {i} \in \mathbf {N} \end{array}\tag{9}
$$

where $t s _ { m i n }$ and $t s _ { m a x }$ are the maximum and minimum tie strengths in the customer network. Then, the degrees of relationships between $c _ { p }$ and the other customers can be described as:

$$
r d _ {p, q} \left\{ \begin{array}{c c} = t s _ {p, q} ^ {\text { Nor }} & (p, q) \in \mathbf {T} \\ = \underset {r _ {i}} {\text { Max }} \prod_ {j = 1, c _ {j} \in r _ {i}} ^ {m} t s _ {j} ^ {\text { Nor }} & c _ {p}, c _ {q} \in \mathbf {N}, r _ {i} \in \mathbf {P a t h} _ {p, q}, (p, q) \notin \mathbf {T} \end{array} \right.\tag{10}
$$

When $c _ { p }$ and $c _ { q }$ are directly connected in the customer network, the degree of their relationship $r d _ { p , q }$ is equal to $t s _ { p , q } ^ { N o r }$ . When $c _ { p }$ and $c _ { q }$ are not directly connected, we suppose $r _ { i }$ is one path from $u _ { p }$ to $u _ { q } ,$ and there are m customers on $r _ { i \cdot }$ The relationship degree of $c _ { p }$ and $c _ { q }$ on $r _ { i }$ is the product of all tie strengths on this path. All paths between $c _ { p }$ and $c _ { q }$ form the set $\mathbf { P a t h } _ { p , q } .$ Finally, $r d _ { p , q }$ is equal to the maximum product of $r _ { i }$ in $\mathbf { P a t h } _ { p , q } .$ . A real example of indirect relationship estimation is described in online supplemental Appendix A.4. The customer with a higher value of rd has a closer relationship to target customer $c _ { p }$ in the customer network, and his service preference is more similar to $c _ { p } .$ This closer relationship implies that the service selection behaviors of a customer with a higher value of rd will serve as a better basis for predicting the preferences of target customer $c _ { p } .$

In addition, customer attributes also have a signi<sup>fi</sup>cant in<sup>fl</sup>uence on how their prior ratings are used to generate service recommendations for other customers, as target customers tend to prefer services that have been rated highly by more experienced customers. Therefore, $r d _ { p , q }$ and $c a _ { q }$ are combined as follows:

$$
r i _ {p, q} = \left(c a _ {p}\right) ^ {1 - \beta} \cdot \left(r d _ {p, q}\right) ^ {\beta} q \in (1,..., m)\tag{11}
$$

where $\beta$ is the weight parameter for adjusting the relative in<sup>fl</sup>uence that ca and rd have when combined to create $r i ,$ which has an interval of [0,1]. $r i _ { p , q }$ is the recommendation in<sup>fl</sup>uence index of $c _ { q }$ to the target customer $c _ { p } .$ A larger value of $r i _ { p , q }$ means that the ratings given by $c _ { q }$ have more in<sup>fl</sup>uence on the decision-making of $c _ { p } .$ Therefore, we sort the customers in descending order based on the value of ri. This sorting results in a ranking of $c _ { q }$ for $c _ { p }$ is $R a n k _ { p , q } ( q { \in } \{ 1 , . . . , m \} , q \neq p )$

## Candidate Service Ranking of Target Customer

The ranking of candidate services provided to a target customer $c _ { p }$ is generated based on the ratings of the other customers and rankings of them. First, we suppose that $I n d e x _ { p , j } ^ { c }$ is the recommendation index of candidate service $o s _ { j } \left( o s _ { j } \notin \mathbf { S } _ { p } \right.$ and $o s _ { j } \in \mathrm { ~ O S ) }$ for $c _ { p } ,$ which is collected from the customer with the highest ranking for which an observed rating is present. In other words, $o s _ { j } \notin \mathbf { S } _ { p }$ and $o s _ { j } \in \mathrm { ~ O } \mathbf { S }$ is equal to the rating of os<sub>j</sub> given by the customer with the highest ranking for $c _ { p } .$ And then, the O2O service platform can recommend several candidate services with the highest rankings (i.e., Rank ) to $c _ { p }$ according to its business requirements. A real example of recommendation index (Index<sup>c</sup>) generation is described in online supplemental Appendix A.5.

## Scale Usage Bias Elimination

Notably, the recommendation index of a candidate service $( \mathrm { i . e . , ~ } I n d e x ^ { \mathrm { c } } )$ is equal to the rating given by one of customers who has used this service. Using a single individual’s rating to generate the recommendation index raises the possiblity that the index is in<sup>fl</sup>uenced by variations in scale usage among users. In our O2O data set, we <sup>fi</sup>nd that customers vary in their usage of the scale. Speci<sup>fi</sup>cally, only 53.2% customers use the full range of ratings on the website’s discrete <sup>fi</sup>ve-star scale (i.e., 1, 2, 3, 4 and 5). The patterns of the other customers include using only the middle of the scale (such as 2, 3 and 4) or using the upper (such as 3, 4 and 5) or lower (such as 1, 2 and 3) end of the scale. These di<sup>f</sup>erent usage patterns are termed as scale usage heterogeneity by Rossi et al. [48]. It can lead to biases in many of the analysis conducted with rating data [18]. A real example of scale usage bias is described in online supplemental Appendix A.6.

The most widely used procedure for coping with this issue is to centralize customer’s rating by subtracting the mean of all ratings and dividing by the standard deviation of them in the following fashion [18, 48]:

$$
r _ {p, i} ^ {\text {Norm}} = \frac {r _ {p , i} - \bar {r} _ {p}}{s _ {p}}\tag{12}
$$

where $r _ { p , i } ^ { N o r m }$ is the rating of $o s _ { i }$ given by $u _ { p }$ after eliminating usage scale bias. $\bar { r } _ { p }$ and $s _ { p }$ are the mean and standard deviation of all ratings given by $u _ { p } ,$ respectively. The impacts of scale usage bias elimination on the performances of our proposed methods are discussed in online supplemental Appendix C.3.

## Service Recommendation (Ranking) Based on Service Location (LRec)

Service location a<sup>f</sup>ects customer service selection in O2O businesses [28]. Customers will evaluate travel cost based on the distances between locations of candidate services and their home (or work) in their decision-makings [4]. However, in order to protect user privacy, customers’ personal addresses are not publicly available on e-commerce platforms. In addition, customers do not like to provide private personal information on public networks. Since this information in not available, we can only estimate customer preference location through his used services. For a target customer $c _ { p } ,$ we estimate his preference location by calculating the center of the locations of his used services [59] in the following way:

$$
c e n _ {p} = \left\{\frac {\sum_ {i = 1} ^ {m} L o n _ {O S _ {i}}}{m}, \frac {\sum_ {i = 1} ^ {m} L a t _ {O S _ {i}}}{m} \right\} o s _ {i} \in \mathbf {S} _ {p}\tag{13}
$$

where $c e n _ { p }$ is the central preference location of $c _ { p } .$ The ${ \bf S } _ { P }$ is the set of used services of $c _ { p } ,$ and m is the number of elements in $\mathbf { S } _ { p } \ ( \mathrm { i } . \mathrm { e } . , \mid \mathbf { S } _ { p } \mid = m )$ $L o n _ { O S _ { i } }$ and $L a t _ { O S _ { i } }$ represent the longitude and latitude of $o s _ { i } ,$ respectively. This geographic information can be obtained from Google Maps (https://maps.google.com). With this data, we calculate the physical distance between candidate service location and central preference location by adopting the Haversine formula [52]. This formula is widely used in geocoding to calculate the distance between two points based on their longitudes and latitudes as follows:

$$
\begin{array}{l} d _ {o s _ {j}, c e n _ {p}} = R * \arcsin \left[ \sin \left(L a t _ {o s _ {j}}\right) * \sin \left(L a t _ {p}\right) + \cos \left(L a t _ {o s _ {j}}\right) * \cos \left(L a t _ {p}\right) * \cos \left(L o n _ {o s _ {j}} - L o n _ {p}\right) \right. \\ \left. + \cos \left(L a t _ {o s _ {j}}\right) * \cos \left(L a t _ {p}\right) * \cos \left(L o n _ {o s _ {j}} - L o n _ {p}\right) \right] o s _ {j} \notin \mathbf {S} _ {p} a n d o s _ {j} \in \mathbf {O S} \end{array}\tag{14}
$$

where OS is the set of all services, and $o s _ { j }$ is one of the candidate services of $u _ { p } .$ $L o n _ { \mathnormal { p } }$ and $L a t _ { P }$ are the longitude and latitude of $c e n _ { p } ,$ , respectively. Similarly, $L o n _ { o s _ { j } }$ and $L a t _ { o s _ { j } }$ are the longitude and latitude of $o s _ { j } ,$ respectively. R is the radius of the earth and is equal to 6371 km [52]. Target customers are more likely to accept recommended candidate services that are closer to the customer central preference location [28]. Therefore, we rank candidate services in ascending order of $d ,$ and the ranking of $o s _ { j }$ for $u _ { p }$ is $R a n k _ { p , j } ^ { d } ~ ( o s _ { j } \notin { \bf { \sf S } } _ { p }$ and $o s _ { j } \in \mathrm { ~ O S ) }$ . Similar to CNRec, LRec used on a O2O service platform can recommend several candidate services with highest rankings $( \mathrm { i . e . , } R a n k ^ { d } )$ to $c _ { p }$ according to its business requirements.

## Service recommendation based on customer network and service location (CNLRec)

After getting these two rankings generated by CNRec and LRec, respectively, we combine them together in the following equation:

$$
I n d e x _ {p, j} = \gamma * R a n k _ {p, j} ^ {c} + (1 - \gamma) * R a n k _ {p, j} ^ {d}\tag{15}
$$

where $\gamma$ is the weight parameter for adjusting the relative weight of $R a n k _ { p , j } ^ { c }$ and $R a n k _ { p , j } ^ { d }$ in the comprehensive index. Using this score, candidate services are ranked in ascending order of $I n d e x _ { p , j } .$ . The <sup>fi</sup>nal ranking, generated from CNLRec, of candidate service $o s _ { j }$ for the target customer $u _ { P }$ is $R a n k _ { p , j }$ . Depending on the needs of O2O service platforms, several top ranked candidate services can be recommended to $u _ { p }$ based on this ranking.

All of the steps of CNLRec are illustrated in Figure 1. As shown in this <sup>fi</sup>gure, CNLRec is composed of two parts: CNRec and LRec, and each of these components can be used independently. CNRec is based on our proposed customer network, and it can be used on most e-commerce platforms if they have customer online ratings of services. LRec is a location-based recommendation method, which can be used in o<sup>fl</sup>ine recommendation scenarios where service location can be obtained and impacts customer service selection. In O2O business model, as customers purchase services online and then experience them o<sup>fl</sup>ine, they are likely to consider both online ratings and o<sup>fl</sup>ine locations of candidate services in making selections. This feature of O2O business makes CNLRec suitable for O2O services as its recommendations consider both online and o<sup>fl</sup>ine information related to services.

In order to explicitly list our contributions, we have divided steps of CNLRec into three levels: 1) the <sup>fi</sup>rst level: new steps proposed by us; 2) the second level: steps that we have borrowed but that have been used in recommendation for the <sup>fi</sup>rst time; and 3) the third level: steps borrowed from prior recommendation research.

Steps in the <sup>fi</sup>rst level are major new contributions in CNLRec, colored in light gray in Figure 1. Contributions include: (1) the generation of a novel customer-customer matrix based on the number of co-used services, and (2) a novel method for estimating tie strength based on the number of co-used services and rating-based similarity (i.e., PCC).

Steps in the second level, depicted in dark gray in Figure 1, are borrowed from extant literatures but are used for the <sup>fi</sup>rst time in recommendations by us. We make four key contributions in the second level. (1) We introduce collaboration network generation method [26] into customer network generation. (2) We introduce customer experience [24] to estimate their attributes from two perspectives: behavior activity and preference diversity. Furthermore, we adopt degree centrality [35] to estimate preference diversity in the model. (3) We eliminate scale usage bias of customers with a method proposed by Rossi et al. [48]. (4) We adopt central location calculation [59] to estimate central preference location of customers. To our knowledge, these four contributions have not been reported in existing recommendation research.

![](/api/attachments/2SKKUAB4/fulltext/images/8d7a8b73129f59a3f8dadf530dd5d6149ddaa998898b3ab5896199d59813a8a9.jpg)  
The whole process of CNLRec.

Other steps of CNLRec are in the third level. These steps are borrowed from prior recommendation research.

## Experiments

Data in experiments is from Dianping’s o<sup>fi</sup>cial website (https://www.dianping.com), Google Maps (https://maps.google.com/) and MovieLens 100K (https://grouplens.org/ datasets/movielens/100k/), which are described in online supplemental Appendix B.1 in detail. In addition, evaluation metrics of experiments are described in online supplemental Appendix B.2.

In experiments, we <sup>fi</sup>rst construct customer networks in matrix densities from 1% to 10% with a step of 1%, and analyze the characteristics of these networks. Second, we compare our proposed models with widely-used and state-of-the-art recommendation methods on our O2O data set and the MovieLens 100K, respectively. We observe the performances of these methods with the increase of matrix density to verify the validity and warranty of data sets and these methods. The parameter settings of our proposed methods are described in online supplemental Appendix B.3. We compare our model against two groups of methods: widely-used recommendation methods and state-of-the-art recommendation methods. The details of these comparative methods are described in online supplemental Appendix B.4. Third, we test di<sup>f</sup>erent values of α, β, and γ of CNLRec, to obtain the values that generate the best recommendation performance. Finally, we discuss the impacts of di<sup>f</sup>erent tie strength estimations and customer scale usage bias, respectively, on CNLRec. As space limitation, these two groups of experiments are shown in online supplemental Appendix C.2 and Appendix C.3, respectively.

## Customer Networks in Di<sup>f</sup>erent Matrix Densities

In this section, we construct customer networks in matrix densities from 1% to 10% with the step of 1% and analyze the characteristics of these networks. First, for clearly showing the networks in limited space, a partial rating matrix is used in this section. The matrix includes 7990 ratings given by 15,393 customers to 50 services. It has a density of 10.03%. Second, di<sup>f</sup>erent numbers of ratings are randomly extracted 9 times from 799 to 7191 with the step of 799. Nine matrices are generated from this randomly extracted data. These matrices have densities between approximately 1% (799 ratings) and 9% (7191 ratings) with a step of 1%. Finally, 10 customer networks are generated from these 9 matrices and the origin matrix, following the steps of customer network generation.

In Figure 2, there are two values presented under each network. The <sup>fi</sup>rst value is the density of the rating matrix which generates this network. The second value represents the connection degree, which is the fraction of the actual connections out of the maximum possible number of connections. In these experiments, if all services are connected with each other, the number of ties is 1225 $( \mathrm { i } . \mathrm { e } . , \mathrm { } c _ { 5 0 } ^ { 2 } )$ , which is the maximum possible number of connections. In the <sup>fi</sup>rst network in Figure 2, there are 86 ties in the generated network when the matrix density is 1%. The connection degree of this network is $\frac { 8 6 } { 1 2 2 5 } { = } 7 \%$ . With the increase of matrix densities, connection degree sharply increases at <sup>fi</sup>rst (matrix density < 5%) and rises steadily subsequently. Therefore, most of the customer networks have high connection degrees, implying more direct connections between customers. Because the evaluation of the relationship between two customers is more accurate when they are connected directly, the higher connection degree can improve recommendation performance.

![](/api/attachments/2SKKUAB4/fulltext/images/d64ce9452df4e005e1d357f734f4cde40262d499a26b3784071aab776dcdb00c.jpg)  
Customer networks in di<sup>f</sup>erent matrix densities.

The density of ratings matrices is larger than 3% in most electronic businesses [1]. As shown in Figure 2, when the matrix density is larger than 2%, all customers are connected to the networks, which implies that all services have the opportunity to be recommended to all customers. In other words, for each customer, all the services used by the other customers in this network could be recommended to him. This feature of our model e<sup>f</sup>ectively addresses the problems that data sparsity causes in other models.

## Comparative Experiments

## Performances of Recommendation Methods in Di<sup>f</sup>erent Training Set Densities

In experiments, 10% to 90% of (with the step of 10%) ratings are randomly extracted as training sets, and the remainder are left as testing sets. In addition, Top-k is the number of recommended services and is set as 30 (i.e., recommending 30 services to the customer), which is the default setting in most recommendation research [63, 64]. Both α and $\beta$ are set as 0.5 in this section. We will analyze the recommendation performances with di<sup>f</sup>erent parameter values in weight experiments.

Figure 3 illustrates the performances of methods evaluated by F-Score, Precision, and Recall, respectively. Generally, all curves in these six <sup>fi</sup>gures go upwards with the increase of training set densities. Since, in general, more data contains more information which can make more accurate predictions [3], this performance veri<sup>fi</sup>es the validity and warranty of O2O data set and MovieLens 100K. Furthermore, it demonstrates that our proposed methods and the comparative methods can be used in recommendations on these two data sets.

As shown in Figure 3, CNLRec and CNRec signi<sup>fi</sup>cantly outperform other methods. Four state-of-the-art methods, MF, DL, CL, and NN, have similar performance to one another, and are superior to CF methods. These results mean that our proposed customer network is e<sup>f</sup>ective in both O2O scenarios and general scenarios represented by the MovieLens 100K. As all items (i.e., O2O services or movies) are candidates which have opportunities to be recommended to each target customer, the common problem of data sparsity in recommendations is addressed to some extent. Since data density of our O2O data set (9.81%) is higher than that of MovieLens 100K (6.03%), the performance of the methods on the O2O data set are better than those on the MovieLens 100K.

For the three proposed methods on the O2O date set, CNLRec outperforms CNRec and LRec as shown in Figure 3a, b, and c. The superior performance of CNLRec implies that both online ratings and o<sup>fl</sup>ine locations are signi<sup>fi</sup>cant for businesses that bring customers from online platforms to o<sup>fl</sup>ine stores. Furthermore, this result indicates that customers evaluate candidate services based on both ratings and locations of these services in their

(f)

![](/api/attachments/2SKKUAB4/fulltext/images/77c03bf5c265dc51d4dcd163c6ea53fd9e974f910a9bacc65b824ebc7028bd63.jpg)  
The performances of recommendation methods in di<sup>f</sup>erent data densities.

selection processes. To our surprise, LRec has similar performances with state-of-the-art methods with higher algorithm complexity. These complex methods stand in contrast to LRec, which generates its recommendations based only on the distance between customer’s central preference location and candidate services. These results mean that customer selections of O2O services are location-sensitive, echoing the signi<sup>fi</sup>cance of location in this decision-making process [13, 28].

Among the comparative methods, state-of-the-art methods can deliver good performance as repeated training can make the models relatively accurate at recognizing customers’ preferences. However, when data is too sparse, these methods do not perform well. In comparison to the state-of-the-art methods, CF methods perform poorly. The key to these methods are preference similarity estimations, usually based on PCC. This estimation can generate accurate preference similarity of two customers when there are a su<sup>fi</sup>cient number of co-used items [2]. When data is sparse, though, there are few coused items, making PCC generate poor estimates of similarity and resulting in unhelpful recommendations for customers. As H-CF makes recommendations by combining both characteristics of customer behavior and service attribute, it performs slightly better than the other two CF-based methods.

## Performances of Recommendation Methods in Higher Data Densities

As the recommendation performances of methods can only be tested on existing ratings, both the training set and testing set are from the same data set [3, 29], resulting in that training set densities are lower than original data density. For instance, density of the O2O data set is 9.81%. When training set density is set as 0.6, the density of data entered in our models is only 5.866% (i.e., 9.81% \*0.6). The rest of the data is used to form the testing data set. For estimating recommendation performance of methods on higher data density, the original densities of O2O data set and the MovieLens 100K should be increased. As occasional raters who usually give few ratings are more responsive to discon<sup>fi</sup>rmation [20] and removing users who post a small number of ratings is standard practice in recommendation research for increasing data density [3], we remove customers with fewer than 12 ratings from the O2O data set and 15 ratings from the MovieLens 100K, respectively. This procedure results in an increase in density from 9.81% to 20.74% and 6.03% to 20.15%, respectively. The other model settings remain the same as those described in the <sup>fi</sup>rst part of comparative experiments. In this section, data density can be derived from training set density. For example, when training set density is 50%, both densities of the O2O data set and the MovieLens 100K entered in the models are around 10% (i.e., 20.74% \* 50% and 20.15% \* 50%). Since data densities in most e-commerce platforms do not exceed 10% in general [3, 61], we set 10% as the threshold data density (i.e., Training set density is 50%). Density above this threshold is de<sup>fi</sup>ned as highdensity, and density below it is de<sup>fi</sup>ned as low-density.

As shown in Figure 4, the results on low-density data (i.e., < 10%) are similar to those in in the <sup>fi</sup>rst part of comparative experiments, because data densities in that section (i.e., from 0.981% to 8.829% in the step of 0.981%) are low-density. In contrast, on high-density data (i.e. density > 10%), the performances of these methods begin to change. The performance of our proposed methods, CNLRec and CNRec, increase steadily on lowdensity data but slowly on high-density data. In comparison, performance of state-of-theart methods maintains the same rate of increase as on both high-density and low-density data. CF methods’ performances increases most rapidly on high-density data, resulting in that their performances rapidly converging on those of other methods’ performances. In some cases, CF methods even outperform other methods on high-density data. Speci<sup>fi</sup>cally, when data density exceeds 15%, some of state-of-the-art methods (i.e., NN and DL) begin to outperform CNLRec on the O2O data set. Furthermore, NN has better performances than CNRec on the MovieLens 100K when data density exceeds 12%.

Our proposed methods are based on the customer network. According to our experiments, when data density exceeds 2%, all customers are connected to the network and the degree of connection between them increases quickly with the increase of data density.

(a) MovieLens 100K

O2O Data Set  
![](/api/attachments/2SKKUAB4/fulltext/images/b6338459e9dc72117ecd52e8157c5c6183ff0706ded301f1114b05a7e5318a29.jpg)

![](/api/attachments/2SKKUAB4/fulltext/images/143ae5ff84fa7dedc766b3b08c4d72a86a8187856cf2da181055327eda570aca.jpg)  
(b)  
The performances of recommendation methods in higher data density.

These features e<sup>f</sup>ectively solve the data sparsity problem in recommendations. In addition, the e<sup>f</sup>ectiveness of this network in addressing the sparsity problem is improved with an increase in the degree of connection. Therefore, the performances of CNLRec and CNRec are better than those of other models, and increase steadily on low-density data. However, when data density exceeds 11%, the connection degree of customer network remains at its maximum value (i.e., 98.3%). Once this connection degree has reached its maximum value, it can no longer cause the improvement of recommendation performances of CNLRec and CNRec, since it no longer increases with the increased density. Therefore, the performance of our proposed methods cannot increase as rapidly as it does on low-density data.

In addition, while customer behavior re<sup>fl</sup>ects customer preference, incomplete data on a customer’s behaviors cannot accurately re<sup>fl</sup>ect his preference. When data density is low, the number of co-used services is very small. Rating-based preference similarity estimation, such as PCC, between this small number and ratings is unreliable, as the small number of observed behaviors of a customer cannot accurately re<sup>fl</sup>ect his preference. In comparison, the number of co-used services of two customers is based on all of their service behaviors. Nonetheless, ratings inherently contain more precise information about customer preferences. Based on enough co-used services, ratings of these services can be used to estimate customer preference similarity more accurately than the number of them. Therefore, as the number of co-used services increases with data density, performances of CF methods, based on PCC [7], become better, and even outperform our proposed methods. This result echoes widely observed outcomes of CF methods commonly used in e-commerce recommendations [2, 3, 29], and is the reason that PCC is considered in the estimation of the tie strength in our proposed methods. Similarly, as state-of-the-art methods basically rely on data training, which make their e<sup>f</sup>ectiveness increase steadily with continuous data entry [34, 63], they have steady performances. Nevertheless, our proposed methods can be used in recommendation scenarios with high-density data, since the performance of them also keep increasing with the increase of data density. In spite of the better performance of the comparative methods on high density data, real densities of data on most online platforms are generally low (< 10%) [3, 61] and hardly increase, as online platforms typically add new items and try to attract new customers for more pro<sup>fi</sup>ts. Therefore, data sparsity is a serious and common problem in recommendations [29], and rating-based recommendation methods, such as CF, are not e<sup>f</sup>ective on sparse data. In comparison, our proposed methods, CNLRec and CNRec, are e<sup>f</sup>ective on real data conditions.

In conclusion, based on our experiments on the O2O data set, when data density exceeds 15%, CNLRec underperforms compared to state-of-the-art methods. Particularly, when data density is around 20%, CF methods perform well with low algorithm complexities. Otherwise, CNLRec is more e<sup>f</sup>ective. Di<sup>f</sup>erent platforms are likely to have di<sup>f</sup>erent data conditions. For example, on e-commerce platforms, CNRec has better performance than other methods when data density is less than 12%. In a general, when data density is relatively low $( \mathrm { e . g . } , \mathrm { ~ < ~ } 1 0 \% )$ , our proposed methods are good choices for practitioners developing these platforms. When data density is higher, they should adopt state-of-theart methods for recommendations. Speci<sup>fi</sup>cally, when data density is relatively very high $( \mathrm { e . g . } > 2 0 \% )$ , CF-based methods should be considered as they have satisfactory performances and low algorithm complexities.

The performances of recommendation methods in di<sup>f</sup>erent Top-k are described in online supplemental Appendix C.1.

## Weight Experiments

There are three weight parameters, $\alpha , \beta$ and γ, in our proposed CNLRec. The α determines the in<sup>fl</sup>uence of the behavior activity and the preferences diversity in the combination of customer attribute. $\beta$ is used to adjust the in<sup>fl</sup>uence of customer attribute and the relationship degree in the combination of recommendation in<sup>fl</sup>uence index. Finally, γ is used to adjust the proportion of two service rankings, based on customer network and based on service location, in the <sup>fi</sup>nal candidate service ranking. To test di<sup>f</sup>erent levels of α, we conduct 6 groups of experiments with Top-k from 5 to 30 with a step of 5. Within each group we vary α between 0 and 1 with a step of 0.1 on data of varying densities (2%, 4%, 6%, and 8%). After <sup>fi</sup>nding the optimal value of α in this way, we conduct a similar set of experiments to <sup>fi</sup>nd the optimal value of $\beta$ using the optimal setting of α. Finally, we conduct the experiments to <sup>fi</sup>nd the optimal value of $\gamma$ using the optimal settings of α and $\beta .$

## Impact of α

α is the weight parameter, which determines the in<sup>fl</sup>uence of the behavior activity and the preference diversity in the combination of customer attributes. When $\alpha = 0 \ ( \mathrm { o r } \ \alpha = 1 )$ ,

(f)

only behavior activity (or preference diversity) is considered in customer attribute estimation. Both $\beta$ and $\gamma$ are set to 0.5 in this section.

As shown in Figure 5, the curves with relatively high data densities are mostly above curves with lower data densities, suggesting that the recommendation performance improves with the increase of data densities. This relationship between data density and performance proves the validity of these experiments. All curves have an invertedu-shaped, and the F-score reaches its maximum value at $\alpha = 0 . 6$ or $\alpha = 0 . 7$ . Notably, recommendation performance is poor when $\alpha = 0$ and $\alpha = 1$ . These experimental results indicate that both service number and service diversity are signi<sup>fi</sup>cant in customer experience estimation. Neither of them on their own can accurately estimate customer experience. In addition, service diversity is little more in<sup>fl</sup>uential than service number in customer experience formation.

![](/api/attachments/2SKKUAB4/fulltext/images/80d1723eef7d4ea99d60be13ddec161cb42110dc7e7e9790cdb9f52ba258ca83.jpg)  
(c)  
The performances of CNLRec with di<sup>f</sup>erent α.

## Impact of $\beta$

The $\beta$ is the weight parameter to determine the in<sup>fl</sup>uence of customer attributes and the relationship degree in the combination of recommendation in<sup>fl</sup>uence index. When $\beta = 0$ (or $\beta \ : = \ : 1 )$ , only the relationship degree (or the customer attribute) is considered in the recommendation in<sup>fl</sup>uence index estimation. In this part, the experiments testing di<sup>f</sup>erent values of $\beta$ are similar to those testing values of α. α are set at the optimal values obtained for any given value of $T o p \mathrm { - k }$ found in the experiments about the impact of α. γ is set as 0.5.

As shown in Figure $^ { 6 , }$ all curves show similar shapes to those depicted in Figure 5. The F-score reaches its maximum value near $\beta = 0 . 5$ . If curves are divided into two parts at their vertexes, the curves on the left sides are steeper than those on the right sides. The experimental results show that customer attribute and relationship degree have the same signi<sup>fi</sup>cance in service recommendations. Neglecting either of them will generate poor recommendation performance. In addition, when $\beta > 0 . 5 ;$ , the experimental results with $\beta$ have better performances than those with $1 \mathopen { } \mathclose \bgroup \left| - \beta \aftergroup \egroup \right. ,$ which is represented by the di<sup>f</sup>erent steepness of curves on the left and right sides of the graphs in Figure 6. For instance, the experimental results with $\beta = 0 . 7$ and $\beta = 0 . 8$ have superior performance to those with 0.3 (1–0.7) and 0.2 (1–0.8). These results imply that when customer attribute and the relationship degree do not have the same weight $( \mathrm { i . e . , } \beta \neq 0 . 5 )$ , setting a higher weight for relationship degree than for customer attribute generates better performance. Reversing the weights results in a decline in performance. For example, $\beta = 0 . 7$ and $\beta = 0 . 3$ represent the weights cases where the weights on relationship degree and the customer attribute are 0.7. In this case, experimental results with $\beta = 0 . 7$ have better performance than those with $\beta = 0 . 3$ . These results mean that the relationship degree is more in<sup>fl</sup>uential than customer attribute. Furthermore, this relationship implies that customer connection is the key to CNLRec’s recommendation performance in sparse data.

## Impact of γ

The γ is the weight parameter to adjust the proportion of two service rankings, based on customer network and based on service location, in the <sup>fi</sup>nal candidate service ranking. The model is identical to LRec when $\gamma = 0$ . Similarly, $\gamma = 1$ means that the model is identical to CNRec. In this part, α and $\beta$ are set to the optimal values obtained for di<sup>f</sup>erent values of Top-k in the aformentioned experiments.

As shown in Figure 7, all curves have an inverted-u-shaped. Furthermore, in most experiments, CNLRec has the best performances when $\gamma = 0 . 6 ,$ which represents that both customer network and service location are signi<sup>fi</sup>cant. This result means O2O service selection is the decision-making process in which customers consider both online and o<sup>fl</sup>ine information of candidate services, as O2O business is the combination of online and o<sup>fl</sup>ine channels. This result also echoes prior results showing that customer selection in businesses that bring customers from an online platform to an o<sup>fl</sup>ine store are locationsensitive [13], which is di<sup>f</sup>erent from other online e-commerce businesses such as Amazon and Net<sup>fl</sup>ix. Service location, as the o<sup>fl</sup>ine information and unique factor in O2O business, shows its signi<sup>fi</sup>cance in customer decision on O2O service selection. In addition, CNLRec when $\gamma = 1$ , performs better than when $\gamma = 0$ as shown in Figure 7. This result implies that customer preference estimation based on online information is still the core of recommendations [29], including location-related scenarios.

![](/api/attachments/2SKKUAB4/fulltext/images/00ba6d034bd21a68e2e3dc1a5ff8aca1b97603c60544cffcd486f0c652c8abd0.jpg)  
(a)

![](/api/attachments/2SKKUAB4/fulltext/images/a541f8e612756aeb95a17e1aa528a6c55e2f664454a0783151626dfe06d58755.jpg)  
(d)

![](/api/attachments/2SKKUAB4/fulltext/images/a82c58ce8e53ff8fc3f2ce976f900253183c2c84596bb39a4721c7f508149df8.jpg)  
(b)

![](/api/attachments/2SKKUAB4/fulltext/images/2888244be2dc3c0f4dd9a99e7e62d493b4af6c732904e618f20182fcc738144f.jpg)  
(e)

![](/api/attachments/2SKKUAB4/fulltext/images/374cff8ff7451729b9f5208dc91fec8b1f241cb04810f477bfec322e1a47c455.jpg)  
(c)

![](/api/attachments/2SKKUAB4/fulltext/images/d21dae5a4f632dd63b3cde4aaf3762b6b8c65c2bf80982e1a54e81553d5c268c.jpg)  
(f)  
The performances of CNLRec with di<sup>f</sup>erent $\beta .$

## Conclusion

In this paper, we proposed CNLRec, a novel O2O service recommendation method based on customer network and service location. Our recommendation method is unique in that it considers both online and o<sup>fl</sup>ine characteristics of O2O services, stemming from their online ratings and o<sup>fl</sup>ine locations, respectively. Our customer network is based on the online rating matrix. In this network, a tie re<sup>fl</sup>ects customer relationships based on their service behaviors. The degree of this relationship is determined by the number and ratings of co-used services. Experimental results show that the relationship degree should be mainly estimated by the number of co-used services and be adjusted (or enhanced) by PCC based on ratings of these services. In addition, in the network nodes represent customers whose attributes are estimated by their experiences. As customer experience is produced by the accumulation of the number and diversity of used services, we estimate it from two di<sup>f</sup>erent perspectives: behavior activity and preference diversity. The presented experiments show that both of these perspectives are signi<sup>fi</sup>cant in customer experience estimation.

![](/api/attachments/2SKKUAB4/fulltext/images/0bb67c1df5c997fb6271f056d179c1eb073aa37caa1adeed60785d4f6fda2de9.jpg)  
(c)  
(f)  
The performances of CNLRec with di<sup>f</sup>erent γ.

Service location is the o<sup>fl</sup>ine information of a service provider. In this study we <sup>fi</sup>nd that it plays a central role in O2O service selection. As coupons purchased online can only be redeemed at o<sup>fl</sup>ine stores, customers must consider the locations of these stores. Therefore, O2O service selection is a location-sensitive decision-making process.

In our experiments, CNLRec clearly outperforms state-of-the-art and widely-used recommendation methods on O2O data set. In general recommendation, such as movie recommendation, CNLRec can be simpli<sup>fi</sup>ed to CNRec, based only on our proposed customer network. CNRec has better performances than comparison methods as well, as this network can connect most customers within a network, which addresses the problem of sparse data found in many applications. In addition, we further explore situations where these recommendation models might be used. We <sup>fi</sup>nd that our proposed methods do not always have better performances than others, and state-of-the-art and widely-used recommendation methods can be adopted when data density is relatively high. Moreover, experimental results show that scale usage bias exists in rating behaviors, and scale usage bias elimination can improve recommendation performance.

There are several issues related to the current research that could be studied in greater depth. First, multi-source heterogeneous data, such as text, audio and video, should be considered in O2O service recommendation. The inclusion of this type of data may make the results of recommendation systems more accurate. Second, if the data on real-time geographic information can be accessed, timeliness of recommendations can be studied in future.

## Funding

This work was supported by the National Natural Science Foundation of China under Grant 71825007, in part by the Chinese Academy of Sciences Frontier Scienti<sup>fi</sup>c Research Key Project under Grant QYZDB-SSW-SYS021, in part by the Marianne and Marcus Wallenberg Foundation under Grant MMW 2015.0007, in part by the Strategic Priority Research Program of CAS under Grant XDA23020203, in part by the supported by the International Partnership Program of Chinese Academy of Sciences, Grant No.211211KYSB20180042, and supported by the Junior Fellowships of CAST Advanced S&T Think-tank Programs-Doctoral Programs (Grant CXY-ZKQN-2019-042).

## Reference

1. Adomavicius, G.; and Tuzhilin, A. Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, 17, 6 (2005), 734–749.

2. Adomavicius, G.; Zan, H.; and Tuzhilin, A. Personalization and recommender systems. INFORMS Tutorials on Operations Research (2008), 55–107. https://pubsonline.informs.org/ doi/abs/10.1287/educ.1080.0044

3. Adomavicius, G.; and Zhang, J. Classi<sup>fi</sup>cation, ranking, and top-K stability of recommendation algorithms. INFORMS Journal on Computing, 28, 1 (2016), 129–147.

4. Aral, S. The problem with online ratings. MIT Sloan Management Review, 55, 2 (2014), 47.

5. Ardizzone, A.; and Mortara, A. Consumers motivations and daily deal promotions. The Qualitative Report, 19, 31 (2014), 1–15.

6. Bag, S.; Kumar, S.K.; and Tiwari, M.K. An e<sup>fi</sup>cient recommendation generation using relevant Jaccard similarity. Information Sciences, 483(2019), 53–64.

7. Banerjee, S.; Sanghavi, S.; and Shakkottai, S. Online collaborative <sup>fi</sup>ltering on graphs. Operations Research, 64, 3 (2016), 756–769.

8. Barragans-Martínez, A.B.; Costa-Montenegro, E.; Burguillo, J.C.; Rey-Lopez, M.; Mikic-Fonte, F.A.; and Peleteiro, A. A hybrid content-based and item-based collaborative <sup>fi</sup>ltering approach to recommend TV programs enhanced with singular value decomposition. Information Sciences, 180, 22 (2010), 4290–4311.

9. Besbes, O.; Gur, Y.; and Zeevi, A. Optimization in online content recommendation services: beyond click-through rates. Manufacturing & Service Operations Management, 18, 1 (2016), 15–33.

10. Bock, G.-W.; Lee, J.; Kuan, H.-H.; and Kim, J.-H. The progression of online trust in the multi-channel retailer context and the role of product uncertainty. Decision Support Systems, 53, 1 (2012), 97–107.

11. Dellarocas, C. Strategic manipulation of internet opinion forums: implications for consumers and <sup>fi</sup>rms. Management Science, 52, 10 (2006), 1577–1593.

12. Dickinger, A.; and Kleijnen, M. Coupons going wireless: determinants of consumer intentions to redeem mobile coupons. Journal of Interactive Marketing, 22, 3 (2008), 23–39.

13. Fang, Z.; Gu, B.; Luo, X.; and Xu, Y. Contemporaneous and delayed sales impact of location-based mobile promotions. Information Systems Research, 26, 3 (2015), 552–564.

14. Friedman, H.H.; and Friedman, L. Endorser e<sup>f</sup>ectiveness by product type. Journal of Advertising Research, 19, 5 (1979), 63–71.

15. Gallino, S.; and Moreno, A. Integration of online and o<sup>fl</sup>ine channels in retail: the impact of sharing reliable inventory availability information. Management Science, 60, 6 (2014), 1434–1451.

16. Ghoshal, A.; Kumar, S.; and Mookerjee, V. Impact of recommender system on competition between personalizing and non-personalizing <sup>fi</sup>rms. Journal of Management Information Systems, 31, 4 (2015), 243–277.

17. Gomez-Uribe, C.A.; and Hunt, N. The Net<sup>fl</sup>ix recommender system: algorithms, business value, and innovation. ACM Transactions on Management Information Systems, 6, 4 (2015), 1–19.

18. Greenleaf, E.A. Improving rating scale measures by detecting and correcting bias components in some response styles. Journal of Marketing Research, 29, 2 (1992), 176–188.

19. Guan, Y.; Wei, Q.; and Chen, G. Deep learning based personalized recommendation with multi-view information integration. Decision Support Systems, 118(2019), 58–69.

20. Ho, Y.-C.; Wu, J.; and Tan, Y. Discon<sup>fi</sup>rmation e<sup>f</sup>ect on online rating behavior: a structural model. Information Systems Research, 28, 3 (2017), 626–642.

21. Hochberg, Y.V.; Lindsey, L.A.; and Wester<sup>fi</sup>eld, M.M. Resource accumulation through economic ties: evidence from venture capital. Journal of Financial Economics, 118, 2 (2015), 245–267.

22. Ji, K.; and Shen, H. Jointly modeling content, social network and ratings for explainable and cold-start recommendation. Neurocomputing, 218(2016), 1–12.

23. Jiménez, F.R.; and Mendoza, N.A. Too popular to ignore: the in<sup>fl</sup>uence of online reviews on purchase intentions of search and experience products. Journal of Interactive Marketing, 27, 3 (2013), 226–235.

24. Koo, D.-M. Impact of tie strength and experience on the e<sup>f</sup>ectiveness of online service recommendations. Electronic Commerce Research and Applications, 15(2016), 38–51.

25. Lappas, T.; Sabnis, G.; and Valkanas, G. The impact of fake reviews on online visibility: a vulnerability assessment of the hotel industry. Information Systems Research, 27, 4 (2016), 940–961.

26. Lee, C.; Pham, M.; Jeong, M.K.; Kim, D.; Lin, D.K.J.; and Chavalitwongse, W.A. A network structural approach to the link prediction problem. INFORMS Journal on Computing, 27, 2 (2015), 249–267.

27. Levav, J.; and Mcgraw, A.P. Emotional accounting: how feelings about money in<sup>fl</sup>uence consumer choice. Journal of Marketing Research, 46, 1 (2009), 66–80.

28. Li, H.; Shen, Q.; and Bart, Y. Local market characteristics and online-to-o<sup>fl</sup>ine commerce: an empirical analysis of Groupon. Management Science, 64, 4 (2017), 1477–1973.

29. Li, L.; Chen, J.; and Raghunathan, S. Recommender system rethink: implications for an electronic marketplace with competing manufacturers. Information Systems Research, 29, 4 (2018), 1003–1023.

30. Li, W.; Cao, J.; Wu, J.; Huang, C.; and Buyya, R. A collaborative <sup>fi</sup>ltering recommendation method based on discrete quantum-inspired shu<sup>fl</sup>ed frog leaping algorithms in social networks. Future Generation Computer Systems, 88(2018), 262–270.

31. Li, X. Impact of average rating on social media endorsement: the moderating role of rating dispersion and discount threshold. Information Systems Research, 29, 3 (2018), 739–754.

32. Lin, Z.; Zhang, Y.; and Tan, Y. An empirical study of free product sampling and rating bias. Information Systems Research, 30, 1 (2019), 260–275.

33. Liu, B.; Xiong, H.; Papadimitriou, S.; Fu, Y.; and Yao, Z. A general geographical probabilistic factor model for point of interest recommendation. IEEE Transactions on Knowledge and Data Engineering, 27, 5 (2015), 1167–1179.

34. Liu, J.; Wu, C.; Xiong, Y.; and Liu, W. List-wise probabilistic matrix factorization for recommendation. Information Sciences, 278(2014), 434–447.

35. Lu, B.; Guo, X.; Luo, N.; and Chen, G. Corporate blogging and job performance: e<sup>f</sup>ects of work-related and nonwork-related participation. Journal of Management Information Systems, 32, 4 (2015), 285–314.

36. Luca, M.; and Zervas, G. Fake it till you make it: reputation, competition, and Yelp review fraud. Management Science, 62, 12 (2016), 3412–3427.

37. Lyu, Y.; Chow, C.-Y.; Wang, R.; and Lee, V.C.S. iMCRec: a multi-criteria framework for personalized point-of-interest recommendations. Information Sciences, 483(2019), 294–312.

38. Mao, M.; Lu, J.; Zhang, G.; and Zhang, J. Multirelational social recommendations via multigraph ranking. IEEE Transactions on Cybernetics, 47, 12 (2017), 4049–4061.

39. Nel, J.; and Bosho<sup>f</sup>, C. Online customers’ habit-inertia nexus as a conditional e<sup>f</sup>ect of mobile-service experience: a moderated-mediation and moderated serial-mediation investigation of mobile-service use resistance. Journal of Retailing and Consumer Services, 47(2019), 282–292.

40. Newman, M.E.J. Coauthorship networks and patterns of scienti<sup>fi</sup>c collaboration. Proceedings of the National Academy of Sciences, 101, suppl 1 (2004), 5200–5205.

41. Pan, Y.; Wu, D.; and Olson, D.L. Online to o<sup>fl</sup>ine (O2O) service recommendation method based on multi-dimensional similarity measurement. Decision Support Systems, 103(2017), 1–8.

42. Pan, Y.; Wu, D.; Luo, C.; and Dolgui, A. User activity measurement in rating-based online-too<sup>fl</sup>ine (O2O) service recommendation. Information Sciences, 479(2019), 180–196.

43. Park, C.W.; Mothersbaugh, D.L.; and Feick, L. Consumer knowledge assessment. Journal of Consumer Research, 21, 1 (1994), 71–82.

44. Pathak, B.; Gar<sup>fi</sup>nkel, R.; Gopal, R.D.; Venkatesan, R.; and Yin, F. Empirical analysis of the impact of recommender systems on sales. Journal of Management Information Systems, 27, 2 (2010), 159–188.

45. Phang, C.W.; Tan, C.-H.; Sutanto, J.; Magagna, F.; and Lu, X. Leveraging O2O commerce for product promotion: an empirical investigation in mainland China. IEEE Transactions on Engineering Management, 61, 4 (2014), 623–632.

46. Ratchford, B.T. The economics of consumer knowledge. Journal of Consumer Research, 27, 4 (2001), 397–411.

47. Rishika, R.; and Ramaprasad, J. The e<sup>f</sup>ects of asymmetric social ties, structural embeddedness, and tie strength on online content contribution behavior. Management Science, 65, 7 (2019), 3398–3422.

48. Rossi, P.E.; Gilula, Z.; and Allenby, G.M. Overcoming scale usage heterogeneity. Journal of the American Statistical Association, 96, 453 (2001), 20–31.

49. Sarwat, M.; Levandoski, J.J.; Eldawy, A.; and Mokbel, M.F. LARS\*: An e<sup>fi</sup>cient and scalable location-aware recommender system. IEEE Transactions on Knowledge and Data Engineering, 26, 6 (2014), 1384–1399.

50. Segal, D. A rave, a pan, or just a fake?. http://www.nytimes.com/2011/05/22/your-money /22haggler.html: New York Times, 2011.

51. Shahmohammadi, A.; Khadangi, E.; and Bagheri, A. Presenting new collaborative link prediction methods for activity recommendation in Facebook. Neurocomputing, 210(2016), 217–226.

52. Si, Y.; Zhang, F.; and Liu, W. An adaptive point-of-interest recommendation method for location-based social networks based on user activity and spatial features. Knowledge-Based Systems, 163(2019), 267–282.

53. Song, Y.; Sahoo, N.; and Ofek, E. When and how to diversify—a multicategory utility model for personalized content recommendation. Management Science 65, 8 (2019), 1–21.

54. Stepan, T.; Morawski, J.M.; Dick, S.; and Miller, J. Incorporating spatial, temporal, and social context in recommendations for location-based social networks. IEEE Transactions on Computational Social Systems, 3, 4 (2016), 164–175.

55. Sussman, A.B.; and O’Brien, R.L. Knowing when to spend: unintended <sup>fi</sup>nancial consequences of earmarking to encourage savings. Journal of Marketing Research, 53, 5 (2016), 790–803.

56. Tan, S.; Bu, J.; Qin, X.; Chen, C.; and Cai, D. Cross domain recommendation based on multi-type media fusion. Neurocomputing, 127(2014), 124–134.

57. Verhagen, T.; and van Dolen, W. Online purchase intentions: a multi-channel store image perspective. Information & Management, 46, 2 (2009), 77–82.

58. Yan, Q.; Zhang, L.; Li, Y.; Wu, S.; Sun, T.; Wang, L.; and Chen, H. E<sup>f</sup>ects of product portfolios and recommendation timing in the e<sup>fi</sup>ciency of personalized recommendation. Journal of Consumer Behaviour, 15, 6 (2016), 516–526.

59. Yang, D.; Zhang, D.; Zheng, V.W.; and Yu, Z. Modeling user activity preference by leveraging user spatial temporal characteristics in LBSNs. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 45, 1 (2015), 129–142.

60. Yang, S.; Lu, Y.; and Chau, P.Y.K. Why do consumers adopt online channel? An empirical investigation of two channel extension mechanisms. Decision Support Systems, 54(2013), 858–869.

61. Zhang, Q.; Wu, D.; Lu, J.; Liu, F.; and Zhang, G. A cross-domain recommender system with consistent information transfer. Decision Support Systems, 104(2017), 49–63.

62. Zhang, W.; Zhang, S.; Chen, Y.; and Pan, X. Combining social network and collaborative <sup>fi</sup>ltering for personalised manufacturing service recommendation. International Journal of Production Research, 51, 22 (2013), 6702–6719.

63. Zhang, W.; Du, Y.; Yoshida, T.; and Yang, Y. DeepRec: a deep neural network approach to recommendation with item embedding and weighted loss function. Information Sciences, 470 (2019), 121–140.

64. Zhang, Z.; Kudo, Y.; and Murai, T. Neighbor selection for user-based collaborative <sup>fi</sup>ltering using covering-based rough sets. Annals of Operations Research, 256, 2 (2017), 359–374.

## About the Authors

Yuchen Pan (panyuchen16@mails.ucas.ac.cn/panyuchenucas@163.com) is working toward the Ph.D. degree at the School of Economics and Management, University of Chinese Academy of Sciences, Beijing, China. His research interests include recommender systems and data mining.

Desheng Wu (dash@risklab.ca) is with the School of Economics and Management, University of Chinese Academy of Sciences, Beijing, China, and also with the Stockholm Business School, Stockholm University, Sweden. His research interests include enterprise risk management in operations, performance evaluation in <sup>fi</sup>nancial industry, and decision sciences. Dr. Wu has authored or coauthored more than 100 papers in refereed journals, such as Production and Operations Management, Decision Support Systems, Decision Sciences, Risk Analysis, IEEE Transactions on Systems Man and Cybernetics, and others. He has served as Associate or Guest Editor of several journals.
