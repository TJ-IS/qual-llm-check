---
otero_id: 4398
otero_key: "DDYAQPCP"
title: "Do search terms matter for online consumers? The interplay between search engine query specification and topical organization"
authors: "Nanda Kumar; Karl R. Lang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Do search terms matter for online consumers? The interplay between search engine query specification and topical organization

Nanda Kumar <sup>⁎</sup>, Karl R. Lang

Zicklin School of Business, Computer Information Systems Department, Baruch College, City University of New York, 55 Lexington Avenue, Box B11-220, New York, NY 10010, USA

Received 2 July 2005; accepted 25 March 2007 Available online 30 March 2007

## Abstract

The Internet has become the primary source of information for a large number of consumers. Thus, search engines as the mediators between consumers and online information is an increasingly important topic of research. The present study contributes specifically to the research in consumer search and decision-making by investigating how a search engine's support for topical organization of search results can help improve search performance. Search term formulation is an integral part of the online search process that consumers conduct. Past research shows that the actual search terms used in search queries do matter for improving search performance and also that users often mis-specify search terms, thereby reducing the efficacy of their online search and decision-making. The results of our experimental study offer evidence that topical organization using clustering support, which is provided by some search engines, helps increase relevance and usefulness of search results. The strongest performance improvements were achieved when clustering support was used in combination with terms that were under-specified. © 2007 Elsevier B.V. All rights reserved.

Keywords: Consumer decision-making; Consumer search; Electronic commerce; Search engines; Search strategies; Query formulation; Clustering; Online shopping

What information consumes is rather obvious: it consumes the attention of its recipients. Hence, a wealth of information creates a poverty of attention and a need to allocate that attention efficiently among the overabundance of information sources that might consume it.

Herbert Simon, Nobel Laureate Economist

## 1. Introduction

