---
otero_id: 16164
otero_key: "YRRKEG6T"
title: "A novel trend surveillance system using the information from web search engines"
authors: "Ze-Han Fang; Chien Chin Chen"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2016.06.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel trend surveillance system using the information from web search engines

Ze-Han Fang, Chien Chin Chen ⁎

Department of Information Management, National Taiwan University, Taiwan

a r t i c l e i n f o

Article history: Received 2 November 2015 Received in revised form 15 April 2016 Accepted 2 June 2016 Available online 11 June 2016

Keywords: Trend surveillance Learning to rank Data mining Feature selection

## a b s t r a c t

Web search engines are becoming a major platform for the general public to access information. It has been suggested that because the search patterns of search engine users are correlated with emerging events, the query log of search engines has the potential for trend surveillance, such as monitoring outbreaks of epidemics. Many trend surveillance studies have investigated the use of query logs and have strived to identify query terms suitable for trend surveillance. Most of these works select representative query terms by consulting domain experts or by preparing a large text corpus for feature selection. The process of these approaches, however, is too costly to make the trend surveillance methods adaptable to different topics. In this paper, we propose an adaptive trend surveillance method. We developed a simple and effective feature selection algorithm, called TF-LTR, which leverages the document returned by search engines and the frequency of the terms in the returned documents to select representative query terms of trending topics. Specifically, we investigated pair-wise learning to rank models in order to measure a term's discriminative power in making a document rank higher in the returned document list. The discriminative power is combined with the term frequency which denotes the on-topic degree of a term to measure a term's representativeness against a trending topic. Representative terms and their query frequencies are applied to a state-of-the-art data mining model to enhance the effectiveness of trend surveillance. The experimental results based on trending topics of different domains show that our trend surveillance method performs well and the ranking information of search engines are helpful for trend surveillance. In light of this, the proposed method can provide effective support for government of cials and authorities in order to help them to respond to fast-changing events and topics, and to make appropriate decisions.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

A trending topic is a long-running event which is highly associated with people's life and activities, and has an index that depicts the topic's status (development). Because trending topics are usually associated with the concerns of individuals and authorities, trend surveillance systems that periodically predict the status of a trending topic are thus important for countries and organizations to help decision makers make appropriate decisions in response to fast-changing national and international situations. For instance, a health surveillance system that systematically collects health-related data from different areas of a country enables a government to monitor the health status of the public [1–4]. Disease outbreaks can be detected that help the government determine in a timely manner where, when, and how to allocate health resources in order to achieve the best epidemic control performance. Financial surveillance systems can assist organizations in understanding domestic and global financial trends which enable the establishment of appropriate business policies [5–8]. There is a great deal of evidence showing that trend surveillance is indispensable and that decision making processes can easily be misguided and problematic without such surveillance systems [9–12].

To construct a reliable surveillance system, representative indicators should be identified. Financial surveillance systems normally make use of business indices such as industrial production, stock price index, and manufacturing sales to measure the economic status of a country [7,13–15]; and health surveillance systems are always based on the infection number of a certain disease reported by medical institutions [16,17]. While the indicators are effective, in practice, their collection normally involves long data processes that delay the announcement of a trend's status [5–7]. The announced trend status thus lags, thereby possibly increasing the uncertainty of decision making. For instance, in the United States, officials generally take more than one month to compile economic indices, which seriously delay the announced economic status [6,7,18,19]. To remedy the problem, how to choose reliable and timely indicators is a practical and important research target.

Recently, due to the rapid development of the Internet, many studies (e.g., [1–5,20–22]) have utilized web search engines for trend surveillance. This is because when important events happen, people generally search the web first to acquire the desired information [18,22,23], which becomes user behavior that is logged on search engines (i.e., in the query logs), and which in turn corresponds well with the development of trending topics [18,20,21]. In this light, the query logs can be potentially used for efficient trend surveillance. In the past, query logs were the private asset of search engine companies and could not be accessed by the general public. However, they are now accessible for the retrieval of the latest search information through a number of online web services. For example, Google trends,<sup>1</sup> which was launched in 2006, provides information on how often a particular search term is queried relative to the total search volume in a particular time period across various regions of the world. Since the web service provides the up-to-date search behavior of users, it attracts many researchers to develop trend surveillance systems using search engine query logs. For instance, Eysenbac [1] observed a high correlation between the usage of epidemic-related terms queried on web search engines and the intensity of epidemics, and found that search engine query logs are effective healthcare surveillance indicators; Chen and Tsai [5] validated that the frequency count of business-related queries are highly correlated with the status of a business cycle, and leveraged query terms to develop a business cycle surveillance system; Li et al. [21] constructed an ontology framework to choose unemployment-related queries, and applied the queries to a support vector regression model to predict future unemployment rates. Basically, the success of the surveillance systems depends on the quality of the selected query terms: the surveillance systems cannot predict a trend status correctly if the query terms are off-topic. Some systems (e.g., [4, 21]) thus consult domain experts to compile query terms relevant to trending topics. However, the manual compilation takes time. While many systems (e.g., [2,3,5]) employ techniques of feature selection to identify query terms automatically, the feature selection techniques require a large document corpus. The query log of each term in the corpus needs to be downloaded and examined in order to acquire terms representative of trending topics; for this reason, the computational cost is high. Since the manual and automatic query term identifications are costly, the existing systems generally are specific to a single topic.

In this paper, we propose a novel trend surveillance system using the information of search engines. We develop an efficient feature selection method, called TF-LTR (Term Frequency-Learning to Rank), which is adaptable to different trending topics. Instead of preparing a large document corpus, the feature selection method requires a small document corpus composed of a few top-ranking documents returned by search engines; the method leverages the ranking order of the documents and the frequency of the terms in the documents to select representative query terms relevant to a trending topic. Techniques of pair-wise learning to rank are employed to measure a term's discriminative power in making a document that is ranked higher in the ranking list. The discriminative power is combined with the term frequency which denotes the on-topic degree of a term to measure a term's representativeness against the trending topic. Representative terms are selected as the indicators of the trending topic and their query frequencies are incorporated into a state-of-the-art data mining method to train a surveillance model which monitors the development of the trending topic. Evaluations based on trending topics of different domains demonstrate that our surveillance system is able to accurately predict the status of various trending topics, and the selected query terms and their query frequencies reveal interesting human behavior patterns for different trending topics. Our experiment results show that TF-LTR feature selection method is robust and it outperforms other popular feature selection methods. We also demonstrate that representative query terms can be extracted efficiently and effectively from a small corpus by making use the ranking order of documents.

The remainder of this paper is organized as follows. Section 2 provides a review of related works. In Section 3, we present the proposed surveillance system, and then in Section 4 we evaluate the system's performance. Section 5 summarizes our conclusions.

## 2. Literature review

We begin this section with a review of the trend surveillance systems using search engine information. We also review a number of popular feature selection methods because the core of the proposed framework is feature selection that selects representative query terms for trend surveillance. These methods will serve as the baselines for the performance evaluation.

## 2.1. Trend surveillance systems using search engine information

Search engine information has been widely adopted to supervise trend status in different domains. Regarding epidemic surveillance, Eysenbach [24] first examined search engine information to inspect the outbreak of epidemics. He observed that epidemic-related searches are generally consistent with the development of epidemics and he presumed that the search frequency of epidemic-related query terms would be an effective indicator of epidemic surveillance. He subsequently used the correlation between the epidemic-related searches on Google and the intensity of epidemics, and demonstrated that the epidemic-related searches can accurately predict the outbreak of epidemics. Ginsberg et al. [2] also utilized Google's search information for epidemic surveillance. The authors scanned the search database of Google to identify query terms that could model the Centers for Disease Control (CDC) influenza-like illness (ILI) visit percentage in the United States. Forty-five query terms out of 50 million candidate searches were selected as indicators to develop a linear regression model which periodically predicts the inflection number of influenza. Fang et al. [4] modeled epidemic surveillance as a data classification problem and compared the surveillance performance of difference machine learning models using query logs of search engines. The authors evaluated various generative and discriminative classification models, and validated that generative models, such as the Naive Bayes model, normally classify the status of dengue accurately.

In addition to epidemic surveillance, many studies also employ query logs to monitor economics-related statuses. For instance, Askitas and Zimmermann [25] utilized the search information of Google Insights to predict the unemployment rate in Germany. The authors manually selected four sets of search queries that were relevant to the topic of unemployment. Their query frequencies were then considered as time series data to construct an error correction model. The experiment results showed that their model could predict the German unemployment rate with a high degree of accuracy. Vosen and Schmidt [22] observed that people who search for consumer goods are likely to purchase the goods, and thereby utilized the query logs of search engines to predict American Consumption Confidence. Their prediction model achieved a significant improvement over the traditional models which are usually based on economic variables, such as the Consumer Confidence Index (CCI) and the Michigan Consumer Sentiment Index (MCSI). Choi and Varian [18] applied query logs to the prediction of retail sales, vehicle sales, real estate sales, and travel package sales. They demonstrated that the predictions based on query logs are more accurate than the predictions based on the methods without using query logs. Chen and Tsai [5] investigated the query frequency of search engines to survey the status of business cycles. Rather than consulting domain experts, the authors employed a correlation coefficient to automatically retrieve query terms whose query frequencies were highly correlated with the status of the business cycle. The selected query terms and the corresponding query frequencies were incorporated into a Naïve Bayes model to predict the status of the business cycle. Data discretization techniques have also been implemented to reduce the sparseness of query frequencies. Li et al. [21] developed an ontology-based web mining framework to predict the unemployment rate. The authors consulted domain experts to construct a labor economics ontology from which query terms regarding labor economics concepts were extracted by means of the feature selection techniques.

The extracted terms then were applied to a support vector regression model to enhance the accuracy of unemployment rate surveillance.

