---
otero_id: 13284
otero_key: "K224ZTYX"
title: "Finding competitive keywords from query logs to enhance search engine advertising"
authors: "Dandan Qiao; Jin Zhang; Qiang Wei; Guoqing Chen"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.11.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Finding competitive keywords from query logs to enhance search engine advertising

Dandan Qiao<sup>a</sup>, Jin Zhang<sup>b,</sup>\*, Qiang Wei<sup>a</sup>, Guoqing Chen<sup>a</sup>

<sup>a</sup> School of Economics and Management, Tsinghua University, Beijing, 100084, China <sup>b</sup> School of Business, Renmin University of China, Beijing, 100872, China

## A R T I C L E I N F O

Article history: Received 30 April 2015 Received in revised form 21 September 2016 Accepted 21 November 2016 Available online xxx

Keywords: Competitive advertising Keywords suggestion Topic modeling Factor graph model Search engine advertising Query log

## A B S T R A C T

This study has proposed a topic based competitive keywords suggestion method called TCK to enhance search engine advertising. On the basis of query logs, the method explores the indirect associations between keywords and extracts the hidden topic information to identify competitive keywords. It can help advertisers not only broaden the choices of keywords but also carry out a competitive strategy for search engine advertising. Extensive experiments have been conducted to demonstrate the effectiveness of the proposed method. Results prove that the proposed method performs better than existing keyword suggestion methods, contributing greatly to the keyword suggestion advertising market.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Search engine advertising (SEA), which is a primary marketing channel in online advertising nowadays [1–4], has been one of the main venues to compete for customers, due to its high targeting, relatively low cost, high <sup>fl</sup>exibility and high variability [5]. Generally, advertisers bid on speci<sup>fi</sup>c keywords related to their business, and then corresponding advertisements are displayed alongside the search results when users query those bidden keywords [6]. For example, a Nestle milk dealer in Shanghai (i.e., an advertiser) would like to bid on the keyword “Nestle Shanghai”, and post the corresponding ad alongside the search results returned by querying with the keyword, since the search engine users querying “Nestle Shanghai” would be possibly interested in the ad and click it. To a great extent, SEA can help business merchants effectively target potential consumers. The advantages of SEA prompt the emergence of keyword suggestion methods to help achieve the business goal.

Generally, a typical keyword suggestion method is to generate a set of keywords that relate to the seed keywords prede<sup>fi</sup>ned by advertisers. The generated keywords can be considered as an expanded description of the business. Taking the Nestle milk dealer as an example, relevant keywords like “Nestle milk price”, “Nestle milk quality” and “Nestle milk formulation” may reasonably be suggested/recommended for advertising. In recent years, numerous research efforts have been devoted to the problem of keyword suggestion. A common technique is to conduct cooccurrence analysis based on query logs [1,7,8,9–12]. Keywords frequently co-occurring with the seed keyword in query logs are selected to conduct search engine advertising. As query logs can timely re<sup>fl</sup>ect users’ intentions [4,13], this category of methods have been adopted as the mainstream technique in search engine advertising marketplace, e.g., Google AdWords<sup>1</sup>, Baidu Tuiguang<sup>2</sup>, etc. In most cases, however, the keywords suggested by the cooccurrence based methods are quite popular and expensive to bid on. They limit advertisers to only a handful of keywords though the total number of query keywords is estimated to exceed a billion [14]. Actually a long tail of other candidate keywords, which is also relevant and occupies a large fraction of the total traf<sup>fi</sup>c [15], is ignored in the existing methods. Moreover, this kind of cooccurrence based methods cannot suggest keywords from the competitive perspective, which is rather signi<sup>fi</sup>cant in today's <sup>fi</sup>erce competition environment [16–19]. Currently, the competitive keyword advertising is emerging as a new type of advertising which attracts more and more attention from advertisers. This strategy is meant to display ads alongside the search results of competitors. Fig. 1 shows a typical example in Bing advertising marketplace. As a tablet provider, Google has bidden on a competitive keyword “kindle <sup>fi</sup>re”, thus prompting a “Nexus” ad to the users querying “kindle <sup>fi</sup>re”. This strategy of advertising is effective and valuable on two folds. First, it can help advertisers <sup>fi</sup>nd and attract more potential consumers to watch their ads, which is the nature of search engine advertising. A user who queries certain products is very likely to be interested in products with similar features/functions provided by competitors. Therefore, as shown in Fig. 1, it increases the possibility for consumers, who want to buy a tablet, to switch from Kindle Fire to Nexus after scanning the ads. Second, the competitive advertising strategy can help advertisers seize potential market shares from competitors. This is critical and important for advertisers to sustain a competitive advantage in the market [19,20]. An advertiser hence may be induced to directly advertise on the competitor’s keywords [17] as shown in Fig. 1. This competitive advertising strategy helps Nexus obtain more by free riding on the market created by Kindle Fire. Therefore, leveraging competitive keywords to achieve the strategy of competitive advertising on search engines is very promising and important for advertisers.

To effectively achieve the goal of competitive advertising on search engines, a large number of competitive keywords should be provided to advertisers. However, advertisers can normally perceive a very small fraction of competitive keywords in their minds due to bounded cognitions. In addition, the existing cooccurrence based methods can hardly accomplish the task since competitive keywords rarely co-occur with the seed keywords in users’ queries. To address the problem, this study proposes a novel method called TCK to automatically suggest keywords for competitive advertising. The proposed method captures the underlying topics hidden in query logs to recommend competitive keywords. Firstly, given a seed keyword, the method TCK could mine a broad enough set of candidate competitive keywords based on their indirect connections with the seed keyword. Secondly, each candidate is mapped into a topic structure extracted from the query logs. The mined topic structure is further combined into a factor graph model to <sup>fi</sup>nally extract a set of effective competitive keywords. Data experiments were conducted across various business domains to demonstrate the effectiveness of TCK.

The remainder of this paper is organized as follows. First, stateof-the-art of keywords suggestion methods is reviewed. Then the problem de<sup>fi</sup>nition is presented. Following this, a novel method of competitive keywords suggestion, namely TCK, is proposed. Then experimental results are shown to reveal the outperformance of the proposed method. In the <sup>fi</sup>nal section, discussions and limitations are concluded.

## 2. Literature review

To effectively help advertisers expose ads to potential consumers who are more dependent on search engines to assist purchase decisions [21,22], a plethora of research efforts have been devoted to the problem of keywords suggestion. According to various types of data source, the methods for keywords suggestion can be categorized into three streams, i.e., query log based, proximity based and meta-tag crawlers based methods [8].

## 2.1. Query log based keywords suggestion

In the branch of query log based methods, keywords are mainly suggested by conducting association/co-occurrence analysis in search engine query logs [3,11]. For instance, “iPad” is found to usually occur jointly with the keyword “Apple” in query logs. So the keyword “iPad” is considered to be highly relevant to the keyword “Apple” and therefore can be suggested to advertisers. The technique of co-occurring analysis has been widely used in many commercial keywords suggestion tools like Google AdWords<sup>1</sup> and Baidu Tuiguang.<sup>2</sup> Query logs from mainstream search engines can timely capture users’ search intentions [21], which are valuable for commercial advertising and query log based keywords suggestion methods. Leveraging query logs, Zhang et al. proposed a bidding mechanism to recommend a group of relevant yet less hot keywords [12]. Chuklin et al. employed all the query phrases that contain the seed keyword to conduct query expansions [23]. In the context-based framework of query auto-completion, Jiang et al. extracted those queries matching the leading characters from query logs to generate query candidates [24]. Ranked by the conditional probabilities, Massoudi et al. selected the terms cooccurring with the original query in posts to augment queries [25]. Fuxman et al. considered the strong associations existing between

![](/api/attachments/K224ZTYX/fulltext/images/42a643559c93dd690a52f770ee7880c7221688bc7207dbce9bdd5d8009293cf9.jpg)  
Fig. 1. An example of competitive search advertising and the translation.

Please cite this article in press as: D. Qiao, et al., Finding competitive keywords from query logs to enhance search engine advertising, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.11.003

queries and clicked URLs. They exploited such reinforcing relationships to mine queries that were related to the interests of the advertiser. Sarmento et al. proposed a keyword suggestion method by mining the logs of previous submitted ads to infer similarity relations among the associated keywords [26]. To some extent, the existing query log based methods can recommend effective keywords to advertisers. However, it’s probable that only a limited number of hot keywords are suggested to many different advertisers [15]. Therefore, the bidding prices of these keywords are driven up, leading to a high advertising cost for advertisers [14]. More importantly, a mass of keywords in the long tail may be ignored despite their high conversional value to advertisers [12].

## 2.2. Proximity based keywords suggestion

