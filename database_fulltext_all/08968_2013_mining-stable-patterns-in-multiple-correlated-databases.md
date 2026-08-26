---
otero_id: 8968
otero_key: "8T336NTT"
title: "Mining stable patterns in multiple correlated databases"
authors: "Yaojin Lin; Xuegang Hu; Xiaomei Li; Xindong Wu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.06.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Yaojin Lin <sup>a,b,</sup>⁎, Xuegang Hu <sup>a,</sup>⁎, Xiaomei Li <sup>a</sup>, Xindong Wu <sup>c</sup>

<sup>a</sup> School of Computer Science and Information Engineering, Heifei University of Technology, Hefei 230001, PR China

<sup>b</sup> Department of Computer Science and Engineering, Zhangzhou Normal University, Zhangzhou 363000, PR China

<sup>c</sup> Department of Computer Science, University of Vermont Burlington, VT 05405, USA

## a r t i c l e i n f o

Article history: Received 20 February 2012 Received in revised form 28 September 2012 Accepted 9 June 2013 Available online 20 June 2013

Keywords: Multiple correlated databases Stable patterns Hierarchical clustering Gray relational analysis

## a b s t r a c t

Many kinds of patterns (e.g., association rules, negative association rules, sequential patterns, and temporal patterns) have been studied for various applications, but very little work has been reported on multiple correlated databases that are all relevant. This paper proposes an ef<sup>fi</sup>cient method for mining stable patterns from multiple correlated databases. First, we de<sup>fi</sup>ne the notion of stable items according to two constraint conditions, minsupp and varivalue. We then measure the similarity between stable items based on gray relational analysis, and present a hierarchical gray clustering method for mining stable patterns consisting of stable items. Finally, experiments are conducted on four datasets, and the results of the experiments show that our method is useful and ef<sup>fi</sup>cient.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Every time a customer interacts with a business, there is an opportunity to gain strategic knowledge. Transactional data collected over time contain a wealth of information about customers and their purchasing patterns. Transactional data collected in a single wholesale store over different time periods can be called a transactional time-stamped database, which may be regarded as multiple correlated databases [36]. For example, market basket transactional data and census data for a certain state from different time periods can also form multiple correlated databases. However, very little research on multiple correlated databases has been done so far. As the database changes over time, the inherent knowledge also changes. Thus, the analysis of the support trend of items in multiple correlated databases over time is an important issue. Identifying groups (clusters) of items with similar support trends is helpful to transactional companies for decision making. For example, clustering stable items based on the support trend of items will enable companies to adjust their marketing strategy.

Many companies spend signi<sup>fi</sup>cant resources on collecting and analyzing transactional data. Such analysis might originate from all kinds of applications. On the one hand, many applications are based on inherent knowledge present in a database. Some data mining algorithms often extract different patterns from a database, such as frequent itemsets [4], association rules [5], both positive and negative association rules [30], sequential patterns [6], and persistent rules [22]. On the other hand, with the advances in information and communication technologies, many large organizations transact from multiple branches. Multi-database mining [26,33] thus becomes an important issue in data mining research, in which local pattern analysis [24,31,34] is an effective and ef<sup>fi</sup>cient mining approach. Nevertheless, many of the existing multi-database mining algorithms aimed at multiple databases [11,26,31,33,34] do not consider the time factor, which might be inappropriate for multiple correlated databases mining. Meanwhile, many pattern mining algorithms [5,6,22,30] only apply to single databases and not to multiple databases. Thus, in this paper, we propose an ef<sup>fi</sup>- cient method for mining stable patterns from multiple correlated databases that are all relevant.

Supposing a company collects a huge amount of transactional data on a yearly basis, we make DT the database corresponds to the i-th year, i = 1, 2, …, m. Each of these databases corresponds to a speci<sup>fi</sup>c period of time. Therefore, we call each database a time-stamped database and the set of all these time-stamped databases is called multiple correlated databases. Although there are some studies conducted on time-stamped databases [2,3,21], this differs from multiple correlated database mining. In this research, we will deal with stable items in each time-stamped database. An interesting characteristic of an item is the variation in sales over time. Those items having less variation in sales over time are useful for devising strategies for a company, so it is important to study such items. Thus, a stable item is de<sup>fi</sup>ned as an item that is purchased by the customers more stably than other items within a unit period of time.

After mining all the stable items from multiple correlated databases, the next step is to study the problem of hierarchically clustering items with supports that are closely related over time. This problem is described formally as follows: Given multiple correlated databases, and two constraint conditions to get stable items from multiple correlated databases, we seek to find clusters of items that have similar support change trends and similar sales volumes of stable items in each cluster. The method we will present is illustrated in $\mathrm { F i g . }$ 1. It shows the support trends of four items $i _ { 1 } , i _ { 2 } , i _ { 3 }$ and $i _ { 4 }$ in <sup>fi</sup>ve time-stamped databases, $D T _ { 1 } , \ D T _ { 2 } , \ D T _ { 3 } , \ D T _ { 4 } ,$ and $D T _ { 5 } .$ Although the supports of these four items are different from each other in the same period of time, we observe that the supports of items $i _ { 1 }$ and $i _ { 2 }$ are more similar than for other pairs of items. We say items $i _ { 1 }$ and $i _ { 2 }$ are closely connected with each other over time. Hence, we consider items $i _ { 1 }$ and $i _ { 2 }$ to have similar support trends and our algorithms return a cluster containing items $i _ { 1 }$ and $i _ { 2 }$ <sup>fi</sup>rst. In this paper, we divide a large database into a sequence of yearly databases. In this context, all the yearly databases can be considered as multiple correlated databases.

According to the varying trends of an item over time, we can classify items into <sup>fi</sup>ve types: (1) stable items—items whose supports are stable over time in a speci<sup>fi</sup>ed duration; (2) popular items—items whose supports are increasing over time in a speci<sup>fi</sup>ed duration; (3) dull items— items whose supports are decreasing over time in a speci<sup>fi</sup>ed duration; (4) periodic items—items whose supports periodically change over time in a speci<sup>fi</sup>ed duration; and (5) general items—items whose supports change irregularly over time in a speci<sup>fi</sup>ed duration. Generally speaking, the minimum duration depends on market need. For example, if marketers want to make a decision based on the last 5 years, the minimum duration is 5 years. In this paper, we present a method for mining stable patterns based on stable items. The proposed method also works for mining popular patterns (popular items-based) and dull patterns (dull items-based), and we only need to apply a slope function instead of the variation function used to measure the degree of variation in the sales volume of a product. Therefore, the method we propose is a typical solution for mining several kinds of patterns.

