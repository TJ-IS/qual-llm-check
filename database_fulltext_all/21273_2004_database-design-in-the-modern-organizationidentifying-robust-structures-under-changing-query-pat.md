---
otero_id: 21273
otero_key: "ZQ2BT4T2"
title: "Database design in the modern organization—identifying robust structures under changing query patterns and arrival rate conditions"
authors: "Andrew N.K. Chen; Paulo B. Goes; Alok Gupta; James R. Marsden"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00048-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Database design in the modern organization—identifying robust structures under changing query patterns and arrival rate conditions

Andrew N.K. Chen<sup>a</sup>, Paulo B. Goes<sup>b</sup>, Alok Gupta<sup>c</sup>, James R. Marsden<sup>b,</sup>\*

<sup>a</sup> Arizona State University, USA

<sup>b</sup> Department of Operations and Information Management, School of Business Administration, University of Connecticut, 2100 Hillside Road, Storrs, CT 06269, USA

<sup>c</sup> University of Minnesota, USA

Received 1 March 2002; accepted 1 June 2002

Available online 10 April 2003

## Abstract

We summarize the problem tackled here in the following way: Given a modern database application environment, how can we identify and select the database structure that provides robust performance across changing query patterns and arrival rate conditions? We demonstrate the importance of investigating the underlying relationships and then utilize this information in formulating robust structures. Our work is pre-theory in the philosophy of science sense. That is, the careful identification and observation of relationships will subsequently be utilized in formulating a testable theory of the development of robust database structures under dynamic query patterns and arrival rates. Our first step in providing a database design or ‘‘structure selection’’ method is to determine potential good performers among different database structures. These potential good performers are selected and analyzed across arrays of query patterns. The next step is to identify database structures that are robust structures, that is good performers across the different types of query patterns and arrival rate levels. The presentation includes illustrations of the determination of actual query pattern processing times and the use of these times within a queuing analysis. In fact, for the database layout analyzed, application of our methods demonstrates the existence of such robust database structures. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Database design; Queueing; Query processing; Query pattern

## 1. Introduction

In the last decade, advances in information technology paired with the complex global business environment have created both the incentives and expectations that database systems will efficiently handle a wide variety of query patterns—combinations of queries of different complexity. Consolidation of corporate information has resulted in diverse populations of internal and external users that may seek significantly different information sets from a given database. For example, many companies already use databases to create customized web pages and dynamic content on their intranet and extranet for their employees, business partners and customers. The breadth of those accessing these pages and their linked content results in a variety of query patterns that the underlying database must handle. In addition, a database may operate under conditions ranging from little or no congestion to severe congestion. These arrival rate conditions can vary significantly because databases have become integrated parts of information delivery both inside and outside an organization. The demand for database services is less predictable and controllable since availability of database information on a wide variety of platforms, such as the web, means that a significant portion of demand may arise from external sources that seek responses to diverse sets of queries.

It is widely recognized that a normalized database structure does not perform well in such an environment [1,2]. Data warehouses and data mining have been the most notable advances to deal with the sheer volume of data that many corporate databases contain. However, these techniques focus on maintaining data to identify relevant information for specific purposes. The focus of this paper is on a different, but very important, aspect relating to data retrieval and usage—new database design methods in the modern organization. Of special interest here is the identification of database structures that perform robustly (consistently well) over a wide variety of query patterns and arrival rate conditions.

A database structure represents a schema of a database with a specific logical design. In this study, on the premise of equivalent information content, different database structures are derived by denormalizing the initial database structure in third normal form (3NF). That is, based on the original normalized database, we construct different structures with lossless natural join operations. The resulting structures might have different numbers of tables but all must posses the same information content. It is well known that such denormalization can be effectively used to improve the performance quality of a database design [13] and query processing [11,12].

It is futile (e.g., Ref. [3]) to attempt to find a single database structure that is best under all conditions. Instead, we seek to identify database structures that perform robustly. We classify a database structure as a good performer if, for a given query, it performs competitively with the best database structure for that query with respect to processing time. We define a database structure to be a robust structure if it is classified as a good performer across the different types of query patterns and arrival rate levels.

It may appear that what follows is a-theoretic, but quite the opposite is true. Our work here is best termed pre-theory in the philosophy of science sense. Our goal is to utilize careful determination and observation of important relationships in order to subsequently develop a testable theory (see the lengthy discussions in Refs. [7,14,15], about the use and importance of the results of controlled laboratory experimental in theory formulation). Thus, we demonstrate the importance of investigating the underlying relationships and utilizing the resulting information in formulating robust structures. The careful identification and observation of relationships will subsequently be utilized in formulating a testable theory of the development of robust database structures under dynamic query patterns and arrival rates.

Fig. 1 presents an overview of our approach. The starting point is the universe of physical schemas (which we call database structures) that can be used to represent the logical schema of the database application. The logical schema captures the information content of the application environment. Current guidelines for normalized database design are prescriptive in nature and are aimed at choosing one physical schema for specific well-defined query instances. For a highly dynamic environment that allows for extreme variation in the nature and frequency of database queries, we propose an approach that is data driven, experimental and inductive in nature.

As Fig. 1 indicates, out of the universe of possible physical schema solutions, which are implemented in a laboratory environment, an initial set of solutions is chosen. The structures in this working pool are the ones that perform very well (in terms of processing times) across the entire range of queries that are possible in the application environment. The next stage is the stress testing of the candidate solutions of the working pool to emulate a wide variety of operating environments, which are represented by diverse query patterns of different complexity levels, and various degrees of system utilization.

