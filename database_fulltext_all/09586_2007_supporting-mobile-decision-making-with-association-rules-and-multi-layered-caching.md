---
otero_id: 9586
otero_key: "Z3XEH5JC"
title: "Supporting mobile decision making with association rules and multi-layered caching"
authors: "Navin Kumar; Aryya Gangopadhyay; George Karabatis"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting mobile decision making with association rules and multi-layered caching

Navin Kumar, Aryya Gangopadhyay<sup>\*</sup>, George Karabatis

University of Maryland, Baltimore County (UMBC), Information Systems Department, 1000 Hilltop Circle, Baltimore, MD 21250, USA

Available online 27 June 2005

## Abstract

We describe a methodology and a prototype implementation of an online analytical processing system for mobile devices. The system guides the user to narrow down the search space using association rules. We also describe multi-layered caching techniques to improve performance and increase system utilization even in the presence of disconnections. The system is built using a three-tier architecture comprising of a data warehouse, a middle-tier server, and client mobile devices. Finally we conducted a series of simulation experiments to evaluate the performance of our association rule-based system and the multilayered caching.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Implementation of mobile applications; OLAP; Data warehouse; Association rules; Caching techniques

## 1. Introduction

With the rapid development of technology for management of data the world is becoming <sup>b</sup>data rich<sup>Q</sup> but <sup>b</sup>information poor.<sup>Q</sup> One of the most promising technologies that attempt to address this limitation is data warehousing and online analytical processing (OLAP). Data warehouses allow the storage and multi-dimensional modeling of historical data in a <sup>b</sup>subjectoriented<sup>Q</sup> manner that is more conducive to decision making than the operational databases, which allow day-to-day transaction processing. OLAP is a part of the data warehouse technology that enables users to examine the data interactively. Mobile devices constitute another major technological innovation towards universal access and connectivity realizing the potential for m-commerce [40]. Although advances in network technologies have improved the bandwidth of wireless channels, a mobile decision maker has difficulty accessing the immense amount of information in a data warehouse, especially over channels with low reliability where disconnections are the norm.

In this paper we describe a methodology and a prototype implementation that provides OLAP support to decision makers using mobile devices. This work addresses several open research issues: First, the level of decision support that most OLAP systems provide is limited to summarized and aggregated data, which may not be sufficient for all users. Additionally, a user must have a fairly good understanding of the multidimensional model and a good intuition of what may be <sup>b</sup>discovered<sup>Q</sup> in order to navigate through the vast magnitude of datasets in an OLAP system. We describe a methodology where users can browse for high-level information presented in the form of association rules and then selectively navigate to the deeper recesses of the dataset. Thus, the system provides guidance while letting the user drive the knowledge discovery process. We view association rules as high-level description of the detailed data. The choice of association rules over other data mining methods is simply a matter of selecting the appropriate level of information needed by most decision makers. Clustering, for example, is too exploratory for most decision makers while classification is too specific. The search process is interleaved between examining association rules and subsequently determining a drill-down path to a more appropriate level of detail. A user can also view the relevant data at any point of time.

Second, the challenges of mobile devices (as in [19]), and the large size of OLAP data pose significant problems to a mobile decision maker who needs to have efficient access to OLAP data [49]. Caching techniques increase data availability and improve data access performance. We propose a multi-layered caching mechanism to locally store the results of previously evaluated queries, promoting reuse of cached data, thus minimizing retransmissions. We describe a multi-tier system architecture and a multi-layered caching mechanism that is suitable for mobile environments.

The major contributions of this paper include: (i) a novel methodology for high-level navigation and mining of the data warehouse space using association rules (ii) a three-tier architecture and a prototype implementation of our system (iii) a multi-layered caching mechanism with locally stored association rules, queries and resulting datasets, to aid mobile users in their decision-making even in the presence of disconnections, and (iv) a set of experiments that validate our methodology.

The rest of the paper is organized as follows: in Section 2 we discuss the related research relevant to this paper. In Section 3 we describe our main contributions including our methodology for mobile DSS, the system architecture and its various components, usage of association rules for analytical mining, and our caching mechanism. Section 4 discusses the implementation details and Section 5 contains a set of experiments to show the advantages of our methodology. Section 6 contains conclusions and future work.

## 2. Related work

A data warehouse is defined as a <sup>b</sup>subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management’s decision making process<sup>Q</sup> [20]. Research in this field has been done in the areas of data warehouse development and maintenance [4,15,62], view materialization [13,48,51,52,56, 61], multi-dimensional modeling [1,3,12,18,57], query languages and evaluation [30,32,33,35,38,54], visualization [8], indexing [5,14,41], storage and chunking [10,23], and online analytical mining (OLAM) [7,16, 17,42]. While all of these works are related to the research presented in this paper, the closest matches are those conducted on OLAM.

OLAM allows multi-dimensional data mining in large databases. Its goal is to reduce the computational effort for data mining and increase its effectiveness by carefully choosing the target datasets. While the issue of controlling the data mining process, such as generation of only those association rules that are potentially useful, is largely unresolved, OLAM can address this issue by allowing the user to selectively identify the target datasets by drilling down/up dimensional hierarchies. The issue of <sup>b</sup>guiding the user<sup>Q</sup> through such navigations becomes important in the complex datasets found in data warehouses. This issue becomes even more critical if the decision maker is a mobile user due to additional constraints of resources and connectivity. While some previous research [7,16,17,42] has proposed OLAM approaches for desktop clients using progressive refinement [7,16,17] and discovery-driven exploration of OLAP data cubes [42], no such work is found in the domain of mobile computing—to the best of our knowledge, which is the topic of this paper.

Caching techniques can be used in OLAP systems to reduce the processing time of multidimensional queries by storing aggregations as materialized views. In semantic data caching [9,24,39] the result set of a query along with its semantic description are stored together:

The Watchman intelligent cache manager [44] delivers the cached result to a query that matches exactly a cached query string. The Dynamat cache manager [26] stores fragments, which are query result aggregations in finer granularity than views, and they are used to answer more general queries. In [10] the authors decompose the multidimensional space into chunks where each distinct dimension is divided into ranges. They define a mapping structure called Domain Index to maintain the correspondence between a dimension value and its ordinal number. Multiple OLAP cache servers (OCS) have been used in [21] to keep track of multidimensional queries allowing inter-OCS communication to deliver cached data from an OCS server to another. This work has been extended in peer-to-peer (P2P) systems comprising a pool of low-end clients caching multidimensional data [22].

OLAP applications for mobile devices can greatly benefit from caching techniques [49,60] while significant work has been performed on caching for mobile environments where data is stored locally on the mobile device [2,6,11,31,36,59]. Semantic data caching techniques have also been explored for mobile environments. In [29] the authors reuse locally cached data blocks to limit the amount of data transmission from the server.

