---
otero_id: 12752
otero_key: "D55NEYGB"
title: "Detecting the migration of mobile service customers using fuzzy clustering"
authors: "Indranil Bose; Xi Chen"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2014.11.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

## Title: Detecting the Migration of Customers of Mobile Services Using Fuzzy Clustering

Author: Indranil Bose Xi Chen

![](/api/attachments/D55NEYGB/fulltext/images/b3eba00485c3e3b0fda2cae5cf1d4d6de41dcba22d0d2cb1c1226050e7bc9db6.jpg)

PII: S0378-7206(14)00135-9

DOI: http://dx.doi.org/doi:10.1016/j.im.2014.11.001

Reference: INFMAN 2770

To appear in: INFMAN

Received date: 17-5-2014

Revised date: 29-9-2014

Accepted date: 9-11-2014

Please cite this article as: <doi>http://dx.doi.org/10.1016/j.im.2014.11.001</doi>

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Highlights

 We study migratory behavior of mobile services customers using fuzzy clustering.

 We propose an algorithm that studies how customers dynamically move between clusters.

 We discover new usage and revenue patterns for two migratory groups of customers.

# Detecting the Migration of Customers of Mobile Services Using Fuzzy Clustering

Indranil Bose

Indian Institute of Management Calcutta

Dimaond Harbour Road, Joka,

Kolkata 700104, West Bengal, India

Phone: 91-33-2467-8300

E-mail: indranil\_bose@yahoo.com

Xi Chen\*

School of Management

Zhejiang University

866 Yuhangtang Road

Hangzhou, Zhejiang Province 310058

Peoples Republic of China

Phone: 86-571-88206827

E-mail: tigychen@gmail.com

\*Corresponding author

# Detecting the Migration of Customers of Mobile Services Using Fuzzy Clustering

## Abstract

Customer clustering is used to build customer profiles which make up the core of a customer centric information system. In this paper, we develop a method for extending the standard fuzzy c-means clustering algorithm using membership functions to detect how customers move between clusters over time. The study leads to discovery of new usage and revenue patterns of customers, identification of two groups of customers that exhibit migratory behavior over time, and determination of specific usage and revenue attributes that impact customer migration. The findings provide insights to mobile services providers about how to detect temporal changes in customer behavior.

## Keywords:

Clustering; Customer behavior; Migration; Mobile services; Temporal data; Usage patterns.

## 1．Introduction

Mobile technologies have entered the everyday life of people around the world. A report from the IDC group stated that the number of mobile devices accessing the Internet is estimated to reach 1.7 billion by 2017 [23]. However, a hot market also implies fierce competition. The mobile telecommunication industry is characterized by “considerable variability in customer behavior” and low commitment as “30% of the typical cellular providers’ customers exit, either switching providers or discontinuing cellular usage, each year” [10]. The monthly churn rates of AT&T, Verizon Wireless, Sprint Nextel, and T-mobile in 2007 were 1.7%, 1.1%, 2.7%, and 2.6%, respectively [34]. In fact, a 30% reduction in churn rate can effectively increase long-term revenues by 15% [10]. The key to survival in this competitive market lies in knowing customers better, and preventing them from churning.

In the context of e-commerce, customer orientation is also regarded as indispensible for developing successful customer relationship management [42]. Knowledge about customers can give e-commerce companies a competitive edge [32]. Profiling of customers usually involves segmentation which refers to all methods that group customers based on their similarities with respect to some characteristics52. For example, the Austrian mobile services provider Tele.ring performed segmentation to build customer profiles to help them target and position customers, and was able to generate a monthly profit of approximately US\$ 25.20 per customer, while attracting 200,000 new customers from their competitors [36]. Clustering algorithms are popular tools for segmentation and are used for customer profiling [41, 52]. However, clustering was usually performed in a static fashion without consideration of the possible changes in customers’ behavior over time. In contrast, the reality is that customers’ behaviors do change over time. For example, Song et al. discovered changes in customers’ online shopping behavior such as frequency of visits, and number of orders in two consecutive temporal stages [50]. Lee et al. studied the Internet users switching behavior across Internet portal websites based on their browsing record [29]. In e-commerce, customers respond to marketing activities much faster due to two techno-economic forces, micro-consumption enabler and micro-commodity enabler. The first force refers to technologies that can reduce the customers’ effort in online shopping such as online payment services and search engines. The second force takes effect when traditional services or products are further dissected to come up with more specialized products or services that satisfy customers’ needs. Without knowing the changes in customers’ behavior caused by these forces, it is impossible to respond to new situations [20]. A feasible solution is to develop analytical techniques such as dynamic clustering algorithms or programs to discover the dynamics in consumers’ preferences, and then use the analytical results as a basis to adjust market segmentation strategies accordingly and dynamically.

In this paper, we examine two issues in the process of multi-stage clustering: identification of new customer clusters and determination of migration path of customers. The determination of new customer clusters can be used as evidence to set up new market segmentation strategies. However, two practical conditions should be taken into consideration. First, the difference between the old segmentation and the new segmentation should be significant enough. Second, each segment should cover an acceptable portion of the customer population. Violation of these two conditions may make investing resources to create new marketing strategies unworthy. We develop a method that extends the standard fuzzy c-means clustering algorithm for identifying new customer clusters from data over multiple time periods. We determine membership functions for each customer that indicate how likely it is for a customer to belong to a cluster. By analyzing each customer’s change of values of membership functions, we discover changes in individual behavior when monitoring the customers’ migration paths. Our analysis also leads to determination of changes in group behavior through the discovery of new customers’ usage and revenue clusters and determination of the relationship between them. We then provide recommendations to firms on augmenting their marketing strategies in response to changes in customers’ behavior.

This paper provides a discussion of the related literature in the next section and moves on to a description of the research method in the section following that. Next, we describe the experimental results. The concluding section provides discussion of results, identifies limitations of this research, and lists some directions for extending this research in future.

## 2. Related literature

Firms spend a lot of money to acquire new customers, and so they prefer to hold on to existing customers rather than to acquire new customers. It is known that “a 1% improvement in retention can increase firm value by 5%” [26], and at the same time “losing customers not only leads to opportunity costs because of lack of sales revenue, but also adds to the cost of attracting new customers” [3]. On the other hand, it would be more important to predict the value of customers in future than just understand it in its current level because customers’ value changes over time [17]. Some customers dissolve the relationship abruptly, while a number of them make this decision gradually, exhibiting changes in their interactive behavior with the firm. This can take the form of a very active customer who becomes a totally passive customer or “a customer who alternates between active and non-active status” till the relationship is dissolved [30]. Therefore, understanding the temporal behavior could be important. Khan et al. [27] discovered that customization based on consumers’ temporal heterogeneity could be more beneficial than

#

customization based on the differences between customers. Service providers’ actions may also influence customers’ migration. Bansal et al. discovered that interaction between the ‘push’ factors of the current service providers that included satisfaction, trust, and commitment, the ‘pull’ factors of the new service providers luring the customers through better financial or quality related benefits, had a significant impact on the customers’ migratory behavior [5]. A timely detection of this migratory behavior of customers can enable firms to introduce strategies that are able to reduce the defection of such customers. It is worth noticing that in order to study migration, we should observe the whole process of migration. “The time frame of the switching path covers the whole history of the process leading to the switching decision” rather than only the events that immediately preceded switching [46].

## 3. Statistical approaches for studying customer migration

In statistical approaches, the patterns of customers’ behavior are captured with the help of probabilistic models. These models do not consider the change in the customers’ behavior over time and use the same static (i.e., time-invariant) model throughout the time period under consideration. One of the earlier researches in the area of customer migration was that of Dwyer who studied customer migration, and predicted repeat purchase behavior and life time value (LTV) of customers using the knowledge of their recency of purchase [15]. An analytical formula for calculating the LTV of a migrating customer was obtained by Berger and Nasr [7]. A similar approach was adopted by Hwang et al. [22]. These papers studied customer migration as a static process. Pfeifer and Carraway modeled the dynamic nature of customer migration using Markov chains where the different situations representing a customer’s possible relationship with the firm were referred to as states and the chance of migrating from one state to another was represented by transition probabilities [40]. Schweidel et al. proposed a hidden Markov chain based approach for studying the migration of customers’ services usage behavior for multiple services [48].

## 3.1. Clustering for studying customer migration

Clustering is a special class of statistical method that is used for understanding customer behavior. Customer clustering classifies customers into different groups so that special pricing and advertising policies targeted to these groups can be devised to satisfy their needs [44]. In addition to observable shopping behavior clustering, clustering can also be used to discover the differences existed in the attitude and intentions of customers [54]. On the basis of data assignment, two types of clustering techniques can be identified: hard clustering and soft clustering. Hard clustering algorithms assign a class label to each data item so that it is allocated to a single cluster. K-means and self organizing map (SOM) belong to the class of hard clustering algorithms [25]. Soft clustering applies fuzzy logic when doing clustering. Fuzzy logic deals with situations that can be partially true. Usually, a continuous value between 0 and 1 is used to represent the truthfulness of the situation [55]. In the language of clustering, partial truth is represented by the degree of membership that associates each data item with all clusters that are discovered [25]. The changes in the degree of membership can be particularly useful for studying migratory behavior of customers. Hui and Jha suggested that hard clustering techniques such as unsupervised Kohonen network could be used to identify customers that were likely candidates for cross-sell as well as to identify possible fraudulent behavior of customers [21]. Ozer [38] used the fuzzy c-means (FCM) algorithm for customer segmentation in online music services, and showed that the results obtained using the FCM algorithm provided insights about customer’s attitudes, interests, and opinions about the services.

## 3.2. Conceptual frameworks for using clustering to study customer migration

The use of clustering techniques for studying migratory behavior of customers has been limited. In mobile telecommunication services related data, the frequency of update is high because mobile telecommunication users use mobile services anytime and anywhere within a single day. Therefore, it is necessary to use temporal data mining when studying customers’ migratory behavioral patterns for mobile services. Antunes and Oliveira remarked that the purpose of temporal data mining was “to discover hidden relations between sequences and subsequences of events” [2]. The states within each time sequence can be interpreted as customer clusters within a time frame, and the assignment of customers to such clusters.

