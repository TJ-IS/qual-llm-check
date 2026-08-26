---
otero_id: 5462
otero_key: "FQUBHA7X"
title: "Scalable and noise tolerant web knowledge extraction for search task simplification"
authors: "Jun He; Yingqin Gu; Hongyan Liu; Jun Yan; Hong Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Scalable and noise tolerant web knowledge extraction for search task simpli<sup>fi</sup>cation<sup>☆</sup>

Jun He <sup>a,b</sup>, Yingqin Gu <sup>a,b</sup>, Hongyan Liu <sup>c,d,</sup>⁎, Jun Yan <sup>e</sup>, Hong Chen <sup>a,b</sup>

<sup>a</sup> Key Labs of Data Engineering and Knowledge Engineering, Ministry of Education, China

<sup>b</sup> School of Information, Renmin University of China, China

<sup>c</sup> Research Center for Contemporary Management, Tsinghua University, China

<sup>d</sup> Department of Management Science and Engineering, Tsinghua University, China

<sup>e</sup> Microsoft Research Asia, Beijing, China

## a r t i c l e i n f o

Article history: Received 23 December 2011 Received in revised form 13 February 2013 Accepted 26 May 2013 Available online 2 June 2013

Keywords: Search task simpli<sup>fi</sup>cation Structured knowledge extraction Information extraction

## a b s t r a c t

The simpli<sup>fi</sup>cation of key tasks of search engine users by directly returning structured knowledge according to their query intents has attracted much attention from both the industry and the academia. The challenge lies in automatically extracting structured knowledge from noisy and complex web scale websites. Although various automatic wrapper induction algorithms have been proposed, ineffectiveness or inef<sup>fi</sup>ciency issues beset many of their web scale applications. In this paper, we propose an unsupervised automatic wrapper induction algorithm, named SKES, to ef<sup>fi</sup>ciently extract knowledge from semi-structured websites. SKES induces the wrapper in a divide-and-conquer mode; dividing the general wrapper into sub-wrappers that can independently learn from data, making it ef<sup>fi</sup>cient and easy to implement in a parallel mode. Moreover, by employing techniques such as tag path representation of web pages, SKES can dramatically reduce the number of tags and naturally differentiate their roles. The proposed solution was applied and evaluated on a large number of real websites as well as compared with two existing methods that are most related to it. The proposed method is much more ef<sup>fi</sup>cient than the existing methods, and provided high extraction accuracy. We have extracted 2.5 million entities and 29 million data <sup>fi</sup>elds from over 10 thousand high traf<sup>fi</sup>c websites, which demonstrates the applicability of this method. Furthermore, based on the automatically extracted data, we built a prototype to serve structured knowledge that simpli<sup>fi</sup>es the key search tasks of end users. The feedback received for the prototype was highly positive.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The simpli<sup>fi</sup>cation of user search tasks is recognized as an emerging trend in information retrieval research [30]. However, users of state-of-the-art commercial search engines continue to endure iterative query-click-browsing procedures despite their having indicated very clear search tasks in their queries. Directly returning structured knowledge to end users instead of requiring them to click among a long list of URLs is regarded as an effective approach to user search task simpli<sup>fi</sup>cation. As shown in Fig. 1, the Bing<sup>1</sup> search engine directly triggers a side-by-side comparison table of athletes to users whose queries intend to compare two athletes. Similarly, Google Square<sup>2</sup> was released to provide structured knowledge in a tabular format to end users. Inspired by these efforts, in this paper, we de<sup>fi</sup>ne the tableformatted structured information as knowledge in user search task simpli<sup>fi</sup>cation.

Directly returning structured knowledge to simplify user search tasks brings two major challenges. The <sup>fi</sup>rst involves the construction of a large-scale structured knowledge base, by which the search tasks of end users are possibly satis<sup>fi</sup>ed. The second challenge comes in understanding the intent of user search queries for triggering structured knowledge. In this paper, we adopt a simple solution for understanding user query intent, focusing on how to automatically construct the large-scale knowledge base from the web for user search task simpli<sup>fi</sup>cation.

Encoded and displayed as semi-structured or unstructured HTML pages, structured data on the web, in general, cannot be directly accessed. The automatic extraction of structured knowledge from the semi-structured and unstructured web is a challenging task; speci<sup>fi</sup>cally, how to develop an effective and ef<sup>fi</sup>cient automatic wrapper induction algorithm for automatic knowledge extraction. Various research efforts aimed to address this problem. Most of the previous methods adopted the supervised learning model [1,10], thereby relying on manual efforts for extracting structured knowledge. Such projects are labor-intensive, as they require manually labeling each input site or website with the structure change. Thus, these methods are not feasible for parsing millions of websites for search task simpli-<sup>fi</sup>cation in generic search. In recent years, fully automatic solutions were proposed [1,12,22–24,26,31,32,34] to overcome this limitation. Among these methods, the structured data extraction from a set of detail pages that displays detailed information on an entity is considered highly effective [1,12] (Fig. 3 in Section 3 depicts an example of detail pages). However, existing algorithms continue to encounter limitations in dealing with web-scale data and noise. For example, extracting information from several hundred web pages requires several hours. With noisy web pages, certain algorithms fail to <sup>fi</sup>nd the template of most web pages, whereas others operate with low accuracy. Section 2 offers a detailed discussion. In this paper, we propose a scalable and noise-tolerant knowledge extraction algorithm, named SKES, for large-scale knowledge extraction from detail pages of entities.

![](/api/attachments/FQUBHA7X/fulltext/images/7905e48668bc3a265337b143e39582907f623a333ffd47f13454e23ccadb4715.jpg)  
Fig. 1. An example of search task simpli<sup>fi</sup>cation in Bing.

SKES exploits a top-down, divide-and-conquer strategy for information extraction. This algorithm divides the general template induction problem into several sub-template induction problems, which are then managed independently. Our method further employs the tag path [33] representation of the input pages, and thus achieves higher ef<sup>fi</sup>ciency compared with many state-of-the-art methods. We con<sup>fi</sup>rmed the applicability of this algorithm by extracting millions of entities and data <sup>fi</sup>elds from three domains, namely, movies, mobile apps, and restaurants. Data noise is managed by introducing a support threshold that prevents the generation of underlying templates in noise pages due to insuf<sup>fi</sup>cient support. Experimental results show that knowledge extraction with high accuracy can be ef<sup>fi</sup>ciently performed and a certain portion of noise pages can be tolerated. We likewise implemented a prototype system for search task simpli<sup>fi</sup>cation that garnered highly positive feedback from the user studies.

The major contributions of this paper could be summarized as follows. First, we proposed a fully automatic unsupervised wrapper induction algorithm, which exploits tag path representation of web pages and induces the wrapper in a top-down, divide-and-conquer manner. To verify the ef<sup>fi</sup>ciency, we applied the proposed algorithm on over 10 thousand high traf<sup>fi</sup>c websites indexed by a commonly used commercial search engine, and then manually labeled the results of random sampling to verify its effectiveness. The results indicate that our method is ef<sup>fi</sup>cient and noise-tolerant for large-scale extraction of structured knowledge from the web. Finally, taking advantage of the extracted knowledge base, we implemented a prototype system for search task simpli<sup>fi</sup>cation. A user study veri<sup>fi</sup>ed the user satisfaction and yielded highly positive feedback.

The rest of this paper is organized as follows. Section 2 introduces the related methods of Web Information Extraction (WIE). Section 3 presents the problem and several de<sup>fi</sup>nitions. Section 4 describes the proposed algorithm, SKES, in detail. Section 5 discusses the experimental results to verify the effectiveness and ef<sup>fi</sup>ciency of our proposed solution in terms of structured knowledge extraction. In addition, we employed an actual user study to verify the user task simpli<sup>fi</sup>cation feature based on the extracted structured knowledge. Finally, Section 6 offers the conclusions and discusses our future work.

## 2. Related work

The web knowledge extraction problem is generally known as WIE. WIE aims to extract information with a speci<sup>fi</sup>c structure, for example, ontology, from the World Wide Web. Different research efforts aimed to extract information from the web using different solutions. Considering types, data could be classi<sup>fi</sup>ed into two categories: unstructured and semi-structured data. For instance, the Natural Language Processing (NLP) and pattern learning algorithms are used for extracting unstructured data [3,5,8,16]; the wrapper induction, deep web querying, and table extraction algorithms are used for extracting semi-structured data [6,9,11,13,19,20,32]. Our work belongs to the latter category, that is, structured data extraction from semi-structured HTML pages.

