---
otero_id: 15868
otero_key: "WCHSQY9U"
title: "Analyzing firm-specific social media and market: A stakeholder-based event analysis framework"
authors: "Shan Jiang; Hsinchun Chen; Jay F. Nunamaker; David Zimbra"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.08.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework

Shan Jiang <sup>a,</sup>⁎, Hsinchun Chen <sup>a</sup>, Jay F. Nunamaker <sup>a</sup>, David Zimbra <sup>b</sup>

<sup>a</sup> Department of Management Information Systems, University of Arizona, McClelland Hall 430, 1130 E. Helen St., P.O. Box 210108, Tucson 85721 AZ, United States <sup>b</sup> Department of Operations Management and Information Systems, Santa Clara University, 500 El Camino Real, Santa Clara, CA 95053, United States

## a r t i c l e i n f o

Article history: Received 18 June 2013 Received in revised form 27 February 2014 Accepted 6 August 2014 Available online xxxx

Keywords: Social media Stakeholder Community identi<sup>fi</sup>cation Market prediction

## a b s t r a c t

Discussion content in <sup>fi</sup>rm-speci<sup>fi</sup>c social media helps managers understand stakeholders' concerns and make informed decisions. Despite such bene<sup>fi</sup>ts, the over-abundance of information online makes it dif<sup>fi</sup>cult to identify and focus on the most important stakeholder groups. In this study, we propose a novel stakeholder-based event analysis framework that uses online stylometric analysis to segment the forum participants by stakeholder groups, and partitions their messages into different time periods of major <sup>fi</sup>rm events to examine how important stakeholders evolve over time. With this approach, we identi<sup>fi</sup>ed stakeholder groups from a sample of six companies in the petrochemical and banking industries, using more than 500,000 online message postings. To evaluate the proposed system, we conducted market prediction within the identi<sup>fi</sup>ed groups, and compared the prediction performance with traditional approaches that did not account for stakeholder groups or events. Results showed that some stakeholder groups identi<sup>fi</sup>ed by our system had stronger relationships with <sup>fi</sup>rms' market performance, compared to the entire set of web forum participants. Incorporating event-induced temporal dynamics further improved the prediction performance.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Firm-speci<sup>fi</sup>c web forums (e.g., Yahoo! Finance Message Board) serve as a specialized social media platform for exchanging investment opinions. A large number of participants in these web forums are company stakeholders with interests in a particular <sup>fi</sup>rm's market performance. They express personal opinions and share investment information in such platforms [25]. Using <sup>fi</sup>rm-speci<sup>fi</sup>c web forums as a proxy, managers may better understand the stakeholders' concerns and make more informed decisions. When major <sup>fi</sup>rm events occur, <sup>fi</sup>rm-speci<sup>fi</sup>c web forums can also become an essential information source for evaluating the impact of events on company stakeholders, allowing more effective managerial responses to be made. However, it is often dif<sup>fi</sup>cult to identify and focus on information from the most important stakeholders due to the vast amount of information posted online.

This study addresses this problem by proposing a stakeholder-based event analysis framework to support managerial decisions regarding <sup>fi</sup>rms' stakeholders and major events. In the proposed framework, forum participants were clustered into stakeholder groups based on their activity characteristics, topics of interest, and stylometric clues. In different stages of events, important stakeholder groups were identi<sup>fi</sup>ed based on their predictive relationships with the company's market performance. We tested the resulting system on six companies' discussion boards and tracked how the importance of different stakeholder groups evolved in response to relevant <sup>fi</sup>rm events.

The remainder of the paper is organized as follows. We <sup>fi</sup>rst provide a review of relevant literature, based upon which research gaps are identi<sup>fi</sup>ed. Next, our stakeholder-based event analysis framework on web forums is presented, which is designed to address these gaps. We then describe two experiments used to evaluate our system, and discuss the results. Finally, conclusions and implications of the study are provided.

## 2. Related works

## 2.1. Stakeholder theory and identification of stakeholder groups

Since the rise of the concept of “stakeholder,” there has been a debate on its de<sup>fi</sup>nitions. In its narrowest de<sup>fi</sup>nition, stakeholders are de<sup>fi</sup>ned as groups of people on whom an organization's survival is dependent [14]. Usually, the narrow de<sup>fi</sup>nition of stakeholders adopts a role-based stakeholder identi<sup>fi</sup>cation that focuses more on groups that hold functional relationships with the <sup>fi</sup>rm, such as customers, employees, and shareholders. In contrast, the broadest de<sup>fi</sup>nition of a stakeholder is “any group or individual who can affect or is affected by the achievement of the organization's objectives” [13]. Stakeholders are identi<sup>fi</sup>ed by “their interest in the corporation, regardless of whether the organization has any corresponding functional interest in them” [28]. From this perspective, participants in <sup>fi</sup>rm-speci<sup>fi</sup>c web forums are all stakeholders. Through analyzing their discussions, managers of a <sup>fi</sup>rm can understand various stakeholder concerns and take informed actions to manage a <sup>fi</sup>rm's reputation in case of events [44].

Traditionally, stakeholder groups are categorized based on their functional roles with the <sup>fi</sup>rm. For example, researchers have used multiple classi<sup>fi</sup>ers to classify stakeholders into functional groups such as customers, employees, and shareholders in web pages [7]. However, within a speci<sup>fi</sup>c functional group, interests and concerns may vary greatly [37]. It has been argued that role-based stakeholder groups may be overly simplistic and does not adequately address the crucial issues managers face in reality [15]. Therefore, researchers have also advocated unsupervised clustering approaches that allow people with similar interests to be grouped together [37]. To directly address their interests and concerns, content-based features such as the terms used in their forum posts can be utilized to capture the major topics of discussions. Also, the association of a stakeholder with a group may be characterized by adoption of similar online communication practices, such as frequency of creating new threads and participating in an existing discussion thread. Stylometric analysis literature also suggests that authors with similar backgrounds and interests tend to have similar writing styles [3]. For these reasons, content-based, forum activity-based and writing style features have been used for identifying and segmenting online groups in social media [1,43].

## 2.2. Social media-based market prediction and analytical techniques

Prior research has extensively studied how stock performance can be predicted based on social media [2,4,8,16,30,40,42]. Common metrics of stock performance indicators include stock return, volatility, and trading volume. These indicators are regressed on various web forum variables in prior time intervals, often in daily basis. The most typical web forum variables include message volume, average message length, sentiment index, and disagreement index. Message volume indicates how many postings are created, indicating the activity level of forum participants. A high message volume in a day is consistently found to result in reduced stock returns the following day [2,8]. Stock volatility, in contrast, has been found to positively correlate to the prior day's message volume [2,8]. Message length denotes the number of words used in a message. A high average message length in a day indicates that forum participants are active. The sentiment index is an aggregated indicator of opinions expressed in discussions, re<sup>fl</sup>ecting whether the overall attitude of forum participants is positive or negative. Researchers have found that the relationship between the sentiment index and next day return is insigni<sup>fi</sup>cant for individual stocks [2,5,8,42]. However, when aggregating industry-wide opinions, sentiments helped predict the return of related aggregated indexes such as the Morgan Stanley High-tech Index [8]. Yu et al. [40] further revealed that the impacts of sentiment on stock return could vary by social media types. The disagreement index, usually de<sup>fi</sup>ned as the variance of message-level sentiment [2,8], measures the extent to which participants' opinions differ. Through disagreement, a trade occurs between a seller and buyer [17]. Therefore, disagreement index may be indicative of trading volume [5].

Several text mining techniques have been employed to analyze textual data in web forums. Sentiment analysis has been extensively used to assess the valence and intensity of opinions in social media texts [2, 8,20]. The techniques can generally be classi<sup>fi</sup>ed as supervised or unsupervised approaches [24]. In supervised approaches, classi<sup>fi</sup>ers are trained based on a set of tagged messages, and then applied to messages of unknown sentiments. For example, Naïve-Bayes and SVM classi<sup>fi</sup>ers were used to classify the forum messages as buy, sell, or hold positions [2,8,40]. An unsupervised approach does not require a manual labeling process. It leverages sentiment lexicons, such as the Senti Word Net (SWN) lexicon [11], to map terms with scores that indicate the term's sentiment valence and intensity [5,33].

