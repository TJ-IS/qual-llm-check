---
otero_id: 12226
otero_key: "QJC2MWED"
title: "ExpertRank: A topic-aware expert finding algorithm for online knowledge communities"
authors: "G. Alan Wang; Jian Jiao; Alan S. Abrahams; Weiguo Fan; Zhongju Zhang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.020"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# ExpertRank: A topic-aware expert <sup>fi</sup>nding algorithm for online knowledge communities

G. Alan Wang <sup>a,</sup>⁎, Jian Jiao <sup>b</sup>, Alan S. Abrahams <sup>a</sup>, Weiguo Fan <sup>c,e</sup>, Zhongju Zhang

<sup>a</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Tech, 1007 Pamplin Hall, Blacksburg, VA 24061, United States

<sup>b</sup> Department of Computer Science, Virginia Tech, 114 McBryde Hall, Blacksburg, VA 24061, United States

<sup>c</sup> Department of Accounting and Information Systems, Pamplin College of Business, Virginia Tech, 3007 Pamplin Hall, Blacksburg, VA 24061, United States

<sup>d</sup> Operations and Information Management Department, School of Business, University of Connecticut, 2100 Hillside Road, Unit 1041, Storrs, CT 06269, United States

<sup>e</sup> School of Information, Zhejiang University of Finance and Economics, Hang Zhou, 310018, P.R. China

## a r t i c l e i n f o

Article history: Received 13 April 2012 Received in revised form 26 October 2012 Accepted 9 December 2012 Available online 4 January 2013

Keywords: Expert <sup>fi</sup>nding Online community Ranking Vector space model Social network analysis Social media analytics

## a b s t r a c t

With increasing knowledge demands and limited availability of expertise and resources within organizations, professionals often rely on external sources when seeking knowledge. Online knowledge communities are Internet based virtual communities that specialize in knowledge seeking and sharing. They provide a virtual media environment where individuals with common interests seek and share knowledge across time and space. A large online community may have millions of participants who have accrued a large knowledge repository with millions of text documents. However, due to the low information quality of user-generated content, it is very challenging to develop an effective knowledge management system for facilitating knowledge seeking and sharing in online communities. Knowledge management literature suggests that effective knowledge management should make accessible not only written knowledge but also experts who are a source of information and can perform a given organizational or social function. Existing expert <sup>fi</sup>nding systems evaluate one's expertise based on either the contents of authored documents or one's social status within his or her knowledge community. However, very few studies consider both indicators collectively. In addition, very few studies focus on virtual communities where information quality is often poorer than that in organizational knowledge repositories. In this study we propose a novel expert <sup>fi</sup>nding algorithm, ExpertRank, that evaluates expertise based on both document-based relevance and one's authority in his or her knowledge community. We modify the PageRank algorithm to evaluate one's authority so that it reduces the effect of certain biasing communication behavior in online communities. We explore three different expert ranking strategies that combine document-based relevance and authority: linear combination, cascade ranking, and multiplication scaling. We evaluate ExpertRank using a popular online knowledge community. Experiments show that the proposed algorithm achieves the best performance when both document-based relevance and authority are considered.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due to increasing knowledge demands and the limited availability of expertise and resources within an organization, professionals often seek knowledge from external sources such as the Internet for problem solving, especially in the information technology (IT) industry where <sup>fi</sup>nding the current best solution is dif<sup>fi</sup>cult [12,52,59]. Online knowledge communities (KCs) are among the most popular and effective of such sources.

KCs are a special type of networks of practice [8,51], specializing in knowledge sharing and seeking. They are composed of individuals who share common interests and voluntarily work together to expand their understanding of a knowledge domain through learning and sharing [31–33]. KCs rely on cooperating members as primary resources, who collaboratively share knowledge and help build a community knowledge repository. They provide a virtual media environment where individuals may seek and share knowledge across time and space. The technologies supporting KCs have evolved from traditional listservs and newsgroups into more advanced Web-based discussion forums and interactive communication systems that are rich in social media. The number of registered members in KCs is also growing rapidly. For example, big-boards.com ranks some of the largest online discussion forums that are implemented using non-proprietary discussion forum platforms. As of October 2012, big-boards listed 186 forums with more than 10 million posts and 1753 forums with more than 1 million posts. Many of the large forums discuss topics such as electronics, automobiles, mechanical equipment, software, healthcare, and sports and gaming. For example, one of the largest IT-related KCs, experts-exchange.com, has attracted more than 10,000 active experts, and more than 3.8 million registered members. Together, these knowledge seekers and experts have contributed more than 16 million postings related to IT solutions since 1996. Many large companies – e.g., Dell (“Dell Community”), Microsoft (“Microsoft Developer Network Forums”; “Microsoft Of<sup>fi</sup>ce Discussion Groups”), TurboTax (“Turbotax Live Community”), Amazon (“Amazon Web Service Discussion Forums”), and others – also run vast, proprietary internal KCs for both their employees and customers for self-service technical support [39,53].

Knowledge management literature suggests that an effective knowledge management solution should make accessible not only written knowledge but also experts who are a source of information and can perform a given organizational or social function [58]. Expert <sup>fi</sup>nding systems, also known as expertise <sup>fi</sup>nding systems or expert recommender systems, are an important tool for KCs to make individuals with sought knowledge accessible. An expert in a KC may help solve technical problems directly or refer to other sources of information as indirect solutions. Different from traditional organizations, where only those with unique knowledge about an item of interest are considered as experts [38], the de<sup>fi</sup>nition of experts in an online KC is much broader in the sense that each community member may have some degree of expertise in a certain area [3].

Existing expert <sup>fi</sup>nding techniques often rely on the following indicators to <sup>fi</sup>nd one's expertise areas and the level of expertise: self-classi<sup>fi</sup>cation, document-based relevance, and social importance. The majority of existing expert <sup>fi</sup>nding techniques are applied to organizations where information quality is high and knowledge hierarchy is well de<sup>fi</sup>ned. However, information quality in online communities is considerably poorer than that in organizations. Gu and Konana [22] found that information quality in an online community is often inversely related to the size of its membership. In the largest community-based open-access online knowledge repository, Wikipedia, merely 0.09% of the articles met a set of information quality assessment criteria and quali<sup>fi</sup>ed as featured articles as of September 2012 [54]. It is unclear whether existing expert <sup>fi</sup>nding techniques still work in the context of online communities. Most automated expert <sup>fi</sup>nding techniques rely on document-based relevance to predict the expertise level of experts for a given query [1,2,5,6,29,45]. These techniques assume that the relevance of one's authored documents to the query is positively related to their expertise level on the query. Recent studies <sup>fi</sup>nd that one's social importance inferred from the structural characteristics of a social network can also be used to <sup>fi</sup>nd experts [62]. However, very few studies have collectively considered both document-based relevance and social network based social importance.

In this study we propose a new expert <sup>fi</sup>nding algorithm, namely ExpertRank, for <sup>fi</sup>nding the experts on a given query in an online knowledge community. The algorithm evaluates experts based on document-based relevance to a given query as well as the experts' social importance in the community. The rest of this paper is organized as follows. Section 2 brie<sup>fl</sup>y reviews related work. Section 3 de<sup>fi</sup>nes our research objectives. Section 4 describes the ExpertRank algorithm in detail. Section 5 explains our evaluation methods and experimental results. Conclusions and future work are discussed in Section 6.

## 2. Related work