Our work has some similarities with semantic delivery of OLAP aggregates for decision making in mobile environments [45–47]. However, the authors utilize summary tables and focus on efficient scheduling algorithms, whereas we take advantage of association rules.

## 3. Methodology

The main problem addressed by this paper is to create an infrastructure that allows a mobile decision maker to perform OLAP operations using a handheld device. In this case we are dealing with two extremes: very large datasets and very low input/output capacity on mobile devices. Our approach is to guide the user in efficiently narrowing down the search space to the most relevant and smallest size dataset. We guide the mobile user through the data using association rules, providing an insight into the patterns of the dataset. The novel aspect in this approach is to store the association rules in the data warehouse and utilize them as metadata information presented to the mobile user. We choose to use association rules instead of clustering or classification due to the following reasons. Clustering provides an exploratory view of how data can be grouped, but it does not provide any information on the characteristics of the groups formed. As opposed to clustering, association rules provide information about measures based on the characteristics of one or more dimensions. Thus, instead of grouping data, association rules provide more detailed description of the data being mined. On the other hand, classification assigns class labels to individual objects instead of providing more generic descriptions of patterns. In contrast, association rules derive generic patterns based on the characteristics of objects instead of assigning labels to them individually.

Our methodology consists of four steps: generating association rules, storing/retrieving association rules in the data warehouse, mapping association rules to queries, and developing caching techniques to enhance the overall system efficiency. We first describe the architecture of the system and then discuss the four steps mentioned above.

## 3.1. System architecture

We present the three-tier architecture depicted in Fig. 1. The system consists of a data warehouse, a middle-tier server, and mobile clients. The data warehouse stores OLAP data (fact, dimension, and aggregate tables) as well as association rules. As multidimensional queries are time consuming, resource intensive, and computationally expensive, instead of sending the queries to the data warehouse we take advantage of computed results that are stored and reused through a multi-layered caching mechanism. The middle-tier server is connected to the data warehouse over a wired connection and acts as a communication link between the data warehouse and the mobile devices. Every mobile request for an association rule or a multidimensional query is sent to the middle-tier server, which in turn, forwards the request to the data warehouse and transmits the desired results back to the mobile device. It also has its own repository called server cache to store incoming mobile requests and results, so that future requests on cached items can be served without accessing the data warehouse.

![](/api/attachments/Z3XEH5JC/fulltext/images/2ae0ada31e37f4d5ce98a13e3289abd048c405e15b732d6f5574994e450161eb.jpg)  
Fig. 1. Mobile 3-tier architecture.

The third-tier in our architecture consists of mobile client devices such as handheld personal digital assistants, smart phones, or smart pagers.

To illustrate our proposed methodology, we adapt a real life example on retail sales from [25]. There are three dimension tables: product, store, and time, and one fact table: profit. Table 1 describes the dimensions and their respective concept hierarchies. We model the dimensional hierarchies as follows.

$$
d _ {i} = i \text { th   dimension }, i = 1,..., N \text { where }
$$

$$
N = \text { number   of   dimensions }\tag{1}
$$

$$
l _ {i} = \text { total   number   of   levels   for   dimension } d _ {i}\tag{2}
$$

Here the level ranges from 0 to $l _ { i } - 1$ . Level 0 indicates that the dimension is aggregated to $A L L$ As the level value increases, the concept hierarchy opens up to show more detailed information about a dimension. Table 1 shows the three dimensions and their hierarchy levels used as a running example in this paper (adapted from [25]). This allows a mobile decision maker to view sales data at different levels and combinations of dimensional hierarchies and identify stores/products/time periods that exhibit exceptional sales.

Dimensional hierarchies and their levels

<table><tr><td></td><td>Product</td><td>Store</td><td>Time</td></tr><tr><td>LEVEL</td><td>Product_Key</td><td>Store_Key</td><td>Time_Key</td></tr><tr><td>0</td><td>ALL</td><td>ALL</td><td>ALL</td></tr><tr><td>1</td><td>Category</td><td>Store_Region</td><td>Year</td></tr><tr><td>2</td><td>Subcategory</td><td>Store_State</td><td>Quarter</td></tr><tr><td>3</td><td>Brand</td><td>Store_City</td><td>Month</td></tr></table>

## 3.2. Generating association rules

The raw data is stored in dimension, fact, and aggregate tables. Information related to each dimension is stored in a separate table. The fact table contains information about measures such as profit and sales, along with keys relating it to the dimension tables. The fact, dimension and aggregate tables can be queried to obtain the measures at different levels of dimensional hierarchies.

In our system, the user can view the data at various levels of dimensional hierarchies. As an example, let us assume that a decision maker has drilled down the product dimension to the <sup>d</sup>Drinks<sup>T</sup> category. Next, let the user now look at the part of the cube where region is <sup>d</sup>South West<sup>T</sup>. The query corresponding to the first request is modified to group the dimensions for year and product subcategory and slice the previous cube for sales region <sup>d</sup>South West<sup>T</sup>. Taking this approach we identify all possible multidimensional queries, that will be used to gather the data for data mining purposes. Using Eqs. (1) and (2), the total number of possible OLAP queries is

$$
\prod_ {i = 1} ^ {N} l _ {i}\tag{3}
$$

Here $l _ { i }$ also includes level 0.

Table 1 shows four levels for each of the dimensions, making a total of 64 $( 4 \times 4 \times 4 )$ potential queries. Corresponding to each query result, association rules are generated by a data miner. Due to system constraints the number of association rules generated is limited to a pre-defined parameter $N _ { \mathrm { t o p } } ,$ the choice of which is governed by system constraints as well as user preferences. From Eqs. (1) and (2), the total number of rules is

$$
\prod_ {i = 1} ^ {N} \left(l _ {i} - 1\right) \times N _ {\mathrm{top}}\tag{4}
$$

The number $l _ { i } - 1$ signifies that there is no association rule for the 0-cuboid ALL.

## 3.3. Database schema for storing association rules

Mobile devices are limited in displaying large quantities of data on small screens. To assist user navigation, we do not just want to show the bulk of data but also display appropriate mining rules for that particular cuboid. We generate the association rules offline and store them in the data warehouse along with the multidimensional data in a relational format, because it is impractical to run the system on the back end to instantaneously generate the rules for a user request. Thus, the system can search for information either in the form of OLAP data or as association rules.