This category has been widely studied in the past decade. A number of existing methods [10,18,21] are based on manually constructed wrappers or supervised machine-learning techniques. These methods are highly labor-intensive, as they rely on continuous manual effort for each new or format-changed site. Fully automatic methods were proposed in recent years, which extract structured data from pages in three main dimensions: (1) extracting the speci<sup>fi</sup>c structure of information such as relational tables, attribute–value pairs, and so on, from all indexed pages [14,26,32]; (2) extracting data records from a single page [9,22–24,31,34]; and (3) extracting structured data from a set of detail pages generated by the same template [1,12]. Among them, the third type of method is the most effective, as detail pages contain much more information than record-level pages and do not necessarily contain speci<sup>fi</sup>c structures.

In a website, detail pages are usually machine-generated from backend databases by using an underlying template. Therefore, structured data extraction from detail pages must automatically induce the underlying template (wrapper) and use this template to extract structured data. RoadRunner [12] and EXALG [1] are two commonly used methods that are fully automatic and strongly related to our work. RoadRunner is the <sup>fi</sup>rst fully automatic method that could extract structured data from similar, multiple-detail pages. A matching technique is developed to compare HTML pages of the same format and generate a template based on their similarities and differences. The technique relies on a greedy approach that starts from one page as an initial template and compares every other page to induce a more general template. EXALG is an improved data extraction method that manages the tokens of all pages at the same time. Underlying templates are detected by two techniques, that is, differentiating roles of tokens and equivalence classes. A template is generated from equivalence classes by further <sup>fi</sup>ltering those with insuf<sup>fi</sup>cient size. As templates are detected in the unit of tokens and <sup>fi</sup>ltered with insuf<sup>fi</sup>cient size, those with a few tokens are excluded and thus cannot be detected by EXALG.

From our observations, RoadRunner and EXALG work well in pure detail pages. A solution for avoiding the labor-intensive, manual identi<sup>fi</sup>cation of such detail pages in each site is to cluster pages to automatically detect different templates [4,13,18], which may lead to noise in each cluster in terms of sharing the same template. However, neither RoadRunner nor EXALG can manage such noisy data. Road-Runner generates the template by comparing each page, and fails to generate the correct template from noisy detail pages. In addition, with the information explosion in the World Wide Web, more sites now contain hundreds of thousands of detail pages (e.g., www. imdb.com). The two methods would have dif<sup>fi</sup>culties inducing good templates from pages on such a large scale. The matching algorithm used in RoadRunner features exponential time complexity with respect to the length of input page. EXALG likewise has a polynomial time complexity, which is still not ef<sup>fi</sup>cient enough for our applications. Although for a given website, the templates may not frequently change, the number of new websites rapidly increases, and the average number of web pages and bytes per page continue increasing each year. The Royal Pingdom Company<sup>3</sup> reports 634 million websites globally as of December 2012, representing a growth rate of 8.7% compared with <sup>fi</sup>gures of last year. The China Internet Network Development Statistics Report<sup>4</sup> indicates the growth rates in 2012 of Chinese websites, web pages, and average number of webpages per website as 16.8%, 41.7%, and 21.4%, respectively, compared with the year 2011. If the extraction method is not ef<sup>fi</sup>cient, even though the process is of<sup>fl</sup>ine, we could not obtain results for websites with a huge number of webpages.

Compared with RoadRunner and EXALG, our algorithm SKES employs a divide-and-conquer strategy. The general template induction problem is divided into several sub-template induction problems and then managed separately, increasing the ef<sup>fi</sup>ciency of our algorithm. In addition, we used tag path representation of HTML pages, which could dramatically reduce the number of tags and naturally differentiate their roles. A support threshold is likewise introduced to manage noisy data, thereby preventing the generation of underlying templates in noise pages due to insuf<sup>fi</sup>cient support.

Other methods that extract structured data from detail pages exist [27,29]. However, these methods focus on speci<sup>fi</sup>c sites such as forums or news sites, and are thus not applicable for general purposes.

## 3. Problem overview

In Section 1, we discussed our aim of extracting structured knowledge from websites for search task simpli<sup>fi</sup>cation. Fig. 2 provides the <sup>fl</sup>owchart for our work.

When a user submits a query, the search engine analyzes this query and directly returns structured knowledge from the knowledge base if the query contains clear knowledge search tasks. SKES processes a large number of websites to extract structured knowledge and obtain a large-scale knowledge base. For each website, a pageclustering algorithm [13] is used to group structurally similar pages so that SKES can be directly applied to each cluster. Therefore, SKES selects detail pages with similar structures as input, and induces the underlying template to extract structured knowledge as output. In this section, we introduce the page representation of our method and de<sup>fi</sup>ne several notations. The knowledge extraction algorithm SKES is described in detail in Section 4.

In this paper, we used tag paths that are powerful representations of original HTML pages and dramatically reduce the number of tags in pages. As a result, the wrapper induction increases in ef<sup>fi</sup>ciency compared with the ones without it. In terms of page representation, each node in an HTML DOM tree (tag tree) of a page can be identi<sup>fi</sup>ed by following a path from the root node to this target node. Such a path is known as a tag path [33]. For each HTML page, we identify the text nodes, that is, nodes containing text information, and store their tag paths with corresponding texts together. These tag paths and corresponding texts are used to represent the original page. Fig. 4 presents a sample HTML code of the <sup>fi</sup>rst page in Fig. 3, and Fig. 5(a) is an example of the page using our representation solution.

We represented the HTML pages in this way for two reasons. First, the roles of tags in different tag paths are naturally differentiated, that is, tags of the same name in different tag paths can be differentiated in the tag path representation. Moreover, our method can detect templates that consist of a few tags, unlike EXALG (mentioned in Section 2). For example, in Fig. 4, the template of the recommended software consists of only one tag “bli>” with insuf<sup>fi</sup>cient size and thus excluded by EXALG. By contrast, our method checks the tag path “bhtml>bul>bli>” and could identify this as a template. Second, our representation only considers the tag paths in text nodes, thereby dramatically reducing the number of tags. Fig. 5(a) shows that the number of tags decreased from the original 35 tags in Fig. 4 to 9 tags.

We introduced several notations and de<sup>fi</sup>nitions for better understanding. As mentioned above, a tag path is a path from the root node to a text node in the DOM tree. A tag path text is the tag path of a text node and the text carried by this node. An occurrence vector of a tag path q (or a tag path text t) is an integer vector $V _ { q } = [ f _ { 1 } , f _ { 2 } , . . . , f _ { n } ] ,$ or $V _ { t } = [ f _ { 1 } , f _ { 2 } , . . . , f _ { n } ] ,$ , where n is the number of input detail pages, and f is the number of occurrences of q (or t) in page i. A position vector of a tag path q (or a tag path text t) is a vector $P S _ { q } \left( \mathrm { o r } P S _ { t } \right) =$ $[ p _ { 1 } , p _ { 2 } , . . . , p _ { n } ] ,$ , where n is the number of input pages, and p is a set of positions where q (or t) occurs in page i.

## De<sup>fi</sup>nition 1. (Support count of tag path)

The support count of a tag path q, count (q), is the number of pages in which q occurs.

## De<sup>fi</sup>nition 2. (Support of tag path text)

Given n input detail pages and a tag path text t with $V _ { t } = [ f _ { 1 } , f _ { 2 } , . . . , f _ { n } ] ,$ the support of t, denoted as support(t), is de<sup>fi</sup>ned as the ratio of the number of elements equal to 1 to the number of elements in V .

![](/api/attachments/FQUBHA7X/fulltext/images/335bbb7a13ab10f9c02428da46791d61c0d0d9f7cad87036deff7ae336078a22.jpg)  
Fig. 2. Flowchart of knowledge extraction for search task simpli<sup>fi</sup>cation.

## De<sup>fi</sup>nition 3. (Support of a set of tag paths)

Let Q be a set of k tag paths, $Q = \{ q _ { 1 } , q _ { 2 } , . . . , q _ { k } \}$ , if the occurrence vectors of the k tag paths have m same non-zero elements, then the support of Q is de<sup>fi</sup>ned as the ratio of m to n, that is, suppor $( Q ) = m / n ,$ where n is the total number of input detail pages.

## De<sup>fi</sup>nition 4. (Equivalence class)

Given n input detail pages and a set Q of k tag paths, Q is called an equivalence class if support(Q) is larger than a user-de<sup>fi</sup>ned support threshold α. Even a single tag path could be an equivalence class.

