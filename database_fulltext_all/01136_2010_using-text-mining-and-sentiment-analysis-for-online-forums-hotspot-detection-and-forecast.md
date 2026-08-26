---
otero_id: 1136
otero_key: "H4MRZRTZ"
title: "Using text mining and sentiment analysis for online forums hotspot detection and forecast"
authors: "Nan Li; Desheng Dash Wu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.09.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using text mining and sentiment analysis for online forums hotspot detection and forecast

Nan Li <sup>a</sup>, Desheng Dash Wu <sup>b,c,</sup>⁎

<sup>a</sup> Department of Computer Science, University of California, Santa Barbara, USA

<sup>b</sup> Reykjavík University, Iceland

<sup>c</sup> RiskLab, University of Toronto, Canada

## a r t i c l e i n f o

Article history: Received 15 July 2008 Received in revised form 8 September 2009 Accepted 17 September 2009 Available online 24 September 2009

Keywords: Text mining Sentiment analysis Cluster analysis Online sports forums Dynamic interacting network analysis Hotspot detection Machine learning Support vector machine

## a b s t r a c t

Text sentiment analysis, also referred to as emotional polarity computation, has become a <sup>fl</sup>ourishing frontier in the text mining community. This paper studies online forums hotspot detection and forecast using sentiment analysis and text mining approaches. First, we create an algorithm to automatically analyze the emotional polarity of a text and to obtain a value for each piece of text. Second, this algorithm is combined with K-means clustering and support vector machine (SVM) to develop unsupervised text mining approach. We use the proposed text mining approach to group the forums into various clusters, with the center of each representing a hotspot forum within the current time span. The data sets used in our empirical studies are acquired and formatted from Sina sports forums, which spans a range of 31 different topic forums and 220,053 posts. Experimental results demonstrate that SVM forecasting achieves highly consistent results with K-means clustering. The top 10 hotspot forums listed by SVM forecasting resembles 80% of K-means clustering results. Both SVM and K-means achieve the same results for the top 4 hotspot forums of the year. © 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

In the Internet and information Age, online data usually grows in an exponential explosive fashion. The majority of these web data is in unstructured text format that is dif<sup>fi</sup>cult to decipher automatically. Other than static WebPages, unstructured or loosely formatted texts often appears at a variety of tangible or intangible dynamic interacting networks [2,4,16,34]. A variety of heterogeneous online communities, societies and forums embody the interacting networks nowadays. When faced with tremendous amounts of online information from various online forums, information seekers usually <sup>fi</sup>nd it very dif<sup>fi</sup>cult to yield accurate information that is useful to them. This has motivated the research on identi<sup>fi</sup>cation of online forum hotspots, where useful information are quickly exposed to those seekers. Our research is to provide a comprehensive and timely description of the interacting structural natural groupings of various forums, which will dynamically enable ef<sup>fi</sup>cient detection of hotspot forums, thus bene<sup>fi</sup>t Internet social network members in the decision making process.

As ef<sup>fi</sup>cient business intelligence methods, data mining and machine learning provide alternative tools to dynamically process large amounts of data available online. Another most recent technique called sentiment analysis, also referred to as emotional polarity computation, has always been simultaneously employed when conducting online text mining. The purpose of text sentiment analysis is to determine the attitude of a speaker or a writer with respect to some speci<sup>fi</sup>c topic. The attitude can be any forms of judgment or evaluation, the emotional state of the author when writing, or the intended emotional communication. It is recognized that the performance of sentiment classi<sup>fi</sup>ers are dependent on domains or topics [22].

