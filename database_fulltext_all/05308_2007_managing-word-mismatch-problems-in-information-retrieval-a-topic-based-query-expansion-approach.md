---
otero_id: 5308
otero_key: "UC2FGYFP"
title: "Managing Word Mismatch Problems in Information Retrieval: A Topic-Based Query Expansion Approach"
authors: "Chih-Ping Wei; Paul Jen-Hwa Hu; Chia-Hung Tai; Chun-Neng Huang; Chin-Sheng Yang"
year: "2007"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222240309"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/UC2FGYFP/fulltext/images/e4f88f2f237598303baadf09e8c7c961bd6856dc85096912caae37e4aa65a577.jpg)

# Managing Word Mismatch Problems in Information Retrieval: A Topic-Based Query Expansion Approach

Chih-Ping Wei , Paul Jen-Hwa Hu , Chia-Hung Tai , Chun-Neng Huang & Chin-Sheng Yang

To cite this article: Chih-Ping Wei , Paul Jen-Hwa Hu , Chia-Hung Tai , Chun-Neng Huang & Chin-Sheng Yang (2007) Managing Word Mismatch Problems in Information Retrieval: A Topic-Based Query Expansion Approach, Journal of Management Information Systems, 24:3, 269-295

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222240309

![](/api/attachments/UC2FGYFP/fulltext/images/26f5b76f3a39e4ea26742cc585c7425c1437889b9c10232716ba344e87b74acc.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/UC2FGYFP/fulltext/images/fe8ac841a4936283015bd4bddd65141ae37e7052d3b95e0aa23f6fb2a5b80252.jpg)

Submit your article to this journal

Article views: 8

![](/api/attachments/UC2FGYFP/fulltext/images/cf2acbbea0d3f11d827efe23bbaf64ce5c3fd60a43581e4b5ba6cb2501ff97ca.jpg)

View related articles

# Managing Word Mismatch Problems in Information Retrieval: A Topic-Based Query Expansion Approach

CHIH-PING WEI, PAUL JEN-HWA HU, CHIA-HUNG TAI, CHUN-NENG HUANG, AND CHIN-SHENG YANG

CHIH-PING WEI is a Professor at the Institute of Technology Management at National Tsing Hua University in Taiwan. He received a B.S. in Management Science from the National Chiao-Tung University in Taiwan in 1987 and an M.S. and a Ph.D. in Management Information Systems from the University of Arizona in 1991 and 1996, respectively. Prior to joining the National Tsing Hua University in 2005, he was a faculty member of the Department of Information Management at the National Sun Yatsen University in Taiwan since 1996 and a visiting scholar at the University of Illinois at Urbana–Champaign in 2001 and the Chinese University of Hong Kong in summer 2006 and summer 2007. His papers have appeared in the Journal of Management Information Systems, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, IEEE Transactions on Systems, Man and Cybernetics, IEEE Transactions on Information Technology in Biomedicine, European Journal of Information Systems, Journal of Database Management, Information Processing and Management, and Journal of Organizational Computing and Electronic Commerce, among others. His current research interests include knowledge discovery and data mining, information retrieval and text mining, knowledge management, multidatabase management and integration, and data warehouse design. He has edited special issues of Decision Support Systems, International Journal of Electronic Commerce, and Electronic Commerce Research and Applications.

PAUL JEN-HWA HU is an Associate Professor and David Eccles Faculty Fellow at the David Eccles School of Business, University of Utah. He has a Ph.D. in Management Information Systems from the University of Arizona. His current research interests include information technology applications and management in health care, technology implementation management, electronic commerce, digital government, human–computer interactions, data/text mining, and knowledge management. Dr. Hu has published papers in the Journal of Management Information Systems, Decision Sciences, Communications of the ACM, Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, IEEE Transactions on Information Technology in Biomedicine, IEEE Transactions on Engineering Management, IEEE Intelligent Systems, IEEE Software, Journal of the American Society for Information Science and Technology, Social Science Computer Review, European Journal of Information Systems, Information and Management, Electronic Commerce Research and Applications, Journal of Computer-Assisted Learning, and Journal of Telemedicine and Telecare.

CHIA-HUNG TAI is a Research Assistant at the Institute of Information Science, Academia Sinica, in Taiwan. He received a B.S. in Management Science from the National

Chiao-Tung University in Taiwan in 2002 and an MBA in Information Management from the National Sun Yat-Sen University in Taiwan in 2004. His research interests include data mining, text mining, natural language processing, Chinese word segmentation, and Chinese semantic composition.

CHUN-NENG HUANG is a Project Manager Engineer of Asiatek Taiwan. He received a B.S. in Management Science from the National Chiao-Tung University in Taiwan in 2001 and an MBA in Management Information Systems from the National Sun Yat-sen University in 2003. His research interests include data mining and text mining.

CHIN-SHENG YANG is a Second Lieutenant in the Republic of China Army. He received a B.S. in Management Information Systems from the National Chengchi University in Taiwan in 2000 and an MBA and a Ph.D. in Management Information Systems from the National Sun Yat-sen University in Taiwan in 2002 and 2007, respectively. His papers have appeared or are forthcoming in the Journal of Management Information Systems, Decision Support Systems, and Information Processing and Management. His current research interests include text mining, information retrieval, and knowledge discovery and data mining.

ABSTRACT: Word mismatch represents a fundamental information retrieval challenge that has become increasingly important as electronic document repositories (e.g., Web resources, digital libraries) grow in number and sheer volume. In general, word mismatch refers to the phenomenon in which a concept is described by different terms in user queries and in source documents. Query expansion represents a promising avenue to address such problems. Previous research predominantly approaches query expansion on the basis of global or local analysis. However, these approaches emphasize a global perspective rather than taking a topic-specific view of term associations. As a consequence, their effectiveness can be severely constrained when the document corpus spans a diverse set of topics. In this study, we propose a topic-based approach for query expansion and develop and empirically evaluate two novel methods—namely, nonfuzzy and fuzzy topic-based query expansion—to address word mismatch problems. According to our evaluation results, the proposed topic-based approach is more effective than a benchmark global analysis method, particularly when user queries consist of multiple query terms.

KEY WORDS AND PHRASES: document clustering, fuzzy clustering, information retrieval, query expansion, text mining, topic-based query expansion, word mismatch.

ADVANCES IN INFORMATION AND NETWORK TECHNOLOGIES have fostered the creation of and convenient access to vast amounts of online information, often available in the form of text documents. Information retrieval (IR) systems therefore assume an increasingly important role in supporting information (document) searches by individuals and organizations alike. Typically, an IR system assesses the relevance of source documents in a repository to a user-provided query and selects a subset of documents relevant to the user’s interest or need [3, 19, 47]. Word mismatch, or the phenomenon in which people use different terms to describe the same concept, represents a fundamental challenge to IR. According to Furnas et al. [17], the probability that two people will use an identical term (or terms) to describe the same concept (or object) is less than 20 percent. For example, some people might use the term “data mining” to describe the process or techniques for extracting novel, valid, and actionable patterns from databases, whereas others may choose “knowledge discovery” or “data archeology” to refer to the same concept. When not properly addressed, word mismatch can significantly constrain the effectiveness of an IR system, particularly in situations in which user queries consist of relatively few terms [8, 11, 21, 55].

Word mismatch problems also prevail in search engine marketing (SEM), whose current practice predominantly depends on exact word matches. In general, firms bid for or purchase particular search words from popular search engines; their offerings or advertisements are included in the search results when a user’s query exactly matches some of their purchased search words.<sup>1</sup> According to the 2005 survey of SEM agencies and advertisers by the SEM Professional Organization (www.sempo.org), SEM in North America amounted to \$5.75 billion in 2005 and is expected to reach \$11.1 billion in 2010; many senior executives consider SEM a top business priority, particularly those with small or medium-sized firms. The use of exact word match in SEM represents a challenge to all stakeholders (including advertisers and users) because it requires each party effectively to anticipate different search words likely to be used by others. For example, an online analytical processing (OLAP) solution provider must identify all probable search words its prospect customers may use (e.g., OLAP, data warehouse, analytics, data mart, multidimensional data modeling, star schema, data cube, business intelligence, executive decision support, executive information systems [IS], etc.) and bid for or purchase all of them from a search engine. Generating a comprehensive list of search words is difficult; any deviations or omissions can lead to losses in leads or revenues. For instance, if a user query is highly related but not identical to any search words purchased by a firm, its offerings or advertisement will not appear in the search result.

Query expansion represents a promising avenue to address word mismatch problems because it expands a user query by incorporating additional terms relevant to the user-provided (original) query. The expanded query increases the likelihood that an IR system will retrieve documents of interest to the user. Query expansion can also mitigate the word mismatch challenge in SEM by expanding the search words purchased by a firm or submitted by the user. Continuing with our OLAP example, the firm bids on a search engine for the search word “OLAP,” which can automatically be expanded by incorporating all related terms, such as data warehouse, analytics, data mart, multidimensional data modeling, business intelligence, and executive decision support. Alternatively, the search engine can expand the user query by incorporating these related terms. In either case, the effectiveness of SEM likely improves.