A consumer generally has several channels to access information before making purchasing decisions. Some of the traditional information sources include conventional mass media (e.g. magazines, newspapers, television, and radio), people (e.g. friends, and experts), sellers (e.g. stores, sales representatives, catalogs, and advertisements), and personal experience (e.g. observations and product trials). Since the explosion of the World Wide Web in the 1990's, the Internet has become an increasingly important information source for consumers. Recent surveys show that about 120 million American adults (84% of the adult Internet population in the USA) have used search engines in the past and that about 59 million American adults are using search engines on a typical day [39]. A shopper may use Web search tools to look up pre-purchase product information (prices, designs, styles, reviews, etc.), even if the transaction is ultimately executed offline. Competing with Web directories, catalogs and online databases, search engines have quickly become primary consumer decision support tools [31]. Since search cost is an important factor affecting consumers' purchase decisions [48,47], consumers usually tend to develop some search strategies to better manage the search process and to reduce search cost. Online consumer search strategies include the choice and usage of search engines, query formulation tactics, stopping rules, and filtering mechanisms, as well as heuristics aimed at coping with the vast amount of information that search engines typically return. However, search strategies are usually implicitly formulated and are rarely documented in any explicit terms. In fact, online shoppers may not even be aware that they follow certain patterns that can be construed as search strategies. They tend to develop their personal strategies over time as they gain experience with offerings on e-commerce sites and become familiar with the IT tools required to support consumer searches and decision-making [c.f., e.g., [26].

Search engines are considered efficient and effective tools for reducing consumer search cost because they cover a huge amount of Web content, provide users with immediate access, present customized and personalized consumer information, and do not charge for their service [2]. Though the use of search engines is free to users, this does not mean that the economical search cost is zero because users still need to spend a significant amount of time and cognitive effort when searching and then processing the found information [54]. Considering search time as well as overall satisfaction with the search process and its outcomes and the eventual consumer decision, we find from personal experience, anecdotal evidence as well as from practice reports many cases where search engines may not guarantee low search cost at all [18]. In other words, search engines may very well be effective in finding specific information but could have limited capabilities when it comes to complex consumer searches and consumer decision support. Nevertheless, in the digital consumer economy, search engines are among the principle tools people use<sup>2</sup> when they shop online [7].

For example, search engines often produce information overload with many thousands of hits returned to the user in response to a simple query. The subsequent filtering and processing that are required to make the information manageable and useful can create significant search costs [54]. A user who doesn't know how to formulate effective queries or doesn't know how to efficiently narrow down these hits to a small set of relevant ones, which still need to be read and processed, may feel frustrated or dissatisfied with the search process. Hence, in many cases, online shopping may incur search costs that are significant.

Finally, search engines may, of course, just fail to find the consumers' desired products or information at all. This could be because the sellers never put the information out, the information is out but the search engine failed to retrieve it, or the user doesn't recognize that the needed information or best product offer has actually already been found. And to complicate matters, users typically modify their initial search task in the process, and change and shift expectations [45] as they learn about touted and realistic shopping possibilities in the process. Therefore, consumers often alter and extend their search beyond their original intentions. Subjective factors like personal satisfaction and pleasure with the process and outcome of an online shopping experience may be more important in determining success and effectiveness of consumer searches than objective utilitarian criteria [22,27].

Undoubtedly, the Internet has and will continue to impact consumer information search behavior. The Internet tends to be the initial and primary source of information for most consumers who use the Internet on a regular basis, thus decreasing the usage and importance of traditional information sources [38]. In addition to search engine technology itself, it is the human–technology interaction that is most important to the usability and effectiveness of search engines in e-commerce [46]. The present study contributes to the research in consumer search and decision-making in online shopping environments. We are particularly interested in the question of how the specific design of a search engine – that is the IT artifact – that guides users in their consumer searches, impacts search outcome and decision-making. Search engine designs differ along several dimensions, including user interface, search algorithms, index coverage and construction, and the organization and presentation of information retrieved. This paper specifically examines two different conceptual designs for presenting search information to the user, namely topical and sequential organization. The study adds to our understanding on the determining factors of search performance by investigating the interaction between the search terms used by consumers and clustering support, a specific form of topical organization, offered by some search engines.

The rest of this paper is organized as follows. The next section reviews relevant literature while Section 3 develops the research model tested in this paper. Section 4 discusses the research design and Section 5 presents the results of the study. We conclude, in Section 6, with a discussion of the potential implications of our research and an outline of future research directions.

## 2. Relevant literature and theoretical background

We are specifically concerned with search performance in online shopping environments. Two largely disjoint streams of literature are particularly relevant to the present research. The role of search cost on consumer decision-making and market efficiency has been analytically and theoretically studied in the information economics and e-commerce field. Online information search, primarily outside the context of e-commerce interactions, has been studied in the information retrieval literature. Since this paper addresses issues at the intersection of technical research on information search, user behavior in online shopping environments, and the economic implications of search cost in terms of consumer decisions we need to briefly review relevant work in information economics and e-commerce theory as well as in information retrieval.

## 2.1. Information economics and electronic commerce research

Classic economic theory asserts that presence of positive consumer search cost (in physical markets) creates market inefficiency in terms of higher, noncompetitive prices charged by sellers. In general, sellers know more about the products and services they sell than consumers do. Sellers can exploit the resulting information asymmetry by charging monopolistic prices [48,47]. Consumers conduct information searches in order to reduce uncertainty about prices, quality, characteristics, and availability of the products and services they are looking for [54,14]. In the physical world, consumer search requires store visits, telephone calls, reading advertisements, or talking to other people to find out more about market offerings. Each search activity incurs some cost in terms of transportation or time and effort spent on obtaining and processing consumer information. Hence, the more one searches, the higher the accruing search cost. If finding the seller who offers the lowest possible price is difficult, it may be more economical to buy from a seller who charges a higher price because of the search cost incurred [49].

Search engines have emerged as consumer tools in online markets brokering seller information to consumers who are looking for certain products or services. Because of technology, consumers can now perform powerful online searches simply by issuing queries that are made up of a few basic search terms. One query can simultaneously retrieve consumer information from multiple sellers and other sources. Search results are also automatically organized, allowing users to store and further process information thus obtained [54]. Hence, search intermediaries – and search engines, in particular – should increase search efficiency and significantly lower consumer search cost. If search engines succeeded in providing consumers with information that is complete, precise, accurate, and trustworthy, search cost could potentially be driven down to zero or close to zero [5]. Traditional theoretical economics models maintain that positive search cost, even if infinitesimally small, will allow sellers to pursue monopolistic pricing strategies [19]. However, more recent studies in the information economics and e-commerce literature typically assume that technology has reduced search cost to zero or quasizero, and assert that negligible search cost should drive prices towards competitive price levels at or near marginal cost [6].

From a theoretical point of view, markets are efficient if all possible trades get executed and all sales transactions occur at the lowest possible price. Theoretically, this competitive price would be uniquely determined as the marginal cost price. Information asymmetries are considered the most significant source for creating market inefficiencies. Hence, reducing consumer search cost is widely regarded as an important driver for increasing market efficiency [43]. Electronic markets like, for example, electronic retailing over the Web, have the potential to become nearly frictionless markets if online search tools (esp. search engines) allow consumers to easily find the right products at the right prices [32,53]. Lower search costs should lead to lower prices for both homogeneous and differentiated goods [5].

Some empirical research has been conducted in an effort to support the theoretical prediction that electronic markets perform more efficiently than traditional markets. The electronic market efficiency hypothesis would be supported if prices found in electronic sales channels were lower and varied less than in the corresponding physical channels. While evidence has been found that price levels might indeed be lower in electronic markets [43,11], there remains significant friction. Substantial levels of price dispersion have been found in three important homogeneous product categories; books, CDs, and air tickets [11,16]. Most studies black-box the design of the underlying IT artifact and assume generally that search engines have the capability to dramatically reduce or eliminate search costs in homogeneous markets [43]. Little research has been done studying efficiency and pricing in markets of more complex and more differentiated products and services. Likewise, to the best of our knowledge, little empirical work is available that examines the impact of different search engine technology designs in terms of specific search support functions on consumer search performance and market behavior.

## 2.2. Information search and retrieval research

The information search literature has proposed a number of independent variables (antecedents) that influence user search behavior (see Table 1). Most studies focus on two dependent variables: search outcome (or search performance) and search process. Search processes are the observed search paths and patterns that result from all the search interactions. Search outcomes are the consequences of search behavior, usually measured with precision and recall<sup>3</sup> [10], which are quite appropriate measures if the correctness of the search result is known or objectively verifiable. While such objective measures are appropriate for traditional information comprehension situations [33], the application of such measurements has some problems with regard to product and consumer searches [46]. Consumers who perform complex, open-ended search tasks don't know what is out there on the Web and may have difficulty verifying the “correctness” of search results. Moreover, recent research suggests that users tend to evaluate the search process and outcome based on their individual satisfaction rather than correctness [46,1,44,34].

Behavioral variables: a summary from the information search literature

<table><tr><td>Research article</td><td>Independent variables</td><td>Dependent variables</td></tr><tr><td>Borgman, Hirsh and Hiller [11]</td><td>1. Search task (type of search, subject domain)2. Searcher characteristics (experience, training, time spent on searching)</td><td>Search outcomes (precision, recall)Search timeSearch paths</td></tr><tr><td>Schmidt and Spreng [41]</td><td>Ability to searchMotivation to searchCosts of searchBenefits of search</td><td>External information search</td></tr><tr><td>Moorthy, Ratchford and Talukdar [37]</td><td>Consumer&#x27;s prior brand perceptionsConsumer expertise and knowledge</td><td>Search strategies</td></tr><tr><td>Yuan [58]</td><td>Search experience</td><td>User&#x27;s command and feature repertoireLanguage usage patternError patternSearch speedAttitude</td></tr><tr><td>Hsieh-Yee [29]</td><td>Search experienceSubject knowledge</td><td>End-user search tactics</td></tr><tr><td>Hoischer and Strube [28]</td><td>Web experienceDomain-specific knowledge</td><td>Search tacticsSearch process</td></tr><tr><td>Spink et al. [46]</td><td>Search taskUncertaintyCognitive stylesSuccessive search behavior</td><td>Search successSearch processesInformation-seeking episodes</td></tr></table>

Capabilities of search engines refer to the technological functions and features that search engines provide to improve end-users' usability and effectiveness [44]. Previous studies have explored both contextrelated (user interface) and content-related (search results) capabilities. Chu and Rosenthal [15] compared and evaluated retrieval performance based on search term specification capabilities like Boolean logic operators, truncation, field search, word and phrase search. Bradlow and Schmittlein [10] investigated links between overall search performance and a search engine's structural and technical properties including search engine size, depth, frame support, image maps and learning frequency. Both studies found that search engine capabilities affect search performance. Besides content-related capabilities, search engines provide nonsearch capabilities [50] built into their user interfaces to enhance usability. These include non-personalized features such as directories, news, weather, maps, animations, and advertising. They also include personalized features such as emails, chat rooms, bulletin boards and personalized home pages [21]. A recent study [23] finds that animation and advertising banners impact user behavior significantly. Some search engines provide non-personalized features only, while others embed the search interface within a Web portal that contains both personalized and non-personalized features. One major difference is that personalized features require users to provide the system with information about their personal identity so that access to the personalized area can be protected, usually with a username and password. However, disclosing personal information generally interferes with privacy and may influence consumers' usage of online search tools [3]. Non-search features in general may affect users preference for search engines [50].

Users typically perform various search tasks. Some are easy to define and specify, while some are complex; some are specific while others are general. In a largescale study on search behavior of online consumers shopping for commodity-like products, Johnson et al. [30] found that experienced and active Internet shoppers search longer and explore more sites than less experienced and active users. The type of the search task has also been identified as a significant factor affecting users' search behavior [9,28]. Complexity [9,28] and risk [25] are important dimensions when measuring differences between types of search tasks. Simple tasks are typically straightforward fact-based questions with known answers that a user intends to find, while complex tasks are typically more researchbased or open-ended [8]. For example, when searching for commodity-like products such as a specific textbook, which is easily and completely specified with book title, author and edition, the complexity is low. But a search task like finding the “best” textbook on DSS or even finding something vaguely defined as a “nice vacation package” is only incompletely specified and is much more complex due to its openness to multiple meanings and many possible “correct” answers. Both scenarios are quite common. But high impact search tasks (e.g. shopping for a product with serious financial consequences) are often also more complex than lowimpact search tasks. When search tasks have high complexity, users may spend more time refining queries, filtering information and identifying search results, thus leading to higher search cost [30].

## 3. Research model

All search engine designs include some specific software technology features that are aimed at helping users organize and manage search results. One of the most promising new features that have recently been introduced is clustering. Other innovations include, for example, provision of search histories, local search, domain-specific search, mobile search, foreign language search, and personalized search. All user searches begin with entering a search query. A search query is composed of search terms, which are formulated and supplied by the user. The effectiveness of search terms is dependent on the search context. Users may in some cases specify search terms that work very well. In other cases, though, they may mis-specify a query by using ineffective or incorrect terms. They may under-specify by using too few terms, or over-specify by using too many terms unnecessarily. In any case, the quality of search terms used for particular search tasks is likely to affect the outcome of the search. The user–technology interaction, that is, in this case, the interplay between search engine technology features and user-generated query formulations, plays a role in determining overall search performance (see Fig. 1). To some degree, technology may offset or amplify user mistakes. This research utilizes users' perception of usefulness and relevance of individual search results as indicators of quality of the search results and hence, indicators of users' perception of search engine performance.

## 3.1. Topical organization of search results: technology support with clustering

A typical search query to a search engine retrieves thousands or millions of search results. One way to deal with information overload is to use an algorithm that displays the search results ordered by some relevance criterion. Google, for example, designed their search algorithm by incorporating a measure of “authority” of web sites to display more popular web sites first, assuming that those are also the more relevant to most users. Web sites can also reduce information overload by providing some additional organizing support, where instead of just providing a long list of search results, the search engine groups the search results in a meaningful way, for example, by topical clusters. Clustering is a powerful technique that has been used in Information Retrieval extensively to improve the relevancy

![](/api/attachments/DDYAQPCP/fulltext/images/0af7d36e4b07da318ea3da11a067543150c8a18a735b61cab91b6ae68093f8f7.jpg)  
Fig. 1. Conceptual research model.

<table><tr><td rowspan="2">Subjects</td><td colspan="4">Search Engine #1</td><td colspan="4">Search Engine #2</td><td colspan="4">Search Engine #3</td></tr><tr><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td></tr><tr><td>1</td><td> $20^8$ </td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>2</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr></table>

T1 - Search Term 1; T2 - Search Term 2 etc.  
§- 10 ratings for usefulness and 10 ratings for relevance

Fig. 2. Research design.

of retrieved results as well as usability [4,40,42,52]. Clustering is emerging as a major particular organizing feature that is already employed by several commercial search engines [35,13,12]. With clustering, users can better access results, grouped by theme or category, by clicking on the category that they believe is most relevant to their search task.

For example, the search engines Teoma, Vivisimo, and Clusty can categorize their search results on the fly, aiming to help users focus their search and refine the results. The clustering capability has been chosen as the differentiator of search engine capabilities in our study. According to [12], cluster-based representations – such as those used by the search engine Clusty<sup>4</sup> that we have chosen for our experiment – help users in processing and responding to large amounts of information, and thus help them find the information they've been looking for more easily. More specifically, clustering helps users sort the search results by categories, filters results more effectively and refines their search queries. Search engines with clustering features are supposed to help consumers with their online shopping searches and should improve search performance as indicated by relevance and usefulness of the search results. While clustering does not help users with the task of formulating queries, it does provide a technical solution by seeking to make searches more robust against poorly specified user queries. Clustering methods extract relevant hits, which might be scattered anywhere in the result list, and organizes them into meaningful and easily accessible categories.

H1a. Consumers will consider the search results from search engines with clustering support to be more relevant to their task at hand than those that offer no clustering support.

H1b. Consumers will consider the search results from search engines with clustering support to be more useful to their task at hand than those that offer no clustering support.

## 3.2. Specification of search terms

Under-specification is the most common form of query mis-specification [4,40,56]. Previous research has shown that most of the search terms supplied by search engine users are short and simple in structure, and hence, often under-specify the intended search problems [45,56]. Moreover, users rarely use advanced search features – such as logical operators – and when they do, they use them erroneously or ineffectively about half the time [56]. Other studies have shown that having domain knowledge about the search problem context increases users' ability to specify better search terms [56,55].

Under-specification of search terms occurs when users visit a search engine with a specific task in mind, but specify search terms that do not adequately represent the search problem they are trying to solve. The difficulty users have in formulating search queries has been well documented [24,36]. There are two main reasons. Users may not always know what exactly they are looking for or they may have problems supplying search terms that accurately match the terms that are actually used by search engines for indexing the links to online resources. In an effort to address this problem, some search engine designs include features to correct misspellings and also incorporate some semantic information that allows them to handle synonyms and homonyms — when retrieving information [55,51]. However, current search and retrieval technology remains limited when analyzing user-generated queries that, all too often, contain insufficient, incomplete, ambiguous, or context-depended search terms [57].

Hence, we posit that mis-specified, and, in particular, under-specified consumer query formulations perform less well than properly specified queries.

H2a. Consumers who under-specify the search terms will find the search results less relevant than those who specify the search terms well.

H2b. Consumers who under-specify the search terms will find the search results less useful than those who specify the search terms well.

## 3.3. Interaction effect

This research further argues that search engine's clustering support has a differential effect on search engine performance based on how well search terms are specified. When users under-specify search terms, search engines that do not support clustering are expected to produce overall less relevant and less useful search results. Most users tend to restrict their attention to search results that are presented at the top, that is, they will primarily consider hits delivered on the first page, and perhaps those returned on the second and, occasionally, the third. But they will rarely examine results that appear further down the list. Rather than exploring all result pages, users reformulate a query and launch a new search [45]. Thus, while search engines will generally return a number of good results, even when queries are poorly formulated, the retrieval algorithm will likely strew relevant and useful hits across all result pages, mixed together, in a quasi-random fashion, with bad results. Consequently, the odds are that users will miss good information that would help them solve their search task. On the other hand, a search engine with support for clustering organizes results automatically into themed categories. By taking a flat list of search results whose order only partially reflects relevance and usefulness (in the user's mind) and introducing a second info-structural level through creating categories, clustering increases order in the search space and helps users focus their attention on the more relevant and useful search results. Hence, using search technology support features like clustering may increase the likelihood that consumers will find upfront the results they are looking for when performing consumer searches.