For example, the tag path of the text node “Price:” at Line 6 in Fig. 4 is “bhtml>bbody>bdl>bdt>”. Therefore, its tag path text is “bhtml>bbody>bdl>bdt> Price:”. With the two example pages in Fig. 5 as input detail pages, then the occurrence vector of the tag path q = bhtml>bbody>bdl>bdt> is (2, 3), which means it occurs twice in the <sup>fi</sup>rst page and three times in the second page. support(q ) = 0, as none of its occurrence vector element is 1. The position vector of q is {(2, 4), (2, 4, 6)}, where (2, 4) means it occurs at the second and fourth positions in the <sup>fi</sup>rst page, and (2, 4, 6) means it occurs at these three corresponding positions in the second page. As the occurrence vector of tag path q = bhtml>bbody> bdl>bdt>bdiv> is also (2, 3), support({q<sub>1</sub>, q<sub>2</sub>}) = 2 / 2 = 1. If the user-de<sup>fi</sup>ned support threshold is 1, then these two tag paths consist of an equivalence class.

## 4. Algorithm

Inducing a good template (schema) of detail pages is key to structured data extraction, as the induced template can be used to automatically extract corresponding data <sup>fi</sup>elds encoded in HTML pages. However, the problem of inducing a good (unambiguous) template is complicated, owing to the existence of missing data <sup>fi</sup>elds. This has been proved as an NP-complete problem [28]. With this limitation, we make some reasonable assumptions in order to perform the extraction more ef<sup>fi</sup>ciently.

SKES consists of three key steps: (1) template induction; (2) structured data extraction; and (3) post-processing of the extracted data. The <sup>fi</sup>rst step addresses the problem of scalable template induction from detail pages, which is vital to our method. The second step uses the induced template to extract corresponding data <sup>fi</sup>elds encoded in pages. The third step processes the extracted data to

Archipelago 1.14  
![](/api/attachments/FQUBHA7X/fulltext/images/950e6f7e944a412d1e96cb46c92fd230b6cd849d5d9fd5166a72076272a20d45.jpg)  
Addictive fast-paced real-time strategy game. Easy to learn, hard to master. Grow and deploy your forces to capture slands of a tropical archipelago.

## Blockx 3D Pro 1.3

![](/api/attachments/FQUBHA7X/fulltext/images/58e259847462b66f1379cfb0bc88bbd1ba06c0f9018e4219225c0c28b3cd3f2c.jpg)  
Forget 2D faling block games, 3D is here to stay! Falling blocks game in 3D, cassic with a completely new twist. Enjoy customizable pit, 3 block sets, autosave & load, global leaderboard. Now supports landscape mode!  
Fig. 3. An example of two detail pages.

properly present the results. All these steps are fully automatic and labor-free. Each step is discussed further.

## 4.1. Template induction

Inspired by the divide-and-conquer strategy, we induced templates in a top-down manner for scalability. This technique is based on the observation that templates and data <sup>fi</sup>elds can be more easily differentiated if a speci<sup>fi</sup>c section can be identi<sup>fi</sup>ed. (With Fig. 5 as example, identifying that tag path “bhtml>bbody>ba>” before “Price:” encodes a data <sup>fi</sup>eld is easy, yet the same is dif<sup>fi</sup>cult to do in overall pages.) Therefore, a key idea of our divide-and-conquer strategy is to induce a template with several con<sup>fi</sup>dent wrappers <sup>fi</sup>rst, which splits the general template into sub-sections, and separately induces more speci<sup>fi</sup>c templates for each sub-section.

For top-down template induction, inducing a good template is an NP-complete problem [28]. To facilitate a scalable inducing method, we make two assumptions for template inductions based on observations of real website pages. First, across pages of the same format, the invariant parts are deemed as templates, and the variant parts are deemed as encoded data fields. Second, different data fields are displayed in the same order in the same cluster of pages within one site. That is, if data <sup>fi</sup>eld A displays in precedence of data <sup>fi</sup>eld B in one page, then B should never display in precedence of A in other similar pages. The <sup>fi</sup>rst assumption is a little strong, as it may fail in a few real world application cases. When this assumption fails, our method either fails to extract the invariant data <sup>fi</sup>elds or extracts the variant template parts as data <sup>fi</sup>elds. However, we observed that most data <sup>fi</sup>elds vary in different pages with the same template, which means that the <sup>fi</sup>rst assumption is rarely broken. When the second assumption is broken, we can solve the problem by a post-processing step.

<table><tr><td colspan="3">Page 1</td></tr><tr><td>01:</td><td></td><td>Archipelago 1.14</td></tr><tr><td>02:</td><td></td><td>Price:</td></tr><tr><td>03:</td><td></td><td>$2.99</td></tr><tr><td>04:</td><td></td><td>Last updated:</td></tr><tr><td>05:</td><td></td><td>09/26/2010</td></tr><tr><td>06:</td><td></td><td>Recommendations</td></tr><tr><td>07:</td><td></td><td>Par 72 Golf</td></tr><tr><td>08:</td><td></td><td>Mathpac 5.6</td></tr><tr><td>09:</td><td></td><td>FourNumGuess 1.0.6</td></tr></table>

![](/api/attachments/FQUBHA7X/fulltext/images/c55c96619bfceb75d6a1adbde59602132c14437c6e00171b7ec2cf3cbd672a1f.jpg)  
Fig. 4. Sampled HTML code of one detail page.

As introduced above, in this paper, we de<sup>fi</sup>ne the table-formatted structured information, which could be used to complete the search tasks of end users, as structured knowledge for user search task simpli-<sup>fi</sup>cation. Thus, we aim to put the extracted data into tables, where each row represents the entity described by a detail page, and each column stands for one attribute of this entity. We only extracted three kinds of data <sup>fi</sup>elds: (a) data <sup>fi</sup>elds in a single slot; (b) data <sup>fi</sup>elds displayed in a list pattern; and (c) data <sup>fi</sup>elds across multiple slots (called data section). Using Fig. 5(a) as an example, line 1 can be extracted as the <sup>fi</sup>rst type of data <sup>fi</sup>eld and lines 7–9 can be extracted as the second type of data <sup>fi</sup>eld. Then, each data <sup>fi</sup>eld is organized in a column of the extracted table.

![](/api/attachments/FQUBHA7X/fulltext/images/7e325ab4a1409d8f2720f60a4fa3e17285e5424a6af724c5c056c38214a3ee29.jpg)  
Fig. 5. (a) and (b) Our representation of two detail pages.

Our top-down template induction method consists of two major steps. The <sup>fi</sup>rst step involves identi<sup>fi</sup>cation of several data sections to construct a general template, called the root template. For each data section, we further identi<sup>fi</sup>ed more speci<sup>fi</sup>c data <sup>fi</sup>elds and data sections to generate a more speci<sup>fi</sup>c template. The second step would repeat the process on the newly generated template until no further details can be added. Speci<sup>fi</sup>cally, we identify several general data sections to construct the root template by detecting them from the tag path texts, their corresponding occurrence vectors, and position vector. The details of the root template induction algorithm are given in Algorithm 1. The support threshold α is a ratio that is set for managing noisy data. In our experiments, the ratio is empirically set to 0.9. Tag path texts with supports above this threshold would be added to the root template. Algorithm 1 takes this threshold and a set of input HTML pages as input to generate a root template RT.

In Algorithm 1, Line 1 converts HTML pages into our tag path representation. Lines 2–3 go through all the pages and initialize essential information, such as tag path texts and occurrence vectors. Lines 4–9 check each tag path text to decide whether it belongs to the root template. According to Assumption 1, tag path texts with support not less than the user-de<sup>fi</sup>ned support threshold α are deemed as a template. If a tag path text is identi<sup>fi</sup>ed as a template, Line 7 adds it to the root template by the order it occurs in one page using Assumption 2. Line 10 checks the position vector of the tag path texts in the root template to determine whether they contain other tag path texts between two adjacent ones. If yes, <sup>fl</sup>ag “Data Section” is inserted between these two tag path texts to show an existing data section for further induction. Fig. 6(a) presents an example of the root template induced from the two detail pages in Fig. 5.

## Algorithm 1. InduceRootTemplate

![](/api/attachments/FQUBHA7X/fulltext/images/c59e1863a5493e4b05ab098f120b76ed504598b9a51f4b1c346cebf4633e938d.jpg)

Given an induced template, the problem of template induction is divided into sub-template induction problems in each data section of the template. For each data section, we further detect patterns of tag paths to identify data <sup>fi</sup>elds and generate more speci<sup>fi</sup>c templates. Speci<sup>fi</sup>cally, two kinds of data <sup>fi</sup>elds exist, namely, data <sup>fi</sup>elds in a single slot and those displayed in a list pattern. A data <sup>fi</sup>eld of the <sup>fi</sup>rst kind can be identi<sup>fi</sup>ed after a tag path occurs exactly once in most pages or in certain portions of pages, and marked as “#value#” or “#optional value#,” respectively. A data <sup>fi</sup>eld of the second kind can be identi<sup>fi</sup>ed after an equivalence class occurs once or more times, and among which no other tag path exists (not nest structure) in most pages, and marked as “#list#”. More speci<sup>fi</sup>c data sections can then be detected because the two kinds of identi<sup>fi</sup>ed data <sup>fi</sup>elds split the original data section into several data sections, which are processed in the next iteration. Algorithm 2 provides further details for speci<sup>fi</sup>c template induction.

