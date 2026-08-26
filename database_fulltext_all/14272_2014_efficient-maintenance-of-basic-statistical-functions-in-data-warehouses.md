---
otero_id: 14272
otero_key: "GKBR5SA6"
title: "Efficient maintenance of basic statistical functions in data warehouses"
authors: "Yeu-Shiang Huang; Do Duy; Chih-Chiang Fang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses

Yeu-Shiang Huang <sup>a,</sup>⁎, Do Duy <sup>a</sup>, Chih-Chiang Fang <sup>b</sup>

<sup>a</sup> Department of Industrial and Information Management, National Cheng Kung University, Taiwan, ROC

<sup>b</sup> Department of Information Management, Shu-Te University, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 5 May 2010 Received in revised form 31 July 2013 Accepted 8 August 2013 Available online xxxx

Keywords: Data warehouse Maintain data warehouse Self-maintainability

## a b s t r a c t

In general, some simple but very meaningful statistical functions are often used to retrieve valuable summary information in corporate databases. However, it is not uncommon that such information is obtained from computerized information systems which spend a great deal of time calculating the large volume of collected data. In practice, such data is usually stored in a data warehouse in which a large number of summary tables or materialized aggregate views are built in order to improve the system performance. Upon changes, most notable new transactional data are collected from various data sources, and all summary tables in the data warehouse that correspond to the transactional data must be updated accordingly. Since the number of summary tables that need to be maintained is often large, ef<sup>fi</sup>ciently maintaining these is thus a critical issue for managing a data warehouse. In this study, an ef<sup>fi</sup>cient maintenance approach to enhance the performance of a data warehouse is proposed, in which some additional auxiliary tables are kept inside a data warehouse with the role of improving the maintenance processes of some statistical functions, such as MIN, MAX, MEAN, and MEDIAN. Finally, a comparative analysis is performed to verify the effectiveness of the proposal method.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Data warehouses are often huge systems which require a very high level maintenance. Any reorganization of the business processes and the source systems may require the data warehouse to change. Updates are often needed in these situations, and more resources are required for maintenance of a data warehouse rather than its development. Views are computed and stored in a database to allow ef<sup>fi</sup>cient querying and analysis of the data, and these are known as materialized views. In order to keep these up to date, it is necessary to maintain the materialized views in response to the changes at the sources. In general, incrementally maintaining a view can be signi<sup>fi</sup>cantly cheaper than recomputing it from scratch, especially if the size of view is large compared to the size of the changes. The problem of <sup>fi</sup>nding such changes in the views based on changes in the base relations is known as the view maintenance problem. Moreover, since statistical functions often play a very important role in the online analytical process (OLAP) in data warehouses, some simple but very meaningful functions are often used to retrieve information. In order to make statistical analysis operations more effective, it is necessary to keep them up to date, which often requires a lot of time and resources. The objective of this study is thus to propose an approach to maintain statistical functions in a data warehouse more ef<sup>fi</sup>ciently, in which some supplementary data are kept with a legacy role. The auxiliary data are organized in a speci<sup>fi</sup>c format that makes them very ef<sup>fi</sup>cient in response to changes in the base tables. In other words, when a base table is changed, the data warehouse will use these auxiliary data to maintain the view instead of reaccessing the entire base table, signi<sup>fi</sup>cantly improving the maintenance processes.

Since data warehouses often contain huge amounts of data, in order to keep performance smooth and constant, maintenance of a data warehouse is crucial. [16] suggested an ef<sup>fi</sup>ciency model for data warehouse operations which contains two major processes (refresh processing and query production), and concluded that only few organizations can obtain good ef<sup>fi</sup>ciency for both processes. While companies may be successful in implementing multi-terabyte data warehouses, it is still dif<sup>fi</sup>cult to translate this investment into useful business knowledge or positive business results. Computing and/or materializing a complete data cube is often expensive, in both time and space, and dif<sup>fi</sup>cult to conduct online. Research has proposed different approaches for dealing with this problem of querying OLAP data cubes [4,14,19]. However, as changes are made to the data sources, the warehouse views must be updated to re<sup>fl</sup>ect this. According to [3,6], the updated view can be either recomputed from scratch or obtained by using incremental maintenance techniques. However, in today's warehouses, the changes to the sources are often not detected and propagated to the warehouse immediately. To ef<sup>fi</sup>ciently deal with changes to the materialized views in relational and deductive database systems, [5] presented a counting algorithm that tracks the number of alternative derivations for each derived tuple in a view. By <sup>fi</sup>rst deleting a superset of the tuples and rederiving some of them, a recursive view can be maintained incrementally. This method was described as the delete and rederive (DRed) algorithm.

For data warehouses that provide global access, even a short period of downtime may not be acceptable. [1] proposed two algorithms called SWEEP and Nested SWEEP to deal with this issue. Both algorithms work without requiring that the data warehouse is quiescent to incorporate the new views. A multi-agent system (MAS) that achieves immediate incremental view maintenance was developed by [21]. [7] proposed an algorithm for ef<sup>fi</sup>ciently computing updates to views without reaccessing the materialization of views. [10] proposed a propagation approach to deal with view maintenance tasks. [9] proposed an approach which employs an extendable multidimensional array to maintain the increment of data cubes with the aim to avoid recomputing the entire data cube. [13] proposed an ef<sup>fi</sup>cient algorithm which can maintain a data cube using only a subset 2<sup>n</sup> delta cuboids.

Incremental maintenance has been studied by [3,22]. In spite of their positive results, view maintenance is still complicated by the fact that the sources are decoupled from the warehouse, so that traditional incremental view maintenance may exhibit anomalies. In this situation, warehouse self-maintainability is desirable. This is the ability of a warehouse to maintain itself without “help” from the underlying databases, i.e., it based only on reported changes to the underlying databases [12]. Auxiliary data is used in order to update materialized views, without accessing the base relation. Research on the construction of auxiliary tables for self-maintainability can be seen in [2,8,15,17,18,20]. According to [12], warehouse independence with respect to queries is the abil ity of the warehouse to answer queries posed to the underlying sources from the warehouse views. Similarly, warehouse independence with respect to updates is the ability of a warehouse to maintain itself based only on reported changes in the underlying sources.

Based on the aforementioned discussion, in this study an ef<sup>fi</sup>cient maintenance approach to enhance the performance of a data warehouse is proposed. The main objective of this study is to avoid reloading all the data in DW completely when calculating some statistical functions is required, no matter if the data are generated from real-time operations or periodical refreshment. In this paper, we maintain some supplementary tables (e.g., auxiliary tables, materialized views) in the DW to keep track of each update, so that the values of required statistical functions, such as MIN, MAX, MEAN, and MEDIAN, can be instantly calculated without a full reloading task. The proposed incremental maintenance approach is statistically proved to be signi<sup>fi</sup>cantly faster than the traditional one (completely reloading and recomputing), especially when the volume of the original data is much larger than that of the changes. Therefore, the proposed approach can be employed in both a periodic data refresh policy or an OLAP environment. This paper is organized as follows: Section 2 considers the maintenance of a data warehouse, Section 3 depicts the development of the proposed approach, Section 4 demonstrates the effectiveness of the proposed approach by performing a numerical experiment, and <sup>fi</sup>nally, Section 5 presents the concluding remarks.

