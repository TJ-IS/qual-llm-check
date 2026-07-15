---
otero_id: 7890
otero_key: "H2Y9VY8C"
title: "The dynamic predictive power of company comparative networks for stock sector performance"
authors: "Kun Chen; Peng Luo; Dongming Xu; Huaiqing Wang"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.07.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The dynamic predictive power of company comparative networks for stock sector performance

Kun Chen<sup>a,</sup>\*, Peng Luo<sup>b</sup>, Dongming Xu<sup>c</sup>, Huaiqing Wang<sup>a</sup>

<sup>a</sup> Department of Finance, South University of Science and Technology, Shenzhen 518055, China

<sup>b</sup> School of Management, Harbin Institute of Technology, Harbin 150001, China

<sup>c</sup> UQ Business School, The University of Queensland, St Lucia, QLD 4072, Australia

## A R T I C L E I N F O

Article history: Received 4 July 2015 Received in revised form 13 June 2016 Accepted 19 July 2016 Available online xxx

Keywords: Company network Sentiment analysis Vector autoregression Stock sector performance

## A B S T R A C T

As economic integration and business connections increase, companies actively interact with each other in the market in cooperative or competitive relationships. To understand the market network structure with company relationships and to investigate the impacts of market network structure on stock sector performance, we propose the construct of a company comparative network based on public media data and sector interaction metrics based on the company network. All the market network structure metrics are integrated into a vector autoregression model with stock sector return and risk. Several <sup>fi</sup>ndings demonstrate the dynamic relationships that exist between sector interactions and sector performance. First, sector interaction metrics constructed based on company networks are signi<sup>fi</sup>cant leading indicators of sector performance. Interestingly, the interactions between sectors have greater predictive power than those within sectors. Second, compared with the company closeness network, the company comparative network, which labels the cooperative or competitive relationships between companies, is a better construct to understand and predict sector interactions and performance. Third, competitive company interactions between sectors impact sector performance in a slower manner than cooperative company interactions. The <sup>fi</sup>ndings enrich <sup>fi</sup>nancial studies regarding asset pricing by providing additional explanations of company/sector interactions and insights into company management using industry-level strategies.

ã 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

As economic integration and business connections increase, companies actively interact with each other in the market in cooperative or competitive relationships. Such relationships often exhibit industry-related features. For example, competitive relationships often exist within an industry because of limited resources and customers. These cooperative relationships usually arise between the supply and demand sides across different industries. Complex interactive business relationships depict the economic market with intra-sector and cross-sector links. These links are helpful for understanding information and shock transfers within and across sectors [1–3]. For example, the spillover effect between sectors was observed during the global <sup>fi</sup>nancial crisis and the recent Chinese stock market crash. Consider the manufacturing sector and the utility sector in the Chinese stock market. Between June and July 2015, the manufacturing sector index<sup>1</sup> decreased by 29.96%, and the utility sector index decreased by 24.93%. The manufacturing sector suffered a much heavier loss than the utility sector. In market interactions, companies in the manufacturing sector have more business connections with other companies than companies in the utility sector. To understand market interactive structures and to explain the spillover effect between sectors, we designed this study.

Previous accounting and <sup>fi</sup>nance studies have begun to establish the connection between market network structure and stock sector performance [1–3]. They have used trading data to create sector relationship graphs, and they have proposed the theory that sectoral shocks are transmitted to other sectors using networks of input and output linkages. However, the trade <sup>fl</sup>ow graphs are rather coarse tools for describing company relationships. In the <sup>fi</sup>eld of information systems (IS), some studies have

K. Chen et al. / Information & Management xxx (2016) xxx–xxx

constructed company relationship networks based on textual information mining. They have identi<sup>fi</sup>ed the co-occurrences of two companies’ names in documents [4–8]. This method helps to measure the closeness of two companies, but it cannot specify the types of comparative relationship, i.e., competitive relations or cooperative relations. In a real-world market, the relationship between Apple and Samsung is de<sup>fi</sup>nitely different from that between Apple and FoxCom. These different relationships have different spillover effects on stock performance. Therefore, to further investigate the connections between market network structure and stock sector performance, we focus on the following research questions.

(1) Does the company comparative network provide a stronger market indicator than the company closeness network?

(2) What are the intra-sector and inter-sector network effects on stock sector performance?

(3) What are the dynamics of the relationship between company comparative network metrics and stock sector performance?

To answer these questions, we use public news<sup>2</sup> as a data source to build company networks because we believe that as an easily accessed Web-based data source, news describes richer business relationships between companies than simple trading data. Moreover, to identify network effects, we construct complex network metrics. First, we use comparative analysis, rather than co-occurrence analysis, to investigate the cooperative (positive) and competitive (negative) relationships identi<sup>fi</sup>ed by public information. Second, we construct inter-sector and intra-sector measurements to compare their different effects.

In contrast to previous studies that aimed to detect the static correlations between company network and stock performances, our study uses a vector autoregression with exogenous variables (VARX) model to consider all of the intricate dynamic relationships among network metrics and stock sector performance. The timeseries model investigates continuous daily company network effects on stock sector performance, and it captures the dynamics of short- and long-term carryover effects over time.

This study has potential implications for theory and practice. Theoretically, our work con<sup>fi</sup>rms and extends <sup>fi</sup>nancial theories by introducing rich market network structure metrics based on public information. We use a time-series model to investigate the dynamic relationships between company comparative networks and stock sector performance. Our research also provides practical suggestions for sector-level strategies such as industry associations and investments.

We <sup>fi</sup>rst describe the theoretical background and hypotheses in Section 2. Section 3 introduces the data and the measurements. Section 4 describes the time-series model. The <sup>fi</sup>ndings are presented in Section 5. The <sup>fi</sup>nal section discusses the implications.

## 2. Theoretical background and hypotheses

2.1. Intra-sector and inter-sector network effects on stock sector performance

Stock sector performance has been demonstrated to be related to sector positions in market networks. In the <sup>fi</sup>nance domain, Aobdia, Caskey, and Ozel [3] constructed an industry network based on trade <sup>fl</sup>ows across different industries, and they found that <sup>fi</sup>rms in central industries are more exposed to systemic risks than other <sup>fi</sup>rms. Acemoglu et al. [1] argued that sectoral risks can be transmitted to other sectors through a network of input and output linkages in a system. Ahern and Harford [2] demonstrated that systematic risks constitute the aggregation of idiosyncratic shocks and that more central sectors in a network of intersectoral trade usually have higher returns because they experience greater exposure to systematic risks.

Because of the popularity of social media and Web 2.0, company interactions regarding sales, debts, and other <sup>fi</sup>nancial or operating activities are reported in public news in real time. Company networks based on keyword co-occurrence have been widely used to explain and predict <sup>fi</sup>nancial metrics such as company revenue; stock return; and risk. For example; Ma; Sheng; and Pant [6] predicted company revenue relationships based on a company network derived from company citations. Graph-theoretic measurements were used in the classi<sup>fi</sup>cation problem. Jin et al. [5] developed complex longitudinal features for company network evolution and proposed feature selection and prediction models to predict company pro<sup>fi</sup>t and revenue growth. Focusing on stock market performance; Creamer; Ren; and Nickerson [9] tested the relationships among company positions in networks; company stock returns; and volatility.

We expect that constructing sector-related metrics based on company networks might also provide a useful indicator for predicting sector performance. Compared with trade <sup>fl</sup>ow, which has been used in previous <sup>fi</sup>nancial studies [2,3], company networks encompass broader business relationships between companies.

H1a. Sector interaction metrics constructed based on company networks have signi<sup>fi</sup>cant predictive relationships with sector performance.

To further investigate the sector-interactive characteristics, we construct two metrics: an inter-sector metric and an intra-sector metric. These two metrics have primarily been used in economics to distinguish trades between different industries or within the same industry [10,11]. These sector metrics have also been used in <sup>fi</sup>nancial studies that have investigated stock performances. Moskowitz and Grinblatt [12] and Aobdia, Caskey, and Ozel [3] demonstrated that inter-sector characteristics have predictive power for assessing <sup>fi</sup>rms’ stock returns. Conversely, Asness, Porter, and Stevens [13] found that intra-sector momentum is superior to inter-sector momentum in explaining stock returns. Because this study aims to inspect how sector-interactive characteristics affect stock returns, we followed the two popular metrics and proposed two competing hypotheses:

H1b. The inter-sector metric has greater predictive power than the intra-sector metric.

H1b’. The intra-sector metric has greater predictive power than the inter-sector metric.

## 2.2. Company comparative networks provide a stronger market indicator than closeness networks

In the business world, company comparative analysis refers to evaluating a list of company metrics to compare them. The targets are usually similar companies in the same industry, such as Ford versus Toyota and eBay versus Amazon. In IS and marketing research, comparative analysis has been extended to the analysis of comparative opinions between two entities [14–16]. Taking products as an example, comparative analysis aims to identify the relationship of two products as “product A is better than product B” or “product B is better than product A.” For example, Jindal and Liu [17,18] proposed using rules and naïve Bayes classi<sup>fi</sup>ers to identify comparative sentences and relationships in these sentences. Xu et al. [19] used a conditional random <sup>fi</sup>eldbased method to extract the comparative relationships between products from a sentence. Zhang et al. [8] proposed a sentiment analysis method for constructing product comparison networks on a coarse-granularity level. In a company analysis scenario, comparative analysis refers to identifying the relationships between companies, including competitive relationships and cooperative relationships. These relations are often hidden in news reports and other public information. Similar to previous sentiment analysis, competitive relationships usually exhibit negative comparative opinions, and cooperative relationships often feature positive comparative opinions.

Although company comparative relationship networks are assumed to constitute a good market indicator, there is little evidence that supports this assumption. Inter-company relationships are currently extracted from textual news based on the cooccurrence of company names. The more frequently the documents mention two companies together, the closer those companies are to each other. This line of reasoning stems from the notion of memory-associative networks [20], and it has strong roots in the co-word analysis literature [21]. Company cooccurrence networks have been used to analyze company <sup>fi</sup>nancial performance.

On the basis of above analysis, we want to build a company comparative network and compare its market predictive power with that of a company co-occurrence network. Thus, the following hypothesis is posited.

H2a. Company comparative analysis provides a stronger sector interactive indicator than company closeness analysis.

To further investigate the sentiment of comparative opinions, we divide company comparative relationships into two categories: cooperative (or positive) relationships and competitive (or negative) relationships. Sentiment analysis has been widely adopted in <sup>fi</sup>nancial studies to predict stock prices [22]. One research stream uses the polarity value of news as a predictive measure of stock performance, e.g., Li et al. [23], Yu, Duan, and Cao [24], and Tetlock, Saar-Tsechansky, and Macskassy [25]. The other stream inspects the differential impacts of positive and negative news on stocks. For example, Chan [26] found less drift for stocks with good news than for those with bad news. Van [27] found that arrival of bad news had a greater impact on volatility than did arrival of good news. This study aims to investigate whether a difference exists between the impact of cooperative (positive) relationships and competitive (negative) relationships. Thus, we propose the following competing hypotheses.

H2b. Cooperative (positive) sector interactive metrics have greater predictive power than competitive (negative) sector interactive metrics.

H2b . Competitive (negative) sector interactive metrics have greater predictive power than cooperative (positive) sector interactive metrics.

## 2.3. The dynamics of the predictive value of company comparative networks

The previous literature has demonstrated the dynamics of stock market responses to word-of-mouth information and social media Luo, Zhang, and Duan [28] compared the short- and long-term effects of social media with those of conventional online behavioral metrics on a <sup>fi</sup>rm’s equity values. They found that social media metrics have faster predictive value. Additionally, Tirunillai and

Tellis [29] demonstrated that negative user reviews are related to stock returns, with signi<sup>fi</sup>cant wear-in effects. In dynamic analysis, the wear-in time, which is de<sup>fi</sup>ned as the time required to reach the peak predictive value, is valuable because it suggests a critical time period for decision-making, whereas the wear-out time, which is de<sup>fi</sup>ned as the time required before the predictive value reaches asymptotes, indicates the impact duration.

Theoretically, the information diffusion model [30] has been widely used in the <sup>fi</sup>nance domain to explain the dynamic effects of information on stock returns. Hong et al. [31] demonstrated that bad news travels slowly through the investing public. Chan [26] also found that prices are slow to re<sup>fl</sup>ect bad public news. This study aims to investigate the differences in wear-in and wear-out effects on competitive and cooperative relationships. Thus, we propose the following two groups of competing hypotheses.