The above studies show the usefulness of query logs' in trend surveillance. Because the trend surveillance performance depends on the quality of the selected query terms, most studies either rely on domain experts to manually define a set of on-topic query terms or apply feature selection techniques to automatically extract representative query terms from a large document corpus. However, not only does it take time for domain experts to compile representative query terms, but the process of feature selection techniques that needs to examine each term in a large corpus leads to high computational costs. Since the manual and automatic query term identifications are both costly, the existing surveillance systems tend to be specific to a single topic, such as epidemics, business cycles, unemployment rates, or retail sales. In this paper, we propose an adaptive trend surveillance method. A simple feature selection method is developed to identify representative query terms in an efficient manner. A merit of our feature selection method is that we do not require a large document corpus. As a result, our trend surveillance system is adaptable to different domains and can be easily applied to various trending topics.

## 2.2. Feature selection

Feature selection is an important component of text mining and increases the performance of text mining by removing irrelevant text features (i.e., terms). Our research is closely related to feature selection because the proposed surveillance system examines the documents returned by search engines to identify representative query terms as surveillance indicators. Here, we review a number of important feature selection methods which will serve as the baseline in our performance evaluation.

Term frequency (TF) [26] assumes a term is important if it occurs frequently in a document corpus. It therefore counts the frequency of each term in the corpus as the term's weight and selects the top frequent terms to construct text mining models. However, many frequent terms such as stop words are too common to describe the theme of the corpus, this is why inverse document frequency (IDF) is generally incorporated with $\mathrm { T F }$ to reduce the weight of common terms. Term frequency-inverse document frequency (TF-IDF) [26] is calculated as the product $w _ { t , d } { = } t f _ { t , d } { \times } \log \left( N / d f _ { t } \right)$ where $w _ { t , d }$ denotes the TF-IDF weight of term t in document d; $t f _ { t , d }$ is the within-document term frequency (TF); log(N/df ) is the inverted document frequency (IDF) of t; N is the number of documents in the corpus; and df is the number documents where t appears. By synthetically combining the term frequency and the inverse document frequency, terms with a large TF-IDF score are chosen as representative features.

The Jaccard index (JI) [27] is the cardinality of the intersection divided by the cardinality of the union of two data sets and it is also a class metric for computing the similarity between text features. Given a pair of terms $t _ { i }$ and $t _ { j } ,$ the Jaccard index is calculated as $J ( t _ { i } , t _ { j } ) = \mid S _ { i } \cap S _ { j } \mid /$ | S ∪S | where S and $S _ { j }$ are the document sets in which t and t appear respectively in a document corpus. The higher the value o $\dot { \boldsymbol { \jmath } } ( t _ { i } , t _ { j } )$ , the greater the similarity is between t and $t _ { j \cdot }$ The terms in the document corpus then are ranked according to their Jaccard values against a topic, and the top-ranked terms are selected as representative term features.

Principal Components Analysis (PCA) [28] utilizes the variance along a dimension (feature) to reflect the dimension's representative power and reduces the dimensionality of data. In terms of text feature selection, let N represent the number of documents in a document corpus and let V be the number of unique terms (features). PCA first constructs a covariance matrix of size $V \times V .$ Then, the eigenvectors of the matrix are decomposed and ranked according to the corresponding eigenvalues. The leading eigenvectors are regarded as the principal components of the document corpus because they well characterize the variance of document features. To select representative features, the terms in the principal components are ranked according to their weights in the eigenvectors, with the top ranked terms being the selected features.

The Laplacian score [29] is a metric used to evaluate the importance of features. A merit of this metric is that it prefers features with not only a large variance but also a strong locality-preserving ability. Given a document corpus containing N documents (data) and V terms (features), the document set can be denoted by a matrix $\pmb { A } = [ \underline { { a } } _ { 1 } , \underline { { a } } _ { 2 } , . . . , \underline { { a } } _ { N } ]$ where $a _ { v n }$ denotes the frequency of the v-th term in the n-th document. In order to evaluate the Laplacian score of each feature, first, the nearest neighbor graph G with N document nodes is constructed. If nodes a

and a are connected, the weight between them is computed by $S _ { i j } =$ $e ^ { - { \frac { \| a _ { i } - a _ { j } \| } { t } } }$ where t is a tunable parameter; otherwise, $S _ { i j } = 0 .$ . Let $\underline { { f _ { \nu } } } = < a _ { \nu 1 } , a _ { \nu 2 } . . . . , a _ { \nu N } >$ consist of the frequencies of the v-th term in the N documents, and then the Laplacian score of the term is $L _ { v } =$ $\frac { \sum _ { i j } ( a _ { v i } - a _ { v j } ) ^ { 2 } S _ { i j } } { V a r ( f _ { v } ) }$ , where Var(f ) denotes the variance of the frequencies in $f _ { \nu } .$ The ascending order of $L _ { \nu }$ of all terms reflects the importance of terms insofar as terms with the minimal $L _ { \nu }$ will be selected as the representative features.

Pointwise mutual information and information retrieval (PMI-IR) [30] is a statistical method that measures the association between terms. Given a pair of terms, PMI-IR uses a search engine to count the number of documents in which the two terms co-occur. The number is then divided by the number of articles containing each of the terms to measure the dependency between the terms. A large PMI-IR score means that the two terms tend to occur simultaneously on the Internet. Thus, they are highly correlated with each other. To identify terms relevant to a topic in a document corpus, the PMI-IR scores each term in the corpus against the topic. Then, terms with a large PMI-IR score are selected to be the representative features.

## 3. Trend surveillance system

## 3.1. Problem definition

In this section, we introduce our trend surveillance system which periodically predicts the status of a trending topic. We utilize query logs of search engines to monitor a trending topic and develop the TF-LTR feature selection method which identifies a set of query terms T as the surveillance indicators. Subsequently, each query frequency of T was downloaded as the indicator value to build the trend surveillance model. Specifically, the proposed system treats trend surveillance as a regression problem which estimates the status of a trending topic as follows:

$$
\hat {a} _ {l} = \Gamma \left(\underline {{Q}} _ {l}\right),
$$

where â denotes the predicted status at time $l , \underline { { Q } } _ { \ l }$ is the query frequencies of the indicators up to time l, and Γ is a regression model that makes use of the query frequencies to measures the status $\hat { \boldsymbol { a } } _ { l }$

Fig. 1 shows the system structure which is composed of two key components feature selection and prediction model construction. In order to select trend surveillance indicators in an efficient manner, we developed the TF-LTR feature selection method which extracts representative query terms from a small document corpus. We first collect the top-ranking web documents regarding the trending topic from a search engine, and then TF-LTR examines the documents' ranking and the frequency of terms in the documents to identify query terms suitable for trend surveillance. Next, the idea of ensemble feature selection is adopted to select the representative query terms. In the process of constructing the prediction model, the query frequencies of the selected query terms are download as the indicator values and are represented as a high dimensional feature vector, i.e., $\underline { { \boldsymbol { Q } } } _ { \boldsymbol { l } }$ . The support vector regression (SVR), which is a state-of-the art regression algorithm, is applied to the feature vector to predict the status of the trending topic. We discuss the two components in the following sub-sections.

![](/api/attachments/YRRKEG6T/fulltext/images/54101fc9326d2c14fd1a88cfff859b7da35ee0bdb266796feeb7fc7464bc1a77.jpg)  
Fig. 1. The trend surveillance system.

## 3.2. Feature selection

## 3.2.1. Data processing

As mentioned above, our feature selection method examines a few top-ranking documents returned by a search engine so as to select representative query terms. Here, we explain how the documents are processed and why their ranking is useful to feature selection. The reason we investigate top documents and their ranking is that most contemporary search engines leverage users' feedback to adjust the ranking order of the returned documents [26,31]. In a sense, document ranking can be said to crowdsource public wisdom [31–34] insofar as it discloses the preference of the general public. Also, it has been not only asserted that the decisions of Internet users are significantly affected by the top documents returned by search engines [23,35,36], but also shown that people often pay attention to the top documents and ignore the rest (e.g., [37–39]). For instance, Dou et al. [23] employed psychology priming theories to validate that the ranking position of products presented by search engines can affect buyers' branding schema. In other words, the higher the rank of a product, the greater the degree of preference that buyers experienced regarding the product's branding. Such experiences further affect buyers' purchase decisions. Moreover, top ranking documents are readily available. Compared with the approach that consults domain experts to compile trend surveillance indicators (i.e., query terms), crowdsourcing is a much more inexpensive way to construct a surveillance system. Consequently, the surveillance system can easily adapt to different trending topics. Because the top documents of search engines are important and their ranking is meaningful, they are examined in this paper in order to identify query terms representative of a trending topic.

In order to identify the top-ranking documents regarding a trending topic, a topic term $q _ { t o p i c } ,$ which is highly associated with the trending topic, is manually defined. The selection of topic terms is crucial because it affects the quality of the retrieved topic documents and surveillance indicators. Here, we follow the topic-based query term principle [40] which recommends using the main concept to search for topic information. Taking the topic of the unemployment initial claims as an example, we consider unemployment as the main concept and use it as the topic term. We submit $q _ { t o p i c }$ to a search engine (e.g., Google), which will then return the top N documents $D = \{ d _ { 1 } , d _ { 2 } , . . . , d _ { N } \}$ } which are collected in order to explore query terms that are suitable for trend surveillance. After this, we tokenize the terms in the documents using the Illinois parser tool.<sup>2</sup> Because Internet users tend to submit nouns when performing web searches [5,41], we extract all unique nouns in $D ,$ which finally form a candidate query term set $V = \{ v _ { 1 } , v _ { 2 } , . . . , v _ { M } \}$ for feature selection.

## 3.2.2. TF-LTR

