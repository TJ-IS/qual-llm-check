---
otero_id: 13172
otero_key: "43BP7SVM"
title: "Ranking web sites using domain ontology concepts"
authors: "Ahmad Kayed; Eyas El-Qawasmeh; Zakariya Qawaqneh"
year: "2010"
journal: "Information & Management"
doi: "10.1016/j.im.2010.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ranking web sites using domain ontology concepts

Ahmad Kayed <sup>a,</sup>\*, Eyas El-Qawasmeh <sup>b</sup>, Zakariya Qawaqneh <sup>c</sup>

<sup>a</sup> Fahad Bin Sultan University, P.O. Box 15700, Tabuk 71454, Saudi Arabia

<sup>b</sup> King Saud University, Saudi Arabia

<sup>c</sup> Jordan University of Science and Technology, Jordan

## A R T I C L E I N F O

Article history: Received 1 January 2009 Received in revised form 1 February 2010 Accepted 1 June 2010 Available online 26 August 2010

Keywords: Ontology Ontology concepts Ranking Semantic web Electronic commerce Relevancy Search engine

## A B S T R A C T

Many web search engines retrieve enormous amounts of irrelevant information in answer to users’ queries. The semantic web provides a promising approach to improve search operation. For specific domains, ontologies can capture concepts to help machines deal with data semantically. Our aim in writing this paper was to show how to measure the closeness (relevancy) of retrieved web sites to user query-concepts and re-rank them accordingly. We therefore proposed a new relevancy measure to rerank retrieved documents. We termed the approach ‘‘ontology concepts’’ and it on the domain of electronic commerce. Results suggested that we could re-rank the retrieved documents (web sites) according to their relevancy to the search query. Our method depends on the frequency of the ‘‘ontology concepts’’ in the retrieved documents and uses this to compute their relevancy.

\- 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The semantic web uses ontology as a tool to capture concepts for specific domains. As a result, computers can deal with the data of those domains semantically. An ontology language can be used generate class and property descriptions based on their names, along with some axioms about them.

Ontology is becoming an important area in IS research. It intersects with: artificial intelligence, software engineering, information architecture, agent based systems, e-commerce content, e-learning, the semantic web, bioinformatics, and geographical IS [3–6,15]. Ontologies have many benefits. First, they capture the concepts, their properties, and their relationships. Second, they represent the domain data in a semantic way and define the knowledge that is embedded in the domain. Third, they can be used to analyze the domain independent of any application requirements. Fourth, they are used to satisfy the new vision of the next generation of the WWW, the semantic web. Fifth, they can be used to build web data in a structured way.

One of the main challenges for search engines is to provide a good ranking for documents that are retrieved as relevant to the users’ query. They use several criteria to rank web documents.

Many involve the use of the number of keyword hits of the retrieved documents as the criteria, ignoring the semantics of their contents. Our approach used the ontology to build a relevancy measure that checked how close the content of a document was to the user query.

The domain of e-commerce has provided many documents that discuss its role in the WWW. The increasing number of users using and dealing with e-commerce on the web and the increasing number of applications in its domain have made it an interesting application to study.

Our approach is termed ‘‘ontology concepts’’. Our ‘‘ontology concepts’’ approach differs from ‘‘keyword concepts’’ because ‘‘ontology concepts’’ search on the semantic of the users’ query not merely on keywords. We have applied this approach in several fields, such as of software quality, the modeling diagrams, requirements engineering, and e-law [7].

Several semantic approaches have been used to search they include concept- and entity-based methods, relying on some form of indexing that summarize or extracts the document’s semantics [1,14]. PageRank depends on a link-analysis that uses hyperlinks for ranking purposes. Ontology concepts and relations were used to define hyperlink relationships that indicate the important entities but unimportant entities might not be selected, maybe undermining the approach. Meza discussed the use of semantic relationships for ranking documents without relying on the existence of any specific structure in the document or links between documents. He used the relationships that existed between the entities in a populated ontology. Relevancy measure in this approach were based on the traversal and semantics of relationships that link entities in an ontology while ours was based on ontology concepts and the frequencies with which these concepts were encountered in a specific document. Semantic technologies are gaining wider use in Web applications. There are ontologies available in some domains that were built with significant human effort. Fortunately, large ontologies can be built using tools for extracting and annotating the metadata; a survey of such Web data extraction tools was presented in [9].

