---
otero_id: 7034
otero_key: "E2992NUJ"
title: "WNavis: Navigating Wikipedia semantically with an SNA-based summarization technique"
authors: "I-Chin Wu; Yi-Sheng Lin"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# WNavi<sup>s</sup>: Navigating Wikipedia semantically with an SNA-based summarization technique

I-Chin Wu ⁎, Yi-Sheng Lin

Department of Information Management, Fu Jen Catholic University, 510 Chung Cheng Rd, Xinzhuang Dist, Xinbei City 24205, Taiwan

## a r t i c l e i n f o

Article history: Received 7 August 2011 Received in revised form 6 February 2012 Accepted 5 April 2012 Available online 16 April 2012

Keywords: Navigation Normalized Google distance Semantics-based SNA-based summary Wikipedia

## a b s t r a c t

Link-based applications like Wikipedia are becoming increasingly popular because they provide users with an ef<sup>fi</sup>cient way to <sup>fi</sup>nd needed knowledge, such as searching for de<sup>fi</sup>nitions and information about a particular topic, and exploring articles on related topics. This work introduces a semantics-based navigation application called WNavi<sup>s</sup>, to facilitate information-seeking activities in internal link-based websites in Wikipedia. WNavi<sup>s</sup> is based on the theories and techniques of link mining, semantic relatedness analysis and text summarization. Our goal is to develop an application that helps users <sup>fi</sup>nd related articles for a seed query (topic) easily and then quickly check the content of articles to explore a new concept or topic in Wikipedia. Technically, we construct a preliminary topic network by analyzing the internal links of Wikipedia and applying the normalized Google distance algorithm to quantify the strength of the semantic relationships between articles via key terms. Because not all the content of articles in Wikipedia is relevant to users' information needs, it is desirable to locate speci<sup>fi</sup>c information for users and enable them to quickly explore and read topic-related articles. Accordingly, we propose an SNA-based single and multiple-document summarization technique that can extract meaningful sentences from articles. We applied a number of intrinsic and extrinsic evaluation methods to demonstrate the ef<sup>fi</sup>cacy of the summarization techniques in terms of precision, and recall. The results suggest that the proposed summarization technique is effective. Our <sup>fi</sup>ndings have implications for the design of a navigation tool that can help users explore related articles in Wikipedia quickly.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

With the ubiquity of Web 2.0 technologies, the World Wide Web (WWW) has become the main source of information and knowledge for countless people in the modern era. According to Alexa Traf<sup>fi</sup>c Rank, the top ten sites on the Web are Google, Facebook, YouTube, Yahoo!, Blogger, Baidu, Wikipedia, Windows Live, Twitter, and QQ.COM (July, 2011). Wikipedia, the most popular web-based, freecontent encyclopedia, is one of the best examples of crowdsourcing systems, which gather like-minded users into groups to collaborate and create long-lasting artifacts that bene<sup>fi</sup>t the whole community [2,13]. The statistical data for Wikipedia shows that, in 2008, the site welcomed 684 million visitors; and over 91,000 contributors worked on more than 16 million articles in 270 languages. Because of the popularity of collaborative peer production systems like Wikipedia, the number of articles is constantly expanding. Hence, an increasing number of people regard Wikipedia as an ef<sup>fi</sup>cient way to <sup>fi</sup>nd needed knowledge, such as searching for de<sup>fi</sup>nitions and information about a particular topic, and exploring articles on related topics. Basically, users browse Wikipedia content in the traditional manner (i.e., by following hyperlinks) when searching for information. However, users may unconsciously change their search goals or get lost when exploring or retrieving information in Wikipedia. To make searching more ef<sup>fi</sup>cient for the vast number of Wikipedia users, more effective search and navigation tools must be developed

Generally, users invest a great deal of time in browsing, i.e., following links or searching for speci<sup>fi</sup>c information. Because of the rapid growth in the volume of information on the WWW, web mining and information retrieval are regarded as key techniques for <sup>fi</sup>nding desired information. Web mining tries to extract potentially useful implicit information, link structures and patterns from information units or activities on the WWW. There are three types of web mining techniques: web content mining, web structure mining, and web usage mining. The main difference between web pages and static text documents is that the former contain content as well as link information, and metadata [1,8,28]. Web content mining exploits information retrieval (IR) and arti<sup>fi</sup>cial intelligence (AI) techniques to mine and analyze information from web pages. Generally, web content mining strategies can be divided into those that mine information or knowledge implicitly from documents, and those designed to improve the search results, i.e., the information retrieved by search engines. IR technology relies primarily on content analysis techniques, but Web pages are usually noisy and contain various types of content, such as text, images, and multimedia. To resolve this problem, some researchers have exploited the hyperlink structure, which provides hyperlink information for a collection of web pages, and proposed ranking algorithms to rank search results. Analyzing the hyperlink structure between WWW pages to support user search activities has attracted a great deal of attention in recent years.

Since the link structure encodes a considerable number of latent human judgments, link mining and analysis techniques are employed by commercial search engines, e.g., the PageRank algorithm [6,34] used by the Google search engine is one of the most well-known linkbased algorithms. Currently, PageRank is the dominant link analysis model for web searches, partly because it does not depend on search queries. It is a query-independent measure of the static ranking of web pages, and is based on the measure of prestige used in social networks. Kleinberg [26] proposed the Hypertext Induced Topic Search (HITS) algorithm, which analyzes the link topology to <sup>fi</sup>nd “hub” and “authority” pages. A hub is a page with several out-links, while an authoritative page contains several in-links. The algorithm analyzes both in-links and out-links to obtain two ranking scores for pages based on the user's query result. It analyzes the relationships between web pages and then ranks the search results accordingly. Almpanidis and Kotropoulos [1] proposed a topical information resource discovery algorithm that applies a focused or topic-driven crawler by combining text and link analysis techniques. Their results show that, in the initial stage, the content-based and link-based algorithm does not need a lot of data, and it outperforms comparable methods. In this work, we show that it is ef<sup>fi</sup>cient to analyze the articles related to a topic based on the link relationships between them without employing tedious content analysis techniques.

In Wikipedia, a topic may be linked to many articles, so it is sometimes dif<sup>fi</sup>cult for users to locate articles relevant to their particular interest simply by following the given hyperlinks. To address this problem, we propose a semantics-based navigation system that is based on the theories and techniques of link mining, semantic relatedness analysis and social network analysis (SNA). Wu and Wu [45] propose a link strength (LS) measure that establishes a network by analyzing the internal links between articles in Wikipedia; however, some irrelevant articles are included in the network. Accordingly, we utilize the normalized Google distance algorithm [10] to quantify the strength of the semantic relationships between articles via key terms, and <sup>fi</sup>lter out articles that do not have strong relationships. We also propose a hybrid measure, i.e., an internal link-based semantic topic network analysis measure, to construct a topic network with stronger semantic relationships. Our preliminary evaluation results demonstrate the effectiveness of applying semantic analysis in an internal link-based network. To help users search for information, we apply centrality-based and cohesive measures in SNA to summarize single and multiple articles. The measures are degree centrality and k-clique, which identify, respectively, the hub article and the subtopics of the seed query for further summarization of multiple articles. When the user clicks on a topic node that he/she wants to explore, an SNA-based summary is presented on the interface. Then, intrinsic and extrinsic methods are used to evaluate the quality of the summarization results. The intrinsic method, measures the quality of a system's text summarization; while the extrinsic method gives classi<sup>fi</sup>cation tasks to users so that they can evaluate the quality of the text summarization results based on the task's performance. To visualize the semantics-based topic network more efficiently. we use the software libraries provided by the Java Universal Network/Graph (JUNG) Framework to create a June-based application called Semantics-based WNavi<sup>s</sup>. Finally, an interface is generated to help users navigate Wikipedia effectively. The contributions of this work are as follows.

1. We designed a navigation support application, the semantics-based WNavi<sup>s</sup>, for Wikipedia, which is an internal link-based website. In addition, we developed associated tools, such as a topic network and topic summaries, to help users explore topics of interest.

2. We apply a series of intrinsic and extrinsic evaluation methods to con<sup>fi</sup>rm the effectiveness of the proposed SNA-based summarization technique. Furthermore, we simulate search tasks to evaluate the quality of multi-article summarization.

3. The techniques proposed in this work can be generalized to applications of navigation support tools in internal link-based knowledge intensive websites, e.g., user-generated encyclopedias and articles in technical forums, to help users gain an overview of topics and explore articles ef<sup>fi</sup>ciently. Moreover, the visualization navigation support application may help users obtain topic knowledge.

The remainder of this paper is organized as follows. The next section reviews some basic concepts and text summarization techniques. In Section 3, we describe the system framework. In Section 4, we incorporate semantic analysis techniques into an internal link-based network; and in Section 5, we discuss SNA-based summaries in Wikipedia. Sections 6 and 7 focus on the evaluation metrics and results; and Section 8 contains some concluding remarks.

## 2. Basic concepts

2.1. Semantic relatedness analysis: normalized Google distance algorithm

People acquire the meaning of a word and its relations to other words based on their background knowledge. By contrast, it is dif<sup>fi</sup>- cult for computers to make judgments about the semantic relationships between keywords. As a result, enabling computers to extract the meanings of words automatically has motivated a great deal of research in the <sup>fi</sup>elds of natural language processing and arti<sup>fi</sup>cial intelligence [10,32].

Basically, three measures are used to estimate the semantic relatedness of words, namely, thesaurus-based, corpus-based and Wikipedia-based measures [15]. Most research methods rely on long-term and labor-intensive techniques to construct the semantic relationships between words. However, Cilibrasi and Vitányi [10,11] proposed an automatic algorithm, called the normalized Google distance (NGD) algorithm, which exploits the search result counts of the Google search engine to determine such relationships. According to a report published by WorldWideWebSize.com, the Google search engine had indexed 23.6 billion web pages by December, 2010. Thus, the WWW is the largest corpus that can be used to analyze the semantic relationships between words. The NGD algorithm tries to determine the relationships between any two terms according to the number of search results, i.e., the number of returned pages. For example, when “hat” and “cowboy” are input as keyword queries to the Google search engine, about 6,730,000 web pages are retrieved. On the other hand, the query “cowboy” and “banana” only returns 1,320,000 pages. Thus, we can say the relationship between “hat” and “cowboy” is stronger than that between “cowboy” and “banana.” To measure this relationship, Cilibrasi and Vitányi [11] used Google page counts to develop a statistical index that shows the logical distance, called the normalized Google distance (NGD) between a pair of terms. A lower value implies a closer relation between two terms. In this paper, we de<sup>fi</sup>ne a query event as a set of web pages returned by Google in response to a search term (query). Formally, if w is the web page and y is a query event, then we denoted it as y={w:y∈w}. As shown in Eq. (1), the probability p(x|y) is de<sup>fi</sup>ned by p(x|y)=p(x,y)/ p(y) and p(y)=|y|/M. In the NGD algorithm, the probability p(y) of a query event y is the number of documents that Google searched in the query event divided by the overall number of web pages M, where M is the total numbers of document indexed by Google search engine. In addition, the joint probability p(x,y) is the number of web pages in the joint query event divided by the overall number of web pages M returned by Google. Because the conditional probabilities are independent of M, we use the frequency, i.e., the number of search pages, instead of the conditional probability to derive Eq. (2).

$$
D (x, y) = \frac {\max \left\{\log^ {1} / p (x | y) ^ {\prime} , \log^ {1} / p (y | x) ^ {\prime} \right\}}{\max \left\{\log^ {1} / p (x) ^ {\prime} , \log^ {1} / p (y) ^ {\prime} \right\}}\tag{1}
$$

$$
N G D (x, y) = \frac {\max \{\log f (x) , \log f (y) \} - \log f (x , y)}{\log M - \min \{\log f (x) , \log f (y) \}}\tag{2}
$$

## 2.2. Text summarization techniques

With the rapid growth of information on the Web, the ability to extract the key abstract content from information sources is important. Therefore, text summarization techniques and tools can help users <sup>fi</sup>nd needed information and make decisions quickly. The primary objective of text summarization is to extract key sentences from one or more documents in order to represent the meaning of the target document(s). Generally, the text summarization process can be divided into three phases: analyzing the source text, determining the salient points and synthesizing an appropriate output [22].

There are two types of summarization: single-document summarization and multi-document summarization. Single-document summarization is generated from the content of one document by different methods that try to reduce the amount of redundant information. Forsyth and Rada [16] computed the TF-IDF weight of a document to identify important terms. Since sentences are composed of many terms, they attempted to extract important sentences by using signature words of the document. Subsequently, Teufel and Moens [39] employed <sup>fi</sup>ve heuristic methods: cue, location sentence length, a thematic word method, and title methods to extract important sentences from document training sets. They examined the effectiveness of each method and then integrated the <sup>fi</sup>ve methods to analyze the tradeoff between them. The experiment results show that cue phrases (i.e., in summary, in conclusion, in short, therefore, and proper nouns) are the strongest single heuristics and the combination of the <sup>fi</sup>ve heuristics will yield the best performance. Lin and Hovy [27] considered the importance of the position of a sentence (i.e. the <sup>fi</sup>rst sentence of a document or a phrase), called the sentence position, to generate a summary directly. McDonald and Chen [31] used <sup>fi</sup>ve heuristics to calculate the value of each sentence and then generate generic summaries. The <sup>fi</sup>ve heuristics are cue phrases, signature words, proper nouns, the sentence's position and the length of the sentence.