Our TF-LTR feature selection method extracts representative query terms from V by integrating the terms selected by term frequency and learning to rank techniques. In the field of text mining, term frequency is a common approach to measure the importance of a term in a document corpus. The approach assumes that terms frequently occurring in the document corpus should be important. For each document $d _ { n }$ in $D ,$ we first represent the document as a M-dimensional vector $\underline { { { X } } } _ { n } =$ $< x _ { n 1 } , x _ { n 2 } , . . . , x _ { n M } >$ where $x _ { n m }$ is the occurrence frequency of term $\nu _ { m }$ in document $d _ { n } .$ Then, we construct a term frequency vector $\underline { { { X } } } _ { D }$ by summing all document vectors, that is, $\begin{array} { r } { \underline { { X _ { D } } } = \sum _ { n = 1 } ^ { N } \underline { { X } } _ { r } } \end{array}$ where an elemen $x _ { D m }$ denotes ${ \nu _ { \mathrm { m } } } ^ { \prime } s$ term frequency in $D .$ The top z frequent terms in $X _ { D }$ are selected to construct the term set $S _ { T F }$

In addition to term frequency, our feature selection method also considers a term's discriminative power. In the information retrieval, a popular term weighting scheme called inversed document frequency (IDF) [26] was frequently used to enhance the discriminative power by reducing the weight of common terms. This scheme measures the discriminative power of a term by counting the number of documents in which the term appears, thereby indicating that the term has less indiscriminative power if it appears in many documents. However, according to our observation, common terms in the top few documents may also be important. For instance, the topic term unemployment is meaningful and always appears in the few top documents when we search for unemployment rates. Hence, IDF is not suitable to our feature selection process and it also ignores document ranking which has the potential for feature selection as we explained above. Hence, we employ techniques of learning to rank [42] to measure a term's discriminative power in terms of the document ranking in D. A term is supposed to have a high discriminative power if it is able to make a document rank higher [35]. Although learning to rank is an active machine learning subject that has been diversely applied in many research fields, such as text mining and recommendation systems [35,36,43], this study is, to the best of our knowledge, the first attempt to apply learning to rank to feature selection. In terms of feature selection, learning to rank learns a model that discriminates the ranking precedence of the documents in $D .$ By analyzing the learned ranking model, terms helpful to document ranking (i.e., with a high discriminative power) can be identified.

Here, we adopt the RankSVM model [35], a famous pairwise learning to rank algorithm, to learn the precedence of document pairs in $D .$ Specifically, RankSVM models learning to rank as a binary classification task and it denotes two precedence classes for a document pair d and $d _ { j }$ in $D _ { * }$ The precedence label $y _ { i j }$ is 1 if the ranking position of $d _ { i }$ is higher than that of $\cdot d _ { j } ,$ otherwise $y _ { i j } \mathrm { i } s - 1$ . Similar to the term frequency approach, each document $d _ { n }$ in $D$ is represented by the frequency vector $\underline { { { X } } } _ { n } ,$ and the RankSVM then identifies a hyperplane that accurately separates the two precedence classes in D under a high dimensional vector space as follows:

$$
\min _ {W} \frac {1}{2} \underline {{W}} ^ {T} \underline {{W}} + C \sum_ {p = 1} ^ {P} \xi_ {p}
$$

subject to the constraints:

$$
\underline {{W}} ^ {T} \left(\varnothing (X _ {i}) - \varnothing \left(\underline {{X}} _ {j}\right)\right) \geq 1 - \xi_ {p}, \xi_ {p} \geq 0, p = 1,..., P, \forall y _ {i j} = 1,
$$

where W is the normal vector (also called the weight vector) of the hyperplane, $\varnothing$ is a kernel function that map $\underline { { \boldsymbol X } }$ to a high dimensional vector space, C is a regularization term used to prevent W from overfitting, $\xi _ { p }$ is the slack variable associated with margin violation for precedence pair $( d _ { i } , d _ { j } )$ , and $\begin{array} { r } { P = ( \frac { N ( N - 1 ) } { 2 } ) } \end{array}$ is the number of document pairs in D. Many mathematical solutions have been proposed to solve the above constrained optimization problem. The weights in W indicate the influence of the terms in discriminating the two precedence classes. Hence, after W is obtained, we choose the top z weighted terms in W to compose the subset $S _ { L T R }$

Finally, to both consider the term importance and discriminative power, we combine $S _ { T F }$ and $S _ { L T R }$ by adopting the union strategy [44], that is, $T = \{ t _ { \mathrm { i } } | t _ { \mathrm { i } } \in S _ { T F } \cup S _ { L T R } \}$ and $\left| T \right| = K .$ . The term set T contains the selected surveillance indicators of the investigated trending topic.

## 3.3. Surveillance model construct

After the query term set T is obtained, the query frequencies of T are downloaded as the surveillance indicator values. We represent the query frequencies as a high-dimensional feature vector, and then use the support vector regression (SVR), a state-of-the-art regression algorithm to construct the trend surveillance model. SVR is an extension of SVM for general estimation and prediction problems, and it finds the best regression hyperplane with smallest prediction error to predict the trend status. Similar to SVM, the regression hyperplane is specified by an intercept term b and a normal vector $\underline { { W ^ { \prime } } }$ . To identify the regression hyperplane, we establish a set of training query frequencies. Let $R =$ $\{ ( \underline { { { Q } } } _ { 1 } , a _ { 1 } ) , ( \underline { { { Q } } } _ { 2 } , a _ { 2 } ) , \dots ( \underline { { { Q } } } _ { L } , a _ { L } ) \}$ be the set of training query frequencies, where $Q _ { l } { = } { < } q _ { 1 l } , q _ { 2 l } { , } { \ldots } { , } q _ { K l } { > }$ denotes the query frequency feature vector at time l and each element $q _ { k l }$ is term $t _ { k } " s$ query frequency downloaded from Google Trend,<sup>3</sup> and $a _ { l }$ is the status of the trending topic at time l.

Then, the hyperplane identification problem can be formulated as the following optimization problem:

$$
\min _ {W ^ {\prime}} \frac {1}{2} \underline {{W}} ^ {\prime T} \underline {{W}} ^ {\prime} + C ^ {\prime} \sum_ {l = 1} ^ {L} \left(\xi_ {l} ^ {+} + \xi_ {l} ^ {-}\right)
$$

subject to the constraints:

$$
\left\{ \begin{array}{l} a _ {l} - \left(\underline {{W}} ^ {\prime T} \underline {{Q}} _ {l} + b\right) \leq \varepsilon + \xi_ {l} ^ {-} \\ \left(\underline {{W}} ^ {\prime T} \underline {{Q}} _ {l} + b\right) - a _ {l} \leq \varepsilon + \xi_ {l} ^ {+}, \\ \xi_ {l} ^ {+}, \xi_ {l} ^ {-} \geq 0 \end{array} \right.
$$

where ε is the precision threshold, $C ^ { \prime }$ denotes the regularization parameter, and symbols $\xi ^ { + }$ and $\xi$ <sup>−</sup> represent the slack variables with nonnegative values to ensure feasible constraints. Again, the constrained optimization problem is solvable by many mathematical solutions. After all the parameters are obtained, the trend status $\hat { \boldsymbol a } _ { l }$ can be predicted by the SVR regression function as follows:

$$
\hat {a} _ {l} = \Gamma \left(\underline {{Q}} _ {l}\right) = \underline {{W}} ^ {\prime T} \underline {{Q}} _ {l} + b
$$

## 4. Performance evaluation

## 4.1. Data description and evaluation metrics

In order to show that the proposed surveillance system is adaptable to different domains, four trending topics covering the domains of economics, healthcare, financial markets, and consumer markets were selected for evaluation. These topics are the unemployment initial claims (UIC) released by the US Department of Labor,<sup>4</sup> the rate of influenza-like illness (ILI) released by the Centers for Disease and Prevention (CDC),<sup>5</sup> the weekly Nasdaq Composite Index (NPI) downloaded from Yahoo! Finance,<sup>6</sup> and the monthly sales of Xbox 360 (XBOX) downloaded from Gamer Investments.<sup>7</sup> The statuses of the first three trending topics are announced on a weekly basis. We collected their statuses that were announced between Jul. 2010 and Jun. 2014, for a total of 624 weekly (four years) statuses. Gamer Investment reports Xbox 360's sales on a monthly basis and the sales that were announced between Nov. 2005 and Apr. 2014, for a total of 102 monthly sales (8 years), were used for the performance evaluations.

As mentioned in Section 3, a topic term is required for a trending topic to collect its top-ranking documents. Here, the topic terms of the four above-mentioned evaluated trending topics are unemployment, flu, nasdaq, and xbox 360. We submitted each of them to Google to collect a small corpus for feature selection and the small corpus was composed of the top-ranking documents. Because the documents returned from search engines are sometimes too short to contain useful information, in this work we removed the returned documents which contained fewer than 500 words. The Illinois language parser was employed to tokenize and annotate the part-of-speech of the terms in the documents. Note that only nouns were used for evaluations and the nouns in the documents formed the candidate term set V. The proposed TF-LTR feature selection method then extracts the most representative terms from V. Next, the query frequencies of the selected terms during the evaluation period were downloaded from Google Trend on a weekly basis for surveillance model construction. In the following sections, we first discuss the influence of system parameters N and z, which respectively determine the size of the document corpus and the number of the selected query terms on system performance. Then, we compare the proposed TF-LTR method with a number of popular feature selection methods. Table 1 details the statistics of the evaluated trending topics.

Table 1  
Statistics of the evaluation dataset.

<table><tr><td>Trending topic</td><td>UIC</td></tr><tr><td>Topic term</td><td>unemployment</td></tr><tr><td>Date</td><td>Jul. 2010-Jun. 2014</td></tr><tr><td># of announced statuses</td><td>208</td></tr><tr><td># of document size/# of candidate terms</td><td>3/1098</td></tr><tr><td></td><td>5/1156</td></tr><tr><td></td><td>10/1247</td></tr><tr><td>Trending topic</td><td>ILI</td></tr><tr><td>Topic term</td><td>flu</td></tr><tr><td>Date</td><td>Jul. 2010-Jun. 2014</td></tr><tr><td># of announced statuses</td><td>208</td></tr><tr><td># of document size/# of candidate terms</td><td>3/1036</td></tr><tr><td></td><td>5/1089</td></tr><tr><td></td><td>10/1170</td></tr><tr><td>Trending topic</td><td>NCI</td></tr><tr><td>Topic term</td><td>nasdaq</td></tr><tr><td>Date</td><td>Jul. 2010-Jun. 2014</td></tr><tr><td># of announced statuses</td><td>208</td></tr><tr><td># of document size/# of candidate terms</td><td>3/349</td></tr><tr><td></td><td>5/471</td></tr><tr><td></td><td>10/981</td></tr><tr><td>Trending topic</td><td>XBOX</td></tr><tr><td>Topic term</td><td>xbox 360</td></tr><tr><td>Date</td><td>Nov. 2005-Apr. 2014</td></tr><tr><td># of announced statuses</td><td>102</td></tr><tr><td># of document size/# of candidate terms</td><td>3/975</td></tr><tr><td></td><td>5/1038</td></tr><tr><td></td><td>10/1399</td></tr></table>

To derive reliable evaluation results, we employed the leave-oneout cross validation method which has been shown to provide an unbiased estimate of the true generalization ability [45]. Specifically, for each trending topic, we evaluated its surveillance performance over multiple runs. Each run selected an announced status as the testing data, and the remaining statuses and the corresponding query frequencies formed the training set for surveillance model construction. For instance, the collected UIC dataset had 208 announced statuses, which resulted in 208 cross validation runs under the trending topic. The prediction results of all the 208 evaluation runs are then aggregated to obtain the global performance comparison. Here, we consider three evaluation metrics, which are mean absolute percentage error (MAPE), mean absolute error (MAE), and root mean square error (RMSE), to measure the performance of the proposed surveillance system [21,46]. These metrics are defined as follows:

$$
\mathrm{MAPE} = \sum_ {l = 1} ^ {L} \frac {| a _ {l} - \hat {a} _ {l} |}{a _ {l}} / L
$$

$$
\mathrm{MAE} = \sum_ {l = 1} ^ {L} | a _ {l} - \hat {a} _ {l} | / L
$$

$$
\mathrm{RMSE} = \sqrt {\sum_ {l = 1} ^ {L} \left(a _ {l} - \hat {a} _ {l}\right) ^ {2} / L},
$$

where L is the number of cross validation runs, and $a _ { l }$ and $\hat { \boldsymbol a } _ { l }$ respectively denote the true status and the predicted status. Since the metrics are based on the difference between the true status and the predicted status, a surveillance system is superior if its MAPE, MAE, and RMSE are low.

## 4.2. Parameter setting

The proposed TF-LTR feature selection method has the two system parameters of z and N, which respectively determine the number of the query terms for trend surveillance and the size of the document corpus. In [21], the authors suggested setting z at 15, but in addition to this setting, we further examined the effect of z at 5 and 10. Parameter N was set between 3 and 10, and was increased in increments of 1. The reason that we restricted N to be within 10 is that search engines (e.g., Google) normally return 10 documents on the first page, and people tend to pay attention to the first page only [23]. Furthermore, having a large N means the preparation of a large document corpus D and a huge candidate query term set V that will increase the cost of the feature selection.

As shown in Tables 2 to 13, setting z at 15 generally produces superior surveillance performance. The results under $z = 5 ,$ , in contrast, are inferior because the selected query terms are too few to comprehend the users' search intention regarding a trending topic. We also noticed that the performance under z = 10 and $z = 1 5$ are close, and they both produce good surveillance performance, thus making these two settings appropriate for surveillance model construction. However, because z = 15 yields the better performance, we used this setting for the performance comparisons. While the best N varies from topic to topic, the performance results under different settings of N are very close, as shown in Fig. 2. It is worth noting that even a small N (e.g., N = 3 for the topic UIC) can produce good surveillance performance. These results suggest that the proposed TF-LTR is not subject to a small N (e.g., N = 3–10) and is capable of constructing accurate surveillance systems for various topics using a small document corpus. In other words, surveillance systems based on TF-LTR can be built efficiently and effectively. In Section 4.3, in order to test the robustness of the compared feature selection methods, we set N at 3, 5, and 10, which respectively stand for N′s minimum, median and maximum.

The TF-LTR MAPE performance of UIC under different settings.

<table><tr><td>MAPE</td><td>N=3</td><td>N=4</td><td>N=5</td><td>N=6</td><td>N=7</td><td>N=8</td><td>N=9</td><td>N=10</td><td>Average</td></tr><tr><td>z=5</td><td>10.82</td><td>9.69</td><td>8.76</td><td>8.47</td><td>9.34</td><td>9.57</td><td>8.47</td><td>8.7</td><td>9.23</td></tr><tr><td>z=10</td><td>8.04</td><td>7.7</td><td>8.73</td><td>8.08</td><td>9.44</td><td>8.34</td><td>8.97</td><td>8.42</td><td>8.47</td></tr><tr><td>z=15</td><td>7.97</td><td>7.98</td><td>8.43</td><td>8.17</td><td>8.05</td><td>8.9</td><td>8.53</td><td>8.18</td><td>8.28</td></tr><tr><td>Average</td><td>8.94</td><td>8.46</td><td>8.64</td><td>8.24</td><td>8.94</td><td>8.94</td><td>8.66</td><td>8.43</td><td></td></tr></table>

The TF-LTR MAE performance of UIC under different settings.

<table><tr><td>MAE</td><td>N=3</td><td>N=4</td><td>N=5</td><td>N=6</td><td>N=7</td><td>N=8</td><td>N=9</td><td>N=10</td><td>Average</td></tr><tr><td>z=5</td><td>41.55</td><td>37.98</td><td>34.41</td><td>33.37</td><td>35.99</td><td>37.21</td><td>33.49</td><td>34.34</td><td>36.04</td></tr><tr><td>z=10</td><td>31.38</td><td>29.98</td><td>34.14</td><td>31.76</td><td>36.67</td><td>33</td><td>35.36</td><td>33.03</td><td>33.17</td></tr><tr><td>z=15</td><td>30.97</td><td>31.46</td><td>32.99</td><td>32.1</td><td>31.52</td><td>34.48</td><td>33.12</td><td>32.43</td><td>32.38</td></tr><tr><td>Average</td><td>34.63</td><td>33.14</td><td>33.85</td><td>32.41</td><td>34.73</td><td>34.90</td><td>33.99</td><td>33.27</td><td></td></tr></table>

Table 4  
The TF-LTR RMSE performance of UIC under different settings.

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>56.94</td><td>55.3</td><td>50.28</td><td>48.8</td><td>51.62</td><td>53.65</td><td>50.27</td><td>53.22</td><td>52.51</td></tr><tr><td>z = 10</td><td>44.93</td><td>44.79</td><td>49.26</td><td>48.04</td><td>52.6</td><td>51.08</td><td>52.37</td><td>48.28</td><td>48.92</td></tr><tr><td>z = 15</td><td>44.45</td><td>46.54</td><td>47.16</td><td>46.84</td><td>45.99</td><td>49.87</td><td>48.65</td><td>49.44</td><td>47.37</td></tr><tr><td>Average</td><td>48.77</td><td>48.88</td><td>48.90</td><td>47.89</td><td>50.07</td><td>51.53</td><td>50.43</td><td>50.31</td><td></td></tr></table>

Table 5  
The TF-LTR MAPE performance of ILI under different settings.

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>18.1</td><td>14.02</td><td>20.23</td><td>16.86</td><td>16.21</td><td>19.89</td><td>17.95</td><td>16.49</td><td>17.47</td></tr><tr><td>z = 10</td><td>14.81</td><td>15.24</td><td>16.05</td><td>15.85</td><td>15.48</td><td>16.64</td><td>16.66</td><td>15.2</td><td>15.74</td></tr><tr><td>z = 15</td><td>14.1</td><td>15.2</td><td>16.77</td><td>15.42</td><td>15.77</td><td>16.91</td><td>16.04</td><td>15.29</td><td>15.69</td></tr><tr><td>Average</td><td>15.67</td><td>14.82</td><td>17.68</td><td>16.04</td><td>15.82</td><td>17.81</td><td>16.88</td><td>15.66</td><td></td></tr></table>

Table 6  
The TF-LTR MAE performance of ILI under different settings.

<table><tr><td>MAE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>0.307</td><td>0.251</td><td>0.329</td><td>0.286</td><td>0.265</td><td>0.312</td><td>0.296</td><td>0.27</td><td>0.29</td></tr><tr><td>z = 10</td><td>0.251</td><td>0.255</td><td>0.267</td><td>0.262</td><td>0.252</td><td>0.272</td><td>0.273</td><td>0.25</td><td>0.26</td></tr><tr><td>z = 15</td><td>0.239</td><td>0.238</td><td>0.269</td><td>0.245</td><td>0.247</td><td>0.268</td><td>0.257</td><td>0.24</td><td>0.25</td></tr><tr><td>Average</td><td>0.27</td><td>0.25</td><td>0.29</td><td>0.26</td><td>0.25</td><td>0.28</td><td>0.28</td><td>0.25</td><td></td></tr></table>

The TF-LTR RMSE performance of ILI under different settings.

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>0.47</td><td>0.41</td><td>0.53</td><td>0.45</td><td>0.39</td><td>0.48</td><td>0.46</td><td>0.42</td><td>0.45</td></tr><tr><td>z = 10</td><td>0.41</td><td>0.42</td><td>0.42</td><td>0.4</td><td>0.37</td><td>0.42</td><td>0.42</td><td>0.37</td><td>0.40</td></tr><tr><td>z = 15</td><td>0.39</td><td>0.35</td><td>0.41</td><td>0.36</td><td>0.36</td><td>0.4</td><td>0.39</td><td>0.38</td><td>0.38</td></tr><tr><td>Average</td><td>0.42</td><td>0.39</td><td>0.45</td><td>0.40</td><td>0.37</td><td>0.43</td><td>0.42</td><td>0.39</td><td></td></tr></table>

The TF-LTR MAPE performance of NAS under different settings.

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>7.34</td><td>7.36</td><td>7.36</td><td>7.87</td><td>7.87</td><td>7.43</td><td>7.87</td><td>7.38</td><td>7.56</td></tr><tr><td>z = 10</td><td>7.61</td><td>7.3</td><td>7.58</td><td>7.35</td><td>6.44</td><td>5.34</td><td>5.56</td><td>7.15</td><td>6.79</td></tr><tr><td>z = 15</td><td>5.1</td><td>5.06</td><td>5.07</td><td>5.77</td><td>4.67</td><td>4.96</td><td>4.9</td><td>5.04</td><td>5.07</td></tr><tr><td>Average</td><td>6.68</td><td>6.57</td><td>6.67</td><td>7.00</td><td>6.33</td><td>5.91</td><td>6.11</td><td>6.52</td><td></td></tr></table>

Table 9  
The TF-LTR MAE performance of NAS under different settings.

<table><tr><td>MAE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>233.94</td><td>223.34</td><td>223.34</td><td>235.95</td><td>235.95</td><td>224.93</td><td>235.95</td><td>224.21</td><td>229.70</td></tr><tr><td>z = 10</td><td>229.42</td><td>219.91</td><td>228.82</td><td>222.06</td><td>190.29</td><td>155.76</td><td>160.48</td><td>211.56</td><td>202.29</td></tr><tr><td>z = 15</td><td>156.97</td><td>155.87</td><td>154.82</td><td>175.32</td><td>138.43</td><td>143.93</td><td>144.85</td><td>147.23</td><td>152.18</td></tr><tr><td>Average</td><td>206.78</td><td>199.71</td><td>202.33</td><td>211.11</td><td>188.22</td><td>174.87</td><td>180.43</td><td>194.33</td><td></td></tr></table>

The TF-LTR RMSE performance of NAS under different settings.

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>338.49</td><td>346.25</td><td>346.25</td><td>353.48</td><td>353.48</td><td>347.16</td><td>353.48</td><td>346.78</td><td>348.17</td></tr><tr><td>z = 10</td><td>351.93</td><td>338.37</td><td>333.96</td><td>336.51</td><td>298.83</td><td>245.07</td><td>264.05</td><td>309.75</td><td>309.81</td></tr><tr><td>z = 15</td><td>208.37</td><td>215.25</td><td>217.12</td><td>245.67</td><td>206.54</td><td>235.55</td><td>219</td><td>219.32</td><td>220.85</td></tr><tr><td>Average</td><td>299.60</td><td>299.96</td><td>299.11</td><td>311.89</td><td>286.28</td><td>275.93</td><td>278.84</td><td>291.95</td><td></td></tr></table>

Table 13  
Table 11  
The TF-LTR MAPE performance of XBOX under different settings

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>43.88</td><td>44.46</td><td>44.83</td><td>36.91</td><td>39.33</td><td>39.33</td><td>39.33</td><td>39.47</td><td>40.94</td></tr><tr><td>z = 10</td><td>35.77</td><td>42.2</td><td>40.12</td><td>34.39</td><td>39.55</td><td>41.03</td><td>40.66</td><td>38.1</td><td>38.98</td></tr><tr><td>z = 15</td><td>37.1</td><td>40.16</td><td>34.69</td><td>34.66</td><td>35.27</td><td>35.95</td><td>36.45</td><td>36.21</td><td>36.31</td></tr><tr><td>Average</td><td>38.92</td><td>42.27</td><td>39.88</td><td>35.32</td><td>38.05</td><td>38.77</td><td>38.81</td><td>37.93</td><td></td></tr></table>

Table 12  
The TF-LTR MAE performance of XBOX under different settings.

<table><tr><td>MAE</td><td>N=3</td><td>N=4</td><td>N=5</td><td>N=6</td><td>N=7</td><td>N=8</td><td>N=9</td><td>N=10</td><td>Average</td></tr><tr><td>z=5</td><td>210,625.55</td><td>212,467.62</td><td>210,623.59</td><td>194,701.69</td><td>195,392.58</td><td>195,392.58</td><td>195,392.58</td><td>195,856.6</td><td>201,306.60</td></tr><tr><td>z=10</td><td>188,386.43</td><td>194,931.22</td><td>192,584.63</td><td>169,108.73</td><td>173,407.5</td><td>179,480.22</td><td>179,445.49</td><td>187,782.18</td><td>183,140.80</td></tr><tr><td>z=15</td><td>167,046.03</td><td>193,205.88</td><td>177,910.78</td><td>160,701.35</td><td>159,112.48</td><td>162,435.94</td><td>165,087.19</td><td>162,810.79</td><td>168,538.81</td></tr><tr><td>Average</td><td>188,686.00</td><td>200,201.57</td><td>193,706.33</td><td>174,837.26</td><td>175,970.85</td><td>179,102.91</td><td>179,975.09</td><td>182,149.86</td><td></td></tr></table>

The TF-LTR RMSE performance of XBOX under different settings.

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 4</td><td>N = 5</td><td>N = 6</td><td>N = 7</td><td>N = 8</td><td>N = 9</td><td>N = 10</td><td>Average</td></tr><tr><td>z = 5</td><td>385,040.82</td><td>384,575.98</td><td>381,918.19</td><td>364,719.6</td><td>362,910.75</td><td>362,910.75</td><td>362,910.75</td><td>363,303.97</td><td>371,036.35</td></tr><tr><td>z = 10</td><td>353,333.87</td><td>349,099.43</td><td>356,287.33</td><td>310,937.81</td><td>309,829.02</td><td>318,062.2</td><td>315,141.02</td><td>343,010.71</td><td>331,962.67</td></tr><tr><td>z = 15</td><td>305,334.74</td><td>348,259.98</td><td>330,824.35</td><td>290,092.91</td><td>288,785.89</td><td>292,660.7</td><td>296,257.96</td><td>287,948.98</td><td>305,020.69</td></tr><tr><td>Average</td><td>347,903.14</td><td>360,645.13</td><td>356,343.29</td><td>321,916.77</td><td>320,508.55</td><td>324,544.55</td><td>324,769.91</td><td>331,421.22</td><td></td></tr></table>

## 4.3. Experiment result

In Sections 4.3.1 to 4.3.4, we compare the proposed TF-LTR method with a number of popular feature selection methods under the four

![](/api/attachments/YRRKEG6T/fulltext/images/fd874fed43dbf2144896914a10378bfa8b68ba6803302326dba66cda441b7c00.jpg)

![](/api/attachments/YRRKEG6T/fulltext/images/30b0d54f04b415c7412e7ff289f73725abab8f26e0ed93aa9aa4a8a486cbb50d.jpg)

![](/api/attachments/YRRKEG6T/fulltext/images/e079dce8721d1ffa47439e980d4ab7c404886aa69a5a2ab5f713bdaaa2ba9d6a.jpg)

![](/api/attachments/YRRKEG6T/fulltext/images/e2cb7992a37b323367d73db1c3f78cfb2a55ccaf8fbf042a3b225492266ac7e8.jpg)  
Fig. 2. The average prediction performance of the TF-LTR method under different N settings.

Table 14  
The MAPE performance of UIC.

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>8.82</td><td>8.92</td><td>9.03</td><td>8.92</td></tr><tr><td>TF</td><td>9.15</td><td>9.59</td><td>9.59</td><td>9.44</td></tr><tr><td>TF-IDF</td><td>10.08</td><td>11.59</td><td>12.01</td><td>11.23</td></tr><tr><td>PMI-IR</td><td>9.79</td><td>9.33</td><td>10.16</td><td>9.76</td></tr><tr><td>Jaccard</td><td>10.23</td><td>10.48</td><td>10.69</td><td>10.47</td></tr><tr><td>Laplacian</td><td>10.03</td><td>10.06</td><td>10.98</td><td>10.36</td></tr><tr><td>PCA</td><td>8.22</td><td>8.22</td><td>8.22</td><td>8.22</td></tr><tr><td>TF-LTR</td><td>7.97</td><td>8.43</td><td>8.18</td><td>8.19</td></tr></table>

Table 15  
The MAE performance of UIC.

<table><tr><td>MAE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>34.18</td><td>33.94</td><td>36.04</td><td>34.72</td></tr><tr><td>TF</td><td>35.66</td><td>37.33</td><td>37.33</td><td>36.77</td></tr><tr><td>TF-IDF</td><td>40.18</td><td>46.31</td><td>46.76</td><td>44.42</td></tr><tr><td>PMI-IR</td><td>39.53</td><td>36.94</td><td>40.10</td><td>38.86</td></tr><tr><td>Jaccard</td><td>40.24</td><td>40.87</td><td>41.59</td><td>40.90</td></tr><tr><td>Laplacian</td><td>40.21</td><td>39.24</td><td>43.46</td><td>40.97</td></tr><tr><td>PCA</td><td>32.68</td><td>32.68</td><td>32.68</td><td>32.68</td></tr><tr><td>TF-LTR</td><td>30.97</td><td>32.99</td><td>32.43</td><td>32.13</td></tr></table>

Table 16  
The RMSE performance of UIC.

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>49.47</td><td>49.04</td><td>56.90</td><td>51.80</td></tr><tr><td>TF</td><td>51.23</td><td>53.41</td><td>53.41</td><td>52.68</td></tr><tr><td>TF-IDF</td><td>56.19</td><td>65.22</td><td>64.64</td><td>62.02</td></tr><tr><td>PMI-IR</td><td>59.44</td><td>55.15</td><td>57.05</td><td>57.22</td></tr><tr><td>Jaccard</td><td>57.42</td><td>57.44</td><td>57.95</td><td>57.60</td></tr><tr><td>Laplacian</td><td>61.99</td><td>55.18</td><td>63.40</td><td>60.19</td></tr><tr><td>PCA</td><td>48.61</td><td>48.61</td><td>48.61</td><td>48.61</td></tr><tr><td>TF-LTR</td><td>44.45</td><td>47.16</td><td>49.44</td><td>47.02</td></tr></table>

evaluated trending topics. In Section 4.3.5, we discuss the experiment results.

## 4.3.1. Surveillance performance on UIC

Tables 14–16 respectively show the MAPE, MAE, and RMSE of the compared methods under different corpus size settings. As shown in the tables, TF-LTR achieved a superior surveillance performance and it generally outperformed the compared methods, excluding some results adopting PCA under N = 5. Among all the experiment results, TF-LTR achieves the best MAPE, MAE and RMSE performance and it also leads to the lowest average MAPE, MAE, and RMSE. Accordingly, TF-LTR is better able to extract representative terms (indicators) for UIC surveillance compared with other feature selection methods.

According to the experiment results, TF-LTR under N = 3 achieves the best prediction performance. Fig. 3 presents the predicted results and the announced unemployment initial claims (number in thousands). As shown in the figure, the predicted results highly correspond with the announced statuses (the Pearson correlation coefficient is 0.82). For instance, there are increments of UIC values between Sep. 2010–Jan. 2011, Sep. 2011–Jan. 2012, Sep. 2012–Jan. 2013, and Sep. 2013–Jan. 2014. The values predicted by the proposed model also capture the inclines and are close to the actual values. In addition, there are sharp decrements in Jan. 2011, Jan. 2012, Jan. 2013, and Jan. 2014. Such rapid changes of UIC were accurately identified by the proposed model as well.

## 4.3.2. Surveillance performance on ILI

Tables 17–19 respectively show the MAPE, MAE, and RMSE performance of the compared methods under the trending topic ILI. In this topic, TF-LTR achieves the best average MAE and RMSE, but TF has a better MAPE performance. Upon closer inspection, TF-LTR produces the best MAPE (14.1) and MAE (0.239) under N = 3, but TF only achieves the best RMSE (0.37) under N = 10. While the performances of TF were comparable to those of TF-LTR, the differences were not significant. The comparisons demonstrate the superiority of TF-LTR for supervising the trend of ILI.

Fig. 4 shows the ILIs predicted by TF-LTR under N = 3, which achieves the best prediction performance. Again, the predicted results highly correspond with the announced ILIs (the Pearson correlation coefficient is 0.92). In other words, our method correctly predicted the ILI trend.

## 4.3.3. Surveillance performance on NC

As shown in Tables 20–22, TF-LTR outperforms all the other feature selection methods. We also plotted the prediction results of the TF-LTR with N = 10, which achieves the best prediction performance. As shown in Fig. 5, our surveillance system was able to accurately model the NCI trend (the Pearson correlation coefficient is 0.93).

## 4.3.4. Surveillance performance on XBOX

Tables 23–25 respectively show the MAPE, MAE, and RMSE of the compared methods on the topic XBOX. Once more, TF-LTR outperforms all the compared feature selection methods, indicating that the terms

![](/api/attachments/YRRKEG6T/fulltext/images/141bd3ddb0a5c2fa43f68bf84222b187257fd53f1f1bca6d54cf7b94a4a3f61e.jpg)  
Fig. 3. The prediction performance of the TF-LTR method under N = 3.

Table 17  
The MAPE performance of ILI.

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>16.26</td><td>16.16</td><td>15.38</td><td>15.93</td></tr><tr><td>TF</td><td>15.28</td><td>15.27</td><td>15.17</td><td>15.24</td></tr><tr><td>TF-IDF</td><td>24.93</td><td>24.99</td><td>20.26</td><td>23.39</td></tr><tr><td>PMI-IR</td><td>21.49</td><td>21.49</td><td>21.20</td><td>21.39</td></tr><tr><td>Jaccard</td><td>18.50</td><td>19.26</td><td>18.40</td><td>18.72</td></tr><tr><td>Laplacian</td><td>28.36</td><td>19.35</td><td>26.90</td><td>24.87</td></tr><tr><td>PCA</td><td>15.89</td><td>15.89</td><td>15.89</td><td>15.89</td></tr><tr><td>TF-LTR</td><td>14.10</td><td>16.77</td><td>15.29</td><td>15.39</td></tr></table>

Table 18  
The MAE performance of ILI.

<table><tr><td>MAE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>0.263</td><td>0.262</td><td>0.249</td><td>0.258</td></tr><tr><td>TF</td><td>0.264</td><td>0.250</td><td>0.242</td><td>0.252</td></tr><tr><td>TF-IDF</td><td>0.472</td><td>0.467</td><td>0.299</td><td>0.413</td></tr><tr><td>PMI-IR</td><td>0.405</td><td>0.405</td><td>0.398</td><td>0.402</td></tr><tr><td>Jaccard</td><td>0.297</td><td>0.310</td><td>0.301</td><td>0.303</td></tr><tr><td>Laplacian</td><td>0.518</td><td>0.401</td><td>0.494</td><td>0.471</td></tr><tr><td>PCA</td><td>0.274</td><td>0.274</td><td>0.274</td><td>0.274</td></tr><tr><td>TF-LTR</td><td>0.239</td><td>0.269</td><td>0.240</td><td>0.249</td></tr></table>

The RMSE performance of ILI.  
Table 19

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>0.40</td><td>0.43</td><td>0.41</td><td>0.412</td></tr><tr><td>TF</td><td>0.43</td><td>0.38</td><td>0.37</td><td>0.392</td></tr><tr><td>TF-IDF</td><td>0.79</td><td>0.78</td><td>0.53</td><td>0.701</td></tr><tr><td>PMI-IR</td><td>0.67</td><td>0.67</td><td>0.67</td><td>0.672</td></tr><tr><td>Jaccard</td><td>0.52</td><td>0.54</td><td>0.52</td><td>0.528</td></tr><tr><td>Laplacian</td><td>0.82</td><td>0.69</td><td>0.76</td><td>0.756</td></tr><tr><td>PCA</td><td>0.43</td><td>0.43</td><td>0.43</td><td>0.432</td></tr><tr><td>TF-LTR</td><td>0.39</td><td>0.41</td><td>0.38</td><td>0.391</td></tr></table>

Table 20

selected by our method are suitable for consumer market surveillance. Fig. 6 shows the predictions made by TF-LTF under N = 10 which produces the best prediction results. It is interesting to note that the sales in each December are significantly higher than the sales predicted by our method. This is because many people make it a rule to buy Christmas presents, hence the actual sales values are significantly higher than the predicted values. Nevertheless, the trend of the Xbox 360 sales can be well-predicted by the proposed model (the Pearson correlation coefficient is 0.82).

The MAPE performance of NCI.

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>5.72</td><td>7.53</td><td>6.04</td><td>6.43</td></tr><tr><td>TF</td><td>6.40</td><td>6.19</td><td>6.00</td><td>6.20</td></tr><tr><td>TF-IDF</td><td>6.24</td><td>7.29</td><td>7.08</td><td>6.87</td></tr><tr><td>PMI-IR</td><td>6.14</td><td>5.29</td><td>6.08</td><td>5.84</td></tr><tr><td>Jaccard</td><td>8.60</td><td>8.49</td><td>8.34</td><td>8.48</td></tr><tr><td>Laplacian</td><td>6.65</td><td>5.81</td><td>7.00</td><td>6.49</td></tr><tr><td>PCA</td><td>5.78</td><td>5.78</td><td>6.58</td><td>6.05</td></tr><tr><td>TF-LTR</td><td>5.10</td><td>5.07</td><td>5.04</td><td>5.07</td></tr></table>

Table 21  
The MAE performance of NCI.

<table><tr><td>MAE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>172.33</td><td>237.83</td><td>183.19</td><td>197.78</td></tr><tr><td>TF</td><td>201.18</td><td>193.02</td><td>176.59</td><td>190.26</td></tr><tr><td>TF-IDF</td><td>189.93</td><td>218.97</td><td>217.41</td><td>208.77</td></tr><tr><td>PMI-IR</td><td>185.51</td><td>164.00</td><td>184.69</td><td>178.07</td></tr><tr><td>Jaccard</td><td>255.59</td><td>261.34</td><td>263.05</td><td>259.99</td></tr><tr><td>Laplacian</td><td>201.01</td><td>176.90</td><td>214.01</td><td>197.31</td></tr><tr><td>PCA</td><td>175.48</td><td>175.48</td><td>198.57</td><td>183.18</td></tr><tr><td>TF-LTR</td><td>156.97</td><td>154.82</td><td>147.23</td><td>153.00</td></tr></table>

Table 22  
The RMSE performance of NCI

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>238.82</td><td>343.85</td><td>244.56</td><td>275.75</td></tr><tr><td>TF</td><td>275.14</td><td>257.61</td><td>273.61</td><td>268.79</td></tr><tr><td>TF-IDF</td><td>235.92</td><td>276.89</td><td>303.86</td><td>272.22</td></tr><tr><td>PMI-IR</td><td>270.09</td><td>212.53</td><td>241.37</td><td>241.33</td></tr><tr><td>Jaccard</td><td>317.66</td><td>328.12</td><td>350.10</td><td>331.96</td></tr><tr><td>Laplacian</td><td>285.95</td><td>221.04</td><td>268.68</td><td>258.56</td></tr><tr><td>PCA</td><td>246.73</td><td>246.73</td><td>311.22</td><td>268.23</td></tr><tr><td>TF-LTR</td><td>208.37</td><td>217.12</td><td>219.32</td><td>214.94</td></tr></table>

## 4.3.5. Experiment discussion

In this subsection, we summarize the experiment results. First, we discuss the effectiveness of using the small corpus. As shown in

![](/api/attachments/YRRKEG6T/fulltext/images/9260eb0683d72535e9e2767536da281f570fcc777d800099ae646c215e539d40.jpg)  
Fig. 4. The prediction performance of ILI method under N = 3

![](/api/attachments/YRRKEG6T/fulltext/images/e073fd2ed5a7bb7de9f501a979c1d57396bb483000e79739924ea1910728802f.jpg)  
Fig. 5. The prediction performance of the TF-LTR method under N = 10.

Section 2, most previous works on trend surveillance select representative query terms by consulting domain experts or by preparing a large text corpus for feature selection. For instance, to supervise UIC, Li et al. [21] consulted economists and experienced practitioners to construct a labor economics ontology and a set of query terms regarding labor economics concepts, which were extracted by several feature selection techniques. Compared with their experiment in which the best derived MAPE was 7.92, ours was 7.97 for terms we automatically extracted from the small corpus, which is on a par with those manually elaborated by experts. To supervise ILI, Ginsberg et al. [2] scanned 50 million candidate terms in the Google database, and based on the selected terms, the Pearson correlation coefficient they derived between the actual ILI values and their predicted values was 0.97. In contrast, the number of candidate terms we examined in the ILI corpus was about 1000, and without a huge computation effort, the correlation coef cient we derived was 0.92. Even though the two methods are able to correctly predict the ILI values, the process of Ginsberg et al.'s approach is clearly too costly to make the trend surveillance method adaptable to different topics. Our experiment results, on the other hand, demonstrate that representative query terms (indicators) can be extracted efficiently and effectively from a small corpus by making use the ranking information of documents. In addition, the top-ranking documents are easily accessible and require less computation, so our method can be easily adapted to different domains.

Table 23  
The MAPE performance of XBOX.

<table><tr><td>MAPE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>40.95</td><td>40.43</td><td>40.59</td><td>40.66</td></tr><tr><td>TF</td><td>38.33</td><td>37.13</td><td>40.34</td><td>38.60</td></tr><tr><td>TF-IDF</td><td>42.08</td><td>44.16</td><td>43.92</td><td>43.39</td></tr><tr><td>PMI-IR</td><td>48.51</td><td>48.51</td><td>46.83</td><td>47.95</td></tr><tr><td>Jaccard</td><td>42.07</td><td>44.58</td><td>47.03</td><td>44.56</td></tr><tr><td>Laplacian</td><td>42.61</td><td>41.67</td><td>42.48</td><td>42.25</td></tr><tr><td>PCA</td><td>38.62</td><td>38.62</td><td>36.94</td><td>38.06</td></tr><tr><td>TF-LTR</td><td>37.10</td><td>34.69</td><td>36.21</td><td>36.00</td></tr></table>

Table 24  
The MAE performance of XBOX.

<table><tr><td>MAE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>181,574.05</td><td>193,495.05</td><td>195,096.42</td><td>190,055.17</td></tr><tr><td>TF</td><td>191,792.76</td><td>189,516.18</td><td>180,805.53</td><td>187,371.49</td></tr><tr><td>TF-IDF</td><td>198,701.95</td><td>205,669.94</td><td>189,847.89</td><td>198,073.26</td></tr><tr><td>PMI-IR</td><td>214,824.33</td><td>214,824.33</td><td>210,554.85</td><td>213,401.17</td></tr><tr><td>Jaccard</td><td>201,760.06</td><td>199,147.93</td><td>204,653.59</td><td>201,853.86</td></tr><tr><td>Laplacian</td><td>213,324.97</td><td>214,099.91</td><td>213,193.98</td><td>213,539.62</td></tr><tr><td>PCA</td><td>192,513.85</td><td>192,513.85</td><td>170,650.17</td><td>185,225.96</td></tr><tr><td>TF-LTR</td><td>167,046.03</td><td>177,910.78</td><td>162,810.79</td><td>169,255.87</td></tr></table>

The experiment results show that TF-LTR achieves superior and robust predictive performance compared with other feature selection methods. Here, we report the statistical significance of the improvement over the compared methods in terms of a one-tailed paired t-test [47]. In general, the improvements of TF-LTR over the compared methods are statistically significant, as shown in the Tables 26–28. However, in some cases (e.g., PCA on the topics UIC and ILI), the improvement was not significant; this is because the terms extracted by the compared methods great overlap with those of our method, which leads to a similar performance. In spite of this, the proposed TF-LTR is robust and provides correct predictions for all the evaluated trending topics. The reason that TF-LTR outperforms the compared feature selection methods is that TF-LTR considers the ranking order of documents, which reflects what people are most concerned about when learning about a trending topic. As TF-LTR considers a user's search intention, it is able to select representative terms as surveillance indicators, thus outperforming the compared methods. For example, we observed that documents containing the terms insurance and benefit in the UIC corpus were generally more highly ranked. This ranking implies that people are

Table 25  
The RMSE performance of XBOX

<table><tr><td>RMSE</td><td>N = 3</td><td>N = 5</td><td>N = 10</td><td>Average</td></tr><tr><td>LTR</td><td>323,289.41</td><td>352,641.72</td><td>367,175.08</td><td>347,702.07</td></tr><tr><td>TF</td><td>365,035.49</td><td>353,165.13</td><td>319,998.90</td><td>346,066.51</td></tr><tr><td>TF-IDF</td><td>375,952.66</td><td>387,180.93</td><td>355,008.60</td><td>372,714.06</td></tr><tr><td>PMI-IR</td><td>393,099.62</td><td>393,099.62</td><td>390,588.06</td><td>392,262.43</td></tr><tr><td>Jaccard</td><td>387,669.47</td><td>370,963.08</td><td>368,977.71</td><td>375,870.09</td></tr><tr><td>Laplacian</td><td>409,994.67</td><td>408,352.39</td><td>402,389.07</td><td>406,912.04</td></tr><tr><td>PCA</td><td>366,886.10</td><td>366,886.10</td><td>312,713.60</td><td>348,828.60</td></tr><tr><td>TF-LTR</td><td>305,334.74</td><td>330,824.35</td><td>287,948.98</td><td>308,036.03</td></tr></table>

![](/api/attachments/YRRKEG6T/fulltext/images/89542cc6e51d4f852a9518debef2a55bea742e419eee05793f9f0a2786c08f45.jpg)  
Fig. 6. The prediction performance of the TF-LTR method under N = 10.

The MAPE one-tailed paired t-test analysis of TF-LTR over competition methods.

<table><tr><td>MAPE</td><td>UIC</td><td>ILI</td><td>NCI</td><td>XBOX</td></tr><tr><td>LTR</td><td>0.01299**</td><td>0.2892</td><td>0.06808*</td><td>0.007149***</td></tr><tr><td>TF</td><td>0.002046***</td><td>0.5664</td><td>0.003756***</td><td>0.04531**</td></tr><tr><td>TF-IDF</td><td>0.01308**</td><td>0.02101**</td><td>0.01638**</td><td>0.01494**</td></tr><tr><td>PMI-IR</td><td>0.02159**</td><td>0.008066***</td><td>0.05354*</td><td>0.003212***</td></tr><tr><td>Jaccard</td><td>0.001702***</td><td>0.01366**</td><td>0.0001455***</td><td>0.02107**</td></tr><tr><td>Laplacian</td><td>0.01202**</td><td>0.05771*</td><td>0.02923**</td><td>0.002288***</td></tr><tr><td>PCA</td><td>0.447</td><td>0.2907</td><td>0.03706**</td><td>0.08283*</td></tr></table>

\*, \*\*, \*\*\* represent one-tail paired t-tests with α = 0.1, 0.05, and 0.01 respectively.

The MAE one-tailed paired t-test analysis of TF-LTR over competition methods.

<table><tr><td>MAE</td><td>UIC</td><td>ILI</td><td>NCI</td><td>XBOX</td></tr><tr><td>LTR</td><td>0.5619</td><td>0.9645</td><td>0.0774*</td><td>0.03434**</td></tr><tr><td>TF</td><td>0.3207</td><td>0.9621</td><td>0.006568***</td><td>0.02059**</td></tr><tr><td>TF-IDF</td><td>0.02961**</td><td>0.06745*</td><td>0.02011**</td><td>0.001234***</td></tr><tr><td>PMI-IR</td><td>0.1667</td><td>0.0001644***</td><td>0.04767**</td><td>0.003321***</td></tr><tr><td>Jaccard</td><td>0.05395*</td><td>0.008756***</td><td>0.001076***</td><td>0.01634**</td></tr><tr><td>Laplacian</td><td>0.01199**</td><td>0.01564**</td><td>0.06426*</td><td>0.004474***</td></tr><tr><td>PCA</td><td>0.2287</td><td>0.9333</td><td>0.05225*</td><td>0.04484**</td></tr></table>

\*, \*\*, \*\*\* represent one-tail paired t-tests with α = 0.1, 0.05, and 0.01 respectively.

The RMSE one-tailed paired t-test analysis of TF-LTR over competition methods

<table><tr><td>RMSE</td><td>UIC</td><td>ILI</td><td>NCI</td><td>XBOX</td></tr><tr><td>LTR</td><td>0.37</td><td>0.03709**</td><td>0.1033</td><td>0.0916*</td></tr><tr><td>TF</td><td>0.01118**</td><td>0.5</td><td>0.009645***</td><td>0.03838**</td></tr><tr><td>TF-IDF</td><td>0.007258***</td><td>0.03007**</td><td>0.03693**</td><td>0.002181***</td></tr><tr><td>PMI-IR</td><td>0.02558**</td><td>0.0005073***</td><td>0.1521</td><td>0.009511***</td></tr><tr><td>Jaccard</td><td>0.01143**</td><td>0.0003122***</td><td>0.001727***</td><td>0.01963**</td></tr><tr><td>Laplacian</td><td>0.02083**</td><td>0.007206***</td><td>0.08955*</td><td>0.00612***</td></tr><tr><td>PCA</td><td>0.1922</td><td>0.02664**</td><td>0.05579</td><td>0.03217**</td></tr></table>

\*, \*\*, \*\*\* represent one-tail paired t-tests with α = 0.1, 0.05, and 0.01 respectively.

normally concerned about unemployment insurance and the corresponding social benefits when they are about to be unemployed, or believe this to be so. These terms are therefore effective surveillance indicators of UIC insofar as by adopting learning to rank, TF-LTR selects such terms as indicators. TF-LTR also measures term frequency in order to avoid selecting off-topic terms. As TF-LTR considers both the importance and discriminative power of a term, it achieves a better prediction performance even in different domain topics. In contrast, the compared feature selection methods (e.g., TF) tend to select common terms such as labor and job; and because the use of only common terms cannot discriminate the intention of users, their surveillance performance is inferior. Also, the comparison results reveal that TF-LTR is adaptable to different domains, but the compared methods are not. For instance, PCA is only good at surveying the topic UIC and TF is only effective for the topic ILI. In sum, the proposed TF-LTR is helpful for decision makers to construct effective and robust trend surveillance systems.

## 5. Conclusion

Supervising the status of trending topics is important to decision makers. In this paper, we have proposed an effective framework for predicting the status of trending topics. We defined status prediction as a regression problem, and proposed a novel feature selection method called TF-LTR for selecting representative query terms. Experiments based on four real world datasets demonstrate that the proposed framework can provide correct predictions and can be easily applied to various trending topics. In light of this, the proposed method can provide effective support for government officials and authorities in order to help them respond to fast-changing events and topics, and make appropriate decisions.

In our future work, we first plan to investigate more information sources (e.g., news posting, internet forum) to enhance the proposed feature selection method. Second, we will examine the effect on the time lag of query frequencies. Finally, we will also investigate using more state-of-the-art data mining models to compute the probability of a trend status, which can be integrated with recommendation systems in order to suggest accurate status that is relevant to the trending topic.

## Acknowledgements

This research was supported in part by MOST 103-2221-E-002- 106-MY2 from the Ministry of Science and Technology, Republic of China.

## References

[1] G. Eysenbach, Infodemiology: tracking flu-related searches on the web for syndromic surveillance, AMIA Annual Symposium Proceedings, American Medical Informatics Association 2006, p. 244.

[2] J. Ginsberg, M.H. Mohebbi, R.S. Patel, L. Brammer, M.S. Smolinski, L. Brilliant, Detecting influenza epidemics using search engine query data, Nature 457 (2009) 1012–1014.

[3] P.M. Polgreen, Y. Chen, D.M. Pennock, F.D. Nelson, R.A. Weinstein, Using internet searches for influenza surveillance, Clinical Infectious Diseases 47 (2008) 1443–1448.

[4] Z.-H. Fang, J.-S. Tzeng, C.C. Chen, T.-C. Chou, A study of machine learning models in epidemic surveillance: using the query logs of search engines, PACIS 2010, p. 137.

[5] C.C. Chen, Y.-T. Tsai, A novel business cycle surveillance system using the query logs of search engines, Knowledge-Based Systems 30 (2012) 104–114.

[6] M. Chauvet, J. Piger, A comparison of the real-time performance of business cycle dating methods, Journal of Business & Economic Statistics 26 (2008) 42–49.

[7] D.B. Jun, Y.J. Joo, Predicting turning points in business cycles by detection of slope changes in the leading composite index, Journal of Forecasting 12 (1993) 197–213.

[8] A.P. Layton, Dating and predicting phase changes in the US business cycle, International Journal of Forecasting 12 (1996) 417–428.

[9] A. Bansal, R.J. Kauffman, R.M. Mark, E. Peters, Financial risk and financial risk management technology (RMT): issues and advances, Information & Management 24 (1993) 267–281.

[10] C.-J. Lu, T.-S. Lee, C.-C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2009) 115–125.

