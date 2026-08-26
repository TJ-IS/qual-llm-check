---
otero_id: 5156
otero_key: "87HGHEFD"
title: "Range query estimation with data skewness for top-k retrieval"
authors: "Anteneh Ayanso; Paulo B. Goes; Kumar Mehta"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Range query estimation with data skewness for top-k retrieval

Anteneh Ayanso <sup>a,</sup>⁎, Paulo B. Goes <sup>b</sup>, Kumar Mehta <sup>c</sup>

<sup>a</sup> Department of Finance, Operations, and Information Systems, Goodman School of Business, Brock University, 500 Glenridge Avenue, St. Catharines, ON L2S 3A1, Canada

<sup>b</sup> Department of Management Information Systems, Eller College of Management, University of Arizona, 1130 E. Helen Street, Tucson, AZ 85721, US

<sup>c</sup> Department of Decision Science and MIS, School of Management, George Mason University, 4400 University Drive, Fairfax, VA 22030, USA

## a r t i c l e i n f o

Article history: Received 10 March 2013 Received in revised form 2 August 2013 Accepted 16 September 2013 Available online 23 September 2013

Keywords: Top-k query Query-mapping Query processing Cost model RDBMSs

## a b s t r a c t

Top-k querying can signi<sup>fi</sup>cantly improve the performance of web-based business intelligence applications such as price comparison and product recommendation systems. Top-k retrieval involves <sup>fi</sup>nding a limited number of records in a relational database that are most similar to user-speci<sup>fi</sup>ed attribute-value pairs. This paper extends the cost-based query-mapping method for top-k retrieval by incorporating data skewness in range estimation. Experiments on real world and synthetic multi-attribute data sets show that incorporating data skewness provides a robust performance across different types of data sets, query sets, distance functions, and histograms. © 2013 Elsevier B.V. All rights reserved

## 1. Introduction

The integration of database and information retrieval technologies is becoming increasingly important, with more and more textual data being stored in relational database management systems (RDBMSs). Many customer-centric applications today require top-k retrieval in which the k most important objects are returned among the potentially huge answer space by a given ranking (distance) function [17]. RDBMSs primarily support queries that deal only with data that exactly match selection criteria [23]. As a result, end-users face the challenge of routinely specifying value ranges of attributes in search of a limited number of approximate matches.

Much of the existing research in top-k retrieval has focused on techniques that involve high-performance indexing that requires signi<sup>fi</sup>cant changes in the query engines of RDBMSs. Due to the complexity in incorporating new index structures in RDBMSs, developing scalable as well as practical top-k retrieval methods is crucial. Among the various approaches proposed in the literature, the query-mapping approach (see Refs. [1,2,4,5,9]) has shown that database pro<sup>fi</sup>les can be effectively used to estimate approximate range queries in order to avoid the requirement of a full sequential scan of a relation to answer top-k queries. The key advantage of this approach is that it can be operationalized at an application layer outside of core query engines of RDBMSs. As a result, the development of new data access methods and specialized index structures can further enhance its feasibility in various application environments [5]. Therefore, the practical appeal of the query-mapping approach provides signi<sup>fi</sup>cant opportunity if the underlying technical limitations are overcome through improvements on the range estimation procedure. This paper extends the cost-based query-mapping strategy [1,2] by incorporating data skewness in the range estimation procedure.

For the purpose of summarizing the contents of relations and estimating query result sizes for ef<sup>fi</sup>cient execution plans, many current database systems (e.g. IBM DB2, Informix, Microsoft SQL Server, and Oracle) maintain some type of histograms. Histograms partition the underlying relations into distinct buckets by specifying value ranges of attributes and the number of database tuples (or records) available within those ranges. In histogram construction, a bucket is de<sup>fi</sup>ned as a partition of a data set speci<sup>fi</sup>ed by attribute value ranges as boundaries and number of database tuples (or records) available within those ranges as frequencies. These summary statistics are key components of the query mapping approach for top-k retrieval. Another key component of the query-mapping approach is a distance function, which is used for measuring the “closeness” of tuples to a query point. Distance or scoring functions based on l-norms (e.g., Euclidean, max, and sum) are commonly used in top-k research [1,2,5,9]. From top-k retrieval perspective, an important property of the l-norm distances is monotonicity which states that if a tuple is closer along each attribute to the values of a query than some other tuple is, then, the distance from the query point to this tuple cannot be longer than that of any other tuple [5,9]. This allows measuring relevance and ranking of tuples to user queries. Thus, the query-mapping mechanism utilizes distance functions and histograms maintained in RDBMSs to obtain upper and lower bounds for selectivity estimates and determine an equivalent range query. Building upon this query-mapping strategy, the cost-based methodology [1,2] further leverages the trade-offs in query processing costs to determine an optimal range for answering top-k queries. More speci<sup>fi</sup>cally, the method incorporates the tradeoff between the cost of dealing with excess tuples and the cost of re-executing (restarting) a query when an estimated range fails to meet the desired number of tuples. Therefore, the method determines a cost-optimal range by minimizing the sum of the expected costs of re-processing and the expected costs of handling results in excess of the required number.

Unlike previous histogram-based methods, such as the dynamic workload-based strategy (DWBS) [5], the cost-based query-mapping method does not require training different workloads of queries for range estimation. However, like previous histogram-based methods, the method utilizes histogram information for range query estimation. The use of histograms as the basis for range query estimation is generally constrained by data distribution, where histograms are assumed to have uniform tuple density within individual histogram buckets or data partitions [4]. In the presence of data skewness, range estimation can be affected by the degree to which histogram buckets conform to uniform tuple density, particularly in multidimensional environments. When using the Uniform distribution assumption for histogram buckets, the result size estimation is based on the notion that tuples are evenly spread over a given search bound. However, in the presence of data skewness, the Uniform distribution assumption may affect the range estimation accuracy for top-k retrieval. This paper particularly addresses this common limitation of the histogram-based methods [1,2,5,9] by incorporating data skewness in histograms in the range estimation process and extending the modeling framework of the cost-based strategy [1,2].

Prior research in query optimization has shown that the use of the attribute value independence assumption for joint data distributions in multidimensional environments can lead to inaccurate result size estimations (e.g., see [11]). Consequently, there has been a signi<sup>fi</sup>cant amount of work on ef<sup>fi</sup>cient techniques to approximate joint data distributions using multi-dimensional histograms (e.g., see Refs. [24–27]). The underlying assumption in these histogram techniques is that the distribution of values of a relation is described by an n-dimensional histogram. Because the objective of the query-mapping strategy is to estimate an equivalent range query for top-k retrieval, the implication of the attribute value independence assumption on approximating joint data distribution is equally signi<sup>fi</sup>cant.

Furthermore, in top-k query-mapping, the consideration of multiple attributes changes how the search space should be viewed in multidimensional histograms for result size estimation. For instance, in a range de<sup>fi</sup>ned by a distance from a given query point, there can be several histogram buckets whose area/volume is either fully or partially included within this distance range. This affects the approach that can be taken in de<sup>fi</sup>ning the search bound and determining the number of tuples available at and around a given query point. In the literature, there are two different approaches to de<sup>fi</sup>ne the search bound for a given query point. The <sup>fi</sup>rst approach [5,9] considers buckets as atomic and takes an ordering of “optimistic” and “pessimistic” distances from the query point to the edges of each bucket. For multi-dimensional histogram, if buckets are not considered atomic, measuring the closeness of tuples in the different partitions of the data space requires estimating the volume overlap of buckets. This is mainly because there can be several buckets of tuples at and around a given query point in the multidimensional space. Thus, the second approach [4] involves the estimation of the volume overlap of buckets that fall within a given distance from a query point as well as the estimation of a data skewness parameter to adjust for the number of tuples that are expected to be included within this range. In measuring data skewness, prior research suggests the use of an error metric [13] or deflation parameter [4] that can be stored for each histogram or for each histogram bucket at the time of histogram construction, respectively. These parameters are then used in adjusting the estimation of the number of tuples available within a given range. It is important to note that the exact way of measuring volume overlap as well as data skewness in a multi-dimensional space are separate research issues. Given any available estimation techniques for volume overlap and data skewness, the objective of this paper is to develop a cost-based range estimation model that accounts for the deviation of data from the Uniform distribution assumption in a multidimensional histogram environment.