For business applications, deciding the number of clusters in a multi-stage context with careful consideration of temporal factors is different from that in a single stage context. When clustering customers using behavioral data, each cluster consists of customers with a certain pattern that is represented by the center of the cluster. Marketers design appropriate services according to these patterns. If the differences between new patterns and old patterns are not significant, it is not worth the effort and cost to introduce new services. As a result, when studying customers’ migratory behavior over multiple stages, the marketers usually want to discover new patterns that are significantly different from patterns in the prior stages.

Wedel and Kamakura stated that there were two types of changes in dynamic segmentation of customers: manifest change and latent change [51]. When manifest change occurred, segment membership was stable but the preference structure of customers in a segment changed. When latent change took place, the preference structure did not change but the size of the segment or the membership of the segment changed. Aggarwal et al. compared the results of clustering using data streams from different time frames [1]. They presented the changes in clusters by answering the following questions. Were there new clusters in the data at time $t _ { 2 }$ that were not present at time $t _ { I } ?$ Had some of the original clusters been lost because of changes in the behavior of the stream? Had some of the original clusters at time $t _ { I }$ shifted in position and nature because of changes in the data? These questions gave clear indications about what type of manifest changes to look for during migration of customer clusters, as proposed by Wedel and Kamakura [51]. Appearance of new clusters meant the addition of new preference structures whereas disappearance of old clusters meant the absence of old preference structures. Shifting of original clusters was a special case in which the preference structure changed but the members of the cluster remained the same. On the other hand, latent changes were all about data or members of clusters, such as, the number of members and the membership function of those members.

More recently, Nasraoui et al. used four types of basic profile evolution (namely, birth, death, persistence, and atavism) for discovering the changes in user profiles based on clustering [35]. Schweidel et al. described two possible dynamics of customers that included portfolio inertia and service stickiness [48]. These characteristics showed the customers’ willingness to maintain their current service portfolio and were similar to persistence of preference structures.

## 3.2. Practices of clustering for studying customer migration

Some researchers used a fixed number of clusters for all temporal stages and studied the changes in data patterns in terms of variations of their membership functions for clusters (e.g. [33]). This approach had a limitation that it could not detect new patterns such as increase or decrease in the number of clusters. Chen et al. proposed a framework for detection of concept drifting, identified outliers that were not similar to existing cluster seeds, and split or merged clusters when there was enough number of outliers [13]. In Nasraoui et al., new clusters were compared with old clusters using distance based similarity measures [35]. In another study, once a new web visiting session was generated, it was compared to the existing cluster seeds in terms of distance based similarity measures [49]. If the similarity measure satisfied the specified threshold, the cluster seed was updated. Otherwise, a new cluster was created. Brice et al. proposed a hierarchical clustering based approach for the discovery of evolving clusters in stream data [11]. The common problem encountered by the above approaches was that the changes of clusters were made by only considering the incoming data items and the clusters were influenced by the incoming data. There was no validation of clusters to ensure that the members of a cluster were similar enough whereas members of different clusters were different enough from each other.

Fleder and Padmanabhan proposed an approach for detecting evolution of clusters [16]. Their approach retained clusters from prior stages when studying data in the new stages. They added new clusters only if the new clusters significantly reduced the value of their loss function which was equal to the difference of the sum of the squared errors and the penalties for newly added clusters. The advantage of their approach was that the clusters in different periods could be compared to an identical base. However, their approach used hard clustering techniques that could identify significant changes in behavioral patterns but could not track the gradual process of change or the migration path of customers. Not all customers changed their behavior abruptly. Some of them kept an intermediate status before the final change [31]. Nasraoui et al. explained that tracking the changes in user profiles could enhance the firm’s understanding of the users’ characteristics such as their access patterns and the impact of seasonality on the purchases [35]. In Table 1, we compared the above studies to our approach (explained in subsequent sections). We observed that research on developing methods that study the appearance and disappearance of clusters, track the migration process of customers among clusters, and combine that with cluster validation is currently unavailable, to the best of our knowledge.

[Insert Table 1 about here]

To bridge this research gap, we used a soft clustering method (i.e., FCM) in this paper to study changes in behavioral patterns as well as migratory behavior of customers of mobile services. FCM is chosen because it assigns a degree of membership to any data item that takes a continuous value in the range of 0-1 and it indicates the strength of an item’s membership in a cluster. Monitoring the change in the degree of membership of an item can provide us interesting knowledge about customers’ changing preferences over time. This knowledge is more informative than a discrete ‘yes’ or ‘no’ about whether the item belongs to a cluster, as determined using hard clustering [47]. In the next section, we describe our proposed method by first introducing the standard FCM algorithm and then explaining how we design the extended FCM algorithm from it.

## 4. Research method

## 4.1. Standard FCM algorithm

Suppose C is the number of clusters and N is the number of data vectors. The clustering process of FCM involves minimization of the objective function shown in (1) that represents the total variance of data points around the centers of clusters. FCM clustering minimizes (1) by assigning data vectors $x _ { k }$ to suitable clusters represented by v with appropriate value of $\mu _ { i k }$ . The final results of clustering include matrix U and vector V. U is a C\*N matrix whose (i,k) element is $\mu _ { i k }$ which is the probability that the kth data vector belongs to the ith cluster. V is a vector whose ith element $\nu _ { i }$ is the center of the ith cluster.

$$
J (X; U, V) = \sum_ {i = 1} ^ {C} \sum_ {k = 1} ^ {N} \mu_ {i k} ^ {q} \left\| x _ {k} - v _ {i} \right\| _ {A} ^ {2}\tag{1}
$$

$$
\text { where } \sum_ {i = 1} ^ {C} \mu_ {i k} = 1, \mu_ {i k} \geq 0, 1 \leq k \leq N, q > 1\tag{2}
$$

In (1), q is the fuzzifier and A is the norm inducing matrix. For standard FCM, a common choice of A is I. Minimization of (1) with respect to U and V, subject to constraint (2), leads to the following Lagrange function (3), where $\lambda _ { i }$ are the Lagrange multipliers.

$$
J (X; U, V) = \sum_ {i = 1} ^ {C} \sum_ {k = 1} ^ {N} \mu_ {i k} ^ {q} \left\| x _ {k} - v _ {i} \right\| _ {A} ^ {2} - \sum_ {i = 1} ^ {N} \lambda_ {i} \left(\sum_ {i} ^ {C} \mu_ {i k} - 1\right)\tag{3}
$$

By setting the gradients of $J ( { \boldsymbol { X } } ; { \boldsymbol { U } } , { \boldsymbol { V } } )$ with respect to U, V, and equal to zero, we can obtain the following equations:

$$
\mu_ {i s} = \frac {1}{\sum_ {i = 1} ^ {C} \left(\frac {d \left(x _ {k} , v _ {s}\right)}{d \left(x _ {k} , v _ {i}\right)}\right) ^ {\frac {1}{q - 1}}}\tag{4}
$$

where $d ( x _ { k } , \nu _ { s } ) = \left\| x _ { k } - \nu _ { s } \right\| ^ { 2 }$

(5)

$$
\text { and } \sum_ {k = 1} ^ {N} \mu_ {i k} \frac {\partial d (x _ {k} , v _ {i})}{\partial v _ {i}} = 0, i = 1,..., C\tag{6}
$$

Usually, an iterative procedure is used to obtain estimates of U and V. Thus, clustering using FCM algorithm begins with the initialization of cluster centers and the probabilities $\mu _ { i k }$ and solves equations (4) and (6) at each iteration till the difference between the new estimate and the old estimate is smaller than a given threshold.

## 4.2. Extension to FCM algorithm

Ganti et al. [18] proposed a framework for discovering the differences between two data sets. Their basic idea was to identify the identical part of the two data sets and then to extend the identical part to include differences between the data sets. We adopted this idea in order to extend the standard FCM method. We retained clusters from the preceding stage as the ‘identical part’ and added new clusters as the ‘difference’ between the two stages. Fleder and Padmanabhan [16] proposed an approach for detecting evolution of clusters based on hard clustering techniques. Their approach retained clusters from earlier stages when analyzing data in the recent stages. Their experiments used simulated data to show that the approach was effective in discovering changes in cluster structures.

It is important to retain clusters from prior stages because the calculation of the membership function depends on the centers of clusters that are determined earlier on. If the centers change from one stage to the next, we cannot compare and track the changes in the values of the membership functions. For example, we may define a cluster which is represented by usage of 1 GB of data and 100 minutes of video call each month as ‘active 3G users’. With that labeling, a customer who actually consumes 1.1 GB of data and 96 minutes of video call can be said to belong to this cluster with a high value of the membership function. In a subsequent quarter, if it is observed that the same customer uses 0.8 GB of data and 80 minutes of video calls a month, then a judgment can be made that (s)he is less active now based of the definition of ‘active 3G users’ that we proposed before. However, if the definition of ‘active 3G user’ is now changed to usage of 0.75 GB of data and 75 minutes of video call each month, then we will classify him/her as an active 3G user once again, without understanding the change that has taken place in the customer’s behavior. Thus, in order to discover the changes taking place over time, it is important to retain the same definition for the cluster center in all temporal stages of data analysis. Because we need to retain clusters from prior stages, the standard FCM algorithm needs to be extended. Clustering using FCM algorithm is an iterative process. The centers of clusters are updated in each iteration. The iteration stops when the value of the membership function does not change any more. In the extension to FCM algorithm, the updating is only applied to centers of clusters that are newly added because centers obtained from the prior stages need to be retained. In order to encourage the algorithm to find clusters that are significantly different from existing ones, we initialize new cluster centers that are very far away from existing cluster centers in terms of Euclidean distance.

#