An association rule has the form AYB where A is the antecedent and B is the consequent. The antecedent A can contain one or more dimensions. The consequent B, can only be a measure with a corresponding value. For example the rule <sup>b</sup>Product category = DrinksY Profit = Low<sup>Q</sup> implies that for product category Drinks, the profit is low. In a preprocessing step, we used equiwitdh binning for discretizing profit into three categories. For each rule, a dimension $d _ { i }$ has a corresponding value $l _ { i j }$ that refers to its level in the dimensional hierarchy. If a dimension $d _ { i }$ does not appear in a rule, then $d _ { i }$ is at level $l _ { i 0 }$ (aggregated for ALL). We explain the storage of a rule using the following example.

$$
(P r o d u c t b r a n d = X, S t o r e \_ {S} t a t e = Y, Y e a r = Z)
$$

$$
\rightarrow \text { Profit } = \text { Low }
$$

The antecedent consists of three dimensions. The product dimension is at level 3 (brand) with a value of X, the store dimension is at level 2 (store<sup>\_</sup>state) with value of $Y ,$ and the time dimension is at level 1 (year) with the value of Z. The consequent contains a measure, profit, with value <sup>b</sup>low<sup>Q</sup>. Table 2 shows our relational structure and sample data for storing association rules. Here, Rule<sup>\_</sup>ID is a unique ID assigned to each association rule. Rule<sup>\_</sup>Portion identifies if it is antecedent or consequent. Attr<sup>\_</sup>Type distinguishes a dimension from a measure. Attr<sup>\_</sup>ID, Attr<sup>\_</sup>Level, and Attr<sup>\_</sup>Value store the dimension/measure ID, the level for the attribute, the level from the dimensional hierarchy, and the value of attribute respectively.

Table 2  
Storing association rules

<table><tr><td>Rule_ID</td><td>Rule_Portion</td><td>Attr_Type</td><td>Attr_ID</td><td>Attr_Level</td><td>Attr_Value</td></tr><tr><td>1001</td><td>ANTE</td><td>D</td><td>101</td><td>1</td><td>Drinks</td></tr><tr><td>1001</td><td>CONS</td><td>M</td><td>201</td><td>0</td><td>Low</td></tr><tr><td>1002</td><td>ANTE</td><td>D</td><td>101</td><td>1</td><td>Supplies</td></tr><tr><td>1002</td><td>ANTE</td><td>D</td><td>103</td><td>1</td><td>1995</td></tr><tr><td>1002</td><td>CONS</td><td>M</td><td>201</td><td>0</td><td>Low</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Let us look at the two first rows with Rule<sup>\_</sup>ID 1001 from Table 2: The value $D$ in the Attr<sup>\_</sup>Type column stands for <sup>d</sup>dimension<sup>T</sup>. The Attr<sup>\_</sup>ID 101 is <sup>d</sup>Product for which Attr<sup>\_</sup>Level 1 identifies <sup>d</sup>Category<sup>T</sup>. In the consequent, attr<sup>\_</sup>type <sup>d</sup>M<sup>T</sup> indicates it is a measure. Attr<sup>\_</sup>ID 201 is profit. Hence the association rule is: (Product Category = <sup>d</sup>Drinks<sup>T</sup>YProfit = Low). Similarly the association rule corresponding to Rule<sup>\_</sup>ID =1002 is: (Product Category = <sup>d</sup>Supplies<sup>T</sup>, Year = 1995YProfit = Low). In this case we have used the convention of representing dimensions with IDs between 100 and 200 and measures with IDs above 200. This information is also stored in separate lookup tables.

## 3.4. Mapping association rules to queries

A mobile user is guided through the OLAP data using association rules, and can further request for the dataset corresponding to a rule of interest. While navigating from an association rule to the underlying dataset, the system maps the rule to a corresponding multidimensional query as follows. The SELECT clause of the query corresponds to the dimensions in the antecedent of the rule. Each selection (j condition) in the WHERE clause of the query corresponds to each of the antecedent conditions of the rule. The join condition and the GROUP BY clause of the query are derived from the dimensions in the antecedent. The aggregation level of the measure corresponds to the consequent of the rule. If the rule has only one dimension in its antecedent, it is automatically drilled down to the next level. However if the antecedent contains more than one dimensions, the user specifies the dimension on which to drill down. The complete pseudo-code can be found in Fig. 2.

For example if we consider the following association rule:

$$
(P r o d u c t C a t e g o r y = S u p p l i e s, Y e a r = 1 9 9 5)
$$

YProfit ¼ Low

This rule has more than one dimension on the antecedent side. If the user selects Product dimension for further exploration, this dimension is drilled down to one level while retaining the same levels for other dimensions. The constructed SQL is as follows.

![](/api/attachments/Z3XEH5JC/fulltext/images/4cea505c63ead8ae2e9606b68050ac2ab416681dca3deecf1732251ad3036513.jpg)  
Fig. 2. Mapping association rules to queries.

```sql
SELECT Product.subcategory, Time.year, sum (FACT.profit)
FROM Product, FACT, Time
WHERE Product.product_key=FACT.product_key
AND Time.time_key=FACT.time_key
AND Product.category='Supplies'
AND Time.year=1995
GROUP BY Product.subcategory, Time.year
ORDER BY Product.subcategory, year;
```

## 3.5. A caching mechanism for mobile users

Considering that a handheld mobile device with a small screen has limited display capabilities [28, 43,55], it is a real challenge to support a mobile decision maker in a productive and effective way. Furthermore, limitations in network bandwidth, network speed and occasional or frequent disconnections are still major issues for handheld devices [49]. Consequently, it is impractical to expect the mobile user to wait long enough for the system to generate the multidimensional data or mining rules and display them on small wireless devices. We address these problems using a caching mechanism, which is described next.

## 3.5.1. A multi-layered cache mechanism

Initially, a mobile user is presented with several association rules displayed in the mobile client device, and after selecting a rule of interest, the user may request the data represented by this association rule. This request is forwarded to the middle tier server as an OLAP query expression and the query result is returned back to the mobile client. Our multi-layered cache mechanism stores the association rules and their correlated query details. These caching layers correspond to three different types of information that are linked together: (i) the generated association rules, (ii) the corresponding multidimensional query expressions and (iii) the actual query results. Consequently the three layers in our caching mechanism correspond to the association rules, query expressions and result set, as shown in Fig. 3.

In Layer-1 we cache the association rules that are being viewed by the mobile clients. Layer-2 is responsible for caching the OLAP query semantics (i.e., the query expressions) corresponding to the current association rule. Here current means the association rule selected by the user at that instant of time. We keep track of the current association rule in order to determine the location (node) of the

![](/api/attachments/Z3XEH5JC/fulltext/images/5bf5047f3379e2de07aa457a09d20c21cbf9cdc54048de2ebc6536d2ee1547cb.jpg)  
Fig. 3. Multi-layered cache.