## 2. Maintaining a data warehouse

The data in data warehouses are in the form of data cubes, which allow data to be modeled and viewed in multiple dimensions. To clarify the complex view of data, a simple example is provided. For instance, in order to respond to changes in the business environment, the board of an enterprise, which is specialized in selling, decides to develop a decision support system with the use of a data warehouse. A part of the system is depicted in Fig. 1.

The system is divided into two parts: (1) the dimension and fact tables and (2) materialized view. The <sup>fi</sup>rst part consists of six dimensional tables (Product, Location, City, Supplier, Time, Branch dimensional tables) and one fact table (Sales). The six dimensional tables describe the information about how the product has been sold, and the fact table describes the detailed information of each transaction. Through these six dimensional and fact tables, we are able to know who, and in which region, buys how much of each product. To assist the decision making process, the analysis team may require information about the minimum, maximum and median sales of a product which have been sold in a certain region in a speci<sup>fi</sup>c week. The leader of the data warehouse building team thus decides to materialize these three values in a materialized view, which is called vw\_AggregateValue and has <sup>fi</sup>ve attributes: RegionID, ProductID, MaxQuantity, MinQuantity, and MedianQuantity. While RegionID and ProductID identify the region and product, respectively, MaxQuantity, MinQuantity, and MedianQuantity keep the aggregated values which describe the maximum, the minimum, and the median amounts of a product sold in a certain region. For example, the <sup>fi</sup>rst tuple in Table 1 tells us that the maximal quantity of laptop computers (ProductID = 004) sold in Tainan city (RegionID = 003) is 1000.

Suppose that one day, the maximal quantity of laptop computers sold in Tainan city needs to be deleted from the fact table “Sales” in the transactional data in the data warehouse. To keep vw\_AggregateValue up to date in response to the change in the Sales table, the system engine has to scan the entire table to obtain the new maximum. Since the Sales table is very large, the scanning process will take a long time to complete. Therefore, a more ef<sup>fi</sup>cient way of maintaining vw\_AggregateValue is a critical issue for an effective data warehouse

The update operation is actually a combination of two operations: <sup>fi</sup>rst, the old record will be deleted, and then a new record will be inserted. Therefore, in this study, only these two operations are considered. Self-maintainability is the ability of a warehouse to maintain itself without any “help” from the underlying databases. It can adapt to an OLAP environment. Once the fact table is changed, the mechanism of self-maintainability would automatically be implemented. For example, every time a customer buys an amount of laptop computers, this new

![](/api/attachments/GKBR5SA6/fulltext/images/3b603e06cf7b16595f11c7774f4b5959ea482f33f8009592f3e1bd2139558cd0.jpg)  
Fig. 1. The example data warehouse architecture

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

Materialized view of vw\_AggregateValue.

<table><tr><td>RegionID</td><td>ProductID</td><td>MaxQuantity</td><td>MinQuantity</td><td>MedianQuantity</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td>003</td><td>004</td><td>1000</td><td>5</td><td>123</td></tr><tr><td>004</td><td>005</td><td>30</td><td>2</td><td>13</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td></tr></table>

data is <sup>fi</sup>rst inserted into the Sales table inside the database. The maintenance engine will then compare the new amount of laptop computers with the value in vw\_AggregateValue, if the former is greater than the latter, then the value in vw\_AggregateValue will be replaced by the new one. In such a case, we have a new maximum without reaccessing the base table, and thus the MAX function has the attribute of selfmaintainability for the insert function.

However, every time a record is deleted from the Sales table inside the fact table, the maintenance engine will compare the deleted value with that in vw\_AggregateValue, and if they are equal the old value in the latter will be deleted. At this time, we do not know what the new maximum sales amount of the region is, since the original one has just been deleted. In order to obtain the new maximal value, we have to access and scan the entire base table, and thus the MAX function is not self-maintainable for the delete and insert operation.

If a materialized view includes self-maintainable functions, it can be maintained incrementally, and if not then the maintenance will need to be calculated from scratch. A function is self-maintainable if both its delete and insert operations are self-maintainable. However, a function is semi-self-maintainable if one of its operations, insert or delete, is nonself-maintainable, and a function is non-self-maintainable if both its operations of insert and delete are non-self-maintainable. Based on the above discussion, we can thus see that MEAN is a self-maintainable function, MIN and MAX are semi-self-maintainable functions, and MEDIAN is a non-self-maintainable function.

Given a materialized view $V ( I D s , S _ { 1 } , . . . , S _ { r } )$ and a set of modi<sup>fi</sup>cations $D ( I D s , A _ { 1 } , . . . , A _ { p } )$ , need to be appended to table $T ( I D s , A _ { 1 } , . . . . , A _ { p } )$ inside the data warehouse. The explanations about the symbols or notations used in the SQL command are shown in Fig. 2.

It is assumed that materialized view V has n tuples, and k is a tuple among n tuples. $S _ { ( k , i ) }$ is the summary value in the cell where k is the row identi<sup>fi</sup>cation and i is the column identi<sup>fi</sup>cation. For example, according to Table $2 , S _ { ( 2 , 3 ) } = 1 0 0 0$ , which stands for the maximum amount of laptop computers that has been sold in Tainan in this case.

In general we can calculate $S _ { ( k , i ) }$ <sub>)</sub> by the following SQL command.

## SELECT Aggregate\_Function $\left( A _ { I D s , u } \right)$ FROM T WHERE T.IDs = V.IDs

In other words, $S _ { ( k , i ) }$ keeps the maximum value (or another value, depending on the aggregate function used) among $A _ { ( \mathrm { k , u ) } }$ values of table T. When m tuples from D are inserted into (or deleted from) T, the new value of $\cdot S _ { ( k , i ) }$ will equal

$$
\begin{array}{c} S _ {(k, i)} = \max \Big (a _ {1} ^ {(I D s, u)},..., a _ {n} ^ {(I D s, u)}, a _ {n + 1} ^ {(I D s, u)},..., a _ {n + m} ^ {(I D s, u)} \Big) o r \\ S _ {(k, i)} = \max \Big (a _ {1} ^ {(I D s, u)},..., a _ {n - m} ^ {(I D s, u)} \Big) \end{array}\tag{1}
$$

As mentioned in the previous section, the MEDIAN function is nonself-maintainable, and the MIN and the MAX functions are non-selfmaintainable for the delete operation. Therefore, the problems are formulated as follows:

1. Incrementally maintain $S _ { ( k , i ) } = \operatorname* { m a x } ( a _ { 1 } ^ { ( I D s , u ) } , . . . , a _ { n \mathrm { ~ - ~ } m } ^ { ( I D s , u ) } )$