The expert <sup>fi</sup>nding problem has attracted research attention in various contexts. Davenport and Prusak argue that knowledge exists within people and is “a <sup>fl</sup>uid mix of framed experience, values, contextual information, and expert insight” [15]. Traditionally, expert <sup>fi</sup>nding has been applied to organizational or enterprise knowledge repositories where knowledge is well documented and information quality is high. For example, computer systems such as the Answer Garden [1,2] and the DEMOIR approach [58] have been developed to <sup>fi</sup>nd the appropriate expert for a given problem in an organization. Both systems achieved satisfactory results in the context of organizations.

Compared with organizations, online KCs usually do not have a universal knowledge structure (e.g., a hierarchical structure). Knowledge is generated when community users are engaged in online discussions and try to help each other solve problems. Information stored in KCs tends to have low information quality due to the fact that KC participants make voluntary contributions and have no obligation to maintain high information quality. Poor information quality will de<sup>fi</sup>nitely affect the performance of knowledge management activities that involve information processing. Moreover, information quality is strongly related to the perceived usefulness and acceptance of information technology [30]. It is not known if organizationoriented expert <sup>fi</sup>nding techniques can still be effective and useful in online KCs.

Existing expert <sup>fi</sup>nding systems utilize three sources of expertise indicators to make expert recommendations: self-disclosed information such as yellow pages and directories, content of authored documents (and software artifacts), and interaction history and social network analysis [40]. In the rest of this section we review existing expert <sup>fi</sup>nding techniques using each type of expertise indicators.

## 2.1. Expert finding based on self-disclosed information

Self-disclosure requires expert candidates to explicitly declare their expertise in their posted pro<sup>fi</sup>les [15]. Expert recommendation systems that employ this approach include yellowpages.com, guru.com, 88owls.com, and other opt-in directory listings of experts. The manual process is time-consuming and expertise pro<sup>fi</sup>les are also unlikely to remain current as each user's expertise is continuously expanding.

## 2.2. Expert finding based on authored documents

Documents that were written or reviewed by an expert candidate are also a useful expertise indicator. There are a number of expert <sup>fi</sup>nding systems that use text mining techniques to automatically capture the authors' expertise [28,34,45]. These expert <sup>fi</sup>nding techniques are referred to as document-based techniques.

For example, in an organizational context, the Answer Garden system [1,2] analyzes questions and answers sent to experts and categorizes the questions and experts into an ontology. The users of the system can navigate the ontology of questions and <sup>fi</sup>nd experts as the “leaf nodes” in the ontology. However, the technique works only with a prede<sup>fi</sup>ned set of experts that is hard to change. In addition, an ontology may not be readily available and it may take some effort to build one.

Streeter and Lochbaum proposed an Expert/Expert-Locator (EEL) system that pairs requests for technical information with appropriate technical organizations [45]. Their system automatically constructs a semantic space of organizations and terms using a statistical matrix decomposition technique to represent term-based semantic similarity in text documents.

In the <sup>fi</sup>eld of stock-market prediction, Hill and Ready-Campbell [23], assess an expert's skill as the conformance between that expert's historic predictions and actual stock market results. Experts with the highest ranking are those with the highest average number of correct future stock movement predictions (‘outperform’ vs. ‘underperform’), for outlook period X (typically 40 trading days=2 work months), made by the expert over the prior calendar year.

Other document-based expert <sup>fi</sup>nding techniques rely on information retrieval techniques to determine the relevance between an expert candidate and a search query. For example, Balog et al. proposed two generative language models to identify experts given a search query and a collection of documents associated with expert candidates [5,6]. Krulwich and Burkey developed ContactFinder that refers electronic bulletin board users with queries to people who can help them based on historical bulletin board messages [29]. The system categorizes messages and extracts their topics using a set of heuristics.

Document-based expert <sup>fi</sup>nding techniques have achieved satisfactory performance in their applications.

## 2.3. Expert finding based on social network analysis

Document-based techniques can be used to <sup>fi</sup>nd experts because documents contain terms that are semantically relevant to the authors' expertise areas. Although document-based techniques are effective, they fail to consider each expert candidate's importance or in<sup>fl</sup>uence in the social network that they belong to.

Social cognitive studies have repeatedly shown that one's social in<sup>fl</sup>uence plays an important role in the perception of their expertise. Romney et al. found that there is generally a positive relationship between the degree that a person's messages are shared with others, and that person's competence [41]. Kameda et al. reasoned that “cognitively central members of a community can provide social validation for other members' knowledge, and that, concurrently, their knowledge is con<sup>fi</sup>rmed by other members, leading to the perception of well-balanced knowledge or expertise in the focal task domain” [26].

Information system studies also show that peripheral information not related to document content is very important in knowledge seeking activities. The knowledge adoption model found that both content-based information quality and non-content-based information source credibility are positively related to perceived information usefulness and users' intention to adopt the received knowledge [46,49]. Cross et al. showed that social structural in<sup>fl</sup>uence was one of the factors in determining whether a pair of survey respondents reported exchanging information bene<sup>fi</sup>t [13]. Speci<sup>fi</sup>cally, they observed that social in<sup>fl</sup>uence played an important role in problem reformulation and the way in which solutions became more broadly accepted. Ibarra suggests that network centrality is positively related to administrative and technical innovation involvement in an organization [24]. Similar to formal authority, higher network centrality implies a higher degree of access to and control over valued information resources [9].

Expert <sup>fi</sup>nding based on social network based characteristics alone is rare. Zhang et al. [62] built a social network based on historical post-reply activities in an online Java programming discussion forum. They proposed and evaluated several link-based expert <sup>fi</sup>nding algorithms. They found that the PageRank-based expert <sup>fi</sup>nding algorithm outperformed other network-based algorithms in the online community setting. However, their algorithm can be used only to <sup>fi</sup>nd experts at the community level. It is not capable of <sup>fi</sup>nding experts on a speci<sup>fi</sup>c topic or query.

## 2.4. Hybrid expert finding techniques

Recent expert <sup>fi</sup>nding systems have started considering both document-based expertise indicators and social relationships [27,36,62].

For example, Serdyukov et al. proposed a relevance propagation algorithm that considered not only the documents directly related to an expert but also those indirectly related through document–author relationships [43]. They also utilized additional peripheral information such as hyperlinks in documents, the organizational structure, and user feedback. Their evaluation results showed that their approach outperformed those methods that considered only directly-related documents.

Campbell et al. introduced a HITS (Hypertext Induced Topic Search) based expert <sup>fi</sup>nding algorithm in the context of email communications [10,14]. HITS is a graph-based link analysis algorithm originally used for rating the importance of Web pages based on authority and hub scores. The algorithm considered both email contents and communication patterns when determining experts' rankings. Experiments showed that their approach performed better than those algorithms that considered only email contents. However, their experiments considered very small networks (less than 15 people) and failed to explain the meaning of hub and authority in HITS in the context of expert <sup>fi</sup>nding.

Fu et al. made a similar attempt that sought to combine document contents and social network information to perform expert <sup>fi</sup>nding [21]. They built social networks based on email communications and the co-occurrences of people on Web pages. They also demonstrated performance improvement over a content-based expert <sup>fi</sup>nding technique. But their technique relied on the identi<sup>fi</sup>cation of a number of seed experts. The performance of their technique was sensitive to the selection of seeds (i.e., non-experts). Moreover, they used an enterprise dataset where documents had relatively high information quality. It is questionable whether the same approach can be applied to online KCs where information quality is low and the size of the community network is very large.

Expert <sup>fi</sup>nding problems have also been explored using knowledge sources that are not well structured and managed. Zhang et al. proposed an expert <sup>fi</sup>nding algorithm in an online help-seeking community, the Java Forum [61]. Their approach considered both document contents and social network information. However, the effectiveness of the proposed algorithm is unknown because of the lack of empirical evaluations.

