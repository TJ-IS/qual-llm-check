---
otero_id: 4828
otero_key: "CDCDXX55"
title: "Category role aided market segmentation approach to convenience store chain category management"
authors: "Shuihua Han; Yongjie Ye; Xin Fu; Zhilong Chen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Category role aided market segmentation approach to convenience store chain category management

Shuihua Han, Yongjie Ye, Xin Fu ⁎, Zhilong Chen

Department of Management Science, School of Management, Xiamen University, Xiamen 361005, China

## a r t i c l e i n f o

Article history: Received 5 December 2012 Received in revised form 11 September 2013 Accepted 21 September 2013 Available online 16 October 2013

Keywords: Category management Market segmentation Convenience store chain management Strategic decision support

## a b s t r a c t

Category management (CM) plays an increasingly important role in retailing management, as it aids retailers to increase their core competitiveness, maximise pro<sup>fi</sup>ts and ensure a good long-term customer relationship. This technique has been successfully applied to diverse large manufacturers and wholesale retailers. However, it remains a challenging task to directly employ the CM technique in convenience store (CVS) chain(s). This is because CVS chains are often distributed in a variety of areas, each store has impulsive consumers, and the traditional market segmentation attributes (e.g. consumer age, salary, and background) are dif<sup>fi</sup>cult to collect under such circumstances. This makes it impractical to apply one general CM solution to all CVS chains. Hence, it is crucial to segment a market region and then apply customised CM solutions to the corresponding segments. This paper presents an innovative market segmentation model which is driven by category-role (CR), for the <sup>fi</sup>rst time, to support CM in CVS chains. A new similarity measure (named HCsim()) and an improved weighted fuzzy K-means clustering algorithm (WFKM) are developed in an effort to cluster the CVSs. The usefulness and applicability of this study is illustrated by means of an empirical study to provide marketing strategy decision support. The derived results are also discussed and compared with existing methods.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Convenience store (CVS) refers to a small store that stocks everyday items such as groceries, beverages and snacks. Convenience is its distinguished strength that attracts consumers. Modern CVSs normally utilise store chain management methods and represent one of the fastest growing segments in the retail market. Such rapid growth brings increasing competition amongst CVS retailers. In recent years, category management (CM) [3,21,38] has gradually gained popularity in these companies to increase their core competitiveness, maximise pro<sup>fi</sup>ts and ensure long-term healthy customer relationship.

CM is a business fundamental that uncovers untapped potential to be explored. It aims to analyse consumer purchasing behaviour and stock the products that consumers are most likely to buy. The basic idea of CM is managing product categories as business unit and customising them to satisfy customers' needs [18]. More speci<sup>fi</sup>cally, the de<sup>fi</sup>ned categories can be used to target the consumer groups and to gain a better understanding of their needs. From early 1990s, CM can be divided into two types: product-centric CM [6,51] and consumer-centric CM [1,14,31]. Product-centric CM uses historical transaction data to gain insights into product movements, so as to identify and employ product attributes to determine a product category. This widely used approach straightforwardly re<sup>fl</sup>ects the movement of products, and historical transaction data is relatively easy and cheap to collect. However, this approach re<sup>fl</sup>ects the overall movement of products, and it is hard to further identify customers' future needs, if no detailed consumer data is available. In consumer-centric CM, the demographics, attitudes, interests, shopping occasions and historical purchase records of consumers are taken into account to segmenting and targeting consumers who share similar purchase patterns. Subsequently, a marketing plan for each distinct consumer group is developed. This approach is driven by the understanding that consumer behaviour can change the design of a product category. A distinct advantage of this approach is that product category is designed by considering diverse customer groups, so that the derived category structure is transparent and interpretable. Also, marketing plans based on this approach can be more ef<sup>fi</sup>cient and accurate. However, this in turn naturally requires the presence of consumer data, and if such data is not available, it is quite costly to collect.

Although CM attracts increasing attentions and some initial results have been obtained [11,14,26,43], applying conventional CM methods to CVS chain management remains a challenging task due to its distinguished features. First, CVSs are often distributed in a variety of areas and each store has impulsive consumers. For example, petrol station CVSs can be located at a city centre, the outskirts of a city or on a motorway. Within the same category, different CVSs may have to provide different products to meet the diverse requirements of their consumers. Second, due to the mobility of CVSs' consumers, especially for the CVSs located at the outskirts of a city or on a motorway, it is dif<sup>fi</sup>cult to collect consumer related data (e.g., the demographics, interests, and shopping occasions) by employing the royalty membership programme. Hence, the conventional consumer-centric CM approaches become less appropriate to analyse and group consumers of CVS chains. Third, CVSs are often small and have very limited storage space, such that it cannot provide a large number of product categories. This leads suppliers to invest most of their time and effort on their large retailers, rather than on CVS chains. This is evident in [1] that ACNielsen mainly provides CM support to wholesalers and supermarket chains, i.e. General Mills, Big Y, SUPERVALU, etc.

To overcome the above dif<sup>fi</sup>culties, this paper proposes an innovative market segmentation model which employs category roles (CRs), for the <sup>fi</sup>rst time, to support CM in CVS chains. Due to the mobility of CVSs' consumers, the consumer related data (e.g., the demographics, interests, and shopping occasions) are dif<sup>fi</sup>cult to collect. The proposed method is still a product-centric approach, but it is equipped with some new features: a) it is a value-centric approach that recognises the values of a category to retailers, consumers and the marketplace; b) it provides a dynamic view, since the growing potential of a category is considered rather than just focusing on a static view.

This new method takes three CR dimensions (importance to retailers, consumers, and the marketplace) into account to segment the market. Distinct market segments can receive a customised CM and marketing strategy. Additionally, the retailer can perceive the market with <sup>fi</sup>ne granularity, and better analyse different behaviour patterns. Initially, the historical transaction data provides a full view of the market. Such data are then used to derive a global category index (CIX) for each store. CVSs that share similar CIXs are clustered into the same group by using a new similarity measure, named HCsim() and an improved weighted fuzzy K-means clustering algorithm (WEKM). Based on the obtained clustering results, the retailer can design varied CM and marketing strategies for different CVS clusters.

The remainder of this paper is organised as follows: Section 2 reviews the existing approaches in CM and market segmentation. In Section 3, a novel method, the CR-based market segmentation model, is proposed to cluster CVSs. In addition, an improved clustering algorithm which employs HCsim() is also introduced in this section. The applicability and utility of the proposed method is demonstrated in Section 4 via an empirical study. The derived results are analysed and discussed in Section 5. The <sup>fi</sup>nal section concludes this paper and points out future work directions.

## 2. Background

## 2.1. Category management

CM was introduced in 1990 as an organised process to enable retailers to effectively reach consumers, while maximising pro<sup>fi</sup>ts. It aims to <sup>fi</sup>nd appropriate products and prices for the target customers, so that the customers are satis<sup>fi</sup>ed and remain loyal to retailers. Many retailers today have adopted the fundamental eight-step process [3] to conduct CM, including Define category, Assign a category role, Assess a category, Set performance and scorecard, Create market strategy, Choose tactics, Implement the plan and Review.

The biggest change over the years in CM is moving from productcentric [11,23,51] to consumer-centric [1,10,24]. A few researchers [10,11,31,40] have posited that different category characteristics can re<sup>fl</sup>ect different consumer needs. They believe that a key tenet of CM is that the retailer should decide the role each category plays in the retailer's overall portfolio. One popular classi<sup>fi</sup>cation schema to assign CR is cross-category quantitative analysis [14,26] which considers the importance to consumers, retailers and the marketplace. The typical four CRs are:

• Destination category: make the store the primary category provider. When consumers would like to purchase products in a certain category, the store is their main choice. This category plays a key role in retailing and distinguishes the store from other competitors. It involves 5%–10% of categories in the store.

• Routine category: make the store one of the preferred category providers. The price of daily necessities is not sensitive and reasonably stable. This category generates solid pro<sup>fi</sup>ts for retailers, while meeting customers' various daily needs. It involves 50%–70% of categories in the store.

• Occasional/seasonal category: make the store a major category provider when consumers would like to buy a given occasional/ seasonal product. The demands for such a category are not stable and are normally short-term. It involves 10%–15% of categories in the store.

• Convenience category: this category helps the store to provide convenience to consumers, so that consumers can buy all they need from a store in one stop. It involves 10%–15% of categories in the store.

CRs are essential to maintain a consistent strategic and tactic plan that provides cohesive market approaches regarding price, promotion and assortment. It is pointed out that the same category may act as a different CR in different stores [43], so that customised category strategies should be implemented in different market segments.

## 2.2. Market segmentation

Market segmentation was initially de<sup>fi</sup>ned by Smith in 1956 [42]. It has been well recognised that a mass market strategy has little chance of success in a highly competitive market. The objective of market segmentation is to divide a heterogeneous market into a number of smaller homogeneous markets in which consumers share suf<sup>fi</sup>ciently similar characteristics. This helps the retailer to identify the consumer groups, and use resources more effectively to match consumers' needs.

In general, existing market segmentation methods can be categorised into two main approaches [17,47,48]: the <sup>fi</sup>rst is the priori approach [16,17]. It segments the market according to prior knowledge or speculated factors that are associated with consumers, services or products (such as demographic characteristics, purchase amounts and geographic areas). The second is a widely used approach called posthoc segmentation. Different from the priori approach, it segments the market by analysing market data. More and more segmentation techniques are becoming available for the post-hoc approach [2,46], including clustering [12], classi<sup>fi</sup>cation and regression trees (CART) [15], self-organising map (SOM) [27], and multi-objective evolutionary algorithms (MOEA) [34].

The selection of segmentation variables is an essential step in building segmentation models. Many scholars generalise segmentation variables from many perspectives, ranging from demographic, geographic, purchasing behaviours to consumer values. Segmentation variables can be classi<sup>fi</sup>ed into two groups: general variables [33,48] and product-speci<sup>fi</sup>c variables [44,47]. General variables focus on neighbourhoods' attributes (such as geographic, lifestyles and demographics) rather than on individual consumers. Product-speci<sup>fi</sup>c variables concern consumers' preferences and their responses to products. These variables involve customer demands, intentions and purchasing behaviours.