Attempts have also been made to <sup>fi</sup>lter out noise and extract the most relevant information from web forums. At the message level, topic analysis or document clustering is often used to group messages of similar topics together [35]. In this approach, the clustering of messages is based on the content-based features, which are mainly term and phrase occurrences. At the user level, forum participants sharing similar characteristics can be grouped by online stylometric analysis. Stylometric analysis extracts stylistic features from texts to construct authorship pro<sup>fi</sup>les for users. In addition to content-based features, stylistic features also include lexical, syntactic and structural feature categories [1,18,43]. Lexical features relate to the character and word usage such as frequency of letters and vocabulary richness [41]. Syntactic features include usage of function words and punctuation. Structural features include the text organization and layout, such as the number of paragraphs. After constructing authorship pro<sup>fi</sup>les, clustering is used to group similar authorship pro<sup>fi</sup>les together.

## 2.3. Event and temporal dynamics of social media

Online discussions in social media show great variations over time, especially when major events occur. This phenomenon is often referred to as the temporal dynamics of social media [39]. The temporal dynamics of social media can be observed in terms of participants, discussion contents, and relationships between social media activity and the real world. The aim of studying the temporal dynamics of social media participants is to understand how different groups of people react to critical social events. Generally, big events attract more people to participate in discussion and change the composition of participants' constituencies. Robinson (2005) conducted a case study on three online forums for two months starting from September 11 [29]. He found that the disaster of 9/11 led to the formation of groups holding different viewpoints in forums. Also, a large number of casual participants were observed immediately after the beginning of September 11. The temporal dynamics of discussion contents has also been studied [9,39]. These studies revealed how people's concerns were affected by events and changed over time. It has been shown that popularity of contents varies over time. Typically, a topic receives attention immediately upon its appearance and reaches its peak within a day. The peak can last for some time and then popularity decreases. When social media activity is used to predict real world phenomena, the predictive relationships may evolve over time. For example, in a movie's pre-production stage, the number of forum postings about a movie is not signi<sup>fi</sup>cantly correlated with the opening strength of the movie, while this relationship becomes signi<sup>fi</sup>- cant during production to release [21]. The changing relationship between social media and the real world can be partially attributed to people's changing attention in response to events [38].

## 2.4. Research gaps

Several gaps can be identi<sup>fi</sup>ed from the literature. First, prior research has suggested that a <sup>fi</sup>rm should address each stakeholder group's concerns individually. Although attempts have been made to classify stakeholder groups into functional groups in business web pages [7], few studies have segmented the participants of <sup>fi</sup>rm-speci<sup>fi</sup>c forums by stakeholder group. As prior research has suggested, signi<sup>fi</sup>- cant noise could be introduced by using the entire web forum for analysis [8,40]. Second, major <sup>fi</sup>rm events can have a great in<sup>fl</sup>uence on stakeholder groups. However, few previous studies have addressed the temporal aspects of social media and examined how stakeholder groups and their relationships with the <sup>fi</sup>rm's market performance changed in response to events.

## 3. System framework

Fig. 1 illustrates the proposed stakeholder-based event analysis framework developed to address the research gaps. The major components of the framework will be discussed next.

![](/api/attachments/WCHSQY9U/fulltext/images/adb90000e3ba1e58443ec66692e12a4be4b47510274f8991222648790bb66766.jpg)  
Fig. 1. Event-based analysis framework of <sup>fi</sup>rm-speci<sup>fi</sup>c web forums.

## 3.1. Stakeholder and topic identification

In this step, we segmented the web forum participants by stakeholder groups. In order for stakeholders to be grouped by their interests in and concerns about the <sup>fi</sup>rm, we followed previous research and used a clustering approach for stakeholder identi<sup>fi</sup>cation [37]. Their message topics were also identi<sup>fi</sup>ed to characterize each stakeholder group. Both the stakeholder and topic identi<sup>fi</sup>cation modules consisted of four steps: feature extraction, principal component analysis, probabilistic clustering, and stakeholder/topic labeling.

In the feature extraction phase, key features were extracted from forum participants or discussion threads to construct feature vectors representing them. Table 1 lists all the features adopted in our research. These features were based on prior online stylometry studies [1,43] and adjusted to web forum contexts. Forum-level and stylistic features were extracted from all the postings of a forum participant to construct his/her feature vector. Forum-level features, including the number of messages and threads, indicate the forum participant's activity level. Stylometric feature categories including lexical, syntactic, structural and contentbased features were also extracted to represent each forum participant's online writing style and word usage. As shown in Table 1, the lexical features characterize each forum participant's character and word usage, such as frequencies of alphabets, digits, and word length distribution. The lexical features also include the lexical richness of an author's vocabulary [34,41]. The syntactic features include the frequencies of punctuation marks and stop-words. The structural features relate to how sentences and paragraphs were organized. The reason for incorporating a stylometric feature category in stakeholder identi<sup>fi</sup>cation was that stylometric features re<sup>fl</sup>ect the writing habits and educational backgrounds of online users. In addition to interests and concerns, different stakeholder groups may also have distinct ways of expressing their opinions. For example, some may use long and extensive discussions in an attempt to in<sup>fl</sup>uence stock prices. Also, recent studies have reported that using stylometric features has resulted in the identi<sup>fi</sup>- cation of user groups that are better for market prediction compared to the groups identi<sup>fi</sup>ed without using stylometric clues [19]. The content-based features include the frequencies of various word and character n-grams. These features were included to help with stakeholder identi<sup>fi</sup>cation, because the typical sets of words and phrases used in forum messages can vary from group to group. For topic identi<sup>fi</sup>cation, forum level features including the number of messages in the thread and the number of unique users in the thread discussion were used to account for the amount of attention given to different topics. Contentbased features for topic instance include word n-grams appearing in each thread because the words and phrases represented the main characteristics of the topics. For all of the word-level content-based features mentioned above, stop-words were <sup>fi</sup>rst removed from the raw text. The remaining terms were then stemmed to unify the in<sup>fl</sup>ections, using the Porter's stemmer [27]. Finally, word-level content-based features were extracted from the stemmed texts. For all other features, raw texts were used directly.

As is common in text processing, the resulting feature vectors suffered from very high dimensionality and correlations, which is unfavorable for clustering [36]. Principal Component Analysis (PCA) is a technique that converts a set of correlated variables into a reduced number of key components that are orthogonal to each other, while maintaining most of the variances in the original data [26]. In this study, the number of PCA components was determined as the minimum number with which cumulative variance exceeded 0.90. After PCA, each forum participant or thread was represented by a PCA vector $\pmb { \nu } = ( \mathrm { f } _ { 1 } , \mathrm { f } _ { 2 } . . . \mathrm { f } _ { \mathrm { N } } )$

The next step was to cluster the reduced vectors into stakeholder or topic groups. Because each thread may have consisted of more than one topic, and each participant may have belonged to multiple stakeholder groups, feature vectors were clustered by EM clustering, which allowed for the probabilistic assignment of each instance to multiple clusters [36]. Compared to Latent Semantic Analysis or Latent Dirichlet Allocation, clustering the PCA vectors representing contents of forum threads was faster, easier to implement, and addressed our problem.