H3a. Cooperative (positive) sector interactive metrics have a shorter wear-in time than competitive (negative) sector interactive metrics.

H3a . Competitive (negative) sector interactive metrics have a shorter wear-in time than cooperative (positive) sector interactive metrics.

H3b. Cooperative (positive) sector interactive metrics have a longer wear-out time than competitive (negative) sector interactive metrics.

H3b . Competitive (negative) sector interactive metrics have a longer wear-out time than cooperative (positive) sector interactive metrics.

## 3. Data and measurements

## 3.1. Data processing

The raw data set consists of one year (2013) of Chinese business news for 300 companies in the Shanghai–Shenzhen 300 Index.<sup>3</sup> These companies span 10 sectors<sup>4</sup> within the Chinese stock market, including materials, <sup>fi</sup>nance, energy, and daily consumption, among others. The news stories are collected from a general search portal,<sup>5</sup> which covers 3000+ online sources, including discussion boards, news wires, and blogs. To obtain a clear overview of the information sources, we focus on the top 100 online news sources ranked by a number of news items. We <sup>fi</sup>nd that the top 100 online news sources cover 76.89% of the total news items online (the total number of news items is 946,935). Among these sources, we identify 74 news websites, 21 discussion boards, and 5 blogs. Discussion boards have the largest number of news items because anyone can freely post opinions about companies or stocks on discussion boards. From the 74 news websites, we con<sup>fi</sup>rm that the major Chinese <sup>fi</sup>nancial web media is covered. It includes government-operated media, such as renmin.com and xinhua.com, and 4 major security newspapers in China (cs.com.cn, cnstock.com, p52.net, and zqrb.ccstock.cn). The websites also include some popular <sup>fi</sup>nancial portals such as ifeng.com, hexun. com, jinrongjie.com, eastmony.com, business.sohu.com, and <sup>fi</sup>- nance.sina.com.cn. In this paper, we want to use a broad range of big data to identify company relationships. Both regular news and rumors are important for investigating the impact of market information. Therefore, we use a variety of news sources.

In the next step, we perform data clearing to delete repeated or forwarded news. According to the ef<sup>fi</sup>cient market hypothesis (EMH) [32], <sup>fi</sup>nancial markets respond to market information in an ef<sup>fi</sup>cient manner. There are three forms of the EMH (the weak form, the semi-strong form, and the strong form), which differ in terms of the information that can be captured in a market (historical public information, current public information, and hidden information). In agreement with the EMH, we must identify the <sup>fi</sup>rst published news to determine the market time of information. In this step, we use the cosine similarity [33] to compare the similarity of documents. For each news item, we fetch documents within a 30-day time window before and after the news is published. With textual features and the cosine similarity, we compare the similarity of two documents. If the similarity between the two documents is greater than 90%, we assume that the two pieces of news are repeated or forwarded news. The one published later is then deleted. After this step, there are 363,421 news items remaining.

To identify intercompany relationships, we <sup>fi</sup>rst exclude documents that only mention one company or mention more than <sup>fi</sup>ve companies because a document that includes many company names is less important than a document that mentions only a few companies [5]. There are 314,475 news items remaining. The next task is to locate target companies in news stories. In contrast to previous studies [6,7,9,24], which assume that news websites clearly label the news with a target company, we believe that labeling news stories is an important task for cases in which news is collected broadly from the Web. Therefore, we de<sup>fi</sup>ne several rules for identifying target companies. If a company name appears in the title, it is the target company. If no company name appears in the title, we determine the most frequently mentioned target companies by counting the number of times that company names occur.

In the subsequent step, we want to identify comparative opinions between companies using machine-learning methods. In the training procedure, we randomly select 3000 news items, which include 8980 sentences containing company names other than the target companies. Then, we manually label these sentences as depicting positive or negative relationships between the appearing company and the target company. The reasons for only using positive and negative labels have previously been summarized [24]. First, a sentence that includes subjective expressions always implies either positive or negative feelings, and “neutral” is a fairly vague concept. Second, no mature methods exist for ef<sup>fi</sup>ciently and accurately identifying neutral sentiments. Using the labeled dataset, we compute the area under the curve (AUC) [34] of different classi<sup>fi</sup>ers based on a 10-fold crossvalidation.

The receiver operating characteristic (ROC) curve illustrates the performance of a binary classi<sup>fi</sup>er system as its discrimination threshold varies. The curve is created by plotting the true positive rate against the false positive rate at various threshold settings. A ROC curve closer to the top-left corner indicates better dynamic performance. How close the ROC curve is to the top-left corner can be re<sup>fl</sup>ected in the AUC measurement, which is also used as an evaluation metric in this paper.

During implementation, we use the bag-of-words feature model,<sup>6</sup> apply information gain (IG)-based feature selection, and tune the thresholds to test different classi<sup>fi</sup>ers’ performances using different feature sizes. We experiment with several popular machine learning algorithms including support vector machines (SVM), decision trees, random forest, and naïve Bayes. The results are displayed in Fig. 1. From Fig. 1 (a), we <sup>fi</sup>nd that classi<sup>fi</sup>ers perform best on the top 820 features ordered by IG. These 820 features are selected when the threshold of IG is set to 0. Fig. 1 (b) shows that the performance of SVM is much better than that of the other classi<sup>fi</sup>ers $( \mathrm { A U C } _ { \mathrm { S V M } } = 0 . 8 0 3 6 ,$ $\mathsf { A U C } _ { \mathrm { D e c i s i o n \_ T r e e } } = 0 . 6 2 1 8$ ${ \sf A U C } _ { \mathrm { N a i v e \_ B a y e s } } = 0 . 7 0 5 8 ,$ $\mathsf { A U C } _ { \mathrm { R a n d o m \_ F o r e s t } } = 0 . 7 1 0 8 )$ . Therefore, we use the 820 features and train the SVM model to classify company comparative sentences. We identify 13,110 negative relationships and 182,970 positive relationships. The ratio between the positive and negative relationships is supported by previous studies of sentiment classi<sup>fi</sup>cation using user-generated content [29].

## 3.2. Network construction

Each node in the network represents a company, and a direct link indicates a comparative relationship between two companies. The corresponding weight of each link indicates the sentiment strength of the comparison relationship. This network is formally de<sup>fi</sup>ned as follows.

Assume that each sentence in the news for target company c1, along with a mention of company c2, is mapped into a comparison tuple $\boldsymbol { \mathsf { t } } = \{ \mathsf { c } 1 , \mathsf { c } 2 , \mathsf { P } / \mathsf { N } \}$ , where P/N indicates that the comparative opinion from c2 to c1 is positive or negative.

We consider the following methods of network construction.

![](/api/attachments/H2Y9VY8C/fulltext/images/4b661a961d58bdc59c67396284da3c111988bd3d9d7f691705500f8a61bdd6ea.jpg)  
(a) AUC values for different classifiers and feature sizes

![](/api/attachments/H2Y9VY8C/fulltext/images/7384570b9b64033001aaf2f87563e022c0ac122eb68ea8c269683fb7bf9e54b4.jpg)  
(b) ROC curve for a feature size of 820  
Fig. 1. Experimental results for sentiment classi<sup>fi</sup>cation.

## 3.2.1. Company closeness (undirected) networks

All n tuples are aggregated to produce a single link with a weight. An edge between nodes c1 and c2 is introduced when $( N _ { p d } + N _ { n d } ) > 0 ,$ , and the weight of the link is $w = ( N _ { p d } + N _ { n d } ) ,$ <sup>ð þ</sup>where $N _ { p d }$ <sup>¼ ð þ</sup>denotes the number of positive sentences and $N _ { n d }$ denotes the number of negative sentences.

## 3.2.2. Company comparative (directed) networks

We construct two categories of directed networks: positive and negative networks. In a positive network, an edge from node c1 to $^ { c 2 }$ is introduced when $N _ { p d } > 0 ,$ and the weight is $w = N _ { p d } .$ Similarly, when $N _ { n d } > 0 ,$ , we can introduce a link from c1 to c2 and set the weight as $w = N _ { n d }$

## 3.3. Measurements

## 3.3.1. Measurements of stock sector performance

On the basis of previous research [28,35], we use two common measures to determine sector performance: sector return and risk. Return or abnormal return refers to sector stock value beyond what is expected based on the stock market average. Risk, which refers to the vulnerability of sector stock value, can be measured as the standard deviation of the residuals of the returns as follows:

$R _ { i t } - R _ { f t } = \alpha _ { i } + \beta _ { i } \big ( R _ { m t } - R _ { f t } \big ) + \varepsilon _ { i t } , ( 2$ )where t is the subscript for the time period, $R _ { i t }$ is the return of stock i at time t, $R _ { m t }$ is the average market return represented by the Shanghai Security Exchange Composite Index, $R _ { f t }$ is the risk-free rate of return, $\alpha _ { i }$ is the intercept, and $\varepsilon _ { i t }$ is the model residual. Eq. (2) is processed for a rolling window of 250 trading days before the target day. The abnormal return of stock i (AR ) is measured as the difference between the observed return and the expected return, and the risk is the standard deviation of the model residuals as indicated below:

$$
A R _ {i t} = \left(R _ {i t} - R _ {f t}\right) - \left(\alpha_ {i} + \beta_ {i} \left(R _ {m t} - R _ {f t}\right)\right). \tag {3}
$$

## 3.3.2. Measurements of sector interaction metrics

The modularity is de<sup>fi</sup>ned as the fraction of edges that fall within the communities minus the expected value of the same quantity if the edges are assigned at random, conditional on the given community memberships and the degree of the vertices [36]. In previous research, the modularity has primarily been used for evaluating community detection [37,38]. This study introduces the modularity to measure the strength of the connection between the nodes within (or between) groups. We divide stocks into different groups based on the sector to which they belong, and we use the modularity to calculate the intra- and inter-group interactions. When computing the interactions of two groups, we treat the two groups as a whole to yield the modularity value of the entire group.

In the comparative (directed) network, let $c _ { i }$ be the community to which node i is assigned and let $\begin{array} { r } { \boldsymbol { w _ { i } ^ { i n } } = \sum _ { j } \boldsymbol { w _ { j i } } , \boldsymbol { w _ { i } ^ { o u t } } = \sum _ { j } \boldsymbol { w _ { i j } } } \end{array}$ . Then the modularity Q is given by Leicht and Newman [39] as follows:

$\begin{array} { r } { Q = \frac { 1 } { m } { \displaystyle \sum _ { i j } } \bigg [ w _ { i j } - \frac { w _ { j } ^ { i n } w _ { i } ^ { o u t } } { m } \bigg ] \delta ( c _ { i } , c _ { j } ) } \end{array}$ <sub>;(4)where the</sub> d <sub>function</sub> $\delta ( u , v )$ is

1 if $u = v$ and 0 otherwise, and $\begin{array} { r } { m = \sum _ { i j } w _ { i j } } \end{array}$ is the sum of the weights in the entire network.

This formula for the modularity is adjusted to measure the intra- and inter-sector interactions as follows:

$$
Q _ {x} ^ {\prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} ^ {i n} w _ {i} ^ {o u t}}{m} \right] \delta^ {\prime} (c _ {i}, c _ {j})\tag{5}
$$

$$
Q _ {x y} ^ {\prime \prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} ^ {i n} w _ {i} ^ {o u t}}{m} \right] \delta^ {\prime \prime} (c _ {i}, c _ {j})\tag{6}
$$

where $\delta ^ { \prime } ( c _ { i } , c _ { j } )$ is 1 when the two stocks i and j belong to the same sector; otherwise, the value is 0. The value of function $\delta ^ { \prime \prime } ( c _ { i } , c _ { j } )$ equals 1 if the two stocks belong to the two target sectors for which we want to calculate the value of inter-sector interactions; otherwise, the value is 0. In the closeness (undirected) network, according to Newman [40], we can measure the intra- and intersector closeness by replacing the w<sup>in</sup> or $w _ { i } ^ { o u t }$ with the sum of the weights that link node i $\begin{array} { r } { ( w _ { i } = \sum _ { j } w _ { i j } ) } \end{array}$ in Eqs. (5) and (6). The algorithms are presented as follows:

$$
Q _ {x} ^ {\prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} w _ {i}}{m} \right] \delta^ {\prime} (c _ {i}, c _ {j})\tag{7}
$$