## 2. Related work

Most search engines compete by enhancing the quality of their results. Measures such as recall, precision, and others have been created to help in achieving this goal. Nowadays, the number of retrieved results (sites, documents, etc.) for any search is very large. Measures are needed to recall only the sites or documents that are most related to the user’s query. These measures may be used later to rank the retrieved results from the most to the least relevant. Many search engines are using several approaches and measures to rank the documents. Approaches can be classified into two groups: one does not use ontologies while the other believes that ontologies will enhance the ranking process.

Of the non-ontological ranking methods, PageRank and HITS (Hypertext Induced Topic Search) are the most common approaches. The PageRank method depends on analysis of the web structure links in order to rank the returned documents [10,13]; this implies that a document having more incoming links has a higher ranking. The HITS is a query-based ranking technique; it uses the link structure to provide two ranking scores: the ‘‘Authority Pages’’ score, which refers to the most relevant pages for the user query, and the ‘‘Hub Pages’’ score which refers to the pages that have links to other authority pages [11].

There are many search engines that use ontology in searching the web. The common ones are now briefly discussed. OntoSearch helps users find relevant documents by combining Google-Web APIs with a hierarchic visualization technique; it allows users to search via a on certain ontology files; it also allows users to inspect the files to check their relevancy [16]. OntoSearch allows the user to enter some words to determine the required ontology. The OntoSearch system is based on JSP, and other technologies. Swoogle is a search engine that exploits the structure of semantic web documents which have been characterized by semantic annotation and meaningful references to other semantic web documents [2]; it crawls and indexes the semantic web documents and stores them, allowing the user to make queries using simple keywords based on the interface. It then returns all ontologies that contain the keywords, allowing the user to choose the appropriate one. It then extracts the terms and their relationships to provide the relevant documents. Thus it helps users find ontology terms and determine the search properties of their terms.

OntoKhoj is a search engine, which is based on algorithms used for searching, aggregating, ranking, and classifying ontologies in Semantic Web. It allows the user to search for suitable ontology by using a keyword based on a searching interface, but does not allow searching for web documents that do not refer to a predefined ontology. ONTOSEARCH2 searches and allows queries by creating and storing a copy of its ontologies in tractable description logic. The core of ONTOSEARCH2 is an inference engine for the Lite Description Logic (DL-Lite) ontology language. ONTOSEARCH2 allows users to query its stored data by using the SPAQL query language. It contains DL-Lite (logic), and a fuzzy DL-Lite query engine, which is used for query answering over ontologies. TOSS can return more relevant documents through expanding a query by using other words that have the same meaning using ontologies [8]. Sim developed an Information Filtering Agent using ontology to determine the relevant documents in its searches. The Agent uses some factors to calculate relevancy. It thus determines evidence phrases using the WORDNET ontology, computing the frequency of evidence phrases, and nearness of keywords.

Our work was based on the idea of building on the results (retrieved web documents) of existing search engines and using ontology to re-rank the documents according to their relevancy to the search query. Our objective was to show how ontology could be used in better ranking retrieved documents. This measure could also be used to test the quality of search engines. We therefore built ontology for the e-commerce domain and then tested their effectiveness in retrieving relevant documents. However, to build a full and formal ontology is beyond the scope of this paper.

## 3. Ranking method and search engine results

## 3.1. The ranking method

## 3.1.1. The first phase: building ‘‘ontology concepts’’

We split the methodologies for building ontologies around three major stages of the ontology life cycle Building, Manipulating, and Maintaining (see Fig. 1). These three stages are overlapped. Ellipses in Fig. 1 represent the inner steps for each stage.

Building ‘‘ontology concepts’’ is a necessity in order for them to be used in the second phase. For this purpose, we generated our ‘‘ontology concepts’’ using KAON, (KArlsruhe ONtology) [12], which was designed for the English language; it is primarily a framework for the developing ontology-based applications. It is an open-source ontology management infrastructure targeted for business applications; it includes a comprehensive tool suite providing functionalities center around easy creation, storage, retrieval, and maintenance of ontologies. KAON, with its simple framework, makes it possible to navigate and search ontologies through Web browsers.

