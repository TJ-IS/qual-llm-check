---
otero_id: 11574
otero_key: "4D6HWRF7"
title: "Accommodating Individual Preferences in the Categorization of Documents: A Personalized Clustering Approach"
authors: "Chih-Ping Wei; Roger H.L. Chiang; Chia-Chen Wu"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222230208"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Accommodating Individual Preferences in the Categorization of Documents: A Personalized Clustering Approach

Chih-Ping Wei , Roger H.L. Chiang & Chia-Chen Wu

To cite this article: Chih-Ping Wei , Roger H.L. Chiang & Chia-Chen Wu (2006) Accommodating Individual Preferences in the Categorization of Documents: A Personalized Clustering Approach, Journal of Management Information Systems, 23:2, 173-201

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222230208

![](/api/attachments/4D6HWRF7/fulltext/images/650cd5479130d7266e0443f142e38baafea184230464041823eced4155e9cd8b.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/4D6HWRF7/fulltext/images/3a5884efa855618743fda717376851c86751bf6eeb11c81b9765054021f1b8f2.jpg)

Submit your article to this journal

![](/api/attachments/4D6HWRF7/fulltext/images/fa7bd79210d26c2c5dcb82bdf2825245e2a952b3847693934c7df87ed3943dbd.jpg)

Article views: 20

![](/api/attachments/4D6HWRF7/fulltext/images/28f8a7cc5a4b1630bcfd4875d4202a619ddec3d65f518193d7a455f6b5d63991.jpg)

View related articles

# Accommodating Individual Preferences in the Categorization of Documents: A Personalized Clustering Approach

CHIH-PING WEI, ROGER H.L. CHIANG, AND CHIA-CHEN WU

CHIH-PING WEI is a Professor at the Institute of Technology Management, National Tsing Hua University, Taiwan. He was a faculty member at the Department of Information Management at National Sun Yat-sen University in Taiwan between 1996 and 2005. He received a B.S. in Management Science from the National Chiao-Tung University in Taiwan in 1987 and an M.S. and a Ph.D. in Management Information Systems from the University of Arizona in 1991 and 1996. His current research interests include knowledge discovery and data mining, text mining, knowledge management, multidatabase management and integration, and data warehouse design. His papers have appeared in IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, Decision Support Systems, European Journal of Information Systems, Information Processing and Management, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Information Technology in Biomedicine, Journal of Database Management, and Journal of Organizational Computing and Electronic Commerce, among others.

ROGER H.L. CHIANG is an Associate Professor of Information Systems at College of Business, University of Cincinnati. He received his B.S. in Management Science from National Chiao-Tung University, Taiwan, an M.S. in Computer Science from Michigan State University and in Business Administration from the University of Rochester, and a Ph.D. in Computers and Information Systems from the University of Rochester. His research interests are in data and knowledge management and intelligent systems, particularly in database reverse engineering, database integration, data and text mining, document classification and clustering, domain knowledge discovery, and semantic information retrieval. His research has been published in a number of journals, including ACM Transactions on Database Systems, DATA BASE for Advances in Information Systems, Data & Knowledge Engineering, Decision Support Systems, Journal of Database Administration, and Very Large Data Base. He is the senior editor of the DATA BASE for Advances in Information Systems, and the Associate Editor of the Journal of AIS, Journal of Database Management, International Journal of Intelligent Systems in Accounting, Finance and Management, and MIS Quarterly. He was the program cochair of the Twenty-Second International Conference on Information Systems, Research in Progress Track, 2001, and ACM International Workshop on Web Information and Data Management in 2001, 2002, and 2003.

CHIA-CHEN WU is a Senior Engineer in the OPE8S Central Manufacturing Planning Division, United Microelectronics Corporation, Taiwan. She received a B.S. and an

MBA in Management Information Systems from National Sun Yat-sen University, Taiwan, in 2001 and 2003, respectively. Her research interests include data mining, text mining, and knowledge management.

ABSTRACT: As electronic commerce and knowledge economy environments proliferate, both individuals and organizations increasingly generate and consume large amounts of online information, typically available as textual documents. To manage this ever-increasing volume of documents, individuals and organizations frequently organize their documents into categories that facilitate document management and subsequent access and browsing. Document clustering is an intentional act that should reflect individual preferences with regard to the semantic coherency and relevant categorization of documents. Hence, effective document clustering must consider individual preferences and needs to support personalization in document categorization. In this paper, we present an automatic document-clustering approach that incorporates an individual’s partial clustering as preferential information. Combining two document representation methods, feature refinement and feature weighting, with two clustering methods, precluster-based hierarchical agglomerative clustering (HAC) and atomic-based HAC, we establish four personalized document-clustering techniques. Using a traditional content-based document-clustering technique as a performance benchmark, we find that the proposed personalized document-clustering techniques improve clustering effectiveness, as measured by cluster precision and cluster recall.

KEY WORDS AND PHRASES: cognitive overload, document clustering, hierarchical agglomerative clustering (HAC), personalization, personalized document clustering, supervised document clustering, text mining.

ADVANCES IN INFORMATION TECHNOLOGIES have fostered the development and proliferation of electronic commerce and knowledge economies. In this emerging environment, organizations generate and consume tremendous amounts of online information, which typically is available as textual documents. Consequently, the effective management of the escalating volume of online textual documents is critical to today’s businesses. Meanwhile, individuals increasingly search on the Internet for relevant or important documents and generally need to archive them for future use. Thus, effective document management is also desirable at the individual level.

Document management practices suggest the popularity of using categories (e.g., clusters, folders) for organizing, archiving, and retrieving documents. Traditionally, individuals have been able to organize their documents manually because the size of the document collection generally is cognitively manageable. However, the sheer volume and availability of online documents to be managed often make the manual clustering approach prohibitively tedious and unpractical, in terms of time and cognitive efforts. An automated document-clustering approach, representing an appealing alternative, groups relevant documents into distinct categories typically on the basis of their content. Each cluster represents a coherent subtopic in the document collection.

According to the context theory of classification, the document-clustering behaviors of individuals not only involve the attributes (including contents) of documents but also depend on who is doing the task and in what context [2, 6, 21, 23, 30]. As a result, document clustering is an intentional act that reflects individuals’ preferences with regard to the semantic coherency or relevant categorization of documents [34]. That is, individuals typically have unique clustering preferences and needs. For example, given a set of research articles, some researchers prefer organizing by research domains (e.g., databases, data mining, network security, electronic commerce), whereas others prefer categories based on research methods (e.g., surveys, experiments, case studies). Furthermore, even when the same categorization schemes are used, the specificity of categories may vary with different researchers. For example, some researchers may use only one category for all papers related to data mining, whereas others may employ a set of increasingly specific categories (e.g., classification analysis, clustering analysis, association rules, sequential patterns) for the same collection of articles.

Document-clustering research traditionally has been anchored in the analyses of document content (i.e., the classical approach). As a consequence, existing document-clustering techniques create a set of clusters that are not tailored to individuals’ categorization preferences and therefore are not able to facilitate personalization. The categorization scheme exhibited in such nonpersonalized clusters may not conform to that of an individual’s expectations and perceptions. However, an individual’s document search typically is guided by his or her own categorization scheme [10, 32]. Thus, when searching documents using a one-for-all categorization scheme, an individual generally entails a semantic internalization process [29] to comprehend the target categorization scheme or experiences coadaptation (i.e., adjusts his or her behavior to the more effective use of a technology and, at the same time, reinterprets and adapts the technology to his or her needs) to address cognitive overload [26, 27]. The semantic internalization and coadaptation processes unnecessarily increase the cognitive load of the individual. Consequently, the individual might spend more time or even have difficulties locating documents of interest because he or she must comprehend the one-for-all categorization scheme and adjust his or her categorization perceptions accordingly. Likewise, when the individual follows a one-for-all categorization scheme for organizing documents, he or she consumes more cognitive effort in determining the appropriate categories for these documents or even classifies documents into inappropriate categories, leading to possible ineffectiveness or inefficiency of future retrievals.

To address individuals’ cognitive load that results from the use of a one-for-all categorization scheme produced by traditional document-clustering techniques, effective document clustering must consider individual preferences to support personalized document clustering [9, 13, 17]. Motivated by the urgent need for such a personalized document-clustering approach, we strive to extend document clustering beyond content-based analysis by soliciting and incorporating an individual’s partial clustering as his or her categorization preference in the document-clustering process.

Let D be a set of documents to be clustered. In this research, partial clustering, which is assumed to be readily available, refers to the individual’s categorization of a small subset of documents in D. For example, some digital libraries or online information providers offer personal bookshelves (e.g., “my bookshelf,” “my favorites,” “my eNews”) to users so that they can organize documents into their personal folders. When a set of documents is retrieved and must be clustered for a particular user, some of the documents in the set may have been previously organized in his or her personal folders. Thus, partial clustering is available and can be employed to facilitate subsequent personalized document clustering.

In this research, we propose a personalized document-clustering approach that is based on an individual’s partial clustering and experimentally evaluate the effectiveness of our approach in comparison with a traditional document-clustering technique.

## Literature Review

## Content-Based Document Clustering