In this paper, online forums hotspot detection and forecast are studied using sentiment analysis and text mining approaches. We develop this approach in two stages: emotional polarity computation and integrated sentiment analysis based on K-means clustering and support vector machine (SVM).The proposed unsupervised text mining approach is used to group the forums into various clusters, with the center of each representing a hotspot forum within the current time span. Data are collected from Sina sports forums (webite: http://bbs. sports.sina.com.cn/treeforum/App/list.php?bbsid=33&subid=0), which include a range of 31 different topic forums and 220,053 posts. Computation indicates that within the same time window, SVM forecasting achieves highly consistent results with K-means clustering.

The rest of the paper is organized as follows. Section 2 discusses related work of our study. Section 3 presents models and methodology. Empirical results and discussion are given in Section 4. Finally, Section 4 concludes the paper.

## 2. Related work

This section investigates three streams of related work: dynamic cluster analysis of online forums, sentiment analysis of web documents and web text mining using machine learning.

## 2.1. Dynamic cluster analysis of online forums

Online forums are usually related to each other due to two reasons. First, strong commonalities are shared by forums with similar topics or themes. For example, within an entertainment society, the Academy Awards forum might be highly correlated to the Golden Globes Award forum. Secondly, emerging events will trigger a temporary correlation between certain forums. For example, the movie “No Country for Old Men” won “Best Motion Picture of the Year” in the 2008 Academy Awards, which rendered noticeable connections between the corresponding forums during the Oscar season. We aim to study the second inter-forum correlation and propose a mathematical approach to dynamically capture, describe and predict these time-varying correlations.

Extensive research work has been conducted upon various types of interacting social networks such as dynamic networks upon individuals, industrial manufacturers, listed companies, and online virtual communities [2,4,16,34,41–43]. One pioneer work from the Doctoral Thesis of Asavathiratham at MIT in 1996 [2] created an in<sup>fl</sup>uence model as a tractable representation for the dynamics of networked Markov chains. This work has been utilized by several scholars, e.g., [4], where tools are developed to automatically and unobtrusively learn the social network structure that arises within a human group based on wearable sensors. [34] chose 662 main ceramic manufacturers in Guangdong Foshan ceramic industry cluster to construct a Competition Relationship Network (CRN) and proved that the network de<sup>fi</sup>ned by competition relationship is a highly clustered scale-free network. Besides, correlated listed company network in stock markets constitutes another important research area in both academia and industry [42,43]. Regarding network dynamics of online virtual societies and communities, [16] proposed a relationship algebra used for various interesting computations on a social network weaved in the virtual communities.

It is observed that limited work was done to depict timely dynamics of online sports communities. Online sports forums within a virtual society are the focus of our study, where machine learning is used to dynamically depict the interacting structure and to cluster the forums according to their emotional polarity.

## 2.2. Sentiment analysis of web documents

There are a variety of metrics to classify web documents, including topics, structures, authors, time and so forth. Text classi<sup>fi</sup>cation based on its emotional polarity has become a newly-emerged frontier appealing to the web mining community. To illustrate how it works, suppose you are considering a vacation in city C, you might use a search engine online such as Google, and shoot the query “C”. It would be handy to know what fraction of the matches Google returns recommends C as a travel destination [18]. Incorporating sentiment analysis into search engine and text retrieval technologies enables a more ef<sup>fi</sup>cient and functional service for users [45]. Sentiment analysis has been utilized in applications such as news tracking and summarizing, online forums, <sup>fi</sup>le sharing, chatting rooms, blogging etc. Youtube introduced sentiment classi<sup>fi</sup>cation technology early this year to categorize all its comments into “Poor” or “Good” [44].

As a promising research area, text sentiment analysis has been extensively studied [1,3,26–28,33,35], where sentiment analysis is used for text classi<sup>fi</sup>cation tasks [8,13,14,40]. Existing sentiment calculation approaches fall into two types: machine learning based approach [3,33] and semantic orientation based approach [1,26–28,33,35]. Languages that have been studied include English [3,13,26–28], Chinese [33,35] and Arabic [1]. Our research aims to further extend the application of text sentiment analysis into cluster analysis for network dynamics of online communities, preliminarily Chinese sports forums.

## 2.3. Web text mining using machine learning

To conduct clustering and forecasting of online forum hotspots, we use two machine learning approaches: K-means and SVM. K-means has been studied and applied in a wide range of domains, e.g., bioinformatics [10–12,39], information security [36], pattern recognition [6,7,19], text classi<sup>fi</sup>cation [22]. In addition, various derivatives of conventional K-means algorithm have been developed [5,9,31]. Based on statistical learning, SVM is able to overcome problems such as over-<sup>fi</sup>tting and local minimum to achieve high generalization [21,29,30,37,38]. Application of SVM includes text classi<sup>fi</sup>cation [15], image processing [24], and time series analysis [25,32]. In our study, machine learning is the key bridge between emotional polarity data and network dynamics. All the forums of Sina sports community form our research targets, each one of which will be converted into a vector representing its user attention within the current time window, in forms of number of posts and average value of sentiment. Those vectors acquired after feature extraction will be fed into the machine learning models for both clustering and forecasting.

## 3. Models and methodology

Our approach is mainly composed of the following steps: data collection and cleansing, text sentiment calculation and marking, hotspot detection based on K-means clustering and hotspot forecast based on SVM classi<sup>fi</sup>cation. Fig. 1 depicts the conceptual diagram of our approach, where three modules are de<sup>fi</sup>ned to integrating text sentiment calculation, K-means and SVM for analyzing forum hotspots.

Module 1 is to convert Chinese texts into value based data through text sentiment computation and analysis. In this module, a new key word based approach is introduced to calculate the sentiment value for each piece of text by use of the commercial Java library developed by Lietu Enterprise Search and the HowNet lexicons. Our approach will yield an integer value for each post, with the sign showing its emotional polarity and the absolute value its emotional intensity.

Based on the sentimental values from Module 1. Module 2 applies K-means into all the forums of Sina sports community to calculate cluster values in each period, i.e., t1, t2,…tT, where T is the length of time cycle under consideration. In our K-means module, there are <sup>fi</sup>ve inputs: The number of topic posts, the average number of responses of topic posts, the average text sentiment value of topic posts, the proportion of positive posts among all the topic posts and the proportion of negative posts among all the topic posts. Hotspot forums are identi<sup>fi</sup>ed by K-means as those closest to th theoretical centers of those clusters. This route generally follows previous work [30,31]. Module 2 is SVM-based classi<sup>fi</sup>cation module, which utilizes forum performance-related data and yielded cluster values to train machine learning model and apply the trained machine learning model to new forums for hotspot identi<sup>fi</sup>cation. K-means clustering results are fed into SVM model as the supervised learning outputs. As can be seen, our integrated approach differs from existing sentiment calculation work, which is either based on machine learning [3,33] or semantic orientation [1,26–28,33,35]. In fact, we aggregate both semantic orientation and machine learning tools and further extend the application of text sentiment analysis into cluster analysis for network dynamics of online communities. This unique approach also combines the Lietu Enterprise Search Java library and the HowNet lexicons, which are applied to a unique problem of Chinese sports forums detection and prediction.

![](/api/attachments/H4MRZRTZ/fulltext/images/528f9ff15ce97526f184afcadfe468842407f16f919feabb65d5789c0a4acfd2.jpg)  
Fig. 1. Conceptual diagram of our approach.

## 3.1. Data collection

Before data crawling and cleansing process are initiated, a comprehensive view of the structure of Sina sports community is necessary. Online Sina sports community exhibits a tree-like structure with root forums, branch forums and a nonseparable bottom layer of leaf forums. There are in total 49 leaf forums for this community. Fig. 2 illustrates the tree-like structure of the Sina sports community, where the root node, red circle node and yellow rectangular node represent the whole community, the <sup>fi</sup>rst layer forums and the leaf forums respectively.

We proceed with the data crawling and cleansing process in the following four steps:

Step 1. Manually create table SINA\_LEAFORUM\_URLLIST

In this step, we manually store the information for all the 49 forums into a table named SINA\_LEAFORUM\_URLLIST in the database, where their names and URL links are contained.

Step 2. Create table SINA\_FORUM\_URL based on SINA\_LEAFORUM\_URLLIST

After the acquisition of the links for all the leaf forums, we parse the <sup>fi</sup>rst pages of them in depth and generate a list of URLs of web pages that contain all the topic posts and the comment posts. The list will be written into the SINA\_FORUM\_URL table in the database.

Step 3. Traverse the links in the SINA\_FORUM\_URL table and crawl down all the posts

This step is to traverse through all the links that are in the SINA FORUM URL table. to parse out all the topic and comment posts contained on the corresponding web pages, and to store them into two tables of SINA\_FORUM\_TOPIC\_POST and SINA\_FORUM\_COMMENT\_POST. Two parsing templates are designed in XML format to parse the posts, which are SinaSportForumReplyPostParseTemplate.xml and SinaSportForumTopicPostParseTemplate xml. Fig, 3 demonstrates the crawling procedure and the structures of the relational tables and the XML templates, where the green highlighted item in the tables are the primary keys.

![](/api/attachments/H4MRZRTZ/fulltext/images/47981546228a514d06558c5f7af7b812074615f1892eab2861516fce73bfcfc7.jpg)  
Fig. 2. The tree-like structure of Sina sports community.

## Step 4. Data cleansing

When the crawling process is accomplished, data cleansing process is applied to the downloaded post sets. In this phase, we manually remove noise data and irrelevant data. Noise data include forums with strange picture/video postings that are not clearly shown online. Irrelevant data are from forums where there are not enough postings or posting contents that are not related to the forum topics at all. After removing noisy data and outliers, the set of leaf forums is narrowed down to 31, with a time span of 52 time windows across the year of 2007 and eac time window is of a week length.

## 3.2. Text sentiment computation of forum posts

In this section, semantic orientation based approach will be developed using a new algorithm by adding up the sentiment values for all key words to achieve the sentiment value for the whole article. Text sentiment analysis is aimed at calculating an integer value for each piece of text, the absolute value of which represents the in<sup>fl</sup>uential power and the sign of which denotes its emotional polarity.

Suppose the current post is p, since it is written in Chinese, we <sup>fi</sup>rst utilize computer-based automatic word segmentation tool to decompose p into an array of key words $\{ w _ { 1 } , w _ { 2 } , w _ { 3 } , . . . , w _ { \mathrm { n } } \}$ , where there are n of them in total. Each key word $w _ { i } ( i = 1 , 2 , 3 , . . . , n )$ will be assigned a sentiment

![](/api/attachments/H4MRZRTZ/fulltext/images/61793e8cc31f7cd6a1d65306919da31861261042e8835807773668fef2db4be1.jpg)  
Fig. 3. Parsing links in table SINA\_FORUM\_URL to generate tables SINA\_FORUM\_TOPIC\_POST and SINA\_FORUM\_COMMENT\_POST.

![](/api/attachments/H4MRZRTZ/fulltext/images/e8d6e2cb506d40838fe3071fc3d14beaddbf87204e345ec3e42d13aaa749f536.jpg)  
Fig. 4. Calculation of the sentiment value v for key word w based on word lists derived from HowNet

value $\nu _ { i }$ by our proposed algorithm, while the sentiment value for p is the sum of the sentiment values for all the key words. Let $V _ { p }$ denote the sentiment value for p and we have

$$
V _ {p} = \sum_ {i = 1} ^ {n} v _ {i}.\tag{1}
$$

Calculation of the sentiment value array $\left\{ \nu _ { 1 } , \nu _ { 2 } , \nu _ { 3 } , . . . , \nu _ { n } \right\}$ is based on key words comparison and matching. In order to calculate the sentiment value for each key word contained in $p ,$ a comprehensive Chinese dictionary consisting of a complete list of sentiment-labeled words and phrase is entailed. In our work, the beta version of Chinese word sets with sentiment labels released by HowNet<sup>1</sup> on October 22, 2007 is utilized, and from which we derive eight word lists in Chinese. These eight lists are: positive Chinese words (POSITIVE), negative Chinese words (NEGATIVE), Chinese privatives (PRIVATIVE) and <sup>fi</sup>ve lists of Chinese modi<sup>fi</sup>ers, with different emotional intensities. These <sup>fi</sup>ve modi<sup>fi</sup>er lists are named a MODIFIER $( i = 1 , 2 , 3 , 4 , 5 )$ , each of which is assigned a value WEIGHT (i=1,2,3,4,5) denoting its sentimental intensity. The procedure of the calculation for the sentiment value of a key word is described in Fig, 4

## 3.3. Hotspot detection using K-means clustering

As aforementioned, the 31 selected leaf forums will undergo feature extraction process. Each forum can be treated as a data point in a vector space. K-means clustering is applied to these 31 data points to obtain a cluster natural groupings description for all time windows in the year 2007. Again, each time window has a length of a week.

Suppose that the current time window is $W _ { i }$ and the 31 leaf forums are denoted as $\left\{ \boldsymbol { F } _ { 1 } , \boldsymbol { F } _ { 2 } , \boldsymbol { F } _ { 3 } , . . . , \boldsymbol { F } _ { 3 1 } \right\}$ . During the feature extraction process, we use a vector $V ^ { i } ( j )$ to represent the emotional polarity or quanti<sup>fi</sup>cation of user attention of any forum $F _ { j } ( j = 1 , 2 , 3 . . . , 3 1 )$ within the time span $W _ { i } .$ The data set used as the input of the K-means clustering in $W _ { i }$ is denoted as $\{ V ^ { i } ( 1 ) , V ^ { i } ( 2 ) , V ^ { i } ( 3 ) . . . . , \hat { V } ^ { i } ( 3 1 ) \}$ , which will be clustered into k groups. $V ^ { i } ( j )$ is composed of <sup>fi</sup>ve elements: the number of the topic posts in $F _ { j }$ within $W _ { i } ,$ the average number of responses of topic posts, the average sentiment value of topic posts, the fraction of positive posts among all the topic posts, and the fraction of negative posts among all the topic posts. We denote these <sup>fi</sup>ve elements by $\mathsf { N U M } ^ { i } ( j )$ , RESPONSE<sup>i</sup> j , SENTIMENT <sup>i</sup> j , POS\_PERC<sup>i</sup>(j) and $\mathsf { N E G \_ P E R C } ^ { i } ( j )$ . Mathematically, we can express $V ^ { i } ( j )$ as:

$$
V ^ {i} (j) = \left( \begin{array}{c} N U M ^ {i} (j) \\ \overline {{R E S P O N S E}} ^ {i} (j) \\ \overline {{S E N T I M E N T}} ^ {i} (j) \\ P O S \_ P E R C ^ {i} (j) \\ N E G \_ P E R C ^ {i} (j) \end{array} \right).\tag{2}
$$

Eq. (2) displays the structure of the representation vector for leaf forums after feature extraction. The transformed vectors are used as the inputs to K-means model. For each $W _ { i } ,$ with a given k, a clustering view of all the 31 leaf forums is obtained by the K-means algorithm, with a center forum for each cluster. The hotspot forums are those closest to the theoretical centers of the clusters. For each time window, the clustering result by K-means is presented in a vector containing 31 elements, and each of which is an integer value of either 1 or $^ { 0 , }$ with 1 denoting a hotspo while 0 a non-hotspot.

## 3.4. Hotspot detection using SVM

Apart from K-means clustering, SVM is utilized in this section to realize hotspot forecasting. SVM forecasts the clustering view of the leaf forums in a sliding time window manner, whose results will be compared to those from K-means.

A sliding time window that goes through the whole experiment time span distinguishes the SVM-based approach from the K-means-based one. In order to forecast the hotspot distribution within the current time window, we fed into the SVM model with the historical data we obtain from the last time window. As for the output of the SVM, which serves as the supervised learning tool in our work, the clustering result by the K-means approach within the current time window is used. A well-trained SVM is utilized to carry out prediction for the next time window, by inputting the data obtained from the current one. Suppose there are T time windows, $\left\{ W _ { 1 } , W _ { 2 } , W _ { 3 } , . . . , W _ { T } \right\}$ , and the current one is $W _ { i } .$ If a forecast for $W _ { i + 1 }$ is expected, we <sup>fi</sup>rst train a SVM by inputting forums' representation vectors of $W _ { i - 1 }$ and setting the output as the clustering result for $W _ { i }$ by K-means. Then the trained SVM generates classi<sup>fi</sup>cation outputs for data of $W _ { i } .$ Finally. SVM result is compared to the K-means clustering result for data of $W _ { i + 1 }$

For each SVM, the input is a matrix containing 31 leaf forums' representation vectors, and the output is a vector containing 31 integer values either 1 or 0 with 1 representing a hotspot and 0 a non-hotspot. Each training and testing sample corresponds to a leaf forum. Computation based on SVM involves both the training process and test process. In the training process, we use a matrix tuple ${ < } I , O { > }$ , where I and O denotes input and output training sample data to SVM. Mathematically, we have

$$
I = \left( \begin{array}{l} V ^ {i - 1} (1) \\ V ^ {i - 1} (2) \\ \dots \\ V ^ {i - 1} (j) \\ \dots \\ V ^ {i - 1} (3 1) \end{array} \right) = \left( \begin{array}{l} N U M ^ {i - 1} (1), \overline {{R E S P O N S E}} ^ {i - 1} (1), \overline {{S E N T I M E N T}} ^ {i - 1} (1), P O S \_ P E R C ^ {i - 1} (1), N E G \_ P E R C ^ {i - 1} (1) \\ N U M ^ {i - 1} (2), \overline {{R E S P O N S E}} ^ {i - 1} (2), \overline {{S E N T I M E N T}} ^ {i - 1} (2), P O S \_ P E R C ^ {i - 1} (2), N E G \_ P E R C ^ {i - 1} (2) \\ \dots \\ N U M ^ {i - 1} (j), \overline {{R E S P O N S E}} ^ {i - 1} (j), \overline {{S E N T I M E N T}} ^ {i - 1} (j), P O S \_ P E R C ^ {i - 1} (j), N E G \_ P E R C ^ {i - 1} (j) \\ \dots \\ N U M ^ {i - 1} (3 1), \overline {{R E S P O N S E}} ^ {i - 1} (3 1), \overline {{S E N T I M E N T}} ^ {i - 1} (3 1), P O S \_ P E R C ^ {i - 1} (3 1), N E G \_ P E R C ^ {i - 1} (3 1) \end{array} \right)\tag{3}
$$

and

$$
O = \left( \begin{array}{c} L ^ {i} (1) \\ L ^ {i} (2) \\ \dots \\ L ^ {i} (j) \\ \dots \\ L ^ {i} (3 1) \end{array} \right),\tag{4}
$$

where $L ^ { i } ( j )$ in O denotes the clustering result for $F _ { j }$ in W by K-means. I $\begin{array} { r } { \mathrm { f } L ^ { i } ( j ) = 1 , } \end{array}$ K-means labels $F _ { j }$ is a hotspot, while $\mathrm { i f } L ^ { i } ( j ) = 0 1$ K-means labels $F _ { j }$ is a non-hotspot. Similarly, letbI′, O′Ndenote the input and output matrix of SVM in the test process and we have

$$
\begin{array}{l} I ^ {\prime} = \left( \begin{array}{c} V ^ {i} (1) \\ V ^ {i} (2) \\ \dots \\ V ^ {i} (j) \\ \dots \\ V ^ {i} (3 1) \end{array} \right) = \left( \begin{array}{c} N U M ^ {i} (1), \overline {{R E S P O N S E}} ^ {i} (1), \overline {{S E N T I M E N T}} ^ {i} (1), P O S \_ P E R C ^ {i} (1), N E G \_ P E R C ^ {i} (1) \\ N U M ^ {i} (2), \overline {{R E S P O N S E}} ^ {i} (2), \overline {{S E N T I M E N T}} ^ {i} (2), P O S \_ P E R C ^ {i} (2), N E G \_ P E R C ^ {i} (2) \\ \dots \\ N U M ^ {i} (j), \overline {{R E S P O N S E}} ^ {i} (j), \overline {{S E N T I M E N T}} ^ {i} (j), P O S \_ P E R C ^ {i} (j), N E G \_ P E R C ^ {i} (j) \\ \dots \\ N U M ^ {i} (3 1), \overline {{R E S P O N S E}} ^ {i} (3 1), \overline {{S E N T I M E N T}} ^ {i} (3 1), P O S \_ P E R C ^ {i} (3 1), N E G \_ P E R C ^ {i} (3 1) \end{array} \right) \\ d \\ O ^ {\prime} = \left( \begin{array}{c} L ^ {i + 1} (1) ^ {\prime} \\ L ^ {i + 1} (2) ^ {\prime} \\ \dots \\ L ^ {i + 1} (j) ^ {\prime} \\ \dots \\ L ^ {i + 1} (3 1) ^ {\prime} \end{array} \right), \end{array}\tag{5}
$$

and

ð<sup>6</sup>Þ

where $L ^ { i + 1 } ( j ) ^ { \prime }$ in $O ^ { \prime }$ represents the binary classi<sup>fi</sup>cation result for $F _ { j }$ in $W _ { i }$ by SVM. If $\cdot { \cal L } ^ { i + 1 } ( j ) ^ { \prime } = 1$ , SVM classi<sup>fi</sup>es $F _ { j }$ as a hotspot, while $F _ { j }$ is classi<sup>fi</sup>ed as non-hotspot if $L ^ { i + 1 } ( j ) ^ { \prime } { = } 0 .$ . Comparative study is carried out between $O ^ { \prime }$ and the clustering result by K-means in $W _ { i + 1 }$

## 4. Empirical results and discussion

## 4.1. Data preparation

The data preparation for the empirical studies primarily includes three tasks: data downloading, data cleansing and data statistics. The data sets used in our experiments are crawled down and compiled from the Internet by an automatic crawling Java program, which consists of two major modules: the target URL list generating module and the HTML page parsing module. We choose to conduct our experiments on Sina sports community because this is the most popular and prestigious online sports community in China. The aforementioned crawler crawled down a complete set of posts in the form of both topics and responses from Sina sports community. This was done within the time span from the time this community was founded until February 2008. The data view before any cleansing and <sup>fi</sup>ltering process is demonstrated in Table 1.

When the crawling is done, noticeable inconsistency and noise of post data entail cleansing and <sup>fi</sup>ltering process. A common time span T is expected, in which the vast majority of the forums have suf<sup>fi</sup>cient data distribution. The cleansing process includes the following six steps.

Step 1. Segment the continuous time line for data into time windows.

Step 2. Determine the optimal value for T.

Step 3. Get a subset F of the 49 forums which have dense data distribution within T.

Step 4. Generate a new post set P that falls within the range de<sup>fi</sup>ned by both T and F.

Step 5. Calculate the text sentiment for all the posts in P.

Step 6. Create the new view for cleansed data sets.

The data view after cleansing and <sup>fi</sup>ltering phase is also demonstrated in Table 1, where 200701 and 200752 stand for the 1st and 52nd week of the year 2007. The reason that the size of data increases after cleansing is that the results of word segmentation are written back to the database. Because the posts to be analyzed are written in Chinese, word segmentation constitutes a signi<sup>fi</sup>cant prerequisite step in text sentiment computation. The word segmentation software tool used in our experiment is the commercial Java library developed by

Lietu Enterprise Search<sup>2</sup>. It is demonstrated in Table 1, where we show a whole experiment time span from the <sup>fi</sup>rst week of 2007 till the last week of 2007. 31 out of the 49 leaf forums are selected as the <sup>fi</sup>nal set of leaf forums under study. Only topic posts are taken into consideration during the preliminary experiment.

We also calculate aggregated statistics in order to get a preliminary intuitive view for user attention of the selected 31 forums within the year 2007. Table 2 shows the average number of topic posts and the average number of responses for the 31 forums spanning across the 52 time windows of the year $2 0 0 7 ^ { 3 }$ . According to the number of topic posts, the most popular forums among users include “Basketball—Yao Ming”, Soccer Tycoons—AC Milan”, “Basketball—NBA”, “Soccer Tycoons—Milan International”, etc. The most popular forums based on the average response number include “Soccer Tycoons—Real Madrid”, “Soccer Tycoons—Juventas”, “Soccer Tycoons—Milan International”, “Soccer Tycoons—FC Barcelona”, etc.

## 4.2. Text sentiment calculation for topic posts using HowNet dictionaries

As previously mentioned, text sentiment computation is a key step in our empirical studies. We use the Chinese lexicons resourced from HowNet,<sup>4</sup> an online common-sense knowledge base unveiling interconceptual relations and inter-attribute relations of concepts as connoting in lexicons of the Chinese and their English equivalents, to form up eight key word lists. Results are described in Table 3. These eight lists correspond to those introduced in Section 3.

Based on the algorithm depicted in Section 3, we conduct sentiment calculation for the 220,053 posts by the eight word lists in Table 3. Since the posts to be analyzed are written in Chinese, word segmentation constitutes a signi<sup>fi</sup>cant prerequisite step in text sentiment computation. The word segmentation software tool used in our experiment is the commercial Java library developed by Lietu Enterprise Search. The Lietu tool not only converts the text into an array of words, but also tags each of the words with its part of speech.

Table 1  
The data view of collected post data from Sina sports community.

<table><tr><td></td><td>Post type</td><td>Number of posts</td><td>Size of data/KB</td><td>Starting time</td><td>Ending time</td><td>Number of forums</td></tr><tr><td rowspan="2">Before data cleansing</td><td>Topic post</td><td>510,218</td><td>616,640</td><td>1999-03-08 11:13:20</td><td>2008-01-02 00:22:29</td><td>49</td></tr><tr><td>Comment post</td><td>5,565,216</td><td>1,978,632</td><td>2003-08-01 22:33:52</td><td>2008-02-16 14:36:25</td><td>49</td></tr><tr><td>After data cleansing</td><td>Topic posts</td><td>220,053</td><td>1,210,112</td><td>2007-01-01 00:00:48</td><td>2007-12-31 23:59:59</td><td>31</td></tr></table>

## 4.3. Computation using K-means clustering

In this section, we conduct K-means clustering among the 31 selected leaf forums for each time window in 2007, based on their emotional polarity. Text sentiment analysis is employed to calculate the emotional polarities for all the posts. We will use K-means to achieve a clustering view for all the 31 forums within each time window over the year 2007, which generates in total 52 clustering results. One de<sup>fi</sup>ciency of K-means is that a predetermined value of k is required. To overcome this drawback, K-means cluster analysis is conducted for a set of k values ranged from 5 to 20. The forums yielding the smallest Euclidean distances to the centers of clusters are considered as hotspot forums within the current time window. Multiple metrics are employed to analyze the clustering results from a wider spectrum of perspectives.

We will examine the clustering results by K-means from the following two perspectives. First, we present the clustering natural groupings for each time window. Second, we show the results on a forum basis by presenting the emotional polarity each forum gets over the year 2007.

## 4.3.1. Clustering results shown on a time window basis

Table 4 demonstrates part of the clustering results by K-means in the year 2007, when k is set from 5 to 7. As before, “200701” stands for the <sup>fi</sup>rst time window of 2007. The forums listed in the table are those closest to the theoretical cluster centers and denote the hotspot forums selected by K-means. The naming rules for those forums are the same as in Table 2.

Table 2  
Post data statistics upon selected 31 forums of Sina sports community over the year 2007.

<table><tr><td>Forum ID</td><td>Forum name</td><td>Average # of posts</td><td>Average # of Responses</td></tr><tr><td>1</td><td>Chinese Soccer-Care About Chinese Football</td><td>120</td><td>4.65336</td></tr><tr><td>2</td><td>Sports shoes</td><td>365</td><td>16.36289</td></tr><tr><td>3</td><td>Soccer Tycoons-Arsenal</td><td>59</td><td>13.97825</td></tr><tr><td>4</td><td>Soccer Tycoons-Juventas</td><td>213</td><td>28.2192</td></tr><tr><td>5</td><td>Basketball-Guangzhou Hongyuan</td><td>17</td><td>7.041931</td></tr><tr><td>6</td><td>International Soccer-Spanish Football League</td><td>22</td><td>11.2351</td></tr><tr><td>7</td><td>Soccer Tycoons-Liverpool</td><td>48</td><td>7.64624</td></tr><tr><td>8</td><td>Sports Saloon-Billiard</td><td>17</td><td>6.819567</td></tr><tr><td>9</td><td>Basketball-Chinese Basketball Association</td><td>67</td><td>15.03061</td></tr><tr><td>10</td><td>Sports Saloon-Tennis</td><td>21</td><td>9.869563</td></tr><tr><td>11</td><td>International Soccer-Italian Football League</td><td>41</td><td>14.39272</td></tr><tr><td>12</td><td>Soccer Tycoons-Chelsea</td><td>127</td><td>15.26819</td></tr><tr><td>13</td><td>The Game of Go</td><td>17</td><td>12.62573</td></tr><tr><td>14</td><td>Chinese Soccer-Dalian Shide</td><td>23</td><td>10.97456</td></tr><tr><td>15</td><td>International Soccer-German Football League</td><td>5</td><td>8.454958</td></tr><tr><td>16</td><td>Soccer Tycoons-AC Milan</td><td>474</td><td>19.30753</td></tr><tr><td>17</td><td>International Soccer-English Football League</td><td>47</td><td>10.31931</td></tr><tr><td>18</td><td>Chinese Soccer-Shandong Luneng</td><td>192</td><td>10.8492</td></tr><tr><td>19</td><td>Outdoor activities</td><td>21</td><td>1.878042</td></tr><tr><td>20</td><td>Soccer Tycoons-Milan International</td><td>375</td><td>27.68831</td></tr><tr><td>21</td><td>Football lottery</td><td>198</td><td>4.880246</td></tr><tr><td>22</td><td>Soccer Tycoons-Manchester United</td><td>189</td><td>22.66756</td></tr><tr><td>23</td><td>Basketball-NBA</td><td>456</td><td>16.47136</td></tr><tr><td>24</td><td>Basketball-Yao Ming</td><td>603</td><td>18.24459</td></tr><tr><td>25</td><td>Soccer Tycoons-A.S. Roma</td><td>46</td><td>10.11552</td></tr><tr><td>26</td><td>Sports Saloon-Table Tennis</td><td>14</td><td>11.62929</td></tr><tr><td>27</td><td>Soccer Tycoons-FC Barcelona</td><td>61</td><td>23.70714</td></tr><tr><td>28</td><td>Volleyball</td><td>145</td><td>10.55084</td></tr><tr><td>29</td><td>Soccer Tycoons-Real Madrid</td><td>100</td><td>40.08629</td></tr><tr><td>30</td><td>Soccer Tycoons-Bayern Munchen</td><td>16</td><td>7.178974</td></tr><tr><td>31</td><td>Chinese Soccer-China Super League of Football</td><td>120</td><td>6.833243</td></tr></table>

Note: the “—” in a forum name separates the leaf forum name from the root forum name.

## 4.3.2. Clustering results shown on a forum basis

In addition to observing hotspot distribution on a timely basis, we further inspect the hotspot distribution among forums, i.e. which forums tend to get more user attention over the year than the others. We propose a method to measure the degree $H _ { j }$ to which the forum $F _ { j }$ gets attention, which counts the number of times $F _ { j }$ is considered as a hotspot, over all the 52 time windows as well as over all the values of k. Usually a larger value of $H _ { j }$ indicates a higher popularity for $F _ { j }$ in year 2007. Fig. 5 is a visualization of the hotspot distribution of the 31 forums in the year 2007 achieved by K-means clustering, with the vertical axis showing their degree values and a higher value of the degree implying a higher user attention.

As shown by Fig. 5, the hotspot degree values for forums span from 226 to 469. Based on the statistics visualized in Fig. 5, we list in Table 5 the top 10 most popular forums in Sina sports community by K-means clustering over the year 2007.

It is observed that the hot forum set determined by K-means clustering is highly consistent with the set obtained in Section 4.1 after intuitive statistics is calculated. The most popular sports topics among Chinese users include basketball, soccer etc. Forums such as Basketball—Yao Ming, Soccer Tycoons—AC Milan, Soccer Tycoons— Chelsea are substantiated to be hotspot forums over the year 2007 by both approaches. Therefore, our approach incorporating K-means clustering and text sentiment analysis is suf<sup>fi</sup>cient to provide helpful information for users to get a good mastery of the hotspot ranking and distribution of Sina sports community.

## 4.4. Computation using SVM classification

During this phase of experiment, we apply SVM-based binary classi<sup>fi</sup>cation to forecast the hotspot distribution among the selected 31 forums of Sina sports community. The analysis is similar to Section 4.3. SVM-based approach forecasts the clustering natural groupings for the future time window by using the data from the past time window. SVM achieves a clustering result by classifying each forum as either hotspot forum or non-hotspot forum, thus converting the clustering task into a binary classi<sup>fi</sup>cation task.

Eight Chinese key word lists based on HowNet online knowledge base.

<table><tr><td>Created Chinese key word lists</td><td>Description</td></tr><tr><td>POSITIVE</td><td>4566 Chinese words with positive sentimental polarity</td></tr><tr><td>NEGATIVE</td><td>4370 Chinese words with negative sentimental polarity</td></tr><tr><td>PRIVATIVE</td><td>14 Chinese privatives, manually collected</td></tr><tr><td colspan="2">The following are five lists of Chinese modifiers, with a decrement in their intensities</td></tr><tr><td> $MODIFIER_1$ </td><td>85 modifiers, with a weight value 10</td></tr><tr><td> $MODIFIER_2$ </td><td>42 modifiers, with a weight value 8</td></tr><tr><td> $MODIFIER_3$ </td><td>37 modifiers, with a weight value 6</td></tr><tr><td> $MODIFIER_4$ </td><td>29 modifiers, with a weight value 4</td></tr><tr><td> $MODIFIER_5$ </td><td>12 modifiers, with a weight value 2</td></tr></table>

Table 4  
Clustering results by K-means for the three time windows.

<table><tr><td>Time window</td><td>k=5</td><td>k=6</td><td>k=7</td></tr><tr><td>200701</td><td>1. Soccer Tycoons—Juventas2. Basketball—Guangzhou Hongyuan3. Outdoor activities4. Soccer Tycoons—Milan International5. Basketball—Yao Ming</td><td>1. Soccer Tycoons—Liverpool2. Chinese Soccer—Care About Chinese Football3. Sports Saloon—Tennis4. The Game of Go5. Chinese Soccer—Shandong Luneng6. Basketball—Yao Ming</td><td>1. Sports shoes2. Soccer Tycoons—Juventas3. Sports Saloon—Tennis4. International Soccer—Italian Football League5. The Game of Go6. International Soccer—English Football League7. Basketball—Yao Ming</td></tr><tr><td>200702</td><td>1. Sports shoes2. Soccer Tycoons—Liverpool3. Soccer Tycoons—Chelsea4. International Soccer—English Football League5. Chinese Soccer—Shandong Luneng</td><td>1. Sports shoes2. International Soccer—Italian Football League3. Chinese Soccer—Shandong Luneng4. Outdoor activities5. Basketball—Yao Ming6. Chinese Soccer—China Super League of Football</td><td>1. Sports shoes2. International Soccer—German Football League3. Chinese Soccer—Shandong Luneng4. Outdoor activities5. Soccer Tycoons—Milan International6. Basketball—Yao Ming7. Chinese Soccer—China Super League of Football</td></tr><tr><td>200703</td><td>1. Sports shoes2. Soccer Tycoons—Chelsea3. Soccer Tycoons—Manchester United4. Soccer Tycoons—FC Barcelona5. Chinese Soccer—China Super League of Football</td><td>1. Sports shoes2. Soccer Tycoons—Chelsea3. The Game of Go4. Chinese Soccer—Dalian Shide5. Soccer Tycoons—Manchester United6. Soccer Tycoons—FC Barcelona</td><td>1. Soccer Tycoons—Juventas2. International Soccer—Spanish Football League3. Sports Saloon—Billiard4. Soccer Tycoons—Milan International5. Soccer Tycoons—Manchester United6. Basketball—Yao Ming7. Chinese Soccer—China Super League of Football</td></tr></table>

![](/api/attachments/H4MRZRTZ/fulltext/images/d051da61c4603d1cf1fc29b8b8e4644b88d2178d9fb35384731c988852251e2b.jpg)  
Fig. 5. The hotspot distribution of the 31 leaf forums using K-means.

As mentioned previously, each training and forecasting cycle of SVM classi<sup>fi</sup>cation strides over three time windows, rendering a total time span for the SVM forecasting starting from the third week of 2007 till the last week of 2007. For each time window, the forecasting result achieved by SVM is compared to that by K-means in the next section. The SVM tool used in this experiment is the open source LIBSVM library<sup>5</sup> written in Java [20,23].

Similar to Section 4.3, we examine the forecasting results by SVM from two perspectives: a time window basis forecasting and a forum basis forecasting. Table 6 demonstrates part of the forecasting results for three time windows in the vear 2007. The forums listed in the table are those forecasted as the hotspot forums by SVM. The k value in the <sup>fi</sup>rst row is a parameter of the K-means method, which is used to enable supervised learning for SVM training. Note that there exists disparity between the k value of K-means clustering and the actual number of hotspots that are labeled by SVM.

Similar forum-based analysis to Section 4.3 is employed here to acquire a view from a forum perspective. The hotspot degree value is de<sup>fi</sup>ned the same as before. Fig. 6 shows the hotspot distribution of the 31 forums in the year 2007 achieved by SVM forecasting, with the vertical axis showing their degree values. Again, a higher value of the degree implies a higher user attention.

Table 5  
Top 10 popular forums in 2007 Sina sports community by K-means.

<table><tr><td>Forum ID</td><td>Forum name</td><td>Hotspot degree</td></tr><tr><td>24</td><td>Basketball—Yao Ming</td><td>469</td></tr><tr><td>23</td><td>Basketball—NBA</td><td>432</td></tr><tr><td>20</td><td>Soccer Tycoons—Milan International</td><td>408</td></tr><tr><td>16</td><td>Soccer Tycoons—AC Milan</td><td>401</td></tr><tr><td>28</td><td>Volleyball</td><td>395</td></tr><tr><td>29</td><td>Soccer Tycoons—Real Madrid</td><td>389</td></tr><tr><td>12</td><td>Soccer Tycoons—Chelsea</td><td>380</td></tr><tr><td>4</td><td>Soccer Tycoons—Juventas</td><td>367</td></tr><tr><td>18</td><td>Chinese Soccer—Shandong Luneng</td><td>366</td></tr><tr><td>22</td><td>Soccer Tycoons—Manchester United</td><td>356</td></tr></table>

Table 6  
Forecasting results by SVM for the 27th till the 29th time window of the year 2007.

<table><tr><td>Time Window</td><td>k=7</td><td>k=8</td><td>k=9</td></tr><tr><td>200727</td><td>1. Sports shoes2. Basketball—Chinese Basketball Association</td><td>1. Soccer Tycoons—Juventas2. Soccer Tycoons—Liverpool3. Sports Saloon—Tennis4. Soccer Tycoons—Chelsea5. The Game of Go6. Soccer Tycoons—AC Milan7. International Soccer—English Football League8. Soccer Tycoons—Milan International9. Soccer Tycoons—Manchester United10. Basketball—Yao Ming11. Soccer Tycoons—Bayern Munchen</td><td>1. Soccer Tycoons—AC Milan2. International Soccer—English Football League3. Basketball—NBA4. Basketball—Yao Ming</td></tr><tr><td>200728</td><td>1. Soccer Tycoons—AC Milan2. Basketball—NBA3. Basketball—Yao Ming</td><td>1. Soccer Tycoons—AC Milan2. Soccer Tycoons—Milan International3. Basketball—NBA4. Basketball—Yao Ming</td><td>1. Soccer Tycoons—AC Milan2. Basketball—NBA3. Basketball—Yao Ming</td></tr><tr><td>200729</td><td>1. International Soccer—Spanish Football League2. Basketball—NBA3. Soccer Tycoons—Bayern Munchen</td><td>1. Chinese Soccer—Care About Chinese Football2. Soccer Tycoons—Arsenal3. International Soccer—Spanish Football League4. International Soccer—English Football League5. Soccer Tycoons—Manchester United6. Soccer Tycoons—Bayern Munchen</td><td>1. Chinese Soccer—Care About Chinese Football2. Soccer Tycoons—Liverpool3. Chinese Soccer—Dalian Shide4. International Soccer—German Football League5. Football lottery6. Sports Saloon—Table Tennis7. Soccer Tycoons—Bayern Munchen8. Chinese Soccer—China Super League of Football</td></tr></table>

As shown by Fig. 6, the hotspot degree values for forums span from 224 to 441. Based on the statistics visualized in Fig. 6, we list in Table 7 the top 10 most popular forums in Sina sports community by SVM forecasting over the year 2007. The results shown in this section further present a noticeable consistency with the results achieved by K-means clustering. It is clearly demonstrated, by both Table 5 and Table 7, that the two lists of top 10 most popular forums resemble each other to as much as 80%. On top of this, K-means and SVM provide the same results for the top 4 most popular forums in the year 2007, which are Basketball—Yao Ming, Basketball—NBA, Soccer Tycoons—Milan International and Soccer Tycoons—AC Milan. Therefore, a strong connection between text sentiment and hotspot distribution for online sports forums is con<sup>fi</sup>rmed by both techniques. This has veri<sup>fi</sup>ed the feasibility of detecting and forecasting hotspot forums with the aid of text sentiment analysis. Besides, SVM-based approach realizes a forecast for the next time window. Finally, in order to see a detailed SVM computation, we depict in Fig. 7 the distribution of hotspots with respect to time. In Fig. 7, the X and Y axis represent respective weeks in the total time horizon and corresponding hotspot forums identi<sup>fi</sup>ed by SVM. Note that a k value of 8 is used in K-means model. Fig. 7 generates the same result as in Table 6. Both Table 6 and Fig. 7 suggest during the 27th, 28th and 29th week, the number of hotspot forums identi<sup>fi</sup>ed by SVM is 11, 4 and 6 respectively.

## 4.5. Comparative Study between K-means and SVM

This section carries out a formal comparative study between Kmeans and SVM to validate model consistency using <sup>fi</sup>ve widely used metrics: accuracy, sensitivity, speci<sup>fi</sup>city, positive predictive value (PPV) and negative predictive value (NPV) [17]. For a certain value of k, a comparative study is exerted for each one of the 50 time windows in 2007, which are the 50 time windows in the SVM-based experiment. Each time window corresponds to a set of these <sup>fi</sup>ve metrics, which are de<sup>fi</sup>ned as follows.

![](/api/attachments/H4MRZRTZ/fulltext/images/12afbbd0770ee3dc7f6cd67bdfd92534649038c52d4190877ecced1e517dbfe2.jpg)  
Fig. 6. The hotspot distribution of the 31 leaf forums in 2007 based on SVM

Table 7  
The top 10 most popular forums in Sina sports community by SVM forecasting over the year 2007.

<table><tr><td>Forum ID</td><td>Forum name</td><td>Hotspot degree value</td></tr><tr><td>24</td><td>Basketball—Yao Ming</td><td>441</td></tr><tr><td>23</td><td>Basketball—NBA</td><td>363</td></tr><tr><td>20</td><td>Soccer Tycoons—Milan International</td><td>361</td></tr><tr><td>16</td><td>Soccer Tycoons—AC Milan</td><td>358</td></tr><tr><td>28</td><td>Sports shoes</td><td>323</td></tr><tr><td>29</td><td>Chinese Soccer—Shandong Luneng</td><td>302</td></tr><tr><td>12</td><td>Soccer Tycoons—Manchester United</td><td>298</td></tr><tr><td>4</td><td>Soccer Tycoons—Juventas</td><td>293</td></tr><tr><td>18</td><td>International Soccer—German Football League</td><td>287</td></tr><tr><td>22</td><td>Soccer Tycoons—Real Madrid</td><td>285</td></tr></table>

De<sup>fi</sup>nition 1. Accuracy:

$$
A c c u r a c y = \frac {T P + T N}{T P + T N + F P + F N},\tag{7}
$$

where TP denotes the number of forums that are estimated by both Kmeans and SVM as hotspots; TN denotes the number of forums that are estimated by both K-means and SVM as hotspots; FP denotes the number of forums that are estimated by SVM as hotspots whereas non-hotspots by K-means; FN denotes the number of forums that are estimated by SVM as non-hotspots whereas hotspots by K-means. Accuracy shows the fraction of forums that are classi<sup>fi</sup>ed into the same category by both K-means and SVM among all the forums.

De<sup>fi</sup>nition 2. Sensitivity

$$
S e n s i t i v i t y = \frac {T P}{T P + F N}.\tag{8}
$$

Sensitivity shows the fraction of forums which are classi<sup>fi</sup>ed by SVM as hotspots among all forums that are labeled by K-means as hotspots.

De<sup>fi</sup>nition 3. Speci<sup>fi</sup>city

$$
S p e c i f i c i t y = \frac {T N}{T N + F P}.\tag{9}
$$

Speci<sup>fi</sup>city shows the fraction of forums which are classi<sup>fi</sup>ed by SVM as non-hotspots among all forums that are labeled by K-means as nonhotspots.

De<sup>fi</sup>nition 4. PPV

$$
P P V = \frac {T P}{T P + F P}.\tag{10}
$$

PPV shows the fraction of forums which are labeled by K-means as hotspots among all the forums that are classi<sup>fi</sup>ed by SVM as hotspots.

De<sup>fi</sup>nition 5. NPV

$$
N P V = \frac {T N}{T N + F N}.\tag{11}
$$

NPV shows the fraction of forums which are labeled by K-means as non-hotspots among all the forums that are classi<sup>fi</sup>ed by SVM as nonhotspots.

![](/api/attachments/H4MRZRTZ/fulltext/images/08c7f69212c6b043547883e2259a48ff713e5bf5ca221cd5dfe8f0fafcb6af40.jpg)  
Fig. 7. Distribution of hotspots with respect to time.

![](/api/attachments/H4MRZRTZ/fulltext/images/7c768293f38ad126db2e80f0396f1ba662e6c357af8d6a9f6d491fc115352977.jpg)  
Fig. 8. The movements of average accuracy over different k values in the year 2007

Using Formulae (7)–(11), we calculate the <sup>fi</sup>ve metrics over different k values ranged from 5 to 20. To get a better visualization of the movements of the <sup>fi</sup>ve metrics over different k values, we depict <sup>fi</sup>ve metrics from Figs. 8–12. These <sup>fi</sup>gures visualize the movements of the average values of the <sup>fi</sup>ve metrics over different k values.

It is clearly indicated through Figs. 8–Fig. 12 that, four measurements are monotonic functions of k except average accuracy. Fig. 8 suggests that our method is generally suf<sup>fi</sup>cient to achieve a satisfying result for accuracy, especially when k is set to a rather small value. During the subsequent experiments, larger values of k (from 20 to 25) are employed, and it is proved that average accuracy increases with k when k has reached a certain value. Therefore, the assumption of facilitating hotspot detection and prediction by machine learning techniques and sentiment analysis is justi<sup>fi</sup>ed. The rest of the four metrics provide evaluation from four other perspectives. Sensitivity is a critical evaluation measurement, which denotes the fraction of forums which are classi<sup>fi</sup>ed by SVM as hotspots among all forums that are labeled by K-means as hotspots. It is visualized in Fig. 9 that the average sensitivity for all time windows displays a monotonic increment over different k values, which is reasonable considering that a larger possibility is enabled for consistency when k is designated a relatively larger value. The fact that when k is larger than 17, a good result is obtained on a sensitivity level proves that under this setting, our SVM-based method is suf<sup>fi</sup>cient in capturing the majority hotspots, which are approved by K-means, for the immediate future. PPV constitutes another important measurement in our experiment, which denotes the fraction of forums labeled by K-means as hotspots among all the forums classi<sup>fi</sup>ed by SVM as hotspots. It is shown that when k is set smaller than 13, a good result is achieved on a PPV level, which indicates that the SVM forecasting results are more reliable when k is relatively small.

## 5. Conclusions and discussions

We have developed an algorithm to automatically analyze the emotional polarity of a text, based on which a value for each piece of text is obtained. The absolute value of the text represents the in<sup>fl</sup>uential power and the sign of the text denotes its emotional polarity. This algorithm is combined with K-means clustering and SVM classi<sup>fi</sup>cation to develop integrated approach for online sports forums cluster analysis. We apply unsupervised clustering algorithm to group the forums into various clusters, with the center of each cluster representing a hotspot forum within the current time span. In addition to clustering the forums based on data from the current time window, we also conduct forecast for the next time window. Empirical studies present strong proof of the existence of correlations between post text sentiment and hotspot distribution. Computation indicates both SVM and K-means produce consistent natural groupings results.

![](/api/attachments/H4MRZRTZ/fulltext/images/436f7c17b8877975a684f86202a13de791a552566cdb605dfa0246657a26664a.jpg)  
Fig. 9. The movements of average sensitivity over different k values in the year 2007.

![](/api/attachments/H4MRZRTZ/fulltext/images/34aecac655e561937da9a11819f75d8b945cbc4e4e294425418200f78a212b4c.jpg)  
Fig. 10. The movements of average speci<sup>fi</sup>city over different k values in the year 2007

Companies, as information seekers can bene<sup>fi</sup>t from our hotspot predicting approaches in several ways. For example, marketing objectives at the marketing department of big retail stores such as Walmart should follow the same rules as the sales objectives, and be measurable, quanti<sup>fi</sup>able, and time speci<sup>fi</sup>c. However, in practice customers' behavior are always hard to be explored and captured. Using our hotspot predicting approaches can help the marketing depart ment understand what their speci<sup>fi</sup>c customers' timely concerns regarding goods and services information. Results generated from our approach can be also combined to market basket analysis to yield comprehensive decision support information.

A <sup>fi</sup>rm in <sup>fi</sup>nancial sector or the <sup>fi</sup>nancial department of a giant company may pro<sup>fi</sup>t from such a sentimental and text mining process. In <sup>fi</sup>nancial market, right before a security market opens and trading begins, analysts people on sales and trading desks usually try to get an overall <sup>fi</sup>x on market sentiment and for particular investments. To get a feel for what will take place, decision makers used to make phone calls to trusted contacts, browse through news, morning reports and use other more quantitative tools. Our hotspot based semantic engine can aggregate the content in the forum and media feeds to determine whether stories on a particular company are positive, negative or neutral, and then generate simple data displays and charts that enable one to get a grasp on likely market sentiment for a company's security very quickly [17].Further work can be done based on this research. First, predicting hotspot using past data may not be accurate since many of the hotspots are emergent events that has no correlation with past hotspot history. Therefore, algorithm design can be improved to treat this problem and yield a more accurate calculation of sentiment. Regarding supervised learning, algorithms other than SVM, or variations of SVM, can be incorporated as well. Second, we can incorporate topic extraction. It is very natural to pop the question what event or topic triggered the user attention after a hotspot is detected. Currently our model is not able to provide analysis in this aspect, which entails a thorough exploration of topic extraction for hotspots in the future. Third, a practical system, in the form of a website portal, is desired as our major future work. The system is expected to possess the following functions.

![](/api/attachments/H4MRZRTZ/fulltext/images/acf4ab95af2ac9d955e86c13d019a39b387a0e3a0fd3a884214a0d7d0484e803.jpg)  
Fig. 11. The movements of average PPV over different k values in the year 2007.

![](/api/attachments/H4MRZRTZ/fulltext/images/54fbd17cb82d6ea20b429652b5c4426a149303da8dc4fb89fc5e63ec3e1a1021.jpg)  
Fig. 12. The movements of average NPV over different k values in the year 2007.

a) Users are able to observe the hotspot forum distribution and its natural groupings by inputting a time span.