The EM algorithm assumes the following generative process of user pro<sup>fi</sup>le data points. First, one of the K hidden class labels $\mathbf { Z _ { k , \ell } }$ (representing a group of stakeholders or topics) is picked with probability $\mathrm { p } _ { \mathrm { k } } ,$ where ${ \tt p } _ { 1 } + { \tt p } _ { 2 } + \ldots + { \tt p } _ { \tt K } = 1$ . Based on ${ \mathrm { { Z } } } _ { \mathrm { { k } } } ,$ the user or thread pro<sup>fi</sup>le v is sampled according to a Gaussian distribution: $\pmb { \nu } | z _ { \mathrm { k } } \sim \mathcal { N } ( \pmb { \mu _ { \mathrm { k } } } , \pmb { \Sigma _ { \mathrm { k } } } )$ , where $\mu _ { \mathbf { k } }$ is the mean vector and $\Sigma _ { \mathbf { k } }$ is the variance matrix of the distribution. $\backprime =$ $\{ \mathsf { p } _ { \mathrm { k } } , \mu _ { \mathrm { k } } , \pmb { \Sigma } _ { \mathrm { \pmb { k } } } | \mathrm { k } = 1 , 2 , \hdots \mathrm { N } \}$ represents the set of unknown parameters to be estimated. Under the assumption, the log likelihood of observing a set of data points V is

$$
\mathrm{L} (\boldsymbol {\lambda}) = \log \mathrm{p} (\boldsymbol {V} | \boldsymbol {\lambda}) = \sum_ {\boldsymbol {v} \in \boldsymbol {V}} \log \left(\sum_ {\mathrm{j} = 1} ^ {\mathrm{K}} \mathrm{p} \left(\boldsymbol {v} | z _ {\mathrm{j}}\right) \cdot p _ {\mathrm{j}}\right).\tag{1}
$$

The EM algorithm initializes λ and then repeats the following steps:

1) E step: An expected class label for each data point v is calculated based on the following distribution:

$$
\mathrm{p} \left(\mathrm{z} _ {\mathrm{k}} \mid \boldsymbol {v}, \boldsymbol {\lambda}\right) = \mathrm{p} \left(\boldsymbol {v} \mid \mathrm{z} _ {\mathrm{k}}\right) \cdot \mathrm{p} _ {\mathrm{k}} / \sum_ {\mathrm{j} = 1} ^ {\mathrm{K}} \mathrm{p} \left(\boldsymbol {v} \mid \mathrm{z} _ {\mathrm{j}}\right) \cdot \mathrm{p} _ {\mathrm{j}},\tag{2}
$$

The $\mathrm { { Z _ { k } } }$ that leads to the highest probability is selected for the class label of v.

2) M step: Parameter set λ is updated to λ’ by maximizing the lower band of $\operatorname { L } ( \lambda ) \colon$

$$
\boldsymbol {\lambda} ^ {\prime} = \underset {\theta} {\operatorname{argmax}} \sum_ {\boldsymbol {v} \in \boldsymbol {V}} p (z (\boldsymbol {v}) | \boldsymbol {v}, \boldsymbol {\lambda}) \cdot \log p (\boldsymbol {v}, z (\boldsymbol {v}) | \theta),\tag{3}
$$

where z(v) is the expected class label for v from E step.

In our study, when the EM procedure converged, $\mathsf { p } ( \mathsf { z } _ { \mathrm { k } } | \mathsf { v } , \lambda )$ ) was used as assignment weights of each data point v to the clusters ${ \cal Z } _ { 1 } { - \cal Z } _ { \mathrm { K } } .$ To determine K, we utilized Bayesian Information Criterion (BIC) [31] to choose the K that minimizes 2 log L λ<sup>^- </sup> + n log w, where n is the number of instances, w is the number of free parameters in λ that results from choosing K, and λ<sup>^</sup> is the estimated parameter values.

To label thread clusters by topics, key phrases that best distinguished one cluster from others were extracted from each cluster. Similar to the TF-IDF schema in information retrieval that assigns greater weights to terms which are recurrent within a document and rare across the document collection, we assigned representativeness scores (REP) for each term in each cluster. REP for a term w in cluster C was de<sup>fi</sup>ned as:

$$
R E P (w, C) = P R O P (w, C) \cdot \ln (N / N _ {C})\tag{4}
$$

where PROP(w, C) was the proportion of term w among all terms in cluster C, N was the total number of clusters, N was the number of clusters with the proportion of term w being equal to or greater than C. Intuition behind the formula was twofold. First, terms that were found more frequently within each cluster better represented the cluster and hence were assigned higher scores by PROP(w, C). Second, if a term in a cluster appeared less frequently in other clusters, it was more representative of its own cluster and thus received a higher score. After assigning REP scores, terms with top scores were used to infer the topic of each thread cluster. To label user clusters by stakeholders, the topic distribution of messages posted by all participants in a cluster was calculated. Stakeholders were then identi<sup>fi</sup>ed based on their topic distribution.

Social media features extracted for stakeholder and topic identi<sup>fi</sup>cation.

<table><tr><td>Target</td><td>Category</td><td>Sub-category</td><td>Features</td></tr><tr><td rowspan="8">Stakeholder</td><td>Forum-level</td><td>-</td><td># of messages# of threads</td></tr><tr><td rowspan="4">Lexical</td><td>Character-level</td><td># of characters per messageFrequency of alphabetic charactersFrequency of upper case charactersFrequency of digit charactersFrequency of white space charactersFrequency of tab charactersFrequency of letters A(a)-Z(z) (26)Frequency of special characters(21)</td></tr><tr><td>Word-level</td><td># of words per messageFrequency of short words (length &lt; 4)Frequency of characters in wordsAverage word lengthAverage sentence length in terms of charactersAverage sentence length in terms of wordsWord length frequency (20)</td></tr><tr><td>Lexical</td><td>Hapax Legomena</td></tr><tr><td>Richness</td><td>Hapax Dislegomena</td></tr><tr><td>Syntactic</td><td>-</td><td>Frequency of punctuationsFrequency of stop-words</td></tr><tr><td>Structural</td><td>-</td><td>Total number of lines per messageTotal number of sentences per messageTotal number of paragraphs per messageFrequency of URLs</td></tr><tr><td>Content-based</td><td>Word-level</td><td>Word n-grams(uni bi tri):Character n-grams(uni bi tri):</td></tr><tr><td rowspan="2">Topic</td><td>Forum level</td><td>-</td><td># of messages# of participants</td></tr><tr><td>Content-based</td><td>Word-level</td><td>Word n-grams(uni bi tri):</td></tr></table>

## 3.2. Event period partitioning

In order to examine the impact of major events on stakeholders, three time windows were constructed to partition web forum messages: “before event,” “during event,” and “after event.” Time windows were constructed as follows. First, the “during event” window was determined based on searching online Wall Street Journal archives. The starting day of the period was determined by the date of the <sup>fi</sup>rst article relevant to the event. For the ending day, announcements that indicated the end of the events were identi<sup>fi</sup>ed. Differing ending days can be selected depending on how an event is de<sup>fi</sup>ned. After determining the duration of the “during event” window, “before event” and “after event” windows were constructed in such a way that each window had an equal number of trading days.

## 3.3. Regression analysis

In regression analysis, stock performance variables are regressed on prior day web forum variables. Dependent variables are daily stock return (RET), volatility (VLT) and trading volume (VOL). The stock return is de<sup>fi</sup>ned as the log difference of the close-to-close stock prices [33]. Volatility is de<sup>fi</sup>ned as the difference between the highest and lowest prices divided by the average of open and close prices [8]. Trading volume is de<sup>fi</sup>ned as log-scaled actual volume. Independent variables were chosen based on previous social media-based market prediction studies [2,8,19,33,42]. They included message volume (MSGVOL), average message length in terms of characters (MSGLEN), sentiment

Please cite this article as: S. Jiang, et al., Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.001

(SENTY) and disagreement (DISAG). Message volume and length were log-scaled. Sentiment scores of messages were evaluated with the SWN lexicon [11]. Daily sentiment was then calculated by averaging the message level sentiment scores of the day. Disagreement is de<sup>fi</sup>ned as the variance of message level sentiments. Assignment weights obtained from EM clustering were used when calculating these independent variables for a speci<sup>fi</sup>c stakeholder group.