This beneficial effect of clustering may be less evident when the search terms are well specified as traditional methods are powerful enough to identify good results and place them at the front pages of the result list when query formulations include sufficiently complete and unambiguous information. A subsequent reordering or restructuring of the results may not significantly improve search performance. Hence, we propose that there is an interaction effect between clustering support and search term specification that plays a significant role in determining overall search performance.

H3a. When consumers under-specify search terms, search engines with clustering support will produce more relevant search results compared to those without clustering support. But the better the search term specification, the smaller the difference.

H3b. When consumers under-specify search terms, search engines with clustering support will produce more useful search results compared to those without clustering support. But the better the search term specification, the smaller the difference.

## 4. Research methodology

## 4.1. Research design

A 2 × 3 experiment was conducted to test the research model shown in Fig. 1. The sample size of the study was 60. The participants were recruited from a large public university on the East coast of the United States. The specification of search terms was manipulated at two levels: under-specified and well-specified search terms. Clustering support provided by search engines was operationalized at three levels: the search engine Google as a control group, and the search engine Clusty with and without clustering support. While Google does not provide clustering support, it was included in the study as a control group because of its reputation and its status as the most widely used and trusted search engine. Clusty is a new search engine developed by Vivisimo, Inc.<sup>5</sup>, that provides search results both with and without clustering. It presents the search results unclustered and with the top ten hits displayed on the first page. In addition, it also shows a list of categories on the left hand side of the screen that contains topical clusters that were automatically created from the original search results. Users can explore the different clusters of search results by clicking on categories. In both cases, Clusty runs the same search and retrieval algorithm to generate the original, unclustered list of search results. Hence, any differences users might perceive between the two search modes must be attributed to the clustering mechanism. This, of course, does not extend to Google, which uses its own, different algorithm to build (unclustered) result lists. At the time of this writing,

