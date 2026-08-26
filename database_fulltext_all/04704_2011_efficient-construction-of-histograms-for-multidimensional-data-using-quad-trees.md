---
otero_id: 4704
otero_key: "KAZV746U"
title: "Efficient construction of histograms for multidimensional data using quad-trees"
authors: "Yohan J. Roh; Jae Ho Kim; Jin Hyun Son; Myoung Ho Kim"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.05.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>cient construction of histograms for multidimensional data using quad-trees

Yohan J. Roh <sup>a,</sup>⁎, Jae Ho Kim <sup>b</sup>, Jin Hyun Son <sup>c</sup>, Myoung Ho Kim

<sup>a</sup> Data Analytics Group, Samsung Advanced Institute of Technology, Samsung Electronics Nongseo-dong, Yongin Si Giheung-gu, Gyeonggi-Do 446-712, South Korea

<sup>b</sup> Department of Computer Science KAIST 373-1 Guseong-dong, Yuseong-gu, Taejon 305–701, South Korea

<sup>c</sup> Department of Computer Science and Engineering Hanyang University 1271 Sa-1 dong, Ansan, Kyunggi-do 425-791, South Korea

## a r t i c l e i n f o

Article history: Received 29 January 2010 Received in revised form 2 May 2011 Accepted 15 May 2011 Available online 19 May 2011

Keywords: Data management Query optimization Selectivity estimation Multidimensional histograms

## a b s t r a c t

Histograms can be useful in estimating the selectivity of queries in areas such as database query optimization and data exploration. In this paper, we propose a new histogram method for multidimensional data, called the Q-Histogram, based on the use of the quad-tree, which is a popular index structure for multidimensional data sets. The use of the compact representation of the target data obtainable from the quad-tree allows a fast construction of a histogram with the minimum number of scanning, i.e., only one scanning, of the underlying data. In addition to the advantage of computation time, the proposed method also provides a better performance than other existing methods with respect to the quality of selectivity estimation. We present a new measure of data skew for a histogram bucket, called the weighted bucket skew. Then, we provide an effective technique for skew-tolerant organization of histograms. Finally, we compare the accuracy and ef<sup>fi</sup>ciency of the proposed method with other existing methods using both real-life data sets and synthetic data sets. The results of experiments show that the proposed method generally provides a better performance than other existing methods in terms of accuracy as well as computational ef<sup>fi</sup>ciency.

Crown Copyright © 2011 Published by Elsevier B.V. All rights reserved

## 1. Introduction

With increasing data volumes, the performance demands on database systems have grown and the need to produce accurate approximations of data distributions has also increased signi<sup>fi</sup>cantly. In particular, the estimation of the selectivity of a query, i.e., the number of data objects in the query region, can be used for database query optimization [18,19]. It also can be used for some types of query processing such as skyline query processing, spatio-temporal query processing, top-k query processing and so on [2,4–7,27,32–34].

Motivated by these applications, there has been much work on the problem of selectivity estimation: histograms [1,3,9–11,13– 16,20,25,29,30,35], wavelet transformation [24,36], discrete cosine transformation [23], and sampling [17]. Among these approaches, histograms have been shown to be one of the most popular and effective ways to obtain accurate estimates of selectivity for multidimensional queries [10].

A histogram consists of a set of buckets $b _ { i } , i { = } 1 , { \ldots } , n ,$ , where each bucket b has its data space s and the number of data objects f in s . All the data objects in the region of a bucket are assumed to be uniformly distributed (commonly called uniform distribution assumption). The number of buckets is usually a system parameter and is reasonably small so that all the buckets can be kept in memory. The process of constructing a histogram is typically performed periodically to re<sup>fl</sup>ect changes in the underlying data distribution.

Given a data range I speci<sup>fi</sup>ed by a query, an estimate of the selectivity for the query is computed as follows, under uniform distribution assumption: $\sum { _ { i = 1 \ldots n } } \lvert S _ { i } \wedge I \rvert / \lvert S _ { i } \rvert \cdot f _ { i } . \mathrm { H e r e } , \rvert$ | denotes the size of a data space and $\cdot _ { s _ { i } } \wedge I ^ { \prime }$ denotes the intersection of s and I. An estimate of the selectivity for one bucket is computed in proportion to the size of the overlapping region between the query region and the bucket region. The selectivity estimate for a query is the sum of all the estimated values for all the buckets.

When data objects are not uniformly distributed in buckets, the accuracy of histograms will decrease. Therefore, a histogram should be organized in such a way that data in each bucket is as uniformly distributed as possible.

Now let us consider index structures that are used widely in commercial database systems. As noted in [10,19], some of the existing index structures can be an interesting starting point for constructing histograms. The quad-tree and its variants have been popularly used as index structures for the fast access of multidimensional data sets. When a quad-tree has already been used as an index for some applications, we can improve the cost of histogram construction by using the data partition information implied in this quad-tree. That is, utilizing the existing quad-tree can provide an advantage of computing time for construction of buckets. Then, our problem can be stated simply as follows, when a given number of buckets is B: Partition a set of leaf nodes in a quad-tree into B groups such that the data objects in each group are as uniformly distributed as possible. Here, each group corresponds to one bucket. When there are K leaf nodes in the quad-tree, the number of ways of partitioning K leaf nodes into B groups, commonly known as Stirling number of the second kind S (K, B), can be quite large in practice. This problem is NP-Hard, and therefore, some heuristics need to be employed. The partitioning of the leaf nodes can proceed in either a bottom-up or top-down fashion. We will start with the root node of the quad-tree and proceed in a topdown fashion.

In this paper, we will propose a new multidimensional histogram method, called the Q-Histogram, which is based on the use of the existing quad-tree. The proposed Q-Histogram divides a given data set with various levels of granularity by using the information in the quad-tree with the minimum number of scanning, i.e., only one scanning, of the underlying data. Through extensive experiments, we show that Q-Histogram has better performance than other existing methods with respect to accuracy as well as computational ef<sup>fi</sup>ciency.

The rest of the paper is organized as follows. Section 2 describes related work. We present our proposed histogram method in Section 3. Section 4 provides the results of performance experiments with four real-life data sets as well as one synthetic data set. Finally in Section 5, we present conclusions and future work.

## 2. Related work

Histograms on multiple attributes can be used for processing and optimizing queries. For query optimization, histograms can be used to estimate the selectivity of queries and to generate the most ef<sup>fi</sup>cient query execution plans [18,19].

For skyline query processing, Chaudhuri et al. [6] and Papadias et al. [27] use histograms to accurately estimate the result sizes of skyline queries, which can be useful in providing immediate feedback to the user and implementing skyline computation as an operator in database systems.

For spatio-temporal query processing, the authors of [7] use a histogram technique and extend it with velocities to estimate the selectivity of spatio-temporal window queries, i.e., the number of objects that will appear in the query window at a given future time. For the same purpose, Tao et al. [33] propose a set of histogram-based solutions. Sun et al. [32] make use of histograms to accurately estimate the selectivity of spatio-temporal joins, i.e., for two given sets $S _ { 1 }$ and $S _ { 2 }$ of objects, the number of pairsbo , o Nof objects, such that $o _ { 1 } { \in } S _ { 1 } , o _ { 2 } { \in } S _ { 2 } ,$ and the distance between these two objects at a given future time is below a certain threshold.

For load-balancing of parallel hash joins, Poosala and Ioannidis [28] use the statistics of histograms to accurately estimate the cost required to perform the join operation, and effectively balance the load across nodes that participate in the parallel execution.

For top-k query processing, Bruno et al. [4] and Chaudhuri et al. [5] use histograms for translating a top-k request into a single range query that can be ef<sup>fi</sup>ciently processed by existing database engines. They have shown that using histograms can avoid the requirement of a full sequential scan of the database, and thus signi<sup>fi</sup>cantly reduce the time to perform top-k queries.