2. Incrementally maintain $S _ { ( k , i ) } = \operatorname* { m i n } ( a _ { 1 } ^ { ( I D s , u ) } , . . . , a _ { n \mathrm { ~ - ~ } m } ^ { ( I D s , u ) } )$

3. Incrementally maintain $S _ { ( k , i ) } ^ { \dot { S } , \dot { \iota } , \dot { \iota } } = \mathrm { m e d i a n } ( a _ { 1 } ^ { ( I D s , u ) } , . . . , a _ { n } ^ { ( I D s , u ) } , a _ { n + 1 } ^ { ( I D s , u ) } ,$ $a _ { n + m } ^ { ( I D s , u ) } )$ and $S _ { ( k , i ) } = \mathrm { m e d i a n } ( a _ { 1 } ^ { ( I D s , u ) } , . . . , a _ { n - m } ^ { ( I D s , u ) } )$

## 3. Incremental maintenance of basic statistical functions

As speci<sup>fi</sup>ed in the previous section, we can classify statistical functions into self-maintainable, semi-self-maintainable, and non-self maintainable. It is relatively easy to maintain self-maintainable functions. However, in order to maintain semi-self-maintainable and non-self maintainable statistical functions we need to use the auxiliary data as a legacy.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- V is the materialized view
- IDs is the identification attribute (or a set of identification attributes) of the tuple
-  $S_{1},\ldots,S_{r}$  are the aggregate information, which are derived from aggregate functions like MAX, MIN, MEDIAN
- r is the amount of summarized information in view V
- T is the fact table inside the data warehouse
- D is the set of tuples which are waiting to be updated
-  $A_{1},\ldots,A_{p}$  are the attributes of the table T
- P is the number of attribute in table T and D
-  $A_{(IDs,u)}$  is the set of tuples selected by the following SQL command:
SELECT  $A_{u}$  FROM T WHERE T.IDS=V.IDs
where  $A_{u}$  is the selected attribute among  $A_{1}\ldots A_{p}$, and IDs is the identification attribute (or a set of identification attributes)
-  $a_{j}^{(IDs,u)}$  is a member (or a specific attribute) of set  $A_{(IDs,u)}.A_{(IDs,u)}=(a_{1}^{(IDs,u)},\ldots,a_{n}^{(IDs,u)})$
</div>

Fig. 2. The symbols and notations used in SQL command

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

Table 2 Example of data table.

<table><tr><td rowspan="2">k</td><td colspan="5">i</td></tr><tr><td>1RegionID</td><td>2ProductID</td><td>3MaxQuantity</td><td>4MinQuantity</td><td>5MedianQuantity</td></tr><tr><td>1</td><td>001</td><td>002</td><td>50</td><td>3</td><td>30</td></tr><tr><td>2</td><td>003</td><td>004</td><td>1000</td><td>5</td><td>123</td></tr><tr><td>3</td><td>004</td><td>005</td><td>30</td><td>2</td><td>13</td></tr></table>

## 3.1. Maintaining self-maintainable statistical functions

Self-maintainability is the ability of a warehouse to maintain itself without any “help” from the underlying databases, based only on reported changes in the underlying databases. SUM and MEAN are two examples of self-maintainable function. When the base table changes, we do no need to calculate the new mean from the whole table's records. For the insert operation, the new mean can be calculated by the following formula:

$\mathop { \mu _ { n e w } } = \frac { \displaystyle \sum _ { i = 1 } ^ { n } { x _ { i + } \sum _ { j = 1 } ^ { m } x _ { j } } } { \displaystyle n + m } ,$ . For the delete operation, the new mean can be calculated as $\underbrace { \sum _ { i = 1 } ^ { n } x _ { i } - \sum _ { j = 1 } ^ { m } x _ { j } } _ { n - m } ,$ , where n is the total number of elements inside the data warehouse, $\sum _ { i = 1 } ^ { n } x _ { i }$ is the sum of all n elements inside the data warehouse, m is the number of elements which is going to be inserted into or deleted from the data warehouse, and $\sum _ { j = 1 } ^ { m } x _ { j }$ is the sum of all m news element which are going to be inserted into or deleted from the data warehouse.

As can be seen from the previous examples, the new mean can be calculated based only on the existing data and without any help from other sources. There are some differences for the standard deviation (SD) and the variance (VAR) functions. The original variance of elements inside the

$$
s ^ {2} = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}}{n - 1}
$$

data warehouse is calculated as s<sup>2</sup> <sup>i</sup>¼<sup>1</sup> , and when m new tuples are inserted into the data warehouse, the mean of the original dataset n−1 will be changed, which leads to the change $\operatorname { o f } s ^ { 2 }$ . The new variance of the data set caused by the insert operation can be obtained from the following proposition.

Proposition 1. If the original variance of elements inside the data warehouse is $s ^ { 2 } ,$ and m new tuples are inserted into the data warehouse, then the new variance of the data set can be given by

$$
s _ {n e w} ^ {2} = \frac {(n - 1) s _ {\text { OriginalSet }} ^ {2} + n \bar {x} _ {\text { OriginalSet }} ^ {2} + (m - 1) s _ {\text { InsertedSet }} ^ {2} + m \bar {x} _ {\text { InsertedSet }} ^ {2} - \left(\frac {1}{n + m}\right) \left(n \bar {x} _ {\text { OriginalSet }} + m \bar {x} _ {\text { InsertedSet }}\right) ^ {2}}{n + m - 1},\tag{2}
$$

where $s _ { O r i g i n a l S e t } ^ { 2 }$ and $\bar { x } _ { o r i g i n a l S e t }$ respectively denote the variance and the mean of the original dataset (before updating), and $s _ { I n s e r t e d S e t } ^ { 2 }$ and x respectively denote the variance and the mean of the inserted dataset.

Proof. Suppose that the set $\mathsf { D } = \{ x _ { 1 } , x _ { 2 } , x _ { 3 } , . . . , x _ { n } , x _ { n } + \imath , . . . , x _ { n + m } \}$ has $n + m$ elements in which the <sup>fi</sup>rst n elements are from the original data set and the last m elements are from the data set which are about to be inserted. The new variance of the whole data set can thus be calculated as

$$
s _ {n e w} ^ {2} = \frac {\sum_ {i = 1} ^ {n + m} \left(x _ {i} - \bar {x}\right) ^ {2}}{n + m - 1} = \frac {\sum_ {i = 1} ^ {n + m} \left(x _ {i} - \frac {1}{n + m} \sum_ {k = 1} ^ {n + m} x _ {k}\right) ^ {2}}{n + m - 1}.
$$

In order to divide the whole data set into the original data set and the inserted data set, the above equation can be arranged as follows:

$$
s _ {n e w} ^ {2} = \frac {\sum_ {i = 1} ^ {n} x _ {i} ^ {2} + \sum_ {j = n + 1} ^ {n + m} x _ {j} ^ {2} - \left(\frac {1}{n + m}\right) \left(\sum_ {i = 1} ^ {n} x _ {i} + \sum_ {j = n + 1} ^ {n + m} x _ {j}\right) ^ {2}}{n + m - 1}.
$$