The remainder of this paper is organized as follows. We discuss related work in Section 2. In Section 3, we brie<sup>fl</sup>y introduce frequent items, hierarchical clustering and gray relational analysis (GRA). We de<sup>fi</sup>ne stable patterns, propose a method to measure similarity between stable items, and cluster stable items hierarchically using our proposed algorithm in Section 4. We present experimental results on four datasets in Section 5. Conclusions are given in Section 6.

## 2. Related work

In management science and decision domains, many methods have been designed to help companies make good decisions [7,8,12]. For association rule mining, the <sup>fi</sup>nal target is not just to <sup>fi</sup>nd the relationships among items, but more interestingly to apply these relationships in practical applications. For example, displaying beer and diapers closed together leads to a several-fold increase in the sales volume of the two commodities.

![](/api/attachments/8T336NTT/fulltext/images/3d10f44a5fba6b0ccff6a66ec2d5c4eb25bea99a2d98a1c0705303c0361b46e1.jpg)  
Fig. 1. The support trends of items.

Mining interesting patterns for various applications has recently become one of the most interesting and popular research topics in the data mining community [1,20,23]. A large number of specialists and scholars have provided a series of methods and techniques for mining all kinds of patterns, such as frequent itemsets [4], association patterns [19], both positive and negative association rules [30], sequential patterns [6], persistent rules [22], and actionable behavioral rules [25]. Since large companies often have multiple branches, many researchers study the problem of mining interesting patterns from multiple databases. Zhang et al. [33] divided the patterns in multiple databases into local patterns, high-vote patterns, exceptional patterns and suggested patterns. Wu et al. [30] advocated a weighting model for synthesizing high-frequency association rules or patterns from different data sources on the basis of data source weights. Zhang et al. [34] proposed a non-linear method that uses kernel estimation for mining global patterns in multiple databases. Adhikari et al. [2] designed an alternative algorithm to <sup>fi</sup>nd the best cluster among items in multiple data sources.

The above research efforts have tackled various important issues in multiple database mining. However, little work has been reported on the area of multiple correlated databases, although many important and useful applications involve transactional time-stamped databases. It is thus meaningful to <sup>fi</sup>nd the relationships among items from continuous time-stamped databases for determining market strategies.

## 3. Preliminaries

In this section, we describe some relevant basic concepts for this problem.

## 3.1. Frequent items

Let $I = \{ i _ { 1 } , i _ { 2 } , . . . , i _ { N } \}$ be a set of N distinct literals called items, and P be a set of transactions over I. Each transaction contains a set of items $i _ { 1 } , i _ { 2 } , . . . , i _ { k } \in I .$ A transaction has an associated unique identi<sup>fi</sup>er called a TIP. In general, a set of items is called an itemset. Each itemset has an associated statistical measure called the support, denoted by supp. For an itemset $A \subset I , s u p p ( A ) = s$ if the fraction of transactions in P containing A equals s.

## 3.2. Clustering

Data clustering has a wide range of applications and has been studied extensively in the data mining community. Traditional clustering algorithms can be categorized into a few classes, e.g., partition-based, hierarchical, density-based, grid-based and model-based algorithms [14]. Hierarchical clustering methods, one popular kind of such algorithms, have sparked wide interest because of their additional advantages and works by grouping data objects into a tree of clusters.

The hierarchical algorithms perform clustering by either merging smaller sub-clusters into a bigger one (an agglomerative method) or dividing a bigger sub-cluster into smaller ones (a divisive method) [17]. There are three representative hierarchical clustering methods, namely, BIRCH (balanced iterative reducing and clustering using hierarchies), CURE (clustering using representatives) and Chameleon (a hierarchical clustering algorithm using dynamic modeling). BIRCH is an integrated hierarchical clustering method that introduces two concepts, clustering feature and clustering feature tree (CF tree), which are used to summarize cluster representations [35]. CURE uses a novel hierarchical clustering algorithm that adopts a middle ground between centroid-based and representative-object-based approaches, and is more robust with respect to outliers [13]. Chameleon is a clustering algorithm that explores dynamic modeling in hierarchical clustering [16]. In its clustering process, two clusters are merged if the interconnectivity and closeness between the clusters are highly related to the internal interconnectivity and closeness of objects within the clusters.

## 3.3. Gray relational analysis

Although there are a number of different ways to compute the similarity between random variables, such as gray relational analysis (GRA), Chi-square, and Pearson's correlation, GRA differs from other coef<sup>fi</sup>cient measure methods. GRA is suitable for small samples, poor information, and uncertainty situations, and does not need a large sample or sample distribution information [9]. Chi-square and Pearson's correlation are suitable for stochastic uncertainty situations, and should usually only be used for large samples. In practical applications, data generally have been collected recently. Thus, GRA is suitable for computing the similarity among stable items from multiple correlated databases.

GRA is a quantitative analysis that explores the similarity and dissimilarity among factors in a developing dynamic process [9]. In recent years, many studies and applications of GRA have appeared [15,18,28,32]. GRA provides a dependency to measure the degree of correlation between factors: the more similarities develop, the more factors correlate. It uses the gray relational grade to measure the relational degree of factors. We describe GRA in more detail below.

Let $X _ { 0 } ^ { ' } = \{ x _ { 0 } ^ { ' } ( k ) | k = 1 , 2 , . . . , n \}$ be the gray reference factor, and $X _ { i } ^ { ' } = \big \{ x _ { i } ^ { \prime } ( k ) | k \stackrel { \sim } { = } 1 , 2 , . . . , n \big \}$ <sup>g</sup>be the gray comparative factor, where $i = 1 , 2 , . . . , m .$ <sup>g</sup>. Before calculating the gray relational grade, one must pre-process the data [19]. To ensure linearity and avoid distorting the data during normalization, we pre-process the data $X _ { 0 } ^ { ' } ,$ , and X<sup>′</sup> $( i = 1 , 2 , . . . , m )$ using Eq. (1):

$$
x _ {j} (k) = \frac {x _ {j} ^ {\prime} (k)}{x _ {j} ^ {\prime} (1)} (k = 1, 2,..., n; j = 0, 1, 2,..., m).\tag{1}
$$

Thus, the gray relational coef<sup>fi</sup>cient between the gray comparative factor and the gray reference factor can be obtained from the following equation:

$$
\begin{array}{l} r (x _ {0} (k) - x _ {i} (k)) \\ = \frac {\underset {i} {\min} \underset {k} {\min} \left| x _ {0} (k) - x _ {i} (k) \right| + \delta \underset {i} {\max} \underset {k} {\max} \left| x _ {0} (k) - x _ {i} (k) \right|}{\left| x _ {0} (k) - x _ {i} (k) \right| + \delta \underset {i} {\max} \underset {k} {\max} \left| x _ {0} (k) - x _ {i} (k) \right|}, \delta \in (0, 1), \end{array}\tag{2}
$$