Over the past decades, many studies have been conducted to enhance the performance of multidimensional histograms. The underlying assumption in using a histogram is that the histogram performs well when data is uniformly distributed in every bucket. However, the problem of organizing buckets in such a way that the data is uniformly distributed in every bucket is NP-hard in two or more dimensions [26] and heuristics have been proposed.

The EquiDepth histogram method [25] partitions the target space, one dimension at a time. Here, in each i-th dimension, the target space is divided into v intervals, each of which has the same number of data. So, for a d-dimensional data set, a set of $\nu _ { 1 } \times \nu _ { 2 } \times \ldots \times \nu _ { d }$ buckets is constructed, where each bucket contains the same number of data. The EquiDepth histogram may be faster to construct among other types of histograms, while because of its rigid structure it may not be <sup>fl</sup>exible to cope with various cases of data skew.

The MinSkew histogram method [1] uses binary space partitioning, where a bucket is partitioned into two new buckets. This partitioning approach may construct histograms rapidly; however, MinSkew may not recognize regions where data are not uniformly distributed, which may decrease the accuracy of selectivity estimation. This is because the partitioning heuristics of MinSkew is based on data skew in only one-dimension at a time rather than considering the skew of multiple dimensions at once.

The GenHist histogram method [15,16] uses multidimensional grids of various sizes, where high-frequency grid cells are converted into buckets. More speci<sup>fi</sup>cally, GenHist iteratively constructs a certain number of buckets by using grids. Here, the grid sizes and the number of buckets constructed per iteration are determined by using the system parameter (i.e., the total number of buckets) and the userprovided parameter (i.e., initial grid size). Being different from the above approaches, this method directly approximates multidimensional (i.e., joint) data distributions. The authors of GenHist claim that the GenHist histogram behaves more accurately for data sets in highdimensional spaces than some previous approaches, such as random sampling, wavelet transformation [36], and MinSkew [1]. However, the performance of GenHist may vary depending on the input parameters. Furthermore, in practice, it is dif<sup>fi</sup>cult for users to provide the optimal or a near optimal value for the required parameter. Another drawback of this technique is that it requires multiple passes (at least 5 to 10) over the entire data set [3].

The RK-Hist histogram method, which has been recently proposed in [10], uses a variant of an R-tree index, called the Hilbert packed R-tree [21], where the entire data are sorted based on their own positions along the Hilbert curve. The sorted data are divided into several leaf nodes of the tree, in which the size of each leaf node is a disk block. Then, RK-Hist creates an initial set of buckets, each constructed by merging a <sup>fi</sup>xed number of leaf nodes. For each bucket, the skew of data is computed, and then some bucket with a high skew is split into two new buckets repeatedly, until the total number of buckets becomes the prede<sup>fi</sup>ned number or there is no improvement of the total skew of data in buckets. The authors of RK-Hist claim that the RK-Hist histogram works better than other existing methods, such as a traditional histogram technique [29], EquiDepth [25], and GenHist [15,16], in terms of estimation accuracy. However, the worst case time complexity of RK-Hist is O $( d \cdot N ^ { 2 } ) ,$ , where d is the dimension of the data space and N is the number of data objects. That is, the construction time of RK-Hist will be high, when the number of data becomes large. RK-Hist may introduce unnecessary buckets, when a <sup>fi</sup>xed number (say p) of leaf nodes are merged into an initial bucket. For example, consider a nonleaf node u with a very low skew that is an ancestor of a large number of leaf nodes. If the number of the descendant leaf nodes of u is much greater than p, several buckets will be constructed from these leaf nodes, but only one bucket consisting of a single node u suf<sup>fi</sup>ces to provide accurate selectivity estimation instead of several buckets. Note that, after the initial buckets are made, no merging is performed in subsequent steps.

There are several approaches for the layout of buckets. In the grid approach, buckets are arranged in rows and columns (e.g., as in the well-known equal-width histogram). In the recursively partitioning approach, a bucket is recursively partitioned into two new buckets along some dimension (e.g., as in MinSkew [1]). There are also other approaches that impose fewer restrictions than the above approaches on the arrangement of buckets, that is, allow a newly created bucket to cover a portion of data space in a more <sup>fl</sup>exible way. For example, in GenHist [15,16] and RK-Hist [10], the regions of buckets are allowed to overlap. The histogram method proposed in this paper also allows the regions of buckets to overlap.

Histograms are typically recomputed to re<sup>fl</sup>ect updates of the underlying data in a periodic manner. There is another interesting approach in maintaining histograms, called the self-tuning histogram [3,30]. This approach incrementally maintains buckets in response to feedback from the query execution engine about the actual result sizes of range queries. Since the actual result sizes re<sup>fl</sup>ect updates of the underlying data, the approach can gracefully adapt buckets to data updates. However, there are limitations that must be taken into account. First, feedback-based maintenance incurs additional overhead on query processing [3,30]. Second, because only the regions of queries that have been processed are used to reorganize histograms, data updates in the other regions may not be re<sup>fl</sup>ected. There is other research on the maintenance of histograms [11,35].

Note that, as alternatives to histograms on multiple attributes, different research groups have proposed other techniques for multidimensional selectivity estimation, such as wavelet transformation [24,36] and sampling [17]. The authors of [24,36] claim that wavelets works more accurately in two-dimension than a traditional histogram technique proposed in [29].

## 3. The proposed histogram method

We present in this section our new histogram method for multidimensional data called the Q-Histogram that utilizes the existing quadtree.

## 3.1. Basic notions and terminology

Fig. 1 shows an example of an eight node quad-tree and an organization of three histogram buckets (simply buckets from now on) built by using the nodes in this quad-tree. In Fig. 1a, each node of the tree is numbered based on the postorder traversal. The geographic representations of the data set for tree nodes are shown in Fig. 1b.

Fig. 1c shows the organization of three buckets constructed by using the tree nodes. The geographic representations of the data for these buckets are given in Fig. 1d.

In the proposed method, tree nodes are utilized as basic building blocks of buckets. Here, one bucket is de<sup>fi</sup>ned by a set of tree nodes, as shown in Fig. 1c and d. For example, Bucket1 consists of a single node (i.e., Node1). Bucket2 consists of two nodes (i.e., Node2 and Node4). Bucket3 consists of Node5 and Node6, which can be represented by a single node Node7. Note that the region of a bucket is the minimum bounding region that encompasses all the data in the corresponding nodes, as shown in Fig. 1d. The object frequency of the bucket is the total number of data in these nodes.

A bucket that can be represented by a single tree node, e.g., Bucket1 or Bucket3 in Fig. 1c, will be called a single-node bucket, and a bucket that has to be represented by two or more nodes, e.g., Bucket2 in Fig. 1c, will be called a multi-node bucket. Note that Bucket3 is considered as a single-node bucket because a sole node Node7 can represent this bucket.

Our algorithm attempts to <sup>fi</sup>nd a set of buckets such that data in each bucket are as uniformly distributed as possible. After constructing an initial set of buckets (which will be discussed later), we iteratively <sup>fi</sup>nd a skew-improved set of buckets, which will be done by appropriate merging and/or split of buckets.

## 3.1.1. Bucket merging

The bucket merge operation takes two buckets as input and returns a single multi-node bucket that is a set of all the nodes in the two input buckets. In other words, for two buckets $b _ { 1 }$ and $b _ { 2 }$ each of which is a set of tree nodes, the merging of $b _ { 1 }$ and $b _ { 2 }$ returns {tree node n $| n \in b _ { 1 } \mathrm { o r } n \in b _ { 2 } \}$