The electronic commerce domain was selected for our research. The key motivation for choosing this was the increasing number of web documents that discuss electronic commerce. It should be pointed out here that the automatic tools depend on the most common terms and most frequent terms in a specific domain. The input to KAON is thus a set of documents. They were collected from several resources such as online reports, news, and academic research. The extracted ‘‘ontology concepts’’ for electronic commerce consisted of concepts that are not only the most frequent terms but also those having high ontological relevance keywords according with KAON. The highest 34 concepts were used as a base in order to test our ranking method. Our criterion for choosing the ‘‘best’’ concepts was to answer the question: Are these concepts covering the meaning of the user’s query? We collected ten e-commerce definitions and found that the 34 concepts covered 90% of the definitions. This was thus our criteria in choosing them. The following terms are the ones we found for the e-commerce domain:

![](/api/attachments/43BP7SVM/fulltext/images/34009c28475790bc04de03716883ec1584581239bba1a2f15a8d49fa39c4865c.jpg)  
Fig. 1. Methodology of building ontologies.

Table 1  
Ontology concepts for the domain of ‘‘e-Commerce’’.

<table><tr><td>Communications</td><td>Exchange</td><td>Declaration</td></tr><tr><td>Trade</td><td>Merchandise</td><td>Payment</td></tr><tr><td>Partners</td><td>Services</td><td>Monetary</td></tr><tr><td>Mediators</td><td>Information</td><td>Stores</td></tr><tr><td>Traders</td><td>Goods</td><td>Activity</td></tr><tr><td>Trade</td><td>Service</td><td>Merchandise</td></tr><tr><td>Productions</td><td>Customers</td><td>Marketing</td></tr><tr><td>Buyer</td><td>Selling</td><td>Shares</td></tr><tr><td>Seller</td><td>Buying</td><td>Consolidation</td></tr><tr><td>Agents</td><td>Consumers</td><td>Demand</td></tr><tr><td>Internet</td><td>Producers</td><td>Credit Card</td></tr><tr><td>Companies</td><td></td><td>Bills</td></tr></table>

Once these steps have been completed, the ‘‘e-commerce ontology concepts’’ are ready to be used in our ranking method (Table 1).

## 3.1.2. The second phase: using the ‘‘ontology concepts’’ to measure relevance

Documents/sites are retrieved in the domain of interest (ecommerce here) using the specified search engines; the ranks of these documents are stored according to the search engines’ (e.g., AltaVista, Google, or Yahoo) ordering. This step was also divided into two parts; the first converts the retrieved documents/sites into text format saving their original ranking, while, In the second, the retrieved documents were input into our algorithm where each was given a new rank based on its ‘‘distance’’ from the ontology

Algorithm complexity: Let N be the maximum number of words in any document; let M be the maximum number of ontology concepts (where N > M). In the above algorithm, Step E will be the longest step in the algorithms since it takes two loops to compute the number of occurrences of ontology concepts in each document. In the worst case, it will take M - N; this implies that the complexity of the algorithm is O(n<sup>2</sup>). The algorithm uses a list of stop words. These stop words are eliminated from the documents. Stop words are generally about 30% of a document. This reduces the complexity of the algorithm and enhances its performance.

The experiments: A program in Visual Basic was written to test our algorithm. It was applied to real data to evaluate its performance. In our experiment we considered three different search engines: AltaVista, Google, and Yahoo. The documents were ranked based on three methods. The first was based on the search engines themselves. The second was based on our method. The algorithm was run to assign the new ranks for each document. In the third, we asked three experts who work in the field of ecommerce to read the first 30 retrieved documents for each search engine and re-rank them from the most relevant to the least. Three conditions made in choosing our experts: they had professors who had been teaching e-commerce for more than two years; working in reputable universities, and publishing books and journal papers in e-commerce fields. Our resources for ontology concepts were: books, reports, research papers, manuals; the collection date spanned from Feb-2007 to June-2007.

The ranks produced by our method and those of the search engines were compared those of the experts. It was assumed that the domain experts would rank each document in the best order by its relevancy to the user query. Only the first thirty documents were selected because it was difficult to find domain experts to rank more. At the same time, our domain experts told us that the relevancy ordering would be likely to be inaccurate after the first twenty. The detailed algorithm is given in Appendix A.