Multi-document summarization focuses on reducing the amount of redundant information as well as <sup>fi</sup>ltering out repeated information. Goldstein et al. [21] proposed a method called maximal marginal relevance multi-document (MMR-MD), which maximizes the marginal relevance of sentences during retrieval and summarization. MMR-MD is based on the maximal marginal relevance algorithm, which is used to produce summaries. Notably, “relevant novelty” is a core metric that minimizes redundancy and maximizes both the relevance and diversity of sentences to extract sentences from multidocuments. Following previous studies, we adopt a heuristic-based method that exploits the characteristics of Wikipedia articles to select candidate sentences and then considers the novelty factor to generate summaries. To help users read summaries of important articles and similar topics easily, we propose an SNA-based article summarization technique. In the proposed WNavi<sup>s</sup> system, the user can click on a hub article in the topic network to get a summary of an article. We utilize the degree centrality measure to identify hub articles in SNA and use k-clique indicators in SNA to label the cohesive sub-groups of articles in a network. We describe the concept and usage of the summaries in Sections 5.3 and 6.4 respectively.

## 2.3. Text summarization evaluation methods

Text summarization evaluation methods try to determine how useful and accurate a summary is relative to its source [22]. They can be divided into two types: intrinsic techniques and extrinsic techniques [19,23]. Intrinsic techniques measure a system's text summarization quality. That is, users judge the relevance of extracted sentences or phrases directly to determine the quality of the summary. By contrast, extrinsic techniques measure a system's performance by the outcome of a given information retrieval task. That is, the quality of the summarization result depends on how well a user can complete a task based on the given summary. The task may involve answering questions related to an article, determining the relevance of a topic or searching for information. For example, the US government conducted a large-scale evaluation of summarization systems as part of its Tipster text program, which was organized by the Defense Advanced Research Projects Agency (DARPA) to promote state of the art text-handling technologies. The program applied an extrinsic evaluation method to a task that required the participants to view either the source text or the summary and determine whether or not the text was relevant to a particular topic [22]. The results demonstrate that the proposed text summarization technique's accuracy is similar to that of reviewing the whole text, but it requires less time.

With regard to evaluation criteria, existing approaches tend to focus on redundancy and diversity evaluation metrics [25]. Ideally, a method should extract suf<sup>fi</sup>cient sentences to cover as many answers as possible, and the number of overlapping answers among the selected sentences should be small. The key criteria used to evaluate the effectiveness of a multi-document summarization system are (1) clustering index, (2) coverage, (3) anti-redundancy index, (4) summary cohesion, (5) quality, (6) identi<sup>fi</sup>cation of inconsistencies in the source information, (7) summary updates, and (8) effective user interfaces [21]. The clustering index assesses a system's ability to cluster similar documents in order to help users <sup>fi</sup>nd related information. The anti-redundancy index assesses the ability to minimize redundancy in the summary. The cohesion index means the ability to combine sentences in a meaningful manner for the user, e.g., by ranking. Similarly, the quality index assesses whether the generated summaries are readable and relevant, and whether they contain enough contexts for users to understand the meanings of the summaries. The effective user interface index assesses whether users can view the contexts of sentences in the summary and interact with the summary. In this work, we exploit the clustering, anti-redundancy, quality and effective user interface indices to assess the summaries of topics and sub topics in Wikipedia. The SNA-based article summarization technique utilizes the clustering index to cluster similar articles based on the structure of the topic network and examines the index with an intrinsic evaluation technique, as explained in Section 7.2. The anti-redundancy index is examined during the single-document summarization process, as described in Section 7.1. The quality and effective user interface indices are assessed by extrinsic evaluations via the classi<sup>fi</sup>cation task and simulated search task, which we discussed in Sections 7.3 and 7.4 respectively. Since it is dif<sup>fi</sup>cult to generate an ideal summary of an article, we propose an extrinsic evaluation approach that helps the user review the topics presented on the interface and accomplish the assigned task.

## 3. The system framework

Internet search engines like Google and Yahoo! provide one of the most popular ways to access information on the WWW. Furthermore, with the emergence of Web 2.0 technologies, social web sites (i.e., social networking websites and micro-blogging services) provide unprecedented opportunities for sharing user-generated content. Wikipedia, one of the most famous collaborative projects on the Web, has become an extremely popular reference database for people seeking information or knowledge. Moreover, because the already vast amount of online information continues to grow rapidly, a large number of people now use IR tools everyday as a matter of course. Thus, there is an increasing demand for effective and ef<sup>fi</sup>cient IR and information management tools to support user's search activities [7,24]. To this end, we propose an application with navigation-aided tools that can be generalized to an internal linkbased knowledge intensive website. The research questions addressed in this work and the associated objectives are listed below.

1. To represent the relationships between hypertexts, we utilize the Link Strength measure and the NGD algorithm to construct an initial internal, link-based network to give users generic views of related articles. Because our research target is the internal link-based website, Wikipedia, we need to modify our methods based on the characteristics of the website. Then, we can use the proposed measure to identify the semantic relationships between articles in the constructed topic network.

2. We propose a novel SNA-based article summarization technique that enables users to explore articles related to similar topics ef<sup>fi</sup>- ciently. We also apply a series of intrinsic and extrinsic evaluation methods to analyze the performance of the proposed technique in terms of the precision and recall metrics.

3. After investigating the type of interface that would help users understand topics quickly and prevent them from getting lost in Wikipedia, we designed a semantics-based interface called WNavi<sup>s</sup>. To assess the usefulness of WNavi<sup>s</sup>, we employed a user task-oriented evaluation method.

The process used to generate the WNavi<sup>s</sup> interface is illustrated in Fig. 1. In the following, we describe the modules of the framework.

## 3.1. Article pre-processing module

The initial article that interests a user is de<sup>fi</sup>ned as the seed article (query), and the articles related to the seed query are called linkrelated articles of n degrees. The proposed framework retrieves all linkrelated articles within three degrees. Besides extracting the hyperlinks from each article, the module stores the content of the article, including the title and its associated links, in XML format. Basically, Wikipedia content is written in wiki markup language, which is based on the XML web language, and comprises a wiki-recognized title, content, and a huge number of out-links and in-links. Fig. 2 shows an article in Wikipedia written in wiki markup language, i.e., an XML <sup>fi</sup>le. In this phase, we identify and extract the information we want to use from the special symbols in wiki language. For example, the symbols “[” and “]” are used for outlinks, while the symbols “[[” and “]]” represent the in-links. This module extracts the IDs, names, editing dates and out-links of the articles and stores them in the database.

## 3.2. Internal link-based semantic network analysis module

We propose an internal-based semantic topic network analysis measure. Speci<sup>fi</sup>cally, this module utilizes the proposed link strength (LS) measure to search for topics related to the user's seed query. It <sup>fi</sup>lters out unimportant articles and <sup>fi</sup>nds possible subgroups around the seed query. If the value or strength of a link is less than a speci<sup>fi</sup>ed threshold, the system will remove the link from the internal linkbased network. The system also performs semantic analysis based on the NGD algorithm to remove noisy nodes from the initial network.

## 3.3. SNA analysis module

This module utilizes the social network analysis (SNA) indicators de-<sup>fi</sup>ned in social network theory [42] to identify the roles of articles in the topic network based on the results of the previous stage. Generally, we apply cohesive and centrality measures in SNA, i.e., k-cliques and degree centrality, to identify, respectively, the subtopics and the key articles of subtopics to help users search for information in Wikipedia.

## 3.4. SNA-based summary generation module

This module generates the summaries of articles based on the SNA analysis results; that is, the interface displays different summarization results based on the type of network topology. To help users search for information, we use centrality-based and cohesive measures in SNA to summarize single and multiple articles. Then, when the user clicks on a topic node that he/she wants to explore, an SNA-based summary is presented on the interface to help the user read the related articles quickly.

![](/api/attachments/E2992NUJ/fulltext/images/03ce4dd9876967d0248d75c2739788e653e525dfb1fcc77b6feba2bfdf633456.jpg)  
Fig. 1. The process for generating a semantics-based WNavi<sup>s</sup> interface.

![](/api/attachments/E2992NUJ/fulltext/images/e1d937ed5c36cd5793197ecc581cbd16749704f3889db5273ceacb36c80bfddc.jpg)  
Fig. 2. An example of a Wiki markup <sup>fi</sup>le for an article in Wikipedia.

To visualize the semantics-based topic network more ef<sup>fi</sup>ciently, we use the software libraries of the Java Universal Network/Graph (JUNG) Framework to create the WNavi<sup>s</sup> interface, which is a June-based appli cation. The JUNG framework provides many useful algorithms and graph layouts to help us work with relational data; thus, it was easy for us to develop the Web-based interface.

## 4.1. Internal link analysis with the LS measure

## 4. Incorporating semantic analysis techniques into the internal link-based network

We use the term “article” to denote an entry in Wikipedia rather than a page on the WWW, and the term “node” to denote a word or phrase in an article with a hyperlink to another article. The link strength (LS), which indicates the degree of closeness between two articles, is determined by considering the type and frequency of the links between the articles. Our goal is to <sup>fi</sup>nd the speci<sup>fi</sup>c topic or related subtopics for a seed query. An article may have three types of links: in-links, out-links, and reciprocal (bi-directional or multi-directional) links. Basically, the in-links and outlinks of an article are hyperlinks. For example, given two articles $a _ { i }$ and $a _ { j } ,$ if article a has one or more nodes that mention article $a _ { j } ,$ but article $a _ { j }$ does not have any nodes that mention article $a _ { i } ,$ it means that $a _ { i }$ is with out-link relationship with article $a _ { j } .$ However, if $a _ { j }$ also has a node that mentions article $a _ { i } ,$ we de<sup>fi</sup>ne the relationship as a reciprocal link, which may be a bi-directional link or a multi-directional link. The three types of links are illustrated in Fig. 3 and an example is given in Fig. 4. In addition to the relationships between articles, the frequency of the links (the link frequency) between the articles is determined by the LS measure, denoted by $\zeta ,$ which is calculated as follows:

$$
\zeta \left(a _ {i}, a _ {j}\right) = \left(f b i \left(a _ {i}, a _ {j}\right)\right) ^ {w 1} + w _ {\mathbf {2}} \times f \text { in } \left(a _ {i}, a _ {j}\right) + w _ {\mathbf {3}} \times f \text { out } \left(a _ {i}, a _ {j}\right),\tag{3}
$$

where $f _ { - } i n ( a _ { i } , a _ { j } )$ denotes the frequency of in-links from a to a ; f\_out(a , a ) denotes the frequency of out-links from a to a ; and $f _ { - } { b i } ( a _ { i } , a _ { j } )$ denotes the frequency of bidirectional links between a and $a _ { j } .$ Note that the frequency of each bi-directional link in the reciprocal link, i.e., the tight or strong-tight link de<sup>fi</sup>ned earlier, is much more important than the unidirectional link; therefore, we put the weight of f $b i ( a _ { i } , a _ { j } ) , w _ { 1 } ,$ , in the exponent part of the equation. Then, we use the parameters $w _ { 2 }$ and w to adjust the relative importance of the in-links and out-links respectively. Based on our analysis results, we set $w _ { 1 }$ at 2 to select strong-tight links <sup>fi</sup>rst; then, we set $w _ { 2 }$ at 0.1, and $w _ { 3 }$ at 0.9. Since the centrality measure in SNA focuses on out-links, it is reasonable to give more weight to outlinks than in-links when analyzing the relationships between articles in Wikipedia. Furthermore, if a node does not have any bidirectional links, i.e., $\begin{array} { r } { f \_ b i ( a _ { i } , \ a _ { j } ) = 0 , } \end{array}$ we remove it from the preliminary internal linkbased network. Details of how to set the relative weights of the in-links and out-links and the threshold of the LS value can be found in our recent work [45].

## 4.2. Semantic relatedness analysis with the NGD algorithm

To <sup>fi</sup>lter articles with low semantic relatedness in the initial internal link-based network, we use the key terms of each article to conduct further tests for semantic relatedness. However, using computers to determine the semantic relationships between keywords is a dif<sup>fi</sup>cult task. In recent years, researchers in the <sup>fi</sup>elds of natural language processing and arti<sup>fi</sup>cial intelligence have expended a great deal of effort on developing methods that enable computers to extract the meanings of words automatically [10,32]. One promising approach, called the normalized Google distance (NGD) algorithm, uses the number of search results returned by the Google search engine to detect the semantic relationships among terms automatically. In this work, we utilize the NGD algorithm to <sup>fi</sup>nd articles with high semantic relatedness by analyzing key terms. Speci<sup>fi</sup>cally, we de<sup>fi</sup>ne the titles of articles in Wikipedia as nodes in the NGD algorithm and try to determine the relevance of two web pages (articles) to one another by analyzing their titles. The NGD algorithm then assigns a value to the distance (strength) of the relationship. The lower the value, the higher will be the semantic relationship between the two articles. We <sup>fi</sup>lter topics that have a distance value higher than a certain threshold in order to remove noise. The formula of the algorithm is given in Eq. (2).