where δ is a discrimination coef<sup>fi</sup>cient with a value between zero and one. In general, we set $\delta = 0 . 5$ . The gray relational grade can be calculated as follows:

$$
r (X _ {0}, X _ {i}) = \frac {1}{n} \sum_ {k = 1} ^ {n} r (x _ {0} (k), x _ {i} (k)).\tag{3}
$$

The gray relational grade $r ( X _ { 0 } , X _ { i } )$ satis<sup>fi</sup>es the following axioms:

Axiom 1. Normalization: $0 \leq r ( X _ { 0 } , X _ { i } ) \leq 1$ , and $r ( X _ { 0 } , X _ { i } ) = 1$ only if $X _ { 0 } = X _ { i } .$

Axiom 2. Integrity: for $X _ { i } , X _ { j } \in X = \{ X _ { s } | s = 0 , 1 , . . . , m ; m \geq 2 \} ,$ , if $r ( X _ { i } , X _ { j } ) \neq r ( X _ { j } , X _ { i } )$ then $i \neq j$

The cluster results for Example 1.

<table><tr><td>Confidence level  $\lambda$ </td><td>Cluster result</td><td>Confidence level  $\lambda$ </td><td>Cluster result</td></tr><tr><td>1</td><td> $\{x_1\}, \{x_2\}, \{x_3\}, \{x_4\}$ </td><td>0.66955</td><td> $\{x_1,x_2,x_3,x_4\}$ </td></tr><tr><td>0.81814</td><td> $\{x_1,x_2\}, \{x_3\}, \{x_4\}$ </td><td>0.61395</td><td> $\{x_1,x_2,x_3,x_4\}$ </td></tr><tr><td>0.70741</td><td> $\{x_1,x_2\}, \{x_3\}, \{x_4\}$ </td><td>0.59596</td><td> $\{x_1,x_2,x_3,x_4\}$ </td></tr><tr><td>0.67681</td><td> $\{x_1,x_2,x_3,x_4\}$ </td><td></td><td></td></tr></table>

Table 2  
Dataset characteristics.

<table><tr><td>DB</td><td>NT</td><td>ALT</td><td>AFI</td><td>NI</td></tr><tr><td>T10I4D100K</td><td>102,857</td><td>9.82</td><td>1161.2</td><td>999</td></tr><tr><td>Mushroom</td><td>8124</td><td>23.00</td><td>1570.2</td><td>119</td></tr><tr><td>Chess</td><td>3196</td><td>37.00</td><td>1576.7</td><td>75</td></tr><tr><td>Retail</td><td>90,489</td><td>10.04</td><td>55.2</td><td>16,469</td></tr></table>

Axiom 3. Even symmetry: for $X _ { i } , X _ { j } \in X , r ( X _ { i } , X _ { j } ) = r ( X _ { j } , X _ { i } )$ ) if and only $\mathrm { i f } X = \{ X _ { i } , X _ { j } \}$

Axiom 4. Appropinquity: the value of $| x _ { 0 } ( k ) - x _ { i } ( k ) |$ decreases as the value of $r ( x _ { 0 } ( k ) - x _ { i } ( k ) )$ increases.

We now illustrate the use of the gray relational grade by an example.

Example 1. Let $X _ { 1 } = \{ 0 . 2 , 0 . 2 5 , 0 . 2 3 , 0 . 2 2 , 0 . 2 4 \}$ be the reference factor, and $\hat { X _ { 2 } } = \{ 0 . 1 8 , 0 . 2 , 0 . \dot { 1 } 9 , 0 . 1 9 , 0 . 2 \} , \ X _ { 3 } = \{ 0 . \dot { 1 } , 0 . 1 5 , 0 . 1 7 , 0 . 1 2 , 0 . 1 \}$ , and $X _ { 4 } = \{ 0 . 1 2 , 0 . 1 8 , 0 . 1 , 0 . 2 , 0 . 1 \}$ be comparative factors. By Eq. (3), the gray relational grades for each comparative factor to the reference factor are 0.8093, 0.6393, and 0.5545, respectively.

## 4. Mining stable patterns

In this section, we <sup>fi</sup>rst describe some relevant basic concepts for stable patterns. We then construct the similarity matrix of stable items based on GRA. Finally, we present a method for hierarchical gray clustering based on transitivity for clustering stable items.

## 4.1. Stable patterns

A transactional database can be divided into M time-stamped databases according to the transactional time period. Let $D T =$ $\{ D T _ { 1 } , D T _ { 2 } , . . . , D T _ { M } \}$ be a set of M distinct literals called timestamped databases. A set of time-stamped databases is referred to as multiple correlated databases. Each time-stamped database contains a set of variable length transactions over I. Each transaction contains a set of items $i _ { 1 } , i _ { 2 } , . . . , i _ { k } \in I .$

To mine stable items from multiple correlated databases, we de-<sup>fi</sup>ne the following two constraint conditions:

(1) minsupp: The support of each item in a time-stamped database must exceed the pre-speci<sup>fi</sup>ed minimum support (minsupp);

(2) varivalue: The sample variation of the support for each item over multiple correlated databases must be less than the pre-speci<sup>fi</sup>ed threshold value (varivalue).

The objective of the <sup>fi</sup>rst constraint condition is to <sup>fi</sup>nd frequent items i that satisfy supp(i) ≥ minsupp in each time-stamped database. The objective of the second constraint condition is to eliminate items whose supports in each time-stamped database are not stable.

Table 3  
Time-stamped database characteristics.

<table><tr><td>DB</td><td>NT</td><td>ALT</td><td>AFI</td><td>DB</td><td>NT</td><td>ALT</td><td>AFI</td></tr><tr><td> $T_1$ </td><td>20,000</td><td>9.8206</td><td>226.02</td><td> $M_1$ </td><td>1600</td><td>24.0000</td><td>549.25</td></tr><tr><td> $T_2$ </td><td>20,000</td><td>9.8210</td><td>226.55</td><td> $M_2$ </td><td>1600</td><td>24.0000</td><td>477.92</td></tr><tr><td> $T_3$ </td><td>20,000</td><td>9.8454</td><td>227.11</td><td> $M_3$ </td><td>1600</td><td>24.0000</td><td>422.99</td></tr><tr><td> $T_4$ </td><td>20,000</td><td>9.8373</td><td>226.67</td><td> $M_4$ </td><td>1600</td><td>24.0000</td><td>375.51</td></tr><tr><td> $T_5$ </td><td>20,000</td><td>9.7895</td><td>225.82</td><td> $M_5$ </td><td>1600</td><td>24.0000</td><td>432.94</td></tr><tr><td> $C_1$ </td><td>600</td><td>37.0000</td><td>341.54</td><td> $R_1$ </td><td>18,000</td><td>9.8985</td><td>17.99</td></tr><tr><td> $C_2$ </td><td>600</td><td>37.0000</td><td>317.14</td><td> $R_2$ </td><td>18,000</td><td>10.1070</td><td>17.56</td></tr><tr><td> $C_3$ </td><td>600</td><td>37.0000</td><td>312.68</td><td> $R_3$ </td><td>18,000</td><td>9.9239</td><td>17.53</td></tr><tr><td> $C_4$ </td><td>600</td><td>37.0000</td><td>312.68</td><td> $R_4$ </td><td>18,000</td><td>9.6949</td><td>18.07</td></tr><tr><td> $C_5$ </td><td>600</td><td>37.0000</td><td>304.11</td><td> $R_5$ </td><td>18,000</td><td>10.5730</td><td>19.09</td></tr></table>