Existing query expansion techniques can be broadly classified into two main approaches—global analysis and local analysis [2, 8, 9, 11, 55]. The global analysis approach is premised on an association hypothesis and thereby analyzes word co-occurrences among documents in the source corpus to estimate the weighted associations between terms (i.e., a statistical-based thesaurus), then generates a ranked list of terms that coincide with the query terms specified in the user-provided query, and finally expands the original query by incorporating the top-ranked terms from the list [13, 39, 45]. Instead of using a thesaurus constructed from the entire document corpus, the local analysis approach expands a user query by selecting relevant terms from the top-ranked documents (or passages) initially retrieved in response to a user-provided query.

A fundamental problem inherent to the global analysis approach is its use of a global thesaurus for query expansion. For each pair of terms, a global weight is derived from the entire document corpus. However, a repository often contains documents that pertain to a diverse set of topics (or domains). As a consequence, the global analysis-based approach can become ineffective because the weight (or strength) of two terms likely varies considerably depending on the underlying topics. Although the local analysis approach does not use the entire document corpus for query expansion, it essentially also takes a global perspective toward term associations. Typically, the local analysis approach derives the weight of an association between two terms from the top-ranked documents initially retrieved for a user-provided query. As with the global analysis, the effectiveness of the local analysis approach may also be limited when the top-ranked documents span different topics.

To address the word mismatch problem and the limitation inherent to the prevalent query expansion techniques, we propose a topic-based query expansion approach that extends global analysis by segmenting a document corpus into a set of document clusters (each corresponding to a particular topic) and then constructs a local thesaurus for each cluster. In a nutshell, our approach is anchored in global analysis, which shows greater robustness and computational efficiency in real-time IR environments than does the local analysis approach [18, 54, 55]. To determine the relevance of individual documents with respect to a user’s interest or need, we build a local thesaurus for each cluster and use the resulting thesauri to expand an original user query, which therefore includes multiple expanded queries. Our approach ranks the source documents in the repository with respect to each expanded query, aggregates the ranking of each document over all the expanded queries, and selects a set of documents presumably relevant to the original user query. Following this approach, we adopt fuzzy and nonfuzzy algorithms to develop two topic-based query expansion methods. We conduct an empirical evaluation to examine the effectiveness of the proposed methods, using a large set of abstracts of articles published in major IS journals. Our evaluation includes a prevalent global analysis method for performance benchmark purposes.

## Literature Review

WORD MISMATCH PROBLEMS CAN GREATLY IMPEDE the effectiveness of an IR system. Previous research has proposed and empirically examined different techniques for expanding a user query Q by incorporating additional terms considered relevant to those originally specified in Q. Depending on the particular information used to determine and select expanded terms for $Q ,$ these techniques can be classified broadly into two main approaches—global analysis and local analysis. Global analysis identifies and selects expanded terms for Q on the basis of all the documents in the source corpus, whereas local analysis extracts expanded terms from a subset of documents in the corpus presumably relevant to Q. The following subsections summarize important characteristics of each approach.

## Global Analysis

Global analysis employs a statistical-based thesaurus for query expansion and constructs the thesaurus on the basis of an association hypothesis, which assumes highly relevant terms likely co-occur in the same documents [24]. Given a user query Q, global analysis generates a ranked list of terms relevant to the user-provided query terms in Q, then expands Q by incorporating the top-ranked terms from the list. Term clustering, which represents one of the earliest global analysis techniques, groups similar terms into distinct clusters according to their co-occurrence in the source document corpus [45]. This technique expands a user query Q by incorporating all terms in the respective clusters that contain the query terms specified in Q.

Qui and Frei [39] propose a concept-based query expansion technique that uses a statistical-based thesaurus constructed from the entire source document corpus to select relevant terms for query expansion on the basis of their respective co-occurrence with the user-provided query terms. Specifically, terms relevant to or co-occurring with more query terms in the original user query are considered more appropriate for expansion than are those relevant to or co-occurring with fewer user-provided query terms. Prior evaluation results [39, 56] suggest the concept-based query expansion technique can improve retrieval effectiveness compared with a traditional, nonexpansion technique that uses only the original query terms.

Preferential term usage may be observed in situations in which highly similar or relevant terms do not frequently co-occur in the same documents in the corpus. For example, “color” and “colour” are highly relevant (i.e., identical) but may not always appear in the same documents. The effectiveness of a statistical-based thesaurus may be constrained in such situations, which diminishes the utilities of the expanded query or queries. In response, Gauch et al. [18] incorporate the context of terms to estimate their similarity, because two highly relevant terms likely share similar contextual (surrounding) terms, even though they seldom co-occur in the same documents. Accordingly, the similarity of two terms can be estimated on the basis of the similarity of their contextual terms in the source document corpus.

Prior studies [13, 55] also investigate latent semantic indexing (LSI) for query expansion. This technique assumes that an underlying latent semantic structure that exists in the document corpus can be partially obscured by the randomness of the term choice [13]. To estimate this latent structure, LSI derives a set of orthogonal LSI dimensions from the document corpus that jointly form a semantic space (i.e., LSI space). To capture important associative patterns in documents while avoiding insignificant variations that can result from idiosyncratic term usage between or among individual documents, LSI reduces the original semantic space by retaining only the most important LSI dimensions. Each document in the source corpus is then mapped onto the LSI space and represented as a document-dimension vector rather than a document-term vector. Similarly, a user query is regarded as a pseudo-document and thus also represented as a document-dimension vector, which enables an estimation of the relevance of individual documents in relation to the user-provided query in the same LSI space. Through dimension transformation and reduction, LSI implicitly performs query expansion on the basis of the entire document corpus and thus has the potential to address the word mismatch problem. However, its effectiveness remains inconclusive, lacking convincing empirical evidence that demonstrates its superiority over standard vector space retrieval systems [55].

Although existing query expansion techniques that use global analysis differ in how they estimate or derive term associations, they share one commonality: they take a global perspective when estimating the similarity between terms. That is, they derive a global weight for each pair of terms from the entire source document corpus, which often spans different topics (or domains). Imaginably, a collection of documents about IS may contain multiple distinct topics, such as databases, artificial intelligence, computer networks, and programming languages. As a result, the global analysis approach may not be effective for query expansion because the weight or strength between terms may vary considerably according to the underlying topics [18, 34]. For example, the terms “object oriented” and “database schema” may be highly related in databases but share little relevance in programming languages. From a topic perspective, the inclusion of “database schema” in an expanded query is appropriate when the user queries “object oriented” for documents pertaining to databases. However, “database schema” should not be considered for query expansion when the user is searching for documents about programming languages. The global analysis approach does not take into account the described topic-based perspective and therefore likely expands a user query using terms that are general or compromised across different topics rather than those specific to the user’s interest or need. Consequently, the effectiveness of the global analysis approach is likely to deteriorate.

## Local Analysis

Local analysis first retrieves documents relevant to a user-provided query and employs them as a basis for selecting additional terms to incorporate into the original query. Selection of documents relevant to a user query can be performed manually or automatically. The manual approach usually employs a relevance feedback mechanism to identify particular documents relevant to the original user query [42, 44]; for example, the user is presented with a list of documents retrieved in response to his or her query and identifies those he or she considers relevant. The automatic approach instead selects relevant documents from the source repository by assuming the topranked documents (or passages) initially retrieved for the original user query provide an appropriate basis for the automated creation of a local thesaurus [2, 25, 54]. Attar and Fraenkel [2] cluster the individual terms appearing in the top-ranked documents and consider the terms in each resulting cluster quasi-synonyms. To expand a user query, each term specified in the original user query incorporates its quasi-synonyms in the corresponding cluster. Xu and Croft [54] develop a local feedback method that expands the original user query with the most frequent terms and phrases (i.e., pairs of adjacent, nonstop words) that appear in the top-ranked documents. The weight between the respective terms in the expanded query then is readjusted using the Rocchio formula.

Instead of expanding a user query by incorporating relevant terms in the query, Khan and Khor [25] consider each expanded term a separate query and submit it to retrieve relevant documents. Their rationale is to ensure the retrieval of the most relevant documents that may satisfy different aspects of the user’s needs. Xu and Croft [55] propose a local context analysis technique similar to the concept-based query expansion technique by Qui and Frei [39]. Specifically, terms that co-occur with more query terms specified in a user-provided query are considered more relevant to that query and therefore incorporated for query expansion, rather than those that co-occur with fewer user-specified query terms.