Since 1956, market segmentation has dramatically expanded its applications to various domains, such as the online shopping market [28], the printed circuit board industry [8], and the tourist market [30]. However, the application of market segmentation is still at a relatively early stage for the retail industry [5,35], particularly when taking consumer demands into consideration. Currently, retailers normally employ uni<sup>fi</sup>ed or traditional segmentation attributes to segment the market, while ignoring underlying and potential consumer characteristics and demands. In particular, little research has been conducted in CVS segmentation. For CVSs, the concept of market segmentation can be employed and expanded to cluster stores into different market segments. This is because the store features (e.g., store location, and historical transaction data) usually carry useful but hidden information regarding consumer behaviours and preferences that cannot be easily exploited by traditional market segmentation approaches. By employing clustered market segmentation, different marketing strategies can be applied to market segments that consist of stores that share similar features, so that consumer requirements can be better satis<sup>fi</sup>ed and more pro<sup>fi</sup>ts can be achieved. This paper mainly concerns the applicability of using market segmentation techniques to segment CVSs to achieve better CM.

## 2.2.1. RFM segmentation model

RFM (recency, frequency, and monetary) is a purchase-behaviour based segmentation model [39,44]. It utilises consumers' historical transaction data to analyse and segment the market. This model is easy to use and has been widely employed in a variety of marketing areas [19,25,45]. The foundation of the RFM model includes three purchase attributes:

• The most recent purchase timestamp, “R” (recency): this is the time difference between the last purchase timestamp and the current timestamp of a given product. A smaller time interval indicates that this product is more likely to be purchased by this consumer.

• The purchase frequency, “F” (frequency): given a period of time, the number of purchase times of a given product. A higher frequency implies that this product is more popular.

• The total purchase volume, “M” (monetary): given a period of time, the total amount of money this consumer spent. Obviously, a higher value indicates that a consumer is more valuable to a retailer, as he/ she contributes more towards the retailer's pro<sup>fi</sup>ts.

In the RFM model, the involved attributes are based on historical transaction data; hence they are relatively handy to collect. However, there exist several drawbacks when applying RFM to CVS market segmentations. First, the analysis of the RFM model is not based on an individual category but instead reveals consumer behaviour for the whole store. Second, for a CVS, the pro<sup>fi</sup>ts of different categories can be quite different. Some products show low pro<sup>fi</sup>t which only exists for providing convenience to consumers. The RFM model only concerns the total purchase volume, without considering the pro<sup>fi</sup>ts in each category. Therefore, it is hard to re<sup>fl</sup>ect the importance of a given category to retailers. Third, given that the analysis is based on historical transaction data, the model may not be suitable to predict future consumer behaviour. To sum up these drawbacks, the RFM is more appropriate to analyse consumer behaviour for individual stores rather than CVS chains.

## 3. CR-based market segmentation approach

Considering the drawbacks of the RFM model and the problem at hand, this section proposes an innovative CR-based market segmentation model, which is particularly suitable for CVS chains.

## 3.1. Category index (CIX)

Cross-category quantitative analysis [3,14,26] has been widely used in the assignment of CRs. In this method, three dimensions (as shown in Table 1) should be taken into consideration and they are described below:

• The importance to consumers: refers to consumers' demands for this category. If a category is more desirable to consumers, then it is more essential and important to consumers. Some indicators exist to measure this dimension, such as the purchase frequency, annual expenditure and purchase volume.

• The importance to retailers: refers to the sales performance of a given category. Since CVSs are often small and have very limited storage space, the categories that are included in CVSs should be carefully selected by retailers. The selection of categories can result in diverse CVS sales performances. Therefore, sales volume, sales gross pro<sup>fi</sup>ts, and ef<sup>fi</sup>ciency plateau are often used to measure this dimension.

Table 1  
Three dimensions of CR.

<table><tr><td>Three dimensions</td><td>Measures</td></tr><tr><td>The importance to consumers</td><td>Annual expenditure; purchase frequency; purchase volume</td></tr><tr><td>The importance to retailers</td><td>Sales volume; sales revenue; sales gross profit; efficiency plateau</td></tr><tr><td>The importance to the marketplace</td><td>Average growth rate; purchase trends; market share changes trends</td></tr></table>

• The importance to the marketplace: while the <sup>fi</sup>rst two dimensions rely on the current status of categories, this dimension re<sup>fl</sup>ects the importance of a given category in the future. It refers to consumers' future demand and purchase propensity. In order to seize market opportunities, CVSs should not only focus on different categories current market status, but also need to consider the categories future development. Some indicators can be used to measure this dimension, such as the average growth rate of a given category, purchase trends, and market share trends.

Due to the availability of dimension measures, <sup>fi</sup>ve segmentation attributes are selected to aggregate a new category index (CIX):

$$
C I X _ {i} = \omega_ {F} F _ {i} + \omega_ {N} N _ {i} + \omega_ {S} S _ {i} + \omega_ {R} R _ {i} + \omega_ {G} G _ {i}\tag{1}
$$

where CIX is the index value of category i, and F , N , S , R and G represent the average sales frequency, average sales volume, average sales revenue, average gross pro<sup>fi</sup>t and average growth rate of category i, respectively. ω , ω , ω , ω and ω represent the corresponding attribute weights and $\omega _ { F } + \omega _ { N } + \omega _ { S } + \omega _ { R } + \omega _ { G } = 1$ . Different from the conventional RFM model, this CR-based model not only reveals consumer desirability and purchase behaviour for a given category, but also takes the retailer's mission and market development direction into consideration to provide a global index value (CIX), and to measure category contributions for retailers.

The new CIX that considers consumers, retailers and the marketplace is employed to build an innovative market segmentation model (as shown in Fig. 1). In the new model, the market is divided into several segments where similar CVSs are grouped together.

## 3.2. CR-based CVS clustering

Clustering is a well-established unsupervised learning method used to explore patterns in a given problem. It aims to group a set of objects that share similar attributes into the same cluster. This technique has been widely used in many <sup>fi</sup>elds, including machine learning, pattern recognition, image analysis, information retrieval, and bioinformatics. Clustering is also a commonly used technique in market segmentation. Thanks to the rapid development of IT in retailing, transaction data becomes easier to collect and this makes it possible to employ clustering techniques to build the newly proposed CR-based market segmentation model.

Suppose that a retailer has N CVSs distributed in different areas and each store has M product categories. Clustering analysis aims to group similar CVSs into the same cluster with regard to their CIXs that are represented by the aforementioned <sup>fi</sup>ve segmentation attributes, including F, N, S, R and G. Although a CVS sells a relatively small number of categories, it is still often required to provide 20–30 categories to meet consumer needs. Therefore, the problem at hand is an $N \times M$ highdimensional clustering problem. Solving such a high-dimensional problem, conventional clustering methods may easily suffer from the curse of dimensionality [50]. The traditional algebraic distance (e.g., Euclidean distance) becomes less precise with the increase of dimensions. To reduce this possibility, a new similarity measure is proposed herein:

![](/api/attachments/CDCDXX55/fulltext/images/64e0b858a916269f64b64c31747bed3069bbc3de78efba5d9eedc1a2c2d8075c.jpg)  
Fig. 1. CR-based market segmentation model.

De<sup>fi</sup>nition 1. Given a category set $\mathbf { C } = \{ c _ { 1 } , c _ { 2 } , \cdots , c _ { M } \}$ , the number of included categories is $l = \vert \mathbf { C } \vert$ . For each category $c _ { i } \in \mathbf { C } ,$ , its category structure is represented as $c _ { i } = \{ p _ { i 1 } , p _ { i 2 } , ~ { \stackrel { . . . } { \cdot } } , p _ { i j } , ~ { \stackrel { . . . } { \cdot } } , p _ { i k } \}$ , where $P _ { i j }$ indicates the jth sub-category or product of the category $c _ { i }$ and $k = | c _ { i } |$ is the total number of sub-categories or products of $c _ { i \cdot }$

De<sup>fi</sup>nition 2. Suppose that $\pmb { S } = \{ s _ { 1 } , s _ { 2 } , \cdots , s _ { N } \}$ is a set of CIX values of all CVSs that belong to a retailer. Given a CVS j, its CIX values of its included categories in a given period of time can be represented as:

$$
s _ {j} = \left\{\mathbf {C} _ {\mathbf {j}} ^ {\prime}, \mathbf {C I X} _ {\mathbf {j}} \right\} = \left\{\left(c _ {j 1} ^ {\prime}, C I X _ {j 1}\right), \left(c _ {j 2} ^ {\prime}, C I X _ {j 2}\right), \dots , \left(c _ {j m} ^ {\prime}, C I X _ {j m}\right) \right\}\tag{2}
$$

where m is the number of categories of $\mathrm { C V } S j$ and C is a non-empty subset of category set C.

De<sup>fi</sup>nition 3. Given two CVSs j and k, their CIX values are written ${ \mathsf { a s } } s _ { j } =$ $\left\{ \mathbf { C _ { j } ^ { ' } } , C I X _ { \mathbf { j } } \right\}$ and $s _ { k } = \Big \{ \mathbf { C _ { k } ^ { ' } } , \mathbf { C } \pmb { I } \pmb { X _ { k } } \Big \} . p _ { j k } ( c _ { i } )$ represents the ratio of common sub-categories or products in category c that are shared by store j and k.

$$
p _ {j k} (c _ {i}) = \frac {\left| c _ {i j} \cap c _ {i k} \right|}{\left| c _ {i j} \cup c _ {i k} \right|}\tag{3}
$$

where $c _ { i j }$ and $c _ { i k }$ are the sub-category or product collection of category c in stores j and k, respectively, and $c _ { i j } { \in } \mathbf { C } _ { \mathrm { ~ j ~ } } ^ { ' }$ and $c _ { i k } { \in } \mathbf { C } _ { \textbf { k } } ^ { ' }$

Based on the features of CVS category data, coupled with both the similarity between category structures and the similarity in data space, a revised category similarity measure, HCsim(), is de<sup>fi</sup>ned as:

$$
H C s i m \left(s _ {j}, s _ {k}\right) = \frac {\sum_ {i = 1} ^ {L} \frac {p _ {j k} \left(c _ {i}\right)}{1 + \left| C I X _ {j i} - C I X _ {k i} \right|}}{L}\tag{4}
$$

where $L = \left| \mathbf { C _ { j } ^ { ' } } \cup \mathbf { C _ { k } ^ { ' } } \right|$ is the total number of categories that are sold by stores j and k. This similarity measure has the following properties:

• The greater similarity value indicates that the two CVSs are more similar to each other.

$0 \leq H C s i m ( s _ { j } , s _ { k } ) \leq ,$ , if and only if two CVSs are identical, then $H C s i m ( s _ { j } , s _ { k } ) = 1$ . In contrast, when $H C s i m ( s _ { j } , s _ { k } ) \to 0 , \operatorname { C V S s } j$ and k are totally different.

