---
otero_id: 20881
otero_key: "7GE64ED3"
title: "An effective data clustering measure for temporal selection and projection queries"
authors: "Jong Soo Kim; Myoung Ho Kim"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00088-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An effective data clustering measure for temporal selection and projection queries

Jong Soo Kim<sup>)</sup>, Myoung Ho Kim

DiÕision of Computer Science, Department of Electrical Engineering and Computer Science, Korea AdÕanced Institute of Science and Technology KAIST , 373-1 Kusung-dong, Yousung-gu, Taejon, 305-701, South Korea ( )

Accepted 12 June 2000

## Abstract

Temporal databases TDBs allow users to record and retrieve time-varying data objects. Since TDBs usually manage aŽ . huge amount of underlying data objects, efficient disk accesses are essential for fast response time in temporal query processing. Data clustering is one of the most effective techniques that can improve performance of TDB systems. However, clustering measures for conventional data objects are not appropriate to temporal data objects because it is important to exploit temporal properties of underlying data objects and temporal queries as data clustering criteria. In this paper, we propose a data clustering measure called temporal affinity that can be used for effective temporal data clustering. The temporal affinity, which is based on the semantics of temporal operators, reflects the closeness among temporal data objects with respect to temporal query processing. We perform experiments to show the effectiveness of the proposed temporal data clustering measure. The experimental results indicate that a data clustering method based on the temporal affinity works better than other methods. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Temporal databases; Data clustering; Temporal affinity

## 1. Introduction

Contrary to conventional database systems that store the most recent snapshots of the real world, temporal database TDB systems maintain past, pre- Ž . sent and future planned data. They usually store a huge amount of data objects in order to allow users to record and query time-varying data objects. They can be applied to many application areas where temporal properties of underlying data objects are important, such as trend analysis and forecasting in decision support systems, history management in data warehouse environment, and so on.

Since query processing in TDB systems require handling of a huge amount of data objects, efficient disk accesses are essential to guarantee fast response time in temporal query processing. Data clustering is an effective method that can improve the locality of data accesses by clustering related data objects together in a single storage block. Data clustering methods can save query response time by allowing TDB systems to prefetch and<sup>r</sup>or postwrite transferred blocks of data objects 2 . Therefore, temporal <sup>w</sup> <sup>x</sup> data objects need to be placed on disks according to a well-designed temporal data clustering method.

A clustering method of a database system requires a proper clustering criterion and an effective measure for the criterion which is a basis of the decision on the selection of data objects to be clustered together. However, clustering measures for conventional database systems are not appropriate to temporal data clustering because it is crucial to exploit temporal properties of underlying data objects and temporal queries as clustering criteria. Conventional queries are represented in forms of predicates composed of conditions on attributes of data objects. On the other hand, temporal queries include time conditions, which specify temporal constraints of data objects on time attributes, as well as the conditions on conventional attributes. Time condition, which is one of the most effective filtering conditions in temporal queries, is expressed with special temporal operators. Therefore, temporal data clustering methods for temporal data objects should take these characteristics of temporal queries into consideration. Yet the proposal of an effective temporal data clustering measure is not so simple problem. Several intuitive measures may be exploited for temporal data clustering. However, straightforward measures cannot effectively cope with various query patterns, which are allowed in TDBs.

There has been much research in the past on various issues in TDBs. However, as far as we are aware of, there is no full-dressed proposal for temporal data clustering on the basis of the temporal characteristics of data objects and possible query patterns in TDBs 8 addressed physical organization<sup>w</sup> <sup>x</sup> of temporal data objects and proposed a data partitioning scheme for range queries and aggregation. However, this work only concerned a single time dimension, which is not enough to be applied to general TDB applications. Thus, it cannot handle temporal queries effectively, in which two time dimensions — valid time and transaction time — are considered 1 proposed a partitioned storage struc- <sup>w</sup> <sup>x</sup> ture for TDBs and mentioned clustering issues only under the proposed storage model briefly. Therefore, an effective temporal data clustering measure based upon the study on the relationships among temporal data objects, semantics of temporal operators, and various temporal query patterns is required.

In this paper, we propose a data clustering measure, called temporal affinity, that can be applied in temporal data clustering. The proposed temporal affinity, which is based on the semantics of temporal operators, reflects the closeness of two temporal data objects with respect to temporal query processing. The closeness of temporal data objects means the possibility that two data objects are retrieved together by a given temporal query. With the proposed measure, two data objects having high affinity are clustered together in order to reduce the number of disk pages that must be accessed on query processing. Experimental evaluations of a data clustering method based on the proposed clustering measure are also presented in this paper. Our performance study indicates that a data clustering method based on the temporal affinity works better than other methods.

The remainder of the paper is organized as follows. We describe some preliminary knowledge for our study in Section 2. The problem of straightforward temporal data clustering measures and the motivation of our work are explained in Section 3. In Section 4, we address canonical temporal queries, which is a classification of temporal query patterns, and describes a temporal data clustering criterion. We then propose temporal affinities based on temporal characteristics of temporal operators for each canonical temporal query. The integration of various temporal affinities into the single temporal affinity is also described. In Section 5, we evaluate performance of a clustering method based on the proposed temporal affinity. Finally, we conclude with a summary of our work in Section 6.

## 2. Preliminaries

## 2.1. The concepts of time in TDBs

TDBs introduce the notion of time into underlying data objects in order to manage past, present, and future planned versions of real world entities. There are two major concepts of time in TDBs: Õalid time and transaction time.<sup>1</sup> Valid time denotes the time interval during which a fact is valid in reality. Transaction time, on the other hand, represents the time interval during which a fact exists in the database. Transaction time interval means the time when the fact is logically current in the database. These two time dimensions are orthogonal and can be supported separately or together. TDBs are classified into snapshot databases, rollback databases, historical databases, and bitemporal databases Ž . 2TDBs according to the time dimensions supported. 2TDBs support both valid time and transaction time 4 . In<sup>w</sup> <sup>x</sup> this paper, TDBs denote 2TDBs and temporal queries denote bitemporal queries in 2TDBs.

Table 1  
A temporal relation Salary Record <sub>–</sub>

<table><tr><td rowspan="2">EmpID</td><td rowspan="2">Sex</td><td rowspan="2">Salary</td><td colspan="2">Valid time</td><td colspan="2">Transaction time</td></tr><tr><td>From (Vs)</td><td>To (Ve)</td><td>Start (Ts)</td><td>Stop (Te)</td></tr><tr><td>E1</td><td>F</td><td>30,000</td><td>Jan-3-97</td><td>Jun-30-97</td><td>Jan-1-97</td><td>Feb-28-97</td></tr><tr><td>E2</td><td>M</td><td>35,000</td><td>Mar-3-97</td><td>May-31-98</td><td>Jan-1-97</td><td>Mar-2-97</td></tr><tr><td>E3</td><td>M</td><td>25,000</td><td>Feb-1-97</td><td>Oct-7-97</td><td>Jan-1-97</td><td>Mar-31-97</td></tr><tr><td>E1</td><td>F</td><td>40,000</td><td>Mar-1-97</td><td>Jun-30-97</td><td>Mar-1-97</td><td>Apr-30-97</td></tr><tr><td>E2</td><td>M</td><td>35,000</td><td>May-1-97</td><td>May-31-98</td><td>Mar-3-97</td><td>Now</td></tr><tr><td>E3</td><td>M</td><td>35,000</td><td>Apr-1-97</td><td>Dec-31-97</td><td>Apr-1-97</td><td>Now</td></tr><tr><td>E1</td><td>F</td><td>45,000</td><td>May-1-97</td><td>Dec-31-97</td><td>May-1-97</td><td>Now</td></tr></table>

There have been various proposals for representing temporal data objects based on relational data model. In this study, we assume that each temporal data object is represented in the tuple time-stamped manner that is addressed in Ref. 5 . Table 1 shows an example of the tuple time-stamped representation of temporal data objects based on relational data model.

We use the terms, surrogate, temporal attributes, non-temporal attributes, and time attributes to denote attributes in a temporal relation as in Ref. 3 . A<sup>w</sup> <sup>x</sup> surrogate is an attribute that can identify an entity in the real world. A temporal attribute is an attribute that varies over time. A non-temporal attribute is an attribute that has a fixed value over time. Time attributes represent the start time and end time of valid<sup>r</sup>transaction time interval. Therefore, a data object in a TDB can be uniquely identified with its surrogate and time attributes. In Table 1, EmpID is the surrogate, Sex is a non-temporal attribute and Salary is a temporal attribute. Vs, Ve, Ts, and Te, which denote the start and end of valid time and transaction time intervals, respectively, are the time attributes of the temporal relation. In this work, we assume that the temporal domain is a sequence of discrete time instants as in Ref. 7 .<sup>w</sup> <sup>x</sup>

