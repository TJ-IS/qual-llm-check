---
otero_id: 10854
otero_key: "MQKA5SFN"
title: "A scalable decision tree system and its application in pattern recognition and intrusion detection"
authors: "Xiao-Bai Li"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.06.016"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A scalable decision tree system and its application in pattern recognition and intrusion detection

Xiao-Bai Li<sup>\*</sup>

College of Management, University of Massachusetts Lowell, One University Avenue, Lowell, MA 01854, United State

Received 31 January 2003; received in revised form 4 June 2004; accepted 9 June 2004 Available online 26 August 2004

## Abstract

One of the most challenging problems in data mining is to develop scalable algorithms capable of mining massive data sets whose sizes exceed the capacity of a computer’s memory. In this paper, we propose a new decision tree algorithm, named SURPASS (for Scaling Up Recursive Partitioning with Sufficient Statistics), that is highly effective in handling such large data. SURPASS incorporates linear discriminants into decision trees’ recursive partitioning process. In SURPASS, the information required to build a decision tree is summarized into a set of sufficient statistics, which can be gathered incrementally from the data, by reading a subset of the data from storage space to main memory one at a time. As a result, the data size that can be handled by this algorithm is independent of memory size. We apply SURPASS to three large data sets pertaining to pattern recognition and intrusion detection problems. The results indicate that SURPASS scales up well against large data sets and produces decision tree models with very high quality. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision trees; Data mining; Classification; Linear discriminants; Pattern recognition; Intrusion detection

## 1. Introduction

In recent years, we have observed an explosion of electronic data generated and collected by individuals and organizations. The widespread use of computers and the Internet for transaction processing and the advances in storage technology and database systems have allowed us to generate and store mountains of data. This rapid growth in data and databases has created the problem of data overload. The technology to analyze massive data sets has lagged far behind the technology to collect and store the data. There has been an urgent need for new techniques and tools that can extract useful information and knowledge from massive volumes of data. Consequently, data mining techniques have emerged and flourished in the past several years to meet this demand.

Data mining techniques have been applied to a wide variety of application domains, including database marketing, credit and loan evaluation, fraud detection, Internet traffic analysis, Web usage profiling, pattern recognition, medical diagnostics, and genome sequencing. This study concerns mining large-scale data for pattern recognition and intrusion detection problems. Pattern recognition can be viewed broadly as the study of how to use computers and other automatic means to learn patterns of interest from their background environment and make reasonable decisions about the essential natures of the patterns. Nobel Laureate Herbert Simon emphasized that his central finding was that pattern recognition is critical in human decision-making process [33]. In the broad sense, many data mining problems mentioned above, such as credit evaluation, Web usage profiling, and medical diagnostics, can also be regarded as pattern recognition. In this study, however, we focus on more traditional pattern recognition problems, such as image pattern recognition, network intrusion detection, and related geographic information systems applications.

Pattern recognition is a process that involves basically three steps: (1) data acquisition, where data are collected with computers or other devices; (2) data processing, where the collected data are transformed through feature selection, extraction, and reconstruction; and (3) pattern analysis and identification, where decision support models are built based on the processed data using classification techniques, such as neural networks and decision trees, and later used for predicting the patterns. There are some characteristics and properties that are unique to pattern recognition data. First, technologies used to generate and collect data, such as remote sensing and image scanning devices, can easily produce tera- and petabytes of data very quickly. Consequently, it is often required that techniques used to process the data and build decision support models for pattern recognition should be able to handle large-scale data. Second, in most pattern-recognition problems, attributes and features in the original and processed data are of mostly numeric type because these attributes and features are usually numeric measurements. Therefore, techniques used to build decision support models must be able to deal with numeric attributes effectively. Third, it has been observed in various studies [2,18,27] that the behavior of the pattern recognition data often cannot be described by statistical distributions, such as normal or binomial distribution, which implies that traditional parametric statistical approaches might not be effective for pattern recognition problems. Finally, a pattern recognition problem often involves more classes than the other classification problems do.

Intrusion detection can be regarded as a special type of pattern recognition. Intrusion detection techniques are utilized to identify illegal use and abuse of computer information systems, to protect the availability, integrity, and confidentiality of the systems. The conventional approach to system and network security is to build a protective shield (e.g., firewalls) around the system to prevent an intruder from entering it. Intrusion detection techniques are based on the beliefs that an intruder’s behavior is different from that of a normal user and that the patterns of intrusions can be learned and detected by intelligent computer systems. Because of its increasing importance in today’s business and technology, research interests in intrusion detection have been growing steadily recently [1,7,21], including studies that apply data mining techniques to the problems [15,16,37].

The process of intrusion detection is similar to that of pattern recognition described earlier. Usually, raw audit data are first collected from the network system. These data are then processed and converted into connection records, where feature selection and reconstruction are often involved. Classification techniques are then applied to the processed data to build detection models. Because network systems are capable of generating huge volumes of data in a short period, intrusion detection systems are often required to handle large-scale data. Attributes and features in the processed data are mostly of numeric and binary types (e.g., frequency counts, numeric measurements, status indicators, etc.). In addition, intrusion detection normally involves classification problems with many classes because the objective is, often, not only to distinguish between an intrusion and a normal usage, but also to identify individual intrusion patterns.

This study focuses on the model building and pattern classification step of the pattern recognition process. We consider using decision tree techniques for the classification problem. As one of the most popular data mining methods, the decision tree techniques have been used extensively in pattern recognition and intrusion detection [15,18,27,37]. In this study, we develop a scalable decision tree system that is highly effective in mining data that are huge in volume, of numeric type in nature, and typically involving more than two classes. We introduce the notion of aggregable sufficient statistics and show that the set of sufficient statistics used in the classical linear discriminant analysis (LDA) is aggregable. We demonstrate that, when LDA is incorporated into decision trees’ recursive partitioning process, the set of statistics can be computed incrementally by reading the data from storage space to main memory one record at a time. As a result, there is virtually no need for storing raw data in the main memory. The algorithm developed in this study is, we believe, the first scalable multivariate tree algorithm. Moreover, the algorithm is flexible in choosing either a single attribute or a linear combination of multiple attributes to form a split. Therefore, it can generate a decision tree with univariate splits only, multivariate splits only, or a mixed form having both types of splits, depending on which structure best fits the patterns underlying the data. We apply the proposed algorithm to three large data sets pertaining to pattern recognition and intrusion detection problems. The results indicate that the proposed algorithm handles large data very efficiently, produces decision tree models with very high quality, and is quite adaptive to different patterns.

The remainder of the paper is organized as follows. In the next section, we provide a brief introduction to decision trees and an overview of existing studies on decision trees for mining large-scale data. Section 3 first describes the idea of linear discriminant analysis and the notion of sufficient statistics and then presents the proposed Scaling Up Recursive Partitioning with Sufficient Statistics (SURPASS) algorithm. An example is given in Section 4 to illustrate how the algorithm works. In Section 5, the SURPASS algorithm is applied to three large data sets pertaining to pattern recognition and intrusion detection problems and is compared with an existing scalable decision tree algorithm and linear discriminant analysis. We conclude our study in Section 6 and discuss possible extensions based on our current work.

## 2. Decision trees for mining large-scale data

Decision trees build classification models based on recursive partitioning of data. Typically, a decision tree algorithm begins with the entire set of data, splits the data into two or more subsets based on the values of one or more attributes, and then repeatedly splits each subset into finer subsets until the size of each subset reaches an appropriate level. The entire modeling process can be represented in a tree structure, and the model generated can be summarized as a set of <sup>b</sup>if–then<sup>Q</sup> rules. Decision trees are easy to interpret, computationally inexpensive, and capable of coping with noisy data. Therefore, the techniques have been widely used in various applications, including pattern recognition [18], credit and loan evaluation [28,32], Web traffic prediction [28], fraud and network intrusion detection [15,37], and medical diagnosis and healthcare management [35]. The majority of decision trees deal with the classification problem, which is also the primary concern of this paper. In this context, the technique is also referred to as classification trees.