![](/api/attachments/FQUBHA7X/fulltext/images/27b319627ae4100bcdc41d434035160b704be80280009d2e6b0a34b7d85f9660.jpg)  
Fig. 6. (a), (b) and (c) Examples of induced templates.

In Algorithm 2, Lines 1–2 pass through all the pages and initialize essential information such as tag paths and occurrence vectors. Lines 3–17 indicate major steps to generate the template in one of the iterations. The iteration stops if no more speci<sup>fi</sup>c template can be induced. Within the iteration, each data section is processed (Lines 5 to 15). For each data section, Line 6 obtains information such as tag paths and occurrence vectors that belong to this data section. Based on the information, Lines 7–13 attempt to induce a sub-template for each data section by checking each tag path and generating a line of template if it is deemed as part of a template. In Line 10, the function check $( p , V _ { p } , P S _ { p } , \alpha )$ detects each tag path p with its equivalence class and identi<sup>fi</sup>es data <sup>fi</sup>elds. Only tag paths with no nest structure are considered part of a template. In this way, some nest structures are divided into several sections and are induced in the next iteration. Flags of “#value#”, “#optional value#”, and “#list#” are added to the tag path according to its type of data <sup>fi</sup>elds, which can be identi-<sup>fi</sup>ed by corresponding occurrence vectors to generate a line of templates. Line 13 sorts the tag paths in sub-template T by their occurrence order in one page (Assumption 2), and then T would be inserted to the current data section in ST. Line 16 further checks the position vectors to identify remaining data sections that need to be induced in the next iteration. The algorithm then starts a new iteration until no new template is induced, which usually stops after two or three iterations in real cases. Fig. 6 presents examples of induced templates based on two detail pages in Fig. 5.

## Algorithm 2. InduceSpeci<sup>fi</sup>cTemplate

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Root template RT, a set of input pages  $DP_{n}$ , a support threshold  $\alpha$ 
Output: A specific template ST.
Steps:
01: Go through  $DP_{n}$ , get all distinct tag paths to set TP,
occurrence vectors  $V_{TP}$  and position vectors  $PS_{TP}$  of these tag paths
02: Initialize ST = RT, template T to be empty.
03: while T != ST
04:    T = ST
05:    for each Data Section d in T do
06:    get  $TP_{d}$ ,  $V_{Pd}$ ,  $PS_{Pd}$  from TP,  $V_{TP}$ ,  $PS_{TP}$ 
07:    Initialize SubTemplate  $T_{s}$  to be empty
08:    for each tag path p in  $TP_{d}$  do
09:    get  $V_{p}$  from  $V_{Pd}$ ,  $PS_{p}$  from  $PS_{Pd}$ 
10:    tl = check( $p$ ,  $V_{p}$ ,  $PS_{p}$ ,  $\alpha$ ) //tl is a template line
11:    Add tl to  $T_{s}$ 
12:    end for
13:    sort  $T_{s}$ 
14:    insert  $T_{s}$  to ST
15:    end for
16:    Go through  $PS_{TP}$ , add flag “Data Section” into ST
17: end while
18: return ST
</div>

## 4.2. Structured data extraction

With an induced template, extracting structured data from pages represented by tag paths can be done in a straightforward manner. We apply the template on each page to obtain several data <sup>fi</sup>elds, and these data constitute a tuple of a table. All related information of one site can be summarized in a table, wherein each row corresponds to an entity in a detail page and each column is an attribute of the entity. Thus, each cell in the table would be the attribute value of the entity in the corresponding row. The number of table columns is determined by the number of data <sup>fi</sup>elds in the template.

As single values of various attributes, columns containing data <sup>fi</sup>elds of the <sup>fi</sup>rst type can be stored directly in a database. As for data <sup>fi</sup>elds of the second type, currently we treat them as multi-valued attributes and store a list of attribute values in one cell of the table where each value is separated by a particular delimiter. Normalizing the table for more convenient storage and retrieval can be achieved in a straightforward manner. For each data section in the <sup>fi</sup>nal template, these are stored in a column as an attribute. The action is reasonable as a website may encode a long data <sup>fi</sup>eld across multiple text nodes (e.g. data <sup>fi</sup>eld of attribute “storyline” in movie domain websites).

## 4.3. Post-processing extracted data

After extracting knowledge, two reasons inspire us to conduct post-processing to polish the extracted data. First, knowledge mixed within the same text node could be neglected. For example, if two data <sup>fi</sup>elds,“1.10” and “Game”, in an underlying data base are encoded into a text node, “bdiv>Price: \$1.10 Category: Gameb/div>”, in a HTML page, our method would identify such text as the same data <sup>fi</sup>eld, which is obviously incorrect. Second, a number of data <sup>fi</sup>elds without valuable knowledge were extracted by SKES. For instance, Line 6 of the template in Fig. 6(c) would extract optional attribute “Category:” as a data <sup>fi</sup>eld. Therefore, our post-processing step aims to further parse the knowledge mixed together and <sup>fi</sup>lter out the extracted noise.

Table 1 Information of some websites.

<table><tr><td>Website</td><td>Domain</td><td>Number of detail pages</td></tr><tr><td>www.imdb.com</td><td>Movie</td><td>351,000</td></tr><tr><td>www.zap2it.com</td><td>Movie</td><td>98,416</td></tr><tr><td>www.moviefone.com</td><td>Movie</td><td>153,931</td></tr><tr><td>www.allmovie.com</td><td>Movie</td><td>149,590</td></tr><tr><td>movies.msn.com</td><td>Movie</td><td>494,815</td></tr><tr><td>movies.yahoo.com</td><td>Movie</td><td>45,883</td></tr><tr><td>www.fandango.com</td><td>Movie</td><td>67,365</td></tr><tr><td>www.movies.com</td><td>Movie</td><td>147,652</td></tr><tr><td>www.amctheatres.com</td><td>Movie</td><td>84,367</td></tr><tr><td>www.mrqe.com</td><td>Movie</td><td>36,589</td></tr><tr><td>www.androidzoom.com</td><td>Mobile app</td><td>127,775</td></tr><tr><td>www.apple.com</td><td>Mobile app</td><td>297,698</td></tr><tr><td>www.brothersoft.com</td><td>Mobile app</td><td>47,415</td></tr><tr><td>iphoneapplicationlist.com</td><td>Mobile app</td><td>14,687</td></tr><tr><td>www.cyrket.com</td><td>Mobile app</td><td>23,521</td></tr><tr><td>www.pocketgear.com</td><td>Mobile app</td><td>94,510</td></tr><tr><td>www.mobiletopsoft.com</td><td>Mobile app</td><td>51,281</td></tr><tr><td>appworld.blackberry.com</td><td>Mobile app</td><td>14,256</td></tr><tr><td>www.freewarepocketpc.net</td><td>Mobile app</td><td>12,368</td></tr><tr><td>www.pocketpc-freeware.net</td><td>Mobile app</td><td>12,897</td></tr><tr><td>www.allmenus.com</td><td>Restaurant</td><td>584,563</td></tr><tr><td>www.menuism.com</td><td>Restaurant</td><td>53,200</td></tr><tr><td>www.restaurantrow.com</td><td>Restaurant</td><td>23,554</td></tr><tr><td>www.city-data.com</td><td>Restaurant</td><td>17,120</td></tr><tr><td>www.cityguide.com</td><td>Restaurant</td><td>51,676</td></tr><tr><td>www.opentable.com</td><td>Restaurant</td><td>12,225</td></tr><tr><td>www.agoda.com</td><td>Restaurant</td><td>8986</td></tr><tr><td>www.insiderpages.com</td><td>Restaurant</td><td>21,367</td></tr><tr><td>www.tripadvisor.com</td><td>Restaurant</td><td>251,119</td></tr><tr><td>www.yellowbot.com</td><td>Restaurant</td><td>78,442</td></tr></table>

