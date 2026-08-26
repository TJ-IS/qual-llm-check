---
otero_id: 21792
otero_key: "8MZCVXBM"
title: "Partitioning-based clustering for Web document categorization"
authors: "Daniel Boley; Maria Gini; Robert Gross; Eui-Hong (Sam) Han; Kyle Hastings; George Karypis; Vipin Kumar; Bamshad Mobasher; Jerome Moore"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00055-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Partitioning-based clustering for Web document categorization

<sup>)</sup> Daniel Boley , Maria Gini, Robert Gross, Eui-Hong Sam Han, Kyle Hastings, Ž . George Karypis, Vipin Kumar, Bamshad Mobasher, Jerome Moore

Department of Computer Science and Engineering, UniÕersity of Minnesota, Minneapolis, MN 55455,USA

## Abstract

Clustering techniques have been used by many intelligent software agents in order to retrieve, filter, and categorize documents available on the World Wide Web. Clustering is also useful in extracting salient features of related Web documents to automatically formulate queries and search for other similar documents on the Web. Traditional clustering algorithms either use a priori knowledge of document structures to define a distance or similarity among these documents, or use probabilistic techniques such as Bayesian classification. Many of these traditional algorithms, however, falter when the dimensionality of the feature space becomes high relative to the size of the document space. In this paper, we introduce two new clustering algorithms that can effectively cluster documents, even in the presence of a very high dimensional feature space. These clustering techniques, which are based on generalizations of graph partitioning, do not require pre-specified ad hoc distance functions, and are capable of automatically discovering document similarities or associations. We conduct several experiments on real Web data using various feature selection heuristics, and compare our clustering schemes to standard distance-based techniques, such as hierarchical agglomeration clustering, and Bayesian classification methods, such as AutoClass. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Clustering; Categorization; World Wide Web documents; Graph partitioning; Association rules; Principal component analysis

## 1. Introduction

The World Wide Web is a vast resource of information and services that continues to grow rapidly. Powerful search engines have been developed to aid in locating unfamiliar documents by category, contents, or subject. Unfortunately, queries often return inconsistent results, with document referrals that meet the search criteria but are of no interest to the user.

While it may not be currently feasible to extract in full the meaning of an HTML document, intelligent software agents have been developed which extract features from the words or structure of an HTML document and employ them to classify and categorize the documents. Clustering offers the advantage that a priori knowledge of categories is not needed, so the categorization process is unsupervised. The results of clustering could then be used to automatically formulate queries and search for other similar documents on the Web, or to organize bookmark files, or to construct a user profile.

In this paper, we present two new clustering algorithms based on graph partitioning and compare their performance against more traditional clustering algorithms used in information retrieval.

Traditional clustering algorithms either define a distance or similarity among documents, or use probabilistic techniques such as Bayesian classification. Many of these algorithms, however, break down as the size of the document space, and hence, the dimensionality of the corresponding feature space increases. High dimensionality is characteristic of the information retrieval applications which are used to filter and categorize documents on the World Wide Web. In contrast, our partitioning-based algorithms perform well in the presence of a high dimensional space.

In Section 2 we describe the clustering algorithms; in Section 3 we present results of a number of experiments using different methods to select features from the documents, and we compare the results of the different clustering algorithms. We show that partitioning clustering methods perform better than traditional distance based clustering. Finally, in Section 3 we compare our work with other similar systems and present ideas for future research.

## 2. Clustering methods

Most of the existing methods for document clustering are based on either probabilistic methods, or distance and similarity measures see Ref. 14 .Ž <sup>w</sup> <sup>x</sup>. Distance-based methods such as k-means analysis, hierarchical clustering 19 and nearest-neighbor <sup>w</sup> <sup>x</sup> clustering 22 use a selected set of words appearing <sup>w</sup> <sup>x</sup> in different documents as features. Each document is represented by a feature vector, and can be viewed as a point in a multidimensional space.

There are a number of problems with clustering in a multidimensional space using traditional distanceor probability-based methods. First, it is not trivial to define a distance measure in this space. Feature vectors must be scaled to avoid skewing the result by different document lengths or possibly by how common a word is across many documents. Techniques such as TFIDF 27 have been proposed precisely to<sup>w</sup> <sup>x</sup> deal with some of these problems, but we have found out in our experiments that using TFIDF scaling does not always help.

Second, the number of different words in the documents can be very large. Distance-based schemes generally require the calculation of the mean of document clusters, which are often chosen initially at random. In a high dimensional space, the cluster means of randomly chosen clusters will do a poor job at separating documents. Similarly, probabilistic methods such as Bayesian classification used in AutoClass <sup>w</sup> <sup>x</sup> 10,28 do not perform well when the size of the feature space is much larger than the size of the sample set or may depend on the independence of the underlying features. Web documents suffer from both high dimensionality and high correlation among the feature values. We have found that hierarchical agglomeration clustering Ž . HAC 12 is computa- <sup>w</sup> <sup>x</sup> tionally very expensive, and AutoClass has performed poorly on our examples.

Our proposed clustering algorithms, described below, are designed to efficiently handle very high dimensional spaces and large data sets, as shown in the experimental results we describe later.

2.1. Association rule hypergraph partitioning ( ) ARHP

Association rule hypergraph partitioning ARHPŽ . <sup>w</sup> <sup>x</sup> 16,17 is a clustering method based on the association rule discovery technique used in data mining. This technique is often used to discover affinities among items in a transactional database for exam-Ž ple, to find sales relationships among items sold in supermarket customer transactions . From a database . perspective, these transactions can be viewed as a relational table in which each item represents an attribute, and the domain of each attribute is either the binary domain indicating whether the item was Ž bought in a particular transaction or a nonnegative . integer indicating the frequency of purchase within a given transaction. Fig. 1 depicts a portion of a typical supermarket transaction database.