The Ef<sup>fi</sup>cient Market Hypothesis has suggested that stock prices adjust to all public information [12]. However, it is commonly agreed that the market is not perfectly ef<sup>fi</sup>cient and it takes some time for the information to be re<sup>fl</sup>ected in the stock prices. Message volume and length re<sup>fl</sup>ect the activity level of forum participants, while sentiment and disagreement re<sup>fl</sup>ect their opinions about the <sup>fi</sup>rms. Since web forum users comprise only a small part of the entire market and the activities and opinions there need time to diffuse, all these variables carry information that is potentially not yet re<sup>fl</sup>ected in the stock prices. Empirically, researchers have observed some predictive relationships between these web forum variables and stock behaviors. In [2], for example, message volume has been found to negatively correlate with next day stock return, and positively correlate with stock volatility and trading volume; average message length and disagreement have been found to positively correlate with next day trading volume; and sentiment has been found to positively correlate with next day volatility and trading volume. Although other relationships have not been found to be statistically signi<sup>fi</sup>cant in prior research, evaluating the web forum variables within individual stakeholder groups may improve the granularity of the measurement and reveal new relationships. Hence we examined all possible relationships between three stock variables and four web forum variables.

In addition to the web forum variables, selected <sup>fi</sup>nancial variables were also included as control variables. For stock return regression, the market return was included to control the overall economic environment, calculated as the log difference of S&P 500 indices in subsequent days [2]. The stock return regression model was formulated as:

$$
\begin{array}{c} R E T _ {t} = \beta_ {0} + \beta_ {1} M S G V O L _ {t - 1, i, j} + \beta_ {2} M S G L E N _ {t - 1, i, j} + \beta_ {3} S E N T Y _ {t - 1, i, j} \\ + \beta_ {4} D I S A G _ {t - 1, i, j} + \beta_ {5} M K T R E T _ {t - 1} + \varepsilon_ {t} \end{array}\tag{5}
$$

where subscripts i and i denoted that web forum variables were evaluated within stakeholder group i in period j (=1,2,3). MKTRET denoted the market return.

In the stock volatility model, we followed the By-Company Volatility Model in [2]. Lagged volatility, lagged volatility in the day of negative return, lagged trading volume, and market return were included as control variables because of the autoregressive property of stock volatility and its high correlation with trading volume [10]. Thus the stock volatility regression model was formulated as:

$$
\begin{array}{r l} & V L T _ {t} = \beta_ {0} + \beta_ {1} M S G V O L _ {t - 1, i, j} + \beta_ {2} M S G L E N _ {t - 1, i, j} + \beta_ {3} S E N T Y _ {t - 1, i, j} \\ & \quad + \beta_ {4} D I S A G _ {t - 1, i, j} + \beta_ {5} V L T _ {t - 1} + \beta_ {6} I (R E T _ {t - 1} <   0) \cdot V L T _ {t - 1} \\ & \quad + \beta_ {7} V O L _ {t - 1} + \varepsilon_ {t}. \end{array}\tag{6}
$$

We also followed past studies for the trading volume model, and included lagged stock return, volatility, trading volume, and market return. Other control variables were day-of-week dummies (MON, TUE, WED, THUR) and a holiday dummy (HOL) indicating if a trading day was right before or after a civic holiday, excluding the case when the trading day was Monday or Friday [2]. The trading volume model was formulated as:

$$
\begin{array}{l} V O L _ {t} = \beta_ {0} + \beta_ {1} M S G V O L _ {t - 1, i, j} + \beta_ {2} M S G L E N _ {t - 1, i, j} + \beta_ {3} S E N T Y _ {t - 1, i, j} \\ \quad + \beta_ {4} D I S A G _ {t - 1, i, j} + \beta_ {5} R E T _ {t - 1} + \beta_ {6} V L T _ {t - 1} + \beta_ {7} V O L _ {t - 1} + \beta_ {8} M K T R E T _ {t - 1} + \\ \quad + \beta_ {9} M O N _ {t} + \beta_ {1 0} T U E _ {t} + \beta_ {1 1} W E D _ {t} + \beta_ {1 2} T H U R _ {t} + \beta_ {1 3} H O L _ {t} \varepsilon_ {t}. \end{array}\tag{7}
$$

## 4. Experiment design

## 4.1. Research test-bed and data preparation

For the experiments, web forum messages were collected from the Yahoo! Finance Message Board. Several reasons motivated the choice of using Yahoo! Message Board as our test-bed. First of all, it provides separate discussion boards for different <sup>fi</sup>rms. This mechanism helped us focus on the users that were most likely to be the stakeholders of a speci<sup>fi</sup>c company. Second, the discussion content is professional and the opinions relate closely to investment and <sup>fi</sup>rms' performance. The quality of message content in Yahoo! Message Board has attracted many researchers to use it as the test-bed for their market prediction research [2,8]. Finally, the number of postings here is much larger than in its competitors such as Ragingbull.com or Investorvillage.com, especially for the companies selected in this study (discussed below). Note that we did not mix the messages from different forums because the same participant may have different IDs or usernames in different platforms, and this would create identity inconsistency in the stakeholder identi<sup>fi</sup>- cation phase. Considering that other forums had very few messages relevant to the companies of interest, using Yahoo! Message Board proved suf<sup>fi</sup>cient for our problem.

To test our stakeholder-based event analysis framework, the “Deepwater Horizon Oil Spill” and “Troubled Asset Relief Program (TARP)” were selected because of their huge societal impact. We expected that events of this magnitude would have a tremendous impact on stakeholders in related web forums. Accordingly, three petrochemical companies and three banking companies with the highest message volumes were selected: British Petroleum (BP), Exxon Mobil, Chevron, Bank of America (BOA), Chase, and Wells Fargo.

Based on the methods described in the previous section, time windows for the two events were constructed, which are summarized in Table 2. The oil spill event was de<sup>fi</sup>ned as starting from the day when the oil leak started, and ending on the day when the well-relief process ended. Since TARP has had long lasting impacts until now, we focused only on its <sup>fi</sup>rst major phase, starting from the day when TARP was signed into law by President George W. Bush, until its Capital Purchase Program (CPP) closed to new investments.

Table 3 summarizes the message collection used in our study. The collection covers the entire events as well as the time windows before and after the events. The size of the data collected for each company was comparable to previous studies on Yahoo! Finance [2,8].

To evaluate the message-level sentiments assigned by SWN, we randomly selected 1000 messages from the entire dataset and asked two judges to manually code their sentiments. The judges were asked to classify the messages as containing “positive,” “negative,” or “neutral” opinions about the <sup>fi</sup>rm or its stock performance. The inter-judge agreement was 85.6%. For those messages upon which the judges agreed, we compared the coded sentiments with the sentiment scores assigned by SWN. As shown in Table 4, the distribution of SWN assigned sentiment scores were quite consistent with the coded sentiments. The results suggested that most of the messages were given valid sentiment scores by our system.

Time window construction for events “Deepwater Horizon Oil Spill” and “TARP.”.

<table><tr><td rowspan="2">Event periods</td><td colspan="2">Event</td></tr><tr><td>Deepwater horizon oil spill</td><td>TARP</td></tr><tr><td>Before event</td><td>11/16/09-04/20/10</td><td>07/11/07-10/03/08</td></tr><tr><td>During event</td><td>04/21/10-09/20/10</td><td>10/04/08-12/31/09</td></tr><tr><td>After event</td><td>09/21/10-02/18/11</td><td>01/01/10-03/30/11</td></tr><tr><td># of trading days</td><td>106 * 3 = 318</td><td>313 * 3 = 939</td></tr></table>

Please cite this article as: S. Jiang, et al., Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.001

Table 6  
Table 3  
Yahoo! <sup>fi</sup>nance board test-bed statistics.

