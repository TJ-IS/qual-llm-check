---
otero_id: 21287
otero_key: "BAB5ADTM"
title: "Intelligent infomediary for web financial information"
authors: "Christopher C. Yang; Alan Chung"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00078-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Intelligent infomediary for web financial information

Christopher C. Yang\*, Alan Chung

Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong, China

Received 1 June 2001; accepted 1 March 2003 Available online 20 June 2003

## Abstract

The World Wide Web is the most popular information dissemination channel in the world. Such information space grows by an estimation of at least 10% every month. Many newspapers take the advantage to expand their services by providing real time electronic versions of news information on the Web in contrast to the traditional ‘‘ink-on-paper’’ newspapers. The timely financial news is very important for decision-making of investors. However, the tremendous amount of information releasing simultaneously creates the problem of information overloading, which reduces the decision-making capabilities significantly. As most of the investors are not experienced users of information retrieval systems, they spend extensive amount of time to identify the relevant information. Software agents act as intermediaries between the users and the information providers to notify users of recently published relevant information. In this paper, we present an intelligent agent that monitors the posting of the Web information providers and utilizes user profiles and user feedback to learn user preference and search for the Chinese Web financial information on behalf of users. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Infomediary; User profiles; Relevance feedback; Internet search engines; Intelligent agents

## 1. Introduction

The World Wide Web has become a major channel for information dissemination. It has been estimated that the amount of information on the Internet doubles every 18 months. Many traditional newspapers are also expanding their services by providing on-line news on the web. Such information on the web is updated frequently. For these reasons, information overload becomes a significant problem. Although there are search engines available on the Web, most commercial search engines take keywords as inputs and suffer in low precision and recall. Besides, users without much experience in text retrieval may also have difficulties in choosing the right keywords for their query. Given the information needs of users and a good information retrieval system, the result of retrieval may still be poor if the users do not provide a query that represents the information needs. The retrieval system may return many documents where only a few of them are relevant (i.e. low precision), if the keyword is too general. On the other hand, some other relevant documents that do not use the exact keyword will not be returned (i.e. low recall), if the keyword is too specific. Query represented by keywords is rather passive. It requires users to properly present their information needs. Intermediaries equipped with intelligent agents that are able to learn user preferences and search on behalf of the users without users taking too much effort to make the query are desired.

Personalized intermediaries are delegated to monitor the Web sites of the information providers or electronic stores and search for relevant information or products. For example, Inktomi Shopping Engine is a B2C price comparison engine and a search engine of online stores that find best price of online products and search contextual information, such as user comments and reviews of products. MySimon is an intermediary equipped with the Virtual Learning Agentk to search the best online store or the products with the best price. Junglee Shopping Guide, acquired by Amazon, uses the virtual database technology and carries more than 15 million items. Such intermediaries help to meet and match the common needs between the huge and rapidly growing consumer base and supplier base [8]. They provide physical infrastructure, economies of scale, and human interaction and transfer information about demand patterns to suppliers for improving inventory management and sharing risk [6,7]. Infomediaries, or information intermediaries, provides informational services to the clients. They create and add value for the clients during several critical phases: initial search, information or product comparison, and transaction or service delivery. Since they aggregate a large number of information providers, the infomediaries save the clients a lot of time and reduce the client’s effort in the tedious piecemeal searches. In this paper, we present a personalized infomediary that search for the timely Chinese financial information on behalf of the users based on the user profile and relevance feedback.

Internet search engines have been a hot topic since the beginning of World Wide Web. There are two major approaches of Internet search engine, online database indexing and searching, and client-based searching agents. Online database indexing and searching is the traditional approach. Systems using this approach collect complete or partial Web documents and then index these documents by keywords on the host server. Searchable interfaces are provided for users to submit their queries. For examples, Lycos,

Alta Vista, and Yahoo are using this approach. Most recent research in Web searching focuses on developing client-based intelligent searching agents to search for relevant web pages on behalf of users. TueMosaic [4], WebCrawler (purchased by American Online in 1995) [15], and Repository Based Software Engineering (RBSE) spider, investigate different conventional best first search. Smart Itsy Bitsy Spider [3,25] employs the genetic algorithm and hybrid simulated annealing for searching. Other searching agents focus on learning user preferences and recommending Web pages. WebWatcher [1], Anatagonomy [9,18], Syskill and Webert [13,14], Leitizia [10,11], and CiteSeer [5] are some prominent examples. Although several techniques have been investigated to capture the user information needs and preference from user feedbacks, there are still many shortcomings. The implicit feedbacks, such as scrolling and enlarging operations, are not necessary representing the user preferences. Many of them are not using full text for retrieval. Only anchor text and headings are used. Some of them even require users’ effort to extract keywords from the documents. In order to reduce user efforts to represent their information needs, full text analysis and automatic keywords extraction must be employed. Inaccurate implicit feedback should be avoided. In the proposed work, semantics of the documents with user feedbacks are automatically extracted and document similarity between the rated documents and newly fetched documents will be computed to improve the performance of the search engine.

In this paper, we present an intelligent infomediary for searching Chinese financial information on the Web. Such Chinese Web financial infomediary is a software agent that transforms meaningful information from Internet content providers to users. It functions as human agents, which take account of user preferences and desires and interact with users to accomplish tasks. User profiles are designed to capture the basic knowledge on user preferences, areas of interest, and reading habits. User feedback is utilized to capture more specific user preferences based on the semantics of the rated news articles. The search engine will then search for the financial news articles that users are most interested in based on the user profiles, user feedback, and the indexed news articles. Comparing to the traditional database indexing and searching approach, our system requires less effort from users to specify their query. It learns user preferences from their profiles and their daily feedback of the rated articles. In the rest of this article, Section 2 describes the system architecture and the five major modules, including fetching, indexing, user profile, relevance feedback, and search engine. Details of the algorithms will be presented in Section 3. Section 4 describes the experiment that measures the performance of the proposed system. Statistical analysis is conducted to investigate the impact of user profiles and user feedback on Chinese financial news articles.

![](/api/attachments/BAB5ADTM/fulltext/images/ed2959d576f83de029c9699d88734186debbe0c5b859428dd63f3dfcb542486c.jpg)  
Fig. 1. System architecture of the intelligent Chinese financial news retrieval system.

## 2. System architecture