TRADITIONAL DOCUMENT-CLUSTERING TECHNIQUES group documents on the basis of the contents of those documents. The documents in the resultant cluster exhibit maximal similarity to those in the same cluster and share minimal similarity with documents in other clusters. As shown in Figure 1, a content-based document clustering process generally comprises three main phases—feature extraction and selection, document representation, and clustering [42, 43].

Feature extraction begins with the parsing of each source document to produce a set of nouns and noun phrases (commonly referred to as “features”) and exclude a list of prespecified “stop words” that are non-semantic-bearing words. Subsequently, representative features are selected from the set of extracted features. Feature selection is important for clustering efficiency and effectiveness, because it not only condenses the size of the extracted feature set but also reduces the potential biases embedded in the original (i.e., nontrimmed) feature set [33, 45]. Commonly used feature selection metrics include (1) term frequency (TF), which denotes the occurrence frequency of a particular term in the document collection; (2) TF×IDF (inverse document frequency), where IDF is measured by log(N/DF), N is the number of documents in the collection, and DF is the number of documents that include the particular term; and (3) their hybrids [3, 24].

As measured by a particular feature selection metric (i.e., TF, TF×IDF, or a hybrid), the k features with the highest selection metric scores then are selected to represent the documents. Based on the chosen representation scheme, each document is described in the k-dimensional space and represented as a feature vector. Commonly employed document representation schemes include binary (which considers simply the presence or absence of a feature in a document), TF (as within-document term frequency), and TF×IDF [3, 24, 28, 33, 43].

In the final phase of document clustering, source documents are grouped into distinct clusters on the basis of the selected features and their respective values in each document. Common approaches for document clustering include partitioning-based [3, 7, 24, 38], hierarchical [12, 33, 39, 40, 43], and Kohonen neural network [22, 25,

![](/api/attachments/4D6HWRF7/fulltext/images/bb765d65e03536b6d49c8ae6d69537d9292c6442931fb5ecf922fbb36dfec03c.jpg)  
Figure 1. General Process of Content-Based Document Clustering

33]. The partitioning-based approach partitions a set of documents into multiple, nonoverlapping clusters. Given a specified number of clusters, it creates an initial partitioning and then attempts to improve the partitioning iteratively by moving documents among clusters. Common partitioning-based algorithms include k-means [1] and PAM (partitioning around medoids) [16].

The hierarchical clustering approach builds a binary clustering hierarchy whose leaf nodes represent source documents to be clustered. Hierarchical clustering methods can be classified further into agglomerative or divisive clustering, depending on whether the clustering hierarchy is formed in a bottom-up or top-down fashion. The hierarchical agglomerative clustering (HAC) algorithm [40], which exemplifies a bottom-up strategy, starts with as many clusters as there are documents. On the basis of a specific intercluster similarity measure of choice (e.g., single link, complete link, group average link, Ward’s method), the two most similar clusters are then merged to form a new cluster. This merging process continues until either a hierarchy, in which a single cluster remains at the top of the hierarchy that contains all the target documents, emerges or a termination condition (e.g., the intercluster similarity is less than a prespecified threshold) holds. In contrast, the hierarchical divisive clustering algorithm [16], which employs a top-down strategy, starts with all the documents in one cluster. The cluster is then subdivided into the two most distinct clusters. The division process is repeated until either each document forms a cluster of its own or a termination condition (e.g., the intracluster similarity of each cluster is greater than a prespecified threshold) is satisfied.

A Kohonen neural network [19, 20, 31], also known as a self-organizing map, is an unsupervised two-layer neural network in which each input node corresponds to a coordinate axis in the input attribute vector space. Each output node represents a node in a two-dimensional grid. The network is fully connected; that is, each output node is connected to each input node with a connection weight. During the neural network training phase, documents to be clustered are fed into the network repeatedly to adjust the connection weights such that the distribution of the output nodes represents that of the input objects.

## Non-Content-Based and Hybrid Approaches

Prior research has proposed non-content-based and hybrid document clustering approaches [9, 18, 47] that could be applied for personalized document clustering. For example, Yu et al. [47] propose the adaptive document-clustering technique, a noncontent-based approach, which captures individuals’ perceptions of the closeness between documents based on those documents’ relevance to user queries. To support personalization for a target individual, all queries should be associated with that individual. Given a document collection $D = \{ d _ { 1 } , d _ { 2 } , . . . , d _ { n } \}$ to be clustered and a set of user queries $Q = \{ q _ { 1 } , q _ { 2 } , . . . . , q _ { m } \}$ (assume that the set of retrieved and relevant documents for each $q _ { j }$ is $D _ { q j } ) _ { \ d j }$ , the adaptive document-clustering technique proceeds as follows. Each document $d _ { i }$ is initially assigned to an arbitrary position on a real line. Subsequently, for each query $q _ { j } ,$ the centroid $x _ { q j }$ of the positions of all documents in $D _ { q j }$ is calculated. Accordingly, every document $d _ { i }$ in $D _ { q j }$ moves toward $x _ { q j } ,$ where the amount of movement is proportional to the distance between the positions of $d _ { i }$ and $x _ { q j } .$ . This process is referred to as a converging operation. However, the positions of all documents in $D$ eventually may bunch together if the converging operation is repeated for many different queries. To avoid such an outcome, after the execution of the converging operation for a query $q _ { j } ,$ the adaptive document-clustering technique performs a pulling operation by randomly selecting a subset of documents $D _ { s }$ from $D$ and moving each document in $D _ { s }$ away from the centroid of $D _ { s }$ by the amount proportional to the distance between the document and the centroid of $D _ { s }$ . The converging and pulling operations are executed for all queries in $Q .$ Finally, the clusters for the documents in D are determined. Specifically, if the distance between two adjacent documents is less than a prespecified threshold, these two documents are considered to belong to the same cluster; otherwise, they belong to different clusters. On the basis of this partitioning criterion, all documents in D can be segmented into clusters.

Deogun and Raghavan [9] propose a user-oriented document-clustering technique, which is also based solely on information about document relevance to user queries. Its process consists of two main phases—divisive and merging. In the divisive phase, the document collection $D$ is divided into several clusters according to the documents’ relevance to the set of user queries Q. Initially, $D$ is assumed to form a single cluster. As the first query $q _ { 1 }$ is processed, the cluster divides into two clusters that correspond to the relevant and irrelevant sets for $q _ { 1 }$ . When a new query $q _ { i }$ is processed, each existing cluster that has a nonempty intersection with $D _ { q i }$ is divided into two clusters (relevant and irrelevant). The division process continues until all queries in $Q$ are processed.

In the merging phase, the clusters obtained previously are combined to form larger clusters. For each cluster $C _ { i }$ produced in the divisive phase that has not been combined, its affinity to every other cluster $C _ { j }$ is calculated on the basis of whether their constituent documents co-occur in the set of relevant documents for each query. Accordingly, $C _ { i }$ is combined with the cluster with which its affinity is maximal and satisfies a predefined threshold. After the merging phase processes all the clusters generated in the divisive phase, the document-clustering process concludes, and the resultant clusters represent the clusters for the document collection D.

Kim and Lee [18] propose a semisupervised document-clustering technique. It is a hybrid approach that considers not only content similarity but also users’ perceptions of document similarity using a relevance feedback mechanism.<sup>1</sup> This hybrid clustering technique can also support personalized document clustering. It consists of preclustering, supervising, and reclustering phases. The preclustering phase, which employs the HAC algorithm, puts each document into a separate cluster and merges those two clusters whose merger produces the smallest increase in diameter. The merging process then repeats until the diameter of the merged clusters reaches a given threshold. Each of such resultant clusters is referred to as a “precluster.” Subsequently, the supervising phase involves obtaining relevance feedback from a user for cluster formation in the later phase. It determines the training document set T that includes all documents within preclusters of fewer than η documents. Accordingly, a document $d _ { i }$ in $T$ is randomly selected to serve as the query. Using this query, a set of documents in T is retrieved and presented to the user, who then judges whether each of the retrieved documents is relevant to the query $( \mathrm { i } . \mathrm { e } . , d _ { i } )$ . Thus, two types of document bundles are formed for $d _ { i } \mathbf { : }$ positive and negative. The documents in the positive bundle, which the user has judged as relevant to $d _ { i } ,$ are placed in the same cluster as $d _ { i } ,$ whereas the documents in its negative bundle must be located in clusters other than $d _ { i } .$

The final reclustering phase involves the formation of clusters for the entire document collection. The preclusters created in the first phase are assigned to the nearest positive bundle. For every precluster assignment, larger clusters are generated, and the set of local cluster prototypes is incrementally updated. Finally, each residual document that has not been retrieved or has been ignored during the relevance feedback process is assigned to the cluster with the nearest local prototype. At this point, documents in negative bundles are examined to verify if they are located in the same clusters. If such documents are found, each is reassigned to the cluster with the document’s second-nearest local prototype.