![](/api/attachments/E2992NUJ/fulltext/images/8d695146f88ffd9d2d2fa8ccb909bc4b61997ee17af68def835d64ed11b6987d.jpg)  
Fig. 3. (A): Out-link a to a (Uni-directional non-reciprocal link). (B): In-link a to a (uni-directional non-reciprocal link). (C) Reciprocal link (bi-directional reciprocal link)

Table 1  
![](/api/attachments/E2992NUJ/fulltext/images/d5617e6d0aa55af34c46e205f1d20a9d4f06ba54752a66a3e66f27fe2417267c.jpg)  
Fig. 4. An example of a reciprocal link.

## 4.2.1. Testing the NGD threshold

According to Evangelista and Kjos-Hanssen [14], the expected value of the NGD threshold should be around 0.7. We invited three experts from the information management department of a major university to determine if the nodes in the topic network were relevant to the seed query “History of the personal computer.” Table 1 shows the nodes (titles) that the experts deemed unrelated to the seed query. The results show that the average NGD value of all the unrelated nodes was 0.695. In another test, the average NGD value of nodes that were unrelated to the seed query “Knowledge management” was 0.712. The results are similar to the expected value reported by Evangelista and Kjos-Hanssen [14], i.e., the NGD value is approximately 0.7. Thus, we set the value of the threshold at 0.7 to construct the <sup>fi</sup>nal topic network for a seed query.

## 4.2.2. Similarity calculation

We also conduct a similarity calculation to compare the internal similarity of each network. Table 2 shows that after applying NGD <sup>fi</sup>ltering to a network, it has a higher cosine value than before semantic analysis was performed.

## 5. SNA-based summaries in Wikipedia

## 5.1. Process for generating summaries

Summaries can be divided into three types based on their purpose: indicative summaries, informative summaries and critical summaries [36]. An indicative summary provides enough information to let the user determine whether the actual document would be helpful, and whether reading the document would be worthwhile. An informative summary condenses the important content of the actual document, and the user could even utilize it instead of the document. A critical summary comments on a text by using summarization methods to help users understand the original content and its purpose. In our research context, we generate informative summaries to help users explore topics in Wikipedia.

NGD threshold values of two seed queries.

<table><tr><td>Title of the article</td><td>Judgment (irrelevant)</td><td>NGD value</td><td>Title of the article</td><td>Judgment (irrelevant)</td><td>NGD value</td></tr><tr><td colspan="3">Seed query “History of personal computers”</td><td colspan="3">Seed query “Knowledge management”</td></tr><tr><td>74181(ALU)</td><td>2</td><td>0.464</td><td>Social Software Engineering</td><td>2</td><td>1.000</td></tr><tr><td>BASIC</td><td>2</td><td>0.876</td><td>The Social Construction of Reality</td><td>2</td><td>1.000</td></tr><tr><td>Bluetooth</td><td>2</td><td>0.971</td><td>ECM</td><td>2</td><td>0.859</td></tr><tr><td>Burroughs_Corporation</td><td>3</td><td>0.444</td><td>Enterprise information management</td><td>2</td><td>0.815</td></tr><tr><td>Laser_diode</td><td>2</td><td>1.000</td><td>Understanding</td><td>2</td><td>0.800</td></tr><tr><td>Left-handedness</td><td>3</td><td>1.000</td><td>Artificial intelligence</td><td>2</td><td>0.779</td></tr><tr><td>Pixar</td><td>2</td><td>0.896</td><td>Group information management</td><td>2</td><td>0.777</td></tr><tr><td>PlayStation_2</td><td>3</td><td>0.736</td><td>Interdisciplinarity</td><td>2</td><td>0.776</td></tr><tr><td>The_Walt_Disney_Company</td><td>3</td><td>0.421</td><td>Webassistant</td><td>2</td><td>0.670</td></tr><tr><td>Video_game</td><td>3</td><td>0.836</td><td>Internal control</td><td>2</td><td>0.671</td></tr><tr><td>Wii_Remote</td><td>3</td><td>0.421</td><td>Jumper 2.0</td><td>2</td><td>0.643</td></tr><tr><td></td><td></td><td></td><td>Knowledge policy</td><td>2</td><td>0.627</td></tr><tr><td></td><td></td><td></td><td>Association for Information and Image Management</td><td>2</td><td>0.591</td></tr><tr><td></td><td></td><td></td><td>Information ecology</td><td>2</td><td>0.577</td></tr><tr><td></td><td></td><td></td><td>Igor Ansoff</td><td>2</td><td>0.535</td></tr><tr><td></td><td></td><td></td><td>Defensive marketing warfare strategies</td><td>2</td><td>0.487</td></tr><tr><td></td><td></td><td></td><td>Guerrilla marketing warfare strategies</td><td>3</td><td>0.467</td></tr><tr><td colspan="3">Average: 0.695</td><td colspan="3">Average: 0.712</td></tr></table>

Table 2  
Comparison of topic network similarity.

<table><tr><td>Queries</td><td>Internal-link based network (IIN)</td><td>IIN With NGD Analysis</td></tr><tr><td>History of PCs</td><td>0.248</td><td>0.240</td></tr><tr><td>Star Trek</td><td>0.149</td><td>0.275</td></tr><tr><td>Abraham Lincoln</td><td>0.103</td><td>0.148</td></tr><tr><td>Knowledge Management</td><td>0.261</td><td>0.291</td></tr></table>

Note: Data in bold denotes the method has better result for the topic.

Fig. 5 shows the two phases involved in generating SNA-based summaries in our research context, i.e., the analysis phase and the synthesis phase. The steps for generating a summary are as follows: (1) pre-process the source articles; (2) parse the articles into terms and calculate the weights of the terms; (3) select the terms based on the feature set; (4) calculate the sentence scores based on the proposed methods; (5) generate summaries from the top-N sentences; and (6) apply relevant novelty sentence (RNS) metrics to <sup>fi</sup>lter sentences and then resort them based on the order of the sentences in the original articles. For multi-article summaries, we consider the role of each article in the social network. That is, we weight the terms based on the roles of the articles in the SNA after step (3). Then, we apply different summarization strategies based on those roles. First, we identify a cohesive article (CA) according to the formula of k-cliques given in SNA. The analysis results help us label the subtopics of the articles in the network. Second, we <sup>fi</sup>nd the hub article (HA) of each sub-topic and analyze it based on the formula of degree centrality given in SNA. The objective is to help the user explore the hub article of each sub-topic. We also present an informative summary of the hub article and its associated articles.

## 5.2. Extracting the summary of a single article

Radev et al. [35] designed the MEDA algorithm to generate the summaries of multi-documents. The algorithm uses three features to select the top sentences of an article, namely, the centroid value, positional value, and <sup>fi</sup>rst-sentence overlap. Similarly, we analyze the characteristics of articles in Wikipedia to extract keywords and then select the top sentences to compile summaries of the topic or sub topic.

## 5.2.1. Feature selection and keyword extraction

In this work, we utilize three features based on the characteristics of Wikipedia to select keywords in an article, namely, the <sup>fi</sup>rst paragraph (FP), the weighted <sup>fi</sup>rst-paragraph overlap (WF) and concept phrases (CP). Fig. 6 shows examples of the <sup>fi</sup>rst paragraphs and concept phrases in articles associated with the “Knowledge Management” query. We incorporated the concept of the position value of a sentence into the concept of the <sup>fi</sup>rst-paragraph overlap to generate the score of each sentence, i.e. the weighted <sup>fi</sup>rst-paragraph overlap, wf , as shown in Eq. (4). The position value, $P _ { i } ,$ means the position of the ith sentence in the document, and n is the number of sentences in the target article. The index i of wf starts from the <sup>fi</sup>rst sentence of the second paragraph. The candidate terms can be selected from those sentences, i.e., sentences with high wf values, as shown in Eq. (5). The <sup>fi</sup>nal keywords are selected based on the relative importance of the <sup>fi</sup>rst paragraph $f _ { \pm }$ the weighted <sup>fi</sup>rst-paragraph overlap a, and the concept phrases, $C \dot { P } _ { k }$ as shown in Eq. (6). Then, the initial summary corpus (Sum\_corpus) is generated based on the proposed technique. Table 3 shows samples of keywords extracted based on the different features.

$$
w f _ {i} = \operatorname{Sim} \left(\vec {f} _ {\mathbb {1}} \vec {f} _ {i}\right) \times P _ {i}
$$

$$
w h e r e P _ {i} = \frac {n - i + 1}{n}\tag{4}
$$

$$
\vec {a _ {k}} = \sum_ {i = 1} ^ {n} w f _ {s _ {i}} \times \vec {S _ {i}}\tag{5}
$$

$$
\vec {a _ {k} ^ {\prime}} \lambda \times t o p (\vec {a _ {k}}) + (\vec {f _ {1}} + C \vec {P _ {k}})\tag{6}
$$

## 5.2.2. Sentence scoring

In this step, we utilize the cosine measure to determine the similarity between the Sum\_corpus, $a _ { \scriptscriptstyle  { R } } ^ { \prime }$ and each sentence in the target article. Then, we calculate the score of each sentence, as shown in Eq. (7). We select the top 20 to 30 sentences with highest scores as the preliminary summary of the target article.

$$
\operatorname{Score} \left(S _ {i}\right) = \operatorname{Sim} \left(\vec {a _ {k} ^ {\prime}} \vec {S _ {i}}\right) = \frac {\vec {a _ {k} ^ {\prime}} \cdot \vec {S _ {i}}}{\left| \vec {a _ {k} ^ {\prime}} \right| \left| \vec {S _ {i}} \right.}\tag{7}
$$

## 5.2.3. Relevant novelty sentences (RNS) calculation

To avoid selecting redundant sentences from the subtopics of the articles, we calculate the overlap degree between sentences and

![](/api/attachments/E2992NUJ/fulltext/images/71f8e48ee470c205277a4e316c7d0222c342c599fcd905ea722cfb218244d1da.jpg)  
Fig. 5. The process for generating SNA-based summaries.

![](/api/attachments/E2992NUJ/fulltext/images/8d694e1dcaa764827b361ae3e063f63214d915f89e488f57ad8a013160d1f8f4.jpg)  
Fig. 6. An example of selecting features.

then select the top sentences based on their “relevant novelty,” which is a metric for minimizing redundancy and maximizing both relevance and diversity [21]. That is, we apply an overlap threshold before adding a new sentence to the pool. If the overlap score is higher than the threshold, the new sentence will not be selected for the summary. The relevant novelty sentence (i.e., RNS) <sup>fi</sup>ltering algorithm is de<sup>fi</sup>ned in Eq. (8). The equation is divided into two parts. For Sim , the equation calculates the similarity between the corpus and the candidate sentence $S _ { m } .$ The corpus comprises the selected features and extracted keywords. For Sim , we calculate the similarity between the candidate sentence, $S _ { m } ,$ and the set of sentences selected previously for the target article. The second part of the equation minimizes the redundancy; thus, we subtract the maximal similarity value as the penalty. In Eq. (8), S denotes the top 15 sentences selected in the previous step; and the parameter α is used to adjust relative importance of Sim , and Sim .

Keyword extraction by different summarization methods.

<table><tr><td colspan="4">Some keywords from the Weighted First-paragraph Overlap of Knowledge Management</td></tr><tr><td>Knowledge</td><td>Insight</td><td>Comprise</td><td>Access</td></tr><tr><td>Management</td><td>Individual</td><td>Create</td><td>Activities</td></tr><tr><td>Organization</td><td>Framework</td><td>Enable</td><td>Technology</td></tr><tr><td>Strategy</td><td>Tacit</td><td>Experiences</td><td>Effort</td></tr><tr><td>Practice</td><td>Rang</td><td>History</td><td>Category</td></tr><tr><td>Represent</td><td>Discussion</td><td>Corporate</td><td>Embed</td></tr><tr><td>Explicit</td><td>Propose</td><td>Program</td><td>...</td></tr><tr><td colspan="4">Total count of terms: 534</td></tr></table>

Some keywords from the First Paragraph of Knowledge Management

<table><tr><td>Knowledge</td><td>Company</td><td>Process</td><td>Intellectual</td></tr><tr><td>Management</td><td>Strategy</td><td>Exist</td><td>Represents</td></tr><tr><td>KM</td><td>Information</td><td>Focus</td><td>Nonaka</td></tr><tr><td>Organization</td><td>Practice</td><td>Share</td><td>Field</td></tr><tr><td>Technology</td><td>Includes</td><td>Learn</td><td>Recently</td></tr><tr><td>Effort</td><td>System</td><td>Business</td><td>Compute</td></tr><tr><td>Individual</td><td>Research</td><td>Internal</td><td>...</td></tr></table>

Total count of terms:129

Keywords from the Concept Phrases of Knowledge Management

<table><tr><td>Intelligence</td><td>Meta-knowledge</td><td>Representation</td><td>Economy</td></tr><tr><td>Management</td><td>Sense-making</td><td>Knowledgebase</td><td>Ecosystems</td></tr><tr><td>Software</td><td>Data</td><td>Ontology</td><td>Tagging</td></tr><tr><td>Organization</td><td>Mining</td><td>Sociology</td><td>Firm</td></tr><tr><td>Unconscious</td><td>Dikw</td><td>Interaction</td><td>Memory</td></tr><tr><td>Engineering</td><td>Bookmarking</td><td>Ecology</td><td>Value</td></tr><tr><td>Worker</td><td>Humancomput</td><td>Community</td><td></td></tr><tr><td colspan="4">Total count of terms:27</td></tr></table>