The rest of the paper is organized as follows. Section 2 provides a review of related research in top-k querying. Section 3 presents the cost-based estimation model, followed by the extension of the model with data skewness in Section 4. Section 5 describes the experimental setting, followed by the discussion of the computational results in Section 6. Finally, Section 7 provides concluding remarks and discusses limitations and future research directions.

## 2. Related literature

The Web has proved to be an ideal example for top-k querying. As such, document retrieval has been the focus of most research in the information retrieval (IR) <sup>fi</sup>eld [3,6,16]. Top-k querying in multimedia systems is another area that stimulated related research in RDBMSs [14,21]. In the absence of ef<sup>fi</sup>cient methods for exploratory search and retrieval in RDBMSs, the naïve approach requires an exhaustive scan of the database. This is obviously not a practical approach for many RDBMS applications which require more ef<sup>fi</sup>cient and scalable performance. As a result, different streams of top-k processing techniques have been proposed in the recent literature [20].

The techniques in the existing literature are different, depending on whether they can be incorporated at the core of query engines or outside query engines at an application layer. Techniques that work at the core query engine level implement specialized rank-aware query operators or introduce new query algebra for query optimization [8,19,22]. On the other hand, the techniques that work at an application level use specialized indexes [7,28] or materialized views [12,18] to improve query response time during execution.

The techniques that are closely related to the method presented here belong to the query-mapping stream [1,2,4,5,9,10]. These techniques work at an application level and provide a mechanism to convert a top-k query into a conventional range query that RDBMSs support. In particular, these techniques avoid the need to do a full sequential scan of the database to answer top-k queries. Instead, these techniques estimate approximate range queries relying on summary information about the database in the form of histograms maintained in RDBMSs [1,2,4,5,9] or sample tuples obtained during query execution [10]. This paper belongs to this stream and extends the cost-based querymapping methodology [1,2] by incorporating data skewness in range estimation. Table 1 summarizes the key contributions and limitations of the techniques that are relevant to this paper.

## 2.1. Estimating volume overlap

Before presenting the details of the range estimation model, we provide a review of the volume overlap and data skewness parameter estimation techniques in the literature. As discussed earlier, the querymapping techniques utilize summary statistics about the database in the form of histograms, which create a partition of the data into distinct buckets of uniform tuple distribution to facilitate result size estimation. Thus, range estimation for top-k retrieval utilizes this histogram information and a distance function (e.g., Euclidean, max, and sum) to measure the “closeness” of database records to query conditions. For a range de<sup>fi</sup>ned by a distance from a given query point, there can be several histogram buckets whose area/volume is either fully or partially included within this distance range. Consequently, if buckets are not considered atomic, measuring the closeness of tuples in the different partitions of the data space requires computing the volume overlap of buckets. The method we adopt for computing the volume overlap of buckets has a closed form solution for the max distance function and an approximate solution for the Euclidean and sum distance functions [4]. Fig. 1 below shows the volume overlap of bucket B2 for the max distance function given a query point q in bucket B1. As illustrated in [4], given a query point q and a distance d, the volume intersection of bucket B2, delimited by the corners $l o w = ( l _ { 1 } . . . , l _ { n } )$ and $h i g h = ( h _ { 1 } . . . , h _ { n } )$ , is obtained by

Table 1  
Summary of contributions and limitations of existing methods.

<table><tr><td>Prior research</td><td>Method(s) and contributions</td><td>Limitations</td></tr><tr><td>Motro (1988)</td><td>-Introduces vague retrieval in RDBMSs-Uses distance functions</td><td>-Requires significant extension to the relational data model.</td></tr><tr><td>Donjerkovic and Ramakrishnan (1999)</td><td>-Framework based on traditional cost estimates using the query optimizer and summary statistics (histograms)-Supports multiple relations and complex queries (Joins and Unions)</td><td>-Method requires repeatedly calling the traditional query optimizer to evaluate costs and optimize query sub-trees.-Uses ranking condition based on single attribute with the attribute value independence assumption.</td></tr><tr><td>Chaudhuri et al. (1999)</td><td>-Propose query mapping method using multi-dimensional histograms and scoring functions-Heuristics based on histogram bounds (Restart, No-restart, Inter-1, and Inter-2)-Improved performance on traditional indexing (sorting) methods</td><td>-Simple heuristics based on optimistic and pessimistic scenarios, and uniform proportions.-Significant performance variation by data sets, histogram types, distance functions, and query sets.</td></tr><tr><td>Chen and Ling (2000)</td><td>-Propose parametric query mapping-method using sample tuples as source of statistics in place of histograms.-Method proportionately determines range based on sampling rate-Method scales better for large number of dimensions</td><td>-Method is workload-adaptive, calibrates pre-specified characteristics of query loads.-Method cannot guarantee the k tuples and could be affected by the sampling rate and the type of sampling.-Method lacks integrated framework to trade-off conflicting efficiency metrics.</td></tr><tr><td>Bruno et al. (2000)</td><td>-Use binary search over a distance range by leveraging information about the data distribution.</td><td>-Bounding the search distance relies on optimistic and pessimistic heuristics.-Method lacks integrated framework to trade-off conflicting efficiency metrics.</td></tr><tr><td>Bruno et al. (2002)</td><td>-Propose parametric or dynamic workload-based query mapping strategy using multi-dimensional histograms and distance functions-Use training and validation workloads for performance assessment.</td><td>-Method is workload-adaptive, calibrates pre-specified characteristics of query loads.</td></tr><tr><td>Ayanso et al. (2007, 2009)</td><td>-Propose cost-based range estimation using histograms and distance functions for single and multidimensional cases.-Provide cost-based framework to trade-off conflicting efficiency metrics.</td><td>-Method lacks integrated framework to trade-off conflicting efficiency metrics.-Performance could be affected by data distribution (i.e., deviation from the Uniform distribution assumption in histogram construction)</td></tr></table>

$$
\operatorname{Vol} (\mathrm{B2}) = \prod_ {i = 1} ^ {n} \max \left\{0, h _ {i} ^ {\prime} - l _ {i} ^ {\prime} \right\}
$$

$$
\text { where } h _ {i} ^ {\prime} = \min \{h _ {i}, q _ {i} + d \} \text { and } l _ {i} ^ {\prime} = \max \{l _ {i}, q _ {i} - d \}.
$$

The shapes of the Euclidean and Sum distance functions, however, make the computation relatively dif<sup>fi</sup>cult. The methods suggested in [4] include the discrete estimation technique using Monte Carlo or approximations based on the smallest hyper-rectangle that encloses (or the largest hyper-rectangle enclosed by) the corresponding shapes of the region de<sup>fi</sup>ned by the Euclidean and Sum distance functions. The Monte Carlo approximation involves generating random points inside a bucket and counting the fraction of the points that lie inside the overlap, which could be an expensive approach to employ at run time. In the alternative approaches, the use of the smallest hyper-rectangle that encloses the region (or the largest hyper-rectangle enclosed in the region) may overestimate (or underestimate) the volume and the expected number of tuples enclosed in the region. In this paper, we adopt the latter approach, which uses the largest hyper-rectangle enclosed by the shapes de<sup>fi</sup>ned by the Euclidean and Sum distance functions. Fig. 2 illustrates this for the Euclidean distance function.

![](/api/attachments/87HGHEFD/fulltext/images/6f44292aa8128cbe676221abec8f609de78204f570b2e587c394df1e5602ec15.jpg)  
Fig. 1. Volume overlap for the max distance [4].

Note in Fig. 2 that the largest hyper-rectangle with radius r is enclosed by the circle with radius d. The furthest points in the hyperrectangle from the query point are its vertices and the distance from the query point to any of the vertices equals $r { \sqrt { n } }$ , which also equals the radius d of the circle. Hence, the radius of the hyper-rectangle equals $r = d / { \sqrt { n } } ,$ , where n is the number of dimensions. Similarly, for the Sum distance function, $r = d / n \left[ 4 \right]$

## 2.2. Estimating data skewness parameter

