---
otero_id: 4686
otero_key: "6GQH5HZ7"
title: "Personalized recommendations based on time-weighted overlapping community detection"
authors: "Haoyuan Feng; Jin Tian; Harry Jiannan Wang; Minqiang Li"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2015.02.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Personalized recommendations based on time-weighted overlapping community detection

Haoyuan Feng <sup>a</sup>, Jin Tian <sup>a,</sup>\*, Harry Jiannan Wang <sup>b</sup>, Minqiang Li <sup>a</sup>

<sup>a</sup> College of Management and Economics, Tianjin University, Tianjin 300072, PR China <sup>b</sup> University of Delaware, Newark, DE 19716, USA

## A R T I C L E I N F O

Article history: Received 17 September 2014 Received in revised form 22 January 2015 Accepted 14 February 2015 Available online xxx

Keywords: Personalized recommendations Recommender system Dynamic user interests Overlapping community Time-weighted association rules

## A B S T R A C T

Capturing and understanding user interests are an important part of social media analytics. Users of social media sites often belong to multiple interest communities, and their interests are constantly changing over time. Therefore, modeling and predicting dynamic user interests poses great challenges to providing personalized recommendations in social media analytics research. We propose a novel solution to this research problem by developing a temporal overlapping community detection method based on time-weighted association rule mining, We conducted experiments using MovieL ens and Netflix datasets, and our experimental results show that our proposed approach outperforms several existing methods in recommendation precision and diversity.

\- 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Capturing, understanding, and predicting user interests are critical tasks for social media sites to provide better product designs [1], accurate targeted advertising, and personalized services [12,55] as well as to enhance users’ continuance and sense of belonging to these social media sites [32]. Twitter launched a new push notification feature in late 2013 to deliver personalized recommendations for tweets and accounts to follow after implementing the long-running @MagicRecs experiment to monitor users’ following and re-tweeting behavior. Recommender systems have been developed to predict user preferences and have been applied to various applications and websites, such as Amazon, Netflix, Pandora, and LinkedIn.

Recommendation algorithms are at the core of recommender systems, which can be divided into three primary categories, i.e., content-based recommendation approaches, collaborative filtering (CF) recommendation approaches, and hybrid approaches [6]. Content-based approaches aim to recommend items to a user based on the item description and the user’s browsing history and interest profile. A lack of diverse recommendations is the drawback of content-based approaches [13]. Collaborative filtering approaches provide recommendations to a user by collecting preference information from many other users, but these approaches often have limitations such as rating sparsity, scalability, and efficiency [36]. Studies have shown that the quality of recommender systems can have a great impact on overall customer satisfaction [17].

Some recommendation methods are developed based on information from all users [26,30]. Given the huge amount of data on users and their item preferences, these approaches often face performance issues due to time-consuming data modeling and processing [37]. Users of social media sites often form special interest groups/communities, e.g., Pinterest users use different boards to form groups such as fashion, home decor, and gardening, and Twitter users use hash tags to group tweets based on special topics. Researchers have found that modeling user preferences based on users’ community or group associations can enhance the efficiency of recommendation algorithms [8,15,21]. Some social media analytics approaches use existing virtual communities on social websites, such as online knowledge communities or discussion forums [2,3,49]. However, these communities cannot be easily categorized in many scenarios. Thus, there is a large variety of community detection methods. Overlapping community is a type of community structure in which a user may belong to more than one community. Clustering users into overlapping communities can not only help with the data sparsity problem but also enhance recommendation diversity by obtaining recommendations from different communities [14,42].

Some early user interest models in recommender systems usually assumed that users’ interests were static and did not change over time. Actually, users’ interests are dynamic rather than static. For example, users may prefer different clothing styles in different seasons and/or at different ages, and users’ interests in digital products such as music and movies are more likely to change over time [5,7,20,27].

Fig. 1 provides an example from the MovieLens dataset to show the percentage of movies in different categories rated by a user over 8 months, from September 1997 to April 1998. Fig. 1 clearly illustrates that this user’s interest in different types of movies changes significantly over time. For example, the user seems to like watching horror movies before February, but this interest disappears in the last three months. Static recommender systems may capture users’ previous interests nicely, but they fail to update the interests over time, resulting in inaccurate recommendations and a poor user experience. Association rules (AR) have been widely adopted to represent user interests in many recommendation models due to their ability to scale to large datasets and achieve high precision [13,38,48]. Time decay functions in AR and other methods, such as Singular Value Decomposition (SVD) and Hidden Markov, have been used to model user interest drift over time [16,22,34,43,45]. However, most of the existing approaches model temporal user interest drift at the individual user level, without considering the effects of related changing overlapping communities.

In this paper, we propose a novel recommendation method called Temporal Overlapping community detection using Time-weighted Association Rules (TOTAR). The key thrust of TOTAR is that temporal factors of user interests are fully incorporated in both overlapping community detection and association rules generation. More specifically, the main contributions of this paper are threefold: (1) the development of a temporal method to detect overlapping communities based on a user–user graph with time-weighted links; (2) the design of a new time-weighted association rule mining algorithm based on temporal overlapping communities to model user interest drift over time; and (3) the proposal of a new recommendation model based on users’ dynamic temporal interests and multi-memberships in their overlapping communities.

The remainder of the paper is organized as follows. Section 2 briefly reviews the relevant literature. The details of the proposed TOTAR approach are elaborated in Section 3. Section 4 presents experiments using the MovieLens and Netflix datasets and discusses the results. Finally, Section 5 summarizes the key points of the paper and discusses future research.

## 2. Literature review

## 2.1. Overlapping community detection

Overlapping community detection methods provide alternatives for representing the variability and diversity of user interests. Early efforts at community detection assumed that communities are non-overlapping or disjointed. To increase detection speed and quality, Newman proposed the Fast Newman algorithm [39], which adopted the Modularity function for global optimization. This algorithm has been widely used in community detection. Palla et al. presented the first overlapping community detection algorithm, the Clique Percolation Method (CPM), which performed well in recognizing overlapping frameworks in complex networks [40]. Lancichinetti and Fortunato showed that the Modularity function did not fit the overlapping community context very well, and it had a problem with resolution limit and extreme degradation under overlapping conditions [24]. More recently, overlapping community detection methods based on local optimization have been proposed. Lancichinetti et al. proposed a local fitness maximization (LFM) algorithm that took advantage of both overlapping and the hierarchy of communities [25]. Meo et al. emphasized enhancing existing community detection algorithms by adding a pre-processing step in which links were weighted according to their centrality [41]. Furthermore, Lee et al. found that a phenomenon called pervasively overlapping communities existed in many networks, which meant that nearly all nodes belong to multiple communities [28]. Pervasively overlapping communities may contain more external than internal links and thus violate the properties of network communities. An expanded LFM algorithm has been proposed to handle the pervasively overlapping community problem [28,29].

## 2.2. Association rule mining

Association rules have been successfully used to represent user interests in static recommendation models [48]. Generally, user interests can be provided by AR in the form ‘A ! B’ (where A and B are user interests or items), which means that users interested in ‘A’ are likely interested in ‘B’. For dynamic interest models, Li et al.

![](/api/attachments/6GQH5HZ7/fulltext/images/d58832efe38e277aba9824b251d9dd3ee96a7d4b7e0a9618165b4b90b3b4e4b7.jpg)  
Fig. 1. Percentage of a user’s interest during different months.

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

H. Feng et al. / Information & Management xxx (2015) xxx–xxx

adopted calendar-based temporal association rules to show the time effect on user interests [30]. Joong and Nam used timeinterval rules to separate interests into long-term and short-term interests and to describe the purchase cycle, which predicted the time until users’ next purchases [18]. Yun proposed a weighted sequential pattern mining algorithm in which both the supports and the weights of the patterns were considered to avoid discarding those important sequences with low supports [53]. Domingues et al. presented a hybrid approach that consisted of inserting contextual and background information for multidimensional recommendations and applied it to two Top-N recommendation techniques – item-based collaborative filtering and recommendations based on association rules [11]. Kardan and Ebrahimi applied the association rules mining technique to discover similar users and presented a hybrid recommendation approach that identified a user similarity neighborhood from some implicit information that can be collected from a discussion group, such as a user’s contributions to common discussions [19].

## 2.3. User interest drift

Concept drift occurs when observed data are generated from a distribution that changes over time [47]. Interest drift can be considered a special term for concept drift in recommendations. This phenomenon occurs in many areas, such as changes in climatic conditions with the seasons and purchase behavior changes in the supermarket.