Note: Available at: http://en.wikipedia.org/wiki/Knowledge\_management (accessed 30 January 2011).

$$
R N S \stackrel {{d e f}} {{=}} \alpha \left(S i m _ {1} \left(\vec {S _ {m}}, \vec {a _ {k}}\right)\right) - (1 - \alpha) \max _ {S _ {n} \in S} S i m _ {2} \left(\vec {S _ {m}} \vec {S _ {n}}\right)\tag{8}
$$

We set α at different values to determine the importance of RNS in the following evaluation procedure.

## 5.3. SNA-based summaries of multi-articles

To identify prominent actors in a social network, we use two types of measures: centrality and prestige. The centrality measures, i.e. degree centrality, closeness centrality, and between centrality, and the prestige measures, i.e. proximity prestige, degree prestige, and rank prestige, are used to quantify the prominence of actors involved in the social network [3,17,20]. Cohesiveness is another well-known measure used to identify subgroups of actors that are relatively strong, direct, intense, and frequent, and have positive ties in a network [42]. There are several cohesive measures, e.g., k-clique, kplexes, and k-core. As mentioned earlier, we utilize the centralitybased measures and cohesive measures to analyze the topology of the topic network. The former identify the most important actors and the latter identify the subtopics in the topic network. Next, we explain the indicators used to generate the SNA-based summaries of the topic network.

## 5.3.1. Subgroup articles

Cohesive SNA indictors identify sub-groups of actors in a social network. We use k-clique indicators to label the cohesive subgroups of articles in a network. A clique in a graph is a maximal complete sub-graph of k nodes; and a k-clique is a maximal sub-graph in which the largest geodesic distance between any two nodes is no greater than k [38]. Thus, the subgroup comprises subsets of articles that have relatively strong ties in the link-based network. Fig. 7(A) shows that the “Knowledge Management” article is at the center of the sub-group of articles and the other nodes are articles related to it. The k-clique indicator is de<sup>fi</sup>ned as follows:

$$
d i s (i, j) \leq k f o r a l l n _ {i}, n _ {j} \in N _ {\text { topic }},\tag{9}
$$

where dis(i, j) denotes that the geodesic distance between any two nodes is not greater than n. In this work, we set k at 3, i.e., all nodes are reachable through at most two intermediary nodes.

## 5.3.2. Hub articles

We utilize the degree centrality measure to identify the hub article in SNA. The measure calculates the number of links an actor has with other actors in the social network, as shown in Fig. 7(B); and the actor with the most connections to other actors is deemed most prominent actor in the network [18,33,38]. The degree centrality of an actor i, i.e., DC(n ), is de<sup>fi</sup>ned as follows:

![](/api/attachments/E2992NUJ/fulltext/images/48a459ad2dcae3a8c9be47087274776811189f84875faa1810276d5cd841d8f8.jpg)  
Fig. 7. (A) Example of the cohesive article applied 3-clique in Knowledge Management topic. (B) Example of the hub article applied degree centrality in Social network topic.

$$
D C (n _ {i}) = d (n _ {i}) = \sum_ {j} x _ {i j} = \sum_ {j} x _ {j i},\tag{10}
$$

where d(n ) is the total number of links of an actor $n _ { i } ;$ and x is the number of in-links or out-links of $n _ { i } .$

## 5.3.3. Generating summaries for multi-articles

We use the k-clique indicators to identify the subgroups of a topic network, as shown in Eq. (9). Then, we use the degree centrality indicator to analyze the hub article of each subgroup, as shown in Eq. (10). To generate multi-article summaries, we consider the content of the hub article and the other articles in the same subgroup based on Eq. (11). Speci<sup>fi</sup>cally, we extract keywords from the central article (CA) and the other articles (denoted as GAs) that are relevant to the CA. Then, we apply the Hybrid(0.1) method with low relevant novelty (i.e., α is set at 0.9) to extract the keywords from each article. On average, the α setting of 0.9 achieves the best performance for single article summaries. We discuss the evaluation results in detail in Section 7. Finally, the keywords extracted from the CA and GAs form the corpus of our multi-article (MA) summaries.

$$
\vec {M A} = \beta \times \vec {C A} + (1 - \beta) \times \vec {G A}\tag{11}
$$

The parameter $\beta$ is used to adjust the relative importance of the CA and GAs.

## 6. Evaluation methods, tasks and metrics

## 6.1. Evaluation method

For single document summaries, we evaluate the performance of <sup>fi</sup>ve methods, namely, the CP&FP, WF, Hybrid(0.1), Hybrid(0.5), and Hybrid(0.9) methods. The CP&FP method selects keywords from the concept phrases and the <sup>fi</sup>rst paragraph of the target article, as shown in Eq. (6). The parameter λ is set at 0 in the equation. The WF method selects keywords from the weighted <sup>fi</sup>rst paragraph, as shown in Eq. (5). In the three Hybrid(λ) methods, we adjust the parameter λ in Eq. (6) to 0.1, 0.5, and 0.9 respectively, and refer to the methods as Hybrid(0.1), Hybrid(0.5), and Hybrid(0.9). We also assess the importance of relevant novelty based on Eq. (8) in Section 5.2. The parameter α is used to adjust the relative importance of similarity and novelty. The method with the best performance on the single article summaries is selected as the basis for generating multi-article summaries. We apply Eq. (11)

to generate the summaries of a group of articles and then evaluate the summarization results by intrinsic and extrinsic methods.

## 6.2. Evaluation tasks

We performed a series of tasks to evaluate the effectiveness of the single and multi-article summarization methods and the usefulness of the developed application. The text summary evaluation methods can be divided into two types: intrinsic methods and extrinsic methods [19,23]. Intrinsic methods measure a system's text summarization quality; while extrinsic methods measure a system's performance based on a given information retrieval task. In this work, we use both methods to evaluate the performance of the single and multi-article summarization methods.

## 6.2.1. The intrinsic evaluation task

First, we evaluate the quality of the summaries produced by the CP, WF, Hybrid(0.1), Hybrid(0.5) and Hybrid(0.9) methods. The precision rate and recall rate are used to compare the <sup>fi</sup>ve methods [37,44]. Determining whether a sentence is relevant to each evaluation article (topic) is an important issue. In this work, we asked two domain experts to manually label sentences that were helpful or partially helpful to each evaluation topic. We also asked them to select the sentences that were not helpful in each evaluation topic. Between 8 and 12 sentences were labeled as helpful (H), and 3 to 7 sentences were labeled as not helpful.

## 6.2.2. The extrinsic evaluation task

We assign a classi<sup>fi</sup>cation task to a group of users. Speci<sup>fi</sup>cally, we ask the users to classify some summaries into subgroups and calculate the precision of the classi<sup>fi</sup>cation results. A short simulated useroriented search task is also performed to evaluate the effectiveness of the proposed interface [4,5,41]. The task involves search missions that need to be accomplished; for example, the users are asked to <sup>fi</sup>nd answers to questions about knowledge management by utilizing the basic Wikipedia interface and the proposed WNavi<sup>s</sup> interface. We explain this aspect in detail in Section 7.4.

## 6.3. Evaluation metrics

We evaluate the performance of the proposed summarization methods applied in the constructed interface. The IR evaluation methodology focuses on the retrieval of quantitative or qualitative data [9]. Retrieval effectiveness is the most commonly used criterion for quantitative evaluation, and the effectiveness of information retrieval is normally measured by the precision and recall rates [9,12,37]. On the other hand, qualitative evaluation of an IR system can be based on the analysis of questionnaires that request information about various evaluation items, such as user satisfaction, usability, and learning ability. Qualitative evaluation is more suitable for evaluating the effectiveness of users' interactive search activities. Both types of evaluations are conducted in this work. Speci<sup>fi</sup>cally, we use the relative scale precision, precision, and recall metrics to compare the <sup>fi</sup>ve methods [37,44].

![](/api/attachments/E2992NUJ/fulltext/images/b875ab4437f5e13f51d588d5e6266f4b51b9e46cbcbff5465d5765257a4fb3c4.jpg)

![](/api/attachments/E2992NUJ/fulltext/images/e4dcc22f54a3ce831169e9e356c9b66925946f1659e83cf8f317c0f09f10d4e7.jpg)  
Fig. 8. (A) The basic Wikipedia interface (interface A). (B) The semantics-based WNavi<sup>S</sup> interface (interface B).

Table 4  
The compression rates used for text summarization.

<table><tr><td>Article no.</td><td>Terms</td><td>Selected terms*</td><td>Compression rate</td><td>Article no.</td><td>Terms</td><td>Selected terms*</td><td>Compression rate</td></tr><tr><td>A1</td><td>2254</td><td>403.4</td><td>82.10%</td><td>A10</td><td>1826</td><td>334.4</td><td>81.69%</td></tr><tr><td>A2</td><td>651</td><td>321.5</td><td>50.61%</td><td>A11</td><td>878</td><td>395.4</td><td>54.97%</td></tr><tr><td>A3</td><td>6422</td><td>355.6</td><td>94.46%</td><td>A12</td><td>2539</td><td>385</td><td>84.84%</td></tr><tr><td>A4</td><td>1105</td><td>347</td><td>68.60%</td><td>A13</td><td>1226</td><td>385.6</td><td>68.55%</td></tr><tr><td>A5</td><td>450</td><td>292.2</td><td>35.07%</td><td>A14</td><td>1046</td><td>367</td><td>64.91%</td></tr><tr><td>A6</td><td>1017</td><td>320</td><td>68.53%</td><td>A15</td><td>4845</td><td>387.6</td><td>92.00%</td></tr><tr><td>A7</td><td>1257</td><td>307.2</td><td>75.56%</td><td>A16</td><td>1986</td><td>484</td><td>75.63%</td></tr><tr><td>A8</td><td>3866</td><td>413</td><td>89.32%</td><td>A17</td><td>10,349</td><td>435.6</td><td>95.79%</td></tr><tr><td>A9</td><td>517</td><td>441</td><td>14.70%</td><td colspan="3">Average compression rate</td><td>70.43%</td></tr></table>

Note: The column of “Selected terms” denotes # of terms selected from the terms.

## 6.3.1. Relative scale precision

We use a three point relevance scale: helpful, partially helpful and not helpful [29]. For a sentence to be deemed helpful, it must enable the evaluators to understand the topic; while a partially helpful sentence provides some information connected to the topic. We calculate the precision of sentences that are partially helpful (labeled PH) as well as a stricter precision criterion for sentences labeled H. The precision scores of partially helpful (PH) and helpful (H) sentences are denoted as Precision@PH and Precision@H respectively.

$$
\text { Precision@PH } = \frac {| \text { Sentences   labled   as   PH   or   H } |}{| \text { Extracted   sentences } |}\tag{12}
$$

$$
\text { Precision@ } H = \frac {| S e n t e n c e s l a b l e d a s H |}{| E x t r a c t e d s e n t e n c e s |}\tag{13}
$$

## 6.3.2. Precision

The precision rate for an evaluation task is the ratio of the total number of relevant articles retrieved to the total number of top-N articles. Note that P@N (precision at N) denotes that the precision is calculated from the N <sup>fi</sup>rst evaluated articles [29,43]. In this work, we evaluated P@1, P@2, and P@3.

## 6.3.3. Recall

The recall rate is the ratio of the total number of really helpful sentences retrieved to the number of top-N support documents in the system. Here, we only consider sentences labeled H. There are between 8 and 12 sentences.

## 6.4. The interfaces

## 6.4.1. Basic Wikipedia interface (interface A)

The basic Wikipedia interface, see Fig. 8(A), only allows participants in the experiment to access Wikipedia via the browser, i.e., IE or Firefox, to accomplish the assigned search task. As shown in the <sup>fi</sup>gure, the interface is divided into two sections. Participants can use the left-hand window to browse and search for needed information, and then list the retrieved articles in the right-hand window.

## 6.4.2. WNavi<sup>S</sup> interface (interface B)

The WNavi<sup>S</sup> interface is divided into three areas, as shown in Fig. 8(B). The upper left-hand area of the interface (①), shows the topic (article) network based on the user's query; and the lower left-hand area (②) shows a related article in Wikipedia when the user clicks on a node in the topic network. In addition, a tree of subtopics is shown on the right-hand side of area ③ to provide users with an overview of the network. The user can click on the <sup>fi</sup>rst level of the tree of sub-topics to check the summaries extracted from a group of articles. Moreover, when the user clicks on a hub article, i.e., the blue nodes, summaries of the article will pop up, as shown in the interface (④). Finally, the user lists the retrieved articles on the right-hand side of the interface (⑤). The interface enables users to <sup>fi</sup>nd articles with similar subtopics easily.

## 7. Evaluation results and discussions

## 7.1. Intrinsic evaluation of summaries of single article