![](/api/attachments/8T336NTT/fulltext/images/aaebef02e42ce20ffca24e8f1881e4585f4951ca31e6da44e9beb904cff82ba7.jpg)  
Fig. 2. The number of stable items varying with minsupp and varivalue in T10I4D100K.

De<sup>fi</sup>nition 1. Given an item A from multiple correlated databases, suppose that supt(A) is a vector containing the support of item A in each time-stamped database. If supp(A, DT ) ≥ minsupp and variation(supt(A)) ≤ varivalue, then we call item A a stable item.

De<sup>fi</sup>nition 2. Given a con<sup>fi</sup>dence level λ and a set of stable items $B ,$ if the gray similarity of each pair of stable items is greater than $\lambda ,$ then we call the set of stable items B a stable pattern.

## 4.2. Similarity measure between stable items

To measure the similarity among stable items, we <sup>fi</sup>rst construct a gray relational grade matrix (GRGM).

De<sup>fi</sup>nition 3. We construct a gray relational grade matrix R from the gray relational grade $r _ { i j }$ as follows:

$$
R = \left[ \begin{array}{c c c c} r _ {1 1} & r _ {1 2} & \dots & r _ {1 m} \\ r _ {2 1} & r _ {2 2} & \dots & r _ {2 m} \\ \vdots & \vdots & \vdots & \vdots \\ r _ {m 1} & r _ {m 2} & \dots & r _ {m m} \end{array} \right],
$$

where $r _ { i j } ( i , j = 1 , 2 , . . . , m )$ denotes the gray relational grade of the gray comparative factor $X _ { j }$ relative to the gray reference factor $X _ { i \cdot }$

![](/api/attachments/8T336NTT/fulltext/images/d207b9a07344e60db8407823507b42fec9ebf58c959da1d2a6dc8f037351ea67.jpg)  
Fig. 3. The number of stable items varying with minsupp and varivalue in Mushroom.

![](/api/attachments/8T336NTT/fulltext/images/502cfa8ce52bd02f14aa27cffde8979ce515bbbd91750a7b9c2e71cc4e297bda.jpg)  
Fig. 4. The number of stable items varying with minsupp and varivalue in Chess.

De<sup>fi</sup>nition 4. Let $r _ { i j }$ be the gray relational grade of $X _ { j }$ relative to $X _ { i \cdot }$ We de<sup>fi</sup>ne $e _ { i j }$ to be the difference coef<sup>fi</sup>cient between $X _ { j }$ and $X _ { i } ,$ where $\begin{array} { r } { e _ { i j } = \frac { \left| \bar { r _ { i j } } - \bar { r _ { i i } } \right| } { \bar { r _ { i i } } } . } \end{array}$

Thus, we can construct the gray relational grade difference matrix (GRGDM) as follows:

$$
E = \left[ \begin{array}{c c c c} e _ {1 1} & e _ {1 2} & \dots & e _ {1 m} \\ e _ {2 1} & e _ {2 2} & \dots & e _ {2 m} \\ \vdots & \vdots & \vdots & \vdots \\ e _ {m 1} & e _ {m 2} & \dots & e _ {m m} \end{array} \right].
$$

De<sup>fi</sup>nition 5. Let $e _ { i j }$ be the difference coef<sup>fi</sup>cient between $X _ { j }$ and $X _ { i \cdot }$ We de<sup>fi</sup>ne $d _ { i j }$ to be the distance measure between $X _ { j }$ and $X _ { i } ,$ where $\begin{array} { r } { d _ { i j } = e _ { i j } + e _ { j i } . } \end{array}$

Thus, we can construct the gray distance matrix (GDM) as follows:

$$
D = \left[ \begin{array}{c c c c} d _ {1 1} & d _ {1 2} & \dots & d _ {1 m} \\ d _ {2 1} & d _ {2 2} & \dots & d _ {2 m} \\ \vdots & \vdots & \vdots & \vdots \\ d _ {m 1} & d _ {m 2} & \dots & d _ {m m} \end{array} \right].
$$

From this de<sup>fi</sup>nition, one can obtain the following property.

![](/api/attachments/8T336NTT/fulltext/images/2413d1f4f80fd9d426b8b5499c91d5c913369d0fba18bf263e0818f4217c1a90.jpg)  
Fig. 5. The number of stable items varying with minsupp and varivalue in Retail.

![](/api/attachments/8T336NTT/fulltext/images/4b373859957116eb57720fddabfd7cedf28a243618ba71472bc214809ee8647d.jpg)  
Fig. 6. Execution time vs. number of correlated databases obtained from T10I4D100K.

Property 1. For factors $X _ { i } , X _ { j }$ and $X _ { k } ,$ we have

(1) symmetry: $d _ { i j } = d _ { j i } ;$

(2) non-negativity: $d _ { i j } > 0 ;$

(3) triangular inequality: $d _ { i j } + d _ { j k } \geq d _ { i k } .$

De<sup>fi</sup>nition 6. Let $d _ { i j }$ be the distance measure between $X _ { j }$ and $X _ { i \cdot }$ . We de<sup>fi</sup>ne $s _ { i j }$ to be the gray similarity degree between $X _ { j }$ and $X _ { i } ,$ where $s _ { i j } = 1 - d _ { i j } .$

Thus, we can construct the gray similarity degree matrix (GSDM) as follows:

$$
S = \left[ \begin{array}{c c c c} s _ {1 1} & s _ {1 2} & \dots & s _ {1 m} \\ s _ {2 1} & s _ {2 2} & \dots & s _ {2 m} \\ \vdots & \vdots & \vdots & \vdots \\ s _ {m 1} & s _ {m 2} & \dots & s _ {m m} \end{array} \right].
$$