<table><tr><td rowspan="2">Time span</td><td colspan="3">Deepwater horizon oil spill</td><td colspan="3">TARP</td></tr><tr><td colspan="3">11/15/09-02/17/11(14 months)</td><td colspan="3">07/10/07-03/29/11(45 months)</td></tr><tr><td>Company</td><td>BP</td><td>Exxon</td><td>Chevron</td><td>BOA</td><td>Chase</td><td>Wells Fargo</td></tr><tr><td># of messages</td><td>153,725</td><td>21,947</td><td>12,421</td><td>195,481</td><td>99,519</td><td>30,168</td></tr><tr><td># of threads</td><td>34,872</td><td>6743</td><td>4523</td><td>68,356</td><td>31,951</td><td>12,525</td></tr><tr><td># of users</td><td>12,034</td><td>2368</td><td>1531</td><td>28,451</td><td>12,960</td><td>4506</td></tr></table>

## 4.2. Experiment 1: group-wise comparison

In this experiment we tested whether our system was effective in identifying stakeholder groups that showed strong relationships with the market. In the baseline model, web forum metrics were evaluated from the entire discussion. In the stakeholder models, web forum metrics were evaluated only from each stakeholder group. The regression models were trained based on the <sup>fi</sup>rst 50% of all trading days and the learnt coef<sup>fi</sup>cients were used to predict the stock variables in the remaining days. By segmenting the forum participants by stakeholder groups and identifying key groups, noise could be reduced from the discussion content, and thus improve the prediction performance. For example, the identi<sup>fi</sup>cation of “prototypical communication groups” in blog-space resulted in reduced prediction errors of stock prices [6]. Therefore, we proposed the following hypothesis:

H1. Stakeholder models will outperform the baseline models for market prediction.

## 4.3. Experiment 2: period-wise comparison

In this experiment we tested our system's ability to evaluate the impact of events on stakeholder groups and track the evolvement of important stakeholders. In each event period, the stakeholder group with the best prediction performance was identi<sup>fi</sup>ed and combined as a dynamic stakeholder model (even when the best group did not change, the model was re-trained using the <sup>fi</sup>rst 50% trading days of each period to update the regression coef<sup>fi</sup>cients). For the baseline, we used the stakeholder model in experiment 1, where the stakeholder group that had the best performance over the entire experiment periods was chosen. The interests of stakeholder groups and their relationships with a <sup>fi</sup>rm evolve over time [23]. When a big event occurs, stakeholders may reevaluate their impressions of the <sup>fi</sup>rm. By incorporating these stakeholders-related temporal dynamics in analysis, the most important information can be tracked, which should provide the most accurate indicators of the <sup>fi</sup>rms' market performance. Therefore, we proposed the following hypothesis:

H2. Dynamic stakeholder models will outperform the stakeholder models (baseline).

To evaluate the models and test these hypotheses, we used the Mean Squared Errors (MSE) in prediction periods and the Wilcoxon signedrank test. MSE evaluates on average how close the predicted stock performance is to the actual values. The Wilcoxon test is a distribution-free, non parametric statistical test that compares the performance of two models. It has been commonly used in prior <sup>fi</sup>nance prediction research [22,32].

Table 4  
A comparison between coded sentiments and SWN assigned sentiment scores.

<table><tr><td rowspan="2">Coded sentiment</td><td rowspan="2"># of messages</td><td colspan="3">Statistics of SWN sentiment scores</td></tr><tr><td>MEAN</td><td>S.D.</td><td>[5%, 95%] percentiles</td></tr><tr><td>Positive</td><td>293</td><td>5.30</td><td>1.88</td><td>[0.74, 12.48]</td></tr><tr><td>Negative</td><td>351</td><td>-6.82</td><td>2.01</td><td>[-17.41, 2.76]</td></tr><tr><td>Neutral</td><td>212</td><td>-0.01</td><td>1.44</td><td>[-2.14, 2.38]</td></tr></table>

Table 5  
The number of PCA components and clusters in stakeholder and topic identi<sup>fi</sup>cation.

<table><tr><td>Instance</td><td></td><td>BP</td><td>Exxon</td><td>Chevron</td><td>BOA</td><td>Chase</td><td>Wells Fargo</td></tr><tr><td rowspan="2">Thread</td><td># PCA components</td><td>31</td><td>28</td><td>29</td><td>28</td><td>30</td><td>27</td></tr><tr><td># of clusters</td><td>16</td><td>11</td><td>9</td><td>14</td><td>13</td><td>10</td></tr><tr><td rowspan="2">User</td><td># PCA components</td><td>42</td><td>46</td><td>42</td><td>38</td><td>39</td><td>40</td></tr><tr><td># of clusters</td><td>11</td><td>13</td><td>9</td><td>13</td><td>15</td><td>8</td></tr></table>

## 5. Results and discussion

## 5.1. Stakeholder and topic identification

First, forum threads were clustered into topic clusters and users were clustered into stakeholder clusters. Table 5 shows the number of PCA components and clusters resulting from our experiments. Although many clusters were identi<sup>fi</sup>ed, many of them were trivial and very small in size. For simplicity, we only used clusters containing at least 5% of the instances for later analysis.

In topic identi<sup>fi</sup>cation, some clusters identi<sup>fi</sup>ed from different companies shared very similar key phrases, and thus were labeled with the same topic names. As a result, 8 distinct topics were identi<sup>fi</sup>ed in total. Table 6 summarizes all the identi<sup>fi</sup>ed topics and their key phrases. Generally, “investment” was the most popular topic across all companies, with proportions being more than 50% in each board. “Environment,” “oil production,” and “war & con<sup>fl</sup>ict” were unique topics exclusively identi-<sup>fi</sup>ed in oil industry discussions, while “<sup>fi</sup>nancial management” and “policy” were unique in the banking <sup>fi</sup>rms. Lastly, there was a non-negligible amount of spam messages across all the boards.

In stakeholder identi<sup>fi</sup>cation, messages within each stakeholder cluster were <sup>fi</sup>rst labeled with the topic assignment values resulting from EM clustering. These values were summed by topics to obtain the proportion of the stakeholder group's messages belonging to each topic. Finally, this topic distribution in each cluster was used to characterize the corresponding stakeholder group. After <sup>fi</sup>ltering the trivial clusters with less than 5% of instances, three major clusters, “investors,” “activists,” and “spam users” were identi<sup>fi</sup>ed across all companies' message boards. “Investors” and “spam users” were characterized by large proportions of the “investment” and “spam” topics respectively, whereas “activists” participated in a more balanced proportion of topics. For example, Fig. 2 shows the identi<sup>fi</sup>ed stakeholder groups and their topic distributions in BP's board. The “activist” group of BP had a higher focus on the “environment” topic. In other companies' boards, the major concerns of the “activist” groups varied (e.g. “banking” for BOA), but all “investors” and “spam users” groups had similar topic distributions.

Identi<sup>fi</sup>ed topic clusters and key phrases.

<table><tr><td>Topic</td><td>Top key phrases</td></tr><tr><td>Investment</td><td>Dividend, cash flow, buy back, stock price, money supply</td></tr><tr><td>Environment</td><td>Environment, greenhouse effect, global warm, shark extinct, clean air act</td></tr><tr><td>Spam messages</td><td>lol, click, http www, ha ha ha</td></tr><tr><td>Oil production</td><td>Import, barrel, crude oil, oil inventory, million barrel day</td></tr><tr><td>Labor</td><td>Wage, employee, sexual orientation, equal employment opportunity</td></tr><tr><td>War &amp; conflicts</td><td>Government, Muslin, white house, gunshot, Saudi Arabia</td></tr><tr><td>Financial mgmt.</td><td>Mortgage, loan, credit card, hedge funding</td></tr><tr><td>Policy</td><td>Government, department treasury, trouble asset relief</td></tr></table>

Please cite this article as: S. Jiang, et al., Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.001

S. Jiang et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/WCHSQY9U/fulltext/images/2278816777e02bbec7640905b02deac14073d074d82089aa90b917ed06133c3e.jpg)

![](/api/attachments/WCHSQY9U/fulltext/images/c2eaa6e997bbcf9d5acf434743fe673dc2dc491fa9f032f3f2bebe1ae70db384.jpg)