$$
Q _ {x y} ^ {\prime \prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} w _ {i}}{m} \right] \delta^ {\prime \prime} (c _ {i}, c _ {j})
$$

8

where $m = 0 . 5 \sum _ { i j } w _ { i j }$ , and the functions of $\delta ^ { \prime } ( c _ { i } , c _ { j } )$ and $\delta ^ { \prime \prime } ( c _ { i } , c _ { j } )$ are the same as those in Eqs. (5) and (6).

## 3.3.3. Measurements of sector news sentiment

According to the EMH [32], stock price re<sup>fl</sup>ects all available market information. To control the in<sup>fl</sup>uences of market momentum on stock performances, we further measure the sentiment of market news [41]. The method of sentiment classi<sup>fi</sup>cation is similar to what we have undertaken in previous comparable relationship mining. We <sup>fi</sup>rst randomly collect 10,000 documents from the news set for labeling. We then select features and perform the test using the labeled data set.<sup>7</sup> With the trained classi<sup>fi</sup>er model, we perform binary classi<sup>fi</sup>cation of the whole news set. Then, we summarize the daily number of positive news about stock as $\boldsymbol { \mathrm { n _ { p } } }$ and the daily number of negative news about stock as $\mathrm { n } _ { \mathrm { n } } .$ The sentiment score of stock on that day is denoted as $n _ { p } - n _ { n }$ . For a sector measurement, the sentiment of individual stock is accumulated. Although other factors that in<sup>fl</sup>uence sector performance exist, as discussed in the conclusions section, we argue that price and market real-time news have covered the most important and popular parts of the available information in measuring an ef<sup>fi</sup>cient market.

## 3.4. An example

Here we provide an example to illustrate the network construction and calculation of sector interaction metrics. First, we focus on stock 00002 (denoted as stock A) and stock 000024 (denoted as stock B). Both are from the <sup>fi</sup>nance sector on December 2, 2013. All the target stocks for the 3 negative links are stock A. Among the 14 positive links, the target stocks of 12 links are A, and the target stocks of the other 2 links are B. As indicated in Fig. 2, when constructing a closeness (undirected) network, only one edge exists between the two stocks, and the weight is $1 7 = 3 + 1 4$ . In the cooperative (positive) network, an edge between B and A exists, and the weight is 12. Simultaneously, an edge runs from A to B, the weight of which is 2. In the competitive (negative) network, the edge between B and A has a weight of 3.

(c) Negative Network  
Table 1  
![](/api/attachments/H2Y9VY8C/fulltext/images/a827dc5c0d93f954ebbbff8627d80aec840b4f6d1e632e6f40fe6c4d26af9141.jpg)  
Fig. 2. Examples of constructing social networks.

Second, we use stock A and stock B on December 2, 2013, to calculate the sector interaction metrics. Taking the undirected network as an example, the total sum of weights on the links in the network is 1521; thus, $m = 1 5 2 1$ . Among all of the links, those with <sup>¼</sup>stock A at one end are used to calculate $\mathsf { W } _ { \mathsf { A } } ,$ , and $\mathsf { W } _ { \mathrm { A } } = 2 1 3$ . Similarly, those that have stock B at one end are used to calculate $\mathsf { W } _ { \mathsf { B } } ,$ and $\mathsf { W } _ { \mathrm { B } } = 2 3$ . The weights of the edges that link both stock A and stock B are used to calculate $\mathsf { W } _ { \mathsf { A B } } ,$ , and $\mathsf { W } _ { \mathsf { A B } } = 1 7 .$ Furthermore, stocks A and B belong to the same sector (<sup>fi</sup>nance); thus, $\delta ^ { \prime } ( c _ { A } , c _ { B } ) = 1$ <sup>ð Þ ¼</sup>Considering other stocks in the <sup>fi</sup>nance sector on the same day, we use Eq. (5) and <sup>fi</sup>nally obtain the intra-sector modularity (intra\_uq) of <sup>fi</sup>nance, which is 0.041.

Given another stock C (601992) that belongs to the materials sector, we can obtain the corresponding values of m=1521, W =213, ${ \sf W } _ { \mathrm { C } } = 5 ,$ , and ${ \mathsf { W } } _ { \mathsf { A C } } = 2$ from the network in a similar manner. The value obtained is accumulated in the inter-sector modularity between materials and <sup>fi</sup>nance. As indicated in Table 1, the intersector modularity between <sup>fi</sup>nance and materials is 0.000306. Fig. 3 displays the relationships in the following three sectors: materials (green), daily consumption (blue), and <sup>fi</sup>nance (red).

In the positive network, the sum of weights is 1448; thus, m = 1448. The links directed to stock A are used for calculating $w _ { A } ^ { i n }$ and the links directed to stock B are used for calculating w<sup>in</sup>: $w _ { A } ^ { i n } = 1 7 2 , w _ { B } ^ { i n } = 8$ . Conversely, the links that start from stock A are <sup>¼ ¼</sup>used for calculatingw<sup>out</sup>, and the links that start from stock B are used for calculating $v _ { B } ^ { o u t } \colon w _ { A } ^ { o u t } = 2 5 , w _ { B } ^ { o u t } = 1 2$ . The weight of the link from A to B is $2 \left( w _ { A B } = 2 \right)$ <sup>¼ ¼</sup>, and the weight of the link from B to A is $1 2 \ ( w _ { B A } = 1 2 )$ <sup>¼</sup>. Because stocks A and B belong to the same <sup>¼fi</sup>nancial sector, the value obtained from Eq. (5) is accumulated in the intra-sector modularity (intra\_pq) of <sup>fi</sup>nance in the positive network as 0.0686.

![](/api/attachments/H2Y9VY8C/fulltext/images/7964d41802857be0aa3aafeca1bdafaad749416cf1742655c1c5d9255ab84658.jpg)  
Fig. 3. Undirected network of three industries

## 4. Econometric model

## 4.1. Rationale for VARX

We employ a VARX model, which is a time-series technique, for an empirical investigation. VARX models include exogenous variables, unlike standard VAR models. VARX models are suitable for examining the dynamics of the relationship between the sector interaction measures and sector performance with the following advantages. First, VARX models are particularly useful for describing interaction and feedback effects for forecasting. They allow for more than one evolving variable. All the variables in the model are treated symmetrically in a structural sense; each variable has an equation that explains its evolution based on its own lags (autoregressive carryover effects) and the lags of the other model variables (cross-effects). In this study, the VARX models capture not only the autoregressive carryover and crosseffects on sector interactions and sector performance but also the control effects of market sentiment. Second, VARX models can track the dynamic cumulative effects of the social network in predicting industry value in the short and long terms using generalized impulse response functions (GIRFs) [42]. This fact is particularly important because GIRFs can uncover dynamic effects that are not observable with other static models. Third, VARX models can assess the relative contributions of the different metrics of social networks using generalized forecast error variance decomposition (GFEVD) [42,43], which is quite helpful for performing hypothesis testing in the study. Recently, VARX models have been broadly adopted in marketing and IS research to investigate the time-series effects of information and economic metrics [28,29,35,44]. Similarly, we use VARX models to estimate complex effects and to determine the full predictive value of social networks.

Intra- and inter-sector modularities.

<table><tr><td>Sector</td><td>Materials (green)</td><td>Daily consumption (blue)</td><td>Finance (red)</td></tr><tr><td>Materials (green)</td><td>0.0045</td><td>-0.00025</td><td>0.00030</td></tr><tr><td>Daily consumption (blue)</td><td>-0.00025</td><td>0.019</td><td>0.00056</td></tr><tr><td>Finance (red)</td><td>0.00030</td><td>0.00056</td><td>0.041</td></tr></table>

Table 2 Sector distribution.

<table><tr><td>Sector ID</td><td>Sector Name</td><td>No. of Stocks</td><td>Missing Days</td></tr><tr><td>1</td><td>Energy</td><td>28</td><td>2</td></tr><tr><td>2</td><td>Materials</td><td>45</td><td>0</td></tr><tr><td>3</td><td>Industry</td><td>56</td><td>0</td></tr><tr><td>4</td><td>Optional consumption</td><td>32</td><td>0</td></tr><tr><td>5</td><td>Daily consumption</td><td>27</td><td>0</td></tr><tr><td>6</td><td>Medical care</td><td>25</td><td>0</td></tr><tr><td>7</td><td>Finance</td><td>54</td><td>0</td></tr><tr><td>8</td><td>Information and technology</td><td>12</td><td>2</td></tr><tr><td>9</td><td>Telecom service</td><td>2</td><td>7</td></tr><tr><td>10</td><td>Utility</td><td>13</td><td>34</td></tr></table>

## 4.2. Model specification

We estimate a VARX model for each sector. The endogenous variables include the sector performance (return and idiosyncratic risk), undirected network metrics (inter-sector modularity value and intra-sector modularity value), positive network metrics (inter-sector modularity value and intra-sector modularity value), and negative network metrics (inter-sector modularity value and intra-sector modularity value). We include only one exogenous variable to control the market sentiment effects on sector performance. The VARX model is speci<sup>fi</sup>ed as follows:

$$
\begin{array}{r l} \left[ \begin{array}{c} \text {Return} _ {t} \\ \text {Risk} _ {t} \\ \text {Intra} _ {U} Q _ {t} \\ \text {Inter} _ {A} U Q _ {t} \\ \text {Intra} _ {P} Q _ {t} \\ \text {Inter} _ {A} P Q _ {t} \\ \text {Intra} _ {N} Q _ {t} \\ \text {Inter} _ {A} N Q _ {t} \end{array} \right] & = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \\ \alpha_ {5} + \delta_ {5} t \\ \alpha_ {6} + \delta_ {6} t \\ \alpha_ {7} + \delta_ {7} t \\ \alpha_ {8} + \delta_ {8} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 8} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 8} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 8} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 8} ^ {k} \\ \phi_ {5, 1} ^ {k} \dots \phi_ {5, 8} ^ {k} \\ \phi_ {6, 1} ^ {k} \dots \phi_ {6, 8} ^ {k} \\ \phi_ {7, 1} ^ {k} \dots \phi_ {7, 8} ^ {k} \\ \phi_ {8, 1} ^ {k} \dots \phi_ {8, 8} ^ {k} \end{array} \right] \\ & . \left[ \begin{array}{c} \text {Return} _ {t - k} \\ \text {Risk} _ {t - k} \\ \text {Intra} _ {U} Q _ {t - k} \\ \text {Inter} _ {A} U Q _ {t - k} \\ \text {Intra} _ {P} Q _ {t - k} \\ \text {Inter} _ {A} P Q _ {t - k} \\ \text {Intra} _ {N} Q _ {t - k} \\ \text {Inter} _ {A} N Q _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \\ \varepsilon_ {6 t} \\ \varepsilon_ {7 t} \\ \varepsilon_ {8 t} \end{array} \right] \end{array}\tag{9}
$$

where $I n t r a _ { U } Q ,$ , Intra Q, and $I n t r a _ { N } Q$ represent the intra-sector modularity values in the undirected network, positive network, and negative network, respectively; $I n t e r _ { A } U Q ,$ $I n t e r _ { A } P Q$ , and $I n t e r _ { A } N Q$ represent the average inter-sector modularity values in the undirected network, positive network, and negative network, respectively; $\alpha _ { i } ( i = 1 , 2 , \cdot \cdot \cdot , 8 )$ are constants; $\delta _ { i } , \phi _ { i , j } ^ { k } ( i , j = 1 , 2 , \cdots , 8 )$ are coef<sup>fi</sup>cients; $\tau _ { 1 , 1 }$ is the coef<sup>fi</sup>cient of the exogenous variable (sector news sentiment) $x _ { 1 t } ;$ K is the lag length, and $\varepsilon _ { i } ( i = 1 , 2 , \cdots , 8 )$ are white-noise residuals.

<sup>ð ¼    Þ</sup>The lag order in the VARX model is usually selected using Schwartz’s Bayesian information criterion (SIC) and the <sup>fi</sup>nal prediction error (FPE) [28,35]. Thus, we select the lag order with the minimized SIC and FPE in each model across 10 industries.

## 5. Estimation result

## 5.1. Time-series data

To prepare the daily data for the time-series analysis, we investigate the daily sector return and risk, in addition to daily

## Table 3

Statistics regarding daily company networks.