Because of the number of components involved in answering a query, a major challenge in modeling database systems has been the ability to assess system time—processing time plus waiting time—for a query. We develop and illustrate methods that yield system

![](/api/attachments/ZQ2BT4T2/fulltext/images/124adccfc8dc71e38fc60c38106f082bd77404fc722ec6615b6986b97d166269.jpg)  
Fig. 1. Identification, evaluation and selection process.

time by integrating actual query processing time measurements into a queueing model. This allows for a rich analysis of commonly occurring situations—changing query patterns and arrival rate conditions—in the operation of modern business systems. In the extensive use of queueing models to evaluate performance of computer systems, two broad approaches have been followed. In theoretical analyses, assumed distribution and relationships are used to derive closed-form solutions for ranges of system performance parameters such as system utilization, average system time and average number of transactions in a system. Since it is difficult to realistically model complex computing systems theoretically, researchers have turned to a second approach—discrete event simulation. In this approach, a complex system is modeled as a collection of several distinct interacting components. However, such simulation analysis requires specific assumptions about both the behaviors of individual components and their interactions. A good overview of techniques for performance analysis of computer systems can be found in Ref. [8]. As explained below, our approach does not require such assumptions since we are able to collect performance data directly using the actual database structures. Using actual processing times, we investigate and compare the performance of alternative structures under various query patterns and arrival rate conditions using a queueing model with random arrivals of queries of various complexity levels.

In our approach: (i) the performance data needs to be collected only once and (ii) simulation modeling of database structures and components is not necessary since the performance data can be collected using the actual database. Using our methods, the advantages of simulation modeling such as measuring the effects of a change of query patterns and/or arrival rates can be computationally realized without the requirement of detailed speculative modeling of the database environment. We summarize the problem tackled here in the following way: Given a modern database application environment, how can we identify and select the database structure that provides robust performance across changing query patterns and arrival rate conditions? The steps we follow to answer this question are:

(1) construct feasible database structures that are potential good performers with necessary information content for the application environment;

(2) for each of these potential good performers, measure processing time for each query type relevant to the application environment in a nocongestion situation;

(3) identify database structures as the top performers (among these potential good performers) across a wide range of query types;

(4) evaluate the performance of the identified database structures under various query patterns and arrival rate conditions using a queueing model with random arrivals of queries of various complexity levels where service times (i.e., system time) are the actual processing times as measured in step 2 plus waiting times; identify ‘‘robust performers’’ across performance measures and arrival rate levels; and

(5) evaluate the performance of the identified database structures for groupings or classifications of query patterns based upon King’s [9] ‘‘selectivity factor’’. Identify ‘‘robust performers’’ across complexity level groupings.

Note that the first three steps of this five-step process are part of our initial ‘‘brute-force’’ approach. If results reported here continue to hold across additional experimental investigations, then applying our approach in real world settings should be able to begin with step (4) utilizing the set of candidate structures. As discussed below, our database design consists of seven tables, which falls toward the upper end of the complexity of the three examples (four tables, TCP-A, a bank; four tables, TCP-B, a bank; and nine tables, TCP-C, supplier of wholesale parts) presented in Chapters 2 and 3 of Gray’s benchmark treatise [5]. We return to this discussion in Section 4.1 below.

The remainder of this paper follows the ordering of the five steps listed above, beginning with details of steps 1 and 2 relating to the database application environment of our experiment (Section 2). Also in Section 2, based on lowest total processing time for our benchmark queries, we identify the top five performing database structures among the 96 database structures possible in our experiment. We analyze performance of these five database structures together with a generic normalized database structure (six in total). Section 3 discusses use of a M/G/1 queueing model to perform arrival rate analysis. Detailed description of our computation experiment is also provided in this section. Section 4 presents the results and analyses including the identification of robust structures and the impact of arrival rate levels on database design or structure selection. Section 5 summarizes this work and discusses possible applications, which include view materialization decisions in data warehousing applications. The concluding remarks also emphasize the use of our work here as informational foundations in the development of a testable theory of robust database structure design.

## 2. Database application environment

Given a conceptual model representing a database application, the first step in our method is to identify the set of alternative database structures that contain the necessary information. For illustration purposes, we consider an example database layout represented in Fig. 2.

The corresponding normalized database structure (named DBS6 in this paper) having seven tables is provided in Fig. 3.

In this study, we consider 96 alternative database structures. These 96 structures are enumerated by considering all possible unique natural joins of one or more of the tables presented in Fig. 3. For simplicity, we do not consider other types of join operations and materialized views. Each of these 96 structures has equivalent information content under the assumption that the natural join operations of forming these database structures are lossless joins. That is, these database structures may have different numbers of denormalized tables but they have the same actual information content. One of the 96 is the normalized structure in Fig. 3, which we refer to as DBS6. Fig. 4 provides several examples and descriptions of the 96 resulting database structures.

![](/api/attachments/ZQ2BT4T2/fulltext/images/bdaa931f53bad7b5c92ac1bf55763949b47c6fa6ca9309b9bfedfdd4232dcf36.jpg)  
Fig. 2. Database layout.

![](/api/attachments/ZQ2BT4T2/fulltext/images/e96704a8c498dafc683ff6be9ef0a9967a7611766cbd93eb81ea8151162c905a.jpg)  
Fig. 3. Original normalized database structure (DBS6) with seven relations (tables).