We summarize existing expert <sup>fi</sup>nding methods in Table 1. Expert <sup>fi</sup>nding based on manually self-disclosed information is timeconsuming and it is dif<sup>fi</sup>cult to keep up with constantly expanding expertise pro<sup>fi</sup>les. Both document-based expertise indicators and social in<sup>fl</sup>uence are important factors for locating experts in automated expert <sup>fi</sup>nding techniques. However, most of the techniques apply to organizational contexts where information quality is high. Expert <sup>fi</sup>nding techniques proposed by Kurlwich and Burkey [29] and Zhang et al. [61] aim to extract expertise pro<sup>fi</sup>les based on postings made in online communities where information quality is low. However, Kurlwich and Burkey's method fails to consider experts' importance in a social context, and the effectiveness of Zhang et al.'s method is unknown. Though Hill and Ready-Campbell [23] consider online communities, they consider only the sequence of binary (‘outperform’ vs. ‘underperform’) stock predictions made by each expert, for each stock ticker symbol, rather than the full textual content of the expert's postings. Information quality in their method is therefore high, as only a small, highlystructured subset of available information is used for ranking the expert. Finally, most previous work has focused only on the static ranking of domain experts without considering user-speci<sup>fi</sup>c information needs, whereas our work serves as a method of dynamic expert ranking based on topic queries.

## 3. Research objectives

In this study we propose a new expert <sup>fi</sup>nding technique that aims to make the following contributions. First, the technique can be applied to online KCs which, compared with organizational or enterprise knowledge repositories, do not have a knowledge ontology, have low information quality, and are rich in social media. Second, our expert <sup>fi</sup>nding technique dynamically ranks experts in the area speci<sup>fi</sup>ed by a search query. Lastly, our technique employs both document content and social network based characteristics as expertise indicators. Document contents are used to evaluate the relevance between an expert candidate's expertise and a search query. Social in<sup>fl</sup>uence is important in assessing an expert candidate's competence and knowledge balance. We describe our expert <sup>fi</sup>nding algorithm in detail in Section 4.

Existing expert <sup>fi</sup>nding studies.

<table><tr><td rowspan="2">Study</td><td colspan="3">Expertise indicators used</td><td rowspan="2">Domain</td><td rowspan="2">Document type</td><td rowspan="2">Information quality</td></tr><tr><td>Self-disclosure</td><td>Document-based</td><td>Social network</td></tr><tr><td>Davenport and Prusak, 1998</td><td>√</td><td></td><td></td><td>Organization</td><td>N/A</td><td>High</td></tr><tr><td>Ackerman and Malone, 1990</td><td>√</td><td></td><td></td><td>Organization</td><td>N/A</td><td>High</td></tr><tr><td>Balog et al., 2006, 2007</td><td></td><td>√</td><td></td><td>Organization</td><td>W3C HTML documents</td><td>High</td></tr><tr><td>Streeter and Lochbaum, 1988</td><td></td><td>√</td><td></td><td>Organization</td><td>Computer accessible documents</td><td>High</td></tr><tr><td>Krulwich and Burkey, 1996</td><td></td><td>√</td><td></td><td>Online community</td><td>Electronic bulletin board messages</td><td>Low</td></tr><tr><td>Hill and Ready-Campbell, 2011</td><td></td><td>√</td><td></td><td>Online community</td><td>Online user postings</td><td>High</td></tr><tr><td>Zhang et al., 2007</td><td></td><td></td><td>√</td><td>Online community</td><td>Online user postings</td><td>Low</td></tr><tr><td>Serdyukov, 2007</td><td></td><td>√</td><td>√</td><td>Organization</td><td>W3C HTML documents</td><td>High</td></tr><tr><td>Campbell et al. 2003</td><td></td><td>√</td><td>√</td><td>Organization</td><td>Emails</td><td>High</td></tr><tr><td>Fu et al., 2007</td><td></td><td>√</td><td>√</td><td>Organization</td><td>Emails</td><td>High</td></tr><tr><td>Zhang et al., 2007</td><td></td><td>√</td><td>√</td><td>Online community</td><td>Online user postings</td><td>Low</td></tr><tr><td>This study</td><td></td><td>√</td><td>√</td><td>Online community</td><td>Online user postings</td><td>Low</td></tr></table>

## 4. The ExpertRank algorithm

We de<sup>fi</sup>ne the expert ranking problem in online KCs as one that identi<sup>fi</sup>es the expertise of a certain expert candidate ca given a query topic q: Expert(ca,q). We argue that an expert candidate's expertise on a certain topic depends not only on whether the candidate has relevant knowledge, but also on the candidate's social importance or in<sup>fl</sup>uence in the community. The idea is similar to what is behind a Web information retrieval technique [25], where the rank of a search result page with respect to a user query is determined by a combination of content-based similarity and link-based importance. We de-<sup>fi</sup>ne the expertise of a candidate ca with respect to a query q as a heuristic combination of expertise relevance and authority:

$$
\text { ExpertRank } (c a, q) = f (R E (c a, q), A U (c a))\tag{1}
$$

where RE(ca,q) denotes a relevance score between the documents (i.e., posts in online KCs) authored by the candidate ca and a user query q, AU(ca) denotes the global authority score of the candidate ca re<sup>fl</sup>ecting the social importance of the member within the community. The function f(•) is a combination strategy that collectively considers expertise relevance and authority to produce an expert ranking.

## 4.1. Expertise relevance

Expertise relevance indicates whether or not a community member has any level of expertise with regard to a speci<sup>fi</sup>c topic. In order to calculate the expertise relevance score, we <sup>fi</sup>rst consider each community participant as a potential expert candidate. We represent each candidate with an expertise pro<sup>fi</sup>le built by merging all the documents that the candidate has previously authored into a single document. Stop-word removal and stemming should be performed to remove insigni<sup>fi</sup>cant words and convert derived words into their root forms before such a document is generated for each candidate. Given a search query, we can employ the Vector Space Model [42], a classic information retrieval technique, to calculate a cosine similarity score [4] between each candidate's expertise pro<sup>fi</sup>le document ca and the query q:

$$
R E (c a, q) = \frac {\sum_ {j = 1} ^ {t} w _ {j} d _ {j}}{\sqrt {\sum_ {j = 1} ^ {t} d _ {j} ^ {2} \sum_ {j = 1} ^ {t} w _ {j} ^ {2}}}\tag{2}
$$

where $w _ { j }$ denotes the term frequency-inverse document frequency (TF-IDF) weight of term $j$ in an expertise pro<sup>fi</sup>le document and $d _ { j }$ denotes the TF-IDF weight of term j in the query vector q.

## 4.2. Expert authority

To determine a member's social in<sup>fl</sup>uence or importance, we need to construct a social network that represents the social interactions of members in an online KC. In a typical online knowledge community, as Fig. 1 illustrates, a community user initiates a discussion topic by creating a new thread while others join the discussion by posting replies to the same thread. The user–thread relationships can be represented using a graph: see Fig. 1.(1). The user–thread relationship graph has two types of vertices: users $u _ { i }$ and threads $t _ { i \cdot }$ A directed edge from a user to a thread denotes a thread starting relationship where the user creates a new thread by posting a question. A directed edge from a thread to a user denotes a thread replying relationship where the user has replied to the thread. We extract user–user relationships by connecting users who participate in the same thread with directed edges from topic starters to repliers: see Fig. 1.(2). The user–user graph depicts social interactions in the online community. We use this user–user relationship graph to infer one's social importance in an online KC.