user while navigating the data cube. In Layer-3 we store the OLAP query results corresponding to query expressions. Note that Layer-1 has a one-to-many relationship with Layer-2, due to the fact that Layer-1 may store rules, which have no corresponding query expressions in Layer-2. For example, Layer-1 caches association rules that may not always connect to any OLAP query expressions, as the user is very likely to look at several association rules but only a few of them would be of further interest. Layer-1 would store every association rule a user is navigating through, but Layer-2 cache would be populated only when a corresponding query expression of the rule is requested. We also observe a one-to-one relationship between Layer-2 and Layer-3: if an OLAP query expression (Layer-2) is selected by the user and sent to the server, this query has to be processed and its result (Layer-3) will be sent back to the user.

It is more beneficial to present high level information to the mobile user, which consists of fewer amounts of data to be transmitted versus having the user submit a multidimensional query, wait until the results are displayed in the mobile device, only to realize that it was not the information of interest. It is important to note the relationship between the multi-layered cache mechanism and the three-tier architecture of our system: Layer-1, Layer-2 and Layer-3 caches are located both on the middle-tier server and the mobile client devices.

## 3.5.2. Layer-1: caching association rules

Fig. 4 illustrates our caching scheme for Layer-1. A mobile user’s request for an association rule $r _ { \mathrm { c u r r } }$ initiates a search in the Layer-1 cache of the mobile device. If the rule $r _ { \mathrm { c u r r } }$ is found it is presented to the user; otherwise the request is forwarded to the middletier server. The server seeks $r _ { \mathrm { c u r r } }$ in its own Layer-1 cache, and if found it is dispatched to the mobile device, otherwise the original user request reaches the data warehouse, which will produce the rule and send it to the middle-tier server.

![](/api/attachments/Z3XEH5JC/fulltext/images/a3bc37f25c6d68f1152565da0d55e9565c6b724c68af0db108b5286debd6a829.jpg)  
Fig. 4. Caching association rules in Layer-1.

Before forwarding the rule to the mobile device, the middle tier server caches $r _ { \mathrm { c u r r } }$ in its Layer-1 cache. If there is insufficient space in its cache, appropriate rule(s) are removed according to our replacement pol icy and $r _ { \mathrm { c u r r } }$ goes into the cache. Each rule is cached along with additional information on timestamp, size of the rule, and the request count, to be used in the cache replacement algorithm further explained in this paper and comparable to [10,22,29,31,44]. Similar to the server, analogous events occur in the Layer-1 cache at the mobile device.

## 3.5.3. Layers 2 and 3: caching query semantics and results

Since Layer-2 and Layer-3 are mutually dependent, we consider them together in our discussion. When a mobile user requests data corresponding to a multidimensional query $\mathcal { Q } ( r _ { \mathrm { c u r r } } )$ it is implied that the user has already selected the corresponding association rule, cached at the time of observation; therefore the rule<sup>\_</sup>id which is sent to the server sufficiently identifies the rule, minimizing the amount of information to be transmitted. Then we trace the semantics (expression) of $\mathcal { Q } ( r _ { \mathrm { c u r r } } )$ asked by the user by looking at the levels of individual dimensions. For example consider the following association rule: Product $\mathrm { C a t e g o r y = \mathrm { ^ { \circ } D r i n k s ^ { \circ } \mathrm { \longrightarrow } } }$ Profit = Low where all dimensions except Product are at their topmost (=ALL) level and the antecedent is constructed only from Product $\mathrm { C a t e g o r y = ^ { \circ } D r i n k s ^ { \circ } }$ . It is obvious that the Product dimension needs to be drilled down one level to subcategory, because the user would be interested in looking at the category=<sup>d</sup>Drinks<sup>T</sup> in depth to discover the reasons for low profits. When a mobile user requests an OLAP query expression $\mathcal { Q } ( r _ { \mathrm { c u r r } } )$ the Layer-2 cache is searched first. If found, the corresponding query results are extracted from the Layer-3 cache (which operates similarly to Layer-2 cache) and presented to the user, otherwise the request moves on to the server or even to the data warehouse and $\mathcal { Q } ( r _ { \mathrm { c u r r } } )$ is sent back to the server and then to the mobile device possibly invoking the replacement policy.

It is important to note that our multi-layered caching mechanism fits the characteristics of both the mobile device and the middle-tier server: On mobile devices the cached data represent the individual client’s browsed data, while on the server they represent aggregate requests from numerous clients.

## 3.5.4. Cache replacement policy

Our cache replacement policy is used when there is not enough free space in the cache to accommodate requested data. To store an association rule $r _ { \mathrm { c u r r } }$ into the Layer-1 cache with insufficient space, we must first search for the candidate rule(s) to be removed based on three metrics, namely timestamp, size, and the request count. Every metric is assigned a weight value $w _ { i }$ such that $\sum w _ { i } = 1$

The rules in the cache are organized in a specific order according to their individual ranks for each metric. A rank $r k _ { j }$ for rule $r _ { j }$ is a numeric value ranging from 1 to $p ,$ , where $p$ is the total number of rules in the cache. For example, $r k _ { j } = 1$ identifies the highest ranking, whereas $\boldsymbol { r } \boldsymbol { k } _ { j } { = } p$ is the lowest ranking. When we consider the timestamp metric, we order the rules in decreasing order of time. Considering size as our metric, we order the rules in decreasing order of their size. The size of a rule is calculated as (rule attributes)  (average size of rule in bytes) where rule attributes is the total number of attributes in the antecedent and consequent portions of the rule. The largest rule in size is assigned a rank $r k _ { j } = 1$ , keeping larger rules in the cache and evicting smaller ones to maintain the highest possible number of rules in the cache. Lastly for the request count metric, we order rules in decreasing order of request count, so that the rule with the highest number of requests is assigned a rank $r k _ { j } = 1$ , keeping frequently visited rules in the cache, while replacing less frequently visited rules. Based on the rank values for all the three metrics, we calculate the overall retention cost, $r c _ { j } ,$ for rule $r _ { j }$ using the following equation:

$$
r c _ {j} = \sum_ {i = 1} ^ {3} w _ {i} r k _ {j}\tag{5}
$$

Rules with high retention costs are removed from the cache to accommodate the new rule $r _ { \mathrm { c u r r } }$ More details on the cache replacement algorithms are presented in the pseudo-code below.

Box 1

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Layer-1 cache replacement algorithm
Algorithm: Cache Replacement Policy for Layer-1
Input:  $r_{curr}$ , the current association rule to be cached
Procedure:
C-L1 $_{avail}$  available cache size for Layer-1;
stat( $r_{curr}$ )cache statistics for  $r_{curr}$ ;
s( $r_{i}$ )size of  $r_{i}$ ;
rc( $r_{i}$ )retention cost for an association rule
 $r_{i}$  in the cache;