Different methods have been proposed to model user interest drift. Cagliero treated interest drift as a change pattern problem of taxonomies by calculating the frequencies of different interest classes [9]. Huang and Huang made use of time windows to strengthen the effects of the most recent data and to mine sequential rules for target users [16]. Rafeh and Bahrehmand modeled user interest changes using a time decay function and proposed an adaptive CF algorithm that took time into account when predicting users’ behavior [43]. Liu et al. proposed a recommendation approach that combined the segmentationbased sequential rule method with the segmentation-based KNN-CF method, which detected sequential rules over time based on the purchase history of user groups and then recommended items to target users [34]. Koren tracked user interest changes in a potential matrix factorization context and incorporated the timedrifting user preference model into two approaches – CF-matrix factorization and neighborhood methods [22]. Sahoo et al. developed a hidden Markov model of changing user preferences based on the probabilistic graphical modeling framework [45]. Liu and Deng predicted users’ phasing activities by estimating links in a time-weighted user–item graph in which the latest phasing activities were recorded with the largest weights [33]. Xiang et al. made temporal recommendations on a user–item graph using defined time session nodes and combined the recommend list with long-term and short-term preferences [51]. Zeng et al. used different snapshots of a user–item graph at different time points to calculate degree changes in the graph and predicted potentially popular items in a given future time window [54]. Sie et al. made real-time recommendations to find co-authors in a user–user graph by performing time-based discounting of keyword-toauthor relatedness to measure authors’ changeable interests over time [46].

## 3. TOTAR framework

In this section, we present our proposed recommendation approach, called Temporal Overlapping community detection

![](/api/attachments/6GQH5HZ7/fulltext/images/76e5028c7fbaee9edc990f2239f10c6afebca10f04ce5b2fa797c6d1aef9b07a.jpg)  
Fig. 2. TOTAR framework.

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

H. Feng et al. / Information & Management xxx (2015) xxx–xxx

using Time-weighted Association Rules (TOTAR). The three main steps are illustrated in Fig. 2. The first step aims to generate overlapping communities via temporal user–user graph construction, overlapping community detection, and community combination. Then, the time-weighted association rules for each user are mined in every overlapping community. Finally, a Top-N recommendation list for each user is generated by filtering association rules and combining recommendations from the user’s different overlapping communities. The details of each step are discussed next.

## 3.1. Overlapping community generation

Given a set of users and a set of items, the transactions between them are usually represented as a user–item interaction graph in which user nodes connect only to the items that they preferred. Note that this study aims to predict the drift of user interests; thus, we only focus on transactions in which users indicate preferences (rather than making purchases). In the movie-rating context, we only consider user ratings with scores of 3 or above on a 1-to-5 scale. Then, a user–user interaction graph can be transformed from the user–item graph, where a link between two user nodes in the user–user graph indicates that the two users have some common preferred items, and the link weight represents the number of common items [44,56]. To incorporate the time effects of user interest changes, we assume that the more closely two users’ common transactions occur in time, the more likely the two users’ interests tend to coincide, which leads to time-weighted links in the user–user graph.

## 3.1.1. User–user graph construction with time-weighted links

According to the data timestamps, the training dataset is separated into several subsets of different periods of time. Suppose that the ith user rates the jth item in the tth period of time. $i = 1 , . . . ,$ $n . ~ j = 1 , ~ . ~ . . , m . ~ t \in \{ 1 , ~ . ~ . . , T L \}$ . n is the number of users, m is the number of items, and TL is the total time length of the transactions in the training dataset. If there is no transaction information or the ratings are smaller than the preferred threshold, t is set to 0.

Then, the transactions can be represented as the time-weighted user–item matrix $\pmb { G } = \left[ g _ { i j } \right] _ { n \times m }$ using a forgetting-curve-like function as follows:

$$
g _ {i j} = \left\{ \begin{array}{l l} e ^ {- (T L - t) / \theta_ {1}} & \text { if } t > 0 \\ 0 & \text { if } t = 0 \end{array} \right.\tag{1}
$$

where $\theta _ { 1 } > 0$ is a pre-designed real number that indicates the time effect of the transactions. The larger the value of $\theta _ { 1 }$ is, the less impact time has on the interactions between users and items. For example, when $\theta _ { 1 } \longrightarrow + \infty ,$ then $g _ { i j } = 1$ and the time-weighted user– item graph turns into a conventional one without considering time effects. Then, the time-weighted user–user graph is transformed from the user–item graph by adding links between users who prefer the same items. Taking a matrix view of the interactions, the user–user graph is described as a user–user matrix:

$$
\boldsymbol {U} = \boldsymbol {G} \times \boldsymbol {G} ^ {T} = [ u _ {i l} ] _ {n \times n}\tag{2}
$$

Therefore, the links between users reflect the similarity of their interests, which is mainly determined by both the number of items that they both like and the time they liked those items. The element u in matrix U calculates the degree of interest similarity between the ith user and the Ith user, and $\begin{array} { r } { u _ { i l } = \sum _ { j = 1 } ^ { m } g _ { i j } \times g _ { l j } , i = 1 } \end{array}$ $\ldots , n , l = 1 , . . . , n .$

## 3.1.2. Overlapping community detection

We enhance the LFM algorithm [25] to detect overlapping communities in time-weighted user–user graphs. First, instead of the random selection of start nodes in the original LFM algorithm, we choose the start nodes by degree ranking. Second, we define that the node-removing process does not start until the nodes in a community stop expanding. Finally, to avoid the endless loops problem, we restrict the start node from being removed. The concept of node degree is used to measure the importance of a node, which is calculated as $d _ { i } = \sum _ { l = 1 } ^ { n }$ u in the user–user graph. After calculating node degrees and selecting start nodes, the communities are identified by maximizing the following fitness function [25]:

$$
f _ {k} = \frac {w _ {k} ^ {\mathrm{in}}}{\left(w _ {k} ^ {\mathrm{in}} + w _ {k} ^ {\mathrm{out}}\right) ^ {\alpha}}\tag{3}
$$

where w<sup>in</sup> means the total internal degree of the kth community, which is equal to two times the total link weights in the kth community, and $w _ { k } ^ { \mathrm { o u t } }$ is the total external degree of the kth community, which is the sum of all of the link weights between the internal nodes and external nodes of the kth community. $\alpha \in [ 1 , 2 ]$ is a pre-designed real number to control the scale of communities. $k \in \left\{ 1 , ~ . . . , ~ K \right\}$ and K is the total number of overlapping communities.

The procedure for overlapping community detection is listed in Table 1.

## 3.1.3. Community combination

If two communities obtained through our enhanced LFM method have too many overlapping nodes, they should be merged into a single community. Considering the different sizes of communities, we propose a hybrid community combination strategy defined below. We first introduce two existing overlapping proportion measures, and then we describe the hybrid combination strategy based on those measures.

The overlapping proportion is calculated to determine whether the two communities should be combined. In this paper, we adopt two types of overlapping proportion measures. One measure is shown as follows [50]:

$$
\delta_ {p q} = \beta \times \frac {\left| C _ {p} \cap C _ {q} \right|}{\left| C _ {p} \cup C _ {q} \right|} + (1 - \beta) \times \frac {\left| N C _ {p} \cap N C _ {q} \right|}{\left| N C _ {p} \cup N C _ {q} \right|}\tag{4}
$$

where $C _ { p }$ and $C _ { q }$ are the pth and qth overlapping communities, $p \in \{ 1 , . . . , K \} ,$ and $q \in \{ 1 , \ . . . , \ K \} . \ N C _ { p }$ and $N C _ { q }$ are the set of ‘‘neighbor’’ nodes that directly connect with the nodes in $C _ { p }$ and $C _ { q } .$

## Table 1

Overlapping community detection procedure.

Step 1: Select node A, which has the highest degree in the whole user–user graph, as the start node.

Step 2: Detect the natural community of this node, which is identified through the following procedure:

(1) Initialize community C with the selected node and set the initial fitness of the community as zero;

(2) Find a set of neighbor nodes of C that are not included in C but that have direct connections with the nodes in C

(3) Calculate the fitness of each neighbor node to community C, i.e., the fitness change of C with and without the neighbor node, Add the one that has the largest positive fitness to community C among all of the neighbor nodes into community C, then recalculate the fitness of the community;

(4) Repeat (2) and (3) until there is no neighbor node that has positive fitness to community C;

(5) Calculate the fitness of each node in community C, which is also the fitness change of C with and without one node. Remove the node that has the largest negative fitness to community C (except the start node in this community), then recalculate the fitness of the community;

(6) Repeat (5) until there is no node in community C that has negative fitness.

Step 3: If there are some nodes that are not assigned to any existing community, select the highest degree node from such nodes and go to Step 2; otherwise, output the final communities.

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

jj is the node number of a community or of a node set. $\beta \in [ 0 , 1 ]$ is a pre-designed parameter to leverage the effect of internal nodes and their neighbors on the combination process. Thus, in this situation, the combination probability of two communities is determined by both the overlapping ratio of the nodes in these communities and the overlapping ratio of those neighbor nodes of the two communities. A combination threshold $\rho _ { 1 } \in [ 0 , 1 ]$ is predesigned. $\mid \mathrm { ~ f ~ } \delta _ { p q } > \rho _ { 1 }$ , then the two communities are combined.

There is another overlapping proportion measure to execute in a situation where the size of one community is much smaller than the other.

$$
\delta_ {p q} = \frac {\left| C _ {p} \cap C _ {q} \right|}{\min \left(\left| C _ {p} \right| , \left| C _ {q} \right|\right)},\tag{5}
$$

which can be interpreted as the proportion of nodes in the smaller community that are embedded in the larger community [28]. A combination threshold $\rho _ { 2 } \in [ 0 , 1 ]$ is pre-designed. I $\dot { } \delta _ { p q } > \rho _ { 2 } ,$ , then the two communities are combined.

If the two overlapping communities are similar in size, both node distributions of the two communities should be considered, and the first overlapping community measure (shown in Eq. (4)) is adopted. However, if one community is much larger than the other, the combination threshold should be mainly determined using the small community rather than the large one, and the second measure (shown in Eq. (5)) can be used for determining the combination. Thus, based on the two pre-designed combination thresholds $\rho _ { 1 }$ and $\rho _ { 2 } ,$ we first determine a threshold z for the community scale ratio of the larger community size to the smaller community size:

$$
\zeta = \frac {\rho_ {2} + \rho_ {2} \times \rho_ {1} - \rho_ {1}}{\rho_ {1}}\tag{6}
$$

Then, the hybrid community combination process is executed as shown in Table 2.

## 3.2. Time-weighted association rule mining

## 3.2.1. Frequent itemset mining

In this paper, we conduct association rule mining on different sizes of overlapping communities. The minimum support value is used to exclude rules without enough support from the result, e.g., an itemset with a support value of 20% will not be selected as a frequent itemset if the minimum support value is set as 30% for a certain community. The minimum support value directly affects the usefulness of the mined rules from the association analysis [10]. A uniform minimum support value for all communities may lead to redundant or insufficient rule generation because of the different distributions of itemsets in communities of different sizes. The total number of itemsets partially reflects information from the mined rules. We intend to select the same proportion of itemsets in each community no matter how many itemsets there

## Table 2

Hybrid overlapping community combination procedure.

Step 1: The ratio of the two community sizes is calculated as $\begin{array} { r } { r _ { p q } = \frac { \operatorname* { m a x } \left( \left| C _ { p } \right| , \left| C _ { q } \right| \right) } { \operatorname* { m i n } \left( \left| C _ { p } \right| , \left| C _ { q } \right| \right) } . } \end{array}$

Step 2: If $r _ { p q } < \zeta ,$ which means that there is no significant difference in size between the two communities, the overlap proportion measure in Eq. (4) is used to calculate the overlapping proportion measure $\delta _ { p q } .$ Otherwise, go to step 4. Step $3 \colon \mathrm { I f } \delta _ { p q } > \rho _ { 1 }$ , the two communities should be combined; otherwise, there is no combination operation executed. Go to step 6.

Step 4: If $\dot { r } _ { p q } \ge \zeta ,$ which means that the size of one community is much smaller than the other, $\operatorname { E q . }$ (5) is used to calculate the overlapping proportion measure $\delta _ { p q } .$ Step 5: I $\partial _ { p q } > \rho _ { 2 } ,$ , the two communities should be combined; otherwise, there is no combination operation executed. Go to step 6.

are in each community. For example, suppose there are two communities that have extracted 100 itemsets and 10 itemsets, respectively. If a uniform minimum support value (such as 20) is adopted, 20 itemsets out of 100 may be mined as the frequent itemsets in the first community, while all 10 itemsets may be selected as the frequent itemsets in the second community. There will not be enough frequent itemsets mined for the first community, but there will be redundant frequent itemsets mined for the second community. Thus, a good alternative strategy is to select 50 frequent itemsets out of the 100 itemsets and 5 frequent itemsets out of the 10 itemsets. We design a special self-adaptive approach to determine the minimum support value and to optimize the frequent itemset mining process.

Due to the frequent dataset scanning in frequent itemset mining, it is desirable to develop parallel processes to speed up the time-consuming computation. The Frequent Pattern Growth (FP Growth) algorithm provides a parallelization scheme to accelerate the search process without generating candidate itemsets [52]. In this search process, the minimum support value plays a key role in affecting the algorithm’s performance and must be self-adaptive so as to provide enough rules for highquality rule mining without excessively increasing the computation time [31].

We transform the submatrix of the time-weighted user–item matrix $\pmb { G } = \left[ g _ { i j } \right] _ { n \times m }$ (mentioned in Section 3.1.1) to identify the items that users prefer in a certain community. The resulting transformed submatrix ${ \pmb Z } _ { k } = [ z _ { i j } ] _ { n _ { \nu } \times m _ { \nu } }$ , which only contains n users and $m _ { k }$ items involved in the kth community, is defined as:

$$
z _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if } g _ {i j} > 0 \\ 0 & \text { if } g _ {i j} = 0 \end{array} \right.\tag{7}
$$