Property 2. For factors $X _ { i } , X _ { j } ,$ we have

(1) reflexivity: $s _ { i i } = 1 ;$

(2) symmetry: $s _ { i j } = s _ { j i } .$

![](/api/attachments/8T336NTT/fulltext/images/563e0e4a2120cebeae2b46d8b19e1b746c8760d6afbe010fa3dc6d6010f5d110.jpg)  
Fig. 7. Execution time vs. number of correlated databases obtained from Mushroom

![](/api/attachments/8T336NTT/fulltext/images/5aa4e16a91fe63bd6b2949e10e0d34fdc2d1dac0cf57caecbb272dad8a054c42.jpg)  
Fig. 8. Execution time vs. number of correlated databases obtained from Chess.

Example 2. (Continued from Example 1). Suppose minsupp = 0.05, varivalue = 0. Constructing the gray similarity degree matrix for factors $X _ { 1 } , X _ { 2 } , X _ { 3 } ,$ , and $X _ { 4 } ,$ , we get

$$
S = \left[ \begin{array}{c c c c} 1 & 0. 8 1 8 1 4 & 0. 6 7 6 8 1 & 0. 5 9 5 9 6 \\ 0. 8 1 8 1 4 & 1 & 0. 6 6 9 5 5 & 0. 6 1 3 9 5 \\ 0. 6 7 6 8 1 & 0. 8 8 9 5 5 & 1 & 0. 7 0 7 4 1 \\ 0. 5 9 5 9 6 & 0. 6 1 3 9 5 & 0. 7 0 7 4 1 & 1 \end{array} \right].
$$

From this example, Property 2 can be veri<sup>fi</sup>ed easily. In practical applications, the gray similarity matrix can be applied to measure the degree of similarity among factors based on the change trends in factors.

Using the above de<sup>fi</sup>nitions and analysis, we design an algorithm for computing the similarity among stable items, presented as Algorithm 1.

In Algorithm 1, we denote by $| D T _ { i } | _ { i } = 1 , 2 , . . . , n$ the number of transactions in the i-th time-stamped database. The time complexity to compute the support of an item in each time-stamped database is $O ( n \times \operatorname* { m a x } ( | D T _ { i } | ) )$ , and the time complexity to construct the gray similarity matrix is $O ( | S | ^ { 2 } )$ , thus, the time complexity of Algorithm 1 is $O ( n \times \operatorname* { m a x } ( | D T _ { i } | ) + | S | ^ { 2 } )$ ).

Algorithm 1 processes items with two constraint conditions, eliminates useless items, and captures the degree of relational similarity among stable items based on the change of trend of item using GRA.

![](/api/attachments/8T336NTT/fulltext/images/f27456aaf302736ce7ae03a5c143260c2e577e37f667a0d5486dc709f03c1191.jpg)  
Fig. 9. Execution time vs. number of correlated databases obtained from Retail.

Table 4 The stable patterns from T10I4D100K where (minsupp = 0.01, varivalue = $1 . 3 3 2 5 * 1 0 ^ { - \hat { 7 } } ) .$

<table><tr><td>Stable patterns</td><td>Confidence level λ</td></tr><tr><td>{130, 649}</td><td>0.8509</td></tr><tr><td>{130, 649}, {171, 265}</td><td>0.8303</td></tr><tr><td>{130, 649}, {171, 265}, {197, 578}</td><td>0.7711</td></tr><tr><td>{130, 649}, {171, 265}, {197, 578}</td><td>0.7487</td></tr></table>

## Algorithm 1. Algorithm for computing the similarity between stable items

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Algorithm for computing the similarity between stable items
Input: n: number of correlated databases;  $DT_{i,i=1,2,\cdots,n}$ : multiple correlated databases; minsupp: the specified value of the minimum support; varivalue: the sample variation of the support for the item over the multiple correlated databases
Output: GSM: grey similarity matrix.
1: for i = 1 to n do
2:    Compute the support of each item in the different databases;
3:    if supp(item,  $DT_{i,i=1,2,\cdots,n}$ ) ≥ minsupp and variation(item) ≥ varivalue then
4:    S ← item;
5:    end if
6: end for
7: for i = 1 to |S| do
8:    for j = 1 to |S| do
9:    GRGM(i,j) = r(S(i), S(j));
10:    end for
11: end for
12: for i = 1 to |S| do
13:    for j = 1 to |S| do
14:    GRGDM(i,j) ←  $\frac{|GRGM(i,j)-GRGM(i,i)|}{GRGM(i,i)}$ ;
15:    GDM(i,j) ← GRGDM(i,j) + GRGDM(j,i);
16:    GSM(i,j) ← 1 - GDM(i,j);
17: end for
18: end for
</div>

## 4.3. Hierarchical clustering of stable items

To bundle high relevant items for sale, we mine stable patterns from the gray similarity matrix in this section. We present an ef<sup>fi</sup>cient hierarchical gray clustering algorithm (HGCA) which references the transitive closure method [27,29]. This clustering algorithm is different from classical hierarchical clustering algorithms, obtaining the dynamic clustering from the gray similarity matrix. The time complexity of the algorithm is smaller than traditional transfer closure method. HGCA works by grouping stable items into a tree of objects, with the number of clusters increasing as the con<sup>fi</sup>dence level increases. Thus the <sup>fi</sup>rst cluster, which is composed of more than two stable items, is the most interesting stable pattern (and has the highest con<sup>fi</sup>dence). We present HGCA in Algorithm 2.

Table 5 The stable patterns from Mushroom where (minsupp = 0.005, varivalue = 0.0135).

<table><tr><td>Stable patterns</td><td>Confidence level λ</td></tr><tr><td>{34, 86}</td><td>0.9994</td></tr><tr><td>{34, 85, 86}</td><td>0.9893</td></tr><tr><td>{34, 85, 86}</td><td>0.9888</td></tr></table>

Algorithm 2. Algorithm for mining stable patterns (HGCA)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Algorithm for mining stable patterns (HGCA)
Input: U: a set of stable items; n: the cardinality of U; λ: confidence level; Q: a queue; S: the similarity matrix of factors.
Output: X: clusters.

1: while  $U \neq \emptyset$  do
2:    for each  $x_{i}$  in U do
3:    $X = \emptyset$ , initialize queue Q;
4:    let j = 0;
5:    while (j &lt; n) do
6:    if  $s(x_{i}, x_{j}) \geq \lambda$ , and  $x_{j} \notin X$  then
7:    $X = X \cup \{x_{j}\}$ , push  $x_{j}$  from queue Q;
8:    $j = j + 1$ ;
9:    end if
10:    end while
11:    if empty(Q) == 1 then
12:    Output cluster result X;
13:    U = U - X;
14:    end if
15:    end for
16:    pop  $x_{i}$  from queue Q;
17: end while
</div>