Search engine results: For the sake of clarity and brevity, we will only discuss the results of the Yahoo search engine in detail. They are summarized in Table 2. The table is divided into 6 parts. The first is a sequence number for referencing purposes. The second shows the three experts’ ranks for a document. The third gives the Yahoo ranking, while the fourth shows our ranking. Parts five and six represent the absolute distance (assumed error) between the experts’ ranking and both Yahoo and our algorithm. The second part of the table shows the experts ranking for the first thirty documents retrieved by Yahoo as relevant documents for the ecommerce domain. The first column in the second part shows the ranking of expert one for these thirty documents. Yahoo ranking for these thirty documents is the order of these documents as retrieved by Yahoo. The fourth part shows results of our method for the same thirty documents. For example, part four shows that the document in position two will be ranked as the 27th document, while the document in position three will be ranked as the 17th document according to our algorithm

The fifth part of the table computes the distance for each document between its rank in Yahoo and its rank according to each of our experts. For example, the rank of the document in the fourth row is 22 according to expert 1 while its rank is 4 by Yahoo. So, the difference of the ranking position for document four between Yahoo and expert one is the absolute value of (22–4) = 18 positions.

The last part shows the distance between each document’s position in our proposed method and its position according to the experts. For example, the document in row four is ranked as 21 by our method while it is ranked as 22, 20, and 17 by expert one, two, and three respectively. So, the absolute difference between our method for document four (in row four) and expert one, two, and three were 22–21 = 1, 20–21 = 1, 17–21 = 4, respectively.

The average ranking error represents the average distance for the documents between their original rank and the experts’ ranks. The average ranking error for Yahoo search engine according to expert one is taken by calculating the average for the values in column 1 of part 5. Thus Yahoo on average ranks every document 8.5 positions from its correct position according to expert one. The average ranking error for our method according to expert one was computed by calculating the average for the values in column 1 of part 6. This means that our approach on average ranked every document 1.4 positions from its correct position per expert one.

The same calculations were repeated for and the other two experts. Therefore, according to expert two, and expert three, the average ranking errors for Yahoo search engine were 8.2 and 8.7, respectively. Also, the average ranking errors for our approach were 1.9 and 2.5, respectively.

The average error for Yahoo search engine ranking compared to the three experts rankings was 8.5. The average error for our method was 1.9. Therefore, by dividing the average distance of Yahoo search engine on the distance of our proposed method ‘‘ontology concepts’’, we can conclude that our ranking was significantly better than Yahoo’s search engine ranking.

Fig. 2 shows two curves, the blue one shows the average difference between each document’s position in Yahoo and the position of each document according to the three experts. The pink curve shows the average difference between each document’s position in our method and the position of each document according to the three experts. For example, the average difference between the position of document 9 in Yahoo and its position according to the three experts was 6, while the average of our method was 1.

Yahoo search engine results compared with our proposed method ‘‘ontology concepts’’ according to the three experts.