## 2.2. Temporal operators

In temporal queries, special built-in operators are used in order to specify temporal constraints of data objects to be retrieved. These operators allow database users to describe various temporal relationships among data objects. A classification of temporal operators has been proposed in Ref. 4 . TSQL2<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 10 , which is one of the most important query languages in TDBs, also uses a number of useful temporal operators for temporal queries. In this paper, we mainly focus on six major temporal operators shown in Table 2 that are commonly addressed in the literature 1,4,10,11 . In the table,  d is a temporal data object and d.start and d.end are the time attributes of d. That is, start can be either Ts or

Table 2  
Temporal operators

<table><tr><td>Type</td><td>Operators</td><td>Selection condition</td></tr><tr><td rowspan="2">Time-slice Operators</td><td>d as-of  $t$ </td><td>d.start  $\leq$  ti $\leq$  d.end</td></tr><tr><td>d within ( $a, b$ )</td><td>d.start  $\geq$   $a$  $\land$  d.end  $\leq$   $b$ </td></tr><tr><td rowspan="4">Temporal Comparison Operators</td><td>d precedes  $t$ </td><td>d.end &lt;  $t$ </td></tr><tr><td>d follows  $t$ </td><td>d.start &gt;  $t$ </td></tr><tr><td>d overlaps ( $a, b$ )</td><td>d.start  $\leq$   $b$  $\land$  d.end  $\geq$   $a$ </td></tr><tr><td>d contains ( $a, b$ )</td><td>d.start  $\leq$   $a$  $\land$  d.end  $\geq$   $b$ </td></tr></table>

Vs, and end can be either Te or Ve, respectively. The operand t is a time instant and Ž .a, b is a time interval.

In the table, time-slice operators can be applied to any relation with valid and<sup>r</sup>or transaction time time-stamps. They take the relation as the first argument and a time instant or an interval as the second argument. They return the argument relation reduced in the time dimension to just those times specified by the argument time instant or interval 4 . We can <sup>w</sup> <sup>x</sup> consider two kinds of time-slice operators according to the second argument: as-of and within.<sup>2</sup> The second argument of as-of operator is a time instant, and that of within operator is a time interval.

The temporal comparison operators are used in order to compose various temporal comparison predicates. They are usually specified in the queries for the purpose of inquiring the history of entities in the real world or in the database. They can be used for transaction time and<sup>r</sup>or valid time of temporal data objects.

## 3. Motivation

3.1. Measures for the clustering of temporal data objects

As we mentioned before, TDBs store a large number of data objects in order to maintain temporal properties of real world entities. In general, these data objects are stored and managed on disks. Therefore, the efficient retrieval of data objects selected by a temporal query is important for fast response time. Data clustering can improve query response time by clustering related data objects in a single disk block and hence reducing the number of disk accesses on query processing 2 .<sup>w</sup> <sup>x</sup>

For the purpose of efficient data clustering in TDBs, we need an appropriate measure based on specific relationships among data objects and temporal queries, and should cluster data objects on the basis of that measure as in conventional databases. For example, consider a database system that maintains the sales records of car dealers. If the records are clustered by using the zip-codes of the dealers<sup>3</sup>, the clustering effect can be utilized for location-based queries such as ‘Retrieve the sales record of the dealers in Chicago, IL’. For the same reason, it is essential for a TDB system to develop a proper temporal data clustering measure in order to improve the effectiveness of the clustering. We assume that 2TDBs on which we are focusing in this paper have the append-only property. That is, a new object is inserted on update instead of modifying an existing data object. Also a data object is not physically removed from the database even if it is logically deleted. Because of the append-only property, TDB systems maintain numerous versions of the same real world entities as time goes by. Therefore, temporal characteristics of underlying data objects must be carefully considered on temporal data clustering.

## 3.2. The problem

To propose an effective measure for temporal data clustering based upon the temporal characteristics of data objects is not so a simple problem. Several intuitive measures, such as the similarity in valid<sup>r</sup> transaction time and the degree of overlapping in valid<sup>r</sup>transaction time intervals, may be exploited. However, these straightforward measures cannot cope with various query patterns allowed in TDBs efficiently. Let us look into the problem in the following example.

Example 1. Suppose that data objects are clustered by using the degree of overlapping in their valid time intervals. That is, the longer is the length of the overlapped valid time interval of two data objects, the larger is the possibility that two objects are clustered together on the same disk block. Fig. 1 shows the valid time intervals of three data objects d1, d2, and d3 on the time line. In the figure, d1 is likely to be clustered together with d2 because the length of the overlapped interval of d1 and d2 is longer than that of d1 and d3. This sort of clustering strategy may be advantageous for some temporal queries in which the valid time-slice operator is specified.

![](/api/attachments/7GE64ED3/fulltext/images/5c7891bf7267d1f91db7ec97024c31b98c447bbe5d296a36660cde17c118bda2.jpg)  
Fig. 1. Temporal data objects and their overlapped valid time intervals.

For example, consider the query, ‘Retrieve all the records whose valid start time follows the time $T '$ The possible ranges of T that retrieves d1 and one of the other two objects — d2 and d3 together are shown in Fig. 2. As shown in the figure, the possibility that d1 and d3 are retrieved together is larger than the possibility for d1 and d2.

The problem in Example 1 stems from the inappropriate clustering measure for some temporal queries. We, however, will have analogous problems even if we adopt other simple clustering criteria such as the degree of overlapping in transaction time intervals and the similarity in valid<sup>r</sup>transaction time. Accordingly, various query patterns in applications as well as various temporal characteristics of data objects should be taken into account for a clustering measure.

## 4. Temporal affinity of temporal data objects

In this section, we classify typical temporal query patterns and define a temporal data clustering criterion, i.e. the closeness of two temporal data objects with respect to temporal query processing. We will develop the temporal affinity, which reflects the closeness of temporal data objects for each classified temporal query pattern in the Section 5.

## 4.1. A classification of temporal query patterns

In order to develop a data clustering measure for efficient temporal query processing, the selection of typical query patterns is required because the effectiveness of a clustering method is closely related with the query patterns of the application. In this work, we focus on the typical basic query patterns addressed in 1,4,9–11 and call them as<sup>w</sup> <sup>x</sup> canonical temporal queries. The canonical temporal queries contain the following types of temporal queries:

## 4.1.1. Time-slice queries

This type of queries produce the argument relation reduced in the proper time dimension to the times specified in the query. The result of a time-slice query is either a snapshot relation or a temporal relation according to the dimension s of the time Ž . argument of the query. The time-slice operators are used in order to describe this type of queries. The time-slice queries can be further classified into valid time-slice queries and transaction time-slice queries by the time dimension reduced.

## 4.1.2. Temporal selection queries

Temporal selection queries are the queries whose selection predicate involves the times associated with data objects in the database. We concentrate on the selection queries with the temporal comparison operators mentioned before. This type of queries can also be further classified according to the time dimensions used in the temporal query.

A taxonomy of typical temporal query patterns is shown in Fig. 3.

To help to understand the meaning of the canonical temporal queries more clearly, let us consider some examples. Table 1 is a temporal relation that represents the time-varying salaries of employees — it also manages contracts of employment of the employees. Consider the query, ARetrieve salary records of all employees as of transaction time Oct. 1, 1997B. This is an example of the transaction time-slice query, and it returns a valid time relation — a relation only with valid time dimension — that was regarded as the current fact on the specified time. The query, ARetrieve all the versions of the employee E1’s salary record whose valid end times precede July 1, 1997B is an example of the temporal selection query with the temporal comparison operator, precedes, on valid time dimension.

![](/api/attachments/7GE64ED3/fulltext/images/855b209b65a629a890a6249e78ab0ae3bfa507e404324599abdd1c397e7d15b0.jpg)  
Fig. 2. The possible range of the query argument to retrieve d1 and one of d2 and d3 together.

![](/api/attachments/7GE64ED3/fulltext/images/13a6ecfe5a78c6e38137ca10ce8ad6da081a788489e7f89caa955084d73189ab.jpg)  
Fig. 3. A taxonomy of typical temporal query patterns.

## 4.2. A temporal data clustering criterion

As we mentioned before, the closeness of temporal data objects means the possibility that two temporal data objects are retrieved together by a given temporal query. Here, the closeness of two temporal data objects is defined formally as follows.