b) Users are able to forecast the hotspot forum distribution and its natural groupings for the immediate future time windows.

c) Users are able to choose the ways hotspot detection results are visualized.

d) Users are able to choose among different clustering or forecasting algorithms.

e) Users are able to further inspect the posts and their sentiments for any detected hotspot forum.

f) Users are able to extract the topics of hotspot forums based on their posts.

g) Users are able to calculate the sentiment value for any post they choose.

## References

[1] K. Ahmad, Y. Almas, Visualising sentiments in <sup>fi</sup>nancial texts? Proceedings of the Ninth International Conference on Information Visualisation (2005). 363-368

[2] C. Asavathiratham, The In<sup>fl</sup>uence Model: A Tractable Representation for the Dynamics of Networked Markov Chains, Dept. of EECS. 2000, MIT, Cambridge, 2000, p. 188.

[3] P. Chaovalit, L. Zhou, Movie review mining: a comparison between supervised and unsupervised classi<sup>fi</sup>cation approaches, Proceedings of the 38th Hawaii International Conference on System Sciences, 2005.

[4] K.W. Cheung, J.T. Kwok, M.H. Law, K.C. Tsui, Mining customer product ratings for personalized marketing, Decision Support Systems 35 (2) (2003) 231–243.

[5] J. Coble, D. Cook, R. Rathi, L. Holder, Iterative structure discovery in graph-based data, International Journal of Arti<sup>fi</sup>cial Intelligence Techniques 1–2 (14) (2005) 101-124