In Algorithm 2, empty(Q) denotes whether the queue Q is empty, with $e m p t y ( Q ) = = 1$ when Q is empty. The time complexity of Algorithm 2 is $O ( n ^ { 2 } )$ , and the time complexity of the transitive closure method is $O ( n ^ { 3 }$ log n), so the time complexity of HGCA is smaller than the transitive closure method.

After clustering the stable items we want to capture the expected patterns, which are the clusters of highly relevant items. According to the shopping mall bundle sales custom, one selects clusters which are composed of two, three or four stable items as stable patterns in a general way.

Example 3. (Continued from Example 2). We can use HGCA to cluster stable items based on the similarity matrix of factors X , X , X and $X _ { 4 } .$ The results are shown in Table 1.

From Table 1, we see the stable pattern {X1, X2} which consists of the most relevant items $X _ { 1 }$ and $X _ { 2 } .$

## 5. Experiments

We carried out several experiments to study the ef<sup>fi</sup>ciency and effectiveness of our approach. We also show that our algorithm is useful for <sup>fi</sup>nding interesting stable patterns. The hardware platform for our experiments is a PC equipped with 3 G main memory and 2.96 GHz Duo CPU. The software is Windows XP Service Pack 2 and Matlab (Version 7.0).

## 5.1. Four datasets

To test the effectiveness of our method in capturing valid stable patterns, some datasets are downloaded from the Frequent itemset mining dataset repository [10], as outlined in Table 2, where the T10I4D100K database was generated using the generator from the IBM Almaden Quest research group, the Retail database was donated by Tom Brijs and contains the (anonymized) retail market basket data from an anonymous Belgian retail store, and the Mushroom and Chess databases were prepared by Roberto Bayardo from the UCI database repository. To meet the experimental requirements, we select the <sup>fi</sup>rst 100,000 transactions from the database T10I4D100K, the <sup>fi</sup>rst 8000 transactions from the database Mushroom, the <sup>fi</sup>rst 3000 transactions from the database Chess, and the <sup>fi</sup>rst 90,000 transactions from the database Retail. We use DB, NT, ALT, AFI, and NI to denote a database, the number of transactions, the average length of a transaction, the average frequency of an item, and the number of items in the corresponding database, respectively.

The stable patterns from Chess where (minsupp = 0.1, varivalue = 0.001).

<table><tr><td>Stable patterns</td><td>Confidence level λ</td></tr><tr><td>{58, 60}</td><td>0.9763</td></tr><tr><td>{52, 58, 60}</td><td>0.9418</td></tr><tr><td>{29, 52, 58, 60}</td><td>0.9416</td></tr></table>

Table 7  
The stable patterns from Retail where (minsupp = 0.01, varivalue = $1 . 3 4 6 6 * 1 0 ^ { - 6 } ) .$

<table><tr><td>Stable patterns</td><td>Confidence level λ</td></tr><tr><td>{123, 740}</td><td>0.8603</td></tr><tr><td>{123, 301, 740}</td><td>0.7962</td></tr><tr><td>{37, 286}, {123, 301, 740}</td><td>0.7800</td></tr></table>

Suppose one wants to make decisions from transactional data which had been collected during the last 5 years. We divide each of the databases T10I4D100K, Mushroom, Chess, and Retail into <sup>fi</sup>ve time-stamped databases, and set the minimum duration as 5 years. For the purpose of performing the experiments, the time-stamped databases for $i = 1 , 2 , . . . , 5$ obtained from T10I4D100K, Mushroom, Chess, and Retail are denoted by $T _ { i } , M _ { i } , C _ { i } ,$ and $R _ { i } ,$ respectively. Some characteristics of these time-stamped databases are presented in Table 3.

## 5.2. Scalability and efficiency

We conduct a series of experiments to <sup>fi</sup>nd the changes in the number of stable items when minsupp changes and to <sup>fi</sup>nd whether varivalue constraints exist in the T10I4D100K (varivalue = 0 and $\nu a r i \nu a l u e = 7 . 7 8 * 1 0 ^ { - 7 }$ , respectively), Mushroom (varivalue = 0 and varivalue $= 0 . 0 1 .$ , respectively), Chess (varivalue = 0 and $\nu a r i \nu a l u e = 0 . 0 1$ , respectively), and Retail (varivalue = 0 and $\nu a r i \nu a l u e = 1 . 3 5 * 1 0 ^ { - 6 }$ , respectively) datasets. The results are shown in Figs. 2–5. In these <sup>fi</sup>gures, the horizontal and vertical axes represent the minimum support (minsupp) and the number of stable items, respectively. We can conclude that when minsupp increases, the number of stable items decreases, as the number of stable items with no varivalue constraint is greater than the number of stable items with a varivalue constraint. The experimental results are consistent with the actual situation.

Second, to exhibit the scalability and ef<sup>fi</sup>ciency of our approach, we conduct another series of experiments. For the T10I4D100K dataset we set minsupp = 0.01 and $\nu a r i \nu a l u e = 1 . 3 3 * 1 0 ^ { - 7 } ,$ for the Mushroom dataset we set minsupp = 0.005 and varivalue = 0.0135, for the Chess dataset we set minsupp = 0.1 and varivalue = 0.001, and for the Retail dataset we set minsupp = 0.01 and varivalue = 1.35 ∗ 10<sup>−6</sup>. Figs. 6–9 show the results of these experiments, with the horizontal and vertical axes representing the number of correlated databases and the execution time, respectively. We observe in Figs. 6–9 that the execution time decreases as the number of correlated databases increases. This is because the number of stable items increases as the number of correlated databases decreases, and thus the execution time decreases as the number of correlated databases increases. It can be seen from the <sup>fi</sup>gures that regardless of the ef<sup>fi</sup>ciency or the scalability, the desired results can be achieved, i.e., this approach can be applied to more practical projects.

Table 8  
The <sup>fi</sup>rst stable pattern characteristics.

<table><tr><td>Database</td><td>The first stable pattern</td><td>Support</td><td>Gray similarity degree</td></tr><tr><td>T10I4D100K</td><td>{130, 649}</td><td>0.00010</td><td>0.88850</td></tr><tr><td>Mushroom</td><td>{34, 86}</td><td>0.97825</td><td>0.97959</td></tr><tr><td>Chess</td><td>{58, 60}</td><td>0.99833</td><td>0.86670</td></tr><tr><td>Retail</td><td>{123, 740}</td><td>0.00000</td><td>0.83427</td></tr></table>

Table 9  
The <sup>fi</sup>rst 2-frequent itemset characteristics.