All attributes that are primary keys or foreign keys in the tables of the normalized database structure keep their indices in all database structures. To populate the tables, we randomly generate numerical values with the size of tables ranging from 625 records to 6250 records. The smallest table in DBS6, the normalized structure, has 140 KB while the largest table in DBS6 has 570 KB. In our simulation, we ran all queries on each different database structure. In addition, all structures have ‘‘equal setup’’—the same storage scheme, indices, and information content. The variation in structure (i.e., the number of tables and tables combined from different base tables) is the only difference. Query performance of a database structure depends on many different factors. Setting indices on non-key attributes and applying specific storage schemes can improve query-processing speed. However, in this study, we do not attempt to find the ‘‘best’’ index arrangement or storage scheme to ‘‘reduce’’ query processing time for each database structure, procedures that may be important when the query set and arrival rates are fixed and known. Our goal is to investigate a design process that yields robust performance in the face of changing query patterns and uncertain arrival rates.

![](/api/attachments/ZQ2BT4T2/fulltext/images/7b7f37d5906218e462d7c93f36808c9e37880721c2e759f17022ae941be40752.jpg)  
Fig. 4. Six examples of the 96 resulting database structures.

Given our method demonstration purpose, we set the database application as retrieval only. The query set is formulated as SELECT hfieldsi FROM htables WHERE hcriteriai. Number of fields, number of tables and number of criteria in a query are randomly generated. Number of fields ranges from 1 to 10, number of tables from 7 to 7 and number of criteria from 1 to 5. Number of tables refers to the total number of tables that would have to be accessed in the normalized database structure (DBS6) to answer the query. Each criterion is constructed using the operators ‘‘ < ’’, ‘‘>’’, ‘‘ <sub>z</sub> ’’, ‘‘ V ’’ or ‘‘ = ’’. Multiple criteria used in each query are concatenated using the ‘‘AND’’ operator.

Following this process, we generate a total of 520 queries and each is run individually on each of the 96 database structures. The 520 queries generated for our simulation include all 52 possible ‘‘query types’’ that can be posted to our example database layout. These ‘‘query types’’ include queries that need to access data from a single table, from joining two tables, from joining three tables and so forth. By generating and running queries from all query types, it allows us to collect data to find out if specific database structures are best at processing specific ‘‘types’’ of queries. With this ‘‘full information’’ approach, we are also able to study any subsets such as queries involving the joining of four tables or queries involving the joining of just two tables. In an actual business setting, the identification of most frequent query patterns can be used to narrow our search for a robust structure to that subset.

Database structures are implemented using Oracle 8 under Windows NT 4.0 running on identical Dell servers with Pentium II 233 MHz processors. This process provides processing time values that are utilized in the computational experiments we describe in Section 3.

Our database design or robust structure selection process begins by first identifying potential good performers by measuring the aggregate performance for each of the 96 database structures. Based on lowest total processing time for the 520 queries, we identify the top five performing database structures (see DBS1 to DBS5 in Fig. 4) as the ‘‘potential good performers’’. Table 1 provides information on processing times of these five database structures, the original normalized database structure (DBS6), and various other database structures that represent the 25th, 50th, 75th, 87th and 100th percentile of performance. The 87th percentile value is included since the performance deteriorated significantly above this percentile.

Using the overall set of 520 different queries explained above, we next generate a set of query patterns that a database may have to process. Instead of purely random draws from the 520 queries to create a query pattern, we first classify or group queries by similarity in complexity levels. This grouping of queries by ‘‘processing difficulty’’ enables us to investigate the performance of alternative database structures across these complexity levels. We use King’s selectivity factor [9] to classify the complexity of our queries since it provides the best correlation between processing time and complexity (see Ref. [3] for a detailed investigation of alternative complexity classification methods such as number of joins, number of selection criteria and number of attributes requested in a query). Selectivity factor is a continuous measure between 0 and 1, and is the expected proportion of tuples from a table to be selected for the output for a query. The selectivity factor for a query is defined as a continuous variable that combines the cardinality of base relation(s) from which a query extracts information, the domain(s) of attribute(s) that the query requests for information and the degree of restriction of selection criteria in the query. If a query has one selection criterion, the proportion of data that would be extracted from an attribute’s domain (data range) is the query’s selectivity factor. When a query has more than one selection criterion, the product of the proportions of data that would be extracted from the corresponding attribute’s domain for each selection criterion is the query’s selectivity factor. We divide the 0 – 1 interval into five subintervals to simplify the analysis and presentation. The five subintervals are not created using uniform distance, but chosen in an attempt to have each interval contain roughly an equal number of queries and so that the response characteristics of representative databases are of the same order for queries in a given subinterval (for details, see Ref. [3]). Applying this classification process actually results in 102 queries in complexity level 1, 148 queries in complexity level 2, 103 queries in complexity level 3, 88 queries in complexity level 4 and 79 queries in complexity level 5.

Information of processing times of the six database structures studied in this paper and other relevant database structures