Estimating data skewness in a multi-dimensional space is a challenging task and no single technique can serve all the different characteristics of skewness. The estimation technique we follow here is based on the box-counting procedure, which is illustrated in [15] for calculating the fractal dimension of data sets and adapted in [4] for measuring data skewness in a histogram bucket. The adaptation of the technique involves building a multi-dimensional grid consisting of t equal-sized cells, where t is approximately the number of tuples available in a bucket. For example, for a bucket containing 10 tuples, a 3 × 3 grid with 9 cells $( \mathrm { i } . \mathsf { e } . , t = 9 )$ will be constructed and the number of cells in the grid that enclose at least one tuple will be counted. Counting the number of cells c that enclose at least one tuple, the data skewness parameter α is de<sup>fi</sup>ned as $\alpha = \log ( t ) / \log ( c )$ , which measures the deviation of the distribution of tuples inside each bucket from the Uniform distribution. For the above example, if the number of cells that enclose at least one tuple is ${ \mathfrak { I } } \left( { \mathrm { i . e . , } } c = 6 \right)$ , then $\alpha = \log ( 9 ) / \log ( 6 ) = 1 . 2 3$ . If the number of cells containing at least one tuple equals the total number of cells in the grid, $\alpha = 1$ implies the uniform spread of the tuples in the bucket. On the other hand, if $\alpha > 1$ , a larger value indicates a higher degree of skewness inside the bucket. This parameter is computed and maintained for each histogram bucket during histogram construction. Additional information and illustration of the box-counting procedure can be found in [4] and [15].

![](/api/attachments/87HGHEFD/fulltext/images/18519bce2503ae3da65ed085be0b3e5a89eeb63b7dca27498d1a0dc463694ce2.jpg)  
Fig. 2. Volume overlap for Euclidean distance [4].

## 2.3. Defining the search bound: restart and no-restart points

In this section, we <sup>fi</sup>rst review the two different approaches of de<sup>fi</sup>ning the search bound (restart and no-restart boundaries) within which the optimal cutoff distance is determined for range query formulation. The <sup>fi</sup>rst approach assumes that histogram buckets are atomic and an ordering of distances from the query point to the closest and furthest points in the buckets provides the search bound [5,9]. The second approach [4], and the one we adopt here, utilizes the volume overlap of buckets to estimate the number of tuples within a given distance range.

## 2.3.1. Search bound considering buckets as atomic

The search bound in this approach is de<sup>fi</sup>ned by an ordering of optimistic and pessimistic distances from the query point to the buckets of the histogram. For a given histogram bucket, the optimistic distance represents the closest distance from the query point to any point in that bucket. On the other hand, the pessimistic distance represents the furthest distance from the query point to any point in that bucket. A cut-off point resulting from an ordering of the optimistic distances where there are at least k records de<sup>fi</sup>nes the restart point. Similarly, a cut-off point resulting from an ordering of the pessimistic distances where there are at least k records de<sup>fi</sup>nes the no-restart point. While the no-restart point is a guaranteed point, the restart point may or may not give the desired number of results. The main drawback in using this approach, particularly using multi-dimensional histograms, is the high probability that a given distance may include a number of adjacent buckets. Thus, any subsequent optimization within this bound could be affected by the information assumed. In fact, the assumed restart point itself could potentially return more results than required as this point is not a guaranteed restart point. Due to this, our cost-based strategy uses the volume overlap of buckets discussed below to de<sup>fi</sup>ne the search bound.

## 2.3.2. Search bound using volume overlap

In this approach, the volume shared by buckets for a given distance from a query point is used to estimate the number of tuples available within this range. Given an ascending ordering of the distances from the query point to the furthest point of each bucket, the overlap of the buckets within a given distance is estimated using the estimation technique illustrated in the previous section. The speci<sup>fi</sup>c steps for de<sup>fi</sup>ning the search bound using volume overlap are as follows:

Step-1: For each histogram bucket, compute the distance from the query point to the furthest point within the bucket. Due to the monotonic property of the distance functions used [5,9], the furthest point within a bucket is the point that is the furthest dimension by dimension.

Step-2: Sort the distances in ascending order.

Step-3: Beginning with the smallest distance and using the count information within each histogram bucket, determine if there are at least k tuples within this range after considering the volume overlap of the other buckets in the order.

Step-4: If there are at least k tuples available within the range, the distance, along with the number of tuples estimated, de<sup>fi</sup>nes the search bound.

Step-5: Compute the data skewness value α for the search bound, taking the average of the values for the buckets included in this bound.

Step-6: If there are less than k tuples available within the range, for the remaining tuples, take this range as the restart range and repeat the above steps to de<sup>fi</sup>ne the no-restart range using the next distance in the order.

The optimal range is thus determined from the bound de<sup>fi</sup>ned by the restart and no-restart ranges. Given this bound, we present below the details of the model for estimating the cost optimal range for top-k retrieval.

## 3. Estimating the optimal range

Extending the cost-based strategy [1,2], we now incorporate the volume overlap of buckets and data skewness to develop the range estimation model. We <sup>fi</sup>rst show the basics of the range estimation model with the Uniform distribution case, and then present the extended model that incorporates data skewness. Table 2 describes the notation used in our model.

Given a top-k query q(k) in an n-dimensional data space $D S \subseteq \Re ^ { n } ,$ , the search region $[ d _ { 1 } , d _ { 2 } ] ^ { n }$ is obtained from a multidimensional histogram using a distance function and the volume overlap of buckets as illustrated in the previous section. First, we project the search region into a normalized data space, a unit hypercube $[ 0 , 1 ] ^ { n }$ as shown in Fig. 3.

Then, we consider the probability density function f(t) for the distribution of tuples within the normalized data space. The probability p that a randomly chosen tuple is inside a given proportion v of the unit hypercube, where $0 \leq \nu \leq 1$ , can be expressed as

$$
p = \int_ {0} ^ {v} f (t) d t = v.\tag{1}
$$

Generalizing the one-dimension model [2], Eq. (1) represents the success probability p of a Bernoulli trial that a randomly chosen tuple is enclosed in the volume v. Thus, the probability of obtaining a given number of tuples j from the search bound v, where $0 \leq \nu \leq 1$ and the interval [0,1] contains N tuples, follows the Binomial distribution. For the Binomial random variable X, the probability of obtaining exactly j tuples is given by Eq. (2).

Table 2 Notation.

<table><tr><td>Symbol</td><td>Description</td></tr><tr><td> $DS \subseteq \Re^{n}$ </td><td>Represents the database consisting of a set of T points in a n-dimensional space</td></tr><tr><td> $n$ </td><td>The dimensionality of the data space</td></tr><tr><td> $k$ </td><td>The number of tuples requested</td></tr><tr><td> $T$ </td><td>The size (total number of tuples) of the database</td></tr><tr><td> $q(k)$ </td><td>The top-k query requesting the k closest tuples</td></tr><tr><td> $Q$ </td><td>The corresponding range query to be formulated</td></tr><tr><td> $[0, d_{1}]^{n}$ </td><td>Represents the restart region for q(k)</td></tr><tr><td> $[0, d_{2}]^{n}$ </td><td>Represents the no-restart region for q(k)</td></tr><tr><td> $[d_{1}, d_{2}]^{n}$ </td><td>The search region defined by the restart and no-restart boundaries for q(k)</td></tr><tr><td> $[0, 1]^{n}$ </td><td>The search region normalized into a unit hypercube</td></tr><tr><td> $k_{1}$ </td><td>The total number of qualifying tuples within the restart region</td></tr><tr><td> $k_{p}$ </td><td>The number of tuples to be retrieved from the search bound;Note:  $k_{p} = k - k_{1}$ </td></tr><tr><td> $N$ </td><td>The total number of qualifying tuples within the search bound</td></tr><tr><td> $v^{*}$ </td><td>The cost-optimal volume proportion that retrieves  $k_{p}$  tuples, where  $0 \leq v^{*} \leq 1$ </td></tr><tr><td> $\alpha$ </td><td>Data skewness parameter</td></tr></table>

![](/api/attachments/87HGHEFD/fulltext/images/6f38ba5a79695c8f047d4bb4cc4ccce83fc9e41dba3f894c781cf7268f2f54c7.jpg)  
Fig. 3. Projection of the search bound into unit hypercube

$$
P (X = j) = \binom {N} {j} v ^ {j} (1 - v) ^ {N - j}, \quad \text { where } j = 0, 1,... N.\tag{2}
$$

With the objective of obtaining $k _ { p }$ tuples from the N qualifying tuples available within the search bound, the probability of obtaining fewer than $k _ { p }$ tuples (i.e., a restart operation) is given by Eq. (3).