The association rule discovery methods 3 first<sup>w</sup> <sup>x</sup> find groups of items occurring frequently together in many transactions. Such groups of items are referred to as frequent item sets. In the ARHP method, we use the discovered frequent item sets to form a hypergraph, where vertices are items and each hyperedge represents a frequent item set. Then a hypergraph partitioning algorithm 20 is used to find the<sup>w</sup> <sup>x</sup> item clusters. The similarity among items is captured implicitly by the frequent item sets.

<table><tr><td>TID</td><td>Beer</td><td>Milk</td><td>Diaper</td><td>Bread</td><td>Coke</td></tr><tr><td>T1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>T2</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>T3</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>T4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>T5</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr></table>

Fig. 1. Portion of a typical supermarket transaction database.

In the document retrieval domain, it is also possible to view a set of documents in a transactional form. In this case, each document corresponds to an item and each possible feature corresponds to a transaction. The entries in the table domain of docu-Ž ment attribute represents the frequency of occur-. rence of a specified feature word in that document. Ž . A frequent item sets found using the association rule discovery algorithm corresponds to a set of documents that have a sufficiently large number of features words in common. These frequent item sets Ž . are mapped into hyperedges in a hypergraph. A typical document-feature dataset, represented as a transactional database, is depicted in Fig. 2.

A hypergraph 4<sup>w</sup> <sup>x</sup> $H = \left( V , E \right)$ consists of a set of vertices Ž . Ž . V and a set of hyperedges E . A hypergraph is an extension of a graph in the sense that each hyperedge can connect more than two vertices. In our model, the set of vertices V corresponds to the set of documents being clustered, and each hyperedge $e \in E$ corresponds to a set of related documents. A key problem in modeling data items as a hypergraph is determining what related items can be grouped as hyperedges and determining the weights of the hyperedge. In this case, hyperedges represent the frequent item sets found by the association rule discovery algorithm.

Association rules capture the relationships among items that are present in a transaction 2 . Let<sup>w</sup> <sup>x</sup> T be the set of transactions where each transaction is a subset of the item set I, and C be a subset of I. We define the support count of C with respect to T to be:

$$
\sigma (C) = | \{t | t \in T, C \subseteq t \} |.
$$

Thus, $\sigma ( C )$ is the number of transactions that contain C. An association rule is an expression of the form $X \Rightarrow ^ { s , \alpha } Y ,$ where $X \subseteq I$ and $Y \subseteq I .$ The support s of the rule $X \Rightarrow ^ { s , \alpha } Y$ is defined as $\sigma ( X \cup Y ) / | T | ,$ and the confidence is defined as $\sigma ( X \cup Y ) _ { \big / }$ $\sigma ( X )$ . The task of discovering an association rule is to find all rules $X \Rightarrow ^ { s , \alpha } Y ,$ , such that s is greater than a given minimum support threshold and is greater than a given minimum confidence threshold. The association rule discovery is composed of two steps. The first step is to discover all the frequent item sets Žcandidate sets that have support greater than the minimum support threshold specified . The second. step is to generate association rules from these frequent item sets.

![](/api/attachments/8MZCVXBM/fulltext/images/811d37fca4abe08e0cf5e5aa629eec7ccf3221d124b76d2508b66db8ec942188.jpg)  
Fig. 2. A transactional view of a typical document-feature set.

The frequent item sets computed by an association rule algorithm such as Apriori are excellent candidates to find such related items. Note that these algorithms only find frequent item sets that have support greater than a specified threshold. The value of this threshold may have to be determined in a domain-specific manner. The frequent item sets capture the relationships among items of size greater than or equal to 2. Note that distance-based relationships can only capture relationships among pairs of data points whereas the frequent items sets can capture relationship among larger sets of data points. This added modeling power is nicely captured in our hypergraph model.

The hypergraph representation can then be used to cluster relatively large groups of related items by partitioning them into highly connected partitions. One way of achieving this is to use a hypergraph partitioning algorithm that partitions the hypergraph into two parts such that the weight of the hyperedges that are cut by the partitioning is minimized. Note that by minimizing the hyperedge-cut, we essentially minimize the relations that are violated by splitting the items into two groups. Now each of these two parts can be further bisected recursively, until each partition is highly connected. For this task we use HMETIS <sup>w</sup> <sup>x</sup> 20 , a multilevel hypergraph partitioning algorithm which can partition very large hypergraphs Ž . of size <sup>)</sup>100 K nodes in minutes on personal computers.

Once, the overall hypergraph has been partitioned into k parts, we eliminate bad clusters using the following cluster fitness criterion. Let e be a set of vertices representing a hyperedge and C be a set of vertices representing a partition. The fitness function that measures the goodness of partition C is defined as follows:

$$
\text { fitness } (C) = \frac {\sum_ {e \subseteq C} \operatorname{Weight} (e)}{\sum_ {| e \cap C | > 0} \operatorname{Weight} (e)}
$$

The fitness function measures the ratio of weights of edges that are within the partition and weights of edges involving any vertex of this partition.

Each good partition is examined to filter out vertices that are not highly connected to the rest of the vertices of the partition. The connectivity function of vertex Õ in C is defined as follow:

$$
\text { connectivity } (v, C) = \frac {\left| \left\{e \mid e \subseteq C , v \in e \right\} \right|}{\left| \left\{e \mid e \subseteq C \right\} \right|}
$$

The connectivity measures the percentage of edges that each vertex is associated with. High connectivity value suggests that the vertex has many edges connecting good proportion of the vertices in the partition. The vertices with connectivity measure greater than a give threshold value are considered to belong to the partition, and the remaining vertices are dropped from the partition.

In ARHP, filtering out of nonrelevant documents can also be achieved using the support criteria in the association rule discovery components of the algorithm. Depending on the support threshold, documents that do not meet support i.e., documents thatŽ do not share large enough subsets of words with other documents will be pruned. This feature is . particularly useful for clustering large document sets which are returned by standard search engines using keyword queries.

## 2.2. Principal direction diÕisiÕe partitioning PDDP( ) algorithm