<table><tr><td>Database structure</td><td>Total processing time for all 520 queries (h)</td><td>Overall rank among 96 database structures</td></tr><tr><td>DBS1</td><td>0.383</td><td>1</td></tr><tr><td>DBS2</td><td>0.429</td><td>2</td></tr><tr><td>DBS3</td><td>0.440</td><td>3</td></tr><tr><td>DBS4</td><td>0.460</td><td>4</td></tr><tr><td>DBS5</td><td>0.494</td><td>5</td></tr><tr><td>DBS6 (normalized)</td><td>0.769</td><td>19</td></tr><tr><td>DBS7</td><td>0.871</td><td>24 (25th percentile)</td></tr><tr><td>DBS8</td><td>1.403</td><td>48 (50th percentile)</td></tr><tr><td>DBS9</td><td>3.065</td><td>72 (75th percentile)</td></tr><tr><td>DBS10</td><td>6.187</td><td>84 (87th percentile)</td></tr><tr><td>DBS11</td><td>108.543</td><td>96 (longest)</td></tr></table>

## 2.1. Query patterns

We define a query pattern as the five-component vector $( L _ { 1 } , L _ { 2 } , L _ { 3 } , L _ { 4 } , L _ { 5 } )$ where $L _ { i } { = } 0 ,$ , 1 or 2 and represents the weighting factor of each complexity level. For example, a vector (1,0,2,0,0) would have one-third complexity level 1 queries, two-thirds complexity level 3 queries and no queries from complexity level 2, 4 or 5. Counting all combinations of 0, 1 and 2 for each query complexity level in the forming of query patterns, mathematically we should have $3 ^ { 5 }$ query patterns (243 query patterns). However, after we exclude redundant and trivial patterns, we have 211 query patterns to investigate in our experiments. For example, the (0,0,0,0,0) pattern is excluded.

The (1,1,1,1,1) pattern is the same pattern as the (2,2,2,2,2) pattern because each has 20% of the queries from each complexity level. Similarly, the (1,1,0,1,0) pattern is the same pattern as (2,2,0,2,0) pattern because each has one-third of the queries from complexity levels 1, 2 and 4 and none from complexity levels 3 and 5. Once we define the query tuple, the next challenge is to make sure that from each query complexity level an integer number of queries are chosen for any possible fraction that may arise for all the 211 query patterns. One way to ensure this is to calculate the required number of queries (N) in each query pattern such that an integer results for any possible fraction. Let $j = 1 , \ldots , 2 1 1$ be an index across the 211 query patterns. We then solve for N by solving the following formulation:

$$
\frac {\sum_ {i = 1} ^ {5} N L _ {i j}}{\sum_ {i = 1} ^ {5} L _ {i j}} = N \quad \forall j = 1, \dots , 2 1 1
$$

where N and $N L _ { i j } / \sum _ { i - 1 } ^ { 5 } L _ { i j }$ must both be integers.

This yields a sample size of N = 2520 queries for each query pattern. To achieve this, we randomly draw a sample of 2520 queries from the base of the original 520 queries for each of the 211 query patterns (i.e., many of the original 520 queries will be used multiple times in a query pattern). Table 2 gives some examples of query patterns used in this study.

Table 2  
Examples of query patterns used in the experiment

<table><tr><td colspan="2">Examples of query patterns used in the experiment</td></tr><tr><td>Proportional ratio for queries from each complexity level</td><td>Number of queries from each complexity level to form a calculation sample</td></tr><tr><td>(0,1,0,0,0)</td><td>2520 queries were all from complexity level 2</td></tr><tr><td>(1,2,0,0,1)</td><td>630 (=1/((1+2+0+0+1))×2520) queries were from complexity level 1, 1260 queries were from complexity level 2 and last 630 queries were from complexity level 5</td></tr><tr><td>(2,0,2,1,2)</td><td>720 (=2/((2+0+2+1+2))×2520) queries were from complexity level 1, 720 queries were from complexity level 3, 360 queries were from complexity level 4 and last 720 queries were from complexity level 5</td></tr></table>

Our objective is to examine the performance of the six selected database structures under various levels of query arrival rates (‘‘congestion’’, if you will) and then seek to identify any robust database structures, i.e., ones that perform competitively with respect to average system times when subjected to a wide array of query patterns under different query arrival rates. Table 3 provides descriptions of key values used in our analysis.

## 2.2. No congestion environment

Before moving on to our analysis of varying query arrival rates and system congestion, we first analyze query pattern processing under the assumption of no queuing, that is, queries are always processed upon arrival. We computed and compared the average processing time, x¯, for each of the six database structures for an $N { = } 2 5 2 0$ query sample in each of the 211 query patterns. For query patterns where all queries are drawn from complexity level 1 or 2 (i.e., query patterns $( 1 , 0 , 0 , 0 , 0 ) , ~ ( 2 , 1 , 0 , 0 , 0 ) , ~ ( 1 , 1 , 0 , 0 , 0 ) .$ (1,2,0,0,0) and $( 0 , 1 , 0 , 0 , 0 ) )$ , the normalized database structure DBS6, provides the fastest average processing time (e.g., an x¯ value of 0.065 s with query pattern $( 1 , 0 , 0 , 0 , 0 ) )$ ). When the query pattern includes queries from complexity level 3 (i.e., for the 6th through the 19th query patterns listed) alone or in conjunction with queries from complexity levels 1 and 2, database structure DBS3 yields the lowest x¯ values. When queries from either complexity level 4 or 5 are present, database structure DBS1 yields the optimal x¯ value in each case (192 query patterns). We also calculate the composite selectivity factor value for each query pattern. Values range from 0.000018 to

Table 3  
Summary of key values in our analysis