$$
P (\text { restart }) = \sum_ {j = 0} ^ {k p - 1} P (X = j) = \sum_ {j = 0} ^ {k p - 1} \binom {N} {j} v ^ {j} (1 - v) ^ {N - j}, \quad \text { where } j = 0, 1,... N.\tag{3}
$$

## 3.1. Modeling cost of restart

The consideration of multiple dimensions has an implication on the de<sup>fi</sup>nition of costs, especially in the cost of restarts. The cost of a restart operation is de<sup>fi</sup>ned as the cost of re-executing the query in the event that the estimated distance fails to retrieve the desired number of results. We use the size of the database T to measure the cost of accessing the database to obtain the remaining results with a no-restart range. Furthermore, the no-restart distance can potentially return a large number of tuples involving a signi<sup>fi</sup>cant sorting overhead. Therefore, the expected cost of a restart operation includes the cost of re-executing the query and the cost of sorting the returned results if the original range query fails to retrieve the required number of tuples. The sorting operation includes the tuples that are retrieved at the restart range $( \mathrm { i } . \mathrm { e } . , k _ { 1 } )$ as well as the additional tuples available within the search bound (i.e., N). Eq. (4) provides the cost of sorting these tuples, based on an operation central to sorting algorithms that are commonly used in commercial RDBMSs. Let ο represent the sorting overhead of these tuples.

$$
o = (k _ {1} + N) \log_ {2} (k _ {1} + N).\tag{4}
$$

The expected cost of restart is thus estimated by Eq. (5).

$$
C (\text { restart }) = (T + o). \sum_ {j = 0} ^ {k p - 1} \binom {N} {j} v ^ {j} (1 - v) ^ {N - j}.\tag{5}
$$

## 3.2. Modeling cost of excess results

To formulate the cost of handling excess results, we <sup>fi</sup>rst estimate the expected number of tuples E[X] in the range [0,v]. If N tuples are available in the range [0,1], Eq. (6) estimates the expected number of tuples E[X] in the range [0,v].

$$
E [ X ] = N \int_ {0} ^ {v} f (t) d t = v. N.\tag{6}
$$

Then, the expected number of results in excess of $k _ { p }$ is estimated by Eq. (7).