Proximity based keyword generation methods query search engines for the seed keyword and recommend keywords from the query results possessing high proximity with the seed keyword. Liu et al. (2011) proposed to generate candidate keywords based on corresponding clustering results in solving query expansion problem. Bendersky et al. presented a framework of query formulation which combined the proximity-matching search results with other external sources. By conducting similarity analysis between the seed keyword and keywords in advertisers websites, Abhishek and Hosanagar proposed a method to recommend keywords with high relevance. Wu et al. employed the search results of the seed keyword to generate a large set of candidate terms and further <sup>fi</sup>lter out the irrelevant ones by leveraging the information of user relevance feedback. To better understand the keyword meaning of the queries and boost the search engine ads, Border et al. proposed a classi<sup>fi</sup>cation method of rare queries using the web search results to determine the topic of the given queries [27]. In addition, some researches focused on calculating the proximity based on vocabulary dictionaries/corpus pre-constructed by domain experts [6,28], e.g., thesaurus dictionary, Wikipedia, etc. The quality of the proximity based methods varies across the source of web pages or corpus. Besides, considering the quantity of the information on each webpage, it would take great computational efforts to conduct the proximity based methods. Furthermore, in many cases, due to the source quality (web pages, texts, dictionaries), the suggested keywords cannot re<sup>fl</sup>ect search engine users’ real intentions, which are the primary concern of advertisers.

## 2.3. Meta-tag crawlers based keywords suggestion

The meta-tag crawlers based methods focus on <sup>fi</sup>nding relevant keywords from meta-tags. They send the seed keyword to the search engine and extract meta-tag keywords from the top ranked web pages. Some popular online tools like WordStream<sup>3</sup> and Wordtracker<sup>4</sup> use meta-tag crawlers to search meta-tag keywords and make suggestion of relevant keywords for advertisers. Though these techniques can suggest keywords from the meta-tag data of web pages, they have two limitations [29]. On one hand, the number of relevant keywords generated by this kind of methods is still limited and cannot provide suf<sup>fi</sup>cient choices for advertisers. On the other hand, there is no guarantee to <sup>fi</sup>nd good and relevant keywords, since the meta-tag keywords of web pages are sometimes too diverse to keep the focal meaning.

From the above discussions, it could be found that, since data from web pages or meta-tags are not issued by search engine users and couldn’t re<sup>fl</sup>ect their direct intentions, the keywords suggested by the proximity based or meta-tag crawlers based methods are then not signi<sup>fi</sup>cantly valued by advertisers who may question about users’ interests in these keywords. As for query log based methods, they only extract keywords explicitly co-occurring with the seed keyword, leading to a narrow choice set for advertisers. More importantly, they can’t suggest competitive keywords which rarely co-occur with the seed keywords in queries. Therefore, in this paper, a novel method is proposed to suggest competitive keywords based on users’ query topics hidden in query logs.

## 3. Methodological framework

This section introduces the framework of TCK, a topic based competitive keyword suggestion method. Two steps are included in the framework of TCK as shown in Fig. 2. The <sup>fi</sup>rst step is to generate candidate keywords through indirect associative analysis. The second step is to suggest competitive keywords with topic based factor graph modeling.

## 3.1. Candidate keywords generation

Supposing Q is a set of queries recording n query log data from a search engine within a period of time. Each query q in Q consists of two elements, the query keywords q.kw and the corresponding number of search volume q.vol. Table 1 shows an example of the query logs about the keyword “Pantene” (a well-known brand of hair care product) within a day from Baidu.<sup>2</sup>

De<sup>fi</sup>nition 1. (Volume of a keyword)Given a query log dataset Q within a certain period, for a keyword k, its search volume, denoted as k.vol, can be calculated as the aggregated volume of the queries that contain k, as shown in (1).

$$
k. v o l = \sum_ {q \in Q, k \in q. k w} q. v o l
$$

1

De<sup>fi</sup>nition 2. (Associative keyword)Given a query log dataset Q within a certain period and a keyword k, for a keyword a, it can be de<sup>fi</sup>ned as an associative keyword of k, if there exists at least one piece of query q in Q satisfying k q.kw and a q.kw simultaneously.

Generally, in the query log dataset Q, there is more than one keyword associated with k. It can thus educe an associative keyword set, denoted by k.AK, which contains all the keywords associated with k, as shown in (2). Besides, it can be found that the keyword k is also an associative keyword of a, indicating the symmetry of the associative relationship.

$$
k. A K = \{a | \exists q \in Q, k \in q. k w \land a \in q. k w \}\tag{2}
$$

![](/api/attachments/K224ZTYX/fulltext/images/00ebf69f8d28bd9d9d94c73eab62d076ddf2ab5db29c3d846b983b85a00b760c.jpg)  
Fig. 2. TCK: Topic based competitive keywords suggestion.

D. Qiao et al. / Information & Management xxx (2016) xxx–xxx

Example of query logs for “Pantene” from Baidu.

<table><tr><td>q.kw</td><td>q.vol</td></tr><tr><td>Pantene</td><td>560</td></tr><tr><td>Pantene liquid shampoo</td><td>150</td></tr><tr><td>Pantene Conditioner</td><td>40</td></tr><tr><td>Pantene emulsion repair shampoo</td><td>20</td></tr><tr><td>Pantene alopecia</td><td>5</td></tr><tr><td>Pantene hair mask</td><td>20</td></tr><tr><td>Official site of Pantene</td><td>30</td></tr><tr><td>...</td><td>...</td></tr></table>

Given a seed keyword s, an associative keyword set, denoted by s.AK, can be extracted from the query dataset Q according to Definition 2. These associative keywords, which co-occur with s, actually serve as a representation of the seed keyword, e.g., {liquid shampoo, conditioner, emulsion repair shampoo, alopecia, hair mask, . . . } with respect to a seed “Pantene”. According to the existing co-occurrence based methods, these keywords would be suggested to advertisers. However, they are hardly competitive keywords. Furthermore, it is worth noticing that the keywords in s. AK may be associated with many alternative keywords in addition to s, e.g., {liquid shampoo, conditioner, emulsion repair shampoo, alopecia, hair mask, . . . } can be frequently observed to co-occur with “Unilever” as an alternative to “Pantene”. The alternative keywords can be roughly regarded as the seed keyword’s competitors. The associative keywords in s.AK to a large extent re<sup>fl</sup>ect common topics perceived by search users on both the competitors and the seed keyword. Therefore, the indirect associations through the associative keywords hidden in the query data could be further investigated to mine competitive keywords for a seed keyword.

Formally, given a query log dataset Q and the set of all keywords in Q, i.e. K, for a given seed keyword s, the associative keywords denoted by s.AK can be obtained by traversing in Q. Further, for each keyword a in s.AK, a set of associative keywords denoted by a. AK can also be derived from Q. As discussed above, the keywords in a.AK can be considered as candidate competitive keywords for the seed keyword s. After aggregating a.AK for all a $\in s . A K ,$ a candidate <sup>2</sup>set of competitive keywords, denoted as s.Cand, could be obtained. The whole process of candidate keywords generation could be modeled as follows,

$$
\begin{array}{l l} \text {Find} & s. C a n d = \{c _ {1}, c _ {2}, \ldots , c _ {n} \} \\ s. t. & s. C a n d \subseteq K \\ & \forall c _ {x} \in s. C a n d, \exists a \in s. A K \cap c _ {x}. A K \end{array}\tag{3}
$$

## 3.2. Topic based competitive keywords suggestion

Given a seed keyword s, the <sup>fi</sup>rst step of TCK discovers a broad set of candidate competitive keywords, denoted by s.Cand. But there may be some noises existing in the candidate set, making it ineffective to advertise directly. For a speci<sup>fi</sup>c item represented by a keyword, there may exists various topics perceived by different users. The associative keyword set could be deemed to serve as a comprehensive description of a topic, since it not only re<sup>fl</sup>ects versatile users’ intents on the item, but possesses a big enough sampling on search engine. In fact, competition between keywords is mainly driven by topic commonalities perceived by users. If the topic structure is extracted, it would bene<sup>fi</sup>t us to further identify effective competitive keywords from the candidate set. For this purpose, Latent Dirichlet Allocation (LDA) model [30], which is an unsupervised machine learning technique to identify latent topics from large documents collection, would be adopted. This probabilistic generative model assumes that every document can be treated as a distribution over topics and every topic is a distribution over words. The associative keywords thus serve as a characteristic pro<sup>fi</sup>le for each candidate and the same case with the seed keyword. These characteristic pro<sup>fi</sup>les could be collected to constitute a query corpus, based on which a LDA based processing on query logs can be designed, as shown in Fig. 3.