a  
b  
![](/api/attachments/KAZV746U/fulltext/images/3a8247b624dd56ad5de7dfdffbe80598bda8856f18310997be41333a6450c0d0.jpg)  
Fig. 1. A quad-tree and an organization of histogram buckets. (a) Quad-tree. (b) Geographic representation of the data set in the quad-tree. (c) Bucket organization. (d) Geographic representation of the bucket organization.

## 3.1.2. Node expansion

For a nonleaf node n in the quad-tree, the expansion of the node n, denoted by expand(n), returns the set of child nodes of the node n, i.e., {tree node i | i is a child node of n}.

## 3.1.3. Bucket split

The bucket split operation divides a bucket into two or more buckets. There are two types of split: “grouping” and “expansion”.

Example 1. Consider Fig. 2 that shows two types of bucket splitting. In this <sup>fi</sup>gure, Bucket1 is a multi-node bucket with a set of tree nodes {7, 10, 15}. A multi-node bucket can be split by properly grouping the nodes in the bucket, by which we can improve the data uniformity of the resulting buckets. Fig. 2a shows a split of Bucket1 into two buckets by grouping the nodes in Bucket1. In some cases, however, splitting a bucket by grouping the nodes in the bucket may not be the best choice, e.g., when data in Node7 representing Bucket2 are skewed. Fig. 2b shows another way of splitting a bucket where the split of Bucket1 is made by expanding a certain node, called the expansion-node, which is Node7 in this example. Suppose expand( $7 ) = \{ 4 , 5 , 6 \}$ . Then, a split of Bucket1 by expanding Node7 results in 4 buckets, where each child node of Node7 is constructed as a single-node bucket (i.e., Bucket4, 5, and 6) and the rest of nodes except Node7 in the original bucket is organized into a multi-node bucket (i.e., Bucket3).

Note that for simplicity, we used numbers to indicate nodes in Example 1, e.g., {4, 5, 6} instead of {Node4, Node5, Node6}. We will use this convention if there is no ambiguity.

## 3.1.4. SplitByExpasion

Suppose we want to split a bucket b by expanding a certain node in b. We <sup>fi</sup>rst choose a node to expand, i.e., the expansion-node. (How to choose it will be discussed later.) Let the expansion-node be n. Then, splitting bucket b by expansion returns a set of the following buckets:

• Single-node buckets, each of which has one node in expand(n).

• A bucket consisting of all the nodes in the original bucket b except the node n.

Note that if an expansion-node has k children, the SplitByExpansion results in k+1 buckets.

## 3.1.5. SplitByGrouping

Consider a multi-node bucket that has k nodes, for k 2. The number of all possible ways of grouping the nodes in the bucket, commonly known as Bell numbers, is ${ \bar { 0 ( ( k / \log { k } ) } } ^ { k } )$ [22]. Even the number of all possible ways of grouping the nodes into two groups, commonly known as Stirling number of the second kind S(k, 2), is O(2<sup>k</sup>) [8]. A grouping of nodes into two groups, which produces two sets of nodes, will be simply called a binary grouping. Note that the amount of computation to consider all possible (even binary) groupings is prohibitive in practice.

![](/api/attachments/KAZV746U/fulltext/images/11ed57657b6e86d9764f22c1be774381c1b06acf95db7cc9202f4e4cf82d1bba.jpg)  
Fig. 2. Two types of the split operation: “grouping” and “expansion”. (a) Bucket split by grouping. (b) Bucket split by expansion.

Example 2. Consider Bucket1 in Fig. 3a that is a multi-node bucket with a set of nodes {1, 2, 3}. There are three possible binary groupings, i.e., ({1}, {2, 3}), ({2}, {1, 3}), ({1, 2}, {3}). Here, in grouping ({2}, {1, 3}) in Fig. 3c, the region within the dashed line, i.e., the minimum bounding region of {2}, is contained within the region i.e., the minimum bounding region of {1, 3}, while this kind of containment between two regions does not occur in groupings ({1}, {2, 3}) and ({1, 2}, {3}) as shown inFig. 3b and d. We can notice in Fig. 3c that a fairly large empty space occurs in the region of {1, 3}, which is not desirable for data uniformity.

We will consider only the cases where there is no possibility of the aforementioned containment relationship between two groups as follows: Consider a bucket that has k nodes. Let a list of these nodes that are sorted in dimension-1 be $L { = } ( N _ { 1 } , N _ { 2 } , . . . , N _ { k } )$ . Here, the order of nodes is based on the order of the <sup>fi</sup>rst data objects in those nodes with respect to dimension-1. We only consider the bisection of L into two non-empty sorted sub-lists $L _ { 1 } = ( N _ { 1 } , . . . , N _ { i } )$ and $L _ { 2 } { = } ( N _ { j } , . . . , N _ { k } )$ such that $N _ { i }$ is an immediate predecessor of $N _ { j }$ in L. We can easily see that there are $k - 1$ ways of such bisections. These bisections are binary groupings of our interest for bucket splitting. If we have d-dimensional data, we need to consider a sorted list of nodes for each dimension. Hence, there are in total $d ( k - 1 )$ binary groupings to consider. Among them, a binary grouping that provides the minimum skew is chosen by using the measure described in the next subsection.

We have discussed two types of bucket splitting policies. Note that a bucket is splittable if one of the following conditions holds:

• There is at least one nonleaf node in the bucket.

• There are two or more nodes in the bucket.

## 3.1.6. Weighted bucket skew

Consider a grid space, as in [26], where each grid cell can contain one or more data objects. The region of a bucket consists of a certain number of grid cells. As a measure of data skew for a bucket, the standard deviation of object frequencies in all the cells of the bucket has often been used in the literature [19].

In what follows, we propose a slightly different measure of skew for a bucket, which will be used in constructing histograms.

Example 3. Consider two buckets $b _ { s m a l l }$ and $b _ { l a r g e } ,$ , and a given query. Suppose the region of bucket $b _ { s m a l l }$ is much less than that of $b _ { l a r g e }$ while the standard deviations of object frequencies in all the cells of these two buckets are the same. Suppose also that bsmall is completely contained in the query region while $b _ { l a r g e }$ is partially overlapped with the query region. In the case where a bucket is completely contained in the query region, $\mathrm { e . g . , } b _ { s m a l l } ,$ the data skew for this bucket has nothing to do with the accuracy of an estimated value for the bucket. In other words, this bucket behaves as if there were no data skew. In the other case, e.g., $b _ { l a r g e } ,$ the accuracy of an estimated value for a bucket is affected by the standard deviation of object frequencies in all the cells of the bucket. In general, as the size of the region of a bucket decreases, the probability that the bucket region is completely contained in a given query region increases.

The weighted skew de<sup>fi</sup>ned below is based on the intuition that the effect of the data skew tends to decrease as the size of the region of a bucket decreases.

De<sup>fi</sup>nition 1 (Weighted skew of a bucket). The weighted skew of a bucket b, denoted by wSkew(b), is de<sup>fi</sup>ned as

$$
w S k e w (b) = s i z e (b) \cdot s d (b),
$$

where size(b) and sd(b) denote the size of the region of b and the standard deviation of object frequencies in all the cells of b, respectively.

The weighted skew of a node or region n is similarly de<sup>fi</sup>ned as wSkew $\begin{array} { r } { \nu ( n ) { = } s i z e ( n ) { \cdot } s d ( n ) } \end{array}$ . In the rest of the paper, for simplicity, we will use a skew to denote a weighted skew in De<sup>fi</sup>nition 1.

a  
![](/api/attachments/KAZV746U/fulltext/images/486f5bbcf2908a0e5f0d8fe207f8702e69621d85ab0719f5b9e4863d21b2c4de.jpg)