[11] M. Lam, Neural network techniques for financial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (2004) 567-581.

[12] W. Ketter, J. Collins, M. Gini, A. Gupta, P. Schrater, Detecting and forecasting economic regimes in multi-agent automated exchanges, Decision Support Systems 47 (2009) 307-318

[13] J.D. Hamilton, G. Perez-Quiros, What do the leading indicators lead? Journal of Business (1996) 27–49.

[14] H. James, A new approach to the economic analysis of nonstationary time series and the business cycle, Econometrica (1989).

[15] C.R. Birchenhall, H. Jessen, D.R. Osborn, P. Simpson, Predicting US business-cycle regimes, Journal of Business & Economic Statistics 17 (1999) 313–323.

[16] T.M. Rath, M. Carreras, P. Sebastiani, Automated detection of influenza epidemics with hidden Markov models, Advances in Intelligent Data Analysis V, Springer 2003, pp. 521–532.

[17] R.E. Serfling, Methods for current statistical analysis of excess pneumonia-influenza deaths, Public Health Reports 78 (1963) 494.

[18] H. Choi, H. Varian, Predicting the present with Google trends, Economic Record 88 (2012) 2–9.

[19] D.R. Osborn, M. Sensier, The prediction of business cycle phases: financial variable and international linkages, National Institute Economic Review 182 (2002) 96–105