• This measure is symmetric, $\mathsf { i . e . , } H C s i m ( s _ { j } , s _ { k } ) = H C s i m ( s _ { k } , s _ { j } )$

This distance function differs from traditional distance functions. Its value re<sup>fl</sup>ects the similar dimensions (categories, in this case) between any two stores and is less affected by dissimilar categories, thus, the more categories shared by two stores, the more similar the two stores are, and vice versa. It matches the natural human-being perceptions well.

By applying the properties of HCsim(), for simplicity, the HCsim() measure can be rewritten as:

$$
H C s i m \left(s _ {j}, s _ {k}\right) = \frac {\sum_ {i = 1} ^ {L} \left(1 - \frac {p _ {j k} \left(c _ {i}\right)}{1 + \left| C I X _ {j i} - C I X _ {k i} \right|} - X \left(c _ {i}\right)\right)}{\sum_ {i = 1} ^ {L} \left(1 - X \left(c _ {i}\right)\right)},\tag{5}
$$

$$
\text { where } X (c _ {i}) = \left\{ \begin{array}{l l} 0 & c _ {i} \notin \mathbf {C ^ {\prime}} _ {j} \text { and } c _ {i} \notin \mathbf {C ^ {\prime}} _ {\mathbf {k}} \\ 1 & \text { otherwise. } \end{array} \right.
$$

Guided by the CR theory, different categories play different roles in a CVS. Additionally, even the same category can play different roles in different CVSs. Therefore, when clustering the CVSs it is not reasonable to assume a given category is equally important to all CVSs. It is required to dynamically assign different weights to different categories, according to their own category attributes.

An improved weighted fuzzy K-means clustering algorithm (WFKM) that employs the previously proposed HCsim() similarity measure is proposed herein to cluster CVSs. The objective function, that WFKM aims to minimise, can be de<sup>fi</sup>ned as follows:

$$
\begin{array}{l} J _ {W F K M} = \sum_ {i = 1} ^ {K} \sum_ {j = 1} ^ {N} \mu_ {i j} ^ {m} H C s i m _ {\omega} \left(s _ {j}, q _ {i}\right) \\ = \sum_ {i = 1} ^ {K} \sum_ {j = 1} ^ {N} \mu_ {i j} ^ {m} \frac {\sum_ {i = 1} ^ {L} \omega_ {i k} ^ {\beta} \left(1 - \frac {p _ {s _ {j} q _ {i}} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})\right)}{\sum_ {i = 1} ^ {L} (1 - X (c _ {i}))}. \end{array}\tag{6}
$$

This objective function satis<sup>fi</sup>es:

$$
\mu_ {i j} \in [ 0, 1 ], \sum_ {i = 1} ^ {K} \mu_ {i j} = 1, \text { and } 1 \leq j \leq N,\tag{7}
$$

$$
\omega_ {i k} \in [ 0, 1 ], \sum_ {k = 1} ^ {L} \omega_ {i k} = 1, \text { and } 1 \leq i \leq K,\tag{8}
$$

where K is the number of clusters, L is the number of categories; $q _ { i }$ is the centroid of the ith cluster, $\mu _ { i j }$ indicates the membership degree of store j belonging to cluster i. ${ \bf \nabla } , \omega _ { i k }$ is the newly introduced important weight of category k to cluster i, and $p _ { s _ { j } q _ { i } } ( c _ { i } )$ is the category similarity between stores $s _ { j }$ and $q _ { i } ,$ also m N 1 and $\dot { \beta } > 1$

By applying $\operatorname { E q } . \ ( 7 )$ and the Lagrangian function, the objective function can be rewritten as:

$$
J _ {W F K M} = \sum_ {i = 1} ^ {K} \sum_ {j = 1} ^ {N} \mu_ {i j} ^ {m} H C s i m _ {\omega} \left(s _ {j}, q _ {i}\right) - \sum_ {j = 1} ^ {N} \lambda_ {j} \left(\sum_ {i = 1} ^ {K} \mu_ {i j} - 1\right),\tag{9}
$$

where $\lambda _ { j }$ is the Lagrangian parameter.

By applying Eq. $( 9 ) , \mu _ { i j }$ can be written as:

$$
\mu_ {i j} = \frac {1}{\left(\sum_ {r = 1} ^ {K} \frac {H C s i m _ {\omega} (s _ {j} , q _ {i})}{H C s i m _ {\omega} (s _ {j} , q _ {r})}\right) ^ {\frac {1}{m - 1}}}.\tag{10}
$$

In this equation, when $s _ { j } = q _ { i } ,$ it indicates that sample point $s _ { j }$ and cluster centroid $q _ { i }$ are identical, i.e., $H C s i m _ { \omega } ( s _ { j } , q _ { i } ) = 0 .$ . In this case, the membership degree of $s _ { j }$ belonging to cluster i is equal to 1, whereas the membership degrees o $\dot { \mathbf { \sigma } } _ { S _ { j } }$ belonging to other clusters are equal to 0.

Similarly, $\omega _ { i k }$ can be calculated as:

$$
\omega_ {i k} = \frac {1}{\left(\sum_ {t = 1} ^ {L} \frac {\sum_ {j = 1} ^ {N} \mu_ {i j} ^ {m} \frac {1 - \frac {p _ {b} (c _ {t})}{1 + | C D _ {e} - C D _ {a} |} - X (c _ {t})}{1 - X (c _ {t})}}{\sum_ {j = 1} ^ {N} \mu_ {i j} ^ {m} \frac {1 - \frac {p _ {b} (c _ {t})}{1 + | C D _ {e} - C D _ {a} |} - X (c _ {t})}{1 - X (c _ {t})}}\right) ^ {1 / \beta - 1}}\tag{11}
$$

when $X ( c _ { i } ) = 1$ , this indicates category $\tau _ { i }$ is not available in both $\mathrm { C V S } ,$ , so that this category contributes less in regard to clustering. Set

$$
\frac {1 - \frac {p _ {j k} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})}{1 - X (c _ {i})} = 1,\tag{12}
$$

for the objective function $J _ { W F K M } ,$ then set:

$$
R _ {i} = \sum_ {j = 1} ^ {N} \frac {\sum_ {i = 1} ^ {L} \mu_ {i j} ^ {m} \omega_ {i k} ^ {\beta} \left(1 - \frac {p _ {j k} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})\right)}{\sum_ {i = 1} ^ {L} (1 - X (c _ {i}))}\tag{13}
$$

$$
T _ {i j} = \frac {\sum_ {i = 1} ^ {L} \mu_ {i j} ^ {m} \omega_ {i k} ^ {\beta} \left(1 - \frac {p _ {j k} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})\right)}{\sum_ {i = 1} ^ {L} (1 - X (c _ {i}))}\tag{14}
$$

where $R _ { i }$ re<sup>fl</sup>ects the total fuzzy similarity degree between data objects and the centroid of category i, and $T _ { i j }$ represents the fuzzy similarity degree between $s _ { j }$ and the centroid of category i.

To obtain the minimal value of J , R is required to obtain the minimal value in each category. Given the category vector $\mathbf { Q } _ { \mathbf { i } } = \{ q _ { i 1 } ,$ $q _ { i 2 } , \cdots , q _ { i x } , \cdots , q _ { i n } \}$ , the purpose is to <sup>fi</sup>nd a q that satis<sup>fi</sup>es the following equation to be the new cluster centroid.

$$
R _ {i} = \min _ {\mathbf {Q} _ {i}} \sum_ {j = 1} ^ {N} \frac {\sum_ {i = 1} ^ {L} \mu_ {i j} ^ {m} \omega_ {i k} ^ {\beta} \left(1 - \frac {p _ {j k} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})\right)}{\sum_ {i = 1} ^ {L} (1 - X (c _ {i}))}.\tag{15}
$$

Given a dataset $\mathbf { Q _ { i } } ,$ the algorithm to <sup>fi</sup>nd the cluster centroid, q , can be summarised below:

Algorithm 1. Find\_centric(Q<sub>i</sub>)

1: Randomly choose $n _ { r }$ sample points from $\mathbf { Q _ { i } }$ as the training dataset.

2: Calculate the sum o $\mathbf { \dot { T } } _ { i , q _ { i I } }$ between $n _ { r }$ and the remaining data points in $\bf { Q _ { i } } ,$ which can be represented as:

$$
S T _ {i x} = \sum_ {r = 1} ^ {n _ {r}} T _ {i, q _ {i r}} = \sum_ {r = 1} ^ {n _ {r}} \frac {\sum_ {i = 1} ^ {L} \mu_ {i j} ^ {m} \omega_ {i k} ^ {\beta} \left(1 - \frac {p _ {j k} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})\right)}{\sum_ {i = 1} ^ {L} (1 - X (c _ {i}))}.
$$

3: Choose n with minimal $S T _ { i x }$ as the testing dataset.

4: Calculate the sum of $T _ { i , q _ { i \nu } }$ between testing dataset and the remaining data points in $\bf { Q _ { i } } ,$ which can be represented as:

$$
S T _ {i t} ^ {\prime} = \sum_ {y = 1} ^ {n} T _ {i, q _ {i y}} = \sum_ {y = 1} ^ {n} \frac {\sum_ {i = 1} ^ {L} \mu_ {i j} ^ {m} \omega_ {i k} ^ {\beta} \left(1 - \frac {p _ {j k} (c _ {i})}{1 + | C I X _ {j i} - C I X _ {k i} |} - X (c _ {i})\right)}{\sum_ {i = 1} ^ {L} (1 - X (c _ {i}))}.
$$

5: Make the testing dataset with the minimal $S T _ { i t }$ to be the centroid of category i.

Similar to the conventional fuzzy C-means clustering algorithm, WFKM can be quickly converged. However, the cluster results are quite sensitive to the initial chosen cluster centroids. Thus, the selection of the initial centroid plays a crucial role for clustering. Randomly choosing the initial centroids may result in diverse clustering results that may converge to local optima. To solve this, this work employs a data density based algorithm [32] to select the initial cluster centroids. This algorithm is based on the assumption that the centroid of each cluster has more intensive data density than other data points. It aims to <sup>fi</sup>nd the top K intensive density data points as the initial cluster centroids.

## Algorithm 2. WFKM()

1: $m = 0 , J _ { W F K M } ^ { m } = \xi ( \xi$ is a large positive constant)

2: choose K initial cluster centroid $q _ { i } ^ { m } , \omega _ { i k } ^ { m } = \scriptstyle \frac { 1 } { L } ( 1 \leq i \leq K , 1 \leq k \leq L )$