b  
![](/api/attachments/KAZV746U/fulltext/images/cbf4a5475b1d0c07cef9267f900722fe4afc19eb1f53a993e9d4ec409b7cdf17.jpg)

![](/api/attachments/KAZV746U/fulltext/images/2912779ab26d36d7674a4f18715c28ec3579144d994a7cc16ca51b1546d3cba7.jpg)

d  
![](/api/attachments/KAZV746U/fulltext/images/290aaccb7c782da7969502182dc1eaa5acf8cb28e253c331dab5c1ef9426ab5c.jpg)  
Fig. 3. Binary groupings of tree nodes in a bucket. (a) A multi-node bucket that has a set of nodes {1, 2, 3}. (b) Binary grouping ({1}, {2, 3}). (c) Binary grouping ({2}, {1, 3}). (d) Binar grouping ({1, 2}, {3}).

## 3.2. Sketch of the proposed method

Consider again the quad-tree and the data set in Fig. 1a and b. Let the prede<sup>fi</sup>ned number of buckets for a histogram be B. Let G be the set of buckets for a histogram. Construction of the proposed histogram, called the Q-Histogram, proceeds as follows: Initially, a bucket with the root node of the tree is created and inserted into G, i.e., G={{8}}. Then, for the construction of B buckets, the bucket split and merge process illustrated in Fig. 4a is executed. Suppose B, i.e., the number of buckets to be constructed, is 3. As a split step, certain splittable buckets in G are split in a repeatable manner until the number of buckets exceeds B. For example, consider G={{8}} again. The sole bucket in G, i.e., bucket {8}, is split by expansion into three buckets {3}, {4}, and {7}, i.e., G becomes {{3}, {4}, {7}} as shown in Fig. 4b. Here, the region of each bucket is the minimum bounding region of all the data objects in its corresponding nodes. Suppose the skew of bucket {3} in the current G is greater than those of the other buckets {4} and {7}. Then, bucket {3} is split by expansion into buckets {1} and {2}, i.e., G={{1}, {2}, {4}, {7}} as shown in Fig. 4c. Now the number of buckets in G is 4, which is greater than B. Thus, we need to reduce the number of buckets by one. The next step is the merge step. Among all possible ways of merging two buckets, suppose the merging of buckets {2} and {4} is the best merging. Then, by merging these buckets, G becomes {{1}, {2, 4}, {7}} as shown in Fig. 4d. The details of the bucket split and merge process will be discussed in the following section.

## 3.3. A new histogram construction using the existing quad-tree

In this section, we describe how to construct our proposed histogram in detail. The proposed method starts with the initialization step, where i) a bucket consisting of the root node of a quad-tree is constructed and inserted into the set of buckets G, and ii) for each node except the root node, we <sup>fi</sup>nd the minimum bounding region (MBR) of data and compute the skew of the MBR. Then, we construct the set G of B buckets by iteratively performing the bucket split and merge process, which consists of the split step and the merge step. Each of these steps will be described in more detail below.

• The Split Step: Among all the splittable buckets in G, a bucket called the split-bucket whose skew is the highest is split to construct new buckets. Since there are many ways of splitting a bucket, we need to determine which way we split the split-bucket.

![](/api/attachments/KAZV746U/fulltext/images/6bb404a95c77305822ba412d4dd06a2aa428038b02c2aa329a3fc7e138698b87.jpg)  
Fig. 4. Histogram construction process for the quad-tree and the data set in Fig. 1a and b. (a) The bucket split and merge process. (b) Bucket organization for G = {{3}, {4}, {7}}. (c) Bucket organization for G = {{1}, {2}, {4}, {7}}. (d) Bucket organization for G = {{1}, {2, 4}, {7}}.

Suppose that the split-bucket is a single-node bucket. Then we have only one way of splitting, i.e., SplitByExpansion. When the split-bucket is a multi-node bucket with k nodes, for k≥2, there are in total k+d(k−1) ways of splitting, i.e., k possible splits by SplitByExpansion and d(k−1) splits by SplitByGrouping where d is the dimension of data.

Among these splits, a split that has the minimum split-induced skew factor is executed. Here, a split-induced skew factor of a given split is de<sup>fi</sup>ned as the sum of all the skews of buckets created by this split. Then, the split-bucket is removed from G and the new buckets created by the split are inserted into G. This procedure of bucket splitting is repeatedly performed until the number of buckets in G exceeds B.

• The Merge Step: After the split step, the number of buckets in G is greater than B. In the merge step, we reduce the number of buckets by merging some buckets. Here, we repeatedly perform a merging of two buckets into one until the total number of buckets reduces to B.

Suppose a set G has m buckets, for m≥2. Then, there are C possible bucket merges. Among these bucket merges, the one that has the maximum merging preference factor is performed. Here, a merging preference factor of a merging of two buckets b and b into a bucket b is de<sup>fi</sup>ned as wSkew(b )+wSkew(b )−wSkew(b ).

Then, the two merged buckets are removed from G and the new bucket created by the merge is inserted into G. Note that performing one merge decreases the size of G (i.e., the number of buckets in G) by one. We can repeat merges of buckets until the total number of buckets becomes B.

## 3.3.1. Repetition of the bucket split and merge process

We can complete our histogram construction by using a single bucket split and merge process just described. However, the following example shows that we can improve the effectiveness of our histogram by applying the bucket split and merge process several times.

Example 4. Consider again the quad-tree and the data set in Fig. 1a and b, and suppose again that B is 3.Fig. 5 shows the result obtained by applying the bucket split and merge process just once.Fig. 6shows a slightly different approach where the bucket split and merge process is repeated two times. In the <sup>fi</sup>rst iteration of the bucket merge and split process, bucket merges in the merge step continues until the number of buckets in G is B−1, not B. In the next iteration, the merge step returns G whose size is B. As can be seen inFig. 6a, the set of buckets G = {{1}, {2, 4, 7}} is obtained after the <sup>fi</sup>rst iteration. Then using this G, we repeat the bucket split and merge process again. Suppose that bucket {2, 4, 7} in G is split by the expansion of Node7, and G becomes {{1}, {2, 4}, {5}, {6}} as shown in the left <sup>fi</sup>gure of Fig. 6b, and then, a merge of buckets {2, 4} and {5} is performed, i.e., G ={{1}, {2, 4, 5}, {6}} as shown in the right <sup>fi</sup>gure of Fig. 6b. We can see that the data uniformity of those buckets in G is better than that of buckets in the right <sup>fi</sup>gure of Fig. 5b.

The underlying reason of applying the bucket split and merge process multiple times is as follows. As mentioned in Section , there are numerous ways of partitioning leaf nodes into B groups. Here, the <sup>fi</sup>rst application of the bucket split and merge process is too much affected by the original data partition implied in the quad-tree structure that does not take into account the skew of data distribution seriously. By applying the bucket split and merge process several times, we can reduce the dependency on the original data partition of the quad-tree and can have a chance of <sup>fi</sup>nding a better data partition, i.e., a set of buckets each of which has a better data uniformity.

![](/api/attachments/KAZV746U/fulltext/images/e4e34046893d1a5705f985fd3c38973a95807bf3bb4eeb85047d71861619d590.jpg)  
Fig. 5. Completion by a single bucket split and merge process. (a) The result of the split step. (b) The result of the merge step.

How to repeat the bucket split and merge process so that the data in each bucket is as uniformly distributed as possible is a dif<sup>fi</sup>cult problem because of the large search space of possible solutions and the large number of local optima that arise. We heuristically use the following strategy for a reasonable computation time.

1) The 1st iteration: Construct G whose size is $B / 2$

2) The 2nd iteration: Construct G whose size is $B / 2 + B / 2 \sp 2 .$

