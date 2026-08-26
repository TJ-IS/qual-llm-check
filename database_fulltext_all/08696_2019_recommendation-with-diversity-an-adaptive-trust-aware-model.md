---
otero_id: 8696
otero_key: "QVB72S4W"
title: "Recommendation with diversity: An adaptive trust-aware model"
authors: "Ting Yu; Junpeng Guo; Wenhua Li; Harry Jiannan Wang; Ling Fan"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113073"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Recommendation with diversity: An adaptive trust-aware model

Ting Yu<sup>a</sup>, Junpeng Guo<sup>a,\*</sup>, Wenhua Li<sup>a</sup>, Harry Jiannan Wang<sup>b</sup>, Ling Fan<sup>c</sup>

![](/api/attachments/QVB72S4W/fulltext/images/600cf2198e8e19bd52c42106e62aa9fad49a47e4a8d1084b4fe1ac4ddca7e831.jpg)

<sup>a</sup> College of Management and Economics, Tianjin University, Tianjin 300072, PR China

<sup>b</sup> University of Delaware, Newark, DE 19716, USA

<sup>c</sup> Tongji University Tezign Design A.I. Lab, Shanghai, PR China

## A R T I C L E I N F O

Keywords: Recommender systems Bipartite network Trust relationships Recommendation diversity Long-tailed products

## A B S T R A C T

Recommender systems have become an integral and critical part of various online businesses to achieve better user experience and drive customer and revenue growth. Recommendation accuracy and diversity are important criteria to evaluate recommender system performance. Many diferent strategies have been developed in existing literature to balance the trade-ofs between accuracy and diversity. However, those methods often focus on a one-size-fit-all trade-of strategy without considering each individual user’ specific recommendation situation, which leads to improvements only in individual diversity or aggregate diversity. In addition, the trust relationships among users have not been studied to improve the trade-of strategy aforementioned. In this paper, we propose an adaptive trust-aware recommendation model based on a new trust measurement developed using a user-item bipartite network. We show via experiments on three diferent datasets that our model can not only balance and adapt accuracy with both individual and aggregate diversities, but also achieve significant im provements on accuracy for cold-start users and long-tailed items.

## 1. Introduction

With the explosive growth of Internet information, recommender systems have played important roles in e-commerce websites [1]. For example, recommendations account for almost 80% of the videos watched on Netflix [2], and 30% of the page views at Amazon [3]. Besides recommendation accuracy, researchers and businesses have realized that recommendation diversity is also an important criterion to evaluate the performance of recommendation results [4, 5]. Accuracy, in this context, is measured as the fraction of the items on the re commendation list of a user that are in fact preferred items to that particular user [6]. Diferent from accuracy-oriented recommendations, diverse recommendations solve overfitting issues [5] and promote sales for long-tailed items [7]. Although long-tailed items have limited demand, they have higher marginal profits than bestsellers and boost the efect of the “one-stop shopping convenience” [8]. Online retailers, such as Amazon and Netflix, mostly ascribe their success to the sales of long-tailed items [8]. However, recommending more long-tailed items reduces bestsellers' recommendation chances, and it is also more difi cult to ensure recommendation accuracy for long-tailed items than for bestsellers. There exists a dilemma between accuracy and diversity [9].

In current literature, diversity research mainly focuses on individual diversity [10], which refers to diferentiation among each user's recommended items, and aggregate diversity [11], which measures the number of distinct items appearing in all users' recommendation lists. As increasing diversity boosts the recommendations of novel and un expected items, novelty is also correlated with diversity [5, 9]. To balance the trade-ofs between accuracy and diversity, researchers mainly adopt two strategies, namely, re-ranking recommendation lists [12, 13] and proposing new recommender models [14, 15]. However, most existing studies concentrates on improving individual or aggregate diversity, and ignoring the importance of recommendation accuracy for cold-start users and long-tailed items [16]. Moreover, they mainly utilize one-size-fits-all methods to provide recommendations to all users with a unified accuracy-diversity trade-ofs. However, individuals vary in their needs for accuracy and diversity [17]. It is necessary to treat users separately and provide recommendations with their desired accuracy-diversity trade-ofs. Further, the focus of existing researches for adaptive diversity is individual diversity [18-20]. Few studies aim to produce recommendation lists, whose aggregate diversity changes adaptively for diferent user groups [11, 12]. It is very challenging to make accuracy-diversity trade-ofs adaptively according to users' needs to ensure accuracy both for cold-start users and long-tailed items and comprehensively improve multiple dimensions of diversity.

Since trust relationships can mine users' potential interests and ef fectively tackle data sparsity and cold-start issues [21], some researchers have utilized them to improve recommendation diversity [22, 23]. However, they do not calculate users' trust degrees in distinguishing the roles of trustees. Additionally, users' personal interests play a crucial role in decision-making. To balance the trade-ofs between accuracy and diversity, it is necessary to appropriately combine users' personal interests with their trustees' tastes.

Table 1  
Revised version of MD and HC

<table><tr><td>Algorithms</td><td>Parameters</td><td>Description</td></tr><tr><td>HPH [9]</td><td> $\lambda$ </td><td>It is a combination of MD and HC. Use  $\lambda$  to control the relative effects of users&#x27; rated and unrated items.</td></tr><tr><td>HHPH [30]</td><td> $(\eta, \lambda)$ </td><td>Set initial resources for HPH.</td></tr><tr><td>Eh_HHPH [31]</td><td> $(\sigma, \eta, \lambda)$ </td><td>Use  $\sigma$  to enhance the resource allocation similarity calculated by HHPH.</td></tr><tr><td>BD [32]</td><td> $(a, b)$ </td><td>Use  $a$  and  $b$  to control the effect of item degrees when resources are transferred from items to users and users back to items.</td></tr><tr><td>SP [33]</td><td> $(\theta, \lambda)$ </td><td>Use  $\theta$  to modify the resources possessed by intermediate users, and  $\lambda$  to control the relative effects of item degrees and user degrees.</td></tr></table>

In this study, we build an adaptive trust-aware recommendation model based on a user-item bipartite network. In our model, we define trust degree of a user towards a trustee as a function of two attributes: (1) the trustee's ability for providing reliable information, and (2) the user's certainty on the trustee's ability. During the recommendation processes, we propose a new method to combine the interests of users with the tastes of their trustees, and establish an adaptive strategy to make trade-ofs between accuracy and multiple dimensions of diversity according to users' needs. Through a set of experiments using Ciao, Epinions and Yelp datasets, we have confirmed that our model can not only balance and adapt accuracy with individual diversity, aggregate diversity and novelty, but also achieve significant improvements on accuracy for cold-start users and long-tailed items.

## 2. Related work

Our work is related to recommendation diversity problem, recommender algorithms based on the user-item bipartite network, and applications of trust relationships in recommender systems. Here, we briefly review related literature.

## 2.1. Recommendation diversity problem

Recently, researchers and businesses have considered diversity as an indispensable component of recommender systems [5]. As mentioned in the Introduction, there are two main strategies to improving diversity. The first one is to re-rank recommendation lists after obtaining predicted rat ings by existing rating prediction approaches, such as item popularity based ranking [11], optimization-based approaches [12], multi-objective evolutionary algorithms [24] and cluster-based approaches [13]. The second one is to construct new recommender models, such as modifying the matrix factorization model by adding a variance minimization reg ularization factor [25] and applying a penalty function to the objective function [26]. PLUS [27] resorts to a power function to suppress the efects of similar users derived from popular items. COUSIN [28] constructs user and item similarity profiles, and adopts a regression model to quantify the association strength between users and items. Similar to PLUS and COUSIN, we also utilize binary data to construct a recommendation mode and consider the roles of power functions but our approach in this paper pays special attention to accuracy for cold-start users and long-tailed items, which is a missing feature of both PLUS and COUSIN.

For adaptively improving diversity, the latent factor portfolio model [18] mines users' interest ranges and uncertainty of their preferences by the variances of their latent factors. Noia et al. [19] re-rank a recommendation list based on some attributes that a target user wants to be diverse. Moreover, users' personalities have also been utilized to re-rank recommendation lists [20]. However, these re-ranking algorithms merely focus on individual diversity. Compared to these algorithms, our adaptive strategy balances the trade-ofs between accuracy and multiple dimensions of diversity for each user.

## 2.2. Bipartite network-based approaches

A user-item bipartite network consists of a user set and an item set, and only connection between a user and an item is allowed [14, 29]. Recommendations in the user-item bipartite network are characterized by high eficiency and low computational complexity. Heat conduction (HC) and mass difusion (MD) are two basic approaches. HC [15] regards recommendation processes as heat transfers on the user-item bipartite network and generates highly personalized but less accurate recommendations. MD [14] builds on a random walk process to distribute a node's resources equally to its neighbors and tends to recommend bestsellers to users. To reach a better trade-of between accuracy and diversity, there are several updated versions of MD and HC, as shown in Table 1.

Although these bipartite network-based algorithms ofer more re commended opportunities for long-tailed items, little attention has been paid to ensuring their recommendation accuracy. Inaccurate recommendations for long-tailed items result in negative feedback, which hurt their subsequent sales more than bestsellers [16]. Moreover, these algorithms ignore accuracy for cold-start users, and their one-size-fit-all ways fail to simultaneously satisfy all users' needs [17, 20]. Our proposed approach difers from the aforementioned algorithms by treating each user separately with an adaptive strategy that seeks to improve accuracy for cold-start users and gradually enhance its performance in terms of novelty, individual diversity, and aggregated diversity based on cumulated user transactions/interactions.

## 2.3. Application of trust relationships in recommender systems

As a social factor, trust relationships have been used to enhance the quality of recommendations and address data sparsity and cold-start issues [21].