In tree-structured representations, a set of data is represented by a node, and the entire data set is represented as a root node. When a split is made, several child nodes, which correspond to partitioned data subsets, are formed. If a node is not to be split any further, it is called a leaf; otherwise, it is an internal node. In this paper, we deal with binary trees, where each split produces exactly two child nodes. To illustrate the idea of decision trees, consider the bivariate two-class problem shown in Fig. 1, where the partitioned data are plotted in the upper part of the figure (with two classes represented by circles and triangles) and the related decision tree is shown in the lower part. Each path from the root to a leaf in a tree constitutes a rule that can be used to classify a data point. For example, the path along the left branches forms the classification rule, ${ } ^ { 6 6 } \mathrm { i f } X _ { 1 } { < } 2$ and $X _ { 2 } { < } 1$ , then classify the data point to triangle.<sup>Q</sup>

When a data point falls in a partitioned region, a decision tree classifies it as belonging to the most frequent class in that region. The error rate is the total number of misclassified points divided by the total number of data points; and the accuracy rate is one minus the error rate. It can be seen from the graph that very few data points are misclassified by this tree model. The splitting attributes and their values in decision trees are determined by a sort-and-search procedure, in conjunction with an impurity measure. The reader is referred to Refs. [4,32] for more details on these subjects.

![](/api/attachments/MQKA5SFN/fulltext/images/7a9943a4e1bdefa2e0b16b161cf810265cbe7a71db116a8db8a3975f31a1332e.jpg)  
Fig. 1. A univariate classification tree.

Two of the most popular decision tree systems are CART [4] and C4.5 [30,32]. Other well-known decision tree algorithms are described in Refs. [13,22,25]. These decision trees all assume that the entire data set can be loaded into memory for manipulation. They are not applicable to a data set that cannot fit in main memory. There are basically two groups of approaches to dealing with large data sets whose sizes are beyond the capacity of main memory. The first approach involves reducing the data set into a subset or dividing it into multiple subsets and running a decision tree algorithm on the reduced subsets. Methods along this line include instance sampling and reconstruction [19], feature selection [14,28], and multiple-trees approach, such as bagging and boosting [5,8]. We do not intend to discuss this approach in this paper. For a comprehensive survey of the methods in this approach, see Ref. [29]. The second approach attempts to build decision trees based on the entire data set, using a scalable data access method, where the term scalable refers to the property that the runtime of an algorithm increases linearly with the number of records in the data set, particularly in cases where the data size exceeds memory size. Typically, a scalable algorithm reads the data from disk to memory in batches, extracts the information needed for building the decision trees, stores and updates this information in a set of small data structures in main memory, and releases the memory space occupied by the current batch of data before reading the next batch. In this way, the scalable algorithm is able to handle a large data set whose size exceeds memory size.

There exist quite a few studies on scalable decision tree algorithms. One of the earliest scalable algorithms, named SLIQ [23], uses a presorting procedure to handle numeric splits and a subsetting procedure for categorical splits. SLIQ implements a breadth-first (instead of traditional depth-first) tree growing strategy. The presorting and breadth-first techniques significantly reduce the cost of evaluating numeric attributes. However, SLIQ requires a data structure to stay memory resident during the entire tree-building process. Because the size of this in-memory data structure is proportional to the number of records in the entire data set, the size of data that SLIQ can handle is therefore limited. To overcome this limitation, an improved scalable algorithm, called SPRINT, was proposed in Ref. [34], where the requirement on the potentially large in-memory data structure was removed. For each attribute, SPRINT creates a data structure, called an attribute list, which is a vertical partition of the training data, and stores it in a disk file. Each row of the jth attribute list contains the record index, the value of the jth attribute for the record, and the class value of the record. The list is sorted by the attribute value at the beginning of the process if the attribute is numeric. At each node, the algorithm scans each attribute list once to find the best split. Then, the attribute list file with the best splitting attribute is partitioned into two files, representing two child nodes on the tree (binary split). Each of the other attribute lists is subsequently partitioned into two files based on a hash table that links the record index in the attribute list containing the best splitting attribute with that of the other attribute lists. SPRINT scales well on large data sets, but it also has some drawbacks. For example, maintaining the attribute lists and the hash table can cost significant increases in storage space and scanning/running time.

The RainForest framework, proposed in Ref. [10], approaches the scalability problem somewhat differently from SLIQ and SPRINT. Observing that most splitting criteria need only aggregate information to find the best split at each node, RainForest uses an inmemory data structure, called the attribute-value class label group or AVC group, to store this aggregate information. For categorical attributes, the AVC group contains the frequency count of each category in each attribute for each class. The size of the AVC group depends on the numbers of classes and attributes and the number of categories of each attribute, which is usually much smaller than memory size. For numeric attributes, RainForest treats each distinct numeric value as a discrete number and stores its frequency in the AVC group in a similar way as a value of a categorical attribute. Hence, the size of the AVC group for a numeric attribute is proportional to the number of distinct values in the attribute, which can be potentially very large.

In another related study conducted by a group of researchers in Microsoft [11], the aggregate information mentioned above was referred to as sufficient statistics. The study focuses on collecting the sufficient statistics needed to build decision trees using the query processing tools, such as SQL, in a relational database environment. The main purpose of the study is to propose a new SQL operator to collect sufficient statistics directly in a database and thus avoid moving a large volume of data from databases to learning systems. However, the method discussed in the study is applicable to categorical data only, and the sufficient statistics discussed there are merely frequency count. No solution for numeric data was discussed. In addition, the study does not propose any new decision tree algorithm.

It becomes clear that the presence of numeric data causes a bottleneck problem to all of existing scalable algorithms. Some researchers even believe that it is impossible to efficiently collect sufficient statistics of numeric data for scalable decision trees (Ref. [36], p. 323). In this paper, we propose a new decision tree algorithm, named Scaling Up Recursive Partitioning with Sufficient Statistics (SURPASS), that is specialized in handling large numeric data such as those found in pattern recognition and intrusion detection problems. SURPASS incorporates a classical statistical method, linear discriminant analysis, into decision trees’ recursive partitioning process. In SURPASS, the information required to build a decision tree can be summarized into a set of sufficient statistics, represented in a few vectors and matrices, whose size depends only on the number of attributes and of classes in the data. The set of these sufficient statistics can be computed incrementally by reading the data from disk to main memory one record at a time. As a result, there is virtually no need for storing raw data in main memory.

## 3. SURPASS—A scalable decision tree algorithm using linear discriminants

Linear discriminant analysis (LDA) deals with classification problems. For a two-class data set, let $n _ { 1 }$ and $n _ { 2 } , \ \bar { \bf X } _ { 1 }$ and $\bar { \mathbf { X } } _ { 2 } ,$ and $\mathbf { S } _ { 1 }$ and $\mathbf { S } _ { 2 }$ be the sample sizes, sample mean vectors, and sample covariance matrices for the class 1 and class 2 data, respectively. The linear discriminant function is given by

$$
y = (\bar {\mathbf {x}} _ {1} - \bar {\mathbf {x}} _ {2}) ^ {T} \mathbf {S} ^ {- 1} \mathbf {x},\tag{1}
$$

where S is the pooled sample covariance matrix, defined by

$$
\mathbf {S} = \frac {(n _ {1} - 1) \mathbf {S} _ {1} + (n _ {2} - 1) \mathbf {S} _ {2}}{(n _ {1} + n _ {2} - 2)}.\tag{2}
$$

A grouping or classification rule can be constructed based on this function. For example, the Anderson rule assigns a data point, $\mathbf { X } _ { 0 } ,$ to group 1 if

$$
\begin{array}{l} \left(\bar {\mathbf {x}} _ {1} - \bar {\mathbf {x}} _ {2}\right) ^ {T} \mathbf {S} ^ {- 1} \mathbf {x} _ {0} > \frac {1}{2} \left(\bar {\mathbf {x}} _ {1} - \bar {\mathbf {x}} _ {2}\right) ^ {T} \mathbf {S} ^ {- 1} \left(\bar {\mathbf {x}} _ {1} + \bar {\mathbf {x}} _ {2}\right) \\ + \log (n _ {2} / n _ {1}) \end{array}\tag{3}
$$

and group 2 otherwise. This rule can be extended to classification problems with more than two classes by using more than one split.

LDA attempts to find a linear hyperplane that makes the best separation between different classes of data points. It transforms the multidimensional data into one dimension such that the distance between two class centroids is maximized. The key underlying assumption in deriving Eqs. (1) and (3) is that the data follow a multivariate normal distribution; but the method works well as long as the assumption is not seriously violated. [Eqs. (1) and (3) also assume a common covariance matrix for the two classes, but there are other LDA formulations dealing with unequal covariance matrices.] Due to its closed form solution, LDA is conceptually simple and computationally very efficient. However, because it uses a single function as its classification model, LDA becomes very ineffective when the classification problem is nonlinear, i.e., when different groups cannot be neatly separated by a linear hyperplane. On the other hand, univariate classification trees, which use a single attribute in each split, are often able to handle nonlinear problems very well, but sometimes less effective when the boundary between two classes is naturally oblique.