<table><tr><td rowspan="2">Position</td><td colspan="3">Expert ranking</td><td rowspan="2">Yahoo ranking</td><td rowspan="2">Ontology ranking</td><td colspan="3">Distance (error) between Yahoo search engine and expert one, two, and three</td><td colspan="3">Distance (error) between our method (ontology concepts) and expert one, two, and three</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>24</td><td>24</td><td>21</td><td>2</td><td>27</td><td>22</td><td>22</td><td>19</td><td>3</td><td>3</td><td>6</td></tr><tr><td>3</td><td>9</td><td>6</td><td>11</td><td>3</td><td>17</td><td>6</td><td>3</td><td>8</td><td>8</td><td>11</td><td>6</td></tr><tr><td>4</td><td>22</td><td>20</td><td>17</td><td>4</td><td>21</td><td>18</td><td>16</td><td>13</td><td>1</td><td>1</td><td>4</td></tr><tr><td>5</td><td>27</td><td>26</td><td>28</td><td>5</td><td>25</td><td>22</td><td>21</td><td>23</td><td>2</td><td>1</td><td>3</td></tr><tr><td>6</td><td>2</td><td>3</td><td>2</td><td>6</td><td>2</td><td>4</td><td>3</td><td>4</td><td>0</td><td>1</td><td>0</td></tr><tr><td>7</td><td>15</td><td>14</td><td>15</td><td>7</td><td>15</td><td>8</td><td>7</td><td>8</td><td>0</td><td>1</td><td>0</td></tr><tr><td>8</td><td>6</td><td>4</td><td>7</td><td>8</td><td>7</td><td>2</td><td>4</td><td>1</td><td>1</td><td>3</td><td>0</td></tr><tr><td>9</td><td>3</td><td>2</td><td>4</td><td>9</td><td>4</td><td>6</td><td>7</td><td>5</td><td>1</td><td>2</td><td>0</td></tr><tr><td>10</td><td>29</td><td>29</td><td>29</td><td>10</td><td>29</td><td>19</td><td>19</td><td>19</td><td>0</td><td>0</td><td>0</td></tr><tr><td>11</td><td>16</td><td>16</td><td>16</td><td>11</td><td>12</td><td>5</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td></tr><tr><td>12</td><td>18</td><td>17</td><td>27</td><td>12</td><td>18</td><td>6</td><td>5</td><td>15</td><td>0</td><td>1</td><td>9</td></tr><tr><td>13</td><td>5</td><td>5</td><td>5</td><td>13</td><td>5</td><td>8</td><td>8</td><td>8</td><td>0</td><td>0</td><td>0</td></tr><tr><td>14</td><td>12</td><td>12</td><td>9</td><td>14</td><td>3</td><td>2</td><td>2</td><td>5</td><td>9</td><td>9</td><td>6</td></tr><tr><td>15</td><td>21</td><td>22</td><td>24</td><td>15</td><td>22</td><td>6</td><td>7</td><td>9</td><td>1</td><td>0</td><td>2</td></tr><tr><td>16</td><td>30</td><td>30</td><td>30</td><td>16</td><td>30</td><td>14</td><td>14</td><td>14</td><td>0</td><td>0</td><td>0</td></tr><tr><td>17</td><td>11</td><td>11</td><td>12</td><td>17</td><td>11</td><td>6</td><td>6</td><td>5</td><td>0</td><td>0</td><td>1</td></tr><tr><td>18</td><td>4</td><td>9</td><td>3</td><td>18</td><td>6</td><td>14</td><td>9</td><td>15</td><td>2</td><td>3</td><td>3</td></tr><tr><td>19</td><td>10</td><td>8</td><td>10</td><td>19</td><td>10</td><td>9</td><td>11</td><td>9</td><td>0</td><td>2</td><td>0</td></tr><tr><td>20</td><td>19</td><td>21</td><td>22</td><td>20</td><td>19</td><td>1</td><td>1</td><td>2</td><td>0</td><td>2</td><td>3</td></tr><tr><td>21</td><td>7</td><td>7</td><td>6</td><td>21</td><td>9</td><td>14</td><td>14</td><td>15</td><td>2</td><td>2</td><td>3</td></tr><tr><td>22</td><td>13</td><td>13</td><td>13</td><td>22</td><td>13</td><td>9</td><td>9</td><td>9</td><td>0</td><td>0</td><td>0</td></tr><tr><td>23</td><td>23</td><td>23</td><td>19</td><td>23</td><td>23</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>4</td></tr><tr><td>24</td><td>20</td><td>19</td><td>20</td><td>24</td><td>20</td><td>4</td><td>5</td><td>4</td><td>0</td><td>1</td><td>0</td></tr><tr><td>25</td><td>25</td><td>25</td><td>18</td><td>25</td><td>28</td><td>0</td><td>0</td><td>7</td><td>3</td><td>3</td><td>10</td></tr><tr><td>26</td><td>17</td><td>18</td><td>23</td><td>26</td><td>16</td><td>9</td><td>8</td><td>3</td><td>1</td><td>2</td><td>7</td></tr><tr><td>27</td><td>28</td><td>28</td><td>25</td><td>27</td><td>24</td><td>1</td><td>1</td><td>2</td><td>4</td><td>4</td><td>1</td></tr><tr><td>28</td><td>8</td><td>10</td><td>8</td><td>28</td><td>8</td><td>20</td><td>18</td><td>20</td><td>0</td><td>2</td><td>0</td></tr><tr><td>29</td><td>14</td><td>15</td><td>14</td><td>29</td><td>14</td><td>15</td><td>14</td><td>15</td><td>0</td><td>1</td><td>0</td></tr><tr><td>30</td><td>26</td><td>27</td><td>26</td><td>30</td><td>26</td><td>4</td><td>3</td><td>4</td><td>0</td><td>1</td><td>0</td></tr><tr><td>The average error</td><td></td><td></td><td></td><td></td><td></td><td>8.47</td><td>8.07</td><td>9.00</td><td>1.40</td><td>2.00</td><td>2.40</td></tr></table>