We identify the common tokens in each column of the extracted data to further parse each text node. If common tokens exist in a column, they would help us split the column or <sup>fi</sup>lter these tokens if they are common pre<sup>fi</sup>xes or suf<sup>fi</sup>xes. We likewise determine whether common delimiters exist (e.g. ‘:’) in each column. If so, such delimiters would be used to separate the attribute name from the value. The column would be split and organized by their attribute names. In the former example, the text node would be split into two parts, “\$1.10” and “Game”, and “Price” and “Category” would become the attribute names of the two parts, respectively. Then, in the “Price” column, we may <sup>fi</sup>lter the token ‘\$’ if only a dollar mark exists in the site.

Our method may extract some varying templates as data <sup>fi</sup>elds, because Assumption 1, mentioned in Section 4, at times cannot be guaranteed to hold. We <sup>fi</sup>lter out these extracted noisy columns by using a heuristic rule that a column would be removed if there is only one distinct value in the column. For example, a column that only contains “Category” and a null data <sup>fi</sup>eld, which is extracted based on Line 6 of the template in Fig. 6, would be removed. For noise pages in the input collection, no data <sup>fi</sup>eld or very few data <sup>fi</sup>elds would exist in their corresponding rows. Similarly, we remove very sparse rows.

## 5. Experimental results

In this section, we present our experimental results using real web pages to demonstrate the effectiveness and ef<sup>fi</sup>ciency of the proposed SKES algorithm. We also conducted a user study based on the extracted knowledge to measure user satisfaction of our implemented prototype system for user task simpli<sup>fi</sup>ed search.

## 5.1. Experimental setup

For the empirical study, we extracted thousands of data-intensive websites in three domains, namely, Mobile application, Movie, and Restaurant from Bing-indexed pages. For evaluation purposes, because manual labeling of the tens of millions of web pages is dif<sup>fi</sup>cult, we chose 30 websites for manual labeling of results and conducted an evaluation. Table 1 presents the detailed information on the 30 selected websites. We compared the ef<sup>fi</sup>ciency of our approach with that of two existing algorithms, RoadRunner and EXALG. RoadRunner's code in Java is available on the web<sup>5</sup> and we implemented EXALG according to the paper.

Table 2  
Performance of SKES on 30 websites.

<table><tr><td>Website</td><td>Precision</td><td>Recall</td><td>F score</td></tr><tr><td>www.imdb.com</td><td>0.99</td><td>0.81</td><td>0.89</td></tr><tr><td>www.zap2it.com</td><td>0.99</td><td>0.88</td><td>0.93</td></tr><tr><td>www.moviefone.com</td><td>0.99</td><td>0.81</td><td>0.89</td></tr><tr><td>www.allmovie.com</td><td>1.00</td><td>0.53</td><td>0.70</td></tr><tr><td>movies.msn.com</td><td>0.96</td><td>0.45</td><td>0.62</td></tr><tr><td>movies.yahoo.com</td><td>1.00</td><td>0.85</td><td>0.92</td></tr><tr><td>www.fandango.com</td><td>0.97</td><td>0.82</td><td>0.89</td></tr><tr><td>www.movies.com</td><td>0.96</td><td>0.74</td><td>0.84</td></tr><tr><td>www.amctheatres.com</td><td>0.96</td><td>0.66</td><td>0.78</td></tr><tr><td>www.mrqe.com</td><td>0.98</td><td>0.74</td><td>0.84</td></tr><tr><td>www.androidzoom.com</td><td>0.97</td><td>0.79</td><td>0.87</td></tr><tr><td>www.apple.com</td><td>0.98</td><td>0.83</td><td>0.89</td></tr><tr><td>www.brothersoft.com</td><td>0.99</td><td>0.91</td><td>0.95</td></tr><tr><td>iphoneapplicationlist.com</td><td>0.97</td><td>0.86</td><td>0.91</td></tr><tr><td>www.cyrket.com</td><td>0.95</td><td>0.73</td><td>0.82</td></tr><tr><td>www.pocketgear.com</td><td>0.96</td><td>0.76</td><td>0.85</td></tr><tr><td>www.mobiletopsoft.com</td><td>0.95</td><td>0.64</td><td>0.77</td></tr><tr><td>appworld.blackberry.com</td><td>0.99</td><td>0.68</td><td>0.81</td></tr><tr><td>www.freewarepocketpc.net</td><td>0.97</td><td>0.75</td><td>0.84</td></tr><tr><td>www.pocketpc-freeware.net</td><td>0.99</td><td>0.80</td><td>0.89</td></tr><tr><td>www.allmenus.com</td><td>0.98</td><td>0.82</td><td>0.90</td></tr><tr><td>www.menuism.com</td><td>0.99</td><td>0.72</td><td>0.84</td></tr><tr><td>www.restaurantrow.com</td><td>0.97</td><td>0.82</td><td>0.89</td></tr><tr><td>www.city-data.com</td><td>0.96</td><td>0.71</td><td>0.82</td></tr><tr><td>www.cityguide.com</td><td>0.95</td><td>0.71</td><td>0.82</td></tr><tr><td>www.opentable.com</td><td>0.98</td><td>0.76</td><td>0.86</td></tr><tr><td>www.agoda.com</td><td>0.97</td><td>0.81</td><td>0.88</td></tr><tr><td>www.insiderpages.com</td><td>0.97</td><td>0.64</td><td>0.77</td></tr><tr><td>www.tripadvisor.com</td><td>0.98</td><td>0.64</td><td>0.77</td></tr><tr><td>www.yellowbot.com</td><td>0.97</td><td>0.78</td><td>0.86</td></tr><tr><td>Average</td><td>0.98</td><td>0.75</td><td>0.84</td></tr></table>

All the experiments were conducted on an AMD Opteron 254 computer with a 2.8 GHz CPU and 16 G of RAM. Our algorithm was implemented in C#, which utilizes HTML Agility Pack<sup>6</sup> to build HTML DOM tree for each page. We run our algorithm for all detail pages in each website to obtain the structured data in a table format. We then manually labeled the attributes of each column to build the knowledge base. We sampled hundreds of pages in each website to compare the algorithms of RoadRunner and EXALG, which are not scalable on such large data. Both algorithms were run using the same procedure and platform on the sampled pages.

## 5.2. Effectiveness evaluation

We used precision and recall as primary metrics to evaluate the effectiveness of SKES. As our datasets are signi<sup>fi</sup>cantly large, generating a complete ground truth is dif<sup>fi</sup>cult. Thus, we randomly selected 100 pages from each website. Six invited editors, who serve as ground truth, manually labeled all data <sup>fi</sup>elds in these pages. The editors labeled the extracted results of the sampled pages in each website to obtain true and false positives and evaluate the precision of our approach. True positives are the set of data <sup>fi</sup>elds (values) correctly extracted by our approach, whereas false positives are the set of data <sup>fi</sup>elds that were incorrectly extracted. The precision, recall, and

Table 4  
Table 3  
Performance of SKES on 10 websites.

<table><tr><td rowspan="2">Website</td><td colspan="3">100 pages</td><td colspan="3">300 pages</td></tr><tr><td>Precision</td><td>Recall</td><td>F score</td><td>Precision</td><td>Recall</td><td>F score</td></tr><tr><td>www.moviefone.com</td><td>0.99</td><td>0.81</td><td>0.89</td><td>0.92</td><td>0.74</td><td>0.82</td></tr><tr><td>movies.msn.com</td><td>0.96</td><td>0.45</td><td>0.62</td><td>0.84</td><td>0.52</td><td>0.64</td></tr><tr><td>movies.yahoo.com</td><td>1.00</td><td>0.85</td><td>0.92</td><td>0.94</td><td>0.81</td><td>0.87</td></tr><tr><td>www.movies.com</td><td>0.96</td><td>0.74</td><td>0.84</td><td>0.90</td><td>0.71</td><td>0.79</td></tr><tr><td>www.mrqe.com</td><td>0.98</td><td>0.74</td><td>0.84</td><td>0.99</td><td>0.76</td><td>0.86</td></tr><tr><td>www.androidzoom.com</td><td>0.97</td><td>0.79</td><td>0.87</td><td>0.91</td><td>0.75</td><td>0.82</td></tr><tr><td>iphoneapplicationlist.com</td><td>0.97</td><td>0.86</td><td>0.91</td><td>0.94</td><td>0.88</td><td>0.91</td></tr><tr><td>www.menuuism.com</td><td>0.99</td><td>0.72</td><td>0.84</td><td>0.91</td><td>0.80</td><td>0.85</td></tr><tr><td>www.restaurantrow.com</td><td>0.97</td><td>0.82</td><td>0.89</td><td>0.90</td><td>0.81</td><td>0.85</td></tr><tr><td>www.tripadvisor.com</td><td>0.98</td><td>0.64</td><td>0.77</td><td>0.96</td><td>0.67</td><td>0.79</td></tr><tr><td>Average</td><td>0.98</td><td>0.75</td><td>0.84</td><td>0.95</td><td>0.74</td><td>0.83</td></tr></table>