In the principal direction algorithm, each document is represented by a feature vector of word frequencies, scaled to unit length. The algorithm is a divisive method in the sense that it begins with all the documents in a single large cluster, and proceeds by splitting it into subclusters in recursive fashion. At each stage in the process, the method a selectsŽ . an unsplit cluster to split, and b splits that cluster Ž .

into two subclusters. For part a we use aŽ . scatter Õalue, measuring the average distance from the documents in a cluster to the mean 12 , though we<sup>w</sup> <sup>x</sup> could also use just the cluster size if it were desired to keep the resulting clusters all approximately the same size. For part b we construct a linear discrim-Ž . inant function based on the principal direction Žthe direction of maximal variance . Specifically, we. compute the mean of the documents within the cluster, and then the principal direction with respect to that mean. This defines a hyperplane normal to the principal direction and passing through the mean. This hyperplane is then used to split the cluster into two parts which become the two children clusters to the given cluster. This entire cycle is repeated as many times as desired resulting in a binary tree hierarchy of clusters in which the root is the entire document set, and each interior node has been split into two children. The leaf nodes then constitute a partitioning of the entire document set.

The definition of the hyperplane is based on principal component analysis, similar to the Hotelling or Karhunen–Loeve transformation 12 . We com-<sup>w</sup> <sup>x</sup> pute the principal direction as the leading eigenvector of the sample covariance matrix. This is the most expensive part, for which we use a fast Lanczos-based singular value solver 15 . By taking advantage of <sup>w</sup> <sup>x</sup> the high degree of sparsity in the term frequency matrix, the Lanczos-based solver is very efficient, with cost proportional to the number of nonzeroes in the term frequency matrix. This has been discussed in more detail in Ref. 6 .<sup>w</sup> <sup>x</sup>

This method differs from that of latent semantic indexing LSI 5 in many ways. First, LSI wasŽ . <sup>w</sup> <sup>x</sup> originally formulated for a different purpose, namely as a method to reduce the dimensionality of the search space for the purpose of handling queries: retrieving some documents given a set of search terms. Secondly, it operates on the unscaled vectors, whereas we scale the document vectors to have unit length. Thirdly, in LSI, the singular value decomposition of the matrix of document vectors itself are computed, whereas we shift the documents so that their mean is at the origin in order to compute the covariance matrix. Fourthly, the LSI method must compute many singular vectors of the entire matrix of document vectors, perhaps on the order of 100 such singular vectors, but it must do so only once at the beginning of the processing. In our method, we must compute only the single leading singular vector Ž . the vector u , which is considerably easier to obtain. Of course we must repeat this computation on each cluster found during the course of the algorithm, but all the later clusters are much smaller than the initial ‘‘root’’ cluster, and hence the later computations are much faster.

In most of our experiments, we used the norm scaling, in which each document is represented by a feature vector of word counts, scaled to unit length in the usual Euclidean norm. This leaves the sparsity pattern untouched. An alternate scaling is the TFIDF scaling 27 , but this scaling fills in all zero entries <sup>w</sup> <sup>x</sup> with nonzeroes, drastically increasing the cost of the overall algorithm by as much as a factor of 20. In spite of the increased costs, the TFIDF scaling did not lead to any noticeable improvement in the PDDP results in our experiments 7 .<sup>w</sup> <sup>x</sup>

## 2.3. Hierarchical AgglomeratiÕe Clustering HAC( )

A classical algorithm we have implemented is a bottom up HAC method based on the use of a distance function 12 . We start with trivial clusters,<sup>w</sup> <sup>x</sup> each containing one document. We cycle through a loop in which the two ‘‘closest clusters’’ are merged into one cluster. Each loop cycle reduces the number of clusters by 1, and this is repeated until the desired number of clusters is reached. For these experiments, we chose a distance function based on the ‘‘cosine’ measure essentially the cosine of the angle betweenŽ the two documents in N-space , where each cluster. was represented by its mean. The cluster means were scaled by the corresponding cluster sizes to discourage large clusters.

## 2.4. Autoclass

The other algorithm we use is AutoClass. Auto-Class 10 is based on the probabilistic mixture mod-<sup>w</sup> <sup>x</sup> eling 28 . Given a set of data <sup>w</sup> <sup>x</sup> X, AutoClass finds maximum parameter values $\hat { \vec { V } }$ for a specific probability distribution functions T of the clusters.

Given $\vec { V } = \{ \vec { V _ { C } } ~ , \vec { V _ { 1 } } , \vec { V } , \dots , \vec { V _ { k } } \}$ where $\hat { \vec { V } _ { C } } =$ $\{ \vec { \pi } _ { 1 } , \vec { \pi } _ { 2 } , \ldots , \vec { \pi } _ { k } \}$ and $\hat { \boldsymbol { \pi } } _ { j }$ is a class mixture probability, AutoClass calculates the probability that data point $X _ { i }$ belongs to class $C _ { j }$ by Bayes’ rule:

$$
P \big (X _ {i} \in C _ {j} \big) = \frac {\hat {\pi} _ {j} P \Big (X _ {i} | \hat {\vec {V}} \Big)}{\sum_ {l = 1} ^ {k} \hat {\pi} _ {l} P \Big (X _ {i} | \hat {\vec {V}} \Big)}
$$

One of the advantages of AutoClass is that it has a theoretical foundation using Bayesian statistics. The clustering results provide the full description of each cluster in terms of probability distribution of each attributes. It also works well for both discrete and continuous attributes. The results of the clustering is fuzzy, i.e., it gives probabilities of one data point belonging to different clusters. Analysts can determine the cluster membership of a data point based on these probabilities.

One of the weaknesses of AutoClass is that the underlying probability model assumes independence of attributes. In many domains, this assumption is too restrictive. Another problem with the basic model is that it does not provide a satisfactory distribution function for ordered discrete attributes 10 . Further-<sup>w</sup> <sup>x</sup> more, irrelevant attributes with respect to clustering Ž . or hidden biases may dominate the clustering process.

## 3. Experimental results

## 3.1. Experimental setup