The test was repeated using the AltaVista, and Google search engines. For expert one, the average ranking error for AltaVista and Google were 9.3 and 7.5, respectively, but the average ranking error for our method were 1.7 and 3.4, respectively. According to expert two, and expert three, the average ranking error for AltaVista were 8.9 and 10.1. And for Google were 7.1 and 8.4, respectively. Also, the average ranking errors for our method compared to AltaVista were 1.9 and 2.4, respectively. Similarly with Google the error was 4.2 and 4.6, respectively. These results are summarized in Table 3 which compares our approach with the three search engines. From the table we see that Yahoo, AltaVista, and Google had average errors of 8.51, 9.42, and 7.64, respectively. Thus Google was the closest in relevancy to our approach.

![](/api/attachments/43BP7SVM/fulltext/images/6f5b67561f8fa4369e81d5b9547c96d18f1ace43b0cd2bd4d6e15e3493b76e05.jpg)  
Fig. 2. Comparing Yahoo and our results.

The results confirm that our method was best in ranking documents.

Fig. 3 shows two curves, the blue represents the distance between each document’s position in AltaVista and its rank according to the three experts. The pink curve represents the distance between each document’s position according t our ‘‘ontology concepts’’ and the position of each document according to the three experts.

Fig. 4 shows two curves, the blue one shows the average difference between each document’s position in Google and the position of each document according to the three experts. The pink curve shows the average difference between each document’s

## Table 3

A summary of the average distances between the three search engines and our proposed method according to the three experts.

<table><tr><td></td><td>Yahoo</td><td>Our approach</td><td>AltaVista</td><td>Our approach</td><td>Google</td><td>Our approach</td></tr><tr><td>Expert 1</td><td>8.47</td><td>1.40</td><td>9.33</td><td>1.73</td><td>7.47</td><td>3.80</td></tr><tr><td>Expert 2</td><td>8.07</td><td>2.00</td><td>8.77</td><td>1.93</td><td>7.07</td><td>4.33</td></tr><tr><td>Expert 3</td><td>9.00</td><td>2.40</td><td>10.07</td><td>2.40</td><td>8.40</td><td>4.67</td></tr><tr><td>Averages</td><td>8.51</td><td>1.93</td><td>9.42</td><td>2.02</td><td>7.64</td><td>4.27</td></tr></table>

![](/api/attachments/43BP7SVM/fulltext/images/c3661d99bcf7caaa4d9349d41e62e796f131b1bd0535295053aad992314a1bdb.jpg)  
Fig. 3. Comparing AltaVista and our results.

![](/api/attachments/43BP7SVM/fulltext/images/8b1c391e27628a7bc3d314b05deefbbdeac047cbe2f90b2fc05f12d3ff56ab4f.jpg)  
Fig. 4. Comparing Google and our results.

position in our method and the position of each document according to the three experts.

## 4. Discussion

One may ask: if the relevancy of order in a search drops dramatically after the 30th site, is it worth building ontology into the search algorithm? We respond that users in many cases may use more than one search engine and thus need to browse beyond 90 sites. Also normal users will access three to five sites. It is beyond human capacity to read 90 sites thoroughly. However even if the relevancy is small after the 30th site, our approach will find the most relevant ones. We agree that building and maintaining ontologies for each user’s query will be expensive and it may not be applicable. However, building ontology concepts is affordable for a specific domain and it will be open for any number of users in that domain.

Our approach is language independent. We applied our application to the Arabic e-commerce domain. The main problem with using an Arabic formal ontology is the absence of the Arabic top level ontology. This forced us to collect our ‘‘ontology concepts’’ resources in English and then translate them to Arabic.