However, the proportion of truly relevant documents in the top-ranked document set influences the effectiveness of the local analysis approach. The effectiveness of the expanded query depends greatly on the term associations extracted from the topranked documents and diminishes substantially when many top-ranked documents are, in effect, not relevant to the user’s need [11, 21, 36, 54, 55]. Effectiveness can deteriorate further when the retrieved top-ranked documents span different topics. In this case, the specific terms selected from the documents for query expansion purposes likely are general across various topics, which makes the resulting expanded query ineffective for retrieving documents relevant to the user. Another important limitation of local analysis is that its derivation of term associations cannot be precomputed, because the top-ranked document set can be obtained only after the user submits a query [18]. This overhead can be computationally demanding, which makes the local analysis approach less appealing in online IR environments characterized by voluminous repositories and stringent response time requirements.

## A Topic-Based Approach for Query Expansion

TO ADDRESS THE LIMITATIONS INHERENT TO THE EXISTING query expansion techniques built from the global thesaurus perspective (i.e., constructed using the entire document corpus or the top-ranked documents), we take a topic-specific view to thesaurus construction and propose a topic-based approach for query expansion that consists of topic-based thesaurus construction and document retrieval phases (as shown in Figure 1). In the topic-based thesaurus construction phase, a set of local thesauri, each of which pertains to a particular topic, emerges from the collection of source documents $D _ { _ { T C } }$ in the repository. In the subsequent document retrieval phase, a user query Q is expanded into multiple expanded queries on the basis of these local thesauri. The expanded queries are then submitted to retrieve, from the source document corpus $D _ { { _ R } }$ a subset of documents relevant to the query $Q .$ . It is worth noting that $D _ { _ { T C } }$ and $D _ { { _ R } }$ can refer to the same document corpus or different corpora, which does not affect the design of our query expansion approach.

![](/api/attachments/UC2FGYFP/fulltext/images/cc7d760333231bdfd5b21967bdb26b7cac36f4ba90641dcb5ca8d9c27a6cf24a.jpg)  
Figure 1. Proposed Topic-Based Query Expansion Approach

## Topic-Based Thesaurus Construction

As Figure 1 depicts, document clustering and local thesaurus creation both occur during the topic-based thesaurus construction phase. Document clustering automatically organizes a large collection of documents into multiple clusters (or groups), each of which discerns a particular topic within the source document corpus and contains (similar) documents about that topic [26, 27, 38, 50, 52]. The documents in each resulting cluster share maximal similarity and are substantially different from documents in other clusters. Although the document clusters generated in the topic-based thesaurus construction phase may not reveal the genuine topics in the source document corpus precisely, the documents in a cluster tend to be highly similar in content and collectively pertain to a particular topic.

Document clustering generally involves several tasks, including feature extraction, feature selection, document representation, and clustering [22, 50, 51, 52]. In feature extraction, a set of features (typically nouns and noun phrases) is extracted from the source documents $D _ { _ { T C } }$ . We use a rule-based part-of-speech tagger [6, 7] to tag syntactically the terms that appear in each document in $D _ { _ { T C } }$ . We follow the approach proposed by Voutilainen [49] and implement a noun-phrase parser for identifying and extracting noun phrases from each syntactically tagged document. The subsequent feature selection reduces the size of the extracted feature set and attempts to suppress potential biases in the original (noncondensed) feature set [14, 43]. Common metrics for feature selection include term frequency (TF),<sup>2</sup> TF×IDF,<sup>3</sup> and their hybrids [4, 5, 32, 40, 50, 52]. In this study, we adopt TF×IDF, a feature selection scheme commonly used by prior research. Specifically, we select k features that have the highest TF×IDF scores as the feature set for $D _ { \scriptscriptstyle { T C } } .$

In document representation, each document in $D _ { _ { T C } }$ is represented using the selected feature set. A review of prior research suggests the prevalent use of binary (i.e., presence versus absence of a feature in a document), within-document TF, and TF×IDF representation methods [4, 32, 43, 53]. We choose the TF×IDF method to represent all documents in $D _ { \scriptscriptstyle { T C } } .$ . Specifically, each document $d _ { i }$ is represented as a documentfeature vector:

$$
\vec {d} _ {i} = <   r _ {i 1}, r _ {i 2}, \dots , r _ {i k} >,
$$

where r is the TF×IDF value of feature $r _ { i j }$ $f _ { _ j }$ in document $d _ { \phantom { \dagger } _ { i } }$

The resulting document-feature vectors serve as input to the subsequent clustering task, which can be classified dichotomously on the basis of whether a document may be included in multiple clusters simultaneously. We adopt and empirically evaluate nonfuzzy and fuzzy clustering algorithms for the target document clustering task. In general, a nonfuzzy algorithm segments a set of documents into multiple, mutually exclusive (i.e., nonoverlapping) clusters, whereas a fuzzy clustering algorithm allows a document to appear in multiple clusters simultaneously. Common nonfuzzy clustering can be supported by partitioning-based [5, 12, 32], hierarchical [16, 43, 48], and Kohonen neural network [20, 31, 33, 43] algorithms. A partitioning-based algorithm (such as k-means [1]) segments a set of documents into multiple, mutually exclusive clusters, whereas a hierarchical algorithm constructs a binary clustering hierarchy whose leaf nodes represent target data objects, such as individual documents. The Kohonen neural network algorithm (also known as a self-organizing map) uses an unsupervised two-layer neural network for clustering [28, 29]. In this study, we choose the partitioning-based k-means algorithm to implement the nonfuzzy document clustering method, primarily because of its computational efficiency and clustering effectiveness, which is highly comparable to that attainable by the computationally demanding hierarchical [46] and Kohonen neural network [20] algorithms. In our implementation of the k-means algorithm, we measure the distance between $d _ { i }$ and the centroid $\nu _ { c j }$ of cluster $C _ { j } ,$ as follows:

$$
d i s t \left(\vec {d} _ {i}, \vec {v} _ {c j}\right) = \frac {1}{\cos \left(\vec {d} _ {i} , \vec {v} _ {c j}\right)} - 1,\tag{1}
$$

where

$$
c o s \left(\vec {d} _ {i}, \vec {v} _ {c j}\right) = \frac {\vec {d} _ {i} \cdot \vec {v} _ {c j}}{\left| \vec {d} _ {i} \right| \times \left| \vec {v} _ {c j} \right|}
$$

denotes the cosine similarity of $\vec { d } _ { i }$ and $\vec { \nu } _ { _ { c j } }$

After performing the nonfuzzy clustering of the document corpus $D _ { \scriptscriptstyle { T C } } ,$ we create a local thesaurus for each document cluster. To avoid generating unreliable thesauri from smaller clusters, we combine clusters that contain fewer than a prespecified number of documents (i.e., β) into an aggregate cluster and then construct a single local thesaurus for the aggregate cluster. A (local) thesaurus consists of a set of term associations, each of which is represented by an undirected weighted link between a pair of terms. To create a local thesaurus for a cluster $C _ { j } ,$ we exclude terms that appear in $C _ { j }$ less frequently than a specified minimum frequency threshold $\delta _ { D F }$ and represent each remaining term $f _ { t }$ (occurrence frequency equal to or exceeding $\delta _ { D F } )$ using the following term-document vector:

$$
\vec {f} _ {t} = \left(w _ {t 1}, w _ {t 2},..., w _ {t | C _ {j} |}\right),
$$

where $| C _ { j } |$ denotes the number of documents in $C _ { j }$ and $w _ { t i }$ represents the weight (TF×IDF metric) of term $f _ { t }$ in document $d _ { i }$

We use the cosine similarity measure to estimate the similarity between two terms, represented by their respective term-document vectors, and thereby obtain a local thesaurus that consists of a set of undirected term associations for each cluster $C _ { j } .$ Specifically, the similarity between terms $f _ { t }$ and $f _ { s }$ in cluster $C _ { j }$ is defined as

$$
\text { Similarity } \left(f _ {t}, f _ {s}\right) = \frac {\vec {f} _ {t} \cdot \vec {f} _ {s}}{\left| \vec {f} _ {t} \right| \times \left| \vec {f} _ {s} \right|} = \frac {\sum_ {\forall d _ {i} \in C _ {j}} w _ {t i} \times w _ {s i}}{\sqrt {\sum_ {\forall d _ {i} \in C _ {j}} \left(w _ {t i}\right) ^ {2}} \sqrt {\sum_ {\forall d _ {i} \in C _ {j}} \left(w _ {s i}\right) ^ {2}}}.\tag{2}
$$

Because nonfuzzy clustering algorithms partition a set of source documents into multiple, mutually exclusive clusters, they may become inappropriate in scenarios in which a source document describes or pertains to multiple topics simultaneously. Therefore, when performing target document clustering in the topic-based thesaurus construction phase, we also develop a fuzzy clustering method that allows for document overlaps across different clusters. Specifically, we adopt the fuzzy c-means (FCM) algorithm [15], which is computationally efficient and commonly used in previous research [30, 35]. Similarly to nonfuzzy clustering, we measure the distance between a source document and a cluster’s centroid using formula (1). In the following, we provide a brief review of the FCM algorithm.