The personalized infomediary system consists of five major modules: fetching, indexing, user profile, relevance feedback, and search engine. The fetching and indexing components fetch the daily financial news articles from the newspaper Web sites and index each fetched document. The user profile captures the knowledge of user preference on the financial news. The user feedback captures the semantics of the userinterested documents obtained by the search engine.

The search engine retrieves the relevant documents based on the indexing of the documents, the user profile, and the user feedback. Fig. 1 illustrates the system architecture. Further elaboration of each module is presented in the following sub-sections. The details of algorithms used in each module are presented in Section 3.

## 2.1. Fetching module

The system monitors the sources of Chinese financial news on the Web and downloads the most recent published information. The sources of the financial information that are currently monitored by our system are listed in Table 1. The number of sources is not limited and is easily expanded in our system.

Several fetching programs, such as Lynx and HtmlGobble, are available on the Web to fetch and display HTML documents (Fig. 2). In order to make our system more portable and integrate with other components, we implement a generic fetching program in Java. It takes the Universal Resource Location (URL) of the Web page and uses the Hyper Text Transfer Protocol (HTTP) to make the connection to the corresponding Web site.

<table><tr><td colspan="3">Table 1Chinese newspaper sources</td></tr><tr><td>Newspaper source</td><td></td><td>URL</td></tr><tr><td>Apple Daily Online</td><td>蘋果日報</td><td>http://www.appledaily.com.hk</td></tr><tr><td>Ming Pao Electronic News</td><td>明報</td><td>http://www.mingpao.com/newspaper</td></tr><tr><td>Oriental Daily News</td><td>東方日報</td><td>http://www.orientaldaily.com.hk</td></tr><tr><td>Hong Kong Commerce Daily</td><td>香港商報</td><td>http://www.hkcd.com.hk</td></tr><tr><td>Sing Tao Electronic Daily</td><td>星島電子日報</td><td>http://www.singtao.com</td></tr><tr><td>Ta Kung Pao</td><td>大公報</td><td>http://www.takungpao.com.hk</td></tr></table>

![](/api/attachments/BAB5ADTM/fulltext/images/bca38de39d5883da2dd6d3687b59a982e9fd7f17501612a209e090bae4e79074.jpg)  
Fig. 2. Fetching robot.

## 2.2. Chinese indexing module

A Chinese indexer recognizes and selects essence of a document and represents the document. Chinese indexing is more difficult than English indexing because Chinese text has no delimiter to mark word boundaries as English text. There are three major approaches on Chinese indexing, (a) statistical approach, (b) lexical rule-based approach, and (c) hybrid approach based on statistical and lexical information. Keywords used in financial information are usually unknown terms such as company names, product names, event names, etc. Lexical approach, which relies on dictionary, is not able to extract such unknown words. In this system, we apply the boundary detection [22 –24] based on the statistical approach. Details are presented in Section 3.1 Experimental result shows that it can extract over 90% of the unknown terms in documents. Fig. 3 depicts the Chinese indexing module.

## 2.3. User profile module

Most financial investors are not experienced users of computers or information retrieval systems. They may be knowledgeable in using the financial information to make decision in their investment; however, they may not be proficient in using the Web search engines. A search engine that requires minimum user effort in specifying their information needs is desired.

In order to obtain the information needs of the less experienced users, agents are utilized to build their profiles. User profile captures basic knowledge on user preferences, areas of interest, and reading habits. A good user profile not only increases the precision of retrieval but also narrows down retrieval scope that directly reduces processing time. Our system builds an initial profile by asking users to answer a few questions and explicitly state their preferences for filtering.

User profiles can be categorized into cognitive profiles and sociological profiles [21]. The cognitive profiles represent the user’s areas of interest based on the content of information. The sociological profiles represent the personal and organizational interrelationships of individual in a community [12]. Most of the existing systems use the cognitive profiles representing by a set of feature vectors where each element is a keyword. For example, Pazzani et al. [14] develop their Syskill and Webert’s user profile by selecting a set of informative words using an information-based approach. In our system, we focus on building a user profile that captures user preference on Chinese financial information published in Hong Kong based on cognitive profile. Therefore, we construct user profiles by (i) sources of news articles, (ii) regions of news, (iii) categories of industries, (iv) listed companies in HK stock market, and (iv) user specified keywords. In addition of using keywords to represent user’s areas of interest, we also capture the user’s preference on the information source and user’s investment profile.

![](/api/attachments/BAB5ADTM/fulltext/images/ef644314fa75dd066f6eef3fa99991f76deadb5db48650f20893ec6852474244.jpg)  
Fig. 3. Chinese indexing module.

## 2.4. User feedback module

The user profile captures the initial knowledge of user preference in general; however, the user preference on the specific content obtained from each news article is not captured. In our system, we use the user feedback to obtain additional information on user preference. Such feedback provides more specific information of users interest in news topics, events, names, and other relevant knowledge. It has been reported that user relevance feedback provides large improvement on information retrieval performance [20].

## 2.5. Search engine module

The search engine takes inputs from indexing, user profile, and user feedback. The indexing component determines the keywords for each newly fetched article. The user profile component captures the knowledge of user interest. The user feedback component records the user interest based on the content of each rated article. Based on these inputs, the search engine will rank all the fetched financial news articles on the day and report them to users. However, on day $0 ,$ the search engine has inputs from indexing and user profile only. No articles have been read and rated yet. Starting from day 1, the search engine will rank all articles based on indexing, user profile, and user feedback.

## 3. Algorithms used in the system

In this section, we describe the details of algorithms and user interfaces in each of the five modules.

## 3.1. Chinese text segmentation and indexing

In the Chinese Indexing Module, boundary detection approach is utilized to segment Chinese text. We detect the boundary of a word by determining if the value of mutual information between two adjacent Chinese characters is lower than a threshold and/or if there is any abrupt change in mutual information. Mutual information $I ( c _ { i } , c _ { j } )$ is the statistical measurement of association between two characters, $c _ { i }$ and $c _ { j } .$

Therefore, characters that are highly associated are considered to be grouped together to form words.

$$
\begin{array}{c} I (c _ {i}, c _ {j}) = \log_ {2} \left(\frac {f (c _ {i} , c _ {i}) / N}{f (c _ {i}) / N f (c _ {j}) / N}\right) \\ = \log_ {2} \left(\frac {N f (c _ {i} , c _ {i})}{f (c _ {i}) f (c _ {j})}\right) \end{array}\tag{1}
$$