<table><tr><td></td><td>Undirected network</td><td>Positive network</td><td>Negative network</td></tr><tr><td>Mean</td><td>137</td><td>133</td><td>30</td></tr><tr><td>Maximum</td><td>276</td><td>274</td><td>116</td></tr><tr><td>Minimum</td><td>87</td><td>84</td><td>12</td></tr><tr><td>Median</td><td>120</td><td>116</td><td>21</td></tr></table>

social networks based on public news. First, we <sup>fi</sup>lter out 6 $\mathrm { \ s t o c k s ^ { 8 } }$ that have experienced long-term trading suspensions during this period. We divide the remaining 294 stocks into 10 sections (Table 2). We calculate the days that a sector does not appear in the company network, which indicates that the company network metrics for the sector are missing for those days. Fortunately, we <sup>fi</sup>nd that few data are missing. The utility sector has 204 valid days of a total of 238 days. We replace these missing data with 0, thus indicating no inter- or intra-sector interactions on that day.

To further investigate the network density, we perform simple statistics for daily <sup>fi</sup>rm networks. As shown in Table 3, the daily <sup>fi</sup>rm network is not quite sparse, considering undirected (company closeness) networks. Even in the smallest network, 87 companies appear. The situation is quite similar for the positive (cooperative company) networks. However, for the negative (competitive company) networks, the nodes are sparse, with a minimum value of 12 companies, because the identi<sup>fi</sup>ed negative relations are much fewer than positive relations. Imbalances between positive and negative opinions have also been found in previous studies of user-generated content [29].

## 5.2. Tests for stationarity in the time series

We conduct stationary and unit root tests to examine the stability of sector performance metrics and company network metrics. These tests investigate whether the variables entering the system evolve continually or are stationary. We conduct augmented Dickey–Fuller (ADF) tests to assess stationarity [45]. As reported in Table 4, except for the risk and news sentiment, the results of ADF testing of all the metrics across 10 sectors are less than the critical value of 2.87, thus leading us to reject the null hypothesis <sup>-</sup>of a unit root at the 95% con<sup>fi</sup>dence level. We use the <sup>fi</sup>rst difference for the risk and sector news sentiment. Furthermore, we <sup>fi</sup>nd that the corrected data series range from 17.83 to 3.29 (Table 3), thereby indicating that the variable series do not co-integrate in equilibrium [28,46].

## 5.3. Tests for granger causality

The results of the Granger causality test [47] are reported in Tables 5 and 6. According to the results, we can conclude that several social network metrics have signi<sup>fi</sup>cant time-based causal relationships with sector performance. In Table 5, the undirected network metrics, including the average inter-sector modularity value and the intra-sector modularity value, can Granger-cause returns in sectors 2, 5, 7, 8, and 10. Additionally, the positive network metrics have strong effects on the returns in sectors 2, 7, and 10. However, the intra-sector modularity value in the negative network is suf<sup>fi</sup>ciently signi<sup>fi</sup>cant to cause a return only in sector 2 $\left( p = 0 . 0 0 5 \right)$ , and the average inter-sector modularity value in the negative network only causes a return in industries 2 and 8 (p = 0.004 and 0.08, respectively).

8

K. Chen et al. / Information & Management xxx (2016) xxx–xxx

Table 4  
Stationarity test of the endogenous variables.

<table><tr><td>Sector</td><td>Return</td><td>ΔRisk</td><td>Δns</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>-13.24</td><td>-14.85</td><td>-8.70</td><td>-15.13</td><td>-15.13</td><td>-15.34</td><td>-15.30</td><td>-13.74</td><td>-13.35</td></tr><tr><td>2</td><td>-17.10</td><td>-11.94</td><td>-6.25</td><td>-15.07</td><td>-15.02</td><td>-15.69</td><td>-15.62</td><td>-4.39</td><td>-4.39</td></tr><tr><td>3</td><td>-17.83</td><td>-6.94</td><td>-5.30</td><td>-14.82</td><td>-14.8</td><td>-14.2</td><td>-14.24</td><td>-15.77</td><td>-15.81</td></tr><tr><td>4</td><td>-15.34</td><td>-10.71</td><td>-5.66</td><td>-12.65</td><td>-12.33</td><td>-13.18</td><td>-12.85</td><td>-14.80</td><td>-14.76</td></tr><tr><td>5</td><td>-14.76</td><td>-12.61</td><td>-5.14</td><td>-12.26</td><td>-12.33</td><td>-12.49</td><td>-12.48</td><td>-13.80</td><td>-13.86</td></tr><tr><td>6</td><td>-13.79</td><td>-14.40</td><td>-3.65</td><td>-8.31</td><td>-8.23</td><td>-8.3</td><td>-8.25</td><td>-12.76</td><td>-12.72</td></tr><tr><td>7</td><td>-15.63</td><td>-8.19</td><td>-7.18</td><td>-11.7</td><td>-12.3</td><td>-12.21</td><td>-12.49</td><td>-14.80</td><td>-15.02</td></tr><tr><td>8</td><td>-14.76</td><td>-13.68</td><td>-3.31</td><td>-12.24</td><td>-12.49</td><td>-12.17</td><td>-12.33</td><td>-14.90</td><td>-15.08</td></tr><tr><td>9</td><td>-15.46</td><td>-13.64</td><td>-10.60</td><td>-3.29</td><td>-5.00</td><td>-14.56</td><td>-5.17</td><td>-15.53</td><td>-15.40</td></tr><tr><td>10</td><td>-13.80</td><td>-13.24</td><td>-5.46</td><td>-14.77</td><td>-14.76</td><td>-14.78</td><td>-14.78</td><td>-15.59</td><td>-15.58</td></tr></table>

Note: Augmented Dickey Fuller (ADF) test statistic critical value: 2.87 (5% level con<sup>fi</sup>dence interval)

Table 5  
Granger causality tests on returns.

<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.43</td><td>0.57</td><td>0.70</td><td>0.79</td><td>0.45</td><td>0.53</td></tr><tr><td>2</td><td>0.02**</td><td>0.01***</td><td>0.02**</td><td>0.02**</td><td>0.005***</td><td>0.004***</td></tr><tr><td>3</td><td>0.45</td><td>0.27</td><td>0.17</td><td>0.09*</td><td>0.97</td><td>0.92</td></tr><tr><td>4</td><td>0.77</td><td>0.17</td><td>0.71</td><td>0.15</td><td>0.61</td><td>0.21</td></tr><tr><td>5</td><td>0.01***</td><td>0.009***</td><td>0.12</td><td>0.13</td><td>0.76</td><td>0.80</td></tr><tr><td>6</td><td>0.09*</td><td>0.13</td><td>0.21</td><td>0.25</td><td>0.61</td><td>0.59</td></tr><tr><td>7</td><td>0.03**</td><td>0.08*</td><td>0.007***</td><td>0.01***</td><td>0.24</td><td>0.21</td></tr><tr><td>8</td><td>0.07**</td><td>0.09*</td><td>0.15</td><td>0.17</td><td>0.4</td><td>0.08*</td></tr><tr><td>9</td><td>0.95</td><td>0.76</td><td>0.95</td><td>0.83</td><td>0.36</td><td>0.36</td></tr><tr><td>10</td><td>0.01***</td><td>0.002***</td><td>0.01***</td><td>0.006***</td><td>0.56</td><td>0.54</td></tr></table>

Note: The estimates of Granger causality are the means of the p-values of the join Wald statistics.  
\*p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

Granger causality tests on risk.

<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.64</td><td>0.45</td><td>0.51</td><td>0.59</td><td>0.56</td><td>0.71</td></tr><tr><td>2</td><td>0.58</td><td>0.71</td><td>0.63</td><td>0.75</td><td> $\mathbf{0.08}^{*}$ </td><td> $\mathbf{0.07}^{*}$ </td></tr><tr><td>3</td><td> $\mathbf{0.002}^{***}$ </td><td> $\mathbf{0.0007}^{***}$ </td><td> $\mathbf{0.01}^{***}$ </td><td> $\mathbf{0.004}^{***}$ </td><td>0.34</td><td>0.42</td></tr><tr><td>4</td><td> $\mathbf{0.003}^{***}$ </td><td> $\mathbf{0.009}^{***}$ </td><td> $\mathbf{0.001}^{***}$ </td><td> $\mathbf{0.007}^{***}$ </td><td>0.41</td><td>0.73</td></tr><tr><td>5</td><td>0.77</td><td>0.67</td><td>0.68</td><td>0.63</td><td>0.86</td><td>0.85</td></tr><tr><td>6</td><td> $\mathbf{0.03}^{**}$ </td><td> $\mathbf{0.01}^{***}$ </td><td>0.72</td><td>0.60</td><td>0.61</td><td>0.64</td></tr><tr><td>7</td><td>0.71</td><td>0.95</td><td>0.52</td><td>0.67</td><td> $\mathbf{0.09}^{*}$ </td><td> $\mathbf{0.07}^{*}$ </td></tr><tr><td>8</td><td>0.65</td><td>0.57</td><td>0.57</td><td>0.80</td><td>0.96</td><td>0.73</td></tr><tr><td>9</td><td>0.84</td><td>0.67</td><td>0.91</td><td>0.69</td><td>0.57</td><td>0.75</td></tr><tr><td>10</td><td>0.16</td><td> $\mathbf{0.06}^{*}$ </td><td>0.19</td><td> $\mathbf{0.09}^{*}$ </td><td> $\mathbf{0.01}^{***}$ </td><td> $\mathbf{0.01}^{***}$ </td></tr></table>

Note: The estimates of Granger causality are the mean of the p-values of the joint Wald statistics.  
\*p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

As indicated in Table 6, the results suggest that the undirected network metrics can cause risk in sectors 3, 4, and 6, followed by the negative network metrics in industries 2, 7, and 10 and the positive network metrics in sectors 3 and 4. These results support H1a in that the sector’s interactive metrics in company networks have predictive power for sector performance.

## 5.4. Short- and long-term relationships between company comparative networks and sector performance

We model the variable dynamics based on GIRFs. In this step, we use the estimated parameters of the VARX model $\phi _ { i , j } ^ { k }$ to generate the GIRFs with $\psi _ { i , j } ( t ) ,$ measuring the net effects of one unit of unexpected change in the social network metrics i on the industry value metric j at time t without assuming a causal ordering [45,48]. We obtain the standard errors by simulating the <sup>fi</sup>tted VARX model using a Monte Carlo method with 1000 runs, and the statistical signi<sup>fi</sup>cance of the parameters is tested. The short-term (immediate predictive value) and long-term (cumulative predictive value) effects are also derived from the GIRFs. We can also assess the dynamics of parameters relative to wear-in time by gauging the number of periods before the peak predictive value is reached and quantify the wear-out time by gauging the number of periods before the stable predictive value is reached.

We <sup>fi</sup>rst investigate the wear-in and wear-out effects on sector performance. Tables 7 and 8 present the results and averages of the outcomes of the time effects between social networks and sector values across 10 industries. From the results, we <sup>fi</sup>nd that negative comparative relationships have a shorter wear-in time on return than positive comparative relationships (F = 6.14, p < 0.01). Simultaneously, negative comparative relationships have a longer wearout time on return than positive comparative relationships

Table 7  
Duration of the short- and long-term impacts on return.

<table><tr><td colspan="7">Wear-in</td><td colspan="6">Wear-out</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td>4</td><td>4</td><td>3</td><td>5</td><td>5</td></tr><tr><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td>6</td><td>4</td><td>4</td><td>6</td><td>7</td></tr><tr><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>7</td><td>7</td><td>6</td><td>6</td><td>8</td><td>8</td></tr><tr><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td></tr><tr><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>2</td><td>2</td><td>8</td><td>8</td><td>7</td><td>8</td><td>8</td><td>9</td></tr><tr><td>6</td><td>4</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td>6</td><td>6</td><td>5</td><td>5</td><td>8</td><td>8</td></tr><tr><td>7</td><td>3</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>4</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>8</td><td>2</td><td>3</td><td>3</td><td>3</td><td>1</td><td>2</td><td>5</td><td>6</td><td>5</td><td>5</td><td>7</td><td>7</td></tr><tr><td>9</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</td><td>6</td></tr><tr><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>4</td><td>4</td><td>10</td><td>9</td><td>9</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Average</td><td>2.8</td><td>3</td><td>2.6</td><td>2.6</td><td>1.5</td><td>1.6</td><td>5.6</td><td>5.9</td><td>5.4</td><td>5.4</td><td>6.8</td><td>7.1</td></tr><tr><td>Test</td><td colspan="6">Intra_pq + Inter_apq &gt; Intra_nq + Inter_anq</td><td colspan="6">Intra_pq + Inter_apq &lt; Intra_nq + Inter_anq</td></tr><tr><td>F-test</td><td colspan="6">6.14***</td><td colspan="6">37.77***</td></tr></table>