Let $X \equiv [ x _ { 1 } , x _ { 2 } , . . . , x _ { { \scriptscriptstyle N } } ]$ be an $N \times k$ matrix, where N represents the number of documents and $x _ { i }$ denotes the feature vector of ith data object (e.g., document) using a dimensionality of k. Let υ be the universe of all possible partitions of X and c represent the number of clusters to be generated, where $1 < c < N . \mathrm { A }$ partition $U \equiv [ u _ { \mathrm { a } } ] \in$ υ, the membership matrix, is a $c \times N$ matrix. Each $u _ { \alpha , i }$ in U describes the degree of membership (more specifically, probability) of data object i belonging to cluster ${ \mathfrak { a } } ,$ which satisfies the following three conditions:

$$
u _ {\alpha , i} \in [ 0, 1 ], \forall \alpha = 1, \dots , c \text { and } \forall i = 1, \dots , N
$$

$$
\sum_ {\alpha = 1} ^ {c} u _ {\alpha , i} = 1, \forall i = 1, \dots , N
$$

and

$$
0 <   \sum_ {i = 1} ^ {N} u _ {\alpha , i} <   N, \forall \alpha = 1, \dots , c.
$$

Let $V \equiv [ \nu _ { _ 1 } , \nu _ { _ 2 } , . . . , \nu _ { _ c } ]$ be a $\mathbf { \xi } _ { ! c \times k }$ matrix that represents the centroids of the respective clusters and ||⋅|| be a distance function. The goal of FCM is to minimize an objective function $J _ { { } _ { m } } ,$ the weighted sum of squared errors, as follows:

$$
J _ {m} (U, V) = \sum_ {i = 1} ^ {N} \sum_ {\alpha = 1} ^ {c} u _ {\alpha , i} ^ {m} \left\| x _ {i} - v _ {\alpha} \right\| ^ {2},
$$

where $x _ { i }$ is the feature vector of the ith data object $( \mathrm { e . g . }$ , document) of $X , \nu _ { \mathrm { a } }$ is the centroid of the αth cluster, $u _ { \alpha , i }$ is the degree of membership of $x _ { i }$ in the cluster α, and $m$ (where $m > 1 )$ is the fuzzifier.

The FCM algorithm proceeds as follows: In the initialization step, FCM specifies the number of clusters $^ { c , }$ the termination criterion $\varepsilon > 0 ,$ , and the value for the fuzzifier $m ,$ then initializes the centroid matrix $V ^ { ( 0 ) }$ accordingly. The partition matrix $U ^ { ( t ) }$ and the centroids of the respective clusters are then calculated as follows:

$$
v _ {\alpha} ^ {(t)} = \frac {\sum_ {i = 1} ^ {N} \left(u _ {\alpha i} ^ {(t - 1)}\right) ^ {m} \cdot x _ {i}}{\sum_ {i = 1} ^ {N} \left(u _ {\alpha i} ^ {(t - 1)}\right) ^ {m}}, \alpha = 1, 2,..., c
$$

$$
u _ {\alpha i} ^ {(t)} = \frac {1}{\sum_ {j = 1} ^ {c} \left(\frac {\left\| x _ {i} - v _ {\alpha} ^ {t} \right\|}{\left\| x _ {i} - v _ {j} ^ {(t)} \right\|}\right) ^ {2 / (m - 1)}}, \begin{array}{l} \alpha = 1, 2,..., c \\ i = 1, 2,... N. \end{array}
$$

The calculation process stops when the termination criterion is satisfied $( \mathrm { i . e . }$ $\| U ^ { ( t + 1 ) } - U ^ { ( t ) } \| < \varepsilon )$ but otherwise continues with partition matrix and centroid calculations. The output produced by FCM is the degree of membership matrix U. To create a local thesaurus, we do not use the degree of membership $u _ { \alpha , i }$ directly to represent the association between a document $d _ { i }$ and a cluster ${ \mathfrak { a } } .$ because the membership value in FCM does not denote the similarity between a document and a cluster. Rather, the degree of membership conveys the probability that a document belongs to a particular cluster, compared with the probabilities that it belongs to other clusters. We use a threshold $\ 8 _ { { t } }$ for defuzzification, which determines whether a document belongs to a particular cluster; thus, a document belongs to a cluster if its membership value exceeds $\delta _ { _ t }$ A document that has multiple membership values exceeding $\ 8 _ { { t } }$ gets assigned to multiple clusters simultaneously, but when it has no membership values greater than $\delta _ { { } _ { t } ; { } }$ , the document is assigned to the cluster for which it has the highest membership value. According to our preliminary experiment results, setting $\ 8 _ { { t } }$ to 1.5/c seems appropriate, where c represents the number of clusters. Thus, we obtain a set of clusters whose documents can overlap and belong to multiple clusters simultaneously. We then apply the same procedure used in the nonfuzzy clustering method to create a local thesaurus for each cluster.

## Document Retrieval

In the document retrieval phase, we use the local thesauri created in the topic-based thesaurus construction phase to expand a user query $Q$ by performing local query expansion and document selection. In local query expansion, we assign a weight of 1 to each term specified in the original user query. When $Q$ consists of a single query term $( q t )$ , the weight of a term $t _ { \scriptscriptstyle j }$ that expands from a local thesaurus equals the similarity strength between $t _ { j }$ and $q t .$ . However, if $Q$ contains multiple query terms $( q t _ { 1 } , q t _ { 2 } , . . . , q t _ { i } )$ the weight of a term $t _ { j }$ that expands from a local thesaurus is the averaged similarity strength between $t _ { j }$ and each ${ { q t } _ { i } }$ in the original user query. Conceptually, our weighting scheme resembles that used by the concept-based query expansion technique [39], as well as the local context analysis technique by Xu and Croft [55]. Specifically, our scheme uses average similarity, which arguably is more appropriate than other schemes (e.g., maximal similarity) because it favors expanded terms that co-occur with more terms in the original user query to those that co-occur with fewer terms.

In each cluster, we rank the terms expanded from the corresponding local thesaurus in accordance with their weights with respect to the original query $Q .$ . When multiple terms have the same weight, we prioritize them on the basis of their occurrence frequency in the documents in the cluster from which we constructed the local thesaurus. The top-ranked n terms are then selected to expand the user query $Q$ in each cluster. As a result, the original query $Q$ is transformed into multiple, locally expanded queries $L Q _ { 1 } , L Q _ { 2 } , . . . , L Q _  \it$ , where $c$ denotes the number of clusters generated in the topicbased thesaurus construction phase. Semantically, the original query is represented by a disjunction that consists of multiple locally expanded queries: $L Q _ { 1 } \lor L Q _ { 2 } \lor \dots \lor$ $L Q _ { c }$ . Each locally expanded query $L Q _ { h }$ is represented by a term vector $\vec { L Q } _ { h } = < w ( q t _ { 1 } ) .$ $w ( q t _ { 2 } ) , . . . , w ( q t _ { p } ) >$ , where $w ( q t _ { j } )$ is the weight of query term ${ { q t } _ { i } }$ (original or expanded) in cluster $C _ { j } ,$ , and $p$ is the sum of the number of expanded terms n and the number of query terms in the original query $Q .$

To retrieve relevant documents in $D _ { _ R }$ for the original query $Q ,$ we use the cosine similarity to assess the degree to which a document is relevant to each locally expanded query $L Q _ { h }$ . For each document $d _ { i }$ in $D _ { R } ,$ we aggregate its degrees of relevance over all locally expanded queries, using the maximum cosine similarity of $d _ { i }$ among all locally expanded queries, to signify the degree of relevance between $d _ { i }$ and $Q .$ . Ultimately, we select and retrieve the top-ranked documents for the user. We choose maximum similarity rather than average similarity, largely because of intrinsically disjunctive nature of the locally expanded queries. That is, if $d _ { \phantom { i } _ { i } }$ is highly related to a locally expanded query, $d _ { i }$ should be highly related to $Q ,$ regardless of the relevance of $d _ { \ast }$ with respect to other locally expanded queries. Maximum similarity is more capable of depicting this disjunctive nature across all locally expanded queries, whereas average similarity is more consistent with the conjunction of locally expanded queries, because it mitigates the significance of those documents that show strong dominance in some locally expanded queries.

## Evaluation Design

IN THIS SECTION, WE DETAIL OUR EVALUATION DESIGN, including the document collections $D _ { _ { T C } }$ and $D _ { _ R }$ for thesaurus construction and document retrieval, evaluation criteria, “gold standard” retrievals, and the performance benchmark we use.

## Source Documents for Thesaurus Construction and

## Document Retrieval