if  $r_{curr}$  in cache
    update stat( $r_{curr}$ );
elsif  $r_{curr}$  not in cache and s( $r_{curr}$ ) = C-
L1 $_{avail}$ ;
    cache  $r_{curr}$ ;
elsif  $r_{curr}$  not in cache and s( $r_{curr}$ ) &gt; C-
L1 $_{avail}$ 
    while C-L1 $_{avail}$ &lt;s( $r_{curr}$ )
    seek candidate rule  $r_{m}$  where
    rc( $r_{m}$ ) = max( $rc(r_{i})$ );
    remove  $r_{m}$  from cache;
    C-L1 $_{avail}$  + = s( $r_{m}$ );
    end while;
    cache  $r_{curr}$ ;
end if;
recalculate rc( $r_{i}$ ) for the cached rules;

The two cache replacement algorithms for Layer-1 on one hand, and Layer-2, Layer-3 on the other are similar as shown in the pseudo-code. An in-depth presentation of our caching policies and specific implementation details is found in [27].
</div>

## 4. System implementation

Our prototype implementation utilizes Oracle9i software for building the data warehouse in our architecture [34]. We used the grocery database available with the Star Tracker application in Data Warehouse Toolkit [25] and we executed multidimensional queries on the Product, Store, and Time dimensions. The multidimensional results were preprocessed and fed into the Weka 3—Machine Learning Software, which analyzed and produced data mining results [58]. The middle-tier server consists of application software and Java Server Pages (JSP) using the Tomcat servlet engine [53]. In the third-tier in our architecture consisting of mobile client devices, we take advantage of Pointbase-Micro (a DBMS for handheld devices [37]), to implement end-user applications, caching techniques, and also store association rules and multidimensional queries. Our applications written in J2ME [50] communicate with the middle tier server over HTTP connections through the Tomcat engine.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Layer-2 and Layer-3 cache replacement algorithm
Algorithm: Cache Replacement Policy for Layer-2 and Layer-3
Input:  $r_{curr}$ , the current association rule  $q_{curr}$ , the multidimensional query constructed from  $r_{curr}$ 
qs( $q_{curr}$ ), size of the semantics for  $q_{curr}$ 
qr( $q_{curr}$ ), size of the query results for  $q_{curr}$ 
Procedure:
C-L2 $_{avail}$  available cache size for Layer-2;
C-L3 $_{avail}$  available cache size for Layer-3;
stat( $q_{curr}$ )cache statistics for  $q_{curr}$ ;
rc( $q_{i}$ )retention cost for query  $q_{i}$  in the cache;
if  $q_{curr}$  in cache
    update stat( $q_{curr}$ );
elsif  $q_{curr}$  not in cache and (qs( $q_{curr}$ ) = C-L2 $_{avail}$  and qr( $q_{curr}$ ) = C-L3 $_{avail}$ );
    cache  $q_{curr}$ ;
elsif  $q_{curr}$  not in cache and (qs( $q_{curr}$ ) &gt; C-L2 $_{avail}$  or qr( $q_{curr}$ ) &gt; C-L3 $_{avail}$ )
    while    qs( $q_{curr}$ ) = C-L2 $_{avail}$  and
    qr( $q_{curr}$ ) = C-L3 $_{avail}$ 
    seek candidate query  $q_{m}$  where
    rc( $q_{m}$ ) = max(rc( $q_{i}$ ));
    remove  $q_{m}$  from cache;
    C-L2 $_{avail}$  + = qs( $q_{m}$ );
    C-L3 $_{avail}$  + = qm( $q_{m}$ );
    end while;
    cache  $q_{curr}$ ;
end if;
recalculate rc( $q_{i}$ ) for the cached queries;
End;
</div>

![](/api/attachments/Z3XEH5JC/fulltext/images/0d814d6b1399865c95a4aa7b010d60cb289a8596576e0e749dead8fa7079ec1f.jpg)  
Fig. 5. (a) Association rules for level 1. (b) Data for level 2—subcategory.

A mobile user who is presented with a set of association rules—see Fig. 5(a), selects the rule of interest and then can choose to either delve into OLAP data, or to analyze the mining rules. In our implementation we keep track of what level of concept hierarchy the user is navigating to, which is possible through the relational representation of dimensions and association rules. For example, if the user is viewing OLAP data for state = <sup>d</sup>CA<sup>T</sup> and would like to investigate the corresponding association rules, the user can simply select the rule. The system has the knowledge that the user is presently looking at the cube for the store dimension at level 2 (see Table 1) and displays the related rules on the screen of the mobile device.

We have used a PalmOS Emulator in our system to demonstrate its functionality. In Fig. 5(a), the user is browsing the data at level 1 for all three dimensions. The corresponding association rules for this scenario are presented on the screen in decreasing order of strength (in support and confidence) starting with the strongest rule at the top. If the user clicks on the rule (Product Category = <sup>d</sup>Drinks<sup>T</sup>YProfit = Low), the system will display underlying multidimensional data. Since this particular association rule has only the Product dimension at level 1 (category), the next screen shown in Fig. 5(b) drills down on product category to level 2 (subcategory), while all other dimensions are kept at their present level. Let us now assume that the user is interested in the precise association rules at this level. The user can click on the <sup>b</sup>Show rules<sup>Q</sup> button to investigate the related rules. The system notes the appropriate levels for the dimensions (i.e. level 2 for the product dimension, and level 1 for store and time).

The association rules satisfying this scenario are extracted and presented to the user as illustrated in Fig. 6(a). Assuming that the user is interested in the South West sales region, the user will select this rule, click on the <sup>b</sup>Explore<sup>Q</sup> button, and will see profit data grouped by year and product subcategory filtered for sales region = South<sup>\_</sup>West, as shown in Fig. 6(b). Visualizing association rules with more than three dimensions is not difficult. However, visualizing the corresponding data with three or more dimensions is a challenging problem. We address this by using the page dimension for displaying dimensions higher than two, as is customary in many OLAP products using tabular displays for multi-dimensional data.

## 5. Experimental results

In this section we describe several experiments testing the performance of our algorithms. In Section

![](/api/attachments/Z3XEH5JC/fulltext/images/5f840509ced2ee52c59174cbf2ba167013fb00d23ed8ec9f1845678ea1bfee0a.jpg)  
Fig. 6. (a) Rules for level 2—product, and level 1—store, time. (b) Filtered results.

5.1 we describe performance validation of data cube traversal using association rules and compare it with traditional OLAP; in Section 5.2 we discuss performance results for the multi-layered caching proposed in this paper. The experiments were based on the grocery data provided in [25].

