---
otero_id: 8980
otero_key: "82SBHSYH"
title: "A collaborative filtering-based approach to personalized document clustering"
authors: "Chih-Ping Wei; Chin-Sheng Yang; Han-Wei Hsiao"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.05.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A collaborative filtering-based approach to personalized document clustering

Chih-Ping Wei <sup>a,⁎</sup>, Chin-Sheng Yang <sup>b</sup>, Han-Wei Hsiao <sup>c</sup>

<sup>a</sup> Institute of Technology Management, College of Technology Management, National Tsing Hua University, Hsinchu, Taiwan, ROC <sup>b</sup> Department of Information Management, College of Management, National Sun Yat-sen University, Kaohsiung, Taiwan, ROC <sup>c</sup> Department of Information Management, College of Economics and Management, National University of Kaohsiung, Kaohsiung, Taiwan, ROC

Available online 18 May 2007

## Abstract

Document clustering is an intentional act that reflects individual preferences with regard to the semantic coherency and relevant categorization of documents. Hence, effective document clustering must consider individual preferences and needs to support personalization in document categorization. Most existing document-clustering techniques, generally anchoring in pure contentbased analysis, generate a single set of clusters for all individuals without tailoring to individuals' preferences and thus are unable to support personalization. The partial-clustering-based personalized document-clustering approach, incorporating a target individual's partial clustering into the document-clustering process, has been proposed to facilitate personalized document clustering. However, given a collection of documents to be clustered, the individual might have categorized only a small subset of the collection into his or her personal folders. In this case, the small partial clustering would degrade the effectiveness of the existing personalized documentclustering approach for this particular individual. In response, we extend this approach and propose the collaborative-filtering-based personalized document-clustering (CFC) technique that expands the size of an individual's partial clustering by considering those of other users with similar categorization preferences. Our empirical evaluation results suggest that when given a small-sized partial clustering established by an individual, the proposed CFC technique generally achieves better clustering effectiveness for the individual than does the partial-clustering-based personalized document-clustering technique.

Keywords: Document clustering; Personalization; Collaborative filtering; Hierarchical agglomerative clustering (HAC); Text mining

## 1. Introduction

With the advances and proliferation of the Internet, available information sources have grown tremendously in number and sheer volume, primarily as a result of global connectivity and ease of publishing. To manage this ever-increasing volume of documents, organizations and individuals typically organize documents into categories (or category hierarchies) to facilitate their document management and support subsequent document retrieval and access. In turn, the development of an effective document-clustering mechanism has become essential for the efficient and effective document management of organizations and individuals.

Document clustering entails the automatic organization of a large document collection into distinct groups of similar documents that reflect general themes hidden within the corpus [21,22,33]. However, according to the context theory of classification, document-clustering behaviors of individuals not only involve the attributes (including contents) of documents but also depend on who is performing the task and in what context [3,11,26,28]. Therefore, document clustering is an intentional act that reflects individuals' unique preferences with regard to the semantic coherency or relevant categorization of documents [40]. For example, given a set of research articles related to “data mining,” researchers engaged in developing novel data mining techniques may prefer organizing the articles according to underlying techniques (e.g., classification analysis, clustering analysis, association rules, sequential patterns). In contrast, researchers who are applying data mining techniques to solve business questions generally would prefer categories based on application domains (e.g., banking, manufacturing, health care, telecommunications). Furthermore, even when they use the same categorization scheme, different researchers may vary in the granularity of the categories they employ. Some researchers, for example, might use a single category for all articles related to classification analysis, whereas others may employ a set of increasingly specific categories (e.g., decision tree induction, neural network, Bayes classification) for the same collection. Effective document clustering therefore must consider individual preferences and needs in order to support personalized document categorization [17,46].

Traditional document-clustering techniques generally have been anchored in pure content-based analysis. As a consequence, most existing document-clustering techniques are not tailored to individuals' preferences and therefore are unable to facilitate personalization. In other words, the categorization scheme exhibited in such nonpersonalized clusters may not conform to a user's expectation and perception. However, a user's document search typically is guided by his or her categorization scheme [14,38]. Thus, when searching documents with a one-for-all categorization scheme, a user generally undertakes a semantic internalization process [34] to comprehend the target categorization scheme or experiences a coadaptation process that adjusts his or her own categorization scheme and, at the same time, reinterprets and adapts the target categorization scheme to his or her needs [31,32]. The semantic internalization and coadaptation processes unnecessarily increase the user's cognitive load. Consequently, he or she likely spends more time or has difficulty locating documents of interest because of the discrepancy between the one-for-all categorization scheme and his or her expectation [46]. The described inefficiency or ineffectiveness of document retrieval and access may adversely affect the efficiency, quality, and satisfaction of decision making that requires references to various documents relevant to the target decision context.

Several prior studies have sought to incorporate noncontent information into the document-clustering process to improve clustering effectiveness. Because the noncontent often is associated with individual users, these document-clustering techniques represent possible approaches to achieve personalized document clustering. For example, the adaptive [50] and user-oriented [13,35] document-clustering techniques take the documents relevance to user queries into account when clustering a collection of documents. To support personalized document clustering for a target user, all queries should be made by that user. However, both techniques assume that all documents in the collection D to be clustered must appear in at least one set of relevant documents for a query. If a document is considered irrelevant to all queries, its similarity with other documents in D cannot be esti mated. As the size of D expands, the number of documents considered irrelevant to all queries increases, creating a serious problem to both techniques. Furthermore, document relevance to queries often is associated with query contexts. Therefore, heterogeneity in query contexts may constrain the effectiveness of these techniques for facilitating personalized document clustering. Kim and Lee [21] propose a semi-supervised documentclustering technique, a hybrid of content- and noncontentbased document-clustering approaches, that considers not only document content similarity but also users' perceptions of document similarity using a relevance feedback mechanism. Relevance feedback offers a means to achieve personalized document clustering, but such realtime feedback is prohibitively tedious and unpractical in terms of both time and cognitive efforts. Moreover, relevance feedback is impractical in many documentclustering applications (e.g., cluster-based browsing by digital libraries and search engines), thereby making it an unfeasible solution for personalized document clustering.

To address the limitations inherent to these techniques, Wei et al. [46] propose a partial-clustering-based personalized document-clustering approach that incorporates a target user's partial clustering into the documentclustering process. Let the set of documents to be clustered be D. A partial clustering denotes a user's categorization of a subset of documents in D. In some application environments, the partial clustering of a user is readily available. For example, some digital libraries and online information providers offer personal bookshelves (e.g., “my bookshelf,” “my favorites,” “my eNews”) so that users can organize documents of interest into their personal folders. When a set of documents is retrieved for clustering for a specific user, some documents in the set may have been previously organized into his or her personal folders. In this case, the user's partial clustering, which reflects his or her categorization preferences, is available and can be employed to facilitate subsequent personalized document clustering.

Empirical evaluation results suggest that the use of a user's partial clustering improves document-clustering effectiveness [46]. However, a user might have categorized only a small number of documents in D. In this case, the small partial clustering can degrade the effectiveness of the partial-clustering-based personalized documentclustering approach for that particular user. To address this limitation, we extend the partial-clustering-based personalized document-clustering approach and propose the use of a collaborative filtering recommendation approach to expand the size of an individual user's partial clustering by considering those of other users with similar categorization preferences. Specifically, we propose a collaborative filtering-based personalized document-clustering technique (CFC) and experimentally evaluate its effectiveness, using that attained by the partial-clusteringbased personalized document-clustering approach and a salient content-based document-clustering technique as performance benchmarks.

The remainder of this paper is organized as follows: in Section 2, we review relevant literature on documentclustering techniques and the collaborative filtering recommendation approach. Section 3 details the proposed CFC technique, including its overall process and specific designs. In Section 4, we describe our evaluation design and discuss some important empirical evaluation results. Finally, we conclude with a summary and future research directions in Section 5.

## 2. Literature review

In this section, we review literature on traditional content-based document-clustering techniques, the partial-clustering-based personalized document-clustering approach, and the collaborative filtering recommendation approach.

## 2.1. Content-based document clustering