<table><tr><td>Parameter</td><td>Formula/Remarks</td><td>Explanation</td></tr><tr><td> $\bar{x}$ </td><td> $\sum_{i=1}^{N} P_i / N$ </td><td> $\bar{x}$  is the average query processing time.  $P_i$  is the processing time of  $i$ th query in a set where  $i = 1, \dots, 2520$  ( $N = 2520$ ).</td></tr><tr><td> $\lambda$ </td><td>Arrival rate(control factor)</td><td> $\lambda$  is the average arrival rate of queries per second.</td></tr><tr><td> $\rho$ </td><td>Utilization rate:  $\lambda \bar{x}$ </td><td> $\rho$  is the measure of overall system use or congestion.</td></tr></table>

0.640189. Up to the value of 0.001911, database structure DBS6 is optimal (smallest x¯). Over the range 0.002858–0.041318, database structure DBS3 is best. At and above 0.043391, database structure DBS1 would be the choice.

If the query set submitted to the system included only queries from the two lowest complexity levels, then using DBS1 rather than DBS6 would result in an average inefficiency (percentage of time lost) ranging from 38% to 50%. If the query pattern included queries from complexity level 4 or 5, selecting database structure DBS6 instead of database structure DBS1 would result in inefficiencies ranging from 1% for query pattern (2,2,0,1,0) to 270% for query pattern $( 0 , 0 , 0 , 0 , 1 )$ . The lowest level of inefficiency occurs for a query pattern with 80% of the queries from complexity level 1 or 2 and 20% from complexity level 4. The highest inefficiency occurs when all queries are from the highest complexity level. These values help illustrate performance gains that can be achieved by ‘‘switching’’, that is using different database structures as query patterns change. It is important to remember that the values are a direct result of our original database layout (see Fig. 2 and normalized structure detailed in Fig. 3 above). Other database layouts would likely yield quite different x¯ results and different switching gains opportunities. Here, we are illustrating a database design or ‘‘structure selection’’ method using the database layout pictured in Fig. 2. While analyzing different layouts might prove interesting, it is not germane to our purpose.

As noted earlier, the results that we discuss here were computed in an environment where queuing does not occur. What happens as we move to more realistic situations where query arrival rates are such that queues do occur? What happens as the arrival rate increases and system congestion occurs? In Section 3, we describe the queuing model used to address these questions.

## 3. Queuing model

The M/G/1 queuing model is a single-server system with Poisson arrivals and an arbitrary query-processing-time distribution [10]. This kind of system has an average arrival rate of k queries per second and a mean interarrival time of 1/k second. When queues are possible, our interest is in total system time, the sum of waiting time or time spent in the queue and processing time. Traditionally, for queuing analysis researchers use hypothetical service time distributions. However, as noted above, we have measured exact processing time for each query. We can thus directly calculate and specify the service time distribution using the processing times for the set of queries comprising a given query pattern.

In M/G/1 systems, the average waiting (in the queue) time, W, is defined as:

$$
W = \frac {\rho \bar {\mathrm{x}} (1 + C ^ {2})}{2 (1 - \rho)}\tag{1}
$$

This expression is well known as the Pollaczek– Khinchin $( P { - } K )$ mean-value formula [10], where $C ^ { 2 } = \sigma ^ { 2 } / \bar { \mathbf { x } } ^ { 2 }$

We now examine the performance of the six selected database structures under various arrival rate values and then identify the robust database structures, i.e., the ones that perform competitively with respect to average system times when subjected to a wide array of query patterns under different arrival rates and system congestion. We calculate $C ^ { 2 } = \sigma ^ { 2 } / \bar { \mathbf { x } } ^ { 2 }$ using the actual processing times measured in the experiment described in Section 2.

For the purpose of the queuing analysis, we draw a hundred samples for each query pattern. Since we use 211 different query patterns, this results in 21,100 samples in total. We then varied the arrival rate, k, from 1 to 900 to indicate the congestion level or utilization rate of the system, q, explained in Table 3 above. Note that, as k reaches 500, DBS6, the normalized structure, has reached a utilization rate of 0.909. When k hits 600, DBS6 is over capacity, that is its use would lead to an ever-increasing queue length.

DBS1 is the structure that has the smallest overall average processing time and lowest utilization or congestion rates across the entire range of k values. Employing a different database structure would result in a percentage deterioration of at least 11% for a k of 1 to at least 69% for a k of 900. Thus, DBS1 provides a robust database structure across the range of k values studied.

In Section 4, we further develop the concept of robustness, this time across query pattern groupings that help reduce the dimensionality of the problem.

## 4. Identification of robust database structures for query pattern groupings under different arrival rate conditions

In our experiment, the choice of five complexity levels results in the need to analyze 211 query patterns. In a given application, the query variety may be quite large and hence the resulting number of query patterns that must be investigated may increase significantly.

Here, we illustrate a query pattern grouping approach using King’s selectivity factor [9] (also see Ref. [3]) to reduce the dimensionality of the problem. We begin by grouping the 211 query patterns based on King’s selectivity factor. The composite selectivity factor for a query pattern is calculated by taking the weighted average of the selectivity factors of individual queries that make up a given query pattern. Seeking to have roughly equal sized groups whose members possessed similar selectivity factor values (for details and complete analysis, see Ref. [3]), we utilize 10 query pattern groupings each containing between 18 and 23 of the original query patterns. We again provide results with respect to overall average system time. In our notation, Group 1 contains the query pattern set (a group of 22 individual query patterns) with similarly low composite selectivity factors. Thus, Group 1 can be viewed as comprised of query patterns containing query mixes dominated by low complexity levels. Group 10 contains the 23 query patterns with similarly high composite selectivity factors. Thus, Group 10 can be viewed as comprised of query patterns containing query mixes dominated by high complexity levels. Groups 2 through 9 are ordered similarly.