The document collection $D _ { _ { T C } }$ used in the thesaurus construction phase includes abstracts of 5,215 articles published in 17 leading IS journals [37, 41] between January 1999 and December 2003.<sup>4</sup> To establish a document corpus $D _ { { _ R } }$ to evaluate the proposed topic-based query expansion methods (i.e., fuzzy and nonfuzzy), we selected abstracts of 386 articles that appeared in Decision Support Systems, Information Systems Research, Journal of Management Information Systems, and MIS Quarterly between January 1999 and March 2003. Table 1 summarizes the document corpus $D _ { { _ R } }$ used in our evaluation.

## Evaluation Criteria and Gold Standard Retrievals

We examine and compare the effectiveness of each topic-based query expansion method in terms of recall and precision rates. Assume that T is the set of documents truly relevant to a user query $Q .$ The recall rate then is the portion of documents in T that are correctly retrieved by an investigated query expansion method, whereas the precision rate is the portion of documents retrieved by that method that are actually in T. In our evaluation, we assess the effectiveness of each investigated method using both average recall and average precision rates across all user queries included in the evaluation study.

We establish a gold standard set of documents (subset of $D _ { \scriptscriptstyle R } )$ that are truly relevant to each user query in our evaluation. We follow a consensus-based strategy to create the gold standard document sets for each query, which we then use to assess the recall and precision rates of the respective methods. Prior studies show that most user queries submitted to Web-based systems consist of one or two query terms [10, 23]. Casual observations in an academic (educational) setting concur with this finding; many user queries consist of one or two query terms. Examples of single-term queries include “electronic commerce” or “data mining.” A typical two-term user query includes one term that specifies the particular subject area of interest and another that describes the target application or context, such as “data management” in “health care” or “ontology” for “knowledge management.” Hence, our evaluation study concentrates on user queries that consist of one or two query terms.

Table 1. Summary of Document Corpus DR

<table><tr><td>Journal</td><td>Number of documents</td><td>Average number of words per document</td><td>Average number of nouns and noun phrases per document</td></tr><tr><td>Decision Support Systems</td><td>163</td><td>138</td><td>50</td></tr><tr><td>Information Systems Research</td><td>56</td><td>177</td><td>54</td></tr><tr><td>Journal of Management Information Systems</td><td>104</td><td>178</td><td>54</td></tr><tr><td>MIS Quarterly</td><td>43</td><td>182</td><td>51</td></tr><tr><td>Total/average</td><td>386</td><td>169</td><td>52</td></tr></table>

To create a query pool appropriate for the target document corpus $D _ { R } ,$ we first listed all of the key words specified by the author(s) of each article in $D _ { R } - \mathrm { a }$ total of 1,359 key words from 386 abstracts—and removed those whose occurrence frequency in the documents in $D _ { { _ R } }$ is less than three. Each of the 341 discovered key words became a candidate for a one-term user query. We used the selected one-term query candidates to enumerate all possible (candidate) two-term queries and again removed those with an occurrence frequency of less than three, which results in a total of 1,178 two-term user queries. Two experienced IS researchers from different universities reviewed the one- and two-term user query candidates individually to identify those that were meaningful and common to IS research. The agreement between the researchers was 0.90 for one-term queries and 0.94 for two-term queries. We used the candidate queries identified by both researchers to create a query pool for the subsequent evaluation study.

We formed three panels, each with three doctoral students in management information systems who had similar research interests, to identify the gold standard documents for each user query. In each panel, the members individually and explicitly specified their self-assessed familiarity with every query candidate on a five-point Likert scale, with 5 being “highly familiar” and 1 being “not familiar at all.” Using their responses, we refined the query pool for each panel by retaining only those that received a minimum score of three from all the members in the panel. We then randomly selected 12 queries for each panel, six one-term queries and six two-term queries, without repetitions (i.e., no queries were assigned to multiple panels).

For each query assigned to a panel, its members individually reviewed all of the documents in $D _ { { _ R } }$ (i.e., 386 abstracts) to identify those they considered relevant. All of the members of a panel then met to discuss and reconcile any disagreements or discrepancies in their individual assessments. On average, a panel member took 10 hours to complete his or her individual assessments and spent an additional three hours for the panel review and discussion. We include documents identified as relevant to a query on a consensus basis in the gold standard retrievals for that query. The average within-panel agreement about whether a document was relevant to the query (between any two panel members) was approximately 0.33 before the panel discussion; furthermore, the agreement between documents identified as relevant by an individual panel member before the panel discussion and those considered relevant by a panel consensus averaged 0.54. The observed consistency seems reasonable and might have been constrained by the difference in individual panel members’ interpretations of the intent or scope of a query. For example, one panel member considered e-government articles irrelevant to the user query “e-commerce,” whereas the others perceived them as important. In this particular case, the panel members reconciled their assessments through discussion and eventually agreed that e-government articles with a clear emphasis on e-procurement should be relevant to the “e-commerce” query. We thereby obtained the gold standard retrievals for each of the 36 user queries included in our evaluation. These retrievals average 13.24 documents per user query.

## Performance Benchmark

For benchmark purposes, our evaluation includes a prevalent query expansion method that uses global analysis. We constructed a global thesaurus on the basis of all the documents collected for thesaurus construction $D _ { _ { T C } }$ (i.e., 5,215 abstracts), following the same procedure for creating a local thesaurus that we described previously. The benchmark method uses a document retrieval mechanism similar to that of the proposed topic-based query expansion methods.

## Evaluation Results and Discussions

## Parameter Tuning

THE GLOBAL ANALYSIS METHOD REQUIRES two parameters, $\delta _ { D F }$ and n, which denote a minimum occurrence frequency threshold in the source documents during the global thesaurus construction and the number of expanded terms, respectively. The proposed nonfuzzy topic-based method involves five parameters: β (i.e., the minimum cluster size threshold), $\delta _ { { D F } }$ (i.e., the minimum occurrence frequency threshold in each cluster’s documents), k (i.e., the number of features considered in document clustering), c (i.e., the number of clusters), and n (i.e., the number of expanded terms in each cluster). The proposed fuzzy method also requires one additional parameter, m, which denotes the degree of the fuzzifier used by the FCM algorithm. We conduct a series of parameter-tuning experiments for each respective method, in which we examine $\delta _ { D F }$ at three levels (i.e., 1, 2, and 3) and evaluate n over the range of 10–40 in increments of 10. For the proposed topic-based methods, we assess β over the range of 50–200 (in increments of 50), k from 1,100 to 1,700 (in increments of 200), and c between 5 and

![](/api/attachments/UC2FGYFP/fulltext/images/7d9afd4c68d6bfa11e20f80e2699472db3830fa7ef21d39ce0687b801d4a4a2c.jpg)  
(a) Nonfuzzy Topic-Based Query Expansion Method

![](/api/attachments/UC2FGYFP/fulltext/images/cba71572c2e715a8370e8eb467c3046333b0bfd309b4dcb07ad7b83d12348621.jpg)  
(b) Fuzzy Topic-Based Query Expansion Method  
Figure 2. Effect of Number of Clusters (c)

25 (in increments of 5). In addition, we investigate the effect of m in the proposed fuzzy method over the range of 1.1–1.9 (in increments of 0.1).

According to our experimental results, the effects of $\delta _ { D F }$ and n appear stable over the range investigated. For the global analysis method, we therefore select 3 for $\delta _ { D F }$ and set n to 30. On the basis of our performance-tuning analyses, we set β to $1 0 0 , \delta _ { { \scriptscriptstyle D F } }$ to 2, k to 1,300, c to 10, and n to 30 for the nonfuzzy query expansion method; for the fuzzy method, we select 100 for β, 3 for $\delta _ { D F } ,$ 1,300 for k, 1.5 for $m ,$ 15 for $^ { c , }$ and 30 for n. Due to space limitations, we only illustrate the influence of c on the effectiveness of the fuzzy and nonfuzzy methods. As Figure 2(a) shows, the effectiveness of the nonfuzzy method increases when c reaches 10 compared with the other values in the range we investigated. On the contrary, the fuzzy method generally records the highest effectiveness in the investigated range when the number of clusters reaches 15, as shown in Figure 2(b). Table 2 summarizes the parameter values we select for each method and use in the subsequent evaluation study.

Table 2. Summary of Parameter Values Used by Respective Techniques

<table><tr><td>Query expansion technique</td><td>Parameter</td><td>Value</td></tr><tr><td rowspan="2">Global analysis method</td><td> $\delta_{DF}$  (document frequency threshold)</td><td>3</td></tr><tr><td>n (number of expanded terms)</td><td>30</td></tr><tr><td rowspan="5">Nonfuzzy method</td><td>β (minimum cluster size)</td><td>100</td></tr><tr><td> $\delta_{DF}$  (document frequency threshold for each cluster)</td><td>2</td></tr><tr><td>k (number of features for document clustering)</td><td>1,300</td></tr><tr><td>c (number of clusters)</td><td>10</td></tr><tr><td>n (number of expanded terms within each cluster)</td><td>30</td></tr><tr><td rowspan="6">Fuzzy method</td><td>β (minimum cluster size)</td><td>100</td></tr><tr><td> $\delta_{DF}$  (document frequency threshold for each cluster)</td><td>3</td></tr><tr><td>k (number of features for document clustering)</td><td>1,300</td></tr><tr><td>m (degree of fuzzifier used by fuzzy c-means)</td><td>1.5</td></tr><tr><td>c (number of clusters)</td><td>15</td></tr><tr><td>n (number of expanded terms within each cluster)</td><td>30</td></tr></table>