Due to privacy concerns, researchers mainly obtain binary trust relationships. To distinguish the roles of users' trustees, researchers infer trust degrees mainly based on common rated items, such as in Refs. [34, 35]. However, there are often few common rated items between users and their trustees, which results in unreliable trust degrees. To derive more reliable trust degrees, we turn to similar items and define trust degrees according to the similarities between items rated by users and their trustees.

For improving aggregate diversity, the creation time of trust relationships has been utilized to diferentiate the roles of trustees [22]. COSRA+T [23] integrates trust relationships into a bipartite networkbased recommender algorithm. Compared with it, our model infers users' trust degrees towards their trustees to distinguish trustees' roles. To recommend items from users' inexperienced categories, Feng et al. [36] and Zhang et al. [37] merge user preference with diverse information from trustees. Diferent from their research focus, we aim to improve diversity and positively promote the sales of long-tailed items.

## 3. A trust-based adaptive diversification recommender algorithm

In this section, we describe our work in three parts, i.e., trust calculation, quantification of users' needs for diversity and recommendation steps on the user-item bipartite network. We represent the recommender system as a user-item bipartite network $G = \{ U , O , E \}$ where $U = \{ u _ { 1 } , u _ { 2 } , . . . , u _ { m } \}$ and $O = \{ o _ { 1 } , o _ { 2 } , . . . , o _ { n } \}$ refer to the vertices of m users and n items, and E is the edge set between user and item vertices. Accordingly, we build an m × n adjacency matrix A. When u rates $o _ { \alpha }$ no less than a given threshold, there exists an edge between $u _ { i }$ and $o _ { \alpha }$ in $E ,$ and $a _ { i \alpha }$ in $\mathbf { A }$ equals 1. Otherwise, $a _ { i \alpha }$ equals 0. k is the degree of u and equals $\textstyle \sum _ { \alpha = 1 } ^ { n } a _ { i \alpha } ,$ while $k _ { o \alpha }$ is the degree of $o _ { \alpha }$ and equals $\textstyle \sum _ { i = 1 } ^ { m } a _ { i \alpha } .$ Similarly, trust relationships are also represented in an m × m adjacency matrix T, where $t _ { i j } = 1$ if u trusts $u _ { j } .$ In Fig. 1, we illustrate an example with seven users and nine items to run through our model. We assume $u _ { 1 }$ trusts $u _ { 2 }$ and $u _ { 7 }$ .

![](/api/attachments/QVB72S4W/fulltext/images/4c4a2118d48d39c7dd92463824362176ffe215a063d0951ac82622ee94d41c49.jpg)  
(a) A user-item bipartite network

![](/api/attachments/QVB72S4W/fulltext/images/a1051b98f3a117860bb11c10d33e8ca6aa05214ba878650667a5e7eabd1a4485.jpg)  
(b) An adjacency matrix  
Fig. 1. An example of a user-item bipartite network and its adjacency matrix.

## 3.1. Trust calculation

In e-commerce websites like $\mathrm { C i a o ^ { 1 } }$ and Epinions<sup>2</sup>, users establish trust relationships with others who can consistently provide reliable information. Obviously, users' trust degrees towards their trustees de pend on the ability of their trustees for providing reliable information. Due to privacy policy, the main accessible information are items experienced by users, which possess diferent features to satisfy the various user needs. By mining the links that exist in items experienced by user $u _ { i }$ and the trustee $u _ { j } ,$ we intend to infer $\vec { u _ { j } ^ { \prime } s }$ ability for providing u with reliable information, and define $\vec { u _ { i } ^ { \prime } s }$ trust degree towards $u _ { j } .$

For u and $u _ { j } ,$ the sets of items they rated are represented as $O _ { i }$ and $O _ { j } { \mathrm { : } }$ , respectively. When $o _ { \alpha } \in O _ { i }$ and $o _ { \beta } \in O _ { j }$ are commonly rated by many users, we argue that there exist similar features between them. Then, $o _ { \beta }$ is likely to satisfy $\vec { u _ { i } ^ { \prime } s }$ needs with its similar features with $o _ { \alpha } .$ In other words, u will consider that information about $o _ { \beta }$ is reliable. Conversely, information about items dissimilar with any items in $O _ { i }$ is unreliable for $u _ { i } .$ According to similarities with items in $O _ { i }$ and a threshold $\epsilon ,$ we can divide $O _ { j }$ into two disjoint parts, i.e., $O _ { j 1 }$ and $O _ { j 2 } .$ For $o _ { \beta } \in O _ { j } ,$ if there exists at least one item $o _ { \alpha } \in O _ { i }$ whose similarity with $o _ { \beta }$ is no less than $\epsilon ,$ $o _ { \beta }$ belongs to $O _ { j 1 } ,$ otherwise, $o _ { \beta }$ belongs to $O _ { j 2 } .$ . The settings of ϵ is to exclude weak similarities calculated with popular items [27]. Based on $O _ { j 1 }$ and $O _ { j 2 } ,$ we respectively define the amount of reliable and unreliable information provided by $u _ { j }$ to $u _ { i }$ as the accumulated average similarities and dissimilarities with items in $O _ { i } ,$ i.e.,

$$
R (i, j) = \frac {1}{k _ {u i}} \sum_ {o _ {\beta} \in O _ {j 1}} \sum_ {o _ {\alpha} \in O _ {i}} S (\alpha , \beta),\tag{1}
$$

$$
I (i, j) = \frac {1}{k _ {u i}} \sum_ {o _ {\beta} \in O _ {j 2}} \sum_ {o _ {\alpha} \in O _ {i}} (1 - S (\alpha , \beta)),
$$

$$
S (\alpha , \beta) = \frac {\sum_ {u \in U _ {\alpha} \cap U _ {\beta}} \frac {1}{k _ {u}}}{\sum_ {u \in U _ {\alpha} \cup U _ {\beta}} \frac {1}{k _ {u}}}.\tag{2}
$$

(3)

In Eqs. (1) and $( 2 ) , S ( \alpha , \beta )$ refers to the similarity between $o _ { \alpha }$ and $o _ { \beta }$ and can be calculated by $\operatorname { E q . }$ (3) or any similarity metrics that can process binary data, such as cosine similarity and Jaccard similarity. $U _ { \alpha }$ and $U _ { \beta }$ are user sets who have rated $o _ { \alpha }$ and $\sigma _ { \beta } .$ , Eq. (3) is a revised version of Jaccard similarity based on the intuition that common users who have experienced fewer items should play more important roles than others in mining similarity between two items. When $\epsilon = 0 . 0 ,$ , Eq. (2) is equivalent to $| O _ { j 2 } |$ , i.e., the number of items in $O _ { j 2 } .$

Then, we define the ability of $u _ { j }$ for providing reliable information to $u _ { i }$ as

$$
R e (i, j) = \frac {R (i , j) + 1}{R (i , j) + I (i , j) + 2}.\tag{4}
$$

Following Laplace's “add-one” rule of succession [38], we add 1 to $R ( i , j )$ and $I ( i , j )$ in Eq. (4). For u ’s trustees in Fig. 1, we divide $u _ { 2 } ^ { \prime } s$ rated items into $O _ { 2 1 } = \{ o _ { 1 } , o _ { 3 } , o _ { 6 } , o _ { 7 } \}$ and $O _ { 2 2 } = \{ o _ { 9 } \}$ , and u ’s rated items into $O _ { 7 1 } = \{ o _ { 4 } , o _ { 6 } \}$ and $O _ { 7 2 } = \{ o _ { 9 } \}$ . ϵ is set to be 0.25. According to Eqs. (1) and (2), we obtain R(1,2) = 1.4108, I(1,2) = 0.9217, R(1,7) = 0.2957 and $I ( 1 , 7 ) = 0 . 9 2 1 7$ . Then, Re(1,2) = 0.5564 and $R e ( 1 , 7 ) = 0 . 4 0 2 7 .$

When few items have been experienced by $u _ { j } ,$ such as u in Fig. 1, the insuficient information will decrease the creditability of ability calculated by Eq. (4). To deal with this issue, we further consider the concept of certainty to measure $\vec { u _ { i } ^ { \prime } s }$ confidence in $\vec { u _ { j } ^ { \prime } s }$ ability. Based on the amount of reliable and unreliable information, u ’s certainty on the ability of $u _ { j }$ is defined as follows [39]:

$$
C (i, j) = \frac {1}{2} \int_ {0} ^ {1} \left| \frac {x ^ {R (i , j)} (1 - x) ^ {I (i , j)}}{\int_ {0} ^ {1} x ^ {R (i , j)} (1 - x) ^ {I (i , j)} d x} - 1 \right| d x,\tag{5}
$$

where x represents the possibility that $u _ { j }$ provides u with reliable information. For $u _ { 2 }$ and $u _ { 7 }$ in Fig. 1, $C ( 1 , 2 ) = 0 . 2 2 1 4$ and $C ( 1 , 7 ) = 0 . 1 7 6 6$ . Though Re(1,2) is close to Re(1,7), C(1,2) and C(1,7) will enlarge the diference between the roles of $u _ { 2 }$ and u .

The rationale behind Eq. (5) is similar to that of Wang and

![](/api/attachments/QVB72S4W/fulltext/images/378fdcb071936ddd654d87ad9a7544e54b5301815b904ca5c5e3d34b23e18a95.jpg)  
(a) Certainty vs. Total amount of info.  
Fig. 2. Changes of certainty.  
(b) Certainty vs. The amount of reliable info.