Both non-content-based (i.e., adaptive and user-oriented techniques) and hybrid (i.e., semisupervised techniques) document-clustering approaches exploit document relevance to queries in their clustering process. However, these techniques encounter several limitations in support of personalized document clustering. First, to be feasible, non-content-based document-clustering techniques assume that all documents in the collection $D$ to be clustered must appear in at least one set of relevant documents for a user query. If a document is considered irrelevant to all queries, its similarity with other documents in D cannot be estimated. As the size of D expands, the number of documents considered irrelevant to all queries increases, creating a serious problem in both techniques. Second, document relevance to queries is often associated with query contexts. For example, in response to the same query, a document may be considered relevant from an e-commerce perspective but irrelevant from a business-to-business (B2B) viewpoint. Therefore, heterogeneity in query contexts may constrain the effectiveness of these approaches for facilitating personalized document clustering. Third, although Kim and Lee’s [18] empirical results suggest that their proposed approach outperforms a traditional content-based document-clustering technique, real-time relevance feedback from an individual can be both timeconsuming and impractical.

## Design of Personalized Document-Clustering Approach

IN RESPONSE TO THE SHORTCOMINGS and limitations of existing document-clustering techniques in terms of accommodating individual categorization preferences, we propose a personalized document-clustering approach that incorporates an individual’s partial clustering, which should be readily available from an individual’s personal folders. The proposed personalized document-clustering approach concentrates on an individual’s partial clustering, organized nonhierarchically, and generates a flat set rather than a hierarchy of document clusters. Thus, the proposed approach consists of three main phases: (1) feature extraction, selection, and consolidation; (2) document representation; and (3) clustering, as shown in Figure 2. In comparison with contentbased document clustering (see Figure 1), our approach includes partial clustering as an additional input. In Figure 2, the shaded components (feature selection, feature consolidation, document representation, and clustering) depict the extensions of our proposed approach.

## Feature Extraction, Selection, and Consolidation Phase

The proposed personalized document-clustering approach starts with feature extraction, which is language dependent. In this research, we implemented two separate feature extraction mechanisms for English and Chinese documents, respectively. For English documents, we adopted the rule-based part-of-speech tagger proposed by Brill [4, 5] to syntactically tag each word in the documents. To extract noun phrases from syntactically tagged documents, we implemented a noun phrase parser, as proposed by Voutilainen [41]. For documents written in Chinese, we employed a hybrid approach that combines dictionary-based and statistical methods (specifically, a mutual information measure) [44] for Chinese term extraction.

In the proposed approach, feature selection first determines the representative features for the entire document collection. We used $T F { \times } I D F$ as the feature selection metric, due to its popularity in document-clustering research [24, 28, 33, 35]. The set of top $k _ { 1 }$ features is selected and referred to as $A L L \_ T F { \times } I D F$ . In addition, because the partial clustering represents an individual’s categorization preference, the extraction and use of a personal categorization scheme (i.e., the set of features that best differentiates each cluster from others) during the document-clustering process should improve the clustering effectiveness. In this vein, the feature selection or dimensionality reduction, a process similar to that in text categorization, is performed on the partial clustering provided by the target individual. Common feature selection metrics for text categorization include document frequency, $\chi ^ { 2 }$ statistic, information gain, and mutual information [37, 46], whereas latent semantic indexing (LSI) is the most wellknown dimensionality reduction method [8, 37]. As shown by Yang and Pedersen [46], the categorization effectiveness achieved by the $\chi ^ { 2 }$ statistic metric is comparable to that of information gain and better than that of mutual information. On the other hand, Schütze et al. [36] experimentally compared the LSI-based dimensionality reduction method for text categorization with the $\chi ^ { 2 }$ statistic–based feature selection method and showed that both methods attained comparable categorization effectiveness when a neural network was used as the underlying learning technique. Accordingly, we employed the $\chi ^ { 2 }$ statistic metric for determining, from the partial clustering, a set of features (denoted Partial $\chi ^ { 2 } )$ that represents the personal categorization scheme.

![](/api/attachments/4D6HWRF7/fulltext/images/27487bb347876a94cb8584b3f65c4f934cd5844bf6e99687133fe175289d7efa.jpg)  
Figure 2. Process of the Personalized Document-Clustering Approach

The $\chi ^ { 2 }$ statistic, which measures the dependence between a feature $f _ { j }$ and a partial cluster $C _ { i } ,$ , tends to 0 when $f _ { j }$ and $C _ { i }$ are independent and to 1 when $f _ { j }$ and $C _ { i }$ are highly relevant. Using a two-way contingency table of a feature $f _ { j }$ and a cluster $C _ { i } ,$ let $n _ { r + }$ be the number of documents in the cluster $C _ { i }$ in which the feature $f _ { j }$ occurs, $n _ { r _ { - } }$ be the number of documents in $C _ { i }$ in which $f _ { j }$ does not appear, $n _ { n + }$ be the number of documents in clusters other than $C _ { i }$ in which $f _ { j }$ occurs, $n _ { n - }$ be the number of documents in clusters other than $C _ { i }$ in which $f _ { j }$ does not appear, and n be the total number of documents included in partial clusters. The $\chi ^ { 2 }$ statistic of $f _ { j }$ relevant to $C _ { i }$ thus is defined as follows [46]:

$$
\chi^ {2} \left(f _ {j}, C _ {i}\right) = \frac {n \times \left(n _ {r +} n _ {n -} - n _ {r -} n _ {n +}\right) ^ {2}}{\left(n _ {r +} + n _ {r -}\right) \left(n _ {n +} + n _ {n -}\right) \left(n _ {r +} + n _ {n +}\right) \left(n _ {r -} + n _ {n -}\right)}.\tag{1}
$$

Once the $\chi ^ { 2 }$ statistic of the feature $f _ { j }$ relevant to each partial cluster $C _ { i }$ is derived, the overall $\chi ^ { 2 }$ statistic of $f _ { i }$ for all partial clusters is calculated using the weighted average scheme [46]. That is, $\chi ^ { 2 } ( f _ { j } , M ) = \Sigma _ { C _ { i } \in M } p ( C _ { i } ) \times \chi ^ { 2 } ( f _ { j } , C _ { i } )$ , where M refers to the set of all partial clusters, and $p ( C _ { i } )$ is the number of documents in $C _ { i }$ divided by n. Accordingly, the top $k _ { 2 }$ features with the highest weighted average o $\chi ^ { 2 }$ statistic scores are selected and included in Partial $\mathcal { X } ^ { 2 }$

Furthermore, we consider frequent but nonrepresentative features in partial clusters to be irrelevant to the categorization scheme for the entire document corpus. Thus, on the basis of the TF selection metric, we select the top $k _ { 3 }$ features (denoted Partial\_TF) from the documents in the partial clustering. The features in the set (Partial\_ $T F -$ $P a r t i a l _ { - } \chi ^ { 2 } )$ are frequent but nonrepresentative features whose inclusion in the document-clustering process may deteriorate the clustering effectiveness.

The third task in this phase, feature consolidation, determines the most relevant features by considering ALL\_TF×IDF, Partial\_ $\mathcal { X } ^ { 2 } ,$ and Partial\_TF. The set of features in Partial $\mathcal { X } ^ { 2 }$ reflects the individual’s document-clustering preferences and must be included for personalized document clustering. The features in (Partial $. T F -$ Partial $\mathcal { X } ^ { 2 } )$ , in contrast, are nondiscriminative features with respect to the partial clustering and therefore should be excluded. Accordingly, the consolidated feature set employed for personalized document clustering is shown in formula (2):

$$
\begin{array}{c} \left(A L L _ {-} T F \times I D F - \left(P a r t i a l _ {-} T F - P a r t i a l _ {-} \chi^ {2}\right)\right) \cup P a r t i a l _ {-} \chi^ {2} \\ = \left(A l l _ {-} T F \times I D F - P a r t i a l _ {-} T F\right) \cup P a r t i a l _ {-} \chi^ {2}. \end{array}\tag{2}
$$

## Document Representation Phase

Each document in the collection is represented by features of the consolidated feature set. Although we initially considered both the $T F { \times } I D F$ and binary schemes, our preliminary evaluation results suggested that the $T F { \times } I D F$ scheme generally outperformed the binary one. Therefore, we adopted TF×IDF as the underlying document representation scheme for our proposed approach. Furthermore, we propose two methods by considering whether a weight is associated with each feature in the consolidated feature set. The first method gives an equal weight (e.g., 1) to all features in the consolidated feature set. Because the consolidated feature set is refined from $A L L \_ T F { \times } I D F$ , this equal-weighting method is referred to as feature refinement. Specifically, in the feature refinement method, each document $d _ { i }$ is described by a feature vector $\vec { d } _ { i }$ as

$$
\vec {d} _ {i} = \left\langle v _ {i 1}, v _ {i 2}, \dots , v _ {i t} \right\rangle ,\tag{3}
$$

where t is the total number of features in the consolidated feature set, and $\nu _ { i j }$ is the $T F \times I D F$ of feature $f _ { j }$ in document $d _ { i } .$