## 5.1. Association rule-based exploration of data cubes

The performance testing was done by looking at the size of the dataset (space analysis) and the time taken to respond to user queries. In traversing multidimensional data cubes, as the number of dimensions and levels of dimensional hierarchies increase, the candidate dataset grows geometrically making it difficult to choose among navigation paths. Thus, in our experiments we varied the number of dimensions as well as dimensional hierarchies for both traditional OLAP and our approach.

The performance is shown in Fig. 7, where OLAP-L and AR-L denote traditional OLAP and our association rule-based system respectively, denoting the hierarchy level with a number following L. As shown in Fig. 7, our approach outperforms traditional OLAP by a factor of eight in terms of the size of the candidate dataset for a three-dimensional data cube and by a factor of 10 for a five-dimensional data cube.

Fig. 8 compares the traditional OLAP system with our association rule-based system on query execution time. In our methodology, there are three ways that a user can navigate though a multi-dimensional data cube. First the user can only rely on the association rules, which we refer to as AR-Rule. In this case the execution time is reduced by 78% for one level of dimensional hierarchy. When the dimensional hierarchies are two or three levels, navigating through the rules saves the total time by about 85% and 75% respectively. Furthermore, AR-Query and AR-Total represent the time taken to execute the query to retrieve the dataset and the total time of execution for retrieving the rule and the query. This is the worstcase scenario in our methodology, where the total reduction in execution time is about 20% for dimensional hierarchies with one level, 11% for two levels, and 15% for three levels, as compared to traditional OLAP system.

![](/api/attachments/Z3XEH5JC/fulltext/images/11ab05070a6568bf3419f37fa3aca383c0fc91baecae5985032b6449b3d2cec0.jpg)  
Fig. 7. Data size under different dimensions.

![](/api/attachments/Z3XEH5JC/fulltext/images/6876c115175f419d71c3b697e403cf45eeabdbafca8325b590388c46bdf51ed1.jpg)  
Fig. 8. Response time under dimensional hierarchies.

## 5.2. Multi-layered caching

We present three metrics indicating the performance of our multi-layered cache: the number of nodes visited while navigating the data cube, cache hit ratio, and bandwidth consumption. Fig. 9 studies the behavior of our multi-layered caching (MLC) against an OLAP system supported by the Least

Recently Used (LRU) caching policy. AR-L1 refers to our proposed Layer-1 cache replacement policy on the mobile device, while AR-L2L3 refers to the Layer 2 and 3 caches together since they are mutually dependent. We compare the number of nodes visited along a path from a source node (starting point within the cube) to a target node (the final destination). We varied the cache size from 8 KB to 56 KB in our experiments. In each experiment, the cache size is kept the same for OLAP and MLC respectively.

Fig. 9(a) depicts the comparison of the total node visits for three replacement policies under varying cache size. We observe that both AR-L1 and AR-L2L3 perform better than OLAP-LRU by significantly reducing the total number of node visits. For example, given a cache size of 16 KB, AR-L1 and AR-L2L3 show a reduction in the node visits by about 63% and 54% respectively, when compared with OLAP-LRU.

Fig. 9(b) illustrates the cache hit ratio comparisons for the three replacement policies. It shows that AR-L1 and AR-L2L3 achieved a higher cache hit ratio than OLAP-LRU. For a cache size of 16 KB, AR-L1 and AR-L2L3 show an improvement of about 43% and 30% on cache hits over OLAP-LRU policy.

Fig. 10 compares the total bandwidth consumption (data transferred in KB between the server and the client) for MLC against an OLAP-LRU system. AR-L1 indicates the total data size requested while navigating through the association rules. We observe that navigating through the association rules consumes a very small (almost negligible) bandwidth compared to OLAP-LRU. AR-L2L3 represents the total bandwidth for query expression and results. AR-MLC is the sum of AR-L1 and AR-L2L3. We see that AR-MLC performs significantly better than OLAP-LRU. For example AR-MLC shows a reduction of over 62% in bandwidth consumption for a cache size of 24 KB.

![](/api/attachments/Z3XEH5JC/fulltext/images/65403155c2a525a2f44a1f82f745a680fec8232f926ff0339d830a0d3b6a25b8.jpg)

(b)  
![](/api/attachments/Z3XEH5JC/fulltext/images/ee1f49636cec5f382e0160ddef4c0ff281a8c0a19b147c273de81ecd2bc85a59.jpg)  
Fig. 9. Comparison on node visits and cache hit ratio.

![](/api/attachments/Z3XEH5JC/fulltext/images/152a3a5fb75f3aff898beccbb890f85ed3b448f849b081fe90b4d9a2a4af75ec.jpg)  
Fig. 10. Bandwidth consumption.

## 6. Conclusions and future work

In this paper, we proposed a methodology, which combines OLAP technology with association rules for decision makers using mobile devices. We addressed the problem of navigating through a very large search space with very a low capacity input/output device. Our approach prunes the search space by providing the decision maker insights into the patterns in the data through association rules. We described a multi-tier architecture and a multi-layered caching mechanism. The mobile cache reduces wireless data exchange between the mobile client and the middle-tier server. The server cache further decreases the amount of data processing time by keeping a copy of the requested data in the server cache, and minimizes communication with the data warehouse. We demonstrated the benefits of our methodology for rule-based cube exploration and caching mechanism through experimental results.

We continually try to improve on our work and minimize its limitations. First it only considers association rules, which, as we have explained in the paper, is at the most appropriate level for most decision-making situations. Although the framework can accommodate data mining methods such as clustering and classification, the paper does not address them. Other useful techniques for decision makers include outlier detection and visualization, which are also beyond the scope of this paper.

There are specific issues that we need to discuss regarding our caching mechanism. First, we assume that the data warehouse is being updated once per day; hence the cached data may need to be refreshed daily. We give the responsibility to the user to decide when to refresh the local cache: either on a daily basis (assuming cached data are invalidated) or on demand. Second, the memory size of the local device (hence the maximum amount of the cached data) plays a significant role in the efficiency of our system. Modern PDAs are equipped with memory sizes big enough to hold tens of megabytes of data, and if we consider external storage in the form of flash memory it may increase even further. However, there is always the possibility of having more incoming data than the capacity of the entire cache. Cases like this are considered unrealistic since at any rate it would take too long to transmit huge amounts of data to the device, therefore we choose to ignore such illformed scenarios for mobile environments.

We are continuing our research on providing decision support using association rules in mobile environments. We are presently exploring additional issues involved in caching multidimensional data, mobile cache management, and content representation on mobile devices. We also plan to explore a fully distributed ad hoc network of mobile devices for a flexible and distributed cache mechanism.

## References