Traditional document-clustering techniques group documents on the basis of their contents. The documents in the resultant cluster exhibit maximal similarity to those in the same cluster and share minimal similarity with documents in other clusters. A content-based documentclustering technique generally consists of three main phases: feature extraction and selection, document representation, and clustering [46,47].

Feature extraction begins with the parsing of each source document to produce a set of nouns and noun phrases (commonly referred to as “features”) and exclude a list of prespecified “stop words” that are non-semanticbearing words. Subsequently, representative features are selected from the set of extracted features. Feature selection is important for clustering efficiency and effectiveness, because it not only condenses the size of the extracted feature set but also reduces the potential biases embedded in the original (i.e., nontrimmed) feature set [15,39]. Previous research commonly has employed such feature selection metrics as term frequency (TF) (which denotes the occurrence frequency of a particular term in the document collection), TF×IDF (in which IDF denotes the inverse document frequency measured by log(N/DF), where N is the number of documents in the collection and DF is the number of documents containing the focal term), and their hybrids [5,7,29,36].

According to the top-k selection method, the k features with the highest selection metric scores are selected to represent each target document in the document representation phase. Thus, each document is represented as a feature vector jointly defined by the previously selected k features. A review of prior research suggests the prevalence of the binary (which indicates the presence or absence of a feature in a document), TF (within-document term frequency), and TF×IDF [5,29,39,48] representation schemes.