To illustrate these situations, consider the bivariate two-class problem shown in Fig. 2. The LDA model can be represented by the single straight line in the graph. This simple function does not work well; it has a rather high misclassification rate. The univariate decision tree classifier can be represented by the combination of seven line segments (staircase dashed lines). This indicates that the tree model may need a series of seven tests to classify a data point. Note that, even if such an effort is made, one circle is still misclassified as a triangle. The classification model to be proposed in this study can be represented by the two thick lines in the graph. The logical representation of the model, shown in the lower portion of Fig. 2, is clearly a tree structure. This model may use multiple attributes, as shown by the oblique thick line, or a single attribute, as shown by the vertical thick line (which overlaps the first split in the univariate tree). Note that this model fits the training data perfectly (no misclassification error).

![](/api/attachments/MQKA5SFN/fulltext/images/b875188d1733cf6742b80ca345e977ed691e96b320c4c8bccaefce1e8aad54cd.jpg)  
Fig. 2. A multivariate classification tree.

The use of a linear combination of multiple attributes in splitting data has been proposed by a number of researchers. Most of the existing multivariate tree algorithms, particularly those implemented in publicly or commercially available systems (e.g., CART [4] and OC1 [25]), still follow the sort-and-search approach to finding an appropriate split at each node, which is similar to that employed in univariate trees. Algorithms that apply linear discriminant analysis to the decision tree-building process were developed in Refs. [9,18,20]. The primary objective of these multivariate methods is to improve classification accuracy, however. None of the existing multivariate decision trees can handle a large data set whose size exceeds main memory capacity. Hence, the algorithm we develop in this paper is, to the best of our knowledge, the first multivariate algorithm that scales up to such large data sets. To describe the algorithm more accurately, we first define some terms.

Definition 1. A set of quantities extracted from a given data set is called a sufficient statistic for a decision tree algorithm if it contains all the information required by the algorithm to build the decision tree model on the given data set.

Note that sufficient statistics are not necessarily unique (e.g., the complete data set itself is a sufficient statistic). We are interested only in the sufficient statistics that take minimal storage space.

Definition 2. Given a data set $D ,$ partition the data horizontally into two arbitrary subsets, $D _ { 1 }$ and $D _ { 2 }$ . Let $S , S _ { 1 }$ , and $S _ { 2 }$ be the sufficient statistics of $D , D _ { 1 }$ , and

$D _ { 2 } ,$ respectively. The sufficient statistic S is said to be aggregable if S can be computed directly from $S _ { 1 }$ and $S _ { 2 }$ without accessing D.

It is straightforward to extend the definition to the cases of more than two subsets. Clearly, if sufficient statistics for an algorithm are aggregable, then the algorithm will be able to load a subset of the data into memory, compute sufficient statistics of the subset, and free up the memory space occupied by the current subset before loading the next subset. The sufficient statistics for the entire data can be derived at the end, based on the sufficient statistics of each subset. It is worth pointing out that the notion of aggregable sufficient statistics can be applied to other data mining algorithms to solve various data mining problems, such as numeric prediction,clustering, and association rules mining.

All of the scalable decision tree algorithms mentioned in Section 2 use splitting criteria that are essentially based on frequency counts when the splitting attribute is categorical. It is obvious that the frequency count is aggregable because the frequency count of a category in the full set is simply the sum of those counts in all subsets. This is the key reason that most scalable algorithms have no problem of handling categorical attributes. When dealing with numeric attributes, most algorithms adopt the sort-and-search approach to find the best split. The sufficient statistics for the sort-and-search approach are the rank orders of distinct values in each numeric attribute. Unfortunately, the rank orders are not aggregable. For example, knowing the median or quartiles of an attribute in each subset does not help in finding the median or quartiles of that attribute in the full set. Moreover, the size of the sufficient statistics in the sort-and-search approach (i.e., sorted distinct values) can be potentially very large when the data is of truly continuous type. These undesirable properties of the sort-and-search approach become the major hurdle that handicaps most existing scalable algorithms. They must either maintain all distinct values in large in-memory data structures (e.g., SLIQ and RainForest) or, when it is impossible to do so, store all sorted data in external disk files (e.g., SPRINT).

In the field of statistics, the most common forms of summary statistics for numeric attribute are the mean and sum of the data. It is easy to show that the mean and sum are aggregable. This property has apparently been overlooked in the existing studies on scalable decision trees. Our proposed algorithm performs recursive partitioning of data using the splitting functions that are based on Eqs. (1) and (3). Therefore, the sufficient statistic used for the proposed algorithm is a set of statistics, {n,x¯, S}. This set of sufficient statistics is aggregable, as formally stated in Theorem 1 below.

Theorem 1. The sufficient statistic {n,x¯ ,S} formed by sample size $n ,$ mean vector x¯ , and covariance matrix S of a data matrix is aggregable.

Proof. Let $p$ be the number of attributes in the data matrix X. Denote two arbitrary subsets of X as $\mathbf { X } ^ { ( 1 ) }$ and $\mathbf { X } ^ { ( 2 ) }$ . Let $n , n ^ { ( 1 ) } , n ^ { ( 2 ) } , \bar { \mathbf { x } } , \bar { \mathbf { x } } ^ { ( 1 ) } , \bar { \mathbf { x } } ^ { ( 2 ) } , \mathbf { S } , \mathbf { S } ^ { ( 1 ) }$ , and $\mathbf { S } ^ { ( 2 ) }$ be the sample sizes, mean vectors, and covariance matrices of $\mathbf { X } , \hat { \mathbf { X } } ^ { ( 1 ) }$ , and $\mathbf { X } ^ { ( 2 ) }$ , respectively. Clearly, n and x¯ can be computed based on $\bar { n } ^ { ( 1 ) } , n ^ { ( 2 ) } , \bar { \mathbf { x } } ^ { ( 1 ) }$ and $\bar { \mathbf { X } } ^ { ( 2 ) }$

$n = n ^ { ( 1 ) } + n ^ { ( 2 ) }$ ; and

$$
\begin{array}{l} \bar {x} _ {j} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i j} = \frac {1}{n} \bigg (\sum_ {i = 1} ^ {n ^ {(1)}} x _ {i j} ^ {(1)} + \sum_ {i = 1} ^ {n ^ {(2)}} x _ {i j} ^ {(2)} \bigg) \\ = \frac {1}{n} \bigg (n ^ {(1)} \bar {x} _ {j} ^ {(1)} + n ^ {(2)} \bar {x} _ {j} ^ {(2)} \bigg), j = 1, \ldots , p. \end{array}\tag{4}
$$

The covariance matrix S has a $p { \times } p$ dimension with the $( j , r )$ entry defined as

$$
s _ {j r} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(x _ {i j} - \bar {x} _ {j}\right) \left(x _ {i r} - \bar {x} _ {r}\right).\tag{5}
$$

It follows from algebraic manipulation that

$$
s _ {j r} = \frac {1}{n - 1} \left(\sum_ {i = 1} ^ {n} x _ {i j} x _ {i r} - n \bar {x} _ {j} \bar {x} _ {r}\right).\tag{6}
$$

By Eq. (4), the second term in Eq. (6) can be derived from corresponding means for $\mathbf { X } ^ { ( 1 ) }$ and $\mathbf { X } ^ { ( 2 ) }$ The first term can be partitioned as

$$
\sum_ {i = 1} ^ {n} x _ {i j} x _ {i r} = \sum_ {i = 1} ^ {n ^ {(1)}} x _ {i j} ^ {(1)} x _ {i r} ^ {(1)} + \sum_ {i = 1} ^ {n ^ {(2)}} x _ {i j} ^ {(2)} x _ {i r} ^ {(2)}.\tag{7}
$$

The summation terms on the right hand side are known quantities once $\bar { \mathbf { x } } ^ { ( 1 ) } , ~ \bar { \mathbf { x } } ^ { ( 2 ) } , ~ \mathbf { \breve { S } } ^ { ( 1 ) }$ <sup>)</sup>, and $\mathbf { S } ^ { ( 2 ) }$ are known becase the elements of $\mathbf { S } ^ { ( 1 ) }$ and $\mathbf { S } ^ { ( 2 ) }$ can also be expressed in the form of Eq. (6). This completes the proof.

