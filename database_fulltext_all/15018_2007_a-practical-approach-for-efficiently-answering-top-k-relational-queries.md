---
otero_id: 15018
otero_key: "UJPXZD2Z"
title: "A practical approach for efficiently answering top-k relational queries"
authors: "Anteneh Ayanso; Paulo B. Goes; Kumar Mehta"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.04.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A practical approach for efficiently answering top-k relational queries

Anteneh Ayanso <sup>a,1</sup>, Paulo B. Goes <sup>b,2</sup>, Kumar Mehta <sup>c,⁎</sup>

<sup>a</sup> Department of Finance, Operations and Information Systems, Brock University, 500 Glenridge Avenue, St. Catharines, ON, Canada L2S 3A1 <sup>b</sup> Department of Operations and Information Management, University of Connecticut, 2100 Hillside Road, U-1041IM, Storrs, CT 06269, USA <sup>c</sup> Decision Science and Management Information Systems, School of Management, George Mason University, 4400 University Drive MSN 5F4, Fairfax, VA 22030, USA

Received 21 September 2005; received in revised form 13 April 2007; accepted 29 April 2007 Available online 5 May 2007

## Abstract

An increasing number of application areas now rely on obtaining the “best matches” to a given query as opposed to exact matches sought by traditional transactions. This type of exploratory querying (also called top-k querying) can significantly improve the performance of web-based applications such as consumer reviews, price comparisons and recommendations for products/ services. Due to the lack of support for specialized indexes and/or data structures in relational database management systems (RDBMSs), recent research has focused on utilizing summary statistics (histograms) maintained by RDBMSs for translating the top-k request into a traditional range query. Because the RDBMS query engines are already optimized for execution of range queries, such approach has both practical as well as efficiency advantages. In this paper, we review the strengths and weaknesses of common histogram construction techniques with regard to their structural characteristics, accuracy in approximating the true distribution of the underlying data, and implications for top-k retrieval. We also present our top-k retrieval strategy (Query-Level Optimal Cost Strategy — QLOCS) and demonstrate its “histogram-independent” performance. Based on comparative experimental and statistical analyses with the best-known histogram-based strategy in the literature, we show that QLOCS is not only more efficient but also provides more consistent performance across commonly used histogram types in RDBMSs. © 2007 Elsevier B.V. All rights reserved.

Keywords: Similarity search; Top-k query; Uncertainty modeling; RDBMSs

## 1. Introduction

Databases are finding an ever-broader application for organized storage of both structured and unstructured data. Central to these applications are the required support for exploratory searches and the ability to retrieve “approximate matches”, or data that can be considered as “close” in relevance or similarity to the specified query. In a relational database context, this type of querying is commonly referred to as top-k querying or k-nearest neighbor (k-NN) querying, which involves retrieving the k closest records or “best matches” rather than only the exact matches of a query [4–7,9–14].

The nature of data in document and multi-media systems makes them ideal candidates for such retrieval methods and has been the focus of most research in the area (e.g., see Refs. [1,8,16,19,29]). An increasing number of application domains are now requiring use of similar exploratory searches over relational database management systems (RDBMSs). For example, in applications such as price comparison services and product recommender systems, it is desirable for users to be able to specify how many results they need and obtain a ranked set of results based on some values of interest on relevant attributes. Despite their direct relevance for such popular applications, top-k queries are not yet efficiently supported in RDBMSs [5,10]. Current implementations require the user to iteratively select value ranges on individual attributes in order to obtain relevant results. This approach is not only time-consuming and frustrating for the user, but also extremely inefficient for the system. Unlike this conventional querying, top-k querying allows users to specify target value(s) of attribute(s) that are of interest and a desired number (i.e., k) of results. The system then returns a ranked set of the desired number of records at and around the specified value(s).

In order to illustrate the conceptual difference between conventional querying and top-k querying, consider an exploratory search SQL query that is submitted based on the user selection of attribute ranges for an airline ticket for travel from New York to Dallas. A user looking for the cheapest ticket might specify the condition for which no results might appear (see the ranges defined by the dotted lines in Fig. 1(a) below).

Select Flight.Number

From Flight

Where Flight.Price <sup>b</sup>200 AND Flight.Time <sup>b</sup>12:00PM

The query returns no results, though there is a flight for which the fare is \$180 and leaves at 12:15 PM (see the data point represented by the little empty circle in Fig. 1 (a)). Having no knowledge about this flight, the user chooses to explore further by increasing the fare, which triggers the following query:

Select Flight.Number

From Flight

Where Flight.Price <sup>b</sup>250 AND Flight.Time <sup>b</sup>12:00 PM

The relaxed query (see the ranges defined by the solid lines in Fig. 1(a)) may return either too many results or too few; and subsequently the user may have to repeat this process a few more times. Note that had the user been able to pose a top-k query the first time (see the data point represented by the little shaded circle in Fig. 1(b)), the search would have been conducted at and around this specified point, and the user would have likely obtained the flight at 12:15 PM and paid only \$180.

As the above example illustrates, supporting top-k querying in RDBMS applications would not only potentially relieve the user from iteratively refining queries, but also reduce the computational load on the system from such repetitive querying. The challenge is, however, how to efficiently retrieve the “best matches” and at the same time, maintain practical simplicity in the operation of the RDBMS.

A conceptually straightforward approach to support top-k queries is to simply retrieve and sort all records from the database by specified criteria, and select the top k records. Obviously, this is not an efficient approach for today's dynamic databases that store millions of records. As an alternative to this naïve approach, earlier techniques in the literature [6,7] suggest use of specialized indexes for fast retrieval of top-k results. However, index-based algorithms and specialized data structures (see also Refs. [2,13,17,18,21,23]) are generally limited by the fact that they are not supported by any of the current RDBMSs. Without such specialized indexes and data structures, the RDBMS requires at least one full sequential scans of the database to support top-k queries [5,10].

![](/api/attachments/UJPXZD2Z/fulltext/images/e6c9b7717038141c55bbae32df244b3276e0a3fa504c755d77f564134b93a373.jpg)

![](/api/attachments/UJPXZD2Z/fulltext/images/196cc27b5f55627ef76b7571e11e56135dbcbefbc4f4482db430bd247225f94c.jpg)  
Fig. 1. Conventional querying (a) versus k-NN querying (b).

Recent approaches suggest use of summary statistics in the form of histograms [5,10,14] or sampling [11] to efficiently translate a top-k request into a “range query” that is normally executed by the RDBMS. A range query is one whose conditions are expressed as ranges of values (e.g., in the case of the above illustrative example, 50<sup>b</sup> prices<sup>b</sup>250 AND 11:30 am<sup>b</sup>time<sup>b</sup>12:30 pm). Histograms are commonly used statistical information in RDBMSs to summarize ranges of attribute values and their frequency of occurrence in the database. Their key advantage over other techniques of summarizing data is that they incur almost no run-time overhead [25]. Several methods of constructing histograms have been proposed in the literature (see Refs. [22,24–26]), and some of these histograms are adopted in many commercial RDBMSs. Major commercial database systems (e.g., Oracle, IBM DB2, Informix, Ingres, Microsoft SQL Server, and Sybase) adopt some of these histograms for summarizing the contents of relations [25,27]. These histograms are used by the systems' query optimization modules for estimating the result sizes of range queries and develop efficient execution plans. If top-k queries can be translated into equivalent range queries, such range queries can be easily posed using standard SQL and executed by the query engines in relational databases. In order to understand the practical appeal of this query translation approach using histogram information, it is important to highlight some potential advantages [5,10]:

▪ Significant efficiency can be obtained by avoiding the requirement of full sequential scans of the database to answer the query.

▪ Translation of the posed query into a traditional range query maintains the transparency in the operation for the RDBMSs and the ultimate optimization of query execution.

▪ The histograms already exist in RDBMSs because they are utilized for optimization of query processing. This eliminates the need for specialized data structures and separate execution mechanisms for the two different classes of queries (range and top-k).

The above advantages, however, come with some requirements in order for a histogram-based approach to be effective. First, because the corresponding range queries are estimated based on summary statistics maintained in histograms, the number of results to be retrieved can either fall short or be in excess of the desired k tuples [5,10].

Secondly, it is highly desirable that any proposed technique provides consistency in performance across different types of histograms commonly used in RDBMSs.

Histogram-based techniques [5,10] have shown significant cost savings over prior techniques [6,7], which require at least one full sequential scans of the database. However, their major limitation is the requirement of a rigorous offline calibration of the database using prespecified query loads to estimate a range query. In other words, the translation of a top-k query into a range query is based on an average parameter obtained from this calibration process. If estimated ranges are not optimal, the corresponding range queries return either fewer than k matches (leading to re-execution), or unnecessarily too many results beyond the required number (entailing additional efforts to rank order the results). Thus, this aggregate level range estimation often leads to inefficient performance for individual queries, especially for queries that are not well represented in a calibration set. In general, the existing histogram-based techniques fall short of systematically modeling the relevant cost trade-offs and optimally estimating the required range at an individual query level. This study contributes toward filling this gap by providing a cost-model that determines an optimal range that can be efficiently executed by the RDBMS query engine.

In this paper, we first analyze the strengths and weaknesses of common histogram construction techniques pertaining to their structural characteristics, accuracy in approximating the underlying data, and subsequent impact on top-k retrieval. Then we present our top-k retrieval strategy (QLOCS — Query-Level Optimal Cost Strategy) that incorporates histogram information as well as cost trade-offs involved in query execution. Based on comparative experimental and statistical analyses with the best-known histogram-based strategy, the Dynamic Workload Based Strategy [5] (for convenience, we call it DWBS), we show that QLOCS is not only more efficient, but also provides more consistent performance across commonly used histogram types in RDBMSs.

The remainder of this paper is organized as follows. Section 2 provides a brief review of the top-k retrieval problem over relational databases as described in the recent literature. Section 3 covers histogram construction and reviews commonly used histogram construction techniques and the relevant literature on histogrambased top-k retrieval. Section 4 presents our cost-based strategy, QLOCS and the mathematical description of its cost model. Section 5 discusses the experimental settings used in this paper, followed by the computational and statistical analyses. Section 6 discusses issues related to possible extensions of the proposed framework to a generalized setting. Finally, Section 7 provides some concluding remarks and future research directions.

## 2. Problem description

A traditional query is defined by conditions, usually in the form of value ranges of relevant attributes, with the objective of obtaining results that are included in the specified ranges. A top-k query is instead a point query, defined by target values of a set of attributes and a desired number $k ,$ with the objective of obtaining a ranked set of the k “closest” tuples at and around the query point $[ 4 , 5 , 1 0 - 1 2 , 1 4 ]$

Definition 1. Given a relation R of size T and n realvalued attributes $A _ { I } , . . . , A _ { n } ,$ a top-k query q on the relation R specifies target values of a set of attributes, $\left\{ A _ { I } = q _ { I } , \ . . . . . , A _ { n } { = } q _ { n } \right\}$ and a desired number of “best matches” according to some “ranking” or “distance” function.

A ranking or distance function is used to measure the “closeness” of each tuple t having attribute values $\{ t _ { I } , \ldots t _ { n } \}$ to the query point q and to determine an ordered set of the k results. The most commonly used distance functions in the literature are distance functions based on vector p-norms for $p { = } 1 , 2$ , and ∞ for Summation, Euclidean, and Maximum distance functions, respectively [5,11]:

Summation distance : $d _ { 1 } ( t , q ) = \sum _ { i = 1 } ^ { n } \left| t _ { i } - q _ { i } \right|$

Euclidean distance : $d _ { 2 } ( t , q ) = { \sqrt { \sum _ { i = 1 } ^ { n } \left[ t _ { i } - q _ { i } \right] ^ { 2 } } }$

Maximum distance : $d _ { \infty } ( t , q ) = \underset { i = 1 } { \overset { n } { \operatorname* { m a x } } } \left| t _ { i } - q _ { i } \right|$

Although most applications naturally involve all kinds of data such as numerical, categorical, or textual, this research primarily deals with metric-space and a notion of distance between a query point and database records involving numeric attributes. Moreover, the appropriateness of a given distance function as well as the ranking of tuples with respect to a given query specification may depend on a particular application and the interpretation of the individual attributes involved. For application environments where users are aware of the implications of the different distance functions, the system should be flexible enough and allow the user to have a choice of distance functions. Otherwise, systems should be able to support a default function that is appropriate for a particular application.

Therefore, given a set of N points and a query point q in an n-dimensional space, the top-k problem is to determine the set of the k nearest neighbor tuples, denoted by NN(k), whose distances from q are minimum based on a given distance function.

Definition 2. Given a relation R and a top-k query q in an n-dimensional space, the kNN problem is to determine the set NN(k) of k nearest neighbor tuples in R such that:

$$
\begin{array}{l} \forall t \in N N (k) \\ \forall t ^ {\prime} \in R - N N (k) \\ d (t, q) \leq d (t ^ {\prime}, q) \end{array}
$$

In what follows, we discuss histograms and their use in RDBMSs and review the relevant literature on the histogram-based range estimation, which is the basis for our strategy, QLOCS.

## 3. Histograms in RDBMSs

The representation of data in the form of summary statistics on an attribute or a set of attributes is one of the basic components of the RDBMS. The fundamental assumption in using histograms as representation of staistics is the partitioning of data sets into buckets containing close-to-uniform distribution of tuples. The intuition behind this assumption is the fact that such grouping of the data minimizes the expected errors in estimating the cardinality of query plans during optimization.

Definition 3. Given a real-valued attribute X in a relation R and the domain D of X, a histogram on attribute X uses a partitioning rule and partitions the data distribution into B mutually disjoint buckets (or bins) and approximates the corresponding frequencies.

## 3.1. Histogram construction technique

Commonly adopted histogram construction techniques, which we review below, include equi-count (equidepth), equi-width, and MaxDiff histograms:

## (i) Equi-count

In the equi-count histogram, also called equi-depth, contiguous ranges of attribute values are grouped into buckets enclosing approximately equal number of tuples [22,24]. It is the most commonly used histogram construction technique in most commercial RDBMSs. For example, IBM DB2, Informix, and Oracle all use one-dimensional equi-count histogram [27]. The basic limitation of the equicount histogram is that it considers only the frequency information of attribute values and ignores the variability of frequency information within individual buckets. This may lead to inaccurate approximation of the distribution of attribute values within individual buckets, particularly for data sets that exhibit clusters around specific values (e.g., the distribution of the income data set)

## (ii) Equi-width

In the equi-width histogram construction, the data domain is grouped into buckets of equal length. In other words, individual buckets have approximately the same width (area or volume), but variable frequencies. This method is another commonly used histogram construction method in practice. For example, Microsoft SQL Server uses one-dimensional equi-width histogram, with adjacent buckets having similar distributions being combined to compress the histogram [27]. This method shares the same drawback as the equi-count method as it creates buckets without considering the variability of frequency information within individual buckets. As a result, it may lead to inaccurate approximation of the distribution of attribute values for sparse data cases.

## (iii) MaxDiff

The MaxDiff method is a relatively newer type of histogram introduced in the literature (e.g., see Refs. [25,26]). Constructing the MaxDiff histogram involves sorting the data values and calculating the frequency of occurrence for each distinct attribute value. Given the desired number of buckets, the bucket boundaries are placed at those attribute values that correspond to the highest frequency gap between two consecutive values. Implicit in this technique is the fact that by avoiding the grouping of dissimilar frequencies, deviations from the uniform frequency assumption in approximating the distribution of attribute values is minimized. This is an important feature that distinguishes it from the other two histogram techniques. Although the MaxDiff technique could form some poorly partitioned buckets depending on the distribution of the data, the partitioning rule takes into account the variability of frequencies within histogram buckets. Based on the one-dimensional partitioning rule, several multi-dimensional versions (e.g., AVI, PHASED, M-HIST) were proposed in the literature. These versions essentially differ in the way they create buckets at each step where the one-dimensional projection of the data set for one of the attributes is considered (see Refs. [25,26] for details of these methods).

The advantages and disadvantages of these histograms underscore the point that there is no “universally optimal” or “universally good-quality” histogram, and as such, commercial database systems currently use one or the other of the above histograms. This requires the flexibility and consistent performance of any optimization technique that relies on the statistics that are maintained in histograms, which can be of different type in different RDBMSs.

In order to provide insight regarding variations in histogram structures in attaining the fundamental Uniform distribution assumption, we plot the density (frequency/ length) of 100 histogram bins created using the above three histogram construction techniques for one of the data sets used in our experiment (the census data set [3]). As can be seen in Fig. 2a below, the equi-count technique, while it maintains approximately equal frequencies within the bins, it may result in some bins with very narrow length and some with very wide length, leading to differences in density across the bins. Similarly, the equiwidth technique may result in some bins with very high frequency and some with very low frequency. Note that many of the records for the equi-width histogram are included in the first few bins out of the 100 bins used in creating the histogram. On the other hand, the bins created using the MaxDiff histogram show varying density for adjacent bins. This is because MaxDiff places bucket boundaries at consecutive values with higher frequency gaps. While consecutive bins have varying density, the overall distribution is relatively more dispersed throughout the bins for the MaxDiff histogram.

In order to further show the degree to which each histogram technique can achieve uniform distribution of tuples within individual bins, we adopted a onedimensional version of the box-counting procedure [4,15] for measuring the goodness-of-fit (gof) to the Uniform distribution. The length of each bin is partitioned into small lengths in accordance with the number of actual counts within the bin. The gof (0<sup>b</sup>gof≤1) of a bin is then represented by the ratio of the number of slices containing at least one tuple to the total number of slices (or counts) per bin. Fig. 2(b) shows this information by histogram technique for the 100 bins created using the census data set. Note that the MaxDiff technique relatively achieves the uniform distribution of tuples better than the equicount and equi-width histograms.

The above plots show that depending on the distribution of the underlying data in the database as well as the particular partitioning strategy to be used, histogram construction techniques can actually vary in achieving the Uniform distribution or being close to it. In other words, every histogram is characterized by some structures based on the possible ways it partitions the data distribution.

![](/api/attachments/UJPXZD2Z/fulltext/images/3d9e66dc3dd589f2f6cfd11e55c9511b400e08a6c8d75be63eb65ed3766400cc.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/a6d149c6f6b2621d019de4cd135361478b1b8ba61a03fb3aee39e269ec68309a.jpg)  
Fig. 2. Histogram bin densities (a) and conformance to Uniform distribution (b).

Such structural characteristics can have both good and bad performance implications for top-k retrieval techniques. Identifying these implications and analyzing the degree to which a given top-k retrieval technique balances the good and bad sides is one way of evaluating the necessary qualities or requirements of a good technique. Thus, among other things, the qualities of a good histogrambased technique should include its consistency of performance across different types of histograms and its capability to leverage the quality of the information captured. Moreover, independent of the specific type of histogram, another desirable quality of a good technique is its robustness in providing results that can be also improved with an improvement in the quality of the information captured by the histogram.

If a technique draws strength primarily from the structural characteristics of a specific type of histogram, its generalizability can be greatly compromised. For example, the DWBS shows significantly better performance with the equi-count histogram, compared to the MHist histogram, which uses MaxDiff as the underlying one-dimensional partitioning technique [5]. Based on the comparison of the main characteristics of the above three histogram techniques, we have discussed that the MaxDiff technique approximates the distribution of attribute values better because of its consideration of the variability of frequency information within individual buckets. An important question to raise is whether or not the better performance obtained using the equi-count histogram is the result of better approximation of attribute values or because of the bound on the frequency size or equal counts kept within a bin, or may be a lack of consistency in the performance of the underlying top-k retrieval technique.

## 3.2. Histogram-based range estimation

Histogram-based range estimation techniques [5,10] are based on the argument that a top-k query is better supported by an execution method that transforms it into a conventional range query. Because RDBMS query engines are already optimized for execution of range queries, the idea is to take advantage of the existing query optimization techniques and provide a mechanism to translate a top-k query into an appropriate range query. The translation of top-k queries into range queries can be conducted by using a middle layer between the application and the querying engine, thereby maintaining transparency for both classes of queries — range and topk queries. Therefore, the goal is to utilize as many of the components within the RDBMS (e.g., histograms, query language, and available index utilities) to estimate and execute an equivalent range query that would provide the required top-k results.

The DWBS [5], which we use in this paper as a benchmark technique, is a generalization of prior histogram-based strategies [10] that identify two relevant distance ranges (restart and no-restart ranges) for translating a top-k query into a range query. The restart range is a range that may fall short of the desired number of results and require re-execution to obtain the remaining tuples. On the other hand, the no-restart range is a range that guarantees the desired number of tuples, but it may potentially return too many tuples.

Using a pre-specified workload of queries for each k value of interest, the DWBS first calibrates an aggregate parameter α such that the search distance $d ( \alpha ^ { * } )$ minimizes the average number of tuples retrieved from the database (i.e., given $d _ { 1 }$ and $d _ { 2 }$ as the restart and no-restart distances, respectively, the cut-off distance is determined by the equation: $d ( \alpha ) = d _ { 1 } + \alpha ( d _ { 2 } - d _ { 1 } ) , 0 \leq \alpha \leq 1 )$ . Thus, for each future query requesting the same k value, the parameter $\alpha ^ { * }$ will be used to determine the cut-off distance within the bounds defined by the query's restart and no-restart ranges. In the event that less than k results are retrieved using this cut-off distance, the no-restart distance is used to guarantee retrieval of the k results during re-execution (see our illustrative example for the restart and no-restart strategies and the DWBS in Appendix A).

The DWBS has shown that utilizing the summary statistics in histograms avoid the requirement of a full sequential scans of the database and significantly reduce the computational time required to support top-k queries [5]. Thus, providing a mechanism to translate a top-k request into a corresponding range query has both practical as well as efficiency advantages. What remains to be addressed is the accurate estimation of the range using only summary statistics (histograms) about the underlying data in the system. For any given top-k request, if the corresponding range query is not optimally estimated, it is prone to returning either fewer or greater than the desired number of results. For example, if the range is underestimated, it requires re-execution to obtain the remaining results, leading to increased cost of accessing the database. On the other hand, if this range is overestimated, it returns excess results that require extra operation to rank order the top-k matches.

## 4. Proposed strategy — QLOCS

Our strategy — QLOCS draws upon the idea of query translation and the motivation in the efficiency gain from leveraging existing histograms, available query language and index structures about the data in the RDBMS. QLOCS is, however, a precautionary strategy based on a cost model that incorporates histogram information as well as cost trade-offs related to possible restarts as well as excess results in executing a single query. It has the following distinct features that specifically allow its performance to stay independent of histogram construction method:

a) The cost-optimal range query is determined for each top-k query, rather than for a pre-specified workload of queries.

b) It accounts for the number of tuples available between the restart and no-restart ranges for each query. This further allows QLOCS to:

i) stay independent of variation in bin sizes within a given histogram rather than average out the effect at the aggregate level.

ii) inherently adjust the estimated distance for increased excess in case of larger bins, as it accounts for the probability of a restart and the associated penalty. More specifically, once data uniformity within a bin has been achieved, performance improvements through further decreasing the size of the histogram bin would be negligible.

## 4.1. Cost model

The cost model of QLOCS is based on the two relevant (distance) ranges: (1) a lower bound or restart distance that may return insufficient tuples; (2) an upper bound or norestart distance that guarantees sufficient tuples, i.e., at least the number of tuples requested or k. For each top-k query, QLOCS identifies these bounds and the available number of tuples between these bounds using a distance function and the histogram maintained by the RDBMS about the value distribution of the data. As stated above, if an arbitrary cut-off distance between these bounds is used to construct a range query, there will be two possible consequences in meeting the requirement of the top-k request. One possibility is that the range used may lead to fewer than k results, leading to a re-processing effort to obtain the remaining results. The other possibility is that the range used may provide results far in excess of the required number, requiring additional operation to rank order the results. Both these scenarios involve processing costs that are quantified in the proposed model in light of the required operations of the RDBMS. The ideal range is one that lies somewhere in between and the cost-optimal range reflects the cost trade-offs between the two scenarios. QLOCS determines this cost-optimal range by minimizing the sum of the expected costs of re-processing and the expected costs of handling results in excess of the required number.

Consider Fig. 3 below, which represents the tuple distribution over distance intervals. Let $d _ { 1 }$ and $d _ { 2 }$ represent the lower and upper bound distances, respectively. Assume that there are N tuples available between the lower and upper bounds based on the histogram information. Thus, the lower bound distance $d _ { 1 }$ returns $k _ { 1 }$ results (where $k _ { 1 } < k )$ . The upper bound distance $d _ { 2 }$ guarantees k tuples, but may retrieve results in excess of the desired number (i.e., $k _ { 1 } + N \ge k )$ . Therefore, the distance that will provide for the additional $k _ { p }$ tuples (where $k _ { p } = k - k _ { 1 } ; ~ k _ { p } > 0 )$ is in the range $[ d _ { 1 } , d _ { 2 } ] _ { \cdot }$ , and needs to be optimally estimated.

![](/api/attachments/UJPXZD2Z/fulltext/images/9ca544648b19785cb2516aeb2b2f196dc1d9fdc91a2d98be5f5e375dcafb7fb7.jpg)  
Fig. 3. Number of tuples over distance intervals.

As a generalization, the range $[ d _ { 1 } , d _ { 2 } ]$ is mapped into the continuous interval [0, 1] such that the optimal distance is denoted by $d ^ { * }$ , where $d ^ { * } \in [ 0 , \ 1 ]$ . Let the function f(t) describes the probability density function for the distribution of tuples over the interval [0, 1]. Hence, the probability that a randomly chosen tuple will be within a given distance d is given by:

$$
p = \int_ {0} ^ {d} f (t) d t\tag{1}
$$

As pointed out earlier, the fundamental assumption in using histograms as representation of statistics is the partitioning of data sets into buckets containing closeto-uniform distribution of tuples. Assuming the Uniform probability density function, Eq. (1) can be written as:

$$
p = d\tag{2}
$$

Considering the probability p as the success rate of a Bernoulli trial, the probability of retrieving a given number of tuples j at distance $d ,$ where the interval [0, 1] contains N tuples, follows the Binomial distribution. Thus, for a binomial random variable X, the probability of obtaining exactly j tuples is given by:

$$
P (X = j) = \binom {N} {j} d ^ {j} (1 - d) ^ {N - j},\tag{3}
$$

where $j = 0 , 1 , . . . N .$

A restart operation is required if fewer than k tuples are obtained within any distance $d ,$ and this probability is estimated by Eq. (4) below:

$$
P (r e s t a r t) = \sum_ {j = 0} ^ {k _ {p} - 1} \binom {N} {j} d ^ {j} (1 - d) ^ {N - j}\tag{4}
$$

Using Eq. (4) above, the expected cost of a restart operation is formulated as:

$$
C (r e s t a r t) = \delta \cdot \sum_ {j = 0} ^ {k _ {p} - 1} \binom {N} {j} d ^ {j} (1 - d) ^ {N - j}\tag{5}
$$

where δ represents the cost of re-executing the query in case of a restart.

Depending on the type of index utilities available in a given system, there is typically more than one way to retrieve tuples from the database. For example, the most selective access path could be through a B+ tree index, or a hash index, or a binary search with available sort order. In the absence of all these utilities, the worst-case scenario would be a file scan.

Definition 4. The expected cost of a restart operation is the cost of re-executing the query if the original range query fails to retrieve the required number of tuples.

The other key component in the cost model captures the extra effort in sorting results in excess of the required number. This cost component is formulated based on an operation central to sorting algorithms that are commonly used in commercial RDBMSs. To do so, we first project an expected number of results at distance d in the interval [0, 1]. Using Eq. (2) above, if N tuples are available in the range [0, 1], the expected number of tuples in the range [0, d] is given by:

$$
E [ X ] = d N\tag{6}
$$

Hence, the additional cost incurred in sorting with the excess results is given by:

$$
C (e x c e s s) = \left\{ \begin{array}{l} (k + d N - k _ {p}) \log_ {2} (k + d N - k _ {p}) - k \log_ {2} k, \text {   if   } \frac {k _ {p}}{N} <   d \leq 1 \\ 0 \end{array} , \text { elsewhere } \right.\tag{7}
$$

Definition 5. The cost of excess is the additional cost in sorting with the results retrieved in excess of the required k tuples within any distance d.

The total cost of executing a given query with estimated distance d is given by Eq. (8) below, which is the sum of Eq. (5) and Eq. (7).

$$
T C (d) = \left\{ \begin{array}{l} \delta \cdot \sum_ {j = 0} ^ {k _ {p} - 1} \binom {N} {j} d ^ {j} (1 - d) ^ {N - j} + (k + d N - k _ {p}) \log_ {2} (k + d N - k _ {p}) \\ - k \log_ {2} k, \text {   if   } \frac {k _ {p}}{N} <   d \leq 1 \\ \delta \cdot \sum_ {j = 1} ^ {k _ {p} - 1} \binom {N} {j} d ^ {j} (1 - d) ^ {N - j}, \quad \text { elsewhere } \end{array} \right. \tag {8}
$$

Due to the decreasing probability of restart as d increases, the cost of a restart is a decreasing function with d for the range $0 \leq d \leq k _ { p } / N .$ Thus, the optimal distance $d ^ { * }$ is determined by setting the conditions $T C ^ { \prime }$ $( d ^ { * } ) { = } 0$ and $T C ^ { \prime \prime } ( d ^ { * } ) { > } 0$ in the range $k _ { p } / N { < } d \leq 1$ . The functions $T C ^ { \prime } ( d )$ and $T C ^ { \prime \prime } ( d )$ are given by Eq. (9) and Eq. (10), respectively:

$$
\begin{array}{l} T C ^ {\prime} (d) = \frac {N}{\ln (2)} [ 1 + \ln (k + d N - k _ {p}) ] \\ \quad - \delta k _ {p} \binom {N} {k _ {p}} d ^ {(k _ {p} - 1)} (1 - d) ^ {(N - k _ {p})} \end{array}\tag{9}
$$

$$
\begin{array}{l} T C ^ {\prime \prime} (d) = \frac {N ^ {2}}{(k + d N - k _ {p}) \ln (2)} \\ \qquad - k _ {p} \binom {N} {k _ {p}} \delta (1 - d) ^ {N - k _ {p} - 1} d ^ {k _ {p} - 2} \\ \qquad \times (k _ {p} + d - d N - 1) \end{array}\tag{10}
$$

A straightforward closed-form solution was not possible to obtain. As a result, $d ^ { * }$ is computed using the successive approximation method,<sup>3</sup> where Eq. (11) below is the approximation function for computing real solution of the equation, $T C ^ { \prime } ( d ) { = } 0$ . An illustrative example for the solution obtained using this method is provided in Appendix B.

$$
d ^ {*} \sim d - \frac {T C ^ {\prime} (d)}{T C ^ {\prime \prime} (d)}\tag{11}
$$

## 5. Experimental setting

As we emphasized before, in any histogram construction technique, histogram buckets are created with the objective of maintaining uniformity in the frequencies and the spread of the data values within individual buckets. Given this ideal condition or as histograms approach this ideal condition, an efficient technique for top-k retrieval is expected to estimate the range query reasonably well and reveal a robust performance regardless of the underlying histogram construction technique. In other words, given this condition, any performance inefficiency in top-k retrieval should be attributable to the underlying technique itself. Therefore, the main objective of the experiments in this paper is to demonstrate “histogramindependent” performance of QLOCS, and compare this property against the benchmark technique, the DWBS. To this end, our experimental setting is designed as follows.

## 5.1. Histograms

Our experiments involve the one-dimensional equicount, MaxDiff, and equi-width histogram techniques. The histograms are constructed by varying the number of histogram bins (i.e., for a given number of bins) in order to approach the Uniform distribution of tuples in histogram buckets as the number of histogram bins increases.

The performances of the two strategies (i.e., QLOCS and DWBS) are then analyzed by histogram type and the number of bins allocated for each.

## 5.2. Data sets

Two different data sets, real and synthetic, are used for the experiments. The real data are the income data of a fragment of the US Census Bureau data [3,28]. This data set has about 210K records with a data domain of (−25,897 to 347,998). The second data set is a synthetic data (array data) generated from a Zipfian distribution. This data set has 500K records with values in the range of (0 to 10,000).

## 5.3. Performance metrics

The major difference between QLOCS and prior histogram-based strategies is on the “tightness” or “optimality” of the range that is determined and used in translating a top-k query into the corresponding range query. As mentioned earlier, the histogram-based strategies [5,10] have shown significant savings in terms of execution time, in comparison with traditional approaches [6,7], which require at least one full sequential scans of the relation to support top-k queries. Given any RDBMS setting in terms of access paths or available index utilities to execute the translated range query, the “tighter” the range is, the more efficient the execution of the query will be. If better indexes and utilities are incorporated in the RDBMS (unless these indexes support top-k query by design), they will be equally important for QLOCS and DWBS, and potentially reduce the execution time in both strategies. In other words, given that our work is an extension of the histogram-based strategies [5,10], the main focus of our experiments is not on the execution time of queries, rather on the efficiency metrics that are directly related to the optimality of the estimated range. Because QLOCS presents the case for the cost-optimal range estimation procedure, our efficiency metrics emphasize the total cost and its key components, namely, the magnitude of excess results and the percentage of restarts. In particular, the following metrics are used for the performance analyses of QLOCS and its comparison with the DWBS.

(i) Excess: The excess metric is one of the cost factors explicitly formulated in our cost model. It is measured as number of results retrieved relative to the size of k. In case of restarts, excess is measured based on the number of results obtained using the guaranteed norestart range. This metric can be related to the metric — Percentage of database retrieved, which was used in previous histogram-based techniques [5,10] to measure the number of tuples retrieved as a percentage of the database size. While both the metrics excess and the percentage of database retrieved generally measure the size of results returned for a given query, the excess metric is a more relevant measure of result size that can be directly contrasted to the size of results requested.

(ii) Percentage of restarts: As used in prior research, this metric is measured as the percentage of queries that lead to restarts from a set of experimental queries (i.e., percentage of queries that fail to retrieve k tuples in the first execution).

(iii) Total Cost: One of the strengths of QLOCS is its ability to capture the trade-offs between the cost of a restart with the cost of excess. As a result, the total cost, defined in Eq. (8) as the sum of the restart cost and the excess cost, is used to evaluate and compare the overall performance of the two techniques. Due to the difficulty in generalizing the cost of the restart operation under different RDBMS settings, the restart cost component (i.e., δ) in our experiments is evaluated using the cardinality of the database T as a proxy to the worst-case scenario in case of a restart. If a range query constructed using the estimated distance from each technique requires re-execution, we apply this restart cost. Similarly, the excess cost component is evaluated based on the actual number of results obtained by a range query, which is constructed by using the estimated range from each technique or using the no-restart range if a restart occurs.

## 5.4. Experimental results

The experimental results are reported by data set. For the census data set, which has about 210K records, the number of bins used for each histogram type is varied from 100 bins to 2000 bins. In presenting the results, the bin sizes of 200, 800, and 2000 are selected to represent low, moderate, and high histogram sizes. In order to execute both strategies, 500 queries are generated uniformly over the data domain. Additional 50 queries are similarly generated for the calibration step in the DWBS. The average performance in terms of excess, percentage of restarts, and the total cost are computed for k values ranging from 5 to 1000 results. Along with the average performance, the variability of performance in terms of standard deviation is also reported for both strategies. Since the array data is more close to the Uniform distribution, analyzing the performance using these data is another way to test whether the improved fit with the Uniform distribution leads to improved performance for both strategies. Histogram sizes for the array database are doubled to reflect its size, which is twice that of the census database. Similar analysis is then conducted for the performance of both strategies in terms of the excess, the percentage of restarts, and the total cost.

## 5.4.1. Performance analysis with the census data set

Fig. 4(a) below shows the average excess for queries successfully executed without restart using the three histogram techniques, for QLOCS on the left side and DWBS on the right side. The results of QLOCS in terms of the average excess (Fig. 4(a)) are consistently low and almost indistinguishable by histogram type for all k sizes. Similarly, as Fig. 4(b) shows, there is no noticeable difference (except for minor variations for smaller k values) for the standard deviation of excess by histogram type for QLOCS.

The performance of DWBS, however, varies significantly across the histogram techniques. For the DWBS, the equi-width histogram shows the worst performance (with higher average excess for smaller k values). For less number of bins, the MaxDiff is worse than the equi-count and this difference somewhat disappears as the number of bins increases to 800. In particular, as the number of histogram bins decreases, the differences in performance by histogram type are noticeable for the DWBS. Although the performance slightly improved when the number of bins increases from 200 bins to 800 bins, there is no convergence in performance when the number of bins increases from 800 bins to 2000 bins.

(a)  
![](/api/attachments/UJPXZD2Z/fulltext/images/ec56a01842796bd40dc3156925d0d07a14d9f05723d3059a13d8498a67287213.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/39d45ed0b0eaed6ca2478edc43f088537e9412bc8da591a3ac904b878e203bc3.jpg)  
Fig. 4. (a) Average excess and (b) St. Dev. of excess for queries executed without restart.

The variation in performance by histogram type as well as size is even more signified for the standard deviation of excess for DWBS (see Fig. 4(b)). The equi-width histogram shows the worst performance in terms of the standard deviation as well. This performance persisted despite an increase in the number of bins to 2000. For the MaxDiff and the equi-count histograms, a pattern similar to the average excess is observed, although MaxDiff looks worse for less number of bins and the variation eventually converges as the number of bins increases.

Fig. 5(a) and (b) below shows the analysis of performance in terms of the percentage of restarts and its standard deviation, respectively. As Fig. 5(a) shows, the percentage of queries requiring restarts is much lower and relatively consistent across the histogram techniques as well as the histogram sizes for QLOCS. Compared to the average excess, however, there exist some degree of variation by histogram technique. Note for instance, the equi-width histogram has slightly higher percentage of restarts than the MaxDiff and equi-count for all k values.

(a)  
![](/api/attachments/UJPXZD2Z/fulltext/images/bb2637fe31f375132257b177d8a1cdcc3be815a7db0b6631d2e5b0c4b9b2879c.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/01896af2f1be0aa390fdf8abfac044a2ee605753056a5684c24bfcafb680d297.jpg)  
Fig. 5. (a) Percentage of restarts and (b) St. Dev. of percentage of restarts.

Number of results requested, k

As the number of bins increases, equi-width shows higher percentage of restarts, and the other two seem to converge, especially for larger k values. In terms of the standard deviation (Fig. 5(b)), the numbers are slightly higher, but the general pattern is the same as that of the percentage of restarts. In general, the degree of inconsistency observed in terms of the percentage of restarts and its standard deviation, are relatively much lower for QLOCS, compared to the results for DWBS.

For DWBS, significant variation is observed by histogram technique in the percentage of queries requiring restart. Note that none of the histogram techniques is consistently better or worse for all k values. In fact, as the number of bins increases, the percentage of restarts becomes worse for the DWBS. This implies that the DWBS is unable to take advantage of the uniformly distributed data available from smaller bin sizes. QLOCS leverages the distribution information within histogram buckets better over a reasonably wide range of histogram bin sizes and it shows improved performance with an improved fit to Uniform distribution from smaller bins.

Since our strategy is driven by the total cost of executing queries, examining performance only on the individual metrics may not give a complete picture on the overall efficiency of QLOCS. Therefore, in addition to the performance analysis with the above individual metrics, the total cost of executing the queries and its variability are examined. This information is reported in Fig. 6 below for both strategies.

A key observation on the average total cost is that QLOCS has generally flat total cost across the number of results requested. This is in contrast to the increasing cost pattern for the DWBS. For QLOCS, as the number of bins increases, a more consistent pattern is revealed, with cost differences becoming smaller for smaller k values. The equi-width histogram shows slightly higher total cost for all k values, followed by equi-count for most of the k values on the lower end. In general, the differences in the standard deviation are much lower than the differences noticed for the average total cost.

For the DWBS, the average total cost and the standard deviation reveal no clear pattern by histogram technique. As can be seen from Fig. 6(a) and (b) for DWBS, no one histogram technique is consistently better or worse for all histogram sizes as well as k values.

## 5.4.2. Performance analysis with the array data set

The results for the array data sets look substantially different. The results of QLOCS, in terms of both the average excess (Fig. 7(a)) and the standard deviation (Fig. 7(b)) completely converge for the three histogram techniques. There is a very high degree of consistency across the histogram sizes for each histogram technique. This is intuitive as histogram size should not play a significant role for data sets, which are close to Uniform distribution. Since the main purpose of histograms is to maintain uniformity by partitioning the data, granularity should not have a significant performance effect for such data sets. Despite this, convergence of performance for the DWBS occurs only for bin sizes of 4000 bins for the average excess and 1600 bins for the standard deviation.

![](/api/attachments/UJPXZD2Z/fulltext/images/d29e4ecd68ced398cbf685677fbda6ddaf8b09d8fd926204ef4f4ed373c9a733.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/3f15dc4a463c4389ae16fd28d76208f59524d371f5b66c4dd71fe4a39d658641.jpg)  
Fig. 6. (a) Average total cost and (b) St. Dev. of total cost.

(a)  
![](/api/attachments/UJPXZD2Z/fulltext/images/1fe8623aa2103af5fdf788bd7833fc7456cf1bb2beccbbb52ddb984539f1a5e6.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/615d6ebd70819855310eb26ea2d0c63baac649ca87af66b6df26c7e32ec5b6c9.jpg)  
Fig. 7. (a) Average excess and (b) St. Dev. of excess.

The percentage of queries requiring restarts (Fig. 8(a)) and its standard deviation (Fig. 8(b)) improved in terms of magnitude as well as consistency for QLOCS. A pattern close to convergence is seen over most of the k values on the lower end and with an increase in histogram sizes to 1600 bins and 4000 bins. For higher k values, the equi-width histogram shows a slightly higher percentage of restarts, which is also reflected in the standard deviation.

Despite an improved fit to the Uniform distribution for the array data, the results of DWBS in terms of the percentage of restarts (Fig. 8(a)) and the standard deviation (Fig. 8(b)) show no noticeable improvement. However, some patterns are now revealed by histogram type. The equi-width histogram consistently shows the worst performance, followed by MaxDiff, and equi-count. The performance deterioration with an increase in number of bins (smaller bin sizes) is also seen for the array data. The comparison of the results for the histogram size of 400 bins versus 4000 bins clearly shows this observation.

Finally, Fig. 9 below summarizes the average total cost and its standard deviation for the array data set. The average total cost for QLOCS is generally lower and relatively flat (see Fig. 9(a)). Similar to the census data set, the differences in costs by histogram technique become smaller with an increase in bin size, particularly for smaller k values. For DWBS, the equi-width histogram reveals the worst performance, followed by MaxDiff, especially for the histograms with fewer number of bins. On the other hand, no significant variation by histogram type and size is seen for the standard deviation of total cost for both strategies (see Fig. 9(b)).

## 5.5. Statistical analysis

Two levels of statistical analyses were conducted to further validate the performance assessment. First, single factor ANOVA results were used to analyze the effect of histogram types on the individual metrics. Second, a more detailed analysis was conducted using General Linear Model (GLM) to examine the effects of histogram type, bin sizes, and k sizes.

Side by side comparison of single factor ANOVA results for the census and array data sets are shown in Tables 2 and 3, respectively (see Appendix C). From Table 2 (census data), it is clear that while there is no significant

(a)  
![](/api/attachments/UJPXZD2Z/fulltext/images/e8914554e156c140552fb1e96e11859fe853eac04387ffe80ef1bffe2ffe3138.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/47d0667b649b1103303eb78b7f2341f5a39e33937574ce40f1e26c2cb8264dd4.jpg)  
Fig. 8. (a) Percentage of restarts and (b) St. Dev. of percentage of restarts.

difference in excess between histogram types for QLOCS, DWBS does show significant differences in performance across different histogram types. Although the individual tests for the percentage of restarts and the total cost are not supported for QLOCS, the same results show significantly better performance for the MaxDiff histogram due to its ability to take into account the variability of frequencies within histogram buckets. As the results show, this is not the case for the DWBS. The results from the array data set (Table 3) provide further evidence of differences in performance for the two approaches. Since array data set is close to uniform in its distribution, both algorithms show no significant difference in excess across histogram types. However, interestingly enough DWBS shows significant variation in performance in terms of percentage restarts and total cost with the change in histogram type.

(a)  
![](/api/attachments/UJPXZD2Z/fulltext/images/813c6fece72053a540f5533d7af1f4311248fd1b9bb4810628762258c38fe1ca.jpg)

(b)  
![](/api/attachments/UJPXZD2Z/fulltext/images/2c96c344da3c5983e68799a4a8d0ab6b6770eeede7b43f888d43cf19ea935336.jpg)  
Fig. 9. (a) Average total cost and (b) St. Dev. of total cost.

The more detailed analyses using GLM are presented in Tables 4 and 5. The results are shown for the excess and total cost metrics for queries that are successfully executed without restart. Considering the inclusion of additional factors and the factor levels, it provides for insights into additional sources of variation in performance. For the census data set (Table $^ { 4 ) }$ , the magnitude of variation, as indicated by the coefficient values for excess and total cost, is significantly smaller than that for DWBS. Notably, the difference in performance of QLOCS over DWBS is observable by significantly smaller coefficients for histogram size. This is indicative of much higher volatility in performance of DWBS by histogram type. Finally, the smaller coefficients for k-values further reinforce the relatively more robust performance of QLOCS over DWBS. For the array data, the GLM results (Table 5) reiterate the observations from single factor ANOVA results for QLOCS. However, the control of other factors reveals that DWBS performance is significantly worse for the MaxDiff histogram over the other two. In terms of the excess, the significant coefficients for histogram size for the DWBS reinforce our earlier observation that it is unable to leverage the improved fit to uniformity as the histogram size increases. Though both approaches show similar sensitivity to k-values, for QLOCS, the insignificant coefficients for histogram type and histogram size are further evidence of its ability to handle structural variation in histogram types. For total cost, the relatively smaller coefficients for histogram sizes and k-values show relatively more robust performance of QLOCS over DWBS for the array data set as well.

## 6. Extension to multi-dimensional setting

In this section, we discuss issues related to extending our framework to the multi-dimensional setting. This is particularly related to two major components of the proposed strategy, namely, histograms and distance functions. As mentioned before, the major difference in the various types of histogram construction techniques lies in the underlying one-dimensional data partitioning strategy. In other words, the multi-dimensional versions of the histograms commonly adopted in commercial database systems as well as the ones proposed in the literature are extensions of the basic one-dimensional partitioning strategy with some common assumptions on combining multiple attributes. For example, most commercial RDBMSs keep one-dimensional histograms and assume the attribute value independence assumption for multiattribute tasks [27]. On the other hand, most of the multidimensional histogram structures proposed in the literature are derived from the underlying one-dimensional partitioning technique with the assumption of joint distributions for multiple attributes (e.g., [22,24–26]). Therefore, as far as histograms are concerned, the multidimensional environment brings the following factors to the strategy we are proposing.

First, the consideration of multiple dimensions changes how the search space should be viewed in multi-dimensional histogram buckets. For instance, for a given distance from a query point to the edge of any given histogram bucket, there can exist other buckets whose area/volume is either fully or partially included within this distance. This affects the approach that can be taken in defining the search bound or the restart and no-restart points for any given query point. We have seen two different implementations in the literature (for example, see Refs. [4,5,10]). One approach considers buckets as atomic and uses an ordering of optimistic and pessimistic distances from the query point to the edges of each bucket to define the search bound for the query point [5,10]. Another approach involves the computation of the volume overlap of buckets that share a given distance from a query point as well as the estimation of a data skew parameter to adjust for the number of tuples that are expected to be included within a given distance [4]. These alternative approaches may have different implications on the performance of a given top-k retrieval strategy and this requires further research.

The distribution of tuples within histogram buckets also becomes a significant factor in the multi-dimensional setting. For example, the optimal distance in our model is based on the assumption that the distribution of tuples within histogram buckets is Uniform. Accordingly, the success probability $p$ is represented by the distance point $d ,$ where $0 \leq d \leq 1$ . When data skew is present, this relationship may not hold, affecting the estimation of the expected number of tuples within the search interval. If the actual distribution of the tuples within each bucket is known (which is not usually the case), this could be easily handled by our general definition of the success probability by incorporating the known density function. Unfortunately, real-life data may have any pattern and this issue needs to be addressed without significantly changing the conceptual framework. Prior research suggests the use of an error metric or deflation parameter that can be stored for each histogram or for each histogram bucket at the time of histogram construction. For example, Ref. [14] suggests the use of an error parameter associated with each histogram for modeling histogram quality. Ref. [4], on the other hand, suggests the use of a deflation parameter for each histogram bucket to capture the local degree of skew of the data inside the bucket. These parameters can be used to adjust the estimation of the number of tuples available in a given range.

Another important component that is related to multidimensionality is the distance function [20]. One major challenge is dealing with attributes that may have different domains (scales) and/or relative importance. For example, if we take the attributes, price and mileage, the user may weigh a 1000 price difference more than a 1000 mileage difference. A possible approach to allow meaningful comparison between such attributes is to standardize the attributes. If a particular user application also requires a different degree of importance or weights to attributes included in a query, the distance functions that are used in the proposed strategy can be formulated to incorporate such weights. For example, the vector p-norm distances can be modified to incorporate user-defined weights as shown below [30].

$$
d _ {p} (t, q) = \left(\sum_ {i = 1} ^ {n} w _ {i} | t _ {i} - q _ {i} | ^ {p}\right) ^ {1 / p} \quad \text { for } p \geq 1.
$$

In general, the one-dimensional setting demonstrated in this paper provides a reasonable theoretical and experimental foundation. The issues discussed above require some degree of flexibility in extending this framework to the generalized setting. Therefore, depending on the context of the application, several alternative approaches and/or assumptions related to the above issues can be incorporated for the multi-dimensional setting.

## 7. Conclusion

In this paper, we have analyzed histogram construction methods pertaining to their structures and accuracy in approximating the underlying data, and their impacts on the performance of top-k strategies. The qualities of a good histogram-based top-k strategy include its generalizability of performance across different types of histograms and its capability to leverage the accuracy of the statistics maintained. We have demonstrated these qualities using our cost-based strategy (QLOCS), along with comparative analysis against our benchmark strategy (the DWBS). The performance analysis using real and synthetic data sets indicates that QLOCS adequately meets these qualities, as shown by its consistent performance across the most commonly used histogram construction techniques and over a reasonably wide range of histogram sizes. The results show that the performance of QLOCS is relatively more robust across different structural characteristics of histograms. In addition, QLOCS leverages the distribution information within histogram bins over a range of bin sizes, and it shows improved performance with an improved fit to Uniform distribution due to smaller bins as well as the type of data set.

In closing, we summarize the viability of using QLOCS to efficiently process top-k queries in relational databases. Its main advantages are: (i) its operational simplicity, not relying on additional complex index structures; (ii) the fact that it constructs the optimal range query for each top-k request without any calibration effort with pre-specified workload; and (iii) as shown in this paper, it is a robust technique that can work with alternative histograms commonly adopted in commercial RDBMSs. These are certainly very attractive features when one considers the enormous installed base of RDBMSs.

There are several open research issues that can be addressed in future research. As we stated before, our objective in this paper is to provide both theoretical and empirical ground that can be extended to different settings with some degree of flexibility. Future research will deal with different approaches and/or assumptions in extending the one-dimensional methodology to multi-dimensional settings. Due to the nature and scope of the problem, this extension could be in many angles, including the histogram environment, the scope of distance functions, the type of data to deal with (e.g., categorical data), and the specific area of application for implementation. For example, while this research currently deals with histogram structures and distance functions that are commonly adopted in current commercial systems, the modeling task in the future will consider the optimality as well as practicality of using other histogram structures and distance functions. In addition, defining and formulating relevant processing costs requires an appropriate balance between the operational realities of RDBMS and the degree of complexity in mathematical modeling. Our current cost framework involves components and/or assumptions that are simplified for ease of exposition. Future research will consider enhancing these components in accordance with their criticality in the proposed framework.

Finally, future research will consider applying the histogram-based cost model to a sampling environment. One fundamental difference inherent in using samples of the database, as opposed to histograms, is the additional runtime costs and the relative difficulty in obtaining precise search bounds because of the possible misrepresentation of the database. On the other hand, sampling has an advantage over histograms in maintenance overhead, especially with an increase in the number of attributes or dimensions involved in queries [11]. Future work will explore ways to apply the cost-based framework to samples of the database in addition to histograms.

![](/api/attachments/UJPXZD2Z/fulltext/images/43830a140e37b23f52ffd9eb55db2f8210c55123f29d78552ff755487ae0b694.jpg)  
Fig. 10. Estimated distances using the DWBS.

## Appendix A. Illustrative example for DWBS

Consider a two-bucket histogram H shown in Fig. 10 above for a 2-attribute data set with 100 tuples. The data domain of the attributes is in the continuous interval [0,1] and the two buckets B1 and B2 have frequencies of 25 and 75, respectively. Now consider a top-50 query q that falls in bucket B1. According to the restart strategy, the closest possible point for B1 is the query point itself, with instances of 25 tuples, and the closest point for B2 is the point on the edge of B2 with distance $d _ { 1 }$ and instances of 75 tuples. Thus, for the restart strategy, the optimistic distance $d _ { 1 }$ is expected to contain at least the required 50 tuples. On the other hand, under the no-restart strategy, the pessimistic distance $d _ { 2 }$ guarantees the required 50 tuples.

Using the restart and no-restart ranges, the DWBS calibrates α for a set of queries, each requesting the top 50 tuples. Then, the average number of tuples retrieved will be examined as a function of α to determine the parameter $\alpha ^ { * }$ that minimizes it. Given any future query requesting the top 50 results, $\alpha ^ { * }$ will be used to determine a cut-off distance between the distances obtained using the restart $( d _ { 1 } )$ and the no-restart (d ) strategies illustrated above.

## Appendix B. Illustrative example for QLOCS

Consider a database of size $T = 5 0 { , } 0 0 0$ tuples and a top-$k$ query $q$ for k = 250, where from the histogram information it is determined that a total of $N { = } 1 0 0$ tuples are present between the Restart and the No-restart distance points, and 200 tuples $( \mathrm { i . e . } \ k _ { 1 } { = } 2 0 0 )$ are known to be retrieved at the Restart point. The objective is to retrieve the remaining 50 tuples $( \mathrm { i } . \mathrm { e } . , k _ { p } = 5 0 )$ from this range. Fig. 11 below illustrates the restart–excess cost trade-off and optimal distance $d ^ { * }$ . Note that a uniform cut-off point in the search range gives a distance of 0.5 $( \mathrm { i . e . , } \hat { d } { = } k _ { p } / N { = } 5 0 / 1 0 0 )$ , which is used to initialize the $d ^ { * }$ estimates in the successive approximation method.

![](/api/attachments/UJPXZD2Z/fulltext/images/01c4c63669fcbbf88a0cbad7e77f346bf92501a6732e01cac1e30b4d735eaf12.jpg)  
Fig. 11. Illustration of the restart–excess cost-tradeoffs and the optimal distance $d ^ { * } .$

ANOVA  
Table 1  
Number of iterations in the successive approximation method

<table><tr><td> $d^{*}$ </td><td>Convergence error</td><td>No. of iterations</td></tr><tr><td>0.664492</td><td>1E-10</td><td>9</td></tr><tr><td>0.664492</td><td>0.000000001</td><td>9</td></tr><tr><td>0.664492</td><td>0.00000001</td><td>9</td></tr><tr><td>0.664492</td><td>0.0000001</td><td>9</td></tr><tr><td>0.664492</td><td>0.000001</td><td>8</td></tr><tr><td>0.664492</td><td>0.00001</td><td>8</td></tr><tr><td>0.664492</td><td>0.0001</td><td>8</td></tr><tr><td>0.664491</td><td>0.001</td><td>7</td></tr><tr><td>0.662608</td><td>0.01</td><td>5</td></tr><tr><td>0.656172</td><td>0.1</td><td>4</td></tr></table>

Where as the cost-optimal distance based on QLOCS is 0.6645.

The main computational advantage of QLOCS over the DWBS is the absence of any calibration effort in the distance estimation process. In addition, evaluating the cost functions, given by Eqs. (9) and (10) in our model, using the successive approximation method is computationally insignificant. Table 1 also shows the number of iterations required to obtain $d ^ { * }$ at different levels of convergence errors. Note that if the convergence error is increased from $1 0 ^ { - 4 } ~ \mathrm { t o } ~ 1 0 ^ { - 1 0 }$ , the optimal point is guaranteed only with one more iteration.

## Appendix C. Statistical results (Tables 2–5)

Table 2  
Single factor ANOVA results from analyses of Census data set performance

<table><tr><td>ANOVA: single factor SUMMARY</td><td colspan="4">Excess</td></tr><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>QLOCS_Equicount</td><td>56</td><td>137.7445</td><td>2.459722893</td><td>2.250445</td></tr><tr><td>QLOCS_MaxDiff</td><td>56</td><td>174.4724</td><td>3.1155785</td><td>4.956035</td></tr><tr><td>QLOCS_Equiwidth</td><td>56</td><td>153.4591</td><td>2.740341071</td><td>3.17901</td></tr></table>

<table><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>12.12766</td><td>2</td><td>6.063831829</td><td>1.751626</td><td>0.176702</td><td>3.050786</td></tr><tr><td>Within groups</td><td>571.2019</td><td>165</td><td>3.461829753</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>583.3296</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>QLOCS_Equicount</td><td>56</td><td>5.826</td><td>0.104035714</td><td>0.005427</td></tr><tr><td>QLOCS_MaxDiff</td><td>56</td><td>3.58</td><td>0.063928571</td><td>0.000773</td></tr><tr><td>QLOCS_Equiwidth</td><td>56</td><td>6.498</td><td>0.116035714</td><td>0.003497</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>0.083398</td><td>2</td><td>0.041698881</td><td>12.9017</td><td>6.22E-06</td><td>3.050786</td></tr><tr><td>Within groups</td><td>0.533288</td><td>165</td><td>0.003232046</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>0.616685</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>QLOCS_Equicount</td><td>56</td><td>1,370,937</td><td>24,481.02391</td><td>3.17E+08</td></tr><tr><td>QLOCS_MaxDiff</td><td>56</td><td>995,067.1</td><td>17,769.05572</td><td>99,532,386</td></tr><tr><td>QLOCS_Equiwidth</td><td>56</td><td>1,558,270</td><td>27,826.24496</td><td>2.42E+08</td></tr></table>

(continued on next page)

Appendix C <sup>(</sup>continued <sup>)</sup>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>2.94E+09</td><td>2</td><td>1,468,955,379</td><td>6.698859</td><td>0.001595</td><td>3.050786</td></tr><tr><td>Within groups</td><td>3.62E+10</td><td>165</td><td>219,284,407.8</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>3.91E+10</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>DWBS_Equicount</td><td>56</td><td>202.5709</td><td>3.617338</td><td>32.40855</td></tr><tr><td>DWBS_MaxDiff</td><td>56</td><td>234.7453</td><td>4.19188</td><td>25.01538</td></tr><tr><td>DWBS_Equiwidth</td><td>56</td><td>531.9861</td><td>9.499751</td><td>249.824</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>1177.98586</td><td>2</td><td>588.9929</td><td>5.750987</td><td>0.003851111</td><td>3.050786</td></tr><tr><td>Within groups</td><td>16,898.6351</td><td>165</td><td>102.416</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>18,076.621</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>DWBS_Equicount</td><td>56</td><td>15.626</td><td>0.279036</td><td>0.108696</td></tr><tr><td>DWBS_MaxDiff</td><td>56</td><td>16.606</td><td>0.296536</td><td>0.053331</td></tr><tr><td>DWBS_Equiwidth</td><td>56</td><td>10.59</td><td>0.189107</td><td>0.008738</td></tr></table>

<table><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>0.37210686</td><td>2</td><td>0.186053</td><td>3.2686604</td><td>0.040538034</td><td>3.050786</td></tr><tr><td>Within groups</td><td>9.39202721</td><td>165</td><td>0.056921</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>9.76413407</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>DWBS_Equicount</td><td>56</td><td>3,415,620</td><td>60,993.21</td><td>4.84E+09</td></tr><tr><td>DWBS_MaxDiff</td><td>56</td><td>3,733,304</td><td>66,666.14</td><td>2.45E+09</td></tr><tr><td>DWBS_Equiwidth</td><td>56</td><td>2,613,185</td><td>46,664.02</td><td>5.48E+08</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>1.1902E+10</td><td>2</td><td>5.95E+09</td><td>2.278422</td><td>0.105660092</td><td>4.736137</td></tr><tr><td>Within groups</td><td>4.3095E+11</td><td>165</td><td>2.61E+09</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>4.4285E+11</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

Table 3  
Single factor ANOVA results from analyses of Array data set performance

<table><tr><td>ANOVA: single factor SUMMARY</td><td colspan="4">Excess</td></tr><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>QLOCS_Equicount</td><td>56</td><td>240.1873</td><td>4.289058</td><td>15.91414</td></tr></table>

Percentage of restart  
Appendix C <sup>(</sup>continued<sup>)</sup>

<table><tr><td>QLOCS_MaxDiff</td><td>56</td><td>253.3753</td><td>4.524559</td><td>16.88662</td></tr><tr><td>QLOCS_Equiwidth</td><td>56</td><td>223.8326</td><td>3.99701</td><td>16.01744</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>7.8224617</td><td>2</td><td>3.911231</td><td>0.240355</td><td>0.786624</td><td>3.050786</td></tr><tr><td>Within groups</td><td>2685.00107</td><td>165</td><td>16.27273</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>2692.8253</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>QLOCS_Equicount</td><td>56</td><td>3.252</td><td>0.058071</td><td>0.002262</td></tr><tr><td>QLOCS_MaxDiff</td><td>56</td><td>3.596</td><td>0.064214</td><td>0.002227</td></tr><tr><td>QLOCS_Equiwidth</td><td>56</td><td>3.912</td><td>0.069857</td><td>0.003316</td></tr></table>

<table><tr><td>Source of Variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>0.00389162</td><td>2</td><td>0.001946</td><td>0.747949</td><td>0.474934</td><td>3.050786</td></tr><tr><td>Within groups</td><td>0.429252</td><td>165</td><td>0.002602</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>0.43314362</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>QLOCS_Equicount</td><td>56</td><td>1,760,973</td><td>31,445.95</td><td>6.53E+08</td></tr><tr><td>QLOCS_MaxDiff</td><td>56</td><td>2,113,333</td><td>37,738.1</td><td>9.69E+08</td></tr><tr><td>QLOCS_Equiwidth</td><td>56</td><td>1,918,074</td><td>34,251.32</td><td>8.17E+08</td></tr></table>

<table><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>1,112,885,403</td><td>2</td><td>5.56E+08</td><td>0.684335</td><td>0.505852</td><td>3.050786</td></tr><tr><td>Within groups</td><td>1.3416E+11</td><td>165</td><td>8.13E+08</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>1.3528E+11</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>DWBS_Equicount</td><td>56</td><td>242.3554</td><td>4.327775</td><td>20.20801</td></tr><tr><td>DWBS_MaxDiff</td><td>56</td><td>267.4031</td><td>4.775056</td><td>29.30088</td></tr><tr><td>DWBS_Equiwidth</td><td>56</td><td>196.7858</td><td>3.514031</td><td>15.13644</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>45.77854</td><td>2</td><td>22.88927</td><td>1.062224</td><td>0.348038</td><td>3.050786</td></tr><tr><td>Within groups</td><td>3555.493</td><td>165</td><td>21.54844</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>3601.272</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>45.77854</td><td>2</td><td>22.88927</td><td>1.062224</td><td>0.348038</td><td>3.050786</td></tr></table>

Appendix C <sup>(</sup>continued<sup>)</sup>

<table><tr><td>Within groups</td><td>3555.493</td><td>165</td><td>21.54844</td></tr><tr><td>Total</td><td>3601.272</td><td>167</td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>DWBS_Equicount</td><td>56</td><td>12.236</td><td>0.2185</td><td>0.075836</td></tr><tr><td>DWBS_MaxDiff</td><td>56</td><td>15.076</td><td>0.269214</td><td>0.055609</td></tr><tr><td>DWBS_Equiwidth</td><td>56</td><td>24.376</td><td>0.435286</td><td>0.035105</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>1.44009</td><td>2</td><td>0.720045</td><td>12.96997</td><td>5.87E-06</td><td>3.050786</td></tr><tr><td>Within groups</td><td>9.160195</td><td>165</td><td>0.055516</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>10.60029</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Groups</td><td>Count</td><td>Sum</td><td>Average</td><td>Variance</td></tr><tr><td>DWBS_Equicount</td><td>56</td><td>6,261,585</td><td>111,814</td><td>1.91E+10</td></tr><tr><td>DWBS_MaxDiff</td><td>56</td><td>7,799,129</td><td>139,270.2</td><td>1.4E+10</td></tr><tr><td>DWBS_Equiwidth</td><td>56</td><td>11,550,172</td><td>206,253.1</td><td>9.91E+09</td></tr></table>

<table><tr><td colspan="7">ANOVA</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>2.64E+11</td><td>2</td><td>1.32E+11</td><td>9.21541</td><td>0.000161</td><td>3.050786</td></tr><tr><td>Within groups</td><td>2.37E+12</td><td>165</td><td>1.43E+10</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>2.63E+12</td><td>167</td><td></td><td></td><td></td><td></td></tr></table>

Table 4 GLM analyses results of census data set performance

<table><tr><td rowspan="2">FACTOR</td><td rowspan="2">FACTOR LEVEL</td><td colspan="3">DWBS</td><td colspan="3">QLOCS</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td></tr><tr><td colspan="8">DEPENDENT VARIABLE=EXCESS</td></tr><tr><td>INTERCEPT</td><td></td><td> $3.267^{(a)}$ </td><td>0.184</td><td>17.749</td><td> $1.203^{(a)}$ </td><td>0.075</td><td>16.143</td></tr><tr><td colspan="8">HISTOGRAM TYPE</td></tr><tr><td></td><td>[HTYPE=EQCO]</td><td> $-5.284^{(a)}$ </td><td>0.116</td><td>-45.623</td><td> $-0.255^{(a)}$ </td><td>0.050</td><td>-5.062</td></tr><tr><td></td><td>[HTYPE=MaxD]</td><td> $-4.688^{(a)}$ </td><td>0.116</td><td>-40.366</td><td> $0.260^{(a)}$ </td><td>0.051</td><td>5.142</td></tr><tr><td></td><td>[HTYPE=EQWI]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">BIN SIZE</td></tr><tr><td></td><td>[HSIZE=100.00]</td><td> $11.570^{(a)}$ </td><td>0.165</td><td>69.982</td><td> $1.405^{(a)}$ </td><td>0.071</td><td>19.696</td></tr><tr><td></td><td>[HSIZE=200.00]</td><td> $4.504^{(a)}$ </td><td>0.164</td><td>27.398</td><td> $0.585^{(a)}$ </td><td>0.071</td><td>8.197</td></tr><tr><td></td><td>[HSIZE=400.00]</td><td> $2.195^{(a)}$ </td><td>0.164</td><td>13.405</td><td> $0.340^{(a)}$ </td><td>0.071</td><td>4.767</td></tr><tr><td></td><td>[HSIZE=800.00]</td><td> $1.069^{(a)}$ </td><td>0.163</td><td>6.550</td><td> $0.171^{(a)}$ </td><td>0.071</td><td>2.394</td></tr><tr><td></td><td>[HSIZE=1200.00]</td><td>0.086</td><td>0.163</td><td>0.528</td><td>0.017</td><td>0.071</td><td>0.245</td></tr><tr><td></td><td>[HSIZE=1600.00]</td><td>0.247</td><td>0.163</td><td>1.515</td><td>0.019</td><td>0.071</td><td>0.262</td></tr><tr><td></td><td>[HSIZE=2000.00]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">K</td></tr><tr><td></td><td>[K=5]</td><td> $14.971^{(a)}$ </td><td>0.197</td><td>75.861</td><td> $5.038^{(a)}$ </td><td>0.082</td><td>61.132</td></tr><tr><td></td><td>[K=10]</td><td> $7.583^{(a)}$ </td><td>0.196</td><td>38.639</td><td> $2.916^{(a)}$ </td><td>0.082</td><td>35.417</td></tr><tr><td></td><td>[K=25]</td><td> $3.431^{(a)}$ </td><td>0.194</td><td>17.650</td><td> $1.561^{(a)}$ </td><td>0.082</td><td>18.961</td></tr><tr><td></td><td>[K=50]</td><td> $2.056^{(a)}$ </td><td>0.194</td><td>10.594</td><td> $0.985^{(a)}$ </td><td>0.082</td><td>11.972</td></tr><tr><td></td><td>[K=100]</td><td> $1.112^{(a)}$ </td><td>0.194</td><td>5.745</td><td> $0.641^{(a)}$ </td><td>0.082</td><td>7.782</td></tr><tr><td></td><td>[K=250]</td><td>0.143</td><td>0.192</td><td>0.746</td><td> $0.329^{(a)}$ </td><td>0.082</td><td>3.992</td></tr><tr><td></td><td>[K=500]</td><td>0.038</td><td>0.189</td><td>0.203</td><td> $0.150^{(b)}$ </td><td>0.082</td><td>1.825</td></tr><tr><td></td><td>[K=1000]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr></table>

Appendix C <sup>(</sup>continued<sup>)</sup>

<table><tr><td rowspan="2">FACTOR</td><td rowspan="2">FACTOR LEVEL</td><td colspan="3">DWBS</td><td colspan="3">QLOCS</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td></tr><tr><td colspan="8">DEPENDENT VARIABLE = TOTAL COST</td></tr><tr><td>INTERCEPT</td><td>Intercept</td><td> $9088.900^{(a)}$ </td><td>131.307</td><td>69.219</td><td> $4874.155^{(a)}$ </td><td>167.697</td><td>29.065</td></tr><tr><td colspan="8">HISTOGRAM TYPE</td></tr><tr><td></td><td>[HTYPE=EQCO]</td><td> $-4579.747^{(a)}$ </td><td>82.606</td><td>-55.441</td><td> $-3332.818^{(a)}$ </td><td>113.447</td><td>-29.378</td></tr><tr><td></td><td>[HTYPE=MaxD]</td><td> $-2842.095^{(a)}$ </td><td>82.831</td><td>-34.312</td><td> $-776.887^{(a)}$ </td><td>113.762</td><td>-6.829</td></tr><tr><td></td><td>[HTYPE=EQWI]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">BIN SIZE</td></tr><tr><td></td><td>[HSIZE=100.00]</td><td> $9841.122^{(a)}$ </td><td>117.927</td><td>83.451</td><td> $7780.615^{(a)}$ </td><td>160.535</td><td>48.467</td></tr><tr><td></td><td>[HSIZE=200.00]</td><td> $5379.077^{(a)}$ </td><td>117.257</td><td>45.874</td><td> $2731.509^{(a)}$ </td><td>160.500</td><td>17.019</td></tr><tr><td></td><td>[HSIZE=400.00]</td><td> $2884.055^{(a)}$ </td><td>116.800</td><td>24.692</td><td> $1777.923^{(a)}$ </td><td>160.450</td><td>11.081</td></tr><tr><td></td><td>[HSIZE=800.00]</td><td> $1537.808^{(a)}$ </td><td>116.465</td><td>13.204</td><td> $910.798^{(a)}$ </td><td>160.434</td><td>5.677</td></tr><tr><td></td><td>[HSIZE=1200.00]</td><td> $643.016^{(a)}$ </td><td>116.304</td><td>5.529</td><td> $268.605^{(b)}$ </td><td>160.379</td><td>1.675</td></tr><tr><td></td><td>[HSIZE=1600.00]</td><td>172.891</td><td>116.249</td><td>1.487</td><td>38.055</td><td>160.366</td><td>0.237</td></tr><tr><td></td><td>[HSIZE=2000.00]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">K</td></tr><tr><td></td><td>[K=5]</td><td> $-8531.633^{(a)}$ </td><td>140.766</td><td>-60.609</td><td> $-4992.276^{(a)}$ </td><td>185.388</td><td>-26.929</td></tr><tr><td></td><td>[K=10]</td><td> $-8379.708^{(a)}$ </td><td>139.981</td><td>-59.863</td><td> $-5113.583^{(a)}$ </td><td>185.235</td><td>-27.606</td></tr><tr><td></td><td>[K=25]</td><td> $-7933.064^{(a)}$ </td><td>138.675</td><td>-57.206</td><td> $-5205.217^{(a)}$ </td><td>185.165</td><td>-28.111</td></tr><tr><td></td><td>[K=50]</td><td> $-7194.503^{(a)}$ </td><td>138.410</td><td>-51.980</td><td> $-4896.124^{(a)}$ </td><td>185.183</td><td>-26.439</td></tr><tr><td></td><td>[K=100]</td><td> $-6277.430^{(a)}$ </td><td>138.092</td><td>-45.458</td><td> $-4213.471^{(a)}$ </td><td>185.182</td><td>-22.753</td></tr><tr><td></td><td>[K=250]</td><td> $-4670.858^{(a)}$ </td><td>136.619</td><td>-34.189</td><td> $-2673.060^{(a)}$ </td><td>185.172</td><td>-14.436</td></tr><tr><td></td><td>[K=500]</td><td> $-3105.689^{(a)}$ </td><td>134.531</td><td>-23.085</td><td> $-1432.653^{(a)}$ </td><td>185.168</td><td>-7.737</td></tr><tr><td></td><td>[K=1000]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr></table>

<sup>(a)</sup>Significant at confidence level, α = 0.05.  
<sup>(b)</sup>Significant at confidence level, α = 0.10.  
<sup>(c)</sup>This parameter is set to zero because it is redundant and coefficients for other levels of the factor should be interpreted as +/− from this.

Table 5  
GLM analyses results of array data set performance

<table><tr><td rowspan="2">FACTOR</td><td rowspan="2">FACTOR LEVEL</td><td colspan="3">DWBS</td><td colspan="3">QLOCS</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td></tr><tr><td colspan="8">DEPENDENT VARIABLE=EXCESS</td></tr><tr><td>INTERCEPT</td><td>Intercept</td><td> $2.102^{(a)}$ </td><td>0.155</td><td>13.531</td><td> $1.502^{(a)}$ </td><td>0.269</td><td>5.578</td></tr><tr><td colspan="8">HISTOGRAM TYPE</td></tr><tr><td></td><td>[HTYPE=EQCO]</td><td>0.016</td><td>0.094</td><td>0.169</td><td>-0.205</td><td>0.297</td><td>-0.690</td></tr><tr><td></td><td>[HTYPE=MaxD]</td><td>0.560</td><td>0.093</td><td>6.031</td><td>-0.284</td><td>0.297</td><td>-0.958</td></tr><tr><td></td><td>[HTYPE=EQWI]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">BIN SIZE</td></tr><tr><td></td><td>[HSIZE=200.00]</td><td> $3.048^{(a)}$ </td><td>0.132</td><td>23.070</td><td>0.163</td><td>0.399</td><td>0.407</td></tr><tr><td></td><td>[HSIZE=400.00]</td><td> $0.674^{(a)}$ </td><td>0.132</td><td>5.108</td><td>0.184</td><td>0.399</td><td>0.461</td></tr><tr><td></td><td>[HSIZE=800.00]</td><td> $0.263^{(a)}$ </td><td>0.131</td><td>1.999</td><td>0.112</td><td>0.399</td><td>0.280</td></tr><tr><td></td><td>[HSIZE=1600.00]</td><td>-0.064</td><td>0.131</td><td>-0.487</td><td>0.016</td><td>0.399</td><td>0.040</td></tr><tr><td></td><td>[HSIZE=2400.00]</td><td>0.052</td><td>0.130</td><td>0.398</td><td>-0.012</td><td>0.399</td><td>-0.031</td></tr><tr><td></td><td>[HSIZE=3200.00]</td><td>0.045</td><td>0.130</td><td>0.346</td><td>-0.005</td><td>0.399</td><td>-0.014</td></tr><tr><td></td><td>[HSIZE=4000.00]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">K</td></tr><tr><td></td><td>[K=5]</td><td> $10.945^{(a)}$ </td><td>0.156</td><td>70.000</td><td> $11.738^{(a)}$ </td><td>0.358</td><td>32.810</td></tr><tr><td></td><td>[K=10]</td><td> $5.741^{(a)}$ </td><td>0.155</td><td>36.966</td><td> $5.640^{(a)}$ </td><td>0.358</td><td>15.766</td></tr><tr><td></td><td>[K=25]</td><td> $1.681^{(a)}$ </td><td>0.154</td><td>10.926</td><td> $2.058^{(a)}$ </td><td>0.357</td><td>5.756</td></tr><tr><td></td><td>[K=50]</td><td> $0.820^{(a)}$ </td><td>0.152</td><td>5.387</td><td> $1.081^{(a)}$ </td><td>0.357</td><td>3.025</td></tr><tr><td></td><td>[K=100]</td><td> $0.399^{(a)}$ </td><td>0.152</td><td>2.617</td><td>0.530</td><td>0.357</td><td>1.485</td></tr><tr><td></td><td>[K=250]</td><td>-0.007</td><td>0.151</td><td>-0.046</td><td>0.031</td><td>0.357</td><td>0.087</td></tr><tr><td></td><td>[K=500]</td><td>0.077</td><td>0.150</td><td>0.516</td><td>-0.049</td><td>0.357</td><td>-0.137</td></tr><tr><td></td><td>[K=1000]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr></table>

Appendix C <sup>(</sup>continued<sup>)</sup>

<table><tr><td rowspan="2">FACTOR</td><td rowspan="2">FACTOR LEVEL</td><td colspan="3">DWBS</td><td colspan="3">QLOCS</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td></tr><tr><td colspan="8">DEPENDENT VARIABLE = TOTAL COST</td></tr><tr><td>INTERCEPT</td><td>Intercept</td><td> $2060.690^{(a)}$ </td><td>101.216</td><td>20.359</td><td> $420.416^{(a)}$ </td><td>126.733</td><td>3.317</td></tr><tr><td colspan="8">HISTOGRAM TYPE</td></tr><tr><td></td><td>[HTYPE=EQCO]</td><td> $793.621^{(a)}$ </td><td>60.972</td><td>13.016</td><td> $904.534^{(a)}$ </td><td>85.732</td><td>10.551</td></tr><tr><td></td><td>[HTYPE=MaxD]</td><td> $2536.088^{(a)}$ </td><td>60.513</td><td>41.910</td><td> $3539.304^{(a)}$ </td><td>85.701</td><td>41.298</td></tr><tr><td></td><td>[HTYPE=EQWI]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">BIN SIZE</td></tr><tr><td></td><td>[HSIZE=200.00]</td><td> $7919.395^{(a)}$ </td><td>86.087</td><td>91.993</td><td> $8803.247^{(a)}$ </td><td>121.478</td><td>72.468</td></tr><tr><td></td><td>[HSIZE=400.00]</td><td> $3990.158^{(a)}$ </td><td>85.919</td><td>46.441</td><td> $2071.126^{(a)}$ </td><td>121.318</td><td>17.072</td></tr><tr><td></td><td>[HSIZE=800.00]</td><td> $2126.057^{(a)}$ </td><td>85.594</td><td>24.839</td><td> $652.856^{(a)}$ </td><td>121.183</td><td>5.387</td></tr><tr><td></td><td>[HSIZE=1600.00]</td><td> $1237.485^{(a)}$ </td><td>85.526</td><td>14.469</td><td> $380.262^{(a)}$ </td><td>121.172</td><td>3.138</td></tr><tr><td></td><td>[HSIZE=2400.00]</td><td> $707.258^{(a)}$ </td><td>84.728</td><td>8.347</td><td> $204.848^{(b)}$ </td><td>121.171</td><td>1.691</td></tr><tr><td></td><td>[HSIZE=3200.00]</td><td> $514.148^{(a)}$ </td><td>84.714</td><td>6.069</td><td>-0.522</td><td>121.173</td><td>-0.004</td></tr><tr><td></td><td>[HSIZE=4000.00]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr><tr><td colspan="8">K</td></tr><tr><td></td><td>[K=5]</td><td> $-4770.191^{(a)}$ </td><td>101.865</td><td>-46.828</td><td> $-2783.492^{(a)}$ </td><td>140.264</td><td>-19.845</td></tr><tr><td></td><td>[K=10]</td><td> $-4709.587^{(a)}$ </td><td>101.187</td><td>-46.544</td><td> $-2691.046^{(a)}$ </td><td>140.154</td><td>-19.201</td></tr><tr><td></td><td>[K=25]</td><td> $-4369.364^{(a)}$ </td><td>100.218</td><td>-43.598</td><td> $-2792.507^{(a)}$ </td><td>140.007</td><td>-19.945</td></tr><tr><td></td><td>[K=50]</td><td> $-4200.369^{(a)}$ </td><td>99.150</td><td>-42.364</td><td> $-2603.694^{(a)}$ </td><td>139.946</td><td>-18.605</td></tr><tr><td></td><td>[K=100]</td><td> $-3538.289^{(a)}$ </td><td>99.232</td><td>-35.657</td><td> $-2296.028^{(a)}$ </td><td>139.933</td><td>-16.408</td></tr><tr><td></td><td>[K=250]</td><td> $-2630.720^{(a)}$ </td><td>98.283</td><td>-26.767</td><td> $-1325.067^{(a)}$ </td><td>139.943</td><td>-9.469</td></tr><tr><td></td><td>[K=500]</td><td> $-1273.489^{(a)}$ </td><td>97.781</td><td>-13.024</td><td> $-595.943^{(a)}$ </td><td>139.923</td><td>-4.259</td></tr><tr><td></td><td>[K=1000]</td><td> $0^{(c)}$ </td><td>.</td><td>.</td><td> $0^{(c)}$ </td><td>.</td><td>.</td></tr></table>

<sup>(a)</sup>Significant at confidence level, $\scriptstyle \alpha = 0 . 0 5 .$  
<sup>(b)</sup>Significant at confidence level, α = 0.10.  
<sup>(c)</sup>This parameter is set to zero because it is redundant and coefficients for other levels of the factor should be interpreted as $+ / -$ from this.

## References

[1] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, ACM Press, New York, 1999.

[2] S. Berchtold, D.A. Keim, H.-P. Kriegel, T. Seidl, Indexing the solution space: a new technique for nearest neighbor search in high-dimensional space, IEEE Transactions on Knowledge and Data Engineering 12 (1) (2000) 45–57.

[3] C. Blake, C. Merz, UCI Repository of Machine-learning Databases, 1999 Available at <sup>b</sup>http://www.ics.uci.edu/\~mlearn/ MLRepository.html<sup>N</sup>.

[4] N. Bruno, S. Chaudhuri, L. Gravano, Performance of multiattribute top-k queries on relational systems. Tech. Rep. CUCS-021-00, Columbia University, 2000 Downloadable from http:// www1.cs.columbia.edu/\~library/2000.html<sup>N</sup>).

[5] N. Bruno, S. Chaudhuri, L. Gravano, Top-k selection queries over relational databases: mapping strategies and performance evaluation, ACM Transactions on Database Systems 27 (2) (2002) /153–187.

[6] M.J. Carey, D. Kossmann, On saying “Enough Already!” in SQL, Proceedings of the 1997 ACM SIGMOD International Conference on Management of Data, May 13–15, Tucson, AZ, 1997, pp. 219–230.

[7] M.J. Carey, D. Kossmann, Reducing the breaking distance of an SQL query engine, Proceedings of the Twenty-fourth International Conference on Very Large Databases, August 24–27, New York City, NY, 1998, pp. 158–169.

[8] S.W.K. Chan, Beyond keyword and cue-phrase matching: a sentence-based abstraction technique for information extraction, Decision Support Systems 42 (2) (2006) 759–777.

[9] K.C. Chang, S. Hwang, Minimal probing: supporting expensive predicates for top-k queries, Proceedings of the 2002 ACM SIGMOD International Conference on Management of Data, June 4–6, Madison, Wisconsin, 2002, pp. 346–357.

[10] S. Chaudhuri, L. Gravano, Evaluating top-k selection queries, Proceedings of the 25th International Conference on Very Large Data Bases, September 7–10, Edinburgh, Scotland, 1999, pp. 397–410.

[11] C.-M. Chen, Y. Ling, A sampling-based estimator for top-k selection query, Proceedings of the 18th International Conference on Data Engineering, February 25–March 1, San Jose, CA, 2002, pp. 617–627.

[12] Y. Chen, W. Meng, Top-N Query: query language, distance function and processing strategies, Proceedings of Fourth International Conference on Web-Age Information Management, August 17–19, Chengdu, China, 2003, pp. 458–470.

[13] Y.D. Chung, W.S. Yang, M.H. Kim, An efficient, robust method for processing of partial top-k/bottom-k queries using the RD-Tree in OLAP, Decision Support Systems 43 (2) (2007) 313–321.

[14] D. Donjerkovic, R. Ramakrishnan, Probabilistic optimization of top N queries, Proceedings of the 25th International Conference on Very Large Data Bases, September 7–10, Edinburgh, Scotland, 1999, pp. 411–422.

[15] C. Faloutsos, I. Kamel, Relaxing the uniformity and independence assumptions using the concept of fractal dimension, Journal of Computer and System Sciences 55 (3) (1997) 229–240.

[16] W. Fan, M. Gordon, P. Pathak, On linear mixture of expert approaches to information retrieval, Decision Support Systems 42 (2) (2006) 975–987.

[17] U. Güntzer, W. Balke, W. Kießling, Optimizing multi-feature queries for image databases, Proceedings of the 26th International Conference on Very Large Data Bases, September 10–14, Cairo, Egypt, 2000, pp. 419–428.

[18] A. Guttman, R-trees: a dynamic index structure for spatial searching, Proceedings of ACM SIGMOD International Conference on Management of Data, June 18–21, Boston, Massachusetts, 1984, pp. 47–57.

[19] S.H. Kwok, J.L. Zhao, Content-based object organization for efficient image retrieval in image databases, Decision Support Systems 42 (3) (2006) 1901–1916.

[20] A. Løkketangen, D.L Woodruff, A distance function to support optimized selection decisions, Decision Support Systems 39 (3) (2002) 345–354.

[21] D.B. Lomet, B. Salzberg, The hB-Tree: a multiattribute indexing method with good guaranteed performance, ACM Transactions on Database Systems 15 (4) (1990) 625–658.

[22] M. Muralikrishna, D.J. DeWitt, Equi-depth multi-dimensional histograms, Proceedings of the 1988 ACM SIGMOD International Conference on Management of Data, June 1–3, Chicago, Illinois, 1988, pp. 28–36.

[23] S.A. Nene, S.K. Nayer, A simple algorithm for nearest neighbor search in high dimensions, IEEE Transactions on Pattern Analysis and Machine Intelligence 19 (9) (1997) 989–1003.

[24] G. Piatetsky-Shapiro, C. Connell, Accurate estimation of the number of tuples satisfying a condition, Proceedings of the 1984 ACM SIGMOD International Conference on Management of Data, June 18–21, Boston, Massachusetts, 1984, pp. 256–276.

[25] V. Poosala, Y.E. Ioannidis, Selectivity estimation without the attribute value independence assumption, Proceedings of the 23rd International Conference on Very Large Databases, August 25–29, 1997, Athens, Greece, 1997, pp. 486–495.

[26] V. Poosala, Y.E. Ioannidis, P.J. Haas, E.J. Shekita, Improved histograms for selectivity estimation of range predicates, Proceedings of the 1996 ACM SIGMOD International Conference on Management of Data, June 4–6, Montreal, Quebec, 1996, pp. 294–305.

[27] R. Ramakrishnan, J. Gehrke, Database Management Systems, 2nd ed.McGraw-Hill, 2000.

[28] RANK-Top-k Query Processing, Computer Science Department, Columbia University (available at <sup>b</sup>http://rank.cs.columbia.edu/ main.html(<sup>N</sup>).

[29] G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, McGraw-Hill, 1983.

[30] P.-N. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Pearson, 2006.

Anteneh Ayanso is an Assistant Professor in Information Systems at Brock University. He received his Ph.D. in Information Systems from the University of Connecticut in 2004. His research interests are in data management, electronic business, quantitative modeling and simulation in information systems and supply chains. His research has appeared in European Journal of Operational Research, and in information systems conferences such as Workshop on Information Technology and Systems (WITS) and International Conference on E-Business (NCEB).

Paulo B. Goes is the Gladstein Professor of Information Technology and Innovation at the School of Business of the University of Connecticut. He received his Ph.D. from the University of Rochester. His research interests are in the areas of design and evaluation of models for e-business, emerging technologies, online auctions, database technology and systems, and technology infrastructure. His research has appeared in several journals including Management Science, MISQ, ISR, Journal of MIS, Operations Research, IN-FORMS Journal on Computing, IEEE Transactions on Communications, IEEE Transactions on Computers. Dr. Goes is Senior Editor of Information Systems Research, and Associate Editor of Management Science, Decision Sciences, Journal of Management Information Systems, and the INFORMS Journal on Computing. In 2004 he cochaired WITS, the Workshop on Information Technology and Systems, and was recently elected the WITS Organization President. He is the co-founder and director of CIDRIS, a research center dedicated to research with Internet data.

Kumar Mehta is an Assistant Professor of Management Information Systems at George Mason University's School of Management. He received his Ph.D. from University of Illinois at Chicago in 2002. His research interests include Data Mining, Information Retrieval and Agent-based Computational Modeling. His research has appeared in Decision Support Systems, Journal of Retailing and Information Technology Management.