[6] M. Dash, H. Liu, Feature selection for classi<sup>fi</sup>cation, Intelligent Data Analysis 1 (3) (1997) 131–156.

[7] C.C. Freifeld, K.D. Mandl, B.Y. Reis, J.S. Brownstein, HealthMap: global infectious disease monitoring through automated classi<sup>fi</sup>cation and visualization of internet media reports, Journal of the American Medical Informatics Association 15 (2008) 150–157.

[8] J. Gaurav, A. Ginwala, Y.A. Aslandogan, An approach to text classi<sup>fi</sup>cation using dimensionality reduction and combination of classi<sup>fi</sup>ers, Proceedings of the 2004 IEEE International Conference on Information Reuse and Integration (2004) 564–569.

[9] A. Goswami, R.M. Jin, G. Agrawal, Fast and exact out-of-core k-means clustering, Fourth IEEE International Conference on Data Mining (2004) 83–90.

[10] V. Guralnik, G. Karypis, A scalable algorithm for clustering protein sequences, Proc. Workshop Data Mining in Bioinformatics (BIOKDD), 2001, pp. 73–80.

[11] K.F. Han, D. Baker, Recurring local sequence motifs in proteins, Journal of Molecular Biology 251 (1) (1995) 176–187.

[12] K.F. Han, D. Baker, Global properties of the mapping between local amino acid sequence and local structure in proteins, Proceedings of the National Academy of Sciences of the United States of America (1996) 5814–5818