F score for each website can be calculated by the following three equations. Table 2 presents experimental results of our approach.

$$
P r e c i s i o n = \frac {\left| t r u e p o s i t i v e s \right|}{\left| t r u e p o s i t i v e s \right| + \left| f a l s e p o s i t i v e s \right|}
$$

$$
\text { Recall } = \frac {| \text { true   positives } |}{| \text { ground   truth } |}
$$

$$
F \text {   Score   } = \frac {2 \times \text { Precision } \times \text { Recall }}{\text { Precision } + \text { Recall }}.
$$

As shown in Table 2, our approach achieves excellent performance on most websites, as most of the F scores were above 80%. However, our approach failed to extract many data <sup>fi</sup>elds in a few websites, which could be attributed to the complex templates that violate our assumptions. For example, in the website “www.allmovie.com”, several data <sup>fi</sup>elds are displayed in a relational table format (<sup>fi</sup>rst row contains attribute names and second row contains data <sup>fi</sup>elds). Various data <sup>fi</sup>elds are encoded in HTML pages with the same tag path, which cannot be separated by our approach. Our approach identi<sup>fi</sup>es such data <sup>fi</sup>elds as list pattern data <sup>fi</sup>elds or merely data sections and organizes them in a column of the result table, which would be labeled as irrelevant data <sup>fi</sup>elds causing low recall in this website. Taking advantage of existing table processing methods [15] to associate with our approach may solve such problems, and our future work would involve integrating methods of extracting such speci<sup>fi</sup>c structures of information [6,26,32].

We randomly chose 10 from the 30 websites and labeled 200 more pages per site to indicate that the results would not considerably change despite the higher number of pages. Table 3 presents the performance of our method.

Table 3 demonstrates small changes in precision, recall, and F score. Thus, we can say that the performance is stable. As RoadRunner and EXALG are not scalable in large-scale websites, we sampled hundreds of pages in each website to build datasets for comparison. For further ef<sup>fi</sup>ciency evaluation, we generated six datasets from each website by using random sampling, with each data set containing 40, 80, 120, 160, 200, and 240 detail pages, respectively. The <sup>fi</sup>rst three columns of Table 4 show the F scores of SKES, EXALG, and Road-Runner to measure the effectiveness, which was averaged on the 30 websites. SKES has similar F scores with EXALG and RoadRunner.

Comparison with existing algorithms.

<table><tr><td>Number of pages</td><td>F score SKES</td><td>F score EXALG</td><td>F score RoadRunner</td><td>Runtime (s) SKES</td><td>Runtime (s) EXALG</td><td>Runtime (s) RoadRunner</td></tr><tr><td>40</td><td>0.92</td><td>0.851</td><td>0.81</td><td>3</td><td>81</td><td>10</td></tr><tr><td>80</td><td>0.91</td><td>0.87</td><td>0.83</td><td>6</td><td>295</td><td>117</td></tr><tr><td>120</td><td>0.88</td><td>0.85</td><td>0.79</td><td>8</td><td>387</td><td>660</td></tr><tr><td>160</td><td>0.88</td><td>0.862</td><td>0.81</td><td>13</td><td>653</td><td>1620</td></tr><tr><td>200</td><td>0.87</td><td>0.91</td><td>0.81</td><td>21</td><td>1090</td><td>5012</td></tr><tr><td>240</td><td>0.85</td><td>0.889</td><td>0.85</td><td>28</td><td>&gt;30 min</td><td>&gt;80 min</td></tr></table>

![](/api/attachments/FQUBHA7X/fulltext/images/a96a25209380836638d85279171da35ae15399962e1824ac820a9baea03ea6eb.jpg)  
Fig. 7. The number of tag path texts and HTML tags in various pages.

## 5.3. Efficiency evaluation

In this section, we evaluate the ef<sup>fi</sup>ciency of our approach in three steps. First, a comparison between our approach and two existing algorithms, RoadRunner and EXALG, is conducted to indicate the dramatic improvement in ef<sup>fi</sup>ciency. Taking several real web pages as cases, we demonstrate the reduction of the number of tags by tag path representation, which is one of the reasons for the high ef<sup>fi</sup>ciency of our method. Finally, we report the scalability of our algorithm on websites with respect to the number of pages.

Table 4 shows that the runtime of our approach linearly increased with respect to the number of pages, whereas the runtime of RoadRunner and EXALG sharply increased. The author of RoadRunner [12] reported that the AND–OR tree used in RoadRunner had the worst exponential size because of its requirement to explore different alternatives for each mismatch. Although several techniques have been proposed to lower the complexity, the algorithm still consumes time in managing real pages. EXALG likewise faces a polynomial time complexity. On the other hand, our algorithm uses a divide-and-conquer strategy and displays excellent ef<sup>fi</sup>ciency.

Fig. 7 shows the number of HTML tags and of tag path texts using our representation, which generally contains <sup>fi</sup>ve to ten times less tags than the original HTML tags. In our approach, these tag path texts would be further divided into several data sections for template induction. Therefore, only a few tag path texts usually exist in a data section, which allows template detection for each data section in SKES to be highly ef<sup>fi</sup>cient.

The runtime of SKES is mainly affected by two aspects, namely, the number of pages and the average number of tag path texts in a page.

![](/api/attachments/FQUBHA7X/fulltext/images/84034429ed36ea408a3c36b4d2031e1b06fcf27440f47a87d123461a0741523f.jpg)  
Fig. 8. Runtime of SKES in pages with various scales.

Table 5  
Performance of SKES in noisy situations.

<table><tr><td rowspan="2">Percent of noise</td><td colspan="2">Precision</td><td colspan="2">Recall</td><td colspan="2">F score</td></tr><tr><td>SKES</td><td>EXALG</td><td>SKES</td><td>EXALG</td><td>SKES</td><td>EXALG</td></tr><tr><td>0%</td><td>0.87</td><td>0.85</td><td>0.83</td><td>0.83</td><td>0.85</td><td>0.84</td></tr><tr><td>2%</td><td>0.86</td><td>0.86</td><td>0.83</td><td>0.83</td><td>0.85</td><td>0.84</td></tr><tr><td>4%</td><td>0.74</td><td>0.82</td><td>0.83</td><td>0.67</td><td>0.78</td><td>0.74</td></tr><tr><td>6%</td><td>0.88</td><td>0.85</td><td>0.83</td><td>0.67</td><td>0.85</td><td>0.75</td></tr><tr><td>8%</td><td>0.86</td><td>0.84</td><td>0.83</td><td>0.67</td><td>0.85</td><td>0.75</td></tr><tr><td>10%</td><td>0.85</td><td>0.82</td><td>0.83</td><td>0.67</td><td>0.84</td><td>0.74</td></tr></table>

Table 6  
Three domains' knowledge base.

<table><tr><td>Domain</td><td>Number of entities</td><td>Number of data fields</td></tr><tr><td>Mobile app</td><td>547,837</td><td>8,894,801</td></tr><tr><td>Movie</td><td>620,173</td><td>6,695,822</td></tr><tr><td>Restaurant</td><td>1,409,791</td><td>13,817,898</td></tr></table>

The variance of the number of tag path texts is not quite large in different websites; thus, we evaluate the runtime of our approach in pages with different scales. To verify ef<sup>fi</sup>ciency, SKES is applied to over 10 thousand high traf<sup>fi</sup>c websites indexed by Bing. The runtimes of our approach in different websites are recorded, a few of which are indicated in Fig. 8. Fig. 8 indicates that the runtime of SKES is generally linear with respect to the number of pages. For clusters containing hundreds of thousands pages, our approach can extract knowledge within hours.

## 5.4. Noise-tolerance evaluation

In this section, we evaluate the performance of our approach for noisy data. We generated <sup>fi</sup>ve more clusters that contain 2%, 4%, 6%,

Table 7  
A sample of submitted queries.

<table><tr><td>Query</td><td>Number of returned entities</td></tr><tr><td>2011 comedy movies</td><td>316</td></tr><tr><td>Movies casted by Tom Cruise</td><td>21</td></tr><tr><td>Movies from 2008 to 2010</td><td>53,485</td></tr><tr><td>Free mobile app</td><td>242,698</td></tr><tr><td>2011 games app</td><td>3557</td></tr><tr><td>Fruit ninja</td><td>10</td></tr><tr><td>Restaurant in Seattle</td><td>11,742</td></tr><tr><td>Restaurant rating over 4.0</td><td>231,423</td></tr></table>