Link analysis algorithms such as PageRank [7] can measure the importance (i.e., authority) of a node in a network based on the link structure of the network. Zhang et al. [62] adapted the concept of PageRank in the context of expert finding. The intuition behind their expert ranking algorithm is that a user's expertise level should be higher than those users whom he or she is able to help. It is similar to the intuition behind the PageRank algorithm where the importance of a Web page depends on the pages that link to it. In the context of online community discussions, a user A will receive a vote of support from another user B whose question is answered by A. If several users help answer B's question, the vote of support from B is evenly distributed to those users. Fig. 1.(2) illustrates a user–user relationship graph derived from discussions in an online community. A user–user relationship graph can be formally de<sup>fi</sup>ned as $U { = } { < } V ,$ E>, where V is a vector of N users and E consists of directed links from discussion thread starters to repliers. Each element in the user–user relationship matrix U, also known as an adjacency matrix in PageRank, can be calculated as

![](/api/attachments/QJC2MWED/fulltext/images/8bac2d06c4c735b72849d72ef040e2bb20ccd090e999b6e8b44781f9784dc638.jpg)

![](/api/attachments/QJC2MWED/fulltext/images/3d9e3487799e2876a7964bbfe3bca49ead1ae56c088308c919a52e770b8681ee.jpg)  
Fig. 1. A user-thread graph and a user-user relationship graph.

$$
u _ {i j} = \left\{ \begin{array}{l l} 0 & i f (i, j) \notin E \\ 1 / o u t (i) & i f (i, j) \in E \end{array} \right.\tag{3}
$$

where out(i) is user i's out-degree, i.e., the total number of users who have helped user i. Each element $u _ { i j }$ represents the vote of support received for user j from user i. Therefore, we can develop a PageRank-like algorithm to measure a user's importance or authority (AU) in a recursive way:

$$
A U (i) = d \cdot \sum_ {j = 1} ^ {N} A U (j) \cdot u _ {j i} + (1 - d) \frac {1}{N}.\tag{4}
$$

d is a damping factor similar to that used in PageRank, allowing the recursive cycles to jump to a random user in the community rather than to follow the links derived from discussions a fraction (1-d) of the time. It is commonly set to 0.85 [7,56]. An iterative algorithm such as the power iteration method can be used in this recursive computation using an initial assignment of authority scores such as $A U ( i ) = 1 / N \left[ 7 , 5 6 \right]$ . The iteration ends when the authority scores converge.

## 4.3. A modified PageRank algorithm

In Eq. (4) we assign an equal weight to each user–user edge when determining the authority score. However, those edges may carry different importance weights. Let us consider two scenarios: (1) two users connected by an edge because they participated in one discussion thread; (2) two users connected by an edge because they participated in a number of different discussion threads. Obviously, the edge in the second scenario should carry more importance. Moreover, we noticed a problem when we applied PageRank to assess users' authority scores in online KCs. Those who tend to discuss frequently with a small number of users would accumulate high authority scores in PageRank. However, they may not deserve high authority ratings for the following reasons. First, those users may share a common interest that is only attractive to a very small audience. They would only deserve high authority scores when the sought topic is highly relevant to their interests. Second, those users often form a collusion structure that leads to in<sup>fl</sup>ated PageRank scores. A perfect collusion structure consists of nodes having no external out-links but only internal out-links to each other. Zhang et al. found that a small group of low ranked (e.g., 10,000th) users could form a collusion that catapulted them into the top-400 [60].

To reduce the in<sup>fl</sup>uence of colluded groups, we modi<sup>fi</sup>ed the calculation of the expert authority score as follows:

$$
A U (i) = d \cdot \sum_ {j = 1} ^ {N} A U (j) \cdot u _ {j i} ^ {\prime} + (1 - d) \frac {1}{N}\tag{5}
$$

where $u _ { j i } ^ { \prime }$ denotes an element in a weighted adjacency matrix U′. We propose a weighted reference relationship (WRR) algorithm for calculating the weighted adjacency matrix. Fig. 2 illustrates the details of the WRR algorithm.

The idea of the WRR algorithm is illustrated in Fig. 3. Step (1) of the WRR algorithm assigns each edge a weight $n _ { i j } ,$ which is the number of replies user j made to user $i \ ( { \mathrm { e . g . } } , n _ { 1 2 } { = } s _ { 1 2 } { = } 1 , n _ { 3 1 } { = } s _ { 3 1 } { = } 2 )$ Self-referencing edges will receive zero weight $( { \bf e . g . } , n _ { 4 4 } = s _ { 4 4 } = 0 )$ .

The matrix S becomes

$$
S = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 2 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right].
$$

In Step (2) the algorithm updates the edge weights in matrix S by weight by subtracting the number of reverse links (both direct and indirect links) from user j to user i with the maximum length of an indirect link being no more than m. Assuming m=2 and $\beta = 0 . 5 , s _ { 3 1 } ^ { \prime } =$ $S _ { 3 1 - s 1 3 } - \beta ^ { * } m i n ( s _ { 1 2 } , s _ { 2 3 } ) = 2 - 0 - 0 . 5 * m i n ( 1 , 1 ) = 1 . 5$ . We then get a new matrix S′

$$
S ^ {\prime} = \left[ \begin{array}{c c c c c} 0 & 0. 5 & 0 & 0 & 0 \\ 0 & 0 & 0. 5 & 0 & 0 \\ 1. 5 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right].
$$

The last step of the algorithm normalizes the weights by each row so that weights on each row add up to 1. We then get

$$
U ^ {\prime} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0. 4 3 & 0 & 0 & 0. 2 8 5 & 0. 2 8 5 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right].
$$

## 4.4. Combination strategies

Now we consider the combination strategy $( \mathrm { i } . \mathrm { e } . , f ( \bullet )$ in Eq. (1)) that combines expertise relevance and expert authority into a single expert ranking score. We propose three strategies as follows:

Strategy 1. Linear combination. The weighted linear combination method is a commonly used data fusion method and has been successfully applied to various data fusion scenarios [35,37,55]. In this strategy we assume that both content-based relevance and link-based authority determine an expertise rank score collectively and simultaneously. The relevance score and authority score are combined as a weighted sum

$$
E R (u _ {i}, q) = a \cdot R E (u _ {i}, q) + (1 - a) \cdot A U (u _ {i})
$$