Singh [40] and is illustrated in Fig. 2. For users with the same ability, u ’s certainty on them is proportional to the total amount of information provided by them, which depends on their previous experiences. In Fig. 2 (a), the circle and square markers respectively correspond to a user $u _ { j _ { 1 } }$ whose $R ( i , j _ { 1 } )$ and $I ( i , j _ { 1 } )$ ) equal 7.0 and 1.0, and a user $u _ { j _ { 2 } }$ whose $R ( i , j _ { 2 } )$ and $I ( i , j _ { 2 } )$ equal 79.0 and 19.0. While $R e ( i , j _ { 1 } )$ equals to $R e ( i , j _ { 2 } ) .$ $C ( i , j _ { 1 } )$ is smaller than C(i,j ), i.e., u has higher confidence for in formation provided by $u _ { j _ { 2 } }$

For the same amount of information, a larger amount of reliable (i.e, higher value of $R e ( i , j ) )$ or unreliable information $( \mathrm { i . e . , }$ smaller value of Re(i,j)) leads to higher certainty. As displayed in Fig. 2 (b), the square and diamond markers respectively correspond to a user $u _ { j _ { 1 } }$ whose Re $( i , j _ { 1 } )$ equals 0.1, and a user $u _ { j _ { 2 } }$ whose $R e ( i , j _ { 2 } )$ equals 0.9. u can con fidently ascertain that the information provided by $u _ { j _ { 1 } }$ is unreliable and that provided by $u _ { j _ { 2 } }$ is fairly reliable. However, it is dificult for $u _ { i }$ to ascertain the reliability of the information provided by $u _ { j } ,$ when the amounts of reliable and unreliable information are close $( \mathrm { i } . \mathrm { e } . , R e ( i , j )$ is close to 0.5). As illustrated by the circle marker in Fig. 2 (b), certainty is the smallest in this situation.

After mining ability and certainty from items experienced by $u _ { i }$ and $u _ { j } ,$ we define $\vec { u _ { i } ^ { \prime } s }$ trust degree $T d ( i , j )$ towards $u _ { j }$ as

$$
T d (i, j) = C (i, j) R e (i, j).\tag{6}
$$

A higher value of $T d ( i , j )$ requires $u _ { j }$ to rate more items and accumulate higher similarities with u ’s rated items for improving $R e ( i , j )$ and C(i,j). In Fig. 1, $u _ { 1 } \ ' s$ trust degrees towards $u _ { 2 }$ and $u _ { 7 }$ are 0.1232 and 0.0711.

## 3.2. Quantification of users' needs for diversity

In this subsection, we quantify users' needs for diverse recommendations. Inspired by Shi et al. [18], we argue that $\vec { u _ { i } ^ { \prime } s }$ needs for diverse recommendations is reflected by items in $O _ { i } .$ Higher dissimilarities among the items in $O _ { i }$ indicate $u _ { i }$ has greater needs for diverse recommendations.

Before presenting our quantification method for diversity, we need to preprocess the similarities calculated by Eq. (3). Although it is more dificult for a long-tailed item $o _ { \alpha } \in O _ { i }$ to find common users with other items than for a popular one, the similarities between $o _ { \alpha }$ and other

<table><tr><td></td><td> $O_1$ </td><td> $O_2$ </td><td> $O_3$ </td><td> $O_5$ </td></tr><tr><td> $O_1$ </td><td>3</td><td>1</td><td>3</td><td>2</td></tr><tr><td> $O_2$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $O_3$ </td><td>3</td><td>1</td><td>5</td><td>2</td></tr><tr><td> $O_5$ </td><td>2</td><td>1</td><td>2</td><td>3</td></tr></table>

(a) The number of common users

$$
\mathrm{O} _ {2}
$$

![](/api/attachments/QVB72S4W/fulltext/images/e605b0beb7f9193016a4851d7ef7c4b9450924b397d6a109da63e2380dad40e2.jpg)

<table><tr><td> $o_1$ </td><td>1.0</td><td>0.4054</td><td>0.3814</td><td>0.3731</td></tr><tr><td> $o_2$ </td><td>0.4054</td><td>1.0</td><td>0.1546</td><td>0.2727</td></tr><tr><td> $o_3$ </td><td>0.3814</td><td>0.1546</td><td>1.0</td><td>0.1969</td></tr><tr><td> $o_5$ </td><td>0.3731</td><td>0.2727</td><td>0.1969</td><td>1.0</td></tr></table>

(b) Item similarities

items in $O _ { i }$ may be higher than those calculated with a popular one $o _ { \beta } \in$ $O _ { i } .$ As displayed in Fig. 3, o has more common users with $o _ { 3 }$ and $o _ { 5 }$ than with $o _ { 2 } ,$ while Eq. (3) infers $o _ { 1 }$ has higher similarity with $o _ { 2 } ,$ , which has only one common user with $o _ { 1 }$ , namely, $u _ { 1 } .$ . In terms of items rated by a user, Eq. (3) is unfavorable for popular items. We argue that information delivered by other users should be valued more for identifying item similarities. Therefore, we adopt a power function to adjust the similarities calculated by Eq. (3): $S ( \alpha , \beta ) ^ { \lambda }$ . When $0 < \lambda < 1$ , the diference between item similarities is narrowed.

Similar to the calculation of $\vec { u _ { i } ^ { \prime } s }$ trust degree towards the trustee $u _ { j } ,$ we divide items in O into two disjoint parts, i.e., $O _ { i 1 }$ and $O _ { i 2 } ,$ according to their dissimilarities with other items in $O _ { i }$ and the threshold $\epsilon .$ For $o _ { \alpha }$ ∈ $O _ { i , }$ if there exists at least one item $o _ { \beta } \in O _ { i }$ whose dissimilarities with $o _ { \alpha }$ is no less than $\epsilon , o _ { \alpha }$ belongs to $O _ { i 1 } ,$ , otherwise, $o _ { \alpha }$ belongs to $O _ { i _ { 2 } } .$ . For items in $O _ { i 1 }$ and $O _ { i 2 } ,$ , we respectively calculate their accumulated dissimilarities and similarities with items in $O _ { i }$ as follows:

$$
R (i, i) = \frac {1}{k _ {u i}} \sum_ {o _ {\beta} \in O _ {j 1}} \sum_ {o _ {\alpha} \in O _ {i}} (1 - S (\alpha , \beta) ^ {\lambda}),\tag{7}
$$

$$
I (i, i) = \frac {1}{k _ {u i}} \sum_ {o _ {\beta} \in O _ {j 2}} \sum_ {o _ {\alpha} \in O _ {i}} S (\alpha , \beta) ^ {\lambda}.\tag{8}
$$

In Eq. (7), we use $1 - S ( \alpha , \beta ) ^ { \lambda } ( \lambda > 0 )$ to define the dissimilarity between $o _ { \alpha }$ and $o _ { \beta } .$ . Obviously, larger ϵ indicates more items in $O _ { i }$ belong to $O _ { i 2 } .$ When $\epsilon = 0 . 0 , O _ { i 1 }$ is equivalent to $O _ { i } ,$ and $I ( i , i )$ equals to 0.0.

The values of R(i,i) and I(i,i) depend on u ’s needs for diversity, which are reflected by the dissimilarities among items in O and the total number of items in $O _ { i } .$ When u has experienced more dissimilar items, the value of R(i,i) will be higher than that of $I ( i , i ) ,$ , which indicates u prefers recommendations with more varied features, i.e., higher individual diversity. By respectively substituting $R ( i , j )$ and I(i,j) in Eq. (4) with R(i,i) and I(i,i), we define u ’s needs for individual diversity, i.e., Re(i.i). When $u _ { i }$ has experienced many items. the values of R(i,i) and I(i,i) will be higher than for other users. For experienced users, recommendations with higher novelty may increase serendipity and satisfaction, as it is more time-consuming for them to find interested novel items than readily available bestsellers. By respectively substituting $R ( i , j )$ and $I ( i , j )$ in Eq. (5) with R(i,i) and I(i,i), we define $u _ { i } ^ { \prime } s$

Fig. 3. An example of similarities among items rated by $u _ { 1 }$ in Fig. 1.

![](/api/attachments/QVB72S4W/fulltext/images/725d94247d17d581939c15781b8134fd998916a21685f10851bf808b0e63e325.jpg)  
(a) Step 1

![](/api/attachments/QVB72S4W/fulltext/images/635aa8be65ac183fd88a0966d071bcf3d7aefea9de5d82f6858cbc81a24a01e6.jpg)  
(b) Step 2

![](/api/attachments/QVB72S4W/fulltext/images/93b2afe26b57d7e74b9d5122e55ea3b3fa9c63b63c925147a156f001114e7a89.jpg)

![](/api/attachments/QVB72S4W/fulltext/images/8e730efa497e08fba3d7f3720698ff5452c5b02f476d8c9e95bd03e10c3915ec.jpg)  
(c) Step 3  
(d) Step 4  
Fig. 4. An example of recommendation process for $u _ { 1 }$ in Fig. 1. Note: The grey squares represent items in $O _ { 1 } ;$ (λ, η, σ, γ) is set as (1.5, 0.1, 3.0, 0.5).

needs for novelty, i.e., C(i,i).

Thus, we quantify the needs of $u _ { i }$ for diverse recommendations as

$$
T d (i, i) = C (i, i) R e (i, i).\tag{9}
$$

Td(i,i) reflects $u _ { i } ^ { \prime } s$ total needs for individual diversity and novelty of the recommendation results. Obviously, the Td(i,i) of cold-start users will be smaller than those of experienced users, and increasing λ will improve Td(i,i). For $u _ { 1 }$ in Fig. 1, Td(1,1) equals 0.2188, 0.2996 and 0.3360, respectively, for $\lambda = 0 . 5$ , 1.0 and 1.5. Algorithm 1 shows the details of calculating users' trust degrees towards their trustees and quantifying users' needs for diversity.