$$
\text { Since } \sum_ {i = 1} ^ {n} x _ {i} ^ {2} = (n - 1) s _ {\text { OriginalSet }} ^ {2} + n \overline {{x}} _ {\text { OriginalSet }} ^ {2}, \sum_ {j = n + 1} ^ {n + m} x _ {j} ^ {2} = (m - 1) s _ {\text { InsertedSet }} ^ {2} + m \overline {{x}} _ {\text { InsertedSet }} ^ {2}, \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} = \overline {{x}} _ {\text { OriginalSet}}, \text { and } \frac {1}{m} \sum_ {j = n + 1} ^ {n + m} x _ {j} = \overline {{x}} _ {\text { InsertedSet}},
$$

$$
\text { we   then   have } _ {\text { new }} ^ {2} = \frac {(n - 1) s _ {\text { OriginalSet }} ^ {2} + n \bar {x} _ {\text { OriginalSet }} ^ {2} + (m - 1) s _ {\text { InsertedSet }} ^ {2} + m \bar {x} _ {\text { InsertedSet }} ^ {2} - \left(\frac {1}{n + m}\right) \left(n \bar {x} _ {\text { OriginalSet }} + m \bar {x} _ {\text { InsertedSet }}\right) ^ {2}}{n + m - 1}.
$$

Note that the values $( s _ { O r i g i n a l S e t } ^ { 2 } , \overline { { { x } } } _ { O r i g i n a l S e t } )$ can be calculated and stored in the Auxiliary table in advance while the former updating process started to enhance the computation performance of the data warehouse. Similarly, when m tuples are deleted from the database, the new variance can be obtain from the following proposition.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

Proposition 2. If the original variance of elements inside the data warehouse is $s ^ { 2 } ,$ and m tuples are deleted from the data warehouse, then the new variance of the data set can be given by

$$
s _ {n e w} ^ {2} = \frac {(n - 1) s _ {O r i g i n a l S e t} ^ {2} + n \bar {x} _ {O r i g i n a l S e t} ^ {2} - (m - 1) s _ {D e l e t e d S e t} ^ {2} - m \bar {x} _ {D e l e t e d S e t} ^ {2} - \left(\frac {1}{n - m}\right) \left(n \bar {x} _ {O r i g i n a l S e t} + m \bar {x} _ {D e l e t e d S e t}\right) ^ {2}}{n - m - 1},\tag{3}
$$

where $s ^ { 2 } { \mathrm { _ { d e l e t e d S e t } } }$ and $\overline { { x } } _ { d e l e t e d S e t }$ respectively denote the variance and the mean of the deleted dataset.

Proof. Suppose that the set $\mathsf { D } = \left\{ x _ { 1 } , x _ { 2 } , x _ { 3 } , . . . , x _ { n } - m , x _ { n - m + 1 } , . . . , x _ { n } - 1 , x _ { n } \right\}$ has n elements in which the <sup>fi</sup>rst n − m elements are from the original data set and the last m elements are from the data set which are about to be deleted. The new variance of the whole data set can be calculated as

$$
s _ {n e w} ^ {2} = \frac {\sum_ {i = 1} ^ {n - m} \left(x _ {i} - \overline {{x}}\right) ^ {2}}{n - m - 1} = \frac {\sum_ {i = 1} ^ {n - m} \left(x _ {i} - \frac {1}{n - m} \sum_ {k = 1} ^ {n - m} x _ {k}\right) ^ {2}}{n - m - 1}.
$$

In order to divide the whole data set into the original data set and the deleted data set, the above equation can be arranged as follows:

$$
\begin{array}{l} s _ {n e w} ^ {2} = \frac {\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \sum_ {j = n - m + 1} ^ {n} x _ {j} ^ {2} - \left(\frac {1}{n - m}\right) \left(\sum_ {i = 1} ^ {n} x _ {i} - \sum_ {j = n - m + 1} ^ {n} x _ {j}\right) ^ {2}}{n - m - 1}. \\ \text {Since} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} = (n - 1) s _ {\text {OriginalSet}} ^ {2} + n \bar {x} _ {\text {OriginalSet}} ^ {2}, \sum_ {j = n - m + 1} ^ {n} x _ {j} ^ {2} = (m - 1) s _ {\text {DeletedSet}} ^ {2} + m \bar {x} _ {\text {DeletedSet}} ^ {2}, \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} = \bar {x} _ {\text {OriginalSet}}, a n d \frac {1}{m} \sum_ {j = n - m + 1} ^ {n} x _ {j} = \bar {x} _ {\text {DeletedSet}}, \\ \text {we then have s_{new} ^{2}} = \frac {(n - 1) s _ {\text {OriginalSet}} ^ {2} + n \bar {x} _ {\text {OriginalSet}} ^ {2} - (m - 1) s _ {\text {DeletedSet}} ^ {2} - m \bar {x} _ {\text {DeletedSet}} ^ {2} - \left(\frac {1}{n - m}\right) \left(n \bar {x} _ {\text {OriginalSet}} + m \bar {x} _ {\text {DeletedSet}}\right) ^ {2}}{n - m - 1}. \end{array}
$$

From Eqs. (2) and (3), we recognize that if we have $\sum _ { i = 1 } ^ { n } \left( x _ { i } - \overline { { x } } _ { O r i g i n a l S e t } \right) ^ { 2 }$ (from now on called DEV) inside the data warehouse we can calculate the new variance without any other help. By keeping DEV inside the data warehouse we can make the variance function become self-maintainable, and the maintenance process can be signi<sup>fi</sup>cantly improved, since we do not have to recalculate everything from scratch

## 3.2. Maintaining semi-self-maintainable statistic functions

The process of maintaining semi and non-self-maintainable statistical functions to auxiliary data when data modi<sup>fi</sup>cation occurs from fact tables is depicted in Fig. 3.

In this process, the auxiliary data and the materialized views are only initialized at the <sup>fi</sup>rst time, and after <sup>fi</sup>nalizing the initialization stage, the auxiliary data will be kept up to date by a speci<sup>fi</sup>c algorithm. Whenever the data warehouse needs to be updated in response to the changes from the sources (fact tables), the auxiliary table and the materialized view will be maintained at the same time for the synchronization between the transactional data and the data warehouse.

## 3.2.1. Structure of the auxiliary data for semi-self-maintainable functions

For each attribute which needs to be maintained, two columns are added to the auxiliary table. The <sup>fi</sup>rst column is named Val, which keeps the smallest values for the MIN function (the biggest values for the MAX function) of the fact table, and which are stored in ascending order (descending order for the MAX function). The second column is named Frq which keeps the frequency of the corresponding value in the fact table with its dimensional tables. Moreover, the Identi<sup>fi</sup>cation tag is used for identifying the dimensional condition (i.e., a set of dimensional attributes' value). All the

![](/api/attachments/GKBR5SA6/fulltext/images/cf02e39e458e0c96e23ec1595fce9e212cee7af532ad453fb4e03116328797bf.jpg)  
Fig. 3. The process of maintaining auxiliary data and materialized views.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

Y.-S. Huang et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/GKBR5SA6/fulltext/images/7225deca23cd602c27237bba41e41cb4f88a51f0d1099798e8230accef81a608.jpg)  
Fig. 4. The structures of auxiliary data, materialized view and fact table.