i) The i-th iteration: Construct G whose size is $B / 2 + \ldots + B / 2 ^ { i } .$

Iteration continues until the size of G becomes B.

Here, we assume that each $B / 2 + . . . + B / 2 ^ { i }$ term is actually $\lceil B / 2 + \ldots +$ B/2<sup>i</sup>⌉. Then, we can easily see that the size of G always converges to B and the total number of iterations is O(logB).

In each iteration (except the <sup>fi</sup>rst), the initial G is the one that is the result of the previous iteration. From this set of buckets $G ,$ the split step performs bucket splitting repeatedly until the size of G exceeds B. Then, in the merge step we perform bucket merges until the size of G becomes our target number speci<sup>fi</sup>ed above.

Example 5. Consider the iterations of the bucket split and merge process, where the number of buckets B we need to construct is 16. The size of G converges to B after O(logB) iterations. After the 1st iteration, the size of G is $( 1 / 2 ) B = ( 1 - 1 / 2 ) B = 8 .$ After the 2nd iteration, the size of G is $( 1 / 2 ) B + ( 1 / 4 ) B = ( 1 - 1 / 2 ^ { 2 } ) B = 1 2 .$ . Such iterations continue until the size of G is 16. Thus, in this example, the size of G becomes 16 after the 5th iteration.

Fig. 7 shows the proposed algorithm ConstructQHistogram that constructs the set of buckets G by iterations of the bucket split and merge process. This algorithm takes as input a quad-tree and B, i.e., the prede<sup>fi</sup>ned number of buckets, which is typically up to 254 in database systems [12]. Note that we assume the number of leaf nodes in a quadtree exceeds B.

## 3.3.2. Computation of weighted skews (Line 3)

Suppose the minimum bounding region of data in a node n consists of p grid cells. Suppose also that object frequencies at each grid cell are $f _ { 1 } , f _ { 2 } , . . . , f _ { p } .$ Then, the skew of the minimum bounding region of data in the node n, denoted by wSkew(n), is

$$
\begin{array}{l} w S k e w (n) = s i z e (n) \cdot s d (n) \\ = p \sqrt {\frac {\sum_ {i = 1} ^ {p} f _ {i} ^ {2}}{p} - \left(\frac {\sum_ {i = 1} ^ {p} f _ {i}}{p}\right) ^ {2}} \\ = \sqrt {p \left(\sum_ {i = 1} ^ {p} f _ {i} ^ {2}\right) - \left(\sum_ {i = 1} ^ {p} f _ {i}\right) ^ {2}}. \end{array}\tag{1}
$$

From Eq. (1), it can be derived that for the computation of the skew of the minimum bounding region, the following are only needed: i) p, ${ \mathrm { i i } } ) \sum _ { i = 1 } ^ { p } \ f _ { i } ^ { 2 } , { \mathrm { a n d ~ i i i } } ) \sum _ { i = 1 } ^ { p } \ f _ { i } .$ . When these are computed according to the postorder traversal of a quad-tree, the computation of the skews for all the nodes can be performed by only one scan of the quad-tree, which typically resides on the disk.

Theorem 1. The worst case time complexity of Algorithm ConstructQHistogram is $0 ( V + B ^ { 2 } ( \log B ) ^ { 2 } )$ , where V is the total number of entries in the leaf nodes of a quad-tree and B is a constant that denotes the prede<sup>fi</sup>ned number of buckets.

Proof. Initialization in Lines 1–3 performs a scan of the quad-tree, which takes O(V) time. Iterations of the bucket split and merge process in Lines 4–7 take $0 ( B ^ { 2 } ( \log B ) ^ { 2 } )$ time, as described next.

Table 1 shows the number of bucket splits and bucket merges, in the worst case, in each iteration of the bucket split and merge process. Note that the size of G after the split step is B + ε in general, where ε is some small number. Consider the computation for splitting a certain split-bucket B times. Suppose a split-bucket has k nodes. Here, k is some constant. Then, for each splitting, we need to choose the best among $0 ( k + d ( k - 1 ) )$ ways of splitting. Thus, splitting a splitbucket B times takes $0 ( B ( k + d ( k - 1 ) ) )$ time. Now consider the computation for performing a bucket merge B times. Initially, we choose the best among ${ \sf O } \left( _ { B } { \sf C } _ { 2 } \right)$ ways of merging. Note that G has approximately B buckets at the beginning of the merge step in each bucket split and merge process. Suppose that a priority queue, implemented with a binary heap data structure, is used to maintain merging preference factors of all possible pairs of two buckets in $G .$ By using the priority queue, we can <sup>fi</sup>nd the best merge in constant time. Initial construction of the priority queue can be done in $0 ( B ^ { 2 } )$ time. After each merge, O(BlogB) time is taken to appropriately maintain the priority queue. Thus, the computation for performing a bucket merge B times takes O(B<sup>2</sup>logB) time. As a result, each bucket split and merge process takes $0 ( B ^ { 2 } \mathrm { l o g } B )$ time. Since the number of iterations of the bucket split and merge process is O(logB), the iterations of the bucket split and merge process require $0 ( B ^ { 2 } ( \log B ) ^ { 2 } )$ time. Consequently, the complexity of algorithm ConstructQHistogram becomes ${ \bar { 0 } } ( V + { \bar { B } } ^ { 2 } ( \log B ) ^ { 2 } )$ . ■

The time O(V) from the initialization step dominates the time complexity of Algorithm ConstructQHistogram in general. Note that V is the total number data objects when a histogram is built on attributes that constitute a key of a relation, and otherwise can be less than the total number of data objects.

![](/api/attachments/KAZV746U/fulltext/images/9d690d9ee05a2e5b5f756ec58e51ae958018f7e2bd819272c1293fb5b1d4de64.jpg)

![](/api/attachments/KAZV746U/fulltext/images/8c9ae2df0ffa6b6669b2a8bdad6c222db7d08b664c234dcec4e73c4a9fa27db0.jpg)

![](/api/attachments/KAZV746U/fulltext/images/04823d556c448db820352480824357c283327dd379b8951fd9c76b5097950236.jpg)

![](/api/attachments/KAZV746U/fulltext/images/de8f3663c4d164b4f6d5d86d5a3d0ef03aae759ef4aa603a225d5ae694f19142.jpg)  
Fig. 6. Completion by two iterations of the bucket split and merge process. (a) 1st iteration. (b) 2nd iteration.

Fig. 8a shows the two-dimensional North East data set, which is a reallife data set (described later in Section 4.1). Fig. 8b shows the proposed histogram for the North East data set. We also present EquiDepth[25], MinSkew[1], GenHist[15,16], and RK-Hist[10] histograms, described in Section 2, for the data set in Fig. 8c, d, e, and f, respectively.

## 4. Performance experiments

We have conducted extensive experiments using synthetic data as well as real-life data, and compared our results with those of EquiDepth [25], MinSkew[1], GenHist[15,16], RK-Hist[10] histograms, and Haar wavelet transformation [24]. All experiments reported in this section have been performed on a Windows server 2003 workstation with two Xeon 3GHz quad-core processors and 8GB memory. The algorithms have been implemented in Visual C++ 2008.

![](/api/attachments/KAZV746U/fulltext/images/37b29814660b8dbfdae5fe951f1cf4ebf39bd0b669447c4a6185d2ab0b0e6d60.jpg)  
Fig. 7. The proposed quad-tree based histogram construction algorithm

e  
Table 1  
The number of bucket splits and bucket merges in the bucket split and merge process.