To select important articles for generating summaries on the interface, we select the seed article and the central article of the topic network, i.e., measure by degree centralities in SNA, as our candidate articles. For example, 17 articles for the “Knowledge Management” topic are selected as candidate articles for extracting summaries. The articles with the associated compression rates are listed in Table 4. Following Rush et al. [36], we use an average compression rate of 70%. As mentioned earlier, we apply relative scale precision and recall metrics to evaluate the performance of the CP&FP, WF, Hybrid(0.1), Hybrid(0.5) and Hybrid(0.9) methods. We calculate the relative scale precision for sentences labeled PH and apply the stricter precision criterion for sentences labeled H, as shown in Eqs. (12) and (13) respectively. We refer to them as Precision@PH and Precision@H, respectively. The precision scores for the 17 topics are shown in Tables 5a and 5b; the results of Precision@H are listed in Tables 6a and 6b; and the recall rates are shown in Tables 7a and 7b.

## 7.1.1. The results based on the Precision@PH metric

The Precision@PH metric is used to determine if a sentence is partially helpful to users in terms of understanding the content of the article. The compression rate is 70% on average. We discuss the evaluation results below.

Discussion 1: The performance of the WF method, i.e., the weighted <sup>fi</sup>rst-paragraph overlap method, is worse than that of the CP&FP method in terms of Precision@PH, as shown in Table 5a. For the “Social Net work” article, the precision is only 0.4778 under the WF method compared to 1.000 under the CP&FP method. This may be because the WF method extracts all the keywords from an article; thus, it cannot select important keywords to generate good summaries.

## Table 5a

Average precision@PH rates for 17 articles under the WF and CP&FP methods.

<table><tr><td>Article no.</td><td>Article title</td><td>WF</td><td>CP&amp;FP</td></tr><tr><td>A1</td><td>KM</td><td>0.7556</td><td>0.7889</td></tr><tr><td>A2</td><td>CSCW</td><td>0.9667</td><td>0.9000</td></tr><tr><td>A3</td><td>Enterprise content management</td><td>0.7556</td><td>0.9000</td></tr><tr><td>A4</td><td>Enterprise social software</td><td>0.8667</td><td>0.9667</td></tr><tr><td>A5</td><td>Knowledge base</td><td>1.0000</td><td>0.8333</td></tr><tr><td>A6</td><td>Knowledge engineering</td><td>0.7556</td><td>0.8667</td></tr><tr><td>A7</td><td>Knowledge market</td><td>0.9667</td><td>0.8667</td></tr><tr><td>A8</td><td>Social network</td><td>0.4778</td><td>1.0000</td></tr><tr><td>A9</td><td>Information ecology</td><td>0.9333</td><td>0.8667</td></tr><tr><td>A10</td><td>Information</td><td>0.9667</td><td>0.9667</td></tr><tr><td>A11</td><td>MIS</td><td>0.7889</td><td>0.8667</td></tr><tr><td>A12</td><td>Organizational learning</td><td>0.7889</td><td>0.7889</td></tr><tr><td>A13</td><td>Personal information management</td><td>0.7889</td><td>1.0000</td></tr><tr><td>A14</td><td>Personal knowledge management</td><td>1.0000</td><td>0.7333</td></tr><tr><td>A15</td><td>Social software</td><td>0.5889</td><td>1.0000</td></tr><tr><td>A16</td><td>Sociology of knowledge</td><td>0.5778</td><td>0.9667</td></tr><tr><td>A17</td><td>Strategic management</td><td>0.5889</td><td>1.0000</td></tr><tr><td colspan="2">Average precision</td><td>0.7980</td><td>0.9007</td></tr><tr><td colspan="2">Deviation</td><td>0.1647</td><td>0.0847</td></tr></table>

Note: Data in bold denotes the method has better result for the article.

Table 5b  
Average precision@PH rates for 17 articles under the Hybrid methods.

<table><tr><td rowspan="2">Relevantnovelty</td><td colspan="3">Hybrid(0.1)</td><td colspan="3">Hybrid(0.5)</td><td colspan="3">Hybrid(0.9)</td></tr><tr><td> $\alpha = 0.1$ </td><td> $\alpha = 0.5$ </td><td> $\alpha = 0.9$ </td><td> $\alpha = 0.1$ </td><td> $\alpha = 0.5$ </td><td> $\alpha = 0.9$ </td><td> $\alpha = 0.1$ </td><td> $\alpha = 0.5$ </td><td> $\alpha = 0.9$ </td></tr><tr><td>A1</td><td>0.9000</td><td>0.7889</td><td>0.7556</td><td>0.7556</td><td>0.6889</td><td>0.7556</td><td>0.7556</td><td>0.6889</td><td>0.7889</td></tr><tr><td>A2</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>A3</td><td>0.9667</td><td>0.9667</td><td>0.9667</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>A4</td><td>0.9667</td><td>0.9000</td><td>0.9000</td><td>0.6444</td><td>0.9000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>A5</td><td>0.7556</td><td>0.8333</td><td>0.7222</td><td>0.7556</td><td>0.8333</td><td>0.9000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>A6</td><td>0.9333</td><td>0.9667</td><td>0.9333</td><td>0.9667</td><td>0.9000</td><td>0.9000</td><td>0.7556</td><td>0.7556</td><td>0.9333</td></tr><tr><td>A7</td><td>0.9667</td><td>0.9667</td><td>0.9667</td><td>0.8667</td><td>0.8667</td><td>0.9667</td><td>0.4778</td><td>0.9000</td><td>0.9667</td></tr><tr><td>A8</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>0.7889</td><td>0.7889</td><td>0.7889</td><td>0.6889</td><td>0.6889</td><td>0.6889</td></tr><tr><td>A9</td><td>0.4444</td><td>0.7667</td><td>0.9333</td><td>0.4778</td><td>0.7222</td><td>0.9000</td><td>0.4778</td><td>0.6556</td><td>0.9333</td></tr><tr><td>A10</td><td>0.8000</td><td>0.9333</td><td>0.9667</td><td>0.9667</td><td>0.9667</td><td>0.9000</td><td>0.9667</td><td>1.0000</td><td>0.9667</td></tr><tr><td>A11</td><td>0.8667</td><td>0.8667</td><td>0.9000</td><td>0.9667</td><td>0.9667</td><td>1.0000</td><td>0.7556</td><td>0.7556</td><td>0.9333</td></tr><tr><td>A12</td><td>0.9000</td><td>0.9000</td><td>0.9667</td><td>0.7556</td><td>0.7889</td><td>0.7889</td><td>0.7556</td><td>0.7889</td><td>0.7889</td></tr><tr><td>A13</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>0.7889</td><td>0.9667</td><td>1.0000</td></tr><tr><td>A14</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>0.9667</td><td>0.9667</td><td>1.0000</td><td>0.9667</td><td>0.9667</td></tr><tr><td>A15</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>A16</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>0.6778</td><td>0.9000</td><td>0.9667</td><td>0.6778</td><td>0.6778</td><td>0.9667</td></tr><tr><td>A17</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>0.7889</td><td>0.9000</td><td>0.9667</td><td>0.9667</td><td>0.9667</td><td>0.9667</td></tr><tr><td>Average</td><td>0.9118</td><td>0.9346</td><td>0.9418</td><td>0.8477</td><td>0.8935</td><td>0.9294</td><td>0.8275</td><td>0.8712</td><td>0.9353</td></tr><tr><td></td><td>0.9294</td><td></td><td></td><td>0.8902</td><td></td><td></td><td>0.8780</td><td></td><td></td></tr><tr><td>Deviation</td><td>0.1418</td><td>0.0789</td><td>0.0839</td><td>0.1578</td><td>0.0997</td><td>0.0824</td><td>0.1813</td><td>0.1396</td><td>0.0914</td></tr></table>

Note: Data in bold denotes the highest recall of each method under different α values.

Discussion 2: The CP&FP method achieves a Precision@PH rate of 90.07% on average, as shown in Table 5a. Only 5 articles (out of 17 articles) have worse Precision@PH scores than those of the WF outperforming the WF method. Furthermore, the Precision@PH rate is less than 80% on only three articles. On four of the articles, the Precision@PH rate is 100% under the CP&FP method. The results show that using the CP&FP method to select keywords from the concept phrases (CP) and the <sup>fi</sup>rst paragraph (FP) of an article in Wikipedia is an effective way to generate an abstract of the article. Discussion 3: We conduct further experiments based on Eq. (6). First, we set the parameter λ to 0.1, 0.5, and 0.9 to test the importance of the component of WF. Second, based on Eq. (8), we set the parameter α to 0.1, 0.5, and 0.9 to test the importance of the novelty of sentences. Recall that the methods are called Hybrid(0.1), Hybrid(0.5) and Hybrid(0.9) based on the weight of the parameter λ. Table 5b shows that, overall, the Hybrid(0.1) method outperforms the other four methods. That is, the smaller the number of keywords selected under the WF method, the higher the Precision@PH rate the method will achieve.

Discussion 4: For the relevant novelty factor in Eq. (8), we found that the higher the weight of the parameter α, i.e., the number of similar sentences, the higher the precision rate it achieved, as shown in Table 5b. In terms of the Precision@PH rate, all three Hybrid methods outperform the WF and CP&FP methods when we consider the factor of relevant novelty slightly, i.e. α is set at 0.9.

## 7.1.2. The results based on the Precision@H metric

The Precision@H measurement is a stricter precision metric for evaluating the helpfulness of extracted sentences, as mentioned in Section 6.2. The compression rates are around 80% on average. We discuss the performance of each method below.

Discussion 1: The performance of the WF method, i.e., the weighted <sup>fi</sup>rst-paragraph overlap method, is worse than that of the CP&FP method in terms of the Precision@H metric, as shown in Table 6a. Discussion 2: The CP&FP method outperforms the WF method on nearly all the articles, i.e., 14 out of 17 articles, as shown in Table 6a. In other words the CP&FP method is more effective in extracting helpful sentences than the WF method.

Discussion 3: Table 6b shows that the Precision@H rates of the three Hybrid methods are better than that of the WF method. In addition, the smaller the number of keywords selected under the WF method, the higher the Precision@PH rate the method will achieve. Overall, the Hybrid(0.1) method outperforms the other four methods.

Discussion 4: For the relevant novelty factor in Eq. (8), we found that the higher the weight of the parameter α, i.e., the number of similar sentences, the higher the Precision@H rate achieved. In terms of the Precision@H rate, all three Hybrid methods outperform the WF and CP&FP methods when we consider the factor of relevant novelty slightly, i.e. α is set at 0.9.

## 7.1.3. The results based on the recall metric

Discussion 1: In terms of the recall rate, the CP&FP method outperforms the WF method, as shown in Table 7a.

Discussion 2: The Hybrid methods outperform the WF and CP&FP methods in terms of recall, as shown in Table 7b. Interestingly,

## Table 6a

Average precision@H rates for 17 articles under the WF and CP&FP methods

<table><tr><td>Article no.</td><td>Article title</td><td>WF</td><td>CP&amp;FP</td></tr><tr><td>A1</td><td>KM</td><td>0.5111</td><td>0.5111</td></tr><tr><td>A2</td><td>CSCW</td><td>0.4778</td><td>0.7333</td></tr><tr><td>A3</td><td>Enterprise content management</td><td>0.2778</td><td>0.4222</td></tr><tr><td>A4</td><td>Enterprise social software</td><td>0.5556</td><td>0.2778</td></tr><tr><td>A5</td><td>Knowledge base</td><td>0.5222</td><td>0.5222</td></tr><tr><td>A6</td><td>Knowledge engineering</td><td>0.6556</td><td>0.5889</td></tr><tr><td>A7</td><td>Knowledge market</td><td>0.5556</td><td>0.5889</td></tr><tr><td>A8</td><td>Social network</td><td>0.3444</td><td>0.5889</td></tr><tr><td>A9</td><td>Information ecology</td><td>0.2778</td><td>0.4889</td></tr><tr><td>A10</td><td>Information</td><td>0.2444</td><td>0.4222</td></tr><tr><td>A11</td><td>MIS</td><td>0.1333</td><td>0.8333</td></tr><tr><td>A12</td><td>Organizational learning</td><td>0.2778</td><td>0.4889</td></tr><tr><td>A13</td><td>Personal information management</td><td>0.2667</td><td>0.6667</td></tr><tr><td>A14</td><td>Personal knowledge management</td><td>0.4778</td><td>0.6333</td></tr><tr><td>A15</td><td>Social software</td><td>0.0000</td><td>0.4444</td></tr><tr><td>A16</td><td>Sociology of knowledge</td><td>0.2444</td><td>0.6556</td></tr><tr><td>A17</td><td>Strategic management</td><td>0.3111</td><td>0.2778</td></tr><tr><td>Average</td><td></td><td>0.3608</td><td>0.5379</td></tr><tr><td>Deviation</td><td></td><td>0.1732</td><td>0.1478</td></tr></table>

Note: Data in bold denotes the method has better result for the article.

Table 6b  
Average precision@H rates for 17 articles under the Hybrid methods.