where $i = 1 , . . . , n _ { k }$ and $j = 1 , . . . , m _ { k } .$

Then, the item graph can be described as $\pmb { V } = [ \nu _ { j h } ] _ { m _ { k } \times m _ { k } }$ , where $\begin{array} { r } { \nu _ { j h } = \sum _ { i = 1 } ^ { n _ { k } } z _ { i j } \times z _ { i h } } \end{array}$ <sup>k k</sup>. The minimum support value in the kth community, mins $\boldsymbol { l } \boldsymbol { p } _ { k } ,$ is calculated as:

$$
\text {   minsu   } p _ {k} = \frac {1}{n _ {k}} \times \max \left\{n _ {\sup} \left| \sum_ {d = 1} ^ {n _ {\sup}} \left(d \times \sum_ {j = 1} ^ {m _ {k}} \sum_ {h = 1} ^ {m _ {k}} (1 - \min (| v _ {j h} - d |, 1))\right) \right. \right.
$$

$$
\leq r _ {t h r e s} \times \left. \sum_ {j = 1} ^ {m _ {k}} \sum_ {h = 1} ^ {m _ {k}} v _ {j h} \right\}\tag{8}
$$

where $n _ { \mathrm { s u p } }$ is the number of itemsets $\{ i t e m _ { j } , i t e m _ { h } \} ,$ , and $r _ { t h r e s } \in ( 0$ 0.5] is used to limit the number of mining rules.

## 3.2.2. Time-weighted association rule mining

We propose a novel time-weighted association rule mining method based on the FP Growth model, which considers the time weights on both the antecedent parts and the consequent parts in the rules. The first step is to divide the training set into TL time periods. If there is a transaction showing that a user prefers (the rating score is greater than the preferred threshold) an item in the tth period of time $( t = 1 , . . . , T L )$ , this transaction’s time effect can be calculated as a weight:

$$
w _ {t} ^ {\text { conf }} = \left\{ \begin{array}{l l} e ^ {- (T L - t) / \theta_ {2}} & \text { if } t > 0 \\ 0 & \text { if } t = 0 \end{array} \right.\tag{9}
$$

where $\theta _ { 2 } > 0$ is a time decay parameter whose value should be learned from the datasets [22,37]. If there is no rating information or the rating scores are smaller than the preferred threshold, t is set as 0. $\tilde { w } _ { t } ^ { \mathrm { c o n f } } \in ( 0 , 1 )$ denotes the normalized values of $w _ { t } ^ { \mathrm { c o n f } }$ . For clarity, $\dot { \tilde { w } } _ { t } ^ { \mathrm { c o n f } } ( A )$ Þ means the time weight of the transactions in which item A appears in the tth time period. Then, the support values of the rules are calculated separately in different time periods to

H. Feng et al. / Information & Management xxx (2015) xxx–xxx

obtain time-weighted confidences Timeconf:

$$
\begin{array}{l}\text {Timeconf} _ {k} (A \rightarrow B) = \frac {1}{n _ {k} ^ {\sup} (A)}\\\times \sum_ {s = 1} ^ {T L} \left(\tilde {w} _ {s} ^ {\text {conf}} (A) \times \sum_ {t = 1} ^ {T L} (\tilde {w} _ {t} ^ {\text {conf}} (B) \times n _ {k} ^ {\sup} (A ^ {(s)}, B ^ {(t)}))\right)\end{array}\tag{10}
$$

where $n _ { k } ^ { \mathsf { s u p } } ( A )$ is the number of transactions in which item A appears in the kth community, and $n _ { k } ^ { \operatorname* { s u p } } ( A ^ { ( s ) } , B ^ { ( t ) } )$ is the number of transactions that contain itemset $ { \mathrm { ~  ~ \bar { ~ } { ~ \it ~ \{ ~ A ~ } ~ } ~ }  _ { \it { B } }   \} \tau$ with the constraint that A appears in the sth time period and B appears in the tth time period in the kth community. This type of time-weighted confidence is sensitive to any small change in user interest. The time weights in both the antecedent part and the consequent part change over time. $\tilde { w } _ { s } ^ { \mathrm { c o n f } } ( A )$ and $\tilde { w } _ { t } ^ { \mathrm { c o n f } } ( B )$ vary from 0 to 1 when s and t vary from the first time period to the last time period (TL). Accordingly, the accumulated weight product is close to 1 when $s = T L$ and $t = T L$ and is close to 0 when s = 1 and t = 1. Thus, this confidence can show the time effect of different rules well.

In conventional rule mining, the antecedent part of rules can be one item or more, but the time-weighted confidence is only fit for a 2-itemset. Therefore, this model transforms all rules into 2- itemsets and reduces the redundancy of traditional rules. The minimum time-weighted confidence is set at 0 because a higher minimum confidence can degrade the model’s performance, particularly in a spare data context. Table 3 shows the procedure for time-weighted rules mining.

## 3.3. Personalized recommendations

Because users can belong to more than one community, our proposed recommendation model considers the membership value of a user and the associated time-weighted rules in every community. The global recommendation value for a user is selected based on the ranking of all recommendations from his associated communities. The membership value of a user in a certain community is defined as the ratio of all of the user’s link weights in this community to the total link weights of the user in all his communities. The membership of the ith user in the kth community is defined as follows:

$$
m e m b _ {k} ^ {i} = \frac {\sum_ {l = 1} ^ {| C _ {k} |} u _ {i l}}{\sum_ {C _ {j} \in \{1 \dots C _ {p} \}} \sum_ {l ^ {\prime} = 1} ^ {| C _ {j} |} u _ {i l ^ {\prime}}}\tag{11}
$$

where $C _ { 1 }$ to $C _ { p }$ are all communities that contain the ith user. The element u calculates the degree of interest similarity between the ith user and the lth user. If the user is not in the community, memb<sup>i</sup> ¼ 0. The global recommendation value of the jth item to the ith user is defined as:

$$
R _ {i j} = \max \left\{m e m b _ {k} ^ {i} \times \max \left\{\text { Timecon } f _ {k} (x \rightarrow j) \right\}\right\}\tag{12}
$$

Table 3

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Frequent itemset  $Fset_{k}$  and dataset  $D_{k}$  for the kth community
Output: Association rules with time-weighted confidences in the kth community
Do for each itemset  $\{A, B\}$  in  $Fset_{k}$  that forms a rule ‘ $A \rightarrow B$ ’
1. Count the number of item A appearances ( $n_{k}^{\mathrm{sup}}(A)$ ) in  $D_{k}$ 
2. Count the number of  $\{A, B\}$  appearances ( $n_{k}^{\mathrm{sup}}(A^{(s)}, B^{(t)})$ ) in  $Fset_{k}$ 
3. Compute the time-decay weight for each month and conduct the normalization for all weights
4. Obtain the time-weighted confidence of ‘ $A \rightarrow B$ ’ using Eq. (10).
End
</div>

where x ! j denotes any rule whose consequent part is the jth item in the kth community. After ranking the recommendation values, a recommendation list for the target user can be generated using the Top-N recommendation strategy.

## 4. Experiments

## 4.1. Experiment design

In this section, we evaluate our proposed approach by running experiments using the MovieLens and Netflix datasets and comparing the results with those obtained using several existing methods. The MovieLens dataset contains approximately 1 million ratings from 6040 users on 3952 movies over three years. For the Netflix dataset, we choose a subset of ratings over two years (from 2004 to 2005) from the original released dataset, which contains approximately 30,000 ratings from more than 10,000 users on 1682 movies. We group user ratings into different months to evaluate the time effects on user interest changes. More specifically, we use six months of data as training data and one additional month of data as testing data, e.g., the training data range from January to June and the testing data are from July. According to the training/testing data segmentation, we can conduct 28 runs of every algorithm on the MovieLens dataset and 30 runs on the Netflix dataset. Each run contains a consecutive seven-month period of ratings. The movie ratings are on a scale of 1–5, with 5 being the highest rating. Given that we are only interested in the movies that users like, we code the ratings with scores of 3 or above to 1 (Like) and the rest to 0 (Dislike). The experimental parameter settings are listed in Table 4. The experimental data are separated into dense data and sparse data using the sparsity threshold of 0.985. $\theta _ { 2 } = 1 . 6 5$ is for dense data, and $\theta _ { 2 } = 3 0$ is for sparse data. These parameters are assigned based on sensitivity analysis. Note that the values of parameters $\rho _ { 1 }$ and $\rho _ { 2 }$ are assigned to satisfy the constraint of $\zeta \geq 1$

Our experiments adopt the Top-N recommendation strategy and use four evaluation metrics, namely, precision, recall, F-measure, and diversity. Then, the recommendations that users actually like are defined as True Positive (TP), and the others are defined as False Positive (FP). The items that are not recommended but that users actually like are defined as False Negative (FN), and the others are defined as True Negative (TN). To handle the data sparsity problem and to reflect the real performance of the algorithms [35,57], we filter out recommendations that do not have any corresponding ratings in the testing dataset. Thus, our Top-N recommendation list contains three parts: the number of True Positive, the number of False Positive, and the number of ignored recommendations (IR for short), that is, the total recommendation number $N = T P + F P + I R .$ . Then, the modified precision is calculated as follows:

$$
p r e c i s i o n = \frac {1}{n ^ {\prime}} \sum_ {i = 1} ^ {n ^ {\prime}} \frac {T P _ {i}}{T P _ {i} + F P _ {i}}
$$

where $T P _ { i } + F P _ { i }$ means the intersection of user-rated items and recommendations, $T P _ { i }$ means the intersection of user-liked items

(13)

Experimental parameter settings.

<table><tr><td>Parameter</td><td>MovieLens</td><td>Netflix</td></tr><tr><td> $\alpha$ </td><td>[1, 2]</td><td>[1, 2]</td></tr><tr><td> $\theta_1$ </td><td>[1, 240]</td><td>[1, 360]</td></tr><tr><td> $\theta_2$ </td><td>1.65/30</td><td>30</td></tr><tr><td> $\beta$ </td><td>0.5</td><td>0.95</td></tr><tr><td> $\rho_1$ </td><td>0.4</td><td>0.7</td></tr><tr><td> $\rho_2$ </td><td>0.9</td><td>0.9</td></tr></table>

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

Table 6  
Table 5  
Detailed information on the compared algorithms.

<table><tr><td>Recommendation category</td><td>Recommendation approach</td><td>Abbr.</td><td>Recommendation technique</td><td>Static/temporal</td></tr><tr><td>The proposed recommendation algorithm</td><td>Time-weighted AR with temporal overlapping community detection</td><td>TOTAR</td><td>· Time-weighted association rule mining· Temporal overlapping community partition</td><td>Temporal</td></tr><tr><td rowspan="4">Conventional recommendation approaches</td><td>AR-based recommendation algorithm</td><td>AR</td><td>· Association rule mining</td><td>Static</td></tr><tr><td>User-based collaborative filtering</td><td>UBCF</td><td>· Nearest neighbor (Pearson)</td><td>Static</td></tr><tr><td>Item-based collaborative filtering</td><td>IBCF</td><td>· Nearest neighbor (Pearson)</td><td>Static</td></tr><tr><td>Singular value decomposition with user implicit information</td><td>SVD++</td><td>· Singular value decomposition</td><td>Static</td></tr><tr><td rowspan="3">Recent proposed temporal recommendation approaches</td><td>Sequential pattern-based collaborative recommender system</td><td>SPCR</td><td>· GA-based clustering· Time-decaying sequential pattern mining</td><td>Temporal</td></tr><tr><td>Time-adaptive collaborative filtering</td><td>TACF</td><td>· Nearest neighbor (time-adaptive similarity to direct/indirect neighbor)</td><td>Temporal</td></tr><tr><td>Singular value decomposition model incorporating time changing interest</td><td>TimeSVD++</td><td>· Singular value decomposition· Time-aware factor model</td><td>Temporal</td></tr></table>

and recommendations, and n<sup>0</sup> is the user number of a selected user subset with the selection constraint of $T P _ { i } + F N _ { i } > 0 . \ : T P _ { i } + F N _ { i }$ is the number of all movies liked by the ith user during the testing months.

Accordingly, the recall metric is defined as follows:

$$
r e c a l l = \frac {1}{n ^ {\prime}} \sum_ {i = 1} ^ {n ^ {\prime}} \frac {T P _ {i}}{T P _ {i} + F N _ {i}}\tag{14}
$$

Generally, precision and recall are two diverging properties, and an increase in recall usually results in a decrease in the value for precision [19]. Thus, the F1 measure is proposed to find a suitable trade-off between precision and recall, and it is defined as

$$
F 1 = \frac {2 \times \text { precision } \times \text { recall }}{\text { precision } + \text { recall }}\tag{15}
$$

The metric of diversity is the number of distinct items recommended to all users [4].

$$
d i v e r s i t y = \left| \bigcup_ {i = 1, \dots , n} L _ {N} (i) \right|\tag{16}
$$

where $L _ { N } ( i )$ is the Top-N items in the recommendation list for the ith user, and n is the number of users.

We compare the proposed temporal model with several existing recommendation approaches. In addition to the conventional AR method, user-based collaborative filtering (UBCF) and item-based collaborative filtering (IBCF) are used for the comparison. A modified singular value decomposition, SVD++, which integrates with latent factor models and implicit user feedback, is also tested [23].

We also compare our results with some temporal recommendation algorithms proposed in the recent literature with some adjustments to fit our experiment/needs. Huang and Huang proposed the Sequential Pattern-based Collaborative Recommendation algorithm (SPCR), which predicted a user’s time-variant interest/purchase behavior [16]. This model first identifies the Top-M recommended classes among hierarchical-clustering classes and then obtains the Top-N recommendation of the M recommended classes for each person. The SPCR model has a constraint that the target users must make purchases at least once per month during the training period (three month horizon) to provide relatively sufficient information to identify sequential patterns. In our experiments, we developed the SPCR model using user ratings instead of transactions and followed the other system parameter settings mentioned in the original paper.

Rafeh and Bahrehmand proposed a Time-Adaptive Collaborative Filtering algorithm (TACF) to predict variations in users’ preferences [43]. The TACF considers different points of view, such as the number of rating items, rating values, rating time, and rating order, to calculate user similarities. The mean absolute error (MAE) is used in TACF as the recommendation evaluation metric, whereas our proposed algorithm adopts the Top-N recommendation strategy.

Precision of TOTAR and compared methods for MovieLens.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>0.1178</td><td>0.1713</td><td>0.2086</td><td>0.2344</td><td>0.2645</td><td>0.2811</td><td>0.2929</td></tr><tr><td>AR</td><td></td><td>0.1048</td><td>0.1479</td><td>0.1768</td><td>0.1984</td><td>0.2285</td><td>0.2552</td><td>0.2655</td></tr><tr><td></td><td>p</td><td>0.2816</td><td>0.1931</td><td>0.1433</td><td>0.1321</td><td>0.1586</td><td>0.2528</td><td>0.2506</td></tr><tr><td>UBCF</td><td></td><td>0.0324</td><td>0.0572</td><td>0.0772</td><td>0.0941</td><td>0.1222</td><td>0.1470</td><td>0.1713</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td></tr><tr><td>IBCF</td><td></td><td>0.0122</td><td>0.0308</td><td>0.0453</td><td>0.0578</td><td>0.0781</td><td>0.0990</td><td>0.1153</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SVD++</td><td></td><td>0.0522</td><td>0.0842</td><td>0.1156</td><td>0.1403</td><td>0.1776</td><td>0.2139</td><td>0.2387</td></tr><tr><td></td><td>p</td><td>0.0001</td><td>0.0000</td><td>0.0001</td><td>0.0001</td><td>0.0012</td><td>0.0102</td><td>0.0352</td></tr><tr><td>TimeSVD++</td><td></td><td>0.0556</td><td>0.0891</td><td>0.1187</td><td>0.1491</td><td>0.1895</td><td>0.2224</td><td>0.2512</td></tr><tr><td></td><td>p</td><td>0.0003</td><td>0.0001</td><td>0.0001</td><td>0.0004</td><td>0.0044</td><td>0.0217</td><td>0.0821</td></tr><tr><td>SPCR</td><td></td><td>0.0510</td><td>0.0794</td><td>0.0946</td><td>0.1088</td><td>0.1314</td><td>0.1489</td><td>0.1612</td></tr><tr><td></td><td>p</td><td>0.0004</td><td>0.0001</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td></tr><tr><td>TACF</td><td></td><td>0.0117</td><td>0.0206</td><td>0.0394</td><td>0.0610</td><td>0.1008</td><td>0.1387</td><td>0.1699</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td></tr></table>

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

H. Feng et al. / Information & Management xxx (2015) xxx–xxx

Table 7  
Recall of TOTAR and compared methods for MovieLens.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>0.0218</td><td>0.0363</td><td>0.0471</td><td>0.0554</td><td>0.0672</td><td>0.0749</td><td>0.0807</td></tr><tr><td>AR</td><td></td><td>0.0154</td><td>0.0256</td><td>0.0350</td><td>0.0419</td><td>0.0528</td><td>0.0636</td><td>0.0703</td></tr><tr><td></td><td>p</td><td>0.0301</td><td>0.0103</td><td>0.0194</td><td>0.0233</td><td>0.0489</td><td>0.1402</td><td>0.1914</td></tr><tr><td>UBCF</td><td></td><td>0.0027</td><td>0.0052</td><td>0.0076</td><td>0.0109</td><td>0.0159</td><td>0.0207</td><td>0.0272</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>IBCF</td><td></td><td>0.0017</td><td>0.0039</td><td>0.0055</td><td>0.0067</td><td>0.0106</td><td>0.0141</td><td>0.0179</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SVD++</td><td></td><td>0.0063</td><td>0.0114</td><td>0.0175</td><td>0.0228</td><td>0.0320</td><td>0.0427</td><td>0.0522</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0006</td></tr><tr><td>TimeSVD++</td><td></td><td>0.0072</td><td>0.0129</td><td>0.0184</td><td>0.0265</td><td>0.0373</td><td>0.0481</td><td>0.0583</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0004</td><td>0.0059</td></tr><tr><td>SPCR</td><td></td><td>0.0087</td><td>0.0141</td><td>0.0188</td><td>0.0230</td><td>0.0296</td><td>0.0363</td><td>0.0412</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>0.0020</td><td>0.0038</td><td>0.0064</td><td>0.0090</td><td>0.0161</td><td>0.0232</td><td>0.0313</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

Thus, we modified the final recommendation portion of the TACF by using the Top-N recommendation strategy. The other system parameters were set to the same values as in the original paper.

Koren proposed a singular value decomposition model that tracked time-changing behavior throughout the life span of the data (TimeSVD++) for Netflix Prize [22]. TimeSVD++ uses the SVD model, implicit information such as purchase history without scores, and temporal information. Because some temporal effects, such as one-day fluctuations, are not fit for the data, we use the TimeSVD++ model that Sahoo et al. modified to perform predictions for the next month [45]. Note that both TimeSVD++ and SVD++ were originally designed using the RMSE recommendation strategy, not Top-N recommendations. Thus, for comparison, we have modified the two algorithms to use the same Top-N strategy as TOTAR and the other comparison algorithms.

Table 5 summarizes the characteristics of the compared recommendation approaches.

## 4.2. Experimental results

We conduct experiments on MovieLens and Netflix datasets to assess the performance of the proposed algorithm compared with other methods via different values of N. We performed a statistical test with a significance level of 95%. The p-values of the t-test statistics were computed and are shown in the following tables. The results indicate the significance of the difference between TOTAR and the other algorithms in terms of precision, recall, F1, and diversity. The best performance for each Top-N recommendation strategy is outlined in bold.

Tables 6–9 show the average performances obtained by TOTAR and the compared algorithms on the MovieLens dataset.

As shown in Table 6, TOTAR performs better in precision than the other compared algorithms at different Ns for the MovieLens dataset, which indicates that both time weights and a temporal overlapping structure improve the performance of TOTAR. For example, TOTAR increases the precision by 15.82% compared with AR when N = 10 and by 10.32% when N = 50. Moreover, most of the compared algorithms are significantly worse than TOTAR, except AR, when N is not larger than 40. When N is set at a small value, such as 5, TOTAR performs 10 times better than TACF in terms of precision.

Table 7 shows that TOTAR performs best in term of recall among the eight algorithms with different Ns for the MovieLens dataset. The p-values indicate that TOTAR is significantly better in recall than the other algorithms, except AR. Furthermore, the recall obtained by TOTAR is 41.56% higher than that of AR when N is 5 and 14.79% higher than AR when N is 50.

Table 8 shows that TOTAR performs best among all of the compared algorithms in terms of F1. When N is 5, the F1 value of

F1 value of TOTAR and compared methods for MovieLens.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>0.0357</td><td>0.0587</td><td>0.0757</td><td>0.0885</td><td>0.1061</td><td>0.1174</td><td>0.1259</td></tr><tr><td>AR</td><td></td><td>0.0261</td><td>0.0427</td><td>0.0575</td><td>0.0684</td><td>0.0850</td><td>0.1010</td><td>0.1103</td></tr><tr><td></td><td>p</td><td>0.0388</td><td>0.0154</td><td>0.0232</td><td>0.0290</td><td>0.0590</td><td>0.1543</td><td>0.1966</td></tr><tr><td>UBCF</td><td></td><td>0.0047</td><td>0.0092</td><td>0.0134</td><td>0.0190</td><td>0.0276</td><td>0.0357</td><td>0.0463</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>IBCF</td><td></td><td>0.0025</td><td>0.00065</td><td>0.0094</td><td>0.0117</td><td>0.0182</td><td>0.0241</td><td>0.0305</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SVD++</td><td></td><td>0.0107</td><td>0.0194</td><td>0.0297</td><td>0.0385</td><td>0.0534</td><td>0.0701</td><td>0.0846</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td><td>0.0009</td></tr><tr><td>TimeSVD++</td><td></td><td>0.0121</td><td>0.0218</td><td>0.0312</td><td>0.0439</td><td>0.0612</td><td>0.0778</td><td>0.0933</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0006</td><td>0.0075</td></tr><tr><td>SPCR</td><td></td><td>0.0143</td><td>0.0235</td><td>0.0308</td><td>0.0374</td><td>0.0479</td><td>0.0580</td><td>0.0653</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>0.0031</td><td>0.0060</td><td>0.0104</td><td>0.0148</td><td>0.0267</td><td>0.0389</td><td>0.0517</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

H. Feng et al. / Information & Management xxx (2015) xxx–xxx

Table 9  
Table 11  
Diversity of TOTAR and compared methods for MovieLens.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>210.8</td><td>315.7</td><td>390.3</td><td>449.0</td><td>527.1</td><td>574.6</td><td>608.2</td></tr><tr><td>AR</td><td></td><td>95.93</td><td>126.4</td><td>143.8</td><td>154.0</td><td>164.1</td><td>167.2</td><td>168.2</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>UBCF</td><td></td><td>260.3</td><td>440.8</td><td>586.1</td><td>710.2</td><td>914.2</td><td>1081</td><td>1231</td></tr><tr><td></td><td>p</td><td>0.9612</td><td>0.9969</td><td>0.9995</td><td>0.9999</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>IBCF</td><td></td><td>396.0</td><td>678.0</td><td>896.0</td><td>1077</td><td>1362</td><td>1583</td><td>1765</td></tr><tr><td></td><td>p</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>SVD++</td><td></td><td>34.39</td><td>56.54</td><td>77.89</td><td>96.79</td><td>131.1</td><td>163.1</td><td>192.6</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TimeSVD++</td><td></td><td>27.64</td><td>46.93</td><td>63.61</td><td>79.86</td><td>107.1</td><td>133.2</td><td>157.9</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SPCR</td><td></td><td>22.14</td><td>37.89</td><td>51.67</td><td>64.64</td><td>87.39</td><td>108.2</td><td>126.5</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>89.50</td><td>152.1</td><td>205.2</td><td>253.9</td><td>339.6</td><td>414.0</td><td>428.3</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0005</td><td>0.0088</td></tr></table>

Table 10  
Precision of TOTAR and compared methods for Netflix.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>0.1820</td><td>0.2606</td><td>0.2883</td><td>0.2971</td><td>0.3030</td><td>0.3071</td><td>0.3075</td></tr><tr><td>AR</td><td></td><td>0.1610</td><td>0.2211</td><td>0.2417</td><td>0.2467</td><td>0.2475</td><td>0.2475</td><td>0.2475</td></tr><tr><td></td><td>p</td><td>0.0355</td><td>0.0008</td><td>0.0002</td><td>0.0001</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>UBCF</td><td></td><td>0.0437</td><td>0.0863</td><td>0.1124</td><td>0.1453</td><td>0.2098</td><td>0.2587</td><td>0.2941</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0001</td><td>0.1300</td></tr><tr><td>IBCF</td><td></td><td>0.0172</td><td>0.0317</td><td>0.0470</td><td>0.0630</td><td>0.0936</td><td>0.1256</td><td>0.1602</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SVD++</td><td></td><td>0.0909</td><td>0.1494</td><td>0.1915</td><td>0.2175</td><td>0.2993</td><td>0.3395</td><td>0.3695</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.4245</td><td>0.9492</td><td>0.9984</td></tr><tr><td>TimeSVD++</td><td></td><td>0.0909</td><td>0.1494</td><td>0.1919</td><td>0.2168</td><td>0.2989</td><td>0.3399</td><td>0.3714</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.4177</td><td>0.9515</td><td>0.9990</td></tr><tr><td>SPCR</td><td></td><td>0.1170</td><td>0.1625</td><td>0.1803</td><td>0.1964</td><td>0.2168</td><td>0.2239</td><td>0.2308</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>0.0163</td><td>0.0330</td><td>0.050</td><td>0.0724</td><td>0.1272</td><td>0.1843</td><td>0.2308</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

TOTAR is approximately 7 times higher than that of UBCF, approximately 14 times higher than IBCF, and approximately 11 times higher than TACF. When N is 50, SPCR only achieves 51.87% of the F1 obtained by TOTAR, and TimeSVD++ only reaches 74.11% of the F1 obtained by TOTAR. The average F1 value of TOTAR is always better than AR. Moreover, the recall value of TOTAR is much higher than that of AR. It is clear that the overlapping structure strongly increases the recall of association rules.

Recall of TOTAR and compared methods for Netflix.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>0.0929</td><td>0.1470</td><td>0.1684</td><td>0.1770</td><td>0.1807</td><td>0.1843</td><td>0.1849</td></tr><tr><td>AR</td><td></td><td>0.0760</td><td>0.1152</td><td>0.1332</td><td>0.1376</td><td>0.1383</td><td>0.1383</td><td>0.1383</td></tr><tr><td></td><td>p</td><td>0.0132</td><td>0.0002</td><td>0.0001</td><td>0.0001</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>UBCF</td><td></td><td>0.0178</td><td>0.0355</td><td>0.0497</td><td>0.0679</td><td>0.1084</td><td>0.1423</td><td>0.1702</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0478</td></tr><tr><td>IBCF</td><td></td><td>0.0060</td><td>0.0117</td><td>0.0173</td><td>0.0238</td><td>0.0368</td><td>0.0526</td><td>0.0729</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SVD++</td><td></td><td>0.0404</td><td>0.0727</td><td>0.0949</td><td>0.1110</td><td>0.1603</td><td>0.1883</td><td>0.2119</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0539</td><td>0.6210</td><td>0.9685</td></tr><tr><td>TimeSVD++</td><td></td><td>0.0404</td><td>0.0727</td><td>0.0954</td><td>0.1101</td><td>0.1604</td><td>0.1886</td><td>0.2129</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0551</td><td>0.6319</td><td>0.9747</td></tr><tr><td>SPCR</td><td></td><td>0.0602</td><td>0.0876</td><td>0.0968</td><td>0.1058</td><td>0.1212</td><td>0.1280</td><td>0.1338</td></tr><tr><td></td><td>p</td><td>0.0001</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>0.0077</td><td>0.0135</td><td>0.0235</td><td>0.0336</td><td>0.0620</td><td>0.0966</td><td>0.1257</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

H. Feng et al. / Information & Management xxx (2015) xxx–xxx

Table 12  
F1 value of TOTAR and compared methods for Netflix.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>0.1221</td><td>0.1875</td><td>0.2128</td><td>0.2213</td><td>0.2259</td><td>0.2299</td><td>0.2304</td></tr><tr><td>AR</td><td></td><td>0.1024</td><td>0.1507</td><td>0.1710</td><td>0.1760</td><td>0.1767</td><td>0.1767</td><td>0.1767</td></tr><tr><td></td><td>p</td><td>0.0155</td><td>0.0002</td><td>0.0001</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>UBCF</td><td></td><td>0.0245</td><td>0.0495</td><td>0.0682</td><td>0.0918</td><td>0.1422</td><td>0.1831</td><td>0.2150</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0597</td></tr><tr><td>IBCF</td><td></td><td>0.0080</td><td>0.0161</td><td>0.0244</td><td>0.0336</td><td>0.0520</td><td>0.0733</td><td>0.0996</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SVD++</td><td></td><td>0.0547</td><td>0.0968</td><td>0.1260</td><td>0.1462</td><td>0.2078</td><td>0.2414</td><td>0.2685</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.1149</td><td>0.7756</td><td>0.9875</td></tr><tr><td>TimeSVD++</td><td></td><td>0.0547</td><td>0.0968</td><td>0.1265</td><td>0.1453</td><td>0.2078</td><td>0.2418</td><td>0.2698</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.1161</td><td>0.7839</td><td>0.9907</td></tr><tr><td>SPCR</td><td></td><td>0.0779</td><td>0.1126</td><td>0.1250</td><td>0.1366</td><td>0.1546</td><td>0.1620</td><td>0.1685</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>0.0096</td><td>0.0181</td><td>0.0311</td><td>0.0450</td><td>0.0827</td><td>0.1262</td><td>0.1621</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

Table 9 records the diversity obtained by the compared algorithms. IBCF performs best among the compared algorithms. However, TOTAR’s diversity is much higher than AR, SVD++, TimeSVD++, SPCR, and TACF, which indicates that TOTAR shows a good ability to obtain diverse recommendations.

Generally, higher diversity resultsin lower precision and F1 values in recommendations, and IBCF, which achieves the highest diversity, performs worse than the others. TOTAR achieves high accuracy and also yields diversity based on the average level of the compared methods. Thus, TOTAR performs best for the MovieLens dataset.

Tables 10–13 show the average precision, recall, F1, and diversity obtained by TOTAR and the other compared algorithms for the Netflix dataset.

Table 10 shows that TOTAR performs best in terms of precision among the eight algorithms when N is less than 40 and performs better than most of the compared algorithms, except TimeSVD++ and SVD++, when N is set at 40 and 50. When shown as p-values, TOTAR achieves significantly higher precision than AR, UBCF, SPCR, and TACF.

Table 11 records the recall performance for Netflix. TOTAR significantly achieves the highest recall among the compared algorithms when N is less than 40. When N is 40 or 50, TimeSVD++ and SVD++ outperform TOTAR.

Table 12 shows the F1 values obtained by the algorithms. TOTAR performs best among the compared algorithms when N is less than 40. TimeSVD++ and SVD++ outperform TOTAR when N equals 40 and 50. The F1 value of TOTAR is 85.40% of that of TimeSVD++ when N = 40, whereas TOTAR produces an F1 that is 2.23 times higher than that of TimeSVD++ when N = 5.

Table 13 shows the diversity of all of the compared algorithms for Netflix.

The results indicate that IBCF achieves the highest diversity for the Netflix dataset. TOTAR performs third best and achieves significantly higher diversity than AR, SVD++, TimeSVD++, and SPCR. Moreover, although TimeSVD++ performs better than TOTAR in terms of precision and recall when N = 40 or N = 50, it achieves much lower diversity compared with TOTAR. TOTAR’s diversity is 9.53 times as high as that of TimeSVD++ when N = 5.

To summarize, TOTAR achieves both high accuracy and high diversity for the two datasets.

Table 13  
Diversity value of TOTAR and compared methods for Netflix.

<table><tr><td>Algorithm</td><td></td><td>Top5</td><td>Top10</td><td>Top15</td><td>Top20</td><td>Top30</td><td>Top40</td><td>Top50</td></tr><tr><td>TOTAR</td><td></td><td>82.90</td><td>123.7</td><td>151.9</td><td>171.2</td><td>193.5</td><td>202.4</td><td>205.6</td></tr><tr><td>AR</td><td></td><td>23.80</td><td>27.60</td><td>28.10</td><td>28.10</td><td>28.10</td><td>28.10</td><td>28.10</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>UBCF</td><td></td><td>139.7</td><td>222.1</td><td>281.1</td><td>322.7</td><td>377.1</td><td>414.6</td><td>439.3</td></tr><tr><td></td><td>p</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>IBCF</td><td></td><td>206.0</td><td>333.3</td><td>416.0</td><td>469.9</td><td>533.6</td><td>562.6</td><td>575.0</td></tr><tr><td></td><td>p</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>SVD++</td><td></td><td>8.700</td><td>15.87</td><td>23.17</td><td>29.90</td><td>43.60</td><td>56.60</td><td>69.83</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TimeSVD++</td><td></td><td>8.700</td><td>15.97</td><td>23.20</td><td>29.87</td><td>43.57</td><td>56.47</td><td>69.73</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>SPCR</td><td></td><td>17.43</td><td>30.53</td><td>43.27</td><td>55.60</td><td>77.07</td><td>98.03</td><td>116.40</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TACF</td><td></td><td>56.37</td><td>93.10</td><td>122.4</td><td>149.0</td><td>190.6</td><td>225.2</td><td>251.6</td></tr><tr><td></td><td>p</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0035</td><td>0.4365</td><td>0.9944</td><td>1.0000</td></tr></table>

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

## 5. Conclusions and future work

In this paper, we proposed a new recommendation approach called TOTAR, which is based on time-weighted overlapping community detection and association rule mining. A number of innovative approaches to incorporate time effects have been proposed in TOTAR to better capture and predict users’ dynamic interests over time. Two datasets from MovieLens and Netflix were used to compare TOTAR with several existing approaches. The experimental results show that TOTAR outperforms other existing algorithms in accuracy and diversity.

We can extend this study in a number of directions. In community detection, the selection strategy of the start nodes, i.e., the seeding strategy, often affects the final community structure and partition. We intend to introduce new seeding strategies such as starting the community detection process from a group of nodes, which would allow for more diversified and explorative searching. User interest shows a clear presence of a long tail that separates interests into long term and short term. We will consider the longtail effect in user interest drift and modify the calculation of granularity within different time periods, such as five years or more, which will allow the proposed model to capture both users’ recent changeable interests and seasonal/permanent changes in preferences. Finally, similar dislikes among users also contain some important information that should be fully considered in recommendations. Thus, we will attempt to depict information about users’ similar dislikes to improve the interest model.

## Acknowledgements

This work was partially supported by the National Science Fund for Distinguished Young Scholars of China (Grant No. 70925005), the General Program of the National Science Foundation of China (Grant Nos. 71471127, 71371135, 71001076, 71101103, and 71271149), and a JP Morgan Chase Fellowship from the Institute for Financial Services Analytics at the University of Delaware.

## References

[1] A.S. Abrahams, W. Fan, J. Jiao, G.A. Wang, Z. Zhang, An integrated text analytic framework for product defect discovery, Product. Operat. Manag. 2014, http:// dx.doi.org/10.1111/poms.12303, (in press).

[2] A.S. Abrahams, J. Jiao, W. Fan, G.A. Wang, Z. Zhang, What is buzzing in the blizzard of buzz: automotive component isolation in social media postings, Decis. Support Syst. 55 (4), 2013, pp. 871–882.

[3] A.S. Abrahams, J. Jiao, G.A. Wang, W. Fan, Vehicle defect discovery from social media, Decis. Support Syst. 54 (1), 2012, pp. 87–97.

[4] G. Adomavicius, Y.O. Kwon, Improving aggregate recommendation diversity using ranking-based techniques, IEEE Trans. Knowl. Data Eng. 24 (5), 2012, pp. 896–911.

[5] G. Adomavicus, R. Sankaranarayanan, S. Sen, A. Tuzhilin, Incorporating contextual information in recommender systems using a multidimensional approach, ACM Trans. Inf Syst, 23 (1) 2005 pp. 103–145.

[6] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions IEEE Trans. Knowl. Data Eng, 17 (6) 2005 pp. 734–749.

[7] H.Y. Bao, Q.D. Li, S.S.Y. Liao, S.Y. Song, H. Gao, A new temporal and social PMFbased method to predict users’ interests in micro-blogging, Decis. Support Syst. 55 (3), 2013, pp. 698–709.

[8] C. Birtolo, D. Ronca, Advances in clustering collaborative filtering by means of fuzzy C-means and trust, Expert Syst. Appl. 40 (17), 2013, pp. 6997–7009.

[9] L. Cagliero, Discovering temporal change patterns in the presence of taxonomies IEEE Trans. Knowl. Data Eng. 25 (3), 2013, pp. 541–555.

[10] Y.S. Chen, M.H. Kuo, A study of minimum support value in association analysisfrom Bavesian viewpoint. in: Proceedings of the Fifth Asia Pacific Industrial Engineering and Management Systems Conference, Gold Coast, Australia, December, 2004, pp. 1–11.

[11] M.A. Domingues, A.M. Jorge, C. Soares, Dimensions as virtual items: improving the predictive ability of top-N recommender systems, Inf. Process. Manag. 49 (3), 2013, pp. 698–720.

[12] W. Fan, M.D. Gordon, The power of social media analytics, CACM 57 (6), 2014, pp. 74–81.

[13] R. Forsati, M.R. Meybodi, Effective page recommendation algorithms based on distributed learning automata and weighted association rules, Expert Syst. Appl. 37 (2), 2010, pp. 1316–1330.

[14] S. Fortunato, Community detection in graphs, Phys. Rep. 486 (3–5), 2010, pp. 75–174

[15] P. Georgios, Discovery of Web user communities and their role in personalization User Model. User-Adapt. Interact. 22 (1/2), 2012, pp. 151–175.

[16] C.L. Huang, W.L. Huang, Handling sequential pattern decay: developing a twostage collaborative recommender system, Electron. Commer. Res. Appl. 8 (3) 2009, pp. 117–129.

[17] Y.C. Jiang, J. Shang, Y.Z. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classification model, Decis. Support Syst. 48 (3), 2010, pp. 470–479.

[18] H.C. Joong, H.P. Nam, Comparative analysis of sequence weighting approaches for mining time-interval weighted sequential patterns, Expert Syst. Appl. 39 (3), 2012, pp. 863–873.

[19] A.A. Kardan, M. Ebrahimi, A novel approach to hybrid recommendation systems based on association rules mining for content recommendation in asynchronous discussion groups, Inf. Sci. 219, 2013, pp. 93–110.

[20] N. Koenigstein, G. Dror, Y. Koren, Yahoo! music recommendations: modeling music ratings with temporal dynamics and item taxonomy in: Proceedings of the Fifth ACM Conference on Recommender Systems, Chicago, USA, November, 2011, pp. 165–172.

[21] J. Koh, Y.G. Kim, B. Butler, G.W. Bock, Encouraging participation in virtual communities, CACM 2 (50), 2007, pp. 68–73.

[22] Y. Koren, Collaborative filtering with temporal dynamics, CACM 53 (4), 2010, pp. 89–97.

[23] Y. Koren, Factorization meets the neighborhood: a multifaceted collaborative filtering model, in: Proceedings of the 14th ACM SIGKDD International Confer ence on Knowledge Discovery and Data Mining, Las Vegas, USA, August, 2008, pp. 426–434.

[24] A. Lancichinetti, S. Fortunato, Limits of modularity maximization in community detection, Phys. Rev. E 84 (6), 2011, p. 066122.

[25] A. Lancichinetti, S. Fortunato, J. Kertesz, Detecting the overlapping and hierarchical community structure in complex networks, New J. Phys. 11 (3), 2009, p. 033015

[26] A.J.T. Lee, Y.A. Chen, Mining frequent trajectory patterns in spatial–temporal databases, Inform. Sci. 179 (13), 2009, pp. 2218–2231

[27] T.Q. Lee, Y. Park, Y.T. Park, A time-based recommender system using implicit feedback, Expert Syst. Appl. 4 (34), 2008, pp. 3055–3062.

[28] C. Lee, F. Reid, A. McDaid, N. Hurley, Seeding for pervasively overlapping communities, Phys. Rev. E 83 (6), 2011, p. 066107.

[29] C. Lee, F. Reid, A. McDaid, N. Hurley, Detecting highly overlapping community structure by greedy clique expansion, In Proceedings of the 4th Workshop on Social Network Mining and Analysis held in Conjunction with the International Conference on Knowledge Discovery and Data Mining (SNA/KDD’10), Washington, DC, USA, July, 2010, pp. 33–42.

[30] Y.J. Li, P. Ning, X.S. Wang, J. Sushil, Discovering calendar-based temporal association rules, Data Knowl. Eng. 44 (2), 2003, pp. 193–218.

[31] W.Y. Lin, Efficient adaptive-support association rule mining for recommender systems, Data Min. Knowl. Discov. 6 (1), 2002, pp. 83–105.

[32] H. Lin, W. Fan, P. Chau, Determinants of users’ continuance of social networking sites: a self-regulation perspective, Inform. Manag. 51 (5), 2014, pp. 595–603.

[33] J. Liu, G.S. Deng, Link prediction in a user-object network based on time-weighted resource allocation, Phys. A 388 (17), 2009, pp. 3643–3650.

[34] D.R. Liu, C.H. Lai, W.J. Lee, A hybrid of sequential rules and collaborative filtering for product recommendation, Inform. Sci. 179 (20), 2009, pp. 3505–3519.

[35] J.G. Liu, T. Zhou, Q. Guo, B.H. Wang, Overview of the evaluated algorithms for personal recommendation systems, Complex Syst. Complex. Sci. 6 (3), 2009, pp. 1–10.

[36] M.O. Mahony, N. Hurley, N. Kushmerick, G. Silverstre, Collaborative recommendations: a robustness analysis, ACM Trans. Internet Technol. 4 (4), 2004, pp. 344–377.

[37] L. Martı´nez, M.J. Barranco, L.G. Pe´reza, M. Espinilla, A knowledge based recommender system with multigranular linguistic information Int. I. Comput. Intell Svst. 1 (3) 2008 pp. 225-236.

[38] B. Mobashe, Web usage mining and personalization, in: P.S. Munindar (Ed.), Practical Handbook of Internet Computing, CRC Press, 2005, pp. 264–265.

[39] M.E.J. Newman, Fast algorithm for detecting community structure in networks Phys. Rev. E 69 (6), 2004, p. 066133.

[40] G. Palla, I. Derenyi, I. Farkas, T. Vicsek, Uncovering the overlapping community structures of complex networks in nature and society, Nature 435 (7043), 2005 pp. 814-818.

[41] D.M. Pasquale, F. Emilio, F. Giacomo, P. Alessandro, Enhancing community detection using a network weighting strategy, Inform. Sci. 222 (2), 2013, pp. 648–668.

[42] I. Psorakis, S. Roberts, M. Ebden, Overlapping community detection using Bayesian non-negative matrix factorization, Phys. Rev. E 83 (6), 2011, p. 066114.

[44] J.J. Ramasco, S.A. Morris, Social inertia in collaboration networks, Phys. Rev. E 73 (1), 2006, p. 016022.

[45] N. Sahoo, P.V. Singh, T. Mukhopadhyay, A hidden Markov model for collaborative filtering, MIS Q. 36 (4), 2012, pp. 1329–1356.

[46] R.LL, Sie, H. Drachsler, M. Bitter-Riipkema, P. Sloep, To whom and why should I connect? Co-author recommendation based on powerful and similar peers Int. J. Technol. Enhanc. Learn. 4 (1), 2012, pp. 121–137.

[47] A. Tsymbal, The Problem of Concept Drift: Definitions and Related Work, Computer Science Department, Trinity College Dublin, 2004.

[48] F.H. Wang, H.M. Shao, Effective personalized recommendation based on timeframed navigation clustering and association mining, Expert Syst. Appl. 27 (3), 2004, pp. 365–377.

Please cite this article in press as: H. Feng, et al., Personalized recommendations based on time-weighted overlapping community detection, Inf. Manage. (2015), http://dx.doi.org/10.1016/j.im.2015.02.004

[49] G.A. Wang, J. Jiao, A.S. Abrahams, W. Fan, Z. Zhang, ExpertRank: a topic-aware expert finding algorithm for online knowledge communities, Decis. Support Syst. 54 (3), 2013, pp. 1442–1451.

[50] Y.P. Wang, Research on Overlapping Community Detection in Complex Networks, Taiyuan University of Technology, Taiyuan, 2011.

[51] L. Xiang, Q. Yuan, S. Zhao, L. Chen, X.T. Zhang, Q. Yang, J.M. Sun, Temporal recommendation on graphs via long-and short-term preference fusion, in: Proceedings of the 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2010.

[52] K.M. Yu, J.Y. Zhou, Parallel TID-based frequent pattern mining algorithm on a PC Cluster and grid computing system, Expert Syst. Appl. 37 (3), 2010, pp. 2486–2494.

[53] U. Yun, A new framework for detecting weighted sequential patterns in large sequence databases, Knowl.-Based Syst. 21 (2), 2008, pp. 110–122.

[54] A. Zeng, S. Gualdi, M. Medo, Y.C. Zhang, Trend prediction in temporal bipartite networks: the case of Movielens, Netflix, and Digg, Adv. Complex Syst. 16 (04n05), 2013, pp. 1–15.

[55] M. Zhou, L. Lei, J. Wang, A.G.A. Wang, W. Fan, Social media adoption and corporate disclosure, J. Inf. Systems 2014, http://dx.doi.org/10.2308/isys-50961, (in press).

[56] T. Zhou, J. Ren, M. Medo, Y.C. Zhang, Bipartite network projection and personal recommendation, Phys. Rev. E 76 (4), 2007, p. 046115.

[57] X.Y. Zhu, L.Y. Lu, Evaluation metrics for recommender systems, J. Univ. Electron. Sci. Technol. China 41 (2), 2012, pp. 163–174.

![](/api/attachments/6GQH5HZ7/fulltext/images/d1a50783bb554e7f2ae939f576e35aea99da1cc03bf3bbe7b66cd52f344602eb.jpg)  
Haoyuan Feng is a Ph.D. candidate in Management Science and Engineering, College of Management and Economics, Tianjin University. He received B.S. in Electronic Commerce from Tianjin University, Tianjin, P. R. China, in 2012. His research interests include personalized recommendation, data mining, and community detection.

![](/api/attachments/6GQH5HZ7/fulltext/images/90a9e33e596e9add57f05977c9027f6b25e9cb08ad32447a12db34f157765452.jpg)  
Jin Tian is an Associate Professor in the Department of Information Management and Management Science, College of Management and Economics, Tianjin University. She received the Ph.D. degree in Management Science and Engineering from Tianjin University, Tianjin, P. R. China, in 2008. Her major research interests include recommender systems, business intelligence, data mining, and evolutionary computation.

She has published papers in academic journals, such as IEEE Transactions on Neural Networks and Learning Systems, Pattern Recognition, Expert Systems with Applications, and Neural Computing & Applications. She is a current member of the Association fo Information Systems.

![](/api/attachments/6GQH5HZ7/fulltext/images/8529e16cd7356164c529781997ecbe5e06e5685b72fe442c6556a11cb867cbb7.jpg)

![](/api/attachments/6GQH5HZ7/fulltext/images/d3206b74009b523748b279cec0a4033ddc4d7e35b273b90bb71b481bd99757f5.jpg)

Harry Jiannan Wang is an Associate Professor of Management Information Systems (MIS) and JPMorgan Chase Fellow in the Lerner College of Business and Economics, University of Delaware. He received Ph.D. in MIS from the Eller College of Management, University of Arizona, USA and B.S. in MIS from Tianjin University, China. His research interests involve business process management, business analytics and intelligence, services computing, and enterprise systems. He has published research articles in journals, such as Information Systems Research, Decision Support Systems, ACM Transactions on Management Information Systems, Journal of Database Management, and Information Technology and Management. Dr. Wang has serviced as associate editor, special issue guest editor, and editorial board member for several journals and organized the 2014 Workshop on business Processes and Service and the 2013 China Summer Workshop on Information Management as a conference co-char. He has also been a program cochair, program committee member, and track co-chair for numerous conferences.

Minqiang Li is a Professor in the Department of Information Management and Management Science, College of Management and Economics, Tianjin University. He received the Ph.D. degree in Systems Engineering and Management Science from Tianjin University, Tianjin, P. R. China, in 2000. His major research interests include management science and decision support, IT strategy, electronic commerce, evolutionary computation, data mining, and intelligent systems. He has published papers in academic journals and conferences, such as the Pattern Recognition, European Journal of Operational Research, Journal of Heuristics, Knowledge-Based Systems, Information Sciences, Applied Soft Computing, Neural Computing & Applications, Expert Systems with Applications, etc. He is a Chinese member of the Association for Information Systems.