There is a distinction between the proposed algorithm and existing LDA based algorithms in terms of classifying data points. Our model classifies data based on the majority class at a node (the same rule as in univariate trees), while other LDA-based algorithms strictly follow Eq. (3) or its variants. To apply Eq. (3) for splitting data, it is not necessary to use all attributes in the data. In particular, Eq. (3) can be applied to a single attribute. In this case, the mean vector and covariance matrix each reduces to a scalar (individual mean and variance, respectively). Our proposed algorithm considers splits based not only on the linear combination of all attributes but also on each individual attribute. That is, if the data have $p$ attributes, then there will be $p { + } 1$ candidate splits at each node. Because there are multiple candidates at each node, an impurity measure is needed to evaluate the quality of the splits and select the best one as the formal split. The impurity measure employed in this algorithm is entropy [32]. It is one of the most popular measures of impurity, and its performance in classification accuracy is among the better ones according to various empirical studies [12,32].

The model generated by the proposed algorithm can be very flexible. When the model contains only one split that uses a linear combination of all variables, its form is identical to LDA, except for the difference in declaring the class of a partitioned set mentioned above. When the model includes a set of tests and each test involves only a single variable, it is a univariate classification tree, although it uses a different splitting criterion than other univariate tree algorithms do. The reason that we consider a univariate split is that it may generate a better split than a multivariate split. This occurs more frequently when the size (number of records) of a node is relatively small compared with the dimension (number of attributes) of the data. In this case, the problem of singular or near singular covariance matrices arises when using the linear combination of all attributes. Another desirable property of the proposed algorithm is that its search space is limited to only $p { + } 1$ candidate splits, each of which is optimal (in terms of distance maximization) in its corresponding dimension space.

The time complexity involved in computing linear discriminant function at each node is linear in the number of records, n, at the current node because the computation is dominated by summing up attribute values and n is dominantly larger than $p ,$ the number of attributes. On the other hand, the time complexity of the sort-and-search algorithms at each node is of order O(nlog n) because the procedure is dominated by sorting operations.

A disadvantage of our proposed method, which is common to all multivariate trees, is that the rules involving several attributes are more difficult to interpret than those with a single attribute. However, empirical studies indicate that multivariate trees usually have fewer nodes than univariate trees do. This partially alleviates the interpretation problem. In addition, if a multivariate tree indeed reflects the true pattern of the data, the rules formed by a univariate tree can be misleading. In terms of classification accuracy, empirical studies (e.g., Ref. [6]) show that multivariate decision trees generally have higher accuracy than univariate trees do, although they might not perform well when the boundaries between different classes are essentially axis-parallel. The proposed SURPASS algorithm can generate both multivariate and univariate splits. Its power, however, relies more on the multivariate split. It tends to be less effective when forced (by the underlying pattern) to use univariate split only. Another disadvantage of multivariate trees is that they are primarily applicable to numeric data. When categorical data are presented, categorical values need to be processed with binary (0–1) coding, which is not trivial when the number of categories of an attribute is large. We discuss this problem and propose a solution in Section 6.

For the classification problems with more than two classes, we adopt the procedure proposed in Ref. [18]. The basic idea is to first group the data into two superclasses to apply Eq. (3). The superclasses are selected such that the Euclidean distance between the two superclass centroids is as large as possible. An exhaustive search for the optimal solution to this problem is computationally expensive. Therefore, a tabu search method is used to make searching time linear in the number of classes. Having described the details of our algorithm, we now summarize the SURPASS algorithm in Fig. 3. Note that it requires only a single pass of the data at the

0. Let $p$ and c be the number of attributes and classes of the data, respectively. Create c vectors of (p + 1) -dimension, $\mathbf { v } _ { 1 } , \ldots , \mathbf { v } _ { c }$ , where the jth entry of $\mathbf { v } _ { k }$ stores the sum of the jth attribute values $x _ { \mathit { i } } \left( \mathit { j } = 1 , . . . , p \right)$ for class k data. Create c matrices of $p \times p$ dimension, $\mathbf { w } _ { 1 } , \ldots , \mathbf { w } _ { c }$ , where the $( j , r )$ entry of $\mathbf { w } _ { k }$ stores the sum of cross-product values $x _ { j } x _ { r } \left( j = 1 , . . . , p ; r = 1 , . . . , p \right)$ for class k data. Set the minimum impurity measure, $e _ { \mathrm { m i n } }$ , to an arbitrarily large number.

1. Let n be the number of records in the dataset represented by the current node, where the data is stored in a disk file D. Compute the sufficient statistics as follows. For i = 1 to $^ { n , }$ do:

a. Read the ith record from the file D to memory.

b. Let k be the class value of this record. Compute the values of $x _ { j } x _ { r }$ for this record, and add x, and $x _ { j }$ $x _ { j } x _ { j }$ values to the respective entries in $\mathbf { v } _ { k }$ and $\mathbf { W } _ { k }$ c. Free the memory space used by this record.

2. Make the best split at the current node:

a. Group the data into two superclasses using the superclass selection procedure in [18]. Combine (by adding entries of the same position) all v vectors of superclass 1 into one vector $\mathbf { V } _ { 1 }$ , and all w matrices of superclass 1 into one matrix $\mathbf { W } _ { 1 }$ . Similarly, construct vector $\mathbf { V } _ { 2 }$ and matrix $\mathbf { W } _ { 2 }$ for super class 2.

b. Compute the mean vectors and covariance matrices for the two superclasses of the data, based on $\mathbf { V } _ { 1 } , \ \mathbf { V } _ { 2 } , \ \mathbf { W } _ { 1 }$ and $\mathbf { W } _ { 2 }$

c. Compute equation (1) and split the data according to equation (3) into two candidate subsets.

d. Compute the impurity value, e, for this split. If $e < e _ { \mathrm { m i n } }$ , set $e _ { \operatorname* { m i n } } = e$

e. Repeat steps (c) and (d) for p more times, each using a different single attribute.

f. Select the split corresponding to $e _ { \mathrm { m i n } }$ and partition the data at this node accordingly into two subsets (child nodes).

3. Reset the values of v vectors and w matrices to 0 and repeat steps 1 and 2 for each of the two child nodes. Stop the process when the node contains less than a pre-specified number of records.

Fig. 3. The SURPASS algorithm.

current node for the algorithm to obtain the required sufficient statistics.

The algorithm described so far concerns growing decision trees. Another important aspect in building the decision tree model is pruning. The most commonly used pruning methods include cost-complexity pruning [4] and pessimistic-error pruning [31,32]. Cost-complexity pruning is more accurate, based on empirical studies (e.g., Ref. [24]). However, its time complexity is, at worst, quadratic in the number of leaves [4,17], which could lead to a significant increase in runtime for large data. Therefore, pessimistic-error pruning is implemented in SURPASS.

## 4. An illustrative example

An example is given in this section to illustrate how the SURPASS algorithm works. The data set, given in Table 1, contains 12 records and three numeric attributes, used to build a decision tree for classifying two classes. In describing the computational procedure below, we will adopt notations given in Section 3, including those in Eqs. (1)–(3) and the SURPASS algorithm in Fig. 3. To explain the scalability issue, we assume that the memory of the computer here cannot be used to hold more than one record.

Table 1 An illustrative example

<table><tr><td>No.</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td>Class</td></tr><tr><td>1</td><td>69</td><td>50</td><td>7.0</td><td>A</td></tr><tr><td>2</td><td>83</td><td>50</td><td>6.0</td><td>A</td></tr><tr><td>3</td><td>94</td><td>45</td><td>5.5</td><td>A</td></tr><tr><td>4</td><td>77</td><td>47</td><td>5.3</td><td>A</td></tr><tr><td>5</td><td>44</td><td>52</td><td>4.5</td><td>A</td></tr><tr><td>6</td><td>48</td><td>55</td><td>4.8</td><td>A</td></tr><tr><td>7</td><td>40</td><td>53</td><td>4.5</td><td>A</td></tr><tr><td>8</td><td>70</td><td>48</td><td>4.6</td><td>B</td></tr><tr><td>9</td><td>56</td><td>50</td><td>4.5</td><td>B</td></tr><tr><td>10</td><td>45</td><td>51</td><td>5.3</td><td>B</td></tr><tr><td>11</td><td>42</td><td>50</td><td>5.0</td><td>B</td></tr><tr><td>12</td><td>48</td><td>51</td><td>5.2</td><td>B</td></tr></table>