Next, we addressed two issues: how to measure the differences between clusters and how to determine which of the detected changes are significant. To settle the first issue, relative clustering validity indexes are used. After reviewing common validity indexes for fuzzy c-means clustering, we chose Xie and Beni’s index (S) and its extension partition index (SC) [6, 8] for the following reasons. First, SC and S consider both intra-cluster homogeneity and inter-cluster separateness which reflect geometrical properties of data sets. Second, the value of SC and S do not have monotonic tendency which implies that they are not affected by the number of clusters. In experiments conducted by different researchers, SC and S’s ability in guiding clustering algorithms to discover the optimal number of clusters in an unsupervised manner is always above average, especially when the fuzzifier is between 1 and 3 [53]. For example, in Pal and Pezdek’s experiments [39], the overall performance of S is better than PC and PE indexes whereas in Wu and Yang’s experiments [53], the overall performance of S is better than FHV index proposed by Gath and Geva [19]. Considering the fact that S has been tested by many researchers with acceptable and stable performance, it appears to be a safe choice for this research. However, it is known that S can be influenced by the presence of noise in data. SC can overcome the problem of noisy data since the denominator of SC can make the value of SC bigger when extremely small number of data points is present. Finally, both SC and S are relatively more sensitive to outlying data than other indices [53]. This property implies that they are able to identify changes in the data structure better than other indices. With a proper control, such as restriction in the size of the clusters, they are able to exclude noisy data from new clusters. Equations (7) and (8) define these

indexes.

$$
S C = \sum_ {c = 1} ^ {C} \frac {\sum_ {n = 1} ^ {N} (\mu_ {c n}) ^ {q} \left\| x _ {n} - v _ {c} \right\| ^ {2}}{N _ {c} \sum_ {k = 1} ^ {c} \left\| v _ {k} - v _ {c} \right\| ^ {2}}\tag{7}
$$

where $N _ { c }$ is the number of data vectors in the cth cluster and $q$ is the fuzzifier.

$$
S = \frac {\sum_ {c = 1} ^ {C} \sum_ {n = 1} ^ {N} \left(\mu_ {c n}\right) ^ {q} \left\| x _ {n} - v _ {c} \right\| ^ {2}}{N \min _ {\forall c , k} \left\| v _ {k} - v _ {c} \right\| ^ {2}}\tag{8}
$$

where N is the total number of data vectors in the data set. SC and S measure the ratio of intra-cluster compactness or the sum of the squared Euclidean distances between each data item and its cluster center (the numerators of (7) and (8)) and inter-cluster separateness (the denominators of (7) and (8)). The difference between SC and S is that SC uses a total distance based measure whereas S uses a minimum-distance based inter-cluster separateness. Ideally the clusters should have large inter-cluster separateness and small intra-cluster compactness. Thus, smaller values of SC and S imply better cluster structures. Also, since SC and S are ratios, they are not affected by the number of data items.

Adding or deleting new clusters should improve the clusters’ structures significantly and reduce the values of SC and S. Since SC and S tend to decrease with an increase in the number of clusters we follow a two-step procedure for determining the appropriate number of clusters.

1) Suppose the number of new clusters we are trying to add is in the range [0, N]. For each value in this range, we run FCM algorithm to cluster the data and obtain a value of $S C = [ s c _ { 0 } , s c _ { I } , . . . , s c _ { N } ]$

$$
\text { and } S = [ s _ {0}, s _ {1}, \dots , s _ {N} ].
$$

2) We calculate the standard deviation of $[ s c _ { 0 } , s c _ { I } , . . . , s c _ { N } ]$ and $[ s o , s _ { I } , . . . , s _ { N } ]$ and denote them by stdSC and stdS respectively. Then, the original values of SC and S are adjusted using equations (9) and (10).

$$
S C _ {i} ^ {\text { adj }} = s c _ {i} + i * \text { stdSC }, \text { where } i = 0, 1,..., N.\tag{9}
$$

$$
S _ {i} ^ {\text { adj }} = s _ {i} + i * \text { stdS }, \text { where } i = 0, 1,..., N.\tag{10}
$$

The reason for calculating stdSC and stdS is to estimate the extent of change in the values of SC and S when the number of clusters increases. By adjusting the values of SC and S, we can determine the appropriate number of new clusters that can bring reduction in the value of SC that is much larger than the average rate of change. We summarize the extended FCM algorithm for detecting temporal changes in clusters as follows:

1) Decide on the number of temporal stages. Suppose there are T stages. For the first stage, standard FCM algorithm is used and SC and S validity indexes are used for finding the appropriate number of clusters. Suppose the cluster centers obtained are $L _ { I } = [ L _ { I I } , L _ { I 2 } , . . . , L _ { I C } ]$ , and the number of clusters is C.

2) Detect whether there is any disappearance of clusters when data from the new stage is used. Use standard FCM algorithm to cluster data in stage 2. Assign data to a cluster if the value of the membership function related to that cluster is the highest. Count the number of data items in each cluster. If number of data items in a cluster is less than a threshold, claim that the cluster has disappeared. Remove the disappeared cluster centers from $L _ { I }$ to obtain $L _ { 1 } ^ { ' }$

3) From stage 2 to stage $T$

(a) Set a range on the possible number of new clusters i, where $i = 0 , \ I , . . . , N .$ . Use the FCM algorithm while retaining the centers from the last stage $\dot { L _ { T - 1 } }$ as the input and add new clusters for each possible number within the range. For example, if i = 1 and there are five cluster centers in the last stage, the algorithm will add one new cluster center, update it iteratively, and combine it with the previous five cluster centers to separate the data into six clusters. During the clustering process, the old cluster centers remain fixed whereas the newly added cluster centers are updated using the procedure of a standard FCM algorithm.

(b) Calculate the values of SC and S indexes for each possible number of new clusters and also the related adjusted values of SC and S.

(c) Select the number of clusters that results in the lowest value of adjusted SC and S as the appropriate number of new clusters. Cluster the data again and calculate the cluster centers $L _ { T }$ and the size of clusters. Remove clusters whose size is smaller than a threshold.

(d) If this is not the last stage, repeat steps (a) to (c). Otherwise, stop the algorithm.

## (e) Return $L _ { I } , L _ { 2 } , . . . , L _ { T } .$

The key contribution of this extension was the use of the standard FCM algorithm in a dynamic fashion over multiple time periods for determining appearance of new clusters, disappearance of new clusters, and movement of data items from one cluster to another with the help of membership functions and validity indexes.

## 5. Numerical experimentation and results

5.1. Data description and preprocessing

The numerical experiments were conducted using data collected from a mobile telecommunication services provider AAA in Hong Kong. Even since its partnership with a major mobile telecommunication services provider from Europe, AAA has become the leader in this industry in Hong Kong providing voice, multimedia and broadband services in the mobile markets through its full-coverage GSM/3G/HSPA+ network. It is well regarded for its use of customer segmentation and targeting for improving its relationship with its customers. The collected data belonged to the time period September 2004 – August 2005, containing more than 10,000 records. Each of the records in the data set represented a customer who was characterized by more than 200 attributes. The set of attributes was a mixture of numerical and categorical variables. Attributes that had more than 60% missing values and attributes that had only one value were removed as the first step of data preprocessing. It was found that most continuous variables were highly skewed in their distribution and 135 out of 160 continuous variables had a skewness index higher than two. Attributes whose skewness was greater than 150 were discarded. This included, for example, ‘complaint count’ whose skewness was 177 and ‘net access’ whose skewness was 155, among others. To overcome this problem, these variables were transformed using the log function. For all continuous variables, 1% of the top and bottom values were treated as outliers, and the related records were removed from further consideration. After the outliers were eliminated, 9810 records remained. In the raw data, the usage and revenue data were aggregated over last three months, last six months, last nine months, and last 12 months. We divided the one year period into four quarters: September 2004 to November 2004, December 2004 to February 2005, March 2005 to May 2005, and June 2005 to August 2005. We then derived the usage and revenue information from the aggregated data for each quarter. For example, the aggregate usage of last six months minus the aggregate usage of last three months is the usage of the customer in the third quarter. After data preparation and derivation, there were six usage variables and five revenue variables for each quarter as shown in Table 2. For example, the continuous variables were transformed so that they ranged between zero and one. We used the values of the attributes in Q1 as the base to transform the continuous variables using (11) so that attributes in later quarters could be compared to an identical base. In (11), x represented the continuous variables.

$$
x ^ {\prime} = \frac {x - M i n (x \text {   in   } Q _ {1})}{M a x (x \text {   in   } Q _ {1}) - M i n (x \text {   in   } Q _ {1})}\tag{11}
$$

We identified two groups of attributes. The first group was related to the mobile services usage data of customers including International Direct Dial (IDD), roaming, General Packet Radio Service (GPRS), Short Message Service (SMS), Picture Mail (PM), and Personal Handphone Service (PHS or voice calls). The usage information was recorded in minutes of use (MOU) or bytes. The second group of attributes represented the revenue contribution of customers for the services they used including revenue for IDD, roaming, value added services via voice network (VASV), value added services via non voice network (VASNV), and other services. VASV included services such as PHS. VASNV included services such as SMS, GPRS, and PM. The attributes belonging to usage and revenue groups were continuous and they were recorded for the most recent month, second most recent month, third most recent month, total of six recent months, total of nine recent months, and total of twelve recent months. Table 2 provides a description of the attributes that we used. The usage of mobile services is decided by the customers’ preferences whereas the revenue contribution is influenced by the pricing plan adopted by the mobile services providers. We divided the data into usage and revenue groups because usage attributes reflected recency and frequency whereas revenue attributes reflected monetary information.

[Insert Table 2 about here]

The correlations between usage and revenue attributes were computed for the four quarters. Table 3 showed the correlation between the two groups of attributes for the four quarters. From the table we observed that only a few of the attributes were highly correlated (i.e., correlation coefficient $< - 0 . 8 \mathrm { o r } > 0 . 8 )$ . For all four quarters, (a) usage of IDD and revenue generated from IDD calls as well as (b) usage of roaming services and revenue generated from roaming services were highly and positively correlated. The usage of PHS and revenue generated from roaming services were highly and positively correlated only for Q1.

[Insert Table 3 about here]