[13] V. Hatzivassiloglou, K.R. McKeown, Predicting the semantic orientation of adjectives, Proceedings of the 35th Annual Meeting of the ACL and the 8th Conference of the European Chapter of the ACL, New Brunswick, NJ, 1997, pp. 174–181.

[14] R.Q. Huang, J.H.L. Hansen, Dialect classi<sup>fi</sup>cation on printed text using perplexity measure and conditional random <sup>fi</sup>elds, IEEE International Conference on Acoustics, Speech and Signal Processing (2007) 993–996.

[15] T. Joachims, Text categorization with SVM: learning with many relevant features, Proceedings of ECM, 10th European Conference on Machine Learning, 1998.

[16] J.I. Khan, S. Shaikh, Relationship algebra for computing in social networks and social network based applications. 2006 IEEE/WIC/ACM International Conference on Web Intelligence. 2006, pp. 113-116.

[17] N. Li, X. Liang, X. Li, C. Wang, D. Wu, Network environment and <sup>fi</sup>nancial risk using machine learning and sentiment analysis, Human and Ecological Risk Assessment 15 (2) (2009) 227–252.

[18] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment classi<sup>fi</sup>cation using machine learning techniques, Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), 2002, pp. 79–86.

[19] T. Saegusa, T. Maruyama, Real-time segmentation of color images based on the K-means CLUSTERING on FPGA, International Conference on Field-Programmable Technology, 2007, pp. 329–332.