8%, and 10% noise pages, respectively, by adding irrelevant pages (e.g. index pages, list pages) into the original detail pages dataset in a website. Our approach was run on the <sup>fi</sup>ve clusters, and their performance results are indicated in Table 5. The support threshold of our approach is set to 0.9. Under this threshold, our approach would fail to detect templates in pages containing over 10% noise. If we lower the support threshold, template detection may have low precision and recall.

Table 5 demonstrates that our approach and EXALG could tolerate a certain portion of noise pages, whereas RoadRunner failed to induce templates even with only 2% noise pages. The support threshold in SKES and SUPTHRES threshold in EXALG are both set to manage noise. SKES performed slightly better than EXALG when the noise percentage was greater than 2%. However, if the pages contained over 10% noise pages, a large number of data <sup>fi</sup>elds are lost in the results of both SKES and EXALG due to the effect of the noise pages, which caused some templates to be <sup>fi</sup>ltered out due to insuf<sup>fi</sup>cient support. Lowering the support threshold may relieve this problem, but may likewise degrade precision.

We run our method on the automatically clustered pages to build a knowledge repository of structured knowledge. After running our method on thousands of data-intensive websites, in addition to the aforementioned 30 selected websites, we built high-quality knowledge bases for three domains (over 97% precision), which contains greater than 2.5 million entities and 29 million data <sup>fi</sup>elds. Table 6 provides information on the knowledge base of each domain.

![](/api/attachments/FQUBHA7X/fulltext/images/0d561651c4e2d6646c41c842a3a7e5a6f3c0235caf760ac4b6524e17cb832fe9.jpg)  
Fig. 9. An example of returned structured knowledge by our prototype system.

Table 8  
Effectiveness of search task simpli<sup>fi</sup>cation.

<table><tr><td>Domains</td><td>Number of queries</td><td>Precision</td><td>Recall</td></tr><tr><td>Movie</td><td>20</td><td>82.17%</td><td>65.32%</td></tr><tr><td>Mobile app</td><td>20</td><td>87.55%</td><td>69.25%</td></tr><tr><td>Restaurant</td><td>20</td><td>85.71%</td><td>66.54%</td></tr></table>

## 5.5. Performance of search simplification

We implemented a prototype system for the user search task simpli<sup>fi</sup>cation (shown in Fig. 9) that utilizes the above knowledge base. As the problem of identifying the intent of user queries and triggering related structured knowledge for users is likewise highly dif<sup>fi</sup>cult, we employ a simple keyword-based method to implement our prototype system. That is, if user queries contain words equal to data <sup>fi</sup>elds in our knowledge base, we merely select and return structured knowledge of entities that satisfy all the keywords. If no satis<sup>fi</sup>ed entity exists, a traditional page list from Bing API<sup>7</sup> would be returned. For example, if a query “2011 comedy movies” is submitted, three words “2011”, “comedy”, and “movies” are identi<sup>fi</sup>ed as keywords for selecting satis<sup>fi</sup>ed entities from our knowledge base. Entities with the attributes “Domain” as “movie”, “Year” as “2011”, and “Genres” as “comedy”, are selected and returned. Our prototype system works well on these queries by further considering heuristic rules, such as identifying words “and”, “or”, “not” as operation AND, OR, NOT, and patterns “from … to …” as a range selection.

We used precision and recall as metrics to evaluate the effectiveness of the search task simpli<sup>fi</sup>cation. The editors submitted a group of queries with knowledge seeking intent that belongs to the three domains, a sample of which is shown in Table 7. The quality of returned structured knowledge was evaluated by directly searching from our knowledge base, which is calculated in the unit of entity. Table 8 presents the experimental results and proves that our prototype system can return high-quality structured knowledge to users with knowledge seeking tasks. The recall is slightly low because our knowledge base contains missing data <sup>fi</sup>elds, and related entities with missing data <sup>fi</sup>elds cannot match all keywords in queries.

In addition, we designed and distributed a questionnaire to 15 users who used the prototype system for a week, to obtain their feedback and subjective evaluation of our system. In the questionnaire, we asked users general information on the prototype system. Several interesting results are listed in Table 9. These questions were answered on a scale of 5, with 5 = strongly agree and 1 = strongly disagree. Table 9 demonstrates that the users were generally satis<sup>fi</sup>ed with the prototype system and admitted that this was helpful for them to seek knowledge. However, a few aspects of the prototype system, such as the problem of low recall, still require improvement.

## 6. Conclusions and future work

This paper presents an algorithm, SKES, that automatically extracts structured knowledge from semi-structured websites for search task simpli<sup>fi</sup>cation. SKES is demonstrated to be ef<sup>fi</sup>cient and noise-tolerant in real websites by using techniques such as top-down template induction algorithm and tag path representation.

Table 9  
Average rating of some questionnaire items.

<table><tr><td>Question</td><td>Rating</td></tr><tr><td>The demo is helpful for knowledge seeking</td><td>4.36</td></tr><tr><td>The demo usually returns correct table</td><td>4.16</td></tr><tr><td>A number of queries can trigger the demo to return structured table</td><td>3.87</td></tr><tr><td>I do not need to browse any pages to seek knowledge</td><td>3.53</td></tr><tr><td>The user interface of the demo is acceptable</td><td>4.06</td></tr><tr><td>Using this demo saves me a lot of time</td><td>4.10</td></tr></table>

After running our algorithm on thousands of related sites, a large structured knowledge base of high quality was built on three domains. We likewise developed a prototype system that simpli<sup>fi</sup>es user search tasks by using the built knowledge base. Our user study demonstrates that SKES bene<sup>fi</sup>ts users in knowledge searches.

Our work offers diverse future directions. On structured data extraction, extracting speci<sup>fi</sup>c structures (such as tables) from HTML pages may improve the effectiveness of SKES. Incorporating several data extraction algorithms to achieve better results is an important and challenging aspect that could be studied. As websites and web pages dynamically change, we will further study methods for updating the templates by developing an incremental extraction method instead of running the extraction process from the beginning. We also intend to focus on methods to detect the structure change of web pages. In addition, more domains require consideration, and techniques in information integration [25] should be adopted, to build large and high-quality knowledge bases. We may also take advantage of techniques, such as attribute names prediction [2], attribute names classi<sup>fi</sup>cation [7], or <sup>fl</sup>exible string match [17], instead of manually labeling each column of extracted knowledge table. For our prototype system of search task simpli<sup>fi</sup>cation, processing of user queries similarly requires improvements in recall.

## Acknowledgment

This work was supported by the 973 program of China under Grant No. 2012CB316205, the major program of National Social Science Fund of China under Grant No. 12&ZD220, the National Natural Science Foundation of China under Grant Nos. 71272029, 61033010 and 71110107027, and by the Microsoft Research Asia (FY11-RES-OPP-058).

## References

[1] A. Arasu, H. Garcia-Molina, Extracting structured data from web pages, Proceedings of the 22th ACM SIGMOD International Conference on Management of Data. 2003, pp. 337-348

[2] L. Arlotta, V. Crescenzi, G. Mecca, P. Merialdo, Automatic annotation of data extracted from large web sites, Proceedings of the Sixth International Workshop on the Web and Databases (WebDB), 2003, pp. 7–12.

[3] M. Banko, M.J. Cafarella, S. Soderland, M. Broadhead, O. Etzioni, Open information extraction from the web, Proceedings of the 20th International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI), 2007, pp. 2670–2676

[4] L. Blanco, N.N. Dalvi, A. Machanavajjhala, Highly ef<sup>fi</sup>cient algorithms for structural clustering of large websites, Proceedings of the 20th International World Wide Web Conference (WWW), 2011, pp. 437–446.

[5] S. Brin, Extracting patterns and relations from the World Wide Web, Proceedings of the 1st International Workshop on the Web and Databases (WebDB), 1998, pp. 172–183.

[6] M.J. Cafarella, A.Y. Halevy, Y. Zhang, D.Z. Wang, E. Wu, Uncovering the relational web Proceedings of the 11th International Workshop on Web and Databases (WebDB), 2008.

[7] A. Carlson, C. Schafer, Bootstrapping information extraction from semi-structured web pages, Proceedings of the European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML/PKDD) 2008, pp. 195–210.

[8] S.W.K. Chan, Beyond keyword and cue-phrase matching: a sentence-based abstraction technique for information extraction, Decision Support Systems 42 (2) (2006) 759-777

[9] Chia-Hui Chang, Chun-Nan Hsu, Shao-Cheng Lui, Automatic information extraction from semi-structured Web pages by pattern discovery, Decision Support Systems 35 (1) (2003) 129–147.