## 5. Conclusions

We have proposed a new approach, the use of ‘‘ontology concepts". as a relevancy measure to re-rank retrieved web documents. We showed its value in the electronic commerce domain. The re-ranking of documents enhanced their relevancy. Our results showed that the average ranking error was less than several search engines.

## Acknowledgment

The first author would like to thank Fahad Bin Sultan University (FBSU) for their support for this research. Also he would like to thank Dr. Shatha Kayed for enhancing the readability of the paper.

## Appendix A. The ranking method

Part one: Obtain the documents and theirs ranks Begin

## Step A

Retrieve documents using search engines. The query ‘‘ecommerce’’ was used to retrieve the relevant web documents.

## Step B

Save the first 30 (or any desired number) documents in text format and save them. These are the data source for testing.

## Step C

Save the original ranking of each document as retrieved by each search engine. Thus document N will be given rank number N, etc.

## End

Here, the original ranks were saved for comparison with our measure.

Part two: The ranking method is based on the ‘‘ontology concepts’’. The algorithm splits each document for each search engine into words and computes the occurrences of these words in the proposed ontology concepts; it then re-ranks these documents according to the number of occurrences.

## Procedure Re-Rank

## Begin

This procedure will be run separately for each search engine.

Step A: For each text document, store its words into an array.

Read the text files to divide each document into words. Then store the words in a string array called split.

Step B: Store only one occurrence for each word into an array.

Eliminate the frequency of words for each document and store them without frequency in a string array called uniqueSplit.

Step C: Eliminate the stop words by using an array of stopwords.

Store stop words in an array to eliminate them from each document. They are to be ignored during the comparison process.

Step D: Determine the ‘‘ontology concepts’’ for each document.

Words in the uniqueSplit Array for each document are compared with the words of the ‘‘ontology concepts’’. Store only the words in the document that are included as ‘‘ontology concepts’’ into an array called DocOntWords.

Step E: Count the frequency of ‘‘ontology concepts’’ for each document.

Use the DocOntWords to compute the frequency of ‘‘ontology concepts’’ in each document; store the frequency for each concept in an array called thefreuencyofExistTerm.

Step F: Re-rank the documents according to their frequency.

Use the array thefreuencyofExistTerm and give the highest rank one) for the highest frequency, and the second highest for the second highest rank (two), etc.

## End

## References

[1] D. Bianchini, V. De Antonellis, M. Melchiori, Capability matching and similarity reasoning in service discovery, CAiSE Int. Workshop on Enterprise Modeling and Ontologies for Interoperability, 2005285–296.

[2] L. Ding, T. Finin, A. Joshi, R. Pan, R. Cost, Y. Peng, et al., Swoogle: a search and metadata engine for the semantic web, in: Proceedings of the 13th ACM Conference Information and Knowledge Management, ACM Press, New York, USA, 2004, pp. 652–659.

[3] L. Ding, R. Pan, T. Finin, A. Joshi, Y. Peng, P. Kolari, Finding and ranking knowledge on the semantic web, in: Proceedings of the 4th International Semantic Web Conference, 2005, pp. 156–170.

[4] N. Guarino, G. Guizzardi, In defense of ontological foundations for conceptual modeling, Scandinavian Journal of Information Systems 18 (1), 2006, pp. 115– 126.

[5] M. Hepp, Possible ontologies: how reality constrains the development of relevant ontologies, IEEE Internet Computing 11 (1), 2007 Feb, pp. 90–96.

[6] A. Kayed, R. Colomb, Extracting ontological concepts for tendering conceptual structures, Data and Knowledge Engineering 40 (1), 2002, pp. 71–89.

[7] A. Kayed, N. Hirzallah, L. Al-Shalabi, M. Najjar, Building ontological relationships: a new approach, Journal of the American Society for Information Science and Technology, ISSN: 1532-2882, John Wiley & Sons Inc., pp. 1801–1809, 2008.

[8] F. Lachtim, A. Moura, M. Cavalcanti, Ontology matching for dynamic publication in semantic portals. Journal of the Brazilian Computer Society 15 (1). 20o9, pp. 27– 43, 0104-6500, Campinas March.