where $f ( c _ { i } ) \mathrm { a n d } f ( c _ { j } )$ correspond to frequencies of $c _ { i }$ and $c _ { j } ,$ respectively, N corresponds to the total number of characters in corpus.

Before we apply the boundary detection algorithm to detect word boundaries, we remove the HTML tags of the HTML documents and use the punctuation to segment the document into strings of Chinese characters. The boundary detection algorithm will then be used to segment the strings of characters.

After word segmentation, term weighting heuristics are then computed. Term frequency, $\mathrm { t f } _ { i j } ,$ represents the numbers of occurrences of term $j$ in document i. The document frequency, $\mathrm { d f } _ { j } ,$ represents the number of documents in a collection of n documents in which the term j occurs. The combined weight of term j in a document $i , d _ { i j }$ is computed as follows:

$$
d _ {i j} = \mathrm{tf} _ {i j} \times \log \left(\frac {N}{\mathrm{df} _ {i}}\right)\tag{2}
$$

The term that occurs more frequent indicates itself as a good descriptor of the document. On the other hand, the term that occurs frequently on many documents implies itself as a general term that does not have any specific meaning. Therefore, a term, which has a high $\mathrm { t f } _ { i j }$ and low df<sub>j</sub>, corresponds to a good keyword of the documents.

## 3.2. User profiles

In the user profile module, user profile is divided into five categories: by (i) sources of news articles, (ii) regions of news, (iii) categories of industries, (iv) listed companies in HK stock market, and (iv) user specified keywords. Details of each category are as follows:

## 3.2.1. Sources of news articles $( w _ { s } )$

Different users have different preferences on the information providers. Although similar content are reported by different information providers, investors find some of the authors in some particulars newspapers more reliable and these authors’ comments are more helpful in their decision making. Therefore, these investors prefer to read articles from particular newspaper Web site in certain financial issues. Our system currently uses six newspaper sources on the Internet (Table 1). As shown in Fig. 4, users may use a slider to submit their confidence level ranged from excellent to very bad for each newspaper source.

## 3.2.2. Preference on regions of news (w<sub>r</sub>)

Since Hong Kong is an international financial center, besides local financial news, news from China and international (such as, south east Asia, Pacific region, North America, and Europe) will affect the Hong Kong stock market. In most of the newspaper sources, the financial news is categorized into three regional categories: (i) local, (ii) China, and (iii) international. For different users, news from different regions may affect their investment by different degree. The user profile of our system captures the importance of the news from different regions for each user by the user interface, as shown in Fig. 5.

## 3.2.3. Categories of industries (f<sub>i</sub>)

There are several major industries in Hong Kong. In our systems, we select 10 industries to focus on: (i)

finance, (ii) banking, (iii) real estates, (iv) technology, (v) manufacturing, (vi) services, (vii) tourism, (viii) entertainment, (ix) food and beverage, and (x) insurance. For each industry, we select a list of keywords (shown in Table 2) that are most significant in the corresponding industry. Users may select the preferred industries by checking the appropriate check box in the panel as shown in Fig. 6.

## 3.2.4. Listed companies in Hong Kong stock market

In our system, user can configure the agent to monitor news articles that are particularly related to a listed company. Our agent provides a list of company names and their stock codes in the Hong Kong Stock Exchange for users to select, as shown in the interface in Fig. 7. The first column is a checkbox for user to select the listed company. The second column is the code of the listed company. The third column is the name of the listed company.

## 3.2.5. User specified keywords (fu)

Besides the categories of industries and the listed companies, users may also specify his or her interests by supplying specific keyword. These interest terms can be person names, locations, or company names, etc. in any number of Chinese character or English words. The system provides an interface for the user to edit their keyword list in their profile (Fig. 8). Users may type keywords in the textfield and click the ‘‘Add’’ button to submit keywords to the system or select keywords in the selection menu and click the $\mathrm { ^ { 6 6 } R e _ { - } }$ move’’ button to remove the selected keywords from the system. The agent will then match the user-specified keywords with the news articles and count their frequency in each news articles. However, if user did not enter any keyword in this list, the agent will disable this function.

![](/api/attachments/BAB5ADTM/fulltext/images/2f6e83f0aa433c3d15a3ad9912727f9354c4b103b6eafcb731787ba5b223b8cd.jpg)  
Fig. 4. Preferences on sources of news articles.

![](/api/attachments/BAB5ADTM/fulltext/images/6e8664bfab757b2dedf79ca14778c33963bda0cb89a152f884e727585fa21e96.jpg)  
Fig. 5. Preference on regions of news.

## 3.2.6. User profile score $( s _ { p } )$

In order to determine the goodness of a news article in terms of the user profile, a formulation $( S _ { \mathrm { p } } )$ as shown in Eq. (3) is adopted. The User Profile Score $( S _ { \mathrm { p } } )$ is the accumulation of the relative weight scores obtained from preference on sources of newspapers, regions of news and keywords matching score obtained from categories of industries, listed companies and user-specified keywords. $w _ { \mathrm { s } }$ and $w _ { \mathrm { r } }$ are the weights of the sources of newspaper and the regions of news for a particular news article provided by the user through the user interface as shown in Figs. 4 and 5, respectively, where $0 { \leq } w _ { \mathrm { s } } , w _ { \mathrm { r } } { \leq } 1$ . The score of categories of industries and the score of listed companies and user-specified keywords are calculated by dividing the frequencies of the corresponding keywords, $f _ { i }$ and $f _ { \mathrm { u } } ,$ by their cardinalities, $C _ { i }$ and $C _ { \mathrm { u } } ,$ and multiplying to their corresponding weights, $w _ { i }$ and $w _ { { \mathbf { u } } } .$ The higher the frequencies of the selected keywords for the industries, listed companies and user-defined keywords appear in a particular news article, the more relevant the article is to the interest of the user. The frequencies are then normalized by the number of selected keywords.

List of predefined keywords in industry items

