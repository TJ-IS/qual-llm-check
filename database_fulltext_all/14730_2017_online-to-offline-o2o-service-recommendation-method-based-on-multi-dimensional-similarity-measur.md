---
otero_id: 14730
otero_key: "QUF3CACD"
title: "Online to offline (O2O) service recommendation method based on multi-dimensional similarity measurement"
authors: "Yuchen Pan; Desheng Wu; David L. Olson"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Online to offline (O2O) service recommendation method based on multi-dimensional similarity measurement

ELSEVIER Decision Support Systems

Yuchen Pan, Desheng Wu, David L. Olson

![](/api/attachments/QUF3CACD/fulltext/images/017401520dfb81c972d3a2220598276c67a6e052599b5653ec12af72552c5d81.jpg)

PII: S0167-9236(17)30146-X

DOI: doi: 10.1016/j.dss.2017.08.003

Reference: DECSUP 12869

To appear in: Decision Support Systems

Received date: 2 February 2017

Revised date: 27 July 2017

Accepted date: 8 August 2017

Please cite this article as: Yuchen Pan, Desheng Wu, David L. Olson , Online to offline (O2O) service recommendation method based on multi-dimensional similarity measurement, Decision Support Systems (2017), doi: 10.1016/j.dss.2017.08.003

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Online to Offline (O2O) Service Recommendation Method Based on Multi-dimensional Similarity Measurement

Yuchen Pan, University of the Chinese Academy of Sciences, Beijing

Desheng Wu, Stockholm University dwu@ucas.ac.cn

David L. Olson, University of Nebraska (corresponding author) dolson3@unl.edu

## Abstract

With the rapid development of information technology, consumers are able to search for and buy services or products online, and then consume them in an offline store. This emerging ecommerce model is called online to offline (O2O) service, which has attracted business and academic attention. The large number of O2O services on the Internet creates a scalability problem, creating massive but highly sparse matrices relating customers to items purchased. In this paper, we proposed a novel O2O service recommendation method based on multidimensional similarity measurements. This approach encompasses three similarity measures: collaborative similarity, preference similarity and trajectory similarity. Experimental results show that a combination of multiple similarity measures performs better than any one single similarity measure. We also find that trajectory similarity performs better than the rating-based similarity metrics (collaborative similarity and preference similarity) in sparse matrices.

Key words: O2O service, recommendation system, similarity measurement, sparse matrix

## Online to Offline (O2O) Service Recommendation Method Based on Multi-dimensional Similarity Measurement

## 1 Introduction

Electronic commerce has continued its rapid growth, providing great opportunities and challenges for both consumers and suppliers. Online access to markets progresses on a scale of real-time, offering consumers a near-infinite number of opportunities for products and services. Thus, it would be valuable to utilize automated systems to aid consumers in their search for providers. Rampell [1] suggested the field of online to offline (O2O) commerce in 2010.

Yang et al. [2] examined factors influencing consumers to select online or offline channels. O2O commerce is a kind of business approach that attracts potential customers from online to offline physical stores. Customers can be classified by online channels (for instance email or website advertisement). These customers might be induced to leave the online space through different mechanisms. This business approach organically combines experience and techniques in online marketing and brick-and-mortar marketing. O2O commerce can be categorized into three kinds of services: information comments on O2O service, intelligent navigation of O2O services and payment O2O services (i.e. dianping.com and meituan.com).

As the most influential and widely used O2O commercial category, payment O2O service has had an impact on many people’s life styles. Group buying O2O services allow customers to buy the coupons first and then to consume them in offline stores. These customers can also give the ratings and comments of the services they have experienced offline. There are one hundred thousand restaurants providing group buying O2O services in Beijing alone on dianping.com. Customers are swamped with choices, making it difficult to make the best decision in selecting the most appropriate O2O services for themselves.

# ACCEPTED MANUSCRIPT

Recommendation systems have been widely utilized in e-commerce [3, 4]. The classical personalized recommendation method of Collaborative Filtering (CF) is the most common approach to deal with the information explosion problem. It has been found to be effective in service recommendation [5], and is utilized by Amazon and ebay. The core of CF is similarity estimation of every pair of users, reflecting the behavioral tendency of target users based on their most similar neighbors. Pearson Correlation Coefficient (PCC) is a typical similarity measurement method, but it ignores ranking preference and user service history. Additionally, since PCC is a numerical calculation, it cannot operate on sparse matrices, and most user-service matrices in this problem area are very sparse.

Therefore, we propose an O2O service recommendation method based on multidimensional similarity, combining collaborative similarity, preference similarity and trajectory similarity. The intent is to compare performance in sparse matrices. The remainder of this paper is organized as follows: Section 2 reviews literatures on O2O service, recommendation systems, collaborative filtering, and similarity estimation in recommender systems. Section 3 describes collaborative similarity, preference similarity and trajectory similarity measurements. Section 4 presents our O2O service recommendation model based on similarity calculated in Section 3. Section 5 reports comparative results of experiments followed by the conclusions and suggestions for future work in section 6.

## 2. Literature Review

O2O has received a lot of research attention in recent years. Many papers have proposed the technology acceptance model for both online and physical stores [6]. Quality of system and information has also been proposed to measure online consumer attitudes [7]. Indeed, consumer trust has been found to travel across online and offline sources [8]. There is evidence, conversely, that loyalty programs work better online than in offline markets, at least in part due to the need to physically visit off-line stores [9]. In reputation management of O2O e-commerce markets, Xiao and Dong [10] proposed a new reputation management system (HSMM-RMS) using a semi-Markov model by combining observable online and offline raw reputation information. Online and offline commerce have been related to the price mechanism with the purpose of finding similarities and differences between electronic commerce and traditional shopping modes [11- 14]. The difference between online and offline systems have been studied from different aspects [15, 16]. However, most published studies have taken the marketing view of O2O, not considering O2O service recommendation.

Personalized recommendation methods are the most common approaches to solve the information scalability problem [3, 4], and have been found to be more efficient in service including CF-based [18, 19], and memory-based recommendation [20]. These researchers also considered the factor of time in service recommendation [21]. In service recommendation research, collaborative filtering (CF) has been the most common approach [22], to include other recommender fields such as graphical [23], to include item-based CF [24] and user-based CF. The core of the CF is similarity estimation, and it applies to all types of recommendation methods [25]. The Pearson Correlation Coefficient (PCC) as the most common similarity measurement, which can generate the numerical distances among users accurately [26]. However, PCC doesn’t work with sparse matrices, and most O2O applications are extremely sparse.