[20] S. Schauland, A. Kummert, P. Su-Birm, I. Uri, Y. Zhang, Vision-based pedestrian detection—improvement and veri<sup>fi</sup>cation of feature extraction methods and SVMbased classi<sup>fi</sup>cation, IEEE Intelligent Transportation Systems Conference (2006) 97–102.

[21] Z.H. Sun, Y.X. Sun, Fuzzy support vector machine for regression estimation, IEEE International Conference on Systems, Man and Cybernetics, vol. 4, 2003, pp. 3336–3341.

[22] S. Tan, J. Zhang, An empirical study of sentiment analysis for chinese documents, Expert Systems with Applications 34 (4) (2008) 2622–2629.

[23] D. Thanh-Nghi, J.D. Fekete, Large scale classi<sup>fi</sup>cation with support vector machine algorithms, ICMLA 2007, Sixth International Conference on Machine Learning and Applications, 2007, pp. 7–12.

[24] S. Tong, E. Chang, Support vector machine active learning for image retrieval, Proceedings of ACM International Conference on Multimedia, 2001, pp. 107–118.

[25] T.B. Trafalis, H. Ince, Support vector machine for regression and applications to <sup>fi</sup>nancial forecasting, Proceedings of the IEEE-INNS-ENNS International Joint Conference on Neural Networks 6 (2000) 348–353.