<table><tr><td></td><td>1st Iteration</td><td>2nd Iteration</td><td>3rd Iteration</td></tr><tr><td>The split step</td><td> $O(B)$ </td><td> $O((1/2)B)$ </td><td> $O((1/2^2)B)$ </td></tr><tr><td>The merge step</td><td> $O((1/2)B + \varepsilon)$ </td><td> $O((1/2^2)B + \varepsilon)$ </td><td> $O((1/2^3)B + \varepsilon)$ </td></tr></table>

## 4.1. Experiment setup

## 4.1.1. Data sets

We generated synthetic data sets, which will be called Cluster data, as suggested in [15,16] with many clusters and therefore high correlations between attributes. The parameters of the data generator are i) the dimension of the data space, ii) the total number of clusters, and iii) the maximum size of a cluster, represented by the ratio of the cluster size to the domain size, respectively set to 2\~5, 30, and 1% in our experiments. The clusters, each de<sup>fi</sup>ned as a hyperrectangle, are randomly located within the data space and the data in each cluster are randomly distributed. Each synthetic data set contains $1 0 ^ { 6 }$ data objects in the space of [1,1000]<sup>d</sup>, where d is the dimension of the data space.

For our real-life data experiments, we used the following data sets: i) the Greece Cities data set, which contains 5922 cities and villages in Greece. ii) the Digital Chart of the World data set, which contains 19,499 populated places in the United States of America and Mexico. iii) the Sequoia data set [31], which contains 62,556 locations in California. iv) the North East data set, shown in Fig. 8a, which contains

123,593 postal addresses in three metropolitan areas—New York Philadelphia, and Boston.

Fig. 9 shows the data sets except that shown in Fig. 8a. Note that the Greece Cities data, the Digital Chart of the World data, the Sequoia data, and the North East data are publicly available on the World Wide Web at http://www.rtreeportal.org and are two-dimensional spatial data sets, which have many real-world applications such as Geographic Information Systems.

## 4.1.2. Buckets, quality measure, and test queries

For fair comparison, all the methods are allowed to have the same amount of memory. We constructed histograms consisting of 50 \~ 1000 buckets for testing the accuracy of histograms with various number of buckets.

Our comparisons are based on the average relative error, commonly used as a performance metric in selectivity estimation, described below: Let θ be the actual result size (or the object frequency) of a query q and θ′ be the estimated object frequency of q by a method. Then, the absolute error $e ^ { a b s }$ and the relative error $e ^ { r e l }$ are de<sup>fi</sup>ned as follows:

$$
e ^ {a b s} = | \theta - \theta^ {\prime} |. e ^ {r e l} = e ^ {a b s} / \theta = | \theta - \theta^ {\prime} | / \max \{\theta , 1 \}.
$$

For a set of queries, the average relative error is de<sup>fi</sup>ned as the sum of the relative errors for all the queries divided by the number of queries. For the test queries, we used 10,000 queries in each experiment, whose regions are randomly located within the data space.

## 4.2. Experimental results

Fig. 10 shows how varying the number of buckets (or the amount of memory allowed) affects the accuracy of the methods for various data sets. Note that the size of a query region, represented by the ratio of the query region size to that of the domain size, is set to 10% and the y-axis is shown on a log scale. In general, average relative errors tend to be reduced with the increasing number of buckets. This is because, when the number of buckets increases, more accurate statistics can be obtained. It can be seen that the proposed method, denoted by Q-Histogram, works generally better than other existing methods. The primary reason for this improvement is that the proposed method effectively handles data skews, which may decrease the accuracy of selectivity estimation, by appropriate merging and/or split of buckets.

a  
![](/api/attachments/KAZV746U/fulltext/images/d75af20ab7a4dfddc24eb1e9d5157c70a5a342f19ae4a7ef15415fa2c36f6231.jpg)

d  
![](/api/attachments/KAZV746U/fulltext/images/0b9fd27090ae78854e628a7df3112ed853fb17fdaa89d83c0c14aca9625d9ca3.jpg)

![](/api/attachments/KAZV746U/fulltext/images/d31cfc90bd3976ab3da11e737f755e6bfcbbc4a25a1866bfbecd8399007850fb.jpg)

c  
![](/api/attachments/KAZV746U/fulltext/images/0f5760a919015ff56891c73199dfd4c58406f1169442a08d9e75c7207b303886.jpg)

![](/api/attachments/KAZV746U/fulltext/images/29bda11937bc73ecf686cf2bee86d480dd314b5e982cdaa792e1f3d9625e5e2c.jpg)

![](/api/attachments/KAZV746U/fulltext/images/2254c84b6880c0ec6a645343e0aed1bf411cb1290d64f45d1d6ff2b2b9fc0d64.jpg)  
Fig. 8. North East data and various histograms (50 buckets). (a) North East data. (b) Our proposed histogram. (c) EquiDepth histogram. (d) MinSkew histogram. (e) GenHist histogram. (f) RK-Hist histogram.

a  
![](/api/attachments/KAZV746U/fulltext/images/d368398e7a2575e4c4be9506ccf59a0c972fcffd05f747036e0fc38b4d65c590.jpg)

b  
![](/api/attachments/KAZV746U/fulltext/images/5a705bb6129c969960bb0e339ee37512b8dde3bb3aaaea46b8bbb23f5f9f7c74.jpg)

c  
![](/api/attachments/KAZV746U/fulltext/images/4ae135e3ae1252607f49e33258648a0e734f06180ec08443b573507bcd2500ba.jpg)

d  
![](/api/attachments/KAZV746U/fulltext/images/2cea6f2a356b997bf61d76d29efa1eb6a4418bb3bfe254fd7a67e980aabb989f.jpg)

e  
![](/api/attachments/KAZV746U/fulltext/images/c91f621d3f1c64d677cdc73cda8124f20648aae89dbde1c345bb92a0c1f0c359.jpg)  
Fig. 9. Data sets. (a) Cluster (2D) data. (b) Cluster (3D) data. (c) Sequoia data. (d) Greece Cities data. (e) Digital Chart of the World data.

a  
![](/api/attachments/KAZV746U/fulltext/images/1e26a6c7b7dc8c941838082a5837ebc3847791d75d6760741668a413ee143ff7.jpg)

b  
![](/api/attachments/KAZV746U/fulltext/images/20a3ce3ac80b6d32009d869c06b3ccc79fdd5a3d36a412b38858ac84acdf0307.jpg)

![](/api/attachments/KAZV746U/fulltext/images/36127025ef46a25003944966f725e90d65780c6df662d2a47f97f921f28751b0.jpg)

d  
![](/api/attachments/KAZV746U/fulltext/images/f1dd3865db5dd0e8b9d9435c2417c6e62c5f0650c07982ca948974719e078032.jpg)

<table><tr><td></td><td>Q-Histogram</td><td>MinSkew</td></tr><tr><td></td><td>GenHist</td><td>RK-Hist</td></tr><tr><td></td><td>EquiDepth</td><td>Wavelet</td></tr></table>

Fig, 10, Average relative errors for varving number of buckets. (a) North East data. (b) Seguoia data. (c) Greece Cities data. (d) Digital Chart of the World data

Table 3  
![](/api/attachments/KAZV746U/fulltext/images/afe9ed6ccb3ca74a70d3bbeb7c6552e187a5fdfaab0810fab7b92dc83ffd7ea6.jpg)