3: set $m = m + 1$

4: cluster data points to each cluster, based on HCsim()

5: calculate $\mu _ { i j } ^ { m } ,$ , by applying Eq. (10)

6: update $\omega _ { i j } ^ { m } ( 1 \leq i \leq K , 1 \leq k \leq L )$ by applying Eq. (11)

7: while $| J _ { W F K M } ^ { m ^ { - } } - J _ { W F K M } ^ { m } | > \alpha$ (α is a pre-de<sup>fi</sup>ned small constant) and mb M do

8: $m = m + 1$

9: cluster data points to each cluster, based on HCsim()

10: calculate $\mu _ { i j } ^ { m } ,$ , by applying Eq. (10)

12: end while

11: update $\omega _ { i j } ^ { m } ( 1 \leq i \leq K , 1 \leq k \leq L )$ by applying Eq. (11)

![](/api/attachments/CDCDXX55/fulltext/images/7ff98e6d5c858ec57178d788e1f4984458ae9337ceaa8ab9ee1e4a53650829a0.jpg)  
Fig. 2. CR-based CVS clustering.  
total of 20 major categories and 75 CVSs remain. This dataset is then imported into a database which includes three types of data: 1) category transaction data (re<sup>fl</sup>ects consumer demands and purchase behaviour on a certain category), 2) category distribution data (represents the category de<sup>fi</sup>nition and structure in different CVSs), and 3) store basic data (represents geographical information of CVSs, etc.). The <sup>fi</sup>ve segmentation attributes used in the proposed model (i.e. F, N, S, R and G) are derived on a monthly basis. To start with, normalisation is performed on these attributes by using the Min–Max method, in which the value of each attribute is mapped onto a range of [0,1].

In summary, the CR-based CVS clustering approach can be illustrated in Fig. 2. The data processing step aims to <sup>fi</sup>lter out missing and noisy data points, and derives a reliable dataset for further use. After that, by the joint use of HCsim() and WFKM, the CVSs are grouped into different clusters, each cluster re<sup>fl</sup>ecting a different market segment. The derived clustering results can then be used to support the development of effective marketing strategies. Ultimately, analysis of the clustering results helps to gain a better understanding of market segments and consumers. It also provides solid evidence for the implementation of CM and appropriate marketing strategies for CVSs.

## 4. Data and empirical results

An empirical study is conducted to verify the proposed model in this section. A dataset from PetroChina is used. It contains transaction records that are collected from 82 petrol CVSs during January–June, 2009 in Guangdong province, China. The dataset contains 2 category levels: 21 major categories and 95 sub-categories, and 3456 products. In addition, QlikView and MATLAB are employed in this work to support the clustering analysis.

## 4.1. Data preprocessing

Initially, noisy, erroneous and missing data is removed from the dataset. In this case, 7 out of 82 CVSs (which only contain transaction data for January and February) are <sup>fi</sup>ltered out. Meanwhile, the Fast food category is also removed due to missing transaction data. Thus, a

## 4.2. Clustering analysis of CVS market segmentation

This paper employs $\begin{array} { r } { \nu = \frac { D _ { m a x _ { d } } } { D _ { m i n _ { d } } } - 1 } \end{array}$ to validate the applicability of the proposed HCsim() measure in the given problem. Given a d-dimensional problem domain, $D _ { m a x _ { d } } = \mathrm { m a x } _ { 1 \leq \mathbf { i } \leq \mathbf { N } , 1 \leq \mathbf { j } \leq \mathbf { N } } H C s i m ( s _ { i } , s _ { j } )$ denotes the largest distance between any two stores, i.e., the ith store (s ) and the jth store (s ). While $\begin{array} { r } { D _ { m i n _ { d } } = \operatorname* { m i n } _ { 1 \leq \mathbf { i } \leq \mathbf { N } , 1 \leq \mathbf { j } \leq \mathbf { N } } H C s i m ( s _ { i } , s _ { j } ) } \end{array}$ denotes the shortest distance. Mathematically speaking, with the increase of dimensionality(d), if v approaches 0, this indicates that $D _ { m a x _ { d } }$ and $D _ { m i n _ { d } }$ are close to each other, so that the distance measure is not suitable for the problem at hand [13]. For comparison purposes, the relationships between dimensionality and v of HCsim() and v of traditional city-block distance [9] are illustrated in Fig. 3, respectively. With the increase in dimensionality, the v of city-block distance approaches 0, while the v of HCsim() gradually increases. Therefore, HCsim() is more appropriate to handle high-dimensional problems.

## 4.2.1. The clustering analysis process

After the data preprocessing and normalisation, the next step is to determine the weights of the <sup>fi</sup>ve segmentation attributes. There are several methods to determine the weights of attributes, such as AHP, Delphi, and the entropy method. Since AHP and Delphi methods arrive at the attribute weights by the use of manual assignments, the results tend to be more subjective and more likely to cause manual biases. Also, in this work, it is dif<sup>fi</sup>cult to <sup>fi</sup>nd a suf<sup>fi</sup>cient number of quali<sup>fi</sup>ed professional CM managers to manually evaluate these attributes. In contrast, the entropy method is a purely data-driven approach, and the obtained results can be more objective. In information theory, entropy is a measure of the uncertainty in a random variable [41]. In [41], entropy quanti<sup>fi</sup>es the expected value of the information contained in a message, and Shannon entropy is the average unpredictability in a random variable, that is equivalent to its information content. Therefore, it is the method used in this paper to determine the weights of the <sup>fi</sup>ve attributes. The detailed calculation step is as follows:

1. Based on the normalised data in Section 4.1, an m × n matrix $R _ { i j } =$ $( r _ { i j } ) _ { m \times n } , ( i = 1 , 2 , \cdots , m ; j = 1 , 2 , \cdots , n )$ of the <sup>fi</sup>ve attributes is built.