![](/api/attachments/WCHSQY9U/fulltext/images/a556a82a940c126af06561f9e9f5a119ea1908e2799e34c412268310f28f70d3.jpg)  
Fig. 2. Characterization of stakeholder groups in BP's board.

## 5.2. Results of experiment 1: group-wise comparison

In this experiment, we trained the regression models using either the entire forum or individual stakeholder groups (investors and activists) identi<sup>fi</sup>ed in the previous step. Due to space limitations, we mainly summarize the qualitative results here. In general, we observed that the individual <sup>fi</sup>rms' stock return was signi<sup>fi</sup>cantly correlated with the prior day message volume (negative, with $\mathsf { p } < 0 . 0 5 )$ and market return (positive, $\mathsf { p } < 0 . 0 1 )$ in all baseline models and stakeholder models for all companies. Stock volatility was signi<sup>fi</sup>cantly correlated with the prior day message volume (positive, $\mathsf { p } < 0 . 0 5 )$ , prior day stock volatility (sign varies, $\mathsf { p } < 0 . 0 5 )$ and trading volume (sign varies, $\mathsf { p } < 0 . 0 1 \AA$ . Trading volume of an individual <sup>fi</sup>rm's stock was signi<sup>fi</sup>cantly correlated with prior day message volume (positive, $\mathsf { p } < 0 . 0 5 )$ , and prior day trading volume (positive, $\mathsf { p } < 0 . 0 1 )$ . These observations were consistent with past market prediction research [2,8]. The $\mathtt { R } ^ { 2 }$ ranged between 0.093 and 0.123 for stock return, and were $0 . 3 4 7  – 0 . 4 1 4$ for volatility and 0.749–0.853 for trading volume, also comparable to past studies and indicating that stock return is dif<sup>fi</sup>cult to predict. In addition, we observed that the signi<sup>fi</sup>cance levels of some web forum variables increased when they were evaluated within some stakeholder groups. For example, in Exxon and Chase, the message volume of the “investor” group had a stronger correlation $\left( \mathbf { p } < 0 . 0 1 \right)$ with the <sup>fi</sup>rm's stock return compared to its baseline $( \mathtt { p } < 0 . 0 5 ) .$ . For BP's stock return, the “activist” group's sentiment was positively signi<sup>fi</sup>cant $\left( \mathtt { p } < 0 . 0 5 \right)$ , while the board's overall sentiment did not show such a relationship. It suggested that evaluating the web forum variables within stakeholder groups could reveal new or strengthened relationships with the stock variables, which may in turn

![](/api/attachments/WCHSQY9U/fulltext/images/589c5358c961785827e3245b9a7c50a3ef2d364dd967467d6565a59df5f21911.jpg)

![](/api/attachments/WCHSQY9U/fulltext/images/cc0de4a95983d68f42307cff105ac44b2e284898946c239d66eba029227f3e17.jpg)

![](/api/attachments/WCHSQY9U/fulltext/images/24b489b54f66a2b8a1d9a830824fbe8351715341db85db27e2e8ac7b7fb9655c.jpg)  
Fig. 3. Comparison of MSEs between baseline model and stakeholder models.

Please cite this article as: S. Jiang, et al., Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.001

S. Jiang et al. / Decision Support Systems xxx (2014) xxx–xxx

Table 7  
Wilcoxon signed-rank tests: “investors” vs the entire forum

<table><tr><td>Company</td><td>BP</td><td>Exxon</td><td>Chevron</td><td>BOA</td><td>Chase</td><td>Wells Fargo</td></tr><tr><td>RET</td><td>5.26 (0.000)</td><td>5.56 (0.000)</td><td>4.62 (0.000)</td><td>6.58 (0.000)</td><td>6.26 (0.000)</td><td>5.90 (0.000)</td></tr><tr><td>VLT</td><td>6.22 (0.000)</td><td>5.18 (0.000)</td><td>5.17 (0.000)</td><td>7.16 (0.000)</td><td>4.73 (0.000)</td><td>5.86 (0.000)</td></tr><tr><td>VOL</td><td>3.11 (0.001)</td><td>4.87 (0.000)</td><td>4.25 (0.000)</td><td>5.17 (0.000)</td><td>4.18 (0.000)</td><td>3.83 (0.000)</td></tr></table>

improve market prediction. To validate this idea, we then compared the prediction performance between the baseline and stakeholder models. Fig. 3 shows the MSE of the models in prediction periods. Overall, we observed that the “investor” groups always had a lower MSE than the baseline or “activist” groups. The “activist” groups generally performed better than the baseline, but sometimes had a higher MSE (e.g. in predicting Chevron's stock return or BP's stock volatility).

We then used the Wilcoxon signed rank test to validate that the prediction errors of the model using “investors” and the baseline model were statistically different. The procedure <sup>fi</sup>rst calculated the differences of absolute prediction errors between the two models (baseline minus “investors”), and ranked the pairs according to the absolute values of the differences (from lower to higher). It then calculated the sum of the ranks where the differences were positive:

$$
W ^ {+} = \sum_ {i = 1} ^ {N} I \left(e _ {\text { baseline }, i} - e _ {\text { investors }, i} > 0\right) \cdot R _ {i}\tag{8}
$$

where N was sample size, $I ( )$ as an indication function that the prediction error of baseline was greater than that of the “investors,” and $R _ { i }$ as the rank of the pair. When the sample size increased, statistic W<sup>+</sup> converged to a normal distribution with a mean of $\mu = \mathrm { n } ( \mathrm { n } + 1 ) / 4$ and a standard deviation of $\sigma = \sqrt { n ( n + 1 ) ( 2 n + 1 ) / 2 4 }$ . Thus the Z statistic was calculated as $Z = ( | W ^ { + } - \mu | - 0 . 5 ) / \sigma .$ High Z values would indicate that the differences of prediction errors between the two models were statistically signi<sup>fi</sup>cant. Table 7 shows the Z statistics and p-values (in parentheses) for all stock variables and all companies. As shown in the table, there were always statistically signi<sup>fi</sup>cant differences between the prediction errors of the baseline and “investor” models. Considering that the MSEs of the models using “investors” were always lower than the baselines (Fig. 3), we can conclude that the stakeholder model using the “investor” group outperformed the baseline, con<sup>fi</sup>rming our Hypothesis 1.

## 5.3. Results of experiment 2: period-wise comparison

Experiment 1 showed that the “investor” group was the most useful group for predicting a <sup>fi</sup>rm's market performance, when prediction was made over all event periods. In experiment 2, we tested if such results still held in each single event period. For example, Fig. 4 shows periodwise MSEs for the “investor” and “activist” groups in BP's board. When predicting BP's stock return and trading volume, the stakeholder group with the best prediction performance shifted from “investors” to “activists” in the during-event period, and shifted back to “investors” after the event. It indicates that during the oil spill event, discussions within the “activists” group were more indicative of BP's stock return and trading volume. For other <sup>fi</sup>rms, we also observed changes of the most useful stakeholder groups in response to events. For example, in Exxon and Chase's boards the best group for predicting trading volume also shifted from “investors” to “activists” in the during-event period, but did not shift back to “investors” after the event. Similar results were observed when predicting BOA and Chase's stock volatility. These changes suggest that relationships between some stakeholder groups and stock behaviors can be affected by major <sup>fi</sup>rm-related events. For space limitations, we omit the plots of the other companies' data in this section.

We then used the Wilcoxon tests to validate that incorporating these changes would result in improved prediction performance. Table 8 shows the Z statistics and p-values resulting from comparing the prediction errors of the dynamic stakeholder model and the baseline model. Results showed that the differences in prediction errors were signi<sup>fi</sup>cant for all stock variables and all companies. Considering that the stakeholder group with the lowest MSE was chosen for each period, we conclude that the dynamic stakeholder model outperformed the baseline model in terms of statistically lower prediction errors, supporting Hypothesis 2.

## 5.4. Suggested use of the system and extensions to a real-time system