<table><tr><td>Precision@H</td><td colspan="3">Hybrid(0.1)</td><td colspan="3">Hybrid(0.5)</td><td colspan="3">Hybrid(0.9)</td></tr><tr><td>Relevant novelty</td><td>α=0.1</td><td>α=0.5</td><td>α=0.9</td><td>α=0.1</td><td>α=0.5</td><td>α=0.9</td><td>α=0.1</td><td>α=0.5</td><td>α=0.9</td></tr><tr><td>A1</td><td>0.3778</td><td>0.5556</td><td>0.5889</td><td>0.6556</td><td>0.4778</td><td>0.5444</td><td>0.6222</td><td>0.4444</td><td>0.5444</td></tr><tr><td>A2</td><td>0.2333</td><td>0.7667</td><td>0.7667</td><td>0.5111</td><td>0.6889</td><td>0.7667</td><td>0.2000</td><td>0.4111</td><td>0.7667</td></tr><tr><td>A3</td><td>0.4111</td><td>0.4556</td><td>0.6556</td><td>0.4556</td><td>0.4556</td><td>0.5222</td><td>0.2333</td><td>0.3444</td><td>0.4444</td></tr><tr><td>A4</td><td>0.2444</td><td>0.2444</td><td>0.4889</td><td>0.2333</td><td>0.3778</td><td>0.4111</td><td>0.2333</td><td>0.3444</td><td>0.4111</td></tr><tr><td>A5</td><td>0.1667</td><td>0.2778</td><td>0.4444</td><td>0.1667</td><td>0.3444</td><td>0.6556</td><td>0.1667</td><td>0.1333</td><td>0.4111</td></tr><tr><td>A6</td><td>0.5889</td><td>0.8333</td><td>0.7667</td><td>0.5889</td><td>0.7667</td><td>0.7667</td><td>0.3111</td><td>0.3778</td><td>0.6222</td></tr><tr><td>A7</td><td>0.4778</td><td>0.6222</td><td>0.8667</td><td>0.1000</td><td>0.2778</td><td>0.6889</td><td>0.1333</td><td>0.2778</td><td>0.5889</td></tr><tr><td>A8</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.2778</td><td>0.3111</td><td>0.4222</td><td>0.2778</td><td>0.2778</td><td>0.5334</td></tr><tr><td>A9</td><td>0.2444</td><td>0.4889</td><td>0.6222</td><td>0.3444</td><td>0.5556</td><td>0.7000</td><td>0.3444</td><td>0.4556</td><td>0.5222</td></tr><tr><td>A10</td><td>0.2778</td><td>0.5222</td><td>0.4556</td><td>0.2667</td><td>0.4889</td><td>0.4889</td><td>0.3778</td><td>0.4889</td><td>0.4222</td></tr><tr><td>A11</td><td>0.5222</td><td>0.5222</td><td>0.5889</td><td>0.4111</td><td>0.5222</td><td>0.6222</td><td>0.3444</td><td>0.4556</td><td>0.6556</td></tr><tr><td>A12</td><td>0.3444</td><td>0.4889</td><td>0.4444</td><td>0.1667</td><td>0.0667</td><td>0.3444</td><td>0.1333</td><td>0.1333</td><td>0.3444</td></tr><tr><td>A13</td><td>0.7333</td><td>0.6667</td><td>0.5222</td><td>0.5889</td><td>0.6556</td><td>0.7000</td><td>0.3444</td><td>0.5889</td><td>0.8000</td></tr><tr><td>A14</td><td>0.6222</td><td>0.5889</td><td>0.6667</td><td>0.6889</td><td>0.6556</td><td>0.8000</td><td>0.4444</td><td>0.5889</td><td>0.7667</td></tr><tr><td>A15</td><td>0.2778</td><td>0.3111</td><td>0.5556</td><td>0.4889</td><td>0.5222</td><td>0.5222</td><td>0.4111</td><td>0.5222</td><td>0.6222</td></tr><tr><td>A16</td><td>0.4111</td><td>0.4444</td><td>0.7333</td><td>0.2333</td><td>0.4889</td><td>0.6889</td><td>0.1333</td><td>0.3778</td><td>0.6556</td></tr><tr><td>A17</td><td>0.4444</td><td>0.3778</td><td>0.3778</td><td>0.1333</td><td>0.3111</td><td>0.2778</td><td>0.4556</td><td>0.3444</td><td>0.3111</td></tr><tr><td>Average</td><td>0.4078</td><td>0.5131</td><td>0.5941</td><td>0.3712</td><td>0.4686</td><td>0.5837</td><td>0.3039</td><td>0.3863</td><td>0.5543</td></tr><tr><td></td><td>0.5050</td><td></td><td></td><td>0.4745</td><td></td><td></td><td>0.4148</td><td></td><td></td></tr><tr><td>Deviation</td><td>0.1594</td><td>0.1596</td><td>0.1354</td><td>0.1922</td><td>0.1755</td><td>0.1570</td><td>0.1355</td><td>0.1327</td><td>0.1493</td></tr></table>

Note: Data in bold denotes the highest recall of each method under different α values.

Hybrid(0.5) achieves the best recall performance. In addition, the lower the weight of the relevance novelty, the better will be the performance of the three Hybrid methods. This <sup>fi</sup>nding is in accordance with the results in terms of Precision@PH and Precision@H.

## 7.1.4. General discussions

To evaluate the CF, WF, Hybrid(0.1), Hybrid(0.5) and Hybrid(0.9) methods in terms of generating summaries of single articles, we selected 17 articles with high degree centrality in the topic network. We discuss each method's performance below.

Discussion 1: The First Paragraph (FP) and Cue Phrases (CP) are important components for generating the summaries of single articles. In addition, by including the weighted <sup>fi</sup>rst Paragraph (WF) and novelty analysis components to expand the corpus and select sentences, we can improve the text summarization results in terms of Precison@PH, Precision@H, and Recall, as shown in Fig. 9. The Hybrid methods clearly outperform the WF method and are slightly better than the CP&FP method.

Discussion 2: As shown in Table 4, the compression rates for Precison@PH and Precison@P are about 70% and 80% respectively. Fig. 9 shows that the precision rate drops signi<sup>fi</sup>cantly as the compression rate increases. Therefore, a 70% compression rate is a good threshold for generating informative summaries.

Discussion 3: The length of an article seems to be an important factor that in<sup>fl</sup>uences the recall results. Table 7b shows that the following <sup>fi</sup>ve articles yielded the worst recall rates: “A3: Enterprise content management,” “A8: Social network,” “A12: Organizational learning,” “A15: Social software,” and “A17: Strategic management.” The articles, which contain 6422, 3866, 2539, 4845, and 10,349 terms respectively, are the <sup>fi</sup>ve longest articles listed in Table 4. In the developed interface, we consider the compression rate to generate summaries for each article.

## 7.2. Intrinsic evaluation of multi-article summarization

In this part, we evaluate the quality of multi-article summaries. The articles in the topic network are grouped by the k-clique method of SNA. Based on our ongoing work, we set k at 3 to group the articles. We then merge the groups based on their similarity. Consequently, there are 14 groups for the topic “Knowledge Management” in Wikipedia, as shown in Table 8.

## 7.2.1. Evaluation procedure

In the intrinsic evaluation procedure for multi-article summaries, we begin by extracting keywords from the hub article (HA) and group articles (GAs), and construct the corpus for each subgroup of the KM topic. Then, we select the test articles to evaluate if they can be classi<sup>fi</sup>ed into the correct group of the KM topic network automatically. Two types of articles are selected: articles with the characteristics of the hub in the topic network, i.e, hub articles (HAs); and articles selected from each subgroup identi<sup>fi</sup>ed by the k-clique arti cles, i.e., group articles (GAs).

## 7.2.2. Evaluation results and discussions

Based on Eq. (11), we adjust the relative importance of β (beta), i.e., we adjust the proportion of keywords extracted from HAs and GAs to generate multi-article summaries. We calculate the precision (as described in Section 6.3) to evaluate the quality of the multiarticle summarization method. We observe some interesting

## Table 7a

Average recall rates for 17 articles under the WF and CP&FP methods.

<table><tr><td>Article no.</td><td>Article title</td><td>WF</td><td>CP&amp;FP</td></tr><tr><td>A1</td><td>KM</td><td>0.6667</td><td>0.6667</td></tr><tr><td>A2</td><td>CSCW</td><td>0.8333</td><td>0.6667</td></tr><tr><td>A3</td><td>Enterprise content management</td><td>0.3000</td><td>0.2000</td></tr><tr><td>A4</td><td>Enterprise social software</td><td>0.5714</td><td>0.4286</td></tr><tr><td>A5</td><td>Knowledge base</td><td>0.4286</td><td>0.5714</td></tr><tr><td>A6</td><td>Knowledge engineering</td><td>0.5556</td><td>0.5556</td></tr><tr><td>A7</td><td>Knowledge market</td><td>0.4444</td><td>0.5556</td></tr><tr><td>A8</td><td>Social network</td><td>0.2727</td><td>0.4545</td></tr><tr><td>A9</td><td>Information ecology</td><td>0.4000</td><td>0.8000</td></tr><tr><td>A10</td><td>Information</td><td>0.2857</td><td>0.2857</td></tr><tr><td>A11</td><td>MIS</td><td>0.5714</td><td>1.0000</td></tr><tr><td>A12</td><td>Organizational learning</td><td>0.3750</td><td>0.5000</td></tr><tr><td>A13</td><td>Personal information management</td><td>0.6667</td><td>0.4444</td></tr><tr><td>A14</td><td>Personal knowledge management</td><td>0.6250</td><td>0.5000</td></tr><tr><td>A15</td><td>Social software</td><td>0.0000</td><td>0.3333</td></tr><tr><td>A16</td><td>Sociology of knowledge</td><td>0.2500</td><td>0.6250</td></tr><tr><td>A17</td><td>Strategic management</td><td>0.4000</td><td>0.3000</td></tr><tr><td>Average</td><td></td><td>0.4498</td><td>0.5228</td></tr><tr><td>Deviation</td><td></td><td>0.2010</td><td>0.1981</td></tr></table>

Note: Data in bold denotes the method has better result for the article.

Table 7b  
Average recall rates for 17 articles under the Hybrid methods.

<table><tr><td>Recall</td><td colspan="3">Hybrid (0.1)</td><td colspan="3">Hybrid(0.5)</td><td colspan="3">Hybrid(0.9)</td></tr><tr><td>Relevant novelty</td><td>α=0.1</td><td>α=0.5</td><td>α=0.9</td><td>α=0.1</td><td>α=0.5</td><td>α=0.9</td><td>α=0.1</td><td>α=0.5</td><td>α=0.9</td></tr><tr><td>A1</td><td>0.6667</td><td>0.6667</td><td>0.5556</td><td>0.7778</td><td>0.7778</td><td>0.7778</td><td>0.6667</td><td>0.6667</td><td>0.7778</td></tr><tr><td>A2</td><td>0.8333</td><td>0.8333</td><td>0.8333</td><td>1.0000</td><td>1.0000</td><td>0.8333</td><td>0.6667</td><td>0.8333</td><td>0.8333</td></tr><tr><td>A3</td><td>0.3000</td><td>0.3000</td><td>0.5000</td><td>0.3000</td><td>0.3000</td><td>0.5000</td><td>0.3000</td><td>0.3000</td><td>0.4000</td></tr><tr><td>A4</td><td>0.2857</td><td>0.2857</td><td>0.5714</td><td>0.4286</td><td>0.5714</td><td>0.7143</td><td>0.4286</td><td>0.4286</td><td>0.4286</td></tr><tr><td>A5</td><td>0.4286</td><td>0.4286</td><td>0.5714</td><td>0.4286</td><td>0.4286</td><td>0.7143</td><td>0.4286</td><td>0.5714</td><td>0.7143</td></tr><tr><td>A6</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.4444</td><td>0.4444</td><td>0.4444</td></tr><tr><td>A7</td><td>0.5556</td><td>0.6667</td><td>0.6667</td><td>0.3333</td><td>0.3333</td><td>0.6667</td><td>0.4444</td><td>0.3333</td><td>0.5556</td></tr><tr><td>A8</td><td>0.3636</td><td>0.3636</td><td>0.3636</td><td>0.2727</td><td>0.1818</td><td>0.1818</td><td>0.2727</td><td>0.2727</td><td>0.1818</td></tr><tr><td>A9</td><td>0.4000</td><td>0.4000</td><td>0.8000</td><td>0.6000</td><td>0.8000</td><td>1.0000</td><td>0.6000</td><td>0.6000</td><td>0.6000</td></tr><tr><td>A10</td><td>0.4286</td><td>0.4286</td><td>0.4286</td><td>0.5714</td><td>0.5714</td><td>0.5714</td><td>0.5714</td><td>0.5714</td><td>0.2857</td></tr><tr><td>A11</td><td>0.7143</td><td>0.7143</td><td>0.7143</td><td>0.7143</td><td>0.7143</td><td>0.8571</td><td>0.4286</td><td>0.4286</td><td>0.7143</td></tr><tr><td>A12</td><td>0.3750</td><td>0.5000</td><td>0.5000</td><td>0.3750</td><td>0.2500</td><td>0.3750</td><td>0.2500</td><td>0.2500</td><td>0.3750</td></tr><tr><td>A13</td><td>0.4444</td><td>0.4444</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.5556</td><td>0.6667</td></tr><tr><td>A14</td><td>0.7500</td><td>0.8750</td><td>0.7500</td><td>0.7500</td><td>0.6250</td><td>0.6250</td><td>0.7500</td><td>0.6250</td><td>0.6250</td></tr><tr><td>A15</td><td>0.2500</td><td>0.3333</td><td>0.3333</td><td>0.3333</td><td>0.4167</td><td>0.4167</td><td>0.4167</td><td>0.4167</td><td>0.5000</td></tr><tr><td>A16</td><td>0.6250</td><td>0.6250</td><td>0.7500</td><td>0.6250</td><td>0.5000</td><td>0.7500</td><td>0.5000</td><td>0.5000</td><td>0.6250</td></tr><tr><td>A17</td><td>0.4000</td><td>0.4000</td><td>0.4000</td><td>0.3000</td><td>0.3000</td><td>0.4000</td><td>0.2000</td><td>0.3000</td><td>0.4000</td></tr><tr><td>Average</td><td>0.4927</td><td>0.5189</td><td>0.5794</td><td>0.5248</td><td>0.5224</td><td>0.6173</td><td>0.4661</td><td>0.4763</td><td>0.5369</td></tr><tr><td></td><td>0.5303</td><td></td><td></td><td>0.5548</td><td></td><td></td><td>0.4931</td><td></td><td></td></tr><tr><td>Deviation</td><td>0.1740</td><td>0.1823</td><td>0.1528</td><td>0.2054</td><td>0.2194</td><td>0.2053</td><td>0.1560</td><td>0.1602</td><td>0.1803</td></tr></table>