<table><tr><td>Database</td><td>The first 2-frequent itemset</td><td>Support</td><td>Gray similarity degree</td></tr><tr><td>T10I4D100K</td><td>{217, 346}</td><td>0.01298</td><td>0.64103</td></tr><tr><td>Mushroom</td><td>{85, 86}</td><td>0.98038</td><td>0.85957</td></tr><tr><td>Chess</td><td>{58, 60}</td><td>0.99833</td><td>0.86670</td></tr><tr><td>Retail</td><td>{39, 48}</td><td>0.32246</td><td>0.66731</td></tr></table>

Finally, we used our algorithm to mine stable patterns. Given minsupp and varivalue, all of the stable patterns can be mined as the con<sup>fi</sup>dence level λ decreases. To demonstrate the validity of our experiments, we observe that three stable patterns are mined from T10I4D100K in Table 4, two stable patterns are mined from Mushroom in Table 5, three stable patterns are mined from Chess in Table 6, and three stable patterns are mined from Retail in Table 7. Each item in these stable patterns denotes a goods item, and all the items in one stable pattern denote a sales association of these goods items.

## 5.3. Experimental analysis

Having presented the problem in Section 1, we now evaluate the effectiveness of our approach in this section. First, we compare our proposed approach with the Apriori algorithm [5]. Table 8 shows the characteristics of the <sup>fi</sup>rst stable pattern mined by our proposed approach, and Table 9 shows the characteristics of the <sup>fi</sup>rst 2-frequent itemset mined by Apriori. Here we see that the <sup>fi</sup>rst stable pattern is not always the same as the <sup>fi</sup>rst 2-frequent itemset, and that the gray similarity degree of the <sup>fi</sup>rst stable pattern is always higher than that for the <sup>fi</sup>rst 2-frequent itemset. In addition, to exhibit changes in the trend of the support for an item in each time-stamped database, we also conduct a series of experiments. Figs. 10–12 show that the similarity of curves between the items in the <sup>fi</sup>rst stable patterns is greater than for the frequent items in the <sup>fi</sup>rst 2-frequent itemset. There is no <sup>fi</sup>gure for Chess because the <sup>fi</sup>rst stable pattern is the same as the <sup>fi</sup>rst 2-frequent itemset. Thus, the proposed method is feasible for mining stable patterns from multiple correlated databases.

We analyzed the stable patterns mined by our algorithms, which are the expected stable patterns and the clusters of items found to be relevant over time. For T10I4D100K, {130, 649} is the <sup>fi</sup>rst stable pattern, for Mushroom, {34, 86} is the <sup>fi</sup>rst stable pattern, for Chess, {58, 60} is the <sup>fi</sup>rst stable pattern, and for Retail, {123, 740} is the <sup>fi</sup>rst stable pattern. Such correlated patterns are expected since they are related hermetically over time. Using our algorithms to <sup>fi</sup>nd all such patterns is meaningful, since it provides useful information for resource optimization (e.g., bundle sales).

![](/api/attachments/8T336NTT/fulltext/images/d56d23dcd24af54bbca354c904e2e171f86c3755a17dd9bab5c0bdefb433afed.jpg)  
Fig. 10. The support of the <sup>fi</sup>rst stable item {130, 649} vs. the <sup>fi</sup>rst 2-frequent item {217, 346} in T10J4D100K

![](/api/attachments/8T336NTT/fulltext/images/81c376ebc410b49ccb2fd75f289ec0bbffac308a86b97a344dab360769fe7aec.jpg)  
Fig. 11. The support of the <sup>fi</sup>rst stable item {34, 86} vs. the <sup>fi</sup>rst 2-frequent item {85, 86} in Mushroom.

## 6. Conclusions

According to the varying trends of items over time, it is important to mine valuable patterns for marketing decisions. In this work, we have proposed a method for mining stable patterns in multiple correlated databases. First, we set two constraint conditions to determine stable items from multiple correlated databases. In addition, we construct a gray similarity degree matrix of stable items according to the support trends of stable items, and propose a hierarchical gray clustering algorithm to mine stable patterns. Finally, experimental results for four datasets show that the proposed method is feasible, ef<sup>fi</sup>cient, and provides a basis for further research in this <sup>fi</sup>eld.

## Acknowledgments

We sincerely thank the anonymous reviewers and the editors of the special issue for their constructive suggestions, which helped improve the quality of this paper vastly. This work is supported in part by the National 863 Program of China under grant 2012AA011005, the National 973 Program of China under grant 2013CB329604, the Natural Science Foundation of China (under grants 61273292, 61229301, 71140004, 61170129), the Education Department of Fujian Province under grant JA12220, and the US National Science Foundation (NSF) under grant CCF-0905337.

![](/api/attachments/8T336NTT/fulltext/images/26247a51aef403355a17c0cbfa79bd10d40c24131ce452f7fd4064361864797b.jpg)  
Fig. 12. The support of the <sup>fi</sup>rst stable item {123, 740} vs. the <sup>fi</sup>rst 2-frequent item {39, 48} in Retail.

## References

[1] A. Achar, S. Laxman, P.S. Sastry, A uni<sup>fi</sup>ed view of the Apriori-based algorithms for frequent episode discovery, Knowledge and Information Systems 31 (2) (2012) 223–250.

[2] J. Adhikari, P.R. Rao, A. Adhikari, Clustering items in different data sources induced by stability The International Arab Journal of Information Technology 6 (4) (2009) 394–402.

[3] J. Adhikari, P.R. Rao, Measure in<sup>fl</sup>uence of an item in a database over time, Pattern Recognition Letters 31 (1) (2010) 179–187.