Our goal was to use the extended FCM algorithm on the usage and revenue attributes and examine whether there were any new usage patterns of customers, any new revenue patterns of customers, and whether the two types of patterns were related to each other. Since the extended FCM algorithm was used, the membership functions for each quarter were obtained. This allowed us to determine the migration paths of customers by studying the changes in the values of the customers’ membership functions. Finally, we conducted inter-cluster analysis to compare between usage patterns and revenue patterns. The next section describes the method we used to validate the extended FCM algorithm’s ability to detect changes in clusters using some benchmark data sets. In the validation process, we used a cluster validity index to determine the quality of the customer clusters obtained by the algorithm.

## 5.2. Clustering and validity index

For determination of the best validity index to go with the extended FCM algorithm, two standard data sets (IRIS and GLASS obtained from the UCI repository of machine learning data bases) [37] and a synthetic data set was used. For all validation data sets we included four temporal stages to simulate a dynamic process of cluster evolution. In general, we added new clusters in the second stage, left the clusters unchanged in the third stage, and removed some clusters in the fourth stage. We designed the experiments in that way to examine the program’s ability to detect appearance of new clusters, disappearance of old clusters, as well as no change in cluster structure. A similar approach was adopted by Fleder and Padmanabhan [16]. The details related to the validation experiments are provided in online supplement Appendix. Next, we selected an appropriate value of the threshold for deciding whether the center of a cluster had disappeared or not. Setting a threshold value to the size of cluster (i.e., the number of data vectors in each cluster) was done to avoid the appearance of insignificant clusters because noise in the data might produce clusters of small size that should be discarded [4 48]. We observed that the quality of the results improved when a minimum cluster size of 3% of the total number of records was used. The choice was made on the basis of experiments done on the validation data sets where we included at least one item and from 1% to 5% of the total number of records as the cluster size. The validation experiments also showed that adjusted SC and adjusted S indexes could help the extended FCM algorithm detect changes more accurately than the standard SC and standard S indexes. We used the adjusted SC index $( S C _ { a d j } )$ to cluster the mobile services data because it performed best for the three validation data sets.

## 5.3. Determination of new clusters

In Tables 4 and 5, the values of $S C _ { a d j }$ for the usage and revenue clusters over four quarters are listed, respectively. For usage and revenue clusters, the number of new clusters varied from two to six in Q1, and zero to six in Q2-Q4. The most effective strategy for deciding the number of clusters was to determine a reasonable range for the number of clusters and then test each number within this range one after the other [8]. In Tables 4 and 5, the cells with bold font indicate the minimum value of $S C _ { a d j } .$ . From Table 4 it is observed that the program identified four usage clusters in Q1, one new usage cluster in $\mathbf { Q } 2 ,$ one new usage cluster in Q3, and no new usage cluster in Q4. For the revenue clusters, the program identified five clusters in Q1, one new cluster in Q2, two new clusters in Q3, and no new cluster in Q4 (as shown in Table 5). In Tables 4 and 5, we also reported the value of $S C _ { a d j }$ index generated from clustering the same set of data using the standard FCM and extended FCM methods. From the results shown in these tables, we can observe that the value of the index obtained using the extended FCM method is smaller than that obtained using the standard FCM method. This indicated that the extended FCM method was able to obtain a better cluster structure than the standard FCM method.

[Insert Tables 4-5 about here]

In Table 6, the clusters detected over four quarters for usage and revenue attributes are listed, respectively. $\mathrm { U C _ { i j } }$ represented the ‘j’th cluster obtained using usage attributes and found in the ‘i’th quarter for the first time. Similarly, $\mathrm { R C _ { i j } }$ identified the ‘j’th cluster obtained using revenue attributes and found in the ‘i’th quarter for the first time. For usage attributes, one new cluster was identified in $\mathbf { Q } 2 \left( \mathbf { U } \mathbf { C } _ { 2 5 } \right)$ and it remained in Q2 and Q3. One more new cluster was identified in Q3 $\left( \mathrm { U C } _ { 3 6 } \right)$ but it disappeared in Q4. For revenue attributes, one new cluster appeared in $\mathbf { Q } 2 \ ( \mathbf { R C } _ { 2 6 } )$ two new clusters appeared in Q3 $( \mathsf { R C } _ { 3 7 }$ and $\mathrm { R C } _ { 3 8 } )$ , and no new cluster appeared in Q4. The new revenue clusters that appeared in Q2 and Q3 did not disappear in later quarters.

## [Insert Table 6 about here]

## 5.4. Interrelationship between usage and revenue clusters

Figures 1 and 2 identify the characteristics of usage and revenue clusters respectively. Each line in Figures 1 and 2 represents a specific cluster. The x-axis lists the attributes used for clustering. The y-axis represents the normalized value of these attributes in Q3. This particular quarter was chosen because all the clusters appeared in this period. As shown in Figure 1, the new usage cluster that appeared in $\mathbf { Q } 2 \left( \mathbf { U } \mathbf { C } _ { 2 5 } \right)$ had high level of IDD and roaming usage. Another new usage cluster appeared in $Q 3 \left( \mathrm { U C } _ { 3 6 } \right)$ . It had even higher level of IDD usage compared to $\mathrm { U C } _ { 2 5 }$ . The new revenue cluster that appeared in $\mathbf { Q } 2 \left( \mathbf { R } \mathbf { C } _ { 2 6 } \right)$ had a high level of revenue contribution for IDD and roaming services. The new revenue cluster that appeared in $\mathbf { Q } 3 \mathbf { \Lambda } ( \mathbf { R } \mathbf { C } _ { 3 7 } )$ had even higher revenue contribution for IDD and roaming than $\mathrm { R C } _ { 2 6 } .$ . Another new revenue cluster $( \mathrm { R C } _ { 3 8 } )$ showed a completely different pattern with low revenue contribution for IDD but high revenue contribution for Roaming, VASV, and VASNV. The new usage clusters $\mathrm { ( U C } _ { 2 5 }$ and $\mathrm { U C } _ { 3 6 } )$ and the new revenue clusters $( \mathrm { R C } _ { 2 6 }$ and $\mathrm { R C } _ { 3 7 } )$ were related to each other.

[Insert Figures 1-2 about here]

In Table 7 we analyze the relationship between the identified usage clusters and revenue clusters of customers. The value in each cell in these tables indicates the number of customers in the usage cluster that is shown as the row and the revenue cluster that is shown as the column simultaneously. Table 7 showed that the majority of customers in usage clusters $\mathrm { U C } _ { 2 5 }$ and $\mathrm { U C } _ { 3 6 }$ also appeared in the revenue clusters $\mathrm { R C } _ { 2 6 }$ and ${ \mathrm { R C } } _ { 3 7 }$ . A majority of customers in usage cluster $\mathrm { U C } _ { 2 5 }$ also appeared in the revenue cluster $\mathrm { R C } _ { 2 6 }$ in Q2. From Table 8, we observed that the majority of customers in $\mathrm { U C } _ { 2 5 }$ belonged to either $\mathrm { R C } _ { 2 6 }$ or ${ \mathrm { R C } } _ { 3 7 }$ because the new usage clusters $\mathrm { U C } _ { 2 5 }$ and $\mathrm { U C } _ { 3 6 }$ were closely related to the new revenue clusters $\mathrm { R C } _ { 2 6 }$ and ${ \mathrm { R C } } _ { 3 7 }$ . The new revenue cluster $\mathrm { R C } _ { 3 8 }$ did not show any relationship with the new usage clusters. Instead, it was more closely related to the old usage clusters identified in Q1. This implied the existence of two different groups of customers who exhibited new behavioral patterns. The first type of customers belonged to usage clusters $\mathrm { U C } _ { 2 5 }$ and $\mathrm { U C } _ { 3 6 }$ and revenue clusters $\mathrm { R C } _ { 2 6 }$ and ${ \mathrm { R C } } _ { 3 7 }$ . We refer to them as Type One customers. Another type of customers showed new revenue patterns (as shown in $\mathrm { R C } _ { 3 8 } )$ but no related new usage patterns. We refer to them as Type Two customers.

[Insert Tables 7-8 about here]

## 5.5. Migration of customers

In Figures 3 and 4, the migratory behavior of Type One and Type Two customers is shown. Here, each line represents the average value of the membership function of these customers with respect to the related clusters. The cluster number on each line and for each quarter represents the cluster for which the value of the membership function is the highest.

From Figure 3, we observed that Type One customers migrated from usage clusters $\mathrm { U C } _ { 1 3 } $ $\mathrm { U C } _ { 2 5 } \to \mathrm { U C } _ { 3 6 } \to \mathrm { U C } _ { 2 5 }$ and revenue clusters $\mathrm { R C _ { 1 5 } }  \mathrm { R C _ { 2 6 } }  \mathrm { R C _ { 3 7 . } U C _ { 1 3 } }$ can be defined by low usage of IDD, roaming, GPRS, PM, PHS, and SMS (as shown in Figure 1). $\mathrm { R C } _ { 1 5 }$ can be defined by low revenue contribution for all services (based on Figure 2). In Q2, Type One customers moved away from cluster $\mathrm { U C } _ { 1 3 }$ and $\mathrm { R C } _ { 1 5 }$ and came closer to the center of a new cluster $\mathrm { U C } _ { 2 5 }$ and $\mathrm { R C } _ { 2 6 }$ $\mathrm { U C } _ { 2 5 }$ can be defined by the characteristics: high usage of IDD and roaming, low usage of GPRS and PM, medium usage of PHS and SMS, while $\mathrm { R C } _ { 2 6 }$ can be defined by the characteristics: high IDD and roaming revenue, and medium VASV revenue. But we could not say that the behavioral patterns represented by $\mathrm { U C } _ { 2 5 }$ were dominant because customers for clusters $\mathrm { U C } _ { 1 3 }$ and $\mathrm { U C } _ { 2 5 }$ were quite close in Q2 (not shown in Figure 3). This phenomenon indicated that these customers changed their behavioral patterns gradually. It was not until Q3 that the dominant position of $\mathrm { U C } _ { 1 3 }$ in Q1 was replaced by two new clusters $\mathrm { U C } _ { 2 5 }$ and $\mathrm { U C } _ { 3 6 }$ . Type One customers kept on changing their behavior by using more IDD and roaming services and this resulted in new clusters $\mathrm { U C } _ { 3 6 }$ and ${ \mathrm { R C } } _ { 3 7 }$ . But Type One customers did not keep on using IDD and roaming services that often and migrated back to $\mathrm { U C } _ { 2 5 }$ in Q4. The increase in IDD and roaming services usage and related increase in revenue generation from IDD and roaming services during Q3 could be due to promotions