Notes: \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005

Table 8  
Duration of the short- and long-term impacts on risk.

<table><tr><td colspan="7">Wear-in</td><td colspan="6">Wear-out</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td><td>3</td><td>6</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>2</td><td>1</td><td>1</td><td>2</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>3</td><td>3</td><td>5</td><td>6</td></tr><tr><td>3</td><td>3</td><td>3</td><td>5</td><td>5</td><td>3</td><td>3</td><td>5</td><td>6</td><td>6</td><td>6</td><td>8</td><td>9</td></tr><tr><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>5</td><td>6</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>3</td><td>8</td><td>9</td><td>8</td><td>8</td><td>9</td><td>9</td></tr><tr><td>6</td><td>3</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>6</td><td>7</td><td>7</td><td>7</td><td>9</td><td>9</td></tr><tr><td>7</td><td>1</td><td>2</td><td>2</td><td>2</td><td>3</td><td>3</td><td>5</td><td>6</td><td>5</td><td>4</td><td>6</td><td>6</td></tr><tr><td>8</td><td>1</td><td>3</td><td>1</td><td>1</td><td>1</td><td>3</td><td>4</td><td>5</td><td>6</td><td>5</td><td>7</td><td>6</td></tr><tr><td>9</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</td><td>6</td><td>7</td><td>7</td></tr><tr><td>10</td><td>8</td><td>8</td><td>8</td><td>8</td><td>6</td><td>6</td><td>9</td><td>8</td><td>9</td><td>9</td><td>10</td><td>10</td></tr><tr><td>Average</td><td>2.6</td><td>2.9</td><td>2.9</td><td>2.9</td><td>2.6</td><td>2.8</td><td>5.5</td><td>5.9</td><td>6</td><td>5.8</td><td>7.3</td><td>7.4</td></tr><tr><td>Test</td><td colspan="6">Intra_pq + Inter_apq &gt; Intra_nq + Inter_anq</td><td colspan="6">Intra_pq + Inter_apq &lt; Intra_nq + Inter_anq</td></tr><tr><td>F-test</td><td colspan="6">0.16</td><td colspan="6">50.79***</td></tr></table>

Notes. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

$( F = 3 7 . 7 7 , p < 0 . 0 1 )$ . Regarding risk measurement, the wear-in time exhibits no signi<sup>fi</sup>cant differences between positive and negative relationships. However, negative comparative relationships do have a longer wear-out time on risk $( F { = } 5 0 . 7 9 , p { < } 0 . 0 1 )$ . This <sup>fi</sup>nding is consistent with previous <sup>fi</sup>nancial studies (Hong et al. [31]) that reported that bad news travels slowly across the public domain and has a longer impact duration. Thus, H3a is partially supported by the sector return, and H3b is well supported by both the sector return and risk.

To further investigate the immediate and cumulative impulsive response elasticities, we calculate the change in basis points (one basis point is one-hundredth of a percentage) of sector return or as a percentage of sector risk in response to one unit of unexpected change in sector interactive metrics [28,29]. Taking the <sup>fi</sup>nance sector (labeled as 7) as an example, Fig. 4 presents the accumulated impulse responses to sector interactive metrics. From the results presented in Tables 9 and 10, we observe that in the undirected network analysis, an unexpected increase in intra-sector closeness will predict a surge in daily sector return by 9.33 basis points in the short term and the accumulated impact of 12.52 basis points in

20 days. However, an unexpected increase in the inter-sector closeness will immediately predict a decrease in the daily sector return by 9.06 basis points $\left( p < 0 . 0 1 \right)$ and accumulated impact of 12.08 basis points $( p < 0 . 1 )$ . In the positive network, the intrasector relationship has positive predictive value with returns both in the short term (11.19 basis points, $p { < } 0 . 1 )$ and the long term (14.52 basis points, $p { < } 0 . 1 )$ . In the negative network, the intrasector relationship is positively related immediately with risk (0.062 basis point, $p < 0 . 1 ) ;$ however, the inter-sector relationship is negatively related immediately with risk ( 0.070 basis point, $p { < } 0 . 1 )$ . Although these effects seem to be small in terms of the number of basis points, they have a substantial impact in terms of the dollar value. In monetary terms, the relationships between company network and sector performance could translate into a signi<sup>fi</sup>cant impact on the market capitalization of the sector [29]. For example, holding other factors constant, for the <sup>fi</sup>nance sector, one unit of unexpected increase in positive intra-sector could add approximately \$11.19 million to the average market capitalization in the short term and could accumulate approximately \$14.52 million over a 20-day period.

![](/api/attachments/H2Y9VY8C/fulltext/images/45269b81ea6308333e6ef4171bafda08934c86e7eb42c8bcc35f13544c6111a8.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/5fb6442ef907d486e6c42b34bb0eff460c6967af7a664b677f5c5639e7286a2c.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/72350fb3d2bbdb9ac261aa4be09f7db94d3c9e5f7d9ab3c1d59be03c50220ee7.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/8a72896f06ab96080711a912ff37020578e03dd1ae18ad40be25acb3d6320faf.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/683988e6c6409eb2d4931ecec6c116cc94db43ad9c31c884a881edfa5ab1e32e.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/f04aec888ce99144c27a40cadfccdb18eca114d6d948b683fc9b7a550679c147.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/9015d63a7e75b75e1a0051f8b076963df7618c83b78d1abecdb3a843483cc0de.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/36161bccd3d5489339fbc186713e2995773bb03727028b7fc36f7f1358183373.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/45152af0e7ff2a0929bc1558d0004e143e5a3f0562bf57a7e033e485bdee027c.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/8981cff01c22e9615e81d6b81fc7cb1b4f7b04ff52c8037f27c838c3991f5240.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/f80acc51ce03f9cc40318207d24eace7cfbd17a3e9910f888f37273783bb1179.jpg)

![](/api/attachments/H2Y9VY8C/fulltext/images/fc9130909b5c02b0db9ad8fde02fd7a828d67a1fafeade6b85cae2d09ece242e.jpg)  
Fig. 4. Accumulated impulse response functions of social network metrics.

Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005

K. Chen et al. / Information & Management xxx (2016) xxx–xxx

Table 12  
Table 9  
Impulse response of return to company network metrics.

<table><tr><td colspan="7">Immediate</td><td colspan="6">Accumulate</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>12.66*</td><td>-12.59*</td><td>14.39*</td><td>-14.59*</td><td>-3.84</td><td>2.89</td><td>12.75*</td><td>-12.79*</td><td>14.86*</td><td>-15.16*</td><td>-4.89</td><td>4.13</td></tr><tr><td>2</td><td>-2.32</td><td>2.69</td><td>-3.06</td><td>3.16</td><td>2.46</td><td>-2.01</td><td>-3.54</td><td>3.14</td><td>-4.26</td><td>3.63</td><td>1.01</td><td>-1.44</td></tr><tr><td>3</td><td>0.573</td><td>-0.852</td><td>2.21</td><td>-2.82</td><td>-3.44</td><td>3.19</td><td>2.32</td><td>-3.28</td><td>4.58</td><td>-6.13</td><td>-7.96</td><td>7.85</td></tr><tr><td>4</td><td>-0.105</td><td>2.85</td><td>-2.14</td><td>5.07</td><td>4.75</td><td>-4.42</td><td>-1.33</td><td>4.34</td><td>-3.32</td><td>6.51</td><td>4.53</td><td>-4.00</td></tr><tr><td>5</td><td>-25.35**</td><td>26.06**</td><td>-20.16*</td><td>19.84*</td><td>-0.196</td><td>-0.67</td><td>-28.62*</td><td>29.33*</td><td>-26.66*</td><td>26.36*</td><td>-0.73</td><td>-0.34</td></tr><tr><td>6</td><td>23.02*</td><td>-21.94*</td><td>14.84</td><td>-14.31</td><td>24.23</td><td>-23.39</td><td>27.83</td><td>-26.41</td><td>19.56</td><td>-18.84</td><td>28.21</td><td>-27.24</td></tr><tr><td>7</td><td>9.33</td><td>-9.06***</td><td>11.19*</td><td>-8.62</td><td>-1.06</td><td>0.544</td><td>12.52</td><td>-12.08*</td><td>14.52*</td><td>-11.92</td><td>-2.90</td><td>2.60</td></tr><tr><td>8</td><td>-8.02</td><td>8.03</td><td>-7.86</td><td>8.89</td><td>-7.32</td><td>16.11</td><td>-5.61</td><td>5.93</td><td>-5.19</td><td>6.41</td><td>-11.42</td><td>20.58</td></tr><tr><td>9</td><td>-3.42</td><td>8.49</td><td>-3.69</td><td>7.78</td><td>10.49</td><td>-4.84</td><td>-1.19</td><td>7.25</td><td>-1.53</td><td>7.47</td><td>15.52</td><td>-6.32</td></tr><tr><td>10</td><td>21.48*</td><td>-21.89*</td><td>21.78*</td><td>-22.5*</td><td>8.84</td><td>-9.11</td><td>21.38</td><td>-21.88</td><td>22.4</td><td>-23.31</td><td>4.27</td><td>-4.43</td></tr></table>

Notes: The coef<sup>fi</sup>cients of returns are in basis points (1 basis point = hundredth of a percentage). \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

Impulse response of risk to company network metrics.

<table><tr><td colspan="7">Immediate</td><td colspan="6">Accumulate</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.116*</td><td>-0.118*</td><td>0.113*</td><td>-0.114*</td><td>0.012</td><td>-0.016</td><td>0.131**</td><td>-0.133**</td><td>0.125**</td><td>-0.127**</td><td>0.027</td><td>-0.031</td></tr><tr><td>2</td><td>0.015</td><td>-0.017</td><td>-0.026</td><td>0.022</td><td>0.122***</td><td>-0.119***</td><td>0.011</td><td>-0.015</td><td>-0.041</td><td>0.037</td><td>0.172**</td><td>-0.175**</td></tr><tr><td>3</td><td>-0.046</td><td>0.055</td><td>-0.004</td><td>0.011</td><td>-0.088**</td><td>0.090**</td><td>-0.075</td><td>0.082</td><td>-0.004</td><td>0.009</td><td>-0.169*</td><td>0.169*</td></tr><tr><td>4</td><td>-0.096***</td><td>0.088***</td><td>-0.105***</td><td>0.089***</td><td>0.010</td><td>-0.0008</td><td>-0.163***</td><td>0.159***</td><td>-0.173***</td><td>0.157***</td><td>-0.015</td><td>0.028</td></tr><tr><td>5</td><td>-0.049</td><td>0.048</td><td>-0.025</td><td>0.021</td><td>0.016</td><td>-0.021</td><td>-0.056</td><td>0.055</td><td>-0.036</td><td>0.031</td><td>0.039</td><td>-0.048</td></tr><tr><td>6</td><td>0.05</td><td>-0.045</td><td>0.074</td><td>-0.072</td><td>-0.015</td><td>0.017</td><td>0.025</td><td>-0.019</td><td>0.068</td><td>-0.065</td><td>-0.081</td><td>0.084</td></tr><tr><td>7</td><td>0.012</td><td>-0.003</td><td>-0.014</td><td>0.016</td><td>0.062*</td><td>-0.070*</td><td>-0.002</td><td>0.007</td><td>-0.030</td><td>0.029</td><td>0.065</td><td>-0.078</td></tr><tr><td>8</td><td>0.027</td><td>-0.015</td><td>0.042</td><td>-0.037</td><td>-0.203*</td><td>0.181*</td><td>0.032</td><td>-0.016</td><td>0.048</td><td>-0.044</td><td>-0.220**</td><td>0.213*</td></tr><tr><td>9</td><td>-0.027</td><td>0.057</td><td>-0.065</td><td>0.087</td><td>0.122</td><td>-0.150</td><td>0.103</td><td>-0.091</td><td>0.079</td><td>-0.054</td><td>0.121</td><td>-0.144</td></tr><tr><td>10</td><td>-0.003</td><td>0.001</td><td>0.005</td><td>-0.008</td><td>-0.084</td><td>0.081</td><td>-0.031</td><td>0.027</td><td>-0.014</td><td>0.008</td><td>-0.143</td><td>0.139</td></tr></table>