For the experiments we present here, we selected 185 Web pages in 10 broad categories: affirmative action AA , business capital BC , electronic com-Ž . Ž . merce EC , employee rights ER , intellectual prop- Ž . Ž . erty IP , industrial partnership IPT , informationŽ . Ž . systems IS , materials processing MP , manufactur- Ž . Ž . ing systems integration MSI , and personnel man-Ž . agement PM .Ž .

These pages were obtained by doing a keyword search using a standard search engine. The pages were downloaded, labeled, and archived. The labeling facilitates an entropy calculation and subsequent references to any page were directed to the archive. This ensures a stable data sample since some pages are fairly dynamic in content.

Results we obtained in similar experiments with a smaller set of documents have been previously reported in Ref. 24 . Those documents were obtained<sup>w</sup> <sup>x</sup> in part from the Network for Excellence in Manufacturing website, on line at http:<sup>rr</sup>web.miep.org:80<sup>r</sup> miep<sup>r</sup>index.html and were used originally for the experiments described in Ref. 30 . The experiments<sup>w</sup> <sup>x</sup> we describe in this paper grew out of our initial set of experiments, and were used to validate on a larger dataset the results we obtained with our original experiments. We have conducted, more recently, another series of experiments with a much larger dataset Ž2340 documents, obtained through the Yahoo online news service that we have used to support our. scalability analysis, as described later in Section 3.2.

The word lists from all documents were filtered with a stop-list and ‘‘stemmed’’ using Porter’s suffix-stripping algorithm 25 as implemented by Ref.<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 13 . We derived 10 experiments, clustered the documents using the four algorithms described earlier, and analyzed the results. Our objective is to reduce the dimensionality of the clustering problem while retaining the important features of the documents. The 10 experiments we conducted are distinguished by further selection rules, as shown in Table 1.

Table 1 Setup of experiments

<table><tr><td>Word set</td><td>Selection criteria</td><td>Dataset size</td><td>Comments</td></tr><tr><td> $J_1$ </td><td>All words</td><td>185 × 10536</td><td>We select all non-stop words (stemmed).</td></tr><tr><td> $J_2$ </td><td>Quantile filtering</td><td>185 × 946</td><td>Quantile filtering selects the most frequently occurring words until the accumulated frequencies exceed a threshold of 0.25, including all words from the partition that contributes the word that exceeds the threshold.</td></tr><tr><td> $J_3$ </td><td>Top 20 + words</td><td>185 × 1763</td><td>We select the 20 most frequently occurring words and include all words from the partition that contributes the 20th word.</td></tr><tr><td> $J_4$ </td><td>Top 5 + plus emphasized words</td><td>185 × 2951</td><td>We select the top 5 + words augmented by any word that was emphasized in the HTML document, i.e., words appearing in &lt;TITLE&gt;, &lt;H1&gt;, &lt;H2&gt;, &lt;H3&gt;, &lt;I&gt;, &lt;BIG&gt;, &lt;STRONG&gt;, or &lt;EMPHASIZE&gt; tags.</td></tr><tr><td> $J_5$ </td><td>Frequent item sets</td><td>185 × 499</td><td>We select words from the document word list that appear in a-priori word clusters. That is, we use an object measure to identify important groups of words.</td></tr><tr><td> $J_6$ </td><td>All words with text frequency &gt;1</td><td>185 × 5106</td><td>We prune the words selected for  $J_1$  to exclude those occurring only once.</td></tr><tr><td> $J_7$ </td><td>Top 20 + with text frequency &gt;1</td><td>185 × 1328</td><td>We prune the words selected for  $J_3$  to exclude those occurring only once.</td></tr><tr><td> $J_8$ </td><td>Top 15 + with text frequency &gt;1</td><td>185 × 1105</td><td></td></tr><tr><td> $J_9$ </td><td>Top 10 + with text frequency &gt;1</td><td>185 × 805</td><td></td></tr><tr><td> $J_{10}$ </td><td>Top 5 + with text frequency &gt;1</td><td>185 × 474</td><td></td></tr></table>

## 3.2. EÕaluation of clustering results

Validating clustering algorithms and comparing performance of different algorithms is complex because it is difficult to find an objective measure of quality of clusters. We decided to use entropy 26 as<sup>w</sup> <sup>x</sup> a measure of goodness of the clusters. When a cluster contains documents from one class only, the entropy value is 0.0 for the cluster and when a cluster contains documents from many different classes, then entropy of the cluster is higher. The total entropy is calculated as the weighted sum of entropies of the clusters. We compare the results of the various experiments by comparing their entropy across algorithms and across feature selection methods Fig. 3 . Note that the hypergraph partitioning Ž . method does not cluster all the documents, so the entropy is computed only for the documents clustered.

Our experiments suggest that clustering methods based on partitioning seem to work best for this type of information retrieval applications, because:

1. they do not require calculation of the mean of randomly chosen clusters, and so the issue of having cluster means very close in space does not apply;

2. they are linearly scalable with respect to the cardinalities of the document and feature spaces Žin contrast to HAC and AutoClass which are quadratic ;.

3. the quality of the clusters is not affected by the dimensionality of the data sets.

In general, all the methods had similar behavior across the experiments in that the filtering based on word frequencies did not have any major impact, except for the frequent item set used in experiment ${ \bf J } _ { 5 } ,$ which is discussed later. Both the ARHP and PDDP methods performed better than the traditional methods except for HAC with norm scaling regard-Ž . less of the feature selection criteria.

Algorithms such as AutoClass and HAC with TFIDF scaling become computationally prohibitive as the dimensionality is increased. For example, when no feature selection criteria was used datasetŽ size of $1 8 5 \times 1 0 5 3 8 )$ , ARHP and PDDP took less than 2 min, whereas HAC took 1 h and 40 min and AutoClass took 38 min.

We have tried the PDDP algorithm on a larger dataset 2340 documents and our experiments showŽ . that the algorithm scales up linearly with the number of nonzero entries in the term frequency matrix 7 .<sup>w</sup> <sup>x</sup> As each document uses only a small fraction of the entire dictionary of words, the term frequency matrix is very sparse. In this larger dataset, only 0.68% of the entries were nonzero. The algorithm is able to take advantage of this sparsity, yielding scalable performance, as illustrated in Fig. 4.