We calculate the average system times to complete a query within that group for different database structures. To obtain these values, we average the query system times for the total number of queries in each group. For example, in Group 1, we compute the average system times for a total of 22 times 2520 times 100 or 5,544,000 queries (i.e., number of query patterns in the group times the number of queries for each pattern times the number of samples of each query pattern as detailed above in Table 2). The utilization rates (congestion levels) are also calculated for each situation. In addition, we let the arrival rate, k, vary from 1 to 1800 queries per hour.

For query pattern Group 1, DBS3 is the optimal performer across all arrival rates. For a k of 1, use of another database structure to the process the query set would result in an inefficiency ranging from 10% (DBS1) to 64% (DBS5). As k increases, the possible inefficiencies from choosing a suboptimal database structure can rise significantly. For a k of 1000, using DBS5 instead of DBS3 would result in an inefficiency of 108%. When k reaches 1800, the inefficiencies from choosing other than DBS3 to process Group 1 queries ranges from 22% (DBS1) to over 1000% (DBS5).

For the specific database layout used here, it turns out that DBS1 is optimal for all other complexity groupings (Groups 2 through 10). Inefficiencies from choosing any other database structure range from approximately 8% (DBS2 for Group 2 with k = 1) to infinitely large values since many of the database structures cannot process the more complex queries at high arrival rates without incurring ever-increasing queues.

For the database layout studied here, our methods were successful in identifying robust database structures. Under different database constructs or layouts, a greater variety of different structures might be optimal for one or more complexity groupings. Here, only two database structures were members of the ‘‘optimal set’’ (i.e., DBS3 was best for Group 1, DBS1 for Groups 2 – 10), yet switching between the two structures could yield significant gains in average system time. With more complex (and perhaps more typical) database layouts, our conjecture is that a greater variety of database structures would be best for one or more complexity groupings. In these situations, we also conjecture that constructing switching rules and query pattern tracking procedures will yield significant savings compared to use of a single database structure.

While we have used overall average system time as the criteria, the methods we set forth can be applied using any number of criteria. One such alternative criterion may center on shielding the organization against the worst-case performance, i.e., the selected structure should have the minimum deviation (or squared deviation) in the worst-case scenario. As noted above, the choice of criteria is application specific, but the steps presented here would still apply.

## 4.1. Lesson learned

The full enumeration or ‘‘brute-force’’ approach (i.e., examining all feasible structures, 96 in total) enabled us to clearly demonstrate that only a handful of database structures are candidate structures or ‘‘potential good performers’’ for further examination in identifying robust database structures. The initial outcomes are encouraging for the candidate set of structures that mainly involve joins of two of the original tables. If results reported here continue to hold across additional experimental investigations, then applying our approach in real world settings should be able to begin with step (4) utilizing the set of candidate structures. As noted above, our database design consists of seven tables. This complexity falls toward the upper end of that of the three examples (four tables, TCP-A, a bank; four tables, TCP-B, a bank; and nine tables, TCP-C, supplier of wholesale parts) presented in Chapters 2 and 3 of Gray’s benchmark treatise [5]. Further, our work follows Gray’s (see Chapter 4) guidance to utilize ‘‘synthetically generated relations instead of empirical data from a real database’’. Gray suggests that, with empirical data, it is difficult to:

. . .specify a selection query with a 10 percent or 50 percent selectivity factor or one that retrieves precisely 1000 tuples. For queries involving joins, it is even harder to model selectivity factors and build queries that produce results or intermediate relations of a certain. An additional shortcoming of empirical data (versus ‘‘synthetic’’ data) is that one has to deal with very large amounts of data before it can be safely assumed that the data values are randomly distributed. By building a synthetic database, random number generators can be used to obtain uniformly distributed attribute values and yet keep the relation size tractable.

Our results indicate that the ‘‘potential good performers’’ are the ones with table(s) that is joined by ‘‘two’’ original tables (not three, four, five, six or seven tables joined). The next question is whether the findings will continues to hold up in additional experimental investigations enabling organizations to utilize our process without requiring the costly brute-force enumeration.

The process of investigating the ‘‘potential good performers’’ only needs to be done once at the earlier designing stage of an organization’s database. We argue that it is a viable and feasible approach to realize potentially significant benefits from using robust structures to process queries under changing query patterns and arrival rate conditions.

## 5. Conclusion

Databases in the modern organization have become integrated parts of information delivery both inside and outside an organization. The demand for database services is less predictable and controllable since availability of database information on a wide variety of platforms, such as the web, means that a significant portion of demand may arise from external sources that seek responses to diverse sets of queries. For example, many companies already use databases to create customized web pages and dynamic content on their intranet and extranet for their employees, business partners and customers. The breadth of those accessing these pages and linked content results in a variety of query patterns that the underlying database must handle. In addition, such access and query demands can fluctuate greatly resulting in a variety of congestion conditions that impact performance.

We summarize the problem tackled here in the following way: Given a modern database application environment, can we identify and select the database structure that provides robust performance across changing query patterns and arrival rate conditions?