Definition 1. Let d1 and d2 be two temporal data objects and q be a temporal query. Then the closeness of d1 and d2 for q, denoted by CŽ . d1,d2,q , is defined as the probability that if one of d1 and d2 is retrieved by q, then the other is also retrieved by q.

From the above definition, it is clear that clustering of d1 and d2 with a large CŽ . d1,d2,q value is advantageous for efficient processing of the query q since two objects can be retrieved together with a single disk page access. Thus, we have the following proposition, which is the fundamental criterion for an effective temporal data clustering measure.

Proposition 1. Let d1 and d2 be two temporal data objects and q be a temporal query. Then any measure for temporal data clustering must haÕe the characteristic such that the Õalue of the measure is proportional to C d1,d2,q . ( )

However, it is not easy to calculate the closeness of temporal data objects directly because there can be many different types of temporal queries. Therefore, we mainly focus on the canonical temporal queries, and develop a measure that reflects the closeness of temporal data objects for each canonical temporal query pattern. In what follows, we first develop temporal affinities for the temporal operators of each canonical temporal query. The integration of those temporal affinities into one integrated temporal affinity is then described.

## 4.3. Temporal affinity for canonical temporal queries

We use the following abbreviations for convenience if there is no ambiguity: for two temporal data objects d1 and d2, MAX Ts denotes<sub>–</sub> max d1.Ts,d2.Ts . Similarly, MIN Te, MAX Vs,Ž . <sub>– –</sub> and MIN Ve denote min d1.Te,d2.Te , max-Ž . <sub>–</sub> Ž . Ž . d1.Vs,d2.Vs , and min d1.Ve,d2.Ve , respectively. On deriving temporal affinities for each temporal operator, we assume that the time dimension is transaction time. Since temporal affinities for valid time dimension can be easily derived in similar ways as in the temporal affinities for transaction time, only the results will be presented later.

## 4.3.1. Transaction time-slice queries with as-of operator

In order to be retrieved by a transaction time-slice query with as-of operator, a temporal data object must have a transaction time interval that contains the time point given in the query. Fig. 4 shows time relationships of three temporal data objects d1, d2, and d3, where t1 and t2 denote the time arguments of two transaction time-slice queries, respectively.

![](/api/attachments/7GE64ED3/fulltext/images/acdcd520d72bc75fe5a3a416aca36b4e8f98e2d3999a71f637393b09ae5a727d.jpg)  
Fig. 4. Selection of temporal data objects by queries with as-of operator.

As illustrated in the figure, in order that both d1 and d2 are selected by a transaction time-slice query with as-of operator, the argument t1 of a query must be in d1.Ts, d2.Te . For d1 and d3, the argument t2<sup>w</sup> <sup>x</sup> must be in d3.Ts, d1.Te . From this observation, we<sup>w</sup> <sup>x</sup> can notice that, in a temporal query with as-of operator, the closeness of two temporal data objects is closely related with the length of the overlapped transaction time interval of the objects. Therefore, temporal affinity for this type of queries is defined as follows. The subscript ‘TTS: as-of’ denotes ‘Transaction Time-Slice query with as-of operator’.

$$
\begin{array}{l} A _ {\mathrm{TTS:as-of}} (\mathrm{d} 1, \mathrm{d} 2) \\ = \left\{ \begin{array}{l l} \frac {(\mathrm{d} 1 . \mathrm{Te} - \mathrm{d} 1 . \mathrm{Ts}) + (\mathrm{d} 2 . \mathrm{Te} - \mathrm{d} 2 . \mathrm{Ts}) - (\mathrm{MAX} _ {-} \mathrm{Te} - \mathrm{MIN} _ {-} \mathrm{Ts})}{\mathrm{MAX} _ {-} \mathrm{Te} - \mathrm{MIN} _ {-} \mathrm{Ts}} & \text {if d1.Te\geq d2.Ts\wedge d2.Te\geq d1.Ts} \\ 0 & \text {otherwise} \end{array} \right. \end{array}\tag{1}
$$

As shown in Fig. 5a, $A _ { \mathrm { T T S : a s - o f } } ( \mathrm { d } 1 , \mathrm { d } 2 )$ is the ratio of the length L1 of the overlapped transaction time interval for two data objects to the length L2 of the possible range of the time argument that makes at least one of two data objects be retrieved. It is easy to see that $A _ { \mathrm { T T S : a s - o f } } ( \mathrm { d } 1 , \mathrm { d } 2 )$ is within 0, 1 . As<sup>w</sup> <sup>x</sup> shown in Fig. 5b, it becomes 1 if the transaction time intervals of two objects are exactly the same, and it becomes zero if the overlapped transaction time interval is zero.

The following theorem shows the validity of $A _ { \mathrm { T T S : a s - o f } }$ as a clustering measure for transaction time-slice queries with as-of operator.

Theorem 1. $A _ { T T S : a s - o f } ( d l , d 2 )$ is proportional to C d1,d2, q for a transaction time-slice query with ( ) as-of operator, $q _ { t }$

Proof. Suppose d1, d2, and d3 are temporal data objects such that $A _ { \mathrm { T T S : a s - o f } } ( { \mathrm { d } } 1 , { \mathrm { d } } 2 ) = \alpha$

![](/api/attachments/7GE64ED3/fulltext/images/490fa18f4da5681c19c2b3db14b695aeb4891209408b0f2422e28eb339bb5a01.jpg)  
Fig. 5. Calculation of the temporal affinity for a transaction time-slice query with as-of operator.

$A _ { \mathrm { T T S : a s - o f } } ( \mathrm { d } 1 , \mathrm { d } 3 ) = \beta$ , and $\alpha > \beta .$ . It is sufficient to show that the probability of selecting d1 and d2 together denoted by Ž $p _ { 1 } )$ is greater than the probability of selecting d1and d3 denoted by Ž $_ { p _ { 2 } ) }$ for any transaction time-slice query with as-of operator when at least one of two data objects is selected by the query. Let t be an argument of a transaction timeslice query, and Length d1,d2 be the length of theŽ . overlapped transaction time interval of d1 and d2, that is, $\mathrm { L e n g t h { ( d 1 , d 2 ) } } = A _ { \mathrm { T T S : a s - o f } } ( \mathrm { d 1 , d 2 ) ( m a x }$ Ž . Ž .. d1.Te,d2.Te <sup>y</sup> min d1.Ts,d2.Ts . Then,

$p _ { 1 } =$ The conditional probability that both d1 and d2

are selected when at least one of them is selected

by the query

$$
= \frac {\text { Length(d1,d2) }}{\max (\mathrm{d1.Te,d2.Te}) - \min (\mathrm{d1.Ts,d2.Ts})}
$$

$$
= \frac {\alpha (\max (\mathrm{d} 1 . \mathrm{Te} , \mathrm{d} 2 . \mathrm{Te}) - \min (\mathrm{d} 1 . \mathrm{Ts} , \mathrm{d} 2 . \mathrm{Ts}))}{\max (\mathrm{d} 1 . \mathrm{Te} , \mathrm{d} 2 . \mathrm{Te}) - \min (\mathrm{d} 1 . \mathrm{Ts} , \mathrm{d} 2 . \mathrm{Ts})} = \alpha
$$

![](/api/attachments/7GE64ED3/fulltext/images/48921b555b18d103a98da81fa47acea8d2177bf7bfecbea45f94b1e688222b85.jpg)  
Fig. 6. Selection of temporal data objects by queries with within operator.

In the same manner, ${ p } _ { 2 } = \beta$ . Since we assumed that $\alpha > \beta$ , it is clear that $p _ { 1 } > p _ { 2 }$

4.3.2. Transaction time-slice queries with within operator

Time-slice queries with within operator retrieve temporal data objects whose transaction time intervals overlap the given argument interval. These types of queries reduce the entire transaction time range into the specified interval, and select data objects that belong to the reduced time range. A temporal data object must have a transaction time interval that overlaps the given argument interval $[ t _ { \mathrm { s } } , \ t _ { \mathrm { e } } ]$ in order to be selected by the query. Therefore, two temporal data objects are selected together by the query only if both of their transaction time intervals overlap the given argument interval.

The measure for this type of queries is closely related with the relative position of the transaction time intervals of two data objects. So, we divide the problem into two sub problems — i the transactionŽ . time intervals of two data objects overlap with each other and ii the intervals are disjoint- and deriveŽ . temporal affinities in each case. First, let us assume that the transaction time intervals of two data objects are disjoint. Fig. 6 illustrates time relationships of temporal data objects d1, d2, and d3, where s1,e1Ž . and s2,e2 denote the argument intervals of two Ž . transaction time-slice queries with within operator, respectively.

As in the figure, we can determine the possible range of the arguments s and e for d1 and one of the other objects in order that two objects are selected together by the query, where s and e are the start<sup>r</sup>end points of the argument intervals. That is, s must be in <sup>w x</sup> <sup>w</sup>0, d2.Te , and e must be in d1.Ts, $T _ { \mathrm { n o w } } ]$ for d1 and d2. $T _ { \mathrm { n o w } }$ denotes the current time of the database. Therefore, the temporal affinity for transaction timeslice queries with within operator — where transaction time intervals of two data objects are disjoint — is defined as follows