2. Convert $R _ { i j } = ( r _ { i j } ) _ { m x n }$ into a normalised matrix $\boldsymbol { R } _ { i j } ^ { ' } = \left( \boldsymbol { r } _ { i j } \right) _ { m \tilde { n } n }$ by using the following equation

$$
r _ {i j} = \frac {r _ {i j}}{\sum_ {i = 1} ^ {m} r _ {i j}}, i \in m, j \in n.\tag{16}
$$

3. Calculate the output information entropy,

$$
E _ {j} = - \frac {1}{\ln m} \sum_ {i = 1} ^ {m} r _ {i j} \ln r _ {i j}, j \in n,\tag{17}
$$

when $r _ { i j } ^ { ' } = 0 , s e t r _ { i j } ^ { ' } \mathrm { l n } r _ { i j } ^ { ' } = 0 .$

4. Calculate the <sup>fi</sup>ve attribute weights $\omega = ( \omega _ { 1 } , \omega _ { 2 } , \cdots , \omega _ { n } )$ , where

$$
\omega_ {j} = \frac {1 - E _ {j}}{\sum_ {k = 1} ^ {n} (1 - E _ {k})}.\tag{18}
$$

The obtained results are shown in Table 2.

Based on Table 2 and collected transaction data, the CIXs (which indicate the global contribution of a given CVS) of different CVSs can be calculated, by the use of Eq. (1). The results are listed in Table 3.

To perform clustering based on the proposed WFKM algorithm, some parameters need to be identi<sup>fi</sup>ed. As shown in Table 4, m is the number of membership functions in the WFKM, and it controls the degree of overlapping between two clusters (in other words, m is the smoothing parameter which controls the fuzziness of the clusters). Guided by [22], this paper sets m = 2 to achieve the optimal results; $\beta$ is a parameter for attribute weight ω, and it is required to be greater than 1 [20]. To simplify the calculation in Eq. (11), β is set to be 2; M and α are the termination parameters of Algorithm 1. Considering the computation ef<sup>fi</sup>ciency, M is set to be 1000 and α is set to be 0.00005; for parameter r, according to Algorithm 1, in order to <sup>fi</sup>nd the cluster centroid, n and n sample points are chosen from $\mathbf { 0 _ { i } }$ to be the training dataset and testing dataset, respectively, and usually $n _ { r } = r \times \mathbf { Q } _ { \mathbf { i } }$ bb n. As indicated in Fig. 4, when r is set to be 5%, 10%, 20%, or 30%, with the iterations increases, the objective functions taking different r values all converge to a stable value (when the number of iterations is N5). Thus, this work randomly selects 20% to be the value of r.

![](/api/attachments/CDCDXX55/fulltext/images/bd0fc7713e989b31b76b662c477a9af1cee8e58c56cfc459e2f97ece7d885665.jpg)  
Fig. 3. The relationship between v and dimensionality.

Table 2  
Attribute weights.

<table><tr><td>Attributes</td><td>Category sales frequency (F)</td><td>Category sales volume (N)</td><td>Category sales revenue (S)</td><td>Category gross profit (R)</td><td>Category growth rate (G)</td></tr><tr><td>Weights</td><td>0.2022</td><td>0.1834</td><td>0.1870</td><td>0.2137</td><td>0.2137</td></tr></table>

For clustering analysis, it is crucial to select the number of clusters — K. In the literature, three measures, namely partition coef<sup>fi</sup>cient [4], fuzzy entropy [29] and XB coef<sup>fi</sup>cient [49] are often employed to assess the clustering performance. For the partition coef<sup>fi</sup>cient, a greater index value indicates better performance, while for the XB coef<sup>fi</sup>cient and fuzzy entropy, a smaller index value indicates better performance. In this work, based on the collected dataset, these three indexes are calculated by using different K values, respectively. The obtained results are depicted in Fig. 5. With the increase of K, the index value of the partition coef<sup>fi</sup>cient gradually decreases; the index value of fuzzy entropy increases at the beginning, reaches the peak index value when $K = 3 ,$ , and then slowly decreases; the index value of the XB coef<sup>fi</sup>cient has a downward trend when K is ∈[2,4], and then tends to become stable when $K { \mathrm { ~ i s } } \in ( 4 , 1 0 ] .$ . In addition, the CM manager of PetroChina pointed out that it is quite expensive and challenging to handle and especially implement a large number of different marketing strategies (which re<sup>fl</sup>ect different market clusters) concurrently. Guided by Fig. 5 and CM expertise, although the overall effectiveness of K=4 and K=9 are comparable, K=4 is chosen in an effort to achieve optimal clustering results.

## 4.2.2. Results

In this work, 100 trials are carried out to clustering the CVSs and each of which uses the same initial cluster centroids (38, 1, 4, and 10) that are selected by using a data density based algorithm [32]. To report the best results, only the clustering results of the trial which achieves the minimal XB coef<sup>fi</sup>cient are listed in Table 5. In this trial, the clustering parameters that are reported in Table 4, the selected K value, and four optimal selected initial cluster centroids are used to derive such results. The CVSs are grouped into four market segments (Chuster , Chuster , Chuster , and Chuster ). For each cluster, the distribution of included CVSs in different regions is summarised in Table 6.

Table 3 CIXs of different CVSs.

<table><tr><td>CVS no.</td><td>Category 1</td><td>Category 2</td><td>Category 3</td><td>...</td><td>Category 20</td></tr><tr><td>1</td><td>0.3895</td><td>0.5226</td><td>0.4591</td><td>...</td><td>0.6574</td></tr><tr><td>2</td><td>0.3129</td><td>0.5377</td><td>0.4729</td><td>...</td><td>0.7216</td></tr><tr><td>3</td><td>0.3447</td><td>0.5383</td><td>0.4844</td><td>...</td><td>0.7256</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td>75</td><td>0.3059</td><td>0.3658</td><td>0.3356</td><td>...</td><td>0.4094</td></tr></table>

Clustering parameters.

<table><tr><td>Maximum # of iterations (M)</td><td># of memberships (m)</td><td>Attribute weight (β)</td><td>Threshold (α)</td><td>Threshold of initial cluster centre optimisation</td><td>Cluster centres to selected parameters (r)</td></tr><tr><td>1000</td><td>2</td><td>2</td><td>0.00005</td><td>0.1</td><td>20%</td></tr></table>

![](/api/attachments/CDCDXX55/fulltext/images/35a63b0dab28f873fbbd3a9e4c478d03e44c6fda510d82c1d3ed0d699fe69438.jpg)  
Fig. 4. The relationship between objective function values and r

![](/api/attachments/CDCDXX55/fulltext/images/e64c4165c5f038c918ab121d77492301bd7b4309a536b1a0a24b2cad978fe828.jpg)  
Fig. 5. Indicators of effectiveness.

In this work, each category is assigned a CR according to its CIX in the corresponding cluster. As mentioned in Section 2.1, the destination category holds 5%–10% of categories in a store, the routine category holds 50%–70% of categories, the occasional/seasonal category takes 10%–15%, and the convenience category takes 10%–15% of categories. As a result, 2 out of 20 (10%) categories are identi<sup>fi</sup>ed as the destination category, 12 categories (60%) are considered as the routine category, 3 categories (15%) are the occasional/seasonal category, and 3 categories (15%) are de<sup>fi</sup>ned as the convenience category. The detailed results, including CIX, category ranking, and CRs are listed in Table 8.

For Chuster , most CVSs are distributed in the middle and west areas of Guangdong province. Also, most of them are located on a motorway. In terms of CIX, this cluster has the second highest average CIX (0.3780), such that it plays a relatively important role in the CVS chain market.

Table 6  
Distribution of CVSs in each cluster.

<table><tr><td rowspan="2">Cluster</td><td rowspan="2"># of CVSs</td><td colspan="3">Geographic area (Guangdong, China)</td><td colspan="2">Price region</td></tr><tr><td>East</td><td>Middle</td><td>West</td><td>City centre</td><td>Motorway</td></tr><tr><td> $\text{Cluster}_1$ </td><td>23</td><td>8.7%</td><td>52.2%</td><td>39.1%</td><td>13.0%</td><td>87.0%</td></tr><tr><td> $\text{Cluster}_2$ </td><td>8</td><td>0.0%</td><td>87.5%</td><td>12.5%</td><td>37.5%</td><td>62.5%</td></tr><tr><td> $\text{Cluster}_3$ </td><td>23</td><td>52.2%</td><td>39.1%</td><td>8.7%</td><td>4.3%</td><td>95.7%</td></tr><tr><td> $\text{Cluster}_4$ </td><td>21</td><td>33.3%</td><td>57.1%</td><td>9.5%</td><td>9.5%</td><td>90.5%</td></tr></table>

For Chuster<sub>2</sub>, although it only consists of 8 CVSs, it achieves the highest average CIX (0.4579). This indicates that this type of CVS outperforms other CVSs in the market. Geographically speaking, 7 out of 8 CVSs are located in the middle of Guangdong province, an economically developed area. This is one possible reason for their good performance. Unlike the other three clusters, the Tobacco category appears in the destination category. Hence, the consumers may include more smokers than in other clusters. Further investigations on smoking consumers may help this segment to develop valuable marketing strategies.

For Chuster , only one store is located in a city centre, while over half of the CVSs are located in the east area of Guangdong. The average CIX (0.3514) ranks in the third place, with the performance not being as good as Chuster and Chuster . It is interesting to observe that the Household goods category that normally appears in the routine category jumps to the seasonal category in this cluster.

For Chuster , most of the CVSs are located on motorways, and the majority of CVSs is located in the middle and east of Guangdong province. This cluster performs the worst in the market, as it has the lowest average CIX (0.3364).

In summary, the destination category achieves a high level of consistency in this study. With the exception of Chuster , the destination category consists of Drinks and Sweets categories. The routine category mainly contains ready-to-eat categories (e.g., Sweets, Crisps/snacks, Biscuits, Milk, and Hot meals). This indicates the clustering results are meaningful, since the derived CR accurately re<sup>fl</sup>ects the reality. Such categories consist of routine products in daily life. Moreover, the routine category highlights the distinguished convenience strength of CVS chains. In the seasonal category, the included categories are quite diverse and none of the market segments consist of identical categories. The convenience category mainly contains Newspaper/magazine and Ice cream, and once again reveals the reliability of the proposed clustering algorithm. As it is well-known that categories such as Newspaper/ magazine and Ice cream are low-pro<sup>fi</sup>t product, but are essential to consumers.

## 5. Discussion

This section discusses and analyses the obtained clustering results. First, the newly proposed WFKM clustering algorithm is compared against the original fuzzy K-means algorithm. Second, the performance of the CR model is evaluated via a comparison with the traditional RFM model by employing the new WFKM algorithm in both models. Third, the CR model segments the market from a new CIX perspective, revealing derived market segments that are different from the ones obtained by using traditional segmentation attributes (i.e., geographical areas and price regions). These differences are summarised in Section 5.2. Based on the clustering results, some market strategies and tactics, including pricing, promotions, shelf space allocation and category-speci<sup>fi</sup>c strategies, are suggested in the remaining part of this section.

Table 5  
Clustering results.

<table><tr><td>Cluster</td><td>Cluster centroid</td><td>CVSs of each cluster</td><td>CVSs # of each cluster</td><td>Ratio of each cluster</td><td>Partition coefficient</td><td>Fuzzy entropy</td><td>XB coefficient</td></tr><tr><td> $Cluster_1$ </td><td>38</td><td>5, 6, 7, 9, 11, 16, 17, 27, 28, 29, 33, 37, 38, 39, 40, 44, 45, 46, 54, 55, 68, 71, 74</td><td>23</td><td>30.7%</td><td>0.3626</td><td>0.3100</td><td>0.4029</td></tr><tr><td> $Cluster_2$ </td><td>1</td><td>1, 2, 3, 14, 15, 18, 19, 57</td><td>8</td><td>10.6%</td><td></td><td></td><td></td></tr><tr><td> $Cluster_3$ </td><td>25</td><td>4, 10, 12, 13, 20, 23, 24, 25, 31, 35, 41, 47, 49, 52, 59, 60, 61, 62, 63, 64, 65, 73, 75</td><td>23</td><td>30.7%</td><td></td><td></td><td></td></tr><tr><td> $Cluster_4$ </td><td>8</td><td>8, 21, 22, 26, 30, 32, 34, 36, 42, 43, 48, 50, 51, 53, 56, 58, 66, 67, 69, 70, 72</td><td>21</td><td>28.0%</td><td></td><td></td><td></td></tr></table>

## 5.1. Model evaluation

5.1.1. Comparison between WFKM and unweighted clustering algorithm

Three measures, partition coef<sup>fi</sup>cient, fuzzy entropy, and XB coef<sup>fi</sup>cient are used throughout this paper to assess the clustering performance. In this section, the clustering results obtained from WFKM and unweighted FKM algorithms are reported in Table 7. In WFKM, each category is dynamically assigned a weight according to its category attributes, whereas the unweighted FKM treats all attributes as equally important. As aforementioned in Section 4.2.1, for the partition coef<sup>fi</sup>cient, the greater index value indicates better performance, while for the XB coef<sup>fi</sup>cient and fuzzy entropy, the smaller index value indicates better performance. Therefore, Table 7 shows that the newly proposed WFKM algorithm outperforms the unweighted FKM algorithm in all three measures.

## 5.1.2. The comparison between the CR model and the RFM model

The proposed CR model is compared with the traditional RFM model and the obtained results are discussed in this subsection. The aim of this work is to cluster CVSs. However, this is a very new topic, and there is no existing clustering model that can be directly employed herein for comparison purposes. The conventional RFM model is usually used to group consumers, the recency (R), frequency (F), and monetary (M) attributes are measured from a customer purchase point of view. However, in principle, RFM model is a purchase-behaviour based segmentation model [39,44]. To some extent, the purchase-behaviour can also be re<sup>fl</sup>ected by the product movements in a CVS. In this work, the conventional RFM model is adjusted from a consumer purchase point of view to a CVS product movement point of view. As mentioned in Section 2.2.1, there exist some challenges to apply the traditional recency, frequency, and monetary measures of the RFM model to CVS market segmentation. In practice, there are a variety of ways of utilising the recency, frequency, and monetary measures, so that RFM analysis can have different meanings to different people [37]. In this work, the R, F and M represent the recency, frequency and monetary, respectively, of a given category in a CVS. These attributes are the key metrics to evaluate the CVS performance. The CVSs can be grouped according to their performances, so that the RFM model is employed in this work to cluster CVSs.

Based on a revised RFM model [36], and jointly considers the features of CVS segmentation at hand and the available data, this work initially selects the following attributes:

• Re : the time difference between the last purchase timestamp and the current timestamp of a given category i. This attribute re<sup>fl</sup>ects the recency in the RFM model.

• $F _ { i } \mathbf { : }$ the average sales frequency of a given category i. This attribute re<sup>fl</sup>ects the frequency in the RFM model.

• N : the average sales volume of a given category i. This attribute re<sup>fl</sup>ects the monetary in the RFM model.

Table 7 WFKM and unweighted FKM algorithm comparison.

<table><tr><td></td><td>WFKM</td><td>Unweighted FKM</td></tr><tr><td>Partition coefficient</td><td>0.3626</td><td>0.3131</td></tr><tr><td>Fuzzy entropy</td><td>0.3100</td><td>0.3226</td></tr><tr><td>XB coefficient</td><td>0.4029</td><td>0.5152</td></tr></table>

• $R _ { i } \mathrm { : }$ the average gross pro<sup>fi</sup>t of a given category i. This attribute re<sup>fl</sup>ects the monetary in the RFM model.

However, in the available dataset, the category transaction data is recorded on a daily basis, and a category/sub-category consists of a number of products. This results in that almost every category has transaction data every day, hence the Re becomes the same for all categories. For computation ef<sup>fi</sup>ciency, the $R e _ { i }$ is removed from the RFM model. Similar to the CR model, the entropy method is used to determine attribute weights, and the same WFKM clustering algorithm is employed to segment the market. In addition, for comparison purposes, the number of clusters, K, is set to be 4.

The obtained results are shown in Table 9, two models derive the same cluster centroid in Chustser and Chuster . More speci<sup>fi</sup>cally, the partition coef<sup>fi</sup>cient, fuzzy entropy, and XB coef<sup>fi</sup>cients in Table 9 are calculated as follows:

The partition coef<sup>fi</sup>cient evaluates the degree of overlapping between two clusters, given a cluster number c, and a fuzzy partition matrix U, the partition coef<sup>fi</sup>cient is de<sup>fi</sup>ned as:

$$
V _ {P C} (U, c) = \frac {1}{n} \sum_ {i = 1} ^ {c} \sum_ {j = 1} ^ {n} \mu_ {i j} ^ {2}\tag{19}
$$

where $\mu _ { i j }$ indicates the membership degree of CVS j belonging to Chuster , and it can be calculated by the use of Eq. (10), and n is the number of CVSs. In this work, $c = 4$ and $n = 7 5$

For fuzzy entropy, the partition coef<sup>fi</sup>cient is de<sup>fi</sup>ned as:

$$
V _ {P E} (U, c) = - \frac {1}{n} \sum_ {i = 1} ^ {c} \sum_ {j = 1} ^ {n} \mu_ {i j} ^ {2} \ln \mu_ {i j}\tag{20}
$$

where $\mu _ { i j } { , } C$ and n are de<sup>fi</sup>ned in the same manner as that in $V _ { P C }$ . Although the partition coef<sup>fi</sup>cient and fuzzy entropy assess some aspects of clustering performance, they both lack a direct correlation with the structural characteristics of the dataset in use. Therefore, Xie and Beni [49] proposed an XB coef<sup>fi</sup>cient that considers the geometry characteristics of the dataset. The XB coefficient can be defined as follows:

$$
V _ {X B} (U, V, c) = \frac {\sum_ {i = 1} ^ {c} \sum_ {j = 1} ^ {n} \mu_ {i j} ^ {m} \left\| v _ {i} - x _ {j} \right\| ^ {2}}{n \times \min _ {i <   = c , k <   = c , i \neq k} \| v _ {i} - v _ {k} \| ^ {2}}.\tag{21}
$$

Apart from the same parameters as the previous two measures, V is the collection of cluster centroids, m is the smoothing parameter that controls the fuzziness of the clusters, $\lvert \lvert v _ { i } - x _ { j } \rvert \rvert ^ { 2 }$ is the HCsim() distance between cluster centroid (CVS i) and a common $\mathrm { C V S } j , \mathrm { i . e . , } \lvert \lvert \nu _ { i } - x _ { j } \rvert \rvert ^ { 2 } =$ $H C s i m ( q ( i ) , s ( j ) ) ; \| v _ { i } - \nu _ { j } \| ^ { 2 }$ is the HCsim() distance between two cluster centroids — CVS i and CVS k, i.e., $| | \nu _ { i } - \nu _ { k } | | ^ { 2 } = H C s i m ( q ( i ) , q ( k ) )$ . The XB coef<sup>fi</sup>cient <sup>fi</sup>nds a balance point between the internal compaction and the external separation.

Table 9 indicates that the XB coef<sup>fi</sup>cient and the fuzzy entropy of the CR model are smaller than that of the RFM model, respectively. In contrast, the partition coef<sup>fi</sup>cient of CR is greater than the partition coef<sup>fi</sup>cient of RFM model. The above results reveal that, compared with the RFM model, the newly proposed CR model outperforms the RFM model as it achieves more accurate and more effective clustering results. In addition, the CR model considers three dimensions (the importance to consumers, retailers and the marketplace). However, this revised RFM only considers the consumer dimension (i.e., average monthly sales frequency and the average monthly sales volume) and the retailer dimension (i.e., average monthly gross pro<sup>fi</sup>t).

Table 8  
The derived CR of categories in different clusters.

<table><tr><td rowspan="2">Ranking</td><td rowspan="2">CR</td><td colspan="2"> $Cluster_1$  (average CIX: 0.3780)</td><td colspan="2"> $Cluster_2$  (average CIX: 0.4579)</td><td colspan="2"> $Cluster_3$  (average CIX: 0.3514)</td><td colspan="2"> $Cluster_4$  (average CIX: 0.3364)</td></tr><tr><td>Category</td><td>CIX</td><td>Category</td><td>CIX</td><td>Category</td><td>CIX</td><td>Category</td><td>CIX</td></tr><tr><td>1</td><td>Destination category(10%)</td><td>Drinks</td><td>0.5124</td><td>Drinks</td><td>0.6687</td><td>Drinks</td><td>0.4852</td><td>Drinks</td><td>0.4419</td></tr><tr><td>2</td><td></td><td>Sweets</td><td>0.4553</td><td>Tobacco</td><td>0.5930</td><td>Sweets</td><td>0.4111</td><td>Sweets</td><td>0.38341</td></tr><tr><td>3</td><td>Routine category (10%-70%)</td><td>Crisps/snacks</td><td>0.4499</td><td>Sweets</td><td>0.5377</td><td>Crisps/snacks</td><td>0.4098</td><td>Crisps/snacks</td><td>0.3823</td></tr><tr><td>4</td><td></td><td>Biscuit</td><td>0.4445</td><td>Crisps/snacks</td><td>0.5306</td><td>Hot meal</td><td>0.3983</td><td>Hot meal</td><td>0.3718</td></tr><tr><td>5</td><td></td><td>Hot meal</td><td>0.4194</td><td>Biscuit</td><td>0.5229</td><td>Biscuit</td><td>0.3981</td><td>Biscuit</td><td>0.3680</td></tr><tr><td>6</td><td></td><td>Milk</td><td>0.4152</td><td>Hot meal</td><td>0.5072</td><td>Milk</td><td>0.3839</td><td>Stationery</td><td>0.3607</td></tr><tr><td>7</td><td></td><td>Tobacco</td><td>0.4068</td><td>Milk</td><td>0.5022</td><td>Engine oil</td><td>0.3816</td><td>Milk</td><td>0.3533</td></tr><tr><td>8</td><td></td><td>Engine oil</td><td>0.3920</td><td>Household good</td><td>0.4883</td><td>Stationery</td><td>0.3472</td><td>Engine oil</td><td>0.3483</td></tr><tr><td>9</td><td></td><td>Household good</td><td>0.3808</td><td>Health &amp; beauty</td><td>0.4777</td><td>Bread</td><td>0.3387</td><td>Health &amp; beauty</td><td>0.3203</td></tr><tr><td>10</td><td></td><td>Stationery</td><td>0.3694</td><td>Bread</td><td>0.4725</td><td>Tobacco</td><td>0.3354</td><td>Bread</td><td>0.3196</td></tr><tr><td>11</td><td></td><td>Health &amp; beauty</td><td>0.3681</td><td>Engine oil</td><td>0.4699</td><td>Auto supplies</td><td>0.3315</td><td>Auto supplies</td><td>0.3158</td></tr><tr><td>12</td><td></td><td>Bread</td><td>0.3634</td><td>Fruits</td><td>0.4400</td><td>Health &amp; beauty</td><td>0.3276</td><td>Tobacco</td><td>0.3132</td></tr><tr><td>13</td><td></td><td>Fruits</td><td>0.3460</td><td>Stationery</td><td>0.4300</td><td>Wine</td><td>0.3207</td><td>Fruits</td><td>0.3128</td></tr><tr><td>14</td><td></td><td>Auto supplies</td><td>0.3317</td><td>Auto supplies</td><td>0.4277</td><td>Fruits</td><td>0.3170</td><td>Pharmacy</td><td>0.3100</td></tr><tr><td>15</td><td>Seasonal category (70%-85%)</td><td>Pharmacy</td><td>0.3297</td><td>Wine</td><td>0.3876</td><td>Household good</td><td>0.3163</td><td>Wine</td><td>0.3085</td></tr><tr><td>16</td><td></td><td>Wine</td><td>0.3286</td><td>Family planning</td><td>0.3476</td><td>Pharmacy</td><td>0.3096</td><td>Family planning</td><td>0.3075</td></tr><tr><td>17</td><td></td><td>Toy/gift</td><td>0.3161</td><td>Pharmacy</td><td>0.3464</td><td>Ice cream</td><td>0.3063</td><td>Toy/gift</td><td>0.3059</td></tr><tr><td>18</td><td>Convenience category (85%-100%)</td><td>Family planning</td><td>0.3140</td><td>Ice cream</td><td>0.3438</td><td>Family planning</td><td>0.3059</td><td>Ice cream</td><td>0.3059</td></tr><tr><td>19</td><td></td><td>Newspaper/magazine</td><td>0.3096</td><td>Newspaper/magazine</td><td>0.3361</td><td>Toy/gift</td><td>0.3059</td><td>Household good</td><td>0.3006</td></tr><tr><td>20</td><td></td><td>Ice cream</td><td>0.3068</td><td>Toy/gift</td><td>0.3277</td><td>Newspaper/magazine</td><td>0.2984</td><td>Newspaper/magazine</td><td>0.2987</td></tr></table>

## 5.2. Segmentation comparison

Given the problem at hand, the market segmentation method which is currently used by PetroChina segments the market either by the CVSs' geographic area (i.e., east, middle and west areas of Guangdong province) or their price region (i.e., city centre or motorway). For example, when considering the geographic area, if one market segment is grouped into east area of Guangdong, then naturally all CVSs in this cluster should be located in east Guangdong. Similarly, when considering price region, CVSs are only grouped into either the city centre cluster or the motorway cluster.

However, the clustering results obtained from the newly proposed CR model are quite different from the existing ones. For each cluster, the distributions of CVSs included in different regions are summarised in Table 6. Since the new model is based on CIXs, the CVSs in one cluster have similar CIX performance, but they can be distributed in different geographic areas and price regions. For example, not all CVSs in Chuster are located on a motorway, 13% of them are located in a city centre. Therefore, category strategy should be ideally designed according to individual CVS cluster performance, rather than using simple geographic/price attributes.

## 5.3. CR-based category strategy

As aforementioned in Section 4.2.2, each category is assigned a CR with respect to their CIXs in the corresponding cluster. Due to their different CRs, customised category strategies should be applied accordingly. For example, in general, the destination category is used to build store image and attract consumers. In this work, the Drinks category appears in the destination category in all clusters and the Sweets category appears in the destination category in Chuster ,

Chuster , and Chuster . These two categories contribute most towards the store performance. It is natural to pay more attentions to these sub-categories and provide a wider variety of products for consumers to choose. Also, frequent and diverse promotional offers on these categories are necessary to gain more pro<sup>fi</sup>ts for CVSs. In terms of shelf space allocation, normally a <sup>fi</sup>xed and suf<sup>fi</sup>cient place needs to be provided to each destination category. For Chuster , the Tobacco category appears in the destination category, which is quite different from other market segments. To better satisfy consumers' needs in Chuster , other data mining techniques (e.g., rule association mining) can be employed to identify other popular products that are associated with Tobacco. This may require adjustment of shelf space allocation.

For the same category, CRs may play different roles in different market segments. To provide a more effective market strategy, it is important to analyse their CRs under different circumstances. For example, the Household goods category is de<sup>fi</sup>ned as a routine category in Chuster and Chuster , while it appears in the seasonal category in Chuster and the convenience category in Chuster . Due to their different CRs, different category strategies for the Household goods category are provided in Fig. 6.

## 5.4. Category tactics

For the obtained four market segments, to grab more market opportunities, it is necessary to establish an effective tactic. The <sup>fi</sup>rst step is to analyse the features of each cluster. Regarding the average CIX, Chuster N Chuster N Chuster N Chuster . According to Table 6, CVSs in Chuster are mainly distributed in the central region of Guangdong province where the economic development is higher than the rest part of this province; and the majority of CVSs in Chuster is located on the motorway. By analysing products' average price trends (as

## Table 9

CR and RFM model comparison.

<table><tr><td rowspan="2">Cluster</td><td colspan="4">CR model</td><td colspan="4">RFM model</td></tr><tr><td> $Cluster_1$ </td><td> $Cluster_2$ </td><td> $Cluster_3$ </td><td> $Cluster_4$ </td><td> $Cluster_1$ </td><td> $Cluster_2$ </td><td> $Cluster_3$ </td><td> $Cluster_4$ </td></tr><tr><td>Cluster centroid</td><td>38</td><td>1</td><td>25</td><td>53</td><td>6</td><td>1</td><td>25</td><td>37</td></tr><tr><td>Average membership</td><td>0.2855</td><td>0.6212</td><td>0.2956</td><td>0.3413</td><td>0.3766</td><td>0.5120</td><td>0.3378</td><td>0.3173</td></tr><tr><td>The partition coefficient</td><td>0.3626</td><td></td><td></td><td></td><td>0.3596</td><td></td><td></td><td></td></tr><tr><td>The fuzzy entropy</td><td>0.3100</td><td></td><td></td><td></td><td>0.3107</td><td></td><td></td><td></td></tr><tr><td>The XB-coefficient</td><td>0.4029</td><td></td><td></td><td></td><td>0.4555</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/CDCDXX55/fulltext/images/985e23294a0a416632e5fec30b564d9742c4fb437e3685555d246e9a8a370f8b.jpg)  
Fig. 6. Category roles and category strategies.

shown in Fig. 7), Chuster charges a relatively higher average price on products than other clusters, while Chuster charges the lowest average price. Meanwhile, compared with Chuster and Chuster , the price trends of Chuster and Chuster tend to be relatively stable. Based on the above features of each cluster, an effective tactic is identi<sup>fi</sup>ed below:

• Though Chuster performs best amongst all market segments, when it comes to the number of CVSs, this cluster only contains 8 stores, which is much less than other clusters. Hence, one suggestion is to set up more CVSs in Chuster to attract more consumers and gain more pro<sup>fi</sup>ts. Furthermore, as illustrated in Fig. 8, compared with other clusters, Chuster achieves better sales volume, sales revenue, and sales gross compared with other clusters in the mid-price products. Therefore, it is suggested that Chuster should pay more attentions to mid-price products, and provide more mid-price products to meet its consumers' needs.

• One possible reason for the higher average price in Chuster is that the majority of its CVSs (95.7%) is located on motorways. The current marketing strategy suggests that consumers of motorway CVSs are less sensitive to product price. The motorway CVSs often attract consumers who are travelling and they visit the store by chance. For such consumers, they are very mobile and have relatively less loyalty to stores. Therefore, the charged price is normally higher than those stores in a city centre. However, the results obtained in this work mildly contradict this assumption, since the average CIX of Chuster only ranks in the third place. This is because today's travellers are aware that motorway CVSs may charge higher prices than supermarkets, so they often prepare their drinks, sweets, and other essentials in advance. Meanwhile, Fig. 8 shows that Chuster gains the highest percentage of sales revenue (around 65%), but the lowest sales volume (around 11%) in high-price products. Since revenue = price × volume, this implies that the price of high-price products in Chuster is higher than that in other clusters. The current strategy for Chuster may need to be revised, possibly by reducing the price of high-price products.