Initially, all values in the v vectors and w matrices, where the sufficient statistics are stored, are set to zero. We first read in record 1, which belongs to class A. Hence, statistics in $\mathbf { v } _ { 1 }$ and $\mathbf { w } _ { 1 }$ are updated as follows:

$$
\mathbf {v} _ {1} = [ 6 9 5 0 7 ],
$$

and

$$
\mathbf {w} _ {1} = \left[ \begin{array}{c c c} 4 7 6 1 & 3 4 5 0 & 4 8 3 \\ 3 4 5 0 & 2 5 0 0 & 3 5 0 \\ 4 8 3 & 3 5 0 & 4 9 \end{array} \right],
$$

where the (1,1) entry in $\mathbf { w } _ { 1 }$ is calculated as 69 69=4761; the (1,2) entry is obtained by $6 9 \times 5 0 { = } 3 4 5 0 ;$ and the other entry values are computed accordingly. Now, delete record 1 and read in record 2. It is still class A, and its individual and cross-product values are

½  83 50 6 ; and

$$
\left[ \begin{array}{c c c} 6 8 8 9 & 4 1 5 0 & 4 9 8 \\ 4 1 5 0 & 2 5 0 0 & 3 0 0 \\ 4 9 8 & 3 0 0 & 3 6 \end{array} \right].
$$

Add these values to $\mathbf { v } _ { 1 }$ and $\mathbf { w } _ { 1 } ,$ , respectively, we have the updated $\mathbf { v } _ { 1 }$ and $\mathbf { w } _ { 1 }$ below:

$$
\mathbf {v} _ {1} = \left[ \begin{array}{l l l} 1 5 2 & 1 0 0 & 1 3 \end{array} \right],
$$

and

$$
\mathbf {w} _ {1} = \left[ \begin{array}{c c c} 1 1 6 5 0 & 7 6 0 0 & 9 8 1 \\ 7 6 0 0 & 5 0 0 0 & 6 5 0 \\ 9 8 1 & 6 5 0 & 8 5 \end{array} \right].
$$

The remaining records can be processed similarly. Starting from record 8, there will be values added to $\mathbf { v } _ { 2 }$ and $\mathbf { w } _ { 2 }$ . After all records are processed, we have:

$$
\mathbf {v} _ {1} = \left[ \begin{array}{l l l} 4 5 5 & 3 5 2 & 3 7. 6 \end{array} \right], \mathbf {w} _ {1} = \left[ \begin{array}{l l l} 3 2 2 5 5 & 2 2 4 9 7 & 2 5 1 5 \\ 2 2 4 9 7 & 1 7 7 7 2 & 1 8 8 3 \\ 2 5 1 5 & 1 8 8 3 & 2 0 7 \end{array} \right],
$$

and

$$
\begin{array}{r l} \mathbf {v} _ {2} & = [ 2 6 1 2 5 0 2 4. 6 ], \mathbf {w} _ {2} \\ & = \left[ \begin{array}{c c c} 1 4 1 2 9 & 1 3 0 0 3 & 1 2 7 2 \\ 1 3 0 0 3 & 1 2 5 0 6 & 1 2 3 1 \\ 1 2 7 2 & 1 2 3 1 & 1 2 2 \end{array} \right], \end{array}
$$

where numbers in the matrices are rounded to integers.

Next, we compute the sample mean vectors and covariance matrices as follows [covariance entries are computed by Eq. (6); note that $n _ { 1 } { = } 7$ and $n _ { 2 } { = } 5 ]$ :

$$
\begin{array}{l} \bar {\mathbf {x}} _ {1} = [ 6 5 5 0. 2 9 5. 3 7 ], \\ \mathbf {S} _ {1} = \left[ \begin{array}{c c c} 4 4 6. 6 7 & - 6 3. 8 3 & 1 1. 7 5 \\ - 6 3. 8 3 & 1 1. 9 0 & - 1. 2 7 \\ 1 1. 7 5 & - 1. 2 7 & 0. 8 2 \end{array} \right], \end{array}
$$

and

$$
\begin{array}{l} \bar {\mathbf {x}} _ {2} = [ 5 2. 2 5 0 4. 9 2 ], \\ \mathbf {S} _ {2} = \left[ \begin{array}{c c c} 1 2 6. 2 0 & - 1 1. 7 5 & - 3. 0 1 \\ - 1 1. 7 5 & 1. 5 0 & 0. 3 2 \\ - 3. 0 1 & 0. 3 2 & 0. 1 3 \end{array} \right]. \end{array}
$$

And the pooled sample covariance matrix, by Eq. (2), and its inverse are

$$
\mathbf {S} = \left[ \begin{array}{c c c} 3 1 8. 4 8 & - 4 3. 0 0 & 5. 8 5 \\ - 4 3. 0 0 & 7. 7 4 & - 0. 6 3 \\ 5. 8 5 & - 0. 6 3 & 0. 5 4 \end{array} \right],
$$

$$
\mathbf {S} ^ {- 1} = \left[ \begin{array}{c c c} 0. 0 1 4 6 & 0. 0 7 5 2 & - 0. 0 6 9 1 \\ 0. 0 7 5 2 & 0. 5 3 1 4 & - 0. 1 8 9 7 \\ - 0. 0 6 9 1 & - 0. 1 8 9 7 & 2. 3 6 7 4 \end{array} \right].
$$

Substituting these values into Eq. (1) and the righthand side of Eq. (3), we have the candidate splitting rule based on linear discriminant function using all attributes, which assign a record to the left node (subset) if

$$
0. 1 7 6 8 X _ {1} + 1. 0 2 9 1 X _ {2} + 0. 1 3 0 2 X _ {3} > 6 2. 6 3 1 2,
$$

and to the right node (subset) otherwise.

![](/api/attachments/MQKA5SFN/fulltext/images/f712f576be03af312be2a42007a6213dd36faec9865e0b69944f83fbb045f583.jpg)  
Fig. 4. Decision tree based on the example data.

To compute splitting rule using a single attribute X<sub>j</sub>, Eq. (3) reduces to

$$
\begin{array}{l} \big (\bar {x} _ {1 j} - \bar {x} _ {2 j} \big) s _ {j j} ^ {- 1} X _ {j} > \frac {1}{2} \big (\bar {x} _ {1 j} - \bar {x} _ {2 j} \big) s _ {j j} ^ {- 1} \big (\bar {x} _ {1 j} + \bar {x} _ {2 j} \big) \\ \qquad + \log (n _ {2} / n _ {1}). \end{array}
$$

All quantities in this expression are scalars and are readily available from $\bar { \mathbf { X } } _ { 1 } , \bar { \mathbf { X } } _ { 2 } .$ , and S that have already been computed. In particular, $s _ { j j }$ is the $j \mathrm { t h }$ diagonal element in S (which is the pooled variance of $X _ { j } )$ , and the inverse is merely the reciprocal. Substituting respective values into this expression, we have three more candidate splits based on individual attributes, as below:

$$
X _ {1} > 5 0. 2 2 8 1, X _ {2} > 4 1. 0 2 4 3, \text { and } X _ {3} > 4. 7 4 1 6.
$$

To determine which of the four splits is the best, we compute the entropy value associated with each candidate split and select the one with the minimum value. This step is similar to that in the other sortand-search algorithms (except that they generally have much more candidate splits to evaluate), and thus, will not be discussed here (see Ref. [32] for detail). The entropy values for the four candidate splits are 0.5035, 0.8755, 0.9793, and 0.9591, respectively. Therefore, the first split that uses linear combination of all attributes is selected. This split divides the full set into two subsets, with records 1, 2, 3, 4, and 6 in one set and the remaining records in the other set. If the process stops here, this split will misclassify two records, while the other three splits will have four, five, and five misclassified records, respectively. These misclassification results also suggest selecting the linear combination split at this root node.

The same procedure is then applied to each of the two subsets recursively. In this case, however, the algorithm stops the further partitioning of the first subset because all records in that set are of class A. The final tree, which consists of three leaves, is given in Fig. 4, where the error rate at each leaf is shown in the parentheses next to the class label (e.g., zero out of five records is misclassified at the first leaf). Note that the best split for the second subset is a univariate split, which produces a perfect outcome.

## 5. Experimental evaluation with pattern recognition and intrusion detection data