[26] P.D. Turney, Mining the web for synonyms: PMI-IR versus LSA on TOEFL, Proceedings of the Twelfth European Conference on Machine Learning, Springer-Verlag, Berlin, 2001, pp. 491–502.

[27] P.D. Turney, Thumbs up or thumbs down? Semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, presented at the Association for Computational Linguistics 40th Anniversary Meeting, New Brunswick, N.J., (2002).

[28] P.D. Turney, M.L. Littman, 315–346, Measuring praise and criticism: inference of semantic orientation from association, ACM Transactions on Information Systems 21 (2003) 315–346.

[29] V. Vapnik, Statistical Learning Theory, Wiley, New York, 1998.

[30] R. Vahidov, R. Elrod, Incorporating critique and argumentation in DSS, Decision Support Systems 26 (3) (1999) 249–258.

[31] D. Wu, Performance evaluation: an integrated method using data envelopment analysis and fuzzy preference relations, European Journal of Operational Research 194 (1) (2009) 227–235.

[32] D. Wu, Z. Yang, L. Liang, Using DEA-neural network approach to evaluate branch ef<sup>fi</sup>ciency of a large Canadian bank, Expert Systems with Applications 31 (1) (2006) 108–115.

[33] D. Xu, S. Liao, Q. Li, Combining empirical experimentation and modeling techniques: a design research approach for personalized mobile advertising applications, Decision Support Systems 44 (3) (2008).