where $u _ { i }$ is an expert candidate and $a \in [ 0 , 1 ]$ is a coef<sup>fi</sup>cient. However, a high rank score achieved using this strategy does not necessarily mean high scores in both relevance and authority. It is possible that a high rank score may result from a highly skewed authority score despite a low relevance score (i.e., the user's expertise pro<sup>fi</sup>le is not relevant to the search query at all).

Strategy 2. Cascade ranking. The cascade ranking method uses a sequence of ranking functions to progressively re<sup>fi</sup>ne a rank order [50]. We <sup>fi</sup>rst use the content-based relevance score alone to rank users; then select a percentage $b \in [ 0 , 1 ]$ of top experts based on the relevance ranking; re-rank the top experts using link-based authority scores. In this strategy we <sup>fi</sup>rst remove those users whose expertise pro<sup>fi</sup>les are less relevant. Therefore, those who rank highly in the <sup>fi</sup>nal ranking list will have an expertise pro<sup>fi</sup>le highly relevant to the search query and a high authority score.

Strategy 3. Scaling strategy. The scaling strategy has been previously used in supervised classi<sup>fi</sup>cation to combine results predicted by different classi<sup>fi</sup>ers and in some cases it outperforms the

Microsoft Of<sup>fi</sup>ce Discussion Groups.

Given two users i and ${ \bf \Xi } _ { j , n ( i , j ) }$ is the number of times that j has replied to i.

Step (1): Construct a matrix S with each element calculated as

$$
s _ {i j} = \begin{array}{l l} \text {i} 0 & \text {if i = j} \\ \text {i} n (i, j) & \text {if i ^ {1} j} \end{array}
$$

Step (2): For each element $s _ { i j }$ in matrix $S ,$ update its weight by subtracting the number of reverse links (both direct and indirect links) from user j to user i

$$
s _ {i j} ^ {\prime} = s _ {i j} - s _ {j i} - \beta \sum_ {k} \min (s _ {j k}, s _ {k i}) - \beta^ {m - 1} \sum_ {k \dots l} \min (s _ {j k},..., s _ {l i})
$$

where m denotes the largest geodesic distance of a reverse link from user i to user j and β denotes a damping factor, a value between 0 and 1

I $\mathrm {  ~ f ~ } s _ { \ i j } ^ { \prime } \ < \theta ,$ then $s \prime _ { i j } = 0$

Step (3): Calculate each element $\boldsymbol { u ^ { \prime } } _ { i j }$ in $U ^ { \prime }$ by normalizing $\boldsymbol { s ^ { \prime } } _ { i j } . ^ { \prime } .$

$$
u _ {i j} ^ {\prime} = \frac {s _ {i j} ^ {\prime}}{\sum_ {k = 1} ^ {N} s _ {i k} ^ {\prime}}
$$

Fig. 2. The weighted reference relationship algorithm.

linear combination strategy [47]. Following this strategy, we combine content-based relevance score and link-based authority score using multiplication.

$$
E R (u _ {i}, q) = R E (u _ {i}, q) ^ {c} \times A U (u _ {i})
$$

where c is a scaling parameter re<sup>fl</sup>ecting the contribution of relevance and authority to the <sup>fi</sup>nal expert ranking.

## 5. Experiments

In this section we describe our empirical evaluations conducted for the proposed ExpertRank algorithm. Because a number of parameters are involved in the proposed algorithm, we <sup>fi</sup>rst conducted experiments to determine the optimal values for those parameters. In addition we tested the three proposed strategies for combining content-based relevance and social network based authority and determined the optimal strategy. Finally, using the optimal parameter values and combination strategy, we compared the proposed ExpertRank algorithm with two baseline methods: (1) a document-based method where only content-based relevance scores were used to rank experts, and, (2) a hybrid (document-based and social-network-based) method which used only a standard (i.e., non-modi<sup>fi</sup>ed) PageRank algorithm to rank experts.

## 5.1. Dataset

Microsoft Of<sup>fi</sup>ce Discussion Groups is the of<sup>fi</sup>cial online helpseeking community that allows Microsoft Of<sup>fi</sup>ce users to share experiences and seek help for problems related to the software suite. The community consists of a number of forums with each focusing on a speci<sup>fi</sup>c Of<sup>fi</sup>ce product, e.g., Word, Access, and Excel. We chose to use this community as our experiment's testbed because this well-established community has accumulated a large volume of online postings with rich social interactions embedded in the posting–replying activities. Moreover, the community members and Microsoft personnel have manually identi<sup>fi</sup>ed the experts in the community. Each year a number of outstanding members of the community are selected to receive the Microsoft Most Valuable Professionals (MVP) award in recognition of their willingness and ability to help others solve problems. These selected members are grouped into different competence lists in corresponding sub forums. These of<sup>fi</sup>cial member competence lists can be naturally employed as the gold standard for our empirical evaluations.

![](/api/attachments/QJC2MWED/fulltext/images/e2e36a90831318fc0f54cf58d81c3913cb00965c01e9de05a0a5b622a356c283.jpg)  
Fig. 3. An illustration of the WRR algorithm.

We crawled all online postings in the Microsoft Of<sup>fi</sup>ce Discussion Groups from the establishment of the discussion groups in 2005 to the end of year 2007, with approximately three years of data. Table 2 lists some basic statistics of the crawled data. Similar to what researchers did in TREC [5], we extracted 19 topic phrases that were the names (i.e., Microsoft Of<sup>fi</sup>ce product names) of the 19 forums and used them as search queries for <sup>fi</sup>nding experts in each topic area.

## 5.2. Evaluation metrics

We employed several commonly used information retrieval metrics to evaluate our experimental results including precision (P), recall (R), macro-average F-measure(Ma), micro-average F-measure(Mi), P@10, and P@20 [57]. Given a query q in a query set $Q _ { ☉ }$ le $a _ { q }$ denote the number of true experts detected (true positive), $b _ { q }$ the total number of experts detected (true positive and false positive), $d _ { q }$ the number of experts in the gold standard (true positive and false negative). The metrics are calculated using the following formula:

<table><tr><td>Number of forums</td><td>19</td></tr><tr><td>Number of sub-domains</td><td>76</td></tr><tr><td>Number of users</td><td>121,289</td></tr><tr><td>Number of users who have asked questions</td><td>105,968</td></tr><tr><td>Number of users who have replied to questions</td><td>66,369</td></tr><tr><td>Number of question posts</td><td>228,787</td></tr><tr><td>Number of replying posts</td><td>624,219</td></tr></table>

![](/api/attachments/QJC2MWED/fulltext/images/9061c9353ca59c35442ecdbf2d4f2128de4f3b11137943e0768ff168980a8207.jpg)  
Fig. 4. The impact of different β values on expert <sup>fi</sup>nding (m=2).

$$
P = \frac {\sum_ {q \in Q} a _ {q}}{\sum_ {q \in Q} b _ {q}},
$$

$$
R = \frac {\sum_ {q \in Q} a _ {q}}{\sum_ {q \in Q} d _ {q}},
$$

$$
F _ {q} = \frac {2 \cdot \frac {a _ {q}}{b _ {q}} \cdot \frac {a _ {q}}{d _ {q}}}{\frac {a _ {q}}{b _ {q}} + \frac {a _ {q}}{d _ {q}}},
$$

$$
M a = \frac {\sum_ {q} F _ {q}}{| Q |},
$$

$$
M i = \frac {2 \cdot P \cdot R}{P + R}.
$$

P@n measures precision for the top n experts detected. Ma and Mi are F-measures that are weighted harmonic means of precision and recall [57]. When a micro-average F-measure is calculated, the binary expert decisions for all search queries are collected in a joint pool. When a macro-average F-measure is calculated, a separate F-measure $F _ { q }$ is <sup>fi</sup>rst calculated for each search query before all $F _ { q }$ values are averaged over all search queries.

## 5.3. The optimal parameter values

To determine the parameters β and m in the WRR algorithm, we applied the WRR algorithm to each of the 19 topic queries and compared the obtained sets of experts to the corresponding MVP competence lists. We <sup>fi</sup>rst let $m = 2$ and conducted a sensitivity analysis on the value of β in a range between 0 and 1. Fig. 4 shows the precision, recall, and F-measures over different β values. We can see that the coef<sup>fi</sup>cient β has a slight impact on the performance of the expert ranking system. As we increased the value of $\beta ,$ the corresponding measures were slightly improved in a monotonic way. In the following experiments we let $\beta = 1$ in order to achieve the optimal performance.

Once the optimal value for coef<sup>fi</sup>cient β was determined, we investigated how the largest geodesic distance, m, would affect the performance of expert <sup>fi</sup>nding. We limited the value range of m to no more than three because the computational complexity would grow exponentially as m increases. Results showed that both F-measure values had the best performance when m=2 (see Fig. 5). Therefore, the optimal value of m is 2.

## 5.4. The optimal combination strategy

We conducted experiments to determine the optimal strategy for combining the content-based expertise relevance score and the link-based expert authority score. Fig. 6 shows the expert ranking results using the linear combination strategy. It achieved its best performance $( \mathrm { M a c r o F 1 } = 0 . 1 7 )$ when $a = 0$ . That means, under the linear combination assumption, using the authority score alone to rank experts would be adequate. The cascade ranking strategy appeared to be the optimal strategy, as Fig. 7 shows. The algorithm achieved its best performance (MacroF1=0.34) when the top 40% of experts – ranked based on expertise relevance score – were re-ranked using authority scores. The best performance of the scaling strategy, as shown in Fig. 8, was comparable with that of cascade ranking. We prefer the cascade ranking strategy because the optimal value of the parameter c in the scaling strategy is dif<sup>fi</sup>cult to interpret.

![](/api/attachments/QJC2MWED/fulltext/images/cfd38edd287ce1bcdd938b685e4255d0bae1e30d0cee165fdfe55c62fc5e9aab.jpg)  
Fig. 5. The impact of different m values on expert <sup>fi</sup>nding (β=1).

![](/api/attachments/QJC2MWED/fulltext/images/52b86f1a4c71c3ea3073c7c2378406cdb1af6e429894f90f6ca1a8c94e792bef.jpg)  
Fig. 6. Expert <sup>fi</sup>nding performance using the linear combination strategy.

## 5.5. Comparing with document-based expert finding

Using the optimal parameter values and combination strategy, we evaluated the effectiveness of our ExpertRank algorithm in comparison with a baseline method where only the content-based relevance score was used to <sup>fi</sup>nd the experts. The results are shown in Fig. 9. ExpertRank signi<sup>fi</sup>cantly outperformed the content-based baseline method (pb0.001). ExpertRank's F-measures (MacroF1 and MicroF1) were around 34%. Those of the baseline method were only about 11%, which was in line with previous expert <sup>fi</sup>nding studies based on documents alone, such as [5].

![](/api/attachments/QJC2MWED/fulltext/images/3373f4a13116d40e555425f824a2f72ecaf643b5c55bf86d74ce092e08714352.jpg)

Fig. 7. Expert <sup>fi</sup>nding performance using the cascade ranking strategy.  
![](/api/attachments/QJC2MWED/fulltext/images/9d2fbe019c33350ddd0ccecbceccb4524b0517596a201fe42b333998365c7ed7.jpg)  
Fig. 8. Expert <sup>fi</sup>nding performance using the scaling strategy.

![](/api/attachments/QJC2MWED/fulltext/images/aeb2787fe67ce82b2f441f9eb5f339edd4dc354fb8342029d119d9fe5054e2e8.jpg)  
Fig. 9. Performance comparison between ExpertRank and document-based expert <sup>fi</sup>nding.

## 5.6. Comparing with PageRank-based hybrid expert finding

In this experiment we compared the effectiveness of the proposed WRR algorithm in our ExpertRank method with the PageRank used in hybrid expert <sup>fi</sup>nding [62]. The WRR algorithm is designed to reduce the effect of in<sup>fl</sup>ated authority scores due to colluded discussion patterns. We used WRR and PageRank to calculate expert candidates' authority scores separately before applying the scores to the proposed ExpertRank algorithm. As shown in Fig. 10, our proposed expert <sup>fi</sup>nding technique achieved better results in almost all performance measures when WRR was used to calculate authority scores in hybrid expert <sup>fi</sup>nding.

## 6. Conclusions and future work

In this paper we proposed a new algorithm for <sup>fi</sup>nding experts in online KCs. Online KCs provide useful and accessible knowledge sources in various <sup>fi</sup>elds. Different from organizational knowledge repositories that are well managed and maintained, the knowledge bases in online KCs do not have a universal knowledge structure and tend to have low information quality due to the voluntary and anonymous nature of their participants. On the other hand, online KCs are rich social media which support interactions between knowledge seekers and contributors. Existing expert <sup>fi</sup>nding techniques are mainly document-centric with few leveraging contextual information such as social media. We proposed a novel expert <sup>fi</sup>nding technique, ExpertRank, for <sup>fi</sup>nding experts in online KCs. ExpertRank evaluates experts on both knowledge relevance and authority in the community. We proposed a modi<sup>fi</sup>ed PageRank algorithm that reduces the biasing in<sup>fl</sup>uence of small-interconnected groups on the calculation of authority scores. Experimental results showed that the ExpertRank algorithm outperformed both document-centric expert <sup>fi</sup>nding and PageRank-based hybrid expert <sup>fi</sup>nding.

![](/api/attachments/QJC2MWED/fulltext/images/6803e47d0f9f4e2b8d1ea8aa43500936dc764f7e413f568ec971d7c17879c362.jpg)  
Fig. 10. Performance comparison between ExpertRank and PageRank-based hybrid expert <sup>fi</sup>nding.

This research has several limitations which we plan to address in the future. Currently, we use a simple TF-IDF weighting to index all keywords in user postings when creating a user pro<sup>fi</sup>le. Better term weighting strategies, such as Okapi [44], could be tried to improve the accuracy of user pro<sup>fi</sup>ling. In addition, we use only content-based and link-based evidence as expertise indicators. There could be other sources of evidence about user expertise, such as the tenure of a user in a KC, number of postings from historic time t to current time, number of users helped from historic time t to current time, etc. These features could be combined with our current design to make the user expertise prediction more effective and accurate. Our current combination strategy is relatively straightforward and simple. We could use more powerful fusion strategies such as genetic algorithms [11,19,20] or genetic programming [16–18,48] to automatically design and <sup>fi</sup>ne-tune the fusion strategies. Moreover, our current evaluation is based on only one large online KC. We could validate our proposed algorithm in more diversi<sup>fi</sup>ed KCs to test its ef<sup>fi</sup>cacy and generalizability.

Expert <sup>fi</sup>nding has become increasingly important in large corporations which have amassed a huge volume of data such as employee internal communications (e.g., emails), knowledge exchanges on internal discussion forums, and customer service interactions collected via the Web. Notable examples include GE, Dell, IBM, KPMG, Microsoft, and Google. The research ideas presented in this article could be easily extended or modi<sup>fi</sup>ed to these data to help build expert databases or organizational memory systems that facilitate knowledge exchange among employees.

## Acknowledgments

This research is partly supported by the Natural Science Foundation of China (grant #70872089 and #71072129) and the National Science Foundation (grant #DUE-0840719).

## References

[1] M.S. Ackerman, T.W. Malone, Answer Garden: a tool for growing organizational memory, Proceedings of the ACM SIGOIS and IEEE CS TCOA Conference on Of<sup>fi</sup>ce Information Systems, Cambridge, MA, 1990, pp. 31–39.

[2] M. Ackerman, D. McDonald, Answer Garden 2: merging organizational memory with collaborative help, Proceedings of the 1996 ACM Conference on Computer Supported Cooperative Work, Boston, MA, 1996, pp. 97–105.

[3] M.S. Ackerman, V. Wulf, V. Pipek, Sharing Expertise: Beyond Knowledge Management, MIT Press, Cambridge, MA. 2002.

[4] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, ACM Press, New York, NY, 1999.

[5] K. Balog, L. Azzopardi, M. de Rijke, Formal models for expert <sup>fi</sup>nding in enterprise corpora, Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, New York, NY, 2006, p. 50.

[6] K. Balog, T. Bogers, L. Azzopardi, M. de Rijke, A. van den Bosch, Broad expertise retrieval in sparse data environments, Proceedings of the 30th Annual International ACM SIGIR Conference, Amsterdam, The Netherlands, 2007, pp. 551–558.

[7] S. Brin, L. Page, The anatomy of a large-scale hypertextual web search engine, Computer Networks 30 (1998) 107–117.

[8] J.S. Brown, P. Duguid, Knowledge and organization: a social-practice perspective, Organization Science 12 (2) (2001) 198–213.

[9] R.S. Burt, Toward a Structural Theory of Action, Academic Press, New York, NY, 1982.

[10] C.S. Campbell, P.P. Maglio, A. Cozzi, B. Dom, Expertise identi<sup>fi</sup>cation using email communications, Proceedings of the 12th International Conference on Information and Knowledge Management, New Orleans LA 2003

[11] H. Chen, Machine learning for information retrieval: neural networks, symbolic learning, and genetic algorithms, Journal of the American Society for Information Science 46 (1995) 194–216.

[12] D. Constant, L. Sproull, S. Kiesler, The kindness of strangers: the usefulness of electronic weak ties for technical advice, Organization Science 7 (2) (1996) 119.

[13] R. Cross, R.E. Rice, A. Parker, Information seeking in social context: structural in-<sup>fl</sup>uences and receipt of information bene<sup>fi</sup>ts, IEEE Transactions on Systems, Man, and Cybernetics, Part C: Applications and Reviews 31 (4) (2001) 438–448.

[14] R. D'Amore, Expertise community detection, Proceedings of the 27th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Shef<sup>fi</sup>eld, UK, 2004, pp. 498–499.

[15] T. Davenport, L. Prusak, Working Knowledge: How Organizations Manage What They Know, Harvard Business School Press, Boston, MA, 1998.

[16] W. Fan, M.D. Gordon, P. Pathak, Discovery of context-speci<sup>fi</sup>c ranking functions for effective information retrieval using genetic programming, IEEE Transactions on Knowledge and Data Engineering 16 (2004) 523–527.

[17] W. Fan, M.D. Gordon, P. Pathak, A generic ranking function discovery framework by genetic programming for information retrieval, Information Processing and Management 40 (4) (2004) 587–602

[18] W. Fan, M.D. Gordon, P. Pathak, Genetic programming-based discovery of ranking functions for effective web search, Journal of Management Information Systems 21 (4) (2005) 37–56.

[19] W. Fan, M. Gordon, P. Pathak, An integrated two-stage model for intelligent information routing, Decision Support Systems 42 (1) (2006) 362–374.

[20] W. Fan, P. Pathak, M. Zhou, Genetic-based approaches in ranking function discovery and optimization in information retrieval — a framework, Decision Support Systems 47 (4) (2009) 398–407.

[21] Y. Fu, R. Xiang, Y. Liu, M. Zhang, S. Ma, Finding experts using social network analysis, Proceedings of the IEEE/WIC/ACM International Conference on Web Intelligence, Fremont, CA, 2007, pp. 77–80.

[22] B. Gu, P. Konana, B. Rajagopalan, H.W.M. Chen, Competition among virtual communities and user valuation: the case of investing-related communities, Information Systems Research 18 (1) (2007) 68–85.

[23] S. Hill, N. Ready-Campbell, Expert stock picker: the wisdom of (experts in) crowds, International Journal of Electronic Commerce 15 (3) (2011) 73–102.

[24] H. Ibarra, Network centrality, power, and innovation involvement: determinants of technical and administrative roles, Academy of Management Journal 36 (3) (1993) 471–501.

[25] R. Jin, S. Dumais, Probabilistic combination of content and links, Proceedings of the 24th International ACM SIGIR Conference on Research and Development in Information Retrieval, New Orleans, LA, 2001, pp. 402–403.

[26] T. Kameda, Y. Ohtsubo, M. Takezawa, Centrality in sociocognitive networks and social in<sup>fl</sup>uence: an illustration in a group decision-making context, Journal of Personality and Social Psychology 73 (2) (1997) 296.

[27] H. Kautz, B. Selman, M. Shah, Referral web: combining social networks and collaborative <sup>fi</sup>ltering, Communications of the ACM 40 (3) (1997) 63–65.

[28] B. Krulwich, C. Burkey, Contact<sup>fi</sup>nder agent: answering bulletin board questions with referrals, The 13th National Conference on Arti<sup>fi</sup>cial Intelligence, Portland, OR, 1996.

[29] B. Krulwich, C. Burkey, Contact<sup>fi</sup>nder agent: answering bulletin board questions with referrals, Proceedings of the 13th National Conference on Arti<sup>fi</sup>cial Intelligence, Portland OR 1996

[30] A.L. Lederer, D.J. Maupin, M.P. Sena, Y. Zhuang, The technology acceptance model and the world wide web, Decision Support Systems 29 (3) (2000) 269–282.

[31] H. Lin, W. Fan, Z. Zhang, Uncovering critical success factors for web-based knowledge communities, Proceedings of the 16th Biennial Conference of the International Telecommunications Society, Bejjing China 2006

[32] H. Lin, W. Fan, L. Wallace, Z. Zhang, An empirical study of knowledge community success, Proceedings of the 40th Hawaii International Conference on System Sciences (HICSS). Big Islands, Hawaji, 2007.

[33] H. Lin, W. Fan, Z. Zhang, A qualitative study of web-based knowledge communities: examining success factors, International Journal of e-Collaboration 5 (3) (2009) 39–57.

[34] X. Liu, G.A. Wang, A. Johri, M. Zhou, W. Fan, Harnessing global expertise: a comparative study of expertise pro<sup>fi</sup>ling methods for online communities, Information Systems Frontiers (2012) 1–13.

[35] C. Marrocco, P. Simeone, F. Tortorella, A linear combination of classi<sup>fi</sup>ers via rank margin maximization, Proceedings of the 2010 Joint IAPR International Conference on Structural, Syntactic, and Statistical Pattern Recognition, Cesme, Izmir Turkey, 2010, pp. 650–659.

[36] D. Mattox, M. Maybury, D. Morey, Enterprise expert and knowledge discovery, Proceedings of the 8th International Conference on Human-Computer Interaction, Munich, Germany, 1999, pp. 23–27.

[37] P. McCullagh, J.A. Nelder, Generalized Linear Models, 2nd ed. Chapman & Hall/CRC, Boca Raton, FL, 1989.

[38] P.A. Morris, Combining expert judgments: a Bayesian approach, Management Science 23 (7) (1977) 679–693.

[39] S. Nambisan, R.A. Baron, Interactions in virtual customer environments: implications for product support and customer relationship management, Journal of Interactive Marketing 21 (2) (2007) 42–62.

[40] T. Reichling, M. Veith, V. Wulf, Expert recommender: designing for a network organization Learning in Communities (2009) 139–171

[41] A.K. Romney, S.C. Weller, W.H. Batchelder, Culture as consensus: a theory of culture and informant accuracy American Anthropologist 88 (2) (1986) 313–338

[42] G. Salton, A. Wong, C.S. Yang, A vector space model for automatic indexing, Communications of the ACM 18 (11) (1975) 613–620.

[43] P. Serdyukov, H. Rode, D. Hiemstra, University of Twente at the TREC 2007 Enterprise Track: modeling relevance propagation for the expert search task, The 16th Text Retrieval Conference (TREC 2007) Enterprise Track, Gaithersburg, MD, 2007.

[44] K. Sparck Jones, S. Walker, S. Robertson, A probabilistic model of information retrieval: development and comparative experiments part 2, Information Processing and Management 36 (6) (2000) 809–840.

[45] L. Streeter, K. Lochbaum, An expert/expert-locating system based on automatic representation of semantic structure, Proceedings of the Fourth Conference on Arti<sup>fi</sup>cial Intelligence Applications, San Diego, CA, 1988, pp. 380–388.

[46] S.W. Sussman, W.S. Siegal, Informational in<sup>fl</sup>uence in organizations: an integrated approach to knowledge adoption, Information Systems Research 14 (1) (2003) 47–65.

[47] D.M.J. Tax, R.P.W. Duin, M. Van Breukelen, Comparison between product and mean classi<sup>fi</sup>er combination rules, Proceedings of Workshop on Statistical Pattern Recognition, Prague, Czech Republic, 1997.

[48] R.S. Torres, A. Falcao, M.A. Goncalves, J.P. Papa, B. Zhang, W. Fan, E.A. Fox, A genetic programming framework for content-based image retrieval, Pattern Recognition 42 (2) (2009) 283–293.

[49] G.A. Wang, X. Liu, W. Fan, A text classi<sup>fi</sup>cation framework for <sup>fi</sup>nding helpful user-generated contents in online communities, Proceedings of the 2011 International Conference on Information Systems, Shanghai, China, 2011.

[50] L. Wang, J. Lin, D. Metzler, A cascade ranking model for ef<sup>fi</sup>cient ranked retrieval, Proceedings of the 34th International ACM SIGIR Conference on Research and Development in Information Retrieval, Beijing, China, 2011, pp. 105–114.

[51] M. Wasko, S. Faraj, Why should I share? Examining social capital and knowledge contribution in electronic network of practice, MIS Quarterly 29 (1) (2005) 35–57.

[52] M. Wasko, S. Faraj, R. Teigland, Collective action and knowledge contribution in electronic networks of practice, Journal of the Association for Information Systems 5 (11–12) (2004) 494–513.

[53] C. Wiertz, K. de Ruyter, Beyond the call of duty: why customers contribute to <sup>fi</sup>rm-hosted commercial online communities, Organization Studies 28 (3) (2007) 347–376.

[54] Wikipedia, Wikipedia: Featured Article Statistics, available at: http://en.wikipedia org/wiki/Wikipedia:Featured\_article\_statistics, (last accessed on October 11, 2012).

[55] S. Wu, Linear combination of component results in information retrieval, Data & Knowledge Engineering 71 (1) (2011) 114–126.

[56] X. Wu, V. Kumar, J. Ross Quinlan, J. Ghosh, Q. Yang, H. Motoda, G.J. McLachlan, A. Ng, B. Liu, P.S. Yu, Top 10 algorithms in data mining, Knowledge and Information Systems 14 (1) (2008) 1–37.

[57] Y. Yang, An evaluation of statistical approaches to text categorization, Information Retrieval 1 (1) (1999) 69–90.

[58] D. Yimam-Seid, A. Kobsa, Expert Finding Systems for Organizations: Problem and Domain Analysis and the DEMOIR Approach, Sharing Expertise: Beyond Knowledge Management, MIT Press, Cambridge, MA, 2003.

[59] W. Zhang, S. Watts, Knowledge adoption in online communities of practice Systemes d'Information et Management 9 (1) (2003) 81–102

[60] H. Zhang, A. Goel, R. Govindan, K. Mason, B. Van Roy, Making eigenvector-based reputation systems robust to collusion, Algorithms and Models for the Web-Graph (2004) 92–104.

[61] J. Zhang, M. Ackerman, L. Adamic, K. Nam, Qume: a mechanism to support exper tise <sup>fi</sup>nding in online help-seeking communities, The ACM Symposium on User Interface Systems and Technology, ACM, 2007, p. 114.

[62] J. Zhang, M.S. Ackerman, L. Adamic, Expertise networks in online communities: structure and algorithms, Proceedings of the 16th International World Wide Web Conference (WWW), Banff, Canada, 2007.

![](/api/attachments/QJC2MWED/fulltext/images/478716db1d049b1356a98bbb41a91a8f8e44ee8da9d3e28a38007225dd092a3b.jpg)  
G. Alan Wang is an Assistant Professor in the Department of Business Information Technology, Pamplin College of Busi ness, at Virginia Tech. He received a Ph.D. in Management Information Systems from the University of Arizona, an M.S. in Industrial Engineering from Louisiana State University, and a B.E. in Industrial Management & Engineering from Tianjin University. His research interests include heteroge neous data management, data cleansing, data mining and knowledge discovery, and decision support systems. He has published in Communications of the ACM, IEEE Transactions of Systems, Man and Cybernetics (Part A), IEEE Computer, Group Decision and Negotiation, Journal of the American Society for Information Science and Technology, and Journal of Intelligence Community Research and Development.

![](/api/attachments/QJC2MWED/fulltext/images/f55a55c8034358ef47605d3f560b9c5567a0d6c303307e2be1493fbbc5d4fb36.jpg)  
Jian Jiao is a Ph.D. candidate in Computer Science at Virginia Tech and a Software Design Engineer at Microsoft. He holds an M.S. in Computer Science from the Beijing Institute of Technology, and has previous work experience at Microsoft Research Asia and Motorola.

![](/api/attachments/QJC2MWED/fulltext/images/e02c0e8b02921ca86d9967c2ea292792d9387a6fec0f4771cf9e9c996cb5a0e7.jpg)

Alan S. Abrahams is an Assistant Professor in the Department of Business Information Technology, Pamplin College of Business, at Virginia Tech. He received a Ph.D. in Computer Science from the University of Cambridge, and holds a Bachelor of Business Science degree from the University of Cape Town. Dr. Abrahams's primary research interest is in the application of decision support systems in entrepreneurship. He has published in a variety of journals including Expert Systems with Applications, Journal of Computer Information Systems, Communications of the AIS, and Group Decision and Negotiation.

![](/api/attachments/QJC2MWED/fulltext/images/f80a5ac3a74a3271b0fed688ae2e6802c8e5ec3f1a7afcfad7391d4e217b30c6.jpg)

Weiguo (Patrick) Fan is a Full Professor of Accounting and Information Systems and Full Professor of Computer Science (courtesy) at the Virginia Polytechnic Institute and State University (Virginia Tech). He received his Ph.D. in Business Administration from the Ross School of Business, University of Michigan, Ann Arbor, in 2002, a M.S. in Computer Science from the National University of Singapore in 1997, and a B.E. in Information and Control Engineering from the Xi'an Jiaotong University, P.R. China, in 1995. His research interests focus on the design and development of novel information technologies – information retrieval, data mining, text/web mining, business intelligence techniques – to support better business information management and decision making. He has published more than

100 refereed journal and conference papers. His research has appeared in journals such as Information Systems Research, Journal of Management Information Systems, IEEE Transactions on Knowledge and Data Engineering, Information Systems, Communications of the ACM, Journal of the American Society on Information Science and Technology, Information Processing and Management, Decision Support Systems, ACM Transactions on Internet Technology, Pattern Recognition, IEEE Intelligent Systems, Pattern Recognition Letters, International Journal of e-Collaboration, and International Journal of Electronic Business.

![](/api/attachments/QJC2MWED/fulltext/images/dd72dc005c8581ad876fcef4b99ab6cdb17b88d00af7aa8b4b7ccc26010f9dcb.jpg)

Zhongju (John) Zhang is an Associate Professor in the School of Business, University of Connecticut. He received his Ph.D. in Management Science (with minors in Economics and Operations Management) from the University of Washington Business School. Zhang's research focuses on the problems at the interface of information systems/ technologies, marketing, economics, and operations research His research has been published in academic iournals including Information Systems Research, INFORMS Journal on Computing, Journal of Management Information Systems, IEEE Transactions on Engineering Management, Decision Support Systems, European Journal of Operational Research, Communications of the ACM, Decision Sciences Journal, as well as in various international conference proceedings.

Zhang was a co-recipient of the Best IS Publications of the Year 2010. He has also won the Research Excellence Award (2011), the MBA Teacher of the Year (2010), the Best Paper Award (2009), and the Ackerman Scholar Award (2007–2009) at the UConn School of Business. Zhang is a guest associate editor for MIS Quarterly and serves on the editorial board of Journal of Database Management, Journal of Electronic Commerce Research, and Electronic Commerce Research and Applications.