statistical characteristics (e.g., Mean. Variance. Max. Min. Median) are calculated under the criterion and stored in the space of statistical measure ment. The structures of the auxiliary data, materialized view and fact table are depicted in Fig. 4.

The auxiliary table for the MAX function is initialized by a SQL command which is as follows:

SELECT TOP k A AS Val, Count(A ) AS Frq INTO AuxiliaryTableName

FROM DataSource

GROUP BY A

ORDER BY A DESC

Note that A is the name of the attribute which needs to be maintained. We can also initialize the auxiliary table for the MIN function by replacing DESC with ASC in the last line of the SQL command. Note that k is the number of tuples that the administrator has to keep, and it implies the possible number which exists in the target attribute of the fact table, How much data that the auxiliary table should keep depends on three characteristics of the fact table. The <sup>fi</sup>rst, and perhaps the most important characteristic that needs to be considered, is the variety of data. In other word, the size of the auxiliary table depends on the possible combinations of numbers of the target attribute value. The more varied the data, the bigger the auxiliary table needed. Consider a fact table consisting of 100,000 tuples with 10,000 different values and a fact table that consists of the same amount of tuples with just 1000 different values. Since the variation ranges of these two fact tables are different, if we keep the same amount of auxiliary data for both, the probability that we will encounter a value which is not in the auxiliary table will be higher for the fact table with more variation. Therefore, the num ber of tuples in the auxiliary table for the fact table with 10,000 different values should be higher than that for the table with only 1000 different values.

Another important characteristic we need to take into consideration is the size of modi<sup>fi</sup>cation. The more modi<sup>fi</sup>cation of data, the bigger the aux iliary table needed. The last characteristic that needs to be considered is the size of the fact table. Although this is not as important as the <sup>fi</sup>rst two characteristics, the administrator should be aware of situations in which it is necessary to scan through a huge fact table just because it is not possible to obtain the desired value from a relatively small auxiliary table. When the fact table gets bigger, we also need to consider increasing the size of the auxiliary table.

## 3.2.2. Maintaining the auxiliary table of semi-self-maintainable functions

When the data sources change the auxiliary table itself also needs to be updated, and we thus propose an algorithm to achieve this. We <sup>fi</sup>rst compare each tuple in the set of modi<sup>fi</sup>cations with every tuple in the auxiliary table. If the value in the modi<sup>fi</sup>cation set is equal to the value in the

1 FOR each tuple in the modification set

2 FOR each tuple in the auxiliary table

3 IF the value from modification set=the value from the auxiliary table THEN

4 Update the corresponding Frq by 1

5 IF the corresponding Frq = 0 THEN

6 DELETE the corresponding tuple from the auxiliary table

7 END IF

8 END IF

Fig. 5. Algorithm to maintain semi-self-maintainable functions.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

Y.-S. Huang et al. / Decision Support Systems xxx (2013) xxx–xxx

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 FOR each tuple in the modification set
2 IF  $A_{(i)} &lt; Val_{(1)}$  THEN
3 FOR each tuple in the auxiliary table
4 IF the value from modification set = the value from the auxiliary table THEN
5 Update the corresponding Frq by 1
6 IF the corresponding Frq = 0 THEN
7 DELETE the corresponding tuple from the auxiliary table
8 END IF
9 END IF
10 END FOR
11 ELSE
12 ADD the first tuple in the auxiliary table
13 END IF
14 END FOR
</div>

Fig. 6. Improvement for MAX function.

auxiliary table, the corresponding Frq of the auxiliary tuple will be increased/decreased by one. After that, we check the value of the corresponding Frq, and if it is equal to 0 it will be deleted from the auxiliary table. The algorithm is shown in Fig. 5.

By ignoring some calculations in case the new value is smaller than the smallest value in the auxiliary table, the algorithm to maintain the auxiliary table for the MAX function can gain some improvement by putting lines 2 to 9 of the algorithm in Fig. 5 between the block IF $A _ { ( i ) } > V a l ( m )$ THEN … END IF. The algorithm is shown in Fig. 6.

The algorithm to maintain the auxiliary table for the MIN function can also be improved if we ignore the calculations when the new value is greater than the greatest value in the auxiliary table. The algorithm for this is shown in Fig. 7.

When an update of the materialized view is necessary, the auxiliary table is used for the updating process. Because of the assistance of the architecture of the auxiliary table, we can easily get the new aggregate value by assigning the value of Val of the <sup>fi</sup>rst tuple to the variable NewAggregateValue. The meaning of NewAggregateValue depends on which auxiliary table is used. If the auxiliary table for the MIN function is used, it is the new minimal value of the corresponding attribute, and if the auxiliary table for the MAX function is used, it is the new maximal value of the corresponding attribute.

## 3.3. Maintaining non-self-maintainable functions

The median of a set of n numbers is the middle value (after the values are sorted) if n is odd, or the average of the middle two numbers if n is even. Fig. 8 is a simple example that shows us how to calculate the median value from a speci<sup>fi</sup>c table.

As shown in Fig. 8, calculating the median value is very time and resource consuming because this method will scan the entire fact table and needs a large space of memory to store the temporary table. Hence, ef<sup>fi</sup>ciently maintaining the median function is a crucial job for any data warehous administrator.

## 3.3.1. Structure of auxiliary table for non-self-maintainable functions

In theory, we need to take into consideration both the amount of data that will be inserted and the amount of data that will be deleted from the fact table when we construct the auxiliary table for the median function. In reality, it is very likely that the total amount of data which is going to be inserted is always greater than the total amount of data which is going to be deleted, and the proposed approach works on this assumption

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 FOR each tuple in the modification set
2 IF  $A_{(i)} &lt; Val_{(k)}$  THEN
3 FOR each tuple in the auxiliary table
4 IF the value from modification set=the value from the auxiliary table THEN
5 Update the corresponding Frq by 1
6 IF the corresponding Frq = 0 THEN
7 DELETE the corresponding tuple from the auxiliary table
8 END IF
9 END IF
10 END FOR
11 ELSE
12 ADD the first tuple in the auxiliary table
13 END IF
14 END FOR
</div>

Fig. 7. Improvement for MIN function.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

Y.-S. Huang et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/GKBR5SA6/fulltext/images/fda99b7b9ed425b7efd64a9c0239cbfb15703d60dd9e8e319c7c0cc7040204c3.jpg)  
Fig. 8. Calculating the median value by using SQL.