Fig. 11 shows how varying the query region size affects the performance of the methods for various data sets. Note that the number of buckets for a histogram is set to 500 and the y-axis is shown on a log scale. As shown in this <sup>fi</sup>gure, as the size of the query region increases, the accuracy of selectivity estimation tends to increase. When the size of the query region increases, the number of histogram buckets that are fully contained in the query region also increases. That is, the effect of buckets that partially overlap with the query region, which are the sources of incorrect selectivity estimation, reduces with the increase of the query region. As can be seen in Fig. 11, the performance of the proposed Q-Histogram is better than other existing methods in many cases. EquiDepth histograms show relatively good accuracy for the Greece Cities data set, as shown in Fig. 10c and Fig. 11c. The underlying assumption of EquiDepth is that the data objects of buckets can be close to uniformly distributed when the whole data set is divided into buckets with the equal number of data objects. The satisfaction of this assumption mostly depends on the distribution of a given data set. In the case when the assumption is considerably satis<sup>fi</sup>ed for a given data set, e.g., the Greece Cities data set, EquiDepth gives relatively good accuracy. Note that, however, as shown in the other <sup>fi</sup>gures of Figs. 10–11 as well as Table 2 described below, the assumption of EquiDepth may not hold for various real-life and synthetic data sets, and thus EquiDepth generally provides les accuracy compared to our proposed Q-Histogram.

Table 2  
Average relative errors for various data sets of varying dimension.

<table><tr><td rowspan="2">Dimension</td><td colspan="4">Average relative error (%)</td></tr><tr><td>2D</td><td>3D</td><td>4D</td><td>5D</td></tr><tr><td>Q-Histogram</td><td>12.02</td><td>10.19</td><td>4.21</td><td>13.81</td></tr><tr><td>MinSkew</td><td>12501.43</td><td>2939.87</td><td>1383.18</td><td>188.21</td></tr><tr><td>GenHist</td><td>3868.81</td><td>1470.15</td><td>514.48</td><td>1297.18</td></tr><tr><td>RK-Hist</td><td>1392.64</td><td>545.88</td><td>280.39</td><td>259.00</td></tr><tr><td>EquiDepth</td><td>2211.8</td><td>1040.57</td><td>163.32</td><td>188.18</td></tr></table>

Average relative errors for various data skew of a bucket.

<table><tr><td rowspan="2">Data skew</td><td colspan="3">Average relative error (%)</td></tr><tr><td>Weighted skew in Definition 1</td><td>Sum of squared errors*</td><td>Data skew in [1]</td></tr><tr><td>2D</td><td>12.02</td><td>16.56</td><td>62112.95</td></tr><tr><td>3D</td><td>10.19</td><td>61.00</td><td>10251.14</td></tr><tr><td>4D</td><td>4.21</td><td>71.98</td><td>5595.75</td></tr><tr><td>5D</td><td>13.81</td><td>554.39</td><td>6057.96</td></tr></table>

\* The sum of squares of absolute errors for all the locations within a bucket. An absolute error of a location r is the difference of the real object frequency at location r and the estimate of the object frequency based on the uniform distribution assumption within the bucket.

Table 2 shows the performance results of the histogram methods for varying dimension. In this experiment, we used a two-, a three-, a four-, and a <sup>fi</sup>ve-dimensional synthetic Cluster data set. Note that the number of buckets for a histogram is set to 500 and the size of the query region is set to 5%. As shown in Table 2, the results of Q-Histogram are better than those obtained from other existing methods.

![](/api/attachments/KAZV746U/fulltext/images/2f98061e7d7ad3c0ec40a952c8368ee4751a08524679a961a7a36278c7fc3ee3.jpg)  
c

b  
![](/api/attachments/KAZV746U/fulltext/images/fde57eb4a83f3e951729848935cf1f9119c1ee46e7b1a6e2ae8c1bdc45ba51a9.jpg)

![](/api/attachments/KAZV746U/fulltext/images/5f806ced6852e12f7cebf458528edde0009f283b400513e663486b2a5f546ce7.jpg)

![](/api/attachments/KAZV746U/fulltext/images/30d31068875b098344ca814da0e5f1867c6c6c6c6aae75f4653bb5219c4ef4e8.jpg)  
Fig, 11, Average relative errors for varving the query region size. (a) North East data. (b) Seguoig data. (c) Greece Cities data. (d) Digital Chart of the World data

Construction time of histograms in various methods.

<table><tr><td rowspan="2">Size of a data set</td><td colspan="8">Time taken (sec)</td></tr><tr><td colspan="4"> $10^6$ </td><td colspan="4"> $5 \cdot 10^6$ </td></tr><tr><td>Dimension</td><td colspan="2">2D</td><td colspan="2">4D</td><td colspan="2">2D</td><td colspan="2">4D</td></tr><tr><td>Numbers of buckets</td><td>250</td><td>500</td><td>250</td><td>500</td><td>250</td><td>500</td><td>250</td><td>500</td></tr><tr><td>Q-Histogram</td><td>0.25</td><td>0.66</td><td>1.41</td><td>1.97</td><td>0.27</td><td>0.64</td><td>6.47</td><td>7.06</td></tr><tr><td>MinSkew</td><td>1.00</td><td>0.95</td><td>1.45</td><td>1.39</td><td>5.23</td><td>4.66</td><td>7.42</td><td>6.89</td></tr><tr><td>GenHist</td><td>6.91</td><td>7.89</td><td>4.86</td><td>6.72</td><td>28.18</td><td>37.03</td><td>20.56</td><td>21.67</td></tr><tr><td>RK-Hist</td><td>1.42</td><td>1.14</td><td>2.50</td><td>2.20</td><td>11.33</td><td>7.34</td><td>69.16</td><td>13.86</td></tr><tr><td>Equi-Depth</td><td>1.34</td><td>1.25</td><td>2.23</td><td>2.27</td><td>7.70</td><td>7.56</td><td>15.17</td><td>14.63</td></tr></table>

In order to study the effect of the use of the weighted skew in De<sup>fi</sup>nition 1 in our proposed Q-Histogram, we have empirically investigated the accuracy of our proposed histograms using different data skew measures. Table 3 shows the experimental results of the accuracy of Q-Histogram for different data skew measures. In this experiment, we used our Q-Histogram as a histogram construction method, and used the weighted skew in De<sup>fi</sup>nition 1 as well as two other well-known measures of data skew as a data skew measure. In the experiment, we used a two-, a three-, a four- and a <sup>fi</sup>ve-dimensional synthetic Cluster data set. Note that the number of buckets for a histogram is set to 500 and the size of the query region is set to 5%. As seen in the results in Table 3, the performance of our proposed histograms using the weighted skew in De<sup>fi</sup>nition 1 is better than those using other measures of data skew in all the cases.

Table 4 shows the construction time of the histogram methods for different number of data objects. In this experiment, we used a twoand a four-dimensional synthetic Cluster data set. As shown in this table, the construction time of the proposed method is generally less than that of other existing histogram methods. The main reason of this improvement is that the proposed histogram is constructed by using the data partition information implied in a quad-tree with the minimum number of scanning, i.e., only one scanning, of the whole data set.

In summary, our experimental results show that the proposed Q-Histogram generally provides a better accuracy with less computation time than other existing methods in all our experiments that use reallife data as well as synthetic data.

Note that quad-tree indexes are usually used for data whose dimensions are not very high. Since our Q-Histograms are based on quad-trees, we can say that Q-Histograms are appropriate for data whose dimensions are not very high. As shown in Table 2, our Q-Histograms provide the best accuracy most of the time until the dimension of data is <sup>fi</sup>ve.

## 5. Conclusions and future work

Histograms can be useful for database query optimization and various query processing techniques. As noted in the literature, some of existing index structures can be a good starting point for constructing histograms. In particular, when a quad-tree, one of the most popular index structures, already exists and is used for some application, the process of constructing a histogram can be accelerated by using the data partition information implied in the quad-tree.

In this paper, we have proposed a new multidimensional histogram method called the Q-Histogram that utilizes existing quad-trees. We have provided a new measure of skew for a histogram bucket and an iterative algorithm for constructing skew-tolerant histograms. We have performed extensive experiments to evaluate the performance of Q-Histogram on various well-known data sets and to compare it with those of other existing methods. The experimental results show that the proposed method generally provides a better accuracy, with better computational ef<sup>fi</sup>ciency, than other existing methods.