Our analyses on what stakeholder groups have been useful in different event periods were done in hindsight. The major use of the resulting system is to show how the importance of a given stakeholder group may shift in response to major <sup>fi</sup>rm events, so that managers can be better prepared for future similar events. For example, the results of experiments 1 and 2 have shown that in most cases the “investors” were the most useful group for market prediction. Experiment 2 has further shown that an “activist” group can sometimes become more important than “investors” when a major <sup>fi</sup>rm event occurs. Therefore,

![](/api/attachments/WCHSQY9U/fulltext/images/5eada09706d6c2e6b88f5e3862aa6d3ff144d798739f94ea37870aed330a7cc4.jpg)  
Fig. 4. Period-wise MSE comparison between investors and activists in BP's board.

Please cite this article as: S. Jiang, et al., Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.001

S. Jiang et al. / Decision Support Systems xxx (2014) xxx–xxx

Table 8  
Wilcoxon signed-rank tests: dynamic stakeholder model vs the baseline model.

<table><tr><td>Company</td><td>BP</td><td>Exxon</td><td>Chevron</td><td>BOA</td><td>Chase</td><td>Wells Fargo</td></tr><tr><td>RET</td><td>6.28 (0.000)</td><td>4.33 (0.000)</td><td>5.82 (0.000)</td><td>3.76 (0.000)</td><td>7.24 (0.000)</td><td>3.02 (0.001)</td></tr><tr><td>VLT</td><td>7.25 (0.000)</td><td>7.18 (0.000)</td><td>6.10 (0.000)</td><td>8.26 (0.000)</td><td>5.69 (0.000)</td><td>4.93 (0.000)</td></tr><tr><td>VOL</td><td>7.12 (0.001)</td><td>4.78 (0.000)</td><td>6.27 (0.000)</td><td>3.77 (0.000)</td><td>6.13 (0.000)</td><td>7.02 (0.000)</td></tr></table>

our suggestion is that a <sup>fi</sup>rm should focus on “investors” by default. When major events that are closely related to the <sup>fi</sup>rm occur, some attention should be given to “activists” whose concerns will center on the event topic, whether it is about the environment, labor concerns, or a political issue. However, the most important group may not switch from “investors” to “activists” when a new type of events occurs and its impact on the <sup>fi</sup>rm is unclear. Moreover, over time, new members may replace the old ones in stakeholder groups.

To this end, it would be more desirable if the system could dynamically adjust the stakeholder identi<sup>fi</sup>cation results and suggest potential groups that will become important in the future, in real time. For a preliminary test of this idea, we modi<sup>fi</sup>ed our system so that it repeated the stakeholder identi<sup>fi</sup>cation step and updated the identi<sup>fi</sup>ed stakeholder groups on a weekly basis to incorporate the latest user pro<sup>fi</sup>les (forum activities and messages up to the adjustment date). The modi<sup>fi</sup>ed system then re-trained the regression models using the past 100 trading days' data (up to the adjustment date), and used the best group resulting from this training interval to predict the market performance for the upcoming week, until the next round of adjustment. Using this setting, we predicted Exxon and BOA's stock return for the entire period again (14 and 45 months, respectively). As a result, the prediction performance of the modi<sup>fi</sup>ed system was signi<sup>fi</sup>cantly better than that of the dynamic stakeholder model in Experiment 1 $( Z _ { \mathrm { E x x o n } } = 5 . 3 5 , \mathrm { p } < 0 . 0 0 1 ;$ $\mathrm { Z _ { B O A } } = 3 . 5 4 , \mathrm { p } < 0 . 0 0 1 )$ . It suggests that adjusting stakeholder identi<sup>fi</sup>cation and the best group's regression coef<sup>fi</sup>cients with shorter intervals is a promising solution for a system that provides decision support for companies in real-time. However, the performance of the modi<sup>fi</sup>ed system was not statistically better than that of the dynamic stakeholder model in Experiment 2. Further improvement may require a more comprehensive tuning of the frequency of updates, and/or to the length of training intervals, which is beyond the scope of this study.

## 6. Conclusion and implications

In this study, we developed an analytical framework that segmented web forum participants into stakeholder groups to examine if analyzing individual stakeholder groups could yield improved stock prediction performance. In most cases, we found that the “investor” group showed the best prediction performance for all stock variables. By further incorporating temporal dynamics into our prediction model, we found that when major <sup>fi</sup>rm events occur, other groups such as “activists” could replace “investors” as a better group for prediction.

Our stakeholder-based event analysis framework makes contributions in many ways. First, it extended prior the research on the relationship between <sup>fi</sup>rm-speci<sup>fi</sup>c web forums and the market by incorporating stakeholder and event analysis. In this way, we provide a venue for restricting social media analysis to the more businessrelevant content. Overall, our dynamic stakeholder model resulted in improved prediction performance compared to baseline models. Second, from a managerial perspective, this study provides an example of how social media can be utilized to better analyze stakeholders' reactions to major <sup>fi</sup>rm events. Our stakeholder-based event analysis framework is best for analyzing historical events and supporting future decisions by “learning from the past”. By analyzing which types of stakeholder groups have been the most important in similar historical events, <sup>fi</sup>rms can be ready for future events and make relatively informed decisions on allocating resources or attention to different stakeholder groups.

Identifying the most important stakeholder groups in real time can be much more dif<sup>fi</sup>cult, as mentioned in the previous section. In this paper, we have done an initial attempt at extending the current framework to a real-time case by updating stakeholder clusters and regression coef<sup>fi</sup>cients on a weekly basis. A more systematic and comprehensive adjustment process is needed to optimize the updating module. That work is left for the future.

## Acknowledgments

The research is based upon the work supported in part by the National Science Foundation under Grant No. CBET-0730908 and by the Defense Threat Reduction Agency under Award No. HDTRA1-09-1- 0058. Thanks to Cathy Larson for her suggestions and comments.

## References

[1] A. Abbasi, H. Chen, J. Nunamaker, Stylometric identi<sup>fi</sup>cation in electronic markets: scalability and robustness, Journal of Management Information Systems 25 (1) (2008) 49–78.

[2] W. Antweiler, M.Z. Frank, Is all that talk just noise? The information content of Internet stock message boards, The Journal of Finance 59 (3) (2004) 1259–1294.

[3] H. Baayen, H. Halteren, A. Neijt, F. Tweedie, An experiment in authorship attribution, Proceedings of JADT 2002: Sixth International Conference on Textual Data Statistical Analysis, (St. Malo, France, 2002), 2002, pp. 69–75.

[4] H. Chen, Business and market intelligence 2.0, part 2, IEEE Intelligent Systems 25 (2) (2010) 74–82.

[5] H. Chen, D. Zimbra, AI and opinion mining, IEEEE Intelligent Systems 25 (3) (2010) 74–80.

[6] M. Choudhury, H. Sundaram, A. John, D. DSeligmann, Extraction, characterization and utility of prototypical communication groups in the blogosphere, ACM transac tion on Information Systems 29 (1) (2010) 1-53

[7] W. Chung, H. Chen, E. Reid, Business stakeholder analyzer: an experiment of classifying stakeholders on the web, Journal of the American Society for Information Science and Technology 60 (1) (2009) 59–74

[8] S. Das, M. Chen, Yahoo! for Amazon: sentiment extraction from small talk on the web, Management Science 53 (9) (2007) 1375–1388.

[9] M. Dubinko, R. Kumar, J. Magnani, J. Novak, P. Raghavan, A. Tomkins, Visualizing tags over time, ACM Transaction on the Web 1 (2) (2007) article 7, 1–22.

[10] R. Engle, A.J. Patton, What good is a volatility model? Quantitative Finance 1 (2) (2001) 237–245.

[11] A. Esuli, F. Sebastiani, SENTIWORDNET: a publicly available lexical resource for opinion mining, Proceedings of the 5th Conference on Language Resources and Evaluation, (Genoa, Italy, 2006), 2006, pp. 417–422.

[12] F. Fama, Ef<sup>fi</sup>cient capital markets: a review of theory and empirical work, Journal of Finance 25 (2) (1970) 383–417.