carried out by the company in that quarter.

## [Insert Figure 3 about here]

The migration pattern of Type Two customers is shown in Figure 4. Type Two customers migrated from usage clusters $\mathrm { U C } _ { 1 2 } \to \mathrm { U C } _ { 1 1 } \to \mathrm { U C } _ { 1 4 }$ and revenue clusters $\mathrm { R C } _ { 1 2 } \to \mathrm { R C } _ { 3 8 } .$ . Type Two customers were close to the centers of $\mathrm { U C } _ { 1 2 }$ in Q1 and Q2. $\mathrm { U C } _ { 1 2 }$ can be defined by the characteristics: low usage of IDD, roaming, and PHS; high usage of GPRS, PM, and SMS. In Q3, those customers came close to the center of $\mathrm { U C } _ { 1 1 }$ that could be defined by the characteristics: low usage of IDD, GPRS, PM; medium usage of SMS; and high usage of roaming and PHS. In Q4, they moved to the center of cluster $\mathrm { U C } _ { 1 4 } . \mathrm { U C } _ { 1 4 }$ could be defined by high SMS usage and low usage for other services. Type Two customers were close to the center of $\mathrm { R C } _ { 1 2 }$ in Q1 and Q2. In Q3 and Q4, $\mathrm { R C } _ { 3 8 }$ became the dominant cluster. Compared to $\mathrm { R C } _ { 1 2 } , \mathrm { R C } _ { 3 8 }$ had higher revenue contribution for roaming services. It seemed that Type Two who belonged to $\mathrm { R C } _ { 3 8 }$ were influenced by promotional activities carried out by the company in Q3. However, compared to Type One customers, Type Two customers had different original behavioral patterns in Q1. Type One customers originated from usage cluster $\mathrm { U C } _ { 1 3 }$ and revenue cluster $\mathrm { R C } _ { 1 5 }$ whereas Type Two customers originated from usage cluster $\mathrm { U C } _ { 1 2 }$ and revenue cluster $\mathbf { R C } _ { 1 2 }$ . This phenomenon indicated that two different types of customers were attracted by different promotional activities of the mobile services provider in Q3.

[Insert Figure 4 about here]

## 5.6. Factors affecting migratory behavior

In order to determine the usage and the revenue attributes that contributed to the difference in the usage and revenue generating behavior of Type One and Type Two customers, we conducted the ANOVA to determine the significance of the difference between the means of usage and revenue attributes in Q1 and Q3 for these customers. The p-values obtained from the ANOVA, shown in Table 9, indicate that for Type One customers the difference in usage was most significant for IDD and roaming attributes (indicated by the very small p-values). At the same time, the difference in revenue was also most significant for IDD and roaming attributes. For the same customer group, the usage of PHS was significantly different (in fact it increased from Q1 to Q3) but the revenue generated by PHS (i.e., VASV) was not significantly different between the quarters. This implied that the revenue a firm gained by increase in customers’ usage of PHS was not significant. Hence, firms should not promote PHS. Values of PHS usage and VASV revenue for Type One and Type Two customers in Q1 and Q3 are shown in Table 10.

For Type Two customers the ANOVA showed that the difference in usage was most significant for roaming and PHS attributes, and at the same time the difference in generated revenue was most significant for roaming and VASV. However, for Type Two customers the usage of IDD was not significantly different between the two quarters, and yet the revenue generated by IDD was significantly different (revenue increased from Q1 to Q3). This indicated that a small change in usage of IDD could result in a significant change in revenue generated by IDD. It implied that the mobile services provider should monitor the IDD usage of customers carefully. Our observation related to IDD could not be extended for PM (which experienced non-significant change between

Q1 and Q3) because the revenue generated by PM was unknown. For Type Two customers we observed that the significant change in revenue generated by VASNV between the two quarters could be due to changes in revenue generated by PM, SMS, or GPRS.

[Insert Tables 9-10 about here]

## 6. Discussion of results

## 6.1. Managerial implications

The discovery of appearance of new clusters and disappearance of old clusters could help the service provider better align their strategy with customers’ preferences. The identification of customers’ migration path could help the marketers understand customers’ needs better. In this study, the new usage patterns and new revenue patterns were related to high IDD usage. When we looked at customers’ behavioral patterns in the earlier stages, it was observed that they used roaming services frequently. This meant that they had the need for making long distance calls. Further, it was worth noticing that the new usage pattern appeared from Q2. In contrast, the new revenue pattern appeared only in Q4. The delay showed that the company did not respond to the appearance of new usage clusters quickly.

We also observed that in Q3, some customers showed very high usage of IDD and roaming services but this pattern disappeared soon thereafter. It was imperative for the company to identify this pattern and provide the right incentives to the customers because “buyers who buy more, buy more frequently, and buy more across different categories” tend to become long-term customers [43] because “as the number of calling hours exceeds a certain level, switching becomes difficult and users accept whatever the company has to offer” [28]. If the company had responded to the changing pattern on time and adopted some appropriate marketing plans, such as “free ticket for movies and discount coupons for entrance fee in the amusement parks” [22] or special customer prioritization programs, to stimulate these customers to maintain this pattern, they could have generated more revenue from these customers. Our research led to the discovery of two types of customers who showed a migratory pattern in their behavior related to usage and revenue. This finding was similar to that of Jain et al. [24] who envisioned the “existence of two different customer segments with different usage levels and revenues” among customers of mobile services. The Type One customers could be labeled as ‘Price Sensitive Travelers’ whose usage of IDD and roaming (and the revenue generated from these services) increased over the quarters. The firm could monitor these customers more closely to determine the frequency and duration of their travel, and provide appropriate promotions related to IDD and roaming to them. They seemed to respond to promotions. However, these behaviors could well be temporary and the firms needed to study them cautiously to see if the behavioral patterns persisted over time. Type Two customers could be called ‘Premium Multi-service Users’ who exhibited medium to high usage of SMS throughout the year and occasionally made IDD calls that generated high revenue. They were suitable candidates for promotions related to use of SMS and MMS.

The proposed technology could also benefit other types of electronic business and traditional business. E-business such as online shopping might use the proposed technology to track the change of customers’ preference by analyzing the browsing behavior of customers through web logs. Due to the pervasive use of database technology, traditional businesses such as supermarkets accumulates huge amount of data at this time. They might use the proposed method to analyze transactional records so as to discover the migratory consumption behavior of consumers.

## 6.2. Academic implications

This research contributed to the literature on customer data analysis and customer centric IS in several ways. In extant research clustering algorithms were usually applied on static data that had no temporal information and therefore did not deal with changing patterns in customer data. However, we used a clustering algorithm on temporal data. We extended the standard FCM algorithm so that it could handle temporal data which is helpful for understanding the dynamics in customer profiles for customer centric IS.

Further, the migration of user behaviors can be generalized into two types: manifest change and latent change [52]. Adopting standard clustering techniques for analyzing temporal data cannot capture manifest change (e.g. [33]). The same problem holds for studies using stochastic methods like Markov methods because the number of status changes is required as input to the model (e.g. [48]). In comparison, our approach allowed addition of new clusters and removal of old clusters and was able to uncover both manifest change and latent change. For example, the new clusters discovered in our experiments were examples of a manifest change which reflected the change in preference for consumption. On the other hand, as shown in Figure 4, Type Two customers did not change their preference structure in the first and second quarters (remained in the same cluster). However, the strength of their memberships to the clusters lessened and this was an example of

latent change.

The issue of heterogeneity is usually handled by dividing individuals into segments so that individuals within the same segment is said to be homogenous. Therefore, it is important to ensure that the results of clustering grouped similar customers and separated different customers at the same time, which cannot be guaranteed by simply making changes based on the mismatch between existing clusters and incoming data points (e.g. [12, 35]). We provided a solution by using modified clustering validity indexes.

We discovered two types of customers. After Q3, Type One customers exhibited increasing IDD usage and revenue. Type Two customers were more in favor of SMS and roaming services. The two types of customers have different original behavioral patterns and migrated to different new patterns. This finding indicated that there were interactions between customer dynamics and marketing strategies.

Finally, the contribution of the proposed method was comparable to that of Fleder and Padmanabhan [16] who extended the K-means algorithm for temporal data. However, our solution went a step further when we used the knowledge of the membership function of FCM algorithm to determine the migration path of customers’ behavior in addition to detecting changes in structures of customer clusters.

## 6.3. Limitations and future research

There were some limitations of this research. We used FCM clustering which is known to be unsuitable for data sets with large variations in their distribution [14, 19]. An alternate technique like Generative Topographic Mapping [9] that can tolerate variations in data distribution better than FCM, should be explored in future for possible improvement in performance. Combining two or more techniques in a hybrid fashion to take advantage of their beneficial features and improve performance might be an interesting topic for exploration in the future. We divided all attributes into two groups and clustered customers separately. However, a different organization of the same data might lead to other interesting conclusions.

Although interesting interpretation of the results were done in this paper, whether or not the knowledge discovered from the application of the extended FCM algorithm on data matched the needs of marketers and whether this could be used for promoting marketing activities such as cross-selling and up-selling needed to be studied in more details. Literature on relationship marketing and customer equity theory has identified several cognitive, affective, and conative antecedents that contributed to customer loyalty [14]. This included commitment, satisfaction, payment equity, loyalty programs, and direct mailings [3]. An analysis of these factors on the migratory behavior was beyond the scope of this paper but should be followed up in future.