The first data set for the pattern recognition problem is the forest cover set, taken from U. C. Irvine’s data repository [3]. This data set, initially used in Ref. [2], consists of 581,012 records of forest cover data. The data set has 54 attributes, including 10 numeric ones representing quantitative measurements of a forest cover example and 44 binary attributes describing various geographic and geologic conditions. Examples of these attributes are the elevation of the location, hill slope, soil type (binary coded), etc. There are seven classes representing different forest cover types. The data mining problem is to build decision tree models to predict the forest cover type of a new record based on its values on the 54 attributes.

Results for forest cover data

<table><tr><td rowspan="2">Sampling proportion</td><td colspan="3">Error rate</td><td colspan="2">Number of leaves</td><td colspan="3">Total CPU time (s)</td></tr><tr><td>SURPASS</td><td>RainForest</td><td>LDA</td><td>SURPASS</td><td>RainForest</td><td>SURPASS</td><td>RainForest</td><td>LDA</td></tr><tr><td>0.1</td><td>0.2080</td><td>0.1996</td><td>0.3820</td><td>2113</td><td>2330</td><td>826</td><td>974</td><td>14</td></tr><tr><td>0.2</td><td>0.1615</td><td>0.1570</td><td>0.3939</td><td>3767</td><td>3914</td><td>1720</td><td>2328</td><td>27</td></tr><tr><td>0.3</td><td>0.1401</td><td>0.1332</td><td>0.3976</td><td>5446</td><td>5421</td><td>2710</td><td>3769</td><td>42</td></tr><tr><td>0.4</td><td>0.1272</td><td>0.1133</td><td>0.4017</td><td>6747</td><td>6447</td><td>3627</td><td>5066</td><td>54</td></tr><tr><td>0.5</td><td>0.1115</td><td>0.1053</td><td>0.3926</td><td>7954</td><td>7515</td><td>4651</td><td>6384</td><td>68</td></tr><tr><td>0.6</td><td>0.1061</td><td>0.0947</td><td>0.3947</td><td>9024</td><td>8483</td><td>5644</td><td>7611</td><td>81</td></tr><tr><td>0.7</td><td>0.0952</td><td>0.0879</td><td>0.3949</td><td>10061</td><td>9205</td><td>6498</td><td>8503</td><td>94</td></tr><tr><td>0.8</td><td>0.0883</td><td>0.0838</td><td>0.3912</td><td>10996</td><td>10123</td><td>7464</td><td>10634</td><td>107</td></tr><tr><td>0.9</td><td>0.0857</td><td>0.0793</td><td>0.3959</td><td>11878</td><td>10630</td><td>8293</td><td>10625</td><td>119</td></tr><tr><td>1.0</td><td>0.0814</td><td>0.0751</td><td>0.3959</td><td>13021</td><td>11517</td><td>9426</td><td>11876</td><td>133</td></tr></table>

Table 3  
Results for waveform data

<table><tr><td rowspan="2">Sampling proportion</td><td colspan="3">Error rate</td><td colspan="2">Number of leaves</td><td colspan="3">Total CPU time (s)</td></tr><tr><td>SURPASS</td><td>RainForest</td><td>LDA</td><td>SURPASS</td><td>RainForest</td><td>SURPASS</td><td>RainForest</td><td>LDA</td></tr><tr><td>0.1</td><td>0.1449</td><td>0.2176</td><td>0.1420</td><td>22</td><td>191</td><td>125</td><td>276</td><td>3</td></tr><tr><td>0.2</td><td>0.1403</td><td>0.1961</td><td>0.1339</td><td>48</td><td>332</td><td>267</td><td>606</td><td>5</td></tr><tr><td>0.3</td><td>0.1382</td><td>0.1946</td><td>0.1389</td><td>67</td><td>505</td><td>427</td><td>946</td><td>8</td></tr><tr><td>0.4</td><td>0.1402</td><td>0.1913</td><td>0.1410</td><td>96</td><td>622</td><td>584</td><td>1296</td><td>10</td></tr><tr><td>0.5</td><td>0.1386</td><td>0.1909</td><td>0.1392</td><td>60</td><td>640</td><td>760</td><td>1649</td><td>13</td></tr><tr><td>0.6</td><td>0.1340</td><td>0.1857</td><td>0.1352</td><td>79</td><td>745</td><td>926</td><td>2042</td><td>15</td></tr><tr><td>0.7</td><td>0.1373</td><td>0.1900</td><td>0.1361</td><td>112</td><td>857</td><td>1107</td><td>2412</td><td>18</td></tr><tr><td>0.8</td><td>0.1369</td><td>0.1855</td><td>0.1361</td><td>102</td><td>905</td><td>1282</td><td>2782</td><td>20</td></tr><tr><td>0.9</td><td>0.1359</td><td>0.1826</td><td>0.1352</td><td>95</td><td>1124</td><td>1455</td><td>3159</td><td>23</td></tr><tr><td>1.0</td><td>0.1374</td><td>0.1846</td><td>0.1380</td><td>136</td><td>1176</td><td>1630</td><td>3560</td><td>25</td></tr></table>

Because the attributes in the forest cover set are largely binary, we investigate another pattern recognition data set, where all attributes are numeric. This simulated data set was generated based on the model described in the CART book [4]. It has been extensively used in decision-tree-related experimental studies. However, we have not seen any study that used it for a large-scale experiment. The problem is to use 21 numeric measurements to predict three waveform types (classes). Because the data set is generated by a computer program, the user has the option to specify the number of records in the data set. We chose to generate a total of 250,000 records.

The intrusion detection data is taken from Refs. [15,16]. The data set contains 311,029 network connection records, each having 41 numeric and binary attributes, representing various measurements, parameters, and status values of a connection. Examples of these attributes include the duration of the connection, number of bytes transferred, number of failed logins, percentage of connections that have a certain type of error, etc. There are 18 classes representing 1 normal connection and 17 different intrusion attacks. The task is to identify the normal connection and each individual attack based on the values of the 41 attributes.

Table 4  
Results for intrusion detection data

<table><tr><td rowspan="2">Sampling proportion</td><td colspan="3">Error rate</td><td colspan="2">Number of leaves</td><td colspan="3">Total CPU time (s)</td></tr><tr><td>SURPASS</td><td>RainForest</td><td>LDA</td><td>SURPASS</td><td>RainForest</td><td>SURPASS</td><td>RainForest</td><td>LDA</td></tr><tr><td>0.1</td><td>0.0268</td><td>0.0293</td><td>0.1377</td><td>171</td><td>195</td><td>167</td><td>203</td><td>7</td></tr><tr><td>0.2</td><td>0.0243</td><td>0.0264</td><td>0.1409</td><td>248</td><td>337</td><td>298</td><td>510</td><td>11</td></tr><tr><td>0.3</td><td>0.0243</td><td>0.0248</td><td>0.1369</td><td>333</td><td>481</td><td>461</td><td>922</td><td>15</td></tr><tr><td>0.4</td><td>0.0243</td><td>0.0253</td><td>0.1364</td><td>407</td><td>590</td><td>747</td><td>1332</td><td>21</td></tr><tr><td>0.5</td><td>0.0241</td><td>0.0249</td><td>0.1399</td><td>497</td><td>722</td><td>898</td><td>1756</td><td>28</td></tr><tr><td>0.6</td><td>0.0239</td><td>0.0238</td><td>0.1402</td><td>602</td><td>892</td><td>1096</td><td>2907</td><td>32</td></tr><tr><td>0.7</td><td>0.0229</td><td>0.0243</td><td>0.1361</td><td>674</td><td>1024</td><td>1283</td><td>3171</td><td>37</td></tr><tr><td>0.8</td><td>0.0234</td><td>0.0232</td><td>0.1387</td><td>738</td><td>1147</td><td>1282</td><td>4117</td><td>41</td></tr><tr><td>0.9</td><td>0.0229</td><td>0.0237</td><td>0.1379</td><td>835</td><td>1235</td><td>1986</td><td>4638</td><td>47</td></tr><tr><td>1.0</td><td>0.0229</td><td>0.0232</td><td>0.1372</td><td>850</td><td>1332</td><td>2001</td><td>5076</td><td>56</td></tr></table>