We first directly determine the performance of each alternative structure for each query type. The best performing structures (in our example, 5 of 96 possible structures) plus the normalized structure were selected and analyzed across arrays of query patterns. We then identified certain database structures as robust structures, that is good performers across the different types of query patterns and arrival rate levels.

Our methods yield total service time or system time by integrating actual query processing time measurements into a queuing model. This allows for a rich analysis of commonly occurring situations, changing query patterns and arrival rate conditions, in the operation of modern business systems. The advantages of our technique includes: (i) the performance data needs to be collected only once and (ii) simulation modeling of database structures and components is not necessary since the performance data can be collected using the actual database. Advantages of simulation modeling, such as the effect of change of query patterns and arrival rates, can be computationally realized without the requirement of detailed modeling of database environment.

If a company is operating a single website with no congestion and the company has accurate information on the population of users accessing that site along with accurate information on the precise information sought, our methods would likely yield no benefit. We would argue that such a scenario is currently unlikely and growing more so each day. The far more likely situation is that of a company operating multiple portals, multiple sites within each portal, facing various arrival rates and lacking accurate information on the exact information sought by the population accessing the sites. In these situations, the ability to identify and utilize structures with robust performance holds great promise.

We also note that our methodology can be used to select which views to materialize in a data warehousing environment. It can be easily extended, for example, to the problem studied by Harinarayan et al. [4], of determining which cuboids to materialize from a preestablished choice set. As emphasized throughout the paper, applying our methods in a given application environment requires the determination of the relationship between specific performance measures and the firm’s net return. Some (e.g., Refs. [4,16]) have suggested proxy measures including that ‘‘the cost of answering a query, Q, is the number of rows present in a table used to construct $\mathrm { Q } '$ [16] (p. 138). We argue, however, that such costs are likely to be system and configuration dependent. As is the case for revenue impact, costs must be investigated within the application environment. In our demonstration here with the presence of both changing query patterns and differing arrival rate levels, we were able to identify robust performing database structures. We also noted that, in any specific environment, selection of appropriate performance criteria must be directly linked to the fulfillment of organizational objectives. This suggests that our next research step, building on the results presented here, is to analyze the robustness of our methods across arrays of such linkages. Will we be able to extend our findings relating to identification of robust database structures? Will we be able identify structures that are robust performers across differing firm objective functions as well across query patterns and arrival rates we have already studied? Most importantly, can we utilize the observations from the current analysis and from expanded analyses to construct and test a theory of robust database structure development? We have begun with a detailed development and analysis of relationships that provides information that helped us illustrate the existence of robust database structures under the specific formulation studied here. The challenge is now to expand the formulations studied and to construct and test a theory of robust database structure design. In the spirit of philosophy of science as detailed in and paraphrased from Hempel [6], we have here set forth on the first two of the four steps in theory formulation and testing:

(i) observation and recording of recording of (all) relevant facts,

(ii) classification and formal analysis of these facts,

(iii) theory construction or ‘‘inductive derivation of generalizations from these facts’’ and

(iv) further testing of the theory or ‘‘generalizations’’.

Using the above process, we can compare database performance of our approach to other alternative designs such as traditional 3NF, datawarehousing or materialized views. For a given application environment, the comparison would require determining the relationships between specific performance measures and the firm’s net return. The work presented here illustrates the gains from identification and utilization of robust database structure. Our task now is to continue the investigation and develop a useful theory that can guide robust database structure design in wideranging dynamic settings.

## Acknowledgements

The authors are grateful for support from the Shenkman Family Chair, the Gladstein Professorship, the Gladstein MIS Research Lab and the Treibick Electronic Commerce Initiative without which this work could not have been completed.

## References

[1] R. Barquin, H. Edelstein, Planning and Designing the Data Warehouse, Prentice Hall, New Jersey, 1997.

[2] S. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, ACM SIGMOD Record 26 (1) (1997) 65 – 74.

[3] A.N.K. Chen, Improving database performance in a changing environment with uncertain and dynamic information demand: an intelligent database system approach, PhD dissertation, University of Connecticut, 1999.

[4] J. Gray, The Benchmark Handbook for Database and Transaction Processing Systems, 2nd ed., Morgan Kaufmann Publishers, San Mateo, CA, 1993.

[5] V. Harinarayan, A. Rajaraman, J.D. Ullman, Implementing data cubes efficiently, SIGMOD ’96, Montreal, Canada, 1996.

[6] C.G. Hempel, Philosophy of Natural Science, Prentice-Hall, Englewood Cliffs, NJ, 1966.

[7] E. Hoffman, J.R. Marsden, A. Whinston, Laboratory experiments and computer simulation: an introduction to the use of experimental and process model data in economic analysis, in: L. Green, J. Kagel (Eds.), Advances in Behavioral Economics, Ablex Publishing, Norwood, NJ, 1990, pp. 1– 31.

[8] R. Jain, The Art of Computer Systems Performance Analysis, Wiley, New York, 1991.

[9] J.J. King, Query optimization by semantic reasoning, PhD dissertation, Stanford University, 1981.

[10] L. Kleinrock, Queueing Systems: Volume 1. Theory, Wiley, New York, 1975.

[11] U. Rodgers, Denormalization: why, what, and how? Database Programming and Design, (1989) 46 – 53.

[12] G.L. Sanders, S. Shin, Denormalization effects on performance of RDBMS, Proceedings of the Thirty-Fourth Hawaii International Conference on System and Sciences, Maui, HI, 2001.