Finally, we assumed that the customers in this research were passive migrants who were not actively searching out better alternatives available in the market [46]. It would be interesting to identify active and passive migratory behavior among customers of mobile services providers in future and discover if any usage or revenue traits could be associated with that.

## 7. Conclusion

In this research, we developed the extended FCM algorithm for detecting significant changes in behavioral patterns of customers of mobile services over time so that it was possible to build dynamic customer profiles which could help customer centric information systems respond to customers’ changing needs. We used it on customer data obtained from a mobile services provider. Using real-life mobile services data we discovered new patterns in usage of mobile services and new patterns in generation of revenue of mobile services. We compared the new usage patterns and the new revenue patterns and also tracked the migration path of two groups of customers who exhibited these patterns. We discovered how the customer groups behaved over the four quarters of a year and what factors impacted their behavior. The proposed algorithm could be used for different applications such as online shopping or mobile shopping. However, the difference between data generated from those contexts and mobile service usage data should be considered. The first difference that should be considered is the choice of the time windows (i.e., daily or monthly or quarterly). Further the dimensionality should also be considered because number of product categories could be much higher than number of types of mobile services.

## Acknowledgement

The first author gratefully acknowledges financial support received from xx in the form of a Category II research grant (Work order number: 3557/RP: ATBOCOMSUDM) for conducting this research.

## References

[1].C.C. Aggarwal, J. Han, J. Wang, A framework for clustering evolving data streams. Proceedings of the 2003 International Conference on Very Large Data Bases, Berlin, Germany, 2003, pp. 81-92.

[2].C.M. Antunes, A.L. Oliveira, Temporal data mining: An overview. Proceedings of the 2001 KDD Workshop on Temporal Data Mining, San Francisco, USA, 2001, pp. 1-13.

[3].A.D. Athanassopoulos, A. Iliakopoulos, Modeling customer satisfaction in telecommunications: Assessing the effects of multiple transaction points on the perceived overall performance of the provider. Production and Operations Management, 12 (2), 2003, pp. 224-244.

[4].G.H. Ball, D.J. Hall, A clustering technique for summarizing multivariate data. Behavioral Science, 12 (2), 1967, pp. 153-155.

[5].H.S. Bansal, S.F. Taylor, Y.S. James, “Migrating” to new service providers: Toward a unifying framework of consumers’ switching behaviors. Journal of the Academy of Marketing Science, 33 (1), 2005, pp. 96-115.

[6].A.M. Bensaid, L.O. Hall, J.C. Bezdek, Validity-guided (re)clustering with applications to image segmentation. IEEE Transactions on Fuzzy Systems, 4 (2), 1996, pp. 112-123.

[7].P.D. Berger, N.I. Nasr, Customer lifetime value: Marketing models and applications. Journal of Interactive Marketing, 12 (1), 1998, pp. 17-30.

[8].J.C. Bezdek, N.R. Pal, Some new indexes of cluster validity. IEEE Transactions on Systems, Man, and Cybernetics – Part B: Cybernetics, 28(3), 1998, pp. 301-315.

[9].C.M. Bishop, M. Svensen, C.K.I. Williams, GTM: The generative topographic mapping. Neural Computation, 10(1), 1998, pp. 215-234.

[10]. R.N. Bolton, A dynamic model of the duration of the customer’s relationship with a continuous service provider: The role of satisfaction. Marketing Science, 17(1), 1998, pp. 45-65.

[11]. P. Brice, W. Jiang, G. Wan, A cluster-based context-tree model for multivariate data streams with applications to anomaly detection. INFORMS Journal of Computing, 23(3), 2011, pp. 364-376.

[12]. X. Chen, I. Bose, An extension of generative topographic mapping for fuzzy clustering. Proceedings of the Second International MultiConference of Engineers and Computer Scientists, Hong Kong, HKSAR, 2007, pp. 823-827.

[13]. H.–L. Chen, M.–S. Chen, S.–C. Lin, Catching the trend: A framework for clustering concept-drifting categorical data. IEEE Transactions on Knowledge and Data Engineering, 21(5), 2009, pp. 652-665.

[14]. A.S. Dick, K. Basu, Customer loyalty: Toward an integrated conceptual framework. Journal of the Academy of Marketing Science, 22(2), 1994, pp. 99-113.

[15]. F.R. Dwyer, Customer lifetime valuation to support marketing decision making. Journal of Direct Marketing, 11(4), 1997, pp. 6-13.

[16]. D. Fleder, B. Padmanabhan, Cluster evolution and interpretation via penalties. Proceedings of the ICDM 2006 Workshop on Data Mining in Marketing, Hong Kong, HKSAR, 2006, pp. 606-614.

[17]. D.J. Flint, C.P. Blocker, P.J. Boutin Jr., Customer value anticipation, customer satisfaction, and loyalty: An empirical examination, Industrial Marketing Management, 40(2), 2011, pp. 219-230.

[18]. V. Ganti, J. Gehrke, R. Ramakrishnan, A framework for measuring changes in data characteristics. Proceedings of the 18th ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems, Philadephia, USA, 1999, pp. 126-137.

[19]. I. Gath, A.B. Geva, Unsupervised optimal fuzzy clustering. IEEE Transactions on Pattern Analysis and Machine Intelligence, 11(7), 1989, pp. 773-781.

[20]. R.D. Gopal, R. Ramesh, A.B. Whinston, Microproducts in a digital economy: Trading small, gaining large. International Journal of Electronic Commerce, 8(2), 2003, pp. 9-29.

[21]. S.C. Hui, G. Jha, Data mining for customer service support. Information & Management, 38(1), 2000, pp. 1-13.

[22]. H. Hwang, T. Jung, E. Suh, An LTV model and customer segmentation based on customer value: A case study on the wireless telecommunication industry. Expert Systems with Applications, 26(2), 2004, pp. 181-188.

[23]. IDC. Worldwide mobile phone market forecast to grow 7.3% in 2013 driven by 1 billion smartphone shipments. 2013. Available at: http://www.idc.com/getdoc.jsp?containerId=prUS24302813. (last accessed September 15, 2014).

[24]. D.C. Jain, E. Muller, N.J. Vilcassim, Pricing patterns of cellular phones and phone calls: A segment-level analysis. Management Science, 45(2), 1999, pp. 131-141.

[25]. A.K. Jain, M.N. Murty, P.J. Flynn. Data clustering: a review. ACM Computing Surveys, 31(3), 1999, pp. 264-323.

[26]. W. Kamakura, C.F. Mela, A. Ansari, Choice models and customer relationship management. Marketing Letters, 16(3-4), 2005, pp. 279-291.

[27]. R. Khan, M. Lewis, V. Singh, Dynamic customer management and the value of one-to-one marketing, Marketing Science, 28(6), 2009, 1063-1079.

[28]. J. Lee, J. Lee, L. Feick, The impact of switching costs on the customer

satisfaction-loyalty link: Mobile phone service in France. Journal of Services Marketing, 15(1), 2001, pp. 35-48.

[29]. S. Lee, F. den Zufry , X. Dreze, A study of consumer switching behavior across Internet portal web sites, International Journal of Electronic Commerce, 7(3), 2003, pp. 39-63.

[30]. M. Lewis, A dynamic programming approach to customer relationship pricing. Management Science, 51(6), 2005, pp. 986-994.

[31]. P. Lingras, M. Hogo, M. Snorek, Temporal analysis of clusters of supermarket customers: Conventional versus interval set approach. Information Sciences, 172(1-2), 2005, pp. 215-240.

[32]. X. Luo, M. Seyedian, Contextual marketing and customer-orientation strategy for E-commerce: An empirical analysis, International Journal of Electronic Commerce, 8(2), 2003, pp. 95-118.

[33]. S.H. Min, I. Han, Detection of the customer time-variant pattern for improving recommender systems. Expert Systems with Applications, 28(2), 2005, pp. 189-199.

[34]. D. Mock, Wireless smackdown: Comparing carrier churn, 2011 Available at http://www.fool.com/investing/general/2007/06/15/wireless-smackdown-churn.aspx (last accessed April 15, 2014).

[35]. O. Nasraoui, M. Soliman, E. Saka, A web usage mining framework for mining evolving user profiles in dynamic web sites. IEEE Transactions on Knowledge and Data Engineering, 20(2), 2008, pp. 202-215.

[36]. M. Natter, A. Mild, U. Wagner, Planning new tariffs at tele.ring: The application and impact of an integrated segmentation, targeting, and positioning tool. Marketing Science, 27(4), 2008, pp. 600-609.

[37]. D.J. Newman, S. Hettich, C.L. Blake, UCI repository of machine learning database. Department of Information and Computer Science, University of California, Irvine, 2011 Available at: http://www.ics.uci.edu/\~mlearn/MLRepository.html (last accessed April 15, 2014).

[38]. M. Ozer, User segmentation of online music services using fuzzy clustering. Omega, 29(2), 2001, pp. 193-206.

[39]. N.R. Pal, and J.C. Bezdek, On clustering validity for the fuzzy c-means model, IEEE Transactions on Fuzzy Systems, 3(3), 1995, pp. 370-379.

[40]. P.E. Pfeifer, R.L. Carraway, Modeling customer relationships as Markov chains. Journal of Interactive Marketing, 14(2), 2000, pp. 43-55.

[41]. G. Punj, D.W. Stewart, Cluster analysis in marketing research: Review and suggestions for application, Journal of Marketing Research, 20(2), 1983, pp. 134-148.

[42]. M. Raghunathan, G. Madey, A firm level framework for planning electronic commerce information systems infrastructure. International Journal of Electronic Commerce, 4(4), 1999, pp. 121-145.

[43]. W.J. Reinartz, V. Kumar, The impact of customer relationship characteristics on profitable lifetime duration. The Journal of Marketing, 67(1), 2003, pp. 77-99.

[44]. M.L. Roberts, P.D. Berger, Direct Marketing Management. Englewood Cliffs: Prentice-Hall, 1989.

[45]. I. Roos, Switching processes in customer relationships. Journal of Service Research, 2(1), 1999, pp. 68-85.