We have assumed in this work that a quad-tree already exists. If the assumption is not true, we can construct a quad-tree in the initialization step of constructing a histogram. In general, a quad-tree can be constructed in O(nlogn) time, where n is the number of data.

In this paper, we have focused on the use of the quad-tree; however, the main principles of our method are general enough to be applicable to other multidimensional index structures such as R-trees and kd-trees. We are investigating the performance of the proposed histograms when these index structures are used.

## Acknowledgment

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MEST) (No. 2010- 0018865). We also thank Dr. Kyoung-Gu Woo and AceAnalytics Project members (Samsung Advanced Institute of Technology, Samsung Electronics) for their support. Moreover, the authors would like to thank the Editor-in-Chief and the anonymous referees for their valuable comments and help.

## References

[1] S. Acharya, V. Poosala, S. Ramaswamy, Selectivity estimation in spatial databases, ACM SIGMOD Int. Conf. on Management of Data, 1999, pp. 13–24.

[2] A. Ayansoa, P.B. Goesb, K. Mehtac, A practical approach for ef<sup>fi</sup>ciently answering top-k relational queries, Decis. Support Syst. 44 (1) (2007) 326–349.

[3] N. Bruno, S. Chaudhuri, L. Gravano, S.T. Holes, A multidimensional workloadaware histogram, ACM SIGMOD Int. Conf. on Management of Data, 2001, pp. 211–222.

[4] N. Bruno, S. Chaudhuri, L. Gravano, Top-k selection queries over relational databases: mapping strategies and performance evaluation, ACM Trans. Database Syst. 27 (2) (2002) 153–187.

[5] S. Chaudhuri, L. Gravano, Evaluating top-k selection queries, Int. Conf. on Very Large Data Bases, 1999, pp. 397–410.

[6] S. Chaudhuri, N. Dalvi, R. Kaushik, Robust cardinality and cost estimation for skyline operator, IEEE Int. Conf. on Data Eng., 2006, p. 64.

[7] Y.J. Choi, C.W. Chung, Selectivity estimation for spatio-temporal queries to moving objects, ACM SIGMOD Int. Conf. on Management of Data, 2002, pp. 440–451.

[8] L. Comtet, Advanced Combinatorics: The Art of Finite and In<sup>fi</sup>nite Expansions, Springer, 1974.

[9] G. Cormode, M. Garofalakis, Histograms and wavelets on probabilistic data, IEEE Trans. Knowl. Data Eng. 22 (8) (2010) 1142–1157.

[10] T. Eavis, A. Lopez, RK-hist: an r-tree based histogram for multi-dimensional selectivity estimation, ACM Int Conf on Inf and Knowl Management, 2007 pp 475–484

[11] P.B. Gibbons, Y. Matias, V. Poosala, Fast incremental maintenance of approximate histograms, ACM Trans. Database Syst. 27 (3) (2002) 261–298.

[12] R. Greenwald, D.C. Kreines, Oracle in a Nutshell, O'Reilly & Associates, Sebastopol, California 2002

[13] S. Guha, K. Shim, A note on linear time algorithms for maximum error histograms, IEEE Trans. Knowl. Data Eng. 19 (7) (2007) 993–997.

[14] S. Guha, N. Koudas, K. Shim, Approximation and streaming algorithms for histogram construction problems, ACM Trans. Database Syst. 31 (1) (2006) 396–438.

[15] D. Gunopulos, G. Kollios, V.J. Tsotras, C. Domeniconi, Approximating multidimensional aggregate range queries over real attributes, ACM SIGMOD Int. Conf. on Management of Data, 2000, pp. 463–474.

[16] D. Gunopulos, G. Kollios, V.J. Tsotras, C. Domeniconi, Selectivity estimators for multidimensional range queries over real attributes VLDBI. 14 (2) (2005) 137–154

[17] P.J. Haas, A.N. Swami, Sequential sampling procedures for query size estimation, ACM SIGMOD Int. Conf. on Management of Data, 1992, pp. 341–350.

[18] Y.E. Ioannidis, Query optimization, ACM Comput. Surv. 28 (1) (1996) 121–123.

[19] Y.E. Ioannidis, The history of histograms, Int. Conf. on Very Large Data Bases, 2003, pp. 19–30.

[20] Y.E. Ioannidis, S. Christodoulakis, Optimal histograms for limiting worst-case error propagation in the size of join Results, ACM Trans. Database Syst. 18 (4) (1993) 709–748.

[21] I. Kamel, C. Faloutsos, On packing r-trees, ACM Int. Conf. on Inf. and Knowl. Management, 1993, pp. 490–499.

[22] D.E. Knuth, The art of computer programming, Fascicle 3, vol. 4, Addison-Wesley, Stoughton, MA, 2005.

[23] J. Lee, D. Kim, C. Chung, Multi-dimensional selectivity estimation using compressed histogram information, ACM SIGMOD Int. Conf. on Management of Data, , 1999, pp. 205–214.

[24] Y. Matias, J.S. Vitter, M. Wang, Wavelet-based histograms for selectivity estimation, ACM SIGMOD Int. Conf. on Management of Data, 1998, pp. 448–459.

[25] M. Muralikrishna, D.J. DeWitt, Equi-depth histograms for estimating selectivity factors for multidimensional queries, ACM SIGMOD Int. Conf. on Management of Data, 1988, pp. 28–36.

[26] S. Muthukrishnan, V. Poosala, T. Suel, On rectangular partitionings in two dimensions: algorithms, complexity, and Applications, Int. Conf. on Database Theory, 1999, pp. 236–256.

[27] D. Papadias, Y. Tao, G. Fu, B. Seeger, Progressive skyline computation in database systems, ACM Trans. Database Syst. 30 (1) (2005) 41–82.

[28] V. Poosala, Y.E. Ioannidis, Estimation of query-result distribution and its application in parallel-join load balancing, Int. Conf. on Very Large Data Bases, 1996, pp. 448–459.

[29] V. Poosala, Y.E. Ioannidis, Selectivity estimation without the attribute value independence assumption, Int. Conf. on Very Large Data Bases, 1997, pp. 486–495.

[30] U. Srivastava, P.J. Haas, V. Markl, N. Megiddo, M. Kutsch, T.M. Tran, ISOMER: consistent histogram construction using query feedback, IEEE Int. Conf. on Data Eng., 2006, p. 39.

[31] M. Stonebraker, J. Frew, K. Gardels, J. Meredith, The SEQUOIA 2000 storage benchmark, ACM SIGMOD Int. Conf. on Management of Data, 1993, pp. 2–11.

[32] J. Sun, Y. Tao, D. Papadias, G. Kollios, Spatio-temporal join selectivity, Inf. Syst. 31 (8) (2006) 793–813.

[33] Y. Tao, J. Sun, D. Papadias, Selectivity estimation for predictive spatio-temporal queries, IEEE Int. Conf. on Data Eng., 2003, pp. 417–428.

[34] Y. Tao, J. Zhang, D. Papadias, N. Mamoulis, An ef<sup>fi</sup>cient cost model for optimization of nearest neighbor search in low and medium dimensional spaces, IEEE Trans. Knowl. Data Eng. 16 (10) (2004) 1169–1184.

[35] N. Thaper, S. Guha, P. Indyk, N. Koudas, Dynamic multidimensional histograms ACM SIGMOD Int. Conf. on Management of Data, 2002, pp. 428–439.

[36] J.S. Vitter, M. Wang, B.R. Iyer, Data cube approximation and histograms via wavelets, ACM Int. Conf. on Inf. and Knowl. Management, 1998, pp. 96–104.