[20] R. Baeza-Yates, A. Tiberi, Extracting Semantic Relations from Query Logs, Google Pat ents, 2011.

[21] Z. Li, W. Xu, L. Zhang, R.Y. Lau, An ontology-based web mining method for unemployment rate prediction, Decision Support Systems 66 (2014) 114–122.

[22] S. Vosen, T. Schmidt, Forecasting private consumption: survey-based indicators vs. Google trends, Journal of Forecasting 30 (2011) 565–578.

[23] W. Dou, K.H. Lim, C. Su, N. Zhou, N. Cui, Brand positioning strategy using search engine marketing, MIS Quarterly 34 (2010) 261–279.

[24] G. Eysenbach, Infodemiology: the epidemiology of (mis) information, The American Journal of Medicine 113 (2002) 763–765.

[25] N. Askitas, K.F. Zimmermann, Google econometrics and unemployment forecasting, German Council for Social and Economic Data (RatSWD) Research Notes, 2009.

[26] C.D. Manning, P. Raghavan, H. Schütze, Introduction to Information Retrieval, Cambridge University Press, Cambridge, 2008.

[27] P. Jaccard, Etude Comparative de la Distribution Florale Dans Une Portion Des Alpes et Du Jura, Impr. Corbaz, 1901.

[28] K. Pearson, LIII. On Lines and Planes of Closest Fit to Systems of Points in Space, The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, Vol.21901.559-572