There have been many recent studies addressing similarity estimation in recommendation systems. Due to the bad performance of PCC in tackling reluctant and sparse ratings problem, ranking similarities are popular utilized, including Kendall Rank Correlation Coefficient (KRCC) [27], Spearman Rank Correlation Coefficient (SRCC) [28], and AP Correlation Coefficient [29]. Considering service consumption, Jaccard’s Coefficient [30] has been adopted [31, 32] to estimate service recommendation similarity. Furthermore, considering the influence of trust relationship on the user decision-making, the degree of trust estimation based on social network analysis has been used to enhance the traditional similarity calculation in recommendation [33]. With the rapid development of deep learning and the presence of big data [34], computing similarity based on video and audio information is highly challenging

Nevertheless, studies on the utilization of recommendation methods on O2O service are limited. There are still no published studies on multi-dimensional similarity measurements methods in O2O recommendation. Our paper seeks to fill this void.

## 3. O2O service user similarity estimation

Assum $\mathbf { O S } { = } \{ o s _ { i } / i { \in } \{ 1 , . . . , n \} \}$ is the set of n O2O services, $\mathbf { U } { = } \{ u _ { p } / p { \in } \{ 1 , { \ldots } , m \} \}$ is the set of m O2O service users, and $\mathbf { R } { = } \{ r _ { i , p } ~ / ~ i { \in } \{ 1 , . . . , n \} , ~ p { \in } \{ 1 , . . . , m \} \}$ is the rating matrix where $r _ { i , p }$ represents the rating of $o s _ { i }$ given by $u _ { p } .$ . Considering different evaluation standards, we classify 1. If R is “benefit”, then the higher ratings are, the more satisfied users are with O2O services. The converse is when R is “cost”. The normalized rating $r _ { i , p } ^ { n }$ can be calculated as following:

$$
r _ {i, p} ^ {n} = \left\{ \begin{array}{l l} \frac {r _ {i , p} - r _ {i} ^ {\text { min }}}{r _ {i} ^ {\text { max }} - r _ {i} ^ {\text { min }}} & R \text {   is   "   benefit" } \\ \frac {r _ {i} ^ {\text { max }} - r _ {i , p}}{r _ {i} ^ {\text { max }} - r _ {i} ^ {\text { min }}} & R \text {   is   "   cos   t" } \end{array} \right.,\tag{1}
$$

where $r _ { i } ^ { m a x }$ and $r _ { i } ^ { m i n }$ are the minimum and maximum ratings of O2O service $o s _ { i } ,$ respectively. We estimate the similarities between every two users who are in U, based on normalized ratings.

Here, ratings are for “benefit”.

## 3.1 Collaborative similarity calculation

Given ratings $r _ { i , p } ,$ we can obtain collaborative similarity, which measures the numerical distance between different O2O service users accurately. It reflects potential users’ preferences. We utilize the Pearson Correlation Coefficient (PCC) to estimate collaborative similarity. PCC is widely used in estimation to the degree of linear association between two entities [3], and generally computes the similarity of users in recommender systems:

$$
C S _ {p, q} = \frac {\sum_ {o s _ {i} \in o s _ {p , q}} \left(r _ {i , p} - \bar {r} _ {p}\right) \left(r _ {i , q} - \bar {r} _ {q}\right)}{\sqrt {\sum_ {o s _ {i} \in o s _ {p , q}} \left(r _ {i , p} - \bar {r} _ {p}\right) ^ {2}} \sqrt {\sum_ {o s _ {i} \in o s _ {p , q}} \left(r _ {i , q} - \bar {r} _ {q}\right) ^ {2}}},\tag{2}
$$

where $C S _ { p , q }$ is the collaborative similarity of $u _ { p }$ and $u _ { q } ,$ which ranges from -1 to 1. The negative value is present the pairs have no correlation, rather than opposite behaviors. For example, if $u _ { p }$ and $u _ { q }$ have negative collaborative similarity, it does not mean when $u _ { p }$ gives high rating of $o s _ { i }$ $u _ { q }$ will conversely give a low rating. Therefore, we only take the positive collaborative similarities into account, and the higher this value the more similar behavior is between the two O2O service users. $\bar { r } _ { p }$ and $\overline { { r } } _ { q }$ are average ratings of O2O services used by $u _ { p }$ and $u _ { q } ,$ respectively. $O S _ { p , q }$ is the set of O2O services co-consumed by $u _ { p }$ and $u _ { q } .$

## 3.2 Preference similarity calculation

Collaborative similarity measures the similarity across users based on concrete values of ratings. However, user rankings of O2O services can better express their preferences. If two users of a particular O2O service give similar rankings, we expect that they have similar preferences in some extent, even though they give different ratings of each O2O service. For example, as shown in Table 1, we suppose the ratings of O2O services os<sub>1</sub>, $o s _ { 2 } .$ , $o s _ { 3 }$ and $O S _ { 4 }$ given by users $u _ { p }$ and $u _ { q } ,$ which is ranges 1 to 5. It is obviously that they give the same ranking of these four services, even

though collaborative similarity is not equal to 1.

Table 1. A sample of difference between collaborative similarity and preference similarity

<table><tr><td></td><td> $os_1$ </td><td> $os_2$ </td><td> $os_3$ </td><td> $os_4$ </td></tr><tr><td> $u_p$ </td><td>5</td><td>2</td><td>1</td><td>4</td></tr><tr><td> $u_q$ </td><td>4</td><td>2</td><td>1</td><td>3</td></tr></table>

Thus, to produce effective recommendation results, the preference similarity between different O2O service users should be calculated as accurately as possible. Motivated by the ratings, the ranking information could provide valuable insight and distinctive information differing from collaborative similarity.

We adopt the Kendall Rank Correlation Coefficient (KRCC) to estimate the preference similarity [32]. KRCC has commonly been used in ranking-oriented recommender system research due to its simple implementation and good performance. PCC is widely adopted in the similarity estimation in recommender systems. But KRCC is more appropriate in the process of $P S _ { p , q }$ calculation, KRCC can be computed as following:

$$
P S _ {p, q} = \frac {\left| o s _ {p , q} \right| \times \left(\left| o s _ {p , q} \right| - 1\right) - 4 \times \sum_ {o s _ {i} , o s _ {j} \in o s _ {p , q}} f \left(\left(r _ {i , p} - r _ {j , p}\right) \left(r _ {i , q} - r _ {j , q}\right)\right)}{\left| o s _ {p , q} \right| \times \left(\left| o s _ {p , q} \right| - 1\right)},\tag{3}
$$

$$
f (x) = \left\{ \begin{array}{l l} 1 & x <   0 \\ 0 & x \geq 0 \end{array} , \right.\tag{4}
$$

where $O S _ { p , q }$ denotes the set of O2O services co-utilized by $u _ { p }$ and $u _ { q } ,$ and $| O S _ { p , q } |$ represents the cardinality of $O S _ { p , q } . f ( x )$ is the binary threshold function which is equal to $0 ( x < 0 )$ or 1 $( x > 0 )$ It is notable that if two O2O users give the same ranking of O2O services, $P S _ { p , q } = 1$

Preference similarity can measure the consistency of different users based on the accurate ranking similarity estimation computed by KRCC. However, it can overestimate the similarity of negative O2O service users who are not really similar, when they have less co-consumed services.

Table 2. A sample of disadvantage of preference similarity

<table><tr><td></td><td> $os_{1}$ </td><td> $os_{2}$ </td><td> $os_{3}$ </td><td> $os_{4}$ </td></tr><tr><td> $u_{1}$ </td><td>4</td><td>3</td><td>1</td><td>2</td></tr><tr><td> $u_{2}$ </td><td>3</td><td>2</td><td>3</td><td>5</td></tr><tr><td> $u_{3}$ </td><td>5</td><td>4</td><td>null</td><td>null</td></tr></table>

Table 2 shows an example, which contains three O2O service users $( u _ { 1 }$ to $u _ { 3 } )$ and four O2O services (cs<sub>1</sub> to cs<sub>4</sub>). The data in this example are all extracted from a real O2O services dataset which is described below. Utilizing Eq. (3) and (4), we compute preference similarities among the users, and obtain the result: $p s _ { I , 3 } > p s _ { I , 2 } ,$ eans $u _ { 1 }$ is more similar with $u _ { 3 }$ with $u _ { 2 }$ Obviously, the result is unilateral because of the limitation of consumption history. Therefore, it is necessary to reinforce similarity estimation considering the user history trajectory, especially in a sparse-matrix environment.

## 3.3 Trajectory similarity calculation

It seems reasonable to consider the number of O2O services consumed by users is small. Therefore, the user-service matrix is too sparse, generally with less than 5% ratings in the dataset. In this case, collaborative similarity and preference similarity are unable to accurately reflect the real situation. In addition, collaborative similarity only estimates a numerical distance, and does not take the consumption trajectory of O2O service users into account. Similarly, preference similarity only considers the ranking distance, which has nothing to do with the statistical features of trajectory records.

# ACCEPTED MANUSCRIPT

Consequently, the trajectory similarity is estimated based on O2O services historical consumption records, which are significant for users’ similarities calculation. For instance, as shown in Table 3, $u _ { p }$ has used services $o s _ { I } , o s _ { 2 } , o s _ { 3 }$ and $o s _ { 4 } ; u _ { q }$ has used $o s _ { 2 } , o s _ { 3 }$ and $o s _ { 5 } ,$ , while $u _ { r }$ has used $o s _ { 6 }$ and $o s _ { 7 }$ . Although $u _ { p } , u _ { q }$ and $u _ { r }$ are unfamiliar O2O service users in the real world, $u _ { p }$ and $u _ { q }$ have a higher similarity than $u _ { p }$ and $u _ { r } ,$ since they have both consumed $o s _ { 2 }$ and $o s _ { 3 } ,$ even if whose ratings are dissimilar given by $u _ { p }$ and $u _ { q } .$

Table 3. A sample of trajectory similarity

<table><tr><td></td><td> $OS_{1}$ </td><td> $OS_{2}$ </td><td> $OS_{3}$ </td><td> $OS_{4}$ </td><td> $OS_{5}$ </td><td> $OS_{6}$ </td><td> $OS_{7}$ </td></tr><tr><td> $u_{p}$ </td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td></tr><tr><td> $u_{q}$ </td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td> $u_{r}$ </td><td></td><td></td><td></td><td></td><td></td><td>√</td><td>√</td></tr></table>

For this reason, we utilize Jaccard’s Coefficient to calculate the trajectory similarity, which is regularly adopted to quantify the discrimination of asymmetric information on binary variables [30], and it can present the consumption trajectory of users. Thus, the trajectory similarity $T S _ { p , q }$ of $u _ { p }$ and $u _ { q }$ can be calculated as following:

$$
T S _ {p, q} = \frac {\left| O S _ {p , q} \right|}{\left| O S _ {p} \right| + \left| O S _ {q} \right| - \left| O S _ {p , q} \right|}\tag{5}
$$

where $/ O S _ { p } /$ and $/ O S _ { q } /$ are the numbers of O2O services which have been both utilized by $u _ { p }$ and $u _ { q } . \mathrm { \ } / O S _ { p , q } /$ $u _ { p }$ $u _ { q } . \ T S _ { p , q }$ is in the interval of [0, 1], and a higher value shows that two service users have similar service consumption history.

## 4. O2O service recommendation model

For similarity estimation of O2O service users, collaborative similarity can accurately reflect user behavior based on numerical calculation. While different users may apply different evaluation standards (i.e., some users like giving higher ratings), the different ratings of O2O services can generate similar ranking which indicates users’ similar preferences. Thus, preference similarity estimates the behavioral consistency from another aspect. In general, however, the O2O service-user rating matrix is sparse, because single user usually have used only a few of several million O2O services, which leads to the user-service matrix having more than 90% zero values, and make collaborative and preference similarity estimation difficult. For this reason, we propose the trajectory similarity estimation based on the service consumption records. Considering the advantages and disadvantages of these three similarity estimation methods, we adopt weight parameters to combine them as following:

$$
S i m = \alpha * C S + \beta * P S + \gamma * T S,\tag{6}
$$

where $\alpha , \beta ,$ and $\gamma$ are in the interval of 0 to 1, and $\alpha { + } \beta { + } \gamma = 1$ . If the parameter of one similarity equals to 0, it means we do not consider that similarity in our recommendation model. On the other hand, if the parameter of one similarity equals to 1, it means we only utilize that similarity in recommendation. In our experiments, we will discuss these three parameters in detail.

After calculating the combined multi-dimensional Sim among every pair of O2O service users, we obtain a similar users-set of the target user by ranking the Sim values. It is worth noting that Sim falls into the interval of -1 to 1. In practice, negative similarity across users may similarities are larger than 0 [25]. The rating $r _ { i , p } ^ { p r e }$ of O2O service $o s _ { i }$ which target user $u _ { p }$ has not used can be predicted as follows:

$$
r _ {i, p} ^ {p r e} = \overline {{r}} _ {p} + \frac {\sum_ {q \in T k _ {p}} S i m _ {p , q} \times \left(r _ {i , q} - \overline {{r}} _ {q}\right)}{\sum_ {q \in T k _ {p}} S i m _ {p , q}},\tag{7}
$$

where $\bar { r } _ { p }$ and $\overline { { r } } _ { q }$ is the average ratings of O2O services which has been consumed by $u _ { p }$ and $u _ { p } ,$ respectively.

Then, the predicted ratings are ranked in decreasing order, and we recommend several top services to the target user according to demand. Figure 1 illustrates the procedures of O2O service recommendation proposed:

![](/api/attachments/QUF3CACD/fulltext/images/40e7e8749e5757126d5fe655ef3af3346b28652d97b1a3846334cc75f7849cef.jpg)  
Figure 1. The process of O2O service recommendation based on multi-dimensional similarity measurement

## 5. Experiments

# ACCEPTED MANUSCRIPT

## 5.1 Data sources

To evaluate the performance of the O2O recommendation approach based on the multidimensional similarity measurement proposed, we utilize the information captured on Dianping.com (https://www.dianping.com/). Dianping.com is one of the biggest O2O companies in China. It has been operating for over 10 years (since April 2003). This website is a leading online city life guide, and one of the first online independent third-party user service rating platforms, including shopping, leisure, restaurant, entertainment, and other lifestyle services. This platform provides group buying service which is one of the most usual and classical O2O business model. Users can buy coupons online, and use them in offline store (e.g. restaurant, KTV and so on). After their service experience, users can give ratings (numbers) and comments (text) on the platform of the O2O services that they have used.

As the food O2O services has the largest service scale in Dianping.com, we utilized a web crawler to capture 66,769,287 ratings of 145,437 restaurants given by 18,087,981 users in Beijing by Mar. 2016, and save them as XML format. Figure 2 is an example:

Figure 2. Extract of Web Crawler Code

Here rid, name, address and tags are the information of the restaurant. uid, and user are the id and username of the user. level and content are the rating and comment given by the user (uid: 45448933) to the restaurant (rid: 507571). In our study, we capture 66,769,287 such recordings. Since we only focus on the ratings, we extracted the uid, id and level from this dataset by utilizing Python 2.7, and then transformed it into a user-service rating matrix using Java on an Eclipse Neon Release (4.6.0) platform. The matrix has 18,087,981 rows and 145,437 columns representing users and restaurants, respectively. Because of the space limitation, we only list part of matrix in Table 4 as follows:

Table 4. The user-restaurant matrix of ratings (partial data)

<table><tr><td>Users\Restaurants</td><td> $r_1$ </td><td> $r_2$ </td><td> $r_3$ </td><td> $r_4$ </td><td> $r_5$ </td><td> $r_6$ </td><td> $r_7$ </td><td> $r_8$ </td><td>...</td><td> $r_{145437}$ </td></tr><tr><td> $u_1$ </td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr><tr><td> $u_2$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr><tr><td> $u_3$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr><tr><td> $u_4$ </td><td>0</td><td>4</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr><tr><td> $u_5$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>...</td><td>0</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $u_{18087981}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr></table>

The ratings are discrete and fall in the interval of 1 to 5 (i.e., 1, 2, 3, 4 and 5), and 0 represent none rating. The matrix is very sparse, with a density of merely 0.52%, and the level of activities of restaurants and users are considerably different. The more active restaurants (i.e., the restaurant rated and commented by many users after their meal) are the most interesting as they have attracted more users. Meanwhile, more active users indicate that they are gastronomes, and thus they are more likely to accept service recommendations.

We filter active restaurants and users using filtering rules: The restaurants must be rated by at least m users who must rate at least n restaurants. Because the numbers of items (users and restaurants) and matrix density are inversely related (i.e., the increase in matrix density will lead to a decrease of items), after trying m and n considerable times, we set m is 30 and n is 7. There are 153,224 ratings given by 372,498 users on 3,760 restaurants, giving a matrix density of 10.94%. Figure 3 illustrates the distribution of 153,224 ratings. We observe that the ratings are roughly normal distribution, and the average of all the ratings is 0.424.

![](/api/attachments/QUF3CACD/fulltext/images/10924c571cd91b5282eb5ab0762e86a8a143f43c022f2b7a3084de3764def1e8.jpg)  
Figure 3. The distribution of ratings

## 5.2 Evaluation metrics

Prediction accuracy is widely adopted in the evaluation of rating-oriented recommendation approaches, based on calculating the deviations between the sample ratings and the predicted ratings. In our paper, for evaluating the predictive performance of single similarity and multidimensional measures, we utilize Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), both widely used in evaluation of rating-oriented recommendation methods [2, 3, 25]. Meanwhile, they are also numerical measurements of prediction accuracy. MAE and RMSE are:

$$
M A E = \frac {\sum_ {i , p} \left| r _ {i , p} - r _ {i , p} ^ {p r e} \right|}{N},\tag{8}
$$

$$
R M S E = \sqrt {\frac {\sum_ {i , p} \left(r _ {i , p} - r _ {i , p} ^ {p r e}\right) ^ {2}}{N}},\tag{9}
$$

Where $r _ { i , p }$ and $r _ { i , p } ^ { p r e }$ denote the sample rating and predicted rating of $o s _ { i }$ rated by $u _ { p } ,$ respectively. N denotes the total number of the sample services. Notably, the rating is in the interval of 0 to 1.

Thus, MAE and RMSE are both in the interval of 0 to 1, and the lower of these two metrics are, the better predictive accuracy generated by the model.

## 5.3 Experiment results and analysis

We adopt multi-dimensional similarities integration in the process of O2O service recommendation, considering ratings, rankings and trajectory history of service consumed by O2O service users. The classical recommendation method Collaborative Filtering (CF) has been widely used in many fields. Therefore, to check the performance of multi-dimensional similarities integration, we utilize CF.

We firstly compare Multi-Dimensional Similarity based Collaborative Filtering (MSCF) with single similarity recommendation methods, including Collaborative Similarity based Collaborative Filtering (CSCF), Preference Similarity based Collaborative Filtering (PSCF), and Trajectory Similarity based Collaborative Filtering (TSCF). Particularly, Pearson Correlation Coefficient (PCC) is usually regarded as a good recommendation method, widely adopted in ecommerce. Additionally, we also test TSCF performance compared with CSCF and PSCF in critical sparse matrix in item-based recommendation generating results based on item correlation computation among all users [24]. Secondly, we adjust the weights (i.e., α, β, and γ) of three similarities (i.e., CS, PS, TS). Then, we observe the impact of every similarity measure with respect to predictive performance.

In these experiments, we randomly abstract 10% to 90% (with the step of 10) of ratings in matrix as training sets, and use the remainder for testing. It is worth noting that if the training set has 10% ratings, the real density of the matrix is 1.094% (i.e., 10%\*10.94%), since all the ratings in original matrix constitute 10.94 percent. To provide an unbiased estimation of the prediction deviation (MAE/RMSE) on training set, k-fold cross-validation (KFCV) is often used, and k is typically set 10 [35]. However, since original sample is merely partitioned once randomly based on KFCV, it lacks randomness. We utilize Class Random in Java class library (Java.util.Random). This Java function is used to generate a stream of pseudorandom numbers. Random seed setting can ensure the randomness of each training set abstraction and consistency in one experiment for different approaches and parameters adjustment. Thus, each result is average value generated by 100 independent repeated random experiments to reduce the uncertainty and strengthen reliability of our experiments.

The experiment results demonstrated that MSCF we proposed is effective enough to generate high-quality prediction given sparse matrices, and TS has better performance.

## 5.3.1 Comparative Experiments

(1) Compare MSCF with CSCF, PSCF and TSCF

To compare MSCF with single similarity recommendation methods (CSCF, PSCF and TSCF), $\alpha = \beta = \gamma = \frac { 1 } { 3 } )$ in our proposed model (MSCF).

![](/api/attachments/QUF3CACD/fulltext/images/64e78e165b9f79bc9f9d4fdea2865a184259b55fab7ce4390b0696ddf48612f6.jpg)  
(a)

![](/api/attachments/QUF3CACD/fulltext/images/856fb2821aac98de6db7cde6199f79e2744e3131c9f7ac42cea29b736d745b3d.jpg)  
(b)  
Figure 4. Performance Comparison with Single Similarity Methods

Figure 4 shows the experiment results, where Figure 4. (a) is the MAE performance, while Figure 4. (b) is the RMSE performance. In Figure 4. (a), the MAE values of four methods decrease with the increasing of training set density, which represents matrix density. Science the training set density is in the interval of 10% to 90% with step of 10%, and simultaneous matrix density falls into the interval of 1.094% (10%\*10.94%) to 9.846% (90%\*10.94%) with the step of 1.094%, which has been discussed above.

Additionally, in Figure 4. (a), MSCF provided significantly better performance than CSCF and PSCF. Due to use of the multi-dimensional similarity method, we can obtain more accurate prediction results than rating-based similarity in O2O service recommendation. TSCF has similar performance with MSCF, which confirms the hypothesis that CS and PS do not provide useful support in recommendation in the presence of sparse matrices. It is worth noting that the MAE of TSCF and MSCF become more stable with denser matrices (after 60%). However, the MAE of CSCF and PSCF continually decrease, indicating that rating-based similarity methods may have better predictive performance for denser matrices, because they can accurately reflect the similarity of service users. RMSE results are similar to those of MAE.

In the process of data mining, more data contains more useful information, so the future trends of events can be better grasped. In our experiments, denser matrices contain more useful information for prediction than sparse matrices. Thus, these experiment results (i.e. 8 curves in Figure 4) meet the objective law, and then verify the validity and warranty of our data set and models, as all curves go downwards with the increasing of training set density.

Additionally, we prove that trajectory similarity can reflect the user behavior tendency more accurately. Since a single user is hard to expose to all services, the statistical features of trajectory records present enough similarity between every pair of service users. On the contrary, strict linear association calculation and ranking estimation cannot perform well. Notably, since ranking preference is generated by less accurate numerical calculation, it performs slightly better than collaborative similarity. However, with the increase of information, recommendation based on accurate numerical similarity will have better performance, because they can estimate similarities precisely based on each specific rating record.

## (2) Compare CSCF, PSCF and TSCF in Item-based Recommendation

![](/api/attachments/QUF3CACD/fulltext/images/90b0ad544ed244f3284180c88e63cafeb72b8c0c5b3c3481e31a9215f9b6fccc.jpg)  
(a)

![](/api/attachments/QUF3CACD/fulltext/images/913db5d643a0f90cab93c852cbe87fe6ddefacad998d7180c25239b6e881f050.jpg)  
(b)  
Figure 5. Item-based Recommendation Performance Based on Single Similarity

The key idea of Item-based CF methods is that users are more likely to use the services which are similar to the service they have used. The recommendation results are generated based on item correlation computation among all users [36]. Figure 5 illustrates the experiment results, which compare three single similarity recommendation methods (CSCF, PSCF and TSCF) as training set density increases. Figure 5. (a) is the MAE performance, while Figure 5. (b) is the RMSE performance.

Obviously, the experiment results are similar to Figure 4, which indicates that, facing the problem of insufficient information, both user action records and service used records are all significant and effective to predict the trend of user behavior than the similarity estimation based on accurate numerical calculation.

## 5.3.2 Weight Experiments

After proving the validity and warranty of our data set and models, and analyzing relative performance, we conducted 66 groups of experiments by adjusting the values of $\alpha , \beta ,$ and $\gamma$ in the interval 0 to 1 with the step of 0.1. Every group in the experiment completed work over the training set with densities of 0.1 to 0.9 with step 0.1, and then generates 594 results for both MAE and RMSE. As space is limited, we present the Top-5 combinations of similarities with different matrix density of MAE and RMSE in Table 5 and Table $^ 6$ where the column property is element is $\gamma ,$ the second $\beta ,$ and the last α (e.g., 0.7/0.2/0.1 represents that $\alpha , \beta ,$ and $\gamma$ are equal to 0.7, 0.2, and 0.1, respectively).

![](/api/attachments/QUF3CACD/fulltext/images/1e4ce22bfe381d9b554575dc2d8432a05c8c3d3d945024a2925d9f734db1a063.jpg)  
(a)

![](/api/attachments/QUF3CACD/fulltext/images/eb58c22bd002bceab2d78aa39484c628f23dc592f5b02cb8591670e71ab67a24.jpg)  
(b)  
Figure 6. Average and Standard Deviation of Weight experiments

In Figure 6. (a), we show the results of 66 experiments and calculate average MAE and RMSE. We obtain different averages with increasing of matrix density. Both lines decrease with density, demonstrating the validity and warranty in experimental process of weight adjustment which similar to discussion in Section 5.3.1. Figure 6. (b) illustrates Standard Deviations of MAE and RMSE, the error fluctuation of the 66 experiments. The two inverted U-shape lines show that when the matrix is too sparse, none of similarity combinations give good results. With increasing matrix density, different similarity combinations generate different predictive performance. If the matrix density is sufficiently high, as information increases, performance

improves.

Table 5. The Top-5 Similarities Combinations in Different Matrix Density (MAE)

<table><tr><td>Top-5\TSD</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td> $1^{st}$ </td><td>0.6/0.4/0.0(0.961692)</td><td>1.0/0.0/0.0(0.662354)</td><td>1.0/0.0/0.0(0.473737)</td><td>0.8/0.2/0.0(0.354304)</td><td>1.0/0.0/0.0(0.288636)</td><td>0.7/0.1/0.2(0.254343)</td><td>0.8/0.1/0.1(0.225105)</td><td>1.0/0.0/0.0(0.206957)</td><td>0.9/0.1/0.0(0.217373)</td></tr><tr><td> $2^{nd}$ </td><td>0.4/0.6/0.0(0.961684)</td><td>0.9/0.1/0.0(0.662400)</td><td>0.9/0.1/0.0(0.473926)</td><td>0.9/0.1/0.0(0.354304)</td><td>0.9/0.1/0.0(0.289303)</td><td>1.0/0.0/0.0(0.254590)</td><td>1.0/0.0/0.0(0.225186)</td><td>0.7/0.0/0.3(0.207263)</td><td>1.0/0.0/0.0(0.217675)</td></tr><tr><td> $3^{rd}$ </td><td>0.7/0.3/0.0(0.925184)</td><td>0.8/0.2/0.0(0.662436)</td><td>0.8/0.2/0.0(0.474206)</td><td>1.0/0.0/0.0(0.354458)</td><td>0.8/0.2/0.0(0.290173)</td><td>0.9/0.1/0.0(0.255022)</td><td>0.9/0.1/0.0(0.225918)</td><td>0.9/0.0/0.1(0.207267)</td><td>0.8/0.2/0.0(0.217799)</td></tr><tr><td> $4^{th}$ </td><td>1.0/0.0/0.0(0.925367)</td><td>0.7/0.3/0.0(0.662476)</td><td>0.9/0.0/0.1(0.474666)</td><td>0.7/0.3/0.0(0.354610)</td><td>0.9/0.0/0.1(0.290559)</td><td>0.8/0.2/0.0(0.255912)</td><td>0.9/0.0/0.1(0.226417)</td><td>0.8/0.0/0.2(0.207295)</td><td>0.7/0.3/0.0(0.218261)</td></tr><tr><td> $5^{th}$ </td><td>0.3/0.7/0.0(0.925409)</td><td>0.6/0.4/0.0(0.662531)</td><td>0.8/0.1/0.1(0.474939)</td><td>0.6/0.4/0.0(0.355146)</td><td>0.7/0.3/0.0(0.290892)</td><td>0.9/0.0/0.1(0.256501)</td><td>0.7/0.2/0.1(0.226454)</td><td>0.8/0.1/0.1(0.207342)</td><td>0.6/0.4/0.0(0.219311)</td></tr></table>

Table 6. The Top-5 Similarities Combinations in Different Matrix Density (RMSE)

<table><tr><td>TSD Top-5</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td> $1^{st}$ </td><td>0.5/0.3/0.2(0.963218)</td><td>1.0/0.0/0.0(0.789472)</td><td>0.9/0.1/0.0(0.631972)</td><td>0.9/0.1/0.0(0.509053)</td><td>1.0/0.0/0.0(0.424293)</td><td>0.8/0.1/0.1(0.371172)</td><td>1.0/0.0/0.0(0.329501)</td><td>0.8/0.1/0.1(0.297437)</td><td>0.7/0.3/0.0(0.318218)</td></tr><tr><td> $2^{nd}$ </td><td>0.9/0.1/0.0(0.964789)</td><td>0.9/0.1/0.0(0.789482)</td><td>1.0/0.0/0.0(0.631985)</td><td>0.8/0.2/0.0(0.509099)</td><td>0.9/0.1/0.0(0.424599)</td><td>1.0/0.0/0.0(0.375545)</td><td>0.7/0.2/0.1(0.329877)</td><td>1.0/0.0/0.0(0.297898)</td><td>0.8/0.2/0.0(0.318366)</td></tr><tr><td> $3^{rd}$ </td><td>1.0/0.0/0.0(0.964911)</td><td>0.8/0.2/0.0(0.789490)</td><td>0.8/0.2/0.0(0.631991)</td><td>1.0/0.0/0.0(0.509133)</td><td>0.8/0.2/0.0(0.425006)</td><td>0.9/0.1/0.0(0.375947)</td><td>0.9/0.1/0.0(0.329889)</td><td>0.9/0.1/0.0(0.298256)</td><td>0.6/0.4/0.0(0.318498)</td></tr><tr><td> $4^{th}$ </td><td>0.9/0.0/0.1(0.969339)</td><td>0.7/0.3/0.0(0.789498)</td><td>0.9/0.0/0.1(0.632397)</td><td>0.7/0.3/0.0(0.509219)</td><td>0.9/0.0/0.1(0.425048)</td><td>0.9/0.0/0.1(0.376567)</td><td>0.8/0.2/0.0(0.330124)</td><td>0.9/0.0/0.1(0.298317)</td><td>0.9/0.1/0.0(0.318572)</td></tr><tr><td> $5^{th}$ </td><td>0.1/0.9/0.0(0.969342)</td><td>0.6/0.4/0.0(0.789512)</td><td>0.8/0.1/0.1(0.632402)</td><td>0.6/0.4/0.0(0.509413)</td><td>0.7/0.3/0.0(0.425377)</td><td>0.8/0.2/0.0(0.376624)</td><td>0.6/0.3/0.1(0.330354)</td><td>0.8/0.2/0.0(0.298997)</td><td>0.5/0.5/0.0(0.318998)</td></tr></table>

We also sought the optimum similarity combinations, and then present similarity combinations generating the five best predictive results for each training set density (MAE and RMSE respectively). In Table 5, no combinations based on only adopting CS and PS appear (i.e., 0.0/1.0/0.0 and 0.0/0.0/1.0 do not exist in Table 5). Thus, our proposed method has better

# ACCEPTED MANUSCRIPT

performance than the single rating-based similarity estimations (i.e. CS and PS). However, as the matrix is too sparse, the TS-only measure can generate better results. Notably, even though the training set density is 0.9, the matrix density is merely 0.09846 (0.9\*0.1094), as discussed in section 5.3.1. Table 6 presents RMSE, illustrating similar conclusions as drawn from Table 5.

MSCF, as a multi-information fusion recommendation method, estimates the user similarity in different aspects and considers the numerical distances, ranking preferences and trajectory records of every two users. Thus, single similarity estimation of recommendation has limitations. Meanwhile, it is worthy to note that the weight of TS accounts for a larger proportion of best results than the other measures, and predictive accuracy increases significantly with TS adoption (bold in Table 5 and Table 6). It again confirms the significance and effectiveness of trajectory records in O2O service recommendation facing the problem of lacking information.

## 6. Conclusion

In this paper, we propose a novel O2O service recommendation approach containing three similarity measurement methods, collaborative similarity estimation, preference similarity estimation and trajectory similarity estimation. These measures consider numerical distance, ranking preference and history of consumption respectively. In the experiments presented, we show that our proposed method has better prediction accuracy than single similarity measures in O2O service recommendation. We further explore the weights of these three similarities to find the optimal combination in different matrix densities. We also show that history consumption records are significant in sparse matrices.

Due to the limitations of available experimental data, we cannot find the combination of the three similarity measures effective for higher matrix density. Meantime, the geographic information of O2O service providers and users are important for recommendation, which is not included. In future work, we will study similarity measurements based on multi-source heterogeneous data (text, audio and video) in the age of Big Data, and take geographic information into consideration.

## References

[1] A. Rampell. Why Online2Offline Commerce is a trillion dollar opportunity. techcrunch.com (2010).

[2] S. Yang, Y. Lu, P.Y.K. Chau. Why do consumers adopt online channel? An empirical investigation of two channel extension mechanisms, Decision Support Systems 54(2) (2013) 858-869.

[3] G. Adomavicius, Z. Huang, A. Tuzhilin, Personalization and Recommender Systems, INFORMS Tutorials on Operations Research (2008) 55-107.

[4] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17(6) (2005) 734-749.

[5] B. Van Roy, X. Yan. Manipulation Robustness of Collaborative Filtering. Management Science, 56(11) (2010) 1911-1929.

[6] T.J. Hess, A.L. McNab, K. Basoglu, K. Asli, Reliability Generalization of Perceived Ease of Use, Perceived Usefulness, and Behavioral Intentions, MIS Quarterly 38(1) (2014) 1-28.

[7] N. Subramanian, A. Gunasekaran, J. Yu, J. Chung, K. Ning. Customer satisfaction and competitiveness in the Chinese E-retailing: Structural equation modeling (SEM) approach to identify the role of quality factors, Expert Systems with Applications 41(1) (2014) 69-80.

[8] G.W. Bock, J. Lee, H.H. Kuan, J.H. Kim, The progression of online trust in the multichannel retailer context and the role of product uncertainty, Decision Support Systems 53(1)

(2012) 97-107.

[9] S. Lim, B. Lee, Loyalty programs and dynamic consumer preference in online markets, Decision Support Systems 78 (2015) 104-112.

[10] S. Xiao, M. Dong, Hidden semi-Markov model-based reputation management system for online to offline (O2O) e-commerce markets, Decision Support Systems 77 (2015) 87-99.

[11] R.K. Chellappa, R.G. Sin, S. Siddarth, Price Formats as a Source of Price Dispersion: A Study of Online and Offline Prices in the Domestic U.S. Airline Markets, Information Systems Research 22(1) (2011) 83-98.

[12] F. Gao, X. Su, Online and Offline Information for Omnichannel Retailing, Manufacturing & Service Operations Management preprint 2016.

[13] N. Granados, A. Gupta, R.J. Kauffman, Online and Offline Demand and Price Elasticities: Evidence from the Air Travel Industry, Information Systems Research 23(1) (2012) 164-181.

[14] V.H. Manshadi, S.O. Gharan, A. Saberi, Online Stochastic Matching: Online Actions Based on Offline Statistics, Mathematics of Operations Research 37(4) (2012) 559-573.

[15] J. Chu, P. Chintagunta, J. Cebollada, Research Note—A Comparison of Within-Household Price Sensitivity Across Online and Offline Channels, Marketing Science 27(2) (2008) 283-299.

[16] P.J. Danaher, I.W. Wilson, R.A. Davis, A Comparison of Online and Offline Consumer Brand Loyalty, Marketing Science 22(4) (2003) 461-476.

[17] J. Wu, L. Chen, Z. Zheng, and et al. Clustering web services to facilitate service discovery, Knowledge and information systems 38(1) (2014) 207-229.

[18] H. Sun, Z. Zheng, J. Chen, M.R. Lyu, Personalized Web Service Recommendation via Normal Recovery Collaborative Filtering, IEEE Transactions on Services Computing 6(4) (2013)

573-579.

[19] Z. Zheng, H. Ma, M.R. Lyu, I King, QoS-Aware Web Service Recommendation by Collaborative Filtering, IEEE Transactions on Services Computing 4(2) (2011) 140-152.

[20] Z. Zheng, M.R. Lyu, Personalized reliability prediction of web services. ACM Transactions on Software Engineering and Methodology 22(2) (2013) 12.

[21] X. Wang, J. Zhu, Zheng, W. Song, Y. Shen, M.R. Lyu, A Spatial-Temporal QoS Prediction Approach for Time-aware Web Service Recommendation, ACM Transactions on the Web 10(1) (2016) 1-25.

[22] Z. Huang, D.D. Zeng, Why Does Collaborative Filtering Work? Transaction-Based Recommendation Model Validation and Selection by Analyzing Bipartite Random Graphs, INFORMS Journal on Computing 23(1) (2011) 138-152.

[23] S. Banerjee, S. Sanghavi, S. Shakkottai, Online Collaborative Filtering on Graphs, Operations Research 64(3) (2016) 756-769.

[24] D. Li, Q. Lv, L. Shang, N. Gu, Item-based top-N recommendation resilient to aggregated information revelation, Knowledge-Based Systems, 67 (2014) 290-304.

[25] G. Adomavicius, J. Zhang, Classification, Ranking, and Top-K Stability of Recommendation Algorithms, INFORMS Journal on Computing 28(1) (2016) 129-147.

[26] P. Ahlgren, B. Jarneving, R. Rousseau, Requirements for a cocitation similarity measure, with special reference to Pearson's correlation coefficient, Journal of the American Society for Information Science and Technology 54(6) (2003) 550-560.

[27] H. Abdi, The Kendall rank correlation coefficient, Encyclopedia of Measurement and Statistics (2007) 508-510.

[28] J.H. Zar, Significance testing of the Spearman rank correlation coefficient, Journal of the

American Statistical Association 67(339) (1972) 578-580.

[29] E. Yilmaz, J.A. Aslam, S. Robertson, A new rank correlation coefficient for information retrieval, Proceedings of the 31st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (2008) 587-594.

[30] H. Seifoddini, M. Djassemi, The production data-based similarity coefficient versus Jaccard’s similarity coefficient, Computers & Industrial Engineering 21 (1991) 263-266.

[31] S. Ding, S. Yang, Y. Zhang, and et al, Combining QoS prediction and customer satisfaction estimation to solve cloud service trustworthiness evaluation problems, Knowledge-Based Systems 56 (2014) 216-225.

[32] S. Ding, Z. Wang, D. Wu, D.O. Olson, Utilizing customer satisfaction in ranking prediction for personalized cloud service selection, Decision Support Systems 90 (2017) 1-10.

[33] Y. Pan, S. Ding, W. Fan, J. Li, S. Yang, Trust-Enhanced Cloud Service Selection Model Based on QoS Analysis, PLoS One 10(11) (2015) e0143448.

[34] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature, 521(7553) (2015) 436-44.

[35] D. Wu, Performance evaluation: an integrated method using data envelopment analysis and fuzzy preference relations, European Journal of Operational Research 194(1) (2009) 227-235.

# ACCEPTED MANUSCRIPT

Yuchen Pan is a PhD candidate at the University of Chinese Academy of Sciences, Beijing, China. His research interests are business analytics and intelligence.

Desheng Wu is a Professor with Stockholm University, Stockholm, Sweden and a Distinguished Professor with the University of Chinese Academy of Sciences, Beijing, China. His current research interests include risk analysis, performance evaluation, and decision support system. He has published over 100 journal papers that have appeared in such journals as Decision Sciences, Production and Operations Management, Risk Analysis, the European Journal of Operational Research, and the IEEE Transactions on Knowledge and Data Engineering. He has published five books at Springer. He has served as an Editor/Guest Editor/Chair for several journals/conferences. He has also edited the special issues include Human and Ecological Risk Assessment in 2009 and 2010, Production Planning and Control in 2009, Computers and Operations Research in 2010, the International Journal of Environment and Pollution in 2009, and Annals of Operations Research in 2010.Mr. Wu is a member of the Professional Risk Managers’ International Association, Academic Advisory Committee, a Steering Committee Member and the Chair of the IEEE Analytics and Risk Committee.

David L. Olson is the James & H.K. Stuart Professor in MIS and Chancellor’s Professor at the University of Nebraska. He has published research in over 150 refereed journal articles, primarily on the topic of multiple objective decision-making, information technology, supply chain risk management, and data mining. He teaches in the management information systems, management science, and operations management areas. He has authored over 20 books, to include Decision Aids for Selection Problems, Introduction to Information Systems Project Management, Managerial Issues of Enterprise Resource Planning Systems, Supply Chain Risk Management, and Supply Chain Information Technology. Additionally, he has co-authored the books Introduction to Business Data Mining, Enterprise Risk Management, Advanced Data Mining Techniques, Enterprise Information Systems, Enterprise Risk Management Models, and Financial Enterprise Risk Management. He has served as associate editor of Service Business, Decision Support Systems, and Decision Sciences and co-editor in chief of International Journal of Services Sciences. He has made over 200 presentations at international and national conferences on research topics. He is a member of the Decision Sciences Institute, the Institute for Operations Research and Management Sciences, and the Multiple Criteria Decision Making Society. He was a Lowry Mays endowed Professor at Texas A&M University from 1999 to 2001. He was named the Raymond E. Miles Distinguished Scholar award for 2002, and was a James C. and Rhonda Seacrest Fellow from 2005 to 2006. He was named Best Enterprise Information Systems Educator by IFIP in 2006. He is a Fellow of the Decision Sciences Institute.

## Highlights

 Internet service recommendation system presented

 Three multi-dimensional similarity measurements evaluated

 Experimental results presented, showing that multiple measures improve performance

 Trajectory similarity performs better than rating-based similarity in sparse matrices