![](/api/attachments/8MZCVXBM/fulltext/images/74a6ab654bae59963067737ef995644296170a7d5ed0306001c29810c16c94c0.jpg)  
Fig. 3. Entropy comparison of different algorithms with 32 clusters. The results shown for ARHP are for slightly different numbers of clusters for each experiment, precisely 30 clusters for $\mathbf { J } _ { 1 } ,$ 28 for $\mathrm { J } _ { 2 } ^ { \phantom { } } .$ , 32 for ${ \bf J } _ { 3 } ,$ , 35 for $\mathrm { J } _ { 4 } , 3 5$ for ${ \bf J } _ { 5 } ,$ 31 for ${ \mathrm { J } } _ { 6 } ,$ 33 for $\mathrm { J } _ { 7 } ^ { } .$ , 32 for ${ \mathrm { J } } _ { 8 } ,$ 40 for $\mathrm { { J } } _ { 9 } ,$ 30 for $\mathrm { { { J } } } _ { 1 0 } .$ . Note that lower entropy indicates better cohesiveness of clusters.

time to obtain 16 clusters by PDDP algorithm  
![](/api/attachments/8MZCVXBM/fulltext/images/c159172732aec612fdc62b30fa14bf1852d2b87b14ac641b71327354738b0c22.jpg)  
Fig. 4. Time to obtain 16 clusters for various data sets using the PDDP algorithm. The time in seconds on an SGI challenge vertical axis isŽ . plotted against the number of nonzeroes in the term frequency matrix horizontal axis .Ž .

Aside from overall performance and quality of clusters, the experiments point to a few other notable conclusions. As might be expected, in general clustering algorithms yield better quality clusters when the full set of feature is used experimentŽ $\mathbf { J } _ { 1 } ) _ { \cdot }$ . Of course, as the above discussion shows, for large datasets the computational costs may be prohibitive. It is therefore important to select a smaller set of

![](/api/attachments/8MZCVXBM/fulltext/images/d0279f7381cbe3e1aeefa1e75f6213ddd639111a9e83fbdfd2900b378ed42787.jpg)  
Fig. 5. Distribution of documents among clusters using the PDDP algorithm with or without TFIDF scaling for 16 clusters. Each column shows how many documents for each label appear in each of the clusters.

![](/api/attachments/8MZCVXBM/fulltext/images/9632fe060c254ac299e9f34000bcdf82ae1c4d8f369d905a73e1354165e6f251.jpg)  
Fig. 6. Distribution of documents among clusters using the HAC algorithm with or without TFIDF scaling for 16 clusters.

representative features to improve the performance of clustering algorithms without losing too much quality. Our experiments with various feature selection methods represented in $\mathrm { J } _ { 1 }$ through $\mathrm { { J } } _ { 1 0 }$ , show that restricting the feature set to those only appearing in the frequent item sets discovered as part of theŽ association rule algorithm , has succeeded in identi-. fying a small set of features that are relevant to the clustering task. In fact, for most algorithms, the experiment $\mathrm { J } _ { 5 }$ produced results that were better than those obtained by using the full set.

![](/api/attachments/8MZCVXBM/fulltext/images/02bfb963ca61b108057b2968303cdd7a5c49064608b32337cded305704103629.jpg)  
Fig. 7. Distribution of documents among clusters using the ARHP algorithm for 18 clusters. The last cluster contains documents that were not clustered by ARHP, which yielded 17 clusters.

It should be noted that the conclusions drawn in the above discussion have been confirmed by an earlier experiment using a totally independent set of documents 24 . <sup>w</sup> <sup>x</sup>

For any particular experiment, we can better judge the quality of the clustering by looking at the distribution of class labels among clusters. Fig. 5 shows the class distribution for the $\mathrm { J } _ { 1 }$ experiment using the PDDP algorithm with and without TFIDF scaling. Similarly, Fig. 6 shows the class distribution for the $\mathrm { J } _ { 1 }$ experiment using the HAC algorithm with and without TFIDF scaling, Fig. 7 shows the results of ARHP, and Fig. 8 shows the results of AutoClass.

![](/api/attachments/8MZCVXBM/fulltext/images/03892577e9589c86ddf3ca778e562ff487388b09605e9f6ab56ed05203981580.jpg)  
Fig. 8. Distribution of documents among clusters using the Auto-Class algorithm for 16 clusters. Not all the documents are clustered.

## 4. Related work

A number of Web agents use various information retrieval techniques 14 and characteristics of open<sup>w</sup> <sup>x</sup> hypertext Web documents to automatically retrieve, filter, and categorize these documents 8,9,11 . <sup>w</sup> <sup>x</sup>

For example, HyPursuit 29 uses semantic infor- <sup>w</sup> <sup>x</sup> mation embedded in link structures as well as document content to classify and group documents by the terms they contain and their hyperlink structures. The system requires that information be maintained in the routers.

BO Bookmark Organizer 23 combines hierar-Ž . <sup>w</sup> <sup>x</sup> chical agglomerative clustering techniques and user interaction to organize collection of Web documents listed in a personal bookmark file.

Pattern recognition methods and word clustering using the Hartigan’s K-means partitional clustering algorithm are used in 30 to discover salient HTML<sup>w</sup> <sup>x</sup> document features words that can be used in find-Ž . ing similar HTML documents on the Web. The clustering algorithm does not scale well to large numbers of documents. Broder 8 calculates a sketch<sup>w</sup> <sup>x</sup> for every document on the Web and then clusters together similar documents whose sketches exceed a threshold of resemblance. Given a document’s URL, similar documents can be easily identified, but an index for the whole WWW needs to be maintained.

Maarek and Ben Shaul 23 use the Hierarchical<sup>w</sup> <sup>x</sup> Agglomerative Clustering method to form clusters of the documents listed in a personal bookmark file. Individual documents are characterized by profile vectors consisting of pairs of lexically affine words, with document similarity a function of how many indices they share. This method may not scale well to large document searches.