![](/api/attachments/CDCDXX55/fulltext/images/dd601ed6a40d14730acea30cc6f329db30b4b8e7089ac3317cb2de4f4d78991b.jpg)  
Fig. 7. Price trends of four market segments during January–June, 2009.

• The price trends of Chuster and Chuster tend to be relatively stable. This indicates that the proposed prices are less sensitive to the time series. This is especially true for Chuster , as its current performance is the worst in the market. Furthermore, it is important to take the price sensitivity into account when adjusting prices. For example, since Chuster performs best in terms of CIX, for those CVSs distributed in the same geographic area and price region, the current pricing strategy used by the CVSs in Chuster can be jointly considered to revise the price of such CVSs in Chuster . Moreover, with an attempt to obtain a better price strategy, a more systematical approach can be developed to analyse the price sensitivity in different time periods. Additionally, when it comes to low-price products, as shown in Fig. 8, the overall performance of Chuster and Chuster are better than Chuster and Chuster . Also, the overall performance of Chuster in the high-price products is better than that of the other clusters (it achieves the highest sales volume and gross pro<sup>fi</sup>ts, and the second highest sales revenue). This reveals that low-price products gain more popularity from consumers in Chuster and Chuster , while high-price products are more popular in consumers in Chuster . One suggestion is that high-price products in Chuster and Chuster can be replaced by low-price products. In contrast, Chuster is suggested to provide more high-price products rather than low-price products.

![](/api/attachments/CDCDXX55/fulltext/images/fcfe1c58e3981b7cbed6922aacedddd73e217fcbc5ba583ccd0ea97ae1d967d9.jpg)  
Cluster3

Cluster2  
![](/api/attachments/CDCDXX55/fulltext/images/c7417a03c80b3674db6f5c107b9507b0bcb2e3118d51395275add6a6a20750ca.jpg)

![](/api/attachments/CDCDXX55/fulltext/images/526a63971e7d383629815e4adf768ad792561af166e196a837257c0d16e9cb06.jpg)  
Fig. 8. The sales performance of each cluster.  
Cluster4

## 6. Conclusions

CM techniques form the basis of mature retail management systems, and they help to integrate supply chain and strategic marketing to develop fast consumer reaction systems. Successful CM cases often appear in the cooperation between large manufacturers and supermarkets (e.g., P&G). However, a CVS has the characteristics of being small and scattered, with a limited number of categories and products. Moreover, different types of markets have various kinds of consumers. CVS consumers have diverse needs and they are also mobile. This makes it very dif<sup>fi</sup>cult to employ the mainstream consumer-centric CM methods to analyse and group consumers of CVS chain. To overcome these dif<sup>fi</sup>culties, it is essential to cluster the CVSs, and apply customised CM strategies to each CVS cluster.

Starting from the three dimensions of CR, this work combines the characteristics of the retail market with traditional behaviour-based market segmentation techniques to propose a new CR-based market segmentation model. In particular, an innovative similarity measure (HCsim()) and an improved WFKM clustering algorithm are proposed to group CVSs with similar CIX into the same market segment. The applicability and utility of the proposed clustering model are demonstrated via an empirical study on a CVS chain dataset provided by PetroChina. By using the CR model, the current retail market is divided into four clusters, and they are ranked as $C h u s t e r _ { 2 } > C h u s t e r _ { 1 } > C h u s t e r _ { 3 } > C h u s t e r _ { 4 }$ with respect to their CIXs. For comparison purposes, the new model is compared with the traditional RFM model, with the comparative results revealing that the CR model achieves more stable and more effective clustering results. Another distinguished feature of the new model is that the CR helps to de<sup>fi</sup>ne appropriate marketing strategies for different categories in different market segments.

![](/api/attachments/CDCDXX55/fulltext/images/b46eb9f1fdbf38b09f5d65e095039b2e4a2f492a58a17305108141aeec3fe46c.jpg)

Although the proposed approach is promising, much progress can be made through further research. First, when identifying the CR, the importance of certain categories to competitors also needs to be considered, so that the derived model would better re<sup>fl</sup>ect the reality. Second, to better simulate the changes in consumers demand and purchasing behaviour, time series analysis will be employed to analyse historical sales data. Moreover, to further validate the utility and ef<sup>fi</sup>ciency of the CR model, customers' responses to the newly derived marketing strategies will be collected. This action will take some time, but once such data becomes available, it can be used to build predictive models [7,39].

## Acknowledgement

This work is supported by the National Nature Science Foundation of China (Grant Nos. 70971112, 71301133, 71371159) and Humanity and Social Science Youth Foundation of Ministry of Education, China (Grant No. 13YJC630033). Thanks also go to PetroChina for the donation of the dataset in use.

## References

[1] A.C. Nielsen, J. Karolefski, A. Heller, Consumer-Centric Category Management: How to Increase Pro<sup>fi</sup>ts by Managing Categories Based on Consumer Needs, John Wiley & Sons, Incorporated, 2005.