## Comparative Evaluation of Investigated Methods

We assess the effectiveness of each investigated method using recall and precision rates. Specifically, the effectiveness of each method is measured by 10 pairs of recall and precision rates we observe with the r top-ranked documents over the range from 5 to 50, in increments of 5. As shown in Figure 3, the nonfuzzy method generally outperforms the global analysis method over the investigated range of r. At each investigated level of $r ,$ the effectiveness of the fuzzy method appears greater than that achieved by the global analysis method. When r equals 5 (i.e., uppermost left point of each performance curve in Figure 3), the nonfuzzy method seems more effective than does the fuzzy method, as manifested by its higher precision and recall rates. As r increases beyond 5, the fuzzy method starts outperforming the nonfuzzy method. Overall, our empirical results suggest that, among all the investigated methods, the fuzzy topic-based query expansion method arguably is the most effective, whereas the benchmark global analysis method appears least effective.

Because of the intrinsic trade-off between recall and precision rates, we also assess the effectiveness of the respective methods using the F1 measure.<sup>5</sup> Across the range of top-ranked documents retrieved (i.e., r), both fuzzy and nonfuzzy methods result in higher F1 values than does the benchmark global analysis method, and the fuzzy method in general has higher F1 values than the nonfuzzy method (see Table 3). Overall, our analysis shows the superiority of our proposed methods (i.e., fuzzy and nonfuzzy) over the benchmark method for expanding user queries across different numbers of top-ranked documents retrieved.

![](/api/attachments/UC2FGYFP/fulltext/images/46ed87de8b7583e2cd7739d1d8fd036797dbe9ffe5882e1e8c3c0677d3b4e8fe.jpg)  
Figure 3. Performance of Topic-Based Query Expansion and Benchmark Methods

User queries often differ in the number of terms included in the query, which necessitates further analysis of our evaluation results on the basis of the exact number of query terms. As we illustrate in Figure 4, the effectiveness of the respective methods, as measured by recall and precision rates, varies with the exact number of terms in the user query. For queries consisting of only one query term, the global analysis method seems to outperform both proposed methods when r is less than 20, but the fuzzy method appears more effective than the global analysis method when r exceeds 20. Among the three methods we investigate, the nonfuzzy method seems least effective for expanding user queries that consist of only one query term. However, across the range of r investigated, both fuzzy and nonfuzzy methods noticeably outperform the global analysis method for user queries that have two query terms. When r is less than 25, the nonfuzzy method outperforms the fuzzy method, which, however, in general appears more effective than the nonfuzzy method when r increases beyond 25. The performance differentials observed between the two topic-based query expansion methods seem marginal over the range of r values studied.

We also use the F1 measure to evaluate each investigated method for expanding user queries that vary in the number of query terms. For single-term queries, the proposed methods (i.e., fuzzy and nonfuzzy) generally have higher F1 values than the global analysis method when r exceeds 20 (see Table 4). According to our comparative analysis, the F1 value of the fuzzy method is consistently higher than that associated with the nonfuzzy method across the range of r we examine. Both topic-based methods exhibit higher F1 values than the global analysis method when expanding user queries that consist of two query terms. In addition, the F1 value of the fuzzy method becomes relatively higher than that of the nonfuzzy method when r increases beyond 10.

<sub>s</sub> <sub>of</sub> <sub>F1</sub> M<sup>easure</sup> <sup>for</sup> <sup>Topic-Based</sup> <sup>Query</sup> <sup>Expansion</sup> <sup>and</sup> <sup>Bench</sup>

<table><tr><td rowspan="2"></td><td colspan="10">r (number of top-ranked documents)</td></tr><tr><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td><td>30</td><td>35</td><td>40</td><td>45</td><td>50</td></tr><tr><td>Global analysis</td><td>0.3196</td><td>0.3681</td><td>0.3606</td><td>0.3393</td><td>0.3036</td><td>0.2878</td><td>0.2757</td><td>0.2646</td><td>0.2530</td><td>0.2424</td></tr><tr><td>Fuzzy topic based</td><td>0.3585</td><td>0.3925</td><td>0.3775</td><td>0.3562</td><td>0.3376</td><td>0.3199</td><td>0.3136</td><td>0.2955</td><td>0.2750</td><td>0.2614</td></tr><tr><td>Nonfuzzy topic based</td><td>0.3712</td><td>0.3923</td><td>0.3631</td><td>0.3398</td><td>0.3213</td><td>0.3072</td><td>0.2951</td><td>0.2815</td><td>0.2697</td><td>0.2546</td></tr></table>

![](/api/attachments/UC2FGYFP/fulltext/images/3f713b3fcfc2261ae5b2c8359935a8a015223555170714cb7af9f8b02d763d5f.jpg)  
(a) Number of Query Terms = 1

![](/api/attachments/UC2FGYFP/fulltext/images/21807bec2bda48ec3aa771db6b2dae17f263518f1a851e239c955956a85402d1.jpg)  
(b) Number of Query Terms = 2  
Figure 4. Effects of the Number of Query Terms

When using a topic-based method for query expansion, whether fuzzy or nonfuzzy, we take an average approach to measure the weight of an expanded term in relation to the user query. A user query that consists of a single query term may not provide sufficient information to determine appropriate document clusters. As a consequence, each cluster whose local thesaurus includes this particular query term (specified in the user query) would be searched. Conceivably, a set of excessively diverse query terms may be selected for query expansion, which means the resulting expanded queries would retrieve a considerably larger number of documents that are irrelevant to the user query. In the case of a two-term query, for each cluster that includes only one of the two query terms in its local thesaurus, the weight of a term expanded from that cluster generally should be less than the weight from another cluster containing both user query terms in its local thesaurus, according to our average approach. Understandably, clusters that contain both query terms therefore may provide a more appropriate context for expanding the user query than that offered by clusters that contain only some of the query terms, which, in turn, would generate more effective search results. Accordingly, the proposed topic-based methods become increasingly effective when user queries are less ambiguous—that is, described by more query terms. Overall, our analyses suggest the relative effectiveness of the proposed methods for query expansion, particularly when more top-ranked documents are considered or multiple terms are included in the user query.

<sub>ects</sub> <sub>of</sub> <sub>the</sub> <sub>Nu</sub>m<sup>ber</sup> <sup>of</sup> <sup>Query</sup> <sup>Terms</sup> <sup>Based</sup> <sup>on</sup>

<table><tr><td rowspan="2"></td><td colspan="10">r (number of top-ranked documents)</td></tr><tr><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td><td>30</td><td>35</td><td>40</td><td>45</td><td>50</td></tr><tr><td colspan="11">(a) Number of query terms = 1</td></tr><tr><td>Global analysis</td><td>0.3841</td><td>0.4819</td><td>0.4702</td><td>0.4360</td><td>0.3941</td><td>0.3736</td><td>0.3541</td><td>0.3369</td><td>0.3182</td><td>0.3046</td></tr><tr><td>Fuzzy topic based</td><td>0.4143</td><td>0.4692</td><td>0.4615</td><td>0.4457</td><td>0.4268</td><td>0.4085</td><td>0.3974</td><td>0.3706</td><td>0.3489</td><td>0.3332</td></tr><tr><td>Nonfuzzy topic based</td><td>0.4045</td><td>0.4541</td><td>0.4334</td><td>0.4070</td><td>0.3966</td><td>0.3923</td><td>0.3733</td><td>0.3563</td><td>0.3385</td><td>0.3190</td></tr><tr><td colspan="11">(b) Number of query terms = 2</td></tr><tr><td>Global analysis</td><td>0.2381</td><td>0.2441</td><td>0.2457</td><td>0.2377</td><td>0.2115</td><td>0.2009</td><td>0.1972</td><td>0.1915</td><td>0.1877</td><td>0.1790</td></tr><tr><td>Fuzzy topic based</td><td>0.2726</td><td>0.2983</td><td>0.2841</td><td>0.2593</td><td>0.2429</td><td>0.2268</td><td>0.2251</td><td>0.2168</td><td>0.1978</td><td>0.1861</td></tr><tr><td>Nonfuzzy topic based</td><td>0.2987</td><td>0.3088</td><td>0.2759</td><td>0.2567</td><td>0.2332</td><td>0.2125</td><td>0.2094</td><td>0.2016</td><td>0.1969</td><td>0.1858</td></tr></table>