Google does not offer clustering support. In our study, both treatments – specification of search terms (2 levels) and search engine capability vis-à-vis clustering support (3 levels) – were with-in subject treatments, that is, each participant was exposed to all 6 levels of treatments.

We asked the participants to evaluate the unclustered search results from Google and Clusty. They were also asked to evaluate the results from Clusty with clustering support by exploring the clusters suggested by the search engine. Appendix A shows the screenshot where the search engine Clusty returns the top 10 unclustered results on the first page in response to a user search for “MP3 Player.” This screenshot also shows the clusters generated by the search engine on the left hand side. Appendix B shows the subsequent screenshot where the user has already selected one of them, the cluster “Review”. The corresponding top 10 results for this cluster are again listed on the first page. Among all of the results found, this cluster gathers all search results that have to do with (product) reviews in the original search context “MP3 Player.”

## 4.2. Procedures

In order to establish a common search task context, all participants were asked to imagine a scenario where they were shopping for an MP3 player to, among other things, listen to music during their commute to school or work. To accomplish this task, the participants were asked to enter search terms and examine the results using the search engine interfaces described above. They were told to limit their attention to only the top 10 hits delivered by the three search engines, that is, the Google (unclustered), Clusty (unclustered), and Clusty (clustered). The top 10 hits from Clusty with clustering support were obtained from the cluster that the users deemed most promising (in terms of relevance and usefulness).

Table 2  
Descriptive statistics for relevance

<table><tr><td rowspan="2"> $S^§$ </td><td rowspan="2">T</td><td rowspan="2">Mean</td><td rowspan="2">Standard error</td><td colspan="2">95% confidence interval</td></tr><tr><td>Lower bound</td><td>Upper bound</td></tr><tr><td rowspan="2">1</td><td>1</td><td>5.297</td><td>.112</td><td>5.072</td><td>5.522</td></tr><tr><td>2</td><td>3.073</td><td>.170</td><td>2.733</td><td>3.414</td></tr><tr><td rowspan="2">2</td><td>1</td><td>4.988</td><td>.122</td><td>4.744</td><td>5.232</td></tr><tr><td>2</td><td>3.230</td><td>.173</td><td>2.883</td><td>3.577</td></tr><tr><td rowspan="2">3</td><td>1</td><td>4.980</td><td>.144</td><td>4.691</td><td>5.269</td></tr><tr><td>2</td><td>4.032</td><td>.138</td><td>3.756</td><td>4.308</td></tr></table>

<sup>§</sup>10 ratings for usefulness and 10 ratings for relevance.

Table 3  
Descriptive statistics for usefulness

<table><tr><td rowspan="2">S</td><td rowspan="2">T</td><td rowspan="2">Mean</td><td rowspan="2">Standard error</td><td colspan="2">95% confidence interval</td></tr><tr><td>Lower bound</td><td>Upper bound</td></tr><tr><td rowspan="2">1</td><td>1</td><td>5.210</td><td>.109</td><td>4.993</td><td>5.427</td></tr><tr><td>2</td><td>2.905</td><td>.173</td><td>2.560</td><td>3.250</td></tr><tr><td rowspan="2">2</td><td>1</td><td>4.830</td><td>.111</td><td>4.608</td><td>5.052</td></tr><tr><td>2</td><td>2.993</td><td>.165</td><td>2.662</td><td>3.324</td></tr><tr><td rowspan="2">3</td><td>1</td><td>4.892</td><td>.168</td><td>4.556</td><td>5.228</td></tr><tr><td>2</td><td>3.843</td><td>.133</td><td>3.576</td><td>4.110</td></tr></table>

S — Search engine; T — Search terms.  
S1: Google (no clustering).  
S2: Clusty without clustering.  
S3: Clusty with clustering.  
T1: Well-specified search terms.  
T2: Under-specified search terms.