[2] P.V.S. Balakrishnan, S. Kumar, P. Han, Dual objective segmentation to improve targetability: an evolutionary algorithm approach, Decision Sciences 42 (4) (2011) 831–857.

[3] S. Basuroy, M.K. Mantrala, R.G. Walters, The impact of category management on retailer prices and performance: theory and evidence, Journal of Marketing 65 (4) (2001) 16-32

[4] J.C. Bezdek, Cluster validity with fuzzy sets, Journal of Cybernetics 3 (3) (1973) 58-73

[5] D.S. Boone, M. Roehm, Retail segmentation using arti<sup>fi</sup>cial neural networks, International Journal of Research in Marketing 19 (3) (2002) 287–301.

[6] N. Borin, P.W. Farris, J.R. Freeland, A model for determining retail product category assortment and shelf space allocation, Decision Sciences 25 (3) (1994) 359–384.

[7] J.R. Bult, T. Wansbeek, Optimal selection for direct mail, Marketing Science 14 (4) (1995) 378–394.

[8] P.-C. Chang, C.-H. Liu, Y.-W. Wang, A hybrid model by clustering and evolving fuzzy rules for sales decision supports in printed circuit board industry, Decision Support Systems 42 (3) (2006) 1254–1269.

[9] R.M.C.R. de Souza, F. de A.T. de Carvalho, Clustering of interval data based on city block distances, Pattern Recognition Letters 25 (3) (2004) 353–365.

[10] D.M. Desrochers, P. Nelson, Adding consumer behaviour insights to category management: improving item placement decisions, Journal of Retailing 82 (4) (2006) 357–365.

[11] S.K. Dhar, S.J. Hoch, N. Kumar, Effective category management depends on the role of the category, Journal of Retailing 77 (2) (2001) 165–184.

[12] G.R. Dowling, D.F. Midgley, Identifying the coarse and <sup>fi</sup>ne structures of market segments, Decision Sciences 19 (4) (1988) 830–847.

[13] R.J. Durrant, A. Kabán, When is ‘nearest neighbour’ meaningful: a converse theorem and implications, Journal of Complexity 25 (4) (2009) 385–397.

[14] C. Dussart, Category management: strengths, limits and developments, European Management Journal 16 (1) (1998) 50–62.

[15] B. Fan, P. Zhang, Spatially enabled customer segmentation using a data classi<sup>fi</sup>cation method with uncertain predicates, Decision Support Systems 47 (4) (2009) 343-353.

[16] R.E. Frank, C.E. Strain, A segmentation research design using consumer panel data, Journal of Marketing Research 9 (4) (1972) 385–390.

[17] P.E. Green, A new approach to market segmentation, Business Horizons 20 (1) (1977) 61–73.

[18] N.P. Group, R. Struse, D. Lonsdale, P. Payack, J. Costello, Category Management: Positioning Your Organization to Win, Nielsen Research Management, 1992.

[19] N.-C. Hsieh, An integrated data mining and behavioral scoring model for analyzing bank customers, Expert Systems with Applications 27 (4) (2004) 623–633.

[20] J. Huang, M. Ng, H. Rong, Z. Li, Automated variable weighting in k-means type clustering, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (5) (2005) 657–668.

[21] A.H. Hübner, H. Kuhn, Retail category management: state-of-the-art review of quantitative research and software applications in assortment and shelf space management, Omega 40 (2) (2012) 199–209.

[22] B. JC, A physical interpretation of fuzzy ISODATA, IEEE Transactions on Systems, Man, and Cybernetics SMC-6 (5) (1976) 387–389.

[23] J.J. Jiang, G. Klein, R.A. Pick, A marketing category management system: a decision support system using scanner data, Decision Support Systems 23 (3) (1998) 259–271.

[24] J.J. Jiang, M. Zhong, G. Klein, H.G. Chen, Nonstationary brand variables in category management: a cointegration perspective, Decision Sciences 35 (1) (2004) 101–128.

[25] J.-J. Jonker, N. Piersma, D.V. den Poel, Joint optimization of customer segmentation and marketing policy to maximize long-term pro<sup>fi</sup>tability, Expert Systems with Applications 27 (2) (2004) 159–168

[26] W.A.K.W. Kang, Chain-wide and store-level analysis for cross-category management, Journal of Retailing 83 (2) (2007) 159–170.

[27] M.Y. Kiang, M.Y. Hu, D.M. Fisher, An extended self-organizing map network for market segmentation — a telecommunication example, Decision Support Systems 42 (1) (2006) 36–47.

[28] K.-j. Kim, H. Ahn, A recommender system using ga k-means clustering in an online shopping market, Expert Systems with Applications 34 (2) (2008) 1200–1209.

[29] B. Kosko, Fuzzy entropy and conditioning, Information Sciences 40 (2) (1986) 165–174.

[30] R. Kuo, K. Akbaria, B. Subroto, Application of particle swarm optimization and perceptual map to tourist market segmentation, Expert Systems with Applications 39 (10) (2012) 8726–8735.

[31] A.R. Linnemann, M. Benner, R. Verkerk, M.A. van Boekel, Consumer-driven food product development, Trends in Food Science & Technology 17 (4) (2006) 184–190.

[32] Q. Liu, M. Deng, Y. Shi, J. Wang, A density-based spatial clustering algorithm considering both spatial proximity and attribute similarity, Computers & Geosciences 46 (2012) 296–309.

[33] Y. Liu, M. Kiang, M. Brusco, A uni<sup>fi</sup>ed framework for market segmentation and its applications, Expert Systems with Applications 39 (11) (2012) 10292–10302.

[34] Y. Liu, S. Ram, R.F. Lusch, M. Brusco, Multicriterion market segmentation: a new model, implementation, and evaluation, Marketing Science 29 (5) (Sep. 2010) 880–894.

[35] L.S. Lockshin, A.L. Spawton, G. Macintosh, Using product, brand and purchasing involvement for retail segmentation, Journal of Retailing and Consumer Services 4 (3) (1997) 171–183.

[36] C. Marcus, A practical yet meaningful approach to customer segmentation, Journal of Consumer Marketing 15 (5) (1988) 494–504.

[37] J.A. McCarty, M. Hastak, Segmentation approaches in data-mining: a comparison of RFM, CHAID, and logistic regression, Journal of Business Research 60 (6) (2007) 656-662

[38] N.A. Morgan, A. Kaleka, R.A. Gooner, Focal supplier opportunism in supermarket retailer category management, Journal of Operations Management 25 (2) (2007) 512–527.

[39] D.L. Olson, B. Chae, Direct marketing decision support through predictive customer response modeling, Decision Support Systems 54 (1) (2012) 443–451.

[40] Óscar González-Benito, M.P. Martínez-Ruiz, A. Mollá-Descals, Retail pricing decisions and product category competitive structure, Decision Support Systems 49 (1) (2010) 110–119.

[41] C.E. Shannon, A mathematical theory of communication, The Bell System Technical Journal 27 (1948) 379–423.

[42] W.R. Smith, Product differentiation and market segmentation as alternative marketing strategies, The Journal of Marketing 21 (1) (1956) 3–8.

[43] M. Trivedi, Regional and categorical patterns in consumer behavior: revealing trends, Journal of Retailing 87 (1) (2011) 18–30.

[44] C.-Y. Tsai, C.-C. Chiu, A purchase-based market segmentation methodology, Expert Systems with Applications 27 (2) (2004) 265–276.

[45] P.C. Verhoef, B. Donkers, Predicting customer potential value an application in the insurance industry, Decision Support Systems 32 (2) (2001) 189–199.

[46] C.-H. Wang, Outlier identi<sup>fi</sup>cation and market segmentation using kernel-based clustering techniques, Expert Systems with Applications 36 (2) (2009) 3744–3750.

[47] M. Wedel, J. Karolefski, W.A. Kamakura, Market Segmentation: Conceptual and Methodological Foundations, 2nd edition Kluwer Academic Publishers, 2000.

[48] Y. Wind, Issues and advances in segmentation research, JMR, Journal of Marketing Research 15 (3) (1978) 317–337.

[49] X. Xie, G. Beni, A validity measure for fuzzy clustering, IEEE Transactions on Pattern Analysis and Machine Intelligence 13 (8) (1991) 841–847.

[50] H. Yu, J. Yang, A direct LDA algorithm for high-dimensional data — with application to face recognition, Pattern Recognition 34 (10) (2001) 2067–2070.

[51] F.S. Zufryden, New computational results with a dynamic programming approach for product selection and supermarket shelf-space allocation, The Journal of the Operational Research Society 38 (2) (1987) 201–203.

![](/api/attachments/CDCDXX55/fulltext/images/b18f1c33af2a58bce07d7ebdc6514767122e062682114634dee1869bcafb2879.jpg)  
Shuihua Han is a professor of Information System, in the Department of Management Science at Xiamen University. His research interests are in business intelligent, supply chain Management, and RFID technology.

![](/api/attachments/CDCDXX55/fulltext/images/e0e11e179a0cdd540110622f7fdbb5ab412bf7db7c758a1da57a6f8c96b50759.jpg)

Yongjie Ye is a postgraduate student at Xiamen University. He follows Professor Shuihua Han on the research <sup>fi</sup>elds of decision support systems, business intelligence and data mining, and smart health. Ye has a bachelor degree in Information Management and Information System from Nanjing University of Aeronautics and Astronautics

![](/api/attachments/CDCDXX55/fulltext/images/f5bacc57129728047e770bb60c7d5c5f85ae4466f7b6a3bbfd714a1ba7f43eac.jpg)

Xin Fu received her BSc degree (1st class honours.) in Computer Science from the University of Ulster, UK, in 2005; the MPhil degree in Informatics from the University of Manchester, UK, in 2007; and the PhD degree in Computer Science from Aberystwyth University UK in 2010 She worked as a post-doctorate research associate on a collaborative project between the University of Bradford, UK and Syngenta Ltd, UK (based at Syngenta Jealott's Hill International Research Center) from 2010 to 2012. She is now with the School of Management, Xiamen University, China. Her research interests include decision support systems, fuzzy and qualitative modelling, business intelligence, and predictive toxicology.

![](/api/attachments/CDCDXX55/fulltext/images/85dea6e43fe09543c07924117c195171c3f765cd3400f12d503a7faae01407bb.jpg)

Zhilong Chen received the master's degree in Management Science and Engineering at Xiamen University in 2012. He followed Professor Shuihua Han on the research fields of business intelligence and data mining. Chen has a bachelor degree in Information Management from Nanjing Audit University