The Syskill & Webert system 1 represents an<sup>w</sup> <sup>x</sup> HTML page with a Boolean feature vector, and then uses naive Bayesian classification to find Web pages that are similar, but for only a given single user profile. Balabanovic et al. 3 present a system that <sup>w</sup> <sup>x</sup> uses a single well-defined profile to find similar Web documents for a user. Candidate Web pages are located using best-first search, comparing their word vectors against a user profile vector, and returning the highest-scoring pages. A TFIDF scheme is used to calculate the word weights, normalized for document length. The system needs to keep a large dictionary and is limited to one user.

A well-known and widely used technique for dimensionality reduction is principal component analysis PCA 18 . Consider a data set withŽ . <sup>w</sup> <sup>x</sup> n data items and m variables. PCA computes a covariance matrix of size m<sup>=</sup>m, and then calculates the k leading eigenvectors of this covariance matrix. These k leading eigenvectors of this matrix are principal features of the data. The original data is mapped along these new principal directions. This projected data has lower dimensions and can now be clustered using traditional clustering algorithms such as Kmeans 19 , hierarchical clustering 19 , or Auto- <sup>w x</sup> <sup>w x</sup> Class.

PCA provides several guidelines on how to determine the right number of dimension k for given data based on the proportion of variance explained or the characteristic roots of the covariance matrix. However, as noted in Ref. 18 , different methods provide<sup>w</sup> <sup>x</sup> widely different guidelines for k on the same data, and thus it can be difficult to find the right number of dimension. The choice of a small k can lose important features of the data. On the other hand, the choice of a large k can capture most of the important features, but the dimensionality might be too large for the traditional clustering algorithms to work effectively.

Latent semantic indexing LSI 5 is a dimension-Ž . <sup>w</sup> <sup>x</sup> ality reduction technique extensively used in information retrieval domain and is similar in nature to PCA. Instead of finding the singular value decomposition of the covariance matrix, it finds the singular value decomposition of the original n<sup>=</sup>m data.

Both PCA and LSI are preprocessing methods which produce a much lower dimensional representation of the dataset for subsequent processing by another algorithm. In the context of query systems, LSI has been singularly successful in reducing the noise in the data, leading to much higher precision in results from user queries 5 . They may also be <sup>w</sup> <sup>x</sup> considered as possible preprocessing modules in the context of unsupervised clustering, and some preliminary experiments in this direction have been carried out using LSI followed by K-means and PDDP, yielding respective entropies of 0.834 and 0.859. To obtain these results, we used LSI to extract a dimension 10 approximation to the term frequency matrix, which was then used as the basis for the subsequent K-means or PDDP method.

The main difficulty with the LSI or PCA methods is the necessity to compute the k leading singular values and vectors of the term frequency matrix, where k is the desired dimension. A naive dense matrix solver takes $O ( n ^ { 3 } )$ operations to compute it and hence is prohibitively expensive. A method which takes advantage of sparsity could be used to speed this up substantially. An example is the Lanczos method 15 which has been used with great <sup>w</sup> <sup>x</sup> success in the PDDP algorithm. However, it is considerably more difficult to compute the leading k singular values and vectors in LSI than just the one leading singular vector as in PDDP. But even if the time is available, the resulting low dimension approximation will typically be dense. This substantially increases the processing cost for the subsequent clustering method as well as potentially occupying as much space as the original data, depending on the choice of k.

The Kohonen self-organizing feature map 21 is a <sup>w</sup> <sup>x</sup> neural network based scheme that projects high-dimensional input data into a feature map of a smaller dimension such that the proximity relationships among input data are preserved. On data sets of very large dimensionality such as those discussed here, convergence could be slow, depending upon the initialization.

## 5. Conclusion

In this paper we have presented two new methods for clustering, namely, ARHP and PDDP, that are particularly suitable for the type of information retrieval applications discussed above. These methods do not depend on distance measures, and perform well in high dimensional spaces.

Our experiments suggest that both of these methods perform better than other traditional clustering algorithms regardless of the techniques used for feature selection. In particular, they both perform well, even when all of the features from each document are used in clustering. In addition, the experiments suggest that if the features selected are restricted to those present in frequent item sets, such as those derived from the Apriori algorithm, then the traditional methods tend to perform better. It is also evident that, the hypergraph partitioning method may perform better, if the features selected include those words emphasized by document authors through the use of HTML tags.

Our future research plans include developing methods for incremental clustering or classification of documents after discovering an initial set of clusters. Furthermore, we plan to investigate the use of clustering techniques proposed here for word clustering. These word clusters can then be used to classify new documents or to search for related documents on the Web.

## Acknowledgements

This work was supported in part by Army Research Office contract DA<sup>r</sup>DAAG55-98-1-0441, by NSF Grant 115-98 11229, by Army High Performance Computing Research Center cooperative agreement number DAAH04-95-2-0003<sup>r</sup>contract number DAAH04-95-C-0008, the content of which does not necessarily reflect the position or the policy of the government, and no official endorsement should be inferred. Additional support was provided by the IBM Partnership Award, and by the IBM SUR equipment grant. Access to computing facilities was provided by Minnesota Supercomputer Institute.

## References

<sup>w</sup> <sup>x</sup> 1 M. Ackerman, D. Billsus, S. Gaffney, S. Hettich, G. Khoo, K. Dong Joon, J. Klefstad, K. Omori, M.J. Pazzani, D. Semler, B. Starr, P. Yap, Learning probabilistic user profiles, AI Magazine 18 2 1997 47–56.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 R. Agrawal, H. Mannila, R. Srikant, H. Toivonen, A.I. Verkamo, Fast discovery of association rules, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smith, R. Uthurusamy Ž . Eds. , Advances in Knowledge Discovery and Data Mining, AAAI<sup>r</sup>MIT Press, 1996, pp. 307–328.