Algorithm 1. Calculating trust degrees and users' needs for diversity

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input: A, T, U, O,  $\lambda$ ; Output: T d
2: for each pair of items  $o_{\alpha}$  and  $o_{\beta}$  do
3: Compute item similarity  $S(\alpha,\beta)$  by Eq. (3);
4: end for
5: for each pair of user  $u_{i} \in U$  and the trustee  $u_{j}$  do
6: Divide  $O_{j}$  into  $O_{j1}$  and  $O_{j2}$ ;
7: Compute  $R(i,j)$  and  $I(i,j)$  with  $S(\alpha,\beta)$  by Eqs. (1) and (2);
8: Compute  $Re(i,j)$  and  $C(i,j)$  by Eqs. (4) and (5);
9: Compute  $Td(i,j)$  by Eq. (6);
10: end for
11: for each user  $u_{i} \in U$  do
12: Compute  $R(i,i)$  and  $I(i,i)$  with  $S(\alpha,\beta)^{\lambda}$  by Eqs. (7) and (8);
13: Compute  $Re(i,i)$  and  $C(i,i)$  by Eqs. (4) and (5);
14: Compute  $Td(i,i)$  by Eq. (9);
15: end for
</div>

## 3.3. Recommendation steps on the user-item bipartite network

In this part, we build our model on the user-item bipartite network in four steps, $\mathrm { i . e . , }$ initializing items' resources, transferring resources from items to users, involving trust degrees, and transferring resources back to items. In Fig. 4, we illustrate our recommendation processes for $u _ { 1 }$ in Fig. 1.

First, target user u ’s rated items receive one unit of resource. Then, items' resources follow the bipartite network and distribute to their linked users. In this step, resources of bestsellers are distributed to many users, which may involve several irrelevant users in the sub sequent recommendation processes. To decrease irrelevant users' interference, we utilize item degrees to control the amount of allocated resources. Thus, the resources received by a user $u _ { j }$ can be calculated as

$$
f _ {j} ^ {1} = \sum_ {\alpha = 1} ^ {n} \frac {a _ {j \alpha} f _ {\alpha} ^ {0}}{k _ {o \alpha} ^ {0 . 5}},\tag{10}
$$