[34] J.M. Yang, X.Z. Huang, D. Zhuang, S.T. Zhang, The complex network analysis of competitive relationships between manufacturers in Foshan Ceramic Industry Cluster, 2006 International Conference on Management Science and Engineering 2006, pp. 1020–1023.

[35] S. Yuan, A personalized and integrative comparison-shopping engine and its applications, Decision Support Systems 34 (2) (2003).

[36] Y. Zhang, Y. Dang, H. Chen, M. Thurmond, C. Larson, Automatic online news monitoring and classi<sup>fi</sup>cation for syndromic surveillance, Decision Support Systems 47 (4) (2009) 508–517.

[37] X.H. Zhang, Z.B. Lu, C.Y. Kang, Underwater acoustic targets classi<sup>fi</sup>cation using support vector machine, Proceedings of the International Conference on Neural Networks and Signal Processing 2 (2003) 932–935.

[38] Y.G. Zhao, Q.M. He, An unbalanced dataset classi<sup>fi</sup>cation approach based on vsupport vector machine, The Sixth World Congress on Intelligent Control and Automation, vol. 2, 2006, pp. 10496–10501

[39] W. Zhong, G. Altun, R. Harrison, P.C. Tai, Y. Pan, Improved K-means clustering algorithm for exploring local protein sequence motifs representing common structural property, IEEE Transactions on NanoBioscience 4 (3) (2005) 255–265.

[40] S. Zhou, T.W. Ling, J. Guan, J.T. Hu, A. Zhou, Fast text classi<sup>fi</sup>cation: a trainingcorpus pruning based approach, Proceedings of the Eighth International Conference on Database Systems for Advanced Applications, 2003, p. 127-13.

[41] http://domino.research.ibm.com/comm/research\_projects.nsf/pages/cni.index html.

[42] http://<sup>fi</sup>nance.google.com/<sup>fi</sup>nance?q=NYSE%3AIBM.

[43] http://<sup>fi</sup>nance.yahoo.com/q/co?s=INTC

[44] http://www.youtube.com

[45] http://zp.isoche.com/.

Nan Li is a Ph.D. candidate at the Department of Computer Science, University of California, Santa Barbara. Her research mainly focuses on business data mining, text mining and Sentiment Analysis. Her work has been published/accepted at such journals as Human and Ecological Risk Assessment.

Desheng Dash Wu is the af<sup>fi</sup>liated Professor in RiskLab at the University of Toronto and the Director of RiskChina Research Center at the University of Toronto. His research interests focus on enterprise risk management, business data mining, and performance evaluation in <sup>fi</sup>nancial industry. He is the coauthor of Enterprise Risk Management book. He is co-editor in chief of International Journal of Services Sciences. His work has appeared in several journals as International Journal of Production Research, European J. of Operational Research, IEEE Transactions on Knowledge and Data Engineering, Annals of Operations Research, J. of OR Society, International J. of Production Economics, Expert Systems with Applications, Computers and Operations Research, Human and Ecological Risk Assessment, International Journal of System Science, etc. He has more than forty journal papers and coauthored 2 books. He has served as Editor/Guest Editor/Chair for several journals/conferences. The special issues he edited include those for Annals of Operations Research, Human and Ecological Risk Assessment, and Production Planning and Control. He is a Member of the Professional Risk Managers' International Association (PRMIA) Academic Advisory Committee.