[1] J. Ang, S.H.T. Thompson, Management issues in data warehousing: insights from the Housing Development Board, Decision Support Systems 29 (2000) 12– 30.

[2] D. Barbara´, T. Imielinski, Sleepers, workaholics: caching strategies in mobile environments, ACM SIGMOD International Conference on Management of Data, Minneapolis, 1994, pp. 1– 12.

[3] A. Bauer, W. Hu¨mmer, W. Lehner, An alternative relational OLAP modeling approach, Proceedings of the International Conference on Data Warehousing, Knowledge Discovery, 2000, pp. 189–198.

[4] M. Bouzeghoub, F. Fabret, M. Matulovic, Modeling data warehouse refreshment process as a workflow application, Proceed-

ings of the International Workshop on Design, Management of Data Warehouses, Heidelberg, Germany, 1999, pp. 6:1 – 6:12.

[5] C.Y. Chan, Y.E. Ioannidis, Bitmap index design and evaluation, Proceedings of ACM SIGMOD, Seattle, USA, 1998, pp. 355–366.

[6] B.Y.L. Chan, A. Si, H.V. Leong, Cache management for mobile databases: design and evaluation, Proceedings of the 14th International Conference on Data Engineering, Orlalndo, USA, 1998, pp. 54 – 63.

[7] Q. Chen, Mining exceptions and quantitative association rules in OLAP data cubes. MSc Thesis, Simon Fraser University, Canada (1999).

[8] Y.-W. Choong, D. Laurent, P. Marcel, Computing appropriate representations for multidimensional data, Proceedings of ACM 4th International Workshop on Data Warehousing, OLAP, Atlanta, Georgia, USA, 2001, pp. 16–23.

[9] S. Dar, M.J. Franklin, B.T. Jonsson, D. Srivastava, M. Tan, Semantic data caching and replacement, Proceedings of the International Conference on Very Large Databases, 1996, pp. 330 – 341.

[10] P.M. Deshpande, K. Ramasamy, A. Shukla, J.F. Naughton, Caching Multidimensional Queries Using Chunks, ACM SIG-MOD, Seattle, WA, USA, 1998, pp. 259– 270.

[11] A. Elmagarmid, J. Jing, A. Helal, C. Lee, Scalable cache invalidation algorithms for mobile data access, IEEE Transactions on Knowledge, Data Engineering 15 (2003) 1498– 1511.

[12] M. Golfarelli, D. Maio, S. Rizzi, Applying vertical fragmentation techniques in logical design of multidimensional databases, Proceedings of the International Conference on Data Warehousing and Knowledge Discovery, Greenwich, 2000, pp. 11– 23.

[13] H. Gupta, I.S. Mumick, Selection of views to materialize under a maintenance-time constraint, International Conference on Database Theory, Jerusalem, Israel, 1999, pp. 453 – 470.

[14] H. Gupta, V. Harinarayan, A. Rajaraman, J. Ullman, Index selection for OLAP, Proceedings of the International Conference on Data Engineering, Birmingham, U.K., 1997, pp. 208– 219.

[15] A. Gupta, I.S. Mumick, J. Rao, K.A. Ross, Adapting materialized views after redefinitions: techniques and a performance study, Information Systems, Special issue on Data Warehousing (2001) 262–323.

[16] J. Han, Towards on-line analytical mining in large databases, ACM SIGMOD (1998) 97–107.

[17] J. Han, S. Chee, J. Chiang, Issues for on-line analytical mining of data warehouses, Proceedings of the 1998 SIGMOD Workshop on Research Issues on Data Mining, Knowledge Discovery, Seattle, Washington, 1998, pp. 2:1 – 2:5.

[18] C. Hurtado, A. Mendelzon, Reasoning about summarizability in heterogeneous multidimensional schemas, Proceedings of the International Conference on Database Theory, 2001, pp. 375– 389.

[19] T. Imielinski, B.R. Badrinath, Mobile wireless computing: challenges in data management, Communications of the ACM, 1994, pp. 18– 28.

[20] W.H. Inmon, Building the Data Warehouse, John Wiley & Sons, New York, 1996.

[21] P. Kalnis, D. Papadias, Proxy-server architectures for OLAP, ACM SIGMOD (2001) 367 – 378.

[22] P. Kalnis, W.S. Ng, B.C. Ooi, D. Papadias, K.L. Tan, An Adaptive Peer-To-Peer Network for Distributed Caching of OLAP Results, ACM SIGMOD, Wisconsin, USA, 2002, pp. 25 – 36.

[23] O. Kaser, D. Lemire, Attribute value reordering for efficient hybrid OLAP, Proceedings of the 6th ACM international workshop on Data warehousing and OLAP, New Orleans, USA, 2003, pp. 1– 8.

[24] A.M. Keller, J. Basu, A predicate-based caching scheme for client–server database architectures, VLDB Journal 5 (1996) 35– 47.

[25] R. Kimball, The Data Warehouse Toolkit, Second ed., 2002.

[26] Y. Kotidis, N. Roussopoulos, DynaMat: a dynamic view management system for data warehouses, Proceedings of the 1999 ACM SIGMOD International Conference on Management of Data, Philadelphia, USA, 1999, pp. 371– 382.

[27] N. Kumar, G. Karabatis, A. Gangopadhyay, Multi-layer caching for mobile devices in OLAP environments. Technical Report, Information Systems, UMBC (2003).

[28] Y.E. Lee, I. Benbasat, Interface design for mobile commerce, Communications of the ACM 46 (2003) 48– 52.

[29] K. Lee, H.V. Leong, A. Si, Semantic query caching in a mobile environment, ACM SIGMOBILE Mobile Computing, Communications Review, 1999, pp. 28–36.

[30] D. Lemire, Wavelet-based relative prefix sum methods for range sum queries in data cubes, Proceedings of the Conference of the Centre for Advanced Studies on Collaborative Research, Toronto, Canada, 2002, pp. 1 –6.

[31] H.V. Leong, A. Si, On adaptive caching in mobile databases, ACM Symposium on Applied Computing, San Jose, California, USA, 1997, pp. 302–309.

[32] P. Marcel, Modeling, querying multidimensional databases: an overview, Networking, Information Systems Journal 2 (1999) 515– 548.

[33] A. Mendelzon, A. Vaisman, Temporal queries in OLAP, Proceedings of Very Large Databases, Cairo, 2000, pp. 242 – 253. [34] Oracle, Oracle9i

[35] C.-S. Park, M.H. Kim, Y.-J. Lee, Rewriting OLAP queries using materialized views and dimension hierarchies in data warehouses, Proceedings of the International Conference on Data Engineering, 2001, pp. 515 – 523.