[13] M. Schkolnick, P. Sorenson, Denormalization: a performance oriented database design technique, Proceedings of the AICA, Bologna, Italy, 1980.

[14] V.L. Smith, Experimental economics: induced value theory, American Economic Review 66 (1976) 274– 279.

[15] V.L. Smith, Microeconomic systems as experimental science, American Economic Review 72 (1982) 923–955.

[16] J. Yang, K. Karlapalem, Q. Li, Algorithms for materialized view design in data warehousing environment, Proceedings of the 23rd Very Large Data Base Conference, Athens, Greece, 1997.

![](/api/attachments/ZQ2BT4T2/fulltext/images/9b2db84d502c5ed8bfdd911f725bdca42732b168156ebff4ee15284428814c93.jpg)  
Andrew N.K. Chen joins Arizona State University as an Assistant Professor in 1999. He received his Bachelor of Business Administration from Soochow University at Taiwan, M.S. in Accountancy from George Washington University, and Ph.D. in Operations and Information Management from University of Connecticut. His current teaching and research interests include electronic commerce, database management, knowledge management,

and business and Web programming applications. His research work has appeared in Journal of Management Information Systems, Decision Support Systems, Journal of Electronic Commerce Research, and international conferences such as ICIS, AMCIS and DSI.

![](/api/attachments/ZQ2BT4T2/fulltext/images/b3c3dc8f0d8695db9b951e7ed9c90fc8770669f790b05e03a61a3ac7f6fa8567.jpg)

Paulo Goes, Associate Professor, Dr. Goes joined the University of Connecticut in 1990. He teaches a variety of courses in Management Information Systems, both at the undergraduate and graduate level. His research interests are electronic commerce, online auctions, confidentiality and security issues, database technology and management, networks and data communications. Dr. Goes’ articles have appeared in Management Science, Operations Research,

Communications of ACM, INFORMS Journal on Computing, Information Technology and Management, IEEE Transactions on Communications, IEEE Transactions on Computers, ORSA Journal on Computing, Decision Support Systems, The International Journal of Flexible Manufacturing Systems, Queuing Systems: Theory and Application and The Journal of the Operational Research Society. MS and PhD in Computers and Information Systems from the University of Rochester, 1987 and 1991. In, addition, he holds a BS in Civil Engineering from the Federal University of Minas Gerais, Brazil, 1979, and an MS in Production Engineering from the Federal University of Rio de Janeiro, Brazil, 1985.

![](/api/attachments/ZQ2BT4T2/fulltext/images/cb1faba69a269955b1990dc612bc67716ea47e6070fcbf42a735bdec6515823c.jpg)

Alok Gupta is an Associate Professor of Information Systems at the Carlson School of Management, University of Minnesota; from 1996 to 2001 he was an Assistant Professor at Dept. of OPIM, University of Connecticut. He received his PhD in Management Science and Information from the University of Texas, Austin. His research has been published in various information systems, economics, and computer science journals such as Management Science, ISR,

CACM, JMIS, Journal of Economic Dynamics and Control, Computational Economics, Decision Support Systems, IEEE Internet Computing, International Journal of Flexible Manufacturing Systems, Information Technology Management, and Journal of Organizational Computer and Electronic Commerce. In addition, his articles have been published in several leading books in the are of economics of electronic commerce. He was awarded a prestigious NSF CAREER Award for his research on dynamic pricing mechanisms on the internet. From 1999 – 2001, he served as co-director of Treibick Electronic Commerce Initiative (TECI), an endowed research initiative at Dept. of OPIM, University of Connecticut. He is also an affiliate of the Center for Research in Electronic Commerce (CREC) at the University of Texas at Austin. He serves on the editorial boards of DSS and Brazilian Electronic Journal of Economics. He teaches courses in the areas of computer networking, electronic commerce, decision support, IT infrastructure, and computer programming at the undergraduate, MBA and PhD levels.

![](/api/attachments/ZQ2BT4T2/fulltext/images/7691accbdbdb6736e833356ac57ccaa47093a4ede5dbecb70b7c4c6ff8bd1e08.jpg)

Dr. James R. Marsden came to UConn in 1993 as Professor and Head, Department of Operations and Information Management, School of Business Administration, University of Connecticut. Dr. Marsden was part of a three-person concept development team that initiated and oversaw the development of the Connecticut Information Technology Institute and is currently serving as its Executive Director. He developed and implemented the Treibick Electronic

Commerce Initiative that is funded through a generous gift provided by Richard Treibick and the Treibick Family Foundation. He was a member of the edgelab development team and currently serves on the edgelab Steering Committee which selects and resources projects and oversees operations. Dr. Marsden is a tow-time winner of the Chancellor’s Award for IT Excellence and a co-winner of the Team Connecticut Program Award from the Office of Economic Development. He has a lengthy research publication record in market innovation and analyses, economics of information, artificial intelligence, and production theory. His research work has appeared in Management Science; IEEE Transactions on Systems, Man, and Cybernetics; American Economic Review; Journal of Economic Theory; Journal of Political Economy; Computer Integrated Manufacturing Systems; Decision Support Systems; Journal of Management Information Systems, and numerous other academic journals. Professor Marsden received his AB from the University of Illinois and his MS and PhD from Purdue University. Having completed his J.D. while at the University of Kentucky, Jim has been admitted to both the Kentucky and Connecticut Bar.