Notes: The coef<sup>fi</sup>cients of risk are in basis points (1 basis point = hundredth of a percentage). \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

## 5.5. Relative importance of sector-interactive metrics

We assess the relative impact of the company network metrics on sector performance using GFEVD. The GFEVD estimates are derived using the following algorithm:

$$
\theta_ {i, j} (t) = \frac {\sum_ {k = 0} ^ {t} \left(\psi_ {i , j} (k)\right) ^ {2}}{\sum_ {k = 0} ^ {t} \sum_ {j = 0} ^ {m} \left(\psi_ {i , j} (t)\right) ^ {2}}, i, j = 1, \dots , m.\tag{8}
$$

GFEVD can identify the relative predictive value of all the company network metrics. It is appropriate to test the hypotheses proposed in our article. The relative value of the endogenous variables is established based on GFEVD over 20 days, which is intended to reduce the short-term functions, as suggested in previous research [28,29].

Variance decomposition of return explained by company network metrics

<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.26</td><td>0.58</td><td>0.12</td><td>0.09</td><td>0.21</td><td>0.41</td></tr><tr><td>2</td><td>0.09</td><td>2.18</td><td>0.29</td><td>1.93</td><td>0.76</td><td>3.20</td></tr><tr><td>3</td><td>0.39</td><td>1.40</td><td>0.95</td><td>2.32</td><td>2.25</td><td>0.30</td></tr><tr><td>4</td><td>0.10</td><td>0.08</td><td>0.36</td><td>0.29</td><td>1.10</td><td>0.65</td></tr><tr><td>5</td><td>3.38</td><td>2.52</td><td>1.57</td><td>2.61</td><td>4.83</td><td>0.57</td></tr><tr><td>6</td><td>1.82</td><td>2.05</td><td>1.01</td><td>1.67</td><td>0.17</td><td>0.93</td></tr><tr><td>7</td><td>1.03</td><td>0.37</td><td>0.50</td><td>3.77</td><td>0.13</td><td>1.25</td></tr><tr><td>8</td><td>0.99</td><td>0.73</td><td>1.13</td><td>0.47</td><td>0.17</td><td>2.60</td></tr><tr><td>9</td><td>0.38</td><td>0.56</td><td>0.18</td><td>0.67</td><td>0.44</td><td>1.81</td></tr><tr><td>10</td><td>2.25</td><td>8.78</td><td>2.46</td><td>8.30</td><td>2.54</td><td>2.14</td></tr><tr><td>Average</td><td>1.07</td><td>1.93</td><td>0.86</td><td>2.21</td><td>1.26</td><td>1.39</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ inter_auq</td></tr><tr><td>F-test</td><td colspan="6">26.43***</td></tr><tr><td>Testing</td><td colspan="6">intra_pq+ inter_apq</td></tr><tr><td>F-test</td><td colspan="6">-0.29</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ intra_pq+ intra_nq</td></tr><tr><td>F-test</td><td colspan="6">2.93*</td></tr></table>

Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * }$ p < 0.01.

The GFEVD of return and risk is used to assess the importance of sector interactive metrics, and Tables 11 and 12 provide the results. The results suggest the order of contributions in predicting sector return to be inter\_apq (2.21%), inter\_auq (1.93%), inter\_anq (1.39%), intra\_nq (1.26%), intra\_uq (1.07%), and intra\_pq (0.86%). Similarly, in predicting sector risk, the results of the contributions of the sector interactive metrics are ordered as inter\_apq (1.87%), inter\_auq (1.79%), inter\_anq (1.44%), intra\_uq (1.38%), intra\_pq (1.27%), and intra\_nq (1.01%). On the basis of these results, we acknowledge that the total directed network metrics (the positive

Variance decomposition of risk explained by company network metrics.

<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.92</td><td>1.02</td><td>0.25</td><td>0.64</td><td>1.50</td><td>0.09</td></tr><tr><td>2</td><td>0.08</td><td>0.12</td><td>0.89</td><td>0.42</td><td>0.36</td><td>2.38</td></tr><tr><td>3</td><td>0.34</td><td>1.46</td><td>2.41</td><td>3.38</td><td>1.45</td><td>0.64</td></tr><tr><td>4</td><td>3.80</td><td>0.17</td><td>0.21</td><td>3.93</td><td>0.90</td><td>0.22</td></tr><tr><td>5</td><td>0.93</td><td>0.30</td><td>1.20</td><td>0.94</td><td>0.78</td><td>0.78</td></tr><tr><td>6</td><td>1.35</td><td>5.30</td><td>4.00</td><td>0.90</td><td>0.60</td><td>0.63</td></tr><tr><td>7</td><td>1.80</td><td>0.87</td><td>0.51</td><td>0.49</td><td>0.43</td><td>2.19</td></tr><tr><td>8</td><td>0.30</td><td>2.88</td><td>0.61</td><td>0.87</td><td>0.27</td><td>0.51</td></tr><tr><td>9</td><td>1.28</td><td>1.08</td><td>0.48</td><td>1.53</td><td>1.29</td><td>0.97</td></tr><tr><td>10</td><td>2.96</td><td>4.65</td><td>2.17</td><td>5.62</td><td>2.54</td><td>5.99</td></tr><tr><td>Average</td><td>1.38</td><td>1.79</td><td>1.27</td><td>1.87</td><td>1.01</td><td>1.44</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ inter_auq</td></tr><tr><td>F-test</td><td colspan="6">6.48***</td></tr><tr><td>Testing</td><td colspan="6">intra_pq+ inter_apq</td></tr><tr><td>F-test</td><td colspan="6">-1.14</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ intra_pq+ intra_nq</td></tr><tr><td>F-test</td><td colspan="6">2.63*</td></tr></table>

Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * }$ p < 0.01.

Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005

and negative network metrics) contribute toward a greater proportion of the variance than the total undirected network metrics (5.72% versus 3.00% for return and 5.59% versus 3.17% for risk). According to the F statistics, the differences are statistically signi<sup>fi</sup>cant $( F = 2 6 . 4 3 , p < 0 . 0 1$ for return and $F = 6 . 4 8 , p < 0 . 0 1$ for risk), thereby supporting H2a because comparative analysis provides a stronger network indicator than closeness metrics.

Furthermore, the total inter-sector metrics, including inter\_auq, inter\_apq, and inter\_anq, consist of a greater proportion of the variance than the total intra-sector metrics, including intra\_uq, intra\_pq, and intra\_nq (5.53% versus 3.19% for return and 5.10% versus 3.66% for risk). These differences are statistically signi<sup>fi</sup>cant according to the F statistics $( F { = } 2 . 9 3 , p { < } 0 . 1$ for return and F=2.63, $p < 0 . 1$ for risk). Thus, these results support H1b in that the intersector metrics have greater predictive power than the intra-sector metrics.

However, the relationship between the positive and negative network metrics is not supported. In a variance decomposition of return, the total negative network metrics account for a larger proportion of variance than the average total positive network metrics across the sectors, and adverse results occur in the variance decomposition of risk. The results are not statistically signi<sup>fi</sup>cant.

## 5.6. Robustness testing

We conduct several tests to ascertain the robustness of the results. We use alternative measurements of the inter-sector and intra-sector interactions, in addition to different subsamples of industries for the robustness tests. First, we replace the modularity measurement with the weighted link number to gauge the sector interaction. The intra-sector interaction is measured by the weighted link number among stocks within a sector. The metrics intra\_uln, intra\_pln, and intra\_nln represent the intra-sector weighted link numbers for the undirected network, positive network, and negative network, respectively. Similarly, the intersector interaction is gauged by the weighted link number among stocks that belong to different sectors. The metrics inter\_auln, inter\_apln, and inter\_anln are the inter-sector weighted link numbers for the undirected network, positive network, and negative network, respectively. Because the negative links are less than the positive links, the metrics of the undirected network variables (intra\_uln and inter\_auln) are strongly correlated with the metrics of the positive network variables (intra\_pln and inter\_apln). In this case, we cannot place all the variables into one VARX model. Therefore, we construct two models: model 1 for the undirected company network and model 2 for the directed company network. This construction enables us to compare two models using the adjusted $R ^ { 2 } [ 3 5 , 4 8 ]$

$$
\begin{array}{c} \left[ \begin{array}{c} \text {Return} _ {t} \\ \text {Risk} _ {t} \\ \text {Intra} _ {U} L N _ {t} \\ \text {Inter} _ {A} U L N _ {t} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 4} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 4} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 4} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 4} ^ {k} \end{array} \right] \\ \cdot \left[ \begin{array}{c} \text {Return} _ {t - k} \\ \text {Risk} _ {t - k} \\ \text {Intra} _ {U} L N _ {t - k} \\ \text {Inter} _ {A} U L N _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \end{array} \right] \end{array}\tag{12}
$$

Model 1

11

Using the two models, we obtain the following results. As indicated in Table 13, the $R ^ { 2 }$ value of model 2 is statistically signi<sup>fi</sup>cantly greater than the $R ^ { 2 }$ of model $\cdot \ ( F { = } 9 . 5 9 , \ p { < } 0 . 0 1$ for return and $F { = } 5 . 9 0 , p { < } 0 . 0 1$ for risk), thus supporting H2a in that the competitive analysis provides a stronger network indicator than the closeness metrics. Additionally, the inter-sector metrics (inter\_apln and inter\_anln) account for signi<sup>fi</sup>cantly greater proportions of the variance than the intra-sector metrics (intra\_pln and intra\_nln) in model 2: 2.53% versus 1.81% for return (F=8.03, $p < 0 . 0 1 $ ) and 5.57% versus 4.23% for risk $( F { = } 2 . 8 7 , p { < } 0 . 1 )$ . To further test the dynamic effects of the company comparative network, we calculate the wear-in and wear-out times in model 2. As indicated in Tables 14 and 15, the negative network metrics (intra\_nln and inter\_anln) have signi<sup>fi</sup>cantly shorter wear-in times than the positive network metrics (intra\_pln and inter\_apln): 3.1 days versus 4.0 days for return (F=4.31, $p < 0 . 0 5 )$ and 3.5 days versus 4.7 days for risk $( F { = } 3 . 2 7 , p { < } 0 . 0 5 )$ . The negative network metrics have signi<sup>fi</sup>cantly longer wear-out times than the positive network

$$
\begin{array}{c} \left[ \begin{array}{c} \text {Return} _ {t} \\ \text {Risk} _ {t} \\ \text {Intra} _ {P} L N _ {t} \\ \text {Inter} _ {A} P L N _ {t} \\ \text {Intra} _ {N} L N _ {t} \\ \text {Inter} _ {A} N L N _ {t} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \\ \alpha_ {5} + \delta_ {5} t \\ \alpha_ {6} + \delta_ {6} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 6} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 6} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 6} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 6} ^ {k} \\ \phi_ {5, 1} ^ {k} \dots \phi_ {5, 6} ^ {k} \\ \phi_ {6, 1} ^ {k} \dots \phi_ {6, 6} ^ {k} \end{array} \right] \\ . \left[ \begin{array}{c} \text {Return} _ {t - k} \\ \text {Risk} _ {t - k} \\ \text {Intra} _ {P} L N _ {t - k} \\ \text {Inter} _ {A} P L N _ {t - k} \\ \text {Intra} _ {N} L N _ {t - k} \\ \text {Inter} _ {A} N L N _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \\ \varepsilon_ {6 t} \end{array} \right] \end{array}
$$

Model 2

Results of the VARX model with network link metrics.