<table><tr><td>Industry</td><td>Examples of keywords</td><td></td></tr><tr><td>Real Estate 地產業Finance 金融業</td><td>單位面積樓宇 房屋住宅恆指期指 基金聯交所 股價 股票</td><td>flats, area, buildings, housing, residence HS index, index futures, funds, SEHK, stock price, stocks</td></tr><tr><td>Banking 銀行業Tourism 旅遊業Manufacturing 製造業</td><td>外匯銀行利率遊客酒店景點生產成衣製造</td><td>foreign exchange, banks, interest rates tourists, hotels, scenic points production, textile products, manufacturing</td></tr><tr><td>Technology 科技業</td><td>高科技電訊科研軟件</td><td>high technologies, telecommunication, scientific research, software</td></tr><tr><td>Food &amp; Beverage 飲食業Service 服務業Entertainment 娛樂業Insurance 保險業</td><td>酒家酒樓飲食零售外貿轉口唱片偶像藝人保險人壽保險保障</td><td>restaurants, food and beveragesretails, exports, exchange CDs, idols, actorsinsurance, life insurance, protection</td></tr></table>

![](/api/attachments/BAB5ADTM/fulltext/images/c196ca7d9fbe1edc03a75afc05c1d5f82906ea646d0d0f857954cfe1cbac1b6c.jpg)  
Fig. 6. Categories of industries.

![](/api/attachments/BAB5ADTM/fulltext/images/73fa8920a000c7e78f1332844aaf69f2bfba999cb70740521a6924446e40caf1.jpg)  
Fig. 7. Listed companies in Hong Kong stock exchange. In the interface, the first column is a checkbox for user to select the listed company; the second column is the code of the listed company; and the third column is the name of the listed company. For example, the user has selected the listed companies, Cheung Kong (Holdings) Limited (1), HSBC Holdings (5), and HKT (8). The translations of the rest of listed companies are CLP Holdings (2), HK and China Gas (3), Wharf Holdings (4), HK Electric (6), Hang Lung Group (10), Hang Seng Bank (11), and Henderson Land (12).