[4] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Proceedings of the ACM SIGMOD International Conference on Management of Data, (SIGMOD '93), Washington DC, ACM New York, NY, USA, 1993, pp. 207–216.

[5] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of International Conference on Very Large Data Bases, Santiago, Chile, 1994, pp. 487–499.

[6] R. Agrawal, R. Srikant, Mining sequential patterns, Proceedings of the Eleventh International Conference on Data Engineering, 1995, pp. 3–4.

[7] H.K. Bhargava, R.R. Chen, The bene<sup>fi</sup>t of information asymmetry: when to sell to informed customers? Decision Support Systems 53 (2) (2012) 345–356.

[8] S.L. Chan, W.H. Ip, A dynamic decision support system to predict the value of customer for new product development, Decision Support Systems 52 (1) (2011) 178–188.

[9] J.L. Deng, Introduction of grey system theory, Journal of Grey System 1 (1) (1989) 1–24. [10] Frequent itemset mining dataset repository, http://<sup>fi</sup>mi.ua.ac.be/data/.

[12] N.F. Granados, A. Gupta, R.J. Kauffman, Designing online selling mechanisms: transparency levels and prices, Decision Support Systems 45 (3) (2008) 729–745.

[13] S. Guha, R. Rastogi, K. Shim, CURE: an ef<sup>fi</sup>cient clustering algorithm for large databases, Proceedings of the International Conference on Management of Data, ACM SIGMOD, Seattle, Washington, USA, June 1998, pp. 73–84.

[14] J.W. Han, M. Kamber, Data Mining: Concepts and Techniques, second ed. Morgan Kaufmann, 2005.

[15] S.J. Huang, N.H. Chiu, L.W. Chen, Integration of the grey relational analysis with genetic algorithm for software effort estimation, European Journal of Operational Research 188 (3) (2008) 898–909.

[16] G. Karypis, E.H. Han, V. Kumar, Chameleon: hierarchical clustering using dynamic modeling IEEE Computer 32 (8) (1999) 68-75.

[17] L. Kaufman, P.J. Rousseeuw, Finding Groups in Data: An Introduction to Cluster Analysis, second edition Wiley-Interscience, 2005.

[18] C.Y. Kung, K.L. Wen, Applying grey relational analysis and grey decision-making to evaluate the relationship between company attributes and its <sup>fi</sup>nancial performance—a case study of venture capital enterprises in Taiwan, Decision Support Systems 43 (3) (2007) 842–852.

[19] B.K. Ehlmann, Association patterns for data modeling and de<sup>fi</sup>nition, Knowledge and Information Systems 26 (1) (2011) 59–86

[20] H.Y. Liu, Y. Lin, J.W. Han, Methods for mining frequent items in data streams: an overview, Knowledge and Information Systems 26 (1) (2011) 1–30.

[21] W.-K. Loh, S. Mane, J. Srivastava, Mining temporal patterns in popularity of web items, Information Sciences 181 (22) (2011) 5010–5028.

[22] K. Rajasethupathy, A. Scime, K.S. Rajasethupathy, G.R. Murray, Finding “persistent rules”: combining association and classi<sup>fi</sup>cation results, Expert Systems with Applications 36 (3) (2009) 6019–6024.

[23] A. Salam, M.H. Khayal, Mining top-k frequent patterns without minimum support threshold, Knowledge and Information Systems 30 (1) (2012) 57–86.

[24] K.L. Su, H.J. Huang, X. Wu, et al., A logical framework for identifying quality knowledge from different data sources, Decision Support Systems 42 (3) (2006) 1673–1683.

[25] P. Su, W.J. Mao, D. Zeng, et al., Mining actionable behavioral rules, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.04.013.

[26] K. Tang, Y.L. Chen, H.W. Hu, Context-based market basket analysis in a multiplestore environment, Decision Support Systems 45 (1) (2008) 150–163.

[27] S. Warshall, A theorem on Boolean matrices, Journal of the ACM 9 (1962) 11–12.

[28] G.W. Wei, GRA method for multiple attribute decision making with incomplete weight information in intuitionistic fuzzy setting, Knowledge-Based Systems 23 (1) (2010) 243–247.

[29] F.B. Wu, Q. Li, W.Z. Song, Transfer algorithm to fuzzy clustering analysis, Journal of Southeast University 29 (2) (1999) 1–6.

[30] X. Wu, C.Q. Zhang, S.C. Zhang, Ef<sup>fi</sup>cient mining of both positive and negative association rules, ACM Transactions on Information Systems 22 (3) (2004) 381–405.

[31] X. Wu, S.C. Zhang, Synthesizing high-frequency rules from different data sources, IEEE Transactions on Knowledge and Data Engineering 15 (2) (2003) 353–367.

[32] L.Y. Zhai, L.P. Khoo, Z.W. Zhong, Design concept evaluation in product development using rough sets and grey relation analysis, Expert Systems with Applications 36(5)(2009).7072-7079

[33] S.C. Zhang, C.Q. Zhang, X. Wu, Knowledge Discovery in Multiple Databases, Springer New York 2004

[34] S.C. Zhang, X.F. You, Z. Jin, et al., Mining globally interesting patterns from multiple databases using kernel estimation, Expert Systems with Applications 36 (8) (2009) 10863–10869.

[35] T. Zhang, R. Ramakrishnan, M. Livny, BIRCH: an ef<sup>fi</sup>cient data clustering method for very large databases, Proceedings of the International Conference on Management of Data, ACM SIGMOD, Montreal, Canada, June 1996, pp. 103–144.

[36] X.Q. Zhu, B. Li, X. Wu, et al., CLAP: collaborative pattern mining for distributed information systems, Decision Support Systems 52 (1) (2011) 40–51.

Yaojin Lin received an MS degree in Systems Engineering from Xiamen University. He currently is a Ph.D. student in Hefei University of Technology, and a lecturer in the Department of Computer and Engineering, Zhangzhou Normal University. His research interests include data mining and granular computing.

Xuegang Hu received a Ph.D. degree in Computer and Science from Hefei University of Technology in 2000. He currently is a professor of Computer Science at Hefei University of Technology. His research interests include data mining and knowledge engineering. He has published more than 100 papers in many journals, such as ACM Transactions on Intelligent Systems and Technology, Neurocomputing, International Journal of Data Mining and Bioinformatics, Cybernetics and Systems, and Journal of Computer Science and Technology.

Xiaomei Li is currently a Ph.D. student in the Hefei University of Technology. Her research interests include data mining and bioinformatics.

Xindong Wu is a Professor of Computer Science at the University of Vermont (USA), and a Fellow of the IEEE. He holds a Ph.D. in Arti<sup>fi</sup>cial Intelligence from the University of Edinburgh, Britain. His research interests include data mining, knowledge-based systems, and Web information exploration. He has published over 200 refereed papers as well a 25 books and conference proceedings in these areas. His research has been supported by the U.S. National Science Foundation (NSF), the U.S. Department of Defense (DOD), the National Natural Science Foundation of China (NSFC), and the Chinese Academy of Sciences, as well as industrial companies including Microsoft Research, U.S. West Advanced Technologies and Impact Solutions.

Dr. Wu is the founder and current Steering Committee Chair of the IEEE International Conference on Data Mining (ICDM), the founder and current Editor-in-Chief of Knowledge and Information Systems (KAIS, by Springer), the Founding Chair (2002–2006) of the IEEE Computer Society Technical Committee on Intelligent Informatics (TCII), and a Series Editor of the Springer Book Series on Advanced Information and Knowledge Processing (AI&KP). He was the Editor-in-Chief of the IEEE Transactions on Knowledge and Data Engineering. He served as Program Committee Chair/Co-Chair for the 2003 IEEE International Conference on Data Mining, the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, and the 19th ACM Conference on Information and Knowledge Management.