[46]. I. Roos, A. Gustafsson, Understanding frequent switching patterns. Journal of Service Research, 10(1), 2007, pp. 93-108.

[47]. S. Russel, W. Lodwick, Fuzzy clustering in data mining for telco database marketing campaigns. Proceedings of the Eighteenth International Conference of the North American Fuzzy Information Processing Society, New York, USA, 1999, pp. 720-726.

[48]. D.A. Schweidel, E.T. Bradlow, P. S. Fader, Portfolio dynamics for customers of a multiservice provider. Management Science, 57(3), 2011, pp. 471-486.

[49]. C. Shahabi, F. Banaei-Kashani, Efficient and anonymous web-usage mining for web personalization. INFORMS Journal on Computing, 15(2), 2003, pp. 123-147.

[50]. H.S. Song, J.K. Kim, S.H. Kim, Mining the change of customer behavior in an Internet shopping mall. Expert Systems with Applications, 21(3), 2001, pp. 157-168.

[51]. M. Wedel, W. Kamakura, Market Segmentation: Conceptual and Methodological Foundations, 2nd ed., Kluwer Academic Publishers: Norwell, Massachusetts, 2000.

[52]. Y. Wind, Issues and advances in segmentation research, Journal of Marketing Research, 15(3), 1978, pp. 317-337.

[53]. K. Wu, M. Yang, A cluster validity index for fuzzy clustering, Pattern Recognition Letters, 26(9), 2005, pp. 1275–1291.

[54]. S.–I, Wu, A comparison of the behavior of different customer clusters towards Internet bookstores, Information & Management, 43(8), 2006, pp. 986-1001.

[55]. L.A. Zadeh, Fuzzy sets, Information and Control, 8(3), 1965, pp. 338-353.

Table 1  
Comparison of studies on clustering for studying customer migration

<table><tr><td rowspan="2"></td><td rowspan="2">Method</td><td rowspan="2">Cluster validation</td><td colspan="2">Manifest change</td><td colspan="2">Latent change</td></tr><tr><td>Appear</td><td>Disappear</td><td>Membership</td><td>Size</td></tr><tr><td>Brice et al. [11]</td><td>Context tree - a hierarchical clustering method</td><td>No</td><td>Yes</td><td>Yes</td><td>Crisply assign data to clusters</td><td>Yes</td></tr><tr><td>Chen et al. [13]</td><td>Similarity measure based clustering</td><td>No</td><td>Yes</td><td>Not reported</td><td>Crisply assign data to clusters</td><td>Yes</td></tr><tr><td>Fleder and Padmanabhan [16]</td><td>Extension to k-means</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Crisply assign data to clusters</td><td>Yes</td></tr><tr><td>Lingras et al. [31]</td><td>A hybrid of SOM and rough set</td><td>No</td><td>No</td><td>Not reported</td><td>Assign data to clusters with membership</td><td>Yes</td></tr><tr><td>Min and Han [33]</td><td>SOM</td><td>Yes</td><td>No</td><td>Not reported</td><td>Crisply assign data to clusters</td><td>Yes</td></tr><tr><td>Nasraoui et al. [35]</td><td>Similarity measure based clustering</td><td>No</td><td>Yes</td><td>Yes</td><td>Crisply assign data to clusters</td><td>Yes</td></tr><tr><td>Shahabi and Banaei-Kashani [49]</td><td>Similarity measure based clustering</td><td>No</td><td>Yes</td><td>Not reported</td><td>Crisply assign data to clusters</td><td>Yes</td></tr><tr><td>Our approach</td><td>Extension to fuzzy c-means</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Assign data to clusters with membership</td><td>Yes</td></tr></table>

Table 2 Description of attributes

<table><tr><td>Group</td><td>ID</td><td>Description</td></tr><tr><td rowspan="6">Usage group(MOU or bytes)</td><td>IDDUQ1, IDDUQ2, IDDUQ3, IDDUQ4</td><td>International direct dial (IDD) usage for the first, second, third, and fourth quarters.</td></tr><tr><td>RoamingUQ1, RoamingUQ2,RoamingUQ3, RoamingUQ4</td><td>Roaming usage for the first, second, third, and fourth quarters.</td></tr><tr><td>PHSUQ1, PHSUQ2, PHSUQ3, PHSUQ4</td><td>Personal Handphone (PHS) usage for the first, second, third, and fourth quarters.</td></tr><tr><td>GPRSUQ1, GPRSUQ2, GPRSUQ3,GPRSUQ3</td><td>Average size of General Packet Radio Service (GPRS) usage for the first, second, third, and fourth quarters.</td></tr><tr><td>SMSUQ1, SMSUQ2, SMSUQ3, SMSUQ4</td><td>Total number of Short Message Service (SMS) calls for the first, second, third, and fourth quarters.</td></tr><tr><td>PMUQ1, PMUQ2, PMUQ3, PMUQ4</td><td>Average size of Picture Mail (PM) usage for the first, second, third, and fourth quarters.</td></tr><tr><td rowspan="5">Revenue group(in dollars)</td><td>IDDRQ1, IDDRQ2, IDDRQ3, IDDRQ4</td><td>Total revenue obtained from IDD services for the first, second, third, and fourth quarters.</td></tr><tr><td>RoamingRQ1, RoamingRQ2, RoamingRQ3,RoamingRQ4</td><td>Total revenue obtained from roaming services for the first, second, third, and fourth quarters.</td></tr><tr><td>VASVRQ1, VASVRQ2, VASVRQ3,VASVRQ4</td><td>Total revenue obtained from value added services via voice network for the first, second, third, and fourth quarters.</td></tr><tr><td>VASNVRQ1, VASNVRQ2, VASNVRQ3,VASNVRQ4</td><td>Total revenue obtained from value added services via non voice network for the first, second, third, and fourth quarters.</td></tr><tr><td>OtherRQ1, OtherRQ2, OtherRQ3,OtherRQ4</td><td>Total revenue obtained from other services in last six months for the first, second, third, and fourth quarters.</td></tr></table>

## Table 3

Correlation between attributes

<table><tr><td rowspan="3"></td><td colspan="7">Usage Attributes</td></tr><tr><td></td><td colspan="6">Q1</td></tr><tr><td></td><td>MIDD</td><td>Roaming</td><td>PHS</td><td>GPRS</td><td>SMS</td><td>PM</td></tr><tr><td rowspan="8">Revenue Attributes</td><td>IDD</td><td>0.97</td><td>0.28</td><td>0.06</td><td>-0.10</td><td>-0.09</td><td>-0.10</td></tr><tr><td>Other</td><td>0.06</td><td>0.18</td><td>0.14</td><td>0.29</td><td>0.45</td><td>0.24</td></tr><tr><td>Roaming</td><td>0.29</td><td>0.98</td><td>0.85</td><td>-0.19</td><td>0.03</td><td>-0.19</td></tr><tr><td>VASV</td><td>-0.03</td><td>-0.02</td><td>-0.03</td><td>0.39</td><td>0.34</td><td>0.36</td></tr><tr><td>VASNV</td><td>-0.08</td><td>-0.05</td><td>-0.04</td><td>0.74</td><td>0.79</td><td>0.67</td></tr><tr><td></td><td></td><td></td><td>Q2</td><td></td><td></td><td></td></tr><tr><td>IDD</td><td>0.98</td><td>0.23</td><td>0.08</td><td>-0.08</td><td>-0.02</td><td>-0.08</td></tr><tr><td>Other</td><td>0.02</td><td>0.16</td><td>0.12</td><td>0.22</td><td>0.38</td><td>0.18</td></tr><tr><td>Roaming</td><td>0.22</td><td>0.99</td><td>0.73</td><td>-0.13</td><td>0.01</td><td>-0.13</td></tr><tr><td>VASV</td><td>-0.05</td><td>-0.03</td><td>0.00</td><td>0.30</td><td>0.29</td><td>0.29</td></tr><tr><td>VASNV</td><td>-0.02</td><td>-0.03</td><td>0.02</td><td>0.66</td><td>0.75</td><td>0.53</td></tr><tr><td></td><td></td><td></td><td>Q3</td><td></td><td></td><td></td></tr><tr><td>IDD</td><td>0.93</td><td>0.27</td><td>0.11</td><td>-0.08</td><td>-0.01</td><td>-0.09</td></tr><tr><td>Other</td><td>-0.02</td><td>0.11</td><td>0.10</td><td>0.18</td><td>0.29</td><td>0.14</td></tr><tr><td>Roaming</td><td>0.26</td><td>0.91</td><td>0.75</td><td>-0.13</td><td>-0.03</td><td>-0.13</td></tr><tr><td>VASV</td><td>-0.07</td><td>-0.04</td><td>0.01</td><td>0.28</td><td>0.24</td><td>0.26</td></tr><tr><td>VASNV</td><td>-0.03</td><td>-0.06</td><td>0.03</td><td>0.65</td><td>0.71</td><td>0.48</td></tr><tr><td></td><td></td><td></td><td>Q4</td><td></td><td></td><td></td></tr><tr><td>IDD</td><td>0.90</td><td>0.26</td><td>0.10</td><td>-0.10</td><td>-0.02</td><td>-0.08</td></tr><tr><td>Other</td><td>-0.02</td><td>0.00</td><td>0.04</td><td>0.09</td><td>0.18</td><td>0.10</td></tr><tr><td>Roaming</td><td>0.24</td><td>0.89</td><td>0.73</td><td>-0.16</td><td>-0.05</td><td>-0.12</td></tr><tr><td>VASV</td><td>-0.06</td><td>-0.03</td><td>0.01</td><td>0.26</td><td>0.21</td><td>0.22</td></tr><tr><td>VASNV</td><td>-0.02</td><td>-0.06</td><td>0.01</td><td>0.60</td><td>0.67</td><td>0.41</td></tr></table>

Table 4

Adjusted SC values of usage clusters using exFCM and FCM methods