![](/api/attachments/BAB5ADTM/fulltext/images/6d2590465d4a733114628de00a03f8a066ddafe40ef17162b73dc5125803c5f8.jpg)  
Fig. 8. User-specified keywords. In the interface, users may type keywords in the textfield and click the $\mathrm { \ " ~ } \mathrm { A d d } ^ { \mathrm { \ : , } }$ button next to it to submit keywords to the system or select keywords in the selection menu and click the ‘‘Remove’’ button to remove the selected keywords from the system. For example, the keyword in the textfield is ‘‘Li Tzar Kai Richard’’, which is also the selected keyword on the second row of the selection menu. The keywords on the selection menu are ‘‘Cyberport’’, ‘‘Li Tzar Kai Richard’’, ‘‘Pacific Century’’, ‘‘high technology’’, ‘‘Chinese medicine’’, ‘‘HSBC Holdings PLC’’, ‘‘Hong Kong Telecommunications’’, ‘‘telecommunications’’, ‘‘HSBC’’ (from top to bottom).

$$
S _ {\mathrm{p}} = w _ {\mathrm{s}} w _ {\mathrm{r}} \left(w _ {i} \frac {\sum_ {j} f _ {i j}}{C _ {i}} + w _ {\mathrm{u}} \frac {\sum_ {j} f _ {\mathrm{u} j}}{C _ {\mathrm{u}}}\right)\tag{3}
$$

where $w _ { \mathrm { s } }$ is the weight of the sources of newspaper, $w _ { \mathrm { r } }$ is the weight of the regions of news, $w _ { j }$ is the weight of categories of industries, $f _ { i j }$ is the frequency of keyword j in categories of industries, $C _ { i }$ is the cardinality of keywords in categories of industries, $w _ { \mathbf { u } }$ is the weight of listed companies and user specified keywords, $f _ { \mathrm { u } j }$ is the frequency of keyword j in listed companies and user specified keywords, and $C _ { \mathrm { u } }$ is the cardinality of keywords in listed companies and user specified keywords.

## 3.3. Relevance feedback

In the user feedback module, relevance feedback of the retrieved document is obtained from the users. Relevance feedback (RF) is a controlled automatic process for query formulation [20]. RF is designed to produce improved query formulation following an initial retrieval operation. Documents are retrieved from a given collection based on the initial operation and then examined for relevance. Improved query formulations could then be constructed in order to retrieve additional relevant documents in the subsequent search operations. Two major methods, vector processing methods [17,19] and probabilistic feedback methods [16,26], are the typical methods being used in RF.

![](/api/attachments/BAB5ADTM/fulltext/images/401edc067c765d545ccda62124ce280836895df4d4c47d4a67c55a2b384b599b.jpg)  
Fig. 9. User relevance feedback Window.

In the vector processing methods, both the collection of documents and queries are represented as tdimensional vector, $\pmb { D } \mathrm { = } \{ d _ { 1 } , ~ d _ { 2 } , ~ . ~ . ~ . , ~ d _ { t } \}$ and $Q \mathrm { = } \{ \boldsymbol { q } _ { 1 }$ 2 $q _ { 2 } , . . . , q _ { \mathrm { t } } \}$ , respectively. The inner product between Q and D is typically used as the similarity measure. After effective feedback, the query will be modified as a summation over the previous query, known as relevant and non-relevant documents. In the probabilistic feedback methods, ranking of documents is based on the probabilities of a vector representation given a relevant or irrelevant item. In this paper, we use the Jaccard’s similarity function to measure the relevance of the recently fetched documents and the documents with user feedbacks of degrees of relevance.

After reading the ranked articles by our system, users may provide feedback to our agent by rating the relevance of the articles. The interface for such feedback is shown in Fig. 9. The feedback will then be used in the learning mechanism, which is based on the latent semantic structures of the news articles and the past accessed history.

We measure the relevance of a newly fetched news article based on the latent semantic structure in terms of the usage of words across documents. If two documents are similar in content, the usage of words between these two documents should be similar. Many statistical techniques have been used to estimate this latent structure. In our system, we adopt the Jaccard’s similarity function [3,25] to measure the similarity between the financial news articles that has been rated by user in the previous days and the newly fetched financial news articles. The Jaccard’s score between two news articles, A and B, is computed as follows:

$$
J (\mathrm{A}, \mathrm{B}) = \frac {\sum_ {j = 1} ^ {L} d _ {\mathrm{Aj}} d _ {\mathrm{Bj}}}{\sum_ {j = 1} ^ {L} d _ {\mathrm{Aj}} ^ {2} + \sum_ {j = 1} ^ {L} d _ {\mathrm{Bj}} ^ {2} - \sum_ {j = 1} ^ {L} d _ {\mathrm{Aj}} d _ {\mathrm{Bj}}}\tag{4}
$$

where $d _ { \mathrm { A } j }$ and $d _ { \mathrm { B } j }$ are the combined weights of term j in article A and the combined weight of term j in article B, respectively, based on the term frequency and inverse document frequency

![](/api/attachments/BAB5ADTM/fulltext/images/40c37af5e549b70113c24d62eeeeed86c6028413de9418b710ebfe60a37580a5.jpg)  
Fig. 10. Window for adjusting the weightings on user profile and semantic measurement.

$$
d _ {\mathrm{A} j} = \operatorname{tf} _ {\mathrm{A} j} \times \log (N / \mathrm{df} _ {j})
$$

$$
d _ {\mathrm{B} j} = \operatorname{tf} _ {\mathrm{B} j} \times \log (N / \mathrm{df} _ {j})
$$

N is the total number of news article fetched L is the total number of keywords.

The combined weights, $d _ { \mathrm { A } j }$ and $d _ { \mathrm { B } j } ,$ are computed in terms of the term frequency and inverse document frequency to measure the significance of keyword j in article A and B, respectively. If the keyword frequency is high, the keyword is representative for the article. However, if the document frequency is high, the keyword is too general.

The rating score of newly fetched articles by our agent also relies on the rating score on each rated article in user feedback. In other words, if user provides a high rating for an article in user relevance feedback, he/she finds this article interesting and likes to receive more news articles with similar content. Therefore, the semantic relevance score, $S _ { \mathrm { s } } ,$ is computed as follows:

$$
S _ {\mathrm{s}} = \sum_ {i = 0} ^ {n} w _ {\mathrm{B}} \times J (\mathrm{A}, \mathrm{B} _ {i})\tag{5}
$$

where $w _ { \mathrm { B } i }$ is the rating of article $\mathrm { B } _ { i }$ by user, $J ( \mathrm { A } , \mathrm { B } _ { i } )$ is the Jaccard’s score between the newly fetched article A and the rated article $\mathrm { B } _ { i } , n$ is the total number of articles that have been rated.

![](/api/attachments/BAB5ADTM/fulltext/images/38b57353a0b06bb2f0e312252a541ecba416893e214c1ab013d45073f29d0b3c.jpg)  
Fig. 11. Result of ranked financial news on a particular day. In the interface, the first column is the ranking of the retrieved document. The second column is the score of the document. The third column is the title of the document in Chinese. The forth column is the News source in Chinese. The fifth column is the date of the document (year, month, day). The sixth column is a checkbox for user to select the document to be a cue for the retrieval of news articles on the next day. For example, on the first row, the document is ‘‘Beautiful Scenery at the Gold Coast Yacht Club’’ from singtao.com. The rest of the retrieved articles are all related to the real estates market.

## 3.4. Ranking by search engine

For each fetched article, the search engine compute a score based on the user profile score, $S _ { \mathrm { p } } ,$ , and the semantic relevance score, $S _ { \mathrm { s } } ,$ as follows:

$$
S = w _ {\mathrm{p}} S _ {\mathrm{p}} + w _ {\mathrm{s}} S _ {\mathrm{s}}\tag{6}
$$

where $w _ { \mathrm { p } }$ is the weighting of user profile score, $w _ { \mathrm { s } }$ is the weighting of semantic relevance score, $S _ { \mathrm { p } }$ is the normalized user profile score, $S _ { \mathrm { s } }$ is the normalized semantic relevance score.

The default values of $w _ { \mathfrak { p } }$ and $w _ { \mathrm { s } }$ are 0.5; however, users are allowed to set their values by the interface shown in Fig. 10.

The search engine ranks the daily fetched news article based on the score computed by Eq. (6). Fig. 11 shows the result of the ranked financial news articles on a particular day. In the interface, the first column is the ranking of the retrieved document. The second column is the score of the document. The third column is the title of the document in Chinese. When users click on a news title, a news browser will pop up and display the article. The forth column is the News source in Chinese. The fifth column is the date of the document (year, month, day). The sixth column is a checkbox for user to select the document to be a cue for the retrieval of news articles on the next day. A check box next to the news article indicates if the users have read and rated the article. If users prefer not to use such article to be a cue for the retrieval of news article on the next day, they can simply remove the check in the box.

## 4. Experiment

We have conducted an experiment, aimed at examining the following issues.

Issue 1: the impact of using user profiles and user feedback on Chinese financial news articles retrieval separately.

Issue 2: the impact of combining user profiles and user feedback on Chinese financial news articles retrieval. Does it produce better performance than applying user profiles or user feedback only?

We are interested to compare the performance of applying user profiles and applying user feedback on the infomediary. User profiles capture the basic knowledge of user preferences but user feedback learns the user preferences through interaction with the users. Using user profiles, information retrieval on each day is performed independently although users may update their profiles any time. However, using user feedback, the knowledge of user preferences is accumulated. We are also interested to see if the combination of user profiles and user feedback can improve the overall performance.

The experiment is a user evaluation involving 50 subjects, 20 subjects from the University of Hong Kong and 30 subjects from the Chinese University of Hong Kong. Each subject is asked to provide his/her user profile and/or feedback and use the system for 5 consecutive days. Approximately, 170 news articles from the six sources of newspapers are fetched everyday. Twenty top ranked news articles are returned on each day based on the input submitted by users, each subject is asked to provide feedback to each of the retrieved news articles. An article is considered relevant if the feedback for the article is ‘‘Good’’ or ‘‘Excellent’’ as shown in Fig. 9. The performance is measured by precision [2,3] of retrieval. Precision is the fraction of the retrieved documents that is relevant, which is computed as follows:

$$
\text { Precision } = \frac {\# \text { of   news   articles   retrieved   by   the   system   that   are   relevant }}{\# \text { of   news   articles   retrieved   by   the   system }}\tag{7}
$$

To compare the performance of user profiles, user feedback, and combination of two, three setups were used. In the first setup (Setup 1), subjects only provide their user profiles, but the feedback of the ranked articles are not submitted. In the second setup (Setup 2), subjects only provide the ratings of the daily ranked articles, but the initial user profiles are not recorded. In the third setup (Setup 3), subjects provide both user profile and user feedback. Table 3 shows the average precision obtained by the three setups over five consecutive days. The comparisons of the average precision of three setups on each day are also presented in Fig. 12.

The result shows that combining both user profiles and user feedback obtains the best performance. Using only user profiles has very close precision on each day with the difference between the maximum precision and minimum precision as 0.03. However, using only user feedback has consistent improvement in precision on each consecutive day, increasing from 0.28 to 0.66.

Table 3  
Average and standard deviation of precision for three setups on five consecutive days

<table><tr><td></td><td>Day 0 average(standard deviation)</td><td>Day 1 average(standard deviation)</td><td>Day 2 average(standard deviation)</td><td>Day 3 average(standard deviation)</td><td>Day 4 average(standard deviation)</td></tr><tr><td>User Profiles</td><td>0.43 (0.1014)</td><td>0.45 (0.1330)</td><td>0.45 (0.1037)</td><td>0.42 (0.0970)</td><td>0.44 (0.1092)</td></tr><tr><td>User feedback</td><td>0.28 (0.1719)</td><td>0.42 (0.1884)</td><td>0.54 (0.1923)</td><td>0.65 (0.2142)</td><td>0.66 (0.2169)</td></tr><tr><td>User profiles +user feedback</td><td>0.43 (0.1014)</td><td>0.54 (0.1256)</td><td>0.65 (0.1631)</td><td>0.67 (0.1797)</td><td>0.66 (0.2247)</td></tr></table>

Number of subjects = 50.

On the first 2 days, using only user profiles has better performance than using only user feedback. However, on the last 3 days, using only user profiles has poorer performance than using only user feedback. Combining both user profiles and user feedback produces the best performance on each day. Similar to using only user feedback, the precision of combining both is increasing on each consecutive day. The precision of combining both is the same as the precision of using only user profiles on day 0. It is because the input on day 0 is only the user profiles even if we are combining both user profiles and user feedback.

We have conducted a two-way analysis of variance (ANOVA) to identify if there are any significant effects of the factors, setups and days, and their interaction. As shown on Table 4, all the p-values are 0.000. The results highlight that each of the main factors has a significant effect on the performance of the infomediary. In addition, a significant positive interaction effect occurred between the two independent factors on the performance.

In order to determine if the factor of consecutive days has effect on the performance of the infomediary for each of the setups, we conduct the ANOVA tests for each of the setups. Table 5 shows the ANOVA results of each setup over the 5 consecutive days. The p-values for the three setups, user profiles (Setup 1), user feedback (Setup 2), and combination of both (Setup 3), are 0.6215, 0.000, and 0.000, respectively. There is no significant difference in the performance over the 5 consecutive days using user profiles (Setup 1) for retrieving financial information. However, there are significant differences in the performance using user feedback (Setup 2) or the combination of user profiles and user feedbacks (Setup 3). Based on this observation, the user feedback makes significant improvement on the performance of retrieving financial information. However, simply using the user profiles does not make any significant changes on the performance over the 5 consecutive days. The continued interaction between the user and the system allows the system to learn more about the user preferences and search on behalf of the users.

![](/api/attachments/BAB5ADTM/fulltext/images/4ca3d6509da55b5aceeafab7eebb05022d11434241ca4e346fe3167717348acf.jpg)  
Fig. 12. Average precision of Setup 1, Setup 2, and Setup 3 on 5 consecutive days.

Table 4  
Two-way ANOVA examining the effects of setups and days, and their interaction

<table><tr><td></td><td>Degree of freedom (df)</td><td>Mean sum of squares (MSS)</td><td>F</td><td>p-value</td></tr><tr><td>Effect: setups</td><td>2</td><td>0.6992</td><td>26.187</td><td>0.000*</td></tr><tr><td>Effect: days</td><td>4</td><td>1.6778</td><td>62.839</td><td>0.000*</td></tr><tr><td>Interaction effect</td><td>8</td><td>0.7892</td><td>29.071</td><td>0.000*</td></tr><tr><td>Within</td><td>735</td><td>0.0267</td><td></td><td></td></tr></table>

Number of subjects: 50.  
\* Significant at $\begin{array} { r } { p < 0 . 0 0 1 . } \end{array}$

To better understand the significance of improvement between the consecutive days, we conduct ANOVA between each pair of successive days from day 0 to day 5 for Setup 2 and Setup 3. Table 6 shows the p-values of ANOVA and the computation of the pvalues can be found in Table A.1 in Appendix A. For Setup 2, the difference between day 0 and day 1, between day 1 and day 2, and between day 2 and day 3 are significant at the significant level of 0.001, 0.005, and 0.05, respectively. However, there is no significant difference between day 3 and day 4. For Setup 3, the difference between day 0 and day 1 and between day 1 and day 2 are significant at the significant level of 0.0005. However, there is no significant difference between day 2 and day 3 and between day 3 and day 4. Based on these observations, we find that there are significance improvements from day 0 to day 3 when only user feedback is applied, but the significance level decreases. There are also significant improvements from day 0 to day 2 when both user profiles and user feedback are applied. We also observe that either using only user feedback or using both user profiles and user feedback will reach an optimal performance after a few days of improvements (3 days for Setup 2 and 2 days for Setup 3). Even if we continue to provide user feedback on the consecutive days, it does not increase the precision any higher than the optimal precision ( f 0.67). The optimal precision is the maximum performance of the system. Unless more news articles are collected from the information providers or the mechanism of the search engines is improved, it may not be able to get better performance than the current maximum performance. From the ANOVA, it shows that the user feedback improves the retrieval performance significantly on each consecutive day starting from the first day until it reaches the optimal precision. The effectiveness of learning user preference based user feedback is impressive. Given the user profile, Setup 3 is able to reach the optimal performance earlier than Setup 2. In addition, the user preferences may change from time to time, if the system does not continue to learn the user preference and capture the changes in user preference, the precision on the consecutive days may decrease. However, there is not any decrease in precision observed in the results of Setup 2 and Setup 3.

Table 5  
ANOVA of each of three setups on five consecutive days

<table><tr><td></td><td>Degree of freedom (df)</td><td>Mean sum of squares (MSS)</td><td>F</td><td>p-value</td></tr><tr><td colspan="5">Setup 1: User Profiles</td></tr><tr><td>Between 5 days</td><td>4</td><td>0.008069</td><td>0.6584</td><td>0.6215</td></tr><tr><td>Within days</td><td>245</td><td>0.012257</td><td></td><td></td></tr><tr><td colspan="5">Setup 2: User Feedback</td></tr><tr><td>Between 5 days</td><td>4</td><td>1.1427</td><td>28.7221</td><td>0.000*</td></tr><tr><td>Within days</td><td>245</td><td>0.0398</td><td></td><td></td></tr><tr><td colspan="5">Setup 3: User Profiles + User Feedback</td></tr><tr><td>Between 5 days</td><td>4</td><td>0.5508</td><td>19.9265</td><td>0.000*</td></tr><tr><td>Within days</td><td>245</td><td>0.02764</td><td></td><td></td></tr></table>

Number of subjects: 50.  
\* Significant at p < 0.001.

Table 6  
p-value of ANOVA for setup 2 and setup 3 between each consecutive days

<table><tr><td></td><td>Between day 0 and day 1</td><td>Between day 1 and day 2</td><td>Between day 2 and day 3</td><td>Between day 3 and day 4</td></tr><tr><td>Setup 2</td><td>0.000*</td><td>0.003016**</td><td>0.04137***</td><td>0.714083</td></tr><tr><td>Setup 3</td><td>0.000*</td><td>0.000*</td><td>0.508657</td><td>0.980643</td></tr></table>

Number of subjects: 50.  
\* Significant at $p { < } 0 . 0 0 1$  
\*\* Significant at $\begin{array} { r } { p < 0 . 0 0 5 . } \end{array}$  
\*\*\* Significant at $\begin{array} { r } { p < 0 . 0 5 . } \end{array}$

As a conclusion, the user profiles help to provide initial knowledge of user preference to obtain a reasonable precision for retrieval of financial information. However, the learning power of user profile is limited because it only captures the general information of user preference. It cannot learn the user preference continuously and the performance of retrieval cannot be improved from time to time. The user feedback helps to learn specific user preference based on the continuous interaction with users. The learning of user preference is effective for user feedback. Interaction on each day will improve the retrieval performance significantly until it reaches the optimal performance. Combining both user profile and user feedback takes the advantage of both to learn the general information and specific information of user performance. Therefore, it has the best performance among the three setups.

## 5. Conclusion

Intelligent infomediary is important as the problem of information overloading becomes more and more serious on the World Wide Web. Such intermediaries provide users with more efficient and effective information retrieval to support their decision-making. In this paper, we develop a system utilizing user feedback and user profiles to learn the user preferences so thathigher precision of information retrieval can be achieved. User profiles capture the general knowledge of user preferences based on sources of news articles, regions of news reported, categories of industries related, listed companies in HK stock market, and user specified keywords. User feedback captures the semantics of the user-rated news articles to obtain specific information of user performance. The search engine searches for the Web news articles based on the user preferences and indexing on behalf of users. We have conducted an experiment to compare the performance of retrieval based on different setups of user profiles and user feedback. It shows that user profiles only capture the general information of user preference but it does not help in improving the retrieval performances continuously. User feedback helps in improving the retrieval performances continuously. It continues to learn the user preference and the changes of user preference. The optimal precision is reached after a few days of learning. Combining both user profiles and user feedback captures the general information and specific information of user preference and produces the best performance. In the future research, we shall develop a collaborative support of Web retrieval. Users with similar user profiles are grouped together and the user feedback of the similar users can support each other’s information searching.

## Acknowledgements

This project is supported by the Direct Research Grant of the Chinese University of Hong Kong, 2050239.

## Appendix A

Table A.1 ANOVA of the Second and Third Setups between the Consecutive Days

<table><tr><td></td><td>Degree of freedom (df)</td><td>Mean sum of squares (MSS)</td><td>F</td><td>p-value</td></tr><tr><td colspan="5">Setup 2: User Feedback</td></tr><tr><td>Between day 0 and day 1</td><td>1</td><td>0.5112</td><td>15.4047</td><td>0.000</td></tr><tr><td>Within days</td><td>98</td><td>0.03319</td><td></td><td></td></tr><tr><td>Between day 1 and day 2</td><td>1</td><td>0.3422</td><td>9.2538</td><td>0.003016</td></tr><tr><td>Within days</td><td>98</td><td>0.03698</td><td></td><td></td></tr><tr><td>Between day 2 and day 3</td><td>1</td><td>0.1806</td><td>4.2727</td><td>0.04137</td></tr><tr><td>Within days</td><td>98</td><td>0.04227</td><td></td><td></td></tr><tr><td>Between day 3 and day 4</td><td>1</td><td>0.0064</td><td>0.1350</td><td>0.714083</td></tr><tr><td>Within days</td><td>98</td><td>0.04740</td><td></td><td></td></tr><tr><td colspan="5">Setup 3: User Profiles + User Feedback</td></tr><tr><td>Between day 0 and day 1</td><td>1</td><td>0.3025</td><td>22.7595</td><td>0.000</td></tr><tr><td>Within days</td><td>98</td><td>0.01329</td><td></td><td></td></tr><tr><td>Between day 1 and day 2</td><td>1</td><td>0.2873</td><td>13.2922</td><td>0.000</td></tr><tr><td>Within days</td><td>98</td><td>0.02161</td><td></td><td></td></tr><tr><td>Between day 2 and day 3</td><td>1</td><td>0.01323</td><td>0.4405</td><td>0.508657</td></tr><tr><td>Within days</td><td>98</td><td>0.03005</td><td></td><td></td></tr><tr><td>Between day 3 and day 4</td><td>1</td><td> $2.5 \times 10^{-05}$ </td><td>0.000592</td><td>0.980643</td></tr><tr><td>Within days</td><td>98</td><td>0.04225</td><td></td><td></td></tr></table>

Number of subjects: 50.

## References

[1] R. Armstrong, D. Freitage, T. Joachims, T. Mitchell, et al., Web-Watcher: a learning apprentice for the world wide web, AAAI 1995 Spring Symposium Information Gathering from Heterogeneous, Distributed Environments, Menlo Park, CA, 1995.

[2] R. Baeza-Yates, B. Ribeiro-Neto, Retrieval Evaluation, Modern Information Retrieval, Addison Wesley, England, UK, 1999, pp. 73– 97, Chapter 3.

[3] H. Chen, Y. Chung, M. Ramsey, C.C. Yang, A smart itsy bitsy spider for the web, Journal of the American Society for Information Science 49 (7) (1998 May 15) 604 – 618.

[4] P. DeBra, R. Post, Information retrieval in the world wide web: making client-based searching feasible. Proceedings of the First International World Wide Web Conference, Geneva, Switzerland, 1994.

[5] C.L. Giles, K.D. Bollacker, S. Lawrence, CiteSeer: an automatic citation indexing system, Proceedings of the Third ACM Conference on Digital Libraries, New York, ACM Press, New York, NY, USA, 1998, pp. 89 – 98.

[6] V. Grover, P. Ramanlal, Six myths of information and markets: information technology networks, electronic commerce, and the battle for consumer surplus, MIS Quarterly 23 (4) (1999) 465– 495.

[7] V. Grover, J.T.C. Teng, E-commerce and the information market, Communications of the ACM 44 (4) (2001 April) 79 – 86.

[8] J. Hagel, J. Singer, Net Worth, Harvard Business School Press, Boston, 1999.

[9] T. Kamba, H. Sakagami, Y. Koseki, Anatagonomy: a personalized newspaper on the world wide web, International Journal of Human-Computer Studies 46 (6) (1997 June) 789–803.

[10] H. Lieberman, Letizia: an agent that assists web browsing, Proceedings of the 14th International Joint Conference on Artificial Intelligence, Montreal, August, 1995.

[11] H. Lieberman, Autonomous interface agents, Proceedings of the ACM Conference on Computers and Human Interface, CHI-97, Atlanta, Georgia, March, 1997.

[12] T. Malone, K. Grant, F. Turbak, S. Brobst, M. Cohen, Intelligent information sharing systems, Communications of the ACM 30 (5) (1987) 390–402.

[13] M. Pazzani, D. Billsus, Learning and revising user profiles: the identification of interesting web sites, Machine Learning, vol. 27, Kluwer Academic Publishing, Dorrdrecht, The Netherlands, 1997, pp. 313– 331.

[14] M. Pazzani, J. Muramatsr, D. Billsus, Syskill and Webert: identifying interesting web sites, Proceedings of the National Conference on Artificial Intelligence, Portland, OR, MIT Press, Cambridge, MA, USA, 1997, pp. 54 – 61.

[15] B. Pinkerton, Finding what people want: experiences with the WebCrawler, Proceedings of the Second International World Wide Web Conference, Chicago, IL, October 17 – 20, 1994.

[16] S.E. Robertson, C.J. van Rijsbergen, M.F. Porter, Probabilistic Models of Indexing and Searching, Information Retrieval Research, Butterworths, London, 1981, pp. 35 – 56.

[17] J.J. Rocchio Jr., Relevance Feedback in Information Retrieval, The Smart System-Experiments in Automatic Document Processing, Prentice Hall, Englewood Cliffs, NJ, pp. 313 – 323.

[18] H. Sakagami, T. Kamba, Learning personal preferences on online newspaper articles from user behaviors, Sixth International on World Wide Web Conference, Santa Clara, California, USA, April 7 – 11, 1997.

[19] G. Saltion, Relevance Feedback and the Optimization of Retrieval Effectiveness, The Smart System-Experiments in Au

tomatic Document Processing, Prentice Hall, Englewood Cliffs, NJ, pp. 324–336.

[20] G. Salton, C. Buckley, Improving retrieval performance by relevance feedback, Journal of the American Society for Information Science 41 (4) (1990) 288– 297.

[21] B. Shapira, P. Shoval, U. Hanani, Experimentation with an information filtering system that combines cognitive and sociological filtering integrated with user stereotypes, Decision Support Systems 27 (1 – 2) (1999) 5 – 24.

[22] C.C. Yang, A. Chung, Intelligent agents for retrieving Chinese web financial news, Proceedings of the International Conference on Information Systems, Brisbane, Australia, December 10–13, AIS, Atlanta, Georgia, USA, 2000, pp. 288– 301.

[23] C.C. Yang, J. Yen, S.K. Yung, A. Chung, Chinese indexing with mutual information, Proceedings of the First Asia Digital Library Workshop, Hong Kong, August 6 – 7, 1998.

[24] C.C. Yang, J.W.K. Luk, S.K. Yung, J. Yen, Combination and boundary detection approaches on Chinese indexing, Journal of the American Society for Information Science 51 (4) (2000) 340 – 351.

[25] C.C. Yang, J. Yen, H. Chen, Intelligent internet searching agent based on hybrid simulated annealing, Decision Support Systems, Special Issue on Intelligent Agents and Digital Community 28 (3) (2000 May) 269 – 277.

[26] C.T. Yu, C. Buckley, K. Lam, G. Salton, A generalized term dependence model in information retrieval, Information Technology: Research and Development 2 (1983) 129 – 154.

![](/api/attachments/BAB5ADTM/fulltext/images/72ed757c18ca0a14fa6763325529fb75ecf8b9f6015285c88a119cd56118e9d1.jpg)

Christopher C. Yang is currently an associate professor in the Department of Systems Engineering and Engineering Management at the Chinese University. From 1997 to 1999, he was an assistant professor in the Department of Computer Science and Information Systems and associate director of the Authorized Academic Java<sup>SM</sup> Campus<sup>SM</sup> at the University of Hong Kong. He received his BS, MS, and PhD in Electrical and Computer Engineering from the University

of Arizona, Tucson, in 1990, 1992, and 1997, respectively. From 1995 to 1997, he was a research scientist in the Artificial Intelligence Laboratory in the Department of Management Information Systems, where he was an active researcher in the Illinois Digital Library project. From 1992 to 1997, he was also a research associate in the Intelligent Systems Laboratory in the Department of Electrical and Computer Engineering. His current research interests are digital library, information visualization, Internet agent, cross-lingual information retrieval, and color image retrieval. He has published over 80 refereed journal and conference papers. He has served as a guest editor for the Journal of the American Society for Information Science and Technology. He was the chairman of Association for Computing Machinery Hong Kong Chapter and the program co-chair of the First International Conference of Asia Digital Library.

Alan Chung received his BS and M.Phil. in Computer Science and Information Systems at the University of Hong Kong in 1997 and 2000, respectively. He is currently with PricewaterhouseCoopers.