Differing from the MIN and the MAX functions, we need to search in the auxiliary table to obtain the median and then store it. There is only one tuple's value in the auxiliary table that can correspond with the median of the fact table under a speci<sup>fi</sup>c dimensional condition from the auxiliary data's identi<sup>fi</sup>cation tag. According to the formulation that calculates the position of the median value, it should be at the (n + 1)/2th under the sorted tuples from the fact table. However, the tuples of a fact table cannot be sorted in practice because they could be millions or even billions, not to mention the data that would be needed to follow some dimensional conditions. Due to the fact that all the tuples of the auxiliary table have been sorted, the median value can be found at the position of the accumulated Frq being equal to or less than (n + 1)/2. Fig. 9 shows the algorithm for searching the median value by using the auxiliary tables.

There are two stages to construct an auxiliary table under different dimensional conditions. In the initial stage, we can take all the data of the fac table to construct the auxiliary table according to the SQL command as mentioned in Section 3.2.1. In the maintenance stage, the proposed algorithm can be used (see Figs. 6 & 7) which can increase ef<sup>fi</sup>ciency without having to scan all the data of the fact table. The rationale behind this will be explained in the following section.

## 3.3.2. Using an auxiliary table to maintain non-self-maintainable functions

As the cost of storing a unit of data is falling day by day, and the time available for managers to make decisions in a dynamic business environment is limited, spending more resources to get information faster is becoming increasingly popular. We can see this very clearly in this case, as by spend ing more resources to keep half of the fact table as the auxiliary table, the decision maker only has to spend half of the time to get the result compared with working without the auxiliary table.

In some cases when the fact table is very big and the amount of transactions is about equal per period of time, we have a more ef<sup>fi</sup>cient way to maintain the data warehouse. Instead of keeping the entire fact table, we can just keep a portion of that, which could be enough to maintain the view without accessing the base table for <sup>fi</sup>ve days, ten days, and so on, depending on the user's choice. Once the fact table is changed, the corresponding auxiliary tables would also be changed by using the proposed algorithms without scanning the entire fact table. The <sup>fi</sup>ve statistics characteristics (Mean, Variance, Max, Min, and Median) will be calculated also at the moment and kept for retrieving.

In case when we keep the last half of the fact table as an auxiliary table, we will add all of the new transactions to the auxiliary table after we have obtained the new median and discard the useless data. This method has one advantage over the previous one, which is that we will never need to scan the entire fact table to get a new auxiliary one. However, the size of the auxiliary table will also increase day by day as the size of the fact table increases.

## 4. Numerical application

In this section, an experiment is performed to investigate the effectiveness of the proposed approach. The hardware and software speci<sup>fi</sup> cations, as well as the data used in the experiment, are stated as follows:

\- Hardware speci<sup>fi</sup>cations

• ASUS i7 3370

• CPU: Intel® 4-Core (3.40 GHz)

• RAM: 8GB

\- Software speci<sup>fi</sup>cations

• Window Server 2008 Enterprise Edition

• Microsoft SQL Server 2008

The data used for the experiment came from the KDD Cup 1999 database, which is the data set used for “The Third International Knowledge Discovery and Data Mining Tools Competition”, held in conjunction with “KDD-99 the Fifth International Conference on Knowledge Discovery and Data Mining”. This database contains a standard set of data to be audited, and includes a wide variety of intrusions simulated in a

![](/api/attachments/GKBR5SA6/fulltext/images/6b2bf9ffd929a18bf0235334ca55e9e806364d7f724fad595a9addb9d3cd9e46.jpg)  
Fig. 9. Searching for the median value by using auxiliary table.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

military network environment (KDD [11]). Software to detect intrusions protects a computer network from unauthorized users, perhaps including insiders. The intrusion detector learning task is to build a predictive model (i.e. a classi<sup>fi</sup>er) capable of distinguishing between “bad” connections, called intrusions or attacks, and “good” normal connections.

The 1998 DARPA Intrusion Detection Evaluation Program was prepared and managed by MIT Lincoln Labs with the objective of surveying and evaluating research in intrusion detection. A standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment, was provided. The 1999 KDD intrusion detection contest uses a version of this dataset. Lincoln Labs set up an environment to acquire nine weeks of raw TCP dump data for a localarea network (LAN), simulating a typical U.S. Air Force LAN. They operated the LAN as if it were a true Air Force environment, but peppered it with multiple attacks. The raw training data was about four gigabytes of compressed binary TCP dump data from seven weeks of network traf<sup>fi</sup>c. This was processed into about <sup>fi</sup>ve million connection records. A connection is a sequence of TCP packets starting and ending at some well-de<sup>fi</sup>ned times, between which data <sup>fl</sup>ows to and from a source IP address to a target IP address under some well-de<sup>fi</sup>ned protocol. Each connection is labeled as either normal or as an attack, with exactly one speci<sup>fi</sup>c attack type. Each connection record consists of about 100 bytes.

We used 1,988,123 tuples (nearly 2 million) of the <sup>fi</sup>eld duration from Basic features of individual TCP connections in the experiment. The <sup>fi</sup>eld duration describes the length (number of seconds) of the connection. The designed MVs consist of the target attribute and the partial categorized attributes for the experiment.

Based on the hardware, software and data speci<sup>fi</sup>ed previously, we conducted an experiment to see the differences (in term of time consumption) between using and not using our proposed approach. For each function, the experiment includes two phases. In the <sup>fi</sup>rst phase, we measure the time needed to calculate a new aggregate value without using our proposed approach. In the second phase, the time needed to calculate the new aggregate value using the proposed approach is measured. The detailed procedure to conduct the experiment for each speci<sup>fi</sup>c function is stated as follows.

For MAX and MIN functions, the auxiliary tables consisting of 1000 tuples are <sup>fi</sup>rst initiated by the SQL commands shown as follows, respectively.

SELECT TOP 1000 Duration INTO auxMax FROM tblData ORDER BY Duration.

SELECT TOP 1000 Duration INTO auxMin FROM tblData ORDER BY Duration DESC.

Note that tblData is the name of the table which keeps the data for our experiment, while auxMax and auxMin are the names of the auxiliary tables for the MAX and MIN functions, respectively. The auxiliary table has the pre<sup>fi</sup>x aux.

After the auxiliary table is initiated, the following steps are conducted to measure the time needed to calculate the new aggregate value, with and without using our proposed approach:

Step 1: Delete a group of tuples by random pick from table tblData.

Step 2: Calculate the new minimum and maximum values.

Step 3: Record the time needed to calculate the new values.

Step 4: Insert a group of tuples which were produced by a random generator.

Step 5: Use our proposed approach to calculate the new aggregate value.

Step 6: Record the time need to calculate the new value.

Step 7: Repeat steps 1 to 6 thirty times.

## Table 3

The SQL commands to initiate the auxiliary table.

<table><tr><td>Function name</td><td>SQL commands to initiate the auxiliary table</td></tr><tr><td>MEAN</td><td>SELECT SUM(Duration)/COUNT(Duration) INTO auxMean FROM tblData</td></tr><tr><td>MAX</td><td>SELECT TOP 1000 Duration INTO auxMin FROM tblData ORDER BY Duration DESC</td></tr><tr><td>MIN</td><td>SELECT TOP 1000 Duration INTO auxMax FROM tblData ORDER BY Duration ASC</td></tr><tr><td>VARIANCE</td><td>SELECT VARIANCE(Duration) AS Dev INTO auxVar FROM tblData</td></tr><tr><td>MEDIAN</td><td>SELECT TOP 50 PERCENT Duration FROM tblData ORDER BY Duration DESC</td></tr></table>