<table><tr><td colspan="9">Number of new clusters</td></tr><tr><td>Quarter</td><td>Method</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td rowspan="2">Q1</td><td>exFCM</td><td>N/A</td><td>N/A</td><td>1.37</td><td>0.47</td><td>0.41</td><td>0.49</td><td>0.43</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>1.37</td><td>0.47</td><td>0.41</td><td>0.49</td><td>0.43</td></tr><tr><td rowspan="2">Q2</td><td>exFCM</td><td>0.75</td><td>0.60</td><td>0.72</td><td>0.80</td><td>0.89</td><td>0.94</td><td>1.03</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>4.0</td><td>1.25</td><td>1.14</td><td>1.22</td><td>1.34</td></tr><tr><td rowspan="2">Q3</td><td>exFCM</td><td>0.62</td><td>0.54</td><td>0.58</td><td>0.63</td><td>0.69</td><td>0.75</td><td>0.83</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>6.38</td><td>1.70</td><td>0.63</td><td>0.60</td><td>0.62</td></tr><tr><td rowspan="2">Q4</td><td>exFCM</td><td>0.59</td><td>0.75</td><td>0.89</td><td>1.03</td><td>0.92</td><td>0.99</td><td>1.08</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>5.68</td><td>1.76</td><td>1.52</td><td>0.71</td><td>1.37</td></tr></table>

Table 5  
Adjusted SC values of revenue clusters using eFCM and FCM methods

<table><tr><td colspan="9">Number of new clusters</td></tr><tr><td>Quarter</td><td>Method</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td rowspan="2">Q1</td><td>exFCM</td><td>N/A</td><td>N/A</td><td>4.38</td><td>1.70</td><td>0.69</td><td>0.58</td><td>0.60</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>4.38</td><td>1.70</td><td>0.69</td><td>0.58</td><td>0.60</td></tr><tr><td rowspan="2">Q2</td><td>exFCM</td><td>0.85</td><td>0.70</td><td>0.76</td><td>0.88</td><td>1.01</td><td>1.09</td><td>1.23</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>5.70</td><td>2.15</td><td>1.09</td><td>0.98</td><td>0.80</td></tr><tr><td rowspan="2">Q3</td><td>exFCM</td><td>0.64</td><td>0.67</td><td>0.61</td><td>0.67</td><td>0.74</td><td>0.82</td><td>0.92</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>5.42</td><td>1.90</td><td>0.88</td><td>0.80</td><td>0.69</td></tr><tr><td rowspan="2">Q4</td><td>exFCM</td><td>0.51</td><td>0.58</td><td>0.64</td><td>0.71</td><td>0.80</td><td>0.85</td><td>0.90</td></tr><tr><td>FCM</td><td>N/A</td><td>N/A</td><td>5.51</td><td>1.43</td><td>0.84</td><td>0.75</td><td>0.67</td></tr></table>

## Table 6

Clusters detected in the four quarters

<table><tr><td>Quarters</td><td>Cluster type</td><td>Clusters appeared</td><td>Clusters disappeared</td></tr><tr><td rowspan="2">Q1</td><td>Usage clusters</td><td> $UC_{11}, UC_{12}, UC_{13}, UC_{14}$ </td><td>No</td></tr><tr><td>Revenue clusters</td><td> $RC_{11}, RC_{12}, RC_{13}, RC_{14}, RC_{15}$ </td><td>No</td></tr><tr><td rowspan="2">Q2</td><td>Usage clusters</td><td> $UC_{25}$ </td><td>No</td></tr><tr><td>Revenue clusters</td><td> $RC_{26}$ </td><td>No</td></tr><tr><td rowspan="2">Q3</td><td>Usage clusters</td><td> $UC_{36}$ </td><td>No</td></tr><tr><td>Revenue clusters</td><td> $RC_{37}, RC_{38}$ </td><td>No</td></tr><tr><td rowspan="2">Q4</td><td>Usage clusters</td><td>No</td><td> $UC_{36}$ </td></tr><tr><td>Revenue clusters</td><td>No</td><td>No</td></tr></table>

Table 7

Relationship between usage and revenue clusters in Q3

<table><tr><td rowspan="2">Usage clusters</td><td colspan="8">Revenue clusters</td><td rowspan="2">Total</td></tr><tr><td> $RC_{11}$ </td><td> $RC_{12}$ </td><td> $RC_{13}$ </td><td> $RC_{14}$ </td><td> $RC_{15}$ </td><td> $RC_{26}$ </td><td> $RC_{37}$ </td><td> $RC_{38}$ </td></tr><tr><td> $UC_{11}$ </td><td>9</td><td>1</td><td>10</td><td>1363</td><td>26</td><td>35</td><td>0</td><td>594</td><td>2038</td></tr><tr><td> $UC_{12}$ </td><td>32</td><td>753</td><td>719</td><td>153</td><td>6</td><td>9</td><td>0</td><td>402</td><td>2074</td></tr><tr><td> $UC_{13}$ </td><td>1030</td><td>177</td><td>231</td><td>411</td><td>507</td><td>3</td><td>0</td><td>112</td><td>2471</td></tr><tr><td> $UC_{14}$ </td><td>292</td><td>499</td><td>848</td><td>260</td><td>26</td><td>6</td><td>0</td><td>198</td><td>2129</td></tr><tr><td> $UC_{25}$ </td><td>25</td><td>14</td><td>27</td><td>95</td><td>24</td><td>395</td><td>18</td><td>31</td><td>629</td></tr><tr><td> $UC_{36}$ </td><td>3</td><td>2</td><td>3</td><td>17</td><td>8</td><td>89</td><td>340</td><td>7</td><td>469</td></tr><tr><td>Total</td><td>1391</td><td>1446</td><td>1838</td><td>2299</td><td>597</td><td>537</td><td>358</td><td>1344</td><td>9810</td></tr></table>

## Table 8

Relationship between usage and revenue clusters in Q4

<table><tr><td rowspan="2">Usage clusters</td><td colspan="8">Revenue clusters</td><td rowspan="2">Total</td></tr><tr><td> $RC_{11}$ </td><td> $RC_{12}$ </td><td> $RC_{13}$ </td><td> $RC_{14}$ </td><td> $RC_{15}$ </td><td> $RC_{26}$ </td><td> $RC_{37}$ </td><td> $RC_{38}$ </td></tr><tr><td> $UC_{11}$ </td><td>0</td><td>0</td><td>3</td><td>1152</td><td>17</td><td>93</td><td>13</td><td>467</td><td>1745</td></tr><tr><td> $UC_{12}$ </td><td>31</td><td>683</td><td>758</td><td>185</td><td>7</td><td>33</td><td>2</td><td>438</td><td>2137</td></tr><tr><td> $UC_{13}$ </td><td>1077</td><td>206</td><td>241</td><td>558</td><td>238</td><td>51</td><td>11</td><td>164</td><td>2546</td></tr><tr><td> $UC_{14}$ </td><td>336</td><td>576</td><td>935</td><td>401</td><td>38</td><td>47</td><td>11</td><td>343</td><td>2687</td></tr><tr><td> $UC_{25}$ </td><td>2</td><td>3</td><td>3</td><td>14</td><td>2</td><td>357</td><td>306</td><td>8</td><td>695</td></tr><tr><td>Total</td><td>1446</td><td>1468</td><td>1940</td><td>2310</td><td>302</td><td>581</td><td>343</td><td>1420</td><td>9810</td></tr></table>

## Table 9

Difference in means of usage and revenue attributes between Q1 and Q3

<table><tr><td>Usage attributes</td><td>Type One (p-value)</td><td>Type Two (p-value)</td><td>Revenue attributes</td><td>Type One (p-value)</td><td>Type Two (p-value)</td></tr><tr><td>IDD</td><td>0.00E+00</td><td>4.95E-01</td><td>IDD</td><td>0.00E+00</td><td>3.25E-02</td></tr><tr><td>Roaming</td><td>1.55E-133</td><td>3.19E-266</td><td>Roaming</td><td>2.78E-108</td><td>3.53E-281</td></tr><tr><td>PHS</td><td>2.27E-21</td><td>1.76E-96</td><td>VASV</td><td>1.28E-01</td><td>3.80E-58</td></tr><tr><td>GPRS</td><td>4.49E-17</td><td>5.88E-14</td><td>VASNV</td><td>2.56E-39</td><td>5.99E-15</td></tr><tr><td>SMS</td><td>4.89E-31</td><td>3.21E-06</td><td>Other</td><td>8.19E-33</td><td>1.92E-19</td></tr><tr><td>PM</td><td>2.70E-02</td><td>9.42E-01</td><td></td><td></td><td></td></tr></table>

## Table 10

Value of PHS usage and VASV revenue for Type One and Type Two Customers in Q1 and Q3

<table><tr><td rowspan="2"></td><td colspan="2">Type One</td><td colspan="2">Type Two</td></tr><tr><td>Q1</td><td>Q3</td><td>Q1</td><td>Q3</td></tr><tr><td>PHS</td><td>0.14(0.29)</td><td>0.29(0.36)</td><td>0.14(0.29)</td><td>0.39(0.31)</td></tr><tr><td>VASV</td><td>0.11(0.23)</td><td>0.13(0.24)</td><td>0.43(0.28)</td><td>0.58(0.13)</td></tr></table>

![](/api/attachments/D55NEYGB/fulltext/images/ca93f240e0f9098bda512535378d64282b4337831259b982372b016bad1db10d.jpg)  
Fig. 1. Characteristics of usage clusters.

![](/api/attachments/D55NEYGB/fulltext/images/8fce291b44eb8efbc99eebd5230466e3f83cbdabd59d9cd9218d8c0a0afd8e9b.jpg)  
Fig. 2. Characteristics of revenue clusters.

![](/api/attachments/D55NEYGB/fulltext/images/e031e6c21c4fc41cdc40921e19d56a4c6de82c53661d2149e5d29b1cf0606f4e.jpg)  
Fig. 3. Migration pattern of Type One customers.

![](/api/attachments/D55NEYGB/fulltext/images/a0a94a6d9ce40f3c19cc63b9ae2a06a0ec46385449fd1eaac2c9c13537442f34.jpg)  
Fig. 4. Migration pattern of Type Two customers.