where $a _ { j \alpha }$ is an element of the user-item adjacency matrix A, and $f _ { \alpha } ^ { 0 }$ refers to $\omega _ { \alpha } { ' } s$ initial resources and equals 1.0.

After distributing resources to mediate users, we introduce $\vec { u _ { i } ^ { \prime } s }$ trust degrees towards the trustees by

$$
f t _ {j} ^ {1} = f _ {j} ^ {1} + t _ {i j} T d (i, j) ^ {\eta},\tag{11}
$$

where $\eta > 0 . t _ { i j }$ is an element of trust relationship matrix T. η adjusts the magnitudes of extra resources added to u ’s trustees, and can be viewed as a regulator for the efect of $u _ { i } ^ { \prime } s$ trustees. According to $u _ { 1 } \ ' _ { s }$ trust degrees in Fig. 1, we allocate extra 0.8111 and 0.7677 resources to $u _ { 2 }$ and $u _ { 7 }$ with η equal to 0.1 in Fig. 4 (c).

Finally, we redistribute resources from mediate users to their rated items. In this step, we utilize user degrees and item degrees to exert discounting efects on resources distributed from users and received by items, respectively. On the one hand, the discounting efect of user degrees can reduce the resources transferred from experienced users, and generate recommendation lists by collecting resources from more users. In our opinion, the more users participate in the generation process of recommendation lists, the more various information is involved to diversify users' recommendation lists. On the other hand, the discounting efect of item degrees can reduce the resources received by popular items and present more long-tailed items in recommendation lists, which do favor to improve aggregate diversity and novelty. However, excessively exerting these discounting efects will amplify the roles of cold-start users and novel items, and cause extreme damage on accuracy. To deal with these issues, we propose an adaptive strategy and calculate the final resources possessed by item o as

$$
f _ {\beta} ^ {2} = \frac {1}{k _ {o \beta} ^ {\gamma p}} \sum_ {j = 1} ^ {m} \frac {a _ {j \beta} f t _ {j} ^ {1}}{k _ {u j} ^ {(1 - \gamma) p}},\tag{12}
$$

where $0 \leq \gamma \leq 1 , p = \exp ( \sigma T d ( i , i ) - 1 ) \mathrm { ~ }$ , and $\sigma > 0 .$ . p decides the total discounting efects of user degrees and item degrees adaptively according to each user's needs for diversity, and varies with λ and σ. According to Eqs. (7) and (8), λ’s increase will have greater influence on users who have experienced more items, and produce more improvement on their needs for individual diversity and novelty, i.e., Td(i,i). Increasing σ will produce more improvements on p for users with higher values of Td(i,i) and less improvements on p for users with lower values of Td(i,i). γ adjusts the relative discounting efect of user degrees and item degrees, and acts as a regulator for individual diversity and ag gregate diversity. According to the roles of p and $\gamma ,$ our adaptive strategy is capable of improving diversity for users who prefer diverse recommendations, such as experienced users, and ensuring accuracy for users who prefer accurate recommendations, such as cold-start users.

After resource allocation processes, we sort $\vec { u _ { i } ^ { \prime } s }$ unrated items ac cording to the final allocated resources in a descending order and pick the top-N items as $\vec { u _ { i } ^ { \prime } s }$ recommendation list. In Fig. 4, the recommended top-2 items are $o _ { 6 }$ and ${ \cal O } _ { 9 } ,$ which receive resources from four diferent users, $\mathrm { i . e . , ~ } \left\{ u _ { 2 } , u _ { 3 } , u _ { 6 } , u _ { 7 } \right\}$ . When $\gamma$ equals to 0.1, the recommended items are $o _ { 6 }$ and $^ { o _ { 7 } , }$ which receive resources from five diferent users, i.e., {u , u , u u , u }. Compared to $\gamma = 0 . 5 , \gamma = 0 . 1$ involves $u _ { 5 } { ' } s$ resources and improves the individual diversity for $u _ { 1 }$ . When $\gamma$ equals to $^ { 1 . 0 , }$ the recommended items are $o _ { 8 }$ and $^ { O _ { 9 } , }$ , which are the least popular items. Compared to $\gamma = 0 . 5 , \ \gamma = 1 . 0$ improves the novelty for $u _ { 1 } .$ Algorithm 2 displays our recommendation steps. As T d can be calculated in ofline, the computational complexity of Algorithm 2 is $O ( m ^ { 2 } + m n )$

Algorithm 2. Recommendation steps on the user-item bipartite network

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input: A, T, U, O, N,  $\lambda$ ,  $\eta$ ,  $\sigma$ ,  $\gamma$ ; Output: Top-N recommendations
2: Compute T d by Algorithm 1;
3: for each user  $u_{i} \in U$  do
4: for each user  $u_{j} \in U$  do
5:  $f_{j}^{1} \leftarrow 0.0$ 
6: for each item  $o_{\alpha} \in O_{j}$  do
7:  $f_{j}^{1} \leftarrow f_{j}^{1} + a_{j\alpha}f_{\alpha}^{0} k_{o\alpha}^{0.5}$ 
8: end for
9: Compute  $ft_{j}^{1}$  using  $f_{j}^{1}$  and  $Td(i,j)$  by Eq. (11).
10: end for
11: for each item  $o_{\beta} \in O$  do
12:  $f_{\beta}^{2} \leftarrow 0.0$ 
13: for each user  $u_{j} \in U_{\beta}$  do
14:  $f_{\beta}^{2} \leftarrow f_{\beta}^{2} + a_{j\beta}ft_{j}^{1} k_{uj}^{(1-\gamma)p}$ 
15: end for
16:  $f_{\beta}^{2} \leftarrow 1 k_{o\beta}^{\gamma p}f_{\beta}^{2}$ 
17: end for
18: Sort  $o_{\beta} \notin O_{i}$  in the descending order of  $f_{\beta}^{2}$ 
19: Generate  $u_{i}$ 's top-N recommendation list
20: end for
</div>

## 4. Data and experimental settings

In this section, we introduce our experimental datasets, evaluation metrics, experimental settings and the comparing methods.

## 4.1. Datasets

Ciao, Epinions and ${ \tt Y e l p } ^ { 3 }$ are e-commerce websites in which users score items by 1 to 5 and establish trust relationships with others. In our experiments, the experimental datasets of Ciao, Yelp, and Epinions are provided by Guo et al. [41], Feng and Qian [42], and Massa and Avesani [43], respectively. Following Zhou et al. [9], we transform ratings into binary ones: rating values that are no less than 3 are preprocessed into 1 (and 0 if otherwise). Table 2 displays the basic information of experimental datasets. Average number of trust links is calculated on users who establish trust relationships with others. Sparsity is the proportion of links in the bipartite network.

## 4.2. Evaluation metrics

We evaluate the quality of top-N recommendation lists from two aspects, i.e., accuracy and diversity. Accuracy is measured by precision ( ) [6], while diversity is measured by individual diversity ( ) [10], aggregate diversity ( <sub>a</sub>) [11] and novelty ( <sub>n</sub>) [9].

Precision calculates the proportions of users' interested items in their recommendation lists. As ratings below 3 have been filtered out, we regard items in users' test set as their interested items. For a target user $u _ { i } ,$ precision is defined as $N _ { u i } / N . \ N _ { u i }$ means the number of $\vec { u _ { i } ^ { \prime } s }$ interested items in u ’s recommendation list $T _ { u i }$ By averaging the precision of all target users, we obtain the mean precision of the whole system as:

$$
\mathcal {P} = \frac {1}{| U |} \sum_ {u _ {i} \in U} \frac {N _ {u i}}{N},\tag{13}
$$

where U is the set of target users, and $| U |$ is the number of target users. Higher $\mathcal { P }$ indicates more accurate recommendations.

Individual diversity calculates the average dissimilarities among items in each user's recommendation list $T _ { u i s }$ namely

$$
\mathcal {D} _ {i} = \frac {1}{| U |} \sum_ {u _ {i} \in U} \frac {\sum_ {o _ {\alpha} \in T _ {u i}} \sum_ {o _ {\beta} \in T _ {u i}} (1 - s i m (\alpha , \beta))}{N (N - 1)}.\tag{14}
$$

sim $( \alpha { , } \beta )$ is the similarity between item $o _ { \alpha }$ and $^ { O } \beta ,$ and is calculated by cosine similarity. As a diversity metric from the user perspective, a higher $\mathcal { D } _ { i }$ indicates greater diferentiation among each user's recommended items.

Aggregate diversity refers to the total number of distinct items that appear in all users' top-N recommendation lists, namely

$$
\mathcal {D} _ {a} = | \bigcup_ {u _ {i} \in U} T _ {u i} |.\tag{15}
$$

As a diversity metric from systems' perspective, a higher $\mathcal { D } _ { a }$ is preferred.

As an index of recommending unexpected items, novelty is measured by

$$
\mathcal {D} _ {n} = \frac {1}{| U |} \sum_ {u _ {i} \in U} \frac {\sum_ {o _ {\alpha} \in T _ {u i}} \log_ {2} (| U | / k o _ {\alpha})}{N},\tag{16}
$$

where $k o _ { \alpha }$ is the item degree. A higher ${ \mathcal { D } } _ { n }$ indicates that more long tailed items appear in users' recommendation lists.

## 4.3. Experimental settings

In our experiments, we randomly extract 80% of links in the bipartite network to form the training set and treat the remainder as the test set. To make results insensitive to the partition of datasets, we conduct this random selection process 30 times and respectively run our experiments on each data split. Our experimental results are the average of 30 runs.

The experimental target users need to simultaneously satisfy following rules: (1) they have rated items both in the training set and test set; (2) they have established trust relationships with others; and (3) their trustees have rated items in training set. In Epinions and Yelp datasets, we further randomly sample 1000 target users from the appropriate candidates to conduct experiments.

We define cold-start users as users who have rated no more than five items, and experienced users as users who have rated more than 20 items. The long-tailed items are items which have been rated by no more than five users. The threshold ϵ is set to be 0.0005. The length of recommendation lists N is 20.

## 4.4. Comparing algorithms

In our experiments, we compare with several algorithms that utilize binary data for diversifying top-N recommendation lists, i.e., BD [32], Eh\_HHPH [30, 31], SP [33], PLUS [27] and COUSIN [28] and COSRA+T [23]. In Table 1, we have displayed the parameter information of BD, Eh\_HHPH, and SP. Except the range of θ in SP is [0.0,

Table 2  
Basic information of experimental datasets.

<table><tr><td>Datasets</td><td>Users</td><td>Items</td><td>Ratings</td><td>Links</td><td>Trust links</td><td>Average trust links</td><td>Sparsity</td></tr><tr><td>Ciao</td><td>30,444</td><td>16,121</td><td>72,665</td><td>65,038</td><td>40,133</td><td>28</td><td>0.0133%</td></tr><tr><td>Epinions</td><td>49,289</td><td>139,738</td><td>664,824</td><td>570,918</td><td>487,002</td><td>14</td><td>0.0083%</td></tr><tr><td>Yelp</td><td>8351</td><td>84,653</td><td>263,777</td><td>229,207</td><td>524,117</td><td>63</td><td>0.0324%</td></tr></table>

2.5], other parameters are in [0.0, 1.0]. PLUS and COUSIN use $\alpha \in$ [0.0,15.0] to adjust item similarities and $\beta \in \left[ 0 . 0 , 3 . 0 \right]$ to adjust user similarities. The range of COSRA+T's parameter θ is [0.0, 1.0]. In our following experiments, we search appropriate parameters for COSRA+T with step 0.01, and for other algorithms with step 0.1.

## 5. Results and discussion

To evaluate our algorithm, we first conduct a series of experiments to analyze the efect of parameters p and $\gamma ,$ which as defined in Section 3.3 are the key variables that control the adaptability of the diversity and regulate individual and aggregate diversity. Based on parameter setting experiment results, we learn the best parameter setting strategy and then compare our approach with other algorithms in terms of recommendation accuracy and diversity.

## 5.1. Efects of parameters p and γ

In our model, we propose an adaptive strategy which utilizes p and γ to balance the trade-ofs between accuracy and diversity. In this part, we intend to validate the roles of $p$ and $\gamma$ on recommendation accuracy for cold-start users and recommendation diversity for experienced users. Then, we can propose parameter adjustment methods for p and γ to provide more flexible trade-ofs between accuracy and diversity, and participate in subsequent comparative experiments with baseline algorithms.

In our experiments, we set the range of λ and η to be [0.1, 1.5], the range of σ to be [0.1, 2.0], and the range of γ to be [0.0, 1.0]. Through exhaustive experiments, we obtain $( \lambda ^ { ^ { * } } , \eta ^ { ^ { * } } , \sigma ^ { ^ { * } } , \gamma ^ { ^ { * } } )$ which is the settings of $( \lambda , \eta , \sigma , \gamma )$ corresponding to the maximal precision. For each pair of $( \lambda ,$ γ), we calculate $p \mathbf { \hat { s } }$ average values p¯ respectively for cold-start and experienced users. By fixing $\eta$ to be $\eta ^ { * }$ , we can observe the common influence of p¯ and γ on accuracy for cold-start users and diversity for experienced users by contour plots in Figs. 5 and $^ { 6 . }$

In Figs. 5 and $^ { 6 , }$ we have four main findings. First, though λ and σ vary in the same ranges for cold-start and experienced users, p¯ changes in a narrower range in Fig. 5 than in Fig. 6. This observation confirms that when we increase $\begin{array} { r l } { ( \lambda , } & { { } \sigma ) _ { \mathrm { { i } } } } \end{array}$ , our model will produce more improvements on p for experienced users to enhance their diversity, and less improvements on $p$ for cold-start users to ensure their accuracy. Second, the sparse contours in the bottom of Fig. 5 indicate that increasing p causes less accuracy loss than increasing γ. According to the location of red stars, decreasing $p \ \mathrm { { o r } \ \gamma }$ can improve precision for coldstart users further. Third, the sparse yellow lines and red stars in the first row of Fig. 6 indicate that increasing p or decreasing γ is able to improve individual diversity for experienced users. At last in the second and third rows of ${ \mathrm { F i g . ~ } } 6 ,$ the dense contours in the bottom left corner and the sparse yellow contours in the upper right corner illustrate that increasing p or γ does favor to improve aggregate diversity and novelty. In Fig. 6, the positive correlation between p and all diversity metrics and $\gamma \mathbf { \hat { s } }$ contrary performance in individual diversity and aggregate di versity confirm that their roles in our model are as expected.

![](/api/attachments/QVB72S4W/fulltext/images/e88b5feb0edcc1e5a7a2c2482c34940230b4cb27d7a2a0c9ef589919e05f236e.jpg)  
(a) $\mathcal { P }$ in Ciao dataset.

Based on above analysis, we can intentionally increase $p , \mathrm { i . e . , } ( \lambda , \sigma )$ to simultaneously improve individual diversity, aggregate diversity and novelty. Alternatively, we can decrease γ to collaborate with $p ^ { \prime } s$ increase, when $p ^ { \prime } s$ increase plays little efect on individual diversity.

## 5.2. Recommendation performance on accuracy and diversity

In this subsection, we compare our algorithm with other algorithms presented in Section 4.4 with four metrics. Based on experiments using all possible parameter combinations, we find that no single algorithm outperforms other algorithms across all evaluation metrics, which demonstrates the dificulty to reach optimal accuracy and optimal diversity simultaneously [9]. In this situation, we adopt the parameter setting strategy as presented in BD [32], SP [33] and COSRA+T [23] to give maximal precision more priority in experiments.

Tables 3 to 5 display experimental results for each dataset. We display comparative algorithms' parameter settings for maximal precision behind their names. TrAdBi1 corresponds to the results of our algorithm with maximal precision. We utilize TrAdBi2 to exemplify changes on accuracy and diversity after implementing our parameter adjustment methods. Besides, we also illustrate recommendation accuracy for cold-start users and long-tailed items in Fig. 7 and recommendation diversity for experienced users in Fig. 8.

For comparative algorithms in Tables 3 to 5, our main findings are

![](/api/attachments/QVB72S4W/fulltext/images/9ee7141a62be263f78c94cb1b2cb52bf70b36463eceb56bc4f18ceae8b3eb03c.jpg)  
(b) $\mathcal { P }$ in Epinions dataset.

![](/api/attachments/QVB72S4W/fulltext/images/e64a6742f0f2fe42478e3850149b07a02baad7c298ac8f46f448a87849a362be.jpg)  
(c) $\mathcal { P }$ in Yelp dataset.  
Fig. 5. Effect of p and γ on precision for cold-start users. Note: 1. Red star markers are located on $( \bar { p } ^ { * } , \gamma ^ { * } )$ in which $\bar { p } ^ { * }$ is p's average value for cold-start users on $( \lambda ^ { \ast }$ σ<sup>\*</sup>). 2. We expand to its 100 times. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

Table 4  
![](/api/attachments/QVB72S4W/fulltext/images/6d9e274a1d1b246e8db11f6a3f077e65e8215ab6f142620a8a075642659bf918.jpg)

![](/api/attachments/QVB72S4W/fulltext/images/24d8c18bce656c1647c9c4b3d94f3a04861cbc5c25991e22332d5ae8fc5f0232.jpg)  
(a) $\mathcal { D } _ { i }$ in Ciao dataset.

![](/api/attachments/QVB72S4W/fulltext/images/8435e19a379b895dd8826d35c8ad155fece76720a5e86f507240398c633d0f80.jpg)  
(c) $\mathcal { D } _ { i }$ in Yelp dataset.

(b) $\mathcal { D } _ { i }$ in Epinions dataset.  
![](/api/attachments/QVB72S4W/fulltext/images/5bed4e5770ff535351e9a8fd34b4497e980348c3fd3ed87c56729c6b6a5941d1.jpg)

![](/api/attachments/QVB72S4W/fulltext/images/d53a27367d86b35d8046cc0852223f9e7ea5dab0cceef42f372c6dcbf5a48a10.jpg)

![](/api/attachments/QVB72S4W/fulltext/images/4100b7d02b419af3db9c4b95c69eea97866ca1ffbd7b5b84d0f60b766a3135c5.jpg)

(d) $\mathcal { D } _ { a }$ in Ciao dataset.  
![](/api/attachments/QVB72S4W/fulltext/images/5f1ea2927768ac99cf7825b0946ba3c1690d74abbc151b85f46c515f630abdc9.jpg)  
$\mathcal { D } _ { n }$ in Ciao dataset

(e) $\mathcal { D } _ { a }$ in Epinions dataset.  
(f) $\mathcal { D } _ { a }$ in ${ \mathrm { Y e l p } }$ dataset.  
![](/api/attachments/QVB72S4W/fulltext/images/0e05a261eb156fcc402930f5ffcb83a47e6021b27079d00428adf350158e5cee.jpg)  
(h) $\mathcal { D } _ { n }$ in Epinions dataset.

![](/api/attachments/QVB72S4W/fulltext/images/f150f944ba520d98073ecbdf9cf3da1175891037da56d35db741931c7319e7ca.jpg)  
$\mathcal { D } _ { n }$ ${ \mathrm { Y e l p } }$ dataset.  
Figure 6. Effect of $\overline { { p } }$ and $\gamma$ on diversity for experienced users. Note: Red star

Fig. 6. Efect of p¯ and γ on diversity for experienced users. Note: Red star markers are located on $( \bar { p } ^ { * } , \gamma ^ { * } )$ in which $\bar { p } ^ { * }$ is p’s average value for experienced users on $( \lambda ^ { \ast }$ , σ<sup>\*</sup>). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

Results of experimental algorithms in Epinions dataset.  
Table 3  
Results of experimental algorithms in Ciao dataset.

<table><tr><td>Experimental algorithms</td><td> $\mathcal{P}(\times 10^{-2})$ </td><td> $\mathcal{D}_{i}$ </td><td> $\mathcal{D}_{a}$ </td><td> $\mathcal{D}_{n}$ </td></tr><tr><td>BD ( $a = 0.1, b = 0.6$ )</td><td>1.276</td><td>0.931</td><td>3827</td><td>5.624</td></tr><tr><td>Eh_HHPH ( $\sigma = 0.5, \eta = 0.6, \lambda = 0.9$ )</td><td>1.539</td><td>0.916</td><td>3472</td><td>5.315</td></tr><tr><td>SP ( $\theta = 1.5, \lambda = 1.0$ )</td><td>1.217</td><td>0.921</td><td>3840</td><td>5.687</td></tr><tr><td>PLUS ( $\beta = 1.9$ )</td><td>1.441</td><td>0.943</td><td>2739</td><td>4.702</td></tr><tr><td>COUSIN ( $\alpha = 10.0, \beta = 0.5$ )</td><td>1.319</td><td>0.855</td><td>4309</td><td>6.971</td></tr><tr><td>COSRA + T ( $\theta = 0.51$ )</td><td>0.735</td><td>0.900</td><td>5076</td><td>7.532</td></tr><tr><td>TrAdBi1 ( $\lambda = 0.1, \eta = 0.7, \sigma = 1.1, \gamma = 0.3$ )</td><td>1.691</td><td>0.890</td><td>3593</td><td>5.372</td></tr><tr><td>TrAdBi2 ( $\lambda = 1.3, \eta = 0.7, \sigma = 1.2, \gamma = 0.3$ )</td><td>1.471</td><td>0.912</td><td>4160</td><td>6.191</td></tr></table>

<table><tr><td>Experimental algorithms</td><td> $\mathcal{P}(\times 10^{-2})$ </td><td> $\mathcal{D}_{i}$ </td><td> $\mathcal{D}_{a}$ </td><td> $\mathcal{D}_{n}$ </td></tr><tr><td>BD ( $a = 0.1, b = 0.4$ )</td><td>1.572</td><td>0.949</td><td>6627</td><td>3.770</td></tr><tr><td>Eh_HHPH ( $\sigma = 0.5, \eta = 0.7, \lambda = 0.8$ )</td><td>1.680</td><td>0.940</td><td>8098</td><td>4.606</td></tr><tr><td>SP ( $\theta = 0.5, \lambda = 0.8$ )</td><td>1.515</td><td>0.948</td><td>8367</td><td>4.627</td></tr><tr><td>PLUS ( $\beta = 2.2$ )</td><td>1.590</td><td>0.948</td><td>4560</td><td>2.939</td></tr><tr><td>COUSIN ( $\alpha = 14.6, \beta = 0.5$ )</td><td>1.573</td><td>0.919</td><td>8249</td><td>5.443</td></tr><tr><td>COSRA + T ( $\theta = 0.58$ )</td><td>0.592</td><td>0.929</td><td>14,574</td><td>8.829</td></tr><tr><td>TrAdBi1 ( $\lambda = 0.1, \eta = 0.3, \sigma = 1.0, \gamma = 0.4$ )</td><td>1.904</td><td>0.902</td><td>7305</td><td>4.153</td></tr><tr><td>TrAdBi2 ( $\lambda = 0.4, \eta = 0.3, \sigma = 1.5, \gamma = 0.2$ )</td><td>1.593</td><td>0.941</td><td>8652</td><td>4.721</td></tr></table>

Table 5  
Results of experimental algorithms in Yelp dataset.

<table><tr><td>Experimental algorithms</td><td> $\mathcal{P}(\times 10^{-2})$ </td><td> $\mathcal{D}_{i}$ </td><td> $\mathcal{D}_{a}$ </td><td> $\mathcal{D}_{n}$ </td></tr><tr><td>BD ( $a = 0.0, b = 0.5$ )</td><td>1.824</td><td>0.914</td><td>6851</td><td>5.967</td></tr><tr><td>Eh_HHPH ( $\sigma = 0.5, \eta = 0.7, \lambda = 0.9$ )</td><td>2.033</td><td>0.877</td><td>7245</td><td>6.043</td></tr><tr><td>SP ( $\theta = 1.0, \lambda = 1.0$ )</td><td>1.677</td><td>0.898</td><td>8533</td><td>6.486</td></tr><tr><td>PLUS ( $\beta = 1.7$ )</td><td>2.005</td><td>0.899</td><td>5706</td><td>5.537</td></tr><tr><td>COUSIN ( $\alpha = 10.7, \beta = 0.6$ )</td><td>1.819</td><td>0.845</td><td>9473</td><td>7.384</td></tr><tr><td>COSRA + T ( $\theta = 0.63$ )</td><td>0.801</td><td>0.851</td><td>12,192</td><td>9.041</td></tr><tr><td>TrAdBi1 ( $\lambda = 0.1, \eta = 0.5, \sigma = 1.1, \gamma = 0.3$ )</td><td>2.219</td><td>0.862</td><td>6694</td><td>5.805</td></tr><tr><td>TrAdBi2 ( $\lambda = 0.6, \eta = 0.5, \sigma = 1.2, \gamma = 0.3$ )</td><td>1.906</td><td>0.880</td><td>8175</td><td>6.780</td></tr></table>

as follows: 1. Eh\_HHPH is the most accurate one; 2. BD, SP and PLUS perform better on individual diversity; 3. COUSIN and COSRA+T have higher aggregate diversity and novelty. Compared to these algorithms, TrAdBi1 has leading precision, and outperforms PLUS in aggregate diversity and novelty. In Fig. 7, we find that TrAdBi1 keeps its advantage on precision for cold-start users, and recommends long-tailed items more accurately than all comparative algorithms except COSRA+T whose aggregate diversity and novelty are far greater than others'. Though TrAdBi1 is inferior to SP and COUSIN in aggregate diversity and novelty, i.e., it recommends fewer long-tailed items, its higher precision for long-tailed items indicates that our model mines users' preferences more suficiently and is more conducive to promote the sales of long-tailed items [16]. In terms of recommendation diversity for experienced users displayed in Fig. 8, the aggregate diversity and novelty of TrAdBi1 are superior to these of Eh\_HHPH and PLUS in Ciao and Yelp datasets, and exceed all comparative algorithms except COSRA+T in Epinions dataset. Compared to Ciao and Yelp datasets, Epinions dataset is sparser in ratings and possesses fewer average trust links. These observations indicate that TrAdBi1 has better performance on diversity for experienced users from sparse datasets.

Through our parameter adjustment methods, TrAdBi2 improves recommendation diversity by sacrificing TrAdBi1's advantages on accuracy. In Fig. 7, we find that TrAdBi2 still keeps TrAdBi1’s advantages on accuracy for cold-start users and long-tailed items. This finding in dicates that our parameter adjustment methods have little influence on cold-start users and long-tailed items. Compared to other algorithms in Tables 3 to 5, TrAdBi2 is superior to Eh\_HHPH and PLUS in aggregate diversity and novelty, superior to BD and SP in precision and novelty, and superior to COUSIN and COSRAT in precision and individual diversity. Besides these advantages, TrAdBi2’s performance for experi enced users also outperforms Eh\_HHPH and PLUS in individual diversity, and outperforms COUSIN in aggregate diversity and novelty. Compared to its performance in Ciao and Yelp datasets, TrAdBi2 performs more outstanding in diversity for experienced users in Epinions dataset. This observation further confirms that our algorithm possesses more advantages on diversity in sparse datasets.

In Table 6, we show the average runtimes of TrAdBi1 and com parative algorithms. The computational complexity for calculating similarity matrix is $O ( m ^ { 2 } n )$ or $O ( n ^ { 2 } m )$ , which is time-consuming for cycling calculation. This process appears in Eh\_HHPH, PLUS, COUSIN and TrAdBi1. As it can be implemented in ofline, we merely count the computational complexity and runtimes for generating recommendation results. Our algorithm has the same complexity with BD, Eh\_HHPH, SP and COSRA+T, which conduct recommendation processes based on the user-item bipartite network. Except PLUS and BD, our algorithm are more eficiency than other algorithms.

## 6. Conclusions

In this study, we build an adaptive trust-aware recommendation model to accomplish accurate recommendations for cold-start users and long-tailed items, and improve recommendation diversity from three aspects, i.e., individual diversity, aggregate diversity and novelty. To utilize trust relationships, we quantify uses' trust degrees towards their trustees by inferring their trustees' ability for providing reliable information and users' certainty about their trustees' ability. Simultaneously, we quantify users' needs for diversity based on the dissimilar level of their experienced items. During the resource allocation processes, we propose a new method to involve information from users' trustees, and build an adaptive strategy by considering the discounting efects of user degrees and item degrees to produce users' recommendation lists according to their needs for diversity.

Through experiments on three datasets, we confirm that our algorithm is able to improve accuracy for cold-start users and long-tailed items, and diversity for experienced users, especially in sparse datasets like Epinions dataset. Although TrAdBi1’s diversity is not outstanding, its accuracy outperforms all comparative algorithms. In terms of the trade-of between accuracy and diversity, TrAdBi1 inclines more to accuracy. According to parameter analysis for the roles o $\dot { } p$ and $\gamma ,$ we propose parameter adjustment methods. By comparing TrAdBi2 with other algorithms, we have exemplified that our parameter adjustment methods ofer more flexible trade-ofs between accuracy and diversity, which are capable of efectively improving diversity for experienced users, and ensuring high accuracy for cold-start users and long-tailed items simultaneously.

## 7. Implications

In our study, several interesting points are meaningful for researchers and practitioners of recommender systems. First, our trust

![](/api/attachments/QVB72S4W/fulltext/images/eddf7b9b20c4559280977c014791ec1916d0a682226410947fdb24e47742c1d3.jpg)  
(a) Precision for cold-start users  
Fig. 7. Precision for cold-start users and long-tailed items.

![](/api/attachments/QVB72S4W/fulltext/images/8fdc0f5333a7a7076d66f56c48521cc144440a0c742fe1acaec439035297330d.jpg)  
(b) Precision for long-tailed items

![](/api/attachments/QVB72S4W/fulltext/images/90e6a909332b1605d09ccd8d231093bf013bf50d776175be95a21adc7f857418.jpg)

![](/api/attachments/QVB72S4W/fulltext/images/7920ea93dc33f71b30813424b7cf0319c3a28bb54228d12025efb035dd7b4234.jpg)

![](/api/attachments/QVB72S4W/fulltext/images/04579a846e6078f92058d5f5cd62889ca0904021d9d1f84578c7101428ea8aa4.jpg)  
Fig. 8. Diversity of all algorithms for experienced users.

Table 6  
Runtimes of experimental algorithms (s).

<table><tr><td>Algorithms</td><td>Complexity</td><td>Ciao</td><td>Epinions</td><td>Yelp</td></tr><tr><td>BD</td><td> $O(m^{2} + mn)$ </td><td>161</td><td>2765</td><td>1338</td></tr><tr><td>Eh_HHPH</td><td> $O(mn)$ </td><td>1439</td><td>-</td><td>-</td></tr><tr><td>SP</td><td> $O(m^{2} + mn)$ </td><td>386</td><td>6425</td><td>3014</td></tr><tr><td>PLUS</td><td> $O(mn)$ </td><td>35</td><td>655</td><td>308</td></tr><tr><td>COUSIN</td><td> $O(mn)$ </td><td>1050</td><td>-</td><td>-</td></tr><tr><td>COSTA+T</td><td> $O(m^{2} + mn)$ </td><td>345</td><td>6141</td><td>2934</td></tr><tr><td>TrAdBi</td><td> $O(m^{2} + mn)$ </td><td>246</td><td>4284</td><td>2042</td></tr></table>

Note: m is the number of users, and n is the number of items.

model considers two parties' roles of a trust relationship, i.e., trustees ability and trustors' certainty, and takes advantage of not only common rated items, but also items similar to a user's rated items. Our algorithm's high accuracy for long-tailed items and TrAdBi1’s leading precision demonstrate the efectiveness of our trust model. It is advisable to build trust models by utilizing more information and considering the joint roles of multiple parties, such as trustors, trustees and service platforms. Second, we propose a new method to combine users' interests with their trustees' tastes. In our model, we allocate extra resources to a user's trustees based on our inferred trust degrees. Instead of a unified level, the total efect of these trustees depends on trust degrees of this user towards them and previous experiences of this user. Third, our model builds links among accuracy and diferent dimensions of diversity in the last step of resource allocation. According to the roles of p and σ, we have proposed parameter adjustment methods and exemplified their efectiveness by TrAdBi2. We believe it is useful to build links among diferent evaluation metrics to coordinate them appropriately for producing recommendations with comprehensive advantages.

Our work has several practical implications for businesses and users. First, our model treats each user separately and make the trade-ofs between accuracy and diversity according to their needs. For users who prefer accurate recommendations, such as cold-start customers, its high accuracy is conducive to improve their familiarity and perceived usefulness with the e-commerce websites [44]. For users who prefer diverse recommendations, such as experienced users, it also recommends more novel products with diferent features to personalize their experiences and improve their retention rates for businesses' benefits. Second, parameter adjustment methods according to the roles of p and γ allow businesses to set parameters intentionally for serving their shortterm or long-term profits. If businesses want to earn more profits in short time, they can utilize accuracy-oriented parameters to produce recommendations with high accuracy and increase users' purchase rates. If business pay more attention to long-term gains, they can adjust $\boldsymbol { p } ^ { * } \ \mathrm { o r } \ \gamma ^ { * }$ to produce more diverse recommendations and get more knowledge of users' preferences for diferent item features. Third, our algorithm recommends long-tailed items accurately, which benefit both businesses and users. From business perspective, long-tailed items possess high marginal profit and boost the efect of “one-stop shopping convenience”. From user perspective, it is more dificult and timeconsuming to search interesting novel items by themselves than readily available bestsellers.

## 8. Limitations and future work

At the technical level, it is time-consuming to obtain a set of parameters in accord with an expected goal, although we acquire each parameter's role on accuracy and diversity. We need a more eficient method to produce the desired parameters easily. In our experiments, we utilize four metrics to evaluate the results; some experimental algorithms have outstanding performance on one or two metrics, but none can defeat others in all metrics. This phenomenon increases the dificulty of evaluation. The concept of Pareto dominance may be used to decide parameter settings for balancing multiple metrics, or to decide the best algorithms. A comprehensive metric is also valuable for evaluating the experimental algorithms more eficiently and more purposefully. Moreover, experimental comparisons with more algorithms in diferent datasets are essential for more comprehensively evaluating our algorithms.

Other context information, such as item content information, time information, and location information, can be used to grasp users' interests to more accurately recommend novel items and diversify users recommendation lists. The structure information about a bipartite network and a trust network may contribute to parameter selection and construction of recommender algorithms. In addition, in e-commerce platforms, there also exist diferent types of retailers that provide services of diferent quality and at diferent prices. Related information about retailers' reliability should be taken into account to produce more practical recommendations.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China (Grant No. 71671121), which is gratefully acknowledged.

## References

[1] J. Bobadilla, F. Ortega, A. Hernando, A. Gutiérrez, Recommender systems survey, Knowledge-Based Systems 46 (2013) 109–132.

[2] C.A. Gomez-Uribe, N. Hunt. The Netflix recommender system: algorithms. business value, and innovation. ACM Transactions on Management Information Systems 6 (4) (2015) 1–19.

[3] B. Smith, G. Linden, Two decades of recommender systems at Amazon,com, IEEE Internet Computing 21 (3) (2017) 12–18

[4] S.-H. Park, S.P. Han. From accuracy to diversity in product recommendations: relationship between diversity and customer retention, International Journal of Electronic Commerce 18 (2) (2014) 51–72

[5] M. Kunaver, T. Požrl, Diversity in recommender systems — a survey, Knowledge-Based Systems 123 (2017) 154–162.

[6] J.L. Herlocker, J.A. Konstan, L.G. Terveen, J.T. Riedl, Evaluating collaborative fil tering recommender systems, ACM Transactions on Information Systems 22 (1) (2004) 5–53.

[7] D.M. Fleder, K. Hosanagar, Recommender Systems and Their Impact on Sales

Diversity, Proceedings of the 8th ACM Conference on Electronic Commerce, ACM, 2007, pp. 192–199.

[8] S. Goel, A. Broder, E. Gabrilovich, B. Pang, Anatomy of the long tail: ordinar people with extraordinary tastes, Proceedings of the Third ACM Internationa Conference on Web Search and Data Mining, ACM, 2010, pp. 201–210.

[9] T. Zhou, Z. Kuscsik, J.-G. Liu, M. Medo, J.R. Wakeling, Y.-C. Zhang, G. Parisi, Solving the apparent diversity-accuracy dilemma of recommender systems, Proceedings of the National Academy of Sciences of the United States of America 107 (10) (2010) 4511–4515.

[10] K. Bradley, B. Smyth, Improving recommendation diversity, Proceedings of the Twelfth Irish Conference on Artificial Intelligence and Cognitive Science, 2001, pp. 85–94.

[11] G. Adomavicius, Y.O. Kwon, Improving aggregate recommendation diversity using ranking-based techniques, IEEE Transactions on Knowledge and Data Engineering 24 (5) (2012) 896–911

[12] G. Adomavicius, Y. Kwon, Optimization-based approaches for maximizing aggregate recommendation diversity, INFORMS Journal on Computing 26 (2) (2014) 351–369.

[13] T. Aytekin, M.Ö. Karakaya, Clustering-based diversity improvement in top-N re commendation, Journal of Intelligent Information Systems 42 (1) (2014) 1–18.

[14] T. Zhou, J. Ren, M. c. v. Medo, Y.-C. Zhang, Bipartite network projection and personal recommendation, Physical Review E - Statistical, Nonlinear, and Soft Matter Physics 76 (2007) 046115.

[15] Y.-C. Zhang, M. Blattner, Y.-K. Yu, Heat conduction process on community networks as a recommendation model. Physical Review Letters 99 (15) (2007) 1–4.

[16] B. Gu, O. Tang, A.B. Whinston, The influence of online word-of-mouth on long tail formation. Decision Support Systems 56 (1) (2013) 474–481

[17] M. Kaminskas, D. Bridge, Diversity, serendipity, novelty, and coverage: a survey and empirical analysis of beyond-accuracy objectives in recommender systems, ACM Transactions on Interactive Intelligent Systems 7 (1) (2016) 1–42.

[18] Y. Shi, X. Zhao, J. Wang, M. Larson, A. Hanjalic, Adaptive diversification of recommendation results via latent factor portfolio. Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2012, pp. 175–184.

[19] T. Di Noia, J. Rosati, P. Tomeo, E.D. Sciascio, Adaptive multi-attribute diversity for recommender systems, Information Sciences 382-383 (2017) 234–253.

[20] W. Wu, L. Chen, Y. Zhao, Personalizing recommendation diversity based on use personality, User Modeling and User-Adapted Interaction 28 (3) (2018) 237–276.

[21] J. Lu, D. Wu, M. Mao, W. Wang, G. Zhang, Recommender system application developments: a survey. Decision Support Systems 74 (2015) 12–32

[22] H. Liu, X. Bai, Z. Yang, A. Tolba, F. Xia, Trust-aware recommendation for improving aggregate diversity, New Review of Hypermedia and Multimedia 21 (3-4) (2015) 242–258.

[23] L.J. Chen, J. Gao, A trust-based recommendation method using network difusion processes, Physica A: Statistical Mechanics and its Applications 506 (2018) 679–691.

[24] S. Wang, M. Gong, H. Li, J. Yang, Multi-objective optimization for long tail re commendation, Knowledge-Based Systems 104 (2016) 145–155.

[25] A. Gogna, A. Majumdar, DiABlO: optimization based design for improving diversity in recommender system. Information Sciences 378 (2017) 59–74.

[26] M.Ö. Karakaya, T. Aytekin, Efective methods for increasing aggregate diversity in recommender systems. Knowledge and Information Systems 56 (2) (2018) 355-372.

[27] M. Gan, R. Jiang, Improving accuracy and diversity of personalized recommendation through power law adjustments of user similarities, Decision Support Systems 55 (3) (2013) 811–821.

[28] M. Gan, COUSIN: a network-based regression model for personalized re commendations. Decision Support Systems 82 (2016) 58–68

[29] F. Yu, A. Zeng, S. Gillard, M. Medo, Network-based recommendation algorithms: a review, Physica A: Statistical Mechanics and its Applications 452 (2016) 192–208

[30] C. Liu, W.X. Zhou, Heterogeneity in initial resource configurations improves a network-based hybrid recommendation algorithm, Physica A: Statistical Mechanic and its Applications 391 (22) (2012) 5704–5711.

[31] Y.H. An, Q. Dong, C.J. Sun, D.C. Nie, Y. Fu, Difusion-like recommendation with enhanced similarity of objects, Physica A: Statistical Mechanics and its Applications 461 (2016).708–715

[32] D.C. Nie, Y.H. An, Q. Dong, Y. Fu, T. Zhou, Information filtering via balanced diffusion on bipartite networks, Physica A: Statistical Mechanics and its Applications 421 (2015) 44–53.

[33] A. Zeng, A. Vidmer, M. Medo, Y.C. Zhang, Information filtering by similarity-preferential difusion processes, Europhysics Letters 105 (5) (2014) 58002.

[34] C.-S. Hwang, Y.-P. Chen, Using trust in collaborative filtering recommendation New Trends in Applied Artificial Intelligence, Springer-Verlag, 2007, pp. 1052–1060.

[35] P. Moradi, S. Ahmadian, F. Akhlaghian, An efective trust-based recommendation method using a novel graph clustering algorithm. Physica A: Statistical Mechanics and its Applications 436 (2015) 462–481.

[36] Y. Feng, H. Li, Z. Chen, Improving recommendation accuracy and diversity via multiple social factors and social circles, International Journal of Web Service Research 11 (4) (2014) 32–46

[37] H. Zhang, D. Ge, S. Zhang, Hybrid recommendation system based on semantic interest community and trusted neighbors, Multimedia Tools and Applications 77 (4) (2018) 4187–4202.

[38] Y. Wang, M.P. Singh, Evidence-based trust: a mathematical model geared for multiagent systems, ACM Transactions on Autonomous and Adaptive Systems 5 (4) (2010) 1–28.

[39] Y. Wang, C.-W. Hang, M.P. Singh, A probabilistic approach for maintaining trust based on evidence, Journal of Artificial Intelligence Research 40 (1) (2011) 221–267.

[40] Y. Wang, M.P. Singh, Formal trust model for multiagent systems, Proceedings of the 20th International Joint Conference on Artifical Intelligence, Morgan Kaufmann Publishers Inc., 2007, pp. 1551–1556.

[41] G. Guo, J. Zhang, D. Thalmann, N. Yorke-Smith, ETAF: an extended trust antecedents framework for trust prediction, Proceedings of the 2014 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining, IEEE Press, 2014, pp. 540–547.

[42] H. Feng, X. Qian, Recommendation via user's personality and social contextual, Proceedings of the 22Nd ACM International Conference on Information & Knowledge Management, ACM, 2013, pp. 1521–1524.

[43] P. Massa, P. Avesani, Trust-aware collaborative filtering for recommender systems, Lecture Notes in Computer Science 3290 (2004) 492–508

[44] B. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, MIS Quarterly 31 (1) (2007) 137–209.

![](/api/attachments/QVB72S4W/fulltext/images/6563a74198f86a85444c0a813ff69cecee35fadf4ddb13a75fac82c617f24524.jpg)  
Ting Yu is a PH. D. student in the College of Management and Economics, Tianjin University, China. She is under the supervision of Prof. Junpeng Guo. She received her master’s degree of Management Science and Engineering from the College of Management and Economics, and her bachelor’s degree in Mathematics and Applied Mathematics from the College of Science in Tianjin University. Her main research interests include social network, trust models and recommender systems.

![](/api/attachments/QVB72S4W/fulltext/images/724f4494b0bbdd24242a42d763ff3766292b6d68fc2f4d4bc11fee2a757b6cfe.jpg)

Junpeng Guo received his Ph. D. degree in Management Science from Tianjin University. China. 2004. He is now a professor of Dept. of Information Management and Management Science in Tianjin University. His main research interests include social media, recommender system, symbolic data analysis and operational research. He is the principal investigator of several projects funded by National Natural Science Foundation of China. He has authored over 40 technical papers in international journals, China journals and international conferences. Additionally, he is the qualified member of Operational Research Society of China (ORSC) and the Director of Operational Research Society of Tianjin, China. He has also served as reviewer of many international journals and conferences. In 2010, he was in

vited as the visiting professor at Mays Business School of Texas A&M University, US. In 2016, he was invited as the visiting professor at Dept. of Information Systems at National University of Singapore.

![](/api/attachments/QVB72S4W/fulltext/images/2f1477e2c6e85e9b2e39743ddddee51ec894da11613771421b5aaa83e5cd309f.jpg)

Wenhua Li received her Ph. D. degree in Management Science from Tianjin University, China, 2007. She is now an associate professor at College of Management and Economics in Tianjin University. Her main research interests include statistical data analysis and financial econometrics. She has authored over 20 technical papers in international journals, China journals and international conferences.

![](/api/attachments/QVB72S4W/fulltext/images/8808d6341b40bb4f297dad206a4c57c820c0046430e2f06645aa7150ee299f8d.jpg)

Harry Jiannan Wang is a Professor of Management Information Systems (MIS) at the University of Delaware. He received Ph.D. in MIS from the Eller College of Management, University of Arizona, USA and B.S. in MIS from Tianjin University, China. His research interests involve artificial intelligence, business analytics, business process management, services computing, and enterprise systems. He has published research articles in journals, such as Information Systems Research, Decision Support Systems, ACM Transactions on Management Information Systems, Journal of Database Management, and Information and Management. Dr. Wang has serviced as guest editor, associate editor, and editorial board member for many leading IS journals and also been a co-chair,

program co-chair, program committee member, and track co-chair for numerous academic conferences.

![](/api/attachments/QVB72S4W/fulltext/images/5eee7c85919230ecf8761627701c2bdb13dfb488b8c601d1df84eec35d06a625.jpg)

Dr. Ling Fan is a scholar and entrepreneur to bridge machine intelligence and creativity. Dr. Fan is the founding chair of Tongji University Design Artificial Intelligence Lab and the founder of Tezign.com, a leading technology startup with the mission to build digital infrastructure for creative resources. Before. he taught at the University of California at Berkeley and China Central Academy of Fine Arts. Dr. Fan is a World Economic Forum Young Global Leader, and an Aspen Institute China Fellow. He received a doctoral degree from Harvard University and master's degree from Princeton University.