These steps can be applied to all the other functions in this study, and the SQL commands to initiate the auxiliary table for these are shown in Table 3.

Table 4 presents the mean scores and the standard deviations of the experimental results. To determine whether the proposed approach has an effect, a statistical test is performed on the differences between the mean scores for each group. Since the samples are independent and the sample size is small, the t-test is used to examine the signi<sup>fi</sup>cance of the proposed approach. According to the proposed approach, we need an auxiliary table to assist us in calculating the new aggregate value, and the needed time to initiate the auxiliary table is presented in Table 4 as the initialization time.

The signi<sup>fi</sup>cance level α = 0.01 is used for our testing. The experimental results in Table 4 show that all the calculated t values (effect size between the two approaches) are greater than the critical value (t = 2.39) and all the p-values are substantially smaller than 0.01 (the signi<sup>fi</sup>cance level). The results of the statistical analysis thus show that the proposed approach has superior performance. As can be seen in Table 4, we realize that the initialization time is relatively large compared with the time spent to calculate a new aggregate value without using our proposed approach. But we do not need to initiate the auxiliary table every time, and after the initialization it does not take much time to maintain it.

In order to gain a signi<sup>fi</sup>cant improvement in maintaining a data warehouse, we have to sacri<sup>fi</sup>ce some storage space for the auxiliary table, and the question is then how much is required? For the MEAN and the VARIANCE functions the space required is just as small as the space needed to keep a number inside the database. For the MIN and the MAX functions, if up to 10,000 tuples are kept for each function, the space needed is still smaller than one MB. We need space to keep up to 50% of the total tuples for the MEDIAN function so the size of the auxiliary table for this is much bigger compared with the other auxiliary tables.

By applying the proposed approach in the data warehouse maintenance process we can obtain signi<sup>fi</sup>cant time reduction. Although we need to spend more time to initiate the auxiliary table, and use more space to keep that auxiliary table inside the data warehouse, it needs to be done only once, and then we can enjoy a very signi<sup>fi</sup>cant reduction in the time required to maintain the VARIANCE function, down from minutes to seconds.

Different from self-maintainable functions for which we can apply the proposed approach to a set of data, in order to maintain the auxiliary table for semi-self-maintainable functions we need to check every tuple in the modi<sup>fi</sup>cation set one by one. Consequently, although we see a signi<sup>fi</sup>cant reduction in time consumption (from 145.88 down to 0.46 for MAX function and from 155.99 down to 0.48 for MIN function), the data warehouse administrator still needs to consider whether it is worth applying this approach because the auxiliary table still needs time to update. If there are not too many tuples of data to be deleted/ inserted, it is good to use our approach to maintain the data warehouse. But if there are too many tuples to be updated (deleted and/or inserted), then this approach will not deliver much improvement. In order to explain why the situation will lead to inef<sup>fi</sup>ciency, we investigated the processing time for updating the auxiliary table for different numbers of tuples updated (deleted and inserted). The simulation was performed by considering different batches of modi<sup>fi</sup>cations (10,000, 20,000, 30,000,…, 300,000), and the amount of modi<sup>fi</sup>cations for each batch is proportional to the number of tuples for the whole base table (nearly 2 million) as 0.5%, 1%, 1.5%,…, 15%. The proposed approach can avoid rescanning the whole base table and reduce the calculation time. However, updating the auxiliary table will need more computation resources if the modi<sup>fi</sup>cations of the database are overly numerous and frequent. Fig. 10 shows the results of the simulation.

Table 4 Experimental results.

<table><tr><td rowspan="2">Function name</td><td rowspan="2">The initialization time</td><td rowspan="2">n</td><td colspan="2">Without the proposed approach</td><td colspan="2">Using the proposed approach</td><td rowspan="2">t-value (effect size)</td><td rowspan="2">P-value (“*” means significance)</td></tr><tr><td> $\bar{x}$ </td><td>s</td><td> $\bar{x}$ </td><td>s</td></tr><tr><td>MEAN</td><td>182</td><td>30</td><td>173.65</td><td>1.03</td><td>2.67</td><td>0.36</td><td>858.3</td><td>&lt;&lt;0.01*</td></tr><tr><td>VARIANCE</td><td>517</td><td>30</td><td>327.45</td><td>0.78</td><td>2.93</td><td>0.39</td><td>2038.2</td><td>&lt;&lt;0.01*</td></tr><tr><td>MAX</td><td>3348</td><td>30</td><td>145.88</td><td>0.71</td><td>0.46</td><td>0.21</td><td>1075.8</td><td>&lt;&lt;0.01*</td></tr><tr><td>MIN</td><td>2791</td><td>30</td><td>155.99</td><td>1.06</td><td>0.48</td><td>0.25</td><td>782.1</td><td>&lt;&lt;0.01*</td></tr><tr><td>MEDIAN</td><td>11,633</td><td>30</td><td>353.32</td><td>5.98</td><td>8.77</td><td>1.72</td><td>303.3</td><td>&lt;&lt;0.01*</td></tr></table>

As can be seen in Fig. 10, It will take 6468 s to update the auxiliary table when the number of modi<sup>fi</sup>cation tuples is over 200,000, which is about 20 times the processing time for the traditional way (SQL, approximately 300 s for each aggregate function in our experiment) to calculate the <sup>fi</sup>ve statistical functions. In other words, if the query of any statistical function is not very frequent or not necessary to have a quick response in practice, the advantage of saving computation time with the proposed approach might not be bene<sup>fi</sup>cial. The tradeoffs between the two approaches are shown in Fig. 10, and the data warehouse administrator can then make her decision whether to use the proposed approach or not by considering different situations.

Nevertheless, in most cases, we believe that the modi<sup>fi</sup>cation of a base table may not exceed 10% within a day, and the frequency of any querying statistical function should be fairly high except for some extreme cases. Therefore, our approach still can improve the ef<sup>fi</sup>ciency of database management. With regard to how to improve our approach in some extreme cases, two suggestions are provided as follows:

(1) If the number of modi<sup>fi</sup>cations is really large, the updating task to the auxiliary table should be arranged in non-peak periods.

(2) The modi<sup>fi</sup>cations can be divided into several parts when updating the auxiliary table, which can avoid the database server being too busy for some periods (for performance balance).

With regard to the level of increment which may make the proposed approach a poor choice, we give an example for explanation. Suppose that a company needs a statistical report for the auditing task every day, so the data warehouse administrator has to query each of the <sup>fi</sup>ve statistical functions at least one time daily. The traditional approach will spend 1156 s (total processing time for the <sup>fi</sup>ve statistical functions) in our experiment. However, with our approach, the total processing time of 1156 s can be spent to deal with 35,000 inserted/ deleted tuples, which includes the calculation time of the <sup>fi</sup>ve statistical functions and the time for updating the auxiliary tables. In other words, once the inserted/deleted tuples for each day are greater than 35,000, it will make our approach a poor choice in this case.