The performance of the proposed SURPASS algorithm is evaluated based on three criteria: (1) classification accuracy (or error rate), which is the percentage of correctly (or incorrectly) classified records in the test data; (2) tree size, which is the number of leaves in the final tree; and (3) computing time. We were unable to run a publicly available decision tree system, such as C4.5, on these data sets because the required memory sizes exceed the limit. None of the scalable decision tree algorithms described in Section 2 has the source programs available for the public. To make comparisons more meaningful, we chose to write a program based on RainForest algorithm because it is the newest and its authors claimed that the algorithm <sup>b</sup>outperform(s) SPRINT by about a factor of five<sup>Q</sup> [10]. Note that RainForest, as well as SLIQ and SPRINT, focus on the scalability issue, not the accuracy aspect of decision trees. They simply adopt the sort-and-search method, as in CART and C4.5, in growing decision trees. We also use linear discriminant analysis (LDA), which is naturally scalable, in this study.

To evaluate the scalability of the SURPASS algorithm, 10 samples were randomly selected from each complete set. The first sample contains 10% of the data, the second sample contains 20%, and so on; and the last sample is the entire data set. Within each sample, we randomly assigned 60% of the data for training, and the remaining 40% for testing. The experimental results on error rate, tree size, and computing time are reported in Tables 2–4 for the three data sets, respectively (there is no <sup>b</sup>tree size<sup>Q</sup> for

Table 5  
Results of SURPASS with and without pruning

<table><tr><td rowspan="2">Data set</td><td colspan="2">Error rate</td><td colspan="2">Number of leaves</td></tr><tr><td>Unpruned</td><td>Pruned</td><td>Unpruned</td><td>Pruned</td></tr><tr><td>Forest cover</td><td>0.0821</td><td>0.0814</td><td>15298</td><td>13021</td></tr><tr><td>Waveform</td><td>0.1735</td><td>0.1374</td><td>6769</td><td>136</td></tr><tr><td>Intrusion detection</td><td>0.0238</td><td>0.0229</td><td>1402</td><td>850</td></tr></table>

LDA because it is not a decision tree algorithm). To examine more closely the relationship between these measures and data size, we also plot these measures against sample size in Figs. 5–13. Because the pessimistic-error pruning is directly implemented in SURPASS, the reader might be interested in the performance of SURPASS without pruning. Table 5 shows the results of classification accuracy and tree size using SURPASS with and without pruning for the three full data sets.

It is evidenced from Figs. 5–7 that, in general, error rates decrease as sample sizes increase, although the situation is more notable in the forest cover case than in the other two cases. LDA’s error curves, however, are essentially flat in all three cases, which could be an indication that LDA is not a good choice for large data sets. In terms of classification accuracy, LDA is clearly the worst in the forest cover and intrusion detection cases, while RainForest falls to the last in the waveform case. SURPASS is among the best in all three cases. To determine whether the differences in the error rates are statistically significant, we applied a two-way analysis of variance (ANOVA; [26]; with family a=0.1) for each of the three cases, using the 10 samples (including the original set) as the blocks. The results of the Tukey multiple comparison tests indicate that the differences in error rates between SURPASS and RainForest in the forest cover and intrusion detection cases are statistically insignificant, while LDA is indeed the worst statistically. In the waveform case, the difference between SURPASS and LDA is statistically insignificant, while RainForest’s error rate is statistically significantly higher.

![](/api/attachments/MQKA5SFN/fulltext/images/54332b56d7de135cda4713ee38ee7f8bc46974a07509a3f2b3b2bde3c676e104.jpg)  
Fig. 5. Classification error rate on forest cover data.

![](/api/attachments/MQKA5SFN/fulltext/images/8b3f2e78a238ff5baed0e14607eabe19d59b64d289b34fb51755b1264db32fd4.jpg)  
Fig. 6. Classification error rate on waveform data.

It is interesting to compare the results of SURPASS and RainForest with the forest cover and waveform data. For the forest cover case, both the error rates and the tree sizes generated by SURPASS are very close to those by RainForest (see Table 2). A further investigation of the trees generated by SURPASS indicates that almost all of the splits in this case are univariate (which can be indirectly verified by the large tree sizes generated by SURPASS). Note that the majority of the attributes in this data set are binary, in which case univariate splits should be favorable, because the covariance matrix involving too many binary attributes tends to be degenerated, causing linear combination split less effective. Another explanation is that the true boundaries between classes in this case are mostly axis-parallel, which also suggests univariate splits. The waveform data, on the other hand, are generated by some complex multivariate functions [4]. In this case, the decision trees produced by SURPASS have significantly lower error rates and smaller tree sizes than those by RainForest (see Table 3). Examining the trees produced by SURPASS, we found that all of the splits are multivariate. Rain-Forest, which can make univariate splits only, is unable to capture the multivariate nature of these data. In general, SURPASS should be the strongest when the true boundaries between classes are oblique, i.e., multivariate [in particular, multivariate normal, because it is an assumption underlying Eq. (3)]. However, given that SURPASS is flexible in choosing either a univariate or a multivariate split, it can adapt well to both axis-parallel and oblique patterns.

![](/api/attachments/MQKA5SFN/fulltext/images/79005ba7fe829bb97da4efdd8004077c7d36ce7d111e278399f8667ee96f163f.jpg)  
Fig. 7. Classification error rate on intrusion detection data.

![](/api/attachments/MQKA5SFN/fulltext/images/d9b481e7918ed3d46a02f76a954c4d63145068501c4286bb609de1fa9f30f999.jpg)  
Fig. 8. Tree size on forest cover data.

It can be observed from Figs. 8–10 that tree size increases with sample size, and RainForest, in general, produces larger trees than SURPASS does. For the waveform case, however, increasing the sample and tree sizes does not appear to help improve classification accuracy. LDA performs extremely well without recursive partitioning at all. Similarly, changes in sample and tree sizes do not cause significant changes in classification accuracy in the intrusion detection case (see Table 4), but this time, the two decision tree methods are clearly better than LDA. In addition, the effect of pruning associated with SURPASS appears to vary with different data, as suggested in the results shown in Table 5.

We now turn to computing time performance and scalability issue. It is very clear from Tables 2–4 that LDA is much faster than the two decision tree algorithms are (because LDA does not involve recursive partitioning). In fact, the runtime values for LDA are so small that they are considered negligible when compared with those of the two decision-tree algorithms. Therefore, LDA’s runtime is not plotted. SURPASS runs faster than RainForest does in all three cases. More importantly, it is clearly demonstrated in

![](/api/attachments/MQKA5SFN/fulltext/images/397c838eeff32bc152bcd1b8c2991ccaa7f5ec9188591ec267a9217fd8473fb5.jpg)  
Fig. 9. Tree size on waveform data.

![](/api/attachments/MQKA5SFN/fulltext/images/5483ca40f687a3760368138568b010ed9032d27175274fdbd11f7663dff6e874.jpg)  
Fig. 10. Tree size on intrusion detection data.

Figs. 11 and 12 that a near-perfect linear relationship exists between the SURPASS’ runtime and the number of records. For the intrusion detection case in Fig. 13, although there are a few fluctuations, the general trend for the relationship is still linear. These results strongly indicate that SURPASS scales up very well on data size. RainForest’s runtime behavior, however, is not that clear. Its runtime curve in the intrusion detection case appears to have a slightly nonlinear upward trend.

## 6. Conclusions and extensions

A new scalable decision tree algorithm based on an efficient gathering of sufficient statistics has been presented. The algorithm effectively solves the problem of mining large numeric data for classification when the data size is beyond the capacity of the main memory. The algorithm is flexible in choosing univariate or multivariate splits and, therefore, is quite adaptive to different patterns. The results of our experimental study, using pattern recognition and intrusion detection data, indicate that the proposed algorithm produces decision trees with very high quality in terms of classification accuracy, and the algorithm appears to scale up well against large data sets, with computing time approximately linear in the number of records in the data.

Although we have considered only pattern recognition and intrusion detection problems in this study, many other application problems, such as fraud detection in credit card and telephone call transactions, accounting and financial data analysis, and geographic information systems applications, share similar data characteristics and properties described here. That is, data in those application domains are very large in volume, are mostly numeric types, and do not satisfy assumptions underlying traditional statistical methods. We plan to apply the SURPASS system to these problems to further explore the potentials of the approach.

![](/api/attachments/MQKA5SFN/fulltext/images/7e7c4c6b89f70a8f476a6d1d1e8662fce4eabd43a21ecd676717d4bfb2b6f7a7.jpg)  
Fig. 11. Total CPU time on forest cover data.