[29] X. He, D. Cai, P. Niyogi, Laplacian score for feature selection, Advances in Neural Information Processing Systems 2005, pp. 507–514.

[30] P. Turney, Mining the Web for Synonyms: PMI-IR Versus LSA on TOEFL, 2001.

[31] A. Doan, R. Ramakrishnan, A.Y. Halevy, Crowdsourcing systems on the world-wide web Communications of the ACM 54 (2011) 86–96

[32] J. Surowiecki, The Wisdom of Crowds, Anchor, 2005.

[33] J. Surowiecki, M.P. Silverman, The wisdom of crowds, American Journal of Physics 75 (2007) 190–192

[34] A. Halavais, Search Engine Society, John Wiley & Sons, 2013.

[35] T. Joachims, Optimizing search engines using clickthrough data, Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2002, pp. 133–142.

[36] E.F. Can, W.B. Croft, R. Manmatha, Incorporating query-specific feedback into learning-to-rank models, Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, ACM 2014, pp. 1035–1038.

[37] T. Joachims, L. Granka, B. Pan, H. Hembrooke, G. Gay, Accurately interpreting clickthrough data as implicit feedback, Proceedings of the 28th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM 2005, pp. 154–161.

[38] T. Joachims, L. Granka, B. Pan, H. Hembrooke, F. Radlinski, G. Gay, Evaluating the accuracy of implicit feedback from clicks and query reformulations in web search, ACM Transactions on Information Systems (TOIS) 25 (2007) 7.