The participants were given two well-specified search terms (“buy MP3 player”, “compare MP3 player”) and two under-specified search terms (“MP3 player”, “MP3”). The participants were instructed to use only these four search terms to accomplish their search tasks. The under-specified search terms are typically shorter and simpler terms relatively devoid of contextual cues relevant to the task at hand. The underspecified term “MP3 player” used in this study ignores the context of the users shopping for MP3 players while the under-specified search term “MP3” ignores both the shopping as well as music player context. Hence, we argue that “MP3” and “MP3 player” are relatively under-specified when compared to the terms “buy MP3 player” and “compare MP3 player” for the task at hand.

The participants used the Internet browser available on the lab computer to look up the search results, but were instructed to use paper-based directions and survey sheets to record their evaluations. Each participant was exposed to all six levels of treatments– 2 levels of search term specifications and 3 levels of search engine capability – as shown in Fig. 2. For each search engine interface, the participants used each of these four search terms. While the order of presentation of the search engines was randomized in the study, the order of presentation of search terms was not because of the logistical difficulty of manually administering the survey. The last section of the paper acknowledges this lack of randomization of search terms as a potential limitation of the study due to possible learning effects. However, that section also discusses how the results of the study indicate absence of such learning effects, thus mitigating the impact of this limitation.

![](/api/attachments/DDYAQPCP/fulltext/images/6c8f9164f28d4b2671e672966d5da00c9f8bcb87b93bf7cb319f0e896f043992.jpg)  
Fig. 3. Box plot for relevance.

![](/api/attachments/DDYAQPCP/fulltext/images/ef0b9e69fb45944ef9d1846c30c357579d86889ea4126e24691c6dcef824aa4d.jpg)  
§: S - Search Engine; T - Search Terms  
S1: Google (no clustering) S2: Clusty without clustering S3: Clusty with clustering  
T1: Well-specified search terms T2: Under-specified search terms

For each of the given search terms (buy MP3 player, compare MP3 player, MP3 player, MP3), the participants rated the top 10 search results in terms of their relevance and usefulness for solving the search task at hand. Most participants spent between 50–80 min to complete the study. While previous research has typically measured relevance as a yes–no binary variable, this research measures relevance and usefulness with the 7-point Likert scale items (1 indicating strongly disagree and 7 indicating strongly agree) listed below. We expect both measures to be highly correlated as search results that are relevant are likely to be perceived as being useful by the participants. Both relevance and usefulness can be treated as indicators of quality of the search results and high correlation between these two items should suggest that the results of the research study are robust.

Table 4  
ANOVA results for relevance

<table><tr><td>Source (IV)</td><td>Sum of squares</td><td>df</td><td>Mean square</td><td>F</td><td>Sig</td><td>Effect size ( $\eta_p^2$ )</td></tr><tr><td>Support for clustering (CL)</td><td>6.18</td><td>1</td><td>6.18</td><td>11.1</td><td>0.002</td><td>0.16</td></tr><tr><td>Search terms (ST)</td><td>243.05</td><td>1</td><td>243.05</td><td>159.3</td><td>0.000</td><td>0.73</td></tr><tr><td>CL * ST</td><td>23.38</td><td>1</td><td>23.38</td><td>48.7</td><td>0.000</td><td>0.45</td></tr></table>

Fig. 4. Box plot for usefulness.  
Table 5  
ANOVA results for usefulness

<table><tr><td>Source (IV)</td><td>Sum of squares</td><td>df</td><td>Mean square</td><td>F</td><td>Sig</td><td>Effect size ( $\eta_p^2$ )</td></tr><tr><td>Support for clustering (CL)</td><td>5.77</td><td>1</td><td>5.77</td><td>9.3</td><td>0.003</td><td>0.13</td></tr><tr><td>Search terms (ST)</td><td>269.36</td><td>1</td><td>269.36</td><td>193.0</td><td>0.000</td><td>0.77</td></tr><tr><td>CL * ST</td><td>23.69</td><td>1</td><td>23.69</td><td>39.6</td><td>0.000</td><td>0.47</td></tr></table>

Relevance: The web site corresponding to this link is likely to have relevant information to help complete my task.

Usefulness: The web site corresponding to this link is likely to have useful information to help complete my task.

All search engines displayed 10 search results on the first page by default. The participants rated these

Table 6  
Descriptive statistics for precision (P@10)

<table><tr><td rowspan="2">S</td><td rowspan="2">T</td><td rowspan="2">Mean</td><td rowspan="2">Standard error</td><td colspan="2">95% confidence interval</td></tr><tr><td>Lower Bound</td><td>Upper Bound</td></tr><tr><td rowspan="2">1</td><td>1</td><td>.798</td><td>.025</td><td>.748</td><td>.847</td></tr><tr><td>2</td><td>.325</td><td>.035</td><td>.254</td><td>.395</td></tr><tr><td rowspan="2">2</td><td>1</td><td>.717</td><td>.026</td><td>.666</td><td>.769</td></tr><tr><td>2</td><td>.365</td><td>.036</td><td>.292</td><td>.437</td></tr><tr><td rowspan="2">3</td><td>1</td><td>.734</td><td>.030</td><td>.675</td><td>.793</td></tr><tr><td>2</td><td>.518</td><td>.030</td><td>.458</td><td>.577</td></tr></table>

S — Search engine; T — Search terms.  
S1: Google (no clustering).  
S2: Clusty without clustering.  
S3: Clusty with clustering.  
T1: Well-specified search terms.  
T2: Under-specified search terms.

![](/api/attachments/DDYAQPCP/fulltext/images/fe0a286b24104be8e52c44f180ecf8563c637912e8b392d63b92a915e84143cf.jpg)  
Fig. 5.

10 search results for usefulness and relevance thus generating 20 individual ratings per cell and a total of 240 ratings per participant (see Fig. 2). We used the individual ratings for only the first 10 search results as previous research has demonstrated that consumers of search engines typically looked at only the first page of the search results and clicked on the first few search results at the top of the page [45,56]. Participants were asked to ignore sponsored links that the search engines showed in addition to their regular results. That is, sponsored links were not used in the computation of the relevance and usefulness scores.

The 10 ratings for relevance corresponding to the top 10 search results were averaged to arrive at a single score for relevance for each search term the user entered (four search terms, thus yielding four scores). The score for each level of search term specification was computed by averaging the scores of two search terms that were used in the operationalization (e.g., the scores for the search terms “buy MP3 player” and “compare MP3 player” were averaged to obtain a final score for well-specified search terms condition). The same procedure was followed to arrive at a single score per cell per subject for usefulness. These two dependent variables – relevance and usefulness – were used to analyze the impact of the two independent variables.

![](/api/attachments/DDYAQPCP/fulltext/images/09a75a5b6e5dfe91465dd28168f8499b1224cd214d629f06aa191357b5e837bd.jpg)  
Fig. 6. 2 × 3 interactions (usefulness).