## Conclusion and Future Research Directions

TO ADDRESS THE CHALLENGE OF THE WORD MISMATCH PROBLEM in IR, we propose two topic-based query expansion methods and empirically examine their effectiveness, using a prevalent global analysis method as a performance benchmark. Overall, our evaluation results are encouraging and suggest that both topic-based methods are generally more effective than the global analysis method and that the fuzzy method outperforms the nonfuzzy method in support of query expansion. The differential performances can be partly attributed to the global analysis method, which expands a user query using terms that are highly general or compromised across different topics. In contrast, the proposed topic-based approach extends global analysis by segmenting a document corpus into a set of clusters and then constructs a local thesaurus for each cluster. Therefore, our proposed methods can expand a user query using terms selected from clusters that are more relevant to the user-provided query, while also taking into consideration its context. For single-term queries, the fuzzy method appears to achieve comparable effectiveness to the global analysis method and outperforms the nonfuzzy method. For two-term user queries, the fuzzy method performs at a level largely comparable to that of the nonfuzzy method and noticeably outperforms the global analysis method.

This study thus contributes to IR research by proposing a novel query expansion approach to address the word mismatch problem. Recognizing the limitations of the global perspective on term associations commonly taken by existing query expansion techniques, we develop two topic-based query expansion methods and empirically show their feasibility in common IR scenarios. In addition, this study demonstrates the effectiveness of a topic-specific view of term associations and therefore can advance current text mining research. For example, most existing text mining techniques (e.g., text categorization, document clustering, question answering) exploit term associations, with a predominant emphasis on a global rather than a topic-specific perspective when constructing a statistical-based thesaurus. Text mining research can consider and extend the design of our proposed topic-based methods to advance existing context-independent text mining techniques from a single global thesaurus to context-specific analyses that use multiple topic-based thesauri. Finally, the current study can advance research and practice in related application domains (e.g., SEM and knowledge management) in which similar word mismatch problems also prevail. For example, many search engines (e.g., Google, Yahoo) offer services that allow advertisers to pay a reasonable fee to ensure their offerings or advertisements appear in the search results when a user submits specific key word(s) they have bid for or purchased. Word mismatch problems clearly can impede the effectiveness of SEM, as measured by hit rate. Our proposed topic-based query expansion methods could help mitigate these problems and thus make SEM far more effective and appealing.

Several areas demand continued investigative efforts. For example, in this study, we consider term associations symmetric, a restriction that should be relaxed in future research because term associations can be directionally asymmetric. Furthermore, we consider only first-order term associations that co-occur in the same documents. These term associations might not be effective for addressing orthographic variations (e.g., color versus colour, personalization versus personalisation). Additional research should extend from first-order term associations to higher-order associations by considering the context of terms. In addition, future studies should expand the current evaluation in both scope and scale. Our reported evaluation focuses on abstracts from selected IS journal articles. For greater validity and robustness, additional research should evaluate the effectiveness of our proposed topic-based query expansion methods using document corpora from different disciplines or application domains. Similarly, the sheer volume of the documents included in the reported evaluation is reasonable but could be increased.

In addition, to cluster the target document corpus into distinct clusters (topics), the proposed topic-based query expansion methods adopt k-means and fuzzy c-means algorithms; it would be interesting to evaluate the effectiveness of the proposed topicbased query expansion approach that uses different document clustering techniques, such as hierarchical clustering or Kohonen neural network algorithms. In this study, we expand a user query in all the clusters generated in the topic-based thesaurus construction phase; hence, we examine user queries individually without considering issues pertaining to cluster selection or prioritization. To further improve the effectiveness of the proposed topic-based methods, continued investigations could attempt to exploit the query history made by a user, thereby estimating the user’s preferences to support cluster selection or prioritization when expanding a query into locally expanded queries. Furthermore, this study concentrates on monolingual IR, in which both user queries and the target document corpus use the same language. However, due to the increasing globalization of business environments, documents in different languages are being generated and archived at a rapidly growing pace in organizational repositories and the Internet, which increases the demand for effective document search and retrieval support across language boundaries. This requirement highlights the importance of extending our proposed topic-based methods from a monolingual scenario to address the challenges common to cross-lingual document search and retrievals. Last but not least, the use of our proposed topic-based methods (or its extensions) in SEM can bring about interesting changes in SEM, affecting publishers and advertisers. For example, search engines should reevaluate their existing pricing considerations and methods when offering SEM services empowered by a set of search words expanded from those purchased by firms. Similarly, firms may need to reassess their bidding strategies for target search words if the search engine provides such expanded SEM capabilities. These changes are intriguing and worthy of research attention.

Acknowledgments: This work was supported by the National Science Council of the Republic of China under the grants NSC 91–2415-H-110–006, 92–2416-H-110–003, and 95–2752-H-007–004-PAE.

## NOTES