<table><tr><td rowspan="2">Sector</td><td colspan="2">Return</td><td colspan="2">Risk</td><td colspan="4">Variance Decomposition of Return</td></tr><tr><td> $R^21$ </td><td> $R^22$ </td><td> $R^21$ </td><td> $R^22$ </td><td>intra_pIn</td><td>inter_apIn</td><td>intra_nIn</td><td>inter_anIn</td></tr><tr><td>1</td><td>0.021</td><td>0.024</td><td>0.043</td><td>0.045</td><td>0.050</td><td>0.119</td><td>0.135</td><td>0.371</td></tr><tr><td>2</td><td>0.068</td><td>0.095</td><td>0.153</td><td>0.177</td><td>1.448</td><td>4.002</td><td>1.875</td><td>2.597</td></tr><tr><td>3</td><td>0.050</td><td>0.072</td><td>0.247</td><td>0.264</td><td>1.156</td><td>0.673</td><td>0.982</td><td>2.075</td></tr><tr><td>4</td><td>0.112</td><td>0.176</td><td>0.300</td><td>0.384</td><td>2.977</td><td>2.628</td><td>2.441</td><td>4.701</td></tr><tr><td>5</td><td>0.043</td><td>0.052</td><td>0.106</td><td>0.124</td><td>0.129</td><td>0.978</td><td>0.497</td><td>0.225</td></tr><tr><td>6</td><td>0.038</td><td>0.041</td><td>0.012</td><td>0.014</td><td>0.157</td><td>0.087</td><td>0.005</td><td>0.358</td></tr><tr><td>7</td><td>0.058</td><td>0.084</td><td>0.174</td><td>0.244</td><td>3.055</td><td>3.071</td><td>2.059</td><td>1.868</td></tr><tr><td>8</td><td>0.026</td><td>0.029</td><td>0.029</td><td>0.033</td><td>0.202</td><td>0.146</td><td>0.203</td><td>0.044</td></tr><tr><td>9</td><td>0.004</td><td>0.006</td><td>0.029</td><td>0.030</td><td>0.115</td><td>0.357</td><td>0.077</td><td>0.054</td></tr><tr><td>10</td><td>0.048</td><td>0.084</td><td>0.064</td><td>0.071</td><td>0.220</td><td>0.577</td><td>0.312</td><td>0.322</td></tr><tr><td>Ave.</td><td>0.047</td><td>0.066</td><td>0.116</td><td>0.139</td><td>0.951</td><td>1.264</td><td>0.859</td><td>1.262</td></tr><tr><td>Testing</td><td colspan="2"> $R^21 < R^22$ </td><td colspan="2"> $R^21 < R^22$ </td><td colspan="4">intra_pIn+ intra_nIn &lt; inter_apIn + inter_anIn</td></tr><tr><td>F-test</td><td colspan="2">9.59***</td><td colspan="2">5.90***</td><td colspan="4">8.03***</td></tr></table>

Table 13  
Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1 .$

<table><tr><td colspan="4">Variance Decomposition of Risk</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr><td>0.580</td><td>0.733</td><td>0.074</td><td>0.142</td></tr><tr><td>1.667</td><td>4.462</td><td>1.278</td><td>1.371</td></tr><tr><td>1.471</td><td>2.649</td><td>0.950</td><td>1.915</td></tr><tr><td>4.585</td><td>4.144</td><td>5.850</td><td>4.450</td></tr><tr><td>0.936</td><td>0.624</td><td>1.094</td><td>1.276</td></tr><tr><td>0.088</td><td>0.340</td><td>0.156</td><td>0.112</td></tr><tr><td>14.136</td><td>20.947</td><td>6.994</td><td>10.271</td></tr><tr><td>0.787</td><td>0.241</td><td>0.092</td><td>0.033</td></tr><tr><td>1.381</td><td>1.322</td><td>0.031</td><td>0.022</td></tr><tr><td>0.103</td><td>0.487</td><td>0.044</td><td>0.125</td></tr><tr><td>2.573</td><td>3.595</td><td>1.656</td><td>1.972</td></tr><tr><td colspan="4">intra_pln + intra_nln &lt; inter_apln + inter_anln 2.87*</td></tr></table>

Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005

Table 14  
Duration of the short- and long-term impacts on return.

<table><tr><td rowspan="2">Sector</td><td colspan="4">Wear-in</td><td rowspan="2">______intra_pln</td><td colspan="4">Wear-out</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td><td></td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr><td>1</td><td>2</td><td>1</td><td>1</td><td>2</td><td>4</td><td></td><td>3</td><td>4</td><td>5</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>8</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>3</td><td>3</td><td>3</td><td>2</td><td>2</td><td>7</td><td></td><td>6</td><td>8</td><td>8</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td></td><td>5</td><td>5</td><td>5</td></tr><tr><td>5</td><td>1</td><td>3</td><td>1</td><td>2</td><td>7</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>6</td><td>2</td><td>1</td><td>1</td><td>2</td><td>5</td><td></td><td>5</td><td>6</td><td>5</td></tr><tr><td>7</td><td>3</td><td>4</td><td>1</td><td>2</td><td>7</td><td></td><td>8</td><td>9</td><td>9</td></tr><tr><td>8</td><td>1</td><td>3</td><td>3</td><td>1</td><td>6</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>9</td><td>1</td><td>1</td><td>1</td><td>1</td><td>5</td><td></td><td>6</td><td>6</td><td>7</td></tr><tr><td>10</td><td>3</td><td>4</td><td>1</td><td>4</td><td>6</td><td></td><td>7</td><td>7</td><td>9</td></tr><tr><td>Average</td><td>1.8</td><td>2.2</td><td>1.3</td><td>1.8</td><td>5.9</td><td></td><td>6.4</td><td>6.9</td><td>7.5</td></tr><tr><td>Test</td><td colspan="4">Intra_pln + inter_apln&gt;Intra_nln + inter_anln</td><td colspan="5">Intra_pln + inter_apln&lt; Intra_nln + inter_anln</td></tr><tr><td>F-test</td><td colspan="4">4.31**</td><td colspan="5">57.45***</td></tr></table>

Table 15  
Duration of the short- and long-term impacts on risk.

<table><tr><td rowspan="2">Sector</td><td colspan="4">Wear-in</td><td rowspan="2">intra_pln</td><td colspan="4">Wear-out</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td><td></td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>5</td><td></td><td>5</td><td>6</td><td>6</td></tr><tr><td>2</td><td>1</td><td>5</td><td>1</td><td>1</td><td>6</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>3</td><td>3</td><td>5</td><td>3</td><td>2</td><td>7</td><td></td><td>8</td><td>8</td><td>8</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td></td><td>4</td><td>5</td><td>5</td></tr><tr><td>5</td><td>2</td><td>1</td><td>3</td><td>1</td><td>6</td><td></td><td>6</td><td>7</td><td>7</td></tr><tr><td>6</td><td>1</td><td>1</td><td>1</td><td>2</td><td>6</td><td></td><td>5</td><td>7</td><td>7</td></tr><tr><td>7</td><td>3</td><td>3</td><td>1</td><td>1</td><td>8</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>8</td><td>1</td><td>5</td><td>1</td><td>5</td><td>7</td><td></td><td>9</td><td>9</td><td>9</td></tr><tr><td>9</td><td>2</td><td>3</td><td>1</td><td>3</td><td>6</td><td></td><td>6</td><td>7</td><td>7</td></tr><tr><td>10</td><td>1</td><td>3</td><td>3</td><td>2</td><td>7</td><td></td><td>8</td><td>9</td><td>9</td></tr><tr><td>Average</td><td>1.8</td><td>2.9</td><td>1.6</td><td>1.9</td><td>6.2</td><td></td><td>6.7</td><td>7.4</td><td>7.6</td></tr><tr><td>Test</td><td colspan="4">Intra_pln + inter_apln&gt; Intra_nln + inter_anln</td><td colspan="5">Intra_pln + inter_apln&lt; Intra_nln + inter_anln</td></tr><tr><td>F-test</td><td colspan="4">3.27**</td><td colspan="5">81.00***</td></tr></table>

metrics: 14.4 days versus 12.3 days for return $( F { = } 5 7 . 4 5 , p { < } 0 . 0 1 )$ and 15 days versus 12.9 days for risk $( F { = } 8 1 . 0 0 , p { < } 0 . 0 1 )$

To control outliers and to determine that our results are not driven by one particular sector, we eliminate one sector at a time on a rolling basis and examine the results. The new results remain similar to the original results. Table 16 presents the consistent variance decomposition results for the data excluding sector 1. UNM refers to the undirected network metrics (intra\_uq and inter\_auq), and DNM denotes the directed network metrics (intra\_pq, inter\_apq, intra\_nq, and inter\_anq). IRAM is the intrasector metrics (intra\_uq, intra\_pq, and intra\_nq), and IERM refers to the inter-sector metrics (inter\_auq, inter\_apq, and inter\_anq).

Variance decomposition of return explained by company network metrics.

<table><tr><td rowspan="2">Sector</td><td colspan="4">Variance Decomposition of Return</td><td colspan="4">Variance Decomposition of Risk</td></tr><tr><td>UNM</td><td>DNM</td><td>IRAM</td><td>IERM</td><td>UNM</td><td>DNM</td><td>IRAM</td><td>IERM</td></tr><tr><td>2</td><td>2.28</td><td>6.18</td><td>1.15</td><td>7.31</td><td>0.19</td><td>4.04</td><td>1.33</td><td>2.91</td></tr><tr><td>3</td><td>1.79</td><td>5.81</td><td>3.59</td><td>4.02</td><td>1.80</td><td>7.88</td><td>4.20</td><td>5.48</td></tr><tr><td>4</td><td>0.18</td><td>2.40</td><td>1.56</td><td>1.02</td><td>3.97</td><td>5.26</td><td>4.91</td><td>4.31</td></tr><tr><td>5</td><td>5.90</td><td>9.58</td><td>9.79</td><td>5.70</td><td>1.24</td><td>3.70</td><td>2.91</td><td>2.03</td></tr><tr><td>6</td><td>3.87</td><td>3.77</td><td>2.99</td><td>4.65</td><td>6.66</td><td>6.12</td><td>5.95</td><td>6.83</td></tr><tr><td>7</td><td>1.40</td><td>5.66</td><td>1.66</td><td>5.39</td><td>2.67</td><td>3.62</td><td>2.73</td><td>3.55</td></tr><tr><td>8</td><td>1.72</td><td>4.37</td><td>2.29</td><td>3.80</td><td>3.18</td><td>2.27</td><td>1.19</td><td>4.26</td></tr><tr><td>9</td><td>0.94</td><td>3.09</td><td>0.99</td><td>3.04</td><td>2.37</td><td>4.27</td><td>3.05</td><td>3.59</td></tr><tr><td>10</td><td>11.03</td><td>15.44</td><td>7.24</td><td>19.22</td><td>7.61</td><td>16.32</td><td>7.67</td><td>16.26</td></tr><tr><td>Average</td><td>3.23</td><td>6.26</td><td>3.47</td><td>6.02</td><td>3.30</td><td>5.94</td><td>3.77</td><td>5.47</td></tr><tr><td>Test</td><td colspan="2">UNM &lt; DNM</td><td colspan="2">IRAM &lt; IERM</td><td colspan="2">UNM &lt; DNM</td><td colspan="2">IRAM &lt; IERM</td></tr><tr><td>F-test</td><td colspan="2">38.77***</td><td colspan="2">2.82*</td><td colspan="2">6.44***</td><td colspan="2">3.20*</td></tr></table>

Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * }$ p < 0.01.

## 6. Discussion and conclusions

This study aims to construct an effective company relationship network using big data and to investigate the dynamic relationships between sector interactions and stock sector performance. The results suggest that company networks constructed based on public news provide predictive indicators for sector performance and that inter-sector interaction has a stronger predictive power than intra-sector interaction. Moreover, in the network construction, comparative analysis provides a better method than closeness analysis. The negative interactions have a shorter reaction time than the positive interactions for return, and they have longer effects for both sector return and risk. These <sup>fi</sup>ndings are also con<sup>fi</sup>rmed using the links as alternative metrics to re<sup>fl</sup>ect the interactions between sectors. Collectively, these <sup>fi</sup>ndings provide important implications for research regarding market structure and stock sector performance.

## 6.1. Theoretical implications

This study contributes to the IS and <sup>fi</sup>nance literature in several aspects. First, the network analysis method has been widely used in IS, focusing on the relationships among social entities, and it is an important addition to standard social and behavioral research. For example, the network effects and personal in<sup>fl</sup>uences relevant to product sales have been investigated [49,50]. Social communication and mood in<sup>fl</sup>uences have been used to study information effects on stock prices [4,51]. In contrast to these studies of social in<sup>fl</sup>uence, the present study focuses on the structure of company comparative networks and demonstrates how sector interactions have a predictive relationship with stock sector performance. The constructed company network is quite different from previous social networks. It describes the relationships between objective entities. The links between nodes are built based on a machinelearning algorithm instead of using observations. The network construction and analysis method inspires social in<sup>fl</sup>uence research from a technical perspective.

Second, we present comparative analysis in network construction. In contrast to previous marketing studies that used comparative analysis for sales predictions [15,52], we examine the predictive power of the company comparative network for stock sector performance. Our study <sup>fi</sup>rst unveils the correlations between the positive (negative) sector interactions and sector performance. Although more positive than negative interactions are found, we observe that the negative interactions have more rapid effects on returns and that they have longer impacts on both returns and risk. Thus, this study motivates us to explore sentiment analysis between sector interactions in IS and <sup>fi</sup>nance.