Note: Data in bold denotes the highest recall of each method under different α values.

![](/api/attachments/E2992NUJ/fulltext/images/784c01d05aae278729573d3b218b78fd54afce8960eed3941209d998a2a281d8.jpg)  
Fig. 9. Comparison of summarization methods in terms of various metrics.

phenomena: (1) Fig. 10 shows that under P@1, P@2, and P@3, the HAs can be classi<sup>fi</sup>ed into the correct subgroups, especially β is set at 0.3. (2) Fig. 10 shows that the GAs are classi<sup>fi</sup>ed accurately by the P@3 metric, but the performance of the P@1 metric is poor. (3) To classify GAs setting β at 0.5 yields a better performance than setting β at 0.7 on average. The results indicate that selecting more keywords from the group articles does not improve the classi<sup>fi</sup>cation result.

## 7.3. Extrinsic evaluation I: Classification tasks for multi-article summarization

For extrinsic evaluation, we invited <sup>fi</sup>ve users, graduate students who have majored in Information Management, to classify the summaries into the correct subgroups. We constructed a preliminary interface, i.e., WNavi<sup>S</sup> (shown in Fig. 8(b)), to help the users execute the classi<sup>fi</sup>- cation task.

## 7.3.1. Evaluation tasks and procedure

Each participant was assigned 14 multi-article summaries (i.e., S1–S14), which were generated from 14 subgroups of the KM topic.

After reading the summaries, the participants were asked to classify them into the correct subgroups. Each participant could select at most three subgroups.

## 7.3.2. Evaluation results and discussions

The classi<sup>fi</sup>cation task results are in terms of precision, i.e., P@1, P@2, and P@3, to evaluate the performance of the extrinsic evaluation method. The last column is the correct group of the target summary. Table 9 shows the precision of the evaluation results. There is very little difference between P@1, P@2, and P@3 for the classi<sup>fi</sup>cation task. The P@3 metric can achieve 0.80 precision. User 3 even achieved 0.93 precision under P@3. We interviewed the users after they <sup>fi</sup>nished the experiment. Overall, they felt that the given summaries provided enough information for them to understand the contents of each subgroup. Thus, we can infer that the quality of the summaries is good enough for users to <sup>fi</sup>nd the proper topics and understand the content of each topic.

Number of articles in each subgroup for the “KM” topic.

<table><tr><td>Group no.</td><td>Numbers of articles</td><td>Group no.</td><td>Numbers of articles</td></tr><tr><td>G1</td><td>28</td><td>G8</td><td>10</td></tr><tr><td>G2</td><td>18</td><td>G9</td><td>6</td></tr><tr><td>G3</td><td>8</td><td>G10</td><td>24</td></tr><tr><td>G4</td><td>8</td><td>G11</td><td>12</td></tr><tr><td>G5</td><td>8</td><td>G12</td><td>24</td></tr><tr><td>G6</td><td>13</td><td>G13</td><td>5</td></tr><tr><td>G7</td><td>12</td><td>G14</td><td>33</td></tr></table>

Intrinsic Evaluation Results  
![](/api/attachments/E2992NUJ/fulltext/images/7b593a086db3ef51262f89855d72d37a95c85cc119d341cb6b319ae8aeb9a856.jpg)  
Fig. 10. Precision of intrinsic evaluation results.

7.4. Extrinsic evaluation II: Simulated search tasks for multi-article summarization

## 7.4.1. Evaluation tasks and procedure

Twenty students in the Department of Information Management at Fu-Jen Catholic University (Taipei) performed the search tasks during the experiment. We used three criteria to select appropriate participants: 1) each participant's English pro<sup>fi</sup>ciency was above average; 2) they knew about or had used Wikipedia; and 3) they were interested in the given tasks and have taken the course called “Knowledge Management” [4,5]. In a previous test, we found that people's experience in using Wikipedia did not in<sup>fl</sup>uence their perception of different kinds of interface. Accordingly, their language ability was the major consideration when we selected participants from the volunteer pool. It is not easy to conduct a task-oriented evaluation of many cases at the same time because the process takes around thirty to forty minutes, and includes a tutorial, evaluation and follow-up questionnaire.

For the task design, all the search questions are related to Knowledge Management (KM). We want to evaluate if the participants can use the proposed interface, WNavi<sup>s</sup>, to <sup>fi</sup>nd more precise answers than those derived via the traditional Wikipedia interface. Table 10 shows the instructions given to the participants for the completion of simulated KM search tasks for four questions. The 20 participants executed the tasks on the provided interfaces. Since all the participants had taken the “Knowledge Management” course, the dif<sup>fi</sup>culty of the tasks was similar. Each participant was asked to select two tasks from the task set for each interface, i.e., the basic Wikipedia interface and our WNavi<sup>s</sup> interface in each phase. In phase 1, each user performed two search tasks randomly via Interface A or Interface B. In phase 2, the participants executed one of the tasks on interface A and the other task on interface B. The effectiveness of the two interfaces is measured in terms of the precision metric.

Average precision of the evaluation results.

<table><tr><td></td><td>P@1</td><td>P@2</td><td>P@3</td></tr><tr><td>User1</td><td>0.71</td><td>0.71</td><td>0.71</td></tr><tr><td>User2</td><td>0.86</td><td>0.86</td><td>0.86</td></tr><tr><td>User3</td><td>0.86</td><td>0.93</td><td>0.93</td></tr><tr><td>User4</td><td>0.71</td><td>0.79</td><td>0.86</td></tr><tr><td>User5</td><td>0.64</td><td>0.64</td><td>0.64</td></tr><tr><td>Average precision</td><td>0.76</td><td>0.79</td><td>0.80</td></tr></table>

## 7.4.2. Evaluation results and discussions

7.4.2.1. Task-oriented evaluation results. We calculate the participants precision rates for the simulated task. Table 11 shows the precision rates for two interfaces.

Discussion 1: The participants achieved higher precision rates on the WNavi<sup>s</sup> interface, i.e., 0.72 for four questions on average.

Discussion 2: For task 1, the precision rate on WNavi<sup>s</sup> was slightly better than that on the Wikipedia interface. Interestingly, four participants answered all the questions correctly on WNavi<sup>s</sup>; however, only one participant achieved the same result on the Wikipedia interface.

Discussion 3: Table 11 shows that the users achieved far better performances on WNavi<sup>s</sup> for task 2, task 3, and task 4. Speci<sup>fi</sup>cally, for task 4, eight of the ten participants gave the correct answers on the WNavi<sup>s</sup> interface; however, only two of the ten participants gave the correct answers on the Wikipedia interface.

Discussion 4: It seems that the participants had dif<sup>fi</sup>culty answering the question that had only one answer, i.e., task 3, nine of the ten participants could not <sup>fi</sup>nd the answer through the Wikipedia interface.

7.4.2.2. Follow-up questionnaire. We asked the participants to describe their experiences when they used the two interfaces to perform the assigned tasks. Each user selected a response on a 5-point Likert scale, i.e., 5-points from strongly agree (5) to strongly disagree (1). The six items in the questionnaire are listed in Table 12; and the results of the two groups of users are shown in Table 13. Overall, the participants were more satis<sup>fi</sup>ed with the WNavi<sup>s</sup> interface than the basic Wikipedia interface, as shown by the higher average scores for WNavi<sup>s</sup> in Table 13. Clearly, the WNavi<sup>s</sup> interface helps users gain a clear view of the topics related to the main query. The users pointed out that the topic network and summaries helped them <sup>fi</sup>nd related information for the assigned task. In addition, the users felt that they would not get lost and they could browse articles in Wikipedia easily with the aid of the hierarchy tree and topic network presented in the interface.

Simulated search task for the “Knowledge Management” topic

<table><tr><td>Please use interface A and interface B to complete the search tasks. The time limit for each task is five minutes. Note that you should write down the answer and copy the hyperlink of the answer.</td></tr><tr><td>Q1.Who has published papers in the Harvard Business Review, or been affiliated with the Harvard Business School?Q2. What are the metrics used in Social network analysis?Q3. Who first coined the terms of tacit knowledge and explicit knowledge?Q4: Chris Argyris and another researcher jointly proposed the concept of the Double-Loop Learning? What was the name of the other researcher?</td></tr></table>

Table 11  
Precision rates of participants for the simulated KM tasks.

<table><tr><td rowspan="2"></td><td colspan="4">Basic Wikipedia (interface A)</td><td rowspan="2"></td><td colspan="4"> $WNavi^s$ (interface B)</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td></tr><tr><td>User-1</td><td>0.75</td><td>0.27</td><td>1.00</td><td>1.00</td><td>User-1</td><td>0.25</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>User-2</td><td>0.66</td><td>0.57</td><td>0.00</td><td>0.50</td><td>User-2</td><td>0.27</td><td>0.00</td><td>0.50</td><td>1.00</td></tr><tr><td>User-3</td><td>0.25</td><td>0.40</td><td>0.00</td><td>0.00</td><td>User-3</td><td>0.33</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>User-4</td><td>0.24</td><td>0.19</td><td>0.00</td><td>0.25</td><td>User-4</td><td>1.00</td><td>1.00</td><td>0.00</td><td>0.00</td></tr><tr><td>User-5</td><td>0.25</td><td>0.44</td><td>0.00</td><td>0.50</td><td>User-5</td><td>0.14</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>User-6</td><td>1.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>User-6</td><td>1.00</td><td>0.75</td><td>1.00</td><td>1.00</td></tr><tr><td>User-7</td><td>0.60</td><td>0.09</td><td>0.00</td><td>0.00</td><td>User-7</td><td>0.50</td><td>0.50</td><td>1.00</td><td>1.00</td></tr><tr><td>User-8</td><td>0.30</td><td>0.36</td><td>0.00</td><td>0.00</td><td>User-8</td><td>0.30</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>User-9</td><td>0.33</td><td>0.20</td><td>0.00</td><td>1.00</td><td>User-9</td><td>1.00</td><td>0.75</td><td>1.00</td><td>0.00</td></tr><tr><td>User-10</td><td>0.27</td><td>0.19</td><td>0.00</td><td>0.00</td><td>User-10</td><td>1.00</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>Average precision</td><td>0.47</td><td>0.37</td><td>0.10</td><td>0.33</td><td></td><td>0.58</td><td>0.75</td><td>0.45</td><td>0.80</td></tr><tr><td> $Correct^a$ </td><td>1</td><td>1</td><td>1</td><td>2</td><td></td><td>4</td><td>5</td><td>4</td><td>8</td></tr><tr><td>Overall precision</td><td>0.43</td><td></td><td></td><td></td><td></td><td>0.72</td><td></td><td></td><td></td></tr></table>

<sup>a</sup> Denotes the number of participants who completed all the tasks correctly.

## 8. Conclusion and future work

Wikipedia, the largest multi-lingual online encyclopedia, allows users to contribute their knowledge as members of a Wiki community; thus, the number of articles in Wikipedia is constantly expanding. In this study, we propose an SNA-based summarization technique and develop a navigation interface called WNavi<sup>s</sup> to help Wikipedia users <sup>fi</sup>nd and organize needed information or topics. First, we employ the NGD algorithm in the proposed LS measure to quantify the strength of the semantic relationships between articles in the topic network. Our evaluation results demonstrate the effectiveness of applying semantic analysis in an internal link-based network. To help users read topic-related articles, we propose SNA-based single and multi-article summarization techniques and then construct the WNavi<sup>s</sup> interface. To summarize articles, we exploit three features, namely, Weighted First Paragraph Overlap (WF), First Paragraph (FP) and Concept Phrase (CP), to extract keywords, select sentences, and then generate the summaries. In addition, we propose <sup>fi</sup>ve methods: the WF, CP&FP, Hybrid(0.1), Hybrid(0.5) and Hybrid(0.9) methods. The widely adopted intrinsic and extrinsic evaluation methods in text summarization are employed to evaluate the ef<sup>fi</sup>cacy of the techniques in terms of precision, and recall. For the single article summarization technique, we found that the keywords extracted from CP and FP features are much more important than those extracted from the WF feature. Moreover, adding some keywords extracted from the WF feature can improve the evaluation results. For the intrinsic multi-article summarization method, we found that the hub article can be classi<sup>fi</sup>ed into the subgroup correctly. For the extrinsic multi-article summarization technique, <sup>fi</sup>ve evaluators used the proposed WNavi<sup>s</sup> interface to classify the summaries into the correct subgroups. The evaluation results con-<sup>fi</sup>rm that the proposed SNA-based single and multi-article summarization techniques are effective. We also simulated a task's execution to evaluate the usefulness of the proposed WNavi<sup>s</sup> interface. The results