$$
\begin{array}{r l} & A _ {\mathrm{TTS:within}} ^ {1} (\mathrm{d} 1, \mathrm{d} 2) \\ & = \frac {2 \mathrm{MIN} _ {-} \mathrm{Te} (T _ {\mathrm{now}} - \mathrm{MAX} _ {-} \mathrm{Ts})}{\mathrm{MAX} _ {-} \mathrm{Te} (2 T _ {\mathrm{now}} - \mathrm{MAX} _ {-} \mathrm{Te}) - (\mathrm{MIN} _ {-} \mathrm{Ts} ^ {2} + (\mathrm{MAX} _ {-} \mathrm{Ts} - \mathrm{MIN} _ {-} \mathrm{Te}) ^ {2})} \end{array}\tag{2}
$$

The following theorem shows the validity of $A _ { \mathrm { T T S : w i t h i n } } ^ { 1 } ( \mathrm { d } 1 , \mathrm { d } 2 )$ as a clustering measure for transaction time-slice queries with within operator where the transaction time intervals of d1 and d2 are disjoint.

Theorem 2. $A _ { T T S : w i t h i n } ^ { l } ( d l , d 2 )$ is proportional to C d1,d2, q for a transaction time-slice query with ( ) within operator, $q _ { t }$ , where the transaction time inter-Õals of d1 and d2 are disjoint

Proof. Suppose d1, d2, and d3 are temporal data objects such that $A _ { \mathrm { T T S : w i t h i n } } ^ { 1 } ( \mathrm { d } 1 , \mathrm { d } 2 ) = \alpha$

$A _ { \mathrm { T T S : w i t h i n } } ^ { 1 } ( \mathrm { d } 1 , \mathrm { d } 3 ) = \beta$ , and $\alpha > \beta$ . It is sufficient to show that the probability of selecting d1 and d2 together denoted byŽ $p _ { 1 } )$ is greater than the probability of selecting d1 and d3 denoted byŽ $_ { p _ { 2 } ) }$ for any transaction time-slice query with within operator when at least one of two data objects is selected by the query. Assume that the current time of the database is $T _ { \mathrm { n o w } }$ . Then the maximum value of a possible transaction time is $T _ { \mathrm { n o w } }$ . Let $[ t _ { \mathrm { s } } , \ t _ { \mathrm { e } } ]$ be an argument interval of the query. Then as shown in

![](/api/attachments/7GE64ED3/fulltext/images/506b792ea6aeb1379c5b76680a18b61ac469079c1cbfdb6aa930e2d60653cc59.jpg)  
Fig. 7. Condition of an argument interval of a transaction time-slice query with within operator in order to select both of two temporal data objects.

Fig. 7, $t _ { \mathrm { s } }$ and $t _ { \mathrm { e } }$ must satisfy the following condition if both d1 and d2 are selected together

$$
\left(0 \leq t _ {\mathrm{s}} \leq \min (\mathrm{d} 1. \mathrm{Te}, \mathrm{d} 2. \mathrm{Te})\right)
$$

$$
\wedge \left(\max (\mathrm{d} 1. \mathrm{Ts}, \mathrm{d} 2. \mathrm{Ts}) \leq t _ {\mathrm{e}} \leq T _ {\text { now }}\right)
$$

Therefore, as in Fig. 8, $p _ { 1 }$ can be calculated as follows

$p _ { 1 } =$ The conditional probability that both d1 and d2 are selected when at least one of them is selected