1. Examples of SEM services include Google AdWords (https://adwords.google.com), Yahoo! Sponsored Search (http://sem.smallbusiness.yahoo.com/searchenginemarketing/), and Microsoft adCenter (https://adcenter.microsoft.com/).

2. Term frequency denotes the occurrence frequency of a particular term in the source document corpus.

3. IDF denotes the inverse document frequency, measured by log (N/df), where N is the number of documents in the source corpus and df is the number of documents that contain the particular term under examination.

4. The 17 leading IS journals are Academy of Management Journal, Academy of Management Review, ACM Computing Surveys, ACM Transactions on Database Systems, Communications of the ACM, Decision Sciences, Decision Support Systems, European Journal of Information Systems, Harvard Business Review, IEEE Transactions on Computers, IEEE Transactions on Software Engineering, Information and Management, Information Systems Research, Journal of Management Information Systems, Management Science, MIS Quarterly, and Sloan Management Review.

5. The F1 measure is defined as (2 × Precision × Recall)/(Precision + Recall).

## REFERENCES

1. Anderberg, M.R Cluster Analysis for Applications. New York: Academic Press, 1973.

2. Attar, R., and Fraenkel, A.S. Local feedback in full-text retrieval systems. Journal of the ACM, 24, 3 (1997), 397–417.

3. Belkin, N.J., and Croft, W.B. Information filtering and information retrieval: Two sides of the same coin? Communications of the ACM, 35, 12 (1992), 29–38.

4. Billhardt, H.; Borrajo, D.; and Maojo, V. A context vector model for information retrieval. Journal of the American Society for Information Science and Technology, 53, 3 (2002), 236–249.

5. Boley, D.; Gini, M.; Gross, R.; Han, E.; Hastings, K.; Karypis, G.; Kumar, V.; Mobasher, B.; and Moore, L. Partitioning-based clustering for Web document categorization. Decision Support Systems, 27, 3 (December 1999), 329–341.

6. Brill, E. A simple rule-based part of speech tagger. In M. Bates and O. Stock (eds.), Proceedings of the Third Conference on Applied Natural Language Processing. East Stroudsburg, PA: Association for Computational Linguistics, 1992, pp. 152–155.

7. Brill, E. Some advances in rule-based part of speech tagging. In B. Hayes-Roth and R. Korf (eds.), Proceedings of the Twelfth National Conference on Artificial Intelligence. Menlo Park, CA: AAAI Press, 1994, pp. 722–727.

8. Carpineto, C.; Romano, G.; and Giannini, V. Improving retrieval feedback with multiple term-ranking function combination. ACM Transactions on Information Systems, 20, 3 (July 2002), 259–290.

9. Croft, W.B., and Harper, D.J. Using probabilistic models of document retrieval without relevance information. Journal of Documentation, 35, 4 (1979), 285–295.

10. Croft, W.B.; Cook, R.; and Wilder, R. Providing government information on the Internet: Experiences with THOMAS. In R. Furuta (ed.), Proceedings of the Second International Conference on Theory and Practice of Digital Libraries. College Station: Hypermedia Research Lab, Computer Science Department, Texas A&M University, 1995, pp. 19–24.

11. Cui, H.; Wen, J.R.; Nie, J.Y.; and Ma, W.Y. Query expansion by mining user logs. IEEE Transactions on Knowledge and Data Engineering, 15, 4 (2003), 829–839.

12. Cutting, D.; Karger, D.; Pedersen, J.; and Tukey, J. Scatter/gather: A cluster-based approach to browsing large document collections. In N. Belkin, P. Ingwersen, and A.M. Pejtersen (eds.), Proceedings of the Fifteenth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1992, pp. 318–329.

13. Deerwester, S.; Dumais, S.T.; Furnas, G.W.; Landauer, T.K.; and Harshman, R.A. Indexing by latent semantic analysis. Journal of the American Society for Information Science, 41, 6 (1990), 391–407.

14. Dumais, S.; Platt, J.; Heckerman, D.; and Sahami, M. Inductive learning algorithms and representations for text categorization. In K. Makki and L. Bouganim (eds.), Proceedings of the Seventh International Conference on Information and Knowledge Management. New York: ACM Press, 1998, pp. 148–155.

15. Dunn, J.C. A fuzzy relative of the ISODATA process and its use in detecting compact well separated clusters. Journal of Cybernetics, 3, 3 (1973), 32–57.

16. El-Hamdouchi, A., and Willett, P. Hierarchical document clustering using Ward’s method. In F. Rabitti (ed.), Proceedings of the Ninth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1986, pp. 149–156.

17. Furnas, G.W.; Landauer, T.K.; Gomez, L.M.; and Dumais, S.T. The vocabulary problem in human-system communication. Communications of the ACM, 30, 11 (November 1987), 964–971.

18. Gauch, S.; Wang, J.; and Rachakonda, S.M. A corpus analysis approach for automatic query expansion and its extension to multiple databases. ACM Transactions on Information Systems, 17, 3 (1999), 250–269.

19. Gudivada, V.N.; Raghavan, V.V.; Grosky, W.I.; and Kasanagottu, R. Information retrieval on the World Wide Web. IEEE Internet Computing, 1, 5 (1997), 58–68.

20. Guerrero Bote, V.P.; Moya Anegón, F.; and Herrero Solana, V. Document organization using Kohonen’s algorithm. Information Processing and Management, 38, 1 (2002), 79–89.

21. Huang, C.K.; Chien, L.F.; and Oyang, Y.J. Relevant term suggestion in interactive Web search based on contextual information in query session logs. Journal of the American Society for Information Science and Technology, 54, 7 (2003), 638–649.

22. Jain, A.K.; Murty, M.N.; and Flynn, P.J. Data clustering: A review. ACM Computing Surveys, 31, 3 (1999), 265–323.

23. Jansen, B.J., and Pooch, U. A review of Web searching studies and a framework for future research. Journal of the American Society for Information Science and Technology, 52, 3 (2001), 235–246.

24. Jing, Y., and Croft, W.B. An association thesaurus for information retrieval. In F. Bretano and F. Seitz (eds.), Proceedings of the Intelligent Multimedia Information Retrieval Systems and Management Conference (RIAO ’94). Paris: Centre de Hautes Etudes Internationales d’Informatique Documentaire (CID), 1994, pp. 146–160.

25. Khan, M.S., and Khor, S. Enhanced Web document retrieval using automatic query expansion. Journal of the American Society for Information Science and Technology, 55, 1 (2004), 29–40.

26. Kim, H.J., and Lee, S.G. A semi-supervised document clustering technique for information organization. In A. Agah, J. Callan, E. Rundensteiner, and S. Gauch (eds.), Proceedings of the Ninth International Conference on Information and Knowledge Management. New York: ACM Press, 2000, pp. 30–37.

27. Kim, H.J., and Lee, S.G. An effective document clustering method using user-adaptable distance metrics. In B. Panda (ed.), Proceedings of the 2002 ACM Symposium on Applied Computing. New York: ACM Press, 2002, pp. 16–20.

28. Kohonen, T. Self-Organization and Associative Memory. Berlin: Springer, 1989.

29. Kohonen, T. Self-Organizing Maps. Berlin: Springer, 1995.

30. Kraft, D.H.; Chen, J.; and Mikulcic, A. Combining fuzzy clustering and fuzzy inferencing in information retrieval. In Proceedings of the Ninth IEEE International Conference on Fuzzy Systems. Los Alamitos, CA: IEEE Computer Society Press, 2000, pp. 375–380.

31. Lagus, K.; Honkela, T.; Kaski, S.; and Kohonen, T. Self-organizing maps of document collections: A new approach to interactive exploration. In E. Simoudis, J. Han, and U. Fayyad (eds.), Proceedings of the Second International Conference on Knowledge Discovery and Data Mining. New York: ACM Press, 1996, pp. 238–243.

32. Larsen, B., and Aone, C. Fast and effective text mining using linear-time document clustering. In U. Fayyad, S. Chaudhuri, and D. Madigan (eds.), Proceedings of the Fifteenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. New York: ACM Press, 1999, pp. 16–22.

33. Lin, C.; Chen, H.; and Nunamaker, J.F. Verifying the proximity and size hypothesis for self-organizing maps. Journal of Management Information Systems, 16, 3 (Winter 1999–2000), 57–70.

34. Liu, Z., and Chu, W.W. Knowledge-based query expansion to support scenario-specific retrieval of medical free text. In L.M. Liebrock (ed.), Proceedings of the 2005 ACM Symposium on Applied Computing. New York: ACM Press, 2005, pp. 1076–1083.

35. Mendes, M.E.S., and Sacks, L. Evaluating fuzzy clustering for relevance-based information access. In O. Nasraoui, H. Frigui, and J.M. Keller (eds.), Proceedings of the Twelfth IEEE International Conference on Fuzzy Systems. Los Alamitos, CA: IEEE Computer Society Press, 2003, pp. 648–653.

36. Mitra, M.; Singhal, A.; and Burkley, C. Improving automatic query expansion. In W.B. Croft, A. Moffat, C.J. van Rijsbergen, R. Wilkinson, and J. Zobel (eds.), Proceedings of the Twenty-First Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1998, pp. 206–214.

37. Mylonopoulos, N.A., and Theoharakis, V. Global perceptions of IS journals. Communications of the ACM, 44, 9 (2001), 29–33.

38. Pantel, P., and Lin, D. Document clustering with committees. In M. Beaulieu, R. Baeza-Yates, and S.H. Myaeng (eds.), Proceedings of the Twenty-Fifth International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 2002, pp. 199–206.

39. Qiu, Y., and Frei, H.P. Concept based query expansion. In R. Korfhage, E. Rasmussen, and P. Willett (eds.), Proceedings of the Sixteenth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1993, pp. 160–169.

40. Raghavan, V.V., and Wong, S.K. A critical analysis of vector space model for information retrieval. Journal of the American Society for Information Science, 37, 5 (1986), 279–287.

41. Rainer, R.K., and Miller, M.D. Examining differences across journal rankings. Communications of the ACM, 48, 2 (2005), 91–94.

42. Rocchio, J. Relevance feedback in information retrieval. In G. Salton (ed.), The SMART Retrieval System: Experiments in Automatic Document Processing. Englewood Cliffs, NJ: Prentice Hall, 1971, pp. 313–323.

43. Roussinov, D., and Chen, H. Document clustering for electronic meetings: An experimental comparison of two techniques. Decision Support Systems, 27, 1–2 (1999), 67–79.

44. Salton, G., and Buckley, C. Improving retrieval performance by relevance feedback. Journal of the American Society for Information Science, 41, 4 (1990), 288–297.

45. Sparck Jones, K. Automatic Keyword Classification for Information Retrieval. London: Butterworths, 1971.

46. Tanaka, H.; Kumano, T.; Uratani, N.; and Ehara, T. An efficient document clustering algorithm and its application to a document browser. Information Processing and Management, 35, 4 (1999), 541–557.

47. van Rijsbergen, C.J. Information Retrieval. London: Butterworths, 1979.

48. Voorhees, E.M. Implementing agglomerative hierarchical clustering algorithms for use in document retrieval. Information Processing and Management, 22, 6 (1986), 465–476.

49. Voutilainen, A. NPtool: A detector of English noun phrases. In K.W. Church (ed.), Proceedings of the First Workshop on Very Large Corpora. East Stroudsburg, PA: Association for Computational Linguistics, 1993, pp. 48–57.

50. Wei, C.; Chiang, R.; and Wu, C. Accommodating individual categorization preferences: A personalized document clustering approach. Journal of Management Information Systems, 23, 2 (Fall 2006), 173–201.

51. Wei, C.; Hu, P.; and Dong, Y.X. Managing document categories in e-commerce environments: An evolution-based approach. European Journal of Information Systems, 11, 3 (September 2002), 208–222.

52. Wei, C.; Yang, C.S.; Hsiao, H.W.; and Cheng, T.H. Combining preference- and contentbased approaches for improving document clustering effectiveness. Information Processing and Management, 42, 2 (March 2006), 350–372.

53. Wong, S.K., and Yao, Y.Y. An information-theoretic measure of term specificity. Journal of the American Society for Information Science, 43, 1 (1992), 54–61.

54. Xu, J., and Croft, W.B. Query expansion using local and global document analysis. In H.P. Frei, D. Harman, P. Schaübie, and R. Wilkinson (eds.), Proceedings of the Nineteenth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1996, pp. 4–11.

55. Xu, J., and Croft, W.B. Improving the effectiveness of information retrieval with local context analysis. ACM Transactions on Information Systems, 18, 1 (January 2000), 79–112.

56. Zazo, A.F.; Figuerola, C.G.; Alonso Berrocal, J.L.; and Rodríguez, E. Reformulation of queries using similarity thesauri. Information Processing and Management, 41, 5 (2005), 1163–1173.