[39] F. Radlinski, T. Joachims, Query chains: learning to rank from implicit feedback, Proceedings of the Eleventh ACM SIGKDD International Conference on Knowledge Discovery in Data Mining, ACM 2005, pp. 239–248.

[40] J. Fan, H. Wu, G. Li, L. Zhou, Suggesting topic-based query terms as you type, web conference (APWEB), 2010, 12th International Asia-Pacific, IEEE 2010, pp. 61–67.

[41] C. Barr, R. Jones, M. Regelson, The linguistic structure of English web-search queries, Proceedings of the Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics 2008, pp. 1021–1030.

[42] T.-Y. Liu, Learning to rank for information retrieval, Foundations and Trends in Information Retrieval, 3 (2009) 225–331

[43] S.-Y. Shih, M. Lee, C.C. Chen, An Effective Friend Recommendation Method Using Learning to Rank and Social Influence, 2015.

[44] C.-F. Tsai, Y.-C. Hsiao, Combining multiple feature selection methods for stock prediction: union, intersection, and multi-intersection approaches, Decision Support Systems 50 (2010) 258–269.

[45] G.C. Cawley, N.L. Talbot, Fast exact leave-one-out cross-validation of sparse leastsquares support vector machines, Neural Networks 17 (2004) 1467–1475.

[46] Z. Guo, W.K. Wong, M. Li, A multivariate intelligent decision-making model for retail sales forecasting, Decision Support Systems 55 (2013) 247–255.

[47] M. Berenson, D. Levine, K.A. Szabat, T.C. Krehbiel, Basic Business Statistics: Concepts and Applications, Pearson Higher Education AU, 2012

Ze-Han Fang received his M.S. degree in Information Management from National Taiwan University, Taiwan, in 2010 and he pursued his Ph.D. in Information Management at National Taiwan University, in 2014. His current research interests include data mining learning to rank, and business intelligence

Chien Chin Chen received his B.S. and M.S. degrees in Computer Science and Information Engineering from National Central University. Taiwan, in 1997 and 1999, respectively. Then he joined the Institute of Information Science at Academia Sinica. Taiwan, as a research assistant and participated several research projects in the area of text mining. In August 2003, he began his Ph.D. program and received his Ph.D. degree in Electrical Engineering from National Taiwan University, Taiwan, in 2007. He is currently an associate professor of the department of Information Management at National Taiwan University. His papers have appeared in Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, ACM Transactions on Information Systems (TOIS), Information Sciences, Knowledge-based Systems, ACM SIGIR, ACM SIGKDD, ECIR, AIRS, PACIS, etc. His current research interests include text mining, business intelligence, data mining, and recommendation systems.