Suppose that, given a seed keyword s, the set of its candidate competitive keywords denoted by s.Cand has been derived. The keyword s and the candidates compose a new keyword set, denoted by I = {s} s.Cand. Each keyword i in the set I owns a list of <sup>[</sup>associative keywords, i.e., i.AK. Since the associative keywords are queried by various users, they can be deemed to constitute a characteristic pro<sup>fi</sup>le for the keyword i. Meanwhile, each associative keyword is af<sup>fi</sup>liated with a value of search volume according to Definition 1. Then for each keyword i, its corresponding characteristic pro<sup>fi</sup>le can be constructed as follows,

$$
i. P r o f = \{(w, w. v o l) | w \in i. A K \}\tag{4}
$$

where w denotes a keyword composing the pro<sup>fi</sup>le and w.vol indicates its corresponding search volume. This characteristic pro<sup>fi</sup>le i.Prof suggests how search engine users perceive and describe the keyword i. Such characteristic pro<sup>fi</sup>les of all the keywords in I can be collected as a corpus, which could be de<sup>fi</sup>ned as $C o r p = \{ i . P r o f | i \in I \}$ . This corpus could be further used as the text <sup>2</sup>source to detect latent topics for the keywords in I.

According to the framework of LDA, the characteristic pro<sup>fi</sup>le i. Prof of each keyword i is interpreted as a multinomial distribution Mult(u) over a series of topics T = {t}. And each topic t is assigned a multinomial distribution Mult(’) over all the words $W = \{ w \}$ in Corp. u and $\varphi$ represent two dirichlet distributions with hyperparameters a and $\beta$ respectively, denoted by u Dir(u|a) and $\varphi \sim D i r ( \varphi | \beta )$ <sup></sup>. For each word w in the pro<sup>fi</sup>le i.Prof, sample a topic t <sup></sup>from the multinomial distribution Mult(u) speci<sup>fi</sup>c with the characteristic pro<sup>fi</sup>le i.Prof. And subsequently sample the observed word w from the multinomial distribution Mult(’) associated with the topic t. Therefore, the generation probability of each word w in the corpus Corp can be formulated as follows,

$$
p (w | i. P r o f) = p (w | t, \beta) p (t | i. P r o f, \alpha)
$$

$$
= \int p (w | \phi) D i r (\phi | t, \beta) d \phi \int p (t | \theta) D i r (\theta | i. P r o f, \alpha) d \theta\tag{5}
$$

Repeating the sampling process above for each word w in a characteristic pro<sup>fi</sup>le with w.vol rounds and then repeating for all the characteristic pro<sup>fi</sup>les of the keywords would <sup>fi</sup>nally give the observed query corpus Corp, whose generation probability can be

![](/api/attachments/K224ZTYX/fulltext/images/8bb81870ad6bcef344a1716f9f1eb27d7cff1c16d2400a1625f052fbe9c6afba.jpg)  
Fig. 3. The LDA processing on query logs.

Please cite this article in press as: D. Qiao, et al., Finding competitive keywords from query logs to enhance search engine advertising, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.11.003

expressed as follows,

$$
p (C o r p) = \prod_ {i \in I} \prod_ {w \in i. p r o f} \prod_ {1 \leq r \leq w. v o l} p _ {r} (w | i. P r o f)\tag{6}
$$

To estimate the parameters u and ’ as well as the latent variables t, the Gibbs sampling [31], i.e., a fast and effective algorithm for approximate inference, is applied to infer the model. After parameter estimation, information about the latent topics of these keywords is acquired. Each keyword i is projected into a topic distribution, denoted by $\{ p _ { t } \}$ , where $p _ { t }$ stands for the probability that the particular keyword i belongs to the topic t. From the perspective of users, it means to what extent that the item represented by i could compete with alternative items on the topic t.

The topic structures derived from LDA modeling map how each item distributes on different topics, which could serve as important clues to infer the competitive relationships between items. In addition to these modeled topics, the query log information of each item should also be considered in identifying the competitive structures. For example, the search volume of each item re<sup>fl</sup>ects its popularity in the mind of search engine users, to some extent revealing the market position of this speci<sup>fi</sup>c item. It should also be noticed that the competitive relationship between a pair of items may also be correlated with other items active in the market instead of being isolated from others. An item may simultaneously compete with many other items in the whole market. Therefore, an item would allocate its limited resources on these multiple competitive relationships. This allocation would then in<sup>fl</sup>uence the extent of different competitive relationships confronted with the item. For example, in the car market Toyota competes with Nissan and Honda at the same time. The competition with Nissan may to some extent shift Toyota’s focus on the competition with Honda. One competitive relationship may in<sup>fl</sup>uence the other as a result. Thus, it’s quite necessary to account for this dependency in predicting the competitive relationship. In summary, two pieces of information could hence be considered to help infer the competitive relationships between items: (1) each item’s own characteristics including search volume and topic distribution; (2) different competitive relationships correlated with other items in the market.

The previous process of candidate keyword generation enables us to get a set of candidate competitive keywords for each item, i.e., the seed keyword. The next step is to use the information described above to further identify the real and effective competitive keywords. Speci<sup>fi</sup>cally, given the seed keyword s and a candidate c in s.Cand, we need to predict whether the relationship between the two keywords, denoted by $< s , c > ,$ , is competitive or not. Here the Factor Graph Model could be adopted to achieve the goal of classifying competitive relationships [32–34]. Factor graph modeling is an instance of graphical modeling which visually expresses the dependency structures between items. Matching to the current case, items and their relationships in the market can be modeled as a graph where each node represents a keyword and each edge denotes the relationship between a pair of keywords. Our goal is to get to know the labels of all the relationships, estimating whether they are competitive or not.

As described above, topic information and query log information are important characteristics, which could be utilized in factor graph modeling to predict the competitive relationships. In general, a set of features $X = \{ x _ { 1 } , x _ { 2 } , \ldots x _ { n } \}$ associated with each edge can be derived to characterize the query log information. Therefore, the relationships (represented as $L )$ between keywords can be expressed as probabilities conditioning on X, i.e., P = {L|X}. That is to say, these features signify whether each pair of keywords could potentially constitute competitive relationships. Two types of functions could be de<sup>fi</sup>ned for each edge j, which has a label $l _ { j }$ indicating whether this is a competitive relationship or not. For such a speci<sup>fi</sup>c edge with $l _ { j } , F ( l _ { j } , X )$ is a function de<sup>fi</sup>ned on features X for the edge and its two nodes. $H ( l _ { j } , L )$ is a function indicating the correlations between different edges. The factor graph model thus represents all the keyword relationships as the factorization below,

$$
p (L | X) = \prod_ {j} F (l _ {j}, X) H (l _ {j}, L)\tag{7}
$$

where j is the relationship index between each pair of keywords, and l represents the label of the relationship. Without loss of generality, two main features with respect to query log information are considered in X. Since the set of features X is mainly derived from query logs, the volume of each keyword on a speci<sup>fi</sup>c edge is directly used as a feature in X. Moreover, as discussed in Section 3.1, each candidate competitive keyword shares a common mediate keyword with the seed item. Therefore, the feature of joint search volume is also included in $X ,$ which represents the associative relationship between the node keyword and the common mediate keyword on this edge. It is worth noting that the volumes of keywords and the joint search volumes can represent the most information of query logs. In the factor graph model, features $X$ is still an open vector, which can be easily integrated with other characteristics of query logs in accordance with speci<sup>fi</sup>c conditions. The regional function $H ( l _ { j } , L )$ represents how a speci<sup>fi</sup>c edge correlates with other edges in the graph. This correlation is de<sup>fi</sup>ned here as sharing keywords among edges. When two competitive relationships share some keyword simultaneously, they are expected to interact with each other in the market. This phenomenon of keyword sharing re<sup>fl</sup>ects the overlap between different competitive relationships, allowing us to take the competition dependency into account.

In addition to the search volume information in query logs, we could also know what kind of topics each item associates with in the query logs. Two competitive items should be related with similar topics due to market overlaps. Therefore, topic information is very important to help judge the competitive relationship. Thus, the factor graph model could be expanded with the topic information as follows,

$$
p (L | X, Q) = \prod_ {j} F (l _ {j}, X) T \left(l _ {j}, p _ {j 1}, p _ {j 2}\right) H (l _ {j}, L)\tag{8}
$$

where $p _ { j 1 }$ and $p _ { j 2 }$ represent the topic probability of the two keywords associated with the edge $l _ { j } ,$ and the new factor $T ( l _ { j } , p _ { j 1 } ,$ $p _ { j 2 } )$ represents the posterior probability of $l _ { j }$ based on the topic structures. To specify these factor functions, the common formalization, namely exponential-linear function [34], is de<sup>fi</sup>ned as follows,

$$
F (l _ {j}, X) = \frac {1}{z _ {1}} \exp \left\{\sum_ {m} \mu_ {m} \times f _ {m} (l _ {j}, X) \right\}\tag{9}
$$

$$
H (l _ {j}, L) = \frac {1}{z _ {2}} \exp \left\{\sigma \times h (l _ {j}, L) \right.\tag{10}
$$

$$
T \left(l _ {j}, p _ {j 1}, p _ {j 2}\right) = \frac {1}{z _ {3}} \exp \left\{r \times t \left(l _ {j}, p _ {j 1}, p _ {j 2}\right) \right\}\tag{11}
$$

where $z _ { 1 } , z _ { 2 } , z _ { 3 }$ are normalization factors, $f _ { m } \left( l _ { j } , X \right)$ represents the $m _ { t h }$ feature function, $h ( l _ { j } , L )$ denotes an indicator function to represent the correlations between keyword relationships, and $t ( l _ { j } ,$ $p _ { j 1 } , p _ { j 2 } )$ is de<sup>fi</sup>ned as the proximity of topic structure for the two keywords in the relation $l _ { j } .$ The learning process in the proposed method is to estimate a parameter con<sup>fi</sup>guration o $( \alpha , \beta , \mu , \sigma , r )$ , so that the likelihood presented in Eq. (8) could be maximized. Two steps are then needed to <sup>fi</sup>nish this modeling process. First, the

```txt
ALGORITHM 1.
TCK (TOPIC BASED COMPETITIVE KEYWORDS SUGGESTION)
Input: Query logs Q, The seed keyword s.
Output: The competitive keyword set CK = {ck₁, ck₂...}.
Begin:
Preprocessing (Q) by Stanford Word Segmenter
Step1:    /* Candidate keywords generation*/
1.    CAND = Φ    /* To store the candidate competitive keywords*/
2.    RELATION = Φ    /* To store the relation pairs for the factor graph modeling*/
3.    TRIPLE = Φ    /* To store the triple information for the factor graph modeling*/
4.    CORP = Φ    /* To store the corpus for LDA modeling */
5.    s.AK = Find_Associative_Keyword_Set (Q, s)
    /* Conduct co-occurrence analysis through query logs*/
6.    s.Prof = Build_Characteristic_Profile (Q, s.AK)
7.    CORP = CORP U { s.Prof }
8.    for each keyword a in s.AK do
9.    a.AK = Find_Associative _Keyword_Set (Q, a)
10.    for each keyword c in a.AK do
11.    CAND = CAND U {c}
12.    RELATION = RELATION U {<s, c>}
13.    X = Calculate_Feature_Vector (Q, <s, c>)
    /* Calculate the features associated with the relation <s, c> based on query logs*/
14.    TRIPLE = TRIPLE U {<s, c, X>}
15.    c.AK = Find_Associative_Keyword_Set (Q, c)
16.    c.Prof = Build_Characteristic_Profile (Q, c.AK)
17.    CORP = CORP U {c.Prof}
18. end
19. end
20. I = CAND U {s}    /* To store the seed keyword and all the candidates*/
Step2:    /*Topic based competitive keywords suggestion*/
21. repeat
22. repeat
23.    for each topic t do
24.    Gibbs_Sample_Mixtureφ ~ Dir(φ,β)
25.    end
26.    for each keyword i in I do
27.    i.Prof = Get_Characteristic_Profile (CORP, i)
28.    Gibbs_Sample_Mixtureθ ~ Dir(θ|α)
29.    for each word w in i.Prof do
30.    repeat
31.    Gibbs_Sample_Topic t~Mult(t|θ,α, i.Prof)
32.    Gibbs_Sample_Word w~Mult(w|φ, β,t)
33.    until w.vol rounds
34.    end
35. end
36. until Convergence
37. IT = Update_Topic_Distribution (I, θ, φ)
/* Each element in IT is a keyword distribution over topics.*/
/* Adopt the sum-product algorithm to learn the factor graph*/
38. repeat
39. Calculate_Likelihood_Equation (8)_Through_LBP (Q, TRIPLE, IT)
40.    (μ,σ,r) = Update_Parameters_Using_Gradient_Descent_Method (Q, TRIPLE, IT)
41.   until Convergence
42.   until Convergence
43. L = Label_Relaitonships (TRIPLE, μ, σ, r)
44. CK = Get_Effective_Competitive_Keyword_Set (TRIPLE, L)
45. OutPut(CK)
```

Gibbs sampling [31] is used to maximize p(Corp|a, b) in Eq. (6). Based on the results of LDA modeling, the next step is to maximize the joint probability p(L|X, Q) through the sum-product algorithm. In the second step, the gradient descent method is introduced to update the parameters in each round. As the graphical structure may be arbitrary and contain cycles, the Loopy Belief Propagation (LBP) approximate algorithm is adopted to obtain the gradient for parameter con<sup>fi</sup>guration update. The whole learning process would iteratively compute over the above two steps until the joint probability in Eq. (8) converges. It can be observed that the topic structure mined from query logs is timely updated into the subsequent prediction of the relationships, since the search engine users’ intents and perceptions have been incorporated. Finally, the relationships between each pair of keywords in the factor graph could be labeled as competitive or non-competitive and only keywords marked as competitive would be suggested to advertisers.

D. Qiao et al. / Information & Management xxx (2016) xxx–xxx

## 3.3. An illustrative example

To better understand the process of the TCK method, an example of competitive keyword suggestion for the seed keyword ‘Budweiser’ is illustrated. Based on Baidu query logs, the associative analysis is conducted to retrieve the associative keywords, exempli<sup>fi</sup>ed in Fig. 4, where the root denotes the seed keyword and each edge indicates an associative relationship. For example, the keyword ‘beer’ is observed to associate with the seed ‘Budweiser’ since they co-occur frequently in query logs. Traditionally, this keyword is recommended to the advertiser as it can help ‘Budweiser’ advertisers target the users who query the keyword ‘beer’. However, in the beer market, there are many alternative merchants and advertisers who bid on the keyword ‘beer’. The intensive competition acutely increases the dif<sup>fi</sup>culty and cost to obtain the keyword ‘beer’, leading to failure of advertising on ‘beer’. This case occurs to the other keywords in the second layer like ‘beer agent’ and ‘draft beer’.

![](/api/attachments/K224ZTYX/fulltext/images/daa8c7d3f4cce62b8aba4adf20ec2f690b9bb889a6c2d3bca412bd1bda841f4d.jpg)  
Fig. 4. An example of associative keywords for ‘Budweiser’.

The proposed method TCK takes a further step to analyze the indirect associations between keywords. That is to say, the associative relationships for the second-layer keywords are also explored. This expands the tree of keyword relationships, as shown in Fig. 5, where keywords in the third layer constitute indirect associative relationships with the seed keyword in virtue of the second-layer keywords. As discussed above, the third-layer keywords can be coarsely considered as candidate competitive keywords of ‘Budweiser’ since they share common topics with the seed keyword. The majority of the candidates (e.g., Heineken) are competitors of ‘Budweiser’. They rival with each other in the beer market and are searched by users with the same conjoint keywords due to the topic commonality, e.g., beer, beer agent, draft beer and so on.

In Fig. 5, it’s easy to <sup>fi</sup>nd that some keywords such as ‘league cannot be effectively utilized for competitive advertising. Thus the method TCK would further extract and deploy the topic information of these candidates to remove noisy keywords. For each candidate keyword in Fig. 5, TCK can mine a series of associative keywords which can function as a characteristic pro<sup>fi</sup>le for the candidates. Leveraging these characteristic pro<sup>fi</sup>les, TCK conducts a topic based factor graph modeling. Then the relationship between each candidate and the seed ‘Budweiser’ is labelled to be competitive or non-competitive. In Fig. 6, it could be observed that the candidate ‘league’, ‘KTV’ and ‘butter’ is crossed out indicating that they are non-competitive with ‘Budweiser’. By

![](/api/attachments/K224ZTYX/fulltext/images/171ce4ddb626ae4532b8ec0674c03012fb55e33382145b38c635d43957dbfd95.jpg)  
Fig. 5. An example of candidate competitive keywords for ‘Budweiser’.

![](/api/attachments/K224ZTYX/fulltext/images/e53dd328330d0638e371bde5db93a3930c780f6f0c41aa2f919789be79285189.jpg)  
Fig. 6. An example of competitive keywords suggestion for ‘Budweiser’

Please cite this article in press as: D. Qiao, et al., Finding competitive keywords from query logs to enhance search engine advertising, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.11.003

removing these non-competitive candidates, a set of high-quality competitive keywords could be <sup>fi</sup>nally suggested to the advertisers.

Through the analysis on the seed keyword ‘Budweiser’ above, it can be observed that the proposed method can effectively suggest competitive keywords for the advertisers. This is helpful for the business merchants/advertisers to carry out competitive advertising.

## 4. Algorithm and ef<sup>fi</sup>ciency analysis

## 4.1. Algorithmic details

Following the analysis above, a set of competitive keywords can be suggested for the seed keyword by running TCK. Candidate keywords which don’t have competitive relationships with the seed keyword would be removed. Only the candidates really competing with the seed keyword are recognized as quali<sup>fi</sup>ed competitive keywords. To better present the whole process of the topic based competitive keywords suggestion method, the details of pseudo-codes are listed as follows.

The whole process of the method TCK consists of two major steps. The <sup>fi</sup>rst step is to generate candidate keywords for a given seed keyword s. It incorporates two rings of co-occurrence analysis to <sup>fi</sup>nd the candidate competitive keywords in query logs. Therefore, the time complexity is mainly determined by two parameters, namely the length of query logs and the number of keywords associated with the seed keyword. For each associative keyword, its corresponding associative keywords should be further scanned in query logs Q. Naturally, the process should be conducted query by query. Denote that the length of query logs Q is l and the number of associative keywords for the seed keyword is n. The time spent on the <sup>fi</sup>rst step is O(ln).

In the second step, the method TCK attempts to utilize the latent topic structure of the keywords to identify competitive keywords. It transfers the problem of keywords mining into the prediction of relationships between keywords over a factor graph model. To accomplish such a task, a predictive function should be trained, which can be achieved by maximizing the joint probability in Eq. (8) iteratively. In each round of the iterative process, one time of LDA modeling should be processed on the whole query logs. Therefore, the time of LDA modeling is crucial to the computation of the second step and the LDA process is to repeatedly sampling the topic and the keyword for the whole corpus. Denoting the average number of the associative keywords for a keyword as n, the size of the corpus is about n<sup>2</sup>. Suppose there are m latent topics for these keywords, the time complexity of LDA modeling thus equals O (mn<sup>2</sup>).

The above analysis shows that the overall time complexity of TCK can be expressed as $O ( l n ) + O ( m n ^ { 2 } )$ . Compared with the length of query logs, e.g., usually tens of thousands or more, the size of associative keywords and the number of latent topics are usually quite small, e.g., couples or dozens, thus m, $n ^ { 2 } < < l .$ Therefore, the time complexity of the proposed TCK is mainly linearly determined by the length l of query logs.

## 4.2. Efficiency analysis

This subsection shows the experimental results on the ef<sup>fi</sup>ciency of the proposed method TCK with large scale of query logs. The method is designed to mine the topic information hidden in query logs for each keyword and then employ such topic information to identify competitive keywords in a factor graph model. As described above, the length l of the query logs signi<sup>fi</sup>cantly affects the time complexity of TCK. To present the ef<sup>fi</sup>ciency with various query log lengths, different scales of testing data ranging from $1 0 ^ { 4 }$ to $1 0 ^ { 5 }$ were synthesized, which is also the conventional size of query logs from real-world search engine. The query keywords and query times for each query log were synthesized randomly. Experimental results are as shown in Fig. 7, which indicates a nearly linear complexity of computation. It re<sup>fl</sup>ects that TCK possesses the scalability to deal with large scales of datasets, which is desirable. Besides, TCK can be further speeded up on more powerful computational platforms like Cloud and parallel computing systems.

![](/api/attachments/K224ZTYX/fulltext/images/a1eebd50b1ad3edb83190c320d7a169086a081c3997c96762330be2857f6b0b1.jpg)  
Fig. 7. The running time for different lengths of query logs.

Moreover, although the proposed method has great potential in computation, it mainly focuses on of<sup>fl</sup>ine analysis in practice according to the way of obtaining query logs. The mainstream search engine platforms iteratively process and organize original queries and transform them into query logs which is stored in the backstage. Therefore, based on query logs of search engines, the keyword suggestion function can also be deployed in the backstage. When advertisers request for suggested keyword, the currently derived keywords could then be presented to them. Because query logs are obtained from two popular search engines of Google and Baidu. Therefore, the proposed method can cover the majority of recent online users’ searching keywords in a timely manner due to the popularity of Google and Baidu, although this is basically an of<sup>fl</sup>ine manner.

## 5. Experimental results

The proposed method TCK can expand the choices of relevant keywords for advertisers in search engine advertising. Moreover, it helps advertisers achieve the strategy of competitive advertising. Therefore, data experiments were conducted from two above perspectives to demonstrate the effectiveness of TCK. The detailed analysis about the experimental results are presented as follows.

## 5.1. Experimental setup

## 5.1.1. Dataset

We perform experiments on query logs collected from Baidu Tuiguang<sup>2</sup>. It is the keyword tool of the search engine Baidu, which occupies the largest share of the search engine market in China [35]. Baidu Tuiguang supports free download of daily query log data for a given keyword in Baidu. The dataset obtained from Baidu Tuiguang is pre-processed with built-in functions, e.g., segmenting, aggregating and clustering words and phrases, and appears in a more structured form. Thereafter, the derived query logs are characterized by query keywords and the corresponding daily search volume, as presented in Table 1.

Twenty seed keywords in different domains were randomly selected for the experiments. To ensure the diversity of domains, the seed keywords were motivated from the mainstream product/ service category [7] of Taobao.com, which is the largest online shopping market in the world and also the pro<sup>fi</sup>t engine of the world’s largest e-commerce <sup>fi</sup>rm, the Alibaba Group [36]. The set of seed keywords are listed below in Table 2. Based on these seed keywords, approximately 8500 query logs on October 2014 were crawled.

## 5.1.2. Evaluation methodology

The TREC-type evaluation methodology was adopted to demonstrate the effectiveness of TCK. TREC-type is one of the classical evaluation methods for information retrieval and search engine performance [37] and has also been widely used in evaluating keywords suggestion methods [1,7,11]. Ground truth labeling of the suggested keywords was provided by 6 human evaluators. To guarantee the quality of the evaluation, all evaluators are Ph.D. students from the department of management information systems, experienced at online shopping and familiar with search engine ads. Each suggested keyword was paired with its corresponding seed keyword, forming a total of around 12000 pairs by collecting results from the TCK method as well as six other methods. To ensure fairness, by which method the keyword was suggested was shielded to the evaluators, and each pair was assigned randomly to three evaluators for evaluation. Besides, for each pair (the seed keyword and the suggested keyword), the evaluators were required to give two evaluations, i.e., whether the suggested keyword was a relevant keyword for the seed keyword and whether it was a competitive keyword for the seed keyword. Only when the agreement was achieved by at least two evaluators, was the suggested keyword considered as an effective relevant or competitive keyword.

## 5.1.3. Benchmark methods

In order to better verify the performance of the TCK method, empirical comparison experiments were conducted with six benchmark methods. Firstly, the naive factor graph model denoted by FGM was used as a baseline, which doesn’t take topic modeling into account. As presented above, TCK <sup>fi</sup>nally transforms the problem of competitive keywords suggestion to the classi<sup>fi</sup>cation of relationships between keywords. Hence two typical classi<sup>fi</sup>cation methods, i.e., libSVM [38,39] and logistic regression (short for LR) [38,40], which are often used for classi<sup>fi</sup>cation, were also compared with TCK. When running the three methods, the same candidates and features with TCK were employed. The previous literature review section summarizes three streams of keyword suggestion methods: co-occurrence based, proximity based and meta-tag based methods. Considering the data context appropriateness, i.e., without incorporating exogenous knowledge, two

## Table 2

<table><tr><td>Index</td><td>Seed Keyword</td><td>Index</td><td>Seed Keyword</td></tr><tr><td>1</td><td>Budweiser</td><td>11</td><td>Pantene</td></tr><tr><td>2</td><td>Canny Elevator</td><td>12</td><td>Pingan Insurance</td></tr><tr><td>3</td><td>Colgate</td><td>13</td><td>Skype</td></tr><tr><td>4</td><td>Columbia Sportswear</td><td>14</td><td>Sony</td></tr><tr><td>5</td><td>Dove</td><td>15</td><td>Tide</td></tr><tr><td>6</td><td>Fanta</td><td>16</td><td>Tuniu.com</td></tr><tr><td>7</td><td>iReader</td><td>17</td><td>Wedome</td></tr><tr><td>8</td><td>Longines</td><td>18</td><td>YOPOO</td></tr><tr><td>9</td><td>MEIZU</td><td>19</td><td>Yoshinoya</td></tr><tr><td>10</td><td>Midea</td><td>20</td><td>Yunifang</td></tr></table>

comparison methods, namely, Cooccur and Proximity, were compared in the experiments. For the Cooccur method, the mature commercial tool, i.e., Baidu Tuiguang, was employed, which enables to provide which keywords occur together on Baidu platform. Then the keywords co-occurring together with the seed keyword could be extracted for comparison. For the Proximity method, a context vector should be created for each term and then the semantic similarity between terms could be computed. Terms with high similarities would be suggested to advertisers. For the purpose of comparison, we here built the vector based on each word’s co-occurrences in the query logs, which is consistent to current context. Finally, keywords with proximity values above the average level would be considered as effective keywords for advertising. The third stream, i.e., meta-tag based, was not compared since it only extracts keywords from the meta-tag information of the webpages, i.e., exogenous knowledge needs to be incorporated, and is then not applicable to our current context. In addition, a recent method, i.e., CMiner [41], which also targets on detecting competitors, was also included to suggest competitive keywords for comparison. This method de<sup>fi</sup>ned a competitiveness measure between items as the coverage of their features and then used the coverage metric to <sup>fi</sup>nd competitive items. Similarly, items above the average coverage level would <sup>fi</sup>nally be chosen as the suggested results for advertising.

## 5.1.4. Measures

A typical metric, namely F -measure, was considered in the experiments to comprehensively evaluate the effectiveness of the methods. It’s commonly used in the performance measurement of information retrieval [42], keywords suggestion [6,14,29], and recommendation [43]. Given the seed keyword s, denote the keywords collection as $K = \{ K _ { 1 } , K _ { 2 } \cdot \cdot \cdot K _ { n } \}$ , in which $K _ { i }$ is a set of <sup>  </sup>keywords suggested by the method M correspondingly. In addition, $E _ { i }$ is a subset of $K _ { i }$ and contains only the effective (relevant or competitive) keywords for the seed keyword s. The metric $\mathrm { F } _ { 1 }$ -measure could be de<sup>fi</sup>ned as follows,

$$
\begin{array}{l} F _ {1} (M _ {i}) = 2 \times \text { Precision } (M _ {i}) \\ \quad \times \text { Recall } (M _ {i}) / (\text { Precision } (M _ {i}) + \text { Recall } (M _ {i})) \end{array}\tag{12}
$$

Where,

$$
\text { Precision } (M _ {i}) = | E _ {i} | / | K _ {i} |\tag{13}
$$

$$
\operatorname{Recall} \left(M _ {i}\right) = \left| E _ {i} \right| / \sum_ {j \in \{1, 2, \dots , n \}} \left| E _ {j} \right|\tag{14}
$$

In Eqs. (13) and (14), |E | and $| K _ { i } |$ represent the size of $E _ { i }$ and $K _ { i }$ respectively. Precision, by comparing the number of effective keywords to all the suggested ones, captures the suggestion accuracy of the corresponding method. Recall, by calculating the ratio between suggested effective keywords and the universal effective ones, measures the power of the method to suggest effective keywords. However, both precision and recall are biased. The promotion of either precision or recall would usually sacri<sup>fi</sup>ce with the decline of the other. The metric $\mathrm { F } _ { 1 } { \mathrm { - m e a s u r e } } ,$ calculated as their harmonic mean, can measure the performance of a keywords suggestion method from the two perspectives simultaneously. Therefore, F -measure is appropriate to compare the performance of TCK and other benchmark methods.

Besides, the metric of Novelty is used to measure the fraction of new effective keywords that are omitted or not found by other methods. For the seed keyword, these identi<sup>fi</sup>ed new effective keywords provide a broad choice for advertisers and decrease the advertising costs. Thus, the novelty matters much in the evaluation of keywords suggestion methods. The following gives its formulation based on the de<sup>fi</sup>nition in [43].

$$
\text { Novelty } (M _ {i}) = \frac {\left| E _ {i} \sum_ {j = 1 , j \neq i} ^ {n} E _ {j} \right|}{\left| K _ {i} \right|}\tag{15}
$$

In Eq. (15), the numerator equals the number of the effective keywords that are identi<sup>fi</sup>ed by the method M but not detected by the other methods. The measure Novelty can be regarded as the contributions of $M _ { i }$ to mining new potential effective keywords for the seed keyword s from query logs.

In the experiments, the evaluators were <sup>fi</sup>rstly requested to judge whether the suggested keyword was a relevant keyword for the seed keyword, which was denoted as “relevance evaluation”. Whereafter, the evaluators were asked to label whether the suggested keyword was a competitive keyword for the seed keyword, which was denoted as “competitiveness evaluation”. Based on the two types of evaluations, TCK was compared with six benchmark methods in terms of $\mathrm { F } _ { 1 }$ -measure and Novelty. For the given 20 seed items there are totally around 12000 distinct keywords suggested by the seven methods. The proposed method TCK could suggest the largest numbers of effective (relevant and competitive), keywords, i.e., 6327 and 4608, respectively. Other benchmark methods, however, can only suggest relatively smaller sets of relevant and competitive keywords for advertisers to choose. Concretely, the numbers of relevant keywords suggested by FGM, libSVM, LR, Cooccur, Proximity and CMiner are 3669,1444, 2395, 833, 2971, and 3160, respectively. The numbers of competitive keywords suggested by FGM, libSVM, LR, Cooccur, Proximity and CMiner are 2771, 1032, 1771, 182, 2303, and 2359, respectively. Therefore, a broader choice could be endowed by the proposed method TCK to advertisers. To further evaluate the performance of these keywords on the goal of search engine advertising, we conducted the following performance analysis in terms of relevance and competitiveness on each different item.

The implementation environment was a Windows 7 system on a PC with Intel Core i3-2100 CPU (3.1 GHz) and 4G RAM. The programs of TCK, FGM and CMiner were implemented with the basic routines in java. As for the method libSVM and LR (Logistic Regression), the popular software Weka 3.7.10 was employed to conduct the analysis.

## 5.2. Experiments on relevance evaluation

Experiments were executed to compare the performance of these methods based on relevance evaluations. Fig. 8 shows the comparison values across the seven methods for all 20 seed keywords. The numbers of the horizontal coordinate represent the indexes of 20 seed keywords as introduced in Table 2. The results in Fig. 8(a) indicate that TCK has the best $\mathrm { F } _ { 1 }$ -Measure values for the 20 seed keywords. It provides suf<sup>fi</sup>cient evidences that TCK shows better performance than benchmark methods to suggest relevant keywords across various domains.

In the market of search engine advertising, the advertisers tend to <sup>fi</sup>ght for a limited number of hot keywords. That leads to high expenses for them, who actually need broader choices to conduct advertising. It’s very important for a keyword suggestion method to provide novel alternative keywords for advertisers. As de<sup>fi</sup>ned above, the measure of Novelty is to assess the innovation of a particular method to extract novel keywords. The larger the novelty value of a method is, the better it performs to provide novel and relevant keywords. Fig. 8(b) shows the experimental results on the novelty value of the seven methods. For most of the seed keywords, TCK has the largest novelty value. Thus the proposed method contributes to suggesting more new relevant keywords.

To further verify the advantage of TCK over other benchmark methods, statistical analysis was conducted through both paired ttest and Friedman test as shown in Table 3. First we can observe that F -Measure values of TCK are signi<sup>fi</sup>cantly larger than the other six comparative methods based on relevance evaluation. As de<sup>fi</sup>ned in above, $\mathrm { F _ { 1 } - m e a s u r e }$ is a comprehensive metric, which re<sup>fl</sup>ects the precision and recall of a keywords suggestion method in a combined manner. These testing results reveal that the proposed method TCK has comparable advantages to suggest relevant keywords than the other six methods. It can not only provide a reliable set of keywords more accurately, but also mine more relevant keywords lurked in the market to expand the choices of advertisers. Second, testing results show that the novelty values of TCK are signi<sup>fi</sup>cantly larger than the other six comparative methods based on the relevance evaluation, further verifying that the proposed method TCK can provide more innovative keywords for advertisers.

(a) Relevance evaluation on $\mathrm { F } _ { 1 }$ -Measure values  
![](/api/attachments/K224ZTYX/fulltext/images/e1b8ca8da1b7e6fa79c4e481db1dd9760e80e7bf9f548f488d9873be151e22e1.jpg)

(b) Relevance evaluation on Novelty values  
![](/api/attachments/K224ZTYX/fulltext/images/ceab5538e1afca0a463102b5372e2e6f19f8ba0b26252b47d1370371e2d57522.jpg)  
Fig. 8. Relevance evaluation across seven methods

Please cite this article in press as: D. Qiao, et al., Finding competitive keywords from query logs to enhance search engine advertising, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.11.003

D. Qiao et al. / Information & Management xxx (2016) xxx–xxx

Statistical tests on relevance evaluation.

<table><tr><td>Hypotheses</td><td>Baselines</td><td>Paired t-test t-value</td><td>Friedman test  $\chi^2$  value</td></tr><tr><td rowspan="6"> $F_1-Measure\ value\ of\ Baseline^5 < F_1-Measure\ value\ of\ the\ TCK$ </td><td>FGM</td><td>-5.355 (*** )</td><td>20.000 (*** )</td></tr><tr><td>libSVM</td><td>-23.762 (*** )</td><td>20.000 (*** )</td></tr><tr><td>LR</td><td>-21.233 (*** )</td><td>20.000 (*** )</td></tr><tr><td>Cooccur</td><td>-16.898 (*** )</td><td>20.000 (*** )</td></tr><tr><td>Proximity</td><td>-12.939 (*** )</td><td>20.000 (*** )</td></tr><tr><td>CMiner</td><td>-13.274 (*** )</td><td>20.000 (*** )</td></tr><tr><td rowspan="6">Novelty value of Baseline &lt; Novelty value of the TCK</td><td>FGM</td><td>-6.662 (*** )</td><td>20.000 (*** )</td></tr><tr><td>libSVM</td><td>-8.044 (*** )</td><td>20.000 (*** )</td></tr><tr><td>LR</td><td>-3.869 (** )</td><td>12.800 (** )</td></tr><tr><td>Cooccur</td><td>-8.044 (*** )</td><td>20.000 (*** )</td></tr><tr><td>Proximity</td><td>-6.853 (*** )</td><td>20.000 (*** )</td></tr><tr><td>CMiner</td><td>-6.549 (*** )</td><td>20.000 (*** )</td></tr></table>

Notes: \*: p < 0.05; \*\*: p < 0.01; \*\*\*: p < 0.001; : no signi<sup>fi</sup>cance.

Whether for the metric of F -measure or Novelty, TCK has been well supported to outperform the other six benchmark methods in relevance evaluation. Thus the proposed method can be used to broaden the choices of relevant keywords for search engine advertising.

## 5.3. Experiments on competitiveness evaluation

As described above, the market of search engine advertising is pursuing a new strategy, i.e. competitive advertising. Therefore, it’s crucial for a particular keyword suggestion method to suggest competitive keywords. The following presents experimental results to demonstrate the performance of TCK for suggesting competitive keywords.

Fig. 9 shows the competitiveness evaluation of the seven methods for all 20 seed keywords. Results in Fig. 9(a) show that TCK possesses the best F -Measure values for the 20 seed keywords among the seven methods. In addition, the analysis of Novelty values in Fig. 9(b) also demonstrates that TCK performs far better than baselines for most of the seed keywords. Traditional keywords suggestion tool, like Google and Baidu, usually do not provide competitive keywords for advertisers. As an emerging and necessary advertising strategy, competitive advertising promotes the needs for competitive keywords suggestion. TCK is proved to be able to provide high-quality competitive keywords, thus well responding to the market needs.

Further evidences are provided from the statistical results tested by paired t-test and Friedman test as shown in Table 4. It again proves that TCK is superior to other benchmark methods on suggesting competitive keywords in terms of both F -measures and novelty. It can mine more competitive keywords with high accuracy, providing great convenience for the advertisers to conduct competitive advertising. Besides, the competitive keywords suggested by TCK are scarcely discovered in the existing methods, which is very valuable to advertisers since they can execute competitive poaching and pay a low expense to the new keywords as well.

From the comparative experiments above, some conclusions about the effectiveness of TCK could be draw. First, TCK shows good performance on F -measure on both relevance evaluation and competitiveness evaluation, revealing that TCK is effective to suggest high quality keywords, especially competitive keywords for advertisers in the market of search engine advertising. Second, as for the measure of Novelty, TCK achieves better performance than other benchmark methods. Especially when considering the competitiveness evaluation, TCK is far superior to the other six methods. This gives suf<sup>fi</sup>cient evidences that TCK is a valuable method to support competitive advertising.

## 6. Conclusions and discussions

This paper proposed a topic based competitive keywords suggestion method to help advertisers promote competitive advertising on search engines. Extensive experiments were conducted to demonstrate the advantages of the proposed method. To summarize, the proposed work makes several major theoretical and practical contributions. First, this study offers a new lens on competitive advertising. As one of the <sup>fi</sup>rst attempts, the concept of competitive keywords from query logs is pragmatised, which can take advantage of agilely accumulated users’ intentions on search engine, to elaborate competitive advertising. This is quite important in current advertising market, which is characterized by the highly speeding competitive atmosphere. Second, the choice of keyword advertising is greatly expanded with the proposed TCK method, which provides more novel keywords and broadens the scope of keywords selection for advertisers. Instead of following the trend to bid on some generic or popular keywords, the advertisers could be supported by the proposed TCK method in a more accurate and distinguishable manner to target on their potential users. Third, we contribute to performance improvement of keyword suggestion methods. Compared with prior methods, the proposed TCK method shows a better performance from different perspectives.

However, there still exist some limitations which could be further explored in the study. First, query logs are generated by crowds, which may contain noises and disturbance. More advanced techniques may be designed to further help purify the query logs to make them more applicable for competitive advertising. Second, as a re<sup>fl</sup>ection of users’ intentions, query logs may neglect the needs of advertisers. How to well involve the advertisers’ preferences into this competitive keyword suggestion process is therefore demanding and essential. Third, the proposed TCK method is essentially a classi<sup>fi</sup>cation method, which does not provide a sequence of results directly. Nevertheless, with the development of search engine advertising, the sequence of keywords will to some extent impact the advertisers’ choice. Therefore, how to elaborate an appropriate sequence of suggested keywords is explicitly a promising research direction in competitiveness keyword suggestion and analysis. Furthermore, considering the big data context, though the proposed TCK method is generally ef<sup>fi</sup>cient, its performance could be further optimized by speeding up with parallel systems or designing an incremental

D. Qiao et al. / Information & Management xxx (2016) xxx–xxx

(a) Competitiveness evaluation on F₁-Measure values  
![](/api/attachments/K224ZTYX/fulltext/images/f72b05957111935ed741bfcd1c4c9af99f8ab9515b49c7d1d38466691ab610c8.jpg)

(b) Competitiveness evaluation on Novelty values  
![](/api/attachments/K224ZTYX/fulltext/images/94247997809a71741d6819121a9560a71347bde1d361cd55a8c7e55567247996.jpg)  
Fig. 9. Competitiveness evaluation across seven methods

Table 4  
Statistical tests on competitiveness evaluation.

<table><tr><td>Hypotheses</td><td>Baselines</td><td>Paired t-test t-value</td><td>Friedman test  $\chi^2$  value</td></tr><tr><td rowspan="6"> $F_1-Measure$  value of Baseline &lt; $F_1-Measure$  value of the TCK</td><td>FGM</td><td>-4.956 (*** )</td><td>20.000 (*** )</td></tr><tr><td>libSVM</td><td>-15.587 (*** )</td><td>20.000 (*** )</td></tr><tr><td>LR</td><td>-14.930 (*** )</td><td>20.000 (*** )</td></tr><tr><td>Cooccur</td><td>-18.870 (*** )</td><td>20.000 (*** )</td></tr><tr><td>Proximity</td><td>-7.223 (*** )</td><td>20.000 (*** )</td></tr><tr><td>CMiner</td><td>-8.256 (*** )</td><td>16.200 (*** )</td></tr><tr><td rowspan="6">Novelty value of Baseline &lt; Novelty value of the TCK</td><td>FGM</td><td>-6.197 (*** )</td><td>20.000 (*** )</td></tr><tr><td>libSVM</td><td>-7.016 (*** )</td><td>20.000 (*** )</td></tr><tr><td>LR</td><td>-3.667 (**)</td><td>9.800 (*** )</td></tr><tr><td>Cooccur</td><td>-7.016 (*** )</td><td>20.000 (*** )</td></tr><tr><td>Proximity</td><td>-6.137 (*** )</td><td>16.200 (*** )</td></tr><tr><td>CMiner</td><td>-5.663 (*** )</td><td>20.000 (*** )</td></tr></table>

Notes: \*: p < 0.05; \*\*: p < 0.01; \*\*\*: p < 0.001; : no signi<sup>fi</sup>cance.

strategy, etc. In addition to competitive keyword suggestion, these user-crowded query logs are diachronic, which may provide a good opportunity to investigate the evolution of competitive structure dynamically. This could bene<sup>fi</sup>t deeper understanding of users’ intentions and achieve the goal of competitive analysis in an intelligent and dynamic manner.

## Acknowledgments

The work was partly supported by the National Natural Science Foundation of China (71490724/71402186/71372044/ 71110107027), and the MOE Project of Key Research Institute of Humanities and Social Sciences at Universities of China (12JJD630001).

## References

[1] Fuxman, A. Tsaparas, P. Achan, K. Agrawal, R, Using the wisdom of the crowds for keyword generation, Proceedings of the 17th International Conference on

World Wide Web, Beijing, China, 2008, pp. 61–70, doi:http://dx.doi.org 10.1145/1367497.1367506.

[2] B.J. Jansen, Z. Liu, Z. Simon, The effect of ad rank on the performance of keyword advertising campaigns, J. Am. Soc. Inf. Sci. Technol. 64 (10) (2013) 2115–2132.

[3] W. Luo, D. Cook, E.J. Karson, Search advertising placement strategy: exploring the ef<sup>fi</sup>cacy of the conventional wisdom, Inf. Manage. 48 (8) (2011) 404–411.

[4] A.A. Kamis, E.A. Stohr, Parametric search engines: what makes them effective when shopping online for differentiated products? Inf. Manage. 43 (7) (2006) 904–918, doi:http://dx.doi.org/10.1016/j.im.2006.08.006.

[5] A. Ghose, S. Yang, An empirical analysis of search engine advertising: sponsored search in electronic markets, Manage. Sci. 55 (10) (2009) 1605– 1622.

[6] Y. Chen, G. Xue, Y. Yu, Advertising keyword suggestion based on concept hierarchy, Proceedings of the 2008 International Conference on Web Search and Data Mining, Stanford CA USA. 2008 pp. 251-260

[7] H. Wu, G. Qiu, X. He, Y. Shi, M. Qu, J. Shen, J. Bu, C. Chen, Advertising keyword generation using active learning, Proceedings of the 18th International Conference on World Wide Web Madrid Spain 2009 pp. 1095–1096.

[8] V. Abhishek, K. Hosanagar, Keyword generation for search engine advertising using semantic similarity between terms, Proceedings of the 9th International Conference on Electronic Commerce, Minneapolis, MN, USA, 2007, pp. 89–94, doi:http://dx.doi.org/10.1145/1282100.1282119.

Please cite this article in press as: D. Qiao, et al., Finding competitive keywords from query logs to enhance search engine advertising, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.11.003

[9] V. Dang, X. Xue, W.B. Croft, Inferring query aspects from reformulations using clustering, Proceedings of the 20th ACM International Conference on Information and Knowledge Management (2011) 2117–2120.

[10] D. Kelly, K. Gyllstrom, E.W. Bailey, A comparison of query and term suggestion features for interactive searching, Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval, Boston, MA, USA, 2009, pp. 371–378.

[11] A. Schwaighofer, J. Quiñonero, T. Borchert, T. Graepel, R. Herbrich, Scalable clustering and keyword suggestion for online advertisements, Proceedings of the 3rd International Workshop on Data Mining and Audience Intelligence for Advertising, Paris, France, 2009, pp. 27–36, doi:http://dx.doi.org/10.1145/ 1592748.1592753

[12] Y. Zhang, W. Zhang, B. Gao, X. Yuan, T. Liu, Bid keyword suggestion in sponsored search based on competitiveness and relevance, Inf. Process. Manage. 50 (4) (2014) 508–523.

[13] A. Ortiz Cordova, B.J. Jansen, Classifying web search queries to identify high revenue generating customers, J. Am. Soc. Inf. Sci. Technol. 63 (7) (2012) 1426– 1441.

[14] K. Bartz, V. Murthi, S. Sebastian, Logistic regression and collaborative <sup>fi</sup>ltering for sponsored search term recommendation, 2nd Workshop on Sponsored Search Auctions, Ann Arbor, Michigan, 2006.

[15] I. Szpektor, A. Gionis, Y. Maarek, Improving recommendation for long-Tail queries via templates, Proceedings of the 20th International Conference on World Wide Web, Hyderabad, India, 2011, pp. 47–56.

[16] J. Lambin, Optimal allocation of competitive marketing efforts: an empirical study, Journal of Business (1970) 468–484.

[17] P.S. Desai, W. Shin, R. Staelin, The company that you keep: when to buy a competitor's keyword, Market. Sci. 33 (4) (2014) 485–508.

[18] J. Eliashberg, R. Chatterjee, Analytical models of competition with implications for marketing: issues, <sup>fi</sup>ndings, and outlook, J. Market. Res. (1985) 237–261.

[19] A. Sayedi, K. Jerath, K. Srinivasan, Competitive poaching in sponsored search advertising and its strategic impact on traditional advertising, Market. Sci. 33 (4) (2014) 586–608.

[20] D. Fudenberg, J. Tirole, Customer poaching and brand switching, Rand J. Econ. (2000) 634–657.

[21] Z. Da, J. Engelberg, P. Gao, In search of attention, J. Finance 66 (5) (2011) 1461– 1499.

[22] J.B. Kim, P. Albuquerque, B.J. Bronnenberg, Mapping online consumer search, Journal of Marketing Research 48 (1) (2011) 13–27.

[23] A. Chuklin, P. Serdyukov, How query extensions re<sup>fl</sup>ect search result abandonments, Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, Portland, OR, USA, 2012, pp. 1087–1088.

[24] J. Jiang, Y. Ke, P. Chien, P. Cheng, Learning user reformulation behavior for query auto-completion, Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, Gold Coast, Australia, 2014, pp. 445–454.

[25] K. Massoudi, M. Tsagkias, M. de Rijke, W. Weerkamp, Incorporating query expansion and quality indicators in searching microblog posts, Advances in Information Retrieval, Springer, 2011, pp. 362–367.

[26] L. Sarmento, P. Trezentos, J.P. Gonçalves, E. Oliveira, Inferring local synonyms for improving keyword suggestion in an on-line advertisement system, Proceedings of the 3rd International Workshop on Data Mining and Audience Intelligence for Advertising (2009) 37–45.

[27] A.Z. Broder, M. Fontoura, E. Gabrilovich, A. Joshi, V. Josifovski, T. Zhang, Robust classi<sup>fi</sup>cation of rare queries using web knowledge, Proceedings of the 30th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Amsterdam, the Netherlands, 2007, pp. 231–238.

[28] H. Amiri, A. AleAhmad, M. Rahgozar, F. Oroumchian, Keyword suggestion using conceptual graph construction from wikipedia rich documents, International Conference on Information and Knowledge Engineering, California, USA, 2008.

[29] A. Joshi, R. Motwani, Keyword generation for search engine advertising, 6th IEEE International Conference on Data Mining-Workshops (ICDMW) (2006) 490–496.

[30] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, The Journal of Machine Learning Research 3 (2003) 993–1022.

[31] Grif<sup>fi</sup>ths, T. (2002). Gibbs Sampling in the Generative Model of Latent Dirichlet Allocation.

[32] F.R. Kschischang, B.J. Frey, H. Loeliger, Factor graphs and the sum-Product algorithm, IEEE Trans. Inf. Theory 47 (2) (2001) 498–519.

[33] G. Colavolpe, G. Germi, On the application of factor graphs and the sum product algorithm to ISI channels, IEEE Trans. Commun. 53 (5) (2005) 818– 825.

[34] H. Loeliger, An introduction to factor graphs, Signal Process. Mag. IEEE 21 (1) (2004) 28–41.

[35] X. Zhang, J. Feng, Cyclical bid adjustments in search-Engine advertising, Manage. Sci. 57 (9) (2011) 1703–1719.

[36] Reuters (2012). China's Alibaba to Pass Amazon, Ebay in Transaction Value: Executive. http://www.reuters.com/article/2012/09/08/net-us-alibabaidUSBRE88702J20120908.

[37] F. Can, R. Nuray, A.B. Sevdik, Automatic performance evaluation of web search engines, Inf. Process. Manage. 40 (3) (2004) 495–514.

[38] D. Zhang, Z. Yan, H. Jiang, T. Kim, A domain-Feature enhanced classi<sup>fi</sup>cation model for the detection of chinese phishing e-Business websites, Inf. Manage. 51 (7) (2014) 845–853.

[39] C. Chang, C. Lin, LIBSVM: a library for support vector machines, ACM Trans. Intell. Syst. Technol. (TIST) 2 (3) (2011) 27.

[40] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Prediction, Inference and Data Mining, second ed., Springer Verlag, New York, 2009.

[41] T. Lappas, G. Valkanas, D. Gunopulos, Ef<sup>fi</sup>cient and domain-Invariant competitor mining, Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (2012) 408–416.

[42] D.M. Powers, Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation, J. Mach. Learn. Technol. 2 (1) (2011) 37–63.

[43] N. Lathia, S. Hailes, L. Capra, X. Amatriain, Temporal diversity in recommender systems, Proceedings of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval (2010) 210–217.

Dandan Qiao is currently pursuing her PhD degree at the School of Economics and Management, Tsinghua University, Beijing, China. Her research interests include competitive intelligence, data mining, and human behavior analytics.

Jin Zhang is an assistant professor in the School of Business, Renmin University of China. He received his PhD degree in management science and engineering from the School of Economics and Management, Tsinghua University, Beijing, China, in 2013. His current research interests include data mining, business intelligence, and web search. His work has been published in journals such as INFORMS Journal on Computing, IEEE Transactions on Neural Networks and Learning Systems, Decision Support Systems, and Journal of Informetrics

Qiang Wei is an associate professor in the Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing, China. His research interests focus on information systems and management, business intelligence and data mining, fuzzy logic, database theory and applications, business modeling, as well as simulation techniques. His work has been published in international journals in the domain of information system, including Decision Sciences, INFORMS Journal on Computing, Decision Support Systems, Information Sciences, Journal of Applied Intelligence, International Journal of Approximate Reasoning, etc.

Guoqing Chen received his PhD from the Catholic University of Leuven (KU Leuven, Belgium) and presently is the Professor of Information Systems at the School of Economics and Management, Tsinghua University, Beijing, China. His research interests include business intelligence and analytics, e-business and IT-enabled innovation, fuzzy logic applications, etc. He has numerous international publications in many journals and conferences, such as Decision Sciences, INFORMS Journal on Computing, Decision Support Systems, IEEE Transactions on Fuzzy Systems, etc.