![](/api/attachments/MQKA5SFN/fulltext/images/5460a9415852db2afb8d8f2cc9038f7083d7e6dc1cc1d89244270d254f2f5f44.jpg)  
Fig. 12. Total CPU time on waveform data.

The SURPASS algorithm introduced in this article is specialized in dealing with numeric data. When categorical data are presented, categorical values need to be processed with binary (0–1) coding. This is easy for binary categorical attributes such as those in this study. When there are many categorical attributes, each having a large number of categories (e.g., zip code), the coding process involves creating a large number of additional binary attributes, which could cause computational problems. A more natural approach to deal with mixed data type is to handle numeric and categorical data using different sufficient statistics. For numeric data, the summation statistics, such as the ones employed in this study, are computed. For categorical data, we can use the frequency count statistics, like those used in many existing algorithms. The quality of a split can be evaluated using the same impurity measure such as entropy, no matter whether the split is based on numeric or categorical attributes.

![](/api/attachments/MQKA5SFN/fulltext/images/26d0df08d78377d2ceb0b640f629ac63b15364d1b68cea9b48e409176884cedc.jpg)  
Fig. 13. Total CPU time on intrusion detection data.

Because of continued access of disk-resident data, the computing time with SURPASS is expected to be longer than those of in-memory decision tree systems such as C4.5 or CART. There are some alternatives to speed up SURPASS. In the early stage of tree growth, we can choose to evaluate only the split based on the linear combination of all attributes, without considering splits using individual attributes. When the partitioned data size drops below a certain level, where the quality of splits based on such linear combination may deteriorate, the algorithm can resume the procedure involving each individual attribute. Another approach to speed up computing time is to use datareduction techniques [19], which work on samples instead of complete set of data. The effectiveness of the data reduction approach requires more extensive and in-depth studies, especially in terms of classification accuracy. For the three data sets investigated in this study, the data reduction approach is more likely to work well for the waveform and intrusion detection sets, where the characteristics of the data can be captured in relatively small samples. But the approach would probably be less effective for the forest cover data, where classification accuracy increases significantly as sample size grows.

## References

[1] J.P. Anderson, Computer Security Threat Monitoring and Surveillance, Technical Report, James P. Anderson Co., Fort Washington, PA, April 1980.

[2] J.A. Blackard, J.D. Denis, Comparative accuracies of artificial neural networks and discriminant analysis in predicting forest cover types from cartographic variables, Computers and Electronics in Agriculture 24 (3) (2000) 131– 151.

[3] C. Blake, E. Keogh, C.J. Merz, UCI Repository of Machine Learning Databases, [http://www.ics.uci.edu/\~mlearn/ MLRepository.html]. University of California, Irvine, Dept. of Information and Computer Science, 1998.

[4] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, Wadsworth, Belmont, CA, 1984.

[5] L. Breiman, Bagging predictors, Machine Learning 24 (1996) 123– 140.

[6] C.E. Brodley, P.E. Utgoff, Multivariate decision trees, Machine Learning 19 (1995) 45–77.

[7] D.E. Denning, An intrusion-detection model, IEEE Transactions on Software Engineering 13 (2) (1987) 222 – 232.

[8] Y. Freund, R.E. Schapire, A decision-theoretic generalization of online learning and an application to boosting, Journal of Computer and System Sciences 55 (1) (1997) 119– 139.

[9] J. Gama, P. Brazdil, Linear tree, Intelligent Data Analysis 3 (1) (1999) 1 – 22.

[10] J. Gehrke, R. Ramakrishnan, V. Ganti, RainForest—a framework for fast decision tree construction of large datasets, Proceedings of 24th International Conference on Very Large Data Bases, New York, NY, 1998.

[11] G. Graefe, U. Fayyad, S. Chaudhuri, On the efficient gathering of sufficient statistics for classification from large SQL databases, Proceedings of 4th International Conference on Knowledge Discovery and Data Mining, New York, NY, 1998.

[12] G.H. John, Enhancements to the Data Mining Process, Doctoral Dissertation, Stanford University, Dept. of Computer Science, Stanford, CA, 1997.

[13] G.V. Kass, An exploratory technique for investigating large quantities of categorical data, Applied Statistics 29 (1980) 119 – 127.

[14] J. Kittler, Feature selection and extraction, in: Young, Fu (Eds.), Handbook of Pattern Recognition and Image Processing, Academic Press, New York, 1986.

[15] W. Lee, S.J. Stolfo, A framework for constructing features and models for intrusion detection systems, ACM Transactions on Information and System Security 3 (4) (2000) 227 – 261.

[16] W. Lee, S.J. Stolfo, K.W. Mok, Mining in a data-flow environment: experience in network intrusion detection, Proceedings of 5th International Conference on Knowledge Discovery and Data Mining, San Diego, CA, 1999.

[17] X.-B. Li, J. Sweigart, J. Teng, J. Donohue, L. Thombs, A dynamic programming based pruning method for decision trees, INFORMS Journal on Computing 13 (4) (2001) 332– 344.

[18] X.-B. Li, J. Sweigart, J. Teng, J. Donohue, L. Thombs, M. Wang, Multivariate decision trees using linear discriminants and tabu search, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 33 (2) (2003) 194 – 205.

[19] H. Liu, H. Motoda (Eds.), Instance Selection and Construction for Data Mining, Kluwer Academic, New York, 2001.

[20] W.-Y. Loh, Y.-S. Shih, Split selection methods for classification trees, Statistica Sinica 7 (1997) 815 – 840.

[21] T.F. Lunt, A survey of intrusion detection techniques, Computers and Security 12 (4) (1993) 405 – 418.

[22] O.L. Mangasarian, Mathematical programming in data mining, Data Mining and Knowledge Discovery 1 (2) (1997) 183 – 201.

[23] M. Mehta, R. Agrawal, J. Rissanen, SLIQ: a fast scalable classifier for data mining, Proceedings of 5th International Conference on Extending Database Technology, Avignon, France, 1996.

[24] J. Mingers, An empirical comparison of pruning methods for decision tree induction, Machine Learning 4 (1989) 227– 243.

[25] S.K. Murthy, S. Kasif, S. Salzberg, A system for induction of oblique decision trees, Journal of Artificial Intelligence Research 2 (1994) 1 – 32.

[26] J. Neter, W. Wasserman, M.H. Kutner, Applied Linear Statistical Models, Irwin, Homehood, IL, 1990.

[27] S.K. Pal, A. Pal (Eds.), Pattern Recognition: From Classical to Modern Approaches, World Scientific, Singapore, 2001.

[28] S. Piramuthu, On learning to predict web traffic, Decision Support Systems 35 (2) (2003) 213– 229.

[29] F. Provost, V. Kolluri, A survey of methods for scaling up inductive algorithms, Data Mining and Knowledge Discovery 3 (2) (1999) 131 – 169.

[30] J.R. Quinlan, Introduction of decision trees, Machine Learning 1 (1986) 81 – 106.

[31] J.R. Quinlan, Simplifying decision trees, International Journal of Man-Machine Studies 27 (1987) 221– 234.

[32] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[33] P.E. Ross, Flash of genius, Forbes 162 (11) (1998 November 16) 98 – 104.

[34] J. Shafer, R. Agrawal, M. Mehta, SPRINT: a scaleable parallel classifier for data mining, Proceedings of 22nd International Conference on Very Large Data Bases, Bombay, India, 1996.

[35] O.R.L. Sheng, C.-P. Wei, P.J.-H. Hu, N. Chang, Automated learning of patient image retrieval knowledge: neural networks versus inductive decision trees, Decision Support Systems 30 (2) 105–124.

[36] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations, Morgan Kaufmann, San Francisco, CA, 2000.

[37] D. Zhu, G. Premkumar, X. Zhang, C.-H. Chu, Data mining for network intrusion detection: a comparison of alternative methods, Decision Sciences 32 (4) (2001) 635 – 660.

![](/api/attachments/MQKA5SFN/fulltext/images/ae3949ed138384fbce474aabd034f243468b76a75564b8dd605617ee95e49a7e.jpg)

Xiao-Bai Li is an Assistant Professor in the College of Management at University of Massachusetts Lowell. He received the PhD degree in management science from the University of South Carolina in 1999, the MBA degree from the University of New Hampshire in 1994, and the BS degree in civil engineering from Chongqing University, China, in 1984. His research interests include decision trees, data mining, databases, and decision support systems. He has

published in IEEE Transactions on Systems, Man, and Cybernetics, European Journal of Operational Research, INFORMS Journal on Computing, among others.