The feature refinement method does not consider the degree of importance of each feature in clustering documents and is essentially identical to its underlying representation scheme $( \mathrm { i . e . , } T F { \times } I D F )$ . Conceivably, a feature with greater power to differentiate the partial clusters should be more important (i.e., given greater weight) than one with less discriminatory power. Therefore, we also developed a feature weighting method for document representation. If the feature $f _ { j }$ belongs to Partial $\mathcal { X } ^ { 2 } .$ , the weight $w _ { j } \mathrm { o f } f _ { j } \mathrm { i }$ is its $\chi ^ { 2 }$ statistic, which is derived from the partial clusters $( \mathrm { i . e . , } w _ { j } = \chi ^ { 2 } ( f _ { j } , M )$ if $f _ { j } \in P a r t i a l _ { - } \chi ^ { 2 } )$ . If the feature $f _ { j }$ is in the consolidated feature set but does not belong to Partial $\mathcal { X } ^ { 2 }$ , its weight $w _ { j }$ is derived on the basis of the weights of the features in Partial $\mathcal { X } ^ { 2 } .$ . Specifically, we assign an equal weight $( \mathrm { i . e . }$ , the average of the weights of all features in Partial $- \chi ^ { 2 } )$ to each of these features; that is,

$$
w _ {j} = \frac {1}{\left| P a r t i a l \_ \chi^ {2} \right|} \sum_ {f _ {h} \in P a r t i a l \_ \chi^ {2}} w _ {h} \text {   if   } f _ {j} \notin P a r t i a l \_ \chi^ {2}.
$$

Accordingly, in the feature weighting method, each document $d _ { i }$ is described by a feature vector $\vec { d } _ { i }$ as

$$
\vec {d} _ {i} = \left\langle v _ {i 1} \times w _ {1}, v _ {i 2} \times w _ {2},..., v _ {i t} \times w _ {t} \right\rangle ,\tag{4}
$$

where $\nu _ { i j }$ is as defined in formula (3).

## Clustering Phase

Among the common document-clustering approaches (including partitioning-based, hierarchical, and Kohonen neural network), hierarchical clustering has an advantage over partitioning-based clustering, in that the number of clusters need not be prespecified and can be decreased (or increased) by simply moving up (or down) the resultant clustering hierarchy. Furthermore, the hierarchical clustering approach might achieve clustering effectiveness comparable to the Kohonen neural network [33]. Therefore, our proposed personalized document-clustering approach uses the hierarchical algorithm (specifically, HAC) as its underlying clustering technique.

With the availability of an individual’s partial clustering, two different clustering methods can be developed. The first method treats each document as an individual cluster and applies the HAC algorithm to generate document clusters. Because this method starts the document clustering at the atomic (single-document) level, it is referred to as the atomic-based HAC method, whose detailed algorithm is shown in

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure Atomic-Based HAC (R: a set of documents;  $\alpha$ : an intercluster similarity threshold)
Begin
    A = ∅;
    For each document  $d_{i}$  in R /* form each document as an initial cluster */
    A = A ∪ {{ $d_{i}$ }};
    Cluster-Merging(A,  $\alpha$ );
    Return A;
End.

Procedure Cluster-Merging (A: a set of document clusters;  $\alpha$ : an intercluster similarity threshold)
Begin
    Repeat
    TargetM₁ = nil; TargetM₂ = nil; MaxSim = 0;
    For each cluster Cᵢ in A
    For each cluster Cⱼ in A where Cⱼ ≠ Cᵢ
    /* Compute the intercluster similarity between Cᵢ and Cⱼ based on the group-average link method */
    Intercluster-Sim(Cᵢ, Cⱼ) =  $\frac{1}{|C_i| \times |C_j|} \sum_{p \in C_i \atop p \in C_j} sim(p,q)$ ;
    If Intercluster-Sim(Cᵢ, Cⱼ) &gt; MaxSim
    Then TargetM₁ = Cᵢ, TargetM₂ = Cⱼ and MaxSim = Intercluster-Sim(Cᵢ, Cⱼ);
    End-for;
    End-for;
    If MaxSim ≥  $\alpha$ 
    Then
    Merge TargetM₁ and TargetM₂ into one cluster (i.e., A = (A ∪ {TargetM₁ ∪ TargetM₂}) - {TargetM₁} - {TargetM₂});
    Until MaxSim &lt;  $\alpha$ ;
End.
</div>

Figure 3. Algorithm of Atomic-Based HAC Method

Figure 3. Essentially, the atomic-based HAC method is identical to the traditional HAC algorithm, as illustrated in Figure 4, where $d _ { i }$ is a document and $C _ { k }$ is an intermediate cluster. The two clusters with the highest intercluster similarity are merged into one cluster in a higher level in the clustering hierarchy until the termination condition (i.e., a predetermined intercluster similarity threshold or a desired number of clusters) is satisfied. In our research, the similarity of two documents $d _ { i }$ and $d _ { j }$ is estimated by the cosine similarity measure, as shown in formula (5). Furthermore, we employ the group-average link method using the average similarity among all intercluster pairs of documents to measure the similarity between two clusters.

$$
\operatorname{sim} \left(d _ {i}, d _ {j}\right) = \frac {\vec {d} _ {i} \cdot \vec {d} _ {j}}{\left| \vec {d} _ {i} \right| \times \left| \vec {d} _ {j} \right|},\tag{5}
$$

where $\vec { d } _ { i }$ is the feature vector of the document $d _ { i } ,$ and $| \vec { d } _ { i } |$ is the length of ${ \vec { d } } _ { i } .$

![](/api/attachments/4D6HWRF7/fulltext/images/f6cfdc147898af3891b9a35b0d75a565ed8e228c43572a4844f7397f6d5b3bf9.jpg)  
Figure 4. Illustration of Atomic-Based HAC Method

However, because some documents already have been grouped into clusters through partial clustering, the HAC algorithm also can use partial clusters during the initial clustering stage. Specifically, the documents in each partial cluster are regarded as an initial cluster, and every document that does not appear in a partial cluster forms its own cluster. Because some documents are preclustered, this method is denoted the precluster-based HAC method. Figure 5 shows its algorithmic details. As illustrated in Figure 6, the HAC algorithm is applied to these initial clusters, where PC is a partial cluster. Subsequently, the precluster-based HAC method proceeds in the same way as the atomic-based HAC method.

## Empirical Evaluation

## Evaluation Design