$$
E x c e s s = \left\{ \begin{array}{l l} v. N - k p, & \text { if   } v. N > k p \\ 0, & \text { otherwise } \end{array} \right..\tag{7}
$$

Therefore, given the estimate by Eq. (7), the additional cost of sorting with the excess results is formulated by Eq. (8).

$$
C (e x c e s s) = \left\{ \begin{array}{l l} (k + v. N - k p) \log_ {2} (k + v. N - k p) - k \log_ {2} k, & \text { if   } v. N > k p \\ 0, & \text { otherwise } \end{array} \right..\tag{8}
$$

Finally, considering both the cost of restart and the cost of excess, the total cost is expressed by

$$
T C (v) = \left\{ \begin{array}{l l} (T + o). \sum_ {j = 0} ^ {k p - 1} \binom {N} {j} v ^ {j} (1 - v) ^ {N - j} + (k + v N - k p) \log_ {2} (k + v N - k p) \\ - k \log_ {2} k, \text {   if   } v. N > k p \\ (T + o). \sum_ {j = 0} ^ {k p - 1} \binom {N} {j} v ^ {j} (1 - v) ^ {N - j}, & \text { otherwise. } \end{array} \right. \tag {1}\tag{9}
$$

Eq. (9) represents the multidimensional cost-based range estimation model. Extending the one-dimensional model, this model is now solved for the optimal volume proportion v \* to account for the number of dimensions. Eq. (10) provides the approximation function for the <sup>fi</sup>rst order condition $T C ^ { \prime } \left( \nu \right) = 0 ,$ , which is solved using the successive approximation method.

$$
v ^ {*} \sim v - \frac {T C ^ {\prime} (v)}{T C ^ {\prime \prime} (v)}.\tag{10}
$$

Given the optimal $\nu ^ { * }$ , the next step involves converting it into distance for range formulation. Technically, this will vary by the distance function being used as different distance functions lead to different multi-dimensional shapes. However, the <sup>fi</sup>nal range query is represented by an n-rectangle, regardless of the distance function used. Therefore, without loss of generality, the conversion of v \* into d \* is done by taking the nth root of $v ^ { \ast }$ as in Eq. (11).

$$
d ^ {*} = \sqrt [ n ]{v ^ {*}}, \text { where } n \text { is   the   number   of   dimensions. }\tag{11}
$$

## 4. Model with data skewness

In this section, we extend the range estimation model to incorporate the skewness parameter. This approach follows a pessimistic approach in de<sup>fi</sup>ning the success probability in the model and uses the Power probability density function for the distribution of tuples over the interval [0,1]. The Power distribution $( X \sim \operatorname { P o w } ( \alpha , \beta ) , \alpha \textrm { > } 0 , \beta > 0 )$ is generally de<sup>fi</sup>ned for the range $0 \leq X \leq 1 / \beta ,$ , where α is the shape parameter and $\beta$ is the scale parameter. The shape parameter α represents the average data skewness estimate for the search bound de<sup>fi</sup>ned in our model. In addition, in the re-de<sup>fi</sup>ned range over the interval [0,1], the scale parameter $\beta$ equals 1. Thus, the speci<sup>fi</sup>c Power distribution we use is Pow(α,1), where $\alpha > 1 .$ . The probability density function is given by Eq. (12).

$$
f (t) = \alpha t ^ {\alpha - 1}.\tag{12}
$$

Note that we are incorporating data skewness in the de<sup>fi</sup>nition of the success probability, which adjusts for the computation of the probability of restart and the expected number of excess results in the range estimation model. In the model with the Uniform distribution assumption, the success probability at each point in the distance interval [0,1] directly corresponds to the distance point. In other words, $p = d$ in the onedimension model, and $p = \nu$ in the multidimensional model. In the presence of data skewness with the Power density function, the probability p that a randomly chosen tuple is inside the volume v, where $0 \leq \nu \leq 1$ , can be expressed by Eq. (13).

$$
p = \int_ {0} ^ {v} \alpha t ^ {\alpha - 1} d t = v ^ {\alpha}.\tag{13}
$$

Fig. 4 shows the success probability de<sup>fi</sup>ned by the Power density function over the interval [0,1] for different values of the data skewness parameter α which can be related to the approach used in [4] in determining the fraction of tuples as a function of volume.

Following this, the probability of restart and the cost of restart are estimated by Eqs. (14) and (15), respectively. Note that the key change in the formulation is the incorporation of the data skewness parameter in the probability density function.

$$
\begin{array}{l} P (\text { restart }) = \sum_ {j = 0} ^ {k _ {p} - 1} P (X = j) = \sum_ {j = 0} ^ {k _ {p} - 1} \binom {N} {j} v ^ {\alpha , j} (1 - v ^ {\alpha}) ^ {N - j}, \text { where } j \\ = 0, 1,... N. \end{array}\tag{14}
$$

$$
C (r e s t a r t) = (T + o). \sum_ {j = 0} ^ {k _ {p} - 1} \binom {N} {j} v ^ {\alpha . j} \bigl (1 - v ^ {\alpha} \bigr) ^ {N - j}.\tag{15}
$$

Similarly, the expected number of tuples E[X] is estimated by Eq. (16).

$$
E [ X ] = N. v ^ {\alpha}.\tag{16}
$$

The expected number of results in excess of $k _ { p }$ is estimated by Eq. (17).

$$
E x c e s s = \left\{ \begin{array}{l l} N. v ^ {\alpha} - k p, & \text { if } N. v ^ {\alpha} > k p \\ 0, & \text { otherwise } \end{array} \right..\tag{17}
$$

![](/api/attachments/87HGHEFD/fulltext/images/5fe4bdab7467051d20e3350649d0e91550c107d195880fef83f2699d308f71dc.jpg)  
Fig. 4. The success probability for varying degree of data skewness

The cost of sorting with the excess results is estimated by Eq. (18).

$$
C (e x c e s s) = \left\{ \begin{array}{l l} (k + N. v ^ {\alpha} - k p) \log_ {2} (k + N. v ^ {\alpha} - k p) - k \log_ {2} k, & \text { if   } N. v ^ {\alpha} > k p \\ 0, & \text { otherwise } \end{array} \right..\tag{18}
$$

Given the restart and excess cost components, the total cost is expressed by Eq. (19).

$$
T C (v) = \left\{ \begin{array}{l l} (T + o). \sum_ {j = 0} ^ {k p - 1} \binom {N} {j} v ^ {\alpha , j} (1 - v ^ {\alpha}) ^ {N - j} + (k + v ^ {\alpha} N - k p) \log_ {2} (k + v ^ {\alpha} N - k p) \\ - k \log_ {2} k, \text {   if   } \hat {v} <   v \leq 1 \\ (T + o). \sum_ {j = 0} ^ {k p - 1} \binom {N} {j} v ^ {\alpha , j} (1 - v ^ {\alpha}) ^ {N - j}, & \text { elsewhere } \end{array} \right.
$$

where $\hat { \nu } = \left( k / N \right) ^ { 1 / \alpha } ,$

19

The optimal $\nu ^ { * }$ is obtained similarly using the <sup>fi</sup>rst and second order derivatives of the total cost (the derivations of the cost functions are given in Appendix-1).

## 5. Experimental setting

In this section, we explain the data sets, the type of histograms, the query sets, and the ef<sup>fi</sup>ciency metrics used to evaluate the performance of the method.

## 5.1. Data sets

The experimental setting involves both real and synthetic data sets. The real data sets are the Census2D and Census3D, which are twodimensional and three-dimensional projections of a fragment of US Census Bureau data, each having about 210 K records [5]. The Census2D has the attributes Age and Income, and the Census3D has the third attribute, number of weeks worked per year. The synthetic data sets are the Array2D and Array3D data sets, characterized by a given number of distinct values generated independently for each dimension [4]. Joint frequencies are generated from a Zipfian distribution with skewness factor Z. Table 3 summarizes the characteristics of the data sets and the parameter values for the synthetic data sets.

## 5.2. Histograms

Two different multi-dimensional histograms, the equi-depth and Phased techniques, are used for the experiments. Equi-depth or equicount histogram is the most commonly used histogram construction technique in many commercial RDBMSs. In the equi-depth histogram, contiguous ranges of attribute values are grouped into buckets enclosing the same number of tuples. We also implement the Phased technique, which uses the MaxDiff technique as the underlying partitioning strategy in one-dimension. Histogram sizes in practice depend on a number of factors in a given setting. For this reason, we show the experimental results for a range of histogram sizes, by varying the number of buckets for each histogram. In order to keep consistency across the different characteristics of the data sets, we use an equal number of partitioning in each dimension and maintain approximately the same number of buckets for all data sets.

Real and synthetic data sets used in experiments.

<table><tr><td>Real</td><td>Attribute Names</td><td>Cardinality</td></tr><tr><td>Census2D</td><td>Age, income.</td><td>210,138</td></tr><tr><td>Census3D</td><td>Age, income, weeks worked per year</td><td>210,138</td></tr><tr><td>Synthetic</td><td>Data characteristics</td><td>Parameter</td></tr><tr><td rowspan="4">Array2D &amp; Array3D</td><td>Cardinality</td><td>500,000</td></tr><tr><td>Data domain</td><td>[0,10,000]</td></tr><tr><td>Number of distinct values</td><td>60</td></tr><tr><td>Skewness</td><td>1</td></tr></table>

## 5.3. Query sets

The query sets used in our experiments are generated in a manner that would allow rigorous assessment of performance. Accordingly, two different sets, a Biased set and a Uniform set are generated. In the Biased set, query points are picked randomly from the data set in accordance with the frequencies of the values. In other words, the chance that a point is picked corresponds to its frequency in the data set. The Uniform set, on the other hand, is uniformly generated over the data domain. For each query type, a 500-query set is generated for the experiments.

## 5.4. Performance metrics

With regard to query execution time, the validity of the querymapping technique against the full sequential scan of the database has been shown in prior research [5,9]. Since our main contribution in this research is in range estimation, the focus of the experimental analysis is on the performance ef<sup>fi</sup>ciency in terms of percentage of restarts, the average excess, the percentage of database retrieved, and the average total cost. The percentage of restarts represents the proportion of queries that fail to retrieve the required k tuples in the <sup>fi</sup>rst execution using the estimated range query. The average excess measures the ratio of total tuples retrieved to the size of k. While the percentage of database measures the number of tuples retrieved in proportion to the database size, the excess ratio provides a more relevant measure of result size that can be directly contrasted to the size of k requested. The average total cost captures the cost tradeoff between a re-execution and excess results and evaluates the overall performance of the method.

## 6. Experimental results

For each of the performance metrics, we present our results for all four data sets using a default setting. The default setting includes the equi-depth histogram, Biased query set, the max distance function, and the k sizes $( k = 1 0 , k = 1 0 0 , k = 1 0 0 0 )$ ). We also compare results by type of histogram, type of query set, and the distance function used.

## 6.1. Performance analysis for default setting

Fig. 5 shows the percentage of restarts using the default setting. The most variable performance is seen for the large k value (i.e. k = 1000). For large k values, the estimation of volume overlap may involve several buckets, especially for histograms with a large number of buckets. In addition, the average data skewness may not accurately capture the actual spread of the tuples within the search bound. For the smaller k values, which are typical in top-k querying, the percentage of restarts is consistently low for all data sets and over the entire range of histogram size.

In terms of the average excess and the percentage of database retrieved, Figs. 6 and 7 also show consistently good performance for all data sets, respectively. Note that the average excess is measured relative to the size of k. As a result, the performance is relatively higher for smaller k values as opposed to the performance in terms of the percentage of database retrieved. For the Array2D, Array3D, and Census2D, not more than 4% of the database is retrieved. The same performance is seen for smaller k values for the Census3D. Even when k equals 1000, the percentage of database is not more than 8%. As the number of histogram buckets increases, the percentage of database retrieved eventually goes down below 4%, and the average excess decreases consistently across all data sets. In general, as the number of dimensions increases, the array data set has better performance than the census data set (i.e., Array3D versus Census3D).

In order to evaluate the overall ef<sup>fi</sup>ciency, we show the average total cost (Fig. 8). Because the optimal range is the result of the cost-tradeoff between restarts and excess tuples, it shows a better picture of the overall performance. For example, the high performance variability in terms of the percentage of restarts for the large k value disappears when we examine the total cost. As expected, the cost increases with an increase in the number of results requested k.

## 6.2. Performance analysis by query set

Our cost-based method is not workload-based. It is designed for a single query, regardless of whether the query point is an existing data point or a randomly chosen point. Because the strategy we follow does not involve calibrating pre-speci<sup>fi</sup>c data characteristics, performance evaluation based on a query load is not necessary for our method. Nevertheless, in order to highlight the main difference with other strategies, we present results for the two different query loads (Biased and Uniform) using the default setting with k value of 100.

![](/api/attachments/87HGHEFD/fulltext/images/d668d87cbc454fcec7aee3c327a895ee041c75ccbe526b174431a0f2740a1be5.jpg)  
Fig. 5. Percentage of restarts.

![](/api/attachments/87HGHEFD/fulltext/images/09f4ec8eaee530eb4077ad0874ca3dd83fea01431d71fbeb8908fecd951940c3.jpg)  
Fig. 6. Average excess.

![](/api/attachments/87HGHEFD/fulltext/images/9753c657351435125216966bac4c4aea4d65019cd7fa3b85daae6beebfb0982c.jpg)  
Fig. 7. Percentage of database.

![](/api/attachments/87HGHEFD/fulltext/images/fa3aa53ca8a3d2cd8bed62ac9d3f02e710be60d27a961d3a409471dc7f385113.jpg)  
Fig. 8. Average total cost.

![](/api/attachments/87HGHEFD/fulltext/images/699678b28d7e891b43066463d9817cd61acab163fb7e98da924b1b0bbb5ccf85.jpg)  
Fig. 9. Percentage of restarts.

As we see from the individual metrics (Figs. 9, 10, and 11), the Uniform query load shows relatively inferior performance, especially for the real data sets (Census2D and Census3D).

The average total cost (Fig. 12) also shows that the general performance is worse for the Uniform load, compared to the Biased load. Even if the data skewness is used, most part of the data space is not populated by data points in the real data sets. As a result, it is expected that the performance of the queries drawn uniformly from this space would generally be poor.

## 6.3. Performance analysis by histogram

In [2], it was shown that the cost-based strategy provides consistent performance across commonly used histograms, namely, the equidepth, the equi-width, and the MaxDiff techniques. This is perhaps the most desirable feature of any histogram-based technique as commercial RDBMSs vary by the histogram technique used to summarize data. In this section, we compare the performance for the multi-dimensional equi-count and Phased histogram techniques. Histogram sizes, in terms of the number of buckets allocated, are the same for both histogram techniques. Figs. 13, 14, and 15 show the performance in terms of the percentage of restarts, the percentage of database retrieved, and the average excess, respectively for $k = 1 0 0$

Overall, the performance is very close for the two histograms, which con<sup>fi</sup>rms the histogram-independent performance shown in [2]. In terms of the percentage of restarts (Fig. 13), Phased shows slightly better performance in all data sets, except for the Array2D. In terms of the average excess (Fig. 14) and the percentage of database retrieved (Fig. 15), equi-depth shows slightly better performance. Most of these variations, however, are observed for smaller histogram sizes. For almost all the data sets, the average excess and the percentage of database decline as the number of buckets increases, with the performance eventually converging for both histogram techniques. This is also another important feature that was shown in [2]. In other words, as the data distribution within histogram buckets approaches uniform with an increase in the number of buckets, the performance variability across histogram techniques diminishes.

The overall performance by histogram technique is also shown in terms of the total cost (Fig. 16). The use of the Power distribution appears to have overestimated the deviation of the data from uniformity, leading to slightly worse performance for Phased. Note that the important characteristic of the Phased histogram is its ability to minimize the frequency variance within bins. Despite this, the performance using the two histograms is very close, and the total costs get closer with an increase in the number of histogram buckets for most data sets.

![](/api/attachments/87HGHEFD/fulltext/images/caa61087a4e98834d3eb844591c5962a80ca9bba79fa441ae66ad0e823eb467a.jpg)  
Fig. 10. Average excess.

![](/api/attachments/87HGHEFD/fulltext/images/1069b3208f7427507b7bace31db0935c01eebb90a3d493995c7892a34b32df37.jpg)  
Fig. 11. Percentage of database.

![](/api/attachments/87HGHEFD/fulltext/images/c2909fa6789be7cc6bea3756573ee5ce5ed388dc97d740e8fbb661597b996d3d.jpg)  
Fig. 12. Average total cost.

![](/api/attachments/87HGHEFD/fulltext/images/764528445faaea0a21f741f48774e631f284593c3d86620b6907c4c375c39406.jpg)  
Fig. 13. Percentage of restarts.

![](/api/attachments/87HGHEFD/fulltext/images/b9cca4e6742eb6ed7e3f76ab8d3e1eb2c8c6fa6d6dde3df2a76629801af21bbc.jpg)  
Fig. 14. Average excess.

## 6.4. Performance analysis by distance function

In single dimension, the effect of the distance functions is not seen as all distance functions are the same on a single dimension. The performance implication of the distance functions is revealed as multiple dimensions are considered. One of the important aspects of this performance implication is the translation of the search distance to range queries in the form of an n-rectangle. For the max distance, the region of all points at a given distance or lower from the query point is the same n-rectangle when transformed into range queries. On the other hand, the construction of an n-rectangle over the region de<sup>fi</sup>ned by the Euclidian and Sum distance functions leads to extra tuples beyond the actual distances obtained [9]. For this reason, the Euclidian and

Sum distance functions tend to give more excess results than expected. As can be seen from Fig. 17, the max distance shows the highest percentage of restarts. On the other hand, the max distance generally gives better performance in terms of the average excess (Fig. 18) and the percentage of database (Fig. 19). In terms of the average total cost (Fig. 20), the results are consistent across the data sets, the sum and max distances leading to relatively higher and lower total cost, respectively.

## 6.5. Performance comparison with prior methods

Extensive comparison of the performance of the cost-based strategy with that of the dynamic workload-based (DWBS) strategy [5] was shown in [1] and [2] for various settings. The comparison showed that the cost-based strategy not only avoids the need to calibrate workloads on speci<sup>fi</sup>c database contents, but also performs at least as well as the DWBS. The DWBS was used as the benchmark method for the cost-

![](/api/attachments/87HGHEFD/fulltext/images/f8dcb3cd3131994158e7ab86dca069a1a4c8d7e1334b5d66cdac82a1ffcdd660.jpg)  
Fig. 15. Percentage of database.

![](/api/attachments/87HGHEFD/fulltext/images/2bba4b3103b646bf91397f2f483bd586f04edd3ec49d76213bd6067609093151.jpg)  
Fig. 16. Average total cost.

based strategy due to its substantially improved performance over the histogram-based heuristics proposed in [9]. In addition, the ef<sup>fi</sup>ciency advantage of the query-mapping approach in terms of execution time against the methods that require sequential scans was shown in prior research [5,9]. In particular, the query-mapping approach assumes index con<sup>fi</sup>gurations that are available in RDBMSs. As a result, the focus of performance evaluation in the query-mapping methods has been on ef<sup>fi</sup>ciency metrics directly related to range estimation. Therefore, in this paper we emphasize the performance advantage of incorporating data skewness in range estimation and show the comparative performance against the baseline cost-based strategy [1]. For the purpose of comparison, we label the baseline cost-based strategy [1] as CBS and the cost-based strategy with data skewness as CBS-Adjusted. We use the default setting in our experiment which includes the equicount histogram, max distance function, Biased query set, and k value of 100. We report the computational results for CBS and CBS-Adjusted in terms of the percentage of restarts, the average excess, the percentage of database retrieved, and the total cost of executing queries. For a visible comparison of performance, we plot the computational results from all four data sets side by side, and consider both small and large histogram allocations for summary statistics.

As Fig. 21(a) shows, the consideration of volume overlap and data skewness has improved the performance of the cost-based strategy in terms of the percentage of restarts. The allocation of a smaller histogram provides summary statistics at coarser levels of detail. Consequently, using histogram buckets as atomic and ignoring the distribution of the local data can lead to rough estimations. Note that the percentage of restarts for the baseline cost-based strategy (CBS) is relatively high for the small histogram. On the other hand, as Fig. 21(b) shows, the allocation of a larger histogram has led to a much better performance in terms of restarts for both methods, with the CBS performing slightly better. However, the lower percentages of restarts for the CBS were obtained at the expense of much higher excess tuples for all data sets as shown in Fig. 22(b). Note also that the percentage of restarts for the CBS-Adjusted is 7% for Census3D, and below 4% for the rest of data sets.

![](/api/attachments/87HGHEFD/fulltext/images/6ebd3ca64ed482cc4bf88766beebe4bcf06445564b3e106d4102e7619392b6fe.jpg)  
Fig. 17. Percentage of restarts.

![](/api/attachments/87HGHEFD/fulltext/images/8be9d56a18a27a9c049282e03514a821cb3a3aee839cf45dc493afe41a9459a8.jpg)  
Fig. 18. Average excess.

For the small histogram, the CBS-Adjusted is more ef<sup>fi</sup>cient both in terms of restarts and excess tuples, with the exception of the average excess for Census3D (see Fig. 22(a)). Yet the cost comparison in Fig. 24(a) shows about the same performance for both methods for Census3D. Although estimating volume overlap and data skewness overcome the limitation of the Uniform distribution assumption for histogram construction, it is still challenging for real life data sets such as the census data. For example, one of the attributes of the census data sets is income, which has natural clusters of values. This makes the estimation of volume overlap and data skewness relatively less accurate, particularly when the number of dimensions in this type of data set increases.

The performance comparison in terms of the percentage of database retrieved also shows the ef<sup>fi</sup>ciency advantage of incorporating data skewness in the range estimation. Over all, CBS-Adjusted shows a better performance for all cases, except for Census3D with small histogram allocation. For the small histogram allocation, the percentage retrieved across all the data sets is below 2.5% for CBS-Adjusted versus 4% for CBS (see Fig. 23(a)). For the large histogram allocation, the percentages are below 1.5% and 5.5% for CBS-Adjusted and CBS, respectively (see Fig. 23(b)).

Finally, the key strength of the cost-based strategy over other querymapping techniques is its ability to tradeoff con<sup>fl</sup>icting ef<sup>fi</sup>ciency objectives (i.e., minimizing restarts versus minimizing excess tuples retrieved) in the range estimation process. Therefore, the average total cost (Fig. 24(a) and (b)) provides a more comprehensive view of the aggregate performance of the two methods. Both Fig. 24(a) and (b) clearly show that CBS-Adjusted provides top-k retrieval with lower total cost. Therefore, the above comparisons of the two methods using the different performance metrics reveal the ef<sup>fi</sup>ciency advantage of incorporating data skewness in the cost-based range estimation.

## 7. Conclusion

This paper extends the cost-based range estimation method for top-k retrieval by incorporating data skewness in multi-dimensional

![](/api/attachments/87HGHEFD/fulltext/images/371e37f7b9bd52862db40a2f3a042401ce2b462590404a712d0317b6f4bc852b.jpg)  
Fig. 19. Percentage of database.

![](/api/attachments/87HGHEFD/fulltext/images/a9d51cc1b05bc0269321b0a243937dd71174dfb508d4a92cf41430ddf5e34fbb.jpg)  
Fig. 20. Average total cost.

![](/api/attachments/87HGHEFD/fulltext/images/d2c052a7404aa7182cac746af1326d8cddbe0cd9ac62824d2854a3adb84bc85f.jpg)  
(a) Histogram Size - Small

![](/api/attachments/87HGHEFD/fulltext/images/188021f3359491c2b559ce82bb220abcd3d00746f7e5f8eced04c66a39ee8686.jpg)  
(b) Histogram Size - Large  
Fig. 21. Performance comparison using percentage of restarts.

histograms. We utilize existing techniques to estimate the volume overlap of buckets and data skewness to account for the deviation of the underlying data from the Uniform distribution assumption. By estimating data skewness for a given search bound in the cost-optimization model, we present an extension of the basic framework to non-Uniform tuple density. Several experiments are conducted using two-dimensional and three-dimensional real and synthetic data sets and using the equidepth and Phased histogram construction techniques. The method is evaluated using Biased and Uniform query sets and different performance metrics.

![](/api/attachments/87HGHEFD/fulltext/images/87a086be37e1b1b5e8866611369d24692cdf4d17b5cc06fd3a495a122889bb19.jpg)  
(a) Histogram Size - Small

![](/api/attachments/87HGHEFD/fulltext/images/d1ece4212955675d7289281fb7572676849815950437be042aab1001e4444720.jpg)  
(b) Histogram Size - Large  
Fig. 22. Performance comparison using average excess.

![](/api/attachments/87HGHEFD/fulltext/images/9a6417688b7912f0c6bf90f801a7cc4677f2a9b36c79ba03a995354c870c8c99.jpg)  
(a) Histogram Size - Small

![](/api/attachments/87HGHEFD/fulltext/images/c2c6a52de4a523b085bcc9b98442f12707bf8df7f457f3ea04bbe0859fa87cc2.jpg)  
(b) Histogram Size - Large  
Fig. 23. Performance comparison using percentage of database.

![](/api/attachments/87HGHEFD/fulltext/images/be6508394a43a23693167e55f066bc1c11bedd1b006e8690436a2c0b30d00b33.jpg)  
(a) Histogram Size - Small

![](/api/attachments/87HGHEFD/fulltext/images/7da4c4ea79c750c6fbc2642901224ebc497de6043fbcb6e48a677b47db22064d.jpg)  
(b) Histogram Size - Large  
Fig. 24. Performance comparison using average total cost

The results con<sup>fi</sup>rm many of the important insights obtained from the one-dimensional setting and further shed signi<sup>fi</sup>cant insights in a generalized setting. In general, the problem environment and the approach presented here become more challenging as the number of dimensions increases. More importantly, the ability to obtain the required information from multi-dimensional histograms becomes more challenging as the number of dimensions increases. In most cases, however, queries involve few important attributes. Thus, using multi-dimensional histograms in lower dimensions provides reasonably good performance as demonstrated by the results obtained for two-dimensional and threedimensional settings. Furthermore, the performance comparison of the method with the baseline cost-based strategy clearly shows the ef<sup>fi</sup>ciency advantage of incorporating data skewness in the range estimation.

Although signi<sup>fi</sup>cant progress has been made in developing ef<sup>fi</sup>cient methods for top-k retrieval, there are limitations that can be addressed in future research. First, the scope of the current research can be expanded in many ways. One open research issue deals with the nature of summary statistics used in the range estimation procedure. Prior research as well as this paper used commonly known histogram structure to summarize relations. Future research can consider other approaches (e.g., learning techniques) to improve the quality of the database pro<sup>fi</sup>le used in the range estimation procedure. In addition, future research can explore more scalable techniques for estimating data skewness. Other avenues for future research include expanding the scope of distance functions, the type of top-k application, and the nature of data to deal with.

Finally, our cost-based framework and the formulation of relevant processing costs involve assumptions and constraints that are simpli-<sup>fi</sup>ed for ease of exposition. Future research can address these limitations in accordance with potential advancements in the operational constraints of RDBMSs as well as the complexity involved in mathematical modeling.

Appendix 1. Derivation of costs: model with data skewness

I. Cost of excess:

The cost of excess is given by:

$$
C (e x c e s s) = \left\{ \begin{array}{l l} (k + N. v ^ {\alpha} - k p) \log_ {2} (k + N. v ^ {\alpha} - k p) - k \log_ {2} k, & \text { if } N. v ^ {\alpha} > k p \\ 0, & \text { otherwise } \end{array} \right..
$$

The derivative of C(excess) w.r.t. v is given by:

$$
\begin{array}{l} \frac {d}{d v} C (e x c e s s) = \left(\alpha N v ^ {\alpha - 1}\right). \frac {\ln \left[ k + v ^ {\alpha} N - k _ {p} \right]}{\ln (2)} \\ + \frac {\left(\alpha N v ^ {\alpha - 1}\right)}{\ln (2) . \left[ k + v ^ {\alpha} N - k _ {p} \right]}. (k + v ^ {\alpha} N - k _ {p} ] \end{array}
$$

$$
C ^ {\prime} (e x c e s s) = \frac {\alpha N v ^ {\alpha - 1}}{\ln (2)} \left[ \ln \left(k + v ^ {\alpha} N - k _ {p}\right) + 1 \right].\tag{A - 1}
$$

## II. Cost of restart:

The cost of restart is given by:

$$
C (r e s t a r t) = (T + o). \sum_ {j = 0} ^ {k _ {p} - 1} \binom {N} {j} v ^ {\alpha . j} \bigl (1 - v ^ {\alpha} \bigr) ^ {N - j}.
$$

elsewhere

The cost of restart can be also written as:

$$
\int_ {0} ^ {v ^ {\alpha}} u ^ {k p - 1} (1 - u) ^ {N - k p} d u   C (\text { restart }) = (T + o) - (T + o) \frac {}{0} \left[ \frac {(k p - 1) ! (N - k p) !}{N !} \right]
$$

$$
C (\text { restart }) = (T + o) - k p \binom {N} {k p} (T + o) \int_ {0} ^ {v ^ {\alpha}} u ^ {k p - 1} (1 - u) ^ {N - k p} d u.
$$

The derivative of C(restart) w.r.t. v is given by:

$$
C ^ {\prime} (\text { restart }) = - k p \binom {N} {k p} (T + o) \left[ v ^ {\alpha \left(k _ {p} - 1\right)} \left(1 - v ^ {\alpha}\right) ^ {N - k p} \right]. \alpha v ^ {\alpha - 1}. \tag {A-2}
$$

III. Total cost:

Using Eq. (A-1) and (A-2), the derivative of the total cost w.r.t. v is given by:

$$
T C ^ {\prime} (v) = \left\{ \begin{array}{l} \frac {\alpha N v ^ {\alpha - 1}}{\ln (2)} [ \ln (k + v. N - k _ {p}) + 1 ] - k _ {p} \binom {N} {k _ {p}} (T + o) \\ . [ v ^ {\alpha (k _ {p} - 1)} (1 - v ^ {\alpha}) ^ {N - k p} ]. \alpha v ^ {\alpha - 1}, \text {if} \hat {v} <   v \leq 1 \\ - k _ {p} \binom {N} {k _ {p}} (T + o). [ v ^ {\alpha (k _ {p} - 1)} (1 - v ^ {\alpha}) ^ {N - k p} ]. \alpha v ^ {\alpha - 1}, \end{array} \right.
$$

where $\hat { \boldsymbol { v } } = \left( k _ { p } / N \right) ^ { 1 / \alpha } .$

A  3

The second order derivative of the total cost w.r.t. v is given by:

$$
T C ^ {\prime \prime} (v) = \left\{ \begin{array}{l} \frac {N v ^ {\alpha - 2} \alpha}{\ln (2)} [ \frac {N v}{(k + v N - k _ {p})} + (\alpha - 1) (1 + \ln (k + v N - k _ {p})) ] + \\ \alpha k _ {p} \binom {N} {k _ {p}} (T + o) v ^ {k _ {p} \alpha - 2} (1 - v ^ {\alpha}) ^ {N - k _ {p} - 1} (1 - \alpha k _ {p} + v ^ {\alpha} (\alpha N - 1)) \\ \alpha k _ {p} \binom {N} {k _ {p}} (T + o) v ^ {k _ {p} \alpha - 2} (1 - v ^ {\alpha}) ^ {N - k _ {p} - 1} (1 - \alpha k _ {p} + v ^ {\alpha} (\alpha N - 1)), \end{array} \right.\tag{elsewhere}
$$

where $\hat { \boldsymbol { v } } = \left( k _ { p } / N \right) ^ { 1 / \alpha }$

A  4

## References

[1] A. Ayanso, P.B. Goes, K. Mehta, A cost-based range estimation for mapping top-k selection queries over relational databases, Journal of Database Management 20 (4) (2009) 1–25.

[2] A. Ayanso, P.B. Goes, K. Mehta, A practical approach for ef<sup>fi</sup>ciently answering top-k relational queries Decision Support Systems 44 (1) (2007) 326–349

[3] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, ACM Press, New York, 1999.

[4] N. Bruno, S. Chaudhuri, L. Gravano, Performance of Multiattribute Top-k Queries on Relational Systems, Technical Report, CUCS-021-00, Columbia University, 2000.

[5] N. Bruno, S. Chaudhuri, L. Gravano, Top-k selection queries over relational databases: mapping strategies and performance evaluation, ACM Transactions on Database Systems 27 (2) (2002) 153-187

[6] S.W.K. Chan, Beyond keyword and cue-phrase matching: a sentence-based abstraction technique for information extraction, Decision Support Systems 42 (2) (2006) 759-777

[7] Y. Chang, I.D. Bergman, V. Castelli, C. Li, M. Lo, J.R. Smith, The onion technique: indexing for linear optimization queries, Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data. 2000, pp. 391–402.

[8] K.C. Chang, S. Hwang, Minimal probing: supporting expensive predicates for top-k queries, Proceedings of the 2002 ACM SIGMOD International Conference on Management of Data, 2002, pp. 346–357.

[9] S. Chaudhuri, L. Gravano, Evaluating top-k selection queries, Proceedings of the 25th International Conference on Very Large Data Bases, 1999, pp. 397–410.

[10] C.-M. Chen, Y. Ling, A sampling-based estimator for top-k selection query, Proceedings of the 18th International Conference on Data, Engineering, 2002, pp. 617–627.

[11] S. Christodoulakis, Implications of certain assumptions in database performance evaluation, ACM Transactions on Database Systems 9 (2) (1984) 163–186.

[12] G. Das, D. Gunopulos, N. Koudas, D. Tsirogiannis, Answering top-k queries using views, Proceedings of the 32nd International Conference on Very large data bases, 2006, pp. 451–462.

[13] D. Donjerkovic, R. Ramakrishnan, Probabilistic optimization of top N queries, Proceedings of the 25th International Conference on Very Large Data Bases, 1999, pp. 411–422.

[14] R. Fagin, Fuzzy queries in multimedia database systems, Proceedings of the seventeenth ACM SIGACT-SIGMOD-SIGART symposium on Principles of database systems, 1998, pp. 1–10.

[15] C. Faloutsos, I. Kamel, Relaxing the uniformity and independence assumptions using the concept of fractal dimension, Journal of Computer and System Sciences 55 (2) (1997) 229–240.

[16] W. Fan, M. Gordon, P. Pathak, On linear mixture of expert approaches to information retrieval, Decision Support Systems 42 (2) (2006) 975–987.

[17] X. Han, J. Li, D. Yang, Supporting early pruning in top-k query processing on massive data, Information Processing Letters 111 (11) (2001) 524–532.

[18] V. Hristidis, N. Koudas, Y. Papakonstantinou, PREFER: a system for the ef<sup>fi</sup>cient execution of multi-parametric ranked queries, Proceedings of the 2001 ACM SIGMOD International Conference on Management of Data, 2001, pp. 259–270.

[19] I.F. Ilyas, W.G. Aref, A.K. Elmagarmid, H.G. Elmongui, R. Shah, J.S. Vitter, Adaptive rank-aware query optimization in relational databases, ACM Transactions on Database Systems 31 (4) (2006) 1257–1304.

[20] I.F. Ilyas, G. Beskales, M.A. Soliman, A survey of top-k query processing techniques in relational database systems, ACM Computing Surveys 40 (4) (2008)(Article 11).

[21] S.H. Kwok, J.L. Zhao, Content-based object organization for ef<sup>fi</sup>cient image retrieval in image databases, Decision Support Systems 42 (3) (2006) 1901–1916.

[22] C. Li, K.C.-C. Chang, I.F. Ilyas, Supporting ad-hoc ranking aggregates, Proceedings of the 2006 ACM SIGMOD International Conference on Management of Data, 2006, pp. 61–72.

[23] V.A.G.U.E. Motro, A user interface to relational databases that permits vague queries, ACM Transactions on Information Systems 6 (3) (1988) 187–214.

[24] M. Muralikrishna, D.J. DeWitt, Equi-depth multi-dimensional histograms, Proceedings of the 1988 ACM SIGMOD International Conference on Management of Data, June 1–3, Chicago, Illinois, 1988, pp. 28–36.

[25] G. Piatetsky-Shapiro, C. Connell, Accurate estimation of the number of tuples satisfying a condition, Proceedings of the 1984 ACM SIGMOD International Conference on Management of Data, 1984, pp. 256–276.

[26] V. Poosala, Y.E. Ioannidis, Selectivity estimation without the attribute value independence assumption, Proceedings of the 23rd International Conference on Very Large Databases, 1997, pp. 486–495.

[27] V. Poosala, Y.E. Ioannidis, P.J. Haas, E.J. Shekita, Improved histograms for selectivity estimation of range predicates, Proceedings of the 1996 ACM SIGMOD International Conference on Management of Data, 1996, pp. 294–305.

[28] P. Tsaparas, T. Palpanas, Y. Kotidis, N. Koudas, D. Srivastava, Ranked join indices, International Conference on Data Engineering, 2003, pp. 277–288.

Anteneh Avanso is an Associate Professor of Information Systems at the Goodman School of Business, Brock University, Canada. He received his Ph.D. in Information Systems from the University of Connecticut in 2004. His research interests are in data management, business analytics, electronic commerce, and electronic government. His research is published/forthcoming in Decision Sciences, Decision Support Systems, European Journal of Operational Research, Journal of Database Management, and Communications of the AIS, among others.

Paulo B. Goes is the Salter Distinguished Professor in Technology and Management, and Department Head of Management Information Systems at the Eller College of Management, the University of Arizona. He received his Ph.D. from the University of Rochester in 1991. His research interests are in the areas of design and evaluation of models for e-business, emerging technologies, online auctions, database technology and systems, and technology infrastructure. His research has appeared in many leading journals includ ing Management Science, MISQ, ISR, Journal of MIS, Operations Research, Decision Sciences, Decision Support Systems, INFORMS Journal on Computing, IEEE Transactions on Communications, IEEE Transactions on Computers, among others. Dr. Goes is currently Editor-In-Chief of MISQ and Senior Editor at Decision Sciences. He has served as Senior Editor Information Systems Research, and Associate Editor of Management Science, Decision Sciences, Journal of Management Information Systems, and the INFORMS Journal on Computing. In 2004 he co-chaired WITS, the Workshop on Information Technology and Systems, and he was the WITS Organization President

Kumar Mehta is an Associate Professor of Management Information Systems and MS Technology Management Academic Director at George Mason University's School of Management. He received his Ph.D. from University of Illinois at Chicago in 2002. His research interests include Data Mining, Information Retrieval and Agent-based Computational Modeling. His research has appeared in Decision Support Systems, Journal of Retailing, Journal of Database Management, and Information Technology and Management, among others.