Table 7  
ANOVA results for precision (P@10)

<table><tr><td>Source (IV)</td><td>Sum of squares</td><td>df</td><td>Mean square</td><td>F</td><td>Sig</td><td>Effect size ( $\eta_p^2$ )</td></tr><tr><td>Support for clustering (CL)</td><td>0.25</td><td>1</td><td>0.25</td><td>8.7</td><td>0.005</td><td>0.13</td></tr><tr><td>Search terms (ST)</td><td>10.86</td><td>1</td><td>10.86</td><td>181.4</td><td>0.000</td><td>0.76</td></tr><tr><td>CL*ST</td><td>0.99</td><td>1</td><td>0.99</td><td>39.4</td><td>0.000</td><td>0.40</td></tr></table>

## 5. Results and discussion

Tables 2 and 3 show the descriptive statistics for relevance and usefulness of the search results, respectively. Figs. 3 and 4 show the effect of the six experimental treatments on the two dependent variables using box plots. Tables 4 and 5 report the ANOVA results (repeated measures ANOVA) showing the impact of the two independent variables (clustering support and specification of search terms) on the two dependent variables (relevance and usefulness). As expected, the correlation between relevance and usefulness is high (0.92) and significant. Both relevance and usefulness are measured as single item Likert scales due to large number ratings provided by each participant (240) in the study, thus making reliability computations impossible. However, the high correlation between these two items acts as an alternative and proves the robustness of the results discussed below as both relate to “quality” of the search results. The box plots for both relevance and usefulness clearly show that while there is no obvious difference among search engines when the search terms are well specified (S1T1, S2T1 and S3T1), the search engine Clusty with support for clustering (S3T2) clearly performs better than other search engines (S1T2 and S2T2) when the search terms are under-specified.

We also derived the quasi-precision scores<sup>6</sup> from the user evaluations of relevance (7-point Likert scale). Table 6 shows the descriptive statistics for precision score (P@10) and Table 7 reports the ANOVA results. Precision is typically computed as a binary variable — 0 for imprecise and 1 for precise. It is commonly used as a dependent variable to measure the relevance of search results returned by a search engine. As this research used a 7-point scale for relevance, the binary values for precision were computed by coding “1”, “2” and “3” on relevance as “0” (irrelevant) and “5”, “6” and “7” on relevance as “1” (relevant). The middle value “4” of the Likert scale was handled in three different ways — drop the value, randomly assign “0” or “1” and use the value “0.5”.<sup>7</sup> All three ways of dealing with the value “4” of relevance yielded a pattern of results that are not only similar to each other but also to the results reported for the 7-point Likert scale. This paper utilized random assignment in reporting the results for precision in Tables 6 and 7, again demonstrating the efficacy of clustering support.

The ANOVA results from Tables 4 and 5 show that both clustering support as well as specification of search terms had a statistically significant impact on relevance and usefulness, thus supporting hypotheses H1a, H1b, H2a and H2b. Even while the main effects are significant and important, the interaction effects (as shown in Tables 4 and 5; Figs. 5, 6, 7 and 8) give a more detailed account of the beneficial impact clustering support on underspecified search terms. Hence, hypotheses H3a and H3b are also supported. While all the hypotheses are statistically significant, we also report the partial Eta squared values in the ANOVA tables to indicate the practical significance. Partial Eta squared is a type of measure of association that can be interpreted “as the proportion of variance in the dependent variable that is attributable to each effect”.<sup>8</sup> Based on the tentative guidelines provided by Cohen [17] who provided rough estimates for different estimations of effect sizes (d, r, and Eta-squared), the results of the study in Tables 4 and 5 show that the effect of clustering support is medium while that of specification of search terms is very large. The effect of the interaction is also large, though smaller than just the main effect of specification of search terms, again underscoring the differential impact of the clustering technology support in improving the performance of search tasks. In other words, poorly specified search terms benefit greatly from clustering support.

The interaction graphs clearly show that clustering support provided by Clusty helps improve the relevance and usefulness scores of under-specified search terms in comparison with the non-clustered results offered by both Clusty and Google (control group). Thus, clustering significantly increases the robustness of search engines against poor query formulations by users. As predicted, the clustering support did not have as big an impact on well-specified search terms where all search engine results performed about the same.

![](/api/attachments/DDYAQPCP/fulltext/images/11cd78d5951b6efc7c48d88f461442e9652ccabd52304f26ef56c24efec88b47.jpg)  
Fig. 7.

## 6. Conclusion

The contributions of this paper are several. While previous studies in information retrieval have examined the impact of clustering and under-specification as separate issues [35,13,55,36], this study investigates the interdependence of the two issues. Our paper empirically shows that the value of clustering support increases especially for under-specified search terms (interaction effect). This means that while search terms still matter for achieving good search performance, they matter not as much when search engines with clustering support are used because technology can compensate to some extent for poor search term specifications. This finding has an impact on research on search cost in the areas of information economics and e-commerce. Our study shows that the design of search support features impacts the effectiveness with which consumers perform shopping related online searches. Relaxing the traditional assumption that users employ search tools in a uniform manner, we find that inexperienced or unsavvy users, who are less effective in terms of both formulating search queries and processing search results, incur higher search cost when shopping online. However, technology, if properly designed, can help compensate these user-generated inefficiencies to some degree. Specifically, we show that clustering support is an effective search feature that can help reduce search cost and increase efficiency in electronic markets.

![](/api/attachments/DDYAQPCP/fulltext/images/47d9403575ab47218fb40d8fc2ee0b229f6ce5ce140920bbe2e3af9e004a1647.jpg)  
Fig. 8. 4 × 3 interactions (usefulness).

The proposed research model (presented in Fig. 1) helps us better understand consumer search behavior and decision-making by studying how a search engine's support for clustering can help improve search performance of even poorly formulated search queries (thus reducing search costs). Search term formulation is an important and integral part of the online search process undertaken by consumers. Past research shows that the actual search terms used do matter in improving search performance and that users often mis-specify search terms, thereby reducing the efficacy of their online search and decision-making process. The results of this study offer evidence that clustering support provided by search engines helps increase relevance and usefulness of search results especially for those search terms that are underspecified. We expect that the results apply also beyond under-specified search terms to most mis-specified search terms. In addition, this research also used a rigorous rating scheme where each participant rated the top 10 search results individually for relevance and usefulness, thus generating 80 ratings for each search engine and a total of 240 ratings per participant. The rigor of the rating scheme and the 7-item Likert scale used to measure relevance and usefulness (instead of the usual binary precision measure) should further increase the confidence in the results of the study.