[36] F. Perich, A. Joshi, T. Finin, Y. Yesha, On data management in pervasive computing environments, IEEE Transactions on Knowledge, Data Engineering 16 (2004) 621–634.

[37] Pointbase, Pointbase Micro Edition, 4.7 ed.

[38] C.K. Poon, Dynamic orthogonal range queries in OLAP, Theoretical Computer Science 296 (2003) 487– 510.

[39] Q. Ren, M.H. Dunham, V. Kumar, Semantic caching and query processing, IEEE Transactions on Knowledge, Data Engineering 15 (2003) 192– 210.

[40] J. Sairamesh, S. Goh, I. Stanoi, C.S. Li, S. Padmanabhan, Self-managing, disconnected processes and mechanisms for mobile e-business, Proceedings of the Second International Workshop on Mobile Commerce, Atlanta, Georgia, USA, 2002, pp. 82– 89.

[41] S. Sarawagi, Indexing OLAP data, IEEE Data Engineering Bulletin 20 (1) (1997) 36 – 43.

[42] S. Sarawagi, R. Agrawal, N. Megiddo, Discovery-driven exploration of OLAP data cubes, Proceedings of the International Conference on Extending Database Technology, Valencia, Spain, 1998, pp. 168 – 182.

[43] S. Sarker, J.D. Wells, Understanding mobile handheld device use and adoption, Communications of the ACM 46 (2003) 35– 40.

[44] P. Scheuermann, J. Shim, R. Vingralek, WATCHMAN: a data warehouse intelligent cache manager, The VLDB Journal (1996) 51– 62.

[45] M.A. Sharaf, P.K. Chrysanthis, Facilitating mobile decision making, Proceedings of the ACM MobiCom Workshop on Mobile Commerce, Atlanta, Georgia, USA, 2002, pp. 45–53.

[46] M.A. Sharaf, P.K. Chrysanthis, Semantic-based delivery of OLAP summary tables in wireless environments, Conference on Information Knowledge Management, McLean, Virginia, USA, 2002, pp. 84–92.

[47] M. Sharaf, Y. Sismanis, A. Labrinidis, P. Chrysanthis, N. Roussopoulos, Efficient dissemination of aggregate data over the wireless web, ACM International Workshop on the Web Databases, San Diego, California, 2003, pp. 93 – 98.

[48] J.R. Smith, C.-S. Li, A. Jhingran, A wavelet framework for adapting data cube views for OLAP, IEEE Transactions on Knowledge, Data Engineering 16 (2004) 552–565.

[49] I. Stanoi, D. Aggarwal, A.E. Abbadi, S.H. Phatak, B.R. Badrinath, Data warehousing alternatives for mobile environments, Proceedings of the Workshop on Data Engineering for Mobile Wireless Access, Seattle, Washington, USA, 1999, pp. 110–115.

[50] Sun, Java 2 Platform Micro Edition.

[51] D. Theodoratos, T. Sellis, Designing data warehouses, Data Knowledge Engineering 31 (3) (1999) 279– 301.

[52] D. Theodoratos, T. Sellis, Dynamic data warehouse design, Proceedings of the International Conference on Data Warehousing, Knowledge Discovery, Florence, Italy, 1999, pp. 1 – 10.

[53] Tomcat, Tomcat Servlet Engine.

[54] A. Vaisman, A. Mendelzon, A temporal query language for OLAP: implementation and a case study, International Workshop on Database Programming Languages, Rome, Italy, 2001, pp. 78–96.

[55] V. Venkatesh, V. Ramesh, A.P. Massey, Understanding usability in mobile commerce, Communications of the ACM 46 (2003) 53– 56.

[56] J.S. Vitter, M. Wang, Approximate Computation of Multi dimensional Aggregates of Sparse Data using Wavelets, ACM SIGMOD, Philadelphia, Pennsylvania, USA, 1999, pp. 193– 204.

[57] H.J. Watson, C. Fuller, T. Ariachandra, Data warehouse governance: best practices at Blue Cross, Blue Shield of North Carolina, Decision Support Systems 38 (2004) 435–450.

[58] Weka, Weka 3—Data mining with open source machine learn ing software in Java.

[59] O. Wolfson, P. Sistla, S. Dao, K. Narayanan, R. Raj, View maintenance in mobile computing, ACM SIGMOD Record 24 (4) (1995) 22– 27.

[60] J. Xu, Q. Hu, W.-C. Lee, D.L. Lee, Performance evaluation of an optimal cache replacement policy for wireless data dissemination, IEEE Transactions on Knowledge, Data Engineering 16 (2004) 125– 139.

[61] J. Yang, K. Karlapalem, Q. Li, Algorithms for materialized view design in data warehousing environment, Proceedings of the International Conference on Very Large Databases, 1997, pp. 136 – 145.

[62] J. Yang, J. Widom, Making temporal views self-maintainable for data warehousing, Proceedings of the 7th International Conference on Extending Database Technology, Konstanz, Germany, 2000, pp. 395 – 412.

![](/api/attachments/Z3XEH5JC/fulltext/images/1e90ec558e01cd38e2e8776b206c6e5ca64c513ab4812350b8eae1af8747787a.jpg)

Navin Kumar is a PhD student at the Department of Information Systems at the University of Maryland, Baltimore County. He received his BTech in Industrial Engineering from Indian Institute of Technology, Kharagpur, and MS in Information Systems from the University of Maryland, Baltimore County. His main research interests are in data warehousing solutions, data mining, and M-Commerce.

![](/api/attachments/Z3XEH5JC/fulltext/images/5fc8c5dcdac781c18b7b96fd703fe948c729a0a5009fec48dad38dd3fd76736d.jpg)

Aryya Gangopadhyay is an Associate Professor of Information Systems at the University of Maryland Baltimore County (UMBC). He has a PhD in Computer Information Systems from Rutgers University. His research interests include decision support using data warehousing and mining, and database applications in geographic information systems and healthcare informatics. He has co-authored and edited three books, many book chapters, and numerous

papers in journals. He can be reached at gangopad@umbc.edu.

![](/api/attachments/Z3XEH5JC/fulltext/images/a4f5076ccc5b49f216c3c93139dbad2815ca8468fdc723a1b842d2db42d3db4d.jpg)

George Karabatis is an Assistant Professor of Information Systems at the University of Maryland, Baltimore County (UMBC). He holds degrees in Computer Science (PhD and MS) and Mathematics (BS). He is pursuing research on various aspects of Information Technology related to databases systems, bioinformatics and applications for wireless handheld devices. Prior to his current appointment he was a Research Scientist at Telcordia Technologies

(formerly Bellcore) where he led several telecommunications projects involving database related technologies. His work has been published in journals, conference proceedings and book chapters.