<sup>w</sup> <sup>x</sup> 3 M. Balabanovic, Y. Shoham, Y. Yun, An adaptive agent for automated Web browsing, Journal of Visual Communication and Image Representation 6 4 1995 http: Ž . Ž . <sup>rr</sup>wwwdiglib.stanford.edu<sup>r</sup>cgi-bin<sup>r</sup>WP<sup>r</sup>get<sup>r</sup>SIDL-WP-1995-0023.

<sup>w</sup> <sup>x</sup> 4 C. Berge, Graphs and Hypergraphs, American Elsevier, 1976.

<sup>w</sup> <sup>x</sup> 5 M.W. Berry, S.T. Dumais, G.W. O’Brien, Using linear algebra for intelligent information retrieval, SIAM Review 37 Ž . 1995 573–595.

6 D.L. Boley, Principal direction divisive partitioning, Technical Report TR-97-056, Department of Computer Science, University of Minnesota, Minneapolis, 1997.

7 D.L. Boley, Hierarchical taxonomies using divisive partitioning, Technical Report TR-98-012, Department of Computer Science, University of Minnesota, Minneapolis, 1998.

<sup>w</sup> <sup>x</sup> 8 A.Z. Broder, S.C. Glassman, M.S. Manasse, Syntactic clustering of the Web, Proc. of 6th International World Wide Web Conference, April 1997, http:<sup>rr</sup>proceedings.www6 conf.org<sup>r</sup>HyperNews<sup>r</sup>get<sup>r</sup>PAPER205.html.

<sup>w</sup> <sup>x</sup> 9 C. Chang, C. Hsu, Customizable multi-engine search tool with clustering, in: Proc. of 6th International World Wide Web Conference, 1997.

<sup>w</sup> <sup>x</sup> 10 P. Cheeseman, J. Stutz, Baysian classification AutoClass :Ž . theory and results, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smith, R. Uthurusamy Eds. , Advances in Knowledge Dis- Ž . covery and Data Mining, AAAI<sup>r</sup>MIT Press, 1996, pp. 153– 180.

<sup>w</sup> <sup>x</sup> 11 L. Chen, K. Sycara, Webmate: a personal agent for browsing and searching, in: Proc. of 2nd International Conference on Autonomous Agents, 1998.

<sup>w</sup> <sup>x</sup> 12 R.O. Duda, P.E. Hart, Pattern Classification and Scene Analysis, Wiley, New York, 1973.

<sup>w</sup> <sup>x</sup> 13 W.B. Frakes, Stemming algorithms, in: W.B. Frakes, R. Baeza-Yates Eds. , Information Retrieval Data StructuresŽ . and Algorithms, Prentice-Hall, Englewood Cliffs, NJ, 1992, pp. 131–160.

<sup>w</sup> <sup>x</sup> 14 W.B. Frakes, R. Baeza-Yates, Information Retrieval Data Structures and Algorithms, Prentice-Hall, Englewood Cliffs, NJ, 1992.

<sup>w</sup> <sup>x</sup> 15 G.H. Golub, C.F. Van Loan, Matrix Computations, 3rd edn., Johns Hopkins Univ. Press, 1996.

<sup>w</sup> <sup>x</sup> 16 E.H. Han, G. Karypis, V. Kumar, B. Mobasher, Clustering based on association rule hypergraphs, Workshop on Research Issues on Data Mining and Knowledge Discovery, Tucson, AZ, 1997, pp. 9–13.

<sup>w</sup> <sup>x</sup> 17 E.H. Han, G. Karypis, V. Kumar, B. Mobasher, Hypergraph based clustering in high-dimensional data sets: a summary of results, Bulletin of the Technical Committee on Data Engineering 21 1 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 J.E. Jackson, A User’s Guide To Principal Components, Wiley, New York, 1991.

<sup>w</sup> <sup>x</sup> 19 A.K. Jain, R.C. Dubes, Algorithms for Clustering Data, Prentice-Hall, Englewood Cliffs, NJ, 1988.

<sup>w</sup> <sup>x</sup> 20 G. Karypis, R. Aggarwal, V. Kumar, S. Shekhar, Multilevel hypergraph partitioning: application in VLSI domain, in: Proceedings ACM<sup>r</sup>IEEE Design Automation Conference, 1997.

<sup>w</sup> <sup>x</sup> 21 T. Kohonen, Self-Organization and Associated Memory, Springer, Berlin, 1988.

<sup>w</sup> <sup>x</sup> 22 S.Y. Lu, K.S. Fu, A sentence-to-sentence clustering procedure for pattern analysis, IEEE Transactions on Systems, Man and Cybernetics 8 1978 381–389.Ž .

<sup>w</sup> <sup>x</sup> 23 Y.S. Maarek, I.Z. Ben Shaul, Automatically organizing bookmarks per contents, in: Proc. of 5th International World Wide Web Conference, May 1996, http:<sup>rr</sup>www5conf. inria.fr<sup>r</sup>fich\_html<sup>r</sup>papers<sup>r</sup>P37<sup>r</sup>Overview.html.

<sup>w</sup> <sup>x</sup> 24 J. Moore, E. Han, D. Boley, M. Gini, R. Gross, K. Hastings, G. Karypis, V. Kumar, B. Mobasher, Web page categorization and feature selection using association rule and principal component clustering, in: 7th Workshop on Information Technologies and Systems, Dec. 1997.

<sup>w</sup> <sup>x</sup> 25 M.F. Porter, An algorithm for suffix stripping, Program 14 Ž . Ž . 3 1980 130–137.

<sup>w</sup> <sup>x</sup> 26 J. Ross Quinlan, C4.5: Programs for Machine Learning. Morgan Kaufmann, San Mateo, CA, 1993.

<sup>w</sup> <sup>x</sup> 27 G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, McGraw-Hill, New York, 1983.

<sup>w</sup> <sup>x</sup> 28 D.M. Titterington, A.F.M. Smith, U.E. Makov, Statistical Analysis of Finite Mixture Distributions, Wiley, New York, 1985.