$$
\begin{array}{l} = \frac {\text {the probability that both d1 and d2 are selected together}}{1 - \text {the probability that neither d1 nor d2 is selected}} \\ = \frac {\text {possible range of} [ t _ {\mathrm{s}}, t _ {\mathrm{e}} ] \text {to select both d1 and d2 together}}{\text {total range - possible range of} [ t _ {\mathrm{s}}, t _ {\mathrm{e}} ] \text {to select neither d1 nor d2}} \\ = \frac {\text {the area of} Q}{\text {total range - the area of(T1 + T2 + T3)}} \\ = \frac {\min (\mathrm{d1.Te,d2.Te}) (T _ {\mathrm{now}} - \max (\mathrm{d1.Ts,d2.Ts}))}{T _ {\mathrm{now}} ^ {2} / 2 - (\mathrm{MIN-Ts} ^ {2} / 2 + (\mathrm{MAX-Ts-MIN-Te}) ^ {2} / 2 + (T _ {\mathrm{now}} - \mathrm{MAX-Te}) ^ {2} / 2} \\ = \frac {2 \min (\mathrm{d1.Te,d2.Te}) (T _ {\mathrm{now}} - \max (\mathrm{d1.Ts,d2.Ts}))}{T _ {\mathrm{now}} ^ {2} - (\mathrm{MIN-Ts} ^ {2} + (\mathrm{MAX-Ts-MIN-Te}) ^ {2} + (T _ {\mathrm{now}} - \mathrm{MAX-Te}) ^ {2})} = \alpha \end{array}
$$

In the same manner, $\begin{array} { r } { p _ { 2 } = \beta . } \end{array}$ . Since we assumed that $\alpha > \beta$ , it is clear that $p _ { 1 } > p _ { 2 }$

![](/api/attachments/7GE64ED3/fulltext/images/db32a409af80dffb54ed0889158810e89227ea036cf80338f46abff814843594.jpg)  
Fig. 8. Possible range of the argument interval of a transaction time-slice query with within operator.

Similarly, we can derive a temporal affinity for a query with within operator where the transaction time intervals of two objects overlap as follows

$$
\begin{array}{r l} & A _ {\mathrm{TTS:within}} ^ {2} (\mathrm{d} 1, \mathrm{d} 2) \\ & = \frac {\mathrm{MIN} _ {-} \mathrm{Te} (2 T _ {\mathrm{now}} - \mathrm{MIN} _ {-} \mathrm{Te}) - \mathrm{MAX} _ {-} \mathrm{Ts} ^ {2}}{\mathrm{MAX} _ {-} \mathrm{Te} (2 T _ {\mathrm{now}} - \mathrm{MAX} _ {-} \mathrm{Te}) - \mathrm{MIN} _ {-} \mathrm{Ts} ^ {2}} \end{array}\tag{3}
$$

The validity of $A _ { \mathrm { T T S : w i t h i n } } ^ { 2 } ( \mathrm { d } 1 , \mathrm { d } 2 )$ can be shown in the same manner as in Theorem 2 without much effort by using Fig. 9. Therefore, from the Eqs. 3Ž . and 4 , the temporal affinity for a transaction time-Ž .

![](/api/attachments/7GE64ED3/fulltext/images/b6f5a1136c941e834c16474cf5c6c8fe1ad8e72d7f6378eeccdcba9a7540e848.jpg)

![](/api/attachments/7GE64ED3/fulltext/images/e5631e050b46b6ee9f28ba6cadb472217db5839bf511ab8448830247c615c732.jpg)

![](/api/attachments/7GE64ED3/fulltext/images/b0599dd130a05fa459789caaba42012575b801e5bdcb62f3fa8bb331eb893ec4.jpg)  
Fig. 9. Possible range of the argument interval in the case of overlapping transaction time intervals.

slice query with within operator, $A _ { \mathrm { T T S : w i t h i n } } ( \mathrm { d } 1 , \mathrm { d } 2 )$ is defined as follows

$$
\begin{array}{r l} & A _ {\mathrm{TTS:within}} (\mathrm{d} 1, \mathrm{d} 2) \\ & = \left\{ \begin{array}{l l} A _ {\mathrm{TTS:within}} ^ {1} (\mathrm{d} 1, \mathrm{d} 2) & \text { if   d } 1. \mathrm{Te} <   \mathrm{d} 2. \mathrm{Ts} \vee \mathrm{d} 2. \mathrm{Te} <   \mathrm{d} 1. \mathrm{Ts} \\ A _ {\mathrm{TTS:within}} ^ {2} (\mathrm{d} 1, \mathrm{d} 2) & \text { otherwise } \end{array} \right. \end{array}\tag{4}
$$

It is easy to see that $A _ { \mathrm { T T S : w i t h i n } } ( \mathrm { d } 1 , \mathrm { d } 2 )$ Ž . is in 0, 1 . As shown in Fig. 10, it becomes 1 if the transaction time intervals of two objects are exactly the same, and it becomes zero if d2.Te<sup>f</sup>0 and d1 $. \mathrm { T s } \approx T _ { \mathrm { n o w } } .$

4.3.3. Transaction time selection queries with precedes operator

From now on, we will describe only the main ideas of temporal affinities for each temporal selection query. The validity of each temporal affinity can also be shown in the similar way as in Theorem 1 and Theorem 2.

![](/api/attachments/7GE64ED3/fulltext/images/b03055e9d8301e020900cd4c45ef5e6a46c67261a4244a18b143231e9b0a4505.jpg)  
Fig. 10. Consistency between $A _ { \mathrm { T T S : w i t h i n } } ( \mathrm { d } 1 , \mathrm { d } 2 )$ and our intuition on the extreme cases.

This type of temporal selection query retrieves temporal data objects whose transaction time intervals precede a specific time point. Hence, two temporal data objects are selected together by a query with precedes operator only if both of their valid time intervals precede the argument t of the query. Fig. 11 shows the relationships of temporal data objects and a transaction time selection query with precedes operator.

As in the figure, the argument t of the query must be in L2 if at least one of d1 and d2 can be selected. Also t must be in L1 if both of two data objects are selected by the query. Thus, the temporal affinity for transaction time selection queries with precedes operator is defined as follows

$$
A _ {\text { TTSEL:precedes }} (\mathrm{d} 1, \mathrm{d} 2) = \frac {T _ {\text { now }} - \text { MAX\_Te }}{T _ {\text { now }} - \text { MIN\_Te }}\tag{5}
$$

In the above equation, the subscript ‘TTSEL:precedes’ denotes ‘Transaction Time SELection query with precedes operator’. Fig. 12 illustrates that $A _ { \mathrm { T T S E L : p r e c e d e s } }$ is in 0, 1 .Ž .

![](/api/attachments/7GE64ED3/fulltext/images/ffe650e42b3480a648c055dfe94a86d8934a6aaf4cc5db1770b946a3b58f944c.jpg)  
Fig. 11. Selection of temporal data objects by a query with precedes operator.

![](/api/attachments/7GE64ED3/fulltext/images/37f294470b0f39ce0c9babec99a827fb7e07f03a9baee8665ba924247f433476.jpg)  
Fig. 12. Consistency between $A _ { \mathrm { T T S E L : p r e c e d e s } } ( { \mathrm { d } } 1 , { \mathrm { d } } 2 )$ and our intuition on the extreme cases.

4.3.4. Transaction time selection queries with follows operator

In this case, temporal data objects whose valid<sup>r</sup> transaction time intervals follow a specific time point are selected. Since this is the symmetric case of precedes operator, the temporal affinity can be derived easily as follows

$$
A _ {\mathrm{TTSEL:follows}} (\mathrm{d} 1, \mathrm{d} 2) = \frac {\mathrm {MIN\_Ts}}{\mathrm {MAX\_Ts}}\tag{6}
$$

4.3.5. Transaction time selection queries with contains operator

Temporal selection queries with contains operators retrieve temporal data objects whose transaction time interval contains the given argument interval. This condition is almost the same as that of the time-slice queries with $a s \ – o f$ operator except that the subject of inclusion is not a time instant but a time interval. Therefore, $A _ { \mathrm { T T S : a s - o f } }$ can also be applied to this type of queries. Hence, the temporal affinities $A _ { \mathrm { T T S E L : c o n t a i n s } } ( \mathrm { d } 1 , \mathrm { d } 2 )$ is defined as follows

$$
\begin{array}{l} A _ {\text {TTSEL:contains}} (\mathrm{d} 1, \mathrm{d} 2) \\ = \left\{ \begin{array}{l l} \frac {(\mathrm{d} 1 . \mathrm{Te} - \mathrm{d} 1 . \mathrm{Ts}) + (\mathrm{d} 2 . \mathrm{Te} - \mathrm{d} 2 . \mathrm{Ts}) - (\mathrm{MAX} _ {-} \mathrm{Te} - \mathrm{MIN} _ {-} \mathrm{Ts})}{\mathrm{MAX} _ {-} \mathrm{Te} - \mathrm{MIN} _ {-} \mathrm{Ts}} & \text {if d1.Te\geq d2.Ts\wedge d2.Te\geq d1.Ts} \\ 0 & \text {otherwise} \end{array} \right. \end{array}\tag{7}
$$

4.3.6. Transaction time selection queries with oÕerlaps operator

This type of queries retrieve temporal data objects whose transaction time interval overlaps the given argument time interval. The semantics of oÕerlaps operator is equal to that of within operator except for the fact that the time dimension of the resulting temporal relation is not reduced. Hence, $A _ { \mathrm { T T S : w i t h i n } }$ can be applied to this type of queries, and the temporal affinities for transaction time selection queries with oÕerlaps operator are defined as follows:

$$
\begin{array}{l} A _ {\text {TTSEL:overlaps}} (\mathrm{d} 1, \mathrm{d} 2) \\ = \left\{ \begin{array}{l l} \frac {2 \operatorname{MIN} _ {-} \operatorname{Te} \left(T _ {\text {now}} - \operatorname{MAX} _ {-} \operatorname{Ts}\right)}{\operatorname{MAX} _ {-} \operatorname{Te} \left(2 T _ {\text {now}} - \operatorname{MAX} _ {-} \operatorname{Te}\right) - \left(\operatorname{MIN} _ {-} \operatorname{Ts} ^ {2} + \left(\operatorname{MAX} _ {-} \operatorname{Ts} - \operatorname{MIN} _ {-} \operatorname{Te}\right) ^ {2}\right)} & \text {if d1.Te <   d2.Ts ∨ d2.Te <   d1.Ts} \\ \frac {\operatorname{MIN} _ {-} \operatorname{Te} \left(2 T _ {\text {now}} - \operatorname{MIN} _ {-} \operatorname{Te}\right) - \operatorname{MAX} _ {-} \operatorname{Ts} ^ {2}}{\operatorname{MAX} _ {-} \operatorname{Te} \left(2 T _ {\text {now}} - \operatorname{MAX} _ {-} \operatorname{Te}\right) - \operatorname{MIN} _ {-} \operatorname{Ts} ^ {2}} & \text {otherwise} \end{array} \right. \end{array}\tag{8}
$$

## 4.3.7. Temporal affinities for Õalid time dimension

The temporal affinities for valid time dimension are almost the same as that of transaction time except that the time dimension is valid time and the maximum permitted time value is not $T _ { \mathrm { n o w } }$ but $T _ { \mathrm { m a x } }$ The following equations are the temporal affinities for valid time

$$
A _ {\mathrm{VTS:as-of}} (\mathrm{d} 1, \mathrm{d} 2) = \left\{ \begin{array}{l l} \frac {(\mathrm{d} 1 . \mathrm{Ve} - \mathrm{d} 1 . \mathrm{Vs}) + (\mathrm{d} 2 . \mathrm{Ve} - \mathrm{d} 2 . \mathrm{Vs}) - (\text {MAX\_Ve} - \text {MIN\_Vs})}{\text {MAX\_Ve} - \text {MIN\_Vs}} & \text {if d1.Ve\geq d2.Vs\wedge d2.Ve\geq d1.Vs} \\ 0 & \text {otherwise} \end{array} \right.\tag{9}
$$

$$
A _ {\mathrm{VTS:within}} (\mathrm{d} 1, \mathrm{d} 2) = \left\{ \begin{array}{l l} \frac {2 \text {MIN} _ {-} \mathrm{Ve} (T _ {\max} - \text {MAX} _ {-} \mathrm{Vs})}{\text {MAX} _ {-} \mathrm{Ve} (2 T _ {\max} - \text {MAX} _ {-} \mathrm{Ve}) - (\text {MIN} _ {-} \mathrm{Vs} ^ {2} + (\text {MAX} _ {-} \mathrm{Vs} - \text {MIN} _ {-} \mathrm{Ve}) ^ {2})} & i f \mathrm{d} 1. \mathrm{Ve} <   \mathrm{d} 2. \mathrm{Vs} \vee \mathrm{d} 2. \mathrm{Ve} <   \mathrm{d} 1. \mathrm{Vs} \\ \frac {\text {MIN} _ {-} \mathrm{Ve} (2 T _ {\max} - \text {MIN} _ {-} \mathrm{Ve}) - \text {MAX} _ {-} \mathrm{Vs} ^ {2}}{\text {MAX} _ {-} \mathrm{Ve} (2 T _ {\max} - \text {MAX} _ {-} \mathrm{Ve}) - \text {MIN} _ {-} \mathrm{Vs} ^ {2}} & o t h e r w i s e \end{array} \right.\tag{10}
$$

$$
A _ {\mathrm{VTSEL:precedes}} (\mathrm{d} 1, \mathrm{d} 2) = \frac {T _ {\max} - \text { MAX\_Ve }}{T _ {\max} - \text { MIN\_Ve }}\tag{11}
$$

$$
A _ {\mathrm{VTSEL:follows}} (\mathrm{d} 1, \mathrm{d} 2) = \frac {\mathrm {MIN\_Vs}}{\mathrm {MAX\_Vs}}\tag{12}
$$

$$
\begin{array}{l} A _ {\mathrm{VTSEL:contains}} (\mathrm{d} 1, \mathrm{d} 2) \\ = \left\{ \begin{array}{l l} \frac {(\mathrm{d} 1 . \mathrm{Ve} - \mathrm{d} 1 . \mathrm{Vs}) + (\mathrm{d} 2 . \mathrm{Ve} - \mathrm{d} 2 . \mathrm{Vs}) - (\mathrm{MAX} _ {-} \mathrm{Ve} - \mathrm{MIN} _ {-} \mathrm{Vs})}{\mathrm{MAX} _ {-} \mathrm{Ve} - \mathrm{MIN} _ {-} \mathrm{Vs}} & \text { if   d } 1. \mathrm{Ve} \geq \mathrm{d} 2. \mathrm{Vs} \wedge \mathrm{d} 2. \mathrm{Ve} \geq \mathrm{d} 1. \mathrm{Vs} \\ 0 & \text { otherwise } \end{array} \right. \end{array}\tag{13}
$$

A<sub>VTSEL:overlaps</sub>Ž . d1,d2

$$
= \left\{ \begin{array}{l l} \frac {2 \text {MIN} _ {-} \mathrm{Ve} \left(T _ {\max} - \text {MAX} _ {-} \mathrm{Vs}\right)}{\text {MAX} _ {-} \mathrm{Ve} \left(2 T _ {\max} - \text {MAX} _ {-} \mathrm{Ve}\right) - \left(\text {MIN} _ {-} \mathrm{Vs} ^ {2} + \left(\text {MAX} _ {-} \mathrm{Vs} - \text {MIN} _ {-} \mathrm{Ve}\right) ^ {2}\right)} & \text {if d1.Ve <   d2.Vs v d2.Ve <   d1.Vs} \\ \frac {\text {MIN} _ {-} \mathrm{Ve} \left(2 T _ {\max} - \text {MIN} _ {-} \mathrm{Ve}\right) - \text {MAX} _ {-} \mathrm{Vs} ^ {2}}{\text {MAX} _ {-} \mathrm{Ve} \left(2 T _ {\max} - \text {MAX} _ {-} \mathrm{Ve}\right) - \text {MIN} _ {-} \mathrm{Vs} ^ {2}} & \text {otherwise} \end{array} \right.\tag{14}
$$

4.4. Integration of the temporal affinities for the canonical temporal queries

Until now, we have developed temporal affinities for each canonical temporal query pattern. However, in order to apply these affinities to temporal data clustering, they need to be integrated. We construct a single temporal affinity, that is, an integrated temporal affinity as a weighted sum of the temporal affinities for the canonical temporal queries. Thus, the integrated temporal affinity, AŽ . d1,d2 , is defined as follows

$$
A (\mathrm{d} 1, \mathrm{d} 2) = \sum_ {i \in \mathrm{CTQ}} \omega_ {i} A _ {i} (\mathrm{d} 1, \mathrm{d} 2)\tag{15}
$$

where CTQ<sup>s</sup>TTS:as-of, VTS:as-of, TTS:within, VTS:within, TTSEL:precedes, VTSEL:precedes, TTSEL:follows, VTSEL:follows, TTSEL:contains, VTSEL:contains, TTSEL:overlaps, VTSEL:overlaps .4

Since each A Ž . d1,d2 is a value between zero and one, the weight of each temporal affinity $\omega _ { i }$ , directly represents the relative importance of each temporal affinity. For example, $\omega _ { i }$ can be determined by the frequency of the corresponding query pattern in an application because temporal affinities of more frequent query patterns need to have larger weights than those of less frequent query patterns.

## 5. Performance evaluation

In this section, we show the effectiveness of the proposed temporal affinity compared with other clustering measures, such as the similarity in surrogate<sup>r</sup> transaction time<sup>r</sup>valid time values and the degree of overlapping in transaction<sup>r</sup>valid time.

5.1. An experiment: effectiÕeness of the temporal affinity

We have conducted an experiment that simulates the management of the contract of employment in a company and the benchmark query processing on clustered temporal data objects. The performance of a data clustering method can be represented by the number of disk pages that need to be accessed to process given benchmark queries. We compute the average number of cluster references during the benchmark query processing. We made the total number of clusters equal to the total number of disk pages, and hence the average number of cluster references represents performance of a temporal data clustering method.

We use a synthetic data set for the experiment. Time attribute values of temporal data objects in the data set are random variables with particular distributions. We assume in this experiment that an event that an employee is hired and the contract is recorded into the data base takes a Poisson process. Then the time interval between transaction start time Ts ofŽ . two consecutive versions takes Exponential distribution if Ts denote the times when those events occur.

## 5.1.1. Clustering of temporal data objects: CLARA

The temporal affinity proposed in this paper is a clustering measure that expresses the relative closeness of two data objects numerically. Therefore, we need a clustering algorithm that clusters data objects according to a given measure for the performance experiment of the proposed measure. One simple clustering algorithm may compute the temporal affinity for every pair of data objects. However, this kind of algorithm is computationally intractable due to combinatorial explosion of the search space. Thus, we use Clustering Large Applications CLARA de-Ž . scribed in 6 for our experiment. CLARA, designed <sup>w</sup> <sup>x</sup> by Kaufman and Rousseeuw, takes a set of data objects and a clustering measure as the input arguments, and produces a predetermined number of data clusters on the basis of the given measure. CLARA uses sampling of the underlying set of data object in order to cluster very large data set efficiently.

In general, k data objects, which are the representative objects of each cluster, should be identified in order to group n data objects into k clusters. These objects are called medoid, and correspond to the most centrally located objects within the clusters. On finding k medoids, CLARA reduces the amount of computation by examining a relatively small sized sample of the data set rather than the entire data set. In other words, CLARA avoids computing temporal affinities for all pairs of temporal data objects in the clustering process. In Ref. 6 , it is shown that the <sup>w</sup> <sup>x</sup> time complexity is $O ( k ( 4 0 + k ) ^ { 2 } + k ( n - k ) )$ for n data objects and k clusters.

Table 3  
The benchmark queries and their frequencies

<table><tr><td>Time dimensions of queries</td><td>Transaction time operator</td><td>Valid time operator</td><td colspan="4">Frequencies</td></tr><tr><td rowspan="12">Single time dimensional queries</td><td>as-of</td><td>-</td><td>0.05</td><td>0.25</td><td>0.5</td><td>1</td></tr><tr><td>within</td><td>-</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>precedes</td><td>-</td><td>0.03</td><td></td><td></td><td></td></tr><tr><td>follows</td><td>-</td><td>0.03</td><td></td><td></td><td></td></tr><tr><td>contains</td><td>-</td><td>0.04</td><td></td><td></td><td></td></tr><tr><td>overlaps</td><td>-</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>-</td><td>as-of</td><td>0.05</td><td>0.25</td><td></td><td></td></tr><tr><td>-</td><td>within</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>-</td><td>precedes</td><td>0.03</td><td></td><td></td><td></td></tr><tr><td>-</td><td>follows</td><td>0.03</td><td></td><td></td><td></td></tr><tr><td>-</td><td>contains</td><td>0.04</td><td></td><td></td><td></td></tr><tr><td>-</td><td>overlaps</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td rowspan="8">Bitemporal queries</td><td>as-of</td><td>precedes</td><td>0.05</td><td>0.25</td><td>0.5</td><td></td></tr><tr><td>as-of</td><td>follows</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>as-of</td><td>contains</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>as-of</td><td>overlaps</td><td>0.10</td><td></td><td></td><td></td></tr><tr><td>within</td><td>precedes</td><td>0.05</td><td>0.25</td><td></td><td></td></tr><tr><td>within</td><td>follows</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>within</td><td>contains</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>within</td><td>overlaps</td><td>0.10</td><td></td><td></td><td></td></tr></table>

By using CLARA, we partition temporal data objects into an appropriate number of clusters according to various clustering measures. For this experiment, we make the total number of clusters be the total number of disk pages that is required to contain the whole data objects. In other words, the total number of clusters K is determined by the total number of data objects N, the size of a data object S, and the size of a disk page P such that K<sup>s</sup> u ? @v <sub>N</sub>r <sub>P</sub>r<sub>S .</sub>

## 5.1.2. Benchmark queries and related parameters

The benchmark queries used in the experiment are constructed with the canonical temporal query patterns mentioned before. We use a set of single time dimensional queries and a set of bitemporal queries. For both cases, we assume that two time-slice operators — as-of, within are used only for the transaction time dimension and four temporal comparison operators — precedes, follows, oÕerlaps, contains are used only for the valid time dimension because time-slice operations usually occur in the transaction time dimension for time travels, and temporal comparison operators are mainly specified with the valid time dimension in practice. We also assume that the frequencies of single time dimensional queries and bitemporal queries are the same. Table 3 shows each benchmark temporal query pattern and its frequency in the experiment. We assume that the arguments of the benchmark queries are random variables with uniform distribution. Table 4 shows important parameters used in the experiment and their configuration.

## 5.1.3. Analysis of the results

Table 5 shows the abbreviated names of clustering measures used in the experiments. We compare the proposed clustering measure AF with those other straightforward measures since, as far as we are aware of, there is no well known clustering measure for general TDB processing environment.

Table 4  
The parameters of the experiment

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Time range</td><td>[0, 3650]</td></tr><tr><td>Number of objects (N)</td><td>5000/10,000/50,000/100,000</td></tr><tr><td>Size of an objects (S)</td><td>30/50/100/200/300 bytes</td></tr><tr><td>Page size (P)</td><td>4 kbytes</td></tr><tr><td>Number of clusters</td><td> $K = \lceil N/\lfloor P/S \rceil \rceil$ </td></tr><tr><td>Number of total benchmark query executions</td><td>1000</td></tr></table>

Table 5  
Clustering measures used in the experiment

<table><tr><td>Name</td><td>Clustering measure</td></tr><tr><td>KEY</td><td>The surrogate value</td></tr><tr><td>TTS</td><td>The similarity in transaction start time (Ts)</td></tr><tr><td>VTS</td><td>The similarity in valid start time (Vs)</td></tr><tr><td>TTO</td><td>The degree of overlapping in transaction time intervals</td></tr><tr><td>VTO</td><td>The degree of overlapping in valid time intervals</td></tr><tr><td>AF</td><td>The temporal affinity</td></tr></table>

The experimental results are given in Table 6. The table shows the average number of cluster references per benchmark query that corresponds to the average number of disk accesses per benchmark query in our experiments.

The results are obtained by varying the total number of data objects Ž . N and the size of an object Ž . S . We repeat the same experiment 12 times and compute the average of 10 values. We take out the maximum value and the minimum value for more reliable results. We think that by conducting the same experiment more than 10 times, the uncertainty caused by the sampling-based clustering algorithm used in the experiments can be minimized.

In the following Figs. 13–15, we present various performance results from the experiments. They show that the best performance is achieved by using the proposed temporal affinity in all the cases. Fig. 13 shows the average number of cluster references per benchmark query when $N = 1 0 0 { , } 0 0 0 .$ In the figure, the increasing value of Number of Clusters, i.e., the x-coordinate means that for the given number of data objects N, we need an increasing number of disk pages due to an increasing value of the size of a data object. We can observe that less numbers of cluster references, that is, less numbers of disk page accesses are required by using AF than other clustering measures on temporal query processing. Note that the figure does not show the performance of KEY that is the typical data clustering measure for conventional databases. This is because KEY works so badly for temporal query processing that the number of cluster references for KEY go beyond the boundary of the figure. For example, when the number of clusters is 2500 the number of cluster references for KEY is 261.3214. The performance of VTS is a little better than that of KEY but it also go beyond the boundary of the figure.

Table 6  
Average number of cluster references

<table><tr><td rowspan="2">Number of objects (N)</td><td rowspan="2">Clustering method</td><td colspan="5">Size of an object (S)</td></tr><tr><td>30</td><td>50</td><td>100</td><td>200</td><td>300</td></tr><tr><td rowspan="5">5000</td><td>AF</td><td>6.0138</td><td>8.1963</td><td>9.9274</td><td>11.8371</td><td>14.0227</td></tr><tr><td>TTS</td><td>7.9231</td><td>12.8102</td><td>14.0037</td><td>22.4478</td><td>25.4032</td></tr><tr><td>VTS</td><td>10.7831</td><td>14.7195</td><td>21.4152</td><td>29.5773</td><td>34.7333</td></tr><tr><td>TTO</td><td>7.1002</td><td>10.0112</td><td>13.1302</td><td>17.0332</td><td>21.0182</td></tr><tr><td>VTO</td><td>7.2087</td><td>10.1031</td><td>14.8761</td><td>18.9071</td><td>22.3530</td></tr><tr><td rowspan="5">10,000</td><td>AF</td><td>6.7416</td><td>9.2187</td><td>13.0193</td><td>17.8190</td><td>21.1338</td></tr><tr><td>TTS</td><td>12.5341</td><td>16.0703</td><td>24.4793</td><td>29.3049</td><td>36.4849</td></tr><tr><td>VTS</td><td>16.2788</td><td>22.7593</td><td>33.5147</td><td>46.1629</td><td>52.3493</td></tr><tr><td>TTO</td><td>9.2098</td><td>13.0002</td><td>17.9311</td><td>25.4042</td><td>29.0053</td></tr><tr><td>VTO</td><td>10.0175</td><td>13.6694</td><td>18.3917</td><td>27.6654</td><td>28.9491</td></tr><tr><td rowspan="5">50,000</td><td>AF</td><td>18.1961</td><td>20.3008</td><td>26.8381</td><td>35.4073</td><td>43.7331</td></tr><tr><td>TTS</td><td>28.9014</td><td>33.2759</td><td>45.5850</td><td>53.2884</td><td>69.9045</td></tr><tr><td>VTS</td><td>48.2473</td><td>57.4623</td><td>82.1416</td><td>105.3862</td><td>120.2427</td></tr><tr><td>TTO</td><td>24.6032</td><td>27.0008</td><td>37.4493</td><td>45.8044</td><td>62.3320</td></tr><tr><td>VTO</td><td>25.5091</td><td>29.4143</td><td>38.9893</td><td>47.6686</td><td>64.2810</td></tr><tr><td rowspan="6">100,000</td><td>AF</td><td>26.0083</td><td>27.1870</td><td>34.1792</td><td>48.1312</td><td>58.0471</td></tr><tr><td>TTS</td><td>34.9071</td><td>39.6601</td><td>53.3038</td><td>77.6103</td><td>96.0019</td></tr><tr><td>VTS</td><td>63.4208</td><td>89.8035</td><td>127.1227</td><td>168.4137</td><td>187.6794</td></tr><tr><td>TTO</td><td>28.8492</td><td>35.9821</td><td>44.3533</td><td>67.2021</td><td>79.9917</td></tr><tr><td>VTO</td><td>30.3731</td><td>36.5911</td><td>49.0427</td><td>75.6115</td><td>84.3739</td></tr><tr><td>KEY</td><td>78.6571</td><td>153.3342</td><td>261.3214</td><td>354.0892</td><td>391.1975</td></tr></table>

![](/api/attachments/7GE64ED3/fulltext/images/db1039d0ee9a4a256740bd1914b8a562352b3325a6b600e0a870465b2b3ba1e2.jpg)  
Fig. 13. Performance when $N = 1 0 0 { , } 0 0 0 .$

Fig. 14 shows the performance difference between the proposed clustering measure and others. The performance difference between AF and KEY is not considered because KEY works so badly that it is meaningless to present the difference between them. In the figure, we can observe that the difference in the number of cluster references becomes larger as the number of clusters increases. This means that the effectiveness of a data clustering measure becomes more important as the size of database increases.

In the experimental results, performance based on transaction time — i.e. TTS and TTO — are better than those based on valid time — i.e. VTS and

![](/api/attachments/7GE64ED3/fulltext/images/2c3371f876e5ac5533df9b8ee7270c5efb8b31b5e366d8c7b41d8a71b4174dfe.jpg)  
Fig. 14. Performance advantage of AF over others when $N =$ 100,000.

![](/api/attachments/7GE64ED3/fulltext/images/ae7bd8e035af8419f631f5672a1a036d61aed8bfdcced8c52ea67310ab15e6eb.jpg)  
Fig. 15. Performance of clustering methods for dynamic environment: $N = 1 0 0 { , } 0 0 0 ,$ $N _ { 0 } = 5 0 { , } 0 0 0 .$ $\rho _ { \mathrm { o } } = 0 . 5 ,$ , and $S = 2 0 0 .$

VTO. This observation can be explained by the properties of the benchmark queries. We can notice that transaction time is more dominant clustering factor than valid time for the benchmark queries used in the experiment. The result is due to the fact that some of the temporal comparison operators used in the valid time dimension have countervailing effect with each other. In other words, the larger is the possibility that two temporal data objects are selected together by a query with precedes operator, the smaller is the possibility that they are selected together by a query with follows operator. Also, we can observe that the degree of overlapping in valid<sup>r</sup>transaction time intervals is more dominant factor than the valid<sup>r</sup>transaction start time from the fact that TTO and VTO outperform TTS and VTS, respectively.

Now, let us consider the computing time of clustering temporal data objects based on the proposed temporal affinity. If we compute a temporal affinity for each pair of two temporal data objects, the time complexity becomes roughly $O ( n ^ { 2 } )$ where n is the total number of data objects. Since n may be orders of 100,000 to 1,000,000 in practice, $O ( n ^ { 2 } )$ computing time may be a serious overhead. However, by using an appropriate sampling technique as in CLARA, the computing time is considerably reduced while achieving a significant performance advantage as shown in Figs. 13 and 14. For example, it took 93 min to compute temporal affinities and determine the proper clusters of all the data objects for AF in Fig. 13, where SUN Enterprise 3000 system with 4 168 MHz UltraSPARC CPUs and 1 GBytes main memory is used. Though we may need additional $I / O$ cost for placement of data objects in disk, we think that clustering temporal data objects based on the proposed temporal affinity must be a viable alternative to simple and straightforward placement of temporal data.

## 5.2. Temporal data clustering in dynamic enÕironment

In the previous experiment, we have examined the effectiveness of the temporal affinity as a measure for temporal data clustering where a collection of temporal data objects is given. Now, consider the case when a number of new temporal data objects are inserted into the database. An insertion of a new temporal data object may require non-negligible computing time and may cause relocation of other existing temporal data objects. To avoid frequent relocation of the existing data and reduce the computing time, we take the following strategy.

v Initially, data objects are clustered into disk pages by using CLARA up to a predetermined load factor of the disk page.

v After the initial clustering, a new data object inserted is allocated to the disk page that has empty space and gives the best temporal affinity value between the inserted data object and the medoid of the disk page. The medoid of a disk page P is the representative data object of P, that is the most centrally located data object within P. The medoids for each disk page, i.e. each cluster, are determined in CLARA.

v When the load factors of all disk pages reach near one, the database is reclustered as in the previous section by using CLARA.

In this way, though the placement may not be optimal with respect to the proposed temporal affinity, newly inserted temporal data objects are easily placed into an appropriate disk page without much computation overhead while minimizing the relocation of the existing data. Note that the time attribute values of the medoids and page load factors are easily maintained in main memory.

We perform an experiment to show that the temporal affinity works well for such a dynamic environment. In the experiment, the total number of data objects is 100,000, and the half of them is stored on the database initially. Hence, the 50,000 objects are clustered with initial average load factor $\rho _ { \mathrm { o } } = 0 . 5 ,$ and all the disk pages are almost half full after the initial clustering. Subsequently, we insert the remaining 50,000 data objects one by one, and the benchmark queries are processed whenever the average disk page load factor increases by 0.1. Fig. 15 shows the numbers of cluster references that are observed in the experiment.

As in the figure, the performance based on AF is better than those based on other clustering measures. The experimental result shows that a clustering method based on the temporal affinity can be exploited effectively even in the circumstance where the size of database increases significantly.

## 6. Conclusion

In this paper, data clustering issues in TDBs have been addressed. Since TDB systems maintain a huge amount of data objects, an efficient clustering of underlying data objects is essential to guarantee fast query response time. A clustering method in a database system requires a proper clustering criterion and an effective measure for the criterion. The clustering measure is a basis of the decision on the selection of data objects to be clustered together. However, clustering measures for conventional databases are not appropriate to TDBs because it is crucial to exploit temporal properties of queries and underlying data objects on temporal data clustering. Temporal queries include time condition that is one of the most effective filtering conditions in temporal query processing. Therefore, a temporal data clustering method should be based on the characteristics of the time condition.

In this work, we have proposed a clustering measure, called temporal affinity, that can be used in temporal data clustering. The temporal affinity reflects the closeness of temporal data objects with respect to temporal query processing. First, we have identified typical temporal query patterns, called canonical temporal queries. The temporal affinity for each canonical temporal query pattern has been defined and the validity of the proposed temporal affinity is also shown. Then we have discussed the integration of the temporal affinities to apply them for temporal data clustering method. We have also conducted experiments in order to evaluate the effectiveness of the temporal affinity. The experimental results have shown that our proposed temporal affinity is more effective than other clustering measures.

## Acknowledgements

This work was supported by grant no. 1999-1- 303-007-3 from the interdisciplinary research program of the KOSEF.

## References

1 I. Ahn, R. Snodgrass, Partitioned storage for temporal databases, Information Systems 13 4 1988 369–391.Ž . Ž .

2 J. Gray, A. Reuter, Transaction Processing: Concepts and Techniques, Morgan-Kaufmann Publishers, 1993.

<sup>w</sup> <sup>x</sup> 3 H. Gunadhi, A. Segev, Query processing algorithms for temporal intersection join, Proceedings of the 7th ICDE, 1991, pp. 336–344.

<sup>w</sup> <sup>x</sup> 4 C. Jensen, J. Clifford, S. Gardia et al., A consensus glossary of temporal database concepts, ACM SIGMOD Record 23 Ž . Ž .1 1994 .

<sup>w</sup> <sup>x</sup> 5 C. Jensen, M. Soo, R. Snodgrass, Unifying temporal data model via a conceptual model, Information Systems 19 7Ž . Ž . 1994 513–547.

<sup>w</sup> <sup>x</sup> 6 L. Kaufmann, P.J. Rousseeuw, Finding Groups in Data: an Introduction to Cluster Analysis, Wiley, 1990.

<sup>w</sup> <sup>x</sup> 7 H. Lu, B. Ooi, K. Tan, On spatially partitioned temporal join, Proceeding of the 20th VLDB Conference, 1994, pp. 546– 557.

<sup>w</sup> <sup>x</sup> 8 D. Rotem, A. Segev, Physical organization of temporal data, Proceedings of the 3rd ICDE, 1987, pp. 547–553.

9 B. Salzberg, V.J. Tsotras, A Comparison of Access Methods for Time Evolving Data. Technical Report NU-CCS-94.21, 1994.

<sup>w</sup> <sup>x</sup> 10 R. Snodgrass, I. Ahn, G. Ariav et al., TSQL2 language specification, ACM SIGMOD Record 23 1 1994 65–86.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 J. Won, R. Elmasri, Representing retroactive and proactive versions in bi-temporal databases 2TDB , Proceedings of theŽ . 12th ICDE, 1996, pp. 85–94.

![](/api/attachments/7GE64ED3/fulltext/images/b57e3f2b983983f612bc8fc1888f06b00868d8cfb3e09dc332a409138a89f8b9.jpg)  
Jong Soo Kim received his BS and MS degree in Computer Science from Korea Advanced Institute of Science and Technology KAIST , Taejon, Korea, in 1995Ž . and 1997, respectively. Currently, he is a PhD student of Computer Science at KAIST. His current interests are temporal databases, OLAP, and information retrieval in WWW environment.

![](/api/attachments/7GE64ED3/fulltext/images/e4983c04e95fa03eac34bf68e0479f1d93242d3e5bddcbcd99b3f636a5183b10.jpg)

Myoung Ho Kim received his BS and MS degrees in Computer Engineering from Seoul National University, Seoul, Korea, in 1982 and 1984, respectively, and his PhD degree in Computer Science from Michigan State University, East Lansing, MI, in 1989. In 1989, he joined the faculty of the Department of Computer Science at KAIST, Taejon, Korea, where currently he is a professor. His research interests include database systems, OLAP, mobile computing, data

mining, information retrieval and distributed processing. He is a member of the ACM and the IEEE Computer Society.