[9] A. Laender, B. Ribeiro-Neto, A. da Silva, J. Teixeira, A brief survey of web data extraction tools, SIGMOD Record 31 (2), 2002, pp. 84–93.

[10] A. Langville, C. Meyer, Deeper Inside PageRank, Internet Mathematics 2005, pp. 335–380.

[11] A. Mendelzon, Review – authoritative sources in a hyperlinked environment, ACM SIGMOD Digital Review 2, 2000

[12] D. Oberle, S. Staab, R. Studer, R. Volz, Supporting application development in the semantic web, ACM Transactions on Internet Technology (TOIT) 5 (May (2)), 2005, pp. 328–358.

[13] B. Sergey, P. Lawrence, R. Motwami, W. Terry, The pagerank citation ranking: bringing order to the web, in: Proceedings of the 14th International Conference on World Wide Web, ACM Press, New York USA, 2005 , pp. 567–574.

[14] A. Sheth, C. Ramakrishnan, Semantic (web) technology in action: ontology driven information systems for search, integration and analysis, IEEE Data Engineering Bulletin 26 (4), 2003, pp. 40–48.

[15] H. Uitermark, P. van Oosterom, N. Mars, M. Molenaar, Ontology-based integration of topographic data sets, International Journal of Applied Earth Observation and Geoinformation, Elsevier 7, 2005, pp. 97–106.

[16] Y. Zhang, W. Vasconcelos, D. Sleeman, Ontosearch: an ontology search engine, in: Proceedings of the 24th SGAI International Conference on Innovative techniques and Applications of Artificial Intelligence, IEEE Computer Society, Washington DC USA, 2004, pp. 256–259

![](/api/attachments/43BP7SVM/fulltext/images/0c4e6d2e6b9e070b9bdc7348378802214a84f879e5099cd69966bed788b4cb41.jpg)

Ahmad Kayed received his Ph.D. from University of Queensland, Australia, (2003) and Master degree from Jordan University, Jordan (1992). He has more than 20 years of experiences in education, research, industry, and business. After finishing his PhD he worked with Monash University, Australia then he joined ASU, Jordan. He is now working as Associate Professor, in the department of Computer Science, College of Computing, Fahad Bin Sultan University, KSA (Head of Computer Science Dept.). His research interests are in the fields of semantic web ontology, conceptual modelling, e-commerce and software engineering. He

has supervised many Ph.D. students and has also been a Committee member for reviewing many Ph.D. and M.sc. proposals in many institutes. He has worked as a consultant for many international companies. He has more than 20 publications and he has been a PC member for many international conferences. Ahmad Kayed is the founder of E-commerce Interest search group 2006, Arab Academic University. He has been awarded Best software, Ideal Accountant, Jordan, 1995/1996.

![](/api/attachments/43BP7SVM/fulltext/images/15d641e070f66e2920110e96711f985e1c5ced98070d19bfe144bbeb186c26de.jpg)

Eyas El-Qawasmeh received his B.Sc. degree in Computer Science in 1985 from Yarmouk University, Jordan. He then joined the Yarmouk University as teaching assistant in the Computer Science Department. In 1992, he joined the George Washington University, Washington, D.C., USA where he obtained his MS and Ph.D. degrees in Software and Systems in 1994 and 1997, respectively. In 2001, he joined George Washington University, USA as visiting researcher through a Fulbright Commission grant. In 2001, he won Hijjawi research prize for Computer Science. His areas of interest include Multimedia Databases, Information Retrieval, and Ob-

ject-Oriented. He has authored/co-authored over 70 research publications in peer reviewed reputed journals, and conference proceedings. In addition, he was a keynote speaker in many International events. He is the program chair and proceedings chair for many international conferences. In addition, he is the guest editor and a member of the editorial board of many journals. El-Qawasmeh is currently an associate professor at King Saud University, Saudi Arabia.

![](/api/attachments/43BP7SVM/fulltext/images/fc1027055380405eab2530b9480e5970b4ff414fc61943d940691b64c03f66ee.jpg)

Zakariya Qawaqneh received his M.Sc. from Jordan University of Science and Technology, Jordan in 2008. Currently, he is working as a lecturer in compute science department of Najran University KSA.