[13] R. Freeman, Strategic Management: A Stakeholder Approach, Pitman, Marsh<sup>fi</sup>eld MA, 1984.

[14] R. Freeman, D. Reed, Stockholders and stakeholders: a new perspective in corporate governance, California Management Review 25 (1) (1993) 88–106.

[15] D. Gioia, Practicability, paradigms, and problems in stakeholder theorizing, The Academy of Management Review 24 (2) (1999) 228–232

[16] M. Hagenau, M. Liebmann, D. Neumann, Automated news reading: stock price prediction based on <sup>fi</sup>nancial news using context-capturing features, Decision Support Systems 55 (3) (2013) 685–697.

[17] M. Harris, A. Raviv, Differences of opinion make a horse race, The Review of Financial Studies 6 (3) (1993) 473–506

[18] C. Huang, T. Fu, H. Chen, Text-based video content classi<sup>fi</sup>cation for online videosharing sites Journal of the American Society for Information Science and Technology 61 (5) (2010) 891–906.

[19] S. Jiang, H. Chen, A computational approach to detecting and assessing sustainabilityrelated communities in social media, Proceedings of 34th International Conference on Information Systems, (Milan, Italy, 2013), 2013, pp. 1–11.

[20] N. Li, D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems 48 (2) (2010) 354–368.

[21] Y. Liu, C. Yubo, F. Robert, C. Hsinchun, Z. David, S. Zeng, User-generated content on social media: predicting new product market success from online word-of-mouth, IEEE Intelligent Systems 25 (1) (2010) 75-78

[22] C. Lu, T. Lee, C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2) (2009) 115-125

Please cite this article as: S. Jiang, et al., Analyzing <sup>fi</sup>rm-speci<sup>fi</sup>c social media and market: A stakeholder-based event analysis framework, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.00

[23] R. Mitchell, B. Agle, D. Wood, Toward a theory of stakeholder identi<sup>fi</sup>cation and salience: de<sup>fi</sup>ning the principle of who and what really counts, The Academy of Management Review 22 (4) (1997) 853–886.

[24] A. Montoyo, P. Martínez-Barco, A. Balahur, Subjectivity and sentiment analysis: an overview of the current state of the area and envisaged developments, Decision Support Systems 53 (4) (2012) 675–679.

[25] L. O'Connor, Investors' information sharing and use in virtual communities, Journal of the American Society for Information Science and Technology 64 (1) (2013) 36–47.

[26] K. Pearson, On lines and planes of closed <sup>fi</sup>t to system of print in space, Philosophical Magazine 2 (6) (1901) 559–572.

[27] M. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 3 (14) (1980) 130–137.

[28] J. Preble, Toward a comprehensive model of stakeholder management, Business and Society Review 110 (4) (2005) 407–431.

[29] L. Robinson, Debating the events of September 11th: discursive and interactional dynamics in three online fora, Journal of Computer-Mediated Communication 10 (4) (2005).

[30] R. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking <sup>fi</sup>nancial news: the AZFin text system, ACM Transaction on Information Systems 27 (2) (2009) 1–19.

[31] G. Schwarz, Estimating the dimension of a model, The Annals of Statistics 6 (2) (1978) 461–464.

[32] A. Sinha, H. Zhao, Incorporating domain knowledge into data mining classi<sup>fi</sup>ers: an application in indirect lending, Decision Support Systems 46 (1) (2008) 287–299.

[33] P. Tetlock, M. Saar-Tsechansky, S. Macskassy, More than words: quantifying language to measure <sup>fi</sup>rms' fundamentals, The Journal of Finance 63 (3) (2008) 1437–1467.

[34] F. Tweedie, R. Baayen, How variable may a constant be? Measures of lexical richness in perspective, Computers and the Humanities 32 (5) (1998) 323–352.

[35] C. Wei, C. Roger, W. Chen, Accommodating individual preferences in the categorization of documents: a personalized clustering approach, Journal of Management Information Systems 23 (2) (2006) 173–201.

[36] I. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques With Java Implementations, Morgan Kaufmann Publishers, San Fransisco, CA, 2002.

[37] R. Wolfe, D.S. Putler, How tight are the ties that bind stakeholder groups? Organization Science 13 (1) (2002) 64–80.

[38] F. Wu, B.A. Huberman, Novelty and collective attention, PNAS 104 (45) (2007) 17599–17601.

[39] J. Yang, J. Leskovec, Patterns of temporal variation in online media, Proceedings of the fourth ACM international conference on Web search and data mining, (Hong Kong, China, 2011), 2011, pp. 177–186.

[40] Y. Yu, W. Duan, Q. Cao, The impact of social and conventional media on <sup>fi</sup>rm equity value: a sentiment analysis approach, Decision Support Systems 55 (4) (2012) 919–926.

[41] G. Yule, The Statistical Study of Literary Vocabulary, Cambridge University Press, Cambridge, UK, 1944.

[42] Y. Zhang, P. Swanson, W. Prombutr, Measuring effects on stock returns of sentiment indexes created from stock message boards, Journal of Financial Research 35 (1) (2012) 79–114.

[43] R. Zheng, J. Li, H. Chen, Z. Huang, A framework for authorship identi<sup>fi</sup>cation of online messages: writing-style features and classi<sup>fi</sup>cation techniques, Journal of the American Society for Information Science and Technology 57 (3) (2006) 378–393.

[44] S. Zyglidopoulos, N. Phillips, Responding to reputational crises: a stakeholder perspective, Corporate Reputation Review 2 (4) (1999) 333–350.

Shan Jiang is a doctoral student in the Department of Management Information Systems at University of Arizona. He received a B.S. in Management Information Systems from Tsinghua University, China. He is currently working as a research associate in Arti<sup>fi</sup>cial Intelligence Lab, University of Arizona. His research interests include business intelligence social media analytics, computational linguistics and social network analysis.

Hsinchun Chen is Thomas R. Brown Chair Professor in Management and Technology, and Regent's Professor at the University of Arizona. He received a B.S. from the National Chiao-Tung University in Taiwan, an MBA from SUNY Buffalo, and a Ph.D. in Information Systems from New York University. Dr. Chen is a Fellow of IEEE and AAAS. He received the IEEE Computer Society 2006 Technical Achievement Award and the INFORMS Design Science Award in 2008. He is author/editor of 20 books, 25 book chapters, more than 250 journal articles, and more than 150 international conference papers, covering topics such as digital libraries, data/text/web mining, intelligence analysis, cyber crime, and security informatics. He has been an advisor for major National Science Foundation, Department of Justice, Department of Defense, and Department of Homeland Security programs pertaining to digital library, digital government, and national security research.

Jay F. Nunamaker, Jr., is Regents and Soldwedel Professor of MIS, Computer Science and Communication at the University of Arizona. He received his Ph.D. in Systems Engineering and Operations Research from Case Institute of Technology, an M.S. and B.S. in Engineering from the University of Pittsburgh, and a B.S. from Carnegie Mellon University. Dr. Nunamaker received the LEO Award from the Association of Information Systems in 2002. This award is given for a lifetime of exceptional achievement in information systems. He was elected as a fellow of the Association of Information Systems in 2000. Dr. Nunamaker has over 40 years, of experience in examining, analyzing, designing, testing, evaluating, and developing information systems. He has served as a test engineer at the Shipping port Atomic Power facility, as a member of the ISDOS team at the University of Michigan, and as a member of the faculty at Purdue University, prior to joining the faculty at the University of Arizona in 1974.

David Zimbra is an assistant professor in the Department of Operations Management and Information Systems at Santa Clara University. He received M.S. and B.S, in Information Systems from Santa Clara University, and a Ph.D. in Management Information Systems from University of Arizona. His research interests include data, text, and web mining, social media analytics, and business intelligence. His research has appeared in MIS Quarterly, IEEE Intelligent Systems, and the Journal of Computer Mediated Communication. His private sector experience includes work at Ernst & Young and Network Appliance.