<sup>w</sup> <sup>x</sup> 29 R. Weiss, B. Velez, M.A. Sheldon, C. Nemprempre, P. Szilagyi, A. Duda, D.K. Gifford. Hypursuit: a hierarchical network search engine that exploits content-link hypertext clustering, in: Seventh ACM Conference on Hypertext, March 1996, http:<sup>rr</sup>paris.lcs.mit.edu<sup>r ;</sup>rweiss<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 30 M.R. Wulfekuhler, W.F. Punch, Finding salient features for personal Web page categories, in: Proc. of 6th International World Wide Web Conference, April 1997, http:<sup>rr</sup>proceedings.www6conf.org<sup>r</sup>HyperNews<sup>r</sup>get<sup>r</sup>PAPER118.html.

Daniel Boley received his AB degree summa cum laude in Mathematics and with distinction in all subjects from Cornell University in 1974, and his MS and PhD degrees in Computer Science from Stanford University in 1976 and 1981, respectively. Since 1981, he has been on the faculty of the Department of Computer Science and Engineering at the University of Minnesota. He has had extended visiting positions at the Los Alamos Scientific Laboratory, the IBM Research Center in Zurich Ž . Switzerland , the Australian National University in Canberra, Stanford University, and the University of Salerno Italy . Dr.Ž . Boley is known for his work on numerical linear algebra methods for control problems, parallel algorithms, iterative methods for matrix eigenproblems, error correction for floating point computations, inverse problems in linear algebra, as well as his more recent work on numerical methods in robot motion planning and unsupervised document categorization. He has been an associate editor for the SIAM Journal of Matrix Analysis and has chaired several symposia.

Maria Gini is a professor in the Department of Computer Science and Engineering at the University of Minnesota in Minneapolis. Before joining the University of Minnesota, she has been a research associate at the Politecnico of Milan, Italy, and a visiting research associate in the Artificial Intelligence Laboratory at Stanford University. Her research interests are in using artificial intelligence to build autonomous entities, such as robots and intelligent software agents. Her major contributions include robot planning and control, navigation, cooperation and coordination strategies for distributed agents, and agents for the Web, She has coauthored over 100 technical papers. She is on the editorial board of the journal ‘‘Autonomous Robots’’ and ‘‘Integrated Computer-Aided Engineering’’ and on the advisory board of IJCAI-99.

Robert L. Gross is a native of St. Paul, MN. After receiving his Bachelor of Electrical Engineering degree from the University of Minnesota, he worked as a systems engineer for Sperry Univac on air traffic control systems. As a member of the Franciscan Order he continued to use his technical skills in the United States, France, and Zaire in various positions. Returning to the University of Minnesota, he pursued graduate studies in computer science, focusing on the clustering of information in web pages and analyzing systems for its efficient retrieval. He graduated with a Masters of Computer and Information Sciences degree in 1998. He is currently employed as a software engineer for Silicone Graphics in Eagan, MN. He is a member of ACM.

Eui-Hong Han is a PhD candidate in the Department of Computer Science and Engineering at the University of Minnesota. He holds a BS in Computer Science from the University of Iowa and an MS in Computer Science from the University of Texas at Austin. He worked at CogniSeis Development and IBM for several years before joining the PhD program. His research interests include high performance computing, clustering, and classification in data mining.

Kyle Hastings holds a BS in Computer Science from the US Naval Academy and an MS in Computer and Information Sciences from the University of Minnesota. His research interests include software engineering, information system security, and information warfare. Kyle is currently a cryptologic officer in the US Navy.

George Karypis received his PhD in Computer Science at the University of Minnesota, and he is currently an assistant professor at the department of Computer Science and Engineering at the University of Minnesota. His current research interests spans the areas of parallel algorithm design, applications of parallel processing in scientific computing and optimization, sparse matrix computations, and data mining. His research has resulted in the development of software libraries for serial and parallel unstructured graph partitioning Ž . METIS and ParMETIS , and for parallel Cholesky factorization Ž . PSPASES . He has coauthored several journal articles and conference papers on these topics and a book titled ‘‘Introduction to Parallel Computing’’ Publ. Benjamin Ž Cummings<sup>r</sup>Addison Wesley, 1994 ..

Vipin Kumar is currently a professor of Computer Science and Engineering at the University of Minnesota. His current research interests include High Performance computing, and data mining. His research has resulted in the development of highly efficient parallel algorithms and software for sparse matrix factorization Ž . Ž . PSPACES , graph partitioning METIS, ParMETIS , and VLSI circuit partitioning Ž . HMETIS . He has authored over 100 research articles, and coedited or coauthored 5 books including the widely used text book ‘‘Introduction to Parallel Computing’’ Publ. Benjamin Ž Cummings<sup>r</sup>Addison Wesley, 1994 . Kumar serves on the edito-. rial boards of IEEE Concurrency, Parallel Computing, the Journal of Parallel and Distributed Computing, and served on the editorial board of IEEE Transactions of Data and Knowledge Engineering during 1993–1997. He is a senior member of IEEE, a member of SIAM, and ACM, and a Fellow of the Minnesota Supercomputer Institute.

Bamshad Mobasher is currently an assistant professor of Computer Science at DePaul University. From 1995–1998, he served as an assistant professor of Computer Science at the University of Minnesota. He received his PhD from Iowa State University in 1994. He has been active in several research areas, including autonomous software agents, multi-agent systems, data mining on the World Wide Web, and semantics of uncertainty and inconsistency in knowledge-based systems. His research projects at the University of Minnesota include the WebACE project which involves the development of a Web agent for document categorization and retrieval, the MAGNET project which is a multi-agent market for automated contracting and electronic commerce, and the WEBMINER project to develop a Web usage mining and analysis system. Dr. Mobasher recently served on the organizing committee and the registration chair for the Second International Conference on Autonomous Agents Agents ’98 which was heldŽ . in Minneapolis in May 1998.

Jerry Moore obtained his MS degree in Computer Science at the University of Minnesota in 1998. Currently, he is with the Minneapolis Star Tribune supporting the newspaper’s award winning web site. His interests include user interface design, data mining, and artificial intelligence.