## 5. Conclusion

By utilizing some more typical auxiliary data, we can get signi<sup>fi</sup>cant improvements in maintaining the statistical functions inside a data warehouse. The proposed approach works ef<sup>fi</sup>ciently with the MEAN, VARIANCE, MIN, and MAX functions. With just thousands of auxiliary

![](/api/attachments/GKBR5SA6/fulltext/images/19556d53899e36b82d03d0acd14530321ab977b61f17ee8fcc34102f0904f168.jpg)  
Fig. 10. The results of the simulation for different numbers of tuples updated.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003

tuples, we can reduce the maintenance time from minutes to seconds. As the dynamic business environment requires managers to make a lot of rapid decisions, and as statistical functions play a very important role in the decision making process, ef<sup>fi</sup>ciently maintaining these basic statistical functions inside a data warehouse might contribute to <sup>fi</sup>rm performance.

At present, in order to maintain the auxiliary table for semi-selfmaintainable functions, the proposed approach needs to check every tuple in the modi<sup>fi</sup>cation set. This means that the proposed approach will deliver no improvement in a case where there are too many tuples to be updated from its base table. This approach was developed for a central data warehouse, but it can still be applied to maintain a distributed data warehouse. However, since the data could be stored in different servers at different places, the productivity of the proposed approach will not be as high as with central data warehouses, although if we consider a data mart as a small data warehouse, this method can still work well.

## References

[1] D. Agrawal, A.E. Abbadi, A. Singh, T. Yurek, Ef<sup>fi</sup>cient view maintenance at data warehouses. Paper presented at the ACM SIGMOD International Conference on Management of Data, Tucson, Arizona, United States, 1997.

[2] M.O. Akinde, O.G. Jensen, M.H. Bohlen, Minimizing detail data in data warehouses, Paper presented at the Sixth International Conference on Extending Database Technology, Spain, 1998.

[3] C.-M. Chao, Incremental maintenance of object-oriented data warehouses, Informa tion Sciences 160 (2004) 91–110.

[4] M. Cho, J. Pei, K. Wang, Answering ad hoc aggregate queries form data streams using pre<sup>fi</sup>x aggregate trees, Knowledge and Information Systems 12 (3) (2007) 301–329.

[5] A. Gupta, I.S. Mumick, V.S. Subrahmanian, Maintaining views incrementally, Paper presented at the ACM SIGMOD international conference on managemetn of data, Washington DC, 1993.

[6] H. Gupta, I.S. Mumick, Incremental maintenance of aggregate and outerjoin expressions Information Systems 31 (2006) 435–464

[7] J.V. Harrison, Incremental view maintenance in extended relational database, Information and Software Technology 37 (1995) 479–491.

[8] T. Imilinski, J. Witold Lipski, Imcomplete information in relational database, Jounal of the ACM 31 (4) (1984) 761–791

[9] D. Jin, T. Tsuji, T. Tsuchida, K. Higuchi, An incremental maintenance scheme of data cubes, Lecture Notes in Computer Science 4947 (2008) 172–187.

[10] A. Koeller, Incremental maintenance of schema-restructuring views in Schema SQL IEEE Transaction on Knowledge and Data Engineering 16 (2004) 1096–1111.

[11] K.D.D. Cup, http://archive.ics.uci.edu/ml/databases/kddcup99/kddcup99.html 1999.

[12] D. Laurent, J. Lechtenborger, N. Spyratos, G. Vossen, Monotonic complements for independent data warehouses, The VLDB Journal 10 (2001) 295–315.

[13] K.Y. Lee, J.H. Song, M.H. Kim, An ef<sup>fi</sup>cient method for maintaining data cubes incrementally, The Information of the Science 180 (2010) 928–948.

[14] H.-G. Li, H. Yu, D. Agrawal, A.E. Abbadi, Progressive ranking of range aggregates, Data & Knowledge Engineering 63 (2007) 4–25.

[15] W. Liang, H. Li, H. Wang, M.E. Orlowska, Making multiple views self-maintainable in a data warehouse, Data & Knowledge Engineering 30 (1999) 121–134.

[16] M.V. Mannino, Z. Walter, Ef<sup>fi</sup>ciency evaluation of data warehouse operations, Decision Support Systems 44 (2008) 883–898.

[17] M. Mohania, Y. Kambayshi, Making aggregate views self-maintainable, Data & Knowledge Engineering 32 (2000) 87–109.

[18] D. Quass, A. Gupta, I.S. Mumick, J. Widom, Making views self-maintainable for data warehousing, Paper presented at the PDIS, 1996.

[19] Z. Shi, Y. Huang, Q. He, L. Xu, S. liu, L. Qin, et al., MSMiner—a developing platform for OLAP. Decision Support Systems 42 (2007) 2016–2028.

[20] H. Shu, View maintenance using conditional tables, Paper presented at the 5th DOOD, Berlin Heidelberg New York, 1997.

[21] G.C.H. Yeung, W.A. Gruver, Multiagent immediate incremental view maintenance for data warehouses, IEEE Transactions on Systems Man and Cybernetics Part A-Systems and Humans 35 (2005) 305–310.

[22] X. Zhang, E.A. Rundensteiner, Integrating the maintenance and synchronizaiton of data warehouses using a cooperative framework, Information Systems 27 (2002) 219-243.

Yeu-Shiang Huang is currently a professor in the Department of Industrial and Information Management at National Cheng Kung University, Taiwan. He earned both his M.S. and Ph.D. degrees in Industrial Engineering from the University of Wisconsin— Madison, U.S.A. His research interests include operations management, supply chain management, reliability engineering, and decision analysis. Related papers have appeared in such professional journals as Software Testing, Verification and Reliability, Software Quality Journal, Computers and Operations Research, Computers and Industrial Engineering, Expert Systems with Applications, International Journal of Computer Mathematics, Journal of Universal Computer Science, IIE Transactions, Naval Research Logistics, IEEE Transactions on Engineering Management, Reliability Engineering and System Safety, IEEE Transactions on Reliability, Communications in Statistics, and others.

Do Duy is a graduate student in the Department of Industrial and Information Management at National Cheng Kung University, Taiwan.

Chih-Chiang Fang is currently an assistant professor in the Department of Information Management at Shu-Te University, Kaohsiung, Taiwan. He received his Ph.D. degree in the Department of Industrial and Information Management at National Cheng Kung University, Taiwan. His research interests include decision analysis, Bayesian statistical methods, and reliability engineering. Related papers have appeared in such professional journals as Naval Research Logistics, IEEE Transactions on Engineering Management, Software Testing Verification and Reliability Computers and Industrial Engineering, and others.

Please cite this article as: Y.-S. Huang, et al., Ef<sup>fi</sup>cient maintenance of basic statistical functions in data warehouses, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.003