For practitioners and search engine companies, the findings may also be useful in improving search engine interface design. The results of this study show that all search engines, regardless of the underlying algorithms, could improve the relevance and the usefulness of the search results for mis-specified queries by offering some form of support for topical organization. Hence, we argue that the commercial search engines can increase the performance of their products by offering specific innovative search features such as support for clustering. Since some of the most popular search engines still do not offer such support, new entrants to the search markets view this aspect of IT-enabled support as one of the differentiators that would give them the much needed foothold into the search engine industry [20]. Clustering support could also be beneficial for other applications that use search features such as web sites or knowledge management systems.

This research was conducted with university students and hence the results as such generalize only to this particular population. The participants rated the search results for four search terms in a specific context — shopping for MP3 players. While the order of presentation of search engines was randomized, the order of presentation of search terms was not randomized. This is a limitation of the study due to possible learning effects of participants as they were exposed to all six levels of treatments. If there were a learning effect, the average ratings for search terms should show a monotonic increase or decrease across all treatments. However, the results of the study actually show that the search performance actually dropped for poorly specified search terms for each of the search engines (hence, there is no monotonic increase or decrease associated with learning effect). As predicted, the slope of the drop was less for the treatment with clustering support than the other two treatments. The results of the study were in conformance with the proposed hypotheses and show that learning effect was not a factor, thus reducing the potency of this particular limitation. In addition, since this research employed a rigorous rating scheme, the sheer number of ratings involved precluded us from including another context in order not to fatigue the participants.

This research evaluated clustering algorithm used by one search engine (Clusty) and the quality of the clustered search results may vary across different search engines that offer clustering support (for e.g. Teoma) thus restricting the generalizability of the study. Once again, the time taken by participants to complete the study precluded us from testing other search engines that offer clustering support. However, the results of this study showed that clustered search results used in the study performed about as well as Google (one of the popular search engines) for well-specified search terms and clearly outperformed Google for under-specified search terms (Figs. 3 and 4) thus strengthening the conclusions of the study. Future research should not only investigate the efficacy of clustering support in different contexts, but also compare the different algorithms used by various search engines to provide this clustering support.

## Acknowledgements

We thank the PSC-CUNY for its support to this project. We also appreciate the valuable feedback provided by Dr. Isak Taksa, the editors and reviewers, and the audience at HICSS where earlier version of this paper was presented.

Appendix A. Screenshot of non-clustered search results from Clusty.com  
![](/api/attachments/DDYAQPCP/fulltext/images/ffc95bd7808261e413937a8ba5991314933513552ac2cd97031e89c5b9a3dc11.jpg)

Appendix B. Screenshot of clustered search results from Clusty.com for the category “Review”  
![](/api/attachments/DDYAQPCP/fulltext/images/767b43bbd849c66d1bd8fb5f48ad22871b35cf42c620fc2b1fc732f72879d92a.jpg)

## References

[1] S.M.Z. Ahmed, C. McKnight, C. Oppenheim, A study of users' performance and satisfaction with the Web of science IR interface, Journal of Information Science 30 (2004) 459–468.

[2] J. Alba, J. Lynch, B. Weitz, C. Janiszeweski, R. Lutz, A. Sawyer, S. Wood, Interactive home shopping: consumer, retailer and manufacturer incentives to participate in electronic marketplaces, Journal of Marketing 61 (1997) 38–53.

[3] N.F. Awad, M.S. Krishnan, The personalization privacy paradox: an empirical evaluation of information transparency and the willingness to be profiled online for personalization, MIS Quarterly 30 (2006) 13–28.

[4] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval. New York: Addison Wesley / ACM Press, 1999.

[5] Y. Bakos, Reducing buyer search costs: implications for electronic marketplaces, Management Science 43 (1997).

[6] Y. Bakos, Towards friction-free markets: the emerging role of electronic marketplaces on the internet, Communications of the ACM 41 (1998) 35–42.

[7] M. Barbaro, Internet sales show big gains over holidays, The New York Times, New York 2005, p. A1.

[8] D. Bilal, Perspectives on children's navigation of the World Wide Web: does the type of search task make a difference? Online Information Review 26 (2002) 108–117.

[9] C.L. Borgman, S.G. Hirsh, J. Hiller, Rethinking online monitoring methods for information retrieval systems: from search products to search process, Journal of the American Society for Information Science and Technology 47 (1996) 568–583.

[10] E. Bradlow, D.C. Schmittlein, The little engines that could: modeling the performance of World Wide Web search engines, Marketing Science 19 (2000) 43–62.

[11] E. Brynjolfsson, M.D. Smith, Frictionless commerce? A comparison of internet and conventional retails, Management Science 46 (2000) 563–585.

[12] M. Carey, D.C. Heesch, S.M. Rueger, Info navigator: a visualization tool for document searching and browsing, Presented at Proceedings of the Ninth International Conference on Distributed Multimedia Systems, Miami, Florida, 2003.

[13] H. Chen, H. Fan, M. Chau, D. Zeng, MetaSpider: meta-searching and categorization on the Web, Journal of American Society for Information Science and Technology 52 (2001) 1134–1147.

[14] A.M. Chircu, V. Mahajan, Managing electronic commerce retail transaction costs for customer value, Decision Support Systems 42 (2006) 898–914.

[15] H. Chu, M. Rosenthal, Search engines for the World Wide Web: a comparative study and evaluation methodology, Presented at Proceedings of the 59th Annual Meeting of the American Society for Information Science, Baltimore, MD, 1996.

[16] E.K. Clemons, I.H. Hann, L. Hitt, Price dispersion and differentiation in online travel: an empirical investigation, Management Science 48 (2002) 534–549.

[17] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, Lawrence Earlbaum Associates, Hillsdale, NJ, 1988.

[18] A.B. Crenshaw, Consumer sovereignty? Power isn't knowledge, The Washington PostSunday Edition ed. Washington D.C., 2004, p. F04.

[19] P.A. Diamond, A model of price adjustment, Journal of Economic Theory 3 (1971) 156–168.

[20] S. Fagliano, Alumni plan new Google alternative, Stanford Daily, San Francisco, 2006.

[21] R. Garfinkel, R. Gopal, A. Tripathi, F. Yin, Design of a shopbot and recommender system for bundle purchases, Decision Support Systems 42 (2006) 1974–1986.

[22] E.J. Garrity, B. Glasberg, Y.J. Kim, L. Sanders, S.K. Shin, An experimental investigation of web-based information systems success in the context of electronic commerce, Decision Support Systems 39 (2005) 485–503.

[23] Y. Gao, M. Koufaris, R.H. Ducoffe, An experimental study of the effects of promotional techniques in web-based commerce, Journal of Electronic Commerce in Organizations 2 (2004) 1–21.