In the final phase of document clustering, the target documents are grouped into distinct clusters on the basis of the selected features and their respective values in each document. Common approaches include partitioning-based [7,12,29], hierarchical [16,39,44], and Kohonen neural network [18,27,30,39]. The partitioningbased approach (e.g., k-means [1]) partitions the set of documents into multiple, nonoverlapping clusters. The hierarchical approach builds a binary clustering hierarchy whose leaf nodes represent the target documents and can be further classified into agglomerative and divisive clustering methods. Specifically, the hierarchical agglomerative clustering (HAC) algorithm, which exemplifies a bottom-up strategy, starts with as many clusters as there are documents [44]. On the basis of the intercluster similarity measure of choice (e.g., single link, complete link, group-average link, Ward's method), the two most similar clusters are merged to form a new cluster. This merging process continues until either a hierarchy emerges with a single cluster at the top or a predefined termination condition is satisfied (e.g., intercluster similarity is less than a prespecified threshold). The hierarchical divisive clustering algorithm [20], in contrast, follows a top-down strategy by having all the documents in one cluster initially. This (root) cluster is then subdivided into the two most distinct clusters, and the division process is repeated until each document forms a cluster of its own or a predefined termination condition is reached. Finally, the Kohonen neural network approach, also known as a self-organizing map (SOM), uses an unsupervised two-layer neural network [23,24]. Within a Kohonen neural network, the input node corresponds to a feature in the selected feature vector space, and the output node represents a cluster in a two-dimensional grid. The network is fully connected; that is, each output node is connected to each input node by a particular connection weight. During the training phase, the target documents are fed into the network multiple times to adjust the connection weights in such a way that the distribution of the output nodes would accurately represent that of the target documents.

## 2.2. Partial-clustering-based personalized documentclustering

In response to the shortcomings and limitations of existing document-clustering techniques for supporting personalization in document categorization, Wei et al. [46] propose a personalized document-clustering approach that incorporates a user's partial clustering into the document-clustering process. Specifically, in addition to the contents of documents to be clustered, the personalized document-clustering approach includes as additional input the partial clustering of a target user and consists of three main phases: (1) feature extraction, selection, and consolidation; (2) document representation; and (3) clustering.

The feature extraction, selection, and consolidation phase first extracts and selects representative features for the document corpus D to be clustered on the basis of the document contents and the partial clustering offered by the target user. Specifically, as measured by the TF×IDF feature selection metric, a set of top-ranked features (referred to as $A L L { } _ { - } T F { } { \times } I D F )$ is selected from D. In addition, to capture the target user's categorization preference, the $\chi ^ { 2 }$ statistic metric is employed to determine, from the partial clustering, a set of features (denoted $P a r t i a l _ { - } \chi ^ { 2 } )$ that best differentiates each partial cluster. Furthermore, the personalized document-clustering approach considers frequent but nonrepresentative features in the partial clusters as irrelevant to the categorization scheme. Thus, on the basis of the TF selection metric, a set of features (denoted Partial\_TF) is identified from the documents in the partial clustering. The features in (Partial \_ $T F - P a r t i a l \_ \textmu ^ { 2 } )$ are thus nondiscriminative with respect to the partial clustering and therefore should be excluded. Accordingly, a consolidated feature set is constructed and employed for personalized document clustering as follows:

$$
\left(A L L \_ T F \times I D F - \left(P a r t i a l \_ T F - P a r t i a l \_ \chi^ {2}\right)\right) \cup P a r t i a l \_ \chi^ {2}.\tag{1}
$$

In the document representation phase, each document in D is represented as a feature vector defined by the consolidated feature set. Two representation methods, feature refinement and feature weighting, are proposed. The feature refinement method does not consider the degree of importance of each feature in the consolidated feature set and adopts the TF×IDF scheme as its underlying representation method. In contrast, the feature weighting method considers a feature with greater power to differentiate the partial clusters as more important (i.e., it is given greater weight) than one with less discriminatory power. Therefore, in addition to its use of TF × IDF as its underlying representation scheme, the feature weighting method uses the $\chi ^ { 2 }$ statistic of each feature as the weight of the feature when representing the documents in D.

Finally, as with traditional content-based documentclustering techniques, the clustering phase groups the target documents into distinct clusters on the basis of the consolidated features and their respective values for each document. Because the user's partial clustering is available, two different clustering methods can be employed. The atomic-based HAC method treats each document in $D$ as an initial cluster and applies the HAC algorithm to generate document clusters, where the similarity of two documents $d _ { i }$ and $d _ { j }$ is estimated by the cosine similarity measure and the group-average link method is adopted to assess the similarity between two clusters. In contrast, with the precluster-based HAC method, the documents in each partial cluster are regarded as an initial cluster, and every document that does not appear in any partial clusters forms its own cluster initially. Subsequently, the precluster-based HAC method proceeds in the same way as the atomic-based HAC method.

Using the traditional content-based document-clustering technique as a performance benchmark, Wei et al.'s [46] empirical evaluation demonstrates that the use of a user's partial clustering can improve document-clustering effectiveness. Though the effectiveness of the partialclustering-based personalized document-clustering approach is encouraging, it is susceptible to the size of the partial clustering. That is, when the size of the partial clustering decreases, the clustering effectiveness attained by this personalized document-clustering approach degrades as well. However, in a typical real-world setting, the partial clustering established by a user often tends to be small; therefore, the partial-clustering-based personalized document-clustering approach needs to be enhanced so that it can effectively cluster documents even when only a small partial clustering is available.

## 2.3. Collaborative filtering recommendation

Recommendation systems typically suggest items (e.g., products, documents) that are of interest to users, according to user demographics, features of items, and/or user preferences. The collaborative filtering recommendation approach identifies users whose tastes are similar to those of a target user and recommends items that the others have liked [2,19]. Among the different collaborative filtering techniques, such as neighborhood-based [19,41,43], Bayesian networks [8], singular value decomposition with neural network classification [6], and induction rule learning [4], the neighborhood-based technique is most prevalent. Its process generally encompasses two major phases: neighborhood formation and recommendation generation [41]. The neighborhood formation phase, referred to as the model-building process for collaborative filtering recommendations, computes the similarities between the preferences of a target user and those of all other users. Several different similarity measures have been proposed [19,41,43], including the Pearson correlation coefficient, constrained Pearson correlation coefficient, Spearman rank correlation coefficient, cosine similarity, and mean-squared difference. For example, the similarity between a target user $u _ { a }$ and another user $u _ { b }$ according to the Pearson correlation coefficient can be derived as:

$$
\operatorname{sim} \left(u _ {a}, u _ {b}\right) = \frac {\sum_ {i = 1} ^ {m} \left(p _ {a _ {i}} - \bar {p} _ {a}\right) \left(p _ {b _ {i}} - \bar {p} _ {b}\right)}{\sqrt {\sum_ {i = 1} ^ {m} \left(p _ {a _ {i}} - \bar {p} _ {a}\right) ^ {2}} \sqrt {\sum_ {i = 1} ^ {m} \left(p _ {b _ {i}} - \bar {p} _ {b}\right) ^ {2}}},\tag{2}
$$

where $p _ { a _ { i } }$ is the preference score of user $u _ { a }$ on item $i ,$ $\overline { { p } } _ { a }$ denotes the average preference score of ${ \dot { u } } _ { a } ,$ and m is the number of items co-rated by both $u _ { a }$ and $u _ { b }$ .

After the similarities between the target user and all other users have been estimated, the next task in the neighborhood formation phase is to form a proximitybased neighborhood with like-minded users for the target user. A review of prior research suggests several neighborhood selection schemes, including weight thresholding (i.e., all neighbors of $u _ { a }$ with absolute similarities greater than a given threshold are selected) and center-based best-k neighbors (i.e., a neighborhood of a prespecified size k is formed for $u _ { a }$ by selecting the k nearest users) [19,41].

Subsequently, in the recommendation generation phase, the preference score for a specific item j is derived for the target user on the basis of the preferences of his or her nearest neighbors, using one of the following methods. The weighted average method combines all neighbors' preference scores on the item j into a prediction, using the similarities between the target user and his or her nearest neighbors as the weights [43]. To account for preference differences, the deviation-from-mean method first computes the deviation of a neighbor's preference score for item j from his or her mean preference score, which is taken across all items the neighbor has rated [25,37]. The weighted average deviation from the mean then is derived across all neighbors, again using the similarities between the target user and his or her nearest neighbors as weights. Finally, the preference score for item j is estimated as the sum of the target user's mean score and the weighted average deviation from the mean calculated previously. Alternatively, to deal with the situation in which the spread of users' preference score distributions differs, the z-score average method, an extension of the deviation-from-mean method, has been proposed [19]. Neighbors' preference scores are first converted to their z-scores, then the preference score of item j for the target user is predicted as the sum of the target user's mean score and a weighted average of the neighbors' z-scores on item j.

## 3. Collaborative filtering-based personalized document-clustering (CFC) technique

In response to the limitation of the partial-clusteringbased personalized document-clustering approach when only a small partial clustering is available [46], we propose a collaborative filtering-based personalized document-clustering (CFC) technique that considers not only a target user's but also other users' partial clusterings when estimating the categorization preference of the target user. As we illustrate in Fig. 1, the proposed technique consists of four main phases: (1) collaborative clustering-expansion, (2) feature construction, (3) document representation, and (4) clustering.

## 3.1. Collaborative clustering-expansion phase

The purpose of the collaborative clustering-expansion phase is to expand the size of a user's partial clustering by considering those of other users with similar categorization preferences. Two major tasks are involved in this phase: neighborhood formation and expansion of the partial clustering.

![](/api/attachments/82SBHSYH/fulltext/images/2c0d4deed8f82a61d2f2ad9579be944e168bae44a25451e8adc87c605f843812.jpg)  
Fig. 1. Overall process of the CFC technique.

To form the neighborhood for target user $u _ { a } ,$ we first compute the similarities between the target user and all other users on the basis of their partial clusterings. Assume that D is the set of documents to be clustered for $u _ { a } .$ . Let $D _ { a b } \subset D$ be a subset of documents that exists in both the personal folders of $u _ { a }$ and those of another user $u _ { b } .$ . Furthermore, assume that $C _ { a }$ is the partial clustering of $u _ { a } ( \mathrm { i } . \mathrm { e } . , C _ { a }$ is a set of clusters for all documents in $D _ { a b }$ that conforms to the personal folder of $\overset { \cdot } { u } _ { a } )$ and $C _ { b }$ is the partial clustering of $u _ { b }$ . The similarity of the clustering preferences of $u _ { a }$ and $u _ { b }$ is estimated as a function of the similarity between $C _ { a }$ and $C _ { b }$ . Because $C _ { a }$ and $C _ { b }$ contain sets of document clusters, we adopt the concept of associations [39,47] to measure their similarity. Let the documents in $D _ { a b }$ be organized in a total order, and $d _ { i } \prec d _ { j }$ if $d _ { i } \in \cal { D } _ { a b }$ appears before $d _ { j } \in D _ { a b }$ in the defined order. Hence, $S _ { a }$ and $S _ { b } ,$ , two sets of associations in $C _ { a }$ and $C _ { b } ,$ respectively, are defined as:

$S _ { a } = \{ ( d _ { i } , d _ { j } ) | d _ { i } \in D _ { a b } , d _ { j } \in D _ { a b } , d _ { i }$ and $d _ { j }$ are in the same cluster in $C _ { a } ,$ and $d _ { i } \prec d _ { j } \}$ and

$S _ { b } = \{ ( d _ { i } , d _ { j } ) | d _ { i } \in D _ { a b } , d _ { j } \in D _ { a b } , d _ { i }$ and $d _ { j }$ are in the same cluster in $C _ { b } ,$ and $d _ { i } \prec d _ { j }  \}$

Accordingly, the similarity of $C _ { a }$ and $C _ { b }$ is defined as:

similarity $\left( C _ { a } , C _ { b } \right)$

$$
= \left\{ \begin{array}{l l} \frac {2 \times | S _ {a} \cap S _ {b} |}{| S _ {a} | + | S _ {b} |} & \text { if } S _ {a} \neq \emptyset \text { and } S _ {b} \neq \emptyset \\ 0 & \text { if } S _ {a} = \emptyset \text { or } S _ {b} = \emptyset \end{array} \right.\tag{3}
$$

Furthermore, if the number of documents in $D _ { a b }$ is large, similarity $( C _ { a } , C _ { b } )$ offers a good estimate of the similarity of the clustering preferences of ${ \dot { u } } _ { a }$ and $u _ { b } .$ . However, a decrease in $| D _ { a b } |$ would decrease our confidence in the use of similarity $( C _ { a } , C _ { b } )$ to estimate the similarity of the clustering preferences of $u _ { a }$ and $u _ { b }$ . Taking into account the described effect of $| D _ { a b } |$ , we define the similarity of the clustering preferences of $u _ { a }$ and $u _ { b }$ as:

$$
\begin{array}{c} \text {similarity} (u _ {a}, u _ {b}) = \text {confidence} (| D _ {a b} |) \\ \times \text {similarity} (C _ {a}, C _ {b}), \end{array}\tag{4}
$$

$$
\text { where   } \text { confidence } (| D _ {a b} |) = \left\{ \begin{array}{l l} \left(\frac {| D _ {a b} |}{\text { SigN }}\right) ^ {h} & \quad \text { if   } | D _ {a b} | \leq \text { SigN }, \\ 1 & \quad \text { if   } | D _ {a b} | > \text { SigN }, \end{array} \right.
$$

and SigN is a predefined significance threshold. In $\mathrm { F i g } . 2$ , we show the curves of the described confidence function with different h (using $S i g N { = } 1 0 )$ . Apparently, varying the value of h changes the steepness of the function curve.

After we compute the similarities between the target user $u _ { a }$ and all other users, we form the neighborhood for $u _ { a } .$ . For this study, we select the top n nearest users to become the neighborhood $N _ { a }$ for $u _ { a } .$ . Subsequently, the expansion of the partial clustering task is undertaken to address the problem of a possibly small partial clustering of $u _ { a }$ that might degrade the effectiveness of the personalized document clustering. Let U be a subset of documents in D that exists either in the personal folders of $u _ { a }$ or those of any of his or her nearest neighbors in $N _ { a }$ . For each pair of documents $d _ { i }$ and $d _ { j }$ in $U ,$ their similarity, collaboratively determined by $u _ { a }$ and his or her neighborhood, is defined as:

![](/api/attachments/82SBHSYH/fulltext/images/41c85be54e2e9fc6f0375316d094d058fccfb24c377f5aecbe65aee14d23b41e.jpg)  
Fig. 2. Examples of confidence functions.

$$
s i m i l a r i t y _ {c o l l a b o r a t i v e} (d _ {i}, d _ {j}) = \lambda \times f _ {a} (d _ {i}, d _ {j})\tag{5}
$$

$$
+ (1 - \lambda) \frac {\sum_ {u _ {b} \in N _ {a}} \text {similarity} (u _ {a} , u _ {b}) \times f _ {b} (d _ {i} , d _ {j})}{\sum_ {u _ {b} \in N _ {a}} \text {similarity} (u _ {a} , u _ {b})}
$$

where $f _ { a } ( d _ { i } , d _ { j } ) \ : ( \mathrm { o r } \ : f _ { b } ( d _ { i } , d _ { j } ) )$ is 1 if $d _ { i }$ and $d _ { j }$ appear in the same folder of ${ u _ { a } } ^ { \mathrm { { , } } } \mathrm { s } \left( \mathrm { o r } { u _ { b } } ^ { \mathrm { { , } } } \mathrm { s } \right)$ partial clustering, 0 if $\dot { } d _ { i }$ and $d _ { j }$ appear in different folders, and 0.5 (i.e., unknown) otherwise. λ denotes the weight of ${ u _ { a } } ^ { \mathrm { { \prime } } } \mathrm { { s } }$ preference-based document similarity between $d _ { i }$ and $d _ { j }$ in their overall collaborative-based document similarity.

Accordingly, on the basis of the defined collaborativebased document-similarity measure, we perform a preclustering on the set of documents in $U$ to obtain a set of extended partial clusters for $u _ { a }$ . We adopt a hierarchical document-clustering approach, specifically the HAC algorithm, for the target preclustering task. It is worth noting that any non-centroid-based clustering algorithm (e.g., hierarchical divisive clustering algorithm [20], PAM algorithm [20]) also could be employed. However, centroid-based clustering algorithms (e.g., k-means [1]) are not suitable for our preclustering task because they require original document feature vectors as inputs and assess the similarity between a document and a centroid directly from their feature vectors. With the HAC algorithm, a prespecified similarity threshold $\beta$ is used to determine the appropriate number of clusters generated for U. Furthermore, clusters with fewer than $\delta$ documents are regarded as unrepresentative and removed from the extended partial clustering $E C _ { a }$ for the target user $u _ { a } .$

## 3.2. Feature construction phase

The purpose of the feature construction phase is to create a set of features for target user $u _ { a }$ that considers not only the documents in D but also the extended partial clustering of $u _ { a } ~ ( \mathrm { i . e . , } ~ E C _ { a } )$ . This phase involves three tasks: feature extraction, selection, and consolidation. Feature extraction converts each document in D into a set of nouns and noun phrases. We adopt the rule-based part-of-speech tagger developed by Brill [9,10] to tag each word syntactically in the documents. Subsequently, we employ the approach proposed by Voutilainen [45] to implement a noun-phrase parser for extracting noun phrases from each syntactically tagged document.

In the proposed CFC technique, feature selection first determines the representative features for the entire document collection D. We use TF×IDF as the feature selection metric because of its popularity in text categorization and document clustering research [7,29,33,39]. The set of top $k _ { 1 }$ features is selected and referred to as $A L L _ { - } T F { \times } I D F .$ Moreover, because the extended partial clustering $E C _ { a }$ reflects the categorization preference of target user $u _ { a } ,$ a set of features (denoted Partial\_ $. {  { \chi } } ^ { 2 } )$ that best differentiates each cluster from others in $E C _ { a }$ is selected on the basis of the weighted average of the $\chi ^ { 2 }$ statistic [49] as the feature selection metric. The $\chi ^ { 2 }$ statistic measures the dependence between a feature f and a partial cluster $H _ { i } .$ Using a two-way contingency table of a feature $f$ and a cluster $H _ { i } ,$ let $n _ { r + }$ be the number of documents in the cluster $H _ { i }$ in which feature f occurs, $n _ { r _ { - } }$ be the number of documents in $H _ { i }$ in which f does not appear, $n _ { n ^ { + } }$ <sub>+</sub> be the number of documents in the clusters other than $H _ { i }$ in which $f$ occurs, $n _ { n - }$ be the number of documents in the clusters other than $H _ { i }$ in which f does not appear, and $n$ be the total number of documents included in the extended partial clustering $E C _ { a } .$ The $\chi ^ { 2 }$ statistic of f relevant to $H _ { i }$ thus is defined as follows:

$$
\chi^ {2} (f, H _ {i}) = \frac {n \times (n _ {r +} n _ {n -} - n _ {r -} n _ {n +}) ^ {2}}{(n _ {r +} + n _ {r -}) (n _ {n +} + n _ {n -}) (n _ {r +} + n _ {n +}) (n _ {r -} + n _ {n -})}.\tag{6}
$$

After we derive the $\chi ^ { 2 }$ statistic of feature f relevant to each partial cluster $H _ { i } ,$ the overall $\chi ^ { 2 }$ statistic of $f$ for all extended partial clusters is calculated using the weighted average scheme [49]. That is, $\chi ^ { 2 } ( f , E C _ { a } ) =$ $\begin{array} { r } { \sum _ { H _ { i } \in E C _ { a } } p ( H _ { i } ) \times \chi ^ { 2 } ( f , H _ { i } ) } \end{array}$ , where $p ( H _ { i } )$ is the number of documents in $H _ { i }$ divided by n. Accordingly, the top $k _ { 2 }$ features with the highest weighted average of $\chi ^ { 2 }$ statistic scores are selected and included in Partial $\mathcal { X } ^ { 2 }$

Furthermore, we consider frequent but nondiscriminative features in the extended partial clustering $E C _ { a }$ as potentially irrelevant to the categorization preference of target user $u _ { a } .$ Thus, on the basis of the TF selection metric, we select the top $k _ { 3 }$ features (denoted Partial\_TF) from the documents in the extended partial clustering. Accordingly, the features in the set (Partial\_ $T F -$

Partial\_ $\mathcal { X } ^ { 2 } )$ are regarded as nonrepresentative features with respect to the extended partial clustering $E C _ { a }$ and therefore should be excluded.

Finally, the feature consolidation task determines a set of relevant features by considering $A L L _ { - } T F { \times } I D F ,$ $P a r t i a l \_ x ^ { 2 }$ , and Partial\_TF. As with the traditional partial-clustering-based personalized document-clustering approach [46], the consolidated feature set derived in the proposed CFC technique is as follows:

$$
\begin{array}{c} (A L L \_ T F \times I D F - (P a r t i a l \_ T F - P a r t i a l \_ \chi^ {2})) \cup P a r t i a l \_ \chi^ {2} \\ = (A L L \_ T F \times I D F - P a r t i a l \_ T F) \cup P a r t i a l \_ \chi^ {2}. \end{array}\tag{7}
$$

As we mentioned previously, ALL\_TF×IDF includes $k _ { 1 }$ features, Partial $\bar { \mathcal { X } } ^ { 2 }$ has $k _ { 2 }$ features, and Partial\_ $. T F$ includes $k _ { 3 }$ features. Assume that $p c$ (where $0 < p c < 1 )$ of the document collection to be clustered appears in the extended partial clustering, and $k _ { 1 } = k$ . For the proposed CFC technique, we set $k _ { 2 } { = } p c ^ { \times } k$ and $k _ { 3 } { = } p c ^ { \times } k$ . Thus, the maximal number of features in the resultant consolidated feature set is $k ^ { + } ( p c \times k )$ , and the minimal number is $k ^ { - } ( p c ^ { \times } k )$ .

## 3.3. Document representation phase

Each document in the collection is represented by features of the consolidated feature set. In this study, the TF×IDF scheme is adopted as the representation method. Specifically, each document $d _ { i }$ is described by a feature vector $\overrightarrow { d } _ { i }$ in the consolidated feature space as:

$$
\overrightarrow {d _ {i}} = <   v _ {i 1}, v _ {i 2}, \dots , v _ {i m} >,\tag{8}
$$

where m is the total number of features in the consolidated feature set ( $\mathrm { . . e . , } k \mathrm { - } ( p c \times k ) \leq m \leq k + ( p c \times k ) )$ , and $\nu _ { i j }$ is the within-document TF×IDF of feature f in document $d _ { i } .$

## 3.4. Clustering phase

On the basis of the extended partial clustering of a target user (obtained in the collaborative clustering-expansion phase) and the feature vectors represented in the consolidated feature space, the clustering phase groups the documents in D into distinct clusters for the specific user. As with traditional content-based document-clustering techniques, any existing clustering algorithm (e.g., partitioning-based, hierarchical, Kohonen neural network) can be employed for the target personalized documentclustering. Among these common clustering approaches, hierarchical clustering has an advantage over partitioningbased, in that the number of clusters need not be prespecified and can be decreased (or increased) by adjusting the intercluster similarity threshold. Furthermore, the hierarchical clustering approach can achieve clustering effectiveness comparable to that of the Kohonen neural network [39]. Therefore, our proposed CFC technique employs the hierarchical clustering approach (specifically, HAC) as its underlying clustering algorithm.

With the availability of the target user's extended partial clustering, some documents have already been grouped into clusters in the extended partial clustering. Therefore, the HAC algorithm can use these extended partial clusters directly during its initial clustering stage. Specifically, the documents in each extended partial cluster are regarded as an initial cluster, and every document that does not appear in any extended partial cluster forms its own cluster. Subsequently, the two clusters with the highest intercluster similarity are merged into one cluster at a higher level in the clustering hierarchy until a termination condition (e.g., a predetermined intercluster similarity threshold) is satisfied. In this study, the similarity of two documents $d _ { i }$ and $d _ { j }$ is estimated by the cosine similarity measure, as we show in Eq. (9). Furthermore, we employ the group-average link method, using the average similarity among all intercluster pairs of documents, to measure the similarity between two clusters.

$$
\operatorname{sim} (d _ {i}, d _ {j}) = \frac {\overrightarrow {d _ {i}} \overrightarrow {d _ {j}}}{| \overrightarrow {d _ {i}} | \times | \overrightarrow {d _ {j}} |},\tag{9}
$$

where $\overrightarrow { d } _ { i }$ is the feature vector of the document $d _ { i } ,$ , and $\mid { \overrightarrow { d } } _ { i } \mid$ is the length of $\overrightarrow { d } _ { i }$

The described clustering phase can be extended easily to other clustering algorithms. For example, when using k-means as the underlying clustering algorithm for grouping the documents in $D$ in the presence of the target user's extended partial clustering, we could first derive the centroid feature vector for each extended partial cluster by averaging the feature vectors that pertain to the constituent documents contained in the extended partial cluster. Accordingly, given a prespecified number of clusters to generate, the k-means algorithm commences its clustering process by taking as its input the centroid feature vectors of the extended partial clusters and the individual feature vectors of the remaining documents that do not appear in any partial clusters.

## 4. Empirical evaluation

This section reports our empirical evaluation of the proposed CFC technique. We highlight our evaluation design (including data collection, evaluation criteria, and evaluation procedure), the document-clustering techniques employed for performance benchmarks, and our parameter tuning experiments and results. We then discuss important empirical evaluation results.

## 4.1. Data collection

The document collection for our evaluation purpose consisted of 435 research articles related to information systems and technologies collected through keyword searches (e.g., XML, data mining, robotics) from a scientific literature digital library Web site (i.e., CiteSeer, at http://citeseer.nj.nec.com/). For each article in our CiteSeer corpus, we used only the abstract and keywords in this evaluation study.

We solicited 17 experimental subjects to construct their preferred clusters for the entire CiteSeer corpus (categorizing all 435 documents). Because the CiteSeer corpus relates to information technology and systems, we constrained the experimental subjects to master's and doctoral students majoring in management information systems. According to their self-reported estimates, each subject spent a minimum of eight hours completing his or her manual clustering of all documents in the CiteSeer corpus. In addition, because the CFC technique requires other users' personal folders to serve as partial clusterings to facilitate its collaborative clustering-expansion phase, we recruited an additional 34 subjects to participate in a personal folder collection. Each subject was assigned approximately 50 documents randomly selected from the CiteSeer corpus and asked to categorize the documents manually without any hints. A subject could remove any document he or she had difficulty understanding or assigning to any category. A summary of the complete and partial clusterings generated by all experimental subjects appears in Table 1.

## 4.2. Evaluation criteria and procedure

We employed cluster recall and cluster precision [39,47], defined according to the concept of associations, to measure the effectiveness of the CFC technique and its benchmark techniques. An association refers to a pair of documents that belong to the same cluster. Assume that the clusters in the complete clustering manually produced by subject $u _ { a }$ are the true categories for $u _ { a } .$ Accordingly, the cluster recall (CR) and cluster precision (CP) from ${ u _ { a } } ^ { \mathrm { { } } } \mathrm { { s } }$ viewpoint are defined as:

$$
C R = \frac {| C A |}{| T A |}, \text { and } C P = \frac {| C A |}{| G A |},\tag{10}
$$

where TA is the set of associations in the true categories established by $u _ { a } ,$ CA is the set of correct associations that exists in both the clusters generated by the document-clustering technique and the true categories, and GA is the set of associations in the clusters generated by the document-clustering technique.

For each subject with complete clustering, we first set $p c { = } 2 0 \%$ (i.e., randomly took 20% of documents categorized by the subject as his or her partial clustering) and then examined the effects of different values of pc on the effectiveness of the proposed CFC technique (see discussion in Section 4.5). Given a specific $_ { p c , }$ the CiteSeer corpus was clustered by each documentclustering technique under investigation. For each subject with complete clustering, we then measured the cluster recall and cluster precision of each technique. The overall clustering effectiveness of each technique was calculated by averaging the cluster recall and cluster precision obtained from all subjects (with complete clustering). To address the inevitable trade-offs between cluster precision and cluster recall, we employed precision/recall trade-off (PRT) curves. A PRT curve represents the effectiveness of a document-clustering technique with different numbers of clusters (i.e., 2–60 in this study). Evidently, as the number of clusters increases, the average number of documents in each cluster decreases; thus, a higher cluster precision comes at the cost of cluster recall. A documentclustering technique with a PRT curve closer to the upperright corner is more desirable.

## 4.3. Benchmark techniques

To evaluate the comparative effectiveness of the proposed CFC technique, we adopted a salient contentbased document-clustering technique as one of our performance benchmarks. Specifically, we employed the HAC algorithm based purely on the analysis of document contents and adopted TF×IDF as the feature selection method and document representation scheme. In addition, as with the proposed CFC technique, we estimated the similarity of two documents $d _ { i }$ and $d _ { j }$ by the cosine similarity measure and employed the groupaverage link method to measure the similarity between two clusters.

Summary of subjects' complete clusterings and personal folders

<table><tr><td rowspan="2"></td><td colspan="2">17 Subjects with complete clustering</td><td colspan="3">34 Subjects with personal folders</td></tr><tr><td>Number of folders generated</td><td>Number of documents in a folder</td><td>Number of documents organized</td><td>Number of folders generated</td><td>Number of documents in a folder</td></tr><tr><td>Maximum</td><td>39</td><td>125</td><td>44</td><td>16</td><td>12</td></tr><tr><td>Minimum</td><td>10</td><td>1</td><td>21</td><td>5</td><td>1</td></tr><tr><td>Average</td><td>19.47</td><td>22.34</td><td>28.85</td><td>9.18</td><td>3.14</td></tr></table>

![](/api/attachments/82SBHSYH/fulltext/images/2cb9ea0c35962e1de2a137eca81aa2ce9932819f7e4b14e8fea9161a2dd5f003.jpg)  
Fig. 3. Effects of feature size k for content-based document-clustering technique.

We also included the partial-clustering-based personalized document-clustering approach [46] as another performance benchmark. When the proposed CFC technique does not take into account the partial clusterings of other users $( \mathrm { i } . \mathrm { e } . , n \mathrm { = } 0 )$ , the CFC technique is based purely on a target user's partial clustering and simulates the partialclustering-based personalized document-clustering approach with the feature refinement method for document representation and the precluster-based HAC method for document clustering [46]. In the following, we denote our implementation of the specific partial-clustering-based personalized document-clustering technique as the CFC (n= 0) technique.

## 4.4. Parameter tuning

In the parameter-tuning experiments, we randomly chose manual document clustering results from four subjects (with complete clustering) to determine appropriate values for the parameters involved in each document-clustering technique investigated. To obtain more reliable tuning results, we expanded the number of trials, each of which included 80% of the documents randomly drawn from our CiteSeer corpus, and subsequently employed each document subset to estimate the effectiveness of each technique with specific combinations of parameter values. The described sampling-andclustering process was performed 10 times, and the overall effectiveness for each document-clustering technique was estimated by averaging the performance estimates obtained from the 10 individual sampling-andclustering processes.

## 4.4.1. Parameter tuning of content-based documentclustering technique

The content-based document-clustering technique involves the parameter of the number of features (k). We examined the effects of k, ranging from 200 to 2000 in increments of 200, on the effectiveness of the contentbased document-clustering technique. As we show in Fig. 3 (to reduce the complexity of the figure, we show only a subset of values for k), the PRT curve of the content-based technique moves in a favorable direction (i.e., toward to the upper-right corner) as k increases from 200 to 2000. Particularly, when we increase k from 200 to 1200, we record a significant performance improvement. However, any further increase of k (i.e., to 2000) has only a marginal effect on the clustering effectiveness. Therefore, we select 2000 as the feature size for the contentbased document-clustering technique.

## 4.4.2. Parameter tuning of CFC technique

The proposed CFC technique involves several parameters, including h and SigN (as required by the confidence function), n (the size of the neighborhood for $u _ { a } ) _ { : }$ λ (for the collaborative-based document similarity), β (the intercluster similarity threshold to create the extended partial clustering for $u _ { a } )$ , δ (the size threshold for eliminating small clusters from the extended partial clustering of $u _ { a } ) _ { : }$ , and k (the basis for determining the number of features in the consolidated feature set). To avoid overfitting the proposed CFC technique to our CiteSeer corpus and reduce the magnitude of parameter-tuning experiments, we set SigN to 10, λ to 0.5, β to 0.5, and δ to 2, in line with our preliminary experimental results. We then conducted the parameter-tuning experiments for h, n, and k for the CFC technique. Specifically, we investigated the effects of different levels of h (i.e., 0.7, 0.9, 1.1, 1.3, and 1.5), n (i.e., 5, 10, 15, and 20), and k (ranging from 200 to 2000 in increments of 200) on the clustering effectiveness of the CFC technique.

![](/api/attachments/82SBHSYH/fulltext/images/900899b67b427b8d627d957b75aa9503a0bec139b73a3caa2531988b09a36fba.jpg)  
Fig. 4. Effects of h for the CFC technique (using n = 5 and k = 1000).

When tuning the parameter h, we set n as 5 and k as 1000. Our evaluation results show that the CFC technique achieves better clustering effectiveness when h is equal to or less than 1.1 (see Fig. 4). However, the effects of h at the levels of 1.1, 0.9, and 0.7 are marginal. Hence, we select 1.1 for h. Subsequently, we examined the effects of n with h as 1.1 and k as 1000. As Fig. 5 shows, the CFC technique achieves the best effectiveness when n = 5. Any further increase of n (i.e., from 5 to 20) impairs the clustering effectiveness. Thus, we adopt 5 for n in subsequent experiments. Finally, we investigated the effects of different feature sizes (i.e., k);

our tuning results show that effects of k on clustering effectiveness of the CFC technique are marginal. Therefore, we select 1000 as the feature size for the CFC technique for subsequent experiments.

## 4.4.3. Parameter tuning of CFC (n=0) technique

As we mentioned previously, the CFC (n = 0) technique that simulates the partial-clustering-based personalized document-clustering technique with the feature refinement method for document representation and the precluster-based HAC method for document clustering serves as our benchmark technique. The CFC (n = 0) technique involves only one parameter, namely, the number of features k, as a basis to determine the number of features in the consolidated feature set. We investigated the effects of k, ranging from 200 to 2000 in increments of 200. Similar to the tuning results of the CFC technique, the effects of k across the range of values examined are marginal (see Fig. 6). Therefore, we also set the feature size for the CFC (n = 0) technique to 1000, consistent with the value adopted for the CFC technique.

![](/api/attachments/82SBHSYH/fulltext/images/e3510920a6add8bcd45519c20ed294f737619c3e41c4d71f1f8e4929c3c8d372.jpg)  
Fig. 5. Effects of n for the CFC technique (using h=1.1 and k=1000).

![](/api/attachments/82SBHSYH/fulltext/images/6bbf93a662acb7a6bbf244b5b0aae1149adbb9ebb7ab1b06180d67c66132fcfe.jpg)  
Fig. 6. Effects of k for the CFC (n = 0) technique.

## 4.5. Comparative evaluation

In our comparative evaluation, we compared the effectiveness of the proposed CFC technique with those of the content-based document-clustering technique and the partial-clustering-based personalized document-clustering technique (i.e., CFC (n = 0)). We first set the size of partial clustering pc (relative to the target document corpus) to 20% for each subject and used the manual document clusterings from all 17 subjects (with complete clustering) for our evaluation. As we show in Fig. 7, the CFC (with n=5) and CFC (n=0) techniques both outperform the content-based document-clustering technique. This empirical evaluation result suggests that the use of a user's partial clustering can lead to better personalized clustering than can the content-based document-clustering technique. Moreover, compared with the CFC (n= 0) technique, the use of the collaborative filtering approach (i.e., n = 5) to expand a user's partial clustering can improve clustering effectiveness further, as measured by cluster recall and cluster precision.

Because the PRT curve attained by each documentclustering technique forms a line in the cluster recall and cluster precision space, a statistical significant test between two lines is difficult, if not impossible. We therefore performed the significant test on the breakeven point attained by each technique. The breakeven point, an effectiveness measure commonly adopted by text categorization research [42], is defined as the value at which cluster recall equals cluster precision. We first identified, for every subject with complete clustering, the breakeven point attained by each technique. The average breakeven point achieved by the CFC technique with n=5 is 0.5992, noticeably higher than that attained by the partial-clustering-based personalized document-clustering (CFC (n= 0)) technique (i.e., 0.5673). The breakeven point of the content-based document-clustering technique is the worst, recording at 0.2597. We then conducted a paired t-test to test the statistical significance among the breakeven points of different document-clustering techniques. As we illustrate in Table 2, the proposed CFC technique with n=5 significantly outperforms the benchmark techniques at $p { < } 0 . 0 1$ . Similarly, the breakeven point attained by the CFC (n=0) technique is also significantly higher than that of the content-based document-clustering technique at $p { < } 0 . 0 1$

![](/api/attachments/82SBHSYH/fulltext/images/f535210e1a3305cca85fa71715232615350a7c29c2356c7d8198bb43cb3f1876.jpg)  
Fig. 7. PRT curves of different document-clustering techniques (pc = 20%).

Table 2  
Significant test (p-value) of different document-clustering techniques

<table><tr><td></td><td>Content-based</td><td>CFC (n= 0)</td><td>CFC (n=5)</td></tr><tr><td colspan="4">Content-based</td></tr><tr><td>CFC (n=0)</td><td>0.0000***</td><td></td><td></td></tr><tr><td>CFC (n=5)</td><td>0.0000***</td><td>0.0015***</td><td></td></tr></table>

<sup>⁎⁎⁎</sup> Significant at $p { < } 0 . 0 1$ on a two-tailed paired t-test.

We further examined the effects of different sizes of partial clustering (pc) relative to the target document corpus on the clustering effectiveness of the proposed CFC technique (with n = 5) and the partial-clusteringbased personalized document-clustering (i.e., CFC (n = 0)) technique. Specifically, we investigated percentages of documents in a partial clustering relative to the total number of documents in the target corpus, ranging from 20% to 5% in decrements of 5%. As we illustrate in Fig. 7 and 8a–b, when pc decreases from 20% to 10%, the CFC technique with $n { = } 5$ still outperforms the CFC (n = 0) technique. That is, in this range of $p c ,$ , the expansion of a user's partial clustering by those of his or her neighbors improves the clustering effectiveness of the proposed CFC technique. However, as we show in Fig. 8(c), with only 5% of the target corpus (i.e., 21.75 documents) in the partial clustering of a user, the clustering effectiveness of the CFC technique with $n { = } 5$ is comparable to that of the CFC (n= 0) technique. In other words, with such a small partial clustering, the CFC technique neither benefits nor suffers from taking other users' partial clusterings into account. Furthermore, across the range of partial clustering sizes, the CFC technique and the CFC (n= 0) technique considerably outperform the content-based document-clustering technique.

![](/api/attachments/82SBHSYH/fulltext/images/7a7f959955dfb41f019732220c56023db5461cf09eb05f325a3fa7bbe9a0dcf8.jpg)  
(a) $p c = 1 5 \%$

![](/api/attachments/82SBHSYH/fulltext/images/6531cb49b6c46c67ac49b411313153da475fc42ec6c5058b8db0496a9e30cbfa.jpg)  
(b) $p c = 1 0 \%$

![](/api/attachments/82SBHSYH/fulltext/images/fc925364dbf63ec706e52e76461d38336755bb263260133a5cfa3ea7e17a68fd.jpg)  
(c) $p c = 5 \%$  
Fig. 8. Effects of size of partial clustering (pc) on the CFC technique.

## 5. Conclusion and future research directions

Most existing document-clustering techniques, which generally are anchored in a pure content-based analysis, generate a single set of clusters for all users without tailoring them to individual users' preferences; thus, they are unable to support personalization. The partialclustering-based personalized document-clustering approach, which incorporates the target user's partial clustering into the document-clustering process, has been proposed to facilitate personalized document clustering [46]. However, given a collection of documents to be clustered, the user might have categorized only a small subset of the collection into his or her personal folders. In this case, the small partial clustering would degrade the effectiveness of the existing approach for this particular user. In response, we extend the partial-clustering-based personalized document-clustering approach and propose the collaborative filtering-based personalized documentclustering (CFC) technique, which expands the size of the user's partial clustering according to the partial clusterings of other users with similar categorization preferences. Our empirical evaluation results suggest that the proposed CFC technique outperforms the benchmarks, namely, the partial-clustering-based personalized and content-based document-clustering techniques. Moreover, with a small partial clustering established by a user, the proposed CFC technique generally achieves better clustering effectiveness than does the partialclustering-based personalized document-clustering technique.

Some ongoing and additional research directions are briefly discussed as follows. First, our evaluation study does not involve a large number of subjects or a large document corpus because of the significant amount of time that each subject (with complete clustering) required to complete the experiment. A future evaluation plan involving more subjects who will classify a larger document corpus is one of our research directions. Second, we concentrate on a user's personal folders organized nonhierarchically, even though users commonly organize their folders into a hierarchical structure. Therefore, the proposed CFC technique should be extended to accommodate users' folder hierarchies when estimating similarities of clustering preferences between users. Third, the CFC technique generates a flat set of document clusters. It would be desirable to extend the CFC technique to organize documents into hierarchical cluster structures. Fourth, this study assesses the similarity of the clustering preferences of two users on the basis of the degree of overlap between two sets of intracluster associations exhibited in the partial clusterings of the two persons. That is, the current similarity measure does not take into consideration the semantic relationships between documents and may suffer from a sparsity problem (i.e., the similarity between the clustering preferences of two users cannot be derived because they do not share common documents in their partial clusterings). To address this sparsity problem, we should attempt to exploit document semantic relationships in the described similarity measure. Fifth, the empirical evaluation of this study was conducted in a laboratory setting. Porting the proposed CFC technique to a digital library and performing empirical evaluations in a real-world setting represents an interesting research direction. Sixth, this study concentrates on the use of users' partial clusterings as a basis to support personalized document clustering. The development of alternative personalized document-clustering techniques that employ other information that may reflect personal categorization preferences would broaden the spectrum of general document-clustering research and, specifically, personalized document-clustering research.

## Acknowledgments

This work was supported in part by the MOE Program for Promoting Academic Excellence of Universities of the Republic of China under the grant 91-H-FA08-1-4 and by the National Science Council of the Republic of China under the grants NSC 94-2416-H-110-018 and 95- 2416-H-007-005.

## References

[1] M.R. Anderberg, Cluster Analysis for Applications, Academic Press, Inc., New York, 1973.

[2] M. Balabanovic, Y. Shoham, Fab: Content-based: Collaborative Recommendation, Communications of the ACM 40 (3) (1997) 66–72.

[3] D.K. Barreau, Context as a factor in personal information management systems, Journal of the American Society for Information Science 46 (5) (1991) 327–339.

[4] C. Basu, H. Hirsh, W. Cohen, Recommendation as classification: using social and content-based information in recommendation, Proceedings of the Workshop on Recommender Systems, AAAI Press, 1998, pp. 11–15.

[5] H. Billhardt, D. Borrajo, V. Maojo, A context vector model for information retrieval, Journal of the American Society for Information Science and Technology 53 (3) (2002) 236–249.

[6] D. Billsus, M.J. Pazzani, Learning collaborative information filtering, Proceedings of the Workshop on Recommender Systems, 1998.

[7] D. Boley, M. Gini, R. Gross, E. Han, K. Hastings, G. Karypis, V. Kumar, B. Mobasher, L. Moore, Partitioning-based clustering for web document categorization, Decision Support Systems 27 (3) (1999) 329–341.

[8] J.D. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative filtering, Proceedings of the 14th Conference on Uncertainty in Artificial Intelligence (UAI-98), San Francisco, CA, 1998, pp. 43–52.

[9] E. Brill, A simple rule-based part of speech tagger, Proceedings of the Third Conference on Applied Natural Language Processing, Trento, Italy, 1992, pp. 152–155.

[10] E. Brill, Some advances in rule-based part of speech tagging, Proceedings of the Twelfth National Conference on Artificial Intelligence (AAAI-94), Seattle, WA, 1994, pp. 722–727.

[11] D.O. Case, Conceptual organization and retrieval of text by historians: the role of memory and metaphor, Journal of the American Society for Information Science 42 (9) (1991) 657–668.

[12] D. Cutting, D. Karger, J. Pedersen, J. Tukey, Scatter/gather: a cluster-based approach to browsing large document collections, Proceedings of 15th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Copenhagen, Denmark, 1992, pp. 318–329.

[13] J. Deogun, V. Raghavan, User-oriented document clustering: a framework for learning in information retrieval, Proceedings of the 9th International ACM SIGIR Conference on Research and Development in Information Retrieval, 1986, pp. 157–163.

[14] J. Donovan, Patrons' expectations about collocation: measuring the difference between psychologically real and the really real, Cataloging and Classification Quarterly 13 (2) (1991) 23–43.

[15] S. Dumais, J. Platt, D. Heckerman, M. Sahami, Inductive learning algorithms and representations for text categorization, Proceedings of the 1998 ACM 7th International Conference on Information and Knowledge Management (CIKM '98), Bethesda, MD, 1998, pp. 148–155.

[16] A. El-Hamdouchi, P. Willett, Hierarchical document clustering using ward's method, Proceedings of ACM Conference on Research and Development in Information Retrieval, 1986, pp. 149–156.

[17] M. Gordon, User-based document clustering by redescribing subject description with a genetic algorithm, Journal of the American Society for Information Science 42 (5) (1991) 311–322

[18] V.P. Guerrero Bote, F. Moya Anegón, V. Herrero Solana, Document organization using Kohonen's algorithm, Information Processing and Management 38 (1) (2002) 79–89.

[19] J.L. Herlocker, J.A. Konstan, A. Borchers, J. Riedl, An algorithmic framework for preforming collaborative filtering, Proceedings of the 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Berkeley, CA, 1999, pp. 230–237.

[20] L. Kaufman, P.J. Rousseeuw, Finding Groups in Data: An Introduction to Cluster Analysis, John Wiley & Sons, New York, 1990.

[21] H. Kim, S. Lee, A semi-supervised document clustering technique for information organization, Proceedings of the 9th International Conference on Information and Knowledge Management, 2000, pp. 30–37.

[22] H. Kim, S. Lee, An effective document clustering method using user-adaptable distance metrics, Proceedings of the 2002 ACM Symposium on Applied Computing, 2002, pp. 16–20.

[23] T. Kohonen, Self-Organization and Associative Memory, Springer, Berlin, 1989.

[24] T. Kohonen, Self-Organizing Maps, Springer, Berlin, 1995

[25] J.A. Konstan, B.N. Miller, D. Maltz, J.L. Herlocker, L.R. Gordon, J. Riedl, GroupLens: applying collaborative filtering to usenet news, Communications of the ACM 40 (3) (1997) 77–87.

[26] B.H. Kwasnik, The importance of factors that are not document attributes in the organization of personal documents, Journal of Documentation 47 (1991) 389–398.

[27] K. Lagus, T. Honkela, S. Kaski, T. Kohonen, Self-organizing maps of document collections: a new approach to interactive exploration, Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Menlo Park, CA, 1996, pp. 238–243.

[28] G. Lakoff, Women, Fire and Dangerous Things: What Categories Reveal about the Mind, University of Chicago Press, Chicago, 1987.

[29] B. Larsen, C. Aone, Fast and effective text mining using lineartime document clustering, Proceedings of the 5th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 1999, pp. 16–22.

[30] C. Lin, H. Chen, J.F. Nunamaker, Verifying the Proximity and Size Hypothesis for Self-organizing Maps, Journal of Management Information Systems 16 (3), 1999–2000, 57–70.

[31] W.E. Mackay, Diversity in the use of electronic mail: a preliminary inquiry, ACM Transactions on Office Information Systems 6 (4) (1988) 380–397.

[32] W.E. Mackay, Responding to cognitive overload: co-adaptation between users and technology, Intellectica 30 (1) (2000) 177–193.

[33] P. Pantel, D. Lin, Document clustering with committees, Proceedings of the 25th International ACM SIGIR Conference on Research and Development in Information Retrieval, 2002, pp. 199–206.

[34] M.R. Quillian, Semantic memory, in: M. Minsky (Ed.), Semantic Information Processing, The MIT Press, Cambridge, MA, 1968, pp. 227–270.

[35] V. Raghavan, J. Deogun, Optimal determination of user-oriented clusters, Proceedings of the 10th International ACM SIGIR Conference on Research and Development in Information Retrieval, 1987, pp. 140–146.

[36] V.V. Raghavan, S.K. Wong, A critical analysis of vector space model for information retrieval, Journal of the American Society for Information Science 37 (5) (1986) 279–287.

[37] P. Resnick, N. Iacovou, M. Suchak, P. Bergstrom, J. Riedl, GroupLens: an open architecture for collaborative filtering of Netnews, Proceedings of the Conference on Computer Supported Cooperative Work (CSCW), Chapel Hill, NC, 1994, pp. 175–186.

[38] F.M. Restorick, Novel filing systems applicable to an automated office: a state-of-the-art study, Information Processing and Management 22 (1986) 151–172.

[39] D.G. Roussinov, H. Chen, Document clustering for electronic meetings: an experimental comparison of two techniques, Decision Support Systems 27 (1–2) (1999) 67–79.

[40] J. Rucker, M.J. Polanco, Siteseer: personalized navigation for the web, Communications of the ACM 40 (3) (1997) 73–75.

[41] B.M. Sarwar, G. Karypis, J.A. Konstan, J. Riedl, Analysis of Recommendation Algorithms for E-Commerce, Proceedings of the 2nd ACM Conference on Electronic Commerce, Minneapolis, MN, 2000, pp. 158–167.

[42] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002) 1–47.

[43] U. Shardanand, P. Maes, Social information filtering: algorithms for automating ‘word of mouth', Proceedings of Conference on Human Factors in Computing Systems, 1995, pp. 210–217.

[44] E.M. Voorhees, Implementing agglomerative hierarchical clustering algorithms for use in document retrieval, Information Processing and Management 22 (6) (1986) 465–476.

[45] A. Voutilainen, Nptool: a detector of english noun phrases, Proceedings of Workshop on Very Large Corpora, Columbus, OH, 1993, pp. 48–57.

[46] C. Wei, R.H.L. Chiang, C.C. Wu, Accommodating individual preferences in the categorization of documents: a personalized clustering approach, Journal of Management Information Systems 23 (2) (Fall 2006) 173–201.

[47] C. Wei, C.S. Yang, H.W. Hsiao, T.H. Cheng, Combining preference- and content-based approaches for improving document clustering effectiveness, Information Processing and Managemen 42 (2) (2006) 350–372.

[48] S.K. Wong, Y.Y. Yao, An information-theoretic measure of term specificity, Journal of the American Society for Information Science 43 (1) (1992) 54–61.

[49] Y. Yang, J.O. Pedersen, A comparative study on feature selection in text categorization, Proceedings of 14th International Conference on Machine Learning, Nashville, TN, 1997, pp. 412–420.

[50] C.T. Yu, Y.T. Wang, C.H. Chen, Adaptive Document Clustering, Proceedings of the 8th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Montreal, Quebec, Canada, 1985, pp. 197–203.

![](/api/attachments/82SBHSYH/fulltext/images/0a6a49204f0e9b09429e799224864b521d85588b19b203722f4a5849a59920d7.jpg)

Chih-Ping Wei received a BS in Management Science from the National Chiao-Tung University in Taiwan, R.O.C. in 1987 and an MS and a Ph.D. in Management Information Systems from the University of Arizona in 1991 and 1996. He is currently a professor of Institute of Technology Management at National Tsing Hua University in Taiwan, R.O.C. Prior to joining the National Tsing Hua University in 2005, he was a faculty member at Department of Information Management at National Sun

Yat-sen University in Taiwan since 1996 and a visiting scholar at the University of Illinois at Urbana-Champaign in 2001. His papers have appeared in Journal of Management Information Systems, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, Cybernetics, IEEE Transactions on Information Technology in Biomedicine, European Journal of Information Systems, Journal of Database Management, Information Processing and Management, and Journal of Organizational Computing and Electronic Commerce, etc. His current research interests include knowledge discovery and data mining, information retrieval and text mining, knowledge management, multidatabase management and integration, and data warehouse design. He has co-guest edited or editing special issues of International Journal of Electronic Commerce, Electronic Commerce Research and Applications, and Decision Support Systems. He can be reached at the Institute of Technology Management, National Tsing Hua University, Hsinchu, Taiwan, R.O.C; cpwei@mx.nthu.edu.tw.

![](/api/attachments/82SBHSYH/fulltext/images/c7d679f6c0e9a342c237f9fcbf7dc650e0b64e59021a346e0f933b45f81996eb.jpg)

Chin-Sheng Yang received a BS in Management Information Systems from the National Chengchi University in Taiwan, R.O.C. in 2000 and a MBA in Management Information Systems from the National Sun Yat-sen University in Taiwan, R.O.C. in 2002. He is currently a doctoral student in the Department of Information Management at National Sun Yat-sen University. His papers have appeared (including forthcoming) in Decision Support Systems and Information Processing and Man-

agement. His current research interests include text mining, information retrieval, and knowledge discovery and data mining. He can be reached at the Department of Information Management, National Sun Yat-sen University, Kaohsiung, Taiwan, R.O.C.; litony@mis.nsysu.edu.tw.

![](/api/attachments/82SBHSYH/fulltext/images/e7403b351f9100910d72c9d74b7ee50db3721d6b866ba61f1d5bf6d13c7f47a5.jpg)

Han-Wei Hsiao received a BS degree in Mathematics from Tunghai University in Taiwan, R.O.C. in 1990, an MS degree in Information Science from National Chiao-Tung University in Taiwan, R.O.C. in 1994, and a Ph.D. in Management Information Systems from the National Sun Yat-Sen University in Taiwan, R.O.C. in 2004. He is currently an assistant professor of Department of Information Management at National University of Kaohsiung in Taiwan, R.O.C.

His papers have appeared (including forthcoming) in Decision Support Systems, Information Processing and Management, Journal of Information Management, Journal of Internet Technology, etc. His current research interests include data mining, text mining, network management, and network security. He can be reached at the Department of Information Management at National University of Kaohsiung, Kaohsiung County, Taiwan, R.O.C; hanwei@nuk.edu.tw.