[10] C.H. Chang, M. Kayed, M.R. Girgis, K.F. Shaalan, A survey of web information extraction systems, IEEE Transactions on Knowledge and Data Engineering 18 (10) (2006) 1411–1428.

[11] W.W. Cohen, M. Hurst, L.S. Jensen, A <sup>fl</sup>exible learning system for wrapping tables and lists in html documents, Proceedings of the 11th International Conference on World Wide Web (WWW), 2002, pp. 232–241.

[12] V. Crescenzi, G. Mecca, P. Merialdo, RoadRunner: towards automatic data extraction from large web sites, Proceedings of the 27th International Conference on Very Large Data Bases (VLDB), 2001, pp. 109–118.

[13] V. Crescenzi, G. Mecca, P. Merialdo, Proceedings of the 17th ACM Symposium on Applied Computing (SAC), 2002, pp. 1108–1112.

[14] N. Derouiche, B. Cautis, T. Abdessalem, Automatic Extraction of Structured Web Data with Domain Knowledge, Proceedings of the 28th International Conference on Data (ICDE), 2012, pp. 726–737.

[15] D.W. Embley, M. Hurst, D.P. Lopresti, G. Nagy, Table-processing paradigms: a research survey, International Journal on Document Analysis and Recognition 8 (2–3) (2006) 66–86.

[16] O. Etzioni, M.J. Cafarella, D. Downey, A.M. Popescu, T. Shaked, S. Soderland, D.S. Weld, A. Yates, Unsupervised named-entity extraction from the web: an experimental study, Arti<sup>fi</sup>cial Intelligence 165 (1) (2005) 91–134.

[17] P. Gulhane, R. Rastogi, S.H. Sengamedu, A. Tengli, Exploiting content redundancy for web information extraction, Proceedings of the 19th International Conference on World Wide Web (WWW), 2010, pp. 1105–1106.

[18] P. Gulhane, A. Madaan, R.R. Mehta, J. Ramamirtham, R. Rastogi, S. Satpal, S.H. Sengamedu, A. Tengli, C. Tiwari, Web-scale information extraction with vertex, Proceedings of the 27th International Conference on Data (ICDE), 2011, pp. 1209–1220.

[19] B. He, M. Patel, Z. Zhang, K.C.C. Chang, Accessing the deep web, Communications of the ACM 50 (5) (2007) 94–101.

[20] J. Hong, Z. He, D.A. Bell, An evidential approach to query interface matching on the deep web, Information Systems 35 (2) (2010) 140–148.

[21] A.H.F. Laender, B.A. Ribeiro-Neto, A. Soares da Silva, J.S. Teixeira, A brief survey of web data extraction tools, SIGMOD Record 31 (2) (2002) 84–93.

[22] B. Liu, Y. Zhai, Net — a system for extracting web data from <sup>fl</sup>at and nested data records, Proceedings of the 6th International Conference on Web Information Systems Engineering (WISE), 2005, pp. 487–495.

[23] B. Liu, R.L. Grossman, Y. Zhai, Mining data records in web pages, Proceedings of the 9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (SIGKDD), 2003, pp. 601–606.

[24] G. Miao, J. Tatemura, W.P. Hsiung, A. Sawires, L.E. Moser, Extracting data records from the web using tag path clustering, Proceedings of the 18th International Conference on World Wide Web (WWW), 2009, pp. 981–990

[25] H. Wache, T. Vögele, U. Visser, H. Stuckenschmidt, G. Schuster, H. Neumann, S. Hübner, Ontology-based integration of information — a survey of existing approaches, Proceedings of the IJCAI-01 Workshop on Ontologies and Information Sharing, 2001, pp. 108–117.

[26] Y.W. Wong, D. Widdows, T. Lokovic, K. Nigam, Scalable attribute–value extraction from semi-structured text, IEEE International Conference on Data Mining Workshops (ICDMW 2009), 2009, pp. 302–307.

[27] Y. Xia, H. Yu, S. Zhang, Automatic web data extraction using tree alignment, Proceedings of the 18th ACM Conference on Information and Knowledge Management (CIKM). 2009. pp. 1645-1648.

[28] G. Yang, I.V. Ramakrishnan, M. Kifer, On the complexity of schema inference from web pages in the presence of nullable data attributes, Proceedings of the Twelfth International Conference on Information and Knowledge Management (CIKM), 2003, pp. 224–231.

[29] J.M. Yang, R. Cai, Y. Wang, J. Zhu, L. Zhang, W.Y. Ma, Incorporating site-level knowledge to extract structured data from web forums, Proceedings of the 18th International Conference on World Wide Web (WWW), 2009, pp. 181–190.

[30] B. Yue, J. Yan, H. Liang, N. Liu, L. Ji, F. Bai, Z. Chen, Quantum path integral inspired query sequence suggestion for user search task simpli<sup>fi</sup>cation, Proceedings of the 2010 IEEE International Conference on Data Mining Workshops (ICDMW 2010), 2010, pp. 647–654.

[31] Y. Zhai, B. Liu, Web data extraction based on partial tree alignment, Proceedings of the 14th International Conference on World Wide Web (WWW), 2005, pp. 76–85.

[32] S. Zhao, J. Betz, Corroborate and learn facts from the web, Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (SIGKDD), 2007, pp. 995–1003.

[33] H. Zhao, W. Meng, Z. Wu, V. Raghavan, C.T. Yu, Fully automatic wrapper generation for search engines, Proceedings of the 14th International Conference on World Wide Web (WWW), 2005, pp. 66–75.

[34] H. Zhao, W. Meng, C.T. Yu, Mining templates from search result records of search engines, Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (SIGKDD), 2007, pp. 884–893.

![](/api/attachments/FQUBHA7X/fulltext/images/3db96ac62bfcdecd8b77831bde3b8e3ab34ba4669cad3d836f70306a0e9e4b32.jpg)

Jun He is an associate professor in the School of Information, Renmin University of China, China. He received his PhD in Computer Science from Renmin University of Chi na. His current research interests include data mining, web mining, information retrieval, and database. Dr. He is a member of ACM, IEEE and has published papers in many international conferences such as ACM SIGKDD, IEEE ICDM, SIAM on Data Mining and PAKDD, and journals such as ACM TOIS, IEEE TKDE, Information Sciences, DSS, Computational Intelligence and Knowledge and Informa tion Systems.

![](/api/attachments/FQUBHA7X/fulltext/images/59bc5736f814925c0a60a095f3dc995fa5f631b2a7fc1020672d5937d2541a96.jpg)

Yingqin Gu is a Master's student in the School of Information, Renmin University of China. His research interests involve social network and web data mining. He has pub lished papers in some international conferences such as CIKM, ADMA and WAIM

![](/api/attachments/FQUBHA7X/fulltext/images/01fbbe79140e4fb693d903814167b95d1a99634a5b76d87c753223844f4c58fd.jpg)

Hongyan Liu is a professor in the Management Science and Engineering Department, Tsinghua University, China She received her PhD in Management Science from Tsinghua University. Her current research interests include Business Intelligence data mining text and web mining OLAP and Data Warehousing. Dr. Liu is a member of ACM, IEEE, SIAM and AIS and has published many papers in top journals such as INFORMS Journal on Computing, ACM TODS, ACM TOIS, IEEE TKDE, DSS and Information Sciences, and in many top international conferences such as VLDB, IEEE ICDE, ACM SIGKDD, IEEE ICDM, SIAM on Data Mining and ACM CIKM. She has won several best paper awards in international conferences such as SDM.

![](/api/attachments/FQUBHA7X/fulltext/images/1400574fc77a4b1e3294d0912701b22611ed97956347701768e3fe4a91a51bdd.jpg)

Jun Yan received his PhD degree from the Department of Information Science, School of Mathematical Science, Peking University, PR China. Currently he is working in the machine learning group of MSRA as a lead researcher. His research interests are on online advertising, large scale information extraction and mining, data preprocessing and information retrieval, etc. So far, he has successfully incubated several technologies, which have been used in Microsoft products. In academia, he has more than 50 quality papers published in referred conferences and journals, including SIGKDD, SIGIR, WWW, ICDM, and TKDE. He has been a PC member of international conferences such as SIGKDD and SIGIR etc.

Hong Chen received the B. E. degree from Renmin University of China in 1986 and the M. E. degree from Renmin University of China, in 1989. In 2000, she received her Ph. D. degree from the Institute of Computing Technology, CAS. She is a professor in the School of Information, Renmin University of China. Her research interests include database systems, data warehouse and data mining, and wireless sensor networks.

![](/api/attachments/FQUBHA7X/fulltext/images/e3b146b3e49edb63610599c7ec1b5635dbc7f9c636e2370784df02164ab56fda.jpg)