[24] F.A. Grootjen, T.P.V.D. Weide, Conceptual relevance feedback, IEEE International Conference on Systems, Man and Cybernetics, 2, (2002) pp. 471–476.

[25] A. Gupta, B.C. Su, Z. Walter, Risk profile and consumer shopping behavior in electronic and traditional channels, Decision Support Systems 38 (2004) 347–367.

[26] G. Häubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (2000) 4–21.

[27] H.v.d. Heijden, User acceptance of hedonic information systems, MIS Quarterly 28 (2004) 695–704.

[28] C. Hoischer, G. Strube, Web search behavior of internet experts and newbies, Computer Networks 33 (2000) 337–349.

[29] I. Hsieh-Yee, Effects of search experience and subject knowledge on the search tactics of novice and experienced searchers, Journal of the American Society for Information Science and Technology 44 (1993) 161–174.

[30] E.J. Johnson, W.W. Moe, P.S. Fader, S. Bellman, G.L. Lohse, On the depth and dynamics of online search behaviour, Management Science 50 (2004) 299–308.

[31] R. Kalakota, A.B. Whinston, Frontiers of Electronic Commerce, Addison Wesley Publishing, Reading, MA, 1996.

[32] R. Kauffman, E. Walden, Economics and electronic commerce: survey and directions for research, International Journal of Electronic Commerce 5 (2001) 5–116.

[33] N. Kumar, I. Benbasat, The effect of relationship encoding, task type and complexity on information representation: an empirical investigation of 2D and 3D graphs, MIS Quarterly 28 (2004) 255–281.

[34] F.Y. Kuo, T.H. Chu, M.H. Hsu, H.S. Hsieh, An investigation of effort accuracy trade-off and the impact of self efficacy on Web searching behaviors, Decision Support Systems 37 (2004) 331–342.

[35] R.M. Losee, L. Church Jr., Are two documents better than one? The cluster performance question for information retrieval, Journal of American Society for Information Science and Technology 56 (2005) 106–108.

[36] R.M. Losee, L.A.H. Paris, Measuring search engine quality and query difficulty: ranking with target and freestyle, Journal of American Society for Information Science and Technology 50 (1999) 882–889.

[37] K.S. Moorthy, B.T. Ratchford, D. Talukdar, Consumer information search revisited: theory and empirical analysis, Journal of Consumer Research 23 (1997) 263–277.

[38] R.A. Peterson, M.C. Merino, Consumer information search behavior and the internet, Psychology and Marketing 20 (2003) 99–121.

[39] L. Rainie, Online activities and pursuits, Pew Internet and American Life Project, 2005.

[40] G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, McGraw-Hill, New York, 1983.

[41] H.B. Schmidt, R.A. Spreng, A proposed model of external consumer information search, Journal of the Academy of Marketing Science 24 (1996) 240–256.

[42] M.M. Sebrechts, J.V. Cugini, S.J. Laskowski, J. Vasilakis, M.S. Miller, Visualization of search results: a comparative evaluation of text, 2D, and 3D interfaces, Presented at 22nd Annual International ACM SIGIR Conference on Research and Devel opment in Information Retrieval, Berkeley, California, United States 1999.

[43] M. Smith, J. Bailey, E. Brynjofsson, Understanding Digital Markets: Review and Assessment, MIT Press, Cambridge, MA, 1999.

[44] A. Spink, A user-centered approach to evaluating human interaction with Web search engines: an exploratory study, Information Processing and Management 38 (2002) 401–426.

[45] A. Spink, D. Wolfram, M.B.J. Jansen, T. Saracevic, Searching the Web: the public and their queries, Journal of the American Society for Information Science and Technology 52 (2001) 226–234.

[46] A. Spink, T.D. Wilson, N. Ford, A. Foster, D. Ellis, Informationseeking and mediated searching part 1—theoretical framework and research design, Journal of American Society for Information Science and Technology 53 (2002) 695–703.

[47] D.O. Stahl, Oligopolistic pricing with sequential consumer search, The American Economic Review 79 (1989) 700–712.

[48] D.O. Stahl, Oligopolistic pricing with heterogeneous consumer search, International Journal of Industrial Organization 14 (1996) 243–268.

[49] J. Stigler, The economics of information, Journal of Political Economy 69 (1961) 213–225.

[50] R. Telang, Consumer choice of internet search engines: empirical and analytical framework, GSIA, Carnegie Mellon University, Pittsburgh, PA 2002.

[51] A. Todirascu, F. Rousselot, Ontologies for information retrieval, Presented at 7th International Conference on Applications of Natural Language to Information Systems, Tours 2001.

[52] C.J. Van-Rijsbergen, Information Retrieval, Butterworths, Boston, 1979.

[53] N. Vulkan, E-commerce for consumers, The Economics of E-Commerce, Princeton University Press, NJ 2003, pp. 22–58.

[54] A.B. Whinston, D.O. Stahl, S.-Y. Choi, Consumers' search for information, The Economics of Electronic Commerce, Macmil lan Technical Publishing, Indianapolis, IN 1997, pp. 263–311.

[55] B.M. Wildemuth, The effects of domain knowledge on search tactic formulation, Journal of the American Society for Information Science and Technology 55 (2004) 246–258.

[56] D. Wolfram, A. Spink, B.J. Jansen, T. Saracevic, Vox populi: the public searching of the Web, Journal of the American Society for Information Science and Technology 52 (2001) 1073–1074.

[57] M.-M. Wu, Understanding patrons' Micro-level Information Seeking (MLIS) in information retrieval situations, Information Processing and Management 41 (2005) 929–948.

[58] W. Yuan, End-user searching behavior in information retrieval: a longitudinal study, Journal of the American Society for Information Science and Technology 48 (1997) 218–234.

Nanda Kumar is an assistant professor in the Computer Information Systems department at Baruch College, City University of New York. He received his Ph.D. in Management Information Systems from the University of British Columbia in 2003. His current research interests include human–computer interaction, behavioral aspects of B2C ecommerce, digital government, impact of IT on the organization of work and leisure. His work has appeared in journals such as Information Systems Research, MIS Quarterly, Communications of the ACM, and Electronic Markets.

Dr. Lang's research interests include decision technologies, management of digital businesses, knowledge-based products and services, and issues related to the newly arising informational society. Dr. Lang holds a PhD in Management Science from the University of Texas at Austin and is currently Associate Professor in Information Systems at Baruch College in New York City. His findings have been published in such diverse journals as Communications of the ACM, Journal of Management Information Systems, Decision Support Systems, Computational Economics, and Annals of Operations Research.