## Table 12

The questionnaire completed after the interface evaluation.

Table 13  
Users' satisfaction with the two interfaces

<table><tr><td rowspan="2">Questions</td><td colspan="2">Basic Wikipedia (interface A)</td><td colspan="2"> $WNavi^s$ (interface B)</td></tr><tr><td>Avg.</td><td>Sdv.</td><td>Avg.</td><td>Sdv.</td></tr><tr><td>Q1</td><td>2.60</td><td>1.07</td><td>4.30</td><td>0.67</td></tr><tr><td>Q2</td><td>2.50</td><td>0.97</td><td>4.00</td><td>0.47</td></tr><tr><td>Q3</td><td>2.50</td><td>1.65</td><td>4.20</td><td>0.79</td></tr><tr><td>Q4</td><td>2.40</td><td>1.17</td><td>4.20</td><td>0.79</td></tr><tr><td>Q5</td><td>2.10</td><td>1.29</td><td>4.00</td><td>0.94</td></tr><tr><td>Q6</td><td>2.20</td><td>1.03</td><td>4.30</td><td>0.48</td></tr></table>

Note: Data in bold denotes the interface has better result in each question

show that the interface can help users accomplish assigned tasks easily and obtain topic related information. In summary, the main contribution of this work is that the proposed techniques can be generalized to applications of navigation support tools in an internal link-based knowledge intensive website to help users <sup>fi</sup>nd information easily.

We should acknowledge the limitations of this study and indicate the direction of our future work. The proposed framework is not computationally ef<sup>fi</sup>cient when the degree of the topic network is more than three because it requires a lot of computing power for topic network expansion. Second, for the extrinsic evaluation tasks in Sections 7.3 and 7.4, the participants accomplished the tasks with the aid of the WNavi<sup>s</sup> interface. We will assess the utility of each module in the interface by the user experience capture, observe and record software. Speci<sup>fi</sup>cally, we will incorporate a user behavior tracking mechanism into the proposed framework to getting a through analyzing. Then, we will re<sup>fi</sup>ne the interface based on the user navigation behavior to provide a better human computer interaction experience. In addition, we will evaluate the outputs and outcomes of the proposed interface [40]. The outputs are the products delivered by the interface, and the outcomes are the bene<sup>fi</sup>ts the interface provides to the user. The concepts are discussed in interactive exploratory search to help users achieve their search goals with the help of the interface or system [30,40]. Furthermore, because of the popularity and importance of handheld devices, we will investigate summarization techniques, visualization techniques and interface designs for extracting subject knowledge from Wikipedia [46]. We will also evaluate the effectiveness of the proposed application on different devices in real-world settings to help knowledge workers and students search for, explore, and learn new concepts.

## Acknowledgments

We thank the editor-in-chief, and the anonymous reviewers for their constructive comments. We also thank Prof. Pertti Vakkari at the University of Tampere for helpful comments.

This research was supported by the National Science Council of Taiwan under Grant No. 99-2410-H-030-047-MY3.

## References

[1] G. Almpanidis, C. Kotropoulos, I. Pitas, Combining text and link analysis for focused crawling—an application for vertical search engines, Information Systems 32 (6) (2007) 886–908.

[2] O. Alonso, R. Baeza-Yates, Design and implementation of relevance assessments using crowdsourcing, Proceedings of the 33rd European Conference on Information Retrieval (ECIR 2011) Ireland 2011 pp. 53–164

[3] A. Bavelas, A mathematical model of group structures, Human Organization 7 (3) (1948) 16–30.

[4] P. Borlund, The IIR evaluation model: a framework for evaluation of interactive information retrieval systems, Information Research 8 (3) (2003) Retrieved June 30, 2011, from http://informationr.net/ir/8-3/paper152.html.

[5] P. Borlund, J.W. Schneider, Reconsideration of the simulated work task situation: a context instrument for evaluation of information retrieval interaction, Proceeding of the Third Symposium on Information Interaction in Context 2010 (IliX 2010), New Brunswick New Jersey USA 2010 pp. 155–164

[6] S. Brin, L. Page, The anatomy of a large-scale hypertextual web search engine, Computer Network 30 (1-7) (1998) 107-117.

[7] J. Callan, J. Allan, C.L.A. Clarke, S. Dumais, D.A. Evans, M. Sanderson, C.X. Zhai, Meeting of the MINDS: an information retrieval research agenda, Forum of the 30th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR'07 Forum), 41 (2, 2007, pp. 25–34, Retrieved December 30, 2011, from http://dx.doi.org/10.1145/1328964.1328967.

[8] M.H. Chehreghani, H. Abolhassani, M.H. Chehreghani, Density link-based methods for clustering web pages, Decision Support Systems 47 (4) (2009) 374–382.

[9] H. Chen, H. Fan, M. Chau, D. Zeng, MetaSpider: meta-searching and categorization on the web, Journal of the American Society for Information Science 52 (13) (2001) 1134–1147.

[10] R.L. Cilibrasi, P.M.B. Vitányi, Automatic extraction of meaning from the Web, Proceeding of IEEE International Symposium on Information Theory (ISIT 2006), Washington USA, 2006, pp. 2309–2313.

[11] R.L. Cilibrasi, P.M.B. Vitányi, The Google similarity distance, IEEE Transactions on Knowledge and Data Engineering 19 (3) (2007) 370–383.

[12] W.B. Croft, What do people want from information retrieval? D-Lib MagazineRetrieved June 30, 2011, from http://mirrored.ukoln.ac.uk/lis-journal/dlib/dlib/ dlib/novermber95/11croft.html1995.

[13] A. Doan, R. Ramakrishnan, A.Y. Halevy, Crowdsourcing systems on the World-Wide Web, Communications of the ACM 54 (4) (2011) 86–96.

[14] A.J. Evangelista, B. Kjos-Hanssen, Google Distance between Words. Frontiers in Undergraduate Research, University of Connecticut, 2006.

[15] L. Finkelstein, E. Gabrilovich, Y. Matias, E. Rivlin, Z. Solan, G. Wolfman, E. Ruppin, Placing search in context: the concept revisited, ACM Transactions on Information Systems (TOIS) 20 (1) (2002) 116–131.

[16] R. Forsyth, R. Rada, Adding an Edge, in Machine Learning: Applications in Expert Systems and Information Retrieval, Ellis Horwood Ltd, 1986, pp. 198–212.

[17] L.C. Freeman, A set of measures of centrality based on betweenness, Sociometry 40 (1) (1977) 35–41.

[18] L.C. Freeman, Centrality in social networks: conceptual clari<sup>fi</sup>cation, Social Networks 1 (3) (1979) 215–239.

[19] T. Fukusima, M. Okumura, Text summarization challenge: text summarization evaluation at NTCIR Workshop2, Proceedings of the Second NTCIR Workshop on Research in Chinese & Japanese Text Retrieval and Text Summarization, Osaka, Japan, 2001, Retrieved June 30, 2011, from http://research.nii.ac.jp/ ntcir/workshop/OnlineProceedings2/fukushima.pdf.

[20] D. Ganley, C. Lampe, The ties that bind: social network principles in online communities, Decision Support Systems 47 (3) (2009) 266–274.

[21] J. Goldstein, V.O. Mittal, J.G. Carbonell, J.P. Callan, Creating and evaluating multi-document sentence extract summaries, Proceedings of the Ninth International Conference on Information and Knowledge Management (CIKM 2000), Washington, DC, USA, 2000, pp. 165–172.

[22] U. Hahn, I. Mani, The challenges of automatic summarization, Journal of IEEE Computer 33 (11) (2000) 29–36.

[23] K.S. Jones, J.R. Galliers, Evaluating Natural Language Processing Systems: An Analysis and Review, Springer, New York, 1996.

[24] S.M. Katz, Distribution of content words and phrases in text and language modelling, Natural Language Engineering 2 (1) (1996) 15–59

[25] D. Kelly, Methods for evaluating interactive information retrieval systems with users, Foundations and Trends in Information Retrieval 3 (1–2) (2009) 1–224, http://dx.doiorg/10.1561/1500000012

[26] J.M. Kleinberg, Authoritative sources in a hyperlinked environment, Proceedings of the 9th Annual ACM-SIAM Symposium on Discrete Algorithms (SODA'98), San Francisco, California, USA, 1998, pp. 668–677.

[27] C.Y. Lin, E. Hovy, Identifying topic by position, Proceedings of the 5th Conference on Applied Natural Language Processing (ANLP'97), Washington, DC, 1997, pp. 283–290.

[28] B. Liu, Web Data Mining: Exploring Hyperlinks, Contents and Usage Data, <sup>fi</sup>rst ed Springer Verlag, New York, 2007.

[29] M. Ljosland, Evaluation of Web search engines and the search for better ranking algorithms, ACM Conference on Research and Development in Information Retrieval (SIGIR'99) Workshop on Evaluation of Web Retrieval, California, USA, 1999, Available at: http://www-nlpir.nist.gov/related\_projects/tipster/ (accessed 30 June 2011).

[30] G. Marchionini, Exploratory search, Communications of the ACM 49 (4) (2006) 41–46.

[31] D.M. McDonald, H.C. Chen, Summary in context: searching versus browsing, Journal of Transactions on Information Systems (TOIS) 24 (1) (2006) 111–141.

[32] D. Milne, I.H. Witten, Learning to link with Wikipedia, Proceedings of the ACM Conference on Information and Knowledge Management (CIKM'2008), Napa Valley, California, 2008, pp. 509–518.

[33] J. Niemincn, On centrality in a graph, Scandinavian Journal of Psychology 15 (1) (1974) 322–336

[34] L. Page, S. Brin, R. Motwani, T. Winograd, The pagerank citation ranking: bringing order to the webRetrieved June 30, 2011, from http://dbpubs.stanford.edu:8090 pub/1999-661998.

[35] D.R. Radev, H. Jing, M. Styś, D. Tam, Centroid-based summarization of multiple documents, Journal of Information Processing and Management 40 (6) (2004) 919–938.

[36] J.E. Rush, R. Salvador, A. Zamora, Automatic abstracting and indexing. II. Production of indicative abstracts by application of contextual inference and syntactic coherence criteria, Journal of the American Society for Information Science 22 (4) (1971) 260–274.

[37] G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, McGrawHill Book Co., New York, 1983

[38] J.P. Scott, Social Network Analysis: A Handbook, second edition SAGE Publications Ltd, London, 2000.

[39] S. Teufel, M. Moens, Sentence extraction as a classi<sup>fi</sup>cation task, Proceedings of the Workshop on Intelligent Scalable Summarization, ACL/EACL Conference, Madrid, Spain, 1997, pp. 58–65.

[40] P. Vakkari, Exploratory searching as conceptual exploration, Proceedings of the 4th Workshop on HCIR, New Brunswick, N.J, 2010, pp. 24–27.

[41] J. Vegas, F. Crestani, P.D.L. Fuente, Context representation for web search results, Journal of Information Science 33 (1) (2007) 77–94.

[42] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, <sup>fi</sup>rst edition Cambridge University Press, New York and Cambridge, ENG, 1994.

[43] R.W. White, P. Bailey, L. Chen, Predicting user interests from contextual information, Proceedings of the 32nd international ACM SIGIR conference on Research and Development in Information Retrieval (SIGIR'09) Boston, Massachusetts USA, 2009, pp. 363–370.

[44] I.H. Witten, A. Moffat, T.C. Bell, Managing Gigabytes: Compressing and Indexing Documents and Images, Morgan Kaufmann Publishers, Los Alto, USA, 1999.

[45] I.C. Wu, C.Y. Wu, Using internal link and social network analysis to support searches in Wikipedia: model and evaluation Journal of Information Science 37 (2) (2011) 189–207.

[46] C.C. Yang, F.L. Wang, An information delivery system with automatic summarization for mobile commerce, Decision Support Systems 43 (1) (2007) 46–61.

I-Chin Wu received a Ph.D. in Information Management from National Chiao Tung University, Taiwan in January 2006. Since 2006 she has been with the Department of Information Management. Fu-Ien Catholic University. Taipei. Taiwan, where she is currently an Associate Professor. She has been a visiting scholar in the School of Information Science, University of Tampere, Finland in 2011. Her research interests are mainly focused on Information Search and Retrieval, Knowledge Management and Web Mining. Her recent research has appeared in Decision Support Systems, Journal of the American Society for Information Science and Technology, Information Processing and Management, and Journal of Documentation

Yi-Sheng Lin received her BBA and MS in Department of Information Management from Fu-Jen Catholic University, Taipei, Taiwan in 2009 and 2011 respectively. His research interests are mainly focused on Information Retrieval, and Web Mining