Finally, previous <sup>fi</sup>nance studies have demonstrated that the network structure between sectors affects sector performance [1– 3]. We agree with this <sup>fi</sup>nding and extend the breadth of research by introducing sector interaction metrics and time-series models. This study investigates both short-term effects and long-term and cumulative effects. Furthermore, we evaluate the dynamic effects of multiple interaction relationships (inter-, intra-, positive, and negative) with VARX models. Thus, this study provides a comprehensive and dynamic approach for both market structure and <sup>fi</sup>nancial research.

## 6.2. Practical implications

This study contributes to sector-level strategies. First, both inter- and intra-sector interactions have predictive power for stock sector performance. This <sup>fi</sup>nding suggests that companies should strengthen their ties within an industry. For example, they can establish industry associations and frequently hold domain conferences. Simultaneously, companies should also encourage interactions between sectors, such as cooperation with companies in upstream or downstream industries.

Second, because the constructed company comparative network signi<sup>fi</sup>cantly in<sup>fl</sup>uences sector performance, companies should pay attention to public media information. They should strengthen efforts to promote public propaganda for improving exposure and should also monitor the company interactive dynamics reported by various media outlets. The shortest wearin time can provide an early warning signal to companies regarding future damage to sector performance, particularly when competitive or negative interactions occur. The company network also provides a good visualization method for understanding the market network structure.

Third, the predictive model contributes to portfolio and risk management. Investors can apply the company comparative analysis and sector interactive analysis methods to predict sector returns and risks on a daily basis.

## 6.3. Limitations and future research

Nevertheless, this study has several limitations that should be addressed in future research. First, we control for few exogenous variables. In this study, we use only news sentiment to control for market environment. In fact, there are many other factors that can have impact on sector performance. For example, the web search volume concerning a stock could indicate a dynamic “hot spot” in the market. Other likely control variables include sector productivity and pro<sup>fi</sup>ts. Second, we have noted that different sectors exhibit different reactions, potentially due to sector properties.

Therefore, analyzing the sector-speci<sup>fi</sup>c results could be an important undertaking. Third, we propose that our results can be applied to portfolio and risk management. We intend to conduct future experiments using real-world data to test the effectiveness of the model for investing.

## Acknowledgement

This paper was supported by the Shenzhen Fundamental Research Grant (No.: JCYJ2010417105742712).

## References

[1] D. Acemoglu, et al., The network origins of aggregate <sup>fl</sup>uctuations, Econometrica 80 (5) (2012) 1977–2016.

[2] K.R. Ahern, J. Harford, The importance of industry links in merger waves, J. Finance 69 (2) (2014) 527–576.

[3] D. Aobdia, J. Caskey, N.B. Ozel, Inter-industry network structure and the crosspredictability of earnings and stock returns, Rev. Account. Stud. 19 (3) (2013) 1191–1224.

[4] B. Han, L. Yang, Social networks, information acquisition, and asset prices Manage. Sci. 59 (6) (2013) 1444–1457.

[5] Y. Jin, et al., Mining dynamic social networks from public news articles for company value prediction, Soc. Netw. Anal. Min. 2 (3) (2012) 217–228.

[6] Z. Ma, O.R. Sheng, G. Pant, Discovering company revenue relations from news: a network approach, Decis. Support Syst. 47 (4) (2009) 408–414.

[7] Z.P. Ma, Gautam Sheng, R.L. Olivia, Mining competitor relationships from online news: a network-based appraoch, Electr. Comm. Res. Appl. 10 (2011) 418–427.

[8] Z.G. Zhang, Chenhui Guo, Paulo Goes, Product comparison networks for competitive analysis of online word-of-mouth, ACM Trans. Manage. Inform. Syst. (TMIS) 3 (4) (2013) 20:1–20:22.

[9] G.G. Creamer, Y. Ren, J.V. Nickerson, Impact of dynamic corporate news networks on asset return and volatility, Social Computing (SocialCom), 2013 International Conference On. 2013. IEEE (2016).

[10] B. Handjiski, Enhancing Regional Trade Integration in Southeast Europe, World Bank Publications, 2010.

[11] R.J. Ruf<sup>fi</sup>n, The Nature and Signi<sup>fi</sup>cance of Intra-industry Trade, 4, Economic and <sup>fi</sup>nancial review-federal reserve Bank of Dallas, 1999, pp. 2–16.

[12] T.J. Moskowitz, G. Mark, Do industries explain momentum? J. Finance 54 (4) (1999) 1249–1290.

[13] C.S. Asness, R.B. Porter, R.L. Stevens, Predicting stock returns using industryrelative firm characteristics. Available at SSRN 213872. (2000).

[14] Y. Chen, Q. Wang, J. Xie, Online social interations: a natural experiment on word of mouth versus observational learning, J. Market. Res. 48 (2) (2011) 238– 254.

[15] Z. Zhang, X. Li, Y. Chen, Deciphering word-of-mouth in social media: textbased metrics of consumer reviews, ACM Trans. Manage. Inform. Syst. (TMIS) 3 (1) (2012) 5.

[16] W. He, et al., A novel social media competitive analytics framework with sentiment benchmarks, Inform. Manage. 52 (7) (2015) 801–812.

[17] N. Jindal, B. Liu, Identifying comparative sentences in text documents, Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2006.

[18] N. Jindal, B. Liu, Mining comparative sentences and relations, AAAI (2006).

[19] K. Xu, et al., Mining comparative opinions from customer reviews for Competitive Intelligence, Decis. Support Syst. 50 (4) (2011) 743–754.

[20] J.R. Anderson, G.H. Bower, Human Associative Memory, Psychology press, 1973.

[21] Q. He, Knowledge discovery through Co-Word analysis, Library Trends 48 (1) (1999) 133–159.

[22] S. Goel, H.A. Shawky, Estimating the market impact of security breach announcements on <sup>fi</sup>rm values, Inform. Manage. 46 (7) (2009) 404–410.

[23] X. Li, et al., News impact on stock price return via sentiment analysis Knowledge-Based Syst. 69 (2014) 14–23.

[24] Y. Yu, W. Duan, Q. Cao, The impact of social and conventional media on <sup>fi</sup>rm equity value: a sentiment analysis approach, Decis. Support Syst. 55 (4) (2013) 919-926

[25] P.C. Tetlock, M. Saar-Tsechansky, S. Macskassy, More than words: quantifying language to measure firms' fundamentals L. Finance 63 (3) (2008) 1437–1467

[26] W.S. Chan, Stock price reaction to news and no-news: drift and reversal after headlines, J. Financial Econ. 70 (2) (2003) 223–260.

[27] P.N. Van, A Good News or Bad News Has Greater Impact on the Vietnamese Stock Market? Banking Academy of Vietnam State Bank of Vietnam. 2015

[28] X. Luo, J. Zhang, W. Duan, Social media and <sup>fi</sup>rm equity value, Inform. Syst. Res. 24 (1) (2013) 146–163.

[29] S. Tirunillai, G. Tellis, Does chatter matter? The impact of online consumer generated content on a <sup>fi</sup>rm’s <sup>fi</sup>nancial performance, Market. Sci. 31 (2) (2012) 198–215.

[30] H. Hong, J.C. Stein, A uni<sup>fi</sup>ed theory of underreaction, momentum trading, and overreaction in asset markets. L. Finance 54 (1999) 2143–2184.

[31] H. Hong, T. Lim, J.C. Stein, Bad news travels slowly: size, analyst coverage, and the pro<sup>fi</sup>tability of momentum strategies, J. Finance 55 (1) (2000) 265–295.

[32] E. Fama, Ef<sup>fi</sup>cient capital markets: a review of theory and empirical work, J. Finance 25 (2) (1970) 383–417

[33] A. Singhal, Modern information retrieval: a brief overview, Bull. IEEE Comput. Soc. Tech. Comm. Data Eng. 24 (4) (2001) 35–43.

[34] K. Dejaeger, T. Verbraken, B. Baesens, Towards comprehensible software fault prediction models using Bayesian network classi<sup>fi</sup>ers, IEEE Trans. Software Eng. 39 (2) (2013) 237–257.

[35] X. Luo, J. Zhang, How do consumer buzz and traf<sup>fi</sup>c in social media marketing predict the value of the <sup>fi</sup>rm? J. Manage. Inform. Syst. 30 (2) (2013) 213–238.

[36] M.E. Newman, M. Girvan, Finding and evaluating community structure in networks, Phys. Rev. E 69 (2) (2004) (026113).

[37] Z. Bu, et al., A fast parallel modularity optimization algorithm (FPMQA) for community detection in online social network, Knowledge-Based Syst. 50 (2013) 246–259.

[38] M.E. Newman, Modularity and community structure in networks, Proc. Natl. Acad. Sci. 103 (23) (2006) 8577–8582.

[39] E.A. Leicht, M.E. Newman, Community structure in directed networks, Phys. Rev. Lett. 100 (11) (2008) (118703).

[40] M.E. Newman, Analysis of weighted networks, Phys. Rev. E 70 (5) (2004) 056131.

[41] E. Rubin, A. Rubin, The impact of business intelligence systems on stock return, Inform. Manage. 50 (2–3) (2013) 67–75.

[42] H.H. Pesaran, Y. Shin, Generalized impulse response analysis in linear multivariate models, Econ. Lett. 58 (1) (1998) 17–29.

[43] G. Koop, M. Pesaran, S. Potter, Impulse response analysis in nonlinear multivariate models, J. Econom. 74 (1996) 119–147.

[44] G. Adomavicius, J. Bockstedt, A. Gupta, Modeling supply-side dynamics of IT components, products, and infrastructure: an empirical analysis using vector autoregression, Inform. Syst. Res. 23 (2) (2012) 397–417.

[45] M.G. Dekimpe, D.M. Hanssens, Sustained spending and persistent response: a new look at long-term marketing pro<sup>fi</sup>tability, J. Market. Res. 36 (4) (1999) 397–412.

[46] J.D. Hamilton, Time Series Analysis, Princeton University Press, Princeton, NJ, 1994.

[47] C. Granger, Investigating causal relations by econometric models and crossspectral methods, Econometrica 37 (3) (1969) 424–438.

[48] S.V. Srinivasan, Koen Marc; Pauwels, Minset metrics in market response models: an integrative approach, J. Market. Res. 47 (3) (2010) 672–684.

[49] G.R. Gonzalez, D.P. Claro, R.W. Palmatier, Synergistic effects of relationship managers' social networks on sales performance, J. Market. 78 (1) (2014) 76– 94.

[50] E. Moretti, Social learning and peer effects in consumption: evidence from movie sales, Rev. Econ. Stud. 78 (1) (2011) 356–393.

[51] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, J. Comput. Sci. 2 (1) (2011) 1–8.

[52] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviewers, Manage. Sci. 57 (8) (2011) 1485–1509.

Kun Chen is an assistant professor in the Department of Finance at South University of Science and Technology of China. She received her Ph.D. from the Department of Information Systems at the City University of Hong Kong. Dr Chen’s research deals with business intelligence, text mining, and big data analytics. She has published in academic journals such as INFORMS Journal on Computing and Journal of Management Information Systems.

Peng Luo is a Ph.D. student in Harbin Institute of Technology. His research focuses on network topology and social networks. Mr. Luo has published in academic journals such as Physica A, Journal of Informetrics, and Management Decisions.

Dongming Xu is a senior lecturer in Business of Information Systems at the University of Queensland Business School and has a Ph.D. in the area of information systems from the City University of Hong Kong. Her interests include research knowledge management, eLearning effectiveness, <sup>fi</sup>nancial monitoring management systems, electronic commerce, and intelligent agent business applications. She has published in academic journals such as Information & Management and Decision Support Systems.

Huaiqing Wang is a professor in the Department of Finance at South University of Science and Technology of China. He is also the Honorary Dean and a Guest Professor of the School of Information Engineering, Wuhan University of Technology, China. He received his Ph.D. from University of Manchester, UK, in 1987. Dr. Wang specializes in research on <sup>fi</sup>nancial intelligence and intelligent systems (such as intelligent <sup>fi</sup>nancial systems, intelligent learning systems, business process management systems, knowledge management systems, conceptual modeling, and ontology). He has published more than 70 international refereed SCI/SSCI journal articles and received more than 700 SCI citations