WE COLLECTED TWO SETS OF DOCUMENTS for the empirical evaluation. One document set includes research articles collected from a scientific literature digital library (CiteSeer Scientific Literature Digital Library, citeseer.ist.psu.edu). This document set, called the CiteSeer Corpus, consists of 436 research articles (written in English) related to information systems and technologies. The second document set, called the Thesis Corpus, gathered from a dissertation and thesis digital library in Taiwan (http://datas.ncl.edu.tw/theabs/1/), contains 570 Chinese abstracts of theses and dissertations from the years 2000 and 2001 written for the management information systems departments of several major national universities in Taiwan. For each document in the CiteSeer or Thesis Corpus, only the title, abstract, and key words were used in the evaluation study.

To collect individuals’ partial and final clustering for a particular document corpus, we developed a Web-based system. Because both document corpora relate to information systems and management, we constrained the experimental subjects to master’s and doctoral students majoring in management information systems. Each experimental subject was asked to categorize the randomly ordered documents manually.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure Precluster-Based HAC (PC: a set of partial clusters; S: the remaining documents in the corpus;  $\alpha$ : an intercluster similarity threshold)
/* Initial clusters are changed from each document as one cluster to each partial cluster or each remaining document (i.e., not in any partial clusters) as one cluster. */
Begin
    A = ∅;
    For each partial cluster  $PC_{i}$  in PC /* form each partial cluster as one initial cluster */
    A = A ∪  $\{PC_{i}\}$ ;
    For each document  $d_{i}$  in S /* form each remaining document as one initial cluster */
    A = A ∪  $\{\{d_{i}\}\}$ ;
    Cluster-Merging(A,  $\alpha$ ); /* same as the cluster merging procedure shown in Figure 3 */
    Return A;
End.
</div>

Figure 5. Algorithm of Precluster-Based HAC Method

![](/api/attachments/4D6HWRF7/fulltext/images/6d204f739c293f1a6c63172ddf1a3c49649844c952347225a828f10d198bfd98.jpg)  
Figure 6. Illustration of Precluster-Based HAC Method

As shown in Figure 7, the main screen of the system included three sections—unclassified documents, folder management, and documents in the folder. In the folder management section, subjects could move documents into a folder or create, delete, and merge folders. At the bottom of the screen, all documents in a selected folder were shown, which enabled subjects to move documents from the selected folder to another (in Figure 7, the contents of the “Agent” folder are shown).

As subjects manually organized documents into a set of categories, all actions (including creating, deleting, and merging folders and inserting and moving documents to selected folders) were recorded. By keeping a log for each subject, we were able to generate the partial clustering for each subject in the subsequent evaluation study. A total of 17 subjects accomplished the manual clustering of the documents for the CiteSeer Corpus, and 20 subjects fulfilled the manual document clustering for the Thesis Corpus. According to the self-reported estimates of the subjects, each subject spent a minimum of eight hours performing manual document clustering. A summary of the document categories generated by the subjects is provided in Table 1.

![](/api/attachments/4D6HWRF7/fulltext/images/38d2e71b3abe9e70263b87986ac5627dcd1e04c986d0a9571a2b81d6ed204cf2.jpg)  
Figure 7. Screenshot of Web-Based Document-Clustering Collection System

Table 1. Summary of Subjects’ Categories in CiteSeer and Thesis Corpora

<table><tr><td rowspan="2"></td><td colspan="2">CiteSeer Corpus</td><td colspan="2">Thesis Corpus</td></tr><tr><td>Number of folders</td><td>Number of documents in a folder</td><td>Number of folders</td><td>Number of documents in a folder</td></tr><tr><td>Maximum</td><td>32</td><td>126</td><td>39</td><td>234</td></tr><tr><td>Minimum</td><td>10</td><td>1</td><td>10</td><td>9</td></tr><tr><td>Average</td><td>20.25</td><td>22.33</td><td>20.55</td><td>33.36</td></tr></table>

For each document corpus, we measure intersubject agreement on the basis of their manual document clusterings. Given the manual document clustering by a subject $S _ { a } ,$ we form a set $T _ { a }$ of intracluster associations, where an association is defined as a pair of documents that belong to the same folder for that subject. Accordingly, we estimate the agreement of manual document clusterings of each pair of subjects, $S _ { a }$ and $S _ { b } ,$ using the Jaccard or Dice similarity measure, respectively,

$$
\text { Similarity } _ {\text { Jaccard }} \left(S _ {a}, S _ {b}\right) = \frac {\left| T _ {a} \cap T _ {b} \right|}{\left| T _ {a} \cup T _ {b} \right|}\tag{6}
$$

Table 2. Summary of Intersubject Agreement (percent)

<table><tr><td></td><td>Jaccard similarity</td><td>Dice similarity</td></tr><tr><td>CiteSeer Corpus</td><td>42.78</td><td>59.91</td></tr><tr><td>Thesis Corpus</td><td>18.33</td><td>30.98</td></tr></table>

and

$$
S i m i l a r i t y _ {D i c e} (S _ {a}, S _ {b}) = \frac {2 \times | T _ {a} \cap T _ {b} |}{| T _ {a} | + | T _ {b} |}.\tag{7}
$$

As Table 2 shows, the average Jaccard similarity for the CiteSeer Corpus is 42.78 percent, while that for the Thesis Corpus is 18.33 percent. In addition, the average Dice similarities for both corpora are 59.91 percent and 30.98 percent, respectively. Such a low degree of intersubject agreement suggests that individuals generally have different categorization preferences, even for the same document corpus. These empirical statistics also justify the need to support personalization in document categorization.

## Evaluation Criteria

We employed cluster recall and cluster precision to measure the effectiveness of the proposed personalized document-clustering approach. Cluster recall and cluster precision [33], similar to the recall and precision measures typically used in information retrieval (IR) research, are defined according to the concept of intracluster association. Assume that the clusters (folders) manually produced by a subject $S _ { a }$ are the true categories for $S _ { a }$ . Accordingly, the cluster precision $( C P )$ from the viewpoint of $S _ { a }$ is defined as

$$
C P = \frac {\left| C A _ {a} \right|}{\left| G \right|},\tag{8}
$$

where $G$ is the set of associations in the clusters generated by a document-clustering technique and $C A _ { a }$ is the set of correct associations that exists in the clusters generated by both the document-clustering technique and the true categories of the subject $S _ { a }$

Cluster recall (CR) from the viewpoint of $S _ { a }$ is defined as

$$
C R = \frac {\left| C A _ {a} \right|}{\left| T _ {a} \right|},\tag{9}
$$

where $T _ { a }$ is the set of intracluster associations in the true categories of the subject $S _ { a }$

For example, the cluster recall and cluster precision can be measured as follows. Assume that subject $S _ { a }$ organizes the documents $d _ { 1 } , d _ { 2 } , . . . . , d _ { 6 }$ into two true categories, $C _ { 1 }$ and $C _ { 2 } ,$ where $C _ { 1 } = \{ d _ { 1 } , d _ { 2 } , d _ { 3 } \}$ and $C _ { 2 } = \{ d _ { 4 } , d _ { 5 } , d _ { 6 } \}$ . In this case, the set of associations in the true categories produced by the subject is $T _ { a } = \{ ( d _ { 1 } - d _ { 2 } ) , ( d _ { 1 } - d _ { 3 } )$ $( d _ { 2 } - d _ { 3 } ) , ( d _ { 4 } - d _ { 5 } ) , ( d _ { 4 } - d _ { 6 } ) , ( d _ { 5 } - d _ { 6 } ) \}$ . Let a document-clustering technique produce three clusters for the same set of documents: $\{ d _ { 1 } , d _ { 2 } \} , \{ d _ { 3 } , d _ { 4 } \}$ , and $\{ d _ { 5 } , d _ { 6 } \}$ . That is, the set of associations in the clusters generated by a document-clustering technique is $G = \{ ( d _ { 1 } - d _ { 2 } ) , ( d _ { 3 } - d _ { 4 } ) , ( d _ { 5 } - d _ { 6 } ) \}$ . Consequently, the set of correct associations with respect to the true categories of subject $S _ { a }$ is $C A _ { a } = \{ ( d _ { 1 } - d _ { 2 } ) , ( d _ { 5 } - d _ { 6 } ) \}$ . In turn,

$$
C P = \frac {\left| C A _ {a} \right|}{\left| G \right|} = \frac {2}{3} = 0. 6 6 7
$$

and

$$
C R = \frac {\left| C A _ {a} \right|}{\left| T _ {a} \right|} = \frac {2}{6} = 0. 3 3 3.
$$

## Evaluation Procedure

As mentioned previously, two document representation methods (i.e., feature refinement and feature weighting) and two clustering methods (i.e., atomic-based HAC and precluster-based HAC) were employed for the proposed approach. We evaluated these four personalized document-clustering techniques in comparison with the traditional content-based document-clustering technique. The four techniques are referred to as “atomic-based (feature refinement),” “atomic-based (feature weighting),” “preclusterbased (feature refinement),” and “precluster-based (feature weighting).” The traditional content-based document-clustering technique (referred to as “content-based clustering”) adopted the TF×IDF metric for feature selection and HAC as its underlying clustering algorithm.

For each subject, we took the first $p \left( \mathrm { e . g . } \right.$ ., 30 percent) of documents categorized by the subject as his or her partial clustering. Subsequently, the respective document corpus was clustered according to each of the five clustering techniques. We also measured the cluster recall and cluster precision for each technique. The overall clustering effectiveness of a technique was calculated by averaging the cluster recall and cluster precision scores obtained from all subjects. To address the inevitable tradeoffs between cluster precision and cluster recall, precision/recall trade-off (PRT) curves were employed. A PRT curve represents the effectiveness of a document-clustering technique with different numbers of clusters (i.e., 2–60 clusters in this study). As the number of clusters increases, the average number of documents in each cluster decreases; thus, a higher cluster precision comes at the cost of cluster recall. A document-clustering technique with a PRT curve closer to the upper-right corner is more desirable.

## Tuning the Number of Representative Features

Both the traditional content-based and the personalized document-clustering techniques require a specification of the number of features to represent each document. In this tuning experiment, we randomly chose manual document clusterings from five subjects for each document corpus to determine the appropriate number of features for each technique investigated. We examined the number of representative features (k), ranging from 100 to 500 in increments of 100, for the traditional content-based document-clustering technique. For the CiteSeer Corpus, k at 100 resulted in the worst clustering effectiveness and k at 400 achieved a clustering effectiveness slightly better than that attained by other values. For the Thesis Corpus, the effects of different numbers of features were marginal. Of the values of k examined for the Thesis Corpus, k at 500 achieved a clustering effectiveness slightly better than that attained by other values. Therefore, for the content-based document-clustering technique in subsequent experiments, we selected 400 as the number of features for the CiteSeer Corpus and 500 for the Thesis Corpus.

As mentioned in the Feature Extraction, Selection, and Consolidation Phase subsection, the feature consolidation phase selects $k _ { 1 } , \ k _ { 2 }$ , and $k _ { 3 }$ features from ALL\_TF×IDF, Partial\_TF, and Partial\_ $\mathcal { X } ^ { 2 }$ , respectively. Assume that $p$ (where $0 <$ $p < 1 )$ of the document collection to be clustered appears in the partial clustering. In the subsequent experiments, we first set $k _ { 2 } = p \times k _ { 1 }$ and $k _ { 3 } = p \times k _ { 1 }$ and then examine the effects of different values for $k _ { 2 }$ and $k _ { 3 }$ on the effectiveness of the proposed personalized document-clustering techniques (see the Effects of $k _ { 2 }$ and $k _ { 3 }$ subsection). To tune the number of representation features for each proposed technique, we set $p$ (the size of partial clustering relative to the target document corpus) at 30 percent and examined the range of $k _ { 1 }$ from 100 to 500 in increments of 100. As with the traditional content-based document-clustering technique, the effects of $k _ { 1 }$ on clustering effectiveness for the four personalized document-clustering techniques were marginal, with $k _ { 1 }$ at 100 as the worst. In this study, we selected $k _ { 1 } = 5 0 0$ for both corpora for our proposed personalized document-clustering techniques. As Table 3 illustrates, with this particular value for $k _ { 1 } .$ , the average number of features removed from ALL\_TF×IDF (i.e., after subtraction of Partial\_TF) was 149.94 (29.99 percent of ALL\_TF×IDF) for the CiteSeer Corpus and 110.45 (i.e., 22.09 percent) for the Thesis Corpus. The resulting average number of features in the consolidated set was 460.20 for the CiteSeer Corpus and 516.20 for the Thesis Corpus.

## Comparative Evaluation

In the comparative evaluation experiment, we set the size $p$ of partial clustering (relative to the target document corpus) at 30 percent. As shown in Figure 8(a), for the CiteSeer Corpus, the proposed personalized document-clustering techniques, with the exception of the atomic-based (feature refinement) technique, achieved better clustering effectiveness (as measured by cluster recall and cluster precision) than did the content-based document-clustering technique. Moreover, the precluster-based

Table 3. Number of Features in Personalized Document-Clustering Approach (when p = 30 percent)

<table><tr><td></td><td>|ALL_TF×IDF|(i.e.,  $k_{1}$ )</td><td>|ALL_TF×IDF–Partial_TF|</td><td>|(ALL_TF×IDF–Partial_TF)∪ Partial_χ2|</td></tr><tr><td>CiteSeer Corpus</td><td>500</td><td>350.06</td><td>460.20</td></tr><tr><td>Thesis Corpus</td><td>500</td><td>389.55</td><td>516.20</td></tr></table>

![](/api/attachments/4D6HWRF7/fulltext/images/b300ccdd06b708836c413a86a3efb0753578791d6073d175f7d3499db0c8edb9.jpg)

![](/api/attachments/4D6HWRF7/fulltext/images/b1ae4c4e7ea930e7543857ac20295166b7daf5eb2a79a9c6c1ace11be9fd989d.jpg)  
b. Thesis Corpus (p = 30 percent)  
Figure 8. PRT Curves of the Different Document-Clustering Techniques

HAC method generally outperformed the atomic-based HAC method, regardless of whether the feature refinement or feature weighting method was used. However, for both HAC methods, feature weighting resulted in better performance than did feature refinement.

Table 4. Average Stability Between a Partial Clustering and Its Final Clustering

<table><tr><td></td><td>p = 10 percent</td><td>p = 20 percent</td><td>p = 30 percent</td><td>p = 40 percent</td><td>p = 50 percent</td></tr><tr><td>CiteSeer Corpus</td><td>0.954</td><td>0.967</td><td>0.970</td><td>0.967</td><td>0.962</td></tr><tr><td>Thesis Corpus</td><td>0.921</td><td>0.921</td><td>0.915</td><td>0.907</td><td>0.907</td></tr></table>

The evaluation results from the Thesis Corpus were generally similar to those from the CiteSeer Corpus. As Figure 8(b) illustrates, the precluster-based HAC techniques achieved the best clustering effectiveness, and the traditional content-based document-clustering technique earned the worst. As with the CiteSeer Corpus, feature weighting resulted in better performance than did feature refinement when either the atomic-based or precluster-based HAC method was employed.

The better clustering effectiveness of the precluster-based HAC method may be attributed to the stability between the partial and the final clusters created by each subject. Most subjects did not change the folder assignment of documents frequently. That is, subjects did not tend to move documents from one folder to another during the categorization process. As shown in Table 4, the average stability (as measured by the percentage of intracluster associations in the partial clustering that appeared in the respective final clusters) for each p is high for both document corpora. Consequently, the precluster-based HAC method is superior to other techniques because most of the document associations in the partial clustering will appear in the final (i.e., true) clusters and can be preserved in the clusters generated by the preclusterbased HAC method. Such high level of stability recorded is reasonable when considering the application scenario of our proposed personalized document-clustering approach. As mentioned, digital libraries and online information providers that offer personal bookshelves to users represent a typical application scenario of our proposed approach. In this scenario, a user continues organizing documents of interest into his or her personal folders. As a result, a user’s personal folders will evolve over time. However, people are habitual in document search and access; this allows efficiency gains through repetitions—that is, the power law of practice [15]. This habitual characteristic demands a necessary continuity in the evolution of a user’s personal folders, the absence of which can greatly hinder the user’s search efficiency. In this connection, an individual’s partial clustering should not deviate too much from the final clustering preferred by the individual. The recorded stability in our experiments, to some extent, captures the desired continuity in an individual’s document-clustering behavior and thus would be considered reasonable in the described scenario. However, if the stability between the partial clustering established and the final clustering preferred by individuals is moderate or even low in other application scenarios, a reevaluation of the effectiveness of the precluster-based HAC method becomes essential.

As shown in Figures 8(a) and 8(b), the clustering effectiveness for the Thesis Corpus was not as good as that for the CiteSeer Corpus. One plausible explanation may be the language difference between these two document corpora (English versus Chinese documents). Although an investigation of language effects on clustering effectiveness is beyond the scope of the current research, it could be a fruitful future research direction. Another plausible explanation may take into account the diversity of documents in the two corpora. The CiteSeer Corpus was obtained through key word searches (e.g., using such query terms as XML, data mining, and robotics) from the CiteSeer Scientific Literature Digital Library, whereas the documents in the Thesis Corpus included the abstracts of theses and dissertations from various national universities in Taiwan. The topics in the Thesis Corpus therefore are understandably much more diverse than are those in the CiteSeer Corpus. The difference in diversity may result in differences in the folders formed by the subjects for each corpus. As the summary in Table 5 shows, eight distinct subjects (i.e., 40 percent) created a large folder containing more than 100 documents when dealing with the Thesis Corpus, whereas only one subject created such a large folder for the CiteSeer Corpus. Because all the document-clustering techniques examined in this study are feature based, they may not be able to generate a large folder that consists of documents that are dissimilar in content, which would degrade their clustering effectiveness. This rationale may explain why the average clustering effectiveness for the Thesis Corpus was worse than that for the CiteSeer Corpus for all five of the document-clustering techniques investigated.

Table 5. Summary of Subjects’ Categorizations

<table><tr><td>Folder size (number of documents  $N_{f}$ )</td><td>Number of distinct subjects (CiteSeer Corpus)</td><td>Number of distinct subjects (Thesis Corpus)</td></tr><tr><td> $N_{f}<100$ </td><td>17</td><td>20</td></tr><tr><td> $100\leq N_{f}<150$ </td><td>1</td><td>5</td></tr><tr><td> $150\leq N_{f}<200$ </td><td>0</td><td>1</td></tr><tr><td> $N_{f}>200$ </td><td>0</td><td>2</td></tr></table>

This comparative evaluation demonstrates that the use of partial clustering improves document-clustering effectiveness, as measured by cluster recall and cluster precision. Of the four personalized document-clustering techniques, the precluster-based HAC method outperforms the atomic-based, and the feature weighting method achieves better clustering results than does the feature refinement method.

## Sensitivity of the Size of Partial Clustering

We further examine the effects of different sizes of partial clustering (p) on clustering effectiveness. Specifically, the percentages of documents in a partial clustering to the total number of documents in a target corpus, ranging from 10 percent to 50 percent in increments of 10 percent, were investigated. Our empirical results show similar effects of different sizes of partial clustering on the effectiveness of clustering in both document corpora. As Figure 9 illustrates, for all four personalized document-clustering techniques with the CiteSeer Corpus, an increase in the size of the partial clustering improved the resultant clustering effectiveness across the range of sizes examined. For both corpora, the effects of the size of partial clustering on the preclusterbased HAC method were much greater than were those on the atomic-based HAC method. That is, as p increased, the improvement in clustering effectiveness achieved by the precluster-based HAC method was more significant than that achieved by the atomic-based HAC one. The use of the feature weighting method for document representation exhibited a higher sensitivity to the size of partial clusters than did the feature refinement method. Even when the partial clustering was only 10 percent of the target document corpus, the four personalized document-clustering techniques were comparable to or even outperformed the content-based document-clustering technique.

## Effects of $k _ { 2 }$ and $k _ { 3 }$

The experiments reported in the two previous subsections employed $k _ { 2 }$ as $p \times k _ { 1 }$ (the number of features in Partial\_TF) and $k _ { 3 } \mathrm { a s } p \times k _ { 1 }$ (the number of features in Partial\_ $\chi ^ { 2 } )$ for the proposed personalized document-clustering techniques. To understand the effects of $k _ { 2 }$ and $k _ { 3 }$ on the clustering effectiveness of the proposed techniques, we further conduct empirical experiments by varying the influence of $k _ { 2 }$ and $k _ { 3 }$ in the consolidated feature sets created with different sizes of partial clustering. Specifically, we examined the range of both $k _ { 2 }$ and $k _ { 3 }$ from 0 to $3 p \times k _ { 1 }$ in increments of $_ p \times$ $k _ { 1 }$ . In both document corpora, the effects of $k _ { 2 }$ and $k _ { 3 }$ exhibited similar trends across the four personalized document-clustering techniques. For this reason, we use the precluster-based (feature weighting) technique with the CiteSeer Corpus as an illustration in the following discussions.

When analyzing the effects of $k _ { 2 } ,$ we set $k _ { 3 }$ to be constant (i.e., $k _ { 3 } = p \times k _ { 1 } )$ . As Figure 10(a) shows, when $p = 1 0$ percent, setting $k _ { 2 }$ to 0 achieved the best clustering effectiveness. An increase of $k _ { 2 }$ from 0 to $3 p \times k _ { 1 }$ slightly degraded the performance of the personalized document-clustering techniques. This empirical result suggests that, when the size of partial clustering is small relative to the target document corpus, selected Partial\_TF features that were considered nonrepresentative might be representative with respect to the entire document corpus. Consequently, minimizing the influence of $k _ { 2 }$ in the consolidated feature set, or even without the removal of Partial\_TF features from the consolidated feature set (i.e., setting $k _ { 2 }$ to 0), would lead to better clustering effectiveness. When $p$ increased from 10 percent to 50 percent, as Figure 10(b) illustrates, the personalized document-clustering technique achieved a comparable clustering effectiveness across all levels of $k _ { 2 }$ examined. Because a greater value for $k _ { 2 }$ results in a smaller consolidated feature set, and thus improves clustering efficiency, setting $k _ { 2 }$ to $3 p \times k _ { 1 }$ would be preferable when a larger partial clustering is available.

Similarly, when analyzing the effects of $k _ { 3 } ,$ we set $k _ { 2 }$ to $p \times k _ { 1 }$ . As Figure 11(a) shows, when $p = 1 0$ percent, the proposed personalized document-clustering approach was ineffective if the $P a r t i a l _ { - } \chi ^ { 2 }$ features were not incorporated into the consolidated feature set $( \mathrm { i . e . , } k _ { 3 } = 0 )$ . With this particular value for $k _ { 3 } ,$ the content-based documentclustering technique considerably outperformed the personalized document-clustering technique under discussion. When we increased $k _ { 3 }$ from 0 to $p \times k _ { 1 }$ , we recorded a significant performance improvement. Any further increase of $k _ { 3 } ( \mathrm { i . e . , t o } 3 p \times k _ { 1 } )$ had only a marginal effect on the clustering effectiveness of the personalized document-clustering technique. Because a greater value for $k _ { 3 }$ results in a larger consolidated feature set, it deteriorates clustering efficiency. Hence, when considering both clustering effectiveness and efficiency, our empirical results suggest that setting $k _ { 2 }$ to $p \times k _ { 1 }$ is appropriate. As shown in Figure 11(b), when $\boldsymbol { \cdot p }$ was expanded to $5 0$ percent, $k _ { 3 }$ exhibited similar effects on the clustering effectiveness. The personalized document-clustering technique also significantly benefited from the incorporation of Partial\_ $\mathcal { X } ^ { 2 }$ features into the consolidated feature set. When we set $k _ { 3 }$ within the range of $p \times k _ { 1 }$ to $3 p \times k _ { 1 }$ , the proposed technique attained almost identical clustering effectiveness. Overall, across the range of $p$ examined, $p \times k _ { 1 }$ for $k _ { 3 }$ appears preferable because of its comparable clustering effectiveness and improved clustering efficiency in comparison with those attained through a higher $k _ { 3 }$ value.

![](/api/attachments/4D6HWRF7/fulltext/images/92793ec3062b6c4f20be8ce4f3a3835c747972fff73935afbf62c9cc112d3f23.jpg)  
a. Atomic-Based (Feature Refinement)

![](/api/attachments/4D6HWRF7/fulltext/images/35d8b0e27475fed4f256c9f1e0616981026734732be86916dca21e57fcea72ef.jpg)

![](/api/attachments/4D6HWRF7/fulltext/images/eae589701a87ed0e1f43703f0cf76bf2b4113daf690a1c844b816cee4467d8e8.jpg)  
c. Precluster-Based (Feature Refinement)

![](/api/attachments/4D6HWRF7/fulltext/images/55e8dedaa82e87c56b29495f48f0106986b1494f4bffbb0adc527553866a5b44.jpg)  
d. Precluster-Based (Feature Weighting)  
Figure 9. Sensitivity of Size of Partial Clustering for the CiteSeer Corpus

![](/api/attachments/4D6HWRF7/fulltext/images/93f987b62d75d8eb9708a32340520a324e89a8dca2c6931c9509b6f9b5a03760.jpg)

![](/api/attachments/4D6HWRF7/fulltext/images/4f453c521b804587e5481c0e639755657ff181fad6778bf1bea4256363d4a3cd.jpg)  
b. p = 50 Percent and $k _ { 3 } = p \times k _ { 1 }$  
Figure 10. Effects of $k _ { 2 }$ (Precluster-Based Feature Weighting Technique with CiteSeer Corpus)

![](/api/attachments/4D6HWRF7/fulltext/images/ad1094205b82d82e8249504d5556fdfd6622b7bd4c2e5434321f32fe7215b89a.jpg)

![](/api/attachments/4D6HWRF7/fulltext/images/502c0bd511daecb7a14eb179756ee02cbf0a8dcbad5e137ef3b83b2003833a72.jpg)  
b. p = 50 Percent and $k _ { 2 } = p \times k _ { 1 }$  
Figure 11. Effects of $k _ { 3 }$ (Precluster-Based Feature Weighting Technique with CiteSeer Corpus)

## Conclusion and Further Research

EXISTING DOCUMENT-CLUSTERING TECHNIQUES create a common set of clusters for all individuals without tailoring those clusters to individuals’ preferences; therefore, they are unable to support personalization. Our research is motivated by the importance of reducing individuals’ cognitive load in document organization and management by considering their categorization needs and preferences. Specifically, we design and implement a personalized document-clustering approach by incorporating individuals’ partial clustering into the document-clustering process. By combining two document representation methods (i.e., feature refinement and feature weighting) with two clustering methods (i.e., precluster-based HAC and atomic-based HAC), we establish four personalized document-clustering techniques.

The empirical evaluation demonstrates that the use of an individual’s partial clustering can improve document-clustering effectiveness, as measured by cluster recall and cluster precision. Moreover, among the proposed personalized document-clustering techniques, the precluster-based HAC method outperforms the atomic-based HAC method. In addition, the feature weighting method generally achieves greater clustering effectiveness than the feature refinement. Furthermore, the effects of the size of the partial clustering on the precluster-based HAC method are much greater than are those on the atomic-based HAC one, and the feature weighting method exhibits a higher sensitivity to the size of partial clusters than does the feature refinement method.

This study is intended to serve as a foundation for continued research on personalized document clustering. Additional research should be aligned strategically to enhance the generalizability and effectiveness of our proposed approach. First, our experimental study did not involve a large number of subjects because of the significant amount of time (a minimum of eight hours) that each subject required to complete the experiment. Our future research efforts therefore will include an evaluation that involves more subjects. Second, although the precluster-based HAC method outperforms the atomic-based HAC method, its preclustered nature prohibits the reclustering of documents in partial clusters. In some application scenarios, if the stability between the partial clustering established and the final clustering preferred by an individual is moderate or even low, the precluster-based method may be constrained to address the evolutionary nature of document groupings. Hence, the development of a precluster-based HAC method that is capable of reclustering or evolution [42] represents an interesting and essential direction for future research work. Third, this research concentrates on an individual’s partial clustering organized nonhierarchically. However, an individual commonly will organize his or her documents into a hierarchical structure. Hence, the proposed approach should be extended to consider partial clustering’s hierarchy. Fourth, our approach generates a flat set of clusters. It would be desirable to extend the proposed personalized document-clustering approach to organize documents into a hierarchical structure of clusters. Fifth, like the traditional content-based document-clustering technique, our proposed personalized document-clustering approach currently uses features extracted from documents. Turning our proposed approach into either a concept- or ontology-based approach may have great potential to improve document-clustering effectiveness further and create a new document-clustering research direction.

Acknowledgments: This work was funded in part by the Ministry of Education Program for Promoting Academic Excellence of Universities of the Republic of China under the grant 91- H-FA08–1-4 and by the National Science Council of the Republic of China under grants 91– 2415-H-110–006 and NSC 92–2415-H-110–003. The study was conducted and completed when the first author was affiliated with and the second author was a visiting scholar at the National Sun Yat-sen University, Taiwan, ROC. The authors are grateful for the support from the College of Management at National Sun Yat-sen University. The authors thank Vladimir Zwass, the Editor-in-Chief, and three anonymous reviewers for their insightful comments and suggestions that helped a great deal in improving the paper. They also thank Tse-Hsiu Huang for his technical support of the experiments.

## NOTE

1. Relevance feedback mechanisms attempt to improve IR effectiveness by modifying a user query on the basis of his or her reaction to the initially retrieved documents. Specifically, the user determines a set of the most relevant documents from the initially retrieved documents. On the basis of the user’s feedback, the IR system reformulates the user query by adding new query terms and adjusting their weights and, accordingly, uses the reformulated query for retrieval [11, 14].

## REFERENCES

1. Anderberg, M.R. Cluster Analysis for Applications. New York: Academic Press, 1973.

2. Barreau, D.K. Context as a factor in personal information management systems. Journal of the American Society for Information Science, 46, 5 (June 1991), 327–339.

3. Boley, D.; Gini, M.; Gross, R.; Han, E.; Hastings, K.; Karypis, G.; Kumar, V.; Mobasher, B.; and Moore, J. Partitioning-based clustering for Web document categorization. Decision Support Systems, 27, 3 (1999), 329–341.

4. Brill, E. A simple rule-based part of speech tagger. In M. Bates and O. Stock (eds.), Proceedings of the Third Conference on Applied Natural Language Processing. East Stroudsburg, PA: Association for Computational Linguistics, 1992, pp. 152–155.

5. Brill, E. Some advances in rule-based part of speech tagging. In B. Hayes-Roth and R.E. Kork (eds.), Proceedings of the Twelfth National Conference on Artificial Intelligence. Menlo Park, CA: AAAI Press, 1994, pp. 722–727.

6. Case, D.O. Conceptual organization and retrieval of text by historians: The role of memory and metaphor. Journal of the American Society for Information Science, 42, 9 (October 1991), 657–668.

7. Cutting, D.; Karger, D.; Pedersen, J.; and Tukey, J. Scatter/gather: A cluster-based approach to browsing large document collections. In N. Belkin, P. Ingwersen, and A.M. Pejtersen (eds.), Proceedings of the Fifteenth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1992, pp. 318–329.

8. Deerwester, S.; Dumais, S.T.; Furnas, G.W.; Landauer, T.K.; and Harshman, R. Indexing by latent semantic analysis. Journal of the American Society for Information Science, 41, 6 (1990), 391–407.

9. Deogun, J., and Raghavan, V. User-oriented document clustering: A framework for learning in information retrieval. In F. Rabitti (ed.), Proceedings of the Ninth International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1986, pp. 157–163.

10. Donovan, J. Patrons’ expectations about collocation: Measuring the difference between psychologically real and the really real. Cataloging and Classification Quarterly, 13, 2 (1991), 23–43.

11. Dunlop, M.D. The effect of accessing nonmatching documents on relevance feedback. ACM Transactions on Information Systems, 15, 2 (April 1997), 137–153.

12. El-Hamdouchi, A., and Willett, P. Hierarchical document clustering using Ward’s method. In F. Rabitti (ed.), Proceedings of the ACM Conference on Research and Development in Information Retrieval. New York: ACM Press, 1986, pp. 149–156.

13. Gordon, M. User-based document clustering by redescribing subject description with a genetic algorithm. Journal of the American Society for Information Science, 42, 5 (1991), 311–322.

14. Haines, D., and Croft, W.B. Relevance feedback and inference networks. In R. Korfhage, E. Rasmussen, and P. Willett (eds.), Proceedings of the Sixteenth International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1993, pp. 2–11.

15. Johnson, E.J.; Bellman, S.; and Lohse, G.L. Cognitive lock-in and the power law of practice. Journal of Marketing, 67, 2 (April 2003), 62–75.

16. Kaufman, L., and Rousseeuw, P.J. Finding Groups in Data: An Introduction to Cluster Analysis. New York: John Wiley & Sons, 1990.

17. Kim, H., and Lee, S. An effective document clustering method using user-adaptable distance metrics. In B. Panda (ed.), Proceedings of the 2002 ACM Symposium on Applied Computing. New York: ACM Press, 2002, pp. 16–20.

18. Kim, H., and Lee, S. A semi-supervised document clustering technique for information organization. In A. Agah, J. Callan, E. Rundensteiner, and S. Gauch (eds.), Proceedings of the Ninth International Conference on Information and Knowledge Management. New York: ACM Press, 2000, pp. 30–37.

19. Kohonen, T. Self-Organization and Associative Memory. Berlin: Springer, 1989.

20. Kohonen, T. Self-Organizing Maps. Berlin: Springer, 1995.

21. Kwasnik, B.H. The importance of factors that are not document attributes in the organization of personal documents. Journal of Documentation, 47, 4 (1991), 389–398.

22. Lagus, K.; Honkela, T.; Kaski, S.; and Kohonen, T. Self-organizing maps of document collections: A new approach to interactive exploration. In E. Simoudis, J. Han, and U. Fayyad (eds.), Proceedings of the Second International Conference on Knowledge Discovery and Data Mining. New York: ACM Press, 1996, pp. 238–243.

23. Lakoff, G. Women, Fire and Dangerous Things: What Categories Reveal About the Mind. Chicago: University of Chicago Press, 1987.

24. Larsen, B., and Aone, C. Fast and effective text mining using linear-time document clustering. In U. Fayyad, S. Chaudhuri, and D. Madigan (eds.), Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. New York: ACM Press, 1999, pp. 16–22.

25. Lin, C.; Chen, H.; and Nunamaker, J.F. Verifying the proximity and size hypothesis for self-organizing maps. Journal of Management Information Systems, 16, 3 (Winter 1999–2000), 57–70.

26. Mackay, W.E. Diversity in the use of electronic mail: A preliminary inquiry. ACM Transactions on Office Information Systems, 6, 4 (1988), 380–397.

27. Mackay, W.E. Responding to cognitive overload: Co-adaptation between users and technology. Intellectica, 30, 1 (2000), 177–193.

28. Pantel, P., and Lin, D. Document clustering with committees. In M. Beaulieu, R. Baeza-Yates, and S.H. Mayeng (eds.), Proceedings of the Twenty-Fifth International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 2002, pp. 199–206.

29. Quillian, M.R. Semantic memory. In M. Minsky (ed.), Semantic Information Processing. Cambridge, MA: MIT Press, 1968, pp. 227–270.

30. Quiroga, L.M.; Crosby, M.E.; and Iding, M.K. Reducing cognitive load. In R.H. Sprague Jr. (ed.), Proceedings of the Thirty-Seventh Hawaii International Conference on Systems Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2004 (available at ieeexplore.ieee.org).

31. Rauber, A., and Merkl, D. Using self-organizing maps to organize document archives and to characterize subject matters: How to make a map tell the news of the world. In T. Bench-Capon, G. Soda, and A.M. Tjoa (eds.), Proceedings of the Tenth International Conference on Database and Expert Systems Applications. Berlin: Springer Verlag, 1999, pp. 302–311.

32. Restorick, F.M. Novel filing systems applicable to an automated office: A state-of-the-art study. Information Processing and Management, 22, 2 (1986), 151–172.

33. Roussinov, D.G., and Chen, H. Document clustering for electronic meetings: An experimental comparison of two techniques. Decision Support Systems, 27, 1–2 (November 1999), 67–79.

34. Rucker, J., and Polanco, M.J. Siteseer: Personalized navigation for the Web. Communications of the ACM, 40, 3 (March 1997), 73–75.

35. Salton, G., and Buckley, C. Term-weighting approaches in automatic text retrieval. Information Processing and Management, 24, 5 (1988), 513–523.

36. Schütze, H.; Hull, D.A.; and Pedersen, J.O. A comparison of classifiers and document representations for the routing problem. In M. Beaulieu, R. Baeza-Yates, and S.H. Myaeng (eds), Proceedings of the Eighteenth International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 2002, pp. 229–237.

37. Sebastiani, F. Machine learning in automated text categorization. ACM Computing Surveys, 34, 1 (March 2002), 1–47.

38. Spangler, S.; Kreulen, J.T.; and Lessler, J. Generating and browsing multiple taxonomies over a document collection. Journal of Management Information Systems, 19, 4 (Spring 2003), 191–212.

39. Talavera, L., and Bejar, J. Integrating declarative knowledge in hierarchical clustering tasks. In D.J. Hand, J.N. Kok, and M.R. Berthold (eds.), Proceedings of the Third International Symposium on Intelligent Data Analysis. Berlin: Springer Verlag, 1999, pp. 211–222.

40. Voorhees, E.M. Implementing agglomerative hierarchical clustering algorithms for use in document retrieval. Information Processing and Management, 22, 6 (1986), 465–476.

41. Voutilainen, A. NPtool: A detector of English noun phrases. In K.W. Church (ed.), Proceedings of the First Workshop on Very Large Corpora. East Stroudsburg, PA: Association for Computational Linguistics, 1993, pp. 48–57.

42. Wei, C.; Hu, P.; and Dong, Y.X. Managing document categories in e-commerce environments: An evolution-based approach. European Journal of Information Systems, 11, 3 (September 2002), 208–222.

43. Wei, C.; Yang, C.S.; Hsiao, H.W.; and Cheng, T.H. Combining preference- and contentbased approaches for improving document clustering effectiveness. Information Processing and Management, 42, 2 (March 2006), 350–372.

44. Yang, C., and Luk, J. Automatic generation of English/Chinese thesaurus based on a parallel corpus in laws. Journal of the American Society for Information Science and Technology, 54, 7 (2003), 671–682.

45. Yang, Y., and Chute, C.G. An example-based mapping method for text categorization and retrieval. ACM Transactions on Information Systems, 12, 3 (1994), 252–277.

46. Yang, Y., and Pedersen, J.O. A comparative study on feature selection in text categorization. In D.H. Fisher (ed.), Proceedings of the Fourteenth International Conference on Machine Learning. San Francisco: Morgan Kaufmann, 1997, pp. 412–420.

47. Yu, C.T.; Wang, Y.T.; and Chen, C.H. Adaptive document clustering. In J.M. Tague (ed.), Proceedings of the Eighth International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: ACM Press, 1985, pp. 197–203.
